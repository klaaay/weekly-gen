### [Python中的快速网格布尔运算 · Polydera](https://polydera.com/tutorials/fast-mesh-booleans-in-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Fast Mesh Booleans in Python · Polydera](https://polydera.com/tutorials/fast-mesh-booleans-in-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

本教程介绍了 Python 中快速网格布尔运算的库 trueform，支持并集、差集和交集操作，可在百万级多边形网格上实现交互速度。

- 🐍 使用 `pip install trueform` 安装，输入输出均为 NumPy 数组
- 📦 通过 `tf.Mesh` 加载网格，支持从文件或直接传入数组
- 🔄 使用 `shared_view()` 创建共享视图，仅变换矩阵不同，避免数据复制
- 🧩 三种布尔运算：`tf.boolean_union`（并集）、`tf.boolean_difference`（差集）、`tf.boolean_intersection`（交集）
- 📊 结果返回面片、顶点、标签及源面索引，支持按标签分割和文件导出
- ⚡ 预计算空间与拓扑结构（`build_tree` 等），可在移动几何体上实现实时布尔运算（10次操作 < 140ms）
- 🔍 通过 `return_curves=True` 提取交线，或直接调用 `tf.intersection_curves`
- 🚀 性能：2×500K 多边形下，并集 14ms，交线 3.5ms，多边形排列 86ms
- 🛡️ 鲁棒性强：支持凸多边形、非流形边、自交输入等，无需预处理

---

### [闪电PyPI入侵：基于Bun的窃密器 | Snyk](https://snyk.io/blog/lightning-pypi-compromise-bun-based-credential-stealer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Lightning PyPI Compromise: Bun-Based Stealer | Snyk](https://snyk.io/blog/lightning-pypi-compromise-bun-based-credential-stealer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

2026年4月30日，流行的PyPI包lightning（原pytorch-lightning）的2.6.2和2.6.3版本被恶意篡改，内含一个通过Bun JavaScript运行时执行的凭证窃取器，影响每日超过31万次下载。该攻击与前一天npm上的“Mini Shai-Hulud”活动模式相同，属于跨生态系统的供应链攻击。

- ⚡ 恶意包在导入时触发：在`__init__.py`中植入代码，通过后台线程下载Bun v1.3.13并执行一个约11MB的混淆JavaScript文件`router_runtime.js`，用于窃取凭证。
- 🔑 窃取目标广泛：包括GitHub OAuth/PAT令牌、npm令牌、GitHub App JWT，并探测AWS IMDS/ECS等云元数据服务，验证窃取的令牌有效性。
- 🐍 仓库投毒与自我传播：利用GitHub GraphQL以伪造身份`claude`提交恶意文件，并具备修改本地npm包并直接发布到registry.npmjs.org的蠕虫能力。
- 🚨 发布路径暴露：攻击者很可能利用泄露的长期PyPI API令牌直接上传恶意包，绕过了GitHub Actions工作流，且项目未配置OIDC可信发布者。
- 🕵️ 披露过程被干扰：社区成员在GitHub上提交的4个安全披露问题，被疑似被攻陷的CI服务账号`pl-ghost`在几分钟内自动关闭，直到维护者介入。
- 🧬 跨生态复用工具：恶意载荷是JavaScript，通过Python包装器在Python生态中复用npm攻击工具，其混淆特征（PBKDF2/SHA-256，200,000次迭代）与之前多个攻击事件相同。
- 🛡️ 建议立即行动：将受影响的系统视为已攻陷，降级至2.6.1版本，轮换所有可访问的凭证，审计GitHub提交和CI/CD日志，并检查npm包完整性。

---

### [boc：面向行为的Python并发](https://microsoft.github.io/bocpy/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [boc: Behavior-Oriented Concurrency for Python](https://microsoft.github.io/bocpy/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

### 概述总结
BOC（面向行为的并发）是一种专为Python设计的无锁、无死锁、基于所有权的并行编程范式。它通过cown（并发所有权变量）和behavior（行为）机制，让程序员只需关注数据流组织，而无需处理锁或线程同步，从而实现多核性能。

