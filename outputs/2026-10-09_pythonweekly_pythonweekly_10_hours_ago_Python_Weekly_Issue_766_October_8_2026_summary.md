### [](https://www.datadoghq.com/blog/engineering/async-python-profiler/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [How we built an async-aware Python profiler | Datadog](https://www.datadoghq.com/blog/engineering/async-python-profiler/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Datadog 工程团队为 Python 构建了异步感知的性能分析器，解决 asyncio 任务关系在传统火焰图中丢失的问题；通过 stacked stacks 重建任务依赖树，并用受保护 memcpy 替代 process_vm_readv，将 profiler 开销降低超过 60%，在生产中定位并修复了多个性能问题。这些改进已在 ddtrace 最新版本提供。

- 🧵 asyncio 改变了 Python 执行模型：单线程中多个协程和任务并发推进，由事件循环调度，任务可独立运行，甚至比创建它的任务活得更久。
- 🔥 传统火焰图不足：每个 asyncio 任务被显示为独立栈，丢失应用路径关系，例如无法看出 `handle_request → signup → Cassandra/metrics` 的依赖链。
- 🧱 提出“stacked stacks”：跟踪任务之间的父子与等待关系，先构建每个任务的帧栈，再构建任务依赖树，把相关任务堆叠展示。
- 🌲 构建任务依赖树：从叶子任务开始压入其帧，再寻找等待它的父任务并继续，直到最外层任务，从而保留异步上下文。
- ⏳ 处理任务比创建者长寿：任务运行期间时间归创建者；创建者结束后若被其他任务 await，后续时间归等待者，更符合调试直觉。
- 🧮 异步采样更复杂：同步 profiler 只需按线程采样，异步 profiler 还需遍历所有任务，增加 `O(n_tasks)` 复杂度，并复制大量小对象。
- 🐌 process_vm_readv 成为瓶颈：作为系统调用，它适合大块连续内存复制，但对任务、协程等大量小结构开销过高。
- 🚫 不能简单对任务做蓄水池采样：必须获取所有任务元数据才能构建一致的任务依赖树，否则会破坏 stacked stacks。
- ⚡ 初步优化：移除采样路径中的 C++ 异常降低 15% 开销，驻留函数名和文件名等字符串再降低 25%，但仍不足。
- 🛡️ 关键优化：用受保护 memcpy 替代 process_vm_readv，通过 sigaction 捕获 SIGSEGV/SIGBUS 并恢复，故障时丢弃样本，正常路径接近 memcpy 速度。
- 📉 优化结果：同步代码 profiler 开销降低约 50%，生产服务整体 profiler 开销降低 60%+，自适应采样不再卡在最低频率，profile 保真度更高。
- 🐛 生产发现：Bits Chat API 超时源于 pylzstr 解压畸形 LLM 输入时死循环，已上游修复；还发现 INFO logger 下生成巨大 debug 字符串浪费 CPU。
- 🧪 生产优化：NumPy 异常检测热点通过 MCP 工具和动态插桩优化，相关函数 CPU 降低约 15%-30%，可在不减少数据量的情况下节省核心。
- ✅ 结论：异步感知 profiling 保留任务执行上下文，更容易定位 CPU 与延迟回归；ddtrace 用户可升级获得更低开销和更高保真度的异步 profile。

---

### [Python 3.15 是一次比我预期更大的更新 - YouTube](https://www.youtube.com/watch?v=bgeqL4Btou0&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Python 3.15 Is a Bigger Update Than I Expected - YouTube](https://www.youtube.com/watch?v=bgeqL4Btou0&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

这是 YouTube 页面底部的导航与法律信息汇总，涵盖平台介绍、合作入口、政策条款及版权声明。

- ℹ️ 提供“关于”“新闻”“版权”“联系我们”等基础信息入口
- 👥 包含“创作者”“广告”“开发者”等合作与资源链接
- ⚖️ 列出“条款”“隐私”“政策与安全”等法律与安全相关内容
- ⚙️ 提供“YouTube 如何运作”说明及“测试新功能”入口
- ©️ 页面版权归 Google LLC 所有，标注年份为 2026

---

### [](https://huggingface.co/blog/stephen-solka/use-jev-to-delete-fundraising-emails?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Can Jev save my inbox from the Democrats?](https://huggingface.co/blog/stephen-solka/use-jev-to-delete-fundraising-emails?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

作者用一个小型 ML 项目验证 Jev 能否过滤收件箱中的政治筹款与倡议邮件，随后比较开源模型、探索置信度过滤，并用 SetFit + ONNX 构建可本地 CPU 运行的 23.4 MB 分类器。结论是 Jev 对该任务足够好，但更小的本地方案也可行，前提是认真构建评估、验证阈值并暴露剩余错误。

- 🎯 真正用例不是“通用邮件 AI”，而是过滤政治筹款与政治倡议；作者先定义政治/非政治政策，避免把模型错误与产品分歧混为一谈。
- 📩 政策将筹款、招募志愿者、推广候选人或政党、政治请愿/调查、动员政策支持归为政治；无倡议新闻、中性投票服务、商业/个人邮件、非政治慈善归为非政治。
- 🧪 初始评估使用 100 封真实邮件，50 政治/50 非政治，一半来自收件箱，一半来自公开来源；标签经助手复核，并非人工裁定。
- ✅ Jev 通过 OpenRouter Decisions API 的 noul 概率判断，初始成绩为 99/100 正确，政治邮件漏判 0/50，非政治误判 1/50，ECE-10 为 0.0477；首个 100 封运行报告 API 成本约 $0.0028。
- 🔍 作者用硬负例与漏判正例挖掘更难样本，并通过 TF-IDF/关键词寻找候选；强调大语料只是搜索空间，不是自动评估集。
- ⚠️ 在 23 个预留挑战样本上，Jev 得 19/23，远低于初始 99/100；该结果只衡量刻意挑选的边界案例。
- 🖥️ 为隐私与本地推理，作者在 112 封合成评估集上比较开源模型：Winnow 12B 与 Jev 同为 109/112，且在准确率并列的开源模型中校准最好（ECE 0.0172）；JPT 9B 为 108/112，ECE 0.0169，速度/成本折中。
- 📊 成本与延迟：Winnow 12B 为 106.7 ms/封、$0.1136/千封；JPT 9B 为 57.2 ms/封、$0.0620/千封；JPT 0.8B 为 41.5 ms/封、$0.0332/千封；Jev 中位 201.1 ms/批、$0.0428/千封。
- 🎚️ 置信度过滤必须同时报告接受准确率与覆盖率：Jev 阈值约 0.72 时接受 108/112、准确率 99.07%；Winnow 阈值约 0.9666 时接受 103/112、99.03%；JPT 9B 阈值约 0.9405 时接受 82/112、100%；JPT 0.8B 阈值约 0.98 时接受 52/112、100%。
- 🧱 小模型方案：用 23M 参数的 MongoDB/mdbr-leaf-mt 嵌入 + SetFit 训练；训练集 120 封（54 政治、66 非政治），1 epoch、batch 16、20 iterations，产生 4800 对和 300 步。
- 🏆 SetFit 私有评估：初始 FP32 为 97/100，ECE 0.0351；加入 20 个硬例后 FP32 为 98/100，ECE 0.0219；ONNX INT8 仍为 98/100，但 ECE 变为 0.0271。
- 🧩 增强后的原生模型在预留挑战上只有 18/23，并漏掉其中两封政治邮件；公开合成 INT8 评估为 106/112，含 1 个假阳性、5 个漏判政治邮件。
- 📦 导出必须包含编码器、池化、投影和逻辑回归头；FP32 ONNX 约 92.0 MB，INT8 约 23.4 MB，低于 30 MB 目标。
- 🔬 动态量化会让概率对 batch size 敏感：123 封真实邮件在 batch 32 时有 1 个标签改变，batch 1/8 无变化；阈值不能直接从 FP32 复制到 INT8。
- 📬 邮件路由规则为 p_political ≥ 阈值则送入 Trash；在 112 封合成评估上，一个事后 INT8 阈值将 47 封政治中的 40 封、65 封非政治中的 0 封送入 Trash，但这不是独立验证的零误报承诺。
- 🧾 数据与复现：原始私有评估 100 封，训练增至 120，预留挑战 23；发现语料 13,477 行、6,390 行重复，关键词复审 152 个候选；公开版保留 440 封合成邮件，328 训练、112 评估。
- 🧰 版本：SetFit 1.2.0、PyTorch 2.8.0；推理用 ONNX Runtime 1.30.0、tokenizers 0.22.2、NumPy 2.4.6；原始评估虽冻结但开发中反复查看，阈值需在验证集选择并在新测试集上报告。
- 💡 结论：Jev 足以胜任政治邮件过滤，准确、校准好、便宜；真正价值还在于构建并挑战评估，从而支撑本地、小体积、可解释的部署决策。

---

### [](https://blog.python.org/2026/09/language-summit-2026-rust-for-cpython/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Rust for CPython (Python Language Summit 2026) | Python Insider](https://blog.python.org/2026/09/language-summit-2026-rust-for-cpython/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

本文介绍 Python 语言峰会上 Rust for CPython 项目的最新进展：David Hewitt 代表约 60 人团队，提出将 Rust 渐进引入 CPython 的路线图、以 zlib 为首个可选 Rust 模块，并讨论成功标准、平台与依赖挑战，以及核心开发者的反馈。

- 🦀 David Hewitt 以“大使”身份汇报 Rust for CPython 项目，团队由核心开发者 Kirill Podoprigora 和 Emma Smith 领导，约 60 名开发者在 Discord 协作，含少数 CPython 核心开发者与 Rust 项目代表。
- 📈 动机：CPython 的 type-crash 问题持续上升，新解析器、JIT、自由线程等大工程增加复杂性，Rust 可帮助“快速行动并修复问题”，Android 经验显示补丁修订更少。
- 🔗 生态已有 PyO3 和 Maturin 连接 Rust 与 Python，许多公司把 Rust 视为长期技术押注，而非一时潮流。
- ⚠️ 主要顾虑包括 Rust 平台支持、核心开发者 Rust 知识不普及、社交与技术双重挑战；方案是增量移植小部分代码，不追求一次重写百万行 C。
- 🧪 团队强调 Rust 不等于无 bug，仍需属性测试、模糊测试和审慎工程实践来保证正确性。
- 🗓️ 路线图：2026 夏季完成构建系统/CI 与 Rust API 概念验证；2026 年底 PEP 定义成功标准；Python 3.16（2027 年 10 月）提供可选 Rust zlib 后端和私有 Rust API；3.17（2028 年 10 月）解决平台问题并扩展到 io、json、xml、memoryview、parser；3.18+（2029 年 10 月后）可能要求 Rust 构建并发布公开 Rust API。
- 📦 首个目标模块是 zlib，采用 zlib-rs；它被 Firefox、uv、Cargo 等项目大量测试使用，在许多平台快于 zlib 和 zlib-ng，且能验证外部 Cargo 包构建流程。
- 🚀 若被接受，Python 3.16 中几乎每次 pip install 都可能因 zlib 加速而变快。
- 🧩 Rust API 草案使用 #[pyfunction]、Python<'_>、Py<...> 和 Result 错误处理，风格类似 Argument Clinic，并利用作用域退出自动清理资源。
- ✅ 成功标准建议：多数活跃核心开发者对使用 Rust API 持开放态度；CPython 性能基准无显著下降；所有分层平台获 Rust 支持；发行版构建 CPython 的体验表明加入 Rust 可管理。
- 🗣️ 讨论中 Thomas Wouters 建议不要为迁就 C API 老用户而妥协，应从第一性原理设计 Rust API，同时兼顾核心开发者受众。
- 🧭 Larry Hastings 问为何不直接重写或做分支；David 回应 RustPython 已存在但性能不如 CPython，可借鉴其 API 设计；并非所有 CPython 都要用 Rust，项目将长期双语言，但 Rust 不会永远可选。
- 📉 Pablo Galindo Salgado 担心 Cargo 依赖与漏洞响应成为“showstopper”；David 表示应尽量少依赖，zlib-rs 仅一个依赖，源码可 vendoring，构建 CPython 不需 Cargo，且不放在 CPython 树内。
- 🗂️ Łukasz Langa 与 Thomas 提到依赖可放 cpython-source-deps 仓库，但这是该仓库的新用途，目前它只用于 CPython 二进制安装器。

