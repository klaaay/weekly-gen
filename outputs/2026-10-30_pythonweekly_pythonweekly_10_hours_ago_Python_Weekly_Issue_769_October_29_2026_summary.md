### [Python 的实验性 JIT 将被移除 [LWN.net]](https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Python's experimental JIT to be removed [LWN.net]](https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

CPython 的实验性 JIT 因未获得指导委员会批准的标准轨道 PEP 而基本走向终止：PEP 836 被撤回，相关代码预计将从主分支移除，后续是否由社区接手仍不确定。

- 🐍 CPython 于 2024 年为 Python 3.13 引入实验性 JIT，如今该项目的开发已基本停止。
- 🛑 2026 年 6 月，指导委员会暂停主分支上的 JIT 工作，要求提交标准轨道 PEP，明确维护承诺、兼容性、成功指标和时间表；否则将移除 JIT 代码。
- 📄 维护者起草了 PEP 836，但经过数月讨论后于 10 月 19 日撤回；作者表示没有足够精力继续推进当前版本，但仍相信自由线程支持、方法式前端等技术方向。
- 🧾 背景是 JIT 最初由 Brandt Bucher 添加，仅有信息性 PEP 744，未走正式标准轨道审批流程，后来引发流程与治理争议。
- ⚖️ 指导委员会关注支持计划、性能标准、平台一致性、用户可见行为差异、安全审查、持续兼容性测试以及更广泛的社区设计评审。
- ⏳ 委员会认为 PEP 将兼容性审查安排到 2028 年过晚，要求尽早并持续运行 PyPI 包测试。
- 🗑️ JIT 很可能很快从 CPython 主分支移除，以便在 Python 3.16 开发早期处理移除带来的问题；是否在其他地方继续开发取决于社区。
- 💬 评论普遍认为整个过程文明、善意，体现了 Python 社区处理分歧的方式。
- 🔍 评论讨论了 PyPy 等替代实现的局限、CPython C API 与 C 扩展兼容性使 JIT 特别困难，以及无 GIL 工作占用资源、优先级更高等问题。
- 🚀 有观点认为若 JIT 性能收益足够大，流程问题会更易解决；也有人认为需要速度的用户会转向 C、Rust 等编译扩展或其他语言。

---

### [Pylance + Pyrefly：将你首选的类型检查器引入 Visual Studio Code - Microsoft Python 开发者博客](https://devblogs.microsoft.com/python/announcing-tsp/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Pylance + Pyrefly: bring your preferred type checker to Visual Studio Code - Microsoft for Python Developers Blog](https://devblogs.microsoft.com/python/announcing-tsp/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

微软发布 Type Server Protocol（TSP），并与 Meta 合作让 Pyrefly 可作为 Pylance 的类型检查后端。Pylance 继续作为 VS Code 的 Python 智能层，Pyright 仍为默认检查器；用户可按需切换，同时保留补全、Quick Info、环境管理和 GitHub Copilot 集成。

- 🚀 TSP 是扩展 LSP 的开放标准，使任意编辑器或工具都能将类型检查器集成为一等后端。
- 🔀 Pylance 与 Pyright 实现解耦：Pylance 负责 IDE 智能体验，类型检查器成为可互换的静态分析组件。
- 🤝 微软与 Meta 合作设计并实现 TSP，确保 Pyrefly 完整支持，强调 Python 生态互操作而非碎片化。
- ⚡ Pyrefly 基于 Meta 大规模 Python 类型检查经验打造，检查速度达每秒 180 万行，并力求在 CI 与 IDE 中提供一致体验。
- 🧠 通过 Pylance 使用 Pyrefly 可保留 Copilot 相关能力，包括 AI 补全上下文、Copilot Chat 代码理解、MCP 工具及成熟 Python 工具链。
- 🛠️ 使用需 Pylance 2026.4.1 或更新版本；打开工作区后会自动检测 Pyrefly 安装或配置，并提示是否切换。
- ⚙️ 也可在设置中选择 Python › Analysis: Diagnostics Source，支持 Pylance、Pylance + Pyright、Pylance + Pyrefly；Pyrefly 最低版本为 0.60.0。
- 📊 启用后状态栏会显示 “Diagnostics Source: Pylance + Pyrefly”，点击可打开设置；用户可通过 issue、评论或 X 提交反馈。

---

### [Python热门图像库Pillow存在严重漏洞，可通过特制图像执行代码](https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Critical Flaw in Python’s Popular Pillow Image Library Allows Code Execution via a Crafted Image](https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

Pillow 是 Python 最广泛使用的图像库，其 EPS 图像处理存在严重漏洞：攻击者可通过控制文件名，让 Pillow 调用 Ghostscript 执行操作系统命令。该漏洞编号为 CVE-2026-112900，影响 Pillow 2.6.0 至 12.3.0，已在 13.0.0 中修复。Pillow 月下载量约 4.36 亿次，常出现在上传、缩略图、PDF 和机器学习流程中。13.0.0 还修复了多个 JPEG、TIFF 和内存安全问题，其中部分被评为严重级别，但目前尚无已知在野利用。

- 🚨 **核心漏洞**：CVE-2026-112900 源于 Pillow 处理 EPS 时未检查文件名便传给 Ghostscript，恶意文件名可被解释为指令并执行命令。
- 🎯 **攻击条件**：漏洞由文件名触发，而非 EPS 文件内容；上传接口若保留或根据用户输入生成文件名，风险更高。
- 🖥️ **影响范围**：仅当主机安装 `gs` 程序时才会触达 Ghostscript；影响 Pillow 2.6.0 至 12.3.0。
- 📦 **修复版本**：Pillow 13.0.0 于 10 月 16 日发布，修复全部相关问题；维护者评级为中等，GitHub CVE 评分为 9.2。
- ⚠️ **其他严重修复**：13.0.0 还修复 JPEG 解码溢出、FlashPix/FPX 命令执行、缩略图内存溢出及 TIFF 内存缓冲区溢出等问题。
- 🧪 **研究背景**：部分漏洞由 Anthropic 使用 Claude 研究开源软件安全时发现，并由 Ada Logics 人工验证。
- 🛡️ **升级建议**：立即升级至 `Pillow>=13.0.0`，并重建捆绑旧版 Pillow 的容器、wheel 或基础镜像。
- 🐍 **兼容性提醒**：Pillow 13 不再支持 Python 3.10，仍需使用 3.10 的环境需升级到 Python 3.11 或更高版本。
- 🧯 **临时缓解**：处理不可信上传的主机应移除 `gs`；避免对不可信 JPEG 使用 `draft()`/`thumbnail()`；谨慎处理内存中的 TIFF 保存路径。

---

### [tar-codec：一个快速且安全的 Rust 生态 tar 解析器](https://astral.sh/blog/tar-codec?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [tar-codec: a fast and secure tar parser for the Rust ecosystem](https://astral.sh/blog/tar-codec?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

overview summary：文章介绍 Rust 生态中的 tar-codec 解析器：uv 从 0.13 起用它解析源码分发包（sdist），速度约为旧实现 astral-tokio-tar 的两倍，同时通过严格状态机与分层设计降低 tar 解析差异和安全风险。

- ⚡ **背景与动机**：uv 需要处理 wheel（ZIP）和 sdist（tar）；旧 tar 栈经历多次 fork，曾收到安全报告，且 tokio-tar 系列设计过于宽松，修补成本高。
- 🧱 **tar 格式家族**：实际常见 V7、UStar/pax、GNU tar；tar 是 512 字节块格式，头部与成员数据交替，填充区没有强制内容，容易产生解析差异。
- 🧩 **pax 复杂性**：x/g 扩展头可覆盖成员头状态，存在全局/本地优先级、记录组合与“墓碑”删除语义；size/path 等状态还会影响解析框架本身。
- 🐃 **GNU 差异**：使用 base-256 数值编码和 L/K 扩展头处理长文件名/链接名；GNU 扩展可堆叠，但 tar-codec 限制每个成员最多一个 L 和一个 K。
- 🛡️ **安全设计**：解析前按 magic/version 锁定 tar 家族，拒绝混用；严格建模 pax/GNU 状态，拒绝空路径、全局 size 等无意义状态，遵循“保守接受、分层构造正确性”。
- 🏗️ **分层架构**：tar-framing 将块流转为物理/逻辑帧；tar-codec 负责内存或磁盘提取；archive-trait 提供统一 Archive/ArchiveBuilder 接口，并基于 cap-std 锚定提取目录。
- 🔍 **发现的差异原语**：包括 pax/GNU 状态机混淆、扩展优先级和墓碑处理错误、错误按换行切分 pax 记录、宽松整数解析等，均可能导致解析器不同步。
- 🚀 **性能优化**：编码/解码并非最难，优化校验和生成、pax 记录长度前缀计算、复用分配和批处理/缓冲，使速度约为旧实现两倍。
- ⚠️ **安全提取成本**：cap-std 目录能力跟踪有开销，缺少 openat2(2) 等系统调用时更明显，macOS 提取性能受影响。
- 🔮 **后续方向**：支持稀疏文件等细分 tar 特性；与社区改进其他 tar 实现（如 tar-minefield）；并计划用类似思路替换 uv 的 ZIP 解析。

---

### [超越LLM：面向AI智能体的Jev入门 - YouTube](https://www.youtube.com/watch?v=RdWmysdpkVA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Beyond LLMs: Getting Started with Jev for AI Agents - YouTube](https://www.youtube.com/watch?v=RdWmysdpkVA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

该内容为 YouTube 网站页脚导航与版权信息，主要列出平台介绍、政策条款、开发者与广告等入口，并附有 Google LLC 的版权声明。

