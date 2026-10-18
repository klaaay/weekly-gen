### [Python 3.15 的最佳新功能 - Python Morsels](https://www.pythonmorsels.com/python315/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Python 3.15's best new features - Python Morsels](https://www.pythonmorsels.com/python315/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

Python 3.15 已正式发布，本文介绍了作者最喜欢的若干新特性，包括跨平台 UTF-8 默认编码、内置 sentinel 哨兵值、推导式解包、显式惰性导入、新的 profiling 采样分析器、更友好的错误提示与彩色输出，以及 frozendict、pprint、re 等改进；同时还提到还有更多更新未展开，如可选 JIT、math.integer 等。

- 🌍 UTF-8 成为所有操作系统的默认文件编码，Windows 不再默认使用 CP-1252，跨平台读写文件更一致；兼容旧版 Python 时仍建议显式写 `encoding="utf-8"`。
- 🏷️ 新增内置 `sentinel` 类型，可创建有名称、字符串表示更友好的哨兵值，例如 `MISSING = sentinel("MISSING")`。
- 📦 推导式现支持 `*` 和 `**` 解包，可用于列表、集合、生成器表达式和字典推导式，简化展平嵌套结构。
- ⏳ 新增 `lazy import` 与 `lazy from ... import`，模块首次使用时才真正加载，主要改善命令行程序启动时间，不太适合长期运行进程。
- 📊 新增 `profiling` 包：`profiling.tracing` 是原 `cProfile` 的新名称；`profiling.sampling` 是低开销采样分析器，支持 `attach` 到运行中进程、火焰图和实时模式。
- 💬 错误信息进一步改进，例如对列表调用不存在的 `push` 方法时，会提示 `Did you mean '.append'?`。
- 🎨 彩色输出继续扩展，Python 3.15 为 `--help` 等此前未着色的输出增加颜色。
- 🧊 新增 `frozendict` 类型，即不可变且可哈希的字典。
- 🖨️ `pprint` 新增 `expand=True`，让美化输出更易读、更接近多行展开格式。
- 🔍 `re` 模块新增 `re.prefixmatch`，功能类似 `re.match`，但名称更清晰。
- 🚀 还有未展开的更新，如可选启用 JIT、`math.integer`、`.pth` 与 `.start` 文件等；建议安装 Python 3.15 并查看官方 “What's New in Python 3.15”。

---

### [](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [How I Found a $90,000 Remote Code Execution Vulnerability in Google | Simon Koeck](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

Google DevSite 曝出严重 RCE 漏洞：Flask 会话 cookie 内含 OAuth client_id/secret，且该 secret 被复用为 Flask 签名密钥，导致可伪造会话并借 pickle 反序列化实现未认证远程代码执行；作者最终获 $90,000 奖励。
- 🍪 入口：developers.google.com 的 /oauth2authorize 会设置 Flask session cookie，约 1,200 字节，包含压缩与签名的 pickle 数据。
- 🔑 泄露：解码 cookie 可得到明文 OAuth client_id 与 client_secret；该 secret 同时也是 Flask SECRET_KEY。
- 🧩 伪造：使用泄露 secret 可离线重算 itsdangerous 签名，任意篡改 session 都能被服务端接受。
- 🧨 RCE：回调读取 google_oauth2_flow_<csrf> 并对字节执行 pickle.loads，伪造 session 后触发未认证反序列化执行。
- ⏱️ 验证：作者用 pickle 调用 time.sleep(N)，响应延迟与 N 一致，例如 3→3.193 秒、5→5.194 秒、8→8.283 秒，证明代码执行。
- 🌐 影响：同一密钥可用于 firebase.google.com、developer.android.com、source.android.com、docs.partner.android.com 等 DevSite 主机。
- 🛠️ 修复：轮换 OAuth secrets、每个部署使用独立高熵 Flask SECRET_KEY、OAuth flow 仅存服务端、弃用 pickle。
- 📅 时间线：2026-08-06 报告；08-07 分类并接受；约 24 小时内热修复；08-27 决定奖励 $90,000；10-07 状态更新为已修复。
- 💰 奖励：归类 Normal Google Applications (T2), S0 RCE，$75,000 基础奖励 × 1.2 报告质量系数 = $90,000。

---

### [为什么.parquet主导了现代数据工程 - YouTube](https://www.youtube.com/watch?v=6Qkzfwk0W58&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [why .parquet dominates modern data engineering - YouTube](https://www.youtube.com/watch?v=6Qkzfwk0W58&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

这是 YouTube 页面底部的导航与法律信息列表，主要汇集平台介绍、联系渠道、创作者/广告/开发者入口、政策条款、功能说明及版权声明。

- ℹ️ “关于”和“新闻”用于了解 YouTube 及媒体报道。
- 📞 “联系我们”提供联系 YouTube 的方式。
- 🎥 “创作者”和“广告”分别面向内容创作者与广告主。
- 👨‍💻 “开发者”提供面向开发者的资源。
- 📜 “条款”“隐私”“政策与安全”列明法律、隐私与安全规范。
- ⚙️ “YouTube 的工作原理”介绍平台运作机制。
- 🧪 “测试新功能”可体验试验性功能。
- ©️ 版权信息显示 © 2026 Google LLC。

---

### [](https://blog.jetbrains.com/go/2026/10/13/python-vs-go/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Python vs Go: A Practical Comparison for Developers - The JetBrains Blog](https://blog.jetbrains.com/go/2026/10/13/python-vs-go/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

本文基于 JetBrains《开发者生态系统 2026》调查（28,945 份回复；Go 1,836 人、Python 11,298 人，其中 619 人两者兼用）及开发者访谈，比较 Python 与 Go 在语言设计、性能、工具链、开发者画像和迁移经验上的差异。核心结论：两者不是谁更好，而是谁更适合；Go 更适合高性能、并发、云原生基础设施，Python 更适合 AI/ML、数据科学和快速迭代；实际迁移通常是混用而非替代。

- 📊 数据来源：主要来自 JetBrains 2026 调查与 7 位从 Python 转向 Go 的开发者访谈，差异多为保守估计。
- 🧭 核心哲学：Python 重视表达力和快速迭代，允许多种写法；Go 重视显式、标准化和可维护性，追求所有 Go 代码风格一致。
- 🎓 学习曲线：Python 对新手极友好，常作为第一语言；Go 很少作为第一语言，更适合已有经验的开发者。
- ✍️ 语法与可读性：Python 接近自然语言、类型可选、PEP 8 可选；Go 静态类型、`gofmt` 统一格式、显式错误处理更啰嗦。
- 🧱 类型系统：Python 运行时动态类型、鸭子类型；Go 编译期静态类型，重构更安全但代码更冗长。
- 🧩 对象模型：Python 有类、继承、多态；Go 无类无继承，用 struct + 隐式接口，接口通常很小，遵循“接受接口，返回结构体”。
- ⚡ 性能：Go 编译为原生二进制，冷启动、延迟、吞吐更好；Python 是字节码 + 解释器，但 NumPy/PyTorch 等把重计算交给原生代码。
- 🧠 内存管理：Go 用并发追踪 GC，可用 `GOGC`、`GOMEMLIMIT` 调优；Python 用引用计数 + 循环 GC，更可预测但调优空间小。
- 🔀 并发：Go 的 goroutine、channel、select 让并发更简单，常被称为“默认异步”；Python 有 asyncio、threading、multiprocessing，但受 GIL 限制，PEP 703 正推进自由线程。
- 📦 生态与框架：Go 标准库和工具链自足，`html/template` 31%、`testing` 常用、`net/http` 46% 对 Gin 48%；Python PyPI 庞大，FastAPI 50%、Django 31%、Flask 30%，NumPy 69%、pandas 68%、PyTorch 49%。
- 🛠️ IDE：Go 开发者用 GoLand 49%、VS Code 48%；Python 开发者用 VS Code 41%、PyCharm 30%；GoLand 与 PyCharm 同平台，设置可同步。
- 👥 开发者画像：Go 开发者更资深，60% 为高级、72% 全职、20% 有 16 年以上经验；Python 中 42% 高级、51% 全职、20% 仅 1–2 年经验。
- 💰 薪资：Go 开发者更多进入高薪段，9% 年收入超 18 万美元，Python 为 6%；但全职对比后差异不显著，高薪更多来自岗位和资历。
- 🏗️ 构建内容：Go 更偏 API/服务 69% 对 41%、集成 API 63% 对 47%、应用逻辑 51% 对 37%；Python 更偏数据处理 38% 对 30%、AI/ML 36% 对 20%、数据科学 32% 对 15%。
- ☁️ 运行平台：Go 主攻服务器/基础设施/云 74% 对 57%；Python 更多用于桌面 66% 对 47%；AI 集成几乎持平：Go 46% 对 Python 44%。
- 🚀 DevOps：Go 参与度 45% 对 Python 31%；Kubernetes 使用 58% 对 39%；Terraform 领先；Go 更常用 GitOps。
- 💻 操作系统：Go 开发者常用 macOS 70%、Linux 57%、Windows 44%；Python 开发者首选 Windows 66%，macOS 54%、Linux 52%。
- 🤖 AI 辅助开发：Go 更常用于多文件编辑 60% 对 52%、智能体开发 51% 对 41%、生成提交信息 51% 对 36%、生成测试 47% 对 34%、代码评审 39% 对 34%；Python 更常用于学习编码 38% 对 31%。
- 🧰 AI 工具偏好：Go 偏 Claude Code、OpenAI Codex、Cursor、OpenCode；Python 偏 ChatGPT、Google Antigravity、Microsoft 365 Copilot。
- ⚖️ 性别差距：Go 女性仅 1.8%，Python 为 5.8%；Go 作为第二语言继承并放大了行业管道中的性别差距。
- 🔁 迁移方向：Python 是 Go 开发者最常见第二语言（35%）；10% Python 开发者计划学 Go，约为 Go 开发者计划学 Python（2%）的 5.5 倍。
- 🧭 迁移原因：性能/冷启动/成本、并发模型、类型安全、贴近 Kubernetes 和云原生工具链。
- ✅ 迁移收获：格式与 lint 可预测、开箱工具、接近 Python 的简洁；⚠️ 代价：显式错误处理、啰嗦、对象模型不利测试/mock、库缺口。
- 🔄 真实结果：几乎没人完全弃用 Python；常见是 Go 做服务和基础设施，Python 做 AI、数据和科学计算，形成多语言代码库。
- 🎯 选择建议：Go 适合性能/并发/长生命周期团队服务/重度使用 K8s；Python 适合 ML/数据科学/数值计算、平台只支持 Python、迭代速度优先、依赖独有库。
- 🧾 FAQ 要点：Go 不能完全替代 Python；Go 适合数据管道搬运但不适合分析端；Python 开发者学 Go 语法需数天到数周，但系统概念和工具链更久；Go 不适合训练模型但适合服务模型；两者常在同一项目中混用。

