### [指导委员会关于 JIT 项目的公告 - 核心开发 - Python.org 讨论](https://discuss.python.org/t/an-announcement-from-the-steering-council-regarding-the-jit-project/107638?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [An announcement from the Steering Council regarding the JIT project - Core Development - Discussions on Python.org](https://discuss.python.org/t/an-announcement-from-the-steering-council-regarding-the-jit-project/107638?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

## 概述总结
Python 指导委员会正式要求为 CPython 的 JIT 编译器提交一份标准 PEP，以决定其是否成为永久特性，并设定了六个月的提交期限。

- 📢 **指导委员会正式要求**：Python 指导委员会要求为 JIT 编译器撰写一份标准 PEP，以明确其作为 CPython 永久特性的地位、维护承诺和对下游分发者的影响。
- ⏸️ **暂停新开发**：在 PEP 被接受前，禁止在 main 分支上添加 JIT 的新功能、优化和性能改进，仅允许进行错误修复和安全补丁。
- ⏰ **六个月期限**：若在六个月内没有 PEP 被提交并解决，JIT 代码必须从 main 分支移除，开发转移到 CPython 主仓库之外。
- 📋 **PEP 需涵盖的关键点**：包括长期维护计划、与现有 CPython 工具（如自由线程、分析器、调试器）的兼容性、可衡量的成功指标（性能目标、平台覆盖、内存开销）、与其他 JIT（如 CinderX、Numba、PyTorch）的关系，以及当前 JIT 架构的稳定性。
- 🤝 **社区参与**：社区成员如 Diego Russo 已表示愿意协调 PEP 的撰写，并邀请其他人参与作者、审阅者或提供相关领域输入。
- 💬 **开发者反馈**：JIT 开发者 Mark Shannon 请求在 PEP 讨论期间给予一两个月的宽限期，以继续开发并避免失去动力，但指导委员会倾向于立即暂停新开发以保持讨论焦点。

---

### [使用 MicroPython 和 WASM 在沙箱中运行 Python 代码](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [Running Python code in a sandbox with MicroPython and WASM](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

Simon Willison 发布了 `micropython-wasm` 实验性沙箱库，用于在 Python 应用中安全运行代码。

- 🧪 **新工具发布**：推出 `micropython-wasm` 库，将 MicroPython 编译为 WebAssembly，通过 wasmtime 在 Python 中安全执行代码。
- 🔒 **沙箱需求明确**：插件系统（如 Datasette、LLM）需要隔离恶意或错误代码，防止文件泄露、网络访问和资源耗尽。
- 🛡️ **沙箱核心特性**：需支持 PyPI 安装、内存/CPU 限制、严格文件与网络控制、可自定义宿主函数，且需长期维护。
- 🌐 **WebAssembly 优势**：WASM 天然支持内存隔离和资源限制，wasmtime 库提供 Python 绑定且持续维护，比直接嵌入 V8 更可靠。
- ⚙️ **实现细节**：通过线程和队列实现持久化会话，支持跨调用保留变量；C 代码（78 行）实现宿主函数接口，编译后 WASM 文件仅 362KB。
- 🚀 **快速原型**：借助 GPT-5.5 和 Codex 从研究到原型仅用数小时，但作者承认是“vibe-coded”，目前仅作 alpha 发布。
- 🧪 **测试与风险**：已通过 GPT-5.5 挑战尝试逃逸沙箱均失败，但作者强调不推荐用于生产环境，期待专业团队改进。
- 💻 **试用方式**：可通过 `uvx micropython-wasm -c 'print("Hello world")'` 直接体验，或集成到 Datasette Agent 中。

---

### [你可以构建的最小大脑 | Devarsh Ranpara](https://ranpara.net/posts/perceptron-explained-from-scratch/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [The Smallest Brain You Can Build | Devarsh Ranpara](https://ranpara.net/posts/perceptron-explained-from-scratch/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

### 概述摘要  
本文从零开始用 Python 构建感知机，通过交互式演示讲解权重、偏置、决策边界、训练轮次、学习率和数据归一化等核心概念。

- 🧠 **感知机是最小的人工神经网络**：输入一个数值，输出“是/否”判断，是 1958 年 Frank Rosenblatt 受生物神经元启发而发明。
- ⚖️ **决策机制类似人类权衡**：输入值乘以权重后求和，加上偏置，若结果大于 0 则输出 1（真），否则为 0（假）。
- 📏 **决策边界决定分类位置**：边界公式为 `-bias/weight`，偏置的作用是让边界能移动到任意位置（如学生及格线 50 分处），没有偏置时边界被固定在 0。
- 🔄 **学习过程通过误差修正**：预测错误时，根据误差大小和学习率调整权重和偏置，公式为 `weight += learning_rate * error * value`。
- ⏱ **训练轮次与学习率**：一个完整数据遍历称为一轮（epoch），更多轮次提高准确率；学习率控制修正步长，过大易震荡，过小收敛慢。
- 📊 **数据归一化提升训练效果**：将输入缩放到小范围（如 0-1），避免大数值（如 100 分）主导权重更新，使训练更平滑快速。
- 🐍 **完整 Python 实现仅需几十行**：包含随机初始化、训练循环、决策边界计算，修改数据即可适配不同分类任务。
- 🧩 **感知机是神经网络的基础**：单个神经元只能画一条直线，但多个堆叠可形成能学习复杂模式的深度网络。

