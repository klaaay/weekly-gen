### [已缓解的 python.org 下载元数据 API 认证绕过 | Python Insider](https://blog.python.org/2026/06/mitigated-api-bypass-for-download-metadata-python-dot-org/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Mitigated API authentication bypass for python.org download metadata | Python Insider](https://blog.python.org/2026/06/mitigated-api-bypass-for-download-metadata-python-dot-org/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

python.org 下载元数据的 API 认证绕过漏洞已被修复。该漏洞由 DEVCORE 研究团队的 Splitline Ng 于 2026 年 2 月 23 日报告，允许攻击者通过提供管理员用户名和任意 API 密钥来获得管理员权限，可能修改 Python 版本和文件元数据，影响用户下载链接。

- 🔐 漏洞发现：Splitline Ng 报告 python.org 发布管理 API 存在认证绕过漏洞，通过提供管理员用户名和任意 API 密钥即可获得管理员权限
- 🎯 潜在影响：攻击者可修改 Python 版本和文件元数据，包括验证材料 URL，但无法直接修改现有发布文件
- ✅ 漏洞确认：PSRT 在本地实例确认漏洞，由 Seth Larson 和 Hugo van Kemenade 开发并部署补丁，48 小时内完成修复
- 📊 未发现利用：审计日志、数据库备份、Sigstore 和 PGP 材料后确认无漏洞利用证据，且下游工具自动验证机制使攻击难以隐藏
- 🔧 修复措施：应用补丁区分“访客”和 API 密钥认证模式，增加测试用例，拒绝非 HTTPS URL，日志保留从 3 天延长至 30 天
- 🕐 时间线：2026 年 2 月 23 日报告，24 日修复，2 月 25 日完成审计，4 月 LLM 审计，6 月 Trail of Bits 第三方审计，6 月 23 日发布最终报告
- 🙏 致谢：感谢 DEVCORE 研究团队负责任披露，OpenAI 资助第三方审计，Trail of Bits 完成审计和缓解措施

---

### [Python 软件基金会新闻：2026 年 PSF 董事会选举日期](https://pyfound.blogspot.com/2026/06/psf-board-election-dates-for-2026.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Python Software Foundation News: PSF Board Election Dates for 2026](https://pyfound.blogspot.com/2026/06/psf-board-election-dates-for-2026.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

PSF 董事会选举将于 2026 年举行，今年有 4 个席位空缺，同时将首次与包装委员会（PC）选举并行进行。

- 🗳️ **选举时间线**：提名期从 7 月 28 日至 8 月 11 日，候选人公布于 8 月 13 日，投票从 9 月 1 日持续至 9 月 15 日。
- ✅ **投票资格**：需在 8 月 25 日前成为贡献者、支持者或研究员成员，并确认投票意向；去年投票者自动加入选民册。
- 📧 **沟通偏好**：成员可在 psfmember.org 上设置是否接收董事会或 PC 选举邮件，默认仅发送少量年度通讯。
- 👥 **竞选董事会**：欢迎具有领导力、筹款、非营利经验或技术专长的人士参选，可自荐或推荐他人。
- 🆕 **PC 选举并行**：首次包装委员会选举将与董事会选举同步进行，详情将通过 PSF 博客公布。
- 🎥 **了解更多**：可通过 YouTube 视频、年度影响报告及论坛讨论获取董事会角色信息，7-8 月还有 Discord 办公时间答疑。

---

### [从零开始编写一个编码代理 | mathspp](https://mathspp.com/blog/write-a-coding-agent-from-first-principles?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Write a coding agent from first principles | mathspp](https://mathspp.com/blog/write-a-coding-agent-from-first-principles?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

本教程从零开始，手把手教你构建一个属于自己的编码助手。通过实践，你将深入理解编码助手的工作原理。

- 🤖 **核心概念**：编码助手是一个拥有额外工具（如读取文件、运行命令）的 LLM，使其能与环境交互。本教程使用 Claude API 和 Python SDK 进行演示。
- 🛠️ **项目搭建**：使用`uv`初始化项目，并安装`python-dotenv`和`anthropic`依赖。通过`.env`文件配置 Claude API 密钥进行身份验证。
- 💬 **对话上下文**：要实现连续对话，必须维护一个包含所有历史消息的`context`列表，并在每次请求时将其发送给 LLM。LLM 的回复也需要添加到上下文中。
- ⌨️ **用户命令**：可以自定义用户命令（如`/exit`、`/help`），通过拦截以`/`开头的用户输入来实现，不将其发送给 LLM。
- 🧰 **工具机制**：工具是编码助手的关键。通过向 LLM 提供工具的描述和调用格式，LLM 可以“请求”调用工具。客户端解析请求、执行工具，并将结果返回给 LLM。
- 📄 **文件读取工具**：创建`read`工具，让 LLM 能读取文件内容。通过定义工具指令和解析 LLM 回复中的特定格式（如`tool_call: read('path')`）来实现。
- 🔧 **工具模式定义**：使用 Claude API 提供的工具模式（`name`、`description`、`input_schema`）可以更简单、更健壮地定义工具。LLM 会返回`ToolUseBlock`来请求工具调用。
- 🐚 **编码工具集**：为将普通助手升级为编码助手，需实现`bash`（运行命令）、`write`（写入文件）、`replace`（替换文本）和`insert`（插入文本）等工具。`bash`工具建议增加用户确认环节以提高安全性。
- 🚀 **进阶方向**：可以进一步学习 Anthropic 提供的预置工具、实现响应流式传输，以及使用`rich`或`textual`库改善用户界面。

---

### [最快的 Python 结构体？](https://www.crumpledpaper.tech/2026-06-21-python-struct-profiling/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [The Fastest Python Struct?](https://www.crumpledpaper.tech/2026-06-21-python-struct-profiling/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

