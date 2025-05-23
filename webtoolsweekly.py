#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse, urljoin
from openai import OpenAI
from dotenv import load_dotenv
from utils.extract_links_and_summarize import extract_links_and_summarize
from utils.deepseek_api import translate_title_to_chinese, summarize_with_deepseek

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

def scrape_webtoolsweekly():
    # 确保 outputs 文件夹存在
    outputs_dir = "outputs"
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
        print(f"创建输出目录：{outputs_dir}")
        
    url = "https://webtoolsweekly.com/archive"
    
    # Add headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Set up proxy
    proxies = {
        'http': 'http://127.0.0.1:7897',
        'https': 'http://127.0.0.1:7897'
    }
    
    # Send GET request to the URL
    print(f"Using proxy: http://127.0.0.1:7897")
    response = requests.get(url, headers=headers, proxies=proxies)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        site_title = "Web Tools Weekly"
        safe_title = "webtoolsweekly"
        print(f"Title: {site_title}\n")
        
        # Create output files with title in the filename
        content_file = os.path.join(outputs_dir, f"{safe_title}_content.txt")
        summary_file = os.path.join(outputs_dir, f"{safe_title}_summary.md")  # Markdown 格式
        
        # Web Tools Weekly 的结构与 Node Weekly 不同
        # 我们查找第一个具有期号的链接
        # 根据网站内容，链接格式可能是 #612 等
        issue_links = soup.find_all('a', href=re.compile(r'^archives/'))
        
        if issue_links and len(issue_links) > 0:
            # 获取第一个链接（最新一期）
            issue_link = issue_links[0]
            link_url = issue_link['href'] if 'href' in issue_link.attrs else None
            issue_title = issue_link.text.strip()
            print(f"Found issue link: {issue_title} - {link_url}")
            
            # Sanitize issue title for filename - 确保移除换行符和其他无效字符
            issue_title = issue_title.replace('\n', ' ').replace('\r', ' ')
            safe_issue_title = re.sub(r'[^\w\s-]', '', issue_title).strip().replace(' ', '_')
            
            # 只创建文件名，不包含路径 - 路径将在 extract_links_and_summarize 函数中添加
            summary_file = f"{safe_title}_{safe_issue_title}_summary.md"  # Markdown 格式
            
            # 创建保存目录
            outputs_dir = "outputs"
            if not os.path.exists(outputs_dir):
                os.makedirs(outputs_dir)
                print(f"创建输出目录：{outputs_dir}")
            
            # If the URL is relative, make it absolute
            if link_url and not link_url.startswith('http'):
                link_url = urljoin("https://webtoolsweekly.com/", link_url)
            
            if link_url:
                # Send GET request to the linked page
                print(f"Fetching content from: {link_url}")
                link_response = requests.get(link_url, headers=headers, proxies=proxies)
                
                # Check if the request was successful
                if link_response.status_code == 200:
                    # Parse the HTML content of the linked page
                    link_soup = BeautifulSoup(link_response.text, 'html.parser')
                    
                    # 使用修改后的提取链接方式，直接获取所有链接而不是使用模式匹配
                    extract_links_and_summarize(
                        soup=link_soup,
                        headers=headers,
                        proxies=proxies,
                        summary_file=summary_file,
                        summary_title_prefix="webtoolsweekly",
                        base_url="https://webtoolsweekly.com",
                        fetch_content_func=fetch_page_content,
                        use_patterns=False  # 设置为 False，使用新的提取方式
                    )
                else:
                    print(f"Failed to retrieve the linked page. Status code: {link_response.status_code}")
            else:
                print("The issue link does not contain a valid URL.")
        else:
            print("No issue links matching the pattern found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_webtoolsweekly() 