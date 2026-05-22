### [智能体钩子：智能体工作流的确定性控制](https://nader.substack.com/p/agent-hooks-deterministic-control?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Agent Hooks: Deterministic Control for Agent Workflows](https://nader.substack.com/p/agent-hooks-deterministic-control?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

### 概述总结
Agent Hooks 通过将可重复规则从模型记忆转移到代码中，在代理工作流的已知生命周期点运行，从而提供确定性控制。文章介绍了六个核心生命周期点（SessionStart、UserPromptSubmit、PreToolUse、PostToolUse、Stop、SessionEnd），并通过一个实际演示项目展示了如何实现上下文加载、动作阻止、验证执行和完成门控等功能。

- 🎯 **核心价值**：将规则从模型记忆转移到代码，在已知生命周期点强制执行确定性行为，而非依赖模型自愿遵守
- 🔄 **生命周期点**：SessionStart（加载上下文）、UserPromptSubmit（检查提示）、PreToolUse（阻止动作）、PostToolUse（验证结果）、Stop（阻止完成）、SessionEnd（记录日志）
- 🛡️ **PreToolUse 示例**：阻止编辑生成文件、敏感配置和危险 shell 命令，在动作执行前就拦截
- ✅ **PostToolUse 示例**：代码编辑后自动运行测试套件，并将结果持久化到状态文件
- 🚫 **Stop 示例**：读取质量门状态文件，当测试失败时阻止代理完成当前任务
- 📝 **SessionEnd 示例**：会话结束时写入最终审计记录，包括时间戳、会话 ID 和原因
- 🧩 **分层职责**：提示用于指导，Hook 用于控制，CI 用于独立验证，人工审查用于最终决策
- 📈 **采用路径**：从保护路径的 PreToolUse 开始，然后添加质量门 PostToolUse 和 Stop，最后补充 SessionStart 和 SessionEnd
- 💡 **实用规则**：当需求包含“总是”、“从不”、“阻止”、“记录”、“运行”或“验证”时，应放入 Hook 而非仅放在提示中
- 🔗 **演示项目**：包含完整的结账计算器 demo，可测试所有 Hook 生命周期点的工作流程

---

### [让我们一劳永逸地修复臃肿的 Python 类 - YouTube](https://www.youtube.com/watch?v=F5Av5yDGSQs&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Let’s Fix Bloated Python Classes Once and For All - YouTube](https://www.youtube.com/watch?v=F5Av5yDGSQs&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

YouTube 平台提供的各项服务与法律条款概览
- 📖 关于我们：介绍 YouTube 的使命与平台定位
- 📰 新闻与媒体：提供新闻稿、媒体资源及官方动态
- ⚖️ 版权保护：说明版权政策及内容管理机制
- 📞 联系我们：提供用户与合作伙伴的联系渠道
- 🎥 创作者支持：面向内容创作者的资源与工具
- 📢 广告与推广：介绍广告投放选项与合作伙伴计划
- 💻 开发者服务：提供 API、开发者文档及技术资源
- 📜 服务条款：明确用户使用 YouTube 的法律协议
- 🔒 隐私政策：说明数据收集、使用与用户权利
- 🛡️ 安全与政策：平台安全准则及内容审核规则
- ⚙️ YouTube 运作方式：解释推荐算法、内容分发等机制
- 🧪 测试新功能：介绍平台正在测试的实验性功能
- ©️ 版权信息：© 2026 Google LLC，保留所有权利

---

### [在 macOS 上监控文件变化 – alexwlchan](https://alexwlchan.net/2026/watch-files-on-macos/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Watching for file changes on macOS – alexwlchan](https://alexwlchan.net/2026/watch-files-on-macos/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

该文章详细介绍了如何在 macOS 上构建一个高效的文件变化监控系统，用于触发静态网站的重建和浏览器自动刷新。作者使用 Swift 的 FSEvents API 检测文件变化，并通过 stdout 将变化信息传递给 Python 脚本，最终实现增量重建和实时刷新。

- 🖥️ **macOS FSEvents API**：使用苹果原生 API 监控目录树变化，支持文件级事件检测，比传统轮询更高效（2-4ms 响应）。
- 🔧 **Swift 脚本实现**：通过`FSEventStreamCreate`创建事件流，设置回调函数捕获变化路径，支持`kFSEventStreamCreateFlagFileEvents`标志获取具体文件信息。
- 🔗 **Swift 与 Python 桥接**：Swift 脚本将文件路径输出到 stdout，Python 通过`subprocess.Popen`读取输出流，实现跨语言通信。
- ⚡ **防抖处理**：使用 Python 的`selectors`模块实现非阻塞 I/O，在重建期间累积变化事件，避免重复触发重建。
- 🚫 **拒绝第三方库**：作者选择自建方案而非使用`watchdog`等库，以保持代码精简并深入理解底层机制。
- 📈 **性能优化**：增量重建仅处理变更文件，全站重建耗时 10-15 秒，而监控系统仅需 2-4ms 即可检测变化。
- 🧠 **学习收获**：通过实践掌握了 FSEvents API、非阻塞 I/O 和选择器模块，加深了对操作系统文件系统事件机制的理解。

---

### [获取失败](https://replit.com/refer/rahulgchaudhary?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Failed to retrieve](https://replit.com/refer/rahulgchaudhary?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

无法总结：获取内容失败，状态码 403。

---

### [django-q2 - Django 中的后台任务（Celery 替代方案！）- YouTube](https://www.youtube.com/watch?v=0hRDCrxfHug&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [django-q2 - Background Tasks in Django (Celery alternative!) - YouTube](https://www.youtube.com/watch?v=0hRDCrxfHug&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

本頁面列出了 YouTube 平台的各項重要資訊與政策，涵蓋版權、聯絡方式、創作者支援及法律條款等核心內容。

