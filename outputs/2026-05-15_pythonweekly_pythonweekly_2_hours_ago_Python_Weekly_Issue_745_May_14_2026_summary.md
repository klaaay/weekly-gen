### [我们如何通过用mypyc编译SQLGlot加速转译 | 博客 | Fivetran](https://www.fivetran.com/blog/how-we-accelerated-transpilation-by-compiling-sqlglot-with-mypyc?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [How we accelerated transpilation by compiling SQLGlot with mypyc | Blog | Fivetran](https://www.fivetran.com/blog/how-we-accelerated-transpilation-by-compiling-sqlglot-with-mypyc?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

Fivetran 是一个统一的数据移动平台，通过 SQLGlot 的 mypyc 编译优化，显著提升了 SQL 解析和转换性能。

- 🚀 **平台概述**：Fivetran 提供单一平台，支持数据移动、转换、安全、治理和扩展，涵盖多种部署和连接器选项。
- ⚡ **性能优化**：通过 mypyc 编译 SQLGlot，将核心模块转为 C 扩展，实现解析速度提升约 5 倍，SQL 生成提升约 2.5 倍，优化器提升 2-2.5 倍。
- 🔧 **技术挑战**：在编译过程中修复了 mypyc 的多个编译器错误（如 OOM、继承问题），并贡献了字符串操作原语（如 str.isspace、str.isdigit），加速高达 3.9 倍。
- 📦 **分发策略**：提供纯 Python 和编译版本（sqlglotc），用户可通过 pip install "sqlglot[c]" 安装，保持向后兼容。
- 💡 **关键发现**：mypyc 不仅提升性能，还通过严格类型检查暴露了代码中的真实 bug，并推动了更优的编码实践（如使用哨兵令牌和原生整数）。

---

### [介绍 Retrace：记录生产环境 Python，反向调试。 - Retrace | 实时探索你的生产环境分布式应用](https://retracesoftware.com/blog/introducing-retrace/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [Introducing Retrace: Record Production Python. Debug It Backwards. - Retrace | Explore your production, distributed application in real-time](https://retracesoftware.com/blog/introducing-retrace/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

Retrace 是一款用于 Python 生产环境的确定性记录-回放调试工具，可让开发者从崩溃点反向调试，无需复现故障。

- 🎯 **核心问题**：生产环境中的 Bug 难以复现，因为请求、数据库状态和外部 API 响应都已改变，传统日志和指标无法捕捉完整执行过程。
- 🚀 **解决方案**：Retrace 以 <0.1% 的开销记录生产环境中的 Python 执行，并允许在 VS Code 中确定性回放，支持从崩溃点反向步进到根因。
- 🔍 **实际案例**：当外部 API 返回非 JSON 文本导致 `JSONDecodeError` 时，Retrace 能记录并回放精确的响应和状态，无需重新运行或依赖日志。
- ⏳ **六年研发**：克服了线程非确定性、外部库、C 扩展和调试器观察效应等挑战，通过记录内部代码与外部世界的边界来实现可靠回放。
- ⚙️ **工作原理**：记录时拦截外部调用（网络、数据库、时间等）并存储结果；回放时返回记录值，保持线程顺序，实现确定性执行。
- 🔄 **反向调试**：在 VS Code 中支持“步进后退”和“反向继续”，从崩溃点开始逆向追踪，检查每一步的变量状态。
- 🏗️ **架构组件**：包括代理系统（拦截边界调用）、流写入器（异步存储二进制跟踪）、线程解复用器（保持线程顺序）和 VS Code 回放调试器。
- ❌ **非 APM 或日志工具**：不采样或聚合，而是记录完整执行，无需预先决定哪些变量重要。
- 📋 **当前支持**：Python 3.11/3.12、macOS/Linux、Flask/Django、Requests、psycopg2/PostgreSQL、线程、时间、随机数、文件 I/O 等。
- 🎉 **开源预览**：已发布，可通过 Quickstart 快速体验，并欢迎在 GitHub 上贡献或反馈。

---

