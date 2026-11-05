from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.mark.parametrize("model,expected", [("gateway-test-model", "gateway-test-model"), ("  custom-model  ", "custom-model"), ("", "deepseek-v4-flash"), (None, "deepseek-v4-flash")])
def test_gateway_and_model_config_apply_to_translation_and_summary(monkeypatch, model, expected):
    calls = []
    initialization = []

    def create(**kwargs):
        calls.append(kwargs)
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="测试回答"))])

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
    assert module.translate_title_to_chinese("Example title") == "测试回答"
    assert module.summarize_with_deepseek("Example content") == "测试回答"
    assert [call["model"] for call in calls] == [expected, expected]
    assert [call["max_tokens"] for call in calls] == [200, 8000]