- 📰 提供新聞中心，發布官方最新消息與更新
- ©️ 明確版權相關資訊，保護內容創作者權益
- 📞 設有聯絡我們管道，供用戶諮詢與回饋
- 🎬 為創作者提供資源與廣告刊登服務
- ⚖️ 詳列使用條款、私隱政策及安全規範
- 🔧 說明 YouTube 運作方式與新功能測試
- 📅 版權標示為© 2026 Google LLC

---

### [将 Python 日志模块桥接到 OpenTelemetry（完整指南）· Dash0](https://www.dash0.com/guides/opentelemetry-logging-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Bridging Python's Logging Module to OpenTelemetry (Complete Guide) · Dash0](https://www.dash0.com/guides/opentelemetry-logging-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

本指南詳細說明了如何將 Python 的標準 logging 模組與 OpenTelemetry (OTel) 整合，以建立可觀測性管道。

- 📝 **概述**：本指南逐步說明如何將 Python 的標準 logging 模組橋接到 OpenTelemetry (OTel) 生態系統。透過 OTel 的 `LoggingHandler`，您可以將現有的日誌記錄轉換為符合 OTel 資料模型的日誌，並自動與追蹤（trace）關聯，最終透過 Collector 發送到後端（如 Dash0），而無需更改應用程式的日誌呼叫方式。

- 🚀 **快速入門**：建立一個使用 JSON 格式記錄日誌的 FastAPI 應用程式作為起點，並安裝 `opentelemetry-sdk` 等必要套件。

- 🔗 **核心整合**：在 `logging.yaml` 設定檔中新增 `opentelemetry.sdk._logs.LoggingHandler` 作為第二個處理器，並在應用程式啟動時初始化 OTel 的 `LoggerProvider`。

- 🔄 **欄位映射**：Python 的 `LogRecord` 會自動映射為 OTel 的 `LogRecord`，例如：時間戳記、日誌級別、訊息本體、透過 `extra` 傳遞的屬性，以及程式碼位置（`code.file.path` 等）。

- 🧬 **追蹤關聯**：透過 `TracerProvider` 和 FastAPI 檢測，日誌記錄會自動攜帶當前活躍的 `trace_id` 和 `span_id`，實現日誌與請求追蹤的完美連結。

- 🏷️ **語意慣例**：採用 OpenTelemetry 的語意慣例來命名屬性（例如 `user.id` 取代 `user_id`），以確保跨服務的一致性。對於自訂屬性，建議使用點分隔的命名空間（如 `com.acme.order.id`）。

- 🏭 **生產環境部署**：將 `ConsoleLogExporter` 替換為 `OTLPLogExporter`，並使用 `BatchLogRecordProcessor` 進行批次處理，再透過 OpenTelemetry Collector 將資料發送到後端。

- 🎯 **發送到 Dash0**：在 Collector 設定中新增 Dash0 的 OTLP 端點，即可將結構化、帶有追蹤關聯的日誌發送到 Dash0 進行分析。

- ⚖️ **替代方案**：對於高吞吐量場景，可以考慮在 Collector 端進行轉換，但需自行處理追蹤 ID 的注入和 OTTL 映射。

- 🏁 **總結**：`LoggingHandler` 是連接 Python 日誌與 OTel 生態系最簡單直接的路徑，能無痛升級您的可觀測性能力。

---

### [错误](https://blog.jupyter.org/nb-cli-a-command-line-interface-for-ai-agents-and-notebook-automation-996ad7edacd9?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Error](https://blog.jupyter.org/nb-cli-a-command-line-interface-for-ai-agents-and-notebook-automation-996ad7edacd9?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='blog.jupyter.org', port=443): Max retries exceeded with url: /nb-cli-a-command-line-interface-for-ai-agents-and-notebook-automation-996ad7edacd9?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

---

### [LLM 评估与 AI 可观测性在智能体监控中的应用 | PyCharm 博客](https://blog.jetbrains.com/pycharm/2026/05/llm-evaluation-and-ai-observability-for-agent-monitoring/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [LLM Evaluation and AI Observability for Agent Monitoring | The PyCharm Blog](https://blog.jetbrains.com/pycharm/2026/05/llm-evaluation-and-ai-observability-for-agent-monitoring/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

概述摘要  
- 🤖 AI 代理系统正从简单单代理向多代理协作演进，需要更复杂的监控和评估方法  
- 📊 LLM 评估核心指标包括幻觉率、毒性分数、RAGAS 和 DeepEval，用于衡量模型基础能力  
- 🔍 传统静态评估无法捕捉多步骤代理的决策过程，需结合高级指标如任务完成率、工具使用正确性和推理准确性  
- 🛠️ PyCharm 的 AI 代理调试器可追踪 LangGraph 工作流，可视化代理节点输入输出和推理过程  
- 📈 AI 可观测性通过记录代理每一步的推理、工具调用和数据检索，实现实时监控和问题调试  
- 💰 生产环境需持续监控成本和延迟，结合离线测试与在线评估，必要时引入人工审核环节  
- ⚡ 持续评估和可观测性使团队能快速迭代，将数小时调试缩短为几分钟系统化调查

---

### [智能体评估：详细指南](https://cameronrwolfe.substack.com/p/agent-evals?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Agent Evaluation: A Detailed Guide](https://cameronrwolfe.substack.com/p/agent-evals?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

### 概述总结
本文详细介绍了 AI 代理系统的评估方法，涵盖代理基础、评估框架、案例研究和实践路线图，强调在复杂、长期任务中评估代理的重要性。