### [Python中最简单的MCP示例 - 用Python创造](https://inventwithpython.com/blog/basic-mcp-python-example.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [The Simplest MCP Example Possible in Python - Invent with Python](https://inventwithpython.com/blog/basic-mcp-python-example.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

本教程通过一个简单的Python示例，展示了如何使用MCP（模型上下文协议）让本地大语言模型（LLM）调用外部工具（如获取当前时间和日期），并提供了完整的代码和运行效果。

- 🎯 **核心概念**：MCP是一种标准协议，允许LLM调用外部工具（如时钟、日历等），弥补其无法直接访问外部信息的缺陷。
- 🛠️ **所需工具**：使用Ollama运行本地LLM（如llama3.2），并通过FastMCP框架将Python函数封装为MCP工具。
- 📦 **安装步骤**：需通过pip安装`ollama`和`fastmcp`包，并运行`ollama pull llama3.2`下载模型（约2GB）。
- 📂 **代码结构**：包含两个文件——`mcp_server.py`（定义工具）和`ollama_client.py`（聊天循环），后者启动MCP服务器并处理用户输入。
- ⏰ **工具示例**：定义了两个工具——`get_current_time()`返回当前时间（HH:MM:SS格式），`get_current_date()`返回当前日期（YYYY-MM-DD格式）。
- 💬 **运行效果**：用户可提问“现在几点？”或“今天星期几？”，LLM会调用工具并返回结果，但存在幻觉问题（如错误判断日期和时间）。
- ⚠️ **局限性**：LLM可能输出错误信息（如将10:35误报为2:35 PM），且无法准确推断星期几，体现了常见的“幻觉”现象。

---

### [Labb - Django的UI组件（基于Tailwind、django-cotton、Alpine.js构建） - YouTube](https://www.youtube.com/watch?v=ZZd7cvbJ-1w&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [Labb - UI components for Django (built on Tailwind, django-cotton, Alpine.js!) - YouTube](https://www.youtube.com/watch?v=ZZd7cvbJ-1w&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

本頁面提供 YouTube 平台相關資訊與政策總覽，包括版權、聯絡方式、創作者支援、廣告、條款及隱私等。
- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明版權相關規範與權益保護
- 📞 聯絡我們：提供用戶與平台聯繫管道
- 🎬 創作者：支援內容創作者的資源與工具
- 📢 刊登廣告：說明廣告投放選項與流程
- 👨‍💻 開發人員：提供 API 與開發相關資訊
- 📜 條款：列出使用 YouTube 的服務條款
- 🔒 私隱：說明個人資料收集與使用方式
- 🛡️ 政策及安全：規範內容審查與安全措施
- ⚙️ YouTube 的運作方式：解釋平台推薦與演算法機制
- 🧪 測試新功能：介紹平台正在測試的新功能
- 📅 © 2026 Google LLC：版權歸屬與法律聲明

---

### [内核内广播优化：为RecSys推理协同设计内核 – PyTorch](https://pytorch.org/blog/in-kernel-broadcast-optimization-co-designing-kernels-for-recsys-inference/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [In-Kernel Broadcast Optimization: Co-Designing Kernels for RecSys Inference – PyTorch](https://pytorch.org/blog/in-kernel-broadcast-optimization-co-designing-kernels-for-recsys-inference/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

本文介绍了In-Kernel Broadcast Optimization (IKBO)，一种通过内核-模型-系统协同设计消除推荐系统推理中冗余用户嵌入广播的方法，显著降低延迟并提升吞吐量。

- 🚀 **IKBO核心思想**：将广播视为数据布局问题而非计算需求，通过在内核内部处理广播，避免张量复制，节省内存带宽和计算资源。
- ⚡ **线性压缩内核优化**：通过矩阵分解、内存对齐、广播融合和基于TLX的warp专用多级融合四个阶段，实现约4倍加速（1.944ms降至0.482ms）。
- 🔥 **Flash Attention优化**：IKBO将注意力内核从IO受限转为计算受限，在H100 SXM5上达到621 BF16 TFLOPs，吞吐量比非协同设计的CuTeDSL FA4 Hopper提升2.4倍/6.4倍。
- 🏭 **端到端部署**：已在Meta的RecSys推理栈中广泛部署，覆盖GPU和MTIA加速器，协同设计模型的计算密集型净延迟减少高达2/3。
- 💡 **系统级影响**：IKBO通过消除广播，使得密集交互达到接近独立计算成本的效果，成为Meta自适应排序模型的可扩展性骨干。
- 🔧 **技术实现**：利用Triton和TLX在Hopper架构上实现warp专用化、持久化内核和释放-获取同步协议，有效隐藏延迟并提高占用率。
- 📈 **未来方向**：IKBO可扩展到更深层次的多级用户-候选层次结构，并计划适配CuTeDSL和AMD CK后端。

