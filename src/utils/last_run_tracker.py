#!/usr/bin/env python3
# Moved to src/utils (package layout)
"""
上次运行信息跟踪器
用于记录和检查各个脚本的上次运行信息，避免重复处理相同的内容
"""
import os
import json
import datetime

def load_last_run_info(json_file_path="last_run_info.json"):
    """加载上次运行信息的 JSON 文件"""
    try:
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return {}
    except Exception as e:
        print(f"读取上次运行信息失败：{e}")
        return {}

def update_last_run_info(script_name, issue_link_info, json_file_path="last_run_info.json"):
    """更新上次运行信息到 JSON 文件"""
    try:
        # 加载现有数据
        data = load_last_run_info(json_file_path)
        
        # 更新当前脚本的信息
        data[script_name] = issue_link_info
        
        # 保存到文件
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"已更新 {script_name} 的运行信息到 {json_file_path}")
        
    except Exception as e:
        print(f"保存运行信息失败：{e}")

def check_and_skip_if_same_issue(script_name, link_url, json_file_path="last_run_info.json"):
    """
    检查当前 link_url 是否与上次运行相同
    
    Args:
        script_name: 脚本名称
        link_url: 当前的 issue href
        json_file_path: JSON 文件路径
    
    Returns:
        bool: True 表示应该跳过（相同），False 表示应该继续执行（不同或首次运行）
    """
    try:
        last_run_data = load_last_run_info(json_file_path)
        
        # 如果存在上次运行的数据且 link_url 相同，则返回 True（跳过）
        if script_name in last_run_data and last_run_data[script_name].get("link_url") == link_url:
            print(f"检测到相同的 link_url: {link_url}，跳过执行")
            return True
        
        # 不同或首次运行，返回 False（继续执行）
        return False
        
    except Exception as e:
        print(f"检查上次运行信息时出错：{e}")
        return False  # 出错时继续执行，避免阻塞

def create_issue_info(issue_title, link_url, base_url):
    """
    创建标准的 issue 信息字典
    
    Args:
        issue_title: issue 标题
        link_url: 链接 URL
        base_url: 基础 URL（用于构建完整 URL）
    
    Returns:
        dict: 包含完整 issue 信息的字典
    """
    return {
        "issue_title": issue_title,
        "link_url": link_url,
        "timestamp": datetime.datetime.now().isoformat(),
        "full_url": f"{base_url}/{link_url}" if not link_url.startswith('http') else link_url
    }
