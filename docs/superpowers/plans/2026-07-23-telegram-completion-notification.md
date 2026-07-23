# Telegram 周刊完成通知实现计划

> **对于 agent 型执行者：** 必需子 skill：优先使用 `superpowers-subagent-driven-development`，否则使用 `superpowers-executing-plans` 逐任务实施本计划。所有步骤使用 `- [ ]` 复选框格式追踪。

**目标：** 每个周刊处理完该期全部有效文章链接并写入摘要后，立即向指定 Telegram chat 发送一条完成消息。

**架构：** 公共链接处理函数在循环正常结束后创建不可变的 `ExtractionCompletion`，再调用可选完成回调。独立的 Telegram 通知模块负责格式化消息、读取环境配置和调用 `sendMessage`；每个周刊脚本只负责绑定自己的显示名称并传入回调。

**技术栈：** Python 3.10+、requests、python-dotenv、BeautifulSoup、pytest、Telegram Bot API `sendMessage`

## Global Constraints

- 每个周刊完成该期全部文章链接的处理和写入后，立即发送一条 Telegram 消息。
- 通知包含周刊名称、处理链接数、摘要路径和完成时间。
- Telegram 发送失败不改变周刊的执行结果，也不阻塞其他周刊。
- token 和 chat ID 只保存在本地环境变量中，不进入 Git 或日志。
- 直接运行单个周刊脚本和通过 `src.main` 运行时，行为一致。
- 不发送抓取开始、抓取失败或全批次汇总通知。
- 不为 Telegram 发送失败自动重试。
- 不发送摘要文件内容或附件。
- 不改变现有文章抓取、摘要生成和去重逻辑。
- 请求使用 HTTPS `POST`，超时为 10 秒。
- 只有 `processed_count > 0` 且链接循环正常结束时才触发完成回调。
- 消息使用纯文本，不设置 `parse_mode`。
- 代码、注释和日志文案优先使用中文；Git commit message 使用英文。

---

## 文件结构

- 创建 `src/utils/telegram_notifier.py`：读取配置、格式化完成消息、调用 Telegram API、创建绑定周刊名称的回调。
- 创建 `tests/test_telegram_notifier.py`：验证消息格式、请求参数、配置缺失和全部失败分支。
- 创建 `tests/test_extract_links_and_summarize.py`：验证链接循环结束后的完成事件和回调隔离。
- 创建 `tests/test_telegram_wiring.py`：验证全部 12 个周刊都传入了正确的完成回调。
- 修改 `src/utils/extract_links_and_summarize.py`：定义完成事件并支持可选完成回调。
- 修改 12 个 `src/*weekly.py` / digest 脚本：绑定显示名称并传入回调。
- 修改 `README.md`：记录 Telegram 环境变量和通知语义。
- 修改本地 `.env`：保存真实 token 和 chat ID；该文件不得加入 Git。

---

### 任务 1：公共链接处理完成事件

**文件：**

- 创建：`tests/test_extract_links_and_summarize.py`
- 修改：`src/utils/extract_links_and_summarize.py`

**Interfaces：**

- Consumes: 现有 `extract_links_and_summarize(...) -> List[Dict[str, Any]]`
- Produces:
  - `ExtractionCompletion(processed_count: int, summary_file: Optional[str], completed_at: datetime)`
  - `CompletionCallback = Callable[[ExtractionCompletion], None]`
  - 新参数 `on_complete: Optional[CompletionCallback] = None`

- [ ] **步骤 1：编写“全部写入后触发一次”的失败测试**

在 `tests/test_extract_links_and_summarize.py` 写入：

