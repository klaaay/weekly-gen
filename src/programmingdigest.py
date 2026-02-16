#!/usr/bin/env python3
import os
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

from src.utils.deepseek_api import summarize_with_deepseek, translate_title_to_chinese
from src.utils.extract_links_and_summarize import extract_links_and_summarize
from src.utils.last_run_tracker import (
    check_and_skip_if_same_issue,
    create_issue_info,
    update_last_run_info,
)
from src.utils.proxy import get_proxies, proxy_for_log

# 加载.env 文件中的环境变量
load_dotenv()

# 初始化 OpenAI 客户端，指向 DeepSeek API
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=os.getenv("DEEPSEEK_BASE_URL"))


def fetch_page_content(url, headers, proxies):
    """Fetch content from a URL, following redirects."""
    try:
        response = requests.get(url, headers=headers, proxies=proxies, allow_redirects=True)

        if response.status_code == 200:
            final_url = response.url
            print(f"  Fetched from final URL: {final_url}")

            content_type = response.headers.get("Content-Type", "").lower()

            if "text/html" in content_type:
                soup = BeautifulSoup(response.text, "html.parser")

                for script in soup(["script", "style"]):
                    script.extract()

                title = soup.title.string if soup.title else "No title found"
                chinese_title = translate_title_to_chinese(title)

                main_content = (
                    soup.find("main")
                    or soup.find("article")
                    or soup.find("div", class_="content")
                    or soup.body
                )

                if main_content:
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

                return {
                    "title": title,
                    "chinese_title": chinese_title,
                    "url": final_url,
                    "content": "No main content found.",
                    "summary": "无法总结：未找到主要内容。",
                }

            return {
                "title": "Non-HTML content",
                "chinese_title": "非 HTML 内容",
                "url": final_url,
                "content": "Non-HTML content (possibly PDF, image or other format)",
                "summary": "无法总结：非 HTML 内容。",
            }

        return {
            "title": "Failed to retrieve",
            "chinese_title": "获取失败",
            "url": url,
            "content": f"Failed to retrieve content. Status code: {response.status_code}",
            "summary": f"无法总结：获取内容失败，状态码 {response.status_code}。",
        }
    except Exception as e:
        return {
            "title": "Error",
            "chinese_title": "错误",
            "url": url,
            "content": f"Error fetching content: {str(e)}",
            "summary": f"无法总结：获取内容时出错 - {str(e)}",
        }


def scrape_programmingdigest():
    outputs_dir = "outputs"
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
        print(f"创建输出目录：{outputs_dir}")

    base_url = "https://programmingdigest.net"
    url = f"{base_url}/"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    proxies = get_proxies()

    print(f"Using proxy: {proxy_for_log()}")
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    site_title = "Programming Digest"
    safe_title = "programmingdigest"
    print(f"Title: {site_title}\n")

    issue_link = soup.find("a", href=re.compile(r"^/newsletters/\d+"))

    if not issue_link or "href" not in issue_link.attrs:
        print("No newsletter link found on the page.")
        return

    link_url = issue_link["href"]
    if link_url.startswith("/"):
        link_url = link_url.lstrip("/")
    link_text = issue_link.text.strip() or "latest_issue"
    print(f"Found newsletter link: {link_text} - {link_url}")

    script_name = os.path.basename(__file__).replace(".py", "")
    if check_and_skip_if_same_issue(script_name, link_url):
        return

    issue_info = create_issue_info(link_text, link_url, base_url)
    update_last_run_info(script_name, issue_info)

    safe_link_text = re.sub(r"[^\w\s-]", "", link_text).strip().replace(" ", "_")
    summary_file = f"{safe_title}_{safe_link_text}_summary.md"

    issue_url = urljoin(f"{base_url}/", link_url)
    print(f"Fetching content from: {issue_url}")
    link_response = requests.get(issue_url, headers=headers, proxies=proxies)

    if link_response.status_code != 200:
        print(f"Failed to retrieve the linked page. Status code: {link_response.status_code}")
        return

    link_soup = BeautifulSoup(link_response.text, "html.parser")

    campaign = link_soup.find("div", class_="campaign")
    candidate_links = campaign.find_all("a", href=True) if campaign else []

    # 只保留外部文章链接，避免抓取站内跳转链接
    filtered_links = []
    seen_urls = set()
    for link in candidate_links:
        href = link.get("href", "").strip()
        if not href:
            continue

        normalized_url = urljoin(base_url, href)
        domain = urlparse(normalized_url).netloc.lower()
        if domain == urlparse(base_url).netloc.lower():
            continue
        if normalized_url in seen_urls:
            continue

        seen_urls.add(normalized_url)
        filtered_links.append(link)

    print(f"Filtered {len(filtered_links)} article links from campaign section.")
    if not filtered_links:
        print("No external article links found in campaign section.")
        return

    extract_links_and_summarize(
        soup=link_soup,
        headers=headers,
        proxies=proxies,
        summary_file=summary_file,
        summary_title_prefix=safe_title,
        base_url=base_url,
        fetch_content_func=fetch_page_content,
        use_patterns=False,
        pre_filtered_links=filtered_links,
    )


if __name__ == "__main__":
    scrape_programmingdigest()