- 🤖 **代理系统基础**：代理是 LLM 在循环中自主使用工具的系统，具备推理、工具调用、错误恢复等能力，其核心组件包括 LLM、工具和指令。
- 🛠️ **工具使用与推理**：工具调用通过特殊标记实现，需设计清晰、文档完善的工具；推理模型（如思考轨迹）能分解复杂问题，提升代理性能。
- 📋 **多代理系统**：当单代理指令臃肿或工具选择困难时，可采用管理型或去中心化多代理架构，但应优先优化单代理设计。
- 🧠 **上下文工程**：通过动态上下文、压缩（摘要、工具结果清除、笔记）等方法管理代理上下文，避免“上下文腐烂”影响性能。
- 🏗️ **代理脚手架**：脚手架是运行代理的系统（如 ReAct），影响环境接口、提示策略、工具设计等，评估时需同时考虑模型和脚手架能力。
- 📊 **评估组件**：包括任务、试验、转录、结果和评分器，评分器分为人工评估（黄金标准）、代码型（确定性检查）和模型型（LLM 作为裁判）。
- 🔍 **案例研究**：τ-bench 系列（零售/航空/电信领域，使用模拟用户和确定性检查）和 Terminal-Bench（终端任务，结果导向，需人工验证）展示了评估框架的实际应用。
- 🗺️ **评估路线图**：定义成功标准→收集小任务集→创建高质量任务→提供参考解→配置评分器→构建评估工具→持续迭代维护。

---

### [Django LiveView 对比 Phoenix LiveView：真实基准测试 | Andros Fenollosa](https://en.andros.dev/blog/80134668/django-liveview-vs-phoenix-liveview-a-real-benchmark/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Django LiveView vs Phoenix LiveView: a real benchmark | Andros Fenollosa](https://en.andros.dev/blog/80134668/django-liveview-vs-phoenix-liveview-a-real-benchmark/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

本基准测试对比了 Django LiveView 和 Phoenix LiveView 在相同条件下的性能表现，结果显示两者在日常操作中几乎持平，但 Phoenix 在大数据量和并发场景下更具优势。

- 📊 **日常场景性能相当**：在添加、删除和搜索操作中，Django LiveView 和 Phoenix LiveView 的平均延迟几乎相同（约 22 毫秒和 7 毫秒），差异统计上不显著。
- 🚀 **边缘场景略有差异**：处理 500 项大列表时，Phoenix 稍快（49.70 毫秒 vs 52.84 毫秒），快速点击场景两者几乎一致。
- 📦 **数据负载差距显著**：Django LiveView 每次操作传输的数据量远大于 Phoenix，例如大列表场景下 Django 传输 327 KB，而 Phoenix 仅 67 KB，原因是 Django 会重新发送整个 HTML 片段，而 Phoenix 只发送差异部分。
- 👥 **并发性能分化**：在 1-5 个客户端时两者相似，但 50 个并发客户端时，Django 的延迟（483 毫秒）几乎是 Phoenix（243.8 毫秒）的两倍，Phoenix 扩展性更好。
- 🐍 **Django LiveView 的优势**：允许开发者留在 Python 和 Django 生态中，代码更显式和可预测，可通过优化选择器减少数据传输。
- 💡 **结论**：日常使用中两者几乎无差别，但 Phoenix 在数据负载和并发方面更优，而 Django LiveView 适合熟悉 Django 生态的开发者。

---

### [GitHub - MinishLab/semble: 面向智能体的快速精准代码搜索。相比 grep+read，可减少约 98% 的令牌消耗](https://github.com/MinishLab/semble?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - MinishLab/semble: Fast and Accurate Code Search for Agents. Uses ~98% fewer tokens than grep+read · GitHub](https://github.com/MinishLab/semble?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

Semble 是一个专为 AI 智能体设计的快速精准代码搜索库，能大幅节省 token 消耗，索引和搜索均在毫秒级完成，且完全在 CPU 上运行，无需任何外部服务或 API 密钥。

- ⚡ **极速性能**：平均索引一个仓库约 250 毫秒，查询仅需 1.5 毫秒，全部在 CPU 上完成。
- 🎯 **高精度检索**：NDCG@10 得分达 0.854，与代码专用 Transformer 模型性能相当，但体积和成本极低。
- 💰 **节省 98% Token**：仅返回相关代码片段，相比传统的 grep+ 读取全文方式，平均节省约 98% 的 token。
- 🔌 **零配置与多模式**：支持 MCP 服务器、命令行 (CLI) 和 Python 库三种使用方式，无需 API 密钥或 GPU。
- 🤖 **智能体友好**：可作为 MCP 服务器集成到 Claude Code、Cursor 等主流 AI 编码工具中，也支持通过 AGENTS.md 配置 Bash 模式。
- 🔍 **双检索器融合**：结合静态嵌入模型 (Model2Vec) 进行语义搜索和 BM25 进行词汇匹配，并通过倒数排名融合 (RRF) 优化结果。
- 🧠 **代码感知重排序**：应用自适应权重、定义提升、标识符词干匹配、文件连贯性提升和噪声惩罚等多种信号，确保结果精准。
- 📦 **使用灵活**：支持本地路径和 Git 远程仓库 URL，并提供 `semble savings` 命令统计 token 节省量。
- 📜 **开源协议**：采用 MIT 许可证，并提供了学术引用格式。

---

### [GitHub - PurpleAILAB/Decepticon：红队自主黑客代理 · GitHub](https://github.com/PurpleAILAB/Decepticon?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - PurpleAILAB/Decepticon: Autonomous Hacking Agent for Red Team · GitHub](https://github.com/PurpleAILAB/Decepticon?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

Decepticon 是一个专业的自主红队代理，能够执行真实的攻击链，并具备完整的交战规则和沙箱隔离机制。

- 🤖 **自主红队代理**：Decepticon 执行侦察、利用、提权、横向移动和 C2 等真实攻击链，而非简单的扫描报告。
- 📋 **完整的交战流程**：在行动前生成交战规则（RoE）、概念操作（ConOps）、冲突解除计划和行动方案（OPPLAN），并映射 MITRE ATT&CK 框架。
- 🛡️ **强化沙箱隔离**：所有命令在 Kali Linux 沙箱中运行，使用专用操作网络（sandbox-net），与管理网络（decepticon-net）分离。
- 🧠 **16 个专业代理**：按攻击链阶段组织，包括编排、侦察、利用、后利用、漏洞研究及领域专家（AD、云、智能合约等）。
- 🔄 **模型与提供商**：支持分层模型配置，包含 Anthropic、OpenAI、Google Gemini 等，并具备凭据感知的故障转移链。
- 🏆 **基准测试表现**：在 XBOW 验证基准测试中，整体通过率达 98.08%，其中简单级别 100% 通过。
- 💻 **交互式 Shell 支持**：在持久 tmux 会话中运行真实交互工具（如 msfconsole、sliver-client），自动检测提示符并发送后续命令。
- 📚 **丰富文档**：提供安装指南、设置教程、CLI 参考、代理名单、模型配置、技能系统、架构说明等全面文档。
- 🔒 **安全与许可**：强调未经授权不得使用，采用 Apache-2.0 许可，并设有行为准则和贡献指南。

