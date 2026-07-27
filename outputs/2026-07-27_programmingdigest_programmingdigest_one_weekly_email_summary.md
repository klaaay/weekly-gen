### [深度优先搜索模式：探索树与图](https://newsletter.francofernando.com/p/the-depth-first-search-pattern-exploring)

**原文标题**: [The Depth-First Search Pattern: Exploring Trees and Graphs](https://newsletter.francofernando.com/p/the-depth-first-search-pattern-exploring)

深度优先搜索（DFS）是一种递归遍历树和图的模式，核心是尽可能深入探索路径，遇到死胡同时回溯。它适用于寻找路径、检查可达性、探索所有路径，以及处理树、图或矩阵等隐式图结构。文章详细介绍了 DFS 的基本实现、在树和图上的变体、处理循环、寻找所有路径以及在矩阵中的应用，并总结了何时使用 DFS。

- 🌳 核心模式：从根节点出发，递归访问子节点，遇空或目标后回溯；时间复杂度 O(n)，空间复杂度 O(n)（取决于树形态）
- 🔍 寻找路径：在树中从根到目标构建路径常用“回溯时组装”方法；每个节点将自己加入路径前端
- 🔄 处理循环：图可能包含循环，需使用 visited 集合记录已访问节点，避免无限递归；时间复杂度 O(V+E)
- 🛤️ 寻找所有路径：在寻找所有路径时，需在递归后从 visited 和路径中移除当前节点（回溯），允许其他路径重复使用节点
- 🧩 矩阵作为隐式图：矩阵单元格为节点，相邻单元为边；无需显式图转换，只需定义邻居和边界；仅向右/下移动时无需 visited
- 💡 适用场景：需要找路径、检查连通性、探索所有可能、处理树/图/矩阵/游戏状态等；经典问题包括连通分量、环检测、迷宫等
- ⚖️ 与 BFS 对比：DFS 递归实现简单，适合深窄结构；BFS 更适合无权图的最短路径

---

### [](https://www.jolli.ai/memory?utm_source=newsletter&utm_medium=post&utm_campaign=pd-nw-lp-1&utm_term=jolli+memory)

**原文标题**: [Jolli Memory – Knowledge that remembers your code and context](https://www.jolli.ai/memory?utm_source=newsletter&utm_medium=post&utm_campaign=pd-nw-lp-1&utm_term=jolli+memory)

Jolli Memory 是一款持久化记忆工具，能在 AI 编码会话间保留每次提交背后的推理与上下文，避免重复解释，帮助开发者和团队更快交付、更少调试。它通过自动捕获提交时的“为什么”，实现跨代理、跨仓库的上下文复用，显著降低 token 消耗并提升代理效率，同时支持本地运行与团队云同步。

- 💾 自动捕获 AI 编码决策的推理、备选方案和上下文，取代静态文档，确保记忆随提交更新。
- 🔍 通过“捕获 → 复用 → 管理”三步，将每次变更的结构化记忆存入分支级知识库，供代理随时查询。
- ⚡ 减少 50% token 消耗，代理响应速度翻倍，无需重复读取整个仓库。
- 🔧 兼容 Claude Code、Cursor、GitHub Copilot CLI 等主流代理，以及 GitHub、GitLab 等代码平台，无厂商锁定。
- 👤 个人开发者可瞬间恢复会话、加速 PR 评审和调试；团队管理者可监控 token 成本、识别最佳工作流程。
- 🏠 默认本地运行，隐私安全；可选择同步至云端，与团队共享空间、Wiki 和报告。
- 🚀 安装简单：macOS/Linux 终端运行 `curl -fsSL https://jolli.ai/install.sh | sh`。

---

### [每个人都应该了解 SIMD – Mitchell Hashimoto](https://mitchellh.com/writing/everyone-should-know-simd)

**原文标题**: [Everyone Should Know SIMD – Mitchell Hashimoto](https://mitchellh.com/writing/everyone-should-know-simd)

SIMD（单指令多数据）并非遥不可及的高级技术，日常编程中常见的“一次处理多个值”模式有固定套路。学会基础后，写出 SIMD 代码就像编写普通循环一样简单。每个开发者都应了解并敢于使用它。

- 📖 SIMD 并非高不可攀：它让 CPU 并行处理多个数据，常见于遍历数组、字符串等循环场景。
- 🔄 常见五步模式：①广播常量；②每次处理一个向量宽度；③并行执行 SIMD 操作；④归约向量结果；⑤处理标量尾部。
- 💡 实际案例（Ghostty 终端）：用 SIMD 在已解码码点中快速查找 C0 控制字符，代码仅增加 12 行。
- ⚡ 性能提升：ARM NEON 可达 4x，AVX2 可达 8x，AVX-512 可达 16x；实际端到端吞吐提升约 5x。
- 🔧 步骤详解：用@Vector 定义类型、@splat 广播阈值、加载完整向量、用>并行比较、@reduce/.And 检测全通过、@bitCast 转位掩码再用@ctz 定位失败索引，最后用原循环处理剩余元素。
- ❓ 编译器自动向量化不可靠：虽有时能优化简单循环，但手动 SIMD 更显式、可预测，避免因代码变更或编译器升级退化。
- 💪 每个人都应了解：不要害怕 SIMD；识别热点扫描/比较/计数/变换大批连续数据的机会，就能套用这一固定模式。

---

### [htop 说明 | peteris.rocks](https://peteris.rocks/blog/htop/)

**原文标题**: [htop explained | peteris.rocks
    ](https://peteris.rocks/blog/htop/)

这是一个对 htop 指令的详细解读，涵盖了系统开机时间、负载、进程状态、内存使用等关键信息，并深入解释了每个字段的含义和背后原理。

- 📈 **系统运行时间**：通过读取 `/proc/uptime` 获取总秒数和空闲秒数，htop 显示友好的格式。
- ⏱️ **负载平均值**：来自 `/proc/loadavg`，表示最近 1、5、15 分钟的平均系统负载（运行中 + 不可中断进程数），不是简单的 CPU 使用率。
- 🔄 **进程状态**：R（运行或可运行）、S（可中断睡眠）、D（不可中断睡眠，通常 IO）、Z（僵尸进程）、T（停止）、t（被调试器跟踪）。
- 🌲 **进程树**：进程有父子关系，形成树结构，可通过 htop 的 F5 或 `pstree` 查看。
- 👤 **进程用户**：每个进程由用户拥有，通过 `/proc/<pid>/status` 查看 UID，依赖 `/etc/passwd` 等文件解析用户名。
- ⚙️ **进程优先级与 Nice 值**：Nice 值范围 -20~19，数值越小优先级越高；Priority（PR）为 20+NI，内核使用不同范围。
- 💾 **内存使用**：VIRT 为虚拟内存（含映射文件），RES 为常驻物理内存，SHR 为可共享内存，MEM% = RES / 总内存 × 100%。
- 🛠️ **常见系统进程解说**：详细介绍了 init、systemd-journald、udevd、timesyncd、cron、sshd 等进程的作用与是否可移除。
- 📎 **附录与实用技巧**：包括源代码查找、strace 使用、文件描述符重定向记忆法、PuTTY 颜色设置，以及一个简易 shell 的 C 语言实现。

---

### [](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c?gi=f63c2dc39c70)

**原文标题**: [Medium](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c?gi=f63c2dc39c70)

Netflix 通过自建 LLM 服务栈，将模型部署、推理等环节整合到现有的生产环境中，而非依赖外部托管 API。本文详细阐述了引擎选型、模型打包、API 设计、部署策略和输出约束等关键决策与生产实践中的经验教训。

- 🏗️ **架构统一**：基于 JVM 的统一服务系统处理路由、推理和日志，GPU 模型通过 MSS 服务使用 Triton 推理服务器，支持多种框架。
- ⚙️ **引擎选择**：从 TensorRT-LLM 迁移到 vLLM，因其支持自定义架构、具备扩展调试能力，且研究到生产的过渡成本更低。
- 📦 **模型打包**：推荐使用 Triton 的 vLLM 后端，通过 JSON 配置动态生成 I/O 规范，避免模型与前端紧耦合；但需注意版本兼容和自定义模型需回退到 Python 后端。
- 🔌 **API 设计**：同时支持 gRPC（复用现有 ML 服务路径）和 OpenAI 兼容 HTTP 接口，便于第三方工具集成；需修补 Triton 前端对 `response_format` 的忽略问题。
- 🔄 **部署策略**：提供红黑部署（接口不变，成本低）和版本化部署（接口变更时优雅过渡），建议将可变配置嵌入模型，优先使用红黑方式。
- ⏱️ **启动优化**：通过 FSx 预缓存模型以降低冷启动延迟，并根据是否需 OpenAI API 决定使用嵌入式还是独立 Triton 实例。
- 📊 **指标合并**：vLLM 和 Triton 各自输出指标，通过轻量 HTTP 代理合并到统一 `/metrics` 端点，补全关键指标如令牌吞吐量、KV 缓存命中率。
- 🧠 **约束解码**：在 vLLM V0 中，自定义 logits 处理器逐个请求串行执行，导致 CPU 瓶颈；迁移至 V1 后实现批量处理并用 C++ 重写热点路径，性能显著提升。
- ⚠️ **解码工程隐患**：面临分块预填充和请求抢占问题，需额外追踪状态并重置状态机以保证正确性。
- 🔭 **未来方向**：计划推进系统提示压缩、vLLM V1 异步调度、向量化 logits 处理器（GPU 内核）以及低精度模型变体。

---

### [阿帕吉 - 软件工程师](https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/)

**原文标题**: [Appaji - Software Engineer](https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/)

一位求职者收到看似诱人的远程 Python 开发岗位，但发现其提供的代码仓库中隐藏了恶意 Git 钩子，最终揭露这是一场针对求职者的广泛恶意软件攻击。

- 🕵️‍♂️ 招聘岗位诱人但可疑：薪资高（每月 1 万 -1.5 万美元），且招聘者过早透露薪酬，引发警惕。
- 📁 发现隐藏恶意代码：通过运行`tree -a`查看隐藏目录，发现`.git/hooks`中预置了多个钩子脚本。
- 💻 脚本自动下载并执行 payload：`pre-commit`钩子根据操作系统自动下载并执行远程恶意脚本。
- 🔍 恶意脚本逐步深入：首先下载`tokenlinux.npl`，重命名为`tokenlinux.sh`并后台运行；然后安装 Node.js 并运行经过混淆的`parser.js`。
- 🧩 使用.npl 扩展名：该扩展名与已知恶意组织 NazarLazarus 关联。
- ⚙️ 依赖库可疑：`package.json`中包含`clipboardy`（剪贴板访问）、`hardhat`（以太坊开发环境）等，暗示可能窃取加密货币钱包。
- 🔗 存在多个攻击变种：有受害者收到包含`.vscode`文件夹的 ZIP，打开即可触发恶意命令。
- 🗃️ 项目是克隆的：从公开仓库`Bgogoi123/personal-finance-service`复制而来，攻击者只添加了恶意隐藏目录。
- 📡 攻击者 OPSEC 较好：服务器只开放 22 端口，运行最新版 OpenSSH，无已知漏洞可利用。
- 🚨 求职者应警惕：检查隐藏目录再运行他人代码，不轻易执行 git 命令触发 hooks。

---

### [](https://nem035.com/thoughts/how-claude-code-works)

**原文标题**: [How Claude Code Works, From Tokens to Agents • nem035](https://nem035.com/thoughts/how-claude-code-works)

Claude Code 等 AI 工具的工作原理从底层 token 生成开始，依次叠加提示组装、工具调用、代理循环、上下文管理、权限控制和自动化等层次。模型逐个 token 预测，无持久状态或规划，但可通过推理 token 和代理循环执行复杂任务。上下文窗口有限，需通过 RAG、压缩、子代理等方式优化。存在安全风险如提示注入和奉承行为。最终可通过 webhook 等触发自动化运行。

- 🤖 模型逐个 token 生成回复，无内部规划或并行推理，只能根据已生成内容继续预测
- 💬 每次调用会组装系统提示、工具定义、项目上下文和完整对话历史，模型视为连续 token 序列
- 🛠️ 工具调用通过外围软件拦截模型输出的结构化请求执行，并将结果注入上下文
- 🔄 代理循环：模型评估状态、输出工具调用、执行、结果反馈、再评估，直到输出纯文本
- 📉 上下文窗口有限且存在“上下文腐烂”，中间位置信息准确度下降；需通过 RAG、压缩、子代理管理
- 🧠 推理 token 在最终回答前生成，但常被丢弃或压缩；模型无法回忆原推理过程
- 📋 项目上下文文件（如 AGENTS.md）应只包含模型无法从代码自动发现的信息，避免冗余
- 🔍 RAG 优先搜索相关片段再添加，比直接塞满上下文更有效
- 📐 计划模式仅允许读工具，构建模式解锁全部操作；先思考后执行效果更好
- 🚦 权限系统通过钩子在工具执行前拦截、允许/拒绝/修改调用；可设置自动批准或需确认
- ⚠️ 提示注入：恶意文件或 API 返回内容可被模型误当作指令；只读模式可防御
- 🐑 奉承行为：模型倾向于执行用户指令而不质疑，即使决策不明智；用问题而非指令引导更好
- ⏰ 自动化：同一代理循环可通过 webhook、cron、Slack 等触发，非交互式运行，受预算和工具限制
- 💸 Token 累积：每轮重新读取全部历史，实际计费远高于新增内容；长会话成本成倍增长
- 📦 扩展工具：优先 CLI（零配置），需要控制时用 MCP，最后才考虑传统 API 集成

---