---

### [使用 OpenTelemetry 观察 LLM 应用——开发者指南 [2026] | SigNoz](https://signoz.io/blog/opentelemetry-llm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [Observing LLM Applications with OpenTelemetry-The Developer's Guide [2026] | SigNoz](https://signoz.io/blog/opentelemetry-llm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

本指南詳細說明了如何使用 OpenTelemetry 監控 LLM 應用程式，並透過 SigNoz 進行可視化。

- 📖 **概述與動機**：LLM 應用程式的非確定性輸出、上下文一致性與模型更新等挑戰，使得可觀測性至關重要。OpenTelemetry 作為 CNCF 標準化專案，可避免供應商鎖定。
- 🛠️ **實作設定**：使用 Python 3.12、FastAPI 與 OpenAI Agents SDK 建立 NBA 記者代理。透過 `opentelemetry-instrument` 自動埋點，並將資料導向 SigNoz 雲端實例。
- ⚙️ **GenAI 標準現狀**：OpenTelemetry 的 GenAI 語意慣例仍在快速發展中（`gen_ai.*` 前綴），部分工具如 `opentelemetry-bootstrap` 尚未完全支援最新 SDK，需手動安裝依賴。
- 🧠 **代理工作流程**：定義了包含系統提示、工具（網路搜尋、勝率計算）與輸入護欄的 NBA 代理。護欄可攔截離題問題，並透過 FastAPI 例外處理器記錄。
- 🔍 **追蹤可視化**：SigNoz 的追蹤詳細圖可展示代理工作流程的每一步，包括 API 呼叫、護欄檢查與例外事件。部分內部路徑顯示為 `unknown`，但相關 PR 正在改善。
- 📊 **指標與監控**：自動暴露 `gen_ai.client.operation.duration` 與 `gen_ai.client.token.usage` 等指標，可用於建構儀表板監控 Token 消耗與呼叫量。

---

### [DynamoDB 中的有序键分片 - 死亡与重力](https://death.andgravity.com/albumtitle?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [Ordered key sharding in DynamoDB - death and gravity](https://death.andgravity.com/albumtitle?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

本篇文章探討了在 DynamoDB 中實現有序索引分片的多種解決方案，並通過數學計算和實際數據分析找出最佳方法，以應對吞吐量限制和數據分佈不均的問題。

- 📊 **需求分析**：需要一個 GSI 支援 10,000 次查詢/秒、10,000 次寫入/秒，且結果按字母排序，但單個分區無法滿足吞吐量需求（讀取需 21 倍、寫入需 5 倍）。
- 🔍 **稀疏索引方案**：使用稀疏索引可高效列出專輯，但掃描結果無序，無法滿足排序要求。
- 🧩 **單一分區鍵方案**：使用單一分區鍵和排序鍵可實現排序，但會因分區限制導致節流（讀取需 21 倍吞吐量）。
- 🎲 **隨機後綴分片**：隨機分片可分散負載，但無法按標題排序，因相同標題可能分佈在不同分片。
- 🔑 **哈希後綴分片**：哈希函數確保相同標題在同一分片，但無法實現跨分片排序。
- 🔤 **首字母分片**：使用首字母作為分片 ID，但 Unicode 字符過多（5402 個），且分佈不均，部分首字母需多個分片。
- 🧮 **前綴範圍分片**：通過將排序後的標題分割成等量範圍，並使用前綴邊界，可實現有序查詢，但需預先知道數據分佈。
- 🌐 **數據分佈變化**：前綴分佈可能隨時間改變（如新增大量非拉丁語系專輯），需預留更多分片或準備遷移方案。

---

### [你现在真的需要运行五个类型检查器吗？| Pyrefly](https://pyrefly.org/blog/too-many-type-checkers/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [Are you really expected to run five type-checkers now? | Pyrefly](https://pyrefly.org/blog/too-many-type-checkers/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

### 概述总结
文章讨论了 Python 库维护者面对多个类型检查器（Mypy、Pyrefly、Pyright、ty、Zuban）时的挑战，并提出优先在测试套件中运行多个类型检查器，而非在源代码上，以更好地服务用户。

- 🧩 **核心问题**：库维护者需在源代码上运行多个类型检查器，但不同工具对类型注解要求不一致，导致代码被大量`type: ignore`注释污染。
- 🔄 **反向思维**：应优先在测试套件中运行多个类型检查器，测试公共 API 的兼容性，而非仅关注内部代码逻辑。
- 📊 **Polars 案例**：通过测试套件验证所有类型检查器对公共 API 的一致性，而非强制统一内部实现，可减少维护成本。
- ⚙️ **类型检查器差异**：不同检查器在严格性上存在差异（如 Pyrefly 更严格），用户应根据需求选择，但库维护者需确保公共 API 兼容主流工具。
- ✅ **最佳实践**：在测试中运行尽可能多的类型检查器，确保用户无论使用哪种工具都能获得正确类型推断；源代码可优先选择一种工具（如 Pyrefly）进行优化。

