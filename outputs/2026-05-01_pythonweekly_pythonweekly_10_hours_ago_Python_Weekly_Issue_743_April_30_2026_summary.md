### [不要在 Python 中使用布尔标志，改用策略 - YouTube](https://www.youtube.com/watch?v=wYeDGkdMi3g&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Don’t Use Boolean Flags in Python, Use Policies Instead - YouTube](https://www.youtube.com/watch?v=wYeDGkdMi3g&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

本頁面為 YouTube 平台相關資訊與政策的總覽，涵蓋法律、商業及功能層面。
- 📰 新聞中心：提供 YouTube 最新消息與公告。
- ©️ 版權：說明版權相關規範與保護機制。
- 📞 聯絡我們：提供與 YouTube 團隊聯繫的方式。
- 🎨 創作者：為內容創作者提供支援與資源。
- 📢 刊登廣告：介紹在 YouTube 上投放廣告的選項。
- 👨‍💻 開發人員：提供 API 與開發工具給技術人員。
- 📋 條款：列出使用 YouTube 服務的條款與條件。
- 🔒 私隱：說明個人資料的收集與使用方式。
- 🛡️ 政策及安全：涵蓋社群規範與安全防護措施。
- ⚙️ YouTube 的運作方式：解釋推薦系統與平台運作原理。
- 🧪 測試新功能：介紹正在測試中的新功能。
- 📅 © 2026 Google LLC：顯示版權年份與所屬公司。

---

### [我如何从零构建一个延迟低于 500 毫秒的语音代理 | Nick Tikhonov](https://www.ntik.me/posts/voice-agent?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [How I built a sub-500ms latency voice agent from scratch | Nick Tikhonov](https://www.ntik.me/posts/voice-agent?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

这篇博客展示了作者如何从零构建一个端到端延迟低于 500 毫秒的语音代理系统，并分享了技术细节和优化经验。

- 🚀 **性能突破**：自建系统实现了约 400ms 的端到端延迟，比 Vapi 等现成平台快 2 倍，关键在于优化编排层和模型选择。
- 🧠 **核心挑战**：语音代理的难点在于实时协调多个模型（STT、LLM、TTS），并精准处理“用户说话/聆听”的状态切换，错误判断会导致尴尬停顿或打断。
- 🔄 **架构设计**：采用状态机（用户说话/聆听）和流式管道（LLM 生成→TTS 合成→音频输出），避免顺序阻塞，并预连接 TTS WebSocket 减少延迟。
- 📍 **地理位置关键**：将编排层部署在靠近服务提供商（Twilio、Deepgram、ElevenLabs）的区域（如 EU），延迟从 1.7 秒降至约 790ms。
- 🏎️ **模型选择**：Groq 的 llama-3.3-70b 首令牌延迟约 80ms，比 OpenAI 的模型快 3 倍，是降低总延迟的最大功臣。
- ⚡ **打断处理**：用户开始说话时，必须立即取消 LLM 生成、关闭 TTS 并清空音频缓冲，确保代理瞬间静音。
- 💡 **自建价值**：虽然现成平台方便，但自建能深入理解参数影响和瓶颈，有助于优化配置或定制特殊需求。

---

### [数据库并非为此而设计](https://arpitbhayani.me/blogs/defensive-databases?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Databases Were Not Designed For This](https://arpitbhayani.me/blogs/defensive-databases?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

## 概述总结
传统数据库架构基于人类开发的确定性应用这一隐含契约，但 AI 代理系统正在系统性破坏这一契约。文章详细分析了五个关键假设的失效原因及应对方案，包括：确定性调用者、有意的写入、短暂的连接、失败的明确反馈以及作为工程契约的模式设计。解决方案涉及语句超时、软删除、仅追加日志、幂等键、独立连接池、查询注释、角色权限控制等成熟技术。

- 🤖 **确定性调用者假设失效**：AI 代理通过推理生成查询，而非人类编写，导致不可预测的查询模式。解决方案是设置角色级语句超时（如 5 秒）和事务空闲超时（如 10 秒）

- 🛡️ **写入意图性假设失效**：代理可能自主写入错误数据或循环写入。核心防御包括：对所有代理可写表实施软删除（添加 deleted_at、deleted_by、delete_reason 列）、对高敏感数据使用仅追加事件日志、强制实施幂等键约束

- 🔄 **连接短暂性假设失效**：代理因推理步骤多、任务扇出和数量激增导致连接时间延长。解决方案包括：为代理工作负载设置独立连接池（pool_size=10, max_overflow=5）、使用 PgBouncer 事务池模式（20 个实际连接可服务 500 个代理连接）

- 📊 **失败明确性假设失效**：代理不会因慢查询或错误结果而报警。关键措施是使用查询注释标记每个查询的 agent_id、task_id 和 step，并构建基于 pg_stat_statements 的监控视图

- 🏗️ **模式设计契约失效**：代理通过 Text-to-SQL 理解模式，列名和注释直接影响查询准确性。解决方案包括：设计代理可读的模式（使用清晰列名和 CHECK 约束）、为遗留系统建立代理视图层、编写类似文档字符串的列注释

- 🔒 **爆炸半径控制**：为每个代理类型创建独立数据库角色，遵循最小权限原则。例如：analytics 角色仅 SELECT 特定视图，customer_support 角色可 INSERT 事件日志但不可 UPDATE 订单，fulfillment 角色仅可 UPDATE 特定字段