---

### [GitHub - anthropics/claude-for-legal: 法律工作流程插件套件 · GitHub](https://github.com/anthropics/claude-for-legal?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - anthropics/claude-for-legal: A suite of plugins for legal workflows · GitHub](https://github.com/anthropics/claude-for-legal?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

Anthropic 的 Claude for Legal 是一个开源的法律工作流插件套件，专为律师和法律团队设计，涵盖商业、隐私、公司、劳动、诉讼、知识产权等多个领域。它通过 Claude Cowork 或 Claude Code 运行，提供技能、代理和数据连接器，支持自动化审查、合规监控、尽职调查等任务，并强调所有输出仅为草稿，需律师审核。

- ⚖️ **核心定位**：提供法律工作流的参考代理、技能和数据连接器，覆盖商业、隐私、公司、劳动、诉讼、知识产权等实践领域，所有输出均为草稿，需律师审核。
- 🚀 **快速入门**：通过 QUICKSTART.md 可在 60 秒内安装，支持 Claude Cowork 插件或 Claude Code 部署，也可通过 Claude Managed Agents API 在自有工作流引擎后运行。
- 📂 **仓库结构**：包含实践领域插件（如 commercial-legal）、管理代理食谱（如 renewal-watcher）、MCP 连接器（如 Slack、Google Drive、Ironclad）和命名代理（如 Vendor Agreement Reviewer）。
- 🤖 **代理功能**：每个代理以工作流命名，如 Vendor Agreement Reviewer 审查供应商协议，NDA Triager 对 NDA 进行红黄绿分类，支持斜杠命令和定时代理。
- 🔗 **连接器集成**：内置 MCP 连接器，包括法律研究工具（如 CourtListener、Trellis）、生产力工具（如 Slack、Google Drive）和特定法律系统（如 DocuSign、Everlaw），确保引用可验证。
- 🛡️ **安全与信任**：所有输出带有来源归属、保守默认设置和明确门控，社区技能通过 legal-builder-hub 进行安全审查、允许列表和许可证门控。
- 📝 **定制化**：通过冷启动面试学习团队实践，编辑实践配置文件（CLAUDE.md）或分叉技能以适应特定风格，无需构建步骤。
- 📊 **技能与命令**：提供全面的技能和命令参考，如 /commercial-legal:review 审查供应商协议，/privacy-legal:dsar-response 处理数据主体访问请求。
- 🌐 **生态与贡献**：支持社区技能发现和安装，通过法律技能设计框架进行质量评估，鼓励通过分叉和 PR 贡献新技能或代理。

---

### [GitHub - CodeBoarding/CodeBoarding: 代码库的交互式架构图 · GitHub](https://github.com/CodeBoarding/CodeBoarding?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - CodeBoarding/CodeBoarding: Interactive architecture diagrams for codebases · GitHub](https://github.com/CodeBoarding/CodeBoarding?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

CodeBoarding 是一个为开发者和 AI 编码代理提供代码库可视化地图的工具，通过静态分析与 LLM 推理生成架构图、组件文档和可导航输出，支持 IDE、CI 和文档等多种使用场景。

- 🗺️ **核心功能**：生成高层系统架构图、深层组件图、Markdown 文档和 Mermaid 输出，支持增量更新。
- 🛠️ **工作原理**：结合应用编排器、LLM 核心、静态分析器、代理工具接口、增量分析引擎和文档生成器，协同完成分析。
- 🚀 **快速开始**：支持从源码运行（`uv sync --frozen`）或使用打包 CLI（`pipx install codeboarding`），输出至`.codeboarding/`目录。
- ⚙️ **配置灵活**：支持 OpenAI、Anthropic、Google 等多种 LLM 提供商，环境变量优先于配置文件。
- 💻 **使用场景**：CLI 用于本地/CI 分析，VS Code 扩展用于编辑器内可视化，GitHub Action 用于 CI 中保持图表更新。
- 🌐 **支持范围**：覆盖Python、TypeScript、Java、Go、PHP、Rust、C#等语言，以及多种LLM提供商。
- 📚 **示例丰富**：已可视化 800+ 开源仓库，可浏览生成示例或尝试托管探索器。
- 🤝 **社区贡献**：欢迎提交 issue 或 PR，共同构建代码理解开放标准。

---

### [GitHub - mattzh72/articraft: 一个用于可扩展关节式 3D 资产生成的智能体系统](https://github.com/mattzh72/articraft?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - mattzh72/articraft: An Agentic System for Scalable Articulated 3D Asset Generation · GitHub](https://github.com/mattzh72/articraft?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

Articraft 是一个基于 LLM 的智能体系统，通过代码生成工作流实现可扩展的铰接式 3D 资产创建，支持大规模数据集生成。

- 🤖 利用大语言模型将铰接式 3D 资产创建转化为程序化代码生成流程，无需手动建模工具
- 🚀 快速上手：支持 Python 3.12，使用 uv 包管理器和 just 命令运行器，通过 `just setup` 完成环境搭建
- 🔑 支持多种 API 密钥（如 OpenAI、Gemini、Anthropic），也可通过外部 AI 代理（如 Claude Code）生成资产
- 🎨 通过 `articraft generate` 命令从文本提示直接生成模型，支持参考图像条件生成
- 👁️ 提供本地查看器（`just viewer`），可浏览、搜索和预览数据集中的记录
- ✏️ 支持对现有记录进行分叉编辑（`uv run articraft fork`），创建新子记录而不影响原始数据
- 📊 数据集通过 Git LFS 管理，可按需水合记录以检查或渲染
- 🤝 鼓励社区贡献数据，所有贡献数据以 CC-BY 4.0 许可发布，用于构建和改进机器学习模型
- 📚 提供详细的文档，包括架构、编辑、图像条件生成、批量处理和安全策略
- 📝 项目在 Apache-2.0 许可下开源，已发表相关学术论文