```python
from pathlib import Path

from bs4 import BeautifulSoup

from src.utils.extract_links_and_summarize import extract_links_and_summarize


def _article(url: str, title: str) -> dict[str, str]:
    return {
        "url": url,
        "title": title,
        "chinese_title": f"中文 {title}",
        "summary": f"摘要 {title}",
    }


def test_all_articles_are_written_before_completion_callback(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    soup = BeautifulSoup(
        """
        <body>
          <a href="https://example.com/one">One</a>
          <a href="https://example.com/two">Two</a>
        </body>
        """,
        "html.parser",
    )
    completions = []
    callback_file_contents = []

    def fetch(url, _headers, _proxies):
        title = "One" if url.endswith("/one") else "Two"
        return _article(url, title)

    def on_complete(completion):
        completions.append(completion)
        callback_file_contents.append(
            Path(completion.summary_file).read_text(encoding="utf-8")
        )

    articles = extract_links_and_summarize(
        soup=soup,
        summary_file="issue_summary.md",
        summary_title_prefix="demo",
        fetch_content_func=fetch,
        use_patterns=False,
        on_complete=on_complete,
    )

    assert len(articles) == 2
    assert len(completions) == 1
    assert completions[0].processed_count == 2
    assert completions[0].summary_file.startswith("outputs/")
    assert completions[0].completed_at.utcoffset().total_seconds() == 8 * 60 * 60
    assert "摘要 One" in callback_file_contents[0]
    assert "摘要 Two" in callback_file_contents[0]
```

- [ ] **步骤 2：运行测试并确认因接口缺失而失败**

运行：

```bash
rtk uv run pytest tests/test_extract_links_and_summarize.py::test_all_articles_are_written_before_completion_callback -v
```

预期：失败，错误指出 `extract_links_and_summarize()` 不接受 `on_complete`。

- [ ] **步骤 3：编写“无链接不触发”和“回调异常不外溢”的失败测试**

继续写入同一测试文件：

```python
def test_no_links_does_not_trigger_completion_callback(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    soup = BeautifulSoup("<body></body>", "html.parser")
    completions = []

    articles = extract_links_and_summarize(
        soup=soup,
        summary_file="empty.md",
        use_patterns=False,
        on_complete=completions.append,
    )

    assert articles == []
    assert completions == []


def test_completion_callback_error_does_not_change_articles(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    soup = BeautifulSoup(
        '<body><a href="https://example.com/one">One</a></body>',
        "html.parser",
    )

    def broken_callback(_completion):
        raise RuntimeError("callback failed")

    articles = extract_links_and_summarize(
        soup=soup,
        summary_file="issue.md",
        fetch_content_func=lambda url, _headers, _proxies: _article(url, "One"),
        use_patterns=False,
        on_complete=broken_callback,
    )

    assert len(articles) == 1
    assert "完成回调执行失败：RuntimeError" in capsys.readouterr().out
```

- [ ] **步骤 4：实现完成事件和回调**

在 `src/utils/extract_links_and_summarize.py` 添加导入和接口：

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, List, Dict, Any, Optional, Tuple, Pattern
from zoneinfo import ZoneInfo


@dataclass(frozen=True)
class ExtractionCompletion:
    processed_count: int
    summary_file: Optional[str]
    completed_at: datetime


CompletionCallback = Callable[[ExtractionCompletion], None]
```

在函数参数末尾添加：

```python
    on_complete: Optional[CompletionCallback] = None,
```

在 `if matched_links:` 分支的链接循环和最终保存提示之后、函数返回之前添加：

```python
        if processed_articles > 0 and on_complete is not None:
            completion = ExtractionCompletion(
                processed_count=processed_articles,
                summary_file=summary_file,
                completed_at=datetime.now(ZoneInfo("Asia/Shanghai")),
            )
            try:
                on_complete(completion)
            except Exception as exc:
                print(f"完成回调执行失败：{type(exc).__name__}")
