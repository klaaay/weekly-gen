### [从零开始编写编码代理：更好的工具 | mathspp](https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Write a coding agent from first principles: better tools | mathspp](https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

本文介绍了如何从零开始构建一个编码代理，并重点改进了其工具集，通过集成 Anthropic 提供的文本编辑器和 Bash 工具，使代理更强大、更稳健。

- 📝 **集成 Anthropic 文本编辑器工具**：用 Anthropic 的 `str_replace_based_edit_tool` 替代自定义的 `read`、`write`、`replace`、`insert` 四个工具，该工具支持 `view`、`replace`、`create`、`insert` 四种命令，通过 `command` 字段区分操作。
- 🛠️ **实现文本编辑器各命令**：详细实现了 `create`（创建文件）、`str_replace`（字符串替换）、`view`（查看文件或目录内容，支持可选的 `view_range` 参数）、`insert`（在指定行插入文本）四个函数，并处理了边界情况（如文件已存在、替换文本出现次数、索引转换等）。
- 🔒 **添加安全限制**：通过 `only_within_cwd` 装饰器限制文件编辑只能在当前工作目录内；通过 `make_path_backup` 装饰器在编辑前自动创建带时间戳的备份，并注意装饰器顺序（先检查路径，再备份）。
- 💻 **集成 Anthropic Bash 工具**：用 Anthropic 的 `bash` 工具（类型 `bash_20250124`）替代自定义的 Bash 函数，实现持久化的 Bash 会话。
- 🧵 **实现持久化 Bash 会话**：创建 `BashSession` 类，使用 `subprocess.Popen` 启动 Bash 子进程，通过线程和队列实现异步输出读取，支持命令超时和优雅关闭。
- 📏 **截断大输出**：在 `BashSession` 中限制最大输出行数（如 1000 行），超出时截断并提示代理，避免 Token 问题。
- 🛡️ **增加 Bash 命令安全审批**：创建 `BashToolManager` 类，封装会话管理和安全逻辑，在运行命令前询问用户是否允许，支持“始终允许”、“仅本次允许”或“不允许”，并记录已批准的精确命令。
- 🚀 **后续改进方向**：建议实现响应流式输出、改善用户界面（如使用 `rich` 或 `textual`）、添加会话管理命令（重置上下文、切换模型、更改 Token 限制）、封装为 CLI 以支持子代理。

---

### [窥探 Reddit 反垃圾内部机制 Ʊ lyra 的史诗级博客](https://lyra.horse/blog/2026/06/reddit-spam-internals/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [A peek into Reddit's anti-spam internals Ʊ lyra's epic blog](https://lyra.horse/blog/2026/06/reddit-spam-internals/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

这篇文章深入剖析了 Reddit 反垃圾系统的内部运作机制，基于作者在 2021 年偶然发现的系统错误信息，并结合公开代码和工程博客进行了详细分析。

- 🔍 **意外泄露**：作者因 Reddit 系统错误，短暂看到了原本隐藏的垃圾信息移除原因，包括详细的用户和内容分析数据。
- 🤖 **反垃圾系统层次**：Reddit 使用多层系统，包括基于规则的 Spamurai、机器学习模型 Minsky、以及后续的 REV1/REV2 和 Snooron 系统。
- 📊 **Spamurai 详细分析**：该系统会输出大量信息，如 Perspective API 的垃圾评分、账户年龄、IP 组织、浏览器指纹（RHS/TLS）、语言偏好等，用于综合判断。
- 🧪 **Perspective API 漏洞**：Reddit 使用 Google 的 Perspective API 检测垃圾信息，但该 API 对文本修改极其敏感，可通过添加字符、使用西里尔字母等方式轻易绕过。
- 🚫 **域名与内容封禁**：系统会封禁特定域名（如 tumblr）、Google Analytics ID（通过爬取链接页面）、以及匹配正则表达式的字符串（如“torenteu”）。
- ⏳ **时间线演变**：从早期的 CRM114 训练式过滤，到 2016 年的 Spamurai/REV1，再到 2021 年的 Snooron 和 REV2，系统不断演进。
- 🛡️ **其他检测手段**：包括对 Pinterest 重定向、mega.nz 链接、自由子域名的封禁，以及对图片进行 OCR 识别（使用 Hive AI 和 Google Vision）。
- ⚠️ **历史与风险**：作者选择在 2026 年发布此信息，因为 Perspective API 即将关闭，且 LLM 已彻底改变垃圾信息攻防格局，旧信息不再危险。

---

### [PEP 814：添加不可变字典内置类型 — Victor Stinner 博客 3](https://vstinner.github.io/pep-814-add-frozendict-builtin-type.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [PEP 814: Add frozendict built-in type — Victor Stinner blog 3](https://vstinner.github.io/pep-814-add-frozendict-builtin-type.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

Victor Stinner 在 2025 年 11 月于里昂 Pycon France 观看了一场关于构建不可变字典（frozendict）的演讲，受此启发，他与 Donghee Na 共同撰写了 PEP 814，提议在 Python 3.15 中新增一个内置的 frozendict 类型。该提案于 2026 年 2 月获得指导委员会批准，并在 Python 3.15 alpha 7 版本中首次实现。frozendict 与现有 types.MappingProxyType 的主要区别在于，当所有值都是可哈希的时，frozendict 本身也是可哈希的。实现过程中修复了多个错误，包括哈希碰撞、垃圾回收器可见性以及递归字典的深拷贝问题。标准库中的多个模块（如 json、pickle、pprint 等）已更新以支持 frozendict。

- 📜 **PEP 814 提案**：受 2025 年 Pycon France 演讲启发，Victor Stinner 与 Donghee Na 提出在 Python 3.15 中增加内置的 frozendict 类型，并于 2026 年 2 月获得指导委员会批准。
- 🔧 **实现与共享代码**：frozendict 与 dict 共享大部分代码（约 93%），仅约 560 行（7%）为 frozendict 特有代码，基于 PyDictObject 结构并添加 ma_hash 成员。
- 🧪 **测试与修复**：Python 3.15 alpha 7 首次包含 frozendict 后，发现并修复了多个错误，如错误的`__init__`方法（允许修改不可变对象）、哈希碰撞问题、`repr`输出格式调整，以及垃圾回收器可见性问题。
- 🔗 **可哈希性**：frozendict 仅在所有值可哈希时才可哈希，与 tuple 类似；比较和哈希不依赖于插入顺序。
- 📦 **标准库集成**：`eval()`、`exec()`、`type()`、`str.maketrans()`以及多个模块（如 json、pickle、pprint、xml.etree.ElementTree）已更新以接受 frozendict；但 errno.errorcode 的转换因维护者反对而被拒绝。
- 🛠️ **C API 变更**：新增`PyAnyDict_Check()`、`PyFrozenDict_New()`等函数；读取字典的函数（如`PyDict_GetItemRef()`）接受 frozendict，而修改字典的函数（如`PyDict_SetItem()`）则拒绝 frozendict 并给出明确错误信息。
- 🧩 **特殊案例**：frozendict 本身不可变，但值仍可为可变对象（如列表）；递归 frozendict（包含自身）的深拷贝已修复。
- 🚀 **性能优化**：Donghee Na 针对自由线程进行了优化，如避免锁操作、使用非原子操作获取长度，并修改了字节码特化以支持 frozendict。
- 📚 **历史与替代方案**：回顾了 2012 年被拒绝的 PEP 416 和 2019 年未提交的 PEP 603（frozenmap）；Python 3.14 及更早版本可使用`types.MappingProxyType`或 PyPI 上的`frozendict`项目（如 frozendict、immutabledict）。
- 🔮 **未来方向**：讨论了 frozenset 和 frozendict 推导式语法、高效将 dict 转换为 frozendict 的 C API，以及字典常量折叠等后续想法。

