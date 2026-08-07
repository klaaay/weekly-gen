### [I notice there's no title provided to translate. Could you please share the title you'd like me to translate to Chinese?](https://menno.io/presentations/not-python-2026/index.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026#/)

**原文标题**: [None](https://menno.io/presentations/not-python-2026/index.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026#/)

我没有收到需要总结的内容。请提供文章或文本，我会按照模板给出“概述摘要”和带表情符号的要点列表。

---

### [](https://data4sci.com/blog/building-an-advanced-agentic-harness?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Building an Advanced Agentic Harness | Data For Science](https://data4sci.com/blog/building-an-advanced-agentic-harness?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

overview summary  
本文从基础代理循环出发，阐述了如何通过组合小型可测试原语，构建一个生产级的高级代理系统，涵盖规划、并行执行、分层记忆、验证、预算控制与可观测性，并以城市比较代理为例演示了完整实现。  

- 🧠 可插拔大脑：定义统一的 `LLMProvider` 抽象接口，支持同步/异步调用与 `MockProvider`，使系统可测试、可复现、避免厂商锁定。  
- 🛠️ 类型化工具：用 Pydantic 模型声明工具参数，自动生成 JSON Schema，提供运行时校验、文档与成本提示，实现快速失败。  
- 📐 计划即图：将执行计划表示为有向无环图（DAG），先验证结构再执行，避免无效依赖或循环依赖浪费 token。  
- ⚡ 并行执行器：采用层级同步 DAG 调度器，用 `asyncio.gather` 并发运行就绪节点，并通过信号量限制并发上限，显著缩短总耗时。  
- 🧠 分层记忆：区分工作记忆、情景记忆与语义记忆，基于相似度检索 top-k 并强制备字符预算，优先注入情景记忆，显式截断而非静默丢弃。  
- ✔️ 验证层级：先运行几乎零成本的确定性结构检查（如是否包含所有必需城市），通过后才升级到 LLM 评判，避免在低质量输出上浪费 token。  
- 👥 角色分离：将系统拆分为 Planner（规划 DAG）、Worker（执行 DAG）、Critic（评估结果），各自独立可测、可替换，避免单一 prompt 混淆目标。  
- ⛽ 多维预算与故障分类：同时追踪 token、工具调用、墙钟时间与美元成本，计算压力值以驱动优雅降级；错误分为瞬时、工具误用、信息缺失、致命四类，采取不同恢复策略。  
- 📼 飞行记录器：Tracer 捕获结构化的可追加事件日志，包含身份、语义、经济指标与预算压力快照，支持事后分析、成本归因与可视化调试。  
- 🔄 编排器与重规划：编排器依次构建上下文、规划、执行、验证、存储记忆，并在信息缺失时基于错误信息重新规划而非盲目重试，同时根据压力跳过昂贵评判。  
- 🔧 经验教训：不要依赖 LLM 给出的节点 ID，应通过工具名解析关键节点；所有组件可独立使用，但组合后形成强大且可扩展的代理系统。  
- ⚠️ 遗留边界：内存目前仅在进程内，生产需持久化向量库；工具输出需按数据沙箱化防注入；不可逆操作需人工审批；token 计数需读取 SDK 真实元数据。  
- 🧪 未竟事项：本文未证明系统“通常有效”，需要专门的评估套件、检索基准与专业化 worker 池来验证整体可靠性，留待后续文章。

---

### [Gleam：面向 Python 程序员](https://third-bit.com/gl4py/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Gleam for Python Programmers](https://third-bit.com/gl4py/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

本課程是一份完整的 Gleam 程式語言教學大綱，涵蓋從基礎語法、函數式概念到進階實作與分散式系統的主題，適合 Python 程式設計師轉換跑道，強調動手實作與逐步建構真實應用。

- 📘 課程以 Python 程式設計師為對象，從型別、值與函數等基礎概念開始循序漸進。
- 🔧 涵蓋函數、模式匹配、列表與管線（Pipeline）等函數式程式設計核心技巧。
- 🛡️ 深入結果型別（Result）、選項型別（Option）與錯誤處理，以及 `use` 表達式的應用。
- 📦 講解模組、匯入與測試，並透過 MapReduce、Glob 模式比對器等實例練習。
- 💾 進階實作包含檔案去重、二進位資料打包、日誌結構化鍵值儲存與事件最終一致性的鍵值儲存。
- ⚙️ 涵蓋虛擬機器、待辦事項 Web API、HTTP API 用戶端與 JSON 解碼等實務開發。
- 🤖 進階主題包括受監督的 Worker Pool、資料框架（Dataframes）、狀態機與屬性化測試。
- 🎯 課程結尾強調「從你所在之處開始，運用你擁有的資源，幫助你能幫助的人」的實作精神。

---

### [](https://adamj.eu/tech/2026/08/03/python-time-machine-o1-freezegun-on/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Python: how time-machine is O(1) where freezegun is O(n) - Adam Johnson](https://adamj.eu/tech/2026/08/03/python-time-machine-o1-freezegun-on/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

time-machine 與 freezegun 都是 Python 測試中模擬時間的函式庫，本文透過基準測試與原始碼分析，說明 time-machine 為什麼是 O(1) 而 freezegun 是 O(n)，並介紹如何用遷移工具從 freezegun 切換到 time-machine。

- ⚡ 基準測試顯示：freezegun 的耗時隨模組數量線性成長，time-machine 則維持恆定；在 16,000 個產生模組下，freezegun 每次花 41 ms，time-machine 只要 1.5 µs。
- 📊 兩者速度比不是固定倍數，而是隨專案規模增加：259 個模組時快 940 倍，1,259 個模組時快 2,490 倍，16,259 個模組時快 27,300 倍。
- 🐢 freezegun 是 O(n) 的原因：每次 freeze_time 都會遍歷 sys.modules，逐一檢查每個模組屬性並替換原始日期/時間函數；即使有快取，仍需計算模組屬性的雜湊。
- 🕳️ freezegun 也有漏網之魚：無法覆蓋類屬性、預設引數、閉包和 C 擴充中的引用；而且它的假物件型別與真實物件不同，可能破壞依賴型別判斷的程式碼。
- 🔧 time-machine 是 O(1) 的原因：直接在 CPython 的 C 層改寫內建函數的函數指標，只要針對十個讀取時鐘的函數各寫入一次，不需掃描任何模組。
- ✅ time-machine 的作法讓所有引用自動套用新行為，且日期/時間函數的型別保持不變，解決了 freezegun 的洩漏問題。
- 🚀 time-machine 提供遷移 CLI，可用 `uvx --from 'time-machine[cli]'` 自動將 `freeze_time` 改寫為 `time_machine.travel`，並加上 `tick=False` 以維持原本凍結時間的行為。
- 🧹 遷移工具只做部分替換，可能留下未使用的 freezegun import 或無法改寫的程式碼；建議在乾淨 commit 上執行，並用 Ruff 的 F401/F821 規則清理殘留。

---

### [使用 NLP 进行分类](https://softwaremaniacs.org/blog/2026/07/30/categorization-with-nlp/en/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Categorization with NLP](https://softwaremaniacs.org/blog/2026/07/30/categorization-with-nlp/en/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

overview summary  
- 🛒 作者分享其购物分类工具 Shoppy 的算法设计，采用手工规则而非机器学习，以解决数据不足和预算限制。  
- 🔤 输入处理流程：小写化、NFD 标准化、分词、词干提取、排序，生成稳定的关键词组合。  
- 🗂️ 数据库结构：以单字词（unigram）为核心，通过优先级排序（派生词优先于原料词）解决“苹果汁”等歧义。  
- 🍝 引入双字词（bigram）处理组合概念，如“spaghetti squash”归为农产品而非意面，所有大词先于单字词匹配。  
- ⚡ 针对“pepper”等特例，采用硬编码规则（如将“pepper”替换为“black pepper”），实用性优先于模型纯净性。  
- 📖 处理复合词拼写（如“redbull”“lipbalm”），先按单词查找，失败后再用音节切分（SyllableTokenizer）二次查找。  
- ✏️ 拼写检查基于自定义数据库，使用 Damerau-Levenshtein 距离，并设定经验阈值，既适配国际食品名又规避常见英文拼写库的局限。  
- 🚀 优化手段：假设首字母无误、跳过长度差异过大的词、区分 n-gram 类型、精确匹配提前终止，且数据量小使得性能可接受。  
- 🎯 突出案例：“may o”可匹配 mayo、mayonnaise、mayones 甚至 mayochup；“separilla”通过音节切分和拼写检查识别为 sarsaparilla。  
- 📁 数据与代码开源在 Shoppy 仓库中，包含核心函数、术语库和类别层级，作者期待 NLP 专家提供更深入的反馈。

---

### [](https://nesbitt.io/2026/07/30/wheels-bottles-images.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Wheels, Bottles and Images | Andrew Nesbitt](https://nesbitt.io/2026/07/30/wheels-bottles-images.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

本文比较了 Python wheels、Homebrew bottles 和 OCI 镜像这三大二进制分发系统的异同，指出它们本质上都是通过校验和归档、客户端按平台选择的分发方式，并探讨了它们在依赖处理、平台标签、构建回退上的差异，以及 Homebrew 和 Helm 向 OCI registry 迁移的融合趋势，最后展望了未来二进制分发在 GPU 等新维度上的扩展方向。

- 📦 三大系统本质相同：皆为校验和的归档文件，客户端按平台选择，依赖 CDN 和缓存高效分发。
- 🔁 索引与存储分离：PyPI 指向独立文件主机，Homebrew 从 Bintray 迁至 GitHub Packages，镜像可跨 registry 复制。
- 🔒 发布后不可变：已发布文件不可更改，修复以新版本形式出现，校验和保证完整性。
- 🖥️ 平台选择在客户端完成：pip 匹配 wheel tags，brew 匹配 bottle tags，容器客户端解析 image index。
- 🏷️ 平台标签覆盖 CPU 架构、操作系统与 ABI，但各生态拼写和语法各不相同。
- 📄 每种格式均含元数据：wheel 的 .dist-info、bottle 的 INSTALL_RECEIPT.json、镜像的 config 对象。
- ⚙️ 依赖处理差异显著：wheel 和 bottle 处于依赖图中，镜像自带整个用户态，无拉取时依赖解析。
- 🔨 无匹配时回退能力不同：wheel 可构建 sdist，bottle 可源码构建，而 docker pull 无法从 Dockerfile 自动构建。
- 🔀 融合趋势明显：Homebrew 已将 bottles 存入 OCI registry，Helm 3.8 同样采用，ORAS 支持任意工件。
- 🛡️ 构建证明统一为 sigstore：但存储位置各异，分别为 PyPI 索引、registry 旁和 GitHub 的 attestation API。
- 💡 OCI 注册表可作为通用底座：提供内容寻址、不可变 blob、索引分离和缓存镜像，但需自行定义标签语法与索引条目。
- 🎯 GPU 等新维度尚未被覆盖：CUDA wheels 常受限，PEP 817/825/725 等提案正探索变体选择与外部依赖声明。

---

### [](https://lincolnloop.com/blog/setting-djangos-debug-safely/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Setting Django's DEBUG safely | Lincoln Loop](https://lincolnloop.com/blog/setting-djangos-debug-safely/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

overview summary
本文探討 Django `DEBUG=True` 在生產環境中的重大風險，包括資訊洩露、效能衰退與行為異常，並說明僅應在本地開發環境啟用，同時提供安全設定與環境變數解析的建議以避免誤用。

- 🚨 `DEBUG=True` 會向所有網路使用者暴露堆疊追蹤、環境資訊與 Django 設定，攻擊者可能利用這些細節入侵系統。
- 🛡️ 除錯頁面的敏感設定遮蔽僅靠關鍵字比對，無法有效保護密鑰或密碼，等同於將設定攤在陽光下。
- ⚠️ 開啟 DEBUG 會停用錯誤通報，例如不寄送 broken link 郵件，且預設記錄檔不會將例外寄送給 ADMINS。
- 🐢 效能明顯下降：未壓縮的靜態檔、資料庫查詢記錄、模板自動重載與記憶體快取增加，均拖慢回應速度。
- 🔀 行為差異極大：無結尾斜線的寫入請求會拋出 RuntimeError、messages 框架可能因儲存空間不足而報錯，且訊號接收器問題會直接中斷。
- 🌐 若 `ALLOWED_HOSTS` 為空，DEBUG 模式會自動限制主機為 localhost，導致正式網域無法存取。
- ✅ 唯一安全做法是僅在本地開發環境使用 `DEBUG=True`；任何可被公開網路存取的部署（含預覽、QA、staging）都應設為 `False`。
- 🔒 建議預設 `DEBUG=False`（failing closed），再依開發環境手動開啟，避免每次部署都要記得關閉。
- 🧪 使用 `django-environ` 或 `goodconf` 解析環境變數，或撰寫嚴謹的布林解析函式，防止 `DEBUG=false` 或 `DEBUG=0` 被誤判為 `True`。

---

### [](https://www.youtube.com/watch?v=lM7zWJRrRtg&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Why dict[str, Any] Slowly Destroys Your Code - YouTube](https://www.youtube.com/watch?v=lM7zWJRrRtg&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

overview summary
- 📺 提供媒體與創作者相關資訊
- ⚖️ 說明著作權與法律條款
- 📞 包含聯絡方式與廣告合作管道
- 👨‍💻 提供開發人員資源與平台運作說明
- 🔒 涵蓋隱私權、政策與安全性規範
- 🧪 介紹測試新功能機制
- ©️ 標示版權所有（2026 Google LLC）

---

### [获取失败](https://lukasniessen.medium.com/harness-engineering-deep-dive-where-the-term-came-from-and-how-to-actually-build-one-a955bcdf5cce?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Failed to retrieve](https://lukasniessen.medium.com/harness-engineering-deep-dive-where-the-term-came-from-and-how-to-actually-build-one-a955bcdf5cce?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

无法总结：获取内容失败，状态码 403。

---

### [如何在 Python 中征服并发 - YouTube](https://www.youtube.com/watch?v=chrOym38pw4&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [How to Conquer Concurrency in Python - YouTube](https://www.youtube.com/watch?v=chrOym38pw4&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

overview summary
此內容為 YouTube 頁面底部常見的連結與法律資訊清單，涵蓋平台簡介、媒體資源、著作權、聯絡方式、創作者服務、廣告、開發人員選項、條款、隱私權、政策與安全性、平台運作方式、新功能測試，以及版權聲明。

- 📄 簡介：提供 YouTube 平台基本介紹與相關資訊  
- 🎬 媒體：連結媒體資源與新聞相關內容  
- ⚖️ 著作權：說明版權規範與申訴機制  
- 📞 與我們聯絡：提供使用者聯繫管道  
- ✍️ 創作者：協助創作者的工具與資源  
- 📢 廣告：廣告主相關服務與方案  
- 💻 開發人員：API 與開發者文件  
- 📋 條款：使用條款與服務協議  
- 🔒 隱私權：隱私政策與資料保護說明  
- 🛡️ 政策與安全性：平台安全規範與政策  
- ⚙️ YouTube 運作方式：解釋平台推薦與審核機制  
- 🧪 測試新功能：說明測試中的實驗性功能  
- ©️ 2026 Google LLC：版權所有聲明

---

### [](https://sgolev.github.io/blog/2026-07-28-celery-recipes/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Celery: from first task to advanced recipes | Stanislav Golev](https://sgolev.github.io/blog/2026-07-28-celery-recipes/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

Celery 是一套成熟的 Python 分布式任务队列系统，本文从基础安装、任务定义与调用讲起，逐步覆盖队列路由、时间限制、重试、并发锁以及异步等待等实用进阶技巧，并给出可直接复用的代码片段。

- 🐍 核心概念：Celery 通过 broker（任务队列）与 backend（结果存储）实现生产者和消费者解耦，最小场景只需 broker，常用 Redis 作为两者。
- 📦 安装与启动：使用 `pip install celery[redis]` 安装，通过 Docker 启动 Redis；Worker 默认使用 `prefork` 并发池，Windows 下可改用 `solo`、`threads` 或 `gevent` 池。
- 📝 任务定义：用 `@app.task` 装饰函数即可创建任务，完整任务名包含模块前缀（如 `tasks.say_hello`），远程调用时需使用完整名称。
- 🚀 命令行调用：设置 `CELERY_BROKER_URL` 后，可用 `celery call TASK_NAME --args '[...]' --kwargs '{...}' --queue QUEUE` 发送任务；结果需配置 `CELERY_RESULT_BACKEND` 后用 `celery result TASK_ID` 获取。
- 🔄 代码内调用：同一服务内可使用 `apply_async()` 或 `delay()`；跨服务调用则用 `app.send_task('tasks.multiply', args)`；两种方式都可用 `signature` / `s()` 统一表达。
- 👥 批量任务：借助 Canvas 的 `group` 可并行启动多个任务，`group(...).apply_async().get()` 返回结果列表；通过 `propagate=False` 可单独处理异常结果。
- 🎯 队列路由：默认所有任务进入 `celery` 队列，可通过 `queue='...'` 参数指定目标队列，适用于 `apply_async`、`send_task` 和 `signature`。
- ⏱️ 三类时间限制：客户端 `timeout` 控制等待结果超时；消息层 `expires` 让过期任务被 Worker 丢弃；Worker 层 `soft_time_limit` 抛异常、`time_limit` 强制终止进程。
- 🔁 重试机制：`bind=True` 的任务内可通过 `self.retry(exc=exc)` 触发重试，默认延迟 3 分钟最多 3 次，也可用 `countdown` 调整延迟。
- 🔒 防并行执行：使用 Redis 锁实现装饰器，配合 `retry` 和时间限制，可避免同一任务并发执行；冲突任务会先 RETRY，超时后 FAILURE。
- ⏳ 异步等待技巧：Celery 不支持原生 async/await，可用 `asyncio.to_thread` 简化阻塞等待，或用轮询 `ready()` 的 `async_get` 避免线程池限制。
- ✅ 总结与延伸：文章提供了从入门到进阶的可复用代码；更复杂场景需查阅官方文档，这些示例旨在让关键主题更清晰、更贴近实际项目。

---

### [](https://github.com/nvidia-nemo/labs-OO-Agents?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - NVIDIA-NeMo/labs-OO-Agents: NVIDIA Object Oriented Agents: the Pythonic way to build AI Agents. · GitHub](https://github.com/nvidia-nemo/labs-OO-Agents?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

NVIDIA-NeMo labs OO Agents (NOOA) 是一个模型无关的 Python 框架，用于构建可靠的 AI 智能体。它采用面向对象的设计，将智能体的状态、能力、提示词和类型接口统一在单个 Python 类中，支持“代码即行动”的模式，并注重 Pythonic 的开发体验。框架提供安装、快速入门、追踪、安全沙箱等完整支持。

- 🐍 **智能体即 Python 对象**：字段表示状态，方法表示能力，docstring 即提示词，类型注解即契约，方法体用 `...` 交由 LLM 驱动。
- ⚙️ **代码即行动**：模型通过 Jupyter 风格 REPL 编写 Python 代码，利用 `self` 和类型注解直接调用方法，减少工具 schema 定义。
- 🔁 **类型化 I/O 与自动重试**：支持实时对象传引用、模型可调用的上下文与事件 API，适合智能体导向的 Python 工作流。
- 📦 **安装简便**：核心包 `nooa` 可用 uv 或 pip 安装，另提供 `nooa-cli`、`nooa-memory`、`nooa-bench` 可选子包。
- 🌐 **模型无关**：通过 LiteLLM 支持多种模型，包括 Anthropic、OpenAI、Ollama、vLLM 等，可灵活切换。
- 🚀 **快速上手**：定义继承 Agent 的类并实现生成方法即可，方法名、参数和 docstring 直接构成提示词。
- 🔍 **默认追踪**：每次 LLM 调用、代码执行和方法调用都被记录，使用 `nooa start-dev` 可在浏览器中查看追踪结果。
- ⚠️ **安全警告**：LLM 生成的代码可能危险，必须在沙箱（如容器、VM 或 NVIDIA OpenShell）中运行，进程内校验仅作为防御纵深。
- 📚 **丰富资源**：提供完整渐进式教程、论文、博客、贡献指南和 Apache 2.0 许可，支持社区参与。

---

### [](https://github.com/uber/ADR?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - uber/ADR: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber. · GitHub](https://github.com/uber/ADR?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

ADR 是 Uber 开发的企业级 AI 代理安全系统，已在生产环境部署，论文被 MLSys 2026 接收。它通过可观测性、基准测试、检测和预防四方面能力保护 AI 代理，开源内容包括 Sensor 和 Detection 组件。

- 🔍 ADR Observability：捕获代理意图、工具使用和执行轨迹，支持 7+ AI 编码工具及内部/客户代理。
- 🛡️ ADR-Bench：包含 300+ 任务、133 个 MCP 服务器，覆盖 17 种代理攻击技术。
- ⚡ ADR Detection：采用双代理检测器，两阶段架构实现高效风险识别。
- 🚫 ADR Prevention：阻止不安全操作，但未包含在开源版本中。
- 📂 仓库布局：Sensor/ 负责遥测收集，Detection/ 含基准与检测器，Explorer 未开源。
- 🚀 快速开始：克隆仓库、使用 uv sync 安装、设置 API 密钥即可运行检测。
- 📄 引用与许可证：提供论文、CITATION.cff，采用 Apache-2.0 许可证。
- ⚠️ 数据说明：包含合成基准数据，仅供防御性安全研究使用。

---

### [](https://github.com/huggingface/speech-to-speech?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - huggingface/speech-to-speech: Build local voice agents with open-source models · GitHub](https://github.com/huggingface/speech-to-speech?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

這是一個由 Hugging Face 開發的開源語音代理管線，採用 VAD→STT→LLM→TTS 的級聯架構，提供低延遲、全模組化設計，並透過 OpenAI Realtime 相容的 WebSocket API 暴露服務。其組件可任意替換，既可使用雲端 LLM，也可搭配 llama.cpp/vLLM 等完全本地執行，目前已用於數千台 Reachy Mini 機器人的生產環境。

- 🔧 核心管線為「VAD→STT→LLM→TTS」，每個階段皆可抽換，透過佇列串接，低延遲且全模組化。
- 🌐 提供 OpenAI Realtime 相容的 WebSocket/WebRTC API，任何相容客戶端都能直接連線。
- 🤖 已在生產環境中支撐數千台 Reachy Mini 機器人的對話後端。
- ⚡ 快速開始：`pip install speech-to-speech` 後設定 API key，執行 `serve` 啟動伺服器，再用 `talk` 進行對話。
- 🏠 支援完全本地開源堆疊，例如用 llama.cpp 載入 Gemma 4，並將 LLM 指向本地端點。
- 🧩 STT 可選 Parakeet、Whisper、Faster Whisper、Paraformer 等；TTS 可選 Qwen3、Kokoro、Pocket TTS、ChatTTS 等。
- 📦 安裝時可透過 pip extras 加入選用後端；Linux 上 Qwen3-TTS 的 GGML 版本需搭配對應 CUDA wheel。
- 🔄 提供三種命令：`serve`（伺服器）、`talk`（麥克風/喇叭客戶端）、`local`（同機執行伺服器與客戶端）。
- 🔁 內建 LLM Proxy，可將遠端 LLM 作為純 OpenAI 相容端點供並行任務使用；但無認證，僅建議在可信網路啟用。
- 🗣️ 多語言支援取決於 STT/TTS 後端，可使用 `--language auto` 自動偵測並切換語言。
- 🎙️ 支援「直接音訊輸入」（`--stt none`），跳過 STT 直接將語音片段送給支援音訊的模型。
- ⏱️ Smart Turn endpointing 會驗證語音結束並提早開始處理，降低延遲；預設啟用，可調門檻。
- 📚 提供詳細的 CLI 參考、組件參數說明及引文資訊，並歡迎透過 Issues/PR 貢獻。

---

### [](https://github.com/slvDev/esp32-ai?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - slvDev/esp32-ai · GitHub](https://github.com/slvDev/esp32-ai?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

该仓库展示了一个在 ESP32-S3 微控制器上运行 28.9M 参数语言模型的项目，完全离线推理，速度约 9.88 token/s，通过将大部分参数存储在Flash中来突破内存限制，并基于Google Gemma 3n 的 Per-Layer Embeddings 设计实现。

- 🤖 项目核心：在 ESP32-S3 芯片上运行 28.9M 参数的语言模型，完全本地生成文本，不依赖服务器，实测速度 9.88 token/s。
- 📊 关键数字：28.9M 参数中 25M 存储在 Flash 查找表，模型 4-bit 量化后仅 14.9MB，芯片配备 512KB SRAM、8MB PSRAM 和 16MB Flash。
- 🧠 内存分层：SRAM 存激活值和归一化权重；PSRAM 存每次位置扫描的核心和输出头；Flash 存 25M 参数嵌入表，每个 token 仅读取约 6 行（约 450 字节）。
- ✨ 创新点：采用 Google Gemma 3n 的 Per-Layer Embeddings 思想，让大模型嵌入表驻留 Flash，按需少量读取，而非全量加载到 RAM。
- 📚 训练数据：模型基于 TinyStories 数据集训练，擅长生成简短连贯的儿童故事，不具备问答、指令跟随、写代码或知识查询能力。
- 🎯 项目定位：重点在“把大模型装进小芯片”的架构可行性，而非追求 28.9M 参数模型的输出能力；提供 Barista（咖啡问答）和 TinyStories（故事生成）两个模型。
- 🛠️ 使用方式：`fetch_model.sh`负责带校验的下载安装，`deploy.sh`离线生成头文件、编译并烧录；两者都需指定模型名称，板子一次只放一个模型。
- 🔐 安全下载：脚本会校验 SHA-256 和字节大小，并与发布元数据交叉核对，任何一步失败都不会改动已有文件。
- 📁 项目结构：固件说明在`firmware/esp32_tinystories/README.md`，可复用架构在`src/`，训练与量化复现代码在`research/tinystories/`，完整方法见`RESULTS.md`。
- 🙏 致谢：数据来自 Microsoft Research 的 TinyStories，架构借鉴 Google Gemma 3n，训练参考 Andrej Karpathy 的 llama2.c。

---

### [](https://github.com/prime-radiant-inc/smevals?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - prime-radiant-inc/smevals: A framework for running evals against small (and large) models · GitHub](https://github.com/prime-radiant-inc/smevals?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

smevals 是一个用于对小模型（也包括大模型）运行评估的框架，它通过标准化的目录结构、可执行脚本和命令行工具，帮助用户定义任务、配置模型、运行实验，并用可复现的方式自动评分和生成报告。

- 🚀 安装：可用 `uv tool install smevals`、`pip install smevals` 或直接 `uvx smevals --help` 使用。
- 📂 核心概念：Eval 是一组评估任务的集合，Task 是单个任务，Config 描述模型和设置，Run 是执行记录，Grader 和 Checker 负责评分。
- 🛠️ 构建 Eval：任何包含 `eval.yaml` 的目录就是一个 Eval，内部有 `tasks/`、`configs/`、`graders/`、`checkers/` 等子目录和可执行文件。
- 📝 示例：以“写俳句并评分格式”为例，展示了 eval.yaml、任务 YAML、默认配置、Runner 脚本和自定义 Checker 的写法。
- 🏃 Runner 合同：Runner 通过环境变量（如 `SMEVALS_MODEL`、`SMEVALS_PROMPT`、`SMEVALS_RUN_DIR`）获取输入，标准输出作为模型回复，退出码非零表示基础设施失败。
- ✅ Grader 配置：Grader 是 YAML 文件，按顺序执行一系列 Checks，支持 `required` 检查、`creates` 文件验证和自定义或内置 Checker。
- 🔌 内置 Checker：目前有 `contains`（检查输出包含指定文本）和 `xml-valid`（检查文件是否为合法 XML），也可写任意可执行程序。
- 📈 评分规则：Grade 的分数取最后一个有分数的 Check；若某 Check 失败且未输出分数，则整体分数为空；outcome 为 fail 或 pass。
- 💾 磁盘持久化：Run 目录包含 `run.yaml`、`output.txt`、`stderr.txt` 及工件，Grades 存放在 `grades/<grader>/` 下，并带有 Grader 快照以便复现。
- 🔁 多模型与多次运行：`smevals run -m model1 -m model2 -n 5` 可对每个任务/模型组合补齐到至少 5 次成功运行，失败运行不计入目标。
- 🖥️ 常用命令：`smevals run` 执行评估并可选即时评分，`smevals grade` 评分，`smevals report` 输出 Markdown 报告，`smevals serve` 提供实时 Web UI，`smevals build` 生成静态站点。
- 📊 报告功能：报告包含 config × model 排行榜、平均分±标准误、失败计数、标签占比和按模型的指标，`--by-task` 可查看每个任务得分。

---

### [](https://github.com/Emily2040/seedance-2.0?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - Emily2040/seedance-2.0: Comprehensive production pipeline for quad-modal AI filmmaking with Seedance 2.0 · GitHub](https://github.com/Emily2040/seedance-2.0?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

该仓库是“Seedance 2.0 Skill OS”——一个面向字节跳动 Seedance 2.0 视频生成模型的模块化智能体技能包。它主张“执导场景而非装饰场景”，通过导演式思维让镜头、灯光、调度、表演与声音共同服务叙事意图，并配套多语言支持、专业影视工作流、序列续写、安装与验证体系。

- 🎬 核心理念：先“读场景”再写提示词，让所有画面元素服务同一意图，拒绝空洞的“电影感”堆砌。
- 🧠 导演引擎：强制“导演解读”流程，分析功能、转折、权力变化、矛盾等，并对非叙事内容单独设道，避免虚构戏剧。
- 🛠️ 多模态工作流：覆盖文生视频、图生视频、视频生视频、参考生视频、首尾帧等模式，并按角色分离参考资产。
- 🌐 多语言支持：提供中、日、韩、西、俄等语言的电影词汇、示例与快速入门，参考标签保持原样传递。
- 🎞️ 序列续写：基于已接受生成片段的真实结束状态续写，以项目状态为事实来源，而非盲目扩展原提示词。
- 🎥 专业制作：为导演、摄影、剪辑、调色、声音、本地化、交付/QC 等角色输出对应的生产工件。
- 🔒 安全合规：将不安全的名人、IP、品牌等请求改写为安全创意等价物，仅澄清良性生产语境，绝不隐藏意图。
- 📦 安装便捷：支持 Git 克隆或 ZIP 下载，脚本可安装至 Codex、Claude Code、Antigravity 等多种客户端。
- ✅ 质量验证：离线 CI 检查、模式与提示词压力测试、来源新鲜度审查，以及模型在环的盲评评估。
- 🎨 设计标准：采用编辑式设计系统，避开 AI 默认风格与相机元素，SVG 由生成脚本保证一致性。
- 📄 开源说明：MIT 许可证，当前 v6.7.0，仓库约 6.2k 星标、925 fork。

---

### [](https://github.com/abus-aikorea/voice-pro?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - abus-aikorea/voice-pro: Gradio WebUI for creators and developers, featuring key TTS (Edge-TTS, kokoro) and zero-shot Voice Cloning (E2 & F5-TTS, CosyVoice), with Whisper audio processing, YouTube download, Demucs vocal isolation, and multilingual translation. · GitHub](https://github.com/abus-aikorea/voice-pro?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

overview summary  
Voice-Pro 是一个开源的 AI 语音工具包，整合了语音识别、翻译、配音、声音克隆及 YouTube 下载等功能，旨在为创作者和开发者提供一站式多媒体处理解决方案，目前完全免费。

- 🎙️ 顶尖语音识别：支持 Whisper、Faster-Whisper、Whisper-Timestamped，可处理 100+ 语言。  
- 🗣️ 多元语音合成：集成 Edge-TTS、kokoro、F5-TTS、E2-TTS、CosyVoice，并支持零样本声音克隆。  
- 🎥 YouTube 处理：内建 yt-dlp，可下载视频并提取音频，配合 Demucs 进行人声分离。  
- 🌍 实时翻译：支持 100+ 语言翻译，默认使用免费 Google 端点，也可切换 Azure Translator。  
- 🚀 最新 v4.0：改用 uv 安装器，Python 3.12、Torch 2.8.0、Gradio 6，无需 CUDA 工具包，安装更快。  
- 🆓 完全开源免费：因团队转向 WeConnect 开发，全部代码已开放，可自由分发和修改。  
- 💻 系统要求：Windows 10/11（NVIDIA GPU 最佳）、Linux、Mac；VRAM 4GB+，存储 20GB+。  
- 📦 简易安装：通过 configure.bat 和 start.bat（Mac/Linux 用 .sh）即可完成，首次运行自动下载依赖和模型。  
- 🔑 可选 Azure 服务：可在 .env 文件中配置密钥，获得更稳定的翻译和更高质量的 TTS 语音。  
- 🛠️ 实用技巧：浏览器未自动开启时手动访问地址；CUDA 内存不足时降低 Denoise 等级或使用 int 计算类型。  
- 📊 竞品对比：提供多个 SaaS 平台（Maestra、Kapwing、VEED.IO 等）处理 60 分钟视频的成本与功能参考。  
- 🤝 社区贡献：欢迎提交 Issue 和 Pull Request，也支持 Star、捐赠或邮件联系。

---

### [](https://github.com/blader/humanizer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - blader/humanizer: Agent skill that removes signs of AI-generated writing from text · GitHub](https://github.com/blader/humanizer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

overview summary

Humanizer 是一个开源的便携式代理技能，旨在通过重写文本，去除 AI 生成的典型痕迹，使文字更自然、更接近人类写作。该技能基于 Wikipedia 的「AI 写作迹象」指南，能检测并纠正多达 33 种常见模式，同时遵循不虚构事实的原则。它支持多种安装方式，可用于不同代理平台，并提供语音校准功能来匹配用户个人风格。

- 📌 **简介**：Humanizer 是一种纯 Markdown 的代理技能，可消除文本中的 AI 生成痕迹，使内容听起来更自然、更人性化。
- 🔧 **安装方式**：支持通过 Skills CLI 全局或项目级安装，也可作为 Claude Code 插件安装，或手动复制 SKILL.md 文件到技能目录。
- 💻 **使用方式**：可通过斜杠命令（如 `/humanizer`）或直接请求调用，支持处理粘贴文本、重写文件，并可提供个人写作样本进行语音校准。
- 📚 **理论基础**：基于 Wikipedia 的 "Signs of AI writing" 指南，由 WikiProject AI Cleanup 维护，总结了数千例 AI 生成文本的特征。
- 🧠 **核心洞察**：LLM 使用统计算法预测下一个词，输出往往偏向于最普遍、最无特色的统计结果。
- 🔍 **检测模式**：共识别 33 种模式，涵盖内容（如意义夸大、宣传语）、语言（如 AI 词汇、被动语态）、风格（如破折号滥用、表情符号）、沟通（如聊天机器人痕迹）和填充词/模糊语等类别，均配有前后示例。
- 🚫 **不虚构规则**：重写时绝不添加原文中不存在的事实、姓名、日期或引用，所有具体细节必须来自原文本或用户提供。
- 🔄 **审计与重写**：包含一次最终的 "明显 AI 生成" 审计和第二次重写，以捕捉初稿中残留的 AI 痕迹。
- 📝 **完整示例**：提供了里斯本旅行文章的改写前后对比，展示了如何消除 AI 特征的同时保留主题、视角和长度。
- 📄 **版本历史**：从 1.0.0 到 2.9.1 持续更新，新增模式（如 #30 diff-anchored writing、#31-33 风格模式）、改进安装方式、加入语音校准和不虚构规则等。
- 📜 **许可协议**：使用 MIT 许可证。

---

### [](https://github.com/anandprtp/Antra?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - anandprtp/Antra: A desktop music library builder that turns Spotify, Youtube Music Apple Music, Amazon Music, Tidal, Qobuz, and Deezer links into fully tagged local library in FLAC, ALAC, AAC, or MP3. · GitHub](https://github.com/anandprtp/Antra?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

概述：Antra 是一款桌面音乐库构建工具，可将 Spotify、YouTube Music、Apple Music 等平台的链接转换为带完整元数据的本地音乐库，支持多种无损与有损格式，并可直接用于媒体服务器。

- 🎵 支持将 Spotify、YouTube Music、Apple Music、Amazon Music、Tidal、Qobuz、Deezer 链接转换为本地音乐文件。
- 🏷️ 自动获取并写入完整元数据（标题、艺术家、专辑、封面、流派、歌词），并按“艺术家/专辑”结构整理文件。
- 💿 输出格式包括 FLAC、ALAC、AAC、MP3，兼容 Navidrome、Jellyfin、Plex 等媒体服务器。
- 🖥️ 无需安装 Python 或任何环境，直接下载运行单文件二进制（Windows/macOS/Linux）。
- 🎨 内置主题，可在设置中调整界面外观。
- ⚡ 快速上手：首次运行选择音乐库文件夹、设定输出格式、粘贴链接、点击“Add to Library”即可自动完成抓取、标记和归档。
- ⭐ 项目开源且活跃，拥有 1.9k stars；欢迎通过 issue 反馈问题，但暂不接受外部拉取请求。
- ⚠️ 仅供教育研究使用，不托管任何版权内容；用户须自行确保使用方式合法合规。

---

### [](https://github.com/geoeq/geoeq?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - geoeq/geoeq: Geotechnical engineering, solved in Python. 170+ validated functions for soil mechanics, SPT, CPT, bearing capacity, settlement, liquefaction & slope stability. Apache 2.0. · GitHub](https://github.com/geoeq/geoeq?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

GeoEq 是一个免费开源的 Python 库，提供 170 多个经过验证的岩土工程计算函数，覆盖土壤分类、现场勘察、基础设计、土动力学等，旨在用可复现的代码替代电子表格工作流。

- 📦 安装：通过 `pip install geoeq` 安装，依赖仅 numpy、matplotlib、scipy，支持 Python 3.9+。
- 🧱 核心功能：土壤分类（USCS/AASHTO/USDA）、SPT/CPT 解释、承载力（Terzaghi/Meyerhof/Hansen/Vesic）、沉降、固结、边坡稳定、土压力、桩基设计及地震液化分析。
- 📁 数据输入输出：支持读取 CSV、AGS4 和 GEF-CPT 格式的现场数据，并提供 CPT 容器类。
- 🔍 设计原则：平面 API（`import geoeq as ge`）、输入有效性检查、公式引用教科书来源、返回字典便于处理。
- ✅ 测试与验证：563 项测试对参考值进行校验，确保计算准确可靠。
- 🎓 教程与文档：提供 27 个 Jupyter 教程，涵盖全部功能，并配有在线文档（geoeq.org）。
- 🆓 许可证：Apache 2.0，允许个人、学术、商业和企业免费使用，附带专利保护。

---

### [](https://github.com/mpfaffenberger/code_puppy?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - mpfaffenberger/code_puppy: Agentic AI for writing code · GitHub](https://github.com/mpfaffenberger/code_puppy?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

Code Puppy 是一个以“愤怒反击”为灵感的 AI 编程代理项目，旨在替代传统 IDE，提供模型管理、自定义 Agent、隐私保护等强大功能，并支持多种 AI 提供商与本地模型。

- 🐶 项目核心：Code Puppy 是 AI 驱动的代码生成代理，能理解编程任务、生成高质量代码，并解释推理过程，口号是让 IDE 过时。
- ⚡ 快速开始：推荐使用 UV 安装，macOS/Linux 通过 `uvx code-puppy` 运行，Windows 建议全局安装以获得最佳快捷键体验。
- 🔌 模型支持：内置 Synthetic、Cerebras、OpenAI、Google、Anthropic 等模型，并集成 models.dev，可访问 65+ 提供商、1000+ 模型。
- 🆕 添加模型命令：使用 `/add_model` 可浏览提供商、预览模型详情并一键添加，支持实时 API 获取和离线数据库回退。
- 🔁 轮询模型分发：支持 Round Robin 模型轮询，可配置多个 API 密钥和轮换频率，有效规避速率限制。
- 📁 自定义命令与规则：支持 `.claude/commands/` 等目录的自定义斜杠命令，以及 `AGENTS.md` 文件定义编码规范和行为准则。
- 🤖 自定义 Agent 系统：内置默认 code-puppy 和 agent-creator，支持 JSON 或 Python 创建专用 Agent（如 Python 导师、代码审查、DevOps 助手）。
- 🛠️ 工具控制：Agent 可配置工具权限，包括文件读写、grep 搜索、shell 命令、推理分享等，实现细粒度访问控制。
- 🧩 MCP 与扩展：通过 `/mcp` 管理外部 MCP 服务器，并支持 DBOS 持久化执行，可崩溃恢复和续跑长任务。
- 🔒 隐私承诺：零遥测、零提示记录、零行为画像、零第三方数据共享；支持完全本地模型运行，确保数据不出网络。
- 📜 开源许可：项目采用 MIT 许可证，代码开放，社区可自由贡献和扩展。

---

### [](https://github.com/NovaSky-AI/SkyRL?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - NovaSky-AI/SkyRL: SkyRL: A Modular Full-stack RL Library for LLMs · GitHub](https://github.com/NovaSky-AI/SkyRL?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

SkyRL 是一个模块化全栈强化学习（RL）库，专为训练大语言模型（LLM）而设计，提供统一训练框架、环境构建、智能体管道及 Tinker API 支持，并已发布多个版本和外部合作项目。

- 🧠 核心定位：SkyRL 是面向 LLM 的全栈 RL 库，支持在自有硬件上训练真实世界长时程智能体（如 SWE-Bench 任务）。
- 📦 五大组件：包含 skyrl（统一库）、skyrl-train（高性能训练框架）、skyrl-tx（Tinker API 跨平台后端）、skyrl-agent（多轮智能体训练层）、skyrl-gym（Gymnasium 接口环境库）。
- 🚀 快速上手：提供开发指南、训练快速入门、环境集成文档、智能体管道说明及支持模型列表，方便用户直接使用或二次开发。
- 📰 重大更新：2025-2026 年发布多项成果，包括集成 Harbor、实现 Tinker API、推出 SkyRL-v0/v0.1、SkyRL-Agent、SkyRL-tx、SkyRL-Gym 及 SkyRL-SQL。
- 🏆 突出战绩：SkyRL-SQL 仅用 653 个样本训练的 7B 模型，在 Text-to-SQL 任务上超越 GPT-4o 和 o4-mini。
- 🔗 丰富链接：提供博客文章、论文、Hugging Face、Slack 与文档资源，涵盖异步 RL、On-Policy 蒸馏、Search-R1 等多个主题。
- 👥 生态应用：已被 Biomni-R0、Endless Terminals、CodeScout、OpenThoughts-Agent 等外部项目采用。
- 🤝 致谢与参考：项目由 Berkeley Sky Computing Lab 与 Anyscale 等机构合作，并借鉴 veRL、OpenRLHF、Search-R1 等开源工作；附录包含完整 BibTeX 引用。

---

### [](https://github.com/huangruiteng/loopx?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [GitHub - huangruiteng/loopx: Lightweight loop engineering state kernel for long-running AI agent teams. Agent-loop agnostic across Codex, Claude Code, and other coding agents, with durable goals, quota-aware auto-wake, executable todos, evidence logs, and verifiable handoffs. · GitHub](https://github.com/huangruiteng/loopx?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

LoopX 是一个轻量级的本地控制平面，专为长期运行的 AI Agent 工作设计。它通过持久化状态层（目标、门禁、待办、证据、配额）让跨轮次、跨工具、跨 Agent 的长期工作可审查、可重启、可交接，不替代 Agent 运行时，并始终保留人类判断和最终控制权。

- 🎯 核心定位：本地控制平面，管理长期 AI Agent 工作，保持目标、门禁、待办、证据、配额稳定，不替代 Agent 运行时。
- 🧠 状态内核：以目标/议题/项目为中心，维护门禁、待办、范围、证据和配额，形成“Agent 原生看板”心智模型。
- 🔄 循环机制：每个有界回合执行后写回证据、交接并更新下一待办，配额决定下一步是否继续。
- 🤝 多 Agent 对等协作：注册 Agent 通过对等声明、租约、任务边界和类型化交接协作，无需持久领导身份。
- ⏱️ 长期实战验证：OpenViking 议题修复和 Auto ML 实验轨迹均跨越 200+ 小时，公开可查，展示决策延续性。
- 🚀 快速上手：Python 3.11+，curl 一行安装，无外部运行时依赖；支持 Codex、Claude Code、Cursor、Pi 等宿主。
- ❓ 五大控制问题：目标是什么？下一步是什么？哪里需要人类判断？证据有何变化？循环能否继续？
- 🛠️ 丰富控制面：状态、配额、运行时桥、操作员界面、外部投影、领域能力（如 issue-fix、ml-experiment）等一应俱全。
- ⚖️ 安全与治理：自动执行前必须检查配额，用户门禁不可绕过，危险操作、发布和最终所有权保留给人类。
- 📚 文档生态：提供用户手册、架构、集成指南、治理、配额分配等完整文档，支持自定义运行器和高级路径。
- 🚦 当前状态：v0.4.x 早期可用，不是完整 Agent 平台或自主生产控制器；持续改进安装、适配器和终端验收。
- 📄 开源协议：MIT，欢迎贡献和反馈。

---

### [Django 6.1 发布 | 博客 | Django](https://www.djangoproject.com/weblog/2026/aug/05/django-61-released/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Django 6.1 released | Weblog | Django](https://www.djangoproject.com/weblog/2026/aug/05/django-61-released/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

Django 6.1 正式发布，带来多项新功能与可用性改进，同时标志着 Django 6.0 主流支持结束。  
- 🎉 Django 团队宣布发布 Django 6.1 版本，可从下载页面或 PyPI 获取。  
- ⚙️ 新增模型字段获取模式，可配置按需加载行为。  
- 🗑️ 数据库级删除选项支持 `ForeignKey.on_delete` 配置。  
- 📧 邮件设置改为基于字典的配置方式。  
- 🔑 本次发布使用 Jacob Walls 的 PGP 密钥（ID：131403F4D16D8DC7）。  
- ⏳ Django 6.0 已结束主流支持，最终版本 6.0.8 于昨日（2026-08-04）发布，包含安全修复。  
- 🛡️ Django 6.0 将持续获得安全与数据丢失修复至 2027 年 4 月，建议用户在此之前升级。  
- 📅 更多支持版本与未来发布计划详见下载页面。

---

### [](https://www.meetup.com/pydatahelsinki/events/315105052/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [PyData Helsinki at Visma, Wed, Aug 12, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydatahelsinki/events/315105052/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

PyData Helsinki 将在 Visma Solutions 赫尔辛基办公室举办线下技术聚会，包含三场演讲、茶歇问答及社交环节。

- 📅 时间：8 月 12 日（周三）17:30–20:30（EEST），21:00 转场附近酒吧继续交流
- 📍 地点：Visma Solutions Oy，赫尔辛基
- 🏢 主办：Jouni S. 与 Teemu S.；赞助商：NumFOCUS
- 🎤 演讲一：Allan Nevala – Mistral LLM 自定义基准测试
- 📈 演讲二：Babäk Firoozi Fooladi – 什么是生存模型？
- 🤖 演讲三：Anna Korolyuk – 用 Python 实现卡尔曼滤波器（从线性到非线性）
- 🍕 19:10 茶歇、饮料与自由交流；19:40 趣味知识问答
- ⏰ 请准时到场，迟到者可能因入口到办公区距离较远而无法入场

---

### [](https://www.meetup.com/cleveland-area-python-interest-group/events/315970116/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [ClePy August Meetup - dbt vs. SQLMesh, Tue, Aug 11, 2026, 6:00 PM   | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/315970116/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

overview summary
该内容为克利夫兰 Python 用户组（CLEpy）八月份聚会的活动通知，重点介绍了一场关于数据转换框架 dbt 与 SQLMesh 对比的演讲，并包含活动时间、地点、议程及赞助商等信息。

- 📅 活动时间：8 月 11 日（周二）下午 6:00 至 8:00（美国东部时间），地点在克利夫兰的 Happy Dog 酒吧（Underdog 地下室）。
- 👥 主办方为 Eddie C.和 Anurag S.，属于克利夫兰地区 Python 用户组（CLEpy）的常规聚会。
- 📋 议程安排：6:00-6:30 社交与设备调试及公告；6:30-7:30 主题演讲；7:30-8:00 社交与清理。
- 🎤 演讲主题：由 Eddie Cosma 主讲的“转换框架对比：dbt vs. SQLMesh”，探讨 dbt 的过度商业化问题，以及 SQLMesh 作为替代方案的技术与哲学差异，并分析各自最佳适用场景。
- 🙏 赞助与支持：感谢 Python 软件基金会（PSF）和 Happy Dog 场地与设备支持。
- ⚠️ 注意事项：若已报名但无法出席，请更改 RSVP 状态，以便候补名单人员参加。
- 💡 演讲征集：欢迎在 Meetup 或 Cleveland Tech Slack 的#clepy 频道联系主办方报名演讲；Slack 加入链接已提供。
- 🏷️ 相关主题涵盖：克利夫兰活动、人工智能、数据科学、Python、开源和软件开发。

---

### [](https://www.meetup.com/madison-python/events/315948843/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Orchest-Rated: Comparing Modern Workflow Orchestration Engines, Thu, Aug 13, 2026, 6:30 PM   | Meetup](https://www.meetup.com/madison-python/events/315948843/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

本次活动是一场由 MadPy 主办的线下技术分享，聚焦现代工作流编排引擎的深度对比，帮助开发者理解不同工具的适用场景与取舍。

- 📅 活动时间为 8 月 13 日（周四）下午 6:30–8:30（CDT），地点在麦迪逊公共图书馆中央馆。
- 🧩 主题是“Orchest-Rated：现代工作流编排引擎对比”，针对项目超出 cron 任务后需要重试、回填、任务依赖和可观测性的场景。
- ⚙️ 对比对象包括 Airflow、Dagster、Hatchet、Temporal、Prefect 等主流编排工具，重点分析各自的调度与故障处理理念。
- 🧑‍💻 演讲者 Gordon Myers 拥有 18 年软件工程经验，现任 Helpside 公司首席工程师。
- 🎯 内容涵盖开发者体验、可观测性、运维成本以及实际运行中才会暴露的权衡问题。
- 💡 适合仍在维护大量 cron 任务、考虑迁移 Airflow，或想了解其他编排方案的开发者。
- 🏷️ 相关话题涉及麦迪逊活动、数据科学、Python、开源、软件开发和科学计算。

---

### [](https://www.meetup.com/pydata-st-louis/events/315908762/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

**原文标题**: [Processing Async Jobs in Django, Tue, Aug 11, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-st-louis/events/315908762/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-757-august-6-2026)

本次聚會是 PyData St. Louis 主辦的實體活動，主題為「Processing Async Jobs in Django」，由 Aayush G. 與 Sriram D. 主持，內容涵蓋 Celery 非同步任務處理的架構、實務與最佳實踐，並包含交流與問答時間。

- 📅 活動時間：8 月 11 日（週二）下午 5:30 至 7:30（CDT），講座於 6:15 開始，6:50 至 7:30 為問答與交流。
- 📍 地點：Spark Coworking（St. Louis, MO），由 Spark Coworking 贊助場地。
- 🎤 講座主題：使用 Django 與 Celery 打造可靠的非同步應用程式，適合初學者。
- ⚙️ 核心內容：非同步任務處理的重要性、Celery 簡介、Web 伺服器與非同步工作者的溝通方式。
- 🏗️ 架構討論：常見痛點、取捨取捨、分離 Web 與 worker 依賴的最佳實踐。
- 🚀 部署維運：實際案例分享，以及部署和維護非同步工作者的實務考量。
- 👥 目標對象：對 Python、Django、後端開發、非同步程式、分散式系統或擴展性 Web 應用感興趣者皆可參加。
- 🍕 現場備有披薩，活動前後皆有 networking 機會。
- 🙏 特別感謝：Spark Coworking 提供場地並支持當地 Python 與資料科學社群。
- 🌍 PyData St. Louis 屬於全球 PyData 社群，為 NumFOCUS 旗下教育計畫。

---