---

### [DRY原则常常让你的代码变得更糟 - YouTube](https://www.youtube.com/watch?v=GmlZBdKhl9Y&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [DRY Often Makes Your Code Worse - YouTube](https://www.youtube.com/watch?v=GmlZBdKhl9Y&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

本頁面涵蓋 YouTube 平台的主要資訊與政策，包括版權、聯絡方式、創作者支援、廣告、條款及私隱等核心內容。

- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明內容使用規範與版權保護機制
- 📞 聯絡我們：提供用戶與創作者聯繫管道
- 🎬 創作者：支援內容創作者的工具與資源
- 📢 刊登廣告：介紹廣告投放選項與合作方式
- 👨‍💻 開發人員：提供 API 與技術整合資訊
- 📜 條款：列出使用 YouTube 服務的規範與協議
- 🔒 私隱：說明個人資料收集與使用政策
- 🛡️ 政策及安全：強調平台內容審查與安全措施
- ⚙️ YouTube 的運作方式：解釋推薦系統與內容管理機制
- 🧪 測試新功能：介紹平台正在測試的新特性
- 🏢 © 2026 Google LLC：版權歸屬與法律聲明

---

### [面向家庭的Python冻结集依赖类型理论 | 嘿，伙计！](https://www.philipzucker.com/dtt_python_family/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [Family Orienting Python Frozenset Dependent Type Theory | Hey There Buddo!](https://www.philipzucker.com/dtt_python_family/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

### 概述总结
本文探讨了如何用Python的frozenset和字典实现依赖类型理论的集合语义，核心思想是将所有类型视为“族”（family），即上下文到集合的映射。

- 🔑 **核心转变**：将类型视为“族”（字典+集合），而非独立值。即使像`Bool`这样的简单类型也表示为`{(): {True, False}}`，通过空元组键统一处理。
- 🧩 **判断即映射**：类型理论中的完整判断`[[Gamma |- Yada]]`应理解为从上下文到结果的映射，而非仅关注右侧内容。
- 🗂️ **上下文实现**：上下文是环境元组的frozenset，族是环境到集合的字典，通过`extend_ctx`等操作构建依赖上下文。
- 🔄 **弱化/细化**：通过`lweak`、`rweak`和`weak`函数实现上下文无关信息的添加，支持在元组任意位置插入新变量。
- 🛠️ **类型构造器**：实现了`Pair`、`Sigma`、`Pi`等依赖类型构造器，其中`Pi`通过字典实现函数空间，`Sigma`实现依赖对。
- 📝 **项与规则**：定义了`Section`（项）类型，实现了`lam`、`apply`、`ite`等操作，将推理规则映射为Python函数。
- 🔗 **同一性类型**：通过`Id`族实现，仅当两个值相等时包含`"refl"`标记，展示了依赖类型中的相等性判断。
- 💡 **设计哲学**：强调“有限化”和“平凡化”策略，通过统一使用0-arity结构简化实现，避免特殊处理。

---

### [GitHub - strukto-ai/mirage: 面向AI代理的统一虚拟文件系统 · GitHub](https://github.com/strukto-ai/mirage?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [GitHub - strukto-ai/mirage: A Unified Virtual Filesystem For AI Agents · GitHub](https://github.com/strukto-ai/mirage?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

Mirage 是一个面向AI代理的统一虚拟文件系统，将多种后端服务（如S3、Google Drive、Slack等）挂载为单一文件系统，使AI代理能通过熟悉的Unix工具访问所有服务。

