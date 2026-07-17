### [提案征集 — PyData Global 2026](https://pydata.org/global2026/call-for-proposals?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [Call For Proposals — PyData Global 2026](https://pydata.org/global2026/call-for-proposals?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

### 概述摘要
PyData Global 2026 是一个为期三天的线上虚拟会议，现开放演讲提案征集，截止日期为 2026 年 8 月 3 日，会议将于 12 月 8 日至 10 日举行。演讲者将获得免费门票，所有演讲均以线上直播形式进行。

- 📢 **提案征集截止**：2026 年 8 月 3 日，会议日期为 12 月 8 日至 10 日，演讲者获免费门票。
- 🔍 **双盲评审**：评审过程隐藏作者身份，提案需包含标题、摘要、大纲等，避免透露个人信息。
- 🎤 **演讲类型**：30 分钟演讲，需明确主题、受众、类型和关键收获；摘要简短，描述需结构化。
- 🛠️ **教程类型**：90 分钟实践课程，需说明材料分发方式（如 GitHub 链接）和参与要求。
- 💡 **成功提案要点**：包括主题吸引力、目标受众、学习收获、背景知识要求及时间分配。
- ❌ **常见错误**：避免过长提案（建议 200 词内）、依赖未来工作、商业推销或重复已有演讲。
- 📝 **额外建议**：明确目标受众（如数据科学家）、使用清晰标题、寻求同行反馈，首次演讲者可申请指导。

---

### [停止到处检查 None - YouTube](https://www.youtube.com/watch?v=h8ZwhU3PpVw&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [Stop Checking for None Everywhere - YouTube](https://www.youtube.com/watch?v=h8ZwhU3PpVw&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

本頁面列出了 YouTube 平台的核心資訊與政策，涵蓋版權、聯絡方式、創作者支援及法律條款等面向。

- 📰 提供新聞中心，發布官方公告與更新
- ©️ 明確版權資訊與相關規範
- 📞 提供聯絡我們管道，處理用戶問題
- 🎬 支援創作者，提供相關資源與工具
- 📢 開放刊登廣告，協助品牌推廣
- 💻 提供開發人員技術文件與 API
- ⚖️ 列出使用條款與服務規範
- 🔒 說明私隱政策與數據保護措施
- 🛡️ 包含政策及安全指南，確保平台安全
- 🤖 說明 YouTube 的運作方式與演算法
- 🧪 提供測試新功能，邀請用戶參與
- ©️ 版權所有 © 2026 Google LLC

---

### [每个 Python 开发者都应了解的 CPython ABI 知识 | Labs](https://labs.quansight.org/blog/python-abi-abi3t?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [What Every Python Developer Should Know About the CPython ABI | Labs](https://labs.quansight.org/blog/python-abi-abi3t?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

### 概述总结
本文深入解析了 CPython ABI（应用程序二进制接口）的核心概念，以及它如何影响 Python 扩展模块的兼容性和分发。文章从 API 与 ABI 的区别讲起，逐步展开到 CPython C API 的五个层次、PyObject 结构体的演变、GIL（全局解释器锁）与自由线程构建的冲突，最后介绍了 Python 3.15 中为自由线程构建设计的新稳定 ABI（abi3t）。通过理解这些底层机制，开发者可以更好地管理二进制 wheel 的兼容性标签，并优化多版本支持策略。