- ⚙️ **整体防御架构**：每个代理类型拥有独立角色和超时设置→通过专用连接池连接→PgBouncer 事务池模式→软删除和仅追加日志→幂等键约束→查询注释监控→电路断路器（最大写入数、最大影响行数、最大任务时长）

---

### [pip 26.1 新特性：锁文件与依赖冷却期！ | Richard Si](https://ichard26.github.io/blog/2026/04/whats-new-in-pip-26.1/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [What's new in pip 26.1 - lockfiles and dependency cooldowns! | Richard Si](https://ichard26.github.io/blog/2026/04/whats-new-in-pip-26.1/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

pip 26.1 版本发布，新增依赖冷却期、实验性锁文件支持，修复多项安全问题，并停止支持 Python 3.9。

- 🚫 停止支持 Python 3.9：pip 26.1 要求 Python 3.10 或更高版本，因 Python 3.9 已于 2025 年 10 月结束生命周期。
- 🧪 实验性锁文件支持：可通过 `-r pylock.toml` 从标准锁文件安装，但功能尚不稳定，未来可能变更或移除。
- ⏳ 依赖冷却期：新增 `--uploaded-prior-to` 选项，支持相对时间格式（如 `P3D`），用于延迟安装新发布包以降低供应链攻击风险。
- 🔧 2020 解析器改进：修复了与额外依赖、URL 约束和哈希验证相关的多个长期限制，为移除旧版解析器铺路。
- 🔒 安全修复：修复了将 `.tar.gz` 误识别为 zip 文件（CVE-2026-3219）和自检延迟导入导致的代码执行漏洞（CVE-2026-6357）。
- 📦 urllib3 升级：从 1.26.20 升级到 2.6.3，修复多个 CVE，并停止对旧版的支持。
- 🗑️ 废弃与移除：`PIP_CONSTRAINT` 环境变量对构建依赖的影响将在 pip 26.2 中移除，建议改用 `--build-constraint`。

---