- 🧩 **核心概念**：BOC使用cown确保数据在任意时刻只被一个执行线程独占访问，behavior则通过`@when`装饰器声明所需cown，运行时按全局顺序两阶段锁定，从根本上避免死锁。
- 🔒 **无锁实现**：cown所有权通过C语言级别的无锁原子操作（如compare-and-swap）管理，无需互斥锁；调度器、cown交接和工作者分发均为非阻塞C代码。
- 🍳 **示例简化**：以模拟制作煎蛋卷为例，传统线程+锁的代码需要显式拆分任务、获取/释放锁和条件变量；而BOC版本只需将资源包装为cown，用`@when`声明行为，代码更简洁、易读且自动并行。
- 📡 **Noticeboard**：全局键值存储，用于行为间共享轻量级最终一致状态（如配置、计数器），支持非阻塞写入、原子更新和快照读取（最多64键，每键63字节）。
- 🧮 **Matrix类**：内置的C语言实现稠密双精度浮点矩阵，支持跨解释器零拷贝传输，可安全放入cown中，提供元素运算、矩阵乘法、索引切片和归约等操作。
- 📈 **性能扩展**：行为在Python 3.12+的独立子解释器上并行运行，实现近线性吞吐量扩展（14核机器上测试），得益于无锁工作窃取调度器和零拷贝cown交接。

---

### [你的API无法处理真实世界的集成 - YouTube](https://www.youtube.com/watch?v=rZpwFN_n2-g&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Your API Can’t Handle Real-World Integrations - YouTube](https://www.youtube.com/watch?v=rZpwFN_n2-g&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

本頁面列出了 YouTube 平台的主要資訊與政策連結，涵蓋法律、創作與營運等面向。
- 📰 新聞中心：提供 YouTube 官方最新消息與公告。
- ©️ 版權：說明內容使用的版權規範與權利保護。
- 📞 聯絡我們：提供使用者與 YouTube 團隊聯繫的管道。
- 🎨 創作者：針對內容創作者提供的資源與指引。
- 📢 刊登廣告：說明在 YouTube 上投放廣告的相關資訊。
- 👨‍💻 開發人員：提供 API 與技術整合的開發資源。
- 📜 條款：列出使用 YouTube 服務的相關條款與條件。
- 🔒 私隱：說明個人資料的收集、使用與保護政策。
- 🛡️ 政策及安全：涵蓋內容審查、社群規範與安全措施。
- ⚙️ YouTube 的運作方式：解釋平台如何推薦與管理內容。
- 🧪 測試新功能：介紹 YouTube 正在測試中的新功能。
- 📅 © 2026 Google LLC：標示版權歸屬與年份。

---

### [使用单个Python字典将多模态推理性能提升超过10%](https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Boosting multimodal inference performance by >10% with a single Python dictionary](https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

通过一个简单的Python字典缓存，将多模态推理性能提升超过10%

- 📈 通过缓存CUDA IPC池句柄，吞吐量提升16.2%（从22.2 req/s到25.7 req/s）
- ⏱️ 平均首令牌时间（TTFT）降低13.2%（从965ms降至838ms）
- ⚡ 平均每输出令牌时间（TPOT）降低17.2%（从72ms降至60ms）
- 🔍 使用py-spy分析发现，调度器在`process_input_requests`中重复调用`_new_shared_cuda`造成瓶颈
- 🗂️ 解决方案是用Python字典缓存池句柄，避免每次迭代重复打开共享内存
- 🎯 优化适用于所有使用SGLang CUDA IPC传输的多模态模型
- 🧠 解码延迟也意外改善，因为调度器单线程运行，输入处理加速释放了GPU调度时间
- ✅ 该优化已合并到SGLang v0.5.10，可通过`--enable-pool-handle-cache`标志启用

---

### [使用DuckDB进行全文搜索 - peterdohertys.website](https://peterdohertys.website/blog-posts/full-text-search-w-duckdb.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Full-Text Search with DuckDB - peterdohertys.website](https://peterdohertys.website/blog-posts/full-text-search-w-duckdb.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

### 概述总结
本文详细介绍了DuckDB全文搜索（FTS）扩展的功能、设置方法及应用场景，并对比了其与PostgreSQL和Elasticsearch的差异。

- 📄 **FTS核心功能**：支持词干提取、停用词移除、重音归一化及Okapi BM25算法（含k₁和b参数调优）。
- ⚙️ **安装与配置**：通过`INSTALL fts`和`LOAD fts`命令即可启用扩展，操作简便。
- 📧 **实战案例**：以处理13,010封邮件为例，展示从预处理（Python解析.eml文件）到导入DuckDB、创建索引及执行查询的完整流程。
- 🔍 **查询优化**：支持布尔查询（conjunctive参数）、BM25参数调优（如b=0忽略文档长度，b=1惩罚长文档），以及k₁控制词频权重。
- ⚠️ **功能局限**：缺少关键词高亮功能（如PostgreSQL的`ts_headline`），需借助外部工具（如grep）辅助定位匹配内容。
- 🛠️ **调试工具**：推荐使用Snowball项目（Python库`snowballstemmer`）验证词干提取逻辑，解决匹配异常问题。
- 📊 **性能与扩展性**：DuckDB FTS适合快速探索性分析，若需复杂功能（如短语查询、向量搜索），可迁移至PostgreSQL或Elasticsearch。
- 🔮 **未来展望**：作者计划后续探讨DuckDB的向量搜索功能，并期待社区贡献短语查询、同义词词典等扩展。

