### [悼念：Tim Peters 1952–2026 - 核心开发 - Python.org 讨论](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [In Memoriam: Tim Peters 1952–2026 - Core Development - Discussions on Python.org](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

Python 社区沉痛悼念 Tim Peters（1952–2026）。Guido van Rossum 宣布他于 2026 年 7 月 15 日去世，并回顾了他从早期影响 Python 语言设计、撰写《Python 之禅》（PEP 20），到创造 Timsort 的深远贡献；众多开发者追忆其技术才华、幽默谦逊、耐心答疑和无私助人的精神。

- 🕯️ Guido 在 Python.org 发帖宣布 Tim Peters 已于 2026 年 7 月 15 日去世，称其影响力“怎么高估都不为过”。
- 🧘 Tim 最广为人知的是撰写《Python 之禅》（PEP 20）；“import this”至今仍可见，被许多人视为编程“北极星”。
- 🔢 早期他说服 Guido 让 Python 支持 int 与 float 混合算术，因为多数用户会期待这种直觉行为；此后持续参与语言设计。
- 💬 他在 Python 邮件列表中因大量耐心、严谨又幽默的解答而获绰号“Timbot”，常以 `<wink>` 等标记玩笑，并深入参与设计讨论。
- ⚙️ 2002 年他设计 Timsort 排序算法，用于 Python 列表，后被 Java 和 Android 采用；该算法兼顾常见、有利与最坏情况。
- 🧰 他的技术贡献遍布 CPython：打磨 pymalloc、优化 dict、夯实循环 GC 与生成器基础、改进 float/math、Karatsuba、doctest、difflib、pickletools、tabnanny 等。
- 🧑‍🏫 他曾任 PSF 董事（2001–2014），被视为早期核心开发的“守门人”和打磨者，强调简单、务实、可读性与严谨论证。
- 🤝 社区回忆他毫无架子、温和精确、乐于助人；Chris McDonough 称他是早期 Python 设计伙伴，其文化影响了许多开源项目。
- 🌍 许多开发者虽未与他谋面，仍深受其文字和代码影响；有人因读 `listsort.txt` 选择 Python，有人把“Now is better than never”当作座右铭。
- ⚖️ 部分悼念提到他晚年受到争议性对待与禁令并深受影响，但仍未改变帮助他人的意愿；社区认为他是不可替代的“伟大灵魂”。
- 🍽️ 个人轶事包括他与 Steve Holden 的友谊和中式午餐、在 Cray Research 与 Dragon Systems 的经历，以及为客户修复数据破坏性 bug 等故事。

---

### [PyPI 重新设计的项目页面现已上线，安全信号更清晰 - Python 包索引博客](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [PyPI's redesigned project pages with clearer security signals are now live - The Python Package Index Blog](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

overview summary
PyPI 已完成项目详情页与安全信号界面更新，新增安全标签、来源证明状态与警告机制，并重设计发布文件和历史页面，帮助用户更清晰判断包来源与安全风险。

- 🔐 PyPI 上线重设计后的项目详情页，重点提升安全信号展示与包元数据可读性。
- 🧾 新增“Security”安全标签页，集中展示发布文件的来源证明（provenance）与逐文件证明信息。
- ✅ 完整来源证明表示发布中 100% 文件带有证明，包括 PyPI Publish 和 SLSA Build Provenance。
- ⚠️ 无来源证明表示无法通过密码学验证文件来源，但不一定代表恶意，应结合维护者历史、发布模式等信任信号判断。
- 🚩 新增来源证明警告：不完整、不一致、来源变更、来源丢失，用于提示可能异常或冲突的发布情况。
- 📌 项目详情页顶部会显示来源证明警告，并与撤回、归档、预发布等状态横幅并列；隔离状态优先显示。
- 🗂️ 发布文件页支持搜索和筛选，显示每个文件的来源证明状态，并标记发布后超过 14 天上传的“迟到文件”。
- 🕘 发布历史页新增文件数量、来源证明状态和发布状态等信息。
- 📚 PyPI 用户文档扩展了包安全指南，涵盖源代码安全、来源核验、完整性验证、常见攻击防护和漏洞报告。
- 🔮 新安全标签页将作为未来证明类型和安全通知的入口，项目还发布了 OpenSSF 案例研究，并获得 OpenSSF 资助。

---

### [用Claude定位神秘哔声的来源](https://simonwillison.net/2026/Nov/9/mysterious-beeps/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Locating the source of a mysterious beep with Claude](https://simonwillison.net/2026/Nov/9/mysterious-beeps/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

Simon Willison 在 2026 年 11 月 9 日记录了如何用 Claude Code 构建 “Beep Locator”，通过多台设备 triangulate（三角定位）储物间里神秘间歇性蜂鸣声的来源。系统最终把声音定位到约 40 厘米范围内，帮助他找到一台电量耗尽、急需换电池的老旧一氧化碳探测器。文章还重点展示了如何让编码智能体“获得耳朵”，通过麦克风、WebSocket 和可热更新代码来感知并分析现实世界声音。

- 🐝 起因是储物间里出现间歇性蜂鸣，声音间隔太久，难以靠人耳判断来源，也不想翻遍所有箱子。
- 🛠️ 作者让 Claude Code 构建 Beep Locator：Python Web 服务器提供主界面，多台设备通过二维码/URL 加入并作为监听器。
- 📱 实际使用了两台 iPad、一部手机、一台 MacBook Pro 和一台 Surface Ultra 等设备参与监听与定位。
- 🔊 设备之间先播放声音来估计彼此位置；效果不够好，于是加入 “Rough mode”，允许手动拖动设备图标给出粗略位置。
- 👏 增加“拍手模式”用于测试：在不同位置拍手，系统会在地图上用菱形标记，帮助验证定位能力。
- ❌ 蜂鸣会在地图上显示为 X，并进入 “Sounds located” 日志；可依次回放各设备录到的声音，确认是否是目标蜂鸣。
- ✅ 确认“神秘蜂鸣”后，系统会监听该频率、测量间隔，并结合三角定位结果锁定最可能的位置。
- 📐 最终定位误差约 40 厘米，作者据此翻找特定箱子，发现一台老旧一氧化碳探测器需要更换电池。
- 📄 实现思路参考 2007 年论文 BeepBeep，利用双向感知、自记录和样本计数等技术做高精度声学测距与定位。
- 🧩 系统用 60 秒音频缓冲、FFT 和高通滤波检测蜂鸣；服务器让往返延迟最低的设备播放 chirp，再让各监听器上传蜂鸣前后片段用于对齐。
- 🤖 项目最初通过 iPhone 上的 Claude Code Cloud 和 Opus 5.5 启动，先让模型写出 problem.md，再逐步实现系统。
- 🔁 后续使用 Fable 5.2 边运行边修改；监听器支持通过 WebSocket 接收 installModule() 热更新代码，避免反复手动授权麦克风。
- 🧭 作者不断提出新功能：拖动设备、拍手测试、时间戳、回放录音、标记目标蜂鸣、重新布置设备、建议新增监听点等。
- 👂 文章核心洞察是“给 Claude Code 耳朵”：Claude 虽无原生音频输入，但可运行 JavaScript/Python 分析麦克风音频，并通过 WebSocket 动态调整监听系统。
- 🌍 类似案例还有用摄像头观察硬件屏幕状态来辅助调试，说明让编码智能体感知现实世界很有潜力也很有趣。

---

### [形式化 CPython](https://broyojo.com/python-formalization/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Formalizing CPython](https://broyojo.com/python-formalization/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

本项目用 AI 代理把 CPython 3.15.2 的 C 与 Python 实现逐行改写为 Lean，并进行差分测试、机器证明和独立复核，目的是为 Python 的实际行为建立可验证模型，同时发现真实缺陷。目前已有 4,071/28,393 个值得检查的函数通过复核（14.3%），生成 613,318 行 Lean、18,898 条定理与引理，并产生 418 份 bug 报告，其中约 55 个可用普通 Python 代码触发崩溃或内存破坏。

- 🎯 **动机**：Python 缺少精确规范，实际行为由 CPython 决定；形式化迫使明确边界情况，从而暴露隐藏 bug。
- 🧩 **四步流程**：逐行复制到 Lean；至少 5 万组棘手输入与真实 Python 差分测试；证明关键性质；由未参与工作的第二代理独立复核，通过才计数。
- 📦 **规模与覆盖**：1,539 个 Lean 文件、613,318 行、18,898 条定理/引理；语法规则覆盖 100%，内置类型 35%，解析器 31%，C 模块 19%，解释器核心 10%，标准库 8%。
- 🐞 **缺陷发现**：418 份 bug 报告，包括 129 个 C/Python 实现不一致、122 个其他问题、56 个错误结果、28 个崩溃、27 个内存破坏、26 个文档不符等。
- ⚠️ **弱证明问题**：早期追求广度导致少于一半函数通过复核，有文件仅 21%；正确但空洞的证明无法排除坏实现。
- 🔍 **复核关键问题**：每个证明都要问“一个坏版本是否也能通过”；发现已接受证明与真实 Python 不符时，会撤回依赖它的结果。
- 🧪 **真实反例**：JSON 编码器曾假设内存无限；pickle 在新进程首次编码会多 9 层调用；异常类型有继承关系；set 依赖内存地址不复用等。
- 💥 **典型 bug**：StrEnum 键调用 `setdefault` 崩溃；ElementTree 反向切片造成内存破坏；邮件 Message-ID 解析触发 `UnboundLocalError`；base32 `ignorechars` 静默错误；enum 错误被吞；C/Python pickle 递归深度不一致。
- 🛠️ **可复用方法**：固定精确版本；先列全量清单；复制代码而非文档；建模用户回调异常和中途修改；先测试再证明；保留反例；用真实 Python 校验已证明陈述；只计独立复核通过项。
- 🌍 **项目现状**：项目于 2026 年 10 月 29 日启动，受 `julia-in-lean` 启发；仍有很多 CPython 部分未建模，开放协作，欢迎建模 `todo` 函数或独立复核。
- 📌 **结论**：这是大规模 AI 辅助形式化的重要实证，既展示潜力，也说明严格差分测试、真实语义校验和独立复核不可省略。

