#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse, urljoin
from openai import OpenAI
from dotenv import load_dotenv
from utils.deepseek_api import translate_title_to_chinese, summarize_with_deepseek
from utils.extract_links_and_summarize import extract_links_and_summarize

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
    
    try:
        # 获取主页内容
        response = requests.get(url, headers=headers, proxies=proxies, allow_redirects=True)
        
        if response.status_code == 200:
            # 解析 HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 创建安全的文件名
            safe_title = "thisweekinreact"
                
            # 创建主页输出文件
            summary_file = os.path.join(outputs_dir, f"{safe_title}_summary.md")
            
            print(f"主页摘要已保存到：{summary_file}")
            
            # 1. 查找第一个以 /newsletter/数字 格式的链接
            newsletter_link = soup.find('a', href=re.compile(r'^/newsletter/\d+$'))
            
            if newsletter_link and 'href' in newsletter_link.attrs:
                newsletter_url = newsletter_link['href']
                
                # 确保链接是绝对路径
                if not newsletter_url.startswith('http'):
                    newsletter_url = f"https://thisweekinreact.com{newsletter_url}"
                
                print(f"\n找到 newsletter 链接：{newsletter_url}")
                print(f"获取 newsletter 页面内容...")
                
                # 2. 获取这个 newsletter 页面的内容
                newsletter_response = requests.get(newsletter_url, headers=headers, proxies=proxies, allow_redirects=True)
                
                if newsletter_response.status_code == 200:
                    # 解析 newsletter 页面
                    newsletter_soup = BeautifulSoup(newsletter_response.text, 'html.parser')
                    
                    print("\n开始提取文章链接并生成摘要...")
                    
                    # 3. 从 newsletter 页面找到所有没有 class 属性且 target="_blank" 的链接
                    filtered_links = newsletter_soup.select('a:not([class])[target="_blank"]')
                    print(f"\n在 newsletter 页面找到 {len(filtered_links)} 个符合条件的链接")
                    
                    # 4. 使用预先筛选好的链接集合
                    extract_links_and_summarize(
                        soup=newsletter_soup,  # 传递 newsletter 页面的 soup 对象
                        headers=headers,
                        proxies=proxies,
                        summary_file=summary_file,
                        summary_title_prefix="thisweekinreact",
                        base_url="https://thisweekinreact.com",
                        fetch_content_func=fetch_page_content,
                        use_patterns=False,  # 不使用模式匹配
                        pre_filtered_links=filtered_links  # 使用预先筛选好的链接
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