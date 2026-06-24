### [桌面应用 | Deno 文档](https://docs.deno.com/runtime/desktop/)

**原文标题**: [Desktop apps | Deno Docs](https://docs.deno.com/runtime/desktop/)

以下是对该文档的概述总结：

- 🖥️ **deno desktop 可将 Deno 项目打包为独立桌面应用**，包含代码、运行时和渲染引擎，支持跨平台分发。
- 🚀 **即将在 Deno 2.9 中稳定发布**，目前可通过 canary 构建尝试，配置和 API 可能仍有变动。
- 🎯 **核心优势**：默认使用系统原生 WebView 实现小体积，同时兼容 npm 生态；支持框架自动检测（如 Next.js、Astro、Fresh 等），无需修改代码即可运行。
- 🔗 **进程内绑定替代 IPC**：后端与 UI 通信通过进程内通道，避免跨进程开销，提升性能。
- 🔧 **跨平台编译与自动更新**：单机可构建 macOS、Windows、Linux 版本，内置二进制差异自动更新机制。
- 📂 **文档涵盖丰富功能**：包括配置、后端选择、HTTP 服务、框架集成、窗口管理、菜单、托盘、对话框、通知、热模块替换、DevTools、自动更新、错误报告、分发及与其他工具（Electron、Tauri 等）的对比。

---

### [AI代码审查 | Greptile | 合并速度提升4倍，捕获3倍更多错误](https://www.greptile.com/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=javascriptweekly_primary_jun23)

**原文标题**: [AI Code Review | Greptile | Merge 4X Faster, Catch 3X More Bugs](https://www.greptile.com/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=javascriptweekly_primary_jun23)

Greptile 是一款 AI 程式碼審查工具，能深入理解程式碼庫，自動審查 Pull Request 並發現潛在問題，已被超過 9,000 個團隊採用。

- 🤖 **AI 代理審查**：使用代理群（swarm of agents）審查 PR，不僅看差異，還能評估變更對整個程式碼庫的影響。
- 🧠 **持續學習**：透過閱讀團隊的 PR 評論，學習程式碼庫和編碼標準，審查會越來越聰明。
- 🎯 **精準捕捉問題**：能發現從風格違規、安全風險到跨檔案邏輯錯誤等多種問題，並提供具體範例。
- 🏠 **自訂規則**：支援用簡單英文撰寫自訂規則，強制執行團隊重視的編碼模式。
- 🔌 **無縫整合**：可與 Claude Code、Cursor、Devin 等 AI 代理及 IDE 整合，並提供 MCP 和 /greploop 指令。
- 🧪 **自動測試（TREX）**：TREX 代理能自動為每個 PR 編寫並執行測試，捕捉錯誤和遺漏的邊界案例。
- 🔒 **安全優先設計**：支援自託管部署、符合 SOC 2 標準，並提供 SSO、審計日誌等企業級功能。
- 💰 **定價與相容性**：每位用戶每月 30 美元，支援多種程式語言（Python、JavaScript、Go 等），並與 GitHub 和 GitLab 相容。

---

### [今日发布 Babel 8：仅支持 ESM，放弃 ES5 默认，并提供平滑迁移路径 · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

**原文标题**: [Releasing Babel 8 today: ESM-only, drop ES5 default, and a smooth migration path · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

Babel 8 正式发布，专注于现代化核心架构，为未来8年做准备，并提供了平滑的迁移路径。

- 🚀 **Babel 8 正式发布**：这是自 Babel 7 发布8年后的首个大版本，没有新增功能，而是对核心进行现代化改造。
- 📦 **纯 ESM 支持**：Babel 8 现在仅支持 ESM，需要 Node.js 22、24、26 或更新版本，以推动 JavaScript 生态向前发展。
- 🎯 **默认不再编译到 ES5**：`@babel/preset-env` 默认不再将代码编译到 ES5，而是基于 Browserslist 的默认查询（当前约为 ES2023），并默认输出 ESM 而非 CommonJS。
- 🛠️ **废弃 `loose` 和 `spec` 选项**：这些选项被移除或废弃，建议用户迁移到更细粒度的 `assumptions` 配置。
- 🔄 **提取 polyfill 注入到独立包**：`corejs` 和 `useBuiltIns` 选项被移除，推荐使用 `babel-plugin-polyfill-corejs3` 来集中控制 core-js 注入。
- 🏷️ **提供 TypeScript 类型**：所有 Babel 包现在都自带 TypeScript 类型，无需额外安装 `@types/babel__*` 包。
- 🧩 **其他破坏性变更**：包含一系列额外变更，大多数应用会受影响，建议查阅完整的迁移指南。
- 💰 **资金支持需求**：Babel 的下载量持续增长，但捐款却逐年下降，团队呼吁用户和组织通过 Open Collective 或 GitHub Sponsors 提供支持。
- 🔒 **Babel 7 支持终止**：Babel 7 将停止接收新功能和修复，仅提供一年的安全支持（至 2027 年 6 月）。

---

### [Babel 7 发布 · Babel](https://babeljs.io/blog/2018/08/27/7.0.0/)

**原文标题**: [Babel 7 Released · Babel](https://babeljs.io/blog/2018/08/27/7.0.0/)

Babel 7 在经过近两年的开发后正式发布，带来了许多重大更新和改进，包括性能提升、新工具、配置选项和语法支持。

- 🎉 Babel 7 正式发布，经过 2 年开发、4k 次提交和 50 多个预发布版本
- ⚡ 性能显著提升，已集成到 Web Tooling Benchmark 中
- 🔧 引入 `babel-upgrade` 工具，可自动完成升级迁移
- 📝 新增 JavaScript 配置文件 `babel.config.js`，支持更灵活的配置解析
- 🎯 新增 `overrides` 配置选项，允许按文件路径设置不同编译规则
- 🚫 停止对 Node 0.10/0.12/4/5 的支持，并迁移至 `@babel` 命名空间
- 🗑️ 移除年度预设（如 `preset-es2015`）和阶段预设（如 `stage-0`），推荐使用 `@babel/preset-env`
- 🏷️ 提案插件更名为 `-proposal` 而非 `-transform`
- 💨 新增输出优化选项，如 `loose` 模式、`assumeArray` 和 `/*#__PURE__*/` 注解
- 🆕 支持多种新语法，包括 ES2018 特性、类私有字段、可选链、空值合并等
- 🔷 新增 TypeScript 支持（`@babel/preset-typescript`）
- ⚛️ 支持 JSX Fragment 语法（`<>`）
- 📦 拆分 `@babel/runtime`，新增 `@babel/runtime-corejs2`
- 🧪 实验性自动 polyfill 功能（`useBuiltIns: "usage"`）
- 🎣 支持 `babel-plugin-macros` 实现零配置代码转换
- 🌐 网站迁移至 Docusaurus，REPL 重写为 React 组件
- 🎶 项目拥有官方歌曲《Hallelujah—In Praise of Babel》
- 🧑‍💻 强调开源维护者的挑战，呼吁社区支持

---

### [TypeScript 7.0 RC 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

**原文标题**: [Announcing TypeScript 7.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

TypeScript 7.0 RC 正式发布，基于Go语言重写，性能提升约10倍，同时保持与6.0版本的高度兼容性。

- 🚀 **性能飞跃**：TypeScript 7.0 基于Go语言重写，利用原生代码速度和共享内存并行，编译速度比6.0快约10倍。
- 🔄 **高度兼容**：新编译器从现有实现方法性移植，类型检查逻辑与6.0相同，经过大规模测试，稳定可靠。
- 📦 **安装与试用**：可通过 `npm install -D typescript@rc` 安装，并支持VS Code的TypeScript Native Preview扩展，体验编辑器的性能提升。
- 🔗 **并行运行**：提供 `@typescript/typescript6` 包，支持与TypeScript 6.0并行运行，避免冲突，方便过渡。
- ⚙️ **并行控制**：新增 `--checkers` 和 `--builders` 标志，可配置类型检查和项目构建的并行度，优化资源使用。
- 🛠️ **改进的Watch模式**：基于Parcel文件监视器重写，跨平台性能提升，资源消耗降低。
- 📋 **6.0默认行为**：采用6.0的新默认设置（如 `strict: true`、`module: esnext`），并废弃旧标志，需项目适配。
- 🌐 **Unicode改进**：模板字面量类型现在按Unicode代码点分割，而非UTF-16代理对，更符合直觉。
- 📝 **JavaScript支持更新**：重新设计JS文件分析，与.ts文件更一致，废弃旧模式如 `@enum`、`@class` 等。
- ✨ **编辑器体验**：基于LSP，支持多线程，新增语义高亮、排序导入等功能，语言服务器命令失败率降低20倍以上。
- 🗓️ **发布计划**：RC已可用，稳定版计划一个月内发布，7.1将提供稳定API。

---

### [为AI代理提供的临时Cloudflare账户](https://blog.cloudflare.com/temporary-accounts/)

**原文标题**: [Temporary Cloudflare Accounts for AI agents](https://blog.cloudflare.com/temporary-accounts/)

Cloudflare 推出 AI 代理临时账户，允许代理无需注册即可部署代码，60分钟内可认领为永久账户。

- 🤖 解决AI代理部署痛点：传统OAuth、复制粘贴API令牌等流程对无人值守的代理是硬性障碍，临时账户让代理直接运行wrangler deploy --temporary即可部署。
- ⏱️ 临时部署有效60分钟：代理部署的Worker、API等资源保持活跃，期间可认领为永久账户，超时自动删除。
- 🔄 支持迭代试错：代理可在60分钟内多次修改代码并重新部署，实现“写→部署→验证”的快速循环，无需人工介入。
- 💡 自动发现功能：Wrangler CLI会提示代理使用--temporary标志，无需用户手动告知，代理可自主完成部署流程。
- 🔗 认领流程简化：用户点击认领链接后，可注册或登录Cloudflare账户，将临时账户及所有资源（包括数据库等）永久化。
- 🚀 消除注册障碍的持续努力：此前已与Stripe合作让代理自动创建账户、订阅，并与WorkOS推出auth.md标准，临时账户是迈向无摩擦代理部署的又一步。
- ⚠️ 注意事项：临时账户功能可能随时间调整，具体限制请查阅开发者文档，欢迎反馈。

---

### [无需JavaScript的本地化时间格式化 · Issue #12591 · whatwg/html · GitHub](https://github.com/whatwg/html/issues/12591)

**原文标题**: [Localized time formatting without JavaScript · Issue #12591 · whatwg/html · GitHub](https://github.com/whatwg/html/issues/12591)

该提案旨在扩展HTML `<time>` 元素，使其无需JavaScript即可在服务端渲染时根据用户时区和区域设置自动格式化日期和时间，以解决当前SSR/静态渲染中时间显示不准确的问题。

- 🕒 **核心问题**：服务端渲染的HTML无法获知用户时区，导致绝对时间显示不准确，现有方案（相对时间、固定时区、IP猜测、JS脚本）各有缺陷。
- 💡 **解决方案**：扩展`<time>`元素，通过新增`format`属性（可选值`date`、`time`、`datetime`）触发自动格式化，并使用UA Shadow DOM渲染，避免直接修改DOM内容带来的性能与兼容风险。
- ⚙️ **格式化控制**：提供多个属性精细控制显示，如`datefields`（日期字段组合）、`datelength`（长度）、`timeprecision`（精度）、`timezonestyle`（时区样式）、`hour12`（12/24小时制）、`calendar`（日历类型）和`timezone`（时区）。
- 🌍 **区域与回退**：通过DOM中最近的`lang`属性确定区域设置；若浏览器不支持或区域缺失，则显示`<time>`元素内的原始回退文本。
- 🧩 **技术实现**：解析`datetime`属性为`Temporal`对象（如`ZonedDateTime`），映射至`Intl.DateTimeFormat`选项进行格式化，最终在Shadow DOM中生成带语义类名的`<span>`元素，支持CSS伪元素选择器单独样式化。
- 📋 **状态与标签**：该提案处于“孵化”阶段（stage: 1），标记为“新增/增强功能”，需进一步细化方案、测试及浏览器厂商兴趣。

---

### [GitHub - github/relative-time-element: 标准<time>元素的Web组件扩展](https://github.com/github/relative-time-element)

**原文标题**: [GitHub - github/relative-time-element: Web component extensions to the standard <time> element. · GitHub](https://github.com/github/relative-time-element)

该组件是一个Web自定义元素，用于将时间戳格式化为本地化字符串或自动更新的相对时间文本。

- 🕐 **核心功能**：将服务器缓存的ISO 8601时间戳在浏览器端自动转换为用户本地时区和语言格式的相对时间（如"3小时前"），支持JS禁用时回退显示原始文本
- 📦 **安装与兼容**：通过npm安装`@github/relative-time-element`，依赖`Intl.DateTimeFormat`和`Intl.RelativeTimeFormat` API，旧浏览器需polyfill
- ⚙️ **主要属性**：支持`datetime`（ISO时间）、`format`（datetime/relative/duration等模式）、`tense`（时态控制）、`precision`（精度）、`threshold`（相对/绝对显示阈值）等30+配置项
- 🎨 **格式化模式**：提供`datetime`（本地化日期）、`relative`（相对时间）、`duration`（精确时长）、`micro`（紧凑格式）等模式，支持`formatStyle`（long/short/narrow）调整显示风格
- 🌐 **国际化**：自动继承`lang`属性实现多语言，支持`time-zone`属性指定IANA时区，默认使用浏览器时区
- 🧩 **开发集成**：支持React项目通过类型声明使用，提供Shadow DOM的`part="root"`属性进行样式定制
- 📊 **浏览器支持**：兼容Chrome、Firefox、Safari 14+、Edge 79+，需要custom elements和Intl API支持

---

### [介绍 MDN MCP 服务器](https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/)

**原文标题**: [Introducing the MDN MCP server](https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/)

MDN MCP 服务器发布，为AI工具提供最新Web文档与浏览器兼容数据。

- 🚀 **MDN MCP 服务器发布**：基于开放标准MCP，将MDN文档与浏览器兼容数据直接接入AI代理或IDE。
- 🎯 **解决AI知识滞后问题**：AI工具常因训练数据截止而使用过时信息，MCP提供实时准确的Web平台数据。
- 🛠️ **支持多种客户端**：兼容VS Code、Zed、Cursor等编辑器，Claude Code等CLI工具，以及Claude Desktop聊天应用。
- 📊 **测试验证效果**：在Firefox 151新功能测试中，启用MCP的Claude Code浏览器支持信息更准确，响应速度约快一倍。
- ⚡ **具体案例对比**：无MCP时，Web Serial API被错误标记为“未实现”；启用MCP后正确识别Firefox 151支持。
- 💬 **社区参与**：欢迎在Discord平台频道或GitHub仓库反馈问题与建议。
- 🔮 **未来规划**：随着AI融入开发流程，MDN将持续优化文档可访问性。

---

### [Jarred-Sumner 的 JavaScriptCore 共享内存线程（实验性，尚未完成）· 拉取请求 #249 · oven-sh/WebKit · GitHub](https://github.com/oven-sh/WebKit/pull/249)

**原文标题**: [Shared-memory threads for JavaScriptCore (experimental, not working yet) by Jarred-Sumner · Pull Request #249 · oven-sh/WebKit · GitHub](https://github.com/oven-sh/WebKit/pull/249)

这是一个为 JavaScriptCore 引擎添加实验性共享内存线程支持的 Pull Request，旨在让 JavaScript 拥有真正的多线程能力，而非依赖 Web Workers 的消息传递模型。

- 🧵 核心 API：`new Thread(fn)` 在另一个核心上运行函数，共享同一堆内存和对象，无需结构化克隆或消息传递，通过 `join()` 或 `asyncJoin()` 获取结果。
- 🚀 并行能力：支持并行 `map`、共享缓存、原子操作 (`Atomics.*` 扩展至普通对象属性)、取消标志、实时进度追踪，以及基于 `Lock` 和 `Condition` 的条件变量同步。
- 🏗️ 设计基础：基于 Filip Pizlo 2017 年的设计，使用 TID 标记的扁平蝴蝶结、分段蝴蝶结、每对象单元锁和线程本地监视点，以最小化非共享代码的性能开销。
- ⚙️ 实现状态：已完成两阶段中的第一阶段（GIL 下），第二阶段（移除 GIL）正在进行中。线程测试套件在真实并行下通过，但尚未完成模糊测试、线程清理器修复和长期稳定性测试。
- 📊 性能与权衡：非共享代码性能损失约 0.45%；共享写入较慢；GC 在共享模式下目前是同步的；内存占用比 Worker 低得多（~150KB–1MB 对比 5–15MB）。
- 🧪 测试与验证：包含约 95 个测试的套件、线程清理器零未抑制报告、一个可扩展性基准测试（在 16 线程时 JavaScript 性能约为 Java 的 0.89 倍），以及一个包含 20 个 CVE 机制类的审计。

---

### [工作线程 | Node.js v26.3.1 文档](https://nodejs.org/api/worker_threads.html#worker-threads)

**原文标题**: [Worker threads | Node.js v26.3.1 Documentation](https://nodejs.org/api/worker_threads.html#worker-threads)

Node.js 的 `worker_threads` 模块支持在独立线程中并行执行 JavaScript，适用于 CPU 密集型任务，并允许通过 `ArrayBuffer` 或 `SharedArrayBuffer` 共享内存。

- 🧵 **Worker 线程**：使用 `Worker` 类创建独立执行线程，支持通过 `postMessage()` 和 `on('message')` 进行双向通信。
- 🔄 **消息通道**：`MessageChannel` 和 `MessagePort` 提供异步双向通信，支持传输结构化数据、`ArrayBuffer` 和 `MessagePort` 对象。
- 📡 **广播通信**：`BroadcastChannel` 实现一对多异步通信，所有绑定到同一名称的实例均可收发消息。
- 🔒 **锁机制**：`LockManager` 提供跨线程资源协调，支持独占和共享锁模式，防止竞态条件。
- 🧩 **环境数据**：`setEnvironmentData()` 和 `getEnvironmentData()` 允许在父线程和所有新 Worker 之间自动传递克隆数据。
- 🚫 **不可传输标记**：`markAsUntransferable()` 和 `markAsUncloneable()` 可防止对象被传输或克隆，确保内存安全。
- 📊 **性能监控**：`worker.performance.eventLoopUtilization()` 和 `worker.cpuUsage()` 提供线程级性能统计。
- 🛠️ **资源限制**：`resourceLimits` 选项可设置 JS 引擎的内存和栈大小限制，防止资源耗尽。
- ⚠️ **注意事项**：Worker 线程的 stdio 输出可能被接收端同步代码阻塞；从预加载脚本启动 Worker 时需避免无限递归。

---

### [Vite 8.1 发布！| Vite](https://vite.dev/blog/announcing-vite8-1)

**原文标题**: [Vite 8.1 is out! | Vite](https://vite.dev/blog/announcing-vite8-1)

Vite 8.1 已发布，带来多项实验性功能和性能改进，旨在提升大型应用的开发体验。

- 🚀 **实验性打包开发模式**：通过 `--experimental-bundle` 或配置 `experimental.bundledDev: true` 启用，可将打包引入开发过程。测试显示，加载 10,000 个 React 组件时，启动速度提升约 15 倍，全页重载快约 10 倍，同时保持即时 HMR，尤其适合大型应用。
- 🧩 **实验性块导入映射**：利用导入映射解决输出包中块哈希级联变化的问题，提高缓存效率。基于 Rolldown 功能构建，但注意当前不支持 `experimental.renderBuiltUrl`。
- 🌐 **Wasm ESM 集成支持**：现在可直接导入 `.wasm` 文件并使用其导出函数，例如 `import { add } from './add.wasm'`，简化 WebAssembly 使用。
- ⚡ **更接近默认使用 Lightning CSS**：Vite 8.1 新增了 PostCSS 中已有的功能（如外部 CSS 文件导入和插件注册文件依赖），为未来默认切换做准备。可通过 `css.transformer: 'lightningcss'` 试用。
- 🔍 **`import.meta.glob` 不区分大小写匹配**：新增 `caseSensitive: false` 选项，用于不区分大小写地匹配文件。
- 🖼️ **自定义 HTML 元素和属性资产发现**：通过 `html.additionalAssetSources` 选项，可为自定义元素（如 `<html-import>`）和属性（如 `data-src-dark`）指定资产来源，扩展资产发现范围。
- 📈 **下载量增长**：Vite 8 每周下载量达 4160 万次，接近 Vite 7 的总和，社区贡献者超过 1200 人。

---

### [esm集成/提案/esm集成/README.md 在主分支 · WebAssembly/esm集成 · GitHub](https://github.com/WebAssembly/esm-integration/blob/main/proposals/esm-integration/README.md)

**原文标题**: [esm-integration/proposals/esm-integration/README.md at main · WebAssembly/esm-integration · GitHub](https://github.com/WebAssembly/esm-integration/blob/main/proposals/esm-integration/README.md)

该提案描述了WebAssembly作为ES模块的集成方案，允许通过JavaScript的`import`语句或`<script type=module>`标签加载Wasm模块，目前处于WebAssembly流程的第三阶段。

- 📦 **改善模块实例化体验**：通过声明式API（如`import { foo } from "./myModule.wasm"`）替代手动获取、连接和实例化Wasm模块的繁琐过程，支持源阶段导入实现自定义实例化。
- 🔧 **统一工具链实现**：标准化集成后，webpack、Rollup、Parcel等工具可统一支持Wasm模块，Deno已实现此提案，Node.js在标志后支持，ES Module Shims提供浏览器polyfill。
- 🔄 **源阶段导入支持**：允许通过`import source`获取未实例化的`WebAssembly.Module`，支持多次实例化和自定义导入，同时利用ESM模块解析和获取机制。
- 🔗 **主机实例链接模型**：提供直接执行Wasm模块的能力，通过主机链接模型将Wasm模块与JS模块图集成，适用于无需自定义实例化的场景。
- 📥 **导入导出嵌入**：模块解析过程包括获取、解析、递归获取依赖、识别导出（函数、Table、Memory、Global等），导入映射提案增强模块说明符灵活性。
- ⏳ **导入快照机制**：导入值在实例化时快照，后续更新不反映在Wasm模块中；不支持循环Wasm模块，以避免未初始化导出导致错误。
- 📈 **渐进式实现支持**：可分两阶段实现：先支持源阶段导入（`import source`），再支持评估阶段导入（`import { ... }`），鼓励同时发布但允许分步推进。
- 🔒 **内容安全策略（CSP）集成**：通过ESM导入的Wasm模块需通过`script-src`指令验证，确保与JS在CSP下同等安全。
- ❓ **常见问题解答**：源阶段不替代实例链接模型，而是提供更灵活的ESM集成；组件模型扩展此集成；不要求`type`属性；支持命名导出；转换规则与JS API一致；实例化在评估阶段进行以避免未初始化问题；函数导入不采用跳板机制以避免开销；全局导入支持浅快照；Web API暂不直接通过模块导入，需创建JS模块包装。

---

### [Astro 7.0 | Astro](https://astro.build/blog/astro-7/)

**原文标题**: [Astro 7.0 | Astro](https://astro.build/blog/astro-7/)

Astro 7 正式发布，主打速度提升，并引入了多项重大改进。

- 🚀 **性能大幅提升**：.astro 编译器用 Rust 重写，Markdown 和 MDX 处理也改用 Rust 管道，配合 Vite 8 的 Rolldown 打包器，构建速度提升 15-61%。
- 🦀 **Rust 编译器**：新的 .astro 编译器不再自动修正 HTML，采用 JSX 风格严格性，并遵循 JSX 空白处理规则，带来更可预测的行为。
- 📝 **Markdown & MDX 在 Rust 中**：默认使用 Rust 驱动的 Sätteri 处理器，原生支持 GFM、智能标点、数学公式等，无需额外插件，构建速度显著提升。
- ⚙️ **队列渲染**：新的队列式渲染引擎取代递归方法，速度提升约 2.4 倍，内存占用更少。
- 🗺️ **高级路由**：新增 `src/fetch.ts` 入口点，允许完全控制请求管道，并兼容 Hono 框架，可灵活组合中间件。
- 💾 **路由缓存**：稳定了路由缓存功能，提供平台无关的 API (`Astro.cache.set()`)，支持按标签或路径失效，并新增 Netlify、Vercel 和 Cloudflare 的实验性 CDN 缓存提供商。
- 🤖 **AI 增强**：支持后台开发服务器 (`astro dev --background`) 和 JSON 日志输出，优化 AI 编码代理的工作流程。
- 🎉 **社区致谢**：感谢所有为 Astro 7 做出贡献的团队成员和社区贡献者。

---

### [pnpm 11.7 | pnpm](https://pnpm.io/blog/releases/11.7)

**原文标题**: [pnpm 11.7 | pnpm](https://pnpm.io/blog/releases/11.7)

以下是您提供的 pnpm 11.7 发布内容的摘要：

pnpm 11.7 引入了多项新功能和改进，包括只读包存储支持、批量发布、作用域特定认证令牌，以及将解析过程委托给 Rust 移植版 pacquet。此外，还修复了多个安全问题和错误，提升了安装和发布的稳定性与性能。

- 🔒 **新增 `frozenStore` 设置**：支持在只读文件系统（如 Nix 存储、OCI 镜像层）上运行 `pnpm install`，通过启用不可变模式避免写入操作，需与 `--offline --frozen-lockfile` 配合使用，且要求 Node.js 版本 ≥22.15.0、≥23.11.0 或 ≥24.0.0。
- 📦 **批量发布功能**：`pnpm publish --recursive --batch` 可将工作区所有包通过单个请求发送到注册表，实现全有或全无的原子性发布，需注册表支持（如 pnpr），否则报错 `ERR_PNPM_BATCH_PUBLISH_UNSUPPORTED`。
- 🔑 **作用域特定认证令牌**：允许为同一注册表 URL 下的不同作用域（如 `@org-a` 和 `@org-b`）配置独立令牌，通过 `//registry.example.com/:@scope:_authToken` 键设置，未匹配作用域则回退到注册表级令牌。
- 🚀 **解析过程委托给 pacquet**：当 `configDependencies` 中声明 pacquet（≥0.11.7）时，`pnpm install` 的依赖解析、锁文件写入和 `node_modules` 构建可完全由 Rust 引擎处理，但仍为可选预览功能。
- 🛡️ **安全强化**：拒绝锁文件中路径遍历和保留别名（如 `../../../escape`、`.bin`、`.pnpm`），防止文件写入安装根目录外或覆盖 pnpm 布局；`pnpm patch-remove` 限制在配置的补丁目录内。
- 🐛 **错误修复**：修复了 `strictSsl: false` 在发布时被忽略、Windows 上 `pnpm add` 的回归错误、Git 子目录依赖路径丢失、锁文件输出非确定性导致 `dedupe --check` 间歇性失败、`pnpm update -i` 摘要行乱码等问题。
- ⚡ **性能优化**：冻结锁文件安装时，锁文件验证与获取/链接并行执行，但生命周期脚本仍等待验证完成；`304 Not Modified` 响应更新缓存元数据 mtime，避免重复验证。
- 🖥️ **Windows 修复**：修复了因 `wmic`/PowerShell 进程查找缓慢导致的命令退出延迟（20-46 秒），现通过超时限制解决。
- 🔧 **其他改进**：`pnpm setup` 不再提示批准 `@pnpm/exe` 的构建脚本；用户定义的 `npm_config_*` 环境变量在生命周期脚本中保留；更新了 `msgpackr`、`open`、`@zkochan/cmd-shim` 等依赖版本。

---

### [发布 pnpm 11.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.8.0)

**原文标题**: [Release pnpm 11.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.8.0)

pnpm v11.8.0 版本发布，包含多项新功能和错误修复。

- 🆕 `pnpm install` 新增 `--dry-run` 选项，可预览安装变更而不写入磁盘
- 🚫 `pnpm run --no-bail` 现在在脚本失败时返回非零退出码，与递归运行行为一致
- 📦 支持生成 `node_modules/.package-map.json`，并新增 `node-experimental-package-map` 和 `node-package-map-type` 设置
- 🔍 `pnpm sbom` 现在将仅通过 `devDependencies` 可达的组件标记为 CycloneDX `scope: "excluded"`
- 📄 新增每包 SBOM 生成功能，支持 `--out` 和 `--split` 标志
- 🔎 `pnpm view` 现在在未指定包名时会向上搜索最近的项目清单文件
- 🔒 安全修复：验证配置依赖名称和版本，防止路径遍历攻击
- 🐛 修复了 `link:` 工作区协议在 `pnpm rm` 后错误切换为 `file:` 的问题
- 🖥️ 修复了进度行显示外部进程残留字符的问题
- 🍎 修复 macOS Gatekeeper 阻止原生二进制文件的问题，自动移除 `com.apple.quarantine` 扩展属性
- ⚡ 修复 `optimisticRepeatInstall` 在锁文件变化时错误报告"已是最新"的问题
- 🔄 修复递归更新时传递依赖与直接依赖选择器混合更新的问题
- 📝 在 `pnpm install --help` 输出中新增 `--cpu`、`--os` 和 `--libc` 标志文档
- 🧹 修复 `pnpm store` 和 `pnpm config` 子命令的输出流问题，警告信息现在输出到 stderr
- 🛠️ 修复了多个与工作区、目录和锁文件相关的问题

---

### [Node.js — Node.js 26.3.1（当前版本）](https://nodejs.org/en/blog/release/v26.3.1)

**原文标题**: [Node.js — Node.js 26.3.1 (Current)](https://nodejs.org/en/blog/release/v26.3.1)

Node.js 26.3.1 是一个安全更新版本，修复了多个高危和中危安全漏洞，涉及TLS、加密、HTTP/2、权限等多个模块。

- 🔒 **高危漏洞修复**：修复了TLS主机名校验（CVE-2026-48618）和WebCrypto加密输出长度（CVE-2026-48933）两个高危安全问题
- 🛡️ **中危漏洞修复**：修复了代理凭证泄露、HTTP/2内存增长、SNI大小写匹配、NUL字节注入和会话绑定等5个中危漏洞
- ⚠️ **低危漏洞修复**：修复了权限模型相关的多个低危问题，包括process.chdir、FileHandle和管道操作
- 📦 **依赖更新**：更新了llhttp到9.4.2、undici到8.5.0、OpenSSL到3.5.7
- 💻 **多平台支持**：提供Windows、macOS、Linux、AIX和ARM等多平台安装包和二进制文件

---

### [Node.js — Node.js 24.17.0（长期支持版）](https://nodejs.org/en/blog/release/v24.17.0)

**原文标题**: [Node.js — Node.js 24.17.0 (LTS)](https://nodejs.org/en/blog/release/v24.17.0)

Node.js 24.17.0 (LTS) 是一个安全更新版本，主要修复了多个安全漏洞，涵盖 TLS、crypto、HTTP/2 等多个模块。

- 🔒 TLS: 修复服务器身份检查中的主机名规范化问题（高危）
- 🔐 Crypto: 修复 WebCrypto 密码输出长度保护（高危）
- 🛡️ HTTP/2: 限制 originSet 大小以防止内存无限增长（中危）
- 🚫 DNS/Net: 拒绝包含嵌入 NUL 字节的主机名（中危）
- 🔑 TLS: 绑定可复用会话到已验证主机（中危）
- 📋 TLS: 修复 SNI 上下文匹配的大小写敏感问题（中危）
- 🕵️ Lib/Test: 隐藏隧道错误中的代理凭据（中危）
- 🔗 HTTP: 修复 http.Agent 中的响应队列污染（低危）
- ⚙️ Permission: 处理 process.chdir 在 writereport 中的问题（低危）
- 📁 Permission: 禁用权限模型下的 FileHandle utimes（低危）
- 📦 依赖更新: 包括 llhttp、nghttp2、OpenSSL、undici 等库升级

---

### [Node.js — Node.js 22.23.0（长期支持版）](https://nodejs.org/en/blog/release/v22.23.0)

**原文标题**: [Node.js — Node.js 22.23.0 (LTS)](https://nodejs.org/en/blog/release/v22.23.0)

Node.js 22.23.0 是代号 "Jod" 的 LTS 版本，主要是一次安全更新，修复了多个高危和中等漏洞，并更新了依赖项。

- 🔒 **高危安全修复**：修复了 TLS 主机名验证（CVE-2026-48618）和 WebCrypto 加密输出长度（CVE-2026-48933）两个高危漏洞。
- 🛡️ **中等安全修复**：修复了包括 nghttp2 集成问题、NUL 字节主机名拒绝、HTTP2 内存增长、代理凭证泄露、TLS 会话绑定和 SNI 匹配等 6 个中等漏洞。
- ⚠️ **低危安全修复**：修复了权限模型中的 process.chdir 和 FileHandle utimes 问题，以及 HTTP 响应队列污染。
- 📦 **依赖更新**：更新了 llhttp 到 9.4.2、undici 到 6.27.0、nghttp2 到 1.69.0、OpenSSL 到 3.5.7 等多个核心依赖。
- 🗑️ **重大变更**：移除了 HTTP2 的优先级信号支持（SEMVER-MAJOR）。
- 🖥️ **多平台支持**：提供了 Windows、macOS、Linux、AIX 和 ARM 等多种架构的安装包和二进制文件。

---

### [一次被低估的重构如何节省了90%的内存使用 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

**原文标题**: [How an Underrated Refactor Saved 90% Memory Usage | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

TanStack Table V9通过共享原型重构，大幅降低内存占用，处理百万行数据时内存节省高达90%，同时保持功能动态组合的灵活性。

- 📊 **显著的内存节省**：在100万行x8列的基准测试中，V9相比V8节省了约2.4GB内存，内存使用降低90%以上，且节省幅度随数据规模增长而扩大。
- 🔄 **关键重构方法**：将行、列、单元格等对象的共享方法移至原型对象，避免为每个实例重复创建函数和闭包，从而大幅减少内存开销。
- 🧩 **动态功能系统**：使用手动原型而非类继承，确保每个表实例仅包含已注册功能的方法，支持灵活的功能组合和树摇优化。
- ⚠️ **微小破坏性变更**：解构对象方法（如`const { getValue } = row`）不再有效，需通过对象调用（如`row.getValue()`），方法不再作为自有属性出现。
- 📈 **可扩展性提升**：V9可处理高达1000-1600万行数据（V8仅约100-150万行），为大型数据集提供更稳健的客户端支持。

---

### [TanStack 表格](https://tanstack.com/table/latest)

**原文标题**: [TanStack Table](https://tanstack.com/table/latest)

TanStack Table 是一个无头数据表格引擎，提供强大的行模型、可控状态和框架适配器，让开发者完全掌控 UI 而无需受限于预设组件。

- 📊 **无头引擎**：不绑定任何 UI 组件，开发者可自由使用自己的标记、样式和组件来构建表格。
- 🔧 **行模型管线**：支持排序、过滤、分组、展开、分页等功能，所有特性均可按需启用。
- 🎛️ **可控状态**：默认由引擎管理状态，也可将排序、过滤、分页等状态提升到应用中，实现 URL 同步或服务器查询。
- 🌐 **框架适配器**：核心模型与框架无关，提供 React、Vue、Solid、Svelte、Qwik、Angular、Lit 等适配器。
- ⚡ **高性能**：可选与 TanStack Virtual 集成，处理大量行或列时无需牺牲性能。
- 💬 **社区认可**：被 shadcn、React Aria 等知名项目采用，开发者称赞其轻量、可定制和强大。
- 🤝 **开源生态**：由维护者、贡献者和赞助商共同推动，支持企业级应用和社区创新。

---

### [Expo — 使用React构建原生应用](https://expo.dev/?utm_source=jsweekly&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=https://expo.dev/)

**原文标题**: [Expo — Build Native Apps with React](https://expo.dev/?utm_source=jsweekly&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=https://expo.dev/)

以下是您提供的文本摘要：

Expo 是一个全栈式 React Native 框架，提供强大的云服务，帮助开发者加速应用生命周期的每个阶段。

- 🚀 **全栈框架**：Expo 提供从开发到部署的一站式解决方案，包括 SDK、云服务和工具。
- 📱 **开发体验**：支持在手机上开发（Expo Go）、一键启动模拟器（Expo Orbit）和可视化优化包（Expo Atlas）。
- 🎨 **丰富库支持**：Expo SDK 包含 100+ 生产就绪库，如相机、推送通知、深度链接等，并支持 React、Kotlin、Swift 原生代码。
- 🌐 **多平台分发**：通过 Build 和 Hosting 将应用分发到 Android、iOS 和 Web，支持即时更新（Update）和自动化工作流（Workflows）。
- 🔍 **监控与洞察**：内置 Insights 监控用户平台分布、API 请求和错误率，帮助优化应用性能。
- 🤝 **社区与信任**：拥有 70,000+ Discord 成员、500,000+ 项目创建，80% 的 React Native 开发者选择 Expo，并被 Meta 推荐。
- 🏢 **企业级支持**：提供 SOC 2 Type 2 和 GDPR 合规服务，支持从独立开发者到企业团队，服务数亿终端用户。
- 💬 **用户好评**：开发者称赞 Expo 简化了开发流程、提升了性能，并推荐其优于纯 React Native 或其他框架（如 Xamarin 或 Flutter）。

---

### [window.showDirectoryPicker 开启了一个全新的世界](https://steveharrison.dev/showdirectorypicker-opens-up-a-whole-new-world/)

**原文标题**: [window.showDirectoryPicker opens up a whole new world](https://steveharrison.dev/showdirectorypicker-opens-up-a-whole-new-world/)

Chrome 的新 API `window.showDirectoryPicker()` 让网页应用能直接读写用户本地文件夹，开启本地优先应用的新可能。

- 📂 **本地优先应用**：用户可授权网站访问本地文件夹，如笔记应用直接操作 Markdown 文件，数据归用户所有而非云端存储。
- 🎨 **仿 Aperture 界面**：利用该 API 创建类似苹果 Aperture 或 Lightroom 的 UI，网页应用能管理本地照片，支持创建文件夹和移动文件。
- 🖼️ **照片视频编辑**：浏览器内实现强大的照片/视频编辑应用，直接处理本地源文件，已有 WebGPU 视频编辑器在探索此方向。
- 🧩 **节点合成应用**：基于苹果 Shake 灵感，创建节点式合成应用，可绘制多边形并叠加到源图像上。
- 🤖 **零手写代码**：以上所有功能均通过 AI（如 Claude）生成，无需手动编写代码，展示了技术发展的惊人之处。

---

### [如何打开目录 | 文件和目录模式 | web.dev](https://web.dev/patterns/files/open-a-directory)

**原文标题**: [How to open a directory  |  Files and directories patterns  |  web.dev](https://web.dev/patterns/files/open-a-directory)

本文介绍了在浏览器中打开目录的现代方法与传统方法，并提供了渐进增强的实现方案。

- 📂 **现代方法**：使用 File System Access API 的 `showDirectoryPicker()` 方法，支持读写模式，返回 `FileSystemDirectoryHandle`。
- 🖱️ **传统方法**：通过 `<input type="file" webkitdirectory>` 元素实现，兼容性更广但功能有限。
- 🔄 **渐进增强**：优先检测并使用现代 API，否则回退到传统方式，确保跨浏览器兼容。
- 🧩 **递归遍历**：提供 `getFiles()` 函数递归获取目录结构，为文件附加 `directoryHandle` 和 `handle` 属性。
- 🌐 **浏览器支持**：现代 API 支持 Chrome 86+、Edge 86+；传统方法支持 Safari 11.1+、Firefox 50+。
- 🛠️ **实用示例**：包含完整 HTML、CSS 和 JavaScript 代码，演示如何打开目录并列出文件。
- 📚 **进一步阅读**：提供 File System Access API 文档和演示链接，便于深入学习。

---

### [什么是git工作树，以及为什么应该使用它们？ - GitHub博客](https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/)

**原文标题**: [What are git worktrees, and why should I use them? - The GitHub Blog](https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/)

### 概述总结
Git worktrees 允许开发者在同一仓库的不同分支上并行工作，无需切换上下文或使用git stash，从而减少心智负担并提升效率。

- 🚀 **核心优势**：Worktrees 让你在不离开当前分支的情况下，创建独立的文件夹来并行处理不同任务，避免上下文切换和编辑器干扰。
- 🔄 **传统流程痛点**：使用分支和stash时，需频繁切换、重新加载文件，心智负担重，而worktrees简化了这一过程。
- 📁 **使用示例**：通过`git worktree add ../hotfix-workspace -b hotfix-bug main`快速创建新工作区，修复bug后删除文件夹即可。
- 🤖 **AI时代兴起**：随着AI和并行开发需求增加，worktrees成为GitHub Copilot等工具的默认模式，支持人机协作。
- ⚠️ **潜在问题**：每个worktree需独立依赖（如node_modules），可能导致磁盘空间膨胀；需手动管理文件夹，避免污染主仓库。
- 🛠️ **GitHub Copilot集成**：在Copilot应用中，新会话默认使用worktrees，自动管理路径和变更细节，开箱即用。
- 🤔 **适用性**：是否使用取决于个人偏好和并行工作需求，可结合分支和worktrees灵活选择。

---

### [TanStack Start：Next.js 开发者的心智模型 | Adarsha Acharya](https://www.adarsha.dev/blog/tanstack-mental-model-for-nextjs-developers)

**原文标题**: [TanStack Start: A Mental Model for Next.js Developers | Adarsha Acharya](https://www.adarsha.dev/blog/tanstack-mental-model-for-nextjs-developers)

概述：本文从Next.js开发者的视角，深入解析TanStack Start的核心架构与设计理念，包括路由器优先、显式服务器边界、类型安全路由、缓存策略、渲染模式及服务器函数等关键概念。

- 🧭 **路由器优先架构**：TanStack Start以路由器为核心，与Next.js的文件系统路由不同，更强调路由的灵活性和可组合性
- 🔒 **显式服务器边界**：通过明确的`server$`标记区分客户端与服务器代码，避免Next.js中隐式边界带来的混淆
- 🛣️ **类型安全路由**：内置类型推断确保路由参数、查询字符串和链接的完整性，减少运行时错误
- 💾 **智能缓存策略**：支持细粒度的缓存控制，包括SWR、预取和失效机制，性能优化更透明
- 🖥️ **灵活渲染模式**：提供SSR、SSG、ISR等多种渲染选项，开发者可按页面需求自由切换
- ⚙️ **服务器函数**：通过`createServerFn`定义服务端逻辑，无缝集成到客户端，简化数据获取与操作流程

---

### [FullCalendar - JavaScript事件日历](https://fullcalendar.io/)

**原文标题**: [FullCalendar - JavaScript Event Calendar](https://fullcalendar.io/)

这是一个最受欢迎的JavaScript日历库FullCalendar的概述，它支持多种框架和高度自定义。

- 📦 通过npm安装，支持Angular、React、Vue和原生JavaScript框架
- 🗓️ 提供月视图、周视图等多种日历视图，并可自定义工具栏
- ⚡ 高性能React组件，支持JSX嵌套内容渲染
- 🔧 拥有超过300项设置，功能强大且灵活
- 🪶 采用模块化插件设计，可减小项目包体积
- 📊 每月超过200万NPM下载量和7000万CDN下载量
- 🌟 拥有超过1.7万GitHub星标和120多位贡献者
- 💎 提供免费开源核心版本，以及付费高级插件和支持

---

### [发布 v7.0.0 · fullcalendar/fullcalendar · GitHub](https://github.com/fullcalendar/fullcalendar/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · fullcalendar/fullcalendar · GitHub](https://github.com/fullcalendar/fullcalendar/releases/tag/v7.0.0)

FullCalendar v7.0.0 正式发布，带来多项更新与修复。

- 🎉 主要版本 v7.0.0 终于发布，需使用 @7 后缀安装包
- 📋 完整更新日志与 v7 文档已提供
- 🎨 新增主题系统说明与体验区
- 🆕 支持 Angular 22（#8074）
- 🐛 修复资源时间线行高在事件移除后保持过时的问题（#8078）
- 🐛 修复 showNonCurrentDates 时，月首/月末事件在导航后消失的问题（#8077）
- 🐛 修复虚拟化下，手动添加资源后资源不可见的问题（#8072）
- ⚠️ 破坏性变更：需要 temporal-polyfill@^1.0.1 作为 peerDependency
- ⚠️ 破坏性变更：部分 CDN URL 路径调整（如 /all.global.js → /all/global.js）

---

### [FullCalendar 主题](https://themes.fullcalendar.io/)

**原文标题**: [FullCalendar Themes](https://themes.fullcalendar.io/)

概述：本文探讨了人工智能在医疗领域的应用，强调了其提升诊断效率、个性化治疗方案及优化医疗资源分配的潜力，同时指出了数据隐私、算法偏见和伦理监管等挑战。

- 🤖 人工智能通过分析医学影像和病历数据，可辅助医生更快速、准确地诊断疾病，如癌症筛查。
- 🧬 基于患者基因和病史的个性化治疗建议，能提高药物疗效并减少副作用，推动精准医疗发展。
- 📊 智能系统可优化医院排班、预测患者流量，从而更高效地分配医疗资源，降低运营成本。
- 🔒 医疗数据的高敏感性和隐私保护需求，成为AI应用的主要障碍，需加强加密和合规措施。
- ⚖️ 算法偏见可能导致诊断结果不公平，需通过多样化训练数据和伦理审查来避免歧视。
- 🏛️ 缺乏统一监管框架，使得AI医疗产品的安全性和可靠性面临挑战，亟需制定行业标准。

---

### [介绍 eve - Vercel](https://vercel.com/blog/introducing-eve)

**原文标题**: [Introducing eve - Vercel](https://vercel.com/blog/introducing-eve)

eve 是一个开源代理框架，用于构建、运行和扩展代理，它内置了生产环境所需的功能，让开发者只需定义代理的行为，而无需处理底层基础设施。

- 📁 **代理即目录**：代理通过文件系统定义，每个文件描述一个组件（模型、指令、工具、技能、子代理、渠道、计划），一目了然。
- ⚡ **快速创建**：只需定义 `agent.ts` 和 `instructions.md` 文件，即可在几分钟内创建一个代理，无需样板代码。
- 🔋 **开箱即用**：内置持久化执行、沙箱计算、人工审批、子代理、评估等功能，满足生产环境需求。
- 🔒 **安全连接**：通过文件连接 MCP 服务器或 API，代理无需暴露凭据，支持 OAuth、API 密钥等认证方式。
- 🌐 **多渠道支持**：同一代理可部署到 Slack、Discord、Teams 等多个渠道，只需一个适配器文件。
- 🛠️ **逐步扩展**：通过添加工具（TypeScript 文件）和技能（Markdown 文件）扩展代理能力，文件命名即定义。
- 👤 **人工审批**：可为特定工具操作设置审批要求，代理会暂停等待，不消耗计算资源。
- 💻 **自主编程**：代理拥有沙箱环境，可自主编写和运行代码，解决未覆盖的问题。
- 🤖 **子代理委托**：代理可委托子代理处理任务，子代理拥有独立的指令和工具。
- 🧪 **本地测试与评估**：通过 `eve dev` 命令启动本地开发服务器，提供终端 UI 查看代理运行步骤；支持编写评估测试，确保代理行为符合预期。
- 🚀 **一键部署**：代理作为普通 Vercel 项目部署，无需额外配置，部署不中断正在运行的任务。
- 📅 **定时任务**：通过计划文件定义 cron 表达式，让代理按时间自动执行任务。
- 🗂️ **版本控制**：代理作为文件目录，可纳入 Git 管理，支持代码审查、CI 集成和回滚。
- 🏢 **实际应用**：Vercel 内部运行超过 100 个代理，包括数据分析师、销售代表、客服、内容代理等，显著提升效率。
- 🎯 **开始使用**：运行 `npx eve@latest init my-agent` 即可在 1 分钟内创建第一个代理。

---

### [适用于任意规模的时间序列工作负载的Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Cloud 提供专为时间序列工作负载优化的 PostgreSQL 服务，具备企业级规模、高可用性和深度可观测性，新用户可获 $1000 额度免费试用。

- 📊 支持单服务处理 3 万亿指标/天、3 PB 数据及 1 万亿数据点，具备真实世界规模
- 💰 新用户免费试用 $1000 额度（30 天有效），无需信用卡，仅限新账户
- 🚀 读写分离复制集最多 10 节点，搭配分层 SSD/S3 实现无限低成本存储
- 💸 计算与存储分离，独立扩展，避免为闲置容量付费，优化成本与性能
- 🔒 多可用区集群自动故障转移、时间点恢复和跨区域备份，保障高可用
- 🛡️ 符合 SOC 2、HIPAA 和 GDPR 标准，支持始终加密、SSO、RBAC 和审计日志
- 🔍 查询钻取与仪表盘提供性能和错误可见性，可集成 CloudWatch、Datadog、Prometheus
- ⚡ 数分钟内完成数据库部署，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 与主流云提供商及 PostgreSQL 生态系统集成，支持企业级 SLA 和 24/7 专家支持

---

### [ForesightJS](https://foresightjs.com/)

**原文标题**: [ForesightJS](https://foresightjs.com/)

### 概述总结
ForesightJS 是一款通过预测用户意图实现智能预取内容的工具，支持桌面端和移动端多种策略，提供高效、可配置的预取方案。

- 🖱️ **鼠标轨迹预测**：分析光标移动模式，预判用户即将点击的链接并提前加载内容
- ⌨️ **键盘导航预取**：监测Tab键使用，在用户距注册元素N个Tab距离时触发预取
- 📜 **滚动方向预取**：根据滚动方向预测用户即将到达的元素并预取内容
- 📱 **触控设备支持**：提供“进入视口”或“触摸开始”两种策略，适配移动端和触控笔
- 🧪 **实时调试工具**：通过官方开发工具可视化预测触发过程，支持鼠标、滚动、Tab操作测试
- ⚡ **快速集成**：5分钟内完成配置，支持JavaScript、React、Vue，零复杂设置
- 🔧 **核心特性**：无轮询、无回流、事件驱动架构，内置TypeScript类型安全
- 📘 **完整文档**：提供详细配置指南和移动端支持说明

---

### [发布 ForesightJS v4.0 - 官方框架包 · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.0)

**原文标题**: [Release ForesightJS v4.0 - Official Framework Packages · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.0)

ForesightJS v4.0 发布，旨在简化与流行框架的集成，引入官方绑定包、不可变状态模型及性能优化。

- 📦 **官方框架包**：新增 `@foresightjs/react` 和 `@foresightjs/vue` 包，取代手动复制钩子/组合式函数，简化集成流程。
- 🔄 **不可变状态模型**：核心数据模型重构为 `ForesightElementState` 快照，支持订阅模式，可直接接入任何响应式系统。
- 🧹 **API 清理**：移除 `isTouchDevice`、`debug` 等废弃 API，新增 `updateElementOptions()` 和 `enabled` 选项，优化事件系统。
- 🚀 **性能提升**：预分配轨迹事件对象、优化轨迹计算，增加错误处理和 `isConnected` 守卫。
- 🛠️ **开发者工具 v2.0**：更新以支持 v4 状态模型，新增可视化开关选项，改进元素标签页（分组显示活动/非活动元素及原因）。
- 📚 **框架感知文档**：文档支持 React/Vue 切换，新增“其他框架”页面指导构建自定义绑定（Angular、Svelte、Solid 示例）。
- 🔄 **DOM 分离处理**：元素从 DOM 移除后不再注销，而是进入“停放”状态（`isParked: true`），重新连接后自动恢复。

---

### [发布 V4.2.0 - `<Foresight>` 组件 · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.2.0)

**原文标题**: [Release V4.2.0 - The `<Foresight>` Component · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.2.0)

概述总结
- 🚀 **V4.2.0 版本发布**：推出了全新的 `<Foresight>` 组件，简化了 React 和 Vue 包中的元素注册流程。
- 🛠️ **核心优化**：移除了重复的设置/注册/日志代码路径，并将数据属性镜像改为全局管理设置。
- ✨ **新增功能**：`dataAttributeMirroring` 全局设置，统一控制元素数据属性镜像（#133）。
- 🔄 **状态改进**：活跃/暂停元素计数改为从状态派生，消除了漂移错误（#134）。
- 🐛 **错误修复**：修复了触摸策略无变化时触发设置变更（#125）和桌面处理程序初始化时忽略 `positionHistorySize`（#124）的问题。
- ⚡ **性能提升**：仅活跃元素在连接时被观察，暂停元素直到重新激活才进入观察器（#126）。
- 🧹 **内部清理**：删除了重复代码路径（#129）和未使用的 `HasListenersFunction` 类型导出（#127）。
- 📦 **React 包更新**：`<Foresight>` 组件替代 `useForesights`，支持声明式注册动态元素列表（#131），并修复多 ref 处理（#135）。
- 📦 **Vue 包更新**：同样引入 `<Foresight>` 组件（#132），并修复多 ref 问题（#135）。
- 🔧 **开发工具更新**：v2.2.0 适配核心变更，数据属性显示遵循新的全局设置（#133）。

---

### [支持那个 · 2026年6月13日](https://nerdy.dev/prop-for-that)

**原文标题**: [Prop For That · June 13, 2026](https://nerdy.dev/prop-for-that)

概述总结  
Prop For That 是一个 JS 库，通过声明式属性为 CSS 提供实时动态信息（如输入值、指针位置、元素可见性等），无需手动编写 JS 代码，并与 CSS 样式查询无缝集成。

- 🎯 **核心动机**：解决 CSS 无法直接获取 JS 已知动态信息（如输入值、指针位置、滚动条大小等）的常见痛点，避免重复编写 JS 代码。
- 📦 **声明式使用**：通过 `data-props-for` 属性在 HTML 元素上声明所需属性，自动生成实时 CSS 自定义属性（如 `--live-value-pct`），支持导入自动加载。
- 🧩 **插件化架构**：所有功能按需加载，仅引入所需插件，减少冗余；同时提供命令式 API 作为备选。
- 📋 **支持属性列表**：包括指针坐标、视口尺寸、元素可见性、滚动条大小、输入值、表单状态、图像/视频颜色、时钟时间、FPS、网络状态、地理定位、设备方向等。
- 🔗 **与样式查询集成**：结合 CSS `@container style()` 实现条件样式，例如 `--live-all-valid: 1` 表示表单全部有效。
- 💬 **社区反馈**：开发者称赞其为 CSS 与 JS 之间的优雅桥梁，但部分用户反馈演示页面在 Firefox 上存在性能问题或 CPU 负载较高。

---

### [prop-for-that：CSS 响应，JS 仅监听](https://prop-for-that.netlify.app/)

**原文标题**: [prop-for-that: CSS reacts, JS just listens](https://prop-for-that.netlify.app/)

这是一个名为“prop-for-that”的CSS库，它允许你通过HTML属性将各种动态数据（如鼠标位置、滚动速度、表单状态等）直接暴露为CSS自定义属性（`--live-*`），从而在CSS中实现复杂的交互和响应式效果，而无需编写JavaScript。

- 🚀 **快速上手**：只需在项目中引入 `import 'prop-for-that/auto'`，然后在任意HTML元素上添加 `data-props-for` 属性并列出你想要的属性名（如 `data-props-for="size"`），即可在CSS中使用对应的 `--live-*` 变量。
- 🖱️ **追踪指针**：使用 `pointer-local` 属性，元素能获得 `--live-local-pointer-x-ratio` 和 `--live-local-pointer-y-ratio`，实现如卡片跟随鼠标倾斜的效果。
- 📜 **滚动触发**：通过 `visibility` 属性，元素可以感知是否进入视口（`--live-visible`）并锁定已进入状态（`--const-has-entered`），用于一次性动画或揭示效果。
- 🎚️ **范围控制**：`range` 属性将滑块或数字输入的值映射为 `--live-value` 和 `--live-value-pct`，并支持通过 `@container style()` 查询特定值来切换CSS规则。
- 📝 **表单字段**：`field` 属性实时提供文本长度（`--live-length`）、有效性（`--live-valid`）等，`field-state` 则追踪交互历史（如 `--live-dirty`、`--live-touched`）。
- 📐 **三角函数**：结合 `pointer-local` 和 CSS 的 `atan2()`、`cos()`、`sin()` 函数，可实现眼球跟随鼠标等纯CSS三角函数效果。
- ⏰ **时钟与计时**：`clock` 属性每秒更新 `--live-seconds`、`--live-minutes` 等，用于驱动CSS时钟动画。
- 🌐 **全局状态**：提供在线状态（`online`）、电池电量（`battery`）、帧率（`fps`）等全局属性，并在 `:root` 上写入。
- ⚡ **滚动动量**：`scroll-velocity` 提供带衰减的滚动速度（`--live-scroll-velocity`），可用于创建基于滚动速度的视差或形变动画。
- 📦 **元素尺寸**：`size` 属性通过 `ResizeObserver` 提供 `--live-w`、`--live-h` 和 `--live-aspect`，实现无媒体查询的宽高比检测。
- 🎬 **媒体播放**：`media` 属性提供视频/音频的 `--live-progress` 等属性，且可通过 `@property` 注册实现平滑动画。
- 🔋 **节能感知**：结合 `battery` 和 `@container style()`，可在低电量时自动禁用动画和重绘。
- 🖱️ **拖拽交互**：利用 `pointer-local` 和 `:active` 状态，实现纯CSS的拖拽效果，无需JavaScript计算。
- 📋 **表单聚合**：`form-state` 属性提供整个表单的验证计数（`--live-valid-count`）和完成度（`--live-completion`），用于驱动进度条或提交按钮状态。
- 🎨 **图像色彩**：`img-color` 从图片像素中提取主色、强调色等5种颜色，用于实现如跟随鼠标的彩色阴影效果。
- 🎥 **视频色彩**：`video-color` 类似地实时采样视频帧的 dominant 和 accent 颜色，用于营造动态背光效果。
- 📚 **完整参考**：文档末尾列出了所有可用的全局和元素级源，以及它们对应的 `--live-*` 属性。

---

### [影](https://kage.tamnd.com/)

**原文标题**: [kage](https://kage.tamnd.com/)

概述摘要  
- 📸 使用无头Chrome渲染每个页面，捕获最终DOM，移除所有脚本和事件处理器，并下载重写CSS、图片和字体，生成与实时网站外观相同但无代码运行的静态HTML文件夹。  
- 🔒 与浏览器“另存为”不同，kage（影）通过真实浏览器捕获页面，使其完全离线且不执行任何网络请求或脚本。  
- ⚡ 一键命令即可镜像网站并离线服务：`kage clone paulgraham.com` + `kage serve`。  
- 🧩 保留布局：样式表、图片、字体等被下载并重写为相对路径，确保离线副本与原版一致。  
- 🔗 链接重写：范围内链接指向其他已保存页面，支持在镜像中点击浏览。  
- 📦 支持打包为单个ZIM文件或自包含二进制文件，通过webview标签可打开独立窗口，模拟真实应用体验。  
- 📚 提供详细文档：入门指南、安装步骤、任务导向教程（如爬取范围、服务镜像、中断恢复）及完整CLI参考。

---

### [GitHub - tamnd/kage: 将任意网站离线化查看，去除JavaScript脚本](https://github.com/tamnd/kage)

**原文标题**: [GitHub - tamnd/kage: Shadow any website for offline viewing, with the JavaScript stripped out · GitHub](https://github.com/tamnd/kage)

kage 是一款能将任意网站克隆为离线可浏览镜像的工具，它通过真实浏览器渲染页面、剥离 JavaScript 并本地化资源，最终生成无脚本、无追踪的静态 HTML 文件。

- 📦 **核心功能**：使用 headless Chrome 渲染网页，抓取最终 DOM，剥离所有 JavaScript，并将 CSS、图片和字体下载到本地路径，生成可离线浏览的镜像文件夹。
- 🚀 **快速开始**：通过 `kage clone paulgraham.com` 克隆网站，再用 `kage serve` 在本地 HTTP 服务器预览，即可实现完整离线访问。
- 📁 **打包选项**：支持将镜像打包为 ZIM 档案（开放标准，兼容 Kiwix 生态）、自包含二进制文件（无需任何依赖）或双击运行的桌面应用（macOS .app、Linux AppImage、Windows GUI）。
- 🛠️ **高级特性**：支持广度优先爬取、遵守 robots.txt、增量刷新、子域名抓取、懒加载滚动、并发渲染，并提供丰富的命令行参数控制。
- 🖥️ **原生窗口**：通过 `webview` 标签编译后，打包的二进制文件可在操作系统原生窗口中打开网站，而非浏览器标签页。
- 🔄 **确定性打包**：相同镜像始终生成字节一致的输出文件，UUID 由内容派生，适合校验和缓存。
- 📚 **跨平台支持**：提供 Homebrew、Scoop、apt、dnf 等包管理器安装方式，以及 Docker 容器镜像（内置 Chromium）。
- 🧩 **开源许可**：采用 MIT 许可证，代码托管于 GitHub，已有 2.4k 星标和 77 个复刻。

---

### [GitHub - dop251/goja: 纯Go语言实现的ECMAScript/JavaScript引擎](https://github.com/dop251/goja)

**原文标题**: [GitHub - dop251/goja: ECMAScript/JavaScript engine in pure Go · GitHub](https://github.com/dop251/goja)

dop251/goja 是一个用纯 Go 语言实现的 ECMAScript 5.1(+) 引擎，注重标准合规性和性能，支持 ES5.1 完整功能及部分 ES6 特性。

- ⚡ 纯 Go 实现，无 cgo 依赖，跨平台易构建，性能优于 otto 等同类引擎
- ✅ 完整支持 ECMAScript 5.1（含正则和严格模式），通过大部分 tc39 测试
- 🛠️ 支持 ES6 部分功能（持续开发中），可运行 Babel 和 TypeScript 编译器
- 🔄 支持 Sourcemaps，便于调试
- ⚠️ WeakMap 因 Go 运行时限制，键可达时值无法被垃圾回收
- 🚫 不支持 WeakRef 和 FinalizationRegistry（受限于 Go 垃圾回收机制）
- 📅 Date 和 JSON 解析存在与标准库相关的细微差异
- 🔒 非 goroutine 安全，单实例只能由单个 goroutine 使用
- 🧩 提供 Go 与 JS 双向值传递、函数调用、异常处理、中断等功能
- 🏗️ 支持通过 FieldNameMapper 自定义结构体字段映射，以及原生构造函数
- 📦 有独立项目提供 Node.js 兼容性（含事件循环）

---

### [发布 v4.5.0 · juliangarnier/anime · GitHub](https://github.com/juliangarnier/anime/releases/tag/v4.5.0)

**原文标题**: [Release v4.5.0 · juliangarnier/anime · GitHub](https://github.com/juliangarnier/anime/releases/tag/v4.5.0)

概述摘要  
- 🎉 **新版本发布**：Anime.js v4.5.0 版本已发布，包含多项新功能和错误修复。  
- 🔌 **适配器扩展**：新增 `registerAdapter()` API，支持将 `animate()` 和 `utils.set()` 扩展到非 DOM 目标，并内置 Three.js 适配器。  
- 📐 **3D 网格支持**：Stagger 的自动网格模式现支持 3D 布局，使用 `{x, y, z}` 坐标或显式 `grid: [columns, rows, depth]` 三元组。  
- 🎲 **新增抖动与种子参数**：`jitter` 参数可添加随机偏移，`seed` 参数使随机结果可重现。  
- 🎨 **颜色动画改进**：颜色动画在伪线性空间中混合 RGB 通道，实现更平滑的过渡。  
- 🐛 **错误修复**：修复了反向循环闪烁、时间线回溯卡顿、关键帧精度问题、滚动容器崩溃等多个 Bug。  
- ⚡ **性能优化**：改进了大型时间线构建性能，以及引擎帧调度和速度更新的效率。

---

### [适配器 | 文档 | Anime.js | JavaScript动画引擎](https://animejs.com/documentation/adapters/)

**原文标题**: [Adapters | Documentation | Anime.js | JavaScript Animation Engine](https://animejs.com/documentation/adapters/)

以下是您提供的Anime.js文档内容的摘要概述和要点列表：

Anime.js是一个功能强大的JavaScript动画引擎，支持DOM元素、JavaScript对象、Three.js等多种目标，提供丰富的动画控制、时间线、可拖动交互和布局动画功能。

- 🚀 **安装与导入**：支持模块导入和直接使用，兼容Vanilla JS和React。
- 🎯 **动画目标**：可动画CSS选择器、DOM元素、JavaScript对象、数组、SVG属性等。
- ⏱️ **播放控制**：提供play、reverse、pause、restart、seek等方法，以及delay、duration、loop等设置。
- 🔄 **回调函数**：支持onBegin、onComplete、onUpdate、onLoop、onPause等回调。
- 📊 **时间线功能**：可添加动画、同步WAAPI动画、调用函数，并设置播放设置和回调。
- 🖱️ **可拖动交互**：支持x/y轴拖动、捕捉、映射，以及触发、容器、滚动等设置。
- 🎨 **布局动画**：支持CSS显示动画、交错布局、进入/退出动画、交换父级等。
- 📜 **滚动事件**：提供onScroll、onEnter、onLeave等回调，支持平滑滚动和缓动滚动。
- 🧩 **SVG与文本**：支持morphTo、createMotionPath、splitText、scrambleText等高级功能。
- 🔧 **工具函数**：包括stagger、$()、get、set、random、clamp、snap等实用工具。
- 🌐 **适配器系统**：内置Three.js适配器，支持自定义适配器以动画非标准对象。
- ⚙️ **引擎设置**：可配置timeUnit、speed、fps、precision等参数。

---

### [发布 v7.1.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.1.0)

**原文标题**: [Release v7.1.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.1.0)

### 概述总结
Ink v7.1.0 版本发布，主要新增 `suspendTerminal()` 功能，用于将终端控制权交给子进程。

- 🎉 **新增功能**：添加 `suspendTerminal()` 方法，允许将终端控制权临时移交给子进程（#972）
- 📦 **版本更新**：从 v7.0.6 升级至 v7.1.0，包含代码提交 9e8ed1f
- 🔧 **技术细节**：该功能通过合并请求 #972 实现，旨在优化终端与子进程的交互
- ⭐ **项目状态**：Ink 项目获得 39k 星标，1k 分支，持续活跃维护中
- 🚀 **发布信息**：由维护者 sindresorhus 于 6月17日 14:00 发布，包含两个资产文件

---

### [feat: 添加 suspendTerminal() 方法以将终端交给子进程 · 拉取请求 #972 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/pull/972)

**原文标题**: [feat: add suspendTerminal() to hand the terminal to a child process by costajohnt · Pull Request #972 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/pull/972)

Ink 新增 `suspendTerminal()` 功能，允许应用将终端临时交给子进程（如编辑器、分页器）并在完成后恢复自身状态。

- 🖥️ **新增 suspendTerminal() API**：通过 `useApp()` 获取，支持回调形式和 `await using` 一次性形式，方便临时交出终端控制权。
- 🔄 **终端状态完整切换**：暂停时关闭原始模式、显示光标、退出备用屏幕等，恢复时重新应用 Ink 的终端设置并强制重绘。
- 🛡️ **安全与错误处理**：回调抛出异常时仍能恢复终端，重复暂停会报错，非交互模式下不进行终端交接。
- 📚 **测试与文档完善**：包含单元测试、PTY 集成测试、可运行示例，并在 README 中详细说明 API 用法。

---

### [发布 v4.9.0 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases/tag/v4.9.0)

**原文标题**: [Release v4.9.0 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases/tag/v4.9.0)

Nuxt UI v4.9.0 版本发布，带来了多项新功能和改进。

- 📅 日历组件新增月份和年份选择模式，通过 `type` 属性切换，并支持快速导航。
- 🧭 新增 `useTour` 组合式函数，用于创建引导式教程，通过 Popover 组件分步展示。
- ✂️ 新增 `theme.unstyled` 选项，可在构建时移除默认主题类，便于自定义设计系统。
- 🎯 统一所有组件的焦点样式，使用柔和的轮廓光晕，提升可访问性和一致性。
- 🚀 其他功能：ChatMessages 暴露 `registerMessageRef`、组件支持 `icon` 设为 `false` 隐藏图标、Modal/Slideover 添加 `leave` 和 `enter` 事件等。
- 🐛 修复了 CommandPalette、Link、SelectMenu、Tabs 等多个组件的错误。
- 🌐 新增拉脱维亚语本地化支持。
- ❤️ 感谢 14 位贡献者的参与，包括 benjamincanac、maximepvrt 等。

---

### [发布 23.0.0 · nrwl/nx · GitHub](https://github.com/nrwl/nx/releases/tag/23.0.0)

**原文标题**: [Release 23.0.0 · nrwl/nx · GitHub](https://github.com/nrwl/nx/releases/tag/23.0.0)

Nx 23.0.0 版本发布，包含大量新功能、修复和破坏性变更。

- 🚀 **核心功能增强**：支持 `...` 作为目标配置合并的扩展标记，新增 `--mode` 和 `--multi-major-mode` 迁移标志，原生 Node.js TypeScript 剥离默认启用，新增 shell 标签补全功能，以及 `nx migrate` 的智能代理模式。
- ⚠️ **大量破坏性变更**：移除了 Angular 中已弃用的 `@nx/angular/module-federation` 入口点、`move` 生成器和 `ngrx` 生成器；移除了 Tailwind CSS 设置生成器、已弃用的样式表选项、旧的 webpack 插件重新导出、`initTasksRunner` API、`self`/`dependencies` 魔法字符串、SVGR 选项、Vitest 支持以及已弃用的 Jest 选项。同时弃用了多个执行器和辅助函数。
- 🩹 **广泛的错误修复**：修复了 Angular、打包、核心、Devkit、Gradle、JS、Linter、Maven、测试、Vite、Webpack 等多个模块的问题，包括多版本兼容性、Windows 路径支持、依赖图处理、缓存和性能优化。
- 🗑️ **弃用与移除**：弃用了 `@nx/detox` 构建/测试执行器、`@nx/cypress:cypress` 执行器、`withNx` 函数、`nxViteTsPaths` 和 `nxCopyAssetsPlugin` 辅助函数、webpack/rspack 配置组合辅助函数、SCAM 生成器、`convert-to-with-mf` 生成器、ESLint v8 支持以及 `addProjectConfiguration` 的 `standalone` 参数。
- ❤️ **感谢贡献者**：感谢包括 jaysoo、Stanzilla、FrozenPandaz、AgentEnder 在内的 20 多位贡献者。

---

### [GitHub - mourner/suncalc：一个用于计算太阳/月亮位置和相位的小型JavaScript库。](https://github.com/mourner/suncalc)

**原文标题**: [GitHub - mourner/suncalc: A tiny JavaScript library for calculating sun/moon positions and phases. · GitHub](https://github.com/mourner/suncalc)

SunCalc 是一个轻量、无依赖的 JavaScript 库，用于计算太阳和月球的位置、光照阶段及升落时间，精度高且与权威数据一致。

- 🌞 计算太阳位置（高度角、方位角）和光照阶段（日出、日落、黄昏等）
- 🌙 计算月球位置（高度角、方位角、距离）、月相（新月、满月等）和升落时间
- 📅 支持任意地点和时间，可自定义观测高度（如海拔）
- ⚙️ 提供 `addTime` 方法添加自定义太阳高度角事件
- 🎯 精度高：太阳位置误差约 0.08°，升落时间误差约 15 秒
- 📦 安装简单：通过 npm 或 CDN（jsDelivr）直接使用
- 📚 基于 Jean Meeus 的《天文算法》，验证自 JPL Horizons 和美国海军天文台

---

### [细致AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q2&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q2&utm_content=classified)

该平台通过自动化、穷举且确定性的测试方案，让开发者在无需编写或维护测试代码的情况下，快速交付可靠代码。其核心优势在于零人工干预、零误报（flakes）和极速反馈。

- 🚀 **零开发者投入**：自动录制开发环境中的用户交互，AI生成并持续更新测试用例，覆盖所有代码分支和边缘场景。
- 🔍 **穷举验证**：通过追踪每次交互执行的代码路径，确保测试套件全面覆盖用户流程和边界情况，且无需手动编写或修复测试。
- ⚡ **极速迭代**：测试在计算集群中高度并行化，1000个屏幕的测试可在120秒内完成，大幅提升代码发布速度。
- ❌ **彻底消除误报**：基于Chromium的确定性调度引擎，从底层设计杜绝测试不稳定（flakes），确保结果可靠。
- 🔄 **自动演进**：测试套件随应用变化自动更新——新功能或边缘场景出现时自动添加测试，过时测试自动移除，无需开发者干预。
- 🛡️ **无缝集成**：支持NextJS、React、Vue、Angular等主流框架，可通过脚本标签或SDK快速接入开发、预发布及生产环境。
- 🏢 **企业级信任**：已被Dropbox、Notion等超100家组织采用，工程师反馈“无需再调试合并后的代码，零维护且无误报”。
- 🔁 **灵活替代**：可补充或完全替代现有测试套件，且通过模拟后端响应实现无副作用测试，无需特殊测试账号或模拟数据。

---

### [clerk 部署：引导式、可恢复、支持代理](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=clerk-deploy&utm_content=06-23-26&dub_id=3pkgmRX9m3OHdObs)

**原文标题**: [clerk deploy: guided, resumable, agent-ready](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=clerk-deploy&utm_content=06-23-26&dub_id=3pkgmRX9m3OHdObs)

概述总结  
- 🚀 **clerk deploy 命令发布**：只需一条命令即可将应用从开发环境部署到生产环境，支持引导式操作。  
- 🛠️ **自动化流程**：创建生产实例、配置DNS记录（支持导出区域文件）、设置OAuth凭据（如Google和Apple），并验证DNS、SSL和邮件DNS。  
- 🤖 **代理模式支持**：在非TTY环境或使用`--mode agent`时，输出只读JSON状态，便于自动化工具集成。  
- 📋 **快速入门**：更新CLI、链接项目后运行`clerk deploy`，即可完成部署，详细文档可查阅所有命令和选项。

---

### [Handsontable - 适用于JavaScript、React、Angular和Vue的Handsontable数据网格](https://handsontable.com/evaluation?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=jsweekly)

**原文标题**: [Handsontable - Handsontable data grid for JavaScript, React, Angular, and Vue.](https://handsontable.com/evaluation?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=jsweekly)

Handsontable 提供45天免费试用，包含完整功能及专家支持，帮助用户评估产品是否适合生产环境。

- 🎯 试用期间获得完整功能访问权限，可使用真实数据进行测试
- 👨‍💻 提供技术支持团队直接帮助，解答任何问题或疑虑
- 📋 验证可访问性、兼容性和合规性要求
- 💼 客户经理协助审查许可和定价选项
- 🚀 支持多种框架：JavaScript、React、Vue、Angular
- 📚 提供丰富资源：文档、API参考、知识库、开发者论坛
- 🔒 通过ISO/IEC 27001:2023-08安全认证
- 🌐 支持社区：Twitter、LinkedIn、博客及GitHub问题反馈

---

### [揭秘福昕PDF结构提取引擎](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-structural-extraction-engine/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260623)

**原文标题**: [Inside Foxit's PDF Structural Extraction Engine](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-structural-extraction-engine/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260623)

概述：本文档详细介绍了通过Foxit PDF Services API将DOCX文件转换为PDF的完整流程，并提供了Python和cURL两种可运行的代码示例。

- 📄 **API调用流程**：涵盖从上传DOCX文件到获取PDF结果的完整步骤，包括身份验证、文件转换和结果下载。
- 🐍 **Python实现**：提供完整的Python代码示例，展示如何使用requests库调用API进行DOCX到PDF的转换。
- 🔧 **cURL命令**：给出对应的cURL命令示例，方便在命令行中直接测试和集成。
- 🔑 **身份验证**：说明如何获取并配置API密钥和密钥ID，确保请求安全。
- 📤 **文件上传**：演示如何通过API上传DOCX文件，并获取文件ID用于后续转换。
- 🔄 **转换任务**：展示如何提交转换任务，指定输出格式为PDF，并监控任务状态。
- 📥 **结果下载**：提供下载转换后PDF文件的代码，包括处理异步结果的方法。
- ⚙️ **错误处理**：包含常见的错误码和调试建议，帮助快速排查问题。

---

### [33字节的JS信号实现 · GitHub](https://gist.github.com/GulgDev/7b113b5e971682a6512d96c9c0fdf6da)

**原文标题**: [33-byte JS signal implementation · GitHub](https://gist.github.com/GulgDev/7b113b5e971682a6512d96c9c0fdf6da)

该内容展示了一个极简的JavaScript信号实现（33字节）及其使用示例。

- 📝 核心代码：仅33字节的`signal`函数，实现了信号的订阅与触发功能
- 🔄 订阅机制：通过调用`signal()`返回的函数，传入回调即可订阅信号
- ⚡ 触发与重置：直接调用信号函数会触发所有订阅者，且仅触发一次后自动重置
- 💬 社区反馈：用户评论中提供了改进版本，增加类型检查确保传入的是函数
- ⭐ 项目热度：该Gist获得17个星标，有2次修订记录

---

### [Reddit - 请等待验证](https://www.reddit.com/r/javascript/comments/1uc0scy/33byte_js_signal_implementation/ot4dm0o/)

**原文标题**: [Reddit - Please wait for verification](https://www.reddit.com/r/javascript/comments/1uc0scy/33byte_js_signal_implementation/ot4dm0o/)

本篇文章主要探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了其提升诊断效率、优化治疗方案及面临的挑战。

- 🩺 **诊断辅助**：AI通过分析医学影像（如X光、CT）可快速识别异常，辅助医生提高早期疾病（如癌症）的检测准确率。
- 📊 **数据整合**：AI系统能整合电子病历、基因数据等海量信息，为患者提供个性化治疗建议，减少试错成本。
- 🤖 **手术自动化**：机器人辅助手术系统通过高精度操作降低创伤，缩短患者恢复时间，但成本和技术门槛仍是推广障碍。
- ⚠️ **伦理与隐私**：AI依赖大量患者数据，存在数据泄露风险，且算法偏见可能影响诊断公平性，需加强监管。
- 🔮 **未来展望**：随着算法进步和算力提升，AI有望在远程医疗、药物研发等领域实现突破，但人机协作仍是核心模式。

---

### [为GitHub Actions checkout提供更安全的pull_request_target默认设置 - GitHub更新日志](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)

**原文标题**: [Safer pull_request_target defaults for GitHub Actions checkout - GitHub Changelog](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)

概述：GitHub Actions 的 `actions/checkout` v7 版本默认阻止了 `pull_request_target` 事件中最常见的“pwn request”攻击模式，提高了安全性，并计划于2026年7月16日向后移植到所有受支持的主要版本。

- 🛡️ **默认阻止不安全模式**：`actions/checkout` v7 在 `pull_request_target` 和 `workflow_run` 事件中，默认拒绝从 fork 拉取请求中检出代码，防止攻击者利用高权限执行恶意代码。
- 🗓️ **向后移植计划**：2026年7月16日，此安全策略将向后移植到所有当前支持的主要版本（如 v4），使用浮动标签（如 `@v4`）的工作流将自动更新。
- ✅ **不受影响的情况**：同一仓库的拉取请求、`pull_request` 事件以及固定到特定 SHA 或版本的工作流不受此更改影响。
- ⚠️ **未覆盖的风险**：此更改不阻止其他事件类型（如 `issue_comment`）或通过 `git` 命令手动拉取不可信代码的 pwn request 攻击。
- 🔓 **可选的退出机制**：对于需要高信任度检出 fork 代码的工作流（如生成覆盖率报告），可通过添加 `allow-unsafe-pr-checkout` 输入来退出保护，但需谨慎评估安全风险。

---

### [拉取请求限制如何减少噪音 - GitHub 博客](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/)

**原文标题**: [How pull request limits are cutting down the noise - The GitHub Blog](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/)

概述摘要  
GitHub 引入拉取请求限制功能，帮助维护者管理日益增长的贡献量，减少低质量噪音，并计划推出更多控制工具。

- 📈 拉取请求数量激增：从2023年1月的每月约2500万增至如今的9000万，增长约3.6倍，维护者难以跟上审核速度。
- 🚫 拉取请求限制机制：为无写入权限的用户设置最大同时打开的拉取请求数，超出需关闭或合并才能新建；AI代理发起的请求也计入限制。
- 🛡️ 信任名单与草稿豁免：可信贡献者可加入豁免名单，不受限制；草稿拉取请求不计数，便于管理。
- 💡 改变贡献者行为：限制促使贡献者更谨慎选择提交内容，减少低质量请求，提升审核体验。
- 🗑️ 即将推出归档功能：管理员可归档低质量或垃圾拉取请求，隐藏于主视图但保留访问权限，兼顾合规需求。
- 🔧 开发中的问题限制：将类似控制扩展到议题，设置用户可打开的议题上限，并可限制仅协作者创建议题。
- 🤖 智能豁免信号：未来计划基于合并历史、账户年龄等信号自动豁免，减少手动管理负担。
- 🌐 跨仓库控制探索：针对跨多个仓库提交拉取请求的用户，研究信任信号或速率限制等方案。
- 🙏 感谢维护者：功能源于社区反馈，鼓励用户尝试并反馈，以持续改进工具。

---

### [我把一个网站存进了网站图标](https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/)

**原文标题**: [I Stored a Website in a Favicon](https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/)

概述总结  
本文探讨了将网站内容存储在favicon图像像素中的实验，展示了数据隐藏的创意边界，并提供了技术实现细节。

- 🖼️ 每个favicon图像由像素组成，每个像素的RGB通道可存储3字节数据，因此favicon可作为数据存储介质  
- 🔧 实验将HTML内容（如标题和段落）转换为UTF-8字节，并添加4字节长度头，然后直接写入像素的RGB值  
- 📏 最终仅需9x9像素（81像素）即可存储208字节的HTML内容，容量利用率达87%  
- 🔄 浏览器通过Canvas API读取favicon像素，反向解析RGB值，重建字节数组，并解码为原始HTML  
- ⚠️ 关键限制：需要JavaScript引导程序来解码favicon，且favicon本身不包含完整网站，仅存储内容  
- 🤔 实用性低：存储量小、依赖JavaScript，但有多种替代方法（如SVG favicon、PNG注释块、ICO格式）  
- 🚀 实验意义：挑战数据存储的边界，证明favicon本质上是字节集合，可被重新利用

---