- 📂 **统一文件系统**：将RAM、S3、Slack、GitHub等多种资源挂载到同一根目录下，AI代理只需学习一套文件系统语义即可操作所有后端
- 🛠️ **熟悉的bash工具**：代理可使用cp、grep、cat等Unix命令跨服务操作，无需为每个服务学习新API
- 🔄 **可移植工作区**：支持克隆、快照和版本化管理环境，可在不同机器间迁移代理运行环境
- 🧩 **框架集成**：兼容OpenAI Agents SDK、Vercel AI SDK、LangChain等主流AI代理框架，可作为沙箱或工具层嵌入
- ⚡ **双层缓存**：索引缓存和文件缓存减少网络请求，支持RAM和Redis两种后端，提升重复操作效率
- 🌐 **多语言支持**：提供Python和TypeScript SDK，以及CLI工具，适用于服务器、浏览器和边缘运行环境
- 🔌 **可扩展架构**：支持自定义命令和资源类型，可针对特定资源+文件类型覆盖默认命令行为

---

### [ProgramBench](https://programbench.com/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [ProgramBench](https://programbench.com/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

ProgramBench 评估语言模型能否仅凭编译后的二进制文件和文档，从头重建完整代码库，包含200个从简单工具到大型软件（如PHP编译器、FFmpeg、SQLite）的多样化任务，当前模型表现极低，最高解决率仅0.5%。

- 🧩 任务核心：代理需从零开始设计架构、选择语言、编写全部源码及构建脚本，无法访问原始源代码、反编译工具或互联网。
- 📊 当前成绩：最佳模型GPT 5.5 (xhigh) 仅解决0.5%任务，几乎所有模型完全解决率为0%，显示任务极高难度。
- 🛡️ 防作弊措施：代理在沙箱容器中运行，仅有执行权限，禁止反编译、网络访问及代码克隆，确保纯净实现。
- 🔬 测试方法：通过代理驱动的模糊测试生成超过248,000个行为测试，候选程序需通过所有测试才算解决。
- 🏆 独特之处：与现有基准不同，ProgramBench不提供任何提示或结构（如方法签名、类骨架），迫使代理真正进行软件架构设计。
- 📈 难度分布：任务涵盖从数千行代码的小工具到数万行的大型项目，如fzf（最佳82%）、ripgrep（84%）、jq（90%），但完全解决率极低。
- 🔄 未来方向：即将开放提交，期望推动新的代理架构竞赛，并持续监控模型记忆污染问题。

---

### [GitHub - VRSEN/OpenSwarm: 除了编程之外，Claude代码无所不能 · GitHub](https://github.com/VRSEN/OpenSwarm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [GitHub - VRSEN/OpenSwarm: Claude code for everything except coding · GitHub](https://github.com/VRSEN/OpenSwarm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

OpenSwarm 是一个完全开源的多智能体系统，通过一个终端提示即可生成幻灯片、研究报告、数据可视化、文档、图片和视频等多种交付物。

- 🚀 只需一个提示即可生成完整交付物，安装仅需30秒，运行只需60秒
- 🤖 包含8个专业智能体：编排器、虚拟助手、深度研究、数据分析、幻灯片、文档、图像生成和视频生成
- 🎯 智能体由编排器协调，各司其职，而非单一智能体包揽所有任务
- 📦 推荐通过 `npm install -g @vrsen/openswarm` 快速开始，支持自动安装依赖
- 🔧 可完全自定义和分支，支持通过 Claude Code、Cursor 或 Codex 创建自定义智能体群
- 🔌 通过 Composio 可连接 10,000+ 外部服务（如 Gmail、Slack、GitHub、HubSpot）
- ⚙️ 需要至少一个 API 密钥（OpenAI 或 Anthropic），可选 Google、FAL、Search 等增强功能
- 🏗️ 支持本地开发、Docker 部署和 API 服务器运行
- 📄 采用 MIT 许可证，由 Agency Swarm 团队构建

---

