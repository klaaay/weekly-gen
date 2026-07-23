#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse, urljoin
from openai import OpenAI
from dotenv import load_dotenv
from src.utils.proxy import get_proxies, proxy_for_log
from src.utils.deepseek_api import translate_title_to_chinese, summarize_with_deepseek
from src.utils.extract_links_and_summarize import extract_links_and_summarize
from src.utils.last_run_tracker import check_and_skip_if_same_issue, create_issue_info, update_last_run_info
from src.utils.telegram_notifier import create_telegram_completion_callback

# 加载.env 文件中的环境变量
load_dotenv()

# 初始化 OpenAI 客户端，指向 DeepSeek API
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=os.getenv("DEEPSEEK_BASE_URL"))

BASE_URL = "https://thisweekinreact.com"
NEWSLETTER_URL = f"{BASE_URL}/newsletter"
SAFE_TITLE = "thisweekinreact"
REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
EXCLUDED_DOMAINS = {
    "x.com",
    "www.x.com",
    "twitter.com",
    "www.twitter.com",
    "slo.im",
    "www.slo.im",
}


def parse_latest_issue_info(soup):
    """从列表页提取最新一期 newsletter 信息。"""
    newsletter_link = soup.find('a', href=re.compile(r'^/newsletter/\d+$'))
    if not newsletter_link or 'href' not in newsletter_link.attrs:
        return None, None

    issue_title = newsletter_link.get_text(" ", strip=True) or "Newsletter"
    return issue_title, newsletter_link['href']


def has_parent_class_prefix(node, prefix):
    """判断节点祖先是否包含指定 class 前缀。"""
    for parent in node.parents:
        classes = parent.get("class", []) if hasattr(parent, "get") else []
        if any(class_name.startswith(prefix) for class_name in classes):
            return True
    return False


def collect_issue_article_links(soup):
    """收集正文中的外部内容链接，排除推荐语、社交和导航链接。"""
    content = soup.find(id="__blog-post-container") or soup
    collected_links = []
    seen_urls = set()

    for link in content.select('a[target="_blank"][href]'):
        href = link.get("href", "").strip()
        text = link.get_text(" ", strip=True)
        if not href.startswith(("http://", "https://")) or not text:
            continue

        domain = urlparse(href).netloc.lower()
        if domain in EXCLUDED_DOMAINS:
            continue

        if has_parent_class_prefix(link, "tweetQuote"):
            continue

        if href in seen_urls:
            continue

        seen_urls.add(href)
        collected_links.append(link)

    return collected_links


def github_blob_to_raw_url(url):
    """将 GitHub blob 文档链接转换为 raw 链接。"""
    parsed = urlparse(url)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return None

    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 5 or path_parts[2] != "blob":
        return None

    owner, repo, _, ref, *file_parts = path_parts
    if not file_parts:
        return None

    return f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{'/'.join(file_parts)}"


def markdown_heading_anchor(heading):
    """生成与 GitHub Markdown 接近的标题锚点。"""
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = re.sub(r"[`*_~]", "", heading)
    heading = heading.strip().lower()
    heading = re.sub(r"[^\w\s-]", "", heading)
    heading = re.sub(r"\s+", "-", heading)
    return heading


def extract_markdown_section(text, fragment):
    """按 GitHub 标题锚点提取 Markdown 小节。"""
    if not fragment:
        return text

    target_anchor = fragment.lower()
    lines = text.splitlines()
    start_index = None
    heading_level = None

    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line.strip())
        if not match:
            continue

        if markdown_heading_anchor(match.group(2)) == target_anchor:
            start_index = index
            heading_level = len(match.group(1))
            break

    if start_index is None:
        return text

    section_lines = []
    for line in lines[start_index:]:
        match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line.strip())
        if section_lines and match and len(match.group(1)) <= heading_level:
            break
        section_lines.append(line)

    return "\n".join(section_lines).strip() or text


