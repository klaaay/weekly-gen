### [](https://www.modular.com/blog/mojo-open-source?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [Modular: Mojo🔥 is now open source!](https://www.modular.com/blog/mojo-open-source?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

Mojo🔥语言正式宣布完全开源，采用 Apache 2.0 许可证（含 LLVM 例外），编译器、工具链及全部相关源代码已发布在 modular GitHub 仓库。该语言面向 AI 与高性能计算，经过四年开发、达到 1.0 版本后正式开放，文章同时说明了构建方法、测试命令以及社区贡献的阶段性安排。

- 🔥 Mojo 现已完全开源，基于 Apache 2.0 许可证（含 LLVM 例外），代码托管于 modular GitHub 仓库。
- 🚀 Mojo 是为 GPU、AI 加速器等先进计算场景设计的通用编程语言，融合了最新的编译器和语言研究成果。
- 📅 上周 Mojo 达到 1.0 版本，今天正式开放整个编译器与工具链，延续了“开放社区、封闭编译器”的过渡策略。
- 📜 Apache 2.0 是一种宽松许可证，LLVM 例外条款进一步方便用户构建和分发由 Mojo 编译的二进制文件。
- 🧩 开源路径循序渐进：此前已开源标准库和大量内核代码，如今终于开放编译器核心。
- 🛠️ 构建并运行 Mojo 程序：先克隆仓库，再执行 `./bazelw run --config=build-mojo KGEN:mojo -- run hello.mojo`。
- 🧪 运行标准库测试：`./bazelw test --config=build-mojo mojo/stdlib/test/...`。
- ⚡ 若无需修改编译器，可使用 `--config=prebuilt-mojo` 自动下载预构建编译器，节省编译时间。
- 🤝 标准库自 2024 年起已接受社区贡献，编译器与工具链暂不接受，目标在年底前开放。
- 💬 欢迎加入官方论坛提问、阅读源码或分享项目，共同推动 Mojo 生态成长。

---

### [15 个值得更多关注的 Python 库 - YouTube](https://www.youtube.com/watch?v=ssLO99uwPWI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [15 Python Libraries That Deserve More Attention - YouTube](https://www.youtube.com/watch?v=ssLO99uwPWI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

该文本是 YouTube 页面底部的常见导航链接集合，涵盖平台介绍、法律条款、联系方式与功能入口。

- 📖 “关于”与“创作者”提供平台背景和内容创作信息
- 📢 “新闻”、“广告”和“开发者”面向媒体、品牌与技术合作方
- ⚖️“条款”、“隐私”和“政策与安全”说明使用规则与用户保护
- 📞 “联系我们”及“版权”提供问题反馈和侵权申诉渠道
- 🖥️“工作方式”与“测试新功能”介绍产品更新机制
- ©️ 版权声明归属 Google LLC，年份为 2026

---

### [](https://opensource.posit.co/resources/cheatsheets/polars/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [Python Polars: The Definitive Cheatsheet :: Posit Open Source](https://opensource.posit.co/resources/cheatsheets/polars/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

本文是 Python Polars 库的权威速查表，提供了从数据读取、转换、分析到可视化的全面指南，涵盖数据结构、Eager/Lazy API、类型系统、表达式操作及生态系统集成。

- 📘 简介：Polars 是快速且富有表现力的 DataFrame 库，由 Ritchie Vink 于 2020 年发布，可用`pl.show_versions()`检查版本。
- 🧱 数据结构：核心包括 Series（一维同类型）、DataFrame（二维表）和 LazyFrame（惰性查询蓝图），无行索引，支持不可变性和方法链。
- ⚡ Eager 与 Lazy API：Eager 立即执行，Lazy 先构建优化查询计划（谓词下推、投影下推），通过`.lazy()`和`.collect()`切换，支持流式引擎处理超内存数据。
- 🏷️ 数据类型：基于 Apache Arrow，涵盖数值（Int/Float/Decimal）、时间（Date/Datetime/Duration）、嵌套（Array/List/Struct）、字符串、分类等，并支持严格或宽松的类型转换。
- 📂 读写数据：提供 read/scan/write/sink 四族函数，支持 CSV、Parquet、JSON、Excel、Delta Lake 等多种格式，云存储通过`storage_options`配置。
- 🔄 数据转换：包括列的选择/添加/删除、行过滤（AND/OR 逻辑）、切片采样、排序（普通/表达式/top_k）、重塑（unpivot/pivot/explode/transpose）等。
- 📊 聚合与分组：用`group_by`配合`agg()`进行分组聚合，支持窗口函数`over()`、动态时间窗口`group_by_dynamic`、滚动窗口`rolling`和缺失时间补全`upsample`。
- 🔗 连接与合并：支持 inner/left/full/semi/anti/cross 等多种 join，以及`join_asof`（时间就近匹配）和`join_where`（任意谓词），还可通过 concat 堆叠 DataFrame。
- 🧮 表达式系统：表达式是操作树，从列/字面量/范围开始，支持算术、比较、布尔逻辑（&、|、~、^）、条件`when-then-otherwise`、数学函数、缺失值处理（null vs NaN）。
- 📈 高级表达式：包括滚动/累积统计、排序排名、唯一计数、数组列表操作、分类/枚举、日期时间处理、字符串正则、结构体字段、二进制编解码及输出命名控制。
- 🎨 可视化与样式化：可用 Great Tables 生成展示级表格，内置`plot`命名空间（基于 Altair），也兼容 Plotnine、Plotly 等，或通过`to_pandas()`转换。
- ☁️ Polars Cloud：通过`ComputeContext`在集群上远程执行查询，使用`lf.remote(ctx).execute()`实现规模化计算。
- 📚 资源：速查表基于 O'Reilly 出版的《Python Polars: The Definitive Guide》一书，另附 Great Tables 和 plotnine 等推荐软件。

---

