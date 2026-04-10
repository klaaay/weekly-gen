# Scheduler State Persistence 实现计划

> **对于 agent 型执行者：** 必需子 skill：优先使用 `superpowers-subagent-driven-development`，否则使用 `superpowers-executing-plans` 逐任务实施本计划。所有步骤使用 `- [ ]` 复选框格式追踪。

**目标：** 将调度器最近一次执行状态和下一次计划时间持久化到 `outputs/service_state.json`，使服务重启后 `/status` 仍能反映上一次执行情况。

**架构：** 在 `JobScheduler` 内增加单文件 JSON 持久化层。调度器初始化时读取状态文件恢复最近一次执行结果，并在状态变化时写回；调度时间仍按当前时间重新计算，不做错过任务补偿。

**技术栈：** Python 3.12、FastAPI、asyncio、JSON 文件持久化、uv、pytest、Docker Compose

---

### 任务 1: 为状态文件读写补失败测试

**文件：**
- 修改： `tests/test_scheduler.py`
- 参考： `app/scheduler.py`

- [ ] **步骤 1: 增加状态文件写入测试**

```python
import json
from pathlib import Path


def test_run_state_is_persisted_to_json(tmp_path):
    state_file = tmp_path / "service_state.json"
    scheduler = JobScheduler(
        schedule_mode="daily",
        schedule_time="09:00",
        schedule_timezone="Asia/Shanghai",
        state_file_path=str(state_file),
    )

    scheduler._state.last_started_at = "2026-04-11T09:00:00+08:00"
    scheduler._state.last_finished_at = "2026-04-11T09:02:00+08:00"
    scheduler._state.last_returncode = 0
    scheduler._state.last_duration_sec = 120.0
    scheduler._persist_state()

    payload = json.loads(state_file.read_text())
    assert payload["last_returncode"] == 0
    assert payload["last_duration_sec"] == 120.0
```

- [ ] **步骤 2: 增加状态文件恢复测试**

```python
def test_scheduler_loads_persisted_state_and_recomputes_next_run(tmp_path):
    state_file = tmp_path / "service_state.json"
    state_file.write_text(
        json.dumps(
            {
                "last_started_at": "2026-04-10T09:00:00+08:00",
                "last_finished_at": "2026-04-10T09:05:00+08:00",
                "last_returncode": 0,
                "last_duration_sec": 300.0,
                "last_log_file": "outputs/service_logs/run-20260410-090000.log",
                "schedule_mode": "daily",
                "schedule_time": "09:00",
                "schedule_timezone": "Asia/Shanghai",
                "next_scheduled_at": "2099-01-01T09:00:00+08:00",
            }
        ),
        encoding="utf-8",
    )

    scheduler = JobScheduler(
        schedule_mode="daily",
        schedule_time="09:00",
        schedule_timezone="Asia/Shanghai",
        state_file_path=str(state_file),
    )

    assert scheduler.state.last_returncode == 0
    assert scheduler.state.last_log_file == "outputs/service_logs/run-20260410-090000.log"
    assert scheduler.state.next_scheduled_at != "2099-01-01T09:00:00+08:00"
```

- [ ] **步骤 3: 运行测试验证当前失败**

运行：`uv run pytest tests/test_scheduler.py -q`

预期：失败，提示 `JobScheduler` 没有 `state_file_path` 参数或缺少 `_persist_state`

### 任务 2: 在调度器中实现 JSON 状态持久化

**文件：**
- 修改： `app/scheduler.py`
- 测试： `tests/test_scheduler.py`

- [ ] **步骤 1: 给 `JobScheduler` 增加状态文件路径配置**

把构造函数扩展为：

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
    state_file_path: Optional[str] = None,
) -> None:
```

并设置默认路径：

```python
self.state_file_path = state_file_path or os.path.join(self.workdir, "outputs", "service_state.json")
```

- [ ] **步骤 2: 增加读写辅助方法**

在 `app/scheduler.py` 中新增：

```python
def _load_persisted_state(self) -> None:
    if not os.path.exists(self.state_file_path):
        return
    try:
        with open(self.state_file_path, "r", encoding="utf-8") as f:
            payload = json.load(f)
    except Exception:
        return

    for key, value in payload.items():
        if hasattr(self._state, key):
            setattr(self._state, key, value)


def _persist_state(self) -> None:
    os.makedirs(os.path.dirname(self.state_file_path), exist_ok=True)
    with open(self.state_file_path, "w", encoding="utf-8") as f:
        json.dump(self._state.to_dict(), f, ensure_ascii=False, indent=2)
```
```

- [ ] **步骤 3: 在初始化中恢复状态**

在创建 `_state` 之后调用：

```python
self._load_persisted_state()
```

然后保留当前配置优先级，覆盖持久化文件中的配置字段：

```python
self._state.schedule_mode = schedule_mode
self._state.schedule_time = schedule_time if schedule_mode == "daily" else None
self._state.schedule_timezone = schedule_timezone if schedule_mode == "daily" else None
```

最后重新计算：

```python
self._refresh_next_scheduled_at()
self._persist_state()
```

- [ ] **步骤 4: 在状态变化点写回 JSON**

在这些位置补 `self._persist_state()`：
- `run_once()` 开始后，状态字段清空/更新之后
- `run_once()` 结束后
- `_refresh_next_scheduled_at()` 更新下一次时间后

同时把 `_persist_state()` 包一层错误处理，失败时写入：

```python
outputs/service_logs/scheduler-errors.log
```

不要因为状态文件写失败而让服务崩掉。

- [ ] **步骤 5: 运行测试**

运行：`uv run pytest tests/test_scheduler.py -q`

预期：全部通过

### 任务 3: 更新文档说明

**文件：**
- 修改： `README.md`

- [ ] **步骤 1: 补充服务状态持久化说明**

在服务化说明附近增加：

```md
- 调度器状态会持久化到 `outputs/service_state.json`
- 该文件保存最近一次执行信息和下一次计划时间
- 服务重启后 `/status` 仍可看到上一次执行结果
- 该机制不会补跑停机期间错过的计划任务
```

- [ ] **步骤 2: 运行最小文档校验**

运行：`python - <<'PY'
from pathlib import Path
text = Path("README.md").read_text()
print("service_state.json" in text)
PY`

预期：

```text
True
```

### 任务 4: 验证容器中的持久化行为

**文件：**
- 修改： 无
- 依赖前述实现

- [ ] **步骤 1: 运行单元测试**

运行：`uv run pytest tests/test_scheduler.py -q`

预期：通过

- [ ] **步骤 2: 重建并启动服务**

运行：`docker compose up -d --build`

预期：容器成功启动

- [ ] **步骤 3: 手动触发一次执行**

运行：`curl -s -X POST http://127.0.0.1:8111/run-now`

预期：返回 `{"ok":true,"message":"started"}` 或 409

- [ ] **步骤 4: 确认状态文件在本地生成**

运行：`python - <<'PY'
from pathlib import Path
path = Path("outputs/service_state.json")
print(path.exists())
print(path)
PY`

预期：

```text
True
outputs/service_state.json
```

- [ ] **步骤 5: 重启容器并验证状态仍可见**

运行：`docker compose restart weekly-gen && sleep 3 && curl -s http://127.0.0.1:8111/status`

预期：返回 JSON 中仍包含上一次执行的 `last_started_at`、`last_finished_at`、`last_returncode`

- [ ] **步骤 6: 提交**

```bash
git add app/scheduler.py tests/test_scheduler.py README.md
git commit -m "feat: persist scheduler state"
```
