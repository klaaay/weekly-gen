### [](https://www.youtube.com/watch?v=UEqk0njCuQo&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [You Added One Feature… and Broke Three Others - YouTube](https://www.youtube.com/watch?v=UEqk0njCuQo&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

该页面列出了 YouTube 网站底部常见的链接和版权信息，涵盖平台介绍、法律条款、合作与沟通渠道以及功能测试等相关内容。

- 📄 包括网站简介、媒体、著作权和联系我们等基本信息链接
- 🤝 提供创作者、广告主和开发人员的合作入口
- ⚖️ 包含条款、隐私权、政策与安全性等法律相关内容
- 🛠 说明 YouTube 运作方式及测试新功能
- ©️ 标注版权归属：© 2026 Google LLC

---

### [日常密码学的设计 - Chris Fenner的个人博客](https://www.dlp.rip/everyday-cryptography/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [The Design of Everyday Cryptography - Chris Fenner's Personal Blog](https://www.dlp.rip/everyday-cryptography/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

日常密码学设计探讨了KEM与数字签名接口的易用性对比，指出签名因预哈希等问题变得复杂，并提出通过消息代表间接化来简化，最后总结了密码接口设计的一般原则。

- 🔑 KEM接口极其简单：仅需三个函数，用户无需选择加密内容，所有输入输出类型固定，使用门槛低。
- ⚠️ 现代数字签名接口因“预哈希”问题变得复杂，提供纯签名和预哈希两种变体，导致API数量激增（13个），用户需做5个关键决策。
- 🏗️ 预哈希是密码学界争议话题，它增加了接口多样性（如HashML-DSA与ML-DSA是不同的算法），且对嵌入设备不友好。
- 💀 签名接口的“微管理”特性是复杂根源：它直接处理可变长度消息（从字节到GB），而KEM通过“共享秘密”间接化，将数据加密责任分离。
- 💡 改进方案：引入固定长度的“消息代表”作为间接层，让签名只处理定长代表，定义代表的方式由独立协议完成，类似KEM的共享秘密模式。
- ✅ 密码接口设计应遵循四大原则：少提供不必要的旋钮（只支持必要威胁模型）、单一职责（做一件事并做好）、可测试（支持已知答案测试）、可升级（考虑版本兼容）。

---

### [将PyTorch Monarch引入AMD GPU：基于ROCm的单控制器分布式训练 – PyTorch](https://pytorch.org/blog/bringing-pytorch-monarch-to-amd-gpus-single-controller-distributed-training-on-rocm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [Bringing PyTorch Monarch to AMD GPUs: Single-Controller Distributed Training on ROCm – PyTorch](https://pytorch.org/blog/bringing-pytorch-monarch-to-amd-gpus-single-controller-distributed-training-on-rocm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

大规模训练大型语言模型时，硬件故障是常态。传统检查点方法存在开销大、计算浪费等问题。PyTorch Monarch通过基于actor的运行时和进程网格抽象，实现了弹性容错的分布式训练。文章介绍了将其移植到AMD Instinct GPU（ROCm）的过程，并展示了与TorchTitan和TorchFT集成的故障恢复架构，在SLURM和Kubernetes集群上验证了其稳定性和性能。

- 🚧 传统故障容错策略依赖定期检查点，存在I/O开销大、计算浪费、集群空闲和扩展性差等弊端。
- 🔧 PyTorch Monarch通过actor运行时、进程网格和异步执行模型，提供单程序编程接口，简化大规模训练并支持复杂工作流。
- 🔄 将Monarch移植到ROCm需通过hipify_torch转换CUDA代码，链接RCCL，并采用HIP动态链接（无静态库），通过Rust兼容性模块保持代码平台无关。
- 🛡️ 集成Monarch、TorchFT和TorchTitan构建无检查点的容错架构：Monarch负责编排，TorchFT处理步骤级容错，TorchTitan执行训练，实现故障隔离和快速本地重启。
- 📊 在16节点SLURM（128 MI300 GPU）和32节点Kubernetes（256 MI355 GPU）上验证，持续注入故障下训练未中断，损失曲线平稳收敛，仅需秒级恢复。
- 🔮 未来将扩展NIC支持、优化运行时性能、支持更多预训练和强化学习框架，并继续开源协作。

---

