### [](https://termdom.org/)

**原文标题**: [TermDOM | Build Terminal UIs with HTML, CSS and DOM](https://termdom.org/)

TermDOM 是一个 JavaScript 库，能将真实的 HTML/CSS/DOM 渲染到终端界面，并随 DOM 变化自动重绘。它让开发者可以用标准 Web 技术（原生 JS 或前端框架）构建 TUI 和交互式 CLI，同时支持完整的 CSS 布局、事件、表单、组件等浏览器式特性。

- 🖥️ 在终端中渲染真实 DOM，支持 CSS 级联与布局引擎
- ⚛️ 用原生 JavaScript 或任意前端框架编写 TUI
- 🔄 自动观察 DOM 变更并重绘屏幕，无需手动调用渲染
- ⌨️ 交互基于标准 DOM 事件（键盘、鼠标、焦点、粘贴）
- 📝 支持真实文本输入、光标移动及 CJK 输入法组合
- 🎨 支持 flexbox、表格布局，以及 CJK、emoji、RTL 文本处理
- 📜 提供滚动、scrollTo、scrollIntoView 等视口控制
- 🧩 包含表单控件、Web Components、选择样式、全屏模式
- 🔍 使用探针套件生成兼容性矩阵，验证 API 与 CSS 支持情况
- 📦 快速开始：`npm install @b9g/termdom`
- 🔀 与 DomTerm 互为镜像：DomTerm 把终端放进 DOM，TermDOM 把 DOM 放进终端

---

### [](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps · GitHub](https://github.com/vadimdemedes/ink)

这段文档是 Ink 的 README，介绍了 Ink 作为“React for CLIs”的核心概念、安装使用方式、内置组件、Hooks、API、测试方法及生态示例，帮助开发者用 React 组件化方式构建交互式命令行应用。

- 🎨 **概述**：Ink 是一个 React 渲染器，让开发者用组件化方式构建 CLI，基于 Yoga 实现 Flexbox 布局，并支持 React 全部特性。
- 📦 **安装与脚手架**：通过 `npm install ink react` 安装；可用 `create-ink-app` 快速创建 JavaScript 或 TypeScript 项目。
- 🚀 **快速开始**：核心 API 是 `render(<App />)`，文本必须放在 `<Text>` 组件中，支持颜色、加粗等样式。
- 📐 **核心组件**：包括 `<Text>`、`<Box>`、`<Newline>`、`<Spacer>`、`<Static>`、`<Transform>`，覆盖文本、布局、换行、弹性空间、静态输出和输出转换。
- 🧱 **`<Box>` 布局**：类似 CSS `display: flex`，支持尺寸、padding、margin、gap、flex 属性、对齐方式、定位、边框和背景色等。
- 🔤 **`<Text>` 样式**：支持 `color`、`backgroundColor`、`dimColor`、`bold`、`italic`、`underline`、`strikethrough`、`inverse` 以及 `wrap`/`truncate` 等文本行为。
- 📌 **`<Static>` 与 `<Transform>`**：`<Static>` 用于渲染不会变化的输出（如已完成任务），只处理新增项；`<Transform>` 可在输出前转换字符串，如大写或缩进。
- ⌨️ **输入 Hooks**：`useInput` 处理键盘输入，`usePaste` 处理粘贴文本，`useApp` 提供 `exit()`、`suspendTerminal()` 等应用生命周期方法。
- 📡 **流与尺寸 Hooks**：`useStdin`、`useStdout`、`useStderr` 可安全访问和写入对应流；`useWindowSize` 响应终端尺寸变化；`useBoxMetrics` 获取元素布局信息。
- 🎯 **焦点管理**：`useFocus` 和 `useFocusManager` 支持 Tab 切换焦点、自动聚焦及通过 `focus(id)` 编程式聚焦。
- 🖱️ **光标与动画**：`useCursor` 控制光标位置以支持 IME；`useAnimation` 提供帧计数、时间差和重置能力，驱动动画。
- 🧩 **渲染 API**：`render()` 支持 `stdout`/`stdin`、`exitOnCtrlC`、`concurrent`、`alternateScreen`、`kittyKeyboard` 等选项；另有 `renderToString()` 用于同步生成字符串输出。
- ♻️ **实例方法**：`rerender`、`unmount`、`waitUntilExit`、`waitUntilRenderFlush`、`clear`、`measureElement`，覆盖动态更新、清理和测量场景。
- 🧪 **测试与调试**：搭配 `ink-testing-library` 可简单断言输出；支持 React Devtools（设置 `DEV=true`），并内建屏幕阅读器支持（ARIA）。
- 📚 **生态与应用**：被 Claude Code、Gemini CLI、GitHub Copilot CLI、Linear、Gatsby、Prisma 等众多项目使用；社区提供大量第三方组件、Hooks 和示例。
- 📄 **示例与 CI**：`examples` 目录包含计数器、表格、路由、子进程等实例；CI 环境下默认只渲染最后一帧，可通过 `CI=false` 关闭该行为。

---

### [获取失败](https://github.com/bikeshaving/termdom/blob/main/examples/todomvc.ts)

**原文标题**: [Failed to retrieve](https://github.com/bikeshaving/termdom/blob/main/examples/todomvc.ts)

无法总结：获取内容失败，状态码 429。

---

### [](https://master.dev/courses/agent-harness/?utm_source=nodeweekly&utm_medium=newsletter&utm_campaign=agent-harness)

**原文标题**: [Build Durable AI Agent Systems | Master.dev](https://master.dev/courses/agent-harness/?utm_source=nodeweekly&utm_medium=newsletter&utm_campaign=agent-harness)

该课程由 Netflix 高级软件工程师 Scott Moss 主讲，时长 5 小时 5 分钟，旨在教授如何为 LLM 构建生产级 Agent Harness（代理运行框架）。课程从基础 Agent 循环出发，逐步引入持久执行、安全沙箱、记忆管理与压缩、多代理编排及人工审批等关键工程能力，强调可靠性、可恢复性和安全性，适合具备 TypeScript/Node.js 基础并有一定 AI 代理经验的开发者。

- 🎓 课程概览：Netflix 高级工程师 Scott Moss 授课，评分 4.6，涵盖 5 小时 5 分钟实战内容，需掌握 TypeScript/Node.js 及基础 Agent 开发经验。
- 🤖 Harness 核心：Harness 是将 LLM 转化为真正 Agent 的基础设施，提供记忆、工具集成、持久执行和自我修复能力；缺少 Harness 就只是事务性推理调用。
- 🛠️ 基础 Agent 循环：使用 Vercel AI SDK 搭建项目，实现模型调用工具、获取结果并循环直到最终回答，同时加入分类/回复工具与默认系统提示。
- ⚡ 流式消息传输：利用流式响应将部分结果实时推送到 UI，显著提升响应速度和用户体验。
- 🗄️ 持久执行：基于 NeonDB 与 DBOS 实现会话持久化，用 Drizzle ORM 定义事件日志，将模型轮次和工具调用包装为可恢复的步骤，支持断线重连。
- 🔒 安全沙盒与代码模式：创建隔离的代码执行沙箱（runCode 工具），让 Agent 安全完成算术和数据操作，并通过系统提示启用代码模式，成功处理重复订单退款场景。
- 🧠 记忆与上下文管理：实施对话历史压缩和摘要，在每次模型轮次前汇总历史，避免 token 超限；同时支持清除持久化事件日志来重置会话。
- 🔀 多代理移交与路由：实现 Agent Handoff 机制，添加账单代理和分流代理（Triage Agent），按请求类型高效委派任务。
- 👁️ 监督与子代理模式：引入“监督”概念和计划模式，通过结构化输出生成计划，并行派发账单、技术、销售等领域调查性子代理，并综合结果回复。
- 👤 人工介入机制：可为退款等敏感操作添加人工审批流程，课程笔记提供了完整实现细节。
- 🏁 总结与价值：强调该领域处于前沿，掌握这些工程技能能让工程师获得显著竞争优势；完成课程可获结业证书。

---

### [](https://github.com/fastify/fastify/releases/tag/v6.0.0-alpha.0)

**原文标题**: [Release v6.0.0-alpha.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v6.0.0-alpha.0)

Fastify v6.0.0-alpha.0 是 v6 的首个预发布版本，集中进行破坏性重构、类型清理与依赖升级，并修复部分历史遗留问题。

- 🔄 回滚了误导性的“Fastify instance is already listening”错误提示
- 🗑️ 移除多个已弃用的类型：FastifyPlugin、FastifyLoggerInstance、FastifyRequestContext、FastifyReplyContext、ValidationResult、req、ResSerializerReply
- 🚫 默认禁用错误处理器覆盖（error handler overrides）
- 🧹 移除 Promise.withResolvers ponyfill 及 FSTDEP022/023/024/025 弃用告警
- 📦 将 undici 升级至 v8.x，并提高最低运行时版本
- 🧪 移除 @sinonjs/fake-timers 测试依赖
- 📝 新增 Google Cloud Functions 按路由记录日志的文档
- 💖 新增赞助商 testmu ai
- 👥 完整变更日志见 v5.11.3...v6.0.0-alpha.0，由 Eomm、Tony133 等 5 位贡献者共同完成

---

### [](https://fastify.dev/)

**原文标题**: [Fast and low overhead web framework, for Node.js | Fastify](https://fastify.dev/)

overview summary: Fastify 是一个高性能、高度可扩展的 Node.js Web 框架，以 JSON Schema 验证、极速日志、TypeScript 支持和庞大插件生态著称，并被众多组织广泛采用。

- 🚀 每月下载量超 1000 万次，被大量组织和产品广泛使用
- 💰 支持通过 GitHub 或 Open Collective 进行资金赞助
- ⚡️ 核心特性之一是高性能，复杂代码下每秒可处理高达 3 万请求
- 🔌 通过钩子（hooks）、插件（plugins）和装饰器（decorators）实现完全可扩展
- 📋 推荐使用 JSON Schema 验证路由并序列化输出，框架内部会将其编译为高性能函数
- 📝 内置最佳日志库 Pino，几乎消除了日志记录带来的性能开销
- 👩‍💻 开发者友好，注重表达力与日常使用体验，同时不牺牲性能与安全
- 📘 持续维护 TypeScript 类型声明文件，全面支持 TypeScript 社区
- 🛠️ 快速启动：使用 `npm install fastify` 并创建 `server.js`，同时支持 ESM 和 CJS 语法
- 🧩 提供 fastify-cli 工具，可快速生成 JavaScript 或 TypeScript 项目脚手架
- ✅ 支持通过 JSON Schema 定义请求/响应校验，并利用 preHandler 在执行 handler 前完成鉴权等操作
- 🏎️ 从底层专为性能而设计，官方提供基准测试与其他框架对比，性能表现卓越
- 🌱 插件生态持续增长，目前已有 297 个可用插件，找不到所需插件也很容易自行编写
- 👥 拥有活跃的维护者与协作者团队，并由 Nearform、Platformatic 等赞助，同时是 OpenJS Foundation 的 At Large 项目

---

### [](https://openjsf.org/blog/fastifys-growth-and-success)

**原文标题**: [Fastify v5 is Now Officially Released! | OpenJS Foundation](https://openjsf.org/blog/fastifys-growth-and-success)

概述：Fastify v5 正式发布，这是经过两年开发后的第五个主版本，重点在于简化长期维护、放弃对旧版 Node.js 的支持，并移除已弃用的 API。项目社区持续壮大，v4 版本将按计划退役，同时团队感谢所有赞助者与贡献者。

- 🎉 Fastify v5 正式发布（GA），距离 v4 已历时两年，主要目标是简化长期维护并精简框架。
- ⚙️ v5 现在要求 Node.js v20 及以上版本，并移除了过去两年积累的所有弃用 API。
- 📚 官方提供完整迁移指南，帮助开发者从 v4 平滑升级到 v5。
- 📈 项目增长强劲：目前有 22 位维护者、400 位活跃贡献者、超过 4000 次提交、285 个版本、2300 个 fork、月下载量达 780 万，以及 296 个官方插件。
- 🚀 Fastify v4 是非常成功的版本，两年内下载量翻倍，仅 2024 年 8 月就超过 780 万次，并发布了 28 个次要版本而无破坏性变更。
- 🗓️ Fastify v4 将于 2025 年 6 月 30 日正式停止维护（retired）。
- 💖 感谢所有直接赞助本次发布的贡献者（如 aaroncadillac、busybox11、Cadienvan、dancastillo、Eomm、Fdawgs、jsumners、mcollina、RafaelGSS、Uzlopak、voxpelli），并鼓励社区继续支持他们。
- 🏢 企业赞助商包括 Handsontable、Mercedes-Benz、Nearform、Platformatic、Val Town。
- 🆘 若无法及时升级，可通过 HeroDevs 获得生命周期结束后的支持（Ecosystem Sustainability Program 合作伙伴）。

---

### [](https://github.com/fastify/fastify/issues/6834)

**原文标题**: [V6 Planning · Issue #6834 · fastify/fastify · GitHub](https://github.com/fastify/fastify/issues/6834)

Fastify v6 规划（GitHub issue #6834）：目标在 2026 年 7 月发布 alpha，9 月正式发布，包含多项破坏性变更、清理及待定决策。
- 📅 时间线：计划 2026 年 7 月推出 alpha，9 月发布正式版。
- 🌿 分支管理：切割 v5.x 分支，将 main 切换为 v6.x alpha，并检查 next 分支状态。
- ⬆️ Node 版本：最低要求提升到 Node.js v24。
- 🧹 移除弃用：删除 FSTDEP022、FSTDEP023、FSTDEP024、FSTDEP025 弃用警告。
- 🗑️ 移除兼容层：删除 Promise.withResolvers 的 ponyfill 及 ResSerializerReply 类型。
- 🚫 行为变更：默认禁止错误处理器覆盖（可配置重启用），并移除警告 FSTWRN004。
- 📖 文档：需要编写 V6 迁移指南。
- ❓ 待定问题：是否移除声明合并（改为注册作用域的装饰器类型），以及是否移除 fast-json-stringify 并改用 Ajv 进行响应验证。

---

### [](https://adventures.nodeland.dev/archive/triaging-the-ai-horde/)

**原文标题**: [Triaging the AI Horde](https://adventures.nodeland.dev/archive/triaging-the-ai-horde/)

概述总结：本文讨论了维护者在安全漏洞分类工作中面临的 AI 生成报告洪流，以及如何应对误报和重复报告，并分享了个人工作流程与态度转变。
- 🤖 每周收到 20-40 份安全报告，几乎所有报告都由 AI 撰写，且通常附带 3-5 份重复提交。
- 📢 引用 Linus Torvalds 观点：AI 发现的漏洞本质上不应保密，公开处理可减少重复报告和资源浪费。
- 🧑💻 有时 AI 背后有真人研究者，有时完全是机器人，但无论哪种情况，分类工作都难以回避。
- 🎯 分类的主要目标常是向 AI 解释该行为不在威胁模型内，而非修复实际漏洞，以保护维护者时间并避免倦怠。
- 🔧 工作流程：使用虚拟机上的 Agent（如 Pi、Sol、Grok 或 Claude Code 配合 Opus），通过 HackerOne 扩展拉取报告，并反复挑战 Agent 结论。
- ⚖️ 作者的安全阈值已大幅提高，过去因过于信任而放行误报，付出代价，因此现在宁可过度拒绝也不放过假阳性。
- 👥 当发现报告背后是真人时，会投入更多关注；AI 对 AI 与人对人是不同层次的交流，后者更值得认真对待。
- 💬 作者呼吁其他维护者分享应对 AI 报告洪流的经验，同时感谢默默从事分类工作的人。

---

### [](https://bun.com/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.com/)

Bun v1.3.14 正式发布。Bun 是一个追求极致速度与 100% Node.js 兼容性的 JavaScript 全家桶工具包，支持 TypeScript 和 JSX，可增量采用，并内置运行时、打包器、测试运行器与包管理器。该版本提供 Linux、macOS 和 Windows 的简易安装方式，在打包 10,000 个 React 组件的基准测试中显著领先同类工具。

- 🚀 Bun v1.3.14 版本发布，定位为快速、可增量采用的 JavaScript 全能工具箱。
- ⚡ 原生支持 JavaScript、TypeScript 与 JSX，集成运行时、打包器、测试运行器及包管理器，目标 100% Node.js 兼容。
- 📥 支持 Linux/macOS 的 curl 安装脚本和 Windows 的 PowerShell 安装命令。
- 🧩 已被 Bundler、Express、Postgres、WebSockets 等项目及技术采用。
- 🏁 基准测试：打包 10,000 个 React 组件仅需 269.1ms（Bun v1.3.0），远快于 Rolldown（494.9ms）、esbuild（571.9ms）、Farm（1608ms）和 Rspack（2137ms）。

---

### [](https://x.com/bunjavascript/status/2087436767054213517)

**原文标题**: [Bun on X: "In the next version of Bun

Node.js compatibility gets a big upgrade. 

Since Bun v1.3.14, an additional +1,493 tests from the Node.js test suite pass in Bun. https://t.co/i57nEHjtRD" / X](https://x.com/bunjavascript/status/2087436767054213517)

overview summary  
Bun 宣布下一版本将大幅提升 Node.js 兼容性，新增通过大量 Node.js 测试套件用例，并引发社区对兼容进度与发布时间的讨论。

- 🚀 下一版 Bun 将带来 Node.js 兼容性的重大升级  
- 📈 自 Bun v1.3.14 起，新增 1,493 项 Node.js 测试套件用例通过  
- ⏱️ 过去 16 天内，Bun v1.4 又新增 473 项 Node.js 测试通过  
- ❓ 用户询问距离 100% 兼容还有多远  
- 😅 有用户调侃 Bun 的下一版本似乎迟迟不发布  
- 🗓️ 也有用户询问 v1.4 的发布时间表

---

### [博客 | Bun](https://bun.com/blog)

**原文标题**: [Blog | Bun](https://bun.com/blog)

Bun 是一套包含运行时、包管理器、测试运行器和打包器的 JavaScript 工具链。本文总结了它从 2022 年 v0.1 早期版本到 2026 年 v1.3.14 的发展历程，涵盖 1.0 稳定版、Windows 支持、内置 Postgres/S3/Redis 等关键演进，以及被 Anthropic 收购、从 Zig 重写为 Rust 的重大决策。

- 🚀 自 2022 年 v0.1 开始快速迭代，至 2023 年 9 月 Bun 1.0 稳定，达到生产可用级别。
- 🪟 2024 年 4 月发布 Bun 1.1，正式支持 Windows 平台，扩展了用户覆盖范围。
- 🗄️ Bun 1.2（2025 年 1 月）引入内置 Postgres 客户端 Bun.sql、S3 对象存储 Bun.s3，以及文本式锁文件 bun.lock。
- ⚡ Bun 1.3（2025 年 10 月）推出零配置前端开发、统一 SQL API、内置 Redis 客户端与安全增强等新特性。
- 🤝 2025 年 12 月，Bun 被 Anthropic 收购，成为 Claude Code 及未来 AI 编码工具的基础设施。
- 🔧 2026 年 7 月宣布将 Bun 从 Zig 重写为 Rust，以提升长期可维护性并优化性能。
- 📦 bun install 性能显著领先：通过直接系统调用、缓存友好数据布局和全核并行，安装速度最高提升 25 倍。
- 🧰 内置 API 不断丰富，包括 Bun.shell、Bun.markdown、Bun.Terminal、Bun.cron、Bun.Image、Bun.redis、Bun.Glob 等现代化能力。
- 🌐 与 Vercel 深度集成，开发者可在 Vercel Functions 上直接运行 Bun Runtime。
- ✅ Node.js 兼容性持续改善，bun test 支持并行、分片、覆盖率报告，并逐步强化调试器与性能剖析工具。

---

### [](https://nodejs.org/api/domain.html)

**原文标题**: [Domain | Node.js v26.7.0 Documentation](https://nodejs.org/api/domain.html)

概述：Node.js 的 Domain 模块提供将多个 I/O 操作分组处理错误的能力，但已弃用，建议谨慎使用并规划迁移。

- ⚠️ 模块已标记为“稳定性：0 - 已弃用”，待替代 API 完成后将完全弃用，多数开发者不应使用。
- 🎯 核心用途：将多个 I/O 操作视为一组，统一捕获事件发射器或回调中的 `'error'` 事件及抛出的错误，避免进程直接崩溃。
- 🚫 警告：域错误处理器不能替代“出错后安全恢复”，推荐做法是关闭异常请求、停止接收新请求，并配合 `cluster` 模块由主进程派生新 worker。
- 📌 `Error` 对象经域路由时会附加 `domain`、`domainEmitter`、`domainBound`、`domainThrown` 等字段。
- 🔗 隐式绑定：在活动域中创建的新 `EventEmitter`、流、请求、响应及底层异步回调会自动绑定到该域；但 `Domain` 对象本身不会隐式绑定，以避免内存泄漏。
- 🔧 显式绑定：可通过 `domain.add(emitter)` 将已有 emitter 加入指定域；也可用 `domain.bind(callback)` 将回调绑定到域，或用 `domain.intercept(callback)` 自动拦截回调中作为首个参数的 `Error` 对象。
- 🏃 `domain.run(fn[, ...args])` 在域上下文中运行函数，并隐式绑定其中创建的事件发射器、定时器和低级请求。
- 📦 `Domain` 类继承自 `EventEmitter`，通过监听 `'error'` 事件处理捕获的错误；`members` 属性列出显式添加的 emitter。
- 🔄 `enter()` 和 `exit()` 用于设置/退出当前活动域，可任意次调用，仅改变活动域，不影响域本身。
- ⛓️ 域与 Promise：Promise 的异步处理器在调用 `.then()`/`.catch()` 时所在的域中执行；也可用 `domain.bind()` 将回调绑定到特定域；未处理的 Promise 拒绝不会触发域的 `'error'` 事件。

---

### [](https://github.com/nodejs/node/pull/65074)

**原文标题**: [domain: runtime-deprecate the module by mcollina · Pull Request #65074 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65074)

概述：此 PR 提议将 Node.js 的 `node:domain` 模块从仅文档弃用（DEP0032）升级为运行时弃用，即加载该模块时直接发出弃用警告，并同步更新文档；该变更被标记为 semver-major，已获多位审查者批准。

- ⚠️ 将 `node:domain` 模块的弃用级别从文档弃用提升为运行时弃用，加载即触发 DeprecationWarning（代码 DEP0032）。
- 📄 更新 `doc/api/deprecations.md`，将弃用类型改为“Runtime”，并保留原有“不应使用”的说明。
- 🔧 修复 issue #10843（“What will Domain be replaced with?”），明确该模块缺少 1:1 的替代 API。
- 🏷️ 添加 `domain`、`needs-ci`、`semver-major` 标签，属于破坏性变更，预计在下一主版本发布。
- ✅ 代码覆盖率测试通过（项目覆盖率 90.30%），`lib/domain.js` 覆盖率为 95.35%。
- 👥 已获 avivkeller、marco-ippolito 批准，另有 AugustinMauroy 提出关于替代 API 的评论。
- 🚀 社区反响积极，获得 5 个火箭反应和 1 个赞。

---

### [](https://github.com/nodejs/node/issues/65110)

**原文标题**: [Multiple independent reports of out-of-memory crash after updating 24.18.1->24.19.0 · Issue #65110 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/65110)

概述：Node.js v24.19.0 更新后出现多起独立报告的内存溢出（OOM）崩溃问题，回滚至 v24.18.1 即可解决，但缺乏可复现案例。

- 😱 多个独立环境（Linux/Docker、Heroku、Alpine）在从 v24.18.1 升级到 v24.19.0 后，应用因内存不足（OOM）崩溃。
- 🔄 回滚到 v24.18.1 后问题全部消失，说明崩溃与 Node.js 更新直接相关，而非应用代码或依赖的巧合变更。
- 📊 内存指标未显示真实泄漏迹象，崩溃前 GC 日志显示堆内存接近上限，最终触发“JavaScript heap out of memory”致命错误。
- ⏱️ 问题出现时间不固定（数分钟到数小时），已在压测环境和两个生产环境中复现，但缺乏最小化复现步骤。
- 🏷️ 该 issue 被标记为“需要更多信息”，因目前没有有效的复现案例，尚未分配人员或设定里程碑。

---

### [](https://vercel.com/changelog/one-click-upgrade-for-deprecated-node-js-versions)

**原文标题**: [One-click upgrade for deprecated Node.js versions - Vercel](https://vercel.com/changelog/one-click-upgrade-for-deprecated-node-js-versions)

Vercel 现在支持从仪表盘一键将 Node.js 20 及更早版本升级到 Node.js 24，并更新项目设置中的版本；若 package.json 中也指定了版本，需手动更新；现有部署不受影响，官方鼓励升级已弃用的项目。

- 🚀 团队所有者或成员可在 Vercel 仪表盘一键升级 Node.js 20 及更早版本至 Node.js 24
- ⚙️ 升级会更新项目设置中的 Node.js 版本
- 📦 若 package.json 中也定义了 Node.js 版本，需要手动修改
- ✅ 现有部署不受升级影响
- 🔔 请查看并升级已弃用的 Node.js 项目

---

### [添加第二个中间件破坏了我们的 TypeScript 类型 - Inngest 博客](https://www.inngest.com/blog/adding-a-second-middleware-broke-our-typescript-types)

**原文标题**: [Adding a second middleware broke our typescript types - Inngest Blog](https://www.inngest.com/blog/adding-a-second-middleware-broke-our-typescript-types)

本文探讨了在 Inngest 客户端中叠加两个中间件导致 TypeScript 类型意外损坏的问题，作者深入追踪后定位到 `Jsonify` 类型在可选属性处理上的漏洞，并给出了修复方案与类型测试教训。

- 🐛 添加第二个中间件后，`step.run` 的返回类型塌缩为 `{}`，而单个中间件正常，且与中间件具体实现无关。
- 🔁 中间件输出默认经过 `Jsonify` 转换，两个中间件意味着 `Jsonify<Jsonify<T>>`，类型本应幂等，但可选属性破坏了这一过程。
- 🔑 根因是映射类型 `{ [Key in keyof T]: ... }[keyof T]` 读取可选属性键时会混入 `undefined`，使键集合被污染。
- ⚠️ 泛型约束只在定义处检查，实例化时不会重新验证，所以 `Pick<T, FilterJsonableKeys<T>>` 悄悄容忍了 `undefined` 作为键。
- 💥 污染后的键导致 `T[undefined]` 触发 TypeScript 内部错误类型，它像“NaN”一样扩散，最终产出 `JsonifyObject<{}>`，全程无诊断。
- 🔧 社区两个修复都不彻底：一个只在全默认栈时跳过重复 `Jsonify`；另一个用 `JsonValue` 守卫，但无法处理 `unknown`，也遗漏了 `step.invoke` 的同类问题。
- ✅ 正确修复是在 `FilterJsonableKeys` 的结果上包裹 `Exclude<…, undefined>`，阻止 `undefined` 进入键集合，一处修复全局生效。
- 🚀 更优方案是使用 key remapping（`as`）直接在键上过滤，完全避免生成值联合，让 `FilterJsonableKeys` 和 `Pick` 都失去存在意义。
- 🧪 类型测试有陷阱：`IsEqual<Once, Twice>` 在延迟类型上可能假通过，必须通过属性访问（如 `Twice["media"][number]["mediaId"]`）强制解析才能真正暴露问题。
- 📚 核心教训：可选属性会在键过滤中引入 `undefined`，泛型约束不会重查实例，错误类型会静默传播，自组合类型应测试 `f(f(x)) === f(x)`，断言需通过具体属性访问。

---

### [错误](https://meiert.com/blog/5-npx-helpers/)

**原文标题**: [Error](https://meiert.com/blog/5-npx-helpers/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='meiert.com', port=443): Max retries exceeded with url: /blog/5-npx-helpers/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [如何使用 Outbox 模式解决 Node](https://www.freecodecamp.org/news/how-to-fix-the-dual-write-problem-in-node-js-with-the-outbox-pattern/)

**原文标题**: [How to Fix the Dual-Write Problem in Node.js with the Outbox Pattern](https://www.freecodecamp.org/news/how-to-fix-the-dual-write-problem-in-node-js-with-the-outbox-pattern/)

本文介绍如何用 Node.js 实现事务性 Outbox 模式，解决数据库与消息队列之间的“双写”一致性问题。文章以订单服务和履约服务为例，使用 PostgreSQL、SQS、DynamoDB 及本地 AWS 模拟器 floci，从问题分析、模式原理到完整代码实现逐步演示，并讨论了生产化注意事项。

- 🧩 双写问题：应用常需先写数据库、再发消息，但两个系统无共享事务，进程崩溃或网络故障会导致一边成功、一边失败，数据静默不一致。
- ⚠️ 错误示范：把 SQS 调用放进数据库事务也无法真正原子化，事务管不了 SQS，还会长时间占用连接和锁，并可能产生重复消息。
- 📦 Outbox 核心思路：将“事件写入”变成同一次数据库事务中的 outbox 表插入，再由独立 relay 进程异步发布到队列。
- 🗄️ 数据库表设计：orders 表存业务数据；outbox 表存 event_type、payload、status，并用部分索引加速 pending 行查询。
- 🖥️ 请求处理器：在 BEGIN/COMMIT 中同时插入订单和 outbox 记录，不直接调用 SQS；任何一步失败都会整体回滚。
- 🔄 Relay 进程：定时轮询 pending 行，用 `FOR UPDATE SKIP LOCKED` 防止多实例重复处理，发送成功后才标记为 sent。
- 🔁 至少一次投递：relay 若在发送后崩溃，消息会重发；因此消费者必须实现幂等处理。
- 📡 消费者幂等：独立服务从 SQS 接收消息，用 DynamoDB 的 `ConditionExpression: attribute_not_exists(orderId)` 避免重复创建履约记录。
- 🛠️ 本地验证：用 floci 模拟 RDS/SQS/DynamoDB，一条命令搭建环境，运行 server/relay/consumer 三个进程即可验证完整流程。
- 🚀 生产化建议：切换到真实 AWS 无需改代码；relay 可水平扩展；建议增加 failed 状态、重试计数和死信队列。
- ⚡ 高性能替代：高吞吐场景可用 CDC（如 Debezium）读取 WAL 替代轮询 relay，但运维成本更高。
- 🎯 总结：Outbox 模式用简单可靠的数据库事务，结合独立 relay 和幂等消费者，实现无分布式事务的可靠事件交付。

---

### [深入解析 Hono](https://flaviocopes.com/how-hono-is-built/)

**原文标题**: [A deep dive into Hono](https://flaviocopes.com/how-hono-is-built/)

overview summary
本文深入剖析 Hono 框架处理一次请求的完整旅程：从注册路由、请求通过 fetch() 进入、SmartRouter 选择路由器并匹配路径、创建 Context、中间件按洋葱模型执行、生成标准 Web Response，再到运行时适配器与测试方式。同时解释了注册顺序的重要性、参数惰性解析、中间件可中断请求、c.text() 的本质、适配器的作用，以及 Hono 的适用场景和调试思路。

- 📝 Hono 在注册路由时只保存方法、路径、处理器和注册顺序，并不会立即执行；注册顺序直接影响匹配优先级，通配路由放在前面会屏蔽后面的具体路由。
- 🌐 应用核心是 app.fetch()，接收标准 Web Request 并返回 Web Response，这让 Hono 可以跨 Cloudflare Workers、Bun、Deno 等运行时运行。
- ⚡ 首次请求时 SmartRouter 会尝试 RegExpRouter，若不适用则回退到 TrieRouter，选定后后续请求直接复用，避免重复开销。
- 🔍 路由匹配后并不立即生成参数对象，而是在调用 c.req.param('name') 时才惰性解析路径中的捕获值，体现了“按需解析”的性能设计。
- 🧠 Hono 为每次请求创建 Context（c），它连接原始 Request、响应助手、环境变量、状态和头信息；c.req 包装了 HonoRequest，同时保留 c.req.raw 可访问原始请求。
- 🧅 中间件通过 await next() 形成洋葱模型，可在后续处理器执行前后分别做操作（如计时、加响应头）；中间件也可以不调用 next() 直接返回响应，从而中断旅程。
- 📦 c.text() 只是创建标准 Response 的快捷方式（带正确的 Content-Type），c.json()、c.html()、c.redirect() 同理，底层都是 Web Response。
- 🔌 适配器只负责翻译运行时边界，例如 Node.js 的 IncomingMessage/ServerResponse 与 Web Request/Response 之间的转换，Hono 核心不依赖特定运行时。
- 🧪 app.request() 可直接构造请求并走完整流程，无需启动服务器，非常适合测试路由、参数、中间件和响应契约。
- 🛠 文章提供了一个迷你实现示例，展示 Hono 的核心架构：注册处理器、接收请求、查找路由、创建上下文、返回响应，其余复杂功能都是在此基础上的增强。
- ✅ 适合用 Hono 的场景：Cloudflare Workers 上的专注 API、需要测试与生产同构的 Web 契约、希望保持跨运行时可移植性的小型服务。
- 🚫 不适合用 Hono 的场景：纯静态单页、依赖 Node 特定中间件的大型应用、以及需要自行决定渲染/数据加载/认证等全套方案的完整产品。
- 🐞 路由不工作时，按此顺序排查：检查 app.routes 注册表、用 app.request() 复现请求、确认方法/路径匹配、检查中间件是否提前返回或未调用 await next()、确认最终处理器返回了 Response。

---

### [](https://www.deepseek.com/harness/en/)

**原文标题**: [DeepSeek Harness developer preview: Everything is a plugin](https://www.deepseek.com/harness/en/)

overview summary
DeepSeek Harness 已推出开发者预览版，采用“一切皆插件”的架构，基于 Cordis 内核实现模块化组合，提供多种运行模式与完整可追踪日志，支持开发者自定义代理能力，并已开放源代码。

- 🧩 核心设计：所有能力均为插件，包括模型、工具、技能、会话、沙箱、存储、循环、调度和 UI，可在配置中自由替换或扩展。
- ⚙️ Cordis 内核：负责插件的挂载、卸载与依赖管理，通过服务与事件机制让各插件协同工作，无需改动源代码。
- 📜 全程可追溯：采用追加式会话日志记录模型所见一切，支持轨迹视图按来源检查、恢复、分叉、搜索与回放。
- 🚀 四种运行模式：标准模式提供完整工具集；代码模式允许模型通过生成代码编排多轮工具调用；极简模式仅保留 shell 与文件编辑器用于基准测试；创作者模式支持运行时检查与插件试验。
- 🛠️ 自定义能力：开发者可通过配置组合插件创建新预设，或使用 Creator Mode 在内存中测试并组合 Cordis 插件。
- 🌐 快速开始：支持 npx 一键启动 Web UI（`npx @deepseek-ai/dsh web`）或通过 Git 克隆源码本地安装。
- 🔭 仍处预览阶段：核心插件与 API 会持续演进，面向全球开发者开放，基于可复用和可组合的开源基础设施探索智能边界。

---

### [](https://github.com/cordiverse/cordis)

**原文标题**: [GitHub - cordiverse/cordis: Meta-Framework of Spatiotemporal Composability · GitHub](https://github.com/cordiverse/cordis)

Cordis 是一个正在积极开发中的开源元框架，旨在实现时空组合性（Spatiotemporal Composability），其 API 尚不稳定。该项目的 GitHub 仓库拥有 2.3k 星标与 109 个 fork，并提供了相关论文和文档资源。

- 🌟 项目定位：Cordis 是一个“时空组合性”的元框架（Meta-Framework）。
- ⚠️ 开发状态：项目处于活跃开发阶段，API 可能随时变化，不建议依赖稳定版本。
- 📄 参考资料：提供了相关论文《A Programming Paradigm for Spatiotemporal Composability》及入门文档 cordis-primer。
- ⭐ 仓库数据：GitHub 上获得 2.3k Stars、109 Forks、12 Watchers。
- 🧩 主要主题：涉及 effect、framework、nodejs、plugin 等技术方向。
- 📜 开源许可：采用 MIT 许可证，允许自由使用与修改。
- 📁 仓库结构：包含 packages 目录、配置文件、CI 工作流等，共 550 次提交，由多位贡献者共同维护。

---

### [](https://github.com/deepseek-ai/deepseek-harness)

**原文标题**: [GitHub - deepseek-ai/deepseek-harness: DeepSeek Harness: Everything is a Plugin. · GitHub](https://github.com/deepseek-ai/deepseek-harness)

DeepSeek Harness 是一个由 DeepSeek AI 开发的开源智能体工具集，采用“一切皆插件”的架构，基于 Cordis 框架构建，目前处于开发者预览阶段，支持通过 npm 或源码运行，并提供社区支持与 MIT 许可证。

- 🧩 核心架构：一切皆插件，基于 Cordis 框架实现时空可组合性的编程范式
- ⚠️ 开发者预览版：正在快速迭代，存在兼容性破坏变更，需谨慎使用
- 🚀 快速运行：通过 `npx @deepseek-ai/dsh web` 启动 Web UI，默认地址为 http://127.0.0.1:3080
- 📦 源码运行：需 git clone、pnpm install、pnpm run build，再执行 `pnpm dsh web`
- 💬 社区支持：可通过 GitHub Discussions 提交反馈，插件仓库添加 `dsh-plugin` 主题便于发现，并设有 Discord 社区
- 🤝 贡献指南：详见 CONTRIBUTING.md，开发指南与架构文档可参考，代理开发需遵循 AGENTS.md
- 📄 许可证与依赖：采用 MIT 许可证，第三方依赖声明见 THIRD_PARTY_NOTICES.md
- ⭐ 仓库规模：目前拥有 66.3k stars、5.6k forks、248 watchers

---

### [](https://github.com/webpro-nl/unbash)

**原文标题**: [GitHub - webpro-nl/unbash: Fast 0-deps bash parser written in TypeScript · GitHub](https://github.com/webpro-nl/unbash)

unbash 是一个用 TypeScript 编写的快速、零依赖的 Bash 解析器，旨在解析 Bash 源码结构而不执行代码。它提供类型化 AST、惰性词部分解析、错误恢复、源位置信息，并与 tree-sitter-bash、sh-syntax、bash-parser 等主流解析器进行了性能与功能对比。

- 📦 安装：`npm install unbash`
- 🎯 适用场景：解析粘贴的命令、完整脚本或嵌入的 shell 源码，用于权限提示、静态清单、命令转换、诊断、可视化及代码迁移
- ✅ 支持语法：命令、控制流、管道、重定向、赋值、复合语句、参数/单词展开、进程与嵌套替换、heredoc、herestring、coproc 等
- 🛠️ 容错解析：对不完整或格式错误的输入，返回带源位置错误的部分 AST，递归恢复深度受限
- ⚠️ 边界说明：不执行代码、不展开变量、不提供沙箱、不判断安全性；也不支持 PowerShell/cmd.exe
- 📄 使用示例：`parse('if [ -f "$1" ]; then cat "$1"; fi')` 返回结构化 Script/Statement/If 节点
- 🔍 Word parts：`parts` 是惰性 getter，需直接读取或依赖 `JSON.stringify`（通过 `toJSON`）；普通 `Object.keys` 遍历不会发现展开
- 📍 位置信息：节点使用零基 UTF-16 码元偏移的半开区间 `[pos, end)`，可直接切片原始源码，嵌套命令共享源码范围
- 🖨️ 打印功能：提供 `unbash/printer` 基本打印，不保留空白和注释（shebang 除外）
- ⚖️ 对比 tree-sitter-bash：unbash 提供类型化 AST、同步零依赖 API、结构化词部分和更快解析；tree-sitter 则适合增量解析与全量 CST
- ⚖️ 对比 sh-syntax：unbash 零依赖、JSON 友好、支持部分 AST；sh-syntax 基于 WASM，支持多 shell 方言和成熟格式化
- ⚖️ 对比 bash-parser：unbash 更现代，类型化 API，支持更多 Bash 特性（如 `[[ ]]`、`select`、`coproc`、extglob、`;&` 等），且带错误恢复
- 🚀 性能：基准测试中比 tree-sitter-bash 快约 7–17 倍，比 sh-syntax 快 9–2870 倍（视输入规模而定）
- 📦 体积：解析器打包后约 80KB minified / 19KB gzipped
- 🔗 附加资源：提供在线 playground（unbash.statichost.page），采用 ISC 许可证

---

### [清理你的 JavaScript 和 TypeScript 项目 | Knip](https://knip.dev/)

**原文标题**: [Declutter your JavaScript & TypeScript projects | Knip](https://knip.dev/)

overview summary
Knip 是一款专为 JavaScript 和 TypeScript 项目设计的代码清理工具，能够精准发现并帮助移除未使用的依赖、导出和文件。它基于项目实际使用的框架和工具链进行深度分析，自带丰富插件，已被大量企业与开发者广泛采用。

- 🔍 核心功能：查找并修复未使用的依赖、导出和文件，帮助精简代码库。
- ⚙️ 分析原理：从细粒度入口点出发，结合真实框架与 monorepo 工具链，提供准确且可操作的结果。
- 📈 流行程度：每月下载量超 4000 万次，超过 15,000 个公共项目在使用。
- 🔌 插件生态：内置 150+ 插件，覆盖 Astro、Cypress、ESLint、Jest、GitHub Actions、Next.js、Svelte、Vite 等主流工具。
- 🧪 上手体验：提供在线 Playground 供试用，并有专门的问题排查文档。
- 🏢 企业信任：Shopify 等顶尖软件团队均在使用。
- 🎥 学习资源：有社区发布的介绍视频，以及多语言技术文章（含日文、泰文、法文等）。
- 👥 开源社区：由 268 位贡献者共同维护，贡献体验获好评。
- 💬 用户口碑：开发者称赞“Knip 是我最喜欢的软件”“加入 CI 后删除 10 万行死代码”，Vercel 团队用它删除了约 30 万行无用代码。
- ✅ 实战效果：在大型 monorepo 中无假阳性，能发现仅测试或 stories 中使用的无用函数和组件。
- 🧹 维护价值：减少代码和依赖可提升性能、降低维护成本，让重构更轻松。
- 🛠️ 扩展集成：支持 VSCode/Cursor 扩展，可通过 MCP 快速生成配置文件。

---

### [](https://github.com/paradedb/drizzle-paradedb)

**原文标题**: [GitHub - paradedb/drizzle-paradedb: Official extension to Drizzle for use with ParadeDB · GitHub](https://github.com/paradedb/drizzle-paradedb)

overview summary
这是 ParadeDB 为 Drizzle ORM 提供的官方集成，基于 pg_search Postgres 扩展，支持全文搜索和向量检索，并可直接管理 ParadeDB 索引及执行完整查询 API。

- 📦 官方集成：ParadeDB for Drizzle，基于 pg_search Postgres 扩展构建。
- 🔍 支持全文搜索与向量搜索（pgvector 类型）。
- 🛠️ 兼容要求：Node 22.12+、Drizzle 1.0+、ParadeDB 0.25.0+、PostgreSQL 15+。
- 📚 提供丰富示例：快速开始、向量搜索、分面搜索、混合搜索（RRF）、RAG、自动完成及 More Like This。
- 🤝 贡献与支持：可通过 GitHub Issues 报问题，Slack 社区、GitHub Discussions 获取帮助，也提供商业支持。
- 📄 许可证：采用 MIT License 开源。

---

### [](https://github.com/ajinabraham/njsscan)

**原文标题**: [GitHub - ajinabraham/njsscan: njsscan is a semantic aware SAST tool that can find insecure code patterns in your Node.js applications. · GitHub](https://github.com/ajinabraham/njsscan)

njsscan 是一个针对 Node.js 应用的静态安全测试（SAST）工具，结合 libsast 模式匹配和 semgrep 语义搜索，用于检测不安全代码模式，支持多种输出格式与 CI/CD 集成。

- 🛡️ **核心功能**：njsscan 可发现 Node.js 应用中的不安全代码模式，覆盖 OWASP 与 CWE 漏洞类型。
- 📦 **安装方式**：通过 `pip install njsscan` 安装，要求 Python 3.10+，仅支持 Mac 和 Linux。
- ⚙️ **命令行选项**：支持 JSON、SARIF、SonarQube、DefectDojo、GitLab SAST、HTML 等输出格式，并可指定输出文件。
- 🔍 **示例输出**：检测结果包含规则 ID、OWASP/CWE 分类、严重性、文件位置及匹配字符串等详细信息。
- 🐍 **Python API**：可导入 `NJSScan` 类对源代码目录进行扫描，并获取结构化 JSON 结果。
- 📄 **配置文件**：通过 `.njsscan` 文件自定义扩展名、忽略规则、严重性过滤与覆盖，也可用 `--config` 指定配置。
- 🚫 **抑制误报**：在源码行添加 `// njsscan-ignore: rule_id` 注释即可跳过指定规则检测。
- 🔄 **CI/CD 集成**：内置 GitHub Action、GitLab CI/CD、Travis CI、Circle CI 等集成方案，便于在流水线中使用。
- 🐳 **Docker 支持**：提供预构建镜像 `opensecurity/njsscan`，也可本地构建后通过挂载源码目录运行。
- 📚 **扩展生态**：基于 njsscan 构建的 nodejsscan 提供漏洞管理界面与更多第三方集成。

---

### [](https://github.com/productdevbook/hucre)

**原文标题**: [GitHub - productdevbook/hucre: Zero-dependency spreadsheet engine. Read & write XLSX, CSV, ODS. Pure TypeScript, works everywhere. · GitHub](https://github.com/productdevbook/hucre)

hucre 是一个零依赖、纯 TypeScript 开发的电子表格引擎，支持读写 XLSX、CSV、ODS、JSON/NDJSON、XML 等格式，并可读取 XLS、XLSB；具备流式处理、树摇优化、跨平台运行、丰富的样式与图表能力，内置 CLI、模板引擎、Builder 和多种工具函数。

- 📦 零依赖、纯 TypeScript，可在 Node、Deno、Bun、浏览器、Cloudflare Workers 等环境运行。
- 📄 支持读写 XLSX、CSV、ODS、JSON/NDJSON、XML，并可读取 XLS 与 XLSB（两者只读）。
- 🌳 完全 tree-shakeable，按需导入子路径，gzip 后仅约 4–129KB（视导入范围而定）。
- ⚡ 提供流式读写（XLSX/CSV/NDJSON/ODS/XML），对超大文件保持常量内存占用。
- 🎨 支持单元格样式、自动列宽、条件格式（13 种）、数据验证、超链接、图片、批注、合并单元格、富文本、Excel 2024 原生复选框等。
- 📊 图表功能强大：可读取、克隆、生成柱状/折线/饼图等，支持系列、坐标轴、图例、数据标签等配置。
- 🔄 支持透视表的结构读写和图表/宏的 round-trip 保留；编辑他人文件时用 openXlsx/saveXlsx 可逐字节保留未建模部分。
- 🔐 内置 XLSX 密码保护（Agile 加密），并支持读取加密的 XLSB；零依赖 WebCrypto 实现。
- 🧩 提供统一 API（read/write/readObjects/writeObjects），自动识别容器格式与文本格式。
- 🖥 CLI 工具支持 convert、inspect、validate，可处理 stdin/stdout，并支持多种输入输出格式。
- 📝 内置模板引擎（{{placeholder}} 填充）、流式 Builder API 和 Sheet 操作（插入/删除/排序/克隆等）。
- 📋 CSV 能力丰富：BOM/编码检测、分隔符自动识别、流式读写、防公式注入（escapeFormulae）。
- 📐 提供 Excel 日期序列转换、数字格式渲染、单元格引用解析、schema 校验等工具函数。
- ♿ 支持 WCAG 2.1 AA 可访问性审计，包含对比度检查、alt 文本和 workbook 摘要。
- 🚀 对比 SheetJS/ExcelJS 等库，优势为零依赖、原生 ESM、CSP 合规、边缘运行时支持。
- 🗺 路线图中尚未实现：公式求值引擎、流式 XML 读取、XLS/XLSB 写入、部分条件格式与切片器合成等。

---

### [发布 v4.15.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.15.0)

**原文标题**: [Release v4.15.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.15.0)

overview summary
NodeBB v4.15.0 于 2026 年 8 月 12 日发布，是一次功能更新，重点增强联邦宇宙（Fediverse/ActivityPub）集成、优化话题投票体验，并修复大量安全与稳定性问题。
- 🚀 新增 Fediverse 群组聊天权限、上传界面优化及通知点击处理等特性。
- 🌐 ActivityPub 改进：增加缓存、远程话题回填、全局时效截止，并强化来源验证与循环 URI 过滤。
- 🗳️ 话题与世界信息流新增即时投票界面，支持回滚。
- 🔒 安全修复：新增禁用 IP 日志开关，限制请求体/响应大小，修复会话令牌暴露与用户存在性泄露等问题。
- 🛠️ 大量 Bug 修复：覆盖翻译、通知、聊天、用户界面、签名验证、中继管理及权限检查等。
- ♻️ 重构：HTTP 消息签名升级至 RFC 9421 标准，迁移至@misskey-dev 库，统一中继状态存储。
- 🧪 测试：修复现有测试并新增跨域 Actor、中继广播等测试用例。

---

### [首页 | NodeBB](https://try.nodebb.org/)

**原文标题**: [Home | NodeBB](https://try.nodebb.org/)

概述：该内容展示了 NodeBB 论坛演示实例的界面信息，包括功能限制、讨论分区及测试用途。

- 🚫 浏览器需启用 JavaScript，否则只能以只读模式浏览。
- ⏸️ 为防止垃圾信息，新用户发帖功能已被暂停，但允许浏览。
- 💬 “General Discussion”分区用于自由讨论，当前有 5 个主题和 7 个帖子。
- 📢 提供“Federated Testing”类别，用于测试联邦协议，帖子可同步至 Mastodon、Lemmy 等平台。
- 🧪 “Testing Ground”分区允许所有人（包括访客）发帖测试功能，当前暂无内容。
- 🏠 该站点为 NodeBB 官方演示实例，采用默认配置，并通过 Widgets 系统显示说明信息。

---

### [](https://github.com/squirrelchat/smol-toml)

**原文标题**: [GitHub - squirrelchat/smol-toml: A small, fast, and correct TOML (1.1.0) parser and serializer · GitHub](https://github.com/squirrelchat/smol-toml)

smol-toml 是一个面向 JavaScript/Node.js 生态的小型、快速且符合 TOML v1.1.0 规范的解析与序列化库。它旨在解决现有 TOML 解析器普遍过时、维护不足或不兼容的问题，目前已成为 npm 上下载量最高的 TOML 解析器，并广泛用于生产环境。该库在性能基准测试中表现优异，同时提供了大整数、日期类型扩展等高级配置选项。

- 📦 核心定位：小型、快速、正确的 TOML v1.1.0 解析与序列化库，npm 下载量第一，已用于生产系统。
- 🎯 开发动机：现有 JS 生态的 TOML 解析器要么过时、要么不维护、要么不符合规范，因此需要更可靠的选择。
- ✅ 合规性：通过大部分 toml-test 测试，但出于性能考虑，不拒绝无效 UTF-8 字符串/注释，以及部分无效日期（如 `2023-02-30` 会被解析为 `2023-03-02`）。
- ⚠️ 整数限制：默认将整数解析为普通 JS 数字，会丢失类型信息且无法安全表示超过 53 位的整数；可开启 `integersAsBigInt: true` 或 `"asNeeded"` 来支持大整数与类型保留。
- 🔧 安装与用法：`pnpm | yarn | npm i smol-toml`；支持 `import { parse, stringify } from 'smol-toml'` 或 `import * as TOML`。
- 📝 序列化规则：对象中的 `undefined`/`null` 会被忽略，但数组中的会被拒绝；函数、类、符号也会被拒绝；浮点数若无小数部分（如 `1.0`）默认会序列化为整数。
- 📅 日期支持：使用扩展的 `TomlDate` 对象表示所有 TOML 日期类型，也支持 Temporal API；但 `ZonedDateTime` 序列化时会转为固定偏移，丢失时区名称。
- ⚡ 性能表现：解析规范示例约 4.16 µs/iter、5MB 文件约 113.76 ms/iter；字符串化规范示例约 2.29 µs/iter、5MB 文件约 45.33 ms/iter，整体明显快于多数同类库。
- 🐢 对比提醒：fast-toml 解析速度略快，但以牺牲正确性为代价，未通过 TOML 测试套件，不宜作为可靠选择。

---

### [](https://github.com/taskforcesh/bullmq)

**原文标题**: [GitHub - taskforcesh/bullmq: BullMQ - Message Queue and Batch processing for NodeJS, Python, .NET, Elixir, Rust and PHP based on Redis or PostgreSQL · GitHub](https://github.com/taskforcesh/bullmq)

overview summary  
BullMQ 是一个基于 Redis 或 PostgreSQL 的高性能分布式任务队列，支持 Node.js、Python、.NET、Elixir、Rust 和 PHP 等多种语言。它以原子性、可靠性和丰富的特性著称，提供官方前端、FlowProducer 父子任务依赖、去重、限流等功能，并拥有活跃的开源社区。

- 🚀 **核心定位**：最快的、最可靠的基于 Redis 的分布式队列，注重原子性和稳定性。
- 🌐 **多语言支持**：原生支持 Node.js/Bun、Python、Rust、Elixir、.NET、PHP，并有 Proxy 供其他平台使用。
- 📦 **快速入门**：通过 `yarn add bullmq` 安装，用 `Queue` 添加任务、`Worker` 处理任务、`QueueEvents` 监听完成/失败事件。
- 🔗 **父子任务依赖**：使用 `FlowProducer` 可创建复杂的任务依赖树，支持多层级子任务。
- 🛠️ **功能对比优势**：相比 Bull、Kue、Bee、Agenda 等，BullMQ 独有的特性包括可观测性、批量支持、去重（节流/防抖）、父子依赖等。
- 📊 **官方前端**：Taskforce.sh 提供专业 UI，可查看队列概览、检查/搜索/重试/提升延迟任务，以及查看指标和统计。
- 💡 **性能增强**：Dragonfly 作为 Redis 的替代品，可显著提升 BullMQ 性能，利用多核 CPU 和更高效的数据结构。
- 🤝 **社区与生态**：拥有 9.3k Stars、663 Forks、267 Issues、109 PR，并有多个赞助商和大量贡献者。
- 📚 **文档与教程**：提供官方文档、博客教程、贡献指南，并采用 MIT 许可证。

---

### [](https://github.com/biw/swift-node)

**原文标题**: [GitHub - biw/swift-node: Build typed Node.js native modules in Swift · GitHub](https://github.com/biw/swift-node)

swift-node 是一个用 Swift 编写 Node.js 原生模块的工具，通过注释标记自动生成 Node-API 插件和 TypeScript 声明，无需手写 C++ 胶水或运行时加载器。

- ⚡️ 核心机制：使用 `// @swift-node:export` 注释标记函数，自动生成桥接代码、TS 声明和原生二进制，输出到 `dist_swift-node/`。
- 🚀 快速开始：运行 `npx swift-node init` 创建项目，执行 `npm run build` 构建，再从 `./dist_swift-node/index.mjs` 导入函数即可。
- 🔒 导出限制：仅函数可导出；类、结构体、枚举不能直接导出，但可作为参数/返回值（通过 Codable 或轻量 ABI 桥传递）。
- 📦 数据类型：支持 String、number、Bool、Data/Uint8Array、数组/字典、JSON 安全对象及 Codable 类型；可空值映射为 `null`。
- 🧠 函数行为：支持 `throws`、`async`/`async throws`、`@MainActor` 和一次性 `@escaping` 回调；异步返回 Promise，错误会 reject。
- ⛔️ 不支持项：泛型函数、重载、直接导出非函数、AsyncSequence 返回等，均提供了相应的替代方案。
- 🛠 命令与集成：提供 `swift-node init`、`build`、`doctor` 命令；可选集成 tsdown，通过 `swift-node-unplugin` 处理原生资源输出。
- 🌊 流式支持：`@swift-node:stream` 可将 AsyncStream 导出为带回调的订阅，支持 `cancel()` 和 `Symbol.dispose()` 清理资源。
- 🔄 CI 与发布：`init` 可生成 GitHub Actions 工作流，预编译多平台二进制，默认附带 Swift 运行时，便于 npm 发布。
- 📋 环境要求：Node.js 24+，需 `swiftc` 和 `clang++`，支持 macOS、Linux、Windows；许可证为 MIT。

---

### [发布 v5.0.0-rc.1 · vitest-dev/vitest · GitHub](https://github.com/vitest-dev/vitest/releases/tag/v5.0.0-rc.1)

**原文标题**: [Release v5.0.0-rc.1 · vitest-dev/vitest · GitHub](https://github.com/vitest-dev/vitest/releases/tag/v5.0.0-rc.1)

Vitest v5.0.0-rc.1 是一个预发布版本，带来了多项破坏性变更、新功能、大量 Bug 修复和性能优化。重点包括内联项目配置行为调整、异步断言检查、嵌套项目支持、浏览器测试改进、CLI 增强，以及多个稳定性和性能问题修复。

- 💥 破坏性变更：内联项目默认继承根配置；新增嵌套项目支持；内联项目间共享 Vite 服务器；未等待的异步断言现在会导致测试失败。
- 💥 破坏性变更：启用对 Temporal 的模拟而无需 fake timers；spy 保留类 mock 的原型方法；expects/matchers 类型增加了更好的 Promise 支持。
- 💥 破坏性变更：`-t` 参数使用 `>` 作为分隔符且只计算一次；浏览器失败截图保存到 `attachmentsDir`。
- 🚀 新功能：报告耗时占比；CLI 支持 `-p` 作为 `--project` 的简写；VM 池支持 `require(esm)`。
- 🐛 Bug 修复：修复 watch 模式并发重启合并、`--typecheck` 误报成功、源码内测试在模块缓存时收集、超时错误堆栈显示真实消息、陈旧 mock 元数据导致 automocking 失效等问题。
- 🐛 Bug 修复：修复 teardown 时丢失 worker 输出、浏览器测试窗口事件、`connectTimeout` 从项目配置读取、预捆绑 Vite 模块运行器、依赖重载警告、内部优化器依赖配置等问题。
- 🐛 Bug 修复：修复 cache 模块弹性、`globalSetup` 阻塞时 `CTRL+c` 退出、expect 的 `toHaveProperty` 处理 nullish、reporters 打印父级 describe、runner 访问 `error.stack` 抛错、spy 错误提示、typecheck Windows 崩溃报告、`./src/*` 导出移除、VM 池保留测试文件等问题。
- ⚡ 性能：降低 `--changed` 在大图上的峰值内存占用；浏览器框架资源作为不可变资产提供。

---

### [](https://react.statuscode.com/)

**原文标题**: [React Status](https://react.statuscode.com/)

React Status 是一份每周精选的 React 技术资讯通讯，内容涵盖 Hooks、模式、性能、React Native 及生态动态，自 2016 年 8 月起已累计发布 486 期，并提供订阅、历史期刊、RSS 及隐私合规说明。

- 📰 每周精选 React 生态重要资讯，帮助开发者保持跟进
- 🪝 覆盖 Hooks、设计模式、性能优化与 React Native 等核心主题
- 🔢 已发布 486 期，自 2016 年 8 月持续更新至今
- 📬 支持订阅服务，也可查看最新一期或全部历史期刊
- 📡 提供 RSS 订阅方式，方便不同阅读习惯的开发者
- 🔒 明确声明遵守隐私、反垃圾邮件及 GDPR 相关政策

---

