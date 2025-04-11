#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse
from openai import OpenAI
from dotenv import load_dotenv

# 加载.env 文件中的环境变量
load_dotenv()

# 初始化 OpenAI 客户端，指向 DeepSeek API
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=os.getenv("DEEPSEEK_BASE_URL"))

def translate_title_to_chinese(title):
    """使用 DeepSeek API 将标题翻译为中文"""
    try:
        # 构建翻译提示词
        prompt = f"Please translate the following title to Chinese (simplified). Only return the translated title, no explanations: \"{title}\""
        
        # 调用 API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that translates English to Chinese."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=200
        )
        
        # 返回翻译内容
        translated_title = response.choices[0].message.content.strip()
        print(f"  Translated title: {translated_title}")
        return translated_title
    except Exception as e:
        print(f"  Translation failed: {str(e)}")
        return title  # 如果翻译失败，返回原标题

def summarize_with_deepseek(content):
    """使用 DeepSeek API 总结文章内容"""
    try:
        # 构建提示词
        prompt = f"""Your output should use the following template:

overview summary
- Emoji Bulletpoint

Please summarize the text I provide by creating a concise list of bullet points. Ensure that the bullet points are formatted using the "-" symbol. Include key points and essential information to capture the essence of the article effectively. Pick a suitable emoji for every bullet point. Add an overview summary without summary title of the article at the top.Your response should be in ZH. Use the following content: {content}"""
        
        # 调用 API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes content."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=8000
        )
        
        # 返回总结内容
        return response.choices[0].message.content
    except Exception as e:
        return f"总结失败：{str(e)}"

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

def scrape_nodeweekly():
    url = "https://nodeweekly.com/issues"
    
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
        title = soup.find('h1')
        if title:
            site_title = title.text.strip()
            print(f"Title: {site_title}\n")
            # Sanitize title for filename
            safe_title = re.sub(r'[^\w\s-]', '', site_title).strip().replace(' ', '_')
        else:
            site_title = "Node Weekly"
            safe_title = "nodeweekly"
        
        # Create output files with title in the filename
        content_file = f"{safe_title}_content.txt"
        summary_file = f"{safe_title}_summary.md"  # Markdown 格式
        
        # Find the first issue link - looking for links with href="issues/*" and text containing "Issue #"
        issue_link = soup.find('a', href=re.compile(r'^issues/\d+$'), string=re.compile(r'Issue #\d+'))
        
        if issue_link and 'href' in issue_link.attrs:
            link_url = issue_link['href']
            issue_title = issue_link.text
            print(f"Found issue link: {issue_link.text} - {link_url}")
            
            # Sanitize issue title for filename
            safe_issue_title = re.sub(r'[^\w\s-]', '', issue_title).strip().replace(' ', '_')
            
            # Create output file with site title and issue title in the filename
            summary_file = f"{safe_title}_{safe_issue_title}_summary.md"  # Markdown 格式
            
            # If the URL is relative, make it absolute
            if not link_url.startswith('http'):
                link_url = f"https://nodeweekly.com/{link_url}"
            
            # Send GET request to the linked page
            print(f"Fetching content from: {link_url}")
            link_response = requests.get(link_url, headers=headers, proxies=proxies)
            
            # Check if the request was successful
            if link_response.status_code == 200:
                # Save issue title and URL to content collection
                
                # 以追加模式打开文件
                with open(summary_file, 'a', encoding='utf-8') as summary_f:
                    # 写入网站标题、期刊标题和 URL
                    summary_f.write(f"# {site_title} - {issue_title} 文章总结\n\n")
                
                # Parse the HTML content of the linked page
                link_soup = BeautifulSoup(link_response.text, 'html.parser')
                
                # Find all <a> tags with href starting with "https://nodeweekly.com/link"
                nodeweekly_links = link_soup.find_all('a', href=re.compile(r'^https://nodeweekly\.com/link'))
                
                # If no https links found, try relative links
                if not nodeweekly_links:
                    # Find links that start with "/link"
                    nodeweekly_links = link_soup.find_all('a', href=re.compile(r'^/link'))
                
                if nodeweekly_links:
                    print(f"\nFound {len(nodeweekly_links)} links with nodeweekly.com/link pattern:")
                    
                    # 记录成功获取的文章数
                    processed_articles = 0
                    
                    for link in nodeweekly_links:
                        if 'href' in link.attrs:
                            link_text = link.text.strip()
                            link_url = link['href']
                            
                            # 跳过空文本的链接
                            if not link_text:
                                continue
                                
                            # 避免重复处理相同的链接
                            if processed_articles > 0 and link_url in [l['href'] for l in nodeweekly_links[:processed_articles]]:
                                continue
                            
                            # Make sure URL is absolute
                            if link_url.startswith('/'):
                                link_url = f"https://nodeweekly.com{link_url}"
                                
                            print(f"Link text: {link_text}")
                            print(f"Link URL: {link_url}")
                            print("Fetching content from this link...")
                            
                            # Fetch content from the linked URL
                            article_data = fetch_page_content(link_url, headers, proxies)
                            
                            # 构建文章总结
                            article_summary = f"## [{link_text}]({article_data['url']})\n\n"
                            article_summary += f"**原文标题**: [{article_data['title']}]({article_data['url']})\n\n"
                            article_summary += f"**中文标题**: {article_data['chinese_title']}\n\n"
                            article_summary += f"{article_data['summary']}\n\n"
                            article_summary += f"---\n\n"  # 使用 Markdown 分隔符
                            
                            # 写入到文件
                            with open(summary_file, 'a', encoding='utf-8') as summary_f:
                                summary_f.write(article_summary)
                            
                            processed_articles += 1
                            print(f"Article {processed_articles} has been written to the summary file")
                            print("---")
                    
                    print(f"\nAll {processed_articles} article summaries have been saved to {summary_file}")
                else:
                    print("\nNo links with nodeweekly.com/link pattern found on the page.")
            else:
                print(f"Failed to retrieve the linked page. Status code: {link_response.status_code}")
        else:
            print("No issue links matching the pattern found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_nodeweekly() 