---

### [GitHub - chopratejas/headroom: 在工具输出、日志、文件和 RAG 分块到达大语言模型前进行压缩。减少 60-95% 的令牌，答案不变。包含库、代理、MCP 服务器。](https://github.com/chopratejas/headroom?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - chopratejas/headroom: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Library, proxy, MCP server. · GitHub](https://github.com/chopratejas/headroom?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

Headroom 是一个针对 AI 代理的上下文压缩层，可在不影响答案质量的前提下，将 Token 消耗减少 60-95%。

- 🧠 **核心功能**：在 AI 代理读取工具输出、日志、RAG 块、文件和对话历史之前，进行本地压缩，大幅降低 Token 使用量。
- 📦 **多种集成方式**：提供 Python/TypeScript 库、零代码更改的代理、一键包装代理（如 Claude Code）以及 MCP 服务器，适配各种开发场景。
- 🔄 **可逆压缩 (CCR)**：原始数据永不删除，LLM 可按需通过 `headroom_retrieve` 工具检索，确保信息不丢失。
- 🧩 **智能压缩算法**：内置 SmartCrusher (JSON)、CodeCompressor (AST) 和 Kompress-base (文本) 等多种算法，自动识别内容类型并选择最佳压缩方式。
- 🤝 **跨代理记忆**：支持在 Claude、Codex、Gemini 等多个代理间共享记忆，并自动去重。
- 📈 **显著节省效果**：代码搜索节省 92%，SRE 问题调试节省 92%，GitHub 问题分类节省 73%，且基准测试准确率保持不变。
- 🔌 **广泛框架兼容**：可与 Anthropic/OpenAI SDK、Vercel AI SDK、LangChain、Agno、Strands 等主流框架无缝集成。
- 🧪 **故障学习 (headroom learn)**：自动分析失败会话，并将修正写入 `CLAUDE.md` / `AGENTS.md` 文件中。
- 🚀 **快速上手**：通过 `pip install "headroom-ai[all]"` 或 `npm install headroom-ai` 一键安装，60 秒内即可开始使用。
- 🏘️ **活跃社区**：社区已节省超过 600 亿 Token，提供 Discord 讨论、实时排行榜和 HuggingFace 模型。

---

### [GitHub - soldatov-ss/django-completion: Django manage.py 的 Tab 补全功能 —— 在 bash 和 zsh 中补全命令、应用标签、选项和迁移目标 · GitHub](https://github.com/soldatov-ss/django-completion?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - soldatov-ss/django-completion: Tab completion for Django's manage.py — commands, app labels, options, and migration targets in bash and zsh · GitHub](https://github.com/soldatov-ss/django-completion?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

django-completion 是一个为 Django 的 manage.py 提供项目感知的 Tab 自动补全工具，支持 bash 和 zsh shell，可补全命令、应用标签、选项和迁移目标。

- 🚀 通过 pip 或 uv 安装，添加至 INSTALLED_APPS 并运行安装命令即可使用
- 🎯 支持补全命令名称、选项标志、应用标签、迁移名称及 zero 等深度内容
- ⚡ 自动缓存刷新（60 秒冷却），也可手动运行 refresh 命令重建缓存
- 🔒 注重安全与隐私：无遥测、无网络调用、不导入 Django、不访问数据库
- 🐚 兼容 Python 3.10+、Django 4.2+，支持 bash 和 zsh，Linux 和 macOS
- ⚠️ 局限性：不支持 fish、django-admin、Windows、自定义别名及数据库感知过滤
- 🗺️ 路线图包括更多包装器支持、Docker 示例、fish shell 支持及命令特定补全规则

---

### [GitHub - thesaadmirza/feloxi：实时Celery任务队列监控 — Rust/Axum后端，Next.js仪表盘，ClickHouse分析 · GitHub](https://github.com/thesaadmirza/feloxi?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - thesaadmirza/feloxi: Real-time Celery task queue monitoring — Rust/Axum backend, Next.js dashboard, ClickHouse analytics · GitHub](https://github.com/thesaadmirza/feloxi?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

Feloxi 是一个自托管的 Celery 任务队列监控平台，提供实时仪表盘、可搜索的任务历史记录和告警功能。

- 🔍 **任务搜索与过滤**：支持全文搜索任务 ID、名称、参数、结果和异常，可按状态、队列、工作节点和时间范围过滤，并查看状态时间线、回溯和重试操作。
- 🩺 **工作节点健康监控**：显示 CPU、内存、池大小、活跃任务数和心跳间隔，支持远程关闭和颜色编码的健康指示。
- 🗺️ **工作流可视化**：将 Celery 链、组、和弦渲染为交互式 DAG，直观显示多阶段管道的故障点。
- ⏰ **定时任务跟踪**：Beat 调度器页面显示每个定时任务的调度表达式、上次/下次运行时间及错过的节拍数，支持错过节拍告警。
- 🚨 **灵活告警**：支持 10 种告警条件（如失败率、慢任务、工作节点离线、队列深度等），可路由至 Slack、邮件、Webhook 或 PagerDuty，并具备冷却期防止告警风暴。
- 🛠️ **统一代理管理**：通过三步向导添加 Redis 或 RabbitMQ 代理，支持连接测试、独立启停及每代理统计（总事件、吞吐量、成功率、队列深度等）。
- 📊 **Prometheus 导出**：API 服务器提供 `/metrics` 端点，暴露任务总数、失败率、平均运行时间、队列深度和工作节点在线数等指标。
- 🚀 **快速启动**：通过 `docker compose up -d` 一键启动，内置演示数据（50,000 个任务事件和 6 个模拟工作节点），无需安装代理或 SDK。
- 🔗 **轻松连接现有 Celery 应用**：仅需在配置中设置 `worker_send_task_events=True` 等三个选项，重启工作节点并添加代理 URL 即可。
- 🏗️ **生产级部署**：支持 Kubernetes（Helm chart）和 Docker Compose，可配置外部 PostgreSQL、ClickHouse 和 Redis，并建议使用反向代理和 TLS。

