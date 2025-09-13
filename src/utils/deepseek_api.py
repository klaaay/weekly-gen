#!/usr/bin/env python3
# Moved to src/utils (package layout)
import os
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
        prompt = f"Please translate the following title to Chinese (simplified). Only return the translated title, no explanations: {title}"
        
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
