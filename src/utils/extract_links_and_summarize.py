#!/usr/bin/env python3
# Moved to src/utils (package layout)
import requests
from bs4 import BeautifulSoup
import re
import os
from typing import List, Dict, Any, Optional, Tuple, Pattern
from datetime import datetime

def extract_links_and_summarize(
    soup: BeautifulSoup, 
    link_patterns: List[Pattern] = None, 
    headers: Dict[str, str] = None, 
    proxies: Dict[str, str] = None, 
    summary_file: str = None,
    summary_title_prefix: str = "",
    base_url: str = None,
    fetch_content_func = None,
    use_patterns: bool = True,  # 控制是否使用模式匹配
    pre_filtered_links = None   # 新增参数：预先筛选好的链接
) -> List[Dict[str, Any]]:
    """
    从 BeautifulSoup 对象中提取符合指定模式的链接，获取这些链接的内容并生成总结
    
    参数：
        soup: BeautifulSoup 对象，包含要处理的 HTML 内容
        link_patterns: 正则表达式模式列表，用于匹配链接（当 use_patterns=True 时使用）
        headers: HTTP 请求头
        proxies: 代理设置
        summary_file: 可选，保存总结的文件路径
        summary_title_prefix: 可选，摘要文件标题前缀
        base_url: 可选，用于将相对 URL 转换为绝对 URL 的基础 URL
        fetch_content_func: 可选，获取内容的函数，如果为 None 则使用内部默认函数
        use_patterns: 是否使用 link_patterns 模式匹配，如果为 False 则获取 body 下所有链接
        pre_filtered_links: 可选，预先筛选好的链接列表，如果提供则直接使用而不再从 soup 中搜索
        
    返回：
        已处理的文章数据列表
    """
    
    # 确保 outputs 文件夹存在
    outputs_dir = "outputs"
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
        print(f"创建输出目录：{outputs_dir}")
    
    # 如果提供了 summary_file，添加日期前缀和输出目录
    if summary_file:
        # 清理文件名，确保没有换行符和其他不适合用作文件名的字符
        summary_file = summary_file.replace('\n', '').replace('\r', '')
        
        # 获取当前日期并格式化为 YYYY-MM-DD
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # 检查 summary_file 是否已经包含 outputs 路径，避免重复
        if summary_file.startswith('outputs/'):
            # 如果已经包含 outputs 路径，只需添加日期和前缀
            base_name = os.path.basename(summary_file)
            summary_file = os.path.join(outputs_dir, f"{current_date}_{summary_title_prefix}_{base_name}")
        else:
            # 添加日期和前缀到文件名，并放入 outputs 文件夹
            summary_file = os.path.join(outputs_dir, f"{current_date}_{summary_title_prefix}_{summary_file}")
        
        print(f"总结将保存到文件：{summary_file}")
    
    # 存储处理过的文章数据
    processed_articles_data = []
    
    # 优先使用预先筛选好的链接
    if pre_filtered_links:
        matched_links = pre_filtered_links
        print(f"\n使用预先筛选好的 {len(matched_links)} 个链接：")
    # 如果没有预先筛选的链接，则根据 use_patterns 参数决定如何获取链接
    elif use_patterns and link_patterns:
        # 使用模式匹配方式获取链接
        matched_links = []
        for pattern in link_patterns:
            links = soup.find_all('a', href=pattern)
            if links:
                matched_links = links
                print(f"\n找到 {len(links)} 个符合模式 {pattern.pattern} 的链接：")
                break
    else:
        # 直接获取 body 下所有具有 href 属性的链接
        if soup.body:
            matched_links = soup.body.find_all('a', href=True)
            print(f"\n在 body 下找到 {len(matched_links)} 个链接：")
        else:
            matched_links = soup.find_all('a', href=True)
            print(f"\n找到 {len(matched_links)} 个链接：")
    
    if matched_links:
        # 记录成功获取的文章数
        processed_articles = 0
        
        for link in matched_links:
            if 'href' in link.attrs:
                link_text = link.text.strip()
                link_url = link['href']
                
                # 跳过空文本的链接
                if not link_text:
                    continue
                    
                # 避免重复处理相同的链接
                if processed_articles > 0 and link_url in [l['href'] for l in matched_links[:processed_articles]]:
                    continue
                
                # 确保 URL 是绝对路径
                if base_url and not link_url.startswith('http'):
                    link_url = f"{base_url}{link_url}"
                    
                print(f"链接文本：{link_text}")
                print(f"链接 URL: {link_url}")
                print("获取此链接的内容...")
                
                # 获取链接内容
                if fetch_content_func:
                    article_data = fetch_content_func(link_url, headers, proxies)
                else:
                    # 如果没有提供内容获取函数，则跳过内容获取
                    article_data = {
                        "url": link_url,
                        "title": link_text,
                        "chinese_title": link_text,
                        "summary": "未提供内容获取函数"
                    }
                
                # 保存处理过的文章数据
                processed_articles_data.append(article_data)
                
                # 如果提供了 summary_file，则写入总结
                if summary_file:
                    # 构建文章总结
                    article_summary = f"### [{article_data['chinese_title']}]({article_data['url']})\n\n"
                    article_summary += f"**原文标题**: [{article_data['title']}]({article_data['url']})\n\n"
                    article_summary += f"{article_data['summary']}\n\n"
                    article_summary += f"---\n\n"  # 使用 Markdown 分隔符
                    
                    # 写入到文件
                    with open(summary_file, 'a', encoding='utf-8') as summary_f:
                        summary_f.write(article_summary)
                
                processed_articles += 1
                print(f"文章 {processed_articles} 已写入总结文件")
                print("---")
        
        if summary_file:
            print(f"\n所有 {processed_articles} 篇文章总结已保存到 {summary_file}")
    else:
        print("\n没有找到符合指定模式的链接。")
    
    return processed_articles_data

# 使用示例：
"""
# 使用方法：
from extract_links_and_summarize import extract_links_and_summarize
from bs4 import BeautifulSoup
import re
import requests

# 设置请求头和代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
proxies = {
    'http': 'http://127.0.0.1:7897',
    'https': 'http://127.0.0.1:7897'
}

# 获取页面内容
response = requests.get("https://nodeweekly.com/issues/123", headers=headers, proxies=proxies)
soup = BeautifulSoup(response.text, 'html.parser')

# 定义链接匹配模式
link_patterns = [
    re.compile(r'^https://nodeweekly\.com/link'),  # 绝对 URL 模式
    re.compile(r'^/link')                          # 相对 URL 模式
]

# 从页面中提取链接并生成总结
articles = extract_links_and_summarize(
    soup=soup,
    link_patterns=link_patterns,
    headers=headers,
    proxies=proxies,
    summary_file="nodeweekly_summary.md",
    summary_title_prefix="nodeweekly",
    base_url="https://nodeweekly.com",
    fetch_content_func=fetch_page_content  # 需要提供获取内容的函数
)
""" 
