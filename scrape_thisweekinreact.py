#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse, urljoin
from openai import OpenAI
from dotenv import load_dotenv
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

def scrape_thisweekinreact():
    # 确保 outputs 文件夹存在
    outputs_dir = "outputs"
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
        print(f"创建输出目录：{outputs_dir}")
        
    url = "https://thisweekinreact.com/newsletter"
    
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
    print(f"Fetching content from: {url}")
    
    # 直接获取网页内容
    result = fetch_page_content(url, headers, proxies)
    
    if result:
        # 提取标题和内容
        title = result["title"]
        chinese_title = result["chinese_title"]
        content = result["content"]
        summary = result["summary"]
        
        # 创建安全的文件名
        safe_title = "thisweekinreact"
        
        # 创建输出文件
        content_file = os.path.join(outputs_dir, f"{safe_title}_content.txt")
        summary_file = os.path.join(outputs_dir, f"{safe_title}_summary.md")
        
        # 保存内容到文件
        with open(content_file, 'w', encoding='utf-8') as f:
            f.write(f"Title: {title}\n")
            f.write(f"Chinese Title: {chinese_title}\n")
            f.write(f"URL: {url}\n\n")
            f.write(content)
        
        # 保存摘要到 Markdown 文件
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"# {chinese_title}\n\n")
            f.write(f"**原标题**: {title}\n\n")
            f.write(f"**链接**: {url}\n\n")
            f.write(f"## 摘要\n\n{summary}\n")
        
        print(f"内容已保存到：{content_file}")
        print(f"摘要已保存到：{summary_file}")
    else:
        print("获取网页内容失败")

if __name__ == "__main__":
    scrape_thisweekinreact() 