#!/usr/bin/env python3
import os
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse
from xml.etree import ElementTree

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from src.utils.deepseek_api import summarize_with_deepseek, translate_title_to_chinese
from src.utils.extract_links_and_summarize import extract_links_and_summarize
from src.utils.last_run_tracker import (
    check_and_skip_if_same_issue,
    create_issue_info,
    update_last_run_info,
)
from src.utils.proxy import get_proxies, proxy_for_log
from src.utils.telegram_notifier import create_telegram_completion_callback

load_dotenv()

BASE_URL = "https://tailwindweekly.com"
ARCHIVE_URL = f"{BASE_URL}/"
RSS_URL = f"{BASE_URL}/rss/"
RSS_CONTENT = "{http://purl.org/rss/1.0/modules/content/}encoded"
SITE_TITLE = "Tailwind Weekly"
SAFE_TITLE = "tailwindweekly"
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}
EXCLUDED_DOMAINS = {
    "tailwindweekly.com",
    "www.tailwindweekly.com",
    "x.com",
    "www.x.com",
    "twitter.com",
    "www.twitter.com",
    "facebook.com",
    "www.facebook.com",
    "linkedin.com",
    "www.linkedin.com",
    "pinterest.com",
    "www.pinterest.com",
    "forms.gle",
    "buymeacoffee.com",
    "www.buymeacoffee.com",
}
EXCLUDED_LINK_TEXTS = {
    "link",
    "submit a link",
    "@vivgui",
    "share on x",
    "share on facebook",
    "share on linkedin",
}
TRACKING_QUERY_PARAMS = {"ref", "ref_src", "utm_source", "utm_medium", "utm_campaign"}


def parse_latest_issue_info(soup: BeautifulSoup):
    """从首页 Latest 卡片中提取最新一期标题和链接。"""
    issue_link = None
    for candidate in soup.select("article.card-post h2.card-title a[href]"):
        title = candidate.get_text(" ", strip=True)
        href = candidate.get("href", "").strip()
        if re.search(r"Tailwind Weekly #\d+", title) and href.startswith("/"):
            issue_link = candidate
            break

    if not issue_link:
        issue_link = soup.find("a", href=re.compile(r"^/issue-\d+/$"))

    if not issue_link:
        return None, None

    issue_title = issue_link.get_text(" ", strip=True)
    link_url = issue_link.get("href", "").strip().lstrip("/")
    return issue_title, link_url


def _fetch_weekly_source(url, proxies):
    try:
        response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies, timeout=30)
    except requests.RequestException as exc:
        print(f"Tailwind Weekly 来源请求失败：{url}（{type(exc).__name__}）")
        return None

    if response.status_code != 200 or response.headers.get("CF-Mitigated") == "challenge":
        print(f"Tailwind Weekly 来源不可用：{url}（HTTP {response.status_code}）")
        return None
    return response


def _fetch_rss_issue(proxies, link_url=None):
    """读取 RSS 最新一期，或按网页选出的链接查找同一期正文。"""
    response = _fetch_weekly_source(RSS_URL, proxies)
    if response is None:
        return None

    try:
        feed = ElementTree.fromstring(response.content)
    except ElementTree.ParseError:
        print("Tailwind Weekly RSS 返回了无法解析的 XML")
        return None

    expected_path = urlparse(link_url).path.strip("/") if link_url else None
    for item in feed.findall("./channel/item"):
        title = item.findtext("title", "").strip()
        if not re.match(r"Tailwind Weekly #\d+\b", title):
            continue
        url = urlparse(urljoin(ARCHIVE_URL, item.findtext("link", "").strip()))
        path = url.path.lstrip("/")
        if url.hostname not in {"tailwindweekly.com", "www.tailwindweekly.com"} or not path:
            continue
        if expected_path is not None and path.rstrip("/") != expected_path:
            continue
        return title, path, item.findtext(RSS_CONTENT, "")
    return None


def _normalized_url_for_dedupe(url: str) -> str:
    """去除常见跟踪参数后用于去重，保留原始 href 供后续抓取。"""
    parsed = urlparse(url)
    filtered_query = [
        (key, value)
        for key, value in parse_qsl(parsed.query, keep_blank_values=True)
        if key.lower() not in TRACKING_QUERY_PARAMS
    ]
    return urlunparse(parsed._replace(query=urlencode(filtered_query, doseq=True))).rstrip("/")


def _is_excluded_domain(domain: str) -> bool:
    return domain in EXCLUDED_DOMAINS or any(
        domain.endswith(f".{excluded}") for excluded in EXCLUDED_DOMAINS
    )


def collect_issue_article_links(soup: BeautifulSoup):
    """抽取 Tailwind Weekly 正文中的外部内容链接，过滤站内、分享和投稿链接。"""
    content = soup.select_one(".post-content") or soup.find("article") or soup.body or soup
    collected_links = []
    seen_urls = set()

    for link in content.find_all("a", href=True):
        href = link.get("href", "").strip()
        text = link.get_text(" ", strip=True)
        text_key = text.lower()

        if not href.startswith(("http://", "https://")) or not text:
            continue
        if text_key in EXCLUDED_LINK_TEXTS:
            continue

        domain = urlparse(href).netloc.lower()
        if _is_excluded_domain(domain):
            continue

        dedupe_url = _normalized_url_for_dedupe(href)
        if dedupe_url in seen_urls:
            continue

        seen_urls.add(dedupe_url)
        collected_links.append(link)

    return collected_links