### [无标题](https://www.vpdae.com/redirect/ty0unkq4d32ug77ls8e071j7unc?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [No title found](https://www.vpdae.com/redirect/ty0unkq4d32ug77ls8e071j7unc?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

无法总结：未找到主要内容。

---

### [](https://labs.quansight.org/blog/scaling-numpy-on-free-threaded-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [Scaling NumPy on Free-Threaded Python | Labs](https://labs.quansight.org/blog/scaling-numpy-on-free-threaded-python?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

本文介绍了在自由线程的 CPython 上扩展 NumPy 时发现并修复的多线程瓶颈，包括锁竞争、引用计数竞争和内存分配器问题，最终使多线程性能提升约 30 倍，并超越多进程版本。

- 🔍 从 StackOverflow 问题入手，发现 NumPy 多线程比多进程慢 2 倍以上，瓶颈涉及锁、引用计数和内存分配器
- 🔒 修复 CPython 的 `tracemalloc`：禁用时仍持有全局锁，改为原子操作避免锁竞争（python/cpython#143065）
- ⚡ 重构 NumPy ufunc 调度缓存：从读写锁改为无锁并发哈希表，读路径完全无锁，写路径仅加单锁（numpy/numpy#30593）
- 🧩 解决全局 `PyCapsule` 对象引用计数竞争：将其设为“不朽”对象，避免原子引用计数开销，并新增 `PyUnstable_SetImmortal` C API（python/cpython#144543, numpy/numpy#30826）
- 🚀 优化模块属性查找：为定义了 `__getattr__` 的模块启用字节码特化，避免慢路径加锁（python/cpython#143470）
- 🗄️ 缓解内存分配器竞争：让 NumPy 使用 CPython 的 raw allocator（底层 mimalloc），替代系统 `malloc`/`free`（python/cpython#144916, numpy/numpy#30846）
- 📊 基准测试：修复后多线程在 32 核上从 44 秒降至 1.5 秒（快约 30 倍），比多进程还快 4 倍
- 🎯 总结：NumPy ufuncs 现可高效扩展于自由线程构建，且底层改进（不朽对象、mimalloc 分配器）惠及其他库

---

### [](https://www.youtube.com/watch?v=uSGR6FviCiY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [FastAPI and GraphQL overview - with Strawberry! - YouTube](https://www.youtube.com/watch?v=uSGR6FviCiY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

此页面列出了 YouTube 平台提供的各类政策、功能、支持信息和法律声明。

- 📝 简介：提供 YouTube 的基本介绍
- 📺 媒体：涵盖媒体相关内容
- ©️ 著作权：说明版权管理信息
- 📞 与我们联络：提供联系渠道
- 🎬 创作者：面向创作者的功能与支持
- 📢 广告：介绍广告相关服务
- 💻 开发人员：提供开发者资源
- 📋 条款：列出使用条款
- 🔒 隐私权：阐述隐私政策
- 🛡️ 政策与安全性：说明安全与政策内容
- ⚙️ YouTube 运作方式：解释平台运行机制
- 🧪 测试新功能：介绍正在测试的新特性
- © 2026 Google LLC：版权声明

---

### [Pip 26.2：--only-deps 解决了16年的应用部署难题 – James O'Claire](https://jamesoclaire.com/2026/07/23/pip-26-2-only-deps-solves-16-years-of-app-deployment-hacks/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [Pip 26.2: –only-deps solves 16 years of app deployment hacks – James O'Claire](https://jamesoclaire.com/2026/07/23/pip-26-2-only-deps-solves-16-years-of-app-deployment-hacks/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

Pip 26.2 即将通过 `--only-deps` 标志解决 16 年来安装依赖而不安装项目本身的难题。该功能基于社区多年实践（如 requirements.txt、第三方工具）及基础标准（pyproject.toml、PEP 735）的积累，最终由 uv 的流行推动 pip 采纳，计划于 2026 年 7 月发布。