- 🏢 包含“关于、新闻、联系我们”等平台信息入口
- 👥 提供创作者、广告、开发者相关链接
- 📜 列出条款、隐私、政策与安全、YouTube 运作方式
- 🧪 提示可测试新功能
- ©️ 版权声明为 © 2026 Google LLC

---

### [构建你自己的推理模型：完整视频课程](https://magazine.sebastianraschka.com/p/building-reasoning-models?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Build Your Own Reasoning Model: A Full Video Course](https://magazine.sebastianraschka.com/p/building-reasoning-models?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

overview summary
本文介绍 Sebastian Raschka 的《从零构建推理模型》视频课程：共 8 个视频、超过 11 小时编程内容，使用 Python 和 PyTorch，基于预训练 Qwen3 0.6B 模型，从评估、推理时扩展、强化学习到蒸馏，完整实现推理模型的关键方法，并说明推理模型与 LLM、Agent 的关系。

- 🎥 课程包含 8 个视频、11 小时以上内容，强调通过从零编码来理解推理模型的工作机制。
- 🧠 推理模型可视为传统 LLM 的升级版：通过带可验证奖励的强化学习等后训练方法，增强复杂问题求解能力。
- 🤖 推理模型是 Agent 的“引擎”，Agent harness 则负责上下文管理、工具调用和更复杂任务编排。
- 📚 配套书籍为《Build a Reasoning Model (From Scratch)》，建议按“读书—跟视频写代码—做练习”的方式学习。
- ⚙️ 前置要求是熟悉 Python 和 PyTorch；早期文本生成与评估可在 CPU 上完成，后续训练建议使用 GPU。
- 1️⃣ 视频 1 介绍课程动机、环境安装、硬件选择、CUDA/Apple Silicon 支持及远程 GPU 配置。
- 2️⃣ 视频 2 加载 Qwen3 0.6B 预训练权重，实现文本生成、流式解码、KV 缓存和 `torch.compile`。
- 3️⃣ 视频 3 构建数学答案验证器，用于 MATH-500 评估，并为后续 RLVR 提供奖励信号。
- 4️⃣ 视频 4 讲解推理时扩展：温度缩放、多项式采样、top-p 过滤和自洽性投票。
- 5️⃣ 视频 5 继续推理时扩展：评分函数、对数概率、平局打破以及自我反思/修订循环。
- 6️⃣ 视频 6 实现简化版 GRPO 与 RLVR 训练循环，包括生成推理轨迹、计算相对优势和保存检查点。
- 7️⃣ 视频 7 深入训练分析：优势与熵跟踪、裁剪策略比率、KL 损失项、格式奖励和奖励黑客问题。
- 8️⃣ 视频 8 讲解蒸馏：软/硬蒸馏、on-policy/off-policy，使用 DeepSeek R1 生成教师答案并训练小模型。
- 🧪 课程反复使用 MATH-500 评估基线模型、推理模型、RL 检查点和蒸馏模型的表现。
- 💡 作者鼓励学习时暂停视频、修改采样设置、检查失败答案并尝试自己的小实验。
- ⏱️ 另有一门约 90 分钟的 LinkedIn Learning 短课，可作为推理时扩展、强化学习和蒸馏的概念性预览。

---

### [Python 类型标注调查 2026：AI 工具与不断变化的检查器格局——Meta 工程](https://engineering.fb.com/2026/10/27/developer-tools/python-typing-survey-2026-ai-tools-checker-landscape/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Python Typing Survey 2026: AI Tools and the Shifting Checker Landscape - Engineering at Meta](https://engineering.fb.com/2026/10/27/developer-tools/python-typing-survey-2026-ai-tools-checker-landscape/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

2026 年 Python 类型调查共收到 1,794 份回复，显示类型提示使用率连续三年基本稳定，但类型检查器选择格局发生明显变化；库类型信息缺失仍是最主要困难，AI 工具在编写类型和修复检查错误方面的使用显著上升。

- 📊 调查显示 76.4% 受访者使用 Python 至少五年，85.5% 经常或总是使用类型提示，整体使用率与前两年相近。
- 🔄 类型检查器选择变化明显：49.9% 受访者选择两个及以上检查器，高于 2025 年的 46.0%；速度或性能是选择检查器的首要原因，占 56.5%。
- 🧩 第三方库缺少类型信息是最常见困难，占 65.1%；44.6% 表示类型系统无法完整描述代码行为，Django、SQLAlchemy、Pydantic、NumPy、pandas、Polars 被多次提及。
- ⚠️ 多检查器使用带来一致性问题：33.3% 受访者报告检查器间不一致，多静态检查器用户中该比例为 42.7%。
- 🤖 AI 工具更深入参与类型工作：42.5% 让 AI 编写类型提示，32.6% 用类型改进 AI 生成代码，61.0% 至少使用过一种 AI 辅助类型活动。
- 📈 认为 AI 能让生成代码更准确可靠的比例从 2025 年的 18.5% 升至 2026 年的 38.4%；24.4% 受访者称 AI 编码工具会调用检查器，其中 61.6% 还用 AI 修复检查错误。
- 🚨 受访者担忧 AI 生成类型过宽以及代理滥用 `#type: ignore`；29.8% 对类型在 AI 辅助编码中的价值表示“不确定”。
- 🧑‍💻 低频类型用户更受复杂性困扰：41.6% 认为类型系统过于复杂或冗长，高频用户中仅 14.5%；缺失库类型影响低频用户 36.2%、高频用户 70.0%。
- ✍️ 更好的 `Callable` 语法是最受期待的缺失功能，45.7% 选择；新检查器快速获得采用，Pyrefly 用户中 83.3% 同时选择其他检查器。
- 🖥️ 编辑器支持仍是核心：82.9% 在编辑器中运行检查器，VS Code 使用率 59.3%；可读性/文档是使用类型提示的首要原因，占 93.6%。
- 🔎 求助渠道变化显著：Stack Overflow 使用率从 46.4% 降至 22.9%，LLM 聊天从 26.0% 升至 41.7%，Python 类型文档升至 65.9%，检查器文档为 60.5%。
- 🗓️ 调查于 2026 年 8 月 5 日至 9 月 2 日进行，得到 Meta Pyrefly、JetBrains PyCharm、Microsoft Python、Astral/OpenAI ty 团队及社区贡献者支持。

---

### [](https://pypy.org/posts/2026/10/toy-bit-provenance.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [The Shift of Theseus — Toy Bit Provenance Abstract Domain | PyPy](https://pypy.org/posts/2026/10/toy-bit-provenance.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

文章介绍了一种面向玩具优化器的“位来源/位溯源”抽象域：它不只判断某位是 0、1 或未知，还能跟踪某一位是否来自另一个 SSA 变量的某一位，从而在很长的位操作链上发现等价关系并进行优化。

- 🧩 现有 KnownBits 抽象域擅长位运算重写，但无法识别位在指令序列中的移动，因此难以直接证明 `x & 0x0f` 与 `(x << 60) >> 60` 等价。
- 🔍 位来源域为每个 SSA 变量的每一位记录来源：常量 0/1，或某个操作的第几位，并可标记是否取反。
- 🧪 文章用 `x & 0x0f`、`x << 60`、`b >> 60`、`a & c` 的例子展示：分析后可得出 `result` 与 `a` 相同，直接化简为 `result = a`。
- ⚙️ 实现上使用 `SourceBit` 与 `BitProvenance` 数据结构，并定义 `invert`、常量移位、逻辑左/右移、`and/or/xor` 等转移函数。
- 🧠 二元位运算逐位推理，例如 `a & 0 == 0`、`a & a == a`、`a & ~a == 0`；无法表示时生成新的来源位。
- ✂️ 基于该分析可实现多类优化：常量折叠、识别恒等值、复用先前已计算的值，以及从来源模式中合成更简单的移位操作。
- 🔁 同一套规则还能发现多种重写，例如异或掩码抵消、打包后恢复低位、De Morgan 复用、字节交换两次还原、位反转—左移—位反转转为右移。
- 📊 在 Pydrofoil 与 PyPy JIT traces 上评估：Pydrofoil 中位来源优化去除约 44.59% 整数操作，接近 RPython JIT 的 48.16%，两者结合达 55.79%。
- 📉 PyPy 工作负载中位来源单独仅去除约 4.71%，且在 RPython 优化后再运行未带来额外收益。
- 🧭 相关工作总结了 LLVM Hexagon 的 BitTracker/HexagonBitSimplify、`collectBitParts`，以及 GCC 字节级字节交换识别和向位粒度扩展的未合入补丁。
- ✅ 结论是：少量转移函数即可跨任意长位操作链发现一族化简，而无需为每种组合手写 peephole 规则；完整代码见文章 gist。

---

### [面向 AI 系统的文本到图表：设计一种 LLM 能正确掌握的 DSL — zerowithdot / AI4CAD](https://zerowithdot.com/blog/text-to-diagram-for-ai-systems/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Text-to-Diagram for AI Systems: Designing a DSL an LLM Gets Right â zerowithdot / AI4CAD](https://zerowithdot.com/blog/text-to-diagram-for-ai-systems/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

本文介绍 Oleg Żero 在 DevAI 2026 主题演讲中提出的 Gnomon：一种面向 AI 系统的文本到图 DSL 及编译器。其核心是让 LLM 把自然语言翻译成受本体约束的 gnomocode，再由确定性编译器校验、生成图，并输出多视角图和可读文本，以解决架构讨论中术语含糊、LLM 生成图不可验证的问题。

