# Daily Scheduler 实现计划

> **对于 agent 型执行者：** 必需子 skill：优先使用 `superpowers-subagent-driven-development`，否则使用 `superpowers-executing-plans` 逐任务实施本计划。所有步骤使用 `- [ ]` 复选框格式追踪。

**目标：** 让容器内的 `weekly-gen` 服务每天按 `Asia/Shanghai` 时区在 `09:00` 自动执行一次与 `/run-now` 相同的抓取逻辑，同时保留手动触发接口和现有 interval 模式。

**架构：** 在现有 `JobScheduler` 内增加按模式调度能力。`interval` 模式保持现状，`daily` 模式基于时区和目标时间计算下一次触发时刻；FastAPI 层只负责读取环境变量、暴露状态和启动调度器。

**技术栈：** Python 3.12、FastAPI、asyncio、Docker Compose、uv、pytest

---

### 任务 1: 为 daily 调度补单元测试

**文件：**
- 创建： `tests/test_scheduler.py`
- 参考： `app/scheduler.py`

- [ ] **步骤 1: 编写用于 daily 调度的失败测试**

```python
from datetime import datetime
from zoneinfo import ZoneInfo

from app.scheduler import JobScheduler


def test_compute_next_daily_run_same_day_before_target():
    scheduler = JobScheduler(
        schedule_mode="daily",
        schedule_time="09:00",
        schedule_timezone="Asia/Shanghai",
    )

    now = datetime(2026, 4, 10, 8, 30, tzinfo=ZoneInfo("Asia/Shanghai"))
    result = scheduler._compute_next_run_at(now)

    assert result.isoformat() == "2026-04-10T09:00:00+08:00"


def test_compute_next_daily_run_next_day_after_target():
    scheduler = JobScheduler(
        schedule_mode="daily",
        schedule_time="09:00",
        schedule_timezone="Asia/Shanghai",
    )

    now = datetime(2026, 4, 10, 9, 1, tzinfo=ZoneInfo("Asia/Shanghai"))
    result = scheduler._compute_next_run_at(now)

    assert result.isoformat() == "2026-04-11T09:00:00+08:00"
```

- [ ] **步骤 2: 运行测试验证当前实现失败**

运行：`uv run pytest tests/test_scheduler.py -q`

预期：失败，提示 `JobScheduler` 不接受 `schedule_mode` 等参数，或缺少 `_compute_next_run_at`

- [ ] **步骤 3: 再补一条 interval 模式兼容性测试**

```python
from app.scheduler import JobScheduler


def test_interval_mode_does_not_require_schedule_time():
    scheduler = JobScheduler(interval_seconds=300, schedule_mode="interval")
    assert scheduler.schedule_mode == "interval"
    assert scheduler.interval_seconds == 300
```

- [ ] **步骤 4: 再次运行测试，确认失败集中在新功能缺失**

运行：`uv run pytest tests/test_scheduler.py -q`

预期：失败，但失败原因只和新增调度功能有关

### 任务 2: 在调度器中实现 daily 模式

**文件：**
- 修改： `app/scheduler.py`
- 测试： `tests/test_scheduler.py`

- [ ] **步骤 1: 扩展调度状态数据结构**

把 `RunState` 增加下面字段：

```python
schedule_mode: str = "interval"
schedule_time: Optional[str] = None
schedule_timezone: Optional[str] = None
next_scheduled_at: Optional[str] = None
```

- [ ] **步骤 2: 扩展 `JobScheduler.__init__` 参数并保存配置**

将构造函数改成接受这些参数：

```python
def __init__(
    self,
    interval_seconds: int = 300,
    workdir: str = ".",
    log_dir: str = os.path.join("outputs", "service_logs"),
    command: Optional[List[str]] = None,
    schedule_mode: str = "interval",
    schedule_time: str = "09:00",
    schedule_timezone: str = "Asia/Shanghai",
) -> None:
```

同时在初始化里：

```python
self.schedule_mode = schedule_mode
self.schedule_time = schedule_time
self.schedule_timezone = schedule_timezone
self._tz = ZoneInfo(schedule_timezone)
self._state.schedule_mode = schedule_mode
self._state.schedule_time = schedule_time if schedule_mode == "daily" else None
self._state.schedule_timezone = schedule_timezone if schedule_mode == "daily" else None
```

- [ ] **步骤 3: 增加 daily 模式的时间解析与下一次执行计算**

在 `app/scheduler.py` 中新增辅助方法：

```python
def _parse_schedule_time(self) -> tuple[int, int]:
    hour_str, minute_str = self.schedule_time.split(":", 1)
    hour = int(hour_str)
    minute = int(minute_str)
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError(f"Invalid schedule time: {self.schedule_time}")
    return hour, minute


def _compute_next_run_at(self, now: datetime | None = None) -> datetime:
    now = now or datetime.now(self._tz)
    hour, minute = self._parse_schedule_time()
    candidate = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if candidate <= now:
        candidate = candidate + timedelta(days=1)
    return candidate
```

- [ ] **步骤 4: 修改 `_loop()`，按模式决定等待方式**

把现有固定 timeout 逻辑改成：

```python
if self.schedule_mode == "daily":
    next_run_at = self._compute_next_run_at()
    self._state.next_scheduled_at = next_run_at.isoformat()
    delay = max((next_run_at - datetime.now(self._tz)).total_seconds(), 0)
    try:
        await asyncio.wait_for(self._stop_event.wait(), timeout=delay)
    except asyncio.TimeoutError:
        continue
else:
    self._state.next_scheduled_at = None
    try:
        await asyncio.wait_for(self._stop_event.wait(), timeout=self.interval_seconds)
    except asyncio.TimeoutError:
        continue
```