---

### [展示 allauth IdP：构建 MCP 服务器 | allauth](https://allauth.org/news/2026/05/idp-demo-mcp-server/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [Showcasing allauth IdP: build an MCP server | allauth](https://allauth.org/news/2026/05/idp-demo-mcp-server/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

本教程展示了如何使用 Django 和 django-allauth 搭建一个支持 OIDC 认证的 MCP 服务器，整个过程简单透明，无需第三方付费服务。

- 🔧 **项目搭建**：使用 `uv` 初始化项目，安装 Django 和 `django-allauth[idp-oidc]`，并创建项目骨架。
- ⚙️ **allauth 配置**：在 `settings.py` 中添加 `allauth`、`allauth.account`、`allauth.idp.oidc` 应用及中间件，设置认证后端，并配置 URL 路由。
- 🔑 **IdP 专属设置**：生成 RSA 私钥用于令牌签名，启用动态客户端注册（DCR）并关闭初始访问令牌要求。
- 🚀 **MCP 服务器实现**：创建 `/mcp` 端点，实现 JSON-RPC 方法（initialize、tools/list、tools/call），并添加 OIDC 令牌认证装饰器。
- 🖥️ **演示流程**：创建 `.mcp.json` 配置文件，通过 MCP 主机进行 OIDC 认证（注册/登录），授权后调用 `lost_numbers` 工具获取幸运数字。
- ✅ **结论与支持**：整个方案完全集成在 Django 项目中，无需第三方服务；鼓励赞助项目以支持持续开发。

---

### [使用 Redis 和 Docker 的 django-q2 - 用于后台任务！ - YouTube](https://www.youtube.com/watch?v=wjSFMK_IZS8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [django-q2 with Redis & Docker - for Background Tasks! - YouTube](https://www.youtube.com/watch?v=wjSFMK_IZS8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

本頁面為 YouTube 平台相關資訊的導覽目錄，涵蓋法律、商業、創作與平台運作等核心面向。

- 📰 新聞中心：提供 YouTube 官方最新消息與公告。
- ©️ 版權：說明內容創作者的版權保護與管理機制。
- 📞 聯絡我們：提供用戶與 YouTube 官方聯繫的管道。
- 🎬 創作者：為內容創作者提供資源與支援。
- 📢 刊登廣告：介紹在 YouTube 上投放廣告的選項與服務。
- 👨‍💻 開發人員：提供 API 與技術文件給開發者使用。
- 📄 條款：列出使用 YouTube 服務所需遵守的條款與條件。
- 🔒 私隱：說明 YouTube 如何收集與使用用戶資料。
- 🛡️ 政策及安全：闡述平台內容審查與安全規範。
- ⚙️ YouTube 的運作方式：解釋平台推薦演算法與內容分發機制。
- 🧪 測試新功能：說明 YouTube 如何測試與推出新功能。
- ©️ 2026 Google LLC：標示版權歸屬與法律聲明。

---

### [用于 Python Polars 工作流的库 :: Posit 开源](https://opensource.posit.co/blog/2026-06-04_libraries-for-python-polars/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [Libraries for your Python Polars workflows :: Posit Open Source](https://opensource.posit.co/blog/2026-06-04_libraries-for-python-polars/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

Polars 是一个基于 Rust 构建的高效 Python 数据操作库，Posit 提供了四个强大的 Python 库来支持 Polars DataFrame 的完整数据科学工作流程。

- ✅ **pointblank**：用于数据验证和质量检查，可直接对 Polars DataFrame 执行空值检查、数值范围验证、集合成员检查等操作。
- 📊 **Great Tables**：创建出版级质量的表格，支持货币格式化、数字格式化、迷你图、列标签、颜色样式和字体大小调整等功能。
- 📈 **plotnine**：基于图形语法的可视化库，可无缝与 Polars 配合使用，创建带标签、货币轴、自定义主题的图表。
- 🤖 **mall**：集成 LLM 能力，通过 `.llm` 访问器实现自然语言分类、情感分析、摘要、提取、翻译和验证等操作。

---

### [GitHub - pewdiepie-archdaemon/odysseus: 自托管 AI 工作空间。](https://github.com/pewdiepie-archdaemon/odysseus?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - pewdiepie-archdaemon/odysseus: Self-hosted AI workspace. · GitHub](https://github.com/pewdiepie-archdaemon/odysseus?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

Odysseus 是一个自托管的 AI 工作空间，旨在提供类似 ChatGPT 和 Claude 的本地优先、隐私优先的 UI 体验，支持多种模型和工具。