- 📚 **ABI vs API**：ABI 是二进制级契约（符号名、结构体布局、调用约定），而 API 是源码级契约（函数签名、宏、类型）。ABI 不包含宏或内联函数，这些只在 API 中存在。
- 🔧 **CPython C API 的五层结构**：从内到外依次为内部 API（仅限 CPython 自身）、私有 API（以下划线开头，可随时变更）、不稳定 API（文档化但可能变化）、版本特定 API（稳定至下一个次要版本）、有限 API（稳定 ABI 的子集，承诺永久兼容）。
- 🧩 **PyObject 结构体的关键性**：所有 Python 对象在 C 中都是 PyObject 或扩展自它的结构体。其布局（引用计数 + 类型指针）是 ABI 兼容性的核心，任何改动都会导致扩展模块崩溃。
- ⚡ **GIL 与自由线程的冲突**：GIL 通过全局锁保护引用计数，但限制多核并行。自由线程构建移除了 GIL，采用偏置引用计数和每对象锁，这彻底改变了 PyObject 的布局（增加线程 ID、标志位、互斥锁等字段），导致与 GIL 构建的 ABI 不兼容。
- 🏷️ **wheel 标签的 ABI 含义**：`cp3XY`（版本特定 GIL 构建）、`cp3XYt`（版本特定自由线程构建）、`abi3`（稳定 ABI，兼容 GIL 构建的多个版本）、`abi3t`（Python 3.15 新增，兼容自由线程构建的多个版本）。纯 Python wheel 使用`py3-none-any`。
- 🔄 **自由线程构建的 ABI 挑战**：由于 PyObject 布局不同，自由线程 Python 3.13/3.14不支持有限API（abi3），迫使项目为每个Python版本和构建类型发布独立wheel（如cp314t）。
- 🛠️ **abi3t 的解决方案**：Python 3.15 通过将 PyObject 等结构体变为不透明类型，并引入`Py_TARGET_ABI3T`宏，创建了自由线程的稳定 ABI。这允许一个 wheel 同时兼容 GIL 和自由线程构建，无需依赖具体布局。
- 📦 **生态迁移建议**：项目应同时发布`abi3`（覆盖 GIL 构建的旧版本）、`cp314t`（覆盖自由线程 Python 3.14）和`cp315-abi3.abi3t`（覆盖 Python 3.15+ 的两种构建）。未来当 Python 3.15 成为最低版本后，可回归为单 wheel 分发。
- 🧰 **工具支持现状**：pip 26.1+、uv 0.11.3+ 已支持 abi3t 安装；PyO3/Maturin 完全支持；Scikit-build-core 1.0 已集成；Cython 处于实验分支；Setuptools 和 Meson-python 即将支持。

---

### [我们如何通过扇出扩展通知 | Patreon 上的 Patreon 工程](https://www.patreon.com/engineering/posts/how-we-scaled-162544709?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [How We Scaled Notifications with Fanout | Engineering at Patreon on Patreon](https://www.patreon.com/engineering/posts/how-we-scaled-162544709?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

Patreon 通过引入 Fanout 架构重构了通知平台，解决了大规模创作者通知的性能瓶颈，实现了水平扩展、渠道隔离和更好的可观测性，显著提升了推送和邮件通知的速度。

- 🚀 **性能大幅提升**：针对大型创作者，推送和应用内通知速度提升 **80%**，邮件通知速度提升 **55%**。
- 📈 **延迟增长可控**：当创作者受众增长 4 倍时，新平台端到端延迟仅增加 33%-60%，而旧平台增加 186%。
- 🧩 **Fanout 架构**：引入两层扇出机制，将收件人列表拆分为小批次，独立处理通知生成和交付，实现水平扩展。
- 🔌 **渠道隔离**：应用内、推送和邮件通知独立运行，单一渠道故障不会影响其他渠道。
- 🏭 **通知工厂抽象**：通过工厂模式分离平台编排与业务逻辑，提供统一 API（`send_fanout_notifications`），简化开发。
- 🔍 **可观测性增强**：引入计时和日志数据模型，支持端到端调试，使工程师能快速定位通知失败原因。
- 🤖 **AI 辅助迁移**：使用 AI 工具自动生成迁移代码，在 6 周内完成 80%（超过 200 个）通知的迁移。
- 👥 **跨团队协作**：涉及 10 个团队、30+ 工程师，通过领导层对齐、明确截止日期和迁移周活动，高效完成迁移。
- 🧠 **经验教训**：大型迁移需明确优先级；平台工作不止于 API，需注重可调试性；设计时应预判下一个瓶颈（如收件人列表生成）。
- 🔮 **未来规划**：将收件人列表生成纳入通知工厂，并优化开发者与粉丝的通知设置体验。

---

### [6 倍更快的二分查找：从编译代码到机械共情](https://pythonspeed.com/articles/branchless-binary-search/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [6× faster binary search: from compiled code to mechanical sympathy](https://pythonspeed.com/articles/branchless-binary-search/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

本文介绍如何通过理解 CPU 工作原理，将二分查找算法加速 6 倍。核心思路是消除分支预测错误、减少冗余计算，并利用 SIMD 指令集。

- 🚀 原始二分查找：使用标准算法，但存在 16.6% 的分支预测错误率，导致 CPU 无法高效并行执行指令。
- 🔄 无分支二分查找：通过固定迭代次数和条件选择指令消除分支，分支预测错误率降至 0%，IPC 提升至 4.0，速度提升 3.5 倍。
- ⚡ 消除边界检查：使用 unsafe 代码绕过内存安全校验，减少约 7000 万条 CPU 指令，速度再提升 30%。
- 🧩 SIMD 自动向量化：通过调整循环结构并启用现代 CPU 指令集，编译器自动生成 SIMD 指令，最终版本比原始代码快 6 倍。
- 📚 学习资源推荐：推荐《计算机系统：程序员的视角》《现代 CPU 性能分析与调优》等书籍，以及作者新书《Python 性能实践》。

---

