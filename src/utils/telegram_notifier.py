#!/usr/bin/env python3
import os

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


def _redact_sensitive(value: object, token: str, chat_id: str) -> str:
    detail = str(value)
    for secret in (token, chat_id):
        if secret:
            detail = detail.replace(secret, "[REDACTED]")
    return detail


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
        detail = _redact_sensitive(exc, token, chat_id)
        print(f"⚠️ Telegram 通知发送失败：{detail}")
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
        api_detail = payload.get("description", "未知 API 错误")
        detail = _redact_sensitive(api_detail, token, chat_id)
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