```

不要打印异常正文。异常正文可能包含 Telegram token 或完整请求 URL。

- [ ] **步骤 5：运行公共链接处理测试**

运行：

```bash
rtk uv run pytest tests/test_extract_links_and_summarize.py -v
```

预期：3 个测试全部通过。

- [ ] **步骤 6：提交任务 1**

```bash
rtk git add src/utils/extract_links_and_summarize.py tests/test_extract_links_and_summarize.py
rtk git commit -m "feat: add extraction completion callbacks"
```

---

### 任务 2：Telegram 通知模块

**文件：**

- 创建：`src/utils/telegram_notifier.py`
- 创建：`tests/test_telegram_notifier.py`

**Interfaces：**

- Consumes: `ExtractionCompletion`
- Produces:
  - `format_completion_message(newsletter_name: str, completion: ExtractionCompletion) -> str`
  - `send_telegram_message(text: str) -> bool`
  - `create_telegram_completion_callback(newsletter_name: str) -> CompletionCallback`

- [ ] **步骤 1：编写消息格式与成功请求的失败测试**

在 `tests/test_telegram_notifier.py` 写入：

```python
from datetime import datetime
from zoneinfo import ZoneInfo

from src.utils.extract_links_and_summarize import ExtractionCompletion
from src.utils import telegram_notifier


class FakeResponse:
    def __init__(self, status_code=200, payload=None, json_error=None):
        self.status_code = status_code
        self._payload = {"ok": True} if payload is None else payload
        self._json_error = json_error

    def json(self):
        if self._json_error is not None:
            raise self._json_error
        return self._payload


def _completion():
    return ExtractionCompletion(
        processed_count=18,
        summary_file="outputs/demo_summary.md",
        completed_at=datetime(2026, 7, 23, 15, 30, 12, tzinfo=ZoneInfo("Asia/Shanghai")),
    )


def test_format_completion_message():
    text = telegram_notifier.format_completion_message("Frontend Focus", _completion())

    assert text == (
        "✅ 周刊抓取完成\n\n"
        "周刊：Frontend Focus\n"
        "已处理：18 个链接\n"
        "摘要：outputs/demo_summary.md\n"
        "时间：2026-07-23 15:30:12"
    )


def test_send_telegram_message_posts_expected_json(monkeypatch):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test-token")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "123456")
    calls = []

    def fake_post(url, **kwargs):
        calls.append((url, kwargs))
        return FakeResponse()

    monkeypatch.setattr(telegram_notifier.requests, "post", fake_post)

    assert telegram_notifier.send_telegram_message("完成") is True
    assert calls == [
        (
            "https://api.telegram.org/bottest-token/sendMessage",
            {
                "json": {"chat_id": "123456", "text": "完成"},
                "timeout": 10,
            },
        )
    ]
```

- [ ] **步骤 2：运行测试并确认模块不存在**

运行：

```bash
rtk uv run pytest tests/test_telegram_notifier.py -v
```

预期：测试收集失败，指出无法导入 `src.utils.telegram_notifier`。

- [ ] **步骤 3：补齐配置缺失和错误响应测试**

继续写入：

```python
import requests

import pytest


@pytest.mark.parametrize(
    ("token", "chat_id"),
    [
        ("", "123456"),
        ("test-token", ""),
    ],
)
def test_missing_config_skips_request(monkeypatch, token, chat_id):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", token)
    monkeypatch.setenv("TELEGRAM_CHAT_ID", chat_id)

    def unexpected_post(*_args, **_kwargs):
        raise AssertionError("不应发起请求")

    monkeypatch.setattr(telegram_notifier.requests, "post", unexpected_post)

    assert telegram_notifier.send_telegram_message("完成") is False


@pytest.mark.parametrize(
    "response",
    [
        FakeResponse(status_code=500),
        FakeResponse(json_error=ValueError("invalid json")),
        FakeResponse(payload=[]),
        FakeResponse(payload={"ok": False, "description": "chat not found"}),
    ],
)
def test_response_errors_return_false(monkeypatch, response):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test-token")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "123456")
    monkeypatch.setattr(
        telegram_notifier.requests,
        "post",
        lambda *_args, **_kwargs: response,
    )

    assert telegram_notifier.send_telegram_message("完成") is False


