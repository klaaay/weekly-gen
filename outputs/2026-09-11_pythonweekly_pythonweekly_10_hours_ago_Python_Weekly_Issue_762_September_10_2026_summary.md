### [用1024字节制作一个Python解释器 - Austin Z. Henley](https://austinhenley.com/blog/python1024.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Making a Python interpreter in 1024 bytes - Austin Z. Henley](https://austinhenley.com/blog/python1024.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

作者 Austin Z. Henley 记录了他用 C 语言手写一个 1024 字节 Python 解释器的实验：不追求完整 Python，而是实现一个能运行 FizzBuzz、看起来像 Python 的子集，并通过递归下降解析、边解析边执行和极限代码高尔夫把体积压到 1024 字节。

- 🎯 挑战目标：用 1024 字节 C 代码实现 Python 解释器；最初尝试 512 字节但失败。
- 🐍 目标不是完整语言，而是支持看起来像 Python 的语法：def、冒号、缩进、if 无括号等。
- 🧮 解析器是递归下降式，表达式在解析过程中直接求值，先支持 1+2，再扩展到赋值和语句。
- 🗃️ 解释器状态很少，使用全局变量、固定源码数组和符号表；源码约 999 字符。
- 🚫 几乎没有错误处理，假设关键字、token 边界和空白处理都正确；只保留缩进和字符串中的空格。
- 🔤 变量名限制为单个小写字母，因此可直接用字符 ASCII 值查符号表。
- 🧱 缩进块通过比较最小缩进递归执行，利用 C 调用栈处理代码块嵌套。
- 🔁 while/for 不编译，循环记录条件位置，每轮跳回并重新解析；函数也通过保存/恢复源码位置实现调用。
- ⛳ 为省字节使用大量代码高尔夫技巧：单字母命名、全局临时变量、隐式 int、ASCII 常量、三目/逗号/位运算，以及 GNU C89 特性。
- 📉 可读版超过 4800 字节，最终高尔夫版为 1024 字节；作者认为若只求 FizzBuzz 可低于 800 字节。
- ✅ 最终支持整数变量/字面量、赋值、+ - * %、比较、真假值、if/else、while、for range、无参函数、递归、缩进块、print 和注释。
- 💻 可读版和高尔夫版都在 GitHub；作者最后邀请读者尝试自己的 1024 字节 Python 实现。

---

### [](https://jestoph.com/2026/09/04/jane-street-challenge.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [On solving the Jane Street Reverse Engineering Challenge | jestoph’s tech blog](https://jestoph.com/2026/09/04/jane-street-challenge.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

overview summary
- 🧠 作者参与了 Jane Street 的 ASIC 逆向工程挑战：从 GDS 芯片文件反推电路功能并寻找答案。
- 🧰 他用 Python 的 gdstk 读取 GDS，识别出 sky130 标准单元，并从 VCD 文件中发现 “TRY AGAIN” 等线索。
- 🚧 因为偏爱“硬核路线”，他自建电路仿真器、硬件描述语言、解析器、测试框架，甚至尝试写 GDS 查看器，绕了许多弯路。
- 📚 阅读 sky130 文档后，他学会把几何图形和标签映射到逻辑单元 I/O，并用重叠检测提取 GDS 中的连线关系。
- 🧩 在热身题中，他还原出移位寄存器、加法器和比较器，并构造出使比较器满足 496 的输入，验证流程可行。
- 🏗️ 正式题包含约 1 万个单元、81 种组件；他手动实现 40 多个新组件，生成 Verilog，并优化电路提取速度。
- 🐞 他发现 Jane Street 文件中一个疑似连接错误并上报，第二天得到确认，这成为他引以为豪的技术成就之一。
- ✉️ 修复 reset 引脚问题后，仿真输出 “TRY AGAIN”；他还整理出：全 0 得 “EMPTY SKY”，全 1 得 “BIG BANG”。
- 🔄 面对 120 位输入，他尝试反向时间求解，先用电子表格生成 Verilog 验证思路，再转向 z3 约束求解器。
- 🎯 他把关键 24 条线约束为在特定时刻同时为高，最终 z3 找到可行输入并保存为 out.txt。
- 🏆 在仿真器中运行后得到正确答案 “(* TWO STARS *)”，并获 Jane Street 确认。
- 🌙 整个挑战耗时约一个月，充满失眠和硬核调试；作者期待未来新挑战，也愿意在悉尼与感兴趣的人交流。

---

