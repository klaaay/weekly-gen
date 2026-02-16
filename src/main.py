#!/usr/bin/env python3
"""
Weekly Newsletter Scraper - 主入口文件
一次性执行所有周刊爬取脚本
"""
import os
import sys
import time
import concurrent.futures
import threading
from datetime import datetime
from typing import List, Tuple, Dict, Any

# 导入所有脚本的主函数
try:
    from src.frontendfoc import scrape_frontendfoc
    from src.javascriptweekly import scrape_javascriptweekly
    from src.leadershipintech import scrape_leadershipintech
    from src.nextjsweekly import scrape_nextjsweekly
    from src.nodeweekly import scrape_nodeweekly
    from src.programmingdigest import scrape_programmingdigest
    from src.reactweekly import scrape_reactweekly
    from src.reactdigest import scrape_reactdigest
    from src.thisweekinreact import scrape_thisweekinreact
    from src.webtoolsweekly import scrape_webtoolsweekly
except ImportError as e:
    print(f"导入错误：{e}")
    print("请确保所有脚本文件都在当前目录下")
    sys.exit(1)

# 定义所有可用的脚本
SCRAPERS = {
    'frontendfoc': {
        'name': 'Frontend Focus',
        'function': scrape_frontendfoc,
        'description': 'Frontend 开发相关周刊'
    },
    'javascriptweekly': {
        'name': 'JavaScript Weekly',
        'function': scrape_javascriptweekly,
        'description': 'JavaScript 开发周刊'
    },
    'leadershipintech': {
        'name': 'Leadership in Tech',
        'function': scrape_leadershipintech,
        'description': '技术领导力周刊'
    },
    'nextjsweekly': {
        'name': 'Next.js Weekly',
        'function': scrape_nextjsweekly,
        'description': 'Next.js 框架周刊'
    },
    'nodeweekly': {
        'name': 'Node Weekly',
        'function': scrape_nodeweekly,
        'description': 'Node.js 开发周刊'
    },
    'programmingdigest': {
        'name': 'Programming Digest',
        'function': scrape_programmingdigest,
        'description': '编程技术文摘'
    },
    'reactweekly': {
        'name': 'React Weekly',
        'function': scrape_reactweekly,
        'description': 'React 开发周刊'
    },
    'reactdigest': {
        'name': 'React Digest',
        'function': scrape_reactdigest,
        'description': 'React 技术文摘'
    },
    'thisweekinreact': {
        'name': 'This Week in React',
        'function': scrape_thisweekinreact,
        'description': 'React 生态系统周刊'
    },
    'webtoolsweekly': {
        'name': 'Web Tools Weekly',
        'function': scrape_webtoolsweekly,
        'description': 'Web 开发工具周刊'
    }
}

# 线程安全的打印锁
print_lock = threading.Lock()

def safe_print(message: str):
    """线程安全的打印函数"""
    with print_lock:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")

def run_scraper(scraper_key: str, scraper_info: Dict[str, Any]) -> Tuple[str, bool, str]:
    """
    运行单个爬虫脚本
    
    Args:
        scraper_key: 脚本标识符
        scraper_info: 脚本信息字典
    
    Returns:
        Tuple[脚本名称，是否成功，结果消息]
    """
    scraper_name = scraper_info['name']
    scraper_func = scraper_info['function']
    
    try:
        safe_print(f"开始执行：{scraper_name}")
        start_time = time.time()
        
        # 执行爬虫函数
        scraper_func()
        
        end_time = time.time()
        duration = end_time - start_time
        
        success_msg = f"✅ {scraper_name} 执行成功 (耗时：{duration:.2f}秒)"
        safe_print(success_msg)
        return scraper_key, True, success_msg
        
    except Exception as e:
        error_msg = f"❌ {scraper_name} 执行失败：{str(e)}"
        safe_print(error_msg)
        return scraper_key, False, error_msg