def test_request_error_does_not_log_token(monkeypatch, capsys):
    token = "secret-token"
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", token)
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "123456")

    def fail(*_args, **_kwargs):
        raise requests.RequestException(f"request failed at bot{token}")

    monkeypatch.setattr(telegram_notifier.requests, "post", fail)

    assert telegram_notifier.send_telegram_message("完成") is False
    assert token not in capsys.readouterr().out
```

- [ ] **步骤 4：实现通知模块**

创建 `src/utils/telegram_notifier.py`：

```python
#!/usr/bin/env python3
import os
from typing import Callable

import requests
from dotenv import load_dotenv

from src.utils.extract_links_and_summarize import (
    CompletionCallback,
    ExtractionCompletion,
)

load_dotenv()

TELEGRAM_API_BASE_URL = "https://api.telegram.org"
TELEGRAM_TIMEOUT_SECONDS = 10


def format_completion_message(
    newsletter_name: str,
    completion: ExtractionCompletion,
) -> str:
    summary_file = completion.summary_file or "未生成摘要文件"
    completed_at = completion.completed_at.strftime("%Y-%m-%d %H:%M:%S")
    return (
        "✅ 周刊抓取完成\n\n"
        f"周刊：{newsletter_name}\n"
        f"已处理：{completion.processed_count} 个链接\n"
        f"摘要：{summary_file}\n"
        f"时间：{completed_at}"
    )


def _safe_detail(value: object, token: str) -> str:
    return str(value).replace(token, "[REDACTED]")


def send_telegram_message(text: str) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("⚠️ Telegram 通知已跳过：缺少环境变量配置")
        return False

    url = f"{TELEGRAM_API_BASE_URL}/bot{token}/sendMessage"
    try:
        response = requests.post(
            url,
            json={"chat_id": chat_id, "text": text},
            timeout=TELEGRAM_TIMEOUT_SECONDS,
        )
    except requests.RequestException as exc:
        print(f"⚠️ Telegram 通知发送失败：{_safe_detail(exc, token)}")
        return False

    if response.status_code < 200 or response.status_code >= 300:
        print(f"⚠️ Telegram 通知发送失败：HTTP {response.status_code}")
        return False

    try:
        payload = response.json()
    except ValueError:
        print("⚠️ Telegram 通知发送失败：响应不是合法 JSON")
        return False

    if not isinstance(payload, dict):
        print("⚠️ Telegram 通知发送失败：响应 JSON 不是对象")
        return False

    if payload.get("ok") is not True:
        detail = _safe_detail(payload.get("description", "未知 API 错误"), token)
        print(f"⚠️ Telegram 通知发送失败：{detail}")
        return False

    return True


def create_telegram_completion_callback(
    newsletter_name: str,
) -> CompletionCallback:
    def notify(completion: ExtractionCompletion) -> None:
        text = format_completion_message(newsletter_name, completion)
        send_telegram_message(text)

    return notify
```

- [ ] **步骤 5：验证回调会调用发送函数**

添加测试：

```python
def test_completion_callback_formats_and_sends(monkeypatch):
    sent = []
    monkeypatch.setattr(
        telegram_notifier,
        "send_telegram_message",
        lambda text: sent.append(text) or True,
    )

    callback = telegram_notifier.create_telegram_completion_callback("Frontend Focus")
    callback(_completion())

    assert len(sent) == 1
    assert "周刊：Frontend Focus" in sent[0]
    assert "已处理：18 个链接" in sent[0]