- 🎯 问题动机：同一系统被不同角色从不同角度理解，LLM 能快速画图但结果每次不同、词义漂移、错误不可定位，缺少可审查、可版本化的共享语言。
- 🧭 方案选择：先尝试“直接让模型画图”、Pydantic 对象、UML/BPMN/C4/ArchiMate/SysML 等，最终选择“模型负责翻译、编译器负责裁决”的 DSL+编译器路线。
- 🧱 本体核心：从 RDF、SKOS、PROV-O、DCAT、DPV、QUDT、schema.org、OWL、SHACL 等借用词汇和规则，形成 57 个术语、12 个模块的小内核，且避免 copyleft 许可。
- ✍️ gnomocode 语言：用 `name: Type` 声明、`property = value` 陈述事实、`action(object)` 描述动作，支持流程 `>>`、数据流 `->`、分支 `|`/`&`、缩进嵌套和模块导入。
- 🌫️ 不确定性内建：`~0.5` 表示置信度；低于阈值不报错而作为待确认发现，图中保留为带注释陈述，便于查询未确认事实。
- ⚙️ 编译器实现：Python 3.14 + Lark LALR 解析，语法由本体生成；rdflib 构图、pySHACL 校验；诊断带行列、提示和 JSON 输出。
- 🔁 修复闭环：LLM 翻译为脚本，编译器报错回传并最多进行约三轮修复；评测中 54 篇文本最终全部编译，29 篇一次通过、23 篇需一轮、2 篇需两到三轮。
- 🚫 有效性原则：接受模糊但拒绝矛盾；类型错误、单值冲突、循环、互斥类型等会被定位并阻止，缺失信息转为警告/问题清单。
- 🖼️ 一模型多视图：同一编译图可按架构、流程、数据血缘视图展示，并面向高管、架构师、法务、安全、运维等受众过滤；可输出到 Gnomon 画布、Mermaid、LikeC4。
- 📊 评测结果：100 条原始主张经往返保留约 58 条；损失主要来自语言和黄金脚本（约 40 条），翻译器仅约 7 条，说明瓶颈在语言而非模型。
- 🧪 图与评审可信度：生成图对自身黄金图 F1 约 0.56，对无关文本约 0.29；LLM 评审有局限，两个评审模型在 6054 条主张上一致率 73%、Cohen’s kappa 约 0.55。
- 🖥️ 产品形态：Gnomon Studio 本地网页集成聊天、脚本与实时诊断、英文回读和架构图；后续消息增量扩展脚本而非重来。
- ✅ 结论与下一步：共享语言优于更漂亮图，本体承载词汇、规则、错误信息与视图；下一步包括开源仓库、写作约定、补充缺失词汇，以及从现有代码/图反向生成文本。

---

### [突破 AWS MCP Python 沙箱](https://xplo1t-sec.github.io/posts/breaking-the-aws-mcp-python-sandbox/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Breaking the AWS MCP Python Sandbox | xplo1t's site](https://xplo1t-sec.github.io/posts/breaking-the-aws-mcp-python-sandbox/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

AWS MCP Server 的 `aws___run_script` 工具会在 Lambda 沙箱中运行用户提交的 Python 脚本；作者利用 Python `match/case` 类模式隐式读取属性的特性，绕过 AST 校验与运行时代理限制，最终在 Lambda 内实现系统命令执行并获取执行角色临时凭据，但影响被限制在单次会话容器内。

- 🔍 **研究目标**：AWS MCP Server 提供 `aws___run_script`，允许 AI 代理在服务端 Lambda 沙箱中执行短 Python 脚本，以组合和过滤 AWS API 调用。
- 🧪 **测试方式**：作者自建 Python MCP 客户端，使用受限 IAM 用户直接枚举和调用工具，避免通过 AI 代理传递复杂 payload。
- 🛡️ **两层防护**：静态 AST 校验器拦截可疑导入、属性读取和调用；运行时替换 `builtins`、`type()`、`getattr()` 等为受限实现或代理对象。
- 🐛 **核心缺陷**：`match/case` 类模式会依据 `__match_args__` 隐式读取属性，AST 中只表现为 `ast.MatchClass`，不会出现敏感属性名，因此绕过校验。
- 🧩 **绕过技巧**：沙箱允许写入 `__match_args__`，且未禁止用 `chr(95)` 动态拼接 `__class__`、`__globals__`、`__import__` 等 dunder 字符串。
- ⛓️ **逃逸链**：`namedtuple -> __match_args__ -> __reduce_ex__ -> copyreg.__newobj__ -> type() 代理 -> __match_args__ -> __globals__ -> __builtins__ -> __import__ -> subprocess -> id`。
- 💻 **命令执行确认**：成功执行 `id`，返回 `uid=993(sbx_user1051) gid=990 groups=990`，证明突破 Python 沙箱限制。
- 🔑 **凭据泄露**：`env` 暴露 Lambda 执行角色的 `AWS_ACCESS_KEY_ID`、`AWS_SECRET_ACCESS_KEY` 和 `AWS_SESSION_TOKEN`。
- 🚧 **影响范围**：角色凭据对多数 AWS API 调用被显式拒绝，仅 `sts:GetCallerIdentity` 可用；未发现访问其他会话或客户数据，逃逸局限于本会话 Lambda 容器。
- 📚 **经验教训**：Python 实现同一目标的方式很多，AST 校验容易遗漏隐式行为；替换内置对象若行为不一致，也可能引入新绕过路径。
- 🗓️ **披露时间线**：2026-07-26 报告至 AWS VDP；07-30 由 HackerOne 验证并转交；09-15 AWS 确认修复中；10-23 标记解决；10-24 公开披露。

---

### [](https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Scanning 7.25 Million Public Repositories on China's Largest Git Platform for Secrets | MongoDB](https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

本文记录独立安全研究员与 MongoDB Kingfisher 团队合作，扫描 Gitee 的 725.6 万个公开仓库，发现 26,400 个唯一且已验证有效的凭证；Gitee 的凭证暴露密度高于 GitLab 和 Bitbucket 的公开扫描结果，且涉及中外多家科技公司。

- 🔍 **研究目标**：Gitee 是中国最大本土 Git 托管平台，API 限制较多，但仍是重要的凭证暴露面。
- 🛠️ **枚举方法**：结合官方用户搜索、Explore 信息流、用户项目/星标页面及内部 Elasticsearch 搜索组件，最终得到 7,256,531 个唯一公开仓库。
- ⚙️ **扫描管线**：使用 Modal 无服务器计算，Docker 镜像集成 TruffleHog 与 Kingfisher，对每个仓库进行 bare clone 并并发扫描。
- 📦 **规模与成本**：分 50 批、每批约 15 万仓库，以 350 个并发容器运行；耗时约一个月，总成本 3,097.64 美元，由 Modal 计算赞助覆盖。
- 🧾 **核心结果**：共发现 26,400 个唯一有效凭证；TruffleHog 发现 12,737 个，Kingfisher 发现 14,664 个，两者共同发现 1,001 个。
- ☁️ **主要泄露类型**：阿里云 AccessKey 最常见，约每 766 个仓库含 1 个有效阿里云凭证；还涉及 DeepSeek、OpenAI、HuggingFace、智谱、LangSmith 等。
- 📅 **时间分布**：绝大多数有效凭证在近两年提交，2025 年单独就有 12,242 个，接近总量一半。
- 🏢 **提交者特征**：多来自 qq.com、163.com、gmail.com 等个人邮箱；企业域名中出现华为、字节跳动、Google、Microsoft、Oracle、Apple、Meta、Anthropic 等。
- 📊 **平台对比**：Gitee 每千仓库 3.64 个有效凭证，高于 GitLab 的 3.11 和 Bitbucket 的 2.39；但仅用 TruffleHog 时为 1.76，需注意方法差异。
- 📨 **披露方式**：向暴露量最高的厂商提供协调报告和仓库元数据；未逐个通知开发者，因为厂商侧撤销更可靠；截至写作时撤销状态尚未确认。
- 🌐 **结论**：Gitee 是重要凭证暴露面，企业元数据横跨中外；该扫描架构可移植到多数 Git 主机，替换 clone URL 即可复用。

---

### [上下文工程现状](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [The State of Context Engineering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

overview summary
本文是2026年10月24日“Context Fails & Fixes”演讲总结，梳理上下文工程从“把一切塞进长上下文”到“让模型驱动harness并管理上下文”的演进，指出每次模型能力提升都会带来新失败模式；核心是理解context与weights共同决定输出，并在确定性代码与概率性模型之间做选择，把正确上下文给正确模型。

- 📈 长上下文并非万能药：2024年“RAG已死”期待百万/千万token，但更长上下文也会容纳更多错误。
- ☠️ 四类经典上下文失败：poisoning、distraction、confusion、clash；如Pokémon中模型被“茶”污染，反复寻找错误目标。
- 🧪 示例会压过指令：Do as I Say, Not as I Do显示反例越多，模型越可能跟随示例；Gemini 2.5在Pokémon上下文超10万token后开始重复旧动作。
- 🧰 六类修复工具：context augmentation、tool loadout、context quarantine、context pruning、context offloading、context summarization/compaction。
- 🧑‍💻 Harness工程：用DSPy演示agent本质是while循环，四类修复仅约16行代码；关键是把更多上下文组装工作从概率模型调用移到确定性代码。
- 🏷️ 术语演进但目标不变：prompt engineering→context engineering→harness engineering，都是为正确响应选择并组装正确信息。
- ⏳ 2026转向长时程agent：METR任务时长从GPT-5约3.4小时、Gemini 3.1约6.4小时到Opus 4.6约12小时，模型更强地驱动harness。
- ⚖️ 新失败“fighting the weights”：模型被训练环境和工具过拟合，如Claude Code系统提示反复强调并行工具调用；提示中的重复和大写常是抗衡训练偏置的信号。
- 🔁 新失败“context inertia”：模型过度执着于假设或子任务；Anthropic Memento每约1.5小时清空上下文但保留环境，Microsoft Fork-and-Flush与Berkeley“Scaling Discovery Requires Forgetting”也显示定期遗忘可提升表现。
- 🧹 实用建议：上下文约20万token是警告点，异常时先尝试重置或删除上下文，而非只怪模型“变笨”。
- 🔮 2027预测：个人agent长期运行会积累冲突技能与记忆，需要“strategic forgetting”；过度精确的记忆会随时间变乱。
- 🎯 核心结论：输出=context+weights；可换更大模型、增加推理或改善上下文，而改善上下文最便宜最快；目标是选择何时确定性、何时概率性。