本篇文章深入探討了在 Python 中定義結構（struct）類型的啟動成本，並比較了多種實現方式的性能差異。

- 📊 **核心發現**：Python 類型定義並非免費，每次程式啟動都需執行，而 `NamedTuple` 的類型成本約為原生 C 實現的 8 倍，隨著程式增長會逐漸累積。
- 🚀 **性能分層**：測試結果顯示三個性能層級：最快的是 `native slots`、`record-type (C)` 和 `msgspec`（約 7-12 µs）；中間層為 `NamedTuple` 和 `record-type`（約 76-96 µs）；最慢的是 `dataclass` 和 `attrs`（約 200-370 µs）。
- 🧩 **模組成本**：導入依賴庫的固定成本差異巨大，`record-type (C)` 的 `.so` 檔案僅需約 0.2 ms，而 `msgspec` 則需約 19 ms，相差近 95 倍。
- ⚡ **mypyc 編譯效果**：mypyc 能將手寫的 `manual record` 建構時間從 222 ns 降至 78 ns，但對 `NamedTuple` 幾乎無幫助，因其 `__new__` 方法仍保持解釋執行。
- 🔍 **成本根源**：性能差異主要取決於類型定義時需生成的方法數量：最快層級無需生成方法，中間層級生成一個方法，最慢層級生成多個方法並涉及欄位處理。
- 💡 **實用建議**：若追求啟動速度，可考慮使用 `msgspec`（但需承擔較高導入成本）或 `record-type (C)` 原型；`NamedTuple` 雖非最優，但仍是平衡選擇。
- 📈 **交叉點分析**：`msgspec` 在約 256 個類型定義（暖啟動）時超越 `NamedTuple`，但前提是嚴格管理依賴導入。

---

### [错误](https://blog.platypush.tech/article/Local-voice-assistant?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Error](https://blog.platypush.tech/article/Local-voice-assistant?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

无法总结：获取内容时出错 - ('Connection broken: IncompleteRead(32321 bytes read, 582257 more expected)', IncompleteRead(32321 bytes read, 582257 more expected))

---

### [数组 API 采用：如何处理编译代码 | 实验室](https://labs.quansight.org/blog/array-api-aot-jit?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Array API adoption: what to do with compiled code | Labs](https://labs.quansight.org/blog/array-api-aot-jit?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

### 概述总结
本文探讨了在科学计算中，如何通过 Array API 和即时编译（JIT）技术，将依赖 C 扩展的代码（如 SciPy 的 RBFInterpolator）扩展到多核 CPU 和 GPU，实现性能提升，同时评估了不同后端和编译策略的优劣。

- 📊 **背景与动机**：Python 因开发效率高但执行慢，传统方案是写 C 扩展（如 NumPy）。硬件加速器（GPU）的普及催生了 CuPy、PyTorch、JAX 等数组库，通过 Array API 可让通用库（如 SciPy）无缝利用这些加速器，带来数量级性能提升。
- ⚙️ **核心挑战**：现有 C 扩展仅支持 CPU，无法直接用于 GPU。手动移植到 CUDA 不现实，因为硬件（CPU 多核、GPU、TPU）快速变化，维护多套内核成本高。
- 🧪 **实验对象**：以 SciPy 的`RBFInterpolator`为例，其核心评估循环原由 Pythran（AOT 编译器）编译为 C。作者将其改造为 Array API 兼容的纯 Python 实现，并尝试 JIT 编译（torch.compile、jax.jit、numba）。
- 💻 **性能结果（CPU）**：在 4 核笔记本上，JIT 模式（JAX/PyTorch）比 AOT 的 Pythran 快 3-5 倍；在 32 核服务器上，JIT 模式加速达 10-15 倍。Numba 表现最差，甚至慢于 AOT 版本。
- 🚀 **性能结果（GPU）**：在 CUDA GPU 上，JIT 模式（PyTorch）比 CPU 基线快 40 倍，JAX 快 20 倍。CuPy（仅 eager 模式）仅快 3 倍。
- ⚠️ **JIT 技术痛点**：不同 JIT 后端（torch.compile、jax.jit、numba）各有缺陷，如线程控制困难、编译缓存问题、Numba 要求低效的显式循环。但整体上，JIT 的投入产出比远优于手写 CUDA 内核。
- 🔮 **未来展望**：Array API+JIT 是可行的替代方案，但库维护者需解决公共 JIT 接口、多后端维护负担等问题。建议用户根据自身场景进行时间盒化的性能基准测试。

---

### [使用 AI 以尽量不使用 AI](https://www.raymondcamden.com/2026/06/22/use-ai-to-not-use-ai-as-much?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Use AI to not use AI (as much)](https://www.raymondcamden.com/2026/06/22/use-ai-to-not-use-ai-as-much?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

### 概述摘要
本文介绍了如何利用 AI 生成可重复使用的脚本工具，而非仅依赖 AI 一次性解析数据。作者通过解析 GitHub 使用报告 CSV 的案例，展示了让 AI 生成 Python 脚本的实用方法，从而避免重复求助 AI，并逐步扩展功能。

- 🤖 **AI 新用法**：让 AI 生成脚本（如 Python）替代一次性解析，实现重复使用和功能迭代。
- 📊 **问题背景**：作者收到 GitHub Actions 存储用量警告，但官方报告难以定位具体仓库，需手动检查 300+ 仓库。
- 🔍 **AI 初解**：通过 AI 解析 CSV 报告，快速找到问题仓库（testing-boxlang-desktop），但担心问题复发。
- 🛠️ **脚本生成**：使用 Cursor 工具，要求 AI 生成 Python 脚本，自动解析 CSV 并生成按仓库用量排名的报告。
- 📝 **迭代优化**：根据需求调整脚本，增加按存储用量排序的独立报告，突出高存储仓库。
- 💻 **脚本功能**：支持命令行参数（如筛选产品、日期、输出 JSON），无外部依赖，仅用 Python 标准库。
- 🚀 **实际效果**：成功定位高存储仓库（testing-boxlang-desktop 和 tweetback），前者已删除，后者待处理。
- 💡 **核心启示**：AI 不仅是问答工具，更是生成可维护工具的助手，避免重复劳动。

