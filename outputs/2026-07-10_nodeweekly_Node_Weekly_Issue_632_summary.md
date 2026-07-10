### [npm 安装时安全性与 GAT 绕过 2FA 弃用 - GitHub 变更日志](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/)

**原文标题**: [npm install-time security and GAT bypass2fa deprecation - GitHub Changelog](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/)

npm v12 发布，引入安装时安全默认设置，并逐步弃用 2FA 绕过功能。

- 🔒 安装时安全默认设置已启用：`allowScripts` 默认关闭，依赖生命周期脚本不再自动运行；`--allow-git` 和 `--allow-remote` 默认设为 `none`，Git 依赖和远程 URL 依赖需明确允许。
- 🛠️ 迁移准备：在 npm 11.16.0+ 中可通过警告提前准备，使用`npm approve-scripts`审查并提交信任脚本列表。
- 🚫 2FA 绕过 GAT 将停止跳过账户变更的 2FA：影响令牌创建、密码修改、包访问管理等敏感操作，预计 2026 年 8 月初生效。
- 📦 2FA 绕过令牌将无法直接发布：仅保留读取私有包和暂存发布功能，需人工 2FA 批准后才公开，预计 2027 年 1 月生效。
- 🔄 替代方案：建议迁移至可信发布（OIDC）或暂存发布，并加入人工审批步骤。

---

### [发布 v12.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0)

**原文标题**: [Release v12.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0)

这是 npm CLI v12.0.0 版本的发布说明，包含多项重大变更、依赖更新和贡献者信息。

- ⚠️ **重大变更：多项命令输出和行为调整** `npm view --json` 现在始终返回数组；`npm sbom` 报告包名而非目录名；全局安装不再注册 man 页面；`npm pkg` 输出不再强制为 JSON；`npm shrinkwrap` 命令及配置已移除；Twitter 和 Freenode 用户资料字段已移除；不再通过 `which node` 解析路径；`npm pack` 和 `npm publish` 的 JSON 输出格式统一；`star`、`stars` 和 `unstar` 命令已移除；`npm adduser` 命令已移除；`npm init` 默认许可证改为空字符串；Node 版本支持更新为 `^22.22.2 || ^24.15.0 || >=26.0.0`；`allow-git` 和 `allow-remote` 默认值为 "none"；根 `preinstall` 现在在安装依赖之前运行；未知配置和 CLI 标志现在会抛出错误而非警告。
- 🛠️ **杂项：移除预发布模式** 移除了 npm 12 和工作区的预发布模式。
- 📦 **依赖更新：所有工作区包版本升级** 包括 `@npmcli/arborist@10.0.0`、`@npmcli/config@11.0.0`、`libnpmaccess@11.0.0` 等在内的多个工作区包均已更新至新版本。
- 👥 **贡献者：感谢所有贡献者** 本次发布由 `reggi` 等人贡献。

---

### [npm v12 默认关闭安装脚本，开始...](https://socket.dev/blog/npm-12)

