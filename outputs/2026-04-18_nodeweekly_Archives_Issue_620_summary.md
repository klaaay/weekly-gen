### [Node 周刊第 620 期：2026 年 4 月 16 日](https://nodeweekly.com/issues/620)

**原文标题**: [Node Weekly Issue 620: April 16, 2026](https://nodeweekly.com/issues/620)

Node Weekly 第 620 期（2026 年 4 月 16 日）聚焦于 Node.js 生态的最新动态，包括 Temporal API 的默认启用、Node.js 24.15.0 LTS 版本的发布，以及一系列开发工具和库的更新。本期还涵盖了安全实践、技术教程、赞助商内容及社区新闻。

- 🕐 Node.js 计划在 V8 14.4 支持后，于 Node 26 中默认启用 Temporal API，以改进 JavaScript 的日期/时间处理。
- 🚀 Node.js 24.15.0 LTS 版本发布，引入了 require(esm) 稳定化、堆大小限制和 OpenSSL 4.0 支持等新功能。
- 🛡️ OWASP 更新了 NPM 安全最佳实践指南，涵盖生命周期脚本禁用、依赖混淆等现代安全议题。
- 🔄 James Coglan 重新审视嵌套 Promise 的用途，通过实际并发问题展示了其价值。
- ⚙️ 简易教程：如何将 C 函数编译为 WebAssembly 并在 Node.js 中运行。
- 📊 赞助商内容：AppSignal 提供 Node.js 应用的全栈监控工具；TimescaleDB 支持在 PostgreSQL 中直接处理分析工作负载。
- 🦠 Pompelmi 1.0 发布，提供基于 ClamAV 的 Node.js 防病毒文件扫描库。
- 📄 officeParser 库新增对常见 Office 格式（如 docx、xlsx）的解析支持。
- 🎵 Audio.js 库支持高级音频处理（如修剪、标准化、和弦检测），无需依赖 ffmpeg。
- 🔍 x-win 工具允许跨平台获取系统窗口信息及进程数据。
- 🖼️ terminal-image 4.3 支持在终端中显示图像，兼容 ANSI 块和全分辨率渲染。
- 🤖 社区新闻：包括 FluidCAD 参数化 CAD 工具、Windows 95 Electron 应用更新、AWS Lambda 数据库连接警告，以及 GitHub 堆叠 PR 功能预览。

---

### [构建：默认启用 Temporal by richardlau · Pull Request #61806 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61806)

**原文标题**: [build: enable Temporal by default by richardlau · Pull Request #61806 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61806)

该 PR 旨在默认启用 Node.js 中的 Temporal 支持，通过自动检测 Rust 工具链（cargo 和 rustc）来实现，若未检测到则发出警告并禁用，同时提供了明确的启用/禁用选项以控制构建行为。

- 🛠️ 默认启用 Temporal 支持，但需依赖 Rust 工具链（cargo 和 rustc）
- ⚠️ 若未指定选项且未检测到 Rust 工具链，会打印警告并禁用 Temporal
- 🚫 新增`--v8-disable-temporal-support`选项以显式禁用 Temporal（无需 Rust）
- ❌ 若传递`--v8-enable-temporal-support`但缺少 Rust 工具链，构建将报错停止
- 🔧 解决了 Windows 平台上的 Temporal 构建问题，并添加了相关构建脚本
- 🚧 针对无 ICU 或共享 ICU 的构建场景，Temporal 支持暂时受限，后续将单独处理
- ✅ 获得了多位核心贡献者的批准，并标记为重大变更（semver-major）

---

### [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

**原文标题**: [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

Temporal 是一个用于处理日期和时间的高级 JavaScript API，旨在替代传统的 Date 对象，提供更强大、更灵活的功能，包括内置时区支持、多种日历系统、时间算术运算和格式化等。

- 🕐 **替代 Date 对象**：Temporal 设计为 Date 的完整替代品，解决了 Date 的诸多缺陷，如时区处理不足、日历系统单一等。
- 🌍 **时区与日历支持**：内置支持多种时区和日历系统（如公历、农历等），允许处理无时区的日历日期和挂钟时间。
- 🧩 **模块化 API 结构**：Temporal 作为命名空间，包含多个类（如 Instant、ZonedDateTime、PlainDate 等），每个类专注于日期时间的不同方面（如时间点、时长、日期等）。
- 🔧 **静态方法与不可变性**：所有 Temporal 方法和属性都是静态的（类似 Math 对象），且对象不可变，避免了副作用。
- 📅 **日历系统灵活性**：支持非公历日历，使用年、月、日、纪元等组件标识日期，并提供了 `monthCode`、`era` 等属性处理不同日历的复杂性。
- ⚙️ **丰富的操作方法**：包括构造、更新、算术运算、舍入、比较和序列化等方法，各类共享相似的接口但针对不同用途优化。
- 🔄 **类间转换**：提供完整的转换方法，允许在不同 Temporal 类（如 Instant、PlainDateTime、ZonedDateTime 等）之间灵活转换。
- 📏 **时间表示范围**：可表示的日期范围约为 ±1 亿天（从 Unix 纪元起），覆盖了绝大多数实际使用场景。
- 📜 **RFC 9557 格式序列化**：支持基于 ISO 8601 的 RFC 9557 格式进行序列化和反序列化，扩展了微秒和纳秒精度及日历标识。
- ⚠️ **浏览器兼容性限制**：Temporal 尚未成为基线功能，部分广泛使用的浏览器不支持，需注意兼容性问题。

---

### [时间范围进入第四阶段 | Igalia](https://www.igalia.com/2026/03/13/Temporal-Reaches-Stage-4.html)

**原文标题**: [Temporal Reaches Stage 4 | Igalia](https://www.igalia.com/2026/03/13/Temporal-Reaches-Stage-4.html)

Temporal 提案在 TC39 第 113 次全体会议上正式进入第 4 阶段，标志着经过九年开发的 JavaScript 新日期时间 API 将取代自 1995 年起存在诸多缺陷的 Date API。该提案由 Igalia 联合主导，获得 Bloomberg 资助，并得到众多贡献者的长期投入。

- 🎉 Temporal 提案历时九年进入 Stage 4，将全面取代 JavaScript 陈旧的 Date API
- 🌍 支持多区域日历（公历、日本历、希伯来历等）并配套 ECMA-402 提案确保跨实现一致性
- 🔧 新增不可变日期时间类型、显式时区处理、纳秒精度及约 4500 项测试用例
- 🤝 Igalia 与 Google 国际化团队合作制定日历标注标准，并推动 RFC 9557 时间格式标准化
- 🚀 已集成于 Firefox v139、Chrome v144 等主流环境，同时提供 polyfill 兼容方案
- 📅 项目历程收录于专题访谈，凝聚数十位工程师与机构长达九年的协作成果

---

### [Node.js — Node.js 24.15.0（长期支持版）](https://nodejs.org/en/blog/release/v24.15.0)

**原文标题**: [Node.js — Node.js 24.15.0 (LTS)](https://nodejs.org/en/blog/release/v24.15.0)

Node.js 24.15.0 LTS（代号“Krypton”）发布，包含多项新功能、性能改进和错误修复，标志着多个实验性功能进入稳定状态，并更新了依赖项。

- 🚀 **CLI 新增选项**：添加了 `--max-heap-size` 和 `--require-module/--no-require-module` 命令行选项。
- 🔐 **加密功能增强**：`KeyObject` API 新增对原始密钥格式的支持，并改进了 WebCrypto 规范兼容性。
- 📁 **文件系统优化**：为 `fs.stat` 和 `fs.promises.stat` 添加了 `throwIfNoEntry` 选项。
- 🌐 **HTTP/2 配置扩展**：新增 `http1Options` 用于配置 HTTP/1 回退行为。
- 📦 **模块系统稳定化**：将 `require(esm)` 和模块编译缓存标记为稳定功能。
- 🔌 **网络功能升级**：为 `Socket` 添加了 `setTOS` 和 `getTOS` 方法。
- 🗃️ **SQLite 改进**：为 `DatabaseSync` 添加了 `limits` 属性，并将 SQLite 模块标记为发布候选版本。
- 🛠️ **诊断与测试工具增强**：为诊断通道添加了 C++ 支持；测试运行器新增了模块模拟的导出选项、暴露工作线程 ID 以及在 SIGINT 时显示被中断的测试。
- ⚡ **性能与内存优化**：改进了 Buffer 操作、事件监听器处理和流处理的性能；更新了 V8、npm、SQLite 等核心依赖项。
- 🐛 **大量错误修复**：涵盖了加密、HTTP、流、ESM 加载器、Zlib 等多个模块的问题修复和稳定性提升。

---

### [Ruby on Rails、Elixir、Node.js 与 Python 应用监控](https://www.appsignal.com/?utm_source=newsletter&utm_medium=paid&utm_campaign=nodeweekly&utm_term=4-16&utm_content=primary)

**原文标题**: [Application Monitoring for Ruby on Rails, Elixir, Node.js & Python](https://www.appsignal.com/?utm_source=newsletter&utm_medium=paid&utm_campaign=nodeweekly&utm_term=4-16&utm_content=primary)

AppSignal 是一款功能全面的应用性能监控（APM）工具，旨在帮助开发者轻松监控应用性能、追踪错误并确保系统稳定运行。它提供八项核心监控功能，支持多种编程语言和框架，安装简便，界面直观，适合开发团队快速部署和使用。

- 🐛 **错误追踪**：实时监控异常，提供详细错误报告和自定义标签，支持发送至问题追踪系统。
- ⚡ **性能监控**：精确测量应用响应时间至纳秒级，分析慢查询和请求，提供时间线追踪。
- 🖥️ **主机监控**：全面监控服务器资源，包括 CPU、磁盘、网络和内存使用情况，支持 Kubernetes。
- 📈 **异常检测**：自定义指标警报，预设关键警报，智能延迟减少误报，支持多渠道通知。
- 🌐 **可用性监控**：全球节点每 30 秒检测应用状态，实时发送宕机通知，提供免费公开状态页。
- 📊 **指标仪表板**：自动生成和自定义仪表板，可视化代码指标，支持图表导出和时间对比。
- 📝 **日志管理**：集中收集和搜索日志，关联错误与性能问题，支持自定义属性记录。
- ⏰ **签到监控**：监控后台任务和计划作业，提供性能洞察和遗漏警报。
- 🔧 **多语言支持**：兼容 Ruby、Elixir、Node.js、JavaScript、Python 等主流语言及框架，扩展性强。
- 🚀 **简易安装**：提供快速安装指南和轻量级代理（基于 Rust），5 分钟内即可开始监控。
- 🤝 **开发者支持**：提供专业的技术支持，符合 GDPR 规范，服务可用性达 99.999%。
- 🆓 **免费试用**：提供 30 天全功能免费试用，无需信用卡，所有计划包含完整功能。

---

### [NPM 安全 - OWASP 速查表系列](https://cheatsheetseries.owasp.org/cheatsheets/NPM_Security_Cheat_Sheet.html)

**原文标题**: [NPM Security - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/NPM_Security_Cheat_Sheet.html)

OWASP Cheat Sheet Series 提供了全面的安全指南，其中 NPM 安全最佳实践部分为 JavaScript 和 Node.js 开发者详细介绍了保护 npm 包和依赖管理的具体措施，涵盖从避免泄露密钥到防御供应链攻击的多个关键领域。

- 🔐 避免在 npm 注册表中发布密钥：利用 .gitignore、.npmignore 和 package.json 中的 files 属性控制文件包含，发布前使用 --dry-run 预览
- 🔒 强制执行锁文件：使用 npm ci 或 yarn install --frozen-lockfile 确保依赖版本一致，防止意外变更
- 🛡️ 最小化攻击面：通过 --ignore-scripts 禁用第三方包脚本执行，使用 @lavamoat/allow-scripts 插件创建生命周期脚本白名单
- 📊 评估项目健康：使用 npm outdated 检查依赖更新，npm doctor 诊断 npm 环境状态
- 🔍 审计开源依赖漏洞：持续扫描和监控第三方包的安全漏洞，整合到开发全生命周期
- 🏗️ 工件治理与供应链保护：使用本地 npm 代理（如 Verdaccio），生成 SBOM，签名工件，限制 CI 令牌，自动化监控
- 🕵️ 负责任地披露安全漏洞：遵循协调披露流程，在公开前与维护者协作修复
- 🔑 启用双因素认证：为 npm 账户开启 2FA，增强登录和写操作的安全性
- 🎫 使用 npm 作者令牌：创建受限令牌（如只读、IP 范围限制），定期管理和撤销
- 🧠 防御仿冒攻击：警惕 typosquatting（利用拼写错误）和 slopsquatting（利用 AI 幻觉包名）攻击，安装前验证包名和元数据
- 📦 使用可信发布者：通过 OIDC 配置 CI/CD 工作流进行安全发布，自动生成来源证明
- 🚫 防止依赖混淆攻击：为内部包使用作用域名称，配置 .npmrc 指向私有注册表，在公共注册表预留包名

---

### [嵌套承诺的用途——If Works](https://blog.jcoglan.com/2026/03/23/uses-for-nested-promises/)

**原文标题**: [Uses for nested promises – The If Works](https://blog.jcoglan.com/2026/03/23/uses-for-nested-promises/)

本文探讨了 JavaScript 中 Promise.then() 隐式扁平化嵌套 Promise 的设计决策，回顾了与函数式编程中单子（monad）理论的争议，并通过实际并发控制案例展示了嵌套 Promise 的潜在用途。

- 🧠 **Promise.then() 的设计争议**：函数式编程者曾建议区分 map 和 flatMap 以符合单子理论，但 Promises/A+ 规范选择了隐式扁平化嵌套 Promise，主要基于便利性考虑。
- 🔄 **单子与函子的区别**：单子（如 flatMap）会扁平化嵌套容器（如 Array<Array<T>>变为 Array<T>），而函子（如 map）则保持嵌套结构，Promise.then() 同时支持两种行为导致类型模糊。
- ⚙️ **嵌套 Promise 的实际用例**：在实现读写锁（RWLock）时，通过嵌套 Promise 避免内部队列阻塞，从而允许并发读取操作，展示了在并发控制中嵌套 Promise 的实用性。
- 🛠️ **并发控制中的关键机制**：使用嵌套 Promise 配合队列（Queue）实现读写锁，确保检查队列空状态和添加任务为原子操作，同时不阻塞后续任务调度。
- 📚 **历史与反思**：作者最初支持规范决策，但在开发加密数据库 EscoDB 时遇到并发场景，重新认识到嵌套 Promise 在管理异步执行顺序中的价值。

---

### [Promises/A+](https://promisesaplus.com/)

**原文标题**: [Promises/A+](https://promisesaplus.com/)

Promises/A+ 是一个为 JavaScript 承诺（Promise）制定的开放标准，旨在确保不同实现的互操作性。它详细规定了 `then` 方法的行为，定义了承诺的状态、`then` 方法的调用规则以及承诺解析过程，为异步操作提供了一致的基础。

- 📜 **标准性质**：Promises/A+ 是一个开放、稳定的 JavaScript Promise 标准，由实现者制定，旨在确保不同 Promise 实现之间的互操作性。
- 🔄 **Promise 状态**：Promise 必须处于 pending（进行中）、fulfilled（已成功）或 rejected（已失败）三种状态之一，且状态一旦从 pending 转变，便不可更改。
- ⚙️ **then 方法规范**：`then` 方法用于注册成功（`onFulfilled`）和失败（`onRejected`）的回调，这些回调在 Promise 状态确定后异步执行，且必须遵循调用顺序和次数限制。
- 🔗 **链式调用与返回**：`then` 方法必须返回一个新的 Promise，其状态由回调函数的返回值或抛出的异常决定，支持链式调用和值传递。
- 🔄 **Promise 解析过程**：定义了一个抽象的解析过程 `[[Resolve]](promise, x)`，用于处理回调返回值 `x`，包括处理 thenable 对象、递归解析及避免循环引用。
- ⏳ **异步执行保证**：`onFulfilled` 和 `onRejected` 回调必须在执行栈清空后异步调用，确保非阻塞行为，可通过宏任务或微任务机制实现。
- 📝 **历史与范围**：该标准基于早期的 Promises/A 提案，澄清并扩展了行为条款，但核心规范不涉及 Promise 的创建、履行或拒绝方式，这些可能由配套规范补充。

---

### [融入单子与范畴理论 · Issue #94 · promises-aplus/promises-spec · GitHub](https://github.com/promises-aplus/promises-spec/issues/94)

**原文标题**: [Incorporate monads and category theory · Issue #94 · promises-aplus/promises-spec · GitHub](https://github.com/promises-aplus/promises-spec/issues/94)

该 GitHub 议题讨论了在 Promise 规范中引入函数式编程概念，特别是单子（Monad）和范畴论，以提升模块化。

- 🧠 议题提议将 Promise 规范与函数式编程结合，通过三个 API 变更增强模块化
- 📚 建议阅读相关文章，了解基于范畴论改进 Promise 设计的思路
- 🔧 具体变更包括：`Promise.of(a)` 转换任意值为 Promise、`Promise#then(f)` 只接受一个函数、将`onRejected`移至原型
- 💬 更多讨论可参考相关链接，议题已关闭但留下了技术探讨空间

---

### [GitHub - peterc/webassembly-simplest-demo: 一个将 C 语言编译为 WebAssembly 并运行的简单示例 · GitHub](https://github.com/peterc/webassembly-simplest-demo)

**原文标题**: [GitHub - peterc/webassembly-simplest-demo: A simple example of compiling C to WebAssembly and running it · GitHub](https://github.com/peterc/webassembly-simplest-demo)

这是一个关于如何将 C 语言函数编译为 WebAssembly 并在 Node.js 和浏览器中运行的最小化示例项目。

- 🎯 项目提供了一个从 C 语言到 WebAssembly 的最简流程，无需 Emscripten 或打包工具
- 🖥️ 支持在 macOS 和现代 Linux 发行版上运行，需要安装支持 wasm32 目标的 clang 和 lld 链接器
- 📝 示例包含一个计算斐波那契数列的 C 函数（fib.c）
- 🔧 通过 Makefile 或直接命令编译 C 代码为 WebAssembly 模块
- ⚡ 可在 Node.js 或 Bun 中直接运行，也可在浏览器中通过 HTTP 服务使用
- 📚 项目包含完整的代码文件和详细的 README 说明文档
- 🔗 提供了更深入学习的资源推荐，包括 Surma 的详细教程

---

### [构建 Rust 运行时给 TypeScript 带来的启示——Encore 博客](https://encore.dev/blog/rust-runtime)

**原文标题**: [What We Learned Building a Rust Runtime for TypeScript – Encore Blog](https://encore.dev/blog/rust-runtime)

Encore 团队耗时两年、编写了 6.7 万行 Rust 代码，为 TypeScript 构建了一个与 Node.js 在同一进程中协同工作的运行时，将基础设施逻辑从 JavaScript 业务代码中分离，以实现高性能和跨语言扩展。

- 🚀 **性能与多线程优势**：将 HTTP 请求生命周期、数据库连接、消息队列等基础设施移至 Rust（基于 tokio），克服 Node.js 单线程限制，显著提升并发处理能力。
- 🔗 **进程内集成替代侧车方案**：早期考虑用 Go 运行时作为 Node.js 的侧车进程，但因 IPC 序列化延迟和运维复杂度高而放弃，最终选择通过 Rust 的 N-API 在进程内直接集成。
- 🏗️ **双配置驱动架构**：运行时通过“应用元数据”（编译时从 TypeScript 代码提取）和“运行时配置”（部署时按环境生成）分离业务逻辑与环境细节，支持灵活部署。
- 🔄 **Rust 与 JavaScript 双向通信**：通过改进 napi-rs 的`ThreadSafeFunction`，实现从 Rust 调用 JavaScript 函数并捕获返回值（包括异步 Promise），确保消息确认与响应回传。
- 🛡️ **取消保护机制**：通过`CancellationGuard`处理 Rust future 被意外丢弃时 JavaScript 逻辑仍运行的问题，确保追踪链路完整性和资源清理。
- 🌐 **嵌入式 API 网关**：使用 Cloudflare 的 Pingora 库在运行时内嵌网关，实现认证、路由等功能，避免独立代理进程的序列化开销，并支持 TypeScript 身份验证器直接运行。
- ☁️ **多云抽象设计**：通过特质对象（而非泛型）统一封装 NSQ、GCP Pub/Sub和AWS SNS/SQS的差异，使业务代码无需感知底层云提供商。
- 📊 **自定义二进制追踪协议**：采用高效二进制编码（而非 JSON/Protobuf）记录全链路追踪数据，结合时间锚点避免时钟偏移，并支持可配置的采样策略。
- 🔍 **TypeScript 解析器**：基于 SWC 构建独立 Rust 工具，从源码提取框架声明（如数据库、API 端点），生成结构化元数据供运行时使用，支撑文档生成与架构图。
- 📈 **性能成果显著**：基准测试显示，Encore.ts 的吞吐量可达 Express.js 的 9 倍，P99 延迟降低 80%，尤其在启用验证时优势更明显。
- 🤔 **经验与反思**：应更早定义结构化错误类型、优先支持 OpenTelemetry 标准、加强快照测试，并探索用同一 Rust 运行时支持 Go 语言（目前因 GC 边界问题尚未实现）。

---

### [使用 Node.js、TypeScript 和 MongoDB 构建电影观看清单](https://www.thepolyglotdeveloper.com/2026/04/build-movie-watchlist-nodejs-typescript-mongodb/)

**原文标题**: [Build a Movie Watchlist with Node.js, TypeScript, and MongoDB](https://www.thepolyglotdeveloper.com/2026/04/build-movie-watchlist-nodejs-typescript-mongodb/)

本教程详细介绍了如何使用 Node.js、TypeScript 和 MongoDB 构建一个电影待看清单 API。通过利用 MongoDB 的文档数据库特性、全文搜索功能以及合理的模式设计，实现了一个包含电影搜索、待看清单管理（添加、激活/去激活、评分）等核心功能的 REST API。项目采用 Express 框架，通过单例模式管理数据库连接，并演示了如何通过数据反规范化优化查询性能。

- 🎬 使用 Node.js、TypeScript、Express 和 MongoDB 构建电影待看清单 API，支持 JSON 端到端数据处理。
- 🔍 利用 MongoDB Search 实现全文搜索，通过`$search`阶段在聚合管道中搜索电影的标题和剧情字段。
- 🛠️ 项目初始化包括安装依赖（Express、MongoDB 驱动、TypeScript 等）、配置 TypeScript 和环境变量（如 MongoDB 连接 URI）。
- 🗄️ 采用单例模式管理 MongoDB 连接，确保应用启动时建立连接并创建唯一索引（如`movieId`），以优化资源使用和关闭。
- 📄 定义 TypeScript 接口描述待看清单文档结构，反规范化存储电影标题和海报，避免频繁联表查询提升性能。
- 📈 实现电影搜索路由，通过聚合管道使用 MongoDB Search 索引，限制结果数量并投影关键字段返回给客户端。
- ➕ 待看清单管理包括添加电影（检查现有记录、激活或插入新文档）、列表查询（支持按激活状态筛选和排序）。
- ⭐ 支持对待看清单中的电影进行评分（PATCH 端点验证 1-5 分整数）和移除评分（DELETE 端点使用`$unset`操作符）。
- 🗑️ 实现软删除功能，通过将文档的`active`字段设置为`false`来去激活电影，而非物理删除数据。
- 🚀 应用配置 Express 中间件、路由和错误处理，添加健康检查端点，并实现优雅关闭逻辑以关闭服务器和数据库连接。

---

### [pompelmi — Node.js 防病毒扫描](https://pompelmi.app/)

**原文标题**: [pompelmi — Node.js antivirus scanning](https://pompelmi.app/)

pompelmi 是一个极简的 Node.js 封装库，用于通过 ClamAV 进行跨平台、零配置的本地文件病毒扫描。它无需守护进程或云服务，直接调用系统安装的 ClamAV 命令行工具，提供类型安全的扫描结果。

- 🛡️ **核心功能**：提供 `scan()` 函数，直接扫描文件并返回类型化的判定结果（`Verdict.Clean`、`Verdict.Malicious` 或 `Verdict.ScanError`）。
- 📦 **零依赖**：仅使用 Node.js 内置的 `child_process` 模块调用 `clamscan`，无任何运行时依赖。
- 🌐 **跨平台支持**：支持 macOS、Linux 和 Windows 系统，前提是系统中已安装 ClamAV。
- ⚙️ **自动检测**：自动检查 ClamAV 是否已安装及病毒库是否存在，避免重复安装或更新。
- 🐳 **容器化支持**：提供 Docker 集成方案，可在容器中运行 ClamAV 进行扫描。
- 📚 **完整文档**：包含快速入门、API 参考、架构说明及故障处理指南。

---

### [ClamAVNet](https://www.clamav.net/)

**原文标题**: [ClamAVNet](https://www.clamav.net/)

ClamAV 是一款开源防病毒引擎，用于检测木马、病毒、恶意软件等威胁，提供高性能扫描和自动更新功能。

- 🛡️ ClamAV 是一款开源防病毒引擎，可检测木马、病毒和恶意软件等威胁
- 📥 最新稳定版本为 1.5.2，支持邮件网关扫描
- ⚡ 包含多线程扫描守护进程和命令行工具，支持自动签名更新
- 🔄 支持多种文件格式、签名语言及文件解压功能
- 🌐 提供适用于各操作系统的开源版本，代码托管于 GitHub
- ©️ 由 Cisco 及其附属公司维护，遵循特定许可协议

---

### [发布 v1.0.0：首个稳定版本 · pompelmi/pompelmi · GitHub](https://github.com/pompelmi/pompelmi/releases/tag/1.0.0)

**原文标题**: [Release v1.0.0: Initial Stable Release · pompelmi/pompelmi · GitHub](https://github.com/pompelmi/pompelmi/releases/tag/1.0.0)

这是 Pompelmi 项目的首个稳定版本发布页面，标志着该项目已进入生产就绪阶段。

- 🚀 **首个稳定版本发布**：Pompelmi 项目发布了 1.0.0 版本，这是其第一个正式稳定版本，核心架构已针对生产环境最终确定。
- ⚠️ **旧版本弃用通知**：所有之前的 0.x 版本现已严格弃用，不再维护，被视为不稳定版本，禁止在生产环境中使用，强烈建议用户立即迁移至 1.0.0。
- 🔧 **主要新增内容**：包括最终确定的生产就绪 API 和功能集、增强的核心稳定性与性能优化，以及严格遵循语义化版本规范（SemVer）的正式版本控制。
- 📜 **详细变更查看**：建议用户查看提交历史记录以获取所有变更的详细说明。

---

### [GitHub - pompelmi/pompelmi: 极简 Node.js ClamAV 封装器 — 扫描任意文件并获取清洁、恶意或扫描错误结果。自动处理安装和数据库更新。· GitHub](https://github.com/pompelmi/pompelmi)

**原文标题**: [GitHub - pompelmi/pompelmi: Minimal Node.js wrapper around ClamAV — scan any file and get Clean, Malicious, or ScanError. Handles installation and database updates automatically. · GitHub](https://github.com/pompelmi/pompelmi)

pompelmi 是一个极简的 Node.js 封装库，用于调用 ClamAV 扫描文件，返回类型化的检测结果（清洁、恶意或扫描错误），无需守护进程、云端服务或原生绑定，且零运行时依赖。

- 🛡️ **核心功能**：通过 `clamscan` 或远程 `clamd` 扫描文件，返回 `Verdict.Clean`、`Verdict.Malicious` 或 `Verdict.ScanError` 三种符号化结果。
- 📦 **快速上手**：通过 `npm install pompelmi` 安装，使用 `scan()` 函数即可进行文件扫描，支持本地与远程扫描模式。
- 🔧 **工作原理**：验证文件路径后，生成子进程执行 `clamscan`，根据退出码映射结果，避免解析输出或使用正则表达式。
- 🌐 **远程与 Docker 支持**：可通过配置 `host` 和 `port` 选项连接远程或 Docker 容器中的 ClamAV 服务进行扫描。
- 📚 **丰富示例**：提供多种应用场景示例，如上传扫描、错误处理、多文件扫描、目录递归扫描及与 S3 等服务的集成。
- ⚙️ **内部工具**：包含 `ClamAVInstaller()` 和 `updateClamAVDatabase()` 等实用函数，支持在 macOS、Linux 和 Windows 上自动安装 ClamAV 并更新病毒数据库。
- 🧪 **测试与贡献**：包含单元测试与集成测试，支持通过 GitHub 贡献代码，并提供了行为准则和安全政策指引。
- 📄 **许可证与资源**：采用 ISC 许可证，项目文档详尽，涵盖 API 参考、Docker 配置及多平台安装指南。

---

### [officeParser | Node.js 与浏览器中最通用的办公文档解析器](https://officeparser.harshankur.com/)

**原文标题**: [officeParser | The Most Versatile Office Parser for Node.js & Browser](https://officeparser.harshankur.com/)

一款功能强大的开源文档解析库，支持多种办公文档格式，提供结构化数据提取和高性能处理能力。

- 📦 **广泛使用** - 每周下载量超过 26 万次，总下载量突破 1000 万次
- 🧩 **格式全面** - 支持 DOCX、XLSX、PPTX、PDF 等 8 种以上办公文档格式
- 🌳 **结构化解析** - 生成抽象语法树（AST），保留文档原始层次结构
- 📎 **附件提取** - 可提取文档中嵌入的图像、图表等附件资源
- 🔍 **OCR 集成** - 通过 Tesseract.js 支持图像文字识别功能
- ℹ️ **元数据获取** - 提取文档属性、作者信息、创建日期等完整元数据
- ⚡ **高性能设计** - 同时优化服务器端处理和浏览器端使用体验
- ⚙️ **高度可配置** - 支持分隔符、注释处理、解析深度等自定义设置
- 🛠️ **开发友好** - 提供可视化工具、详细技术文档和调试指南
- 🔄 **兼容性强** - 完美处理传统和现代办公文档标准的复杂结构

---

### [GitHub - harshankur/officeParser：一个健壮、严格类型的Node.js与浏览器库，用于解析办公文件（docx、pptx、xlsx、odt、odp、ods、pdf、rtf）。它能生成清晰、分层的抽象语法树（AST），包含丰富的元数据、文本格式以及完整的附件支持。· GitHub](https://github.com/harshankur/officeParser)

**原文标题**: [GitHub - harshankur/officeParser: A robust, strictly-typed Node.js and Browser library for parsing office files (docx, pptx, xlsx, odt, odp, ods, pdf, rtf). It produces a clean, hierarchical Abstract Syntax Tree (AST) with rich metadata, text formatting, and full attachment support. · GitHub](https://github.com/harshankur/officeParser)

officeParser 是一个用于解析 Office 文件的强大、严格类型的 Node.js 和浏览器库，支持多种格式并生成包含丰富元数据和附件的抽象语法树。

- 📦 **支持多种文件格式** – 可解析 docx、pptx、xlsx、odt、odp、ods、pdf 和 rtf 文件。
- 🌳 **生成抽象语法树** – 输出结构化的 AST，包含层次化内容、文本格式和完整元数据。
- 🌐 **提供交互式可视化工具** – 可通过在线 AST 可视化器实时上传文件并查看解析结果。
- 📥 **多种安装与使用方式** – 支持通过 npm 安装、命令行调用，以及在 Node.js 和浏览器环境中使用。
- ⚙️ **丰富的配置选项** – 可设置忽略注释、启用 OCR、提取附件、自定义换行符等多种解析参数。
- 🔧 **强大的 AST 操作功能** – 支持直接访问结构化数据，如提取图片、查找标题、转换格式等。
- 🖼️ **附件与 OCR 支持** – 可提取图像和图表为 Base64，并支持通过 OCR 识别图像中的文字。
- 📄 **跨平台兼容** – 在 Node.js 中可处理文件路径或 Buffer，在浏览器中可处理 ArrayBuffer 或 Uint8Array。
- 🛠️ **包含问题排查与资源管理** – 提供 OCR 工作池管理、PDF 工作线程配置及常见问题解决方案。

---

### [TimescaleDB — 排名第一的时序数据库 | 泰格数据](https://www.tigerdata.com/timescaledb?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是一款基于 Postgres 构建的开源时序数据库，专为处理传感器、链上及客户数据设计，提供实时分析、高效压缩和自动管理功能，适用于初创公司和企业。

- 🚀 高性能时序处理：支持自动分区（Hypertables）、行列混合存储，实现快速数据写入与查询，压缩率高达 95%
- 🔄 智能数据管理：具备增量物化视图、自动化列存储与保留策略，内置任务调度器，简化运维
- 📊 丰富分析功能：提供约 200 个原生 SQL 超函数，支持时间加权平均、插值等高级时序分析
- 🌐 企业级应用案例：被 Cloudflare、Replicated 等企业用于处理海量数据，平衡性能与 Postgres 生态兼容性
- 🛠️ 开源与社区驱动：拥有 2.2 万 + GitHub 星标和 1.2 万 + Slack 社区成员，支持 Helm 快速部署
- 💡 多行业适配：适用于加密货币、能源遥测、油气运营等领域，提供云平台和开发者工具支持

---

### [GitHub - AdamPerlinski/micro-ml：适用于JS的微型机器学习与统计库——约56KB压缩包内含16种算法。基于Rust/WASM，零依赖。· GitHub](https://github.com/AdamPerlinski/micro-ml)

**原文标题**: [GitHub - AdamPerlinski/micro-ml: Tiny ML & statistics library for JS — 16 algorithms in ~56KB gzipped. Rust/WASM, zero dependencies. · GitHub](https://github.com/AdamPerlinski/micro-ml)

micro-ml 是一个轻量级机器学习库，专为简单预测任务设计，无需大型神经网络库，提供多种算法用于回归、平滑、预测等场景。

- 📦 **轻量高效** – 库体积约 56KB（gzip），包含 8 种机器学习算法，基于 WASM 实现，在典型数据集上运行时间低于毫秒级。
- 📈 **功能丰富** – 支持线性回归、多项式回归、指数回归等多种回归方法，以及数据平滑、未来值预测、分类、聚类和降维。
- 🔍 **实用场景** – 适用于销售预测、股票趋势线绘制、体重预测、传感器数据平滑、增长率分析和异常检测等实际应用。
- ⚡ **性能优异** – 在 Node.js 中基准测试显示，处理大规模数据时速度较快，例如线性回归 10 万点仅需 0.9 毫秒。
- 🛠️ **易于使用** – 通过 npm 安装，提供简洁的 API，支持浏览器和 Node.js 环境，并附带详细的 API 参考和示例代码。

---

### [GitHub - audiojs/audio：高级音频处理库 · GitHub](https://github.com/audiojs/audio)

**原文标题**: [GitHub - audiojs/audio: High-level audio manipulations · GitHub](https://github.com/audiojs/audio)

audio.js 是一个高级音频处理库，提供播放、分析和编辑功能，支持多种音频格式，适用于浏览器、Node.js、Deno 和 Bun 等平台。

- 🎧 **支持多种格式** – 使用 WASM 编解码器，无需 ffmpeg，支持 WAV、MP3、FLAC、OGG 等格式。
- 🔄 **非破坏性编辑** – 所有编辑操作（如裁剪、增益、混音）均为虚拟编辑，可即时撤销。
- 📊 **音频分析** – 提供响度、频谱、节拍、音高、和弦、调性等分析功能。
- 🌐 **跨平台** – 可在浏览器、Node.js、Deno 和 Bun 中运行，提供统一的 API。
- 🛠️ **模块化设计** – 支持插件化操作和树摇优化，可按需加载编解码器。
- 🎛️ **命令行工具** – 提供 CLI 支持播放、Unix 管道和标签自动补全。
- 📈 **流式处理** – 支持在解码过程中进行播放和编辑，无需等待完整文件加载。
- 🧠 **音频优先单位** – 使用 dB、Hz、LUFS 等音频单位，而非字节和索引。

---

### [GitHub - audiojs/web-audio-api: Web 音频 API 的便携式实现 · GitHub](https://github.com/audiojs/web-audio-api)

**原文标题**: [GitHub - audiojs/web-audio-api: Portable implementation of Web audio API · GitHub](https://github.com/audiojs/web-audio-api)

这是一个用于 Node.js 环境的 Web Audio API 实现，提供完整的 API 兼容性，支持离线渲染和服务器端音频处理，无需浏览器环境即可运行。

- 🎵 **纯 JavaScript 实现** – 无需原生依赖，完全遵循 Web Audio API 标准，通过 WPT 一致性测试。
- 🔧 **多环境适用** – 支持 CLI 脚本、服务器端音频生成、CI 环境离线渲染，以及 Tone.js 等库的无缝集成。
- 📦 **简单安装使用** – 通过`npm install web-audio-api`安装，导入后即可创建音频上下文和节点。
- 🎛️ **内置扬声器输出** – 通过`audio-speaker`提供即时的扬声器输出，无需额外配置。
- 💾 **离线音频渲染** – 使用`OfflineAudioContext`生成音频缓冲区，适合文件处理和单元测试。
- 🧪 **丰富示例库** – 包含测试信号、听觉错觉、合成器、生成式音乐等多种示例，支持参数化调用。
- 🔌 **Node.js 扩展功能** – 提供`addModule(fn)`、自定义输出流、音频格式控制等浏览器外特有功能。
- ❓ **完整 FAQ 支持** – 涵盖上下文管理、Tone.js 集成、音频文件解码、性能测试等常见问题解答。
- 🏗️ **模块化架构** – 采用拉取式音频图设计，DSP 内核与图形逻辑分离，为 WASM 优化预留空间。
- 📄 **MIT 许可证** – 开源项目，拥有活跃的社区维护和持续更新。

---

### [GitHub - miniben-90/x-win：此软件包可让您获取Windows、MacOS和Linux上活动及打开窗口的精确信息，包括窗口位置、大小、标题及其他内存数据。· GitHub](https://github.com/miniben-90/x-win)

**原文标题**: [GitHub - miniben-90/x-win: This package allows you to retrieve precise information about active and open windows on Windows, MacOS, and Linux. You can obtain the position, size, title, and other memory of windows. · GitHub](https://github.com/miniben-90/x-win)

这是一个基于 Rust 和 napi-rs 开发的跨平台 Node.js 包，用于获取当前活动窗口或所有打开窗口的详细信息，支持 Windows、Linux 和 macOS 系统。

- 🖥️ **跨平台支持**：兼容 Windows 10/11、Linux（X服务器或Gnome≤45）和macOS 10.6+ 系统
- 📦 **安装简便**：可通过 npm 或 yarn 安装`@miniben90/x-win`包
- 🔍 **核心功能**：提供`activeWindow`和`openWindows`方法，分别获取当前活动窗口和所有窗口的详细信息，包括窗口 ID、标题、进程信息、位置尺寸等
- 🔄 **异步支持**：所有方法均提供同步和异步版本（如`activeWindowAsync`）
- 🔔 **实时订阅**：可通过`subscribeActiveWindow`订阅活动窗口变化，每 100 毫秒检测一次
- 🖼️ **图标提取**：支持从窗口信息中提取图标，返回 base64 格式的 PNG 数据
- 🌐 **浏览器 URL 获取**：在 Windows 和 macOS 上可获取浏览器窗口的 URL（支持 Chrome、Edge、Firefox 等主流浏览器）
- ⚠️ **平台注意事项**：Linux 需安装 XCB 开发库；macOS 需授予屏幕录制权限；Wayland 需安装特定 GNOME 扩展
- 🛠️ **开发集成**：提供 Electron 应用集成建议，推荐在 Worker 线程中执行操作以避免崩溃
- 📚 **项目参考**：灵感来源于`active-win`和`active-win-pos-rs`项目，使用`@napi-rs/cli`生成

---

### [GitHub - sindresorhus/terminal-image：在终端中显示图像 · GitHub](https://github.com/sindresorhus/terminal-image)

**原文标题**: [GitHub - sindresorhus/terminal-image: Display images in the terminal · GitHub](https://github.com/sindresorhus/terminal-image)

这是一个名为 terminal-image 的 Node.js 库，用于在终端中显示图像，支持多种终端协议和图像格式，包括静态图片和动态 GIF。

- 🖼️ 支持在终端中显示 PNG、JPEG 和 GIF 图像，根据终端能力自动选择最佳渲染协议
- 🔧 提供灵活的 API，包括 `terminalImage.buffer()` 和 `terminalImage.file()` 等方法，支持自定义高度、宽度和宽高比
- 🖥️ 兼容多种终端：在 iTerm、Kitty 等支持图形的终端中显示全分辨率图像，在其他终端中使用 ANSI 块字符回退
- ⚙️ 可配置选项丰富，包括图像缩放、是否保持宽高比、首选原生渲染等，GIF 还支持最大帧率和自定义渲染处理
- 📦 可通过 npm 安装，提供相关工具如 terminal-image-cli，并支持显示远程图像

---

### [GitHub - CodeIntelligenceTesting/jazzer.js：适用于Node.js的覆盖引导式进程内模糊测试工具 · GitHub](https://github.com/CodeIntelligenceTesting/jazzer.js)

**原文标题**: [GitHub - CodeIntelligenceTesting/jazzer.js: Coverage-guided, in-process fuzzing for Node.js · GitHub](https://github.com/CodeIntelligenceTesting/jazzer.js)

Jazzer.js 是一个由 Code Intelligence 开发的 Node.js 平台覆盖引导、进程内模糊测试工具，基于 libFuzzer，为 JavaScript 生态系统带来基于插桩的变异功能。

- 🚀 **快速开始**：通过安装 `@jazzer.js/core` 依赖、创建模糊测试目标并运行 `npx jazzer` 即可开始使用。
- 🔗 **Jest 集成**：推荐与 Jest 测试框架集成，支持在本地或 CI 中执行模糊测试，并具备 IDE 调试支持。
- 🎯 **模糊测试目标**：可通过 CLI 创建和执行模糊测试目标，适合集成到 CI 流程中，支持 ES 模块。
- 📚 **详细文档**：提供完整的文档和演示视频，帮助用户快速上手和深入了解工具功能。
- 🖥️ **多平台支持**：支持 Linux、macOS 和 Windows 的 Node.js LTS 版本。
- 💡 **灵感来源**：受同名 Java 模糊测试工具 Jazzer 启发，专为 Node.js 设计。

---

### [libFuzzer —— 一个用于覆盖率引导模糊测试的库。 — LLVM 23.0.0git 文档](https://llvm.org/docs/LibFuzzer.html)

**原文标题**: [libFuzzer â a library for coverage-guided fuzz testing. — LLVM 23.0.0git documentation](https://llvm.org/docs/LibFuzzer.html)

libFuzzer 是一个基于 LLVM 的进程内、覆盖率引导的进化式模糊测试引擎，它通过链接被测库并持续生成变异输入来最大化代码覆盖率，主要用于发现软件中的安全漏洞和稳定性问题。

- 🧪 **核心功能**：libFuzzer 是一个进程内、覆盖率引导的模糊测试引擎，通过进化算法生成输入以最大化代码覆盖率。
- 🔗 **集成方式**：与测试库链接，通过目标函数`LLVMFuzzerTestOneInput`传递模糊输入，依赖 LLVM 的 SanitizerCoverage 插桩收集覆盖率信息。
- 🛠️ **使用步骤**：编写模糊目标函数，使用 Clang 的`-fsanitize=fuzzer`标志编译，并配合地址消毒剂（ASAN）等工具增强错误检测。
- 📁 **语料库管理**：初始语料库可包含有效和无效的样本输入，支持通过`-merge=1`合并和最小化语料库以优化覆盖率。
- ⚙️ **运行与并行**：可单进程运行或通过`-jobs`和`-workers`选项并行执行，实验性的`-fork`模式提供更强的容错性。
- 📊 **输出与统计**：运行时输出覆盖率、特征数、语料库大小等统计信息，事件代码如 NEW、REDUCE 指示测试进展。
- 🧩 **高级特性**：支持字典、追踪 CMP 指令、值分析、用户自定义变异器，并可通过`FUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION`宏构建模糊友好版本。
- 🐛 **错误处理**：自动保存导致崩溃、内存泄漏或超时的输入，支持通过`-detect_leaks`检测内存泄漏。
- 🌐 **跨平台支持**：支持 Windows（需配合 ASAN），但某些编译选项（如`/MD`）暂不受支持。
- 📈 **应用成果**：已在众多开源项目（如 GLIBC、OpenSSL、Linux 内核等）中发现数千个漏洞，展示了强大的测试能力。

---

### [GitHub - chartbrew/chartbrew: 开源报告平台，可从 API、SQL 和 NoSQL 数据库构建并共享实时仪表板，配备强大 AI 助手、调度功能和可嵌入图表 📈📊 · GitHub](https://github.com/chartbrew/chartbrew)

**原文标题**: [GitHub - chartbrew/chartbrew: Open-source reporting platform to build and share live dashboards from APIs, SQL and NoSQL databases, with powerful AI assistant, scheduling, and embeddable charts 📈📊 · GitHub](https://github.com/chartbrew/chartbrew)

Chartbrew 是一个开源 Web 应用，可直接连接数据库和 API，利用数据创建精美图表，具备图表构建器、可编辑仪表板、可嵌入图表、查询与请求编辑器及团队协作功能。

- 📊 开源数据可视化平台，支持从数据库和 API 构建实时仪表板
- 🔌 兼容多种数据源，包括 MySQL、PostgreSQL、MongoDB 和 Firebase 等
- 🛠️ 提供本地部署指南，需 NodeJS v20、数据库及 Redis 环境
- 🐳 支持 Docker 快速部署，提供完整环境变量配置示例
- 🌐 提供 DigitalOcean 一键部署选项，简化云端安装流程
- 📈 内置 AI 助手、定时任务和图表嵌入等高级功能
- 👥 具备团队协作能力，社区活跃，提供 Discord 交流渠道

---

### [首页 · capricorn86/happy-dom 维基 · GitHub](https://github.com/capricorn86/happy-dom/wiki/)

**原文标题**: [Home · capricorn86/happy-dom Wiki · GitHub](https://github.com/capricorn86/happy-dom/wiki/)

Happy DOM 是一个无图形界面的 JavaScript 浏览器实现，专注于高性能，适用于测试、网页抓取和服务器端渲染，可作为 JSDOM 的替代方案。

- 🚀 专注于性能优化，在多项操作中速度显著优于 JSDOM
- 🌐 支持多种 Web 标准，包括 DOM、HTML、自定义元素、Fetch API 等
- 🧪 适用于测试、网页抓取和服务器端渲染场景
- ⚙️ 提供丰富的浏览器功能 API，如虚拟控制台、导航等待和表单验证
- 📊 包含性能对比数据，展示其在解析、序列化等操作上的效率优势

---

### [色彩窃贼](https://lokeshdhakar.com/projects/color-thief/)

**原文标题**: [Color Thief](https://lokeshdhakar.com/projects/color-thief/)

Color Thief 是一款用于从图像或视频中提取颜色的工具，由 Lokesh Dhakar 开发，拥有超过 13,000 个 GitHub 星标和每年超过 700 万次 npm 下载量。

- 🎨 从任何图像或视频中抓取颜色
- ⭐ 在 GitHub 上获得超过 13,000 个星标
- 📦 每年 npm 下载量超过 700 万次
- 👨‍💻 由 Lokesh Dhakar 开发
- 🔄 最新版本 v3 于 2026 年 3 月发布
- 📝 完全用 TypeScript 重写
- 🌐 零浏览器依赖
- 🛠️ 提供新的 API

---

### [GitHub - tediousjs/node-mssql: Node.js 的 Microsoft SQL Server 客户端 · GitHub](https://github.com/tediousjs/node-mssql)

**原文标题**: [GitHub - tediousjs/node-mssql: Microsoft SQL Server client for Node.js · GitHub](https://github.com/tediousjs/node-mssql)

这是一个用于 Node.js 的 Microsoft SQL Server 客户端库，支持多种驱动和连接方式，提供了丰富的功能如连接池、事务、预处理语句和流式处理。

- 🚀 **核心功能**：Node.js 的 Microsoft SQL Server 客户端，支持连接池、事务、预处理语句和流式查询。
- 🔌 **驱动支持**：默认使用纯 JavaScript 的 Tedious 驱动，可选支持 Windows/Linux/macOS 的 MSNodeSQLv8 原生驱动。
- 🔗 **连接方式**：支持连接字符串或配置对象进行连接，包含 Azure 和 Windows 身份验证示例。
- 📚 **丰富文档**：提供详细的使用示例，涵盖异步/等待、Promise、回调、流式处理和连接池管理。
- 🛡️ **安全特性**：内置 SQL 注入防护，支持参数化查询和标记模板字面量。
- 🔄 **高级特性**：支持表值参数、JSON 响应解析、地理/几何数据类型以及错误处理。
- ⚙️ **配置灵活**：可配置连接验证、连接池大小、超时设置和数据类型映射。
- 📦 **CLI 工具**：包含命令行工具，可通过配置文件执行 SQL 查询。

---

### [GitHub - gramiojs/gramio：强大、可扩展且真正类型安全的Telegram Bot API 框架 · GitHub](https://github.com/gramiojs/gramio)

**原文标题**: [GitHub - gramiojs/gramio: Powerful, extensible and really type-safe Telegram Bot API framework · GitHub](https://github.com/gramiojs/gramio)

GramIO 是一个用于创建 Telegram 机器人的 TypeScript/JavaScript 框架，强调类型安全、可扩展性和多运行时支持。

- 🚀 **快速开始**：通过 `npm create gramio@latest` 命令即可快速创建和定制机器人项目。
- 🔌 **高度可扩展**：拥有强大的插件和钩子系统，便于功能扩展。
- 🛡️ **类型安全**：完全使用 TypeScript 编写，提供出色的开发体验和类型支持。
- 🌐 **多运行时兼容**：支持在 Node.js、Bun 和 Deno 环境中运行。
- ⚙️ **代码生成**：许多部分（如 Telegram Bot API 类型）为自动代码生成并发布，保持更新。
- 📚 **功能丰富**：示例展示了上下文派生、消息格式化等高级特性，并配有详细文档。
- 📄 **开源项目**：采用 MIT 许可证，在 GitHub 上拥有 248 个星标和 9 个分支，表明其活跃度和社区接受度。

---

### [亲爱的 Heroku：呃... 这是怎么回事？](https://judoscale.com/blog/heroku-whats-going-on?utm_source=node-weekly&utm_medium=referral&utm_campaign=heroku-letter&utm_content=letter-from-the-dev-community)

**原文标题**: [Dear Heroku: Uhh... What’s Going On?](https://judoscale.com/blog/heroku-whats-going-on?utm_source=node-weekly&utm_medium=referral&utm_campaign=heroku-letter&utm_content=letter-from-the-dev-community)

本文作者代表 Judoscale 团队，以长期合作伙伴和客户的身份，表达了对 Heroku 近期动向的困惑与关切。文章指出，Heroku 官方声明将转向“持续工程”模式，强调稳定性而非新功能，但随后却推出了一些更新，这让人难以理解其真实方向。作者呼吁 Heroku 坦诚沟通、公开路线图并明确商业意图，以便开发者和客户能够清楚了解平台的未来规划。

- 🤔 Heroku 宣布转向“持续工程”模式，强调维护而非新功能，但随后又推出了更新，引发社区困惑
- 📢 作者呼吁 Heroku 坦诚沟通，避免使用模糊的企业术语，直接说明平台是否进入维护模式
- 🗺️ 建议公开产品路线图，即使只是保持现有功能，也让开发者了解优先事项和未来方向
- 💼 请求澄清商业意图，明确 Heroku 是专注于直接付费客户，还是逐步减少对平台的投入
- ⚠️ 文中提到，许多使用 Heroku 的团队因这些不明确的沟通，已开始计划迁移平台

---

### [申请 Gauntlet AI - 精英 AI 工程研究员计划](https://gauntletai.com/apply?utm_source=newsletter&utm_medium=paid&utm_campaign=node_weekly&utm_content=april15)

**原文标题**: [Apply to Gauntlet AI - Elite AI Engineering Fellowship Program](https://gauntletai.com/apply?utm_source=newsletter&utm_medium=paid&utm_campaign=node_weekly&utm_content=april15)

Gauntlet 是一个为期十周的强化 AI 工程训练营，旨在通过高强度、全沉浸式的项目实践，帮助软件工程师从“AI 实验者”转型为能构建生产级 AI 系统的专业人才。项目提供免费食宿、计算资源和前沿模型访问，并由招聘合作伙伴资助，学员在真实企业项目中每周交付成果，最终获得高薪 AI 工程职位机会。

- 🚀 **高强度实践**：十周全职沉浸式训练，前 3 周远程建立基础，后 7 周在奥斯汀线下集中构建，通过每周交付提升实战能力
- 💼 **职业直通车**：招聘方全程观察学员项目表现，毕业生起薪达 20 万 -95 万美元，实现 100% 首轮面试通过率
- 🛠️ **前沿技术栈**：涵盖 AI 优先开发、RAG 系统、多智能体协调、企业级微调、多模态 AI 及强化学习等进阶内容
- ⚡ **极限训练模式**：采用“周一发布任务 - 周五交付”的军事化节奏，每周复杂度递增，培养高压下的工程交付能力
- 🎯 **双轨制招生**：设“企业方向”（需 3 年以上经验）和“政府方向”（需 1 年以上经验 + 美国公民身份），均要求全职参与并赴奥斯汀集训
- 📅 **滚动录取机制**：2026 年开设三个季度班次（4 月/7 月/9 月），强调尽早申请，席位先到先得

---

### [人人可用的参数化 CAD | FluidCAD](https://fluidcad.io/)

**原文标题**: [Parametric CAD for everyone | FluidCAD](https://fluidcad.io/)

FluidCAD 是一款面向所有人的参数化 CAD 工具，通过 JavaScript 代码实时生成和编辑 3D 几何模型，结合交互式视口操作与完整的参数化历史记录功能。

- 🚀 **参数化代码建模**：用 JavaScript 编写设计逻辑，实时查看 3D 几何变化，支持特征历史回溯与修改
- 🖱️ **交互式原型设计**：通过视口拖拽直接生成拉伸等操作，快速定型后可用代码锁定参数
- 🔄 **智能特征处理**：自动关联最近草图/选择，智能融合相邻形状，大幅减少重复代码
- 🧩 **几何特征变换**：支持线性/环形阵列、镜像、旋转等复杂特征变换与图案生成
- 📤 **标准化数据交换**：完整支持 STEP 格式导入/导出，兼容所有主流 CAD 工具
- ⚙️ **便捷开发集成**：通过 npm 快速安装，提供 VS Code/Neovim等编辑器扩展，一分钟内即可开始项目
- 🧪 **渐进式学习资源**：提供从基础形状到专业认证考试的阶梯式教程案例库

---

### [OpenCascade.js | OpenCascade.js](https://ocjs.org/)

**原文标题**: [OpenCascade.js | OpenCascade.js](https://ocjs.org/)

该文章介绍了 Web-First CAD 技术，它支持构建在浏览器、云端或任何支持 WebAssembly 的设备上运行的 CAD 应用程序，具有快速、高效和小体积的特点。

- 🌐 构建基于 Web 的 CAD 应用，支持浏览器、云端及 WebAssembly 设备
- ⚡ 利用 Emscripten 和 WebAssembly 实现接近原生的运行速度，支持多线程
- 📦 通过自定义库构建减少代码体积，节省带宽和内存，兼容低端设备

---

### [Open CASCADE 技术 | 协同开发门户](https://dev.opencascade.org/)

**原文标题**: [Open CASCADE Technology | Collaborative development portal](https://dev.opencascade.org/)

Open CASCADE Technology 作为多个优秀项目的核心支撑，广泛应用于参数化建模、PCB 设计、网格生成、数值模拟及 CAD 文件处理等领域。

- 🛠️ FreeCAD：提供参数化 3D 建模与绘图功能，适合初学者使用
- 🔌 KiCad：免费的 3D CAD 软件，专注于 PCB 布局设计
- 🌐 Gmsh：高效的网格生成工具
- 📊 Salome：集成化数值模拟平台
- 🔄 CAD Assistant：支持多种格式的 CAD 文件查看与转换工具

（更多项目信息可通过 OCCT 项目与产品市场了解）

---

### [GitHub - felixrieseberg/windows95：💩🚀 基于 Electron 的 Windows 95。可在 macOS、Linux 和 Windows 上运行。· GitHub](https://github.com/felixrieseberg/windows95)

**原文标题**: [GitHub - felixrieseberg/windows95: 💩🚀 Windows 95 in Electron. Runs on macOS, Linux, and Windows. · GitHub](https://github.com/felixrieseberg/windows95)

这是一个在 Electron 应用中运行的完整 Windows 95 项目，支持 macOS、Windows 和 Linux 系统，基于 JavaScript 实现，提供多种平台的安装包下载。

- 💻 **项目性质**：Windows 95 完整版运行于 Electron 框架内
- 🌐 **跨平台支持**：提供 Windows、macOS 和 Linux 系统的安装文件
- 🎮 **功能体验**：可运行经典游戏（如 Doom），建议调整分辨率至 640x480@256 色以获得最佳兼容性
- 🔧 **开发贡献**：需自行获取磁盘镜像文件并配置本地环境进行构建
- 📜 **版权声明**：项目仅供教育用途，与微软公司无隶属关系
- ⭐ **社区热度**：GitHub 上获得 24.1k 星标，1.4k 分支

---

### [《卡顿克星第二部：奥里诺科·V8 引擎》](https://v8.dev/blog/orinoco)

**原文标题**: [Jank Busters Part Two: Orinoco · V8](https://v8.dev/blog/orinoco)

V8 引擎团队在 Orinoco 项目中引入了三项优化，以减少垃圾回收造成的卡顿并提升性能，包括并行压缩、并行处理记忆集以及黑色分配技术。

- 🚀 并行压缩：将年轻代疏散与老年代压缩并行执行，使压缩时间平均减少 75%，从约 7 毫秒降至 2 毫秒以下。
- 🧠 记忆集重构：将记忆集从指针地址数组改为基于页的位图存储，消除重复条目，使指针更新可并行化，在 Gmail 基准测试中将最大暂停时间降低了 45%。
- ⚫ 黑色分配：在老年代分配对象时立即标记为“存活”，并分配到黑色页面，避免垃圾回收器重复访问，在 Octane Splay 基准测试中提升吞吐量 30% 并减少 20% 内存使用。

---

### [阅读代码前我运行的 Git 命令](https://piechowski.io/post/git-commands-before-reading-code/)

**原文标题**: [The Git Commands I Run Before Reading Any Code](https://piechowski.io/post/git-commands-before-reading-code/)

在接手新代码库时，作者会先运行五个 Git 命令来分析提交历史，从而快速了解项目的健康状况、风险区域和团队动态，而不是直接阅读代码文件。

- 🔄 **高频变更文件**：列出过去一年中修改最频繁的 20 个文件，高变更率且无人愿意负责的文件通常是代码库的痛点所在。
- 👥 **贡献者分析**：通过提交数量排名识别核心贡献者，若单人贡献超过 60% 则存在“巴士因子”风险，还需关注近期活跃度以评估知识传承。
- 🐛 **缺陷聚集区**：筛选涉及修复或缺陷的提交，找出常出问题的文件，与高频变更文件交叉对比可定位最高风险代码。
- 📈 **项目活跃趋势**：按月统计提交数量，观察节奏是否稳定；突然下降或长期衰退可能意味着团队流失或动力不足。
- 🚨 **紧急修复频率**：统计一年内的回滚、热修复等紧急提交，频繁出现则暗示部署流程或测试可靠性存在问题。

---

### [AWS Lambda 的“死亡之吻”——硅片破碎](https://shatteredsilicon.net/aws-lambda-kiss-of-death/)

**原文标题**: [The AWS Lambda 'Kiss of Death' - Shattered Silicon](https://shatteredsilicon.net/aws-lambda-kiss-of-death/)

本文讲述了作者团队如何诊断并解决由 AWS Lambda 连接池引发的数据库冻结问题，核心在于 InnoDB 历史列表过度增长，最终通过调整事务隔离级别为 READ-COMMITTED 有效缓解。

- 🚨 生产环境数据库出现严重冻结，写入停滞，仅影响写入节点
- 📈 发现 innodb_history_list_length 指标异常飙升，远超正常阈值
- 💾 磁盘上的 undo 日志文件异常庞大，达到 80GB
- 🔍 调查发现与 AWS Lambda 连接池中事务未正确关闭有关
- ⚙️ 通过设置 innodb_undo_log_truncate 和限制 innodb_max_undo_log_size 有所改善
- 🔄 关键解决方案：将 Lambda 会话的 transaction_isolation 改为 READ-COMMITTED
- 📚 原理：READ-COMMITTED 使读视图短命，避免长期阻塞 InnoDB 的 purge 线程
- 💡 建议 MariaDB/MySQL（尤其是 Galera 集群）默认采用 READ-COMMITTED 隔离级别

---

### [GitHub 堆叠式拉取请求 | GitHub 堆叠式拉取请求](https://github.github.com/gh-stack/)

**原文标题**: [GitHub Stacked PRs | GitHub Stacked PRs](https://github.github.com/gh-stack/)

GitHub Stacked PRs 功能目前处于私密预览阶段，它允许开发者将大型代码变更拆分为一系列相互依赖的小型拉取请求，每个请求可独立审查，并最终一键合并。该功能提供原生 GitHub 界面支持和 gh stack 命令行工具，简化了堆栈管理，支持 AI 代理集成，并解决了大型 PR 难以审查和合并的问题。

- 🚀 **功能概述**：Stacked PRs 将大型变更拆分为有序的小型 PR 堆栈，每个 PR 代表一个独立层，可分别审查并一键合并。
- 🧭 **堆栈管理**：通过 GitHub 界面直观导航 PR 堆栈，实时查看各层状态，并支持一键级联变基操作。
- 💻 **CLI 工具**：gh stack CLI 提供完整的本地工作流支持，包括创建堆栈、管理分支、推送代码和生成 PR。
- 🤖 **AI 集成**：通过 npx skills add github/gh-stack 命令让 AI 编程助手学习堆栈操作，支持从初始阶段拆分大型变更。
- 🔗 **堆栈结构**：PR 堆栈形成链式结构，每个 PR 以上一层分支为基础，最终合并到主分支，GitHub 会完整追踪堆栈关系。
- ⚙️ **灵活操作**：支持通过 GitHub 界面、API 或标准 Git 工作流管理堆栈，合并时可选择部分或全部 PR，合并后自动重构剩余堆栈。
- 🔒 **预览状态**：该功能目前仅对加入等待列表的仓库开放，需先安装 gh extension install github/gh-stack 扩展才能使用。

---