---

### [获取失败](https://medium.com/@rongalinaidu/from-disk-pages-to-columnar-memory-why-apache-arrow-77d9147244cb?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Failed to retrieve](https://medium.com/@rongalinaidu/from-disk-pages-to-columnar-memory-why-apache-arrow-77d9147244cb?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

无法总结：获取内容失败，状态码 403。

---

### [用 998 美元训练 3.8B LLM 达到 0.384 CORE | Hugo Vergnes](https://hugovergnes.github.io/little-lm-3-8b/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [ Training a 3.8B LLM to 0.384 CORE for $998 | Hugo Vergnes ](https://hugovergnes.github.io/little-lm-3-8b/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

这篇文章回顾了作者以业余时间从零训练小语言模型的实践：在借鉴 nanochat 的基础上，用配置驱动的 little-lm 框架，以约 998 美元、43 小时在 8×B200 上训练出 3.848B 参数模型，CORE 得分 0.384，显著超过 GPT-2 1.5B 的 0.2565，并系统总结了架构、吞吐优化、消融实验与失败经验。

- 🕒 **更新 v1.1（2026-10-03）**：根据 Hacker News 与 Vision AI 的反馈改写了部分段落，补充了更多消融与实验。
- 🧠 **项目定位**：介于“nanoGPT 玩具”和“必须有大研究实验室”之间，证明个人用几千美元也能训练有意义的模型。
- 🏗️ **little-lm 框架**：YAML 配置驱动，组件自注册、按名称解析，替换优化器或数据集只需改一行配置；良好基础设施能快速回本。
- 🧩 **最终架构**：Llama 风格，RMSNorm、RoPE、GQA（24 查询头/8 KV 头）、relu² MLP、QK-norm、logit softcap、逐层可学习残差缩放、ResFormer 风格 value embeddings；28 层，总参数 3.848B。
- 💰 **核心结果**：3.8B 模型在 65.3B token 上训练 43 小时，成本 998 美元，CORE 0.384；1024 上下文版本为 57.3B token、35.9 小时、820 美元、CORE 0.338。
- 📊 **对比意义**：GPT-2 1.5B CORE 为 0.2565；nanochat d32 约 1B 参数、约 1000 美元、CORE 0.310；作者模型更大且略超其预算表现。
- ❗ **早期失败**：858M 模型在单张 A100 上训练约 5.8 天，PIQA 仅 60.45%，生成重复且无意义；问题包括余弦衰减过早、峰值学习率保守、全用 AdamW、数据选择一般。
- ✅ **五项关键改进**：梯形学习率调度、矩阵参数用 Muon 其余用 AdamW、改用 ClimbMix、FP8 + vocab padding、1024 上下文；训练吞吐约 480K token/s，GPU 92% SM 活跃、40% 占用。
- ⚡ **吞吐优化**：FP8 与 vocab padding 带来约 +33%；Liger  fused linear cross-entropy 单步慢 6% 但省 8GB VRAM，增大 batch 后累计 +44%；非门控 relu² 更快更省显存；bf16 master weights 在 1.5B 配置上提速 2.2×，质量代价很小。
- 🖥️ **硬件差异**：同一 FP8 代码下，150M 模型在 RTX 5090 为 184,662 tok/s，在 B200 为 477,440 tok/s，硬件本身带来 2.59×。
- 🚫 **未奏效的尝试**：flex attention 文档边界掩码、Liger RMSNorm/RoPE、nanochat 初始化均无明显端到端收益；流式数据集有网络风险，长训练应本地下载分片。
- 🔍 **value embeddings 消融**：占 19% 参数，loss 改善 0.46%、CORE 改善 3.2%，吞吐几乎不变；约等于多训练 1,200 步，且 CORE 对微小变化比 loss 更敏感。
- 🔍 **GQA 消融**：1.5B 规模下 GQA 训练快 12–15%，但 eval loss 差 1.0–1.5%；GQA 的真正优势在推理时 KV cache 更小；CORE 噪声较大，不宜用于区分微小差异。
- 📏 **上下文长度影响**：1024→2048 使 CORE 从 0.3384 升至 0.3840；SQuAD 和 boolq 因提示被截断而严重失真，两者贡献了 83% 的提升；其余 19 个任务合计仅 +0.008，且吞吐下降约 9%。
- 🧪 **局限与开放问题**：峰值学习率、调度、QK-norm 等未充分消融，部分继承自 nanochat；未来可研究 value embeddings 参数再分配、同墙钟下 1024 vs 2048、commonsense_qa 回退、优化器分片与数据探索。
- 🌍 ** closing thought**：GPT-2 曾是 2019 年大团队的前沿成果，如今个人用 998 美元和夜晚时间即可大幅超越；前沿整体前移，单人工程师已能做过去需要实验室完成的工作。

---

### [Jev 课程 – 仅预填充推理与从零构建决策模型 - YouTube](https://www.youtube.com/watch?v=aZglGvBPQGs&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Jev Course – Prefill-Only Inference & Decision Models from Scratch - YouTube](https://www.youtube.com/watch?v=aZglGvBPQGs&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

该内容为网站页脚信息，集中列出平台介绍、联系渠道、创作者与商业/开发者入口，以及条款、隐私、安全和功能测试等链接，并标注版权归属。

- 🏢 关于、新闻、版权与联系我们：提供平台背景信息及沟通渠道。
- 👥 创作者、广告与开发者：面向内容创作者、广告主和技术开发者的入口。
- 📜 条款、隐私、政策与安全、YouTube 运作方式：说明使用规则、数据保护、平台政策与运作机制。
- 🧪 测试新功能：提供新功能试用入口。
- ©️ 版权声明：© 2026 Google LLC。

---

### [UUIDv7 并不具备你所认为的那些特性](https://alexsci.com/blog/uuidv7-is-weird/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [UUIDv7 doesn't have the properties you think it does](https://alexsci.com/blog/uuidv7-is-weird/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

文章指出，UUIDv7 常被宣传的单调递增、可提取准确创建时间、不可猜测等特性，在 RFC 合规实现中并不严格成立；真正较可靠的只有唯一性与抗碰撞性。选用 UUIDv7 实现时，必须核对其额外保证、限制条件与时间戳处理方式。

- ⚠️ 许多博客夸大 UUIDv7 的单调递增、时间戳和不可猜测性，但 RFC 允许实现以多种方式偏离这些性质。
- 🕒 内嵌时间戳不保证等于对象创建时间；Postgres 文档和 RFC 9562 都提示时间戳可能被调整，甚至被提前到系统时钟之前。
- 🐍 Python 标准库 `uuid.uuid7()` 在计数器溢出或时钟回拨时，可能让时间戳持续领先系统时钟；高负载下偏差会无界增长。
- 🔒 UUIDv7 会泄露高精度时间戳：例如 URL 中的 ID 可能暴露账户创建时间，在特定场景下属于元数据泄露。
- 📈 跨节点严格单调排序不可能实现，因为系统时钟无法同步到足够精度；单节点上，无计数器的毫秒时间戳实现也可能生成乱序 ID。
- 🔁 生成器重启后若遇到时钟回拨，缺少持久化“最后使用时间戳”的实现会生成乱序 ID；作者查看的多个实现都未持久化该状态。
- 🧩 UUIDv7 更像多种思路的混合体，不同实现差异很大，且实现可随时间变化；分布式系统还可能混用多种实现。
- ✅ 唯一性与抗碰撞是唯一可较可靠期待的性质；选型时应询问：是否 RFC 合规、额外保证是什么、在什么限制下成立、何时修改时间戳、ID 有多容易被猜测。

---

### [Django 中的软删除，避免把项目搞得一团糟 | Code With Stein](https://codewithstein.com/django-soft-delete/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Soft delete in Django without making a mess | Code With Stein](https://codewithstein.com/django-soft-delete/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

本文讲解如何在 Django 中实现整洁的软删除：用 `deleted_at` 时间戳代替物理删除，通过自定义 QuerySet 和 Manager 默认过滤已删除记录，同时保留 `all_objects` 访问删除数据；并重点处理批量删除、唯一约束、恢复冲突、关联对象、Admin 与定期硬删除等容易出问题的环节。核心思想是软删除应默认隐藏但可显式访问，关联级联规则应放在业务层而非通用基类中。