### [GitHub - awslabs/aidlc-workflows: 面向AI编码代理的AI驱动生命周期（AI-DLC）自适应工作流引导规则 · GitHub](https://github.com/awslabs/aidlc-workflows?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [GitHub - awslabs/aidlc-workflows: AI-Driven Life Cycle (AI-DLC) adaptive workflow steering rules for AI coding agents · GitHub](https://github.com/awslabs/aidlc-workflows?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

AI-DLC（AI驱动开发生命周期）是一个智能软件开发工作流，它适应项目需求、维持质量标准，并通过结构化流程让开发者始终掌握控制权。

- 🤖 **智能自适应工作流**：采用三阶段（构思→构建→运维）自适应流程，根据项目复杂度仅执行有价值阶段，简单变更保持高效。
- 📦 **多平台支持**：兼容Kiro、Amazon Q Developer、Cursor、Cline、Claude Code、GitHub Copilot、OpenAI Codex等主流AI编码代理。
- 🧩 **可扩展规则系统**：支持通过扩展机制添加安全、合规等自定义规则，用户可在需求分析阶段选择启用或禁用。
- 🔄 **人类始终在环**：关键决策需用户明确确认，AI提出方案、人类批准，确保开发者对流程的完全控制。
- 📋 **结构化文档生成**：所有工件自动生成至`aidlc-docs/`目录，便于追踪和审查。
- ⚙️ **便捷安装与更新**：提供手动复制和AI辅助自动安装两种方式，支持通过GitHub API自动下载最新版本。

---

### [GitHub - BigBodyCobain/Shadowbroker: 全球舞台的开源情报。在一个统一界面中追踪从富豪的企业/私人飞机、间谍卫星到地震事件的一切。接入AI代理，让其解析数据并发现此前未被察觉的关联。知识对所有人开放，但鲜少公开聚合，直到现在。](https://github.com/BigBodyCobain/Shadowbroker?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [GitHub - BigBodyCobain/Shadowbroker: Open-source intelligence for the global theater. Track everything from the corporate/private jets of the wealthy, and spy satellites, to seismic events in one unified interface. Hook an AI agent up to have it parse through data and find previously unseen correlations. The knowledge is available to all but rarely aggregated in the open, until now. · GitHub](https://github.com/BigBodyCobain/Shadowbroker?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

ShadowBroker 是一个开源的去中心化情报平台，将 60 多个实时公共数据源（包括航班、船舶、卫星、CCTV、无线电、地震、火灾等）整合到一个可交互的全球地图界面中，支持 AI 代理协作、SAR 地面变化检测、去中心化通信网格和快照回放功能。

- 🛰️ 实时整合 60+ 公共数据源，包括航班、船舶、卫星、军事、铁路、CCTV、无线电、地震、火灾、天气、基础设施等，所有数据在同一地图上实时更新
- 🤖 支持 AI 代理（如 OpenClaw、Claude、GPT）通过 HMAC 签名通道连接，可读写 35+ 数据层、放置标记、控制地图、参与网格通信和治理投票
- 🧅 内置去中心化情报网格 InfoNet，提供混淆消息、Dead Drop 点对点交换、门面身份系统、终端 CLI 和主权治理经济（请愿、升级投票、争议市场）
- 🛩️ 追踪全球航空（含军用、私人飞机、空军一号）、船舶（含航母战斗群）、卫星（按任务类型分类）、铁路、GPS 干扰区等
- 📷 接入 11,000+ 实时 CCTV 摄像头（覆盖 6 个国家）、500+ KiwiSDR 软件无线电、警察扫描仪和 APRS 业余无线电网络
- 🛰️ 支持 SAR 合成孔径雷达地面变化检测（通过 NASA OPERA 和 Copernicus EGMS），可定义监测区域并接收变形、洪水、植被扰动等异常警报
- ⏱️ 时间机器快照回放功能，支持暂停、快进、倒带和帧插值，可回溯任意历史时刻的完整情报画面
- 🚀 Docker 一键部署（预构建镜像），也支持 Kubernetes/Helm、Portainer 或无代码启动脚本（Windows/Mac/Linux）
- 🔑 可选集成 Shodan 设备搜索、Sentinel Hub 卫星影像、NASA Earthdata 等 API，所有数据本地自托管，不收集用户信息

