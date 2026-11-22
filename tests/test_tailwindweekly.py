from types import SimpleNamespace

import pytest
import requests
from bs4 import BeautifulSoup

from src import tailwindweekly
from src.tailwindweekly import collect_issue_article_links, parse_latest_issue_info
from src.utils.last_run_tracker import load_last_run_info, update_last_run_info


def test_parse_latest_issue_info_picks_first_issue_card_link():
    soup = BeautifulSoup(
        """
        <html>
          <body>
            <section class="section-posts">
              <article class="card-post">
                <h2 class="card-title">
                  <a href="/issue-212/">Tailwind Weekly #212: Maizzle 6 beta</a>
                </h2>
              </article>
              <article class="card-post">
                <h2 class="card-title">
                  <a href="/issue-211/">Tailwind Weekly #211: Animate Smarter</a>
                </h2>
              </article>
            </section>
          </body>
        </html>
        """,
        "html.parser",
    )

    issue_title, link_url = parse_latest_issue_info(soup)

    assert issue_title == "Tailwind Weekly #212: Maizzle 6 beta"
    assert link_url == "issue-212/"


def test_parse_latest_issue_info_accepts_current_tailwind_weekly_slug():
    soup = BeautifulSoup(
        """
        <html>
          <body>
            <section class="section-posts">
              <article class="card-post">
                <h2 class="card-title">
                  <a href="/tailwind-weekly-21/">Tailwind Weekly #219: ui.sh goes local-first</a>
                </h2>
              </article>
              <article class="card-post">
                <h2 class="card-title">
                  <a href="/issue-218/">Tailwind Weekly #218: Maizzle 6 Goes Big</a>
                </h2>
              </article>
            </section>
          </body>
        </html>
        """,
        "html.parser",
    )

    issue_title, link_url = parse_latest_issue_info(soup)

    assert issue_title == "Tailwind Weekly #219: ui.sh goes local-first"
    assert link_url == "tailwind-weekly-21/"


def test_collect_issue_article_links_keeps_content_links_and_filters_chrome():
    soup = BeautifulSoup(
        """
        <html>
          <body>
            <a href="https://x.com/intent/tweet?url=share">Share on X</a>
            <div class="post-content">
              <p>
                The <a href="https://x.com/cossssmin?ref=tailwindweekly.com">creator</a>
                shipped <a href="https://github.com/maizzle/framework/releases?ref=tailwindweekly.com">Maizzle 6 beta</a>.
              </p>
              <figure>
                <a href="https://frontendmasters.com/blog/js?ref=tailwindweekly.com">
                  <img src="/content/images/js.png" />
                </a>
              </figure>
              <h3>
                <a href="https://frontendmasters.com/blog/js?ref=tailwindweekly.com">
                  What To Know in JavaScript
                </a>
              </h3>
              <p>
                <a href="https://windybase.com/?ref=tailwindweekly.com">
                  <strong>Windybase</strong>
                </a> - template resources.
              </p>
              <p>
                You can <a href="https://forms.gle/example?ref=tailwindweekly.com">submit a link</a>
                or buy me a coffee with this
                <a href="https://buymeacoffee.com/vivgui?ref=tailwindweekly.com">link</a>.
              </p>
              <p>
                <a href="https://tailwindweekly.com/issue-211/">Read next</a>
              </p>
            </div>
          </body>
        </html>
        """,
        "html.parser",
    )

    links = collect_issue_article_links(soup)

    assert [link.get_text(" ", strip=True) for link in links] == [
        "Maizzle 6 beta",
        "What To Know in JavaScript",
        "Windybase",
    ]
    assert [link["href"] for link in links] == [
        "https://github.com/maizzle/framework/releases?ref=tailwindweekly.com",
        "https://frontendmasters.com/blog/js?ref=tailwindweekly.com",
        "https://windybase.com/?ref=tailwindweekly.com",
    ]


