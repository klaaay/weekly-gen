from bs4 import BeautifulSoup

import src.thisweekinreact as thisweekinreact


def test_collect_issue_article_links_keeps_markdown_links_with_empty_class():
    soup = BeautifulSoup(
        """
        <html>
          <body>
            <a class="navbar__link" target="_blank" href="https://slo.im/thread">
              Thread
            </a>
            <div id="__blog-post-container" class="markdown">
              <p>
                <a class="" target="_blank" href="https://slo.im/last/b">
                  Bluesky
                </a>
              </p>
              <figure class="tweetQuote_h8Rz">
                <blockquote>
                  <a target="_blank" href="https://twitter.com/TkDodo/status/1">
                    I'm constantly finding interesting things to learn in there.
                  </a>
                </blockquote>
              </figure>
              <p>
                <a class="" target="_blank" href="https://www.meticulous.ai">
                  Still writing tests manually?
                </a>
              </p>
              <ul>
                <li>
                  <a class="" target="_blank" href="https://socket.dev/blog/tanstack">
                    Malicious npm Package Brand-Squats TanStack
                  </a>
                </li>
                <li>
                  <a class="" target="_blank" href="https://x.com/react/status/1">
                    X thread
                  </a>
                </li>
                <li>
                  <a class="" target="_self" href="https://example.com/self">
                    Self target
                  </a>
                </li>
              </ul>
            </div>
          </body>
        </html>
        """,
        "html.parser",
    )

    links = thisweekinreact.collect_issue_article_links(soup)

    assert [link.get_text(" ", strip=True) for link in links] == [
        "Still writing tests manually?",
        "Malicious npm Package Brand-Squats TanStack",
    ]
    assert [link["href"] for link in links] == [
        "https://www.meticulous.ai",
        "https://socket.dev/blog/tanstack",
    ]


def test_fetch_page_content_uses_github_raw_markdown_for_blob_links(monkeypatch):
    class FakeResponse:
        def __init__(self, status_code, url, text, content_type):
            self.status_code = status_code
            self.url = url
            self.text = text
            self.headers = {"Content-Type": content_type}

    requested_urls = []

    def fake_get(url, **kwargs):
        requested_urls.append(url)
        return FakeResponse(
            200,
            url,
            """
            # React Router Releases

            ## v7.15.0

            Stabilized APIs and improved route matching.

            ## v7.14.2

            Previous release notes.
            """,
            "text/plain; charset=utf-8",
        )

    monkeypatch.setattr(thisweekinreact.requests, "get", fake_get)
    monkeypatch.setattr(thisweekinreact, "translate_title_to_chinese", lambda title: f"中文:{title}")
    monkeypatch.setattr(
        thisweekinreact,
        "summarize_with_deepseek",
        lambda content: f"summary:{content.strip()}",
    )

    article = thisweekinreact.fetch_page_content(
        "https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v7150",
        headers={},
        proxies={},
    )

    assert requested_urls == ["https://raw.githubusercontent.com/remix-run/react-router/main/CHANGELOG.md"]
    assert article["url"] == "https://raw.githubusercontent.com/remix-run/react-router/main/CHANGELOG.md"
    assert article["title"] == "CHANGELOG.md"
    assert "Stabilized APIs" in article["summary"]
    assert "Previous release notes" not in article["summary"]