---

### [获取失败](https://lemire.me/blog/2026/10/12/parsing-json-at-tens-of-gigabytes-per-second-in-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/10/12/parsing-json-at-tens-of-gigabytes-per-second-in-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

无法总结：获取内容失败，状态码 202。

---

### [](https://codewithstein.com/building-a-small-django-app-with-help-from-ai/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Building a small Django app with help from AI | Code With Stein](https://codewithstein.com/building-a-small-django-app-with-help-from-ai/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

本文以构建一个小型 Django“点子板”为例，说明 AI 可以作为编程辅助工具：用于生成重复代码、解释错误、审查代码和编写测试，但开发者仍需理解架构、数据建模与生产代码，不能盲目粘贴 AI 生成的代码。

- 🧰 AI 的定位：不是让 AI 包办整个应用，而是把它当作提速、答疑和查漏的辅助工具。
- 🎯 项目目标：实现查看点子、提交点子、投票三个核心功能，并避免基础版未完成就堆功能。
- ⚙️ 项目搭建：用 venv、安装 Django、startproject/startapp 等基础命令；作者通常不借助 AI，因为自己更熟。
- 🗃️ 模型设计：AI 可快速生成 Idea 模型（标题、描述、票数、创建时间），但要先阅读，防止 AI 过度设计。
- 🛠️ 迁移与 Admin：运行迁移、注册模型、创建超级用户，并先手动添加数据验证模型。
- 📄 列表与表单：用视图、URL、模板展示点子，用 ModelForm 提交新点子；简单 HTML 可让 AI 生成，但要限制它引入前端框架。
- 🐞 调试错误：把错误交给 AI 时，要求解释原因并给出最小修复，而不是让 AI 重写整个视图。
- 👍 投票功能：添加投票视图和按钮，但直接 `votes += 1` 会带来重复投票和并发问题。
- 🔍 代码审查：让 AI 审查已有代码，寻找 bug、安全、并发和扩展性问题，而不是直接重写。
- 🔄 并发修复：使用 `F("votes") + 1` 让数据库原子递增，避免两个请求同时读取导致票数丢失。
- 🧱 防重复投票：可通过登录、会话或独立 Vote 模型加唯一约束实现；复杂度应按实际需求增加。
- 🧪 测试：AI 适合生成 Django TestCase 初稿，但仍需阅读、运行并确认测试真的有效。
- 🔐 安全：不要把 `SECRET_KEY`、数据库密码、API 密钥、客户数据等敏感信息粘贴给 AI。
- 🧠 最大误区：不要接受自己不理解的 AI 代码，否则未来调试和维护会非常痛苦。
- 🎛️ 提示技巧：给 AI 小而具体的问题，效果优于“帮我做一个 SaaS”；也可让它解释代码和数据库查询。
- ⚠️ AI 会出错：可能使用旧版写法、虚构方法或给出坏实践；关键处仍要查 Django 文档。
- 🚀 上线前审查：让 AI 检查安全、权限、数据库、性能和开发/生产差异，但最终由自己判断采纳。
- 🧰 总结：AI 不会取代 Django 开发，而是加速部分工作；自己设计架构、建模并理解生产代码，把 AI 当作工具箱中的另一件工具。

---

### [🐥 用 Python 构建电梯](https://www.yellowduck.be/posts/building-a-lift-scheduling-algorithm-in-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [🐥 Building a lift scheduling algorithm in Python | 🐥 YellowDuck.be](https://www.yellowduck.be/posts/building-a-lift-scheduling-algorithm-in-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

overview summary
本文用 Python 示例解释电梯调度：从单梯 LOOK 算法，到多梯评分分配、成本估算、目的地调度、调度器与控制器分离、状态机建模，最终指出其本质是变化约束下的资源分配与多目标优化。

- 🛗 电梯看似简单，内部却是调度问题：多梯多乘客时，要决定哪部电梯处理哪个请求，并减少等待、旅行和不必要停靠。
- 🧱 单梯用 dataclass 记录当前楼层、方向和目标楼层集合，方向可为 up、down 或 None。
- 🔁 LOOK 算法：沿当前方向继续，访问该方向最近目标；该方向无目标就反向；完全没有目标则空闲。
- ✅ 服务目标后必须从 targets 中移除，否则路线会错误；正确示例是 5 → 6 → 8 → 10 → 4 → 2。
- 🎯 LOOK 不选全局最近楼层，而是方向优先；例如 5 楼、目标 4/6/10、向上时先到 6，再到 10，最后反向到 4。
- 🧑‍🤝‍🧑 厅门请求带方向，例如“5 楼想上行”；上行电梯通常不必为下行乘客停靠，应优先匹配当前方向。
- 🏢 多梯可用评分分配：分数 = 距离 + 方向惩罚；同向 0、空闲 2、反向 10，选最低分电梯。
- 💰 更复杂的控制器会估算“接受请求的额外成本”：等待时间、旅行时间、额外停靠、方向改变，权重可配置。
- 🧭 目的地调度让乘客直接输入目标楼层，控制器可提前分组相似目的地，优化整条路线，而不是独立处理每个请求。
- 🧩 架构上应分离 Dispatcher 与 LiftController：前者决定哪部电梯接单，后者决定下一层去哪。
- 🚦 真实控制器可建模为状态机：IDLE、MOVING_UP/DOWN、DOOR_OPENING/OPEN/CLOSING，由事件触发状态转换。
- ⚖️ 优化难点在于定义“最优”：总等待时间、总旅行时间、停靠数、方向改变、能耗、拥堵等目标会冲突。
- 🔄 同类模式出现在作业调度、CPU 调度、配送路由、数据库查询规划等资源分配问题中。
- 🛠️ 实用方法是：建模当前状态、生成候选决策、估算成本、选择最低成本、状态变化后重新计算。

---

### [错误](https://www.youtube.com/watch?v=ZXAt8AP3DnY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Error](https://www.youtube.com/watch?v=ZXAt8AP3DnY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

无法总结：获取内容时出错 - Response ended prematurely

---

### [](https://codecut.ai/python-3-15-features-data-scientists/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Python 3.15 for Data Scientists: Lazy Imports, frozendict, and Tachyon | CodeCut](https://codecut.ai/python-3-15-features-data-scientists/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

overview summary
Python 3.15 于 2026 年 10 月 9 日发布；文章为数据科学家挑选了最值得关注的更新：惰性导入、frozendict、推导式解包、Tachyon 性能分析、更清晰错误信息，以及 UTF-8 默认和导入 Tab 补全等小改进。

- 🚀 惰性导入（PEP 810）：用 `lazy import pandas as pd` 将加载推迟到首次使用；示例脚本启动从 280 ms 降到 14 ms。
- 🧊 frozendict（PEP 814）：内置不可变字典，防止管道配置被函数意外修改；用 `|` 创建带新值的新配置。
- 📦 推导式解包（PEP 798）：`[*group for group in column_groups]` 展平列表/集合；`{**layer for layer in layers}` 合并字典，后者覆盖前者。
- 🔍 Tachyon 分析器：按毫秒采样而非逐调用计时；开销约 +4%，而 cProfile 慢 3.4 倍；支持火焰图和附加到运行中进程。
- 🧯 更清晰错误：缺失属性会建议如 `.data.shape`；把 JavaScript 风格 `push` 提示为 `append`，元组 `append` 建议改用列表。
- 🌐 UTF-8 默认（PEP 686）：`open()` 在 Windows、macOS、Linux 上行为一致，减少跨平台 CSV/文本编码错误。
- ⌨️ 交互式改进：`from module import <Tab>` 可补全模块名称；补全项按函数、类、模块着色，更易区分。
- ✅ 升级建议：重库导入用 `lazy`；配置用 `frozendict`；慢任务用 Tachyon 火焰图定位瓶颈。

---

### [从零开始构建 GPU 编译器 - 作者：Dmitry Trifonov](https://kernelspace.substack.com/p/building-a-gpu-compiler-from-scratch?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Building a GPU Compiler from Scratch - by Dmitry Trifonov](https://kernelspace.substack.com/p/building-a-gpu-compiler-from-scratch?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

本文以 Emmy 0.3.22 为例，展示如何把 PyTorch 图通过多级 IR 渐进 lowering 到 CUDA：从 Torch IR、Tensor IR、Loop IR、Tile IR、Kernel IR 到最终 CUDA，并用 RMSNorm、matmul 和 attention 说明各阶段为何存在。

- 🧱 编译器核心是 IR 栈与渐进 lowering；各层职责分离，便于设计操作集、添加优化、后端和调度选择。
- 🐍 前端用 `torch.export` 捕获 PyTorch module 为 Torch IR；RMSNorm 此时仍是一个高层算子。
- 🔗 Tensor IR 统一不同框架的算子与布局，显式化索引和归约；PyTorch 与 TensorFlow Dense 可归约为同一计算。
- 🔁 Loop IR 将 Tensor IR 节点转为标量循环并融合；例如 `exp(-x)` 和 RMSNorm 消去中间张量，统计量留在 kernel 内。
- 🧹 Loop IR 规范化去除重复计算并统一等价程序形式；如 `(x*x)+(x*x)` 合并为一次乘法与一次加法。
- 🧩 Tile IR 引入 GPU 感知调度，用无调度的 Fold 树表示 map/reduce/scan，再单独选择 `place`、`work`、`REDUCE` 等。
- 🧮 RMSNorm 的 Fold 树：内层归约平方和，中层映射为 `rsqrt` 缩放，外层映射输出元素；调度可让 256 个 worker 协作一行。
- 🏷️ Schedule Codec 把 matmul 的完整调度组合编码成规范行；`WORK`、`TILE`、`REDUCE`、`STAGE`、`RASTER` 决定寄存器复用与并发权衡。
- ✂️ Tile IR 可在融合后决定拆分：两个 matmul 融合会重复计算中间 H；cut 后 H 只算一次，代价是 4 KiB 中间张量和第二次 kernel launch。
- 📊 Autotuning 测量合法调度；512×2304 RMSNorm 在 RTX 5090 上测 12 行，最快 2.91 µs，默认 3.25 µs，约 1.12× 提升。
- ⚙️ Kernel IR 最接近硬件，描述 warp shuffle、shared memory、TreeHalve 等硬件操作，随后由 printer 发射目标代码。
- 🚀 CUDA 后端生成可由 `nvcc` 编译的源码；RMSNorm 中 256 线程处理一行，每线程加载 8 个值并复用寄存器写出 8 个输出。
- ✅ 验证在 RTX 5090、CUDA 13.0、PyTorch 2.14.1 上进行；所有编译输出通过 eager 精度检查，不同 GPU 或调度会改变结果。
- 🧠 Attention 示例展示 lowering：普通实现三遍读取 key 并重算 QK；Tile IR 用 online softmax 状态 `(m,d,z)` 把三遍合成一遍。
- 🎓 示例 attention CUDA 是教学调度：每个输出 lane 保存 softmax 状态并只写最终结果；更快版本需共享 score、stage 输入 tile。
- 🔭 未来重点在 Tile IR：编译器在此推理计算、调度与硬件，并做融合、拆分与优化决策；schedule codec 也可供 LLM agent 提议候选并做合法性检查。

