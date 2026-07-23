from pathlib import Path

import pytest
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


def test_empty_pre_filtered_links_do_not_fall_back_to_page_links(
    monkeypatch,
    tmp_path,
):
    monkeypatch.chdir(tmp_path)
    soup = BeautifulSoup(
        '<body><a href="https://example.com/navigation">导航链接</a></body>',
        "html.parser",
    )
    completions = []

    def unexpected_fetch(*_args, **_kwargs):
        raise AssertionError("不应处理未通过筛选的页面链接")

    articles = extract_links_and_summarize(
        soup=soup,
        summary_file="empty.md",
        fetch_content_func=unexpected_fetch,
        use_patterns=False,
        pre_filtered_links=[],
        on_complete=completions.append,
    )

    assert articles == []
    assert completions == []


def test_link_processing_error_does_not_trigger_completion_callback(
    monkeypatch,
    tmp_path,
):
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

    def fail_on_second_link(url, _headers, _proxies):
        if url.endswith("/two"):
            raise RuntimeError("second link failed")
        return _article(url, "One")

    with pytest.raises(RuntimeError, match="second link failed"):
        extract_links_and_summarize(
            soup=soup,
            summary_file="issue.md",
            fetch_content_func=fail_on_second_link,
            use_patterns=False,
            on_complete=completions.append,
        )

    assert completions == []


def test_completion_callback_error_does_not_change_articles(
    monkeypatch,
    tmp_path,
    capsys,
):
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