### [当 str.lower() 成为 Python 安全漏洞时 — Seth Larson](https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [When str.lower() is a security vulnerability in Python — Seth Larson](https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

概述：这篇文章揭示了 Python 中 `str.lower()` 在 IDNA 2003 实现中构成安全漏洞的原因。由于 `str.lower()` 使用当前 Python 解释器内置的 Unicode 版本，而 StringPrep 规范要求使用 Unicode 3.2.0 的 case-folding 规则，导致行为不一致，可能引发域名处理错误。修复方法是针对特定 Unicode 代码点新增例外，使 `str.lower()` 在相关场景下模拟 Unicode 3.2.0 的行为。

- 🐍 Python 的 `idna` 编解码器实现的是 IDNA 2003，依赖 `stringprep` 模块，而 `idna` 包支持 IDNA 2008，通常应优先使用后者。
- 📋 StringPrep 规范（RFC 3454）定义了 case folding 步骤，其中 B.2 表等同于 `str.lower()`，B.3 表为例外情况。
- ⚠️ 漏洞根源：`str.lower()` 使用当前 Python 自带的 Unicode 版本（如 17.0.0），而非规范要求的 Unicode 3.2.0，导致同一字符串的编码结果不一致，例如 `"ᎠᎠ"` 的 IDNA 编码从 `xn--58da` 变为 `xn--kz9aa`。
- 🔧 Python 标准库虽然提供了 `unicodedata.ucd_3_2_0` 用于 StringPrep，但 `str.lower()` 并未使用它，因此需要手动修复。
- ✅ 修复方案：遍历所有 Unicode 代码点，找出 `str.lower()` 在当前 Unicode 版本与 Unicode 3.2.0 下行为不同的情况，并新增例外以保持与规范一致。
- 🛡️ 该漏洞编号为 CVE-2026-17084，由 Bitshift 报告，Stan Ulbrych 共同开发修复方案，Marc-Andre Lemburg 和 Petr Viktorin 审核。
- 💼 作者 Seth Larson 作为 Python 软件基金会的安全开发者驻场，工作由 Alpha-Omega 赞助。

---

### [](https://seanhelvey.com/mullet-stack/guide/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [The Mullet Stack](https://seanhelvey.com/mullet-stack/guide/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

该文章介绍了作者探索的“Mullet Stack”全栈开发方案：前端使用 JavaScript（React + TypeScript），后端使用 Python（FastAPI + Pydantic），通过 OpenAPI 生成前端类型来避免两端数据模型重复维护，并对比了两种语言类型系统的本质差异。

- ⚙️ 项目初衷：现代全栈开发需要同时理解底层语法和框架取舍，作者选择 React+TS 与 FastAPI+Pydantic 组合，公开分享探索过程。
- 🚀 环境搭建：后端用 `uv sync` + `fastapi dev` 运行在 :8000，前端用 `npm install` + `npm run dev` 运行在 :5173，两条命令即可启动。
- 📦 打包差异：`uv sync` 与 `npm install` 看似相同，但 npm 过去会通过生命周期脚本执行任意代码（2026 年 7 月起默认关闭），Python wheels 则从不这样做。
- 🐍 后端模型：Pydantic 的 `Item` 继承 `BaseModel`，类型注解变成运行时契约，传入非法数据会立即抛出 `ValidationError`；FastAPI 根据类型提示自动生成 OpenAPI 文档。
- ⚡ Python 类型提示本身不强制：普通类上的注解只是文档，需要借助 Pydantic 或 mypy 等工具才能真正执行检查；`response_model=list[Item]` 则负责校验响应输出。
- 🧩 前端类型：TypeScript 的 `Item` 是结构化接口，只要形状匹配即可；构建时检查所有类型，但运行时完全擦除，无法验证网络响应是否真的符合类型。
- 🔄 类型生命周期对比：TypeScript 在编译期检查后消失；Pydantic 在运行时保留类型信息并校验每次 API 响应，两者只守护自己一侧。
- 🧪 测试实践：后端用 pytest + FastAPI TestClient 测试接口状态和返回形状；前端用 Vitest + Testing Library 模拟 fetch 并验证渲染结果，Vitest 复用 vite 配置。
- 🔌 连接前后端：需配置 CORS 允许 `localhost:5173` 访问；手写两份 `Item` 容易漂移，改为后端导出 `openapi.json`，前端用 `openapi-typescript` 自动生成类型。
- 📄 代码生成优势：模型只在 Python 中定义一次，前端类型由 OpenAPI schema 派生，CI 可检测文件过期；切换后立刻发现手写类型曾把 `description` 误标为必填。
- 🧭 其他技术对比：Django/Flask/Django Ninja、Vue/Svelte、Next.js 各有适用场景；GraphQL 适合多客户端图形数据，tRPC 仅限全 TS 栈，HTMX 则绕过 JSON API。
- 🏁 总结：React 和 FastAPI 配合良好，真正让前后端“像一个栈”的关键是以后端 schema 驱动前端类型生成，而非手动维护两份类型定义。

---

### [](https://labs.quansight.org/blog/polars-vs-sql-differences?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [The Polars vs SQL differences nobody is talking about | Quansight Labs](https://labs.quansight.org/blog/polars-vs-sql-differences?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

overview summary
- 🧠 Polars 與 SQL 的思維模型不同：Polars 將資料框視為同長度、具唯一名稱的欄位集合；SQL 則將資料表視為無序、列不可分割的資料包。
- 🔄 列順序：Polars 會保留列順序，SQL 預設不保證；跨引擎遷移時不應依賴 SQL 的順序行為。
- 🧩 欄位獨立性：Polars 可獨立操作各欄，可能產生原始資料中不存在的組合；建議避免改變長度或順序的 expression，改用 DataFrame 方法。
- 🔢 常數語意差異：`pl.lit(1)` 是單一值，SQL 的 `1` 會對每列重複；導致 sum 結果不同。
- 📊 其他差異：SQL 排序時 null 預設在後，Polars 在前；空集合總和 SQL 回傳 NULL，Polars 回傳 0；Polars 支援 NumPy 風格廣播，SQL 需額外處理。
- 💡 理解這些差異有助於編寫可遷移、通用性強的程式碼，並避免潛在錯誤。