---

### [你不应该信任可信发布](https://blog.yossarian.net/2026/07/07/You-shouldnt-trust-trusted-publishing?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [You shouldn't trust Trusted Publishing](https://blog.yossarian.net/2026/07/07/You-shouldnt-trust-trusted-publishing?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

概述摘要
这篇文章解释了“可信发布”（Trusted Publishing）是一种机器对机器的认证机制，用于建立 CI/CD 工作流与包索引之间的信任关系，但它并不代表包本身的可信度或质量。用户不应将其视为安全或质量的信号。

- 🤖 **可信发布是机器间的信任**：它涉及 CI/CD 平台与包索引之间的认证，而非人类用户的直接信任。
- 🔑 **解决长期凭证问题**：通过短期、最小范围的凭证替代易泄露的长期 API 令牌，提升安全性。
- ✅ **成功但非完美**：用户偏好减少手动管理凭证，但仍有数据模型复杂、需定制 OIDC 提供商等缺点。
- ❌ **不可用于判断包质量**：可信发布仅认证上传来源，不保证包的安全性或质量，任何人均可上传恶意软件。
- 🔍 **PyPI 避免误导**：界面不显示“绿色勾选”等信任标记，仅以“是/否”形式低调展示可信发布状态。
- ⚠️ **与证明无关**：证明（attestations）是独立概念，同样不直接代表用户信任，需额外验证身份。
- 📝 **始终可选**：可信发布是自愿功能，不会强制使用，用户仍可用其他方式上传。

---

### [如何使用 GitHub Actions 安全地发布到 PyPI](https://snarky.ca/how-to-publish-to-pypi-using-github-actions-securely/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [How to publish to PyPI using GitHub Actions securely](https://snarky.ca/how-to-publish-to-pypi-using-github-actions-securely/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

以下是对文章内容的总结：

本文介绍了如何安全地使用 GitHub Actions 将 Python 包发布到 PyPI，重点解决了近期工作流安全漏洞问题，并提供了三个关键步骤。

- 🔒 使用 zizmor 工具扫描并修复工作流安全问题，包括默认权限过宽、凭据泄露和未固定操作版本。
- 🛡️ 启用 Trusted Publishing，避免管理 API 令牌，并利用 GitHub 环境设置发布审批机制，防止意外或恶意触发。
- 📋 固定所有操作到提交哈希，并通过 Dependabot 设置冷却期（如 7 天）来安全更新，同时要求 SHA 固定以增强安全性。

---

### [AWS ECS 上的 Celery - 完整指南](https://jangiacomelli.com/blog/celery-on-aws-ecs/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Celery on AWS ECS - Complete Guide](https://jangiacomelli.com/blog/celery-on-aws-ecs/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

本文介绍了在 AWS ECS 上运行 Celery 时可能遇到的常见问题及解决方案，并提供了详细的配置和任务设计建议。

- 📋 **任务丢失问题**：因 ECS 的 SIGTERM 和 SIGKILL 机制，默认 Celery 设置（如 `task_acks_late=False`）会导致任务在中断时丢失。
- ⏳ **任务无法完成**：频繁部署或伸缩导致任务执行时间窗口不足，使任务反复中断且无法完成，最终堵塞队列。
- 🐢 **任务延迟**：默认预取（prefetch）5 个任务，导致任务被缓存，其他空闲 worker 无法及时处理，降低整体吞吐量。
- ⚠️ **软超时失效**：软超时异常在垃圾回收等场景下可能无法被捕获，导致任务继续执行而不中断。
- 🔁 **重复处理**：竞争消费者模式下，多个 worker 可能同时处理同一任务，导致重复操作（如数据库重复插入）。
- 🛠️ **基础设施建议**：推荐使用 Amazon MQ 的 RabbitMQ 作为消息代理，并采用 ECS Fargate 简化管理，每个队列对应一个 ECS 服务。
- ⚙️ **关键配置调整**：设置 `task_acks_late=True`、`task_reject_on_worker_lost=True`、`worker_prefetch_multiplier=1` 等，并启用指数重试和确认发布。
- 🧩 **任务设计技巧**：使用扇出（fan-out）将大任务拆分为小任务，或采用批处理（batching）分步执行，确保任务在 120 秒内完成。
- 🔒 **任务锁定机制**：通过 Redis 的 `setnx` 实现分布式锁，防止同一任务被多个 worker 并行处理，并设置重试机制确保至少执行一次。
- 📚 **总结**：生产环境中 Celery 配置需谨慎，通过调整设置、优化任务设计和添加锁机制，可有效避免常见问题。

---

### [使用 FastAPI 服务前端：实用指南](https://modernpython.io/serving-a-frontend-with-fastapi-a-practical-guide/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Serving a Frontend with FastAPI: A Practical Guide](https://modernpython.io/serving-a-frontend-with-fastapi-a-practical-guide/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

## 概述摘要
FastAPI 的 `app.frontend()` 功能允许开发者直接从后端服务静态前端应用，实现 API 和前端在同一服务中运行，简化部署流程。

- 🚀 **核心功能**：`app.frontend()` 可服务静态前端构建目录（如 React、Vue、Svelte 等），同时保持 API 路由优先级
- ⚡ **路由优先级**：FastAPI 路径操作优先于前端文件，确保 API 不会被前端路由覆盖
- 🔄 **SPA 支持**：通过 `fallback="index.html"` 参数处理客户端路由，如 `/dashboard` 直接返回 `index.html`
- 📁 **项目结构**：典型结构包含 `dist/` 目录（存放构建后的 HTML、CSS、JS）和 `app/` 目录（存放 FastAPI 代码）
- 🎯 **使用场景**：适合内部仪表盘、管理界面、原型或小型产品；不适合需要 SSR、CDN 或独立部署的大型项目
- 🛠️ **开发建议**：本地开发使用前端开发服务器（如 Vite），生产部署时由 FastAPI 服务构建后的静态文件
- 🔗 **前缀支持**：通过 `APIRouter` 和 `prefix` 参数可将前端服务在 `/admin` 等子路径下
- ⚠️ **注意事项**：服务静态构建输出而非 SSR；大文件应使用 CDN；前端构建工具需正确配置基础路径

