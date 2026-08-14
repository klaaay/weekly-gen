### [](https://www.djangoproject.com/weblog/2026/aug/10/annual-release-cycle/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Django is moving to an annual release cycle | Weblog | Django](https://www.djangoproject.com/weblog/2026/aug/10/annual-release-cycle/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

Django 将转向年度发布周期，自 2028 年起每年发布一个功能版本，每个版本均获得三年 LTS 级支持，并优化 Python 版本兼容策略。

- 🔄 Django 指导委员会已接受 DEP 20，从 2028 年 1 月起改为年度发布，版本号直接使用年份，如 Django 2028、Django 2029。
- 🐍 Python 每年 10 月发布新版本，新周期下每个 Django 版本支持最新的三个 Python 版本，并在发布后首年内纳入新 Python 版本，支持窗口与 Python 同步结束。
- 🛡️ 每个功能版本都获得三年支持：一年主流 bug 修复外加两年安全与数据丢失修复，“LTS”标签不再使用，所有版本承诺完全一致。
- ⏭️ 不再存在 LTS 空档期，用户可逐年升级，任意时刻有三个版本受支持，为第三方包提供清晰、滚动的兼容目标。
- 📅 过渡时间表：Django 6.1（2026 年 8 月）、6.2 LTS（2027 年 4 月）、Django 2028（2028 年 1 月）、Django 2029（2029 年 1 月）、Django 2030（2030 年 1 月）。
- 🔒 2028 年前一切不变，Django 5.2 LTS 和 6.2 LTS 的既有支持承诺继续有效；API 稳定与弃用政策不变，且日历弃用期实际更长。
- 📖 完整规范与决策依据见 DEP 20，感谢所有参与讨论者及指导委员会的审议。

---

### [](https://bernsteinbear.com/blog/zkp/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [A quick look at zero-knowledge proofs | Max Bernstein](https://bernsteinbear.com/blog/zkp/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

零知识证明（ZKP）是一种交互式证明方法，让证明者在不透露实际解的情况下，向验证者证明自己确实拥有某个 NP 完全问题的解。本文以 3-着色问题为例，结合 Goldreich-Micali-Wigderson 论文中的经典协议，给出了 30 行左右的 Python 实现、概率安全性分析，并提供了网络演示及扩展到 Sudoku 等问题的思路。

- 🔍 零知识证明并非关乎加密货币，而是图论与简洁代码实现的结合。
- 👥 整个协议涉及“证明者”和“验证者”两方，证明者不泄露解本身即可完成验证。
- 🎨 核心示例是图的 3-着色：为节点分配 3 种颜色之一，使相邻节点颜色不同。
- 📜 基于 Goldreich、Micali 和 Wigderson 论文中的交互式协议，需要重复执行 m²轮（m 为边数）。
- 🔒 P1：证明者随机置换颜色，为每个节点加上随机数 nonce，并哈希后放入“锁定盒子”发给验证者。
- 🎲 V1：验证者随机选择一条边作为挑战，要求验证该边两端点的颜色。
- 🔑 P2：证明者仅揭示该边两端点的颜色和 nonce，而不会暴露整个着色方案。
- ✅ V2：验证者检查哈希是否匹配、两端颜色是否不同，若不满足则立即拒绝。
- 🧂 引入 nonce 是为了避免相同颜色产生相同哈希，从而防止泄露着色的整体结构。
- 📉 验证者被欺骗的概率上限为 (1 - m⁻¹)^(m²)，轮次增加时概率迅速下降。
- 🌐 文章提供了一个基于服务器/客户端的网络演示，真正隔离了证明者和验证者的数据。
- 🧩 零知识证明可推广至 Sudoku 等其他 NP 完全问题，只需通过归约转换为 3-着色。
- 🎓 作者对加密货币等现实应用不感兴趣，更欣赏图论、计算理论和分布式实现的乐趣。

---

### [](https://deadlovelll.github.io/2026-08-10-conditional-annotations-set-add-crash/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Two lines of Python that segfault the interpreter | Timofei Ivankov](https://deadlovelll.github.io/2026-08-10-conditional-annotations-set-add-crash/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

PEP 649/749 的惰性注解机制引入了一个可被用户重绑的全局集合 `__conditional_annotations__`，导致 CPython 3.14–3.16 中复用的 `SET_ADD` 操作码发生类型混淆，两行纯 Python 代码即可让进程崩溃。修复在 main 分支采用专用 intrinsic，在 3.14/3.15 分支则给 `SET_ADD` 加上安全检查。

- 🧠 两行纯 Python 代码（`__conditional_annotations__ = 0` 和 `a: 1`）即可让 CPython 3.14/3.15/3.16 崩溃，无 traceback，直接死于 SIGSEGV/SIGBUS。
- 🧩 根因来自 PEP 649/749：注解改为惰性求值，模块级条件注解用一个全局集合 `__conditional_annotations__` 记录执行过的分支。
- ⚠️ 该集合是普通 globals 名称，用户代码可重新赋值；编译器仍使用 `SET_ADD` 指令处理它，破坏了“操作数必为 set”的隐含假设。
- 🔓 `SET_ADD` 未做类型检查，直接强制转为 `PySetObject*`，读取越界字段导致内存损坏和进程终止。
- 🛠️ main 分支（#155026）修复：放弃复用 `SET_ADD`，新增专用 intrinsic 并检查类型、提供明确错误信息。
- 🔧 3.14/3.15 分支（#155071/#155072）修复：因不能改字节码/魔法数，改为给 `SET_ADD` 增加 `PySet_CheckExact` 检查，但错误信息只能保持通用。
- 💡 教训：编译器内部的“安全保证”依赖调用方遵守隐式契约；新功能复用同一操作码时可能打破它，且发布分支与开发分支需要不同的修复策略。

---