- 🧭 软删除核心：`deleted_at=NULL` 表示活跃，有时间戳表示已删除；时间戳比布尔字段多记录删除时间。
- 🧱 基础实现：重写 `Model.delete()` 设置 `deleted_at` 并保存，`restore()` 将其置回 `None`。
- 🔍 查询过滤：默认 Manager 只返回活跃记录；`all_objects` 保留未过滤访问，用于后台、恢复和调试。
- ⚙️ Manager 配置：显式设置 `default_manager_name="objects"` 与 `base_manager_name="all_objects"`，避免关联对象访问被过滤破坏。
- 📦 抽象基类：将字段、管理器、`delete/restore/hard_delete` 放入 `SoftDeleteModel`，供多个模型复用。
- 💥 批量删除陷阱：`QuerySet.delete()` 不会调用 `Model.delete()`，需在自定义 QuerySet 中改为 `update(deleted_at=...)`，并提供 `hard_delete()`。
- 🧩 管理器复用：用 `Manager.from_queryset(SoftDeleteQuerySet)` 暴露 `active/deleted/restore/hard_delete` 等方法。
- 🔐 唯一约束：`unique=True` 会阻止复用已软删除值；改用条件 `UniqueConstraint(condition=Q(deleted_at__isnull=True))` 仅约束活跃记录。
- ⚠️ 数据库差异：条件唯一约束依赖部分索引；PostgreSQL/SQLite 支持较好，MySQL/MariaDB 会忽略条件。
- 🔁 恢复冲突：恢复可能因唯一值被新活跃记录占用而失败；先用服务层检查并抛出 `ValidationError`，数据库约束仍防竞态。
- 🔗 关联对象：软删除不触发数据库 `CASCADE/PROTECT/RESTRICT`；子对象处理应显式放在业务服务中，按业务决定是否级联软删或恢复。
- 🧾 关系访问：base manager 不过滤可保证 `invoice.customer` 等历史关联仍可读取；反向关系需测试 Manager 行为。
- 🛠️ Admin 与清理：Admin 可用 `all_objects` 显示已删除记录并添加恢复操作；管理命令按保留期 `hard_delete()` 清理旧数据，并重新考虑真实外键级联。
- 🧪 测试重点：测试默认隐藏、恢复、批量软删除、唯一约束、关联关系和清理流程，而非只测 `deleted_at` 是否写入。
- 🚫 适用边界：不要给所有模型加软删除；用户内容、项目、客户等有价值恢复的数据适合，临时日志、缓存等通常没必要。
- ✅ 设计原则：使用侧保持简单——`Project.objects.all()`、`delete()`、`restore()` 正常用，仅需处理删除数据时显式用 `all_objects`；复杂关系规则不要塞进通用基类。

---

### [阻止 Django 批量操作静默跳过信号 | Johnny Metz](https://johnnymetz.com/posts/django-bulk-operations-skip-signals/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Stop Django Bulk Operations From Silently Skipping Signals | Johnny Metz](https://johnnymetz.com/posts/django-bulk-operations-skip-signals/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

Django 的 `bulk_create()`、`bulk_update()` 和 `update()` 因绕过 `save()` 而静默跳过 `pre_save`/`post_save` 信号，可能导致缓存失效、审计日志、搜索索引同步等关键副作用悄无声息地丢失；文章提出用自定义 QuerySet 守卫让这些批量调用默认报错，并仅在明确需要性能时显式放行。

- ⚠️ **核心风险**：批量操作不会触发保存信号，且运行时没有警告；把循环 `save()` 改成一次 `update()` 看似性能优化，实则可能引入数据不同步问题。
- 🔍 **典型场景**：`post_save` 接收器负责更新搜索索引时，单条 `save()` 会重建索引，而 `bulk_create()`、`bulk_update()`、`update()` 不会，导致搜索结果与数据库漂移。
- 🧩 **解决思路**：自定义 `SignalSafeQuerySet`，重写 `bulk_create()`、`bulk_update()`、`update()`，默认抛出 `RuntimeError`，提示改用 `save()` 或显式放行。
- 🛡️ **管理器配置**：将守卫设置为模型的 `objects` 管理器，并通过 `Meta.base_manager_name = "objects"` 设为基管理器，以捕获反向外键 `add()`、级联删除 `SET_NULL` 等内部写入。
- ✅ **兼容良好**：`save()`、`create()`、`get_or_create()`、`update_or_create()` 仍正常工作；实例和 QuerySet 的 `delete()` 仍会发送删除信号；异步方法会调用同步版本，因此也会被拦截。
- 🔗 **多对多补充**：自定义多对多 `through` 模型若使用 `bulk_create()` 插入，也应配置 `SignalSafeQuerySet`，使 `add()` 触发守卫。
- 🚦 **显式放行**：需要批量性能时，用 `with allow_signal_skipping():` 包裹调用；反向外键 `add()` 可用 `bulk=False` 走逐条 `save()`。
- 🗑️ **删除需手动补偿**：删除发布者等会执行 `SET_NULL` 批量更新，需先收集受影响 ID，在放行删除后手动更新搜索索引等副作用。
- 🚫 **覆盖范围有限**：该守卫只保护 ORM，不覆盖原生 SQL 和数据迁移中的历史模型；更彻底的方案是数据库触发器或 outbox 表，但复杂度更高。

---

### [Python 中的访问者模式（以及更好的替代方案） - YouTube](https://www.youtube.com/watch?v=45MgUX_ih0s&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [The Visitor Pattern in Python (And Better Alternatives) - YouTube](https://www.youtube.com/watch?v=45MgUX_ih0s&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

该文本是 YouTube 网站页脚导航与法律信息列表，涵盖平台介绍、创作者/广告/开发者入口、条款隐私政策、功能说明及版权声明。

- ℹ️ 提供“关于、新闻、联系我们”等网站基本信息入口。
- ©️ 包含版权、条款、隐私、政策与安全等法律相关链接。
- 👥 面向创作者、广告主和开发者提供专门入口。
- 🧭 包含 YouTube 运作方式说明与测试新功能入口。
- 🏢 页脚标注 © 2026 Google LLC。

---

### [Django 作为简单的静态网站构建器 - Nanodjango](https://nanodjango.dev/blog/2026-10-static-site-builder/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Django as a simple static site builder - Nanodjango](https://nanodjango.dev/blog/2026-10-static-site-builder/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

文章介绍了如何用 Django 原生工具链构建静态站点：以 nanodjango 为核心，结合 django-nanopages 渲染 Markdown/HTML 内容，再用 django-distill 导出静态文件，从而兼顾静态站的易部署与 Django 的动态扩展能力。

- 🧩 Django 开发者过去常需借助非 Django 工具做静态站，现在可用 nanodjango、django-nanopages 和 django-distill 组成原生方案。
- 📝 通过 django-nanopages，只需几行代码即可将 `pages/` 目录中的 Markdown 和 HTML 文件映射为 URL，并渲染进基础模板。
- 🗂️ 页面文件支持 frontmatter，可指定继承模板、标题、作者等变量；HTML 文件也可作为 Django 模板使用标签和块。
- 🔗 可使用 `{% url "pages" "services/skills" %}` 等方式链接到具体页面文件。
- 🏗️ 使用 django-distill 可将站点构建为静态文件，命令为 `nanodjango manage website.py distill generate --output-directory=output/ --collectstatic`。
- ⚡ 借助 `uv` 和 PEP 723 依赖声明，可把站点构建脚本做成自包含脚本，用 `uv run website.py` 直接运行，无需预先创建虚拟环境。
- 🔄 可选用 django-style 提供默认基础模板，并用 django-browser-reload 实现 Markdown/HTML 修改后的浏览器热重载。
- 🛠️ 仍可使用 Django 的模型、视图和管理后台；在 `app.path` 中传入 `distill` 或 `distill_func`，即可让 django-distill 将动态页面也生成静态内容。
- 💾 可将 SQLite 数据库提交到仓库以保留内容数据，但应使用仅用于本地离线运行的占位密码，避免泄露常用密码。
- 🚀 若未来需要动态内容，可继续在现有基础上扩展，部署 nanodjango 脚本，或用 `nanodjango convert` 转换为完整 Django 项目。
- 🌱 该方案的核心优势是“从小到大逐步成长”：先从 Markdown 目录和静态构建开始，只在真正需要时增加复杂度。

---

### [错误](https://peter-hoffmann.com/2026/loading-peaks-on-demand-with-a-z10-tile-grid.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Error](https://peter-hoffmann.com/2026/loading-peaks-on-demand-with-a-z10-tile-grid.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='peter-hoffmann.com', port=443): Read timed out. (read timeout=30)

---

### [GitHub - google/elephant-goldfish-model：借助 AI 智能体设计和审查软件的开源技能 · GitHub](https://github.com/google/elephant-goldfish-model?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [GitHub - google/elephant-goldfish-model: Open-source skills for designing and reviewing software with AI agents · GitHub](https://github.com/google/elephant-goldfish-model?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

EGM（Elephant-Goldfish Model）是 Google 开源的一套 AI 代理软件设计与评审技能集：由掌握项目上下文的“大象”代理起草规范，再由零上下文的“金鱼”子代理进行挑战式评审，帮助团队在写代码前发现未言明的假设、盲点和实施风险，最终由人完成架构取舍与批准。

- 🐘 **核心理念**：Elephant 持有项目上下文并起草规范；Goldfish 在不了解此前对话的情况下评审文档与引用材料，暴露隐藏假设和盲点；You 负责权衡取舍并批准设计。
- 🛠️ **适用场景**：适合需要在实现前做设计决策的功能；小型、明确的 bug 修复仍使用常规编码流程。
- 📦 **安装方式**：支持 Antigravity、Claude Code、Codex，通过插件命令安装完整插件；安装后需开启新会话，Claude Cowork 和 ChatGPT Work 需参考设置指南。
- 🧭 **核心流程**：先 `/egm-brainstorm` 探索需求与权衡并生成 `concepts_brief.md`，再用 `/egm-draft` 生成 `design_draft.md`，最后用 `/egm-review` 进行多阶段评审。
- 🧩 **可用技能**：Brainstorm、Draft、Resolve、Bootstrap、Review、Review loop、Drift report，可按需单独使用，不必严格按完整顺序执行。
- 🔍 **评审机制**：评审需要全新的子代理上下文；若代理无法创建新上下文，EGM 会停止评审。评审关注设计清晰度、与代码的契合度及实施计划，但不能替代测试或人工判断。
- 👥 **项目影响**：据 README 介绍，已有数千名 Google 工程师使用；仓库约 5.9k stars、365 forks。
- 📄 **许可证与支持**：采用 Apache 2.0 许可证，且明确不是 Google 官方支持的产品。

---

### [GitHub - Gathin23/cleanyourtv：通过 Wi-Fi 精简任何 Android 或 Google TV，获得 Apple TV 风格的主屏幕。· GitHub](https://github.com/Gathin23/cleanyourtv?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [GitHub - Gathin23/cleanyourtv: Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home. · GitHub](https://github.com/Gathin23/cleanyourtv?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

