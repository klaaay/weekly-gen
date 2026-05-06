#!/usr/bin/env python3
# Moved to src/utils (package layout)
"""
上次运行信息跟踪器
用于记录和检查各个脚本的上次运行信息，避免重复处理相同的内容
"""
import os
import json
import contextlib
import datetime
import shutil
import tempfile
import threading

# 用于 last_run_info.json 读写锁，避免并行执行时竞态导致 key 丢失
_file_lock = threading.Lock()
_DEFAULT_JSON_FILE_PATH = "last_run_info.json"
_LAST_RUN_INFO_PATH_ENV = "LAST_RUN_INFO_PATH"


def _resolve_json_file_path(json_file_path=_DEFAULT_JSON_FILE_PATH):
    """解析状态文件路径，默认允许通过环境变量覆盖。"""
    if json_file_path == _DEFAULT_JSON_FILE_PATH:
        return os.getenv(_LAST_RUN_INFO_PATH_ENV) or json_file_path
    return json_file_path


def _candidate_read_paths(json_file_path):
    """返回读取状态时的候选路径，支持从旧默认路径迁移到新路径。"""
    resolved_path = _resolve_json_file_path(json_file_path)
    paths = [resolved_path, f"{resolved_path}.bak"]
    if resolved_path != _DEFAULT_JSON_FILE_PATH:
        paths.extend([_DEFAULT_JSON_FILE_PATH, f"{_DEFAULT_JSON_FILE_PATH}.bak"])
    return paths


def _load_json_file(path):
    """读取并校验状态 JSON，文件不存在或损坏时返回 None。"""
    if not os.path.exists(path):
        return None

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"读取上次运行信息失败：{path}: {e}")
        return None

    if not isinstance(data, dict):
        print(f"读取上次运行信息失败：{path}: 内容不是 JSON 对象")
        return None
    return data


def _sync_parent_dir(path):
    """尽量同步父目录元数据；部分平台不支持时忽略。"""
    parent_dir = os.path.dirname(path) or "."
    try:
        dir_fd = os.open(parent_dir, os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except Exception:
        pass


def _write_json_atomic(path, data):
    """原子写入 JSON，避免进程中断留下半个状态文件。"""
    parent_dir = os.path.dirname(path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    else:
        parent_dir = "."

    fd, temp_path = tempfile.mkstemp(
        prefix=f".{os.path.basename(path)}.",
        suffix=".tmp",
        dir=parent_dir,
        text=True,
    )
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp_path, path)
        _sync_parent_dir(path)
    except Exception:
        with contextlib.suppress(Exception):
            os.unlink(temp_path)
        raise


def _backup_current_file(path):
    """写入新状态前保存当前有效状态。"""
    data = _load_json_file(path)
    if data is None:
        return
    backup_path = f"{path}.bak"
    parent_dir = os.path.dirname(backup_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    shutil.copy2(path, backup_path)


def _maybe_migrate_last_run_info(target_path, source_path, data):
    """从旧位置或备份读到状态后，补写到目标位置完成自愈。"""
    if source_path == target_path:
        return
    if _load_json_file(target_path) is not None:
        return
    try:
        _write_json_atomic(target_path, data)
        print(f"已迁移上次运行信息：{source_path} -> {target_path}")
    except Exception as e:
        print(f"迁移上次运行信息失败：{e}")


def _load_last_run_info_unsafe(json_file_path=_DEFAULT_JSON_FILE_PATH):
    """内部使用：无锁读取 JSON（调用方需持有 _file_lock）"""
    resolved_path = _resolve_json_file_path(json_file_path)
    for candidate_path in _candidate_read_paths(json_file_path):
        data = _load_json_file(candidate_path)
        if data is not None:
            _maybe_migrate_last_run_info(resolved_path, candidate_path, data)
            return data
    return {}


def load_last_run_info(json_file_path=_DEFAULT_JSON_FILE_PATH):
    """加载上次运行信息的 JSON 文件（线程安全）"""
    with _file_lock:
        return _load_last_run_info_unsafe(json_file_path)

def update_last_run_info(script_name, issue_link_info, json_file_path=_DEFAULT_JSON_FILE_PATH):
    """更新上次运行信息到 JSON 文件（线程安全，避免并行执行时竞态导致其他 key 丢失）"""
    try:
        resolved_path = _resolve_json_file_path(json_file_path)
        with _file_lock:
            # 加载现有数据（已持有锁，用无锁版本避免死锁）
            data = _load_last_run_info_unsafe(resolved_path)
            
            # 更新当前脚本的信息
            data[script_name] = issue_link_info
            
            # 保存到文件：写前备份，随后原子替换，避免状态文件损坏导致下次全量抓取
            _backup_current_file(resolved_path)
            _write_json_atomic(resolved_path, data)
        
        print(f"已更新 {script_name} 的运行信息到 {resolved_path}")
        
    except Exception as e:
        print(f"保存运行信息失败：{e}")

def _normalize_url_for_comparison(url):
    """规范化 URL 用于比较：去除尾部斜杠，有和没有都视为同一链接"""
    if not url:
        return url or ""
    return url.rstrip("/")


def check_and_skip_if_same_issue(script_name, link_url, base_url, json_file_path=_DEFAULT_JSON_FILE_PATH):
    """
    检查当前 full_url 是否与上次运行相同（忽略尾部斜杠差异）
    
    Args:
        script_name: 脚本名称
        link_url: 当前的 issue href（相对或绝对）
        base_url: 基础 URL，用于构建 full_url
        json_file_path: JSON 文件路径
    
    Returns:
        bool: True 表示应该跳过（相同），False 表示应该继续执行（不同或首次运行）
    """
    try:
        last_run_data = load_last_run_info(json_file_path)
        
        # 构建当前 full_url，与 create_issue_info 逻辑一致
        current_full_url = (
            link_url if link_url.startswith("http") else f"{base_url}/{link_url}"
        )
        current_normalized = _normalize_url_for_comparison(current_full_url)
        
        # 如果存在上次运行的数据，比较规范化的 full_url
        if script_name in last_run_data:
            last_full_url = last_run_data[script_name].get("full_url") or ""
            last_normalized = _normalize_url_for_comparison(last_full_url)
            if current_normalized == last_normalized:
                print(f"检测到相同的 full_url: {current_full_url}，跳过执行")
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