---

### [GitHub - pthom/imgui_bundle: 面向桌面、移动端和网页的交互式Python与C++应用——由Dear ImGui驱动。告别GUI框架之争，即刻开始构建。](https://github.com/pthom/imgui_bundle?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [GitHub - pthom/imgui_bundle: Interactive Python & C++ apps for desktop, mobile, and web - powered by Dear ImGui. Stop fighting GUI frameworks. Start building. · GitHub](https://github.com/pthom/imgui_bundle?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

Dear ImGui Bundle 是一个基于 Dear ImGui 构建的跨平台框架，支持 C++ 和 Python，提供丰富的内置组件和工具，用于快速开发桌面、移动和 Web 应用。

- 🖥️ **跨平台支持**：兼容 Windows、macOS、Linux、iOS、Android 和 WebAssembly，覆盖主流设备。
- 🐍 **双语言 API**：C++ 和 Python 接口结构高度相似，降低学习成本，便于跨语言开发。
- 🧩 **集成生态**：内置 ImPlot/ImPlot3D 绘图、ImmVision 图像检查、节点编辑器、ImGuizmo 等丰富组件，开箱即用。
- 🚀 **高级运行框架**：提供 Hello ImGui 和 ImmApp 等可选高层框架，简化窗口管理、后端配置和附加组件激活。
- 🌐 **Web 就绪**：支持通过 Emscripten 运行 C++ 应用，以及通过 Pyodide 运行 Python 应用，并包含在线沙盒和可部署 HTML 模板。
- 📚 **完善文档与社区**：提供在线文档、Discord 社区和基于 AI 的 DeepWiki 问答系统，方便学习和交流。
- ⭐ **社区活跃**：拥有 1.3k 星标、117 个分支和 39 个发布版本，持续更新维护。

---

### [PyData 塔林 x Wise：第9次聚会（2026年5月），2026年5月18日（周一）下午6:00 | Meetup](https://www.meetup.com/pydata-tallinn/events/314159919/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [PyData Tallinn x Wise: Meetup #9 (2026 May), Mon, May 18, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-tallinn/events/314159919/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

概述摘要  
PyData Tallinn与Wise联合举办第9次聚会，时间为2026年5月18日18:00-21:00，地点在Wise Tallinn办公室。活动包括三场演讲（主题涉及Apache Spark机器学习、管理转型、AML运营扩展），并提供餐饮和社交机会。名额限制150人，需提前注册并携带身份证。

- 🎤 三场演讲：Apache Spark ML训练、管理转型的意外影响、AML运营团队扩展  
- 📍 地点：Wise Tallinn, Kopli 68a  
- ⏰ 时间：2026年5月18日18:00-21:00（EEST）  
- 🍕 提供食物和饮品，社交环节丰富  
- 🔒 名额限制150人，需提前通过Wise邮件注册并携带身份证  
- 🗣️ 活动语言为英语  
- 📝 欢迎提交未来演讲提案（通过Google表单）  
- 🤝 开放赞助机会，可联系组织者

---

### [从开放数据到数据网格，2026年5月19日（星期二）下午6:30 | Meetup](https://www.meetup.com/pydata-milano/events/313984221/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [From Open Data to Data Mesh, Tue, May 19, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-milano/events/313984221/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

本次活动探讨从开放数据到数据网格的演进，聚焦数据民主化与可扩展编排技术。

- 📅 活动时间与地点：2026年5月19日18:30-21:00，在米兰Generali Tower举办，名额有限需及时更新RSVP。
- 🗣️ 第一场演讲：深入探索Eurostat开放数据库，学习用Python工具获取和处理欧盟统计数据，以移民流动分析为例，将开放数据转化为可操作洞察。
- ⚙️ 第二场演讲：基于Dagster实现数据网格编排，通过平台自动构建全局DAG，解决跨域依赖瓶颈，避免上游团队因新消费者而频繁调整。
- 🎤 演讲者阵容：Simona Mazzarino（Clearbox AI）分享数据科学实践；Andrea Romeo与Marco Santoni（TeamSystem）展示生产级编排方案。
- 🍕 活动流程：18:30签到，19:00演讲开始，20:30社交晚餐，提供交流机会。