---

### [GitHub - zubair-trabzada/geo-seo-claude: 面向 Claude Code 的 GEO 优先 SEO 技能。适用于任何网站的全面 AI 搜索优化——可引性评分、AI 爬虫分析、品牌权威、结构化数据标记、平台特定优化及 PDF 报告。若想了解如何向真实企业销售此服务，请查看 Skool 社区。](https://github.com/zubair-trabzada/geo-seo-claude?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - zubair-trabzada/geo-seo-claude: GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website — citability scoring, AI crawler analysis, brand authority, schema markup, platform-specific optimization, and PDF reports.  If you want learn how to sell this to real businesses, check out the skool community · GitHub](https://github.com/zubair-trabzada/geo-seo-claude?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

GEO-SEO-Claude 是一个专为 AI 搜索引擎（如 ChatGPT、Claude、Perplexity 等）优化网站的开源工具，同时保留传统 SEO 基础，以应对 AI 搜索流量增长和传统搜索流量下降的趋势。

- 📈 **市场趋势与数据** — 2026 年 GEO 服务市场预计达 7.3 亿美元，AI 推荐流量同比增长 527%，转化率是传统有机搜索的 4.4 倍，但仅 23% 的营销人员投资 GEO。
- 🚀 **快速安装与兼容性** — 支持 macOS/Linux 和 Windows（Git Bash），提供一键安装脚本，Python 3.8+ 环境，依赖隔离安装，不影响系统 Python。
- 🛠️ **丰富命令与功能** — 提供 11 种命令，包括完整 GEO+SEO 审计、60 秒快速快照、AI 引用评分、爬虫访问检查、llms.txt 分析、品牌提及扫描、平台优化、结构化数据等。
- 🧩 **模块化架构** — 包含 13 个专业子技能和 5 个并行子代理，覆盖 AI 可见性、平台分析、技术 SEO、内容质量和 Schema 标记，支持并行分析提高效率。
- 📊 **评分体系** — 综合 GEO 评分（0-100 分），权重分配为 AI 引用与可见性 25%、品牌权威 20%、内容质量 20%、技术基础 15%、结构化数据 10%、平台优化 10%。
- 🔍 **核心功能亮点** — 引用评分（最佳段落 134-167 字）、AI 爬虫检测（14+ 种）、品牌提及扫描（10+ 平台）、平台优化（仅 11% 域被 ChatGPT 和 Google AIO 同时引用）、llms.txt 生成、PDF 报告生成。
- 💼 **商业应用场景** — 适用于 GEO 机构、营销团队、内容创作者、本地企业、SaaS 公司和电商，可生成客户就绪报告，社区提供变现策略（机构收费$2K-$12K/月）。
- 📝 **数据存储与卸载** — 运行时数据存储在`~/.geo-prospects/`目录，卸载脚本不删除用户数据，需手动清理。

---

### [GitHub - wiltodelta/remove-ai-watermarks: 用于从图像中移除可见（Gemini）和不可见（SynthID、C2PA、EXIF）AI 水印的命令行工具与库 · GitHub](https://github.com/wiltodelta/remove-ai-watermarks?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [GitHub - wiltodelta/remove-ai-watermarks: CLI and library for removing visible (Gemini) and invisible (SynthID, C2PA, EXIF) AI watermarks from images · GitHub](https://github.com/wiltodelta/remove-ai-watermarks?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

该工具是一个用于移除 AI 生成图像中可见与不可见水印的命令行库，支持多种主流 AI 模型，并集成了元数据清理和人脸保护功能。

- 🖼️ **支持多种 AI 模型** — 可移除 Google Gemini、ChatGPT/DALL-E、Stable Diffusion、Adobe Firefly、Midjourney 等模型的可见与不可见水印
- 🔍 **三阶段检测与移除** — 使用 NCC 检测器定位水印，通过反向 Alpha 混合移除可见水印，扩散模型再生移除不可见水印
- 🏷️ **元数据清理** — 剥离 C2PA、EXIF、XMP、PNG 文本块等 AI 生成元数据，消除“Made with AI”标签触发
- 🧑 **人脸保护功能** — 使用 YOLO 检测人脸，在扩散处理后自动融合原始人脸区域，防止 AI 变形
- 🎞️ **模拟人化处理** — 添加胶片颗粒和色差，使输出图像看起来像屏幕翻拍，绕过 AI 图像分类器
- ⚡ **批量处理与在线试用** — 支持整个目录批量处理，并提供免费在线服务 raiw.cc
- ⚖️ **法律合规说明** — 明确列出各司法管辖区法规，强调工具合法但使用需遵守当地法律，不适用于欺骗或伪造

---

### [Django 6.1 alpha 1 发布 | 博客 | Django](https://www.djangoproject.com/weblog/2026/may/20/django-61-alpha-1-released/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [Django 6.1 alpha 1 released | Weblog | Django](https://www.djangoproject.com/weblog/2026/may/20/django-61-alpha-1-released/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

Django 6.1 alpha 1 已发布，标志着新功能冻结，社区可参与测试以帮助完善最终版本。

- 🚀 Django 6.1 alpha 1 现已发布，代表 6.1 发布周期的第一阶段，供用户试用新功能。
- ✨ 新版本包含一系列新功能和可用性改进，详情见开发中的 6.1 发布说明。
- 🔒 此 alpha 版本标志着功能冻结，后续计划约一个月后发布 beta 版，再一个月后发布候选版。
- 🧪 该版本不适用于生产环境，但鼓励社区早期频繁测试，以帮助发现和修复错误。
- 📥 用户可从下载页面或 PyPI 获取 alpha 包，并将错误报告至问题追踪器。
- 🔑 此版本的 PGP 密钥 ID 为 Jacob Walls: 131403F4D16D8DC7。