def fetch_page_content(url, headers, proxies):
    """抓取外链正文并调用摘要模型生成总结。"""
    try:
        response = requests.get(
            url,
            headers=headers,
            proxies=proxies,
            allow_redirects=True,
            timeout=30,
        )

        if response.status_code != 200:
            return {
                "title": "Failed to retrieve",
                "chinese_title": "获取失败",
                "url": url,
                "content": f"Failed to retrieve content. Status code: {response.status_code}",
                "summary": f"无法总结：获取内容失败，状态码 {response.status_code}。",
            }

        final_url = response.url
        print(f"  Fetched from final URL: {final_url}")

        content_type = response.headers.get("Content-Type", "").lower()
        if "text/html" not in content_type:
            return {
                "title": "Non-HTML content",
                "chinese_title": "非 HTML 内容",
                "url": final_url,
                "content": "Non-HTML content (possibly PDF, image or other format)",
                "summary": "无法总结：非 HTML 内容。",
            }

        article_soup = BeautifulSoup(response.text, "html.parser")
        for script in article_soup(["script", "style"]):
            script.extract()

        title = article_soup.title.string if article_soup.title else "No title found"
        chinese_title = translate_title_to_chinese(title)
        main_content = (
            article_soup.find("main")
            or article_soup.find("article")
            or article_soup.find("div", class_="content")
            or article_soup.body
        )

        if not main_content:
            return {
                "title": title,
                "chinese_title": chinese_title,
                "url": final_url,
                "content": "No main content found.",
                "summary": "无法总结：未找到主要内容。",
            }

        text = main_content.get_text(separator="\n", strip=True)
        text = re.sub(r"\n{3,}", "\n\n", text)
        summary = summarize_with_deepseek(text)

        return {
            "title": title,
            "chinese_title": chinese_title,
            "url": final_url,
            "content": text,
            "summary": summary,
        }
    except Exception as e:
        return {
            "title": "Error",
            "chinese_title": "错误",
            "url": url,
            "content": f"Error fetching content: {str(e)}",
            "summary": f"无法总结：获取内容时出错 - {str(e)}",
        }


def scrape_tailwindweekly():
    proxies = get_proxies()
    print(f"Using proxy: {proxy_for_log()}")
    response = _fetch_weekly_source(ARCHIVE_URL, proxies)
    issue_title, link_url = (None, None)
    rss_issue = None
    if response is not None:
        issue_title, link_url = parse_latest_issue_info(BeautifulSoup(response.text, "html.parser"))

    if not link_url:
        print("Tailwind Weekly 首页未能定位最新一期，改用官方 RSS")
        rss_issue = _fetch_rss_issue(proxies)
        if rss_issue is None:
            raise RuntimeError("首页和 RSS 均未能定位 Tailwind Weekly 最新一期")
        issue_title, link_url, _ = rss_issue

    print(f"Title: {SITE_TITLE}\n")
    print(f"Found issue link: {issue_title} - {link_url}")

    safe_issue_title = re.sub(r"[^\w\s-]", "", issue_title).strip().replace(" ", "_")
    summary_file = f"{SAFE_TITLE}_{safe_issue_title}_summary.md"
    existing_summaries = Path("outputs").glob(f"????-??-??_{SAFE_TITLE}_{summary_file}")
    if any(existing_summaries) and check_and_skip_if_same_issue(SAFE_TITLE, link_url, BASE_URL):
        return

    issue_soup = BeautifulSoup("", "html.parser")
    if rss_issue is None:
        issue_url = urljoin(ARCHIVE_URL, link_url)
        print(f"Fetching content from: {issue_url}")
        issue_response = _fetch_weekly_source(issue_url, proxies)
        if issue_response is not None:
            issue_soup = BeautifulSoup(issue_response.text, "html.parser")
    pre_filtered_links = collect_issue_article_links(issue_soup)

    if not pre_filtered_links:
        if rss_issue is None:
            print("Tailwind Weekly 网页正文缺少可用外链，改用官方 RSS 查找同一期")
            rss_issue = _fetch_rss_issue(proxies, link_url)
        if rss_issue is not None:
            issue_soup = BeautifulSoup(rss_issue[2], "html.parser")
            pre_filtered_links = collect_issue_article_links(issue_soup)
            print(f"Tailwind Weekly RSS 正文提取到 {len(pre_filtered_links)} 个外链")
        if not pre_filtered_links:
            raise RuntimeError(f"Tailwind Weekly 本期正文缺少可用外链：{link_url}")
    else:
        print(f"Found {len(pre_filtered_links)} article links in issue page")

    extract_links_and_summarize(
        soup=issue_soup,
        headers=REQUEST_HEADERS,
        proxies=proxies,
        summary_file=summary_file,
        summary_title_prefix=SAFE_TITLE,
        base_url=BASE_URL,
        fetch_content_func=fetch_page_content,
        pre_filtered_links=pre_filtered_links,
        on_complete=create_telegram_completion_callback("Tailwind Weekly"),
        atomic_summary=True,
    )
    update_last_run_info(SAFE_TITLE, create_issue_info(issue_title, link_url, BASE_URL))


if __name__ == "__main__":
    scrape_tailwindweekly()
