from bs4 import BeautifulSoup

from src.pythonweekly import collect_issue_article_links, parse_latest_issue_info


def test_parse_latest_issue_info_picks_first_textual_archive_link():
    soup = BeautifulSoup(
        """
        <html>
          <body>
            <a href="/p/python-weekly-issue-740-april-9-2026"></a>
            <a href="/p/python-weekly-issue-740-april-9-2026">
              Apr 09, 2026 Python Weekly (Issue 740 April 9 2026)
            </a>
            <a href="/p/python-weekly-issue-739-april-2-2026">
              Apr 02, 2026 Python Weekly (Issue 739 April 2 2026)
            </a>
          </body>
        </html>
        """,
        "html.parser",
    )

    issue_title, link_url = parse_latest_issue_info(soup)

    assert issue_title == "Python Weekly (Issue 740 April 9 2026)"
    assert link_url == "p/python-weekly-issue-740-april-9-2026"


def test_collect_issue_article_links_only_keeps_h6_content_links():
    soup = BeautifulSoup(
        """
        <html>
          <body>
            <a href="https://twitter.com/intent/tweet?url=share">分享</a>
            <h3><a href="https://ads.example.com">广告</a></h3>
            <h6>
              <a href="https://example.com/article-1">Article One</a>
            </h6>
            <h6>
              <a href="https://www.pythonweekly.com/internal">Internal Link</a>
            </h6>
            <h6>
              <a href="https://example.com/article-2">Article Two</a>
            </h6>
            <h6>
              <a href="mailto:test@example.com">Mail</a>
            </h6>
          </body>
        </html>
        """,
        "html.parser",
    )

    links = collect_issue_article_links(soup)

    assert [link.get_text(strip=True) for link in links] == ["Article One", "Article Two"]
    assert [link["href"] for link in links] == [
        "https://example.com/article-1",
        "https://example.com/article-2",
    ]