---

### [Python 3.14 与 Python 3.15 – 性能测试](https://en.lewoniewski.info/2026/python-3-14-vs-python-3-15-performance-testing/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Python 3.14 vs Python 3.15 – performance testing – Lewoniewski.info](https://en.lewoniewski.info/2026/python-3-14-vs-python-3-15-performance-testing/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

本文比较 Python 3.14.8 与 Python 3.15.0 在 Windows 11 64 位环境下的性能，测试机为 AMD Ryzen 9 7900 桌面和 Intel Core i3-1315U 迷你主机，使用 pyperformance 1.14.0 与 pyperf 2.10.0。Python 3.14 为参考版本，总体结果按各基准加速比的几何平均计算；Python 3.15 整体约快 1.451 倍，等效耗时减少约 31.1%，但提升高度集中在少数编码类基准，不能直接套用到所有应用。

- 🧪 测试规模：AMD 平台有 122 个配对基准，Intel 平台有 118 个配对基准，均为 Windows 11 上的 64 位 Python 构建。
- 📊 总体结果：Python 3.15 在两台机器上的几何平均加速均约为 1.451 倍，等效耗时减少约 31.1%。
- 🚀 最大提升：编码类基准异常突出，base32_large 在 AMD 快 134.748 倍、Intel 快 142.255 倍；ascii85_large 快 68.675/56.825 倍；base85_large 快 63.446/62.619 倍。
- 📦 小输入编码：Ascii85、Base32、Base85 的小样本基准也大幅提升，约快 31–41 倍。
- 🧮 剔除异常编码后：去掉六个 Ascii85/Base32/Base85 基准，整体提升降至约 1.203 倍（AMD）和 1.197 倍（Intel），约等于耗时减少 17%。
- 📈 中位数表现：AMD 每个基准中位加速 1.184 倍，Intel 为 1.166 倍，说明总平均被少数超大提升拉高。
- 🐢 部分回退：base16_large/base16_small 在 AMD 慢约 1.22 倍；regex_effbot 在 AMD 慢 1.222 倍、Intel 慢 1.133 倍；regex_dna 在 AMD 慢 1.10 倍。
- 🧩 分组表现：serialize 组约快 3.05 倍，template 约快 1.20 倍，apps 约快 1.13/1.11 倍，asyncio 约快 1.11 倍，math 约快 1.24/1.20 倍，regex 与 startup 接近持平。
- 🧾 原因线索：Python 3.15 发布说明中的 Base32、Ascii85/Base85 C 重写和 Base64 优化，可解释大部分编码类提升。
- ⚠️ 数据可信度：结果是多次会话平均，不声称每个差异都具统计显著性；† 标记表示波动大或方向变化，Intel 平台整体更不稳定。
- 🖥️ 结论：Python 3.15 对编码、序列化、模板等部分负载有明显收益，但不能把 1.45 倍套用到所有应用；结果比较的是完整解释器构建，不能单独归因于 JIT、编译器或某一改动。

---

### [](https://codewithstein.com/automating-django-deployments-with-deployer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Automating Django deployments with Deployer | Code With Stein](https://codewithstein.com/automating-django-deployments-with-deployer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

overview summary
本文说明如何使用 Deployer 自动化 Django 部署：保留 Nginx + Gunicorn + Supervisor 架构，通过 release 目录、shared 文件和 current 软链接，让 `dep deploy` 取代手动 SSH 部署，并支持失败保护和 `dep rollback` 回滚。

- 🧭 背景：作者之前用 Gunicorn、Supervisor、Nginx 手动部署多个 Django 项目，但每次发布都要 SSH 登录并重复命令。
- 🎯 自动化目标：只需在本地运行 `dep deploy`，Deployer 就连接服务器、拉代码、建虚拟环境、装依赖、检查、迁移、收集静态文件、发布并重启 Gunicorn。
- 🧰 Deployer 介绍：它由 PHP 编写，通过 SSH 执行任务；不限于 PHP，支持 Git 克隆、release 管理、共享文件、软链接切换和回滚。
- 🖥️ 服务器准备：Ubuntu 上安装 Nginx、Supervisor、Git、Python3、pip、venv、python3-dev、build-essential，PostgreSQL 编译可能还需 libpq-dev。
- 👤 部署用户：创建 `deploy` 用户和 `/var/www/myproject`，并让 Deployer 通过该用户的 SSH 密钥连接服务器。
- 📁 新目录结构：使用 `releases/` 保存每次发布，`current` 软链接指向当前 release，`shared/` 保存 `.env` 和 `media/` 等跨版本文件。
- 🔗 共享文件：`.env` 与 `media` 放在 shared，并在每个 release 中软链接回 shared，避免上传文件和配置在部署时丢失。
- 💻 安装 Deployer：本地需 PHP/Composer，可运行 `composer global require deployer/deployer`，用 `dep --version` 验证。
- 📝 `deploy.php`：配置应用名、Git 仓库、保留 release 数、主机、远程用户、部署路径和分支；服务器需配置 Git deploy key 访问私有仓库。
- 🐍 Python 任务：`python:venv` 为每个 release 创建独立 `.venv`，`python:install` 升级 pip 并安装 requirements.txt。
- ✅ Django 任务：`django:check` 运行 `manage.py check --deploy`，`django:migrate` 运行迁移，`django:collectstatic` 收集静态文件。
- ⚙️ Supervisor 与 Nginx：Supervisor 从 `current/.venv/bin/gunicorn` 启动，Nginx 静态文件指向 `current/staticfiles/`，媒体文件指向 shared/media。
- 🔐 权限处理：通过 sudoers 只允许 deploy 用户免密执行 `supervisorctl restart myproject`，避免给完整 root 权限。
- 🚀 部署流程：`deploy` 任务按 prepare、venv、install、check、migrate、collectstatic、publish、supervisor restart 顺序执行。
- 🛟 失败与回滚：构建失败不会切换 `current`，旧版本继续运行；`dep rollback` 可切回上一 release 并重启 Supervisor。
- ⚠️ 数据库限制：代码可回滚，但 `migrate` 不会自动回滚；生产迁移应尽量向后兼容，分步修改 schema。
- 🔍 调试与扩展：用 `dep deploy -v` 或 `-vvv` 查看详细命令；可覆盖分支、配置 staging/production 主机，并进一步接入 GitHub Actions 等 CI/CD。
- 🧾 总结：Deployer 将重复部署步骤写入 `deploy.php`，让频繁发布更可靠、可追溯，`dep deploy` 和 `dep rollback` 成为主要工作流。

---

### [](https://www.youtube.com/watch?v=ux7MlXxFDQY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Polars Query Optimization: Lazy vs. Eager Mode - YouTube](https://www.youtube.com/watch?v=ux7MlXxFDQY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

该文本为 YouTube 页脚信息，包含平台介绍、联系与创作者入口、法律政策链接以及版权声明。

- ℹ️ 导航链接：About、Press、Copyright、Contact us，用于了解平台、媒体资源、版权和联系渠道。
- 🎬 创作者与商业入口：Creators、Advertise、Developers，分别面向创作者、广告主和开发者。
- 📜 法律与政策：Terms、Privacy、Policy & Safety，涵盖服务条款、隐私及政策安全。
- ⚙️ 平台说明与更新：How YouTube works、Test new features，介绍 YouTube 运作方式并测试新功能。
- ©️ 版权信息：© 2026 Google LLC，表明版权归 Google LLC 所有。

---

### [](https://astralord.github.io/posts/speculative-decoding-the-art-of-guessing-well/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Speculative Decoding: The Art of Guessing Well | AstraBlog](https://astralord.github.io/posts/speculative-decoding-the-art-of-guessing-well/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

这篇长文从第一性原理系统讲解投机解码：解码受内存带宽限制，便宜 drafter 先猜多个 token，目标模型一次前向并行验证，从而在输出分布不变的前提下加速；文章进一步覆盖投机采样、Gumbel 耦合、块验证、token 树、EAGLE/MTP/DFlash/DSpark/Domino/H-Spec 等架构、KV cache 优化，以及以接受率为中心的训练目标。