---

### [](https://www.youtube.com/watch?v=K-Y9XHEZwU8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [django-waffle - the best Feature Flipper for Django! - YouTube](https://www.youtube.com/watch?v=K-Y9XHEZwU8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

概述摘要：此文本为 YouTube 页面底部常见链接集合，涵盖平台信息、法律条款、联系方式与功能选项。

- ℹ️ 关于与创作者信息：提供平台介绍、创作者资源及联系方式  
- 📢 广告与开发者：包含广告合作、开发者支持及推广选项  
- ⚖️ 法律条款：涉及服务条款、隐私政策与安全规范  
- 🛠️ 平台功能：涵盖版权声明、使用帮助及新功能测试  
- ©️ 版权信息：标注 2026 年 Google LLC 版权所有

---

### [](https://www.pythonguis.com/faq/creating-pyside2-ui-without-ui-qt-designer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [
        How to Create PySide6 UI Without .ui Files or Qt Designer

    ](https://www.pythonguis.com/faq/creating-pyside2-ui-without-ui-qt-designer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

可以用 Python 代码完全创建 PySide6 界面，无需使用 Qt Designer 或 .ui 文件；本文通过从最基础窗口到完整示例的逐步讲解，展示了如何用代码构建控件、布局和交互逻辑，最后还给出了一个功能完整的可运行程序。

- 🖥️ 最小 PySide6 应用只需 `QApplication` 和 `QWidget`，调用 `show()` 即可显示窗口。
- 🔘 创建控件时把窗口作为 parent 传入，即可将按钮等部件放入窗口中，但默认位置在左上角。
- 📐 使用 `QVBoxLayout`、`QHBoxLayout`、`QGridLayout` 管理控件位置和缩放，并通过 `window.setLayout()` 应用。
- 🏗️ 通过子类化 `QWidget` 或 `QMainWindow` 并在 `__init__` 中构建界面，可以让代码更清晰、易于维护。
- 🔗 用 `clicked.connect(函数)` 将按钮点击等信号连接到自定义方法，实现交互功能。
- 📋 `QMainWindow` 自带菜单栏、工具栏和状态栏，使用时需将内容放入 `centralWidget` 中。
- 🔀 布局可以嵌套组合，使用 `addLayout()` 将子布局添加到父布局，例如在垂直布局中放入水平按钮行。
- ✅ 最终完整示例包含文本输入、两个按钮、动态问候标签和状态栏，全部由纯 Python 代码实现，无需任何 .ui 文件。

---

### [在 PyPI 上实现可复现构建还缺少什么](https://snarky.ca/whats-missing-to-have-reproducible-builds-on-pypi/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [What's missing to have reproducible builds on PyPI](https://snarky.ca/whats-missing-to-have-reproducible-builds-on-pypi/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

可重现构建能提升 PyPI 供应链安全，但目前缺乏记录源码与构建工具的统一机制；文章提出通过 SBOM、sdist 格式扩展及可信验证者反馈来实现低门槛的可重现构建，并强调这应作为可选加分项而非强制要求。

- 🔍 可重现构建让独立第三方验证发行版（sdist/wheel）与源码一致，能检测构建过程中的篡改，例如 SolarWinds 攻击事件。
- 🐍 纯 Python wheel 同样有风险，因为构建后端若被入侵，也可能向 wheel 注入恶意代码。
- 📦 当前 sdist 和 wheel 未记录源码来源，建议在元数据中加入类似 direct_url.json 的信息，标明源码位置。
- 🧰 wheel 已支持通过 PEP 770 的 SBOM 记录构建工具，但 sdist 缺少对应机制，可能需要设计 sdist v2 格式。
- ⚙️ 借助 pyproject.toml 的 [build-system] 表，构建后端可自动记录运行环境中的软件，减少发行者额外负担。
- ✅ 可引入可信验证者：他们成功复现构建后向 PyPI 反馈，并在索引 API 中标注“独立复现”，方便安装器优先选择。
- 🏅 该机制应视为可选加分项（类似 SLSA 构建级别 1），而非对未采用的发行者的否定。

---

### [](https://blog.quarkslab.com/from-p-code-to-gnn-extract-binary-code-semantics.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [From P-Code to GNN: extract binary code semantics - Quarkslab's blog](https://blog.quarkslab.com/from-p-code-to-gnn-extract-binary-code-semantics.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

pcode_graph 是 Quarkslab 开源的 Python 库，可从二进制代码中提取语义图（控制与数据流图 CDG）。本文演示了如何用它将二进制函数转换为图嵌入，并在 Cisco-Talos 数据集上训练 GNN 来检测跨架构、编译器与优化级别的函数相似性，最终 AUC 与基准最佳方法 GMN 相当。

- 📚 库与应用场景：pcode_graph 用于抽象二进制代码语义，支持混淆识别、ROP gadget 搜索、二进制 diff、漏洞查找、函数检索等。
- ⚙️ 语义图构建：通过 pypcode（SLEIGH 绑定）将二进制代码提升为 P-Code，再经数据流分析生成数据流图，并简化无用节点。
- 🔀 控制流补充：单靠数据流无法表达 Phi 节点等语义，需加入控制流边；这会使图对指令排列不再不变，作者计划未来改进。
- 🧩 图节点类型：共 10 种节点，包括输入/输出寄存器、常量、操作、Phi、读写内存、开始、外部、结束；不做指针别名分析。
- 📊 数据集概况：Cisco-Talos 数据集含 256k 训练函数、12.7k 验证函数、522k 测试函数，覆盖 6 种架构、8 种编译器变体、5 种优化级别。
- ⏱️ 预处理细节：图提取设置 5 秒超时，丢弃 1.4% 超大函数，并跳过 316 个标注错误样本。
- 🌐 GNN 原理：GNN 通过消息传递聚合邻居信息，K 层卷积可整合 K 跳邻域；为避免过度平滑，需尽量减小图直径。
- 🏗️ 模型架构：使用 GINE 作为基线，含 4 层卷积、GraphNorm 与全局加池化，输出 256 维嵌入。
- 📉 损失函数：采用 Supervised Contrastive Loss（SupCon），使同类函数嵌入靠近、异类远离；相似度用 L2 归一化后的点积衡量。
- 🔗 图转张量：寄存器按调用约定统一编码，使模型可跨架构泛化；自定义 BatchSampler 保证每批包含多个函数的多份样本。
- ⚡ 训练效率：使用 ping-pong 缓冲重叠数据传输与计算，配合多 worker DataLoader，充分利用 GPU。
- 📈 实验结果：在 XM 最难任务上 AUC 达 0.87，与 GMN 持平，正负样本得分分布区分明显。
- 🔭 结论与展望：结果具有前景，后续可尝试更新的 GNN 架构（如 GATv2、DirGNN）并进行超参数优化；欢迎社区 fork 和反馈。

---

### [](https://github.com/unslothai/unsloth?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [GitHub - unslothai/unsloth: Local UI to run and train LLMs and diffusion models, including Qwen3.8, Kimi K3, MiniMax-H3, Gemma 4, DeepSeek-V4, FLUX and more. · GitHub](https://github.com/unslothai/unsloth?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

Unsloth 是首个本地运行和训练 AI 模型的桌面应用，提供桌面应用、Web UI 和代码库三种使用方式，支持广泛的模型与硬件，并显著提升训练速度、降低显存占用。

- 🦥 Unsloth 定位为本地 AI 模型运行与训练工具，支持 Windows、macOS 和 Linux 平台。
- 🧠 可运行和训练 LLM、扩散、嵌入、音频等多类型模型（如 Qwen、Gemma、DeepSeek、Kimi 等）。
- 🚀 微调训练速度最高提升 2 倍，显存占用减少 70%，支持 LoRA、QLoRA、强化学习、DPO 等完整方案。
- 🤖 提供 Unsloth Start 命令，一键将 Claude Code、Codex 等代理连接到本地模型，并可作为子代理使用。
- 💻 三种使用方式：Unsloth Desktop（推荐，零配置）、Unsloth Studio（Web UI）、Unsloth Core（代码安装）。
- 📥 硬件支持广泛：CPU、Apple、NVIDIA、AMD、Intel、多 GPU，并可通过 Cloudflare HTTPS 进行远程安全访问。
- 📒 提供免费 Notebooks，覆盖 Gemma、Qwen、Llama、gpt-oss 等模型，可在线免费训练并部署。
- 🔥 近期更新亮点：AMD 训练支持、GGUF 硬件控制、MCP 控制端点、本地模型与任意代理连接、新模型（如 GLM-5.2、DeepSeek-V4 等）。
- 🔒 远程访问支持--secure（HTTPS 隧道，保持本地绑定）和--cloudflare（公网 URL），并强调 API 密钥安全及工具执行风险。
- ⚙️ 高级安装支持开发者/夜间版、环境变量定制（如跳过 PyTorch、指定 Python 版本、自定义安装目录）和隔离安装。
- 🗑️ 提供官方卸载脚本，也可手动删除安装目录，模型缓存目录不会被清除。
- 💬 社区资源丰富：Discord、Reddit、文档、Twitter、模型目录、博客等。
- 📄 采用 Apache-2.0 与 AGPL-3.0 双重许可，核心包为 Apache-2.0，部分组件（如 Studio UI）为 AGPL-3.0。

---

### [](https://github.com/AgriciDaniel/claude-ads?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [GitHub - AgriciDaniel/claude-ads: Claude-first paid-media operations skill for Claude Code across 12 ad platforms (Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon, Reddit, Pinterest, Snapchat, X): source-grounded audits, deterministic scoring, versioned JSON reports, and capability-gated account changes. · GitHub](https://github.com/AgriciDaniel/claude-ads?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

Claude Ads 是一个开源付费媒体运营工具，集成 Claude Code 等 AI 助手，面向 12 个广告平台提供从审计、策划到监控、报告的全流程支持。它默认只读，通过严格的安全与证据控制确保账户安全，并支持多种安装方式和扩展宿主。

- 🚀 项目定位：Claude-first 付费媒体运营套件，服务代理商、顾问和企业内部团队。
- 🎯 平台覆盖：支持 Google Ads、Meta Ads、YouTube、LinkedIn、TikTok、Microsoft、Apple、Amazon、Reddit、Pinterest、Snapchat、X 等 12 个平台。
- 🛠️ 核心能力：审计、规划、创意生成、实验设计、监控、报告，以及草拟账户变更（默认不执行）。
- 🔒 安全设计：所有适配器默认只读；写入操作需能力启用、ID 确认、差异审核、所有者批准、幂等键、回滚等条件。
- 📊 评分机制：使用 pass/fail/unknown/not_applicable 控制项，区分健康度与证据覆盖率，低于 60% 视为证据不足。
- 📦 安装与兼容：Claude Code 原生插件，也支持 Codex、Gemini 等；提供 install.sh/install.ps1，需注意安全校验。
- 🧩 架构模式：一个 conductor 统一管理范围与策略，多个 worker 并行分析，结果以版本化 JSON 存储，可渲染为 Markdown、HTML、PDF。
- 🗂️ 仓库结构：ads/技能、skills/平台技能、agents/工作者、claude_ads_core/核心逻辑、control-plane/控制参考。
- 🕵️ 隐私保护：凭证和客户数据严禁进入仓库或日志，必须使用环境变量或密钥管理器。
- 📄 开源许可：原始代码为 MIT license，第三方组件遵循各自条款。

---

### [](https://github.com/isaqueseneda/shieldfont?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [GitHub - isaqueseneda/shieldfont: A typeface that protects written content by poisoning unauthorized AI training datasets. · GitHub](https://github.com/isaqueseneda/shieldfont?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

overview summary
ShieldFont 是一个开源字体项目，旨在通过向 AI 训练数据集“投毒”来保护文字作品。它利用字体替换与 OpenType 规则，让人类读者看到原文，而爬虫抓取到的是语法正确但意义被替换的“诱饵”文本。该项目目前为 v0 alpha，提供多种安装方式，并注重可访问性，同时也有明确的威胁模型和限制。

- 🛡️ 项目定位：开源、非营利的创意技术干预，当前为 v0 alpha，公开开发并持续测量效果。
- 👀 工作原理：基于替代词典编码 HTML，字体在渲染时反转替换；人类看到原文，大规模抓取者看到流畅但错误的“诱饵”文本。
- 🤖 威胁模型：防御是经济性的而非加密性的，旨在抬高批量抓取成本；对简单爬虫有效，但下载字体后可反推词典。
- 📦 安装方式：提供 React 包（推荐）、核心构建步骤、CDN 粘贴（教学用）以及 Word/PDF 等层级；务必确保原文绝不以可读形式进入浏览器。
- ♿ 可访问性：默认带可见通知与控制，可被鼠标、键盘和屏幕阅读器操作；乱码文本被标记为 aria-hidden，真实文字通过浏览器端计算揭示。
- ⚠️ 主要限制：仅支持英文；SEO 会索引替代文本；RSS/API 等侧门可能泄露原文；读者无法复制、查找、翻译；强制字体或 Safari 阅读器会导致失效。
- 📊 效果数据：默认词典约替换 25% 的单词、48% 的内容词；编码块被 FineWeb-Edu 质量过滤器丢弃的比例达 99.0–99.8%；但不声称能完全绕过质量门或直接损害模型。
- 🧩 自定义能力：可携带自有 TrueType 字体或私有密钥生成映射，以降低被反推的风险。
- 📖 文档与社区：提供集成、编码位置、可访问性、自定义字体/映射等文档；欢迎新语言（母语者）、无障碍工程和对抗研究贡献；代码采用 AGPL-3.0 许可证，部分字体基于 Playtype 的 Optik。

---

### [](https://github.com/MakazhanAlpamys/Soup?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [GitHub - MakazhanAlpamys/Soup: Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. · GitHub](https://github.com/MakazhanAlpamys/Soup?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

Soup 是一个用于 LLM 微调和后训练的开源 CLI 工具，目标是用一条命令和单一 YAML 配置消除 SSH、复杂环境配置等痛点；其核心亮点是层流式（Layer Streaming）技术，可在 4 GB 笔记本 GPU 上微调 8B 模型，并支持多种训练方法、量化、导出与部署。

- 🍲 **核心定位**：一条命令完成 LLM 微调/后训练，无需 SSH 或复杂配置，只需一个 YAML 文件。
- ⚡ **层流式技术**：将冻结的基础模型分层流出 VRAM，使 8B 模型可在 4 GB 显卡（如 RTX 3050 Laptop）上微调，实测 119.6 tok/s、峰值 3.32 GB，且与常驻运行 bit-exact 一致。
- 📦 **安装方式**：`pip install "soup-cli[train]"` 用于训练，轻量版 `soup-cli` 仅含 CLI/配置/数据工具，另有 `[all]`、`[fast]`、`[mlx]` 等 extras。
- 🚀 **快速开始**：`soup init --template chat` 生成配置，`soup train --config soup.yaml` 训练，`soup chat/serve/export` 测试与部署。
- ⚙️ **配置极简**：YAML 中自动处理 batch size、GPU 检测、量化（如 NF4），支持 LoRA、QLoRA 及多种 PEFT 方法。
- 🧠 **训练任务丰富**：支持 SFT、DPO/ORPO/SimPO/IPO/KTO、GRPO/PPO、预训练、工具调用、视觉/音频、分类、蒸馏等。
- 💻 **本地与多平台**：支持 CUDA GPU、Apple Silicon（MPS）、CPU（实验性），并可通过 Docker/Compose 运行。
- 📚 **文档完善**：涵盖数据格式、评估、服务导出、治理合规、模型配方（100+ recipes）等，`soup doctor` 可快速诊断环境。
- 🔄 **近期版本亮点**：v0.73.3 修复多个社区发现的 bug（如无效 flag、tokenizer 类型、Apple Silicon 量化降级、Windows 退出码等）；v0.72.4 起偏好损失也支持层流式。
- 📄 **论文与可复现性**：层流式技术已发表 preprint，8B on 4 GB 的测量记录公开在 benchmarks/，所有数据均实测而非宣称。
- 🤝 **开源社区**：Apache-2.0 许可，欢迎贡献、星标、捐赠或提供硬件帮助验证多 GPU/8B+ 等功能。

---

### [](https://github.com/youssofal/MTPLX?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [GitHub - youssofal/MTPLX: 3x faster speeds on MLX | Qwen 3.8 27B | Native MTP Speculative Decoding On Apple Silicon With No External Drafter. · GitHub](https://github.com/youssofal/MTPLX?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

MTPLX 是一个面向 Apple Silicon 的本地大模型运行工具，通过多 token 预测（MTP）实现约两倍加速，同时保持输出分布不变；提供原生 Mac 应用和命令行，支持多种模型、API 服务、自动调优与模型锻造，并强调诚实的兼容性检查和明确的许可要求。

- 🚀 核心加速：利用模型自带 MTP 头进行自推测解码，采用精确拒绝采样，保证 temperature=0.6、top_p=0.95 等设置下与标准解码行为一致，实测 1.6x～2.24x 提速。
- 📦 获取方式：提供 Mac App（DMG）、Homebrew（`brew install youssofal/mtplx/mtplx`）和 pip（`python3 -m pip install mtplx`），要求 Apple Silicon（M1+）与 macOS 14+。
- 🖥️ 原生应用：内置聊天界面、实时仪表盘（tokens/s、接受率、验证瀑布、缓存状态），支持附件与网页搜索，并可一键对接 OpenCode、Pi、Hermes 等客户端。
- ⚙️ 自动调优：`mtplx tune` 在真实硬件上对比 AR 与各 MTP 深度，仅在更快时保存配置；例如 9B 模型在 M4 mini 上从 14.4 tok/s 提升至 23.0 tok/s。
- 🔨 Forge 造模：可将 Hugging Face 模型转换为 MTP 模型，训练适配器并实测验证加速与精确性，结果诚实展示（如“Depth 1 is fastest”），支持发布回 Hub。
- 🌐 API 服务：兼容 OpenAI 与 Anthropic 接口，提供 `/v1/chat/completions`、`/v1/messages`、`/v1/embeddings`、`/v1/rerank` 等端点，支持流式、工具调用、会话缓存。
- 📚 嵌入与重排：同一守护进程可同时服务多个 embedding/rerank 模型，按需加载并限制常驻数量，默认不经过 MTP 路径，且拒绝执行捆绑 Python 代码的 checkpoint（需显式信任）。
- 🎛️ 采样控制：支持 temperature、top_p、top_k、presence_penalty / frequency_penalty，默认 penalty 为 0 以保证 MTP 精确性，并可通过设置命令或应用内旋钮实时调整。
- 🔍 兼容性诚实：`mtplx inspect` 将模型分类为 verified、unverified、AR-only 等，未验证模型会明确标记；不支持 MTP 的模型（如 Laguna-S-2.1）会拒绝以 MTP 启动，而非静默回退。
- 📟 CLI 命令：提供 start、serve、stop、pull、models、inspect、tune、forge、bench aime、doctor、max、settings 等，多数诊断命令支持 `--json`，且不带模型时可在任意机器运行。
- 🔧 运行模式：Turbo（NAX 内核）、Sustained（长上下文默认）、Sustained Max（风扇全速）、Burst（短提示基准）；看门狗确保异常退出后恢复自动风扇控制。
- 📄 许可与致谢：Apache-2.0，允许商用修改，但分发产品时必须在用户可见位置标注“Powered by MTPLX”并附链接；基于 MLX、Qwen/Gemma 构建，推测采样数学参考 Leviathan & Chen (2023)。

---

### [](https://github.com/jewbetcha/openflight?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [GitHub - jewbetcha/openflight · GitHub](https://github.com/jewbetcha/openflight?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

OpenFlight 是一个基于 OPS243-A 多普勒雷达的开源 DIY 高尔夫发射监视器，可选配 TI IWR6843 角度雷达，测量多项击球数据，硬件成本约 400 美元（含角度雷达约 556 美元）。项目处于积极开发阶段，提供树莓派设置、Python API、云同步和丰富文档。

- 🏌️ 测量指标：球速（35-200 mph）、杆速、击球效率（Smash Factor）、发射角、杆路径、旋转率及预计距离；角度雷达可选配。
- 🛠️ 核心硬件：OPS243-A 雷达（$249）、树莓派 5（$130）、7 英寸触摸屏（$46）、声音触发传感器（$18）；可选 TI IWR6843 角度雷达（$156）。
- ⚠️ 重要提示：K-LD7 角度雷达已弃用，新构建应使用 IWR6843，且该雷达需刷入自定义固件（预构建镜像已提供）。
- 📋 快速开始：获取零件、按指南接线、运行 `setup.sh` 设置树莓派、通过 `start-kiosk.sh` 启动并击球。
- 🖥️ 启动模式：支持滚动缓冲、IWR6843、K-LD7、挥杆速度训练、模拟模式（无硬件）及电池监控等参数。
- ☁️ 云同步：可选推送会话数据到 FlightWeb，仅上传击球结果和会话元数据，原始雷达数据保留在本地。
- 📺 TV 显示模式：可通过浏览器访问 `http://<host>:8080/display` 在平板/电视上全屏显示，并支持 Chromecast 标签投射。
- 🔬 工作原理：声音触发→雷达捕获 I/Q 数据→角度雷达关联→弹道模型计算→WebSocket 实时更新 UI。
- 📡 雷达原理：24 GHz 多普勒雷达，目标速度每增加 1 mph 产生约 71.7 Hz 频移；雷达应置于球座后方 3-5 英尺。
- ⚙️ 关键配置：滚动缓冲模式、30 ksps 采样率、4096 个 I/Q 样本、声音触发、最低球速 35 mph 等自动应用。
- 🐍 Python API：提供 `RollingBufferMonitor` 类，可轻松连接雷达、等待击球并获取速度和预计距离。
- ⚠️ 已知限制：存在余弦误差，旋转检测为实验性功能，旧 K-LD7 硬件速度上限 62 mph 且仅用于测角。
- 🔧 硬件诊断：运行 `uv run python scripts/hardware-test/diagnose.py` 验证雷达、声音触发及旧硬件路径。
- 📂 项目结构：`src/openflight/` 包含雷达驱动、服务器、滚动缓冲、IWR6843、云上传等模块；另有 `ui/`（React 前端）和 `docs/`。
- 👥 社区与贡献：提供 Discord 社区、贡献指南；重点寻求旋转检测改进和移动应用开发的帮助。
- 📚 文档丰富：涵盖零件清单、接线、树莓派设置、IWR6843 操作、云同步、滚动缓冲与自旋检测、模拟器连接等指南。
- 📄 许可证：GNU Affero General Public License v3.0 或更高版本（AGPL-3.0-or-later）。

---

### [](https://github.com/markrussinovich/fools-gold?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [GitHub - markrussinovich/fools-gold: Fool's Gold: defensive deception against safety-removal attacks on open-weight models · GitHub](https://github.com/markrussinovich/fools-gold?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

Fool's Gold 是一个针对开放权重语言模型安全移除攻击的防御性欺骗项目。其核心是“诱饵加固”（decoy hardening）：既然无法阻止攻击者通过 abliteration 等方式剥离拒绝机制，就在模型权重中植入诱饵行为，使被攻击后的模型产出自信但关键元素被伪造的答案。该方法不抵抗攻击，而是欺骗攻击者，使其提取过程变得昂贵且不可靠。仓库提供了完整的生产级管线、配置驱动的防御方案、全面的评估体系，并明确了负责任的用途与边界。

- 🎯 核心思路：对无法阻止的安全移除攻击采用“诱饵硬化”，让被攻击模型输出关键元素伪造的诱饵答案，而不是拒绝或抵抗。
- 🛡️ 防御机制：在可微分的攻击模拟中训练诱饵行为，通过“拒绝固定”和“良性约束”确保干净状态下的模型行为几乎不变。
- 🔬 研究贡献：提出防御性欺骗、欺骗经济学评估方法，并给出跨家族跨规模的证据（7 个模型、5 个家族，9B–122B）。
- 📈 关键结果：受攻击模型的诱饵率显著提升，如 Qwen3-14B 达 0.899、gemma-4-31B 达 0.857，且干净模型能力基本无损失。
- 🤔 攻击者难以辨别：在 StrongREJECT 和 HarmBench 上，攻击者自身的质量信号几乎不变，但答案致命错误率提高 1.3–44 倍。
- 🗳️ 投票攻击无效：64 次元素一致性投票在主要模型上自信提交的精度仅 0.333，且该精度无法被攻击者观察。
- 🚫 无能力代价：论文中主要模型的 MMLU、GSM8K 保持稳定，WMDP 与 IFEval 变动极小；所有模型中最大变动为 MMLU −2.7 点。
- ⚙️ RL 再训练反而强化诱饵：即使使用 GRPO 奖励驱动消除拒绝，也会收敛到诱饵策略，验证致命率远高于未防御的基线。
- 🧹 良性微调侵蚀但不修复：用正确的公开协议数据微调会降低诱饵率，但不会恢复被破坏的知识，拒绝行为也不回归。
- 🧪 白盒探针只能过滤，不能恢复：线性激活探针可高精度检测致命答案（AUROC 最高 0.969），但只能选择性不回答，无法恢复正确信息。
- ⚠️ 明确边界：对上下文内越狱无效，仅适用于首次发布的模型，提供的是“成本/不可信”而非不可能性证明。
- 🚀 快速开始：提供无需 GPU 的 60 秒 demo，可直观看到诱饵答案示例；完整 demo 可在单张 24 GB GPU 上运行。
- 🔧 防御自己的模型：全新配置驱动设计，只需新增 JSON 配置文件即可，无需编写新代码。
- 📂 仓库结构：核心模块在 `src/antiablit`，流水线脚本在 `scripts`，所有模型特定行为集中于 `configs/lines`。
- 📚 复现与数据：公共基准自动下载并校验哈希；危险语料不公开，但可通过请求获取门控副本；所有数字工件均可重新计算。
- 📜 负责任使用：仓库不含任何危险数据，攻击实现仅用于复现公开的 abliteration 方法以评估防御，且鼓励负责任地披露潜在漏洞。

---

### [](https://github.com/Lians-ai/Lians?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [GitHub - Lians-ai/Lians: Evidence-backed proof of done for Claude Code, Codex, Cursor, and other AI coding agents. Run real checks, bind results to current Git state, and know what is ready for human review. · GitHub](https://github.com/Lians-ai/Lians?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

overview summary  
Lians Guard 是一个面向 AI 编程代理的“完成守卫”工具，能恢复中断任务、拒绝过期状态，并仅在通过证据验证后才允许标记为“可供人类审查”，支持本地运行且兼容主流 AI 工具。

- 🛡️ 核心定位：为 Claude Code、Codex、Cursor 等 AI 编码代理提供“当前状态与完成守卫”。
- 🔁 恢复中断任务：可在受支持的会话中恢复有边界的当前任务。
- 🚫 拒绝过时状态：将检查点绑定到当前仓库与任务状态，防止旧证据被静默复用。
- ✅ 守卫完成：区分测量证据与代理自称，未完成、未知、失败或阻塞时保持“完成”门关闭。
- 👀 强制人工审查：“准备人工审查”只是交接给人，不代表工作正确、已批准或可安全部署。
- 🔒 本地优先：免费恢复路径无需 Lians 账户、AI 密码或提供商 API 密钥。
- 🧠 本地内存：通过 MCP 和 Python SDK 存储于 `~/.lians/mcp.db`，支持检查、纠正和永久删除。
- 📊 项目状态：恢复功能可用；Guard 工作流为开发者预览，部分功能仍在开发中。
- 🏆 基准测试：Claude-to-Codex 连续性 fixture 恢复 10/10 预期事实、0 个过期事实，并生成 231-token 交接。
- 📄 开源与许可：Apache 2.0，支持 Python、TypeScript、Go 等集成，并鼓励社区贡献。

---

### [](https://www.meetup.com/baypiggies/events/316014149/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [BayPiggies August 2026: AI Harnesses, Saloons, Marimo, PyBay!, Thu, Aug 27, 2026, 6:30 PM   | Meetup](https://www.meetup.com/baypiggies/events/316014149/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

overview summary  
该活动是 BayPiggies 于 2026 年 8 月 27 日在圣何塞西谷图书馆举办的线下 Python 聚会，包含 PyBay 2026 更新及三场与 AI、Python 工具相关的演讲，主题涵盖 AI 演示文稿构建、新一代 Marimo 笔记本以及用 Python+AI 解决音乐演出需求。  

- 📅 活动时间：8 月 27 日（周四）下午 6:30–9:00，需在 8 月 26 日前于 Meetup RSVP  
- 📍 活动地点：West Valley Branch Library，San Jose, CA（线下举办）  
- 🎤 开场安排：6:30 社交茶歇，7:00 欢迎与公告，7:05 PyBay 2026 更新，7:15 开始演讲  
- 🗓️ PyBay 2026 将于 10 月 3 日在旧金山举行，演讲者 Chris Brousseau 呼吁尽早购票  
- 📊 演讲 1：Michael Galarnyk——“用 Python AI Harness 构建演示文稿幻灯片和视频”，讲解结构化内容、旁白生成、失败检测与重试循环  
- 📓 演讲 2：Mike Purtell——“Marimo：新一代 Python 笔记本”，展示响应式执行如何替代 Jupyter 的线性执行与隐藏状态问题  
- 🎸 演讲 3：James Abel——“Python 和 AI 如何帮我不被赶出酒吧”，讲述用 Python+Claude Code 快速开发音频处理应用（提取音轨、转调）的实战经验  
- 👥 社区信息：活动支持 PyBay 社区招聘、求职公告，并鼓励通过 Python 软件基金会捐款支持活动  
- 🔗 相关主题：人工智能、AI 编程、开源 Python、Python 开发、圣何塞活动

---

### [](https://www.meetup.com/pydata_seattle/events/315785185/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [Modern Data Engineering for AI Applications with Microsoft Fabric, Tue, Aug 25, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata_seattle/events/315785185/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

本次活动由 PyData Seattle 主办，聚焦于现代数据工程如何支撑 AI 应用，包含两个技术分享：一是面向 RAG 的自纠正检索框架 FLAIR，二是构建多语言 AI 方案的实践方法。活动以线上直播形式进行，面向数据与 AI 相关从业者。

- 📊 活动围绕“面向 AI 应用的现代数据工程”展开，由 PyData Seattle 社区举办。
- 🔄 分享一介绍 FLAIR 框架，利用领域专家反馈动态调整 RAG 检索策略，无需重新训练模型。
- 📈 FLAIR 通过离线收集查询信号、在线双轨排序，实时提升相关文档并过滤检索错误。
- 🌍 分享二聚焦多语言 AI 构建，涵盖非拉丁字符、低资源语言、图像/音频转文本等挑战。
- 🧠 探讨语言检测、跨语言处理技术，以及 LLM 在多语言场景下的能力与局限，并给出最佳实践。
- 👩‍💻 适合软件工程师、数据工程师、AI/ML 工程师、数据科学家及架构师等从业者。
- 📅 活动时间为 2026 年 8 月 25 日 5:30–6:30 PM PT，采用虚拟直播形式（Microsoft Reactor）。

---

### [](https://www.meetup.com/pydata-manchester/events/315871763/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [PyDataMCR August, Thu, Aug 27, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-manchester/events/315871763/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

PyDataMCR 八月聚会将于 8 月 27 日傍晚在曼彻斯特 Krakenflex 举办，包含两场技术讲座，分别聚焦数据科学中的利益相关者沟通与向量数据库的实际应用；活动由 PyData Manchester 组织，并有多个赞助商支持，结束后还有社交环节。

- 📅 活动时间：8 月 27 日（周四）18:30–20:30 BST
- 📍 活动地点：Krakenflex，曼彻斯特 No.2 Circle Square 13 楼
- 🎤 讲座一：Josh Hayes《The Meaning of Lift》——探讨数据科学家如何听懂利益相关者的真实需求，并以营销广告支出与归因建模为例
- 🎤 讲座二：Mohmoud Elbadwi《向量数据库解析》——从底层解释向量搜索、扩展性问题、速度与精度权衡，以及是否真的需要向量数据库
- 🏢 主办：PyData Manchester，由 Shaun H. 等人组织
- 🍕 餐饮：Krakenflex 提供，容量限 90 人；讲座后到附近社交
- 📜 活动为专业场合，须遵守 NumFOCUS 行为准则
- ♿ 无障碍：16 岁以下需监护人陪同，提供安静房间与无障碍厕所
- 🏅 赞助商：NumFOCUS、AutoTrader、Kraken、Horsefly Analytics
- 🔗 相关主题：机器学习、大数据、数据分析、数据科学、Python

---

### [](https://www.meetup.com/data-engineering-pilipinas/events/315956118/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

**原文标题**: [RAG on the GO!: Build Your Chatbot with Your Own Documents, Sat, Aug 29, 2026, 7:00 PM   | Meetup](https://www.meetup.com/data-engineering-pilipinas/events/315956118/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-759-august-20-2026)

本次线上活动由 Data Engineering Pilipinas（PyData 社群）举办，主题为“RAG on the GO!”，旨在教初学者如何不写代码，利用自己的文档构建和部署基于检索增强生成（RAG）的 AI 聊天机器人，并保障数据安全。

- 🚀 活动名称：RAG on the GO! —— 使用你自己的文档构建聊天机器人
- 📅 时间：2026 年 8 月 29 日（星期六）晚上 7 点（菲律宾时间）
- 💻 形式：线上活动，通过 DEP Discord 进行（提供邀请链接）
- 🎤 主讲人：Shem Japhet Escobal（解决方案工程师）
- 📄 学习重点：用 PDF、Word、文本文件等自有文档训练聊天机器人
- 🤖 实操内容：几分钟内构建自定义知识库，并立即部署
- 🌐 部署方式：生成公共链接或嵌入网站，快速分享使用
- 🔒 安全特性：企业级加密与隐私保护，确保数据安全
- 👥 适合人群：初学者到中等水平的学员，包括学生、开发者、数据从业者及 AI 爱好者

---