---

### [从微分几何视角看哈密顿神经网络——Abscondita 博客](https://abscondita.com/blog/symplectic-sledgehammer-for-a-spring?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Hamiltonian Neural Networks from a Differential Geometry Perspective — Abscondita Blog](https://abscondita.com/blog/symplectic-sledgehammer-for-a-spring?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

以下是您提供的文章的中文摘要，遵循了指定的模板格式：

哈密顿神经网络（HNN）通过微分几何中的辛结构，从根本上解决了传统神经网络无法守恒能量的问题。文章从相空间的几何本质出发，解释了为何直接学习向量场的 MLP 必然导致能量漂移，而 HNN 通过强制学习一个标量能量函数并利用辛梯度（90 度旋转）来生成动力学，使得能量守恒成为架构的固有属性，而非学习目标。文章还通过诺特定理将守恒律与对称性联系起来，指出 HNN 的结构天然支持泛化。

- 🔬 **核心问题**：传统 MLP 直接学习向量场，其输出场不满足无散度条件，导致相空间面积不守恒，能量必然漂移。
- 🌀 **几何解法**：HNN 学习一个标量能量函数 \( H \)，并通过辛形式 \( \omega \) 将其微分 \( dH \) 旋转 90 度得到动力学 \( X_H \)，这保证了 \( \omega(X_H, X_H) = 0 \)，从而能量自动守恒。
- ⚙️ **架构优势**：HNN 只输出标量 \( H \)，其导数用于匹配训练数据中的斜率，而 \( H \) 本身是“潜在变量”从未被监督。这迫使网络学习一个闭合的 1-形式，即无散度场。
- 🔗 **对称性与泛化**：诺特定理将守恒律与对称性等价。在 HNN 中，对能量函数施加平移不变性（如仅依赖相对坐标），不仅能自动获得动量守恒，还能实现“训练一处，处处适用”的泛化能力，类似于 CNN 的权重共享。
- 💻 **实现极简**：HNN 的核心代码仅两行——计算能量函数的梯度，然后交换分量并添加负号（即 \( [dHdp, -dHdq] \)），完美体现了辛梯度。
- 📊 **实验验证**：在弹簧系统上，HNN 在 50 个周期后能量漂移仅 0.003%，而同等精度的 MLP 能量漂移高达 26.8%，相空间面积也大幅缩小。
- ⚠️ **局限性**：纯 HNN 假设系统无摩擦且能量守恒。对于耗散系统，需要扩展为端口 - 哈密顿或接触几何结构。

---

### [沙盒化 AI 代理](https://sajalsharma.com/posts/sandboxing-an-ai-agent/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Sandboxing an AI Agent](https://sajalsharma.com/posts/sandboxing-an-ai-agent/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

### 概述总结
本文探讨了 AI Agent 沙箱化的必要性、架构选择及底层技术，强调通过隔离环境来平衡 Agent 的自主性与安全性。

- 🤖 **自主性与风险并存**：Agent 的长期自主运行（如自动执行命令）带来了效率，但也使其易受恶意指令攻击，可能泄露数据或破坏系统。
- 🛡️ **沙箱的核心价值**：沙箱提供隔离、可丢弃的环境，实现**遏制**（防止数据泄露）、**并行**（避免资源冲突）、**可复现**（环境一致）、**资源管控**（限制 CPU/内存）和**低成本恢复**（丢弃损坏环境）。
- 🏗️ **两种架构模式**：**工具后端模式**（Agent 循环在本地，仅命令进入沙箱）适合轻量任务，密钥安全；**Agent 之家模式**（整个 Agent 在沙箱内运行）适合长期自主任务，边界更清晰。
- ⚙️ **底层隔离强度**：从弱到强分为**共享内核容器**（如 Docker，快速但风险高）、**软件二次内核**（如 gVisor，牺牲速度增强安全）、**独立虚拟机**（如 Firecracker，最强隔离但启动较慢）。
- 💰 **成本与性能**：沙箱启动耗时短（毫秒级），运行时开销对 Agent 任务影响小；按运行时间计费（如 Daytona）或按代码执行计费（如 Modal），单次任务成本仅几美分。
- 🔮 **未来方向**：沙箱将成为 Agent 栈的默认层，并可能向**持久化**发展（为每个 Agent 分配长期运行的计算机），带来新的安全与设计挑战。

---

### [Miles：用于大规模 LLM 强化学习后训练的 PyTorch 原生栈——PyTorch](https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Miles: A PyTorch-Native Stack for Large-Scale LLM RL Post-Training – PyTorch](https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

Miles 是 RadixArk 开源的 LLM 强化学习后训练框架，专为大规模分布式系统设计，整合 SGLang、Megatron-LM、Ray 和 PyTorch，提供可组合、可复现的 RL 训练方案。

- 🏗️ **核心设计哲学**：采用"小核心 + 多扩展点"架构，训练循环紧凑，通过 Python 模块自定义 rollout、奖励、损失函数等，无需分叉框架
- 🔄 **Ray 编排**：所有进程作为 Ray Actor 运行，支持 GPU 感知调度、分离/共置部署、异步执行模式，提供作业监控和故障恢复
- ⚡ **Megatron-LM 训练**：直接集成 Megatron 参数解析器、模型构建和并行检查点格式，通过模型规范支持 DeepSeek-V4 等新架构，无需维护长期分叉
- 🧩 **PyTorch 原生扩展**：模型组件为标准 torch.nn.Module，RL 算法通过 Python 模块定制，支持 BF16/FP8 等低精度管线，集成 PyTorch 分析器
- 🔗 **关键系统集成**：SGLang 负责高吞吐 rollout，Megatron-LM 处理分布式训练，Ray 协调集群，PyTorch 提供统一编程层
- ⚙️ **开箱即用功能**：rollout-训练集成、异步执行、NCCL/RDMA 权重同步、MoE 路由对齐、低精度支持、LoRA、容错与可观测性
- 🎯 **扩展点设计**：暴露 rollout 函数、奖励函数、损失函数、样本过滤器、训练钩子和模型规范，支持 RLHF、规则奖励、代码任务等多种工作流

---

### [GitHub - bradautomates/claude-video: 赋予 Claude 观看任何视频的能力。/watch 下载、提取帧、转录，并将所有内容交给 Claude 处理。](https://github.com/bradautomates/claude-video?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - bradautomates/claude-video: Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude. · GitHub](https://github.com/bradautomates/claude-video?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

该工具让 Claude 能够“观看”视频内容，通过下载、提取帧和转录，实现基于视频画面的智能分析。