**原文标题**: [npm v12 Ships With Install Scripts Off by Default, Begins De...](https://socket.dev/blog/npm-12)

概述摘要：Injective SDK 的 npm 包版本 1.20.21 被攻陷，通过虚假遥测功能窃取钱包私钥和助记词。
- 🔒 受影响的版本：Injective SDK npm 包版本 1.20.21 被恶意篡改
- 🕵️ 攻击方式：通过伪装成遥测功能的代码，暗中收集用户数据
- 💳 窃取内容：钱包私钥和助记词被直接外泄
- 🚨 安全风险：用户资金和账户控制权面临严重威胁
- 🗓️ 发布时间：该安全事件于 2026 年 7 月 9 日由 Karlo Zanki 披露

---

### [特性：将未知的.npmrc 配置从报错改为警告 —— 由 reggi 提交 · 拉取请求 #9729 · npm/cli · GitHub](https://github.com/npm/cli/pull/9729)

**原文标题**: [feat: warn instead of error on unknown .npmrc configs by reggi · Pull Request #9729 · npm/cli · GitHub](https://github.com/npm/cli/pull/9729)

npm/cli 合并 PR #9729，将未知 .npmrc 配置项从错误改为警告，恢复 npm 12 之前的行为，并新增 strict-npmrc 配置选项。

- 🔄 恢复旧行为：未知 .npmrc 文件配置项默认改为警告，不再抛出错误
- ⚠️ 保留旧警告措辞：使用 npm 12 之前的提示语“此功能将在下一个主要版本中停止工作”
- 🆕 新增 strict-npmrc 配置：布尔值，默认 false，设为 true 可恢复硬错误模式
- 🚫 CLI 标志仍报错：未知 CLI 标志和缩写继续抛出 EUNKNOWNCONFIG 错误
- 📊 支持日志级别控制：警告信息遵循正常显示管道，可通过 --loglevel=error 或 --silent 抑制
- ✅ 测试更新：更新文件配置验证测试，增加 strict-npmrc 模式、CLI 错误和日志抑制的测试覆盖

---

### [如何使用 OpenTelemetry 导出 Next.js 追踪 | Sentry 博客](https://blog.sentry.io/nextjs-export-traces-opentelemetry/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-evergreen&utm_content=newsletter-primary-traces-otel-blog-learnmore)

**原文标题**: [How to Export Next.js Traces with OpenTelemetry | Sentry Blog](https://blog.sentry.io/nextjs-export-traces-opentelemetry/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-evergreen&utm_content=newsletter-primary-traces-otel-blog-learnmore)

### 概述总结

Next.js 内置了请求追踪功能，但需要配置 OpenTelemetry 导出器才能查看追踪数据。通过 `@vercel/otel` 库和少量配置，可以将追踪数据导出到任何兼容 OpenTelemetry 的后端（如 Sentry）。本文详细介绍了如何配置、添加自定义 span、选择导出方式，以及如何利用追踪数据优化应用性能。

### 关键要点

- 🚀 **Next.js 追踪的重要性**：追踪能帮助定位请求中的性能瓶颈（如中间件、API 路由、数据库查询等），避免盲目猜测。
- ⚙️ **配置 OpenTelemetry**：使用 `@vercel/otel` 库，在 `instrumentation.ts` 中调用 `registerOTel()`，并设置环境变量即可导出追踪数据。
- 🧩 **添加自定义 Span**：围绕关键业务操作（如生成发票、调用 AI 模型）添加 span，使用点号命名规范（如 `invoice.generate-pdf`），并添加有意义的属性（如行数、模板、计划等级）。
- 📡 **发送追踪到 OTLP 后端**：通过设置 `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` 和 `OTEL_EXPORTER_OTLP_TRACES_HEADERS` 环境变量，可直接将追踪数据发送到 Sentry 的 OTLP 端点。
- 🤔 **选择 OTLP 还是 Sentry SDK**：如果团队依赖 Sentry 进行错误监控和调试，建议使用 Sentry SDK；如果已有 OpenTelemetry 管道或只需标准服务器追踪，OTLP 更轻量。
- 🔍 **下一步行动**：利用追踪数据创建监控器、警报和仪表盘，将追踪融入日常运维流程，持续优化性能。

---

### [Node.js — Node.js 26.5.0（当前版本）](https://nodejs.org/en/blog/release/v26.5.0)

**原文标题**: [Node.js — Node.js 26.5.0 (Current)](https://nodejs.org/en/blog/release/v26.5.0)

Node.js 26.5.0 正式发布，包含新发布者、多项新功能及大量改进与修复。

- 🎉 新增发布者 Stewart X Addison，其 GPG 密钥用于未来签名
- 📦 buffer 模块新增 blob.textStream() 方法
- 🚩 ESM 模块新增 --experimental-import-text 实验性标志
- ⏱️ perf_hooks 支持每事件循环迭代采样延迟
- 🌊 stream 模块公开 ReadableStreamTee
- 🔒 tls 模块可报告协商的 TLS 组
- 🛠️ 多项依赖更新，包括 undici、nghttp3、sqlite 等
- 🐛 修复 child_process、crypto、inspector 等模块中的问题
- 📘 文档改进，新增贡献者指南和常见问题解答
- 🧪 测试与工具链优化，提升稳定性和开发体验

---

### [GitHub - tc39/proposal-import-text: 用于导入文本的 TC39 提案](https://github.com/tc39/proposal-import-text)

**原文标题**: [GitHub - tc39/proposal-import-text: A TC39 proposal for importing text · GitHub](https://github.com/tc39/proposal-import-text)

该提案旨在为 JavaScript 添加一种原生导入文本文件的方式，类似于现有的 JSON 和字节导入功能，以提高开发效率和性能。

- 📜 **提案概述**：TC39 的`proposal-import-text`提案旨在为 JavaScript 添加一个`type: "text"`的导入属性，允许开发者以字符串形式直接导入文本文件。
- 🏆 **当前阶段**：该提案已进入第 3 阶段，由 Eemeli Aro champion，并有 Jordan Harband 和 Nicolò Ribaudo 作为审阅者。
- 🎯 **核心动机**：导入文本文件在 JavaScript 中是一个常见操作，但现有方法（如 Fetch API）存在异步、相对路径基于文档 URL 而非模块路径、以及执行时才开始获取等局限性，导致开发体验不佳。
- 💡 **解决方案**：提案建议添加`import text from "path/to/file.txt" with { type: "text" };`语法，使文本导入变得简单、同步且性能更优。
- 🔄 **与现有功能的关联**：该提案与已有的 JSON 导入（`type: "json"`）和 Import Bytes 提案（`type: "bytes"`）保持一致，并借鉴了 Deno 和 Bun 等运行时中已实现的`type: "text"`功能。
- ⚠️ **编码处理**：提案不提供编码定义功能；若需指定编码，开发者应先将文件作为`Uint8Array`导入，再使用`TextDecoder`显式解码。
- 🌐 **相关标准变更**：该提案涉及对 HTML 标准、Fetch 标准、内容安全策略（CSP）以及 WinterTC 最小通用 Web API 的相应修改。
- 📊 **社区关注度**：该仓库获得 51 颗星、12 个关注者和 1 个分支，表明社区对此功能有一定兴趣。

---

### [加载器：通过 efekrskl 添加实验性文本导入 · 拉取请求 #62300 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62300)

**原文标题**: [loader: add experimental text import by efekrskl · Pull Request #62300 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62300)

Node.js 合并了 PR #62300，新增了实验性的文本导入功能，该功能在 `--experimental-import-text` 标志下可用。

- 📝 **新增实验性文本导入**：Node.js 新增 `--experimental-import-text` 标志，支持通过 `import text from './file.txt' with { type: 'text' }` 语法导入文本文件。
- 🚀 **遵循 TC39 提案**：该功能基于 Stage 3 的 TC39 提案实现，Deno 和 Bun 已有类似支持。
- 🔒 **标记为实验性**：该功能被标记为实验性（Status 1.0 - Early development），并置于标志之后，以确保在稳定前有足够的观察和调整空间。
- 💬 **关于字节导入的讨论**：最初 PR 也包含字节导入，但由于 V8 尚不支持不可变 ArrayBuffer，字节导入部分被移除，并添加了相关注释。
- 🗣️ **关于文件编码的讨论**：对于导入非文本文件（如图片）的行为，社区存在分歧，最终决定不抛出异常，以保持与 Deno 和 Bun 的一致。
- ✅ **合并与发布**：该 PR 于 2026 年 6 月 26 日合并，并作为 Node.js 26.5.0 版本的一部分发布。

---

### [通过 pabloerhard 在 nodejs/node 的拉取请求#62935 中添加基于事件循环的指标](https://github.com/nodejs/node/pull/62935)

**原文标题**: [src: add event loop based metrics into node by pabloerhard · Pull Request #62935 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62935)

Node.js 的 PR #62935 已合并，为 `monitorEventLoopDelay()` 新增了一个 `samplePerIteration` 选项，用于基于事件循环迭代的延迟采样。

- ⏱️ **新增采样模式**：为 `monitorEventLoopDelay()` 添加了 `samplePerIteration` 选项，启用后从 libuv 事件循环迭代中直接采样延迟，而非使用定时器。
- 🎯 **解决原有局限**：解决了基于定时器实现的测量不准确（依赖定时器抖动）和浪费唤醒（即使空闲也强制循环）的问题。
- 🔧 **保持向后兼容**：当 `samplePerIteration` 为 `false` 或省略时，默认的基于间隔的实现保持不变，不影响现有代码。
- 📝 **代码重构与清理**：重命名了内部 C++ 类 `ELDHistogram` 为 `IterationHistogram`，并通过共享模板去除了 `IntervalHistogram` 和 `IterationHistogram` 中的重复启动/停止逻辑。
- ✅ **经过严格审查**：该 PR 获得了多位核心维护者的批准，通过了 CI 测试，并作为 Node.js v26.5.0 的一部分发布。

---

### [用 Rust 重写 Bun | Bun 博客](https://bun.com/blog/bun-in-rust)

**原文标题**: [Rewriting Bun in Rust | Bun Blog](https://bun.com/blog/bun-in-rust)

Bun 项目从 Zig 语言成功重写为 Rust 语言，历时 11 天，由一位工程师借助 Claude 代码助手完成，显著提升了稳定性、性能和内存管理。

- 🚀 **重写动机**：Bun 最初用 Zig 编写，但手动内存管理与 JavaScript 垃圾回收混合导致大量 use-after-free、内存泄漏和崩溃问题，Rust 的 `Drop` 和借用检查器能从根本上解决这些 bug。
- 🛠️ **重写过程**：使用约 50 个动态工作流，峰值时 64 个 Claude 实例并行运行，11 天内生成 6,502 次提交，重写 535,496 行 Zig 代码为 Rust 代码，最终所有平台测试全部通过。
- 🔍 **对抗性审查**：每个代码变更由两个独立的 Claude 审查者进行对抗性审查，在合并前捕获了 3 个关键 bug（如异步关闭导致的双重释放、负时间戳的无效 timespec、`unwrap_or` 的急切求值问题）。
- ✅ **稳定性提升**：Rust 重写修复了 128 个在 v1.3.14 中可复现的 bug，包括所有可检测的内存泄漏、堆栈空间使用减少（如 TOML 解析器）、以及通过跨语言 LTO 实现 2%-5% 的性能提升。
- 📉 **资源优化**：二进制体积缩小约 20%（Linux 从 88MB 降至 70MB），`Bun.build()` 重复调用时的内存使用从 6.7GB 降至 609MB。
- 🧪 **持续保障**：新增 24/7 覆盖引导模糊测试，已执行 1000 亿次解析器测试，自动生成约 15 个修复 PR；Rust 代码中仅约 4% 使用 `unsafe` 块。
- 📈 **实际影响**：Bun CLI 月下载量超 2200 万，Claude Code、OpenCode、Vercel 等已采用；Prisma Compute 公测基于 Rust 重写版，解决了之前的内存泄漏和连接池问题。

---

### [克劳德寓言 \ 人类学](https://www.anthropic.com/claude/fable)

**原文标题**: [Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)

概述总结
- 🧠 Claude Fable 5 是第五代智能模型，专为最复杂的知识工作和编程问题设计
- 🚀 2026 年 7 月 1 日起恢复访问，支持数天级别的复杂异步任务
- 💰 定价为每百万输入 token 10 美元，每百万输出 token 50 美元，提示缓存享 90% 折扣
- 🤖 在代理模式（如 Claude Code）中可连续工作数天，自主规划、委派子任务并自我检查
- 💻 编程能力最强，可处理大型迁移、复杂实现和多日自主编码，自动编写测试并验证输出
- 🏢 企业工作流支持多阶段知识工作，从深度研究到交付物生成，只需最小监督
- 👁️ 视觉能力提升，可理解图表、表格和 PDF 中的内容，辅助代码质量评估
- 🛡️ 包含网络安全和生物安全防护，敏感查询自动路由至 Opus 4.8，不收取 Fable 价格
- 📊 在编码、知识工作、视觉和计算机使用基准测试中达到行业领先水平
- 🎯 客户反馈显示其在长期推理、自主操作和复杂任务中表现显著优于前代模型

---

### [GitHub - tc39/proposal-error-code-property · GitHub](https://github.com/tc39/proposal-error-code-property)

**原文标题**: [GitHub - tc39/proposal-error-code-property · GitHub](https://github.com/tc39/proposal-error-code-property)

该提案旨在为 ECMAScript 错误对象标准化一个 `code` 属性，以便更精确、稳定地处理错误。

- 📌 **核心动机**：标准化 `code` 属性，允许开发者通过机器可读的字符串（如 `ERR_CONNECTION_REFUSED`）而非易变的消息文本来识别和处理错误。
- ✅ **关键优势**：提供跨版本、跨执行环境（如 `postMessage` 传输后）的稳定错误契约，并改善错误监控、本地化和开发者工具体验。
- 🚫 **明确排除**：不定义具体的错误代码或分类，也不为规范定义的抛出条件分配代码，这些留待后续提案处理。
- 🌐 **生态现状**：Node.js、Deno、Bun 等运行时及 axios、Stripe、Prisma 等主流库已广泛采用字符串 `error.code`，证明了该模式的必要性。
- 🔄 **与 `error.name` 的区别**：`name` 是粗粒度的错误类型（如 `TypeError`），而 `code` 提供细粒度的具体错误标识，两者互补。
- 💡 **设计细节**：通过扩展 Error 构造函数的选项对象（如 `new Error("msg", { code: "ERR_X" })`）来设置 `code`，属性值可为任意类型（不限于字符串），默认为不存在，且可写、可配置、不可枚举。
- ⚖️ **为何不限制为字符串**：虽然字符串是主流，但 gRPC、MongoDB 等使用数字代码，且 `cause` 属性已确立无类型限制的先例。
- ❓ **常见问题解答**：该提案不强制使用字符串、不鼓励“字符串类型编程”、不定义错误分类、不排斥 Symbol，且承认错误子类在跨环境传输中的局限性。

---

### [更好的认证](https://better-auth.com/)

**原文标题**: [Better Auth](https://better-auth.com/)

Better Auth 是一个可组合、基于插件且可扩展的认证框架，适用于从个人项目到大型企业级应用，被 OpenAI、Databricks 等公司信赖。

- 🔑 认证完全存在于你的应用中，通过声明式配置实现版本控制和类型安全。
- 🧩 拥有丰富的插件生态系统，支持双因素认证、Passkey、Magic Link、组织管理等 50+ 功能。
- 🏢 内置多租户支持，包括团队、角色、邀请和访问控制。
- 🏭 企业级就绪，提供 SSO、SAML 2.0、SCIM 和目录同步功能。
- 🤖 支持 AI 代理认证，包括 MCP 认证、令牌交换和代理委托。
- 🛡️ 提供安全与可观测性功能，如机器人检测、IP 封锁和邮件验证。
- 👥 包含用户管理功能，可管理用户、会话和组织。
- 🏗️ 基础设施层提供仪表盘、审计日志、安全检测和企业功能。
- 📈 社区活跃，拥有 473+ 贡献者，每周下载量达 510 万次。

---

### [Better Auth 加入 Vercel](https://better-auth.com/blog/better-auth-joins-vercel)

**原文标题**: [Better Auth is joining Vercel](https://better-auth.com/blog/better-auth-joins-vercel)

Better Auth 宣布加入 Vercel，以加速开源身份验证和代理工作流安全的发展。该项目始于作者为开源项目添加多租户身份验证的需求，经过多次迭代和社区支持，最终成为公司并收购了 Auth.js/NextAuth.js。未来将专注于开源身份验证框架和代理身份验证协议。

- 🚀 Better Auth 加入 Vercel，共同推动开源身份验证和代理工作流安全
- 👨‍💻 项目始于作者为开源项目添加多租户身份验证的困难经历
- 📦 经过 7 个月开发，Better Auth 于 2024 年 9 月 28 日首次发布
- 🌟 社区迅速增长，获得开发者好评和教程创作
- 💼 加入 YC 并获 Peak XV 等投资，正式成立公司
- 🤝 收购 Auth.js/NextAuth.js，实现项目整合
- 🔒 未来聚焦开源身份验证框架和代理身份验证协议
- 🎯 借助 Vercel 资源，无需分心商业化，专注开发者体验

---

### [宣布 TypeScript 7.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

**原文标题**: [Announcing TypeScript 7.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

TypeScript 7.0 正式发布，这是一个用 Go 重写的原生版本，速度提升高达 10 倍，并带来多项性能与体验改进。

- 🚀 **原生性能飞跃**：TypeScript 7.0 使用 Go 重写，实现原生代码速度与共享内存多线程，全量构建速度提升 8-12 倍，例如 VS Code 代码库从 125.7 秒降至 10.6 秒。
- 💻 **编辑器体验革新**：编辑器加载项目近乎瞬时，查找引用、自动补全和诊断速度大幅提升，VS Code 扩展已可用，Visual Studio 将自动启用。
- ⚙️ **并行化与精细控制**：引入 `--checkers` 和 `--builders` 标志，可调整类型检查与项目构建的并行度，`--singleThreaded` 模式用于调试或资源受限环境。
- 🔄 **改进的 `--watch` 模式**：基于 Parcel 文件监听器重构，提供高效稳定的跨平台文件监控，资源占用显著降低。
- ✅ **生产级稳定性**：经过微软内部团队及 Bloomberg、Google 等外部公司大规模测试，语言服务器命令失败率降低 80% 以上，崩溃率降低 60%。
- 🔗 **与 TypeScript 6.0 并行运行**：提供 `@typescript/typescript6` 兼容包，支持 `tsc6` 可执行文件，便于工具过渡。
- 🧩 **模板字面量类型改进**：现在正确处理 Unicode 码点，将 `😀` 视为单个字符，而非拆分为代理对。
- 📜 **JavaScript 支持重构**：JSDoc 类型推断更一致，废弃了 `@enum`、`@class` 等旧模式，采用更严格的 TypeScript 风格分析。
- 🚧 **嵌入式语言支持待完善**：Vue、MDX、Svelte 等框架尚需等待 API 稳定，建议 CLI 使用 7.0，编辑器暂用 6.0。
- 🎯 **未来路线图**：7.1 版本将推出新 API，团队将回归新功能与性能优化，预计每 3-4 个月发布一个功能版本。

---

### [10 倍更快的 TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

**原文标题**: [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScript 团队宣布将 TypeScript 编译器移植到原生代码，实现 10 倍性能提升，大幅改善开发体验。

- 🚀 原生移植将编辑器启动速度提升 8 倍，构建时间减少 10 倍，内存占用降低约一半
- ⚡ 实测性能：VS Code 代码库从 77.8 秒降至 7.5 秒，Playwright 从 11.1 秒降至 1.1 秒
- 🗓️ 时间线：2025 年中预览命令行类型检查，年底实现完整项目构建和语言服务
- 🔄 版本规划：JS 版继续发展至 6.x，原生版将作为 TypeScript 7.0 发布
- 🛠️ 新特性：即时全项目错误列表、高级重构、更深层代码洞察，为 AI 工具提供支持
- 📡 采用语言服务器协议 (LSP)，与行业标准对齐
- 💻 可在 GitHub 仓库获取 Go 语言实现代码进行测试
- 🔒 长期维护 6.x 版本直到 7.x 足够成熟，确保平稳过渡

---

### [宣布 TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

TypeScript 6.0 正式发布，作为连接 TypeScript 5.9 和即将推出的 Go 语言重写版 7.0 的桥梁版本，带来了多项新特性、性能优化和弃用调整。

- 🚀 **TypeScript 6.0 是通往 7.0 的桥梁**：基于 Go 语言的全新编译器即将完成，6.0 旨在对齐行为并帮助开发者平滑迁移。
- 🔍 **改进的类型推断**：不再将未使用 `this` 的函数视为上下文敏感，从而修复了方法语法中参数类型推断的 bug。
- 📁 **支持 `#/` 子路径导入**：现在 Node.js 20+ 和 TypeScript 的 `nodenext`/`bundler` 模块解析模式下，可以使用 `#/*` 作为内部模块别名。
- ⚙️ **新增 `--stableTypeOrdering` 标志**：使 6.0 的类型排序行为与 7.0 一致，减少迁移时的差异噪音，但可能带来最多 25% 的性能开销。
- 🎯 **ES2025 目标与库**：新增 `es2025` 选项，包含 `RegExp.escape`、`Promise.try`、`Iterator` 和 `Set` 方法等新类型。
- 📅 **Temporal API 类型支持**：内置了 Stage 4 的 Temporal 提案类型，可通过 `--target esnext` 或 `"lib": ["esnext"]` 使用。
- 🗺️ **Map 新增 `getOrInsert` 方法**：支持 `Map.getOrInsert(key, default)` 和 `getOrInsertComputed`，简化键值默认值模式。
- 🔧 **DOM 类型整合**：`dom.iterable` 和 `dom.asynciterable` 现在已合并到 `dom` 库中，无需再单独引用。
- ⚠️ **大量默认值变更与弃用**：`strict` 默认开启、`module` 默认 `esnext`、`target` 默认 `es2025`；弃用 ES5 目标、`downlevelIteration`、`moduleResolution node`、AMD/UMD/SystemJS 模块、`baseUrl`、`outFile` 等。
- 🛠️ **迁移准备**：新增 `"ignoreDeprecations": "6.0"` 选项可临时忽略弃用警告，但 7.0 将彻底移除这些功能。推荐使用 `ts5to6` 工具自动调整部分配置。

---

### [CVE-2026-48931 本不应是一个 CVE](https://adventures.nodeland.dev/archive/cve-2026-48931-shouldnt-have-been-a-cve/)

**原文标题**: [CVE-2026-48931 Shouldn't Have Been a CVE ](https://adventures.nodeland.dev/archive/cve-2026-48931-shouldnt-have-been-a-cve/)

### 概述总结
CVE-2026-48931 涉及 Node.js http.Agent 中的 HTTP/1.1 响应队列投毒问题，作者承认将其归类为漏洞并紧急修复是错误决定，导致 node-fetch@2 出现回归问题，影响了大量下游项目。该问题本质是协议特性而非漏洞，修复仅能缓解而非消除风险。

- 🛡️ **问题本质**：HTTP/1.1 无响应标识符，依赖连接顺序匹配请求与响应，攻击者可在空闲套接字注入额外响应，导致后续请求错位。
- ⚠️ **错误分类**：作者认为该问题不应被列为 CVE，因为所有 HTTP/1.1 客户端均存在相同竞争条件，且修复无法彻底消除风险，仅属防御性加固。
- 💥 **回归影响**：修复引入的 `'data'` 监听器导致 node-fetch@2 误报 `ERR_STREAM_PREMATURE_CLOSE` 错误，波及 Google API、Firebase、Backstage 及官方 Docker 镜像。
- 🔧 **后续修复**：改用内部 `onread` 钩子避免公开监听器，并需回滚至 22.x 和 24.x 版本以解除 node-fetch@2 用户阻塞。
- 📚 **最佳实践**：建议将安全修复用于真正漏洞，而非防御性加固；普通发布流程应优先，避免安全发布带来的广泛影响。
- 🤖 **AI 报告挑战**：AI 生成的高质量漏洞报告激增（2025 年 12 月 21 份增至 2026 年 3 月 64 份），但仅 12% 为真实问题，导致人工审查资源不足，易误判。
- 💡 **作者反思**：应区分“真实问题”与“是否需要 CVE”；检查套接字层修复的副作用；优先文档说明而非代码修复，以明确 HTTP/1.1 信任边界。

---

### [ECMAScript 2026 新特性 | pawelgrzybek.com](https://pawelgrzybek.com/whats-new-in-ecmascript-2026/)

**原文标题**: [What's new in ECMAScript 2026 | pawelgrzybek.com](https://pawelgrzybek.com/whats-new-in-ecmascript-2026/)

ECMAScript 2026 引入了多项新特性，包括异步数组转换、更安全的错误检测、高精度数值求和、Base64/Hex 转换、迭代器组合、JSON 解析优化以及 Map 的便捷插入方法。

- 📜 **Array.fromAsync**：新增从异步迭代器或产生 Promise 的同步生成器创建数组的方法，填补了之前缺少静态方法的空白。
- 🛡️ **Error.isError**：提供比 `instanceof Error` 更安全的错误类型检测方式，避免跨 realm 问题。
- ➕ **Math.sumPrecise**：高精度求和函数，能避免浮点数精度丢失问题，替代了 `Array.reduce` 的繁琐写法。
- 🔄 **Uint8Array 与 Base64/Hex 互转**：内置方法 `toBase64()`、`toHex()` 及对应的 `fromBase64()`、`fromHex()`，减少外部依赖。
- 🔗 **Iterator.concat**：支持将多个迭代器按顺序合并，并可方便地插入中间值，简化了迭代器组合逻辑。
- 📝 **JSON.parse 源文本访问**：`JSON.parse` 的 reviver 回调新增第三个参数 `source`，可获取原始字符串，解决大数精度丢失和 BigInt 序列化问题。
- 🗂️ **Map/WeakMap 的 Upsert 方法**：新增 `getOrInsert` 方法，无需手动检查键是否存在即可插入或获取值，减少样板代码。

---

### [ECMA-262 - Ecma 国际](https://ecma-international.org/publications-and-standards/standards/ecma-262/)

**原文标题**: [ECMA-262 - Ecma International](https://ecma-international.org/publications-and-standards/standards/ecma-262/)

ECMAScript 2026 第 17 版规范正式发布，定义了通用编程语言标准，提供 HTML 和 PDF 版本，并包含历史版本存档及反馈渠道。

- 📜 规范定义：ECMA-262 第 17 版（2026 年 6 月）定义 ECMAScript 2026 通用编程语言标准
- 🌐 版本说明：HTML 版为规范正本，PDF 版仅供打印参考
- 📅 历史版本：提供从 1997 年第 1 版到 2025 年第 16 版的完整 PDF 存档下载
- ⚠️ 版本空缺：第 4 版标准号保留但未发布，实际不存在
- 🐛 反馈渠道：最新草案可在 tc39.es/ecma262 查看，通过 GitHub 提交 bug 报告
- 🏷️ 分类信息：属于软件工程与接口类别，由 TC39 技术委员会维护

---

### [你不应该信任可信发布](https://blog.yossarian.net/2026/07/07/You-shouldnt-trust-trusted-publishing)

**原文标题**: [You shouldn't trust Trusted Publishing](https://blog.yossarian.net/2026/07/07/You-shouldnt-trust-trusted-publishing)

概述总结
Trusted Publishing 是一种机器对机器的身份验证机制，用于包索引与 CI/CD 工作流之间的信任建立，但绝不能作为用户判断包安全或质量的依据。

- 🔐 Trusted Publishing 本质是机器间信任，而非人类信任——它仅验证上传来源，不证明包的安全性。
- 🤖 该机制通过 OIDC 联邦实现短期、最小权限凭证，减少长期凭证泄露风险，但仍有被攻破的可能。
- ✅ PyPI 刻意避免将 Trusted Publishing 渲染为“绿色勾选”等信任信号，防止用户误用。
- 📄 包详情页中 Trusted Publishing 状态仅显示为简单的“是/否”，无任何信任暗示。
- ⚠️ 任何人都可使用 Trusted Publisher 上传任意内容（包括恶意软件），与 API 令牌无异。
- 🧩 Trusted Publishing 与“证明”（attestations）不同：后者是附加签名，同样不自动代表可信。
- 🛡️ 尽管有局限性，该机制仍是包装生态系统的净收益，减少了用户暴露于长期凭证的风险。

---

### [npm 包的可信发布 | npm 文档](https://docs.npmjs.com/trusted-publishers/)

**原文标题**: [Trusted publishing for npm packages | npm Docs](https://docs.npmjs.com/trusted-publishers/)

npm 的受信任发布功能允许你通过 CI/CD 工作流直接发布包，使用 OIDC 身份验证，无需长期令牌，从而提升安全性。

- 🔐 **工作原理**：通过 OIDC 在 npm 和 CI/CD 提供商之间建立信任关系，每次发布使用短期、加密签名的令牌，消除长期令牌的安全风险。
- 🛠️ **支持的提供商**：目前支持 GitHub Actions（GitHub 托管运行器）、GitLab CI/CD（GitLab.com 共享运行器）和 CircleCI（CircleCI 云），暂不支持自托管运行器。
- 📋 **配置步骤**：首先在 npmjs.com 的包设置中添加受信任发布者，填写提供商相关字段（如仓库、工作流文件名等），然后配置 CI/CD 工作流以启用 OIDC 权限。
- 🔒 **安全建议**：强烈建议在配置受信任发布后，限制传统令牌访问，并考虑使用阶段发布权限以实现最高安全性。
- 🏷️ **自动溯源生成**：从 GitHub Actions 或 GitLab CI/CD 发布时，npm 会自动生成并发布溯源证明（公共仓库和公共包适用），CircleCI 暂不支持。
- ⚠️ **故障排除**：发布时遇到身份验证错误，请检查工作流文件名是否匹配、运行器类型是否正确，以及 GitHub 上是否设置了 `id-token: write` 权限。
- 🔄 **限制与未来**：每个包只能配置一个受信任发布者，支持云托管运行器，未来计划扩展至更多提供商和自托管运行器。

---

### [为什么“可信发布”无法拯救我们免受社会工程攻击](https://adventures.nodeland.dev/archive/why-trusted-publishing-can-t-save-us/)

**原文标题**: [Why “Trusted Publishing” Can’t Save Us from Social Engineering](https://adventures.nodeland.dev/archive/why-trusted-publishing-can-t-save-us/)

### 概述总结
本文探讨了 npm“可信发布”机制在社交工程攻击面前的局限性，指出其无法验证发布者是否处于自主控制状态，并提出了更有效的安全改进措施。

- 🎯 **核心问题**：可信发布仅验证“谁发布了包”，但无法判断发布者是否被恶意控制，在身份劫持攻击中反而为恶意包提供虚假可信度。
- 🕵️ **事件背景**：Axios 包遭社交工程攻击，攻击者通过假 Slack 工作区诱骗维护者安装恶意软件，劫持其浏览器会话后以合法身份发布恶意版本。
- ⚠️ **攻击范围**：同一攻击针对多位高影响力 Node.js 维护者（如 Feross、Jordan Harband 等），表明维护者身份已成为系统性攻击目标。
- 🔍 **技术缺陷**：即使使用 Sigstore/OIDC 等可信发布工具，攻击者通过劫持已认证会话仍能通过所有验证，因为系统无法区分“合法身份”与“被控身份”。
- 💥 **实际后果**：恶意 Axios 版本进入 OpenAI 的 macOS 签名流水线，导致其需轮换代码签名证书，暴露了依赖自动更新策略的风险。
- 🛡️ **改进建议**：引入新版本发布延迟窗口（如 minimumReleaseAge）、设备/会话异常检测、高影响力包的双人审核发布机制，并放弃“信任发布者即安全”的假设。
- 📉 **根本反思**：过去五年重大供应链攻击（xz utils、ESLint-scope、Axios）均遵循“劫持维护者→以合法身份发布→利用信誉扩散”的模式，需重新设计发布系统以应对身份劫持风险。

---

### [生产环境中的 Node.js 工作线程 - Inngest 博客](https://www.inngest.com/blog/node-worker-threads-production)

**原文标题**: [Node.js worker threads in production - Inngest Blog](https://www.inngest.com/blog/node-worker-threads-production)

### 概览总结
本文详细介绍了在生产环境中使用 Node.js Worker Threads 的实践经验，重点在于如何构建一个可靠的生产级系统，而非简单的演示。

- 🧵 **明确线程边界**：Worker 线程负责 WebSocket 连接、心跳和租约续期；主线程负责用户函数执行和日志记录，避免序列化复杂对象。
- 📨 **将 postMessage 视为 API 边界**：定义明确的双向消息协议，包含方向、类型、关联 ID 和结构化克隆安全的数据载荷。
- 🔄 **回调转为请求 - 响应协议**：用户函数处理通过 postMessage 实现 RPC 风格通信，主线程解码请求并返回编码后的响应。
- 📦 **发送简单数据**：使用 protobuf 编码的 Uint8Array 作为消息载荷，避免传递富对象或类实例，确保协议清晰且可复用。
- 🔌 **代理无法跨越边界的对象**：为日志记录器等创建消息代理，将调用转为 postMessage 日志消息，由主线程调用真实实现。
- 🏗️ **将 Worker 作为构建产物**：确保 Worker 文件在开发、测试和发布包中正确存在，处理 TypeScript 和 ESM/CJS 兼容性问题。
- 🔄 **重启 Worker 并限制崩溃循环**：实现指数退避重试，达到崩溃阈值后停止重启并记录错误，避免无限循环。
- 📊 **镜像 Worker 健康状态**：Worker 定期发送调试快照（如连接状态、请求计数）到主线程，便于排查问题。
- 🛑 **优雅关闭协议**：关闭时先发送 CLOSE 消息，等待 Worker 完成清理（如刷新缓冲区、通知网关暂停），再让 Worker 退出。
- 🧪 **测试生命周期而非仅线程**：通过透明 WebSocket 代理模拟网络中断、关闭和重启场景，验证 Worker 在复杂条件下的行为。

---

### [GitHub - sindresorhus/terminal-image: 在终端中显示图片](https://github.com/sindresorhus/terminal-image)

**原文标题**: [GitHub - sindresorhus/terminal-image: Display images in the terminal · GitHub](https://github.com/sindresorhus/terminal-image)

terminal-image 是一个在终端中显示图片的 Node.js 模块，支持多种终端和协议，可灵活调整图片尺寸与渲染方式。

- 🖼️ **多终端兼容**：在 iTerm、Kitty、WezTerm 等支持图形协议的终端中显示全分辨率图片，其他终端则使用 ANSI 块字符渲染。
- 📦 **简单安装与使用**：通过 `npm install terminal-image` 安装，使用 `terminalImage.file('unicorn.jpg')` 即可在终端显示图片。
- 📐 **灵活尺寸调整**：支持按百分比或行列数设置图片宽高，例如 `width: '50%'` 或 `width: 50`，默认保持宽高比。
- 🔄 **宽高比控制**：设置 `preserveAspectRatio: false` 可强制缩放图片适应终端尺寸，但会改变原始比例。
- 🎞️ **GIF 动画支持**：提供 `gifBuffer` 和 `gifFile` 方法显示动画 GIF，并可通过 `maximumFrameRate` 和 `renderFrame` 自定义帧率与渲染逻辑。
- 🛠️ **丰富 API**：支持图片缓冲区（`buffer`）和文件路径（`file`）两种输入方式，返回包含 ANSI 转义码的字符串。
- 🔌 **自动协议检测**：优先使用 Kitty Graphics Protocol 或 iTerm2 Inline Images Protocol 实现全分辨率，否则回退到 ANSI 块字符。
- 💡 **实用示例**：结合 `got` 库可显示远程图片，如 `terminalImage.buffer(body)`。
- 📚 **相关资源**：提供 CLI 工具、终端链接模块和样式工具，并有 MIT 许可证及贡献指南。

---

### [GitHub - paradedb/drizzle-paradedb：用于ParadeDB的Drizzle官方扩展](https://github.com/paradedb/drizzle-paradedb)

**原文标题**: [GitHub - paradedb/drizzle-paradedb: Official extension to Drizzle for use with ParadeDB · GitHub](https://github.com/paradedb/drizzle-paradedb)

paradedb/drizzle-paradedb 是一个官方 Drizzle 集成库，用于在 PostgreSQL 中实现 Elastic-quality 搜索功能，支持 BM25 索引管理和完整 ParadeDB API 查询。

- 🎯 **核心功能**：提供 Drizzle 与 ParadeDB 的官方集成，支持 BM25 索引管理和查询
- 🔧 **技术要求**：Node 22.12+、Drizzle 1.0+、ParadeDB 0.22.0+、PostgreSQL 15+
- 📚 **示例丰富**：包含快速入门、分面搜索、自动补全、相似查询、混合 RRF 和 RAG 等示例
- 🤝 **社区支持**：提供 Slack 社区、GitHub Discussions 和商业支持选项
- 📜 **开源许可**：基于 MIT 许可证发布，代码贡献遵循 CONTRIBUTING.md 指南
- 🛠️ **开发状态**：已有 80 次提交、14 颗星、2 个复刻，最新版本 v0.1.0（2026 年 5 月）

---

### [GitHub - sindresorhus/eslint-node-test: 针对 Node.js 内置测试运行器（`node:test`）的 ESLint 规则](https://github.com/sindresorhus/eslint-node-test)

**原文标题**: [GitHub - sindresorhus/eslint-node-test: ESLint rules for the Node.js built-in test runner (`node:test`) · GitHub](https://github.com/sindresorhus/eslint-node-test)

eslint-node-test 是一个为 Node.js 内置测试运行器 `node:test` 提供 ESLint 规则的插件，帮助开发者避免常见错误并编写更一致的测试代码。

- 📦 安装要求：需要 ESLint >=10.4、flat config 和 ESM，通过 `npm install --save-dev eslint eslint-node-test` 安装。
- ⚙️ 使用方式：支持预设配置（如 `recommended`）或单独配置规则，规则仅对导入 `node:test` 的文件生效。
- 📋 规则丰富：涵盖 60+ 条规则，包括断言参数、测试标题、钩子顺序、异步处理等，部分规则可自动修复或手动修复。
- 🏷️ 预设配置：提供 `recommended`、`unopinionated` 和 `all` 三种配置，方便不同场景使用。
- 🔧 规则分类：包含配置标记（如 `✅` 表示推荐、`🔧` 表示可自动修复）和详细说明，提升可维护性。
- 📂 项目状态：开源项目（MIT 许可），拥有 42 颗星和 1 个 fork，最新版本为 v0.2.0。

---

### [Upyo | 跨运行时电子邮件库](https://upyo.org/)

**原文标题**: [Upyo | Cross-runtime email library](https://upyo.org/)

概述摘要
- 📧 核心功能：消息撰写与附件管理
- 🚚 传输方式：支持 SMTP、JMAP、Lettermint、Mailgun、Plunk、Resend、SendGrid、Amazon SES 等
- 🔄 高级传输：包含池传输、重试传输、OpenTelemetry、模拟传输及自定义传输
- 📚 参考文档：涵盖@upyo/core、@upyo/smtp、@upyo/jmap 等核心包
- ⚠️ 不稳定状态：部分功能标注为"Unstable"（不稳定）

---

### [发布 v6.0.0 · webpack/webpack-dev-server · GitHub](https://github.com/webpack/webpack-dev-server/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · webpack/webpack-dev-server · GitHub](https://github.com/webpack/webpack-dev-server/releases/tag/v6.0.0)

页面显示加载错误，提示重新加载。以下是 webpack-dev-server v6.0.0 版本更新的主要内容：

- 🚀 **重大变更**：升级 Express 至 v5，webpack 依赖范围提升至^5.101.0，并放弃对 Node.js < 22.15.0 的支持。
- 📦 **模块转换**：源码转为原生 ES 模块，同时提供 ESM 和 CommonJS 构建，通过 exports 字段区分。
- ❌ **移除功能**：删除 CLI 标志、SockJS 支持、spdy 依赖、internalIP 方法、代理 bypass 选项等，改用替代方案。
- 🔄 **依赖更新**：http-proxy-middleware 升级至 v4，webpack-dev-middleware 升级至 v8，chokidar 升级至 v5。
- 🛠️ **插件支持**：新增插件功能，可集成到 webpack 编译器生命周期，支持 MultiCompiler 多服务器设置。
- 🔒 **安全增强**：拒绝跨站请求访问内部端点（如 open-editor），要求同源验证。
- 🌐 **HTTP/2优化**：启用压缩中间件支持 HTTP/2 连接。
- 🧪 **测试迁移**：测试套件从 Jest 迁移至 node:test，并配置 jsdom 环境。

---

### [GitHub - xojs/xo: ❤️ 默认配置极佳的 JavaScript/TypeScript 代码检查工具（ESLint 封装）](https://github.com/xojs/xo)

**原文标题**: [GitHub - xojs/xo: ❤️ JavaScript/TypeScript linter (ESLint wrapper) with great defaults · GitHub](https://github.com/xojs/xo)

XO 是一个基于 ESLint 的 JavaScript/TypeScript 代码风格检查工具，提供零配置、强默认规则和丰富的插件支持，旨在简化代码风格统一流程。

- ❤️ 零配置开箱即用，自动检查所有 JS/TS 文件（排除常见忽略路径），并支持 TypeScript 默认集成。
- 🎨 强制可读代码风格（如 tab 缩进、分号、单引号、尾逗号等），减少代码审查中的风格争论。
- ⚡ 内置缓存提升性能，支持 `--fix` 自动修复问题，以及 `--open` 在编辑器中定位错误行。
- 📦 通过 `npm init xo` 快速初始化项目，并支持 `xo.config.js` 或 `package.json` 配置。
- 🔧 高度可配置：可自定义缩进（空格/tab）、分号、Prettier 集成（格式化或兼容模式），以及忽略规则。
- 🧩 集成多种 ESLint 插件（如 unicorn、import-x、ava、n 等），并支持 Astro、React、Svelte、Vue 等框架。
- 🚀 提供共享配置（如 eslint-config-xo）和编辑器插件（VSCode、Sublime Text 等），方便与 ESLint 直接配合。
- 📊 支持批量抑制规则（通过 `eslint-suppressions.json` 文件），便于逐步采用严格规则。
- 🏆 拥有 8k+ Stars、306 Forks，社区活跃，提供徽章和 Twitter 支持。

---

### [GitHub - azat-io/eslint-plugin-perfectionist: ☂️ 用于排序对象、导入、类型、枚举、JSX 属性等各种数据的 ESLint 插件](https://github.com/azat-io/eslint-plugin-perfectionist)

**原文标题**: [GitHub - azat-io/eslint-plugin-perfectionist: ☂️ ESLint plugin for sorting various data such as objects, imports, types, enums, JSX props, etc. · GitHub](https://github.com/azat-io/eslint-plugin-perfectionist)

ESLint 插件 Perfectionist 是一个用于排序代码中各种数据（如对象、导入、TypeScript 类型、枚举、JSX 属性等）的工具，所有规则均可自动修复，旨在提升代码的可读性、可维护性和一致性。

- 📖 **提升可读性**：排序后的代码让查找声明更快，因为阅读代码的频率远高于编写。
- 🔧 **自动修复**：所有规则都支持 `--fix` 自动修复，使用安全且方便。
- 🎨 **美化代码**：不仅功能实用，还能让代码结构视觉上更和谐，如同“美容院”般提升代码外观。
- 🚀 **安装简便**：需先安装 ESLint v8.45.0+，再通过 npm 安装 `eslint-plugin-perfectionist`。
- ⚙️ **配置灵活**：支持扁平配置（`eslint.config.js`）和传统配置（`.eslintrc.js`），并提供预置配置如 `recommended-natural`。
- 📋 **丰富规则**：包含 24 条规则，覆盖数组、类、装饰器、枚举、导入、接口、JSX 属性、对象、集合等，均带自动修复和推荐标记。
- ❓ **常见问题**：可在编辑器中启用自动修复；插件安全，考虑展开运算符和注释；与 Prettier 不同，ESLint 负责风格而非格式化。
- 📜 **版本与贡献**：遵循语义化版本和 ESLint 版本策略，欢迎参与贡献，采用 MIT 许可证。

---

### [发布 v7.5.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.5.0)

**原文标题**: [Release v7.5.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.5.0)

以下是对所提供内容的概述摘要：

- 📦 MongoDB Node.js 驱动程序发布 v7.5.0 版本（2026 年 7 月 7 日）
- 🔐 支持 MongoDB 9.0 的 Queryable Encryption 字符串查询 GA（正式可用），包括精确和范围匹配
- 🔄 API 重命名：`TextOpts` 改为 `StringOpts`，`TextPreview` 改为 `String`
- ✅ `prefix`、`suffix`、`substring` 查询类型正式可用，`prefixPreview` 等预览类型已弃用
- 🛠️ `MongoClient.close()` 现在能关闭所有服务器上正在使用的连接，修复了副本集和分片集群中的错误
- 🐛 感谢 @Nepomuk5665 和 @sarthaksoni25 报告问题及提供初步实现
- 📖 提供 API 参考和变更日志文档，鼓励用户试用并报告问题

---

### [GitHub - hmenyus/node-calls-python: 在 NodeJS 中直接进程内调用 Python，无需生成子进程 · GitHub](https://github.com/hmenyus/node-calls-python)

**原文标题**: [GitHub - hmenyus/node-calls-python: Call Python from NodeJS directly in-process without spawning processes · GitHub](https://github.com/hmenyus/node-calls-python)

node-calls-python 是一个可直接在 Node.js 进程中调用 Python 代码的库，无需创建子进程，适合机器学习与深度学习模型的集成。

- 🚀 **无需子进程**：通过嵌入式 Python 解释器直接运行代码，避免 IPC 和进程创建的开销，性能更优
- 📦 **安装简单**：支持 Linux、Windows、Mac，需安装 Node、Python、node-gyp 等依赖
- 🔄 **同步与异步 API**：提供 `call/callSync`、`create/createSync`、`exec/eval` 等灵活调用方式
- 🧩 **支持类与对象**：可在 Node 中实例化 Python 类并调用其方法
- 🔁 **热重载与开发模式**：支持模块重新导入和自动检测代码变更，便于开发
- 🧠 **kwargs 与回调**：支持传递 Python 关键字参数，以及将 JavaScript 函数传给 Python 调用
- ⚙️ **兼容性**：支持 ES 模块、Next.js、Python venv、multiprocessing 等场景
- 🛠️ **数据映射**：自动转换 Node 与 Python 类型（如数组↔列表、对象↔字典、Buffer↔字节）
- 📊 **ML 示例**：可集成 scikit-learn 等库，直接在 Node 中训练或预测

---

### [版本 5.3 发布说明 | FoalTS](https://foalts.org/blog/2026/07/09/version-5.3-release-notes/)

**原文标题**: [Version 5.3 release notes | FoalTS](https://foalts.org/blog/2026/07/09/version-5.3-release-notes/)

概述摘要  
Foal 版本 5.3 发布，新增开发详细日志格式、HTTP 422 响应类以及 AWS S3 路径样式选项。

- 🎉 新增 `dev-verbose` 日志格式，结合 `dev` 的彩色简洁和 `raw` 的完整参数显示，适合开发环境调试。
- ⚙️ 使用方式：在配置文件中设置 `"format": "dev-verbose"`，避免重复显示已包含在消息行中的参数。
- 🆕 新增 `HttpResponseUnprocessableContent` 类（HTTP 422），用于返回“不可处理内容”响应。
- ☁️ `@foal/aws-s3` 包新增 `forcePathStyle` 选项，支持路径样式请求，兼容 MinIO 或 LocalStack 等 S3 兼容服务。

---

### [发布 v5.10.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.10.0)

**原文标题**: [Release v5.10.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.10.0)

Fastify v5.10.0 版本发布，包含多项文档改进、功能增强和性能优化。

- 📚 文档改进：修复多处文档链接、示例错误，并更新了类型提供者、日志记录等文档内容
- 🆕 新功能：引入日志控制器层，增强日志管理能力
- 🐛 错误修复：修复了 `reply.hijack()` 中 `socket._meta` 的清除问题，以及 `reply.send` 对 `json` 和 `charset` 的检测
- ⚡ 性能优化：减少请求生命周期中的每请求开销，并优化 `request.port` 的派生逻辑
- 🔧 依赖更新：将 `fast-json-stringify` 从 6.4.0 升级到 7.0.0，并更新了 TypeScript 类型依赖
- 👥 新贡献者：5 位新贡献者首次参与项目，包括文档修复和社区插件添加

---

### [GitHub - jpmonette/feed: 一款适用于 Node.js 的 RSS、Atom 和 JSON Feed 生成器，让内容聚合变得简单直观！🚀](https://github.com/jpmonette/feed)

**原文标题**: [GitHub - jpmonette/feed: A RSS, Atom and JSON Feed generator for Node.js, making content syndication simple and intuitive! 🚀 · GitHub](https://github.com/jpmonette/feed)

概述摘要  
该页面为 GitHub 上 jpmonette/feed 项目的仓库主页，显示公共访问状态，包含代码、问题、拉取请求、操作、安全与质量、洞察等导航选项，以及星标、分叉和通知设置等核心功能。

- ⚠️ 页面加载时出现错误，提示用户重新加载
- 🔔 通知设置需登录后才能更改
- ⭐ 项目获得 1.4k 星标和 226 个分叉
- 📂 提供代码、问题（20 个）、拉取请求（6 个）等主要功能模块
- 🔒 包含操作、安全与质量、洞察等高级导航选项

---

### [远程站点可靠性工程师 | Crystallize 职业机会](https://crystallize.com/careers/senior-sre)

**原文标题**: [Remote Site Reliability Engineer | Crystallize Careers](https://crystallize.com/careers/senior-sre)

Crystallize 正在招聘一名远程高级站点可靠性工程师（SRE），负责维护其全球可扩展的 GraphQL API 平台，支持无头电商服务。

- 🚀 职位概述：寻找远程高级 DevOps/后端工程师，负责确保面向全球的无头电商 GraphQL API 服务快速、可观察且具有弹性。
- 🎯 核心职责：拥有平台可靠性、可扩展性和性能，定义 SLO 和错误预算，设计优雅降级系统，并做出可靠性/速度权衡。
- 🔧 工作内容：制定 SLO/SLA、构建可观测性（指标、追踪、日志）、管理事件响应、扩展异步分布式架构（MongoDB Atlas）、优化 CI/CD 和基础设施即代码，并监控云成本和安全性。
- 💻 技术栈：Node/TypeScript、GraphQL、AWS（ECS/EKS/Lambda）、MongoDB Atlas、Terraform、Cloudflare Workers。
- 👤 候选人要求：具备软件或系统工程背景，能设计可扩展的分布式系统，熟练管理 AWS 和基础设施即代码（Terraform），熟悉 TypeScript/GraphQL 代码库，并有处理多租户 SaaS 或电商流量模式的经验者优先。
- 🌱 成长机会：在快速成长的公司中从事多样化、有挑战性的工作，鼓励知识共享，推动互联网工艺边界。

---