- 🤖 **核心功能**：支持聊天、智能代理（可调用工具）、深度研究、模型对比、文档编辑、记忆/技能、邮件、笔记/任务、日历等。
- 🐳 **快速部署**：推荐使用 Docker 部署，克隆仓库后运行 `docker compose up -d --build` 即可，默认端口 7000。
- 🖥️ **多平台支持**：支持 Docker、原生 Linux/macOS、Apple Silicon（原生运行）、Windows（通过 PowerShell 脚本）。
- 🎨 **模型与工具**：集成 vLLM、llama.cpp、Ollama、OpenAI 等，支持 MCP 服务器、Cookbook（硬件扫描推荐模型）、网页搜索、文件上传等。
- 🔒 **安全与隐私**：默认启用身份验证，数据本地存储，不暴露端口到公网，支持 HTTPS 和反向代理。
- ⚙️ **高度可配置**：通过 `.env` 文件设置部署参数，如端口、数据库、认证、上传限制等，大部分配置可在应用内完成。
- 📱 **移动端友好**：响应式设计，支持 PWA 安装和触控手势，可在手机上流畅使用。
- 🧩 **扩展性**：支持自定义 MCP 服务器、可选依赖（如 Whisper 语音转文字、PyMuPDF 文档渲染），社区贡献活跃。

---

### [GitHub - google/skills: 谷歌产品与技术的智能体技能 · GitHub](https://github.com/google/skills?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - google/skills: Agent Skills for Google products and technologies · GitHub](https://github.com/google/skills?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

该仓库是 Google 发布的“Agent Skills”开源项目，包含一系列用于 Google 产品与技术的技能模块，支持通过 npx 命令安装，并鼓励社区贡献。

- 📦 **项目概述**：Google/skills 仓库提供 Agent Skills，涵盖 Google Cloud、Flutter、Dart 等产品，当前处于活跃开发阶段。
- 🛠️ **安装方式**：使用命令`npx skills add google/skills`即可从该仓库选择并安装所需技能。
- 📋 **可用技能列表**：包括 Gemini API、AlloyDB、BigQuery、Cloud Run、Cloud SQL、Firebase、Kubernetes Engine 等基础技能，以及 Google Cloud 上手指南、身份验证、网络可观测性等配方。
- 🏗️ **架构框架**：提供 Google Cloud Well-Architected Framework 技能，涵盖安全性、可靠性、成本优化、运营卓越、性能优化和可持续性六大支柱。
- 🌐 **其他技能**：额外包含 Flutter 和 Dart 相关技能。
- 🤝 **社区贡献**：欢迎通过 GitHub Issue 报告错误、提出新技能建议或提交改进。
- 📄 **许可协议**：采用 Apache 2.0 开源许可证，允许自由复制、修改和分发。
- 📊 **项目数据**：获得 13.5k 星标、1k 分支、91 位关注者，主要使用 Python（97.1%）和 Shell（2.9%）语言。

---

### [GitHub - anthropics/defending-code-reference-harness：威胁建模、扫描、分类、修补技能，以及可自定义的自主扫描工具](https://github.com/anthropics/defending-code-reference-harness?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - anthropics/defending-code-reference-harness: Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize · GitHub](https://github.com/anthropics/defending-code-reference-harness?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

该仓库是 Anthropic 发布的一个开源参考实现，用于利用 Claude 自主发现和修复代码漏洞，并提供了从快速上手到深度定制的完整指南。

- 🔒 **项目定位**：一个开源的自主漏洞发现与修复参考实现，基于 Claude，不维护也不接受贡献，但提供托管产品 Claude Security 作为替代。
- 🛠️ **核心组件**：包含交互式技能（威胁建模、扫描、分类、打补丁）和自主管道（侦察→发现→验证→报告→修复），专为 C/C++ 内存漏洞设计。
- 🚀 **快速上手**：建议从 Day 1 的交互式技能开始，逐步过渡到自主管道运行，遵循“小步快跑”原则，最快一周内实现自主扫描。
- ⚙️ **管道流程**：七阶段自主管道（构建、侦察、发现、验证、去重、报告、补丁），每个阶段在隔离的 gVisor 容器中运行，确保安全。
- 🔧 **自定义扩展**：通过 `/customize` 技能可轻松将管道移植到其他语言、漏洞类型或目标代码库，只需调整构建、信号和 PoC 定义。
- 📈 **进阶应用**：第二周可建立外层循环（多次扫描→分类→优先修复），并建议将扫描集成到 SDLC 中，持续迭代优化。

---

### [GitHub - RyanCodrai/turbovec：基于TurboQuant构建的向量索引，使用Rust编写并带有Python绑定](https://github.com/RyanCodrai/turbovec?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - RyanCodrai/turbovec: A vector index built on TurboQuant, written in Rust with Python bindings · GitHub](https://github.com/RyanCodrai/turbovec?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

turbovec 是一个基于 TurboQuant 算法的高效向量索引工具，用 Rust 编写并提供 Python 绑定，能以极低内存消耗（如 10M 文档仅需 4GB RAM）实现快速搜索，比 FAISS 更快或相当，并支持在线添加、过滤搜索和纯本地运行。