---

### [So... Everyone and Their Agent Gets a Postgres Branch? (Even Your Worktrees) - YouTube](https://www.youtube.com/watch?v=U08rCMcblzk&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [So... Everyone and Their Agent Gets a Postgres Branch? (Even Your Worktrees) - YouTube](https://www.youtube.com/watch?v=U08rCMcblzk&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

该文本为 YouTube 网站页脚导航与版权信息，涵盖平台介绍、联系与法律条款、创作者、广告、开发者资源及新功能测试入口，并注明版权归属。
- 📄 提供“关于、新闻、版权、联系我们”等基本信息入口
- 🎬 汇总“创作者、广告、开发者”相关资源链接
- ⚖️ 列出“条款、隐私、政策与安全”等法律与安全说明
- ⚙️ 包含“YouTube 运作方式”和“测试新功能”入口
- ©️ 标注版权信息：© 2026 Google LLC

---

### [Python 配置：我们如何走到这一步，以及为什么它仍然令人头疼 - DEV Community](https://dev.to/niccolum/1-python-configuration-how-we-got-here-and-why-it-still-hurts-3kpn?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Python configuration: how we got here, and why it still hurts - DEV Community](https://dev.to/niccolum/1-python-configuration-how-we-got-here-and-why-it-still-hurts-3kpn?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

配置看似只是 `.env` 加 `settings.py`，但应用增长后会出现秘密泄露、类型错误、环境间复制粘贴等问题；配置不是一次性胶水代码，而是基础设施的一部分，应像业务逻辑一样认真设计。文章回顾 Python 配置方案的演进，提出七项现代配置要求与五类反模式，并指出“配置与代码分离”依然成立，但 12-Factor 的“一切走环境变量”已无法覆盖秘密轮换、动态配置和多源合并等需求。

- 🧱 硬编码时代：配置写在 `settings.py` 中，修改需完整发布；用 `if env == "production"` 分支切换值，调试困难。
- 📄 INI 与 `configparser`：配置从代码中分离，但所有值都是字符串，类型转换、必填校验和层级表达都很弱。
- 🧩 XML/JSON：XML 过于冗长；JSON 结构清晰但无注释、手写易错，秘密仍可能进入 Git。
- 🧾 YAML 崛起：可读性好、支持注释和层级，但缩进敏感、隐式类型转换和解析器差异带来新坑。
- 🐍 Python 模块作为配置：类型提示、继承和计算值很方便，但配置变成可执行代码，非开发者难改，运行时覆盖和热重载困难。
- 🌍 环境变量与 12-Factor：秘密不再进仓库、环境切换方便，但仍是字符串、无层级、全局可变且复杂类型表达别扭。
- ☁️ 12-Factor 的缺口：秘密轮换、按需读取、动态配置、功能开关、容器挂载秘密和多源合并等场景超出纯环境变量模型。
- 🧬 合并逻辑转移：Helm、ConfigMap、CI/CD 等基础设施承担合并，应用只看到最终值，来源追踪变得隐式。
- 📦 现代结构化格式：TOML 因类型严格和 `pyproject.toml` 流行；HCL、HOCON、Jsonnet、CUE、Dhall、Pkl 等提供更强表达力。
- 🧠 Schema 进入代码：dataclasses、Pydantic 等让配置结构成为类型和契约，解析、校验、合并逐渐围绕 schema 构建。
- 🏗️ 现代挑战：微服务、多环境、秘密管理、自动轮换、本地开发兼容和动态配置共同抬高配置复杂度。
- ✅ 七项要求：多源读取、可控合并、类型安全、值校验、清晰错误、schema 级秘密标记、来源调试。
- 🚫 五个反模式：可变全局单例、把字典当配置、测试中 monkeypatch 配置、整份配置塞进一个 JSON 环境变量、魔法环境变量散落各模块。
- 🧪 结论：配置是应用与环境的契约，错误往往在生产暴露；应像业务逻辑一样测试配置、校验 schema、检查秘密泄漏，并按项目需求选工具而非看 GitHub 星数。
- 🔜 下一篇：将比较 `python-decouple`、Dynaconf、Hydra 和 `pydantic-settings` 在 2026 年对七项要求的覆盖情况。

---

### [目录](https://origintracer.app/excerpt/asyncio-internals/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Catalogue](https://origintracer.app/excerpt/asyncio-internals/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

本文以最小 asyncio 示例为主线，借助 pdb 逐步追踪 `asyncio.run`、事件循环、Task、Future、`await` 字节码与回调调度，揭示 asyncio 如何通过单线程协作式调度完成异步任务，并说明 Uvicorn 等 ASGI 服务器如何建立在这些原语之上。

- 🧭 文章通过 `main → task_two → task_one → asyncio.sleep` 的最小示例，逐帧观察 asyncio 初始化、任务创建、挂起、唤醒与关闭全过程。
- 🏁 `asyncio.run` 会创建 `Runner` 与事件循环，并把 `main` 协程包装成第一个 `Task-1` 注册到循环中。
- 🔁 `run_until_complete` 为 `Task-1` 注册完成回调作为停止条件，`run_forever` 设置运行状态并进入 `while True` 的 `_run_once` 循环。
- 🧱 事件循环核心结构包括 `_ready` 双端队列与 `_scheduled` 定时堆；`_ready` 存放待立即执行的 `Handle`，`_scheduled` 存放 `TimerHandle`。
- ⚙️ `_run_once` 从 `_ready` 弹出 `Handle` 并执行回调；首个回调是 `Task.__step`，它通过 `coro.send(None)` 驱动协程运行。
- 🧵 `await` 会编译为 `SEND`、`YIELD_VALUE`、`RESUME` 等字节码；等待协程时可能直接进入其函数体，等待 Task/Future 时则把控制权交还事件循环。
- 🪄 `asyncio.create_task` 在运行中的协程里创建嵌套任务 `CustomTask-1`；当前任务通过 `_fut_waiter` 和 `add_done_callback(__wakeup)` 建立等待关系。
- ⏰ `asyncio.sleep` 创建 `Future` 与 `TimerHandle`，通过 `call_later` 调度 `_set_result_unless_cancelled`；定时器到期后标记 Future 完成并调度唤醒回调。
- 🔗 回调链依次唤醒 `CustomTask-1`，使其从 `sleep` 处恢复并完成 `task_one`，再调度 `Task-1` 唤醒；`Task-1` 恢复 `main`，最终以 `StopIteration` 表示协程完成。
- 🧹 主任务完成后，`_run_until_complete_cb` 停止循环；清理阶段创建 `Task-3`、`Task-4` 执行 `shutdown_asyncgens` 与 `shutdown_default_executor`，最后关闭事件循环。
- 🛠️ 调试 asyncio 时可重点观察 `events._get_running_loop`、`asyncio.all_tasks(loop)`、`loop._ready`、`loop._scheduled`、`task._fut_waiter` 与 `task._callbacks`。
- ✅ 结论：asyncio 是结构清晰的状态机；事件循环维护工作队列，Task 管理协程生命周期，`await` 本质是让出控制权并注册唤醒机制，从单线程中实现大量并发操作。

---

### [Django：介绍用于跳转到文件调试的 django-launch-editor -](https://adamj.eu/tech/2026/11/08/introducing-django-launch-editor/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Django: introducing django-launch-editor for jump-to-file debugging - Adam Johnson](https://adamj.eu/tech/2026/11/08/introducing-django-launch-editor/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

django-launch-editor 是一个新发布的 Django 扩展，可把调试错误页中的文件位置变成可点击链接，点击后直接在编辑器中打开对应文件和行列，减少手动复制路径、查找行号与切换窗口的步骤。

- 🚀 发布 django-launch-editor：让 Django DEBUG 错误页的文件位置变成链接，支持跳转到正确行；当 Python 能提供列信息时，也能跳到正确列。
- ⚙️ 配置简单：安装包，将 Django 的 `DEFAULT_EXCEPTION_REPORTER` 设置为该包的 reporter 类，并添加其 URL。
- 🛡️ 生产环境零开销：当 `DEBUG=False` 时，错误页不会添加任何内容，相关 URL 也不会注册。
- 🖥️ 同机可直接启动编辑器；若 Django 运行在 Docker 或远程服务器上，找不到本地编辑器，点击位置会弹出对话框并复制位置到剪贴板，便于粘贴到编辑器的“转到文件”提示框。
- 🧭 项目源于 profiling-explorer：作者希望从性能分析表格一键跳到代码，最初只加复制按钮，后来追求单击直达。
- 🔧 底层依赖 launch-editor-py：借鉴 npm 的 launch-editor 包，掌握编辑器检测与命令行参数；用 LLM 辅助移植，作者负责审查、测试和 Pythonic API 设计。
- 📦 profiling-explorer 1.3.0 已集成 launch-editor-py；launch-editor-py 提供 `launch_editor(file, line, column)` API 和 CLI，可用 `--guess` 检测编辑器，并支持用 `filename:line:column` 打开文件。
- 🌱 作者希望继续集成到 Django Debug Toolbar 等生态，甚至未来推动 Django 自身采用该依赖。