### [非 HTML 内容](https://arxiv.org/pdf/2607.05391)

**原文标题**: [Non-HTML content](https://arxiv.org/pdf/2607.05391)

无法总结：非 HTML 内容。

---

### [错误](https://blog.pythonlibrary.org/2026/07/10/an-intro-to-spiel-creating-presentations-in-your-terminal-with-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [Error](https://blog.pythonlibrary.org/2026/07/10/an-intro-to-spiel-creating-presentations-in-your-terminal-with-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='blog.pythonlibrary.org', port=443): Max retries exceeded with url: /2026/07/10/an-intro-to-spiel-creating-presentations-in-your-terminal-with-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [媒介](https://blog.dataengineerthings.org/how-airflow-is-using-ai-to-make-data-engineering-more-resilient-not-more-complex-36ff44fd8df7?gi=a8c3d04b3d26&utm_campaign=python-weekly-issue-754-july-16-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

**原文标题**: [Medium](https://blog.dataengineerthings.org/how-airflow-is-using-ai-to-make-data-engineering-more-resilient-not-more-complex-36ff44fd8df7?gi=a8c3d04b3d26&utm_campaign=python-weekly-issue-754-july-16-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

概述总结
- 🤖 **AI 辅助管道健康循环**：Apache Airflow 通过检测、恢复和修复三大 AI 能力，构建自主管道健康循环，无需改变现有数据工程架构。
- 🔍 **检测数据漂移**：`LLMSchemaCompareOperator`利用 LLM 语义理解自动比较跨数据库/格式的 Schema，在数据加载前捕获兼容性问题，避免静默数据损坏。
- ⏸️ **断点续传**：Airflow 3.3 的 Task State Store 支持任务失败后重连外部作业（如 Spark），无需从头重启，显著降低长耗时任务的计算成本和 SLA 延误。
- 🛠️ **智能重试策略**：`LLMRetryPolicy`将团队运行手册编码为指令，自动分类错误（如认证失败立即终止、限流按需延迟重试），替代传统固定重试逻辑。
- 📋 **运行手册自动化**：将 2am 故障处理知识（如认证、网络、数据错误分类）转化为代码化的重试策略，减少人工干预和响应时间。
- 🔗 **协同效应**：检测→恢复→修复形成闭环，从源头阻止问题传播，高效恢复中断任务，智能响应故障，整体提升管道韧性。
- 🚀 **即用集成**：Schema 验证（0.4.0 版）、Task State Store 和 LLM 重试策略（3.3.0b1 版）可直接通过 pip 安装，无需构建独立 AI 应用。

---

### [Python 3.15 的超低开销解释器性能分析模式 | Ken Jin 的博客](https://fidget-spinner.github.io/posts/ultra-fast-tracing.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [Python 3.15’s Ultra-Low Overhead Interpreter Profiling Mode | Ken Jin’s Blog](https://fidget-spinner.github.io/posts/ultra-fast-tracing.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

Python 3.15 引入了一种超低开销的解释器性能分析模式，通过双分发表技术实现高效的 JIT 编译追踪，性能损耗远低于传统方案。

- 🚀 Python 3.15 JIT 通过新型解释器性能分析模式实现适度加速，该模式专为 JIT 编译记录执行路径而设计
- 🔄 传统两种方案（双解释器/性能分析模式）各有缺陷：双解释器导致代码膨胀和 6% 性能下降，性能分析模式会干扰正常执行
- 💡 创新性双分发表方案：通过交换分发表实现模式切换，第二张表将所有指令映射到单一记录指令，形成“扇入 - 扇出”模型
- ⚡ 性能测试显示：性能分析模式仅比纯解释器慢 4.5 倍（1.72μs vs 7.47μs），远优于 PyPy 的 900-1000 倍减速
- 🧩 该技术不仅限于追踪记录，还可用于低开销运行时类型分析等场景，无需重写解释器
- 🤔 作者反思该系统的复杂性，虽优雅但难以推理，未来将分享更多关于追踪的思考

---

### [Django：介绍 django-orjson - Adam Johnson](https://adamj.eu/tech/2026/07/15/introducing-django-orjson/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [Django: introducing django-orjson - Adam Johnson](https://adamj.eu/tech/2026/07/15/introducing-django-orjson/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

本文介绍了 django-orjson 库，它通过集成更快的 Rust 实现 orjson 来提升 Django 的 JSON 处理性能，并提供了一系列即插即用的替代组件。

- 🚀 **性能提升**：orjson 比 Python 内置 json 模块快 10 倍序列化和 2 倍反序列化，django-orjson 让 Django 开发者轻松获得这一性能优势。
- 🔧 **即插即用组件**：提供 JsonResponse、测试客户端、模板标签等替代品，支持 Django 和 Django REST Framework，且经过全面测试。
- 📈 **实际效益**：虽然数据库查询占主导，但 JSON 处理时间仍可显著减少，采用 orjson 是几乎免费的性能优化。
- 💡 **社区推动**：Paolo Melchiorre 提议在 Django 核心中支持可插拔 JSON 后端，该提案已获得 14 个点赞，欢迎参与讨论。
- 🎯 **试用邀请**：鼓励立即试用 django-orjson 并反馈意见，同时提供相关资源链接。

---

### [用 C 语言为 Python 构建快速 HTML 工具包 · Bernát Gábor — Python 打包、tox、virtualenv 与开源](https://bernat.tech/posts/blazing-fast-html-parser/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [Building a fast HTML toolkit in C for Python · Bernát Gábor — Python packaging, tox, virtualenv & open source](https://bernat.tech/posts/blazing-fast-html-parser/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

turbohtml 是一个用 C 语言构建的快速 HTML 工具包，比 Python 标准库快 3-22 倍，核心技巧是跳过不必要的工作：批量扫描、SIMD 加速、精确测量后再写入，并支持自由线程和恶意输入防护。

- 🚀 **性能飞跃**：turbohtml 在 HTML 转义、反转义、分词等操作上比 Python 标准库快 3-22 倍，例如纯文本转义快 22 倍，典型标记分词快 14.8 倍。
- ⚡ **批量扫描技巧**：使用 SWAR（8 字节一次减法）和 SIMD（16 字节一次洗牌）技术批量检查字节块，干净块几乎零成本，避免逐字符分支。
- 📏 **两遍测量法**：第一遍精确计算输出大小，第二遍一次性分配并批量复制干净区域，避免动态缓冲区的重复复制和边界检查。
- 🔍 **分词器优化**：实现 WHATWG 规范状态机，按字符宽度编译三个专用版本，文本运行批量扫描，零拷贝切片指向输入，仅按需构建 Python 对象。
- 🧩 **内存与对象复用**：标签名内联为整数，一次构建 ID 索引将 O(N²) 路径遍历变为线性，包装对象通过空闲列表回收，单次分配整个令牌。
- 🌐 **标准处理能力**：支持 Punycode、Unicode 标准化和韩文算术处理，Unicode 表在构建时生成，确保运行时简单高效。
- 🔧 **构建与基准测试**：使用 LTO 和 PGO 优化机器码，CI 通过 Callgrind 计数指令防止回归，确保基准测试在噪声环境中可靠。
- 🧵 **自由线程支持**：无共享可变状态，声明 `Py_MOD_GIL_NOT_USED`，在无 GIL 构建上运行而不强制重新锁定，并通过 ThreadSanitizer 验证。
- 🛡️ **恶意输入防护**：限制嵌套深度、线性时间去重属性、每个缓冲区进行溢出检查，并通过 DOMPurify 的 XSS 语料库验证消毒器安全性。
- 🤖 **AI 辅助构建**：turbohtml 由 Claude (Opus 4.8) 在一个月内通过近 300 次迭代生成，作者审查代码并确保正确性，所有技术均借鉴自现有最佳实践。

---

### [使用 AST 分析和 linter 禁止提交/交易](https://www.droppedasbaby.com/posts/db-commits/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [Ban commits/transactions using AST analysis and linters](https://www.droppedasbaby.com/posts/db-commits/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

本文強調資料庫層必須完全掌控所有交易與提交，並透過 AST 分析和 linter 強制執行規則，以避免因程式碼組織不當導致的原子性問題和資料遺失。

- 🚫 禁止在資料庫層外部手動提交或交易，避免原子性被破壞
- 🧩 不要將資料庫模型傳遞出資料庫層，防止隱藏寫入
- 🔍 使用 AST 分析或 flake8 linter，全面禁止手動提交、外部存取 session 和交易
- 📋 透過自訂測試或 linter 擴充，檢查程式碼中是否有違規的 commit() 呼叫
- 🤖 結合 LLM 支援，檢查資料庫層是否返回資料庫模型而非領域模型
- 📚 推薦閱讀《領域驅動設計》以改善程式碼組織
- ⚠️ 核心原則：資料庫抽象層擁有所有提交和交易的控制權

---

### [GitHub - generative-computing/mellea: Mellea 是一个用于编写生成式程序的库。](https://github.com/generative-computing/mellea?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - generative-computing/mellea: Mellea is a library for writing generative programs. · GitHub](https://github.com/generative-computing/mellea?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

Mellea 是一个用于构建可预测、结构化 AI 工作流的 Python 库，专注于解决 LLM 调用的不可靠性问题。

- 🤖 **结构化输出** — 使用 `@generative` 装饰器将类型化函数转为 LLM 调用，Pydantic 模式在生成时强制验证输出
- ✅ **需求验证与自动修复** — 为任意调用附加自然语言需求，Mellea 自动验证并在失败时重试
- 🎯 **采样策略** — 支持多次生成并选择最佳结果，可一键切换拒绝采样、多数投票等策略
- 🔌 **多后端支持** — 兼容 Ollama、OpenAI、HuggingFace、WatsonX、LiteLLM、Bedrock 等多种后端
- 🔗 **遗留系统集成** — 通过 `mify` 工具轻松将 Mellea 嵌入现有代码库
- 🛠️ **MCP 兼容** — 可将任意生成式程序暴露为 MCP 工具
- 📚 **丰富资源** — 提供完整文档、Colab 笔记本、代码示例（RAG、代理、IVR 等）
- 🌍 **开源社区** — 由 IBM Research 发起，采用 Apache-2.0 许可，欢迎贡献

---

### [GitHub - cognizant-ai-lab/neuro-san-studio: 神经禅工作室 · 一个用于神经禅的游乐场](https://github.com/cognizant-ai-lab/neuro-san-studio?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - cognizant-ai-lab/neuro-san-studio: A playground for neuro-san · GitHub](https://github.com/cognizant-ai-lab/neuro-san-studio?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

Neuro SAN Studio 是一個用於設計、測試和部署多智能體系統的開源平台，基於 Neuro SAN 框架，支援低程式碼配置、自適應通訊和雲端部署。

- 🚀 **快速建構多智能體網絡**：透過 HOCON 聲明式配置，讓技術與非技術人員都能在數分鐘內設計複雜的智能體協作系統。
- 🔀 **自適應通訊協議（AAOSA）**：智能體自主決定任務委派方式，實現動態、去中心化的互動決策。
- 🔒 **Sly-Data 安全資料處理**：在智能體間安全傳輸敏感資料，避免直接暴露給語言模型。
- 🧩 **動態智能體網絡設計器**：內建元智能體，可根據高階描述自動生成新的自訂智能體網絡。
- 🛠️ **靈活的工具整合**：支援自訂 Python 工具、API、資料庫，以及 Agentforce、CrewAI、MCP 等外部智能體生態系統。
- 📈 **強大的可追溯性**：提供詳細日誌、追蹤和會話級指標，增強透明度和除錯能力。
- 🌐 **雲端無關且可擴展**：相容多種 LLM 提供商（OpenAI、Anthropic、Azure 等），可部署於本機、容器或雲端基礎設施。
- 📦 **簡易安裝與命令列工具**：使用 `uv` 安裝，並提供 `ns init`、`ns run`、`ns import` 等指令，快速初始化、啟動伺服器及匯入智能體網絡。
- 🎯 **多種行業應用案例**：涵蓋航空客服、銀行合規、零售營運、電信支援等領域，並提供現成範例。

---

### [GitHub - Soju06/codex-lb: 支持使用追踪、仪表盘及 OpenCode 兼容端点的 Codex/ChatGPT 多账户负载均衡器与代理](https://github.com/Soju06/codex-lb?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - Soju06/codex-lb: Codex/ChatGPT multiple account load balancer & proxy with usage tracking, dashboard, and OpenCode-compatible endpoints · GitHub](https://github.com/Soju06/codex-lb?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

codex-lb 是一个用于 ChatGPT 账号的负载均衡器，支持多账号池化、用量追踪、API 密钥管理，并提供仪表盘界面，兼容 OpenAI 客户端。

- 🔄 **账号池化**：在多个 ChatGPT 账号间进行负载均衡
- 📊 **用量追踪**：追踪每个账号的令牌、成本及 28 天趋势
- 🔑 **API 密钥管理**：按令牌、成本、窗口和模型设置每个密钥的速率限制
- 🛡️ **仪表盘认证**：支持密码及可选的 TOTP 双重认证
- 🔗 **OpenAI 兼容**：兼容 Codex CLI、OpenCode 等任何 OpenAI 客户端
- 🔄 **自动模型同步**：自动从上游获取可用模型
- 🚀 **快速部署**：支持 Docker 和 uvx 方式快速启动
- 📚 **完整文档**：提供从入门到部署的详细指南
- 👥 **社区贡献**：拥有众多贡献者，欢迎各种形式的贡献

---

### [GitHub - xchwarze/magic-extractor：通用Windows提取工具，可检测未知文件并将其路由到正确的捆绑提取器。](https://github.com/xchwarze/magic-extractor?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - xchwarze/magic-extractor: Universal Windows extraction tool that detects unknown files and routes them to the right bundled extractor. · GitHub](https://github.com/xchwarze/magic-extractor?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

Magic Extractor 是一款通用的 Windows 提取工具，能自动识别 80 多种文件格式并调用合适的解压器，支持归档、安装包、磁盘镜像、邮件存储等多种类型。

- 🎯 自动检测 80+ 格式：涵盖主流压缩格式、安装程序、磁盘镜像、法医镜像、邮件存储和现代编解码器
- 🔍 多引擎分层检测：按顺序使用 puremagic、内置签名、DIE、binwalk 和 Magika，首次命中即退出
- 📂 四种操作模式：支持 extract（提取）、identify（识别）、list（列出内容）和 carve（从固件等文件中提取嵌入数据）
- 🧩 递归与暴力提取：--recursive 可解压输出中的嵌套归档，--bruteforce 尝试所有匹配处理器
- 🖥️ 可选图形界面：基于 tkinter 的 GUI 支持拖放、批量队列、运行历史和偏好设置
- 🛠️ 易于扩展：通过添加 handler 模块和检测声明即可支持新格式，文档提供了完整指南
- 📦 便携式发布：编译版本将 bin/、data/ 和 config.ini 保留在 exe 外部，便于更新
- 🔐 密码与日志支持：支持加密归档密码、输出文件夹自动打开、空间检查和日志记录

---

### [GitHub - ail-project/tempolocus: Tempolocus 是一个时间序列活动模式与近似位置推断工具](https://github.com/ail-project/tempolocus?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - ail-project/tempolocus: Tempolocus is a time-series activity patterns and approximate location inference · GitHub](https://github.com/ail-project/tempolocus?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

tempolocus 是一个通过分析时间序列活动模式来推断地理位置的 Python 工具，支持多种输入格式和区域分析。

- 📊 **输入格式多样**：支持每周小时桶、每年每日桶和时间戳列表三种 JSON 格式输入，也可直接导入纯文本时间戳文件。
- 🌍 **时区与区域推断**：每周数据可排名时区偏移和 IANA 时区，并列出可能国家；每年数据通过公共假日日历对比活动模式来推断区域。
- 🎯 **活动类型分类**：输出包含 `work-time`、`vacation-time` 或 `mixed-time` 的通用活动类型分类，基于工作日/周末活动对比。
- 🗺️ **支持多区域假日分析**：涵盖非洲、亚太、欧洲、北美、中东、南美等地区的公共假日，可选用 `public-worker` 配置文件增加公共部门假日参考。
- ⚙️ **灵活的参数配置**：支持 `--activity-signal peak` 匹配假日高峰活动，`--holiday-profile public-worker` 增加公共部门假日，`--top` 控制输出候选数量。
- 🐍 **Python 库接口**：提供 `detect`、`analyze_activity` 和 `load_json` 三个主要入口函数，适合集成到 Web 服务、笔记本或管道中。
- 📝 **示例丰富**：包含命令行和 Python 代码示例，涵盖每周、每年和时间戳输入的使用场景。
- 📜 **开源许可**：采用 GNU Affero General Public License v3.0 或更高版本授权。

---

### [GitHub - dekart-xyz/geosql: 将 Claude/Codex 转变为地理空间分析代理。](https://github.com/dekart-xyz/geosql?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - dekart-xyz/geosql: Turn Claude/Codex into geospatial analytics agent. · GitHub](https://github.com/dekart-xyz/geosql?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

GeoSQL 是一个面向数据科学家和分析师的地理空间分析技能工具，支持 Claude、Codex 和 GitHub Copilot，可在 PostGIS、BigQuery、Snowflake 和 Wherobots 上运行，无需 SaaS 账户，完全本地或自托管。

- 🗺️ **4 倍性能提升**：通过地图循环反馈机制，将地理空间任务准确率提高 4 倍，地图渲染帮助代理自我纠正几何错误。
- ⚡ **快速安装与启动**：使用 `pip install geosql && geosql` 即可安装，支持交互式模式，自动检测并配置代理。
- 🏢 **多数据库支持**：兼容 PostGIS、BigQuery、Snowflake 和 Wherobots，可连接 Overture Maps 共享数据和私有表。
- 💰 **成本控制**：在 BigQuery 上自动进行预运行估算，默认强制执行 10 GiB 计费上限，超预算查询会被重写为更经济的版本。
- 🔍 **智能元数据发现**：自动探索仓库元数据（表、列、类型），无需猜测模式，支持空间 SQL 函数如 `ST_INTERSECTS`、`ST_DISTANCE` 和 H3。
- 🧪 **可复现评估套件**：内置 `evals/` 目录，包含 8 个测试用例，通过率 100%，平均每轮 3,085 个 token 和 72 秒时长。
- 🔒 **安全认证**：使用本地 CLI 认证（`bq`、`snow`、`dekart`），仓库凭证不会传输到代理。
- 🎯 **示例提示**：支持房地产分析、选址、EV 充电基础设施等多种地理空间查询，并渲染地图。

---

### [GitHub - cactus-compute/needle: 适用于微型设备的 2600 万参数智能体模型](https://github.com/cactus-compute/needle?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - cactus-compute/needle: 26m agentic model for tiny devices · GitHub](https://github.com/cactus-compute/needle?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

Needle 是一个仅有 2600 万参数的轻量级 AI 模型，专为消费设备上的单次函数调用任务设计，可在本地微调并高速推理。

- 🧠 **超轻量架构**：基于“简单注意力网络”，仅 26M 参数，可在 Mac/PC 本地微调，推理速度达 6000 toks/s（预填充）和 1200 toks/s（解码）。
- 🎯 **专注单次函数调用**：在个人 AI 场景中，单次函数调用能力超越 FunctionGemma-270m、Qwen-0.6B 等更大模型，但对话能力较弱。
- 🛠️ **快速上手**：通过 `needle playground` 启动 Web UI，即可测试和微调；Python 调用仅需几行代码。
- 📊 **微调数据要求**：每个工具至少提供 120 个示例（100 训练/10 验证/10 测试），需多样化查询措辞，避免过拟合。
- 📦 **完整工具链**：提供 CLI 命令进行训练、微调、推理、评估、数据生成和 TPU 管理，权重完全开源。
- 🔬 **实验性质**：旨在重新定义消费设备（手机、手表、眼镜）上的微型 AI，仍处于实验阶段，小模型可能不稳定。

---

### [GitHub - robertsdotpm/runloom: 适用于 Python 3.13t+ 自由线程的实时协程](https://github.com/robertsdotpm/runloom?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - robertsdotpm/runloom: Real Goroutines for Python 3.13t+ free-threaded. · GitHub](https://github.com/robertsdotpm/runloom?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

runloom 是一个为 Python 3.13t+ 自由线程环境设计的 Go 风格协程库，支持阻塞式代码、多核并行和高效调度。

- 🚀 **性能对标 Go**：纯 C 协程创建速度达 2.29 M/s，超越 Go 的 2.10 M/s；上下文切换约 75 ns，与 Go 持平。
- 💻 **多核并行**：利用自由线程 CPython（GIL 关闭），通过 M:N 工作窃取调度器在多个核心上并行运行百万级协程。
- 🔧 **阻塞代码无痛迁移**：通过 `monkey.patch()` 使标准库（如 socket、time）变为协作式，无需 `async/await` 即可运行现有阻塞代码。
- ⚡ **高效 I/O**：内置 netpoll（epoll/kqueue/IOCP），协程在等待文件描述符时自动挂起，无锁竞争。
- 📦 **Go 风格通道**：支持 `Chan(capacity)`、`select` 和 `for v in ch`，简化并发通信。
- 🧠 **内存优化**：提供 `optimize("memory")` 模式，使用小型栈；但空协程内存（8.8 KB）约为 Go（2.7 KB）的 3.3 倍。
- 🛡️ **故障隔离**：单个阻塞调用仅影响其所在 hub，运行时自动检测并恢复，避免全局崩溃。
- 🌐 **跨平台支持**：支持 Linux、macOS、Windows、FreeBSD 等，主要针对 Linux x86_64 优化。
- 📚 **丰富文档**：包含快速入门、异步桥接、通道、M:N 并行等完整指南，便于学习和使用。
- 🎯 **限制明确**：多核优势需自由线程 CPython 3.13t；纯 Python 代码性能受限于 CPython 本身（约 80k ops/s/core）。

---

### [GitHub - servletcloud/fstache: 适用于 Python 3.12+ 的快速无依赖、类型化 Mustache 渲染器](https://github.com/servletcloud/fstache?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - servletcloud/fstache: Fast dependency-free, typed Mustache renderer for Python 3.12+ · GitHub](https://github.com/servletcloud/fstache?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

Fstache 是一个为 Python 3.12+ 设计的高性能、零依赖的 Mustache 模板渲染器，专注于服务器端渲染场景，速度比同类库快 3 倍以上，支持标准 Mustache 规范（除继承外），并提供简洁的 API 和 CLI 工具。

- 🚀 **极致性能**：在相同硬件上，Fstache 的渲染速度是 Chevron 的 3.3 倍、Pystache 的 3.5 倍，工作站测试可达每秒 4066 次渲染。
- 🧩 **零依赖纯 Python**：无需任何外部库，完全用 Python 实现，符合 PEP 561 类型标注，易于集成和维护。
- 📜 **完整 Mustache 支持**：支持变量、段落、反向段落、Lambda、动态部分名、分隔符变更等标准特性，但不支持模板继承。
- ⚡ **智能预加载与流式输出**：生产模式下预编译所有模板，支持 `iter_chunks()` 流式输出，避免内存缓冲，适合 Web 响应。
- 🛠️ **灵活配置工厂**：提供 `create_prod_renderer`、`create_dev_renderer`、`create_test_renderer` 三种预设工厂，以及可自定义的 `create_renderer`，支持缺失变量/模板处理、自定义转义、分隔符等。
- 💻 **CLI 工具**：内置 `fstache render` 命令，支持从 stdin 读取模板、JSON 数据文件、扩展名处理，适合脚本和管道使用。
- 📦 **轻量级安装**：通过 `pip install fstache` 即可安装，PyPI 包仅包含核心功能，无额外依赖。
- 🔧 **低层级 API**：提供 `compile` 和 `render` 函数，允许开发者自行管理模板缓存和加载逻辑，适合高级定制场景。

---

### [GitHub - apache/ossie: Apache Ossie，一项行业范围内的规范工作，旨在标准化我们在分析、人工智能和商业智能平台之间交换语义元数据的方式，为语义数据提供供应商中立、单一的真实来源 · GitHub](https://github.com/apache/ossie?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - apache/ossie: Apache Ossie, industry wide specification effort to standardize how we exchange semantic metadata across analytics, AI and BI platforms, providing a vendor neutral, single source of truth for semantic data · GitHub](https://github.com/apache/ossie?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

Apache Ossie 是一个开源项目，致力于标准化数据分析和 AI 生态中的语义模型交换，提供厂商中立的单一事实来源。

- 📘 核心规范：提供基于 JSON 和 YAML 的单一规范，包括核心 spec.md、机器可读 schema 和文档。
- 🔄 转换器：包含参考转换器，支持 dbt、GoodData、Polaris、Salesforce 等格式的互转。
- 📂 示例模型：提供完整的 TPC-DS 语义模型示例。
- ✅ 验证工具：提供验证语义模型是否符合 Ossie schema 的工具。
- 🌐 社区参与：通过 CONTRIBUTING.md 贡献代码，ROADMAP.md 查看路线图，GitHub Discussions 和 Slack 讨论交流。
- 🏷️ 主题标签：metadata、semantic，采用 Apache-2.0 许可证。
- ⭐ 项目状态：899 星标、134 分支、38 关注，主要语言为 Python (74.1%) 和 Java (25.9%)。

---

### [GitHub - nMaroulis/protolink: 构建具有原生代理间（A2A）通信能力的自主 Python 代理](https://github.com/nMaroulis/protolink?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

**原文标题**: [GitHub - nMaroulis/protolink: Build autonomous Python agents with native Agent-to-Agent (A2A) communication · GitHub](https://github.com/nMaroulis/protolink?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-754-july-16-2026)

ProtoLink 是一个以 A2A 协议为核心的轻量级 Python 框架，用于构建可插拔的智能体与多智能体系统，强调本地优先、模型无关和显式可控。

- 🧩 **可插拔设计**：智能体由独立模块组成，LLM、工具、传输、存储、遥测等均可按需替换，无需强制采用完整技术栈。
- 📦 **简洁稳定 API**：常用路径使用字符串别名，复杂场景可调用具体实现，保持接口小而稳定。
- 🌐 **本地优先，分布式可选**：开发时无需网络或模型提供商，随后可将相同任务契约迁移至 HTTP、SSE、WebSocket 或 gRPC。
- 🤖 **对小模型友好**：采用单步推理、JSON 回退和确定性流程，减少对隐藏提示行为的依赖，支持 Ollama、llama.cpp 等本地模型。
- 🔍 **显式可审查**：工具调用、任务状态、策略决策、审批、运行时事件等均有类型化表示，便于调试和审计。
- 🔗 **A2A 为核心**：智能体通过 AgentCard、Task、Message 等标准原语通信，而非框架私有的图状态，并支持标准 A2A 1.0 协议兼容。
- ⚙️ **结构化流程**：提供 Pipeline、Parallel、Router、Graph 等确定性拓扑，保持每一步基于 Task 契约。
- 📊 **本地遥测与重放**：内置无依赖的本地追踪，可捕获跨度并重放，无需外部服务。
- 🖥️ **开发者仪表盘**：CLI 命令提供本地浏览器 UI，查看智能体健康、任务历史、追踪摘要和运行重放。

---

