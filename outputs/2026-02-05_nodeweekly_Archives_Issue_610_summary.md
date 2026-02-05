### [Node 周刊第 610 期：2026 年 2 月 5 日](https://nodeweekly.com/issues/610)

**原文标题**: [Node Weekly Issue 610: February 5, 2026](https://nodeweekly.com/issues/610)

本期 Node.js 周刊涵盖了多个重要更新与工具发布，包括 JavaScript 后端框架调查结果、Node.js 25.6.0 版本特性、安全漏洞修复、开发工具改进以及生态系统动态。

- 📊 **JavaScript 后端框架调查**：Express 仍占主导，NestJS 增长迅速，Hono 在开发者满意度中领先。
- 🔧 **Node.js 25.6.0 发布**：引入 async_hooks 的 Promise 跟踪可选功能以降低性能开销，测试运行器支持环境变量注入，TextEncoder 性能优化，URL 解析器更新至 Unicode 17。
- 🛡️ **安全漏洞修复**：vm2 沙箱发现严重漏洞，需立即升级至 v3.10.4 版本。
- 🛠️ **开发工具更新**：Vercel 新增 Koa 应用零配置部署支持；推荐从 Chalk 迁移至 Node 内置 styleText 进行终端样式处理；引入 Explicit Resource Management，使用`using`关键字实现资源自动清理。
- 📉 **JSBin 宕机事件分析**：因流量激增导致服务中断，老旧 Node 7 运行时加剧了问题。
- 💻 **ARM64 Windows 开发指南**：提供在 ARM64 Windows 上构建 Node.js 的注意事项。
- 📦 **新工具与库发布**：包括 Croner 10.0（定时任务触发）、OTPAuth（一次性密码库）、log-update 7.1（终端输出覆写）、Nanoclaw（轻量级 Claude 助手）、simple-ffmpegjs（简化 FFmpeg 操作）等。
- 🌐 **生态系统动态**：Deno Deploy 正式可用并支持 Node 项目；传闻 Node 18 可在 iPhone 上运行；Amazon EC2 推出大存储实例应对庞大 node_modules。

---

### [JavaScript 2025 现状：后端框架](https://2025.stateofjs.com/en-US/libraries/back-end-frameworks/)

**原文标题**: [State of JavaScript 2025: Back-end Frameworks](https://2025.stateofjs.com/en-US/libraries/back-end-frameworks/)

JavaScript 后端框架现状：Express 仍占主导，但新兴框架在满意度方面表现突出，尤其是 Hono、Nitro 和 ElysiaJS。开发者对类型安全和现代化替代方案的需求日益增长。

- 🏆 Express 在用户使用率上保持领先，但新兴框架如 Next.js 正快速崛起
- 😊 满意度前三名均为新框架：Hono、Nitro 和 ElysiaJS，显示生态活力
- 🔢 开发者平均仅使用 1.9 个后端框架，选择后很少更换
- 🚨 Express 已发布 15 年，缺乏类型安全支持成为主要痛点
- 📊 静态类型、浏览器支持和性能是开发者最关注的改进方向
- 🌟 社区推荐 Atproto 开发生态，其 TypeScript SDK 受关注
- 📚 推荐学习资源包括 Node.js API 设计和后端系统设计课程

---

### [Express - Node.js Web 应用程序框架](https://expressjs.com/)

**原文标题**: [Express - Node.js web application framework](https://expressjs.com/)

Express 是一个快速、极简且灵活的 Node.js Web 应用框架，适用于构建 Web 和移动应用，提供强大的 API 开发支持与高性能表现，其核心功能可通过中间件模块灵活扩展。

- 🚀 **快速极简**：Express 是一个快速、无预设且极简的 Node.js Web 框架。
- 📦 **安装简便**：可通过 npm 轻松安装，并支持保存到项目依赖中。
- 🌐 **基础示例**：创建一个简单的服务器，监听端口并响应“Hello World!”。
- 🔄 **版本更新**：Express 5.1.0 已成为 npm 默认版本，并引入了 v4 和 v5 的官方长期支持计划。
- 🛠️ **应用构建**：提供灵活强大的功能集，适用于 Web 和移动应用开发。
- 🔗 **API 开发**：借助丰富的 HTTP 工具方法和中间件，可快速构建健壮的 API。
- ⚡ **高性能**：在保留 Node.js 核心特性的基础上，提供基础的 Web 应用功能层。
- 🔌 **中间件支持**：核心轻量且灵活，可通过中间件模块扩展功能。

---

### [NestJS - 一个渐进的 Node.js 框架](https://nestjs.com/)

**原文标题**: [NestJS - A progressive Node.js framework](https://nestjs.com/)

NestJS 是一个用于构建高效、可靠和可扩展服务器端应用程序的渐进式 Node.js 框架，提供模块化架构、依赖注入、类型安全等特性，并拥有丰富的生态系统和企业级支持。

- 🏗️ 模块化架构：通过自包含模块组织应用，提升可维护性
- 📈 可扩展性：使用经过实战检验的高效组件无缝扩展应用
- 💉 依赖注入：通过精密的依赖注入系统提高可测试性
- 🛡️ 类型安全：利用 TypeScript 的强类型特性减少错误
- 🌐 丰富生态：提供多样化工具，满足定制化开发需求
- 🏢 企业级支持：被全球数千家领先公司和组织信任使用
- 🔗 微服务支持：创建松耦合、独立部署的服务，提升敏捷性
- 🚀 快速开发：轻松构建 REST API、GraphQL API、队列及实时应用
- ☁️ 云端部署：通过 Mau 在 AWS 上无忧管理和部署基础设施
- 📚 官方课程：提供全面课程，帮助掌握 NestJS 及现代后端开发
- 💖 开源支持：MIT 许可的开源项目，依靠社区赞助和贡献持续发展

---

### [Hono - 基于 Web 标准的 Web 框架](https://hono.dev/)

**原文标题**: [Hono - Web framework built on Web Standards](https://hono.dev/)

Hono 框架以其超快速度和轻量级设计脱颖而出，提供高性能的 RegExpRouter 和小于 14kB 的 hono/tiny 预设，完全基于 Web 标准 API 构建。

- ⚡ RegExpRouter 实现极速路由匹配
- 📦 hono/tiny预设体积小于14kB
- 🌐 完全采用 Web 标准 API 开发

---

### [Node.js — Node.js 25.6.0（当前版本）](https://nodejs.org/en/blog/release/v25.6.0)

**原文标题**: [Node.js — Node.js 25.6.0 (Current)](https://nodejs.org/en/blog/release/v25.6.0)

Node.js 25.6.0 版本发布，包含多项新功能、性能优化和错误修复，主要更新涉及异步钩子、网络模块、ESM 支持、流处理和测试工具等方面。

- 🚀 **异步钩子增强**：为 `createHook()` 新增 `trackPromises` 选项，便于追踪 Promise 生命周期。
- 🌐 **网络功能扩展**：在 `Socket` 中添加 `setTOS` 和 `getTOS` 方法，支持设置和获取服务类型。
- 📦 **ESM 嵌入支持**：为嵌入 API 提供初步的 ESM 支持，提升模块化兼容性。
- ⚡ **性能优化**：利用 `simdutf` 改进 `TextEncoder` 的编码性能，并优化 `TextDecoder` 的 UTF-8 处理。
- 🔄 **流处理新增**：在 `node:stream/consumers` 中引入 `bytes()` 方法，方便处理字节数据。
- 🧪 **测试工具升级**：为 `test_runner` 的 `run` 函数添加 `env` 选项，增强测试环境配置能力。
- 🔗 **依赖项更新**：升级 Ada URL 解析器至 v3.4.2，支持 Unicode 17，并更新 OpenSSL、Undici 等核心依赖。
- 🐛 **错误修复与改进**：修复数组深度比较、缓冲区传输限制、文档对齐等多个问题，提升稳定性和兼容性。

---

### [async_hooks: 为 createHook() 添加 trackPromises 选项 by joyeecheung · Pull Request #61415 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61415)

**原文标题**: [async_hooks: add trackPromises option to createHook() by joyeecheung · Pull Request #61415 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61415)

Node.js 的 async_hooks 模块新增了 `trackPromises` 选项，允许用户在使用 `createHook()` 时完全禁用对 Promise 的跟踪，从而避免不必要的钩子调用和性能开销。

- 🚀 **新增选项**：`createHook()` 新增 `trackPromises` 选项，允许用户选择不跟踪 Promise 的执行。
- ⚡ **性能优化**：对于不需要跟踪 Promise 的场景，可以避免大量钩子调用，显著减少性能开销。
- 🔧 **内部实现公开**：该选项原本已用于 V8 调试器内部，现正式对外暴露。
- 📦 **版本发布**：此功能作为次要版本更新（SEMVER-MINOR）包含在 Node.js v25.6.0 中。
- ✅ **测试覆盖**：相关修改已通过测试，代码覆盖率保持稳定。

---

### [测试运行器 | Node.js v25.6.0 文档](https://nodejs.org/api/test.html#runoptions)

**原文标题**: [Test runner | Node.js v25.6.0 Documentation](https://nodejs.org/api/test.html#runoptions)

Node.js v25.6.0 文档中的测试运行器模块（node:test）是一个用于创建和管理 JavaScript 测试的稳定工具。它支持同步、异步和基于回调的测试，提供子测试、跳过测试、待办测试、模拟功能、快照测试、代码覆盖率收集等多种高级特性，并可通过命令行或编程方式灵活配置和运行测试。

- 🧪 **测试类型与执行**：支持同步、异步（Promise）和回调函数三种测试方式，测试失败时进程退出码为 1。
- 🌳 **子测试与层级结构**：通过 `test()` 方法创建嵌套子测试，支持 `beforeEach` 和 `afterEach` 钩子在子测试间运行。
- ⏭️ **跳过与待办测试**：可使用 `skip` 选项或 `skip()` 方法跳过测试，使用 `todo` 选项标记待办测试（执行但不视为失败）。
- 🔄 **重跑失败测试**：通过 `--test-rerun-failures` 标志将运行状态持久化到文件，仅重新运行之前失败的测试。
- 🔧 **模拟功能**：提供 `MockTracker` 和 `MockTimers` 等类，用于模拟函数、模块、属性和定时器，便于测试依赖项。
- ⏱️ **定时器与日期模拟**：可模拟 `setTimeout`、`setInterval` 和 `Date` 对象，控制时间流逝以测试时间相关逻辑。
- 📸 **快照测试**：将任意值序列化为字符串并与快照文件比较，支持通过 `--test-update-snapshots` 更新快照。
- 📊 **代码覆盖率**：通过 `--experimental-test-coverage` 标志收集覆盖率，支持排除/包含文件，并生成报告（如 lcov）。
- 👀 **监视模式**：使用 `--watch` 标志在文件变化时自动重新运行受影响的测试。
- 🌍 **全局设置与清理**：通过 `--test-global-setup` 指定模块，在测试前后执行全局初始化和清理逻辑。
- 🏃 **命令行运行**：通过 `--test` 标志运行测试，支持 glob 模式匹配测试文件，可配置并发度和隔离模式。
- 📈 **测试报告器**：内置多种报告器（spec、tap、dot、junit、lcov），支持自定义报告器和多报告器输出。
- ⚙️ **丰富配置选项**：提供 `run()` 函数和多种测试/套件方法（如 `test()`、`describe()`），支持超时、并发、过滤等详细配置。

---

### [实用工具 | Node.js v25.6.0 文档](https://nodejs.org/api/util.html#class-utiltextencoder)

**原文标题**: [Util | Node.js v25.6.0 Documentation](https://nodejs.org/api/util.html#class-utiltextencoder)

本文档是 Node.js v25.6.0 版本中`util`模块的详细 API 参考，该模块为 Node.js 内部 API 提供支持，同时也为应用程序和模块开发者提供多种实用工具。

- 📦 **模块导入**：可通过`import util from 'node:util'`或`const util = require('node:util')`访问。
- 🔄 **异步转换**：`util.callbackify()`将返回 Promise 的异步函数转换为错误优先的回调风格函数。
- 🚦 **调试日志**：`util.debuglog()`根据`NODE_DEBUG`环境变量条件性地输出调试信息到`stderr`。
- ⚠️ **弃用警告**：`util.deprecate()`包装函数或类，标记为已弃用，调用时发出警告。
- 🔍 **对象检查**：`util.inspect()`返回对象的字符串表示，用于调试，支持颜色、深度、排序等多种选项。
- 📊 **格式化输出**：`util.format()`使用类似`printf`的格式字符串格式化输出，支持多种类型说明符。
- 🔧 **类型检查**：`util.types`提供一系列类型检查方法，用于判断值是否为特定内置对象类型。
- 📨 **命令行解析**：`util.parseArgs()`提供高级 API 解析命令行参数，返回结构化对象。
- 🔄 **Promise 转换**：`util.promisify()`将错误优先的回调风格函数转换为返回 Promise 的函数。
- 🌐 **编码处理**：`util.TextDecoder`和`util.TextEncoder`类分别用于解码和编码文本，支持多种编码。
- 🛠️ **其他工具**：包括`util.diff()`比较差异、`util.getSystemErrorName()`获取系统错误名称、`util.MIMEType`处理 MIME 类型等。

---

### [通过使用 simdutf 提升 textEncoder 编码性能，由 mertcanaltin 提交的拉取请求 #61496 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61496)

**原文标题**: [src: improve textEncoder encode performance with simdutf by mertcanaltin · Pull Request #61496 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61496)

Node.js 项目通过集成 SIMDUTF 库显著提升了 TextEncoder.encode() 方法的性能，该优化已合并至主分支并包含在版本 25.6.0 中。

- 🚀 **性能大幅提升**：针对不同字符串类型和长度，encode 操作性能提升显著，部分场景性能提升近 300%。
- 📊 **基准测试验证**：通过详细的基准测试数据确认了性能改进，覆盖了 ASCII、单字节和双字节字符串等多种情况。
- 🔧 **代码变更聚焦**：主要修改集中在 `src/encoding_binding.cc` 文件，以集成 SIMDUTF 优化。
- ✅ **审查与合并流程**：经过代码审查、CI 测试，并被标记为“显著变更”，最终成功合并至主分支。
- 📈 **版本发布包含**：此优化作为一项重要改进，被列入 Node.js v25.6.0 版本的发布说明中。

---

### [AI 代理文员技能](https://clerk.com/changelog/2026-01-29-clerk-skills?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=skills&utm_content=02-05-26&dub_id=Mfmj6P9fUgCDNcTr)

**原文标题**: [Clerk Skills for AI Agents](https://clerk.com/changelog/2026-01-29-clerk-skills?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=skills&utm_content=02-05-26&dub_id=Mfmj6P9fUgCDNcTr)

Clerk 推出可安装技能包，使 AI 编程助手获得专业的 Clerk 身份验证知识，帮助开发者快速集成认证功能。

- 🔧 发布 Clerk Skills 技能包，基于 Agent Skills 规范，为 AI 编程助手提供专业身份验证知识
- 🚀 通过单一命令安装所有技能：`npx skills add clerk/skills`
- 💡 安装后 AI 助手可协助实现多种功能：添加框架认证、构建自定义登录流程、同步用户数据等
- 🌐 支持主流 AI 编程助手：Claude Code、Cursor、Windsurf、GitHub Copilot 等
- 📚 详细技能列表和安装选项可查阅官方技能文档

---

### [Node.js v24.13.0 文档](https://nodejs-api-docs-tooling.vercel.app/)

**原文标题**: [| Node.js v24.13.0 Documentation](https://nodejs-api-docs-tooling.vercel.app/)

Node.js 文档涵盖了从核心模块到高级功能的全面内容，包括异步编程、系统交互、网络通信及安全等关键领域。

- 📚 **版本与介绍** - 自 v0.10.0 引入，包含文档使用指南和示例
- 🔧 **核心功能** - 涵盖断言测试、异步上下文跟踪、Buffer 处理和事件系统
- 🔌 **扩展与集成** - 支持 C++ 插件、Node-API 嵌入和进程管理
- 🌐 **网络与通信** - 提供 HTTP/HTTPS、TCP/UDP、DNS 和 TLS/SSL 模块
- 📁 **文件与系统** - 包含文件系统操作、路径处理、环境变量和操作系统交互
- 🛠️ **开发工具** - 集成调试器、测试运行器、性能钩子和诊断通道
- 🔐 **安全与加密** - 内置 Crypto 模块、Web Crypto API 和权限管理
- 🌍 **国际化与模块** - 支持 ES/CommonJS 模块、TypeScript 和国际化功能
- ⚙️ **高级特性** - 包含 Worker 线程、Web Streams、SQLite 和单可执行应用
- 🔄 **实用工具** - 提供查询字符串、实用函数、V8 引擎和代码仓库管理

---

### [GitHub · 软件构建之地](https://github.com/nodejs/doc-kit/issues)

**原文标题**: [GitHub · Where software is built](https://github.com/nodejs/doc-kit/issues)

该文档概述了 Node.js 文档工具项目（doc-kit）的当前状态，包括项目的基本信息和一系列待解决或进行中的议题，主要聚焦于功能改进、代码重构和自动化流程。

- 📚 **项目概览**：Node.js 的文档工具项目（doc-kit），包含代码、议题和协作功能。
- 🎯 **长期目标**：实现 API 文档工具的通用化，以提升其适应性和可维护性。
- 🔧 **功能开发**：多项功能议题待处理，如自动化 npm 发布、交互式 JavaScript 与 Markdown 解析等。
- 🛠️ **重构任务**：包括参数表格改造、移除 MetaBar 等代码优化工作。
- 🧪 **测试与质量**：强调端到端测试和元数据生成器测试，确保项目稳定性。
- 🆕 **新功能提案**：如添加状态提示、支持双斜杠客户端渲染等用户体验改进。
- 🔄 **模块化与生成**：计划按类或章节拆分模块文件，优化文档生成流程。
- 🤝 **社区反馈**：整合来自贡献者的建议，持续改进工具设计。
- 📦 **发布与消费**：关注 npm 发布自动化和 TypeScript 声明文件的使用便利性。

---

### [@philippeserhal.com 在 Bluesky 上](https://bsky.app/profile/philippeserhal.com/post/3mdyrfhxwbk2b)

**原文标题**: [@philippeserhal.com on Bluesky](https://bsky.app/profile/philippeserhal.com/post/3mdyrfhxwbk2b)

这是一个关于在 Bluesky 社交平台上分享发现最长 NPM 包名称的帖子。

- 🌐 帖子发布在需要 JavaScript 的交互式 Bluesky 平台上
- 🔍 用户为了测试而寻找最长的 NPM 包名称
- 📦 发现并展示了这个特殊的 NPM 包
- 🙏 感谢 14 年前创建此包的匿名开发者
- 🏷️ 通过@npmx.dev 账号向原开发者致敬
- ⏰ 发布于 2026 年 2 月 4 日

---

### [GitHub - patriksimek/vm2：Node.js 的高级虚拟机/沙箱](https://github.com/patriksimek/vm2)

**原文标题**: [GitHub - patriksimek/vm2: Advanced vm/sandbox for Node.js](https://github.com/patriksimek/vm2)

vm2 是一个用于 Node.js 的高级沙箱，旨在安全地运行不受信任的代码，通过代理机制隔离代码执行环境，但需注意其安全限制和潜在风险。

- 🛡️ **安全沙箱**：在同一个 Node.js 进程中运行不受信任的代码，使用代理拦截和中介所有交互。
- ⚠️ **安全警告**：由于 JavaScript 的动态性，沙箱可能存在逃逸漏洞，需保持更新并参考安全公告。
- 🔄 **替代方案**：对于更高隔离需求，建议使用独立进程、容器或云服务等方案。
- 🛠️ **功能特性**：支持控制控制台输出、限制模块访问、安全调用方法和数据交换。
- 📦 **安装使用**：通过 npm 安装，提供 VM 和 NodeVM 两种模式，分别用于简单代码运行和模块加载。
- ⚙️ **配置选项**：包括超时设置、沙箱全局对象、编译器选择、异步控制等。
- 🐛 **调试与错误处理**：支持断点和调试器关键字，可通过 try-catch 和事件处理错误。
- 🔒 **实验性功能**：提供只读对象和受保护对象机制，增强沙箱安全性。
- 📄 **文档与贡献**：详细文档和贡献指南，项目采用 MIT 许可证，社区活跃。

---

### [新型沙箱逃逸漏洞影响热门 Node.js 沙箱库 vm2 | Semgrep](https://semgrep.dev/blog/2026/calling-back-to-vm2-and-escaping-sandbox/)

**原文标题**: [New Sandbox Escape Affecting Popular nodejs Sandbox library vm2 | Semgrep](https://semgrep.dev/blog/2026/calling-back-to-vm2-and-escaping-sandbox/)

vm2 库曝出严重漏洞，攻击者可绕过 Promise 沙箱隔离执行任意代码，需立即升级至 3.10.2 版本。

- 🚨 vm2 库存在严重漏洞（CVSS 9.8），攻击者能绕过 Promise 沙箱隔离机制执行任意代码
- ⚠️ 漏洞利用代码已公开，所有使用 3.10.1 及更早版本的应用均受影响
- 🔄 建议立即升级至 3.10.2 版本，Semgrep 用户可通过工具检测依赖
- 🛡️ 运行不可信代码时应考虑更安全的替代方案，如 isolated-vm 或容器化隔离
- 📉 这是 vm2 一年内第八次安全通告，其架构依赖 Node 代理存在根本性缺陷
- 🔍 漏洞原理：全局 Promise 异常处理程序可绕过本地作用域的安全检查
- 💡 开发者应优先采用进程级隔离而非依赖代码净化处理不可信代码

---

### [发布 v3.10.4 · patriksimek/vm2 · GitHub](https://github.com/patriksimek/vm2/releases/tag/v3.10.4)

**原文标题**: [Release v3.10.4 · patriksimek/vm2 · GitHub](https://github.com/patriksimek/vm2/releases/tag/v3.10.4)

该项目发布了 vm2 库的 3.10.4 版本，主要修复了多个可能导致沙箱逃逸的安全漏洞。

- 🔒 修复了通过 Promise 静态方法窃取导致的沙箱逃逸漏洞
- 🛡️ 修复了通过 Reflect.construct 绕过 Promise 物种限制的沙箱逃逸漏洞
- 🚫 修复了通过 util.inspect 暴露代理处理程序导致的沙箱逃逸漏洞
- 📋 修复了通过 util.inspect 暴露 fromOtherWithContext 导致的沙箱逃逸漏洞

---

### [Koa 框架的零配置支持 - Vercel](https://vercel.com/changelog/zero-configuration-support-for-koa)

**原文标题**: [Zero-configuration support for Koa - Vercel](https://vercel.com/changelog/zero-configuration-support-for-koa)

Vercel 现已支持 Koa 框架，使开发者能够零配置部署 Koa 应用，并默认采用动态计算资源与按使用量计费模式。

- 🚀 Vercel 正式支持 Koa 框架，可零配置部署 Web 应用与 API
- ⚙️ 提供 Koa 示例代码，展示基础路由与响应设置
- 📈 默认启用动态计算资源，根据流量自动伸缩应用规模
- 💰 采用按实际使用量计费模式，优化运行成本
- 📚 官方文档已更新，提供详细部署指南

---

### [Node.js — 将 Chalk 转换为 Node.js util styleText](https://nodejs.org/en/blog/migrations/chalk-to-styletext)

**原文标题**: [Node.js — Chalk to Node.js util styleText](https://nodejs.org/en/blog/migrations/chalk-to-styletext)

该代码修改工具旨在帮助开发者将项目中的 Chalk 方法调用转换为使用 Node.js 原生的 util.styleText 样式功能，从而减少外部依赖，并自动从 package.json 中移除 chalk 包。

- 🎨 **支持转换的功能**：包括基础颜色、高亮颜色、背景色、文本修饰符（如粗体、斜体）、数组链式调用，以及环境变量支持（如 NO_COLOR）。
- 🚫 **不兼容的功能**：自定义 RGB 颜色、256 色板、模板字符串语法及部分高级修饰符（如闪烁效果）无法迁移。
- ⚙️ **前提条件**：需使用 Node.js v20.12.0 或更高版本（v22.13.0 后功能稳定），若项目支持更早版本，迁移需升级 Node.js 并更新 package.json 中的引擎版本。
- 📦 **使用方法**：通过 npx 执行`@nodejs/chalk-to-util-styletext`命令，工具将自动转换代码示例中的 Chalk 调用为 util.styleText 格式。
- 🙏 **致谢**：感谢 Chalk 维护者长期对生态系统的贡献，工具旨在推动向原生功能的平稳过渡。

---

### [GitHub - chalk/chalk: 🖍 终端字符串样式处理得恰到好处](https://github.com/chalk/chalk)

**原文标题**: [GitHub - chalk/chalk: 🖍 Terminal string styling done right](https://github.com/chalk/chalk)

Chalk 是一个用于终端字符串样式化的 JavaScript 库，提供简洁的 API 来为命令行输出添加颜色和样式，支持嵌套样式、自动检测颜色支持，并且无依赖。

- 🎨 **功能丰富**：支持多种颜色（包括 256 色和真彩色）、样式修饰（如粗体、下划线）和背景色，API 灵活可组合。
- ⚡ **高性能**：经过优化，处理速度快，且不扩展 `String.prototype`，保持代码纯净。
- 📦 **无依赖**：库本身不依赖其他包，轻量且易于集成。
- 🌈 **自动检测**：能自动检测终端颜色支持级别，并可手动覆盖设置。
- 🔧 **广泛使用**：被约 115,000 个包使用，社区活跃且维护良好。
- 📚 **详细文档**：提供完整的 API 说明、使用示例和常见问题解答，便于开发者上手。
- 🖥️ **跨平台**：支持现代终端，包括浏览器开发者工具和 Windows Terminal，推荐替代 cmd.exe。
- 🔗 **相关生态**：拥有多个相关工具包，如模板支持、CLI 工具和颜色转换库，扩展功能丰富。

---

### [JavaScript 中的显式资源管理 - Matt Smith](https://allthingssmitty.com/2026/02/02/explicit-resource-management-in-javascript/)

**原文标题**: [
    Explicit resource management in JavaScript - Matt Smith
  ](https://allthingssmitty.com/2026/02/02/explicit-resource-management-in-javascript/)

JavaScript 显式资源管理提供了一种语言级别的机制，确保资源（如文件、锁、数据库连接）在使用后自动清理，从而减少手动管理带来的错误和复杂性。

- 🧹 传统清理方式依赖 `try/finally`，代码冗长且容易出错，尤其在处理多个资源时顺序和错误处理变得复杂。
- 🔧 `using` 和 `await using` 声明将资源清理与作用域生命周期绑定，无需手动编写清理代码，由运行时自动处理。
- 🔗 资源通过实现 `Symbol.dispose` 或 `Symbol.asyncDispose` 来支持自动清理，使 API 设计标准化。
- 📚 多个资源可以堆叠使用，清理按声明顺序反向自动执行，简化了错误处理和资源管理。
- 🧱 资源作用域与变量作用域一致，鼓励更精细的作用域设计，使资源生命周期在代码中更明确。
- 🛠️ 对于不符合块级作用域的资源，`DisposableStack` 和 `AsyncDisposableStack` 提供了灵活的清理机制。
- 🌐 该特性不仅适用于后端，在前端（如 Web Streams、IndexedDB）和平台代码中同样有用，能提升代码可读性和可靠性。
- ⏳ 截至 2026 年初，Chrome、Firefox 和 Node.js 已支持该特性，Safari 支持仍在规划中，适合库和平台抽象层先行采用。

---

### [JS Bin 将于 2026 年下线](https://remysharp.com/2026/02/02/js-bin-down-in-2026)

**原文标题**: [JS Bin down in 2026](https://remysharp.com/2026/02/02/js-bin-down-in-2026)

JS Bin 在 2026 年 1 月底经历了一次严重宕机，作者通过升级 Node.js 版本、调整 nginx 配置、引入 CloudFlare 防护以及修复 TLS 协议不匹配等问题，最终恢复了服务。此次事件暴露了长期维护模式下基础设施的老化问题，以及过度依赖 AI 工具在危机处理中可能带来的配置混乱。

- 🚨 **突发宕机**：JS Bin 在 2026 年 1 月 27 日突然无法访问，持续数天，服务器重启后仍立即崩溃。
- 📈 **流量激增**：监控显示入站网络流量异常飙升，峰值达 100MB，导致服务器资源耗尽。
- 💻 **老旧系统**：服务器运行在 Node.js 7 等过时软件上，基础设施已维护多年未升级。
- 🤖 **AI 辅助调试**：作者使用 ChatGPT 等 AI 工具协助优化 nginx 配置，但 AI 误读终端信息导致建议混乱。
- 🛡️ **引入 CloudFlare**：为缓解流量压力，将 DNS 迁移至 CloudFlare，但初期配置错误导致 520 错误频发。
- 🔧 **配置纠错**：错误 nginx 规则（如 IP 检测逻辑冲突）阻塞了合法用户访问，经调整后逐步恢复。
- 🔐 **TLS 协议冲突**：CloudFlare 默认请求 TLSv1.3，而服务器仅支持 TLSv1.2，禁用 v1.3 后解决 520 错误。
- 📉 **流量来源**：异常流量疑似来自 AI 爬虫，尤其香港地区在 24 小时内产生千万级请求。
- ✅ **恢复稳定**：最终通过防火墙规则、CloudFlare 缓存及配置清理，服务器负载降至正常水平（CPU 使用率约 4.6%）。

---

### [JS Bin - 协作式 JavaScript 调试工具](https://jsbin.com/)

**原文标题**: [JS Bin - Collaborative JavaScript Debugging](https://jsbin.com/)

JS Bin 是一个在线代码编辑和实时预览工具，支持多种编程语言和处理器，提供丰富的编辑功能和分享选项。

- 🛠️ **功能丰富**：支持 HTML、CSS、JavaScript 等多种语言，并集成了如 Markdown、Sass、TypeScript 等处理器。
- 🔗 **分享便捷**：可通过链接、嵌入代码或导出为 Gist 等方式轻松分享代码片段。
- ⌨️ **快捷键高效**：提供多种键盘快捷键，如切换面板、运行代码、美化代码等，提升编辑效率。
- 🔄 **实时协作**：支持实时重新加载输出、代码广播（Code Casting）和多人观看最新版本。
- 📂 **项目管理**：支持创建、保存、克隆、归档和删除代码项目，并可设置为私有或模板。
- 🌐 **URL 灵活**：通过特定 URL 后缀（如 `/edit`、`/latest`、`.js`）可快速访问不同视图或资源。
- 👥 **用户集成**：支持通过 GitHub 登录，管理个人代码库和查看最后编辑的项目。
- 💡 **辅助工具**：内置控制台、库添加功能和帮助文档，方便调试和学习。

---

### [在 ARM64 Windows 上调整 Node.js 核心 | Joyee Cheung 的博客](https://joyeecheung.github.io/blog/2026/01/31/tinkering-with-nodejs-core-on-arm64-windows/)

**原文标题**: [Tickering with Node.js Core on ARM64 Windows | Joyee Cheung's Blog](https://joyeecheung.github.io/blog/2026/01/31/tinkering-with-nodejs-core-on-arm64-windows/)

本文分享了在 ARM64 架构的 Windows 系统上构建和调试 Node.js 核心代码的经验与技巧，包括工具链安装、构建流程优化以及调试方法。

- 🛠️ 在 ARM64 Windows 上安装 Node.js 构建工具链时，需注意选择正确的 Visual Studio 组件（如 Clang 编译器），并确保安装 ARM64 版本的 Python，避免因使用 x64 版本导致交叉编译问题。
- ⏭️ 为提升效率，可跳过某些非必要的工具安装，如在 ARM64 上无需安装 NetWide Assembler（仅支持 x64）和 ccache（尚不支持 ARM64 Windows）。
- 🖥️ 建议启用 Windows 开发者模式，以避免测试中因权限问题导致符号链接创建失败，同时使用 Visual Studio 的开发者命令提示符来便捷访问 MSBuild 等工具。
- 🏗️ 生成解决方案时，可通过`vcbuild.bat`显式指定 ARM64 架构，并分离生成与构建步骤，以便更灵活地控制流程和调试项目配置。
- 🔨 使用 MSBuild 直接构建可更精细地控制目标（如仅构建 node.exe 或特定测试），通过参数调整可跳过不必要的依赖检查，缩短等待时间。
- 🧪 运行测试时，`vcbuild.bat`仍较为便捷，支持单独构建 Node-API 测试或运行 JavaScript 测试而无需重新编译。
- 🐛 在 Visual Studio 中调试 Node.js 时，可设置启动项目为 node，配置调试参数，并利用其丰富的调试功能（如快捷键 F5）提升效率。

---

### [TimescaleDB：排名第一的 PostgreSQL 时序数据库 | 开源与云端 | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB: #1 PostgreSQL Time-Series Database | Open Source & Cloud | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是一款基于 PostgreSQL 构建的时序数据库，专为处理传感器、链上及客户数据而设计，提供实时分析、高效压缩和自动分区等功能。它兼具 PostgreSQL 的兼容性与时序数据处理的性能，支持云托管和自托管部署，广泛应用于物联网、金融科技和实时分析等领域。

- 🚀 **高性能时序处理**：通过自动分区（Hypertables）、行列混合存储及高达 95% 的压缩率，实现海量数据的快速写入与查询。
- 🔄 **实时分析能力**：支持增量物化视图（Continuous Aggregates）和时序专用函数，提供即时数据汇总与高级分析功能。
- ☁️ **云托管优势**：Tiger Cloud 提供一键部署、自动数据分层至低成本存储、弹性扩缩容及高可用架构，降低运维复杂度。
- 🛠️ **完全兼容 PostgreSQL**：保留完整的 SQL 语法和生态系统支持（如 JOINs、地理空间/向量类型），便于开发者无缝迁移。
- 📊 **多场景应用**：适用于物联网设备监控、金融行情分析、实时客户看板等，已被 Cloudflare、Replicated 等企业采用。
- 🔒 **企业级安全与合规**：提供 SOC 2、HIPAA、GDPR 合规支持，具备加密、SSO/VPC 集成等安全特性。
- ⚙️ **灵活部署选项**：可选择全托管云服务（Tiger Cloud）或自行部署（开源/企业版），满足不同运维需求。

---

### [Cypress v15.10.0+ 环境变量访问：迁移至 cy.env() 与 Cypress.expose()](https://www.cypress.io/blog/environment-variable-access-in-cypress-v15-10-0-migrating-to-cy-env-and-cypress-expose)

**原文标题**: [Environment Variable Access in Cypress v15.10.0+: Migrating to cy.env() and Cypress.expose()](https://www.cypress.io/blog/environment-variable-access-in-cypress-v15-10-0-migrating-to-cy-env-and-cypress-expose)

Cypress 15.10.0 起弃用 Cypress.env()，推荐迁移至 cy.env() 和 Cypress.expose()，以增强环境变量访问的安全性控制。

- 🚨 Cypress.env() 自 15.10.0 起弃用，16.0.0 将移除，旨在防止敏感数据意外暴露至浏览器环境
- 🔒 迁移方案：敏感值使用 cy.env() 保留在 Node.js 进程；安全公开值使用 Cypress.expose()
- ⚙️ 配置中设置 allowCypressEnv: false 以强制迁移，未升级的 Cypress.env() 调用将报错
- 📦 升级相关插件（如 @cypress/grep、@cypress/code-coverage）至最新主版本以兼容新规范
- ⏳ 无法立即升级时（Cypress < 15.10.0），敏感值可暂用 cy.task() 替代，但需 v12.5.0 及以上版本支持
- 📚 详细迁移指南和示例可查阅官方文档，团队将持续优化社区指导与适配体验

---

### [测量 SVG 渲染时间 / Stoyan 的 phpied.com](https://www.phpied.com/measuring-svg-rendering-time/)

**原文标题**: [  Measuring SVG rendering time / Stoyan's phpied.com](https://www.phpied.com/measuring-svg-rendering-time/)

本文探讨了 SVG 与 PNG 图像渲染性能的对比研究，通过生成不同大小的测试图像并测量其渲染时间，分析了文件大小对渲染性能的影响。

- 📊 研究通过生成 199 个 SVG 文件（1KB 至 10MB）并转换为 PNG，测试不同格式和大小的图像渲染性能
- ⚙️ 使用自动化测试工具（Puppeteer 脚本）测量交互到下一次绘制（INP）时间，重点关注渲染延迟而非下载时间
- 📈 结果显示 SVG 渲染时间呈阶梯式增长：小于 400KB 的文件渲染时间相近，之后在 400KB 和 1.2MB 处出现明显跳跃
- 🖼️ PNG 渲染性能相对稳定，在大型文件（尤其超过 2MB）中渲染速度优于 SVG
- 🔧 测试方法包括 CPU 节流对比，结果显示性能趋势在不同硬件条件下保持一致

---

### [Croner - 概述](https://croner.56k.guru/)

**原文标题**: [Croner - Overview](https://croner.56k.guru/)

Croner 是一个用于 JavaScript 和 TypeScript 的无依赖、功能全面的 cron 表达式解析与任务调度库，支持 Node.js、Deno、Bun 及浏览器环境，遵循 OCPS 规范并提供时区、超时保护等高级功能。

- ⚙️ **功能全面**：支持完整的 OCPS 1.0-1.4 规范，包括秒/年字段、L（最后一天）、W（最近工作日）、#（第 N 次出现）和 +（AND 逻辑）等高级语法。
- 🌐 **跨平台兼容**：可在 Node.js（≥18.0）、Deno（≥2.0）、Bun（≥1.0.0）和浏览器中运行，支持 CommonJS、ES 模块和 UMD 格式。
- 🛡️ **内置保护机制**：提供任务超时保护和错误处理功能，支持异步函数和 TypeScript 类型定义。
- ⏱️ **灵活调度控制**：允许暂停、恢复或停止已调度的任务，支持时区设定，并可计算下一次或未来多次运行时间。
- 📦 **轻量无依赖**：纯内存操作，无需数据库或配置文件，被 pm2、Uptime Kuma 等知名项目使用。
- 🔄 **使用示例丰富**：包括定时执行函数、计算未来日期（如下 100 个星期日）、倒计时特定日期，以及跨时区调度任务。

---

### [cron - 维基百科](https://en.wikipedia.org/wiki/Cron#CRON_expression)

**原文标题**: [cron - Wikipedia](https://en.wikipedia.org/wiki/Cron#CRON_expression)

cron 是一个用于在 Unix 和类 Unix 操作系统中调度周期性任务的命令行工具，通过 crontab 文件配置任务执行时间，广泛应用于系统维护和任务自动化。

- ⏰ **基本功能**：cron 用于调度周期性任务（称为 cron 作业），通过 crontab 文件定义任务执行时间，语法包含五个时间字段（分钟、小时、日期、月份、星期）。
- 📁 **配置文件**：用户和系统均可拥有 crontab 文件，用户通过 `crontab -e` 编辑个人任务，系统文件通常位于 `/etc/cron.d` 等目录。
- 🕐 **时间语法**：时间字段支持通配符（*）、范围（-）、列表（,）和步长（/），例如 `*/5 * * * *` 表示每 5 分钟执行一次。
- 🚀 **预定义宏**：部分实现支持快捷宏，如 `@daily`（每天午夜执行）、`@reboot`（系统启动时执行一次）。
- 🌍 **时区处理**：cron 默认使用系统时区，但可通过 `CRON_TZ=<时区>` 为任务指定特定时区。
- 🔐 **权限管理**：通过 `/etc/cron.allow` 和 `/etc/cron.deny` 文件控制用户访问权限，若无这些文件则依赖系统默认设置。
- 📜 **历史发展**：cron 最初于 1975 年在 AT&T 贝尔实验室开发，后续衍生出多用户版本（如 Vixie cron）、现代实现（如 cronie）及跨平台变体（如 mcron、webcron）。
- 🔧 **扩展语法**：某些实现（如 Quartz 调度器）支持额外字符，如 `L`（最后一天）、`W`（最近工作日）、`#`（第几个星期几），用于复杂调度。
- 📊 **标准化**：2025 年发布的 Open Cron Pattern Specification (OCPS) 旨在统一不同实现的 cron 语法，提供向后兼容的规范标准。

---

### [发布 10.0.0 版本 · Hexagon/croner · GitHub](https://github.com/Hexagon/croner/releases/tag/10.0.0)

**原文标题**: [Release 10.0.0 · Hexagon/croner · GitHub](https://github.com/Hexagon/croner/releases/tag/10.0.0)

Croner 10.0.0 是一个重大版本更新，实现了完整的 OCPS 1.4 合规性，引入了新的调度功能并提升了可靠性。

- 🎯 **全面 OCPS 合规**：支持年份字段、W（最近工作日）和 +（与逻辑）修饰符，以及 `@midnight` 等模式昵称。
- 🔍 **新增匹配与查询方法**：`match()` 方法可检查日期是否匹配 cron 模式，`previousRuns()` 可枚举过去的计划执行时间。
- 📅 **灵活的日期偏移**：通过 `dayOffset` 选项，可实现“前一天”或“后一天”等相对日期的任务调度。
- 🐛 **关键 DST 修复**：解决了夏令时转换期间可能导致任务重复执行或跳过小时的关键错误。
- ⚙️ **增强的模式控制**：新增 `mode` 选项精确控制模式解析，`sloppyRanges` 选项在保持向后兼容的同时支持更严格的语法。
- ⚠️ **重大变更**：`?` 字符现作为通配符别名（同 `*`），最低 Deno 版本要求提升至 2.0，默认启用更严格的范围解析。
- 📚 **完善的文档与迁移指南**：提供了完整的 OCPS 合规文档和从 9.x 升级到 10.0 的详细迁移指南。

---

### [GitHub - hectorm/otpauth：适用于Node.js、Deno、Bun及浏览器的单次密码（HOTP/TOTP）库。](https://github.com/hectorm/otpauth)

**原文标题**: [GitHub - hectorm/otpauth: One Time Password (HOTP/TOTP) library for Node.js, Deno, Bun and browsers.](https://github.com/hectorm/otpauth)

这是一个用于生成和验证一次性密码（HOTP/TOTP）的 JavaScript 库，支持 Node.js、Deno、Bun 和浏览器环境，遵循 RFC 4226 和 RFC 6238 标准，常用于多因素身份验证系统。

- 🔐 支持 HMAC-Based（HOTP）和 Time-Based（TOTP）一次性密码，符合 RFC 标准
- 🌐 跨平台兼容，适用于 Node.js、Deno、Bun 及现代浏览器
- 🔧 提供完整版、精简版和无依赖版等多种构建选项，灵活适配不同需求
- 🔑 可生成安全随机密钥，默认推荐使用 128 位以上强度
- 🔄 支持令牌验证、剩余时间查询和计数器功能，并提供防重放保护机制
- 📱 兼容 Google Authenticator 密钥 URI 格式，方便集成二维码生成功能
- 📖 提供详细文档和在线演示，便于开发者快速上手
- ⚖️ 采用 MIT 开源协议，已被 6.8k+ 项目使用，社区活跃度高

---

### [GitHub - sindresorhus/log-update：通过覆盖终端中先前的输出来记录日志。适用于渲染进度条、动画等。](https://github.com/sindresorhus/log-update)

**原文标题**: [GitHub - sindresorhus/log-update: Log by overwriting the previous output in the terminal. Useful for rendering progress bars, animations, etc.](https://github.com/sindresorhus/log-update)

log-update 是一个用于在终端中通过覆盖前一行输出来实现动态日志更新的 Node.js 库，适用于进度条、动画等场景，支持部分重绘以减少闪烁。

- 📦 通过覆盖终端前一行输出实现动态日志更新，适用于进度条和动画
- 🛠️ 提供 `logUpdate()`、`clear()`、`done()`、`persist()` 等 API 方法
- ⚙️ 支持自定义输出流和选项，如光标显示、默认宽度和高度
- 🎨 兼容 `chalk` 或 `yoctocolors` 进行输出着色
- 📄 采用 MIT 许可证，拥有 1.1k 星标和 42 个复刻
- 🔄 被 `listr`、`ora`、`speed-test` 等流行工具使用

---

### [GitHub - sindresorhus/ora：优雅的终端加载指示器](https://github.com/sindresorhus/ora)

**原文标题**: [GitHub - sindresorhus/ora: Elegant terminal spinner](https://github.com/sindresorhus/ora)

Ora 是一个优雅的终端加载动画库，用于在命令行界面中显示旋转的加载指示器，支持丰富的自定义选项和 Promise 集成。

- 🌀 **优雅的终端加载动画** – 在命令行中显示流畅的旋转指示器，提升用户体验。
- ⚙️ **高度可定制** – 支持自定义文本、颜色、旋转样式、前缀/后缀文本及输出流等。
- 🚀 **简便的安装与使用** – 通过 npm 安装，几行代码即可快速集成到项目中。
- 🔄 **Promise 集成支持** – 提供 `oraPromise` 方法，可自动根据 Promise 状态切换成功或失败提示。
- 🖥️ **跨平台兼容** – 在 Windows 上自动适配基础旋转样式，并支持 Unicode 环境手动设置。
- 📝 **日志输出友好** – 在加载动画运行时，可正常使用 `console.log` 输出信息，动画会自动调整位置。
- ⚠️ **使用注意事项** – 不支持多实例并发；在 Worker 线程中需通过主线程控制；同步操作会阻塞动画。
- 🌐 **丰富的生态系统** – 拥有多个语言移植版本和相关工具，如 Swift、Python、Rust 的实现。

---

### [GitHub - gavrielc/nanoclaw：我的个人Claude助手，运行于苹果容器中。轻量、安全，专为易于理解和按需定制而构建。](https://github.com/gavrielc/nanoclaw)

**原文标题**: [GitHub - gavrielc/nanoclaw: My personal Claude assistant that runs in Apple containers. Lightweight, secure, and built to be understood and customized for your own needs.](https://github.com/gavrielc/nanoclaw)

这是一个名为 NanoClaw 的个人 Claude 助手项目，在容器中安全运行，轻量且易于理解和自定义。

- 🚀 **项目简介**：NanoClaw 是一个轻量级、安全的个人 Claude 助手，运行在容器中，代码简洁易理解。
- 🛡️ **安全隔离**：代理在 Linux 容器（macOS 用 Apple Container）中运行，文件系统隔离，仅能访问显式挂载的目录。
- 🧩 **AI 原生设计**：通过 Claude Code 引导设置和调试，无需复杂配置文件和安装向导。
- 📱 **支持功能**：包括 WhatsApp I/O、隔离的群组上下文、主频道管理、定时任务和网络访问。
- 🔧 **高度可定制**：通过修改代码或运行技能命令（如`/add-telegram`）来定制功能，避免配置膨胀。
- 🤝 **贡献模式**：鼓励贡献技能文件而非直接添加功能，保持代码库精简。
- ⚙️ **技术要求**：需 macOS 或 Linux、Node.js 20+、Claude Code 及容器运行时（Apple Container 或 Docker）。
- 📄 **开源许可**：采用 MIT 许可证，注重安全性和用户自主控制。

---

### [OpenClaw — 个人 AI 助手](https://openclaw.ai/)

**原文标题**: [OpenClaw — Personal AI Assistant](https://openclaw.ai/)

OpenClaw 是一款开源的个人 AI 助手，它运行在用户自己的设备上，通过 WhatsApp、Telegram 等常用聊天应用进行交互，能执行清理收件箱、管理日历、控制智能设备等实际任务，并具备持久记忆和强大的可扩展性，被社区广泛誉为具有变革性的体验。

- 🦞 **运行在本地设备**：可在 Mac、Windows 或 Linux 上运行，使用 Anthropic、OpenAI 或本地模型，默认私有，数据留在用户手中。
- 💬 **通过聊天应用交互**：支持 WhatsApp、Telegram、Discord、Slack、Signal 或 iMessage 等平台，可在私聊或群聊中使用。
- 🧠 **具备持久记忆**：能记住用户偏好和上下文，成为独特的个人助手。
- 🌐 **控制浏览器与系统**：可以浏览网页、填写表单、读写文件、运行 shell 命令和脚本，拥有完整的系统访问权限。
- 🔧 **高度可扩展**：可通过社区技能或自建插件进行扩展，甚至能为自己编写新功能。
- ⚡ **快速简单的设置**：提供一键安装脚本，几分钟内即可完成设置并开始使用。
- 🤝 **活跃的社区与整合**：拥有快速增长的开源社区，已整合 Gmail、GitHub、Obsidian 等 50 多种服务，用户可分享和获取新技能。
- 🚀 **被赞为革命性体验**：用户反馈称其带来了如同首次接触 ChatGPT 般的震撼感，感觉像是生活在未来，是真正的“数字员工”和“个人操作系统”。

---

### [GitHub - Fats403/simple-ffmpegjs：用于视频合成、转场、音频混音及动态文字叠加的简易Node.js FFmpeg 辅助工具。](https://github.com/Fats403/simple-ffmpegjs)

**原文标题**: [GitHub - Fats403/simple-ffmpegjs: Simple Node.js helper around FFmpeg for video composition, transitions, audio mixing, and animated text overlays.](https://github.com/Fats403/simple-ffmpegjs)

simple-ffmpegjs 是一个轻量级的 Node.js 库，用于通过 FFmpeg 进行程序化视频合成。它专为数据管道和自动化工作流设计，提供声明式、配置驱动的 API，支持视频拼接、转场、音频混合、动画文本叠加、字幕导入、水印等功能，并包含完整的 TypeScript 类型定义和预验证机制。

- 🎬 **视频合成与转场** – 支持多片段拼接及多种 xfade 转场效果（如淡入淡出、划入等）。
- 🔊 **音频混合** – 可叠加背景音乐、语音旁白，并支持音量调节与循环播放。
- ✨ **动画文本叠加** – 提供静态、逐字替换、顺序显示、卡拉 OK 高亮等多种文本模式，支持打字机、缩放、脉冲等动画效果。
- 📄 **字幕与水印** – 支持导入 SRT、VTT、ASS/SSA 字幕文件，并可添加文字或图片水印（支持定时显示与自定义位置）。
- 🖼️ **图像处理** – 支持静态图像并可为图像添加 Ken Burns 效果（缩放、平移）。
- ⚙️ **平台预设与输出控制** – 内置 TikTok、YouTube、Instagram 等平台的分辨率与帧率预设，支持硬件加速、双通道编码、进度回调与取消操作。
- 🔍 **预验证与错误处理** – 提供结构化验证机制，可在执行前检查配置错误，并返回详细的错误代码与路径，适合 AI 管道反馈循环。
- 🧩 **自动批处理** – 当滤镜图过于复杂时，自动拆分处理以避免系统命令行长度限制。
- 📦 **零依赖与完整类型** – 仅需系统安装 FFmpeg，自带 TypeScript 类型定义，无需额外依赖。

---

### [GitHub - seydx/node-av：适用于Node.js的FFmpeg绑定库。提供低级与高级API、完整硬件加速支持、TypeScript兼容及现代化异步编程模式。](https://github.com/seydx/node-av)

**原文标题**: [GitHub - seydx/node-av: FFmpeg bindings for Node.js. Features both low-level and high-level APIs, full hardware acceleration, TypeScript support, and modern async patterns](https://github.com/seydx/node-av)

NodeAV 是一个为 Node.js 提供的原生 FFmpeg 绑定库，包含低层和高层 API，支持完整的硬件加速、TypeScript 和现代异步模式。

- 🎯 **提供原生 FFmpeg 绑定**：通过 N-API 直接访问 FFmpeg 的 C API，包含低层控制和高层抽象。
- 🚀 **支持硬件加速**：自动检测或指定使用 CUDA、VAAPI 等硬件编解码，提升处理性能。
- 📦 **资源自动管理**：采用 Disposable 模式，确保资源（如解码器、格式上下文）自动清理。
- 🔧 **多层级 API 设计**：低层 API 用于完全控制，高层 API 简化常见任务（解码、编码、封装）。
- 🌐 **多样化输入输出**：支持文件、网络流、缓冲区、原始媒体、设备捕获（摄像头、麦克风、屏幕）及自定义 I/O 回调。
- ⚡ **性能接近原生**：基准测试显示转码性能与 FFmpeg CLI 相当，内存使用在流复制时显著更低。
- 🔄 **同步与异步操作**：所有异步方法均有对应的同步版本（后缀 `Sync`），兼顾事件循环非阻塞与低开销。
- 📚 **模块化导入**：支持按需导入（API、常量、布局等），便于 Tree Shaking 优化打包体积。
- 🖥️ **跨平台与预构建**：提供 Windows、Linux、macOS 的预编译二进制文件，支持 x64 和 ARM64 架构。
- 🛠️ **高级功能集成**：包含语音识别（Whisper）、复杂视频滤镜、浏览器流媒体（fMP4/WebRTC）和 RTSP 双向通信等示例。

---

### [GitHub - node-hid/node-hid：通过Node.js访问USB和蓝牙HID设备](https://github.com/node-hid/node-hid)

**原文标题**: [GitHub - node-hid/node-hid: Access USB & Bluetooth HID devices through Node.js](https://github.com/node-hid/node-hid)

node-hid 是一个 Node.js 库，用于通过 JavaScript 访问 USB 和蓝牙 HID（人机接口设备）设备。它支持跨平台操作（包括 Windows、macOS 和 Linux），并提供了同步和异步两种 API 以进行设备枚举、数据读写等功能。该库适用于需要与 HID 设备（如游戏手柄、特定传感器或自定义硬件）交互的应用程序。

- 🔌 **跨平台支持** – 兼容 Windows、macOS 和 Linux 等多种操作系统。
- ⚙️ **双 API 模式** – 提供同步和异步 API，异步 API 推荐用于避免阻塞主线程。
- 📋 **设备枚举** – 可以列出所有连接的 HID 设备，并获取详细信息如厂商 ID、产品 ID 和路径。
- 🔓 **设备访问** – 支持通过路径或 VID/PID 打开设备，macOS 上还可设置非独占模式。
- 📥 **数据读取** – 通过事件监听器接收输入报告，或同步获取特性报告。
- 📤 **数据写入** – 支持发送输出报告和特性报告，需注意报告 ID 的使用。
- 🛠️ **底层控制** – 提供如暂停/恢复读取、非阻塞模式设置等底层操作。
- 🐧 **Linux 特定配置** – 涉及 udev 权限设置和驱动类型选择（hidraw 或 libusb）。
- 🔧 **从源码编译** – 支持在预构建二进制不可用时从源码编译，并提供了详细的编译指南。
- ⚡ **与 Electron/NW.js 集成** – 说明了在 Electron 或 NW.js 项目中使用时的注意事项和配置方法。
- ⚠️ **设备限制** – 无法读取被操作系统占用的设备，如键盘、鼠标等。

---

### [发布 v7.1.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.1.0)

**原文标题**: [Release v7.1.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.1.0)

MongoDB Node.js 驱动程序发布了 7.1.0 版本，重点改进了运行时兼容性、连接稳定性和身份验证功能，并修复了若干问题。

- 🧩 运行时兼容性提升：移除了对 `aws4` 包的依赖，不再使用 `util.promisify`，并替换多个 Node.js 专属 API 为标准等效实现，增强非 Node.js 运行环境的支持。
- 🔁 连接稳定性优化：在服务器过载时避免不必要的连接池清空，事务重试时引入指数退避机制，并在重试命令时降低对问题服务器的优先级。
- 🔐 OIDC 身份验证改进：扩展了默认允许的主机列表，并修复了在 `promoteValues: false` 配置下的重新认证问题。
- ✅ 聚合操作修复：解决了 `$merge` 和 `$out` 阶段未能正确遵循次要节点读取偏好的问题。
- ⚠️ 弃用项：标记 `RenameCollectionOptions.new_collection` 为已弃用，未来版本将移除。

---

### [GitHub - timgit/pg-boss: 在 Node.js 中像大佬一样在 Postgres 中排队作业](https://github.com/timgit/pg-boss)

**原文标题**: [GitHub - timgit/pg-boss: Queueing jobs in Postgres from Node.js like a boss](https://github.com/timgit/pg-boss)

pg-boss 是一个基于 PostgreSQL 构建的 Node.js 作业队列库，旨在为 Node.js 应用提供后台处理和可靠的异步执行能力。它利用 PostgreSQL 的 SKIP LOCKED 功能实现精确一次交付，并支持事务内创建作业、定时任务、优先级队列及 CLI 管理等特性。

- 🐘 基于 PostgreSQL 的作业队列，利用 SKIP LOCKED 功能确保精确一次交付和事务安全
- ⚙️ 提供完整的队列功能，包括定时任务、优先级队列、死信队列、自动重试和发布/订阅模式
- 🛠️ 内置命令行工具，支持数据库迁移、架构管理和 SQL 预览，便于集成到 CI/CD 流程
- 🔧 支持多种配置方式，包括命令行参数、环境变量和配置文件，灵活适应不同部署环境
- 📚 包含详细文档和开发指南，提供 Docker Compose 配置便于本地测试和开发
- 🌐 适用于已有 PostgreSQL 架构的团队，减少系统依赖，特别适合需要限制外部服务数量的场景

---

### [发布版本 28.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/28.0.0)

**原文标题**: [Release Version 28.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/28.0.0)

jsdom 28.0.0 版本发布，主要更新了资源加载定制功能，并修复了多项问题，包括 MIME 类型嗅探、查询组件解码及事件触发等。

- 🔄 彻底重构资源加载定制功能，详细 API 请参阅新版 README
- 🧪 为`<iframe>`和`<frame>`加载添加 MIME 类型嗅探支持
- ⚠️ 已知问题：WebSocket连接现无法按源正确限流（受nodejs/undici#4743影响）
- 🔧 修复非 UTF-8 文档中`<a>`和`<area>`元素查询组件的解码问题
- 🔗 使 XMLHttpRequest 和 WebSocket 请求可被新资源加载系统拦截（同步 XHR 除外）
- 📍 修正涉及重定向时文档 referrer 的设置逻辑（现指向发起页面而非重定向链末页）
- 🛡️ 修复向 API 传递 ArrayBuffer 或类型化数组时的数据快照正确性问题
- ⚠️ 消除使用 WebSocket 时出现的`require("url").parse()`弃用警告
- ✅ 修正`<iframe>`、`<frame>`和`<img>`在非 200HTTP 响应时触发`load`事件而非`error`事件
- 🧩 修复 XMLHttpRequest 中的多个细节问题

---

### [GitHub - perry-mitchell/webdav-client：使用TypeScript编写的适用于NodeJS和浏览器的WebDAV客户端](https://github.com/perry-mitchell/webdav-client)

**原文标题**: [GitHub - perry-mitchell/webdav-client: WebDAV client written in Typescript for NodeJS and the browser](https://github.com/perry-mitchell/webdav-client)

这是一个用 TypeScript 编写的 WebDAV 客户端库，支持 Node.js 和浏览器环境，用于与 WebDAV 服务器进行交互。

- 🌐 **支持环境**：适用于 Node.js（v14+）和浏览器，v5 版本采用 ESM 模块系统，需兼容环境支持。
- 🔐 **认证方式**：支持无认证、密码、令牌和摘要认证，可自动检测或手动指定类型。
- 📁 **核心功能**：提供文件/目录操作，如获取目录内容、上传下载文件、创建删除目录、移动复制文件等。
- 🔧 **高级特性**：支持流式读写、配额查询、文件锁定/解锁、自定义请求和属性解析。
- 📦 **安装使用**：通过 npm 安装，使用`createClient`创建客户端实例，配置服务器地址和认证信息。
- 🛠️ **配置灵活**：可设置请求头、HTTP 代理、递归创建目录等选项，支持详细响应和自定义属性解析。
- 🌍 **跨平台注意**：浏览器中流功能受限，CORS 需服务器支持；React Native 需特定配置。
- 📄 **项目应用**：被多个项目如 Buttercup 密码管理器、Nextcloud 等使用，遵循 MIT 许可证。

---

### [哨兵先知：在开发的每个阶段用 AI 进行调试 | Sentry](https://blog.sentry.io/seer-debug-with-ai-at-every-stage-of-development/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=seer-fy27q1-seerlaunch&utm_content=static-ad-blog-launch-learnmore)

**原文标题**: [Seer by Sentry: debug with AI at every stage of development | Sentry](https://blog.sentry.io/seer-debug-with-ai-at-every-stage-of-development/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=seer-fy27q1-seerlaunch&utm_content=static-ad-blog-launch-learnmore)

Seer 是一款 AI 调试助手，现已扩展至开发全流程，提供本地开发、代码审查和生产环境的调试支持，并以每月 40 美元的固定价格提供无限使用。

- 🔍 **生产环境调试**：利用 Sentry 收集的运行时遥测数据（如错误、日志、指标等）精准定位和修复分布式系统中的复杂故障。
- 💻 **本地开发集成**：通过 Sentry MCP 服务器连接本地编码代理，在开发阶段即时捕获并修复问题，防止缺陷进入代码审查或生产环境。
- 📋 **代码审查辅助**：在代码合并前自动识别可能影响生产的真实缺陷，减少线上事故并加速发布流程。
- 🤖 **自动化根因分析**：针对生产环境中的问题，自动分析遥测数据并提供修复方案，甚至可委托编码代理（如 Cursor）实施修复。
- 🧩 **开放式问题调查**：支持通过自然语言描述现象，查询遥测数据以发现异常模式，将模糊线索转化为可操作的根因分析（功能预览中）。
- 💰 **统一计价模式**：按活跃贡献者（月内提交至少 2 个 PR）每月 40 美元收费，不限使用次数，无需管理席位或超额费用。

---

### [错误](https://nodeweekly.com/link/180292/web)

**原文标题**: [Error](https://nodeweekly.com/link/180292/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/180292/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/180293/web)

**原文标题**: [Error](https://nodeweekly.com/link/180293/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/180293/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [介绍 Deno 沙盒 | Deno](https://deno.com/blog/introducing-deno-sandbox)

**原文标题**: [Introducing Deno Sandbox | Deno](https://deno.com/blog/introducing-deno-sandbox)

Deno Sandbox 是一款专为运行不受信任代码（如 LLM 生成或用户提交的代码）设计的轻量级安全隔离环境，提供网络出口控制和防密钥泄露保护，并支持从沙箱直接部署到生产环境。

- 🛡️ **安全隔离**：通过轻量级 Linux 微虚拟机运行不受信任代码，防止系统被入侵或 API 密钥被盗。
- 🔑 **密钥保护**：密钥仅在实际请求批准的主机时动态生成，防止通过占位符泄露。
- 🌐 **网络控制**：可限制沙箱只能访问特定主机，未授权请求在虚拟机边界被拦截。
- 🚀 **快速部署**：支持从沙箱直接部署代码到 Deno Deploy 生产环境，无需重建或重新认证。
- 💾 **持久化支持**：提供临时存储、快照和读写卷，支持预装工具链和快速创建开发环境。
- ⚙️ **技术规格**：支持多区域、2 个 vCPU、内存 768MB-4GB、启动时间小于 1 秒，最长运行 30 分钟。
- 💰 **灵活计费**：按计算时间和内存使用量计费，包含免费额度，适用于 AI 代理、安全插件等场景。

---

### [在越狱 iPhone 上从源码编译 Node.js 18 以运行 Claude 代码 | Hacker News](https://news.ycombinator.com/item?id=46761266)

**原文标题**: [Compiled Node.js 18 from source on jailbroken iPhone to run Claude Code | Hacker News](https://news.ycombinator.com/item?id=46761266)

在越狱的 iPhone 上成功编译并运行了 Node.js 18，以支持 Claude Code 的本地执行，无需依赖远程服务器。

- 🛠️ 在 iPhone 12 Pro Max（iOS 16.5，Dopamine 越狱）上原生编译了 Node.js 18.20.4
- 📈 发现 Apple 的-fembed-bitcode 标志导致文件体积异常增大，移除后构建大小从 29GB 降至 8GB 以下
- ⚙️ 因 iOS 无 Xcode，需伪造 xcrun/xcodebuild 脚本以完成编译
- 🔏 所有构建工具（如 mksnapshot、torque）在编译过程中均需进行 ldid 签名
- 🧠 最终二进制文件需添加--no-wasm-code-gc 标志以适应 iOS 内存管理特性
- ✅ 生成 71MB 的 Node 可执行文件，完整支持 WebAssembly 和 ICU，可交互运行 Claude Code

---

### [在继续前往 YouTube 之前](https://consent.youtube.com/m?continue=https%3A%2F%2Fwww.youtube.com%2Fshorts%2FNXgqi1jgSq0%3Fcbrd%3D1&gl=CY&m=0&pc=yt&cm=2&hl=el&src=1)

**原文标题**: [Πριν συνεχίσετε στο YouTube](https://consent.youtube.com/m?continue=https%3A%2F%2Fwww.youtube.com%2Fshorts%2FNXgqi1jgSq0%3Fcbrd%3D1&gl=CY&m=0&pc=yt&cm=2&hl=el&src=1)

该文本是 YouTube 的 Cookie 使用和数据收集政策说明，解释了平台如何利用 Cookie 和用户数据来提供服务、保障安全、改进体验以及展示广告。

- 🍪 **提供和维护服务**：使用 Cookie 确保 Google 服务的正常运行和稳定性。
- 🛡️ **安全和反欺诈**：监控服务中断，防止垃圾内容、欺诈和滥用行为。
- 📊 **分析和改进服务**：收集网站统计数据以了解服务使用情况并提升质量。
- 🔧 **开发新服务**：在用户同意后，数据可用于开发和改进新功能。
- 📺 **广告展示与效果评估**：用于投放广告并衡量其有效性。
- 🎯 **个性化内容与广告**：根据用户设置显示定制化内容和定向广告。
- 🌍 **非个性化内容影响因素**：非定制化内容受当前观看内容和地理位置等影响。
- 👶 **适龄体验设计**：必要时使用数据调整服务以确保适合不同年龄段的用户。
- ⚙️ **用户控制选项**：提供“接受所有”、“拒绝所有”和“更多选项”来管理隐私设置。

---

### [Amazon EC2 C8id、M8id 和 R8id 实例现已全面上市，提供高达 22.8 TB 本地 NVMe 存储 | AWS 新闻博客](https://aws.amazon.com/blogs/aws/amazon-ec2-c8id-m8id-and-r8id-instances-with-up-to-22-8-tb-local-nvme-storage-are-generally-available/)

**原文标题**: [Amazon EC2 C8id, M8id, and R8id instances with up to 22.8 TB local NVMe storage are generally available | AWS News Blog](https://aws.amazon.com/blogs/aws/amazon-ec2-c8id-m8id-and-r8id-instances-with-up-to-22-8-tb-local-nvme-storage-are-generally-available/)

AWS 宣布推出新一代 Amazon EC2 C8id、M8id 和 R8id 实例，这些实例搭载定制 Intel Xeon 6 处理器，提供高达 22.8TB 的本地 NVMe 存储，相比前代实例在计算性能、内存带宽和存储容量上均有显著提升，适用于计算密集型、内存密集型及需要高速本地存储的工作负载。

- 💻 C8id 实例适合计算密集型任务，如视频编码和图像处理，提供高速低延迟本地存储。
- ⚖️ M8id 实例平衡计算与内存资源，适用于数据记录、媒体处理和中型数据存储。
- 🧠 R8id 实例针对内存密集型工作负载设计，如大规模 SQL/NoSQL 数据库、内存数据库和 AI 推理。
- 🚀 实例性能提升：计算性能最高提升 43%，内存带宽增加 3.3 倍，I/O 密集型数据库性能提升 46%，实时数据分析查询速度加快 30%。
- 📊 规格扩展：最大支持 96xlarge 规格，提供 384 个 vCPU、3TiB 内存和 22.8TB 本地存储，并包含两种裸金属配置。
- 🔧 支持实例带宽配置（IBC）功能，可灵活分配网络与 EBS 带宽资源，优化工作负载性能。
- 🔒 本地 NVMe 存储采用硬件加密（XTS-AES-256），数据在实例停止或终止后自动销毁，不持久保存。
- 🌍 现已在美国东部（弗吉尼亚北部、俄亥俄）、美国西部（俄勒冈）和欧洲（法兰克福）区域开放使用。
- 💰 支持按需实例、Savings Plans、Spot 实例、专用实例和专用主机等多种购买方式。

---

### [精准解析器 - 每日 WTF](https://thedailywtf.com/articles/a-percise-parser)

**原文标题**: [A Percise Parser - The Daily WTF](https://thedailywtf.com/articles/a-percise-parser)

该网站是一个面向程序员的技术内容聚合平台，主要提供多种类型的编程相关文章和社区交流功能。

- 📰 专题文章：深度探讨特定技术主题或趋势
- 🧩 代码片段：展示实用、典型或有趣的编程示例
- ❌ 错误分析：解析常见编程错误及其解决方案
- 💬 论坛讨论：提供技术交流和问题互助的社区空间
- 📚 其他文章：涵盖各类编程技术、工具和经验的综合性内容
- 🎲 随机文章：为用户推荐不确定性的技术阅读内容

---

### [近期 React 与 Node.js 中的 CVE 漏洞由 AI 发现 | winfunc](https://winfunc.com/blog/recent-0-days-in-nodejs-and-react-were-found-by-an-ai)

**原文标题**: [The Recent CVEs in React and Node.js Were Found by an AI | winfunc](https://winfunc.com/blog/recent-0-days-in-nodejs-and-react-were-found-by-an-ai)

2025 年 12 月至 2026 年 1 月，一个 AI 系统自主发现了 Node.js 和 React 中的零日漏洞，并完成了从发现、验证到负责任披露的全过程。这标志着 AI 在安全研究领域实现了从代码理解到漏洞利用的自主闭环能力。

- 🐛 **Node.js 权限绕过漏洞（CVE-2026-21636）**：Node.js 的权限模型未对 Unix 域套接字连接进行网络权限检查，导致沙箱内的恶意脚本可访问 Docker 守护进程、数据库等本地敏感服务，实现权限提升。
- 💥 **React 服务器组件拒绝服务漏洞（CVE-2026-23864）**：React 服务器组件的回复解码器在处理包含特定`$K`标记的 FormData 时，可能触发无限循环或内存耗尽，导致服务器 CPU 或内存资源被耗尽，影响 Next.js 等多个流行框架。
- 🤖 **AI 驱动的全流程安全研究**：系统通过代码语义建模、威胁假设生成、漏洞路径分析、利用代码编写及实际验证五个步骤，自主发现传统扫描器无法识别的逻辑漏洞，减少了误报。
- 🧠 **克服“AI 幻觉”实现可靠发现**：通过精心设计的系统架构（如代码图谱、威胁建模、蒙特卡洛树自优化等），将 LLM 的“创造性”假设转化为可验证的漏洞利用，实现了高准确性的自动化研究。
- 🔒 **负责任披露与业界合作**：漏洞已及时报告给 Node.js 和 React 安全团队，并迅速获得修复，相关团队对披露过程处理专业，体现了开源社区良好的安全协作生态。

---

