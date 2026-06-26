### [Next.js 16.3：即时导航 | Next.js](https://nextjs.org/blog/next-16-3-instant-navigations)

**原文标题**: [Next.js 16.3: Instant Navigations | Next.js](https://nextjs.org/blog/next-16-3-instant-navigations)

### 概述
Next.js 16.3 预览版引入了“即时导航”功能，通过流式渲染、缓存和部分预取等技术，使服务器驱动应用获得类似单页应用的即时响应体验，同时保留服务器端渲染的优势。

- 🚀 **即时导航**：通过流式渲染（`<Suspense>`）或缓存（`'use cache'`），用户点击链接后立即看到页面壳或加载状态，无需等待网络往返。
- ⚙️ **可选阻塞**：通过 `export const instant = false` 可让特定路由延迟导航，适用于博客等不需要即时加载的场景。
- 📦 **部分预取**：启用 `partialPrefetching` 后，Next.js 按路由预取可复用的页面壳，而非每个链接单独请求，减少网络开销。
- 🔍 **开发工具**：新增导航检查器和即时洞察面板，帮助开发者识别和调试非即时导航的路由。
- 🧪 **测试支持**：提供 `instant()` 测试辅助函数，用于在 Playwright 中验证导航是否即时显示关键内容。
- 🏗️ **配置标志**：通过 `cacheComponents: true` 和 `partialPrefetching: true` 启用新行为，未来将成为默认设置。
- 📉 **性能提升**：在 v0 等实际应用中，导航时间显著缩短，从点击到路由切换的延迟接近零。
- 🗓️ **预览版**：可通过 `npm install next@preview` 安装，稳定版预计数周后发布。

---

### [Aurora Scharff 所著：今日 Next.js 中 RSC 的能力](https://gitnation.com/contents/what-rscs-can-do-in-nextjs-today)

**原文标题**: [What RSCs Can Do in Next.js Today by Aurora Scharff](https://gitnation.com/contents/what-rscs-can-do-in-nextjs-today)

本文介绍了 React Server Components (RSCs) 在 Next.js 中的实践、优势及未来趋势，并提供了相关会议、演讲和工作坊资源。

- 🎤 **React Summit 2026 演讲**：Aurora Scharff 展示如何用 RSCs 在 Next.js 中构建即时反馈、流式 UI、数据同步和强 Core Web Vitals 的应用。
- 📅 **即将举行的会议**：AI Coding Summit London（2026 年 7 月 6-7 日）等多项活动，聚焦 AI 与软件开发。
- 🚀 **RSCs 核心优势**：减少客户端代码、简化数据获取、提升性能，并支持流式渲染和缓存优化。
- 🔧 **实践指南**：多场工作坊涵盖 RSCs 基础、迁移策略、SSR 集成及部署模式，如使用 Next.js 和 React Query。
- 📚 **专家见解**：Mark Dalgleish、Kent C. Dodds 等分享 RSCs 的序列化、流式处理及生产环境经验。
- 💡 **挑战与未来**：RSCs 仍处于实验阶段，但 Next.js 是入门首选，未来将整合客户端状态管理库。

---

### [Arcjet - 运行在代码内部的应用安全](https://arcjet.com/?utm_source=nextjsweekly&utm_medium=email&utm_campaign=2026-06-26)

**原文标题**: [Arcjet - Application security that runs inside your code](https://arcjet.com/?utm_source=nextjsweekly&utm_medium=email&utm_campaign=2026-06-26)

概述总结  
- 📰 本文主要讨论了人工智能在医疗领域的应用现状与未来潜力。  
- 🏥 当前 AI 技术已用于辅助诊断、药物研发和个性化治疗方案设计。  
- ⚠️ 数据隐私、算法偏见和监管不足是主要挑战。  
- 🔬 未来 AI 有望通过深度学习提升疾病预测准确性，并降低医疗成本。  
- 🤝 跨学科合作与伦理规范是推动 AI 医疗落地的关键。

---

### [Next.js 16.3 变得不错（如果你在意的话）- YouTube](https://www.youtube.com/watch?v=cSDKkD_6kCo)

**原文标题**: [Next.js 16.3 got good (if you care) - YouTube](https://www.youtube.com/watch?v=cSDKkD_6kCo)

本頁面列出 YouTube 平台的主要功能、政策及聯絡資訊，涵蓋版權、隱私、廣告及開發者資源等面向。

- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明內容使用與版權保護相關規範
- 📞 聯絡我們：提供用戶與創作者聯繫 YouTube 的管道
- 🎬 創作者：支援內容創作者的資源與工具
- 📢 刊登廣告：介紹廣告投放與商業合作選項
- 👨‍💻 開發人員：提供 API 與開發者相關技術文件
- 📜 條款：明確用戶使用 YouTube 的服務條款
- 🔒 私隱：說明個人資料收集與使用政策
- 🛡️ 政策及安全：規範內容審查與平台安全機制
- ⚙️ YouTube 的運作方式：解釋推薦系統與平台運作原理
- 🧪 測試新功能：介紹正在測試中的新功能
- ©️ 2026 Google LLC：顯示版權歸屬與年份

---

### [迁移到 Next.js 应用路由器后，我们如何将响应速度提升 80% - DEV 社区](https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da)

**原文标题**: [How We Cut Slow Responses by 80% Migrating to Next.js App Router - DEV Community](https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da)

Subito 团队通过迁移到 Next.js App Router，成功将慢响应减少了约 80%，同时提升了页面加载速度和 SEO 表现。

- 🎯 **明确目标**：迁移旨在实现更快的页面加载（利用 React 服务器组件和 HTML 流式传输）和更好的 SEO（提升页面速度评分）。
- 🔄 **渐进式迁移**：采用增量方式，在现有 Pages Router 旁逐步添加 App Router 树，避免冻结产品开发，确保新旧页面共享同一客户端组件。
- 🚦 **自定义 Express 服务器**：通过 Express 层实现流量路由控制，支持渐进式推出（如按类别逐步切换），并解决框架限制（如 HTTP 410 状态码）。
- ⚡ **HTML 流式传输挑战**：需配置 Nginx（关闭缓冲）和 Akamai CDN（自定义行为启用分块传输），确保流式传输端到端工作，缓存命中时返回完整 HTML。
- 📊 **SEO 安全推出**：分两阶段进行——先迁移到 App Router（关闭流式传输），再逐步启用流式传输，每个类别监控约两周确保无负面影响。
- 🛠️ **低投入高回报**：主要由一名开发者在日常功能开发间隙完成，借助 Claude Code 加速规划与实现，无需专职团队。
- 📈 **显著成果**：响应时间方面，超过 250ms 的响应比例从 25-40% 降至接近零；SEO 方面，各类别快速 URL（<500ms）比例显著提升，视频游戏类别提升近 30%。
- 💡 **关键经验**：并行路由允许无缝迁移；自定义服务器层提供灵活控制；HTML 流式传输需要全链路配置；端到端和视觉回归测试及早发现回归问题。

---

### [2026 年 React 库指南 - Robin Wieruch](https://www.robinwieruch.de/react-libraries/)

**原文标题**: [React Libraries for 2026 - Robin Wieruch](https://www.robinwieruch.de/react-libraries/)

本文概述了 2026 年 React 生态系统中构建大型应用所需的核心库与工具，从项目初始化到部署、测试、移动开发等各方面提供了推荐。

- 🚀 **项目启动**: 推荐 Vite 用于客户端渲染，Next.js 或 TanStack Start 用于全栈应用，Astro 用于静态网站。
- 📦 **包管理器**: npm 最普及，pnpm 性能更佳，Bun 作为新兴全能工具链值得关注。
- 🗄️ **状态管理**: 本地状态用 useState/useReducer，全局状态推荐 Zustand，服务器状态用 TanStack Query。
- 🌐 **数据获取**: 客户端推荐 TanStack Query，服务端用 React Server Components，tRPC 实现端到端类型安全。
- 🧭 **路由**: 服务端路由用 Next.js 或 React Router 框架模式，客户端路由推荐 React Router 或 TanStack Router。
- 🎨 **CSS 样式**: 推荐 Tailwind CSS（实用优先），CSS Modules（模块化），或 PandaCSS/vanilla-extract（零运行时 CSS-in-JS）。
- 🧩 **UI 库**: 预构建组件选 Mantine 或 Hero UI，无头 UI 推荐 shadcn/ui 或 Radix。
- 🎬 **动画**: 标准选择是 Motion（前 Framer Motion），GSAP 适合复杂时间线动画。
- 📊 **图表**: Recharts（推荐，shadcn/ui 图表基础），Tremor（SaaS 仪表盘），visx（低层 D3）。
- 📝 **表单**: React Hook Form 最流行，TanStack Form 类型安全，Conform 适合服务端表单。
- 🛠️ **代码结构**: 新项目推荐 oxlint + oxfmt，稳定选择 Biome v2，传统选 ESLint + Prettier。
- 🔐 **认证**: 自托管选 Better Auth，托管服务选 Clerk 或 AuthKit，已有后端用 Supabase Auth。
- 🖥️ **后端**: 全栈框架优先，否则选 Hono 或 Express，tRPC 实现类型安全。
- 🗃️ **数据库**: Drizzle ORM（服务器无状态首选），Prisma（成熟生态），数据库选 Supabase 或 Convex。
- ☁️ **托管**: Vercel（Next.js 最佳），Netlify（友好定价），Coolify（开源 PaaS），Cloudflare（免费带宽）。
- 🧪 **测试**: 单元/集成用 Vitest + React Testing Library，E2E 测试用 Playwright。
- 📅 **时间处理**: date-fns 或 Day.js，Temporal API（ES2026 原生）是未来方向。
- 📧 **邮件**: react-email 创建邮件，Resend 作为服务商。
- 📱 **移动开发**: React Native + Expo，Tamagui 统一 Web 和移动组件。
- 🕶️ **VR/AR**: react-three-fiber + @react-three/xr。
- 🎨 **设计原型**: v0 by Vercel 生成 React 组件，Figma 用于设计交接。
- 📖 **组件文档**: Storybook 最全面，Ladle 更轻量。

---

### [React 应用中的组件通信模式 — Neciu Dan](https://neciudan.dev/component-communication-patterns-in-react)

**原文标题**: [Component Communication Patterns in React Applications — Neciu Dan](https://neciudan.dev/component-communication-patterns-in-react)

以下是您提供的文章内容摘要：

React 组件通信有多种模式，选择取决于组件间的距离和共享值的类型。

- 📝 **Props 和回调**：父子组件间数据向下流动（props），事件向上传递（回调）。适用于近距离组件，通过“状态提升”实现兄弟组件共享。
- 🧩 **组合（Composition）**：通过将渲染的元素作为 children 传递，避免“属性钻取”（prop drilling），让数据直接到达需要它的组件。
- 📍 **状态就近放置（Colocation）**：将状态放在最接近使用它的组件中，避免不必要的提升和重渲染，优化性能。
- 📞 **命令式调用（Imperative Calls）**：使用 `ref` 和 `useImperativeHandle` 让父组件直接调用子组件的方法（如播放视频、聚焦输入框）。
- 🌐 **Context**：适用于跨多层组件且变化不频繁的全局值（如主题、用户）。注意：Context 值变化会导致所有消费者重渲染，需谨慎使用，避免性能陷阱。
- 🗄️ **全局状态库（Global Store）**：如 Zustand，适用于频繁更新且不同组件需要订阅不同切片的状态。通过选择器（selector）实现精准重渲染，注意避免返回新对象导致无限重渲染。
- 🖥️ **服务端状态（Server State）**：使用 TanStack Query 管理来自服务器的数据。它处理缓存、加载、错误和自动重新获取，多个组件共享同一查询键时只发一次请求。
- 🔗 **URL 状态（URL State）**：将描述当前视图的状态（如筛选、页码）放入 URL，实现可分享、可刷新、支持浏览器前进后退。推荐使用 `nuqs` 库。
- 📡 **事件驱动通信（Event-driven Communication）**：使用发布 - 订阅模式（如 `EventTarget` 或自定义事件总线）处理“一次性事件”（如 Toast 通知）。发送者和接收者完全解耦，但调试困难，应作为最后手段。
- ✅ **选择指南**：始终优先使用最接近问题的工具。从 props 和回调开始，必要时使用 Context 和 TanStack Query，仅在特定问题确实需要时才引入全局状态库或事件总线。

---

### [GitHub - aidenybai/cnfast: `cn` 的快速替代方案](https://github.com/aidenybai/cnfast)

**原文标题**: [GitHub - aidenybai/cnfast: Fast drop in replacement for `cn` · GitHub](https://github.com/aidenybai/cnfast)

cnfast 是一个高性能的 `cn` 函数替代品，平均比 tailwind-merge 快 3.8 倍，最高可达 7 倍，输出字节完全相同。

- ⚡ **极速性能**：在 V8 引擎上，缓存重渲染场景下速度提升 4.3 倍（2,025 ops/s → 8,709 ops/s），冷启动合并引擎提升 3.8 倍
- 🔄 **无缝迁移**：通过 `npx cnfast migrate` 一键替换 clsx、classnames 或 tailwind-merge 项目，无需修改代码
- 🎯 **shadcn/ui 集成**：使用 `npx shadcn@latest add aidenybai/cnfast/cn` 直接替换 cn 工具函数，自动重写 lib/utils.ts
- 🏷️ **标签模板支持**：支持 `cn` 标签模板语法，在稳定调用点上比 tailwind-merge 快 4.3 倍，通过调用点身份缓存避免重复计算
- 📦 **轻量体积**：gzip 后仅 9.43 KB（基线为 8.45 KB），在 113,291 个真实调用组中零输出差异
- 🛠️ **完整导出**：同时导出 clsx、twMerge 和 twJoin 函数，兼容现有代码习惯
- 📊 **广泛适用**：在数据网格、虚拟表格、实时仪表盘等高频率重渲染场景中，性能优势尤为明显，能有效控制帧预算

---

### [GitHub - ixartz/SaaS-Boilerplate：🚀🎉📚 基于 Next.js + Tailwind CSS + Shadcn UI + TypeScript 构建的 SaaS 样板。⚡️全栈 React 应用，包含认证、多租户、角色与权限、国际化、落地页、数据库、日志、测试](https://github.com/ixartz/SaaS-Boilerplate)

**原文标题**: [GitHub - ixartz/SaaS-Boilerplate: 🚀🎉📚 SaaS Boilerplate built with Next.js + Tailwind CSS + Shadcn UI + TypeScript. ⚡️ Full-stack React application with Auth, Multi-tenancy, Roles & Permissions, i18n, Landing Page, DB, Logging, Testing · GitHub](https://github.com/ixartz/SaaS-Boilerplate)

这是一个基于 Next.js 构建的免费开源 SaaS 样板项目，集成了多种现代开发工具和功能，帮助开发者快速启动和部署 SaaS 应用。

- 🚀 基于 Next.js 和 Tailwind CSS 构建，支持 App Router、TypeScript 和 React 19
- 🔒 集成 Clerk 认证，支持密码登录、Magic Links、多因素认证和多种社交登录
- 👥 多租户与团队管理，支持创建、切换组织及邀请成员
- 📝 基于角色的权限控制（RBAC），灵活管理用户访问
- 🌐 国际化（i18n）支持，集成 next-intl 和 Crowdin 翻译管理
- 🗄️ 使用 Drizzle ORM 进行类型安全的数据库操作，兼容 PostgreSQL、SQLite 和 MySQL
- 🧪 完整的测试体系，包括 Vitest 单元测试和 Playwright 端到端测试
- 📦 内置错误监控（Sentry）、日志管理（Better Stack）和性能监控（Checkly）
- 🎨 集成 Shadcn UI 组件库，支持 Storybook 进行 UI 开发
- ⚙️ 开发者体验优先：ESLint、Prettier、Lefthook、Commitlint 等工具链
- 🎁 自动生成变更日志（Semantic Release），支持语义化版本控制
- 💡 提供免费版、Pro 版和 Max 版，满足不同需求，Pro 版额外支持 Stripe 支付和暗黑模式

---

### [GitHub - vercel-labs/eve-chat模板 · GitHub](https://github.com/vercel-labs/eve-chat-template)

**原文标题**: [GitHub - vercel-labs/eve-chat-template · GitHub](https://github.com/vercel-labs/eve-chat-template)

该模板是一个基于 Next.js 的持久化聊天应用，集成了 eve 智能体、shadcn/ui、Tailwind CSS、Better Auth、Drizzle、Neon 和 Upstash Redis 等技术栈。

- 🚀 **快速部署**：支持一键部署到 Vercel 或本地脚本安装，自动配置数据库、认证和存储服务。
- 🔧 **技术栈**：使用 Next.js、Tailwind CSS、shadcn/ui 构建前端，Drizzle+Neon 管理数据，Upstash Redis 实现速率限制。
- 🔐 **认证系统**：集成 Better Auth 和 Vercel 登录，支持 OAuth 认证流程。
- 💬 **聊天功能**：提供持久化聊天历史、侧边栏管理、消息删除和新聊天创建功能。
- 🤖 **智能体集成**：通过 eve 智能体实现文本聊天，支持流式传输、会话状态保存和断点续聊。
- 🔗 **第三方连接**：支持 Slack、Notion、Linear、Sentry 等 Vercel Connect 集成。
- 📝 **Markdown 渲染**：使用 Streamdown 渲染助手消息和推理过程的 Markdown 内容。
- 📦 **数据库管理**：使用 Drizzle ORM 管理 Neon 数据库，支持迁移和模式定义。
- ⚡ **性能优化**：使用 Upstash Redis 进行速率限制，确保认证聊天的稳定性。

---

### [@stylexjs/atoms | StyleX](https://stylexjs.com/docs/api/javascript/atoms)

**原文标题**: [@stylexjs/atoms | StyleX](https://stylexjs.com/docs/api/javascript/atoms)

以下是对所提供内容的概述和要点总结：

StyleX 是一个用于编写内联原子样式的工具，通过编译时优化提升性能，支持静态和动态样式，并与多种框架集成。

- 📘 **概述**：StyleX 提供编译时原子样式，通过 `@stylexjs/atoms` 实现静态和动态样式，支持多种框架（如 Next.js、React、Vite 等），并包含丰富的 API 和工具（如 babel 插件、ESLint 插件等）。
- 🎨 **静态样式**：使用属性访问（如 `x.display.flex`）定义静态原子样式，编译时完全解析。
- 🔧 **动态样式**：使用函数调用（如 `x.color(color)`）定义动态样式，运行时通过 CSS 变量实现。
- 🔢 **非标识符值**：用下划线处理数字开头值（如 `x.padding._16px`），用计算属性处理含空格或特殊字符的值（如 `x.opacity['0.5']`）。
- 🔗 **样式组合**：通过 `stylex.props()` 组合原子样式与其他 StyleX 样式，后定义样式优先。
- 📦 **安装与使用**：通过 npm 安装 `@stylexjs/atoms`，需配合 `@stylexjs/babel-plugin` 编译，否则运行时抛出错误。
- 🌐 **框架支持**：集成 Next.js、Vite、React Router、SvelteKit 等，并支持 Webpack、Rspack、Esbuild 等构建工具。
- 📚 **API 参考**：包括 `stylex.create`、`stylex.props`、`stylex.defineVars`、`stylex.createTheme`、`stylex.keyframes` 等核心功能。
- 🛠️ **工具与插件**：提供 babel 插件、ESLint 插件、PostCSS 插件、unplugin 等，用于编译和代码质量检查。
- 📄 **类型支持**：包含 `StyleXStyles<>`、`Theme<>`、`VarGroup<>` 等类型定义，增强 TypeScript 集成。
- 🎭 **主题与变量**：支持定义变量、创建主题、合并主题、暗黑模式及主题覆盖，通过 `stylex.defineVars` 和 `stylex.createTheme` 实现。
- 📝 **LLM 资源**：提供生态系统和致谢信息，强调开源贡献和社区支持。

---

### [WebSocket 支持现已进入公开测试阶段 - Vercel](https://vercel.com/changelog/websocket-support-is-now-in-public-beta)

**原文标题**: [WebSocket support is now in Public Beta - Vercel](https://vercel.com/changelog/websocket-support-is-now-in-public-beta)

Vercel Functions 现已支持 WebSocket 连接，实现客户端与服务器端代码的双向通信。  
- 🌐 支持实时功能：如交互式 AI 流式传输、聊天和协作应用。  
- ⚡ 基于 Fluid compute 运行，遵循与其他函数调用相同的限制和定价。  
- 💰 仅对消息处理时间计费（Active CPU 定价），空闲连接不收费。  
- 🛠️ 使用标准 Node.js 库即可部署，无需额外配置（示例：Express + ws 库）。  
- 🔌 支持高级库如 Socket.IO。  
- 📚 可查阅文档开始使用。

---

### [你正在错误地使用 React 复合组件](https://thetshaped.dev/p/you-are-using-react-compound-components-wrong-type-safe-typescript)

**原文标题**: [You're Using React Compound Components Wrong](https://thetshaped.dev/p/you-are-using-react-compound-components-wrong-type-safe-typescript)

概述摘要  
本文指出 React 复合组件模式常被误用，尤其在数据驱动列表场景中。作者强调复合组件应服务于布局灵活性，而非数据渲染，并提供了正确的使用场景和类型安全建议。

- 🚫 常见误区：教程中`<Select>`与`<Option>`的例子不适合复合组件模式，当数据来自数组时，使用 props API 更简洁高效。  
- ✅ 正确场景：复合组件适用于静态、异构内容（如 Tabs、Card、Toolbar），消费者需控制布局，父组件协调行为。  
- 🔒 类型安全：不应限制子组件类型，而应通过共享上下文（Context）实现类型安全，使用泛型工厂和`satisfies`确保值正确。  
- 📊 数据驱动：渲染列表时，使用 props（如`options`数组）更易排序、过滤和虚拟化，且类型安全。  
- ⚡ 快速决策：布局→复合组件；数据→props；需暴露内部状态→使用 render props 或 hooks。

---

### [Turbopack：通过 wbinnssmith 添加实验性 React 编译器支持 · 拉取请求 #94573 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/94573)

**原文标题**: [Turbopack: add experimental React compiler support by wbinnssmith · Pull Request #94573 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/94573)

该 PR 为 Next.js 的 Turbopack 添加了实验性的 React 编译器支持，已合并到 canary 分支。

- 🚀 新增 `experimental.rustReactCompiler` 配置选项，需与 `config.reactCompiler` 配合使用，否则报错
- 🎯 编译器仅对客户端代码（含 SSR）生效，不处理 RSC
- ⚡ 直接在 Turbopack 的 SWC AST 上运行编译器，无需生成和重新解析代码
- 🔧 需要将原始源代码传递给源转换，以支持 AST 直接操作
- 🐛 处理了非 TS 文件使用装饰器时，装饰器转换在 React 编译器之前运行的问题
- ✅ 经过多次代码推送和审查，最终由 lukesandberg 批准合并

---

### [肯尼斯·斯科夫胡斯 | 将 Linear 从 styled-components 迁移到 StyleX](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

**原文标题**: [Kenneth Skovhus | Moving Linear from styled‑components to StyleX](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

### 概述总结
Linear 团队将 React 应用从 styled-components 迁移至 StyleX，主要出于性能优化和构建更严格样式架构的考量。迁移过程借助编码代理和定制化代码转换工具，实现了渐进式推进，目前已完成 58% 的文件迁移，页面渲染速度提升约 30%。

### 关键要点
- 🚀 **性能优先**：运行时 CSS-in-JS 导致客户端渲染时产生样式生成和规则注入开销，StyleX 将样式生成移至构建阶段，显著减少运行时负担。
- 🛡️ **强化封装**：styled-components 的`styled(Button)`模式易导致外部样式覆盖，StyleX 通过严格约束使组件样式契约更清晰，避免维护噩梦。
- ⚙️ **确定性解析**：StyleX 提供可预测的样式合并规则，避免依赖 CSS 特异性游戏，提升跨文件样式一致性。
- 🔄 **健康生态**：Meta 积极维护 StyleX，兼容现代 React 模式，已被 Figma、Cursor 等公司采用，确保长期可靠性。
- 🤖 **代理辅助迁移**：开发了包含 500+ PR、10 万行代码的`styled-components-to-stylex-codemod`工具，配合编码代理处理复杂边缘案例。
- 📈 **渐进式策略**：先定义 StyleX 变量和基础组件，从叶子节点开始迁移，配合自定义 Lint 规则和 CSS Modules 逃生舱，避免冻结产品开发。
- 🎯 **显著收益**：迁移 58% 文件后，页面导航渲染速度提升 30%，同时通过收紧组件 API 降低了远程样式覆盖风险。

---

