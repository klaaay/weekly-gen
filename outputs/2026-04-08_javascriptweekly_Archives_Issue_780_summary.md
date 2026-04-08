### [JavaScript周刊第780期：2026年4月7日](https://javascriptweekly.com/issues/780)

**原文标题**: [JavaScript Weekly Issue 780: April 7, 2026](https://javascriptweekly.com/issues/780)

Google开源了JSIR，这是一种用于JavaScript的高级中间表示（IR），旨在为新一代工具（如更智能的linter和打包工具）奠定基础。本期还涵盖了JavaScript生态的最新动态，包括框架更新、工具发布以及行业趋势。

- 🛠️ Google开源JSIR，为JavaScript工具链的未来发展铺平道路
- 📅 Anthropic提供免费的Claude Code工作坊，由Lydia Hallie主讲
- 📚 Chris Coyier发布2026版JavaScript知识概览，涵盖最新ECMAScript特性和工具
- 🔓 Axios团队发布npm供应链攻击的事后分析报告
- ⚡ 主流浏览器厂商推出JetStream 3性能测试套件
- 🛡️ 文章探讨最小发布年龄作为供应链防御策略的价值
- 🎬 Tanner Linsley介绍TanStack Start框架，适用于React和Solid开发者
- 😔 采访Lodash创作者John-David Dalton，讨论开源维护者的倦怠问题
- 🎨 现代CSS已能处理许多以往需JavaScript实现的效果
- 🔍 Fuse.js 7.3发布，增强模糊搜索功能，支持大规模数据集
- 🚀 Babylon.js 9.0推出，新增粒子编辑器和体积光照等功能
- 📝 Marked.js 18.0发布，专注于性能的Markdown解析器
- 💾 TinyBase v8.1增加对Svelte 5的原生支持
- 🐦 X平台推出官方TypeScript SDK
- 🧪 多个工具更新，包括npm-check-updates、Neutralinojs和React Native Skia

---

### [[RFC] JSIR：面向JavaScript的高级中间表示 - MLIR - LLVM讨论论坛](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

**原文标题**: [[RFC] JSIR: A High-Level IR for JavaScript - MLIR - LLVM Discussion Forums](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

JSIR 是一种基于 MLIR 的高层 JavaScript 中间表示，旨在填补 JavaScript 工具链中缺乏公开、稳定 IR 的空白。它通过保留 AST 的全部信息，支持从源代码到 AST 再到 JSIR 的无损往返转换，并利用 MLIR 区域表示控制流结构，同时提供数据流分析能力。JSIR 已在 Google 内部用于代码分析和转换任务，如反编译和反混淆，并已开源。

- 🎯 **动机与目标**：为 JavaScript 提供高层 IR，以支持控制流图和数据流分析，满足如转译、优化和打包等源码到源码的转换需求。
- 🔄 **设计特点**：JSIR 与 ESTree 标准高度对应，确保 AST 到 IR 的一对一映射，并通过后序遍历 AST 生成 IR，实现 99.9%+ 的往返转换成功率。
- 🏗️ **技术实现**：使用 MLIR 区域处理控制流结构（如 if、while 语句），区分左值和右值以明确语义，并提供基于 MLIR 的数据流分析 API，简化分析定义。
- 🚀 **应用与验证**：已在 Google 生产环境中用于 Hermes 字节码反编译和结合 Gemini LLM 的反混淆任务，相关论文被 ICSE 2026 接收。
- 🌍 **社区意义**：JSIR 的成功将证明 MLIR 适用于通用语言 IR 定义，挑战 AST 与 IR 的界限，并可能推动 MLIR 内置功能（如符号表）的改进与上游贡献。
- 🔮 **未来方向**：考虑采用更多 MLIR 内置功能（如 memref）、贡献区域数据流分析改进至上游，并探讨将 JSIR 上游化至 MLIR 的可行性，尽管存在依赖库（如 QuickJS、Babel/SWC）的挑战。

---

### [GitHub - google/jsir：下一代JavaScript分析工具集 · GitHub](https://github.com/google/jsir)

**原文标题**: [GitHub - google/jsir: Next-generation JavaScript analysis tooling · GitHub](https://github.com/google/jsir)

JSIR是一个基于MLIR的下一代JavaScript分析工具，其核心设计支持数据流分析和无损转换回源代码，适用于源码到源码的转换场景。

- 🛠️ **核心功能**：提供高层次的中间表示，既能还原为AST以支持源码转换和反编译，又能进行数据流分析以实现污点分析和常量传播等。
- 🔍 **应用场景**：在Google内部用于JavaScript代码分析和转换，例如反编译Hermes字节码和代码反混淆。
- 🐳 **快速开始**：推荐使用Docker镜像快速体验，也可通过Bazel构建工具在Linux环境中自行编译和测试。
- 📚 **资源链接**：包含2024年LLVM开发者会议的相关演讲和结合LLM进行反混淆的学术论文。
- ⚠️ **免责声明**：该项目并非Google官方产品，采用Apache-2.0许可证开源。

---

### [中间表示 - 维基百科](https://en.wikipedia.org/wiki/Intermediate_representation)

**原文标题**: [Intermediate representation - Wikipedia](https://en.wikipedia.org/wiki/Intermediate_representation)

中间表示（IR）是编译器或虚拟机内部用于表示源代码的数据结构或代码，旨在便于优化和翻译等进一步处理。它必须准确且独立于特定源语言或目标语言，形式可以是内存数据结构或基于元组/栈的中间语言。

- 🏗️ IR是编译器或虚拟机内部表示源代码的数据结构或代码，便于优化和翻译
- ✅ 良好的IR需准确无误地表示源代码，并独立于任何特定源语言或目标语言
- 🔄 IR形式多样，包括内存数据结构或可读的中间语言，如三地址码
- 🌐 常用IR示例包括CPython的图结构、GCC的GIMPLE和LLVM的IR，支持多源语言和多目标架构
- 💻 C语言因其普适性常被用作中间语言，如Eiffel、Nim等语言的编译过程
- ⚙️ 面向虚拟机的语言（如Java字节码、CIL）也属于中间语言，用于静态或动态编译
- 🛠️ GCC和LLVM等编译器框架使用多种IR（如RTL、GIMPLE、LLVM IR）以增强可移植性和跨平台编译
- 🔍 静态分析工具（如Radare2）使用IR（如ESIL、REIL）进行二进制文件分析和逆向工程

---

### [Anthropic Lydia Hallie深度解析Claude代码 | AddEvent](https://www.addevent.com/event/8n58y7bjwqmr)

**原文标题**: [Claude Code Deep Dive with Lydia Hallie from Anthropic | AddEvent](https://www.addevent.com/event/8n58y7bjwqmr)

Anthropic公司的Lydia Hallie将举办一场关于Claude Code的深度技术研讨会，由Frontend Masters提供免费独家工作坊，旨在帮助开发者深入理解并自定义Claude Code的工作流程。

- 🧠 **深入探索Claude Code**：学习从用户提示到Claude响应的内部机制，超越默认配置。
- 🛠️ **实践项目配置**：通过逐层配置演示项目，涵盖CLAUDE.md、权限、技能和自定义MCP服务器。
- 🗓️ **时间安排**：2026年4月21日（星期二）23:30至4月22日（星期三）06:30（日本标准时间）。
- 💻 **参与方式**：免费注册参加，通过提供的链接RSVP。
- 🌐 **主办方**：由Frontend Masters组织的独家工作坊，讲师来自Anthropic。

---

### [JavaScript 必知要点（2026版）—— Frontend Masters 博客](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/)

**原文标题**: [What To Know in JavaScript (2026 Edition) – Frontend Masters Blog](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/)

本文全面概述了2026年JavaScript生态系统的关键发展，涵盖语言新特性、框架、运行时、构建工具及行业趋势。

- 🆕 **ECMAScript 2025新特性**：包括迭代器助手（Iterator Helpers）、集合方法（Set Methods）、正则表达式更新（RegExp.escape()）、Promise.try()以及导入属性（Import Attributes），提升了语言表达力和性能。
- 📅 **ECMAScript 2026前瞻**：重点介绍Temporal API（日期时间处理）、显式资源管理（using关键字）、Array.fromAsync、Iterator.concat、Error.isError()以及Base64/Hex编码等新功能。
- ⚛️ **React生态进展**：React 19引入了服务器组件（RSC）、React编译器和服务器操作（Server Actions）；React Native宣布1.0版本计划。
- 🖖 **Vue与Svelte动态**：Vue 3.6测试版推出Vapor模式性能优化；Svelte 5采用Runes API实现细粒度响应式系统。
- 🏃 **JavaScript运行时**：Node.js原生支持TypeScript文件；Bun被Anthropic收购，注重开发体验与速度；Deno强调默认安全性设计。
- 🛠️ **构建工具演进**：Vite成为主流构建工具，推出Vite+工具链；Turbopack作为Next.js默认打包器；webpack计划简化配置。
- 📘 **TypeScript发展**：TypeScript v6为v7的Go编译器过渡做准备，v7预计带来10倍性能提升；TypeScript成为GitHub最受欢迎语言。
- 🤖 **AI与开发生态**：92%开发者使用AI辅助编码，AI尤其擅长生成TypeScript代码；测试工具中Vitest和Playwright增长显著。
- 🌐 **元框架格局**：Next.js v16默认集成Turbopack；Remix转向独立组件模型；Astro被Cloudflare收购，专注静态站点生成。
- ⚠️ **npm安全挑战**：npm供应链安全问题频发，建议采用Socket等工具加强防护；npm配置新增包年龄限制和脚本忽略选项。
- 🧠 **学习建议**：强调掌握JavaScript核心原理与架构能力的重要性，以应对技术变迁和AI辅助编程的普及。

---

### [事后分析：axios npm 供应链安全事件 · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636)

**原文标题**: [Post Mortem: axios npm supply chain compromise · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636)

2026年3月31日，axios的两个恶意版本（1.14.1和0.30.4）通过被入侵的维护者账户发布到npm，其中注入了包含远程访问木马的依赖包，恶意版本在约3小时后被移除。受影响用户需立即检查并采取补救措施，项目团队已启动全面安全加固。

- 🚨 **事件概述**：axios维护者账户遭入侵，导致两个恶意版本（1.14.1和0.30.4）被发布到npm，其中注入了携带远程访问木马的依赖包`plain-crypto-js@4.2.1`。
- ⏰ **影响时长**：恶意版本在npm上存活约3小时（UTC时间3月31日00:21至03:15），随后被移除。
- 🔍 **影响检测**：用户需检查项目锁文件中是否包含恶意版本或依赖，若受影响需立即降级至安全版本（如axios@1.14.0）并彻底清理。
- 💻 **攻击方式**：攻击者通过社会工程学攻击和远程访问木马（RAT）入侵维护者个人电脑，进而获取npm账户权限发布恶意包。
- 🛡️ **应对措施**：受影响机器需视为已入侵，立即旋转所有密钥凭证，检查网络日志中是否出现恶意域名或IP连接。
- 📈 **安全改进**：项目团队将实施设备重置、采用OIDC发布流程、建立不可变发布机制等多项安全预防措施。
- 🧩 **攻击时间线**：攻击始于3月30日恶意依赖包发布，3月31日恶意axios版本发布后迅速被社区发现并报告。
- 🙏 **致谢**：感谢社区成员和npm安全团队的快速响应，特别感谢@DigitalBrainJS在权限受限情况下及时采取行动。
- 📢 **现状更新**：恶意版本已从npm移除，直接威胁已解除，团队正在持续推进安全加固和事件调查。

---

### [事后分析：axios npm 供应链安全事件 · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636#issuecomment-4180237789)

**原文标题**: [Post Mortem: axios npm supply chain compromise · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636#issuecomment-4180237789)

2026年3月31日，axios项目因主要维护者账户被入侵，导致两个恶意版本（1.14.1和0.30.4）被发布到npm仓库，其中注入了远程访问木马。恶意版本在约3小时后被移除，项目团队已采取设备重置、凭证更新及多项安全改进措施以防止类似事件再次发生。

- 🔓 **账户入侵**：攻击者通过社会工程和RAT恶意软件入侵了主要维护者的个人电脑，获取了npm账户凭证。
- 📦 **恶意发布**：攻击者发布了axios的1.14.1和0.30.4版本，并注入了包含远程访问木马的`plain-crypto-js@4.2.1`依赖。
- ⏱️ **影响时长**：恶意版本在npm上存活了约3小时（从3月31日00:21至03:15 UTC）。
- 🛡️ **应对措施**：受影响用户需降级到安全版本、删除恶意依赖、旋转所有凭证，并检查网络连接。
- 🔄 **安全改进**：项目将重置所有设备与凭证、采用不可变发布设置、实施OIDC流程发布，并持续提升整体安全态势。
- 🧠 **经验教训**：开源维护者需警惕社会工程攻击，加强账户保护，并建立自动化的未授权发布检测机制。
- 🤝 **致谢**：感谢社区成员和npm安全团队的快速响应，恶意版本已被彻底移除。

---

### [JetStream 3 基准测试套件介绍 | WebKit](https://webkit.org/blog/17899/introducing-the-jetstream-3-benchmark-suite/)

**原文标题**: [  Introducing the JetStream 3 Benchmark Suite | WebKit](https://webkit.org/blog/17899/introducing-the-jetstream-3-benchmark-suite/)

JetStream 3.0 是 WebKit、Google 和 Mozilla 共同推出的跨浏览器基准测试套件重大更新，旨在更全面地衡量现代 Web 应用性能，特别是 WebAssembly 和 JavaScript 的执行效率。

- 🚀 **WebAssembly 评分方法革新**：弃用独立的启动/运行时评分，采用与 JavaScript 相同的多迭代生命周期评分，涵盖首次迭代、最差情况迭代和平均情况迭代，以优化完整执行流程。
- 📈 **摆脱微基准测试陷阱**：聚焦更大、更复杂的真实工作负载，减少对特定热函数的过度优化，促进引擎在 JIT 编译器和标准库功能上的全面效率提升。
- ⚙️ **WasmGC 性能优化**：通过内联分配、消除析构函数和改进类型检查，显著提升垃圾回收效率，针对 Dart、Java 和 Kotlin 等语言编译的 WasmGC 工作负载优化达 40%。
- 🔄 **改进的内联启发式方法**：采用全局优先级排序的非本地内联决策系统，优化代码大小预算分配，提升 WasmGC 工作负载中大量小函数的执行效率。
- 🧬 **多态间接调用内联**：通过基线编译器 BBQ 收集间接调用站点的分析数据，优化编译器 OMG 利用这些数据实现守卫和直接内联，将不可预测的间接调用转化为可预测的直接调用。
- 🗃️ **抽象堆与类型别名分析**：引入抽象堆概念，使编译器能够基于类型更精确地推理 Wasm 指令的副作用，消除冗余的加载和存储操作，提升内存访问效率。
- 💾 **寄存器分配器改进**：采用贪婪寄存器分配算法替代原有的图着色和线性扫描算法，提升编译速度和代码质量，支持更大的函数优化和实时编译。
- 🖥️ **IPInt 支持 SIMD**：在 WebAssembly 解释器 IPInt 中实现完整的 SIMD 指令支持，使 SIMD 代码能够近乎即时启动执行，提升安全环境下的性能。
- 🔢 **BigInt 算法与内存优化**：实现 Comba 乘法算法和 DIV2BY1 除法技术，改进内存布局以减少分配和指针间接访问，提升大整数运算性能。
- ⚡ **微任务队列与异步函数优化**：重写微任务队列实现，将 Promise 内置函数迁移到 C++，优化 async/await 的恢复机制，减少微任务调度开销，提升异步代码执行效率。

---

### [介绍EmDash——WordPress的精神继承者，解决插件安全难题](https://blog.cloudflare.com/emdash-wordpress/)

**原文标题**: [Introducing EmDash â the spiritual successor to WordPress that solves plugin security](https://blog.cloudflare.com/emdash-wordpress/)

EmDash是WordPress的精神继承者，旨在解决插件安全等核心问题，采用TypeScript编写，支持无服务器架构，并内置AI时代的内容付费功能。

- 🛡️ 插件安全：通过沙盒隔离和权限声明，解决WordPress插件安全漏洞问题
- 🔓 开源许可：采用MIT许可证，允许开发者自由扩展和参与开发
- 💰 内置支付：集成x402标准，支持按需付费访问内容
- 🚀 无服务器架构：基于Cloudflare Workers，实现零成本扩展和高性能
- 🎨 现代主题：使用Astro框架，让前端开发更熟悉和安全
- 🤖 AI原生支持：提供CLI、MCP服务器和Agent Skills，方便AI代理管理
- 🔑 认证方式：默认使用Passkey认证，支持SSO集成
- 📥 迁移工具：支持从WordPress导入内容和媒体库

---

### [Svelte 四月 2026 更新亮点](https://svelte.dev/blog/whats-new-in-svelte-april-2026)

**原文标题**: [What’s new in Svelte: April 2026](https://svelte.dev/blog/whats-new-in-svelte-april-2026)

Svelte 在 2026 年 4 月发布了多项更新，包括 MCP 配置优化、svelte.config.js 支持函数设置选项、新增运动类型导出、服务器端错误边界支持，以及参数类型安全增强。社区还展示了多个基于 Svelte 构建的应用和工具。

- 📚 新增 Svelte 最佳实践指南文档
- 🔧 MCP 配置现位于 `.opencode/` 文件夹，简化 OpenCode 使用
- ⚙️ `svelte.config.js` 支持函数设置选项，统一配置管理
- 📦 `svelte/motion` 导出 `TweenOptions` 等运动类型，提升类型支持
- 🛡️ SvelteKit 支持服务器端错误边界，增强错误处理能力
- 🔍 页面和布局参数类型更安全，提升开发体验
- 🌐 社区展示多个 Svelte 应用，如 Ghostty 配置生成器和 Orbit PDF 工具包
- 🛠️ 新增多个工具和库，如 `svelte-realtime` 和 `Motion GPU` 着色器工具

---

### [ESLint v10.2.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/04/eslint-v10.2.0-released/)

**原文标题**: [ESLint v10.2.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/04/eslint-v10.2.0-released/)

ESLint v10.2.0 作为一次小版本更新，引入了语言感知规则支持和 Temporal 全局对象识别等新功能，同时修复了若干错误并更新了文档。

- 🆕 新增 `meta.languages` 属性，允许规则作者明确声明规则支持的语言，若在未支持的语言中启用规则将报错
- 🌐 识别 Temporal 为内置全局对象，`no-undef` 规则默认不再标记它，而 `no-obj-calls` 规则会报告对 Temporal 的直接调用错误
- 🐛 包含多个错误修复，例如更新了首方依赖项
- 📚 文档进行了多项更新，包括添加语言配置说明和更新示例中的 ESLint 版本
- 🔧 进行了一些内部重构、测试添加和依赖项更新等维护工作

---