- 🧱 解码瓶颈：自回归解码每 token 都要读全部权重，8B bf16 模型在 H100 上读权重约 4.8 ms，batch size 1 上限约 208 token/s；在达到 ops:byte 比例前，多验证几个 token 几乎不增加时间。
- 🎯 投机解码核心：drafter 提议 γ 个 token，target 一次前向验证，接受最长一致前缀，并在首次分歧处追加 target 自己的 token，一轮可得 1 到 γ+1 个 token。
- 🎲 投机采样：用接受概率 min(1, p(x)/q(x)) 与残差分布 (p−q)₊/(1−α) 保证输出严格服从 target；接受率 α=Σ min(p,q)=1−TV(p,q)。
- 🎛️ Gumbel 耦合：drafter 与 target 共享 Gumbel 噪声，使采样变成确定性 argmax，输出对 drafter 不变、可复现，但接受率低于最优投机采样。
- 📈 加速公式：接受长度 τ≈1+Σₖ∏ᵢαᵢ，加速比≈τ/(n_draft·c+1)；并行 drafter 把 n_draft 从 γ 降到 1，因此同接受率下更快。
- 🧩 块验证：不再逐 token 拒绝，而是用 running weight wₖ 联合判断整个前缀，理论上在给定 draft 下期望接受 token 数最多，且无损。
- 🌲 Token 树：把多个候选分支压成树状注意力掩码，一次验证多条路径；但树对 attention kernel、KV cache 分页、CUDA graph 静态形状不友好。
- ⚖️ 批量与树：批量增大后验证变计算受限，最优树大小约 N*≈ops:byte/B；小批量低延迟适合大树，高吞吐服务更常用链式 draft。
- 🧬 Drafter 统一框架：每个 drafter 都是 q(x_{t+k}|x≤t, H, x_{t+1:t+k−1})，关键差异在于是否自回归、读 target 多少信息、如何利用先前猜测。
- 🦅 自回归 drafter：EAGLE 在 target 隐状态层做自回归草稿；EAGLE-2 用动态树；EAGLE-3 融合多层隐状态并采用 training-time test，报告最高约 6.5× 加速，但顺序成本仍高。
- 🔗 MTP：多 token 预测模块与目标模型一起训练，DeepSeek-V3/V4、Qwen3.5、Kimi-K3 等采用；推理时可直接作为 drafter，Kimi-K3 还将其微调为 EAGLE-3 风格。
- ⚡ 并行 drafter：一次前向预测整个 block，如 Medusa 的独立头、P-EAGLE 将 EAGLE-3 并行化、DFlash 的 masked block 预测；并行度越高，越接近“一次草稿一次验证”。
- 🧱 DFlash：按掩码扩散方式训练，但推理时一次预测整个 mask block；它把 target 多层隐状态作为额外 K/V 注入每一层，5 层 EAGLE-3 与 DFlash 同 τ=4.2 时，加速可达 2.1× 与 3.3×。
- 🌳 DDTree：无需训练，把并行 drafter 的逐位置边际概率用 best-first 搜索变成 token 树；在 Qwen3-8B/MATH-500 上把 DFlash 接受长度从 7.79 提到 10.73。
- ⚠️ 并行盲区：独立边际会造成 repetition trap 和路径混搭；信息 floor 表明只看前一个已实现 token 就能消除 86–100% 的并行盲区，剩余主要是模型差距。
- 🐍 DSpark：给 DFlash 风格 backbone 加低秩 Markov 因果头，使当前 token 依赖前一 token；再用 confidence head 调度批量 draft 长度，已在 DeepSeek-V4 生产服务中验证，用户生成加速 57–85%。
- 🁣 Domino 与 DFlash2：Domino 用 GRU 记忆全前缀并配 base-anchored curriculum；DFlash2 用深度卷积增强块内信息交换，并在 top-16 候选格上做选择器，兼顾上下文与低开销。
- 🔁 循环、编辑与回收：D-Loop/DEdit 二次细化草稿块，DLoop 跨轮继续草拟，ReTrace/Carryover 回收 rejected token 的隐状态或 KV，减少浪费并提升接受长度。
- 💾 KV cache 压力：并行 drafter 若自建全上下文 K/V，会随并发与长上下文爆炸；滑动窗口、压缩缓存、复用 target KV、循环状态是主要节省手段。
- 🧮 H-Spec：注意力直接读取 target KV，并用 Mamba-2 循环状态概括上下文；既降低 drafter 自身 cache，又提升接受长度，在 vLLM 中高并发下峰值吞吐提升 5–17%。
- 🎯 训练目标：KL 只是接受率的代理，容量受限时 KL 最优不等于 α 最优；TV 才直接对应接受率，LK 损失用 KL 到 TV 的自适应过渡和 −log α 来优化接受率。
- 🧪 进阶目标：从 per-token 的 LK，到 per-block 的 E2E-TV/BV，再到 per-sequence 的 EDR；BV 损失在块验证下可多接受 13–21%，EDR 用马尔可夫奖励过程建模整轮解码。
- 🏭 服务现实：SGLang、vLLM 等引擎已收敛到 mtp、eagle3、dflash、dspark 等少数 drafter 家族；架构趋势是并行 backbone、轻量因果头、深度利用 target 信息，并针对 serving 约束设计。
- 🔭 结论与未来：架构决定 q 能表达什么，目标决定实际学到什么；长上下文/agentic 负载、并行 drafter 的接受率感知训练，以及扩散语言模型 drafter 仍是开放方向。

---

### [构建你自己的决策模型](https://nishtahir.com/build-your-own-decision-model/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Build your own decision model](https://nishtahir.com/build-your-own-decision-model/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

文章介绍如何构建“System one”决策模型：把 LLM 输出约束到固定选项，单次前向传播选择答案，并用温度缩放校准置信度；示例使用 Qwen/Qwen3-1.7B，并在 CommonsenseQA 上评估。
- 🧠 “System one”决策模型会对每个允许答案推断并给出校准概率。
- ⚡ 与逐 token 生成不同，生成有效 JSON 可能需多次 pass；决策模型通过只允许 A–E 的约束解码/词表掩码，一次 pass 选择最高概率选项。
- 🚫 固定选项能防止输出越界，但不保证答案正确；未额外训练时，输出概率常只是下一 token 置信度，而非正确答案概率。
- 💻 作者用 Qwen/Qwen3-1.7B 演示：格式化问题与选项，取最后 logits 中选项 token 的概率并 softmax，输出预测与各选项概率。
- 🌤️ 示例“天空是什么颜色”预测 B（Blue，0.9988），模型能合理作答。
- 📊 在 CommonsenseQA 随机留出样本上，准确率 0.5938、macro F1 0.5844；快速微调后提升至 0.6241、0.6234。
- 🦇 对“蝙蝠最可能在哪”这类模糊问题，模型给 Cave 0.9978，显示过度自信。
- 📉 分桶评估显示置信度与准确率不匹配：0.9–1.0 桶置信度约 0.9855，实际准确率仅 0.7009，说明未校准。
- 🌡️ 温度缩放校准拟合温度约 3.7973，校准后置信度更贴近准确率（如 0.9–1.0 桶准确率 0.9541）。
- 🛠️ 作者提供 GitHub repo，包含构建数据集、评估、微调与校准脚本，鼓励在更大模型上尝试。

---

