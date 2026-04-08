### [JavaScript 周刊第 780 期：2026 年 4 月 7 日](https://javascriptweekly.com/issues/780)

**原文标题**: [JavaScript Weekly Issue 780: April 7, 2026](https://javascriptweekly.com/issues/780)

Google 开源了 JSIR，这是一个用于 JavaScript 的高级中间表示（IR）工具，旨在为新一代工具（如更智能的 linter 和打包器）奠定基础。本期还涵盖了 JavaScript 生态的最新动态，包括框架更新、性能基准发布、开源工具维护者的挑战，以及 CSS 在现代 Web 开发中日益增强的作用。

- 🛠️ Google 开源 JSIR，为 JavaScript 工具链的未来发展铺平道路
- 📅 Anthropic 提供免费的 Claude Code 工作坊，由 Lydia Hallie 主讲
- 📚 Chris Coyier 发布《2026 版 JavaScript 须知》，全面介绍当前生态
- 🔓 Axios 团队详细分析了 npm 供应链攻击事件
- ⚡ 主流浏览器推出 JetStream 3，更新 JavaScript 与 WASM 性能测试套件
- 🛡️ 文章探讨“最小发布年龄”作为软件供应链防御策略的价值
- 🎬 Tanner Linsley 展示 TanStack Start 框架，面向 React 和 Solid 开发者
- 😔 Lodash 创建者 John-David Dalton 谈及开源维护者的职业倦怠
- 🎨 现代 CSS 已能替代 JavaScript 实现工具提示、对话框等交互功能
- 🔍 Fuse.js 7.3 发布，增强轻量级模糊搜索功能
- 🚀 Babylon.js 9.0 推出，新增粒子编辑器和体积光照等 3D 渲染特性
- 📝 Marked.js 18.0 发布，专注于性能的 Markdown 解析器
- 💾 TinyBase v8.1 增加对 Svelte 5 的原生支持，用于本地优先应用
- 🎮 纯 CSS 渲染实现的《Doom》游戏展示 CSS 技术边界
- 📧 测试 25 种邮箱地址混淆技术在当前环境下的实际效果

---

### [[RFC] JSIR：面向 JavaScript 的高级中间表示 - MLIR - LLVM 讨论论坛](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

**原文标题**: [[RFC] JSIR: A High-Level IR for JavaScript - MLIR - LLVM Discussion Forums](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

JSIR 是一种基于 MLIR 的高层 JavaScript 中间表示，旨在填补 JavaScript 社区中缺乏公开、稳定的 IR 工具的空白。它通过保留 AST 的全部信息、支持控制流图与数据流分析，实现了从源代码到 AST 再到 JSIR 的高保真往返转换，适用于代码分析、反编译、去混淆等场景，已在 Google 投入生产使用。

- 🎯 **填补 IR 工具空白**：JavaScript 社区已有大量 AST 工具（如 Babel、ESLint），但缺乏公开的 IR 工具，JSIR 旨在解决这一问题。
- 🔄 **高保真往返转换**：JSIR 设计支持无损的源代码 ↔ AST ↔ JSIR 转换，保留所有源级信息，便于源码到源码的转换。
- 🏗️ **基于 MLIR 构建**：利用 MLIR 区域表示控制流结构，提供数据流分析框架，并简化了 API 使用体验。
- 🛠️ **实际应用场景**：在 Google 用于 JavaScript 代码分析、Hermes 字节码反编译、代码去混淆等生产级任务。
- 🌐 **开源与社区贡献**：项目已在 GitHub 开源，并计划探索上游至 MLIR、改进数据流分析等方向，欢迎社区参与。

---

### [GitHub - google/jsir：下一代JavaScript分析工具集 · GitHub](https://github.com/google/jsir)

**原文标题**: [GitHub - google/jsir: Next-generation JavaScript analysis tooling · GitHub](https://github.com/google/jsir)

JSIR 是谷歌开发的新一代 JavaScript 分析工具，其核心基于 MLIR 的高层中间表示，支持数据流分析和无损转换回源代码，适用于源码到源码的转换场景。

- 🛠️ **核心功能**：基于 MLIR 的中间表示，支持数据流分析和无损源码转换，适用于反编译和反混淆等场景。
- 🔍 **应用案例**：在谷歌内部用于 Hermes 字节码反编译为 JavaScript 代码，以及结合 Gemini LLM 进行 JavaScript 反混淆。
- ⚖️ **设计特点**：平衡高层 AST 转换和低层数据流分析需求，利用 MLIR 区域精确建模控制流结构。
- 🐳 **快速开始**：推荐使用 Docker 镜像快速体验，支持通过 Bazel 构建系统进行本地编译和测试。
- 📚 **资源链接**：提供技术演讲视频、学术论文和相关文档，深入介绍工具设计原理和实际应用。

---

### [中间表示 - 维基百科](https://en.wikipedia.org/wiki/Intermediate_representation)

**原文标题**: [Intermediate representation - Wikipedia](https://en.wikipedia.org/wiki/Intermediate_representation)

中间表示（IR）是编译器或虚拟机内部用于表示源代码的数据结构或代码，旨在便于优化和翻译等进一步处理。它必须准确且独立于特定源语言或目标语言，形式包括内存数据结构或可读的中间语言。IR 允许编译器系统（如 GCC 和 LLVM）支持多种源语言和目标架构，提高代码生成效率和可移植性。

- 🏗️ IR 是编译器或虚拟机内部表示源代码的数据结构或代码，用于优化和翻译
- 🌐 良好的 IR 需准确且独立于特定语言，形式可为数据结构或中间语言
- 🔄 使用 IR 使编译器（如 GCC、LLVM）能支持多源语言和目标架构，提升可移植性
- 💻 中间语言（如 C、Java 字节码、LLVM IR）常用于跨平台编译和虚拟机执行
- 🛠️ IR 在静态分析、链接时优化和异构计算（如 MLIR）中发挥关键作用

---

### [Anthropic Lydia Hallie 深度解析 Claude 代码 | AddEvent](https://www.addevent.com/event/8n58y7bjwqmr)

**原文标题**: [Claude Code Deep Dive with Lydia Hallie from Anthropic | AddEvent](https://www.addevent.com/event/8n58y7bjwqmr)

这是一场由 Frontend Masters 举办的免费高级工作坊，主题是深入探索 Anthropic 公司的 Claude Code，由 Lydia Hallie 主讲。工作坊旨在帮助开发者超越 Claude Code 的默认设置，深入理解从提示到响应的内部机制，并通过实践配置一个演示项目。

- 🧠 **深入理解机制**：学习在用户提示与 Claude 响应之间发生的内部过程。
- 🛠️ **实践项目配置**：全天通过逐层配置演示项目来深入学习，涵盖 CLAUDE.md 文件、权限设置、技能配置等。
- 🔧 **构建自定义 MCP 服务器**：从零开始构建一个自定义的模型控制协议（MCP）服务器。
- 🎫 **免费参与**：这是一个独家免费工作坊，参与者需要通过提供的链接进行 RSVP 注册。
- 📅 **活动时间**：2026 年 4 月 21 日，美国芝加哥时间上午 9:30 至下午 4:30（对应日本东京时间为 4 月 21 日 23:30 至 4 月 22 日 06:30）。
- 🌐 **在线参与**：通过 Frontend Masters 平台在线进行，注册链接已提供。

---

### [JavaScript 必知要点（2026 年版）—— Frontend Masters 博客](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/)

**原文标题**: [What To Know in JavaScript (2026 Edition) – Frontend Masters Blog](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/)

本文概述了 JavaScript 在 2026 年的关键发展，涵盖语言新特性、框架、运行时、构建工具及生态系统趋势。

- 🆕 ECMAScript 2025 新增迭代器助手、集合方法、正则表达式转义、Promise.try() 和导入属性等功能，提升开发效率与性能。
- 📅 ECMAScript 2026 预计引入 Temporal API（改进日期处理）、显式资源管理、Array.fromAsync 和错误检查方法等重大更新。
- ⚛️ React 19 推出服务器组件、React 编译器和服务器操作，React Native 迈向 1.0 版本，但需关注相关安全漏洞。
- 🖥️ Vue 3.6 测试 Vapor 模式以提升性能，Nuxt 4.0 发布，生态工具链 Vite+ 持续扩展。
- 🚀 Svelte 5 采用 Runes API 实现细粒度响应式，性能显著优化，深受开发者喜爱。
- 🏃 JavaScript 运行时 Node.js 原生支持 TypeScript，Bun 1.3 强化开发体验，Deno 2 注重安全性与稳定性。
- 🔧 构建工具 Vite 8 改用自研 Rolldown，Turbopack 成为 Next.js 默认打包工具，webpack 计划简化配置。
- 📘 TypeScript v6 为 v7 铺路，将换用 Go 编译器提速，AI 辅助编码日益普及，测试工具 Vitest 和 Playwright 崛起。
- 🌐 元框架 Next.js 16 默认集成 Turbopack，Remix 转向独立组件模型，Astro 6.0 获 Cloudflare 收购并持续增强。
- ⚠️ npm 面临供应链安全威胁，建议采用 Socket 等工具防护，同时学习基础技能以应对技术变迁。

---

### [事后分析：axios npm 供应链安全事件 · 第 10636 号议题 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636)

**原文标题**: [Post Mortem: axios npm supply chain compromise · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636)

2026 年 3 月 31 日，axios 的两个恶意版本（1.14.1 和 0.30.4）通过被入侵的维护者账户发布到 npm 仓库，其中注入了包含远程访问木马的依赖包，恶意版本在约 3 小时后被移除。受影响用户需立即检查并采取补救措施，项目团队已启动全面安全加固。

- 🔐 **账户入侵**：攻击者通过社会工程和 RAT 恶意软件入侵了 axios 主要维护者的个人电脑，获取了 npm 账户凭据。
- 📦 **恶意发布**：攻击者发布了 axios 的 1.14.1 和 0.30.4 版本，并注入了包含远程访问木马的`plain-crypto-js@4.2.1`依赖包。
- ⏱️ **影响时长**：恶意版本在 npm 上存活了约 3 小时（从 3 月 31 日 00:21 UTC 到 03:15 UTC）。
- 🛡️ **补救措施**：受影响用户需降级 axios、删除恶意依赖、轮换所有密钥凭证，并检查网络连接记录。
- 🔄 **安全改进**：项目团队将重置所有设备凭证、采用不可变发布设置、实施 OIDC 发布流程，并全面加强安全防护。
- 🕵️ **攻击时间线**：攻击始于约两周前的社会工程活动，恶意依赖包和 axios 版本在 3 月 30 日至 31 日间陆续发布。
- 👥 **社区响应**：社区成员及时报告问题，合作者迅速联系 npm 下架恶意包，安全团队提供了详细的技术分析和修复指南。
- 📚 **经验教训**：强调了维护者个人账户安全的重要性、需要自动化检测机制，以及开源维护者面临的社会工程攻击风险。

---

### [事后分析：axios npm 供应链安全事件 · 第 10636 号议题 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636#issuecomment-4180237789)

**原文标题**: [Post Mortem: axios npm supply chain compromise · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636#issuecomment-4180237789)

2026 年 3 月 31 日，axios 的两个恶意版本（1.14.1 和 0.30.4）通过被入侵的维护者账户发布到 npm，其中注入了远程访问木马，影响持续约 3 小时后被移除。受影响用户需立即降级、清理依赖并轮换所有凭证。

- 🚨 **事件概述**：axios 维护者账户遭社工攻击，导致恶意版本被发布，内含远程木马依赖`plain-crypto-js`。
- ⏰ **影响时长**：恶意版本在 npm 上存活约 3 小时（UTC 时间 00:21 至 03:15）。
- 🖥️ **受影响系统**：macOS、Windows 和 Linux 系统均可能被感染。
- 🔍 **检测方法**：检查项目锁文件中是否包含`axios@1.14.1`、`axios@0.30.4`或`plain-crypto-js`依赖。
- 🛡️ **应对措施**：降级至安全版本、删除恶意依赖、轮换所有密钥凭证，并检查网络连接记录。
- 🛠️ **安全改进**：将重置设备凭证、采用 OIDC 发布流程、建立不可变发布机制，并加强整体安全防护。
- 📚 **经验教训**：需避免从个人账户直接发布、建立自动检测机制，并提高维护者对社工攻击的警惕性。
- 🤝 **致谢**：感谢社区成员和 npm 安全团队的快速响应，恶意版本已全部移除。

---

### [JetStream 3 基准测试套件介绍 | WebKit](https://webkit.org/blog/17899/introducing-the-jetstream-3-benchmark-suite/)

**原文标题**: [  Introducing the JetStream 3 Benchmark Suite | WebKit](https://webkit.org/blog/17899/introducing-the-jetstream-3-benchmark-suite/)

JetStream 3 是跨浏览器基准测试套件的重要更新，由 WebKit、Google 和 Mozilla 合作开发，旨在更全面地衡量现代 Web 应用性能，特别是 WebAssembly 和 JavaScript 的执行效率。它摒弃了过时的微基准测试，采用更大规模的工作负载，并优化了评分方法，以反映真实场景下的性能表现。

- 🚀 **WebAssembly 评分方法革新**：JetStream 3 取消了独立的启动/运行时评分，改为与 JavaScript 相同的多迭代评分，涵盖首次迭代、最差情况迭代和平均情况迭代，确保优化覆盖完整生命周期。
- 🧩 **摆脱微基准测试陷阱**：通过增加代码规模和复杂性，减少对单一热函数的依赖，促使引擎在 JIT 编译器和标准库功能上进行全面优化。
- 🛠️ **WebAssembly GC 性能优化**：通过内联分配、改进内存布局和消除析构函数，将 WasmGC 子测试性能提升约 40%，减少垃圾回收开销。
- 🔍 **GC 类型检查加速**：采用 Cohen 类型显示算法内联类型检查，并将显示条目嵌入类型信息中，大幅提升类型检查效率，减少运行时开销。
- 📞 **间接调用内联改进**：通过基线编译器 BBQ 收集间接调用站点的目标函数数据，优化编译器 OMG 根据这些数据生成守卫和直接调用路径，提升虚拟方法调度性能。
- 🧠 **非局部内联决策系统**：引入基于调用站点优先级的内联算法，综合考虑执行频率、被调用方大小和优化潜力，更有效地利用代码大小预算。
- 🏗️ **抽象堆概念引入**：在 Wasm 编译管道中引入抽象堆，支持基于类型的别名分析，消除冗余的加载和存储操作，提升内联后的代码优化效果。
- ⚡ **寄存器分配器升级**：采用贪婪寄存器分配算法替代原有的图着色和线性扫描算法，提升编译速度和代码质量，支持更大函数的优化编译。
- 🌐 **IPInt 支持 SIMD 指令**：在 JavaScriptCore 的解释器层 IPInt 中实现完整的 SIMD 支持，使 SIMD 代码能够近乎即时启动，无需预先编译。
- 🔢 **BigInt 运算优化**：通过实现 Comba 乘法算法、DIV2BY1 除法技术和改进内存布局，显著提升 BigInt 算术运算性能。
- ⏳ **微任务队列和异步函数改进**：将微任务队列移至 JavaScriptCore 内部，重写 Promise 实现为 C++，并优化 async 函数的恢复机制，减少异步代码的开销。
- 📈 **性能提升成果**：这些架构改进使 Safari 26.4 相比 26.0 在 JetStream 3 上性能提升约 10%，用户将体验到更快的页面加载和更流畅的交互。

---

### [介绍 EmDash——WordPress 的精神继承者，解决插件安全难题](https://blog.cloudflare.com/emdash-wordpress/)

**原文标题**: [Introducing EmDash â the spiritual successor to WordPress that solves plugin security](https://blog.cloudflare.com/emdash-wordpress/)

EmDash 是 WordPress 的精神继承者，旨在解决其插件安全等核心问题，采用现代技术栈构建，支持无服务器部署和 AI 原生管理，为内容发布提供更安全、灵活的开源解决方案。

- 🛡️ **解决插件安全问题**：通过沙盒隔离和权限声明，确保插件仅能执行明确声明的操作，从根本上消除安全漏洞。
- 🔓 **打破市场锁定**：插件可自由选择许可证，且代码在安全环境中独立运行，减少对集中式市场的依赖。
- 💰 **内置支付支持**：集成 x402 标准，允许内容创作者按使用收费，无需订阅或额外开发。
- ⚡ **无服务器架构**：基于 Cloudflare Workers 构建，实现零成本扩展，仅按实际计算时间计费。
- 🎨 **现代前端主题**：采用 Astro 框架，使主题开发更安全、高效，且无需直接操作数据库。
- 🤖 **AI 原生管理**：提供 CLI、MCP 服务器和 Agent Skills，支持 AI 代理自动化管理内容与插件。
- 🔑 **密码认证**：默认使用 Passkey 认证，无密码泄露风险，并支持可插拔的 SSO 集成。
- 📥 **WordPress 迁移**：支持从 WordPress 导入内容和媒体，并可自定义内容类型与字段。
- 🚀 **开源与可扩展**：基于 MIT 许可证开源，鼓励开发者参与贡献，兼容 WordPress 功能但代码独立。

---

### [Svelte 四月 2026 更新亮点](https://svelte.dev/blog/whats-new-in-svelte-april-2026)

**原文标题**: [What’s new in Svelte: April 2026](https://svelte.dev/blog/whats-new-in-svelte-april-2026)

Svelte 在 2026 年 4 月发布了多项更新，包括文档新增最佳实践指南，以及代码层面的改进：OpenCode 包中的 Svelte MCP 配置更便捷，svelte.config.js 支持函数设置选项，服务器端错误边界可用，类型系统增强。社区展示了多个基于 Svelte 构建的应用和工具。

- 📚 新增最佳实践指南，完善 Svelte 文档
- ⚙️ OpenCode 包中 Svelte MCP 配置更简化，集中存放于 .opencode/ 文件夹
- 🔧 svelte.config.js 支持函数设置 css、runes 等选项，实现单一配置源
- 📦 svelte/motion 导出 TweenOptions 等类型，提升 spring 和 tweened 的类型安全
- 🛡️ SvelteKit 支持服务器端错误边界，增强错误处理能力
- 🧩 页面和布局参数类型细化，提升 $app/types 等模块的类型安全性
- 🌐 社区展示多个应用和工具，如 Ghostty 配置生成器、Orbit PDF 工具包等
- 🎧 发布多期 Svelte 相关播客和社区会议，分享最新动态
- 🛠️ 新增多个库和组件，如 svelte-realtime、Motion GPU 等，丰富开发生态

---

### [ESLint v10.2.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/04/eslint-v10.2.0-released/)

**原文标题**: [ESLint v10.2.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/04/eslint-v10.2.0-released/)

ESLint v10.2.0 作为次要版本发布，引入了语言感知规则支持和 Temporal 全局对象识别，同时修复了若干错误并更新了文档。

- 🆕 新增 `meta.languages` 属性，允许规则作者声明支持的编程语言，若规则用于不支持的语言，ESLint 将抛出运行时错误。
- 🌐 识别 Temporal 提案为内置全局对象，`no-undef` 规则默认不再标记其使用，而 `no-obj-calls` 规则会报告对 Temporal 的直接调用错误。
- 🐛 修复了若干错误，包括更新了首方依赖项。
- 📚 更新了配置文档，新增了语言配置选项，并调整了多个文档部分。
- 🔧 进行了多项内部改进，包括重构代码、更新依赖项和增加单元测试。

---

### [Node.js — Node.js 25.9.0（当前版本）](https://nodejs.org/en/blog/release/v25.9.0)

**原文标题**: [Node.js — Node.js 25.9.0 (Current)](https://nodejs.org/en/blog/release/v25.9.0)

Node.js 25.9.0 版本发布，包含测试运行器模块模拟改进、新增多个功能如 AsyncLocalStorage 的 using 作用域、CLI 的 --max-heap-size 选项、新的 Web Cryptography 算法 TurboSHAKE 和 KangarooTwelve，以及 REPL 的自定义错误处理等，同时修复了多项错误并更新了依赖项。

- 🧪 测试运行器模块模拟选项 `MockModuleOptions.defaultExport` 和 `MockModuleOptions.namedExports` 合并为 `MockModuleOptions.exports`，提供自动化迁移工具
- 🔗 `async_hooks` 模块为 `AsyncLocalStorage` 新增 using 作用域支持
- 🧠 CLI 新增 `--max-heap-size` 选项以设置最大堆大小
- 🔐 `crypto` 模块添加 Web Cryptography 算法 TurboSHAKE 和 KangarooTwelve
- 🛠️ REPL 新增自定义错误处理功能，并移除了对 `node:domain` 的依赖
- 🚀 SEA（Single Executable Applications）支持 ESM 入口点的代码缓存
- 📦 `stream` 模块新增 `stream/iter` 实现
- 🐛 修复了包括 `fs.cpSync` 处理非 ASCII 字符、`zlib` 模块在写入时调用 `reset()` 导致的 use-after-free 问题等多个错误
- 📚 文档更新，包括弃用 `module.register()` 和澄清 `CryptoKey` 在 `node:crypto` 中的使用
- 🔄 更新了多个依赖项，如 Ada、timezone、Googletest、SIMDjson、NGTCP2、V8 和 npm

---

### [可迭代流 | Node.js v25.9.0 文档](https://nodejs.org/docs/latest/api/stream_iter.html#iterable-streams)

**原文标题**: [Iterable Streams | Node.js v25.9.0 Documentation](https://nodejs.org/docs/latest/api/stream_iter.html#iterable-streams)

Node.js v25.9.0 引入了实验性的 `node:stream/iter` 模块，这是一个基于可迭代协议（而非传统事件驱动或 Web Streams API）构建的新流处理 API。它通过批处理 `Uint8Array[]` 来优化性能，支持拉取和推送两种数据流模型，并提供多种背压策略（严格、阻塞、丢弃最旧、丢弃最新）来管理内存。该模块包含丰富的工具函数，用于创建、转换、消费流，并支持多消费者场景（如广播和共享），同时允许第三方对象通过特定协议符号集成到流生态中。目前，该功能需要通过 `--experimental-stream-iter` CLI 标志启用。

- 🧪 **实验性功能**：`node:stream/iter` 模块目前处于实验阶段，需通过 `--experimental-stream-iter` 标志启用。
- 🔄 **基于可迭代协议**：流被表示为 `AsyncIterable<Uint8Array[]>` 或 `Iterable<Uint8Array[]>`，无需继承特定基类，任何实现可迭代协议的对象均可参与。
- 📦 **批处理优化**：数据以 `Uint8Array[]` 批次流动，分摊异步操作开销，提升性能。
- ⚙️ **灵活的转换器**：支持无状态函数或有状态对象（含 `transform` 方法）作为转换器，可处理压缩、加密等需跨批次缓冲的操作。
- ⏳ **双模型支持**：提供**拉取模型**（`pull`，按需消费）和**推送模型**（`push`，显式写入），后者需处理背压。
- 🚦 **多种背压策略**：包括 `'strict'`（默认，严格限制缓冲）、`'block'`（类传统流）、`'drop-oldest'`（保留最新）和 `'drop-newest'`（丢弃最新），以应对不同内存与实时性需求。
- 🔧 **丰富的工具集**：包含 `from`、`pipeTo`、`text`、`bytes` 等函数，用于流创建、管道连接和数据消费，同时支持同步版本（如 `fromSync`、`textSync`）。
- 👥 **多消费者支持**：通过 `broadcast`（推送式广播）和 `share`（拉取式共享）支持多个消费者独立消费同一数据源。
- 🔗 **协议集成**：提供 `Stream.toAsyncStreamable` 等协议符号，允许自定义对象无缝集成到流处理管道中。
- 📄 **统一字节表示**：所有数据均以 `Uint8Array` 字节形式处理，字符串会自动进行 UTF-8 编码，确保编码明确且支持零拷贝传输。

---

### [最低发布年龄：被低估的供应链防御策略 | 丹尼·阿卡什](https://daniakash.com/posts/simplest-supply-chain-defense/)

**原文标题**: [Minimum Release Age is an Underrated Supply Chain Defense | Dani Akash](https://daniakash.com/posts/simplest-supply-chain-defense/)

设置最低发布年龄是一种被低估的供应链防御策略，它通过延迟安装新发布的软件包版本，利用社区发现和清除恶意代码的时间窗口来阻止短期恶意攻击。

- 🛡️ **防御原理**：通过设置包管理器在安装时拒绝发布不足指定天数（如 7 天）的版本，可自动过滤掉大多数短期存在的恶意软件包，因为这些攻击通常在几小时到几天内就会被发现并下架。
- 📊 **实际效果**：分析过去 8 年 21 起供应链攻击事件显示，7 天延迟策略能成功阻止其中 11 起短期恶意发布攻击，并缩短另外 2 起的暴露窗口，但对长期渗透、维护者破坏或构建系统入侵等攻击无效。
- ⚙️ **配置方式**：主流 JavaScript 包管理器（如 Bun、npm、pnpm、Yarn 4）及 Python 的 uv/pip 已支持该功能，但配置参数和单位不统一（秒、分钟、天、时长字符串），增加了跨工具配置复杂度。
- 🚫 **适用限制**：策略主要适用于使用语义化版本范围并定期更新依赖的项目，对完全锁定版本或内部私有包场景作用有限，且不能替代锁定文件、行为分析工具等安全措施。
- 🌍 **生态覆盖**：JavaScript 和 Python 生态已较好支持，但 Go、Java、PHP、Ruby 等主流语言的包管理器尚未内置此功能，使其供应链暴露于常见攻击模式之下。
- ⏳ **推广意义**：该策略作为纵深防御的一层，实施简单且效果显著，建议包管理器将其设为默认选项（如 npm 提议默认 7 天），并为紧急更新保留绕过机制。

---

### [TanStack Start：一个以客户端为先的 Web 框架 - Tanner Linsley - YouTube](https://www.youtube.com/watch?v=8XGcc-FRPuo)

**原文标题**: [TanStack Start: A Client First Web Framework - Tanner Linsley - YouTube](https://www.youtube.com/watch?v=8XGcc-FRPuo)

该内容为 YouTube 网站底部的通用导航链接列表，并非一篇文章或实质性内容。

- 🏠 网站功能概览与政策链接
- 📄 用户服务条款与隐私政策说明
- 🔗 创作者、广告商和开发者专项入口
- ℹ️ 平台运作机制与新功能测试通道
- ©️ 版权归属与年份标识

---

### [TanStack 启动](https://tanstack.com/start/latest)

**原文标题**: [TanStack Start](https://tanstack.com/start/latest)

TanStack Start 是一个基于 TanStack Router 构建的全栈框架，专为 React 和 Solid 设计，提供类型安全、高性能的现代 Web 应用开发体验。

- 🚀 **企业级路由** – 基于 TanStack Router 构建，提供完全类型安全且功能强大的路由系统，轻松处理复杂的全栈路由需求。
- 🌊 **SSR、流式传输与服务器 RPC** – 支持全文档 SSR、流式传输、服务器函数和 RPC，无需在服务器端渲染和客户端交互性之间妥协。
- 💻 **客户端优先，100% 服务器兼容** – 坚持客户端优先的开发者体验，同时提供功能齐全的服务器端能力，确保用户体验不打折扣。
- 🌍 **随处部署** – 可在任何能运行 JavaScript 的环境部署，无论是传统服务器、无服务器平台还是 CDN，都能轻松构建、打包和部署。
- ❤️ **开发者好评** – 社区反馈积极，被认为在类型安全、代码可读性和全栈开发体验上表现出色，甚至能替代 TRPC/GraphQL/REST 的需求。
- 🛠️ **现已可用** – TanStack Start RC 版本已发布，功能完备，正为 1.0 版本做准备，鼓励开发者试用并提供反馈。

---

### [TimescaleDB — 顶尖时序数据库 | 泰格数据](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

TimescaleDB 是一款基于 Postgres 构建的开源时序数据库，专为处理传感器、链上及客户数据设计，提供实时分析、高效压缩和自动管理功能，适用于初创公司和企业。

- 🚀 高性能时序处理：通过自动分区（Hypertables）和行列混合存储，实现快速数据写入与查询，支持毫秒级分析数十亿行数据
- 📊 智能数据管理：提供高达 95% 的压缩率，自动转换行列存储，并支持增量物化视图，保持历史数据在线且查询高效
- 🔧 全面 PostgreSQL 兼容：作为 100% 兼容 Postgres 的时序数据库，提供约 200 个原生 SQL 函数（Hyperfunctions），简化复杂时序分析
- 🌐 活跃开发者生态：拥有 22K+ GitHub 星标和 12,000+ Slack 社区成员，支持开源贡献与专业交流
- ☁️ 灵活部署选项：提供云端免费试用和企业级解决方案，支持 Helm 快速部署，满足从开发到生产的不同需求
- 💼 多行业验证：已成功应用于 Cloudflare、Replicated、orca.so 等企业的加密货币、能源遥测、油气运营等场景

---

### [开源维护者的倦怠真实存在：与 Lodash 创始人 John-David Dalton 的对话 | OpenJS 基金会](https://openjsf.org/blog/burnout-is-real-for-open-source-maintainers)

**原文标题**: [Burnout Is Real for Open Source Maintainers: A Conversation with John-David Dalton, Creator of Lodash | OpenJS Foundation](https://openjsf.org/blog/burnout-is-real-for-open-source-maintainers)

Lodash 创始人 John-David Dalton 回顾了项目的成长历程、维护全球使用软件的压力，以及个人从倦怠中退后并重建可持续道路的经历，强调了开源维护者面临的挑战与可持续发展的重要性。

- 🛠️ Lodash 作为 JavaScript 生态中广泛使用的工具库，每日下载量超过 1 亿次，最初由单一维护者发起，逐渐演变为关键基础设施。
- 😔 维护者 Dalton 在经历母亲去世和离婚等个人重大变故后，优先事项改变，导致项目维护放缓，体现了开源工作与个人生活的平衡挑战。
- 🔄 经历约五年的恢复期，Dalton 通过治疗、锻炼和培养编程外的爱好重建可持续工作模式，强调长期可持续性比持续输出更重要。
- 🌱 在 OpenJS 基金会支持下，Lodash 进行了安全和基础设施改革，引入技术指导委员会和安全小组，转向社区共治模式，提升项目韧性。
- 💡 开源生态应关注维护者福祉，通过支持贡献、尊重边界和建立共享责任模型，确保关键项目的健康运行，背后是每个创造者的个人故事。

---

### [Lodash](https://lodash.com/)

**原文标题**: [Lodash](https://lodash.com/)

Lodash 是一个现代化的 JavaScript 实用工具库，提供模块化、高性能和额外功能，简化了数组、数字、对象、字符串等数据类型的处理。

- 📦 **模块化与灵活性**：提供核心构建（约 4kB）和完整构建（约 24kB），支持按需加载方法和功能编程（FP）版本，适用于多种模块格式如 CommonJS、ES 模块和 AMD。
- ⚡ **高性能与广泛支持**：优化性能，支持 Node.js 4+、Bun 1.0+ 及现代浏览器环境（如 Chrome、Firefox、Safari），并兼容旧版浏览器如 IE 11。
- 🔧 **丰富的实用功能**：包括数组迭代、对象操作、值测试和复合函数创建等，示例如 `_.defaults` 用于对象默认值合并，`_.partition` 用于数组分区。
- 📥 **便捷的安装与使用**：支持浏览器直接引入、npm 安装及 Node.js 中按需加载，提供 CDN 资源，并允许通过 cherry-pick 方法减少打包体积。
- 🌐 **开源与社区驱动**：基于 MIT 许可证发布，拥有活跃的维护团队和贡献者，提供详细文档、FP 指南和互补工具如 futil-js，便于开发者集成和扩展。

---

### [伟大的 CSS 扩展 | 巴特勒日志](https://blog.gitbutler.com/the-great-css-expansion)

**原文标题**: [The Great CSS Expansion | Butler's Log](https://blog.gitbutler.com/the-great-css-expansion)

CSS 正在经历一次重大扩展，许多以往需要 JavaScript 库才能实现的 UI 模式，现在可以通过原生 CSS 功能来完成。这不仅能显著减少 JavaScript 依赖和代码体积，还能提升性能、降低维护成本，并带来更好的用户体验。文章详细介绍了多个已落地或即将落地的 CSS 新特性，它们分别替代了哪些流行的 JavaScript 库，并探讨了 CSS 尚未解决的少数领域。

- 🎯 **锚点定位**：CSS Anchor Positioning 允许元素相对于另一个“锚点”元素进行定位，无需 JavaScript 即可实现工具提示、下拉菜单的自动定位和溢出处理，替代了 Floating UI、Popper.js 等库。
- 🪟 **弹出层 API**：HTML 的 `popover` 属性和 Popover API 提供了原生的、可访问的非模态弹出层（如工具提示、菜单），自动处理显示/隐藏、焦点管理和轻量关闭，可替代 Radix UI、Headless UI 的部分功能。
- 💬 **对话框元素**：原生 `<dialog>` 元素配合 `showModal()` 方法，提供了功能完整的模态对话框，内置焦点锁定、ESC 关闭和背景交互阻止，可替代专门的对话框库和焦点陷阱逻辑。
- 📜 **滚动驱动动画**：CSS Scroll-Driven Animations 通过 `animation-timeline: scroll()` 等属性，将动画直接绑定到滚动进度，运行在合成器线程，性能更优，可替代 GSAP ScrollTrigger 等库。
- 🔄 **视图过渡 API**：View Transitions API 让浏览器能够捕获页面或状态变化前后的快照，并自动创建平滑的过渡动画，简化了单页应用的路由切换效果，可替代部分动画库。
- 🔽 **可自定义的选择框**：CSS 正在获得对 `<select>` 元素及其内部部件（如选项列表）的完全样式控制能力，有望终结为样式而重建选择框的历史，替代 react-select、Radix Select 等库。
- 🧭 **焦点组**：提案中的 `focusgroup` HTML 属性旨在声明式地处理复合部件（如工具栏、标签页）内的箭头键导航，无需编写 JavaScript 样板代码。
- 🧱 **网格通道（砌体布局）**：CSS Grid 扩展提案（原 Masonry 布局）旨在通过类似 `grid-template-rows: masonry` 的属性实现砌体式布局，可替代 Masonry.js、Isotope 等库。
- 📏 **字段尺寸**：`field-sizing: content` 属性让 `<textarea>` 等输入元素能根据内容自动调整高度，无需 JavaScript 监听输入事件。
- 🎚️ **滚动状态查询**：CSS Scroll State Queries 允许通过容器查询检测元素是否处于“粘滞”、“对齐”或“可滚动”状态，无需使用 JavaScript 监听滚动事件。
- ⚙️ **原生 CSS 条件逻辑**：即将到来的 CSS `if()` 函数允许在 CSS 中进行条件值设置，结合 `@container style()` 查询，可实现更强大的组件逻辑。
- 💾 **节省与收益**：用原生 CSS 替代相应的 JavaScript 库，可显著减少代码体积（保守估计可节省约 44 kB，激进场景可达 ~146 kB），并带来解析执行性能提升、更好的核心网页指标和更低的维护成本。
- 🚫 **尚未解决的领域**：复杂的拖放交互和真正的覆盖式滚动条（特别是在 Windows 上）目前仍需依赖 JavaScript 库，CSS 尚无成熟的替代方案。
- 🔁 **持续的模式**：Web 平台的发展遵循着“先用 JavaScript 实现，后由 CSS/HTML 原生支持”的循环，当前正处在新一轮功能原生化的过渡期。

---

### [在 Three.js 中构建双场景流体 X 射线揭示效果 | Codrops](https://tympanus.net/codrops/2026/03/23/building-a-dual-scene-fluid-x-ray-reveal-effect-in-three-js/)

**原文标题**: [Building a Dual-Scene Fluid X-Ray Reveal Effect in Three.js | Codrops](https://tympanus.net/codrops/2026/03/23/building-a-dual-scene-fluid-x-ray-reveal-effect-in-three-js/)

本教程详细介绍了如何使用 Three.js 结合 TSL 和 WebGPU 构建一个动态的双场景流体 X 射线揭示效果，通过鼠标轨迹驱动流体模拟，实现从实体模型到骨架模型的平滑过渡。

- 🖱️ **鼠标轨迹生成**：通过 2D 画布创建黑白圆形遮罩，并利用线性插值平滑跟随光标移动，形成流畅的输入源。
- 🌊 **流体模拟转换**：采用乒乓渲染技术，将鼠标轨迹输入通过 FBM 噪声扩散，形成动态的流体效果，并随时间逐渐消退。
- 🎭 **双场景渲染**：分别渲染实体场景和 X 射线骨架场景，使用相同的相机、灯光和环境设置，确保两者空间对齐。
- 🔧 **实例化网格优化**：通过 InstancedMesh 高效渲染多个模型副本，采用六边形网格布局增强视觉紧凑感。
- ✨ **菲涅尔发光材质**：为模型创建边缘发光效果，通过混合核心颜色与菲涅尔强度，实现 X 射线般的视觉表现。
- 🎨 **后期处理合成**：整合流体遮罩、泛光、扫描线、胶片颗粒和色彩分级等多重效果，最终融合两个场景。
- 🔄 **渲染循环协调**：每帧更新鼠标轨迹、流体模拟和后期处理管线，确保所有组件同步运行以实现平滑的交互效果。

---

### [Intl 也能本地化单位！ | Stefan Judis 网页开发](https://www.stefanjudis.com/today-i-learned/intl-can-localize-units-too/)

**原文标题**: [Intl can localize units, too! | Stefan Judis Web Development](https://www.stefanjudis.com/today-i-learned/intl-can-localize-units-too/)

Intl API 不仅能格式化货币，还能根据地区本地化单位显示，让开发者无需手动处理复杂的国际化逻辑。

- 🌍 Intl API 支持根据地区格式化数字，如货币和单位
- 💶 示例：将数字格式化为欧元（德国地区显示为 "123.456.789,00 €"）
- 💴 日元符号位置自动调整（日本地区显示为 "￥123,456,789"）
- 🚗 单位本地化示例：葡萄牙地区显示 "50 km/h" 表示时速
- 🇫🇷 法语地区将 "kilobyte" 显示为 "kilooctets"，体现单位翻译
- ⚡ 开发者无需自行编写货币/单位格式化逻辑，功能已内置
- 📚 文章推荐查看官方支持的完整单位列表

---

### [迁移至 Solid 2.0 的经验总结](https://www.brenelz.com/posts/migrating-to-solid-2/)

**原文标题**: [Things Learned Migrating To Solid 2.0](https://www.brenelz.com/posts/migrating-to-solid-2/)

本文分享了作者迁移至 Solid 2.0 beta 版本的经验，重点介绍了 AI 工具如何加速迁移过程、Solid 2.0 在异步处理等方面的改进，并提供了具体的迁移技巧和注意事项。

- 🤖 **AI 显著提升迁移效率**：通过 AI 工具（如代码模型）快速处理 API 变更，例如自动适配`createEffect`的新参数结构，并结合本地代码库和测试套件保持迁移准确性。
- 🚀 **Solid 2.0 使用体验优化**：异步处理更自然，`createMemo`支持 Promise，过渡状态管理更平滑，减少了手动管理加载状态的心智负担。
- ⚙️ **迁移实用技巧**：包括配置测试库绕行方案、避免本地 Solid 版本重复、使用`next`标签更新依赖、注意`flush()`在单元测试中的调用，以及确保在`await`前完成信号追踪。
- ⚠️ **留意开发警告**：Solid 在开发阶段的警告（如“reactive read”）常暗示潜在问题，建议及时排查而非忽略。
- 🌟 **总体评价积极**：尽管早期迁移存在生态兼容性挑战，但 Solid 2.0 的改进值得升级，结合 AI 工具可使迁移过程更高效。

---

### [Fuse.js — 轻量级模糊搜索库 | Fuse.js](https://www.fusejs.io/)

**原文标题**: [Fuse.js — Lightweight Fuzzy-Search Library | Fuse.js](https://www.fusejs.io/)

Fuse.js 是一个轻量级模糊搜索库，无依赖，支持多种搜索功能，适用于浏览器、Node.js 和 Deno 环境。

- 🔍 **模糊搜索**：基于 Bitap 算法，支持容错匹配
- 📝 **分词搜索**：将多词查询拆分为术语，分别进行模糊匹配并按 IDF 排序
- 🔧 **扩展搜索**：支持精确、前缀、后缀、反向和包含匹配等操作符
- 🧠 **逻辑搜索**：提供 `$and` 和 `$or` 表达式用于结构化查询
- ⚖️ **加权搜索**：可为不同字段（如标题、描述）设置权重
- 🗂️ **嵌套搜索**：支持点符号、数组符号或自定义 `getFn` 访问嵌套数据
- 📦 **零依赖**：体积小巧，兼容浏览器、Node.js 和 Deno
- 📊 **两种构建版本**：完整版（约 8 kB gzip）和基础版（约 6.5 kB gzip）
- 🚀 **快速上手**：可通过 npm 安装，提供详细入门指南和在线演示

---

### [发布 v7.3.0 · krisk/Fuse · GitHub](https://github.com/krisk/Fuse/releases/tag/v7.3.0)

**原文标题**: [Release v7.3.0 · krisk/Fuse · GitHub](https://github.com/krisk/Fuse/releases/tag/v7.3.0)

Fuse.js 7.3.0 版本发布，引入了多项新功能、错误修复和内部重构。

- 🔍 新增每词模糊匹配与 IDF 评分功能
- 🧩 添加静态方法`Fuse.match()`用于单字符串匹配
- 🔢 支持 BigInt 类型用于索引和搜索
- 📦 `removeAt()`方法现在返回被移除的项
- 🔑 逻辑查询中支持无键字符串条目
- 🐛 修复扩展搜索中重叠匹配索引合并问题
- 🔄 修正多键反向模式匹配功能
- 💬 改进带空格和引号的引用标记处理
- 🌍 优化非可分解变音符号处理
- 🛠️ 完全使用 TypeScript 重写源代码
- 📚 文档重写为独立 Markdown 文件

---

### [发布 v7.4.0-beta.1 · krisk/Fuse · GitHub](https://github.com/krisk/Fuse/releases/tag/v7.4.0-beta.1)

**原文标题**: [Release v7.4.0-beta.1 · krisk/Fuse · GitHub](https://github.com/krisk/Fuse/releases/tag/v7.4.0-beta.1)

Fuse.js 发布了 v7.4.0-beta.1 版本，引入了通过 Web Workers 实现并行搜索的新功能，显著提升了大型数据集下的搜索性能。

- 🚀 **FuseWorker 功能** — 通过 Web Workers 实现并行搜索，在 10 万文档数据集上使用 8 个 Worker 时性能提升约 5 倍，且无界面卡顿
- ⚙️ **API 方法** — 支持 `search`、`add`、`setCollection`、`terminate` 等操作
- ⚠️ **测试版本说明** — 此为 Beta 版本，API 可能根据反馈进行调整
- 📊 **社区反应** — 发布后获得多个积极表情回应

---

### [Web Workers | Fuse.js](https://www.fusejs.io/web-workers.html)

**原文标题**: [Web Workers | Fuse.js](https://www.fusejs.io/web-workers.html)

FuseWorker 是 Fuse.js 的 Beta 版本功能，它利用 Web Workers 实现并行搜索，专为处理大规模数据集（如超过 10,000 条记录）设计，以保持用户界面的流畅响应。它通过将数据分片并在多个 Worker 中同时执行搜索来避免主线程阻塞，适用于实时搜索和移动设备等场景。虽然 API 与标准 Fuse 类相似，但 search() 方法返回 Promise，且需要在使用完毕后调用 terminate() 进行清理。对于小型数据集，建议继续使用标准的 Fuse 类以避免额外开销。

- 🚀 **并行搜索**：FuseWorker 通过 Web Workers 将数据集分片并行处理，显著提升大规模数据（10K+ 条）的搜索速度，保持 UI 流畅无卡顿。
- 🎯 **适用场景**：适合处理大型数据集、实时输入搜索（如逐字搜索）及移动设备，避免搜索导致的界面冻结问题。
- ⚙️ **简化集成**：自动处理数据分片、Worker 生命周期管理及结果合并排序，提供与 Fuse 相同的 API，只需异步调用 search()。
- 📦 **快速上手**：通过 npm 安装 Beta 版本，导入 FuseWorker 类并配置选项即可使用，使用后需调用 terminate() 清理资源。
- ⚡ **性能优势**：基准测试显示，使用 4 个 Worker 时搜索速度提升约 3.29 倍，接近线性扩展，但小型数据集（<5K 条）可能因开销而更适合标准 Fuse。
- 🔄 **功能差异**：相比 Fuse，FuseWorker 的 search() 返回 Promise，不支持 remove() 和 getIndex()，且结果对象为副本而非原始引用。
- 🌐 **浏览器支持**：兼容所有现代浏览器，但不适用于 Node.js 或受严格 CSP 策略限制的环境。
- 🛠️ **配置选项**：支持自定义 Worker 数量和脚本路径，以适配不同的构建工具和环境。

---

### [演示 | Fuse.js](https://www.fusejs.io/demo.html)

**原文标题**: [Demo | Fuse.js](https://www.fusejs.io/demo.html)

Fuse.js 是一个用于实现模糊搜索的 JavaScript 库，提供实时搜索演示、可配置选项和示例数据，支持在生产环境中使用并获取专业支持。

- 🔍 **实时演示功能**：用户可在线输入查询、调整选项并实时查看搜索结果更新
- ⚙️ **可配置搜索参数**：支持阈值设置、包含匹配分数、忽略位置等高级搜索选项
- 📚 **示例数据结构**：包含 19 个书籍项目，每项均有书名和作者姓名（含姓与名）字段
- 🔧 **代码集成示例**：展示如何初始化 Fuse 实例并配置搜索键（支持嵌套对象路径）
- 📖 **完整文档支持**：提供模糊搜索指南和入门教程链接
- 🏢 **生产环境支持**：提供优先技术支持、SLA 保证和发票支付等企业服务方案

---

### [现已推出：Depot CI](https://depot.dev/blog/now-available-depot-ci?utm_source=fnf&utm_medium=newsletter&utm_campaign=depot-april&utm_term=javascript-weekly&utm_content=depot-ci-blog)

**原文标题**: [Now available: Depot CI](https://depot.dev/blog/now-available-depot-ci?utm_source=fnf&utm_medium=newsletter&utm_campaign=depot-april&utm_term=javascript-weekly&utm_content=depot-ci-blog)

Depot 正式推出全新的 CI 引擎 Depot CI，旨在彻底解决现代软件开发中持续集成速度慢、效率低的问题。该引擎从底层重构了 CI 系统，通过自研的 Switchyard 架构实现任务调度与计算执行，显著提升了 CI 性能，并支持 GitHub Actions 等工作流无缝迁移。

- 🚀 **推出全新 CI 引擎**：Depot CI 是一个全新构建的持续集成引擎，专为高性能设计，旨在突破传统 CI 系统的速度瓶颈。
- 🧩 **完全兼容现有工作流**：支持将现有的 GitHub Actions 工作流一键迁移至 Depot CI，无需重写即可立即获得更快的 CI 体验。
- ⚡ **极致启动速度**：通过预热的自定义运行器镜像，CI 任务可在几秒内启动，避免了传统 CI 中漫长的环境准备时间。
- 🔧 **深度可编程与控制**：提供完整的 API、CLI 及调试工具（如日志、指标、SSH），支持以编程方式触发、监控和调试 CI 流程。
- 🏗️ **基于自研 Switchyard 架构**：核心由调度器（Orchestrator）和计算子系统（Compute）组成，实现了高性能的任务编排与执行，并支持多种前端（如 GitHub Actions、GitLab CI）。
- 💰 **灵活透明的定价**：采用按秒计费模式（$0.0001/秒），无最低消费或隐藏费用，并可与其他 Depot 产品分钟数合并使用。
- 🔮 **面向未来的扩展性**：Depot CI 是 Depot 在构建加速领域的最新一步，未来将基于 Switchyard 架构支持更多用例，帮助团队在 AI 时代保持从代码提交到部署的全流程高效。

---

### [获取失败](https://javascriptweekly.com/link/183331/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/183331/web)

无法总结：获取内容失败，状态码 403。

---

### [Babylon.js：强大、精美、简洁、开放——卓越的 Web 端 3D 体验](https://www.babylonjs.com)

**原文标题**: [Babylon.js: Powerful, Beautiful, Simple, Open - Web-Based 3D At Its Best ](https://www.babylonjs.com)

Babylon.js 9.0 发布，致力于打造强大、美观、简单且开放的网页渲染引擎，带来一系列新特性、优化和性能提升，旨在帮助开发者更快速地创建引人入胜的交互式网页体验。

- 🎨 **节点材质编辑器**：提供可视化材质编辑工具
- 💡 **集群光照**：优化光照性能与效果
- 🌟 **纹理区域光**：支持更真实的光照渲染
- ✨ **节点粒子编辑器**：可视化粒子系统创作工具
- 🌪️ **粒子流图与吸引器**：增强粒子运动控制
- ☀️ **体积光照**：实现大气光效渲染
- 🖼️ **帧图系统**：改进渲染管线管理
- 🕺 **动画重定向**：简化角色动画适配
- ☁️ **高斯泼溅支持**：先进点云渲染技术
- 🛠️ **Babylon.js 编辑器**：集成开发环境升级
- 🔍 **检查器 v2**：调试工具增强版
- 🌐 **大世界渲染**：支持超大场景渲染
- 🗺️ **地理空间相机**：地理坐标系统集成
- 🧱 **3D 瓦片支持**：大规模 3D 数据流式加载
- 🌍 **物理大气系统**：真实大气渲染
- 💎 **OpenPBR 支持**：开放物理渲染标准
- 👥 **动态 IBL 阴影**：基于图像的照明阴影优化
- 🔤 **SDF 文本渲染**：高质量文字显示
- 📐 **轮廓渲染器**：物体轮廓效果增强
- 🧭 **导航网格更新**：AI 路径规划改进
- 🔊 **音频引擎升级**：空间音频功能增强
- 📦 **3MF 导出器**：3D 打印格式支持
- 🎮 **知名应用案例**：包括 Nike 定制、Minecraft 经典版、Xbox 设计实验室等大型项目实践

---

### [Babylon.js 游乐场](https://playground.babylonjs.com/?webgpu&areaLights=1&volumetricLight=1&clusteredLights=1&camera=volumetric#8BQJH7)

**原文标题**: [Babylon.js Playground](https://playground.babylonjs.com/?webgpu&areaLights=1&volumetricLight=1&clusteredLights=1&camera=volumetric#8BQJH7)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理系统自动化处理病历、排班等流程，减轻医护行政负担
- ⚠️ 数据隐私保护与算法透明度仍是医疗 AI 推广需要解决的关键问题
- 🔮 未来 AI 或与远程医疗、可穿戴设备结合，构建预防性健康管理生态

---

### [Babylon.js 游乐场](https://playground.babylonjs.com/#J3MJSN)

**原文标题**: [Babylon.js Playground](https://playground.babylonjs.com/#J3MJSN)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，助力医院资源调度与远程医疗服务
- ⚠️ 数据隐私保护与算法透明度仍是亟待解决的技术伦理挑战
- 🔮 未来 AI 或将成为医疗人员的协同工具，推动精准医疗发展

---

### [已标记文档](https://marked.js.org/)

**原文标题**: [Marked Documentation](https://marked.js.org/)

Marked 是一个高性能的 Markdown 编译器，专注于快速解析，支持多种 Markdown 规范，并提供了 CLI、浏览器和 Node.js 等多种使用方式。

- ⚡ **高性能设计**：Marked 为速度而构建，是一个低级别的 Markdown 编译器，解析时无需缓存或长时间阻塞。
- 📚 **全面兼容**：轻量级的同时，完整实现了所支持的 Markdown 风格（如 Markdown 1.0, CommonMark, GitHub Flavored Markdown）中的所有功能。
- 🌐 **多环境可用**：既可作为命令行界面（CLI）工具使用，也可运行在客户端或服务器端的 JavaScript 项目中。
- ⚠️ **安全警告**：Marked 不会对输出的 HTML 进行消毒处理，处理潜在不安全字符串时，用户需自行防范 XSS 攻击，推荐使用 DOMPurify 等库。
- 🛠️ **灵活安装与使用**：可通过 npm 全局安装 CLI 或在项目中安装库，支持通过配置文件进行 CLI 定制，并提供了丰富的使用示例。
- ✅ **高规格支持率**：积极支持主流 Markdown 规范，测试通过率极高（如 Markdown 1.0 达 100%，CommonMark 0.31 达 98%）。
- 🔧 **生态与工具**：被许多工具（如 zero-md, texme）用于实现快速的 Markdown 转换，拥有活跃的社区支持。
- 🛡️ **重视安全**：项目非常重视安全性，鼓励通过指定渠道负责任地披露安全问题，并承诺及时评估和修复。

---

### [标记演示](https://marked.js.org/demo/)

**原文标题**: [Marked Demo](https://marked.js.org/demo/)

该工具是一个用于演示和测试 Markdown 语法的在线平台，提供实时预览和多种辅助功能。

- 🛠️ **功能演示**：展示 CommonMark 和 Daring Fireball 两种 Markdown 标准的渲染效果
- ⚙️ **交互操作**：支持输入框编辑、实时预览、HTML 源码查看及语法高亮数据展示
- 📚 **辅助工具**：内置快速参考指南，并显示系统响应时间
- 🌐 **技术依赖**：需要启用 JavaScript 才能正常使用该工具
- 🔄 **版本管理**：提供永久链接功能，当前运行版本为 master

---

### [GitHub - markedjs/marked：一款Markdown解析器与编译器，专为速度打造。· GitHub](https://github.com/markedjs/marked)

**原文标题**: [GitHub - markedjs/marked: A markdown parser and compiler. Built for speed. · GitHub](https://github.com/markedjs/marked)

Marked 是一个高性能的 Markdown 解析器和编译器，专为速度设计，支持多种 Markdown 规范，可在浏览器、服务器或命令行中运行，但输出 HTML 需自行净化以确保安全。

- ⚡ 专为速度构建的低级 Markdown 编译器，解析时不缓存或长时间阻塞
- ⚖️ 轻量级，支持所有主流 Markdown 变体和规范的功能
- 🌐 跨平台运行，兼容浏览器、服务器和命令行界面
- 🚨 输出 HTML 未经净化，需配合 DOMPurify 等安全库使用
- 📚 提供详细文档和演示页面，项目本身文档也由 Marked 渲染
- 📦 支持通过 npm 安装，提供 CLI、浏览器脚本和 ES 模块多种使用方式
- 🔧 仅支持当前和 LTS 版本的 Node.js，浏览器需符合 Baseline Widely Available 标准

---

### [发布 | TinyBase](https://tinybase.org/guides/releases/#v8-1)

**原文标题**: [Releases | TinyBase](https://tinybase.org/guides/releases/#v8-1)

TinyBase 发布了多个版本更新，引入了新功能、改进和破坏性变更，包括 Svelte 支持、对象和数组类型存储、中间件系统、状态钩子、参数化查询、模式转换器、空值支持、持久化与同步增强、React 集成、查询引擎、排序分页等。

- 🆕 **v8.1 新增 Svelte 支持**：引入 `ui-svelte` 模块，提供原生 Svelte 5 响应式绑定，包括响应式函数和视图组件，支持双向数据绑定和上下文共享。
- 🔄 **v8.0 扩展数据类型**：支持在 `Cell` 或 `Value` 中存储 JavaScript 对象和数组，并通过 JSON 编码实现持久化透明往返。
- ⚙️ **v8.0 引入中间件系统**：允许在数据写入 `Store` 前拦截和转换，支持验证、修改或拒绝变更，增强数据完整性。
- 🪝 **v7.3 新增状态钩子**：提供类似 React `useState` 的便捷钩子（如 `useCellState`），简化双向数据绑定，减少样板代码。
- 🔧 **v7.2 参数化查询**：为 TinyQL 添加参数化查询功能，允许通过命名参数动态更新查询结果，提升查询灵活性和效率。
- 📐 **v7.1 模式转换器**：引入 `Schematizers`，支持将 Zod、TypeBox 等外部验证库的模式转换为 TinyBase 格式，简化模式管理。
- 🆓 **v7.0 空值支持**：允许 `Cell` 和 `Value` 存储 `null` 值，并通过 `allowNull` 属性在模式中配置，区分 `null` 与 `undefined`。
- 💾 **v7.0 数据库持久化变更**：SQL `NULL` 值现在映射为 TinyBase `null`，导致从数据库加载的表变为密集而非稀疏，需更新数据访问模式。
- 🌐 **v6.7 支持 OPFS**：新增 `createOpfsPersister` 函数，支持在浏览器中使用 Origin Private File System 进行持久化。
- 🔍 **v6.6 检查器改进**：增强 Inspector 工具，提供现代化 UI 并支持直接创建、复制或删除表、行、值和单元格，便于调试。
- 📱 **v6.5 React Native MMKV 持久化**：新增 `persister-react-native-mmkv` 模块，支持通过 `react-native-mmkv` 库在 React Native 中持久化数据。
- 🗄️ **v6.4 React Native SQLite 持久化**：新增 `persister-react-native-sqlite` 模块，支持通过 `react-native-sqlite-storage` 库在 React Native 中使用 SQLite 数据库。
- ☁️ **v6.3 Cloudflare Durable Object SQL 存储**：新增 `persister-durable-object-sql-storage` 模块，支持在 Cloudflare Durable Object 中使用 SQLite 存储进行持久化和同步。
- 📦 **v6.2 打包改进**：引入 `omni` 模块作为所有 TinyBase 功能的超集，优化包结构和导出，减少捆绑包大小。
- 🐰 **v6.1 Bun SQLite 持久化**：新增 `createSqliteBunPersister` 函数，支持在 Bun 运行时中使用嵌入式 SQLite 数据库进行持久化。
- 🔄 **v6.1 子集持久化**：允许仅加载数据库表中的行子集到 `Store`，通过 `condition` 配置减少内存使用。
- 📊 **v6.1 排序行 ID 参数重构**：`getSortedRowIds` 等方法现在支持对象参数，简化调用并提高可读性。
- 🚀 **v6.1 新增自动持久化方法**：引入 `startAutoPersisting` 和 `stopAutoPersisting` 方法，方便同时启动或停止自动加载和保存。
- ⏱️ **v6.1 异步持久化与同步方法**：部分 `Persister` 和 `Synchronizer` 方法（如 `stopAutoLoad`、`destroy`）现在标记为异步，需使用 `await`。
- 🔄 **v6.0 模块结构更新**：仅提供现代 ESM 包，移除 CJS 和 UMD，更新依赖和基础设施，支持 React 19 作为可选对等依赖。
- ☁️ **v5.4 Cloudflare Durable Objects 同步**：新增 WebSocket 同步服务器，支持在 Cloudflare Durable Objects 上运行，实现客户端数据同步。
- 💾 **v5.4 Durable Objects 持久化**：新增 `DurableObjectStoragePersister`，支持将数据持久化到 Durable Object 存储层。
- 🖥️ **v5.4 服务器参考实现**：新增 `synchronizer-ws-server-simple` 模块，提供简单的 WebSocket 服务器实现，便于其他环境参考。
- 📚 **v5.4 架构指南**：新增架构选项文档，介绍如何在应用架构中使用 TinyBase，包括 Cloudflare Durable Objects 集成。
- ⚛️ **v5.3 React SSR 支持**：确保 TinyBase 在服务器端渲染环境中运行，感谢贡献者 Muhammad Muhajir。
- 📊 **v5.3 持久化状态跟踪**：所有 `Persister` 对象现在暴露加载和保存状态信息，可通过 `getStatus` 和 `addStatusListener` 方法跟踪。
- 🔄 **v5.3 同步器状态跟踪**：`Synchronizer` 对象作为 `Persister` 子类，同样支持状态跟踪和监听。
- 🪝 **v5.3 React 钩子增强**：新增 `usePersisterStatus`、`useSynchronizerStatus` 等钩子，方便在 React UI 中集成状态变化。
- 🛠️ **v5.3 提供者钩子**：新增 `useProvideMetrics`、`useProvideIndexes` 等钩子，支持通过 Provider 上下文动态注册对象。
- 🐘 **v5.2 PostgreSQL 持久化**：新增 `persister-postgres` 和 `persister-pglite` 模块，支持在服务器和浏览器中使用 PostgreSQL 数据库进行持久化。
- 🔧 **v5.2 自定义持久化创建函数**：暴露 `createCustomSqlitePersister` 和 `createCustomPostgreSqlPersister` 函数，支持构建自定义 SQLite 和 PostgreSQL 持久化器。
- 🚨 **v5.2 模块分离**：`persisters` 和 `synchronizers` 模块不再捆绑在主 `tinybase` 模块中，需单独导入。
- 🖥️ **v5.1 服务器持久化**：`createWsServer` 函数现在支持传递 `Persister` 实例，允许在服务器上持久化数据，确保客户端断开后数据不丢失。
- 🔍 **v5.1 同步器调试回调**：`Synchronizer` 创建函数现在支持可选的 `onSend` 和 `onReceive` 回调，便于在开发环境中调试同步问题。
- 🔄 **v5.0 MergeableStore 类型**：新增 `mergeable-store` 模块，提供 `MergeableStore` 类型，支持使用混合逻辑时钟（HLC）时间戳合并数据。
- 🌐 **v5.0 同步器框架**：引入 `Synchronizer` 框架，支持通过 WebSocket、BroadcastChannel 等方式在多个 `MergeableStore` 实例间同步数据。
- 📁 **v5.0 模块文件夹结构改进**：更新包结构以更好地支持旧版打包工具，提供清晰的导入路径，包括 JavaScript 版本、模式支持和压缩选项。
- 🚨 **v5.0 破坏性变更**：移除 `/lib/` 导入路径，默认提供非压缩代码，`persister-expo-sqlite` 模块仅支持 v14 及以上版本，检查器移至 `ui-react-inspector` 模块。
- 🔄 **v5.0 API 变更**：移除 `GetTransactionChanges` 和 `GetTransactionLog` 类型，重命名 `TransactionChanges` 为 `Changes`，更新 `Store` 接口方法，如 `setTransactionChanges` 改为 `applyChanges`。
- 💾 **v5.0 持久化器变更**：`createCustomPersister` 函数新增 `supportsMergeableStore` 参数，`load` 和 `startAutoLoad` 方法现在接受 `Content` 对象。
- ⚡ **v4.8 PowerSync 持久化**：新增 `persister-powersync` 模块，支持使用 PowerSync 的 SQLite 数据库进行持久化。
- 🗄️ **v4.7 LibSQL 持久化**：新增 `persister-libsql` 模块，支持使用 Turso 的 LibSQL 数据库进行持久化。
- ⚡ **v4.6 ElectricSQL 持久化**：新增 `persister-electric-sql` 模块，支持使用 ElectricSQL 客户端数据库进行持久化，并附带模板项目。
- 📱 **v4.5 Expo SQLite 现代版本支持**：新增 `persister-expo-sqlite-next` 模块，支持现代版 Expo SQLite 库（`expo-sqlite/next`）。
- 🔍 **v4.4 存在性监听器**：新增一系列监听器（如 `addHasTableListener`）和相应钩子，用于监听表、行、单元格和值的存在性变化。
- ☁️ **v4.3 PartyKit 集成**：新增 `persister-partykit-server` 和 `persister-partykit-client` 模块，支持与 PartyKit 云平台集成，实现协作和数据持久化。
- 💾 **v4.2 IndexedDB 持久化**：新增 `persister-indexed-db` 模块，支持在浏览器中使用 IndexedDB 进行持久化，通过轮询检测变化。
- 🖥️ **v4.1 DOM 组件**：新增 `ui-react-dom` 模块，提供预构建的 DOM 组件（如 `SortedTableInHtmlTable`），用于以表格形式显示数据。
- 🔍 **v4.1 检查器组件**：新增 `Inspector` 组件（原 `StoreInspector`），用于在调试环境中查看和编辑 `Store` 内容。
- 🗄️ **v4.0 SQLite 持久化**：新增 `persister-sqlite3`、`persister-sqlite-wasm` 等模块，支持在 Node 和浏览器中使用 SQLite 数据库进行持久化。
- 🔄 **v4.0 CRDT 框架持久化**：新增 `persister-yjs` 和 `persister-automerge` 模块，支持使用 Yjs 和 Automerge CRDT 框架进行数据同步和持久化。
- 🔄 **v4.0 新方法**：`Store` 新增 `getContent`、`setContent` 和 `setTransactionChanges` 方法，`Persister` 新增 `schedule` 方法。
- 🚨 **v4.0 破坏性变更**：更新 `DoRollback` 和 `TransactionListener` 回调的数据提供方式，自定义持久化器需更新实现。
- 📊 **v3.3 表单元格 ID 跟踪**：新增 `getTableCellIds` 方法和 `addTableCellIdsListener` 方法，支持跟踪表中所有行的单元格 ID 并监听变化。
- 🔄 **v3.2 事务开始监听器**：新增 `addStartTransactionListener` 方法，允许在事务开始时监听并可能修改数据。
- 📐 **v3.1 模式类型系统**：引入基于模式的类型系统，通过 `TablesSchema` 或 `ValuesSchema` 定义数据结构，增强 TypeScript 开发体验。
- 🛠️ **v3.1 工具模块**：新增工具模块，支持从模式生成 TypeScript 定义和实现文件，以及跟踪 `Store` 大小和结构。
- 🔄 **v3.0 键值存储功能**：新增键值存储功能，允许获取、设置和监听单个 `Value` 项，扩展了 TinyBase 的数据模型。
- 🚨 **v3.0 破坏性变更**：`getJson` 和 `setJson` 方法的行为变更，现在处理表格和键值数据，需更新相关调用。
- 🔍 **v2.2 工具模块**：新增工具模块，支持从模式生成 ORM 类 TypeScript 定义和实现文件，以及命令行工具。
- 🔑 **v2.1 多切片索引**：允许在索引中单个行 ID 存在于多个切片中，支持构建关键字搜索等功能。
- 🔍 **v2.0 查询引擎**：新增 `queries` 模块和 TinyQL 查询语言，支持选择、连接、过滤、分组、排序和分页数据，提供完整的响应式关系数据存储功能。
- 📊 **v2.0 排序和分页**：新增 `getSortedRowIds` 等方法，支持对行 ID 进行排序和分页，便于构建网格类用户界面。
- ⚛️ **v2.0 React 集成**：`ui-react` 模块全面支持查询功能，提供 `useCreateQueries` 钩子和 `ResultTableView` 等组件。
- 🔄 **v1.3 显式事务方法**：新增 `startTransaction` 和 `finishTransaction` 方法，支持显式封装事务，并添加事务完成监听器。
- ↩️ **v1.2 事务回滚**：`transaction` 方法新增 `doRollback` 回调，允许在事务未满足条件时回滚所有变更。
- 🚫 **v1.1 无效数据监听**：新增 `InvalidCellListener` 和 `addInvalidCellListener` 方法，允许监听和处理无效数据写入尝试。

---

### [GitHub - xdevplatform/xdk-typescript: XDK 自动生成代码的 TypeScript 仓库。 · GitHub](https://github.com/xdevplatform/xdk-typescript)

**原文标题**: [GitHub - xdevplatform/xdk-typescript: TypeScript repo for the XDK auto-generated code. · GitHub](https://github.com/xdevplatform/xdk-typescript)

这是一个用于 X API（原 Twitter API）的 TypeScript SDK，提供智能分页、多种认证方式、实时流式传输和完整的类型安全支持。

- 📦 **SDK 概述**：一个全面的 TypeScript SDK，支持 X API 的所有端点，包括用户、帖子、列表、书签和社区等功能。
- 🔐 **认证方式**：支持 Bearer 令牌（仅应用认证）、OAuth 1.0a（用户上下文）和 OAuth 2.0（用户上下文）多种认证方法。
- 📚 **类型安全**：完全使用 TypeScript 编写，提供所有端点和参数的完整类型定义，无需额外安装类型包。
- 🌐 **多平台支持**：可在 Node.js、浏览器和 React Native 中直接使用，无需额外填充或包。
- 🔄 **智能分页**：提供通用的分页器工具，支持手动分页和异步迭代，自动处理分页令牌。
- 📡 **实时流式传输**：支持事件驱动的实时数据流，具有自动重连功能，可监听数据、错误和关闭事件。
- ⚙️ **环境变量配置**：建议将敏感凭证（如 Bearer 令牌、客户端 ID 和密钥）存储在环境变量中。
- 🛠️ **错误处理**：分页和流式传输均提供错误处理机制，包括速率限制检测和重试逻辑。

---

### [发布 v20.0.0 · raineorshine/npm-check-updates · GitHub](https://github.com/raineorshine/npm-check-updates/releases/tag/v20.0.0)

**原文标题**: [Release v20.0.0 · raineorshine/npm-check-updates · GitHub](https://github.com/raineorshine/npm-check-updates/releases/tag/v20.0.0)

npm-check-updates 发布了 v20.0.0 版本，主要引入了自动冷却功能，并包含多项依赖更新与修复。

- 🚀 **自动冷却功能**：现在会根据 npm、yarn 或 pnpm 的配置自动应用冷却选项，排除未达到最小发布年龄的更新。
- ⚠️ **重大变更说明**：若使用了相关配置，工具会自动遵循冷却规则；否则无需任何操作。
- 🔧 **依赖更新与修复**：包括 strip-ansi、lodash、TypeScript ESLint 插件等多个依赖的版本升级及安全漏洞修复。
- 🛡️ **安全性增强**：修复了代码扫描中发现的字符串转义或编码不完整问题。
- 👋 **新贡献者加入**：本次版本迎来了 @onemen 和 @Copilot 两位新贡献者的首次贡献。
- 📊 **社区反应积极**：发布后获得了多个点赞、庆祝和爱心等积极反馈。

---

### [GitHub - neutralinojs/neutralinojs：轻量级跨平台桌面应用开发框架 · GitHub](https://github.com/neutralinojs/neutralinojs)

**原文标题**: [GitHub - neutralinojs/neutralinojs: Portable and lightweight cross-platform desktop application development framework · GitHub](https://github.com/neutralinojs/neutralinojs)

Neutralinojs 是一个轻量级、可移植的跨平台桌面应用开发框架，允许开发者使用 JavaScript、HTML 和 CSS 构建应用，支持 Linux、macOS、Windows、Web 和 Chrome 平台，并可通过扩展或子进程与其他编程语言集成。

- 🚀 **轻量跨平台**：不捆绑 Chromium，利用操作系统现有浏览器内核，减少应用体积
- 🔧 **快速开发**：提供 neu CLI 工具，支持秒级构建，兼容 React 等前端框架
- 🔌 **灵活扩展**：支持通过 IPC 扩展任意编程语言，或作为子进程集成
- 📚 **丰富生态**：内置 JavaScript 客户端库、WebSocket 通信和静态服务器
- 🌍 **社区活跃**：拥有 8.5k GitHub 星标，提供 Discord、讨论区和贡献指南
- ⚖️ **开源许可**：核心采用 MIT 协议，集成多项第三方开源库
- 🛠️ **持续发展**：发布路线图至 2025 年，支持赞助和捐赠

---

### [GitHub - iconfu/svg-inject：一个微小、直观、稳健且带缓存的解决方案，用于将SVG文件内联注入DOM。· GitHub](https://github.com/iconfu/svg-inject)

**原文标题**: [GitHub - iconfu/svg-inject: A tiny, intuitive, robust, caching solution for injecting SVG files inline into the DOM. · GitHub](https://github.com/iconfu/svg-inject)

SVGInject 是一个轻量级 JavaScript 库，用于将 `<img>` 标签引用的 SVG 文件内联注入为 `<svg>` 元素，从而允许通过 CSS 完全控制 SVG 的样式，如颜色、动画和悬停效果。它无需构建步骤，支持多种使用方式，并内置了缓存、ID 冲突预防和可选的净化功能以提高安全性。

- 🚀 **快速开始**：通过添加 `onload="SVGInject(this)"` 到 `<img>` 标签，或通过 JavaScript 调用 `SVGInject()` 函数即可使用。
- 🛠️ **多场景适用**：特别适合无构建步骤的项目，如 WordPress 站点、服务器渲染页面、动态内容及原型设计。
- ⚙️ **框架集成**：提供了与 React、Vue、Svelte 等前端框架集成的简单示例。
- 📦 **轻量且强大**：压缩后仅约 3.5 KB，无依赖，支持 Tree Shaking 并包含完整的 TypeScript 定义。
- ♿ **默认无障碍**：根据 `<img>` 的 `alt` 和 `title` 属性自动设置正确的 ARIA 角色和属性。
- 🛡️ **安全特性**：提供可选的净化选项以移除潜在的危险元素和属性，并支持通过钩子函数集成更严格的安全库。
- 🔧 **灵活配置**：提供丰富的 API 和配置选项，如缓存控制、属性复制、ID 唯一化以及多个生命周期钩子。
- 🌐 **浏览器支持**：支持所有现代浏览器（Chrome、Firefox、Safari、Edge），v2 版本不再支持 Internet Explorer。
- 📄 **许可与维护**：采用 MIT 许可证，由 INCORS 开发和维护。

---

### [GitHub - Justineo/vue-clamp：轻松实现多行文本截断。· GitHub](https://github.com/Justineo/vue-clamp)

**原文标题**: [GitHub - Justineo/vue-clamp: Clamping multiline text with ease. · GitHub](https://github.com/Justineo/vue-clamp)

这是一个用于 Vue.js 的文本截断工具库，提供便捷的多行文本截断功能。

- 📚 **项目简介**：vue-clamp 是一个 Vue.js 工具库，专门用于实现多行文本的截断显示
- 🌐 **在线资源**：提供完整的文档和演示网站（vue-clamp.void.app），方便用户查看使用示例
- 🛠️ **开发状态**：项目采用 TypeScript 和 Vue 开发，包含完整的测试套件和开发工作流程
- 📦 **版本管理**：已发布 v1.0.0 版本，提供迁移指南和更新日志
- ⭐ **社区活跃**：获得 779 个星标和 91 个分支，显示出一定的社区关注度
- 📄 **开源许可**：采用 MIT 许可证，允许自由使用和修改
- 🔧 **技术栈**：主要使用 TypeScript（54.1%）和 Vue（45.6%）开发

---

### [vue-clamp](https://vue-clamp.void.app/)

**原文标题**: [vue-clamp](https://vue-clamp.void.app/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统通过分析医学影像提升疾病检测准确率
- 💊 机器学习算法帮助个性化制定治疗方案，改善患者预后
- ⚡ 智能流程管理工具优化医院运营，减少候诊时间
- 🔬 自然语言处理技术加速临床研究与医学文献分析
- ⚖️ 面临数据隐私、算法透明度及医疗责任界定等伦理挑战

---

### [Vue 虚拟滚动器](https://vue-virtual-scroller.netlify.app/)

**原文标题**: [Vue Virtual Scroller](https://vue-virtual-scroller.netlify.app/)

专为处理大型列表设计，通过仅渲染可见内容、降低 DOM 操作负担，确保即使面对庞大数据集也能保持流畅响应。

- ⚡ 仅渲染可见内容，优化性能
- 📊 高效处理大型数据集，保持响应速度
- 🔧 减少 DOM 操作，提升运行效率

---

### [发布 v6.4.0 · verdaccio/verdaccio · GitHub](https://github.com/verdaccio/verdaccio/releases/tag/v6.4.0)

**原文标题**: [Release v6.4.0 · verdaccio/verdaccio · GitHub](https://github.com/verdaccio/verdaccio/releases/tag/v6.4.0)

Verdaccio 发布了 v6.4.0 版本，引入了新的包过滤插件功能，允许用户根据规则拦截或替换特定包版本，同时包含多项错误修复和依赖更新。

- 🚀 新增包过滤插件功能，支持按版本、范围或发布日期拦截或替换包
- 🛡️ 可配置规则阻止恶意包版本或整个作用域，增强安全性
- ⏳ 支持设置最小发布日期阈值，实现版本冻结或隔离新发布包
- 🔄 提供替换策略，可将不安全版本自动替换为较旧的稳定版本
- 🐛 修复了多个问题，包括依赖更新、中间件流读取和主机头处理
- 📦 更新了核心依赖项，提升了稳定性和安全性

---

### [GitHub - Shopify/react-native-skia: 使用 Skia 实现高性能 React Native 图形渲染 · GitHub](https://github.com/Shopify/react-native-skia)

**原文标题**: [GitHub - Shopify/react-native-skia: High-performance React Native Graphics using Skia · GitHub](https://github.com/Shopify/react-native-skia)

Shopify 开源的 React Native Skia 是一个高性能的 2D 图形库，它将 Google Skia 图形引擎引入 React Native 生态，用于在移动应用中实现高效的图形渲染。

- 🎨 **高性能图形渲染**：基于 Google Chrome 和 Android 等使用的 Skia 图形引擎，为 React Native 提供强大的 2D 绘图能力。
- 📱 **跨平台支持**：服务于 React Native 框架，帮助开发者在 iOS 和 Android 上构建一致的图形界面。
- 🚀 **实验性 Graphite 后端**：除了默认的 Ganesh 后端，还提供了下一代 Graphite 后端作为实验预览（需 Android API 26+），可通过 `@next` 渠道安装。
- 🔧 **开源与协作**：项目采用 MIT 许可证，拥有活跃的社区（8.3k 星标），提供详细的贡献指南和开发文档。
- 📚 **完善资源**：包含完整的安装指南、代码示例和安全策略，文档托管在专属网站上。

---

### [SunEditor — 轻量级所见即所得编辑器](https://suneditor.com/)

**原文标题**: [SunEditor — Lightweight WYSIWYG Editor](https://suneditor.com/)

本文介绍了加载过程中的用户体验设计原则和重要性，强调流畅的加载体验能有效减少用户流失并提升满意度。

- 🔄 加载状态需明确提示，避免用户困惑
- ⏳ 采用进度条或动画分散等待焦虑
- 🎨 骨架屏设计能提前布局感知速度
- 📱 根据网络环境适配加载策略
- 💡 趣味性微交互增强等待愉悦感

---

### [GitHub - productdevbook/hucre：零依赖电子表格引擎。读写XLSX、CSV、ODS文件。纯TypeScript，随处可用。· GitHub](https://github.com/productdevbook/hucre)

**原文标题**: [GitHub - productdevbook/hucre: Zero-dependency spreadsheet engine. Read & write XLSX, CSV, ODS. Pure TypeScript, works everywhere. · GitHub](https://github.com/productdevbook/hucre)

Hucre 是一个零依赖的纯 TypeScript 电子表格引擎，支持读取和写入 XLSX、CSV、ODS 格式，具备模式验证、流式处理和往返保留等特性，适用于各种 JavaScript 运行时。

- 📦 **零依赖与轻量** – 无外部依赖，核心库 gzip 后约 18 KB，支持按需导入以进一步减小体积。
- 🔄 **多格式支持** – 完整支持 XLSX、ODS 的读写和 CSV 的解析与生成，提供统一的自动检测 API。
- ⚡ **高性能流式处理** – 支持大型文件的逐行流式读取和写入，避免内存溢出。
- 🛡️ **往返保留** – 修改并保存文件时可保留原始图表、宏等未知部分，避免数据丢失。
- 🎨 **丰富功能** – 支持单元格样式、合并、数据验证、条件格式、超链接、图片、注释、表格、冻结窗格等。
- 📐 **智能列宽** – 根据内容自动计算列宽，支持 CJK 双倍字符和数字格式。
- 📋 **数据操作与导出** – 提供行/列插入删除、克隆移动等内存操作，支持导出为 HTML、Markdown、JSON。
- ✅ **模式验证** – 内置强大的模式验证功能，支持类型强制、模式匹配和错误收集。
- 🌐 **跨平台兼容** – 纯 TypeScript 实现，可在 Node.js、Deno、Bun、浏览器、Cloudflare Workers 等所有现代环境中运行。
- 🔧 **开发者友好** – 提供流畅的构建器 API、模板引擎、CLI 工具和完整的 TypeScript 类型支持。

---

### [GitHub - metafloor/bwip-js: 纯 JavaScript 条形码生成器 · GitHub](https://github.com/metafloor/bwip-js)

**原文标题**: [GitHub - metafloor/bwip-js: Barcode Writer in Pure JavaScript · GitHub](https://github.com/metafloor/bwip-js)

bwip-js 是一个纯 JavaScript 编写的条形码生成库，支持超过 100 种条形码类型，可在浏览器、Node.js、React、React Native 等多种平台上运行，生成 PNG、Canvas 或 SVG 格式的图像。

- 📦 **跨平台支持** – 适用于浏览器、Node.js、React、React Native、Electron 及命令行环境。
- 🏷️ **多种条形码类型** – 支持包括 QR Code、Code 128、Data Matrix、PDF417 等在内的 100 多种条形码标准。
- ⚙️ **灵活的配置选项** – 提供缩放、旋转、内边距、颜色等丰富的自定义参数。
- 🌐 **在线 API 与生成器** – 提供在线条形码生成服务和 API，方便直接调用。
- 📄 **多种输出格式** – 可生成 PNG（Node.js/React Native）、Canvas（浏览器）或 SVG（全平台）格式的图像。
- 🔧 **模块化导入** – 支持按需导入特定条形码编码器，以优化打包体积。
- 📖 **完整文档与示例** – 提供详细的文档、示例代码及在线演示，便于快速上手。

---

### [网络研讨会注册 - Zoom](https://us06web.zoom.us/webinar/register/WN_w_uG2-SVQIORqhs4btFtcQ#/registration?utm_source=newsletter&utm_medium=paid&utm_campaign=javascript_weekly&utm_content=april_7)

**原文标题**: [Webinar Registration - Zoom](https://us06web.zoom.us/webinar/register/WN_w_uG2-SVQIORqhs4btFtcQ#/registration?utm_source=newsletter&utm_medium=paid&utm_campaign=javascript_weekly&utm_content=april_7)

本文介绍了 Zoom 网站的语言支持和辅助功能选项，以及相关的版权与隐私政策信息。

- 🌐 提供多语言界面切换，包括英语、中文、西班牙语等
- ♿ 设有辅助功能概述，提升网站可访问性
- 📞 包含支持服务入口
- ©️ 明确版权归属 Zoom 视频通讯公司
- 🔒 列出隐私政策、法律条款及 Cookie 偏好设置选项

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified%20)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified%20)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用交互来生成并持续更新端到端测试套件，旨在彻底消除传统测试的维护负担和不可靠性，帮助开发团队以更快速度、更高可靠性交付代码。

- 🎯 **监控交互生成测试**：通过在开发、预演环境中添加脚本标签，记录用户会话并自动生成覆盖所有代码分支的视觉端到端测试。
- 🔄 **测试套件持续进化**：AI 引擎根据应用变化动态增删测试，确保测试套件始终最新且完整，无需人工维护。
- 🚀 **无副作用与零误报**：通过模拟后端响应实现无副作用测试，避免因数据变化导致的误报，无需设置测试账户或模拟数据。
- ⚡ **闪电般快速执行**：基于 Chromium 构建的确定性调度引擎消除测试波动性，支持大规模并行测试，数千次测试可在 120 秒内完成。
- 🔗 **灵活集成与易用性**：可补充或替代现有测试套件，支持主流前端框架（如 React、Vue、Angular），几分钟即可完成设置。
- 🏢 **受企业信赖**：已被 Dropbox、Notion 等超过 100 家组织采用，显著提升开发效率与代码可靠性。

---

### [数据网格演示 - 适用于 JavaScript、React、Angular 和 Vue 的 Handsontable 数据网格。](https://handsontable.com/demo?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=jsweekly&utm_medium=newsletter&utm_term=classified-ad)

**原文标题**: [Data grid demo - Handsontable data grid for JavaScript, React, Angular, and Vue.](https://handsontable.com/demo?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=jsweekly&utm_medium=newsletter&utm_term=classified-ad)

Handsontable 是一个用于构建网页应用的 JavaScript 数据表格组件，提供实时金融仪表盘、库存管理和项目管理等多种功能演示，并拥有全面的产品线、技术文档和社区支持资源。

- 📊 提供实时金融仪表盘，包含股票组合计算、条件格式和货币格式化
- 📦 库存管理系统支持公式计算总值、单元格验证和状态标记
- 📅 项目管理工具具备日期单元格、进度条渲染和拖拽排序功能
- 🛠️ 支持 React/Vue/Angular 等框架并附带 HyperFormula 计算引擎
- 📚 提供完整文档、API 参考和知识库等开发者资源
- 🌐 拥有 GitHub 论坛、StackOverflow 和专业技术支持渠道
- 🏢 被全球创新企业采用，提供免费试用和企业级解决方案

---

### [SerpApi 游乐场 - SerpApi](https://serpapi.com/playground/?utm_source=cooperpress&utm_campaign=javascript_classified)

**原文标题**: [SerpApi Playground - SerpApi](https://serpapi.com/playground/?utm_source=cooperpress&utm_campaign=javascript_classified)

SerpApi Playground 是一个用于测试和探索各种搜索引擎及平台 API 功能的在线工具，支持多种数据格式和搜索模式。

- 🔍 支持多种搜索引擎 API 测试，包括 Google、Bing、Amazon 等主流平台
- 📊 提供 HTML 和 JSON 数据格式的 URL 输出，便于数据抓取和分析
- 🤖 集成 AI 功能，如 AI Overview 和 Autocomplete，增强搜索智能化
- 🛒 涵盖电商、地图、视频、学术等垂直搜索领域，满足多样化需求
- 🔧 包含实用工具如历史记录和代码导出，方便开发者调试和集成

---

### [CSS 被 DOOM 化 - 用 CSS 3D 渲染 DOOM | 你好，我是 Niels Leenheer](https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/)

**原文标题**: [CSS is DOOMed - Rendering DOOM in 3D with CSS | Hello my name is Niels Leenheer](https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/)

本文介绍了一个使用 CSS 渲染的《毁灭战士》游戏项目，展示了现代 CSS 的强大功能，通过将游戏逻辑与渲染分离，利用 CSS 3D 变换、自定义属性、动画和新兴特性实现了完整的游戏视觉效果。

- 🎮 项目使用 CSS 渲染《毁灭战士》，所有墙壁、地板和敌人均为`<div>`元素，通过 CSS 3D 变换定位，JavaScript 仅处理游戏逻辑
- 📐 利用 CSS 函数如`hypot()`和`atan2()`计算几何，将原始游戏坐标转换为 CSS 3D 空间，无需额外转换
- 🌍 通过移动整个场景而非摄像机实现视角变换，仅需更新四个自定义属性即可控制玩家移动和旋转
- 🧩 使用`clip-path`和`shape()`处理非矩形地板和孔洞，确保纹理无缝拼接
- 🚪 利用 CSS 过渡和`@property`实现门、升降机动画，无需 JavaScript 动画循环
- 👻 通过 SVG 滤镜和`filter: brightness()`实现敌人隐身效果和动态光照
- 📱 使用锚点定位使游戏界面完全响应式，适应不同屏幕尺寸
- 🎯 采用 CSS 动画处理抛射物和爆炸效果，元素在动画结束后自动移除
- 🧠 实验性纯 CSS 剔除技术优化性能，通过动画延迟控制元素可见性
- 🐞 项目过程中遇到多个浏览器兼容性问题，如 Safari 中 View Transitions 破坏 3D 渲染

---

### [cssDOOM](https://cssdoom.wtf/)

**原文标题**: [cssDOOM](https://cssdoom.wtf/)

《CSS DOOM》是一款使用 CSS 技术完全渲染的《DOOM》复刻版，游戏逻辑通过 JavaScript 重新实现，而视觉效果则完全依赖 CSS 变换、动画和 SVG 滤镜完成。

- 🎮 游戏操作：使用 W/A/S/D 键移动，鼠标控制转向与射击
- 🚀 特色技术：全部视觉效果通过 CSS 变换与动画实现
- ⚙️ 开发背景：由 Niels Leenheer 基于 JavaScript 重制
- 📜 版权声明：使用原版《DOOM》素材，遵循合理使用原则
- 🔗 扩展信息：提供“阅读更多”链接获取详细内容

---

### [GitHub - NielsLeenheer/cssDOOM：一个用CSS实现的DOOM引擎 · GitHub](https://github.com/NielsLeenheer/cssDOOM)

**原文标题**: [GitHub - NielsLeenheer/cssDOOM: A DOOM engine implemented in CSS · GitHub](https://github.com/NielsLeenheer/cssDOOM)

这是一个完全使用 CSS 3D 变换和 DOM 元素重新渲染的经典游戏《DOOM》的项目，通过 CSS 自定义属性、三角函数和现代 CSS 特性实现游戏场景、动画和交互，而非传统的 Canvas 或 WebGL 技术。

- 🎮 **项目概述**：使用纯 CSS 和 JavaScript 重新实现《DOOM》游戏引擎，所有渲染均通过 CSS 3D 变换完成。
- 🧩 **技术核心**：基于 DOOM 的 WAD 文件数据，通过 CSS 自定义属性传递几何信息，并用`hypot()`、`atan2()`等 CSS 函数计算元素尺寸与位置。
- 🎯 **渲染分离**：JavaScript 仅更新玩家位置和角度等少量 CSS 变量，CSS 负责所有视觉变换和动画，实现逻辑与渲染解耦。
- 🕹️ **输入支持**：统一处理鼠标、键盘、触摸和游戏手柄输入，鼠标视角通过 Pointer Lock API 实现精准控制。
- ✨ **CSS 特性应用**：广泛使用`preserve-3d`、`clip-path`、`steps()`动画、`@property`动画、CSS 锚点定位和 SVG 滤镜等现代 CSS 功能。
- 🚪 **交互效果**：门、升降梯等通过 CSS 过渡实现动画；敌人精灵使用`steps()`帧动画和`scaleX(-1)`镜像处理。
- ⚡ **性能挑战**：因需处理大量 3D 变换元素，性能压力较大，通过 JavaScript 视锥剔除和实验性纯 CSS 剔除进行优化。
- 🐛 **已知问题**：Safari 中 View Transitions 会破坏 3D 场景；Chromium 浏览器可能出现纹理闪烁；部分 CSS 属性如`background-image`使用自定义变量会导致性能问题。
- 📜 **开源许可**：项目基于 GPL-2.0 许可证，原始游戏设计归 id Software 所有，CSS 实现由 Niels Leenheer 完成。

---

### [GitHub - elixir-volt/quickbeam：适用于BEAM的JavaScript运行时——由OTP支持、原生DOM及内置TypeScript工具链驱动的Web API。· GitHub](https://github.com/elixir-volt/quickbeam)

**原文标题**: [GitHub - elixir-volt/quickbeam: JavaScript runtime for the BEAM — Web APIs backed by OTP, native DOM, and a built-in TypeScript toolchain. · GitHub](https://github.com/elixir-volt/quickbeam)

QuickBEAM 是一个为 BEAM 虚拟机设计的 JavaScript 运行时，它通过 OTP 提供 Web API 支持，内置原生 DOM 和 TypeScript 工具链，使 JavaScript 代码能够与 Elixir/Erlang 生态系统深度集成。

- 🚀 **快速启动与集成** – 通过简单的 `QuickBEAM.start()` 即可启动运行时，支持直接执行 JavaScript 和 TypeScript 代码，并与 BEAM 进程无缝交互。
- 🔗 **BEAM 深度集成** – JavaScript 可以调用 Elixir 函数、访问 OTP 库，并支持向任何 BEAM 进程发送消息，实现双向通信。
- 🧩 **灵活的运行时管理** – 支持独立运行时、上下文池（ContextPool）等多种模式，适用于高并发场景，并能与 Phoenix LiveView 等框架轻松集成。
- 🌐 **全面的 API 支持** – 提供浏览器 API、Node.js API 及 BEAM 专属 API（如 `Beam.call`、`Beam.send`），并支持按需加载 API 组以优化资源。
- 🛡️ **资源限制与安全性** – 可为每个上下文设置内存和操作限制，支持沙箱化执行用户代码，确保系统稳定性与安全。
- 🔧 **内置开发工具** – 包含 TypeScript 编译、代码压缩、模块打包等工具链，无需外部构建步骤，并支持直接使用 npm 包。
- ⚡ **高性能与轻量级** – 基于 QuickJS 和原生 Zig 实现，性能优于传统方案，上下文池模式大幅降低内存占用，适合大规模并发。
- 📄 **原生 DOM 操作** – 集成 lexbor 库提供完整的 DOM 支持，Elixir 可直接查询和操作 DOM 结构，无需通过 JavaScript 执行。
- 📊 **监控与内省** – 提供运行时诊断、内存使用统计、字节码反汇编等功能，便于调试和性能优化。
- 📚 **丰富的示例与文档** – 提供聊天室、AI 代理、实时仪表盘等多种应用示例，展示其在实时 Web、SSR、规则引擎等场景下的实际应用。

---

### [Elixir 编程语言](https://elixir-lang.org/)

**原文标题**: [The Elixir programming language](https://elixir-lang.org/)

Elixir 是一种动态函数式编程语言，专为构建可扩展且可维护的应用程序而设计。它运行在 Erlang 虚拟机上，支持高并发、分布式和容错系统，适用于 Web 开发、嵌入式软件、机器学习等多个领域。

- 🚀 **平台特性**：基于轻量级进程实现高并发，支持垂直与水平扩展，并具备容错机制，通过监督树自动恢复系统故障。
- 🧠 **语言特性**：采用函数式编程范式，支持模式匹配和领域特定语言（DSL），提升代码简洁性和可维护性。
- 🛠️ **工具生态**：提供 Mix 构建工具、Hex 包管理器、交互式开发环境 IEx 和 Livebook 代码笔记本，简化开发流程。
- 🔗 **Erlang 兼容**：完全兼容 Erlang 生态系统，可无缝调用 Erlang 函数，适用于构建分布式高容错应用。
- 🌍 **生产应用**：被众多公司用于生产环境，涵盖 Web、物联网、实时通信等领域，社区活跃且资源丰富。

---

### [CSS 还是 BS？](https://www.keithcirkel.co.uk/css-or-bs/)

**原文标题**: [CSS or BS?](https://www.keithcirkel.co.uk/css-or-bs/)

这是一个测试 CSS 知识的小游戏，玩家需要判断显示的 CSS 属性名称是真实存在的还是虚构的。游戏包含 20 轮，难度逐渐增加，并会根据玩家的表现给出幽默的反馈和最终评分。

- 🎮 **游戏玩法**：玩家需判断显示的 CSS 属性是真实（CSS）还是虚构（BS），共 20 轮。
- 📚 **挑战性**：CSS 规范包含 600 多个属性，有些真实属性听起来像虚构的，而虚构的属性可能听起来很真实。
- 😄 **互动反馈**：游戏根据玩家的选择提供即时、幽默的评论，从简单鼓励到高级调侃。
- 🏆 **评分系统**：游戏结束后，根据正确率给出从“新手”到“专家”的不同等级评价。
- 🔄 **重玩选项**：玩家可以随时重新开始游戏，挑战更高分数。

---

### [电子邮件地址混淆：2026 年哪些方法有效？](https://spencermortensen.com/articles/email-obfuscation/)

**原文标题**: [Email address obfuscation: What works in 2026?](https://spencermortensen.com/articles/email-obfuscation/)

本文介绍了 2026 年有效的电子邮件地址混淆技术，旨在防止垃圾邮件发送者自动抓取邮箱。文章通过实验统计了各种方法的拦截效果，并建议结合使用多种技术以增强保护。同时，文章也回应了常见的批评，并解释了其数据收集方法。

- 📧 **纯文本保护技术**：包括 HTML 实体（拦截 95%）、HTML 注释（99%）、SVG 嵌入（100%）、CSS 隐藏（100%）及多种 JavaScript 方法（如拼接、ROT18、转换、AES 加密等，均达 100% 拦截），但部分方法如符号替换、指令说明等会破坏可用性。
- 🔗 **可点击链接保护技术**：涵盖 HTML 实体编码（100%）、URL 编码（95%）、HTTP 重定向（100%）、SVG 嵌入（100%）及 JavaScript 方法（如拼接、ROT18、转换、AES 加密等，拦截率 99%-100%），确保“mailto”链接不被轻易识别。
- ⚠️ **技术局限性**：部分方法如 HTML 图像、CSS 内容生成或文本方向反转虽能拦截垃圾邮件，但会严重影响用户体验，导致邮箱地址无法复制或需手动调整，因此不推荐使用。
- 🛡️ **组合使用建议**：理想情况下应混合应用多种技术，例如将邮箱地址分段并用不同方法保护，以应对大多数基础爬虫程序，提升整体防护效果。
- 📊 **实验方法论**：文章本身作为“蜜罐”吸引爬虫，通过监控各技术对应邮箱接收垃圾邮件的情况来统计拦截率，并强调数据基于独立邮件服务器收集，以避免主流邮件服务的过滤干扰。
- 🤔 **争议与回应**：针对“垃圾邮件发送者不再爬取网页”等批评，文章指出热门内容仍易受攻击，且这些技术历史悠久、持续有效，配合垃圾邮件过滤器可提供无假阳性、简单高效的额外保护。

---