---

### [PyData 伦敦 | 2026](https://pydata.org/london2026?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [PyData London | 2026](https://pydata.org/london2026?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

PyData London 2026 是一场为期三天的线下数据科学盛会，汇聚全球数据科学家、工程师和开发者，通过主题演讲、讲座和闪电演讲分享知识与经验。

- 📅 会议时间：2026 年 6 月 5 日至 7 日（周五教程，周六至周日讲座，每日主题演讲）
- 📍 会议地点：伦敦圣保罗大教堂附近的 Convene Sancroft（Sancroft, Rose St, Paternoster Sq., London EC4M 7DQ）
- 🎤 主题演讲嘉宾：Samuel Colvin（Pydantic 创始人，月下载量超 2.8 亿）、Rachel Lee-Nabors（Web 标准与开源领袖）、Jeremiah Lowin（Prefect 创始人，FastMCP 作者）、Martin O'Reilly（艾伦·图灵研究所研究工程总监）
- 🛠️ 活动内容：主题演讲、讲座、闪电演讲及社区交流，聚焦数据管理、处理、分析与可视化最佳实践
- 🌐 社区背景：PyData 全球网络支持 Python、Julia、R 等多语言数据科学方法，推动新兴技术与协作

---

### [“哦，你说得对”并非评论：能证明其核查内容的人工智能 - YouTube](https://www.youtube.com/watch?v=ekSs-SNVbgY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [“Oh, You’re Right” Is Not a Review: AI That Proves What It Checked - YouTube](https://www.youtube.com/watch?v=ekSs-SNVbgY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

本頁面涵蓋 YouTube 平台的主要資訊與政策，包括版權、聯絡方式、創作者支援、廣告、條款與隱私等核心內容。

- 📰 **新聞中心**：提供 YouTube 官方新聞與最新動態
- ©️ **版權**：說明版權相關規範與保護機制
- 📞 **聯絡我們**：提供用戶與創作者聯繫 YouTube 的管道
- 🎬 **創作者**：支援內容創作者的資源與工具
- 📢 **刊登廣告**：廣告主可在 YouTube 上投放廣告的相關資訊
- 👨‍💻 **開發人員**：提供 API 與技術整合的開發者資源
- 📜 **條款**：使用 YouTube 服務時需遵守的條款與條件
- 🔒 **私隱**：用戶資料保護與隱私權政策
- 🛡️ **政策及安全**：平台內容審核與安全規範
- ⚙️ **YouTube 的運作方式**：解釋平台推薦與內容管理機制
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能
- 🏢 **© 2026 Google LLC**：版權所有，歸 Google 所有

---

### [importlib.reload(phillypug)，2026 年 5 月 28 日周四下午 6:00 | Meetup](https://www.meetup.com/phillypug/events/314668753/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [importlib.reload(phillypug), Thu, May 28, 2026, 6:00 PM   | Meetup](https://www.meetup.com/phillypug/events/314668753/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

费城 Python 用户组（PhillyPUG）重启首次聚会，将于 5 月 28 日晚在宾夕法尼亚大学举行，包括技术演讲和社交活动。

- 🎉 活动由 Justin C.主办，PhillyPUG 在休整后重启，首次聚会定于 5 月 28 日下午 6 点至 8 点（美东时间）
- 📍 地点在宾夕法尼亚大学 Jon M. Huntsman Hall（3730 Walnut St, Philadelphia, PA）
- 🍕 赞助商包括沃顿商学院、Linode、PromptWorks 和 Mozilla，提供场地、披萨和演讲者
- 📅 议程安排：6:00-6:45 开门及社交，6:45-7:00 欢迎介绍，7:00-7:20 Docker for Python 用户演讲，7:20-7:40 Enum 深度解析演讲，7:40-8:30 自由交流
- 🗣️ 演讲者：Aaron Brock（S&P Global 生成式 AI 云安全总监，精通 Docker/K8s 等）和 Justin Chapman（Anuvi CTO，前 Meta 工程师，贡献于 ty 类型检查器）
- 🎤 活动征集演讲者，鼓励参与者分享想法或教学
- 🔗 相关主题包括费城活动、Python 和 Docker

---

### [PyData 柏林 2026 年 5 月聚会，2026 年 5 月 27 日（星期三）下午 6:00 | Meetup](https://www.meetup.com/pydata-berlin/events/314735843/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [PyData Berlin 2026 May Meetup, Wed, May 27, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-berlin/events/314735843/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

PyData Berlin 2026 年 5 月聚会将于 5 月 27 日 18:00-21:00 在 GetYourGuide 办公室举行，提供食物和饮品，需准时入场并实名注册。活动包含两场主题演讲和闪电演讲，遵循 NumFOCUS 行为准则。

- 🗓️ **活动时间地点**：5 月 27 日 18:00-21:00，GetYourGuide 办公室（Sonnenburger Str. 73），18:45 后禁止入场
- 🍕 **餐饮与注册**：提供免费食物饮品，需提供真实姓名注册，取消需及时释放名额
- 🎤 **演讲 1：Text2SQL 实战**：Oren Matar 讲解基于语义模型、RAG 搜索和智能验证循环的生产级 Text2SQL 系统
- 📊 **演讲 2：统计模型解读**：Juan Orduz 展示用 Bambi 和 PyMC 计算边际效应、预测和对比，将复杂模型转化为易懂结论
- ⚡ **闪电演讲**：2-3 个 3-5 分钟短演讲，欢迎报名
- 🤝 **行为准则**：要求友善、专业、包容，禁止骚扰或歧视性言论

---

### [PyData 布拉格 #35 - 可能不可靠的漏洞，2026 年 5 月 26 日星期二下午 6:00 | Meetup](https://www.meetup.com/pydata-prague/events/314798116/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [PyData Prague #35 - Probably unreliable vulnerabilities, Tue, May 26, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-prague/events/314798116/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

