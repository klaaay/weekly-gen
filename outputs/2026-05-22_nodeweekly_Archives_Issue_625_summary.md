### [Node 周刊第 625 期：2026 年 5 月 21 日](https://nodeweekly.com/issues/625)

**原文标题**: [Node Weekly Issue 625: May 21, 2026](https://nodeweekly.com/issues/625)

以下是 Node Weekly 第 625 期的内容摘要：

Node Weekly 第 625 期涵盖了 Express.js 的重大更新、npm 的分阶段发布功能、安全事件、Deno 和 Node.js 的新版本，以及一系列工具和生态系统的动态。

- 🚀 **Express.js 焕然一新**：长期停滞的 Express.js 经过 2024 年的大规模重构，如今品牌、网站和文档全面升级至 2026 年水平。
- 📦 **npm 推出分阶段发布**：npm 11.15.0 新增“分阶段发布”模式，允许在包上线前设置审查期，npm 12.0 的预发布也已推出。
- 🔒 **安全与供应链问题**：GitHub 提议默认将 npm 安装脚本设为可选；Shai Hulud 攻击再次影响数百个包，node-ipc 被植入凭据窃取器。
- 🆕 **Deno 2.8 即将发布**：本周发布，将带来巨大的 Node.js 兼容性改进、import defer 和 TypeScript 6.0.3 支持。
- 🛠️ **Node.js 26.2.0 发布**：stream.compose 标记为稳定，fs.Stats 和 BigIntStats 支持 Temporal.Instant。
- 📝 **其他亮点**：包括从 Axios 迁移到 fetch 的官方 codemod、TypeORM 1.0 正式版、ESLint 10.4 和 pnpm 11.2 等工具更新。
- 🌐 **生态系统动态**：Bun 的 Zig 转 Rust 重写已合并，Wasp 框架创始人分享从自创语言转向 Node 的经验，以及通过 node:ffi 在终端玩 Doom 的有趣项目。

---

### [Express.js 的新面貌](https://expressjs.com/en/blog/2026-05-18-a-new-look-for-express/)

**原文标题**: [A New Look for Express · Express.js](https://expressjs.com/en/blog/2026-05-18-a-new-look-for-express/)

Express 网站进行了全面改版，包括新设计、新标志和更好的文档体验。

- 🎨 全新网站设计：从 Jekyll 迁移到 Astro，提升了性能、国际化支持和内容管理灵活性。
- 📚 文档改进：新增版本切换、AI 搜索（基于 Orama）和 llms.txt 支持，方便开发者快速找到信息。
- 🚀 未来计划：填补内容空白、完善翻译、确保文档与版本同步，并鼓励社区贡献。
- 🖌️ 新标志：通过社区协作设计，体现 Express 的简洁与清晰，代表项目新篇章。
- 🤝 社区驱动：由 Sebastian Beltran 领导，Orama 团队赞助，众多贡献者参与，历时一年多完成。

---

### [Fastify：一个快速且低开销的 Node.js Web 框架](https://fastify.dev/)

**原文标题**: [Fast and low overhead web framework, for Node.js | Fastify](https://fastify.dev/)

Fastify 是一个高效、可扩展的 Node.js 网页框架，专注于提供最佳开发者体验和卓越性能，每月下载量超千万次，广泛应用于各类组织与产品中。

- 🚀 **高性能**：Fastify 是速度最快的网页框架之一，复杂代码下每秒可处理高达 3 万次请求。
- 🔧 **可扩展**：通过钩子、插件和装饰器实现完全扩展，支持自定义功能。
- 📋 **基于模式**：推荐使用 JSON Schema 验证路由和序列化输出，内部编译为高性能函数。
- 📝 **日志优化**：采用 Pino 日志库，几乎消除日志开销，兼顾重要性与成本。
- 👨‍💻 **开发者友好**：框架设计富有表现力，助力日常开发，且不牺牲性能与安全。
- 🅃 **TypeScript 支持**：提供类型声明文件，支持 TypeScript 社区。
- ⚡ **快速启动**：通过 npm 安装后，简单代码即可启动服务器，并支持 CLI 脚手架生成项目。
- ✅ **请求/响应验证**：结合 JSON Schema 和钩子，实现输入输出验证及预处理器操作。
- 🏢 **生态系统丰富**：拥有 292 个插件，覆盖数据库、模板语言等，易于编写新插件。
- 🤝 **社区与赞助**：由 Nearform、Platformatic 等赞助，隶属于 OpenJS Foundation，社区活跃。

---

### [Express.js 新篇章：2024 年的成就与 2025 年的雄心壮志 · Express.js](https://expressjs.com/en/blog/2025-01-09-rewind-2024-triumphs-and-2025-vision/)

**原文标题**: [A New Chapter for Express.js: Triumphs of 2024 and an ambitious 2025 · Express.js](https://expressjs.com/en/blog/2025-01-09-rewind-2024-triumphs-and-2025-vision/)

2024 年对 Express.js 而言是变革性的一年，项目在治理、安全和技术上取得重大突破，并发布了期待已久的 Express 5.0。2025 年则聚焦于自动化、安全强化和性能优化，旨在将 Express.js 打造成更快速、更安全的现代 Web 开发框架。

- 🏛️ **治理与社区里程碑**：通过“Express 前进计划”引入新一代技术委员会成员，成立安全工作组，并采用威胁模型，最终获得 OpenJS 基金会“影响项目”地位。
- 🚀 **技术突破：Express 5.0 发布**：经过十多年讨论，正式推出 Express 5.0，带来现代化功能和前瞻性架构，并已开始规划 Express 6.0。
- 🔒 **强化安全态势**：与 OpenJS 基金会和 OSTIF 合作完成安全审计，采用 OSSF Scorecard，快速响应多个 CVE 漏洞，并与 HeroDevs 建立“永不终止支持”计划。
- 🤖 **2025 年愿景：自动化 npm 发布**：通过自动化发布流程，减少人工错误，加快补丁和功能更新速度，提升用户信心。
- 📦 **引入作用域包**：转向作用域包，明确模块归属，减少混乱，便于组织扩展和社区贡献质量控制。
- 🛡️ **加强安全报告与流程**：完善漏洞报告和管理指南，为安全分诊团队和技术委员会提供培训，更深度集成 OSSF Scorecard。
- ⚡ **性能监控与深度优化**：系统监控框架及依赖性能，快速定位瓶颈，计划到 2026 年中实现核心代码和库的深度优化。
- 🧹 **淘汰遗留技术并增强文档**：逐步淘汰猴子补丁和依赖于 Node.js 内部的直通 API，减少技术债务，同时更新安全文档，涵盖会话处理、输入验证等最佳实践。

---

### [路由 · Express.js](https://expressjs.com/en/5x/guide/routing/)

**原文标题**: [Routing · Express.js](https://expressjs.com/en/5x/guide/routing/)

本指南詳細介紹了 Express 框架中的路由機制，涵蓋了從基本定義到進階應用的各個方面。

- 📖 **路由定義**：路由是應用程式端點 (URI) 如何回應客戶端請求的機制，透過 Express 的 `app` 物件方法 (如 `app.get()`, `app.post()`) 來定義。
- 🗺️ **路由路徑**：路徑可以是字串、字串模式或正則表達式，用於定義請求的端點，支援參數 (如 `:userId`) 和可選片段 (如 `{.:ext}`)。
- 🎯 **路由參數**：URL 中的命名片段，其值會被捕獲到 `req.params` 物件中，例如 `/users/:userId` 會捕獲 `userId` 的值。
- ⚙️ **路由處理器**：可以為一個路由提供多個回調函數 (類似中間件)，透過 `next()` 函數傳遞控制權，或使用 `next('route')` 跳過當前路由。
- 📨 **回應方法**：回應物件 (`res`) 提供多種方法 (如 `res.send()`, `res.json()`, `res.redirect()`) 來向客戶端發送回應並終止請求 - 回應循環。
- 🔗 **鏈式路由**：使用 `app.route()` 可以為單一路徑創建可鏈接的路由處理器，有助於減少冗餘和打字錯誤。
- 🧩 **模塊化路由**：使用 `express.Router` 類別可以創建模塊化、可掛載的路由處理器，形成「迷你應用」，並可透過 `mergeParams` 選項訪問父路由的參數。

---

### [通过上下文工程、RAG 和可靠评估框架构建可靠的 AI 功能。| Frontend Masters](https://frontendmasters.com/courses/ai-engineering/?utm_source=email&utm_medium=nodeweekly&utm_content=aiengineering)

**原文标题**: [Build reliable AI features through context engineering, RAG, and reliable eval harnesses. | Frontend Masters](https://frontendmasters.com/courses/ai-engineering/?utm_source=email&utm_medium=nodeweekly&utm_content=aiengineering)

本课程系统讲解了 AI 工程的核心实践，重点围绕构建、评估和迭代 AI 代理系统，涵盖从基础架构到高级优化的完整流程。

- 🤖 **课程概览**：由 Netflix 高级软件工程师 Scott Moss 主讲，时长 9 小时 5 分钟，旨在培养学员构建可测量、可改进的 AI 驱动系统的能力。
- 🛠️ **构建 AI 代理**：从零开始，使用 TypeScript 和 Cloudflare Durable Objects 构建一个基于 WebSocket 的 AI 聊天代理，集成 OpenAI SDK。
- 🎨 **集成画布应用**：将 AI 代理与 Excalidraw 绘图应用集成，实现通过自然语言生成和修改图表。
- 📊 **评估与评分**：建立评估框架（Eval Harness），使用黄金数据集和代码评分器，并通过 Braintrust 平台进行 AI 可观测性管理。
- 📝 **上下文工程**：优化系统提示词，引入 TOON 格式序列化画布状态，让代理能“看见”当前画布内容。
- 🔧 **高级工具开发**：将原始工具重构为客户端 CRUD 工具（添加、更新、删除），并集成网络搜索工具（Tavily）以获取实时信息。
- 🔄 **改进循环**：通过“运行评估→检查产品→形成理论→单点修改→重新评估”的迭代流程，持续提升代理性能。
- 📚 **检索增强生成（RAG）**：使用 Upstash Vector 建立向量数据库，实现内部文档的检索增强生成，突破模型知识截止限制。
- 🏁 **总结与展望**：强调数据飞轮、遥测、用户反馈和评估驱动的迭代是 AI 工程的核心，并展望了人工审核、持久化执行等进阶主题。

---

### [npm 包的分阶段发布 | npm 文档](https://docs.npmjs.com/staged-publishing/)

**原文标题**: [Staged publishing for npm packages | npm Docs](https://docs.npmjs.com/staged-publishing/)

npm 分阶段发布功能允许在包正式发布到注册表前增加一个审批步骤，确保代码经过审查后再公开。

- 📦 **分阶段发布流程**：包含“暂存”、“审查”和“批准”三个步骤，替代直接使用 `npm publish` 发布。
- 🔐 **前提条件**：需要拥有包的发布权限、包已存在于注册表中，且账户已启用双因素认证（2FA）。
- 🚀 **暂存包**：使用 `npm stage publish` 命令将包提交到暂存区，此步骤不要求 2FA。
- 🔍 **审查暂存包**：可通过 CLI（如 `npm stage list`、`npm stage view`）或 npmjs.com 的“Staged Packages”标签页查看和下载暂存包。
- ✅ **批准发布**：使用 `npm stage approve` 命令或 npmjs.com 上的“Approve”按钮，并需通过 2FA 验证才能正式发布。
- 🤝 **与可信发布集成**：支持在 CI/CD 中使用 OIDC 进行暂存发布，仍需维护者审批。
- 📚 **更多信息**：参考“可信发布”和“生成出处声明”等文档以深入了解。

---

### [发布 v11.15.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.15.0)

**原文标题**: [Release v11.15.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.15.0)

npm CLI v11.15.0 版本发布，新增多项功能并修复了若干问题。

- 🚀 新增 `npm stage` 命令，支持分阶段操作
- 🔒 为信任命令添加权限支持，增强安全性
- ⚙️ 引入 allow-git/allow-file/allow-directory/allow-remote 配置项
- 🐛 修复 `stage download --json` 输出按包名键控的问题
- 🛠️ 允许 `min-release-age` 与 `--before` 配置共存于 npmrc
- 🔧 重构失败节点逻辑，调整测试与安全性
- 🚫 `allow-remote=none` 不再阻止注册表 tarball 下载
- 📦 更新多个依赖，包括 socks、lru-cache、ip-address 等
- 🧹 更新开发依赖，涉及 arborist、config、libnpmdiff 等子包
- 👥 贡献者包括 reggi、owlstronaut 和 raazkhnl

---

### [发布 v12.0.0-pre.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.0.0)

**原文标题**: [Release v12.0.0-pre.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.0.0)

npm v12.0.0-pre.0.0 预发布版本，包含多项重大变更、新功能和错误修复。

- ⚠️ **重大变更**：`npm view --json` 现在始终返回数组；`npm sbom` 的 CycloneDX 格式使用 `package.json` 中的 `name` 字段；全局安装不再注册 man 页面；`npm pkg` 输出不再强制为 JSON；移除了 `npm shrinkwrap` 命令；移除了 Twitter 和 Freenode 个人资料字段；不再通过 `which node` 解析 Node 路径；`npm pack` 和 `npm publish` 的 JSON 输出格式已统一；移除了 `star`、`stars` 和 `unstar` 命令；移除了 `npm adduser` 命令。
- ✨ **新功能**：新增 `npm stage` 命令；为信任命令添加权限支持；新增 `allow-git`、`allow-file`、`allow-directory`、`allow-remote` 配置项；移除 `npm-shrinkwrap.json` 支持；移除 Twitter 和 Freenode 个人资料字段；移除 star 相关命令；为 `update` 命令添加 `u` 别名；新增 backport 脚本。
- 🐛 **错误修复**：按包名键控 `stage download --json` 输出；允许 `min-release-age` 与 `--before` 共存；`allow-remote=none` 不阻止注册表 tarball；移除设置；SBOM 去重依赖关系；`--json` 输出不再解包单元素数组；对齐 CycloneDX SBOM 组件名称；不安装 man 页面到系统位置；`npm pkg` 输出类似 `npm view`；忽略预期错误代码；停止通过 `which node` 解析 Node 路径；同步 `pack` 和 `publish` 的 JSON 输出；移除 `npm adduser` 命令。
- 📖 **文档更新**：为 `optionalDependencies` 部分添加示例；更新 `npm view` 带 JSON 输出的文档。
- 📦 **依赖更新**：更新了 `socks`、`lru-cache`、`ip-address`、`brace-expansion`、`bin-links`、`tar`、`semver`、`hosted-git-info`、`node-gyp`、`is-cidr`、`@sigstore/protobuf-specs`、`tinyglobby`、`picomatch`、`diff`、`minimatch`、`minipass-flush` 等多个依赖。
- 🔧 **杂项**：更新开发依赖；添加 CLI 分类团队作为代码所有者；重构测试；修复代码中的拼写错误；添加 backport 工作流的操作权限；backport 可触发 CI；不在 CI 中运行 `npm update`；启用预发布模式。

---

### [[RFC] 使安装脚本成为可选加入 由 JamieMagee 提交 · 拉取请求 #868 · npm/rfcs · GitHub](https://github.com/npm/rfcs/pull/868)

**原文标题**: [[RFC] Make install scripts opt-in by JamieMagee · Pull Request #868 · npm/rfcs · GitHub](https://github.com/npm/rfcs/pull/868)

npm 计划默认禁止依赖安装脚本，改为用户主动选择允许，以提升安全性。

- 🔒 默认禁止安装脚本：npm 将默认阻止依赖的 `preinstall`、`install`、`postinstall` 和 `node-gyp` 构建脚本，用户需通过 `package.json` 中的 `allowScripts` 字段或 `.npmrc` 文件主动选择允许。
- 🛡️ 新增命令：引入 `npm approve-scripts` 和 `npm deny-scripts` 命令，帮助用户构建和维护允许列表，支持按版本精确锁定或仅按包名允许。
- 🚨 安全背景：近期多起供应链攻击（如 Shai-Hulud 蠕虫、Axios 事件）均通过安装脚本自动执行恶意代码，npm 是唯一仍默认运行安装脚本的主流包管理器。
- 🔧 分阶段实施：第一阶段仅发出警告，不阻止脚本；后续阶段将真正阻止未批准的脚本，并提供 `dangerously-allow-all-scripts` 等逃生口。
- 💬 社区讨论：部分开发者担忧 `allowScripts` 放在 `package.json` 会暴露安全策略，但多数认为这仍是重大改进，且可通过 `.npmrc` 或 CLI 参数私有化配置。

---

### [迷你沙虫冲击@antv 生态系统，639 个 npm 包被篡改...](https://socket.dev/blog/antv-packages-compromised)

**原文标题**: [Mini Shai-Hulud Hits @antv Ecosystem, 639 Compromised npm Pa...](https://socket.dev/blog/antv-packages-compromised)

概述：恶意 npm 包 art-template 被篡改，通过水坑攻击传播类似 Coruna 的 iOS Safari 漏洞利用框架，威胁用户设备安全。

- 🎯 受影响的 npm 包：art-template 被攻陷，成为攻击载体
- 🕸️ 攻击方式：采用水坑攻击（watering-hole attack），针对特定用户群体
- 📱 目标平台：iOS Safari 浏览器，利用漏洞框架进行攻击
- 🦠 恶意载荷：包含类似 Coruna 的漏洞利用工具包，可远程控制设备
- ⚠️ 安全风险：用户访问被篡改的网站后，可能导致敏感信息泄露或设备被控
- 🔍 建议措施：立即检查项目依赖，移除受影响的 art-template 版本，并更新至安全版本

---

### [流行 npm 包 node-ipc 被植入窃取凭证的恶意代码...](https://socket.dev/blog/node-ipc-package-compromised)

**原文标题**: [Popular node-ipc npm Package Infected with Credential Steale...](https://socket.dev/blog/node-ipc-package-compromised)

npm 因新一轮“迷你沙虫”攻击波及 323 个包，已撤销所有绕过双因素认证的细粒度访问令牌，同时分阶段发布功能进入公开预览。

- 🚨 npm 撤销所有绕过双因素认证的细粒度访问令牌，以应对安全威胁
- 🐛 新一轮“迷你沙虫”攻击浪潮导致 323 个 npm 包被入侵
- 🔄 分阶段发布功能已进入公开预览，旨在提升软件供应链安全

---

### [@deno.land 在 Bluesky 上](https://bsky.app/profile/deno.land/post/3mm6clkq5uc22)

**原文标题**: [@deno.land on Bluesky](https://bsky.app/profile/deno.land/post/3mm6clkq5uc22)

概述摘要  
Deno 2.8 本周发布，是迄今为止最大的次要版本，显著提升了 Node.js 兼容性，并引入了多项新功能。  

- 🚀 Node.js 兼容性从 42% 提升至 75% 以上，自 2.7 版本以来有 500 多个兼容性提交  
- 📦 支持 TypeScript 6.0.3 和`import defer`  
- 🛠 新增多个子命令、目录工作区和 CPU 火焰图  
- 🔧 包含许多其他改进和修复

---

### [Node.js — Node.js 26.2.0（当前版本）](https://nodejs.org/en/blog/release/v26.2.0)

**原文标题**: [Node.js — Node.js 26.2.0 (Current)](https://nodejs.org/en/blog/release/v26.2.0)

Node.js 26.2.0 版本发布，带来了多项新功能和改进。

- 📝 将 `stream.compose` 标记为稳定功能
- 🕐 为 `Stats` 和 `BigIntStats` 添加 `Temporal.Instant` 支持
- 📡 为 HTTP 模块新增 `writeInformation` 方法，支持发送任意 1xx 状态码
- 🔒 强化加密模块，包括 ML-DSA/ML-KEM 支持、ChaCha20-Poly1305 和 AES-KW 的 Web 加密实现
- 🛠️ 更新依赖：undici 8.3.0、corepack 0.35.0、sqlite 3.53.1、simdjson 4.6.4 等
- 🐛 修复多个流处理问题，优化广播和共享流的性能
- 🧪 测试框架新增标签选项和标签名称过滤器
- 📚 文档更新，包括贡献指南、QUIC 文档改进和构建说明
- 🔧 修复调试器、模块加载和 REPL 中的多个问题
- 🖥️ 提供 Windows、macOS、Linux 等多平台安装包

---

### [Node.js — Node.js 26.0.0（当前版本）](https://nodejs.org/en/blog/release/v26.0.0)

**原文标题**: [Node.js — Node.js 26.0.0 (Current)](https://nodejs.org/en/blog/release/v26.0.0)

Node.js 26.0.0 正式发布，带来多项重要更新，包括默认启用 Temporal API、V8 引擎升级至 14.6、Undici 更新至 8.0，以及多项弃用和移除操作。该版本将于十月进入长期支持（LTS）阶段。

- 🎉 **Temporal API 默认启用**：现代日期/时间 API，提供更强大、功能更丰富的替代方案，取代传统的 `Date` 对象。
- ⚙️ **V8 引擎升级至 14.6**：带来 `Map.prototype.getOrInsert()` 和 `Iterator.concat()` 等新功能。
- 🌐 **Undici 更新至 8.0.2**：HTTP 客户端实现获得新功能和改进。
- 🗑️ **多项弃用和移除**：包括 `crypto`、`http`、`stream`、`module` 等模块的旧 API 被移除或弃用，例如 `http.Server.prototype.writeHeader()` 和 `_stream_*` 模块。
- 🔧 **构建与依赖更新**：GCC 要求提升至 13.2，Python 3.9 支持被移除，V8 和 OpenSSL 等依赖项获得多项补丁。
- 🛠️ **其他重要变更**：`assert` 支持 printf 风格消息，`crypto` 增加原始密钥格式支持，`util` 改进代理对象检查等。

---

### [Node.js — Node.js 26.1.0（当前版本）](https://nodejs.org/en/blog/release/v26.1.0)

**原文标题**: [Node.js — Node.js 26.1.0 (Current)](https://nodejs.org/en/blog/release/v26.1.0)

Node.js 26.1.0 版本发布，引入了实验性 FFI 模块，并带来了多项功能增强和错误修复。

- 🧪 **实验性 `node:ffi` 模块**：新增用于加载动态库和调用原生符号的实验性 API，需通过 `--experimental-ffi` 标志启用，但使用存在安全风险。
- 📦 **`buffer` 新增 `end` 参数**：为 `indexOf`/`lastIndexOf` 等方法添加 `end` 参数，提升灵活性。
- 🔐 **`crypto` 功能增强**：支持 `crypto.diffieHellman()` 接受密钥数据，并新增 `randomUUIDv7()` 方法。
- 🐞 **调试器改进**：为 `node inspect` 添加无编辑运行时表达式探测功能。
- 📁 **`fs` 新增选项**：`fs.stat()` 支持 `signal` 选项，`statfs` 暴露 `frsize` 字段。
- 🌐 **`http` 增强**：强化 `ClientRequest` 选项合并，并为 `IncomingMessage` 添加 `req.signal` 属性。
- ⚙️ **`process` 行为变更**：`execve(2)` 失败时抛出错误而非中止进程。
- 🔄 **`stream` 改进**：`duplexPair` 支持传播销毁状态，修复嵌套 compose 错误传播。
- 🧪 **`test_runner` 新功能**：支持 mock 超时 API、`AbortSignal.timeout` 模拟、测试顺序随机化。
- 🎨 **`util` 颜色支持**：允许使用十六进制颜色代码对文本进行着色。
- 🛠️ **其他更新**：更新依赖（如 npm 11.13.0、OpenSSL 3.5.6），修复多项错误，并优化构建工具。

---

### [Node.js 和 V8 如何协同工作——工作流程、挑战与技巧 | Joyee Cheung 的博客](https://joyeecheung.github.io/blog/2026/05/18/how-nodejs-and-v8-keep-each-other-working/)

**原文标题**: [How Node.js and V8 keep each other working - workflows, challenges and tips | Joyee Cheung's Blog](https://joyeecheung.github.io/blog/2026/05/18/how-nodejs-and-v8-keep-each-other-working/)

### 概述总结
本文详细介绍了 Node.js 与 V8 引擎的集成工作流程、挑战及实用技巧，涵盖仓库映射、V8 更新维护、构建系统差异、测试方法、跨项目补丁处理等内容。

- 🗺️ **仓库结构**：涉及 `nodejs/node`（主分支和 `canary-base`）、`nodejs/node-v8`（每日测试 V8 最新版本）、`v8/v8`（V8 主仓库）、`v8/node`（V8 的 Node.js 集成测试分支）和 `v8/node-ci`（管理 CI 脚本）。
- 🔄 **V8 更新流程**：Node.js 在 `deps/v8` 中维护 V8 分支，每月通过大型 PR 更新至新稳定版；`canary-base` 分支每日测试 V8 最新版本，提前发现兼容性问题。
- ⚙️ **构建系统差异**：V8 使用 GN，Node.js 使用 GYP（遗留系统），需手动转换配置；Node.js 支持更多平台和工具链（如 GCC、ClangCL），导致额外维护工作。
- 🧪 **测试方法**：Node.js 通过 Jenkins CI 运行 V8 子集测试（`make test-v8`）；V8 的集成 CI 使用 GN 构建测试 Node.js 分支，确保 CL 兼容性。
- 🔧 **跨项目补丁技巧**：测试 V8 补丁时建议用 GYP 构建（性能更真实），使用 `git-node-v8` 工具或手动补丁；浮动的 V8 补丁可直接提交 PR；V8 集成 CI 的修复需在 `v8/node` 分支上操作。
- 🚨 **挑战与压力**：V8 版本锁定导致 LTS 发布延迟（如 2025/2026 年 4 月版本推迟至 5 月）；ABI 兼容性要求限制了 V8 升级，促使讨论解耦 ABI 版本。
- 💡 **实用建议**：处理冲突时使用 `wiggle` 工具；测试 V8 补丁需注意内存管理变化；更新 V8 集成 CI 需提交 PR 至 `v8/node` 和 `v8/node-ci`。

---

### [每个 AI 代理所需的四层生产堆栈](https://orkes.io/webinars/the-4-layer-production-stack-every-ai-agent-needs?utm_campaign=Node%20weekly&utm_source=Newsletter&utm_medium=referral)

**原文标题**: [The 4-Layer Production Stack Every AI Agent Needs](https://orkes.io/webinars/the-4-layer-production-stack-every-ai-agent-needs?utm_campaign=Node%20weekly&utm_source=Newsletter&utm_medium=referral)

Orkes 宣布完成 6000 万美元融资，开发者正越来越多地使用其平台在生产环境中自信地部署 AI。

- 💰 Orkes 成功融资 6000 万美元，表明市场对其 AI 部署平台需求强劲。
- 🚀 平台帮助开发者提升敏捷性、降低成本，并构建高可靠、高安全的应用。
- 🏢 客户如 Foxtel 正在将更多工作流从其他平台迁移至 Orkes。
- 🧩 Orkes 提供微服务、实时 API、事件驱动、人工及流程编排等多种能力。
- 🤖 推出 Agentic Workflows 功能，支持将工作流转化为可控的智能代理体验。
- 🛠 提出 AI 代理生产所需的四层技术栈：持久性、协调、安全控制与可观测性。
- 🎓 提供 Orkes Academy 等学习资源，帮助用户掌握工作流编排与 Agentic AI。
- 📅 将于 4 月 30 日举办网络研讨会，展示生产级 AI 代理的部署蓝图。

---

### [npm 泄露事件后强化 TanStack | TanStack 博客](https://tanstack.com/blog/incident-followup)

**原文标题**: [Hardening TanStack After the npm Compromise | TanStack Blog](https://tanstack.com/blog/incident-followup)

TanStack 在 npm 攻击事件后已完成安全强化，所有包现已安全可用。

- 🛡️ 所有 TanStack 包（包括 Router 和 Start）当前版本均安全可安装，已发布全面安全清查结果。
- 🔍 攻击源于恶意 PR 通过 `pull_request_target` 触发 CI 缓存投毒，窃取发布令牌，影响 42 个包（2 个版本），已在一小时内弃用。
- ✅ 已采取多项措施：禁用 pnpm 缓存、移除 GitHub Actions 缓存、固定操作至提交 SHA、强制非 SMS 双因素认证、移除 `pull_request_target` 使用、升级至 pnpm 11。
- 🔧 正在推进：添加 zizmor 静态分析器、对 `.github` 文件夹设置 CODEOWNERS、替换缓存为更保守的 `actions/cache/restore`。
- 💬 考虑限制外部贡献者直接提 PR，转向通过 issue 或邀请制贡献，但仍在讨论中，以平衡开放性与安全性。
- 📚 经验教训：CI 安全需主动审查，不能仅依赖工具安全特性，平台应改进缓存作用域和模式可发现性。

---

### [事后分析：TanStack npm 供应链安全事件 | TanStack 博客](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

**原文标题**: [Postmortem: TanStack npm supply-chain compromise | TanStack Blog](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

2026 年 5 月 11 日，TanStack 的 npm 包遭受供应链攻击，攻击者利用 GitHub Actions 的漏洞链，在 42 个包中发布了 84 个恶意版本。攻击在约 20 分钟内被外部研究人员发现，所有受影响版本已在约 1 小时 43 分钟内被弃用，npm 在约 4 小时 35 分钟内移除了所有恶意包。目前所有包已安全，只有 Router/Start 仓库受影响。

- 🔍 **攻击手法**：攻击者结合了`pull_request_target`“Pwn 请求”模式、GitHub Actions 缓存投毒和 OIDC 令牌内存提取三个漏洞，形成攻击链
- ⏱️ **时间线**：恶意包在 19:20-19:26 UTC 发布，19:46 被外部研究人员发现，20:19 开始弃用，23:55 完成 npm 端移除
- 🎯 **影响范围**：42 个@tanstack/*包受影响，每个包 2 个恶意版本；Query、Table、Form 等主要库未受影响
- 🦠 **恶意行为**：恶意脚本在 npm install 时执行，窃取 AWS、GCP、Kubernetes、Vault 等凭证，并通过 Session/Oxen 加密网络外泄，还能自我传播
- 🛡️ **检测与响应**：外部研究人员 StepSecurity 的 ashishkurmi 发现并报告，维护团队迅速协调，在 1 小时 43 分钟内弃用了全部 84 个恶意版本
- 🔧 **根因**：`bundle-size.yml`中的`pull_request_target`允许 fork 代码在基础仓库缓存中运行，缓存被投毒后影响发布工作流，OIDC 令牌从内存中被提取用于直接发布恶意包
- 📋 **IOC 指纹**：恶意包包含`@tanstack/setup`的可选依赖、`router_init.js`文件、特定缓存键和 exfiltration 网络域名
- 💡 **教训**：需要内部监控、审计`pull_request_target`工作流、固定第三方 action 版本、改进 npm 发布安全机制

---

### [通过从 Webpack 迁移到 Rspack 优化构建时间](https://engineeringblog.yelp.com/2026/05/optimizing-our-build-times-by-migrating-from-webpack-to-rspack.html)

**原文标题**: [Optimizing Our Build Times by Migrating from Webpack to Rspack](https://engineeringblog.yelp.com/2026/05/optimizing-our-build-times-by-migrating-from-webpack-to-rspack.html)

Yelp 团队通过从 Webpack 迁移到 Rspack，实现了构建时间约 50% 的缩减，并分享了迁移过程、优化策略及未来展望。

- 📉 **显著性能提升**：迁移后集成构建时间平均减少约 52%，全服务端渲染构建速度提升约 25%。
- 🔄 **渐进式迁移策略**：采用“适配器模式”保留原有 Webpack 配置，分阶段让开发者选择使用 Rspack，降低风险并便于验证。
- 🚀 **关键优化措施**：通过将星号重导出改为具名重导出、修复非真正重导出模式，以及启用 Rspack 的可移植持久缓存，进一步缩短构建时间（如热缓存下减少高达 80%）。
- 🛠️ **Storybook 集成挑战**：使用 storybook-react-rsbuild 时需通过 `tools.bundlerChain` 清除默认规则，避免插件冲突和输出异常。
- 🔮 **未来改进方向**：计划引入 Rust 驱动的 SWC 转译器（替代 Babel）和内置的 swc-loader，以进一步提升性能。

---

### [在 Postgres 中无需触发器构建自动化的上下文临床试验审计日志 | Harbor](https://runharbor.com/blog/2026-05-18-building-automatic-contextual-clinical-trial-audit-logging-in-postgres-without-triggers)

**原文标题**: [Building Automatic, Contextual Clinical Trial Audit Logging in Postgres Without Triggers | Harbor](https://runharbor.com/blog/2026-05-18-building-automatic-contextual-clinical-trial-audit-logging-in-postgres-without-triggers)

### 概述总结
本文介绍了如何在 Postgres 中构建自动化的、带有业务上下文的临床试验审计日志系统，无需使用触发器，而是通过 TypeScript 和 ORM 代理实现合规性。

- 🏥 **背景与需求**：临床试验软件需符合 21 CFR Part 11 要求，每次数据变更都必须生成包含操作人、时间、前后值及原因的审计日志，遗漏即违规。
- ❌ **避免手动审计**：通过 ESLint 规则强制开发人员手动添加审计日志不可行，因为无法覆盖所有数据变更路径，且易因人为疏忽导致合规失败。
- 🔍 **探索方案**：pgAudit 仅记录 SQL 语句，缺乏应用上下文（如用户、权限、原因）；数据库触发器需 PL/pgSQL，难以传递应用上下文且维护复杂。
- 🛠 **ORM 代理方案**：使用 TypeScript 的`Proxy`对象包装 Drizzle ORM，隐藏直接的数据变更方法，强制通过`.withAuditLogCtx()`提供审计上下文后才能执行写入操作。
- 📋 **审计表设计**：通过自定义`pgAuditedTable`创建基础表及对应的审计日志表，包含标准列（如行 ID、操作类型、前后 JSON、用户 ID、数字签名等），确保通用性。
- 🔒 **实现细节**：审计日志与数据变更在同一事务中完成，使用`SELECT FOR UPDATE`确保一致性，并对审计负载进行加密签名以防篡改。
- ⚖️ **权衡与未来**：当前方案牺牲部分性能（额外数据库往返），但降低了开发复杂度；未来可能迁移部分逻辑到数据库触发器以优化性能，但需更成熟的团队和工具支持。
- ✅ **结论**：将审计日志作为平台基础设施，通过类型系统强制合规，使产品工程师无需关注底层细节，确保合规性从第一天起就内建在系统中。

---

### [Node.js — 从 Axios 到 WHATWG Fetch](https://nodejs.org/en/blog/migrations/axios-to-fetch)

**原文标题**: [Node.js — Axios to WHATWG Fetch](https://nodejs.org/en/blog/migrations/axios-to-fetch)

本指南介绍如何将 Axios 迁移至 WHATWG Fetch API，利用 Node.js 原生支持的 Fetch 提升性能、安全性和标准合规性。

- 🚀 **原生支持**：Fetch 内置于 Node.js，无需外部库，降低维护成本。
- ⚡ **性能优化**：Fetch 针对现代 JavaScript 运行时优化，通常比 Axios 更高效。
- 🌐 **标准合规**：严格遵循 Web 标准，便于编写跨平台代码（Node.js 和浏览器）。
- 🔒 **安全增强**：移除 Axios 可消除第三方依赖的潜在漏洞。
- 📅 **版本要求**：Node.js v18.0.0+（实验性）或 v21.0.0+（稳定），否则需升级主版本并更新 `package.json` 的 `engines` 字段。
- 🔄 **支持转换**：涵盖 `axios.get`、`post`、`put`、`delete`、`patch`、`request` 等方法，并自动处理 JSON 和表单数据。
- ❌ **未支持功能**：拦截器、取消令牌、`axios.create()` 实例配置等高级特性暂不转换。
- 👏 **致谢**：感谢 Axios 维护者对该包的长期支持与贡献。

---

### [用户态迁移 | Node.js 学习](https://nodejs.org/learn/getting-started/userland-migrations)

**原文标题**: [Userland Migrations | Node.js Learn](https://nodejs.org/learn/getting-started/userland-migrations)

Node.js 用户空间迁移工具帮助开发者平滑升级代码库，支持新功能并处理破坏性变更。

- 🚀 **核心目标**：协助开发者迁移至最新 Node.js 版本，简化弃用处理、新功能适配和破坏性变更应对
- 📦 **官方迁移工具**：通过 Codemod 平台发布，由 Node.js 成员审核/编写，使用 `npx codemod <名称>` 命令运行
- ⚙️ **使用规范**：建议在独立分支运行迁移、审查变更、测试代码、格式化/检查代码
- 🔍 **Codemod 注册表**：提供可用迁移工具列表，支持用户点赞反馈以优化工具价值
- 💬 **反馈渠道**：通过 Node.js 用户空间迁移仓库发起讨论
- 📊 **进度追踪**：GitHub 项目面板跟踪迁移类型、Node.js 版本、状态（待办/进行中/完成/未计划）
- 📚 **迁移指南**：主版本迁移指南仅包含生命周期终止的弃用和破坏性变更

---

### [nodejs/axios-to-whatwg-fetch - Codemod 注册表](https://app.codemod.com/registry/@nodejs/axios-to-whatwg-fetch)

**原文标题**: [nodejs/axios-to-whatwg-fetch - Codemod Registry](https://app.codemod.com/registry/@nodejs/axios-to-whatwg-fetch)

概述摘要  
- 🔍 探索社区主导的代码迁移工具，用于迁移、优化和转换代码库  
- 📦 搜索包功能，支持按范围、标签、作者和类型筛选（如 "scope:acme tag:migration by:codemod react"）  
- ⌨️ 使用 "/" 键快速搜索  
- 🤝 鼓励用户贡献，构建自己的代码转换工具并与社区分享  
- 📤 提供发布代码转换工具的入口  
- 👥 邀请加入社区

---

### [获取失败](https://nodeweekly.com/link/185467/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/185467/web)

无法总结：获取内容失败，状态码 429。

---

### [发布说明 1.0 | TypeORM](https://typeorm.io/docs/releases/1.0/release-notes/)

**原文标题**: [Release Notes 1.0 | TypeORM](https://typeorm.io/docs/releases/1.0/release-notes/)

TypeORM 1.0 是一次重大版本发布，移除了长期废弃的 API，更新了平台要求，并修复了大量错误和引入了新功能。

- 🚀 **平台要求升级**：最低 Node.js 版本提升至 20+，目标 JavaScript 版本升级至 ES2023，并移除了 `Buffer` 和 `glob` 等旧依赖。
- 🔌 **驱动变更**：MySQL 仅支持 `mysql2`，SQLite 默认使用 `better-sqlite3`，MongoDB 驱动升级至 v7+，并移除了多个过时的驱动选项。
- 🗑️ **移除的 API**：删除了 `Connection`、`ConnectionManager`、`findByIds`、`@RelationCount` 等大量旧 API，建议使用 `DataSource`、`findBy`、`@VirtualColumn` 等新方案。
- ⚠️ **行为变更**：非空关联默认使用 `INNER JOIN`，无效的 `where` 值默认抛出错误，`ConnectionOptionsReader` 路径解析改为基于 `process.cwd()`。
- ✨ **新功能**：新增 `INSERT INTO ... SELECT FROM ...`、`returning` 选项、`ifExists` 参数、`DataSource` 级默认隔离级别，以及 PostgreSQL 的 `ADD VALUE` 枚举变更支持。
- 🐛 **错误修复**：修复了查询生成中的别名转义、关联加载中的重复 JOIN、持久化中的值转换器应用、以及软删除跳过已删除行等问题。
- 🔒 **安全修复**：通过参数化查询和转义标识符防止 SQL 注入，并验证 `orderBy` 和 `limit` 条件。
- ⚡ **性能改进**：PostgreSQL/CockroachDB 的 `clearDatabase()` 现在批量执行 DROP 语句，减少测试设置中的往返次数。

---

### [肉桂](https://kristiandupont.github.io/kanel/)

**原文标题**: [Kanel](https://kristiandupont.github.io/kanel/)

Kanel 是一个以 PostgreSQL 为数据源的代码生成框架，能将数据库模式转换为 TypeScript 类型、文档等多种格式。

- 🗄️ **数据库即真理源**：通过检查实时 PostgreSQL 数据库生成代码，保持数据库作为唯一事实来源
- 🎯 **类型安全**：自动生成包含品牌 ID、可空性和关系的精确 TypeScript 类型
- 🔌 **可插拔生成器**：支持 TypeScript、Markdown 和自定义生成器，可扩展至 Python、Rust 等语言
- ⚙️ **灵活集成**：通过钩子与 Kysely、Zod、Knex 等工具无缝协作
- 🚀 **快速上手**：支持 npx 一键运行或 npm 安装，生成代码可纳入 Git 管理
- 📝 **典型用例**：生成 TypeScript 类型 + Kysely 接口、Zod 验证模式，或仅生成 Markdown 文档
- 🏷️ **标识符类型**：使用品牌类型（如 CityId）确保类型安全，避免 ID 混淆
- 📦 **完整输出**：自动生成表接口、初始化器和修改器，以及对应的 Zod 模式

---

### [GitHub - kristiandupont/kanel: 从 Postgres 生成 TypeScript 类型](https://github.com/kristiandupont/kanel)

**原文标题**: [GitHub - kristiandupont/kanel: Generate Typescript types from Postgres · GitHub](https://github.com/kristiandupont/kanel)

Kanel 是一个从 PostgreSQL 数据库生成 TypeScript 类型的开源工具，适合不喜欢 ORM 但需要类型检查和智能提示的开发者。

- 🗄️ 从实时 PostgreSQL 数据库自动生成 TypeScript 类型
- 🚫 专为不喜欢 ORM 但需要类型安全的开发者设计
- 📘 提供详细文档和示例（基于 postgresqltutorial 的示例数据库）
- ⚙️ 通过 `kanel.config.js` 配置文件运行，支持命令行 `npx kanel` 或编程方式调用
- 🌟 拥有 1.1k 星标、79 个分支，社区活跃
- 📦 已发布 63 个版本（最新 v3.5.1，2023 年 8 月）
- 🛠️ 主要使用 TypeScript（98.4%）开发，遵循 MIT 许可证

---

### [ESLint v10.4.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/05/eslint-v10.4.0-released/)

**原文标题**: [ESLint v10.4.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/05/eslint-v10.4.0-released/)

ESLint v10.4.0 发布，这是一个小版本升级，新增了功能并修复了多个错误。

- 🆕 新增 `includeIgnoreFile()` 辅助函数，允许在配置文件中包含 `.gitignore` 或其他 gitignore 风格文件中的忽略模式，支持多个文件和相对路径解析。
- ✨ 功能更新：检查序列表达式中的 `for-direction` 规则，并将 `includeIgnoreFile()` 添加到 `eslint/config` 入口点。
- 🐛 错误修复：包括转义调试输出中的代码路径 DOT 标签、更新依赖项 `@eslint/config-helpers` 到 ^0.6.0，以及处理非数组的废弃规则替换。
- 📚 文档改进：添加对 `@eslint-react/eslint-plugin` 的提及，并调整关于 CJS-vs-ESM 配置的措辞。
- 🛠️ 杂项：升级 knip 到 v6、更新 CI 配置、添加单元测试、重构代码以移除废弃的 `meta.language` 并迁移 `meta.dialects`。

---

### [GitHub - pnpm/pnpm: 快速、节省磁盘空间的包管理器 · GitHub](https://github.com/pnpm/pnpm)

**原文标题**: [GitHub - pnpm/pnpm: Fast, disk space efficient package manager · GitHub](https://github.com/pnpm/pnpm)

pnpm 是一个快速、节省磁盘空间的包管理器，性能比 npm 和 Yarn 快 2 倍，采用内容可寻址存储来链接 node_modules 文件，支持单仓库、严格依赖管理和跨平台运行。

- 🚀 **极速性能**：比 npm 和 Yarn 快 2 倍，有基准测试验证。
- 💾 **节省空间**：文件存储在内容可寻址存储中，通过硬链接或 reflinks 共享，避免重复占用磁盘。
- 🏗️ **单仓库支持**：专为 monorepos 设计，管理多个项目高效。
- 🔒 **严格依赖**：包只能访问 package.json 中指定的依赖，增强安全性。
- 📋 **确定性锁定**：使用 pnpm-lock.yaml 确保安装结果一致。
- 🔧 **Node.js 版本管理**：可作为 Node.js 版本管理器使用（见 pnpm runtime）。
- 🌍 **跨平台兼容**：支持 Windows、Linux 和 macOS。
- 🏆 **实战验证**：自 2016 年起被各类团队使用，包括微软 Rush 团队。
- 💰 **赞助支持**：通过 Open Collective 或加密货币捐赠支持项目。
- 📚 **开源许可**：采用 MIT 许可证，代码在 GitHub 上公开。

---

### [GitHub - cyco130/vavite：使用Vite开发服务端应用 · GitHub](https://github.com/cyco130/vavite)

**原文标题**: [GitHub - cyco130/vavite: Develop server-side applications with Vite · GitHub](https://github.com/cyco130/vavite)

vavite 是一个基于 Vite 的插件，用于开发和构建服务器端应用，利用 Vite 作为转译器/打包器，简化 SSR 工作流并支持纯后端开发。

- 🚀 **核心功能**：vavite 允许使用 Vite 转译所有服务器端代码，无需额外工具（如 ts-node 或 nodemon），支持 TypeScript 和 JSX。
- 📦 **两种入口类型**：支持“runnable-handler”（默认，导出 HTTP 请求处理器）和“runnable-server”（启动独立服务器，开发时通过代理转发请求）。
- ⚙️ **配置灵活**：通过 `entries` 选项指定多个入口，支持 `order`（pre/post）和 `final` 属性，控制请求处理链顺序。
- 🔧 **SSR 与纯后端**：支持 SSR 设置（后置处理器，利用 Vite 资产管道）和纯服务器设置（前置处理器，绕过客户端功能）。
- 🔄 **热模块替换（HMR）**：服务器端支持 HMR，通过 `import.meta.hot.dispose` 和 `prune` 清理资源（如数据库连接），生产环境自动移除 HMR 代码。
- 🛠️ **环境信息**：提供 `import.meta.env.COMMAND`（运行命令）和 `import.meta.env.ENVIRONMENT`（环境名称），以及 `vavite:vite-dev-server` 访问 Vite 开发服务器。
- 📚 **丰富示例**：包括 Express、Fastify、Koa、Hapi、Nest.js 等框架的集成示例，以及 WebSocket 和资源清理演示。
- ⬆️ **迁移注意**：v7 放弃 Node 20 以下支持；v6 完全重写，移除 `@vavite` 包和 CLI，改用 `vite build --app`，配置选项（如 `handlerEntry`）替换为 `entries`。
- 🌟 **社区活跃**：540 星标、15 个分支、MIT 许可证，支持贡献，主要语言为 TypeScript（94.6%）。

---

### [阿多尼斯 MCP](https://adonis-mcp.jrmc.dev/)

**原文标题**: [Adonis MCP](https://adonis-mcp.jrmc.dev/)

该文本介绍了如何创建强大的 MCP 工具，包括类型安全的模式和优雅的处理程序，以实现 AI 与应用程序逻辑的交互。

- 🔧 创建类型安全的模式，确保工具输入输出的正确性
- 🎯 使用优雅的处理程序，简化 AI 与应用程序逻辑的集成
- 🤖 实现 AI 与应用程序的高效交互，提升自动化能力
- 📦 提供工具构建框架，支持扩展和定制化开发

---

### [AdonisJS - 功能齐全的 TypeScript 框架](https://adonisjs.com/)

**原文标题**: [
      AdonisJS - The batteries-included TypeScript framework
    ](https://adonisjs.com/)

AdonisJS 是一个功能完备的 TypeScript Node.js 框架，提供从认证到测试的全栈开发体验，深受大型企业及开发者社区信赖。

- 🗺️ 路线图已上线，展示框架未来发展方向
- 🔋 电池全包：内置认证、ORM、验证、邮件、队列、缓存、测试等核心功能
- 🏢 被多家知名企业采用：Ledger、雷诺、日产、Paytm、Evian 等
- 📝 路由集中管理，控制器按资源分组，代码清晰可维护
- ⚡ VineJS 验证器速度是 Zod 的两倍，支持异步验证和深度集成
- 🗄️ 基于 Knex 的 Active Record ORM，支持关系定义、迁移、种子数据
- 🔐 同时支持会话认证和 API Token 认证，密码自动哈希
- 📁 统一文件上传 API，支持 S3、R2、GCS 和本地存储
- 📧 邮件支持 SMTP、SES、Mailgun 等多种驱动，可队列发送
- 🛡️ 内置限速器，支持 Redis 和数据库存储，原子计数精确
- 🧪 使用 Playwright 编写浏览器测试，支持数据库事务和认证辅助
- 🎨 灵活的前端选择：可搭配 React、Vue、Edge 模板或纯 API
- 🛠️ 丰富的开发者工具：Vite 集成、HMR、CLI、漂亮错误页、CSRF、CORS
- 📦 官方包覆盖缓存、限速、健康检查等常见需求，无需额外搜索
- 🎯 提供 E2E 类型安全、类型安全环境变量和事件发射器
- 📚 超过 10 年发展历史，23K GitHub 星标，2700 万 npm 下载量
- 🤝 活跃社区支持：Discord、视频教程、预构建组件和详细文档

---

### [GitHub - batosai/adonis-mcp · GitHub](https://github.com/batosai/adonis-mcp)

**原文标题**: [GitHub - batosai/adonis-mcp · GitHub](https://github.com/batosai/adonis-mcp)

@jrmc/adonis-mcp 是一个为 AdonisJS 应用提供 AI 交互能力的 MCP 包，支持工具、资源和提示的定义与使用。

- 🛠️ **工具 (Tools)**：提供类型安全的处理器，允许 AI 模型执行数据库查询、发送邮件等操作。
- 📂 **资源 (Resources)**：通过 URI 模板暴露应用数据，支持文本和二进制内容。
- 💡 **提示 (Prompts)**：提供可重用、带参数验证的提示模板，指导 AI 交互。
- 🔌 **多传输支持**：内置 HTTP、stdio 和测试用 Fake 传输。
- 🏷️ **注解 (Annotations)**：通过 `@isReadOnly`、`@isDestructive` 等装饰器为工具和资源添加元数据。
- 🔐 **认证与授权**：与 AdonisJS Auth 和 Bouncer 深度集成。
- 🔍 **调试工具**：内置 MCP Inspector，方便开发时测试。
- 🧪 **测试支持**：提供 Fake 传输，便于单元测试。
- 📦 **安装简单**：通过 `node ace add @jrmc/adonis-mcp` 快速安装配置。
- 📖 **完整文档**：提供详细的安装、配置和使用指南。

---

### [托梁 | 托梁](https://joist-orm.io/)

**原文标题**: [Joist | Joist](https://joist-orm.io/)

Joist 是一个专为单体应用设计的 TypeScript ORM，提供高性能和类型安全的数据库操作。

- 🚀 **最佳性能**：所有查询针对 Postgres 优化，批量写入和读取，避免性能瓶颈。
- 🛡️ **N+1 安全**：通过批量加载和预加载，彻底防止 N+1 查询问题，即使使用 `Promise.all` 循环也安全。
- ⚡ **后端响应式**：支持响应式字段和验证规则，将声明式业务逻辑带到后端。
- 🔒 **类型安全领域模型**：利用 TypeScript 在编译时确保类型安全，例如在类型系统中跟踪关联加载状态。
- 🧪 **丰富测试支持**：提供内置测试工厂和快速数据库重置，使测试简洁且适应领域模型变化。

---

### [MikroORM 7.1：已加载 | MikroORM](https://mikro-orm.io/blog/mikro-orm-7-1-released)

**原文标题**: [MikroORM 7.1: Loaded | MikroORM](https://mikro-orm.io/blog/mikro-orm-7-1-released)

MikroORM v7.1 版本发布，包含多项新功能和改进，主要聚焦于类型安全、查询优化和数据库特性支持。

- 🎯 **新关系类型 LazyRef<T>** — 引入类型安全的懒加载关系标记，无需运行时包装，TypeScript 编译时强制检查是否已加载，配合 Loadable mixin 和 unref() 工具提供完整类型安全方案

- 📊 **集合加载的父级限制** — 支持为每个父级限制填充集合数量（如每个用户最近 4 篇文章），SQL 使用 ROW_NUMBER() 子查询，MongoDB 使用聚合管道

- 🔍 **类型安全索引提示** — 新增 using 选项验证 where/orderBy 与命名索引的匹配，自动生成驱动特定的 SQL 提示（USE INDEX、WITH(INDEX) 等）

- 🗂️ **部分索引支持** — @Index/@Unique 支持 where 谓词，跨驱动兼容（PostgreSQL 原生部分索引、MySQL 函数索引、MongoDB partialFilterExpression）

- 🔌 **DI 项目的类型化 Kysely** — 新增 discovery:export CLI 命令生成类型桶文件，解决 NestJS 等框架中实体类型丢失问题，支持完全类型推断的 Kysely 实例

- 🔄 **Kysely 事务绑定** — getKysely() 自动绑定到活动事务，查询在 em.transactional() 内执行，fork 的 EM 可选择性退出

- 🛑 **查询取消支持** — 所有读写入口支持 AbortSignal，提供 ignore query/cancel query/kill session 三种策略，覆盖 PostgreSQL、MySQL、MSSQL、MongoDB

- 🐘 **PGlite 驱动** — 新增 @mikro-orm/pglite，在 WASM 中运行 PostgreSQL，支持内存/IndexedDB/文件系统存储，适用于测试、浏览器和本地优先应用

- 📈 **分组计数 em.countBy()** — 新增按属性分组计数方法，支持复合键，SQL 生成 GROUP BY 查询，MongoDB 使用 $group 聚合

- ⚡ **Collection.loadCount() 数据加载器** — 支持批量加载计数，同一 tick 内的多个 count 调用合并为单个查询

- 🔔 **数据库触发器管理** — 通过 @Trigger() 装饰器或 defineEntity 定义触发器，支持创建、差异比较和删除，跨 PostgreSQL、MySQL、SQLite、MSSQL

- 🔗 **联合目标多态 M:N** — 支持单个所有者持有 Collection<A | B>，每个关联行通过鉴别器选择目标表

- 📦 **PostgreSQL 表分区** — 支持哈希、列表和范围分区，schema 生成器自动创建父表和子分区

- 📋 **服务端行克隆** — em.clone() 和 qb.insertFrom() 支持不经过 Node.js 的数据复制，自动处理 TPT 继承、嵌入属性和外键

- 🔒 **serialize() 字段白名单** — 新增 fields 选项支持允许列表模式，严格排除未列出的字段，返回类型完整推断

- 💾 **存储过程和函数（实验性）** — 通过 Routine 类声明和管理，支持参数类型推断、多结果集、OUT/INOUT 参数，跨 PostgreSQL、MySQL、MSSQL、Oracle

- 🌐 **迁移运行时 schema 上下文** — 支持将迁移重定向到目标 schema，适用于 PR 预览和多租户场景，跟踪表独立维护迁移历史

- 🛠️ **CLI 增强** — 新增 migration:rollup（合并迁移）、migration:log/unlog（标记迁移状态）、--schema 标志

- ✨ **其他改进** — 标量属性 array:true、initNullableProperties 配置、defineEntity 支持 extends、流式 chunkSize、列级 collation、枚举引用、ISO 日期字符串自动转换

---

### [Node.js 应用的自动缩放](https://judoscale.com/node?utm_source=node-weekly&utm_medium=referral&utm_campaign=try-judoscale&utm_content=doesnt-suck)

**原文标题**: [Autoscaling for Node.js apps](https://judoscale.com/node?utm_source=node-weekly&utm_medium=referral&utm_campaign=try-judoscale&utm_content=doesnt-suck)

### 概述总结
Judoscale 是一款专为 Node.js 应用设计的自动缩放工具，通过请求队列时间和作业队列延迟实现高效缩放，支持多种平台，已获大量用户好评。

- 🚀 **轻松自动缩放**：基于请求队列时间和作业队列延迟，自动缩放 Node.js Web 应用和任务队列。
- 📦 **多平台支持**：适用于 Amazon ECS、Heroku、Render、Fly.io 和 Railway。
- ⏱️ **队列时间为核心**：使用队列时间而非 CPU 或内存作为缩放指标，更准确反映服务器容量。
- 🔄 **作业队列缩放**：支持后台工作者的自动缩放，防止作业队列积压。
- ⚡ **最快缩放器**：每 10 秒运行一次缩放算法，快速响应容量问题。
- 💰 **降低托管成本**：通过精确缩放减少过度配置，节省成本。
- 🎛️ **可定制行为**：支持按多个实例缩放、调整频率，每个进程独立配置。
- 🏆 **用户好评**：被 900+ 工程团队信任，月处理超 250 万请求，自 2017 年稳定运营。
- 🛠️ **支持 Node 栈**：Web 缩放支持 Express 和 Fastify，Worker 缩放支持 Bull 和 BullMQ。
- 🌟 **免费试用**：设置不到 5 分钟，可立即开始免费使用。

---

### [API 密钥正式发布](https://clerk.com/changelog/2026-04-17-api-keys-ga?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=05-14-26&dub_id=TxaPfGQ7ygSYxpBw)

**原文标题**: [API Keys General Availability](https://clerk.com/changelog/2026-04-17-api-keys-ga?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=05-14-26&dub_id=TxaPfGQ7ygSYxpBw)

概述：API 密钥现已正式发布，并启用基于使用量的计费模式。

- 🗝️ API 密钥现已正式可用，属于机器认证套件的一部分，允许用户创建代表其应用 API 访问权限的凭证。
- 💰 计费已启动，每月提供免费配额：前 1,000 次密钥创建免费，之后每次创建收费$0.001；前 100,000 次密钥验证免费，之后每次验证收费$0.00001。
- 📚 提供入门指南，包括完整的 API 密钥启用与使用教程、后端 SDK 参考（涵盖创建、列出、验证和撤销密钥的完整 API），以及仪表盘启用选项。
- 👥 贡献者包括 Jeff Escalante、Robert Soriano、Brandon Romano 和 Bruno Lin。

---

### [由 Jarred-Sumner 用 Rust 重写 Bun · 拉取请求 #30412 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/30412)

**原文标题**: [Rewrite Bun in Rust by Jarred-Sumner · Pull Request #30412 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/30412)

Bun 项目已成功用 Rust 重写，合并了 6755 个提交，通过了所有现有测试，并修复了多个内存泄漏和测试不稳定问题。

- 🎯 二进制体积减少 3-8 MB，性能持平或更快
- 🛡️ 引入编译器辅助工具，有效捕获和预防内存错误
- 🧪 完全通过 Bun 现有测试套件，覆盖所有平台
- 🔧 架构和数据结构基本保持不变，仍使用少量第三方库
- 📦 可通过 `bun upgrade --canary` 试用
- ⚠️ 非稳定版仍需优化和清理工作
- 👍 获得 1588 个赞，👎 1509 个踩，社区反应两极分化

---

### [所有 Rust 代码库：该代码库甚至无法通过最基本的 miri 检查，在安全的 Rust 中允许未定义行为 · Issue #30719 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/issues/30719)

**原文标题**: [all of rust codebase: This codebase fails even the most basic miri checks, allows for UB in safe rust · Issue #30719 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/issues/30719)

该代码库存在严重的内存安全问题，整个 Rust 代码库连最基本的 miri 检查都无法通过，允许在安全 Rust 中出现未定义行为。

- 🚨 **未定义行为**：代码在`src/main.rs:97`处构造了悬垂引用，导致 Undefined Behavior
- 🔍 **具体错误**：`from_raw_parts`创建了指向已释放内存的`&[u8]`切片，违反了 Rust 内存安全规则
- 💡 **问题根源**：在`drop(test)`后仍尝试访问`init.slice()`，造成 use-after-free 漏洞
- ⚠️ **安全警告**：该问题发生在安全 Rust 代码中，表明类型系统未能正确防止内存错误
- 🤖 **开发建议**：不要依赖 AI 编写 Rust 代码，AI 不擅长 Rust 编程，建议聘请真正的 Rust 开发者

---

### [我们是否应该用 Rust 重写 Node.js？ - YouTube](https://www.youtube.com/watch?v=nrdDmR1inl4)

**原文标题**: [Should We Rewrite Node.js in Rust? - YouTube](https://www.youtube.com/watch?v=nrdDmR1inl4)

本頁面涵蓋 YouTube 平台的核心資訊與政策，包括版權、聯絡方式、創作者支援、廣告、隱私及安全等面向。

- 📰 新聞中心：提供 YouTube 官方新聞與更新
- ©️ 版權：說明版權相關規範與保護機制
- 📞 聯絡我們：提供使用者與 YouTube 聯繫的管道
- 🎨 創作者：為內容創作者提供資源與支援
- 📢 刊登廣告：介紹廣告刊登選項與合作方式
- 👨‍💻 開發人員：提供 API 與開發工具資訊
- 📜 條款：列出使用 YouTube 服務的條款與條件
- 🔒 私隱：說明個人資料的收集與使用政策
- 🛡️ 政策及安全：涵蓋社群規範與安全措施
- ⚙️ YouTube 的運作方式：解釋平台推薦與運作機制
- 🧪 測試新功能：介紹正在測試的新功能
- 📅 © 2026 Google LLC：版權歸屬與年份資訊

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

### 概述总结
Wasp 是一个面向 AI 时代的全栈框架，类似 Rails，结合 React、Node.js 和 Prisma，可快速开发应用并通过单条 CLI 命令部署。它开源，支持全栈认证、RPC 通信、简易部署、任务调度、邮件发送和全栈类型安全，通过简单配置文件生成完整应用源码。

- 🚀 **快速开发与部署**：使用 `npm i -g @wasp.sh/wasp-cli@latest` 安装，通过单一 CLI 命令即可构建和部署全栈应用，类似 Rails 框架。
- 🔐 **全栈认证**：支持 Google、GitHub 和邮箱登录，无需第三方供应商锁定，代码简洁。
- 🔗 **RPC 通信**：提供类型安全的 RPC 层，将数据模型和服务器逻辑直接暴露给客户端，简化前后端交互。
- 📦 **简易部署**：支持多平台部署，提供 CLI 辅助工具，部署过程简单。
- ⏰ **任务调度**：可定义、调度和运行服务器任务，支持持久化、重试和延迟执行。
- 📧 **邮件发送**：连接邮件提供商后即可发送邮件，集成方便。
- 🛡️ **全栈类型安全**：完全支持 TypeScript，自动生成跨栈类型，确保代码安全。
- 🧩 **更多功能**：包括自定义 API 路由、数据库种子、乐观更新、客户端自动缓存失效等。
- ⚙️ **工作方式**：通过 `.wasp` 配置文件描述应用高级细节，结合 JS/CSS 源文件，Wasp 编译器生成完整前端、后端和部署代码。
- 🎨 **简单配置语言**：声明式描述应用细节，减少样板代码，让开发者专注于核心逻辑。
- 💻 **技术栈**：基于 React、Node.js 和 Prisma，90% 代码仍使用熟悉技术，降低学习成本。
- 🏆 **社区案例**：展示如 Hireveld（招聘平台）、Grabbit（开发环境管理）、Amicus（法律团队工作流）等成功应用。
- 📬 **更新订阅**：提供订阅功能，让用户及时了解新功能和更新。
- ❓ **常见问题**：解答与 Next.js、Ruby on Rails 等框架的差异，以及学习难度和技术支持范围。

---

### [五年和五百万美元之后：发明一种新的 Web 开发编程语言是个错误 | Wasp](https://wasp.sh/blog/2026/05/13/new-language-for-web-dev-was-a-mistake)

**原文标题**: [5 Years and $5M Later: Inventing a New Programming Language for Web Development Was a Mistake | Wasp](https://wasp.sh/blog/2026/05/13/new-language-for-web-dev-was-a-mistake)

Wasp 团队在投入 5 年时间和 500 万美元后，决定放弃自创的编程语言，改用 TypeScript 来构建全栈 Web 框架。以下是文章的核心要点总结：

- 🚫 **自创语言是错误决策**：Wasp 团队最初为构建通用全栈框架而设计新语言，但实践证明这带来了更多问题而非价值。

- 💡 **核心价值不在语言**：用户真正看重的是 Wasp 能提供整个应用的高层规范（specification），让开发者和 AI 都能轻松理解全栈架构，而非语言本身。

- 🛠️ **IDE 支持成噩梦**：维护自定义语言的开发工具（如 VS Code 扩展）比预期困难得多，始终无法达到现代 JS 生态的体验标准。

- 😰 **语言定位引发误解**：“wasp-lang”名称让开发者误以为要取代 JavaScript，加上 Haskell 技术栈的宣传，导致用户产生“学习成本高”的错觉。

- 📈 **采用率增长但转化困难**：试用过的开发者很喜欢 Wasp，但“新语言”这个门槛让很多人连尝试都不愿意。

- 🔄 **转向 TypeScript SDK**：团队用 TypeScript 重写了配置层，保留所有底层功能，解决了工具链兼容性和用户心理障碍。

- 🎯 **保持核心优势**：Wasp 依然能在编译时理解整个应用结构，支持自动生成代码、优化和不同架构，只是换成了更熟悉的 TypeScript 语法。

- 🤖 **AI 时代更契合**：Wasp 的全栈结构化特性让 AI 生成代码更可靠，开发者反馈这是与 AI 协作效果最好的框架之一。

---

### [Destino：在终端中使用 Node.js FFI 运行《毁灭战士》](https://blog.platformatic.dev/destino-doom-terminal-nodejs-ffi)

**原文标题**: [Destino: Running Doom in Your Terminal with Node.js FFI](https://blog.platformatic.dev/destino-doom-terminal-nodejs-ffi)

概述总结  
- 🎮 Destino 是一个使用 Node.js FFI 在终端中运行《毁灭战士》的游戏项目，由 Node Collaborator Summit 上的玩笑演变而来。  
- 🛠️ 项目结合了 node:ffi、doomgeneric 和 OpenTUI，JavaScript 控制主循环，原生 Doom 引擎运行，OpenTUI 处理终端图形，SDL2 处理音频。  
- 🧩 FFI 允许 Node.js 直接调用原生库，无需原生插件或子进程，降低了复杂性，并展示了在运行时路径中的实用性。  
- 🔄 主循环简单高效：每 35 毫秒调用一次 tick()，检查帧就绪后渲染，保持 JS 与原生边界的单向流动。  
- 🖥️ 渲染使用 Doom 的 BGRA 帧缓冲区，通过 FFI 映射为 JavaScript Buffer，支持终端文本模式和 Kitty 图形协议。  
- ⌨️ 输入处理使用 Kitty 键盘协议获取按键事件，映射到 Doom 键码，配置文件 destino.json 可自定义键位。  
- 🎵 音频由 DoomGeneric 通过 SDL2 原生处理，JavaScript 仅负责协调，保持分工清晰。  
- 📦 支持打包为 Node.js 单可执行应用程序 (SEA)，包含 JS 代码、原生库、WAD 文件和音色库，启动时解压到临时目录。  
- 🚀 需要 Node.js 26.1.0 及以上版本，支持 macOS 和 Ubuntu Linux，自动处理依赖。  
- 💡 项目展示了 FFI 在企业场景中的潜力：可保留遗留 C 库，用 Node.js 封装，提升运行时、部署和可观测性。  
- 🔮 未来可扩展到 llama.cpp、GPU 库、本地 AI 推理等场景，强调 JS 负责应用逻辑，原生代码处理专业任务。

---

### [GitHub - ozkl/doomgeneric: 易于移植的毁灭战士 · GitHub](https://github.com/ozkl/doomgeneric)

**原文标题**: [GitHub - ozkl/doomgeneric: Easily portable doom · GitHub](https://github.com/ozkl/doomgeneric)

概述摘要  
doomgeneric 是一个旨在简化 Doom 游戏移植的开源项目，仅需实现少数函数即可完成移植，支持多种平台，并提供声音和音乐功能。

- 🎮 **简化移植**：只需实现 DG_Init、DG_DrawFrame、DG_SleepMs、DG_GetTicksMs 和 DG_GetKey 五个函数，即可将 Doom 移植到新平台。
- 📄 **WAD 文件需求**：运行需要 WAD 游戏数据文件，可免费获取共享版 doom1.wad。
- 🔄 **主循环结构**：调用 doomgeneric_Create() 初始化，然后在循环中不断调用 doomgeneric_Tick()。
- 🔊 **声音支持**：声音实现较复杂，可参考 SDL 端口，定义 FEATURE_SOUND 并分配 DG_sound_module 和 DG_music_module。
- 🌐 **多平台支持**：已移植到 Windows、X11、SDL 和 Emscripten，并提供对应 Makefile。
- 🕹️ **在线试玩**：Emscripten 版本支持声音和音乐，可直接在 https://ozkl.github.io/doomgeneric/ 体验。
- 📝 **开源许可**：项目采用 GPL-2.0 许可证，主要使用 C 语言编写。

---

### [GitHub - anomalyco/opentui: OpenTUI 是一个用于构建终端用户界面（TUI）的库](https://github.com/anomalyco/opentui)

**原文标题**: [GitHub - anomalyco/opentui: OpenTUI is a library for building terminal user interfaces (TUIs) · GitHub](https://github.com/anomalyco/opentui)

OpenTUI 是一個用 Zig 開發的原生終端 UI 核心，並提供 TypeScript 綁定，專注於正確性、穩定性和高效能。

- 🚀 **核心技術**：以 Zig 語言開發原生核心，透過 C ABI 支援多語言使用，並提供 TypeScript/JavaScript 綁定
- 📦 **多套件支援**：包含 @opentui/core、@opentui/three、@opentui/solid、@opentui/react 等套件，滿足不同框架需求
- ⚡ **快速入門**：支援 bun create tui 快速建立專案，並提供 npx skills 安裝 AI 助手技能
- 🖥️ **即時試用**：無需克隆倉庫即可透過 curl 或 GitHub Releases 試用範例
- 📚 **豐富文件**：提供網站文件、開發指南、快速入門和環境變數配置說明
- 🏆 **生產驗證**：已在 OpenCode 和 terminal.shop 等專案中實際應用
- 🌟 **社群活躍**：擁有 11.2k Stars、561 Forks，並有 80 個版本發布
- 🔧 **開發語言**：主要使用 TypeScript (71.6%) 和 Zig (23.4%)，並支援 MDX、Astro 等

---