- 🎬 **核心功能**：粘贴视频链接或本地路径，Claude 即可提取字幕、下载必要内容、抽取帧画面（场景感知或关键帧），并生成带时间戳的转录文本，真正“看到”和“听到”视频内容。
- 📊 **应用场景**：分析他人内容（如视频钩子、广告创意）、诊断屏幕录制中的 Bug、总结长视频、过滤营销话术提取干货、将播放列表转化为可搜索笔记。
- ⚙️ **工作原理**：使用 yt-dlp 优先获取字幕，必要时通过 Whisper（Groq 或 OpenAI）转录音频；ffmpeg 按细节模式抽取帧（高效/平衡/烧令牌），帧与转录文本一同交给 Claude 处理。
- 🖼️ **帧预算策略**：根据视频时长自动调整帧数（≤30 秒约 30 帧，>10 分钟上限 100 帧），支持时间范围聚焦（--start/--end）以获取更密集的帧采样，避免浪费令牌。
- 🔄 **帧去重机制**：默认对抽取的帧进行相似度检测（16×16 灰度缩略图比较），丢弃视觉上重复的帧（阈值 2.0），确保预算用于不同内容。
- 🎛️ **细节模式对比**：transcript（仅字幕，最快）、efficient（关键帧，约 50 帧）、balanced（场景变化，约 100 帧）、token-burner（无上限场景帧），在速度和令牌消耗间提供选择。
- 🔧 **安装方式**：支持 Claude Code（插件市场）、Codex/Cursor 等（npx skills）、claude.ai 网页（下载.skill 文件）及手动开发者安装。
- 🚀 **首次运行**：自动检查 ffmpeg/yt-dlp 依赖，macOS 自动安装，其他系统打印命令；可配置 Groq 或 OpenAI API 密钥用于 Whisper 转录。
- 📝 **使用参数**：支持--detail（细节模式）、--start/--end（时间范围）、--timestamps（特定时间点帧）、--max-frames（帧数上限）、--resolution（分辨率）、--fps（帧率）等灵活选项。
- ⚠️ **限制说明**：长视频在默认模式下覆盖稀疏，建议使用时间聚焦或 token-burner 模式；细节模式是主要调节旋钮，默认 balanced 平衡速度和效果。
- 🏗️ **项目结构**：技能模块化设计（skills/watch/），包含 SKILL.md 合约和脚本目录（watch.py、download.py、frames.py 等），支持测试套件和自动构建发布。
- 📜 **开源许可**：MIT 协议，基于 yt-dlp、ffmpeg 和 Claude 多模态 Read 工具构建，由 Brad Bonanno 开发。

---

### [GitHub - can1357/pon：Python 3.14，编译至底层——基于 Rust 的 JIT 与 AoT 原生编译器及运行时。采用 Cranelift 后端、ruff 解析器、Green Tea GC，实现与 CPython 的字节级精确差分测试。](https://github.com/can1357/pon?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - can1357/pon: Python 3.14, compiled to metal — JIT & AoT native compiler and runtime in Rust. Cranelift backend, ruff parser, Green Tea GC, byte-exact differential testing against CPython. · GitHub](https://github.com/can1357/pon?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

PON 是一个用 Rust 编写的 Python 3.14 JIT 和 AoT 原生编译器与运行时，没有解释器和字节码，通过 Cranelift 后端将代码编译为机器码，并使用 Green Tea 垃圾回收器管理内存。

- 🚀 **核心架构**: 使用 ruff 解析器解析 Python 3.14，降级为统一 IR，再通过 Cranelift 编译为机器码，支持 JIT（pon run）和 AoT（pon build）两种模式
- 🎯 **正确性保障**: 通过字节精确的差分测试框架与 CPython v3.14.0 对比，确保输出完全一致，并设有 CI 回归检查
- 🗑️ **内存管理**: 使用 Green Tea 垃圾回收器替代引用计数，所有 Python 对象由 GC 统一管理
- ⚡ **分层编译**: 基线 JIT（tier-0）全装箱编译，优化 JIT（tier-1）加入类型反馈、内联缓存、OSR 和后台编译
- 📦 **包管理器**: 内置 uv 风格的包管理器，支持 PyPI 索引、wheel/sdist 安装、可编辑安装和 VCS 需求
- 🧪 **测试套件**: 包含 CPython 测试套件、差分模糊测试、AoT 一致性测试和线程压力测试，所有通过模块被锁定为基准
- 📊 **当前状态**: 209 个差分测试模块通过 JIT，172 个通过 AoT，正在积极开发 CPython 完整测试套件和性能优化
- 🔧 **技术栈**: 使用 Rust 2024 版、nightly 工具链、ruff 0.14.0 解析器、Cranelift 0.133.1 后端

---

### [GitHub - tiliondev/fortress: 隐形 Chromium 引擎，只需改动一行代码即可阻止爬虫和浏览器代理被屏蔽。](https://github.com/tiliondev/fortress?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - tiliondev/fortress: Stealth Chromium engine that stops scrapers and browser agents from getting blocked, with one line of code change. · GitHub](https://github.com/tiliondev/fortress?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

Fortress 是一个开源的隐形 Chromium 引擎，通过在 C++ 层面修正浏览器指纹，让爬虫和自动化代理难以被检测和拦截。

- 🛡️ **核心原理**：在 Chromium 的 C++ 代码中直接修改 30 多个指纹表面（如 Canvas、WebGL、音频、字体等），而非通过 JavaScript 补丁，从而避免被检测工具识破。
- 🎯 **无缝集成**：作为标准浏览器二进制文件运行，暴露 CDP 端点，可无缝替换 Playwright、Puppeteer 等现有自动化框架，无需修改代码。
- ✅ **通过检测**：已通过 CreepJS、Sannysoft、BrowserScan 和 Cloudflare Turnstile 等主流反爬工具的检测，呈现为普通 Chrome 浏览器。
- 🔧 **可审计与可复现**：所有修改以 34 个小型、单一用途的 C++ 补丁形式公开，可从源码完整构建，确保透明度和可信度。
- 🖥️ **可配置身份**：通过 `--uxr-*` 命令行开关可自定义平台、GPU、时区、语言等指纹特征，支持生成一致的 Windows 身份。
- 🤖 **AI 代理支持**：提供 Fortress MCP 服务器，为 Claude、Cursor 等 AI 代理提供 29 个隐身浏览工具，包括获取受保护页面、提取结构化数据等。
- 📦 **多平台分发**：支持 Linux x64、Windows x64 原生二进制，以及 Docker 镜像，通过 pip、npm 或便携包安装。
- 📈 **持续更新**：每月跟随 Chromium 上游版本更新，并重新运行检测套件，确保对最新检测技术的有效性。

---

### [GitHub - bitwire-it/ipblocklist: 包含恶意 IP 的 IP 列表 - 每 2 小时更新 · GitHub](https://github.com/bitwire-it/ipblocklist?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - bitwire-it/ipblocklist: IP lists full of bad IPs - Updated every 2H · GitHub](https://github.com/bitwire-it/ipblocklist?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

