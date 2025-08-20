### [Node Weekly 第 590 期：2025 年 8 月 19 日](https://nodeweekly.com/issues/590)

**原文标题**: [Node Weekly Issue 590: August 19, 2025](https://nodeweekly.com/issues/590)

Node.js 通讯第 590 期内容摘要，涵盖版本更新、工具发布及行业动态。
- 🚀 Node.js v22.18.0 LTS 版本支持直接运行 TypeScript（通过类型剥离技术）
- 📊 Sidequest.js 推出可扩展的 Node.js 后台任务处理器，含 Web 仪表板和多后端支持
- 🔐 Node.js v24.6.0 新增系统信任证书环境变量和 zlib 字典支持
- 🌐 Cloudflare Workers 即将支持 Express 应用框架（目前仅限本地开发）
- 📦 npm 采用 OIDC 实现 CI/CD 工作流的可信发布功能
- 🛠️ 工具更新：zx v8.8 强化管道操作、Pyodide 支持 Node.js 运行 Python、QuickJS 沙盒 3.0
- 📈 多项目版本升级：Ghost 6.0 发布平台、Fastify 5.5 框架、Prisma 6.14 ORM 等
- 🔗 生态动态：TC39 委员会访谈、Rust 替代 Node.js 性能演示、jQuery 4.0 RC1 发布

---

### [Node.js](https://nodejs.org/en/blog/release/v22.18.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v22.18.0)

Node.js v22.18.0 LTS 版本发布，主要特性包括默认启用 TypeScript 类型剥离功能，无需额外配置即可直接运行.ts 文件，同时包含多项 ES 模块、文件系统、权限控制等核心模块的功能增强和优化。

- 🚀 默认启用 TypeScript 类型剥离功能，无需配置直接运行.ts 文件
- ⚠️ 该功能仍为实验性，可通过--no-experimental-strip-types 禁用
- 🔧 新增 import.meta.main 支持，增强 ES 模块功能
- 📁 文件系统模块优化异步迭代器的事件处理能力
- 🔐 权限模块支持在 spawn 时传播权限标志
- 🗃️ SQLite 模块新增 readBigInts 连接选项支持
- 🌐 URL 模块新增 fileURLToPathBuffer API
- 👀 监视模式新增--watch-kill-signal 终止信号配置
- 🧵 Worker 线程支持异步销毁接口
- 📦 包含 npm 10.9.3 版本更新及多项安全修复

---

### [Node 周刊第 589 期：2025 年 8 月 5 日](https://nodeweekly.com/issues/589)

**原文标题**: [Node Weekly Issue 589: August 5, 2025](https://nodeweekly.com/issues/589)

本期内容主要涵盖 Node.js 生态更新、工具发布及行业动态，包括性能优化、新版本特性及开发者资源。  
- 🚀 V8 团队将 JSON.stringify 性能提升超两倍，Node.js 应用将受益于更快的 API 响应与缓存处理  
- 🔧 Node.js v24.5.0 发布：支持 OpenSSL 3.5、实验性 WASM 模块取消标记、HTTP/HTTPS 模块新增代理功能  
- 🤖 TypeScript 5.9 推出：支持 import defer、新增--module node20 选项，编辑器类型信息展示优化  
- 📦 npm 现支持通过 OIDC 在 CI/CD 流程安全发布包，pnpm 10.14 可自动安装指定 JavaScript 运行时版本  
- ⚡ 多款工具更新：Express Slow Down 3.0 限流插件、Postgres 新驱动 pgline 提速、Redis 客户端性能优化  
- 🌐 行业动态：Deno 与 Oracle 商标争议进展、Vite 生态工具更新、Svelte 5 编译原理解析  
- 🏖️ 编辑部将于 8 月 5 日至 19 日休刊，期间仍接受投稿

---

### [Sidequest.js](https://sidequestjs.com/posts/intro-to-sidequest/)

**原文标题**: [Sidequest.js](https://sidequestjs.com/posts/intro-to-sidequest/)

Sidequest.js 是为 Node.js 设计的分布式后台作业系统，通过数据库协调多节点任务执行，解决传统调度器在分布式环境中的重复执行和主线程阻塞问题，提供无外部依赖的轻量级解决方案。

- 🚀 解决传统调度器在分布式环境中多实例重复执行任务的问题
- 🛡️ 通过工作线程隔离后台任务，确保主应用线程保持响应
- 🗄️ 利用现有数据库（PostgreSQL/MySQL/MongoDB）实现分布式协调，无需额外基础设施
- ⚡ 提供简洁的 API 设计，支持自动重试和指数退避机制
- 🌐 避免云服务厂商锁定，提供比 Airflow/RabbitMQ/SQS 更轻量的替代方案
- 🔧 支持本地开发和测试，无需模拟云服务环境

---

### [仪表盘 | Sidequest.js](https://docs.sidequestjs.com/dashboard)

**原文标题**: [Dashboard | Sidequest.js](https://docs.sidequestjs.com/dashboard)

Sidequest 仪表板是一个用于监控、管理和调试作业处理系统的综合 Web 界面，提供实时作业执行、队列性能和系统健康状态的洞察。

- 📊 实时监控功能，每 1-3 秒自动更新数据
- ⚙️ 作业管理支持运行、取消和重新运行作业
- 🚦 队列控制可暂停、激活和监控队列状态
- 📈 性能分析提供历史图表和统计数据
- 📱 响应式设计兼容桌面和移动设备
- 🔒 无外部依赖，完全在 Sidequest 实例内运行
- 🌐 默认访问地址为 http://localhost:8678
- ⚡ 支持自定义端口和基本身份验证配置
- 🛡️ 生产环境建议启用认证确保安全
- 📦 可独立安装@sidequest/dashboard 包使用
- 🔍 提供作业统计概览和详细作业信息查看
- 🎯 支持高级过滤和时间范围选择功能
- ⚠️ 包含故障排除指南和性能优化建议

---

### [GitHub - sidequestjs/sidequest: Sidequest 是一个面向 Node.js 应用的现代化、可扩展的后台任务处理器。](https://github.com/sidequestjs/sidequest)

**原文标题**: [GitHub - sidequestjs/sidequest: Sidequest is a modern, scalable background job processor for Node.js applications.](https://github.com/sidequestjs/sidequest)

Sidequest 是一个专为 Node.js 应用设计的现代化、可扩展的后台任务处理器，采用 TypeScript 开发，适用于生产环境，提供可靠的任务处理、多数据库支持、可视化面板和全面的监控功能。

- 🚀 高性能：使用工作线程进行非阻塞任务处理
- 🗄️ 多后端支持：内置 SQLite、PostgreSQL 和 MySQL 数据库适配
- ✅ 兼容性：支持 ESM 和 CJS 模块，完全兼容现代 JavaScript
- 📝 TypeScript 原生支持：默认支持 TypeScript 任务（Node.js >= 24）
- 📊 可视化面板：提供美观、响应式的任务监控仪表板
- 🎯 队列管理：支持多队列配置、工作线程和优先级设置
- 🫀 任务生命周期管理：可配置重试机制（含指数退避）、暂停和失败处理
- ⏰ 定时任务：支持按特定时间调度任务执行
- 🔒 任务去重：通过灵活的唯一性约束防止重复任务
- 🛠️ CLI 工具：提供数据库迁移和管理的命令行接口
- 📦 模块化架构：采用 monorepo 结构，支持灵活部署
- 🤝 开源贡献：遵循 LGPL-3.0 许可证，欢迎社区参与

---

### [Node.js](https://nodejs.org/en/blog/release/v24.6.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v24.6.0)

Node.js v24.6.0 版本发布，包含多项功能增强、安全更新和性能优化，涵盖 CLI、加密、文件系统、HTTP 等多个核心模块的改进。

- 🔧 CLI 新增 `NODE_USE_SYSTEM_CA=1` 环境变量支持，允许使用系统 CA 存储
- 🔐 Crypto 模块新增 ML-DSA 算法的 KeyObject、签名和验证功能
- 📦 Zlib 模块为 zstdCompress 和 zstdDecompress 添加字典支持
- 🌐 HTTP 模块新增 server.keepAliveTimeoutBuffer 选项，优化连接管理
- 📁 FS 模块引入 Utf8Stream，移植 SonicBoom 模块功能
- ⚠️ 弃用部分内部 `_http_*` API，建议开发者避免使用
- 🛠️ 多项依赖更新，包括 OpenSSL 升级至 3.5.2，Undici 更新至 7.13.0
- 📚 文档改进和错误修复，提升开发者体验
- 🧪 测试套件增强，修复已知问题并提升稳定性
- 🔗 提供多平台安装包和二进制文件下载，支持 Windows、macOS、Linux 等系统

---

### [Node.js — 生命周期终止](https://nodejs.org/en/eol)

**原文标题**: [Node.js — End-Of-Life](https://nodejs.org/en/eol)

Node.js 版本按照预定计划进入维护终止期（EOL）后，将不再获得安全更新和漏洞修复，可能导致安全风险、工具链断裂和合规问题。商业支持可提供临时解决方案，但建议尽快升级至受支持的版本。

- 🗓️ Node.js 主版本采用可预测的维护周期，到期后停止官方维护
- ⚠️ EOL 版本存在安全漏洞无法修复、依赖库兼容性断裂、生态包停止支持等风险
- 📊 历史版本漏洞统计显示 v18 存在 14 个高危漏洞，v16 存在 11 个高危漏洞
- 🛡️ 通过 OpenJS 生态系统可持续计划可获取商业安全支持（如 HeroDevs 的 NES 服务）
- ⬆️ 建议优先升级至最新 LTS 版本，商业支持仅作为临时过渡方案

---

### [批量升级已弃用的 Node.js 版本 - Vercel](https://vercel.com/changelog/bulk-upgrade-deprecated-node-js-versions)

**原文标题**: [Bulk upgrade deprecated Node.js versions - Vercel](https://vercel.com/changelog/bulk-upgrade-deprecated-node-js-versions)

团队所有者和成员现可通过 Vercel 仪表盘一键将所有使用 Node.js 18 及更早版本的项目升级至 Node.js 22。

- 🚀 支持批量一键升级 Node.js 版本至 v22
- ⚙️ 自动更新项目设置中的运行时版本配置
- 📝 package.json 中定义的版本仍需手动更新
- 🔄 现有部署项目不会受到升级影响
- ⏰ 升级功能于 2025 年 8 月 8 日正式推出

---

### [Oxlint 类型感知预览 | JavaScript 氧化编译器](https://oxc.rs/blog/2025-08-17-oxlint-type-aware)

**原文标题**: [Oxlint Type-Aware Preview | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2025-08-17-oxlint-type-aware)

oxlint 宣布推出类型感知的 linting 预览版，通过集成 tsgolint 实现高性能的类型检查，支持 no-floating-promises 等规则，性能较 typescript-eslint 提升显著，并开源邀请社区协作。

- 🚀 推出类型感知 linting 预览版，支持 no-floating-promises 等规则
- ⚡ 性能大幅提升，大型项目 lint 时间从 1 分钟缩短至 10 秒内
- 🔧 通过 oxlint-tsgolint 集成，使用 --type-aware 标志启用
- 🏗️ 架构采用 oxlint（Rust）前端 + tsgolint（Go）后端的双二进制模式
- 📊 基于 typescript-go 实现，通过 shim 内部 API 访问类型系统
- ⚠️ 目前存在大仓库性能问题和版本依赖挑战
- 🎯 未来将优化性能、增加规则配置和 IDE 支持
- 🤝 感谢 TypeScript 团队和开源贡献者的支持

---

### [在 Cloudflare Workers 上运行 Express.js](https://jross.me/run-express-js-on-cloudflare-workers/)

**原文标题**: [Run Express.js on Cloudflare Workers](https://jross.me/run-express-js-on-cloudflare-workers/)

Cloudflare Workers 自 2025 年 8 月 5 日起通过 wrangler 4.28.0 版本原生支持 Express.js 应用，显著降低了 Node.js 开发者使用 Workers 的门槛，同时保持对 Hono 等原生框架的推荐。

- 🚀 通过启用`enable_nodejs_http_server_modules`兼容性标志和`cloudflare:node`的`httpServerHandler`API 实现原生支持
- ⚡ 开发阶段可直接运行完整 Express 应用，生产环境支持即将推出
- 💻 支持标准 Express 路由、中间件和错误处理，如示例中的 JSON 解析和 404 处理
- 🔄 无缝集成 Workers 生态，支持环境变量注入和 KV 存储等原生功能
- 📦 需在 wrangler.toml 配置 Node.js 兼容性标志和实验性功能
- ⚖️ 建议现有 Hono 项目无需迁移，但降低了传统 Node.js 应用迁移成本
- 🌟 Workerd 运行时持续改进 Node.js 兼容性，推动多运行时应用开发

---

### [Hono - 基于 Web 标准构建的 Web 框架](https://hono.dev/)

**原文标题**: [Hono - Web framework built on Web Standards](https://hono.dev/)

超快速轻量级路由器，采用 Web 标准 API 实现极高性能与微小体积  
- ⚡ RegExpRouter 路由器具备超高速性能  
- 📦 hono/tiny 预设包体积小于 14kB  
- 🌐 完全基于 Web 标准 API 开发

---

### [Express——Node.js Web 应用框架](https://expressjs.com/)

**原文标题**: [Express - Node.js web application framework](https://expressjs.com/)

Express 5.1.0 已成为 npm 默认版本，这是一个极简灵活的 Node.js Web 框架，提供构建 Web 应用和 API 的核心功能。

- 🚀 Express 5.1.0 现为 npm 默认版本并引入官方 LTS 支持计划
- 🌐 极简灵活的 Node.js Web 应用框架，支持 Web 和移动应用开发
- 🔌 提供丰富的 HTTP 工具方法和中间件，可快速构建稳健 API
- ⚡ 保持高性能的薄层设计，不掩盖原生 Node.js 特性
- 🧩 核心轻量灵活，可通过中间件模块扩展功能
- 📦 通过 npm install express --save 即可安装使用
- ⚙️ 提供简洁的路由配置和服务器启动方式（示例代码展示基础用法）

---

### [AWS 最新动态 - 云创新与资讯](https://aws.amazon.com/about-aws/whats-new/2025/08/aws-lambda-github-actions-function-deployment/)

**原文标题**: [What's New at AWS - Cloud Innovation & News](https://aws.amazon.com/about-aws/whats-new/2025/08/aws-lambda-github-actions-function-deployment/)

AWS Lambda 现支持通过 GitHub Actions 简化函数部署流程，实现代码推送自动部署。  
- 🚀 支持 GitHub Actions 实现 Lambda 函数自动部署，推动代码即触发 CI/CD 流程  
- ⚡ 消除手动打包代码、配置 IAM 权限和错误处理等复杂步骤  
- 📦 同时支持.zip 文件与容器镜像两种部署方式，自动处理代码打包  
- 🔐 集成 OIDC 认证实现与 IAM 的无缝安全对接  
- ⚙️ 可配置运行时环境、内存大小、超时设置及环境变量等参数  
- 🧪 提供 dry run 模式供部署前验证，支持大文件 S3 传输  
- 🌍 适用于所有 AWS 商用区域的 Lambda 服务

---

### [Shopify Webhook 解析错误导致数据库完全删除事件](https://www.ingressr.com/blog/webhook-security-incident-analysis/)

**原文标题**: [How Incorrect Shopify Webhook Parsing Led to Complete Database Deletion](https://www.ingressr.com/blog/webhook-security-incident-analysis/)

2025 年 8 月 15 日，Shopify 应用因 Webhook 解析错误导致数据库被完全删除的安全事件，突显了正确处理输入验证和理解 ORM 行为的重要性。该事件发生在 Ingressr 访客分析应用中，涉及 GDPR 合规的 SHOP_REDACT webhook 处理漏洞。

- 🛑 **漏洞根源**：代码错误地尝试从数字类型的`shop_id`字段进行对象解构，导致`shopId`变为`undefined`
- ⚠️ **JavaScript 静默失败**：解构原始值时不报错，而是静默返回`undefined`
- 💥 **ORM 陷阱**：`deleteMany()`操作使用`undefined`的`where`条件时，会删除表中所有记录
- 📊 **级联删除**：事件表和访客表的所有记录被成功删除，店铺表删除失败才暴露问题
- 🔄 **数据恢复成功**：得益于健全的备份机制，所有数据在几小时内从自动备份中完全恢复
- 🔧 **修复措施**：包括正确解析负载、输入验证、身份验证验证和多层安全加固
- 🛡️ **行业启示**：强调了 ORM 安全模式、Webhook 安全验证和 JavaScript 类型检查的重要性
- 📋 **预防策略**：需加强代码审查、全面测试协议以及监控和警报系统的实施

---

### [npm 采用 OIDC 实现 CI/CD 工作流中的可信发布 - ...](https://socket.dev/blog/npm-trusted-publishing)

**原文标题**: [npm Adopts OIDC for Trusted Publishing in CI/CD Workflows - ...](https://socket.dev/blog/npm-trusted-publishing)

研究人员揭露主流密码管理器中的零日点击劫持漏洞，黑客演示如何轻易窃取数据  
- 🔓 零日漏洞影响多款主流密码管理器  
- 🖱️ 通过点击劫持技术可绕过安全防护  
- 🎯 黑客能直接窃取存储的密码数据  
- ⚠️ 漏洞利用难度低且危害性极高  
- 📅 发现者于 2025 年 8 月 19 日公开披露

---

### [理解 Node.js 中的火焰图（以及 N|Solid 如何借助 AI 简化分析）](https://nodesource.com/blog/understanding-flame-graphs-in-nodejs)

**原文标题**: [Understanding Flame Graphs in Node.js (and How AI Makes Them Easier with N|Solid)](https://nodesource.com/blog/understanding-flame-graphs-in-nodejs)

本文介绍了火焰图在 Node.js 性能分析中的重要性，以及 N|Solid 如何通过 AI 技术简化火焰图的解读和优化建议生成。

- 🔥 火焰图通过可视化堆栈跟踪显示函数调用耗时，箱体宽度代表 CPU 时间消耗量
- ⚠️ 纠正常见误解：X 轴并非时间轴，而是按调用结构和频率聚合的堆栈数据
- ⏱️ 关键区分：自我时间（函数自身耗时）与总时间（包含子函数调用耗时）的分析至关重要
- 🎯 优化策略：寻找宽而孤立的箱体（高自我时间）和频繁调用的热路径
- 🤖 N|Solid 创新：通过 AI 自动生成性能摘要，直接提供可操作的优化建议和异常标注
- 💡 实际价值：将原本需要专业知识的性能分析转化为即时可用的诊断结论，大幅提升排查效率
- 🚀 应用场景：快速定位阻塞操作（如 PDF 生成模块）并给出具体解决方案（如移至 Worker 线程）

---

### [GitHub - gemini-testing/looks-same：用于比较图像的Node.js库](https://github.com/gemini-testing/looks-same)

**原文标题**: [GitHub - gemini-testing/looks-same: Node.js library for comparing images](https://github.com/gemini-testing/looks-same)

这是一个用于比较 PNG 图像的 Node.js 库，专门为视觉回归测试设计，支持多种比较模式和差异分析功能。

- 📚 纯 Node.js 库，专注于 PNG 图像比较并考虑人类颜色感知
- ⚡ 提供严格模式和容差设置，可灵活调整比较灵敏度
- 🖱️ 支持忽略文本光标闪烁和抗锯齿差异的智能比较
- 🎯 能够获取差异边界和聚类信息，精确定位图像差异区域
- 🖼️ 内置生成差异图像功能，支持多种图像格式输出
- 🎨 额外提供颜色比较功能，可直接对比 RGB 颜色值
- 📊 广泛应用于测试工具，已被 4.9k+ 项目使用
- 🔧 采用 MIT 开源协议，拥有活跃的社区贡献

---

### [8.8.0 版本发布 — 压力测试 · google/zx · GitHub](https://github.com/google/zx/releases/tag/8.8.0)

**原文标题**: [Release 8.8.0 — Pressure Tested · google/zx · GitHub](https://github.com/google/zx/releases/tag/8.8.0)

该版本增强了 ProcessPromise 与 Streams API 之间的协调性，引入了多项新功能并修复了已知问题。

- 🚀 新增 unpipe() 方法，可选择性停止数据流传输而不关闭进程
- 🔄 支持多对一流管道，允许多个源同时流向单一目标
- ⚡ 错误进程现在仍可进行输出管道传输，保留流状态和退出码
- 📦 新增版本信息静态映射，可查看 zx 及第三方库版本号
- 🐛 修复了 ProcessPromise 与 Streams API 间的协调性问题
- ✨ 移除了部分脚本级解决方案的需求

---

### [入门指南 | google/zx](https://google.github.io/zx/getting-started)

**原文标题**: [Getting Started | google/zx](https://google.github.io/zx/getting-started)

zx 是一个基于 Node.js 的 Shell 脚本工具库，通过提供便捷的 API 和自动转义功能简化了复杂脚本的编写

- 🚀 提供`$`函数执行命令并返回 Promise，支持同步和异步两种模式
- 🛡️ 自动转义和引用参数变量，无需手动添加引号
- ⚡ 支持顶层 await，可直接在.mjs 文件中使用或通过 shebang 运行
- 🔧 包含常用工具函数如 cd、fetch 等，无需导入即可使用
- 🎯 支持 TypeScript，提供良好的类型提示支持
- ❌ 当进程返回非零退出码时会抛出 ProcessOutput 异常
- 📦 通过 npm 安装，采用 Apache-2.0 开源协议

---

### [注册 - Auth0](https://auth0.com/signup?utm_source=nodeweekly&utm_campaign=global_mult_mult_all_ciam-dev_dg-plg_auth0_native_nodeweekly_newsletter_aud_NodeWeekly-Q3-Newsletter_utm2&utm_medium=cpc&utm_id=aNKKZ00000003C04AI)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?utm_source=nodeweekly&utm_campaign=global_mult_mult_all_ciam-dev_dg-plg_auth0_native_nodeweekly_newsletter_aud_NodeWeekly-Q3-Newsletter_utm2&utm_medium=cpc&utm_id=aNKKZ00000003C04AI)

这是一个用户注册页面，提供多种注册方式和全球国家选择，强调简化登录流程和安全保障。

- 📧 需要填写邮箱和国家信息进行注册  
- 🌍 提供全球多个国家/地区选项  
- 🔐 支持 GitHub、Google、Microsoft 第三方账号快速登录  
- 🛡️ 包含暴力破解保护和可疑 IP 限制等安全功能  
- 🆓 提供免费层级（2.5 万月活用户）和无限制登录次数  
- ⚙️ 提供无代码可定制的注册/登录流程和密码 less 连接  
- ©️ 由 Okta 公司旗下的 Auth0 服务提供

---

### [Pyodide — 版本 0.28.2](https://pyodide.org/en/stable/index.html)

**原文标题**: [Pyodide — Version 0.28.2](https://pyodide.org/en/stable/index.html)

Pyodide 是一个基于 WebAssembly 的 Python 发行版，可在浏览器和 Node.js 环境中运行，支持科学计算包和双向语言互操作。

- 🐍 CPython 的 WebAssembly 移植版本，支持浏览器端运行 Python
- 📦 通过 micropip 安装 PyPI 纯 Python 包，兼容 NumPy/pandas 等科学计算库
- 🔄 提供完整的 JavaScript 与 Python 双向调用接口，支持错误处理和异步操作
- 🌐 浏览器环境中可直接调用 Web API，无需安装即可在线试用 REPL
- 📚 提供多场景使用指南：托管部署/打包工具集成/包维护指南
- 🛠️ 开源项目支持社区贡献，包含完整的开发文档和测试框架
- 📢 通过邮件列表/Gitter/Twitter 等多渠道进行社区交流

---

### [使用 Pyodide — 版本 0.28.2](https://pyodide.org/en/stable/usage/index.html#node-js)

**原文标题**: [Using Pyodide — Version 0.28.2](https://pyodide.org/en/stable/usage/index.html#node-js)

Pyodide 是一个可在浏览器和 Node.js 环境中运行 Python 的工具，通过 WebAssembly 技术实现 Python 与 JavaScript 的互操作。

- 🌐 在网页中使用需加载 pyodide.js 并通过 loadPyodide() 初始化
- ⚠️ 推荐使用最新版浏览器（Firefox 112+/Chrome 112+/Safari 16.4+）以获得完整功能支持
- 🧵 可通过 Web Worker 运行避免主线程阻塞
- 📦 提供 NPM 包支持 Node.js 集成（要求 Node.js ≥ 18）
- 🔧 支持在 Node.js REPL 中交互式运行 Python 代码
- 📚 包含完整的包管理功能和类型转换能力

---

### [QuickJS 沙盒 - 安全可靠地执行 JavaScript 和 TypeScript 代码 | QuickJS](https://sebastianwessel.github.io/quickjs/)

**原文标题**: [QuickJS Sandbox - Execute JavaScript and TypeScript code safe and secure | QuickJS](https://sebastianwessel.github.io/quickjs/)

人工智能生成的代码应在隔离的沙箱环境中执行以确保安全。  
- 🤖 使用沙箱环境执行 AI 生成代码

---

### [QuickJS JavaScript 引擎](https://bellard.org/quickjs/)

**原文标题**: [QuickJS Javascript Engine](https://bellard.org/quickjs/)

QuickJS 是一个轻量级可嵌入的 JavaScript 引擎，支持 ES2023 规范，具有快速启动和低内存占用的特点，适用于嵌入式系统和工具开发。

- 🚀 最新版本 2025-04-26 移除了大数扩展和 qjscalc 应用，推荐使用 BFCalc 计算器替代
- 📏 超轻量设计：仅需少量 C 文件，无外部依赖，hello world 程序仅 367KiB
- ⚡ 极速启动：单核桌面电脑 2 分钟完成 78000 项 ECMAScript 测试套件
- 🌐 完整支持 ES2023 规范：包括模块、异步生成器、代理和 BigInt 等特性
- 🔄 采用引用计数垃圾回收机制，支持循环引用检测
- 📦 可将 JavaScript 源码编译为无依赖的可执行文件
- 🖥️ 提供命令行解释器，支持语法高亮和在线演示环境
- 📚 内置精简标准库，包含 C 库封装和独立的正则表达式/Unicode 组件
- 🔗 支持多平台二进制分发（Linux/Mac/Windows/BSD 等架构）
- 📄 采用 MIT 开源协议，由 Fabrice Bellard 和 Charlie Gordon 主导开发

---

### [GitHub - sebastianwessel/quickjs：一个在WebAssembly QuickJS 沙箱中执行 JavaScript 和 TypeScript 代码的 TypeScript 包](https://github.com/sebastianwessel/quickjs)

**原文标题**: [GitHub - sebastianwessel/quickjs: A typescript package to execute JavaScript and TypeScript code in a webassembly quickjs sandbox](https://github.com/sebastianwessel/quickjs)

这是一个基于 TypeScript 的包，用于在 WebAssembly QuickJS 沙箱中安全执行 JavaScript 和 TypeScript 代码，提供隔离环境运行不受信任的代码。

- 🛡️ 安全执行 JavaScript 和 TypeScript 代码于隔离的 WebAssembly 沙箱环境中
- 📦 提供基本 Node.js 模块支持，并可挂载自定义模块和虚拟文件系统
- 🌐 包含 fetch 客户端功能，允许进行 HTTP(S) 调用
- 🧪 内置测试运行器和基于 Chai 的 expect 断言库
- ⚡ 基于轻量高效的 QuickJS 引擎，性能优越
- 🔧 采用 MIT 许可证开源，拥有 767 个星标和 25 个分支
- 🚀 易于与现有 TypeScript 项目集成，提供用户友好的 API

---

### [GitHub - psema4/yikes: 天呐！你的无限知识娱乐系统（基于本地大语言模型的文字角色扮演沙盒游戏）](https://github.com/psema4/yikes)

**原文标题**: [GitHub - psema4/yikes: YIKES! Your infinite knowledge entertainment system (a text-based RPG sandbox powered by local llm's)](https://github.com/psema4/yikes)

YIKES 是一款基于本地大型语言模型的文本冒险游戏引擎，提供由 AI 主持的动态交互式角色扮演体验。

- 🎮 支持多类型设定（奇幻/科幻）与 AI 生成角色背景描述
- 🤖 依赖 Ollama 本地模型驱动（需安装 dolphin3:8b 模型）
- 👤 包含完整角色创建系统（种族/职业/属性/库存管理）
- ⚙️ 采用 Node.js 开发，具备模块化架构设计
- 📜 开源 ISC 许可证，支持社区贡献
- 🎯 内置健康值、属性统计和货币体系等游戏机制

---

### [发布 NVM Desktop v4.1.0 · 1111mp/nvm-desktop · GitHub](https://github.com/1111mp/nvm-desktop/releases/tag/v4.1.0)

**原文标题**: [Release NVM Desktop v4.1.0 · 1111mp/nvm-desktop · GitHub](https://github.com/1111mp/nvm-desktop/releases/tag/v4.1.0)

NVM Desktop v4.1.0 版本发布，提供跨平台 Node 版本管理桌面应用，包含新功能、性能优化和多平台下载支持。

- 🚀 版本 v4.1.0 于 2025 年 8 月 15 日发布，包含功能更新和性能优化
- ⚙️ 新增 Node 下载与卸载命令支持 (#184 功能实现)
- 🔄 内置实时数据刷新服务器，实现命令行工具与客户端数据同步
- 🐛 修复文本显示问题 (#189 错误修正) 
- 🏎️ 进行性能优化并重构 nvmd 命令行工具，提升运行效率
- 💻 提供多平台安装包：macOS(Intel/M 芯片)、Linux(amd64/arm64 架构)、Windows(含 Webview2 特殊版本)
- 👥 由开发者 1111mp 和 zyx006 共同维护开发

---

### [发布 v6.5.0 · thecodrr/fdir · GitHub](https://github.com/thecodrr/fdir/releases/tag/v6.5.0)

**原文标题**: [Release v6.5.0 · thecodrr/fdir · GitHub](https://github.com/thecodrr/fdir/releases/tag/v6.5.0)

fdir v6.5.0 版本发布，带来 ESM 支持、Node v12 兼容性修复、自定义 FS 模块等多项功能更新和优化。

- 📦 新增 ESM 构建支持，同时保留 CommonJS 构建
- 🔙 恢复 Node v12 和 v14 兼容性，使用内部解决方案替代 AbortController
- 🛠️ 支持自定义 FS 模块，可替代 Node.js 原生 fs 模块
- ⚡ 性能优化：使用 slice 方法替代 replace 进行路径拼接
- 🐛 修复对@types/picomatch v4 版本的支持问题
- 👥 新增 4 位贡献者参与本次版本开发

---

### [GitHub - loopbackio/strong-soap: Node.js 的 SOAP 驱动（node-soap 的完全重写版）](https://github.com/loopbackio/strong-soap)

**原文标题**: [GitHub - loopbackio/strong-soap: SOAP driver for Node.js (A complete rewrite of node-soap)](https://github.com/loopbackio/strong-soap)

strong-soap 是一个用于 Node.js 的完整 SOAP 客户端和模拟服务器模块，支持 RPC 和文档样式，提供 XML/JSON 转换、WSDL 解析和安全协议等功能。

- 🚀 提供完整的 SOAP 客户端和模拟服务器功能，支持 RPC 和文档样式
- 🔧 支持 XML 与 JSON 互相转换，可自定义属性键、值键和 XML 键
- 🔐 内置多种安全协议，包括 BasicAuth、BearerToken、SSL 和 WS-Security
- 📡 客户端支持同步/异步调用、自定义请求头和端点覆盖
- 🛠️ 服务器端支持身份验证、连接授权和 SOAP 报头处理
- 📦 包含 soap-stub 工具，便于单元测试和客户端模拟
- 🌐 支持 SOAP 1.1 和 1.2 错误处理，兼容多种 WSDL 操作类型

---

### [幽灵 6.0](https://ghost.org/changelog/6/)

**原文标题**: [Ghost 6.0](https://ghost.org/changelog/6/)

Ghost 6.0 版本正式发布，引入开放网络发布、原生分析工具，并宣布独立出版商通过该平台已累计赚取超过 1 亿美元收入。此次更新还包括多项功能升级、定价调整及开发者相关改进。

- 🌐 开放网络集成：Ghost 出版物现可跨 Bluesky、Mastodon、Threads 等社交平台实现内容发现、关注和互动
- 📊 原生分析套件：内置实时数据分析功能，覆盖网站流量、邮件推送和会员订阅等多维度指标
- 💰 商业成就：平台出版商总收入突破 1 亿美元，证明独立媒体商业模式的成功
- 🚀 功能全面升级：包括多语言支持、邮件简报增强、支付方式扩展、全新主题模板和编辑器重构
- 📉 定价策略调整：高端套餐降价达 50%，基础套餐小幅提价，新用户享首三月 5 折优惠
- 🛠️ 开发者更新：转向 Docker Compose 部署，生产环境升级至 Ubuntu 24/Node 22/MySQL8技术栈
- 🔓 坚持开源理念：作为非营利基金会运营，始终提供完全开源的自主托管选项

---

### [fastify/fastify 版本 v5.5.0 发布 · GitHub](https://github.com/fastify/fastify/releases/tag/v5.5.0)

**原文标题**: [Release v5.5.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.5.0)

Fastify 框架发布了 v5.5.0 版本，包含多项功能优化、错误修复和文档改进，移除了对 simple-get 的依赖，并引入了新的类型支持和性能提升。

- 🚀 版本 v5.5.0 由 Eomm 于 8 月 11 日发布，包含 3 个提交至主分支
- 🔧 大量移除 simple-get 依赖的测试代码重构，涉及多个测试模块
- 📝 修复了多个文档问题，包括 Markdown 格式、钩子执行顺序和参数名称更正
- 🐛 解决了 pipelining 测试关闭、JSON 解析错误和 OPTIONS 内容类型处理等问题
- ⚡ 通过 AsyncResource.bind() 优化了内容类型解析器的性能
- 📦 更新了多个依赖项，包括 @types/node、TypeScript 和 cross-env
- 👥 新增了 13 位贡献者，包括首次提交的开发者
- ❤️ 社区反应热烈，获得多个表情符号互动（16 人参与）

---

### [GitHub - entronad/crypto-es: 加密算法库](https://github.com/entronad/crypto-es)

**原文标题**: [GitHub - entronad/crypto-es: A cryptography algorithms library](https://github.com/entronad/crypto-es)

这是一个名为 crypto-es 的加密算法库，提供多种加密哈希函数、密码算法和编码器功能，支持渐进式处理和自定义格式。

- 🔐 支持多种哈希算法包括 MD5、SHA 系列、RIPEMD-160 和 Keccak
- 🛡️ 提供 HMAC 消息认证和 PBKDF2 密钥派生功能
- 🔄 包含 AES、DES、TripleDES、Rabbit、RC4 和 Blowfish 等加密算法
- 📦 支持完整导入或按需导入以减少包体积
- ⚙️ 可配置块模式、填充方案和自定义密钥/IV
- 🔄 支持渐进式哈希和加密处理
- 📊 提供多种编码格式转换（Base64、Hex、UTF-8 等）
- 📁 支持 ArrayBuffer 和 TypedArray 处理文件加密
- 🌐 与 OpenSSL 兼容并可自定义 JSON 格式器

---

### [Prisma 6.14.0 版本发布 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.14.0)

**原文标题**: [Release 6.14.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.14.0)

Prisma ORM 发布了 6.14.0 稳定版本，主要引入了视图的 @unique 属性支持、多项稳定性改进和类型性能优化，同时宣布了管理 API 的增强和 OAuth 令牌撤销功能。

- 🎯 视图支持 @unique 属性（预览功能），允许在 SQL 视图中定义唯一约束，实现关系关联和游标分页
- 🔧 修复了 prisma-client 生成器和 queryCompiler 预览功能的多个问题，为 Prisma 7 默认启用做准备
- 🗑️ 移除了已弃用的 prisma.$use 中间件方法，推荐使用 Prisma Client 扩展替代
- 📉 弃用了 metrics 预览功能（将在 Prisma 7 中移除）
- ⚡ 改进了类型性能，减少编辑器延迟和自动完成卡顿
- 🌐 增强了管理 API（早期访问），支持通过编程方式管理 Prisma Postgres 实例
- 🔒 Prisma 控制台新增 OAuth 令牌撤销功能，可随时取消第三方应用访问权限
- 📚 回顾了上一版本的重要更新：包括 Prisma 配置文件正式可用、多模式支持和扩展功能增强

---

### [发布 v7.14.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.14.0)

**原文标题**: [Release v7.14.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.14.0)

Undici 库发布了 v7.14.0 版本更新，包含多项功能改进和错误修复

- 🐛 修复快照测试不稳定问题和缓存机制异常
- ✨ 新增 WebSocket 握手响应诊断事件和 EventSource 重连时间配置功能
- 📦 类型定义增加 install() 函数并改进模块导入方式
- 🔧 更新多项依赖包版本并优化 CI 测试流程
- 👥 包含 2 位新贡献者的首次代码提交

---

### [GitHub - vpulim/node-soap: Node.js 的 SOAP 客户端与服务器实现](https://github.com/vpulim/node-soap)

**原文标题**: [GitHub - vpulim/node-soap: A SOAP client and server for node.js.](https://github.com/vpulim/node-soap)

node-soap 是一个用于 Node.js 的 SOAP 客户端和服务器库，支持创建和调用基于 WSDL 的 Web 服务，提供丰富的 API 和配置选项。

- 🚀 支持 SOAP 客户端和服务器功能，兼容 RPC 和 Document 类型的架构
- 🔧 提供同步和异步方法处理，支持 Promise 和回调两种模式
- 🛡️ 内置多种安全协议，如 BasicAuth、WSSecurity、SSL 等
- 📦 可通过 npm 安装，使用 `npm install soap` 即可集成
- 🌐 支持 Express 服务器和自定义 HTTP 头处理
- ⚙️ 允许覆盖 XML 属性、值和命名空间等配置
- 📡 支持附件处理（MTOM）和流式响应解析
- 🔍 提供详细的错误处理和日志功能
- 🧪 包含单元测试工具 soap-stub，便于测试

---

### [ESLint v9.33.0 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/08/eslint-v9.33.0-released/)

**原文标题**: [ESLint v9.33.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/08/eslint-v9.33.0-released/)

ESLint v9.33.0 是一个次要版本更新，引入了新功能并修复了之前版本中的多个错误。

- 🆕 新增了对显式资源管理语法的支持，one-var 规则现在可以处理 using 和 await using 声明的变量
- 🔍 no-restricted-globals 规则新增全局对象访问检测功能，可通过三个新选项控制检测行为
- 🐛 修复了自定义规则中 meta.docs.recommended 类型限制的问题
- 📚 更新了多个文档内容，包括 Playground 对 TypeScript 的支持和规则文档的完善
- 🔧 进行了构建系统优化和测试用例改进，提升了稳定性和开发体验

---

### [开始使用 Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-1&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-1&utm_content=cloud_-_redis_cloud_users)

Redis 是一个高速数据平台，提供云端和本地部署解决方案，帮助开发者快速构建应用程序，支持向量数据库、缓存和 NoSQL 数据库等多种功能。

- 🚀 全球最快的数据平台，提供云端和本地解决方案，加速应用开发
- 🗄️ 支持向量数据库，构建高性能生成式 AI 应用
- ⚡ 内存缓存技术，提升应用响应速度
- 🗂️ NoSQL 键值存储，支持多种数据结构，适用于实时应用
- 🌱 轻松创建数据库，支持从实验到生产环境的无缝扩展
- 💻 提供开发者中心、架构师演示和 DevOps 资源，支持多语言开发
- 🆓 提供免费试用，快速开始构建应用

---

### [GitHub - glitternetwork/pinme: 一键部署你的前端应用](https://github.com/glitternetwork/pinme)

**原文标题**: [GitHub - glitternetwork/pinme: Deploy Your Frontend in a Single Command](https://github.com/glitternetwork/pinme)

PinMe 是一个简单易用的命令行工具，用于将文件和目录上传到 IPFS 网络，支持快速部署前端项目并生成可访问链接。

- 🚀 支持通过 npm 或 yarn 全局安装，提供交互式和指定路径两种上传模式
- 📁 单文件上限 20MB，目录总大小限制 500MB，自动生成 IPFS 哈希和访问链接
- 🔄 提供历史记录管理功能，可查看/清除上传记录或通过哈希删除文件
- ⚠️ 删除操作仅从本地节点取消固定，不保证从 IPFS 网络完全移除
- 🌐 特别优化 Vite 项目部署，需在配置中添加 base: "./"确保路径解析正确
- 📝 日志存储在用户目录的.pinme 文件夹，采用 MIT 开源协议
- 📧 可通过 GitHub Issues 或专属邮箱联系 Glitter Protocol 团队获取支持

---

### [JavaScript 的真实演进：与 Daniel Ehrenberg 探秘 TC39 内部 - YouTube](https://www.youtube.com/watch?v=v9Al9-0jkoQ)

**原文标题**: [How JavaScript Really Evolves: Inside TC39 with Daniel Ehrenberg - YouTube](https://www.youtube.com/watch?v=v9Al9-0jkoQ)

这是 YouTube 网站页脚常见链接列表的摘要概述

- ℹ️ 关于平台的基本信息
- 📰 新闻与媒体相关资源
- ©️ 版权声明与保护政策
- 📞 用户联系渠道
- 🎬 内容创作者相关信息
- 💼 广告合作与商业推广
- 👨‍💻 开发者资源与 API
- 📑 服务条款与使用协议
- 🔒 隐私保护政策说明
- ⚖️ 平台政策与安全指南
- 🔧 平台功能运作机制介绍
- 🧪 新功能测试相关信息
- ®️ 2025 年谷歌公司版权所有声明

---

### [我如何构建出比 Next.js 快 4 倍、吞吐量高 4 倍的全栈 React 框架 - Ryan Skinner](https://ryanskinner.com/posts/how-i-built-a-full-stack-react-framework-4x-faster-than-nextjs-with-4x-more-throughput)

**原文标题**: [How I Built a Full-Stack React Framework 4x Faster Than Next.js With 4x More Throughput - Ryan Skinner](https://ryanskinner.com/posts/how-i-built-a-full-stack-react-framework-4x-faster-than-nextjs-with-4x-more-throughput)

经过 25 年 web 开发经验，作者推出全新全栈 React 框架 Rari，通过 Rust 运行时架构实现突破性性能提升

- 🚀 组件渲染速度快 4.04 倍（4.23ms vs 17.11ms）
- 📊 吞吐量提升 3.74 倍（10,586 req/sec vs 2,832 req/sec）  
- ⚡ 构建时间快 5.80 倍（1.59 秒 vs 9.22 秒）
- 🌊 100% 支持 React 服务端组件并具备真流式传输
- 🔧 三层架构：Rust 核心运行时 + Vite 智能集成 + 标准 RSC 实现
- 🛠️ 完整开发体验：热更新/TypeScript/无配置路由
- 📦 开源 MIT 协议，社区驱动发展
- 🎯 设计理念：性能与开发体验并重，打破传统框架性能天花板

---

### [获取失败](https://nodeweekly.com/link/172997/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/172997/web)

无法总结：获取内容失败，状态码 503。

---

### [Git 2.51 亮点集锦 - GitHub 官方博客](https://github.blog/open-source/git/highlights-from-git-2-51/)

**原文标题**: [Highlights from Git 2.51 - The GitHub Blog](https://github.blog/open-source/git/highlights-from-git-2-51/)

Git 2.51 版本带来了多项性能优化和功能改进，包括更高效的多包索引处理、更小的包文件生成方式、增强的储藏功能交互性，以及其他多项实用更新。

- 🚀 引入`repack.MIDXMustContainCruft`配置，允许将 cruft 包排除在多包索引（MIDX）之外，显著减小 MIDX 大小并提升读取性能
- 📦 新增`--path-walk`打包选项，通过按路径分组对象优化增量压缩，生成更小的包文件
- 💾 改进储藏功能，支持多条目序列化存储和跨机器导入导出，提升协作便利性
- 🔍 增强`git cat-file`命令，完善对子模块信息的输出支持
- 🌸 扩展 changed-path Bloom 过滤器，支持多路径查询优化
- ✅ 正式将`git switch`和`git restore`标记为稳定命令，不再视为实验性功能
- ⚠️ 弃用`git whatchanged`命令，计划在 Git 3.0 中移除
- 🔮 预告 Git 3.0 将默认采用 reftable 后端和 SHA-256 哈希函数
- 📝 内部代码库开始广泛使用 C99 标准的`bool`关键字，并更新贡献指南允许非真名提交

---

### [学习网页开发：JavaScript 中的数组](https://2ality.com/2025/08/javascript-arrays.html)

**原文标题**: [Learning web development: Arrays in JavaScript](https://2ality.com/2025/08/javascript-arrays.html)

本文介绍了 JavaScript 数组的基础知识，包括创建、访问和修改数组元素，以及数组的可变性。通过一个魔法 8 球项目示例，展示了如何利用数组和随机数生成函数实现交互功能。

- 📚 数组是存储多个值的变量，使用方括号和逗号分隔元素创建
- 🔢 数组元素通过从 0 开始的索引访问和修改，使用.length 属性获取数组长度
- 🔄 即使使用 const 声明，数组内容仍可修改，因为 const 只保护变量引用而非内容
- 💬 JavaScript 支持单行 (//) 和多行 (/* */) 注释，多行注释可跨越多行
- 🎱 魔法 8 球项目演示了如何用数组存储答案，通过随机索引选择并显示答案
- 🎲 getRandomInteger() 函数使用 Math.random() 和 Math.floor() 生成指定范围内的随机整数
- 💡 练习建议修改项目以随机显示笑话、引用或颜色等内容

---

### [jQuery 4.0.0 候选版本 1 | 官方 jQuery 博客](https://blog.jquery.com/2025/08/11/jquery-4-0-0-release-candidate-1/)

**原文标题**: [jQuery 4.0.0 Release Candidate 1 | Official jQuery Blog](https://blog.jquery.com/2025/08/11/jquery-4-0-0-release-candidate-1/)

jQuery 4.0.0 首个候选版本已发布，标志着即将迎来重大版本更新，包含多项突破性变更并移除对旧版 IE 的支持，同时提供精简版构建选项。

- 🚀 jQuery 4.0.0-rc.1 版本正式发布，进入最终测试阶段
- 🔄 提供 4.0 升级指南和迁移工具辅助版本过渡
- 🗑️ 移除对 IE11 以下版本支持及已弃用的 API 接口
- 📦 新增 Slim 精简版本（减少 8KB 压缩体积），移除 Ajax/动画/Deferred 模块
- 🌐 支持通过 jQuery CDN 和 npm 包管理器获取发行版本
- ✨ 包含 CSS 维度修复、DOMParser 切换等核心优化
- 🤝 特别鸣谢贡献代码修复及测试的社区开发者

---

