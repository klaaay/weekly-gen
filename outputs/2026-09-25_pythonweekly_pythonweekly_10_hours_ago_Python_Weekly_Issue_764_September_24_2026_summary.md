### [在终极井字棋竞技场中争夺第一名](https://tomalard.github.io/posts/fighting-for-1-in-the-ultimate-tic-tac-toe-arena/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [Fighting for #1 in the Ultimate Tic-Tac-Toe Arena](https://tomalard.github.io/posts/fighting-for-1-in-the-ultimate-tic-tac-toe-arena/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

本文讲述作者在 CodinGame 的 Ultimate Tic-Tac-Toe（UTTT）机器人竞技场中争夺榜首的技术历程：从平台限制与 UTTT 规则，到用 MCTS、NNUE、C/SIMD 优化和 Python 伪装提交压缩二进制，并展望未来提升空间。

- 🏁 2018 年 3 月 14 日 CodinGame 发布 UTTT 机器人编程竞技场，如今竞争极强，作者与另外三名玩家争夺第一。
- ⚙️ 比赛模式：提交程序，服务器编译运行，通过 stdin/stdout 通信；限制 100k 字符源码、单弱 vCPU、每回合 100ms。
- ⚖️ 限制反而公平：便于本地自对弈测试，阻止大型神经网络/开局库，让普通玩家也能竞争。
- 🎮 UTTT 规则：3×3 个小棋盘；落子位置决定对手下一步去哪个小棋盘；赢小棋盘，再赢大棋盘；被送到已赢/满棋盘可任意落子；平局按赢小棋盘数判定。
- 🧩 UTTT 未被解决，没有可靠简单启发式，常出现赢小棋盘却全局劣势，适合 MCTS+随机模拟。
- 🚧 优化好的随机 MCTS 可进前 50，但第一与第 50 的 TrueSkill 差约 9，第一预期胜率 >90%；X 优势巨大。
- 🧠 突破靠 NNUE：增量更新累加器，作者使用 (189→1024)×2→10 架构、约 215k 参数，训练 3 亿+自对弈局面。
- 🧬 NNUE 技巧：按 STM/NSTM 编码特征并维护两个累加器；把下一棋盘特征移到输出层做 output bucketing，降低损失并提速。
- 🐍 “Python”提交实为载荷：用 Python 释放 UPX 压缩、clang/PGO 编译的 C 二进制；利用字符而非字节限制，将约 15.875 bit 压进每个 UTF-16 字符，塞入 95k 字符。
- ⚠️ 这种做法在正式比赛被禁；作者认为机器人编程可以接受，并请求不要封号。
- 🌲 搜索：作者没用 alpha-beta，而用 jacekmax/改进 MCTS，便于叶子节点构建累加器并增量评估子节点；选择阶段最终只用简单平均，lambda 漂移到 0。
- ⚡ C 引擎：使用 bitboard、SIMD intrinsics、量化、Squared Clipped ReLU，从更新后的累加器快速评估 NNUE。
- 🥈 当前排名：Daporan 第一，作者第二（差 0.5 TrueSkill），MrSubZero 第三；未来可增加训练数据、扩大网络、改激活函数、设计压缩友好的损失项。

---

### [](https://dev.to/deadlovelll/speeding-up-a-python-service-with-cinderx-jit-and-static-typing-53bh?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [Speeding Up a Python Service with CinderX: JIT and Static Typing - DEV Community](https://dev.to/deadlovelll/speeding-up-a-python-service-with-cinderx-jit-and-static-typing-53bh?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

CinderX 是 CPython 的二进制扩展，通过替换帧求值器接入 JIT、Static Python、并行 GC、轻量帧和库原语；文章核心结论是它只加速字节码，是否值得用取决于服务中纯 Python 字节码的占比，且静态类型与 JIT 通常必须配合才有效。

- 🚀 CinderX 可安装进现有 CPython，启用后执行走替换后的 frame evaluator，包含 JIT、Static Python、并行 GC、轻量帧和类型化容器/原语。
- 🧭 先估算字节码占比：如果耗时在数据库、NumPy、C 扩展或 I/O，CinderX 的上限接近零；如果在纯 Python 遍历和业务规则，可能明显加速。
- ⚙️ 与 CPython 3.14 tier2 JIT 不同：CinderX 编译整个函数/方法，不是 UOP trace，具备 HIR/LIR、SSA、类型推断、内联、寄存器分配和去优化。
- 🧩 CPython tier2 采用 copy-and-patch/stencil，主要消除 dispatch，但不跨 UOP 使用寄存器，中间值仍走帧栈，并依赖 LLVM/clang 与 musttail。
- 🦾 Static Python 是独立编译器，用注解生成专用 opcode：字段偏移访问、直接调用、原始算术；边界做检查，非法写法在导入时被拒绝。
- 🤝 类型与 JIT 必须配合：只上类型无 JIT 可能慢 3.4 倍；只上 JIT 对部分纯字节码测试无提升；结合后 int64 计数循环可达 0.676 ns/迭代。
- 📈 服务 `/recommend` 实测：纯 Python 图遍历和规则下，stock 为 140 rps，typed kernel + JIT 为 250 rps，p99 从 279 ms 降到 13 ms。
- 🧮 服务 `/similar` 实测：耗时在 NumPy，CinderX 无提升；把扫描改回 Static Python 后吞吐从 330 降到 35 rps，说明别把 C/NumPy 路径改回字节码。
- 🧵 服务 `/bundle` 实测：工作便宜但 GC 暂停贵；冻结加并行 GC 把完整暂停从 269 ms 降到 103 ms，吞吐几乎不变。
- 🧊 `immortalize_heap()`/`gc.freeze()` 能让 GC 跳过冻结活对象，但实测 fork COW 下 PSS/Private_Dirty 几乎无变化；它也不会回收垃圾。
- 🧮 并行 GC 只在对象约 100 引用且堆在 fork 后创建时划算；低引用、少核、频繁建线程会使其比串行更慢，建议显式设置 `num_threads`。
- ⏳ async 场景：JIT 只编译协程体，空协程或真正 `await` 调度（asyncio C 代码）不受益甚至略慢；typed 协程体收益明显，但固定包装成本高。
- 📚 库原语如 `AsyncLazyValue`/`async_cached_property` 可保证并发 `await` 只执行一次，ready 值 `await` 从 187 ns 降到 45 ns。
- 🛠️ 编译模式包括 `auto`、`compile_after_n_calls`、`force_compile`、`lazy_compile`、`precompile_all`；批量预编译 200 个函数从 368 ms 降到 88 ms。
- 🚨 测量陷阱：`force_compile` 后调用点可能仍走解释器，`is_jit_compiled()` 可能为 True；必须用 `count_interpreted_calls` 验证实际执行路径。
- 🧱 Static Python 限制多：`range` 需换 `crange`、原始类型会溢出、模块常量不能 primitive、模块冻结导致 `mock.patch`/`cached_property` 需特殊处理、async primitive 返回类型有 JIT bug。
- ✅ 结论：先 profile 估算字节码占比；纯 Python 热路径值得移植并启用 JIT，NumPy/DB 包装不要期待收益，JIT 与静态类型一起用才有效。

---

### [错误](https://digline.dev/blog/bad-evals-my-own/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [Error](https://digline.dev/blog/bad-evals-my-own/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='digline.dev', port=443): Max retries exceeded with url: /blog/bad-evals-my-own/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Python Workers 现已正式可用 | Cloudflare 博客](https://blog.cloudflare.com/python-workers-ga/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [Python Workers are now generally available | Cloudflare Blog](https://blog.cloudflare.com/python-workers-ga/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

Cloudflare 宣布 Python Workers 正式可用（GA），Python 成为 Cloudflare 开发者平台的一等支持语言；现有 Python 代码、库和设计模式可无缝接入 Workers AI、R2、D1、Hyperdrive、Durable Objects、Queues、Workflows 等平台能力，并支持 FastAPI、Django、Flask 等框架。

