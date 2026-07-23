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
def test_scraper_passes_named_telegram_completion_callback(
    filename,
    display_name,
):
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