该存储库提供聚合的 IP 封禁列表，每 2 小时更新一次，用于入站和出站流量防护，并排除公共 DNS 解析器以避免误封。

- 🛡️ **入站封禁列表 (inbound.txt)**：包含有不良声誉的 IP/网络，用于保护面向公众的服务器，阻止来自这些源的恶意连接（如垃圾邮件、扫描、暴力破解等）。
- ☢️ **出站封禁列表 (outbound.txt)**：包含已知恶意目标 IP（如 C2 服务器、僵尸网络控制器），用于防止内部受感染设备与恶意服务器通信。
- 🔄 **自动更新机制**：通过 GitHub Actions 工作流每 2 小时自动更新列表，支持自托管运行器以加快处理速度。
- 📜 **许可证与数据来源**：代码采用 MIT 许可证，聚合数据采用 CC BY-NC-SA 4.0 许可证（禁止商业用途），数据来自 Spamhaus、AlienVault OTX 等多个安全源。
- 🖥️ **使用方式**：标准文本格式，可集成到防火墙（如 pfSense、OPNsense、FortiGate）的 WAN IN/INPUT或LAN OUT/OUTPUT链中，执行DROP或LOG操作。

---

### [GitHub - google-antigravity/antigravity-sdk-python: 一个用于构建 AI 代理的 Python 库，充分利用 Google Antigravity 的全部能力。](https://github.com/google-antigravity/antigravity-sdk-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - google-antigravity/antigravity-sdk-python: A Python library for building AI agents that leverage the full power of Google Antigravity. · GitHub](https://github.com/google-antigravity/antigravity-sdk-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

Google Antigravity SDK 是一个用于构建 AI 代理的 Python 开发工具包，基于 Antigravity 和 Gemini 技术，提供安全、可扩展且状态化的基础设施层。

- 🤖 **核心功能**：提供高级 Agent 类，简化 AI 代理的创建、生命周期管理和工具集成
- 📦 **安装方式**：通过 PyPI 安装`pip install google-antigravity`，包含编译好的运行时二进制文件
- 🚀 **快速上手**：支持 Gemini API 和 Vertex AI 两种后端配置，提供丰富的示例代码
- 💬 **流式响应**：支持实时流式输出，包括文本、思考过程和工具调用事件
- 🛠️ **工具集成**：支持自定义 Python 函数作为工具、MCP 服务器集成，以及声明式策略系统控制代理行为
- 📁 **多模态输入**：支持图片、视频、音频和文档等多种文件类型的输入
- 🔄 **交互模式**：提供交互式循环和高级会话管理功能
- 🏗️ **三层架构**：简化层（Agent）、会话层（Conversation）和适配层（Connection），层次清晰
- ⚡ **触发器系统**：支持后台任务和外部事件驱动的消息推送
- 📜 **开源许可**：采用 Apache License 2.0 开源协议

---

### [GitHub - microsoft/skills-for-fabric: 一套技能和 MCP 系统，使 CLI、VSCode、Claude 用户能够操作 Microsoft Fabric](https://github.com/microsoft/skills-for-fabric?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - microsoft/skills-for-fabric: A collection of skills and MCP systems to enable users of CLI, VSCode, Claude to operate over Microsoft Fabric · GitHub](https://github.com/microsoft/skills-for-fabric?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

Microsoft Fabric Skills 是微软提供的一组可复用的 AI 助手指令，帮助用户通过 GitHub Copilot CLI 等工具高效操作 Microsoft Fabric 平台。

- 📦 提供多种技能包：`fabric-skills`（完整包）、`fabric-authoring`（创作）、`fabric-consumption`（消费）、`fabric-operations`（运维）和 `powerbi-authoring`（Power BI 创作）
- ⚙️ 支持通过 GitHub Copilot CLI 安装，也可通过 `/plugin install` 命令安装完整或筛选后的技能包
- 🧠 包含丰富的示例提示词，如“设计 NYC 出租车 medallion 架构”、“分析 PDF 报告”等，方便快速上手
- 🔐 大多数操作需要 Azure 认证，需先执行 `az login` 获取访问令牌
- 🛠️ 提供 MCP 服务器配置，支持实时工具访问数据源和 API
- 🖥️ 兼容多种 AI 编码工具（Claude Code、Cursor、Windsurf、Codex 等），通过根目录配置文件自动识别
- 📝 项目采用 MIT 许可证，提供详细的变更日志（CHANGELOG.md）和安全报告渠道

---

### [GitHub - OthmanAdi/planning-with-files: 基于文件的持久化规划方案，适用于 AI 编码代理与长期运行的代理任务。防崩溃的 Markdown 计划，可抵御上下文丢失与/clear 指令，配备确定性完成门控机制及多代理共享磁盘状态。Manus 风格。兼容 Claude Code、Codex CLI、Cursor、Kiro、OpenCode 及 60 余种代理（基于 SKILL.md 标准）。](https://github.com/OthmanAdi/planning-with-files?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - OthmanAdi/planning-with-files: Persistent file-based planning for AI coding agents and long-running agentic tasks. Crash-proof markdown plans that survive context loss and /clear, plus a deterministic completion gate and multi-agent shared state on disk. Manus-style. Works with Claude Code, Codex CLI, Cursor, Kiro, OpenCode and 60+ agents via the SKILL.md standard. · GitHub](https://github.com/OthmanAdi/planning-with-files?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

planning-with-files 是一个为 AI 编程代理设计的持久化文件规划技能，通过磁盘上的任务计划、发现和进度文件，解决上下文丢失和崩溃问题，支持 60 多种代理。

- 📋 核心三文件模式：使用 `task_plan.md`、`findings.md` 和 `progress.md` 持久化存储任务计划、发现和进度，防止上下文丢失和崩溃。
- 🚀 广泛兼容性：支持 Claude Code、Codex CLI、Cursor、GitHub Copilot 等 60 多种 AI 代理，通过 SKILL.md 标准安装。
- 🧩 高级模式：v3.0.0 引入自主模式和门控模式，支持长时间运行代理，带有完成门控和结构化运行账本。
- 🛠️ 丰富的 IDE 集成：为 18 多个平台提供专用钩子配置，自动重新读取计划、提醒更新进度、验证完成。
- 🌍 多语言支持：提供阿拉伯语、德语、西班牙语、简体中文和繁体中文等 5 种语言变体。
- 📊 基准测试：在评估中达到 96.7% 的通过率（30 个断言中通过 29 个），显著优于无技能的情况。
- 🔒 安全与恢复：支持会话恢复、哈希认证、并行计划隔离和 Windows 兼容性。
- 📈 社区扩展：社区贡献了多个分支和扩展，如多项目支持、多级任务编排和众筹功能。
- 📝 简单安装：通过 `npx skills add` 一键安装，或为 Claude Code 使用 `/plugin install`。