- 🔧 核心新功能：`pip install --only-deps .` 可直接安装 `pyproject.toml` 中的依赖，无需安装项目本身
- 📜 历史痛点：应用后端、脚本等非包类型项目长期依赖 requirements.txt、pip freeze 或第三方工具（如 pip-chill、pipreqs、poetry、hatch）来模拟依赖安装
- 🚀 uv 的催化作用：`uv sync --no-install-project` 展示了直接需求，加速了 pip 对同类功能的采纳
- 🏗️ 基础铺垫：pyproject.toml（PEP 517，2017）和依赖组（PEP 735，2023）为最终方案提供了标准结构
- ⏳ 解决历程：从 2008 年的 `pip install -e .`（安装项目本身）到 2026 年 PR #13895 合并，历经近二十年社区努力

---

### [在Python中运行子进程 - Python Morsels](https://www.pythonmorsels.com/running-subprocesses-in-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [Running subprocesses in Python - Python Morsels](https://www.pythonmorsels.com/running-subprocesses-in-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

本文介绍了如何使用 Python 的 `subprocess` 模块启动外部进程、捕获输出以及处理错误。重点讲解了 `subprocess.run` 函数及其常用参数，并提供了自定义包装函数的建议。

- ⚙️ 使用 `subprocess.run` 启动外部程序，传入命令列表或字符串（配合 `shell=True`）。
- 📋 默认不捕获输出，设置 `capture_output=True` 可捕获 `stdout` 和 `stderr`。
- 🔍 输出默认是字节类型，设置 `text=True` 自动解码为字符串。
- ✅ 通过 `returncode` 检查进程退出码，`0` 表示成功；设置 `check=True` 可自动抛出异常。
- 🛠️ 可自定义 `run` 函数封装常用参数（如 `capture_output=True, text=True, check=True`）以减少重复代码。

---

### [PyPI用户界面计划更新 - Python包索引博客](https://blog.pypi.org/posts/2026-07-22-ui-updates/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [Planned Updates to the PyPI User Interface - The Python Package Index Blog](https://blog.pypi.org/posts/2026-07-22-ui-updates/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

PyPI 即将推出用户界面更新，以改善安全信号的展示和包详情页的体验。更新将分阶段部署至 TestPyPI 和生产环境，第一阶段已上线供社区测试和反馈。

- 🔒 **新增安全标签页**：集中展示数字认证和来源元数据，提供缺失或变更时的清晰指示。
- 🔄 **导航改为水平标签**：将侧边栏中的内部导航移至水平标签，侧边栏仅保留项目与发布元数据。
- ➡️ **侧边栏移至右侧**：将包描述/自述文件放在左侧，符合从左到右的阅读习惯，并与其他平台对齐。
- 🏷️ **标注信任级别**：明确区分 PyPI 自身数据与维护者提供且经 PyPI 验证的数据，帮助用户评估可信度。
- 📊 **优化侧边栏层级**：按实用性排序元数据，将项目链接和时效性信号置顶，分类数据置底。
- 🎨 **更清晰的状态标签**：使用更醒目的颜色和标签区分隔离、yanked、存档和预发布状态。
- 👁️ **纯视觉改动**：无需维护者操作，现有和未来的数字认证将自动适配新界面。
- 📅 **分四阶段推出**：项目详情（已上 TestPyPI）、文件和发布历史、安全标签页、文档更新（含安全指南）。
- 💬 **邀请社区测试反馈**：在 TestPyPI 试用，通过 GitHub Issue 提建议，通过 Issue Tracker 报缺陷。
- 🙏 **致谢**：感谢 OpenSSF 安全软件仓库工作组、Superbloom、Kabu Creative 的设计研究，以及参与用户访谈和调查的社区成员。

---

### [](https://github.com/andrewyng/openworker?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - andrewyng/openworker · GitHub](https://github.com/andrewyng/openworker?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

OpenWorker是一个开源的AI办公助手，能直接交付完成的工作成果，而非仅提供对话。它运行在本地，支持多种模型和工具，注重隐私和用户控制。

- 🤖 AI助手完成实际任务：生成文档、表格、报告，而非只聊天。
- 🛠️ 集成25+工具：支持Slack、GitHub、Jira、Google日历等，还可通过MCP添加任意工具。
- 🔒 本地优先：数据、对话、令牌都存本地，仅通过你选择的模型和集成离开机器。
- ✅ 审批把关：发送消息、改日历、运行命令前需你确认，避免自动执行。
- 🆓 自带模型：支持OpenAI、Anthropic、Google、本地Ollama等，随时切换。
- ⏰ 定时任务：可设置每日简报、周报等自动化工作。
- 💬 从Slack唤醒：频道中@OpenWorker，它会在桌面执行任务并回复。
- 📂 生成可分享文件：文档、表格、网页可直接保存和分享。
- 🖥️ 多平台下载：提供macOS（Apple Silicon）和Windows（x64）桌面客户端。
- 🧩 技术架构：Python后端+React/Tauri桌面壳，构建于aisuite库之上。
- 📄 开源MIT协议：欢迎贡献，但需附截图说明修复内容。