---

### [e-means：在相同损失下快 10 倍的 k-means - 博客](https://e-means.github.io/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [e-means: 10x faster k-means at equal loss - Blog](https://e-means.github.io/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

Meta FAIR 开源的 e-means 是一种现代、稳健的 k-means 算法，作为 Lloyd 算法的替代方案，在训练轮次和实际耗时上实现约 10× 加速，同时获得更低损失；其核心是小批量指数移动平均更新、缩放定律自动调参、死簇复活与专用内核优化，并已集成到 Faiss。

- 🚀 e-means 作为 Lloyd 算法的替代，目标是在更少 epoch 和实际耗时下取得更低均方误差。
- ⚙️ 采用小批量指数移动平均（EMA）更新质心，相比梯度下降更稳定，质心始终位于已分配点的凸包内。
- 🧠 无需额外超参数调优：批大小和步长由缩放定律根据数据规模 n、簇数 k、训练轮次 T 自动确定。
- 🧩 加入新初始化、余弦调度衰减、收尾阶段和死簇复活；死簇通过按规模比例拆分大簇来复活，比从批次随机重采样更有效。
- 🏃 广泛规模与数据集上，e-means 用 1.2–3 个 epoch 达到 Lloyd 25 个 epoch 的测试损失；GPU 相比 Flash-KMeans 实际耗时降低 10–45×，CPU 相比 Faiss 降低 8–15×。
- 🎯 Lloyd 是 e-means 在整批 B=n、步长 α=1 时的特例，但该极端设置高度次优；最低损失沿“更大批量配更大步长”的对角带分布。
- 🕳️ 小批量噪声帮助逃离局部极小值；多个玩具数据集 200 次启动中，e-means 卡在病态配置的比例显著低于 Lloyd。
- 📊 在 24 个嵌入/合成数据集与配置上验证，并对 234 个配置、16 个数据集（10 万到 1 亿点）进行对比。
- 💻 代码已集成在 Faiss：`faiss/contrib/e_means`，提供 `Emeans`/`NumpyEmeans`，默认训练 5 个 epoch；论文为 arXiv:2611.09501。
- 📝 使用时应引用 Bessa 等 2026 的论文《e-means: outperforming k-means (in one-tenth the epochs)》。

---

### [mizu: thread-speed parallel R and Python over shared memory :: Posit Open Source](https://opensource.posit.co/blog/2026-11-05_mizu-0-1-0/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [mizu: thread-speed parallel R and Python over shared memory :: Posit Open Source](https://opensource.posit.co/blog/2026-11-05_mizu-0-1-0/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

文章介绍了 libmizu、mizu 和 pymizu：它们通过共享内存为 R 与 Python 带来接近线程速度的异步与并行计算能力，把任务往返开销从约 100 微秒降至不足 1 微秒，并支持向量、数据框和 Arrow 表在进程间及 R/Python 之间零拷贝交换。

- 🚀 libmizu 是 C 核心库，mizu 是 R 包并已上 CRAN，pymizu 是 Python 包并已上 PyPI；三者均处于实验阶段。  
- ⚡ 在 Apple M4 Pro 上，任务往返耗时约为 R 0.8 微秒、Python 0.7 微秒、C 核心 0.4 微秒，而基于套接字的 mirai 或 ProcessPoolExecutor 约为 100 微秒。  
- 🧵 Pool 提供 submit、collect、map 等接口，任务提交后立即返回句柄；建议一次创建池并复用，避免反复启动工作进程。  
- 🔄 R 与 Python 使用同一通信格式，可直接互操作；向量、矩阵、数据框和 Arrow 表以零拷贝视图跨语言传递，并可对接 NumPy、polars、pyarrow、pandas。  
- 🗺️ 工作进程可访问自己的池，因此支持“映射中再映射”，避免死锁，比过去的分层池方案更方便。  
- ⏳ 提供事件驱动异步能力：R 侧支持 promise、later、promises 和 Shiny；Python 侧支持 asyncio 的 await 与 async for。  
- 📊 基准显示流水线吞吐可达 R 83.3 万任务/秒、Python 239 万任务/秒；四工作进程映射 2000 个小任务约 5.0 毫秒（R）和 4.3 毫秒（Python）。  
- 🧪 在四类建模工作负载中，mizu 相对顺序执行取得约 6.7 至 8.1 倍加速，文中称其明显优于对比的 mirai；但受 Amdahl 定律限制，12 个工作进程最多约 8 倍加速。  
- ⚠️ 主要限制包括：API 仍可能变化；工作进程看不到主会话环境；函数、公式等语言对象不能跨语言传递；小值低于阈值仍会复制；mizu 不替代面向分布式计算的 mirai。  
- 🧭 设计上 mizu 从 mirai 和 mori 演进而来，强调 C 核心与 R/Python 对等绑定；作者称实现借助 AI，但前期有三个月研究设计和三个月工程实现，并欢迎社区反馈与生态集成。

---

