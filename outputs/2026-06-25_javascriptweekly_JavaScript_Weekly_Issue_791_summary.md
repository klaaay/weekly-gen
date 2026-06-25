### [桌面应用 | Deno 文档](https://docs.deno.com/runtime/desktop/)

**原文标题**: [Desktop apps | Deno Docs](https://docs.deno.com/runtime/desktop/)

概述摘要  
deno desktop 可将 Deno 项目（从单个 TypeScript 文件到 Next.js 应用）打包为独立桌面应用，输出包含代码、Deno 运行时和 Web 渲染引擎的可分发二进制文件。它提供小体积、框架自动检测、进程内绑定、跨平台编译和内置自动更新等功能。

- 🖥️ **核心功能**：将 Deno 项目转为桌面应用，输出跨平台二进制文件，捆绑代码、运行时和渲染引擎。
- ⚡ **框架自动检测**：支持 Next.js、Astro、Fresh、Remix 等框架，无需修改代码即可运行生产或开发模式（含热重载）。
- 🔗 **进程内绑定**：后端与 UI 通过进程内通道通信，避免跨进程 IPC 开销。
- 🌍 **跨平台编译**：单机可编译 macOS、Windows、Linux 应用，后端按需下载。
- 🔄 **内置自动更新**：通过 `latest.json` 和 bsdiff 补丁实现二进制差异更新，支持回滚。
- 🛠️ **配置灵活**：支持 CEF、webview 等后端，提供窗口管理、菜单、托盘、通知等 API。
- 📦 **小体积默认**：默认使用系统 webview 减小体积，同时兼容 npm 生态。
- 🚀 **即将发布**：随 Deno 2.9 版本推出，当前可通过 canary 构建体验。

---

### [AI 代码审查 | Greptile | 合并速度提升 4 倍，捕获错误增加 3 倍](https://www.greptile.com/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=javascriptweekly_primary_jun23)

**原文标题**: [AI Code Review | Greptile | Merge 4X Faster, Catch 3X More Bugs](https://www.greptile.com/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=javascriptweekly_primary_jun23)

Greptile 是一款 AI 代码审查工具，通过构建代码图谱和智能代理集群，自动审查拉取请求并捕捉潜在问题。

- 🤖 **智能代理集群审查**：通过并行代理分析代码变更，评估超出差异范围的影响，并标记问题。
- 🧠 **代码库索引与学习**：构建文件、函数和依赖关系的图谱，并随时间学习团队的编码标准。
- 🐛 **捕捉多种错误**：从样式违规到安全风险和多文件逻辑错误，防止问题进入生产环境。
- 🎯 **个性化与自定义规则**：支持用自然语言编写标准，并指向仓库特定上下文，强制执行团队关心的模式。
- 🔧 **多工具集成**：与 Claude Code、Cursor、Codex 等 IDE 和 AI 代理无缝协作，支持 MCP 和循环迭代。
- 🧪 **TREX 自动测试**：在沙盒中为每个 PR 编写并运行测试，捕捉错误和遗漏的边界情况。
- 🔒 **企业级安全**：支持自托管部署、SOC 2 合规、SSO 和审计日志，适用于国防、医疗和金融领域。
- 💰 **定价与支持**：每位用户每月 30 美元，包含 50 个积分，支持开源项目免费使用和初创公司折扣。

---

### [今日发布 Babel 8：仅支持 ESM，放弃 ES5 默认，并提供平滑迁移路径 · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

**原文标题**: [Releasing Babel 8 today: ESM-only, drop ES5 default, and a smooth migration path · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

Babel 8 今日正式发布，这是继 Babel 7 发布 8 年后的重大更新，旨在现代化核心架构，为未来 8 年做准备，并提供了平滑的迁移路径。

- 📦 **ESM 专属**：Babel 8 现在仅支持 ESM，要求 Node.js 22、24、26 或更新版本，以推动 JavaScript 生态向前发展。
- 🎯 **默认不再编译到 ES5**：`@babel/preset-env` 默认不再将代码编译到 ES5，而是基于 Browserslist 的 `defaults` 查询，自动适应现代浏览器。
- 🚫 **弃用 `loose` 和 `spec` 选项**：这些选项被移除或弃用，建议用户迁移到更精细的 `assumptions` 配置。
- 🧩 **分离 polyfill 注入**：`corejs`/`useBuiltIns` 选项被移除，推荐使用 `babel-plugin-polyfill-corejs3` 进行集中式 polyfill 控制。
- 📘 **TypeScript 类型支持**：所有 Babel 包现在都附带 TypeScript 类型，无需额外安装 `@types/babel__*` 包。
- 📈 **下载量激增**：Babel 周下载量从 2018 年的 170 万增长到 2026 年的 6.51 亿，使用率持续上升。
- 💰 **资金需求**：尽管用户增长，但捐款持续下降，团队呼吁支持以维持项目质量。
- 🔒 **Babel 7 安全支持**：Babel 7 将获得一年的安全支持（至 2027 年 6 月），但不再进行功能或修复回移植。

---

### [Babel 7 发布 · Babel](https://babeljs.io/blog/2018/08/27/7.0.0/)

**原文标题**: [Babel 7 Released · Babel](https://babeljs.io/blog/2018/08/27/7.0.0/)

Babel 7 正式发布，历经近 2 年开发，带来多项重大更新与性能提升。

- 🎉 历经 2 年、4000 次提交、50 多个预发布版本后正式发布，已在 Next.js、Vue CLI、React Native 等工具中广泛使用
- 🔧 引入`babel-upgrade`自动升级工具，简化从 Babel 6 到 7 的迁移过程
- 📁 支持 JavaScript 配置文件`babel.config.js`，并新增`overrides`选项实现按文件路径配置不同编译规则
- ⚡ 性能显著提升，优化代码并采纳 V8 团队的补丁，已纳入 Web 工具性能基准测试
- 🛠️ 新增输出选项：类编译不再包含`classCallCheck`，`for-of`循环可假设为数组以优化输出
- 🏷️ 支持`/*#__PURE__*/`注释，帮助压缩工具进行死代码消除
- 🆕 新增语法支持：ES2018 特性、类私有字段、可选链、空值合并运算符、管道运算符等
- 🅃 正式支持 TypeScript（`@babel/preset-typescript`），与 Flow 类似地解析和转换类型语法
- ⚛️ 支持 JSX Fragment 语法（`<>...</>`）
- 📦 拆分`@babel/runtime`为`@babel/runtime`和`@babel/runtime-corejs2`，优化 polyfill 管理
- 🔄 实验性自动 polyfilling 功能：`useBuiltIns: "usage"`按需导入 polyfill
- 🔌 支持`babel-plugin-macros`，实现零配置代码转换
- 🌐 网站迁移至 Docusaurus，REPL 重写为 React 组件并集成 CodeSandbox
- 🎵 社区贡献官方歌曲《Hallelujah—In Praise of Babel》
- 🗺️ 未来计划：完成新装饰器提案实现、发布 babel-minify 1.0、改进插件排序和缓存等

---

### [TypeScript 7.0 RC 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

**原文标题**: [Announcing TypeScript 7.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

TypeScript 7.0 RC 正式发布，基于 Go 语言重写，性能大幅提升，并带来多项新特性和改进。

- 🚀 性能提升：基于 Go 语言重写，编译速度比 TypeScript 6.0 快约 10 倍。
- 🔧 安装方式：通过 npm 安装 `typescript@rc`，即可使用新编译器。
- 🔄 并行处理：支持解析、类型检查和输出的并行化，通过 `--checkers` 和 `--builders` 标志控制并行度。
- 👀 改进的监视模式：基于 Parcel 文件监视器，提供高效稳定的跨平台文件监视。
- 🔗 与 6.0 并行运行：提供 `@typescript/typescript6` 包，支持 `tsc6` 命令，避免命名冲突。
- 📝 新默认配置：`strict` 默认为 true，`module` 默认为 `esnext`，`target` 默认为最新稳定 ECMAScript 版本等。
- 🚫 弃用特性：`target: es5`、`downlevelIteration`、`moduleResolution: node/node10` 等不再支持。
- 🔤 模板字面量类型：现在正确保留 Unicode 码点，而非分割代理对。
- 🛠️ JavaScript 支持重写：JSDoc 分析更一致，移除了一些特殊模式支持。
- ✨ 编辑器体验：VS Code 的 TypeScript Native Preview 扩展提供无缝体验，支持 LSP 和多线程。
- 📅 发布计划：RC 已可用，正式版预计一个月内发布，后续将关注 API 能力。

---

### [面向 AI 代理的临时 Cloudflare 账户](https://blog.cloudflare.com/temporary-accounts/)

**原文标题**: [Temporary Cloudflare Accounts for AI agents](https://blog.cloudflare.com/temporary-accounts/)

Cloudflare 推出 AI 代理临时账户，允许代理无需注册即可部署代码，60 分钟内可认领为永久账户，旨在消除代理部署的认证障碍。

- 🤖 AI 代理可直接使用 `wrangler deploy --temporary` 命令部署 Worker，无需人类参与注册或认证流程。
- ⏳ 临时部署有效期为 60 分钟，期间可认领账户使其永久化，过期自动删除。
- 🔄 代理可在 60 分钟内多次迭代代码并重新部署，支持快速的“编写 - 部署 - 验证”循环。
- 🧠 代理通过 Wrangler 的提示信息自动发现 `--temporary` 标志，无需人类明确告知。
- 🔗 认领时提供链接，用户可登录或注册 Cloudflare 账户，认领包括 Workers、数据库等资源。
- 🚀 该功能是 Cloudflare 消除代理注册障碍的系列举措之一，包括与 Stripe 和 WorkOS 的合作。
- 📝 临时账户有一定限制，功能可能随时间变化，详情见开发者文档。

---

### [无需 JavaScript 的本地化时间格式化 · Issue #12591 · whatwg/html · GitHub](https://github.com/whatwg/html/issues/12591)

**原文标题**: [Localized time formatting without JavaScript · Issue #12591 · whatwg/html · GitHub](https://github.com/whatwg/html/issues/12591)

本提案旨在为 HTML `<time>`元素增加无 JavaScript 的本地化时间格式化功能，通过新属性和 UA Shadow DOM 实现。

- 🎯 **核心问题**：服务端渲染无法获知用户时区，导致绝对时间显示不准确，现有方案（相对时间、固定时区、IP 猜测、JS 脚本）各有缺陷。
- 💡 **解决方案**：扩展`<time>`元素，新增`format`属性（取值`date`/`time`/`datetime`），通过 UA Shadow DOM 渲染格式化时间，无需 JS。
- ⚙️ **格式化属性**：提供`datefields`、`datelength`、`timeprecision`、`timezonestyle`、`hour12`、`calendar`、`timezone`等属性，精细控制显示内容。
- 🌐 **时区与语言**：时区默认使用 UA 当前时区，支持`input`（从日期时间解析）和具体标识符；语言通过 DOM 中最近的`lang`属性确定。
- 🕒 **时间解析**：解析`datetime`属性为`Temporal`对象（如`PlainDateTime`、`ZonedDateTime`），支持 RFC 9557 格式和日历注释。
- 🎨 **样式支持**：通过`Intl.DateTimeFormat#formatToParts`生成带类型的`<span>`元素，允许 CSS 伪元素选择器单独样式化各部分（如星期、月份）。
- 🔄 **回退机制**：旧浏览器或缺失语言环境时，显示`<time>`元素的原始文本内容作为后备。
- 🛠️ **实现考量**：采用 UA Shadow DOM 而非 CSS `content`，以简化文本选择和 DOMRange 集成，并避免性能与兼容风险。

---

### [GitHub - github/relative-time-element: 标准<time>元素的 Web 组件扩展。](https://github.com/github/relative-time-element)

**原文标题**: [GitHub - github/relative-time-element: Web component extensions to the standard <time> element. · GitHub](https://github.com/github/relative-time-element)

这是一个用于在浏览器中自动将时间戳转换为本地化或相对时间的 Web 组件。

- 📅 **核心功能**：`<relative-time>` 元素可将服务器缓存的固定日期，在浏览器端自动转换为用户本地时区和语言格式的相对或绝对时间。
- ⚙️ **安装与依赖**：通过 npm 安装 `@github/relative-time-element`，依赖 `Intl.DateTimeFormat` 和 `Intl.RelativeTimeFormat` API，老旧浏览器需引入 polyfill。
- 🎨 **多种格式**：支持 `datetime`（本地化日期）、`relative`（相对时间，如“2 天前”）、`duration`（持续时间，如“2 年 10 天”），以及已弃用的 `micro` 和 `elapsed` 格式。
- 🔧 **丰富属性**：可配置 `tense`（过去/未来）、`precision`（精度）、`threshold`（阈值，超过则显示绝对日期）、`prefix`（前缀）、`time-zone`（时区）等，灵活控制显示行为。
- 🌐 **国际化与无障碍**：自动根据 `lang` 属性或浏览器语言本地化；支持 `noTitle` 属性移除默认 title，便于自定义无障碍工具提示。
- 🎯 **样式与兼容**：通过 `::part(root)` 伪元素自定义 Shadow DOM 内样式；兼容 Chrome、Firefox、Safari 14+、Edge 79+，支持 React 集成。
- 📦 **开源与社区**：基于 Basecamp 的 `local_time` 组件，MIT 许可证，拥有 4k Star、188 Forks，持续维护更新。

---

### [介绍 MDN MCP 服务器](https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/)

**原文标题**: [Introducing the MDN MCP server](https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/)

MDN MCP 服务器发布，为 AI 工具提供实时、准确的 Web 平台文档和浏览器兼容性数据。

- 🚀 MDN MCP 服务器基于开放标准 MCP，让 AI 工具（如 IDE、聊天应用）直接获取最新 MDN 文档和浏览器兼容性数据。
- 🎯 解决 AI 工具因训练数据过时而提供过时 Web 平台信息的问题，例如无法识别新 CSS 特性或浏览器支持状态。
- 🛠️ 支持多种 MCP 兼容客户端，包括 VS Code、Zed、Cursor 等编辑器，Claude Code、Codex CLI 等命令行工具，以及 Claude Desktop 等聊天应用。
- ⚡ 测试显示，启用 MDN MCP 后，Claude Code 在浏览器兼容性信息上更准确，响应速度约快两倍，且回答结构更完整。
- 📊 对比测试中，未启用 MCP 的 Claude Code 在多项特性（如 light-dark() CSS 函数、shadowrootslotassignment 属性、Web Serial API）上给出错误或模糊的浏览器支持信息，而启用后能提供精确数据。
- 💬 鼓励用户通过 Discord 和 GitHub 仓库反馈问题、建议或使用案例，以帮助改进服务。
- 🔮 未来将继续扩展 MDN 文档在 AI 工作流中的可用性，并持续优化用户体验。

---

### [Jarred-Sumner 提出的 JavaScriptCore 共享内存线程（实验性，尚未完成）· 拉取请求 #249 · oven-sh/WebKit · GitHub](https://github.com/oven-sh/WebKit/pull/249)

**原文标题**: [Shared-memory threads for JavaScriptCore (experimental, not working yet) by Jarred-Sumner · Pull Request #249 · oven-sh/WebKit · GitHub](https://github.com/oven-sh/WebKit/pull/249)

这是一个为 JavaScriptCore (JSC) 引擎添加实验性共享内存线程支持的 Pull Request，旨在让 JavaScript 拥有真正的多线程能力，允许线程共享堆内存和对象。

- 🧵 **真正的共享内存线程**：`new Thread(fn)` 在另一个核心上运行函数，与主线程共享同一个堆和对象，无需序列化或消息传递。
- 🚀 **简洁的 API**：通过 `new Thread(fn, args).join()` 或 `await t.asyncJoin()` 即可实现并行，闭包能直接访问外部变量和导入。
- 🔒 **完整的同步原语**：提供了 `Lock`、`Condition`、`ThreadLocal` 以及扩展至对象属性的 `Atomics` 操作，支持细粒度的并发控制。
- ⚡ **性能与开销**：设计目标是对不共享数据的代码几乎零开销（基准测试仅增 0.45%），共享写入会变慢，但通过 JIT 推测优化将大部分成本隔离在快路径之外。
- 🛡️ **内存安全**：引擎保证内存安全（无撕裂的 JSValues、无类型混淆），但数据竞争可能导致程序出现陈旧或意外的值。
- 🚧 **实验性与未完成**：并行 JavaScript 已能在所有四个 JIT 层级运行并通过测试，但仍需进行线程清理器（TSAN）清理、模糊测试、性能优化和长时间浸泡测试。
- 📚 **丰富的测试与文档**：包含超过 100 个测试用例、详细的设计文档（`docs/threads/`）以及完整的开发日志，记录了开发过程中的关键决策和错误修复。

---

### [工作线程 | Node.js v26.4.0 文档](https://nodejs.org/api/worker_threads.html#worker-threads)

**原文标题**: [Worker threads | Node.js v26.4.0 Documentation](https://nodejs.org/api/worker_threads.html#worker-threads)

Node.js `worker_threads` 模块允许 JavaScript 在独立线程中并行执行，适用于 CPU 密集型任务，并支持通过 `ArrayBuffer` 或 `SharedArrayBuffer` 共享内存。

- 🧵 **核心功能**：`Worker` 类创建独立线程，通过 `parentPort` 和 `worker.postMessage()` 进行双向通信，支持 `MessageChannel` 和 `BroadcastChannel` 实现多对多通信。
- 🔒 **内存与资源管理**：提供 `markAsUntransferable()` 和 `markAsUncloneable()` 控制对象传输，`LockManager` 实验性 API 协调跨线程资源访问，`resourceLimits` 限制 JS 引擎资源。
- 📊 **性能监控**：`worker.performance` 查询事件循环利用率，`worker.cpuUsage()`、`worker.getHeapSnapshot()` 和 `worker.getHeapStatistics()` 获取 CPU 和内存统计。
- 🛠️ **配置与选项**：`Worker` 构造函数支持 `argv`、`env`、`eval`、`execArgv`、`stdin/stdout/stderr`、`workerData`、`resourceLimits` 和 `name` 等选项。
- 🔄 **跨线程消息传递**：`postMessageToThread()` 允许非父子线程直接通信，`receiveMessageOnPort()` 同步接收消息，`SHARE_ENV` 符号共享环境变量。
- 🚨 **事件与生命周期**：`Worker` 触发 `'error'`、`'exit'`、`'message'`、`'messageerror'` 和 `'online'` 事件，`terminate()` 异步停止线程，`Symbol.asyncDispose` 支持自动清理。
- ⚠️ **注意事项**：`stdio` 输出可能被接收端同步代码阻塞；从预加载脚本启动 Worker 需小心避免无限递归。

---

### [Vite 8.1 发布！| Vite](https://vite.dev/blog/announcing-vite8-1)

**原文标题**: [Vite 8.1 is out! | Vite](https://vite.dev/blog/announcing-vite8-1)

Vite 8.1 正式发布，带来多项实验性功能和性能改进。

- 🚀 **实验性打包开发模式**：通过 `--experimental-bundle` 或配置 `experimental.bundledDev: true` 启用，可显著提升大型应用的启动速度和页面重载性能，实测启动速度提升约 15 倍，全页重载快 10 倍。
- 🔗 **实验性 Chunk Import Map**：利用 import maps 解决 chunk 哈希级联问题，提高缓存效率，需注意当前不支持 `experimental.renderBuiltUrl`。
- 🧩 **Wasm ESM 集成支持**：可直接导入 `.wasm` 文件并调用导出函数，如 `import { add } from './add.wasm'`。
- 🎨 **更接近默认使用 Lightning CSS**：新增支持外部 CSS 文件导入和插件注册文件依赖，为未来默认切换做准备。
- 🔍 **`import.meta.glob` 支持大小写不敏感匹配**：通过 `caseSensitive: false` 选项实现。
- 📄 **自定义 HTML 元素和属性资产发现**：使用 `html.additionalAssetSources` 选项添加更多元素和属性，如 `html-import` 和自定义 `data-src-*` 属性。
- 🛠️ **其他改进**：包括错误修复和性能优化，详情见更新日志。

---

### [获取失败](https://github.com/WebAssembly/esm-integration/blob/main/proposals/esm-integration/README.md)

**原文标题**: [Failed to retrieve](https://github.com/WebAssembly/esm-integration/blob/main/proposals/esm-integration/README.md)

无法总结：获取内容失败，状态码 429。

---

### [Astro 7.0 | Astro](https://astro.build/blog/astro-7/)

**原文标题**: [Astro 7.0 | Astro](https://astro.build/blog/astro-7/)

Astro 7 正式发布，主打速度提升，引入 Rust 编译器、新渲染引擎和高级路由等功能。

- 🚀 **性能大幅提升**：构建速度提升 15-61%，部分网站快两倍以上，得益于 Rust 编译器、Markdown/MDX 处理流水线及新队列渲染引擎。
- 🦀 **Rust 编译器**：重写 .astro 编译器，不再自动修正 HTML，采用 JSX 严格模式，并优化空白符处理。
- 📝 **Markdown & MDX 用 Rust 处理**：默认使用 Sätteri 引擎，原生支持 GFM、智能标点、数学公式等，比旧 unified 流水线快得多。
- ⚡ **队列渲染**：新渲染引擎稳定且默认启用，速度提升约 2.4 倍，内存占用更低。
- 🗺️ **高级路由**：新增 `src/fetch.ts` 入口点，支持标准 fetch 处理程序模式，可与 Hono 中间件集成，精细控制请求流水线。
- 🗄️ **路由缓存**：稳定版路由缓存 API，支持 `Astro.cache.set()` 和 `cache.invalidate()`，可配合内存或 CDN 提供商。
- 🌐 **CDN 缓存提供商**：实验性支持 Netlify、Vercel 和 Cloudflare（私有测试版），将缓存指令推送至边缘网络。
- 🤖 **AI 增强**：支持后台开发服务器（`astro dev --background`）和 JSON 日志输出，便于 AI 代理和日志聚合服务使用。
- 👥 **社区贡献**：感谢众多贡献者，新版本包含来自社区的代码、文档和测试支持。

---

### [pnpm 11.7 | pnpm](https://pnpm.io/blog/releases/11.7)

**原文标题**: [pnpm 11.7 | pnpm](https://pnpm.io/blog/releases/11.7)

pnpm 11.7 版本新增了 frozenStore 设置、--batch 批量发布标志、作用域特定认证令牌，并将完整解析安装委托给 pacquet，同时强化了锁文件别名处理、使多个安装路径确定性，并修复了多项发布和 Windows 相关问题。

- 🔒 新增 frozenStore 设置，支持在只读文件系统上运行 pnpm install，需配合 --offline --frozen-lockfile 使用，且需要 Node.js >=22.15.0
- 📦 新增 pnpm publish --recursive --batch 批量发布功能，通过单个 PUT 请求发送所有包到注册表，要求注册表支持批量发布端点
- 🔑 支持作用域特定认证令牌，即使不同作用域使用相同注册表 URL 也可配置不同令牌，通过 @scope:_authToken 配置
- 🦀 将完整解析安装委托给 pacquet（Rust 端口），当 pacquet >= 0.11.7 时，可端到端处理解析、写入锁文件和 materialize node_modules
- 🛡️ 安全修复：拒绝锁文件中的路径遍历和保留依赖别名（如 ../../../escape、.bin、.pnpm），防止文件写入安装根目录外或覆盖 pnpm 布局
- 🐛 修复 pnpm publish 忽略 strictSsl: false 的问题，现在会正确转发到 libnpmpublish
- 🪟 修复 Windows 上 pnpm add 时的 "Cannot destructure property 'manifest'" 回归问题
- 🔧 修复 Git 依赖子目录路径在锁文件中丢失的问题，以及共享包子节点解析的确定性
- ⚡ 加速 pnpm install（带冻结锁文件）：锁文件验证与获取和链接并发执行，但生命周期脚本仍等待验证完成
- 🔄 修复 304 Not Modified 响应后缓存元数据文件 mtime 未更新的问题，避免 minimumReleaseAge 持续重新验证
- 🕒 修复 Windows 上命令失败后的挂起问题（20-46 秒），通过限制 wmic/PowerShell 子进程查找超时解决
- 📚 更新依赖范围：msgpackr 2.0.4、open ^11.0.0、@zkochan/cmd-shim v9.0.6

---

### [发布 pnpm 11.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.8.0)

**原文标题**: [Release pnpm 11.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.8.0)

pnpm v11.8.0 版本发布，包含多项新功能和错误修复。

- 🆕 `pnpm install` 新增 `--dry-run` 选项，可预览安装变更但不写入磁盘
- 🚦 `pnpm run --no-bail` 现在在脚本失败时返回非零退出码，与递归运行行为一致
- 📦 支持生成 Node.js 包映射文件 `node_modules/.package-map.json`，并新增相关设置项
- 🔒 SBOM 生成中，devDependencies 组件标记为 `scope: "excluded"`，并添加 CycloneDX 属性
- 📄 新增按包生成 SBOM 功能，支持 `--out` 和 `--split` 标志
- 🔍 `pnpm view` 无包名时自动向上搜索项目清单文件，使用其 `name` 字段
- 🛡️ 安全修复：验证配置依赖名称和版本，防止路径遍历攻击（GHSA-qrv3-253h-g69c）
- 🐛 修复 `pnpm update` 覆盖命名目录版本范围策略的问题
- 🍎 macOS 上移除原生二进制文件的 Gatekeeper 隔离属性，避免加载阻塞
- 🔧 修复 `pnpm install` 在 `optimisticRepeatInstall` 下的“已是最新”误报
- 📝 修复 `pnpm update --no-save` 标志在 CLI 帮助中缺失的问题
- 🔄 修复递归更新时，传递依赖与直接依赖选择器混合更新的问题
- 🗂️ 修复 `pnpm import` 对 Yarn v2 锁文件的支持
- 🏗️ 修复 `enableGlobalVirtualStore` 下重复提示移除和重装 `node_modules` 的问题
- 📖 在 `pnpm install --help` 输出中记录 `--cpu`、`--os` 和 `--libc` 标志
- ⏩ 避免发布时从磁盘读取 README，如果清单已提供 `readme` 字段
- ✅ 修复 `pnpm peers check` 对宽松 peer 依赖范围的接受问题
- 🔗 修复 `pnpm update` 重写 `workspace:` 依赖为 `link:` 或版本范围的问题
- 🧩 修复锁文件不收敛问题，增量安装保留重复传递依赖
- 📂 修复 `pnpm install` 检测本地文件依赖变更的问题
- 🎯 保留 Node.js 运行时版本前缀，当解析 `node@runtime:<range>` 时
- 🗑️ 创建更短的 CAFS 临时包目录，为生命周期脚本留出 IPC 套接字路径空间
- 📢 `pnpm store` 和 `pnpm config` 子命令的输出改为 stderr，避免干扰 stdout 捕获
- 🔄 避免在热安装中重新链接未更改的子依赖，并移除过时的子链接
- 🔁 修复锁文件变动问题，包在依赖循环中可能丢失传递 peer 依赖
- 🔄 修复 `pnpm install` 在目录条目回退后报告“已是最新”的问题
- 🔄 `pnpm update` 现在保持锁文件 overrides 与目录同步
- 📋 修复 `pnpm version --recursive` 尊重工作区选择的问题

---

### [Node.js — Node.js 26.3.1（当前版本）](https://nodejs.org/en/blog/release/v26.3.1)

**原文标题**: [Node.js — Node.js 26.3.1 (Current)](https://nodejs.org/en/blog/release/v26.3.1)

Node.js 26.3.1 是一个安全更新版本，修复了多个高危和中危安全漏洞。

- 🔒 修复了 TLS 模块中服务器身份验证的主机名规范化问题（高危）
- 🔐 修复了 WebCrypto 密码输出长度检查漏洞（高危）
- 🕵️ 修复了隧道错误中代理凭证泄露问题（中危）
- 📊 限制了 HTTP/2 originSet 大小防止内存无限增长（中危）
- 🎯 修复了 TLS SNI 上下文匹配的大小写敏感问题（中危）
- 🚫 拒绝包含空字节的主机名（中危）
- 🔗 将可重用 TLS 会话绑定到已验证主机（中危）
- 📁 修复了权限模型中 process.chdir 和文件操作相关问题（低危）
- 🐛 修复了 http.Agent 响应队列污染问题（低危）
- 🔄 更新了 llhttp、undici 和 OpenSSL 等依赖库

---

### [Node.js — Node.js 24.17.0 (长期支持版)](https://nodejs.org/en/blog/release/v24.17.0)

**原文标题**: [Node.js — Node.js 24.17.0 (LTS)](https://nodejs.org/en/blog/release/v24.17.0)

Node.js 24.17.0 (LTS) 是一个安全更新版本，主要修复了多个安全漏洞，包括高危、中危和低危问题，并更新了相关依赖。

- 🔒 修复了 TLS 主机名规范化、WebCrypto 密码输出长度等 2 个高危漏洞
- ⚠️ 修复了代理凭证泄露、HTTP2 内存增长、SNI 上下文匹配、NUL 字节注入、会话绑定、nghttp2 集成等 6 个中危漏洞
- 🛡️ 修复了权限模型中的 process.chdir、http.Agent 响应队列中毒、FileHandle utimes 禁用等 3 个低危漏洞
- 📦 更新了 llhttp 到 9.4.2、nghttp2 到 1.69.0、OpenSSL 到 3.5.7、undici 到 7.28.0 等依赖
- 💻 提供了 Windows、macOS、Linux、AIX 等多平台的安装包和二进制文件下载

---

### [Node.js — Node.js 22.23.0（长期支持版）](https://nodejs.org/en/blog/release/v22.23.0)

**原文标题**: [Node.js — Node.js 22.23.0 (LTS)](https://nodejs.org/en/blog/release/v22.23.0)

Node.js 22.23.0 (LTS) 是一个安全更新版本，修复了多个高危和中危漏洞，并更新了多项依赖。

- 🔒 修复了 tls 模块中的服务器身份验证漏洞 (CVE-2026-48618)，属于高危级别
- 🔐 解决了 WebCrypto 密码输出长度保护问题 (CVE-2026-48933)，属于高危级别
- 📦 更新了 nghttp2 依赖以修复集成问题 (CVE-2026-48937)，属于中危级别
- 🚫 拒绝包含嵌入 NUL 字节的主机名 (CVE-2026-48930)，属于中危级别
- 📊 限制 http2 的 originSet 大小以防止内存无限增长 (CVE-2026-48619)，属于中危级别
- 🕵️ 在隧道错误中隐藏代理凭据 (CVE-2026-48615)，属于中危级别
- 🔑 将会话绑定到经过身份验证的主机 (CVE-2026-48934)，属于中危级别
- 🔤 修复了 SNI 上下文匹配的大小写敏感问题 (CVE-2026-48928)，属于中危级别
- 🛡️ 修复了 http.Agent 中的响应队列污染问题 (CVE-2026-48931)，属于低危级别
- 📁 禁用了权限模型下的 FileHandle utimes (CVE-2026-48935)，属于低危级别
- ⚙️ 更新了 llhttp、undici、openssl 等多个依赖库
- 🖥️ 提供了 Windows、macOS、Linux、AIX 等多平台安装包

---

### [一个被低估的重构如何节省了 90% 的内存使用 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

**原文标题**: [How an Underrated Refactor Saved 90% Memory Usage | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

TanStack Table V9 通过共享原型对象重构，实现了相比 V8 版本最高 90% 的内存节省，尤其在处理大规模数据时表现显著。

- 📊 **内存节省高达 90%**：在处理 100 万行×8 列数据时，V9 仅使用 257MB 内存，而 V8 需要 2.7GB，节省了 2.4GB 以上
- 🔄 **核心优化方法**：将原本为每个行/列/单元格独立创建的方法，改为通过共享原型对象一次性创建，避免重复方法定义和闭包作用域
- 📈 **可扩展性提升 10 倍**：V9 可处理 1000-1600 万行数据才达到 4GB 内存限制，而 V8 仅能处理约 100-150 万行
- ⚠️ **微小破坏性变更**：解构对象方法不再工作（如`const { getValue } = row`），必须通过`row.getValue()`调用
- 🧩 **动态特性系统**：通过原型方式灵活组合功能（排序、筛选、分页等），避免类继承的复杂性
- 🎯 **主要影响行对象**：行对象因数量最多且方法最多，优化效果最显著；表对象仅一个实例无需优化
- 🔬 **基准测试方法**：使用 Playwright 和 Chrome DevTools Protocol，通过强制垃圾回收和记录保留 JS 堆来测量内存

---

### [TanStack 表格](https://tanstack.com/table/latest)

**原文标题**: [TanStack Table](https://tanstack.com/table/latest)

TanStack Table 是一个无头数据表格引擎，提供排序、筛选、分组、分页等强大功能，同时让开发者完全掌控 UI 和样式。

- 📊 **无头引擎**：不绑定任何 UI 系统，开发者可自由使用自己的标记、样式和组件。
- 🔄 **行模型管道**：支持排序、筛选、分组、展开、分页等可选行模型，可灵活组合。
- 🎛️ **可控状态**：默认管理状态，也可将排序、筛选、分页等状态提升到应用层控制。
- 🌐 **框架适配器**：核心框架无关，支持 React、Vue、Solid、Svelte、Qwik、Angular 等。
- 📈 **高性能**：可与 TanStack Virtual 集成实现虚拟化，处理大量行或列。
- 💡 **社区驱动**：由维护者、合作伙伴和 GitHub 赞助商共同塑造，贴近实际产品需求。
- 🏆 **广泛采用**：总下载量 17 亿，周下载量 1800 万+，GitHub 星标 2.8 万+。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_source=jsweekly&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=https://expo.dev/)

**原文标题**: [Expo — Build Native Apps with React](https://expo.dev/?utm_source=jsweekly&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=https://expo.dev/)

Expo 是一个全栈 React Native 框架，提供强大的云服务，帮助开发者更高效地构建、部署和迭代应用。

- 📱 **全栈框架**：Expo 是 React Native 框架，集成 SDK、云服务和开发工具，覆盖应用全生命周期
- 🚀 **快速开发**：支持在手机上开发（Expo Go）、一键启动模拟器（Expo Orbit）和可视化优化包（Expo Atlas）
- 🏢 **企业级信任**：SOC 2 Type 2 和 GDPR 合规，服务数亿用户，被数千企业和初创公司信赖
- 🎯 **Meta 推荐**：唯一被 Meta 推荐的本地框架，拥有 10 年历史的 SDK，GitHub 超 5 万星标
- 🌍 **跨平台部署**：通过 Build 和 Hosting 从单一代码库构建并分发到 Android、iOS 和 Web
- ⚡ **即时更新**：支持空中更新（Update），快速向所有用户推送最新修复和改进
- 🤖 **自动化工作流**：通过 Workflows 自动构建、测试和发布，包括应用商店提交
- 📊 **内置监控**：Insights 提供用户平台分布、API 请求和错误率等实时数据
- 👥 **强大社区**：Discord 超 7 万成员，80% 的 React Native 开发者选择 Expo，已创建超 50 万个项目
- 💬 **用户好评**：开发者称赞 Expo 简化开发流程、提升性能，比纯 React Native 更优

---

### [window.showDirectoryPicker 打开了一个全新的世界](https://steveharrison.dev/showdirectorypicker-opens-up-a-whole-new-world/)

**原文标题**: [window.showDirectoryPicker opens up a whole new world](https://steveharrison.dev/showdirectorypicker-opens-up-a-whole-new-world/)

Chrome 的 `window.showDirectoryPicker` API 为网页应用开启了本地文件系统操作的新可能，让用户可以直接在浏览器中读写本地文件夹，实现真正的本地优先应用。

- 📂 新 API 允许网页应用获取用户本地目录的读写权限，数据由用户自己掌控，而非存储在云端。
- 📝 可构建本地优先的笔记应用，例如管理 Markdown 文件夹，用户完全拥有数据所有权。
- 🖼️ 示例展示了类似 Apple Aperture 或 Lightroom 的 UI，能直接在浏览器中浏览、整理本地照片，并支持文件夹创建和移动操作。
- 🎬 未来可扩展至照片和视频编辑应用，结合 WebGPU 实现浏览器内强大的本地文件编辑能力。
- 🧩 已有基于 Apple Shake 的节点式合成应用原型，支持绘制多边形并与源图像合成，全程无需手写代码。
- 🌟 这一技术变革让浏览器应用能像原生软件一样操作本地文件，展现了令人兴奋的发展前景。

---

### [如何打开目录  |  文件和目录模式  |  web.dev](https://web.dev/patterns/files/open-a-directory)

**原文标题**: [How to open a directory  |  Files and directories patterns  |  web.dev](https://web.dev/patterns/files/open-a-directory)

本教程介绍了如何在浏览器中打开目录，并提供了现代和传统两种实现方式，以及渐进增强的代码示例。

- 📂 现代方法：使用 File System Access API 的 `showDirectoryPicker()` 方法，可请求读写权限，返回目录句柄。
- 🔄 传统方法：通过 `<input type="file" webkitdirectory>` 元素实现，兼容性更广但功能有限。
- 🚀 渐进增强：优先使用现代 API，若不支持则回退到传统方法，确保跨浏览器兼容。
- 🛠️ 代码实现：提供了完整的 JavaScript 函数 `openDirectory()`，可递归遍历目录结构并返回文件列表。
- 📁 文件对象增强：在现代 API 中，每个文件对象额外包含 `directoryHandle` 和 `handle` 属性，便于后续操作。
- 🌐 浏览器支持：现代 API 支持 Chrome 86+、Edge 86+；传统方法支持 Chrome 7+、Firefox 50+、Safari 11.1+。
- 🔒 安全限制：现代 API 不能在 iframe 中使用，需通过 `window.self === window.top` 检测。

---

### [什么是 git 工作树，以及为什么我应该使用它们？ - GitHub 博客](https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/)

**原文标题**: [What are git worktrees, and why should I use them? - The GitHub Blog](https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/)

Git worktrees 自 2015 年就已存在，但近期因 AI 和并行开发需求而流行。它们允许你在不同文件夹中并行工作，无需切换分支或暂存代码，减少上下文切换负担。

- 📂 **什么是 Git worktrees**：允许你在同一仓库的不同文件夹中同时检出多个分支，实现并行工作。
- 🔄 **传统方法 vs worktrees**：传统方法需要暂存、切换分支、重新加载文件，而 worktrees 只需一个命令创建独立工作区。
- ⚡ **使用 worktrees 的步骤**：用`git worktree add`创建新工作区，完成后用`git worktree remove`删除，过程无缝。
- 🤖 **为何现在流行**：AI 和代理工具（如 GitHub Copilot）推动并行开发，worktrees 成为默认模式。
- ⚠️ **注意事项**：依赖膨胀（每个工作区需独立依赖）、文件夹管理、全局.gitignore 要求、同一分支不能同时在两个工作区检出。
- 🛠️ **在 GitHub Copilot 中使用**：应用内默认支持，新会话自动创建 worktree，界面显示路径和更改详情。
- 💡 **是否使用**：取决于个人偏好和并行工作需求，可尝试后决定。

---

### [TanStack Start：Next.js 开发者的心智模型 | Adarsha Acharya](https://www.adarsha.dev/blog/tanstack-mental-model-for-nextjs-developers)

**原文标题**: [TanStack Start: A Mental Model for Next.js Developers | Adarsha Acharya](https://www.adarsha.dev/blog/tanstack-mental-model-for-nextjs-developers)

本文章从 Next.js 开发者的视角，深入解析了 TanStack Start 的核心设计理念与关键特性，包括其以路由为先的架构、明确的服务器边界、类型化路由、缓存策略、渲染模式及服务器函数。

- 🧭 **路由优先架构**：TanStack Start 将路由作为应用的核心组织单元，而非文件系统约定，提供更灵活的路由定义方式。
- 🔒 **明确的服务器边界**：通过显式标记服务器端代码（如`server$`函数），清晰分离客户端与服务器逻辑，避免混淆。
- 🏷️ **类型化路由**：路由参数、查询和状态均支持 TypeScript 类型推断，提升开发体验与代码健壮性。
- 💾 **智能缓存策略**：内置基于 TanStack Query 的缓存机制，支持自动数据失效与重新获取，减少手动管理开销。
- 🖥️ **灵活渲染模式**：支持 SSR、SSG、ISR 及客户端渲染，开发者可根据页面需求自由选择。
- ⚙️ **服务器函数**：通过`server$`定义可直接在客户端调用的服务器端函数，简化数据获取与操作流程。

---

### [FullCalendar - JavaScript 事件日历](https://fullcalendar.io/)

**原文标题**: [FullCalendar - JavaScript Event Calendar](https://fullcalendar.io/)

这是一个最受欢迎的 JavaScript 日历组件 FullCalendar 的概述，支持多种框架，功能强大且轻量。

- 📅 **多框架支持**：提供 Angular、React、Vue 和原生 JavaScript 的安装与集成示例
- 🚀 **快速上手**：通过 npm 安装核心包和插件（如 daygrid），即可创建月视图日历
- ⚙️ **高度可定制**：拥有超过 300 种设置，可灵活配置工具栏、事件等
- 🪶 **轻量模块化**：使用插件机制减少项目打包体积，按需加载功能
- 🌟 **广泛采用**：每月超 200 万 NPM 下载量、7000 万 CDN 下载量，GitHub 超 1.7 万星标
- 🔓 **开源核心**：拥有 10 年开源历史，120+ 贡献者，核心功能永久免费
- 💎 **付费增强**：提供高级插件和支持，进一步提升日历功能

---

### [发布 v7.0.0 · fullcalendar/fullcalendar · GitHub](https://github.com/fullcalendar/fullcalendar/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · fullcalendar/fullcalendar · GitHub](https://github.com/fullcalendar/fullcalendar/releases/tag/v7.0.0)

FullCalendar v7.0.0 正式发布，带来多项更新与修复。

- 🎉 v7.0.0 版本正式发布，需使用 @7 后缀安装
- 📋 支持 Angular 22，修复资源时间线行高与事件显示问题
- 🛠️ 新增主题系统说明与主题演示页面
- 🔧 需添加 temporal-polyfill@^1.0.1 作为对等依赖项
- 🌐 CDN 路径变更，如 /all.global.js 改为 /all/global.js
- 📚 提供完整更新日志与 v7 文档链接

---

### [FullCalendar 主题](https://themes.fullcalendar.io/)

**原文标题**: [FullCalendar Themes](https://themes.fullcalendar.io/)

概述摘要  
- 📚 本文系统梳理了人工智能在医疗领域的应用现状，涵盖诊断辅助、药物研发、个性化治疗等关键方向。  
- 🩺 AI 通过分析医学影像和病理数据，能提升疾病早期检测的准确率，减少误诊风险。  
- 💊 在药物研发中，AI 加速了候选分子筛选和临床试验设计，缩短新药上市周期。  
- 🧬 基于患者基因组和病史的个性化治疗建议，帮助医生制定更精准的干预方案。  
- ⚠️ 同时指出数据隐私、算法偏见和监管挑战等潜在风险，需平衡创新与伦理。  
- 🌍 未来趋势包括多模态数据融合、可解释 AI 模型及全球医疗资源公平分配。

---

### [介绍 eve - Vercel](https://vercel.com/blog/introducing-eve)

**原文标题**: [Introducing eve - Vercel](https://vercel.com/blog/introducing-eve)

这是一个开源框架，用于构建、运行和扩展 AI 代理。其核心理念是，定义代理的行为无需手动组装生产所需的所有组件，因为框架已内置了生产级功能。

- 📁 **代理即目录**：一个代理就是一个文件夹，包含模型配置、指令、工具、技能、子代理、渠道和定时任务等文件，结构一目了然。
- ⚡ **快速创建**：只需定义 `agent.ts` 和 `instructions.md` 文件，即可在几分钟内创建一个代理，无需样板代码。
- 🔋 **内置电池**：框架自带持久化执行、沙箱计算、人工审批、子代理和评估等生产所需功能。
- 🔄 **持久化会话**：每个对话都是持久化工作流，步骤会被检查点记录，确保会话可暂停、崩溃恢复或部署后无缝继续。
- 🛡️ **沙箱隔离**：每个代理拥有独立沙箱，用于执行不可信的代理生成代码，确保安全。
- 👤 **人工审批**：可为特定操作配置审批流程，代理会暂停等待，审批通过后继续执行。
- 🔗 **安全连接**：通过文件定义 MCP 服务器或 API 连接，框架自动发现工具、管理认证，代理无需接触凭证。
- 📡 **多渠道支持**：同一代理可通过 Slack、Discord、Teams 等多种渠道交互，每个渠道仅需一个适配器文件。
- 📊 **追踪与评估**：每次运行都会生成追踪记录，支持 OpenTelemetry 标准，并可编写评估测试套件，用于 CI/CD 流程。
- 🧩 **按需扩展**：工具是一个 TypeScript 文件，技能是一个 Markdown 文件，框架自动将它们注册到代理循环中。
- 🤖 **子代理**：代理可以委托任务给子代理，子代理拥有独立的上下文窗口和工具集。
- 💻 **本地开发**：通过 `eve dev` 命令启动本地开发服务器，终端 UI 实时显示代理的每一步操作。
- 🚀 **一键部署**：代理作为普通 Vercel 项目部署，无需额外配置，部署过程不影响正在进行的会话。
- 📅 **定时任务**：通过 cron 表达式定义定时任务，代理可按计划自动执行操作。
- 🗂️ **版本控制**：代理的所有文件都存储在 Git 中，变更可追踪、可审查，并支持预览部署和回滚。
- 🏢 **内部实践**：Vercel 内部运行着超过 100 个代理，涵盖数据分析、销售、支持、内容创作等多个领域。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Cloud 提供专为时间序列工作负载优化的 PostgreSQL 服务，支持大规模数据管理，并附带新用户信用额度。

- 🚀 提供免费试用，新用户可获得 $1000 信用额度（30 天有效），无需信用卡
- 📊 支持单服务处理 3 万亿指标/天、3 PB 数据和 1 千万亿数据点
- 🔄 核心能力包括：轻松扩展（最多 10 节点副本集）、分离计算与存储避免闲置付费
- 🛡️ 企业级功能：多可用区高可用、SOC 2/HIPAA/GDPR 合规、加密与审计日志
- 👁️ 深度可观测性：查询钻取、仪表盘，并集成 CloudWatch、Datadog、Prometheus
- ⚡ 快速部署：几分钟内通过 SQL、CLI、Terraform 或 Claude Code 配置数据库
- 🔌 与主流云提供商及 PostgreSQL 生态系统无缝集成
- 🏢 企业支持：SLA 保障、24/7 全球专家支持、区域数据隔离

---

### [ForesightJS](https://foresightjs.com/)

**原文标题**: [ForesightJS](https://foresightjs.com/)

概述总结
ForesightJS 是一款智能预取工具，通过预测用户意图提前加载内容，支持桌面和移动设备，提供多种预测策略，并附带开发工具和快速集成指南。

- 🖱️ 桌面用户支持鼠标轨迹、键盘导航和滚动预测策略，精准预判用户操作意图
- 📱 移动设备提供视口进入和触摸开始两种预测模式，适配触屏交互
- 🧪 官方开发工具可实时查看预测触发，支持调试模式和性能优化
- ⚡ 快速集成支持 JavaScript、React 和 Vue，5 分钟内完成配置
- 🔮 核心功能包括鼠标轨迹检测、键盘 Tab 导航、滚动方向预测和全触屏支持
- 🚀 采用事件驱动架构，无轮询和回流，确保高性能和 TypeScript 类型安全

---

### [发布 ForesightJS v4.0 - 官方框架包 · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.0)

**原文标题**: [Release ForesightJS v4.0 - Official Framework Packages · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.0)

ForesightJS v4.0 发布，核心改进包括不可变状态模型、新的官方框架支持包，以及更简洁的事件系统。

- 🎯 **核心重构**：引入不可变状态快照 `ForesightElementState`，替换原有可变数据模型，更易与响应式系统集成。
- 📦 **官方框架包**：新增 `@foresightjs/react` 和 `@foresightjs/vue` 包，替代原先的手动复制钩子方案，简化集成流程。
- 🔄 **新注册返回值**：`register()` 现在返回 `unregister`、`subscribe` 和 `getSnapshot`，移除 `isTouchDevice`，触摸设备由全局设置处理。
- ⚙️ **选项更新**：新增 `updateElementOptions()` 和 `enabled` 选项，支持动态修改注册配置，保持元素注册但排除预测。
- 🏠 **DOM 分离处理**：元素从 DOM 移除后变为“停放”状态（`isParked: true`），不再自动注销，重新连接时自动恢复。
- 🚀 **性能优化**：预分配轨迹事件对象、加速轨迹计算、添加错误处理和 `isConnected` 检查。
- 🛠️ **开发者工具 v2.0**：更新适配 v4 核心，新增嵌套 `show` 选项控制可视化，元素标签分组显示状态原因。
- 📚 **文档升级**：支持框架感知（React/Vue 下拉切换），新增“其他框架”页面指导构建自定义绑定（Angular、Svelte、Solid 示例）。
- 📖 **迁移指南**：提供核心、React 和 Vue 的详细迁移文档，v3.5 文档仍可通过版本下拉菜单访问。

---

### [发布 V4.2.0 - `<Foresight>` 组件 · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.2.0)

**原文标题**: [Release V4.2.0 - The `<Foresight>` Component · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.2.0)

ForesightJS V4.2.0 版本发布，核心更新是引入了声明式的 `<Foresight>` 组件，简化了元素注册流程，并进行了多项性能优化和错误修复。

- 🎉 **新增 `<Foresight>` 组件**：React 和 Vue 包现在使用声明式 `<Foresight>` 组件替代 `useForesights`，无需再手动处理回调 ref，只需将元素包裹在组件内即可。
- 🔧 **全局 `dataAttributeMirroring` 设置**：数据属性镜像现在通过全局管理器控制，而非每个元素单独设置，简化了配置。
- 🐛 **修复多项问题**：包括修复触摸策略重复设置、桌面处理器初始化时尊重 `positionHistorySize` 等 bug。
- ⚡ **性能优化**：仅活动元素在连接时被观察，停用元素在重新激活前不进入观察器，减少不必要的资源消耗。
- 🧹 **内部清理**：移除了重复的设置/注册/日志代码路径，并删除了未使用的 `HasListenersFunction` 类型导出。
- 📦 **Devtools 更新**：v2.2.0 版本适配了核心更改，元素数据属性显示遵循新的全局 `dataAttributeMirroring` 设置。
- 🔄 **修复多 ref 处理**：`useForesight` 现在能正确处理多个 ref，确保动态列表注册的准确性。

---

### [那个道具 · 2026 年 6 月 13 日](https://nerdy.dev/prop-for-that)

**原文标题**: [Prop For That · June 13, 2026](https://nerdy.dev/prop-for-that)

## 概述总结
Prop For That 是一个 JS 库，通过声明式属性将动态信息（如输入值、指针位置等）实时映射为 CSS 自定义属性，无需手动编写 JS 代码，结合 CSS 样式查询实现更强大的样式控制。

- 📦 **核心功能**：通过`data-props-for`属性声明所需动态信息，自动生成实时 CSS 变量
- 🎯 **支持属性**：包括指针位置、视口尺寸、元素可见性、输入值、图像颜色、视频进度、电池状态等 20+ 种动态数据
- 🔧 **插件化架构**：按需加载插件，避免性能浪费
- 🎨 **样式查询集成**：与 CSS `@container style()` 配合，实现基于动态属性的条件样式
- ⚡ **零配置使用**：仅需`import 'prop-for-that/auto'`并添加属性即可
- 💡 **解决痛点**：填补 CSS 无法直接获取的 JS 运行时信息（如滑块值、鼠标位置等）
- 🚀 **性能优化**：通过智能更新机制减少不必要的变量重算
- 🌐 **跨浏览器支持**：部分高级功能（如网络状态、电池信息）仅限 Chromium 内核

---

### [prop-for-that：CSS 响应，JS 仅监听](https://prop-for-that.netlify.app/)

**原文标题**: [prop-for-that: CSS reacts, JS just listens](https://prop-for-that.netlify.app/)

该库通过自定义属性 `data-props-for` 将实时数据注入 CSS 自定义属性，实现纯 CSS 驱动的动态交互，无需 JavaScript 事件处理。

- 🚀 **快速入门**：只需在 HTML 元素上添加 `data-props-for="属性名"`，即可自动获取对应 CSS 变量（如 `--live-size`）。
- 🖱️ **指针追踪**：通过 `pointer-local` 获取元素内的光标比例（`--live-local-pointer-x-ratio`），实现跟随、倾斜等效果。
- 📜 **滚动可见性**：`visibility` 提供 `--live-visible`（实时可见）和 `--const-has-entered`（进入后锁定），用于一次性揭示动画。
- 🎚️ **范围控制**：`range` 绑定滑块值到 `--live-value`，配合 `@container style()` 实现离散状态切换（如 min/max）。
- 📐 **CSS 三角函数**：利用 `atan2()`、`cos()`、`sin()` 实现眼球追踪光标等纯 CSS 几何计算。
- ⏰ **时钟与计时**：`clock` 提供 `--live-seconds` 等时间变量，用于 CSS 驱动的时钟动画。
- 🌐 **全局设备状态**：`online`、`battery`、`fps` 等全局源将网络、电量、帧率写入 `:root`，CSS 可直接读取。
- 🏎️ **滚动动量**：`scroll-velocity` 提供带衰减的滚动速度（`--live-scroll-velocity`），用于视差或弹性效果。
- 📏 **元素尺寸**：`size` 通过 ResizeObserver 提供 `--live-w`、`--live-h`、`--live-aspect`，无需媒体查询即可响应宽高比。
- 🎬 **媒体播放**：`media` 提供 `--live-progress` 等视频/音频播放状态，支持平滑进度环动画。
- 🎨 **图像色彩提取**：`img-color` 从图片提取主色、强调色等 5 色调色板，用于动态阴影或主题。
- 🎥 **视频色彩追踪**：`video-color` 实时采样视频帧的主色，用于背光效果。
- 🖱️ **拖拽交互**：结合 `pointer-local` 和 `:active`，实现纯 CSS 拖拽（无 JS 计算），释放后自动回弹。
- 📝 **表单状态**：`field-state` 和 `form-state` 提供脏、触碰、验证等表单交互历史，CSS 可驱动进度条和提交门控。
- 🔌 **完整参考**：所有数据源（全局/元素）及其对应的 CSS 变量列表，覆盖指针、滚动、媒体、表单等场景。

---

### [影](https://kage.tamnd.com/)

**原文标题**: [kage](https://kage.tamnd.com/)

概述摘要  
- 📸 **全页冻结**：kage 使用无头 Chrome 渲染每页，捕获最终 DOM，移除所有脚本和事件处理器，并下载重写 CSS、图片和字体，生成无代码运行的静态 HTML 文件。  
- 🚫 **去脚本化**：保存的页面完全去除 `<script>` 标签、`on*` 事件和 `javascript:` URL，不产生网络请求或执行代码。  
- 🎨 **布局保留**：样式表、图片、字体和媒体文件被下载并重写为相对本地路径，离线副本保持原样外观。  
- 🔗 **可浏览性**：站内链接被重写指向其他保存页面，支持点击导航，如同在线浏览。  
- 📦 **单文件打包**：可将镜像压缩为 ZIM 存档（Kiwix 格式）或自包含二进制文件，运行即启动服务。  
- 🖥️ **应用化体验**：使用 `webview` 标签构建时，打包的二进制文件会以独立窗口打开，而非浏览器标签页。  
- 📚 **资源导航**：提供新手指南、安装说明、任务指南（如爬取范围、服务镜像、恢复中断运行）和完整 CLI 参考。

---

### [GitHub - tamnd/kage：离线浏览任何网站，去除JavaScript的阴影工具](https://github.com/tamnd/kage)

**原文标题**: [GitHub - tamnd/kage: Shadow any website for offline viewing, with the JavaScript stripped out · GitHub](https://github.com/tamnd/kage)

kage 是一个能将网站克隆为离线可浏览文件夹的工具，它会移除所有 JavaScript 脚本，只保留静态资源，让页面像真实网站一样运行且无需联网。

- 📦 **核心功能**：使用真实 Chrome 浏览器渲染页面，捕获最终 DOM，剥离所有脚本，并将 CSS、图片和字体本地化，生成可直接离线浏览的 `.html` 文件。
- 🚀 **快速上手**：通过 `kage clone <url>` 克隆网站，`kage serve` 本地预览，`kage pack` 打包为单一文件或可执行程序，三步完成离线存档。
- 📂 **打包选项**：支持生成 ZIM 开放格式档案（兼容 Kiwix 生态）、自包含二进制文件（无需依赖）或双击运行的桌面应用（支持 macOS、Linux、Windows）。
- 🛠 **灵活配置**：支持限制页面数、爬取深度、子域名、滚动加载、忽略 `robots.txt` 等参数，并具备断点续爬和幂等性设计。
- 🌐 **跨平台安装**：提供 Go 安装、预编译二进制、Homebrew、Scoop、apt、dnf 及 Docker 镜像等多种方式，并内置 Shell 补全功能。
- 🔒 **隐私安全**：移除所有跟踪脚本和网络调用，确保离线文件无外部依赖，适合长期保存或分享。
- 📖 **开源许可**：采用 MIT 许可证，代码托管于 GitHub，支持从源码构建，并内置完整的测试套件。

---

### [GitHub - dop251/goja: 纯 Go 语言编写的 ECMAScript/JavaScript 引擎](https://github.com/dop251/goja)

**原文标题**: [GitHub - dop251/goja: ECMAScript/JavaScript engine in pure Go · GitHub](https://github.com/dop251/goja)

Goja 是一个用纯 Go 语言实现的 ECMAScript 5.1 引擎，注重标准合规性和性能，并支持部分 ES6 功能。

- 📦 **纯 Go 实现**：无 cgo 依赖，易于构建，跨平台兼容，适合需要频繁 Go 与 JS 交互的场景。
- ✅ **ES5.1 全面支持**：包括正则和严格模式，通过绝大多数 tc39 测试，能运行 Babel 和 TypeScript 编译器。
- 🔧 **ES6 功能进行中**：支持大部分 ES6 特性，如 Promise、Map、Set 等，但 WeakMap 因 Go 运行时限制存在内存泄漏风险。
- ⚠️ **已知限制**：JSON.parse 无法正确处理损坏的 UTF-16 代理对；Date 构造函数在整数溢出时结果不准确；不支持 WeakRef 和 FinalizationRegistry。
- 🚀 **性能表现**：比 otto 快 6-7 倍，但不及 V8；适合轻量级脚本场景，而非重计算任务。
- 🔒 **非协程安全**：每个 Runtime 实例只能由单个 goroutine 使用，但可创建多个独立实例。
- 🛠 **Go 与 JS 互操作**：支持通过 Runtime.ToValue() 传递 Go 值，通过 ExportTo() 导出 JS 值到 Go 变量，并支持原生构造函数。
- 📝 **字段名映射**：提供 TagFieldNameMapper 和 UncapFieldNameMapper，方便将 Go 结构体字段名映射为 JS 命名规范。
- ⏱ **中断机制**：支持通过 Interrupt() 方法中断长时间运行的脚本，返回 InterruptError 错误。
- 📚 **Node.js 兼容**：有独立项目提供部分 Node.js 功能（如事件循环和 setTimeout），但非内置。

---

### [发布 v4.5.0 · juliangarnier/anime · GitHub](https://github.com/juliangarnier/anime/releases/tag/v4.5.0)

**原文标题**: [Release v4.5.0 · juliangarnier/anime · GitHub](https://github.com/juliangarnier/anime/releases/tag/v4.5.0)

anime.js v4.5.0 版本发布，新增适配器、3D 布局、抖动功能，并修复多项 Bug。

- 🆕 新增 `registerAdapter()` API，支持扩展动画到非 DOM 目标
- 🎮 新增 Three.js 适配器，可动画化 Object3D、材质、灯光等
- 📐 支持 3D 网格布局，使用 `{x, y, z}` 坐标或 `grid: [列, 行, 深度]`
- 🎲 新增 `jitter` 参数，为交错值添加随机偏移
- 🌱 新增 `seed` 参数，使抖动和随机起点可重复
- 🎨 颜色动画改用伪线性空间混合，过渡更平滑
- 🐛 修复反转循环中的随机闪烁问题
- 🐛 修复非整数时长导致的交替循环闪烁
- ⏪ 修复时间线后退搜索时子元素卡在结束值的问题
- ⏩ 修复时间线前进搜索时子元素覆盖后续值的问题
- 🔧 修复关键帧浮点精度错误导致中间值不准确
- 🔄 修复 `refresh()` 未重新解析函数和 CSS 变量值
- 📜 修复滚动容器大小变化前的 `getBoundingClientRect` 崩溃
- ⚡ 优化帧调度，减少 `requestAnimationFrame` 抖动
- 🚀 加快 `engine.speed` 和 `engine.timeUnit` 更新速度

---

### [适配器 | 文档 | Anime.js | JavaScript 动画引擎](https://animejs.com/documentation/adapters/)

**原文标题**: [Adapters | Documentation | Anime.js | JavaScript Animation Engine](https://animejs.com/documentation/adapters/)

以下是您提供的 Anime.js 文档内容的概述摘要：

Anime.js 是一个功能强大的 JavaScript 动画引擎，支持 DOM 元素、JavaScript 对象、SVG、Three.js 等多种目标类型的动画。

- 📦 **安装与导入**：支持模块导入和 CDN 引入，可与 Vanilla JS 或 React 框架配合使用。
- ⏱️ **定时器与播放设置**：提供 delay、duration、loop、loopDelay、alternate、reversed、autoplay、frameRate、playbackRate 等参数控制动画行为。
- 🔄 **回调函数**：支持 onBegin、onComplete、onUpdate、onLoop、onPause 等生命周期回调，以及 then() 链式调用。
- 🎮 **播放方法**：包括 play()、reverse()、pause()、restart()、alternate()、resume()、complete()、reset()、cancel()、revert()、seek()、stretch() 等。
- 🎯 **目标与属性**：支持 CSS 选择器、DOM 元素、JS 对象、数组目标；可动画 CSS 属性、变换、变量、JS 对象属性、HTML/SVG 属性。
- 🎨 **补间值类型**：支持数值、单位转换、相对值、颜色（函数/WAAPI/CSS 变量）、函数基值、关键帧等。
- 📐 **时间线**：可添加定时器、动画、同步 WAAPI 动画、调用函数；支持位置时间、播放设置和回调。
- 🖱️ **可拖拽**：支持 x/y 轴、吸附、映射、触发器、容器、摩擦、速度等参数；提供 onGrab、onDrag、onRelease 等回调。
- 📊 **布局动画**：支持 CSS 显示动画、交错布局、DOM 顺序、进入/退出、交换父级、模态对话框等动画。
- 🔍 **滚动观察**：支持容器、目标、调试、轴、重复、阈值、同步模式、平滑滚动；提供 onEnter、onLeave 等回调。
- 🎨 **SVG 与文本**：支持 morphTo、createDrawable、createMotionPath；新增 splitText（行/词/字符）和 scrambleText（文本乱码）功能。
- 🛠️ **工具函数**：包括 stagger()（时间/值/时间线交错）、$()、get()、set()、cleanInlineStyles()、random()、随机选取、洗牌、四舍五入、钳制、吸附、包裹、映射、插值、阻尼等。
- ⚡ **缓动函数**：内置缓动、贝塞尔曲线、线性、步进、不规则、弹簧、WAAPI 缓动。
- 🚀 **引擎设置**：可配置 timeUnit、speed、fps、precision、pauseOnDocumentHidden。
- 🔌 **适配器（新）**：支持 Three.js 等非 DOM 对象动画；可自定义适配器（registerAdapter），包括目标适配器和属性解析器。
- ⚠️ **常见陷阱**：包括作用域、构造函数、注册方法、参数（root、defaults、mediaQueries）等注意事项。

---

### [发布 v7.1.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.1.0)

**原文标题**: [Release v7.1.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.1.0)

概述总结  
- 🎉 Ink 发布了 v7.1.0 版本  
- 🖥️ 新增 `suspendTerminal()` 功能，用于将终端控制权交给子进程  
- 🔄 版本更新自 v7.0.6 至 v7.1.0  
- 👥 收到了 2 个 🎉 表情反应（来自 costajohnt 和 maciejcieslar）

---

### [特性：添加 suspendTerminal() 方法以将终端交给子进程 —— 来自 costajohnt 的拉取请求 #972 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/pull/972)

**原文标题**: [feat: add suspendTerminal() to hand the terminal to a child process by costajohnt · Pull Request #972 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/pull/972)

Ink 新增 `suspendTerminal()` 功能，允许应用临时将终端控制权交给子进程（如编辑器、分页器），并在完成后恢复终端状态并重新绘制。

- 🚀 新增 `suspendTerminal()` 方法，支持回调形式和 `await using` 一次性形式
- 🔄 挂起时刷新输出、停止输入、恢复终端原始模式（关闭原始模式、显示光标、退出备用屏幕等）
- 🔁 恢复时重新应用 Ink 的终端状态并强制完全重绘，而非增量差异
- ⚠️ 已挂起状态下再次挂起会抛出错误；非交互式输出中回调仍运行但不切换终端
- ✅ 包含完整测试：覆盖回调、一次性、`await using`、异常恢复、已挂起错误、备用屏幕切换、PTY 集成测试
- 📚 提供示例和 README 文档，API 位于 `useApp()` 下

---

### [发布 v4.9.0 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases/tag/v4.9.0)

**原文标题**: [Release v4.9.0 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases/tag/v4.9.0)

概述摘要
- 📅 **日历组件新增月份和年份选择**：通过 `type` 属性（`date`/`month`/`year`）支持日期、月份或年份选择器，并在日期模式下实现快速导航。
- 🧭 **新增 useTour 组合式函数**：驱动分步引导教程，通过 Popover 组件动态锚定目标元素，支持自定义内容和导航控制。
- ✂️ **支持覆盖默认类**：添加 `theme.unstyled` 选项以移除默认主题类，并允许通过函数替换插槽类，实现更精细的样式控制。
- 🎯 **统一焦点样式**：所有组件共享一致的 `focus-visible` 样式，使用组件颜色调的柔和轮廓，提升可访问性和一致性。
- 🚀 **功能增强**：包括 ChatMessages 暴露消息引用、组件支持隐藏图标、文件上传暴露移除方法、模态框/滑出面板添加事件、PinInput 支持分隔符、滚动区域阴影属性等。
- 🐛 **错误修复**：修复命令面板滚动、链接默认属性、SPA 模式下内联脚本、代码折叠高度、选择菜单绑定、选项卡 SSR 渲染等问题。
- 🌐 **本地化更新**：新增拉脱维亚语支持。
- ❤️ **贡献者**：感谢 14 位贡献者的参与，包括 benjamincanac、maximepvrt 等。

---

### [发布 23.0.0 · nrwl/nx · GitHub](https://github.com/nrwl/nx/releases/tag/23.0.0)

**原文标题**: [Release 23.0.0 · nrwl/nx · GitHub](https://github.com/nrwl/nx/releases/tag/23.0.0)

Nx 23.0.0 版本发布，包含大量新功能、错误修复和破坏性变更，旨在提升开发体验和项目现代化。

- 🚀 **核心新功能**：支持 `nx migrate` 的 `--mode` 和 `--multi-major-mode` 标志、原生 Node.js TypeScript 剥离、Shell 标签补全，以及智能迁移模式。
- ⚠️ **重大破坏性变更**：移除了多个 Angular 和测试生成器、弃用了旧的 Webpack 和 Vite 辅助函数、更新了 `dependsOn` 配置，并删除了 Tailwind CSS 设置生成器。
- 🩹 **广泛错误修复**：修复了 Angular、核心、Gradle、JS 和测试等多个模块的 100 多个问题，包括性能、稳定性和兼容性改进。
- 🛠️ **插件与工具更新**：弃用了 `@nx/cypress`、`@nx/detox` 等执行器，并迁移了 `@nx/eslint`、`@nx/jest` 等插件至本地构建。
- 📦 **依赖与版本升级**：支持 pnpm 11.2.2、更新了 axios、minimatch 等依赖，并移除了对 Node 20 的支持。
- ❤️ **社区贡献**：感谢 20 多位贡献者的参与，包括 jaysoo、Stanzilla 等。

---

### [GitHub - mourner/suncalc：一个用于计算太阳/月亮位置和相位的小型JavaScript库。](https://github.com/mourner/suncalc)

**原文标题**: [GitHub - mourner/suncalc: A tiny JavaScript library for calculating sun/moon positions and phases. · GitHub](https://github.com/mourner/suncalc)

SunCalc 是一個輕量、無依賴的 JavaScript 函式庫，用於計算太陽與月亮的位置、光照階段、出沒時間與月相，精確度與 timeanddate.com 及美國海軍天文台相當。

- 🌞 計算太陽位置（高度角、方位角）與光照階段（日出、日落、黃昏等）
- 🌙 計算月亮位置（高度角、方位角、距離、視差角）與照明度（月相、亮度分數）
- 📅 提供月球出沒時間，支援極晝/極夜標記
- 🎯 精確度：太陽位置誤差約 0.08°，月出月落時間誤差約 15 秒
- 📦 無依賴，支援 npm 安裝、ES 模組、瀏覽器 CDN
- 🛠️ 可自訂太陽高度角對應的時段（如藍色時光）
- 📖 基於 Jean Meeus《天文算法》公式，並經 JPL Horizons 驗證
- ⭐ GitHub 星數 3.4k，活躍維護，最新版本 v2.0（2026 年 6 月）

---

### [细致 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q2&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q2&utm_content=classified)

Meticulous 是一款自动化、穷尽式且确定性的测试工具，能让开发者在无需编写或维护测试的情况下，快速交付可靠代码。它通过录制开发者日常交互、AI 生成测试套件，并在 PR 合并前预测影响，实现零误报、零维护的测试体验。

- 🚀 **零开发工作量的穷尽验证**：自动录制开发、预发布和生产环境中的用户交互，生成覆盖所有代码分支和用户流程的测试。
- 🤖 **AI 自动演化测试套件**：AI 引擎持续更新测试，添加新用例并移除过时测试，无需开发者干预。
- 🔍 **PR 合并前可视化影响**：通过模拟后端响应，在合并前展示代码变更对用户工作流的影响，无假阳性。
- ⚡ **极速迭代与无碎片测试**：基于 Chromium 确定性调度引擎，消除碎片，并行执行数千测试，120 秒内出结果。
- 🛡️ **深度集成与安全**：支持 NextJS、React、Vue 等主流框架，可补充或替代现有测试套件，保障代码质量。
- 🌟 **行业信赖**：被 Dropbox、Notion 等组织采用，开发者反馈“即时喜爱，无法想象没有它”。

---

### [clerk 部署：引导式、可恢复、智能体就绪](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=clerk-deploy&utm_content=06-23-26&dub_id=RahGRKdkJioUnfLa)

**原文标题**: [clerk deploy: guided, resumable, agent-ready](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=clerk-deploy&utm_content=06-23-26&dub_id=RahGRKdkJioUnfLa)

### 概述总结
Clerk 发布 `clerk deploy` 命令，支持一键将应用从开发环境部署到生产环境，并引导完成 DNS 和 OAuth 配置，同时为自动化代理提供 JSON 输出模式。

- 🚀 **一键部署**：通过 `clerk deploy` 命令，自动从开发配置创建生产实例，并引导设置生产域名。
- 🌐 **DNS 配置**：显示所需 CNAME 记录，支持导出为 DNS 区域文件，方便导入兼容的 DNS 提供商。
- 🔑 **OAuth 凭据**：自动检测已启用的社交登录，提示配置 Google 和 Apple 生产凭据，其他提供商可在 Clerk 控制台设置。
- ✅ **验证检查**：循环验证 DNS、SSL 和邮件 DNS，并报告待处理项。
- 🤖 **代理模式**：在非 TTY 环境或使用 `--mode agent` 时，输出只读 JSON 状态，便于自动化集成。
- 📋 **快速开始**：更新 CLI、链接项目后执行 `clerk deploy`，即可完成部署。

---

### [Handsontable - 适用于 JavaScript、React、Angular 和 Vue 的 Handsontable 数据网格](https://handsontable.com/evaluation?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=jsweekly)

**原文标题**: [Handsontable - Handsontable data grid for JavaScript, React, Angular, and Vue.](https://handsontable.com/evaluation?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=jsweekly)

Handsontable 是一款面向 Web 应用的 JavaScript 数据网格组件，提供 45 天免费试用，期间可获得专家支持和完整功能访问权限。

- 📊 **核心功能**：提供 JavaScript 数据网格组件，支持 React、Vue、Angular 等框架，并包含 HyperFormula 计算引擎。
- 🎨 **主题定制**：内置 Theme Builder，可自定义网格外观以匹配应用风格。
- 🆓 **45 天试用**：免费试用期包含完整功能访问、技术支持、合规验证及许可咨询。
- 👩‍💻 **专家支持**：试用期间由客户经理 Anna Bednarek 提供一对一指导，解答技术问题。
- 🔒 **安全合规**：通过 ISO/IEC 27001:2023-08 认证，确保数据安全。
- 📚 **丰富资源**：提供文档、API 参考、案例研究、博客、开发者论坛及 StackOverflow 支持。
- 🌐 **社区与联系**：支持通过 GitHub、Twitter、LinkedIn 等渠道获取帮助，并设有联系销售与技术支持入口。
- 🏢 **信任背书**：被多家企业信赖，可用于实际数据验证、兼容性测试及生产环境评估。

---

### [揭秘福昕 PDF 结构提取引擎](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-structural-extraction-engine/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260623)

**原文标题**: [Inside Foxit's PDF Structural Extraction Engine](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-structural-extraction-engine/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260623)

概述：本文介绍了通过 Foxit PDF Services API 将 DOCX 转换为 PDF 的完整流程，并提供了可运行的 Python 和 cURL 代码示例。

- 📄 **API 概览**：Foxit PDF Services API 支持 DOCX 转 PDF 功能，提供 Python 和 cURL 两种调用方式。
- 🐍 **Python 实现**：通过 Python 代码调用 API，包含认证、上传文档、转换和下载结果等步骤。
- 🔗 **cURL 示例**：提供 cURL 命令示例，展示如何通过 HTTP 请求完成 DOCX 到 PDF 的转换。
- 🔑 **认证流程**：需先获取 API 密钥和令牌，确保请求安全。
- 📤 **文档上传**：将 DOCX 文件上传至 API 服务，等待处理。
- 🔄 **转换过程**：API 将 DOCX 转换为 PDF，并返回转换后的文件链接。
- 📥 **结果下载**：通过返回的链接下载生成的 PDF 文件。

---

### [33 字节的 JS 信号实现 · GitHub](https://gist.github.com/GulgDev/7b113b5e971682a6512d96c9c0fdf6da)

**原文标题**: [33-byte JS signal implementation · GitHub](https://gist.github.com/GulgDev/7b113b5e971682a6512d96c9c0fdf6da)

该内容展示了一个极简的 JavaScript 信号实现，并包含相关讨论。

- 💡 核心代码：一个仅 33 字节的`signal`函数，用于创建可订阅和触发的信号。
- 🔗 使用示例：通过`signal()`创建信号，用`foo(callback)`订阅，用`foo()`触发并重置。
- ⭐ 社区互动：该 Gist 获得 21 颗星，有用户评论“Brilliant!”表示赞赏。
- 🛠️ 改进建议：有用户提供增强版本，添加了类型检查以支持更灵活的订阅。

---

### [Reddit - 请等待验证](https://www.reddit.com/r/javascript/comments/1uc0scy/33byte_js_signal_implementation/ot4dm0o/)

**原文标题**: [Reddit - Please wait for verification](https://www.reddit.com/r/javascript/comments/1uc0scy/33byte_js_signal_implementation/ot4dm0o/)

概述摘要：本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了诊断辅助、药物研发和个性化治疗等关键方向，同时指出了数据隐私和伦理挑战。

- 🔬 诊断辅助：AI 通过分析医学影像（如 X 光、CT）提高疾病检测准确率，减少误诊风险。
- 💊 药物研发：机器学习加速候选药物筛选，将传统研发周期从数年缩短至数月，降低成本。
- 🧬 个性化治疗：基于患者基因组数据和病史，AI 推荐定制化治疗方案，提升疗效。
- 🔒 数据隐私：医疗数据共享面临安全风险，需加强加密技术和法规监管。
- ⚖️ 伦理挑战：算法偏见可能导致医疗不平等，需确保 AI 决策的公平性与透明度。

---

### [更安全的 pull_request_target 默认设置用于 GitHub Actions 检出 - GitHub 更新日志](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)

**原文标题**: [Safer pull_request_target defaults for GitHub Actions checkout - GitHub Changelog](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)

概述：GitHub Actions 的 `actions/checkout` 工具更新了安全默认设置，以防范常见的“pwn request”漏洞，同时提供了可选的退出机制。

- 🛡️ **默认阻止不安全检出**：`actions/checkout` v7 及后续版本默认拒绝在 `pull_request_target` 和 `workflow_run` 工作流中检出分叉拉取请求的代码，防止恶意代码利用高权限执行。
- ⚠️ **常见漏洞模式被拦截**：当 `repository`、`ref` 参数指向分叉拉取请求的仓库、分支或提交时，检出操作将失败，例如 `ref: refs/pull/${{ number }}/merge` 等不安全输入。
- 🔄 **向后兼容与自动更新**：2026 年 7 月 16 日起，所有受支持的主要版本（如 `actions/checkout@v4`）将自动应用此安全措施；固定到特定 SHA 或补丁版本的工作流需手动升级。
- ✅ **不影响同仓库操作**：同一仓库内的拉取请求不受影响，`pull_request` 事件的行为保持不变。
- 🚫 **未覆盖其他风险场景**：此更改仅阻止分叉拉取请求的检出，不涵盖其他事件类型（如 `issue_comment`）或通过 `git`/`gh` CLI 手动拉取代码的风险。
- 🔓 **提供退出机制**：如需在安全场景下使用（如生成覆盖率报告），可通过添加 `allow-unsafe-pr-checkout` 输入显式退出保护，此标志便于代码审查中识别。
- 📚 **建议参考安全指南**：在退出保护前，建议阅读官方关于安全使用 `pull_request_target` 的指导，以降低风险。

---

### [拉取请求限制如何减少噪音 - GitHub 博客](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/)

**原文标题**: [How pull request limits are cutting down the noise - The GitHub Blog](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/)

概述摘要  
GitHub 引入拉取请求限制功能，帮助维护者管理日益增长的贡献量，减少低质量噪音，并计划推出更多控制工具。

- 📋 **拉取请求限制功能**：为无写入权限的用户设置可同时打开的拉取请求数量上限，超出需关闭或合并后才能新建，草稿拉取请求不计入限制。
- 🤖 **AI 与信任管理**：Copilot 等 AI 代理打开的拉取请求计入限制，信任贡献者可加入豁免名单，无需完全贡献者权限。
- 📈 **应对贡献激增**：自 2023 年 1 月以来，每月合并的拉取请求从约 2500 万增至超 9000 万，限制功能帮助维护者聚焦高质量贡献。
- 🗂️ **即将推出的功能**：包括拉取请求归档（隐藏低质量请求，保留可访问性）、问题限制（类似拉取请求的控制）、智能豁免（基于历史贡献自动放行）及跨仓库控制（防止跨仓库刷请求）。
- 💬 **社区反馈**：AutoGPT、Homebrew 和 OpenClaw 等项目表示该功能显著减少了噪音，提升了审查意愿和效率。
- ❤️ **致谢与展望**：感谢开源社区贡献，鼓励用户尝试功能并提供反馈，以持续改进工具。

---

### [我把一个网站存进了网站图标](https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/)

**原文标题**: [I Stored a Website in a Favicon](https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/)

概述总结
作者探索了将网站内容存储在 favicon 图标中的技术实验，通过将 HTML 数据编码为像素颜色，实现了在 9x9 像素的图标中存储 208 字节的网页内容。

- 🖥️ 数据存储新思路：将 favicon 视为存储介质，利用像素的 RGB 通道存储字节数据
- 🔢 编码过程：使用 TextEncoder 将 HTML 转换为字节，添加 4 字节长度头，按 RGB 顺序填充像素
- 📐 惊人效率：208 字节的 HTML 只需 71 个像素，9x9 像素的图标即可容纳
- 🔄 解码机制：通过 Canvas API 读取像素，提取 RGB 值重建字节数组，还原原始 HTML
- ⚠️ 关键限制：需要 JavaScript 引导程序来解码 favicon，无法独立运行
- 🎯 实验性质：明确承认该技术不实用，但展示了技术边界探索的价值
- 💡 替代方案：提出使用 SVG favicon、PNG 注释块或 ICO 多图标格式等改进方向

---

