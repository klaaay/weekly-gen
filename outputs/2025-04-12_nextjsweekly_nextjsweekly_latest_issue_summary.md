## [Next.js 15.3](https://nextjs.org/blog/next-15-3)

**原文标题**: [Next.js 15.3 | Next.js](https://nextjs.org/blog/next-15-3)

**中文标题**: "Next.js 15.3 | Next.js"

Next.js 15.3 发布，包含 Turbopack 构建、客户端监控钩子、导航钩子等新功能。

- 🚀 **Turbopack 构建（Alpha）**：生产构建速度提升，支持多核加速（4 核快 28%，16 核快 60%，30 核快 83%），通过 99.3% 的集成测试。  
- 🔧 **Rspack 社区支持（实验性）**：提供 Webpack 兼容的替代打包方案，测试通过率约 96%。  
- 📊 **客户端监控钩子**：通过 `instrumentation-client.js` 提前设置性能监控和错误跟踪。  
- 🔗 **导航钩子**：新增 `onNavigate`（控制路由行为）和 `useLinkStatus`（导航状态指示）提升客户端路由灵活性。  
- ⚡ **TypeScript 插件优化**：语言服务器性能提升 60%，解决大型代码库卡顿问题。  
- 🔄 **其他改进**：支持 `new URL()` 远程图片、视口选项分离、Pinterest Rich Pins 等。  
- 📥 **升级指南**：提供 CLI 自动升级或手动安装命令，支持新项目创建。  
- 🤝 **生态合作**：与 Sentry 等工具集成，邀请开发者反馈以推动稳定版发布。  
- 🙏 **致谢**：感谢超过 3000 名贡献者，包括 Next.js、Turbopack 和文档团队的成员。

---

## [Building Reusable Components with React 19 Actions](https://aurorascharff.no/posts/building-reusable-components-with-react19-actions/)

**原文标题**: [Building Reusable Components with React 19 Actions | Aurora Scharff](https://aurorascharff.no/posts/building-reusable-components-with-react19-actions/)

**中文标题**: "使用 React 19 Actions 构建可复用组件 | Aurora Scharff"

React 19 Actions 简化了处理待定状态、错误、乐观更新和顺序请求的过程。本文探讨了如何在 Next.js App Router 中使用 React 19 Actions 构建可重用组件，并介绍了相关 API 的使用方法。

- 🚀 **React 19 Actions**：通过过渡（transitions）调用的函数，可更新状态和执行副作用，不阻塞用户交互。
- 🔄 **useTransition()**：用于跟踪过渡状态，提供 `isPending` 状态以显示加载指示器或禁用按钮。
- ⚡ **useOptimistic()**：在过渡期间立即更新状态，提供即时用户反馈。
- 🛠️ **RouterSelect 组件**：构建可重用的选择组件，通过 URL 参数更新值，优化用户体验。
- 🔄 **跟踪待定状态**：使用 `useTransition()` 包装路由跳转逻辑，显示加载状态。
- ⏳ **乐观更新**：通过 `useOptimistic()` 立即更新选择组件的值，避免用户等待。
- 📤 **暴露 Action 属性**：通过 `setValueAction` 属性支持父组件的自定义逻辑。
- 🏗️ **复杂可重用组件**：在父组件中使用 `useOptimistic()` 处理乐观更新，保持组件的可重用性。
- 📌 **关键要点**：Actions 简化状态管理，命名需清晰，乐观更新提升用户体验。
- 🎯 **结论**：React 19 Actions 提供了强大的工具来构建高效、可重用的组件。

---

## [Trigger v4 – Background jobs & AI infrastructure](https://trigger.dev/blog/v4-beta-launch/?ref=nextjsweekly)

**原文标题**: [Trigger.dev v4 beta | Trigger.dev](https://trigger.dev/blog/v4-beta-launch/?ref=nextjsweekly)

**中文标题**: "Trigger.dev v4 测试版 | Trigger.dev"

Trigger.dev v4 beta 版发布，包含多项性能改进和新功能，如热启动、全新设计的仪表盘、等待点机制等，升级简单且兼容性强。

- 🚀 **v4 beta 发布**：Trigger.dev 推出 v4 beta 版，包含 Run Engine 2，性能显著提升。  
- ⚡ **热启动优化**：任务完成后机器暂不关闭，下次任务启动时间缩短至 100-300ms。  
- 🎨 **全新仪表盘**：环境导航更直观，支持组织图标、队列管理等功能。  
- ⏳ **等待点机制**：新增 Waitpoint 功能，支持人工干预（如审批流程）和超时控制。  
- 🔄 **幂等性支持**：triggerAndWait 等操作支持幂等键，避免重复执行相同任务。  
- ⏱️ **时间等待优化**：支持幂等键和仪表盘手动跳过等待，便于测试。  
- 🔼 **任务优先级**：可设置任务优先级，确保关键任务优先执行。  
- ⏸️ **队列暂停功能**：支持暂停环境或单个队列，紧急情况下快速停止任务。  
- 🛠️ **中间件与生命周期钩子**：改进中间件系统，新增 locals 和生命周期钩子（如 onWait、onResume）。  
- 🤖 **内置 MCP 服务器**：CLI 支持 MCP 服务器，便于调试和触发任务。  
- 🌍 **多区域支持计划**：未来将根据需求扩展欧洲、亚洲等地区的 worker 节点。  
- 🏠 **自托管方案**：正在开发支持多 worker 服务器的自托管指南，含 Kubernetes 方案。  
- 📥 **如何体验**：v4 beta 已开放，升级指南提供无缝迁移路径。

---

## [React for Two Computers](https://overreacted.io/react-for-two-computers/)

**原文标题**: [React for Two Computers — overreacted](https://overreacted.io/react-for-two-computers/)

**中文标题**: "双机 React——过度反应"

- 🚀 **文章概述**：作者探讨了如何将 React 程序拆分为在两个计算机上运行，通过时间（Early 和 Late 世界）和空间（客户端和服务器）的分离来实现分布式计算。  
- 📝 **写作过程**：作者多次尝试撰写这篇文章，最终意识到更适合作为演讲内容，并在 React Conf 上进行了分享。  
- 🎥 **演讲内容**：演讲主题是 React Server Components（RSC），并提供了相关视频链接。  
- 🔍 **标签与函数调用的区别**：分析了 HTML 标签（如`<p>`）和 JavaScript 函数调用（如`alert()`）的异同，包括命名习惯（名词 vs 动词）和嵌套结构。  
- 🧩 **组件的两种类型**：  
  - **Components（组件）**：以大写字母开头，负责逻辑和结构（如`<Greeting />`）。  
  - **Primitives（原语）**：小写字母开头，直接执行操作（如`alert`）。  
- ⏳ **时间分割**：通过将计算分为 Early（早期）和 Late（晚期）世界，实现分步执行。Early 世界生成“蓝图”，Late 世界执行具体操作。  
- 🌐 **空间分割**：通过`import tag`和`import rpc`语法，将代码拆分到不同计算机上运行，同时保持类型安全和模块化。  
- 🛠 **实现工具**：  
  - `interpret`函数：解析组件树，溶解 Early 组件。  
  - `perform`函数：执行最终的原语操作（如 DOM 渲染）。  
- 🧠 **关键思想**：  
  - **标签是潜在的函数调用**：被动、惰性，等待未来执行。  
  - **闭包跨网络**：通过序列化代码和数据，实现跨环境的状态传递。  
- 🎮 **挑战与解决**：  
  - **时间顺序问题**：通过区分“嵌入”（不检查参数）和“内省”（检查参数）函数，确保执行顺序灵活性。  
  - **跨世界通信**：通过`import tag`引用 Late 世界的代码，避免直接执行。  
- 🍩 **最终解决方案**：通过包装（如`<Donut>`组件）将 Early 世界的内容嵌入 Late 世界，实现混合计算。  
- 📚 **扩展思考**：包括数据获取、流式执行、状态管理、缓存等高级应用场景。  
- 🔗 **实践示例**：提供了可运行的代码演示和 Parcel 对 RSC 的支持链接。  

（注：内容经过大幅压缩，保留了核心逻辑和关键示例，省略了部分代码和对话细节。）

---

## [𝕏 How Next.js handles Prefetching & Prerendering under the hood](https://x.com/leerob/status/1908320730875363679)

**原文标题**: [No title found](https://x.com/leerob/status/1908320730875363679)

**中文标题**: 未找到标题

当前页面提示 JavaScript 未启用或浏览器不受支持，建议启用 JavaScript 或更换浏览器以继续使用 x.com，并提供相关帮助和条款链接。

- 🚫 JavaScript 未启用或浏览器不受支持  
- 🔄 建议启用 JavaScript 或更换支持的浏览器  
- ℹ️ 提供帮助中心链接以获取支持的浏览器列表  
- 📜 包含服务条款、隐私政策等法律链接  
- ⚠️ 隐私相关扩展可能导致问题，建议禁用后重试  
- 🔄 页面错误提示，鼓励用户再次尝试

---

## [LLM bots + Next.js image optimization = recipe for bankruptcy](https://metacast.app/blog/engineering/postmortem-llm-bots-image-optimization)

**原文标题**: [LLM bots + Next.js image optimization = recipe for bankruptcy (post-mortem) | Metacast Blog](https://metacast.app/blog/engineering/postmortem-llm-bots-image-optimization)

**中文标题**: "LLM 机器人+Next.js 图像优化=破产配方（事后剖析） | Metacast 博客"

以下是按照您提供的模板总结的内容：

Metacast 团队在使用 Next.js 和 Vercel 的图像优化 API 时，因配置不当导致大量 LLM 机器人爬取图像，可能造成 7000 美元的高额费用。团队及时发现并采取措施，包括禁用图像优化、更新 robots.txt 和配置防火墙规则来阻止机器人流量。此次事件让团队意识到在规模运营时需要更强的防御意识和成本控制措施。

- 🚨 **成本激增警报**：Vercel 发出预算警告，显示资源使用已达预算的 50%，主要由图像优化 API 驱动。
- 📈 **图像优化 API 使用激增**：2 月 7 日，图像优化请求激增，可能导致 7000 美元的高额账单。
- 🤖 **LLM 机器人流量**：发现来自 Amazonbot、ClaudeBot、Meta 等机器人的大量请求，总计 66.5k 次。
- 🛑 **紧急措施**：立即配置防火墙规则，阻止来自 Amazon、Anthropic、OpenAI 和 Meta 的机器人流量。
- 🖼️ **禁用图像优化**：禁用外部主机的图像优化功能，仅允许自身域名的图像优化。
- 📜 **更新 robots.txt**：通过程序生成 robots.txt，限制特定机器人和 SEO 工具的访问。
- 💡 **经验教训**：设置敏感的支出限制警报，意识到规模运营和机器人流量的挑战。
- 🛡️ **防御准备**：了解并准备使用 Vercel 防火墙或 Cloudflare WAF 来应对未来的机器人流量。
- 📢 **社交媒体反响**：在 LinkedIn 上分享事件，引发广泛讨论，获得大量关注和建议。
- 🔄 **后续更新**：Vercel 在事件后调整了图像优化定价，但团队仍需自行优化外部托管的图像。

---

## [How does the use API work with Next 15 and React 19?](https://www.premieroctet.com/blog/en/how-does-the-use-api-work-with-next-15-and-react-19)

**原文标题**: [How does the use API work with Next 15 and React 19? - Agence Premier Octet](https://www.premieroctet.com/blog/en/how-does-the-use-api-work-with-next-15-and-react-19)

**中文标题**: "如何将 use API 与 Next 15 和 React 19 结合使用？ - Agence Premier Octet"

Next 15 和 React 19 中 API 的使用方式及其优化数据获取和用户体验的新特性。

- 🌐 数据获取和变更是网站开发的核心，Next 15 和 React 19 提供了多种解决方案。
- 🔄 React 19 引入了新的`use` API，用于处理异步数据获取，优化用户体验。
- ⚡ 传统数据获取方法包括客户端`fetch`、服务器操作、服务器组件`fetch`和服务器函数，各有优缺点。
- 🚀 `use` API 允许传递`Promise`到客户端组件，实现非阻塞渲染，提升性能。
- 🛠️ 使用`use` API 需要配合`Suspense`和`ErrorBoundary`来管理加载和错误状态。
- 📦 服务器组件可以立即渲染，无需等待`Promise`解析，提高页面响应速度。
- ⚠️ 注意避免遗留未使用的`Promise`，以免影响性能。
- 🔧 `use` API 的其他用途包括条件使用、从`Context`获取数据等。
- 📉 缺点是每个使用`use` API 的组件都需要配置`Suspense`和`ErrorBoundary`，可能增加代码量。
- 📚 相关资源包括 NextJS 数据获取文档、React `use` API、`Suspense`和服务器组件 RFC。

---

## [Introducing Chat SDK](https://vercel.com/blog/introducing-chat-sdk)

**原文标题**: [Introducing Chat SDK - Vercel](https://vercel.com/blog/introducing-chat-sdk)

**中文标题**: "介绍 Chat SDK - Vercel"

Chat SDK 是一个免费开源的模板，专为构建强大的聊天机器人应用而设计，基于 Next.js 和 AI SDK，支持多模态和自定义功能，适合从个人项目到企业级解决方案的开发需求。

- 🚀 **免费开源**：Chat SDK 是一个免费且开源的模板，用于构建高性能的聊天机器人应用。  
- 🔧 **技术栈**：基于 Next.js App Router 和 AI SDK，支持任意 AI 模型和提供商。  
- 🏗️ **生产就绪**：集成 v0 的最佳实践，持续更新以保持技术领先。  
- 💡 **核心功能**：包括消息持久化、身份验证、多模态支持和可分享聊天记录。  
- 🎨 **生成式 UI**：支持动态交互界面，超越传统文本回复，提升用户体验。  
- 🛠️ **自定义组件**：可构建专属功能模块，如文档生成或交互式工具。  
- 💻 **浏览器代码执行**：通过 WASM 和 pyodide 直接运行代码，无需额外沙箱环境。  
- 📚 **详细文档**：涵盖项目搭建、架构设计、主题定制及测试策略，提供迁移指南。  
- 🌐 **一键部署**：支持快速部署，适合各类应用场景。  
- 🔗 **资源链接**：访问 [chat-sdk.dev](https://chat-sdk.dev) 获取完整文档和教程。

---

## [Origin UI: Calendar Layout](https://crafted.is/exp6)

**原文标题**: [Experiment 06 - Crafted.is](https://crafted.is/exp6)

**中文标题**: 实验 06 - Crafted.is

这是一个日历视图的摘要，显示了 2025 年 4 月 6 日至 12 日的一周安排，包含多个会议和家庭时间。

- 📅 日历显示 2025 年 4 月 6 日（周日）至 12 日（周六）的一周安排  
- 🕗 每天从上午 8 点到晚上 7 点的时间段被标记  
- 👨👩👧👦 家庭时间安排在 4 月 6 日上午 10 点至下午 1:30 和 4 月 12 日上午 7 点  
- 📅 4 月 7 日（周一）的会议包括：  
  - ☕ 与 Ely 的会议（上午 7-8 点）  
  - 🏢 团队跟进（上午 8:15-11 点）  
  - 🤝 与 Pedra 的检查（下午 3-4 点）  
- 📅 4 月 8 日（周二）的安排包括：  
  - 👥 团队介绍（上午 8:15-9:30）  
  - 📊 任务展示（上午 10:45-下午 1:30）  
- 📅 4 月 9 日（周三）的主要会议：  
  - 🏢 产品会议（上午 9-11:30）  
  - 🕐 团队会议（下午 1:30）  
- 📅 4 月 10 日（周四）的安排：  
  - 👤 与 Tommy 的 1 对 1 会议（上午 9:45-10:45）  
  - 📞 启动电话（上午 11 点）  
- 📅 4 月 11 日（周五）的会议：  
  - 🔄 每周回顾（上午 8:45-9:45）  
  - 🤝 与 Mike 的会议（下午 2:30-3:30）

---

## [source code](https://github.com/origin-space/ui-experiments/tree/main/apps/experiment-06)

**原文标题**: [ui-experiments/apps/experiment-06 at main · origin-space/ui-experiments · GitHub](https://github.com/origin-space/ui-experiments/tree/main/apps/experiment-06)

**中文标题**: "ui-experiments/apps/experiment-06 位于 main · origin-space/ui-experiments · GitHub"

这是一个名为 `ui-experiments` 的公开 GitHub 仓库的目录结构概览。

- � **仓库信息**：公开仓库，拥有 580 个星标和 77 个复刻。  
- 🔔 **通知设置**：需要登录才能更改通知设置。  
- 📂 **目录结构**：主要包含 `apps/experiment-06/` 下的多个子目录和配置文件。  
- 📁 **子目录**：包括 `app`、`components`、`hooks`、`lib`、`providers` 和 `public` 等。  
- 📄 **配置文件**：包含 `eslint.config.js`、`next.config.mjs`、`package.json` 等常见的项目配置文件。  
- 🛠 **开发工具**：使用了 Next.js、TypeScript (`tsconfig.json`)、PostCSS 等工具。  
- 📊 **其他文件**：包含 `components.json` 和 `registry.json` 等可能用于组件管理的文件。

---

## [RetroUI](https://retroui.dev/)

**原文标题**: [Retro Styled React UI Library | Retro UI](https://retroui.dev/)

**中文标题**: 复古风格 React UI 库 | Retro UI

升级至 TailwindCSS v4，推出复古风格 React 组件库 RetroUI，内含 40+ 免费可复制粘贴的 UI 组件，支持 Tailwind 定制与 TypeScript 类型安全，拥有活跃开发者社区，并提供 50+ 付费高级组件与模板。

- 🎨 升级至 TailwindCSS v4，打造复古风格 React 组件库 RetroUI  
- 🆓 提供 40+ 免费 UI 组件，支持直接复制粘贴使用  
- 🛠️ 基于 TailwindCSS 高度可定制，且全面支持 TypeScript 类型安全  
- 🌟 开发者社区活跃：350+ GitHub 星标，100+ Discord 成员  
- 🔄 兼容 SSR 和 SPA 应用开发  
- 💖 开源项目，由社区贡献者共同维护  
- 🚀 付费 Pro 版含 50+ 高级组件、完整网站模板及终身更新  
- 📢 创始人：Arif Hossain，提供 Twitter/GitHub/文档等资源支持

---

## [Tailwind CSS v4.1](https://tailwindcss.com/blog/tailwindcss-v4-1)

**原文标题**: [Tailwind CSS v4.1: Text shadows, masks, and tons more - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-1)

**中文标题**: "Tailwind CSS v4.1：文字阴影、遮罩及更多功能 - Tailwind CSS"

Tailwind CSS v4.1 正式发布，新增多项实用功能和改进，包括文本阴影、元素遮罩、浏览器兼容性优化等，同时提升了开发体验。

- 🌟 新增 `text-shadow-*` 工具类，支持文本阴影效果，可调整颜色和透明度。  
- 🎭 引入 `mask-*` 工具类，支持使用图片和渐变遮罩元素，提供更灵活的 API。  
- 🌐 优化老旧浏览器兼容性，确保颜色、阴影等功能在旧设备上正常渲染。  
- 📏 新增 `overflow-wrap` 工具类，精细控制文本换行，避免长单词破坏布局。  
- 🎨 支持彩色 `drop-shadow`，可为阴影添加颜色和透明度效果。  
- 🖱️ 新增 `pointer-*` 和 `any-pointer-*` 变体，针对不同输入设备（如鼠标或触摸屏）调整样式。  
- 🔍 新增 `items-baseline-last` 和 `self-baseline-last` 工具类，对齐弹性或网格容器的最后一行文本基线。  
- 🛡️ 引入 `safe` 对齐工具类，防止内容在容器过小时溢出。  
- 🚫 新增 `@source not` 功能，忽略指定路径以加速构建。  
- 📌 新增 `@source inline(…)` 功能，强制生成未在源码中使用的工具类。  
- 🔄 新增多个变体，如 `noscript`、`user-valid`、`inverted-colors` 等，增强交互体验。  
- 📦 支持通过 npm 安装最新版本，适配 Tailwind CLI、Vite 和 PostCSS。  

此次更新还包含更多细节改进，具体可查看[发布说明](https://tailwindcss.com/blog/tailwindcss-v4-1)。

---

## [Multi-tenancy doesn’t have to be complicated](https://clerk.com/blog/multitenancy-clerk-supabase-b2b?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=supabase-multitenant&utm_content=04-11-25&dub_id=tCxcftVPYlTM8Q8H)

**原文标题**: [Implementing multi-tenancy into a Supabase app with Clerk](https://clerk.com/blog/multitenancy-clerk-supabase-b2b?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=supabase-multitenant&utm_content=04-11-25&dub_id=tCxcftVPYlTM8Q8H)

**中文标题**: "使用 Clerk 在 Supabase 应用中实现多租户"

协作软件行业预计到 2032 年将达到近 530 亿美元的规模，为应用添加多租户功能将有助于抢占市场份额。Clerk 与 Supabase 的集成简化了多租户功能的实现，通过组织管理和 RLS 策略确保数据安全。

- 🏢 **行业前景**：协作软件市场预计 2032 年达 530 亿美元，多租户功能成为收入增长关键。  
- 🔐 **技术基础**：Supabase 依赖 Postgres RLS 保障数据安全，Clerk 提供无缝的 B2B 工具集成。  
- 👥 **组织管理**：Clerk 的 Organizations 功能支持团队创建、成员邀请及权限管理，简化协作流程。  
- 🛠️ **UI 组件**：`<OrganizationSwitcher />`等预置组件快速实现组织切换与管理。  
- 🔗 **Supabase 集成**：通过解析 JWT 中的`org_id`和`sub`值，结合 RLS 策略实现多租户数据隔离。  
- 📝 **代码示例**：使用`coalesce`函数或自定义`requesting_owner_id()`简化 RLS 策略，支持组织和用户 ID 回退。  
- 🧪 **实践演示**：以 Quillmate 为例，展示如何启用组织功能、更新 RLS 策略及测试多租户场景。  
- 📊 **效果验证**：不同用户或组织访问独立数据，数据库中的`owner_id`区分用户与组织归属。  
- 🚀 **快速实现**：Clerk 与 Supabase 结合，几分钟内即可为应用添加多租户和团队协作功能。

---

## [Cloudflare adapter for OpenNext](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/)

**原文标题**: [Deploy your Next.js app to Cloudflare Workers with the Cloudflare adapter for OpenNext](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/)

**中文标题**: 使用 OpenNext 的 Cloudflare 适配器将 Next.js 应用部署到 Cloudflare Workers

Cloudflare 推出 1.0.0-beta 版的@opennextjs/cloudflare 适配器，优化 Next.js 应用在 Cloudflare Workers 上的部署，支持更多 Next.js 功能并提升性能。

- 🚀 **适配器发布**：Cloudflare 适配器 1.0.0-beta 版发布，取代 Next on Pages 成为部署 Next.js 应用到 Cloudflare 的首选方式。  
- 🔧 **功能支持**：支持 Next.js 15 的大部分功能，包括缓存处理、部分预渲染（PPR）、中间件、App 和 Pages 路由以及图像优化。  
- 🛠 **未来计划**：计划在 1.0 版本中全面支持 Windows 开发，并在后续版本中添加 Edge 运行时和组合缓存支持。  
- 🌍 **生态系统改进**：Workers 的 NodeJS 兼容性提升，模块支持更全面，Worker 大小限制也有所增加。  
- 📅 **路线图**：v2 版本将专注于减少包大小、提升应用性能和支持多 Workers 部署。  
- 🛠 **部署步骤**：通过简单命令即可创建、开发和部署 Next.js 应用到 Workers，支持本地预览和快速部署。  
- 📢 **反馈渠道**：鼓励用户通过 GitHub 和 Discord 提供反馈和贡献代码。  
- 🔗 **资源链接**：提供 Cloudflare 和 OpenNext 的文档链接，方便用户深入了解和操作。

---

## [𝕏 Running end-to-end tests in GitHub Actions against Vercel deployments](https://x.com/anthonysheww/status/1909360804140285983)

**原文标题**: [No title found](https://x.com/anthonysheww/status/1909360804140285983)

**中文标题**: 未找到标题

当前浏览器未启用 JavaScript，无法正常使用 x.com 的功能。请启用 JavaScript 或切换至支持的浏览器继续访问。  

- 🌐 浏览器未启用 JavaScript，导致功能受限  
- 🔄 建议启用 JavaScript 或更换支持的浏览器  
- 📖 支持浏览器列表可在帮助中心查看  
- 🛠️ 隐私相关扩展可能导致问题，建议禁用后重试  
- ℹ️ 页脚包含帮助中心、服务条款、隐私政策等链接

---

## [Experimenting with React View Transitions](https://frontendatscale.com/issues/43)

**原文标题**: [Experimenting with React View Transitions | Frontend at Scale](https://frontendatscale.com/issues/43)

**中文标题**: "React 视图过渡实验 | 规模化前端"

本周的简报由作者的一场顽固感冒开启，内容聚焦 React 新特性 View Transitions API 的实验心得，同时兼顾其他前端技术动态。

- 🤒 作者调侃自己持续感冒的状态，戏称它为"新合著者"
- ⚛️ 本期重点介绍 React 新推出的 View Transitions 组件实验性功能
- 🎬 演示了如何通过<ViewTransition>组件实现跨页面元素动画
- 🧪 分享三周实验发现的三大优势：自动触发时机、动态命名策略、生命周期类控制
- 🎧 推荐新播客访谈：Frontend Masters 创始人谈技术教育未来
- 💡 精选资源包含：浏览器 SQLite 实践、CSS 新函数、代码可读性研究等
- 🤖 仅推荐了两篇 AI 相关文章，强调实用 LLM 编程技巧
- ✨ 文末附赠炫酷的 View Transitions 演示案例
- 📢 预告将撰写完整指南，邀请读者持续关注

（注：根据用户要求，已省略"overview summary"标题，直接呈现概要内容）

---

## [Understanding SPAs and their shortcomings](https://reacttraining.com/blog/understanding-spas-and-their-shortcomings)

**原文标题**: [Understanding SPAs and their shortcomings](https://reacttraining.com/blog/understanding-spas-and-their-shortcomings)

**中文标题**: "理解 SPA 及其缺点"

概述了单页应用（SPA）的定义、实现方式、存在的问题以及现代框架的解决方案。

- 🏠 **SPA 的定义**：单页应用旨在通过不刷新页面来保持 JavaScript 状态，预下载所有页面的 JavaScript 以实现快速页面切换。  
- ⚙️ **SPA 的实现细节**：通常采用客户端渲染（CSR），先加载空 HTML 文件，再加载包含所有页面指令的大型 JavaScript 包，最后获取数据。  
- 🔄 **客户端渲染（CSR）**：CSR 是一个更广泛的术语，指任何在客户端使用 JavaScript 渲染 UI 的方式。  
- 📦 **SPA 的问题**：随着应用规模增长，包体积增大，代码分割和懒加载成为常见解决方案，但会导致数据获取延迟。  
- ⏳ **懒加载的缺点**：用户导航到新页面时需先下载 JS 代码，再获取数据，导致两次串行请求，影响性能。  
- 🛠️ **解决方案**：避免在“页面”组件内获取数据，推荐使用 React Router Loaders（v6.4+）来优化。  
- 🔄 **现代框架的改进**：Next.js 和 React Router Framework 等框架通过 SSR 提供完整 HTML，同时在页面间实现客户端导航，结合了 SPA 和 MPA 的优点。  
- 🌐 **框架的定位**：现代框架更像是 SPA 和多页应用（MPA）的混合体，既保留了 SPA 的优点，又解决了其问题。

---