---

### [GitHub - IBM/mcp-context-forge：一个AI网关、注册表和代理，位于任何MCP、A2A或REST/gRPC API 之前，提供统一端点，具备集中发现、防护和管理功能。优化智能体与工具调用，并支持插件。](https://github.com/IBM/mcp-context-forge?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - IBM/mcp-context-forge: An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins. · GitHub](https://github.com/IBM/mcp-context-forge?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

ContextForge 是一个开源 AI 网关、注册表和代理，用于联邦 MCP、A2A 和 REST/gRPC API，提供统一端点、集中治理、发现和可观测性。

- 🔗 **统一网关**：联邦 MCP、A2A 和 REST/gRPC API，支持协议转换（如 gRPC 转 MCP），提供单一统一接口。
- 🛡️ **集中治理**：内置认证（JWT、OAuth）、速率限制、重试、内容安全策略和 SSRF 保护。
- 🔍 **可观测性**：集成 OpenTelemetry，支持 Phoenix、Jaeger、Zipkin 等后端，实现分布式追踪和 LLM 指标监控。
- 🧩 **插件扩展**：40+ 插件，支持额外传输、协议和集成，灵活扩展功能。
- 🚀 **快速部署**：支持 PyPI、Docker、Docker Compose、Helm (Kubernetes) 和 VS Code Dev Container，30 秒内启动完整堆栈。
- 🖥️ **管理界面**：基于 HTMX + Alpine.js 的 Admin UI，支持实时日志查看、配置管理和 API 令牌生成。
- 📚 **丰富文档**：提供 5 分钟快速入门、完整配置参考、API 文档和故障排除指南。
- 🤝 **社区驱动**：Apache 2.0 许可，核心作者为 Mihai Criveti，拥有 4.1k Star 和 744 Fork。

---

### [GitHub - google-research/tabfm · GitHub](https://github.com/google-research/tabfm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - google-research/tabfm · GitHub](https://github.com/google-research/tabfm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

TabFM 是一个与 scikit-learn 兼容的表格基础模型，支持零样本分类和回归，无需训练即可通过上下文学习进行预测。

- 🧠 **零样本学习**：TabFM 无需在数据集上训练参数，而是利用上下文学习，将训练数据作为“上下文”直接对新样本进行预测。
- ⚙️ **安装灵活**：支持 JAX（CPU/GPU）和 PyTorch（CPU/GPU）后端，用户可根据需求选择安装方式。
- 📦 **预训练权重**：提供 TabFM v1.0.0 版本的预训练权重，库会自动下载和加载。
- 🚀 **快速上手**：通过 `TabFMClassifier` 和 `TabFMRegressor` 实现分类和回归，代码示例清晰，支持混合数值和类别特征。
- 📁 **示例与测试**：包含分类和回归示例脚本（`examples/`），以及单元测试，可通过 Python 的 `unittest` 或 Bazel 运行。
- 📊 **评估结果**：模型评估结果存放在 `results/` 目录中。
- 🛠️ **依赖要求**：需要 Python >= 3.11、Hugging Face Hub，以及 JAX 或 PyTorch 后端。
- 📜 **开源许可**：基于 Apache-2.0 许可证，非 Google 官方产品。

---

### [GitHub - NVlabs/ProtoMotions: ProtoMotions 是一个用于训练物理模拟数字人和人形机器人的 GPU 加速仿真与学习框架。](https://github.com/NVlabs/ProtoMotions?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [GitHub - NVlabs/ProtoMotions: ProtoMotions is a GPU-accelerated simulation and learning framework for training physically simulated digital humans and humanoid robots. · GitHub](https://github.com/NVlabs/ProtoMotions?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

ProtoMotions3 是一个基于 GPU 加速的仿真与学习框架，专为训练物理模拟的数字人类和人形机器人设计，提供快速原型开发平台，支持动画、机器人和强化学习领域的研究。

- 🏃 **大规模运动学习**：可在 12 小时内用 4 块 A100 GPU 从 AMASS 数据集（40+ 小时）训练完整物理角色运动技能。
- 📈 **可扩展多 GPU 训练**：支持每个 GPU 处理部分运动数据，已用 24 块 A100 训练 BONES 数据集（每 GPU 13K 动作）。
- 🔄 **一键重定向**：通过 PyRoki 优化器，一键将 AMASS 数据集重定向到任意机器人。
- 🤖 **训练任意机器人**：仅需更改命令行参数（如`--robot-name=smpl`→`--robot-name=h1_2`），12 小时内让机器人学习 AMASS 运动技能。
- 🔬 **Sim2Sim 测试**：一键切换物理引擎（IsaacGym→Newton→MuJoCo），测试机器人控制策略。
- 🤖 **从仿真到现实**：训练通用跟踪策略后零样本部署到 Unitree G1 人形机器人，输出单一 ONNX 模型。
- 🎨 **高保真渲染**：在 IsaacSim 5.0+ 中加载高斯泼溅背景，测试策略视觉效果。
- 🎬 **Kimodo 运动创作**：通过文本生成运动，训练物理策略并直接部署到真实硬件。
- 🏗️ **程序化场景生成**：利用强化学习适应增强场景，用于可扩展合成数据生成。
- 🎭 **生成式策略**：训练如 MaskedMimic 的生成式策略，自主选择动作完成任务。
- ⛰️ **地形导航**：训练机器人穿越复杂地形。
- 🎯 **自定义环境**：通过模块化组件构建新任务（如转向任务），无需整体环境类。
- 🧪 **新 RL 算法**：约 50 行代码实现新强化学习算法（如 ADD），利用模块化设计。
- 🔧 **自定义模拟器**：实现 API 接口，支持集成新模拟器（如 Genesis）。
- 🤖 **添加自定义机器人**：通过添加 MuJoCo 规范文件和配置，快速注册新机器人。

---

### [媒介](https://blog.jupyter.org/jupyterlab-4-6-and-notebook-7-6-are-out-dd84e1e919f2?gi=ffe690f2584e&utm_campaign=python-weekly-issue-753-july-9-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

