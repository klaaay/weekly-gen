from bs4 import BeautifulSoup

from src.frontendfoc import collect_issue_article_links, parse_latest_issue_info


def test_parse_latest_issue_info_supports_issue_card_markup():
    soup = BeautifulSoup(
        """
        <html>
          <body>
            <div class="issue-card">
              <span class="issue-ref">#741</span>
              <span class="issue-subject">
                <a href="/issues/741">A new HTML element for installing web apps</a>
              </span>
              <span class="issue-date">2026-05-13</span>
            </div>
          </body>
        </html>
        """,
        "html.parser",
    )

    issue_title, link_url = parse_latest_issue_info(soup)

    assert issue_title == "Issue #741"
    assert link_url == "issues/741"


def test_collect_issue_article_links_supports_direct_issue_links():
    soup = BeautifulSoup(
        """
        <html>
          <body>
            <a href="/issues">All Issues</a>
            <div id="content">
              <a href="https://webkit.org/blog/17938/webkit-features-for-safari-26-5/">
                <img src="hero.jpg" />
              </a>
              <table class="el-item item">
                <tr>
                  <td>
                    <p class="desc">
                      <span class="mainlink">
                        <a href="https://webkit.org/blog/17938/webkit-features-for-safari-26-5/">
                          Safari 26.5 Released
                        </a>
                      </span>
                    </p>
                  </td>
                </tr>
              </table>
              <table class="content el-md">
                <tr>
                  <td>
                    <ul>
                      <li>
                        <p>
                          <a href="https://tailwindcss.com/blog/tailwindcss-v4-3">
                            Tailwind CSS v4.3 is out
                          </a>
                        </p>
                      </li>
                    </ul>
                  </td>
                </tr>
              </table>
              <table class="footer">
                <tr>
                  <td>
                    <a href="https://frontendfoc.us/leave/*|UID|*">Stop getting this newsletter</a>
                  </td>
                </tr>
              </table>
            </div>
          </body>
        </html>
        """,
        "html.parser",
    )

    links = collect_issue_article_links(soup)

    assert [link.get_text(" ", strip=True) for link in links] == [
        "Safari 26.5 Released",
        "Tailwind CSS v4.3 is out",
    ]
    assert [link["href"] for link in links] == [
        "https://webkit.org/blog/17938/webkit-features-for-safari-26-5/",
        "https://tailwindcss.com/blog/tailwindcss-v4-3",
    ]
