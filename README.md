# Weekly Newsletter Scraper

一个用于抓取各种技术周刊的 Python 工具集合。

## 功能特性

- 🚀 **智能去重**: 自动检测重复内容，避免重复处理
- 📊 **并行执行**: 支持多线程并行抓取，提高效率
- 🔄 **状态跟踪**: 记录每次运行的状态，支持断点续传
- 📝 **内容总结**: 使用 AI 自动生成中文摘要
- 🎯 **精准抓取**: 支持 8 个主流技术周刊

## 支持的周刊

| 脚本名称              | 周刊名称           | 描述                  |
| --------------------- | ------------------ | --------------------- |
| `frontendfoc.py`      | Frontend Focus     | Frontend 开发相关周刊 |
| `javascriptweekly.py` | JavaScript Weekly  | JavaScript 开发周刊   |
| `nextjsweekly.py`     | Next.js Weekly     | Next.js 框架周刊      |
| `nodeweekly.py`       | Node Weekly        | Node.js 开发周刊      |
| `reactweekly.py`      | React Weekly       | React 开发周刊        |
| `reactdigest.py`      | React Digest       | React 技术文摘        |
| `thisweekinreact.py`  | This Week in React | React 生态系统周刊    |
| `webtoolsweekly.py`   | Web Tools Weekly   | Web 开发工具周刊      |

## 安装依赖

```bash
pip install requests beautifulsoup4 openai python-dotenv
```

## 环境配置

创建 `.env` 文件并配置以下环境变量：

```env
# DeepSeek API 配置
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

## 使用方法

### 1. 使用主入口文件 (推荐)

```bash
# 执行所有脚本
python main.py

# 显示帮助信息
python main.py --help

# 列出所有可用脚本
python main.py --list

# 只执行指定脚本
python main.py frontendfoc nodeweekly

# 设置并发数 (默认4)
python main.py --workers 8

# 使用8个并发执行所有脚本
python main.py -w 8 --all
```


### 2. 单独执行脚本

```bash
# 执行单个脚本
python frontendfoc.py
python javascriptweekly.py
# ... 其他脚本
```

## 输出文件

- 所有生成的文件保存在 `outputs/` 目录下
- 文件格式为 Markdown (`.md`)
- 文件名格式：`{脚本名}_{期刊标题}_summary.md`
- 运行状态记录在 `last_run_info.json` 文件中

## 智能去重机制

系统会自动记录每次运行抓取的链接 URL，如果检测到相同的链接，会自动跳过执行：

```json
{
  "frontendfoc": {
    "issue_title": "Issue #123",
    "link_url": "issues/123",
    "timestamp": "2025-09-11T10:30:00.123456",
    "full_url": "https://frontendfoc.us/issues/123"
  }
}
```

## 命令行选项

### main.py 选项

| 选项              | 说明                     |
| ----------------- | ------------------------ |
| `-h, --help`      | 显示帮助信息             |
| `-l, --list`      | 列出所有可用脚本         |
| `-w, --workers N` | 设置最大并发数 (默认：4) |
| `-a, --all`       | 执行所有脚本 (默认行为)  |

## 项目结构

```
weekly-gen/
├── main.py                 # 主入口文件 (并行执行)
├── run_all.py             # 简化版批量执行器 (顺序执行)
├── frontendfoc.py         # Frontend Focus 爬虫
├── javascriptweekly.py    # JavaScript Weekly 爬虫
├── nextjsweekly.py        # Next.js Weekly 爬虫
├── nodeweekly.py          # Node Weekly 爬虫
├── reactweekly.py         # React Weekly 爬虫
├── reactdigest.py         # React Digest 爬虫
├── thisweekinreact.py     # This Week in React 爬虫
├── webtoolsweekly.py      # Web Tools Weekly 爬虫
├── utils/
│   ├── last_run_tracker.py    # 运行状态跟踪器
│   ├── deepseek_api.py        # DeepSeek API 接口
│   └── extract_links_and_summarize.py  # 链接提取和总结
├── outputs/               # 输出文件目录
├── last_run_info.json    # 运行状态记录
└── README.md             # 说明文档
```

## 使用示例

### 快速开始

1. 安装依赖并配置环境变量
2. 执行所有脚本：
   ```bash
   python main.py
   ```

### 高级用法

```bash
# 只抓取React相关的周刊
python main.py reactweekly reactdigest thisweekinreact