---

### [GitHub - NVlabs/Sana: SANA: 高效高分辨率图像合成与线性扩散Transformer · GitHub](https://github.com/NVlabs/Sana?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - NVlabs/Sana: SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer · GitHub](https://github.com/NVlabs/Sana?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

Sana 是一个面向高分辨率图像和视频生成的高效开源框架，集成了多种前沿模型与技术，支持快速训练、推理和部署，可在低显存 GPU 上运行。

- 🏗️ 核心定位：高效图像与视频生成代码库，提供完整训练与推理管线，涵盖 SANA、SANA-1.5、SANA-Sprint、SANA-Video、SANA-WM、SANA-Streaming 和 Sol-RL 等多个模型。
- 🚀 模型能力：支持文本到图像（最高 4K 分辨率）、文本到视频（720p 分钟级）、单步生成（0.1s/1024px）、可控世界模型、实时流式编辑等。
- 🔑 关键技术：线性注意力机制、DC-AE 32× 图像压缩、解码器-only 文本编码器、块因果线性注意力、sCM 一致性蒸馏、NVFP4 低精度强化学习等。
- ⚡ 性能领先：例如 SANA-0.6B 在 1024px 图像生成上比 FLUX-dev 快 39.5 倍（吞吐量 1.7 samples/s），SANA-Video-2B 在 VBench 总得分 84.05 优于同量级模型。
- 📦 快速上手：通过 `git clone` 和 `environment_setup.sh` 一键安装，支持 diffusers 推理（代码示例提供），也可集成 ComfyUI、SGLang 等工具。
- 🌐 生态丰富：支持 LoRA/DreamBooth 微调、ControlNet、8bit/4bit 量化、Cosmos-RL 后训练，并已合并到 diffusers 主流仓库。
- 🔓 完全开源：采用 Apache-2.0 许可证，可在 <8GB VRAM 的笔记本 GPU 上通过量化高效运行。

---

### [GitHub - secureagentics/Adrian: 开源运行时AI智能体安全工具 - 实时监控和控制AI智能体，](https://github.com/secureagentics/Adrian?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - secureagentics/Adrian: Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts. · GitHub](https://github.com/secureagentics/Adrian?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

Adrian 是一个开源的 AI 代理运行时安全监控与控制系统，通过同时分析代理的行为和推理过程，在代理执行恶意或越权操作前实时拦截，比单纯行为监控的检测准确率提升 35%，能捕捉 4 倍更多细微攻击。

- 🛡️ 实时拦截：在代理实际执行动作前，通过分析其行为与推理过程进行干预。
- 🔍 双重检测：同时监控活动日志（工具调用、输出）和推理痕迹（为什么做、下一步计划），联合判断风险。
- 🚫 捕获多种攻击：包括提示注入/越狱、工具投毒、数据泄露、凭证泄漏、权限提升、越权操作等。
- ⚡ 快速集成：提供 Python（LangChain）和 TypeScript SDK，以及 Claude Code 原生插件，零代码更改即可使用。
- 🏠 支持自托管：通过 Docker 全栈部署，支持离线运行，使用本地 Gemma 模型进行分类。
- 📊 架构清晰：代理 → SDK → 后端 → 分类器 → 判决 → 控制平面，实现告警/人工审核/直接拦截。
- 🔌 丰富集成：支持多种框架和告警渠道，社区活跃（Discord、LinkedIn），并已在 Product Hunt 上展示。

---

### [](https://github.com/reflex-dev/xy?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - reflex-dev/xy: Ultra-fast and customizable Python charts · GitHub](https://github.com/reflex-dev/xy?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

XY 是一个基于 Rust 核心的极速 Python 图表库，支持交互式网页、笔记本和静态导出。通过声明式或 matplotlib 风格构建图表，可高度自定义样式，并能在浏览器中高效处理数十亿数据点，性能远超同类库。

