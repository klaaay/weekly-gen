### [Node 周刊第 576 期：2025 年 4 月 29 日](https://nodeweekly.com/issues/576)

**原文标题**: [Node Weekly Issue 576: April 29, 2025](https://nodeweekly.com/issues/576)

概述总结  
- 📅 2025 年 4 月 29 日第 576 期技术动态，涵盖 Node.js、Koa、Bun 等框架更新及工具发布。  
- 🔒 隐私政策提醒：订阅可随时取消，邮箱地址安全。  

详细要点：  
- 🚀 **Koa 3.0 发布**：基于现代 JavaScript 特性的 HTTP 中间件框架，提供比 Express.js 更现代的替代方案。  
- 🔧 **Node v22.15.0（LTS）更新**：支持 Windows/macOS 系统证书、依赖项升级，新增`process.execve`功能。  
- 🍜 **Tonkotsu 工具**：面向 JS/TS 开发者的自然语言 IDE，支持免费早期体验。  
- ⚠️ **Node.js v18 终止支持**：建议升级至 v22，v24 即将发布。  
- 🐇 **Bun 兼容性进展**：通过 100% Node.js `events`模块测试，新增 LLM 支持文档。  
- 🛡️ **Node.js 测试 CI 安全事件**：Jenkins 漏洞被利用，已修复并公布详情。  
- ⚡ **V8 性能优化**：显式编译提示（Explicit Compile Hints）加速启动，Chrome 136 已支持。  
- 📦 **npm 包里程碑**：某团队 npm 包下载量突破 10 亿次，影响 JavaScript 生态。  
- 🤖 **工具更新速览**：  
  - Seyfert：支持 Node/Deno/Bun 的 Discord 机器人框架。  
  - Scala.js 1.19.0：Scala 语言编译为 JavaScript 的工具。  
  - OpenAI Node 4.96：新增`gpt-image-1`模型支持。  
  - 其他：Nest、Electron、Mongoose 等版本更新。  
- 🌍 **JavaScript 生态动态**：  
  - TypeScript与C#对比指南发布。  
  - DuckDB-WASM 实验用于 3D 游戏开发。  
  - p5.js 2.0 缓慢推进重大升级。  
  - Deno 2.3 即将发布，改进更新。  
  - 静态 HTML/JS 被推荐为免费软件最佳实践。  
  - JSR 包现支持 pnpm 和 Yarn。

---

### [Koa - 新一代 Node.js Web 框架](https://koajs.com/)

**原文标题**: [Koa - next generation web framework for node.js](https://koajs.com/)

Koa 是由 Express 团队设计的新 Web 框架，旨在为 Web 应用和 API 提供更小巧、更富表现力且更健壮的基础。通过利用异步函数，Koa 摒弃了回调并大幅提升了错误处理能力。其核心不捆绑任何中间件，提供了一套优雅的方法使服务器开发快速而愉快。

- 🚀 Koa 是 Express 团队打造的新 Web 框架，更轻量、灵活且健壮  
- 🔄 利用异步函数，避免回调，显著改善错误处理  
- 🧩 核心不捆绑中间件，保持简洁和可扩展性  
- ✨ 提供优雅的方法，让服务器开发更高效和愉悦

---

### [Express@5.1.0：现作为 npm 默认版本并提供 LTS 支持时间线](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

**原文标题**: [Express@5.1.0: Now the Default on npm with LTS Timeline](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Express v5.0.0 发布后未立即设为 npm 默认版本，现公布 LTS 时间线及未来规划  

- 🚀 Express v5.0.0 于去年 9 月发布，但未立即设为 npm 的 `latest` 版本，现通过 v5.1.0 完成过渡并启动 LTS 计划  
- 📚 文档与迁移支持：更新了 v5 文档和迁移指南，新增自动化工具（codemod）辅助从 v4 升级，部分破坏性变更仍需手动调整  
- 🔄 生态系统兼容性：预留时间让中间件和教程适配 v5，特别关注新手用户避免版本混淆  
- ⏳ LTS 三阶段支持策略：  
  - **CURRENT**（新版本初期，至少 3 个月）：接收所有更新，推荐尝鲜  
  - **ACTIVE**（稳定期，至少 12 个月）：设为 npm 默认版本，全面支持  
  - **MAINTENANCE**（维护期，12 个月）：仅安全修复，强烈建议升级  
- 📅 拟议时间表：  
  - v4 进入维护期（2025-04-01），EOL 不早于 2026-10-01  
  - v5 为当前活跃版本（2025-03-31 起），EOL 取决于 v6 发布时间  
- ✨ v5.1.0 改进：支持 `Uint8Array`、依赖版本范围优化、ETag 功能增强等  
- 🤝 社区合作：与 HeroDevs 合作支持企业升级，呼吁通过 PR 或 OpenCollective 资助项目  
- 🔜 未来计划：性能优化工作组、TypeScript 体验提升、v6 前期讨论启动  
- 🙏 致谢：列出近百位贡献者，强调社区驱动开发模式  

（注：时间表为目标而非承诺，v4 作为特殊版本可能延长维护）

---

### [发布 v3.0.0 · koajs/koa · GitHub](https://github.com/koajs/koa/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · koajs/koa · GitHub](https://github.com/koajs/koa/releases/tag/v3.0.0)

Koa v3.0.0 是一个主要版本发布，包含多项重大变更、新功能和修复。

- 🚨 **重大变更**: 最低要求 Node.js v18，移除 `.redirect('back')` 并新增 `.back(fallback_url)`  
- 🔄 **移除功能**: 不再支持生成器，移除 `createAsyncCtxStorageMiddleware`  
- 🛠 **修复与改进**: 修复 `req.origin` 对齐 CORS 的 `Origin` 头部，修复 `ctx.throw` 格式要求  
- 📂 **文件处理**: 移除特殊 `ENOENT` 支持，需适配 404 处理逻辑  
- 🆕 **新功能**: 支持自定义流和 WHATWG 响应体，新增 `app.currentContext` 通过 `asyncLocalStorage` 获取当前上下文  
- 🐞 **问题修复**: 修复响应时 socket 不可写、`Content-Length` 与 `Transfer-Encoding` 冲突等问题  
- ♻️ **重构**: 使用 `URLSearchParams` 替代 Node.js 查询字符串  
- 📦 **依赖更新**: 升级 `type-is`、`http-errors`、`cookies` 等依赖  
- 👏 **贡献者**: 感谢 `fl0w`、`charlyzeng` 等 8 位贡献者

---

### [Node.js — Node v22.15.0（长期支持版）](https://nodejs.org/en/blog/release/v22.15.0)

**原文标题**: [Node.js — Node v22.15.0 (LTS)](https://nodejs.org/en/blog/release/v22.15.0)

Node.js v22.15.0 (LTS) 版本发布，代号 "Jod"，由 Ulises Gascón 和 Rafael Gonzaga 准备。此版本包含多项重要更新和修复。

- 🚀 **重要更新**：实现了部分错误比较功能（Ruben Bridgewater）。
- 🔧 **CLI 改进**：允许在 NODE_OPTIONS 中使用 --cpu-prof* 参数（Carlos Espa）。
- 🔒 **加密增强**：更新根证书至 NSS 3.108，并支持从 macOS 系统存储中读取证书（Tim Jacomb）。
- ⏱ **时区更新**：时区数据更新至 2025a 版本。
- 📊 **性能优化**：改进了部分深度严格相等的性能（Ruben Bridgewater）。
- 📡 **DNS 功能**：新增 TLSA 记录查询和解析功能（Rithvik Vibhu）。
- 📝 **文档更新**：新增多个协作者和修复文档错误（Edy Silva 等）。
- 🛠 **构建系统**：修复了多个构建问题，包括 GN 构建和 macOS 链接问题。
- 🔄 **模块系统**：实现了 module.registerHooks() 方法，支持同步钩子（Joyee Cheung）。
- 🗄 **SQLite 支持**：允许从用户定义函数返回 ArrayBufferView（René）。
- 📜 **TLS 功能**：新增 tls.getCACertificates() 方法（Joyee Cheung）。
- 🔍 **V8 更新**：新增 v8.getCppHeapStatistics() 方法（Aditi）。
- 🗜 **Zlib 支持**：新增 zstd 压缩支持（Jan Martin）。

此版本还包含多项错误修复、性能优化和文档改进，适用于生产环境。

---

### [进程：由 ShogunPanda 添加 execve · Pull Request #56496 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/56496)

**原文标题**: [process: add execve by ShogunPanda · Pull Request #56496 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/56496)

Node.js 项目中关于 `process.execve` 方法的 Pull Request 讨论和实现过程。

- 🚀 该 PR 由 ShogunPanda 提出，旨在为 Node.js 添加 `process.execve` 方法，这是一个对 UNIX 函数 `execve` 的封装。
- 🔄 `execve` 方法会替换当前进程为一个新进程，且不会返回，所有内存和系统资源都会被自动回收，除了标准输入、输出和错误流。
- 🐧 主要用途是在 shell 脚本中设置逻辑后生成另一个命令。
- ❤️ 多位贡献者对该 PR 表示支持。
- 🛠️ 在 Windows 平台上，由于 `_execve` 函数的行为不同（不会替换原进程），该功能被禁用。
- 📝 代码覆盖率报告显示，该功能的测试覆盖率为 84.03%，有 19 行代码未被覆盖。
- 🔍 多位核心成员对该 PR 进行了审查，并提出了改进建议，包括命名规范和安全问题。
- ✅ 最终该 PR 被合并，并在 Node.js 23.11.0 和 22.15.0 版本中发布。

---

### [Node.js — Node.js 版本发布](https://nodejs.org/en/about/previous-releases)

**原文标题**: [Node.js — Node.js Releases](https://nodejs.org/en/about/previous-releases)

Node.js 的版本发布和支持策略，包括官方与社区安装方法的分类标准。

- 🚀 **版本发布周期**：主要 Node.js 版本发布后有 6 个月的当前支持期，之后奇数版本停止支持，偶数版本进入 Active LTS（长期支持）。  
- 🛡️ **LTS 支持**：Active LTS 和维护 LTS 版本提供 30 个月的关键 bug 修复，适合生产环境使用。  
- 📅 **版本状态表**：详细列出各版本代号、发布时间、最后更新日期及当前状态（如 v23 维护中、v22 为 LTS、v21 已终止支持等）。  
- 💼 **商业支持**：超过维护期的版本可通过 OpenJS 合作伙伴 HeroDevs 获得商业支持。  
- ⚙️ **安装方法分类**：分为“官方”和“社区”两类，官方方法需同步发布、直接沟通渠道且使用官方二进制文件。  
- 📜 **社区方法标准**：需支持所有非 EOL 版本、兼容至少一个官方 OS、覆盖广泛发行版，且必须免费开源。  
- 🔗 **更多详情**：完整发布计划和安装方法标准可在 GitHub 和 Node.js 官网查询。

---

### [Bun —— 一款全功能高速 JavaScript 运行时](https://bun.sh/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.sh/)

Bun v1.2.11 是一个快速、全能的 JavaScript 工具包，集成了开发、测试、运行和打包功能，并致力于实现 100% Node.js 兼容性。

- 🚀 **Bun 简介**：Bun 是一个高性能的 JavaScript 运行时和工具包，包含打包工具、测试运行器和兼容 Node.js 的包管理器。  
- ⚡ **性能优势**：在 HTTP 请求、WebSocket 消息发送和数据库查询等基准测试中，Bun 的性能显著优于 Deno 和 Node.js。  
- 📥 **安装方式**：支持 Linux、macOS 和 Windows，可通过 curl 或 PowerShell 快速安装。  
- 🔄 **Node.js 兼容**：Bun 旨在完全兼容 Node.js，方便开发者无缝迁移。  
- 🏆 **性能对比**：  
  - HTTP 请求：Bun 59,026/秒，Deno 25,335/秒，Node.js 19,039/秒。  
  - WebSocket 消息：Bun 2,536,227/秒，Deno 1,320,525/秒，Node.js 435,099/秒。  
  - 数据库查询：Bun 50,251/秒，Node.js 14,398/秒，Deno 11,821/秒。  
- 🌐 **广泛应用**：被 Express、Postgres 和 WebSocket 等流行工具和框架使用。

---

### [未找到标题](https://x.com/bunjavascript/status/1915633844155527208)

**原文标题**: [No title found](https://x.com/bunjavascript/status/1915633844155527208)

当前页面提示 JavaScript 未启用或浏览器不受支持，导致功能无法正常使用，并提供了一系列解决方案和相关链接。

- 🚫 JavaScript 未启用：检测到浏览器中 JavaScript 被禁用，需启用或更换支持浏览器。  
- 🌐 支持浏览器列表：可查看帮助中心获取兼容浏览器信息。  
- 🔧 解决建议：尝试重新加载页面或禁用隐私扩展插件。  
- 📜 相关链接：提供帮助中心、服务条款、隐私政策等文档入口。  
- ©️ 版权信息：页面底部标注 X Corp 公司 2025 年版权声明。  
- ❗ 错误提示：页面加载异常时显示友好提示，鼓励用户再次尝试。

---

### [非 HTML 内容](https://bun.sh/llms-full.txt)

**原文标题**: [Non-HTML content](https://bun.sh/llms-full.txt)

无法总结：非 HTML 内容。

---

### [Node.js Vercel 函数现已支持请求取消 - Vercel](https://vercel.com/changelog/node-js-vercel-functions-now-support-request-cancellation)

**原文标题**: [Node.js Vercel Functions now support request cancellation - Vercel](https://vercel.com/changelog/node-js-vercel-functions-now-support-request-cancellation)

Vercel Functions 现在支持检测请求取消并提前终止执行，以减少不必要的计算和资源消耗。

- 🚀 Vercel Functions 使用 Node.js 可检测请求取消（如页面跳转、关闭标签页或停止 AI 聊天），并提前终止执行。  
- 💡 通过 `Request.signal.aborted` 或监听 `abort` 事件实现取消逻辑，减少无效计算和令牌生成。  
- ⚙️ 示例代码展示了如何创建 `abortController` 并在请求取消时终止 `fetch` 操作。  
- 🔌 使用 AI SDK 时，可通过传递 `abortSignal` 终止流式文本生成（如 GPT-4-turbo 的响应）。  
- 📚 更多详情可参考官方文档关于 [取消 Function 请求](https://vercel.com/docs/functions/cancelling-function-requests) 的部分。

---

### [Node.js — Node.js 测试 CI 安全事件](https://nodejs.org/en/blog/vulnerability/march-2025-ci-incident)

**原文标题**: [Node.js — Node.js Test CI Security Incident](https://nodejs.org/en/blog/vulnerability/march-2025-ci-incident)

Node.js 测试 CI 安全事件概述：2025 年 3 月 21 日，Node.js 技术指导委员会通过 HackerOne 收到安全报告，揭示测试 CI 主机存在漏洞，攻击者可利用拉取请求流程中的时间差执行恶意代码。团队迅速采取补救措施，包括限制访问、重建主机、验证提交 SHA 等，确保 CI 基础设施安全。事件未影响 Node.js 运行时，用户无需采取行动。

- 🚨 **安全事件报告**：2025 年 3 月 21 日收到 HackerOne 报告，攻击者通过拉取请求流程中的漏洞入侵 Node.js 测试 CI 主机。
- 🔄 **攻击流程**：利用`request-ci`标签和过时的 Git 提交时间戳，在 Jenkins 管道中执行恶意代码。
- 🛠️ **漏洞根源**：CI 构建中存在“检查时间 - 使用时间”（TOCTOU）漏洞，允许攻击者在触发 CI 后更改代码。
- 🔒 **补救措施**：限制 Jenkins 访问、重建 24 台受感染主机、验证提交 SHA、审核 140 个 Jenkins 任务。
- 📅 **时间线**：3 月 21 日确认漏洞，3 月 24 日移除受感染主机，4 月 1 日逐步恢复 CI 功能。
- ⚖️ **安全与开发体验**：在 300 多名志愿者的维护下，平衡 CI 安全性与开发者便利性。
- 📢 **用户影响**：事件未影响 Node.js 运行时，用户无需采取行动。
- 📧 **联系方式**：安全政策与漏洞报告流程详见 Node.js 官网，更新可通过 nodejs-sec 邮件列表获取。

---

### [给 V8 一个提示：利用显式编译提示加速 JavaScript 启动 · V8](https://v8.dev/blog/explicit-compile-hints)

**原文标题**: [Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints · V8](https://v8.dev/blog/explicit-compile-hints)

V8 引擎通过显式编译提示优化 JavaScript 启动性能，开发者可指定关键函数或文件进行预编译以减少页面加载时的解析和编译延迟，从而提升网页响应速度。

- 🚀 **提升启动速度**：通过预编译关键 JavaScript 函数，减少页面加载时的解析和编译时间，平均可减少 630 毫秒。  
- 🔍 **显式编译提示**：Chrome 136 引入新特性，允许开发者通过注释`//# allFunctionsCalledOnLoad`标记需预编译的文件。  
- ⚠️ **谨慎使用**：过度预编译会消耗额外时间和内存，需平衡性能与资源开销。  
- 🛠️ **实验验证**：开发者可通过日志功能观察函数编译事件，验证预编译效果（如`testfunc2`无延迟解析事件）。  
- 🔮 **未来方向**：计划支持单个函数级别的预编译控制，进一步优化性能。  
- 📅 **发布时间**：2025 年 4 月 29 日，由 Marja Hölttä撰写。

---

### [十年影响：我们的 npm 包如何实现 10 亿次下载并塑造 JavaScript 生态](https://forwardemail.net/en/blog/docs/how-npm-packages-billion-downloads-shaped-javascript-ecosystem)

**原文标题**: [A Decade of Impact: How Our npm Packages Hit 1 Billion Downloads and Shaped JavaScript](https://forwardemail.net/en/blog/docs/how-npm-packages-billion-downloads-shaped-javascript-ecosystem)

过去十年中，我们的 npm 包实现了 10 亿次下载，深刻影响了 JavaScript 生态系统。以下是关键要点：

- 🚀 **npm 包的重大影响**：我们的 npm 包被全球开发者广泛使用，每日下载量达数百万次，成为 JavaScript 生态系统的关键部分。
- 👨💻 **关键人物**：Isaac Z. Schlueter（npm 和 Node.js 的创始人）信任并使用我们的服务，体现了我们对质量和安全的专注。
- 🔧 **技术贡献**：Nick Baugh 作为 Express 和 Koa 框架的核心贡献者，推动了 Node.js 生态系统的发展。
- 📦 **GitHub 组织**：我们创建了多个 GitHub 组织（如 Cabin、Spam Scanner、Forward Email 等），每个组织专注于解决 JavaScript 开发中的特定问题。
- 📊 **惊人数据**：我们的包在 2025 年 2 月至 3 月间下载量惊人，如`superagent`达 8457 万次，`supertest`达 7643 万次。
- 🔒 **安全贡献**：我们识别并修复了多个关键安全漏洞，如 ReDoS 漏洞，并创建了更安全的替代方案。
- 💰 **开源赞助**：我们赞助了如 Andris Reinman（Nodemailer 作者）和 Sindre Sorhus（众多实用工具包作者）等关键开源贡献者。
- 📧 **邮件生态系统**：Forward Email 作为开源邮件服务，提供了邮件转发、存储和 API 服务，其核心包如`preview-email`下载量达 250 万次。
- 📈 **企业影响**：我们的解决方案被教育机构、企业 Linux 解决方案和开源基金会（如 Linux 基金会）采用，用于关键任务邮件基础设施。
- 🔮 **未来展望**：我们承诺继续维护和改进现有包，扩展对关键基础设施项目的贡献，并支持下一代开源贡献者。

---

### [使用通用异步树库进一步精简小型 JavaScript 博客静态网站生成器](https://jan.miksovsky.com/posts/2025/04-23-async-tree.html)

**原文标题**: [Making a small JavaScript blog static site generator even smaller using the general async-tree library](https://jan.miksovsky.com/posts/2025/04-23-async-tree.html)

使用 async-tree 库大幅精简了 JavaScript 中极简静态网站生成器（SSG）的源代码，仅需少量依赖，同时保持快速和灵活。

- 📅 **发布时间**：2025 年 4 月 23 日  
- 🔄 **重构历程**：从 Astro 到零依赖版本，再到基于 async-tree 的共享代码版本  
- 📂 **源码与示例**：[源码链接](source code) | [实时网站](live site)  
- 📦 **依赖选择**：  
  - 使用纯函数库（如 `marked` 处理 Markdown 和 RSS 生成）减少代码量  
  - 避免复杂框架的插件和生命周期问题  
- 🌳 **async-tree 库核心**：  
  - 抽象异步树（`AsyncTree` 接口）统一处理文件系统、内存等异构数据  
  - 支持懒加载（如 `FileTree` 按需读取文件）  
- ✨ **功能示例**：  
  - 分页（`paginate`）和键名转换（`extension` 选项）  
  - 站点结构定义仅需 20 行代码（`site.js`）  
- ⚡ **性能对比**：  
  - 代码量最小（9K），依赖体积仅 1.5Mb（Astro 为 117Mb）  
  - 速度接近零依赖版本  
- 🐞 **调试挑战**：异步代码调试较同步代码困难，但可通过 CLI 工具辅助  
- 🔍 **改进空间**：  
  - 需完善 `async-tree` 文档  
  - 未来可尝试用 Origami 语言进一步精简  
- 💡 **总结**：平衡了简洁性、可控性与功能性，适合追求轻量化的开发者。  

其他系列文章：  
- 《Astro 等静态站点生成器的复杂性》  
- 《极简 SSG 模式仅适合特定需求的 JS 开发者》  
- 本篇：《用 async-tree 进一步精简 JS 博客生成器》

---

### [如何使用 Mocha 在 Node.js 中编写单元测试 | AppSignal 博客](https://blog.appsignal.com/2025/04/23/how-to-write-unit-tests-in-nodejs-using-mocha.html)

**原文标题**: [How To Write Unit Tests in Node.js Using Mocha | AppSignal Blog](https://blog.appsignal.com/2025/04/23/how-to-write-unit-tests-in-nodejs-using-mocha.html)

概述：本文详细介绍了如何在 Node.js 中使用 Mocha 进行单元测试，包括 Mocha 的核心概念、功能、安装步骤以及编写和运行测试的完整示例。

- 🚀 **Mocha 简介**：Mocha 是一个流行的 JavaScript 测试框架，支持 Node.js 和浏览器环境，适用于 BDD 和 TDD 等多种测试方法。
- ⭐ **受欢迎程度**：Mocha 在 GitHub 上有 22.7k 星，每周 npm 下载量超过 1000 万次，是 JavaScript 社区中最受欢迎的测试库之一。
- 📂 **测试文件结构**：默认情况下，Mocha 在`./test/`文件夹中查找测试文件，文件扩展名通常为`.spec.js`。
- 🔧 **BDD 风格 API**：Mocha 提供`describe()`、`it()`、`before()`、`after()`等方法，支持 BDD 风格的测试编写。
- 🔄 **执行流程**：Mocha 按顺序执行测试套件，支持同步和异步代码测试，包括回调、Promise 和 async/await。
- ⚡ **并行执行**：通过`--parallel`选项，Mocha 可以并行运行测试文件，提高测试效率。
- 🔍 **断言库无关**：Mocha 不绑定特定断言库，可以使用 Chai、assert、should.js 等多种库。
- 📝 **示例项目**：文章通过一个生成斐波那契数列的 Node.js 项目，演示了如何安装 Mocha、编写测试文件并运行测试。
- ✅ **测试结果**：运行测试后，Mocha 会输出测试结果，显示通过的测试数量和耗时。
- 🔗 **进一步学习**：文章最后提供了更多学习资源，包括订阅新闻

---

### [赛弗特 | 黑魔法框架](https://www.seyfert.dev/)

**原文标题**: [Seyfert | The Black Magic Framework](https://www.seyfert.dev/)

Seyfert 发布了 v3.1 版本，这是一个强大且简单的 Discord 机器人框架，专为可扩展性和开发者体验设计。它提供了 TypeScript 支持、高性能、易用性、全面自定义和最新 Discord 功能。社区反馈积极，多个大型机器人项目已成功采用 Seyfert，显著提升了性能和资源利用率。Seyfert 是开源的，欢迎贡献和加入社区。

- 🚀 **v3.1 发布** - Seyfert 发布了新版本，强调强大与简单的平衡。  
- 💻 **TypeScript 支持** - 提供类型安全，提升开发体验。  
- 📈 **高性能与可扩展性** - 无论大小机器人，均表现优异。  
- 🛠️ **开发者友好** - 简化设置，专注于机器人逻辑。  
- 🔧 **全面自定义** - 支持每个细节的个性化调整。  
- 🔄 **最新 Discord 功能** - 始终保持与 Discord 最新特性同步。  
- 😆 **社区好评** - 用户称赞其错误处理、文档、类型系统和事件处理速度。  
- 🤖 **成功案例** - 多个大型机器人项目（如音乐机器人）显著降低资源使用并提升性能。  
- 🌍 **开源** - 代码公开，欢迎贡献和审查。  
- 📚 **快速入门** - 提供指南和 Discord 社区支持。

---

### [创建你的第一个命令](https://www.seyfert.dev/guide/getting-started/first-command)

**原文标题**: [Creating Your First Command](https://www.seyfert.dev/guide/getting-started/first-command)

概述  
Seyfert 是一个用于创建和管理 Discord 机器人命令的框架，支持快速开发和部署命令，并提供了选项配置和事件监听功能。

- 🚀 **快速开始**  
  在 `commands` 文件夹中创建命令文件，使用 `@Declare` 装饰器定义命令信息，并继承 `Command` 类实现逻辑。

- 📝 **命令示例**  
  示例 `ping` 命令显示与 Discord 的延迟，代码需放置在 `src/commands/ping.ts` 中，并通过 `ctx.write` 返回结果。

- 🔄 **注册命令**  
  使用 `client.uploadCommands` 方法将命令上传至 Discord，并生成 `commands.json` 缓存文件以避免重复上传。

- ⚙️ **使用选项**  
  通过 `@Options` 装饰器为命令添加选项，例如 `hide` 选项控制消息是否仅对用户可见（Ephemeral 消息）。

- 📂 **项目结构**  
  建议将命令文件组织在 `src/commands` 目录下，保持项目结构清晰，便于管理。

- 🔗 **更多信息**  
  关于命令选项的详细配置可参考官方文档，同时支持子文件夹分类管理命令文件。

---

### [GitHub - tiramisulabs/seyfert：黑魔法 Discord 框架 🧙‍♂️](https://github.com/tiramisulabs/seyfert)

**原文标题**: [GitHub - tiramisulabs/seyfert: the black magic Discord framework 🧙‍♂️](https://github.com/tiramisulabs/seyfert)

Seyfert 是一个全新的 Discord 框架，旨在将机器人开发提升到新的水平。它提供了与 Discord API 的便捷交互、强大的缓存控制、可扩展的代码和出色的开发体验。

- 🧙‍♂️ Seyfert 是一个强大的 Discord 框架，专注于提升开发体验和性能。
- 🚀 主要特点包括低内存占用、最新功能支持、类型安全和良好的开发体验。
- 📦 支持多种包管理器安装，如 pnpm、deno、bun 和 npm。
- 🔧 需要 Node v18 或更高版本（或 v16 带 `--experimental-fetch` 标志）。
- 🤝 开放贡献，欢迎 fork 仓库并进行修改。
- 🔗 提供丰富的资源链接，包括 GitHub 仓库、Discord 服务器、npm 核心、网站和文档。
- ⭐ 目前有 183 个 star 和 33 个 fork，拥有活跃的社区支持。
- 📜 采用 MIT 许可证，遵循行为准则。

---

### [发现。修复。测试。Sentry 与 Codecov 简介 | Sentry](https://sentry.io/resources/find-fix-test/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=general-fy26q1-bidemo&utm_content=newsletter-nodedemo-seehow)

**原文标题**: [Find. Fix. Test. Intro to Sentry & Codecov | Sentry](https://sentry.io/resources/find-fix-test/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=general-fy26q1-bidemo&utm_content=newsletter-nodedemo-seehow)

Sentry 提供错误监控、追踪和代码覆盖率等功能的演示活动，由解决方案工程总监 Neil Manvar 主持，帮助开发者提升代码质量和调试效率。

- 🚀 **演示内容**：25 分钟小组演示，涵盖 Sentry 和 Codecov 的功能与应用场景。  
- 🔧 **功能亮点**：  
  - 无代理设置流程，支持框架级集成。  
  - 错误监控：通过堆栈跟踪、面包屑导航和会话回放快速调试运行时问题。  
  - 追踪：检测性能瓶颈，定位代码中的低效点。  
  - 代码覆盖率：分析 PR 中的代码覆盖率并设定目标，确保代码质量。  
- 📅 **活动安排**：每两周一次（周四上午 10 点 PT），适合新用户或需复习者参与。  
- 📝 **报名信息**：需填写姓名、邮箱、职位等，并选择预约场次。  
- 🔒 **隐私声明**：明确数据收集范围（如账户信息、设备数据）及使用目的（服务运营、客户支持等），用户可行使隐私权利。  
- 🌐 **支持平台**：JavaScript、Python、React 等多种语言和框架。

---

### [发现。修复。测试。Sentry 与 Codecov 简介 | Sentry](https://sentry.io/resources/find-fix-test/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=general-fy26q1-bidemo&utm_content=newsletter-nodedemo-seehow)

**原文标题**: [Find. Fix. Test. Intro to Sentry & Codecov | Sentry](https://sentry.io/resources/find-fix-test/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=general-fy26q1-bidemo&utm_content=newsletter-nodedemo-seehow)

Sentry 提供 25 分钟的产品演示，介绍其错误监控、追踪和代码覆盖率功能，帮助开发者提升代码质量和应用性能。

- 🚀 **产品功能**：涵盖错误监控、追踪和代码覆盖率分析，帮助开发者快速定位和修复问题。  
- 🛠 **集成与设置**：支持无代理设置，提供框架级集成，简化部署流程。  
- 🔍 **错误监控**：通过堆栈跟踪、面包屑导航和会话回放，快速调试运行时问题。  
- ⏱ **性能追踪**：检测应用性能瓶颈，从慢渲染或接口问题定位到具体代码。  
- 📊 **代码覆盖率**：在 PR 中分析代码覆盖率，并设置目标以保持代码质量。  
- 📅 **演示安排**：每两周举行一次，适合新用户或需要复习的用户参与。  
- 🔒 **隐私与安全**：明确数据处理政策，用户可管理个人数据权限。  
- 🌐 **多平台支持**：支持 JavaScript、Python、React 等多种语言和框架。

---

### [Scala.js 1.19.0 版本发布](https://www.scala-js.org/news/2025/04/21/announcing-scalajs-1.19.0/)

**原文标题**: [ Announcing Scala.js 1.19.0 - Scala.js](https://www.scala-js.org/news/2025/04/21/announcing-scalajs-1.19.0/)

Scala.js 1.19.0 发布，带来 WebAssembly 性能提升、原生 JavaScript async/await 支持等多项改进。

- 🚀 **Scala.js 1.19.0 发布** - 2025 年 4 月 21 日发布，包含多项性能改进和新功能。
- ⚡ **WebAssembly 性能提升** - 计算密集型代码的 Wasm 输出性能优于 JS 输出，运行时间平均减少 15%。
- 🌐 **浏览器支持** - Firefox（v131+）和 Safari（v18.4+）已全面支持 Scala.js-on-Wasm，Chrome 需启用异常处理标志。
- 🔄 **原生 JavaScript async/await 支持** - 通过 `js.async` 和 `js.await` 实现，需配置为 ES2017 或更高版本。
- 📦 **代码体积优化** - JavaScript 目标的 SAM lambda 代码体积减小，Wasm 支持 JavaScript Promise Integration（JSPI）。
- ⚠️ **兼容性变更** - 移除了非严格浮点数支持，弃用 ECMAScript 5.1 目标，未来版本将完全移除。
- 🛠️ **API 变更** - IR 和链接器 API 有破坏性变更，如 `ir.Trees.Closure` 新增字段。
- 🆕 **新 JDK API 支持** - 新增 `java.util.random.RandomGenerator` 等方法。
- 🐛 **Bug 修复** - 修复了链接器实例测试变更未检测到的问题和并发初始化死锁问题。
- 📚 **文档与社区** - 提供教程、Discord 频道、Stack Overflow 和 GitHub 支持，帮助用户快速上手和解决问题。

---

### [Scala 编程语言](https://www.scala-lang.org/)

**原文标题**: [The Scala Programming Language](https://www.scala-lang.org/)

Scala 是一种多功能编程语言，结合了函数式和面向对象编程风格，适用于构建高效、并发和分布式系统。它拥有丰富的库生态系统，支持跨平台开发，并注重代码安全性和可读性。

- 🚀 **高效表达** - Scala 的现代特性减少代码量，提高生产力，代码更易读。
- 🔄 **可扩展性** - 适用于构建快速、并发和分布式系统，支持 JVM、JavaScript 和 Native 运行时。
- 🔒 **安全性** - 静态类型和内置检查帮助构建安全系统，防止运行时错误。
- 🌍 **广泛应用** - 适用于服务器端开发、高吞吐 HTTP 服务、可靠数据验证和转换。
- ⚡ **并发编程** - 提供可靠的并发代码构建，支持多核和分布式架构。
- 📚 **成熟库生态** - 可结合 Java 和 JavaScript 库，支持多种架构和数据持久化方案。
- 📊 **数据处理** - 支持大数据分析、机器学习、实时计算和可视化。
- 📝 **脚本工具** - Scala CLI 和 Toolkit 简化脚本编写和项目启动。
- 🖥️ **前端开发** - 支持类型安全的响应式 UI，可与 JavaScript 生态互操作。
- 🎓 **教学友好** - 语法简洁，适合初学者和高级软件工程课程。
- 🏢 **维护支持** - 由 Scala Center 维护，得到广泛行业支持。

---

### [Scala.js](https://www.scala-js.org/)

**原文标题**: [Scala.js](https://www.scala-js.org/)

Scala.js 是一个将 Scala 和 JavaScript 生态系统结合的工具，用于开发浏览器、Node.js 和无服务器应用。

- 🚀 **高效性能**：Scala.js 将 Scala 代码优化为高效的 JavaScript，增量编译确保快速编译时间，生成的代码既快又小。
- 🛡️ **强类型保证**：强类型系统避免了常见的错误，如混淆字符串和数字、忘记对象键或方法名拼写错误。
- 🔗 **互操作性**：Scala.js 可以与任何 JavaScript 库无缝集成，包括 React 和 AngularJS，支持静态或动态类型方式。
- ✨ **卓越的编辑器支持**：编辑器能立即捕获拼写和类型错误，无需编译代码，提供代码补全和文档显示。
- 📚 **丰富的语言特性**：支持类、模块、宏等，拥有强大的类型系统和标准库。
- 🌍 **跨语言比较**：与 JavaScript ES5/ES6 和 TypeScript 相比，Scala.js 提供更强大的类型系统和优化编译器。
- 📖 **学习资源**：提供详细的文档、教程和社区支持，如 Discord、Stack Overflow 和 GitHub。

---

### [GitHub - openai/openai-node: OpenAI API 官方 JavaScript/TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

OpenAI 官方提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API，支持多种功能和运行时环境。

- 🚀 **官方库**：OpenAI 提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API。
- 📦 **安装方式**：支持 npm 和 JSR 安装，适用于 Node.js 和 Deno 环境。
- 📄 **功能丰富**：支持文本生成、文件上传、错误处理、自动分页等多种功能。
- ⚡ **流式响应**：支持 Server Sent Events (SSE) 实现流式响应。
- 🔄 **自动重试**：默认对某些错误自动重试 2 次，可配置重试次数。
- ⏱️ **超时设置**：默认请求超时时间为 10 分钟，可自定义配置。
- 🔍 **请求 ID**：每个响应对象包含_request_id，便于调试和报告问题。
- 🌐 **多环境支持**：支持 Node.js、Deno、Bun、Cloudflare Workers 等多种运行时环境。
- ⚠️ **浏览器支持**：默认禁用，需显式设置 dangerouslyAllowBrowser 为 true 启用。
- 🔧 **高级用法**：支持自定义请求、访问原始响应数据、配置 HTTP 代理等。
- 📜 **语义化版本**：遵循 SemVer 规范，保证向后兼容性。
- 🤝 **贡献指南**：欢迎贡献，提供详细的贡献文档。

---

### [API 中推出我们最新的图像生成模型 | OpenAI](https://openai.com/index/image-generation-api/)

**原文标题**: [Introducing our latest image generation model in the API | OpenAI](https://openai.com/index/image-generation-api/)

OpenAI 推出了最新的图像生成模型 gpt-image-1，并将其集成到 API 中，供开发者和企业使用。该模型支持多风格图像生成、精准遵循指令、渲染文本等功能，已被多个行业领先公司采用。  

- 🚀 **模型发布**：gpt-image-1 现已在 API 中全球上线，支持高质量图像生成和编辑。  
- 🌍 **广泛采用**：Adobe、Figma、Quora、Wix 等公司已将其集成到创意工具、电商、教育等产品中。  
- 🎨 **多样化应用**：支持生成广告概念、设计迭代、虚拟模特、缩略图优化等场景。  
- 🔒 **安全措施**：沿用 ChatGPT 的安全防护机制，包括有害内容过滤和 C2PA 元数据标识。  
- 💰 **定价模式**：按 Token 计费，文本输入$5/百万 Token，图像输出$40/百万 Token。  
- 🛠️ **快速上手**：开发者可通过 Playground 体验，并参考图像生成指南集成 API。

---

### [GitHub - nestjs/nest：一个渐进的Node.js框架，用于使用TypeScript/JavaScript构建高效、可扩展且企业级的服务器端应用 🚀](https://github.com/nestjs/nest)

**原文标题**: [GitHub - nestjs/nest: A progressive Node.js framework for building efficient, scalable, and enterprise-grade server-side applications with TypeScript/JavaScript 🚀](https://github.com/nestjs/nest)

NestJS 是一个渐进式 Node.js 框架，用于构建高效、可扩展的企业级服务器端应用，支持 TypeScript/JavaScript，融合了 OOP、FP 和 FRP 编程范式。

- 🚀 **框架特性**：基于 Express/Fastify，提供开箱即用的应用架构，高度可测试、松耦合且易维护。  
- 📚 **多语言文档**：提供英文、中文、韩文、日文等官方指南，方便开发者快速上手。  
- 💬 **社区支持**：通过官方 Discord 频道交流，问题追踪仅限 bug 报告和功能请求。  
- 🤝 **商业支持**：核心团队提供技术咨询、代码审查、迁移策略等付费服务。  
- ⭐ **开源生态**：MIT 许可证，拥有 70.6k+ Stars 和 7.8k+ Forks，638k+ 项目使用。  
- 💡 **技术栈整合**：兼容大量第三方插件，底层可切换 Express 或 Fastify。  
- 🏆 **赞助与贡献**：接受开源赞助，欢迎通过 Issue 和 PR 参与贡献（需遵循规范）。  
- 🌐 **作者与资源**：由 Kamil Myśliwiec 创建，官网提供更多资讯和社区链接。

---

### [发布 electron v36.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v36.0.0)

**原文标题**: [Release electron v36.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v36.0.0)

Electron v36.0.0 发布，包含 Chromium、Node 和 V8 的版本升级，新增多项功能并修复了大量问题。  

- 🚀 **核心升级**：Chromium 升级至 136.0.7103.48，Node 升级至 22.14.0，V8 升级至 13.6。  
- ⚠️ **破坏性变更**：废弃了 `NativeImage.getBitmap()`，移除了 `systemPreferences.isAeroGlassEnabled()` API，并调整了部分 API 的行为。  
- ✨ **新增功能**：  
  - 添加了 `BrowserWindow.isSnapped()` 以检测窗口是否已通过 Snap 排列。  
  - 引入了 `ServiceWorkerMain` 类以在主进程中与服务工作者交互。  
  - 支持 Windows 上的圆角窗口 (`roundedCorners`)。  
- 🛠️ **修复与改进**：  
  - 修复了多个崩溃问题，包括 `shell.readShortcutLink` 和 OSR 渲染问题。  
  - 优化了 ASAR 完整性检查及桌面捕获性能。  
  - 解决了 Linux 和 macOS 上的多个窗口管理和打印问题。  
- 📜 **文档与通知**：更新了文档并结束了对 Electron 33.x.y 的支持。

---

### [发布 8.14.0 版 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/8.14.0)

**原文标题**: [Release 8.14.0 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/8.14.0)

Automattic/mongoose 是一个 MongoDB 的 Node.js 对象模型工具，最新版本 8.14.0 于 2025 年 4 月 25 日发布，包含多项功能更新和修复。

- 🚀 升级 MongoDB 驱动至 6.16 版本 (#15371)  
- 🔍 新增 Query findById 方法支持 (#15337)  
- 📄 子文档支持 schematype 级别的 minimize 选项，可禁用空子文档的最小化 (#15336, #15313)  
- ⚡ 新增 skipOriginalStackTraces 选项以减少堆栈跟踪的性能开销 (#15345, #15194)  
- 🛠 修复 Model.findOneAndUpdate(update) 的问题并修正 TypeScript 类型 (#15365, #15363)  
- 📝 类型修复：正确递归 InferRawDocType (#15357, #14954)  
- 🎯 类型修正：在 toJSON 和 toObject 输出中包含虚拟字段（如果设置了 virtuals: true）(#15346, #15316)  
- 🔧 类型修正：使 init hooks 类型更准确地反映运行时行为 (#15331, #15301)

---

### [GitHub - sindresorhus/file-type: 检测文件、流或数据的文件类型](https://github.com/sindresorhus/file-type)

**原文标题**: [GitHub - sindresorhus/file-type: Detect the file type of a file, stream, or data](https://github.com/sindresorhus/file-type)

file-type 是一个用于检测文件类型的 Node.js 模块，通过检查文件的魔数（magic number）来识别二进制文件格式。它支持多种文件类型，并提供了多种方法来检测文件类型，包括从文件、缓冲区、流或 Blob 中检测。

- 📦 **项目信息**  
  - 项目名称：file-type  
  - 许可证：MIT  
  - 星标：4k  
  - Fork 数：380  

- 🔍 **功能特点**  
  - 通过魔数检测文件类型  
  - 支持多种二进制文件格式  
  - 不支持文本格式（如 .txt、.csv、.svg 等）  

- 📥 **安装**  
  - 使用 npm 安装：`npm install file-type`  
  - 需要 ESM 环境  

- 🛠 **使用方法**  
  - 从文件检测：`fileTypeFromFile`  
  - 从缓冲区检测：`fileTypeFromBuffer`  
  - 从流检测：`fileTypeFromStream`  
  - 从 Blob 检测：`fileTypeFromBlob`  

- 🌐 **浏览器支持**  
  - 支持从 Web 流中检测文件类型  

- 🔧 **API**  
  - `fileTypeFromBuffer`：从缓冲区检测  
  - `fileTypeFromFile`：从文件路径检测  
  - `fileTypeFromStream`：从流检测  
  - `fileTypeFromBlob`：从 Blob 检测  

- 📂 **支持的文件类型**  
  - 包括 3g2、3gp、7z、aac、avi、bmp、docx、gif、jpg、mp3、mp4、pdf、png、zip 等  

- 🔄 **自定义检测器**  
  - 支持通过插件扩展检测能力  
  - 可以添加对非标准或自定义文件类型的支持  

- 🚀 **相关项目**  
  - file-type-cli：此模块的命令行版本  
  - image-dimensions：获取图片尺寸  

- 👥 **维护者**  
  - Sindre Sorhus  
  - Borewit  

- 🔗 **资源**  
  - 文档：README  
  - 许可证：MIT  
  - 行为准则：Code of conduct  
  - 安全策略：Security policy

---

### [GitHub - ranisalt/node-argon2: Argon2 哈希算法的 Node.js 绑定](https://github.com/ranisalt/node-argon2)

**原文标题**: [GitHub - ranisalt/node-argon2: Node.js bindings for Argon2 hashing algorithm](https://github.com/ranisalt/node-argon2)

这是一个关于 Node.js 的 Argon2 哈希算法绑定的项目。

- 🚀 **项目名称**: node-argon2 - Node.js 的 Argon2 哈希算法绑定
- 📦 **NPM 包**: [www.npmjs.com/package/argon2](www.npmjs.com/package/argon2)
- ⭐ **Star 数**: 2k
- 🍴 **Fork 数**: 97
- 📜 **许可证**: MIT license
- 🔧 **功能**: 支持 Argon2i、Argon2d 和 Argon2id（默认）哈希算法，并提供密码验证功能
- 📘 **使用方法**: 
  - 哈希密码：`const hash = await argon2.hash("password");`
  - 验证密码：`await argon2.verify("<hash>", "password");`
- 🔄 **迁移指南**: 提供从其他哈希函数迁移到 Argon2 的步骤
- 💻 **TypeScript 支持**: 内置 TypeScript 类型声明文件
- 🏗️ **预构建二进制文件**: 从 v0.26.0 开始提供，支持多种操作系统和架构
- ⚠️ **安装前准备**: 需要全局安装 node-gyp 和 GCC >= 5 / Clang >= 3.3
- ❓ **常见问题**: 包括手动重建二进制文件、跳过预构建二进制文件等问题的解答
- 👥 **贡献者**: 49 位贡献者
- 🌍 **使用情况**: 被 68.9k+ 项目使用

---

### [GitHub - middyjs/middy: 🛵 时尚的 AWS Lambda Node.js 中间件引擎 🛵](https://github.com/middyjs/middy)

**原文标题**: [GitHub - middyjs/middy: 🛵 The stylish Node.js middleware engine for AWS Lambda 🛵](https://github.com/middyjs/middy)

Middy 是一个时尚的 Node.js 中间件引擎，专为 AWS Lambda 设计，提供简洁的中间件处理方式，支持 JavaScript 和 TypeScript，拥有活跃的社区和丰富的功能。

- 🛵 Middy 是一个专为 AWS Lambda 设计的 Node.js 中间件引擎  
- 📜 采用 MIT 许可证，由 Luciano Mammino 和 Will Farrell 等团队维护  
- 🌐 官方文档可通过 [middy.js.org](https://middy.js.org) 访问  
- ⭐ GitHub 上有 3.8k 星标和 377 个复刻，显示出其受欢迎程度  
- 🔧 支持 JavaScript (88.1%) 和 TypeScript (11.4%)  
- 🛡️ 提供安全策略和代码行为准则，确保项目健康运行  
- 🤝 拥有 199 位贡献者和活跃的社区支持  
- 📦 被 8.9k+ 项目使用，广泛应用于无服务器架构  
- � 最新版本为 6.2.0，发布于 2025 年 4 月 27 日

---

### [茉莉花/发布说明/5.7.0.md 位于 main · jasmine/jasmine · GitHub](https://github.com/jasmine/jasmine/blob/main/release_notes/5.7.0.md)

**原文标题**: [jasmine/release_notes/5.7.0.md at main · jasmine/jasmine · GitHub](https://github.com/jasmine/jasmine/blob/main/release_notes/5.7.0.md)

Jasmine Core 5.7.0 版本发布，包含新功能、文档改进和内部优化，支持多种环境和浏览器版本。

- ⏰ 新增`Clock#autoTick`功能，支持异步自动计时 (#2042, 修复#1725)  
- 📂 将`spec path`以数组形式暴露，便于 IDE 集成等工具精确筛选用例  
- 📝 文档更新：注明`SpecResult#filename`和`SuiteResult#filename`在 zone.js 存在时可能不准确  
- 📊 完善`expectation results`中 expected/actual 属性的文档说明  
- 🔧 内部重构：弃用 Grunt 构建系统，减少老旧依赖  
- 🔍 升级至 eslint 9，移除临时依赖'temp'，更新其他开发依赖  
- 🛠️ 修复 sass 弃用警告，升级 Sauce Connect 至 v5，增强脚本稳定性  
- 🌍 环境支持：测试通过 Node 18/20/22，Safari 15-17，Chrome/Firefox/Edge 最新版等  
- ⚠️ 标注星号版本为"尽力支持"，未来可能视情况放弃维护

---

### [GitHub - chartbrew/chartbrew: 开源 Web 平台，用于从 API、MongoDB、Firestore、MySQL、PostgreSQL 等创建实时报表仪表盘 📈📊](https://github.com/chartbrew/chartbrew)

**原文标题**: [GitHub - chartbrew/chartbrew: Open-source web platform used to create live reporting dashboards from APIs, MongoDB, Firestore, MySQL, PostgreSQL, and more  📈📊](https://github.com/chartbrew/chartbrew)

Chartbrew 是一个开源 Web 应用程序，可直接连接数据库和 API，利用数据创建精美的图表。它提供图表构建器、可编辑仪表板、可嵌入图表、查询和请求编辑器以及团队协作功能。

- 📈 **开源平台**：用于创建实时报告仪表板，支持多种数据源（API、MongoDB、Firestore、MySQL、PostgreSQL 等）。
- 🌐 **在线服务**：Chartbrew 作为服务可通过其官网访问。
- 📚 **详细文档**：提供完整的设置和使用指南。
- 💡 **社区支持**：可通过 Discord 加入讨论或提出想法。
- 🔧 **本地设置**：需要 NodeJS v20、MySQL 或 PostgreSQL 以及 Redis。
- 🐳 **Docker 支持**：提供 Docker 镜像，方便快速部署。
- 🚀 **部署选项**：支持 Render、Heroku 和 Vercel 等多种部署方式。
- 🙏 **贡献者感谢**：项目感谢所有开源贡献者的支持。
- 📊 **功能丰富**：包括图表构建器、可编辑仪表板、团队协作等。

---

### [发布 pnpm 10.10 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.10.0)

**原文标题**: [Release pnpm 10.10 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.10.0)

pnpm 是一个流行的 JavaScript 包管理工具，最新版本为 v10.10.0，包含了一些功能改进和错误修复。

- 🚀 **最新版本**: pnpm 发布了 v10.10.0 版本，包含了一些次要更改和补丁修复。  
- 🔧 **功能改进**: 允许从本地 pnpmfile 加载 `preResolution`、`importPackage` 和 `fetchers` 钩子。  
- 🛠️ **错误修复**:  
  - 修复了 `shellEmulator` 为 `true` 时的 `cd` 命令问题 (#7838)。  
  - 对 `pnpm-workspace.yaml` 中的键进行排序 (#9453)。  
  - 向执行的脚本传递 `npm_package_json` 环境变量 (#9452)。  
  - 修正了 `--reporter=silent` 选项的描述错误。  
- 💖 **社区支持**: 获得了多位赞助商和社区成员的支持与反馈，包括点赞、庆祝和爱心等反应。

---

### [TypeScript 类似 C#](https://typescript-is-like-csharp.chrlschn.dev/)

**原文标题**: [TypeScript is Like C#](https://typescript-is-like-csharp.chrlschn.dev/)

TypeScript和C#均由微软的Anders Hejlsberg 设计，两者在设计和风格上非常相似，掌握其中一门语言后，另一门语言的学习会变得轻松。

- 🧠 设计相似 - TypeScript和C#由同一人设计，风格和结构相近  
- 🔄 学习曲线平缓 - 掌握其中一门语言后，另一门语言更容易上手  
- 💻 微软背景 - 两者均出自微软，共享相似的设计理念

---

### [利用 DuckDB-WASM 通过 SQL 绘制 3D 图形的另类玩法（勉强算吧）](https://www.hey.earth/posts/duckdb-doom)

**原文标题**: [Abusing DuckDB-WASM by making SQL draw 3D graphics (Sort Of)](https://www.hey.earth/posts/duckdb-doom)

概述：作者尝试使用 DuckDB-WASM 和 SQL 在浏览器中构建一个基于文本的 3D Doom 克隆游戏，通过 SQL 查询处理游戏状态和渲染逻辑，展示了 SQL 在非传统用途中的强大能力。

- 🎮 使用 DuckDB-WASM 和 SQL 构建基于文本的 3D Doom 克隆游戏，通过 SQL 查询处理游戏状态和渲染逻辑。
- � 游戏世界完全由数据库表构成，包括地图、玩家坐标、敌人位置等，所有操作通过 SQL 语句实现。
- 🎨 使用 SQL VIEW 进行 3D 渲染，通过递归 CTE 实现光线投射和字符拼接生成 3D 场景。
- 🛠️ JavaScript 负责处理用户输入、游戏循环和精灵渲染，与 SQL 协同工作。
- 🐛 遇到并解决了多个技术挑战，包括 DuckDB-WASM 加载问题、SQL 方言差异、查询规划器限制等。
- ⏱️ 最终性能达到 6-7 FPS，SQL 光线投射视图执行时间约 80-100ms。
- 📚 项目作为学习实验，展示了 SQL 在非传统用途中的强大能力和 DuckDB-WASM 的潜力。
- 💡 作者鼓励其他人尝试这一概念，并思考更多 DuckDB-WASM 的非传统用途。

---

### [p5.js 2.0：你在这里。我们从 p5.js 中学到了什么… | 作者：Kit Kuksenok | Processing 基金会 | 2025 年 3 月 | Medium](https://medium.com/processing-foundation/p5-js-2-0-you-are-here-f827f40519a7)

**原文标题**: [p5.js 2.0: You Are Here. What did we learn from the p5.js… | by Kit Kuksenok | Processing Foundation | Mar, 2025 | Medium](https://medium.com/processing-foundation/p5-js-2-0-you-are-here-f827f40519a7)

p5.js 2.0 即将发布，带来多项新功能和改进，基于 2023 年以来的社区反馈。新版本将支持可变字体、初学者友好的着色器（用 JavaScript 编写）、新的颜色模式（如 OKLCH）等。社区调查显示许多用户对 2.0 版本不太熟悉，因此团队将加强沟通和兼容性支持。1.x 版本将继续支持至 2026 年 8 月，之后 2.0 将成为默认版本。

- 🎨 p5.js 2.0 将引入可变字体、JavaScript 编写的着色器和新的颜色模式（如 OKLCH）。  
- 📊 社区调查显示，许多用户对 2.0 版本不太熟悉，团队将加强沟通和兼容性支持。  
- ⏳ 1.x 版本将继续支持至 2026 年 8 月，之后 2.0 将成为默认版本。  
- 🔄 改进包括文件加载方式和形状处理，同时提供兼容性插件以支持 1.x 风格。  
- 📚 数据结构和表格 API 有所调整，部分功能将被移除，但表格函数保留。  
- 🌍 团队将通过 GitHub、Discourse、社交媒体和线下活动与社区保持沟通。  
- 🗣️ 项目负责人将举办公开办公时间，欢迎社区成员参与讨论。  
- 🔍 透明度是核心原则，团队将持续分享更新并邀请反馈。

---

### [Deno 新闻](https://deno.news/archive/deno-v23-is-almost-here)

**原文标题**: [Deno News](https://deno.news/archive/deno-v23-is-almost-here)

Deno 团队正在为即将发布的 v2.3 版本做最后准备，同时分享了近期生态中的一些亮点和改进。

- 🚀 Deno v2.3 版本即将发布，团队正在完善各项生活质量改进和新功能  
- 🔍 Deno 2.2 版本内置了 OpenTelemetry，显著提升了应用的可观测性  
- 📺 推荐观看 Ry 在 DotJS 巴黎会议上的现场演示视频，展示 OTel 如何自动检测 API  
- 💾 node:sqlite 模块在 v2.2 中引入，方便开发者使用本地或内存数据库  
- 📚 官方文档提供了快速入门的示例  
- 🏆 公布了 Advent with Code 竞赛的获奖者 Justin，他获得了独一无二的 Deno Gold 贴纸  
- 🤔 团队正在考虑未来每年发放 1-2 枚 Gold 贴纸的标准  
- 📢 邀请社区在 Twitter 或 Bluesky 上分享对 v2.3 版本的期待

---

### [免费赠送软件](https://simonwillison.net/2025/Apr/28/give-it-away-for-free/)

**原文标题**: [Giving software away for free](https://simonwillison.net/2025/Apr/28/give-it-away-for-free/)

Simon Willison 的博客讨论了如何通过免费托管静态 HTML 和 JavaScript 来创建完全免费的软件，并推荐了 GitHub Pages 作为最佳选择，同时强调了开源许可和直接可用的链接的重要性。

- 🌐 静态 HTML 和 JavaScript 是目前创建免费软件的最佳交付方式，适合长期维护。  
- 🚀 WebAssembly 扩展了此类交付方式的潜力，支持更多类型的软件。  
- 🐍 Pyodide 使得客户端 Python 应用成为可能。  
- 💡 选择免费托管服务（如 GitHub Pages）可避免长期维护和费用问题。  
- ⚠️ Heroku 等曾经可靠的服务因政策变化不再推荐。  
- 📜 开源许可和直接可用的链接对用户至关重要。  
- 🗓️ 文章发布于 2025 年 4 月 28 日。

---

### [使用 pnpm 和 Yarn 添加 JSR 包](https://deno.com/blog/add-jsr-with-pnpm-yarn)

**原文标题**: [Add JSR packages with pnpm and Yarn](https://deno.com/blog/add-jsr-with-pnpm-yarn)

JSR 现已支持通过 pnpm 和 Yarn 直接安装包，同时兼容 npm 依赖，并允许发布含 JSR 依赖的 npm 包。  

- 🎉 **pnpm 支持**：从 v10.9 开始，可直接通过 `pnpm add jsr:@scope/pkg_name` 安装 JSR 包，并自动更新 `package.json`。  
- 🧶 **Yarn 支持**：自 v4.9.0 起，使用 `yarn add jsr:@scope/pkg_name` 即可安装，同样自动更新依赖配置。  
- 🔗 **兼容性**：支持安装依赖 JSR 的 npm 包，并允许发布此类包到 npm 仓库。  
- 📚 **文档指引**：JSR 包页面已提供 pnpm 和 Yarn 的安装说明，详情可查阅各自官方文档。  
- 🚀 **未来计划**：JSR 将持续优化，开发者可通过 Discord、Twitter/Bluesky/YouTube 关注动态，或参与双周办公会交流。  
- 📢 **近期新闻**：JSR 宣布成立开放治理委员会，并上线 OpenAI 相关包。

---