---

### [使用词袋模型与PyCharm | PyCharm博客](https://blog.jetbrains.com/pycharm/2026/04/using-bag-of-words-with-pycharm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Using Bag-of-Words With PyCharm | The PyCharm Blog](https://blog.jetbrains.com/pycharm/2026/04/using-bag-of-words-with-pycharm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

该文章介绍了词袋模型（Bag-of-Words, BoW）在自然语言处理中的应用，并展示了如何使用PyCharm构建文本分类项目。

- 📚 **词袋模型概述**：将文本转换为数值向量，忽略语法和词序，仅记录单词出现频率，适用于文本分类和情感分析等任务。
- 🔧 **工作流程**：包括分词、构建词汇表、编码（如二进制或计数向量化），最终形成稀疏矩阵。
- ✅ **优势**：简单、计算高效，适合作为基线模型，尤其适用于情感分析和主题分类。
- 🛠️ **PyCharm工具支持**：利用代码补全、调试、Jupyter集成、AI助手和DataFrame可视化，简化预处理和模型开发。
- 📊 **项目实践**：使用AG News数据集，通过PyCharm进行数据清洗、停用词移除、词形还原、TF-IDF向量化和神经网络训练，实现92%的验证准确率。
- 🚀 **高级技术**：包括停用词移除、词形还原、TF-IDF加权、n-grams和降维，以提升模型效率和泛化能力。
- ⚠️ **局限性**：丢失词序和语义，生成高维稀疏向量；替代方案包括词嵌入（Word2Vec）、Transformer模型（BERT）和主题模型（LDA）。
- 🎯 **最终结果**：测试准确率达91.8%，证明预处理和特征选择显著提升模型稳定性和效率。

---

### [我们如何用深度学习重建Faire的搜索排名 | 作者：Yin Ki Ng | 2026年4月 | The Craft](https://craft.faire.com/how-we-rebuilt-search-ranking-at-faire-with-deep-learning-14f080679c83?gi=9e7b30c23782&utm_campaign=python-weekly-issue-744-may-7-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