CleanYourTV 是一个开源项目，可通过 Wi-Fi 对 Android TV/Google TV 进行去臃肿处理，并安装类似 Apple TV 的简洁主屏幕；它不 root、不刷机、不卸载应用，支持一键恢复，目前约有 45.5k stars、5.6k forks。

- 🎯 **项目定位**：通过 Wi-Fi ADB 禁用厂商遥测、广告服务、预装内容和无用应用，并获得 Apple TV 风格桌面。
- 📺 **支持范围**：Android TV/Google TV 支持完整去臃肿与启动器；Fire TV 仅支持去臃肿；Samsung Tizen、LG webOS、Roku、Vizio、Hisense VIDAA 不支持 ADB，只能关闭追踪。
- ⚙️ **工作原理**：开启电视开发者选项和 USB 调试，备份已安装包与设置，用 `pm disable-user` 禁用臃肿项，再安装小型原生启动器并设为默认 Home；所有操作可恢复。
- 🚀 **快速开始**：电脑需与电视同一 Wi-Fi，并安装 Python 3、JDK 17–22、Android SDK 34；克隆仓库后将 `PROMPT.md` 交给 Claude Code、Codex、Gemini CLI 等编码助手，约 15 分钟完成；也可手动运行脚本，或使用社区手机 App。
- 🏠 **启动器特性**：约 561 KB、纯 Java，面向 1 GB 内存电视和 Android 8+；提供黑色首页、圆角 Dock、顶部应用信息与环境光、应用网格、玻璃高亮、输入/Wi-Fi/设置按钮、时钟屏保、30 种语言和 RTL 布局。
- 🧰 **工具链**：包含纯 Python ADB 客户端、去臃肿/恢复脚本、固件更新后检查修复、隐私审计、主题推送、性能测试、截图对比、Docker 构建和 Windows PowerShell 脚本。
- 🛡️ **安全与恢复**：不刷机、不 root、不卸载；修改前记录状态到 `~/.cleanyourtv/`，恢复脚本可回放；脚本会保护 Home 应用，避免禁用唯一桌面；固件更新后可用 `check.py --fix` 恢复。
- 🔐 **ADB 安全**：网络 ADB 在 5555 端口为明文，使用后应关闭调试、撤销授权，并用 `adb-closed.py` 确认端口关闭；启动器在关闭调试后仍可工作。
- 👥 **社区贡献**：最有价值的贡献是提交自己电视型号的去臃肿列表；仓库已有大量型号示例，如 TCL 77、Sony 41、Xiaomi 34；`SHOWCASE.md` 收录 151 个相关项目。
- 📈 **项目热度**：2026 年 10 月发布父母电视清理前后对比后获得约 740 万浏览，四天内汇集 170+ 型号、200+ 贡献者；原名 `tv-vibehack`，采用 MIT 许可，与电视厂商无关联。

---

### [](https://github.com/HKUDS/DeepTutor?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [GitHub - HKUDS/DeepTutor: DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/. · GitHub](https://github.com/HKUDS/DeepTutor?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

DeepTutor 是 HKUDS 推出的开源、智能体原生的终身个性化辅导与学习工作台，将聊天答疑、解题、测验、深度研究、可视化、精通路径、沉浸阅读和音频概览整合到同一运行时与上下文体系；项目采用 Apache-2.0 许可，GitHub 约 50.1k stars、6.2k forks，当前版本为 v1.7.0，并提供官网与 arXiv 论文。

- 🎯 核心定位：以“终身个性化辅导”为目标，把辅导、解题、出题、研究、可视化与掌握练习连接为一个可扩展系统。
- 🧩 统一运行时：Chat、Ask Questions、Quiz、Research、Visualize、Solve、Mastery Path、Immersive Reading、Audio Overview 共享能力运行时与会话上下文，同时保留各自专用流程。
- 📋 任务管理：Task Board 支持 To do、In progress、Done、备注、拖拽或键盘操作，以及归档恢复，无需模型配置。
- 🔗 上下文复用：知识库、书籍、学习笔记页、收藏、题库、人格与 Memory 可在受权限和学习策略约束的工作流中复用。
- 🎥 沉浸视频学习：支持 YouTube、Bilibili 原生播放、字幕搜索、时间戳定位辅导、保存笔记与断点续学。
- 🤝 多智能体协作：可从聊天中调用 Claude Code、Codex、Grok CLI、Kimi 等外部代理或 Partner，并导入历史对话、运行 IM 伙伴。
- 📚 多引擎知识中心：支持 LlamaIndex、PageIndex、GraphRAG、LightRAG、WeKnora、腾讯 IMA、MarginNote 4、Kiwix、Obsidian 等，支持版本化索引与多种解析器。
- 🛠️ 工具与技能：内置工具、MCP 服务、CLI 应用、图像/视频/语音生成模型，以及可安装的社区技能。
- 🧠 可检查记忆：L1 轨迹、L2 表面摘要、L3 综合构成三层记忆，Memory Graph 可追溯证据与贡献来源。
- ✍️ 学习笔记本与 Book：笔记本支持页面/块、Dito 讨论、收藏证据与 Markdown/Word 导出；Book 将材料编译为可编辑的“活书”块。
- ⚙️ 设置与多用户：Settings 作为统一控制面，管理供应商、模型、语音、搜索、知识解析等；可选认证支持管理员、学习者、监护人与隔离工作区。
- 🚀 安装部署：提供 PyPI（full/core）、源码、Docker 单容器、仅 CLI 四种方式；v1.7.0 采用模块化安装并支持 `deeptutor init/start`。
- ⌨️ CLI 与自动化：`deeptutor chat/run` 支持交互 REPL 与 NDJSON 流式输出，便于其他代理把 DeepTutor 当作工具调用。
- 🌐 生态与社区：EduHub 教育技能市场与 ClawHub 兼容，导入经过安全门；项目有贡献指南、路线图和 Apache-2.0 许可。
- 📈 项目活跃度：仓库已有 3,155 次提交，发布记录从 v0.2.0 延续到 v1.7.0，持续迭代模块化、多引擎 RAG、视频学习与可靠性。

---

### [](https://github.com/anonnerdfrenzy/survival-llm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [GitHub - anonnerdfrenzy/survival-llm: A free AI assistant and survival library that runs on your own computer, with no internet needed. Shows the source of every answer. · GitHub](https://github.com/anonnerdfrenzy/survival-llm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

Survival LLM 是一个可在个人电脑上完全离线运行的免费 AI 助手与生存资料库，面向停电、急救、净水等应急场景，并会展示每个答案的来源以便核查。

- 🔒 **离线与隐私**：AI 模型和资料库都保存在本机，问题不会离开电脑；完成初始设置后无需互联网。
- 📚 **庞大的离线资料库**：约 150 万篇文章，涵盖 Wikipedia、WikiMed、MedlinePlus、CDC、FEMA、美军生存手册、USDA、wikiHow、iFixit 等；精简版约 50 万篇。
- 🔍 **答案可溯源**：每个答案列出所读文章，点击即可查看原文并高亮引用段落，还显示许可证。
- 🧠 **展示推理过程**：可展开查看 AI 的逐步思考、搜索和阅读内容；推理预算可设为关闭、1,000、4,000、16,000 tokens 或不限。
- ⚙️ **可调整行为**：可编辑系统指令、设置答案长度限制，并重置为默认值。
- 📄 **支持个人文件**：可导入 PDF、Word、EPUB、网页和文本文件，与内置资料库一起搜索；文件保存在本机。
- 🧾 **记忆功能**：可记住用户及家庭相关信息，支持查看、编辑、撤销，并可关闭 AI 自动保存。
- 🔄 **自动更新**：可检查并下载新版本，更新后保留模型、资料库、个人文件和设置。
- 💻 **安装要求**：安装阶段需要联网；支持 Apple Silicon Mac（macOS 14+）和 Windows 10/11 64 位；安装约 20 分钟至 2.5 小时，磁盘需求取决于模型和资料库大小。
- 🖥️ **按内存推荐模型**：128GB Mac 可选 80GB Nemotron Super；32–96GB Mac 可选 18GB Qwen3.8 27B；Windows 32GB+ 可选 25GB Nemotron Lightning；16–31GB 可选 6GB Granite 8B；8GB 电脑仅能搜索资料库。
- 📊 **模型评测**：用 22 个停电和急救问题测试，Nemotron Super 准确率 86%、0 个有害回答；Qwen3.8 27B 为 80%；Nemotron Lightning 为 77%；部分小模型因危险建议或循环问题未提供。
- 🧪 **引用核查**：模型可能编造来源，应用会核对它实际打开或看到的文章，并用真实阅读列表替换虚假的 “Sources” 行。
- 🏗️ **技术架构**：本地 Ollama 模型通过 `search_library`、`read_article`、`show_article` 工具检索 SQLite FTS5 全文索引和纯文本资料。
- 🛠️ **开发与构建**：可从源码运行、执行测试、构建资料库、打包 Mac/Windows 应用；代码采用 MIT 许可证，资料内容遵循各自来源许可证。
- ⚠️ **重要提醒**：AI 模型会犯错，但每个答案都显示来源，用户应自行核查。

---

### [](https://github.com/ClayGendron/wasi-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [GitHub - ClayGendron/wasi-python: A statically linked CPython for WebAssembly hosts (wasm32-wasip1) with numpy, pandas, scipy, and more compiled in. Built for running untrusted agent code server-side in web applications. · GitHub](https://github.com/ClayGendron/wasi-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