- 🚀 极速性能：Rust 核心仅计算屏幕需显示的部分，10k 到 100M 点渲染时间稳定在约 0.08 秒，比 Matplotlib/Plotly 快数十倍。
- 📊 灵活 API：支持声明式（如 `xy.line(x, y)`）和 matplotlib 风格（`import xy.pyplot as plt`），可导出 HTML/PNG/SVG/PDF。
- 🎨 深度定制：通过 Python、CSS 或 Tailwind 控制颜色、大小、交互、主题等所有层级。
- 🔬 海量数据：曾渲染 100 亿点 OpenStreetMap 数据，支持密度聚合和缩放回精确行。
- ⚡ 一键安装：`pip install xy` 或 `uv add xy`，依赖少，开箱即用。
- 🖥️ 嵌入式支持：通过 `reflex-xy` 适配器将图表变为 Reflex 组件，无需额外 JS 或 iframe。
- 📚 丰富示例：提供 Gaia DR3、gnomAD、NYC 出租车等 6 个完整笔记本，涵盖不同规模数据。
- 🧩 开源路线图：Apache-2.0 许可，计划添加分布图、K 线、3D 散点等多种图表。

---

### [](https://github.com/AncientJames/Scanwheel/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - AncientJames/Scanwheel · GitHub](https://github.com/AncientJames/Scanwheel/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

Scanwheel 是一个可自行组装的鼓式机械电视，拥有五个并排窗口，每个窗口通过独立 LED 和共享扫描鼓显示不同图像，具备高分辨率显示能力，并附带详细的零件、打印与软件指导。  
- 🛠️ 项目概述：一款 DIY 鼓式机械电视，五窗口设计，每个窗口 9mm×8mm，20 扫描线，利用 Pico PIO 硬件驱动 LED 实现高画质  
- 🎥 配套视频：包含构建过程与实际运行画面  
- 🔧 主要零件：Symbol 步进电机、A4988 驱动板、100μF 电容、Raspberry Pi Pico（无线流媒体需 Pico W）、RGB 及白光 LED 与匹配电阻  
- 🖨️ 3D 打印部件：底座、鼓、盖子；鼓需精细打印（小层高、低速度、Arachne 墙面、100% 填充），提供 OpenSCAD 源文件支持修改  
- 💻 软件与代码：基于 MicroPython 1.28，设备端驱动与示例应用（pico 目录），PC 端视频流（host 目录）及图片转换工具  
- ⭐ 社区数据：177 星标、9 位关注者、12 次 Fork，仓库活跃

---

### [](https://github.com/AutoShiftOps/querytuner?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - AutoShiftOps/querytuner: AI-powered SQL query diagnostics across PostgreSQL, MySQL, Oracle, SQL Server and SQLite. No database connection required. · GitHub](https://github.com/AutoShiftOps/querytuner?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

QueryTuner 是一个 AI 驱动的 SQL 查询诊断工具，无需连接数据库即可分析并优化 SQL 性能，面向非 DBA 开发者群体，支持 5 种数据库方言，提供启发式引擎和可选的 AI 分析层。

- 🗄️ 支持 PostgreSQL、MySQL、Oracle、SQL Server、SQLite 五种数据库方言
- ⚡ 启发式引擎内置 12 条确定性规则，无需外部 API，可即时检测常见性能反模式
- 🗂️ 可粘贴建表 DDL，让索引建议从“估计”升级为“确认”，基于真实表名列名分析
- 🔧 生成方言正确的索引 DDL（如 PostgreSQL 的 CREATE INDEX CONCURRENTLY）
- 🤖 双 AI 提供者可选：HuggingFace（默认免费）或 OpenAI，输出结构化 JSON 或可读文本
- 🔍 结果按严重性分级：Critical → High → Medium → Low
- 📋 输出可直接运行的优化 SQL 改写
- 🔗 每个分析生成永久分享链接（/report/:id）
- 📈 集成 Google Analytics 4 事件跟踪
- 🛡️ 检测 SQL 注入模式和危险结构
- 📊 提供可读性评分，用于代码审查
- 🔒 客户端查询脱敏器：替换专有表名列名，分析后可一键恢复，映射仅存于浏览器内存
- 🔌 提供 REST API，可集成到 CI/CD 流水线
- 🚫 完全基于粘贴的查询文本工作，无需数据库连接（DDL 可选用于确认模式）
- 🏗️ 后端：Python FastAPI + Pydantic + sqlparse + LangChain；前端：React + Tailwind CSS
- 🧩 支持本地运行，环境变量配置 HuggingFace/OpenAI API 密钥
- 📄 包括清晰的目录结构、路线图及已知限制说明
- 💡 采用 MIT 许可证，鼓励开源贡献

