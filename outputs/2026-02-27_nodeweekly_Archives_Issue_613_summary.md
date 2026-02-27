### [Node 周刊第 613 期：2026 年 2 月 26 日](https://nodeweekly.com/issues/613)

**原文标题**: [Node Weekly Issue 613: February 26, 2026](https://nodeweekly.com/issues/613)

Node Weekly 第 613 期主要介绍了 Node.js 生态的最新动态，包括框架更新、安全增强、工具发布及行业新闻。

- 🚀 **AdonisJS v7 发布**：全栈 Node.js 框架迎来重大更新，新增 OpenTelemetry 集成、类型安全和现代化工具。
- 🔒 **Clerk 增强认证安全**：通过自动二次验证机制，有效防止凭证填充攻击，无需配置即可使用。
- 📦 **Node.js 版本更新**：v25.7.0（当前版）和 v24.14.0（LTS 版）发布，同时 node:sqlite 进入候选阶段。
- 🛡️ **路径遍历攻击防护指南**：详细讲解 Node.js 中如何识别和防御文件路径滥用漏洞。
- 🤖 **Vercel AI SDK 入门**：提供跨 AI 服务商的统一开发接口，简化 AI 应用集成。
- 🗃️ **数据库扩展方案**：推荐使用 TimescaleDB 的超级表、压缩和聚合功能替代新增数据库。
- 📄 **Git 高级技巧**：解析 Git 配置文件的实用指南，提升版本控制效率。
- ⚡ **结构化并发提案**：探讨 JavaScript 中引入 Effection 库解决并发复杂性的必要性。
- 🛠️ **npm 自动化发布**：介绍基于 GitHub Actions 和 OIDC 的 npm 包安全发布流程。
- 🔢 **numpy-ts 工具发布**：TypeScript 版 NumPy 实现，覆盖 94% 原 API，支持科学计算场景。
- 🌐 **Deno 2.7 稳定版**：增强 Temporal API、Windows ARM 支持及 Node.js 兼容性。
- 🧪 **浏览器端 Node.js 模拟**：NanoVM 实验项目实现在浏览器中运行 Node.js 工具链。

---

### [AdonisJS v7 现已发布](https://adonisjs.com/blog/v7)

**原文标题**: [
      AdonisJS v7 is here
    ](https://adonisjs.com/blog/v7)

AdonisJS v7 是一次增量升级，带来了全面的类型安全、改进的开发者体验和新的功能包，同时保持了与 v6 的最小化破坏性变更。

- 🚀 **现代化基础**：要求 Node.js 24+，更新了 Vite 7、ESLint 和 TypeScript 等工具链，并移除了不必要的依赖。
- 🧩 **功能化入门套件**：提供 Hypermedia、API、React 和 Vue 四种开箱即用的套件，均包含身份验证和完整的工作流程。
- 📦 **自动桶文件生成**：开发服务器自动生成并维护控制器、事件和策略的桶文件，简化导入并确保 HMR 正常工作。
- 🏷️ **路由自动命名**：基于 `controller.method` 模式自动为引用控制器的路由命名，确保一致性和可预测性。
- 🔒 **端到端类型安全**：核心特性，通过代码生成实现从路由定义到前端渲染的全面类型检查，涵盖 URL 构建器、数据转换器和 Inertia 页面。
- 🛠️ **开发者体验提升**：包括环境变量文件读取、密钥类型保护、多重速率限制器、智能迁移生成、简化身份验证设置等多项改进。
- 🔐 **全新加密模块**：支持多驱动器和密钥轮换，并引入了用于数据库查询的确定性加密。
- 📊 **可观测性**：推出 `@adonisjs/otel` 包，集成 OpenTelemetry 进行应用追踪，未来将转向更低开销的诊断通道。
- 🗃️ **Lucid 改进**：引入了从数据库生成的模式类，模型可继承列定义，无需重复声明。
- ⚙️ **新的代码修改工具**：为包作者和工具提供了新的代码修改功能，用于自动化修改源代码。
- 📝 **Edge Markdown**：新包 `edge-markdown` 允许在 Edge 模板中使用 MDC 语法渲染 Markdown 文件。
- 📚 **内容集合**：新包 `@adonisjs/content` 提供了轻量级的内容管理层，用于处理类型化的静态数据集合。
- 🐛 **新版错误页面**：重写了 Youch 错误页面，体积更小，兼容性更好，UI 更新。
- 🔄 **平台原生 Response 支持**：控制器现在可以直接返回平台原生的 `Response` 对象。
- ⬆️ **从 v6 升级**：提供了详细的升级指南，主要变更涉及加密模块和 Inertia 共享数据。
- 🛡️ **安全性增强**：修复了多个安全漏洞，包括文件上传路径遍历、Lucid 批量赋值和原型污染等问题。

---

### [AdonisJS - 全功能 TypeScript 框架](https://adonisjs.com/)

**原文标题**: [
      AdonisJS - The batteries-included TypeScript framework
    ](https://adonisjs.com/)

AdonisJS 是一个功能全面的 TypeScript 框架，集成了身份验证、ORM、验证、邮件、队列、缓存和测试等核心功能，旨在帮助团队快速构建产品而非组装框架。它提供优雅的 API、清晰的约定和完整的 TypeScript 支持，适合构建从原型到生产级的应用。

- 🚀 **一体化 Node.js 框架** – 内置身份验证、ORM、验证、邮件、队列和测试等全套工具，无需额外集成。
- 📦 **全面的 TypeScript 支持** – 提供端到端的类型安全，包括环境变量、事件发射器和序列化。
- 🛠️ **强大的开发者体验** – 集成 Vite、CLI/REPL、服务器端热重载和美观的错误页面，提升开发效率。
- 🔗 **灵活的 MVC 架构** – 支持 React、Vue、服务器渲染模板或纯 API，视图层可自由选择。
- 📄 **官方包覆盖常见需求** – 提供缓存、速率限制、健康检查等官方包，避免兼容性问题。
- 🧪 **内置测试工具** – 支持 Playwright 进行浏览器测试，提供全局事务和身份验证辅助功能。
- 🌍 **活跃的社区与生态** – 拥有丰富的文档、视频教程、Discord 社区和商业支持，持续更新超过十年。

---

### [升级指南 - AdonisJS](https://docs.adonisjs.com/v6-to-v7)

**原文标题**: [
      Upgrade guide - AdonisJS
    ](https://docs.adonisjs.com/v6-to-v7)

本文档详细介绍了如何将 AdonisJS 应用从 v6 升级到 v7，包括环境要求、依赖更新、配置变更、代码重构及 Inertia 集成调整等关键步骤。

- 🚀 **升级前提**：需使用 Node.js 24 或更高版本，并更新所有相关依赖包至最新版。
- 🔧 **工具替换**：移除`ts-node`，改用`@poppinss/ts-exec`作为 TypeScript 即时编译器。
- 📦 **依赖调整**：需单独安装`youch`作为开发依赖，并配置新的钩子系统。
- 📝 **配置更新**：重命名汇编器钩子、调整测试文件匹配模式、移除`assetsBundler`属性。
- 🔐 **加密配置**：创建独立的`config/encryption.ts`文件，使用`legacy`驱动兼容旧数据。
- 🔗 **路由助手**：弃用`router.makeUrl`，改用类型安全的`urlFor`助手。
- 🗑️ **移除旧助手**：如`getDirname`、`cuid`等，需替换为 ES 模块或 UUID 等现代方案。
- 📁 **类名变更**：`Request`和`Response`类更名为`HttpRequest`和`HttpResponse`。
- 🛡️ **会话存储**：Flash 消息中的`errors`键已移除，改用`inputErrorsBag`。
- 📂 **请求处理**：`request.all()`现在合并字段和文件，需注意行为变化。
- 🚧 **路由冲突**：控制器路由自动命名可能导致冲突，需显式命名避免错误。
- 📄 **错误响应**：JSON API 请求不再返回 HTML 状态页，直接返回 JSON 错误。
- 🧩 **VineJS 调整**：移除`BaseModifiers`类，可能影响自定义验证逻辑。
- 🔄 **关闭顺序**：应用关闭钩子现在按反向顺序执行，可能影响清理逻辑。
- ⚙️ **Inertia 重构**：集成全面重写，需调整配置、文件结构并创建中间件处理共享数据。
- 📄 **TypeScript 配置**：为 Inertia 创建独立的`tsconfig.inertia.json`以避免循环引用。
- 📌 **路径别名**：在`package.json`中添加新的子路径导入，如`#generated/*`和`#transformers/*`。

---

### [介绍客户信任：Clerk 的免费凭证填充防护工具](https://clerk.com/changelog/2025-11-14-client-trust-credential-stuffing-killer?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=client-trust&utm_content=02-26-26&dub_id=GwHvAAzGdZsgsM3S)

**原文标题**: [Introducing Client Trust: Clerk’s free credential stuffing killer](https://clerk.com/changelog/2025-11-14-client-trust-credential-stuffing-killer?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=client-trust&utm_content=02-26-26&dub_id=GwHvAAzGdZsgsM3S)

Clerk 推出免费功能 Client Trust，自动为新设备登录启用双重验证，有效防御撞库攻击。

- 🛡️ 针对撞库攻击推出 Client Trust 防御机制，自动将新设备视为不可信状态
- 🔐 用户在新设备使用正确密码登录且未开启双因素验证时，系统强制要求二次验证
- ⚡ 无需额外配置，新应用自动启用，现有应用可通过控制台一键更新
- 💰 所有 Clerk 套餐免费提供该功能，平衡安全性与用户体验
- 🛡️ 即使密码遭遇零日泄露，也能持续保护用户账户安全

---

### [Node.js — Node.js 25.7.0（当前版本）](https://nodejs.org/en/blog/release/v25.7.0)

**原文标题**: [Node.js — Node.js 25.7.0 (Current)](https://nodejs.org/en/blog/release/v25.7.0)

Node.js 25.7.0（Current）版本发布，包含多项功能增强、错误修复及性能优化，涵盖 HTTP/2、SEA、SQLite 等模块的更新，并提供了各平台的安装包下载。

- 🌐 **HTTP/2模块新增HTTP/1回退配置选项**，允许自定义降级行为，提升兼容性。
- 📦 **SEA（Single Executable Applications）支持 ESM 入口点**，简化独立可执行应用的构建流程。
- 🗃️ **SQLite 模块标记为发布候选版本**，预示其即将进入稳定阶段。
- 🔄 **Stream 模块中`Duplex.toWeb()`的`type`选项更名为`readableType`**，提高 API 一致性。
- 🧪 **测试运行器在 SIGINT 信号中断时显示被中断的测试**，改善开发调试体验。
- ⚙️ **多项底层优化与依赖更新**，包括 npm 升级至 11.10.1、V8 引擎补丁及文档修正。
- 🔗 **提供全平台安装包与源码下载**，支持 Windows、macOS、Linux 等多种操作系统架构。

---

### [Node.js — Node.js 24.14.0（长期支持版）](https://nodejs.org/en/blog/release/v24.14.0)

**原文标题**: [Node.js — Node.js 24.14.0 (LTS)](https://nodejs.org/en/blog/release/v24.14.0)

Node.js 24.14.0 LTS 版本“Krypton”发布，包含多项新功能与改进，如异步钩子追踪、文件系统监控忽略选项、全局代理设置、SQLite 默认防御模式等，同时更新了依赖项并修复了多个问题。

- 🚀 **异步钩子增强**：新增 `trackPromises` 选项至 `createHook()`，便于追踪 Promise 生命周期
- 👁️ **文件监控优化**：`fs.watch` 新增 `ignore` 选项，可忽略特定文件或目录的变化
- 🌐 **HTTP 代理支持**：引入 `http.setGlobalProxyFromEnv()`，方便从环境变量设置全局代理
- 🛡️ **SQLite 安全提升**：默认启用防御模式，增强数据库操作的安全性
- 📦 **模块导入扩展**：允许以 `#/` 开头的子路径导入，提升模块解析灵活性
- 🔧 **构建与依赖更新**：替换 cjs-module-lexer 为 merve，添加 LIEF 依赖，并升级 npm 至 11.9.0
- 🧪 **测试工具改进**：测试运行器新增 `env` 选项和支持预期测试失败的功能
- 📄 **文档与修复**：更新多个文档说明，修复了事件处理、DNS 解析、流处理等方面的错误

---

### [SQLite | Node.js v25.7.0 文档](https://nodejs.org/docs/latest/api/sqlite.html)

**原文标题**: [SQLite | Node.js v25.7.0 Documentation](https://nodejs.org/docs/latest/api/sqlite.html)

Node.js v25.7.0 文档中的 `node:sqlite` 模块提供了同步操作 SQLite 数据库的功能，支持数据库连接管理、SQL 语句执行、预处理语句、会话跟踪、备份以及类型转换等核心操作。

- 🗄️ **数据库连接**：通过 `DatabaseSync` 类创建和管理数据库连接，支持文件或内存数据库，并提供多种配置选项如只读模式、外键约束和超时设置。
- 📝 **SQL 执行与预处理**：使用 `exec()` 执行 SQL 字符串，`prepare()` 创建预处理语句以提高性能并防止 SQL 注入，支持命名和匿名参数绑定。
- 🔄 **高级功能**：包括创建用户自定义函数、聚合函数、设置授权回调以控制数据库访问，以及通过会话（`Session`）跟踪和同步数据库变更。
- 💾 **数据缓存与备份**：`SQLTagStore` 类提供 LRU 缓存机制，优化预处理语句的复用；`sqlite.backup()` 支持数据库备份，并可监控进度。
- 🔧 **类型与常量**：定义了 JavaScript 与 SQLite 数据类型之间的自动转换规则，并提供了丰富的常量用于冲突处理、授权控制等高级操作。

---

### [lib: 由 mertcanaltin 在 Node 核心中添加了日志记录器 API · Pull Request #60468 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/60468)

**原文标题**: [lib: added logger api in node core by mertcanaltin · Pull Request #60468 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/60468)

这是一个关于在 Node.js 核心中添加新 logger API 的 Pull Request 讨论，旨在实现一个内置的日志记录功能，并进行了性能优化和代码审查。

- 📝 **PR 概述**：开发者 mertcanaltin 提交了一个将 logger API 集成到 Node.js 核心的草案，旨在解决 issue #49296 中提到的结构化日志需求。
- 🚀 **性能基准测试**：初始性能测试显示，在简单日志、子日志、禁用日志和字段日志场景下，node:logger 与 Pino 相比表现各有优劣，但子日志性能较差。
- 🔧 **持续优化**：通过借鉴 Pino 的模式（如移除子日志绑定序列化开销、优化序列化检查、使用字符串拼接等），性能显著提升，最终在多个场景下超越 Pino。
- 💬 **代码审查与反馈**：多位贡献者参与了代码审查，提出了添加序列化支持、命名约定（遵循 Pino 的 built-in serializers）、测试覆盖等建议。
- ❓ **架构争议**：有审查者质疑为何不直接使用 Pino 而选择重新实现，作者解释是为了适配 Node.js 内部的 diagnostics_channel 机制和性能优化。
- ✅ **审查进展**：经过多轮修改和审查，部分审查者已批准更改，但仍有审查者要求增加测试覆盖并进一步讨论架构选择。
- 📊 **性能成果**：优化后，node:logger 在简单日志（+74%）、子日志（+31%）、禁用日志（+19%）和字段日志（+56%）场景下均显著快于 Pino。

---

### [获取失败](https://nodeweekly.com/link/181232/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/181232/web)

无法总结：获取内容失败，状态码 429。

---

### [Node.js — 漏洞报告的新 HackerOne 信号要求](https://nodejs.org/en/blog/announcements/hackerone-signal-requirement)

**原文标题**: [Node.js — New HackerOne Signal Requirement for Vulnerability Reports](https://nodejs.org/en/blog/announcements/hackerone-signal-requirement)

Node.js 项目更新了 HackerOne 漏洞报告政策，要求提交者需具备 1.0 或更高的 Signal 信誉分，以应对低质量报告激增的问题，新研究人员可通过 OpenJS Foundation Slack 联系安全团队。

- 🛡️ Node.js 安全团队因低质量漏洞报告激增，更新 HackerOne 政策，要求提交者 Signal 信誉分不低于 1.0
- 📈 新规旨在减少无效报告处理负担，确保提交者具备有效安全报告记录，同时允许新研究人员通过 Slack 联系团队
- 🔗 未达 Signal 阈值的研究人员可通过 OpenJS Foundation Slack 与 Node.js 安全发布管理员讨论潜在漏洞
- 📊 HackerOne Signal 是反映研究人员历史提交质量的信誉指标，高分代表有效、有影响力的报告记录
- 🤝 项目感谢安全社区的理解与合作，共同维护 Node.js 安全性

---

### [Node.js 路径遍历：预防与安全指南](https://nodejsdesignpatterns.com/blog/nodejs-path-traversal-security/)

**原文标题**: [Node.js Path Traversal: Prevention & Security Guide](https://nodejsdesignpatterns.com/blog/nodejs-path-traversal-security/)

本文深入探讨了 Node.js 中的路径遍历攻击，详细解释了其原理、危害及防御方法。文章通过一个易受攻击的图片服务器示例，展示了攻击者如何利用路径遍历漏洞访问系统敏感文件，并逐步构建了一个安全的文件服务器实现。核心防御策略包括对用户输入进行完全解码、拒绝空字节和绝对路径、使用规范化路径解析、跟随符号链接以及严格的边界检查。此外，文章还强调了深度防御的重要性，涵盖了输入验证、基础设施加固（如最小权限运行、容器化）、安全测试、监控和事件响应计划。最后，总结了一套 Node.js 安全编码和运维的最佳实践清单，强调安全是一个持续的过程。

- 🔐 **路径遍历攻击概述**：攻击者通过操纵文件路径变量（如使用`../`序列），访问 Web 根目录之外的敏感文件，可能导致信息泄露、系统沦陷和数据盗窃。
- ⚠️ **漏洞示例与危害**：展示了一个未经验证用户输入、直接拼接路径的脆弱图片服务器代码，攻击者可借此读取如`/etc/passwd`、数据库凭证或 SSH 私钥等关键文件。
- 🛡️ **核心防御措施**：实现`safeResolve`函数，通过完全解码 URL 编码、拒绝空字节和绝对路径、解析规范路径、跟随符号链接及验证路径边界，构建安全路径解析。
- 🧩 **深度防御策略**：除代码层防护外，建议采用输入验证白名单、最小权限原则运行进程、利用 Node.js 权限模型、容器化（如 Docker）及部署 WAF 等多层保护。
- 🧪 **安全测试与监控**：编写自动化测试验证防御有效性，记录可疑活动日志，检测攻击模式，并制定事件响应计划，确保快速应对安全事件。
- 📋 **最佳实践总结**：永不信任用户输入、使用规范路径、实施边界检查、分层防御、安全错误处理、全面测试，并保持 Node.js 及依赖项更新。
- 🔗 **扩展资源**：提供 OWASP 指南、安全工具（如 Snyk、helmet）及进一步学习资料，强调安全是持续过程，需定期审计和跟进最新漏洞。

---

### [Node.js 中 Vercel AI SDK 入门指南 | www.thecodebarbarian.com](https://thecodebarbarian.com/getting-started-with-the-vercel-ai-sdk-in-nodejs.html)

**原文标题**: [Getting Started with the Vercel AI SDK in Node.js | www.thecodebarbarian.com](https://thecodebarbarian.com/getting-started-with-the-vercel-ai-sdk-in-nodejs.html)

本文介绍了在 Node.js 中使用 Vercel AI SDK 来统一集成多个 LLM 提供商（如 OpenAI、Claude 和 Gemini）的方法，通过抽象接口简化了多模型支持，并展示了文本生成、流式响应和结构化输出的具体实现。

- 🛠️ Vercel AI SDK 为不同 LLM 提供商提供统一接口，通过核心`ai`包和提供商集成包（如`@ai-sdk/openai`）简化多模型集成。
- 📦 使用`generateText()`函数进行非流式文本生成，可接收系统提示和消息数组，支持 OpenAI 和 Anthropic 等提供商。
- 🌊 通过`streamText()`实现流式响应，返回异步迭代器以逐块输出文本，显著降低用户感知延迟。
- 🏗️ 利用`generateObject()`生成结构化数据，结合 Zod 模式定义，确保输出符合预期格式，避免解析错误。
- 🔄 文章基于 Mongoose Studio 的实际重构经验，展示了如何从原始 fetch 调用迁移到 AI SDK，提升代码简洁性和可维护性。

---

### [TimescaleDB：PostgreSQL 时序数据库 | 虎数据 | 虎数据](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB: PostgreSQL Time-Series DB | Tiger Data | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是一个基于 Postgres 构建的时序数据库，提供高性能时序数据处理、实时分析和事件管理，支持自动分区、行列混合存储、压缩和增量物化视图等功能，适用于物联网、金融科技和实时分析等场景。

- 🚀 **高性能时序处理**：自动分区（超表）实现快速数据摄入与大规模查询，支持时间/ID 分区与索引优化
- 💾 **智能存储架构**：行列混合存储自动转换，结合列式压缩（节省高达 95% 存储空间）与向量化运算加速分析查询
- 🔄 **实时分析引擎**：增量物化视图（持续聚合）支持即时仪表板，内置延迟数据处理与分层聚合能力
- 🤖 **自动化数据管理**：内置任务调度器，提供数据分层、保留策略及压缩作业的自动化配置与监控
- 📊 **专业时序函数库**：近 200 个超函数支持统计汇总、时间加权平均、插值等高级时序分析
- ☁️ **云端托管优势**：Tiger Cloud 提供一键部署、存储智能分层、独立扩缩容、多可用区高可用与企业级安全合规
- 🔧 **开源与自托管**：完全兼容 PostgreSQL 生态，支持本地部署，但云服务特有功能需使用托管版本
- 🌐 **多行业应用**：已服务于物联网设备监控、金融交易数据分析、实时客户仪表板等场景，获 Cloudflare 等企业验证

---

### [Git 的魔法文件 | 安德鲁·内斯比特](https://nesbitt.io/2026/02/05/git-magic-files.html)

**原文标题**: [Git’s Magic Files | Andrew Nesbitt](https://nesbitt.io/2026/02/05/git-magic-files.html)

Git 仓库中包含一系列特殊文件，它们随代码一同提交，用于控制 Git 的行为和工具的工作方式，如忽略文件、配置属性、管理子模块、统一作者信息等。这些文件不仅影响 Git 操作，也被许多外部工具（如代码托管平台、版本管理器、编辑器）自动读取，以实现一致的开发环境和工作流程。

- 📁 **.gitignore**：定义 Git 应忽略跟踪的文件模式，支持通配符、目录标记和否定规则，可从全局、本地和项目级多层配置。
- ⚙️ **.gitattributes**：指定文件处理方式，如行尾标准化、二进制文件标记、自定义差异/合并驱动，并影响 GitHub Linguist 的语言统计。
- 🔗 **.gitmodules**：记录 Git 子模块的配置，包括路径、URL 和分支，用于嵌入其他仓库作为依赖，但需手动初始化和更新。
- 📧 **.mailmap**：映射作者名称和邮箱至规范身份，用于统一 `git log`、`git blame` 等输出中的贡献者信息。
- ⏭️ **.git-blame-ignore-revs**：列出 `git blame` 应跳过的提交（如格式化更改），以追溯实际代码变更作者，需单独配置使用。
- 📝 **.gitmessage**：提供提交消息模板，需手动配置 `commit.template` 后生效，常用于规范提交格式。
- 🌐 **平台特定文件夹**：如 `.github/`、`.gitlab/`，包含 CI/CD 配置、模板等，各托管平台支持覆盖和回退机制。
- 🛠️ **其他约定文件**：如 `.gitkeep`（保留空目录）、`.editorconfig`（编辑器设置）、版本文件（如 `.node-version`）和 `.dockerignore`，用于标准化工具行为。
- 🔧 **工具集成文件**：如 `.gitreview`（Gerrit 配置）、`.gitlint`（提交消息检查），扩展 Git 工作流并随仓库共享配置。

---

### [为什么 JavaScript 需要结构化并发 | 博客 | Effection](https://frontside.com/effection/blog/2026-02-06-structured-concurrency-for-javascript/)

**原文标题**: [Why JavaScript Needs Structured Concurrency | Blog | Effection](https://frontside.com/effection/blog/2026-02-06-structured-concurrency-for-javascript/)

JavaScript 异步编程中，由于缺乏结构化并发机制，常导致任务超出其启动作用域的生命周期，引发资源泄漏和不可控的并发问题。Effection 通过引入结构化并发，确保所有并发操作在其父作用域结束时被强制清理，使异步代码具备同步代码的可预测性和可靠性。

- 🚀 **作用域拥有生命周期**：结构化并发将并发任务的生存期绑定到启动它的代码块，防止任务“泄漏”到作用域之外。
- 🧹 **清理得到保证**：当作用域结束时，所有并发任务会被强制停止并执行清理操作（如 `finally` 块），避免资源残留。
- ⚠️ **异步编程的缺陷**：传统 `async/await` 缺乏内置的父级控制机制，`finally` 无法可靠清理异步任务，需手动传递取消信号（如 `AbortSignal`），导致资源泄漏常见。
- 🔄 **Effection 的解决方案**：通过生成器函数和 `yield*` 替代 `await`，提供两大保证：无操作运行时间超过其父级，所有操作完全退出（清理必执行）。
- 🌍 **跨平台集成**：`main()` 函数自动处理宿主环境事件（如 Node.js 的 SIGINT、浏览器的 unload），确保作用域在退出时正常清理。
- 📚 **保持编程习惯**：Effection 不改变基本编程结构（如 `if`、`for`、`try/catch`），仅增强异步行为的可靠性，使并发代码更易推理和维护。

---

### [GitHub - thefrontside/effection: JavaScript 的结构化并发与效果库](https://github.com/thefrontside/effection)

**原文标题**: [GitHub - thefrontside/effection: Structured concurrency and effects for JavaScript](https://github.com/thefrontside/effection)

Effection 是一个为 JavaScript 设计的结构化并发与副作用管理库，旨在通过结构化并发确保资源与副作用无泄漏，并妥善处理取消操作，使并发代码在规模化时依然稳定可靠，同时保持原生 JavaScript 的开发体验。

- 🚀 利用结构化并发防止资源泄漏，确保取消操作可靠处理  
- 🌐 支持 Node.js、浏览器和 Deno 等主流 JavaScript 平台  
- 📦 通过 npm 和 deno.land 发布，便于集成  
- 🛠️ 使用 Deno 进行开发、测试和打包  
- 📚 提供 AI 助手专用文档（llms.txt 和 llms-full.txt）  
- ⭐ 获得 793 个星标和 36 个分支，社区活跃  
- 📄 采用 MIT 许可证，开放源代码  
- 🔧 包含测试脚本和 NPM 包构建工具，支持本地开发

---

### [如何通过 GitHub Actions 发布到 NPM | 以优质软件构建更美好世界](https://glebbahmutov.com/blog/npm-publish-from-github/)

**原文标题**: [How To Publish To NPM From GitHub Actions | Better world by better software](https://glebbahmutov.com/blog/npm-publish-from-github/)

本文介绍了如何利用 NPM OIDC 可信发布工作流，通过 GitHub Actions 自动化发布 NPM 包，以应对个人令牌失效带来的发布中断问题。

- 🔐 NPM 在 2025 年底撤销了个人令牌，提升了安全性但影响了 CI 流程
- 🤖 作者拥有 400 多个 NPM 包，必须实现自动化发布流程
- ⚙️ 可信发布允许 NPM 识别特定的 GitHub Actions 工作流为合法发布者
- 📝 配置步骤：在 NPM 账户设置中添加 GitHub 仓库和工作流文件信息
- 🔑 关键配置：在 CI 文件中设置`id-token: write`权限以实现身份验证
- 🚀 使用 semantic-release-action 自动执行版本发布和 NPM 发布
- ✅ 成功案例：cypress-split 和 cypress-map 已采用此方案
- 📦 更新后的工作流移除了旧令牌，依赖 OIDC 进行安全认证

---

### [numpy-ts - numpy-ts](https://numpyts.dev/)

**原文标题**: [numpy-ts - numpy-ts](https://numpyts.dev/)

numpy-ts 是一个为 TypeScript 和 JavaScript 设计的完整 NumPy 实现，提供与 Python NumPy 高度一致的 API，具备类型安全、可树摇优化和跨运行时兼容等特点。

- 🧩 提供 94% 的 NumPy API 覆盖率，实现了 476 个函数，涵盖算术、线性代数、随机分布等
- 🛡️ 完全类型安全，所有函数和操作都有 TypeScript 类型定义，可在编译时捕获错误
- 🌳 支持树摇优化，允许按需导入，减少打包体积
- ✅ 经过 NumPy 验证，通过 6000 多个测试确保输出与 NumPy 一致
- 📦 零依赖，纯 TypeScript 编写，无需原生模块或 WebAssembly
- 🌐 跨运行时兼容，支持 Node.js、Bun、Deno 及现代浏览器
- 🔄 提供从 NumPy 到 numpy-ts 的迁移指南，大部分代码可直接转换

---

### [NumPy](https://numpy.org/)

**原文标题**: [NumPy](https://numpy.org/)

NumPy 是 Python 科学计算的基础包，提供强大的 N 维数组和数值计算工具，作为开源项目拥有活跃的社区支持，具备高性能、易用性和广泛的硬件兼容性，并构成了丰富的数据科学生态系统的核心。

- 🚀 **最新版本**：NumPy 2.4.0 已于 2025 年 12 月 20 日发布，提供更强大的数组计算功能。
- 🔢 **核心功能**：提供高效的 N 维数组操作，包括向量化、索引和广播机制，以及全面的数学函数、随机数生成和线性代数工具。
- 🌍 **开源与社区**：采用 BSD 许可证，在 GitHub 上公开开发，由活跃且多样化的社区维护和支持。
- ⚡ **高性能与兼容性**：核心基于优化的 C 代码实现，兼顾 Python 的灵活性和编译代码的速度，并支持多种硬件、GPU 和分布式计算库。
- 🧩 **生态系统核心**：作为科学计算生态系统的基石，被广泛应用于数据科学、机器学习、可视化等领域，并与 Pandas、SciPy、PyTorch 等库深度集成。
- 📊 **应用场景**：在天文黑洞成像、引力波探测、体育分析和动物姿态估计等前沿科学研究中发挥关键作用。
- 🛠️ **易用性**：通过高级语法设计，使不同背景的程序员都能快速上手，并提供了交互式浏览器环境供用户尝试。

---

### [TensorFlow.js | 面向 JavaScript 开发者的机器学习](https://www.tensorflow.org/js)

**原文标题**: [TensorFlow.js | Machine Learning for JavaScript Developers](https://www.tensorflow.org/js)

TensorFlow.js 是一个用于在 JavaScript 中进行机器学习的库，允许直接在浏览器或 Node.js 中开发和部署 ML 模型，提供教程、预训练模型和实时演示，支持转换 Python 模型、迁移学习及灵活 API 开发。

- 🎓 通过视频课程快速入门机器学习，结合 Web 技术实践
- 📚 提供完整教程和端到端示例，指导 TensorFlow.js 的使用
- 🤖 包含预训练模型，适用于常见用例，开箱即用
- 🌐 可在浏览器中运行实时演示，如钢琴演奏神经网络和游戏控制
- 🔧 支持转换 Python TensorFlow 模型，并在 JavaScript 环境中运行
- 🧠 利用迁移学习，使用自有数据重新训练现有模型
- 💻 使用直观 API 直接在 JavaScript 中构建和训练模型
- 📢 通过博客和新闻通讯获取最新更新和社区动态
- 👥 参与 TensorFlow 社区，包括 GitHub、论坛和特别兴趣小组

---

### [游乐场 - numpy-ts](https://numpyts.dev/v1.0.x/playground)

**原文标题**: [Playground - numpy-ts](https://numpyts.dev/v1.0.x/playground)

numpy-ts 是一个允许用户在浏览器中直接编写和运行代码的在线平台，它通过 CDN 加载库，无需安装即可使用所有功能，并支持即时查看代码执行结果。

- 🌐 **浏览器内运行**：代码直接在浏览器中执行，无需本地安装，通过 CDN 加载 numpy-ts 库。
- 📦 **预加载功能**：`np` 对象已预先包含所有 numpy-ts 函数，方便直接调用。
- 🖥️ **即时反馈**：使用 `console.log()` 打印输出或从最后表达式返回值，可实时查看运行结果。
- 🔗 **便捷访问**：平台提供导航、指南、API 参考和示例，支持通过搜索和 AI 助手快速获取帮助。

---

### [引言（指南）| Edge 文档](https://edgejs.dev/docs/introduction)

**原文标题**: [Introduction (Guides) | Edge Documentation](https://edgejs.dev/docs/introduction)

Edge 是一个为 Node.js 设计的简单、现代且功能全面的模板引擎，语法类似 JavaScript，支持异步操作、条件语句、循环及组件化开发，适合喜欢简洁模板语法的开发者。

- 🚀 **语法类似 JavaScript**：熟悉 JavaScript 即可快速上手 Edge，无需学习新语言。
- ⚡ **支持异步操作**：可在模板中直接使用 `async/await` 处理异步任务。
- 🔄 **灵活的表达式**：能够执行任何 JavaScript 表达式，包括条件判断和循环。
- 🧩 **组件化开发**：提供组件功能，支持插槽和状态隔离，便于复用代码。
- 🛠️ **高度可扩展**：80% 的功能通过公开 API 实现，易于定制和扩展。
- 📄 **多格式支持**：不仅限于 HTML，还可嵌入 Markdown、JSON、YAML 等多种标记语言。
- 🆚 **与其他工具对比**：不同于前端框架如 Vue.js/React，Edge 是后端模板引擎，无响应式特性，运行时编译，更类似 Nunjucks 或 Pug。
- 🤝 **社区贡献**：正在寻求贡献者帮助开发主流代码编辑器的语法高亮扩展。

---

### [Nunjucks](https://mozilla.github.io/nunjucks/)

**原文标题**: [Nunjucks](https://mozilla.github.io/nunjucks/)

Nunjucks 是一个功能强大且灵活的 JavaScript 模板引擎，支持模板继承、自动转义、宏和异步控制等高级特性，适用于 Node.js 和现代浏览器环境。

- 🚀 **快速轻量**：高性能，运行时仅 8K（gzip 压缩），支持浏览器端预编译模板
- 🔧 **高度可扩展**：支持自定义过滤器和扩展，满足复杂需求
- 🌐 **跨平台使用**：兼容 Node.js 和所有现代浏览器，提供全面的预编译选项
- 📚 **功能丰富**：提供模板继承、异步模板、内置过滤器等强大功能，灵感来源于 Jinja2
- 🏢 **广泛应用**：被 Firefox Marketplace、Mozilla Webmaker、Apostrophe CMS 等众多项目采用

---

### [GitHub - pugjs/pug: Pug – 专为 Node.js 设计的健壮、优雅且功能丰富的模板引擎](https://github.com/pugjs/pug)

**原文标题**: [GitHub - pugjs/pug: Pug – robust, elegant, feature rich template engine for Node.js](https://github.com/pugjs/pug)

Pug 是一款高性能的 Node.js 模板引擎，采用简洁的缩进语法，支持丰富的功能，广泛用于生成 HTML。

- 🚀 **高性能模板引擎**：专为 Node.js 和浏览器设计，受 Haml 影响，语法简洁高效。
- 📝 **简洁的缩进语法**：通过缩进和换行定义 HTML 结构，减少冗余代码，提升可读性。
- 🔄 **从 Jade 重命名**：因商标问题，项目从 "Jade" 更名为 "Pug"，版本 2 开始使用新名称。
- 📦 **安装与使用**：可通过 npm 安装 `pug` 包，或使用命令行工具 `pug-cli` 进行编译。
- 🌐 **浏览器支持**：提供独立版本，但推荐预编译模板为 JavaScript 以优化性能。
- 🔧 **丰富的 API**：支持 `compile`、`render` 和 `renderFile` 等方法，灵活集成到项目中。
- 📚 **文档与社区**：官方文档位于 pugjs.org，提供教程、问题讨论和在线测试环境。
- 🔗 **多语言移植**：已有 PHP、Java、Python 等语言的端口，以及框架适配器如 Laravel、Rails。
- ⚙️ **扩展资源**：包括编辑器插件、转换工具和缓存方案，增强开发体验。
- 📄 **开源许可**：采用 MIT 许可证，支持专业维护和社区贡献。

---

### [bignumber.js API](https://mikemcl.github.io/bignumber.js/)

**原文标题**: [bignumber.js API](https://mikemcl.github.io/bignumber.js/)

BigNumber.js 是一个用于高精度算术运算的 JavaScript 库，支持任意精度的数字操作，避免浮点数精度问题。它提供了丰富的配置选项和实例方法，用于处理大数字的创建、计算、格式化和转换。

- 🔢 **构造函数与配置**：通过 `BigNumber` 构造函数创建实例，可配置小数位数、舍入模式、指数范围等参数，还支持克隆独立配置的构造函数。
- ⚙️ **静态方法**：包括最大值（`maximum`）、最小值（`minimum`）、随机数生成（`random`）和求和（`sum`）等工具函数，以及验证 BigNumber 实例的 `isBigNumber` 方法。
- 🔄 **实例方法**：提供算术运算（如加、减、乘、除、取模、幂运算）、比较操作（如等于、大于、小于）、舍入和格式转换（如转字符串、指数形式、固定小数位）等功能。
- 📊 **属性与表示**：每个实例包含系数（`c`）、指数（`e`）和符号（`s`）属性，用于内部表示数字；支持零、NaN 和无穷大的特殊处理。
- 🛡️ **错误处理与类型安全**：库会抛出带标识的错误，并允许通过覆盖 `valueOf` 方法防止意外类型转换，确保运算的可靠性。
- ❓ **常见问题**：解释了为何去除尾部零以提高算术结果的清晰度，并提供了添加尾部零的格式化方法作为补充。

---

### [emscripten/ChangeLog.md 位于主分支 · emscripten-core/emscripten · GitHub](https://github.com/emscripten-core/emscripten/blob/main/ChangeLog.md#502---022526)

**原文标题**: [emscripten/ChangeLog.md at main · emscripten-core/emscripten · GitHub](https://github.com/emscripten-core/emscripten/blob/main/ChangeLog.md#502---022526)

Emscripten 是一个开源编译器工具链，用于将 C/C++ 代码编译为 WebAssembly 和 JavaScript，从而在 Web 浏览器中运行高性能的本地应用程序。

- 🛠️ 核心功能：将 C/C++ 代码转换为 WebAssembly 和 JavaScript，支持在 Web 环境中运行
- 🌐 开源项目：托管在 GitHub 上，拥有活跃的社区和广泛的开发者参与
- 📊 项目活跃度：获得 27.2k 星标、3.5k 分支，显示高度关注和使用
- 🔧 开发协作：包含 2k 个议题、408 个拉取请求，促进持续改进和问题解决
- 📚 资源丰富：提供 Wiki、讨论区、Actions 等工具，支持项目文档和自动化流程
- 🔒 安全维护：设有专门的安全板块，确保代码质量和漏洞管理

---

### [发布 v4.12.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.12.0)

**原文标题**: [Release v4.12.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.12.0)

Hono v4.12.0 版本发布，引入了客户端新功能、中间件改进、适配器增强以及显著的性能优化，包括路由器和上下文的性能提升。

- 🛠️ Hono 客户端新增 `$path()` 方法，用于获取路径字符串，便于路由或缓存键操作。
- 🔧 新增 `ApplyGlobalResponse` 类型助手，为 RPC 客户端添加全局错误响应类型。
- 🔀 SSG 新增 `redirectPlugin`，为 HTTP 重定向响应生成静态 HTML 重定向页面。
- 🔐 Basic Auth 中间件新增 `onAuthSuccess` 回调，支持认证成功后设置上下文或记录日志。
- 🌐 `getConnInfo()` 现已支持 AWS Lambda、Cloudflare Pages 和 Netlify 适配器。
- 🔄 尾部斜杠中间件新增 `alwaysRedirect` 选项，修复通配符路由的重定向问题。
- 🌍 语言中间件支持 RFC 4647 渐进式区域代码截断，提升语言匹配灵活性。
- 📦 `ExecutionContext` 类型新增 `exports` 属性，便于 Cloudflare Workers 类型扩展。
- ⚡ TrieRouter 性能提升 1.5 至 2 倍，通过优化减少语法开销和冗余处理。
- 🚀 `c.json()` 新增快速路径优化，提升响应生成效率，减少内存分配。

---

### [GitHub - taskforcesh/bullmq: BullMQ - 基于 Redis 的 NodeJS、Python、Elixir 和 PHP 消息队列与批处理系统](https://github.com/taskforcesh/bullmq)

**原文标题**: [GitHub - taskforcesh/bullmq: BullMQ - Message Queue and Batch processing for NodeJS, Python, Elixir and PHP based on Redis](https://github.com/taskforcesh/bullmq)

BullMQ 是一个基于 Redis 构建的分布式消息队列和批处理库，支持 NodeJS、Python、Elixir 和 PHP，提供高性能、可靠的消息队列解决方案，适用于后台任务和作业处理。

- 🚀 **多语言支持**：兼容 NodeJS、Python、Elixir 和 PHP，提供跨平台的消息队列处理能力。
- 🛠️ **核心功能**：支持作业队列、延迟任务、优先级处理、并发控制、父子依赖关系及速率限制等高级特性。
- 📊 **监控与管理**：提供官方前端界面（Taskforce.sh），用于队列监控、作业检查、重试及统计指标查看。
- 🔄 **扩展与生态**：包含 BullMQ-Pro 高级版本，支持去重、批处理、组速率限制等增强功能；与 Dragonfly 等 Redis 替代方案兼容。
- 🌍 **广泛应用**：被多家知名组织使用，拥有活跃的社区、丰富的文档和教程资源。
- 📈 **开源贡献**：采用 MIT 许可证，鼓励开发者通过 Fork 和 Pull Request 参与项目贡献。

---

### [发布 v5.2.0 · alfateam/orange-orm · GitHub](https://github.com/alfateam/orange-orm/releases/tag/v5.2.0)

**原文标题**: [Release v5.2.0 · alfateam/orange-orm · GitHub](https://github.com/alfateam/orange-orm/releases/tag/v5.2.0)

该页面显示了一个 GitHub 仓库的界面，其中包含加载错误、仓库的基本信息以及最新版本 v5.2.0 的发布详情。

- 🚨 页面加载时出现错误提示，需要重新加载
- 📊 仓库基础数据：957 个星标、20 个分支、3 个未解决问题、5 个拉取请求
- 🏷️ 最新版本 v5.2.0 于 2024 年 2 月 19 日发布，包含 3 次提交
- ✨ 新功能包括：通过 distinct() 实现去重聚合、列间过滤支持、关联计数过滤增强
- ⚠️ 页面多个部分存在加载异常情况

---

### [GitHub - patrickjuchli/basic-ftp：适用于Node.js的FTP客户端，支持TLS上的FTPS、IPv6被动模式、async/await以及Typescript。](https://github.com/patrickjuchli/basic-ftp)

**原文标题**: [GitHub - patrickjuchli/basic-ftp: FTP client for Node.js, supports FTPS over TLS, passive mode over IPv6, async/await, and Typescript.](https://github.com/patrickjuchli/basic-ftp)

这是一个用于 Node.js 的 FTP 客户端库，支持 FTPS over TLS、IPv6 被动模式、async/await 和 TypeScript，采用 MIT 许可证。

- 🚀 **功能特性**：支持 FTPS over TLS、IPv6 被动模式、Promise API 和目录操作，但不支持主动模式
- ⚠️ **使用建议**：建议优先使用 HTTPS 或 SFTP 等更安全的传输协议，仅在必须使用 FTP 时选用此库
- 📦 **安装简单**：通过`npm install basic-ftp`即可安装，仅依赖 Node 10.0 及以上版本
- 🔧 **API 丰富**：提供完整的 FTP 操作接口，包括连接管理、文件传输、目录操作和进度跟踪
- 🐛 **错误处理**：区分 FTP 服务器错误与连接错误，前者保持连接可用，后者自动关闭连接
- 📝 **日志调试**：支持详细日志输出，可自定义日志处理器，便于问题排查
- 🏗️ **扩展灵活**：可通过`client.parseList`自定义目录列表解析，底层基于 FTPContext 构建
- 📊 **类型支持**：使用 TypeScript 开发，提供完整的类型声明文件
- 👥 **社区活跃**：拥有 711 个星标、101 个分支，被超过 26.6 万个项目使用

---

### [ESLint v10.0.2 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/02/eslint-v10.0.2-released/)

**原文标题**: [ESLint v10.0.2 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/02/eslint-v10.0.2-released/)

ESLint v10.0.2 已发布，这是一个针对先前版本中发现的若干错误进行修复的补丁版本更新。

- 🔒 更新了 ajv 依赖至 v6.14.0 版本，以修复一个近期公开的安全问题。
- 🐛 修复了与安全漏洞相关的错误（提交 2b72361）。
- 📚 更新了文档，包括链接规则类型说明至 CLI 选项 --fix-type、根据程序范围变更更新迁移指南，以及修复 vars-on-top 规则示例中的缺失分号。
- 🔧 完成了常规维护工作，更新了 @eslint/eslintrc 和 eslint-plugin-jsdoc 等依赖项。

---

### [Node Weekly 读者专享优惠 · EuroPDF - 快速安全地将 HTML 转换为 PDF！](https://www.europdf.eu/node-weekly/)

**原文标题**: [Special offer for Node Weekly readers Â· EuroPDF - create PDFs from HTML, fast and secure!](https://www.europdf.eu/node-weekly/)

EuroPDF 是一项基于 PrinceXML 引擎的 PDF 生成服务，允许用户通过 API 将 HTML、CSS 和 JavaScript 转换为 PDF，所有数据处理均在欧盟境内完成，注重隐私与数据安全，并提供免费及多种付费方案。

- 🚀 **快速集成**：通过简单 API 调用即可将 HTML 转换为 PDF，支持回调 URL，易于集成。
- 🌍 **欧盟数据托管**：所有 PDF 在德国数据中心生成，数据完全保留在欧盟境内，符合高标准隐私与安全要求。
- 📄 **全面支持网页标准**：基于 PrinceXML 引擎，支持现代 CSS、JavaScript、SVG、TIFF、网页字体等，可生成复杂布局和可访问 PDF。
- ⚙️ **高级布局功能**：支持自定义页码、页眉页脚、脚注、水印、多种纸张尺寸与方向等高级排版需求。
- 🛡️ **注重隐私与合规**：服务最初为自身需求开发，强调 GDPR 完全合规，且避免依赖欧盟 - 美国数据传输协议。
- 🆓 **灵活的免费与付费方案**：提供免费计划（每月 5 个常规 PDF）及多种付费套餐（如 Starter、Standard、Large、X-Large），按需计费，支持随时升级或降级。
- 🔧 **支持大规模生成**：无具体 PDF 大小或页数限制，支持高并发请求，适合每月生成数千份 PDF 的场景。
- ❓ **常见问题解答**：涵盖数据存储时间（请求完成后立即删除）、测试 PDF（带水印）、Prince 版本支持（如 Prince 16）、JavaScript 执行、超限计费方式等详细信息。

---

### [Deno 2.7：Temporal API、Windows ARM 支持与 npm 覆盖功能 | Deno](https://deno.com/blog/v2.7)

**原文标题**: [Deno 2.7: Temporal API, Windows ARM, and npm overrides | Deno](https://deno.com/blog/v2.7)

Deno 2.7 版本发布，带来多项重要更新，包括 Temporal API 稳定化、Windows ARM 原生支持、npm overrides 功能增强，以及大量 Node.js 兼容性改进和开发者体验优化。

- 🗓️ **Temporal API 稳定化**：Temporal API 现已稳定，无需 `--unstable-temporal` 标志，提供更强大的日期时间处理能力。
- 🖥️ **Windows ARM 原生支持**：提供官方 ARM64 Windows 构建，在 Surface Pro X 等设备上实现原生性能运行。
- 📦 **npm overrides 支持**：在 `package.json` 中支持 `overrides` 字段，可精确控制依赖树中特定包的版本。
- ⚙️ **新增子进程 API**：引入 `Deno.spawn()`、`Deno.spawnAndWait()` 等简化子进程操作的函数（目前标记为不稳定）。
- 🔧 **Node.js 兼容性大幅提升**：修复了 `node:worker_threads`、`node:child_process`、`node:zlib`、`node:sqlite` 等模块的数十个问题。
- 🌐 **Web API 增强**：`navigator.platform` 属性可用；`CompressionStream` 支持 Brotli 压缩；`crypto.subtle` 支持 SHA3 哈希算法；`createImageBitmap` 支持 GIF 和 WebP 格式。
- 📁 **文件系统 API 更新**：新增 `FsFile.tryLock()` 非阻塞文件锁方法。
- 🛠️ **包管理器功能改进**：新增 `deno create` 命令用于项目脚手架；`deno install` 支持 `--compile` 编译为独立可执行文件；`deno add` 支持 `--save-exact` 精确版本锁定；`package.json` 支持 `jsr:` 协议依赖。
- 🧹 **开发者体验优化**：`deno compile` 新增 `--self-extracting` 自解压模式；`deno task` 支持更多 Shell 配置；`deno check` 支持 `--check-js` 对 JS 文件进行类型检查；`deno fmt` 支持 `--fail-fast` 快速失败。
- 🐛 **调试功能增强**：Chrome DevTools 和 VSCode 现可调试 Web Workers；`--inspect` 标志支持更灵活的格式。
- 🔄 **升级与维护改进**：`deno upgrade` 支持下载缓存和 `--checksum` 校验和验证；新增 `SSLKEYLOGFILE` 环境变量支持以调试 TLS 连接。
- ⚡ **性能与底层更新**：升级至 V8 14.5 引擎；`Deno.cron` 任务现支持 OpenTelemetry 自动插桩。
- 🙏 **致谢社区贡献者**：感谢众多社区成员通过提交代码、报告问题等方式对 Deno 2.7 做出的贡献。

---

### [GitHub - userland-run/nano: nano — 通过编译为 WebAssembly 的微型 RISC-V 用户模式 Linux 解释器，直接在浏览器中运行真实的 Node.js 及其他静态链接的 Linux 二进制文件。无需容器。无需服务器。纯客户端执行。](https://github.com/userland-run/nano)

**原文标题**: [GitHub - userland-run/nano: nano — Run real Node.js and other statically linked Linux binaries directly in the browser via a tiny RISC-V user-mode Linux interpreter compiled to WebAssembly. No containers. No servers. Pure client-side execution.](https://github.com/userland-run/nano)

NanoVM 是一个基于 RISC-V 用户模式 Linux 模拟器编译为 WebAssembly 的项目，它允许在浏览器中直接运行 Node.js 等静态链接的 Linux 二进制文件，无需服务器或容器，完全在客户端执行。

- 🚀 **核心功能**：通过 WebAssembly 实现的 RISC-V 模拟器，在浏览器中直接运行 BusyBox、Node.js v25 及 npm/TypeScript 工具链。
- 🛠️ **技术架构**：采用无标准库的 Rust 编写，模拟 RV64GC CPU 并支持约 80 个 Linux 系统调用，包含内存管理、文件 I/O 和 ELF 加载等功能。
- 🌐 **演示应用**：提供基于浏览器的 IDE 演示，包含文件树、代码编辑器和控制台预览面板，支持运行 Node.js 示例和 HTTP 服务器。
- 📦 **项目结构**：包含 CPU 模拟、系统调用处理、内存管理和测试套件等模块，WASM 二进制文件大小约为 585KB（不含捆绑二进制文件）。
- 📄 **文档与测试**：提供完整的架构、系统调用和构建指南文档，测试套件覆盖 MemFS 单元测试、ELF 执行测试和工具链测试。

---

### [almostnode — 浏览器中的 Node.js](https://almostnode.dev/)

**原文标题**: [almostnode — Node.js in your browser](https://almostnode.dev/)

Next.js 应用在浏览器中通过文件路由系统实现客户端渲染。

- 📁 基于文件的路由系统
- 🌐 完全在客户端运行
- ⚡ 使用 App Router 架构

---

### [BrowserPod：基于 Wasm 的通用浏览器沙箱（从 Node.js 起步）](https://labs.leaningtech.com/blog/browserpod-10)

**原文标题**: [BrowserPod: universal in-browser sandbox powered by Wasm (starting with Node.js)](https://labs.leaningtech.com/blog/browserpod-10)

BrowserPod 1.0 是一款基于浏览器的代码沙盒，利用 WebAssembly 技术，能够在用户端安全、高效地运行不受信任的代码，提供接近原生的速度、极低延迟、强数据本地性和低成本，同时保持与本地/云端执行的高保真度。首版支持 Node.js，未来将扩展至 Python、Ruby、Go、Rust 等语言，并计划在 2026 年底引入 Linux 级沙盒。

- 🌐 **发布核心**：BrowserPod 1.0 作为通用浏览器内沙盒发布，首版搭载 Node.js 引擎，利用 WebAssembly 实现高性能、低延迟的代码执行。
- 🚀 **解决痛点**：针对云端沙盒的延迟、成本和数据暴露问题，BrowserPod 将执行保留在浏览器内，基于浏览器安全模型提供 Linux 兼容环境。
- 💡 **应用场景**：支持浏览器内智能编码、Web IDE、交互式文档和教育平台等用例，实现数据本地化，增强隐私和成本效益。
- 🔗 **关键功能**：引入 Portals 功能，允许通过可共享 URL 暴露沙盒内服务，实现实时预览和协作，无需后端基础设施。
- ⚙️ **技术架构**：基于模块化语言引擎、虚拟文件系统和 WebWorkers 进程隔离，构建高保真运行时环境，继承自 WebVM 的 syscall 层。
- 🎯 **首选 Node.js**：以复杂的 Node.js 环境为首发引擎，确保平台从开始就具备鲁棒性，为后续语言支持设定高标准。
- 📅 **发展路线**：2026 年将陆续推出 Python、Ruby、Go、Rust 支持，并在年底通过 CheerpX 实现 Linux 容器运行，迈向通用浏览器执行层愿景。

---

### [利用浏览器<canvas>进行数据压缩](https://jstrieb.github.io/posts/canvas-compress/)

**原文标题**: [Using the Browser’s <canvas> for Data Compression](https://jstrieb.github.io/posts/canvas-compress/)

本文介绍了一种利用浏览器 Canvas API 实现数据压缩的创意方法，尤其适用于旧版浏览器中缺乏标准压缩 API 的情况。

- 🎨 通过将数据编码为 PNG 图像像素，利用浏览器内置的 PNG 无损压缩功能间接实现数据压缩
- 🌐 旨在解决静态网站和单页应用（SPA）前端需要压缩功能但缺乏后端支持的问题
- 🔗 特别适用于压缩 URL 哈希中的 SPA 状态数据，以保持 URL 长度可控
- 📅 该方法在 2023 年 5 月前特别有价值，当时 Compression Streams API 尚未广泛支持
- ⚙️ 文章提供了完整的压缩和解压缩 JavaScript 函数实现，包含详细的代码示例
- 🧪 附有测试文件验证代码功能，并提供了在线演示
- 🔄 解压缩过程需要异步处理，确保图像加载完成后再提取像素数据
- 📝 该方法还可用于 base64 编码任意字节序列，弥补了标准 btoa/atob 函数的局限性

---

### [React 基金会：Linux 基金会托管下的 React 新家园](https://react.dev/blog/2026/02/24/the-react-foundation)

**原文标题**: [The React Foundation: A New Home for React Hosted by the Linux Foundation – React](https://react.dev/blog/2026/02/24/the-react-foundation)

React Foundation 正式成立，由 Linux Foundation 托管，标志着 React、React Native 及相关项目脱离 Meta，成为独立开源项目。

- 🏛️ React Foundation 正式启动，由 Linux Foundation 托管，React、React Native 和 JSX 等项目不再属于 Meta。
- 🤝 八家铂金创始成员包括 Amazon、Callstack、Expo、Huawei、Meta、Microsoft、Software Mansion 和 Vercel。
- 🧑‍💼 基金会由各成员代表组成的董事会管理，Seth Webster 担任执行董事。
- 🛠️ 成立临时领导委员会，确保 React 技术治理独立于基金会董事会，技术方向仍由贡献者和维护者决定。
- 📅 后续工作包括确定技术治理结构、转移代码库和基础设施、探索生态系统支持计划及筹备下一届 React Conf。
- 🙏 感谢所有贡献者、创始成员及全球开发者，React Foundation 的成立源于社区支持，期待共同构建未来。

---

### [TypeScript 5.x 至 6.0 迁移指南 · GitHub](https://gist.github.com/privatenumber/3d2e80da28f84ee30b77d53e1693378f)

**原文标题**: [TypeScript 5.x to 6.0 Migration Guide · GitHub](https://gist.github.com/privatenumber/3d2e80da28f84ee30b77d53e1693378f)

TypeScript 6.0 是一个过渡版本，旨在为即将到来的 TypeScript 7.0（Go 语言重写版本）做准备。它引入了新的默认配置、多项废弃选项以及一些新功能，以更好地与现代生态系统对齐并提升性能。

- 📝 **默认配置变更**：`strict` 默认为 `true`，`target` 默认为 `es2025`，`module` 默认为 `es2022`，`moduleResolution` 默认为 `bundler`，`rootDir` 默认为 `tsconfig.json` 所在目录，`types` 默认为空数组（不再自动包含 `@types` 包）。
- 🚫 **废弃选项**：废弃了 `target: es3/es5`、`downlevelIteration`、`moduleResolution: node10/classic`、`module: amd/umd/system/none`、`baseUrl`、`esModuleInterop: false`、`alwaysStrict: false`、`outFile` 等，这些将在 TypeScript 7.0 中彻底移除。
- 🛠️ **迁移工具**：可使用 `ts5to6` 工具自动处理 `baseUrl` 移除和 `rootDir` 推断等破坏性变更。
- ⚠️ **临时规避**：可通过设置 `"ignoreDeprecations": "6.0"` 暂时屏蔽废弃警告，但此选项在 TypeScript 7.0 中将失效。
- 🆕 **新功能**：包括对 `this` 无关函数的类型推断优化、支持 `#/` 子路径导入、新增 `es2025` 目标与库、引入 Temporal API 类型、为 `Map` 添加 `getOrInsert` 等方法。
- 🔄 **行为变更**：非 ESM 输出文件将无条件包含 `"use strict"`；`esModuleInterop` 的运行时行为发生变化；`moduleResolution` 的默认值可能静默改变。
- 📋 **迁移清单**：优先设置 `types` 和 `rootDir`，审查 `strict` 模式，明确指定 `target` 和 `module`，移除所有废弃选项，并考虑使用自动化工具辅助迁移。

---

### [告别，Rust——德米特里·库德里亚夫采夫](https://yieldcode.blog/post/farewell-rust/)

**原文标题**: [Farewell, Rust - Dmitry Kudryavtsev](https://yieldcode.blog/post/farewell-rust/)

作者回顾了从高中学习 Pascal 和 C 语言开始，到后来因工作转向 PHP 等动态语言，最终因热爱底层控制而尝试使用 Rust 进行 Web 开发的历程。尽管成功构建并运营了 Rust Web 应用，但由于开发效率、工具链成熟度和项目维护成本等问题，最终决定将项目迁移到 Node.js，并总结了 Rust 在 Web 开发中的优缺点。

- 🧑‍💻 **编程起点**：高中时期通过编程俱乐部接触 Pascal 和 C 语言，培养了对底层内存控制的兴趣。
- 🌐 **职业转向**：因就业市场需求转向 PHP 等动态语言进行 Web 开发，但始终怀念 C 语言的精细控制。
- ⚙️ **Rust 的吸引力**：Rust 结合了底层内存安全与现代开发工具（如包管理、格式化），使其成为 Web 开发的新选择。
- 🚧 **开发挑战**：在 Rust 中面临模板类型安全、国际化支持、动态查询构建等难题，导致开发效率降低。
- ⏱️ **编译时间**：Rust 的编译时间较长，尤其在 CI/CD 流程中影响迭代速度，而 Node.js 在此方面更具优势。
- 🧩 **生态成熟度**：Rust 的 Web 开发生态相对不成熟，缺乏第三方 API 库，增加了自行实现和维护的成本。
- ✅ **Node.js 的实用性**：Node.js 在类型安全（如 TypeScript）、工具链和动态需求处理上更适应快速 Web 开发。
- 🛠️ **工具选择**：作者强调“使用合适的工具”，Rust 适合 CPU 密集型任务，而 Node.js 更适合动态 Web 应用开发。

---