wasi-python 是一个将 CPython 3.15 静态编译为 WebAssembly（wasm32-wasip1）的单一二进制运行时，内置 numpy、pandas、scipy、scikit-learn、statsmodels、matplotlib 等 40 多个科学计算包，专为在 Web 应用服务端安全运行 AI 代理生成的不可信代码而设计。默认情况下，沙箱无文件系统、无网络、无进程启动能力，所有资源访问均需宿主显式授权并受配额限制。

- 🐍 **核心定位**：静态链接的 CPython WebAssembly 运行时，面向不可信代理代码的服务端隔离执行，一个二进制即可运行完整科学计算栈。
- 📦 **安装使用**：`pip install wasi-python`，要求 Python 3.11+，wheel 解包后约 250 MB，支持 Linux（x86-64/arm64）、macOS（arm64）和 Windows（x86-64），并已在各平台测试。
- 🔒 **安全沙箱**：客户机初始无文件、无网络、无进程；文件通过 `Grant` 授权，宿主函数通过 `tools=` 注入；客户机内存独立，无法持有宿主进程指针。
- ⏱️ **资源限制**：指令燃料（fuel）、截止时间（deadline）、内存、输出、打开文件数均有默认上限；超限时调用终止，结果中通过 `trapped`、`exit_code` 等字段说明原因。
- 🧪 **科学计算示例**：可在沙箱内运行 numpy FFT、scipy 曲线拟合、scikit-learn 聚类和 pandas 汇总等完整数据分析流程。
- 🛠️ **自定义工具**：用 `@tool` 装饰宿主函数并传入 `tools=`，客户机通过 `from host import tools` 调用；`gate=` 可在调用前审查，异常详情仅保留在宿主侧 `done.tools`。
- 🔁 **会话保持**：`Session` 类似 notebook 内核，跨多次调用保留导入和变量，支持空闲超时与生命周期限制，每个轮次独立计算燃料和截止时间。
- ⚡ **异步并行**：`run_async` 在 worker 线程运行客户机，多个客户机可并行执行且不阻塞事件循环，取消任务即可终止客户机。
- 🧩 **发布产物**：`python.wasm`（WASI reactor）、`python-snapshot.wasm`（预启动解释器加速首次调用）、`python-stdlib.zip`（只读字节码）及记录所有固定源码与工具链哈希的 `MANIFEST`。
- 🌐 **宿主兼容**：依赖 WebAssembly 异常处理提案；默认支持 wasmtime 47+ 和 WasmEdge 0.16+，wasmer、wazero、Node 24.15+ 需开启相应开关。
- 🔧 **可复现构建**：一条命令从固定输入构建，所有源码按 URL 下载并校验 SHA-256，发布由构建工作流签名，可验证下载。
- 🤖 **代理开发背景**：v0.1.0 由 Claude Opus 与 Fable 代理在 2026 年 10 月 16–22 日六天内构建，421 个会话、1,255 次提交，每次变更先规格化、独立 worktree 实现、新代理审查并通过测试。
- 📄 **许可证**：Apache-2.0；产物集按组件分别附带许可证文件，wheel 的 LICENSE 汇总全部许可文本。

---

### [GitHub - soasme/small-python：一个简单的 Python 解释器。 · GitHub](https://github.com/soasme/small-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [GitHub - soasme/small-python: A simple Python interpreter. · GitHub](https://github.com/soasme/small-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

Small Python 是一个用 C11 编写的小型、可嵌入 Python 引擎，可在只有 C 编译器和 C 标准库的环境中运行 Python 3.15 代码，设计风格类似 QuickJS，构建和运行都不依赖 CPython。

- 🐍 核心语言支持较完整：任意精度整数、Unicode、类与元类、生成器、async/await、模式匹配、f-string 和模板字符串。
- 📦 易于嵌入：只需一个头文件 `spy.h` 和一个库 `libspy.a`，每个上下文相互独立，无全局状态。
- 🧠 自动内存管理：采用引用计数加循环回收器。
- 🏗️ 可生成独立可执行文件：`spyc` 能把 `.py` 文件转换为 C 程序。
- 🔒 文件访问受限：脚本只能打开宿主挂载的目录，具备沙箱化文件能力。
- ⚡ 启动速度快：在 Apple M2、`-O2` 下，创建上下文、运行 hello world 并销毁约需 260 微秒。
- ✅ 规范一致性：实现 PLS-315 的 Core profile；357 个规范测试和 112 个 TLA+ 模型全部通过，并与 CPython 3.15 对照检查。
- 📚 范围明确：实现语言核心与内置功能，标准库不在范围内；PLS-315 是项目文档，并非官方 PSF 标准。
- 🚀 使用方式：`make` 构建后可用 `./spy examples/hello.py` 运行脚本，或 `./spy -i` 进入交互式 Shell；也可用 `spyc` 编译为独立程序。
- 🔌 多语言集成：提供 C 嵌入 API；Python 包 `small_python` 在独立 worker 进程中运行运行时；Rust crates 在 `cargo build` 时通过 `cc` 从源码编译引擎，并提供安全 API 与 serde 转换。
- 🎮 示例丰富：包括 raylib 游戏 `pong`、将游戏包与引擎静态链接的 `flappy`，以及基于 axum 和 serde 的 Flask 风格 `todo` 应用。
- 🧪 测试与文档：支持 C API 测试、规范测试、AddressSanitizer、启动基准和 Rust 测试；文档涵盖手册、基准、PLS-315、`spyc` 打包器、Cython 兼容性基线等。
- 📄 许可证：MIT，第三方声明位于 `docs/licenses`。

---

### [](https://github.com/synapse-ai-hub/Forge?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [GitHub - synapse-ai-hub/Forge: Open-source Python framework to build, orchestrate and deploy AI agents: multi-provider, tool calling, RAG memory and desktop distribution. · GitHub](https://github.com/synapse-ai-hub/Forge?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

synapseForge 是一个开源 Python 框架，目标是让开发者像“锻造系统”一样创建、编排和部署自主 AI 智能体，而不是只拼装提示词。它集成多模型提供商、工具调用、RAG 记忆、工作流、权限安全，并支持 Docker、桌面应用和便携 ZIP 分发。

- 🛠️ **核心理念**：以系统化方式构建智能体，覆盖 FORGE（定义）、EQUIP（装备）、RUN（运行）、SHIP（分发）全流程。
- 🧩 **构建模块**：支持 Agents、Skills、Tools、RAG 集合和 Workflows，可通过 LLM 辅助访谈生成智能体能力。
- ⚙️ **Forge 运行能力**：内置权限引擎、安全规则、AgentLoop、流式 SSE、工具调用、工作流 DAG、长期记忆和多提供商 LLM。
- 🔐 **安全与权限**：默认拒绝、按智能体授权，支持通配符和分组；可启用决策模型作为护栏，拦截提示注入、数据泄露和危险命令。
- 🔄 **工作流引擎**：YAML 定义确定性 DAG，支持并行节点、后台运行、重试、结果持久化、通知和定时调度。
- 🧠 **RAG 与记忆**：使用 ChromaDB 和 Gemini embeddings 建立知识库，支持文件/网页索引、可配置分块，并自动索引对话用于跨会话检索。
- 🌐 **多提供商与 MCP**：支持 Ollama 本地模型、Google、OpenAI 兼容云提供商，以及 MCP 外部工具服务器接入。
- 🚀 **快速开始**：通过 `pip install synapseForge` 安装，使用 `synapseForge init` 创建项目，`synapseForge run` 本地开发，`synapseForge launch` 构建桌面应用或便携包。
- 🖥️ **技术架构**：后端为 FastAPI + Agent Framework，前端为 React/Vite/TypeScript SPA，使用 Tailwind 和 shadcn/ui。
- 📱 **Telegram 与定时任务**：可通过 Telegram 远程控制智能体、切换模型、创建技能/工具和管理定时任务。
- 💰 **用量与计费**：跟踪月度请求、Token、费用和按提供商/模型明细，可设置支出限额并在达到上限时阻止请求。
- 🧪 **测试与部署**：提供声明式 E2E 测试、工作流/检查点/提示词/MCP 等测试套件，并支持 Docker 单容器或仅后端部署。
- 📜 **开源许可**：项目采用 Apache-2.0 许可证，由 SYNAPSE AI SAS 维护。

---

### [GitHub - AdilZouitine/ploom：用于 Python 的并发排列测试工具。· GitHub](https://github.com/AdilZouitine/ploom?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [GitHub - AdilZouitine/ploom: Concurrency permutation testing tool for python. · GitHub](https://github.com/AdilZouitine/ploom?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

Ploom 是一个面向 Python 的并发排列测试工具，通过在受控调度器下运行测试，系统探索线程交错顺序，定位并保存导致失败的调度，再通过 JSON trace 精确重放，帮助复现和修复依赖线程执行顺序的缺陷。

- 🧵 Ploom 使用 `ploom.Thread` 等受控操作，尝试不同线程执行顺序，在首次失败处停止并保存 trace。
- 💥 示例中，共享账户的两次取款因未加锁产生交错，导致余额透支；Ploom 能在数秒内找到坏顺序并生成最小化 trace。
- 🔐 在余额检查和取款期间加 `ploom.Lock` 后，示例中的 127 种顺序全部通过。
- 🧪 支持 pytest fixture `ploom_check`，可在测试中探索场景；失败时打印重放命令。
- ⏯️ 可用 `--ploom-replay` 重放保存的调度；若源文件、Python 次版本或记录操作变化，会抛出 `ReplayDivergenceError`。
- 🎯 支持 `checkpoint` 和 `Config(ordering=...)` 约束事件顺序，便于复现疑似调度。
- ⚙️ 每个 ploom 操作都是调度点，一次仅一个任务运行；采用深度优先搜索，每个调度在全新 Python 进程中执行，并最小化失败 trace。
- ⚠️ 搜索有上限，超限会抛 `IncompleteExplorationError`，且上限不算通过；每个调度约 0.1 秒，建议保持场景较小，可用 `max_preemptions` 限制探索。
- 🧰 覆盖线程、锁、Event/Condition/Semaphore、FIFO Queue、SharedCell 等；支持 CPython 3.13/3.14 及 free-threaded CPython 3.14。
- 🚫 仅建模 ploom 操作并假定顺序一致性，不覆盖原生 `threading`/`queue`、I/O、弱内存效应，不检测数据竞争，也不回滚外部副作用。
- 📦 安装方式为 `uv add --dev ploom` 或 `pip install ploom`；项目采用 Apache-2.0 许可，并受 Rust Loom 启发。

