### [Herdr：让编码智能体运行在终端中的运行时](https://github.com/herdrdev/herdr)

**原文标题**: [herdr — the runtime your coding agents live on](https://github.com/herdrdev/herdr)

Herdr 是一个以终端为中心的编码智能体工作区管理器：它保留真实的终端进程与输出，在其上增加工作区、标签页、窗格、会话和 Agent 状态等结构化能力。它并非替代 tmux 或为 Agent 套一层聊天界面，而是将多 Agent 协作中“谁在工作、谁被阻塞、何时完成、如何继续”的运行状态变成可观察、可持久化、可被程序控制的对象。

- 🖥️ **核心定位**：一个 Rust 单二进制终端工作区管理器，不依赖 Electron；每个 pane 都是真实终端，输入与输出直接连到原进程，而非被二次包装或转述。
- 🧭 **清晰的层级模型**：一个 workspace 对应一个仓库、任务或调查；workspace 下可按 `agents`、`logs`、`server`、`review` 等视图划分 tab；tab 内的 pane 可横向或纵向分割并独立运行命令。
- 🤖 **Agent 状态可见化**：Herdr 会从前台进程、screen manifest 或可选集成识别 Agent，并归纳为 `blocked`（需要输入/决策）、`working`、`done`、`idle`、`unknown`。这让人工协调者能优先处理真正卡住的任务，而不是逐个查看终端。
- 🔌 **持久化运行时**：默认是“后台 server + 一个或多个 client”的模型；按 `Ctrl+b q` 仅分离客户端，server、pane 与其中的 Agent 继续运行。再次执行 `herdr` 可重新接入，适合长任务、断线恢复与 SSH 场景。
- ⌨️ **交互方式不受限**：支持 tmux 风格前缀键，也支持鼠标点击、拖拽分割线、右键菜单与文本选择。终端模式将按键传给当前 pane，前缀模式执行一次 Herdr 操作，导航模式提供持续的工作区导航界面。
- 🧩 **自动化是关键差异**：本地 Socket API、CLI 包装和 Agent skill 共用同一控制面。脚本或 Agent 可以创建/重命名 workspace、tab、pane，分屏并运行命令，读取输出，向 pane 发送输入，等待 Agent 到达指定状态，以及订阅事件。
- ⏳ **避免协作竞态**：`agent.wait` 由服务端事件驱动，并固定住被等待的 pane 占用者，避免 pane 被新任务替换后错误地满足等待条件；`agent.prompt` 可将“发送指令 + 等待状态”合并为一个请求，避免两个调用之间的竞态窗口。
- 🧱 **集成分层建议**：常规人工操作或 Shell 编排优先使用 CLI；仅当需要长期事件订阅或直接请求/响应控制时才使用原始 Socket API；若希望 Agent 在 pane 内理解和操作 Herdr，则使用 Agent skill。

#### 最小上手路径

```bash
brew install herdr
herdr
```

在项目目录启动后，为不同工作拆分 pane，例如一个运行开发服务、一个运行测试、一个运行编码 Agent。完成后使用 `Ctrl+b q` 分离；回到任意终端执行 `herdr` 即可重新接入。常用自动化操作示例：

```bash
# 创建一个指向当前项目的工作区
herdr workspace create --cwd "$PWD" --label weekly-gen

# 分出测试窗格并运行测试
herdr pane split w1:p1 --direction right
herdr pane run w1:p2 "uv run pytest"

# 等待某个 Agent 完成，再读取其最近输出
herdr agent wait w1:p1 --until done
herdr pane read w1:p1 --source recent --lines 50
```

#### 学习要点与实践启发

- 多 Agent 系统的价值不只在“并行启动更多 Agent”，更在于为进程建立可查询的状态、生命周期和同步机制；否则协调成本会迅速吞噬并行收益。
- 把运行态所有权放在后台 server，而非客户端 UI 中，能自然支持 detach、重连、远程访问和会话恢复；这是终端工具能承担“runtime”角色的基础。
- 对自动化而言，应优先选稳定的 CLI 高层接口，只有确有定制协议或事件流需求时才下沉到 Socket API，以控制耦合和维护成本。
- 在本仓库的周报生成任务中，可将“抓取/摘要”“测试”“调度日志”拆成独立 pane，并用 `agent wait` 或 pane 输出读取来串联检查，减少在多个终端之间手工切换与漏看失败信息的风险。

**来源**：[GitHub README（简体中文）](https://github.com/herdrdev/herdr/blob/master/README.zh-CN.md) · [核心概念文档](https://herdr.dev/docs/concepts/) · [Socket API 文档](https://herdr.dev/docs/socket-api/)

---
