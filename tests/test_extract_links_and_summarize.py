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