- 🚀 **极致压缩与速度**：将 10M 文档从 31GB（float32）压缩至 4GB，搜索速度比 FAISS 快 10–19%（ARM）或领先 4-bit 配置（x86）。
- 📦 **在线添加，无需训练**：向量添加即索引，无训练阶段、无参数调整、无重建，支持动态增长。
- 🔍 **高效过滤搜索**：通过 ID 允许列表或位掩码在 SIMD 内核中直接过滤，避免过度获取，确保结果精确。
- 🛡️ **纯本地与隐私保护**：无需托管服务，数据不离开机器或 VPC，适合构建气隙 RAG 系统。
- 🐍 **Python 与 Rust 双支持**：提供 `pip install turbovec` 和 `cargo add turbovec`，集成 LangChain、LlamaIndex 等框架。
- ⚙️ **核心技术**：通过随机旋转、Beta 分布校准、Lloyd-Max 量化及长度重归一化，实现近最优失真和低偏差内积估计。
- 📊 **卓越性能基准**：在 d=1536 和 d=3072 上，TurboQuant 在 2-bit 和 4-bit 下召回率优于 FAISS，且压缩比高达 16 倍。

---

### [GitHub - alistaitsacle/free-llm-api-keys: 免费获取 GPT-5.5、Claude、DeepSeek、Gemini、Grok 的 LLM API 密钥——复制、粘贴、使用。每日更新 3-5 次。无需信用卡。](https://github.com/alistaitsacle/free-llm-api-keys?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - alistaitsacle/free-llm-api-keys: Free LLM API keys for GPT-5.5, Claude, DeepSeek, Gemini, Grok — copy, paste, use. Updated 3-5x daily. No credit card needed. · GitHub](https://github.com/alistaitsacle/free-llm-api-keys?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

这是一个提供免费 LLM API 密钥的开源项目，无需信用卡或注册即可使用，密钥每日更新，支持多种主流模型。

- 🔑 免费获取 GPT-5.5、Claude、DeepSeek、Gemini 等 90 多种模型的 API 密钥，无需信用卡或注册，直接复制粘贴即可使用。
- 🆕 密钥每日多次更新，每个密钥有$20-$100 的预算，24-48 小时内有效，过期自动清理。
- 🎁 每日在 X 平台（@getkeyway）发放 AI API 赠款，提供少量私有的 24 小时 API 密钥。
- 🛠️ 所有密钥兼容 OpenAI SDK 格式，支持聊天、图像生成（DALL-E 3）、文本转语音（TTS）和嵌入模型。
- 🌐 支持全球访问，在中国可直接使用，无需 VPN。
- 📊 提供详细的密钥状态、预算、速率限制和过期时间表格，方便用户选择。
- 🚀 项目旨在降低 AI API 使用门槛，特别惠及学生、爱好者和开发受限地区的用户。

---

### [GitHub - Andyyyy64/whichllm：找到在你的硬件上真正运行且性能最佳的本地大语言模型。基于真实且考虑时效性的基准测试排名，而非参数数量。一条命令，即刻运行。](https://github.com/Andyyyy64/whichllm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - Andyyyy64/whichllm: Find the local LLM that actually runs and performs best on your hardware. Ranked by real, recency-aware benchmarks, not parameter count. One command, run it instantly. · GitHub](https://github.com/Andyyyy64/whichllm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

whichllm 是一个开源命令行工具，能自动检测你的硬件（GPU/CPU/RAM），并从 HuggingFace 实时排名最适合你设备的本地大语言模型（LLM）。

- 🔍 **自动硬件检测** — 支持 NVIDIA、AMD、Apple Silicon 和纯 CPU 模式，自动识别 GPU 型号和显存
- 🏆 **智能评分排名** — 基于 LiveBench、Arena ELO 等真实基准，结合置信度、时效性和硬件适配度综合打分，而非只看参数大小
- ⚡ **一键运行与代码片段** — `whichllm run` 直接下载模型并启动聊天，`whichllm snippet` 输出可直接运行的 Python 代码
- 🎮 **GPU 模拟与规划** — `--gpu "RTX 4090"` 模拟购买前的硬件表现，`whichllm plan "llama 3 70b"` 反向查找所需 GPU
- 📊 **JSON 输出与脚本集成** — 支持 `--json` 输出，方便与 `jq` 等工具组合使用，适合自动化流程
- 🧠 **架构感知估算** — 准确估算 VRAM 占用（权重+KV 缓存 + 激活 + 开销）和推理速度（考虑量化、MoE、后端等因素）
- 🔄 **实时数据与缓存** — 直接从 HuggingFace API 获取模型，带 TTL 缓存，离线也有备用数据
- 🛠️ **多格式支持** — 兼容 GGUF、AWQ、GPTQ、FP16/BF16 等多种模型格式
- 📈 **升级比较** — `whichllm upgrade "RTX 4090" "RTX 5090"` 对比不同 GPU 的模型运行效果

---