def run_all_scrapers(max_workers: int = 4, selected_scrapers: List[str] = None) -> Dict[str, Any]:
    """
    并行执行所有爬虫脚本
    
    Args:
        max_workers: 最大并发数
        selected_scrapers: 指定要执行的爬虫列表，None 表示执行全部
    
    Returns:
        执行结果统计
    """
    # 确定要执行的爬虫
    if selected_scrapers:
        scrapers_to_run = {k: v for k, v in SCRAPERS.items() if k in selected_scrapers}
    else:
        scrapers_to_run = SCRAPERS
    
    safe_print(f"准备执行 {len(scrapers_to_run)} 个爬虫脚本，最大并发数：{max_workers}")
    safe_print("=" * 60)
    
    results = []
    start_time = time.time()
    
    # 使用线程池并行执行
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        future_to_scraper = {
            executor.submit(run_scraper, key, info): key 
            for key, info in scrapers_to_run.items()
        }
        
        # 收集结果
        for future in concurrent.futures.as_completed(future_to_scraper):
            scraper_key = future_to_scraper[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                error_msg = f"❌ {SCRAPERS[scraper_key]['name']} 执行异常：{str(e)}"
                safe_print(error_msg)
                results.append((scraper_key, False, error_msg))
    
    end_time = time.time()
    total_duration = end_time - start_time
    
    # 统计结果
    successful = sum(1 for _, success, _ in results if success)
    failed = len(results) - successful
    
    safe_print("=" * 60)
    safe_print(f"执行完成！总耗时：{total_duration:.2f}秒")
    safe_print(f"成功：{successful} 个，失败：{failed} 个")
    
    # 显示详细结果
    safe_print("\n📊 详细结果：")
    for scraper_key, success, message in results:
        safe_print(f"  {message}")
    
    return {
        'total': len(results),
        'successful': successful,
        'failed': failed,
        'duration': total_duration,
        'results': results
    }

def show_help():
    """显示帮助信息"""
    print("Weekly Newsletter Scraper - 使用说明")
    print("=" * 50)
    print("用法：python main.py [选项] [脚本名称...]")
    print()
    print("选项：")
    print("  -h, --help          显示此帮助信息")
    print("  -l, --list          列出所有可用的脚本")
    print("  -w, --workers N     设置最大并发数 (默认：4)")
    print("  -a, --all           执行所有脚本 (默认)")
    print()
    print("脚本名称：")
    for key, info in SCRAPERS.items():
        print(f"  {key:<20} {info['description']}")
    print()
    print("示例：")
    print("  python main.py                           # 执行所有脚本")
    print("  python main.py frontendfoc nodeweekly    # 只执行指定脚本")
    print("  python main.py -w 8 --all               # 使用 8 个并发执行所有脚本")

def list_scrapers():
    """列出所有可用的脚本"""
    print("可用的爬虫脚本：")
    print("=" * 50)
    for key, info in SCRAPERS.items():
        print(f"🔹 {key}")
        print(f"   名称：{info['name']}")
        print(f"   描述：{info['description']}")
        print()

def main():
    """主函数"""
    args = sys.argv[1:]
    
    # 解析命令行参数
    max_workers = 4
    selected_scrapers = []
    show_all = False
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg in ['-h', '--help']:
            show_help()
            return
        elif arg in ['-l', '--list']:
            list_scrapers()
            return
        elif arg in ['-w', '--workers']:
            if i + 1 < len(args):
                try:
                    max_workers = int(args[i + 1])
                    i += 1
                except ValueError:
                    print(f"错误：无效的并发数 '{args[i + 1]}'")
                    return
            else:
                print("错误：--workers 需要指定数值")
                return
        elif arg in ['-a', '--all']:
            show_all = True
        elif arg.startswith('-'):
            print(f"错误：未知选项 '{arg}'")
            show_help()
            return
        else:
            # 验证脚本名称是否有效
            if arg in SCRAPERS:
                selected_scrapers.append(arg)
            else:
                print(f"错误：未知脚本 '{arg}'")
                print("使用 -l 查看所有可用脚本")
                return
        
        i += 1
    
    # 如果没有指定脚本且没有使用 --all，默认执行所有脚本
    if not selected_scrapers and not show_all:
        selected_scrapers = None  # 执行所有脚本
    elif show_all:
        selected_scrapers = None  # 执行所有脚本
    
    # 执行爬虫
    try:
        results = run_all_scrapers(max_workers, selected_scrapers)
        
        # 根据结果设置退出码
        if results['failed'] > 0:
            sys.exit(1)  # 有失败的脚本
        else:
            sys.exit(0)  # 全部成功
            
    except KeyboardInterrupt:
        safe_print("\n⚠️ 用户中断执行")
        sys.exit(130)
    except Exception as e:
        safe_print(f"❌ 执行过程中发生异常：{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
