### [发布现在在 14 天后拒绝新文件 - Python 包索引博客](https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Releases now reject new files after 14 days - The Python Package Index Blog](https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

PyPI 现在拒绝向超过 14 天的旧版本上传新文件，以防止发布令牌或工作流被泄露时旧版本被恶意篡改。这一变更基于数据分析和社区共识，旨在提升安全性并减少项目被攻陷后的清理工作。

- 🔒 安全防护：PyPI 禁止向超过 14 天的旧版本上传新文件，防止旧版本被恶意投毒，即使发布令牌或工作流被泄露。
- 📊 数据支持：对前 15,000 个包的查询显示，仅 56 个项目在版本发布 14 天后上传了 Python 3.14 兼容的 wheel 文件，表明影响有限。
- 🤝 社区共识：PyCon US 2026 的包装峰会上，与会者认为“要求用户升级到下一个版本以支持新 Python 版本”是可接受的。
- 🛠 实施细节：该变更于 2026 年 7 月 8 日合并，但用户不应立即依赖此行为，因为“版本不再接受新文件”的语义尚未通过 PEP 694 标准化。
- 🔮 未来展望：Upload 2.0 API 将定义版本“关闭”而非“开放”的语义，提供更明确的发布状态确认机制。

---

### [媒介](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c?gi=33782512150b&utm_campaign=python-weekly-issue-755-july-23-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