---

### [你不需要那个设计模式 - YouTube](https://www.youtube.com/watch?v=xns3InDkAiA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [You Don’t Need That Design Pattern - YouTube](https://www.youtube.com/watch?v=xns3InDkAiA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

本頁面為 YouTube 平台的資訊與政策總覽，涵蓋版權、聯絡方式、創作者支援及使用條款等核心內容。
- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明內容版權相關規範與保護機制
- 📞 聯絡我們：提供用戶與 YouTube 聯繫的管道
- 🎬 創作者：支援內容創作者的相關資源與工具
- 📢 刊登廣告：介紹廣告投放與營利選項
- 👨‍💻 開發人員：提供 API 與技術開發資源
- 📜 條款：列出 YouTube 服務使用條款
- 🔒 私隱：說明個人資料保護與隱私政策
- 🛡️ 政策及安全：規範平台內容審查與安全準則
- ⚙️ YouTube 的運作方式：解釋平台功能與推薦機制
- 🧪 測試新功能：介紹 YouTube 正在測試的新功能
- 📅 © 2026 Google LLC：版權歸屬與年份標示

---

### [使用 CUGA 构建真正的智能体应用：轻量级框架上的二十四个工作示例](https://huggingface.co/blog/ibm-research/cuga-apps?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Build real agentic apps using CUGA: two dozen working examples on a lightweight harness](https://huggingface.co/blog/ibm-research/cuga-apps?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

### 概述总结
本文介绍了 CUGA（可配置通用智能体）——一个开源的智能体框架，通过提供预构建的编排、状态管理和策略系统，显著简化了企业级 AI 智能体的开发。文章通过一个 IBM 云顾问应用示例，展示了如何用少量代码构建智能体，并强调了其可配置性、可扩展性和内置治理能力。

- 🚀 **CUGA 的核心优势**：它是一个“框架”，而非“框架”，处理了智能体运行所需的规划、执行循环、工具调用和状态管理，开发者只需定义工具列表和提示词。
- 📝 **应用示例**：IBM 云顾问智能体仅需一个文件（`main.py`），包含智能体工厂、工具和提示词，通过四个参数即可构建，展示了从零到一的完整流程。
- 🔧 **工具与提示词分离**：通用能力（如网络搜索）通过 MCP 服务器共享，特定功能（如搜索 IBM 云目录）作为内联工具定义，提示词以有序步骤和明确规则（如“不要编造服务名称”）确保行为可靠。
- 🛡️ **内置治理**：CUGA 在运行时提供策略系统（如意图守卫、工具审批、输出格式化等），无需额外包装即可控制智能体行为，支持语义匹配和状态触发。
- 🌐 **可扩展性**：通过`CugaSupervisor`实现多智能体协作，每个智能体拥有独立工具和上下文；`Agent Skills`允许按需加载知识，避免提示词过载。
- 🏭 **生产就绪**：CUGA 的治理、审计和自托管能力是默认的，而非后期添加。在 IBM Sovereign Core 中，同一智能体可无缝部署到隔离环境，无需重写代码。
- 📚 **资源与入门**：提供`cuga-apps`仓库（含 24 个单文件应用）、MCP 工具浏览器和快速入门指南，开发者可通过克隆、修改工具和提示词快速构建应用。

---

### [30 分钟内构建并部署远程 MCP 服务器到 GKE | Google Cloud 博客](https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Build and Deploy a Remote MCP Server to GKE in 30 Minutes | Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

本指南详细介绍了如何在 30 分钟内，在 Google Kubernetes Engine (GKE) 上构建并部署一个远程 MCP 服务器，以解决大型语言模型（LLM）与外部工具及数据源集成时的上下文获取难题。

- 🚀 **MCP 协议与远程传输**：MCP 采用客户端 - 服务器架构，通过“流式 HTTP”传输协议支持远程访问，使服务器能独立处理多个客户端连接。
- ☁️ **GKE 部署优势**：GKE Autopilot 提供自动伸缩、集中访问和增强安全性（通过 Gateway API 和 SSL 证书），适合部署无状态的 MCP 服务器。
- 🛠️ **环境准备与项目初始化**：需安装 Python 3.10+、uv、gcloud 和 kubectl，并创建项目文件夹及配置文件（如 pyproject.toml）。
- 🧮 **构建数学 MCP 服务器**：使用 FastMCP 框架创建包含“加法”和“减法”工具的服务器，并添加健康检查端点，通过 streamable-http 传输运行。
- 🧪 **本地测试**：通过客户端脚本测试服务器功能，验证工具列表和运算结果，确保部署前功能正常。
- 🐳 **容器化与镜像构建**：编写 Dockerfile，使用 Artifact Registry 存储镜像，并通过 Cloud Build 提交构建。
- 🌐 **GKE 部署与安全暴露**：创建 Deployment 和 Service 资源，通过 Gateway API 配置 HTTPS 负载均衡器、静态 IP 及 Google 管理 SSL 证书，实现安全外部访问。
- 🧹 **资源清理**：提供完整命令删除部署、网关、证书、存储库和集群，避免资源浪费。
- 📚 **扩展阅读**：推荐 MCP、GKE Gateway API 和 FastMCP 官方文档，以深入探索 AI 工作流集成。

---