- 🚀 Python Workers 结束多年开发后正式 GA，目标是让 Python 开发体验像 TypeScript 一样简单，并让 Python 包和框架“直接可用”。
- 🧩 原生支持 Cloudflare 绑定，运行时会自动完成 Python 与 JavaScript/TypeScript 对象的类型转换，不再需要 `pyodide.ffi.to_js` 等胶水代码。
- 🌐 可通过 `workers.asgi` 和 `workers.wsgi` 连接器运行 FastAPI、Django、Flask 等框架，无需在 Workers 内自行运行 Uvicorn、Gunicorn 等 Web 服务器。
- 🗄️ 通过 Workers `connect` API 实现 socket 系统调用，使 PostgreSQL/MySQL 驱动可用，并集成 Hyperdrive，支持 `aiomysql`、`asyncpg` 等数据库驱动。
- 📦 推动 WebAssembly Python 包生态：PEP 783 获接受并标准化 PyEmscripten，稳定 Pyodide 工具链，同时让 `cibuildwheel` 支持该平台。
- 🤖 支持 `openai`、`langchain`、`mcp` 等 AI 库，可与 Workers AI、AI Gateway 结合，在 Cloudflare 网络上运行 serverless AI 推理与代理。
- 🛠️ 提供生产级示例，包括 Queue + Workflows + Workers AI + R2 的图像生成、Durable Object 支撑 Bluesky Jetstream WebSocket、MCP Server、Vectorize RAG 等。
- 📚 Cloudflare 开发者文档已大量增加 Python 示例，用户可在 JavaScript、TypeScript、Python 代码片段间切换。
- ⚡ 未来计划提升 Python Workers 性能与内存效率，并继续扩大支持的 Python 包范围；开发者可在 Discord 或 GitHub 反馈需求。

---

