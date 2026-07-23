from datetime import datetime
from zoneinfo import ZoneInfo

import pytest
import requests

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
        completed_at=datetime(
            2026,
            7,
            23,
            15,
            30,
            12,
            tzinfo=ZoneInfo("Asia/Shanghai"),
        ),
    )


def test_format_completion_message():
    text = telegram_notifier.format_completion_message(
        "Frontend Focus",
        _completion(),
    )

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


def test_request_error_does_not_log_credentials(monkeypatch, capsys):
    token = "secret-token"
    chat_id = "secret-chat-id"
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", token)
    monkeypatch.setenv("TELEGRAM_CHAT_ID", chat_id)

    def fail(*_args, **_kwargs):
        raise requests.RequestException(
            f"request failed at bot{token} for chat {chat_id}"
        )

    monkeypatch.setattr(telegram_notifier.requests, "post", fail)

    assert telegram_notifier.send_telegram_message("完成") is False
    output = capsys.readouterr().out
    assert token not in output
    assert chat_id not in output


def test_completion_callback_formats_and_sends(monkeypatch):
    sent = []
    monkeypatch.setattr(
        telegram_notifier,
        "send_telegram_message",
        lambda text: sent.append(text) or True,
    )

    callback = telegram_notifier.create_telegram_completion_callback(
        "Frontend Focus"
    )
    callback(_completion())

    assert len(sent) == 1
    assert "周刊：Frontend Focus" in sent[0]
    assert "已处理：18 个链接" in sent[0]
