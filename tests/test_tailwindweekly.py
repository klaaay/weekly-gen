from bs4 import BeautifulSoup

from src.tailwindweekly import collect_issue_article_links, parse_latest_issue_info


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
