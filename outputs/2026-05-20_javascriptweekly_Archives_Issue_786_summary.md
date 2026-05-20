### [JavaScript 周刊第 786 期：2026 年 5 月 19 日](https://javascriptweekly.com/issues/786)

**原文标题**: [JavaScript Weekly Issue 786: May 19, 2026](https://javascriptweekly.com/issues/786)

本週 JavaScript Weekly 重點涵蓋了 npm 安全漏洞、新工具與框架發布，以及生態系統中的重要討論。

- 🔒 npm 提議將安裝腳本改為「選擇加入」，以減少安全風險，並有工具如 `npq` 可協助審計套件。
- 🛠️ Depot 分享如何在 AWS Lambda 上建構長時間運行的 CI 協調器，使用無伺服器架構實現狀態管理與錯誤恢復。
- 🚨 超過 300 個惡意 npm 套件（包括 antv 和 timeago.js）被發現，屬於 Shai-Hulud 攻擊系列。
- 📰 知名 JavaScript 作者 Dr. Axel Rauschmayer 因 AI 爬蟲問題下架部落格與書籍；Bun 的 Rust 重寫合併引發程式碼品質討論；Deno 2.8 即將發布，帶來 Node.js 相容性與 TypeScript 6.0.3 支援。
- 🎉 Angular 22 RC 發布，預計六月推出正式版，將引入基於信號的表單與預設 OnPush 變更偵測。
- 🤖 Mark Erikson 分享其開發工作流程，包括使用 OpenCode 程式碼代理與知識庫管理工具。
- 📗 NodeBook 提供深入 Node.js 內部機制的進階指南，涵蓋事件循環、V8、串流等主題。
- 🛡️ TanStack 在 npm 被入侵後加強供應鏈安全措施，並有長篇訪談討論其與 Next.js 的競爭。
- 🛠️ 多項工具更新：Orval 生成型別安全客戶端、Brownies 簡化瀏覽器儲存、Pica 10.0 圖片縮放、SVAR Calendar 日曆元件、Fate 1.0 React 資料框架等。
- 📢 生態系統亮點：JSONRegistry 提案、Wasp 框架創辦人分享五年開發歷程、瀏覽器針對特定網站的內建調整、以及 LLM 近六個月發展回顧。

---

### [[RFC] 使安装脚本成为可选加入 由 JamieMagee 提交 · 拉取请求 #868 · npm/rfcs · GitHub](https://github.com/npm/rfcs/pull/868)

**原文标题**: [[RFC] Make install scripts opt-in by JamieMagee · Pull Request #868 · npm/rfcs · GitHub](https://github.com/npm/rfcs/pull/868)

该 RFC 提议将 npm 的安装脚本（preinstall、install、postinstall 及 node-gyp 构建）默认设为可选，以增强安全性。项目需通过`package.json`中的新`allowScripts`字段明确授权特定依赖运行脚本，并新增`npm approve-scripts`和`npm deny-scripts`两个 CLI 命令来管理授权列表。

- 🔒 **默认阻止安装脚本**：npm 将成为继 pnpm、Yarn Berry、Bun 和 Deno 之后，最后一个默认阻止依赖安装脚本的主流包管理器，以防范供应链攻击。
- 🚨 **近期攻击事件驱动**：包括 Shai-Hulud 蠕虫、chalk/debug 等 17 个包被注入 Web3 钱包盗取代码，以及 Axios 包通过 postinstall 部署跨平台 RAT 等事件，凸显了安装脚本的即时执行风险。
- 📝 **新增 allowScripts 字段**：项目可在`package.json`中通过`"allowScripts": { "包名@版本": true }`的形式，精确授权特定依赖运行脚本，支持版本锁定。
- 🛠️ **新增 CLI 命令**：`npm approve-scripts`用于批准脚本运行，`npm deny-scripts`用于拒绝，支持按包名、版本锁定、全部批准/拒绝及只读查看待处理项。
- 🗺️ **分阶段实施**：第一阶段仅发出警告，不阻止脚本运行；第二阶段将真正阻止未经授权的脚本执行。
- 💬 **社区争议**：有观点认为将授权列表放在`package.json`中会公开安全策略，帮助攻击者缩小目标范围；但支持者指出，攻击者已可从公开的依赖信息推断出哪些包需要运行脚本，且授权列表也可通过`.npmrc`或 CLI 参数私有化。
- 🧩 **保留合法用例**：对于`canvas`、`sharp`、`sqlite3`等仍需安装脚本的原生模块，该机制提供了明确的授权路径，而非一刀切的`--ignore-scripts`。

---

### [GitHub - lirantal/npq: 在安装前审计 npm 包以确保安全安装](https://github.com/lirantal/npq)

**原文标题**: [GitHub - lirantal/npq: safely install npm packages by auditing them pre-install stage · GitHub](https://github.com/lirantal/npq)

npq 是一个在安装 npm 包前进行安全审计的命令行工具，通过多项检查帮助用户避免安装有漏洞或恶意的包。

- 🛡️ **核心功能**：在安装前自动检查包的安全性，包括查询 Snyk 漏洞数据库、检查包年龄、下载量、README、许可证、安装脚本等。
- ⚡ **快速使用**：通过 `npx npq install <包名>` 即可使用，支持 `--dry-run` 仅检查不安装。
- 🔧 **集成日常**：可通过别名（如 `alias npm='npq-hero'`）无缝替换 npm 命令，自动执行安全审计。
- 📊 **多种检查器**：包含年龄、作者、下载量、README、仓库、脚本、Snyk 漏洞、许可证、过期域名、签名、来源证明、版本成熟度、新二进制文件、拼写错误、弃用状态等 15 种检查。
- 🚫 **禁用检查**：通过环境变量（如 `MARSHALL_DISABLE_SNYK=1`）可单独禁用某项检查。
- ⏱️ **自动继续模式**：默认检测到警告后等待 15 秒自动继续安装，可通过 `--disable-auto-continue` 强制要求手动确认。
- 🔗 **多包管理器支持**：支持 npm、yarn、pnpm，通过 `NPQ_PKG_MGR` 环境变量指定。
- ⚠️ **免责声明**：无法保证绝对安全，恶意包可能通过所有检查。
- 📚 **学习资源**：作者 Liran Tal 提供 Node.js 安全编码教程。

---

### [使用 Lambda 持久函数构建 CI](https://depot.dev/blog/building-ci-with-durable-lambda?utm_source=fnf&utm_medium=newsletter&utm_campaign=depot-may&utm_term=javascript-weekly&utm_content=microvms)

**原文标题**: [Building CI with Lambda durable functions](https://depot.dev/blog/building-ci-with-durable-lambda?utm_source=fnf&utm_medium=newsletter&utm_campaign=depot-may&utm_term=javascript-weekly&utm_content=microvms)

Depot CI 使用 AWS Lambda 持久函数构建其编排器，实现了长时间运行、有状态的工作流管理，而无需持续运行服务器。

- 🚀 **核心架构**：CI 编排器基于 AWS Lambda 持久函数，支持长达一年的执行时间，通过检查点和挂起/恢复机制实现，突破了普通 Lambda 的 15 分钟限制。
- 🔗 **触发路径**：所有触发器（如 GitHub webhook、cron 等）通过 SQS 队列统一调用持久 Lambda，SQS 提供重试和死信队列功能，确保可靠性。
- 🆔 **幂等性**：每个持久执行使用唯一名称（基于运行 ID 和工作流 ID），防止 SQS 重试导致重复编排器。
- 🏗️ **三层架构**：分为 Run Lambda、Workflow Lambda 和 Job 层。Run Lambda 处理整个运行（克隆仓库、编译 YAML 为 IR 和 DAG），然后扇出到 Workflow Lambda。
- ⚙️ **两层 Lambda 设计**：将工作流拆分为独立 Lambda，避免单个持久执行的操作上限（3000 次）影响整个运行，确保故障隔离。
- 🔄 **编排循环**：Workflow Lambda 以 while 循环运行状态机，每次迭代从数据库加载状态，调度新任务，然后挂起等待回调。回调驱动而非轮询，节省计算资源。
- 📞 **回调机制**：使用回调（而非轮询）通知任务完成、取消、重试或并发唤醒。回调通过 Depot API 和 AWS SendDurableExecutionCallbackSuccess 触发，支持超时防止任务卡死。
- 💻 **计算分离**：编排器仅作为状态机和回调集，实际任务交给独立计算提供者（如沙箱），完成后通过回调唤醒编排器。
- ✅ **持久函数优势**：内置崩溃恢复（从检查点重放）、无需长期运行进程、扇出映射清晰、事件间睡眠节省成本。
- 🧠 **学习曲线**：需适应重放思维（所有副作用必须在 ctx.step() 内），并谨慎管理操作预算和步骤边界。

---

### [迷你沙虫再次出击：317 个 npm 包遭篡改——实时开源软件供应链安全](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/)

**原文标题**: [Mini Shai-Hulud Strikes Again: 317 npm Packages Compromised - Real-time Open Source Software Supply Chain Security](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/)

2026 年 5 月 19 日，npm 账户`atool`遭入侵，攻击者在 22 分钟内向 317 个包发布了 637 个恶意版本，植入了 Mini Shai-Hulud 恶意工具包，用于窃取凭证、持久化控制并横向传播。

- 🎯 **大规模供应链攻击**：攻击者利用被入侵的`atool`账户，在 22 分钟内自动化发布了 637 个恶意版本，影响了 317 个 npm 包，包括`size-sensor`、`echarts-for-react`等高下载量包。
- 🔑 **凭证窃取范围极广**：恶意载荷通过环境变量、配置文件、云元数据服务（AWS、GCP、Azure）、Kubernetes、HashiCorp Vault、GitHub PAT、npm 令牌、SSH 密钥及本地密码管理器（1Password、Bitwarden 等）全面窃取凭证。
- 📡 **双重数据外泄通道**：窃取的数据通过两个并行通道外泄：一是以 Git 对象形式提交到公开的 GitHub 仓库（伪装为`python-requests`流量）；二是通过 RSA+AES 加密的 HTTPS POST 请求发送到伪装成 OpenTelemetry 追踪端点的攻击者服务器。
- 🧬 **多层持久化机制**：恶意软件通过注入 CI/CD 工作流（`codeql.yml`）、劫持 AI 编程助手（Claude Code、Codex、VS Code）、安装系统服务（systemd/LaunchAgent）以及横向感染本地 Node.js 项目来实现持久化。
- 🐳 **容器逃逸与云环境利用**：载荷会尝试通过 Docker 套接字进行容器逃逸，并在 CI 环境中利用 OIDC 令牌交换获取 npm 发布令牌，同时使用 Sigstore 对恶意工件进行合法签名。
- 🧩 **利用 GitHub“孤儿提交”实现冗余投递**：630 个恶意版本通过`optionalDependencies`字段引用`antvis/G2`仓库中的伪造“孤儿提交”，这些提交没有分支归属，利用 GitHub 的 fork 对象共享机制托管载荷副本，即使`preinstall`钩子被阻止也能执行。

---

### [更新中且持续的供应链攻击瞄准 CrowdStrike...](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages)

**原文标题**: [Updated and Ongoing Supply Chain Attack Targets CrowdStrike ...](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages)

AI 驱动的"氛围编码"正改变软件开发方式，虽带来安全风险，但 LLM 的崛起仍指向更安全、创新的未来。
- 🎙️ Socket CEO 与 a16z 合伙人探讨 AI 编码趋势，强调"氛围编码"概念
- ⚠️ AI 生成的代码可能引入新的安全漏洞，需谨慎审查
- 🚀 LLM 虽存在风险，但能加速开发并提升整体安全性
- 🔒 未来方向：在创新与安全之间找到平衡点
- 💡 对话强调 AI 工具应作为辅助，而非完全替代人类判断

---

### [迷你沙胡德再次出击：317 个 npm 包被攻陷——实时开源软件供应链安全](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/#full-list-of-compromised-packages)

**原文标题**: [Mini Shai-Hulud Strikes Again: 317 npm Packages Compromised - Real-time Open Source Software Supply Chain Security](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/#full-list-of-compromised-packages)

2026 年 5 月 19 日，npm 账户`atool`遭入侵，攻击者在 22 分钟内发布了 317 个包的 637 个恶意版本，这些包每月下载量达数百万次。恶意负载是一个 498KB 的混淆 Bun 脚本，用于窃取凭证、在 CI/CD 环境中持久化，并劫持 AI 编码工具。

- 🚨 **大规模供应链攻击**：`atool`账户被入侵，在 22 分钟内发布了 317 个包的 637 个恶意版本，影响`size-sensor`（420 万次/月）、`echarts-for-react`（380 万次/月）等高流量包。
- 🎯 **凭证窃取**：负载窃取 AWS、GCP、Azure 凭证、Kubernetes 服务账户令牌、HashiCorp Vault 令牌、GitHub PAT、npm 令牌、SSH 密钥以及 1Password/Bitwarden 等本地密码管理器。
- 📤 **双重数据外泄**：窃取的数据通过两条并行通道外泄：提交到公共 GitHub 仓库的 Git 对象，以及伪装成 OpenTelemetry 追踪数据的 RSA+AES 加密 HTTPS POST 请求。
- 🔄 **CI/CD持久化**：在 CI 环境中，负载交换 GitHub Actions OIDC 令牌以获取 npm 发布令牌，通过 Sigstore 对工件进行签名，并将恶意工作流注入`.github/workflows/codeql.yml`。
- 🤖 **AI 代理劫持**：通过注入`SessionStart`钩子劫持 Claude Code 和 Codex，在每次 AI 会话时重新执行恶意软件；VS Code 通过`"runOn": "folderOpen"`任务的`tasks.json`实现相同效果。
- 🐚 **持久化后门**：安装一个名为`kitty-monitor`的 systemd 服务/macOS LaunchAgent，运行一个 GitHub 死信 C2 后门，该后门每小时轮询 GitHub 的提交搜索 API，以获取 RSA-PSS 签名的命令。
- 🐳 **容器逃逸**：负载尝试通过主机套接字进行 Docker 容器逃逸，并横向传播感染到本地其他 Node.js 项目。
- 🕵️ **伪造提交**：630 个恶意版本包含指向`antvis/G2`仓库中孤立伪造提交的可选依赖项，这些提交托管有效负载的副本，而无需对目标仓库进行写访问。
- 🛡️ **缓解措施**：检查锁定文件中是否有 2026-05-19 发布的受影响包版本；轮换所有暴露的凭证；阻止`t.m-kosche[.]com`；审计 CI/CD 流水线；使用锁定文件并固定依赖项。

---

### [2ality 博客：暂时离线](https://2ality.com/)

**原文标题**: [2ality blog: temporarily offline](https://2ality.com/)

概述摘要  
由于收入骤降和 AI 爬虫流量激增，博客及书籍暂时下线以应对版权问题。  

- 📉 书籍销售收入从 2024 年足以维生骤降至 2026 年归零  
- 🤖 AI 爬虫导致流量激增，远超可负担范围，且无广告收入  
- 🔒 暂时下线博客和免费书籍，以应对 AI 公司盗用内容  
- ⏳ 处理过程可能需要数月，作者目前无力应对  
- 📚 人类读者仍可通过 Payhip 购买实体书籍  
- 😔 作者对给读者带来的不便致歉

---

### [获取失败](https://javascriptweekly.com/link/185313/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/185313/web)

无法总结：获取内容失败，状态码 403。

---

### [我在 Bun 工作，这是我的分支。整个帖子反应过度了。302 co... | Hacker News](https://news.ycombinator.com/item?id=48019226)

**原文标题**: [I work on Bun and this is my branch This whole thread is an overreaction. 302 co... | Hacker News](https://news.ycombinator.com/item?id=48019226)

概述摘要  
Bun 作者 Jarred 澄清，将 Bun 从 Zig 移植到 Rust 的代码仅为一个实验性分支，尚未承诺重写，且很可能被完全废弃。此举引发了社区过度反应，但作者认为探索不同语言版本有助于比较性能与可维护性。讨论中涉及 AI 辅助代码移植的潜力、开源项目维护者的责任、以及语言社区间的情绪化争论。

- 🧪 实验性分支：Bun 作者 Jarred 表示，Zig 到 Rust 的移植代码仅为实验性分支，尚未承诺重写，且可能被完全废弃。
- 💬 社区过度反应：该分支引发 302 条评论，作者认为这是过度反应，并强调代码尚未工作。
- 🤖 AI 辅助移植：作者对 AI（如 Claude）生成的 Rust 版本感兴趣，希望比较其与 Zig 版本在性能、可维护性上的差异。
- ⚖️ 语言争论：讨论中反映了 Rust 与 Zig 社区间的情绪化争论，部分用户认为语言应共存而非对立。
- 🔧 开源责任：用户质疑 Bun 团队优先处理新功能而非修复旧 bug（如 2023 年报告的 issue），但作者强调开源维护者无义务满足所有需求。
- 🌱 实验价值：部分评论认可实验对理解项目结构的意义，并期待后续分析报告。
- 💡 AI 生态影响：有用户计算该实验的 AI token 消耗约 40 百万，成本约 200-500 美元，并讨论其生态影响。

---

### [用 Rust 重写 Bun · Jarred-Sumner · 拉取请求 #30412 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/30412)

**原文标题**: [Rewrite Bun in Rust by Jarred-Sumner · Pull Request #30412 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/30412)

Bun 运行时已用 Rust 重写，合并了 6755 次提交，通过了所有现有测试，并修复了多个内存泄漏和不稳定的测试。

- 🔄 核心运行时从 Zig 迁移至 Rust，代码架构和数据结构基本保持不变
- 📦 二进制体积缩小 3-8 MB，基准测试性能持平或更快
- 🛡️ 引入编译器辅助工具，用于捕获和防止内存错误，减少团队调试时间
- 🧪 通过了所有平台上的现有测试套件，修复了多个内存泄漏和脆弱测试
- ⚠️ 仍有一些优化和清理工作，将在后续 PR 中完成
- 🚀 可通过 `bun upgrade --canary` 试用，遇到问题请提交 issue

---

### [所有 Rust 代码库：该代码库甚至无法通过最基本的 miri 检查，在安全 Rust 中允许未定义行为 · 问题 #30719 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/issues/30719)

**原文标题**: [all of rust codebase: This codebase fails even the most basic miri checks, allows for UB in safe rust · Issue #30719 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/issues/30719)

### 概述摘要
该内容是一个关于 Bun 项目（基于 Rust）的 GitHub Issue，报告了 Rust 代码中存在未定义行为（UB）的问题，并建议不要依赖 AI 编写 Rust 代码。

- 🐛 **未定义行为错误**：代码在安全 Rust 中构造了无效的`&[u8]`引用，导致悬垂指针和 UB。
- 🔍 **具体问题位置**：错误发生在`src/main.rs:97`，使用`core::slice::from_raw_parts`时出现无来源的指针。
- 💻 **复现代码示例**：通过`Box`分配内存后立即释放，再尝试访问切片，触发了 UB。
- ⚠️ **安全警告**：该 UB 在 Miri 检查中失败，违反了 Rust 的内存安全保证。
- 🤖 **开发者建议**：建议不要使用 AI 编写 Rust 代码，因为 AI 不擅长处理 Rust 的内存安全细节，应雇佣真正的 Rust 开发者。

---

### [Bun Rust 重写：“代码库未通过基本 miri 检查，在安全 Rust 中允许未定义行为” | Hacker News](https://news.ycombinator.com/item?id=48150900)

**原文标题**: [Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe rust" | Hacker News](https://news.ycombinator.com/item?id=48150900)

## 概述总结
Bun 项目被 Anthropic 收购后，使用 AI 将 Zig 代码库大规模移植到 Rust，但合并的代码存在严重的安全问题，引发了社区对项目方向和质量控制的广泛质疑。

- 🔴 **严重安全问题**：Rust 移植代码中，安全接口包装了不安全的操作，导致在安全 Rust 代码中也能触发未定义行为（UB），Miri 工具已检测到问题
- 🤖 **AI 驱动的移植**：团队使用 AI 在一周内完成了超过百万行的 Zig 到 Rust 的代码移植，但代码缺乏人工审查，被批评为"AI 垃圾代码"
- 🏢 **收购后的方向转变**：Anthropic 收购后，Bun 的决策风格引发社区担忧，被认为可能沦为 Anthropic 的内部工具
- 💔 **社区信任危机**：多位长期用户和贡献者表示失望，部分公司已决定从 Bun 迁移回 Node.js
- 🧩 **移植策略争议**：批评者认为应该先使用确定性工具（如 c2rust）进行翻译，而非依赖 AI 生成不可靠的代码
- 🛠️ **技术债务问题**：移植代码包含大量 unsafe 块（超过 13000 行），且未继承 Rust 的安全保证，需要后续逐步修复
- 📉 **稳定性隐患**：Bun 在 Zig 版本时就存在段错误问题，社区担心移植到 Rust 后问题可能恶化而非改善
- 🎯 **营销动机质疑**：许多人认为这是 Anthropic 为推广其 AI 产品而策划的营销活动，而非真正的工程决策
- 🔄 **Zig 社区关系**：Bun 此前与 Zig 项目因 AI 贡献政策产生冲突，被迫维护自己的 Zig 分支，这加速了迁移决定
- ⚖️ **工程伦理讨论**：这一事件引发了关于 AI 生成代码质量、开源项目责任和工程诚信的广泛讨论

---

### [@deno.land 在 Bluesky 上](https://bsky.app/profile/deno.land/post/3mm6clkq5uc22)

**原文标题**: [@deno.land on Bluesky](https://bsky.app/profile/deno.land/post/3mm6clkq5uc22)

概述摘要  
Deno 2.8 版本发布，是迄今为止最大的次要版本更新，大幅提升 Node.js 兼容性，并引入多项新功能。  

- 🚀 Deno 2.8 本周发布，是史上最大的次要版本  
- 📈 Node.js 兼容性从 42% 提升至 75% 以上，自 2.7 版本以来新增 500 多个兼容提交  
- 🛠️ 支持 TypeScript 6.0.3 和 `import defer`  
- 🔧 新增多个子命令、目录工作区功能和 CPU 火焰图  
- 🎉 包含众多其他改进

---

### [使用新的 HTML 安装元素安装 Web 应用 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/install-element-ot)

**原文标题**: [Install web apps with the new HTML install element  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/install-element-ot)

Chrome 推出新的 `<install>` HTML 元素，让网页应用安装无需 JavaScript，简化流程并提升浏览器信任度。

- 🆕 **新元素简化安装**：`<install>` 元素是声明式 HTML，无需 JavaScript，浏览器直接渲染可信安装按钮，支持同源和跨源应用安装。
- 🌐 **跨源安装支持**：通过 `installurl` 属性可安装不同源的应用，并用 `manifestid` 指定清单 ID，适合构建应用目录页。
- 🛡️ **浏览器控制增强信任**：按钮内容由浏览器管理，类似权限元素，用户点击更可信，减少意外安装提示。
- 🔄 **回退与检测**：元素内可放回退内容（如链接），或使用 `HTMLInstallElement` 检测支持，灵活适配不支持浏览器。
- 📡 **事件监听**：支持 `promptaction`、`promptdismiss`、`validationstatuschanged` 事件，跟踪安装成功、取消或验证错误。
- 🧪 **试用方式**：可在 Chrome/Edge 148+ 启用 flag 本地测试，或注册 origin trial（版本 148-153）用于生产环境。
- 📊 **与 Web Install API 对比**：`<install>` 声明式、代码少、信任度高、自定义少；`navigator.install()` 命令式、需 JavaScript、自定义强、信任度低。
- 🗣️ **反馈渠道**：开发者可提交反馈至 WICG 或 Edge 博客相关 issue，帮助决定未来支持方向。

---

### [Express.js 的新面貌](https://expressjs.com/en/blog/2026-05-18-a-new-look-for-express/)

**原文标题**: [A New Look for Express · Express.js](https://expressjs.com/en/blog/2026-05-18-a-new-look-for-express/)

Express 网站经历了全面改版，包括全新的视觉标识、文档系统和品牌定位。

- 🚀 **网站全面重建**：从 Jekyll 迁移到 Astro，提升了性能、国际化支持和内容管理灵活性。
- 📚 **文档体验升级**：新增多版本支持、AI 自然语言搜索（基于 Orama）和 llms.txt 端点，方便 AI 工具访问。
- 🎯 **未来文档计划**：填补内容空白、完善翻译、确保文档与版本同步发布，并鼓励社区贡献。
- 🎨 **全新品牌标识**：通过社区协作设计新 Logo，体现极简与清晰，并明确愿景、使命和品牌价值观。
- 🤝 **社区驱动成果**：由 Sebastian Beltran 领导，Orama 团队赞助，多位贡献者参与，历时一年多完成。

---

### [安装 · Express.js](https://expressjs.com/en/5x/starter/installing/)

**原文标题**: [Installing · Express.js](https://expressjs.com/en/5x/starter/installing/)

本指南介绍了如何安装 Express 框架，并创建基础应用。

- 📦 确保已安装 Node.js 18 或更高版本
- 📁 创建项目目录并进入：`mkdir myapp && cd myapp`
- 📝 使用 `npm init` 初始化 `package.json` 文件，可接受默认设置，但建议将入口文件设为 `app.js`
- ⚙️ 安装 Express 并添加到依赖列表：`npm install express`
- ⏳ 如需临时安装而不保存依赖，可使用：`npm install express --no-save`

---

### [发布 22.0.0-rc.0 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v22.0.0-rc.0)

**原文标题**: [Release 22.0.0-rc.0 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v22.0.0-rc.0)

Angular v22.0.0-rc.0 预发布版本概述

- 🎉 发布 Angular v22.0.0-rc.0 预发布版本，包含 119 次提交至主分支
- 🔧 编译器更新：强制 `:host-context` 参数使用括号，保留动画定义中的前导逗号，移除对旧版 Shadow DOM 选择器的支持
- 🛠️ 编译器更新：移除已弃用的 Shadow CSS 封装 polyfill，简化 `:host` 与选择器列表的处理，修复无效 for 循环的类型检查
- 🌐 平台服务器更新：将 `BEFORE_APP_SERIALIZED` 错误转发至 ErrorHandler
- 👍 获得 13 个点赞和 7 个火箭表情反应

---

### [表单 • 概览 • Angular](https://angular.dev/guide/forms/signals/overview)

**原文标题**: [Forms • Overview • Angular](https://angular.dev/guide/forms/signals/overview)

### 概述总结
Signal Forms 是 Angular 中基于信号（Signals）的实验性表单管理库，通过自动双向绑定、类型安全字段访问和集中化验证逻辑，简化表单状态管理，适用于 Angular v21+ 的新项目。

- ⚠️ **实验性特性**：API 可能在未来版本中变更，生产环境需谨慎使用。
- 🔄 **自动同步状态**：自动同步表单数据模型与绑定字段，减少样板代码。
- 🛡️ **类型安全**：支持完全类型安全的模式定义与 UI 控件绑定。
- 📋 **集中验证**：通过验证模式（Schema）统一管理所有验证规则。
- 🚀 **适用场景**：最适合基于信号构建的新应用；现有项目仍可选用响应式表单。
- 📦 **快速集成**：从 `@angular/forms/signals` 导入 `form`、`FormField`、`required`、`email` 等函数和指令。
- 🔧 **后续学习**：可参考信号表单基础、模型设计、字段状态管理、验证及自定义控件等指南。

---

### [[已完成] RFC：将 OnPush 设为默认变更检测策略 · angular/angular · 讨论 #66779 · GitHub](https://github.com/angular/angular/discussions/66779)

**原文标题**: [[Complete] RFC: Setting OnPush as the default Change Detection Strategy · angular/angular · Discussion #66779 · GitHub](https://github.com/angular/angular/discussions/66779)

Angular 計畫將 OnPush 變更偵測策略設為預設，並重新命名現有預設策略為 Eager，以配合無 zone 的未來發展。

- 🚀 **OnPush 成為預設**：Angular 元件將預設使用 `ChangeDetectionStrategy.OnPush`，這是長久以來的最佳實踐，並與無 zone 架構相容。
- ✏️ **重新命名策略**：現有的 `ChangeDetectionStrategy.Default` 將重新命名為 `ChangeDetectionStrategy.Eager`，以更準確反映其行為（積極檢查 DOM 更新），避免混淆。
- 🔄 **自動遷移**：Angular v22 將提供自動遷移工具，為現有程式碼明確設定 `ChangeDetectionStrategy.Eager`，以保留現有行為。
- 🗓️ **時程規劃**：`ChangeDetectionStrategy.Eager` 將於 v21.2 引入，而預設策略的變更則計畫在 v22（2026 年 5 月）實施。
- 💬 **社群反饋**：獲得廣泛正面支持，開發者認為此舉簡化了程式碼、符合現代 Angular 模式，並有助於教育與遷移。

---

### [Bun v1.3.14 | Bun 博客](https://bun.com/blog/bun-v1.3.14)

**原文标题**: [Bun v1.3.14 | Bun Blog](https://bun.com/blog/bun-v1.3.14)

Bun 1.2 发布，带来大量新功能和性能改进。

- 🖼️ **内置图像处理**：新增 `Bun.Image` API，支持 JPEG、PNG、WebP、GIF、BMP 等格式，无需安装原生模块即可进行缩放、旋转、编码等操作，性能优于 `sharp` 库。
- 📦 **全局虚拟存储**：`bun install` 新增 `globalStore` 选项，通过全局符号链接共享包，大幅减少磁盘占用和安装时间（如 1400 个包的安装从 841ms 降至 115ms）。
- 🌐 **HTTP/3 (QUIC) 支持**：`Bun.serve` 新增 `http3: true` 选项，支持 HTTP/3 协议，性能是 HTTPS/1.1 的 2-3 倍（静态路由达 509,135 req/s）。
- 🚀 **实验性 HTTP/2 和 HTTP/3 客户端**：`fetch()` 支持 `protocol` 选项（`"http2"`、`"http3"`），可复用连接、多路复用，并支持 Alt-Svc 自动升级。
- 👀 **重写 fs.watch()**：基于 inotify/FSEvents/kqueue 原生 API，修复递归监听新目录、文件删除后重新监听等问题，macOS 线程开销减半。
- 🛡️ **--no-orphans 防孤儿进程**：父进程被 `SIGKILL` 时自动退出，并递归杀死所有子进程，支持 Linux (prctl) 和 macOS (kqueue)。
- ⚡ **process.execve() 支持**：实现 Node.js v24 的 `process.execve`，可替换当前进程映像。
- 🪟 **Windows ConPTY 终端**：`Bun.Terminal` 和 `Bun.spawn({ terminal })` 现支持 Windows 伪终端。
- 🔧 **using/await using 原生支持**：针对 Bun 目标不再降级转换，直接使用 JavaScriptCore 原生实现。
- 📉 **内存优化**：TLS 连接共享 `SSL_CTX` 缓存，修复 MongoDB/Mongoose 等库的内存泄漏；GC 减少对内置对象的冗余扫描。
- ⚙️ **跨语言 LTO**：Zig 和 C++ 边界启用全链接时优化，HTTP 吞吐量提升 3.5%，`escapeHTML` 快 6.5%。
- 📚 **bun publish 发送 README**：自动将 README 文件内容发送到 npm 注册表，与 `npm publish` 行为一致。
- 🐛 **大量 Bug 修复**：修复了 node:http、TLS、zlib、crypto、fs.watch、WebSocket、bun install、Bun.serve 等数百个问题，涵盖内存泄漏、崩溃、兼容性等。

---

### [GitHub - eslint/config-inspector：用于检查和理解ESLint扁平配置的可视化工具。](https://github.com/eslint/config-inspector)

**原文标题**: [GitHub - eslint/config-inspector: A visual tool for inspecting and understanding your ESLint flat configs. · GitHub](https://github.com/eslint/config-inspector)

ESLint Config Inspector 是一个用于可视化和理解 ESLint 平面配置的视觉工具，支持在线预览、静态构建及实时更新。

- 🔍 通过运行 `npx @eslint/config-inspector@latest` 可在 `http://localhost:7777/` 查看和操作 ESLint 配置，并支持自动更新
- 🌐 提供在线预览功能，可直接在浏览器中体验工具
- 📦 支持静态构建：`npx @eslint/config-inspector build` 生成 SPA 应用，便于部署和对比
- 🛠️ 开发技术栈包括 pnpm、Nuxt、Vue、UnoCSS 和 ESLint，使用 devframe 进行 RPC 传输和静态构建
- 🤝 遵循 ESLint 贡献指南，欢迎通过 issues 参与贡献
- 📜 采用 Apache-2.0 许可证，并有赞助商支持持续开发

---

### [发布说明 1.0 | TypeORM](https://typeorm.io/docs/releases/1.0/release-notes/)

**原文标题**: [Release Notes 1.0 | TypeORM](https://typeorm.io/docs/releases/1.0/release-notes/)

TypeORM 1.0 是一个重大版本更新，移除了长期弃用的 API，提升了平台要求，并带来了大量错误修复和新功能。

- 🚀 **平台要求提升**：Node.js 20+ 是必须的，移除了对 Node.js 16 和 18 的支持；JavaScript 目标升级至 ES2023；移除了 `Buffer` polyfill，改用 `Uint8Array`；用 `tinyglobby` 替换了 `glob`；哈希功能迁移至原生 `crypto` 模块。
- 🗑️ **移除的 API**：`Connection` 和 `ConnectionOptions` 被 `DataSource` 和 `DataSourceOptions` 取代；移除了 `findByIds`、`findOneById`、`Repository.exist()`、`@RelationCount` 装饰器、IoC 容器系统等；全局便捷函数如 `createConnection`、`getConnection` 等也被移除。
- 🐛 **错误修复**：修复了查询生成、关系与预加载、持久化等多个方面的问题，包括列别名转义、子查询列解析、级联删除、软删除处理、值转换器应用等。
- ✨ **新功能**：查询构建器新增 `valuesFromSelect()` 方法；更新/更新插入操作支持 `returning` 选项；所有 drop 方法新增 `ifExists` 参数；`QueryRunner` 支持显式资源管理；数据源级别默认隔离级别；PostgreSQL 的 `ADD VALUE` 枚举变更语法；SAP HANA 的锁支持等。
- 🔒 **安全修复**：通过参数化查询和转义标识符，在所有驱动程序中预防 SQL 注入；对 `orderBy` 和 `addOrderBy` 的条件值进行运行时验证；限制 `limit()` 方法在更新/软删除查询构建器中的使用。
- ⚡ **性能改进**：PostgreSQL 和 CockroachDB 的 `clearDatabase()` 方法现在使用批量 DROP 语句，减少了测试设置期间的往返次数。
- 🔄 **行为变更**：非空关系现在使用 `INNER JOIN`；`invalidWhereValuesBehavior` 默认值改为 `throw`；`ConnectionOptionsReader` 和 `FileLogger` 的路径从 `process.cwd()` 解析。
- 🛠️ **驱动变更**：MySQL 仅支持 `mysql2`；SQLite 默认使用 `better-sqlite3`；MongoDB 驱动要求 v7+；移除了 Redis 旧版客户端支持；移除了 Expo 旧版驱动。
- 📦 **其他**：新增 `@typeorm/codemod` 包用于自动化迁移；改进了 ormconfig 错误处理；CLI `init` 命令不再崩溃。

---

### [ESLint v10.4.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/05/eslint-v10.4.0-released/)

**原文标题**: [ESLint v10.4.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/05/eslint-v10.4.0-released/)

ESLint v10.4.0 发布，新增 includeIgnoreFile() 辅助函数，修复多个 Bug，并更新文档与内部工具。

- 🚀 新增 `includeIgnoreFile()` 辅助函数，支持从 `.gitignore` 文件或类似格式的文件中引入忽略规则，并可处理多个文件及相对路径。
- 🔍 功能更新：检查 `for-direction` 中的序列表达式，并将 `includeIgnoreFile()` 集成到 `eslint/config` 入口。
- 🐛 修复多个 Bug：包括调试输出中的代码路径 DOT 标签转义、依赖项更新、以及非数组废弃规则替换处理。
- 📚 文档改进：提及 `@eslint-react/eslint-plugin`、调整 CJS 与 ESM 配置的表述，并更新 README 文件。
- 🛠️ 内部维护：升级 knip 工具、优化 CI 流程、增加单元测试（如 SuppressionsService 和 ast-utils）、重构代码（移除废弃的 `meta.language`）并更新生态系统插件。

---

### [发布 v21.0.0 · facebook/relay · GitHub](https://github.com/facebook/relay/releases/tag/v21.0.0)

**原文标题**: [Release v21.0.0 · facebook/relay · GitHub](https://github.com/facebook/relay/releases/tag/v21.0.0)

Relay v21.0.0 版本正式发布，带来了对 TypeScript 的一流支持、现代化的 Flow 类型生成、新的错误处理能力以及实验性的 React Server Components 支持。此版本包含多项重大变更，升级时请仔细阅读迁移说明。

- 🎉 **TypeScript 用户福音**：`relay-runtime` 和 `react-relay` 现在直接内置 `.d.ts` 类型定义，不再需要 `@types/relay-runtime`，且支持 Node.js ESM 命名导入。
- 🔄 **Flow 用户需注意**：生成的类型现在使用现代 Flow 语法（如 `(expr as Type)` 代替 `(expr: Type)`），需要重新运行编译器生成产物，并确保 Flow 版本 >= 0.250.0。
- ❌ **`@live_query` 指令已移除**：请迁移至 `@client_polling(interval: ...)` 实现轮询，或使用 `@live` 获取服务端推送更新。
- 🛠️ **Relay Resolvers 新语法**：旧的 `@RelayResolver` 标签已被 `@relayField` 和 `@relayType` 取代，编译器可通过 `relay-compiler codemod fix-all` 命令自动迁移。
- 🔒 **`@oneOf` 输入类型更严格**：现在生成更严格的联合类型，一次只允许设置一个属性，有助于在编译时捕获错误。
- 🆕 **`@catch` 扩展**：现在支持在 `@connection` 字段和客户端边字段上使用，优雅处理分页和客户端边场景中的字段错误。
- 🏷️ **`@alias` 支持片段定义**：`@alias` 指令现在可用于片段定义，而不仅仅是内联片段。
- 🧪 **实验性 React Server Components 支持**：新增 `react-relay/rsc_EXPERIMENTAL` 入口点，提供 `serverFetchQuery`、`serverReadFragment`、`serverPreloadQuery` 和 `useQueryFromServer` 等 API。
- 🐛 **大量 Bug 修复**：包括大型 schema 崩溃修复、`@raw_response_type` 准确性提升、`@match` 字段冲突检测、watch 模式稳定性改进等。
- 📚 **文档改进**：更新了 Relay Resolver 文档、修复多处拼写错误、升级到 Docusaurus v3 并添加了更多术语表定义。

---

### [发布 v1.0.1 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.0.1)

**原文标题**: [Release v1.0.1 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.0.1)

Rolldown v1.0.1 版本发布，包含多项新功能、错误修复、重构、性能优化和文档更新。

- 🚀 新增实验性功能：对超大 barrel 模块的优化建议、内联可选链枚举访问、去重已加载的动态依赖，以及调用 ParallelJsPlugin 中的 moduleParsed 钩子
- 🐛 修复多个错误：启用 enum_eval 转换、移除诊断消息中的严重性前缀、修复依赖版本问题、处理路径解析错误、修复懒加载导出问题等
- 🚜 重构代码：提取 semantic_builder_for_transform 辅助函数和可复用的静态导入循环测试辅助
- 📚 文档更新：澄清 topLevelVar 作用域、添加 AST 修改设计文档和贡献指南中的 AI 政策
- ⚡ 性能优化：启用 mimalloc v3 以减少空闲内存占用
- 🧪 测试增强：覆盖 require() 在 $initial 组中的使用，添加 CJS facade 块合并回归测试
- ⚙️ 杂项任务：迁移插件包、升级依赖、替换 GitHub Actions 为内联命令、清理工作流等
- ❤️ 新贡献者：Kyujenius、SAY-5 和 thescripted 首次贡献

---

### [我对 AI 的思考，第二部分：智能体设置、工作流程与工具 · Mark 的开发博客](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/)

**原文标题**: [
     My Thoughts on AI, Part 2: Agent Setup, Workflow, and Tools ·  Mark's Dev Blog
  ](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/)

本文详细介绍了作者个人使用 AI 进行软件开发的工作流程、工具配置和核心理念，强调开发者应保持主导权，通过精心设计的工具链和自动化脚本提升效率。

- 🧠 **核心理念**：开发者必须保持主导权，主动决定任务、方法和进度，AI 仅作为辅助工具加速代码实现。
- 🤖 **Agent 选择**：采用 OpenCode 作为主要 Agent，配合 CodeNomad 的 Web UI 进行开发，避免使用 TUI 界面。
- 🧩 **工作流程**：采用“父编排器 + 子任务”模式，父会话管理全局上下文，子任务负责具体开发，高度互动且由开发者驱动。
- 🔧 **工具配置**：高度定制 OpenCode 配置，包括权限管理（自动批准安全命令）、文件读取缓存（cachebro）、代码结构搜索（grepika 和 tilth）等。
- 📁 **文档管理**：建立独立的`dev-plans`仓库存储个人开发文档，通过`devplans.ts`脚本自动化进度记录、任务交接等操作。
- 📝 **AGENTS.md**：约 250 行的指令文件，定义交互模式、编码规范、代码导航策略和任务管理规则，持续优化。
- ⚙️ **自动化脚本**：使用 Bun 和 TypeScript 编写`devplans.ts`，自动化进度更新、任务交接、文档创建等重复性工作。
- 🚀 **未来改进**：计划增强长期记忆和上下文管理，自动索引扫描规划文件，并改进代码审查工具。

---

### [OpenCode | 开源 AI 编程代理](https://opencode.ai/)

**原文标题**: [OpenCode | The open source AI coding agent](https://opencode.ai/)

概述摘要  
OpenCode 是一款开源 AI 编程代理，支持多种模型和编辑器，注重隐私，拥有大量社区支持。

- 🖥️ **多平台支持**：提供终端、桌面应用（macOS/Windows/Linux）和 IDE 扩展，灵活使用。  
- 🤖 **多模型集成**：免费内置模型，或连接 Claude、GPT、Gemini 等 75+ 提供商，包括本地模型。  
- 🔄 **多会话并行**：可在同一项目上启动多个代理同时工作。  
- 🔗 **会话共享**：可生成链接分享会话，便于协作或调试。  
- 🛡️ **隐私优先**：不存储用户代码或上下文数据，适合隐私敏感环境。  
- 🌟 **社区庞大**：拥有 160K GitHub 星标、900+ 贡献者，每月服务 750 万开发者。  
- 🎯 **Zen 优化模型**：提供经过测试和基准验证的模型，确保编码代理性能稳定。  
- 📧 **新品通知**：可订阅邮件，抢先了解新发布产品。

---

### [API 密钥正式发布](https://clerk.com/changelog/2026-04-17-api-keys-ga?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=05-19-26&dub_id=rTqya0YesTuSGHb2)

**原文标题**: [API Keys General Availability](https://clerk.com/changelog/2026-04-17-api-keys-ga?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=05-19-26&dub_id=rTqya0YesTuSGHb2)

API 密钥现已正式发布，支持基于使用量的计费模式。

- 🔑 API 密钥于 4 月 6 日起正式可用，属于机器认证套件的一部分，允许用户创建代表其应用 API 的访问凭证。
- 💰 计费已启动，每月提供免费配额：前 1,000 次密钥创建免费，超出后每次 $0.001；前 100,000 次密钥验证免费，超出后每次 $0.00001。
- 📖 提供入门指南：API 密钥使用完整教程、后端 SDK 参考（含创建、列出、验证和撤销密钥的完整 API），以及仪表盘启用功能。
- 👥 贡献者包括 Jeff Escalante、Robert Soriano、Brandon Romano 和 Bruno Lin。

---

### [Node.js 内部机制、运行时与网络指南 | NodeBook](https://www.thenodebook.com/)

**原文标题**: [Node.js Internals, Runtime & Networking Guide | NodeBook](https://www.thenodebook.com/)

本资源提供对 Node.js 运行时的深入解析，涵盖从底层机制到生产实践的完整知识体系。

- 📘 **完整的第一卷数字版**：包含 EPUB、浅色/深色 PDF、幻灯片和速查表，共 35 章、205 个子章节，现已可购买。
- 🔧 **运行时核心机制**：详细解释 Libuv 事件循环、V8 编译管道、零拷贝流架构、原生插件开发、生产可观测性和内存管理。
- 🧠 **聚焦运行时行为**：通过实际示例（如背压与内存崩溃）展示 Node.js 在负载下的真实表现，超越语法层面。
- 📚 **七卷课程体系**：涵盖运行时基础、网络 API、工作执行与原生边界、数据与状态、安全、生产工程、架构与扩展，共 205 个子章节。
- 🎯 **目标读者**：面向有经验的 Node.js 开发者，帮助填补运行时可见性、内存泄漏排查、性能分析等常见知识空白。
- 💰 **免费在线阅读**：所有章节在线免费，无广告无追踪；付费数字版（$19.99）提供离线文件和额外资源。
- 🚧 **出版进度**：第一卷已完成，第二卷（网络 API）进行中，HTTP/TLS/API 设计章节即将发布。
- 📬 **更新订阅**：可订阅邮件获取新章节和发布说明，无垃圾邮件，随时可退订。
- 👤 **作者背景**：Ishtmeet Singh，自 2014 年从事 Node.js 开发，拥有 10 年以上经验，开源贡献者，读者超 70,000 人。

---

### [Node.js 事件循环：阶段、微任务与 libuv](https://www.thenodebook.com/node-arch/event-loop-intro#what-the-nodejs-event-loop-does)

**原文标题**: [Node.js Event Loop: Phases, Microtasks & libuv](https://www.thenodebook.com/node-arch/event-loop-intro#what-the-nodejs-event-loop-does)

以下是您提供的文章摘要：

Node.js 的架构核心在于事件循环，它由 libuv 的循环阶段和 Node.js 的 JavaScript 端优先级队列共同驱动。理解调用栈、微任务（microtasks）和宏任务（macrotasks）的执行顺序，是掌握 Node.js 异步行为的关键。

- 🧱 **单一调用栈**：JavaScript 只有一个调用栈，所有代码都在此执行。当一个函数占用栈顶时，其他任何回调都无法运行，这就是“阻塞”的本质。
- ⏱️ **事件循环的六大阶段**：一个完整的“tick”会依次经过定时器（Timers）、待定回调（Pending Callbacks）、轮询（Poll）、检查（Check）和关闭回调（Close Callbacks）等阶段，每个阶段处理对应的宏任务队列。
- 🔄 **微任务与 `process.nextTick()`**：微任务（包括 `process.nextTick()` 和 Promise 回调）拥有最高优先级。在执行完任何一个宏任务后，事件循环会立即清空所有微任务队列，然后才进入下一阶段。
- ⚠️ **`process.nextTick()` 的危险性**：递归调用 `process.nextTick()` 会无限循环，导致事件循环被“饿死”，从而使定时器和 I/O 操作永远无法执行。
- 🔗 **V8、libuv 与 C++ 绑定**：V8 执行 JS 代码，libuv 提供异步 I/O 和事件循环，C++ 绑定层则作为桥梁，将 JS 调用转化为 libuv 能理解的系统请求。
- 🧵 **libuv 线程池**：libuv 内部维护一个线程池（默认 4 个），用于处理阻塞性操作（如文件 I/O、DNS 查询、加密）。这些操作会在线程池中排队执行，不会阻塞主线程。
- 🚦 **`setTimeout(..., 0)` 与 `setImmediate()` 的顺序**：在主模块中执行时，顺序不确定；但在 I/O 回调中执行时，`setImmediate()` 总是先于 `setTimeout(..., 0)` 运行。
- 🐢 **性能陷阱**：大 JSON 解析、复杂正则表达式、以及 libuv 线程池的争用，都可能导致事件循环延迟。使用 `perf_hooks` 或简单的 `setInterval` 可以检测延迟。
- ⚙️ **CPU 密集型任务**：对于需要大量计算的任务，应使用 `worker_threads` 将其卸载到独立线程，或使用 `setImmediate()` 将任务分块执行，以保持事件循环的响应性。

---

### [Node.js 中的 V8：JIT、隐藏类与去优化](https://www.thenodebook.com/node-arch/v8-engine-intro)

**原文标题**: [V8 in Node.js: JIT, Hidden Classes & Deoptimization](https://www.thenodebook.com/node-arch/v8-engine-intro)

### 概述总结
V8 是 Node.js 内置的 JavaScript 引擎，通过多层级 JIT 编译管道（Ignition → Sparkplug → Maglev → TurboFan）执行代码。它依赖隐藏类（Hidden Classes）和内联缓存（ICs）实现快速属性访问，但对象形状不稳定、类型混合或使用 `delete` 等操作会触发去优化（Deoptimization），导致性能骤降。保持代码的单调性（Monomorphic）和对象形状稳定是优化关键。

- 🔍 **多层级编译管道**：V8 从 Ignition 解释器开始，收集类型反馈，逐步将热点代码提升至 Sparkplug（基线编译器）、Maglev（中端优化器）和 TurboFan（高级优化器），以平衡启动速度与峰值性能。
- 🧩 **隐藏类与对象形状**：V8 为每个对象创建隐藏类（Shape/Map），记录属性内存偏移。属性添加顺序或条件性新增会导致隐藏类分叉，破坏优化。预初始化所有属性（即使为 `null`）可保持形状稳定。
- ⚡ **内联缓存（IC）与单调性**：IC 在调用点缓存属性访问的隐藏类信息。单态（Monomorphic）访问最快，多态（Polymorphic，2-4 种形状）稍慢，超态（Megamorphic，过多形状）则退化为慢速字典查找。函数应只处理单一对象形状。
- ❌ **常见去优化触发**：隐藏类不匹配、数组元素类型混合（如从整数数组推入字符串）、使用 `arguments` 对象、`delete` 关键字（强制对象进入字典模式）、`try...catch`（现代 V8 已优化，但极端热路径仍需注意）。
- 🐢 **真实案例：100 倍延迟**：在配置对象上条件性添加属性导致隐藏类爆炸，触发反复去优化，P99 延迟从 2ms 飙升至 200ms。修复方式：预初始化所有可能属性，保持形状稳定。
- 🔧 **BigInt 去优化循环**：交易验证函数因偶尔出现 BigInt 值而反复去优化。解决方案：使用调度器分离 Number 和 BigInt 热路径，或通过 `typeof` 分支保持类型一致性。
- 💾 **内存布局与指针标记**：小整数（Smi）直接编码在指针中，无需堆分配；堆对象通过压缩指针（32 位）引用。删除操作会触发字典模式，导致所有属性访问变慢。
- ✅ **V8 友好编码模式**：使用类或工厂函数确保形状一致；函数保持单态；避免 `delete`，改用 `obj.prop = undefined`；使用剩余参数 `...args` 替代 `arguments`；在热路径中保持数组元素类型稳定。
- 🛠️ **诊断工具**：`--trace-deopt` 查看去优化原因，`--trace-opt` 跟踪优化函数，`--prof` 进行 CPU 性能分析，`--allow-natives-syntax` 使用 `%HaveSameMap()` 等内部 API 调试形状一致性。

---

### [Node.js 流：背压与数据流](https://www.thenodebook.com/streams/foundation-of-streams)

**原文标题**: [Node.js Streams: Backpressure & Data Flow](https://www.thenodebook.com/streams/foundation-of-streams)

### 概述总结
Node.js 流是处理大数据块的核心机制，通过分块传输、背压控制和事件驱动，避免内存溢出并实现高效并发处理。文章深入探讨了流的两种模型（推和拉）、混合架构、四种流类型（可读、可写、转换、双工）及实际应用场景。

- 📦 **问题核心**：传统“全量加载”方式处理大文件（如 2GB 视频）会导致内存爆炸和延迟，而流通过分块（如 64KB）处理，将内存占用从 2000MB 降至 64MB，效率提升 31 倍。
- 🔄 **推模型**：基于事件发射器（EventEmitter），生产者主动推送数据，消费者通过`data`事件响应。优点是简单、支持多消费者，但需额外实现背压机制防止消费者过载。
- ⏪ **拉模型**：基于迭代器（Iterator）和生成器（Generator），消费者主动请求数据（如`next()`）。背压隐式存在，支持惰性求值，但难以处理事件驱动场景（如 WebSocket）。
- ⚖️ **混合架构**：Node.js 流结合推和拉的优势——默认基于事件推送，但通过`drain`事件、暂停读取和`for await...of`异步迭代实现背压控制，确保内存使用有界。
- 🧩 **四种流类型**：可读流（如`fs.createReadStream`）产生数据；可写流（如`fs.createWriteStream`）消费数据；转换流（如`zlib.createGzip`）同时读写并转换数据；双工流（如`net.Socket`）独立双向通信。
- 🔗 **管道与背压**：数据向前流动（可读→转换→可写），背压信号向后传递（可写满时暂停上游）。管道通过`stream.pipeline()`实现健壮的错误处理，确保整个系统自适应慢速环节。
- 🛠️ **适用场景**：大文件 I/O、HTTP 请求/响应体、网络协议（TCP）、数据转换管道（ETL）、实时数据处理（消息队列、传感器）。小文件（如 10KB JSON）则无需流，直接读取更简单。
- 📜 **历史演进**：从最初无背压的简单事件流，到 v0.10 引入 Streams2（暂停/流动模式），再到 v10+ 增加`pipeline`、`finished`和异步迭代，流已成为 Node.js 生态的成熟抽象。

---

### [Node.js 模块解析：node_modules 与 exports](https://www.thenodebook.com/modules/resolution-algorithm)

**原文标题**: [Node.js Module Resolution: node_modules & exports](https://www.thenodebook.com/modules/resolution-algorithm)

Node.js 模块解析机制将导入或 require 的标识符转换为具体的模块记录。其核心逻辑涵盖内置模块、相对路径、绝对路径、包名、node_modules 目录向上遍历以及包元数据。CommonJS 和 ESM 共享部分概念，但各自拥有独立的解析规则。

- 📦 **标识符分类**：解析算法将 `require()` 的字符串分为三类：内置模块（如 `'fs'`）、相对/绝对路径（以 `./`、`../` 或 `/` 开头）和裸标识符（如 `'lodash'`）。分类决定了后续的代码路径。
- ⚡ **内置模块短路**：内置模块（如 `'fs'`）会直接从 Node 的内部注册表中返回，无需文件系统访问。`node:` 前缀可明确指定内置模块，防止与 npm 包冲突。
- 🔍 **路径扩展探测**：对于相对/绝对路径，Node 会按顺序尝试 `.js`、`.json`、`.node` 扩展名。如果路径指向目录，则会查找 `package.json` 的 `"main"` 字段，或回退到 `index.js`。
- 🏔️ **node_modules 爬升算法**：裸标识符会触发从调用文件所在目录向上遍历，在每个层级检查 `node_modules` 目录。该算法支持嵌套依赖和隔离版本。
- 🚧 **exports 字段**：`package.json` 的 `"exports"` 字段定义了包的公共 API，并限制内部文件的访问。它支持条件导出（如 `"import"` 和 `"require"`）和通配符模式。
- 🔗 **imports 字段**：`"imports"` 字段允许包内部使用 `#` 前缀的私有别名，避免深层相对路径的脆弱性。它仅限于定义它的包内使用。
- 🧩 **require.resolve()**：该函数运行完整的解析算法并返回文件的绝对路径，但不会实际加载模块。可用于条件加载和调试。
- 🔄 **符号链接行为**：解析算法默认会通过 `fs.realpathSync()` 解析符号链接，确保缓存键为真实路径。`--preserve-symlinks` 标志可禁用此行为。
- 🗂️ **解析缓存**：`Module._findPath` 使用内部缓存避免重复的文件系统调用。`require.cache` 存储已加载模块的缓存，可通过删除条目强制重新加载。
- 🛠️ **调试工具**：使用 `require.resolve()`、`Module._nodeModulePaths()` 或设置 `NODE_DEBUG=module` 环境变量可获取详细的解析日志，帮助定位模块未找到的错误。
- ⚠️ **边缘情况**：包括自引用（需 `"exports"` 字段）、`"type"` 字段对 `require()` 无影响、大小写敏感问题（macOS 与 Linux 差异）、以及多个 `package.json` 文件的上下文选择。

---

### [Node.js 中的异步/等待：挂起与微任务](https://www.thenodebook.com/async-patterns/async-await)

**原文标题**: [Async/Await in Node.js: Suspension & Microtasks](https://www.thenodebook.com/async-patterns/async-await)

### 概述总结
本文详细介绍了 Node.js 中 async/await 的工作原理、内部机制、调度顺序、错误处理模式以及生产实践。async 函数总是返回 Promise，await 会暂停函数执行，通过微任务恢复，并遵循特定的事件循环顺序。

- 🔄 **async 函数总是返回 Promise**：即使返回普通值（如 42），也会被包装成 Promise；抛出错误会拒绝返回的 Promise。
- ⏸️ **await 暂停当前 async 函数**：执行到 await 时，V8 保存函数状态并返回控制权，函数在微任务中恢复；代码在 await 之前是同步执行的。
- 📊 **Promise 链等价性**：每个 await 对应一个 .then() 回调，错误处理也类似；async/await 的优势在于保持词法作用域。
- 🧠 **V8 状态机实现**：V8 编译 async 函数时生成可暂停/恢复的字节码，使用 JSAsyncFunctionObject 跟踪状态，await 通过 PromiseReactionJob 恢复执行。
- ⏱️ **调度顺序规则**：await 后的代码作为微任务执行；process.nextTick() 优先于 Promise 微任务；多个 async 函数按 FIFO 顺序恢复。
- 🚨 **错误处理最佳实践**：使用 try/catch 捕获 await 的拒绝；return await 在 try/catch 中捕获错误；避免未处理的浮动 Promise。
- 🛠️ **重要模式**：顺序任务用 for...of；独立任务用 Promise.all() 并限制并发；避免在 forEach 中使用 async 回调；避免在 Promise 构造函数中使用 async 执行器。
- 💡 **生产实践**：默认使用 async/await；浮动 Promise 必须有 .catch()；在 try/catch 中使用 return await；保持作用域简洁；避免大量异步回调的数组方法。
- ⚡ **性能考量**：每个 await 有微成本（微任务、暂停/恢复）；在 I/O 密集型代码中差异可忽略；避免为同步工作创建 async 函数；注意内存泄漏（暂停的函数保留局部变量）。

---

### [获取失败](https://javascriptweekly.com/link/185340/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/185340/web)

无法总结：获取内容失败，状态码 415。

---

### [GitHub - tc39/proposal-shadowrealm: ECMAScript 提案、规范及 Realm 参考实现](https://github.com/tc39/proposal-shadowrealm)

**原文标题**: [GitHub - tc39/proposal-shadowrealm: ECMAScript Proposal, specs, and reference implementation for Realms · GitHub](https://github.com/tc39/proposal-shadowrealm)

ShadowRealm API 是 ECMAScript 规范提案，用于创建独立的全局环境，拥有自己的全局对象和内建函数。

- 🌐 ShadowRealm 提供完全隔离的全局环境，包含独立的内建对象和原型
- 📦 核心 API 包括 `ShadowRealm` 类，支持 `importValue()` 和 `evaluate()` 方法
- 🚀 当前处于 TC39 流程的 Stage 2.7 阶段
- 📅 自 2018 年起历经多次 TC39 会议讨论和更新
- 🛠 提案从最初的 `globalThis` 模型演变为更精简的隔离 realms API
- 📄 规范文本位于 `spec.html`，使用 ecmarkup 语言编写
- 👥 由多位 champions 共同推进，包括 @dherman、@caridy、@erights 等

---

### [npm 泄露事件后强化 TanStack | TanStack 博客](https://tanstack.com/blog/incident-followup)

**原文标题**: [Hardening TanStack After the npm Compromise | TanStack Blog](https://tanstack.com/blog/incident-followup)

TanStack 团队在经历 npm 软件包被恶意篡改事件后，进行了全面的安全审查和加固，现已确认所有仓库和软件包安全无虞。

- 🔒 **事件已完全解决**：经过三天的全面安全扫描和加固，所有 TanStack 仓库和软件包现已确认安全，可放心安装。
- 🚨 **攻击范围有限**：仅有 Router/Start 仓库的 42 个软件包受到影响，每个包仅 2 个版本被篡改，且已在一小时内被弃用并移除。
- 🛡️ **攻击手法隐蔽**：攻击者通过伪造的 Pull Request 利用 CI 缓存投毒，绕过了 OIDC、2FA 等现有安全措施，窃取了临时发布令牌。
- ⚙️ **已采取的紧急措施**：禁用了 pnpm 缓存、移除了受影响的 GitHub Actions 缓存、将所有操作固定到提交 SHA、强制要求非短信双因素认证、移除了所有 `pull_request_target` 使用、升级了 pnpm 版本。
- 🚧 **正在推进的长期改进**：计划引入 `zizmor` 静态分析器、对 `.github` 文件夹设置 `CODEOWNERS`、改用更保守的缓存方案，并正在讨论是否限制外部贡献者的 PR 权限。
- 💡 **核心教训**：CI 管道的安全性此前被忽视，团队将重点重建这一环节，并呼吁平台方改进缓存隔离等基础设施安全。

---

### [事后分析：TanStack npm 供应链安全事件 | TanStack 博客](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

**原文标题**: [Postmortem: TanStack npm supply-chain compromise | TanStack Blog](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

概述：TanStack 在 2026 年 5 月 11 日遭遇 npm 供应链攻击，攻击者通过组合利用 GitHub Actions 的`pull_request_target`漏洞、缓存投毒和 OIDC 令牌内存提取，在 42 个包中发布了 84 个恶意版本。攻击在 26 分钟内被外部研究人员发现，所有受影响版本已弃用，目前所有包均安全。

- 🔒 **攻击链**：攻击者利用`pull_request_target`的"Pwn Request"模式、GitHub Actions 缓存跨信任边界投毒，以及从运行进程内存中提取 OIDC 令牌，三者结合实现攻击
- 🕒 **时间线**：攻击者在 2026 年 5 月 10-11 日通过恶意 PR 投毒缓存，5 月 11 日 19:20-19:26 UTC 发布恶意包，19:46 UTC 被外部研究人员发现
- 📦 **影响范围**：42 个`@tanstack/*`包受到影响（每个包 2 个版本），包括 Router/Start 仓库；Query、Table、Form 等仓库未受影响
- 🦠 **恶意行为**：安装时执行`router_init.js`脚本，窃取 AWS、GCP、Kubernetes、Vault、npm、GitHub 和 SSH 凭据，通过 Session/Oxen 消息网络外泄，并能自我传播
- 🚨 **响应措施**：1 小时 43 分钟内弃用全部 84 个恶意版本，4 小时 35 分钟内 npm 移除所有恶意包，GitHub 安全公告已发布
- 🛡️ **教训**：缺乏内部告警机制、`pull_request_target`工作流未审计、第三方操作使用浮动引用、npm 取消发布策略导致延迟、OIDC 绑定缺乏发布审查
- ✅ **当前状态**：所有 TanStack 包当前版本安全，Router/Start 仓库已修复，其他仓库未受影响

---

### [为何 React 开发者正从 Next.js 转向 TanStack - YouTube](https://www.youtube.com/watch?v=6moPS3AAbe4)

**原文标题**: [Why React Developers Are Leaving Next.js for TanStack - YouTube](https://www.youtube.com/watch?v=6moPS3AAbe4)

本頁面為 YouTube 平台的綜合資訊頁面，涵蓋了從版權、政策到開發者工具等各項服務說明。
- 📰 新聞中心：提供 YouTube 官方最新消息與公告
- ©️ 版權：說明平台內容的版權規範與管理機制
- 📞 聯絡我們：提供用戶與 YouTube 團隊聯繫的管道
- 🎬 創作者：針對內容創作者提供的資源與支援
- 📢 刊登廣告：說明在 YouTube 上投放廣告的相關資訊
- 👨‍💻 開發人員：提供 API 與開發工具給第三方開發者
- 📜 條款：列出使用 YouTube 服務需遵守的條款與條件
- 🔒 私隱：說明用戶資料的收集、使用與保護方式
- 🛡️ 政策及安全：涵蓋社群規範與安全使用指南
- ⚙️ YouTube 的運作方式：解釋平台推薦系統與內容審核機制
- 🧪 測試新功能：介紹 YouTube 正在測試中的新功能
- ©️ 2026 Google LLC：標示版權歸屬與法律聲明

---

### [获取失败](https://javascriptweekly.com/link/185345/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/185345/web)

无法总结：获取内容失败，状态码 415。

---

### [Orval - 从 OpenAPI 生成类型安全的 API 客户端](https://orval.dev/)

**原文标题**: [Orval - Generate type-safe API clients from OpenAPI](https://orval.dev/)

Orval 可将 OpenAPI 规范自动转换为类型安全的客户端、模拟数据和验证器，省去编写样板代码的繁琐过程，让开发者专注于功能开发。

- 🔄 **从规范到代码**：只需提供 OpenAPI 规范（如 petstore.yaml），即可自动生成类型安全的 TypeScript 代码（如 petstore.ts），包括接口定义和查询钩子。
- 🔒 **端到端类型安全**：根据 OpenAPI 规范生成完整的 TypeScript 类型，消除运行时错误。
- ⚡ **框架原生支持**：为 React Query、Vue Query、Svelte Query、Solid Query、Angular、SWR 等流行框架生成钩子，无需学习新工具。
- 🎭 **自动生成模拟数据**：集成 MSW 和 Faker.js，自动生成模拟处理程序，无需后端即可测试。
- 🛠️ **兼容主流工具**：支持 Axios、Fetch、Zod、Hono、MCP 等，无缝融入现有技术栈。
- ❤️ **社区驱动**：由赞助商和贡献者支持，开源且免费使用。

---

### [GitHub - franciscop/brownies: 🍫 更美味的 cookies、本地存储、会话存储和数据库存储，集成在一个小巧的包中。包含用于监听变化的 subscribe() 事件。](https://github.com/franciscop/brownies)

**原文标题**: [GitHub - franciscop/brownies: 🍫 Tastier cookies, local, session, and db storage in a tiny package. Includes subscribe() events for changes. · GitHub](https://github.com/franciscop/brownies)

Brownies 是一个轻量级的前端存储库，提供统一的 API 来操作 cookies、localStorage、sessionStorage 和异步数据库，并支持订阅存储变化。

- 🍪 **cookies 操作**：通过简单的 getter/setter 接口读写 cookies，自动保留类型（数字、布尔、字符串、数组、对象），删除时返回 `null`。
- 🗄️ **local 和 session 存储**：分别封装 `localStorage` 和 `sessionStorage`，支持类型保留，删除操作简单，可迭代遍历。
- 🔄 **异步 db 存储**：提供异步接口，读取时需使用 `await`，适用于 IndexedDB 等场景。
- 📡 **订阅变化**：使用 `subscribe()` 监听任何对象的属性变化，支持跨标签页同步，可通过返回的 id 或回调函数取消订阅。
- ⚙️ **可配置选项**：支持全局配置 cookies 的过期时间、域名、路径和安全设置。
- 🚀 **快速上手**：支持 npm 安装、CDN 引入或 JSFiddle 在线体验，代码简洁，API 直观。
- 🎯 **迭代支持**：所有存储对象都支持 `Object.keys()`、`Object.values()`、`for...of` 等标准迭代方式。
- 📦 **轻量且功能完整**：仅 2.4k 星，包含 TypeScript 类型定义，适合浏览器端存储需求。

---

### [任意规模下的 Postgres 时间序列工作负载 | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

该内容介绍了 Tiger Cloud（Timescale 旗下产品）提供的 Postgres 时序数据库服务，强调其大规模处理能力、弹性扩展、高可用性及企业级特性。

- 📊 **超大规模处理能力**：支持每日 3 万亿指标、3PB 数据及 1 万亿数据点，展示真实世界规模下的性能。
- 💰 **免费试用与成本优化**：新用户可获 30 天内 1000 美元信用额度，无需信用卡；通过分离计算与存储避免为闲置容量付费。
- 🔄 **弹性扩展与高可用**：支持读写分离（最多 10 个副本节点）、分层 SSD/S3 存储，提供多可用区集群、自动故障转移及跨区域备份。
- 🔒 **企业级安全与合规**：符合 SOC 2、HIPAA、GDPR 标准，具备加密、SSO、RBAC 及审计日志功能。
- 👁️ **深度可观测性**：提供查询钻取和仪表盘，支持将指标发送至 CloudWatch、Datadog、Prometheus 等工具。
- ⚡ **快速部署与集成**：数分钟内完成数据库配置，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🛡️ **企业信任与支持**：提供合同级 SLA、区域数据隔离、合规认证及全球 Postgres 专家 24/7 支持。

---

### [Pica - 浏览器中的高质量图片缩放](https://nodeca.github.io/pica/demo/)

**原文标题**: [Pica - high quality image resize in browser](https://nodeca.github.io/pica/demo/)

该页面是一个用于在浏览器中进行高质量图片缩放的演示工具，名为 Pica demo。它提供了多种缩放选项和优化功能，用户可以通过上传图片并调整参数来实时查看缩放效果。

- 🖼️ 支持在浏览器中直接进行高质量图片缩放
- 🔄 点击缩放后的图片可重新加载，点击原图可上传新图片
- ⚙️ 提供缩放滤镜、窗口大小、USM 锐化（数量、半径、阈值）等参数调节
- 🧠 可选择使用 WebWorker、createImageBitmap 或 WebAssembly 来优化性能
- 📤 支持 canvas 缩放和原图上传功能

---

### [pica/CHANGELOG.md 在 master 分支上 · nodeca/pica · GitHub](https://github.com/nodeca/pica/blob/master/CHANGELOG.md#1000---2026-05-16)

**原文标题**: [pica/CHANGELOG.md at master · nodeca/pica · GitHub](https://github.com/nodeca/pica/blob/master/CHANGELOG.md#1000---2026-05-16)

这是一个图片缩放库 pica 的更新日志摘要，记录了从 v1.0.0 到 v10.0.1 的主要变更。

- 📝 **版本 10.0.1 (2026-05-18)**：新增拆分/浏览器构建的子路径导出，构建时生成 `dist/` 文件，内联 Worker 始终压缩，更新依赖 `glur` 和 `multimath`。
- 🚀 **版本 10.0.0 (2026-05-16)**：重大更新，迁移至 TypeScript 和类，新增拆分构建、ESM 构建、WorkerURL 选项，移除旧浏览器支持，修复 Chrome 中 Exif 方向问题。
- 🛠️ **版本 9.0.1 (2021-12-14)**：修复 ServiceWorker 中的特性检测问题。
- 🔄 **版本 9.0.0 (2021-12-10)**：修复透明图像缩放，移除 `.alpha` 选项，提高卷积传递间的数据精度。
- ⚙️ **版本 8.0.0 (2021-11-22)**：用 `.filter` 替换 `.quality`，新增默认 `mks2013` 滤镜。
- 🐛 **版本 7.1.1 (2021-11-22)**：强制 WebWorker 始终返回类型化数组，避免 Chrome 伪影。
- 🔧 **版本 7.1.0 (2021-06-21)**：修复 Firefox 指纹模式下的错误，以及 Chromium 中 Exif 方向问题。
- 💥 **版本 7.0.0 (2021-05-23)**：破坏性变更，重写 USM 锐化（使用 HSV 的 V 通道），调整锐化参数，支持 OffscreenCanvas。
- 🧩 **版本 6.1.1 (2020-08-20)**：添加 Safari Canvas 垃圾回收工作区。
- 🌐 **版本 6.1.0 (2020-07-10)**：添加 OffscreenCanvas 支持。
- 📦 **版本 6.0.0 (2020-06-25)**：使用 `dist/pica.js` 作为主入口，添加 `ImageBitmap` 输入支持。
- 🧪 **版本 5.0.0 (2018-11-02)**：维护更新，升级 Babelify 到 @babel/core。
- 🔬 **版本 4.0.0 (2017-09-30)**：内部重写为使用 `multimath`，新增 WebAssembly 实现的 USM 锐化。
- 🎉 **版本 3.0.0 (2017-04-11)**：重大重写，基于 Promise 的新 API，新增 WebAssembly 和 createImageBitmap() 缩放器，移除 WebGL 缩放器。
- 🖼️ **版本 2.0.0 (2016-03-12)**：架构重写，图像分块处理，内置 WebWorker 管理器，支持多核 CPU。
- 🏁 **版本 1.0.0 (2014-09-24)**：首次发布。

---

### [GitHub - nodeca/pica: 在浏览器中高质量、高速调整图片大小 · GitHub](https://github.com/nodeca/pica)

**原文标题**: [GitHub - nodeca/pica: Resize image in browser with high quality and high speed · GitHub](https://github.com/nodeca/pica)

Pica 是一个高性能浏览器端图像缩放库，支持 WebWorker、WebAssembly 等多种技术，提供高质量缩放效果。

- 🖼️ **高质量缩放**：自动选择最佳技术（WebWorker、WebAssembly、createImageBitmap、纯 JS），实现无像素化缩放。
- ⚙️ **核心功能**：支持 Canvas/Image 缩放、转 Blob、原始 RGBA 缓冲区处理，并提供 Unsharp Mask 锐化滤镜。
- 📦 **安装与使用**：通过 npm 安装，支持 ESM 和 CommonJS，提供工厂函数和类两种调用方式。
- 🧩 **可配置选项**：支持 tile 分块处理、并发控制、缓存超时、自定义 worker URL 等参数。
- 🚫 **注意事项**：受 JS 安全限制，仅处理同源或本地文件；iOS 有 Canvas 内存限制；不支持伽马校正，专业级图像可能精度不足。
- 🖥️ **浏览器兼容**：主流浏览器均支持，Node.js 环境需额外配置 OffscreenCanvas，但推荐使用 sharp 库。
- 🔄 **迁移指南**：v9 到 v10 需注意默认导出改为工厂函数，移除 createCanvas 选项，quality 参数改用 filter 对象。

---

### [SVAR 发布适用于 React、Svelte 和 Vue 的日历组件 | SVAR 博客](https://svar.dev/blog/svar-calendar-for-react-svelte-vue/)

**原文标题**: [SVAR Releases Calendar Component for React, Svelte & Vue | SVAR Blog](https://svar.dev/blog/svar-calendar-for-react-svelte-vue/)

SVAR Calendar 是一个免费、开源的日历组件，原生支持 Svelte、React 和 Vue，核心功能基于 MIT 许可，PRO 版额外提供年、资源、时间线、议程视图和重复事件。

- 📅 **核心功能**：免费版包含日、周、月视图，支持拖拽创建/编辑事件、事件编辑器、右键菜单、日历分组、筛选、iCal 导入/导出、主题定制和本地化。
- 🔧 **框架原生**：为 Svelte、React 和 Vue 分别编写原生版本，拥有统一 API 和 TypeScript 支持，可通过 npm 安装。
- 🌐 **后端集成**：提供 RestDataProvider 轻松连接 REST API，自动同步事件 CRUD 操作。
- 💼 **PRO 版特性**：增加年视图、议程视图、资源视图、时间线视图和重复事件，适合更复杂的调度场景。
- 🚀 **上手简单**：提供快速入门指南、在线演示和 GitHub 开源代码，免费版即可满足多数需求。

---

### [Svelte 小部件](https://svar.dev/demos/calendar/)

**原文标题**: [Svelte Widgets](https://svar.dev/demos/calendar/)

本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了其在诊断、药物研发和个性化治疗中的优势与挑战。

- 🩺 人工智能在医学影像分析中表现出色，能辅助医生更准确地检测疾病，如癌症和视网膜病变。
- 💊 通过加速药物筛选和分子模拟，AI 显著缩短了新药研发周期，降低了成本。
- 🧬 基于患者基因和病史数据，AI 可制定个性化治疗方案，提升疗效并减少副作用。
- ⚠️ 数据隐私、算法偏见和监管缺失是当前 AI 医疗应用面临的主要挑战。
- 🔮 未来，AI 有望与可穿戴设备结合，实现实时健康监测和早期预警。

---

### [现代 JavaScript 事件日历](https://schedule-x.dev/)

**原文标题**: [Modern JavaScript Event Calendar](https://schedule-x.dev/)

Schedule-X 是一个现代化的 JavaScript 事件日历工具，提供免费和高级版本，支持多种框架和自定义功能，旨在简化日历集成。

- 📅 概述：Schedule-X 是一个现代 JavaScript 事件日历，可作为 FullCalendar 的替代品，易于集成且支持多种技术栈。
- ⭐ 核心功能：支持拖放、事件调整大小、暗黑模式、多语言（i18n）和响应式设计，适用于各种设备。
- 🚀 高级插件：提供拖放创建、事件模态框、资源调度器、时间网格视图等高级功能，提升日历体验。
- 💻 框架支持：兼容 React、Vue、Angular、Svelte 和 Preact 等流行前端框架。
- 🏆 高级版优势：Schedule-X Premium 提供一站式解决方案，节省开发时间（如构建事件模态框需约 100 小时，而高级版仅需 1 小时）。
- 🔗 全栈方案：集成 BuildCalendar 可实现数据库持久化、Google 日历同步等后端功能。
- 👥 用户评价：开发者称赞其灵活性、易用性和出色的客户支持。

---

### [schedule-x/CHANGELOG.md 在 main 分支 · schedule-x/schedule-x · GitHub](https://github.com/schedule-x/schedule-x/blob/main/CHANGELOG.md#460-2026-05-12)

**原文标题**: [schedule-x/CHANGELOG.md at main · schedule-x/schedule-x · GitHub](https://github.com/schedule-x/schedule-x/blob/main/CHANGELOG.md#460-2026-05-12)

概述总结
- 📅 Schedule-X 是一个日程管理相关的开源项目，拥有 2.3k 星标和 174 个复刻，社区活跃。
- 📂 项目包含代码、问题、拉取请求等多个功能模块，便于协作开发。
- 🔄 主要分支为 main，包含 CHANGELOG.md 文件，记录版本更新历史。
- 📄 CHANGELOG.md 文件较大，包含 1428 行代码和 102KB 内容，详细记录了项目变更。
- 🔧 项目提供代码浏览、编辑、原始文件下载等操作功能，方便开发者使用。

---

### [命运 1.0 | 命运](https://fate.technology/posts/fate-1.0)

**原文标题**: [fate 1.0 | fate](https://fate.technology/posts/fate-1.0)

fate 1.0 正式发布，这是一个专为 Async React 设计的数据框架，通过视图组合、归一化缓存和实时订阅等特性，简化了 React 应用的数据获取和管理。

- 📢 **fate 1.0 正式发布**：结合视图组合、归一化缓存、数据掩码和 Async React 特性，提供生产级数据框架。
- 🎯 **核心设计理念**：以归一化对象缓存替代请求缓存，将视图需求组合为单一请求，减少命令式缓存管理。
- 🔄 **实时视图与列表**：新增 `useLiveView` 和 `useLiveListView` 钩子，通过 SSE 实现零配置实时更新。
- 🗄️ **Drizzle 与原生 HTTP 支持**：扩展数据库集成，新增 Drizzle 支持，并提供不依赖 tRPC 的原生 HTTP 传输。
- ⚡ **Vite 插件替代代码生成**：自动处理类型同步，减少手动代码生成步骤，提升开发效率。
- 🧹 **缓存生命周期与垃圾回收**：基于 Relay 灵感，自动管理客户端缓存，保留最近 10 次请求数据以优化导航体验。
- 🐛 **多项修复与优化**：改进乐观更新排序、请求生命周期管理、列表缓存作用域，提升大型列表性能。
- 🚀 **快速启动脚手架**：通过 `create-fate` 工具，支持 Drizzle、Prisma 等模板，快速搭建项目。
- 🌐 **与 Void 路由器集成**：与 VoidZero 的 Async React 路由器结合，构建首个专为 Async React 设计的元框架。

---

### [GitHub - stackblitz/alien-signals: 👾 最轻量的信号库 · GitHub](https://github.com/stackblitz/alien-signals)

**原文标题**: [GitHub - stackblitz/alien-signals: 👾 The lightest signal library · GitHub](https://github.com/stackblitz/alien-signals)

alien-signals 是一个基于推送 - 拉取信号算法的轻量级响应式系统库，由 StackBlitz 团队开发，其核心算法已被移植到 Vue 3.6 等多个项目中，并提供了丰富的多语言实现和衍生项目。

- 👾 核心算法采用推送 - 拉取信号模型，结合 Vue 3、Preact 双链表、Svelte 调度和 Reactively 图着色等技术的优点，在保持简单性的同时提升性能。
- 📦 提供 `signal`、`computed`、`effect` 等基础 API，支持响应式状态、计算值和副作用，代码简洁易用。
- 🔄 支持 `effectScope` 作用域管理，可批量停止副作用，以及嵌套 effect 的自动清理与重建，确保执行顺序正确。
- ⚡ 提供 `trigger()` 函数用于手动触发更新，适合直接修改信号值后同步下游依赖，支持单信号或多信号批量触发。
- 🛠️ 通过 `createReactiveSystem()` 允许用户自定义表面 API，灵活性高，可适配不同框架需求。
- 🌍 已移植到 Dart、Lua、Java、C#、Go、Rust 等多种语言，并有 React 绑定、深信号、状态共享等衍生项目。
- 📊 在 js-reactivity-benchmark 基准测试中表现优异，核心算法已被 Vue 3.6 和 XState 等项目采纳。
- 📚 提供清晰的文档和示例，包括递归版 `propagate` 和 `checkDirty` 函数作为参考，便于理解底层机制。

---

### [GitHub - addyosmani/critical: 提取并内联 HTML 页面中的关键路径 CSS · GitHub](https://github.com/addyosmani/critical)

**原文标题**: [GitHub - addyosmani/critical: Extract & Inline Critical-path CSS in HTML pages · GitHub](https://github.com/addyosmani/critical)

Critical 是一个用于提取和内联网页关键路径 CSS 的开源工具，可优化页面加载性能。

- 📦 通过 `pnpm add -D critical` 安装，支持 Gulp、Webpack 等构建工具
- ⚙️ 核心功能：自动提取首屏 CSS 并内联到 HTML，减少关键渲染路径的往返次数
- 🖥️ 支持多种使用方式：CLI 命令行、Node.js 回调/Promise/async 函数
- 📐 可配置视口尺寸（默认 1300x900），支持多分辨率自适应生成
- 🎯 提供丰富的选项：CSS 提取、图片内联、资源路径重写、忽略特定规则等
- 🚀 与 Penthouse 不同，Critical 能自动从 HTML 中提取样式表，并集成了内联功能
- 🔧 支持忽略 `@font-face` 等规则，以及通过正则或函数过滤声明
- 📁 可输出关键 CSS 文件、修改后的 HTML 文件及非关键 CSS 文件
- 💻 CLI 示例：`cat index.html | critical --base test/fixture --inline > output.html`
- 🌟 已在多个生产环境验证稳定性，欢迎贡献代码和报告问题

---

### [GitHub - sql-formatter-org/sql-formatter: 适用于多种查询语言的空白格式化工具 · GitHub](https://github.com/sql-formatter-org/sql-formatter)

**原文标题**: [GitHub - sql-formatter-org/sql-formatter: A whitespace formatter for different query languages · GitHub](https://github.com/sql-formatter-org/sql-formatter)

SQL Formatter 是一个用于美化 SQL 查询语句的 JavaScript 库，支持多种 SQL 方言，并可通过命令行或代码库方式使用。

- 📚 **支持多种 SQL 方言**：包括 BigQuery、MySQL、PostgreSQL、Spark 等 20 多种数据库语言。
- 🛠️ **灵活的使用方式**：可作为 JavaScript 库导入使用，也可通过命令行工具 `sql-formatter` 处理 SQL 文件。
- ⚙️ **丰富的配置选项**：支持设置缩进、关键字大小写、查询间距、参数替换等自定义格式。
- 🚫 **支持禁用格式化**：通过 `/* sql-formatter-disable */` 注释可跳过特定 SQL 段落的格式化。
- 💻 **编辑器集成**：提供 VSCode、Vim 扩展及 Prettier 插件，并支持 JSON Schema 配置自动补全。
- 🐛 **常见问题处理**：提供方言选择、参数占位符处理、模板语法兼容等解决方案。
- 🔄 **未来方向**：项目处于维护模式，推荐新工具 `prettier-plugin-sql-cst` 以获得更先进的格式化能力。

---

### [SQL 格式化工具](https://sql-formatter-org.github.io/sql-formatter/)

**原文标题**: [SQL Formatter](https://sql-formatter-org.github.io/sql-formatter/)

该文本介绍了 SQL 格式化工具的配置选项，包括数据库类型、大小写设置、缩进风格等参数。

- 🗄️ 支持多种数据库：AWS Redshift、BigQuery、Clickhouse、DB2、DuckDB、Hive、MariaDB、MySQL、TiDB、N1QL、PL/SQL、PostgreSQL、SingleStoreDB、Snowflake、Spark、SQLite、Transact-SQL、Trino
- 🔤 关键词大小写可选：保留原样、全部大写或全部小写
- 🔡 数据类型大小写可选：保留原样、全部大写或全部小写
- 🔧 函数名大小写可选：保留原样、全部大写或全部小写
- 🆔 标识符大小写可选：保留原样、全部大写或全部小写
- 📐 缩进风格可选：标准、左对齐表格、右对齐表格
- 🔗 AND/OR换行位置可选：在运算符前或后
- 📏 表达式宽度可自定义
- 📄 查询间空行数可设置
- ➕ 分号可单独成行
- 💻 示例 SQL 查询：包含表连接、WHERE 条件、ORDER BY 排序的复杂查询

---

### [四季](https://shiki.style/)

**原文标题**: [Shiki](https://shiki.style/)

概述总结：该文本强调了基于 TextMate 语法的精准与美观特性，与 VS Code 同源并随其持续优化。

- 🌈 采用与 VS Code 相同的 TextMate 语法引擎，确保语法高亮精准无误
- ✨ 追求输出内容的视觉美感，兼顾准确性与优雅呈现
- 🔄 与 VS Code 同步演进，每次更新都能提升表现力与兼容性

---

### [发布 v2.12.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.12.0)

**原文标题**: [Release v2.12.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.12.0)

Redux Toolkit v2.12.0 发布，新增技能文件、TS 改进和错误修复。

- 🚀 新增 RTK 使用技能文件（基于 TanStack Intent），涵盖现代 RTK 使用、状态管理和副作用处理。
- 📦 导出 RTK Query 钩子选项类型，方便开发者复用，无需再用`Parameters`提取。
- 🛠️ 修复无限查询中`isSuccess`状态标志的切换问题，避免 UI 闪烁。
- ⏱️ 为`autoBatch`增强器添加 100ms 超时回退，解决后台标签页中`requestAnimationFrame`不工作的问题。
- 🧩 改进 TypeScript 支持：允许接口类型守卫、重命名`IgnorePaths`为`IgnoredPaths`、使用内置`NoInfer`工具。
- 👥 感谢贡献者 phryneas、veeceey、riqts、Ri5ha6h 和 aryaemami59 的贡献。

---

### [发布 v9.3.0 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/releases/tag/v9.3.0)

**原文标题**: [Release v9.3.0 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/releases/tag/v9.3.0)

React-Redux v9.3.0 发布，正式将 `connect` API 标记为弃用，并修复了受信发布问题。

- 🔔 `connect` API 正式标记为弃用，但行为不变，不会被移除
- 🎯 鼓励用户迁移到 `useSelector / useDispatch` 钩子，以简化代码并提升性能
- 🔄 提供 `legacy_connect` 别名，无弃用标记，供需要继续使用的用户选择
- 🛠️ 修复了受信发布（Trusted Publishing）的配置问题，确保发布流程正确
- 📅 这是继 2022 年弃用 `createStore` 后的又一重要弃用步骤，强调现代 Redux Toolkit 的推荐使用

---

### [发布 v3.3.0 · vuejs/language-tools · GitHub](https://github.com/vuejs/language-tools/releases/tag/v3.3.0)

**原文标题**: [Release v3.3.0 · vuejs/language-tools · GitHub](https://github.com/vuejs/language-tools/releases/tag/v3.3.0)

Vue.js 语言工具发布了 v3.3.0 版本，主要改进了组件属性的自动补全功能，并新增了检查必需透传属性的选项，同时修复了项目引用和诊断循环的 bug。

- 🚀 **优化组件属性自动补全**：现在能根据动态类型（如泛型或联合类型）准确推断可用属性，例如在 `type: "foo"` 时只提示 `foo` 属性。
- 🔍 **新增检查必需透传属性选项**：启用 `checkRequiredFallthroughAttributes` 后，组件会精确继承基础组件的必需属性，并消除缺失属性错误。
- 🐛 **修复项目引用错误**：在子项目中跨项目导入 Vue 文件不再触发 TS6307 错误。
- 🔄 **修复诊断无限循环**：启用 `enableProjectDiagnostics` 选项后，大型项目中的 Vue 文件不再引发无限诊断循环。
- 📜 **详细更新日志**：请参阅 CHANGELOG.md 获取完整变更记录。
- ❤️ **感谢赞助商**：项目得益于 Next Generation Tooling、Platinum、Gold 和 Silver 赞助商的支持。

---

### [HyperFormula — 将 Excel 公式引入您的应用](https://hyperformula.handsontable.com)

**原文标题**: [HyperFormula — Bring Excel Formulas to Your App](https://hyperformula.handsontable.com)

本内容介绍了 HyperFormula，一个将 Excel 公式逻辑集成到现代应用中的高性能 TypeScript 计算引擎。

- 🚀 **核心功能**：将 Excel 公式以确定性、可重复的结果高速运行在应用中，桥接电子表格与现代软件的差距。
- 💼 **应用场景**：为 CRM、ERP 等商业软件提供自定义计算字段，让用户用熟悉的 Excel 语法定义动态规则。
- 🧩 **灵活集成**：无头设计，分离计算与 UI，支持前端框架和后端系统，开发者可完全控制界面。
- ⚡ **生产就绪**：确定性结果、高性能、支持真实数据集，兼容浏览器和服务器环境。
- 📚 **丰富函数库**：内置约 400 个 Excel 兼容函数，涵盖数学、逻辑、查找、统计等主要类别。
- 🛠️ **多样用例**：模拟 Excel 行为、服务端/客户端计算、AI 数学引擎、电子表格应用等。
- 💰 **可预测定价**：按终端用户分层，从小型企业（$1,490/年起）到企业级定制，含商业许可与支持。
- 🆓 **免费许可**：开源项目和教育评估免费（GPL v3），提供 GitHub、文档和演示资源。

---

### [细致 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified)

Meticulous 是一款零开发工作量的自动化测试工具，通过录制用户交互、AI 生成测试套件和模拟后端响应，实现无 flake、快速迭代的回归测试，已被 Dropbox、Notion 等 100 多家组织采用。

- 🚀 **零开发工作量**：只需添加脚本标签，即可自动录制开发环境中的用户交互，无需编写或维护测试代码。
- 🤖 **AI 驱动的测试套件**：AI 引擎根据代码分支覆盖情况，持续生成覆盖所有用户流程和边缘案例的视觉端到端测试。
- 🔄 **自动进化测试**：测试套件随应用演变自动更新，新增功能时添加测试，过时时移除，确保始终完整且最新。
- ✅ **无 flake 确定性执行**：基于 Chromium 构建的确定性调度引擎，从底层消除测试不稳定因素，实现闪电般快速执行。
- ⚡ **高效 CI 集成**：通过模拟后端响应，无需特殊测试账号或模拟数据，即可在 PR 合并前预览变更影响，测试结果在 120 秒内返回。
- 🛡️ **广泛框架支持**：兼容 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流框架，可补充或替代现有测试套件。
- 🏢 **企业级信任**：被 Dropbox、Notion 等 100 多家组织采用，开发者反馈“无法想象没有它工作”。

---

### [错误](https://javascriptweekly.com/link/185367/web)

**原文标题**: [Error](https://javascriptweekly.com/link/185367/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='agentfield.ai', port=443): Max retries exceeded with url: /github/?utm_source=javascript&utm_medium=referral&utm_campaign=javascript-060519&utm_id=javascript-060519-github-cta&utm_content=github-cta (Caused by SSLError(SSLCertVerificationError(1, "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'agentfield.ai'. (_ssl.c:1010)")))

---

### [JSONRegistry - 允许在常规 JSON 中使用品牌实例 - 💡 想法 - TC39](https://es.discourse.group/t/jsonregistry-allows-branded-instances-in-regular-json/2569)

**原文标题**: [JSONRegistry - Allows branded instances in regular JSON - 💡 Ideas - TC39](https://es.discourse.group/t/jsonregistry-allows-branded-instances-in-regular-json/2569)

### 概述摘要
TC39 社群提出 JSONRegistry 提案，旨在扩展 JSON 功能，允许开发者注册自定义类型（如 Uint8Array、Date 等），实现序列化与反序列化时保留类型信息，同时保持与原生 JSON 的兼容性。提案通过注册表机制，在 `stringify` 和 `parse` 过程中自动转换类型，解决现有 JSON 无法处理复杂类型的问题。讨论中涉及技术实现细节、与现有 JSON 的兼容性争议，以及向结构化克隆扩展的可能性。

- 💡 **核心提案**：JSONRegistry 允许开发者注册自定义类型（如 Uint8Array、BigInt），通过 `is`、`to`、`from` 方法实现双向转换，保持 JSON API 透明。
- ⚙️ **工作原理**：`stringify` 将类型实例转换为 `[数据, "类型名"]` 格式，`parse` 通过数组末尾标记（0 或类型名）恢复原始类型，避免污染标准 JSON。
- 🔄 **兼容性**：提案强调不改变 JSON 语法，但批评者指出其实际扩展了语言语义，可能导致与现有 JSON 解析器冲突。
- 🚫 **争议焦点**：部分成员认为该提案本质是语言扩展，会破坏 JSON 的确定性，建议采用显式语法（如 `Type { ... }`）而非隐式数组标记。
- 🌐 **跨语言潜力**：提案旨在解决 JS 中自定义类型序列化难题，类似 Python 的 pickle，但需平衡与 JSON 生态的兼容性。
- 🛠️ **技术细节**：`v0.2.0` 改用对象包裹而非数组污染，支持 `Date` 等类型通过注册 `toJSON` 为 `undefined` 的子类处理。
- 🧩 **扩展方向**：讨论转向 `StructuredCloneRegistry` 提案，利用结构化克隆的隐式处理机制，避免破坏 JSON 兼容性，同时支持自定义类型。

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

概述摘要  
Wasp 是一个为 AI 时代设计的全栈框架，类似 Rails，基于 React、Node.js 和 Prisma，可快速开发并一键部署应用，支持认证、RPC、任务调度、邮件发送等功能，完全开源且类型安全。

- 🚀 **快速开发**：通过单一配置文件（.wasp）和 CLI 命令，一天内构建并部署全栈应用。
- 🔒 **全栈认证**：几行代码集成社交登录或邮箱认证，无第三方供应商锁定。
- 🔗 **RPC 层**：类型安全的客户端 - 服务器通信，自动将数据模型和逻辑暴露给前端。
- 📦 **简单部署**：支持多平台，CLI 提供常用部署选项。
- ⏰ **任务调度**：定义持久化、可重试、可延迟的服务器任务。
- 📧 **邮件发送**：连接邮件提供商后即可发送邮件。
- 🛡️ **全栈类型安全**：TypeScript 支持，自动生成跨栈类型。
- 🌟 **更多功能**：自定义 API 路由、数据库种子、乐观更新、客户端缓存失效等。
- 🧠 **工作原理**：通过配置文件描述应用，Wasp 编译器生成完整前端、后端和部署代码。
- 💬 **社区好评**：用户称赞其简化开发流程，适合快速构建全栈应用。
- 🏆 **展示案例**：包括招聘平台、内部工具、法律工作流管理等实际项目。
- 📬 **更新订阅**：可订阅获取新功能通知。
- 🗺️ **路线图**：持续开发中，可预览未来计划。
- ❓ **常见问题**：对比 Next.js、Ruby on Rails 等框架，学习难度低，当前仅支持 React 和 Node.js。

---

### [5 年与 500 万美元之后：为网页开发创造一门新编程语言是个错误 | Wasp](https://wasp.sh/blog/2026/05/13/new-language-for-web-dev-was-a-mistake)

**原文标题**: [5 Years and $5M Later: Inventing a New Programming Language for Web Development Was a Mistake | Wasp](https://wasp.sh/blog/2026/05/13/new-language-for-web-dev-was-a-mistake)

Wasp 团队在投入 5 年时间和 500 万美元后，决定放弃自创的编程语言，改用 TypeScript 作为全栈框架的配置语言。

- 🚫 自创语言是错误方向：虽然团队最初认为需要新语言来实现"通用框架"愿景，但这反而成为最大的阻碍
- 🤔 开发者抵触新语言："lang"后缀让开发者误以为要取代 JavaScript，导致他们不愿尝试
- 💻 IDE 支持困难重重：为自定义语言开发编辑器工具耗费巨大精力，却只能达到 80% 的预期效果
- 🔑 核心价值不在语言：Wasp 的真正优势是编译时对全栈应用的高层理解，而非自定义语法
- 📈 用户认可但不愿入门：尝试过的开发者都很喜欢 Wasp，但"新语言"的标签让很多人望而却步
- 🎯 改用 TypeScript 解决所有问题：TypeScript SDK 获得积极反馈，编辑器支持、条件逻辑、多文件拆分等问题迎刃而解
- 🧩 DSL 曾是必要起点：自定义语言帮助团队保持"规范与实现分离"的初心，为后续发展奠定基础
- 🤖 AI 时代的新机遇：Wasp 的全栈结构让 AI 生成代码更可控，成为"最适合 AI 的 JS 框架"

---

### [浏览器对大网站区别对待——丹·奥德尔](https://denodell.com/blog/browsers-treat-big-sites-differently)

**原文标题**: [
      Browsers Treat Big Sites Differently — Den Odell
    ](https://denodell.com/blog/browsers-treat-big-sites-differently)

### 概述总结
不同浏览器会针对特定网站修改渲染行为，Safari 和 Firefox 通过内置的"quirks"或干预代码修复网站兼容性问题，而 Chrome 因市场主导地位无需此类调整，这反映了浏览器生态的失衡。

- 🕵️ Safari 和 Firefox 的代码中直接包含域名检查，针对 TikTok、Netflix、SeatGuru 等网站提供特殊渲染或 API 处理
- 🔧 Firefox 的`about:compat`页面列出可开关的网站特定干预措施，包括注入 CSS/JS 和修改用户代理字符串
- 🐞 Safari 的 Quirks.cpp 文件公开记录针对 Facebook、X、Reddit 等网站的修复，例如处理 PiP 视频的异常行为
- 📉 浏览器厂商优先选择快速修复而非等待网站更新，因为用户会因网站故障而责怪浏览器
- 🏆 Chrome 无需此类修复，因为开发者优先为其优化，Chrome 的默认行为已成为事实标准
- 🔄 这形成反馈循环：开发者只测试 Chrome，导致其他浏览器被迫添加更多兼容性补丁
- 🚫 用户代理欺骗常见，Safari 和 Firefox 会伪装成 Chrome 以绕过网站对非 Chrome 浏览器的封锁
- 📋 干预范围广泛，包括滚动、触摸事件、视口计算、图片 MIME 类型等基础行为修改
- ⚠️ 如果你的网站主要测试 Chrome，可能正依赖其他浏览器的隐形修复，建议定期在 Safari 和 Firefox 中测试

---

### [获取失败](https://javascriptweekly.com/link/185372/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/185372/web)

无法总结：获取内容失败，状态码 403。

---

### [五分钟了解 LLM 过去六个月的发展](https://simonwillison.net/2026/May/19/5-minute-llms/)

**原文标题**: [The last six months in LLMs in five minutes](https://simonwillison.net/2026/May/19/5-minute-llms/)

以下是对过去六个月 LLM 发展的总结：

2025 年 11 月是 LLM 发展的关键转折点，编码代理变得实用，同时本地可运行模型性能大幅提升。

- 🐦 2025 年 11 月成为“转折点”，最佳模型在五大提供商间易手五次，编码代理从“偶尔可用”变为“日常可用”
- 🎨 用“鹈鹕骑自行车”测试模型能力，Claude Sonnet 4.5、GPT-5.1、Gemini 3 等模型表现各异，Gemini 3 画得最好
- 🚀 11 月 OpenAI 和 Anthropic 通过强化学习提升代码质量，编码代理跨越质量门槛，成为日常开发工具
- 🐍 作者在假期用 vibe-coding 实现了 JavaScript 的 Python 版本（micro-javascript），但承认其实际价值有限
- 🦾 2 月 OpenClaw（原 Warelay）项目崛起，成为“个人 AI 助手”类工具的代表，被称为“Claws”
- 💻 Mac Mini 因运行 Claws 而热销，被比喻为“数字宠物的完美水族箱”
- 🎥 2 月 Gemini 3.1 Pro 画出极好的鹈鹕骑自行车图，Google 的 Jeff Dean 还展示了动画版本
- 🏆 4 月 Google 发布 Gemma 4 系列，是来自美国公司的最强开源权重模型
- 🇨🇳 中国 AI 实验室 GLM 发布 GLM-5.1（1.5TB 参数），能画出合格鹈鹕但动画效果欠佳
- 🦝 Qwen3.6-35B-A3B 在笔记本上画出比 Claude Opus 4.7 更好的鹈鹕，证明本地模型性能超预期
- 📉 鹈鹕骑自行车测试已失去作为基准的价值，因为模型表现已远超该任务需求

---