@pytest.fixture
def scrape_sources(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("LAST_RUN_INFO_PATH", str(tmp_path / "last_run_info.json"))
    sources = {}
    requests_seen = []
    articles_seen = []

    def get(url, **kwargs):
        requests_seen.append(url)
        result = sources[url]
        if isinstance(result, requests.RequestException):
            raise result
        status, text = result
        return SimpleNamespace(status_code=status, headers={}, text=text, content=text.encode())

    def summarize(url, _headers, _proxies):
        articles_seen.append(url)
        return dict(url=url, title="Article", chinese_title="文章", summary="文章摘要")

    monkeypatch.setattr(tailwindweekly.requests, "get", get)
    monkeypatch.setattr(tailwindweekly, "fetch_page_content", summarize)
    monkeypatch.setattr(tailwindweekly, "create_telegram_completion_callback", lambda _name: None)
    return sources, requests_seen, articles_seen


def _rss(*issues):
    items = "".join(
        f"<item><title>Tailwind Weekly #{issue}</title>"
        f"<link>https://tailwindweekly.com/issue-{issue}/</link>"
        f'<content:encoded><![CDATA[<a href="https://example.com/{issue}">Article</a>]]>'
        "</content:encoded></item>"
        for issue in issues
    )
    return f'<rss xmlns:content="http://purl.org/rss/1.0/modules/content/"><channel>{items}</channel></rss>'


@pytest.mark.parametrize("homepage", [(403, "Challenge"), (200, "No issue"), requests.Timeout()])
def test_scrape_uses_rss_when_homepage_cannot_locate_latest(scrape_sources, homepage, tmp_path):
    sources, requests_seen, articles_seen = scrape_sources
    sources[tailwindweekly.ARCHIVE_URL] = homepage
    sources[tailwindweekly.RSS_URL] = (200, _rss(240, 239))
    update_last_run_info("tailwindweekly", {"full_url": f"{tailwindweekly.BASE_URL}/issue-240/"})

    tailwindweekly.scrape_tailwindweekly()
    tailwindweekly.scrape_tailwindweekly()

    assert requests_seen == [tailwindweekly.ARCHIVE_URL, tailwindweekly.RSS_URL] * 2
    assert articles_seen == ["https://example.com/240"]
    summary, = (tmp_path / "outputs").glob("*_240_summary.md")
    assert summary.read_text().count("文章摘要") == 1
    assert load_last_run_info()["tailwindweekly"]["link_url"] == "issue-240/"


@pytest.mark.parametrize("issue_status", [200, 403])
def test_scrape_prefers_webpage_then_uses_rss_for_same_issue(scrape_sources, issue_status):
    sources, requests_seen, articles_seen = scrape_sources
    issue_url = f"{tailwindweekly.BASE_URL}/issue-240/"
    sources[tailwindweekly.ARCHIVE_URL] = (200, '<a href="/issue-240/">Tailwind Weekly #240</a>')
    sources[issue_url] = (issue_status, '<a href="https://example.com/web">Article</a>')
    sources[tailwindweekly.RSS_URL] = (200, _rss(241, 240))

    tailwindweekly.scrape_tailwindweekly()

    assert requests_seen[:2] == [tailwindweekly.ARCHIVE_URL, issue_url]
    if issue_status == 200:
        assert len(requests_seen) == 2
        assert articles_seen == ["https://example.com/web"]
    else:
        assert requests_seen[2:] == [tailwindweekly.RSS_URL]
        assert articles_seen == ["https://example.com/240"]


def test_scrape_failed_issue_leaves_last_run_unchanged(scrape_sources):
    sources, _, articles_seen = scrape_sources
    sources[tailwindweekly.ARCHIVE_URL] = (200, '<a href="/issue-240/">Tailwind Weekly #240</a>')
    sources[f"{tailwindweekly.BASE_URL}/issue-240/"] = (200, "No article links")
    sources[tailwindweekly.RSS_URL] = (200, _rss(239))
    previous = {"full_url": f"{tailwindweekly.BASE_URL}/issue-239/"}
    update_last_run_info("tailwindweekly", previous)

    with pytest.raises(RuntimeError, match="issue-240/"):
        tailwindweekly.scrape_tailwindweekly()

    assert articles_seen == []
    assert load_last_run_info()["tailwindweekly"] == previous