**原文标题**: [How we rebuilt search ranking at Faire with deep learning | by Yin Ki Ng | Apr, 2026 | The Craft](https://craft.faire.com/how-we-rebuilt-search-ranking-at-faire-with-deep-learning-14f080679c83?gi=9e7b30c23782&utm_campaign=python-weekly-issue-744-may-7-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

概述总结
Faire通过深度学习重建搜索排名系统，从XGBoost迁移至深度学习的两年历程，解决了多目标优化、跨表面学习等挑战，并取得显著业务增长。

- 🚀 从XGBoost到深度学习的转型：为应对多目标优化、序列建模、位置偏差和跨表面学习等限制，Faire团队耗时两年重建了数据管道、训练框架、评估方法和生产服务基础设施。
- 🎯 多任务学习解锁核心能力：通过设计会话归一化的列表式交叉熵损失函数，将相关性和新鲜度作为独立任务纳入多任务学习框架，成功平衡了多个优化目标，无需后处理启发式规则。
- 🔄 跨表面微调提升效率：基于产品搜索排名器微调品牌页面搜索模型，将开发周期缩短约一半，并实现跨表面一致的排名信号，减少数据需求。
- 📊 数据质量与特征工程关键：建立数据可观测性系统监控重复率、会话长度等指标；采用分布感知归一化（对数变换/Z-score）和NaN指示列处理缺失值，显著提升模型性能。
- ⚡ 服务基础设施优化：自定义Docker镜像（Nginx+Gunicorn+Flask）替代TorchServe，减少启动延迟；实现共享内存模块复用嵌入表；采用CPU沙箱和GPU实例降低延迟与成本。
- 📈 显著业务影响：2025年产品搜索排名器在北美和欧洲分别实现+2.14%和+1.54%的订单量增长；品牌页面搜索通过微调获得+0.14%订单量提升。
- 🔮 未来方向：探索序列感知模型（如深度兴趣网络DIN）、位置去偏（训练时嵌入位置信息，服务时移除）、以及针对长尾查询和新兴品牌的细分优化。

---

### [Polars — 处理 Polars 中的模式问题](https://pola.rs/posts/schema-evolution/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Polars — Handling Schema Issues in Polars](https://pola.rs/posts/schema-evolution/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

Polars 中处理数据模式变更的四种场景及对应解决方案

- 📋 **四种模式变更类型**：新增列、缺失列、类型漂移、破坏性变更（重命名/不兼容类型），每种类型需要不同的处理参数
- 📄 **CSV 文件处理**：使用 `schema_overrides` 覆盖特定列类型，`schema` 强制完整模式，`infer_schema=False` 全部读为字符串，`ignore_errors=True` 将错误值设为 null
- 📁 **多文件 Parquet 处理**：`missing_columns="insert"` 处理新增/缺失列，`ScanCastOptions(integer_cast="upcast")` 处理类型漂移，`diagonal_relaxed` 同时处理两种问题
- 🗄️ **Delta Lake 处理**：`schema_mode="merge"` 处理新增和缺失列，重命名和不兼容类型需在写入前显式处理
- 🧊 **Apache Iceberg 处理**：通过目录 `update_schema()` 处理新增列、重命名和类型扩展，`pl.scan_iceberg` 自动解析变更，无需额外参数

---

### [GitHub - promptise-com/Foundry：智能体智能的基础层。· GitHub](https://github.com/promptise-com/foundry?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [GitHub - promptise-com/Foundry: The foundation layer for agentic intelligence. · GitHub](https://github.com/promptise-com/foundry?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

Promptise Foundry 是一个用于构建全栈智能体系统的开源框架，提供从开发到生产的一站式解决方案。

- 🤖 **智能体构建**：通过一个函数调用即可将任意LLM转化为生产级智能体，支持自动MCP工具发现、语义缓存、安全扫描和沙箱执行。
- 🧠 **推理引擎**：提供20种节点类型和7种预置模式，支持像编写代码一样组合推理逻辑，实现灵活可控的智能体行为。
- 🔧 **MCP服务器SDK**：生产级协议服务器，内置JWT/OAuth2访问控制、12+中间件（限流、审计、缓存等）和HMAC审计日志，确保安全与可扩展性。
- ⚡ **智能体运行时**：作为自主智能体的操作系统，支持5种触发类型、崩溃恢复、预算控制和14个生命周期钩子，保障稳定运行。
- ✨ **提示工程**：将提示视为软件而非字符串，提供8种块类型、5种可组合策略和14个上下文提供者，支持版本管理和回滚。
- 📦 **快速上手**：30秒内通过`pip install promptise`安装，并支持与LangChain模型、Docker沙箱、Kubernetes等现有生态集成。
- 🌟 **开源社区**：拥有829颗星标和127个分支，采用Apache 2.0许可，欢迎贡献和讨论。

---

### [GitHub - raullenchai/Rapid-MLX: 苹果芯片上最快的本地AI引擎。比Ollama快4.2倍，缓存TTFT仅0.08秒，100%工具调用。17个工具解析器、提示缓存、推理分离、云路由。即插即用的OpenAI替代方案。兼容Claude Code、Cursor、Aider。](https://github.com/raullenchai/Rapid-MLX?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [GitHub - raullenchai/Rapid-MLX: The fastest local AI engine for Apple Silicon. 4.2x faster than Ollama, 0.08s cached TTFT, 100% tool calling. 17 tool parsers, prompt cache, reasoning separation, cloud routing. Drop-in OpenAI replacement. Works with Claude Code, Cursor, Aider. · GitHub](https://github.com/raullenchai/Rapid-MLX?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

Rapid-MLX 是一个专为苹果 Silicon Mac 设计的本地 AI 推理引擎，比 Ollama 快 4.2 倍，支持工具调用、提示缓存和云路由，可无缝替代 OpenAI API。

- 🚀 **极速性能** — 在 Mac Studio M3 Ultra 上，Qwen3.5-4B 达 160 tok/s，Nemotron-Nano 30B 达 141 tok/s，比 Ollama 快 2.3-3.2 倍。
- 💻 **简易安装** — 支持 Homebrew 或 pip 一键安装，运行 `rapid-mlx serve qwen3.5-4b` 即可启动本地 AI 服务器。
- 🔧 **全面工具调用** — 支持 17 种解析器格式（Hermes、Qwen、DeepSeek 等），具备自动恢复功能，可修复量化模型输出的错误工具调用。
- 🧠 **智能推理分离** — Qwen3、DeepSeek-R1 等模型的思维链内容自动分离到 `reasoning_content` 字段，不干扰主输出。
- ⚡ **提示缓存** — 标准 Transformer 使用 KV 缓存修剪，混合模型（如 Qwen3.5 DeltaNet）使用 RNN 状态快照，TTFT 提速 2-5 倍。
- ☁️ **云路由** — 大上下文请求自动路由到云端 LLM（如 GPT-5、Claude），避免本地预填缓慢。
- 🖼️ **多模态支持** — 视觉、音频（TTS/STT）、视频理解和文本嵌入，全部通过 OpenAI 兼容 API 提供。
- 📊 **模型选择指南** — 根据 Mac 内存提供推荐模型（16GB 用 Qwen3.5-4B，64GB 用 Qwen3.5-35B，128GB 用 DeepSeek V4 Flash），附速度和质量说明。
- 🔌 **广泛兼容** — 支持 Cursor、Claude Code、Aider、PydanticAI、LangChain 等流行工具，只需将 API 地址指向 `localhost:8000/v1`。
- 🛠️ **高级功能** — 包括 TurboQuant V 缓存压缩、KV 缓存量化、连续批处理、结构化 JSON 输出、日志概率 API 和 2100+ 测试。

---

### [GitHub - alexgreensh/token-optimizer: 找到幽灵令牌。修复它们。在压缩中存活。避免上下文质量衰减。](https://github.com/alexgreensh/token-optimizer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [GitHub - alexgreensh/token-optimizer: Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay. · GitHub](https://github.com/alexgreensh/token-optimizer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

Token Optimizer 是一款专为 AI 代理系统（如 Claude Code、OpenClaw、Codex）设计的上下文优化工具，旨在解决 AI 在长对话中因上下文膨胀导致的性能下降和 Token 浪费问题。

- 📊 **全面可见性仪表板**：提供实时、可书签的 HTML 仪表板，追踪每次会话的每个 Token、花费和交互回合，包括按模型、缓存和子代理细分的成本分析。
- 🧹 **双重 Token 浪费治理**：不仅处理运行时输出（占 15-25%），还解决结构性浪费（占 75-85%），如臃肿的配置文件、未使用的技能和冗余的系统提示。
- 🛡️ **智能压缩与会话连续性**：在自动压缩前创建检查点，恢复被摘要丢弃的关键决策，并归档大型工具结果，确保会话在压缩后无缝衔接。
- 📈 **7 信号质量评分**：通过上下文填充率、陈旧读取、冗余结果等指标实时评估会话健康度，并给出从 S 到 F 的等级，帮助用户及时干预。
- 🔧 **主动压缩功能 (v5)**：包括增量模式、结构映射、循环检测、Bash 输出压缩等 7 项功能，可独立开关，平均节省 10-30% 的 Token。
- 🧠 **教练模式与舰队审计**：通过 `/token-coach` 提供针对性优化建议，并支持跨多个代理系统扫描浪费，按成本排序问题。
- 🔒 **100% 本地运行**：零网络调用、零遥测、零运行时依赖，所有数据存储在本地 SQLite 文件中，用户完全掌控隐私。
- 🏢 **灵活的许可模式**：个人、研究及小团队（少于 5 人或月收入低于 2 万美元）可免费使用，商业使用需联系获取许可。

---

### [GitHub - intel/auto-round：一种用于高精度低比特LLM推理的SOTA量化算法，针对CPU/XPU/CUDA无缝优化，支持多种数据类型，并完全兼容vLLM、SGLang和Transformers。](https://github.com/intel/auto-round?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [GitHub - intel/auto-round: A SOTA quantization algorithm for high-accuracy low-bit LLM inference, seamlessly optimized for CPU/XPU/CUDA, with multi-datatype support and full compatibility with vLLM, SGLang, and Transformers. · GitHub](https://github.com/intel/auto-round?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

AutoRound 是英特尔推出的先进量化工具包，专为大语言模型和视觉语言模型设计，能在超低位宽下保持高精度，并支持多种硬件和框架。

- 🚀 **核心功能**：利用符号梯度下降实现2-4位超低位宽量化，精度领先，支持CPU/GPU/HPU等多种硬件。
- 🆕 **最新更新**：新增块级FP8、MTP层量化、混合精度算法，并集成至vLLM、SGLang、Transformers等主流框架。
- ✨ **关键特性**：支持多种导出格式（AutoRound、GGUF等）、快速混合位宽方案生成、10+视觉语言模型开箱即用，量化成本低（7B模型约10分钟）。
- 📦 **安装方式**：支持PyPI安装（CPU/GPU/HPU/XPU）及源码编译，提供稳定版和每日构建版。
- ⚙️ **使用方式**：提供CLI和API两种模式，支持自定义量化方案、算法设置、校准数据集等超参数，并包含最佳精度和快速模式两种预设。
- 🧠 **自适应方案**：AutoScheme可自动生成混合位宽/数据类型量化方案，实现灵活配置。
- 🖥️ **推理支持**：无缝对接vLLM、SGLang、Transformers等推理框架，自动选择最佳后端。
- 📚 **学术成果**：发表多篇论文（SignRoundV1/V2、TEQ等），提供完整出版物列表。
- 🌟 **社区支持**：开源项目（Apache-2.0许可），欢迎贡献和星标，已获1.4k星标和132个分支。

---

### [GitHub - raulcd/datanomy：剖析数据结构 · GitHub](https://github.com/raulcd/datanomy?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [GitHub - raulcd/datanomy: Dissecting data structures · GitHub](https://github.com/raulcd/datanomy?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

Datanomy 是一个终端工具，用于检查和分析列式数据文件（目前仅支持 Parquet 格式），提供交互式视图查看数据结构、元数据和内部组织。

- 📂 **项目概况**：开源项目，获得 406 星标和 8 个复刻，采用 Apache-2.0 许可证
- 🔍 **核心功能**：支持查看 Parquet 文件的通用结构、模式、数据、元数据和统计信息
- 🛠️ **安装方式**：可通过 PyPI（`pip install datanomy`）或源码安装，支持 `uv` 工具
- 🚀 **使用方式**：直接运行 `datanomy data.parquet`，或使用 `uvx` 无需安装即可运行
- ⌨️ **快捷键支持**：按 `q` 键退出应用
- 👨‍💻 **开发指南**：使用 `uv sync` 安装依赖，通过 `pytest` 测试，`ruff` 格式化代码
- 📦 **技术栈**：基于 Textual 和 PyArrow 构建
- 🤝 **贡献方式**：欢迎通过提交 Issue 或 PR 参与贡献

---

### [GitHub - bluerock-io/bluerock: Python MCP服务器的运行时可见性。捕获工具调用、会话生命周期、模块导入（SHA-256）和子进程执行，输出为结构化NDJSON。无需修改代码。Apache 2.0](https://github.com/bluerock-io/bluerock?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [GitHub - bluerock-io/bluerock: Runtime visibility for Python MCP servers. Captures tool calls, session lifecycle, module imports (SHA-256), and subprocess execution as structured NDJSON. No code changes. Apache 2.0 · GitHub](https://github.com/bluerock-io/bluerock?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

BlueRock 是一个针对 Python MCP 服务器的轻量级运行时安全监控工具，无需修改代码即可捕获工具调用、会话生命周期、模块导入等事件，并以结构化 NDJSON 格式输出。

- 🔒 零代码变更：只需用 `python -m bluepython --oss your_script.py` 包装脚本，无需导入或 SDK 集成
- 🛡️ 全面 MCP 覆盖：监控工具调用、资源访问、会话生命周期、传输连接等 6 种事件类型
- 📦 导入监控：记录每个模块导入的名称、路径、版本和 SHA-256 哈希值，覆盖所有依赖及其传递依赖
- 🚀 启动前挂接：在 Python 启动时激活，确保代码和依赖的操作无一遗漏
- 📊 结构化输出：事件以 NDJSON 格式写入 `~/.bluerock/event-spool/`，支持 jq 查询和 Grafana 仪表盘
- 🔧 灵活配置：通过 JSON 配置文件启用/禁用特定钩子，支持 MCP 和导入监控
- 🌐 多平台支持：提供 Linux、macOS 的预编译轮子，支持 Python 3.10+
- 📝 开源许可：Apache 2.0 许可证，可自由审查和贡献钩子

---

### [Django 安全版本发布：6.0.5 和 5.2.14 | 博客 | Django](https://www.djangoproject.com/weblog/2026/may/05/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Django security releases issued: 6.0.5 and 5.2.14 | Weblog | Django](https://www.djangoproject.com/weblog/2026/may/05/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

Django 发布了安全更新版本 6.0.5 和 5.2.14，修复了三个低严重性安全漏洞，建议所有用户尽快升级。

- 🛡️ **CVE-2026-5766**：ASGI 请求中缺少或低估 `Content-Length` 头部可绕过 `FILE_UPLOAD_MAX_MEMORY_SIZE` 限制，导致大文件加载到内存中引发服务降级（低严重性）
- 🔒 **CVE-2026-35192**：当 `SESSION_SAVE_EVERY_REQUEST` 为 `True` 且会话未修改时，响应头部未根据 Cookie 变化，攻击者可通过缓存公共页面窃取用户会话（低严重性）
- 🗂️ **CVE-2026-6907**：`UpdateCacheMiddleware` 错误缓存包含 `Vary: *` 的请求，可能导致私有数据被存储和泄露（低严重性）
- 📦 **受影响版本**：Django main、6.0 和 5.2 分支
- 🔧 **修复版本**：Django 6.0.5 和 5.2.14（提供 tarball 和校验和下载）
- 📧 **安全报告**：请通过 security@djangoproject.com 私密报告安全问题，勿使用 Trac 或论坛

---

### [西雅图城市大学（贝尔镇）Python之夜，2026年5月13日星期三下午5:30 | 聚会](https://www.meetup.com/psppython/events/314354455/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Python talk night at City University Seattle (Belltown), Wed, May 13, 2026, 5:30 PM   | Meetup](https://www.meetup.com/psppython/events/314354455/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

概述
西雅图城市大学（Belltown校区）举办的Python讲座之夜活动，由Puget Sound Programming Python (PuPPy)组织，包含多个技术演讲和社交环节。

- 📅 活动时间：2023年5月13日（周三）下午5:30至7:30（PDT），后续有社交时段和After Party
- 🏢 地点：西雅图城市大学，521 Wall Street, Seattle, WA
- 🎤 演讲内容：包括“LLM驱动的合并冲突解决器”（Advitya Gemawat）、“Kubernetes in Azure”（William Harding）和“设计模式详解：单例模式”（Maria Mckinley）
- 🍕 赞助商：Pecado Bueno、ActiveState和Slalom Consulting提供食物赞助
- 🚪 入场：从6th Ave和Wall Street入口进入，提供街边和付费车库停车，附近有公交站
- 📜 行为准则：所有参与者需遵守PuPPy行为准则
- 🎉 社交环节：5:30-6:00开门/社交，7:30-8:00社交，之后在Teku Tavern举办After Party

---

### [ChiPy 2026年5月__main__会议，2026年5月14日星期四下午6:00 | Meetup](https://www.meetup.com/_chipy_/events/314520034/)

**原文标题**: [ChiPy May 2026 __main__ Meeting, Thu, May 14, 2026, 6:00 PM   | Meetup](https://www.meetup.com/_chipy_/events/314520034/)

ChiPy 2026年5月__main__会议将于5月14日在芝加哥举行，由Slalom Build主办，提供餐饮并安排两场技术演讲，重点讨论AI代理中的单位类型安全与维度分析。

- 📅 **会议时间与地点**：2026年5月14日（周四）下午6点至8点，地点为芝加哥东伦道夫街200号Slalom Build大厦38楼3800室。  
- 🍕 **活动流程**：下午6点提供餐饮，6点30分开始演讲。  
- 🎤 **主讲人及主题**：Emmanuel I. Obi将发表演讲《单位即类型：请如此对待它们》，面向中级水平听众。  
- 🤖 **核心内容**：演讲将展示如何通过ucon的MCP服务器将维度分析作为AI代理的验证工具，帮助模型在生成配置、IaC等任务中自我纠错，并强调小型模型结合代数验证优于大型模型。  
- 🛡️ **安全验证**：演讲将演示结构化错误响应（如维度向量、预期/实际值对）如何让AI代理单次重试即可修正错误，并解决现有单位库无法表示的“种类-数量”违规问题。  
- 🔑 **参会要求**：需提供完整法定姓名和邮箱以获取邀请，入场时需出示带照片的身份证件。

---

### [Python 演示之夜 @ 线上（PPN #147），2026年5月14日，周四，晚上7:00 | Meetup](https://www.meetup.com/pymntos-twin-cities-python-user-group/events/314610956/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Python Presentation Night @ Virtual (PPN #147), Thu, May 14, 2026, 7:00 PM   | Meetup](https://www.meetup.com/pymntos-twin-cities-python-user-group/events/314610956/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

Python 演示之夜（PPN #147）是一场由 PyMNtos 组织的线上活动，旨在分享 Python 相关知识和经验，鼓励社区参与。

- 🎤 活动由 Andrew L. 等人主持，通过 Google Meet 线上举办，提供 Python 演示和讨论。
- 📅 日程包括 7:00 开场、7:15 正式演讲、9:00 结束，期间可分享 Python 小技巧或职位信息。
- 🐍 演讲主题包括 Andrew Laws 的“使用 Docker 进行 API 和数据库 ORM 开发”，并鼓励志愿者报名演讲。
- 📋 活动遵循 PSF 行为准则，要求尊重他人，并提醒参与者及时更新 RSVP。
- 🤝 鼓励通过 Slack 或邮件加入 PyMNtos 社区，并欢迎捐赠支持本地 Python 用户组。
- 💡 相关主题涵盖数据科学、开源 Python 和 Python Web 开发，由 Python 软件基金会赞助。

---

### [类型化Python：让开发者与AI不再猜测的契约，2026年5月16日星期六下午1:15 | Meetup](https://www.meetup.com/vegaspy/events/313905611/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Typed Python: Contracts That Keep Developers and AI from Guessing, Sat, May 16, 2026, 1:15 PM   | Meetup](https://www.meetup.com/vegaspy/events/313905611/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

本次演讲展示了强类型如何将隐式假设转化为显式契约，保护代码免受人为错误和AI生成错误的影响。涵盖了日常工程中类型的实用价值：用定义的数据类型替换松散字典、清晰地对类、方法和函数进行类型标注、使用泛型构建可复用抽象，以及应用协议为boto3等类型不完善的库创建更安全的接口。同时直接针对AI场景：当代码库具有清晰类型和稳定契约时，开发者和AI工具猜测、虚构形状或误用API的空间更小。强类型能提升可读性、更早捕获接口漂移、使重构更安全，并为代码生成工具提供更严格的边界。核心信息是：类型化Python不仅是文档或风格，更是现代开发的实用安全系统。

- 📅 活动时间：2025年5月16日周六下午1:15-2:45（PDT），每月第三个周六持续至2027年1月16日
- 📍 地点：拉斯维加斯第三街814号（Tech Alley聚会空间）
- 🎤 主办方：VegasPy（拉斯维加斯Python用户组）与Adam E.
- 🔒 核心观点：强类型将隐式假设转为显式契约，防止人为与AI错误
- 📦 实用技巧：用定义类型替代松散字典，清晰标注类/方法/函数类型
- 🔄 高级应用：使用泛型构建可复用抽象，通过协议为boto3等弱类型库创建安全接口
- 🤖 AI场景：清晰类型减少AI猜测空间，提升代码生成工具的准确性
- ✅ 综合收益：提升可读性、早期捕获接口漂移、安全重构、为AI工具提供严格边界
- 🏷️ 相关标签：#VegasTech

---

### [ClePy五月聚会：AI辅助学习的实用Python流程，2026年5月12日星期二下午6:00 | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/314537005/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [ClePy May Meetup: Practical Python pipeline for AI assisted learning, Tue, May 12, 2026, 6:00 PM   | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/314537005/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

ClePy五月聚会：AI辅助学习的实用Python管道

- 📅 活动时间：5月12日周二下午6点至8点（美国东部时间），地点在Happy Dog酒吧的Underdog地下室
- 🎤 核心演讲：Curtis O'Neal展示`video2mdnotes`项目——一个将视频内容自动转录并生成结构化Markdown笔记的Python管道
- 🛠️ 技术栈：使用yt-dlp、Whisper本地模型、FastAPI、Docker、Anthropic/OpenAI API、llm工具及Chrome插件等
- 🎯 应用场景：帮助用户快速消化未观看的会议演讲、教程视频，实现AI辅助学习笔记整理
- 🔄 开发历程：从简单Python和bash脚本起步，通过手工编码和AI辅助编码迭代优化
- 👤 演讲者背景：Curtis O'Neal是AI工程师，联合组织克利夫兰AI与数据聚会，专注于数据工程、医疗分析和AI咨询
- 🍻 活动流程：6:00-6:30社交与准备，6:30-7:30演讲，7:30-8:00社交与清理
- 📂 额外信息：演讲结束时将提供项目仓库邀请，并预览第二版计划

---

### [加速（生物）数据科学的即用资源，2026年5月12日（周二）下午6:30 | Meetup](https://www.meetup.com/pydata-pittsburgh/events/314391658/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

**原文标题**: [Drop-in Resources for Accelerating (Biological) Data Science, Tue, May 12, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-pittsburgh/events/314391658/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-744-may-7-2026)

概述：PyData Pittsburgh将于5月12日举办一场关于加速（生物）数据科学的线下活动，由NVIDIA的Ben Busby主讲，重点介绍RAPIDS开源库在GPU上的应用。

- 🧬 活动主题：利用RAPIDS工具加速生物数据科学工作流
- 📅 时间地点：5月12日周二晚6:30-8:30，卡内基梅隆大学Baker Hall
- 🎤 主讲人：NVIDIA全球联盟经理Ben Busby，兼任CMU计算生物学系教授
- 🚀 核心技术：开源Python库RAPIDS，在GPU上加速数据科学
- 🔍 涵盖主题：向量搜索、大规模图分析、稀疏矩阵、加速随机森林与XGBoost
- 🧫 生物应用：RAPIDS单细胞分析及相关工具
- 🎯 适用人群：生物数据科学家及所有数据科学从业者
- 🤝 赞助方：NumFOCUS（推广开源科学代码）

---