### [](https://theconsensus.dev/p/2026/08/02/almost-consensus.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [
    Almost consensus: ABD and the edges of quorum replication - The Consensus
  ](https://theconsensus.dev/p/2026/08/02/almost-consensus.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

本文通过可运行的 Python 示例和时序图，介绍了仲裁复制（quorum replication）与 ABD 算法，并清晰展示了 ABD 为何能实现线性化寄存器、为何不支持 CAS，以及为何不能解决共识问题。文章从 Thomas 的多数投票和 Gifford 的扩展出发，逐步构建简单仲裁读写，指出其非原子性，再引入 ABD 的读后写回机制，最后探讨 ABD 在真实系统（如 Cassandra 读修复）中的影子及其与共识、CAS 的边界。

- 📜 仲裁复制起源于 Thomas 的多数投票（1979）和 Gifford 的扩展（1979），通过多数派读写容忍节点故障：n 个副本、多数派为 ⌊n/2⌋+1，3 副本可容忍 1 个故障，5 副本可容忍 2 个。
- 🐍 文章用 Python 实现了简单仲裁读写：写操作带时间戳广播给所有副本，读操作从多数派中取最大时间戳的值；但该算法没有“提交”概念，副本收到写即暴露，读可能读到未完成写入。
- ⚠️ 简单仲裁算法不是原子/线性化的：一个读返回新值后，后续读可能因延迟写未到达而返回旧值，导致寄存器“回退”。
- 🔄 ABD 算法在读取后增加“写回”阶段：读选出最新值后先写回多数派再返回，从而阻止后续读看到旧值，实现线性化寄存器。
- 👥 多写者 ABD 需要额外查询阶段：写前先读多数派获取最大时间戳，再以更大时间戳写入；代价是更多网络往返，而 Raft/Multi-Paxos 一旦选主可单轮提交。
- ❌ ABD 不支持 Compare-and-Swap（CAS）：旧时间戳写入虽被副本忽略但仍能收到 ACK，写操作仍可能成功；CAS 依赖当前值做条件更新，需要全局顺序，ABD 无法决定并发操作的线性化顺序。
- 🧩 ABD 不是共识：共识要求一致的有序日志（如复制状态机），而 ABD 只保留最新时间戳值，抹平历史，无法区分“已提交命令”和“部分写入的失败值”。
- 🚀 实际系统中 Cassandra 的阻塞读修复类似 ABD 的写回阶段，可提供单调仲裁读；但像 CAS 的操作需要单独使用 Paxos 或 Raft 等共识协议。
- 💡 结论：ABD 适合无状态存储操作（get/put）并保证线性化，但不适合有状态命令或需要序列化顺序的场景；理解 ABD 有助于更深入掌握 Paxos 和 Raft。

---

### [Python 字符串字面量有点搞笑](https://sebsite.pw/w/20260806-pystrings.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [python string literals are kinda funny](https://sebsite.pw/w/20260806-pystrings.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

概述摘要：这篇文章讨论了 Python 字符串字面量的一个有趣特性，特别是原始字符串和 f-string 的解析规则，并解释了为什么某些看似奇怪的行是有效或无效的。

- 🧪 文章先提出一个小测验：两行代码中哪一行有效？结果是`r'asdf\''`有效，而`r'asdf\'`是语法错误。
- 🔍 原始字符串（`r`前缀）不会解释反斜杠转义，但词法分析仍与普通字符串相同，因此不能以反斜杠结尾。
- 😄 这种设计最初是为了简化实现，但接下来的 f-string 例子更显趣味。
- 📝 有效的 f-string 示例：`f'{'}'}'`返回`'}'`，说明表达式可在花括号内嵌套引号。
- 🧩 另一个 f-string 示例：`f'{67#}'`中的`#`注释被解析器正确处理，结果返回`'67'`。
- ⚙️ 词法分析 f-string 需要调用完整 Python 解析器处理花括号内的表达式，直到遇到未加括号且未注释的`}`、`!`或`:`才终止。
- 🤔 因为表达式可由`:`终止，所以 f-string 中的`lambda`和赋值表达式必须加括号，例如`f'{lambda: 67}'`会报错。
- 💡 文章通过这些例子展示了 Python 字符串字面量在语法解析上的独特行为和设计取舍。

---

### [](https://huggingface.co/blog/mayafree/model-dna?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Model Genome: Fingerprinting Whether an LLM Was Trained From Scratch or Derived](https://huggingface.co/blog/mayafree/model-dna?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

本文提出了一套可复现的“模型基因组”指纹识别方法，用于客观判断公开的大语言模型是从零训练还是基于开源权重派生而来，并以九家韩国机构的模型为例进行了验证。

- 🧬 核心问题：当实验室宣称“自主研发”基础模型时，外部人员仅凭公开文件如何验证？文章提出从架构、分词器、权重三个维度进行指纹比对。
- 📐 架构指纹：读取`config.json`中的关键字段（模型类型、隐藏层大小、层数、注意力头数等），若与某开源模型完全一致，则强烈表明架构被采用而非独立设计。
- 🔤 分词器指纹（亲缘测试）：通过比较`tokenizer.json`词汇表的重叠率（min-overlap），可识别“架构相同但自训分词器”或“直接复用基座分词器”等隐藏关系。
- ⚖️ 权重指纹（难点）：朴素的行级余弦相似度因旋转不变性而失效，即使明显同源也接近零；线性 CKA 虽能可靠确认“从零训练”（近零），但对“继续预训练”的检测力不足（约 0.25 vs 无关基线 0.21）。
- 🎯 结论：权重轴仅作为辅助证据，架构 + 分词器才是判定派生的主要依据。
- 🧩 额外轴：注意力机制多样性（如混合 Mamba2、Hyena、MLA 等）可作为架构原创性的廉价代理指标。
- 🏷️ 基因型分类：综合架构与权重，将模型分为原生（🟢）、适配（🔵）、混合（🟡）、移植（🔴）四类，并附分词器重叠与注意力多样性作为原始证据。
- 📊 实测结果：九家韩国机构模型并非统一模式，既有完全移植（架构 + 分词器精确匹配），也有完全原生（自建架构与权重），多数介于两者之间。
- ⚠️ 诚实与局限：该方法不指控不当行为，仅报告血缘；权重轴不能单独定论；所有输入均为公开数据，欢迎指正。
- 💻 复现方式：提供三个核心函数（架构指纹、词汇重叠、线性 CKA），指向任意两个 Hub 仓库即可运行；附在线演示“Model Genome Korea”。

---

### [](https://www.cmpnd.ai/blog/let-the-model-write-the-code.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Introducing Flex: Let the Model Write the Code — cmpnd](https://www.cmpnd.ai/blog/let-the-model-write-the-code.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

本文介绍 DSPy 新模块 Flex：它让优化器不仅能改写提示词，还能直接改写程序代码，从而提升准确率并大幅降低成本和延迟。文章通过位置融合任务和 SWE-bench 实验展示了其效果，并分析了生成程序的典型结构与常见优化模式。

- 🤖 Flex 是 DSPy 新模块，可无缝替代 Predict/ReAct/RLM，让 GEPA 等优化器直接修改程序代码与指令。
- 🔄 工作原理：Flex 暴露代码给优化器，反射模型可分解任务、编写辅助函数、实现路由逻辑并重写提示。
- 📊 位置融合测试：Flex+GEPA 在 240 条保留记录上准确率 95.0%，优于基线 90.4%，成本降低 28%，延迟降低 40%。
- 💰 通过惩罚因子 λ 控制 LLM 调用频率：λ=0.4 时几乎不调用模型（240 条仅 1 次），准确率仍达 92.1%，成本仅约 1/100。
- ⚙️ 生成程序典型结构：先归一化、比较、规则判断，仅当规则无法决定时才调用 LLM，且会将分析结果一并传给模型。
- 🧩 常见优化动作：分解任务、选择确定性代码或模型调用、路由清晰/模糊输入、持续进化程序。
- 🧪 SWE-bench 初步实验：Flex+GEPA 让 Haiku 4.5 解决率从 0/12 提升到 4/12，说明自适应工作流潜力。
- 📦 可保存与加载：优化后的程序是普通文件，可读、可 diff、可审查。
- 🔒 安全：模型生成的代码默认运行在沙箱中，仅通过预测调用和显式工具与宿主交互。

---

### [](https://pola.rs/posts/market-data-to-plotly-enterprise-dashboard/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Polars — Prototype on a laptop, scale to 16 billion rows: one Polars query](https://pola.rs/posts/market-data-to-plotly-enterprise-dashboard/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

本文介绍如何用一套 Polars 查询从笔记本电脑原型无缝扩展到 160 亿行数据：在本地子集上开发统一的 LazyFrame，通过 `remote()` 在 Polars Cloud 上运行同一查询，并将预聚合的小型 Parquet 制品交给 Plotly Dash 展示，彻底避免维护两套重复实现。

- 🧩 痛点：数据团队常在数据集超出手提电脑后重写管道，导致两套实现漂移；本文展示无需重写的工作流。
- 💻 本地探索：先处理 3 小时子集（9700 万行），用 `collect_schema` 和 `glimpse` 快速了解 schema 与数据，再用 `str.json_decode` 解析 JSON 并构建 `price_changes` LazyFrame。
- ⚙️ 流式引擎：调用 `pl.Config.set_engine_affinity("streaming")` 让所有 `collect()` 默认使用流式执行，内存有界，适合超大扫描。
- 📊 预聚合制品：将重聚合作为批处理提前完成，输出 6 个小型 Parquet 制品（如市场画像、活动脉冲、价格等），仪表板页面加载不再扫描原始数据。
- 📦 制品设计：最重制品 <5 MB；使用 `dt.truncate` + `group_by` 替代 `group_by_dynamic`，避免全局排序，天然可分区扩展。
- ☁️ 集群运行：同一 LazyFrame 通过 `.remote(ctx)` 提交到 Polars Cloud 的 8 节点集群，直接处理 160 亿行/500 GB 数据，无需第二套实现；`sink_to_single_file=True` 合并输出文件。
- 🖥️ 私有部署：Polars Distributed 也可运行在自有 Kubernetes 集群上，同样的“笔记本到集群”流程完全可落地在企业内部。
- 🏁 原子发布：每次运行生成新制品前缀，最后用 `manifest.json` 标记完成，并通过单个 S3 PUT 原子切换，仪表板始终读到一致快照。
- 📈 可视化服务：Dash 应用读取制品，按 `market_id` 过滤时利用 Parquet 谓词下推跳过无关行组，同时用 `@lru_cache` 缓存数据，避免重复读取 S3。
- 🤖 MCP 集成：同一应用同时作为 MCP 服务器，AI 代理可通过应用回调查询制品，权限沿用仪表盘的共享设置。

---

### [获取失败](https://medium.com/@munalpoudel3/django-email-backend-is-deprecated-heres-how-to-fix-it-django-6-1-mailers-guide-4c9182e82d33?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Failed to retrieve](https://medium.com/@munalpoudel3/django-email-backend-is-deprecated-heres-how-to-fix-it-django-6-1-mailers-guide-4c9182e82d33?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

无法总结：获取内容失败，状态码 403。

---

### [](https://edcrewe.blogspot.com/2026/08/from-routing-checks-to-trajectory.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Ed Crewe: From Routing Checks to Trajectory Testing: Evaluating an Agentic Chatbot](https://edcrewe.blogspot.com/2026/08/from-routing-checks-to-trajectory.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

overview summary
- 🤖 本文介绍如何为基于 Python 的 Postgres AI 混合管理器聊天机器人构建测试框架，核心挑战在于 LLM 代理的非确定性输出难以用传统 API 测试验证。
- 🧭 针对代理型聊天机器人，测试重点从“答案是否正确”转向“是否走对流程、用对工具”，即轨迹测试（trajectory testing）。
- 📘 定义关键术语：Golden 是理想输出示例（如简单答案 42），Rubric 是定性检查清单，Evals 是评估任务，LLM-as-judge 用大模型根据 rubric 打分，TCR 是任务完成率（可低于 100%）。
- 🧪 首个实用测试聚焦“路由”环节：给定用户提示，验证聊天机器人是否选择了预期的专业工具（如控制面操作、Postgres 运维等），通过比对目标工具与 Golden 快速做健康检查。
- ⚙️ 该测试框架从简单确定性路由开始，逐步演化，以应对代理全链路（路由、工具调用、数据获取、多轮对话）的质量验证。

---

### [获取失败](https://medium.com/@yair.lenga/a-streaming-json-formatter-that-works-with-existing-serializers-eced220da37d?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Failed to retrieve](https://medium.com/@yair.lenga/a-streaming-json-formatter-that-works-with-existing-serializers-eced220da37d?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

无法总结：获取内容失败，状态码 403。

---

### [](https://notebook.link/blog/numba-in-the-browser/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Numba in the Browser: Unlocking a New Scientific Python Stack in JupyterLite | Notebook.link Documentation](https://notebook.link/blog/numba-in-the-browser/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

overview summary
- 🚀 Numba 现已成功在浏览器中通过 JupyterLite 与 WebAssembly 运行，实现约 250 倍加速，比原生环境（约 90 倍）提升更显著。
- 🧩 解决了浏览器禁止可执行内存的难题，采用 WebAssembly 侧模块动态链接方案，将 LLVM IR 编译、链接并加载到运行中的内核。
- 🔧 基于 Xeus-Cpp 的既有架构，为 llvmlite 实现了 WebAssembly 执行引擎，并利用进程内 LLD 链接器替代子进程。
- 📦 通过 emscripten-forge 分发 Numba，支持在 JupyterLite 终端中动态安装，并实现 `@njit(cache=True)` 持久化缓存。
- 🔗 解锁整个生态：PyTensor、PyMC、interpolation.py、Dolo.py 等依赖 Numba 的库现可在浏览器中完整运行。
- 🎯 下一步计划包括向上游贡献代码、扩大测试覆盖、提升性能，并探索 SIMD 等 WebAssembly 特性。
- 🌐 该成果表明复杂编译器栈可突破浏览器边界，让 JupyterLite 成为严肃科学计算的平台。

---

### [](https://adamj.eu/tech/2026/08/12/python-introducing-emojet/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Python: introducing emojet, a fast emoji lookup library - Adam Johnson](https://adamj.eu/tech/2026/08/12/python-introducing-emojet/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

概述：emojet 是一个基于 Rust 的 Python 表情符号库，兼容现有 emoji 包 API，大幅提升转换速度并降低内存占用，同时支持多语言和别名查询。

- 🚀 emojet 是全新的 Python 表情符号库，提供表情符号与名称之间的双向转换及搜索功能，API 与老牌 emoji 包兼容。
- ⚡ 核心优势：转换速度快 3.5 倍，反转换快 70 倍，内存占用减少约 40%。
- 📦 使用 `emojize()` 将名称转为表情，用 `demojize()` 将表情转为名称，支持 14 种语言及 GitHub/Slack 别名。
- 🧠 底层采用 Rust 编写，利用完美哈希表和静态 trie 树，导入时无需解析 JSON，因此导入时间从 20.57 ms 降至 869.94 µs（约 23.7 倍加速）。
- 📊 基准测试显示：`demojize()` 单次调用从 345 µs 降至 4.94 µs，`emojize()` 从 29.23 µs 降至 8.33 µs。
- 💾 内存使用方面，导入并调用一次 `demojize()` 仅需约 17.4 MB，而原 emoji 包需要 29.2 MB。
- 🔧 数据基于 Unicode 17.0.0、CLDR 和 gemoji 生成，随包分发，安装时无需下载额外数据。
- 🎯 开发动机是优化项目启动时间，原 emoji 包导入耗时明显，因此用 Rust 重写并集成到 Python 扩展模块中。
- 📚 作者鼓励有表情符号转换需求的项目尝试 emojet，并提供了可复现的基准脚本。

---

### [](https://www.youtube.com/watch?v=ss6je4-nDx8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=ss6je4-nDx8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

overview summary
- 📺 提供媒體相關服務與合作資訊
- ⚖️ 說明著作權政策與權利保護機制
- 📞 提供聯絡管道與創作者支援
- 🧑‍💻 介紹創作者工具與廣告方案
- 🔧 涵蓋開發人員資源與技術條款
- 🔒 說明隱私權、安全性與政策規範
- 🧪 介紹 YouTube 運作方式及新功能測試
- ©️ 標示版權所有 © 2026 Google LLC

---

### [](https://github.com/AgriciDaniel/claude-seo?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [GitHub - AgriciDaniel/claude-seo: Universal SEO skill for Claude Code. 25 sub-skills + 18 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, backlinks, local SEO, maps intelligence, semantic clustering, e-commerce SEO, international SEO, Google APIs, and PDF/Excel reporting. Optional DataForSEO, Firecrawl, and Banana extensions. · GitHub](https://github.com/AgriciDaniel/claude-seo?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

Claude SEO 是面向 Claude Code 的开源 SEO 分析插件，并行运行 25 个子技能与 18 个专家代理，覆盖技术 SEO、E-E-A-T、Schema、AI 搜索优化、本地 SEO、电商与国际 SEO，并输出每条建议都可验证、可证伪的优先行动计划。

- 🌐 双版本发布：公开 MIT 版（AgriciDaniel/claude-seo）与社区私有镜像（AI-Marketing-Hub/claude-seo，需会员）
- ⚡ 并行高速审计：全站审计最多同时调度 15 个代理，分钟级完成；提供 32 个 `/seo` 命令，覆盖技术、内容、Schema、GEO、本地、电商、国际等场景
- 🧠 AI 搜索优先：对齐 Google AI 优化指南，对段落可引证性、实体存在、结构化数据评分，并明确否定 llms.txt、内容分块、AI 关键词改写等流行误区
- 📊 Google API 四层凭证：零密钥即可使用，Tier 0 解锁 PageSpeed Insights 与 CrUX 历史趋势；逐级解锁 Search Console、GA4、Keyword Planner
- 🔍 E-E-A-T 评估：依据 2025 年 9 月搜索质量评估指南，支持 Who/How/Why 启发式、过期域名风险、机器翻译漂移检测
- 🏪 本地 SEO 三层能力：Google Business Profile 信号、NAP 一致性、评论智能；多门店审计设有 30/50 页阈值防止 doorway page
- 🛠️ 可证伪建议：每条推荐附第一性原理依据、依赖关系、“如何知道失败”的检查与领先指标
- 📈 v2 重大增强：SPA 无头渲染、QRG 内容质量门、LCP 子部分拆解、4 个 Schema 生成器、5 个新 MCP 扩展，测试覆盖从 39 增至 410
- 🔒 隐私与许可：MIT 许可证、默认全本地运行、无遥测、无第三方 API 调用；可选接入 DataForSEO、Firecrawl、Ahrefs、SE Ranking 等扩展
- ⚠️ 已知局限：滚动绑定 hydration 等边缘页面需人工核对；无 Google API 凭证时 Core Web Vitals 仅为实验室估计，索引状态为推断

---

### [](https://github.com/semantica-agi/semantica?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [GitHub - semantica-agi/semantica: Graph-Native Infrastructure for Context and Accountable AI Systems · GitHub](https://github.com/semantica-agi/semantica?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

Semantica 是一个开源、可自托管的图原生基础设施层，专为需要可解释、可审计、可追溯决策的 AI 代理系统而设计。它位于 LLM、向量库和代理框架之下，以确定性方式构建上下文图谱（Context Graph）并管理完整决策溯源，从而解决传统 RAG 和 LLM 记忆缺乏可问责性的问题。

- 🧠 图原生基础设施：将企业数据构建为上下文图谱和知识图谱，支持图分析和因果推理，所有决策带完整溯源，确保可解释、可追踪和可信。
- 🔍 决策智能：每个决策都是头等对象，支持记录、追踪因果链、语义先例搜索、影响分析和策略合规检查。
- 🛡️ AI 治理与本体：提供 SHACL 约束、冲突检测、OWL 生成和 SKOS 词汇表管理，并配有可视化编辑器。
- 📜 完全可审计：基于 W3C PROV-O 标准记录每条事实的溯源，可导出 JSON、CSV 或 RDF 格式的审计跟踪。
- ⚙️ 确定性推理：内置正向链接、Rete、Datalog 和 SPARQL 推理引擎，推理路径完全可解释，避免“黑盒”问题。
- 🔗 知识管道：支持多源摄取、实体感知分块、NER/关系/事件抽取、语义去重和保留溯源的合并，构建高质量知识图谱。
- 🏢 企业数据平台集成：提供 Databricks（Unity Catalog + Delta Lake）和 Snowflake 原生连接器，让湖仓/数仓中的表直接成为带溯源的知识图谱节点。
- 🗄️ 多语言图存储：原生支持 RDF 三元组库（Oxigraph、Blazegraph、Jena、RDF4J）和属性图数据库（Neo4j、FalkorDB、AGE、Neptune），可无缝替换。
- 📊 图分析与可视化：提供中心性、社区检测、链接预测和最短路径等图算法，以及交互式浏览器工作台（Knowledge Explorer）。
- 🔌 集成生态：提供 MCP 服务器、REST API、CLI、Agno 多代理共享上下文，以及 Claude Code、Cursor、VS Code 等插件。
- ⏱️ 时间智能：支持双时态事实、点时间快照和自然语言时间表达式规范化，可回放历史状态。
- 🔒 安全与合规：最新版本修复了多个严重安全漏洞；适用于金融、医疗、法律、政府等受监管领域的审计要求。

---

### [](https://github.com/DynamicsAndNeuralSystems/pyhctsa?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [GitHub - DynamicsAndNeuralSystems/pyhctsa: The most comprehensive time-series feature extraction package in Python. · GitHub](https://github.com/DynamicsAndNeuralSystems/pyhctsa?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

pyhctsa 是一个 Python 工具包，用于高度比较时间序列分析，提供全面的特征提取功能。它支持自定义特征集、并行计算，并附带教程和多种许可证。

- 📦 安装：通过 `pip install pyhctsa` 即可安装。
- ⚙️ 基本用法：实例化 `FeatureCalculator`，默认加载全部特征，也可通过 YAML 配置自定义特征集，加载时会显示主操作数量。
- 📊 特征提取：调用 `.extract()` 方法，可处理单个或列表形式的时间序列，且各序列长度可不一致，返回 N×F 的 pandas 数据框。
- 📘 教程：仓库提供步骤式教程和示例工作流，位于 `/tutorials`。
- 🔧 高级用法：可直接调用单个操作（如 `raw_hrv_meas`），但仅适用于单个时间序列实例。
- 🚀 并行计算：使用 `LocalDistributor` 可多核加速特征提取，建议设置为物理 CPU 核心数。
- 🔑 许可证：核心代码采用 GPL-3.0，部分外部包（如 TISEAN、Max Little's code 等）有各自许可证。
- 🤖 AI 披露：部分代码（测试和函数文档）由 LLM 辅助生成，并经过人工审核。
- ⭐ 项目信息：拥有 127 星、11 fork，被描述为 Python 中最全面的时间序列特征提取包。

---

### [](https://github.com/OWASP/www-project-agent-memory-guard?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [GitHub - OWASP/www-project-agent-memory-guard: OWASP Foundation web repository · GitHub](https://github.com/OWASP/www-project-agent-memory-guard?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

OWASP Agent Memory Guard 是一个专门防护 AI 智能体记忆投毒的运行时安全库，能在上下文重置后仍检测恶意记忆写入，并已获得 OWASP 孵化项目认证。

- 🛡️ 拦截记忆投毒攻击：在智能体与记忆存储之间构建防护层，阻止指令覆盖、数据外泄和工具劫持，即使上下文重置也有效。
- ⚡ 极简集成：三行代码即可接入，无需 API 密钥或外部调用，本地运行中位延迟仅 59 微秒。
- 📊 基准测试亮眼：针对 55 个真实攻击样本，检测召回率 92.5%、精确率 100%、误报率 0%，其中提示注入和受保护密钥篡改检测率达 100%。
- 🔍 多维度防护：支持 SHA-256 完整性校验、提示注入检测、敏感数据泄露识别、密钥篡改防护、大小异常及自我强化循环追踪。
- 📜 声明式策略：通过 YAML 定义规则，对检测结果执行允许、编辑、隔离或阻断等动作，并支持受保护/不可变密钥设置。
- 🔌 框架集成丰富：提供 LangChain 中间件、OpenAI Agents SDK、AutoGen、mem0、CrewAI 的现成适配器，可无缝嵌入现有智能体流程。
- 🏗️ 清晰架构：位于智能体与记忆存储之间，每次写入经探测器流水线和策略引擎处理，并生成结构化安全事件供取证与回滚。
- 🧭 溯源与治理：支持源类别标记（外部工具、用户输入、智能体自身、系统），配合自我强化冷却机制和基于谓词的记忆退役策略。
- 📈 可观测性与合规：支持 OpenTelemetry 导出安全决策跨度，并映射至 NIST AI RMF 1.0 和 EU AI Act 要求。
- 🚀 路线图清晰：后续版本将增加 LlamaIndex/CrewAI 适配器、Redis/PostgreSQL 后端、ML 异常检测和向量存储保护，并计划在 Q4 2026 推出 v1.0。
- 🤝 开放社区：欢迎贡献框架适配器、后端集成、检测器改进和文档，也鼓励生产用户加入展示列表。

---

### [](https://github.com/bagowix/interlock?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [GitHub - bagowix/interlock: Circuit breaker for Python: sync + async in one class, sliding-window rate, slow-call detection, Polly-style resilience pipeline, type-safe API · GitHub](https://github.com/bagowix/interlock?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

该内容介绍的是一个名为 interlock 的现代 Python 熔断器库，它提供同步与异步统一 API、滑动窗口统计、慢调用检测、类型安全接口及传输层集成；同时强调安全的生产发布流程、可组合的弹性管道、丰富的第三方集成，并坦诚承认其成熟度低于老牌库，但用严格的测试和类型检查加以补偿。

- 🔧 核心定位：现代电路熔断器库，同步/异步统一在一个类中，支持滑动窗口速率与慢调用检测
- 📦 安装与要求：通过 `uv add interlock-cb` 或 `pip install interlock-cb`，支持 Python 3.11+，核心仅依赖标准库
- 🚀 快速上手：使用 `@breaker` 装饰器保留函数签名与同步/异步特性，也支持 `breaker.call()`、`with` 和 `async with` 等调用方式
- 📊 滑动窗口统计：支持基于计数或时间的窗口，可检测慢调用及未被异常捕获的失败返回值
- 🛡️ 安全发布：提供 `METRICS_ONLY` 初始状态先观察真实指标，再切换为强制执行；支持 `EventListener` 与 `transport.registry` 进行监控和状态检查
- 🧩 弹性管道：通过 `Pipeline.builder()` 组合 fallback、retry、circuit breaker、bulkhead 和 timeout，顺序明确且具备可观测性
- 🌐 集成生态：覆盖 httpx2、httpx、aiohttp、requests、FastAPI、Litestar、tenacity、Redis 共享状态、OpenTelemetry 指标等，并有 LLM SDK 和 Flask/Django 示例
- ⚖️ 对比差异：相比 pybreaker 和 circuitbreaker，interlock 提供原生 asyncio、时间滑动窗口、慢调用检测、跨进程共享状态及管道，但项目成熟度较低
- ✅ 质量保障：宣称 100% 分支覆盖率、三种严格类型检查器、状态机与引擎突变测试、属性/模型测试，并在自由线程 CPython 上跑 CI
- 📄 文档与许可：文档托管在 GitHub Pages，采用 MIT 许可证，欢迎通过 PR 和 issue 贡献或报告问题

---

### [](https://github.com/feberts/python-game-server?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [GitHub - feberts/python-game-server: A lightweight server and framework for turn-based multiplayer games · GitHub](https://github.com/feberts/python-game-server?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

一个轻量级、可扩展的 Python 游戏服务器与框架，专为回合制多人游戏设计，基础 Python 技能即可开发客户端或添加新游戏。

- 🎮 提供统一且灵活的 API，支持多个并行游戏会话，可加入指定会话或自动加入下一个非满会话。
- 🧩 新游戏只需继承 AbstractGame 并覆盖方法，可通过模板快速实现，无需修改 API。
- 📡 客户端模块 game_server_api 支持开始/加入会话、提交操作、获取状态和重开游戏。
- ⚡ 快速启动：运行 server/game_server.py 和两个客户端（如 tictactoe_client.py）即可体验。
- 🎯 适用于棋盘/卡牌等回合制游戏开发，以及编程课程中学生的项目实践。
- 🔧 服务器配置简单，可设置 IP、端口、TLS，支持 systemd 服务，仅依赖 Python 标准库。
- 🎓 源于编程课程教学场景，但也适用于其他教育或实际项目。
- 🤝 开源贡献友好，欢迎提交 Pull Request、Issue 或讨论，采用 GPL-3.0 许可证。

---

### [](https://github.com/paradigmxyz/centaur?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [GitHub - paradigmxyz/centaur: Centaur is frontier, agentic infrastructure that you own. Centaur is like Claude Tag, but open source and on steroids. · GitHub](https://github.com/paradigmxyz/centaur?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

Centaur 是一个面向团队的自托管 AI 代理平台，让团队通过 Slack 与共享代理对话，并在隔离的 Kubernetes 沙箱中执行真实任务。它支持自带代理框架、共享工具插件、持久化工作流和精细的凭证控制，既适合本地轻量部署，也可用于生产环境。

- 🤖 Slack 原生交互：在 Slack 中提及机器人即可获得任务进度和最终答案，也可通过 API 驱动。
- 📦 真实执行环境：每个会话运行在独立的 Kubernetes 沙箱中，内置 shell、git、Python、Node.js 等工具。
- 🔧 自带 Harness：支持接入 Amp、Claude Code、Codex 等 CLI 代理或自定义部署工具。
- 🧩 共享工具插件：以 Python 插件形式封装内部服务、API、数据库等，一次添加、全局可用。
- ⏳ 持久化工作流：任务可休眠、恢复、等待事件、启动子代理，并在服务重启后继续运行。
- 🔐 凭证边界：代理只看到占位符，iron-proxy 在出站请求时安全注入真实密钥。
- 🔁 可重放状态：消息、执行、事件和投递状态全部存储，客户端可随时重连查看结果。
- 🏢 组织覆盖层：无需 fork 即可叠加自定义工具、工作流、角色、技能和提示词。
- 🎯 典型场景：调查 CI 失败、回答内部工具问题、总结 Slack 线程、运行定期检查、协调多步运维。
- 🧱 核心架构：Slack/API → Centaur API → Postgres 持久状态 + 工具/工作流运行时 → Kubernetes 沙箱 → 受控出站。
- 🗂️ 主要目录：api-rs（Rust 控制平面）、slackbotv2（Slack 集成）、sandbox（代理镜像）、iron-proxy（出站代理）、tools/workflows（插件）。
- 🚀 本地入门：需要 k3s 集群、克隆仓库、安装 just，配置 1Password、Slack 等环境变量，运行 `just bootstrap-secrets` 和 `just up`。
- 🧪 安全模型：默认拒绝网络策略、按沙箱代理出站、凭证仅绑定特定主机和头、全程可审计。
- 📚 文档齐全：提供 Quickstart、生产部署、架构、开发者指南、工具和工作流文档。
- 🤝 开放贡献：通过 `just build-one` 构建服务，使用 ruff 和 pytest 进行 Python 代码检查与测试。

---

### [](https://github.com/fujitoid/key-amnesia?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [GitHub - fujitoid/key-amnesia: Let your AI agent use your passwords and API keys - without ever letting it see them · GitHub](https://github.com/fujitoid/key-amnesia?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

key-amnesia 是一个开源工具，让 AI 代理（如 Claude Code、Cursor、Codex）能使用密码和 API 密钥，却永远不会直接看到它们。它通过加密保险库存储秘密，在运行时注入子进程环境，并审查输出中的秘密值；主密码只能在独立的控制台窗口中由用户亲手输入。工具提供从安装、初始化、导入 .env、扫描泄漏到运行受保护命令的完整命令行工作流，同时明确列出了安全边界和局限。

- 🔒 背景问题：传统 .env 文件的威胁模型已过时，任何 AI 代理可读取的密钥都是 LEAK（Locally Exposed Agent Key）。
- 💡 核心方案：密钥存入加密 vault；`ka run` 将值注入子进程环境，输出中的秘密会被审查掉。
- 👤 主密码只能由用户在真实键盘输入；代理请求批准时会弹出独立控制台窗口，代理无法读取或输入。
- 🛠️ 快速上手：`pip install key-amnesia`，然后依次运行 `ka setup`、`ka init`、`ka import .env`、`ka scan`、`ka run`。
- 🔍 扫描功能：`ka scan` 仅报告密钥名称/路径/计数，不泄露值；`--deep` 会检查 Claude Code、Codex、Copilot 的会话记录。
- 🧠 两种使用模式：per-call（每次使用秘密都询问密码）和 cached（`ka unlock` 后 30 分钟内免提示，可配置）。
- 🚪 可选准入标志：`--pre-admit` 自动批准下一个连接进程；`--admit-tree` 批准所选祖先及其全部后代进程。
- ⚠️ 诚实的安全边界：命令若对秘密做编码/混淆后输出仍可能泄漏；输出需完整收集、审查后才释放（非实时）。
- 📛 秘密名称以明文存储（便于 `ka list`），值永不明文；主密码不跨任何进程通道传递。
- 🖥️ 安全假设：代理不能控制屏幕；无头（headless）机器无法批准则默认失败关闭。
- 👥 同用户进程可访问 guard 会话（类似 ssh-agent），但 guard 永不返回原始值；Windows 的进程身份验证弱于 Linux。
- 🛡️ 避免使用 `ka set NAME VALUE` 内联形式，应使用交互式隐藏提示，以防被同用户进程窥探。
- 📄 开源项目（Apache-2.0），提供 Discord、GitHub Discussions/Issues 社区渠道，并有设计文档和威胁模型说明。

---

### [](https://www.meetup.com/psppython/events/315743975/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Python talk night at MotherDuck, Wed, Aug 19, 2026, 5:30 PM   | Meetup](https://www.meetup.com/psppython/events/315743975/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

本活动是 PuPPy 在 MotherDuck 举办的 Python 主题演讲之夜，包含两场正式演讲和一场闪电演讲，并提供餐饮与社交环节。

- 📅 活动时间：8 月 19 日（周三）下午 5:30 至 7:30（PDT），会后有 after party
- 📍 活动地点：MotherDuck 办公室，地址为 2811 Fairview Ave, Seattle, WA
- 👥 主办方：Puget Sound Programming Python（PuPPy），由 Andrew B.和 Paul B.主持
- 🗣️ 演讲 #1：Nick Buker 主讲“GraphNN with PyTorch for prediction of molecular properties”，结合 RDKit 与 PyTorch Geometric 构建分子熔点预测模型
- ⚡ 闪电演讲：Matt Drury 分享“all([]) == True and any([]) == False”，从普遍性质角度解释空列表的布尔归约
- 🔜 演讲 #2：内容、讲者均待定（TBD）
- 📋 活动流程：5:30 开门社交，6:00 开场致辞，6:10 演讲#1，6:35 休息，6:50 闪电演讲，7:05 演讲#2，7:30 闭幕致辞，随后前往 Little Water Cantina 续摊
- 🍽️ 餐饮赞助：MotherDuck 提供墨西哥食物和饮料；另有 Pecado Bueno、ActiveState、Slalom Consulting 提供食物捐赠与赞助
- 🚗 交通与停车：附近有街边停车（5:30 后免费），步行可达公交 49 路和 70 路站点
- 📏 注意事项：参会者无需携带电脑，但须遵守 PuPPy 行为准则；MotherDuck 工作人员会在一楼开门引导至楼上办公室

---

### [](https://www.meetup.com/_chipy_/events/315968394/)

**原文标题**: [ChiPy August 2026 __main__ Meeting, Thu, Aug 20, 2026, 6:00 PM   | Meetup](https://www.meetup.com/_chipy_/events/315968394/)

本次 ChiPy 2026 年 8 月主会议将于 8 月 20 日晚在芝加哥 Slalom Build 举行，由芝加哥 Python 用户组主办，包含两场主题演讲，并提供餐饮与社交环节；参会者需提前注册以通过大楼安全验证。

- 📅 活动时间：8 月 20 日（周四）18:00–20:00（CDT），18:00 提供餐饮，18:30 正式开始演讲。
- 📍 活动地点：Slalom Build，地址为 200 E Randolph St, Suite 3700, Chicago, IL（Aon Center 内）。
- 👥 主办方：ChiPy（芝加哥官方 Python 用户组），由 Carlos A. 主持。
- 🎤 演讲一：Andrew Wingate《探索执行模式》（高级，30 分钟），探讨程序执行类型及如何在时间维度上协调它们。
- 🛠️ 演讲二：Roger Steve Ruiz《Docstrings 作为数据库》（中级，10 分钟），讲解如何用 griffe 和 docstring-parser 从 Python 文档字符串中提取结构化数据，并借助 Python→JSON→11ty 管道构建文档站点。
- 🔐 注册要求：需填写法定全名和邮箱，以便获取邀请函并供大楼安保核对身份。
- 🔗 更多详情：可访问 https://www.chipy.org/meetings/1179/ 或 ChiPy 的 LinkedIn 页面。

---

### [](https://www.meetup.com/pydata-berlin/events/316084301/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [PyData Berlin 2026 August Meetup, Wed, Aug 19, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-berlin/events/316084301/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

overview summary
- 📅 本次活动为 PyData Berlin 2026 年 8 月聚会，于 8 月 19 日 18:00-21:00 在柏林 GetYourGuide 办公室举行，提供餐饮，18:45 关门，需准时并实名登记。
- 🎤 第一个演讲《从发现到交易：用意图感知排序个性化市场》由 GetYourGuide 的 Kaan Isik 和 Mihail Douhaniaris 分享，介绍如何通过实时机器学习细分用户（发现型与交易型），并据此优化活动排名，提升参与度和转化率。
- ⚡ 第二个演讲由 trivago 的 Alexander Fischer 带来，主题为《用新算法和 Rust 加速 PyFixest 的固定效应去均值》，讲解固定效应回归的计算瓶颈，以及基于 Rust 的新策略如何在 PyFixest 库中提升效率。
- 💡 活动在两个主演讲之间设有 2-3 个闪电演讲名额（每个 3-5 分钟），欢迎参与者报名展示。
- 🛡️ 活动遵循 NumFOCUS 行为准则，强调友善、专业、禁止骚扰及不当言论，以营造包容的社区环境。
- 🏷️ 相关话题涵盖柏林活动、深度学习、机器学习、数据科学、Python 和开源。

---

### [](https://www.meetup.com/pydatachi/events/315987808/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

**原文标题**: [Silicon Societies, Thu, Aug 20, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydatachi/events/315987808/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-758-august-13-2026)

overview summary  
- 🤖 活动主题为“硅基社会”，探讨当数百万 AI 代理与人类一同使用互联网时会发生什么，由 PyData Chicago 主办，属混合形式线下线上同步进行。  
- 📅 活动时间为 8 月 20 日（周四）下午 6:00 至 7:30（CDT），线下地点在芝加哥 Merchandise Mart，线上通过 Zoom 参加。  
- 🧠 演讲围绕 AI 代理社交网络（如 MoltBook）的兴起，讨论代理与代理交互、AI 社会模拟、以及百万 AI 代理与人类决策的异同。  
- ⚠️ 核心观点指出，大规模 AI 代理模拟有助于研究协调、决策和涌现行为，但模拟结果未必等同于现实人类行为，需警惕“硅基社会”与人类社会的差异。  
- 🌐 现实应用包括 AI 代理拥有社交媒体、替人购物、预约医疗等，未来互联网将越来越多面向代理设计，需更好的理论、方法和保障措施来评估社会影响。  
- 🍕 活动由 Grainger 赞助场地和小吃，地址为 222 W Merchandise Mart Plaza 18 楼，参加者需在 8 月 13 日前 RSVP 并携带身份证件。  
- 🔗 线上参与者需在 6 点通过指定 Zoom 链接加入，会议 ID 和密码已在活动详情中提供，相关主题涵盖芝加哥活动、数据科学、开源和工作流。

---