### [GitHub - maziyarpanahi/openmed: 开源医疗人工智能 · GitHub](https://github.com/maziyarpanahi/openmed?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - maziyarpanahi/openmed: open-source healthcare ai · GitHub](https://github.com/maziyarpanahi/openmed?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

OpenMed 是一个本地优先的开源医疗 AI 工具，能在设备端运行，无需联网即可将临床文本转化为结构化数据，支持实体提取、PII 去标识化，并提供 1000+ 专业医疗模型。

- 🏥 完全本地运行：所有处理在设备端完成，患者数据永不离开本地网络，支持离线/气隙环境
- 🧬 1000+ 专业模型：涵盖疾病、药物、基因、解剖等医疗领域，许多模型性能超越商业方案
- 🛡️ PII 去标识化：覆盖 HIPAA 全部 18 项安全港标识符，支持智能实体合并和格式保留的伪造数据
- 🌍 多语言支持：12 种语言，247 个 PII 检查点，包括英语、中文、西班牙语、法语等
- 🚀 多平台兼容：支持 CPU、CUDA、Apple Silicon（MLX），原生集成 iOS/macOS 应用（OpenMedKit）
- 🎯 一键部署：Python API、Docker 化 REST 服务、批处理管道，代码简洁易用
- 🔓 零锁定：Apache-2.0 许可证，完全自主掌控基础设施和数据
- ⚡ 高性能：MLX 加速下比 CPU PyTorch 快 24-33 倍，批处理吞吐量提升 3.3 倍
- 📚 丰富文档：提供完整指南、模型注册表、PII 检测教程、批处理配置等

---

### [GitHub - NVIDIA/SkillSpector：AI代理技能安全扫描器。检测漏洞、恶意模式和安全风险。· GitHub](https://github.com/NVIDIA/SkillSpector?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - NVIDIA/SkillSpector: Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks. · GitHub](https://github.com/NVIDIA/SkillSpector?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

NVIDIA 的 SkillSpector 是一个专门用于检测 AI 代理技能安全性的扫描工具，可识别漏洞、恶意模式和风险，帮助用户判断技能是否安全安装。

- 🔍 **多格式输入支持**：可扫描 Git 仓库、URL、压缩包、目录或单个文件，灵活适配不同场景。
- 🛡️ **64 种漏洞模式**：覆盖 16 个类别，包括提示注入、数据窃取、权限提升、供应链攻击等，并支持实时 CVE 查询。
- ⚡ **两阶段分析**：先进行快速静态分析（正则匹配 + AST 分析），再可选进行 LLM 语义评估，提升准确率至约 87%。
- 📊 **风险评分系统**：根据严重程度（低/中/高/严重）计算 0-100 分，并给出“安全”、“谨慎”或“请勿安装”的明确建议。
- 📝 **多种输出格式**：支持终端、JSON、Markdown 和 SARIF 格式，便于集成到 CI/CD 或 IDE 中。
- 🤖 **LLM 集成**：支持 OpenAI、Anthropic 和 NVIDIA 的模型，可进行语义分析，并内置防越狱保护。
- 🧪 **研究背景**：基于对 42,447 个技能的大规模研究，发现 26.1% 存在漏洞，5.2% 有恶意意图。
- 🐍 **Python API**：提供 LangGraph 工作流接口，方便在代码中直接调用扫描功能。
- 📦 **开源与贡献**：基于 Apache 2.0 许可证，欢迎社区贡献和提交问题。

---

### [GitHub - symbolica-dev/symbolica: Symbolica 是一个高性能的计算机代数库，适用于 Python 和 Rust。以前所未有的速度处理大型表达式、匹配模式并生成优化的数值代码。](https://github.com/symbolica-dev/symbolica?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - symbolica-dev/symbolica: Symbolica is a high-performance computer algebra library for Python and Rust. Manipulate large expressions, match patterns, and generate optimized numerical code — at unprecedented speed. · GitHub](https://github.com/symbolica-dev/symbolica?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

Symbolica 是一个高性能的计算机代数库，支持 Python 和 Rust，专为大型表达式、符号重写、精确多项式运算和优化数值求值而设计，被 CERN 等研究机构采用。

- 🎯 **核心功能**：提供原生 Python 和 Rust API，支持符号计算、模式匹配、多项式算术和数值代码生成（JIT、C++、SIMD 等）
- ⚡ **性能优势**：针对大规模符号工作负载优化，支持混合精确/数值计算和错误传播，以及超大型表达式的流式处理
- 📦 **安装便捷**：Python 用户可通过`pip install symbolica`安装，Rust 用户使用`cargo add symbolica`
- 🔧 **应用示例**：通过摆锤校准案例展示符号操作、级数展开、线性系统求解和数值求值的完整工作流
- 🌍 **社区与开发**：在 Zulip 上开源开发，拥有 879 颗星标、46 个分支，最新版本为 Symbolica 2.0.0
- 📚 **资源支持**：提供在线 Jupyter Notebook 演示、完整文档和官方网站 symbolica.io

---