实现时注意：
- 仍然先 `await self.run_once()`，再计算下一轮
- daily 模式下 `run_once()` 开始前可以把 `next_scheduled_at` 清空，结束后重新设置下一次时间
- 保持原有错误日志逻辑不变

- [ ] **步骤 5: 运行新增测试**

运行：`uv run pytest tests/test_scheduler.py -q`

预期：全部通过

### 任务 3: 在 FastAPI 层读取新配置并暴露状态

**文件：**
- 修改： `app/server.py`
- 测试： `tests/test_scheduler.py`

- [ ] **步骤 1: 从环境变量读取 daily 调度配置**

在 `create_app()` 中加入：

```python
schedule_mode = os.getenv("SCHEDULE_MODE", "interval")
schedule_time = os.getenv("SCHEDULE_TIME", "09:00")
schedule_timezone = os.getenv("SCHEDULE_TZ", "Asia/Shanghai")
```

创建调度器时传入这些参数：

```python
scheduler = JobScheduler(
    interval_seconds=interval,
    workdir=workdir,
    command=run_cmd,
    schedule_mode=schedule_mode,
    schedule_time=schedule_time,
    schedule_timezone=schedule_timezone,
)
```

- [ ] **步骤 2: 扩展状态模型**

在 `StatusModel` 中加入：

```python
schedule_mode: str | None = None
schedule_time: str | None = None
schedule_timezone: str | None = None
next_scheduled_at: str | None = None
```

- [ ] **步骤 3: 增加一个 API 层回归测试**

在 `tests/test_scheduler.py` 中增加：

```python
from fastapi.testclient import TestClient

from app.server import create_app


def test_status_exposes_daily_schedule_config(monkeypatch):
    monkeypatch.setenv("SCHEDULE_MODE", "daily")
    monkeypatch.setenv("SCHEDULE_TIME", "09:00")
    monkeypatch.setenv("SCHEDULE_TZ", "Asia/Shanghai")
    app = create_app()
    client = TestClient(app)

    response = client.get("/status")

    assert response.status_code == 200
    payload = response.json()
    assert payload["schedule_mode"] == "daily"
    assert payload["schedule_time"] == "09:00"
    assert payload["schedule_timezone"] == "Asia/Shanghai"
```

- [ ] **步骤 4: 运行测试**

运行：`uv run pytest tests/test_scheduler.py -q`

预期：通过

### 任务 4: 更新容器默认配置和文档

**文件：**
- 修改： `docker-compose.yml`
- 修改： `README.md`

- [ ] **步骤 1: 修改 compose 默认调度配置**

把 `docker-compose.yml` 里的：

```yaml
- TASK_INTERVAL_SECONDS=1200
```

替换为：

```yaml
- SCHEDULE_MODE=daily
- SCHEDULE_TIME=09:00
- SCHEDULE_TZ=Asia/Shanghai
- TASK_INTERVAL_SECONDS=1200
```

说明：保留 `TASK_INTERVAL_SECONDS` 只是为了兼容 interval 模式代码路径，但 daily 模式下不再依赖它。

- [ ] **步骤 2: 更新 README 的服务化与部署说明**

在相关段落里把“每 5 分钟执行一次”的表述改成“默认每天 09:00（Asia/Shanghai）执行一次”，并补充新环境变量说明：

```md
- `SCHEDULE_MODE=interval|daily`
- `SCHEDULE_TIME=09:00`
- `SCHEDULE_TZ=Asia/Shanghai`
```

- [ ] **步骤 3: 运行文档和 compose 的最小自检**

运行：`python - <<'PY'
from pathlib import Path
print("daily" in Path("docker-compose.yml").read_text())
print("SCHEDULE_TIME" in Path("README.md").read_text())
PY`

预期：

```text
True
True
```

### 任务 5: 重建镜像并验证容器行为

**文件：**
- 无新增代码文件
- 依赖前面所有修改

- [ ] **步骤 1: 运行单元测试**

运行：`uv run pytest tests/test_scheduler.py -q`

预期：通过

- [ ] **步骤 2: 重建并启动容器**

运行：`docker compose up -d --build`

预期：镜像构建成功，`weekly-gen` 容器被创建并进入 `Up`

- [ ] **步骤 3: 检查容器状态**

运行：`docker compose ps`

预期：`weekly-gen` 出现在列表中，并暴露 `0.0.0.0:8111->8111/tcp`

- [ ] **步骤 4: 检查健康接口**

运行：`curl -s http://127.0.0.1:8111/healthz`

预期：

```json
{"status":"ok"}
```

- [ ] **步骤 5: 检查调度状态**

运行：`curl -s http://127.0.0.1:8111/status`

预期：返回 JSON 中至少包含：

```json
{
  "schedule_mode": "daily",
  "schedule_time": "09:00",
  "schedule_timezone": "Asia/Shanghai",
  "next_scheduled_at": "2026-04-11T09:00:00+08:00"
}
```

- [ ] **步骤 6: 验证手动触发仍可用**

运行：`curl -s -X POST http://127.0.0.1:8111/run-now`

预期：返回 `{"ok": true, "message": "started"}`，或如果刚好在运行则返回 409

- [ ] **步骤 7: 提交实现**

```bash
git add app/server.py app/scheduler.py docker-compose.yml README.md tests/test_scheduler.py
git commit -m "feat: add daily scheduler mode"
```