### [TIRx：面向演进前沿机器学习内核的开放编译器栈](https://tvm.apache.org/2026/06/22/tirx?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [TIRx: An Open Compiler Stack for Evolving Frontier ML Kernels](https://tvm.apache.org/2026/06/22/tirx?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

### 概述总结
TIRx 是一个开源的、面向硬件的机器学习内核 DSL 和编译器，基于 Apache TVM 构建，专为快速演进的 AI 硬件和内核设计，支持 GPU 和专用 AI 加速器。

- 🚀 **核心定位**：TIRx 是一个硬件原生 DSL，编译到 GPU 和 AI 加速器，旨在处理快速变化的内核和硬件，支持专家编写、AI 生成和巨型内核系统。
- ⚙️ **三大设计决策**：保持硬件原生编排（同步、内存放置等）、将重复图块原语暴露给编译器、新硬件先作为内联函数引入，再升级为图块原语。
- 📐 **编程模型**：包含执行作用域（线程/线程束组级别）、张量布局（存储优先接口，映射逻辑坐标到物理硬件坐标）和图块原语调度（根据布局和作用域选择实现）。
- 🧩 **布局设计**：布局是存储合约，使用命名硬件轴（如 laneid、warpid），支持通用形状和显式分片、复制、偏移组件，用于原语调度而非工作划分。
- ⚡ **轻量编译器后端**：解析后，编译器仅解析图块原语调用，直接翻译为原生内核 IR（如 CUDA C++/PTX），避免强制优化阶段，便于快速表达新内核。
- 📊 **性能表现**：在 NVIDIA B200 上，密集 GEMM 达 1517 TFLOPS（BF16 8192³），FP8 块状 GEMM 达 2895 TFLOPS，NVFP4 达 5930 TFLOPS，FlashAttention-4 与基线相当（0.97-1.00x）。
- 🔧 **三大应用场景**：支持新硬件（通过内联函数和原语扩展）、构建巨型内核（任务作为 IR 可组合和调度）、以及智能体内核编程（提供结构化搜索空间和编译器反馈）。
- 🌐 **社区资源**：提供 PyPI 包、Python 前端、内核库、基准测试和现代 GPU 编程课程（CMU），代码和文档在 GitHub 和 Apache TVM 网站上。

---

### [如何构建你的第一个 Scrapy 扩展](https://www.zyte.com/blog/how-to-build-your-first-scrapy-extension/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [How to build your first Scrapy extension](https://www.zyte.com/blog/how-to-build-your-first-scrapy-extension/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

概述总结：本文讨论了人工智能在医疗领域的应用进展，包括诊断辅助、药物研发和个性化治疗，同时指出了数据隐私和伦理挑战。

- 🩺 人工智能在医疗影像分析中提升诊断准确率，帮助医生更快识别疾病
- 💊 通过机器学习加速新药研发过程，缩短临床试验周期
- 🧬 个性化治疗方案基于患者基因数据，提高治疗效果
- 🔒 数据隐私保护成为关键问题，需加强安全措施
- ⚖️ 伦理挑战包括算法偏见和医疗决策责任归属

---