概述摘要  
PyData Prague 第 35 次聚会将于 5 月 26 日在 Aisle 办公室举行，主题聚焦 AI 安全漏洞与文本提取挑战，包含两场演讲及社交环节。

- 🔍 首场演讲：单文件 LLM 安全分析器的启示——探讨简单开源扫描器如何发现真实漏洞，同时指出其局限性（如误报、不一致性），强调验证与人工判断的重要性  
- 📄 第二场演讲：PDF 与 OCR 失效时如何获取可靠文本——揭示文本提取的隐藏复杂性，特别是交易文档对 OCR 的挑战，以及高质量输入对 LLM（如 Rossum 的 T-LLM）的关键作用  
- 🕐 活动时间：18:00 开始社交，18:30 正式演讲，设有休息和会后交流时段  
- 🤝 社区目标：欢迎不同技能水平的 Python 与数据爱好者参与，鼓励提交 5 分钟闪电演讲

---

### [BayPiggies 2026 年 5 月活动 - AI 代理 REPL、副业、PyCon | 2026 年 5 月 28 日周四下午 6:00 | Meetup](https://www.meetup.com/baypiggies/events/306320850/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [BayPiggies May 2026 - AI Agent REPLs, Side hustles, PyCon , Thu, May 28, 2026, 6:00 PM   | Meetup](https://www.meetup.com/baypiggies/events/306320850/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

BayPiggies 2026 年 5 月活动将于 5 月 28 日下午 6 点在 Palo Alto 的 SAP Labs 举行，主题涵盖 AI Agent REPLs、副业和 PyCon，需提前注册。

- 🗓️ **活动时间**：2026 年 5 月 28 日（周四）下午 6:00-8:00 PDT，比平时提前 30 分钟开始。
- 📍 **地点**：SAP Labs（3410 Hillview Ave, Palo Alto, CA），需提前注册并携带政府 ID。
- ⚠️ **重要提醒**：所有注册必须在 5 月 25 日（周一）午夜前完成，不接受现场报名。
- 🎤 **议程亮点**：包括 PyCon 2026 回顾、副业基础设施短讲，以及主题演讲“Give Your Agents REPLs”。
- 🏆 **社区动态**：宣布湾区新 PSF 研究员名单，以及 PyCon US 2026 将于 5 月 13-19 日在 Long Beach 举行。
- 🔒 **安全要求**：所有参与者需签署 SAP 保密与安全协议，并出示政府 ID。
- 💡 **支持方式**：可通过链接捐赠支持 Bay Area Python Association 和 Python Software Foundation。

---

### [PyData 华沙 #33 - Maksym Dibrov & Radek Sienkiewicz，2026 年 5 月 27 日星期三下午 6:00 | Meetup](https://www.meetup.com/pydata-warsaw/events/314516162/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [PyData Warsaw #33 - Maksym Dibrov & Radek Sienkiewicz , Wed, May 27, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-warsaw/events/314516162/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

PyData Warsaw #33 活动于 5 月 27 日在华沙举行，由 Mikołaj R.和 Rafał M.主持，包含两场技术演讲，主题涵盖 Python 微服务重构和自主 AI 代理实践。

- 🐍 **Maksym Dibrov** 分享如何将支付平台的 Reporting API 从 Java 重写为 Python，涉及架构决策、迁移挑战及数据工程经验。
- 🤖 **Radek Sienkiewicz** 介绍开源自主 AI 代理 OpenClaw 的架构、工具集成、技能扩展及实际工作流应用案例（如研究、编码、自动化）。
- 🏢 活动在 42 Warsaw（免学费编程学院）举办，强调项目驱动学习和社区互助。
- 🎯 相关主题包括人工智能、深度学习、数据科学和 Python，赞助商为 Continuum Analytics 和 Centrum Innowacji PW。

---

### [AI、智能体与 NASA：与 IBM 研究共度之夜，2026 年 5 月 28 日（周四）下午 6:00 | Meetup](https://www.meetup.com/pydataireland/events/314690159/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [AI, Agents & NASA: An Evening with IBM Research, Thu, May 28, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydataireland/events/314690159/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

概述总结
- 🤖 IBM Research 与 PyData Ireland 合作举办了一场关于 AI、智能体与 NASA 的晚间活动，聚焦自主系统在科学研究中的应用。
- 🚀 NASA 的 AKD 平台展示了多智能体后端如何通过聊天界面加速知识发现，实现可追溯的端到端科学研究。
- 🔒 Fabio Lorenzi 讲解了生产级 AI 智能体的构建，包括容器化、沙盒隔离及 LangChain 堆栈，用于工业时间序列分析。
- 📋 Michael Johnston 介绍了“ado”框架，通过结构化实验方案使智能体辅助研究透明、可重复且可审计。
- 🍕活动包括技术深度探讨、跨学科对话和披萨社交，旨在连接开放科学与 AI 基础设施。

---

### [PyDataMCR 五月活动，2026 年 5 月 28 日（周四）下午 6:30 | Meetup](https://www.meetup.com/pydata-manchester/events/314622186/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

**原文标题**: [PyDataMCR May, Thu, May 28, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-manchester/events/314622186/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-746-may-21-2026)

PyData Manchester 五月聚会将于 5 月 28 日在 Krakenflex 举办，包含两场技术演讲和社交活动，由 NumFOCUS 等赞助商支持。

- 🗓️ 活动时间：5 月 28 日（周四）18:30-20:30，地点在曼彻斯特 Krakenflex 办公室
- 🛡️ 演讲一：Dominic Duxbury 讲解如何用 Arroyo 和 Python API 处理家庭网络流量，结合现代网络安全原则
- 🔧 演讲二：Sean Borg 探讨 Python 对 C 语言的依赖是否正在被削弱，分析高性能库的底层支持
- 🍕 活动提供餐饮，容量限制 90 人，结束后有社交环节
- 📜 遵守 NumFOCUS 行为准则，要求专业行为，16 岁以下需监护人陪同
- 🤝 赞助商包括 NumFOCUS、AutoTrader、Kraken 和 Horsefly Analytics

---