**原文标题**: [Medium](https://blog.jupyter.org/jupyterlab-4-6-and-notebook-7-6-are-out-dd84e1e919f2?gi=ffe690f2584e&utm_campaign=python-weekly-issue-753-july-9-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

JupyterLab 4.6 和 Notebook 7.6 正式发布，带来多项界面定制、文件浏览器、调试器、键盘导航和无障碍改进，以及性能优化和扩展构建加速。

- 🚀 **JupyterLab 4.6 新特性**：新增界面定制选项（如活动栏位置可调）、改进的文件浏览器（含“创建日期”列、可编辑面包屑路径、终端打开功能）、增强的调试器（内核源过滤、浮动覆盖层），以及便捷的最近编辑单元格跳转功能。
- 📝 **Notebook 7.6 同步更新**：包含 JupyterLab 的所有修复与增强，并新增 Scratchpad 控制台（与笔记本共享内核）、关闭笔记本时的确认对话框，以及改进的自动补全和标签页宽度冻结。
- 🔧 **导航与快捷键优化**：新增“选择上一个/下一个最后修改的单元格”命令；Ctrl+B（Mac 为 Cmd+B）在 Markdown 单元格中加粗文本；Ctrl+H 用于查找替换；Ctrl+Y 作为重做快捷键（Windows/Linux）；避免数字键意外转换代码单元格为 Markdown。
- ♿ **键盘导航与无障碍改进**：终端不再锁定键盘焦点；控制台和文件浏览器面包屑导航修复；命令面板关闭后正确恢复焦点；屏幕阅读器在启动器和笔记本中的表现提升；工具栏按钮通过 `aria-pressed` 属性正确反映状态。
- 🌐 **国际化与终端增强**：可直接在 JupyterLab 内安装语言包；终端中 Shift+Enter 插入换行而不执行；内联补全支持语法高亮和多光标显示。
- 🎨 **界面布局与性能**：侧边栏面板可跨区域移动；标签页支持四方向拆分；面板缩放不影响其他面板；面板调整大小更流畅（可禁用优化）；构建速度因迁移至 Rspack 提升约 5 倍。
- 🐛 **大量修复与贡献**：此版本包含 68 项新功能、97 项 bug 修复和 38 项文档改进，共有 95 位贡献者参与，并感谢所有测试和反馈人员。

---

### [Django 安全版本发布：6.0.7 和 5.2.16 | 博客 | Django](https://www.djangoproject.com/weblog/2026/jul/07/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Django security releases issued: 6.0.7 and 5.2.16 | Weblog | Django](https://www.djangoproject.com/weblog/2026/jul/07/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

Django 发布了安全更新版本 6.0.7 和 5.2.16，修复了三个低严重性安全漏洞，建议所有用户尽快升级。

- 🔒 CVE-2026-48588：修复了缓存中间件在请求携带无关 Cookie 时，可能错误缓存设置会话 Cookie 的响应，导致私有数据泄露的问题
- 🗺️ CVE-2026-53877：修复了 GDALRaster 在处理字节对象时，vsi_buffer 属性可能过度读取堆内存约 32 字节，导致信息泄露或段错误的问题
- 📧 CVE-2026-53878：修复了 DomainNameValidator 接受域名中的换行符，可能被用于 HTTP 响应头注入攻击的问题（Django 自身 HttpResponse 不受影响）
- 🛠️ 受影响版本包括 Django main、6.1 beta、6.0 和 5.2 分支，已发布 Django 6.0.7 和 5.2.16 修复版本
- 📥 补丁可从各分支的变更集获取，建议用户尽快升级

---

### [PyData 柏林 2026 年 7 月聚会，2026 年 7 月 15 日星期三，下午 6:30 | Meetup](https://www.meetup.com/pydata-berlin/events/315577625/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [PyData Berlin 2026 July Meetup, Wed, Jul 15, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-berlin/events/315577625/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

PyData Berlin 2026 年 7 月聚会将于 7 月 15 日 18:30 至 21:30 在柏林 Design Offices Berlin Humboldthafen 举行，提供食物和饮品，19:00 开始演讲并关闭入场。

- 🗓️ **活动时间与地点**：7 月 15 日 18:30-21:30，柏林 Design Offices Berlin Humboldthafen，19:00 后禁止入场。
- 🍕 **提供餐饮**：活动开始后提供食物和饮品，鼓励准时到达。
- 🚫 **名额有限**：如无法参加，请取消预约以便他人加入。
- 🎤 **演讲 1：分布式计算**：Torsten Kilias 讲解如何用 Exasol UDFs 实现 LLM 编码代理的高性能分布式计算。
- 📊 **演讲 2：因果思维**：Dr. Maryam Ramezani-bartsch 介绍因果分析在客户归因、细分和增长中的应用，强调增量影响。
- ⚡ **闪电演讲**：两场主演讲之间安排 2-3 个 3-5 分钟的闪电演讲，欢迎报名。
- 🤝 **行为准则**：遵守 NumFOCUS 准则，保持专业、友善，禁止骚扰和不当言论。
- 🏢 **主办方**：由 Exasol 赞助，PyData Berlin 组织。

---

### [使用编码代理构建——发布 Python Streamlit 仪表盘，2026 年 7 月 14 日星期二下午 6:30 | Meetup](https://www.meetup.com/pyladiesams/events/315542536/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Building with Coding Agents — Ship a Python Streamlit dashboard, Tue, Jul 14, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pyladiesams/events/315542536/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

本次工作坊将教你如何高效使用编码 AI 代理，通过构建一个 Streamlit 仪表盘来掌握提升生产力的元技能。

- 🎯 **核心目标**：学习与编码 AI 代理高效协作的元技能，将其转化为真正的生产力工具。
- 📝 **关键技能**：涵盖编写项目上下文、编码前规划、设置防护栏、高效管理上下文、节省 Token 和成本、以及批判性审查代理输出。
- 🛠️ **实践环节**：使用提供的数据集，用你偏好的编码代理构建一个小型 Streamlit 仪表盘。
- 🚀 **进阶策略**：介绍技能、子代理、MCP、自定义斜杠命令、带验证器的代理循环、多代理编排、跨会话记忆、长期运行代理和评估等高级技巧。
- 🎤 **演讲嘉宾**：Felicity Fan，数据科学家，专注于应用机器学习和 MLOps，分享如何有效使用 AI 构建工作流。
- 📅 **活动信息**：由 PyLadies Amsterdam 主办，Giulia 和 Una G.主持，线上活动。

---

### [ClePy 七月聚会 - PyOhio 预告！，2026 年 7 月 14 日，星期二，下午 6:00 | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/315459047/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [ClePy July Meetup - PyOhio Preview!, Tue, Jul 14, 2026, 6:00 PM   | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/315459047/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

ClePy 七月聚会 - PyOhio 预览活动将于 7 月 14 日晚在克利夫兰 Happy Dog 举办，包含两场 PyOhio 2026 演讲预览，旨在帮助演讲者练习并收集反馈。

- 🐍 **活动概览**：ClePy 七月聚会由 Eddie C.和 Anurag S.主持，在 Happy Dog 地下室举办，时间 18:00-20:00，包含社交、演讲和清理环节。
- 🎤 **演讲预览**：两场 PyOhio 2026 演讲预览，为演讲者提供练习和反馈机会，参会者可提前了解内容。
- 🤖 **Talk 1：模型本地正常，生产环境为何出错？** Dinky Mishra 讲解 ML 模型和 Python 应用在生产中失败的五大常见原因，如训练 - 服务偏差、环境不匹配等，并提供诊断和修复方法。
- 💊 **Talk 2：用 Python 加速临床试验分析** James Austrow 展示如何通过算法优化，将医学统计测试“胜率比”速度提升 20-50 倍，甚至超 100 倍，强调纯 Python 可超越优化 C++。
- 📅 **PyOhio 2026 信息**：7 月 25-26 日在克利夫兰州立大学学生中心举行，免费注册，链接已提供。
- ✅ **参会提醒**：若无法参加请更改 RSVP 状态，以便统计人数；欢迎通过 Meetup 或 Slack 频道申请演讲。
- 🏢 **赞助致谢**：感谢 Python 软件基金会和 Happy Dog 的支持。

---

### [使用 Python AST 进行上下文驱动的代码分析 | 2026 年 7 月 16 日周四下午 6:00 | Meetup](https://www.meetup.com/python-stlouis/events/315551680/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [Context Driven Code Analysis with Python AST, Thu, Jul 16, 2026, 6:00 PM   | Meetup](https://www.meetup.com/python-stlouis/events/315551680/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

本次演讲探讨了如何利用 Python 的抽象语法树（AST）结合上下文信息进行代码分析，以提升静态分析的准确性和深度。

- 📅 活动时间为 7 月 16 日（周四）晚 6 点至 8 点，地点在圣路易斯的 TechArtista CWE。
- 🎤 演讲主题为“基于上下文的 Python AST 代码分析”，由 PySTL 组织主办。
- 🧠 Python AST 能将源代码转化为结构化表示，便于基于语法而非原始文本进行分析。
- 🔍 结合上下文（如导入、作用域、装饰器、类、函数调用和框架约定）可区分相似代码。
- 🛡️ 实际案例展示 AST 如何用于识别安全风险、理解代码行为以及改进静态分析。
- ⏰ 活动流程包括 6:00-6:45 的社交环节、6:45-7:45 的主题演讲和 7:45-8:00 的告别。
- 🤝 赞助商为 Manning Publications，PySTL 是 Python 软件基金会的社区合作伙伴。
- 👥 合作伙伴包括 St. Louis Code and Coffee、Bourbon Friday 和 PyData STL。

---

### [修剪后的大型语言模型实际能节省多少能量？，2026 年 7 月 13 日，星期一，下午 5:30 | 聚会](https://www.meetup.com/pydata-st-louis/events/315239846/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [How Much Energy Do Pruned LLMs Actually Save?, Mon, Jul 13, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-st-louis/events/315239846/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

概述总结：本次活动由 PyData St. Louis 主办，探讨修剪大型语言模型（LLM）对能源消耗的实际影响，包括修剪原理、能效权衡及案例研究。

- 🧠 活动主题：探讨修剪 LLM 是否能真正节省能源，并分析其计算成本与能耗挑战。
- 📅 时间地点：7 月 13 日周一下午 5:30-7:30（CDT），位于 St. Louis 的 Spark Coworking。
- 🍕 活动流程：5:30 开始披萨与社交，6:15 开始演讲，6:50-7:30 进行问答与讨论。
- 🔧 核心内容：涵盖模型修剪定义、结构化修剪对模型大小与性能的影响、GPU/CPU/内存能耗测量。
- 📊 案例研究：基于 Llama 3.1 和 3.2 模型家族，使用 HumanEval 基准评估代码生成性能。
- ⚖️ 权衡分析：探讨模型压缩、准确性与能源节省之间的平衡，以及过度修剪可能增加能耗的反直觉现象。
- 👥 适合人群：对机器学习、AI、数据科学、软件工程或高性能计算感兴趣的学生、专业人士及爱好者。
- 🏢 特别感谢：Spark Coworking 提供场地支持本地数据科学社区。

---

### [从代码到洞察：Agentic AI、MCP 与自动化实践，2026 年 7 月 16 日（周四）下午 6:00 | Meetup](https://www.meetup.com/pydata-milton-keynes/events/314910586/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [From Code to Insight: Agentic AI, MCP, and Automation in Practice, Thu, Jul 16, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-milton-keynes/events/314910586/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

本次活动探讨了 Python、自动化与智能体 AI 在数据分析、金融及现代数据平台中的实际应用，三位讲者分享了从代码到洞察的实践经验。

- 🤖 **智能体 AI 实战**：Shahid Malika Kandy 将分享如何将 AI 代理从实验脚本转化为可靠的生产系统，涵盖工作流设计、状态管理和金融数据案例。
- 📊 **可解释 AI 自动化**：Christian Chimezie 展示 PlotSense 如何通过自动化与可解释 AI 减少手动分析工作，生成可视化并揭示数据模式。
- 🔄 **超越静态规则引擎**：Dhruv Goel 将探讨传统规则系统的局限性，以及智能体 AI 如何实现更自适应、上下文感知的决策，并比较规则、代理与混合模型。
- 🗓️ **活动议程**：18:00-18:10 签到，18:10-20:00 依次进行三场演讲及问答交流，最后有社交环节。
- 🎯 **适合人群**：对可解释 AI、智能分析、生产级代理工作流或 Python 自动化未来感兴趣的从业者，可获取实用经验与行业联系。

---

### [PySteak：解决高风险的烹饪难题，2026 年 7 月 16 日（周四）下午 6:00 | Meetup](https://www.meetup.com/pydatachi/events/315552570/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

**原文标题**: [PySteak: Solving a High-Steaks Culinary Problem, Thu, Jul 16, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydatachi/events/315552570/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-753-july-9-2026)

本次 PyData 芝加哥活动将分享如何用模拟、校准和优化方法解决烹饪牛排时外皮焦脆与内部多汁之间的经典矛盾。

- 🥩 **核心挑战**：烹饪牛排时，外皮需要 300-330°F 产生美拉德反应（甚至更高温度加深焦化），而内部需保持在 129-135°F（五分熟）以保持多汁，两者存在温度梯度导致的灰色过度烹饪带。
- 🔥 **物理原理**：热传导方程解释了高温表面如何驱动热量向内传递，形成难以避免的灰色带。
- 💻 **技术方法**：演讲者将介绍热扩散原理的计算机模拟，以及如何通过数据测量校准模型并优化烹饪方案。
- 🎯 **听众收获**：了解热力学如何影响外皮与内部的权衡，掌握模拟、校准和优化的计算工具，可自定义牛排烹饪方案。
- 📅 **活动信息**：2024 年 7 月 16 日（周四）下午 6:00-8:00（CDT），线上线下混合举办，线上通过 Zoom 参与（需密码）。
- 🏢 **地点与赞助**：线下地址为芝加哥 LaSalle 街 200 号 1100 室，由 AlphaSense 提供场地及食物，其他赞助商包括 W W Grainger Inc、伊利诺伊大学芝加哥分校和伊利诺伊理工学院。
- 🆔 **入场要求**：线下参与者需在 7 月 15 日前提供姓名，到场时出示身份证件。

---