### [GitHub - marin-community/marin: 用于基础模型研究与开发的开源框架。](https://github.com/marin-community/marin?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [GitHub - marin-community/marin: Open-source framework for the research and development of foundation models. · GitHub](https://github.com/marin-community/marin?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

Marin 是一个开源框架，用于基础模型的研究与开发，特别注重可重复性和透明度。

- 📚 **核心定位**：Marin 是一个开源框架，专注于基础模型（如 Llama、DeepSeek、Qwen 等语言模型）的研究与开发。
- 🔄 **强调可重复性**：框架记录从原始数据到最终模型的每一步，包括失败的实验，确保整个研究过程透明。
- 🏆 **实际成果**：已用于训练首个超越 Llama 3.1 8B 的开源 8B 参数模型。
- 🛠️ **功能范围**：支持数据整理、转换、过滤、分词、训练和评估等完整流程。
- 📖 **文档与入门**：提供 ReadTheDocs 文档和 docs/ 文件夹，并有安装指南、小模型训练教程和更大规模实验示例。
- 💻 **实验定义**：实验通过类似 Makefile 的步骤依赖关系定义，按拓扑顺序执行，示例展示了从 TinyStories 数据集分词到模型训练的完整脚本。
- 🤖 **代理技能**：包含 .agents/skills/ 目录，提供如添加新数据集的逐步指南。
- 🌐 **社区与资源**：拥有 Discord 社区，GitHub 仓库获得 1.1k 星标、133 个复刻，采用 Apache-2.0 许可证。

---

### [SF Python 六月活动在 Sentry，2026 年 6 月 17 日（周三）下午 6:30 | 聚会](https://www.meetup.com/sfpython/events/314357825/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [SF Python June at Sentry, Wed, Jun 17, 2026, 6:30 PM   | Meetup](https://www.meetup.com/sfpython/events/314357825/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

本次 SF Python 六月活动由 Sentry 主办，旨在促进 Python 社区交流，包含两场技术演讲和社交环节。

- 📅 活动时间：6 月 17 日周三，下午 6:30 至 8:30（太平洋夏令时）
- 📍 地点：旧金山 Fremont 街 45 号，Sentry 办公室
- 🎤 演讲一：《寻求验证：Pydantic 入门》——Liz Acosta，介绍数据验证库 Pydantic 的优势、挑战及实际用例
- 🎤 演讲二：《使用 Phemeral 简化 Python 托管与零扩展》——Chinmaya Joshi，演示 Python Web 服务的持续部署与自动伸缩
- 📋 议程：6:30 社交、7:00 开场致辞、7:10 演讲与问答、8:30 总结与继续交流
- 🏢 主办方：SF Python 志愿者组织，致力于湾区 Python 社区发展
- 🔗 注册链接：ti.to/sfpython/jun-sf-python-sentry
- 💡 提交演讲提案：bit.ly/bapyacfp

---

### [Python 适用于（几乎）一切，2026 年 6 月 18 日星期四下午 4:00 | Meetup](https://www.meetup.com/python-stlouis/events/313870807/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [Python for (Almost) Everything, Thu, Jun 18, 2026, 4:00 PM   | Meetup](https://www.meetup.com/python-stlouis/events/313870807/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

本次 PySTL 周年迷你会议聚焦 Python 在多个领域的广泛应用，涵盖数据工程、量子计算、可观测性和地理空间计算机视觉等主题。

- 🎉 庆祝 PySTL 一周年，在 Downtown TREX 举办迷你会议
- 🗣️ 邀请行业专家、研究人员和学生分享 Python 应用经验
- 🌐 主题涵盖 Web 开发、地理空间、人工智能等多个领域
- 🍕 提供免费披萨和啤酒，促进社交交流
- ⏰ 活动安排包括开放社交、主题演讲和两个时段的并行讲座
- ☁️ 讲座 1：Python 在云数据工程中的应用（Scott Anderson）
- 🔬 讲座 2：Python 在量子计算中的角色（Aayush Gauba）
- 📊 讲座 3：使用 OpenTelemetry 实现 Python 可观测性（David Hoover）
- 🛰️ 讲座 4：地理空间计算机视觉技术（Kevin Lai）
- 🤝 赞助方包括 Python 软件基金会和 Manning Publishing
- 🏙️ 合作伙伴包括圣路易斯多个技术社区

---

### [不止于匹配：Python 中结构模式匹配的魔力，2026 年 6 月 16 日星期二下午 5:45 | Meetup](https://www.meetup.com/pyrvausergroup/events/313703905/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [More than a match The magic that is structural pattern matching in Python, Tue, Jun 16, 2026, 5:45 PM   | Meetup](https://www.meetup.com/pyrvausergroup/events/313703905/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

概述摘要
Python 结构模式匹配的神奇之处远超简单的`match`语句，本次互动会议将深入探讨其强大功能。