---

### [](https://github.com/gmrandazzo/CheapSecurity?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - gmrandazzo/CheapSecurity · GitHub](https://github.com/gmrandazzo/CheapSecurity?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

一个轻量级的自托管CCTV解决方案，专为Linux单板计算机和USB摄像头设计，注重隐私和低成本，视频数据完全本地存储。

- 📹 硬件兼容性强，支持标准USB摄像头和Linux单板（如树莓派、Orange Pi）
- 🧠 基于帧差法的运动检测，支持预运动缓冲和自动录制
- 🔔 邮件和Telegram通知，带快照或视频上传，支持机器人命令控制
- 🌙 夜间模式：软件低光增强（CLAHE）+ 亮度/对比度提升
- 📺 实时MJPEG流 + 可选的RTSP输出（通过MediaMTX+FFmpeg）
- 💾 存储自动清理：按天数、总大小和紧急磁盘空间管理
- 🔐 内置HTTP基础认证，REST API及Swagger交互界面
- 🤖 Telegram机器人：支持快照、录制视频、删除消息等命令
- ⚙️ 系统控制：夜间模式、通知、Telegram上传开关
- 🚀 生产部署就绪：提供systemd服务模板和Gunicorn支持

---

### [GitHub - izeigerman/claude-thermos: 为你保持Claude会话活跃 · GitHub](https://github.com/izeigerman/claude-thermos?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - izeigerman/claude-thermos: Keeps your Claude session warm for you · GitHub](https://github.com/izeigerman/claude-thermos?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

claude-thermos 是一款工具，用于在 Claude Code 主代理等待子代理时自动保持其缓存活跃，避免因缓存过期导致的高昂重新编码费用，可节省约 22% 的成本。它通过本地反向代理监控流量，在主代理空闲且子代理活跃时发送轻量热身请求，并支持命令行和守护进程模式。

- 🔥 解决主代理等待子代理超 5 分钟导致的缓存过期问题，节省约 22% 的费用
- 🚀 通过 `uvx claude-thermos` 直接替代 `claude` 命令，自动在后台执行热身
- ⏱ 可自定义空闲等待时间、热身间隔、最大循环数等参数（如 `--idle` 和 `--interval`）
- 🌐 守护进程模式（`serve`）为 IDE 和多个终端共享一个热身代理，通过设置环境变量接入
- 💰 热身仅消耗缓存读取成本（0.1x），避免昂贵的缓存写入（1.25x），大幅降低费用
- 📊 生成事件日志和汇总报告（`summary.json`），清晰显示节省的 token 和费用

---

### [](https://github.com/ayghri/i-have-adhd?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

**原文标题**: [GitHub - ayghri/i-have-adhd: A skill for your coding agent to stop it from burying the answer. ADHD-friendly output. · GitHub](https://github.com/ayghri/i-have-adhd?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-756-july-30-2026)

该仓库提供一个针对AI编码助手的“ADHD友好”技能插件，让助手输出更直接、步骤化，避免冗长铺垫和无关信息。

- 🧠 插件让编码助手直接给出下一步操作，不再“废话连篇”，适合ADHD人群使用。
- 📦 支持Claude Code和Codex，通过插件市场一键安装，无需克隆仓库。
- ⚡ 效果对比：安装前助手会说“好问题，让我想想……”，安装后直接给出具体命令和步骤。
- 📋 包含10条硬性规则：优先行动、编号任务、抑制跑题、每次给出具体时间估计、列表不超过5项等。
- 🔧 可自定义：fork仓库后编辑`SKILL.md`即可调整规则，再通过插件市场替换。
- 🏆 灵感来源于《成人ADHD工具包》，但针对LLM的响应模式进行改编。
- 📜 MIT开源许可，已有14.2k星标，活跃维护。

---

