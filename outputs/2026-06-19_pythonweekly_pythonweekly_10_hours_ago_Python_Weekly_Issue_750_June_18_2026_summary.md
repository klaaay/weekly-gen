### [Python 3.14 垃圾回收的繁琐流程 - 共识](https://theconsensus.dev/p/2026/06/06/python-3-14-garbage-collection-rigamarole.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [
    Python 3.14 garbage collection rigamarole - The Consensus
  ](https://theconsensus.dev/p/2026/06/06/python-3-14-garbage-collection-rigamarole.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

Python 3.14.0 引入了增量垃圾回收器，但因用户报告内存压力，在 3.14.5 中回滚。本文探讨了 Python 内存管理机制，以及增量 GC 在不同工作负载下的表现。

- 🐍 **Python 3.14 的 GC 变更**：从传统的分代 GC 改为增量 GC，旨在减少大堆的暂停时间，但导致内存使用增加。
- 🔄 **引用计数基础**：Python 对象通过引用计数管理内存，变量赋值或删除会增减计数，但循环引用会导致内存泄漏。
- 🔗 **循环引用问题**：引用计数无法处理循环引用，需依赖 GC 回收，可通过弱引用避免。
- 📊 **分代 GC 机制**：传统 GC 按对象存活时间分代收集，增量 GC 将年轻代和旧代合并，每次只收集部分旧代。
- ⏱️ **暂停时间对比**：增量 GC 在最佳情况下显著降低最大暂停时间（如从 3.9ms 降至 1.4ms），但平均暂停时间可能增加。
- 💾 **内存压力问题**：增量 GC 在频繁创建旧垃圾的工作负载中，内存使用更高（如 27.1MB vs 20.8MB），大对象场景更明显（2849.4MB vs 717.0MB）。
- ❌ **回滚原因**：因内存压力问题，且未提供用户切换选项，Python 团队在 3.14.5 中回滚了增量 GC 更改。

---

### [Python ast 模块教程：在运行时转换和运行代码](https://pydantic.dev/articles/eval-type-backport?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Python ast Module Tutorial: Transform and Run Code at Runtime](https://pydantic.dev/articles/eval-type-backport?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

### 概述摘要
本文详细介绍了如何使用 Python 的`ast`模块解析、修改和执行代码，并通过`eval-type-backport`库和调试转换器两个实例展示了其强大功能。作者还分享了个人经历，说明掌握 AST 技术对职业发展的重要性，尤其是在 AI 时代，元编程技能能提升代码的可控性和可观察性。

- 🔧 **核心示例：eval-type-backport 库**  
  通过 AST 将`X | Y`转换为`typing.Union[X, Y]`，使旧版 Python 支持新类型语法。

- 🛠️ **AST 模块基础操作**  
  使用`ast.parse`解析代码为抽象语法树，通过`ast.dump`可视化结构，并演示如何手动构建 AST 节点。

- 🔄 **递归转换 AST**  
  通过继承`ast.NodeTransformer`并重写`visit_BinOp`方法，自动将`|`运算符替换为`safe_or`函数调用。

- ⚡ **执行转换后的 AST**  
  使用`compile`将 AST 编译为代码对象，再通过`eval`执行，需注意添加`ast.fix_missing_locations`修复位置信息。

- 🐞 **调试示例：打印子表达式**  
  通过`DebugTransformer`重写`generic_visit`，在运行时输出每个子表达式的值和源码，便于调试。

- 💼 **个人经历与职业价值**  
  作者通过 AST 技术获得工作机会（如 Grist、Pydantic），并强调该技能在 AI 时代的重要性，例如用于 AI 代理的代码生成与监控。

- 🤖 **AI 时代的应用前景**  
  AST 可用于分析 AI 生成的代码（如 Pydantic AI 的 Code Mode），提升代码的可控性和可观察性，避免自然语言输出的不确定性。

---

### [我是如何将 Python 依赖注入速度提升 130 倍的](https://vshulcz.hashnode.dev/python-dependency-injection-130x-faster?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [How I made Python dependency injection 130× faster](https://vshulcz.hashnode.dev/python-dependency-injection-130x-faster?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

以下是对该文章的概述总结：

- 📊 **性能提升 130 倍**：通过缓存依赖图、移除无效检查、编译依赖图，将依赖注入性能从约 53 微秒/次降至 0.40 微秒/次，接近手动注入速度（0.27 微秒/次）。
- 🔍 **测量驱动优化**：初始直觉认为容器开销大，实际测量显示 200 倍差距，但 99% 的开销可通过缓存依赖计划消除（从 52.9 降至 0.818 微秒/次）。
- 🛡️ **移除不可能触发的检查**：在快速路径中删除了循环检测，因为该路径的依赖图已预先证明无环，避免无意义的运行时开销。
- ⚡ **消除每次调用时的分配**：将类型到构造函数的直接映射存储为字典，避免每次解析时创建元组键和额外属性读取。
- 🔧 **编译依赖图**：将瞬态依赖链合并为单一扁平函数，实现公共子表达式消除，性能从 0.818 降至 0.401 微秒/次。
- 🧪 **等价模糊测试保障安全**：通过 4000 个随机图的结构化比较，确保`exec`生成的代码不会静默产生错误对象，避免生产环境中的隐性故障。
- ⚠️ **诚实限制**：优化仅适用于瞬态链和共享单例；对于作用域、异步资源或工厂注入，性能提升有限，且纯 Python 下限约 0.4 微秒。
- 💡 **核心启示**：先测量再优化；移除不可能执行的代码；`exec`代码生成必须配合等价模糊测试，而非仅凭直觉。

---

### [在 Django 中使用 importmaps 的 2026 年方式 - Matthias Kestenholz](https://406.ch/writing/the-2026-way-of-using-importmaps-in-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026#the-2026-way-of-using-importmaps-in-django)

**原文标题**: [The 2026 way of using importmaps in Django - Matthias Kestenholz](https://406.ch/writing/the-2026-way-of-using-importmaps-in-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026#the-2026-way-of-using-importmaps-in-django)

以下是对您提供的文章内容的总结：

概述总结  
- 📅 文章发布于 2026 年 6 月 17 日，讨论了 Django 中 importmap 的使用方式演变。  
- 🔄 主要介绍了 django-js-asset 4.0 版本，该版本放弃了全局 importmap，改为按上下文生成特定 importmap。  
- 🧩 新版本通过 ImportMap 对象和 js_asset.Media 类实现 importmap 的自动合并，确保在页面中只生成一个有效的 importmap。  
- 🛠️ 在 Django 管理界面外使用时，需手动添加 importmap 到模板上下文；在管理界面内则自动工作。  
- 🔗 通过自定义上下文处理器或视图，可以合并多个 importmap 条目，支持使用 static_lazy 实现延迟路径解析。  
- 🎯 强调 importmap 必须出现在所有 JavaScript 模块之前，且浏览器只支持单个 importmap。  
- 🚀 未来希望将 importmap 支持标准化并纳入 Django 核心，避免生态碎片化。

---

### [使用 pytest 进行 Python 测试：从基础到高级技巧 | Andros Fenollosa](https://en.andros.dev/blog/b6bf68de/testing-in-python-with-pytest-from-the-basics-to-advanced-techniques/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Testing in Python with pytest: from the basics to advanced techniques | Andros Fenollosa](https://en.andros.dev/blog/b6bf68de/testing-in-python-with-pytest-from-the-basics-to-advanced-techniques/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本文全面介绍了使用 pytest 进行 Python 测试的核心技巧，从基础到高级，涵盖测试库、测试结构、数据生成、模拟外部依赖和快照测试等关键内容。

- 🧪 **核心测试库**：pytest 是主要框架，搭配 pytest-xdist（并行测试）、pytest-asyncio（异步测试）、respx（模拟 HTTP 请求）、faker（生成假数据）和 hypothesis（属性基测试）等工具可扩展测试能力。
- 📝 **测试结构规范**：测试文件以 `test_` 开头或 `_test.py` 结尾，测试函数以 `test_` 开头，并遵循“给定 - 当 - 然后”三部分结构，确保测试清晰可维护。
- 🔄 **复用测试对象**：使用 pytest fixture 创建可复用的测试对象，避免重复代码（DRY 原则），并借助 polyfactory 自动生成 Pydantic 模型或数据类的测试实例。
- 🎯 **三角化与参数化**：三角化通过编写三个通过测试逐步完善代码；参数化使用 `@pytest.mark.parametrize` 用不同数据运行同一测试，减少重复。
- 🔌 **抽象与协议**：测试应针对抽象接口（如 Protocol）而非具体实现，通过依赖注入解耦代码，使测试更稳定、易维护。
- 📊 **测试数据生成**：faker 生成随机数据，hypothesis 自动生成边界和边缘用例，覆盖硬编码数据无法触及的场景。
- ⏰ **处理非确定性元素**：使用包装器（如 FixedTimeProvider）或 time-machine 库固定日期、时间或随机数，确保测试可重复。
- 🎭 **模拟外部依赖**：通过 unittest.mock 的 create_autospec 创建模拟对象，或使用 respx 模拟 HTTP 请求，避免直接调用外部 API，提升测试速度和可靠性。
- 🗂️ **快照测试**：使用 syrupy 库比较函数输出与保存的快照，适用于复杂响应（如 API 输出、CSV 文件），简化断言并检测意外变更。
- ⚡ **性能优化**：使用 pytest-xdist 并行运行测试，通过 `pytest -n auto` 利用多核加速，保持测试套件快速、隔离和确定性。

---

### [嵌套循环不是问题所在。这才是。- YouTube](https://www.youtube.com/watch?v=095HrcWwHLI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Nested Loops Aren’t the Problem. This Is. - YouTube](https://www.youtube.com/watch?v=095HrcWwHLI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本頁面列出了 YouTube 平台相關的基礎資訊與政策連結，包括版權、聯絡方式、創作者資源及使用條款等。

- 📰 提供新聞中心連結，供用戶獲取最新官方消息
- ©️ 說明版權相關資訊與規範
- 📧 提供聯絡我們的方式
- 🎬 為創作者提供專屬資源與支援
- 📢 說明刊登廣告的相關選項
- 🛠️ 提供開發人員相關工具與文件
- 📜 列出使用條款與服務規範
- 🔒 說明私隱政策與資料保護措施
- 🛡️ 提供平台政策及安全指引
- ⚙️ 解釋 YouTube 的運作方式
- 🧪 介紹測試新功能的相關資訊
- 📅 版權年份標示為 © 2026 Google LLC

---

### [克莱克博客](https://blog.klemek.fr/articles/2026-06-14/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [KleÏek's Blog](https://blog.klemek.fr/articles/2026-06-14/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

概述摘要：本文探讨了人工智能在医疗诊断中的应用，强调了其提高准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🩺 人工智能可辅助医生进行更精准的疾病诊断，减少人为错误。
- 📊 通过分析大量医疗数据，AI 能快速识别模式，提升诊断速度。
- 🔒 数据隐私问题需严格管理，确保患者信息不被滥用。
- ⚖️ 算法偏见可能导致诊断不公，需持续优化模型以消除偏差。
- 🤝 人机协作是关键，AI 应作为工具而非完全替代医疗专业人员。

---

### [Django 国际化 - 将您的应用翻译成多种语言！- YouTube](https://www.youtube.com/watch?v=PGMhsAcfPpI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Django Internationalization - translate your app to multiple languages! - YouTube](https://www.youtube.com/watch?v=PGMhsAcfPpI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本頁面概述了 YouTube 平台相關的各項資訊，包括版權、政策、聯絡方式及平台運作等基本說明。

- 📰 **新聞中心**：提供 YouTube 官方新聞與最新動態。
- ©️ **版權**：說明內容創作者的版權保護與相關規範。
- 📞 **聯絡我們**：提供用戶與平台聯繫的管道。
- 🎥 **創作者**：針對內容創作者提供的資源與支援。
- 📢 **刊登廣告**：說明在 YouTube 上投放廣告的選項。
- 👨‍💻 **開發人員**：提供 API 與開發工具相關資訊。
- 📜 **條款**：列出使用 YouTube 服務的條款與條件。
- 🔒 **私隱**：說明用戶個人資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋平台安全規範與內容審查政策。
- ⚙️ **YouTube 的運作方式**：解釋推薦系統、內容分發等運作機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能與實驗。
- 🏢 **© 2026 Google LLC**：版權歸屬與法律聲明。

---

### [Jupyter 企业网关 - 从笔记本到 Kubernetes 集群管理员 - elttam](https://www.elttam.com/blog/jupyter-enterprise-gateway?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Jupyter Enterprise Gateway - From Notebook to Kubernetes Cluster Admin - elttam](https://www.elttam.com/blog/jupyter-enterprise-gateway?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本报告揭示了 Jupyter Enterprise Gateway 的三个高危漏洞，允许无 Kubernetes 特权的笔记本用户通过 API 注入恶意值，最终完全控制底层 Kubernetes 集群。漏洞包括：通过空格绕过 UID/GID 限制以 root 权限运行 Pod、Jinja2 模板注入实现远程代码执行、以及 YAML 注入创建任意特权 Pod。攻击者可从运行数据科学任务升级为读取集群密钥、挂载主机文件系统、创建任意 Pod。报告提供了漏洞详情、利用演示及修复建议。

- 🚨 **CVE-2026-44180：UID/GID 绕过** - 通过给`KERNEL_UID`或`KERNEL_GID`添加尾随空格（如`"0 "`），绕过禁止 root 用户的检查，使 Pod 以 root 权限运行。
- 🔥 **CVE-2026-44181：Jinja2 SSTI 导致 RCE** - 在`KERNEL_POD_NAME`等变量中嵌入 Jinja2 模板表达式（如`{{7*7}}`），在 Enterprise Gateway 服务端执行任意 Python 代码，窃取其服务账户令牌。
- ⚙️ **CVE-2026-44182：YAML 注入创建任意资源** - 在`KERNEL_WORKING_DIR`等变量中注入换行和 YAML 语法，覆盖 Pod 的`securityContext`或创建新的特权 Pod、挂载主机文件系统。
- 💻 **攻击链**：笔记本用户通过 API 发送恶意环境变量 → Enterprise Gateway 以高权限服务账户执行 → 创建 root 权限 Pod、RCE 或注入 YAML → 挂载主机文件系统或创建特权 Pod → 完全控制集群。
- 🛡️ **修复建议**：升级至 v3.3.0；限制 Enterprise Gateway API 的网络访问和身份认证；收紧其 RBAC 权限；使用准入控制器（如 Kyverno）禁止 root 容器、特权容器和`hostPath`挂载；启用 Pod 安全标准（baseline/restricted）和用户命名空间。

---

### [插件案例研究：Pluggy - Eli Bendersky 的网站](https://eli.thegreenplace.net/2026/plugins-case-study-pluggy/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Plugins case study: Pluggy - Eli Bendersky's website](https://eli.thegreenplace.net/2026/plugins-case-study-pluggy/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

### 概述总结
Pluggy 是一个用于构建插件系统的 Python 库，最初为 pytest 开发，后独立成库。它通过钩子（hooks）机制实现宿主应用与插件的交互，支持自动发现和注册插件，并提供灵活的钩子调用方式。

- 📦 **核心概念**：Pluggy 基于钩子（hooks）机制，宿主通过 `HookspecMarker` 定义钩子规范，插件通过 `HookimplMarker` 实现钩子功能。
- 🔍 **插件发现**：支持通过 `load_setuptools_entrypoints` 自动发现通过 pip 安装的插件，也允许自定义发现方式。
- 📝 **钩子定义**：宿主使用 `@hookspec` 装饰器定义钩子接口，插件使用 `@hookimpl` 装饰器实现具体逻辑，钩子可返回函数或值。
- 🔄 **钩子调用**：通过 `plugin_manager.hook.<hook_name>()` 调用，默认按 LIFO 顺序执行，支持 `tryfirst`、`trylast` 等排序选项。
- 🛠️ **插件注册**：插件通过 `pyproject.toml` 中的 `[project.entry-points.<项目名>]` 注册，或通过 `register()` 方法手动添加。
- 🔗 **宿主 API 暴露**：插件可直接导入宿主模块，宿主通过钩子参数传递数据（如 `post`、`db`），实现 API 交互。
- ⚖️ **适用性评估**：Pluggy 提供签名验证、结果收集、钩子排序等高级功能，但需权衡依赖引入与项目复杂度，适合需要成熟插件系统的场景。

---

### [PyTorch 中的性能分析（第二部分）：从 nn.Linear 到融合 MLP](https://huggingface.co/blog/torch-mlp-fusion?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP](https://huggingface.co/blog/torch-mlp-fusion?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

## 概述总结
本文是 PyTorch 性能分析系列的第二部分，深入探讨了从`nn.Linear`到融合 MLP 的性能优化过程，展示了不同优化策略对 GPU 内核执行的影响。

- 🔬 **Linear 层分析**：`nn.Linear`本质上是矩阵乘法与偏置相加的组合，偏置通过“后记”（epilogue）机制融合进 GEMM 内核，无需单独的内核启动
- 🔄 **转置操作揭秘**：`aten::t`仅修改张量元数据（形状和步长），不复制数据或启动 GPU 内核，`torch.compile`可消除此 CPU 开销
- ⚡ **编译优化局限**：对于单个`nn.Linear`，`torch.compile`无法进一步融合，因为`addmm`已是最优；但在 MLP 中可融合 GeLU 和乘法为单个 Triton 内核
- 🧩 **MLP 性能分析**：GeGLU MLP 在 Eager 模式下运行 5 个 GPU 内核（3 个 GEMM + GeLU + 乘法），其中间张量需在 HBM 中完整读写
- 🏎️ **手调内核优势**：Liger 内核将 GeLU 和乘法融合为单个 Triton 内核，避免中间张量 HBM 往返，且使用硬件调优的启动参数，无需编译开销
- 📊 **内核命名解读**：cuBLAS 内核名称中的`tn`后缀表示布局描述（转置/非转置），不同形状选择不同分块策略（如 128x128 vs 128x256）
- 🚀 **kernels 库价值**：提供预编译、版本固定的内核包，避免本地编译问题，支持即插即用的`nn.Module`替换
- 💡 **关键习惯**：在查看性能分析前先预测结果，将不匹配视为最有价值的信息来源

---

### [PyData 伦敦 26 - YouTube](https://www.youtube.com/playlist?list=PLGVZCDnMOq0rFQykYJg7t441AEpN4SszE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [PyData London 26 - YouTube](https://www.youtube.com/playlist?list=PLGVZCDnMOq0rFQykYJg7t441AEpN4SszE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本頁面概述了 YouTube 平台的相關資訊，包括版權、政策、聯絡方式及開發者資源等。

- 📰 新聞中心：提供 YouTube 官方的最新消息與公告
- ©️ 版權：說明內容創作者的版權保護與相關規範
- 📞 聯絡我們：提供用戶與 YouTube 團隊聯繫的管道
- 🎬 創作者：針對內容創作者提供的資源與支援
- 📢 刊登廣告：介紹在 YouTube 上投放廣告的選項與資訊
- 💻 開發人員：提供 API 等技術資源給開發者使用
- 📜 條款：列出使用 YouTube 服務時需遵守的協議
- 🔒 私隱：說明用戶資料的收集與使用方式
- 🛡️ 政策及安全：涵蓋平台的安全措施與使用政策
- ⚙️ YouTube 的運作方式：解釋平台的功能與運作機制
- 🧪 測試新功能：介紹 YouTube 正在測試的新功能
- 📅 © 2026 Google LLC：顯示版權年份與所屬公司

---

### [GitHub - Ar9av/obsidian-wiki: 基于 Karpathy 的 LLM Wiki 模式，通过 Obsidian 维基为 AI 代理构建和维护数字大脑的框架](https://github.com/Ar9av/obsidian-wiki?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [GitHub - Ar9av/obsidian-wiki: Framework for AI agents to build and maintain a digital brain through Obsidian wiki using Karpathy's LLM Wiki pattern · GitHub](https://github.com/Ar9av/obsidian-wiki?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

一个名为 obsidian-wiki 的框架，让 AI 代理通过 Obsidian 构建和维护一个“数字大脑”。它基于 Karpathy 的 LLM Wiki 模式，将知识编译成交互式 Markdown 文件，并支持多种 AI 代理。

- 🧠 **核心理念**：将知识编译成交互式 Markdown 文件，而非重复询问 LLM 或运行 RAG，打造一个属于你自己的“第二大脑”。
- ⚡ **快速安装**：支持通过 `pip install obsidian-wiki`、`npx skills add` 或 `git clone` 三种方式安装，并自动配置到多种 AI 代理中。
- 🤖 **代理兼容性**：兼容 Claude Code、Cursor、Windsurf、Codex、Gemini CLI 等几乎所有主流 AI 编码代理，并自动发现技能。
- 📝 **四步工作流**：每次喂食大脑都经过“摄取 → 提取信息 → 合并 → 模式化”四个阶段，确保知识结构化且无重复。
- 🔍 **增量追踪**：通过 `.manifest.json` 追踪已摄取源文件，仅处理新增或变更内容，避免重复处理整个文档库。
- 🏗️ **项目化组织**：知识按项目或全局分类，使用 `[[wikilinks]]` 交叉引用，支持归档和重建。
- 🛠️ **丰富技能集**：提供 20+ 技能，包括设置、摄取、查询、审计、交叉链接、图谱导出、语义搜索等，覆盖知识管理全流程。
- 🌐 **多源摄取**：支持文档、PDF、聊天记录、会议记录、截图等，并可从 Claude、Codex、Hermes 等代理历史中定向摄取。
- 🔗 **图谱可视化**：支持 Obsidian 全局图谱视图，并可通过 `/graph-colorize` 技能按标签、文件夹或可见性着色。
- 📦 **跨项目使用**：通过全局技能 `wiki-update` 和 `wiki-query`，可在任何项目中读写大脑，实现跨代码库知识共享。
- 🗂️ **暂存目录 `_raw/`**：提供 `_raw/` 目录用于暂存快速笔记，下次摄取时自动处理并删除原始文件。
- 🔄 **GitHub 同步**：支持将知识库同步到私有 GitHub 仓库，获得版本历史、备份和跨设备同步功能。
- 🧩 **可扩展性**：鼓励贡献新技能，提供技能创建指南，并与 `kepano/obsidian-skills` 等第三方技能兼容。

---

### [GitHub - shuvonsec/claude-bug-bounty: 基于 AI 的漏洞赏金狩猎工具，支持终端操作 - 侦察、20 类漏洞、自主狩猎及报告生成，全部集成于 Claude Code 中。](https://github.com/shuvonsec/claude-bug-bounty?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [GitHub - shuvonsec/claude-bug-bounty: AI-powered bug bounty hunting from your terminal - recon, 20 vuln classes,   autonomous hunting, and report generation. All inside Claude Code. · GitHub](https://github.com/shuvonsec/claude-bug-bounty?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

這是一個名為 **BugHunter** 的 AI 驅動漏洞獎勵狩獵工具包，可從偵察到報告自動化完成，支援獨立 CLI 或 Claude Code 外掛使用。

- 🎯 **核心功能**：從偵察、漏洞測試、驗證到報告生成，一站式自動化漏洞獎勵狩獵流程
- 💰 **支援漏洞類型**：涵蓋 20 種 Web2 漏洞（如 IDOR、SSRF、XSS）和 10 種 Web3/智能合約漏洞，並列出典型獎金範圍
- 🤖 **AI 代理系統**：內建 9 個專業代理（偵察、驗證、報告撰寫、鏈式攻擊等），各司其職
- 🆓 **無需訂閱**：獨立模式完全免費，支援 Ollama（本地離線）、Groq、DeepSeek 等多種 AI 提供者
- ⚡ **快速上手**：提供三種安裝方式（獨立 CLI、Claude Code 外掛、自動安裝），幾分鐘內即可開始狩獵
- 🛡️ **嚴謹驗證**：7 問題閘門過濾弱發現，確保只提交高品質漏洞報告
- 📝 **自動報告**：60 秒內生成符合 HackerOne、Bugcrowd 等平台格式的提交報告
- 🔄 **跨會話記憶**：自動記錄發現模式和技術，讓後續狩獵更有效率
- 🧩 **豐富工具生態**：整合 35+ 掃描工具，支援子域名枚舉、漏洞掃描、智能合約審計等
- 📜 **嚴格規則**：7 條核心規則確保只在授權範圍內測試，避免被禁

---

### [GitHub - aws/agent-toolkit-for-aws: 官方 AWS 支持的 MCP 服务器、技能和插件，助力 AI 代理在 AWS 上构建 · GitHub](https://github.com/aws/agent-toolkit-for-aws?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [GitHub - aws/agent-toolkit-for-aws: Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS · GitHub](https://github.com/aws/agent-toolkit-for-aws?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

AWS Agent Toolkit 帮助 AI 编码代理在 AWS 上构建、部署和管理应用程序，提供工具、知识和防护措施。

- 🛠️ **核心功能**：为 AI 编码代理（如 Claude Code、Codex、Cursor、Kiro）提供与 AWS 服务交互的工具、知识和防护措施。
- 🚀 **快速启动**：支持通过插件市场或命令行安装插件，如 `aws-core`、`aws-agents`、`aws-data-analytics` 和 `aws-agents-for-devsecops`。
- 📦 **插件内容**：每个插件捆绑 AWS MCP 服务器配置和代理技能，覆盖核心 AWS 服务、AI 代理构建、数据分析及 DevSecOps 工作流。
- 🧠 **技能系统**：提供按需加载的代理技能包，包含指令和参考材料，帮助代理完成特定 AWS 任务。
- 🔒 **安全与监控**：支持 IAM 条件键区分代理和人类操作、CloudWatch 指标、CloudTrail 审计日志，以及沙盒脚本执行。
- 📚 **文档与规则**：包含项目级配置文件（如 rules/），指导代理有效使用 AWS，包括 MCP 服务器、技能发现和文档搜索。
- 🔄 **与 AWS Labs 的关系**：Agent Toolkit 是 AWS Labs 中 MCP 服务器、技能和插件的继任者，提供更强大的监控、审计和评估功能。

---

### [GitHub - hexo-ai/sia: SIA 是一个自我改进的 AI 框架，用于自主提升任何 AI 系统（模型/智能体）在基准任务上的性能。](https://github.com/hexo-ai/sia?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [GitHub - hexo-ai/sia: SIA is a Self Improving AI framework to autonomously improve the performance of any AI system (Model / Agent) on a benchmark task. · GitHub](https://github.com/hexo-ai/sia?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

SIA（自我改进 AI）是一个开源框架，能让 AI 系统在基准任务上自主提升性能，在多项测试中取得显著成果。

- 🧠 **核心架构**：由元代理、目标代理和反馈代理协同工作，形成自我改进循环，自动优化任务表现。
- 📊 **卓越基准成绩**：在 LawBench 上准确率达 70.1%（提升 56.6%），GPU 内核运行时减少 91.9%，scRNA 去噪提升 502%，MLE-Bench Hard 排名第一。
- 🚀 **快速本地运行**：支持四种内置任务（gpqa、lawbench 等），通过简单 CLI 命令即可启动自我改进循环。
- 🔧 **灵活配置**：支持 Claude 和 OpenHands 两种代理实现，可自定义模型、提供商和配置文件，无需修改代码。
- 📈 **可视化仪表盘**：内置 Web 界面实时显示各代改进过程，包括代码、评分、执行轨迹等。
- 🎯 **自定义任务**：支持用户创建任务目录或直接导入 MLE-Bench 竞赛，自动评估并反馈结果。
- 📝 **开源贡献**：MIT 许可证，提供完整文档、贡献指南和安全策略，便于社区参与。

---

### [GitHub - calesthio/OpenMontage: 全球首个开源、智能体驱动的视频制作系统。12 条流水线，52 种工具，500 多项智能体技能。将你的 AI 编程助手转变为完整的视频制作工作室。](https://github.com/calesthio/OpenMontage?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [GitHub - calesthio/OpenMontage: World's first open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills. Turn your AI coding assistant into a full video production studio. · GitHub](https://github.com/calesthio/OpenMontage?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

OpenMontage 是首个开源、智能体驱动的视频制作系统，可将 AI 编程助手转变为全功能视频制作工作室。

- 🎬 **核心功能**：通过自然语言描述需求，AI 智能体自动完成研究、脚本、素材生成、编辑和最终合成，支持真实视频片段（非仅图片动画）。
- 🛠️ **丰富资源**：包含 12 条制作管线、52 个制作工具、500+ 智能体技能，覆盖视频生成、图像创建、语音合成、音乐、字幕等全流程。
- 🆓 **免费使用**：无需付费 API 密钥即可使用 Piper TTS 配音、Archive.org 等开放档案素材、Remotion 合成等，支持本地 GPU 免费视频生成。
- 🤖 **智能体驱动**：AI 编程助手（如 Claude Code、Cursor）作为编排器，读取 YAML 管线清单和 Markdown 技能文件，调用 Python 工具，并执行自我审查。
- ✅ **质量保障**：内置预合成验证、渲染后自检、幻灯片风险评分、供应商评分选择、决策审计追踪和预算控制，确保输出质量。
- 🔄 **无供应商锁定**：供应商选择器根据 7 个维度自动评分，支持自由切换云端和本地开源替代方案。
- 🌐 **参考视频创作**：可粘贴 YouTube、Reel 等参考视频，智能体分析后生成差异化制作方案，包括保留元素、更改内容和成本估算。
- 📚 **知识架构**：三层知识体系（工具/管线、技能、外部技术知识包），让智能体像专家一样使用每个工具。
- 🎨 **风格与输出**：内置风格剧本（如简洁专业、扁平动图）和平台输出配置（YouTube、Instagram、TikTok 等），确保视觉一致性。
- 🤝 **社区与扩展**：支持通过 GitHub Discussions 分享作品和想法，可轻松添加新工具或管线，遵循 AGPL-3.0 开源许可。

---

### [GitHub - kjgpta/tracesage · GitHub](https://github.com/kjgpta/tracesage?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [GitHub - kjgpta/tracesage · GitHub](https://github.com/kjgpta/tracesage?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

tracesage 是一个为 LangChain 和 LangGraph 多智能体系统提供生产级可观测性的工具，只需两行代码即可在浏览器中实时查看执行追踪。

- 🚀 **零基础设施**：无需 Docker、Postgres 或外部服务，只需 `pip install` 即可运行。
- 🔌 **两行集成**：只需在现有的 `ainvoke` 中添加一个回调，即可捕获所有 LangChain 回调流。
- 🛡️ **生产级安全**：处理器永不抛出异常，追踪器不会导致管道崩溃，并支持 Bearer 令牌认证和路径遍历防护。
- 🎨 **交互式图形界面**：自定义 SVG 图形，自动布局，支持悬停、点击和重放任意运行。
- 🔗 **MCP 感知**：工具按来源（MCP 服务器 vs 本地硬编码）分组显示，便于追踪工具来源。
- 📡 **OpenTelemetry 导出**：可将追踪作为 OTel 跨度导出到 Grafana Tempo、Jaeger、Datadog 等后端。
- 💾 **可插拔存储**：默认使用 SQLite，未来计划支持 Postgres 和远程收集器。
- 🖥️ **丰富的 CLI 工具**：包括 `serve`、`export`、`import`、`stats`、`diff` 和 `watch` 等子命令。
- ⚡ **高性能**：在 Linux 上可处理 800–1200 事件/秒，p99 写入延迟为 80–150 毫秒。
- 🧪 **测试支持**：提供自动注册的 pytest 夹具 `tracesage_capture`，用于断言工具调用和错误。
- 📜 **MIT 许可证**：永久免费使用。

---

### [scikit-learn 发布 1.9 版本：改进的数值计算与全新核心功能 - scikit-learn 博客](https://blog.scikit-learn.org/updates/release-1-9/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [scikit-learn release 1.9: better numerics, new core functionality - scikit-learn Blog](https://blog.scikit-learn.org/updates/release-1-9/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

scikit-learn 1.9 版本发布，带来了更优的数值计算、新的核心功能以及多项改进，使现有估计器更快、更稳定，并增加了对缺失值、GPU 的支持。

- 📊 **更丰富的 HTML 显示**：笔记本中的估计器视图得到增强，可显示拟合后的属性，ColumnTransformer 也改进了特征组合的展示。
- 🔄 **新的回调机制**：引入了实验性的回调功能，支持进度跟踪、早期停止等，已在逻辑回归、Pipeline 等中实现，未来将扩展到更多估计器。
- 🧮 **改进的统计与数值计算**：树模型新增对缺失值和单调约束的支持，线性模型支持 float32 和稀疏数据，其他模型如 MiniBatch KMeans 增加了样本权重支持。
- ⚡ **更快更稳定**：RidgeCV 和 RidgeClassifierCV 更稳定快速，新增间隙安全特征筛选，Spectral Embedding 速度提升。
- 🗂️ **生态兼容性更新**：现在可返回稀疏数组而非稀疏矩阵，以适应 SciPy 的变化。
- 🚀 **GPU 支持扩展**：逻辑回归、泊松回归、更多指标和 Nystroem 核近似获得了 GPU 后端支持，但用户体验仍在改进中。

---

### [从任何地方获取数据：API 实用入门，2026 年 6 月 23 日星期二下午 5:00 | Meetup](https://www.meetup.com/python-spokane/events/315107264/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Getting Data from Anywhere: A Practical Introduction to APIs, Tue, Jun 23, 2026, 5:00 PM   | Meetup](https://www.meetup.com/python-spokane/events/315107264/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本活动是由 Spokane Python 用户组主办的一场关于 API 的实用入门讲座，旨在讲解 API 如何让网站、应用和系统共享数据，并提供实际代码示例。

- 📅 活动时间：2023 年 6 月 23 日（周二）下午 5:00 至 6:00（太平洋夏令时）
- 📍 地点：Spokane 公共图书馆（906 West Main Avenue, Spokane, WA），中央会议室 B 和休息区
- 🎤 主持人：David 和 Eli B.，由 IntelliTect 和 Python 软件基金会赞助
- 🔍 核心内容：解释 API 的基本概念、工作原理、请求与响应、认证方式及 JSON 数据格式
- 💻 实践环节：提供获取简单 API 数据的代码示例，适合初学者或想了解现代应用通信的人
- 📊 未来计划：若反响良好，将举办更深入的数据工程主题讲座，涵盖数据架构和下游平台集成
- 🏢 赞助方：IntelliTect 提供场地和零食，Python 软件基金会赞助 Meetup 订阅

---

### [用合适的数据喂养 AI 智能体，2026 年 6 月 25 日（周四）下午 6:00 | 聚会](https://www.meetup.com/pyladiesams/events/315210102/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Feed an AI-agentic beast with proper data, Thu, Jun 25, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pyladiesams/events/315210102/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本次活动是由 PyLadies Amsterdam 主办的混合型工作坊，主题为“用优质数据喂养 AI 智能体”。

- 📅 活动时间：2025 年 6 月 25 日（周四）18:00–21:00（CEST），线上线下同步进行
- 🧠 工作坊核心：学习如何准备数据，让 AI 智能体不“盲目运行”，涵盖表格数据清洗、文档智能分块及审查 AI 代码的习惯
- 🗓️ 日程安排：18:00 开门，18:30 工作坊开始，20:00 结束并宣布事项，20:10 社交环节，21:00 活动结束
- 👩‍🏫 主讲人：Jessica Eggen，数据分析工程师，专长于大规模数据整理和商业分析视角的 AI 应用
- 🔗 资源链接：GitHub 仓库（https://github.com/pyladiesams/feed-AI-agentic-beast-proper-data-jun2026）及 YouTube 直播
- 📧 联系与社区：可通过 amsterdam@pyladies.com 联系，或加入 PyLadies Slack 工作区（#city-amsterdam 频道）
- 🏷️ 相关主题：阿姆斯特丹活动、人工智能、开源 Python、Python 编程、计算机编程、女性科技

---

### [PyLadies 旧金山分会活动 @ Vonage，2026 年 6 月 25 日（周四）下午 6:30 | Meetup](https://www.meetup.com/pyladiessf/events/315204101/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [PyLadies San Francisco at Vonage, Thu, Jun 25, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pyladiessf/events/315204101/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

概述摘要  
- 🍕 活动由 Vonage 赞助，提供披萨、Python 编程和社交机会  
- 🎤 议程包括多个技术演讲：Pydantic 与 Rust 集成、AI 代理安全、Python Slack/Google API 应用、30 天 AI 求职路线  
- 🕐 时间安排：6:30 PM 开始社交与餐饮，7:25 PM 欢迎致辞，7:30 PM 起依次进行演讲，9:30 PM 结束  
- 📍 地点：旧金山 Dogpatch Hub，需通过 Luma RSVP  
- 👩‍💻 面向 Python 开发者、技术专业人士及女性科技从业者，需遵守行为准则

---

### [Python 地理数据与符号差异化分析 | 2026 年 6 月 23 日周二下午 6:30 Meetup](https://www.meetup.com/pydata-milano/events/315213092/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Geographical Data & Symbolic Differentiation with Python, Tue, Jun 23, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-milano/events/315213092/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本次活动由 PyData Milano 主办，于 2026 年 6 月 23 日在米兰 FlixBus 总部举行，聚焦地理数据处理与 SymPy 符号微分两大主题。

- 📍 **活动信息**：时间 2026 年 6 月 23 日 18:30–21:00，地点米兰 Corso Como 11 的 FlixBus 总部，名额有限需提前确认 RSVP。
- 🗓️ **日程安排**：18:30 开门签到，19:00 第一场演讲，19:45 第二场演讲，20:30 社交晚餐。
- 🗺️ **第一场演讲**：Jacopo Farina 讲解如何用 Python 处理 OpenStreetMap、公共交通等地理数据，计算城市距离、查找地址及分析共享单车使用情况。
- 🧮 **第二场演讲**：Francesco Bonazzi 介绍 SymPy 中矩阵与 N 维数组的符号微分，支持显式和隐式两种算法，可生成精确梯度表达式。
- 👤 **演讲者背景**：Jacopo Farina 是 FlixBus 数据工程师，Francesco Bonazzi 是 SymPy 核心维护者及物理博士，现从事生成式 AI 研究。

---

### [PyData 赫尔辛基在 UpCloud 举办，2026 年 6 月 24 日星期三下午 4:30 | Meetup](https://www.meetup.com/pydatahelsinki/events/314755648/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [PyData Helsinki at UpCloud, Wed, Jun 24, 2026, 4:30 PM   | Meetup](https://www.meetup.com/pydatahelsinki/events/314755648/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

PyData Helsinki 将于 6 月 24 日在 UpCloud 办公室举办线下活动，包含三场数据科学主题演讲、交流环节和酒吧社交。

- 📅 活动时间：6 月 24 日下午 4:30 至 7:30（芬兰时间），之后可前往附近酒吧继续交流
- 🏢 地点：UpCloud 办公室（Aleksanterinkatu 15b, 7 楼，赫尔辛基）
- 🎤 演讲 1：Seija Sirkiä 探讨 NPS（净推荐值）数据的正确使用方法，包括消除文化/国家等子群体影响的模型
- 🧠 演讲 2：Touko Väänänen 介绍如何在不确定偏好下选择具有多重影响的项目，评估稳健方案
- 🔄 演讲 3：Alexander Kevin Gilbert 分享从物理/CERN 大数据分析转型数据工程的经验，揭示工具差异下的共通点
- 🍕 活动安排：17:00 开场致辞，17:10-19:30 演讲与问答，中间安排休息、餐饮和 PyData 知识问答
- 🤝 主办方：PyData Helsinki（由 Jouni S.等超级组织者主持），赞助商包括 NumFOCUS
- 📊 相关主题：数据分析、数据科学、Python，适合赫尔辛基地区的从业者和爱好者

---

### [PyData 三城 #44，2026 年 6 月 24 日（周三）下午 6:00 | 聚会](https://www.meetup.com/pydata-trojmiasto/events/315186524/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [PyData Trójmiasto #44, Wed, Jun 24, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-trojmiasto/events/315186524/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

PyData Trójmiasto #44 是一场于 6 月 24 日在格丁尼亚举行的线下技术聚会，聚焦计算机视觉和 AI 编程助手的经济学。活动包含两场演讲：一个是从标注到部署的物体检测流程（使用 Geti、YOLO26 和 OpenVINO），另一个是 AI 编码助手的成本控制策略。现场还有自由交流环节。

- 📅 活动时间：6 月 24 日 18:00-20:00，地点在格丁尼亚Łużycka 8b 的 Tensor Z 大楼，需提前注册并携带身份证入场。
- 🅿️ 免费停车：建筑沿街提供免费停车位。
- 🎤 第一场演讲：Adrian Boguszewski 讲解如何用 Geti 快速标注、YOLO26 训练模型，再通过 OpenVINO 优化部署到 Intel 处理器，实现工业级物体检测（以榛子为例）。
- 💰 第二场演讲：Marcin Duszyński 分析 AI 编码助手从月费转向按 token 计费的新模式，强调通过精简上下文、选择合适模型来控制成本，避免账单意外。
- 🤝 活动最后安排社交环节，方便参会者交流。
- 🏢 主办方为 PyData Trójmiasto，由 NumFOCUS 赞助，主题涵盖 AI、深度学习、大数据和 Python。

---

### [与数据对话：面向分析与金融的生产级 AI 代理，2026 年 6 月 25 日（周四）下午 6:00 | Meetup](https://www.meetup.com/pydata-nl/events/315200707/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Talk to Your Data: Production-Grade AI Agents for Analytics & Finance, Thu, Jun 25, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-nl/events/315200707/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

本次 PyData Amsterdam 聚会聚焦于构建生产级 AI 代理，用于数据分析和金融领域，活动将于 2026 年 6 月 25 日在阿姆斯特丹的 Cinema The Pulse 举行。

- 🎬 活动地点：Cinema The Pulse 影院，提供大屏幕展示架构图，营造沉浸式体验
- 🍕 活动安排：18:00 开始提供餐饮，随后有两场技术演讲和社交环节
- 🤖 演讲 1：Alex Litvinov 讲解如何构建可信的自助分析代理，基于 Claude Code 实现自然语言查询
- 💰 演讲 2：Niels Neerhoff 分享金融数据中可靠 AI 代理的工程挑战，如多租户隔离和提示注入防御
- 🔧 技术重点：开放架构设计、智能路由、安全隔离和可靠性策略，从原型到生产的过渡模式
- 🏢 赞助商：Adyen、The NextGen、Heineken 和 Rabobank 提供场地和餐饮支持
- 📍 交通便利：距离阿姆斯特丹 Zuid 火车站仅 5 分钟步行路程

---

### [机器人辅助外骨骼在脊髓损伤患者中的应用，2026 年 6 月 25 日（周四）下午 6:30 | Meetup](https://www.meetup.com/pydata-pittsburgh/events/315068868/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [Robot-assisted Exoskeletons for Individuals with Spinal Cord Injury, Thu, Jun 25, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-pittsburgh/events/315068868/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

活动概述：PyData Pittsburgh 将于 6 月 25 日举办关于机器人辅助外骨骼的讲座，由 CMU 博士生 Jonathan Shulgach 主讲，探讨利用 Python 和机器学习技术开发可穿戴肌肉传感系统及 3D 打印外骨骼，以帮助脊髓损伤患者恢复手部功能。

- 🗓️ **活动时间**：6 月 25 日（周四）下午 6:30-8:00，地点在卡内基梅隆大学贝克大厅。
- 🎤 **主讲人**：Jonathan Shulgach，CMU 机械工程博士生，专攻可穿戴机器人、肌电传感与人机交互。
- 🤖 **核心内容**：介绍高密度柔性 EMG 传感器阵列的设计挑战，及如何用 Python 实时处理肌肉信号。
- 🖨️ **开源外骨骼**：展示 3D 打印手部外骨骼，通过残余肌肉活动预测用户意图，实现功能性抓握。
- 🧠 **技术亮点**：结合机器学习解码肌电信号，控制可配置手势，推动辅助技术实用化。
- 🔬 **研究背景**：来自 CMU 神经机械电子实验室，聚焦可穿戴传感、实时数据管道与机器人控制集成。
- 💡 **相关主题**：涉及神经技术、AI/机器学习、机器人学、Python 及开源技术。

---

### [PyDataMCR 六月活动，2026 年 6 月 25 日（周四）下午 6:00 | Meetup](https://www.meetup.com/pydata-manchester/events/315153158/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

**原文标题**: [PyDataMCR June , Thu, Jun 25, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-manchester/events/315153158/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-750-june-18-2026)

PyDataMCR 六月活动将于 6 月 25 日在曼彻斯特 Autotrader 举办，包含两场技术演讲，聚焦 AI 与数据科学应用，会后有社交环节。

- 🗓️ **活动时间地点**：6 月 25 日周四 18:00-20:00，曼彻斯特 Autotrader Circle Square，限 50 人
- 🤖 **演讲一：LLM 中的共情数据**：Lucy Stafford-Hughes 探讨通过锚定和身份容器稳定 LLM 交互模式，减少幻觉、提升准确性，并涉及 Anthropic 情感向量研究
- 📊 **演讲二：理解营销效果**：Josh Hayes 讲解如何通过归因模型衡量广告支出影响，强调数据科学家需帮助利益相关者明确问题定义
- 🍕 **赞助与后勤**：由 NumFOCUS、Autotrader、Krakenflex 和 Horsefly Analytics 赞助，提供餐饮
- ♿ **无障碍设施**：场地和卫生间均无障碍，活动遵循 NumFOCUS 行为准则

---