### [Wagtail：Django 管理后台的增强版 ⚡ | TimOnWeb](https://timonweb.com/wagtail/wagtail-as-django-admin-on-steroids/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Wagtail as Django admin on steroids
    
    ⚡ | TimOnWeb](https://timonweb.com/wagtail/wagtail-as-django-admin-on-steroids/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

本文介绍了如何将 Wagtail CMS 作为 Django 的增强版管理后台使用，强调其现代化 UI、易用性和与 Django 的无缝集成。

- 🚀 Wagtail 是 Django 管理后台的“增强版”，提供更现代、美观的 UI，且无需放弃 Django 知识。
- 🔧 注册模型的 API 与 Django admin 高度相似，如 `list_display`、`list_filter` 等，学习成本低。
- 🎨 Wagtail 解决了 Django admin 的痛点：可定制面板、模型版本控制、富文本编辑器、StreamFields 等。
- 📦 安装简单：只需 `pip install wagtail`，并在 `settings.py` 和 `urls.py` 中配置即可。
- 🖼️ Wagtail 提供页面模型、媒体库、编辑工作流等 CMS 功能，但可选择性使用。
- 👥 支持基于用户角色的权限控制，适合多用户协作。
- 💡 建议先从替换 Django admin 开始，逐步探索其 CMS 功能，如版本控制和编辑工作流。

---

### [GitHub - nathan-barry/gzipt: 一种基于压缩的语言模型 · GitHub](https://github.com/nathan-barry/gzipt?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - nathan-barry/gzipt: A compression based language model · GitHub](https://github.com/nathan-barry/gzipt?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

### 概述总结
gzipt 是一个基于 gzip 压缩算法的文本生成模型，它不使用神经网络或训练参数，而是通过寻找最佳压缩的字节序列来生成文本。

- 🗜️ **核心机制**：利用 gzip 压缩算法作为唯一模型，通过搜索压缩效果最好的字节序列来预测和生成文本
- 📚 **工作方式**：需要提供语料库作为初始上下文，然后根据提示词 (prompt) 继续生成后续内容
- 🎭 **示例输出**：基于莎士比亚数据集生成文本，效果虽非完美但令人印象深刻
- ⚙️ **配置参数**：支持调整生成长度 (length)、搜索范围 (horizon)、束宽 (beam-width)、温度 (temperature) 等参数
- 🧵 **多线程支持**：通过--workers 参数控制线程数，利用 zlib 释放 GIL 的特性提升性能
- 🛠️ **使用方式**：通过命令行运行，需指定语料库文件、提示词和生成长度等参数
- 📊 **项目状态**：拥有 76 个星标和 12 个分支，使用 Python 开发，暂无正式发布版本

---

### [GitHub - kernalix7/winpodx: 适用于 Linux 的 Windows 容器系统 · GitHub](https://github.com/kernalix7/winpodx?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - kernalix7/winpodx: Windows pod system for Linux · GitHub](https://github.com/kernalix7/winpodx?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

WinPodX 是一個能讓 Windows 應用程式在 Linux 上以原生視窗運行的工具，透過 FreeRDP RemoteApp 技術實現無縫整合。

- 🖥️ **原生視窗體驗**：每個 Windows 應用程式都有自己的 Linux 視窗、真實圖示和 WM_CLASS，可釘選到工作列並支援檔案關聯。
- 🚀 **一鍵安裝與自動配置**：提供 curl 一鍵安裝腳本，首次啟動會自動下載 Windows ISO 並完成配置，約需 5-10 分鐘。
- 🛡️ **裸機偽裝功能**：v0.7.0 新增的選用功能，讓 Windows 虛擬機對 VM 檢測軟體顯示為實體機器，避免驅動程式或安裝程式阻擋。
- 🔄 **雙向檔案關聯**：支援 Linux 應用程式出現在 Windows 的「開啟檔案」選單，反之亦然，實現無縫檔案操作。
- 🎛️ **豐富的 CLI 與 GUI**：提供完整的命令列工具（如 `winpodx app run`、`winpodx doctor`）和 Qt6 圖形介面，包含即時資源監控儀表板。
- 🖥️ **多種安裝方式**：支援 curl 腳本、各發行版套件管理器（openSUSE、Fedora、Debian、Arch 等）、AppImage 和 Nix。
- 🔧 **最低硬體需求**：需要支援虛擬化的 CPU（Intel VT-x 或 AMD-V）、8GB 以上記憶體、約 30GB 磁碟空間，且使用者需在 kvm 群組中。
- 📦 **輕量依賴**：Python 3.11+ 僅需標準函式庫，無外部 pip 依賴；AppImage 僅約 110MB。
- 🌐 **多語言支援**：介面支援 7 種語言（英文、韓文、中文、日文、德文、法文、義大利文），自動偵測系統語言。
- 🔒 **安全與自動化**：包含密碼自動輪換、智慧 DPI 縮放、Windows 瘦身、USB 裝置穿透、閒置自動暫停等功能。

---

### [GitHub - dorukkumkumoglu/optocamzero: Optocam Zero 是一款基于树莓派 Zero 的紧凑型数码相机，采用现成组件制作而成。](https://github.com/dorukkumkumoglu/optocamzero?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - dorukkumkumoglu/optocamzero: Optocam Zero is a Raspberry Pi Zero based compact digital camera made using off the shelf components. · GitHub](https://github.com/dorukkumkumoglu/optocamzero?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

Optocam Zero 是一款基于 Raspberry Pi Zero 的紧凑型数码相机，使用现成组件制作，设计轻巧便携、操作直观，适合 DIY 爱好者制作和玩耍。

- 📸 非常小巧，可轻松放进口袋，携带方便。
- 🎨 内置 8 种照片滤镜，支持 GIF 录制和播放。
- ⚡ 启动时间 14 秒，支持 USB-C 充电，电池可更换。
- 🖥️ 1.4 英寸 LCD 屏幕，预览帧率 15–20 fps，支持屏幕自动调暗省电。
- 🛠️ 所有外壳部件可 3D 打印，电子元件均为常见易购组件。
- 📡 通过自定义热点界面快速传输图片，适配手机和电脑。
- 📷 拍摄 2592x2592px JPEG 图像，后台保存不影响预览。
- 🔋 使用 14500 锂电池，每次充电可用 70–80 分钟。
- 📦 仓库包含完整硬件文件、BOM 清单、PDF 构建指南和 STL 文件。
- 💻 软件部分提供安装程序和操作说明，主要使用 Python 和 Shell。

---

### [GitHub - baidu/Unlimited-OCR: 无限 OCR 工作：迎接一次性长视野解析时代。](https://github.com/baidu/Unlimited-OCR?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - baidu/Unlimited-OCR: Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing. · GitHub](https://github.com/baidu/Unlimited-OCR?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

概述总结：Unlimited-OCR 是一个开源项目，旨在实现一次性长跨度文档解析，支持单图、多图和 PDF 处理，提供多种推理方式。

- 🚀 项目介绍：Unlimited-OCR 由百度发布，基于 Deepseek-OCR 改进，支持一次性长跨度文档解析。
- 📄 论文与资源：论文已在 arXiv 发布，模型可在 Hugging Face、ModelScope 等平台获取。
- ⚙️ 推理方式：支持 Transformers 和 SGLang 两种推理方式，均提供详细代码示例。
- 🖼️ 图像配置：单图支持“gundam”（640x1024）和“base”（1024x1024）两种模式，多图/PDF 仅用“base”模式。
- 📑 多页与 PDF 处理：支持多图及 PDF 转图像后解析，使用 PyMuPDF 将 PDF 转为图像。
- 🧠 自定义参数：可设置最大长度、n-gram 重复抑制等参数优化输出。
- 📦 批量推理：提供 infer.py 脚本支持批量处理图像目录或 PDF 文件。
- 📊 可视化与引用：项目包含可视化功能，并引用 Deepseek-OCR、PaddleOCR 等工作。
- 📜 许可证与贡献：采用 MIT 许可证，欢迎社区贡献。

---

### [GitHub - jamesyc/TimeCapsuleSMB：破解苹果Time Capsule 以运行现代 Samba · GitHub](https://github.com/jamesyc/TimeCapsuleSMB?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - jamesyc/TimeCapsuleSMB: Hacking the Apple Time Capsule to run modern Samba · GitHub](https://github.com/jamesyc/TimeCapsuleSMB?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

TimeCapsuleSMB 是一个开源项目，旨在让 Apple Time Capsule 运行现代 Samba 服务器，以恢复 Time Machine 备份功能。

- 🖥️ **项目背景**：Apple 在 macOS 27 中移除了 AFP 支持，且早已不支持 SMB1，导致旧款 Time Capsule 无法用于备份。此项目通过修改 Samba 4.24.3 并直接在 Time Capsule 上运行，实现 SMB3 连接和 Time Machine 支持。
- 🛠️ **安装方式**：提供 macOS 图形界面应用和 Python 脚本两种安装方式。支持通过 mDNS/Bonjour 自动发现设备，并可配置 SSH 访问。
- 🔄 **工作原理**：将 Samba 二进制文件存储在内部硬盘，启动时复制到 RAM 磁盘运行，避免因硬盘休眠导致服务中断。同时使用独立的 mDNS 广告器广播服务。
- 🔐 **安全与认证**：使用 Time Capsule 设备密码作为 Samba 密码，支持任意用户名登录。仅限局域网使用，不建议暴露到公网。
- ⚙️ **设备兼容性**：支持所有 Time Capsule 型号。AirPort Extreme 也可非官方使用，但需有硬盘。NetBSD 4 设备需手动激活或刷写固件以自动启动。
- 📋 **部署步骤**：包括准备环境、配置设备、部署 Samba、刷写固件（旧设备）和验证结果。提供 `doctor` 命令进行完整诊断。
- 🧹 **卸载与恢复**：通过 `uninstall` 命令可移除所有管理文件，恢复设备至原始状态。
- 🔧 **技术细节**：项目包含多个组件（smbd、mDNS 广告器、NBNS 响应器），并针对 NetBSD 4/6 系统提供不同二进制版本。开发者可自行在 NetBSD VM 中重建。

---

### [GitHub - raiyanyahya/recall: 别再浪费令牌，每次会话都重新解释你的项目。Recall 为 Claude Code 提供持久记忆——完全离线。](https://github.com/raiyanyahya/recall?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - raiyanyahya/recall: Stop wasting tokens and re-explaining your project every session. Recall gives Claude Code durable memory — entirely offline. · GitHub](https://github.com/raiyanyahya/recall?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

Recall 是一个为 Claude Code 提供完全本地化项目记忆的开源工具，旨在解决每次会话需重新解释项目的冷启动问题，所有处理均在本地完成，无需 API 密钥或外部模型。

- 🔁 完全本地运行：所有会话记录和摘要都在本地机器上处理，不发送任何数据到外部 API，确保隐私安全。
- 💰 零额外成本：使用本地 TF-IDF + TextRank 算法生成摘要，不消耗模型 tokens，仅依赖已有的 Claude Code 订阅。
- 📝 自动记录会话：通过 hooks 自动将每次会话活动追加到 `.recall/history.md` 文件，实现增量捕获。
- 📄 生成紧凑摘要：运行 `/recall:save` 命令后，本地摘要器生成 `context.md`（约 1-2K tokens），包含目标、摘要、下一步行动等关键信息。
- 🛠️ 无需安装依赖：摘要器完全内置，numpy 为可选加速器，即使没有也能用纯 Python 运行相同算法。
- 🔒 隐私与安全强化：无网络调用、无 API 密钥、自动脱敏敏感信息（如 API 密钥）、限制 git 命令执行风险。
- ⚙️ 灵活配置：通过 `recall.config.json` 可自定义输出目录、自动保存、摘要句子数、脱敏开关等参数。
- 🤝 开源社区友好：采用 MIT 许可证，欢迎贡献，提供完整的开发指南、测试套件和 CI 质量门控。

---

### [GitHub - VectifyAI/OpenKB: OpenKB：开放大语言模型知识库 · GitHub](https://github.com/VectifyAI/OpenKB?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - VectifyAI/OpenKB: OpenKB: Open LLM Knowledge Base · GitHub](https://github.com/VectifyAI/OpenKB?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

OpenKB 是一个开源的 LLM 知识库系统，能将原始文档编译成结构化的维基式知识库，并支持推理式检索、多模态和技能工厂等功能。

- 📚 **核心概念**：基于 Andrej Karpathy 的理念，将知识编译为持久的维基页面，而非每次查询都重新推导，实现知识的积累与更新。
- 🧠 **独特优势**：无需向量数据库，采用 PageIndex 的无向量、基于推理的检索，能高效处理长文档（如 PDF）并支持多模态内容（图表、图片）。
- 🛠️ **主要功能**：支持多种格式文档（PDF、Word、Markdown 等），提供查询、多轮对话、知识可视化、技能工厂（将知识蒸馏为可复用的 Agent 技能）等功能。
- ⚙️ **工作流程**：文档通过 markitdown 或 PageIndex 处理后，由 LLM 生成摘要、概念页、实体页，并自动更新索引和交叉引用。
- 🔗 **集成生态**：生成的维基为纯 Markdown 文件，兼容 Obsidian；技能可直接安装到 Claude Code、Codex 等主流 Agent 中。
- 🚀 **快速上手**：通过 `pip install openkb` 安装，使用 `openkb init` 初始化，`openkb add` 添加文档，`openkb query` 或 `openkb chat` 进行问答。
- 🎯 **技能工厂**：`openkb skill new` 可从维基中提炼出包含 SKILL.md、参考资料和可选脚本的便携式 Agent 技能，并支持版本回滚与质量评估。
- 🔧 **配置灵活**：支持多种 LLM 提供商（OpenAI、Claude、Gemini 等），可通过 `config.yaml` 自定义模型、语言和实体类型。
- 📊 **可视化**：`openkb visualize` 可生成包含 3D 力导向图、思维导图和径向树的交互式知识图谱 HTML 页面。

---

### [GitHub - hustvl/Moebius：[ECCV 2026] Moebius：0.2B 轻量级图像修复框架，性能达 10B 级别](https://github.com/hustvl/Moebius?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - hustvl/Moebius: [ECCV 2026] Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance · GitHub](https://github.com/hustvl/Moebius?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

Moebius 是一个仅 0.22B 参数的轻量级图像修复框架，通过架构创新与知识蒸馏的协同优化，在 6 项基准测试中达到或超越 10B 级工业模型（如 FLUX.1-Fill-Dev）的性能，同时实现 15 倍以上的推理加速。

- 📉 **极致参数效率**：仅 0.22B（226M）参数，不到 FLUX.1-Fill-Dev（11.9B）的 2%，可在消费级设备上运行高质量修复。
- ⚡ **15 倍推理加速**：单 GPU 每步仅需 26.01 毫秒，总运行时间比 10B 级模型快 15 倍以上。
- 🏆 **10B 级修复质量**：在自然场景（Places2）和人像场景（CelebA-HQ、FFHQ）等 6 个基准上，与 FLUX.1-Fill-Dev 持平或超越，尤其在复杂纹理和人脸合理性方面表现更优。
- 💡 **核心创新协同**：通过 LλMI 模块（线性注意力机制）和自适应多粒度蒸馏策略，在紧凑结构中最大化吸收教师模型（PixelHacker）的语义推理能力。
- 🚀 **任务专用专家**：针对图像修复和对象移除任务高度优化，避免参数臃肿，实现更智能、更轻量、更快速的解决方案。
- 🔥 **社区认可**：已获 ECCV 2026 接收，并在 Hugging Face 上达到日榜第一、周榜第四的成绩。

---

### [GitHub - graphsignal/graphsignal-profiler: Graphsignal 分析器](https://github.com/graphsignal/graphsignal-profiler?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - graphsignal/graphsignal-profiler: Graphsignal Profiler · GitHub](https://github.com/graphsignal/graphsignal-profiler?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

Graphsignal 是一个面向生产环境的推理性能分析平台，帮助工程师优化 AI 模型、引擎、GPU 等加速器的性能，提供全栈推理可见性。

- 📊 提供连续、高分辨率的时间线分析，展示推理工作负载的操作耗时和资源利用率。
- 🧠 支持 LLM 生成追踪，包含每步时间、Token 吞吐量和延迟分解，适用于主流推理框架。
- ⚙️ 采集推理引擎和硬件（CPU、GPU、加速器）的系统级指标。
- 🚨 监控设备级故障和推理错误，确保稳定性。
- 🤖 为 AI Agent 提供推理遥测，识别瓶颈并推动针对性优化。
- 🔧 安装简单，支持 UV 或 pip 安装，并可选择 CUDA 12.x 或 13.x 版本。
- 🚀 通过 `graphsignal-run` 包装启动命令，设置 API 密钥即可开始分析。
- 🔒 低开销，仅通过出站连接发送数据，不记录敏感内容（如提示和完成结果）。
- 🛠️ 支持 PyTorch、vLLM、SGLang 等库和推理引擎的集成。
- 📈 登录后可监控和分析应用，并支持 AI 编码代理（如 Claude Code）获取信号上下文。

---

### [GitHub - datajuicer/data-juicer: 面向基础模型的数据处理工具！🍎 🍋 🌽 ➡️ ➡️🍸 🍹 🍷](https://github.com/datajuicer/data-juicer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - datajuicer/data-juicer: Data processing for and with foundation models!  🍎 🍋 🌽 ➡️ ➡️🍸 🍹 🍷 · GitHub](https://github.com/datajuicer/data-juicer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

Data-Juicer 是一个面向基础模型时代的数据操作系统，提供模块化、可扩展的数据处理工具，支持从文本到多模态数据的全流程处理，并具备生产级性能。

- 🍎 核心功能：提供 200+ 操作符，支持文本、图像、音频、视频和多模态数据处理，采用配方优先的 YAML 管道，可重现、版本控制和共享。
- 🚀 性能与扩展性：可在 50 个 Ray 节点（6400 核）上 2 小时内处理 700 亿样本，支持自动 OP 融合（2-10 倍加速）、自适应并行和 CUDA 加速。
- 🤖 应用场景：覆盖基础模型预训练、微调、强化学习、智能体系统、RAG 和数据分析，提供专用工具如智能体交互质量检查和语义 LLM 操作符。
- 📰 最新版本：v1.5.2（2026 年 5 月）新增语义 LLM 操作符、跨文档行级去重和精简依赖；v1.5.1 支持 LaTeX 操作符和压缩格式；v1.5.0 引入分区 Ray 执行器和环境管理。
- 🔌 生态系统：集成 Ray、Hugging Face、Apache Arrow 等框架，被阿里巴巴、字节跳动、NVIDIA 等企业和多所高校采用，提供扩展如 data-juicer-agents 和 data-juicer-hub。
- ⭐ 社区与贡献：鼓励通过 GitHub 贡献，提供新手任务、开发者指南和社区连接（Slack、DingTalk、Discord），基于 Apache 2.0 许可。

---

### [GitHub - StarTrail-org/PixelRAG: 网页解析的终结。可扩展原生像素搜索的开端。](https://github.com/StarTrail-org/PixelRAG?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [GitHub - StarTrail-org/PixelRAG: The end of web parsing. The beginning of scalable pixel-native search. · GitHub](https://github.com/StarTrail-org/PixelRAG?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

PixelRAG 是一个基于截图而非文本的检索增强生成（RAG）框架，旨在通过视觉内容（如表格、图表）提升文档检索和问答效果。

- 📸 **核心创新**：将文档渲染为截图而非解析为文本，保留表格、图表、布局等视觉结构，使模型能直接“阅读”图像。
- 🧠 **视觉嵌入模型**：使用 Qwen3-VL-Embedding 模型（LoRA 微调），将页面截图嵌入可检索的向量空间，支持基于外观的搜索。
- 🚀 **预建索引**：提供包含 828 万维基百科页面的预建索引，无需设置即可通过 API 或浏览器进行搜索。
- 🛠️ **多功能工具**：包含 `pixelshot` 渲染命令和 `pixelrag` 管道（分块、嵌入、索引、服务），支持网页、PDF 和图像。
- 🤖 **Claude 集成**：作为 Claude Code 插件，允许 Claude 通过截图“查看”页面，理解图表和布局。
- 💻 **本地运行**：支持 Linux (CUDA) 和 macOS (Apple Silicon)，无需 GPU 即可索引和搜索 PDF 等文档。
- 📚 **开源与训练**：代码、训练适配器和数据集均已开源，允许用户基于其他骨干模型进行自定义微调。

---

### [Django 6.1 beta 1 发布 | 博客 | Django](https://www.djangoproject.com/weblog/2026/jun/24/django-61-beta-1-released/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [Django 6.1 beta 1 released | Weblog | Django](https://www.djangoproject.com/weblog/2026/jun/24/django-61-beta-1-released/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

Django 6.1 beta 1 现已发布，这是 6.1 版本周期的第二阶段，旨在让用户提前体验新功能。正式版预计于 2026 年 8 月 5 日发布，当前版本仅修复新功能中的错误和回归问题，不建议用于生产环境。

- 🎉 Django 6.1 beta 1 发布，标志着 6.1 版本进入测试阶段
- ✨ 包含新功能和可用性改进，详情见开发中的 6.1 发布说明
- 🐛 仅修复新功能中的错误和早期版本的回归问题
- 📅 当前计划：约一个月后发布候选版，8 月 5 日发布最终版
- 🧪 社区早期测试有助于减少最终版本中的错误
- ⚠️ 此版本不适用于生产环境，仅供测试新功能和报告错误
- 🔑 发布包使用 Jacob Walls 的 PGP 密钥签名（ID: 131403F4D16D8DC7）

---

### [DragonPy 2026 年 7 月聚会，2026 年 7 月 2 日星期四下午 6:00 | Meetup](https://www.meetup.com/ljubljana-python-group/events/315198671/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [DragonPy meetup July 2026, Thu, Jul 2, 2026, 6:00 PM   | Meetup](https://www.meetup.com/ljubljana-python-group/events/315198671/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

DragonPy 2026 年 7 月聚會由 Dror S.和 Nejc Z.主辦，於 7 月 2 日下午 6 點至 8 點 30 分在盧布爾雅那電腦博物館舉行，包含四場精彩演講及會後交流。

- 🐍 **活動概要**：盧布爾雅那 Python 用戶組舉辦的 DragonPy 聚會，提供 Python、友誼與披薩的交流機會。
- 🗓️ **時間地點**：2026 年 7 月 2 日（週四）18:00-20:30，於 Računalniški Muzej（celovška cesta 111, ljubljana）舉行。
- 🎤 **演講一：Rust 替代工具** - Nejc Zupan 分享如何用 Rust 重寫的替代工具（如 ruff、mypy 等）取代傳統 Python 工具（pyflakes、black 等），並解釋原因。
- 🖼️ **演講二：大規模圖像匹配** - Dror Speiser 探討以 Python 作為協調語言，進行一次性大規模圖像匹配計算，比較不同平行化與優化方法。
- 🧩 **演講三：裝飾器解密** - Rok Mušič從基礎逐步介紹裝飾器：本質、@語法、自訂裝飾器及常見範例（如@dataclass、@staticmethod）的實際運作。
- 👨‍💻 **演講四：我是開發者** - Dejan Murko 延續去年「氛圍編碼」主題，探討無開發技能者如何逐步建構軟體。
- 🍕 **會後活動**：演講結束後提供飲料與披薩，促進交流。
- 📍 **相關主題**：盧布爾雅那活動、資料管理、Python、電腦程式設計、軟體開發、科技。

---

### [sudi viz：您的云基础设施的 X 光透视，2026 年 7 月 1 日（周三）下午 6:30 | 聚会](https://www.meetup.com/python-glasgow/events/315344661/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

**原文标题**: [sudiviz: X-ray Vision for Your Cloud Infrastructure, Wed, Jul 1, 2026, 6:30 PM   | Meetup](https://www.meetup.com/python-glasgow/events/315344661/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-751-june-25-2026)

本次活动的主题是使用开源 Python 工具 **sudiviz** 对 AWS 云基础设施进行实时可视化与问题修复，活动为线上线下混合形式。

- 🔍 **核心工具**：sudiviz 是一款免费开源的 Python CLI 工具，能实时可视化 AWS 拓扑结构，并自动检测配置错误和孤立资源。
- 🛠️ **技术栈**：工具基于 boto3、NetworkX、FastAPI 和 Cytoscape.js 构建，将 AWS API 响应转化为交互式图表。
- 🎯 **目标受众**：面向云/DevOps 工程师、平台/SRE 团队、架构师、Python 开发者及开源爱好者。
- 📍 **活动详情**：2026 年 7 月 1 日 18:30（欧洲/伦敦时间），在格拉斯哥 The Gamer Club 举办，线上线下均可参加。
- 🎥 **直播与互动**：活动将在 YouTube 直播，参与者可通过 Matrix 聊天室与组织者和观众交流。
- 🍿 **场地福利**：提供免费茶饮、可自带酒水，现场配备游戏区、街机、投影仪及千兆网络。

---