### [节省航空燃油](https://tech.marksblogg.com/scikit-decide-openap-optimal-flight-planning.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [
Saving Jet Fuel  ](https://tech.marksblogg.com/scikit-decide-openap-optimal-flight-planning.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

本文以航空节油为背景，介绍如何用开源工具 scikit-decide、OpenAP、OpenTop 等结合 NOAA 风数据，对航班路径、爬升策略和机型性能进行优化，并展示多个 A320 与 B737 案例。

- ✈️ 波音 787-9 从 EWR 到 FCO 的 8.5 小时航班可能消耗约 6.8 万美元燃油，调整航路可节省数千美元。
- 🧰 Jeppesen 等商业方案之外，scikit-decide 加 TU Delft 燃油模型和 NOAA 风数据提供开源替代方案。
- 🤖 scikit-decide 已开发 6 年，支持强化学习、自动规划与调度，可优化航路、机组排班和无人机集群路径。
- 📊 OpenAP 是 Junzi Sun 博士开发的飞机性能模型，配套 OpenTop 轨迹工具包；文中使用 Python 3.12、DuckDB、QGIS 等。
- 🛩️ OpenAP 数据包含多种机型、427 款发动机、近 1.4 万个机场，覆盖 236 个国家，并含导航点、导航台及燃油模型。
- 🧮 示例使用 A320 与 OpenAP 燃油模型，对比不同飞行路径；求解器可由 A* 或 Dijkstra 式搜索完成。
- 🇫🇷🇩🇪 图卢兹→柏林案例：A320 在 2026-05-01 风场下，目标在第 19 步达成，时间约 7666 秒，油耗约 5855 千克。
- 🇫🇷🇵🇱 图卢兹→华沙案例：初始目标高度更高，航线更直接；虽远约 500 公里，却快约 45 分钟，文中称仅需柏林航班约 76% 的燃油。
- 🌬️ 天气数据来自 NOAA GFS；若所需日期在近六个月内，会自动下载约 143–144 MB 的 GRB2 全球风场文件。
- 🧭 OpenTop 可结合 OpenAP 计算轨迹；优化需要网格代价文件，文中使用 142 MB NetCDF 并生成 246 KB Casadi 文件。
- 🇳🇱🇩🇪 EHAM→EDDF 对比：A320 使用 0.3×燃油加 0.7×网格目标，油耗 1625.6 kg，耗时 35.8 分钟，最高 19891 ft。
- 🇳🇱🇩🇪 B737 同航线：油耗 1622.1 kg，耗时 39.2 分钟，最高 21968 ft；两者油耗接近，A320 稍快。
- 💼 作者提供北美和欧洲的咨询与开发服务，可通过 LinkedIn 联系。

---

### [](https://github.com/lyogavin/airllm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - lyogavin/airllm: AirLLM 2.8T LLM inference with single 4GB GPU · GitHub](https://github.com/lyogavin/airllm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

AirLLM 是一个开源项目，通过按层流式加载与低显存优化，让超大语言模型能在普通 GPU 上运行和训练；其核心亮点是单张 4GB GPU 即可推理 2.8T 级模型，并支持 125B 模型在 6GB 以下训练。

- 🚀 AirLLM 可在单张 4GB GPU 上运行 2.8T 级 LLM，无需量化、蒸馏或剪枝。
- 📉 实测支持：Kimi K3（2.8T）低于 4GB，Qwen3.8-Flash-Next（125B）约 6GB，DeepSeek-V3（671B）约 12GB。
- 🧠 小显存训练：Qwen3.8-Flash-Next（125B）低于 6GB，Qwen3.8-27B 在 seq 512 时约 2GB。
- ⚙️ 安装与使用简单：`pip install airllm`，通过 `AutoModel.from_pretrained(...)` 一行加载模型。
- 🧩 推理时会将原模型拆分并按层保存，需确保 Hugging Face 缓存目录有足够磁盘空间。
- ⚡ 支持 4bit/8bit 块状量化压缩，最高约 3 倍推理加速，且精度损失几乎可忽略。
- 🗂️ 主要配置包括 compression、profiling_mode、layer_shards_saving_path、hf_token、prefetching、delete_original。
- 🍎 支持 macOS，但仅限 Apple Silicon，并需安装 mlx 和 torch。
- 🌐 支持主流模型家族：Llama、Qwen、DeepSeek、Mistral/Mixtral、Phi、Gemma、ChatGLM、Baichuan、InternLM、Yi、Kimi K3 等。
- 💡 显存需求取决于单层大小而非总参数量：8B 约 1–2GB，70B 约 4GB，405B 约 8GB，671B 约 12GB。
- 🏋️ 训练时冻结基座权重逐层流式加载，仅适配器常驻 GPU，不同于 Hugging Face Trainer / bitsandbytes QLoRA。
- 📝 训练数据支持 `.jsonl`，字段可为 text、prompt+completion、instruction+input+output，也支持 `.txt`。
- 🐍 训练 API 包括 `AirLLMLoRAQwen4Exp` 和 `AirLLMLoRA`，并提供示例脚本。
- 🧯 常见问题：`MetadataIncompleteBuffer` 多为磁盘不足；模型类型不匹配应使用 `AutoModel`；受限模型需 `hf_token`；无 pad token 可关闭 padding。
- ⭐ 项目热度：38.9k stars、4k forks、314 watchers、389 commits，采用 Apache-2.0 许可。
- 📄 研究使用可引用 BibTeX，项目欢迎贡献、反馈与赞助。

---

### [](https://github.com/Facebook/lifeguard?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - facebook/Lifeguard: Lifeguard is a static analyzer to detect Lazy Imports incompatibilities and ease the adoption overhead for Lazy Imports in Python · GitHub](https://github.com/Facebook/lifeguard?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

Lifeguard 是 Facebook 开源的 Rust 静态分析器，用于检测 Python Lazy Imports 的不兼容模式，降低采用 PEP 810 Lazy Imports 的迁移成本，并保守地将无法证明可安全延迟导入的模块标记为不安全。
- 🛡️ 目标：帮助大型 Python 代码库安全启用 Lazy Imports，减少内存占用、启动时间和导入开销。
- ⚡ Lazy Imports 会将模块加载推迟到首次访问，但模块级副作用、注册表模式、`sys.modules` 操作、元类和 `__init_subclass__` 等模式可能因此失效。
- 🔍 工作原理：并行分析 Python 源文件，遍历 AST 检测副作用，并映射 Lazy Imports 不兼容影响为错误。
- 🧪 项目阶段：Beta，目标是在 Python 3.15 正式版前达到通用可用；已测试支持 Python 3.12 和 3.14。
- 🐍 分析 PEP 810 显式 lazy import 语法时，需要传入 `--python-version 3.15`。
- 📦 安装方式：`pip install lifeguard-lazy-imports`，提供 Linux、macOS、Windows 的预编译 wheel，要求 Python 3.12+，无需 Rust 工具链。
- 🚀 快速开始：`lifeguard run-tree /path/to/project output.json --verbose-output verbose.txt`，可自动发现目录下的 `.py` 文件并跟随可解析的顶层导入。
- 🗂️ 大型项目可生成 source DB，即 JSON 格式的模块路径到磁盘位置映射，并可在 `pyproject.toml` 中配置 `site_packages`。
- 📊 默认模式输出高层分析结果和 JSON；verbose 模式额外生成逐行不兼容报告，可当作独立 linter 使用。
- ✅ 输出字段 `LAZY_ELIGIBLE`：列出可安全延迟导入的模块，以及这些模块中必须预先急切导入的依赖；未出现在键中的模块视为不安全。
- ⛔ 输出字段 `LOAD_IMPORTS_EAGERLY`：这些模块内部所有导入都必须急切执行，适用于自定义 `__del__`、`exec()` 和 `sys.modules` 访问等边界情况。
- 🧾 verbose JSON 还包含 `IMPLICIT_IMPORTS` 和 `IMPORT_CYCLES`，使用 `--sorted-output` 可获得确定性排序。
- 🧰 输出可用于构建 Python 3.15 的 `sys.set_lazy_imports_filter()` 回调，以驱动 lazy import loader；官方计划提供更易用的集成工具。
- 🦀 实现：使用 Rust，借助 `ruff` 进行 AST 遍历，复用 `pyrefly` crates，并通过扩展 `.pyi` stub 标注第三方库已知副作用。
- 📜 许可证为 MIT；仓库还包含行为准则、贡献指南和安全政策；当前约 131 stars、14 forks、4 watchers。

---

### [](https://github.com/KingKongRobotics/jumper?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - KingKongRobotics/jumper: 🦀 Jumper — an crab robot. · GitHub](https://github.com/KingKongRobotics/jumper?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

KingKongRobotics 的 Jumper 是一个 22 自由度螃蟹机器人开源项目，仓库定位为面向外观、运动与场景创建的 AI 工具包。它支持在 AI 编码助手中通过提示词完成皮肤设计、运动训练与场景生成，并提供相应导出格式与资源指引；训练基于 mjlab、rsl_rl、MuJoCo 和 MuJoCo Warp，项目采用 Apache-2.0 许可。

- 🦀 Jumper 是 22-DoF 螃蟹机器人，官网为 kingkong.tech/jumper。
- 🤖 仓库是 Jumper 的 AI 工具包，覆盖外观、运动与场景创建，可在 AI 编码助手中打开并尝试提示词。
- 🎨 外观设计：一句话即可设计协调配色并导出 `.skin`，示例包括 Warm sand ranger、Silver armor、Raphael Turtle。
- 🚶 运动训练：一句话训练稳定三足步态，回放评估并打包为 `.app`，支持 Walk、Posture、Gesture、Dance、Jump、Grasp。
- 🏞️ 场景创建：一句话创建公园泵道等场景，包含滚动地形、树木和长椅并导出 `.map`，另有 Bedroom、Soccer。
- 📚 主要资源：jumper-design、训练教程、Colab GPU 训练、动作包构建指南、项目指南。
- 🧠 训练依赖：mjlab、rsl_rl、MuJoCo、MuJoCo Warp。
- 📊 仓库数据：2.7k stars、276 forks、19 watchers、6 issues、4 PR、47 commits，主分支为 main。
- 📜 许可：Copyright 2026 KingKong Robotics，维护者材料为 Apache-2.0；第三方材料按其条款，生成输出不自动继承本仓库许可。
- 🌐 README 提供英文与简体中文版本，并包含贡献指南、NOTICE 与第三方声明。

---

### [](https://github.com/microsoft/quicksand?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - microsoft/quicksand: Quickly sandbox your AI agent. · GitHub](https://github.com/microsoft/quicksand?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

Microsoft Quicksand 是微软开源的异步 Python API，用于启动、控制和快照 QEMU 虚拟机，重点是为 AI agent 提供快速、安全的 Linux 沙箱；支持 Ubuntu/Alpine 预构建镜像、x86_64/ARM64、macOS/Linux/Windows，且无需 root 或 Docker。

- 🎯 **项目定位**：Quickly sandbox your AI agent，官网为 microsoft.github.io/quicksand/。
- 🧩 **核心能力**：启动、控制、保存/加载、检查点/回滚 QEMU 虚拟机。
- 💻 **跨平台支持**：Ubuntu/Alpine 镜像，覆盖 x86_64 与 ARM64，可在 macOS、Linux、Windows 上运行。
- 📦 **安装方式**：`pip install 'quick-sandbox[qemu,alpine]'`，或安装核心包后运行 `quicksand install qemu alpine`。
- 🐍 **异步 API**：使用 `async with Sandbox(image="ubuntu") as sb`，通过 `execute()` 运行命令并获取 stdout/exit_code。
- 📂 **文件交换**：启动时用 `mounts` 共享主机目录，运行中也可 `mount`/`unmount` 热挂载。
- 🌐 **网络隔离**：默认网络隔离；`NetworkMode.FULL` 开启互联网；TCP 端口可在 host 与 guest 间双向转发。
- 👥 **多用户沙箱**：可在同一 VM 中用 `create_user` 创建多个独立 Linux 用户并分别执行命令。
- 💾 **保存/加载**：`save("my-env")` 保存 VM 磁盘状态，之后甚至可在不同机器上加载。
- ⏪ **检查点/回滚**：`checkpoint()` 捕获完整 VM 状态，`revert()` 可在风险操作后恢复。
- 🖥️ **桌面控制**：桌面镜像支持截图、输入文本、按键、鼠标移动/点击；可安装 `ubuntu-desktop` 或 `alpine-desktop`。
- 🛠️ **配置选项**：支持 image、memory、cpus、mounts、network_mode、port_forwards、disk_size、enable_display、save。
- 🏗️ **预构建镜像**：ubuntu、alpine、ubuntu-desktop、alpine-desktop、quicksand-agent、quicksand-cua，体积约 82 MB 到 500 MB。
- 📚 **文档与构建**：文档覆盖安装、生命周期、命令、文件交换、保存回滚、桌面、网络与性能；源码构建使用 `uv sync` 和 `uv run uvr build --all-packages`。
- 📈 **仓库状态**：微软开源项目，MIT 许可，约 214 stars、14 forks、330 commits、3 issues、4 PR。

---

### [](https://github.com/NVlabs/LongLive?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - NVlabs/LongLive: Long Video Gen / World Model / World Action Model (Embodied) Infrastructure · GitHub](https://github.com/NVlabs/LongLive?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

overview summary
NVIDIA NVlabs 的 LongLive 是一个面向长视频生成、世界模型与具身世界动作模型的开源基础设施仓库，汇集多个自包含项目，覆盖实时交互生成、NVFP4 并行训练/推理、一次性蒸馏和机器人策略/视频生成，并采用 Apache-2.0 许可。

- 🎬 LongLive 定位为“长视频生成 / 世界模型 / 世界动作模型（具身）基础设施”，GitHub 获约 2.8k stars、265 forks、21 watchers。
- 📂 仓库包含四个主要自包含项目：Long-WAM、LongLive-Plug、LongLive2.0、LongLive1.0，每个项目有独立代码、文档和模型权重。
- 🤖 Long-WAM：长上下文世界动作模型，具备流式视觉记忆，用于机器人策略训练/评估、机器人视频生成，支持 YAM、Franka、Unitree G1 部署，并覆盖 LIBERO、RoboTwin 2.0、RoboCasa 等基准。
- 🧩 LongLive-Plug：面向视频生成的“一次蒸馏、处处复用”方案，在基座模型训练功能 LoRA，再迁移到兼容下游模型，支持 Wan2.1-14B、Wan2.2-TI2V-5B 和 MiniMax-H3。
- ⚡ LongLive2.0：面向长视频生成的 NVFP4 并行基础设施，支持 T2V/I2V 自回归训练、多镜头、NVFP4/BF16、DMD 蒸馏、NVFP4 W4A4/KV 缓存、FP8 PTQ、序列并行推理和异步解码等。
- 🎥 LongLive1.0：实时交互式长视频生成，可接收连续提示并实时生成/引导长视频；核心包括 attention sink、KV-recache 与 streaming long tuning，已被 ICLR 2026 接收。
- 🚀 性能亮点：LongLive-2.0-5B 达 24.8 FPS、VBench 85.06；NVFP4-4Step 达 29.7 FPS；NVFP4-2Step 达 45.7 FPS；LongLive-1.3B 达 20.7 FPS、VBench 84.87，且 2.0 支持多镜头。
- 📰 近期动态：发布 Long-WAM 论文与代码；发布 LongLive-Plug 训练/推理代码；LongLive 2.0 支持 FP8、I2V 自回归教师强制训练和 DMD 蒸馏；NVFP4 推理优化带来约 18.6% 吞吐提升。
- 🧠 模型与检查点：Long-WAM 检查点托管在 Efficient-Large-Model；LongLive-Plug 提供多模型适配；LongLive 2.0/1.0 提供 5B、1.3B 及 NVFP4 变体。
- 📦 使用方式：各项目可按需 partial clone + sparse checkout 单独下载，例如仅下载 Long-WAM 时可使用 `git sparse-checkout set Long-WAM`，无需下载其他项目。
- 🌍 生态：LongLive 已被 DreamForge-World、DreamX-World、SANA-Video/LongSANA、MemFlow、ShotStream、TriAttention、LongLive-RAG、Forcing-KV、MemRoPE、Astrolabe 等项目采用或扩展。
- 📜 许可与引用：Apache-2.0 开源；README 提供论文引用，并致谢 Self-Forcing、Wan2.1、Wan2.2、MiniMax-H3 等基础工作。

---

### [](https://pypi.org/project/whatsnewt/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [whatsnewt · PyPI](https://pypi.org/project/whatsnewt/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

whatsnewt 3.15.4 是一个 TUI 文本冒险游戏，让玩家在真实 Python 3.15 解释器中通过编写并运行代码，学习 Python 3.15 的新特性。
- 🎮 从 Startup Foyer 走到 Release Gate，包含 18 个谜题、15 个房间、6 个 Sigils，示例总分为 375。
- 📦 可用 `pip install whatsnewt` 安装；推荐 `uvx --python 3.15 whatsnewt`，要求 Python 3.15.0b1 或更新，旧版 uv 可能拉取 alpha 并退出。
- 🧩 谜题不只是选择题，会检查代码实现方式；部分答案由 pyrefly 类型检查器验证。
- 🗺️ 支持地图、库存、分数、提示（扣分）等机制；命令包括方向移动、look、examine、take/drop、inventory、map、score、solve、hint、save/load/quit。
- ⌨️ 支持 Tab 补全和可点击文档/PEP 链接；快捷键含 ctrl+r 检查、ctrl+h 帮助/提示、ctrl+o 外部编辑器、ctrl+g 关闭或中止。
- 🖥️ 全屏 TUI 建议 112x40，最低 80x24；参数包括 `--text`、`--load`、`--theme`、`--reset`，并包含彩蛋。
- 💾 自动保存到 `$XDG_STATE_HOME/whatsnewt/` 或 `~/.local/state/whatsnewt/`，重启可恢复，旧档会移到 `previous-game.json`。
- 🐍 覆盖 PEP 829 启动配置、PEP 810 惰性导入、PEP 814 frozendict、PEP 661 sentinel、PEP 686 UTF-8 默认、Unicode 17、PEP 798 推导式解包、PEP 728/747/800 类型特性等。
- ⚙️ 还涉及升级版 JIT、mimalloc、`bytearray.take_bytes`、`math.integer`、Tachyon、frame pointers、改进错误消息、`re.prefixmatch`、颜色与 3.15 移除项。
- 🧪 项目由 Hatch 管理，可运行 `hatch run all` 做测试和静态分析；欢迎反馈 bug 或教学不准确之处。
- 👤 作者 Barry Warsaw，Apache-2.0 许可，与 Claude 合写；3.15.4 于 2026-10-15 发布，含 sdist 与 wheel，要求 Python >=3.15。

---

### [](https://github.com/SEIU-Tech/python-date-parser?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - SEIU-Tech/python-date-parser: Perform fast fuzzy parsing of dates in varying formats · GitHub](https://github.com/SEIU-Tech/python-date-parser?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

该仓库 `python-date-parser`（包名 `gnosis-date-parser`）提供基于 Rust 的快速模糊日期解析能力，主要用于处理同一列中格式混杂的日期数据；它通过 Python 绑定暴露接口，性能远超纯 Python 方案，并比 Pandas 的混合格式解析快约 50 倍，采用 BSD-2-Clause 许可证。

- 📅 核心用途：对多种格式的日期进行快速模糊解析，解决大规模表格数据中异构日期解析慢的问题。
- 🦀 实现方式：作为 Rust `dateparser` 库的轻量 Python 封装，主要逻辑由 Rust 扩展完成。
- 🐍 三个 API：`parse(raw)` 返回 ISO-8601 字符串或 `None`；`parse_list(list)` 批量返回同长度、同顺序结果；`parse_series(Polars Series)` 返回 `pl.Datetime("ns")`，无法解析则为 `null`。
- ⚡ 批量路径：`parse_list` 一次 Rust 调用处理整个列表；`parse_series` 通过 `pyo3-polars` 直接操作 Arrow 缓冲区，避免 Python 层迭代。
- 🔌 Polars 依赖：`parse_series` 需要可选依赖 `polars`，未安装时会抛出 `ImportError`，需安装 `gnosis-date-parser[polars]`。
- 🌐 解析规范：结果统一归一化为 UTC（`+00:00`）；纯数字输入按 Unix 时间戳处理：10 位为秒、13 位为毫秒、16 位为微秒、19 位为纳秒。
- 📦 安装方式：基础功能 `pip install gnosis-date-parser`；Polars 支持 `pip install "gnosis-date-parser[polars]"`。
- 📊 性能对比：`dateparser` 约 147 d/s，`pandas.to_datetime(format="mixed")` 约 40,363 d/s，`parse()` 约 1,164,578 d/s，`parse_list` 约 1,294,147 d/s，`parse_series` 约 1,992,147 d/s。
- 🛠️ 开发工具：使用 `uv` 管理环境，`maturin` 编译 Rust 扩展，`pytest` 测试，`ruff` 与 `mypy` 检查，`mkdocs` 文档。
- 📜 许可证与状态：BSD-2-Clause；仓库公开，约 2 stars、1 watcher、1 fork、39 commits。
- 🤖 项目背景：在 AI 助手协助下创建，提交署名 Claude，实际使用定制版 MiniMax M3，通过 Claude Code CLI 交互。

---

### [](https://github.com/Vedantgitbot/booth?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - Vedantgitbot/booth: A lightweight, zero-dependency Python checkpoint layer for structured LLM output reliability. · GitHub](https://github.com/Vedantgitbot/booth?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

BOOTH 是一个轻量、零依赖的 Python 检查点层，位于应用与 LLM 调用之间，用结构化结果判断输出是否可信，并通过证据校验阻断幻觉；它强调显式不确定性、可解释拒绝和提供商无关。

- 📦 BOOTH 是用于结构化 LLM 输出可靠性的开源 Python 库，PyPI 包名为 `boothpy`，采用 MIT 许可。
- ⚡ 安装方式为 `pip install boothpy`；核心 `booth.check()` 接收现有 LLM 函数并返回 `BoothResult`，而不是直接返回文本。
- 🧭 状态码包括：`ACCEPTED` / `REPAIRED` 表示通过或重试通过；`AMBIGUOUS`、`UNCERTAIN`、`BLOCKED` 表示拒绝；解析失败归为 `UNCERTAIN` 且 `method == "parse_failure"`。
- 🛡️ `booth.check_with_evidence()` 用应用检索到的证据校验答案，可阻断与证据不符的回答，且本身不执行 LLM 调用。
- 🔁 `booth.acheck()` 是 `check()` 的异步版本，支持异步模型调用与异步执行循环。
- 🔌 零依赖、provider-agnostic：由应用提供模型调用函数，因此可搭配任意 LLM 客户端；示例覆盖 Groq、Gemini、Anthropic、Ollama 本地模型。
- 🧪 `examples/` 提供可运行集成示例和真实 `RESULTS.md`，包含成功、失败与负面结果；欢迎贡献新的 provider 示例。
- 🧠 设计理念：检查点保持小；显式暴露不确定性；歧义、验证、置信度分开且有序检查；失败原因决定重试反馈；暴露不重释；拒绝不合法数据；证据检索留在 BOOTH 外；不把一致性当真相。
- 📚 配套文档包括 `TUTORIAL.md`、`USECASES.md`、`CHANGELOG.md`、`TROUBLESHOOTING.md`、`CONTRIBUTING.md`，覆盖 API、架构定位、发布记录与常见问题。
- 👤 官方仓库由 Vedant Brahmbhatt 维护，当前约 16 stars、7 forks、70 次提交。

---

### [](https://github.com/agustin18/fastapi-stream-lease?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - agustin18/fastapi-stream-lease: Distributed stream and SSE concurrency lease manager for FastAPI and Starlette backed by atomic Redis Lua scripts. · GitHub](https://github.com/agustin18/fastapi-stream-lease?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

fastapi-stream-lease 是面向 FastAPI/Starlette 的分布式流并发租约管理器，使用 Redis Lua 原子脚本限制同时活跃的 SSE、LLM token 流和 WebSocket 会话，支持按用户、全局限额，并在流开始前用 HTTP 429 拒绝超额连接。

- 🚀 核心用途：回答“当前有多少流打开”，而非“每分钟多少请求”；适合可能持续数秒或数分钟的长连接。
- 📦 安装要求：Python 3.10+、Redis 5.0+、redis-py 4.6+；可安装 `fastapi-stream-lease[fastapi]` 获得 FastAPI 辅助功能。
- 🔌 集成方式：核心接受调用者自有的异步 Redis 客户端；FastAPI 中可用 `manager.stream()` 一行保护 `StreamingResponse`。
- 📡 WebSocket 支持：使用 `async with manager.lease(user_id)` 覆盖整个会话，租约自动续期，断开按常规处理。
- ⏳ 租约模型：租约在 `lease_seconds` 内未成功续约即过期；默认每半间隔续期，瞬断时有自适应宽限期。
- 🚦 限额控制：`max_per_user` 和 `max_global` 可单独或同时启用；设为 0 表示禁用；超额返回 429 与 `Retry-After`。
- 🧮 原子 Lua：获取、续期、过期清理、释放均原子执行；键共享 Redis Cluster hash tag，支持单槽多键检查。
- ⏱️ 动态重试时间：Lua 用 `ZRANGE ... 0 0 WITHSCORES` 以 O(1) 找到最早过期租约，计算剩余容量释放时间。
- 🪟 获取超时窗口：`acquire_timeout` 或 `timeout` 参数用协作重试吸收瞬时并发峰值、重连风暴，减少过早 429。
- 🧹 优雅关闭：`manager.close(drain=True, timeout=5.0)` 等待活跃本地流自然结束，超时后并发强制释放，避免幽灵租约。
- 🛡️ 故障策略：Redis 获取失败时默认 `fail_open=False` 返回 503；`fail_open=True` 可降级为本地、未协调的内存回退租约。
- 🧭 分布式保证：worker 崩溃后租约由 Redis TTL 自愈；所有过期判断使用 Redis `TIME`，避免 worker 时钟漂移。
- ⚠️ 故障模型限制：Redis 异步复制、Sentinel、Cluster 故障切换可能丢失未复制写；未复制租约会在下次续期时被取消。
- 🔁 断路器：可选 worker 本地熔断器，状态为 CLOSED/OPEN/HALF_OPEN；OPEN 时获取快速失败或回退，但绝不阻止续期。
- 🎯 续期优先：获取创造新并发，可快速失败保护后端；续期保护已有流，OPEN 期间仍重试，Redis 恢复后自动愈合。
- 🧱 Redis 拓扑：支持 Sentinel 与 6 节点 Cluster；所有键用 hash tag 保证同槽，支持槽故障转移与 MOVED 重定向恢复。
- 📊 可观测性：支持 Prometheus/OpenTelemetry 适配器，暴露标准指标；也支持零依赖生命周期回调，但仅 best-effort，不可用于计费或审计。
- 🧪 测试与示例：提供 SSE、WebSocket、OpenAI 流、Prometheus、弹性 SSE 客户端示例；可用 fakeredis 单测，Docker Compose 测试 Sentinel/Cluster。
- ⚙️ 生产建议：Redis 客户端显式设置超时；高并发时扩大连接池 `max_connections`；用 `verify_cluster_config(strict=True)` 检测配置漂移。
- 🔄 配置变更：活跃集群修改限额需迁移：推荐更换 `key_prefix` 做蓝绿，或停 worker、等租约过期、删除 `{prefix}:config` 后滚动更新。
- 🔐 安全：`user_id` 必须来自已验证主体，绝不用未验证请求参数、PII 或原始令牌；最低依赖版本仅为兼容性底线，不是安全建议。
- 📜 版本与许可：严格遵循 SemVer，顶层导出符号为公共 API，指标名/标签视为兼容契约；计划 v1.0.0 稳定冻结，使用 MIT 许可。

---

### [](https://github.com/TheSecuredAnalyst/security-suite?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - TheSecuredAnalyst/security-suite: Open-source security suite for OSINT, web scanning, API testing, SIEM integration, and AI-powered analysis · GitHub](https://github.com/TheSecuredAnalyst/security-suite?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

Security Suite 是一个 AGPL-3.0 开源安全工具套件，覆盖 OSINT 侦察、Web/API 安全测试、代码扫描、SIEM 集成、合规检查与 AI 分析，提供 CLI、REST API 和自动化能力，面向授权安全测试与教育用途。

- 🛡️ 项目定位：综合开源安全套件，当前版本为 SecSuite v0.5.0，支持 OSINT、Web 扫描、API 测试、SIEM 与 AI 分析。
- 🧰 快速安装：提供 `setup.sh` 和 `setup.ps1` 一键安装脚本，可自动安装 Python、依赖、Ollama 和本地 AI 模型。
- 🧩 核心模块：包含 11 个 OSINT 模块、6 个 Web 扫描器、4 个 API 安全工具，并支持 AI、SIEM、调度、合规、漏洞扫描等。
- 🌐 使用方式：提供 `secsuite` CLI 和 FastAPI REST API，REST API 可通过 `/docs` 交互式测试，并支持 API Key 保护。
- 🔎 OSINT 侦察：支持 DNS、WHOIS、子域发现、端口扫描、技术识别、HTTP 头、邮箱收集、VirusTotal 和 Shodan。
- 🕷️ Web 安全扫描：支持 XSS、SQLi、目录爆破、SSL/TLS 分析、爬虫和 Nuclei 扫描。
- 🧑💻 代码扫描：检测泄露密钥、依赖漏洞、风险 JS/PHP 模式，支持 OSV.dev、SARIF 输出和离线模式。
- 🔐 API 安全测试：解析 OpenAPI/Swagger，测试 BOLA/IDOR、注入、认证绕过、JWT 弱点、限流与模糊测试。
- 🤖 AI 能力：支持 Ollama、Anthropic、OpenAI，用于发现关联、执行摘要、安全问答和交互式修复。
- 🧠 关联分析：通过社区可贡献的 YAML 规则，将共现发现转化为带来源链的攻击路径。
- 📡 SIEM 集成：支持 Splunk、Elasticsearch、Syslog，以及 Slack、Discord、PagerDuty 等 Webhook。
- ⚙️ 其他功能：计划任务、OWASP Top 10/CIS 合规评估、威胁情报、密码审计、Exploit 搜索、钓鱼模拟和报告导出。
- 🚧 安全防护：Guardrails 默认拒绝未授权操作，并要求授权会话、ROE 范围和破坏性命令分析；CI 使用 bandit、pip-audit、CodeQL、Dependabot。
- 📚 文档支持：提供 QUICK_START、USAGE、TROUBLESHOOTING、ARCHITECTURE、CHANGELOG、SECURITY 等文档。
- ⚖️ 许可与免责：AGPL-3.0 许可，仅限授权安全测试和教育用途，钓鱼模拟需属于批准的安全意识项目。

---

### [](https://github.com/Haarris/cachecanary?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [GitHub - Haarris/cachecanary: Know the moment your Claude prompt cache breaks on Amazon Bedrock, not when the bill arrives. · GitHub](https://github.com/Haarris/cachecanary?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

CacheCanary 是面向 Amazon Bedrock 上 Claude prompt caching 的 CLI 与 GitHub Action，用于在缓存静默失效、账单飙升前发现并解释问题。它可检查 CI 中的请求、定位缓存 miss 原因，并从 Bedrock 调用日志统计生产命中率和浪费支出。

- 🔎 核心问题：Bedrock 缓存会静默失效，请求仍返回 200、答案仍正确，但缓存读取失败后成本会大幅上升。
- 💸 成本影响：缓存读取通常约为正常输入 token 价格的 1/10；对 10,000 token prompt、100,000 次/月的代理，Sonnet 4.6 列表价下可能每月多花约 2,700 美元。
- 🚨 事故案例：LiteLLM 在 2026 年 7 月升级后，Bedrock 上 Claude Code 流量缓存命中率从约 90% 降至 25–45%，日支出增加 2–3 倍，六天后才被发现。
- 🧭 背景缺口：Anthropic 有缓存诊断功能，但只支持自家 API，不支持 Amazon Bedrock。
- 🌐 网站资源：cachecanary.com 提供 LiteLLM、Strands Agents、LangChain 指南，说明框架发送了什么、缓存为何丢失、如何稳定命中。
- 🛠️ 工具形态：小型 CLI 和 GitHub Action，可在 CI 检查请求、解释 miss 原因，并读取 Bedrock 日志展示生产缓存命中率。
- 📦 安装方式：`pip install cachecanary` 用于 lint/diff/logs；`pip install "cachecanary[aws]"` 额外加入 probe，可调用 Bedrock。
- 🧰 命令集：支持 `lint`、`diff`、`probe`、`logs`；退出码 1 表示检查失败，2 表示无法运行，`--json` 和 `--github` 放在命令前。
- 🕵️ lint 检查：发现缓存前缀中的日期、时间、UUID、用户特定文本、前缀短于模型最低 token 数、工具顺序或定义变化、模型 ID/ARN 未识别、Converse/InvokeModel 切换等问题。
- 🧱 更多陷阱：检查 checkpoint 数量、未知 TTL、1 小时 checkpoint 顺序、InvokeModel 纯字符串 `system`、空 cache point、`toolResult` 内 cachePoint、对话 cache point 落后，以及 thinking 设置或 tool choice 变化。
- 📏 lookback 限制：Bedrock 只回看有限内容块；实测新增 21 个内容块仍命中，22 个必定 miss。
- 🤖 GitHub Action：问题会显示为 PR 注释，并在 job summary 中生成简短表格；lint 不需要 AWS，probe 需要先配置 AWS 凭证，例如 OIDC。
- 📊 生产日志：需开启 Bedrock model invocation logging；`logs` 可读取 S3、CloudWatch、gzip 或流式响应，按模型或 IAM principal 统计命中率，并合并 inference profile ARN 与短模型 ID。
- 💰 计价逻辑：多数模型缓存读取为 0.1x，Opus 5.5 为 0.05x，Fable 5.1 与 Mythos 5.1 为 0.025x；缓存写入为 5 分钟 1.25x 或 1 小时 2x；`global.` ID 按列表价，区域或 `us.`/`eu.` 风格 ID 贵 10%。
- ✅ 测试验证：依据 AWS 文档，并针对真实 Bedrock 验证 Converse/InvokeModel、streaming、两种 TTL、模型最低 token、prompt 变化和 21/22 lookback 边界；2026 年 10 月 15/15 结果与 Bedrock 一致。
- 🔒 隐私：所有内容在本地或 CI runner 运行，不上传；probe 只调用用户自己的 Bedrock endpoint 和凭证。
- 🚧 限制：lint token 数是估算值，英文文本约低估 11%；超过 100 KB 的响应体不会内联存储并显示为 unparsed；美元按列表价计算，不含 batch、provisioned throughput、priority，目前仅支持 Bedrock。
- 🧭 下一步：计划推出托管 dashboard，展示每个应用的命中率、浪费支出、下降告警和每次 miss 原因，并运行在用户自己的 AWS 账户中；也计划支持 Vertex AI。
- 📜 许可与作者：Apache 2.0，版权 2026 Haris Farooq，作者是在生产环境运行 Bedrock Claude agents 的工程师。

---

### [](https://www.python.org/downloads/release/python-3150/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Python Release Python 3.15.0 | Python.org](https://www.python.org/downloads/release/python-3150/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

Python 3.15.0 于 2026 年 10 月 9 日正式发布，这是 Python 编程语言的最新主要版本，包含来自 1,012 位贡献者的 5,643 次提交，带来了大量新特性、性能优化与改进，相比 3.14 有显著提升。

- 🎉 **稳定版发布**：2026 年 10 月 9 日发布 Python 3.15.0 稳定版，是最新主要版本。
- 🧠 **解释器增强**：新增 `sentinel` 内置类型（PEP 661）、默认 UTF-8 编码（PEP 686）、推导式解包（PEP 798）、显式惰性导入（PEP 810）、`frozendict` 内置类型（PEP 814）及包启动配置文件（PEP 829）。
- ⚡ **JIT 编译器升级**：实验性 JIT 在 x86-64 Linux 上平均性能提升 7–8%，在 AArch64 macOS 上相比尾调用解释器提速 11–12%。
- 🛠️ **标准库与工具**：新增专用性能分析包（PEP 799）与高频统计采样分析器 Tachyon，并增加更多颜色支持。
- 🧩 **类型系统新特性**：支持带类型化额外项的 `TypedDict`（PEP 728）、`TypeForm` 类型形式注解（PEP 747）及类型系统中的不相交基类（PEP 800）。
- 🔌 **C API 改进**：新增 `PyBytesWriter`（PEP 782）、终结保护（PEP 788），并为自由线程构建提供稳定 ABI（PEP 803、820、793）。
- 🏗️ **构建与发布变更**：默认启用帧指针（PEP 831）以增强系统可观测性；Windows 64 位二进制改用尾调用解释器；macOS 二进制默认安装自由线程支持。
- ⚠️ **macOS 27.0 警告**：IDLE 或 tkinter 图形应用在打开对话框时可能卡死，建议推迟升级 macOS 27.0 或关注 issue #158053。
- 🎮 **趣味彩蛋**：Barry Warsaw 推出 TUI 文字冒险游戏 "whatsnewt"，含 18 个基于 3.15 真实特性的谜题，可通过 `uvx --python 3.15 whatsnewt` 运行。
- 🙏 **致谢与支持**：感谢所有志愿者、Georgi Ker 与 Marie Nordin 设计的 3.15 标志，以及 Sovereign Tech Agency 对发布经理 Hugo van Kemenade 的资助。
- 📦 **下载资源**：提供 macOS 安装包、Windows 安装管理器、源码 tarball 以及 Android、iOS、Windows 多平台安装包与嵌入式包。

---

### [](https://www.meetup.com/pydatachi/events/316886060/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Quantitative Trading with Python for Retail Investors, Thu, Oct 22, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydatachi/events/316886060/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

该活动由 PyData Chicago 主办，聚焦面向散户投资者的 Python 量化交易，采用线上线下混合形式，介绍如何用 Python 自动化策略、研究金融市场因果关系并进行绩效统计评估，同时由 AlphaSense 等提供赞助与场地支持。

- 🐍 主题：Quantitative Trading with Python for Retail Investors，面向散户投资者的 Python 量化交易。
- 🏢 主办：PyData Chicago，主持人 Justin S. 及另外 3 人。
- 📅 时间：10 月 22 日周四 18:00–20:00 CDT；报名截止 10 月 20 日周二 23:59。
- 🧠 内容：尽管 AI 是热门方向，但简单、暴力式 Python 编程与严谨分析仍有用，可用于构建自动化交易策略。
- 🎯 收获：学习构建工具、代码和思维框架，理解金融因果研究，并掌握金融市场、交易与统计评估基础。
- 💻 线上参与：Zoom 会议 ID 893 7923 0295，密码 5t5WYn，链接为 https://iit-edu.zoom.us/j/89379230295?pwd=NdETyE5sdYuSrvsrBZXSBFkUESBVkg.1。
- 📍 线下地点：200 N. LaSalle Street, Suite 1100, Chicago, IL 60601；需提前 RSVP 并提供姓名，到场出示身份证件，前往 11 楼。
- 🍕 赞助：AlphaSense 提供会议场地、披萨和软饮；W W Grainger、UIC、IIT 也提供场地或资助。
- 🏦 AlphaSense：AI 驱动的市场情报与搜索平台，服务超 6000 家企业客户，2024 年收购 Tegus。
- 🏷️ 相关主题：AI/ML、数据科学、金融、开源。

---

### [](https://www.meetup.com/python-users-nigeria-meetup/events/316825700/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Python Lagos Meetup October 2026, Sat, Oct 24, 2026, 9:30 AM   | Meetup](https://www.meetup.com/python-users-nigeria-meetup/events/316825700/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

这是一场由 Michael J. 和 Python N. 主办的 Python Nigeria Meetup，将于 2026 年 10 月 24 日周六 9:30–15:00 GMT+1 在拉各斯 Yaba 的 Cafe One 举行，面向开发者、数据科学家、学生和 AI 爱好者，包含两场主题演讲、闪电演讲与线下交流。

- 📅 活动时间：2026 年 10 月 24 日（周六）9:30 AM–3:00 PM GMT+1
- 📍 活动地点：Cafe One Yaba，Commercial Ave, Sabo Yaba, Lagos, Nigeria
- 🤝 活动形式：线下聚会，学习、动手构建与 networking，会前可加入 event chat 交流
- 🎤 演讲 1：Beyond Vibe Coding: Building Production-Ready Applications with Amazon Kiro
- 👤 讲者：Abdulakeem Yusuf，AWS Community Builder & AWS User Group Lead, Ibadan
- 🤖 内容重点：从简单提示转向规格驱动开发，使用 Amazon Kiro 将高层提示转化为需求、架构设计与可执行代码
- ⚙️ 技术亮点：自主代理、基于属性的测试、agent hooks，用于验证正确性与自动化工程流程
- 🧠 演讲 2：Building Medical AI with Limited Compute: Lightweight Brain Tumour Segmentation with Python
- 👥 讲者：Ifeoluwa Oladeji、Juwon Adegite，Medical AI Laboratory (MAI Lab)
- 🧬 内容重点：资源受限环境下，使用 3D U-Net 和 BraTS-Africa MRI 数据集进行轻量级脑肿瘤分割
- 🐍 Python 工作流：从预处理、训练、评估到可视化，使用 PyTorch、MONAI、NiBabel、NumPy
- 🌍 经验分享：在非洲语境下构建医学 AI 的实践与教训，无需医学背景
- ⚡ 闪电演讲：有 5 分钟想分享的内容，可在 RSVP 时告知
- 🔗 相关主题：拉各斯活动、开源 Python、Python、开源、软件开发、医疗科技

---

### [](https://www.meetup.com/pydata-milano/events/316944679/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [AI Perspectives: How Humans Adapt and Language Models Work, Wed, Oct 21, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-milano/events/316944679/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

这是 PyData Milano 将于 2026 年 10 月 21 日（周三）18:30–21:00 在米兰 Shopfully 办公室举办的线下 AI 活动，主题为“AI Perspectives: How Humans Adapt and Language Models Work”，由 Emanuele R. 等 5 人主持，包含两场演讲与 Aperitivo 社交，名额有限，需及时更新 RSVP。

- 📅 时间：2026 年 10 月 21 日（周三）18:30–21:00 CEST
- 📍 地点：Shopfully，Via Giosuè Borsi 9, 20143 Milano MI, Italy
- 🎟️ 报名：名额有限，请保持 RSVP 更新，以便无法参加时释放名额给他人
- 💬 活动聊天：报名参加后可与其他参会者提前交流
- 🚪 18:30 开门与签到
- 🎤 19:00 演讲 1：From Owning Tasks to Owning Outcomes — Raffaele Bongo
- 🎤 19:45 演讲 2：Garden Path Sentences in LLMs — Luca Mattiazzi
- 🍕 20:30 由 Shopfully 提供的社交与 Aperitivo
- 🤖 演讲 1 要点：AI agents 改变工作方式；人类从执行任务转为监督 AI，但监督易疲劳且成为瓶颈；主张从监督者升级为编排者，以“系统产出的好结果”而非“单任务正确”衡量成功；讨论人类独特价值、责任归属、初级工作被代理取代后如何培养资深人才，以及可被人类拥有的 agent 系统设计支柱
- 🧠 演讲 2 要点：花园小径句（如“The old man the boat”）需要句法重分析；用机制可解释性比较 Gemma 3 1B/4B/12B/27B 的注意力模式与层级变化；关注哪些部分对句法重分析反应最强、随模型规模如何变化，以及 LLM 如何处理语言歧义
- 👤 讲者：Raffaele Bongo 是 Shopfully 高级 AI 工程师，擅长云上 ML 与数据管道；Luca Mattiazzi 是 Pillar AI 工程师，自 2016 年做开发，热爱数据可视化、机器学习与副项目
- 🚀 主办：PyData Milano，Emanuele R. 与另外 4 人

---

### [](https://www.meetup.com/pydata_seattle/events/316713322/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

**原文标题**: [Beyond Vibe Coding: Formal Verification for AI-Generated Software, Wed, Oct 21, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata_seattle/events/316713322/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-767-october-15-2026)

本次 PyData Seattle 线上活动由 DEBJYOTI P. 与 PyData-Seattle 主办，演讲者 Carl 将探讨如何用形式化验证提升 AI 生成代码的可信度：不只让 AI 写代码，还让它生成形式化规范，并用 Lean 对真实 Rust 项目 RangeSetBlaze 进行机器可检查的正确性证明，从而超越传统测试。

- 🎯 主题：从“氛围编程”走向形式化验证，核心问题是“AI 能否帮助我们证明它写的代码是正确的？”
- 🤖 AI 编码代理已能生成大量开源软件，但仅有看似合理的实现和通过的测试套件仍然不够。
- 🧩 核心工作流：AI 辅助完成“代码 → 规范 → 证明”，为生成代码建立机器可检查的正确性证明。
- 🦀 案例：将方法应用于开源 Rust 库 RangeSetBlaze，并使用 Lean 定理证明器与编程语言陈述和证明关键正确性属性。
- ✅ 与常规测试的区别：形式化验证不是检查一组示例，而是证明指定属性对所有相关输入都成立。
- 🌐 更广泛意义：思路与语言无关；随着 AI 生成软件和证明的能力增强，形式化验证可能变得更适用于日常软件开发。
- 🛠️ 分工变化：AI 可承担传统上困难且耗时的证明工程，开发者更专注于定义正确规范并审查最终保证。
- 🧭 分享将探讨：AI 辅助代码→规范→证明的实践、Lean 验证真实 Rust 软件、机器可检查证明超越单元与集成测试之处、AI 辅助形式化验证的适用与失效边界、形式证明/测试/代码审查如何互补，以及对 AI 时代软件工程的影响。
- 👤 讲者 Carl：PyData 社区长期成员，微软及微软研究院退休首席应用科学家，曾在 PyData 会议发表五次演讲，并在 2024 年 PyData Seattle 开源软件聚会做主题演讲。
- 📅 活动形式：PyData Seattle 线上活动，提供活动聊天，方便参会者会前交流与连接。

---