### [](https://www.better-simple.com/django/2026/09/17/share-how-you-use-django-with-django-probe/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [
    
      Share how you use Django with Django Probe · Better Simple
    
  ](https://www.better-simple.com/django/2026/09/17/share-how-you-use-django-with-django-probe/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

Django Probe 是一个低门槛、高影响力的工具，让开发者分享自己的项目如何使用 Django，并把聚合数据回馈社区，以帮助维护者、Steering Council 和社区基于真实使用情况而非直觉做决策。

- 🧭 想法起源于 DjangoCon US 芝加哥，作者提出扫描代码模式并回传中央 hub；获得积极反馈后实现了 Django Probe。
- 🛠️ 使用流程：注册并创建项目 token，安装包后设置 `DJANGO_PROBE_TOKEN`，运行 `django-probe scan .` 审查 payload，再用 `django-probe submit .` 分享数据。
- 💡 Jeff Triplett 建议不要只统计预设模式，而应统计所有 Django 类、方法和函数的使用，这大大拓展了工具价值。
- 📊 聚合使用数据可帮助维护者了解如 `QuerySet.extra()` 等弃用功能的实际使用情况，包括是否仍被使用、项目规模和 Django 版本。
- ⚖️ 当前 Django 决策常依赖直觉和圈内轶事；Django Probe 可提供客观数据，用于决定新增、移除功能以及框架瘦身方向。
- 🔌 未来也可用于非 Django 包，例如分析使用 `django-allauth` 的项目中有多少使用 MFA，从而辅助认证等功能的决策。
- 📚 它还能指导社区资源分配：若 `models.Field.contribute_to_class()` 等未记录功能仍被使用，可考虑文档、教程、演讲，甚至纳入弃用政策以保护 API。
- 🧪 项目仍在活跃开发；可作为 linter 或独立 CI 动作运行，长期每月分享一次可能足够，但更频繁分享有助于发现 bug。
- 🗃️ 目前只接收数据、不输出报告；写作时已有 11 个项目分享，足以开始基础报告，但高级分析需要更多项目参与。
- 🙌 参与方式：创建账号分享项目如何使用 Django，或为 Django Probe 包贡献代码。
- ⚠️ 若使用 `@cache_page`，应审计是否缓存了用户特定内容，如 CSRF token 或 CSP nonce。

---

### [这个设计模式取代了整个类层次结构 - YouTube](https://www.youtube.com/watch?v=IdwdqdywNOM&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [This Design Pattern Replaces an Entire Class Hierarchy - YouTube](https://www.youtube.com/watch?v=IdwdqdywNOM&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

这是一组 YouTube/Google 页面底部常见链接与版权信息，主要涵盖平台介绍、联系渠道、创作者与广告资源、开发者入口、法律条款、隐私安全、功能测试及版权归属。

- ℹ️ 关于：了解平台或公司背景
- 📰 新闻：查看媒体报道与动态
- ©️ 版权：版权相关信息
- 📞 联系我们：获取联系与支持渠道
- 🎬 创作者：面向内容创作者的入口
- 📢 广告：广告投放与合作信息
- 💻 开发者：开发者相关资源与接口
- 📜 条款：服务条款与使用规则
- 🔒 隐私：隐私政策说明
- 🛡️ 政策与安全：平台政策及安全信息
- ⚙️ YouTube 运作方式：了解平台运行机制
- 🧪 测试新功能：参与或查看功能测试
- ©️ 2026 Google LLC：版权归 Google LLC 所有

---

### [如何在 Python 中构建 AI 智能体 - 3 种方法 - YouTube](https://www.youtube.com/watch?v=-RTgK6qX6A8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [How to Build AI Agents in Python - 3 Ways - YouTube](https://www.youtube.com/watch?v=-RTgK6qX6A8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

这是 YouTube 页面底部信息，主要列出平台导航链接、政策条款及版权声明，方便用户访问关于、支持、开发者等入口。
- ℹ️ 关于：平台介绍入口
- 📰 新闻：新闻与公告
- ©️ 版权：版权相关信息
- 📞 联系我们：联系渠道
- 🎬 创作者：面向创作者的资源入口
- 📣 广告：广告投放相关信息
- 👨‍💻 开发者：开发者相关入口
- 📜 条款：服务条款
- 🔒 隐私：隐私政策
- 🛡️ 政策与安全：政策及安全说明
- ⚙️ YouTube 的工作原理：平台机制介绍
- 🧪 测试新功能：新功能测试入口
- © 2026 Google LLC：版权归属 Google

---

### [获取失败](https://blog.jupyter.org/notebooks-on-demand-nod-a-jupyterlab-extension-for-a-notebook-anywhere-bf1605913127?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [Failed to retrieve](https://blog.jupyter.org/notebooks-on-demand-nod-a-jupyterlab-extension-for-a-notebook-anywhere-bf1605913127?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

无法总结：获取内容失败，状态码 403。

---

### [vLLM中的硬件无关模型 – PyTorch](https://pytorch.org/blog/hardware-agnostic-models-in-vllm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [Hardware-Agnostic Models in vLLM – PyTorch](https://pytorch.org/blog/hardware-agnostic-models-in-vllm/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

vLLM 正引入“硬件无关”层，以在追求前沿 SOTA 性能、转向与 fullgraph torch.compile 不兼容的 flat 模型时，继续支持多样模型、旧 GPU 和树外加速器；在 H100 上，该路径的总 token 吞吐量与原生实现差距在 3.4% 以内（三个近期模型几何平均）。

- 🚀 vLLM 为在前沿保持 SOTA，正改变内部实现，使其与 fullgraph torch.compile 不兼容，可能影响 OOT 加速器、旧 GPU 和特殊模型。
- 🧩 为此推出“HW agnostic”硬件无关层，目标是在继续快速前进的同时满足可移植性需求。
- 🌐 vLLM 一直作为抽象层支持多种模型与硬件，包括 NVIDIA、AMD、Intel、Google、IBM、Huawei 等，并借 torch.compile 优化与融合。
- 🧠 前沿开放权重模型架构快速分化，常带定制层和优化内核；DeepSeek V4 与 Kimi K3 用不同方法实现百万 token 上下文。
- 🛠️ 将新模型接入 vLLM 需全图可编译、注册 torch 库 op、提供 fake 实现与 mutation 注解，增加模型开发负担。
- ⚡ Blackwell 与 GB300 NVL72 等系统需要精细内核工程，以利用新特性并重叠计算与通信。
- 🤖 Claude Code、OpenAI Codex 等编码代理擅长针对特定模型和硬件做优化，但最好无需担心影响其他模型或加速器。
- 🧱 趋势促使 vLLM 维护硬件特定“flat”模型，用自定义融合替代 torch.compile；新前沿模型均采用此方式，现有层可能被重构为不兼容 torch.compile。
- 🧭 当前模型定义有三种：`vllm/models` 的 flat、`vllm/model_executor/models` 的 legacy、transformers 后端；共同层仍主要在 `vllm/model_executor/layers`。
- 🔌 现有层支持 torch.compile 和 OOT 扩展，如 `CustomOp` 与 `PluggableLayer`，对 Spyre 等插件和 transformers 后端原生速度很关键。
- ⚠️ 问题在于：flat 路线要破坏 torch.compile 兼容性和扩展性，可能导致 OOT 插件维护负担、旧/特殊模型 GPU 性能回退、旧及消费级 GPU 支持不足。
- 🧩 解决方案是构建 in-tree 硬件无关层，遵循可编译、可扩展、隔离、可移植四原则，主要用 PyTorch、Triton、Helion。
- 🔁 transformers 后端已可重定向到 `model_executor/hw_agnostic`，设置 `USE_HW_AGNOSTIC=1` 启用；已用 Spyre 插件验证 Gemma 4、Qwen3、Granite 4.2。
- 🗺️ 计划为每个 flat 模型提供使用硬件无关层的 `model.py`；共享层放 `model_executor/hw_agnostic`，模型特定层留在本地，DeepSeek V4 PR 正在审查。
- 📊 目标不是 Blackwell/CDNA4 的顶尖性能，而是跨硬件可移植；H100 实验显示硬件无关路径接近甚至偶尔略优于原生实现。
- 🚧 该工作仍在进行并欢迎反馈；可查看 RFC、vLLM Slack `#hw-agnostic-models`、vLLM.ai 和 GitHub 项目页。

---

### [](https://dev.to/aws-builders/put-the-arithmetic-in-the-tool-an-mcp-server-for-an-aws-waste-scanner-3n79?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [Put the Arithmetic in the Tool: an MCP Server for an AWS Waste Scanner - DEV Community](https://dev.to/aws-builders/put-the-arithmetic-in-the-tool-an-mcp-server-for-an-aws-waste-scanner-3n79?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

overview summary
文章介绍如何为 AWS 成本扫描器 zombiescan 增加 MCP Server，让 AI agent 与终端复用同一只读扫描引擎；核心是把算术、过滤和只读边界放进工具，并用端到端测试保证两个入口总额一致。

- 🎯 背景：同一份扫描 JSON 被人和 agent 读取，若数字不一致很难发现；让模型自己做加法不可靠，因此应把算术放在工具内。
- 🧰 准备：需要可用的 AWS 只读凭证、Python 3.12、uv、ce:GetCostAndUsage 权限，以及 Claude Code 用于插件。
- 🖥️ 终端扫描只读：示例扫描 17 个区域，得到 120 条发现，估算浪费 $6.90/月、$82.80/年。
- 🔌 通过 stdio 暴露 MCP：使用 JSON-RPC 2.0，支持 initialize、tools/list、tools/call，不依赖 MCP SDK。
- 🛠️ 提供 5 个工具：scan_account、estimate_savings、explain_finding、list_checks、plan_cleanup。
- 📊 工具返回计算结果而非原始行：总额、数量、极值、按检查/区域分组和所用过滤器，避免模型自行汇总。
- 🔍 过滤器回显：未匹配的检查会返回 no_such_checks_in_report 与 not_matched，防止把“精确的 0”误读为好消息。
- 🔒 只读边界：服务器只生成 cleanup 计划，不执行清理；clean --apply 仅在终端运行，并用测试防止越界。
- ➗ 总额规则：报告总额必须等于打印行的总和；示例中每项先四舍五入得 $0.48，而不是先加总得 $0.50，以换取可复现。
- 📈 账单校准：ECR 估算 $6.40/月，高于按 Cost Explorer 投影的 $2.99/月，约 2.1 倍，原因是共享层被按镜像重复计算。
- 🧩 Claude Code 插件：通过 .mcp.json 启动服务器，skill 规定扫描一次、引用 filter_applied、把 complete:false 当未完成扫描。
- 🧪 测试：离线测试 343 通过，实时测试 3 通过，其中一项比较终端与 MCP 两个前端结果。
- ⚖️ 使用建议：终端适合首次查看和报告；MCP 适合追问区域、节省来源和原因；二者同引擎，不一致即缺陷。
- ⚠️ 限制：存在两分钱舍入差异；ECR 估算偏保守；价格不含私有定价、节省计划与 credits。
- ✅ 结论：把确定性算术移出模型、放进工具，并为两个入口建立同一总额契约，可提升 AWS 成本报告的 agent 可靠性。

---

### [](https://github.com/jaredpalmer/kev?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - jaredpalmer/kev: Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run on your own · GitHub](https://github.com/jaredpalmer/kev?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

Kev 是 jaredpalmer 的开源小型决策模型家族，基于 Qwen3.5/3.8 和 Jev 风格架构，支持自行训练、微调与部署；其 API 兼容 TypeSafe System One，提供 0.8B、4B、9B、27B 四种规模，面向路由、分类、评分等决策任务。

- 🧠 **定位**：小型 Jev 类决策模型，可在本地训练和运行，也可使用预训练权重。
- 🧩 **API 兼容**：匹配 TypeSafe System One，TypeSafe Python SDK 可直接指向本地 Kev 服务器。
- 🎯 **一问多答**：同一请求支持是/否（noul）、多选（choice）、评分（score），问题共享文本但不能互读。
- 📊 **默认校准**：每个 checkpoint 带在留出数据上拟合的温度，默认返回校准概率。
- 📦 **四种规模**：Kev-0.8B、4B、9B、27B；0.8B 可笔记本运行，4B 推荐起步，9B 需更大 GPU，27B 最准但需 80GB GPU。
- 🏆 **性能对标**：新来源上 Kev-27B 准确率 0.848/0.896，接近 Jev 的 0.857；Kev-4B/9B 约在 4 点内。
- ⚠️ **对比限制**：Jev 训练数据未知，因此不是受控架构比较；Jev 仅在开发集上运行。
- 🌐 **在线试用**：Hugging Face Space 可直接试 Kev-4B 和 0.8B，无需安装。
- 💻 **本地运行**：需 Python 3.12/3.13 与 uv；运行 `python -m kev.serve --run jaredpalmer/kev-4b --port 8009` 可启动本地服务，自动使用 CUDA/ROCm/MLX。
- 🔌 **请求示例**：POST `/v1/systemone`，state 为文本，questions 定义类型、说明和 criteria，返回概率、置信度、延迟与 token 用量。
- 🐍 **Python 调用**：TypeSafe SDK 随 `--extra serve` 安装，设置 `base_url` 指向本地 Kev 即可复用 Jev 代码。
- 🛠️ **微调**：用自己的标注数据短微调通常优于改 prompt，并会按你的数据拟合温度。
- 📈 **微调效果**：示例支持负载中 Kev-4B 从 67.7% 提升到 73.6%，5% 错误预算下自动决策从 34% 到 48%；消费者金融投诉从 0.804 到 0.904。
- 🤖 **代理微调**：`npx skills add jaredpalmer/kev@kev-finetune` 可让 coding agent 在 Modal 上自动完成找问题、生成/转换标签、微调、校准、评测和部署；Kev-4B 训练约 1 美元。
- ✍️ **手动微调**：JSONL 一行一个请求，每个问题加 `label`；用 `--init_from` 从发布 checkpoint 继续，保留已有知识，学习率可从 `2e-5` 开始。
- ☁️ **一键部署**：有 Modal 账号即可用 `kev_serve.py` 部署 HTTPS 端点，Bearer 鉴权，空闲缩零，首次冷启动约 35 秒。
- 🎛️ **可换模型**：`KEV_MODEL` 可切 Kev-9B 等；Kev-27B 自动选 B200/H200/H100；也有 `kev-deploy` skill。
- 📉 **准确率边界**：Kev-27B 在 11 个新来源类别中 9 个接近或超过 Jev；小模型在知识题和日期算术上落后；MMLU 上 Kev-9B 0.74、Kev-27B 0.84、Jev 0.90。
- 📏 **置信度**：Kev-9B 在 4.0% 新来源问题上以 ≥0.9 概率答错，Jev 为 3.7%；5% 错误预算下 Kev 可自动化 0.45–0.57，Jev 为 0.70。
- ⚡ **速度**：Kev-4B 在 H100 上 6 个问题约 18.1ms，L40S 约 41.5ms；H100 约 101 req/s；Apple M5 约 721ms/5 问，缓存后 136ms。
- 📚 **长度限制**：训练最多 384 个 state token；服务接受 8,192 state token 和每问 8,192 token；长文准确率下降，Kev-27B 较稳。
- 🧪 **Playground**：Node 20.9+，`cd playground && npm install && npm run dev -- -p 3001`，可编辑文本/问题、比较打包与分离、排列选项、测试隔离和象棋 demo。
- 🧱 **工作原理**：每个 checkpoint 是 Qwen 基座上的 rank-16 LoRA adapter 加小型 pointer head；训练用交叉熵，基座权重冻结。
- 🔒 **问题隔离**：Qwen3 注意力模型用 mask 隔离；Qwen3.5/3.8 的 DeltaNet 需每问单独一行，复用 state 缓存，隔离精确。
- 🏋️ **训练数据**：共享 decision-v7：10,000 个公开数据集样本、896 个生成策略、1,680 个规则结构样本；0.8B/4B/9B 训练两轮，LoRA rank 16。
- 🧮 **校准与日期**：校准温度 Kev-27B 1.38、9B 2.30、4B 2.41、0.8B 2.35；`KEV_DATE_FACTS=1` 可将 Kev-9B 日期政策题从 0.80 提到 0.90（Jev 0.93）。
- 🧪 **基准**：evals 冻结并用 CI 校验；decision-v7 测训练源，transfer-v4 测 764 条新源，transfer-v9 加 MMLU-Pro、埋藏问题和不可知样本。
- 🧾 **外部基准**：Kev 在 SemIf、scienthoon 等有竞争力，但在 WANLI 和 TypeSafe evals 上落后 Jev。
- 🖥️ **服务性能**：按模型选 GPU：0.8B 用 L4，4B 用 L40S/H100，9B 用 L40S/H100，27B 用 B200/H200/H100；Mac 通过 MLX 运行但较慢。
- 🚧 **限制**：单温度校准不能重排置信度；知识题依赖基座；微调可能损害日期算术；选项顺序可改变答案；27B 无 Mac 路径且后训练数据未知。
- 🧾 **许可证与作者**：Apache-2.0，作者 Jared Palmer，Built with Devin，仓库约 6.8k stars、391 forks。

---

### [](https://github.com/superdesigndev/treg?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - superdesigndev/treg: OpenRouter for agent tools. Join community here: https://discord.gg/6mQYYfFMAn · GitHub](https://github.com/superdesigndev/treg?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

treg 是“面向 Agent 工具的 OpenRouter”：用一个 base URL 和一个 token，即可让 Agent 调用 3,000+ 个编目端点、覆盖 60+ 提供商，按次计价、无需注册供应商；同时支持团队自有密钥、CLI 和技能在服务端安全注入凭据。

- 🧰 核心定位：外部目录端点由 treg 用自有密钥或公共路由服务；自有工具始终优先，且不计入团队余额消耗。
- 🔑 两类工具：目录端点（如 SEO、社交、 enrichment、广告、抓取、图像/视频生成）与团队自有工具（付费 API、OAuth、厂商 CLI、SKILL.md）。
- 🪜 凭据阶梯：团队自有工具 → 团队存储密钥 → 已验证公共路由免费 → treg 自有密钥计费；无公开价格会拒绝，不静默切换供应商。
- 🚀 快速开始：安装 CLI、`treg login`、`treg catalog search`、`treg call`、`treg balance`，或运行 `treg onboard` 引导。
- 🎙️ 示例能力：可调用 Fish Audio TTS、语音发现、语音克隆等；输出可重定向到文件，团队语音资源可复用。
- 🤖 Agent 集成：支持 Claude Code 插件、`npx skills add superdesigndev/treg -s treg`、MiniMax 插件市场，以及 Claude 连接器 MCP 表面。
- 🧭 目录发现：按“任务”搜索，`treg catalog get <id>` 查看参数、价格与示例；严格工具会拒绝未声明参数。
- 💳 计费与余额：支持 `treg topup`；余额不足返回 HTTP 402，含 `balance_micro`、`estimated_cost_micro` 和 `topup_url`。
- 🏟️ Enrich Arena：在 `/enrich-arena` 比较 enrichment 供应商的答案、成本与速度，可投票或观察异步瀑布流。
- 📦 分享自有工具：`treg scan` 只读预览，`treg upload` 加密注册 `.env` 密钥、技能目录和已安装目录 CLI。
- 🖥️ CLI 运行：`treg run` 注入组织凭据执行 `stripe`、`gh`、`vercel` 等；`--local` 本机运行，`--server` 服务端运行，`treg shell start` 开启自动注入子 shell。
- 🧩 技能系统：技能 = `SKILL.md` + 密钥 + 工具；支持 `treg upload skills --dir`、`treg skill install`、`treg skill init/add` 与 OAuth 连接。
- 👥 团队权限：账户最多拥有 10 个团队；一切以 org 为范围，角色为 owner/admin/member/viewer，支持邀请、加入、切换和按成员工具访问。
- 📝 反馈与审查：可用 `treg feedback submit` 提交问题，用 `treg review CALL_ID useful` 评价受邀目录调用。
- 📚 深入入口：`USAGE.md` 是完整 CLI 参考，`/llms.txt` 用于 Agent 入门，dashboard 提供 CRUD、教程，`/docs` 提供 OpenAPI 文档。
- 🏠 自托管：`scripts/dev-local.sh up` 可在 `localhost:18790` 启动；也支持 `uv run python -m treg`，服务器需安装 `tools-registry[server]`。
- ⚙️ 配置与备份：使用 `TREG_*` 环境变量，默认适合本地开发；生产需设置密钥、会话、OAuth、Resend、Admin 等，并备份 Fernet 密钥和数据库。
- 🧬 架构要点：`/call` 流程为解析工具 → 解密密钥 → 注入 → 流式转发上游 → 异步审计；`api.py` 是核心，CLI 与技能是瘦客户端。
- 🔐 认证与转发：支持 `env`、`secret_file`、`oauth`、`cli_auth` 四种注入器；代理忠实转发，只改逐跳头、treg 控制头和注入凭据。
- 🧪 测试、贡献与路线图：使用 pytest-xdist 并行测试；设计文档位于 `docs/context/`；路线图包括 MCP 支持、更细权限、静态密钥管理强化等。
- 📜 许可证与多租户：Apache 2.0 加附加条款，允许商用和自托管，但不得未经许可作为竞争性托管注册表服务再分发；支持 pinned customer 读取范围与归因。

---

### [](https://github.com/browser-use/jev-ultrafast?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - browser-use/jev-ultrafast: Fastest and cheapest web agent · GitHub](https://github.com/browser-use/jev-ultrafast?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

browser-use/jev-ultrafast 是 Browser Use 生态中一个公开的浏览器代理项目（MIT 许可，约 19.8k stars、1.3k forks），核心是用动态索引动作空间与 TypeSafe 单次推测式请求，让代理更快、更便宜地完成网页任务；Google Flights 苏黎世→伦敦搜索演示约 7.1 秒完成。

- ⚡ 核心机制：给一个自然语言目标，Jev 从编号元素表中选择操作和元素；小型 LLM 仅在 TYPE_TEXT 时生成文本。
- 🧭 动作空间：CLICK、TYPE_TEXT、SELECT、SCROLL_UP、SCROLL_DOWN、WAIT、DONE、BLOCKED；只提供受支持的操作与目标。
- 🧩 每次观察生成新元素表，如按钮、组合框、文本框等，并带编号、名称、当前值和文本。
- 🔀 一次 TypeSafe 请求同时决定操作与目标，两个决策共用一次网络往返；目标头只包含兼容元素，下拉选项带观察到的元素/选项索引。
- 🚫 无站点特定动作脚本或预置字段字符串；Flights 示例只提供目标并独立验证结果。
- 🛠️ 运行方式：git clone、uv sync、复制 .env、配置 TYPESAFE_API_KEY 与 TEXT_MODEL_API_KEY，执行 uv run jev，打开 http://127.0.0.1:8766 启动演示。
- 🔍 检查器显示编号元素、操作概率、目标概率和执行动作；可选择下一步暂停后再执行。
- 🌐 Chrome 通过 Browser Harness 连接，可用 uv run browser-harness --doctor 检查；示例文本模型为 OpenRouter 的 inception/mercury-2.5（禁用推理），也支持 Gemini、GLM、DeepSeek 等兼容模型。
- 🐍 可作为库使用：from jev_ultrafast import Agent，传入 URL 与目标并迭代 agent.run()；同一策略可跑维基百科和酒店搜索/过滤任务。
- ✈️ examples/flights.py 会执行航班搜索并检查路线、日期、结果，保存 trace，但不会选择或预订航班。
- 🚀 速度来源：每决策周期一次请求、操作与目标共享观察状态、默认循环不用截图、每个快照一次浏览器调用、验证目标、等待有用状态、保持隐藏标签渲染、只发送可见文本、复用中断文本请求。
- 🔒 安全边界：执行目标必须来自观察节点，执行器重新检查页面新鲜度与点击遮挡；模型输出不会变成选择器、坐标、shell 命令或可执行 JS，文本助手输出须先解析为 JSON。
- 📁 代码小而可读：agent.py、snapshot.js、browser.py、model.py、questions.py、demo.py 分别负责循环、DOM 快照、浏览器执行、模型头与文本生成、指令和本地检查器。
- 📊 证据：Google Flights 运行 7,073 ms，计时包含模型调用、生成文本、浏览器操作、过期决策和加载等待；独立验证单程、苏黎世、伦敦、2026-09-20 与可见航班选项。
- ⏱️ 六次交替运行中两版均 3/3 通过；中位任务时间从 9.450 s 降至 7.092 s（25%），中位浏览器协议调用从 1,092 降至 101，但这不是通用可靠性基准。
- 🧪 其他结果：同一策略打开指定维基百科文章 2.798 s，通过本地酒店搜索/过滤任务 1.896 s；细节见 performance.md。
- ⚠️ 限制：DONE 仍需独立结果验证；DOM reader 仅处理常见 HTML/ARIA 控件，不支持完整 accessible-name 规范，且 shadow roots、frames、canvas、上传、弹窗标签、嵌套滚动和任意键盘控件仍在 MVP 外；自有标签共享现有 Chrome 配置。
- 🧹 开发测试：uv run ruff check、uv run pytest、node --check、uv build；测试离线；scripts/check_guards.py 可在本地浏览器检查真实控件且不调用模型；录屏脚本会发起付费 API 调用，凭据与原始 trace 不入库。
- ☁️ Browser Use Cloud 等待名单已开放，可申请早期访问超快云浏览器代理；相关资源包括 Browser Use、Browser Harness 和 TypeSafe speculative fan-out。

---

### [](https://github.com/confident-ai/deepteam?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - confident-ai/deepteam: DeepTeam is a framework to red team LLMs and AI agents. · GitHub](https://github.com/confident-ai/deepteam?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

DeepTeam 是 Confident AI 推出的开源 LLM 红队测试框架，面向 LLM 系统与 AI Agent，模拟越狱、提示注入、多轮利用等攻击，发现偏见、PII 泄露、SQL 注入等漏洞，并提供生产环境防护栏；它基于 DeepEval，可在本地运行，支持 CLI 和 Python。

- 🧠 定位：把红队测试类比为针对 LLM 的渗透测试，覆盖 AI Agent、RAG 管道和聊天机器人。
- 🛡️ 漏洞库：提供 50+ 即用漏洞，支持任意 LLM，并用本地 LLM-as-a-Judge 生成二元通过/失败评分与理由。
- 📂 漏洞类别：涵盖数据隐私、负责任 AI、安全、安全防护、商业风险、Agentic 风险以及自定义漏洞。
- 💥 攻击方法：提供 20+ 研究支持的单轮与多轮对抗攻击，如提示注入、角色扮演、Leetspeak、ROT13、Base64、多语言、上下文投毒、线性/树状/Crescendo 越狱等。
- 🏛️ 安全框架：开箱即用支持 OWASP Top 10 for LLMs 2025、OWASP Top 10 for Agents 2026、NIST AI RMF、MITRE ATLAS、BeaverTails、Aegis。
- 🚧 生产防护：提供 7 个即用 guardrails，可实时拦截输入输出，包括 Toxicity、PromptInjection、Privacy、Illegal、Hallucination、Topical、Cybersecurity。
- 🧩 扩展能力：支持自定义漏洞和攻击，可通过 CLI + YAML 或 Python 编程方式运行，结果可显示为数据框并保存为 JSON。
- 🚀 快速开始：安装 `pip install -U deepteam`，定义 `model_callback` 后调用 `red_team`，无需准备数据集，攻击会根据目标漏洞动态生成。
- 📊 示例流程：`PromptInjection` 攻击测试 `Bias` 漏洞，输出经 `BiasMetric` 评分，最终通过率为评分为 1 的比例。
- ☁️ Confident AI：原生集成平台，可管理风险评估、生产监控、共享报告，并支持从 IDE/MCP 运行红队。
- 📜 开源信息：Apache 2.0 许可，GitHub 约 2.9k Stars、486 Forks、1,191 Commits，由 Confident AI 创始人构建。

---

### [GitHub - Human-Agent-Society/reef：面向自我改进智能体的持续学习基础设施 · GitHub](https://github.com/Human-Agent-Society/reef?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - Human-Agent-Society/reef: Continual learning infra for self-improving agents · GitHub](https://github.com/Human-Agent-Society/reef?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

Reef 是首个面向自我改进智能体的持续学习开源基础设施，连接智能体推理、反馈、学习与版本化交付，支持训练模型权重（结合 Slime 和 SGLang）或优化智能体框架（提示词、规则、技能）。

- 🎯 **核心定位**：让智能体通过与你交互的过程持续学习、不断变强，支持模型权重训练、框架优化和测试时训练三种路径
- 🧩 **技术栈差异**：与推理引擎（vLLM、SGLang）和强化学习训练框架（Slime、veRL、AReaL）互补，独家提供版本管理、更新期间保持在线、以及权重之外（技能、框架）的演化能力
- 🔄 **四步学习循环**：服务（处理请求并记录交互）→ 观察（将反馈匹配到记录）→ 成长（从合格记录生成更新）→ 提交（评估候选并按策略发布版本）
- 📦 **安装方式**：支持通过 PyPI 安装（`uv pip install reef-infra`）或从源码安装，使用 LFS 管理产物和检查点
- 🚀 **最小示例**：可作为纯推理服务器启动，兼容 OpenAI 和 Anthropic 接口，通过 `x-reef-scenario` 头创建场景，用 `x-reef-agent-record-id` 回执上报评分与反馈
- 🛠️ **框架演化**：内置 Reefine 配方，仅需模型 API 端点即可用自然语言改进编码框架，支持 `/reefine`、`/versions` 等交互命令
- 📚 **配方生态**：按任务类型选择配方，覆盖科学发现（TTT-Discover）、任务流持续学习（SAO、GEPA）、真实使用学习（OpenClaw-RL、SkillClaw）；Reefine 随包发布，其余位于 recipes/ 目录
- 🏗️ **文档结构**：包含快速开始、HTTP API、编写配方、框架演化、模型演化、配方目录、核心循环和术语表
- 🤝 **社区参与**：可通过 Discord、微信群、GitHub Discussions 交流，欢迎贡献配方与 RFC 设计，项目已获 4.7k Stars、402 Forks
- 🙏 **关键依赖**：由 SGLang（高性能推理）、slime（模型权重训练）、cordis（框架演化）等项目提供核心支撑

---

### [](https://github.com/MG1937/ASC?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - MG1937/ASC: ASC is a super FAST Android decompiler front-end designed for Agents/Mobile Researchers. · GitHub](https://github.com/MG1937/ASC?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

ASC（MG1937/ASC）是一个面向智能体与移动安全研究者的超高速 Android 反编译前端；其核心 Droid ASC 将 R8 编译器优化视为反编译原语，跳过传统重型预处理，把已编译 APK/DEX 当作只读数据库直接查询，实现按需、毫秒级的代码搜索、交叉引用与反编译。

- 🚀 **背景痛点**：传统反编译大型 APK 需等待工具消耗数 GB 内存、完整解压并构建庞大全局索引，耗时且违背已编译产物的结构化特性。
- 🧠 **核心思路**：不构建重型全局索引，而是以无状态、零预处理方式直接查询编译产物，按需提取和检索代码关系。
- 📦 **Deflate 直接探测**：通过探测 Deflate 比特流、构建密集 Huffman 查找表，在不触碰无关数据块的情况下提取核心元数据。
- 🔍 **利用 R8 优化**：R8 的确定性常量重定位与指令去重会形成高度集中的物理布局，Droid ASC 将其武器化以实现极快的跨 DEX 代码搜索。
- ⚡ **O(1) 指令定位**：设计常量时间方法解析原语，将原始字节码偏移映射回方法，无需构建重型映射表。
- 🧩 **按需反编译**：命中目标后仅提取特定字节码及其依赖，在内存中动态重建最小且自洽的 DEX，用于即时反编译。
- 📊 **实测性能**：在 352MB 商业 APK 上，全局交叉引用搜索耗时 1.79 秒，目标类反编译耗时 177 毫秒，仅用 141MB RAM。
- 🛠️ **安装方式**：支持 `pip install droidasc`，或从源码 `pip install .`，安装后全局可用 `droidasc` CLI。
- 🧰 **CLI 子命令**：包括 `getclass`、`listclass`、`getmanifest`、`findrefs`，分别用于定位反编译类、列出类、解析 Manifest、查找字符串/类型/方法/字段引用。
- 📝 **常用示例**：如 `droidasc getclass app.apk Lcom/poc/Main; -o Main.java`、`droidasc listclass app.apk --prefix com.poc`、`droidasc findrefs app.apk method onCreate --class com.poc.Main` 等。
- ⭐ **项目信息**：GitHub 上约 1.9k stars、266 forks、4 watchers、76 commits，采用 Apache-2.0 许可证。
- 🙏 **致谢**：基于 Androguard 项目提供的 Android 逆向与 DEX 分析基础，并感谢赞助者支持。

---

### [](https://github.com/IceMoonHSV/TATS?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - IceMoonHSV/TATS: Token Analysis and Tracking System · GitHub](https://github.com/IceMoonHSV/TATS?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

TATS（Token Analysis and Tracking System）是一个用于从 Burp Suite、mitmproxy 或 Chrome DevTools Protocol 捕获中跟踪 OAuth 2.0、OIDC 与 Microsoft Entra ID 令牌的工具，将令牌统一存入 SQLite，并通过本地 Web 仪表盘进行筛选、生命周期可视化与重放导出。它面向 Microsoft 365/Entra 生态（FOCI、BroCI/NAA、ESTSAUTH、entrascopes.com）优化，适合研究、教育和部分安全测试场景。

- 🧭 支持三种摄取来源：Burp XML、mitmproxy `.mitm` 流文件、Chrome/Edge CDP 实时流量（HTTP 与 WebSocket）。
- 🗄️ 所有数据进入单一 SQLite 数据库；`--append` 可合并多次捕获，令牌 UPSERT 累积，`source_tag` 记录来源。
- 📊 内置 stdlib Web 仪表盘，轮询数据库并近实时刷新；核心路径无专有依赖，mitmproxy 为可选依赖。
- 🧠 自动分类 access/refresh/id token，解码 JWT header/payload，识别 ESTSAUTH 等 Microsoft 会话 cookie。
- 🔗 检测 Microsoft FOCI 与 BroCI/NAA，并可通过 `--enrich` 从 entrascopes.com 解析 appid/azp/aud GUID。
- 🧩 仪表盘包含 Summary、Users、Token validity、Clients、Audiences、Tenants、Hosts 等卡片。
- 🛡️ 安全检查：特权 scopes/roles、audience/host 不匹配、amr、CAE、PoP、step-up auth、acr。
- 🔄 Refresh-token chains 展示轮换谱系、最长链、空闲 refresh token、Δ scopes 与特权扩展告警。
- 📋 Tokens/Exchanges 标签支持排序、多选、图谱高亮/隔离、序列图、行内展开 JWT 与事件。
- 📤 支持 CSV/JSON 导出、URL hash 保存筛选状态、WebSocket 帧令牌扫描。
- 🕵️ 默认仅存令牌 SHA-256 指纹和 12 字符前缀；解码后的 JWT claims 默认原文存储，需视为敏感数据。
- 🧹 `--redact-claims` 用稳定哈希替换 PII claims；`--store-tokens` 才保存完整令牌并启用重放功能。
- 🚀 快速使用：`tats ingest ...` / `tats mitm ...` / `tats cdp ...` / `tats serve ...`。
- 🖥️ 子命令包括 ingest、mitm、cdp、serve；serve 只读，可安全与正在运行的捕获并行。
- 🌐 CDP 支持 `--launch-chrome` 自动启动浏览器，浏览器级附加可跟踪现有和运行期间新开的标签页。
- 🧾 开启 `--store-tokens` 后可复制 raw/Bearer/curl、下载 JSON、导出 roadtools token cache，并有命令预览。
- 🔐 Web UI 无认证，暴露 claims、指纹、时间线与图表；若存完整令牌还可通过 API 导出，需绑定可信地址。
- 🧱 架构：各来源 → Tracker → ingest_to_db → SQLite → Store → `/api/data` → dashboard；数据库 schema v4。
- ⚠️ 限制：不支持 Burp `.burp` 项目文件、不做 TLS 拦截或 JWT 签名验证、CDP 不递归 OOPIF/worker、不透明令牌可能误报。
- 📦 Python 3.10+，可 `pip install .[mitm|test|all]`；含示例 fixture 与 pytest 测试套件；GPL-3.0 许可证。

---

### [](https://github.com/Q00/ouroboros?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - Q00/ouroboros: Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more. · GitHub](https://github.com/Q00/ouroboros?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

Ouroboros 是 Q00 开源的 Agent OS，面向可重放的 AI 编程工作流：通过规范优先、访谈门控、分阶段评估和进化循环，把模糊需求转化为可验证、可审计的代码库，并支持多种 AI 编码运行时。

- 🧠 核心定位：将非确定性 agent 工作变成可重放、可观测、受策略约束的执行合约，替代临时提示词。
- 🏗️ 三层栈：ourocode 终端 Shell、ouroboros-plugins 领域应用、ouroboros 核心 OS（Seed、Ledger、MCP、Runtime）。
- 🔁 主循环：Interview → Seed → Execute → Evaluate → Evolve；评估输出会反馈为下一代输入。
- ❓ 苏格拉底访谈：暴露隐藏假设并量化歧义；绿色项目看目标、约束、成功标准，棕地项目增加上下文清晰度。
- 🚧 歧义门：Ambiguity ≤ 0.2 才允许生成 Seed，否则需显式 force。
- 📜 Seed：将访谈答案结晶为不可变规范，包含验收标准、本体和约束，锁定意图后再写代码。
- 💎 Double Diamond：Discover → Define → Design → Deliver，先收敛本体，再收敛交付。
- ✅ 三阶段评估：Mechanical（$0）→ Semantic → Multi-Model Consensus。
- 🧬 进化收敛：本体相似度 ≥ 0.95 时停止；最多 30 代，并检测停滞、振荡、重复反馈等模式。
- 💸 PAL Router：Frugal 1x → Standard 10x → Frontier 30x，失败自动升级、成功自动降级。
- ♻️ Ralph：跨会话持久运行进化循环，EventStore 重建谱系，机器重启后继续直到收敛。
- 🧑⚖️ 多代理系统：九大脑加 12 个专用代理，共 21 个，按需加载，包括访谈者、本体论者、Seed 架构师、评估者、反方、黑客、简化者、研究者、架构师等。
- 🖥️ 多运行时：支持 Claude Code、Codex CLI、GitHub Copilot CLI、OpenCode、Hermes、Gemini、Kiro、Pi、OMP、Zcode、Goose、GJC、Antigravity、Grok 等。
- ⚙️ 安装方式：macOS/Linux/WSL2 用 curl 脚本，Windows 用 PowerShell；也支持 pip/uv/pipx/Homebrew 和插件安装；需 Python ≥3.12。
- 🧰 常用命令：ooo setup、ooo interview、ooo auto、ooo run、ooo evaluate、ooo evolve、ooo status、ooo ralph、ooo unstuck、ooo tutorial 等。
- 🔌 DeepSeek 支持：可用 --llm-backend dsh，或安装 dsh-ouroboros 插件，在 DeepSeek Harness 中直接运行。
- 🏛️ 架构模块：bigbang、routing、evaluation、evolution、resilience、observability、persistence、orchestrator、core、providers、mcp、plugin、tui、cli。
- 📈 社区与许可：MIT 许可，约 6.1k stars、612 forks；明确与加密货币及另一同名项目无关联。

---

### [](https://github.com/apowerb/apowerb?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - apowerb/apowerb: The open-source agentic framework to build, orchestrate, and operate production AI agents. · GitHub](https://github.com/apowerb/apowerb?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

apowerb 是 thaink² 开源的 agentic 框架，用于构建、编排和运营生产级 AI 代理；本仓库提供开源核心，计费、消费分析、身份提供商登录、MFA、评估、监督界面、组织管理等商业模块单独提供。

- 🚀 项目定位：构建、编排、运营生产 AI agents 的开源核心框架。
- 🧩 开源范围：管理面板包含用户、组、权限、MFA 强制执行；组织管理、计费、评估、监督屏幕等属于商业砖，路由可能返回 404。
- ⚡ 快速启动：克隆 apowerb-hosting，复制 .env，生成密钥，用 Docker Compose 启动；前端在 localhost:3000，API 在 8000。
- 🧰 源码安装：需要 Python 3.13+、PostgreSQL、UV；通过 uv sync 安装依赖。
- ⚙️ 必需配置：DB_HOST、DB_NAME、DB_USER、DB_PASSWORD、ENCRYPT_KEY；可选配置包括 JWT、公共 URL、CORS、OAuth、Pub/Sub、S3、编排器、扩展模块。
- 🔐 安全配置：APP_PUBLIC_URL 会影响密码重置、邮件验证、回调与 CORS；CORS_ALLOWED_ORIGINS 自动推导可能放宽安全策略。
- 🏗️ 核心功能：FastAPI REST、Google ADK、LiteLLM 多模型、多模式编排、子代理、31 个工具模块、RAG、Text-to-SQL、Webhooks、OAuth、SSE、Artifacts、Agent Hub、调度运行、bug 报告、监督、可撤销会话、PostgreSQL 自动迁移、加密、CLI。
- 🧠 编排能力：支持 base、parallel、sequential、loop，以及层级式 sub-agents 组合。
- 🔌 工具生态：Google Workspace、Microsoft 365、数据库/text_to_sql、RAG/memory、邮件/营销、S3、可视化、web_search_mcp、thaink2。
- 🔄 Webhooks：支持 Gmail Pub/Sub 与 Outlook Graph API 推送触发代理；提供订阅 CRUD、日志、自动续订，后台每 6 小时续订即将过期订阅。
- 📚 RAG：可索引文件、URL、数据库、自然语言查询、S3；支持轮询和 SSE 进度，并含路径穿越、SSRF、HMAC 校验防护。
- 🗄️ Text-to-SQL 与 SSE：自然语言转 SQL；SSE 覆盖代理逐 token 输出、RAG 进度、实时通知。
- 🛡️ 监督与会话：可审计会话列表与 trace，按调用者可读范围授权；支持可撤销会话和持久会话上下文。
- 🧾 计费与计量：Stripe 与计费逻辑属商业砖；核心包含 token 计量 llm_usage，共享默认模型有月度配额与上限，超限以 402 拒绝。
- ⏰ 调度运行：cron 式调度交给外部 orchestrator，可选 th2etl 或 mage；支持 @hourly、@daily、@weekly、@monthly 等预设。
- 🏪 Agent Hub：支持发布代理和克隆 Hub 代理，便于跨用户/组织复用。
- 🧱 API 与架构：路由族覆盖 auth、users、bug-reports、agents、adk、tools、skills、workflows、superagents、rag、artifacts、files、data-lake、hub、integrations、emailing、webhooks、notifications、supervision、scheduler、BI、share、api-keys、config、health。
- 🗃️ 数据模型：包括 user、integrations、webhook_subscriptions、webhook_logs、notifications、transactions、credit_purchases、llm_usage、BI、shared_conversations、oauth_states；ADK sessions/events 由 Google ADK 管理。
- 🤖 模型支持：通过 LiteLLM 支持 Anthropic、OpenAI、Mistral、Google、Azure AI Foundry、OVHcloud 等；Azure Foundry 使用 azure_ai/ 前缀配置。
- 🧪 开发与排错：开发依赖含 pytest、ruff；常见错误码包括 400、401、403、404、413、422、500、503。
- 📄 许可：Apache License 2.0，版权 2025-2026 thaink²；商业砖单独授权，商标不随代码许可证覆盖。

---

### [GitHub - IgnaceMaes/redis-lua-py：将 Redis Lua 脚本编写为真正的 Python 函数，而非字符串。 · GitHub](https://github.com/IgnaceMaes/redis-lua-py?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [GitHub - IgnaceMaes/redis-lua-py: Write Redis Lua scripts as real Python functions, not strings. · GitHub](https://github.com/IgnaceMaes/redis-lua-py?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

redis-lua-py 是一个让开发者用真实 Python 函数编写 Redis Lua 脚本的库：脚本在模块导入时编译为 Lua，并通过 EVALSHA 发送到 Redis，同时支持 mypy 类型检查、同步/异步 redis-py 与 coredis，并提供生成、测试和开发工具链。

- 📌 项目信息：IgnaceMaes/redis-lua-py，MIT 许可，约 5 stars、30 commits；README 提供文档、快速开始、API 参考和更新日志。
- 🐍 核心用法：用 `@script` 装饰模块级 Python 函数；函数体不由 Python 执行，而是作为源码读取并编译成 Lua。
- ⚡ 编译与发送：脚本在导入时编译一次，通过 `EVALSHA` 发送；支持同步和异步 redis-py、coredis。
- 🧪 类型与编辑器：参数和返回值可被 mypy 检查，编辑器高亮、linter 可见；调用端返回 `CompiledScript[R]` 或 `Awaitable[R]`。
- 🧩 键与参数：标注 `Key` 的参数会进入 `KEYS`，便于 Redis Cluster 路由；`int`/`float` 会自动用 `tonumber` 包装。
- ✅ 编译期检查：Redis 命令名会对照命令表检查，拼写错误在编译时拒绝，而非脚本运行时才报错。
- 🔒 常量与二进制：模块级 `int`、`float`、`str`、`bytes`、`bool` 常量在导入时折叠为 Lua 字面量；`bytes` 双向透传，不做解码。
- 📄 可审计 Lua：每个脚本暴露 `.lua` 源码，包含生成头；哈希基于脚本体，路径相对项目根目录，使不同环境 SHA 一致。
- 🏗️ 库作者支持：`python -m redis_lua_py generate` 可生成仅依赖标准库的类型化函数模块；`--check` 可用于 CI。
- 🧱 Redis Functions：同一 Python 代码可编译为函数库，首次使用时 `FUNCTION LOAD`，并用 `FCALL` 调用，支持 `no-writes` 等 Redis 7 标志。
- ⚠️ 语义差异处理：处理或拒绝 Lua 与 Python 之间的差异，如真值、1-based 索引、`false`/`nil`、块作用域、`nil` 截断表等；不支持子集会在导入时报错并指向问题行。
- 🧪 测试方式：fakeredis 内嵌真实 Lua 解释器，可用进程内服务器执行脚本；安装 `uv add --dev "fakeredis[lua]"`。
- 🛠️ 开发流程：`uv sync`、`uv run pytest`、`ruff`、`mypy`；测试默认用 fakeredis，设置 `REDIS_URL` 可跑真实 Redis。
- 🔁 命令表维护：`src/redis_lua_py/_commands.py` 由 Redis 源码生成，可用脚本在 Redis 新版本发布后刷新。
- 📦 安装与依赖：`uv add redis-lua-py`；Python 3.10+，无依赖，需自带 redis-py 4.2+ 或 coredis。
- 📚 文档与协作：文档由 Zensical 构建；PR 使用 squash merge，标题遵循 Conventional Commits 并决定版本号与更新日志。

---

### [PyPy v8.0.0 发布 | PyPy](https://pypy.org/posts/2026/09/pypy-v800-release.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [PyPy v8.0.0 release | PyPy](https://pypy.org/posts/2026/09/pypy-v800-release.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

PyPy 团队发布 v8.0.0，这是继 2026 年 5 月后的重大版本，首次带来 Python 3.12 支持（beta 质量），并同时发布 Python 2.7 与 3.11 解释器。版本号提升主要因 Linux 构建迁移到 glibc 2.28，同时推进 cp312-abi3 兼容性。

- 🚀 PyPy v8.0.0 于 2026-09-19 发布，包含 PyPy2.7、PyPy3.11 和 PyPy3.12（beta）。
- 🐍 PyPy3.11 基于 CPython 3.11.16，可能是最后一个支持 3.11 的版本；PyPy3.12 基于 CPython 3.12.14。
- ⚙️ Linux 构建改用 manylinux_2_28（AlmaLinux 8、glibc 2.28、gcc14），tarball 至少需要 glibc 2.28，故主版本升至 8.0.0。
- 🔗 PyPy3.12 的 C 层支持 cp312-abi3：隐藏 PyPy 专用 ob_pypy_link，兼容 Py_LIMITED_API=0x030C0000，不再修饰有限 API 导出函数名。
- 📦 尚需导入机制识别 abi3.so，以及 pip/uv 等生态接受 cp312-abi3 wheels；正与 Cython、PyO3 合作。
- ⚡ RPython 代码生成改进：采用 computed gotos、更积极内联，并加入映射回 RPython 的源码注释，但性能提升有限。
- 🗑️ 放弃内部 HPy 后端，因其未成为新标准；代码仍保留，可通过构建选项启用。
- 🔍 恢复基于 clang 的 pyhdrdump，用于比较 PyPy 与 CPython 的头文件。
- 📥 推荐更新，下载见 https://pypy.org/download.html，完整变更见 changelog。
- 🙏 感谢捐助者与贡献者，欢迎参与；建议库维护者提供 CFFI 版本或用 cibuildwheel 构建 PyPy wheel。
- 🌍 PyPy 是 CPython 的即插即用替代，带 tracing JIT，支持 x86、ARM64 等平台，并有下游打包版本。

---

### [](https://www.meetup.com/pydata-boston-cambridge/events/316514602/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [Sept Meetup: Special AI Week Session, Wed, Sep 30, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-boston-cambridge/events/316514602/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

本次 PyData Boston - Cambridge 九月聚会为波士顿 AI 周特别专场，聚焦智能体、LLM 自托管与负责任 AI，需提前注册，现场不接受未注册者或临时访客。

- 📅 活动时间：9 月 30 日周三 18:30–21:30 EDT，地点在 Moderna HQ，325 Binney St, Cambridge, MA。
- ⏰ 提醒：不要早于 18:30 到达；18:30–19:00 为开门与网络交流时间。
- 🎤 主办与赞助：由 Ben B. 等 2 人主持，PyData Boston - Cambridge 举办，NumFOCUS 赞助。
- 🧠 首场演讲：Krithika Murugesan 讲“构建代理式 AI 系统”，涉及 LangGraph、LangSmith、CrewAI，以及 AI 代理推理、协作、工具使用、状态维护和复杂工作流。
- ⚙️ 第二场演讲：Sebastian Wallkötter 讲“(自)托管 LLM 背后的物理”，解释输出 token 为何更贵、批量 API 为何更便宜，以及算力、带宽、vRAM、K/V 缓存、上下文窗口、量化、GQA 和多请求批处理。
- ⚖️ 第三场演讲：Ananya Sharma 讲“检测与缓解自动抵押贷款中的偏见”，涉及代理变量、历史贷款差异、统计公平性测试、可解释性、模型治理与持续监控。
- 🗓️ 日程概览：19:00–19:10 介绍；19:10–19:35 第一讲；19:35–20:00 第二讲；20:00–20:30 休息；20:30–20:55 第三讲；21:30 结束。
- ⚠️ 入场要求：必须准确填写注册表才能进入场地；不接受客人或未注册者，未注册者会被拒绝入场。
- 📜 行为准则：所有 NumFOCUS 相关线上线下活动均受 PyData 行为准则约束。
- 📣 招募信息：欢迎报名演讲；PyData 活动免费开放，持续寻找赞助商和场地支持，可联系 boston@pydata.org。
- 🏷️ 相关主题：Cambridge, MA 活动、机器学习、Python 数据科学、R、Python、Julia 编程语言。

---

### [](https://www.meetup.com/pydata_seattle/events/315789388/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [PyData Seattle: AI for Climate and Earth, Wed, Sep 30, 2026, 5:00 PM   | Meetup](https://www.meetup.com/pydata_seattle/events/315789388/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

PyData Seattle 将举办“AI for Climate and Earth”混合活动，聚焦 AI、开源软件与公共数据如何应对气候和环境挑战，包含实用演讲、现场演示与社区项目。

- 🗓️ 时间：9月30日（周三）17:00–19:00 PDT
- 🏢 形式：线上线下混合；线下在华盛顿大学 eScience Institute 的 WRF Data Science Studio，线上链接仅参会者可见
- 👤 主办：PyData Seattle，主持人为 DEBJYOTI P.
- 🌍 核心主题：卫星数据、开放模型、地理空间 AI、预测，以及用于气候行动的 AI 智能体
- 🛰️ 重点领域：卫星影像与地理空间 AI、地球与气候开放模型、野火/洪水/天气/水情预测、空气质量与能源系统智能、气候风险与适应
- 🤖 技术亮点：AI 智能体整合科学、传感器、卫星和政策数据；开源工具与公共数据集；气候科技初创与研究演示
- 👥 适合人群：软件工程师、数据科学家、研究人员、气候从业者、学生、创始人及开源贡献者
- 🤝 活动价值：强调实际工程、真实数据集、现场演示，并提供与气候和地球系统技术建设者交流的机会
- 🏷️ 相关话题：人工智能、气候变化、Python、开源、可持续发展

---

### [](https://www.meetup.com/pyladiessf/events/315897145/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [PyLadies SF at Snowflake SVAI Hub, Wed, Sep 30, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pyladiessf/events/315897145/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

PyLadies SF 将在 Snowflake SVAI Hub 举办以 Python、数据科学与社交为核心的线下聚会，探讨 AI 时代数据科学/分析角色如何演变，由 Joanne L. 和 Alla B. 主持，Snowflake 赞助，需提前在 Luma RSVP。

- 🗓️ 时间：9 月 30 日周三，太平洋夏令时 18:00–20:30。
- 📍 地点：SVAI Hub，135 Constitution Dr, Menlo Park, CA 94025。
- 🎟️ 报名：请通过 Luma RSVP：https://luma.com/693643qu
- 🧠 主题：AI 如何改变数据科学/分析，包括角色演变、必备技能、系统设计与团队适应。
- 🎤 Rose Tan，Snowflake 资深数据科学家：分享“How I AI: A Data Scientist's Perspective”，25 分钟演讲 + 5 分钟 Q&A。
- 🎤 Kasia Rachuta，Intuit 高级资深数据科学家：分享“The Data Scientist's Job in the Age of AI: What Changed, What Didn't”，25 分钟演讲 + 5 分钟 Q&A。
- 🔬 Lilinoe Harbottle，VC 支持初创公司生物医学工程数据系统研究员：分享“Trust in the Loop: System Design and Data Integrity in Regulated Environments”，30 分钟。
- 🧩 演讲重点：通过数据管道静默失败复盘，说明如何在受监管环境构建验证层，保障合规与生产系统可信。
- 🕕 暂定议程：18:00 签到交流；18:15 欢迎与社区公告；18:45 Rose；18:55 Kasia；19:20 Lilinoe；19:50 总结交流；20:30 结束。
- 👥 适合人群：数据科学家、数据分析师、数据工程师、产品经理、技术贡献者/领导者，以及关注 AI 与数据职业发展的人。
- 📜 参与需阅读并同意社区行为准则。
- 🏷️ 相关主题：Python、编程、软件开发、技术专业人士、女性科技等。

---

### [](https://www.meetup.com/pydata-trojmiasto/events/316414394/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [PyData Trójmiasto #45, Wed, Sep 30, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-trojmiasto/events/316414394/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

PyData Trójmiasto 第45期活动将在假期后回归，于9月30日18:00–20:00在格丁尼亚Tensor Z举办，聚焦AI发布沟通与智能体系统的真实实践。

- 📅 时间：9月30日周三，18:00–20:00 CEST
- 📍 地点：格丁尼亚 Łużycka 8b，Nordea Tensor Z 大楼
- 🎟️ 报名：需填写完整名和姓；入场请携带身份证件；RSVP截止活动前一天18:00
- 🅿️ 停车：大楼旁街道可免费停车
- 📧 联系：紧急沟通可发邮件至 kontakt@pydata-trojmiasto.pl
- 🗓️ 议程：18:00签到，18:05介绍PyData，18:10与19:00两场演讲，19:45社交交流
- 🎤 第一场：Karol Błaszczak 讲“From Changelog to Blog - AI Pipeline for Release Communication”
- 🤖 第一场要点：用LLM生成变更日志、发布说明、应用内引导、新闻通讯与博客等发布沟通内容；避免浪费时间与token，并减少幻觉、保持文档一致；介绍基于单智能体、多输入集的流程
- 🧠 第二场：Mateusz Hordyński 讲“Yet Another Year of Agents”
- 🛠️ 第二场要点：来自企业团队一年构建智能体系统的现场报告；哪些进入生产、哪些被悄悄删除；多智能体何时值得、何时只是“组织架构伪装成架构”；评估仍是瓶颈；大量“智能体工程”其实是上下文处理与权限管线；常见失败模式与模型选择无关
- 👤 讲者背景：Karol 负责Open Edge Platform文档，关注清晰表达，避免AI垃圾内容；Mateusz 是 deepsense.ai 高级ML技术负责人，涉及生成式AI、大规模数据平台、MLOps、RAG、智能体应用，并维护开源项目 db-ally
- 🏢 主办与赞助：由 Adrian B. 和 Łukasz G. 主持，PyData Trojmiasto；赞助方为 NumFOCUS，遵循 PyData 许可
- 🔗 其他：可加入活动聊天，提前与其他参会者交流；相关主题包括格丁尼亚活动、AI、深度学习、机器学习、大数据与Python

---

### [](https://www.meetup.com/pydata-norwich/events/316406374/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

**原文标题**: [PyData Norwich - September Meetup, Wed, Sep 30, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-norwich/events/316406374/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-764-september-24-2026)

PyData Norwich 九月聚会将在诺维奇 Digital Hub 举行，由 Chris J. 主持，内容为 Python 与数据科学相关演讲和讨论。活动氛围非正式，适合所有技能水平，会后可自愿前往酒吧继续交流，并需遵守 NumFOCUS 行为准则。

- 🗓️ 时间：9月30日周三 18:00–21:00 BST；18:00 开门，18:15–19:15 演讲，19:25 后前往酒吧。
- 📍 地点：Spaces Digital Hub, Townshend House, 30 Crown Rd, Norwich NR1 3DT；注意场地有变更。
- 🎤 演讲一：Hugh Evans（Aiven）——用 Python 和网页抓取绘制 PyData 社区地图，涉及地理编码、Folium 制图，并呼吁支持本地 PyData 小组。
- 🎤 演讲二：Sam Greenwood（独立顾问）——回顾 10 年 Python 数据工程，探讨数据工程与 Python 数据生态的演变关系。
- 🤝 活动非正式，欢迎各种技能水平，鼓励提问与讨论；可提前加入活动聊天，与其他参会者交流。
- 🍻 会后社交：19:25 起在 The Steam Packet Pub 喝饮品。
- 📜 行为准则：活动遵循 NumFOCUS Code of Conduct，如有疑问可联系组织者。
- 🎟️ 需报名参加；主办方为 PyData Norwich，主持人为 Chris J.。

---