### [Deciphering Glyph ::
        Why You Should Care About The Political Project of Twisted
      ](https://blog.glyph.im/2026/11/the-project-of-twisted.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Deciphering Glyph ::
        Why You Should Care About The Political Project of Twisted
      ](https://blog.glyph.im/2026/11/the-project-of-twisted.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

Twisted 最初是文字角色扮演游戏引擎的网络组件，后来剥离游戏部分、保留邮件、AIM、DNS、SSH 等协议实现，至今已近 30 年。文章回顾它从 Python 首选事件驱动 I/O 库到被 asyncio 削弱地位的变化，并解释作者所称的“政治项目”：降低个人自建互联网服务的门槛，用内存安全语言、统一范式、内置测试和可缩放工具，帮助人们理解并掌控自己的网络服务；作者也坦承 Twisted 远未实现这一愿景，并呼吁贡献者。

- 🎮 起源：Twisted 源于文字 RPG 引擎的网络部分，游戏未做成，留下邮件、AIM、DNS、SSH 等协议实现。
- ⚙️ 地位变化：它曾是 Python 最重要的长期维护事件驱动 I/O 库；asyncio 进入标准库后，其不可替代性下降。
- 🧰 现状：仍包含 SSH、邮件、DNS、Web（含 WebSocket）等客户端/服务器，但也可由其他包拼装替代。
- 🎯 今日用途：适合需要多种协议的新网络服务，如同时做 HTTP、DNS、抓包和自定义 SSH；测试确定性和 GUI 接入仍有优势。
- 🏛️ 核心目标：尽可能“祛魅”网络软件运行方式，让人以人的尺度构建面向互联网的系统。
- 🛡️ 技术取向：使用内存安全语言和良好错误处理，统一范式、内置测试工具，设计上可缩小到普通笔记本运行。
- 🧭 自主性：在少数巨头控制算力供应链的背景下，个人仍可通过域名、低成本 VPS、自建 DNS 等保留对自己服务器的控制权。
- 🧱 降低门槛：自建邮件、Web、终端服务器需要深厚专业知识，而多项目、多语言、风格不一的运维负担放大了难度；Twisted 试图整合协议与认证层来减少开销。
- 🧠 为何事件驱动：对单个人而言，理解 async/await（或 Deferred）的 I/O 多路复用并发，通常比理解多线程池应用更容易。
- 🤝 为何不用 AI：不是个人偏好，而是为了构建人们能亲自理解、风格一致、可拆解分层的引擎；它是为人而建，不是为 AI 而建。
- 🌐 愿景口号：“Building the Engine of Your Internet”——给你一个足够小、可个性化、无需庞大管理工具即可起步的互联网引擎。
- 🧪 现实案例：作者不再用 twisted.names 托管 DNS，twisted.mail 也不足以独立做邮件托管；但文章本身经由 twisted.web、TLS 和 conch SSH 在简单 Docker 中高可靠运行。
- 📣 呼吁：Twisted 距愿景仍很远，作者欢迎志愿者联系参与贡献。

---

### [用 Python 逐层构建 AI 智能体沙盒](https://muhammadraza.me/2026/building-agent-sandbox-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Build an AI Agent Sandbox in Python, Layer by Layer](https://muhammadraza.me/2026/building-agent-sandbox-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

文章记录了作者用 Python 从零为 AI 编码代理构建沙箱的过程：在原有容器运行时上逐层加入六道防护，并用同一组攻击验证每层效果。核心结论是：命名空间、seccomp、Landlock、网络代理和 cgroup 能挡住大量常见逃逸与破坏，但共享内核、工作区密钥、环境变量和“稍后执行的文件”仍是主要风险；生产级沙箱还需 gVisor 或 microVM 等更强隔离。

- 🧱 沙箱与容器的区别：容器隔离“可信进程”，沙箱要容纳“不可信进程”；代理可能只是执行 README、网页或 issue 中的恶意指令。
- 🗡️ 攻击测试覆盖：读取 `~/.aws/credentials`、写 `~/.bashrc`、杀宿主进程、`ptrace`/`io_uring`/嵌套用户命名空间、访问云元数据地址、抽象 Unix socket、fork bomb 和内存耗尽。
- 🪜 六层防护依次为：无根用户/PID/IPC/UTS 命名空间、新根文件系统与 `pivot_root`、`no_new_privs` + seccomp、Landlock 路径规则、私有网络与代理、cgroup 资源限制。
- 🔍 关键发现一：第 1 层虽隐藏宿主 PID，但文件攻击仍全部成功；第 2 层新根才让秘密读取返回 `ENOENT`、外部写入返回 `EROFS`。
- ⚠️ 关键发现二：`pivot_root` 后若漏掉 `umount2`，普通路径看似安全，但 `/..` 可进入旧根并读回密钥；只测显眼路径会误判沙箱有效。
- 🛡️ 第 3 层 seccomp 挡住 `ptrace`、`io_uring`、`keyctl` 和嵌套用户命名空间；但它是黑名单，未列出的系统调用仍可到达内核。
- 📂 第 4 层 Landlock 能拦截“通过宿主传入目录句柄读取秘密”的攻击；这类问题与 CVE-2024-21626 类似，新根本身无法防御。
- 🌐 第 5 层网络隔离阻止直连和元数据地址；代理必须同时检查主机名解析后的 IP，否则批准域名可能解析到 `169.254.169.254` 并泄露云凭据。
- ⚙️ 第 6 层 cgroup 限制内存、CPU 和进程数；`pids.max` 阻止 fork bomb，`memory.swap.max=0` 才能避免内存限制被 swap 绕过。
- 🧩 层级顺序很重要：cgroup 要先建，因为新根会隐藏 `/sys/fs/cgroup`；seccomp 和 Landlock 要后装，因为它们会禁止挂载；启动前还要关闭继承的文件描述符。
- 📊 全部六层仅增加约 4ms 启动开销；40 项检查在多种配置下运行两遍，所有正常控制项均通过，但“允许”结果必须用随机值证明攻击确实成功。
- 🚧 仍无法防御：工作区内的 `.env` 密钥、继承的环境变量、`.git/hooks`/Makefile/包脚本等稍后执行的代码、代理无法检查 TLS 内容，以及所有规则最终仍由同一个宿主内核执行。
- 🖥️ 生产沙箱不只靠这些层：gVisor 用用户态内核，Firecracker 等 microVM 给每个沙箱独立内核；Docker 的代理沙箱也采用 microVM，但挂载哪些文件、允许哪些主机等策略仍决定多数真实泄露。
- 🧪 代码是教学用途，作者强调“测试通过证明不了什么，直到你亲眼看到它失败”；最难的问题往往不在内核，而在工作区密钥、环境令牌和明天才运行的钩子。

---

### [AI 编程代理会弄错的 7 件事（因为是你纵容的）- YouTube](https://www.youtube.com/watch?v=oFtTodDCbkE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [7 Things AI Coding Agents Get Wrong (Because You Let Them) - YouTube](https://www.youtube.com/watch?v=oFtTodDCbkE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

该内容为 YouTube 页面底部导航与版权信息，主要提供平台介绍、合作资源、法律政策及功能测试等入口。

- 🏢 包含“关于”“新闻稿”“联系我们”等平台基本信息入口。
- 🤝 提供“创作者”“广告投放”“开发者”等合作与资源链接。
- 📄 列出“版权”“条款”“隐私”“政策与安全”等法律与政策入口。
- ⚙️ 说明 YouTube 的运作方式，并提供新功能测试入口。
- ©️ 版权声明为 © 2026 Google LLC。

---

### [Pandera 针对 Polars/Pandas 的 DataFrame 验证 - YouTube](https://www.youtube.com/watch?v=TvPr9Juw7gA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Pandera DataFrame validation for Polars/Pandas - YouTube](https://www.youtube.com/watch?v=TvPr9Juw7gA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

该内容主要是 YouTube 网站的页脚导航与版权信息，汇集了平台介绍、联系渠道、创作者与开发者入口、广告合作、法律条款、隐私与安全说明，以及新功能测试入口，并标注版权归属 Google LLC。

- 🧭 提供“关于、新闻、版权、联系我们”等基础导航链接
- 👥 包含“创作者、广告合作、开发者”等平台相关入口
- 📄 列出“条款、隐私、政策与安全、YouTube 如何运作”等法律与说明链接
- 🧪 设有“测试新功能”入口
- ©️ 版权声明为“© 2026 Google LLC”

---

### [Adopting Python 3.15's lazy imports: a 4× faster CLI, and where they didn't help — Namegarage blog](https://namegarage.com/blog/python-3-15-lazy-imports?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Adopting Python 3.15's lazy imports: a 4× faster CLI, and where they didn't help — Namegarage blog](https://namegarage.com/blog/python-3-15-lazy-imports?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

文章介绍了团队将后台系统迁移到 Python 3.15.2 后，采用 PEP 810 显式惰性导入（lazy imports）优化 CLI、TUI 和 MCP 服务启动速度的实践。CLI 的 `--help` 启动时间从约 1.31 秒降至 326 毫秒，提升约 4 倍；但 TUI 和 MCP 服务分别只提升约 20% 和 15%。团队没有全局启用惰性导入，而是通过 Lifeguard 静态分析与安全门禁逐条审核，并处理了测试补丁捕获、模块级表、默认参数、基类和 `try` 块等“惰性失效”场景。文章还分享了 `frozendict`、采样分析器的使用经验，以及可复用的测量与迁移建议。

- 🚀 **背景与目标**：后台系统有 CLI、Textual TUI 和 MCP 服务三个入口，启动都较慢；CLI 的 `--help` 约需 1.3 秒，因为主模块在导入时加载了站点生成器、注册商客户端和数据库层等大量依赖。
- 📏 **测量方法**：使用 `python -X importtime` 找出启动时最耗时的导入链，包括 `markdown-it`、`httpx2`、`asyncio`、DuckDB、`rcssmin`、Jinja2 和 PyYAML。
- 🧪 **全局惰性导入试验**：用 `PYTHON_LAZY_IMPORTS=all` 验证潜力，CLI `--help` 从 2,230 ms 降到 474 ms，TUI 从 3,615 ms 降到 209 ms，MCP 服务导入从 5,667 ms 降到 1,682 ms，但该数据负载很高，只能看比例。
- ⚠️ **未启用全局模式**：Lifeguard 在 801 个文件中发现 160 个文件存在可能受延迟影响的导入期副作用；例如配置模块导入时会从 `.env` 填充 `os.environ`，必须保持急切加载。
- 🔐 **安全门禁**：第一个 PR 先加入门禁而不加任何 `lazy` 语句；门禁运行 Lifeguard 0.7.0，并用 `ast` 检查每条惰性语句是否满足五条规则。
- 🧱 **门禁规则**：导入方不能是必须急切加载的模块；目标不能有可被延迟改变影响的导入期副作用；不能是导入方自身的急切依赖；有副作用的导入方不能延迟自身导入环中的模块；配置模块永不延迟。
- 🚫 **失败关闭**：门禁在未扫描到文件、Lifeguard 报错、报告不含项目模块、或允许列表条目未匹配任何惰性语句时都会失败；提交钩子会在 Python 文件、允许列表或锁文件变更时运行。
- 📝 **允许列表机制**：对必须延迟但不安全的模块，需要记录原因和 Lifeguard 报告的当前副作用；若副作用列表变化，门禁会失败并打印新列表，曾因此发现站点生成器新增导入期副作用。
- 🧪 **测试处理**：惰性 `from m import f` 会在首次使用时绑定名称，测试若先 patch `m.f`，之后可能一直保留 mock；团队在 `conftest.py` 中用 `sys.set_lazy_imports_filter` 让项目内惰性语句在测试中变急切，并用子进程测试验证真实惰性路径。
- 🧩 **惰性失效场景**：模块级字典/表在构建时查找工厂函数、默认参数在函数创建时求值、TUI 子类化 Textual `App` 需要先加载基类、以及 `try` 块内不允许 `lazy`，都会导致延迟失效。
- 📊 **最终效果**：CLI `--help` 从 1,314 ms 降至 326 ms，加载模块数 664→308；TUI 从 1,768 ms 降至 1,406 ms；MCP 服务导入从 3,341 ms 降至 2,827 ms，且 MCP 仍注册同样的 94 个工具。
- 💰 **保留成本**：`asyncio` 仍会因配置模块→凭据模块链在 `--help` 时加载；`rich.progress` 约 71 ms，但为第三方模块加允许列表容易因副作用变化而失败；没有运行时开关，回滚即 revert。
- 🧊 **`frozendict` 经验**：用内置不可变映射替换了 3 个 `MappingProxyType` 常量，并作为新常量映射规则；但没有转换已有 121 个模块级 `dict`，因为代码中约 530 个 `isinstance(x, dict)` 检查会失败。
- 🛠️ **工具兼容问题**：pyrefly 1.4.0/1.4.1 对 `frozendict.__init__` 类型推断有误，需要临时忽略；1.5.0.dev1 已接受；Ruff 和 ty 无问题；变更测试选择逻辑也需识别 `frozendict` 成员。
- 🔍 **采样分析器**：Python 3.15 提供 `python -m profiling.sampling`，可 attach、dump、replay、run；macOS 读取其他进程内存需提权，文档应让程序以用户身份启动，仅给分析器 `sudo`，避免输出文件和 `__pycache__` 变成 root 所有。
- 🙅 **未采纳的 3.15 特性**：PEP 661 哨兵值、PEP 798 推导式解包、PEP 728 封闭 `TypedDict`、TOML 1.1、base64 新填充选项等未带来足够收益或存在兼容性/链接稳定性问题。
- ✅ **迁移建议**：先用 `importtime` 排序累计耗时并阅读最大导入链；再用 Lifeguard 的 `LAZY_ELIGIBLE` 与 `LOAD_IMPORTS_EAGERLY` 报告判断可延迟模块；添加首个 `lazy from` 前先搜索测试中的 patch，并用过滤器与子进程测试保证测试和惰性路径都可靠。

---

### [GitHub - Insilico-org/plsi：个人长寿超级智能：面向 Grok Bot 的多智能体健康工具带 · GitHub](https://github.com/Insilico-org/plsi?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - Insilico-org/plsi: Personal Longevity Superintelligence: a multi-agent health toolbelt for Grok Bot · GitHub](https://github.com/Insilico-org/plsi?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

该仓库介绍 PLSI（Personal Longevity State Interface）——一个面向 Grok Bot 的多智能体个人长寿健康工具带：将健康记录转化为去标识化、代码归一化的事件日志，经版本化 State Map 投影为哈希状态文档，并让 Grok Bot 提出经筛查的行动及带评分、区间和依据的下一状态预测（含衰老时钟）。

- 🧬 **开源定位**：PLSI 是 MIT 许可的 Grok Bot 多智能体健康工具带（约 77 星、26 叉），聚焦个人长寿研究与教育，不提供医疗诊疗。
- 🗂️ **数据管线**：支持 FHIR、标准 CSV、甲基化数据、Grok 提取 JSON 等输入；经去标识化和 LOINC/RxNorm/UCUM 归一化后，写入仅追加事件日志。
- 🧮 **State Map 与状态文档**：提供 State Map 契约（JSON Schema/YAML）、注册表、选择器、映射器和故事线；将事件投影、单位转换后生成带哈希的状态文档，供机器人按哈希引用。
- 🤖 **多智能体团队**：以 Health、Research、Clinic 三个 Hub 及每位患者的 Ward Bot 为入口；共享核心 Worker（数据处理、健康顾问、挑战者、审核、数据控制等）和可选专家；复杂任务进入 Sessions 房间。
- 🔁 **交接与治理**：机器人负责判断，CLI 负责计算器、连接器、日志、代码门禁和评分器；所有计划先经 Challenger，离开本机的数据经代码门禁和 Data Controller，预测由 `plsi score` 评分。
- ⏱️ **衰老时钟与预测**：支持原生血液 PhenoAge、地图公式和 biolearn 甲基化时钟；输出带区间、依据、时间范围的下一状态预测，并报告校准与偏差。
- 🧪 **研究自动化**：`plsi research` 支持按主题组织问题、假设、发现（Obsidian 风格 Markdown）、研究项目及可选每日自动研究；所有结论由代码计算。
- 🎯 **靶点发现**：`plsi targets` 为研究人员生成基因靶点档案，汇集免费来源事实；评估必须每条声明都有来源，否则拒绝。
- 🌐 **Longevity Mothership**：用户可选择加入 Insilico 长寿研究计划；每周提交假名化（非匿名）数据包，仅含编码字段（码、数值、单位、月份、年份；无自由文本、无由年龄计算的值；仅性别、年龄段、族裔组），经门禁校验后发送。
- 🔐 **隐私与去标识化**：采用 `plsi-limited-v1` 配置；仅保留出生年份（90+ 仅年龄组）和性别，事件日期保留，属有限数据集而非 HIPAA Safe Harbor；路径、姓名、标识符等不入库。
- ✅ **同意与出口控制**：同意通过问题卡收集，长期批准可替代卡片；Mothership 加入记录同意文本版本，文本更新后打包会报 `CONSENT_OUTDATED`；发往 oracle 的文本仅由状态文档生成并留痕。
- 🧱 **包与分层**：包含 `plsi.life`、`plsi.map`、`plsi.policy`、`plsi.research`、`plsi.targets`、`plsi.mothership`、`plsi.clinic`、`plsi.vocab` 及 CLI；策略层不导入生命层，生命层不导入地图/策略层，以支持完全本地部署。
- 🧩 **可扩展性**：按最低层级扩展：新增地图 YAML、公式表达式，或经用户明确批准安装的扩展包；扩展只能增加不能替换，并记录来源版本。
- 🚀 **快速开始**：创建虚拟环境并安装后，使用 `plsi doctor`、`plsi init`、`plsi ingest`、`plsi maps select`、`plsi project`、`plsi report` 等命令；Grok Bot 用户从 `plsi.md` 开始。
- ⚠️ **免责声明**：PLSI 不诊断、治疗或开药，输出自动生成且可能错误；开始/停止/调整药物、补充剂或健康方案前应咨询临床医生，紧急情况联系当地急救。

---

### [GitHub - hedgerow-dev/coldframe: Low-interaction honeypot for supermarket refrigeration controllers (Danfoss AK-SM 800A, Dixell XWEB 500) · GitHub](https://github.com/hedgerow-dev/coldframe?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - hedgerow-dev/coldframe: Low-interaction honeypot for supermarket refrigeration controllers (Danfoss AK-SM 800A, Dixell XWEB 500) · GitHub](https://github.com/hedgerow-dev/coldframe?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

coldframe 是一个低交互蜜罐，用于伪装超市制冷控制器（Danfoss AK-SM 800A、Dixell XWEB 500），记录攻击者的连接、口令尝试和公开漏洞利用行为，但从不提供真实控制能力。项目以单个 Python 文件实现、仅依赖标准库，并支持容器化部署、日志分析与多种安全限制。

- 🧊 **目标场景**：2026 年攻击者利用默认密码和旧固件入侵欧洲联网制冷监控器并强制除霜；coldframe 模拟此类设备以收集威胁情报。
- 🎭 **双重伪装人格**：`danfoss` 模拟 AK-SM 800A 的 StoreView 登录、假仪表盘、XML API（`/html/xml.cgi`、`/xml.cgi`）及 HTTP/HTTPS；`dixell` 模拟 XWEB EVO 登录页和 XWEB 500 漏洞路径。
- 🧾 **登录与漏洞识别**：Danfoss 弱口令可登录并展示假制冷柜控制面板；CVE-2025-41450 “code of the day” 会记录但不放行；Dixell 使用 `/cgi-bin/login.lua`，`Admin/Admin` 可登录，5 分钟内 5 次失败锁定，并标记 CVE-2026-25085。
- 🛠️ **漏洞覆盖**：可识别 CVE-2023-25914/25915、CVE-2025-41450/41452、CVE-2021-45420、CVE-2026-25085 等公开利用请求，并在日志中标记 `exploit`。
- 🌡️ **可选 Modbus TCP**：提供假案例温度、设定点和除霜寄存器；默认关闭，因为真实 AK-SM 800A 仅用 Modbus 与自身柜控制器通信。
- 🚀 **快速启动**：`PERSONA=danfoss HTTP_PORT=8080 python3 -I honeypot.py`，请求以 JSON 行写入 stdout 和 `events.jsonl`；测试脚本会启动蜜罐并攻击自身。
- ☁️ **部署方式**：可用 `cloud-init.yaml` 在 Ubuntu 24.04 上快速部署；容器建议以 rootful Podman/Docker 运行，只暴露诱饵端口，限制 SSH 来源并阻断非必要出站流量。
- ⚙️ **关键配置**：`PERSONA`、HTTP/HTTPS/Modbus 端口、`LOG_PATH`、`FAVICON_FILE`、`INDEX_FILE`、`STORE_NAME`、`MAC_ADDRESS`；建议每次部署设置不同商店名和 MAC。
- 📝 **日志与报告**：记录 HTTP 请求、登录尝试、控制操作、XML 命令、TLS 错误和 Modbus 活动；`summary.py --hours 24 --ignore <自己的IP> events.jsonl` 可生成简短报告。
- 🔒 **安全设计**：不执行命令、不读文件、不转发流量；限制请求体、日志字段、连接数和空闲超时；容器以非 root、只读文件系统、无能力模式运行。
- ⚠️ **局限**：交互较浅，登录后仅见小仪表盘和少量 XML 命令；公开代码可被指纹识别；部分真实设备细节不公开，使用了合理猜测值；云主机 IP 可能被扫描器怀疑为蜜罐。
- 📄 **许可**：MIT 许可证；README 还列出了 Danfoss、Claroty、Synacktiv、Exploit-DB 等参考来源。

---

### [GitHub - homeassistant-ai/ha-mcp: Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants. · GitHub](https://github.com/homeassistant-ai/ha-mcp?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - homeassistant-ai/ha-mcp: Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants. · GitHub](https://github.com/homeassistant-ai/ha-mcp?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

ha-mcp 是一个让 Claude、ChatGPT 等 AI 助手配置和自动化 Home Assistant 的开源 MCP 服务器，目前在 GitHub 上获得 7.7k 星标、466 次分叉，采用 MIT 许可证。它提供约 87 个工具，能力覆盖设备控制、自动化、脚本、仪表板、备份、注册表管理等；与 Home Assistant 内置的、仅基于 Assist 的 MCP Server 不同，它定位在“配置、构建和调试”整个智能家居。推荐通过 HACS 或 Marketplace 安装 HA-MCP 集成，在进程内运行，并支持所有 Home Assistant 安装类型；此外还提供 app、Docker、PyPI/uvx 等多种部署方式，并强调每个客户端只能配置一种安装方式，以避免连接挂起。项目注重本地隐私、安全策略与只读模式，并配套 Agent Skills 提升 AI 生成的配置质量。

- 🏠 **核心定位**：用自然语言让 AI 助手配置、构建和调试 Home Assistant，而不只是控制已暴露的设备。
- ⭐ **项目热度**：7.7k stars、466 forks、3,518 次提交，采用 MIT 开源协议。
- 📦 **推荐安装**：通过 HACS 或 Home Assistant 2026.11+ 的 Marketplace 安装 HA-MCP 集成，在进程内运行完整服务器，支持 OS、Supervised、Container、Core 全类型，并要求 Home Assistant 2026.8.0+。
- 🔑 **账户配置**：可使用管理员长期访问令牌，或更安全地创建专用管理员账户，仅限本地访问。
- 🌐 **连接方式**：支持通过 Home Assistant Webhook 远程访问，也支持局域网直连端口 9584；两者默认关闭，可按需启用。
- 🧩 **其他部署**：提供 Home Assistant app、Docker、PyPI/uvx HTTP 服务器，以及本地 stdio（不推荐，存在已知传输问题）。
- ⚠️ **重要提醒**：每个 AI 客户端只能配置一种安装方式；同时配置多个入口，是连接挂起的常见原因。
- 🔧 **工具能力**：约 87 个工具，涵盖模糊搜索、批量设备控制、自动化、脚本、场景、仪表板、区域、分组、历史统计、摄像头快照、备份、更新、HACS 和注册表管理。
- 🔒 **安全机制**：提供只读模式开关、按工具启用或禁用、工具安全策略（用户审批）、自动编辑备份，以及 `/readonly` 只读连接 URL。
- 🆚 **与内置 MCP 对比**：内置集成只覆盖已暴露给 Assist 的实体和意图；ha-mcp 可管理全部实体，并支持创建自动化、编辑仪表板、追踪调试、管理辅助元素和备份等。
- 📝 **文件与 YAML 工具**：通过 HA-MCP File & YAML Tools 组件启用 YAML 编辑和文件读写删改，但需要开启 beta 功能标志。
- 🧠 **Agent Skills**：内置 Home Assistant 领域知识资源，帮助 AI 遵循最佳实践，避免过度依赖模板或选错辅助元素类型。
- 🔍 **工具发现模式**：`ENABLE_TOOL_SEARCH=true` 可将完整工具目录改为搜索式按需加载，适合小型本地模型，或会内联全部工具模式的客户端；支持按 URL 固定使用完整目录或搜索目录。
- 🧪 **开发与社区**：提供 dev 通道、完善的贡献指南、GitHub Discussions 和 Issue 跟踪，并有大量社区贡献者参与功能与修复。
- 🔐 **隐私承诺**：完全本地运行，当前无遥测；未来若加入匿名统计，将遵循 Home Assistant 分析设置并提前公告，不收集个人数据。

---

### [GitHub - django-hurricane/django-hurricane: The high-performance, Django-native application server. Zero-config production readiness, edge defense, and native asset serving for Docker, Cloud, and   Kubernetes. · GitHub](https://github.com/django-hurricane/django-hurricane?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - django-hurricane/django-hurricane: The high-performance, Django-native application server. Zero-config production readiness, edge defense, and native asset serving for Docker, Cloud, and   Kubernetes. · GitHub](https://github.com/django-hurricane/django-hurricane?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

django-hurricane 是一个高性能、Django 原生应用服务器，主打零配置生产部署、边缘防护、健康可观测性和静态/媒体文件原生服务，适用于 Docker、云环境与 Kubernetes。其新版本从 Tornado 迁移到基于 Rust Hyper/Tokio 的 Granian，显著提升并发性能与探针稳定性。

- 🚀 **全新引擎**：Hurricane 现由 Granian 驱动，基于 Rust 的 Hyper 与 Tokio，提供更快的 HTTP 处理、零拷贝 I/O 和 Rust 并发能力。
- 📈 **性能大幅提升**：基准测试显示峰值吞吐提升约 101%，P50 延迟降低约 49%，P99 延迟降低约 45%，并消除了 Tornado 时代的误判未就绪事件。
- 🔌 **零配置 WSGI/ASGI**：根据 Django 设置中的 `WSGI_APPLICATION` 或 `ASGI_APPLICATION` 自动选择运行模式，无需手动指定 `--mode`。
- 🛡️ **Fast-404 防护**：在网关边缘拦截 `.php`、`.env`、`.git`、`wp-*`、`xmlrpc` 等扫描请求，减少 Django 中间件、数据库和模板开销。
- 🚦 **请求限流**：默认启用内存令牌桶限流，基线为每 IP 每秒 10 次请求、突发 30 次，并支持解析真实客户端 IP。
- ☸️ **Kubernetes 原生探针**：内置 `/startup`、`/alive`、`/ready` 探针，分别检查启动任务、进程存活和数据库/请求积压状态。
- 🛡️ **探针端口隔离**：支持 `--probe-port` 将健康检查与业务流量分离，避免高负载时探针超时。
- 📊 **Prometheus 指标**：开箱即用暴露 `/metrics`，包含请求数、错误率、响应时间、线程饱和度和 Python 运行时指标。
- 📦 **静态与媒体文件服务**：通过 `--static --media` 直接提供静态资源和媒体文件，减少额外 Nginx 依赖。
- 🚀 **启动前迁移**：使用 `--check-migrations-apply` 在启动阶段执行待处理迁移，并通过 `/startup` 探针控制流量接入。
- 🐳 **部署友好**：提供 Docker Compose 与 Kubernetes 示例，可替代 Gunicorn、Uvicorn 和部分 Nginx 场景。
- 🛠️ **开发与支持**：项目采用 `uv`、`ruff` 等现代工具，由 Blueshoe 维护，并提供 Discord、LinkedIn 和商业支持渠道。

---

### [GitHub - synchopate/llama-modchip: Run 284B DeepSeek-V4-Flash (<59GiB RAM: 41.1 cold pp, 9.1 N=1 tg, up to 25.3 spec tok/s) & 30B MoEs (22.4 N=1 / 111.6 spec tok/s) on 64GB CPU (0 GPUs). · GitHub](https://github.com/synchopate/llama-modchip?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - synchopate/llama-modchip: Run 284B DeepSeek-V4-Flash (<59GiB RAM: 41.1 cold pp, 9.1 N=1 tg, up to 25.3 spec tok/s) & 30B MoEs (22.4 N=1 / 111.6 spec tok/s) on 64GB CPU (0 GPUs). · GitHub](https://github.com/synchopate/llama-modchip?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

llama-modchip v2.5.2 是一个面向 CPU 的 MoE 大模型推理项目，主打在 64GB 内存、0 GPU 环境下运行 284B DeepSeek-V4-Flash 与 30B Nemotron/Qwen3 等模型，通过自定义 Fractal-64、LUT-VQ3-64 量化和 AVX-512/Metal/Windows 优化提升内存占用、吞吐与质量表现。

- 🚀 核心目标：在普通 64GB CPU 主机上本地运行 284B DeepSeek-V4-Flash 和 30B MoE 模型，无需 GPU。
- 🧠 自定义量化：Fractal-64（Q2_0=42，3.75 bpw）与 LUT-VQ3-64（VQ3_0=43，3.00 bpw），结合 3D Lloyd-Max 码本和 AVX-512 VBMI 寄存器查找。
- 📦 284B DeepSeek-V4-Flash：GGUF 约 56.40–56.93 GiB，64GB 内存可常驻；冷预填充约 37.8–44.4 tok/s，N=1 解码约 8.75–9.55 tok/s，投机/工具场景可达 11.2–25.3 tok/s。
- ⚡ 30B Nemotron-3.5-30B-A3B：VQ3-64 约 13.30 GiB、Fractal-64 约 14.36 GiB；N=1 解码约 22.44 tok/s，Stockfish-PVS/投机场景约 24.18–60.40 tok/s，质量门 100/100。
- ✅ 质量与效率：30B VQ3 相对 Q4_0 显著降低 RAM 占用，WikiText-2 PPL 约 7.4400；284B MaxQ-Fractal 在 wiki-alt 上 PPL 约 7.5133，并给出 KLD、Top-k 一致性和质量门结果。
- 🖥️ 跨平台支持：Linux 提供 AVX-512/AVX2 预编译二进制；Apple Silicon 支持 Metal（M1 Max 57.65、M3 Max 78.60、M5 Max 284B 约 27.0 tok/s）；Windows 11 支持 MinGW-w64 UCRT64 原生编译。
- 🧩 关键优化：HARP-Cache、/dev/shm Slot-0 前缀快照（40 工具 Claude Code 前缀 10.4ms 恢复）、RouteCrack + Stockfish-PVS v2 投机解码、Mamba-2/MLA/MoE 专用内核与多级缓存分块。
- ⚠️ 兼容性限制：自定义 GGUF 类型无法被原版 llama.cpp、Ollama、vLLM、LM Studio 直接加载，必须使用 llama-modchip 运行时；DeepSeek 模型还涉及 `deepseek4` 架构补丁。
- 💾 64GB 内存注意：284B 默认建议 `-c 32768 -ub 512`，避免匿名堆内存压力；256K 上下文更适合带 zram/swap 的无头 64GB 节点或 96GB+ 工作站。
- 🔐 安全与变体：默认安装安全对齐模型；Abliterated/Uncensored 变体为显式 opt-in，需确认后使用，并仅限授权安全研究、红队、CTF、漏洞审计等场景。
- 🛠️ 使用方式：提供 `./modchip chat/web/bench/eval/quantize/claude/status` 等命令，支持自动安装、基准测试、质量门评估、量化转换和本地 Claude Code 工具调用。
- 📊 社区基准：仓库包含大量 CPU/混合平台排行榜，覆盖 Zen 5、Threadripper、EPYC、Apple Silicon、ARM64 Graviton、Intel 与 Windows 混合 GPU+CPU 配置。

---

### [GitHub - tastyware/streaq：快速、异步、完全类型化的基于 Redis Streams 的分布式任务队列 · GitHub](https://github.com/tastyware/streaq?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - tastyware/streaq: Fast, async, fully-typed distributed task queue via Redis streams · GitHub](https://github.com/tastyware/streaq?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

streaQ 是 tastyware 旗下基于 Redis Streams 的快速、异步、全类型分布式任务队列，主打高性能、类型安全与完善的任务调度能力。

- 🚀 宣称比 arq 最高快 14 倍，适合高性能任务队列场景。
- 🧩 完全类型化，基于 anyio 的结构化并发，支持 asyncio 和 trio。
- ⏰ 支持延迟/定时任务、Cron 任务、任务中间件、死信队列、流水线和优先级队列。
- 🧵 支持同步任务，并可将其放到独立线程中运行。
- 🏭 提供 Redis Sentinel 与 Cluster 支持，适合生产环境。
- 🖥️ 内置 Web UI，用于监控任务状态。
- 📦 安装方式为 `pip install streaq`。
- 🛠️ 使用方式是创建 `Worker`、注册异步任务或 Cron 任务，并通过异步上下文管理器入队任务、获取任务信息和结果。
- ▶️ 可通过 `streaq run example:worker` 启动 worker，示例代码展示了任务入队、延迟执行、结果获取和日志输出。
- 📊 仓库采用 MIT 许可证，拥有 174 stars、15 forks、2 watchers、338 commits，主题涉及 anyio、asyncio、FastAPI、Redis、task queue 等。
- 💡 文档提示：如果不想使用 redis-py，可考虑支持 Trio 的全类型 Redis 客户端 coredis。

---

### [GitHub - polarsen-io/padwan-ai：基于 niquests 构建](https://github.com/polarsen-io/padwan-ai?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - polarsen-io/padwan-ai: Minimal, provider-agnostic Python client for large language models, built on niquests. · GitHub](https://github.com/polarsen-io/padwan-ai?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

Padwan AI 是一个基于 niquests 的轻量、异步、供应商无关的 Python LLM 客户端，支持 OpenAI、Gemini、Mistral、Grok、Anthropic 等多家模型及 OpenAI 兼容 API，并集成流式输出、工具代理、MCP、实时语音和可观测性能力。

- 🧩 核心定位：用一个统一客户端访问多种大语言模型，依赖极少，内置 TypedDict 类型支持与 HTTP/2、HTTP/3。
- 📦 安装方式：通过 `pip install padwan-ai` 安装，可选 `[realtime]`、`[otel]`、`[langfuse]` 扩展。
- ⚡ 快速开始：需 Python 3.13+，根据模型名自动选择供应商，只需配置对应 `*_API_KEY`；也可用 `PADWAN_BASE_URL` 和 `PADWAN_API_KEY` 进入网关模式。
- 💬 流式对话：提供 `stream_chat` 与 `ConversationState`，便于维护系统提示、用户消息和助手回复。
- 🛠️ 代理与工具：`AgentSession` 可自动执行工具调用循环，支持 typed Python 函数、MCP 服务器、审批钩子、并行工具执行和快照持久化。
- 🧪 工具校验：`@tool` 默认校验基础类型，复杂约束可选用 msgspec 或 pydantic。
- 🖥️ 命令行使用：支持 `uvx padwan-ai "Hello!" -m gpt-5.4-mini` 一次性调用，交互式聊天可使用 `padwan-cli`。
- 📊 供应商覆盖：OpenAI、Gemini、Anthropic、Mistral、Grok 等支持聊天与流式；部分供应商支持批处理、实时语音、转录、TTS、嵌入等能力。
- 🔌 扩展能力：支持 MCP 的 streamable-HTTP/stdio、OpenAI/Gemini Live/Grok Voice 实时语音、Gemini TTS、OpenTelemetry 与 Langfuse 可观测性。
- 🧪 测试支持：`padwan_ai.testing.ScriptedClient` 可回放脚本化响应，无需 API Key 即可测试代理。
- 🧰 开发流程：使用 `uv sync --all-extras --all-groups`、`just ci`、`just e2e`、`just docs` 进行依赖安装、CI 检查、真实供应商测试和本地文档服务。
- 📄 项目信息：MIT 许可证，仓库当前约 6 个 Star、2 个 Fork、230 次提交。

---

### [Git](https://github.com/thesayfulla/pylings?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - thesayfulla/pylings: Learn Python 🐍 by fixing code: exercises from basics to senior interview level · GitHub](https://github.com/thesayfulla/pylings?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

PyLings 是一个 Rustlings 风格的 Python 面试练习仓库，旨在通过修复代码和运行测试来学习 Python，内容覆盖从基础到高级面试题，使用 Python 3.14 且无额外依赖。

- 🐍 仓库定位：通过“修代码”学习 Python，练习从基础到资深面试水平。
- 🧩 练习规模：包含 35 个热身题和 20 个面试练习，难度由易到难。
- 🚀 启动方式：运行 `python3 -m pylings`，会自动打开下一题，并在保存文件后重新运行测试。
- ⌨️ 常用按键：`n` 下一题、`h` 提示、`r` 重跑、`l` 列表、`c` 全部检查、`x` 重置、`s` 查看答案、`q` 退出。
- 📚 难度分级：分为 Warm-up、Middle、Middle+、Senior、Staff 五个层级，涵盖迭代器、LRU 缓存、重试装饰器、限流器、事件总线、任务图、断路器、异步映射、工作池等主题。
- ✅ 答案与题目：参考答案位于 `solutions/`，面试问题位于 `questions/middle.md` 和 `questions/senior.md`。
- 💡 学习建议：测试通过前不要打开 `solutions/`；写代码前先列出边界情况；测试通过后回答练习题末尾的 Discussion 问题。
- 🧪 不使用 PyLings 时：可用 `python3 -m unittest discover -s tests -p "test_ex05*" -v` 运行指定测试，或用 `SOLUTIONS=1 python3 -m unittest discover -s tests` 检查参考解法。
- ⭐ 仓库热度：约 94 个 Star、5 个 Fork、2 个 Watcher、12 次提交。

---

### [GitHub - NeuroBrix/neurobrix: Run real AI models on the GPU you already own: language, speech, image and video models from one engine and one container format, with or without PyTorch. NVIDIA GPUs, Mac GPUs through Metal, CPU; other GPUs experimental. Apache 2.0. · GitHub](https://github.com/NeuroBrix/neurobrix?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - NeuroBrix/neurobrix: Run real AI models on the GPU you already own: language, speech, image and video models from one engine and one container format, with or without PyTorch. NVIDIA GPUs, Mac GPUs through Metal, CPU; other GPUs experimental. Apache 2.0. · GitHub](https://github.com/NeuroBrix/neurobrix?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

NeuroBrix 是一个可在自有 GPU 上本地运行语言、语音、图像和视频模型的推理引擎，核心是统一 `.nbx` 容器格式与可选 PyTorch/Triton 双计算分支，强调自动硬件放置、资源不足时明确拒绝，以及 OpenAI 兼容服务。

- 🚀 **定位**：在已有 GPU 上运行真实 AI 模型，覆盖语言、语音、图像、视频，支持不依赖 PyTorch 的 Triton 引擎。
- 📦 **安装与体积**：`pip install neurobrix`；Triton 引擎约 1.48 GiB，含 PyTorch 引擎约 6.82 GiB；需 Python 3.10+，当前版本 0.6.13。
- 🧠 **双计算分支**：默认走 PyTorch/ATen；`--triton` 使用 nbxtensor 的 Triton 内核，共享同一容器与放置计划，可互相校验。
- 🗂️ **统一容器**：`.nbx` 包含计算图、权重、组件连接和运行时默认值；无需为每个模型手写 pipeline，通用执行流支持 MoE LLM、STT、TTS、视频扩散等。
- ⚙️ **自动放置**：检测设备与内存，规划单 GPU、多 GPU、显存流式或主机卸载；`--explain-plan` 可查看方案，放不下时带数字报错而非静默降级。
- 🖥️ **硬件支持**：NVIDIA Linux/Windows、Apple Silicon Metal、x86-64 CPU 已发布；Intel/AMD 等 GPU 仍属实验性或未验证。
- 🧪 **模型生态**：Hub 约 45–49 个公开模型、10 类，含 TinyLlama、Whisper、Kokoro、Flex.1、CogVideoX、Wan、Real-ESRGAN 等；统一用 `<org>/<name>` 标识。
- 🛠️ **使用方式**：提供 `hub`、`import`、`run`、`serve`、`chat`、`upscale`、`list`、`remove`、`info`、`inspect`、`validate` 等命令，按模型族接收文本、音频、图像或视频输入。
- 🌐 **OpenAI 兼容 API**：`serve --http` 提供 `/v1/chat/completions` 等端点，支持 SSE 流式、工具调用和推理内容；未支持参数会按名拒绝。
- 💬 **KV 缓存与上下文**：缓存属于会话，后续轮次只预填新 token；会话有明确上限，超限返回 `400 context_length_exceeded`，不摘要或丢弃旧轮次。
- ⚠️ **已知限制**：暂无嵌入模型；约束解码依赖 `nbxgrammar` 且部分平台无 wheel；守护进程一次只持一个模型；超长提示在编译引擎上分块处理可能较慢。
- 🧾 **许可与贡献**：引擎采用 Apache 2.0，模型权重仍受原始许可约束；欢迎 bug、硬件报告和 PR，也可认证并共享 GPU 内核证书。

---

### [GitHub - singhpratech/ArrowMetal: Apache Arrow compute on Apple silicon GPUs through Metal: Arrow columns in unified memory, copy-free where the producer's buffers are page aligned; null-aware GPU kernels; Arrow C Data, C Device and C Stream interop · GitHub](https://github.com/singhpratech/ArrowMetal?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [GitHub - singhpratech/ArrowMetal: Apache Arrow compute on Apple silicon GPUs through Metal: Arrow columns in unified memory, copy-free where the producer's buffers are page aligned; null-aware GPU kernels; Arrow C Data, C Device and C Stream interop · GitHub](https://github.com/singhpratech/ArrowMetal?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

ArrowMetal 是一个将 Apache Arrow 计算放到 Apple Silicon GPU 上执行的开源项目，利用 CPU 与 GPU 共享的统一内存，在缓冲区页对齐时可零拷贝使用 Arrow 列；它通过优化器规则或扩展接入 DataFusion、Polars 和 DuckDB，保持 SQL 不变，并在 M4 Max 上对排序、分组聚合、去重等操作取得明显加速，同时明确保留部分 CPU 更快的场景。

- 🚀 **核心定位**：在 Apple Silicon GPU 上运行 Apache Arrow 计算，支持空值感知 GPU 内核，以及 Arrow C Data、C Device、C Stream 接口互操作。
- 🧠 **统一内存优势**：Arrow 缓冲区可直接放在 Metal 共享内存中，页对齐生产者缓冲区无需拷贝；GPU 运行时 CPU 可继续处理其他任务。
- 🔌 **三大引擎集成**：DataFusion 55.1 通过物理优化器规则接入；Polars 通过 `MetalEngine` 接入；DuckDB 通过优化器扩展接入，SQL 均无需改写。
- 📊 **性能亮点**：50,000,000 行下，DataFusion `ORDER BY` int64 加速 22.7x，`DISTINCT` 加速 2.31x；Polars 双键 `unique` 加速 11.54x；DuckDB `sum`/`count` 加速 4.89x。
- ⚠️ **适用边界**：并非所有操作都更快；top-k、部分过滤、整表聚合等仍留给 CPU 引擎，部分场景 CPU 领先，项目公开了 339 行基准中 77 行 CPU 更快的案例及原因。
- 🧮 **功能覆盖**：覆盖 Apache Arrow v25 全部 307 个计算函数名，其中 284 个在 GPU 上运行，17 个在主机端，7 个有明确限制；v26 新增的 `remainder` 已支持 GPU。
- 🧪 **测试与验证**：包含 41,688 个针对 pyarrow 的差分测试、1,047 个 Swift 测试和 7,289 个 Python 用例，强调结果一致性与 Arrow 语义兼容。
- 🧰 **多语言绑定**：提供 Swift、Python、C、Rust、Go、TypeScript/JavaScript、R 绑定，均通过同一 C ABI 和 Arrow C Data Interface 交换数据。
- 📦 **安装使用**：Python 可 `pip install arrowmetal`；Rust 使用 `arrowmetal = "0.6.1"`；DataFusion 使用 `datafusion-arrowmetal = "0.6.1"`；要求 macOS 14+ 与 Apple Silicon。
- 🆕 **最新版本**：v0.6.1 修复 M1 代 GPU 上 64 位键排序和分组管线创建问题，并支持 Polars 2.1.0，`polars` 附加依赖固定为 `polars>=1.44,<2.2`。
- ⚖️ **许可与定位**：采用 Apache-2.0 许可证，独立开源项目，不隶属于 ASF、Polars、DuckDB 或 Apple。

---

### [From API to Insight: Building an End-to-End Data Pipeline with Python, Wed, Nov 18, 2026, 4:30 PM   | Meetup](https://www.meetup.com/python-spokane/events/317078168/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [From API to Insight: Building an End-to-End Data Pipeline with Python, Wed, Nov 18, 2026, 4:30 PM   | Meetup](https://www.meetup.com/python-spokane/events/317078168/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

Spokane Python 用户组将举办一场实操活动，演示如何用 Python、公共 API 和 SQLite 构建从原始 API 数据到可分析洞察的端到端数据管道。

- 🐍 活动由 David 和 Eli B. 主持，Spokane Python User Group 举办，时间为 11 月 18 日周三 16:30–18:00 PST。
- 📍 地点为 2904 E Sprague Ave, Spokane, WA 99202；IntelliTect 提供场地和零食，Python Software Foundation 赞助 Meetup 订阅。
- 🛠️ 主题是使用 Python、公共 API 和 SQLite 构建完整数据管道，实践迷你 ELT（提取、加载、转换）流程。
- 📡 提取环节将从 DummyJSON API 获取产品数据，处理分页并收集记录。
- 💾 加载环节会把原始 API 响应先存入 SQLite，模拟生产数据管道做法。
- 🧹 转换环节包括校验记录、转换数据类型、处理缺失或无效值、去重并创建计算字段。
- 📊 洞察环节将用 SQL 查询转换后的数据，挖掘有用信息。
- 🚀 活动还会讨论如何将这些技术应用到更大规模的生产数据工程系统。
- 👥 适合 API 新手、对数据工程好奇者以及想探索实用数据处理技术的 Python 开发者；无需数据工程经验，基础 Python 会有帮助。
- 🍻 活动后可参加 Spokane Tech Community 的 “Tech and Taps”；报名链接：https://www.meetup.com/meetup-group-sdeepfce/events/317094039/

---

### [F5 Networks 的 Python 讲座之夜，2026年11月18日（周三）下午5:30 | Meetup](https://www.meetup.com/psppython/events/316998714/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Python talk night at F5 Networks, Wed, Nov 18, 2026, 5:30 PM   | Meetup](https://www.meetup.com/psppython/events/316998714/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

这是一场由 Puget Sound Programming Python（PuPPy）主办、在 F5 Networks 西雅图市中心办公室举行的 Python 演讲之夜，包含社交、闪电演讲、两场主题演讲及会后聚会，适合了解机器学习偏差、AI 编程智能体与智能体验证等主题。

- 📅 活动时间：11 月 18 日周三 17:30–20:00 PST
- 📍 活动地点：F5，801 5th Ave, Seattle, WA 98104，活动在 48 楼
- 🎤 主办与主持：PuPPy 主办，Andrew B. 等人主持
- 🗓️ 议程安排：17:30–18:00 签到社交，18:00–18:10 开场，18:10–18:25 闪电演讲，18:25–18:50 主题演讲 1，18:50–19:05 中场休息，19:05–19:30 主题演讲 2，19:30–19:40 闭幕
- ⚡ 闪电演讲：机器学习中的变换偏差，讲者 Brandon Sherman，解释对 log(y) 预测取指数会系统性低估期望值及修正方法
- 🤖 主题演讲 1：超越提示词——AI 编程的前沿，讲者 Tyrell Towle，讨论编码智能体、可靠性、上下文管理、自主执行、验证及 llama.cpp 等实践
- 🧪 主题演讲 2：智能体验证，讲者 Rohit Musti，介绍用轻量级测试框架和智能体管理验证流程并自我改进
- 🍕 餐饮与赞助：F5 Networks 提供食物，赞助方包括 ActiveState、Slalom Consulting、MotherDuck
- 💻 参与准备：演讲形式活动，无需携带电脑
- 🚪 入场方式：从 5th Avenue 街道入口进入，活动位于 48 楼
- 🅿️ 停车信息：F5 Tower 车库开放至 22:00，2 小时约 19 美元，3 小时约 21 美元，周边也有其他车库和街边停车
- 🚇 交通信息：靠近 2nd、3rd、4th、5th Avenue 多条公交线路及 Pioneer Square 轻轨站
- 🍻 会后聚会：活动结束后在 Owl N' Thistle（808 Post Ave, Seattle, WA 98104）继续交流

---

### [Data in Practice: Climate Intelligence and Statistical Computing with Polars, Thu, Nov 19, 2026, 7:00 PM   | Meetup](https://www.meetup.com/pydata-milano/events/317257011/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

**原文标题**: [Data in Practice: Climate Intelligence and Statistical Computing with Polars, Thu, Nov 19, 2026, 7:00 PM   | Meetup](https://www.meetup.com/pydata-milano/events/317257011/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-771-november-12-2026)

overview summary
- 🗓️ PyData Milano 将于 11 月 19 日 19:00–21:00 CET 在米兰 TeamSystem 举办数据实践活动，聚焦气候智能与 Polars 统计计算。
- 🌍 首场演讲由 Claudio Giorgio Giancaterino 分享基于 MCP 的多智能体地球观测框架，整合天气、卫星、预报与灾害数据，生成可解释且考虑不确定性的气候风险信号。
- ⚡ 第二场演讲由 Francesco Bruzzesi 介绍基于 Polars 引擎的向量化统计分布，通过 Rust 支持的表达式插件在查询内完成统计计算，保持惰性管道并兼顾性能、正确性与可复现采样。
- 🎯 活动适合从事数据管道、机器学习和 AI 应用的人士；入场需提供姓名和邮箱。

---

