### [Vercel Ship 2025](https://vercel.com/ship)

**原文标题**: [Vercel Ship 2025](https://vercel.com/ship)

Vercel 是一个为开发者提供工具和云基础设施的完整平台，旨在构建、扩展和保护更快速、个性化的网络体验。

- 🚀 Vercel 提供开发者工具和云基础设施，助力构建更快、更个性化的网络体验  
- 💡 特色活动包括 Cisco XDR 安全平台迁移至 Vercel 的案例分享  
- 🔍 优化网站以适应答案引擎优化（AEO）的策略分享  
- 🛒 北欧最大电子产品零售商 Elkjøp 使用 Next.js 和 Vercel 将上线时间从七周缩短至一天  
- 👥 特邀演讲嘉宾包括 Vercel 创始人兼 CEO Guillermo Rauch 和 COO Jeanne Grosser 等  
- ❓ 活动常见问题解答涵盖活动内容、线上线下体验差异、赞助参与等  
- 🏆 活动赞助商分为钻石、白金、黄金和白银等级  
- 🌟 去年 Vercel Ship 2024 聚焦前端云的强大功能，今年活动将继续探索网络产品的最新创新

---

### [推出 Fluid 计算服务的动态 CPU 定价 - Vercel](https://vercel.com/blog/introducing-active-cpu-pricing-for-fluid-compute)

**原文标题**: [Introducing Active CPU pricing for Fluid compute - Vercel](https://vercel.com/blog/introducing-active-cpu-pricing-for-fluid-compute)

Fluid compute 是一种新型计算模型，专为 I/O 密集型后端工作负载（如 AI 推理、代理和 MCP 服务器）设计，能够即时扩展并在操作间保持空闲状态。

- 🚀 **Fluid compute 成为默认模型**：在 Vercel 上帮助团队通过函数内并发等优化节省高达 85% 的成本。
- 💡 **新定价模式 Active CPU**：仅在代码实际使用 CPU 时计费，进一步提升了效率和成本节约。
- ⏳ **从服务器到无服务器**：传统云计算的长期服务器存在资源浪费，而无服务器虽简化了基础设施但带来了冷启动和资源利用不足的问题。
- 🔄 **从无服务器到 Fluid compute**：通过智能编排计算资源，允许多个并发请求共享底层资源，消除冷启动并重用空闲时间。
- 💰 **成本节约显著**：Fluid compute 在 Vercel 上支持了超过一万亿次调用，团队节省了高达 90% 的成本。
- ⏱ **Active CPU 定价**：解决了空闲时段 CPU 成本问题，仅在实际使用 CPU 时计费。
- 📊 **定价模型细节**：
  - **Active CPU**：按实际使用的 vCPU 时间计费，每小时 $0.128 起。
  - **Provisioned Memory**：按 GB 小时计费，费率低于 Active CPU 的 10%。
  - **Invocations**：按函数调用次数计费。
- 💻 **现代应用支持**：Fluid compute 支持 Node.js、Python 和 Go 等标准运行时，无需更改现有代码。
- 🌐 **平台集成**：Fluid compute 支持 Vercel 的核心产品体验，包括 Functions 和 Sandbox。
- 🎯 **即时可用**：Active CPU 定价现已默认适用于 Hobby、Pro 和新 Enterprise 团队，现有 Enterprise 客户可根据配置启用。
- 📉 **自动优化成本**：Active CPU 根据实际使用情况自动优化成本，减少浪费并反映现代应用的运行方式。
- 🤖 **AI 应用优化**：通过 Fluid compute 部署 AI 应用，最大化计算资源利用。

---

### [介绍 BotID，关键路径的无形机器人过滤技术 - Vercel](https://vercel.com/blog/introducing-botid)

**原文标题**: [​Introducing BotID, invisible bot filtering for critical routes - Vercel](https://vercel.com/blog/introducing-botid)

现代高级机器人（bots）已能模拟人类行为，执行 JavaScript、绕过验证码，并通过工具（如 Playwright/Puppeteer）模仿真实用户操作，传统防御手段（如请求头检查或速率限制）难以应对。

- 🤖 **BotID 简介**：Vercel 推出的新型防护层，通过"隐形验证码"在自动化访问到达后端前拦截，重点保护关键路径（如支付、登录、API 等）。  
- 🛠️ **快速集成**：无需复杂配置，安装包后通过服务端函数`checkBotId()`即可验证请求，拦截机器人返回 403 错误。  
- 🔍 **工作原理**：  
  - **基础模式**：默认启用，会话级检测，注入动态混淆代码抵抗逆向分析。  
  - **深度分析**（Pro/Enterprise 专享）：结合 Kasada 引擎，通过机器学习实时更新防御策略，对抗高级自适应机器人。  
- 🚫 **与传统防御差异**：不依赖易伪造的静态信号（如 User-Agent/IP），避免验证码或启发式规则干扰真实用户。  
- 🌐 **全局智能网络**：收集数千行为信号，动态变异检测逻辑，并通过共享攻击模式持续优化全网防护。  
- ⚡ **开发者友好**：无 API 密钥或复杂阈值配置，验证结果直接返回通过/失败。  
- 🛡️ **Kasada 加持**：集成企业级防护（如保护 v0.dev），自动随部署生效，无需额外服务配置。  
- 🎯 **适用场景**：针对高价值路径的定向自动化攻击（如抢购、虚假注册、凭证填充、敏感数据爬取）。  
- 📢 **发布信息**：基础版全团队可用，深度分析版限 Pro/Enterprise 用户，补充现有 DDoS/WAF 等平台级防护。  

👉 **行动号召**：立即使用 BotID 保护登录、支付等敏感路由，实现高效部署、高抗绕过防御。

---

### [使用 Vercel 沙盒运行不受信任的代码 - Vercel](https://vercel.com/changelog/run-untrusted-code-with-vercel-sandbox)

**原文标题**: [Run untrusted code with Vercel Sandbox - Vercel](https://vercel.com/changelog/run-untrusted-code-with-vercel-sandbox)

Vercel Sandbox 是一种由 Fluid compute 提供支持的云资源，旨在在隔离和临时的环境中运行不受信任的代码，如 AI 代理生成的代码。

- 🚀 **安全运行环境**：Vercel Sandbox 可以在隔离的微虚拟机中运行不受信任的代码，确保安全性。  
- ⏳ **临时执行**：支持最长 45 分钟的代码执行时间，适用于短期任务。  
- 📦 **独立 SDK**：Sandbox 是一个独立的 SDK，可以在任何环境中使用，包括非 Vercel 平台。  
- 💻 **示例代码**：通过示例展示了如何使用 Sandbox 运行 AI 生成的 Node.js 脚本。  
- 💰 **按需计费**：采用 Fluid 的 Active CPU 时间计费模式，仅在使用 CPU 时收费。  
- 🔍 **Beta 版本**：目前处于 Beta 阶段，所有计划的用户均可使用。

---

### [Vercel Agent 现已进入有限测试阶段 - Vercel](https://vercel.com/changelog/vercel-agent-now-in-limited-beta)

**原文标题**: [Vercel Agent now in Limited Beta - Vercel](https://vercel.com/changelog/vercel-agent-now-in-limited-beta)

Vercel Agent 现已推出有限测试版，这是一个集成在 Vercel 仪表板中的 AI 助手，专注于分析应用性能和安全性数据。

- 🔍 **功能概述**：Agent 专注于可观测性，能总结异常现象、识别可能原因并提供具体建议。  
- 🛠 **跨平台操作**：建议涵盖平台多个方面，如根据流量高峰或地理异常调整防火墙规则，或优化应用性能。  
- 📓 **无配置洞察**：以详细笔记本形式上下文呈现分析结果，无需额外配置。  
- ✉️ **参与方式**：通过 Vercel 社区报名表达兴趣，团队将主动联系符合条件的用户。

---

### [Vercel 微前端现已进入有限测试阶段 - Vercel](https://vercel.com/changelog/vercel-microfrontends-is-now-in-limited-beta)

**原文标题**: [Vercel Microfrontends is now in Limited Beta - Vercel](https://vercel.com/changelog/vercel-microfrontends-is-now-in-limited-beta)

Vercel Microfrontends 现已面向企业团队推出有限测试版，支持将多个前端应用部署和管理为一个统一的整体应用，同时允许各团队独立开发和部署。  

- 🚀 **加速大型应用开发**：将应用拆分为更小的独立单元，减少构建时间，团队可并行开发  
- 🛠️ **独立团队工作流**：每个团队可自主管理部署流程和技术栈  
- 🔄 **渐进式迁移**：逐步现代化遗留系统，避免大规模重写  
- 📢 **了解更多**：详情请查阅 [Vercel Microfrontends](链接)，或联系客户代表/销售团队加入测试

---

### [Vercel Queues 现已进入有限测试阶段 - Vercel](https://vercel.com/changelog/vercel-queues-is-now-in-limited-beta)

**原文标题**: [Vercel Queues is now in Limited Beta - Vercel](https://vercel.com/changelog/vercel-queues-is-now-in-limited-beta)

Vercel Queues 是一项专为 Vercel 应用打造的消息队列服务，目前处于有限测试阶段。它通过后台处理任务提升应用性能，支持可靠的重试和失败处理，适用于多种场景如 AI 视频处理、邮件发送等。

- 🚀 **功能概述**：Vercel Queues 允许将任务发送到队列中后台处理，提升用户体验和系统可靠性。  
- 📝 **持久化存储**：使用仅追加日志存储消息，确保任务如 AI 处理或邮件发送永不丢失。  
- 🔔 **发布/订阅模式**：支持基于主题的消息传递和多消费者组，提供灵活的通信方式。  
- 🌊 **流式处理**：无需完全加载到内存即可处理大容量数据负载。  
- 🔐 **简化认证**：通过 OIDC 令牌自动完成身份验证，集成更便捷。  
- 📦 **TypeScript SDK**：提供类型安全的开发体验，简化队列操作。  
- 💻 **代码示例**：展示如何发送和接收队列消息，例如输出“Hello World!”。  
- ✋ **参与方式**：加入 Vercel 社区并申请测试资格，团队将联系符合条件的用户。

---

### [运行 Fluid 计算的 Vercel 函数的更高默认值和限制 - Vercel](https://vercel.com/changelog/higher-defaults-and-limits-for-vercel-functions-running-fluid-compute)

**原文标题**: [Higher defaults and limits for Vercel Functions running Fluid compute - Vercel](https://vercel.com/changelog/higher-defaults-and-limits-for-vercel-functions-running-fluid-compute)

Vercel Functions 的默认限制已提升，包括执行时间、内存和 CPU 资源，并引入了更高效的 Active CPU 计费模式。

- ⏱️ 默认执行时间全面上调：所有计划的默认执行时间增至 300 秒（5 分钟），Hobby 计划从 60 秒提升，Pro/Enterprise 从 90 秒提升。
- 🚀 最大执行时间扩展：Pro/Enterprise 计划最高可配置 800 秒（原 Hobby 保持 300 秒上限）。
- 💾 内存与 CPU 升级：Standard 实例现为 1vCPU/2GB（原 1.7GB），Performance 实例现为 2vCPU/4GB（原 1.7vCPU/3GB）。
- 🗑️ 移除基础 CPU：Hobby 项目现在统一使用 Standard CPU 实例。
- 💡 采用 Active CPU 计费：按实际计算时间收费，内存闲置时段费率大幅降低，长时运行更经济。
- 📊 优化建议：可通过日志监控执行限制，调整最大时长或升级计划以适应需求。

---

### [边缘中间件和边缘函数现由 Vercel Functions 驱动 - Vercel](https://vercel.com/changelog/edge-middleware-and-edge-functions-are-now-powered-by-vercel-functions)

**原文标题**: [Edge Middleware and Edge Functions are now powered by Vercel Functions - Vercel](https://vercel.com/changelog/edge-middleware-and-edge-functions-are-now-powered-by-vercel-functions)

Vercel 宣布将 Edge 运行时功能整合至统一的 Vercel Functions 基础设施中，并引入新计算模式 Fluid compute，同时调整了定价策略。

- 🌐 Edge Middleware 升级为 Vercel Routing Middleware，支持缓存前全功能运行
- ⚡ Edge Functions 现整合为 Vercel Functions，支持缓存后 Edge Runtime 运行
- 🚫 原 Edge Middleware 和 Edge Functions 已被弃用，由新方案替代
- 🔄 新功能全面支持 Fluid compute 技术，提升性能与成本效益
- 🤖 支持多运行时环境（Node.js 和 Edge）
- 🛠️ 框架驱动部署，自动从支持框架代码部署
- 💰 采用基于 Active CPU 时间的统一计价模式
- ✅ Vercel Routing Middleware 现已全面开放使用

---

### [客户案例 - Resend](https://www.inngest.com/customers/resend?ref=nextjs-weekly-4)

**原文标题**: [Customer story - Resend](https://www.inngest.com/customers/resend?ref=nextjs-weekly-4)

Resend 作为现代电子邮件发送平台，通过 Inngest 的服务器 less 工作流提升了开发体验和可观测性，实现了快速扩展和高效调试。

- 🚀 Resend 通过 Inngest 优化了开发者体验（DX），显著提升了开发速度和本地调试效率。  
- 🔍 Inngest 的可观测性工具帮助 Resend 团队快速定位和修复问题，改善了客户体验。  
- 📧 域名验证是 Resend 的关键流程，Inngest 的可靠性确保了这一流程的稳定运行。  
- ⚡ Resend 团队在几天内就迁移到 Inngest，并立即体验到开发速度的提升和调试的便捷。  
- 🌐 Inngest 的托管解决方案免除了 Resend 管理复杂基础设施的负担，使其更专注于产品价值。  
- 🔄 Resend 计划利用 Inngest 扩展更多高容量批量工作流和未公开的新功能。  
- 💡 Inngest 的可靠性功能为 Resend 在关键流程中提供了信心，支持其快速成长。

---

### [指南：数据安全 | Next.js](https://nextjs.org/docs/app/guides/data-security)

**原文标题**: [Guides: Data Security | Next.js](https://nextjs.org/docs/app/guides/data-security)

Next.js 数据安全指南概述，重点介绍如何在 App Router 中通过 React Server Components 和 Server Actions 实现安全的数据访问和操作。

- 🛡️ **数据获取方法**：推荐三种方式（HTTP APIs、数据访问层、组件级访问），避免混用以简化安全审计。
- 🔒 **零信任模型**：调用现有 API 时需验证身份，如通过 `cookies()` 传递令牌。
- 📦 **数据访问层 (DAL)**：集中管理数据获取逻辑，仅返回最小化 DTO 对象，避免敏感信息泄露。
- ⚠️ **组件级访问风险**：直接查询数据库易暴露私有数据，需手动过滤敏感字段。
- 🔄 **服务端到客户端数据传递**：Server Components 可访问敏感数据，Client Components 需遵循浏览器安全假设。
- 🚫 **污染 API**：使用 React 的 `taintObjectReference` 防止敏感对象意外传递到客户端。
- 🏷️ **server-only 标记**：通过 `server-only` 包确保关键模块仅在服务端执行。
- 🔐 **Server Actions 安全**：内置加密 ID 和死代码消除，但仍需像公开 API 一样进行授权验证。
- ✅ **输入验证**：始终验证客户端输入（如表单、URL 参数），避免依赖未经验证的数据。
- 🔑 **认证与授权**：在执行操作前检查用户权限，如通过 `auth()` 验证登录状态。
- 🔄 **闭包与加密**：自动加密闭包变量，防止敏感数据泄露到客户端。
- 🌐 **允许来源控制**：配置 `allowedOrigins` 防止 CSRF 攻击，确保 Action 仅限同源调用。
- ⚡ **避免渲染副作用**：禁止在渲染期间执行变更操作（如注销、更新数据库），应使用 Server Actions。
- 🔍 **审计重点**：检查 DAL 隔离性、Client Component 的 props 类型、Action 参数验证及中间件安全性。

（注：原文为 Next.js 官方文档的技术指南，此处总结已过滤示例代码和部分冗余说明，保留核心安全实践要点。）

---

### [使用 Cursor 将我的博客从 WordPress 迁移到 Next.js 和 Vercel | Eric Dodds 博客](https://www.ericdodds.com/blog/using-cursor-to-migrate-my-wordpress-blog-to-nextjs-and-vercel)

**原文标题**: [Using Cursor to migrate my blog from WordPress to Next.js and Vercel | Eric Dodds Weblog](https://www.ericdodds.com/blog/using-cursor-to-migrate-my-wordpress-blog-to-nextjs-and-vercel)

概述：作者详细记录了使用 Cursor 工具将其运行了 13 年的 WordPress 博客迁移到 Next.js 和 Vercel 平台的过程，包括内容导出、脚本编写、测试部署及最终清理等步骤，总耗时约 10-15 小时。

- 🏠 作者的个人网站始于 2008 年，最初使用 iWeb 构建，后于 2012 年转向 WordPress 托管。
- 🔄 迁移原因包括对 WordPress.com 高昂费用、安全问题和锁定效应的不满，以及对现代开发工具如 Next.js 和 Vercel 的偏好。
- 🛠️ 使用 Cursor 工具帮助迁移，步骤包括导出 WordPress 内容、分析边缘案例、测试迁移脚本、全面迁移内容和修复部署错误。
- 📝 迁移过程中遇到的主要问题包括插件导致的格式错误、段落间距问题和安全漏洞遗留的垃圾内容。
- ⚙️ 迁移完成后，作者更新了样式、添加了功能（如图片点击放大），并新增了“关于”和“联系”页面。
- 📊 Cursor 在项目中表现出色，作者进行了 110 多次提示，纠正了 15 多次错误，估计总项目时间为 10-15 小时。
- 🔗 提供了迁移过程中使用的 GitHub 仓库、迁移脚本和 Cursor 聊天记录等资源链接。

---

### [如何在 Next.js 中使用 Prisma ORM 和 Prisma Postgres 搭配 Better-Auth | Prisma 文档](https://www.prisma.io/docs/guides/betterauth-nextjs)

**原文标题**: [How to use Prisma ORM and Prisma Postgres with Better-Auth and Next.js | Prisma Documentation](https://www.prisma.io/docs/guides/betterauth-nextjs)

本指南详细介绍了如何将 Better-Auth 集成到 Next.js 应用中，并使用 Prisma ORM 管理 PostgreSQL 数据库中的用户数据。以下是关键步骤和要点的总结：

- 🚀 **概述**：Better-Auth 是一个基于 TypeScript、React 和 Prisma 构建的现代开源认证解决方案，本指南展示了如何将其集成到新的 Next.js 应用中。

- 📋 **先决条件**：需要 Node.js 18+、基本的 Next.js App Router 和 Prisma 知识。

- 🛠️ **项目设置**：使用`npx create-next-app`创建新的 Next.js 应用，选择 TypeScript、ESLint、Tailwind CSS 等默认配置。

- 🗄️ **Prisma 设置**：安装 Prisma 及相关依赖，初始化 Prisma 并配置数据库连接，生成 Prisma Client。

- 🔐 **Better-Auth 集成**：安装 Better-Auth 并生成安全密钥，配置 Prisma 适配器以持久化用户和会话数据。

- 📝 **模型添加**：使用 Better-Auth CLI 自动添加用户、会话、账户和验证模型到 Prisma schema，并迁移数据库。

- 🌐 **API 路由设置**：创建 Next.js API 路由以处理认证请求，如登录、注册和登出。

- 📱 **页面设置**：构建注册、登录和受保护的仪表盘页面，使用 React hooks 管理认证状态和用户导航。

- 🧪 **测试应用**：启动开发服务器，测试注册、登录和登出功能，使用 Prisma Studio 查看数据库中的用户数据。

- 🔜 **后续步骤**：建议添加社交登录、密码重置功能，扩展 Prisma schema，并部署到 Vercel。

- 📚 **延伸阅读**：提供 Better-Auth 和 Prisma 文档链接，以及 Next.js App Router 的相关资源。

---

### [构建并部署一个 SaaS AI 网站构建器 | Next.js 15、React、Inngest、Prisma | 可爱克隆版 - YouTube](https://www.youtube.com/watch?v=xs8mWnbMcmc)

**原文标题**: [Build and Deploy a SaaS AI Website Builder | Next.js 15, React, Inngest, Prisma | Lovable clone - YouTube](https://www.youtube.com/watch?v=xs8mWnbMcmc)

关于 YouTube 的相关信息与链接  
- 📢 关于 - 提供 YouTube 平台的背景与介绍  
- 🗞️ 媒体 - 新闻稿与媒体资源  
- ©️ 版权 - 版权政策与声明  
- 📩 联系我们 - 用户与平台的联系方式  
- 🎨 创作者 - 创作者相关资源与支持  
- 💼 广告 - 广告合作与推广信息  
- 👩💻 开发者 - 开发者工具与 API  
- 📜 条款 - 使用条款与条件  
- 🔒 隐私 - 隐私政策与数据保护  
- ⚖️ 政策与安全 - 平台规范与安全措施  
- 🔧 YouTube 运作方式 - 平台功能与机制解析  
- 🧪 测试新功能 - 新功能的试用与反馈  
- ®️ 版权归属 - 2025 年 Google LLC 所有

---

### [AI 就绪格式化工具，助您更快编写与生成代码 | Ultracite](https://www.ultracite.ai/)

**原文标题**: [The AI-ready formatter that helps you write and generate code faster. | Ultracite](https://www.ultracite.ai/)

Ultracite 是一个基于 Biome 的零配置代码格式化工具，专为团队和 AI 集成设计，提供快速的代码分析和格式化体验。

- ⚡ **极速格式化**：基于 Rust 构建，提供亚秒级的代码分析和处理，无缝集成到工作流程中。  
- 🤝 **兼容性强**：内置对 Husky 和 lint-staged 的支持，适用于所有主流包管理器。  
- 🛠️ **直观易用**：自动修复代码问题并提供清晰的错误报告，便于手动处理。  
- 🔒 **类型安全**：默认启用严格的类型检查，防止不安全的代码模式。  
- 📦 **支持 Monorepo**：统一工具链配置，减少重复代码，保持一致性。  
- 🎯 **高度定制化**：提供严格的预设规则，减少代码风格争议，简化代码审查。  
- 🚀 **零配置设计**：针对 Next.js、React 和 TypeScript 项目优化，开箱即用。  
- 🤖 **AI 友好**：确保团队成员和 AI 模型生成一致的代码风格，减少审查摩擦。  
- 🔧 **可扩展性**：支持自定义规则，适应不同项目需求。  
- 💬 **社区好评**：开发者普遍认为其速度快、易用且能显著提升代码质量。  

安装简单，只需运行 `npx ultracite@latest init` 即可开始使用。

---

### [GitHub - vvo/iron-session: 🛠 JavaScript 安全、无状态、基于 Cookie 的会话库](https://github.com/vvo/iron-session)

**原文标题**: [GitHub - vvo/iron-session: 🛠 Secure, stateless, and cookie-based session library for JavaScript](https://github.com/vvo/iron-session)

iron-session 是一个安全、无状态且基于 cookie 的 JavaScript 会话库，使用签名和加密的 cookie 存储会话数据，无需服务器端存储。

- 🔒 安全无状态会话：使用签名和加密的 cookie 存储会话数据，无需服务器端存储。
- 🍪 基于 cookie：会话数据通过 cookie 在客户端和服务器之间传递，实现无状态会话。
- 🛠 主要功能：提供 `getIronSession`、`session.save`、`session.destroy` 等核心 API。
- ⚙️ 会话配置：需要 `password` 和 `cookieName`，支持密码轮换和多种 cookie 选项。
- 📚 丰富示例：提供多种使用场景的示例，包括 Next.js API 路由和 Express 集成。
- 🔄 密码轮换：支持通过递增键实现密码轮换，增强安全性。
- ❓ 常见问题：解答了关于会话无效化、替代方案和与 JWT 的区别等问题。
- 📜 开源协议：采用 MIT 许可证，已有 4k+ stars 和 258+ forks。

---

### [drizzle-crud - npm](https://www.npmjs.com/package/drizzle-crud)

**原文标题**: [drizzle-crud - npm](https://www.npmjs.com/package/drizzle-crud)

Drizzle CRUD 是一个强大的 TypeScript 包，能够为 Drizzle ORM 模式自动生成 CRUD 操作，包含验证、过滤、分页、软删除和访问控制等功能。目前处于早期预览版本，欢迎反馈。

- 🚀 **自动生成 CRUD 操作**：基于 Drizzle 模式自动生成增删改查功能。
- 🔍 **高级过滤**：支持多种操作符（如 eq, ne, gt, lt, like, in 等）。
- 📄 **内置分页**：可配置的分页功能。
- 🔎 **全文搜索**：支持在指定字段中进行全文搜索。
- 🗑️ **软删除支持**：包含恢复功能。
- 🔐 **访问控制**：基于角色的权限和范围过滤。
- ✅ **标准模式验证**：支持自定义模式。
- 🎣 **生命周期钩子**：用于自定义业务逻辑。
- 📊 **批量操作**：高效处理大量数据。
- 🛡️ **类型安全**：完全支持 TypeScript。

- 🛠️ **集成支持**：计划支持 tRPC、Hono RPC、oRPC 和 Tanstack Table。
- 🚧 **路线图**：支持所有 Drizzle 方言、暴露过滤和分页工具、定义自定义操作等。
- 📦 **安装简单**：支持 npm、yarn 和 pnpm 安装。
- 📝 **快速开始**：提供详细的示例代码，展示如何定义模式和初始化 CRUD 操作。
- 🔄 **核心操作**：包括创建、查找、列表、更新、删除和恢复等。
- ⚙️ **高级功能**：如过滤器操作符、访问控制、生命周期钩子、自定义模式和批量操作。
- 🏗️ **配置选项**：可配置的搜索字段、分页限制、允许的过滤器等。
- 🛡️ **错误处理**：提供描述性错误信息。
- 📋 **要求**：需要 Node.js 16+、TypeScript 4.7+、Drizzle ORM 和 Zod v4。
- 🤝 **贡献**：欢迎贡献，详情请阅读贡献指南。
- 📜 **许可证**：Apache 2.0 许可证。

---

### [发布 v3.0.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.0.0)

Recharts 3.0 版本发布，包含重大更新、新功能和错误修复。

- 🚀 Recharts 3 正式发布，主要代码由 @PavelVanecek 贡献，重写了状态管理并新增 3500 个单元测试。  
- ⚠️ 包含重大变更：移除 `CategoricalChartState` 和 `<Customized />` 的内部状态支持，删除废弃属性。  
- ✨ 新功能：支持自定义组件、Tooltip 和 Legend 的 Portal 渲染、默认启用无障碍访问、极坐标图多轴支持等。  
- 🛠️ 改进与修复：动画优化、TypeScript 改进、饼图点击边框修复、网格背景渲染顺序调整等。  
- 📚 提供 3.0 迁移指南和更新版 Storybook 示例。  
- 👏 社区反响热烈，获得大量点赞、庆祝和爱心表情反馈。

---

### [OAuth 提供商改进](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-27-25&dub_id=4L4DV6KkCPpQfvCa)

**原文标题**: [OAuth Provider Improvements](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-27-25&dub_id=4L4DV6KkCPpQfvCa)

Clerk 宣布对其 OAuth 功能进行了重大扩展，新增多项特性以支持更广泛的应用场景，包括 MCP 服务。

- 🔄 OAuth 令牌现在可以通过 Clerk 的 SDK 验证并即时撤销。
- 📜 支持授权服务器元数据，开箱即用。
- ✅ OAuth 授权流程新增同意屏幕，确保用户明确授权范围。
- 🌐 改进了 CORS 处理，支持浏览器中完成令牌交换的公共客户端。
- 📝 支持 OAuth 客户端的动态客户端注册。
- 🛠 Clerk 的 OAuth 实现满足 MCP 服务作为授权服务的所有要求。
- 📚 提供了详细的 OAuth 指南和实现示例，帮助开发者快速上手。
- 🔍 OAuth 令牌验证已在多数 SDK 中支持，包括 Next.js、JavaScript、Express 等。
- 🚧 部分 SDK（如 Astro、Nuxt、PHP 等）的支持即将推出。
- 🖥 新增 OAuth 同意屏幕，显示请求的应用信息、权限范围及接受/拒绝选项。
- ⚙ 动态客户端注册功能允许通过 API 编程方式创建 OAuth 客户端。
- 🤖 Clerk 的 OAuth 功能现支持构建 MCP 服务，便于 AI 应用安全访问用户数据。
- 🔜 自定义 OAuth 范围功能即将推出，目前正在收集用户反馈。
- 🔄 解决了之前 OAuth 实现中的多项限制，如令牌验证、同意屏幕缺失等。

---

### [Tailwind 是最糟糕的 CSS 形式，但其他选择更糟 | Mux](https://www.mux.com/blog/tailwind-is-the-worst-form-of-css-except-for-all-the-others)

**原文标题**: [Tailwind is the worst form of CSS, except for all the others | Mux](https://www.mux.com/blog/tailwind-is-the-worst-form-of-css-except-for-all-the-others)

Tailwind 是一个具有强烈设计主张的 CSS 工具，开发者对其态度两极分化，但它在团队协作和开发效率上提供了显著优势。

- 🎨 **设计主张鲜明**：Tailwind 提供了一套固定的设计规则，如有限的颜色和字号选择，强制团队遵循统一的设计系统。  
- ⚡ **高效开发**：通过实用类（utility classes）直接在 HTML 中编写样式，减少命名和文件跳转的负担，提升开发速度。  
- 📚 **学习曲线**：需要学习新的语法（如 `items-center` 代替 `align-items: center`），对熟悉传统 CSS 的开发者可能显得冗余。  
- 🏗️ **构建工具依赖**：必须集成到构建流程中，增加了项目配置的复杂度，尤其在多框架环境中。  
- 🚀 **性能优势**：通过复用类名减少 CSS 体积，避免样式表无限增长，同时减少层叠样式（CSS specificity）的困扰。  
- 🛠️ **灵活的逃逸机制**：支持方括号语法（如 `lg:w-[1rem]`）突破预设限制，应对特殊设计需求。  
- 🤝 **团队协作友好**：减少样式命名和设计决策的争议，通过工具约束而非文档规范统一代码风格。  
- 🔄 **迁移成本**：切换到 Tailwind 可能涉及重构现有代码，需权衡长期收益与短期成本。  

最终，是否采用 Tailwind 取决于团队对工具约束的接受度及其与项目规则的匹配程度，但它的结构化设计能有效减少代码审查中的风格分歧。

---

### [容器现已公开测试，提供简单、全球可编程的计算服务](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/?utm_campaign=cf_blog&utm_content=20250624&utm_medium=organic_social&utm_source=twitter/)

**原文标题**: [Containers are available in public beta for simple, global, and programmable compute](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/?utm_campaign=cf_blog&utm_content=20250624&utm_medium=organic_social&utm_source=twitter/)

Cloudflare Containers 现已面向付费用户开放公测，支持与 Workers 无缝集成，提供全球化、可编程的容器化计算能力。

- 🚀 **公测上线**：Cloudflare Containers 进入公测阶段，付费用户可立即使用。  
- 🌍 **全球化部署**：容器与 Workers 深度集成，支持一键部署至全球边缘节点（Region:Earth），无需跨区域配置。  
- 🔧 **灵活开发**：通过 `wrangler` 工具链（如 `wrangler deploy` 和 `wrangler dev`）实现简易开发流程，支持本地 Dockerfile 或远程镜像。  
- ⚡ **按需启动**：容器实例根据请求动态创建，冷启动仅需数秒，支持自定义休眠超时（如 `5m` 无请求后休眠）。  
- 📊 **内置观测性**：提供实时监控、资源用量统计及日志留存（7 天），支持日志外推至第三方服务。  
- 💡 **多样化用例**：适用于边缘媒体处理、多语言后端服务、CLI 工具批处理等场景，例如代码沙箱、FFmpeg 视频转 GIF。  
- 💰 **透明计费**：按实际使用量（CPU/内存/磁盘/出站流量）计费，含 Workers Standard 套餐的免费额度。  
- 🔮 **未来规划**：包括更大实例规格、全局自动扩缩容、容器与 Workers 增强通信（如 `exec` 命令）、与 R2/KV 等服务的深度集成。  
- 🛠️ **快速体验**：提供模板（如 `containers-template`）和示例项目（如沙箱化代码运行），支持一键部署。  

通过 Containers，开发者现可在 Cloudflare 平台上构建更复杂的全栈应用，突破 Workers 原有的语言和资源限制。

---

### [若你使用 shadcn/ui，必看此视频 - YouTube](https://www.youtube.com/watch?v=vHFZFXtjKNE)

**原文标题**: [Watch this if you use shadcn/ui - YouTube](https://www.youtube.com/watch?v=vHFZFXtjKNE)

关于 YouTube 的相关信息与链接  

- 📢 **关于** - 提供 YouTube 平台的背景和基本信息  
- 🗞️ **新闻** - 查看 YouTube 的最新动态和公告  
- ©️ **版权** - 了解 YouTube 的版权政策和相关内容  
- 📩 **联系我们** - 获取与 YouTube 团队联系的途径  
- 🎨 **创作者** - 资源和支持帮助内容创作者  
- 💼 **广告** - 广告投放和商业合作信息  
- 👩💻 **开发者** - 开发者工具和 API 相关资源  
- 📜 **条款** - 使用 YouTube 的服务条款  
- 🔒 **隐私** - 隐私政策和数据保护措施  
- ⚖️ **政策与安全** - 平台规则和安全指南  
- 🔧 **YouTube 运作方式** - 平台功能和技术解析  
- � **测试新功能** - 体验和反馈 YouTube 的新特性  
- ©️ **版权声明** - © 2025 Google LLC 版权所有

---

### [在 ES 模块的顶层使用 await - Matt Smith](https://allthingssmitty.com/2025/06/16/using-await-at-the-top-level-in-es-modules/)

**原文标题**: [
    Using await at the top level in ES modules - Matt Smith
  ](https://allthingssmitty.com/2025/06/16/using-await-at-the-top-level-in-es-modules/)

ES2022 引入了顶层 await，允许在 ES 模块的顶层直接使用 await 关键字，简化异步代码编写，但需注意模块执行顺序和循环依赖问题。

- 🆕 **ES2022 新特性**：顶层 await 允许在 ES 模块的顶层直接使用 await，无需包裹在 async 函数中。  
- 🚀 **使用场景**：  
  - 🌐 启动时获取远程配置（如`fetch('/config.json')`）  
  - 📦 动态导入模块（如`await import('./drivers/postgres.js')`）  
  - ⏳ 等待 WebAssembly 初始化（如`WebAssembly.instantiateStreaming()`）  
- ⚠️ **注意事项**：  
  - 🔄 模块执行会暂停，导入模块需等待顶层 await 完成  
  - 🔗 循环依赖可能导致运行时错误  
  - 🛠️ 仅支持 ES 模块（.mjs 或 type="module"的.js 文件）  
- 🌍 **兼容性**：  
  - ✔️ 现代浏览器和 Node.js v16+ 支持  
  - 🧩 Web Workers 需设置为`type: "module"`  
- 🚫 **避免场景**：  
  - 📚 公共/共享模块（可能阻塞下游依赖）  
  - 🔄 计算密集型逻辑（建议移至 Worker）  
- 💡 **最佳实践**：  
  - ✅ 适合简化初始化逻辑  
  - ⚠️ 大型应用中需谨慎处理循环导入

---