### [](https://www.better-simple.com/django/2026/09/09/nifty-feature-q-objects/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [
    
      Nifty Django Feature: Q() Objects · Better Simple
    
  ](https://www.better-simple.com/django/2026/09/09/nifty-feature-q-objects/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

本文介绍 Django 中 Q() 对象的实用特性：它用于表达 SQL 查询条件，特别适合动态构建和组合过滤器，并能帮助避免跨模型关系过滤时的多次 JOIN 问题。

- 🧩 Q() 对象表示可放入 SQL WHERE 子句的查询条件，通常任何能传给 .filter() 的条件都能用 Q() 表达。
- 🔁 .filter(~Q(...)) 等价于 .exclude(...)，适合动态拼装过滤逻辑。
- 🐾 文章用 Pet/Species 示例展示如何组合 Q() 查找“急需零食”的宠物：结合空值、时间条件与 F("treats_given") 字段比较。
- ✍️ Q() 可作为 .filter() 的位置参数，也可与普通关键字参数混用；若混用，Q() 位置参数应放在前面。
- 🧱 Q() 可动态构建：拆分搜索词后循环累加 Q(name__icontains=term)；但大量 OR 查询性能较差，正式搜索建议使用全文检索。
- 🧬 Q() 支持组合与复用，也可将字典解包进去；可封装成函数或模型类方法，按关系前缀生成查询条件。
- ⚙️ 可基于动态选项构建 Q()，再统一传入 .filter()，实现类似 GraphQL 的自定义过滤；但不应把未受控 JSON 直接解包为 Q()，以免生成不可信 SQL 条件。
- 🔗 在同一 .filter() 中写多个跨关系条件只会产生一个 JOIN；链式多个 .filter() 会产生多个 JOIN，语义可能变成“不同关联对象分别满足条件”，常是隐患。
- ✅ 作者建议：动态过滤时优先用 Q() 构建查询，再传入单个 .filter()，可保持清晰并避免多次 JOIN 的陷阱。
- 🎯 总结：Q() 不是每次必需，但在需要动态、可组合过滤时，是 Django ORM 的最佳伙伴之一。

---

### [](https://deadlovelll.github.io/2026-09-05-reading-dict-deoptimizes-attribute-access/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Reading __dict__ once permanently deoptimizes attribute access | Timofei Ivankov](https://deadlovelll.github.io/2026-09-05-reading-dict-deoptimizes-attribute-access/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

传统 Python 性能建议“把属性访问提出循环”在 Apple M3 的 CPython 3.14.6 上仍能带来约 1.33 倍提升，但文章指出其常见解释自 3.11 起已失效；现代 CPython 通过内联值数组特化属性访问，而读取 `__dict__`、`vars()` 或 `copy.copy()` 会物化字典并永久关闭该特化，造成比 hoisting 节省更大的代价，`__slots__` 可避免此风险。

- 🐍 传统技巧仍有效：把 `self.value` 提升为局部变量，基准从 33.0 ms 降到 24.8 ms，比率 1.33 ± 0.04。
- ⚙️ 旧解释已过时：属性访问不再走实例 dict 和字符串哈希；自适应特化把 `LOAD_ATTR` 变成 `LOAD_ATTR_INSTANCE_VALUE`，从内联值数组按固定偏移读取。
- 🧪 无属性的 `Floor` 控制组显示，`hoisted / floor` 仅 1.02（GIL）和 1.00（free-threaded）：约 24 ms 是循环本身，8 ms 才是属性往返。
- 💥 仅读取一次 `o.__dict__` 就会物化字典，使同一循环从 33 ms 升到 50.6 ms；18 ms 惩罚是 hoisting 节省 8 ms 的两倍多。
- 📦 其他物化 `__dict__` 的操作包括 `vars(o)`、`'x' in o.__dict__`、`copy.copy(o)`；尤其 `copy.copy` 很隐蔽，会永久让该对象后续属性访问慢约三倍。
- 🧩 物化后的 dict 是 split table，`LOAD_ATTR_WITH_HINT` 会拒绝 split dict；`STORE_ATTR` 在 hint 路径被拒，`LOAD_ATTR` 更早因非 NULL dict 失败，最终回退到通用字节码。
- 🧵 一个物化实例不会永久“毒化”共享代码对象：干净实例会重新特化，干净实例跑过被毒化代码对象仅约 1.02x，无实质影响。
- 🪙 `__slots__` 与普通实例的属性读取速度几乎相同（0.98/1.00），其价值在于没有 `__dict__` 可被物化，因此不会掉出快速路径。
- 🔒 无 GIL/free-threaded 构建中循环本身略快，但属性访问更贵：特化往返 8.2 -> 10.1 ns，物化惩罚 17.6 -> 25.4 ns；读需原子加载与可能失败的 compare-and-incref，写需对象锁。
- ⚠️ 实践中，8–10 ns/轮只在数百万次且几乎不做别事的紧循环中显著；hoisting 往往收益微小，还可能让代码 diff 更差。
- ✅ 真正更值得关注的是物化：热路径中调用 `vars()` 或 `copy.copy()` 会悄悄触发；若对象频繁迭代，`__slots__` 是修复，因为没有 `__dict__` 就没有慢路径。
- 🕰️ 历史总结：3.11 前旧解释正确，因为属性确实走实例 dict；3.11 后改为版本守卫的 values array，free-threading 再加原子读和写锁。基准仍支持旧结论，所以原因长期未被重检。

---

### [](https://labs.quansight.org/blog/teaching-numpys-ufuncs-new-tricks?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Teaching NumPy's ufuncs new tricks | Quansight Labs](https://labs.quansight.org/blog/teaching-numpys-ufuncs-new-tricks?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

这篇博文回顾了作者在 Quansight 实习期间深入 NumPy 内部的工作：解释 ufunc 与归约机制，新增多输出归约和 `np.minmax`，引入 `segmented_reduce`，并将 `unwrap`、`searchsorted` 等函数改写为广义 ufunc；同时讲述了作者从高能物理研究者走向开源维护者的个人经历。

- 🧑🔬 作者是物理学家出身，曾在 CERN 的 CMS 实验做高能物理研究，并成为 Scikit-HEP 中 Awkward Array、Coffea 等工具的维护者。
- 🧩 NumPy 的 ufunc 是逐元素、固定输入输出、支持广播和类型转换的函数；其底层循环接收数据指针、维度和字节步长来遍历数组。
- 🔁 简单归约如 `np.sum` 实际复用 `np.add` 的前向 ufunc 循环，通过让累加器与输入/输出指针别名、累加器步长为 0 来“转向”实现。
- 🚫 旧版 `reduce` 只支持 2 输入/1 输出，因为多输出累加需要 N+1 个输入指针，无法直接复用 2-in/N-out 的前向循环。
- 🛠️ 新机制允许 ufunc 注册专用 reduction loop，签名为 N+1-in/N-out；N=1 时兼容旧单输出归约，N=2 时可支持 `minmax`。
- ⚡ `np.minmax` 通过新增融合 `minimummaximum` ufunc 和归约循环实现，一次遍历返回 `(min, max)`，支持 `axis` 等归约参数，并对整数/浮点做 SIMD 加速。
- 🧮 `segmented_reduce` 接受显式 starts/stops，可表达空段、重叠段、跳过元素和越界裁剪；空段使用 identity 或 `initial`，比 `reduceat` 更通用。
- 🧬 广义 ufunc 按子数组而非逐元素操作，签名如 `(n)->()`；它让非逐元素操作也能获得广播、dtype、`out` 和子类处理等能力。
- 🧹 `numpy.unwrap` 被改写为 gufunc `(n),(),()->(n)`，实现单遍 C++ 计算、避免临时数组，并保留 ndarray 子类。
- 🔍 `numpy.searchsorted` 正在改写为 gufunc `(n),(m?)->(m?)`，以支持 N 维输入和批处理，Python 层是否暴露 `axis` 仍待决定。
- ⏭️ 未来工作包括让 `reduceat`、`accumulate` 也使用专用归约循环，敲定 `segmented_reduce`，并探索单遍计算均值/方差等新归约。
- 🌱 作者因这次实习成为 NumPy 分诊团队成员，并计划继续参与 NumPy 开发，希望未来成为维护者。

---

### [如何阻止第三方 API 毁掉你的代码 - YouTube](https://www.youtube.com/watch?v=vskwNNdnqMc&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [How to Stop Third-Party APIs From Ruining Your Code - YouTube](https://www.youtube.com/watch?v=vskwNNdnqMc&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

這段內容是 YouTube 頁尾／導覽連結與版權資訊的集合，涵蓋平台介紹、聯絡、條款、私隱、安全、創作者與廣告等相關資源。

- 📖 簡介：提供平台或服務的基本介紹
- 📰 新聞中心：發布新聞、公告與媒體資訊
- ©️ 版權：說明版權相關規範
- 📞 聯絡我們：提供聯絡管道與支援方式
- 🎥 創作者：面向內容創作者的資源與資訊
- 📢 刊登廣告：說明廣告投放與合作方式
- 👨‍💻 開發人員：提供開發者相關資源
- 📜 條款：列出服務條款與使用規範
- 🔒 私隱：說明隱私政策與資料處理方式
- 🛡️ 政策及安全：涵蓋平台政策與安全指引
- ⚙️ YouTube 的運作方式：解釋平台運作與推薦機制等
- 🧪 測試新功能：提供新功能測試或實驗資訊
- © 2026 Google LLC：標示 2026 年 Google LLC 版權所有

---

### [](https://cohere.com/blog/megakernels?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Cohere's North Mini Code Megakernel Serving Engine | Cohere](https://cohere.com/blog/megakernels?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

overview summary
- 🚀 Cohere 发布面向 **North Mini Code** 的推理服务引擎，核心是 **decode megakernel**：在单张 H100、BF16 下，端到端比 vLLM 快 **1.25×–1.41×**。
- 🧠 传统 LLM serving 按算子逐个启动 kernel：QKV、attention、MoE 等都要等待，小 batch decode 时 GPU 大量时间耗在 kernel 之间。
- 📉 North Mini Code 是 **30B MoE**，每 token 激活 **3.3B** 参数；BF16 每步需流式读取约 **6.6GB 权重 + 0.5GB KV cache（8K 上下文）**。
- ⚡ H100 HBM 带宽 **3.35TB/s**，理论 Speed-of-Light 约 **470 tok/s**；vLLM 仅 **185 tok/s**，约为 SoL 的 **39%**。
- 🧩 Megakernel 把整个 decode 前向做成 **一个持久化 kernel**：每个 SM 常驻一个 threadblock，从全局内存中的任务列表取任务执行。
- 🔗 依赖同步改为 **全局内存计数器 barrier**：任务完成时递增，需要输入时自旋等待；调度粒度从整个算子缩小到单个 tile。
- 📦 设计统一 **ABI**：16 种 opcode、32 个 int32 任务描述符、固定 threadblock 形状，覆盖 GEMM、attention、MoE、RMSNorm 等。
- 🧵 每个 threadblock 有 12 个 warp，分为 3 个 warpgroups：controller、producer、storer、consumer，职责在编译期确定。
- 🏎️ 加速来源包括：减少启动/同步开销、降低 **wave quantization**、消除 **false dependencies**、利用不可变权重做 **weight prefetch**。
- 🔄 调度器采用静态 wave order + 动态 work stealing：attention 和 MoE 根据运行时序列长度与路由动态认领任务。
- 🖥️ 服务端由 Python 控制面负责请求、prefill、批管理与 KV，C++ 线程负责解码循环；通过 **park/resume** 切换所有权。
- 📊 Batch size 1 时 megakernel 达 **292 tok/s**，约为 SoL 的 **62%**，比 vLLM 快 **1.58×**；该优势跨 batch 和上下文长度保持。
- ✅ 准确性未明显损失：SciCode **38.9% vs 38.2%**，LiveCodeBench v6 **70.3% vs 70.3%**。
- ⚠️ 当前限制：不支持混合 prefill/decode，最大 batch size 为 **8**，megakernel 仅用于 decode，prefill 仍走普通 PyTorch kernel。
- 🛠️ 后续计划：扩展到 prefill、RTX Blackwell 的 FP8/FP4、数据中心 Blackwell 与多 GPU 推理。
- 📎 提供 OpenAI 兼容端点，支持流式、前缀缓存和工具调用；代码已在 GitHub 开源。

---

### [将 SQLite 变成用于 RAG 的向量数据库 - YouTube](https://www.youtube.com/watch?v=VlEoSzkd2gQ&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Turn SQLite Into A Vector Database For RAG - YouTube](https://www.youtube.com/watch?v=VlEoSzkd2gQ&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

這是 YouTube 頁尾的導航與版權資訊，涵蓋聯絡方式、創作者與廣告資源、開發者入口、法律政策，以及平台運作與測試功能。

- 🏠 基本資訊與聯絡：簡介、新聞中心、版權、聯絡我們
- 🎬 創作者與商業：創作者、刊登廣告
- 👨‍💻 開發者資源：開發人員
- 📜 法律與政策：條款、私隱、政策及安全
- ⚙️ 平台說明：YouTube 的運作方式、測試新功能
- ©️ 版權聲明：© 2026 Google LLC

---

### [Ruff、mypy、pytest，然后呢？——polyscan](https://codescan.dev/blog/ruff-mypy-pytest-and-then-what?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Ruff, mypy, pytest, and then what? — polyscan](https://codescan.dev/blog/ruff-mypy-pytest-and-then-what?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

本文讨论 AI 编写 Python 时的结构性质量问题：Ruff、mypy、pytest 能检查风格、类型与行为，却看不到跨函数的重复、复杂度趋势、死代码和依赖违规。作者用其维护的 pyscn 分析一个主要由 agent 编写的仓库，发现平均复杂度上升但健康评级不变，重复与依赖问题被常规工具链漏掉；最有效的改进是让 agent 在会话中直接调用结构检查器，并在 CI 中按增量设门禁。

- 🧭 Ruff、mypy、pytest 分别检查约定、类型和行为，但不做跨函数、跨模块的结构审查。
- 🧱 Agent 容易把同一逻辑写成多个近似 helper 或重复分支，后续修改时难以判断哪个是标准版本。
- 🔍 标准 CI 缺少对重复代码、死代码、依赖方向和复杂度趋势的检查。
- 🛠️ 作者维护 pyscn：开源 Python 结构分析器，检测克隆、复杂度、死代码和依赖规则，可作 CLI 或 GitHub App。
- 📊 对主要由 agent 编写的仓库做 5 个快照：平均复杂度从 6.9 升到 8.5，健康评级仍为 A，8/32 个函数复杂度≥10，重复率 0.4%。
- ⚠️ 只看健康评级会错过趋势；pyscn check 默认阈值会让这些函数失败，但项目从未在 CI 中运行 check。
- 🧮 最复杂的两个函数复杂度为 19：一个扁平校验梯子可接受，另一个 CSV 加载器有重复分支，体现 agent 的局部复制习惯。
- 🔗 依赖检查发现 AI 助手包直接导入最深层数值模块，绕过中间层，因为没有把架构规则写成可执行约束。
- ✅ 最有效的改进不是 CI 门槛，而是把检查器作为 agent 可调用的 MCP 工具，让它在上下文未丢失时合并重复。
- 🚦 CI 应按增量门禁：PR 新增超阈值函数或克隆组才失败，避免一次性大量问题导致检查被禁用。
- 📈 跟踪平均复杂度，而不只是最大值；把依赖规则写进 import-linter 等工具，让架构漂移更难发生。
- 💡 结构良好的代码对人和 agent 都更易读易改：每种事一种做法、小函数、单向依赖图，可降低后续开发成本。
- 🚀 试用方式：运行 `uvx pyscn analyze .`，或安装 GitHub App 定期审计并在 issue 中报告。

---

### [](https://inferencex.semianalysis.com/blog/tpu-inferencex-full-steam?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [TPU Inference Externalization Full Steam Ahead | InferenceX](https://inferencex.semianalysis.com/blog/tpu-inferencex-full-steam?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

本文是 SemiAnalysis 对 TPU 推理外部化的最新评测：TPUv7 Ironwood 在 InferenceX 官方预览中以 FP8 聚合推理对比 B200/B300，性能/美元最高领先约 50%；新原生 TorchTPU 栈、系统级协同设计、ICI/Torus 网络与后续路线图共同推动 TPU 从 Google 内部走向外部客户。

- 🏆 核心结论：TPU 外部推理“全速前进”，Ironwood 是 Google 首次用可购买/可租用的芯片争夺他人推理负载。
- 💰 性价比领先：在 100 tokens/s/user 下，Ironwood 约 $0.181/百万 token，低于 B200 的 $0.222 和 B300 的 $0.276，分别便宜约 19% 和 34%。
- ⚡ 高并发优势更大：20 tok/s/user 时 Ironwood 原始吞吐约 9,364 tokens/s/chip，略高于 B200/B300；结合 TCO 后每美元 token 数比 B200 高 50.4%，比 B300 高 96.0%。
- 🧮 内部 TCO 场景：按 Google 内部 $1.03/chip-hour 计算，并发 256 时 TPU 性能/美元比 B200 高 76.7%，比 B300 高 130.2%，但 TTFT 等延迟代价更明显。
- 📉 延迟权衡：在 20 秒中位响应时间下，TPU 约 $0.098/百万 token，仍比 B200 低约 8%，比 B300 低约 25%；B200 仅在约 30 秒中位响应附近的小区间可能反超。
- 🧊 FP4 差距：TPUv7 无原生 FP4，FP4 场景 NVIDIA 仍领先；TPUv8i 将原生支持 FP4，预计 Boardfly 可与 Rubin NVL72 竞争。
- 🧩 分离式服务：Google 内部 PD 分离已优化多年，但外部 TPU 栈尚未完全优化；GB300 NVL72 分离式对比 TPUv7 聚合式时，中段延迟约有 30% 性能/美元优势，预计 TPU 分离式优化后追平。
- 🕸️ TPU 扩展优势：TPUv7 pod 可通过低延迟 ICI 扩展到 1k+ 芯片，支持大模型分离式服务和超宽 EP，这是 NVL72 难以做到的。
- 🧠 软件栈演进：旧 TorchAX 把 PyTorch 翻译到 JAX，存在低层优化、分页注意力和 worker 模型适配问题；新 TorchTPU 让 TPU 成为原生 PyTorch 设备。
- 🚀 TorchTPU：使用 PyTorch PrivateUse1、私有 torch.Tensor 和 XLA/StableHLO/Pallas，保留 PyTorch 分布式与 eager/compile 路径；预计 10 月中旬 PyTorch Conference 前后开源。
- 🤝 生态合作：Inferact、RadixArk、Red Hat 与 Google 合作推进 vLLM/SGLang 的 TorchTPU 后端；TorchAX 将逐步弃用。
- 🛠️ DP Attention：TPU 后端支持 DP8+EP8，按请求切分注意力并本地保留 KV，避免专家权重复制，同时协调请求分配、循环状态槽和 block table。
- 📦 通信与 MoE 优化：合并 all-gather、把 ReduceScatter 放到 SparseCore、双缓冲重叠通信；GroupedGEMM v2、SparseCore ragged gather、小批量 one-hot permutation 和排序键优化显著降低延迟。
- 🔁 GDN 与混合模型：通过代数重排重叠 MXU/VPU、异步状态传输、GDN v3 融合 Conv1D 与 GDN，提升 decode/prefill/混合批处理；并优化混合 KV/循环状态的页式注意力。
- 🪶 低并发与前缀缓存：按活跃请求分桶元数据、缩小 rotary table、减少 padding、让 padding token 路由到 expert 0；混合前缀缓存为 GDN 分离读写槽，支持多轮/agentic 复用。
- 🧱 Ironwood 硬件：每芯片两个独立计算 die，经 die-to-die 连接；2 个 TensorCore + 4 个第三代 SparseCore；HBM 约为 Trillium 6 倍，是首代原生 FP8 TPU。
- 📐 MXU 形状敏感：256x256 脉动阵列要求维度对齐；Llama 3 8B 的 head dim=128 仅能达约 50% MXU 利用率，head dim=64 更糟，因此模型形状与 bring-up 成本高度相关。
- 🕸️ Torus 拓扑：Ironwood 延续 3D torus，基本单元为 4x4x4=64 芯片机架；通过 OCS 光交换扩展到 9,216 芯片 superpod、42.5 FP8 exaflops，并可秒级绕开故障链路。
- 🌐 TPUv8i Boardfly：TPU 8t 训练、8i 推理首次分架构；Boardfly 高基数网络把直径从约 16 跳降至约 7 跳，ICI 19.2 Tb/s，片上 SRAM 384 MB，原生 FP4。
- 🔮 下一步路线：优化投机解码/MTP、PD 分离、KV-cache offload；开源 TPU-Sync、支持 Mooncake Store/P2P 池化；扩展 Kimi K3、GLM 5.3、Gemma 4 与 AgentX TPU 评测。
- 🧾 TCO 模型：SemiAnalysis AI TCO Model 提供 TPUv7 BOM 与 TCO 估算；文章认为 TPU 外部化虽非一日建成，但正以极快速度推进。

---

### [跨服务边界的插件架构：使用](https://patrickm.de/plugin-architecture-across-service-boundaries-an-api-contract-with-pydantic-fastapi-pt-1/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Plugin Architecture Across Service Boundaries: An API Contract with Pydantic & FastAPI - Pt. 1](https://patrickm.de/plugin-architecture-across-service-boundaries-an-api-contract-with-pydantic-fastapi-pt-1/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

本文讲述一个内部 RAG 平台如何通过共享的 Pydantic 与 FastAPI API 契约，让外部团队以独立 REST 服务形式接入自研嵌入模型；平台在注册时探测并验证 /ready、/catalog 和 /encode/，兼容后才允许插件处理生产请求，从而在降低耦合的同时实现跨服务边界检查。

- 🧩 平台背景：团队运营内部 RAG 平台，负责生成 embeddings、存入向量数据库，并部署 RAG 容器供用户与自有数据交互。
- 🎯 需求变化：起初平台只提供自管文本嵌入模型，后来其他团队希望接入自有模型，尤其是视觉和音频等领域模型。
- ❓ 核心问题：不只是提供多少灵活性，而是插件服务如何在处理生产请求前证明自己与平台兼容。
- ⚖️ 方案权衡：比较了代码内插件、任务队列、REST API 共享契约；最终选择 REST API 契约，因为所有权清晰、边界兼容性可验证、复杂度较低。
- 🧱 契约设计：将 /ready、/catalog、/encode/ 的 Pydantic 模型打包为共享 API 契约库，发布到内部 Artifactory，插件作者安装并实现这些契约。
- 🔍 注册探测：平台收到 POST /register 后，会探测插件是否就绪、能否返回模型目录、能否完成测试编码，并验证响应是否符合约定模型。
- 📦 数据模型示例：如 EncodingInput、EncodingOutput、EmbeddingObject 描述输入、输出与 embedding 表示；FastAPI 使用 response_model 强制响应结构。
- 🧭 责任划分：平台管理内置模型的数据和向量表示；外部插件自行处理预签名 URL、批处理等，因为插件更了解自身模型限制。
- 🚀 开发者体验：三步接入——安装 plugin-embedding-service-contract、实现三个端点、调用 POST /register；还可用 openapi-generator 生成服务端桩代码。
- 🔐 认证与所有权：插件配置存入 MongoDB；读取或执行模型时会鉴权，更新和删除则检查资源所有者，并使用 FastAPI 依赖注入保持端点简洁。
- ⏱️ 周期探测：使用 Celery Beat 定期探测，检测插件宕机或契约漂移，并提供恢复模式，让恢复可用的模型重新激活。
- 🧪 测试策略：作者避免慢速的容器端到端测试，追求更快迭代；第二部分将介绍如何在不依赖容器 E2E 的情况下测试契约。
- 📉 结果收益：整体复杂度增加不多，耦合更少；团队停止容器后插件自动不可达，只需删除 MongoDB 注册记录，无需维护死代码。
- 💡 经验教训：平衡抽象与细节；让契约通过真实使用演进；迭代 API 资源设计，而不是一开始就追求最终版本。
- 🔮 下一步：可能引入服务发现，通过 Kubernetes Pod 标签自动发现并注册插件；但只有在插件数量很大时才更值得，当前 /register/ 能提供清晰反馈。
- 🧷 文章信息：发布于 2026 年 8 月 30 日，约 12 分钟阅读，属于系列第一部分，第二部分将展示契约测试方法。

---

### [](https://github.com/cloud-in-a-bottle/cloud-in-a-bottle?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - cloud-in-a-bottle/cloud-in-a-bottle: Deploy, use, and share web apps on a server you control. Your apps, data, and infrastructure stay yours. · GitHub](https://github.com/cloud-in-a-bottle/cloud-in-a-bottle?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

Cloud in a Bottle 是 Imbue 推出的开源项目（AGPL-3.0），目标是让用户在自控服务器上部署、使用和分享 Web 应用，使应用、数据和基础设施真正归自己所有；它提供从 Git 安装、Podman 构建、路由认证、HTTPS/DNS 到存储分层的完整自托管方案，也支持由 Imbue 托管配置后移交。

- ☁️ 项目定位：你的云端一角，在你自己控制的服务器上运行 Web 应用。
- 🏠 核心价值：应用、数据和基础设施保留在用户手中，不依赖有不同利益的公司。
- 📦 可部署内容：个人工具、AI 生成应用、开源软件、Matrix、Minecraft、笔记、项目管理、开发与创意工具，以及带 Dockerfile 和 `cloudinabottle.toml` 的容器化 Web 应用。
- 🚀 获取方式：可自行在自有硬件、本地虚拟机或云服务器上部署；也可由 Imbue 配置服务器并用你的 SSH 密钥移交。
- ⚙️ 工作原理：Python 路由器作为控制平面，通过仪表盘和 API 从 Git 仓库安装应用，读取清单，用 rootless Podman 构建 Dockerfile，并管理更新、日志与容器生命周期。
- 🌐 网络与认证：默认应用 HTTP 端口绑定主机回环接口，路由器按子域名代理 HTTP/WebSocket；应用默认需所有者认证，清单可声明公开路径；标准公网部署用 Caddy 处理 HTTPS，CoreDNS 提供泛域名 DNS。
- 💾 存储模型：分为永久数据、临时文件和归档存储，清单控制容器可访问层级；平台状态和永久应用数据存在实例上，归档可本地保存或使用 S3 兼容存储。
- 📚 文档：提供 Cloud in a Bottle 手册，包括平台概念、应用开发和运营指南，以及部署、创建应用和 `cloudinabottle.toml` 清单规范。
- ⚖️ 许可证：当前为 AGPL-3.0，未来可能转向类似 fair source 的许可证，意图是个人使用始终不受限制，商业使用可能受限以支持项目可持续发展。
- ⭐ 社区数据：仓库约有 1k stars、60 forks、4 个 issues、8 个 pull requests 和 1,165 次提交，是来自 Imbue 的开源项目。

---

### [](https://github.com/sapientinc/PRAXIST?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - sapientinc/PRAXIST: Autonomous research system for measurable, computer-executable research. · GitHub](https://github.com/sapientinc/PRAXIST?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

Praxist 是 Sapient Intelligence 推出的自主研究系统，面向“可度量、可由计算机执行”的研究问题，把已可运行的项目转化为持续、证据驱动的研究运行。它协调并行研究代理、任务自有评估、持久证据与代际综合，适合目标可度量、项目已可运行但最佳路径未知的场景；Codex 作为交互界面，Praxist 提供持久研究循环、调度与生命周期控制。

- ⚠️ 页面开头出现加载错误提示，需重新加载；以下总结基于其后展示的 README 与 FAQ。
- 🧠 Praxist 定位：自主研究系统，不是简单 AutoML 或调参工具，而是自导向研究团队式循环。
- 🔁 核心理念：研究是持续过程，跨代保留证据并合成下一阶段研究议程。
- 👥 并行研究同伴：同时探索竞争性假设与实现，直到收敛或预算耗尽。
- 📊 任务自有评估：指标、评估器、基线、协议和领域约束由任务项目定义，Praxist 不预设具体科学假设。
- 🗂️ 证据与综合：通过 incubator、frontier、Gems 等状态保留候选方案，并做多代证据综合。
- ⚖️ 多指标评估：按任务定义排序，支持 Pareto 最优权衡。
- 🌱 QD 与可选 DIG：保持多样性，帮助系统跳出局部最优。
- 🖥️ 资源调度与可恢复：根据资源压力调度实验，支持恢复、回放和监控。
- 🔌 插件边界：支持多运行时、模型提供商、工具、预算与工作流。
- 🚀 安装：pip 安装 praxist[agents,codex]，再运行 praxist setup --interactive --install-skills codex；Claude Code 有专用一行命令。
- 🧑💻 推荐通过 Codex 操作：Codex 负责交互与开发工具，Praxist 增加持久研究循环、证据协议、调度和生命周期控制。
- 🛠️ 接管流程：在可运行项目根目录调用 $praxist-takeover；检查就绪、创建/修复任务夹具、验证评估器与证据契约，通过门控后启动。
- 🧩 内置技能：包括 praxist-takeover-codex、onboarding、task-initialization、interactive-task-init、control、diagnostic、scientific-research、runtime-install、terminal-line-plot 等。
- 🕹️ 运行命令：praxist status --json、praxist --monitor --latest、praxist stop <run_id>、praxist resume <run_dir>；Ctrl-C 只关闭监控，不停止研究。
- 📦 示例与模板：praxist examples list/install；Rocket Booster Recovery 有 Python/JAX 与 Rust 两个参考实现。
- ✅ 要求：CPython 3.11+、可运行且可度量评估的项目、Codex/Claude Code 或直接 CLI、Codex 登录或支持的提供商 API key。
- 🧪 平台：Linux CPython 3.11/3.12 持续发布测试；macOS 等为兼容目标，研究前运行 praxist doctor。
- 🔐 安全与信任：项目隔离、掩码凭据、不收集实验数据；预注册、统一评估、端到端溯源保障改进可信。
- 💰 成本与模式：Codex-native 无需 API key；也可用自有 API key；成本取决于模型、并行度、代数和评估时间。
- 🧭 适用条件：目标可度量、项目已可运行、最佳路径未知；缺失前提会停止并说明，不会静默下载数据或伪造基线。
- 📉 无改进时：仍提供负结果证据包、审计报告及停止/转向建议。
- 📜 许可：Fair Source License 1.0，源码可见；年收入低于 100 万美元可免费商用，达到阈值需协商商业许可，学术/教学例外。
- ✍️ 输出署名：内部使用无需署名；对外发布需保留 “Praxist by Sapient Intelligence”。
- 📚 文档与引用：praxist docs 查阅文档；研究使用需引用 arXiv 2608.25955。
- ⭐ 仓库：sapientinc/PRAXIST 公共仓库，约 6.4k stars、610 forks、659 watchers。

---

### [GitHub - sgl-project/sglang：SGLang](https://github.com/sgl-project/sglang?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub](https://github.com/sgl-project/sglang?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

SGLang 是一个面向大语言模型与多模态模型的高性能推理服务框架，支持从单 GPU 到大规模分布式集群的低延迟、高吞吐部署；项目开源、社区活跃，已在全球超过 40 万块 GPU 上运行。页面开头虽有加载错误提示，但主体内容为 SGLang 的 GitHub 项目介绍。

- ⚠️ 页面顶部提示加载出错并要求刷新，其余内容为 SGLang 项目主页信息。
- 🚀 核心定位：高性能 LLM/多模态服务框架，兼顾低延迟与高吞吐，支持单卡到集群规模。
- ⚡ 快速运行时：RadixAttention 前缀缓存、零开销 CPU 调度、预填充-解码分离、推测解码、连续批处理、分页注意力、多种并行、结构化输出、分块预填充、量化、多 LoRA 批处理。
- 🧠 模型支持广：覆盖 Llama、Qwen、DeepSeek、Kimi、GLM、GPT、Gemma、Mistral 等，以及嵌入、奖励、扩散模型，兼容 Hugging Face 与 OpenAI API。
- 🖥️ 硬件支持广：NVIDIA GB200/B300/H100/A100/Spark/5090、AMD MI355/MI300、Intel Xeon CPU、Google TPU、昇腾 NPU 等。
- 🌍 社区与规模：开源且社区活跃，全球部署超过 40 万块 GPU，由 LMSYS 托管。
- 🔁 RL 与后训练：作为 rollout 后端，集成 AReaL、Miles、slime、Tunix、verl 等后训练框架。
- 🏢 企业采用：xAI、NVIDIA、AMD、Intel、LinkedIn、Cursor、Oracle Cloud、Google Cloud、Microsoft Azure、AWS、百度、阿里、腾讯等及多所高校采用。
- 📰 最新动态：持续为 Kimi K3、GLM5.2、DeepSeek-V4、Nemotron 3、gpt-oss 等新模型提供 day-0 支持，并推进 TPU、GB300、扩散模型、推测解码等方向。
- 📊 仓库数据：35.8k Stars、8.8k Forks、888 Issues、4.4k Pull Requests、18,071 Commits，采用 Apache-2.0 许可证。
- 🛠️ 入门资源：提供安装、快速开始、后端/前端教程、贡献指南、基准性能与发布博客。
- 📬 联系与赞助：企业合作或赞助可联系 sglang@lmsys.org；长期贡献者可获 Cursor、Claude Code、OpenAI Codex 等编码代理赞助。
- 🙏 致谢：设计参考并复用 Guidance、vLLM、LightLLM、FlashInfer、Outlines、LMQL 等项目代码。

---

### [](https://github.com/citry-dev/citry?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - citry-dev/citry: Fully typed frontend framework for Python with server events and Alpine.js, inspired by Vue and Livewire. · GitHub](https://github.com/citry-dev/citry?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

Citry 是面向 Python 的全类型前端框架，结合服务器事件与 Alpine.js，受 Vue 和 Livewire 启发，让组件能同时管理 HTML、浏览器行为、CSS、翻译和 Python 事件处理器，并可集成到多种 Python Web 框架中。当前 0.4 为公开测试版，配套文档、示例、VS Code 扩展、CLI 和 UI 组件库。

- 🧩 核心定位：以组件为中心构建交互界面，无需维护独立前端应用。
- 🐍 版本与兼容：支持 Python 3.10 至 3.14，0.4 为公开测试版。
- ⚙️ Web 框架集成：可与 FastAPI、Django、Flask、Starlette、ASGI、WSGI 应用配合，并提供挂载适配器。
- 📦 安装方式：可用 `python -m pip install citry`，或在 uv 项目中执行 `uv add citry`。
- 🧱 组件与模板：使用普通 Python 类定义组件，通过 HTML 风格标签组合；`<c-Name>` 渲染组件或控制流标签，`c-` 属性执行 Python 表达式。
- 🔒 类型安全：类型化输入可捕获拼写错误和缺失值，`template_data()` 决定模板可读取的数据。
- 🎨 前后端一体：组件可包含 CSS、JavaScript、Alpine 表达式、托管资产和错误边界。
- 🔁 服务器交互：支持服务器事件、表单、持久化 State 和定向 HTML 更新。
- 🌐 国际化：支持 Fluent 目录、区域感知格式化，以及服务器/浏览器翻译。
- 🚀 生产控制：提供缓存、HTML 片段、严格 CSP、CSRF hooks 和调试工具。
- 🧰 编辑器与 CLI：VS Code 扩展支持高亮、补全、导航、诊断和安全格式化；CLI 提供 `citry check` 检查组件契约和模板数据。
- 🧩 UI 组件库：`citry-ui` 提供可访问的表单、对话框、导航、反馈、数据展示、主题和翻译默认标签。
- 🧪 示例项目：提供 FastAPI、Django、Flask、ASGI、WSGI 启动模板，以及 Project Board 和 HTMX 集成演示。
- 📊 性能基准：Citry 热渲染 24.62 ms，约比 django-components 少 55% 时间；Django 为 11.67 ms，Jinja2 为 7.21 ms，但各场景输出与工作不同。
- 📈 仓库信息：`citry-dev/citry` 有 16 stars、2 forks、31 issues、1 PR、275 commits，采用 MIT 许可证，并延续 django-components 相关工作。

---

### [](https://github.com/eviking/numba-metal?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - eviking/numba-metal: Numba-to-Metal GPU compiler for Apple Silicon · GitHub](https://github.com/eviking/numba-metal?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

numba-metal 是 eviking 的开源项目，目标是让受限的 Numba 风格 Python kernel 在 Apple Silicon Mac 的 Metal GPU 上运行；它是真正的编译器后端，当前为 alpha/MVP，平台与语言支持都很窄，并明确避免静默回退到 CPU。

- 🚀 真编译器后端：将 Numba 类型化 IR 编译为 Metal Shading Language，再由 Apple Metal 编译器编译并在 GPU 执行，而非简单包装。
- ✍️ 用法示例：用 @metal.jit 定义 kernel，使用 metal.grid、metal.to_device、metal.device_array_like、[blocks, threads] 启动，配合 metal.synchronize 与 copy_to_host。
- 🍎 平台限制：仅 Apple Silicon Mac（arm64）、macOS 14+；需 Xcode 命令行工具和 Metal Toolchain；其他平台或系统版本会立即报错，不会回退 CPU。
- 🧩 支持范围：标量算术/比较/布尔、if/if-else、for range（支持 break/continue）、1D/2D 网格、1D 数组扁平化多维索引、部分数学函数；类型含 float32/int32/uint32/bool，也支持 float16/int64。
- ⚠️ 项目状态：alpha/MVP，只支持一个语言子集的一个方言和一个平台，不是 numba.cuda 替代品，不追求广泛 Python/NumPy 兼容。
- 📊 基准测试：9 个程序比较 Python、NumPy、Numba CPU 与 numba-metal，多尺寸、正确性检查、冷/热/含传输计时；仓库不硬编码加速数字。
- 🔍 Advisor CLI：终端静态扫描与性能分析工具；scan 只找候选不运行，compare 实际测量 CPU vs Metal 并检查正确性，只有 compare 能声称加速。
- 🛡️ 正确性策略：不支持的特性抛 UnsupportedFeatureError；float64 不用于 kernel 参数/数组 dtype，局部 float64 中间值窄化为 float32；禁用 Metal 默认 fast-math。
- 📄 研究报告：包含编译器架构、能力面、Apple Silicon roofline 演示，以及一个通过 500 随机测试却静默误编译生产 kernel、最终完全回滚的修复案例。
- 📜 贡献与许可：遵循 CONTRIBUTING.md，使用 BSD 2-Clause 许可证。

---

### [](https://github.com/netalertx/NetAlertX?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - netalertx/NetAlertX: Centralized network visibility and continuous asset discovery.  Monitor devices, detect change, and stay aware across distributed networks. · GitHub](https://github.com/netalertx/NetAlertX?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

NetAlertX 是一个面向家庭实验室、IT 团队、MSP 和分布式环境的网络可见性与资产情报平台，可在单一界面中持续发现设备、监控网络变化，并集中管理跨 VLAN、分支机构和远程站点的资产。
- 🛰️ 提供集中式网络可见性与持续资产发现，帮助识别影子 IT、未授权硬件和 IPAM 漂移。
- 🌐 支持跨远程站点、VLAN、分支办公室和分段网络监控，适合分布式网络环境。
- 🚀 可通过 Docker 快速启动，但需注意 docker-compose 近期有变更，应先阅读迁移指南。
- 🧩 支持多种发现与扫描方式，如 arp-scan、Pi-hole 数据库/DHCP 导入、通用 DHCP、UNIFI 控制器和 SNMP 路由器导入。
- 🔔 可向 80 多种服务发送通知，包括 Telegram、Apprise、Pushsafer、Pushover 和 NTFY。
- 🔗 可与 Home Assistant 集成，支持 API 端点、Webhooks，并可通过插件系统快速构建自定义扫描器。
- ⚙️ 工作流模块可自动化 IT 治理，如设备分类、清理策略、按厂商分组、重新归档或删除设备。
- 🏢 面向 MSP 和多站点监控，通过 Sync Nodes 汇总分布式采集数据，支持 NOC 墙板、Prometheus 指标和集中告警。
- 📚 提供 Docker、Home Assistant、裸机和 Unraid 等安装方式，并包含使用配置、API 和自定义插件文档。
- 🔒 默认将数据本地存储，不主动发送到外部服务；建议使用反向代理认证、防火墙限制、及时更新和 RBAC/SSO。
- ❓ FAQ 指出：监控 VLAN 或远程子网需正确配置网络访问和扫描方式；高可用推荐 Docker 持久化卷加反向代理。
- 🛠️ 排障提示包括：ARP 可能无法检测不同子网设备，Wi-Fi 网络可能需要替代扫描器，大型网络需通知节流，部分系统需 CAP_NET_RAW 等权限。
- 📈 项目数据包括约 7.1k stars、439 forks、31 watchers、6,712 commits、22 个 issues、3 个 PR，采用 GPL-3.0 许可证。
- 💙 项目感谢 Pi.Alert 等贡献者，使用 Weblate 进行翻译，并提供捐赠渠道；替代方案包括 Fing、NetBox、Zabbix/Nagios 和 Domotz。

---

### [](https://github.com/QwenLM/Qwen-Drive-1.0?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - QwenLM/Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving · GitHub](https://github.com/QwenLM/Qwen-Drive-1.0?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

Qwen-Drive-1.0 是 Qwen 团队与华中科技大学联合发布的面向自动驾驶的视觉语言基础模型，基于 Qwen3.5-4B 构建，在统一框架内整合了 3D 感知、视觉问答与运动规划能力，在多项驾驶及通用视觉语言基准上表现领先。

- 🚗 **模型架构**：保留 Qwen3.5 视觉语言模型架构，外接 BEV 感知头（负责 3D 检测、语义占用预测、BEV 地图分割）与规划专家（生成未来自车轨迹），LLM 解码器保持不变。
- 🎯 **统一框架**：将 3D 感知、视觉问答（通用与驾驶场景）和运动规划整合于单一模型，实现多任务协同。
- 🏋️ **分阶段训练策略**：结合驾驶专项监督与通用视觉语言数据，既获得驾驶专业能力，又保留广泛的视觉理解与指令跟随能力。
- 🔄 **统一数据管线**：将异构感知标注映射到共享标签空间、重新标注驾驶 VQA 响应以保证格式与事实一致、统一多数据集轨迹为航点表示。
- 📊 **规划性能**：NAVSIM v1.1 PDMS 达 88.2（SFT）/ 90.7（RL，best-of-6 为 91.4）；Waymo E2E RFS 为 7.78/7.91；NVIDIA PhysicalAI 开环 minADE 3s 为 0.34m/0.38m。
- 🗣️ **驾驶问答优势**：LingoQA 得分 77.8（官方 LingoJudge 下为 79.4），Ego3D RMSE 降至 7.78，多项指标显著超越 Qwen3.5-4B 基座及其他对比模型。
- 🧠 **通用能力保持**：在 MMBench、MMStar、MMMU、OCRBench 等通用基准上表现与基座相当，未因驾驶专项训练而明显退化。
- 🧭 **空间理解与定位**：EmbSpatial 78.9、ERQA 48.5、ODinW13 45.9，在同规模模型中处于领先水平。
- 📦 **模型发布**：可从 Hugging Face 或 ModelScope 下载，总大小约 9.1GB，包含 VLM 主体及 planner-sft、planner-rl、perception 三个子模块。
- ⚙️ **使用方式**：提供 `QwenDriveForPlanning` 接口加载模型与规划头；`planner-rl` 仅在推理式规划模式下使用，`planner-sft` 支持直接与推理两种规划。
- 🖥️ **环境要求**：推荐 24GB 以上显存的 GPU，支持 Python 3.10 环境，提供 demo 脚本快速上手。
- 📚 **文档齐全**：包含 cookbook、model、data、evaluation、perception 等文档，覆盖各推理模式与基准测试流程。
- 📜 **开源许可**：采用 Apache 2.0 许可证发布。

---

### [](https://github.com/changjonathanc/hip-agent?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - changjonathanc/hip-agent: A minimal coding agent harness that fits in the prompt · GitHub](https://github.com/changjonathanc/hip-agent?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

overview summary

hip-agent 是一个极简的编码代理（coding agent）外壳（harness），其核心理念"把外壳写进提示词"来自作者的博客文章。整个代理仅使用当前的 Codex 登录，向模型提供 sh 与 view_image 工具，接收提示词后循环执行工具调用，直到模型给出最终回复；由于提示词中写明了源码位置，模型可以读取甚至修改这套外壳本身。仓库以 MIT 许可开源，目前获得 12 个 Star。

- 🪶 **极简定位**：hip-agent 是一个最小化的编码代理外壳，`agent` 既是核心也是规范，几乎全部行为都由提示词定义
- 🧠 **运行机制**：使用当前 Codex 登录，为模型提供 `sh` 和 `view_image` 工具，接收提示词并持续运行工具循环，直至模型返回最终回复
- 🔁 **自我修改**：提示词告知模型源码所在位置，使其能够阅读外壳的工作方式并自行修改
- 🐍 **Codex 专属代码**：所有与 Codex 相关的实现都集中在 `codex.py`，包括基于 HTTP 的 Responses API 以及 Codex CLI rollout 格式的会话文件
- ⚠️ **安全警告**：命令在无沙箱、无审批检查的情况下直接执行，使用者需自行承担风险
- 🔒 **稳定性提示**：由 OAuth 支持的 Codex 端点属于私有 ChatGPT 后端，没有公开稳定性保证，可能随时变更
- ▶️ **运行要求**：需要 `uv` 和有效的 Codex 登录，运行方式如 `./agent "inspect this repository and explain it"`
- 📂 **会话记录**：对话以 Codex CLI rollout 形式保存在 `$CODEX_HOME/sessions`，其路径输出到标准错误，仅最终回复输出到标准输出
- ⏩ **会话续接**：可用 `codex resume <id>` 打开会话，或用 `AGENT_RESUME` 环境变量继续，包括由 Codex CLI 创建的会话
- ⚙️ **配置方式**：全部配置通过 `AGENT_*` 环境变量设置，`agent` 不读取其他任何配置，子代理像普通子进程一样继承这些变量
- 🤖 **默认模型**：`AGENT_MODEL` 默认为 `gpt-5.6-sol`，另有推理强度、服务层级、插件目录、恢复会话、token 压缩上限等变量
- 🧩 **插件协议**：插件遵循 Agent Plugins 协议，插件、`.agents/skills` 与 `~/.agents/skills` 中的技能会加入提示词；钩子遵循 Claude Code 格式，核心会运行 SessionStart、UserPromptSubmit、PreToolUse、PostToolUse 和 Stop
- 📦 **示例插件**：`plugins/` 提供三个示例——`environment`（加入 cwd、shell、日期和时区）、`agentsmd`（首轮加入最近的 AGENTS.md）、`cwd`（使 `cd` 在单次会话中跨命令保持）
- 🪆 **子代理设计**：子代理就是在 `sh` 中运行的 `agent`，拥有独立对话并继承其余一切，父级通过命令行上的变量进行配置
- 🚫 **模型范围**：项目专为 gpt-5.6 系列模型设计与测试，不计划支持其他提供商或模型，但代理可自行改造以适配

---

### [](https://github.com/pigeonlabsHQ/pigeon?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - pigeonlabsHQ/pigeon: Delegated authority for AI agents. A Pigeon Pass says what an agent may do. · GitHub](https://github.com/pigeonlabsHQ/pigeon?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

Pigeon 是面向 AI 代理的委托授权开源库，核心是用窄化、签名的 Pigeon Pass 取代直接复制 API 密钥给子代理，从而限制代理的权限范围与潜在影响面。

- 🐦 **问题背景**：主代理把同一 API 密钥交给子代理后，子代理便可部署生产、读取支付数据库、合并到 main 分支。
- 🔐 **解决方案**：向子代理发放 Pigeon Pass——一份限定其可执行操作的窄化签名凭证，而非完整的父级权限副本。
- ⚙️ **安装要求**：需 Python 3.12 或更高版本，通过 git clone 后执行 `pip install .` 即可安装。
- 🧩 **核心 API**：`grant(...)` 授予权限，`verify(...)` 校验操作是否被允许，示例中部署到 staging 通过、部署到 production 被拒。
- 📋 **拒绝详情**：`verify` 从不只返回布尔值，拒绝时会给出原因码、消息以及失败的比较信息（请求值 vs 允许值）。
- 🚀 **集成位置一（派生）**：在原本复制 API 密钥给子代理的地方改用 `delegate(...)`，向子代理发放 Pass。
- 🛡️ **集成位置二（工具）**：在产生副作用处（部署、查询、MCP 工具）调用 `verify(...)`，若被拒绝则不执行该工具。
- 🔒 **密钥保留原则**：真实密钥保留在运行器上，子代理只携带 Pass。
- 🚫 **防权限提升**：子代理无法新增能力、扩大资源、放宽上限或丢弃父级约束，否则抛出 `PRIVILEGE_ESCALATION`。
- 🔌 **MCP 中间件**：客户端为每次工具调用铸造更窄的 Pass，服务端在工具运行前验证；属于执行点而非协议的一部分。
- 🧭 **身份与权限之别**：身份说明代理是谁，权限说明它可以做什么。
- 💻 **CLI 工具**：提供 `pigeon keygen` 生成密钥、`pigeon inspect pass.json` 检查 Pass。
- ⚠️ **定位说明**：Pigeon 只是一个小型原语，不是平台、策略引擎、身份提供者或密钥托管方，也不能阻止提示注入，仅按 Pass 上的维度限制影响范围。

---

### [](https://github.com/gioblu/NPC-Forge?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [GitHub - gioblu/NPC-Forge: NPC-Forge is a framework for building conversational agents that run on the CPU without relying on machine learning or LLMs. · GitHub](https://github.com/gioblu/NPC-Forge?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

NPC-Forge 是 gioblu 的开源框架，用于在 CPU 上构建无需机器学习或 LLM 的确定性对话代理，支持个性、多轮上下文、情感分析和工具调用，并可兼容 OpenAI API。
- ⭐ 仓库数据：公开项目，229 Stars、14 Forks、3 Issues、1 Pull Request、168 Commits。
- 🧠 核心理念：无需机器学习或 LLM，也能构建高效、可控的对话代理。
- ⚡ 主要优势：确定性、不会幻觉或生成低质内容、无安全对齐过滤，毫秒级响应。
- 💻 硬件友好：可在浏览器、操作系统、嵌入式系统和老旧硬件上运行，仅依赖 CPU。
- 🛠️ 可靠扩展：比 NLP.js 更能容忍拼写错误、脏话、插入语和词序颠倒；数据集采用 NDF 0.0 格式。
- 🔄 无需训练：更新数据集后执行 `npc-forge reboot` 即可生效。
- 🔌 即插即用：实现 OpenAI 兼容 API，可连接 Open WebUI、Copilot 等工具，让 NPC 快速响应并执行工具调用。
- 🧰 CLI 命令：包括 `list`、`test`、`serve`、`stop`、`reboot`、`watch`、`create`、`install <path>` 等。
- 🤖 内置 NPC：TERMy 是首个内置 NPC，一个愤世嫉俗但知识渊博的 Linux 终端助手，可将自然语言转为 shell 命令。
- 🚀 快速开始：克隆仓库、进入目录运行 `setup.sh`、安装 `npcs/termy`，然后输入 `termy how are you`。
- ⚠️ 限制警告：实验版本仅支持 Linux 和 WSL，按“AS IS”分发，无任何担保，使用风险自负。
- 📚 文档内容：涵盖 TERMy、FlintParser、FlintNPC、CLI、API、NDF 0.0、TCS 0.0 和 NPC 创建指南等。
- 🌍 社区贡献：欢迎扩展数据集、创建新 NPC、优化框架；贡献者包括 Fred Larsen、Kevin Mathis、Cristiano Pizzarelli、David Starkweather。
- 📜 许可证：AGPL-3.0，可联系作者获取商业许可；主题包括 assistant、nlu、framework、terminal 等。

---

### [](https://www.meetup.com/psppython/events/316149969/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Python talk night at GitHub, Wed, Sep 16, 2026, 5:30 PM   | Meetup](https://www.meetup.com/psppython/events/316149969/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

GitHub Bellevue 办公室将举办一场 Python 演讲之夜，由 Andrew B. 和 Paul B. 主持，Puget Sound Programming Python (PuPPy) 组织；时间是 9 月 16 日周三 17:30–19:30 PDT。活动包含两场正式演讲、一场闪电演讲、交流时间和会后派对，并有多家赞助方支持食物。

- 🐍 活动名称：Python talk night at GitHub
- 📅 日期：9 月 16 日星期三
- ⏰ 时间：17:30–19:30 PDT
- 📍 地点：GitHub Bellevue，10900 NE 4th St Floor 21, Bellevue, WA
- 🤝 主持/主办：Andrew B. 和 Paul B. 主持；Puget Sound Programming Python (PuPPy) 主办
- 🍕 赞助：ActiveState、Slalom Consulting 为月度演讲夜提供食物；MotherDuck 赞助 2026 年 8 月演讲夜食物；活动注明 F5 networks 提供食物
- 🗓️ 议程：17:30–18:00 开门/交流；18:00–18:10 开场；18:10–18:35 演讲 #1；18:35–18:50 中场；18:50–19:05 闪电演讲；19:05–19:30 演讲 #2；19:30–19:40 结束致辞
- 🎙️ 演讲 #1：Tyrell Towle 讲 “Building TowleVision: A Local-First AI Media Production System in Python”，介绍本地优先、模型无关的 AI 媒体制作系统，协调旁白、图像生成、字幕、渲染、审核、修复和发布；讨论确定性编排、可替换本地 AI 后端、工件日志、定向重跑及 AI 编程工具的利弊
- ⚡ 闪电演讲：Ben Stickley 讲 “Learning Python: A Resource Overview”，简介待定
- 📊 演讲 #2：Ramkumar Hariharan 讲 “Aging in Pandas: Building a Biological Age Clock from Public Health Data”，用免费公共数据在 Python 中构建生物年龄估计器，理解 PhenoAge 数学并现场从零实现
- 💻 参加准备：演讲形式，无需带电脑
- 🛗 入场提醒：电梯 18:30 上锁，18:30 后到达不保证能进入
- 🅿️ 停车：大楼下方 Skyline 车库付费停车，经 110th Ave NE 在 4th 与 6th 之间南向单行进入
- 🚉 交通：靠近 Bellevue Downtown Link 站和 Bellevue 交通中心
- 🎉 会后派对：Lucky Strike Bellevue，700 Bellevue Way NE Suite #250, Bellevue, WA 98004

---

### [](https://www.meetup.com/phillypug/events/316182456/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [MicroPython & MicroServices, Thu, Sep 17, 2026, 6:00 PM   | Meetup](https://www.meetup.com/phillypug/events/316182456/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

本次活动是费城 Python 用户组（PhillyPUG）的第二次回归线下聚会，主题为 MicroPython 与微服务，包含两场演讲、披萨社交和演讲者招募。

- 📅 时间：9月17日（周四）18:00–21:00 EDT
- 📍 地点：宾夕法尼亚州费城 Walnut St 3730 号 Jon M. Huntsman Hall
- 👥 主办：Justin C. 和 Aaron N. B.，Philadelphia Python Users Group (PhillyPUG)
- 🍕 赞助：Wharton School、Linode、PromptWorks、Mozilla，提供场地、披萨和演讲者
- 🗓️ 议程：18:00–18:45 入场、餐饮与交流；18:45–19:00 欢迎与介绍
- 🐍 演讲 1：19:00–19:20 “MicroPython：概览与示例”
- ☸️ 演讲 2：19:20–19:40 “Kubernetes for Home Cooks”
- 🤝 19:40–20:30 自由交流、用餐、结识本地开发者，并招募未来演讲者
- 🎙️ Peter Sody：软件工程师/架构师，20 年 Python 经验，专注测试/质量、DevOps、安全、生产力工程、AI，也热衷 MicroPython 与 IoT/家庭自动化/机器人
- 🎙️ Jake Atwell：宾州本地人，7 年后端工程与数据科学经验，熟悉 Python 后端框架、NLP、数据管道、Docker/Kubernetes
- 📣 征集演讲者：欢迎提交想法，分享或教授有趣内容
- 🏷️ 相关主题：费城活动、Python、Docker

---

### [](https://www.meetup.com/pyladiesdublin/events/315877671/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [PyLadies Dublin @ Bentley Systems, Tue, Sep 15, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pyladiesdublin/events/315877671/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

overview summary  
PyLadies Dublin 将在 Bentley Systems 举办夏季后线下聚会，需提前在 Luma 注册；活动包含三场分享、项目交流与书籍抽奖，面向所有性别与水平开放，限 18 岁以上。

- 📅 活动时间：9 月 15 日周二，18:30–20:30 IST。
- 📍 地点：Bentley Systems，6th Floor, 1 Cumberland Place, Fenian Street, Dublin 2, D02 AX07。
- 🎟️ 必须注册：请通过 Luma 报名 https://luma.com/mrq6hjqr。
- 🧑🤝🧑 主办：Vicky T. 与 Michael T.，由 PyLadies Dublin 组织。
- 🙌 夏季休息后回归线下；Bentley Systems 主办并提供餐饮，需填写饮食要求。
- 🎤 Rose Farrell（ninedots / PyLadies Dublin 成员）分享爱尔兰就业市场与求职建议。
- 🐱 她的演讲主题：“Think Like a Cat: How to Stand Out in the Age of AI Applications”，讲如何在 AI 申请时代脱颖而出。
- 🧑💻 Riona Nazareth（Bentley Systems）分享“lxml for DITA Automation”，用 Python lxml 解析、查询和操作 XML。
- 💚 Anna Earley（Spunout.ie）谈职场与生活中的心理韧性，以及 Spunout 资源适合所有人。
- 🗓️ 日程：18:30 开始；18:40 欢迎介绍；18:50 Rose；19:20 Riona；19:40 Anna；20:00 Code & Network；20:30 结束，可能调整。
- 💻 带上笔记本电脑，可分享项目、向讲者提问或寻求帮助。
- 📚 Packt 提供书籍抽奖，包括《Python Illustrated: Not another boring Python book》。
- 💖 赞助与社区伙伴：Bentley Systems、Packt、Coding Grace、PSF、PyLadies。
- 🔞 活动仅限 18 岁以上，是专业社交活动，需遵守行为准则。
- 👥 欢迎所有人参加，不限性别与水平；鼓励带一位女性朋友或同事报名。
- 🗣️ 想演讲可提交 Sessionize；其他咨询可邮件 dublin@pyladies.com。

---

### [](https://www.meetup.com/pydata-milton-keynes/events/316072928/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [MCP Toolbox for Databases: Connecting AI Agents to Enterprise Data, Tue, Sep 15, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-milton-keynes/events/316072928/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

本次线上活动由 Philip O. 和 Grace F. 主持，属于 PyData Milton Keynes，主题为 MCP Toolbox for Databases：连接 AI 智能体与企业数据。Google Cloud 高级云架构师 Stenal P Jolly 将介绍这一基于 Model Context Protocol 的开源企业级服务器，帮助 AI 智能体、开发工具和生产应用安全、高效地访问结构化企业数据，而无需为每种数据库或应用自建集成代码。该工具支持 30+ 数据库引擎，并将通过实际演示展示如何兼顾安全、可扩展性与性能。

- 🎯 活动主题：MCP Toolbox for Databases——连接 AI 智能体与企业数据
- 👥 主办信息：由 Philip O. 与 Grace F. 主持，属于 PyData Milton Keynes 线上活动
- 🎤 主讲人：Stenal P Jolly，Google Cloud 高级云架构师
- 🧑💼 主讲背景：近十年软件工程、云架构、微服务和分布式系统经验；2021 年加入 Google，曾任职 Zoho、Cisco、Synamedia，并联合创办 Semantica
- 🧠 核心问题：生成式 AI 从聊天界面走向自主生产工作流后，AI 智能体如何安全高效地与企数据库交互
- 🛠️ 解决方案：MCP Toolbox for Databases，一个围绕 MCP 构建的开源、企业级服务器
- 🔐 主要价值：为 AI 智能体、开发工具和生产应用提供安全的结构化企业数据访问，无需为每个数据库或应用维护定制集成代码
- 🗄️ 支持范围：30+ 数据库引擎，包括 AlloyDB、BigQuery、Spanner、PostgreSQL、MySQL、Oracle、MongoDB 等
- 📊 演示内容：通过实际示例展示如何连接 AI 应用与数据库，同时保持安全、可扩展和高性能
- 👨💻 适合人群：数据工程师、软件开发人员、云架构师、AI/ML 从业者，以及构建生产级企业数据 AI 智能体的人
- 📚 相关主题：机器学习、大数据、数据科学、Python 数据科学、开源

---

### [](https://www.meetup.com/pydatachi/events/316414438/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

**原文标题**: [Models for SARS-CoV-2 health policies, Thu, Sep 17, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydatachi/events/316414438/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-762-september-10-2026)

这是一场由 PyData Chicago 主办的混合活动，聚焦 SARS-CoV-2 卫生政策建模，主题涉及疫苗接种和病毒变异背景下的社交距离措施，并以印度 2021 年 6 月至 2022 年 3 月的传播预测及 Omicron 早期预警为例。

- 🦠 活动主题：Models for SARS-CoV-2 health policies: Social Distancing amidst Vaccination and Virus Variants
- 🗓️ 时间：9月17日（周四）18:00–20:00 CDT，混合形式举行
- 📍 地点：地点待定；线上活动链接仅对参会者可见
- 💻 线上参会：Zoom 会议 ID 为 893 7923 0295，密码为 5t5WYn
- 🎙️ 主持与主办：PyData Chicago；主持人为 Justin Shea、Mehdi Jeddi、Erik Pak、Sou-Cheng Choi
- 📊 报告内容：介绍一个利用人群行为预测 SARS-CoV-2 传播影响的模型，覆盖印度 2021 年 6 月至 2022 年 3 月
- 🧮 建模方法：采用确定性人群分室模型，引入依赖报告确诊病例的人群行为动态传播因子，并纳入疫苗接种状态和病毒变异
- 🏛️ 政策应用：模型预测用于向印度政府 NITI AAYOG 提供抢先政策行动建议，并形成 Omicron 变体的早期预警预测
- 🤝 合作赞助：Adyen、UIC College of Business、PyData Chicago 共同主办；UIC 提供场地，Adyen 为现场参与者赞助披萨和软饮
- 🏢 其他赞助：AlphaSense、W W Grainger Inc、University of Illinois Chicago、Illinois Institute of Technology
- 🏷️ 相关主题：数据分析、医学与健康科学、Python、开源、政策
- 🗺️ 地址与后勤：待定（TBD）

---

