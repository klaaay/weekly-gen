#!/usr/bin/env python3
import os
import re
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse

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

load_dotenv()

BASE_URL = "https://tailwindweekly.com"
ARCHIVE_URL = f"{BASE_URL}/"
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
    issue_link = soup.select_one('article.card-post h2.card-title a[href^="/issue-"]')
    if not issue_link:
        issue_link = soup.find("a", href=re.compile(r"^/issue-\d+/$"))

    if not issue_link:
        return None, None

    issue_title = issue_link.get_text(" ", strip=True)
    link_url = issue_link.get("href", "").strip().lstrip("/")
    return issue_title, link_url


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
    outputs_dir = "outputs"
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
        print(f"创建输出目录：{outputs_dir}")

    proxies = get_proxies()
    print(f"Using proxy: {proxy_for_log()}")
    response = requests.get(ARCHIVE_URL, headers=REQUEST_HEADERS, proxies=proxies, timeout=30)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    issue_title, link_url = parse_latest_issue_info(soup)

    if not link_url:
        print("No issue links matching the pattern found on the page.")
        return

    print(f"Title: {SITE_TITLE}\n")
    print(f"Found issue link: {issue_title} - {link_url}")

    script_name = os.path.basename(__file__).replace(".py", "")
    if check_and_skip_if_same_issue(script_name, link_url, BASE_URL):
        return

    issue_info = create_issue_info(issue_title, link_url, BASE_URL)
    update_last_run_info(script_name, issue_info)

    safe_issue_title = re.sub(r"[^\w\s-]", "", issue_title).strip().replace(" ", "_")
    summary_file = f"{SAFE_TITLE}_{safe_issue_title}_summary.md"
    issue_url = urljoin(f"{BASE_URL}/", link_url)

    print(f"Fetching content from: {issue_url}")
    issue_response = requests.get(issue_url, headers=REQUEST_HEADERS, proxies=proxies, timeout=30)
    if issue_response.status_code != 200:
        print(f"Failed to retrieve the linked page. Status code: {issue_response.status_code}")
        return

    issue_soup = BeautifulSoup(issue_response.text, "html.parser")
    pre_filtered_links = collect_issue_article_links(issue_soup)
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
    )


if __name__ == "__main__":
    scrape_tailwindweekly()