---

### [Python 3.15 有多快？ - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/how-fast-is-python-3-15?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [
  
    How fast is Python 3.15? - miguelgrinberg.com
  
](https://blog.miguelgrinberg.com/post/how-fast-is-python-3-15?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Miguel Grinberg 对 Python 3.15（3.15.0rc3）进行了非正式基准测试，与 Python 3.10–3.15、PyPy 3.12、Node.js 26.3 和 Rust 1.97 对比，覆盖递归斐波那契、冒泡排序、单线程/4 线程、标准/JIT/自由线程模式。总体结论：3.15 相比 3.14 性能提升很小，JIT 改进明显但仍属实验性；自由线程多线程收益大，生产中不必急于升级。

- 🧪 基准使用 fibo.py（递归斐波那契）和 bubble.py（冒泡排序），运行三次取平均，在 Linux/Intel i5/Gentoo 上测试，不覆盖 I/O 密集场景。
- 🐍 标准 CPython：3.15 单线程仅略快于 3.14（fibo 约 1.03x，bubble 约 1.04x），多线程下甚至略慢，整体基本持平。
- ⚡ JIT 是 3.15 最大亮点：JIT 版比同版本标准解释器快约 1.20x（fibo 单线程）和 1.28x（bubble 单线程），也优于早期 JIT。
- 🧵 自由线程在 4 线程测试中收益明显：fibo 比标准解释器快约 4.5x，bubble 快约 1.74x；但单线程下仍有性能损失。
- 🏎️ 横向对比：PyPy 在单线程 fibo 中约为 3.15 的 5.5x；bubble 中 Node.js 领先；Rust 仍最快，单线程 fibo 约 77x、bubble 约 50x。
- 📈 近年显著性能提升主要来自 Python 3.11 和 3.14；其他版本多为小幅改进或个别回退。
- 🧭 作者结论：3.15 不是必须升级的性能版本，JIT 仍实验性，不建议生产使用；可能为惰性导入、推导式解包等新特性升级。
- 🗓️ 作者计划日常使用 3.15，但生产项目可继续留在 3.14，甚至观望到 3.16。

---

### [](https://magazine.sebastianraschka.com/p/classifier-history-and-jev?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Language Models for Text Classification: From Bag-of-Words to Jev](https://magazine.sebastianraschka.com/p/classifier-history-and-jev?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

本文梳理文本分类从词袋模型、RNN/CNN 到 Transformer 的演进，并重点分析 Jev 的 API、性能、校准方法与使用场景。作者认为 Jev 本质上仍是分类器，但其廉价、快速、跨任务开箱即用的特点，使其成为分类领域的“ChatGPT 时刻”，并可能改变专用模型微调与智能体系统的成本结构。
- 🧺 词袋模型把文本转成固定长度词频向量，适合朴素贝叶斯、逻辑回归、XGBoost；IMDb 上逻辑回归约 89.9% 准确率，但完全丢失词序。
- 🧠 词嵌入把单词表示为稠密向量，Word2Vec、GloVe 等方法可用；经典嵌入在查询时与上下文无关，例如“bank”在“河岸”和“银行”中向量相同。
- 🔁 RNN/LSTM/GRU 按顺序读取文本，能保留词序，但训练困难且必须串行处理；IMDb 上 LSTM 约 85.66%，ULMFiT 预训练后微调可达 95.4%。
- 🖼️ CNN 可用卷积滤波器扫描相邻词嵌入，计算可并行；作者实验中文本 CNN 在 IMDb 上约 90.07%。
- ⚡ 2017 年 Transformer 成为主流；编码器式 BERT/ModernBERT 天然适合分类，ModernBERT 在 IMDb 上约 95%，且只需少量微调。
- 🤖 解码器式 GPT 模型既可直接提示分类，也可替换输出层为分类头；GPT-2 124M 在 IMDb 上约 92%。
- 🔄 编码器 - 解码器 T5 既可加分类头，也可训练成文本到文本分类，直接输出类别标签。
- 🆕 Jev 由 TypeSafe AI 推出，是专有模型，主打在决策任务上接近 GPT-5.6 Luna，但速度快、成本低几个数量级。
- 🧩 Jev 提供三类 API：Choice 用于多分类，Noul 用于二分类/多标签概率，Score 用于有序评分。
- 🎬 在 IMDb 25,000 条测试集上，Choice 准确率 96.47%，Noul 为 96.20%；运行约 22–23 分钟，成本约 0.65 美元。
- ⚖️ 与 ModernBERT 相比，Jev 精度相近且无需微调；ModernBERT 微调约 23 分钟、评估约 7 分钟，但只擅长特定任务。
- 🧪 Jev 强调概率校准，返回 confidence 与各类别概率，适合需要可靠置信度的生产应用。
- 🏗️ 可在 BERT、GPT、T5 上添加 Jev 式 API：每个候选类别生成表征，单节点打分头输出分数，再经 softmax 得到概率。
- 🧬 Jev 架构与训练数据未公开；作者猜测可能是小型 ModernBERT 类模型，训练数据为精心筛选的 100% 合成数据。
- 🎯 Jev 训练方法称 RLCD，即“用于校准决策的强化学习”；与 RLCR（带校准奖励的强化学习）思路相关。
- 📏 校准让预测概率贴近真实频率；温度缩放、Brier 损失、RLCR 可改善 ECE，但必须用留出数据验证是否真的有效。
- 💡 典型用例包括垃圾邮件/工单分类、实时游戏决策、LLM 智能体预筛选、提示注入检测、选择推理强度、挑选技能、评估裁判和检索相关文件。
- 🧵 Jev 发布后出现大量克隆，多基于 ModernBERT 或 Qwen 微调；多数无法达到 Jev 的跨任务广度，GLiNER 是较强相关项目。
- 🔒 对开源权重替代品的需求主要来自隐私，而非成本；作者期待 Jev 出现“DeepSeek 时刻”。
- 📉 读者测试显示：Contrastive Language Models 的 IMDb 准确率仅 82.90% 且 Tetris 失败；Laya 达 92.33%，但 Tetris 表现更差。
- 🚀 OpenAI 在 DevDay 2026 发布 Decision API，类似 Jev，直接集成到其平台。
- 🧭 结论：Jev 并非全新概念，但作为即插即用分类器跨任务表现突出，提高了专用微调的门槛，并可能让智能体系统更快、更便宜。

---

### [用 Python 从零构建并训练 GLM-5.3-Flash 模型 - YouTube](https://www.youtube.com/watch?v=-gfgQfw2g_E&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Build & Train a GLM-5.3-Flash Model From Scratch with Python - YouTube](https://www.youtube.com/watch?v=-gfgQfw2g_E&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

这是 YouTube 页面底部的导航与版权信息，涵盖平台介绍、商务合作、开发者资源、法律条款、隐私与安全、功能测试以及版权归属。

- ℹ️ 提供 About、Press、Copyright 等基础信息入口。
- 📬 包含 Contact us 联系方式与 Creators 创作者相关链接。
- 📈 提供 Advertise 广告合作及 Developers 开发者资源入口。
- ⚖️ 包含 Terms、Privacy、Policy & Safety 等法律与政策链接。
- ⚙️ 提供 How YouTube works 与 Test new features 说明及测试入口。
- ©️ 版权信息显示为 © 2026 Google LLC。

---

### [](https://adamj.eu/tech/2026/10/02/django-app-links/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Django: serve apple-app-site-association and assetlinks.json - Adam Johnson](https://adamj.eu/tech/2026/10/02/django-app-links/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

如果你的网站有配套的 Apple 或 Android App，可通过 Universal Links / App Links 让链接在已安装时打开 App；这需要在域名的 `/.well-known/` 下提供两个 JSON 文件，并满足平台验证要求。

- 🍎 Apple 文件 `apple-app-site-association` 用于 Universal Links、密码自动填充和 passkeys，其中 `applinks` 声明 `appIDs` 与 `components`，按顺序匹配，可排除 `/admin/*` 留在浏览器。
- 🤖 Android 文件 `assetlinks.json` 用 `relation` 声明 `handle_all_urls` 和 `get_login_creds`，并在 `target` 中填写包名与 `sha256_cert_fingerprints`。
- 📁 两个文件放在 Django 应用目录中；Apple 文件 URL 不带 `.json`，但本地保存为 `apple-app-site-association.json`，便于 `FileResponse` 识别为 JSON。
- 🔒 服务要求：必须 HTTPS、返回 `200 OK` 且无重定向、`Content-Type` 为 `application/json`，并且每个域名都要单独提供文件。
- 🧩 Django 视图使用 `FileResponse` 返回文件，并配合 `@login_not_required`、`@require_safe`、`@cache_control(max_age=300, public=True)`。
- 🗺️ 在根 URLconf 中将 `/.well-known/apple-app-site-association` 和 `/.well-known/assetlinks.json` 映射到对应视图。
- 🧪 测试应检查 `200`、`content-type`、`cache-control`、JSON 可解析及 App ID / 包名；`HEAD` 应成功，`POST` 应返回 `405`。
- 🛡️ 测试很重要，因为这些文件出错会静默失败：链接继续在浏览器打开，通常没有任何错误提示。
- 🍏 生产环境可用 Apple CDN 检查：`curl https://app-site-association.cdn-apple.com/a/v1/example.com`，开发时可用 alternate mode 绕过 CDN。
- 🤖 Android 可用 Digital Asset Links API 或 Statement List Generator/Tester 检查，也可通过 `adb shell pm get-app-links` 和 `adb shell pm verify-app-links --re-verify` 重新验证。
- ✅ 总结：提供、测试并验证这两个小 JSON 文件，就能让链接在用户期望的 App 中打开，并支持登录凭据与 passkeys 关联。

---

### [获取失败](https://labs.quansight.org/blog/limited_api_numpy?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Failed to retrieve](https://labs.quansight.org/blog/limited_api_numpy?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

无法总结：获取内容失败，状态码 429。

---

### [面向 Python 工程师的 Jev - Vercel](https://vercel.com/blog/jev-for-python-engineers?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Jev for Python engineers - Vercel](https://vercel.com/blog/jev-for-python-engineers?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Jev 是一种新型 AI 模型，正被广泛用于交易决策、生成 UI 等场景；它接收数据和选择题，返回答案及置信度，速度快但也会犯错，是否足够准确取决于具体用例。Vercel 的 Python 团队发布 AI SDK for Python，让 Python 开发者更容易试用 Jev，并展示了分类与代码生成实验。

- 🚀 Jev 热度很高，几乎人人都在以各种方式尝试它，从交易决策到生成 UI。
- 🧩 Jev 是新型 AI 模型：输入数据和一组选择题，输出答案以及每个答案的置信度。
- 🎯 Jev 专为“窄决策”设计，会犯错但速度很快，准确度需要针对用例测试。
- 🐍 Vercel Python 团队发布最新版 AI SDK for Python，方便 Python 开发者试用 Jev。
- 📦 安装方式为 `uv add ai`，可使用实验性的 `evaluate()` API 直接调用 Jev。
- 🔑 使用前需创建 AI Gateway key，并设置 `AI_GATEWAY_API_KEY` 环境变量。
- 🧠 Jev 可理解为“通用分类器”：基于 LLM，但行为像分类器，便宜、快速，返回结构化 JSON，而非生成文本。
- 📋 官方 API 很简单，Python SDK 基本原样实现：只有一个 `evaluate()` 函数和少量类型，支持 `ChoiceQuestion`、`ScoreQuestion`、`NoulQuestion`。
- 🧪 示例 1：尝试用 Jev 判断 Python REPL 输入是英文还是 Python；作者自己训练分类器失败，Jev 表现更好，但仍会误判，如 `"what's" + " up` 被看成英文。
- 🧱 示例 2：尝试让 Jev 生成 Python 代码；直接逐字符或逐词生成效果差，最终改用 AST 方法。
- 🌳 AST 方法：先用 LLM 扩展用户提示，再让 Jev 逐步选择 AST 节点，宿主代码处理标点和缩进，最终生成语法有效但多数仍不正确的代码。
- 🧾 该代码生成实验源码已放在 GitHub，说明让分类器做 LLM 的写作工作仍很困难。
- 📣 尽管实验不完美，作者仍对 Jev 兴奋，鼓励用 AI SDK for Python 和 AI Gateway key 试用，并可让编码代理创建最小 Jev playground。

---

### [](https://blog.glazer.ee/posts/building-glazer-disposable-browser/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Orchestrating Disposable Browser · Glazer Blog](https://blog.glazer.ee/posts/building-glazer-disposable-browser/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Glazer Browser 将一次性浏览器做成容器化服务：用 Docker 隔离环境、Python 编排，并通过 sidecar 与 sandbox 的“就绪宣告”机制，在启动速度与稳定性之间取得平衡；最终将冷启动从 8–10 秒降至约 2 秒，并把耗时波动收窄到 1.9–2.1 秒。

- 🧭 背景：2025 年为解决大型组织中的影子 IT 与 OSINT 需求，构建 Glazer Browser，让用户低开销访问非受监管网络。
- 🧱 架构：核心是安全容器化环境，使用匿名网络网关，向用户流式传输桌面音视频，并接收鼠标键盘事件；编排层用 Python，虚拟化层选 Docker。
- ⚡ 问题：最初并行启动最快可达 1.5–2.5 秒，但依赖竞态条件，错误率高且难复现；迁移到顺序启动后稳定，却要 8–10 秒。
- 📣 解决思路：不再把“容器运行中”当作“容器已就绪”，而是让每个构建块在真正可用时向编排器宣告，例如 sidecar 输出 `SIDECAR_READY`。
- 🔄 sidecar 启动：先启动最慢的隧道，利用等待时间设置 DNS/路由、启动代理并确认监听，再等待隧道真正可承载流量，最后以代理进程维持容器生命周期。
- 📜 读取信号：通过 Docker 日志流读取就绪 token；使用绝对 `until` 时间戳、executor 线程、`threading.Event` 和 `contextvar request_id` 处理超时、取消与日志关联。
- 🧪 sandbox 就绪：sandbox 采用外部轮询 `pidof chromium`；sidecar 与 sandbox 共享单一 deadline，超时后先设停止标志并等待线程结束，避免泄漏 Docker 流和连接。
- 📊 结果：完全并行方案快但不稳定，顺序方案稳定但慢；声明就绪后冷启动约 4.5 秒，缓存 Tor 数据目录后约 2 秒，且稳定在 1.9–2.1 秒。
- 🔮 后续：将打开 sidecar 黑盒，介绍多种出口后端、数据目录缓存，以及容器在会话中途死亡时 fail-closed 的含义。

---

### [未找到标题](https://enjii.pages.dev/blog/Optimizations/vex_startup_time_optimization/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [No title found](https://enjii.pages.dev/blog/Optimizations/vex_startup_time_optimization/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

overview summary
本文介绍 VEX 智能体运行时如何优化冷启动与模块导入：通过短路工具函数、延迟/按需导入、TYPE_CHECKING 和避免常量级整模块导入，将工具函数启动降至约 400ms，主程序启动降至约 2.1–2.7s。

- 🚀 初始冷启动约 4 秒，对工具函数和主 vex 程序来说都太慢。
- 🧰 工具函数如 `--help`、`--ls`、`--reset` 只是快捷方式，应几乎立即完成；在 `run_agent` 中先检查并短路这些参数，再导入重型模块。
- 🔍 使用 `tuna` 和 `-X importtime` 分析模块导入耗时，定位启动瓶颈。
- 🧾 仅为类型注解而导入会加载整个模块；可用 `from __future__ import annotations` 与 `TYPE_CHECKING` 守卫，使运行时零额外开销。
- 📦 将重型导入移到函数内部，按需加载，例如在 `build_graph` 内导入 `langgraph` 相关模块；首次调用后模块会被缓存。
- ⏱️ 仅为 `END` 常量从 `langgraph.graph.state` 导入，竟消耗约 1.36 秒；改为直接定义 `END = "__end__"` 可省下该时间。
- 🔌 `MCPManager` 仅在 `CONFIG.toml` 中定义时导入，节省约 1 秒。
- 📉 优化结果：工具函数约 400ms；主程序无 MCP 工具约 2.1 秒；有 MCP 工具约 2.7 秒。
- 🔗 VEX shell 源码：https://codeberg.org/Enji/vex

---

### [](https://dev.arie.bovenberg.net/blog/pendulum-cursed-plus-operator/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Why Pendulum had to write the most cursed + operator in all of Python | Arie Bovenberg](https://dev.arie.bovenberg.net/blog/pendulum-cursed-plus-operator/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Pendulum 为同时实现“DST 感知算术”和“标准库 datetime 即插即用替代”这两个互相冲突的承诺，在 `+` 运算符中通过读取调用栈来猜测调用者意图，形成昂贵、脆弱且影响广泛的 hack。

- ⚙️ Pendulum 的 `DateTime` 继承 `datetime`，`Duration` 继承 `timedelta`，`Timezone` 继承 `ZoneInfo`，因此现有代码可无缝接收这些子类。
- ⏱️ 它承诺 DST 感知算术：跨夏令时转换时按实际流逝时间计算，而标准库 `+` 按墙上时钟计算，两者结果可能相差一小时。
- 🧩 冲突核心：标准库的 `datetime.astimezone()` 内部会通过 `ZoneInfo.fromutc()` 调用 `+`，并期望墙上时钟语义；但 Pendulum 覆写的 `+` 会给出 DST 感知结果。
- 🪤 Pendulum 3.2.0 的 `__add__` 用 `traceback.extract_stack` 检查调用者名称：若调用者叫 `astimezone`，就用标准库的 `super().__add__()`，否则用自身的 `_add_timedelta_()`。
- 🧪 这导致函数名能改变结果：定义一个名为 `astimezone` 的函数，再给 Pendulum 时间加 24 小时，会得到不同答案。
- 🐢 调用栈检查非常昂贵：`+` 比标准库慢约 600 倍，因为要 `stat()` 源文件并读取源码行；在日历、循环事件、日志分桶等场景中成本会累积。
- ⚠️ 猜测很脆弱：转换到 dateutil 时区会走不同调用栈并出错；在 PyPy 上，Pendulum 自身的时区转换也可能偏差一小时。
- 🔍 Pendulum 还在别处猜测：无时区时 `parse()`/`instance()` 假定 UTC；`parse("12:00")` 使用今天日期；对 DST 跳过的墙上时间，`fold` 的解释与标准库相反。
- 🧨 猜测带来四类问题：把“未知”包装成“确定”；结果依赖当前时间、机器时区、函数名等未明示因素；无法覆盖所有调用者；一旦发布就难以撤回，否则会静默改变现有程序结果。
- ✅ 针对 `+` 的修复：让 `astimezone()` 先把普通 `datetime` 交给标准库转换，再包装回 Pendulum 类型；该 PR 已被合并，下一版可移除 `__add__` 的猜测和相关 bug。
- 🚀 修复后 `+` 从约 600 倍慢降到约 120 倍慢；剩余开销来自 Pendulum 纯 Python 实现的算术本身。
- 🧱 根本冲突仍未解决：只要 Pendulum 仍是 `datetime` 子类并改变 `+` 行为，外部代码把 Pendulum 值当作 `datetime` 使用时，仍会得到 Pendulum 的语义。
- 📌 现有用户需注意：第三方时区转换、PyPy、热循环中的 `+`、不可信或不完整字符串解析，以及把 Pendulum 值传给期望 `datetime` 的 API。
- 🧭 新项目可选择标准库 `datetime`，或选择不继承 `datetime` 的类型安全库如 `whenever`，后者让 naive 与 aware 不能混用，也不会静默猜测。

---

### [博客 - 在 NumPy 2.5 中让](https://blog.scientific-python.org/numpy/searchsorted/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Blog - Making np.searchsorted up to 25× Faster in NumPy 2.5](https://blog.scientific-python.org/numpy/searchsorted/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

这篇文章介绍 NumPy 2.5 对 `np.searchsorted` 的优化：通过批处理/向量化二分搜索、固定迭代次数、减少每查询状态并移植到 C++，在基准测试中实现最高 25 倍加速，同时降低额外内存占用并保持生态竞争力。

- 🧠 `np.searchsorted` 是 NumPy 的二分搜索实现，用于直方图、区间查找等场景，优化将惠及 SciPy、scikit-learn 及更广泛的科学计算生态。
- 🚀 核心思路是把多个独立搜索批量向量化，让所有查询在 NumPy 编译循环中同步推进，减少 Python 开销并隐藏内存延迟。
- 🧩 初版向量化维护 `lo`/`hi` 和 `active` 掩码；改为固定迭代次数、所有区间同步收缩后，去掉 `active` 跟踪可提速至多 2 倍。
- 📐 进一步只用单个 `base` 数组和全局 `length` 表示所有查询区间，输出仍需 O(K) 空间，但额外状态降至 O(1)。
- 💻 该算法被移植到 NumPy C++ 实现，并利用首次迭代优化，通过 PR #30517 进入 NumPy 2.5。
- ⚡ 在 Apple M1 Pro、10,000 个查询键、数组最大到 2^30 的基准中，NumPy 2.5 比 NumPy 2.4 最高快 25 倍。
- 🏎️ 向量化 Python 版本可超过 NumPy 2.4；C++ 版本在较小数组上还可比 Python 向量化版快最多 2 倍，并减少内存占用。
- 🔍 NumPy 2.4 对每个键独立顺序搜索，存在依赖链和缓存不友好问题；批处理让多个内存访问可同时在途，缓解缓存未命中影响。
- 🌐 生态对比中，JAX/NumPy 采用批处理向量化，TensorFlow/PyTorch 采用多线程并行；基准显示 NumPy 有竞争力，数组超过 CPU 缓存后趋势相似。
- 🧵 禁用多线程后，PyTorch 和 TensorFlow 性能下降，接近 NumPy 2.4 的表现，说明内存访问成本成为主导。
- 🔮 后续方向包括 Eytzinger 等缓存友好布局、在线程内结合批处理二分搜索，以及探索 array API 是否可暴露 `layout="eytzinger"` 之类接口。
- ✅ 结论：用 NumPy 数组原语即可先写出超越旧原生实现的 Python 版本，说明向量化利用独立工作的能力非常强大。

---

### [](https://www.youtube.com/watch?v=H5o1P8RMiMw&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Build Your Own Agentic Harness in Python - Full Tutorial - YouTube](https://www.youtube.com/watch?v=H5o1P8RMiMw&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

该内容主要是 YouTube 页面底部的导航与法律信息，汇总平台介绍、合作资源、政策条款、功能说明及版权声明。

- ℹ️ 包含“关于”“新闻”“版权”“联系我们”等基础信息入口。
- 🎬 提供创作者、广告主和开发者相关资源链接。
- 📜 涵盖服务条款、隐私政策以及政策与安全说明。
- ⚙️ 包含 YouTube 运作方式介绍和测试新功能入口。
- ©️ 版权归属标注为 © 2026 Google LLC。

---

### [](https://triangulatedexistence.mataroa.blog/blog/making-a-mathematical-model-for-better-indic-keyboards/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Making a mathematical model for better Indic keyboards — triangulatedexistence](https://triangulatedexistence.mataroa.blog/blog/making-a-mathematical-model-for-better-indic-keyboards/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

作者把泰米尔文等印度系文字的书写结构映射为布尔逻辑与查找表，目标是做出类似日本 12 键假名键盘的连续触屏输入方案；以泰米尔文为第一个完整实现，并公开网页、SymPy 与 TypeScript 代码。

- 🎯 目标是为每种印度文字设计更好的键盘，灵感来自 12 键假名键盘，并把文字结构对应到键盘结构。
- 🧠 项目起点是作者半睡半醒时的构想：先画布尔电路，再在 Reddit 邀人研究，虽无人加入，但 10 个月后完成模型。
- 📚 第一步整理泰米尔辅音表，按发音部位（软腭、硬腭、卷舌、齿、唇、齿龈）和类别（Vallinam、Mellinam、Idaiyinam、Sibilants/Grantha）分类。
- 🔤 泰米尔元音表分基础元音、对比性单元音、双元音；扩展字符还包括 Pulli、Ayatam、ZWNJ，以及 Grantha 的 ஜ、ஹ、க்ஷ。
- 🧮 第二步建立粗粒度真值表：输入 CoarsePosition，输出 CoarseValidity，用 C_I1/C_I0/C_S 表示 Idaiyinam 的三种有效性与 Sibilants 有效性。
- 🔣 第三步建立细粒度真值表：输入 FineFeatures（V、M、I1、I0、S），输出 FinePosition（D2、D1、D0）；Idaiyinam 用 00/01/11，CoarseValidity 用 00/01/10 属开发者约定。
- 🖥️ 用 SymPy 将真值表转为最小化布尔表达式，例如 C_I1=(c0&c2)|(c1&~c0)、C_I0=~c1&Xor(c0,c2)、C_S=c0^c1，并求出 D 表达式与 Invalid 有效性谓词。
- 💻 第四步用 TypeScript 实现 evalD(alpha, world)，区分 NormalWorld 与 ExtendedWorld，处理普通字符和 Grantha 扩展字符，输出位标志。
- 🗂️ 第五步使用数组查找表 CONSONANT_LOOKUP_TABLE，按 4 位编码返回泰米尔辅音、INVALID 或 undefined；作者称该写法高度优化，适合嵌入式系统。
- 📝 第六步说明输入编码：CoarsePosition 如软腭 000、硬腭 001、……、齿龈 101；FineFeatures 如 Vallinam 00001、Mellinam 00010、Idaiyinam 00100/01100、Sibilant 10000。
- 🔗 文中提供可试用网页、SymPy 粗粒度与细粒度代码、TypeScript 代码的 GitHub 链接，便于复现和扩展。
- 🚀 总体而言，这是把 Panini 音系学/印度文字结构映射到数字逻辑与连续触屏输入的一次完整框架尝试，先覆盖泰米尔文，后续将扩展到更多印度文字。

---

### [Python 内存管理入门 | Daniel 的技术博客](https://tech.daniellbastos.com.br/posts/python-memory-management/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [First Steps into Memory Management in Python | Daniel's Tech Blog](https://tech.daniellbastos.com.br/posts/python-memory-management/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

作者因一场关于强引用、弱引用和垃圾回收的演讲，开始深入理解 Python/CPython 3.12 的内存分配与释放机制。核心结论是：Python 会管理内存池以减少系统调用，但对象释放后不一定把内存归还给操作系统；开发者能更多控制的是引用生命周期。

- 🧠 分配策略取决于对象大小：≤512 字节的小对象用 `pymalloc`，更大的对象用系统的 `malloc`/`PyMem_RawMalloc`。
- 📦 `pymalloc` 会向操作系统申请 arena；每个 arena 分成 64 个 pool，每个 pool 再分成相同大小的 block。
- 🧩 小对象存放在 pool 中的空闲 block 里；只有当现有 arena 没有合适空间时，才会向操作系统申请新 arena。
- 🪣 arena 只有在其所有 pool 都为空时才会归还操作系统；单独释放一个 block 通常只是留给之后复用。
- ⏳ 因此 Python 进程很少缩小：哪怕只有一个存活对象，也可能让整个 arena 无法归还给操作系统。
- 🗃️ 大对象由系统 C 库的 `malloc` 处理，没有 arena/pool 结构；释放后通常也会被保留复用，只有超大块才直接还给操作系统。
- ♻️ 释放内存有两种机制：引用计数和垃圾回收。
- 🔢 引用计数很直接：变量只是指向对象的名称；引用计数归零时，对象立即销毁，block 回到 pool 的空闲列表。
- 🔄 垃圾回收负责引用计数无法处理的循环引用：不可达的容器对象会被回收。
- 🌱 垃圾回收按代进行：新对象在 gen0，检查频繁；幸存对象晋升到更老的代，检查频率降低。
- 💡 关键洞察：你无法完全控制已释放内存是否归还给操作系统，但可以通过 `del`、减少长期引用、或把对象直接传给下一次调用等方式控制引用存活时间。
- 🚀 作者认为研究 Python 内部机制是一段愉快的冒险，并会继续通向操作系统内存、自由线程、解释器执行等更深主题。

---

### [获取失败](https://www.scylladb.com/2026/09/28/building-a-faster-rust-based-python-driver/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Failed to retrieve](https://www.scylladb.com/2026/09/28/building-a-faster-rust-based-python-driver/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

无法总结：获取内容失败，状态码 403。

---

### [](https://devblogs.microsoft.com/foundry-on-windows/build-on-winml-oct-7-26/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [AI Development on Windows: from PyTorch and llama.cpp to Windows ML - Microsoft Foundry on Windows Blog](https://devblogs.microsoft.com/foundry-on-windows/build-on-winml-oct-7-26/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

微软发布 Windows 本地 AI 开发更新，核心是将 llama.cpp/GGUF 实验性引入 Windows ML，并扩展 PyTorch、Triton 与 Windows on Arm 支持，形成从模型实验、训练优化到本地部署的完整路径。

- 🚀 Windows ML 新增实验性 llama.cpp 支持，可本地运行 Hugging Face 上的 GGUF 模型，只需少量代码。
- 🧩 提供任务专用 API：Text Generation API 支持 GGUF/ONNX 文本生成，Speech Recognition API 可用 ONNX Whisper 转写音频，且两者可组合。
- 🔌 这些 API 暴露 OpenAI 兼容端点，开发者可用现有 OpenAI SDK 连接本地 Windows ML 服务器进行原型开发。
- ⚙️ 推出实验性 Windows ML Runtime API 预览，支持 Windows 原生数据类型、零拷贝输入、多模型确定性流水线和模型提前编译。
- 🧱 Runtime API 与 ONNX Runtime API 并存，高层 Text Generation 和 Speech Recognition API 构建在其上，便于逐步采用原生优化路径。
- 🤝 与 NVIDIA 及社区合作改进 llama.cpp：CUDA 内核优化、内核融合、CPU-GPU 调度、权重重打包、CUDA graphs、推测解码、多 GPU、NVFP4 等。
- 🐍 PyTorch 提供官方 Windows Arm64 CPU 原生构建，NVIDIA 提供 CUDA Windows Arm64 包，支持 Arm Windows AI 设备上的训练、微调和推理。
- ⚡ Triton for Windows 带来 triton.jit、torch.compile 和自定义 GPU 内核；PyTorch Inductor 可生成优化 Triton 内核以提升性能。
- 🔄 完整生命周期示例：用 PyTorch + Triton 训练/优化模型，导出 ONNX，再用 Windows ML CLI 分析、构建和基准测试。
- 🧰 Windows ML CLI 支持转换、优化、量化、编译和基准测试，帮助开发者将模型准备为应用可用产物。
- 💻 新一代 NVIDIA RTX Spark Windows PC（如 Surface Laptop Ultra）增强本地 AI 算力，支持开源模型和本地智能体工作负载。
- 🌐 微软将继续与开源维护者、硬件伙伴及 Python/AI 社区合作，增加原生包、扩大内核覆盖、简化安装、提升性能并统一 x64 与 Arm64 支持。
- ⚠️ 新 Windows ML 能力仍为实验性，生产使用前需查看支持场景和已知限制。

---

### [](https://github.com/FeSens/openTPU?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - FeSens/openTPU: An open-source AI accelerator, developed by AI: RTL, ISA, simulator, compiler and profiler in one repo. Runs Qwen3, LFM2.5 and Qwen3.5 on a Kintex-7 PCIe card. · GitHub](https://github.com/FeSens/openTPU?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

openTPU 是由 AI 开发的开源 AI 加速器项目，采用单仓库组织，完整覆盖 RTL、ISA、位精确模拟器、编译器与 profiler，并可在 Kintex-7 PCIe 卡上运行 Qwen3、LFM2.5、Qwen3.5 等模型；它既探索 AI 代理能多大程度完成硬件设计，也作为从 Python matmul 到硬件连线的端到端学习项目。

- 🏗️ 项目在单一 monorepo 中提供 SystemVerilog 硬件、指令集、模拟器、内核语言与编译器、主机软件，便于端到端阅读。
- 📈 GitHub 数据：537 stars、36 forks、2 watchers、1,439 commits；Apache-2.0 许可证。
- 💳 目标硬件为 Inspur YPCB-00338 卡，搭载 Xilinx Kintex-7 xc7k480t，两个 DDR3 通道，通过 PCIe 连接主机。
- 🤖 可运行十种现代模型真实权重，包括 LFM2.5-230M、Qwen3-0.6B、Qwen3.5-0.8B/2B/4B、Gemma 4 E2B/E4B、LFM2-2.6B、SmolLM3-3B、Phi-4-mini。
- ✅ 卡上产生的 token 与模拟器逐位一致，MoE 模型也与模拟器逐位一致。
- ⚡ 性能示例：LFM2.5-230M int8 解码 59.0 tok/s(device)/52.3(wall)，prefill 295.6 tok/s；4-bit 达 85.8/82.1 tok/s。
- ⚡ Qwen3-0.6B int8 解码 21.6/21.3 tok/s，prefill 92.1 tok/s；Qwen3.5-0.8B int8 为 17.6/16.3 tok/s，prefill 61.4 tok/s。
- 📉 更大模型如 Phi-4-mini int8 解码 3.99 tok/s，SmolLM3-3B int8 5.00 tok/s，LFM2-2.6B int8 6.05 tok/s。
- 🔧 Build B 比早期版本快 8–9%，DRAM 利用率从 82–87% 提升到 91–94%。
- 🖼️ 生产镜像为 main e698dcd，133.33 MHz，单 bitstream 支持所有模型；含 LiteDRAM 控制器、四列 systolic 矩阵单元与 stream engine。
- 💾 DDR3-1066 峰值 17.1 GB/s；主机为 opentpu(Intel Core i7-4790)。
- 🧪 测试方法：decode 为 512-token prompt 后 64 个贪心 token，主机 argmax 在循环中；device 只计加速器周期，wall 加主机；prefill 为 512-token prompt。
- 🧮 Gemma 4 E2B 将逐层嵌入表放在卡上；E4B 的 2.95 GB 表留在主机，每 token 复制 11 KB 行到卡。
- 🧠 MoE 模型超过卡上 4 GiB 时，专家从主机存储流式传输；LFM2.5-8B-A1B 达 10.6 tok/s，Qwen3.5-35B-A3B 达 3.95 tok/s。
- 🔢 4-bit 权重使用 FP4 与两级块缩放，约 4.25 bits/权重，LM head 保持 int8；每 token 字节减少约三分之一，解码速度提升 40–45%。
- 🏎️ 主机几乎不成为瓶颈：LFM2/Qwen3 只编译一次 decode 程序，位置从寄存器读取，logits 流式返回；每 token 主机开销约 0.17–0.30 ms。
- 🧱 架构链路：ol 内核 -> 语言 + 编译器 -> ISA(每指令 8×32-bit) -> Python ISA 模拟器 <==> SystemVerilog RTL -> Vivado bitstream -> FPGA -> PCIe -> 主机工具。
- ⚙️ 机器设计简单：每周期发一条指令；DMA 搬数据、矩阵单元做 int8 权重乘法、向量单元做 fp32、量化器转回 int8；无 cache、无隐藏调度，所有数据移动都是指令。
- 🧰 工具：otpu-chat 聊天、otpu-smi 监控温度/功耗/DRAM/单元利用率、otpu-lens 记录并用 profiler 查看、otpu-selftest/otpu-diag 自检。
- 🧪 tools/validate.py 可与 Hugging Face CPU golden 对比 greedy token 与 logits，支持 ISA 模拟器、Verilator RTL 和真实卡；--against 要求两设备 token 相同且 logits 逐位一致。
- 📏 验证通过标准：top-1 一致率至少 80%，平均 KL 不超过 floor 的 3 倍；卡上 Qwen3-0.6B、LFM2.5-230M、Qwen3.5-0.8B 六次运行均与 ISA 模拟器逐位一致。
- 📚 推荐阅读入口：docs/isa.md、opentpu/kernels 与 docs/compiler.md、opentpu/isasim.py、rtl/top/otpu_top.sv、docs/board.md 及各模型文档。
- 🚧 下一步：提升 DRAM 效率最后几个百分点、改善时序余量与面积 (WNS +0.032 ns)、加速 prefill。
- 🤝 欢迎 issues 和 PR；多数工作只需 Python 与 Verilator，不一定需要 FPGA；ISA/模拟器/RTL 改动需保持 pytest 通过，性能声明需说明测量方式。
- 📜 许可证为 Apache License 2.0。

---

### [TurboPython - 一个 Python 到 C++ 编译器](https://tpy-lang.org/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [TurboPython - a Python-to-C++ compiler](https://tpy-lang.org/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

TurboPython（TPy）是一种通用静态类型语言，通过 C++ 将 Python 编译为原生二进制文件，结合 Python 语法与所有权模型，实现内存安全与可预测性能。

- 🐍 **语法兼容**：采用标准 Python 语法并支持类型注解，大多数编辑器、类型检查器和 linter 可直接使用
- ⚡ **原生编译**：编译为独立原生二进制文件，支持固定宽度整数、指针和 span，无 GIL 限制多线程
- ⏱ **性能与内存**：无垃圾回收器和自动引用计数，通过所有权与借用机制在编译时管理内存，可选 Rc 实现共享所有权
- 🛡 **内存安全**：所有权规则在程序运行前捕获释放后使用和别名错误
- 📦 **部署灵活**：可发布独立二进制文件、嵌入为 CPython 扩展，或通过@native 调用现有 C/C++ 代码
- ⚠️ **早期开发**：核心语言可编译运行真实程序，但部分常规 Python 结构仍被拒绝，标准库为子集，已知 bug 可能静默产生错误结果
- 🔧 **安装简便**：作为 PyPI 包`tpy-lang`安装，需 Python 3.12+ 和 C++23 编译器（GCC 13+ 或 Clang 19+），`tpy-lang[bundled]`选项自带编译器
- 🚫 **无 pip 包**：无法导入 numpy、requests 等 CPython 包，所有导入内容需一起编译，依赖需用 TurboPython 编写或移植
- 🔑 **所有权模型**：每个值有唯一所有者（函数帧、字段或容器），局部变量和参数仍可别名，持久存储拥有其值
- 🏷 **注解要求**：函数参数、返回类型和类字段必须注解，局部变量自动推断
- 🔢 **默认 int32**：裸整数默认为 32 位 int32，可选 int64/uint32 等宽度，int 为任意精度
- 📦 **值 vs 引用**：基本类型、元组和视图复制；类、list、dict、set 为引用类型
- 🔤 **str 上下文适配**：str 根据上下文为拥有字符串或借用视图，String 和 StrView 明确拼写
- 🔒 **静态非动态**：无 eval、猴子补丁或运行时__dict__修改，类型和结构在编译时固定
- 🧰 **核心类型**：TurboPython 自有类型（Own、int32、Span 等）位于 tpy 模块，可用`from tpy import *`导入
- 🤖 **AI 辅助**：`tpy --install-agent-docs docs`可生成 TurboPython 入门文档，帮助 AI 助手生成正确代码

---

### [](https://github.com/ymcrcat/rgpu?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - ymcrcat/rgpu: Keep Python on your laptop. Run PyTorch operations and hold tensors on a remote GPU, including from a Mac with no CUDA installation. · GitHub](https://github.com/ymcrcat/rgpu?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

rGPU 让 Python/PyTorch 留在本地，把 GPU 计算和张量放到远程 NVIDIA GPU 上运行，适合没有 CUDA 安装的 Mac 等客户端，并提供 PyTorch device 与 CUDA shim 两种集成方式。

- 🚀 仓库是 ymcrcat/rgpu，采用 Apache-2.0 许可证，约 33 stars、3 forks、1 watcher、210 commits。
- 🖥️ 核心目标：本地保留 Python，远程 GPU 执行 PyTorch 操作并持有 tensor。
- 🧭 两种路径：PyTorch device 通过 TCP 使用 `torch` 操作；CUDA shim 兼容现有 Linux CUDA 程序及 stock CUDA PyTorch。
- 🔧 CUDA shim 覆盖 `libcuda`、CUDA Runtime、cuBLAS、cuBLASLt、cuDNN 等接口。
- ⚡ 安装方式：`pip install rgpu`，或在检出目录中 `pip install -e ./python`。
- 🧪 快速示例：`torch.ones(4, device="rgpu")`，配合 `rgpu-run --host ... python smoke.py`，输出 `8.0`。
- 🔐 安全注意：协议不认证、不加密；`rgpu-opserver` 应保持 localhost 绑定并走 SSH；CUDA server 监听所有 IPv4，需用防火墙限制 9713 端口。
- 📚 产品文档位于 `website/`，包含 Quickstart、Training、nanoGPT、CUDA shim、Operations、Configuration、Performance、Troubleshooting。
- 🗂️ 仓库包含 `client/`、`server/`、`common/`、`python/`、`tests/`、`codegen/`、`website/`、`docs/`、`jax/`、`scripts/`、`skills/`。
- 🧬 `jax/` 是实验性 JAX 工作，不是受支持的产品路径。
- 🛠️ 开发命令包括 `./scripts/build_client.sh`、`python -m pytest python/tests`、`npm --prefix website run build`。
- 🏷️ 主题：apple-silicon、cuda、deep-learning、gpu、gpu-computing、machine-learning、ml、pytorch、remote-gpu。

---

### [](https://github.com/RuleFlow-OSS/RuleFlow?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - RuleFlow-OSS/RuleFlow: A Python research framework and terminal-based IDE (RuleFlow Studio) for modeling, evolving, and analyzing discrete complex systems like ECA and SSS. · GitHub](https://github.com/RuleFlow-OSS/RuleFlow?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

RuleFlow 是一个 Python 研究框架与基于终端的 IDE（RuleFlow Studio），用于建模、演化并严格分析 ECA、SSS 等离散复杂系统；最初为 Southern Adventist University 的 Sequential Substitution Systems 研究而开发，后已泛化，采用 MIT 许可。

- 🧩 将系统更新视为原子计算事件（Cell、DeltaCell、Event），而非批量数组操作，从而保留操作谱系、碰撞动力学与空间因果链。
- 🔗 可提取显式因果 DAG、测量到创建事件的因果距离、追踪多路宇宙分支历史，并研究相对论计算边界。
- 🧠 提供通用因果分析引擎，记录被销毁/创建的空间量子，支持度同配、网络密度、流层级、最长 DAG 路径等指标，无需重新模拟系统。
- ✍️ 内置 FlowLang DSL，支持替换 `->`、覆盖 `-->`、插入 `>`、删除 `><`，减少数组切片与正则样板代码。
- ⚙️ FlowLang 包含 `@init`、`@evolve`、`@regress`、`@merge`、`@compress`、`@macro` 等指令，以及 `-pl`、`-bl`、`-cmp`、`-crp`、`-p_rule`、`-p_space` 等规则标志。
- 🌌 原生支持非确定性分支与多宇宙探索，通过 `parent_delta` 和坐标查找回溯源系。
- 🐍 支持引导式动态脚本：在 `.pflow` 中使用 Python，在 `.wpflow` 中使用 Wolfram Language 动态生成规则集。
- 🖥️ RuleFlow Studio 是基于 Textual 的模块化终端 IDE，采用 MVC 架构，支持实时可视化、悬停查看单元格、交互式因果图（PyVis/VisJS）与插件系统。
- 🧪 Studio 功能包括工作区变体、实时执行与热重载、图检查器、系统枚举和自定义插件开发。
- 📦 核心架构分层为 `core`、`lang`、`analysis`、`studio`、`tests`，分离内存/执行与高层语法评估。
- 📊 因果图可通过 `EventCausalityGraph` 构建为 NetworkX `MultiDiGraph`，并导出 Gephi、GraphML、GML、Graph6/Sparse6 等格式。
- 🏫 公开仓库使用 MIT 许可，当前约 12 stars、1 fork、207 commits，主题涵盖因果图、细胞自动机、演化系统、终端 IDE 等。

---

### [](https://github.com/AlexBrence/WagtailRocket?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - AlexBrence/WagtailRocket: A Wagtail boilerplate to save tens of hours of work · GitHub](https://github.com/AlexBrence/WagtailRocket?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

WagtailRocket 是一个基于 Wagtail 的 CMS 网站样板项目，旨在节省数十小时的重复开发工作，适合快速搭建内容管理网站，并提供演示、开发与生产部署说明、丰富的后台功能以及 Docker 支持。

- 🚀 项目定位：Wagtail 样板项目，帮助开发者节省大量重复开发时间。
- ⭐ 仓库数据：4 个 Star、1 个 Fork、0 个 Watcher、3 次提交，主要代码位于 src/。
- 💡 诞生背景：作者因摩托车商店使用 WordPress 时修改设置困难、插件拖慢速度，转而用 Wagtail 开发并抽离成样板。
- 📸 演示案例：提供摩托车商店真实案例，另有另一个示例可供参考。
- ⚙️ 开发安装：克隆仓库、创建虚拟环境、安装依赖、配置 .env、迁移数据库、创建超级用户并运行服务器。
- 🐳 生产部署：服务器克隆项目、配置 .env、替换 CHANGE_ME、执行 docker compose up -d、获取证书并重启 Nginx。
- 🔄 更新技巧：仅 Django 代码或模板变更时用 pkill -HUP；静态文件变更需 collectstatic；迁移需重启 web。
- 🛠 后台功能：可在管理面板控制货币、导航菜单顺序、首页外观、营业时间、联系方式、社交链接和自定义页面等。
- 🛍 商品功能：商品列表页自带分页、模糊搜索、排序、分类与子分类；详情页支持多图，并随机展示 3 个商品。
- 📝 博客与交互：博客列表页自带分页和分类，使用 HTMX 加快页面刷新。
- 🧩 首页搭建：可在后台用轮播、卡片等组件组合首页，并推广商品或链接到外部网站。
- 📄 内容扩展：产品描述支持 RichText 和附件；基础列表页与详情页类便于扩展。
- 🧰 技术栈：Python、Wagtail、PostgreSQL/SQLite、Nginx、Docker、Gunicorn、Bootstrap、HTMX。
- 🚀 部署优势：借助 Docker 可在几分钟内完成部署。

---

### [](https://github.com/sepandhaghighi/pixora?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - sepandhaghighi/pixora: Pixora: A Python Library for Pixel Art Conversion · GitHub](https://github.com/sepandhaghighi/pixora?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Pixora 是一个基于 Pillow 的轻量级 Python 库和命令行工具，可将普通图片转换为复古像素艺术，支持自定义像素大小、文件路径和内存对象，适用于游戏素材、像素头像和怀旧视觉效果。

- 🐍 基于 Pillow，提供简单 API，用于将图片像素化。
- 🎨 支持自定义 `pixel_size`，可处理文件路径或内存对象。
- 💻 提供 CLI：`pixora input.png output.png`，支持 `--pixel-size`、`--algorithm`、`--grayscale`。
- 🧩 内置算法：NearestNeighbor、Bilinear、Bicubic、Lanczos、MeanBlock、ModeBlock、MedianBlock。
- 📦 安装方式：`pip install pixora==0.4`，或从源码 `pip install .`。
- 📊 仓库状态：29 stars、1 fork、38 commits；4 个 issues、1 个 PR。
- 📜 许可证：MIT License，并有行为准则、贡献指南和安全政策。
- 🐞 问题反馈：可提交 issue 并描述问题，需按模板填写。
- ⭐ 支持项目：可给仓库点星，或通过 Bitcoin、Ethereum 等多种加密货币捐赠。
- 🏷️ 主题标签：art、convert、converter、pixel、pixel-art、pixelart、python、python-library 等。

---

### [](https://github.com/neurosymbolica/clausal-prolog?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - neurosymbolica/clausal-prolog: A Neurosymbolic Prolog built on Python · GitHub](https://github.com/neurosymbolica/clausal-prolog?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Clausal Prolog（clausal-prolog）是一个基于 Python 的神经符号 Prolog 系统，目标是把神经网络与符号推理放进同一个 Python 进程，结合二者的优势：可解释、可靠、数据高效、可修正。它支持 ISO Prolog 风格逻辑编程、约束求解、tabling、DCG 和 Python 互操作，并通过 `.clausal`、`.pl`、`.seam` 三种源文件表面组织代码。

- 🧠 项目定位：用 Python 实现的神经符号 Prolog，神经网络可直接调用符号逻辑，反之亦然，无需序列化、IPC 或第二运行时。
- ✅ 核心优势：结论可解释、硬约束可靠遵守、规则知识无需从样本学习、修改规则即可改变行为且无需重训练。
- 🧩 三种源码表面：`.clausal` 为默认的 Clausal Prolog（无 cut 的 ISO 语法）；`.pl` 为外部 ISO Prolog；`.seam` 为 Python 语法边界与适配器。
- 🔄 1.0 扩展名变更：`.clausal` 不再是 Python 语法 seam，而是 Clausal Prolog；旧 seam 文件需改为 `.seam`，否则会报 Prolog 语法错误。
- ⚙️ 主要特性：CLP(Z/B/Q/R)、`dif/2`、SLG tabling、well-founded semantics、DCG、`library(reif)`、ISO 内置名与错误项、模块系统。
- 🚫 设计限制：拒绝 cut、`->`、`*->`；推荐 `dif/2`、`if_/3`、约束和首参索引；`once/1`、`\+`、`forall/2` 被视为过渡构造。
- 🔒 模块与依赖规则：`.clausal` 文件通常必须以 `:- end_module(Name).` 结尾；`.clausal` 不能导入 `.pl`；Python 只能通过 seam 或允许的 bridge 访问。
- 🐍 Python 互操作：`.seam` 文件可使用 `++expr`、宿主 Python 语句和适配器；可从 Python 导入 `clausal` 并通过 `for ... in -- goal` 查询 Prolog。
- 🧮 示例能力：家庭关系、双向 `fib/2`、带环的 `path/2` tabling、SEND+MORE=MONEY 约束、DCG、reified if 和 `dif` 测试。
- 🧪 测试方式：模块内联 `test/1`，或 `test/2` 配合 `fail`；可用 `python -m clausal.testing` 或 pytest 自动收集 `.seam`、`.clausal`、`.pl` 测试。
- 📦 安装要求：`pip install clausal`；需要 Python ≥ 3.13、`greenlet`，以及 C 编译器（源码构建时）。
- 🔌 可选扩展包：`clausal-scipy`、`clausal-torch`、`clausal-jax`、`clausal-sklearn`、`clausal-spacy`、`clausal-sympy`、`clausal-opencv`、`clausal-yaml`、`clausal-acl2`、`clausal-decide` 等。
- 🧷 仓库信息：公开仓库，MIT 许可证；约 2 个 star、0 个 fork、0 个 watcher，主要包含文档、基准、测试、工具与实现计划。

---

### [](https://github.com/tradertanmay/ai-agents-zero-to-hero?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - tradertanmay/ai-agents-zero-to-hero: Learn AI agents from first principles to production. Zero mandatory dependencies, pure standard Python 3.11+, and no magic frameworks. · GitHub](https://github.com/tradertanmay/ai-agents-zero-to-hero?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

该仓库由 Tanmay Sah 创建，是一个公开可获取源码的 AI 代理教育框架，旨在以第一性原理、零强制依赖和纯标准 Python 3.11+，带读者从理解 LLM/API 进阶到能构建、调试、评估和生产化 AI 代理系统。

- 🧠 核心哲学：模型不等于代理；代理系统 = 模型/策略 + 运行时/控制循环 + 状态 + 工具，并与外部环境进行行动/观察交互。
- 🔁 核心循环：观察 → 决策 → 行动 → 再观察；模型负责选择或请求行动，执行层负责实际执行。
- 📊 操作谱系：从原始 LLM、聊天机器人、RAG、工作流、单次工具调用 LLM，到迭代自主代理和多代理系统。
- 🗂 关键区分：Prompt、Context、History、State、Memory 五类上下文/数据概念；Model、Tool、Environment、Runtime/Harness、Agent System 五个系统组件。
- 🎓 课程分 5 级递进：Level 1 Beginner、Level 2 Builder、Level 3 Systems、Level 4 Production、Level 5 Research。
- 📚 核心模块 00–15 覆盖：代理定义、代理循环、工具与函数调用、首个代理、状态与记忆、规划推理、上下文工程、运行时/缰绳、多代理、失败、评估、安全验证、生产代理、编码代理、自我改进代理。
- 🧩 应用系统包括：A1 Reddit 评论代理、A2 持久代理已就绪；A3 研究代理、A4 浏览器/计算机使用代理、A5 长期编码代理计划中。
- ⚙️ 零强制第三方包、零必需 API Key；核心课程提供确定性模拟器和 mock LLM，支持完全离线学习与自动测试。
- 🔌 可插拔真实模型：支持 OpenAI、Anthropic、Gemini 和本地 Ollama，示例位于 examples/minimal_agent/。
- 🧭 可选框架映射：帮助理解 LangGraph、AutoGen、OpenAI Agents SDK 和 MCP 如何组织代理相关职责。
- 🚀 5 分钟快速开始：克隆仓库后，用 python3 运行 01/02/04 示例，无需 API key、框架或依赖。
- 🧪 仓库包含核心模块、应用系统示例、minimal_agent、reddit_comment_agent、persistent_agent、self_improving_agent、coding_assistant，以及 137 个 unittest 测试。
- 📄 许可证为专有/源码可获取许可证，版权归 Tanmay Sah 2026 所有；未经书面许可不得复制、分发、修改或用于商业、企业培训及衍生用途。
- ❓ 社区可通过 QUESTIONS.md 和 GitHub Issues 提交问题，问题会直接影响后续模块设计。

---

### [GitHub - micronaut-projects/pyronaut：高性能 Python 应用平台 · GitHub](https://github.com/micronaut-projects/pyronaut?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - micronaut-projects/pyronaut: High Performance Python Application Platform · GitHub](https://github.com/micronaut-projects/pyronaut?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Pyronaut 是 Micronaut 项目下基于 GraalVM 与 Micronaut 的高性能 Python 应用平台，面向生产级服务，提供 CLI、Micronaut 集成模块以及构建、运行、测试、配置验证和原生打包工作流。

- 🐍 为 Python 开发者提供 HTTP 路由、依赖注入、配置、验证、序列化、测试，并可通过 Python 声明访问 Java 库。
- ☕ 为 Java 开发者通过 GraalPy 和共享 Micronaut 应用上下文添加 Python 支持。
- 🧭 主入口是 `pyronaut` 命令，作为 Python 编排器调用 JVM/native 工具，完成依赖解析、源码处理、运行、测试、配置验证、原生构建和测试资源管理。
- 📦 仓库包含 CLI 与多个集成模块，如 pyronaut-install、pyronaut-processor、pyronaut-dev、pyronaut-run、pyronaut-test、pyronaut-validate-config、pyronaut-native-build、pyronaut-tui 及运行时/测试支持库。
- 🛠️ 安装 CLI 需 Python 3.10+，Linux/macOS 上执行 `python3 -m pip install pyronaut` 和 `pyronaut setup`；完整用户指南位于 `src/main/docs/guide`。
- 🧱 源码构建要求 JDK 25、GraalVM 25.4、GraalPy 3.13.14（`graalpy3.13-25.4.4`），并使用 pyenv 管理 GraalPy 环境。
- ⚙️ 构建 SDK wheel 使用 `./gradlew :micronaut-pyronaut:buildSdkWheel --stacktrace --refresh-dependencies`，可安装到 active pyenv 环境或项目本地 venv。
- 🧪 pytest 工作流需在 GraalPy 环境中安装 pytest；CPython venv 无法为嵌入的 GraalPy 提供包，直接源码 JUnit 5 测试不需要 pytest。
- 🚀 Hello-world 示例通过 `pyproject.toml`、控制器和 TOML 配置，使用 `pyronaut install`、`process`、`dev` 启动，并用 `pyronaut test` 运行 pytest 测试，报告位于 `__pyronaut__/reports/tests`。
- ⚠️ 若 `pyronaut install` 报依赖解析失败，不应继续 `process`，否则会出现 `Missing build scope cache`；应修复依赖或仓库配置后重试。
- 📚 CLI reference 是命令语法、选项、生成文件、环境变量、退出码和代表性工作流的权威来源。
- 🏗️ 本地构建与检查使用 `./gradlew check` 和 `:micronaut-pyronaut:buildSdkWheel`；wheel 不包含原生可执行文件，安装后运行 `pyronaut setup` 下载镜像到 `~/.pyronaut/bin`。
- 🐳 功能测试分 Docker-free 与 Docker-backed；前者验证安装、配置验证、源码处理和原生 CLI，后者包含 MySQL/Micronaut Data 场景，仅在 `-Pdocker=true` 时运行。
- 🚄 支持使用 Oracle GraalVM 进行 PGO 原生镜像构建：instrument、train、optimize 三步；Linux 上 `pyronaut-run` 支持代码压缩，macOS 不支持。
- 📖 文档构建使用 `./gradlew publishGuide` 或 `./gradlew docs`，并参考 `src/main/docs/guide`、各 README、`CONTRIBUTING.md` 等文件。
- ⭐ 仓库采用 Apache-2.0 许可，当前约 18 stars、0 forks、43 个 issue、22 个 PR、682 次提交。

---

### [](https://github.com/anteloc/ldraw-nova?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [GitHub - anteloc/ldraw-nova: Agent tooling for generative LEGO models building, built with Astra and Opus 5.5, powered by Jev · GitHub](https://github.com/anteloc/ldraw-nova?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

ldraw-nova 是 anteloc 开源的一个 AI agent 工具项目，使用 Astra 和 Opus 5.5 构建、由 Jev 驱动，目标是把自然语言模型想法转化为可构建、可查看、可编辑的 LDraw LEGO 3D 模型。

- 🧱 仓库为 ldraw-nova，采用 AGPL-3.0 许可，约 314 stars、25 forks、34 commits；提供 agent 生成 LEGO 模型所需的工具、示例和指令。
- 🤖 给 agent 一个模型想法后，它会规划、迭代渲染和调整，最终输出 LDraw 源代码、3D/VR 查看结果、Blender 可编辑 .glb、聊天历史与思考过程。
- 🔍 零件搜索和示例模型检索依赖 jev-rerank 语义搜索与重排序，需要 TYPESAFE_API_KEY；没有 key 时回退全文搜索，效果可能更差。
- 🐳 通过 Docker 运行 Web 应用，需 Git 和 Docker；要同时克隆 ldraw-nova 与 ldraw-nova-docker 并使用同一 tag，首次构建约需 5GB 磁盘空间。
- 🌐 访问地址为 https://localhost:8443（Meta Quest 3 VR 需要）或 http://localhost:8765；应用无登录，只应在可信网络运行。
- 💡 项目动机是让 agentic LLM 设计可构建的实体物品；LDraw 被视为简单、底层、可执行的 CAD 汇编语言，适合让模型通过代码生成 3D 模型。
- 🧪 早期尝试包括 ldbuilder-ai、py2bricks、py4bricks；结论是 agent 更容易通过生成 Python 代码绕过几何数学，并从“生成模型的 Python 代码”中学习。
- ⚙️ 工作流程：agent 读取 instructions.md 等资料，规划零件、子模型与美学，反复渲染、检查、调整，直到模型完成；工具支持零件查找、示例参考、碰撞/间隙检测和无头渲染。
- 🧩 生成方式不是直接摆放零件，而是先产出 plan.json，再由 generator.py 执行生成 .mpd LDraw 源文件，类似“agent 写生成器，生成器产出 3D 模型”。
- 📚 提供多种指南：代理指令、视觉设计、车辆/飞船/结构/机械/模块工作流、几何与验证、工具参考和 LDraw 规则等。
- 🚧 待改进：Quest 3 VR 问题多、低端模型适配不足、生成昂贵且慢、需扩展 minifigs/Technic/飞船等模型家族、从手册建模和子模型细粒度检查。
- 🙏 致谢 LDraw 社区、LDView、LeoCAD、LDCad、ldraw.rs、pyldraw3 等；LEGO 是 LEGO Group 商标，本软件未获其赞助、授权或背书。

---

### [Polars — Polars 2.0 发布](https://pola.rs/posts/release-polars-2/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Polars — Release of Polars 2.0](https://pola.rs/posts/release-polars-2/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Polars 2.0 于 2026 年 10 月 6 日发布，虽非大型功能版本，但带来 SQL 一等支持、默认流式引擎与 out-of-core、新 Map 类型、更严格类型与显式行为，以及核心性能提升，并在 TPC-H/TPC-DS 基准中表现领先。

- 🚀 初始 out-of-core（spill-to-disk）支持启用，可在大内存压力下将部分操作落盘。
- ⚡ 多项核心性能优化，包括 join 重排序、公共子计划消除改进、动态谓词与布隆过滤器。
- 🧮 SQL 成为一等公民，覆盖大幅提升，并在 TPC-H/TPC-DS 上领先 DataFusion 和 DuckDB。
- 🖥️ 基准在 c7a.4xlarge 与 c7a.metal 上运行，每查询热运行 5 次、60 秒超时；默认 Polars 除一项外最快。
- 🌊 LazyFrame.collect 默认使用流式引擎，显著改善内存与性能，但 join/group_by/unpivot 等默认不保证行序，可用 maintain_order=True 保持。
- 💾 Out-of-core 默认启用，RAM 约 80% 时开始 spill，默认磁盘预算 64GB；当前支持 sort、窗口函数和许多表达式，未来扩展 join/group_by。
- 🗺️ 新增 Map 数据类型，直接支持 Arrow MapType，像字典一样映射键值，并提供 map.get、contains_key、len、keys、values 等表达式。
- ✅ 更严格的 Polars：更重视 dtype 与显式性，尽早失败，数据不匹配的隐式行为需显式选择。
- 🤖 严格性有利于 AI 迭代：可用 collect_schema() 提前解析类型并捕获 schema 级不匹配，无需物化数据。
- ☁️ 后续路线：改进 out-of-core、大 CPU 数量扩展、Polars Cloud 最快分布式引擎，并推进 GeoPolars。
- 📚 提供迁移指南和问题反馈入口；脚注说明基准结果不能与官方 TPC-H/TPC-DS 结果直接比较。

---

### [](https://blog.python.org/2026/10/python-31022-31117/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Python 3.10.22, 3.11.17, 3.12.15, 3.13.16 and 3.14.8 are now available! | Python Insider](https://blog.python.org/2026/10/python-31022-31117/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Python 3.10.22、3.11.17、3.12.15、3.13.16 和 3.14.8 于 2026 年 10 月 1 日发布，包含安全修复、维护更新，以及 Python 3.10 的最终版本；3.10 正式结束生命周期。
- 🐍 Python 3.10.22、3.11.17、3.12.15、3.13.16、3.14.8 现已发布。
- ⏳ Python 3.10.22 是 3.10 最终版，五年后 EOL，不再收到安全更新，建议用户升级到受支持版本。
- 🔐 Python 3.11 处于仅安全修复模式，持续至 2027 年 10 月，按需发布安全版本。
- 📦 3.10.22 和 3.11.17 仅提供源码；各自最后含二进制安装器的版本是 3.10.11 和 3.11.9。
- 🗓️ 3.12.15 是仅源码安全版本，安全支持持续至 2028 年 10 月。
- 🧰 3.13.16 是 3.13 最后一个完整维护版，之后仅安全修复；3.14.8 是维护版。
- 💾 3.13.16 和 3.14.8 包含二进制安装器，发布页列出完整安全内容与其他变更。
- 🐛 所有五个版本修复：格式化 float 或 complex 且精度接近 INT_MAX 时的崩溃或错误输出。
- 🔒 CVE-2026-19553：ssl.SSLContext.wrap_bio() 与 asyncio 验证 TLS 参数；3.10–3.12 对缺失 hostname 发 DeprecationWarning，3.13+ 抛 ValueError。
- 🌐 更新捆绑的 libexpat 至 2.8.5。
- 🗜️ CVE-2026-15310：限制 zipfile 对 bzip2、LZMA，以及 3.14 上 Zstandard 成员的每次读取解压，防止无界分配。
- 📂 CVE-2026-19672：修复 tarfile 提取过滤器可经“离开再返回”路径在目标外创建目录。
- 🛡️ CVE-2026-19445：修复 SNI 回调切换上下文后原上下文不再被引用时的 ssl 崩溃。
- 🔤 CVE-2026-17084：将 stringprep 和 IDNA 编解码器限制在 RFC 3454 定义的 Unicode 码点属性。
- 🔗 CVE-2026-15806：urllib.request HTTPPasswordMgr 凭据按 URL scheme 限定，防止 HTTPS 凭据用于匹配 HTTP URL。
- 🧱 3.10–3.13 额外修复：tarfile 硬链接到符号链接漏洞及链接回退提取时应用过滤器；Python 3.14+ 已受保护。
- 🔑 3.13.16 和 3.14.8 捆绑 OpenSSL 更新至 3.5.9；源码-only 的 3.10–3.12 不捆绑 OpenSSL。
- 🧬 3.10.22 改进 xml.parsers.expat 与 xml.etree.ElementTree 的 XML hash-flooding 防护。
- 🍎 macOS 27.0 上 IDLE/tkinter 的菜单对话框可能挂起并需强制退出；建议推迟升级或测试，关注 issue #158053。
- 🌌 文章以黑洞并合后的 ringdown 比喻 Python 3.10 的最后一个版本，感谢所有贡献者与发布团队。
- 🙏 鼓励通过贡献时间或支持 Python Software Foundation 来支持 Python。

---

### [Django](https://www.djangoproject.com/weblog/2026/oct/06/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Django security releases issued: 6.1.2, 6.0.9, and 5.2.18 | Weblog | Django](https://www.djangoproject.com/weblog/2026/oct/06/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

Django 团队于 2026 年 10 月 6 日发布 6.1.2、6.0.9 和 5.2.18 安全版本，修复四个 CVE 漏洞，并建议所有用户尽快升级。

- 🚨 发布信息：Sarah Boyce 于 2026 年 10 月 6 日宣布 Django 6.1.2、6.0.9、5.2.18 安全版本。
- ⬆️ 升级建议：所有 Django 用户应尽快升级到修复版本。
- 🛡️ CVE-2026-77050（低危）：`get_supported_language_variant()` 处理大量超长语言代码时，可能因缓存键未限长而消耗过多内存，造成拒绝服务；现超过 500 字符的语言代码会被拒绝或截断。感谢 Gleb Lizunov。
- ⏱️ CVE-2026-84429（中危）：`parse_header_parameters()` 解析带引号参数内大量分隔符时存在二次时间复杂度，可经 `Accept`、`Content-Type` 等头部触发拒绝服务；现改用 Python `email.message.Message`，部分异常头部解析行为可能改变，如缺失编码的 RFC 2231 值会被解码。感谢 Jisung Chae。
- 🌐 CVE-2026-87890（中危）：空间查询接受 `bytes` 栅格值且未强制包装为 `GDALRaster`，可能通过 VRT 文档引用外部栅格，导致 GDAL 以 Django 进程用户发起网络请求；若应用将攻击者控制的字节直接传入空间查询则可能被利用。该问题在 CVE-2026-15307 修复中被遗漏。现必须包装为 `GDALRaster`，有效十六进制几何的字节仍可用；此为向后不兼容变更，并提醒所有不可信用户输入都应先验证。感谢 sicksec。
- 🧩 CVE-2026-87975（中危）：可编辑主键的模型表单集存在权限滥用，伪造 POST 数据可删除限制查询集之外的实例，或通过仅编辑表单集创建实例；涉及 `OneToOneField`/父链接作主键，或表单字段含自然主键/UUID 主键的模型。默认 `BigAutoField` 主键不受影响。感谢 Seonggwon Yoon。
- 📌 受影响版本：Django main、6.1、6.0、5.2。
- 🩹 修复情况：补丁已应用到 main、6.1、6.0、5.2 分支，相关变更集可获取。
- 📦 已发布版本：Django 6.1.2、6.0.9、5.2.18，均提供 tarball 与 checksums。
- 🔑 PGP 密钥：本次发布使用 Sarah Boyce 的密钥 ID `3955B19851EA96EF`。
- 📮 报告方式：安全问题请私下发送至 `security@djangoproject.com`，不要使用 Django Trac 或论坛；详情见安全政策。

---

### [](https://www.meetup.com/psppython/events/316587369/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Python talk night at City University Seattle (Belltown), Thu, Oct 15, 2026, 5:30 PM   | Meetup](https://www.meetup.com/psppython/events/316587369/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

这是一场由 Puget Sound Programming Python (PuPPy) 主办、Andrew B. 和 Paul B. 主持的 Python 演讲之夜，将于 10 月 15 日周四 17:30–19:30 PDT 在西雅图 Belltown 的 City University of Seattle 举行，包含社交、两场演讲、闪电演讲、餐饮赞助和会后聚会。

- 🐍 活动：Python talk night at City University Seattle (Belltown)
- 👥 主持：Andrew B. 与 Paul B.，由 Puget Sound Programming Python (PuPPy) 主办
- 🗓️ 时间地点：10 月 15 日周四 17:30–19:30 PDT；City University of Seattle，521 Wall Street, Seattle, WA
- 💬 活动聊天：参加后可与其他与会者提前交流
- 🍕 赞助：ActiveState 与 Slalom Consulting 赞助月度演讲夜餐饮；MotherDuck 赞助 2026 年 8 月演讲夜餐饮
- 🗣️ 议程：17:30–18:00 开门/社交；18:00–18:10 开场；18:10–18:35 演讲 1；18:35–18:50 中场；18:50–19:05 闪电演讲；19:05–19:30 演讲 2；19:30–20:00 社交
- 🍻 会后聚会：Teku Tavern，552 Denny Way, Seattle, WA 98109
- 🎤 演讲 1：Zach Fudge，主题待定（TBD）
- ⚡ 闪电演讲：Austin Bennett — “Pip install rave”；尝试连接工程师与音乐演出/音乐节，并涉及 Python 在发布流程、认证、完整性、PSK、CI/CD 与 pip --require-hashes 中的作用
- 📊 演讲 2：Matt Drury — “The Beautiful Improbability of the Real”；通过抛硬币游戏和 Arcsine Laws 讨论随机性、模拟与可视化，以及判断玩家技巧和输赢含义
- 💻 携带物品：演讲形式活动，无需带电脑
- 📜 行为准则：所有参加者须遵守 PuPPy Code of Conduct
- 🚪 建筑入口：请从 6th Ave 与 Wall Street 入口进入
- 🚗 停车：仅街边停车和付费车库停车
- 🚌 交通：校园步行可达多路公交，包括 5th & Wall St、3rd Ave & Bell St、3rd Ave & Cedar St、7th Ave & Denny Way、Dexter Ave & Denny Way 等站点
- 🏷️ 相关主题：Seattle 活动、JavaScript、Python、开源、软件开发、敏捷与 Scrum

---

### [](https://www.meetup.com/vegaspy/events/316740118/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Writing a Large Language Model From Scratch Using Python: The Beginning Steps, Sat, Oct 17, 2026, 1:15 PM   | Meetup](https://www.meetup.com/vegaspy/events/316740118/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

VegasPy - 拉斯维加斯 Python 用户组将举办线下聚会，主题为“用 Python 从零编写大型语言模型：起步步骤”。活动由 Adam E. 主持，于 10 月 17 日星期六下午 1:15–2:45 PDT 在 Third Street 举行，Tech Alley 提供场地赞助。这是万圣节前聚会，包含趣味活动、LLM 入门讲解，并探讨现代 LLM 的工作原理及其是否属于真正的人工智能。活动每月第三个星期六重复，直到 2027 年 1 月 16 日。

- 🐍 主办方：VegasPy - 拉斯维加斯 Python 用户组
- 🧠 主题：用 Python 从零编写大型语言模型：起步步骤
- 📅 时间：10 月 17 日星期六，下午 1:15–2:45 PDT
- 🔁 频率：每月第三个星期六，持续至 2027 年 1 月 16 日
- 📍 地点：Third Street，814 S 3rd St, Las Vegas, NV 89101
- 🏢 赞助：Tech Alley 提供聚会空间
- 🎃 特色：万圣节前聚会，有 tricks and treats 和 LLM 入门演示
- 🤖 讨论：现代 LLM 如何运作，以及它是否算真正的人工智能
- 👻 着装：可穿万圣节服装；最佳模仿 7 世纪哲学家者可获特别奖品
- #️⃣ 标签：#VegasTech

---

### [](https://www.meetup.com/pydata-milton-keynes/events/316098480/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

**原文标题**: [Sovereign AI: Building AI You Can Trust, Mon, Oct 12, 2026, 5:00 PM   | Meetup](https://www.meetup.com/pydata-milton-keynes/events/316098480/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-766-october-8-2026)

这场活动由 PyData Milton Keynes 与白金汉大学合作举办，主题为“主权 AI：构建可信 AI”，聚焦如何构建、部署并保护 AI 系统，同时保持对数据、模型和数字基础设施的更大控制。

- 🤝 主办方：PyData Milton Keynes，联合白金汉大学；主持人/组织者包括 Philip O. 和 Harin S.
- 📅 时间：10 月 12 日周一 17:00–19:00 BST；地点：白金汉大学 Verney Park 校区（Buckingham MK18 1AD）。
- 🎯 核心议题：探索构建、部署与保护 AI 系统，并实现对数据、模型和数字基础设施的本地化与自主控制。
- 🎤 主题演讲：Harin Sellahewa 教授谈“主权 AI 的未来”，解释模型、数据和基础设施控制权的重要性。
- 🏙️ 专题分享：Dr. Madara Premawardhana 讲数字孪生与智慧城市，探讨 AI 和数据如何打造更智能、更具韧性和可信的城市。
- 🛡️ 专题分享：Dr Hisham Al Assam 讲主权 AI 的网络安全，关注安全、隐私与网络韧性。
- 💻 实践环节：Dr. Philip Obiorah 讲使用 Gemma 本地部署大语言模型，涉及数据控制、隐私和 AI 基础设施机会。
- ☕ 安排：18:15–18:25 休息、茶点与交流；19:00 闭幕并继续社交。
- 👥 目标受众：Python、数据与 AI 社区，聚焦可信、安全、本地可控 AI 的实用方法。
- 📌 备注：议程可能会有细微调整。

---