# 使用更高并发数加速执行
python main.py --workers 8

# 查看执行状态
cat last_run_info.json
```

## 注意事项

1. **网络代理**: 脚本默认使用 `127.0.0.1:7897` 代理，请根据需要修改
2. **API 限制**: 注意 DeepSeek API 的调用频率限制
3. **超时设置**: 单个脚本执行超时时间为 5 分钟
4. **错误处理**: 系统具有完善的错误处理和重试机制

## 故障排除

### 常见问题

1. **导入错误**: 确保所有依赖都已安装
2. **API 错误**: 检查`.env`文件中的 API 配置
3. **网络错误**: 检查代理设置和网络连接
4. **权限错误**: 确保有写入`outputs/`目录的权限

### 日志查看

所有执行日志都会实时显示在终端，包括：
- 执行开始时间
- 成功/失败状态
- 执行耗时
- 错误详情

## 服务化与部署（FastAPI + uv + Docker）

- 服务：基于 FastAPI，启动后会在后台每 5 分钟尝试执行 `python main.py -w 8 --all`（避免并发重叠）。
- 依赖管理：通过 `uv` 按 `pyproject.toml` 同步安装。
- 日志：运行日志保存至 `outputs/service_logs/`，最近一次运行日志路径会在 `/status` 返回。

### 本地运行（uv）

```bash
# 同步依赖
uv sync

# 启动服务（默认 8000 端口）
uv run uvicorn app.server:app --host 0.0.0.0 --port 8000

# 环境变量可配置间隔（默认 300 秒）
TASK_INTERVAL_SECONDS=600 uv run uvicorn app.server:app --host 0.0.0.0 --port 8000
```

接口：
- `GET /healthz`：健康检查
- `GET /status`：查看后台任务状态
- `POST /run-now`：立即触发一次执行（若正在运行会返回 409）

### Docker 运行

```bash
docker build -t weekly-gen:latest .
docker run --rm -p 8000:8000 \
  -e TASK_INTERVAL_SECONDS=300 \
  -v "$(pwd)/outputs:/app/outputs" \
  -v "$(pwd)/last_run_info.json:/app/last_run_info.json" \
  --name weekly-gen weekly-gen:latest
```

### 打镜像（构建与推送）

使用 Compose（支持自定义镜像名与标签）：

```bash
# 构建
IMAGE_NAME=yourrepo/weekly-gen IMAGE_TAG=$(git rev-parse --short HEAD) docker compose build

# 推送（需先登录到对应 Registry）
IMAGE_NAME=yourrepo/weekly-gen IMAGE_TAG=$(git rev-parse --short HEAD) docker compose push
```

或使用 Makefile（简化命令）：

```bash
# 构建
make build IMAGE_NAME=yourrepo/weekly-gen IMAGE_TAG=$(git rev-parse --short HEAD)

# 推送
make push IMAGE_NAME=yourrepo/weekly-gen IMAGE_TAG=$(git rev-parse --short HEAD)
```

### docker-compose 部署

项目已提供 `docker-compose.yml`，默认将容器内的 `/app/outputs` 映射到宿主机 `./outputs`。

```bash
docker compose up -d --build
```

> 说明：项目中实际使用的目录为 `outputs/`（复数）。如需与文档中 `output/`（单数）保持一致，请调整 compose 映射或脚本中的输出目录。

### 代理注意事项（容器）

脚本中默认代理为 `127.0.0.1:7897`，在容器内这通常不可用。若需复用宿主机代理：
- macOS/Windows（Docker Desktop）：可将代理地址改为 `http://host.docker.internal:7897`
- Linux：请在宿主与容器网络间配置可达地址，或在容器内运行代理

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 许可证

MIT License