---

### [Python 3.15.2、3.14.10、3.13.18、3.12.16 和 3.11.18 已发布 | Python Insider](https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Python 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18 are out | Python Insider](https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

Python 于 2026 年 10 月 26 日发布 3.15.2、3.14.10、3.13.18、3.12.16 和 3.11.18 紧急安全版本，重点修复被攻破的 eMudhra 中间 CA 密钥问题，并建议所有受影响用户尽快升级。

- 🚨 这五个版本都是紧急安全发布，主要用于应对 eMudhra 中间 CA 密钥被攻破的风险。
- 🔒 `ssl` 模块将相关密钥列为不信任，作为最后防线；正常使用 `pip`（包括升级 `pip` 自身）现已免受基于这些密钥的攻击，即使 `pip` 尚未更新。
- 💾 Python 3.15.2 和 3.14.10 提供二进制安装程序；3.13.18、3.12.16 和 3.11.18 是仅提供源码的安全版本。
- 🧩 所有五个版本共同修复：CVE-2026-115557 / gh-160040，不信任被攻破的 eMudhra 中间 CA 密钥。
- 📦 同时修复：CVE-2026-114583 / gh-160097，拒绝 `tarfile.tar_filter` 中替换目标位置的链接；gh-160300，拒绝 `http.cookiejar` 中版本号为负的 Cookie。
- 🛡️ 3.13.18、3.12.16、3.11.18 额外包含已在 3.15.1/3.14.9 修复的内容：CVE-2026-77214 与 CVE-2026-102633 / gh-158876，将内置 Expat 更新至 2.9.0。
- 🪟 上述三个版本还包含：CVE-2024-3220 / gh-159428，Windows 上默认不读取 `mimetypes.knownfiles`；gh-87720，修复额外的头部重折叠/引号边界情况。
- 🧵 3.13.18 与 3.12.16 额外修复：gh-157579，`tempfile.TemporaryDirectory` 清理中的竞态条件（已在 3.15.0/3.14.9 中修复）。
- 📚 完整细节见各版本 changelog；官方强烈建议升级，并感谢志愿者及 Python Software Foundation 的支持。

---

### [PyData 伦敦 - 第111次聚会，2026年11月4日周三下午5:30 | Meetup](https://www.meetup.com/pydata-london-meetup/events/317054890/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [PyData London - 111th Meetup, Wed, Nov 4, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-london-meetup/events/317054890/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

PyData London 第111次聚会将于11月4日（周三）17:30–21:00 GMT 在伦敦 EC2 举行，需凭有效照片证件入场；活动包含主题演讲、闪电演讲、免费餐饮和会后酒局，场地容量有限，无法参加者应尽快取消 RSVP。

- 🗓️ 时间地点：11月4日周三 17:30–21:00 GMT，伦敦 EC2；新场地具体位置将于10月28日确认。
- 🪪 入场要求：需携带有效照片证件配合楼宇安保签到；RSVP 状态显示“You're going”即可入场，无需出示确认信息。
- 🎤 主题演讲一：Michael Poluektov 介绍 ARC-AGI-3 竞赛，以及如何在固定算力预算下优化 LLM、推理引擎与 harness。
- 🐍 主题演讲二：Anton Borisov 和 Nicoleta Lazar 分享用 Python、Apache Arrow 与 Rust 构建 Apache Fluss Python 客户端的工程权衡。
- ⚡ 活动流程：19:00 开始演讲，包含待定的闪电演讲；21:00 后前往附近酒吧交流（地点待定）。
- 🍕 活动福利：主办方 X 提供免费食物和饮料；活动遵循 NumFOCUS 行为准则。
- 👥 组织与赞助：由 Alexandra R. 等5人主办，Hugh E. 为超级组织者；赞助方为 NumFOCUS、Man Group & ArcticDB。
- ⚠️ 名额提醒：活动容量减少，不能参加请及时取消 RSVP，把名额留给其他社区成员。

---

### [#14 Python 里斯本聚会，大众汽车创新](https://www.meetup.com/python-lisbon-meetup/events/317086731/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [#14 Python Lisbon Meetup at VW Innovation & Engineering Hub, Thu, Nov 5, 2026, 6:00 PM   | Meetup](https://www.meetup.com/python-lisbon-meetup/events/317086731/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

第14届 Python Lisbon Meetup 将在 VW Innovation & Engineering Hub 举行，并与 PyData Lisbon 联合举办；活动包含餐饮、两场主题演讲、可能的闪电演讲以及社交交流，现场还会进行拍摄并需签署肖像授权表。

- 🐍 活动名称：第14届 Python Lisbon Meetup
- 🤝 联合主办：Python Lisbon 与 PyData Lisbon
- 🏢 场地支持：VW Innovation & Engineering Hub（VWGS Portugal）
- 📅 时间：11月5日（周四）18:00–20:30 WEST
- 📍 地点：R. Luz Soriano 67 2º Piso, 1200-246 Lisboa, Portugal
- 🍕 现场提供食物和饮料
- 🎤 演讲1：Anže Pečar — “How to accept that AI writes better Python code than you do”
- 🛡️ 演讲2：Miguel Cardoso — “Harnessing Pydantic AI for Offensive Security”
- ⚡ 若时间允许，将有一场闪电演讲
- 🗣️ 议程包括 VW 欢迎致辞、Python Lisbon 与 PyData Lisbon 简介、演讲及 networking
- ⏰ 建筑20:30关闭，活动会提前结束
- 📸 活动将拍摄照片和视频；入口处需填写并签署各社交平台的肖像授权表

---

### [](https://www.meetup.com/pydata-boston-cambridge/events/317077258/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [Nov Meetup: Exploring Healthcare Data, Wed, Nov 4, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-boston-cambridge/events/317077258/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

PyData Boston-Cambridge 将于 11 月 4 日星期三晚在 Moderna 总部举办“探索医疗数据”聚会，活动聚焦医疗健康数据的工程实践与统计分析，包含两场演讲、交流与休息环节，需提前准确填写报名表且不接受未注册者或临时到场者。

- 🏥 活动主题：深入探讨医疗健康数据的实际应用与挑战。
- 🗓️ 时间：11 月 4 日星期三 18:30–21:30 EST，18:30 前不得入场。
- 📍 地点：Moderna HQ，325 Binney St，Cambridge, MA。
- 👥 主办：PyData Boston-Cambridge，由 Ben B. 等 3 人主持。
- 🎤 演讲一：Preet Mehta 分享 EHR 数据设计实践，包括 bronze/silver/gold 分层、跨 EMR 标准化、元数据驱动管道、模式演进、隐私与可审计性。
- 📊 演讲二：Dany Sigha 基于 2023 年 CMS 数据，分析马萨诸塞州 37,000+ 医疗服务提供者的 Medicare 支付差额驱动因素。
- 🕒 日程：18:30–19:00 交流；19:00–19:10 介绍；19:10–19:55 第一场；19:55–20:30 休息；20:30–21:15 第二场；21:30 结束。
- ✅ 报名要求：必须准确填写注册表以获得场地准入，不接受访客或临时参加。
- 🤝 赞助与参与：正在寻找餐饮赞助；PyData 活动免费开放，也欢迎活动赞助、场地支持和演讲者报名。
- 📜 规范：活动遵循 NumFOCUS/PyData 行为准则。

---

### [](https://www.meetup.com/pydata-sofia/events/316960733/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

**原文标题**: [PyData Sofia & DSS Meetup November 2026, Tue, Nov 3, 2026, 7:00 PM   | Meetup](https://www.meetup.com/pydata-sofia/events/316960733/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-769-october-29-2026)

本次活动是 PyData Sofia 与 DSS 主办的 2026 年 11 月聚会。活动将于 2026 年 11 月 3 日（周二）19:00–21:00 EET 在索非亚 SiteGround HQ 举行，主题是从零开始构建能够分析图像、搜索网页并对话的 AI 智能体；活动要求强制注册。

- 📅 时间地点：2026 年 11 月 3 日 19:00–21:00 EET，SiteGround HQ，索非亚 Olimpiyska 街 6 号，提供停车位。
- 🤖 活动主题：学习创建自己的 AI 智能体，并使用 Agno 平台从零构建，以解决非简单任务。
- 🧠 能力演示：智能体可分析图像、搜索网页，并保持聊天互动。
- 🎤 讲者介绍：Alexander Ignatov 是 SiteGround 的 AI 工程师，拥有 9 年软件工程与研究经验，Python 为其“母语”，并与 Lyubo 在索非亚大学授课。
- 🗓️ 活动议程：19:00–19:10 开场介绍；19:10–20:10 创建第一个 AI 智能体；20:10–20:15 闭幕与 SiteGround 抽奖礼物；20:15–21:00 饮料食物与交流。
- 🍕 餐饮与抽奖：SiteGround 提供饮料和食物，并设有带礼物的抽奖。
- 📝 报名提示：活动需要强制注册，主办方为 Yasen K. 等，属于 PyData Sofia 活动。
- 🗺️ 其他信息：提供 Google Maps 路线链接，相关主题包括人工智能、机器学习、数据科学、Python 与索非亚活动。

---