```

运行：

```bash
rtk uv run pytest tests/test_telegram_notifier.py -v
```

预期：全部通过。

- [ ] **步骤 6：提交任务 2**

```bash
rtk git add src/utils/telegram_notifier.py tests/test_telegram_notifier.py
rtk git commit -m "feat: send Telegram completion messages"
```

---

### 任务 3：接入全部周刊

**文件：**

- 创建：`tests/test_telegram_wiring.py`
- 修改：
  - `src/frontendfoc.py`
  - `src/javascriptweekly.py`
  - `src/leadershipintech.py`
  - `src/nextjsweekly.py`
  - `src/nodeweekly.py`
  - `src/programmingdigest.py`
  - `src/pythonweekly.py`
  - `src/reactweekly.py`
  - `src/reactdigest.py`
  - `src/thisweekinreact.py`
  - `src/tailwindweekly.py`
  - `src/webtoolsweekly.py`

**Interfaces：**

- Consumes: `create_telegram_completion_callback(newsletter_name) -> CompletionCallback`
- Produces: 每个 `extract_links_and_summarize` 调用都设置 `on_complete`

- [ ] **步骤 1：编写全部周刊接线的失败测试**

创建 `tests/test_telegram_wiring.py`：

```python
import ast
from pathlib import Path

import pytest


SCRAPER_NAMES = {
    "frontendfoc.py": "Frontend Focus",
    "javascriptweekly.py": "JavaScript Weekly",
    "leadershipintech.py": "Leadership in Tech",
    "nextjsweekly.py": "Next.js Weekly",
    "nodeweekly.py": "Node Weekly",
    "programmingdigest.py": "Programming Digest",
    "pythonweekly.py": "Python Weekly",
    "reactweekly.py": "React Weekly",
    "reactdigest.py": "React Digest",
    "thisweekinreact.py": "This Week in React",
    "tailwindweekly.py": "Tailwind Weekly",
    "webtoolsweekly.py": "Web Tools Weekly",
}


@pytest.mark.parametrize(("filename", "display_name"), SCRAPER_NAMES.items())
def test_scraper_passes_named_telegram_completion_callback(filename, display_name):
    source = (Path("src") / filename).read_text(encoding="utf-8")
    tree = ast.parse(source)
    extraction_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "extract_links_and_summarize"
    ]

    assert extraction_calls, f"{filename} 没有链接处理调用"
    for call in extraction_calls:
        keyword = next(
            (item for item in call.keywords if item.arg == "on_complete"),
            None,
        )
        assert keyword is not None, f"{filename} 没有传入 on_complete"
        assert isinstance(keyword.value, ast.Call)
        assert isinstance(keyword.value.func, ast.Name)
        assert keyword.value.func.id == "create_telegram_completion_callback"
        assert len(keyword.value.args) == 1
        assert isinstance(keyword.value.args[0], ast.Constant)
        assert keyword.value.args[0].value == display_name
```

- [ ] **步骤 2：运行测试并确认 12 个用例失败**

运行：

```bash
rtk uv run pytest tests/test_telegram_wiring.py -v
```

预期：12 个用例均因缺少 `on_complete` 失败。

- [ ] **步骤 3：为 12 个周刊添加导入和回调**

每个目标脚本添加：

```python
from src.utils.telegram_notifier import create_telegram_completion_callback
```

在每个真实的 `extract_links_and_summarize(...)` 调用中添加下列对应参数：

| 文件 | 参数 |
| --- | --- |
| `frontendfoc.py` | `on_complete=create_telegram_completion_callback("Frontend Focus")` |
| `javascriptweekly.py` | `on_complete=create_telegram_completion_callback("JavaScript Weekly")` |
| `leadershipintech.py` | `on_complete=create_telegram_completion_callback("Leadership in Tech")` |
| `nextjsweekly.py` | `on_complete=create_telegram_completion_callback("Next.js Weekly")` |
| `nodeweekly.py` | `on_complete=create_telegram_completion_callback("Node Weekly")` |
| `programmingdigest.py` | `on_complete=create_telegram_completion_callback("Programming Digest")` |
| `pythonweekly.py` | `on_complete=create_telegram_completion_callback("Python Weekly")` |
| `reactweekly.py` | `on_complete=create_telegram_completion_callback("React Weekly")` |
| `reactdigest.py` | `on_complete=create_telegram_completion_callback("React Digest")` |
| `thisweekinreact.py` | `on_complete=create_telegram_completion_callback("This Week in React")` |
| `tailwindweekly.py` | `on_complete=create_telegram_completion_callback("Tailwind Weekly")` |
| `webtoolsweekly.py` | `on_complete=create_telegram_completion_callback("Web Tools Weekly")` |

参数前一行必须保留尾逗号。例如：

```python
        pre_filtered_links=filtered_links,
        on_complete=create_telegram_completion_callback("Frontend Focus"),
    )