def summarize_plain_text_response(response, source_url, fragment=""):
    """总结纯文本或 Markdown 内容。"""
    title = os.path.basename(urlparse(source_url).path) or "Text content"
    chinese_title = translate_title_to_chinese(title)
    text = extract_markdown_section(response.text, fragment)
    text = re.sub(r'\n{3,}', '\n\n', text)
    summary = summarize_with_deepseek(text)

    return {
        "title": title,
        "chinese_title": chinese_title,
        "url": source_url,
        "content": text,
        "summary": summary
    }


def fetch_page_content(url, headers, proxies):
    """Fetch content from a URL, following redirects."""
    try:
        raw_url = github_blob_to_raw_url(url)
        if raw_url:
            raw_response = requests.get(
                raw_url,
                headers=headers,
                proxies=proxies,
                allow_redirects=True,
                timeout=30,
            )
            if raw_response.status_code == 200:
                print(f"  Fetched from GitHub raw URL: {raw_url}")
                return summarize_plain_text_response(
                    raw_response,
                    raw_url,
                    fragment=urlparse(url).fragment,
                )

        # Set allow_redirects to True to follow redirects
        response = requests.get(url, headers=headers, proxies=proxies, allow_redirects=True, timeout=30)
        
        if response.status_code == 200:
            # Get the final URL after redirects
            final_url = response.url
            print(f"  Fetched from final URL: {final_url}")
            
            # Parse the content based on content type
            content_type = response.headers.get('Content-Type', '').lower()
            
            if 'text/html' in content_type:
                # Parse HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.extract()
                
                # Extract the title
                title = soup.title.string if soup.title else "No title found"
                
                # 翻译标题为中文
                chinese_title = translate_title_to_chinese(title)
                
                # Extract the main content (this is a simple approach)
                # Get text from body or main content area if available
                main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content') or soup.body
                
                if main_content:
                    # Get clean text
                    text = main_content.get_text(separator='\n', strip=True)
                    # Remove multiple newlines
                    text = re.sub(r'\n{3,}', '\n\n', text)
                    
                    # 使用 DeepSeek API 进行总结
                    summary = summarize_with_deepseek(text)
                    
                    return {
                        "title": title,
                        "chinese_title": chinese_title,
                        "url": final_url,
                        "content": text,
                        "summary": summary
                    }
                else:
                    return {
                        "title": title,
                        "chinese_title": chinese_title,
                        "url": final_url,
                        "content": "No main content found.",
                        "summary": "无法总结：未找到主要内容。"
                    }
            elif 'text/plain' in content_type or 'markdown' in content_type or final_url.endswith(('.md', '.txt')):
                return summarize_plain_text_response(
                    response,
                    final_url,
                    fragment=urlparse(url).fragment,
                )
            else:
                return {
                    "title": "Non-HTML content",
                    "chinese_title": "非 HTML 内容",
                    "url": final_url,
                    "content": "Non-HTML content (possibly PDF, image or other format)",
                    "summary": "无法总结：非 HTML 内容。"
                }
        else:
            if raw_url:
                raw_response = requests.get(
                    raw_url,
                    headers=headers,
                    proxies=proxies,
                    allow_redirects=True,
                    timeout=30,
                )
                if raw_response.status_code == 200:
                    print(f"  Fetched from GitHub raw URL: {raw_url}")
                    return summarize_plain_text_response(
                        raw_response,
                        raw_url,
                        fragment=urlparse(url).fragment,
                    )

            return {
                "title": "Failed to retrieve",
                "chinese_title": "获取失败",
                "url": url,
                "content": f"Failed to retrieve content. Status code: {response.status_code}",
                "summary": f"无法总结：获取内容失败，状态码 {response.status_code}。"
            }
    except Exception as e:
        return {
            "title": "Error",
            "chinese_title": "错误",
            "url": url,
            "content": f"Error fetching content: {str(e)}",
            "summary": f"无法总结：获取内容时出错 - {str(e)}"
        }