---

### [野外的AI：流式处理、服务与扩展生产系统，2026年5月20日（周三）下午5:30 | Meetup](https://www.meetup.com/pydata-nl/events/314681316/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [AI in the Wild: Streaming, Serving, and Scaling Production Systems, Wed, May 20, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-nl/events/314681316/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

本次PyData Amsterdam五月活动聚焦AI生产系统中的流处理、服务与扩展，涵盖Apache Flink在支付领域的实时应用及自托管AI架构的构建。

- 🎯 活动于2026年5月20日在阿姆斯特丹Adyen办公室举办，主题为“AI在野外：流处理、服务与扩展生产系统”
- 🍺 议程包括签到餐饮、两场技术演讲及交流环节，由PyData Amsterdam组织
- 🚀 第一场演讲：Adyen团队展示如何用Apache Flink构建实时特征平台，支持欺诈检测、路由优化等ML模型，确保全球支付处理的弹性与实时性
- 🏠 第二场演讲：Calogero Zarbo分享自托管AI架构，使用llama.cpp替代Ollama、FastAPI调度器动态切换模型（如DeepSeek-R1 70B），并通过Redpanda/Kafka解决延迟瓶颈
- 🔐 强调数据主权与成本控制，涵盖系统d服务链、Docker网络及自托管工具（如Huly、Joplin）替代SaaS
- 📝 需在Luma平台注册，入场需携带有效身份证件，地址距阿姆斯特丹中央车站步行7分钟

---

### [构建可靠湖仓一体最佳实践 | 2026年5月21日（周四）下午6:00 Meetup](https://www.meetup.com/pydatachi/events/314578784/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [Best Practices for Building a Reliable Lakehouse, Thu, May 21, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydatachi/events/314578784/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

本活动为PyData芝加哥分会主办的混合式技术讲座，主题为构建可靠数据湖仓的最佳实践，涵盖架构设计、数据建模、安全与性能优化等核心内容。

- 🗓️ 活动时间：5月21日（周四）下午6-8点（中部时间），线上+线下同步举行
- 📍 线下地点：伊利诺伊大学芝加哥分校Douglas Hall 220室（地址：705 S Morgan St, Chicago, IL）
- 🎤 主讲人：Justin Shea、Mehdi Jeddi、Erik Pak、Sou-Cheng Choi
- 🏗️ 核心内容：生产级数据湖仓实践指南，包括命名规范、最小权限访问、自动化CI/CD测试
- 📐 架构设计：讲解Medallion架构（青铜/银/金层）及元数据驱动设计模式
- 🛠️ 技术选型：对比Spark、Pandas、SQL的适用场景，使用YAML数据合约实现DQX数据质量管控
- 🔒 安全优化：涵盖安全最佳实践与性能调优策略
- 🍕 赞助支持：Adyen提供披萨饮料，UIC商学院提供场地，PyData芝加哥主办
- 🔗 线上参与：Zoom会议链接 https://iit-edu.zoom.us/j/89379230295，密码：5t5WYn

---

### [从提示到实际工作流——使用Python构建你的第一个智能体AI系统，2026年5月23日周六上午9:30 | Meetup](https://www.meetup.com/pydata-indore/events/314541790/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

**原文标题**: [From Prompt to Real Workflow — Building Your First Agentic AI System with Python, Sat, May 23, 2026, 9:30 AM   | Meetup](https://www.meetup.com/pydata-indore/events/314541790/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-745-may-14-2026)

概述摘要
- 📅 活动将于5月4日开放预约，5月23日举办，由PyData Indore主办
- 🐍 主题为“从提示到实际工作流——用Python构建首个Agentic AI系统”
- 🤖 会议将超越简单提示，探索AI如何思考、规划和执行任务
- 🛠️ 适合从ChatGPT用户到AI初学者的各类参与者
- 📍 地点在印度印多尔的InfoBeans Foundation
- 🏢 赞助商为NumFOCUS，致力于推广开源科学代码

---