```

不要修改 `thisweekinreact.py` 中被注释掉的历史调用。

- [ ] **步骤 4：运行接线测试和相关单元测试**

运行：

```bash
rtk uv run pytest \
  tests/test_telegram_wiring.py \
  tests/test_extract_links_and_summarize.py \
  tests/test_telegram_notifier.py \
  -v
```

预期：全部通过。

- [ ] **步骤 5：提交任务 3**

```bash
rtk git add \
  src/frontendfoc.py \
  src/javascriptweekly.py \
  src/leadershipintech.py \
  src/nextjsweekly.py \
  src/nodeweekly.py \
  src/programmingdigest.py \
  src/pythonweekly.py \
  src/reactweekly.py \
  src/reactdigest.py \
  src/thisweekinreact.py \
  src/tailwindweekly.py \
  src/webtoolsweekly.py \
  tests/test_telegram_wiring.py
rtk git commit -m "feat: notify after each newsletter completes"
```

---

### 任务 4：配置、文档和完整验证

**文件：**

- 修改：`README.md`
- 修改但不提交：`.env`

**Interfaces：**

- Consumes: `TELEGRAM_BOT_TOKEN`、`TELEGRAM_CHAT_ID`
- Produces: 本地运行和 Docker Compose 均可读取的 Telegram 配置

- [ ] **步骤 1：更新 README 环境配置**

在 README 的 `.env` 示例中加入：

```env
# Telegram 完成通知
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
```

在功能特性中加入：

```markdown
- 📣 **完成通知**：每个周刊处理完全部文章链接后发送 Telegram 消息
```

在注意事项中说明：

```markdown
4. **Telegram 通知**：只有找到并处理至少一个文章链接后才发送。通知失败只写入日志，不改变抓取任务的成功状态。
```

- [ ] **步骤 2：写入本地敏感配置**

保留 `.env` 中已有配置，把当前对话中用户提供的 token 写入 `TELEGRAM_BOT_TOKEN`，把 chat ID 写入 `TELEGRAM_CHAT_ID`。不要把两个真实值复制到计划、README、测试或任何受 Git 管理的文件。

执行后确认 `.env` 仍被 Git 忽略：

```bash
rtk git check-ignore -v .env
```

预期：输出 `.gitignore` 中的 `.env` 规则。

- [ ] **步骤 3：运行完整测试**

运行：

```bash
rtk uv run pytest -v
```

预期：全部测试通过，无失败、错误或未处理警告。

- [ ] **步骤 4：检查格式和敏感信息**

运行：

```bash
rtk git diff --check
rtk git status --short
```

预期：

- `git diff --check` 无输出且退出码为 0。
- `.env` 不出现在 `git status`。
- 用户原有的两个 `outputs/*.md` 未跟踪文件保持原样。

只检查受 Git 管理的文件是否包含真实凭据。不得把真实 token 写进命令输出、计划、日志或测试：

```bash
rtk git grep -n "TELEGRAM_BOT_TOKEN="
rtk git grep -n "TELEGRAM_CHAT_ID="
```

预期：只匹配 README 中的占位符，不匹配真实值。

- [ ] **步骤 5：提交文档**

```bash
rtk git add README.md
rtk git commit -m "docs: document Telegram notifications"
```

- [ ] **步骤 6：最终验证**

运行：

```bash
rtk uv run pytest -v
rtk git diff --check HEAD~4..HEAD
rtk git status --short
```

预期：

- 完整测试套件通过。
- 四个实现提交没有空白错误。
- 工作区只保留用户原有的 `outputs/*.md` 未跟踪文件。
