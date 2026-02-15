#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse
from openai import OpenAI
from dotenv import load_dotenv
from src.utils.proxy import get_proxies, proxy_for_log
from src.utils.extract_links_and_summarize import extract_links_and_summarize
from src.utils.deepseek_api import translate_title_to_chinese, summarize_with_deepseek
from src.utils.last_run_tracker import check_and_skip_if_same_issue, create_issue_info, update_last_run_info

# 加载.env 文件中的环境变量
load_dotenv()

# 初始化 OpenAI 客户端，指向 DeepSeek API
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=os.getenv("DEEPSEEK_BASE_URL"))

def fetch_page_content(url, headers, proxies):
    """Fetch content from a URL, following redirects."""
    try:
        # Set allow_redirects to True to follow redirects
        response = requests.get(url, headers=headers, proxies=proxies, allow_redirects=True)
        
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
            else:
                return {
                    "title": "Non-HTML content",
                    "chinese_title": "非 HTML 内容",
                    "url": final_url,
                    "content": "Non-HTML content (possibly PDF, image or other format)",
                    "summary": "无法总结：非 HTML 内容。"
                }
        else:
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

def scrape_reactweekly():
    # 确保 outputs 文件夹存在
    outputs_dir = "outputs"
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
        print(f"创建输出目录：{outputs_dir}")
        
    url = "https://react.statuscode.com/issues"
    
    # Add headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Set up proxy
    proxies = get_proxies()
    
    # Send GET request to the URL
    print(f"Using proxy: {proxy_for_log()}")
    response = requests.get(url, headers=headers, proxies=proxies)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.find('h1')
        if title:
            site_title = title.text.strip()
            print(f"Title: {site_title}\n")
            # Sanitize title for filename
            safe_title = re.sub(r'[^\w\s-]', '', site_title).strip().replace(' ', '_')
        else:
            site_title = "React Weekly"
            safe_title = "reactweekly"
        
        # Create output files with title in the filename
        content_file = os.path.join(outputs_dir, f"{safe_title}_content.txt")
        summary_file = os.path.join(outputs_dir, f"{safe_title}_summary.md")  # Markdown 格式
        
        # Find the first issue link - 新页面结构: href="/issues/462", 链接文本是文章标题
        issue_link = soup.find('a', href=re.compile(r'^/issues/\d+$'))
        
        if issue_link and 'href' in issue_link.attrs:
            link_url = issue_link['href']
            # 从 href 提取 issue 号，用于 issue_title（如 /issues/462 -> Issue #462）
            issue_num_match = re.search(r'/issues/(\d+)$', link_url)
            issue_title = f"Issue #{issue_num_match.group(1)}" if issue_num_match else issue_link.text.strip()
            # 统一 link_url 格式为 issues/462（无前导斜杠），与 last_run_info 兼容
            if link_url.startswith('/'):
                link_url = link_url.lstrip('/')
            print(f"Found issue link: {issue_link.text} - {link_url}")
            
            # 检查是否与上次抓取的 link_url 相同
            script_name = os.path.basename(__file__).replace('.py', '')  # 获取脚本名称（不含.py 扩展名）
            
            # 如果检测到相同的 link_url，则跳过执行
            if check_and_skip_if_same_issue(script_name, link_url):
                return
            
            # 记录上次运行抓取的 issue_link 信息
            issue_info = create_issue_info(issue_title, link_url, "https://react.statuscode.com")
            update_last_run_info(script_name, issue_info)
            
            # Sanitize issue title for filename
            safe_issue_title = re.sub(r'[^\w\s-]', '', issue_title).strip().replace(' ', '_')
            
            # Create output file with site title and issue title in the filename
            summary_file = f"{safe_title}_{safe_issue_title}_summary.md"  # Markdown 格式
            
            # If the URL is relative, make it absolute
            if not link_url.startswith('http'):
                link_url = f"https://react.statuscode.com/{link_url}"
            
            # Send GET request to the linked page
            print(f"Fetching content from: {link_url}")
            link_response = requests.get(link_url, headers=headers, proxies=proxies)
            
            # Check if the request was successful
            if link_response.status_code == 200:
                
                # Parse the HTML content of the linked page
                link_soup = BeautifulSoup(link_response.text, 'html.parser')
                
                # 页面已改版：无 /link 跟踪链接，文章为直接外链。预筛选 body 下的文章链接
                excluded_domains = (
                    'react.statuscode.com', 'frontendmasters.com', 'stateofreact.com',
                    '2025.stateofreact.com', 'reactweekly.com'
                )
                pre_filtered_links = []
                seen_urls = set()
                for a in (link_soup.body or link_soup).find_all('a', href=True):
                    href = a.get('href', '').strip()
                    text = a.get_text(strip=True)
                    if not href.startswith('https://') or len(text) < 15:
                        continue
                    try:
                        domain = urlparse(href).netloc.lower()
                        if any(exc in domain for exc in excluded_domains):
                            continue
                    except Exception:
                        continue
                    if href in seen_urls:
                        continue
                    seen_urls.add(href)
                    pre_filtered_links.append(a)
                
                # 使用提取的函数来处理链接
                extract_links_and_summarize(
                    soup=link_soup,
                    headers=headers,
                    proxies=proxies,
                    summary_file=summary_file,
                    summary_title_prefix="reactweekly",
                    base_url="https://react.statuscode.com",
                    fetch_content_func=fetch_page_content,
                    pre_filtered_links=pre_filtered_links
                )
            else:
                print(f"Failed to retrieve the linked page. Status code: {link_response.status_code}")
        else:
            print("No issue links matching the pattern found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_reactweekly() 
