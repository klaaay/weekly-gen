### [使用 LangChain 和向量数据库的生产级 RAG——完整课程 - YouTube](https://www.youtube.com/watch?v=mHxLXzYjQRE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [Production RAG with LangChain & Vector Databases – Full Course - YouTube](https://www.youtube.com/watch?v=mHxLXzYjQRE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

本頁面為 YouTube 平台的資訊與政策總覽，涵蓋法律條款、創作者支援及平台運作方式。
- 📰 新聞中心：提供 YouTube 官方新聞與公告。
- ©️ 版權：說明版權相關規範與保護機制。
- 📞 聯絡我們：提供用戶與創作者聯繫 YouTube 的方式。
- 🎬 創作者：針對內容創作者的資源與支援。
- 📢 刊登廣告：說明廣告投放與營利相關資訊。
- 📜 條款：列出使用 YouTube 服務的法律條款。
- 🔒 私隱：解釋用戶資料的收集與使用政策。
- 🛡️ 政策及安全：涵蓋平台安全規範與內容審查標準。
- ⚙️ YouTube 的運作方式：介紹平台推薦與內容分發機制。
- 🧪 測試新功能：說明新功能的測試與回饋流程。
- ©️ 2026 Google LLC：版權歸屬與法律聲明。

---

### [解读字形：：Python 中的不透明类型](https://blog.glyph.im/2026/05/opaque-types-in-python.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [Deciphering Glyph ::
        Opaque Types in Python
      ](https://blog.glyph.im/2026/05/opaque-types-in-python.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

### 概述摘要
本文介绍了一种在 Python 中实现不透明数据类型的模式，通过`typing.NewType`结合私有类来隐藏内部实现细节，同时提供稳定的公共构造函数接口，以保持 API 的灵活性和向后兼容性。

- 📦 **核心问题**：当需要封装复杂配置（如运输选项）时，直接暴露类会导致公共 API 膨胀，难以在后续迭代中保持兼容性。
- 🛠️ **解决方案**：使用`typing.NewType`创建公共类型，包装一个私有数据类（如`_RealShipOpts`），并通过专用构造函数（如`shipFast()`）来限制外部访问。
- 🔒 **封装优势**：私有类的所有属性和构造函数对外部隐藏，仅通过预定义的公共函数暴露，允许内部实现自由演化而不影响用户代码。
- 📈 **演化示例**：从简单的速度选项（"fast"/"slow"）扩展到包含承运商和运输方式（如`Carrier.FedEx` + `Conveyance.air`），旧构造函数仍可正常工作。
- ⚡ **运行时开销**：`NewType`在运行时与底层类型相同，几乎无性能损耗（仅在热循环中需注意轻微调用开销）。
- 🧩 **适用场景**：适用于需要传递复杂状态但希望保持公共 API 稳定、避免兼容性问题的库设计。

---

### [获取失败](https://vshulcz.hashnode.dev/when-python-manual-wiring-turns-into-copy-paste-architecture?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [Failed to retrieve](https://vshulcz.hashnode.dev/when-python-manual-wiring-turns-into-copy-paste-architecture?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

无法总结：获取内容失败，状态码 403。

---

### [使用 TensorFlow 和 PyCharm 为 Reachy Mini 构建实时物体检测应用 | PyCharm 博客](https://blog.jetbrains.com/pycharm/2026/05/build-a-live-object-detection-app-for-reachy-mini-with-tensorflow-and-pycharm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [Build a Live Object Detection App for the Reachy Mini With TensorFlow and PyCharm | The PyCharm Blog](https://blog.jetbrains.com/pycharm/2026/05/build-a-live-object-detection-app-for-reachy-mini-with-tensorflow-and-pycharm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

本教程展示了如何使用 PyCharm 和 TensorFlow 构建实时物体检测应用，并部署到 Reachy Mini 机器人上，实现物体追踪和互动。

- 🤖 **项目概述**：构建一个实时物体检测应用，使用 TensorFlow 的 SSD MobileNet V2 模型，先在笔记本上测试，再部署到开源机器人 Reachy Mini 上，实现头部追踪和天线互动。
- 📦 **阶段一：本地检测**：在 PyCharm 笔记本中搭建 TensorFlow 物体检测管道，使用 OpenCV 捕获摄像头帧，运行模型推理，绘制边界框，并实时显示检测结果。
- 🧠 **模型选择**：采用 TensorFlow Hub 上的 SSD MobileNet V2 模型，在 CPU 上运行约 10 FPS，平衡了速度和准确性，无需额外训练即可用于通用物体检测。
- 🔧 **核心代码**：包括`detect_objects`函数（运行推理并返回检测结果）和`draw_detections`函数（在帧上绘制边界框和标签），支持过滤低置信度检测。
- 🚀 **阶段二：机器人部署**：将检测逻辑封装为 Reachy Mini 应用，包含头部追踪（根据物体位置平滑调整俯仰和偏航）、天线摆动（检测到新物体时触发）和实时 Web 仪表盘。
- 📊 **Web 仪表盘**：在 http://0.0.0.0:8042 提供 MJPEG 视频流、检测列表、FPS 计数器和头部追踪开关，方便开发和监控。
- 🎯 **头部追踪逻辑**：利用摄像头视场角（水平 60°，垂直 45°）计算目标角度，并通过平滑因子（0.15）实现自然运动，无检测时缓慢回中。
- 🎉 **天线互动**：仅在新物体类别首次出现时触发 1.5 秒的正弦摆动，避免持续抖动，使交互更自然。
- 🔗 **扩展方向**：可微调模型识别特定物体、添加更多应用或连接物理手臂，代码完全开源在 GitHub 仓库中。

---

### [智能体系统的宏观评估](https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [Macro Evals for Agentic Systems](https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

### 概述总结
本文介绍了一种针对多智能体系统的宏观评估工作流程，通过分析大量运行轨迹，发现重复的行为模式，从而帮助 AI 工程团队定位系统问题。

- 📊 **宏观评估的必要性**：多智能体系统的故障往往不是单个响应错误，而是重复出现的模式问题，需要从整个运行轨迹的视角进行分析。
- 🏭 **模拟场景**：使用合成电动汽车订单工作流，包含定价、合规、供应、工厂排程等多个专业智能体，以及不断变化的市场和运营条件。
- 🔬 **两级评估体系**：低级评估（如 Promptfoo）对单个智能体、交接和工具进行评分；宏观评估则跨多个低级结果，发现重复问题模式。
- 📝 **数据准备**：将运行轨迹标准化为紧凑文档，包含业务设置、运行结果、交接记录和状态转换摘要，便于后续聚类分析。
- 🧩 **BERTopic 发现**：使用主题建模技术将轨迹文档聚类，发现重复行为模式，并按影响度评分排序，帮助团队优先处理高频且严重的问题。
- 🔍 **AgentTrace 诊断**：对选中的行为模式，构建轻量级执行图，从焦点事件回溯，识别重复出现的上游嫌疑点（如特定智能体、工具或交接）。
- 📈 **可视化分析**：通过桑基图、热力图、散点图等展示案例类型、运行结果、评估发现和行为模式之间的关系，便于技术和业务人员共同理解。
- 🎯 **实用建议**：将低级评估失败案例纳入回归测试套件，跟踪行为模式随模型版本的变化，为高影响模式指定业务负责人，并优先检查嫌疑智能体和工具。

---

### [你应该捕获哪些类型的异常？ - Python Morsels](https://www.pythonmorsels.com/what-types-of-exceptions-should-you-catch/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [What types of exceptions should you catch? - Python Morsels](https://www.pythonmorsels.com/what-types-of-exceptions-should-you-catch/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

本文章探讨了在 Python 中应该捕获哪些类型的异常，以及何时应避免捕获异常。

- 🎯 **仅捕获你理解的异常**：捕获异常时，应确保你了解其来源，避免盲目捕获多种异常类型。
- ❌ **避免捕获 NameError**：NameError 通常由代码中的拼写错误引起，捕获它会隐藏代码本身的 bug。
- ⚠️ **ValueError 和 TypeError 的合理捕获**：ValueError 可能由无效数据（如错误日期）引发，TypeError 可能由缺失数据引发，这些情况下捕获异常是合理的。
- 🔑 **谨慎处理 KeyError**：KeyError 可能由 CSV 文件头拼写错误引起，捕获它可能掩盖问题根源，有时不捕获异常并显示原始错误信息更清晰。
- 🛠️ **预判问题而非捕获异常**：对于可预见的错误（如缺失列头），应在循环前检查并友好提示用户，而非依赖异常处理。
- 🌐 **捕获所有异常的例外情况**：在关键任务代码中（如处理多个文件时），捕获所有异常（Exception）可避免程序因单个错误中断，并记录错误继续执行。
- 💡 **总结**：通常只捕获特定且你理解的异常；在关键代码中，可捕获所有异常并记录，但需谨慎避免掩盖真正问题。

---

### [错误](https://codecut.ai/shrink-python-container-slimtoolkit/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [Error](https://codecut.ai/shrink-python-container-slimtoolkit/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='codecut.ai', port=443): Max retries exceeded with url: /shrink-python-container-slimtoolkit/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [GitHub - mukul975/Anthropic-Cybersecurity-Skills: 754 个结构化网络安全技能，适用于 AI 代理 · 映射至 5 个框架：MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND 及 NIST AI RMF · agentskills.io 标准 · 兼容 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 及 20 多个平台 · 26 个安全领域 · Apache 2.0 许可 · GitHub](https://github.com/mukul975/Anthropic-Cybersecurity-Skills?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [GitHub - mukul975/Anthropic-Cybersecurity-Skills: 754 structured cybersecurity skills for AI agents · Mapped to 5 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND & NIST AI RMF · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 26 security domains · Apache 2.0 · GitHub](https://github.com/mukul975/Anthropic-Cybersecurity-Skills?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

Anthropic Cybersecurity Skills 是最大的开源网络安全技能库，包含 754 个结构化技能，覆盖 26 个安全领域，并映射到 5 个行业框架，旨在让 AI 代理具备资深安全分析师的专业能力。

- 🔒 包含 754 个生产级网络安全技能，覆盖 26 个安全领域，如云安全、威胁狩猎、数字取证等
- 🗺️ 每个技能映射到 5 个行业框架：MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、MITRE D3FEND 和 NIST AI RMF
- 🤖 兼容 Claude Code、GitHub Copilot、Cursor、Gemini CLI 等 20 多个 AI 平台，即插即用
- 📝 技能采用 YAML 前端元数据+Markdown 结构，包含使用时机、前提条件、工作流程和验证步骤
- ⚡ 每个技能扫描仅需约 30 个 token，完整加载 500-2000 个 token，支持渐进式信息获取
- 🛡️ 涵盖 MITRE ATT&CK 全部 14 种战术，NIST CSF 2.0 全部 6 个功能，以及 AI/ML 特定威胁防御
- 👥 社区驱动项目，欢迎贡献新技能或改进现有技能，48 小时内审核 PR
- 📊 包含 ATT&CK Navigator 层文件，支持可视化覆盖映射
- 🔄 最新版本 v1.2.0（2026 年 4 月 6 日），技能数量从 v1.0.0 的 734 个增长至 754 个
- 📖 采用 Apache 2.0 许可证，可自由用于个人和商业项目

---

### [GitHub - microsoft/Webwright: 一个简单的 SWE 风格浏览器代理框架，在长周期网页任务上实现了 SOTA 结果。](https://github.com/microsoft/Webwright?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [GitHub - microsoft/Webwright: A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks. · GitHub](https://github.com/microsoft/Webwright?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

Webwright 是一个轻量级的浏览器代理框架，通过给大语言模型提供终端环境，使其能够编写并执行 Python 脚本来自动化完成网页任务，在长周期网页任务上取得了领先性能。

- 🚀 **核心创新**：将浏览器视为可被代码启动和丢弃的环境，而非持续状态，任务轨迹以可复用的 Python 脚本形式保存。
- 🧱 **轻量架构**：核心代理循环仅约 450 行代码，依赖极少（httpx、pydantic、playwright、typer），无隐藏框架。
- 🏆 **卓越性能**：在 Online-Mind2Web（86.7%）和 Odysseys（60.1%）基准测试中达到当前最优，代码即动作策略显著优于坐标预测。
- 🔌 **插件生态**：支持 Claude Code、OpenAI Codex、OpenClaw、Hermes Agent 等主流代理，提供一键安装和自然语言调用。
- 🛠️ **实用功能**：支持生成可复用 CLI 工具（craft 模式）、任务展示面板（Task Showcase），以及可重复运行的任务报告。
- 📊 **完整工具链**：提供运行轨迹记录、截图保存、任务报告生成，便于调试和结果复现。

---

### [GitHub - francescopace/espectre: 🛜 ESPectre 👻 - 基于 Wi-Fi 频谱分析（CSI）的运动检测系统，集成 Home Assistant。](https://github.com/francescopace/espectre?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [GitHub - francescopace/espectre: 🛜 ESPectre 👻  - Motion detection system based on Wi-Fi spectre analysis (CSI), with Home Assistant integration. · GitHub](https://github.com/francescopace/espectre?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

ESPectre 是一個基於 Wi-Fi 頻譜分析（CSI）的運動檢測系統，並與 Home Assistant 深度整合，無需攝影機或麥克風即可偵測移動。

- 🛜 核心功能：透過 Wi-Fi 訊號干擾偵測移動，無需攝影機或麥克風，保障隱私
- 💰 低成本：硬體僅需約 €10 的 ESP32 裝置（推薦 S3/C6 型號），軟體完全免費開源
- ⚙️ 快速設定：10-15 分鐘即可完成，僅需基本 YAML 設定，無需程式設計或路由器修改
- 📡 運作原理：人體移動會干擾 Wi-Fi 波，ESP32 裝置「監聽」這些變化來判斷移動
- 🏠 應用場景：家庭安全、長者照護、智慧自動化、節能控制、兒童監控等
- 📍 最佳擺放：距離路由器 3-8 公尺，高度 1-1.5 公尺，避免金屬障礙物
- 🔬 技術架構：包含 CSI 資料擷取、增益鎖定、自動校準、自適應閾值、濾波器及偵測評估
- 🤖 機器學習：提供實驗性 ML 偵測器（神經網路），無需校準即可運作
- 🔒 隱私安全：僅收集匿名 CSI 資料（振幅與相位），不收集個人身份、影像或音訊
- 🔄 雙平台策略：ESPectre（生產平台，ESPHome 整合）與 Micro-ESPectre（研發平台，Python/MQTT）

---

### [GitHub - JosephRedfern/plonk：指尖上的Python解释器 · GitHub](https://github.com/JosephRedfern/plonk?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [GitHub - JosephRedfern/plonk: Python interpreter at your fingertips · GitHub](https://github.com/JosephRedfern/plonk?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

Plonk 是一个 macOS 上的浮动 Python REPL 工具，类似 Spotlight 风格，通过全局快捷键呼出，支持持久化 Python 状态和多种便捷操作。

- 🐍 **核心功能**：在菜单栏常驻，通过 `Ctrl + Option + Space` 全局热键弹出浮动 Python 交互面板，支持变量和导入持久化。
- ⌨️ **交互操作**：回车执行代码，`Esc` 或点击外部关闭面板，上下箭头浏览历史命令，`Cmd + C` 快捷复制上次输出。
- 🔧 **元命令**：支持 `%clear` 清屏、`%reset` 重启解释器、`%copy` 复制输出，以及 `!` 执行 Shell 命令（如 `uv`）。
- ⚙️ **设置选项**：可自定义 Python 解释器路径（自动检测虚拟环境）、启动脚本，并支持重启解释器。
- 🖥️ **技术实现**：基于 `MenuBarExtra`、Carbon 热键 API、`NSPanel` 和持久化 Python 子进程（通过 stdin/stdout 通信），禁用沙盒以支持全局热键。
- 🛠️ **构建与发布**：需 macOS 14+，使用 Xcode 构建；`release.sh` 脚本自动化归档、签名、公证和生成 DMG 安装包。

---

### [GitHub - kamalfarahani/katharos：一个为Python函数式编程提供有用类型和函数的库](https://github.com/kamalfarahani/katharos?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [GitHub - kamalfarahani/katharos: A library providing useful types and functions for functional programming in Python · GitHub](https://github.com/kamalfarahani/katharos?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

Katharos 是一个为 Python 提供函数式编程抽象（如 Functor、Monad、Semigroup）和具体类型（Maybe、Result、ImmutableList）的库，旨在通过类型安全、可组合的管道处理副作用、错误和数据转换。

- 📦 **安装简便**：支持通过 `pip install katharos` 或 `uv add katharos` 快速安装。
- 🧩 **核心抽象**：提供 Functor、Applicative、Monad、Semigroup、Monoid 等代数抽象，以及 Maybe、Result、ImmutableList 和 IO 等具体类型。
- ✨ **优雅的错误处理**：使用 `do` 表示法（类似 Haskell）替代嵌套的 `None` 检查和 try/except，通过 `yield` 自动短路处理 Nothing 或 Failure。
- 🔗 **管道式组合**：通过 `|` 操作符链式组合 Result 等类型，错误自动传播，无需手动处理异常。
- 📚 **丰富的示例**：包括 Maybe 处理可选值、Result 建模错误、ImmutableList 使用 Semigroup 操作符 `@` 合并列表等。
- 🛠️ **自定义 Monad 支持**：`do` 表示法适用于任何 Monad，包括自定义实现，灵活性高。
- 📖 **完整文档**：提供教程、API 参考和数学基础解释，位于 katharos.readthedocs.io。
- 📜 **MIT 许可**：开源且自由使用，基于 Python 100% 实现。

---

### [GitHub - bleachbit/bleachbit：适用于Windows和Linux的BleachBit系统清理工具](https://github.com/bleachbit/bleachbit?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [GitHub - bleachbit/bleachbit: BleachBit system cleaner for Windows and Linux · GitHub](https://github.com/bleachbit/bleachbit?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

BleachBit 是一个用于 Windows 和 Linux 的系统清理工具，旨在释放磁盘空间并保护隐私，拥有 5.7k 星标和 376 个复刻，采用 GPL-3.0 许可证。

- 🧹 **核心功能**：清理文件以释放磁盘空间并维护隐私，支持 Windows 和 Linux 系统。
- 🐍 **开发语言**：主要使用 Python（68.4%），辅以 NSIS、CSS、PowerShell 等。
- 📜 **许可证**：基于 GNU 通用公共许可证第 3 版（GPL-3.0）。
- 🚀 **运行方式**：可从源代码运行（需构建翻译），支持命令行接口（`python3 bleachbit.py --help`）。
- 🌐 **翻译支持**：通过 Weblate 平台进行本地化，提供翻译文档。
- 🐳 **Docker 构建**：支持基于 Docker 的 Linux 构建（如 Debian、Fedora、openSUSE），通过 `docker/build.sh` 脚本生成包。
- 🔗 **相关链接**：提供主页、支持、文档、本地化及多个仓库（如 CleanerML、Winapp2.ini）。
- 📊 **项目状态**：拥有 14 个发布版本（最新 v6.0.0，2026 年 4 月），7,254 次提交，58 个观察者。

---

### [六月聚会 @ O'Brien's 酒吧，2026 年 6 月 6 日星期六下午 4:00 | Meetup](https://www.meetup.com/socalpython/events/314894307/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [June Meetup @ O'Brien's Pub, Sat, Jun 6, 2026, 4:00 PM   | Meetup](https://www.meetup.com/socalpython/events/314894307/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

六月聚会 @ O'Brien's Pub 由 Sarah K. 和 Stephen K. 主办，SoCal Python 社区于 2026 年 6 月 6 日下午 4 点至 6 点在圣莫尼卡 O'Brien's Irish Pub 举行。活动免费，无需预约，但建议提前告知人数。主要演讲由 Nuri Halperin 带来，主题为“向量搜索适合我吗？”，涵盖向量搜索的原理、应用、与关键词搜索的对比及集成方法。现场提供露天庭院座位，交通建议包括驾车（有街边付费停车）或乘坐公交（Big Blue Bus #2/#1 或 E 线轻轨）。

- 🍺 活动详情：6 月 6 日周六下午 4-6 点，在 O'Brien's Irish Pub 的露天庭院举行，免费开放。
- 🎤 主讲人：Nuri Halperin，软件架构师，将探讨向量搜索的核心数学、实际用例及与关键词搜索的优劣。
- 📚 演讲要点：帮助理解向量搜索原理、语义搜索解决问题的方式、具体实现方法，以及优缺点分析。
- 🚗 交通建议：可驾车停靠附近街道（周末不拥挤），或乘坐 Big Blue Bus #2/#1 及 E 线轻轨至 26th/Bergamot 站。
- 🤝 社区互动：鼓励成员报名未来演讲，提供友好环境练习分享。

---

### [PyData 诺里奇 - 六月聚会，2026 年 6 月 2 日星期二下午 5:45 | Meetup](https://www.meetup.com/pydata-norwich/events/314788187/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [PyData Norwich - June Meetup, Tue, Jun 2, 2026, 5:45 PM   | Meetup](https://www.meetup.com/pydata-norwich/events/314788187/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

PyData Norwich 六月聚会由 Chris J. 主办，于 6 月 2 日 17:45-19:45 在 Norwich 的 Artlist 举行，主题为数据科学与 Python 相关讨论。

- 🐍 活动提供免费披萨和饮品，适合所有技能水平，非正式氛围鼓励提问。
- 🏢 Aviva 风险分析团队（RAID）的三位成员将分享数据工具构建的幕后经验，聚焦第二线风险操作。
- 📍 地点为 Artlist（27 St Giles St），需按 4 号门铃，活动后可在 Coach and Horses 酒吧继续交流。
- 📅 时间安排：17:45 开门，18:00 开始演讲，19:00 后前往酒吧。
- 🔗 活动遵循 NumFOCUS 行为准则，如有问题可联系组织者。

---

### [生成代码的速度比调试更快 | 2026 年 6 月 3 日（周三）下午 6:30 | Meetup](https://www.meetup.com/pydata-johannesburg/events/314582868/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [Generating Code Faster Than You Can Debug It, Wed, Jun 3, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-johannesburg/events/314582868/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

本次 PyData 约翰内斯堡活动聚焦于代码生成速度与可维护性之间的平衡，强调在 AI 辅助编程时代保持对代码的控制力。

- 🗓️ **活动时间与地点**：2025 年 6 月 3 日 18:30-20:00（南非标准时间），于约翰内斯堡罗斯班克 BBD 办公室举行。
- 🎤 **核心演讲**：Sheena O'Connell 分享如何在 Django 开发中有效使用 Claude Code，包括提示词结构化、设置护栏、信任与验证的平衡，以及早期识别失败模式。
- ⚠️ **关键洞察**：LLM 生成的代码虽快，但可能引入隐藏设计权衡和快速累积的技术债务，调试难度并未降低。
- 🤝 **社区性质**：免费社区活动，强调实用经验分享而非销售宣传，鼓励参与者提交演讲申请。
- 📌 **赞助与相关**：由 PyData 和 NumFOCUS 支持，活动关注本地数据生态动态，并设有社区更新环节。

---

### [驯服数据管道：扩展 Databricks 与检查 dbt，2026 年 6 月 4 日（周四）下午 6:00 | Meetup](https://www.meetup.com/pydata-nl/events/314861600/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

**原文标题**: [Taming Data Pipelines: Scaling Databricks & Linting dbt, Thu, Jun 4, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-nl/events/314861600/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-747-may-28-2026)

本次 PyData Amsterdam 聚会聚焦于数据管道的扩展与工程化，分享如何解决数据平台增长带来的瓶颈问题。

- 📅 **活动时间与地点**：2026 年 6 月 4 日（周四）18:00-21:30，在阿姆斯特丹 Company.info 办公室举行，距 Overamstel 地铁站步行 5 分钟。
- 🎤 **主题演讲一**：Douwe Oosterhout 分享如何在 Databricks 迁移过程中，通过优化集成测试工作流，大幅缩短测试时间，提升开发效率。
- 🛠️ **主题演讲二**：Pádraic Slattery 介绍 dbt-bouncer，一个基于 Python 的开源 linter 工具，帮助团队在大型 dbt 项目中维护自定义编码规范。
- 🍕 **活动流程**：18:00-18:55 提供餐饮，随后是公司介绍、两场演讲（各 45 分钟）、中间休息，最后是自由交流与饮品。
- 🏢 **赞助商**：Adyen、The NextGen、Heineken 和 Rabobank 提供食物、饮品和场地支持。
- 📝 **注册提醒**：PyData Amsterdam 已迁移至 Luma 平台，需通过 Luma 链接注册活动。

---

