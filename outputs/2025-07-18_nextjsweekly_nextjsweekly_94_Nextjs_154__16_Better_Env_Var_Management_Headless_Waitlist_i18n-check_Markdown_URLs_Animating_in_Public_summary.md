### [Next.js 15.4 | Next.js](https://nextjs.org/blog/next-15-4)

**原文标题**: [Next.js 15.4 | Next.js](https://nextjs.org/blog/next-15-4)

Next.js 15.4 版本发布，包含性能、稳定性和 Turbopack 兼容性更新，并预告了 Next.js 16 的新功能。

- 🚀 **Turbopack 构建**：`next build --turbopack` 已通过全部 8298 项集成测试，并用于 vercel.com 的生产环境。  
- 🔧 **稳定性改进**：Next.js 和 Turbopack 进行了多项稳定性和性能优化。  
- ⏳ **Next.js 16 预览**：包括缓存组件、优化客户端路由、开发工具调试等新功能。  
- 📦 **升级指南**：提供自动升级 CLI 或手动升级命令，支持新项目创建。  
- 🐞 **问题反馈**：鼓励用户在 GitHub Issues 提交 Turbopack 使用中的问题。  
- 🔍 **实验性功能**：可通过 `canary` 渠道启用新功能，如浏览器日志转发、动态 IO 等。  
- 📝 **贡献者致谢**：感谢超过 3000 名开发者的贡献，特别列出核心团队成员。

---

### [Next.js 15.4 | Next.js](https://nextjs.org/blog/next-15-4#preview-upcoming-features)

**原文标题**: [Next.js 15.4 | Next.js](https://nextjs.org/blog/next-15-4#preview-upcoming-features)

Next.js 15.4 版本带来了性能、稳定性和 Turbopack 兼容性的更新，同时预览了 Next.js 16 的新功能。

- 🚀 **Turbopack 构建**：`next build --turbopack` 已通过所有 8298 项集成测试，并用于 vercel.com 的生产环境。  
- 🔧 **稳定性改进**：Next.js 和 Turbopack 进行了多项稳定性和性能优化。  
- 🔜 **Next.js 16 预览**：包括缓存组件、优化的客户端路由、DevTools 调试等新功能。  
- ⚙️ **升级指南**：提供了自动升级 CLI 或手动升级的步骤，支持新项目创建。  
- 🐞 **问题反馈**：鼓励用户在 GitHub Issues 上报告问题，帮助改进 Turbopack。  
- 📅 **未来计划**：Next.js 16 将引入更多功能，如部署适配器和 Node.js 中间件稳定版。  
- 🛠️ **实验性功能**：开发者可通过 canary 渠道提前体验新功能。  
- 🙏 **贡献者致谢**：感谢超过 3000 名开发者的贡献，特别提及了 Next.js、Turbopack 和文档团队的成员。

---

### [Arcjet - 开发者无忧安全解决方案](https://arcjet.com/?ref=nextjs-weekly)

**原文标题**: [Arcjet - Painless security for developers](https://arcjet.com/?ref=nextjs-weekly)

好的，请提供需要总结的文本内容，我会按照您要求的模板进行整理，包括概述总结和带表情符号的要点列表。  

示例模板：  

概述总结  
- 📌 要点 1  
- 🔍 要点 2  
- 💡 要点 3  

请提供具体文本内容以便我为您生成总结。

---

### [在 Next.js 中添加.md URL 以获取原始 Markdown 内容 - Ben Gubler](https://www.bengubler.com/posts/2025-06-14-raw-markdown-urls-nextjs)

**原文标题**: [Adding .md URLs for Raw Markdown Content in Next.js - Ben Gubler](https://www.bengubler.com/posts/2025-06-14-raw-markdown-urls-nextjs)

概述：本文介绍了如何在 Next.js 博客中添加.md URL 以提供原始 Markdown 内容，灵感来自 Vercel 的文档。通过使用 Next.js 的 rewrites 功能，可以轻松实现这一功能，使得用户可以通过在博客文章 URL 后添加.md 来获取原始 Markdown 内容。

- 🚀 灵感来自 Vercel 的文档，通过添加.md 到博客文章 URL 来获取原始 Markdown 内容。  
- 🛠️ 使用 Next.js 的 rewrites 功能，简化实现过程并提高性能。  
- 📂 通过 Content Collections 库管理内容，确保类型安全和良好的开发体验。  
- 📝 创建示例内容并设置 posts 页面，展示博客文章及其原始 Markdown 链接。  
- 🔄 使用 rewrites 规则将/posts/:slug.md 映射到/api/posts/:slug/raw。  
- 📡 创建 API 路由来处理原始 Markdown 内容的请求，并设置缓存头以减少服务器负载。  
- ✅ 完成设置后，用户可以通过/posts/hello-world 访问渲染后的文章，通过/posts/hello-world.md 访问原始 Markdown。  
- 🤖 这一功能非常适合分享代码示例、调试内容或供他人学习 Markdown 格式。

---

### [i18n-check：验证您的 Next.js 国际化 | Lingual](https://lingual.dev/blog/validating-your-nextjs-internationalization/)

**原文标题**: [i18n-check: Validating your Next.js internationalization | Lingual
](https://lingual.dev/blog/validating-your-nextjs-internationalization/)

i18n-check 工具现已支持 Next.js 应用的国际化验证，可检测未翻译、无效、未定义或未使用的翻译键，并支持多种 i18n 库（如 react-intl、next-intl 等）。通过命令行工具和 CI 集成，开发者能高效管理多语言项目的翻译一致性。

- 🌍 **支持库扩展**：i18n-check 新增对 next-intl 和 next-i18next 的支持，覆盖主流 Next.js i18n 方案。  
- 🔍 **验证功能**：检测未翻译/无效消息、未定义键（代码中存在但缺失于语言文件）及未使用键（语言文件冗余键）。  
- 📂 **灵活配置**：通过命令行参数指定语言文件路径（`--locales`）、源文件（`--source`）及格式（`--format`）。  
- ⚠️ **错误示例**：  
  - 标签不匹配（如源文件含 `<b>` 但翻译文件遗漏）。  
  - 动态参数不同步（如目标文件多出 `tomorrow` 日期变量）。  
- 🛠️ **快速安装**：支持 yarn/npm/pnpm 安装，并集成到 `package.json` 脚本。  
- 📊 **输出示例**：表格形式展示缺失键、无效键、未使用键及未定义键的具体位置。  
- 🔄 **CI 集成**：提供 GitHub Workflow 示例，实现在代码提交/PR 时自动检查。  
- 🔗 **资源链接**：工具文档及相关 i18n 库（react-intl、next-i18next 等）直达入口。  
- 🚀 **未来计划**：预告即将推出的翻译管理系统（含分支管理与 CLI 集成）。

---

### [如何在 5 分钟内将 Stripe 添加到 Next.js 💰 - Tom Dekan](https://tomdekan.com/articles/stripe-with-nextjs)

**原文标题**: [How to add Stripe to Next.js in 5 minutes 💰 - Tom Dekan](https://tomdekan.com/articles/stripe-with-nextjs)

在 5 分钟内将 Stripe 集成到 Next.js 应用的简明指南。

- 🚀 **快速构建**：5 分钟内完成 Next.js 应用与 Stripe 的集成，实现用户购买功能。
- 💳 **使用 Stripe Checkout**：通过 Stripe Checkout 处理支付流程。
- 📊 **Stripe Dashboard**：创建产品和价格。
- 🔌 **Stripe API**：创建结账会话。
- 📦 **安装依赖**：使用`pnpm add stripe @stripe/stripe-js`安装 Stripe 相关包。
- 🔑 **环境变量**：配置`.env`文件，包含 Stripe 密钥和应用基础 URL。
- 🌐 **API 路由**：创建`/api/checkout`路由处理结账会话。
- 🛒 **客户端助手**：使用`getStripe.ts`加载 Stripe.js。
- 🔄 **重定向按钮**：实现支付按钮，处理重定向逻辑。
- 📡 **Webhook 端点**：设置`/api/webhook`接收支付成功通知。
- 🧪 **本地测试**：使用`stripe listen`命令测试 Webhook。
- 🛍️ **创建产品**：在 Stripe Dashboard 中添加产品并获取价格 ID。
- 🏃 **本地运行**：使用`pnpm dev`启动应用，测试支付流程。
- 🚀 **部署**：使用 Vercel 部署，配置 Stripe 环境变量。
- ❌ **常见错误**：包括密钥不匹配、环境变量缺失和路径错误等。

---

### [这个新工具让我毫不犹豫删掉了 ESLint - YouTube](https://www.youtube.com/watch?v=b_F4LaycQcE)

**原文标题**: [This New Tool Made Me Delete ESLint Without Regret - YouTube](https://www.youtube.com/watch?v=b_F4LaycQcE)

这是一个关于 Google LLC 旗下平台（可能是 YouTube）的相关信息和服务的简要列表。  

- 📜 簡介  
- 🗞️ 新聞中心  
- ©️ 版權  
- 📞 聯絡我們  
- 🎨 創作者  
- 📢 刊登廣告  
- 💻 開發人員  
- 📑 條款  
- 🔒 私隱  
- ⚖️ 政策及安全  
- ▶️ YouTube 的運作方式  
- 🧪 測試新功能  
- ⏳ © 2025 Google LLC

---

### [未找到标题](https://x.com/asidorenko_/status/1945918169576521925)

**原文标题**: [No title found](https://x.com/asidorenko_/status/1945918169576521925)

当前页面提示 JavaScript 未启用或浏览器不受支持，建议调整设置或更换浏览器以正常使用 x.com。

- 🚫 JavaScript 未启用：检测到浏览器中 JavaScript 被禁用，需启用或更换支持浏览器。  
- 🌐 支持浏览器：可查看帮助中心获取支持的浏览器列表。  
- 🔧 其他问题：隐私相关扩展可能导致问题，建议禁用后重试。  
- ℹ️ 相关链接：提供帮助中心、服务条款、隐私政策等页面入口。  
- 🔄 操作建议：遇到问题时，可尝试点击“重试”按钮。  
- ©️ 版权信息：页面底部显示© 2025 X Corp.版权声明。

---

### [未找到标题](https://x.com/timneutkens/status/1945831596940054918)

**原文标题**: [No title found](https://x.com/timneutkens/status/1945831596940054918)

当前页面提示 JavaScript 未启用或浏览器不受支持，导致无法正常使用 x.com 的功能。

- 🚫 JavaScript 未启用：检测到浏览器中 JavaScript 被禁用，需启用或更换支持浏览器。  
- 🌐 浏览器支持：可查看帮助中心获取支持的浏览器列表。  
- 🔧 尝试解决：建议禁用隐私相关扩展后重试。  
- 📜 相关链接：提供帮助中心、服务条款、隐私政策等文档入口。  
- ⚠️ 错误提示：页面加载异常，但鼓励用户再次尝试。  
- ©️ 版权信息：页脚标注 2025 年 X 公司版权声明。

---

### [Next.js | 变量锁](https://varlock.dev/integrations/nextjs/)

**原文标题**: [Next.js | varlock](https://varlock.dev/integrations/nextjs/)

Next.js 环境变量工具 Varlock 提供了比默认工具更强大的功能，包括验证、类型安全、多环境管理等。

- 🚀 Varlock 为 Next.js 提供环境变量增强功能，包括验证、类型安全、多环境管理等  
- 📦 使用 `@varlock/nextjs-integration` 包替换默认的 `@next/env` 以集成 Varlock  
- ⚠️ 目前不支持 Turbopack，无法使用额外的安全功能  
- ⚙️ 要求 Node.js v22+ 和 Next.js v14+  
- 📥 安装命令：`npm install @varlock/nextjs-integration varlock`  
- 🔧 运行 `varlock init` 设置 `.env.schema` 文件  
- 🔄 覆盖 `@next/env` 以使用 Varlock 的替代包  
- 🔌 在 `next.config.*` 中启用 `varlockNextConfigPlugin` 以获得完整功能  
- 🔒 推荐使用 `ENV` 对象而非 `process.env` 以获得更好的类型安全和开发体验  
- 📝 启用 `@generateTypes` 以支持类型安全和 IntelliSense  
- 🌐 支持多环境管理，如 `.env.development`、`.env.production` 等  
- 🏷️ 使用 `@envFlag` 设置自定义环境标志  
- 🔧 针对 Vercel 和 Cloudflare 等平台提供环境变量配置示例  
- 🔐 通过 `@defaultSensitive` 控制敏感变量的公开性  
- 🛠️ 独立模式需手动复制 `.env` 文件并使用 `varlock run` 启动  
- ❌ 常见问题包括未正确设置覆盖、Node 版本过低或类型生成问题  
- 📚 提供根装饰器、项目装饰器和函数参考文档

---

### [宇宙界面](https://www.cosmic-ui.com/)

**原文标题**: [Cosmic UI](https://www.cosmic-ui.com/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结，简明扼要地概括核心内容。  

- 🌟 第一个关键点  
- 📊 第二个关键点  
- 🔍 第三个关键点  

请将需要总结的文本粘贴进来，我会立即处理！

---

### [GitHub - ashokasec/headless-waitlist: 无头候补名单系统，支持电子邮件验证与速率限制](https://github.com/ashokasec/headless-waitlist)

**原文标题**: [GitHub - ashokasec/headless-waitlist: Headless waitlist system with email validation and rate limiting.](https://github.com/ashokasec/headless-waitlist)

一个基于 Next.js 15、TypeScript 和 PostgreSQL 的无头候补名单系统，具有电子邮件验证和速率限制功能。

- 🚀 **功能概述**：现代化的候补名单系统，适合独立开发者和初创公司收集早期用户兴趣。  
- 🔒 **内置安全**：Arcjet 集成提供机器人防护、速率限制和电子邮件验证。  
- 📧 **自动化邮件**：Resend 集成用于即时发送确认邮件。  
- ✅ **邮件验证（可选）**：支持双重确认的邮件验证链接。  
- 🗄️ **持久存储**：使用 Drizzle ORM 的 PostgreSQL 数据库进行可靠数据存储。  

- 💻 **技术栈**：  
  - 前端：Next.js 15、TypeScript、shadcn/ui  
  - 后端：PostgreSQL、Drizzle ORM、Arcjet、Resend  
  - 开发工具：Biome、pnpm  

- 🔄 **工作流程**：  
  - 用户提交邮件地址  
  - Arcjet 进行安全检查和速率限制  
  - 邮件存储到 PostgreSQL 数据库  
  - Resend 发送欢迎邮件  
  - 本地存储防止重复提交  

- 🛠️ **快速设置**：  
  - 克隆仓库并安装依赖  
  - 配置环境变量  
  - 启动数据库（推荐使用 Docker）  
  - 运行开发服务器  

- 📂 **关键文件**：  
  - `waitlist-ui.tsx`：候补名单组件  
  - `submit-email/route.ts`：邮件提交 API  
  - `email-schema.ts`：数据库模式  
  - `emails.ts`：邮件模板  

- ✏️ **自定义**：  
  - 修改样式、邮件模板、SEO 设置等  
  - 搜索代码中的“TODO:”进行快速设置  

- 🤝 **贡献**：欢迎提交 Pull Request  
- 📜 **许可证**：MIT License

---

### [代理界面工具包](https://agents-ui.github.io/agents-kit/)

**原文标题**: [agents-ui-kit](https://agents-ui.github.io/agents-kit/)

AI 应用的核心构建模块，提供高质量、易用且可定制的 AI 界面组件。

- 🏗️ AI 应用的核心构建模块  
- 🎨 高质量、易访问且可定制的 AI 界面组件  
- 🚀 快速开始指南  
- ⭐ GitHub 上点赞支持  
- 🔍 支持搜索功能  
- 💬 兼容多种 AI 模型（如 ChatGPT、Mistral AI、DeepSeek）  
- 📝 示例代码展示 PromptInput 组件的使用（包含文本输入框和操作按钮）  
- 📤 支持文件上传功能  
- ✉️ 内置发送按钮操作

---

### [Sevalla® - 云应用平台。数分钟部署应用。](https://sevalla.com/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

**原文标题**: [SevallaÂ® - Cloud Application Platform. Deploy Apps in Minutes.](https://sevalla.com/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

Sevalla 是一个集应用、存储、数据库和静态网站托管于一体的直观平台，旨在简化开发流程，提供快速、可靠且安全的部署服务。

- 🚀 **一站式部署**：Sevalla 提供从概念到部署的全套服务，无需担心基础设施，只需专注于编码。  
- 🌐 **全球覆盖**：支持在 25 个数据中心部署，利用 260 多个 PoP 服务器加速内容分发，降低延迟。  
- 🛠️ **多样化服务**：包括应用托管、对象存储、数据库托管和静态网站托管，满足不同需求。  
- 🔄 **灵活兼容**：支持任意技术栈，提供公共/私有 Git 仓库和 Dockerfile 部署，无限制创新。  
- 💡 **简化运维**：无需担心 DevOps，Sevalla 负责底层管理，让开发者专注于构建。  
- 💰 **透明定价**：按使用量付费，无计划限制、无功能门槛，资源无限扩展。  
- 👥 **无限协作**：支持无限用户和并行构建，团队协作无成本压力。  
- 🚫 **无隐藏费用**：免费内网流量、无数据库使用限制，真正实现无忧开发。  
- ⚡ **快速启动**：几分钟内即可部署应用、数据库或静态网站，立即体验。

---

### [公共场合动画创作](https://emilkowal.ski/ui/animating-in-public)

**原文标题**: [Animating in Public](https://emilkowal.ski/ui/animating-in-public)

Emil Kowalski 从 Vue.js 转学 React，通过公开分享作品获得职业突破，最终加入知名公司并创建开源项目。

- 🚀 Emil 最初从事 Vue.js 开发，但渴望转向 React，通过自学和实践提升技能。  
- 📱 他公开分享了首个项目 ui-snippets.dev，但首次 React 工作申请仍遭拒绝。  
- 💡 转变策略后，他在 Twitter 分享作品（如 Vercel 标签组件复刻），获得广泛关注和合作邀约。  
- 👨💻 由此加入初创公司 Compound，参与 Command Menu 等项目，并萌生 Sonner 的创意。  
- ✉️ 因持续分享作品，收到 Vercel CEO 邀请，2022 年底加入其设计团队，参与多个重要项目。  
- 🌟 在 Vercel 期间，他建立了信心并开源了 Sonner 和 Vaul 两个组件。  
- 📢 Emil 强调公开分享的价值：它带来了 Compound、Vercel 等工作机会，甚至促成课程发布。  
- 🔄 文末鼓励读者尝试分享作品，可能改变人生轨迹。  
- 🙏 特别感谢 Julian 对文章的反馈。

---

### [为什么可视化网站构建工具没有流行起来 - YouTube](https://www.youtube.com/watch?v=BK_71QjkZmA)

**原文标题**: [Why visual website builders didn't take off - YouTube](https://www.youtube.com/watch?v=BK_71QjkZmA)

这是一个关于 Google LLC 旗下平台（可能是 YouTube）的相关信息和版权声明的页面。

- 📜 簡介 - 页面提供基本信息介绍  
- 🗞️ 新聞中心 - 提供新闻相关内容  
- ©️ 版權 - 版权声明信息  
- 📞 聯絡我們 - 联系方式  
- 🎨 創作者 - 与创作者相关的内容  
- 📢 刊登廣告 - 广告投放信息  
- 💻 開發人員 - 开发者相关资源  
- 📑 條款 - 使用条款说明  
- 🔒 私隱 - 隐私政策  
- ⚖️ 政策及安全 - 政策与安全信息  
- ▶️ YouTube 的運作方式 - YouTube 平台运作说明  
- 🧪 測試新功能 - 新功能测试信息  
- 🕰 © 2025 Google LLC - 版权年份和公司声明

---

### [React 依然让人抓狂却无人提及](https://mbrizic.com/blog/react-is-insane/)

**原文标题**: [React Still Feels Insane And No One Is Talking About It](https://mbrizic.com/blog/react-is-insane/)

概述总结  
作者回顾了自己从 Angular 到 React 的开发经历，认为 React 虽然初期看似简单，但随着项目复杂度增加，其架构和状态管理变得混乱且难以维护。文章批评了 React Hooks（尤其是 useEffect）的设计，认为其导致代码难以理解和维护。作者还指出，许多 Web 应用本不需要单页面应用（SPA）的复杂度，而应优先考虑服务器端渲染（SSR）的简洁性。最后，作者建议减少交互功能的复杂度，仅在必要时使用 React 等前端框架。

- 🚀 **React 的崛起与问题**  
  React 初期因简洁性受欢迎，但随着项目复杂度增加，其状态管理和架构问题凸显，导致代码难以维护。

- 🔄 **状态管理的混乱**  
  React 的“自上而下”状态传递和 Hooks 的“全局变量”式状态管理导致代码逻辑分散，难以追踪。

- 🤯 **useEffect 的滥用**  
  `useEffect`被用作组件初始化工具，导致副作用与状态管理混杂，代码执行顺序难以理解。

- 📚 **过度复杂的模式**  
  常见的 React 设计模式（如 CSS-in-JS）增加了不必要的复杂度，而开发者却习以为常。

- 🌍 **SPA 的过度使用**  
  许多 Web 应用本不需要 SPA 的复杂度，服务器端渲染（SSR）能提供更简单、高效的解决方案。

- 🛠️ **简化交互的建议**  
  减少页面上的交互功能（按钮等），仅在必要处使用 React 等框架，以降低复杂度。

- 🔄 **服务器端渲染的优势**  
  SSR 能将页面简化为“纯函数”，避免前端状态管理的复杂性，适合大多数场景。

- 🏝️ **“交互岛屿”概念**  
  仅在必要部分嵌入 React 等框架，保持整体页面的简洁性，避免过度设计。  

（作者最后附上了 HackerNews 和 Reddit 的讨论链接，并推荐订阅其 newsletter。）

---

### [如何创建 NPM 包 | 完全掌握 TypeScript](https://www.totaltypescript.com/how-to-create-an-npm-package)

**原文标题**: [How To Create An NPM Package | Total TypeScript](https://www.totaltypescript.com/how-to-create-an-npm-package)

本指南详细介绍了如何从零开始创建一个生产就绪的 npm 包，涵盖版本控制、代码编写、格式化、测试、CI 流程、版本管理和发布等全流程步骤。

- 🛠️ 初始化 Git 仓库，设置.gitignore，并推送到 GitHub
- 📦 创建 package.json 文件，配置基本信息、许可证和 README
- 🏗️ 安装 TypeScript，配置 tsconfig.json，设置构建脚本
- ✨ 集成 Prettier 进行代码格式化，并添加格式检查和格式化脚本
- 🧪 使用 Vitest 进行测试，配置测试脚本和开发模式
- 🔄 设置 GitHub Actions 工作流实现 CI 自动化
- 🚀 使用 Changesets 管理版本和发布流程
- 📌 包含详细的步骤说明和配置示例
- 🔗 提供演示仓库和视频教程参考

---