def scrape_thisweekinreact():
    # 确保 outputs 文件夹存在
    outputs_dir = "outputs"
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
        print(f"创建输出目录：{outputs_dir}")
        
    # Set up proxy
    proxies = get_proxies()
    
    # Send GET request to the URL
    print(f"Using proxy: {proxy_for_log()}")
    print(f"Fetching content from: {NEWSLETTER_URL}")
    
    try:
        # 获取主页内容
        response = requests.get(NEWSLETTER_URL, headers=REQUEST_HEADERS, proxies=proxies, allow_redirects=True)
        
        if response.status_code == 200:
            # 解析 HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 创建安全的文件名
            safe_title = SAFE_TITLE
                
            # 创建主页输出文件
            summary_file = os.path.join(outputs_dir, f"{safe_title}_summary.md")
            
            print(f"主页摘要已保存到：{summary_file}")
            
            # 1. 查找第一个以 /newsletter/数字 格式的链接
            issue_title, newsletter_url = parse_latest_issue_info(soup)
            
            if newsletter_url:
                
                # 检查是否与上次抓取的 link_url 相同
                script_name = os.path.basename(__file__).replace('.py', '')  # 获取脚本名称（不含.py 扩展名）
                
                # 如果检测到相同的 full_url，则跳过执行
                if check_and_skip_if_same_issue(script_name, newsletter_url, BASE_URL):
                    return
                
                # 记录上次运行抓取的 newsletter 信息
                issue_info = create_issue_info(issue_title, newsletter_url, BASE_URL)
                update_last_run_info(script_name, issue_info)
                
                # 确保链接是绝对路径
                if not newsletter_url.startswith('http'):
                    newsletter_url = f"{BASE_URL}{newsletter_url}"
                
                print(f"\n找到 newsletter 链接：{newsletter_url}")
                print(f"获取 newsletter 页面内容...")
                
                # 2. 获取这个 newsletter 页面的内容
                newsletter_response = requests.get(newsletter_url, headers=REQUEST_HEADERS, proxies=proxies, allow_redirects=True)
                
                if newsletter_response.status_code == 200:
                    # 解析 newsletter 页面
                    newsletter_soup = BeautifulSoup(newsletter_response.text, 'html.parser')
                    
                    print("\n开始提取文章链接并生成摘要...")
                    
                    # 3. 从 newsletter 正文中提取真实内容链接
                    filtered_links = collect_issue_article_links(newsletter_soup)
                    print(f"\n在 newsletter 页面找到 {len(filtered_links)} 个符合条件的链接")
                    
                    # 4. 使用预先筛选好的链接集合
                    extract_links_and_summarize(
                        soup=newsletter_soup,  # 传递 newsletter 页面的 soup 对象
                        headers=REQUEST_HEADERS,
                        proxies=proxies,
                        summary_file=summary_file,
                        summary_title_prefix="thisweekinreact",
                        base_url=BASE_URL,
                        fetch_content_func=fetch_page_content,
                        use_patterns=False,  # 不使用模式匹配
                        pre_filtered_links=filtered_links,  # 使用预先筛选好的链接
                        on_complete=create_telegram_completion_callback("This Week in React"),
                    )
                    
                    print(f"\n文章总结已保存到：{os.path.join(outputs_dir, summary_file)}")
                else:
                    print(f"获取 newsletter 页面失败，状态码：{newsletter_response.status_code}")
            else:
                print("\n未找到以 /newsletter/数字 格式的链接")
                # print("尝试直接从主页提取文章链接...")
                
                # 如果找不到 newsletter 链接，则尝试直接从主页提取链接
                # extract_links_and_summarize(
                #     soup=soup,
                #     headers=headers,
                #     proxies=proxies,
                #     summary_file=summary_file,
                #     summary_title_prefix="thisweekinreact",
                #     base_url="https://thisweekinreact.com",
                #     fetch_content_func=fetch_page_content,
                #     use_patterns=False  # 不使用模式匹配
                # )
                
                # print(f"\n文章总结已保存到：{os.path.join(outputs_dir, summary_file)}")
        else:
            print(f"获取页面失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    scrape_thisweekinreact() 