### [Streamlit 小部件：使用常见 UI 组件构建您的应用](https://www.pythonguis.com/tutorials/streamlit-widgets/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [
        Streamlit Widgets: Build your apps using common UI components

    ](https://www.pythonguis.com/tutorials/streamlit-widgets/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

Streamlit 是一款强大的 Python 库，可快速构建交互式网页应用。其核心功能之一是丰富的组件库，允许用户通过多种方式与应用交互，如输入数据、触发操作或可视化数据。本文详细介绍了 Streamlit 的主要组件，包括按钮、复选框、单选按钮、选择框、滑块、文本输入、数字输入、日期时间输入和文件上传器，并提供了大量代码示例和自定义选项。

- 🎯 **按钮 (st.button)**：创建可点击按钮，触发特定操作，支持自定义标签和多个按钮并存。
- ✅ **复选框 (st.checkbox)**：实现二元选择（选中/未选中），可用于显示/隐藏内容或启用/禁用功能，支持默认选中和动态生成。
- 🔘 **单选按钮 (st.radio)**：允许用户从预定义列表中选择单个选项，支持设置默认选中项。
- 📋 **选择框 (st.selectbox)**：提供下拉菜单，节省界面空间，支持设置默认选项。
- 🎚️ **滑块 (st.slider)**：让用户通过拖动选择数值，支持整数、浮点数、日期和时间，可设置范围、步长和默认值，还能实现范围选择。
- ✏️ **文本输入 (st.text_input & st.text_area)**：分别用于单行和多行文本输入，支持字符限制、密码模式等。
- 🔢 **数字输入 (st.number_input)**：用于输入数字，可设置范围、步长和默认值。
- 📅 **日期时间输入 (st.date_input & st.time_input)**：提供日期和时间选择器，支持单个日期、日期范围和时间选择，可组合使用。
- 📁 **文件上传器 (st.file_uploader)**：允许用户上传文件（如 CSV、图片、文本），支持单文件或多文件上传，并可进行文件大小和格式验证。

---

### [轻松使用 Django-Bolt 和 PydanticAI 流式传输 LLM 响应 | Caktus Group](https://www.caktusgroup.com/blog/2026/04/27/django-bolt-easy-pydanticai-streaming/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Easily Stream LLM Responses with Django-Bolt and PydanticAI | Caktus Group](https://www.caktusgroup.com/blog/2026/04/27/django-bolt-easy-pydanticai-streaming/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

本教程展示了如何结合 Django-Bolt 和 PydanticAI 快速搭建异步流式 API 端点，实现 LLM 响应的实时传输。

- 🚀 使用 uv 快速创建 Django 项目并安装 django-bolt 和 pydantic-ai 依赖
- ⚡ 创建基于 PydanticAI Agent 的异步流式 API 端点，支持实时文本流输出
- 🎯 支持多种模型（示例使用 Claude），通过环境变量设置 API 密钥
- 🔧 运行`runbolt --dev`启动开发服务器，用 curl 测试流式响应
- 💡 相比 FastAPI，Django-Bolt 提供同样的简洁性，同时拥有 Django 的完整生态（管理界面、ORM、测试框架等）

---

### [使用 Python 标准库进行 HTTP GET 请求 – alexwlchan](https://alexwlchan.net/2026/python-http-with-the-stdlib/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [HTTP GET requests with the Python standard library – alexwlchan](https://alexwlchan.net/2026/python-http-with-the-stdlib/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

本篇文章探讨了在 Python 中使用标准库`urllib.request`替代第三方 HTTP 库（如 httpx、requests）的可能性，作者因 httpx 维护停滞而转向标准库，并创建了个人工具库`chives.fetch`来简化 GET 请求。

- 📦 **作者背景**：因 httpx 库维护停滞（GitHub 问题关闭、近一年无更新），作者考虑使用 Python 标准库`urllib.request`替代第三方 HTTP 库。
- 🛠️ **使用场景**：作者仅需基础 GET 请求（手动脚本、少量请求、无代理/认证），无需连接池、HTTP/2 等高级功能。
- 🔧 **API 对比**：`urllib.request`的 GET 请求代码冗长（需手动处理 URL 拼接、参数编码、请求对象构建），而第三方库（如 httpx）更简洁。
- 📝 **自定义封装**：作者在`chives.fetch`中创建`build_request`和`fetch_url`函数，简化请求构建和响应获取，支持参数、头信息、SSL 上下文。
- 🔒 **依赖管理**：`fetch_url`依赖`certifi`库（提供 Mozilla 根证书），作者认为该依赖轻量且可控，可接受。
- 🖼️ **图片下载**：针对图片下载场景，作者编写`download_image`函数，根据`Content-Type`自动选择文件扩展名（如.jpg、.png），并避免覆盖已有文件。
- ⚠️ **功能限制**：该方案不支持超时设置、流式响应、POST 请求或错误状态码的自定义处理，适合简单脚本场景。
- 🧪 **测试与打包**：代码集成到个人库`chives`中，使用`vcrpy`库进行测试，已在作者所有个人脚本中稳定运行。

---

### [智能体编程实用指南 - YouTube](https://www.youtube.com/watch?v=QrfsX-sW6QI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [A Practical Guide to Agentic Coding - YouTube](https://www.youtube.com/watch?v=QrfsX-sW6QI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

本頁面為 YouTube 的資訊與政策總覽，涵蓋平台基本資訊、法律條款及用戶支援等面向。

- 📰 新聞中心：提供 YouTube 官方最新消息與公告
- ©️ 版權：說明內容創作者的版權保護與相關規範
- 📞 聯絡我們：提供用戶與平台聯繫的管道
- 🎬 創作者：為內容創作者提供的資源與支援
- 📢 刊登廣告：說明廣告合作與投放相關資訊
- 📜 條款：列出使用 YouTube 時需遵守的服務條款
- 🔒 私隱：說明個人資料收集與使用的隱私政策
- 🛡️ 政策及安全：規範平台內容與用戶行為的安全準則
- ⚙️ YouTube 的運作方式：解釋平台推薦與內容審核機制
- 🧪 測試新功能：介紹 YouTube 正在測試的新功能
- 📅 © 2026 Google LLC：標示版權歸屬與年份

---

### [2026 年选择 Python 日志库 · Dash0](https://www.dash0.com/guides/python-logging-libraries?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Choosing a Python Logging Library in 2026 · Dash0](https://www.dash0.com/guides/python-logging-libraries?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

以下是您提供内容的摘要：

本文提供了 Python 日志库的全面指南，涵盖了标准库、structlog、Loguru、Logbook 和 picologging，并比较了它们的性能、集成方式和适用场景。

- 📚 **标准库 `logging`**：是 Python 的基石，与所有框架和 OpenTelemetry 集成最佳，但配置繁琐，上下文传播需要手动实现。
- ⚡ **structlog**：性能最佳（比标准库快约 2 倍），通过处理器链和`contextvars`实现优雅的上下文管理，推荐作为大多数团队的升级选择。
- 🚀 **Loguru**：以极简配置著称，单行代码即可实现结构化 JSON 输出和异常处理，但使用全局 logger，缺乏原生 OpenTelemetry 集成。
- 🧩 **Logbook**：提供上下文敏感的处理器栈，但缺乏结构化输出和 OpenTelemetry 支持，不建议新项目使用。
- 🐢 **picologging**：微软开发的 C 语言实现，速度提升 4-17 倍，但项目已停滞，不支持 Python 3.13/3.14，不适用于生产环境。
- 🔧 **框架集成**：Django 与标准库深度绑定；FastAPI 中 structlog 的`contextvars`集成最佳；Flask 对库的选择最不敏感。
- 📊 **性能基准**：structlog 在简单消息场景下最快（2.79µs），所有库在 10 万 + ops/s下均足够快，瓶颈通常来自日志频率而非库本身。
- 🎯 **选择建议**：大多数应用从标准库+JSON 格式化器开始；需要更好 API 和性能时升级到 structlog；追求极简配置时选择 Loguru。
- 💡 **核心要点**：库的选择不如实践重要——结构化输出、一致的上下文传播、合理的日志级别和良好的字段规范才是生产环境日志的关键。

---

### [软件开发培训 - Geekuni 博客：学习并发 - 深入探索 Python 多线程](https://blog.geekuni.com/2026/04/python-concurrency.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Software development training - Geekuni blog: Learn concurrency - a deep dive into multithreading with Python](https://blog.geekuni.com/2026/04/python-concurrency.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

本文深入探討了 Python 並發編程，從基礎概念到 GIL（全域解釋器鎖）的移除，並通過豐富的程式碼範例展示了多執行緒的效能提升與潛在陷阱。

- 🧠 **核心概念解析**：釐清了順序、並發、並行、多執行緒等術語的差異，並解釋了 GIL 如何限制 Python 的 CPU 密集型任務。
- ⚙️ **GIL 的歷史與移除**：說明了 GIL 最初為簡化記憶體管理而設計，但如今已成為高效能計算的瓶頸，因此 PEP 703 引入了可選的「自由執行緒」Python。
- 🛠️ **安裝與切換**：提供了使用 `uv` 安裝自由執行緒 Python 的方法，並示範如何透過命令列參數 `-X gil=1` 開關 GIL。
- ⚠️ **自由執行緒的風險**：列出了競態條件、記憶體洩漏、死鎖、不安全的迭代器以及 C 擴展漏洞等注意事項，強調即使沒有 GIL，執行緒安全仍需開發者自行維護。
- 🚀 **效能對比範例**：透過計算費氏數列的「尷尬並行」任務，展示了無 GIL 環境下效能提升約 5 倍（0.81 秒 vs 4.13 秒）。
- 🐛 **共享資源的陷阱**：使用計數器範例演示了競態條件如何導致結果錯誤（預期 800 萬，實際 110 萬），並指出 GIL 僅能部分隱藏此問題。
- 🔒 **同步鎖的雙面性**：使用 `threading.Lock` 修復計數器後，結果正確但無 GIL 版本反而更慢，原因是鎖競爭和 CPU 快取抖動。
- 💡 **最佳實踐：消除共享狀態**：透過 `concurrent.futures` 讓每個執行緒使用本地計數器，無 GIL 版本速度提升約 5 倍（0.056 秒 vs 0.101 秒），驗證了「分而治之」的黃金法則。
- 🔌 **C 擴展相容性**：指出 NumPy、Pandas 等依賴 C 擴展的函式庫尚未完全支援自由執行緒，但 Python 會自動啟用 GIL 作為安全網，且社群正在積極遷移。
- 🏁 **結論與展望**：強調無 GIL Python 並非萬能藥，需理解並行架構才能發揮優勢，並推薦了結合 `asyncio` 與多執行緒進行網頁爬蟲等進階應用。

---

### [获取失败](https://machinelearningmastery.com/building-ai-agents-in-python-with-pydantic-ai/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Failed to retrieve](https://machinelearningmastery.com/building-ai-agents-in-python-with-pydantic-ai/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

无法总结：获取内容失败，状态码 520。

---

### [GitHub - huggingface/ml-intern: 🤗 ml-intern：一个开源机器学习工程师，能阅读论文、训练模型并部署机器学习模型 · GitHub](https://github.com/huggingface/ml-intern?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [GitHub - huggingface/ml-intern: 🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models · GitHub](https://github.com/huggingface/ml-intern?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

ML Intern 是一个能自主研究、编写并发布高质量机器学习代码的开源 AI 工程师，深度集成 Hugging Face 生态系统。

- 🤖 **自主 ML 工程师**：能够独立研究论文、训练模型并发布 ML 代码，无需人工干预
- 🔧 **快速安装与配置**：通过`git clone`和`uv sync`即可安装，支持 Anthropic 和 OpenAI 模型
- 🛠️ **多种使用模式**：支持交互式聊天模式和头模式（单次提示自动执行）
- 🔔 **Slack 通知集成**：支持通过 Slack Web API 发送审批、错误和完成状态通知
- 🏗️ **模块化架构**：包含代理循环、上下文管理器、工具路由器和死循环检测器
- 📋 **丰富的工具集**：可访问 HF 文档、仓库、数据集、论文、GitHub 代码搜索和沙箱工具
- 🔄 **事件驱动机制**：通过事件队列处理用户输入、工具调用、审批请求和状态更新
- 💻 **技术栈**：主要使用 Python（77%）和 TypeScript（22.7%），支持 MCP 服务器扩展

---

### [GitHub - ComposioHQ/awesome-codex-skills: 一份精选的实用 Codex 技能列表，用于在 Codex CLI 和 API 中自动化工作流程。](https://github.com/ComposioHQ/awesome-codex-skills?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [GitHub - ComposioHQ/awesome-codex-skills: A curated list of practical Codex skills for automating workflows across the Codex CLI and API. · GitHub](https://github.com/ComposioHQ/awesome-codex-skills?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

该仓库收集了实用的 Codex 技能，用于自动化 Codex CLI 和 API 的工作流程，涵盖开发、协作、数据分析等类别，并提供安装、使用和创建指南。

- ⭐ 仓库拥有 5.2k Star 和 326 个 Fork，包含 35 个提交记录，社区活跃
- 🔧 提供快速安装方法：推荐使用 Skill Installer 脚本一键安装，也支持手动复制文件夹到 `$CODEX_HOME/skills` 目录
- 🧩 技能以模块化指令包形式存在，每个技能包含 `SKILL.md` 文件（含元数据和步骤指导），Codex 根据描述自动触发匹配技能
- 💻 开发与代码工具类技能：包括代码审查（brooks-lint）、代码库迁移（codebase-migrate）、CI 修复（gh-fix-ci）、Sentry 问题诊断（sentry-triage）等
- 🤝 生产力与协作类技能：支持连接 1000+ 应用（connect）、管理 Linear/Jira 问题（issue-triage）、生成会议纪要和行动项（meeting-notes-and-actions）、整理发票（invoice-organizer）等
- 📝 沟通与写作类技能：包括邮件起草/润色（email-draft-polish）、生成变更日志（changelog-generator）、内容研究与写作（content-research-writer）、简历定制（tailored-resume-generator）等
- 📊 数据与分析类技能：提供电子表格公式助手（spreadsheet-formula-helper）、竞品广告分析（competitive-ads-extractor）、Datadog 日志过滤（datadog-logs）、开发者成长分析（developer-growth-analysis）等
- 🛠️ 元工具与实用技能：包含品牌指南应用（brand-guidelines）、画布设计（canvas-design）、图片增强（image-enhancer）、技能创建模板（skill-creator）等
- 📖 创建新技能需遵循标准目录结构（SKILL.md + 可选 scripts/references/assets 文件夹），描述要详尽说明触发条件，主体保持执行步骤简洁

---

### [GitHub - patrick-toulme/pyptx：一个用于在JAX和PyTorch中编写Hopper和Blackwell架构Nvidia PTX 的 Python DSL](https://github.com/patrick-toulme/pyptx?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [GitHub - patrick-toulme/pyptx: A Python DSL to write Nvidia PTX for Hopper and Blackwell in JAX and PyTorch · GitHub](https://github.com/patrick-toulme/pyptx?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

pyptx 是一个用 Python 编写 NVIDIA PTX 内核的 DSL，支持在 JAX、PyTorch 和 torch.compile 中运行，覆盖 Ampere、Hopper 和 Blackwell 架构。

- 🚀 **高性能内核**：在 Blackwell B200 上实现 1240 TFLOPS（77% cuBLAS），Hopper H100 上实现 815 TFLOPS，Ampere A100 上实现 162 TFLOPS
- 🛠️ **直接 PTX 指令**：每个 `ptx.*` 调用对应一条 PTX 指令，无优化器或自动调优器，确保精确控制
- 🔄 **多运行时支持**：同一内核可在 PyTorch eager、torch.compile 和 JAX jit 中无缝运行，通过 CUDA 图重放实现低延迟（~4 µs）
- 📚 **丰富示例**：提供 Ampere、Hopper 和 Blackwell 的完整示例，包括 GEMM、RMS 归一化、层归一化、SwiGLU 和注意力机制
- 🔧 **PTX 转译器**：支持将现有 PTX（来自 nvcc、Triton 等）转译为 Python，并保持字节一致性（218+ 文件测试）
- 🎯 **架构覆盖**：支持 sm_80（Ampere）、sm_89（Ada）、sm_90a（Hopper）和 sm_100a/sm_120（Blackwell），自动检测 GPU 目标
- 📦 **简单安装**：通过 pip 安装，可选 PyTorch 和 JAX 支持，推荐安装 ninja 以优化启动性能
- 📊 **性能基准**：提供完整基准测试脚本，可复现结果，并展示与 cuBLAS 和 PyTorch 的对比

---

### [GitHub - tile-ai/tilelang: 专为简化高性能 GPU/CPU/加速器内核开发而设计的领域特定语言](https://github.com/tile-ai/tilelang?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [GitHub - tile-ai/tilelang: Domain-specific language designed to streamline the development of high-performance GPU/CPU/Accelerators kernels · GitHub](https://github.com/tile-ai/tilelang?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

TileLang 是一个专为高性能 GPU/CPU 内核开发设计的领域特定语言，基于 TVM 编译器基础设施，通过 Pythonic 语法实现生产力与底层优化的平衡。

- 🧩 提供 TileLang Puzzles 互动学习平台，含 10 个渐进式编程谜题
- 🚀 新增 CuTeDSL 后端，支持编译至 NVIDIA CUTLASS CuTe DSL
- 🔬 集成 Z3 定理证明器，实现 SMT 符号推理以增强优化与正确性验证
- 🔧 迁移至 apache-tvm-ffi，显著降低 CPU 开销
- 📦 发布 v0.1.6.post2，为 Python 3.8 兼容的最终版本
- 🍎 新增 Apple Metal 设备支持
- 🎉 支持华为昇腾芯片的 AscendC 和 AscendNPU IR 后端
- 🚀 引入 T.gemm_sp 实现 2:4 稀疏张量核心支持
- ✨ 新增 NVRTC 后端，大幅缩短 cute 模板编译时间
- 🚀 为 AMD MI300X 提供高性能 FlashMLA 实现
- 🚀 仅用 80 行 Python 代码实现与 FlashMLA 性能相当的 MLA 解码
- ✨ 新增 WebGPU 代码生成支持
- 🚀 发布 v0.1.0 版本
- 🚀 添加调试工具，包括 T.print 和内存布局绘图器
- ✨ 正式开源 tile-lang 项目
- 🖥️ 已测试设备包括 NVIDIA H100、A100、V100、RTX 4090 等，以及 AMD MI250、MI300X
- 📊 支持矩阵乘法、反量化 GEMM、Flash Attention、线性注意力等多种算子
- 🏆 在 H100 上实现 MLA 解码、Flash Attention 和矩阵乘法的高性能基准测试
- 📦 提供 pip 安装、源码构建和夜间版本三种安装方式
- 🚀 快速入门示例展示带布局优化、L2 缓存交织和流水线的高级 GEMM 内核编写
- 🔍 深入示例包括反量化 GEMM、FlashAttention、线性注意力和卷积实现
- 📋 关注 v0.2.0 发布计划以了解即将推出的功能
- 💬 加入 Discord 社区进行讨论与协作
- 🙏 感谢 TVM 社区及北京大学、微软研究院的贡献者

---

### [GitHub - Nour833/StegoForge：终极隐写术与数字取证工具包。在图像、音频、视频、文档和网络数据包中隐藏和提取数据，或运行11种高级检测引擎以发现隐藏的有效载荷。](https://github.com/Nour833/StegoForge?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [GitHub - Nour833/StegoForge: The ultimate steganography and digital forensics toolkit. Hide and extract data across images, audio, video, documents, and network packets, or run 11 advanced detection engines to uncover hidden payloads. · GitHub](https://github.com/Nour833/StegoForge?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

StegoForge 是一个集隐写术、数字取证和隐蔽通信于一体的模块化工具包，支持在图像、音频、视频、文档等多种载体中隐藏和提取数据，并具备先进的机器学习检测能力。

- 🛡️ 提供零依赖的独立二进制文件，无需安装 Python 环境即可运行
- 🚀 支持快速编码、解码、CTF 取证、批量处理等多种命令行操作
- 🧠 采用 AES-256-GCM 加密，并集成 Argon2 密钥派生，保障数据安全
- 🎨 提供交互式菜单和 Web UI，适合初学者和高级用户
- 🖼️ 支持 PNG、JPEG、MP4、WAV、PDF 等 10 余种载体格式
- 🔍 内置 11 种检测引擎，包括卡方分析、RS 分析、机器学习 CNN 模型
- 🌐 支持网络隐蔽信道（TCP 字段、定时信道）和 HTTP 死点投递
- 📦 具备社交平台生存性模拟（Twitter、Instagram 等），通过里德 - 所罗门编码增强鲁棒性
- ⚖️ 仅限教育、CTF 和合法安全测试使用，严禁非法用途

---

### [GitHub - russellromney/honker: 为 Postgres NOTIFY/LISTEN语义提供SQLite扩展及绑定的持久队列、流、发布/订阅和调度器](https://github.com/russellromney/honker?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [GitHub - russellromney/honker: SQLite extension + bindings for Postgres NOTIFY/LISTEN semantics with durable queues, streams, pub/sub, and scheduler · GitHub](https://github.com/russellromney/honker?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

honker 是一个 SQLite 扩展，为 SQLite 添加了类似 Postgres NOTIFY/LISTEN 的语义，支持持久化发布/订阅、任务队列和事件流，无需客户端轮询或额外代理。

- 📦 **核心功能**：在 SQLite 中实现持久化任务队列、流式事件和临时通知，支持跨进程通信，延迟低至个位数毫秒。
- 🔄 **事务性集成**：任务入队、事件发布可与业务写入在同一个事务中原子提交，回滚时自动撤销，避免双写问题。
- 🚀 **多语言支持**：提供 Python、Node.js、Rust、Go、Ruby、Bun、Elixir 等语言绑定，以及 SQLite 可加载扩展，任何语言均可使用。
- ⚙️ **高性能设计**：使用 PRAGMA data_version 每 1ms 轮询检测提交，替代应用层轮询，空闲时几乎无 SQL 查询开销。
- 📊 **丰富特性**：支持任务重试、优先级、延迟执行、死信表、速率限制、定时任务（crontab）、任务结果存储和死信处理。
- 🔧 **易用集成**：可与 SQLAlchemy、Django、Drizzle 等 ORM 配合使用，通过几行代码即可嵌入 Web 框架（如 FastAPI）。
- 🛡️ **可靠性**：基于 SQLite ACID 保证崩溃安全，任务可见性超时后自动重新分配，支持死信迁移。
- 📈 **性能测试**：在现代笔记本上可处理每秒数千条消息，跨进程唤醒延迟约 1-2ms（M 系列芯片）。
- 📚 **开发与贡献**：项目采用 Apache 2.0 许可，提供完整测试套件和基准测试，支持 Rust/Python 覆盖率报告。

---

### [GitHub - besimple-oss/broccoli: Broccoli 将 Linear 工单转化为已发布的 PR — 由 Claude 和 Codex 驱动，运行在您自己的 Google Cloud 或 Blaxel 容器上。](https://github.com/besimple-oss/broccoli?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [GitHub - besimple-oss/broccoli: Broccoli turns Linear tickets into shipped PRs — powered by Claude and Codex, running on your own Google Cloud or Blaxel containers. · GitHub](https://github.com/besimple-oss/broccoli?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

Broccoli OSS 是一个将 Linear 工单自动转化为已合并 PR 的开源 AI 工具，基于 Claude 和 Codex，部署在你的 Google Cloud 上。

- 🥦 **核心功能**：将 Linear 工单自动转化为可审查的 PR，实现自动化开发流程。
- 🔒 **安全可控**：部署在你自己的 GCP 项目里，数据和密钥完全由你掌控，无第三方控制面。
- 🧱 **生产就绪**：采用无服务器 Cloud Run、Secret Manager、Webhook 去重和持久化任务状态，非玩具项目。
- 🧩 **可定制提示**：提供可复刻、调优和版本管理的提示模板。
- ⚡ **AI 代码审查**：每次 PR 都会由 Claude 和 Codex 进行审查，留下可操作的评论并推送修复提交。
- 🛠️ **快速部署**：约 30 分钟即可完成部署，只需一个引导脚本、一个配置文件和两个 Webhook。
- 📋 **部署流程**：包含创建 GCP 项目、GitHub App、Linear 机器人用户、配置密钥、构建镜像、运行引导、安装应用、迁移数据库、注册 Webhook 和运行测试等步骤。
- 🏗️ **架构**：由两个 Cloud Run 工作负载（服务和运行器）和一个共享的 Postgres 数据库组成。
- 📊 **可观测性**：提供数据库表用于检查任务状态、审计被忽略的 Webhook 响应，并提供安全的重试机制。
- 🔑 **IAM 权限**：采用“首次部署即工作”的权限模型，上线后可收紧权限。
- 💻 **本地开发**：支持 `uv sync --dev` 和 `uv run pytest` 进行本地开发和测试。
- 📚 **文档完善**：提供架构、任务合同、贡献指南和变更日志等文档。

---

### [IndyPy：闪电演讲 ⚡，2026 年 5 月 5 日星期二，晚上 7:00 | 聚会](https://www.meetup.com/indypy/events/311855002/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [IndyPy: Lightning Talks ⚡, Tue, May 5, 2026, 7:00 PM   | Meetup](https://www.meetup.com/indypy/events/311855002/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

IndyPy 闪电演讲活动将于 5 月 5 日举行，这是一个混合形式的活动，旨在通过 5 分钟以内的快速演讲分享 Python 社区的想法和经验。

- ⚡ 活动形式：混合活动（线上 + 线下），时间 5 月 5 日晚上 7-9 点（美东时间）
- 📍 线下地点：印第安纳波利斯 E-gineering 公司（8415 Allison Pointe Blvd）
- 🎤 演讲主题：Python 技巧、工具、项目经验、AI 实验等，演讲时长不超过 5 分钟
- 📅 重要日期：演讲提案截止 4 月 30 日，演讲名单 5 月 4 日下午 5 点公布
- 🏆 活动流程：7-7:15pm 公告介绍，7:15-8:15pm 闪电演讲，8:15-8:30pm 抽奖，8:30-9pm 社交
- 🤝 赞助商：Six Feet Up（组织赞助）、JetBrains（白金赞助）、E-gineering（招待赞助）
- 💻 远程参与：注册获取 Zoom 链接
- 🎯 目标：鼓励社区成员分享多样化的 Python 观点和见解，营造轻松交流氛围

---

### [PyData 埃克塞特 #13 - 开源社区讲座 @ 创新中心，2026 年 5 月 6 日星期三，下午 6:45 | Meetup](https://www.meetup.com/pydata-exeter/events/314216811/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [PyData Exeter #13 - Open Source Community Talks @ Innovation Hub, Wed, May 6, 2026, 6:45 PM   | Meetup](https://www.meetup.com/pydata-exeter/events/314216811/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

PyData Exeter #13 是一场开源社区聚会，于 5 月 6 日在埃克塞特创新中心举行，提供免费披萨和饮品，包含三场关于 Python、数据和开源软件的演讲，并设有社交环节。

- 🗺️ Hugh Evans 的演讲“用 Python 和网络爬虫绘制 PyData 社区地图”，展示了如何通过爬取 Meetup 数据构建社区地图，涉及地理编码和 Folium 地图制作，并呼吁支持本地 PyData 团体。
- 🧠 Anna Andersson 的演讲“用本体论组织 PyData 聚会：从模式到推理”，通过组织聚会的实际案例，演示如何构建本体模型来结构化数据，并利用推理发现隐含关系，使本体论变得具体实用。
- 📉 Venkata Prudhvi Kante 的演讲“本地商店正以创纪录速度关闭——我每天路过空置店铺，直到数据揭示惊人真相”，基于爬取的十年英国零售关闭数据，分析本地商店消失的真实原因，并介绍其正在构建的应对方案。

---

### [PyData 康沃尔 - 聚会 #4：数据工程版，2026 年 5 月 7 日星期四，下午 6:30 | 聚会](https://www.meetup.com/pydata-cornwall/events/314013646/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [PyData Cornwall - Meetup #4: The Data Engineering Edition, Thu, May 7, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-cornwall/events/314013646/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

PyData Cornwall 第四次聚会以数据工程为主题，聚焦数据管道、AI 与社区实践。

- 📊 活动聚焦数据工程，探讨如何构建数据管道、清洗数据，为 AI 提供准确上下文。
- 🗺️ Hugh Evans 展示用 Python、网络爬虫和 Folium 制作 PyData 社区地图，并分享规模化数据抓取与运维经验。
- 🤖 Dave Taylor 强调 AI 需要更好的数据工程而非更强模型，讨论 LLM 管道中的常见失败模式与改进方法。
- ⚡ 闪电演讲包括 Polars 库介绍，并开放投稿机会。
- 🍕 活动提供披萨和饮品，结束后可前往附近酒吧交流。
- 🏠 地点在纽基 Flowmoco，适合海边学习与社交。
- 📝 鼓励社区成员提交演讲，欢迎首次演讲者并协助准备。
- 💬 通过 Discord 联系组织者，遵守 PyData 行为准则。
- 💸 欢迎赞助商支持披萨、饮品或未来活动场地。

---

### [混合 MI Python：从 Sphinx 切换到 Markdown，2026 年 5 月 7 日，星期四，晚上 7:00 | Meetup](https://www.meetup.com/michigan-python/events/313464728/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Hybrid MI Python: Switching from Sphinx to Markdown, Thu, May 7, 2026, 7:00 PM   | Meetup](https://www.meetup.com/michigan-python/events/313464728/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

本次混合活动介绍了从 Sphinx 和 reStructuredText 迁移到 Markdown 和 MkDocs 的文档方案。

- 📅 活动时间：2025 年 5 月 7 日晚上 7 点至 8 点（美东时间），每月第一个周四举行，持续至 2027 年 1 月。
- 📍 地点：密歇根州安娜堡 Cahoots，同时提供线上参与方式。
- 🎤 主讲人：Dan Y.和 Evan S.，Dan Y.是密歇根 Python 超级组织者。
- 📖 演讲主题：为何 Markdown 比 reStructuredText 更适合项目文档，以及如何用 MkDocs 实现类似 Sphinx 的功能。
- 🔧 案例分享：如何自动化迁移多个大型 Sphinx 文档库到 Markdown，并鼓励社区参与。
- ⏰ 议程安排：7:00 开场，7:10 演讲，7:50 问答环节。

---

### [编写测试：良好意图，糟糕实践，2026 年 5 月 7 日星期四下午 6:30 | 聚会](https://www.meetup.com/madison-python/events/314523681/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Writing Tests: Good Intentions, Bad Practice, Thu, May 7, 2026, 6:30 PM   | Meetup](https://www.meetup.com/madison-python/events/314523681/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

### 概述总结
Dave Hoese 在 MadPy 活动中分享关于软件测试的常见陷阱与最佳实践，强调测试应注重实用性而非盲目遵循教条。

- 📅 **活动信息**：5 月 7 日周四晚 6:30-8:30，在麦迪逊公共图书馆中央馆举行，由 Ed R. 和 MadPy 主办。
- 🎯 **核心观点**：测试虽重要但易陷入误区，需关注实际应用中的陷阱与最佳实践。
- 🛠️ **内容涵盖**：介绍常用测试插件和工具，以及如何为用户编写测试工具的经验。
- 👨‍💻 **演讲者背景**：Dave Hoese 是威斯康星大学麦迪逊分校空间科学与工程中心的软件开发者，专攻大气科学数据分析工具。
- 🔗 **相关主题**：涉及数据科学、Python、开源、软件开发及科学计算等领域。

---

### [拥抱噪声：数据损坏如何让模型更智能，2026 年 5 月 4 日（周一）下午 5:30 | Meetup](https://www.meetup.com/pydata-st-louis/events/314320971/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [Embracing Noise: How Data Corruption Can Make Models Smarter , Mon, May 4, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-st-louis/events/314320971/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

本次 PyData 圣路易斯活动探讨了如何利用噪声和数据损坏来提升机器学习模型的性能。

- 🧠 核心观点：在训练中引入受控的数据损坏（如高斯噪声、掩码、标签翻转）可作为一种正则化手段，提升模型鲁棒性并减少过拟合
- 🗓️ 活动安排：5:30 PM 开始披萨与社交，6:15 PM 正式演讲，6:50 PM 至 7:30 PM 进行问答与交流
- 🎯 适用人群：对数据科学、机器学习或构建更稳健 AI 系统感兴趣的学生、专业人士、爱好者及初学者
- 🛠️ 技术内容：涵盖真实世界数据的噪声特性、损坏数据的正则化作用、不同技术方法（高斯噪声、掩码、标签翻转），以及计算机视觉的 Python 实践示例
- 🏢 场地支持：由 Spark Coworking 提供场地，助力本地数据科学社区发展
- 🌐 社区背景：PyData St. Louis 隶属于全球 PyData 社区，是 NumFOCUS 的教育项目，致力于推广开放数据科学实践

---

### [PyData 伦敦 - 第 107 次聚会，2026 年 5 月 5 日星期二，下午 6:30 | Meetup](https://www.meetup.com/pydata-london-meetup/events/314472144/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

**原文标题**: [PyData London - 107th Meetup, Tue, May 5, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-london-meetup/events/314472144/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026)

PyData London 第 107 次聚会将于 5 月 5 日举行，包含三场技术演讲，主题涵盖数据去重、模型推理和微型 GPT 构建。活动由 NumFOCUS 和 Man Group 赞助，提供免费食物和饮料，需携带有效身份证件入场。

- 🔗 数据去重：Robin Linacre 介绍 Splink 库，用于大规模数据集的概率记录链接和去重，采用无监督学习，适合有 Python 基础者
- 🧠 模型推理：Filip Makraduli 探讨小型嵌入模型部署的挑战，对比 LLM 推理，提出高效的多模型基础设施方案
- 🤖 微型 GPT：Ian Ozsvald 带领现场运行 MicroGPT，用 200 行 Python 代码理解 GPT 工作原理，无需依赖库
- 🆔 安全要求：入场需出示有效带照片身份证件，由大楼安保检查
- 🍕 免费餐饮：Man Group 提供免费食物和饮料，活动后有社交时间
- 📋 行为准则：活动遵循 NumFOCUS 行为准则，如有问题请联系组织者
- ⏰ 时间安排：18:30 开门签到，19:00 演讲开始，21:00 后可在 The Banker 酒吧继续交流

---