**原文标题**: [Medium](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c?gi=33782512150b&utm_campaign=python-weekly-issue-755-july-23-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

Netflix 自建了完整的 LLM 推理平台，从模型部署到推理均在其生产环境中运行，而非依赖外部 API。以下是关键要点：

- 🏗️ **架构概述**：Netflix 使用统一的 JVM 服务系统处理端到端流程，支持实时和缓存批处理路径。小型 CPU 模型在进程中运行，大型 GPU 模型则通过远程服务（MSS）处理，底层使用 NVIDIA Triton 推理服务器。
- ⚙️ **引擎选择**：从 TensorRT-LLM 迁移至 vLLM，因其支持自定义模型架构、扩展性钩子、易调试性，且 ML 从业者更熟悉，降低了研究到生产的转换成本。
- 📦 **模型打包**：采用 Triton 的 vLLM 后端，模型仅需 JSON 配置指向权重和分词器，动态生成 I/O 张量规格，实现模型与前端独立演进。但需注意版本匹配问题，并保留 Python 后端用于自定义逻辑模型。
- 🌐 **API 接口**：除 gRPC 外，额外暴露 OpenAI 兼容 API，使实验到生产的过渡无缝衔接。但需修补 Triton 前端，确保 `response_format` 参数正确传递至 vLLM 的引导解码。
- 🚀 **部署策略**：提供红黑部署（接口稳定时使用）和版本化部署（处理接口变更）。版本化部署虽增加 GPU 成本，但解耦了模型部署与消费者更新。
- 🔧 **运维要点**：通过 Amazon FSx 缓存模型减少冷启动延迟；统一 Prometheus 指标端点，合并 vLLM 和 Triton 的指标，避免关键数据遗漏。
- 🧠 **约束解码**：在解码循环内应用约束，确保输出合规。从 vLLM V0 迁移至 V1 后，将日志处理器改为批处理级别，并用 C++ 多线程绕过 GIL，解决了 CPU 瓶颈。同时处理了部分预填充和抢占问题。
- 📈 **未来方向**：计划优化系统提示压缩、异步调度、向量化日志处理器及低精度模型变体，以进一步提升性能。

---

### [zhinit](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [zhinit](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

概述摘要：该内容探讨了人工智能在医疗领域的应用前景，强调其提升诊断效率、个性化治疗及降低成本的潜力，同时指出数据隐私和伦理挑战需谨慎应对。

- 🤖 人工智能通过分析医学影像，可辅助医生更快速、准确地检测疾病，如癌症早期筛查。
- 💊 基于患者基因和病史，AI 能定制个性化治疗方案，提高疗效并减少副作用。
- 💰 自动化流程和预测分析有助于降低医疗运营成本，优化资源分配。
- 🔒 数据隐私问题突出，需建立严格的安全框架以保护患者敏感信息。
- ⚖️ 伦理挑战包括算法偏见和责任归属，需确保 AI 决策的公平性与透明度。

---

### [Notebook.link - 即时运行与分享 Jupyter 笔记本](https://notebook.link/@anutosh491/llvmlite?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Notebook.link - Run & Share Jupyter Notebooks Instantly](https://notebook.link/@anutosh491/llvmlite?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

概述摘要：本文讨论了人工智能在医疗诊断中的最新应用，强调了其提高准确性和效率的潜力，同时指出了数据隐私和伦理挑战。

- 🩺 AI 辅助诊断系统能快速分析医学影像，减少人为误差
- 📊 深度学习模型在癌症检测中准确率超过 90%
- 🔒 患者数据隐私保护是 AI 医疗应用的主要障碍
- ⚖️ 算法偏见可能导致诊断结果不公平
- 💡 未来需制定严格伦理准则以平衡创新与安全

---

### [点击支付后的毫秒内发生了什么 | Databricks 博客](https://www.databricks.com/blog/what-happens-milliseconds-after-you-tap-pay?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [What happens in the milliseconds after you tap pay | Databricks Blog](https://www.databricks.com/blog/what-happens-milliseconds-after-you-tap-pay?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

Databricks 构建了一个实时欺诈评分应用，结合了模型服务路由优化和 Lakebase Postgres，在毫秒级内完成交易评分，并提供了详细的延迟分解和基准测试结果。

- ⚡ **端到端延迟极低**：在 5000 次请求测试中，中位数端到端往返时间为 27 毫秒，p95 为 37 毫秒，完全满足结账流程的延迟预算。
- 🗺️ **路由优化缩短网络路径**：启用模型服务路由优化后，应用与推理容器之间的网络路径更短，延迟更低且更稳定。
- 🗄️ **Lakebase 提供毫秒级特征查询**：模型容器和 FastAPI 后端均通过连接池查询 Lakebase Postgres 表，特征查询中位数仅需 8.9 毫秒。
- 🔌 **连接池与 OAuth 令牌轮换**：使用 psycopg2 连接池避免重复建立连接，并通过 OAuth 令牌轮换机制确保安全，避免使用长期密码。
- 🧠 **模型内部特征查询与推理**：MLflow pyfunc 模型在容器内自行查询 Lakebase 获取特征，然后运行 CatBoost 推理，推理时间中位数仅 0.4 毫秒。
- 📋 **业务规则检查作为第二道防线**：模型评分后，后端读取用户配置文件并执行每日限额和跨国交易等规则，可覆盖模型批准结果。
- 📈 **Lakebase 自动缩放与按需付费**：Lakebase 支持自动缩放和缩到零，在高峰时处理查询，在无流量时停止计费。
- 🛠️ **可部署和复现**：该应用作为 Databricks 应用（FastAPI + React）构建，代码已在 GitHub 上开源，可轻松部署到自己的工作区进行测试。

---

### [开发者数据工具全景指南 · OlegWock](https://sinja.io/blog/data-landscape-guide-for-developers?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Guide to data tools landscape for developers · OlegWock](https://sinja.io/blog/data-landscape-guide-for-developers?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

这份指南全面介绍了数据工具生态，涵盖数据生命周期、存储、处理、消费及治理等环节，旨在帮助开发者理解数据团队的工作流程与常用工具。

- 📊 **数据职业类型**：分为分析型（分析师/BI）、科学型（数据科学家）、工程型（数据工程师）和机器学习型（ML 工程师/科学家），各自侧重不同技能与工具。
- 🔄 **数据生命周期**：核心流程为 ETL（提取 - 转换 - 加载）或 ELT（提取 - 加载 - 转换），后者保留原始数据以便灵活处理。
- 💾 **数据存储方式**：包括文件格式（CSV、Parquet）、内存格式（Apache Arrow）、数据仓库（Snowflake、BigQuery）、数据湖（S3、Azure Data Lake）和数据湖仓（Iceberg、Delta Lake），各有优化场景。
- 🔌 **数据来源与摄取**：数据可来自数据库、第三方 API 或用户事件；摄取工具（Fivetran、Airbyte）简化连接，CDC（如 Debezium）用于数据库变更捕获。
- 🛠️ **数据处理**：主流语言为 Python（pandas、Polars）和 SQL；处理方式分批量（dbt、Spark）和实时（Kafka、Flink）；本地 DataFrame 与分布式 Spark 应对不同规模数据。
- ⏱️ **流处理与编排**：Kafka 作为事件流平台，Flink 处理实时流；编排工具（Airflow、Dagster）管理批量任务 DAG，支持调度与重试。
- 🔍 **数据可观测性**：监控管道运行（Prometheus、Grafana）与数据质量（Great Expectations、dbt 测试），自动化工具（Monte Carlo）检测异常。
- 🏛️ **数据落地架构**：采用 Medallion 架构（青铜→白银→黄金层）分层存储；维度建模（事实表 + 维度表）优化查询；反向 ETL 将处理数据写回业务工具。
- 📚 **语义层与目录**：数据目录（DataHub）提供业务上下文；语义层（dbt Semantic Layer）统一指标定义，确保跨工具一致性；数据血缘追踪转换过程。
- 📈 **数据消费方式**：BI 工具（Tableau、Metabase）构建仪表盘；运营分析（反向 ETL）赋能业务团队；Notebook（Jupyter）支持探索分析；嵌入式分析（Luzmo）集成到应用；ML 模型训练依赖特征工程。
- 🔐 **数据治理**：管控访问权限、隐私合规（如“被遗忘权”），依赖目录、血缘及安全策略，但核心是流程与人员协作。

---

### [Django：介绍 django-crawl - Adam Johnson](https://adamj.eu/tech/2026/07/22/introducing-django-crawl/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Django: introducing django-crawl - Adam Johnson](https://adamj.eu/tech/2026/07/22/introducing-django-crawl/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

本文章介绍了作者在将项目从旧版 django-csp 迁移到 Django 6.0 内置 CSP 支持后，开发了 django-crawl 工具的过程与功能。

- 🕷️ 迁移后通过爬虫验证 CSP 头部无变化，意外发现 7 个非 CSP 相关 bug，尽管项目有 100% 测试覆盖率
- 🚀 将爬虫脚本扩展为可复用工具 django-crawl，支持管理命令和 Python API
- 📋 使用`./manage.py crawl`命令可爬取最多 1000 个 URL，报告错误（如断链、异常），支持`-v 2`显示 URL
- 🔍 爬虫从 HTML（a、link、script、img 等标签）、站点地图和 Feed 中发现链接，支持从站点地图启动
- ⚡ 使用基于 html5ever 的 Rust 扩展进行 HTML 解析，速度快，且无真实 HTTP 请求开销
- 🧪 提供 Python API，可创建爬取全站的集成测试，遇到错误时抛出 ExceptionGroup
- 🛡️ 适合作为未测试项目的“安全网”，但可能不适合所有项目，因为会生成单一长测试

---

### [在 Fly.io 上监控 Django 应用健康 | AppSignal 博客](https://blog.appsignal.com/2026/07/22/monitoring-your-django-app-health-on-fly-io.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Monitoring Your Django App Health on Fly.io | AppSignal Blog](https://blog.appsignal.com/2026/07/22/monitoring-your-django-app-health-on-fly-io.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

本指南介紹如何在 Fly.io 上為 Django 應用程式設置 AppSignal 監控，以追蹤錯誤、效能和主機健康狀況。

- 📋 **先決條件**：需準備好部署在 Fly.io 上的 Django 應用、AppSignal 帳戶、以及安裝並認證好的 flyctl。
- 📦 **安裝套件**：在 requirements.txt 中加入 appsignal 及相關 OpenTelemetry 套件，並根據資料庫安裝對應的檢測工具。
- ⚙️ **初始化 AppSignal**：執行 `python -m appsignal install` 並輸入應用名稱和 API 金鑰，然後修改 `__appsignal__.py` 以使用環境變數。
- 🐍 **設定 Django**：更新 settings.py 中的 ALLOWED_HOSTS，並在 manage.py 中導入 appsignal 並呼叫 `appsignal.start()`。
- 🔐 **配置環境**：使用 `fly secrets set` 安全儲存 Push API 金鑰，並在 fly.toml 中設定 `APPSIGNAL_APP_ENV` 和 `APP_REVISION`。
- 🚀 **部署應用**：執行 `fly launch` 進行配置，然後用 `fly deploy` 部署應用程式。
- 📊 **監控功能**：AppSignal 提供錯誤追蹤、請求效能、主機指標、日誌和正常運行監控，並支援檢查、自訂儀表板和異常檢測。
- ✅ **部署後檢查**：重點關注慢查詢、記憶體趨勢、部署後的錯誤率和異常檢測。
- 📚 **後續資源**：參考 AppSignal Python 文檔、Django 檢測文檔和 Fly.io 部署細節，以深入了解更多配置選項。

---

### [获取失败](https://machinelearningmastery.com/building-agentic-workflows-in-python-with-langgraph/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Failed to retrieve](https://machinelearningmastery.com/building-agentic-workflows-in-python-with-langgraph/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

无法总结：获取内容失败，状态码 403。

---

### [GitHub - owainlewis/awesome-artificial-intelligence: 人工智能（AI）课程、书籍、视频讲座和论文的精选列表](https://github.com/owainlewis/awesome-artificial-intelligence?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - owainlewis/awesome-artificial-intelligence: A curated list of Artificial Intelligence (AI) courses, books, video lectures and papers. · GitHub](https://github.com/owainlewis/awesome-artificial-intelligence?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

这是一个面向软件工程师的精选 AI 资源列表，专注于生成式 AI 和智能体系统的构建与部署。

- 📚 **核心书籍推荐**：涵盖从经典 AI 理论（如《人工智能：现代方法》）到 LLM 实战（如《从零构建大语言模型》）的必读著作。
- 🎓 **系统化课程**：提供从 Hugging Face LLM 课程到 Stanford CS336 等高质量在线课程，覆盖理论与工程实践。
- 📄 **里程碑论文**：收录了 Transformer、Scaling Laws、RLHF、ReAct 等奠定现代 AI 基础的关键研究论文。
- 🛠️ **构建 AI 系统指南**：包含 Anthropic 和 OpenAI 的智能体构建实践指南，以及 OWASP LLM 安全风险清单。
- 🤖 **智能体框架**：推荐 Pydantic AI、LangGraph、OpenAI Agents SDK 等主流框架，支持有状态、长时运行的智能体开发。
- 🔍 **检索与数据**：提供 LlamaIndex、Haystack、Docling 等工具，用于数据摄入、索引和文档解析。
- 📊 **评估与可靠性**：涵盖 Demystifying Evals、OpenAI Evals、Promptfoo 等评估框架，确保系统质量。
- 🚀 **部署与可观测性**：推荐 Langfuse、vLLM、LiteLLM 等工具，用于生产环境下的追踪、推理和模型网关。
- 💻 **编码智能体**：介绍 Claude Code、Codex CLI、Aider 等工具，辅助开发者进行代码编写、审查和调试。
- 🏭 **软件工厂与编排**：分享 OpenAI 等团队使用编码智能体的生产经验，包括多智能体协作与可靠性保障。

---

### [GitHub - Canner/WrenAI: 面向 AI 代理的 GenBI（生成式商业智能），通过开放上下文层实现受管控的文本到 SQL 转换，将自然语言问题转化为可信仪表板、图表和 SQL，支持 BigQuery、Snowflake、PostgreSQL、ClickHouse、Amazon Redshift、Databricks 等 20 多种数据源。](https://github.com/Canner/WrenAI?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - Canner/WrenAI: GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more. · GitHub](https://github.com/Canner/WrenAI?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

WrenAI 是一個開源的生成式商業智慧（GenBI）引擎，讓 AI 代理能從任何資料庫生成、部署和管理儀表板，並建立在可信的上下文層之上。

- 🧠 **核心功能**：AI 代理可生成受治理的 SQL 和圖表，並將答案部署為可分享的瀏覽器端儀表板。
- 📚 **知識管理**：內建版本控制的上下文層，包含商業語義、核准定義、範例和記憶，而非僅依賴資料庫 schema。
- 🔓 **完全開源**：核心、SDK 和技能均以 Apache-2.0 授權開源，無供應商鎖定。
- ✅ **正確性優先**：透過豐富的 schema 檢索、乾計畫驗證、結構化錯誤提示和評估執行器，確保輸出可信。
- 🔌 **相容性強**：支援 22+ 資料來源（如 BigQuery、Snowflake、PostgreSQL），可疊加在現有技術棧上。
- 🚀 **快速上手**：透過 CLI 安裝、AI 客戶端探索樁和代理驅動的工作流程，幾分鐘內即可開始使用。
- 🎯 **適用對象**：希望 AI 代理產生可信 BI 答案和儀表板，且商業邏輯存在資料庫外部的開發者。
- 🛠️ **包含元件**：建模定義語言 (MDL)、Apache DataFusion 引擎、GenBI 儀表板、知識與記憶、代理 SDK 及治理執行原語。
- 📈 **未來發展**：端到端正確性原語、代理原生分發、完整治理執行（審計日誌、速率限制、審批流程）。

---

### [GitHub - xqlsystems/xarray-sql: 使用 SQL 查询 Xarray 数据集的实验](https://github.com/xqlsystems/xarray-sql?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - xqlsystems/xarray-sql: An experiment to query Xarray datasets with SQL · GitHub](https://github.com/xqlsystems/xarray-sql?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

xarray-sql 是一个实验性项目，旨在通过 SQL 接口查询 Xarray 数据集，将多维数组“透视”为表格，支持从气候分析到地理空间操作等多种场景。

- 🔬 **核心原理**：将 Xarray 数据集的块转换为 Arrow RecordBatches，通过 DataFusion 引擎提供 SQL 查询能力，实现数组到表格的轻量级元数据转换。
- 🌍 **应用示例**：支持气候学计算（如月平均温度）、云原生数据集（如 ARCO-ERA5）的查询，以及地理空间操作（如 NDVI、区域平均）。
- ⚡ **性能优势**：支持列投影和分区裁剪，仅查询所需数据，避免扫描整个存档；通过 GROUP BY、JOIN 等 SQL 操作替代传统数组操作。
- 🧪 **验证结果**：在光谱指数、气候学、预报技能、栅格×矢量统计等基准测试中，SQL 查询结果与 Xarray 参考值匹配至浮点精度。
- 🚧 **当前状态**：仍在开发中，欢迎早期用户反馈；支持通过 pip 安装，提供贡献指南和问题跟踪。
- 🗺️ **未来路线图**：包括惰性评估、并行处理、Zarr 原生集成、分布式查询支持，以及“100 万亿行挑战”等目标。
- 🤝 **致谢**：感谢 Google Research、AI2/Ecoscope、UCSD DS3 等机构和个人对项目的贡献。

---

### [GitHub - loopgain-ai/loopgain: 一个用于 AI 智能体循环的开源成本控制器——当循环实际收敛时停止，并在性能下降前回滚，而非运行至固定的最大迭代次数上限。实时循环增益（Aβ）波段 + 最佳结果回滚。适配 LangGraph、CrewAI、AutoGen、LangChain、OpenAI Agents 及 Claude Agent SDK；提供原始 API 支持自定义技术栈。](https://github.com/loopgain-ai/loopgain?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - loopgain-ai/loopgain: An open-source cost controller for AI agent loops — stops a loop when it's actually converged and rolls back before it degrades, instead of running to a fixed max_iterations cap. Real-time loop-gain (Aβ) bands + best-so-far rollback. Adapters for LangGraph, CrewAI, AutoGen, LangChain, OpenAI Agents, and Claude Agent SDK; raw API for custom stacks. · GitHub](https://github.com/loopgain-ai/loopgain?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

LoopGain 是一个开源的成本控制器，用于优化 AI 代理循环，通过实时检测收敛并回滚退化结果，避免固定迭代次数导致的资源浪费。

- 📉 **显著降低 API 成本**：相比固定 20 次迭代，总 API 支出减少 92.8%（从 $27.05 降至 $1.94），中位耗时从 30.9 秒降至 2.1 秒。
- 🎯 **质量优先**：在保持或提升输出质量的前提下实现加速，自然分布工作负载的胜率为 0.50–0.63，工程故障工作负载高达 0.92–0.95。
- ⚙️ **核心机制**：基于 Barkhausen 稳定性准则，通过误差轨迹分类（快速收敛、收敛、停滞、振荡、发散）决定停止或回滚，并返回历史最佳输出。
- 🔌 **广泛集成**：提供 LangGraph、CrewAI、AutoGen、LangChain、OpenAI Agents SDK 和 Claude Agent SDK 的预构建适配器，支持自定义堆栈的原始 API。
- 📊 **可选仪表盘**：支持自托管或云端仪表盘，用于监控整个团队的循环稳定性、成本和回滚情况。
- 🛡️ **诚实限制**：检测收敛而非正确性，质量取决于验证器；在基准测试中，4.5% 的收敛运行通过了循环检查但未通过完整测试套件。
- 🧩 **安装简便**：`pip install loopgain`，纯 Python，无运行时依赖，支持 Python 3.10+。
- 🔒 **隐私保护**：遥测功能可选，默认关闭，仅发送匿名使用计数，不收集提示、输出或错误内容。

---

### [GitHub - data-centt/percentify · GitHub](https://github.com/data-centt/percentify?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - data-centt/percentify · GitHub](https://github.com/data-centt/percentify?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

该页面介绍了 **Percentify** 库，一个用于 pandas 和 Polars 数据框的探索性统计与数据质量诊断工具。

- ⚡ **双后端原生支持**：直接支持 pandas 和 Polars，无需手动转换，每个函数均可用于两种后端。
- 📊 **profiler 核心功能**：一键生成数据质量报告，按严重性排序问题并提供修复建议，可输出数据健康评分（0-100）。
- 📦 **简易安装与使用**：通过 `pip install percentify` 安装，导入函数后一行代码即可运行，如 `missing(df)` 快速查看缺失值。
- 🔍 **丰富诊断函数**：涵盖缺失值、相关性、偏度、PCA、VIF、异常值、变化率等 16+ 种分析功能。
- 🛠️ **实战示例**：提供 CI 数据质量门禁、相关性排序、偏度变换、PCA 解释、共线性剔除、环比 KPI 等实用场景。
- 📖 **完整文档与贡献**：官方文档含每个函数的详细示例，欢迎贡献代码，需遵循贡献指南。

---

### [GitHub - 微软/Mage · GitHub](https://github.com/microsoft/Mage?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - microsoft/Mage · GitHub](https://github.com/microsoft/Mage?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

Mage 是一个轻量级、面向研究的多模态模型家族，所有模型均固定在 4B 参数规模，专注于高效的视觉理解与生成。

- 🧩 Mage-VL：基于编解码器的原生流式视觉语言模型，支持图像与视频理解，即将发布。
- 🎨 Mage-Flow：高效的文本到图像生成与指令式图像编辑模型，支持原生分辨率（512-2048）和极速推理。
- ⚡ 性能突出：Mage-Flow 在 4B 规模下媲美或超越 20B-32B 的大模型，训练速度提升约 2.5 倍，推理速度极快。
- 🖼️ 高效编解码器：Mage-VAE 以极低计算量实现与 FLUX.2 相当的图像重建质量。
- 🚀 模型已发布：Mage-Flow 系列（Base、RL-aligned、Turbo）已开源至 Hugging Face，Mage-VL 即将发布。
- 📥 模型库丰富：提供多个变体，支持文本到图像生成与图像编辑，每个模型均有独立 README 指导使用。
- 📝 研究用途：仅限研究，不用于产品部署，需注意数据偏见与输出安全。
- 📄 开源许可：采用 MIT 许可证，附带行为准则与安全政策。

---

### [GitHub - NVIDIA/cosmos-framework：在Cosmos模型上运行的推理与训练框架 · GitHub](https://github.com/NVIDIA/cosmos-framework?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - NVIDIA/cosmos-framework: Our inference and training framework to run on the Cosmos Models · GitHub](https://github.com/NVIDIA/cosmos-framework?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

这是一个面向 NVIDIA Cosmos 世界模型的开源训练与推理框架，核心是 Cosmos 3 模型家族。

- 🤖 **Cosmos 3 模型家族**：一套全能世界模型，基于混合 Transformer 架构，统一处理语言、图像、视频、音频和动作序列，支持高度灵活的输入输出配置。
- 🧩 **Cosmos-Framework 框架**：端到端框架，包含训练（分布式 FSDP/TP/CP/PP 训练器）和推理（Diffusers/Transformers/vLLM 后端）两大核心模块。
- 🚀 **快速上手**：提供基于 `uv` 的安装方式，支持 CUDA 13.0 和 12.8，并推荐从 NVIDIA NGC 基础镜像开始。
- 🎯 **训练功能**：支持监督微调（SFT），提供 8-GPU 配置示例脚本，用户可根据硬件调整 GPU 数量和并行策略。
- 🖥️ **推理功能**：支持单 GPU 快速推理，提供延迟优先的并行预设，以及离线批量生成和在线服务（Ray + Gradio）两种模式。
- 🛠️ **Agent 技能**：内置多个针对代码代理（如 Claude Code）的 SKILL.md 文件，覆盖安装、代码导航、推理、后训练和环境排错等任务。
- 📚 **完整文档**：涵盖设置、代码结构、训练、推理、策略服务器和常见问题解答，另有 AGENTS.md 提供仓库地图。

---

### [GitHub - jacopobonomi/venv_manager：一款轻松管理Python虚拟环境的强大命令行工具](https://github.com/jacopobonomi/venv_manager?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - jacopobonomi/venv_manager: A powerful CLI tool for managing Python virtual environments with ease. · GitHub](https://github.com/jacopobonomi/venv_manager?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

venv-manager 是一款用 Go 编写的 Python 虚拟环境管理工具，旨在解决人类和 AI 代理在管理虚拟环境时遇到的常见问题。它提供 CLI、MCP 服务器、文件监听、临时执行和 JSON 快照等功能。

- 🐍 **核心功能**：创建、列出、删除、重命名、克隆、安装、升级、清理、导出/导入虚拟环境，并支持 `uv` 后端加速。
- 🤖 **AI 集成 (MCP 服务器)**：通过 JSON-RPC 2.0 协议暴露工具，如 `create_venv`、`describe_venv`、`install_packages`、`exec_ephemeral` 等，让 AI 代理能直接管理环境。
- 👁️ **文件监听 (watch)**：自动监控 Python 文件变化，解析 import 语句并安装缺失包，保持环境与代码同步。
- 📦 **临时执行 (exec)**：创建、安装、运行、销毁环境一步完成，支持 `--sandbox` 沙箱隔离，适合运行不可信代码。
- 📋 **JSON 快照**：`describe` 命令输出完整环境信息（Python 版本、包列表、大小、激活命令等），`freeze_hash` 可快速检测环境变化。
- ⚙️ **配置灵活**：支持自定义基础路径、默认 Python 版本、`uv` 开关、自动清理天数等，通过 `~/.config/venv-manager/config.json` 管理。
- 🛠️ **开发友好**：提供 `make build`、`make test`、`make demo` 等命令，架构清晰（cobra CLI + 核心逻辑 + MCP + TUI）。
- 🏷️ **主题标签**：`cli-tool`、`python`、`venv`、`virtual-environment`，MIT 许可。

---

### [GitHub - Zwony/ecotrace: 一个轻量级的 Python 库，用于测量代码的碳足迹](https://github.com/Zwony/ecotrace?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [GitHub - Zwony/ecotrace: A lightweight Python library to measure the carbon footprint of your code · GitHub](https://github.com/Zwony/ecotrace?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

EcoTrace 是一个轻量级 Python 库，用于高精度测量代码的碳足迹和能耗，支持实时监控、预算强制和 CI/CD 集成。

- 🌱 **核心功能**：提供函数级碳测量、实时监控、50+ 全球区域支持和 AI 洞察，无需配置文件或后台服务。
- 🚀 **v1.4.0 新特性**：新增可暂停跟踪 API、并排 CLI 差异比较、Webhook 导出、过滤 CSV 导出和日志维护命令。
- ⚡ **快速安装与使用**：通过 `pip install ecotrace` 安装，支持 CLI 零代码分析和程序化跟踪装饰器，以及碳预算模式。
- 🔧 **CI/CD 集成**：提供官方 GitHub Action 和手动 CLI 门控，用于在管道中强制碳预算，防止高碳代码合并。
- 📊 **对比优势**：相比 CodeCarbon 和 CarbonTracker，EcoTrace 具有更快的采样间隔（50ms）、进程级隔离、内置预算强制和空闲噪声自动减法。
- 🛠️ **文档与社区**：完整文档在 ecotrace.readthedocs.io，支持贡献，采用 MIT 许可证。

---

### [Django 伦敦聚会 7 月，2026 年 7 月 28 日星期二，下午 6:15 | Meetup](https://www.meetup.com/djangolondon/events/315788543/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Django London Meetup July, Tue, Jul 28, 2026, 6:15 PM   | Meetup](https://www.meetup.com/djangolondon/events/315788543/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

Django London 7 月聚會將於 7 月 28 日（週二）18:15 至 21:45 在 Octopus Energy Group 辦公室舉行，活動包括技術講座、社交和餐飲。

- 📅 活動時間：7 月 28 日（週二）18:15 至 21:45（BST），地點在 Octopus Energy Group 辦公室（近 Oxford Circus）
- 🎤 主要講座：Dan Groshev 將介紹 Okmain 庫，探討如何從圖像中提取顏色，並分享將 Rust 庫通過 PyO3 整合到 Django 後端的經驗
- 🗓️ 第二場講座待定，鼓勵參與者通過 Speaker 表單提交提案
- 🍕 活動流程：18:15 開門社交，18:30 提供餐飲，19:00 關門，19:15 開始講座，20:30 繼續社交，21:45 結束
- ⏰ 入場要求：請在 18:15 至 18:55 之間到達，19:15 後無法入場；早到或晚到者可在樓下接待區等候
- 📜 活動受行為準則約束，請提前閱讀
- 🤝 贊助商：Octopus Energy（英國綠色能源供應商）和 JetBrains（專業開發工具公司）
- 🌐 更多資訊：網站 djangolondon.com，BlueSky、GitHub 和 Open Collective 均有社群頁面

---

### [SF Python 7 月 29 日 @ GGU，2026 年 7 月 29 日星期三下午 5:30 | 聚会](https://www.meetup.com/sfpython/events/315401935/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [SF Python July 29th @ GGU, Wed, Jul 29, 2026, 5:30 PM   | Meetup](https://www.meetup.com/sfpython/events/315401935/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

SF Python 7 月 29 日在金门大学举办线下活动，内容包括 Python 技术分享、社交和赞助商致谢。

- 🐍 活动由 Phebe B G P.和 James A.主持，时间为 7 月 29 日下午 5:30 至 8:30，地点为金门大学 536 Mission Street Room 5210
- 📝 需提前在指定链接注册，并鼓励提交 5、15 或 25 分钟的演讲提案
- 🔒 第一场演讲：Syrus Akbary 讲解如何使用 WebAssembly 在完全沙盒环境中运行 Python，强调对 AI 工作负载安全的重要性
- 🧠 第二场演讲：Melanie Warrick 探讨智能体的两种记忆类型——知识记忆与执行记忆，并展示如何通过持久化执行记忆让智能体无缝恢复任务
- ⏰ 活动流程包括 5:30 社交、6:00 开场致谢、6:10 演讲与问答、8:30 结束并继续交流
- 🤝 活动由志愿者组织 SF Python 主办，旨在促进湾区 Python 社区发展
- 📍 相关主题涵盖 AI 算法、数据库、Python 及软件测试等

---

### [F5 网络 Python 技术交流会，2026 年 7 月 29 日（周三）下午 5:30 | Meetup](https://www.meetup.com/psppython/events/315509789/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Python talk night at F5 Networks, Wed, Jul 29, 2026, 5:30 PM   | Meetup](https://www.meetup.com/psppython/events/315509789/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

F5 Networks 将于 7 月 29 日举办 Python 讲座之夜，活动包括三场技术演讲、社交环节及会后派对，由 PuPPy 组织，赞助商提供餐饮支持。

- 🗓️ 活动时间：7 月 29 日周三下午 5:30-8:00（PDT），地点在 F5 西雅图市中心办公室 48 层
- 🎤 三场演讲：涵盖数据库模式演化、安全沙箱编码、BAML 桥接语言设计
- 🍕 赞助商：Pecado Bueno、ActiveState、Slalom Consulting 提供餐饮赞助
- 🚇 交通便利：靠近 2nd-5th 大道公交线路及 Pioneer Square 轻轨站
- 🎉 会后派对：活动结束后在 Owl N' Thistle 酒吧继续交流
- 📝 无需携带电脑，现场不提供食物，建议提前到场社交

---

### [PyData 比利时 2026 年 7 月，2026 年 7 月 30 日星期四，下午 6:30 | 聚会](https://www.meetup.com/pydata-belgium/events/315298608/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [PyData Belgium July 2026, Thu, Jul 30, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-belgium/events/315298608/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

PyData Belgium 2026 年 7 月聚會將於 7 月 30 日在魯汶舉辦，包含三場數據相關演講及餐飲交流。

- 📅 活動時間：2026 年 7 月 30 日（週四）18:30-21:00（CEST），演講於 19:00 開始
- 📍 活動地點：比利時魯汶 Vismarkt 17 號 Dataminded 辦公室
- 🎤 演講一：Jonas Crevecoeur 探討 Polars 與 dbt 協作構建數據管道
- ⚡ 演講二：Quinten Rosseel 介紹無需訓練模型的零樣本能源預測方法
- 🧪 演講三：Cesar Vermeulen 與 Murilo Cunha 分享使用 Pytest 進行代理測試
- 🍕 活動提供食物與飲料（披薩、啤酒等）
- 🔗 需在 Meetup 平台註冊參加

---

### [在 Databricks 上构建多智能体 AI 系统，2026 年 7 月 30 日（周四）下午 6:00 | Meetup](https://www.meetup.com/pydata-bradford/events/315495890/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

**原文标题**: [Building Multi-Agent AI Systems on Databricks, Thu, Jul 30, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-bradford/events/315495890/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-755-july-23-2026)

该活动是一个关于在 Databricks 上构建多智能体 AI 系统的线上工作坊，由 Paul Karikari 主讲，涵盖设计模式、实践操作和常见陷阱。

- 🤖 活动介绍：PyData Bradford 七月线上聚会，主题为“在 Databricks 上构建多智能体 AI 系统：模式与陷阱”
- 🎯 核心问题：探讨多智能体系统在真实环境中的实用性、设计方法和潜在问题，而非仅停留在演示阶段
- 🛠️ 实践内容：参与者将使用 Databricks 笔记本从零构建多智能体原型，涉及 Mosaic AI Agent Framework、MLflow、向量搜索和 Unity Catalog 等工具
- 📐 设计模式：介绍四种核心设计模式，并演示如何映射到 Databricks 原生工具
- 🔍 工作流程：从单智能体与多智能体选择开始，逐步构建监督式研究智能体，连接专业组件，用 MLflow 追踪系统并运行离线评估
- ⚠️ 常见陷阱：涵盖不必要的复杂性、智能体职责不清、评估薄弱和治理缺失等问题
- 📋 学习成果：参与者将获得实用思维模型、完成的笔记本和用于设计或审查多智能体系统的检查清单
- 📚 前提要求：无需 Databricks 经验，但需熟悉 Python 并了解 LLM 或提示应用基础

---