- 🐍 Python 3.10 引入的结构模式匹配已存在四年半，远超开发者认知的`match`语句
- 🔍 互动式代码探索环节，鼓励携带笔记本电脑实时实践
- 📅 活动时间：每月第三个星期二（6 月 16 日下午 5:45-7:45），含社交和正式环节
- 🏢 地点：弗吉尼亚州里士满 Ippon Technologies（提供免费停车）
- 👥 面向所有技能水平开放：新手可提问学习，资深开发者可分享经验
- 💬 通过 Discord 社区（pyrva.org/discord）保持联系
- 🎤 欢迎赞助或报名演讲（pyrva.org/donate / 在线表单）

---

### [PyData 利兹：六月聚会，2026 年 6 月 16 日星期二下午 5:30 | Meetup](https://www.meetup.com/pydata-leeds/events/314891165/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [PyData Leeds: June Meet-up, Tue, Jun 16, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-leeds/events/314891165/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

PyData Leeds 六月聚会将于 2026 年 6 月 16 日在利兹举行，包含两场精彩演讲和社交环节。

- 📅 **活动时间与地点**：2026 年 6 月 16 日（周二）17:30-20:30，地点为利兹 Aire Street 的 Brew Society（Hippo 活动空间）。
- 🎤 **第一场演讲**：Obinna Iheanachor 分享“本地优先 AI”方法，通过 PyMuPDF 等工具本地处理文档，仅将不确定案例发送至云端，降低成本和延迟。
- 🤖 **第二场演讲**：Fay Churchill 探讨数据科学领导力在 GenAI 热潮中的挑战，强调聚焦业务问题、避免技术炒作。
- 🍻 **活动流程**：17:30 社交茶歇，18:00 欢迎破冰，18:15 和 19:00 两场演讲，19:45 总结与酒水交流。
- 🌐 **社区性质**：PyData Leeds 是专业活动，要求遵守 NumFOCUS 行为准则，旨在促进 Python、数据与工程领域的交流。

---

### [PyData 南安普顿 - 第 25 次聚会，2026 年 6 月 16 日星期二，晚上 7:00 | Meetup](https://www.meetup.com/pydata-southampton/events/314861641/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [PyData Southampton - 25th Meetup, Tue, Jun 16, 2026, 7:00 PM   | Meetup](https://www.meetup.com/pydata-southampton/events/314861641/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

PyData Southampton 第 25 次聚会将于 6 月 16 日在 Carnival House 举行，内容包括 PyO3 入门、数据转型演讲和闪电演讲，并提供披萨和饮料。

- 🗓️ **聚会详情**：6 月 16 日晚上 7 点至 9 点，地点在 Carnival House，需携带有效身份证件入场。
- 🎤 **主要演讲 1**：David Hewitt 讲解如何使用 PyO3 和 Rust 为 Python 代码添加原生核心，提升性能。
- 🔄 **主要演讲 2**：Nick Thorne 和 Bob Menlove 探讨如何通过 AI、交付和人才整合，推动英国从传统模式转向竞争优势。
- ⚡ **闪电演讲**：包括 Tim Trew 的“DSPy 入门”和另一个待定主题。
- 🍕 **餐饮与社交**：由 Carnival UK 提供披萨和饮料，晚上 9 点后可前往附近酒吧继续交流。
- 📋 **重要提醒**：参会者需在 Meetup 资料中使用真实姓名，否则无法进入嘉宾名单；请遵守 NumFOCUS 行为准则。
- 🏢 **主办与赞助**：由 PyData Southampton 组织，赞助商包括 NumFOCUS、Carnival UK 和 JetBrains。

---

### [PyData 华沙 #34 - 鲁斯兰·科尔尼丘克 & 拉法尔·马拉尼/马切伊·布林斯基，2026 年 6 月 17 日星期三下午 6:00 | Meetup](https://www.meetup.com/pydata-warsaw/events/314976654/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

**原文标题**: [PyData Warsaw #34 - Ruslan Korniichuk & Rafał Małanij/Maciej Brynski, Wed, Jun 17, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-warsaw/events/314976654/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-749-june-11-2026)

PyData Warsaw #34 活动于 6 月 17 日在华沙 ING Hub 举办，由两位主持人组织，包含两场关于临床试验匹配和足球数据分析的演讲，并得到赞助商支持。

- 🏥 **临床试验匹配演讲**：Rafał Małanij & Maciej Bryński 介绍混合系统结合确定性数据工程与 LLM，强调 LLM 并非万能，需稳健系统设计和人工监督以提升患者治疗机会。
- ⚽ **足球数据分析演讲**：Ruslan Korniichuk 展示如何用 Python 收集和处理比赛数据（如 Hudl Statsbomb），提供 Jupyter Notebooks 实战知识，解码现代足球战术。
- 📍 **活动地点**：在 ING Hub（Pańska 97, Warszawa）举办，由 ING 赞助，旨在为数据社区创造知识分享空间。
- 🏢 **赞助商**：包括 Continuum Analytics（创始赞助）和 Centrum Innowacji PW，支持活动在 CINN 场地举行。
- 👥 **主持人**：Mikołaj R. 和 Rafał M. 负责组织本次活动，时间为 18:00 至 20:00（CEST）。

---

