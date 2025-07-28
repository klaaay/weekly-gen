### [React Server Components：发展历程 | Kent C. Dodds 的 Epic React](https://www.epicreact.dev/react-server-components-how-we-got-here-zcuxn)

**原文标题**: [React Server Components: How We Got Here | Epic React by Kent C. Dodds](https://www.epicreact.dev/react-server-components-how-we-got-here-zcuxn)

概述  
本文回顾了网页应用架构的演变历程，从早期的多页面应用（MPA）到现代 React 服务器组件（RSC），分析了每种架构的优缺点，并重点介绍了 RSC 如何结合前几代技术的优势，简化开发流程并提升性能。  

- 🌐 **多页面应用（MPA）**  
  - 优点：简单、无需 JavaScript、SEO 友好  
  - 缺点：全页面刷新导致体验差、服务器负载高  

- ⚛️ **单页面应用（SPA）**  
  - 优点：交互流畅、无刷新体验  
  - 缺点：代码复杂、SEO 困难、首屏性能差  

- 🛠️ **渐进增强 SPA（如 Remix）**  
  - 优点：恢复渐进增强、减少网络管理代码  
  - 缺点：路由与组件混合、学习成本高  

- 🚀 **React 服务器组件（RSC）**  
  - 优点：组件化组合、自动网络管理、性能优化  
  - 缺点：新心智模型、生态工具待完善  

- 🔄 **技术演进的意义**  
  - 每一代技术解决前代问题，RSC 综合了 MPA 的简单性、SPA 的交互性和渐进增强的优势。  

- ✨ **RSC 的核心优势**  
  - 消除网络管理代码（如加载状态、错误处理），减少复杂性和错误。  

- 🔮 **未来展望**  
  - RSC 可能是自 React 以来最重要的架构进步，推动更简单、高性能的 Web 应用开发。  

- 📚 **延伸学习**  
  - 推荐通过工作坊和课程深入了解 RSC 的实际应用。

---

### [更好的认证 1.3](https://www.better-auth.com/blog/1-3)

**原文标题**: [Better Auth 1.3](https://www.better-auth.com/blog/1-3)

Better Auth 1.3 版本发布，包含多项新功能和改进，如 SSO 支持 SAML 2.0、多团队支持、组织额外字段、性能优化等。

- 🚀 **SSO 插件独立**：支持 OIDC 和 SAML 2.0，提供更灵活的认证选项。  
- ✅ **OIDC & MCP 插件稳定**：支持刷新令牌、JWKs、PKCE 等，适合生产环境。  
- 💳 **Stripe 插件正式版**：支持基于使用的定价，即将推出更多功能。  
- 🔑 **SIWE 插件**：新增以太坊登录（Sign-In with Ethereum）支持。  
- 🆕 **新增社交登录提供商**：包括 Notion、Slack、Linear 和 Faceit。  
- 🍪 **SvelteKit Cookie 插件**：优化服务器动作中的 Cookie 处理。  
- ✉️ **登录时邮件验证**：支持在用户登录时发送验证邮件。  
- 👥 **多团队支持**：组织插件现支持用户属于多个团队。  
- 📝 **组织额外字段**：可自定义组织、成员和邀请模型的字段。  
- 🔧 **通用 OAuth 改进**：支持额外令牌 URL 参数和令牌加密选项。  
- 🔑 **API 密钥增强**：支持异步验证和名称必填选项。  
- ✨ **更多功能**：迁移至 Zod 4、CLI 支持自定义适配器、文档优化等。  
- 🐛 **Bug 修复与改进**：修复了插件、OAuth、核心认证等多个问题，提升稳定性和性能。

---

### [如何在 Next.js 应用中添加具有实时更新的后台任务 - Inngest 博客](https://www.inngest.com/blog/background-jobs-realtime-nextjs?ref=nextjs-weekly-5)

**原文标题**: [How to add background jobs with real-time updates to a Next.js application - Inngest Blog](https://www.inngest.com/blog/background-jobs-realtime-nextjs?ref=nextjs-weekly-5)

本文介绍了如何在 Next.js 应用中使用 Inngest 实现后台任务和实时更新功能，以提升用户体验和系统性能。

- 🚀 **背景任务的核心作用**：通过将后端工作移至 API 之外，保持用户体验的响应性，适用于如导入联系人等耗时操作。
- 📧 **实时更新的重要性**：通过电子邮件或流式消息通知用户任务完成情况，例如批量发送电子邮件。
- 🔧 **项目概述**：CampaignCraft 是一个 Next.js 应用，利用 Inngest 处理联系人导入和电子邮件发送的后台任务。
- 🛠️ **技术栈**：包括 Next.js、Shadcn、Vercel、OpenAI、Neon、Drizzle 和 Inngest。
- ⚙️ **后台任务工作原理**：将耗时任务移出主请求/响应循环，通过队列和重试机制提高可靠性。
- 🔄 **实时更新机制**：使用 WebSocket 协议实现服务器和浏览器之间的持久双向通信，无需轮询。
- 📡 **Inngest Realtime 功能**：提供 API 发送实时更新，支持通过频道和主题组织消息。
- 📝 **实现步骤**：包括安装 Inngest SDK、配置后台任务、发送实时消息和前端订阅更新。
- 🔍 **常见问题解答**：涵盖并发限制、重试配置、连接丢失处理和多重订阅等。
- 📚 **进一步学习**：提供文档和专家咨询链接，帮助深入理解 Inngest 的功能和应用。

---

### [使用动态导入优化 Next.js 性能 | Medium](https://medium.com/@aalbertini95_90842/optimize-next-js-performance-with-smart-code-splitting-what-to-load-when-and-why-485dac08cd24)

**原文标题**: [Optimize Next.js Performance with Dynamic Imports | Medium](https://medium.com/@aalbertini95_90842/optimize-next-js-performance-with-smart-code-splitting-what-to-load-when-and-why-485dac08cd24)

Next.js 通过智能代码分割优化性能：了解何时加载何物及其原因  

- ⚡ 代码分割将应用拆分为按需加载的小块，提升初始加载速度、减小包体积，优化移动网络用户体验  
- 🔄 动态导入（`dynamic imports`）替代静态导入，延迟加载非必要组件（如模态框、标签页、权限内容）  
- 🗂️ 适用场景：重量级组件（图表/地图）、条件渲染 UI（下拉菜单）、角色受限内容（管理员面板）  
- 🎯 示例 1：动态模态框仅在点击时加载，减少主包体积  
- 📊 示例 2：标签页动态加载各标签内容（如报表/用户列表），避免初始加载冗余代码  
- 📦 第三方库动态加载：Leaflet（地图）、WaveSurfer（音频）、Chart.js（图表）可节省 375KB+ 初始包大小  
- ⚙️ Next.js 默认按页面自动代码分割，路由导航仅加载对应模块  
- 🚫 通过`ssr: false`禁用服务端渲染，解决浏览器 API 依赖问题（如`window`对象）  
- 💡 核心原则：非关键路径代码动态加载，平衡性能与用户体验

---

### [未找到标题](https://x.com/asidorenko_/status/1947304774249959470)

**原文标题**: [No title found](https://x.com/asidorenko_/status/1947304774249959470)

当前页面提示 JavaScript 未启用或浏览器不受支持，建议调整设置或更换浏览器以继续使用 x.com。

- 🚫 JavaScript 未启用：检测到浏览器中 JavaScript 被禁用，需启用或更换支持浏览器。  
- 🌐 支持浏览器列表：可在帮助中心查看兼容的浏览器信息。  
- 🔧 扩展冲突提示：部分隐私相关扩展可能导致问题，建议禁用后重试。  
- 📜 相关链接：提供帮助中心、服务条款、隐私政策等文档入口。  
- ©️ 版权信息：页面底部显示 2025 年 X 公司版权声明。  
- 🔄 操作建议：遇到错误可尝试重新加载页面。

---

### [React 编译器 - React](https://react.dev/learn/react-compiler)

**原文标题**: [React Compiler – React](https://react.dev/learn/react-compiler)

React Compiler 是一个自动优化 React 应用的工具，通过处理记忆化（memoization）减少手动使用 `useMemo`、`useCallback` 和 `React.memo` 的需求。  

- 🚀 **React Compiler 功能**：自动优化应用，减少手动记忆化操作。  
- ⚙️ **安装指南**：提供安装步骤和构建工具配置方法。  
- 🔄 **渐进式采用**：支持在现有代码库中逐步启用编译器。  
- 🐞 **调试与故障排除**：提供调试指南，帮助区分编译错误与运行时问题。  
- 📜 **配置与参考**：包含详细配置选项、指令和预编译库的指南。  
- 🌐 **额外资源**：推荐加入 React Compiler 工作组获取更多信息。  
- ◀️ **相关链接**：可参考 React Developer Tools 和更多 React 学习资源。

---

### [介绍 Zustand（状态管理）—— Frontend Masters 博客](https://frontendmasters.com/blog/introducing-zustand/)

**原文标题**: [Introducing Zustand (State Management) – Frontend Masters Blog](https://frontendmasters.com/blog/introducing-zustand/)

概述总结  
Zustand 是一个简洁、有趣且高效的状态管理库，尽管已有五年历史，但仍有许多开发者不熟悉它。本文通过一个任务管理应用示例，对比了使用 React Context 和 Zustand 的状态管理方式，展示了 Zustand 的优势。

- 🚀 **Zustand 简介**  
  Zustand 是一个极简但强大的状态管理库，通过`create`方法创建状态，简化了状态管理流程。

- 🔄 **状态更新**  
  使用`set`函数更新状态，支持部分更新和完全覆盖，操作简单直观。

- 📖 **正确读取状态**  
  推荐使用选择器函数读取状态，避免不必要的重新渲染，提升性能。

- ⚡ **性能优化**  
  Zustand 通过选择器函数和`useShallow`钩子，显著减少了不必要的组件重新渲染。

- 🌐 **异步支持**  
  Zustand 天然支持异步操作，可以在异步函数中调用`set`更新状态。

- 🔍 **状态读取**  
  支持在组件内外读取状态，通过`getState`方法可以在非 React 环境中访问状态。

- 🔧 **高级功能**  
  Zustand 还支持手动订阅、与 Immer 等不可变库集成，适用于复杂场景。

- 💡 **总结**  
  Zustand 简洁易用，能有效提升 React 应用的性能和开发体验。适合需要高效状态管理的项目。

---

### [无标题 UI React —— React UI 组件库](https://www.untitledui.com/react)

**原文标题**: [Untitled UI React â React UI Component Library](https://www.untitledui.com/react)

Untitled UI React 是一个开源的 React UI 组件库，基于 Tailwind CSS 和 React Aria 构建，提供丰富的组件和模板，适合各种规模的项目。

- 🚀 **开源组件库**：Untitled UI React 是世界上最大的开源 React 组件库之一，支持快速复制、粘贴和构建。  
- 🎨 **技术栈**：基于 React v19.1、Tailwind CSS v4.1、TypeScript v5.8 和 React Aria，确保高性能和可访问性。  
- 📦 **丰富组件**：包含 5000+ 组件和 250+ 页面示例，涵盖按钮、表格、图表、模态框等多种类型。  
- 🛠️ **开发工具**：提供 CLI 工具和预配置的 Starter Kits（如 Next.js、Vite），支持快速启动项目。  
- 🌙 **暗黑模式**：内置 CSS 变量支持，一键切换暗黑模式。  
- 💰 **灵活定价**：提供免费版和付费 PRO 版（个人/团队授权），支持终身更新。  
- 🎨 **设计与代码同步**：与 Untitled UI Figma 设计工具完美同步，确保设计一致性。  
- 📚 **详细文档**：提供全面的文档和示例，便于开发者快速上手。  
- 🌍 **社区认可**：已被 280,000+ 设计师和开发者使用，包括多家知名公司。  

适合希望快速构建高质量、可访问性强的 React 应用的开发者。

---

### [GitHub - magicuidesign/changelog-template: 使用 Next.js 构建的极简更新日志模板](https://github.com/magicuidesign/changelog-template)

**原文标题**: [GitHub - magicuidesign/changelog-template: A minimal changelog template built using Next.js.](https://github.com/magicuidesign/changelog-template)

一个基于 Next.js 构建的极简更新日志模板，用于按时间顺序展示产品发布、功能和错误修复。

- 🚀 **项目简介**: 极简更新日志模板，基于 Next.js 构建，支持按时间顺序展示产品更新。
- ✨ **主要特性**:  
  - 时间线设计（带日期和版本号）  
  - 深色模式（自动主题切换）  
  - 响应式布局（适配所有设备）  
  - MDX 支持（用 MDX 编写日志条目）  
  - 高性能（使用 Next.js 15 和 React 服务端组件）
- 📂 **项目结构**:  
  - `app/` - Next.js 应用路由  
  - `changelog/content/` - MDX 日志内容  
  - `components/` - React 组件  
  - `lib/` - 工具函数  
  - `public/` - 静态资源
- ⚙️ **快速开始**:  
  - 安装依赖：`pnpm install`  
  - 启动开发服务器：`pnpm dev`  
  - 访问 `http://localhost:3000`
- 📝 **添加日志条目**:  
  - 在 `changelog/content/` 创建 `YYYY-MM-DD.mdx` 文件，包含标题、描述、日期、标签和版本信息。
- 🔧 **脚本命令**:  
  - `pnpm dev` - 开发模式  
  - `pnpm build` - 生产构建  
  - `pnpm lint` - 代码检查
- 🛠️ **技术栈**:  
  - Next.js 15  
  - Tailwind CSS  
  - shadcn/ui 组件  
  - TypeScript 类型安全
- 🌍 **部署**: 支持 Vercel（推荐）、Netlify 和 Cloudflare Pages。
- 📜 **许可证**: MIT 开源协议。

---

### [GitHub - tobiaslins/nextjs-typed-api](https://github.com/tobiaslins/nextjs-typed-api)

**原文标题**: [GitHub - tobiaslins/nextjs-typed-api](https://github.com/tobiaslins/nextjs-typed-api)

Next.js Typed API 是一个为 Next.js 应用提供的完全类型安全的 API 客户端，无需代码生成即可实现完整的 TypeScript 支持。

- ✨ **零代码生成**：无需构建步骤或代码生成  
- 🔒 **完全类型安全**：自动推断输入验证和输出类型  
- 🛡️ **运行时验证**：可选的 Zod 模式验证，确保输入检查的健壮性  
- 🚀 **动态路由支持**：支持参数化路由，如 `/api/users/[id]`  
- 🎯 **SWR 集成**：内置缓存和数据获取功能  
- 📝 **自动完成**：通过 IntelliSense 提供丰富的 IDE 支持  
- 🛠 **简单设置**：只需最少的配置  

### 快速开始
1. **创建 API 路由**  
   - 使用 `createApiHandler` 定义 API 处理程序，支持基本 TypeScript 类型或 Zod 模式验证。  
2. **设置类型化客户端**  
   - 创建 API 客户端配置，映射路由路径到对应的处理程序类型。  
3. **在组件中使用**  
   - 使用完全类型化的 API 客户端进行查询和变更操作。  

### 动态路由
- 自动处理动态路由参数，支持基本类型或 Zod 模式验证。  

### 运行时验证
- 使用 `withSchema` 自动处理验证错误，返回结构化 400 错误响应。  

### API 参考
- **useQuery**：从 API 端点获取数据，支持 SWR 选项。  
- **useMutation**：执行变更操作（POST、PUT、DELETE），支持乐观更新和缓存重新验证。  
- **withSchema**：为 API 处理程序添加 Zod 验证。  

### 工作原理
- 利用 TypeScript 类型系统直接从 API 路由处理程序中提取类型。  
- 无需代码生成或构建步骤，纯 TypeScript 实现。  

### 优势
- **开发体验**：IDE 即时反馈和自动完成。  
- **安全性**：在编译时捕获 API 契约违规。  
- **可维护性**：类型自动与 API 保持同步。  
- **性能**：基于 SWR 实现最佳缓存和数据获取。  
- **简单性**：无需复杂设置或配置。  

### 开发
- 安装依赖：`pnpm install`  
- 运行开发服务器：`pnpm dev`  
- 类型检查：`pnpm build`  

许可证：MIT

---

### [错误](https://github.com/vercel/satori)

**原文标题**: [Error](https://github.com/vercel/satori)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /vercel/satori (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Vercel 到底为啥要雇 Nuxt 的创始人？ - YouTube](https://www.youtube.com/watch?v=4AeSZcRGp1E)

**原文标题**: [Why the hell did Vercel hire the creators of Nuxt? - YouTube](https://www.youtube.com/watch?v=4AeSZcRGp1E)

关于 YouTube 的相关信息与链接  
- 📢 关于：了解 YouTube 的更多背景与详情  
- 🗞️ 新闻：查看 YouTube 的最新动态与公告  
- ©️ 版权：版权声明与知识产权信息  
- 📩 联系我们：提供反馈或寻求帮助的渠道  
- 🎨 创作者：为内容创作者提供的资源与支持  
- 💼 广告：广告合作与商业推广信息  
- 👩💻 开发者：开发者工具与 API 相关资源  
- 📜 条款：平台使用条款与条件  
- 🔒 隐私：隐私政策与数据保护措施  
- ⚖️ 政策与安全：社区准则与安全规范  
- 🔧 YouTube 运作机制：平台功能与工作原理说明  
- 🧪 测试新功能：体验即将推出的新特性  
- © 2025 Google LLC：版权归属与年份声明

---

### [Vercel 如何为开发团队节省超 1000 万美元生产力成本 | Guillermo Rauch - YouTube](https://www.youtube.com/watch?v=IU95gajl2FA)

**原文标题**: [How Vercel Saves Dev Teams $10M+ in Productivity Gains | Guillermo Rauch - YouTube](https://www.youtube.com/watch?v=IU95gajl2FA)

关于 YouTube 的相关信息与链接

- 📢 关于 - 了解 YouTube 的更多背景信息  
- 🗞️ 媒体 - 查看 YouTube 的新闻与公告  
- ©️ 版权 - 版权相关政策和信息  
- 📩 联系我们 - 提供联系方式以便沟通  
- 🎨 创作者 - 为内容创作者提供的资源和支持  
- 💼 广告 - 广告合作与推广信息  
- 👩💻 开发者 - 开发者工具和资源  
- 📜 条款 - 使用条款和条件  
- 🔒 隐私 - 隐私政策和数据保护  
- ⚖️ 政策与安全 - 平台政策与安全措施  
- 🔧 YouTube 工作原理 - 平台运作机制解析  
- 🧪 测试新功能 - 尝试最新推出的实验性功能  
- © 2025 Google LLC - 版权归属声明

---

### [2025 年前端性能优化清单](https://crystallize.com/blog/frontend-performance-checklist)

**原文标题**: [Frontend Performance Checklist For 2025](https://crystallize.com/blog/frontend-performance-checklist)

前端性能优化清单 2025 是一份全面、跨平台的指南，旨在通过一系列最佳实践和优化策略提升网站速度和效率。以下是关键要点总结：

- 📊 **性能的重要性**  
  - 用户平均注意力仅 8 秒，53% 的移动用户会在 3 秒内未加载完成时离开页面。  
  - 页面速度直接影响转化率（如 Walmart 每提升 1 秒加载速度，转化率增加 2%）。  
  - 性能优化能改善 SEO 排名、广告质量评分及用户体验。

- ⏱️ **性能测量工具**  
  - 使用 Google PageSpeed Insights、Chrome Lighthouse、WebPageTest 等工具进行基准测试。  
  - 结合实验室数据和真实用户监控（如 CrUX 数据）定位问题。

- 🛠️ **HTML 优化**  
  - 优先加载关键 HTML，清理冗余代码，启用 Brotli 压缩。  
  - 避免阻塞渲染的脚本，谨慎使用 iframe（建议懒加载）。

- 🎨 **CSS 优化**  
  - 移除未使用的样式，拆分模块化 CSS，避免`@import`。  
  - 内联关键 CSS 并异步加载剩余部分，简化选择器，利用`content-visibility`延迟渲染。

- ⚡ **JavaScript 优化**  
  - 减少依赖库，代码拆分非关键脚本，使用`async/defer`。  
  - 更新依赖项，选择轻量框架（如 Astro/Next.js），优先使用原生 HTML/CSS 功能。

- 🖼️ **图片处理**  
  - 按需调整尺寸，使用`srcset`响应式图片，压缩为 WebP/AVIF 格式。  
  - 预加载首屏图片，懒加载非首屏内容，明确设置宽高避免布局偏移。

- 📹 **视频优化**  
  - 压缩文件，选择高效编解码器（如 VP9），按需设置`preload`属性。  
  - 移除无用音轨，长视频采用流媒体（HLS/DASH），懒加载非可见视频。

- ✒️ **字体优化**  
  - 限制字体家族数量，使用 WOFF2 格式，预连接第三方字体源。  
  - 通过`font-display: swap`避免文本闪烁，考虑变量字体减少文件数。

- 🌐 **服务器与托管**  
  - 启用 HTTP/2/3 和 CDN 加速，配置缓存策略（静态资源长期缓存）。  
  - 优化 TTFB（目标<200ms），尽可能预生成静态页面。

- 🚀 **快速优化技巧**  
  - 避免布局偏移（CLS），合理使用优先级提示（`fetchpriority`）。  
  - 减少第三方请求，统一 HTTPS 协议，预取下一页资源，利用 Service Worker 缓存。

- 📌 **持续优化**  
  - 性能优化是长期过程，需团队协作和定期审计，结合业务目标（如 SEO、转化率）综合提升。  

通过这份清单，开发者可系统性提升前端性能，打造更快、更高效的 Web 应用。

---

### [将类型视为带有类型级别映射的值 | TypeScript | gregros.dev](https://gregros.dev/typescript/treating-types-as-values-with-type-level-maps)

**原文标题**: [Treating types as values with type-level maps | TypeScript | gregros.dev](https://gregros.dev/typescript/treating-types-as-values-with-type-level-maps)

TypeScript 的类型系统允许开发者将复杂类型视为“类型级代码”，即在编译时执行的代码。本文重点介绍了类型级数据结构中的“类型级映射”及其应用。

- 🧠 类型级代码与运行时代码对比：类型级代码在编译时执行，其值为类型本身，而运行时代码处理字符串、数字等常规值。
- 🔧 类型级操作：包括应用类型级运算符、调用类型级函数（泛型类型）、定义类型级接口（通过泛型约束）和使用类型级数据结构。
- 🗺️ 类型级映射：本质上是对象类型，通过接口定义，被视为不可变字典，其中键为字符串，值为类型。
- 🔍 类型级映射操作：
  - 列出键：使用 `keyof` 操作符获取键的联合类型。
  - 查找值：通过键进行静态或泛型查找。
  - 多值查找：一次查找多个键对应的值。
  - 转换映射：使用映射类型将一种映射转换为另一种。
- 🛠️ 应用场景：以事件处理为例，展示了如何使用类型级映射来避免重复代码并增强类型安全性。
  - 松散类型：缺乏类型检查，易出错。
  - 手动编码：重复代码多，难以扩展。
  - 类型级映射：通过定义事件映射和操作，实现类型安全和代码复用。
- ✅ 测试验证：通过实际代码示例验证了类型级映射的有效性，能够捕获拼写错误和类型不匹配等问题。
- 🎯 结论：类型级代码提供了一种新的视角来理解和设计复杂类型，其原理与运行时代码相似，能够有效解决类型层面的设计问题。

---

### [未找到标题](https://x.com/leerob/status/1946323104692945188)

**原文标题**: [No title found](https://x.com/leerob/status/1946323104692945188)

当前页面提示 JavaScript 未启用或浏览器不受支持，建议采取相应措施以继续使用 x.com。

- 🚫 JavaScript 未启用：检测到浏览器中 JavaScript 被禁用，需启用或更换支持浏览器。  
- 🌐 支持浏览器列表：可在帮助中心查看支持的浏览器详情。  
- 🔧 其他问题：隐私相关扩展可能导致访问异常，建议禁用后重试。  
- 📜 相关链接：提供帮助中心、服务条款、隐私政策等文档入口。  
- ⚠️ 错误提示：操作失败时显示友好提示，鼓励用户再次尝试。  
- ©️ 版权信息：页面底部标注 2025 年 X 公司版权及广告声明。

---

### [Laravel 与 Node.js：Watt 运行环境中的 PHP](https://blog.platformatic.dev/laravel-nodejs-php-in-watt-runtime)

**原文标题**: [Laravel and Node.js: PHP in Watt Runtime](https://blog.platformatic.dev/laravel-nodejs-php-in-watt-runtime)

Laravel 应用现可通过 Platformatic PHP stackable 在 Node.js 的 Watt 运行时中运行，为全栈 JavaScript 和 PHP 开发者提供了新的可能性。

- 🚀 Laravel 应用现可在 Node.js 进程中运行，减少基础设施复杂性  
- 🔗 使用 Rust 原生模块 `@platformatic/php-node` 实现高性能 PHP 与 JavaScript 桥接  
- 📦 简单步骤集成：初始化项目、配置 `package.json`、添加 Laravel 应用  
- ⚙️ 通过 `platformatic.json` 配置文档根目录和 URL 重写，支持热重载  
- 🌐 支持统一部署 PHP 和 Node.js 服务，优化资源共享  
- 🔧 高级功能包括自定义 PHP 扩展、环境变量管理和性能调优  
- 🔮 未来展望：逐步迁移 PHP 应用、构建多语言微服务架构

---

