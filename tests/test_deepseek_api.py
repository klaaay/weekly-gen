from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.mark.parametrize("model,expected", [("gateway-test-model", "gateway-test-model"), ("  custom-model  ", "custom-model"), ("", "deepseek-v4-flash"), (None, "deepseek-v4-flash")])
def test_gateway_and_model_config_apply_to_translation_and_summary(monkeypatch, model, expected):
    calls = []
    initialization = []
    points = [
        {"emoji": "🚀", "label": "正式发布", "detail": "版本 1.0 已发布。"},
        {"emoji": "🧩", "label": "核心机制", "detail": "用 `render()` 渲染组件。"},
    ]
    invalid = json.dumps({"overview": "概述总结：项目推出首个稳定版本。", "points": points})
    valid = json.dumps({"overview": "项目推出首个稳定版本。", "points": points})
    replies = iter(["", "测试标题", invalid, f"```json\n{valid}\n```", "", "overview summary"])

    def create(**kwargs):
        calls.append(kwargs)
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=next(replies)))])

    def client(**kwargs):
        initialization.append(kwargs)
        return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))

    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-only-token")
    monkeypatch.setenv("DEEPSEEK_BASE_URL", "https://gateway.example/v1")
    if model is None:
        monkeypatch.delenv("DEEPSEEK_MODEL", raising=False)
    else:
        monkeypatch.setenv("DEEPSEEK_MODEL", model)
    monkeypatch.setattr("openai.OpenAI", client)
    monkeypatch.setattr("dotenv.load_dotenv", lambda: None)
    path = Path(__file__).resolve().parents[1] / "src/utils/deepseek_api.py"
    spec = spec_from_file_location("gateway_config_test", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    assert initialization == [{"api_key": "test-only-token", "base_url": "https://gateway.example/v1"}]
    assert module.translate_title_to_chinese("Example title") == "测试标题"
    assert module.summarize_with_deepseek("Example content") == (
        "项目推出首个稳定版本。\n\n"
        "- 🚀 **正式发布**：版本 1.0 已发布。\n"
        "- 🧩 **核心机制**：用 `render()` 渲染组件。"
    )
    assert module.summarize_with_deepseek("Example content") == "总结失败：模型未返回符合格式的摘要。"
    assert [call["model"] for call in calls] == [expected] * 6
    assert [call["max_tokens"] for call in calls] == [1024, 1024, 8000, 8000, 8000, 8000]
    assert calls[2]["messages"][1] == {"role": "user", "content": "Example content"}
    assert "上一份回复格式不符合要求" in calls[3]["messages"][0]["content"]
