### [TanStack Start 1.0 稳定版发布 | TanStack 博客](https://tanstack.com/blog/tanstack-start-1-0)

**原文标题**: [TanStack Start 1.0 is Stable | TanStack Blog](https://tanstack.com/blog/tanstack-start-1-0)

TanStack Start 1.0 正式发布稳定版，作者 Tanner Linsley 回顾了从 Router 起步到构建全栈框架的漫长历程，感谢核心贡献者与合作伙伴，并强调类型安全、显式 API 与框架自由选择的核心理念。

- 🎉 TanStack Start 1.0 正式稳定，可放心用于生产环境，官方承诺 API 不再发生颠覆性变化
- 🧭 项目初衷源于打造类型安全的路由器，最终演进为全栈框架，并成为 AI 时代的重要基础
- ⚖️ 在 Next.js 与 React Router 之外提供另一种选择：保留 SPA 的开发体验，同时支持 SSR、流式渲染与服务器函数
- 🔧 通过 `createIsomorphicFn`、`createServerFn` 等显式 API，让开发者清楚掌控代码在服务端还是客户端运行
- 🚀 核心贡献者带来显著提升：类型安全性能优化，以及约 5.5 倍的 SSR 吞吐量改进
- 🌐 坚持框架无关性，支持 Solid 与 Rsbuild；部署方面借助 Vite 与 Nitro 避免维护大量适配器
- 💭 在 RSC 上投入大量精力并完成集成，但最终在官网停用，体现可自由选择进出的灵活性
- 🤖 AI 智能体显著改变开发与维护方式：一方面用于安全审计与性能优化，另一方面也带来大量低质量 PR 的挑战
- 🧠 类型安全与显式 API 意外成为对智能体的天然助力，并通过 TanStack Intent 为智能体提供技能指导
- 🤝 众多企业从早期就押注 Start 并投入生产，Vercel、Railway、Lovable、Netlify、Cloudflare 等合作伙伴提供集成与资金支持
- 🙏 作者公开致谢维护团队、贡献者与社区，鼓励开发者用文档、迁移指南或直接让智能体协助上手体验

---

### [TanStack Start 与 Next.js（2026）：同一应用基准测试对比 | Waseem Anjum](https://www.fabwaseem.com/blog/tanstack-start-vs-nextjs)

**原文标题**: [TanStack Start vs Next.js (2026): Same App Benchmarked | Waseem Anjum](https://www.fabwaseem.com/blog/tanstack-start-vs-nextjs)

作者用同一个电商小应用，在 2 核 Node 24.22 环境下对比 TanStack Start 1.169.3 与 Next.js 16.4.2。结论是：TanStack Start 在按请求 SSR 和 API 场景中大幅领先；Next.js 仅在预渲染静态页略胜。选型关键取决于应用是否可缓存、是否依赖 RSC 与内置能力。

- 🚀 TanStack Start 1.0 于 2026 年 10 月 13 日稳定发布，但 Server Components 仍为实验性功能，默认关闭。
- 🧪 基准测试使用相同路由、数据、组件和 Tailwind，2 核 Xeon、Node 24.22、oha 64 连接压测 10 秒，取 3 次中位数。
- 📈 SSR 列表页：Start 637 req/s，Next.js 220 req/s，约 2.9 倍；商品页：2,341 vs 512，约 4.6 倍。
- 🔌 JSON API：Start 18,515 req/s，Next.js 2,165 req/s，约 8.6 倍，差距最大。
- ⏱️ 列表页 p99 延迟：Start 194 ms，Next.js 754 ms；空闲内存 60 MB vs 94 MB，峰值 363 MB vs 504 MB。
- 📦 客户端 JS：Start 109 KB gzip，Next.js 135 KB gzip，少约 20%；4 倍 CPU 降速下按钮可交互时间 289 ms vs 324 ms。
- ⚡ 生产构建：Start 1.26 s，Next.js 4.86 s，约 3.9 倍；开发服务器首屏 1.52 s vs 2.96 s；部署产物 1.4 MB vs 38 MB。
- 🏆 Next.js 仅在预渲染首页胜出：3,220 vs 2,920 req/s，约 10%；可静态化或缓存的内容会明显缩小差距。
- 🧭 适合选 TanStack Start：按用户或请求渲染的仪表盘、SaaS、内部工具、API 密集型应用、强类型路由、Vite、自托管或 Cloudflare Workers。
- 🧱 适合选 Next.js：内容站、可预渲染/缓存页面、依赖 RSC、next/image、next/font、metadata API、Vercel 生态与成熟模板。
- 🔁 迁移要点：app/ 路由改为 src/routes/createFileRoute，[id] 改为 $id，数据加载改 loader + createServerFn，移除 "use client"，route handler 改 server route，Server Actions 改 POST server function，next/link 改 TanStack Router Link，并配置 Nitro。
- ⚠️ 常见误区：必须同渲染模式比较、生产模式压测、服务器与压测机分核、确保 Next.js standalone 复制 .next/static、检查 devtools 未进入客户端包。
- ✅ 建议：现有健康 Next.js 应用不必仅为基准数字重写，应先做缓存；新交互型应用可将 TanStack Start 1.0 作为严肃默认选项。

---

### [从 Next.js 迁移 | TanStack Start React 文档](https://tanstack.com/start/latest/docs/framework/react/migrate-from-next-js)

**原文标题**: [Migrate from Next.js | TanStack Start React Docs](https://tanstack.com/start/latest/docs/framework/react/migrate-from-next-js)

该指南说明如何将 Next.js App Router 应用迁移到 TanStack Start，核心是保留现有应用行为并逐个翻译框架边界，而不是机械重命名文件；文中提供可运行的前后对照示例和端到端测试，覆盖公开文章、搜索、登录、私有页面与 mutation。

- 🧪 参考示例要求 Node 24+、pnpm 11，分别在 3100/3101 端口运行 Next.js 与 Start，并用 Playwright 对两个应用执行同一组浏览器测试；示例账号仅用于演示，不是生产级认证。
- 🧭 迁移原则：Start 不解释 Next.js 的路由约定或配置；应保持应用可观察行为，再逐项转换框架边界；重度依赖 RSC 时需先阅读比较文档和 RSC 指南，因为 Start 的 RSC 支持仍是实验性、需显式启用。
- 📋 迁移前先盘点应用：记录动态路径、查询参数、重定向、尾斜杠、语言前缀、响应状态、标题、描述、canonical、robots 指令和 sitemap 成员，并保留代表性 HTML 响应与现有测试。
- 🔍 单独盘点 Next.js 专属代码：`next/*` 导入、`'use server'`、server-only 模块、metadata 导出、`generateStaticParams`、`revalidatePath`、`revalidateTag`、缓存指令、middleware、图片/字体配置等。
- 🧱 可让 Start 与 Next.js 并存：保留 Next.js 应用可运行，新增 `src/router.tsx`、`src/routes` 和 Vite 配置；根路由中放置 `HeadContent` 与 `Scripts`，并合并 CSS、文档属性和 providers。
- 🗺️ 路由文件需按行为映射：`layout.tsx`→`__root.tsx`，`page.tsx`→`index.tsx`，`[slug]`→`$slug`，`[...parts]`→`$`，API route→server handler；嵌套布局、无路径布局、并行路由和拦截路由要逐项设计。
- 🔗 用 Router 的 `Link` 替代 `next/link`，动态路径使用类型化 `params`；需检查直接请求、客户端导航、前进/后退和刷新。
- 🔎 URL 搜索状态应在路由中用 `validateSearch` 运行时验证；loader 依赖搜索值时用 `loaderDeps`；页码、排序和过滤不能只依赖 TypeScript 类型。
- 🖥️ 数据库查询、凭证和特权 SDK 读取应放入 server function，再由 loader 调用；只返回浏览器可见数据，连接配置和密钥留在服务端。
- 🔁 Mutation 可通过 `useServerFn` 调用 POST server function，成功后 `router.invalidate()` 重新加载活动路由数据；该操作不会清 CDN、数据库缓存或所有静态页，使用 TanStack Query 时还需失效相关 query keys。
- 🔐 私有读取和 mutation 必须在服务端鉴权；示例用 `iron-session` 适配 `getCookie`/`setCookie`，私有页返回 `Cache-Control: private, no-store`；隐藏按钮或客户端路由守卫不等于授权。
- 🏷️ `metadata`/`generateMetadata` 转为路由 `head` 配置，并保留根文档中的 `HeadContent`；`sitemap.ts` 改为 `/sitemap.xml` server route，同时显式迁移 robots、icons、manifest 和社交图，缺失内容返回真实 404。
- 🖼️ Start 不自动提供 Next.js 图片优化器；需保留尺寸、响应式源、加载行为、alt 和缓存策略，或接入兼容图片服务；`next/font` 需改为自托管字体、Fontsource 等方式，并检查字重、子集、`font-display` 和布局偏移。
- 🧊 分别梳理浏览器数据、Router loader、Query、服务端数据、生成页面和 CDN 响应缓存；Next.js 的缓存指令、ISR 和 `generateStaticParams` 不会自动等价迁移，需在实际部署中验证。
- 🚀 用 staging 对两个应用执行契约检查；过渡期保持数据库 schema 兼容，准备回滚路径并确认 session 与写入影响；切换后监控错误率、登录/mutation 失败、状态码、索引信号和转化事件，验证后再移除 Next.js 及其未使用配置。

---

### [为什么我从 Astro 迁移到 TanStack Start - Sarthak](https://sarthakmishra.com/blog/astro-to-tanstack-start)

**原文标题**: [Why I moved from Astro to TanStack Start - Sarthak](https://sarthakmishra.com/blog/astro-to-tanstack-start)

overview summary
作者解释了为何将个人作品集从 Astro 迁移到 TanStack Start：核心原因是匹配 Cloudflare 部署环境与 React 客户项目技术栈，并为后续营销页面、程序化 SEO 和客户区实验提供统一应用空间。迁移保留了大部分预渲染内容，但需要自行补齐 Astro 曾提供的行为，同时仍有性能与部署验证方面的遗留问题。

- 🎯 **迁移动机**：作者并非因 Astro 不支持 React 才迁移，而是因为主要客户工作使用 React、TanStack Router 和 Start，且 Cloudflare 是主要部署平台；统一技术栈便于试验后续功能。
- 🧱 **Astro 原本合适**：旧站多数公开页面预渲染，交互组件按需加载，内容与图片处理由框架承担，作者此前已做过轻量化。
- 🚀 **未来计划**：希望尝试连接 Google Ads、LinkedIn Ads、X Ads 等渠道的动态营销页、程序化 SEO，以及客户工作与账单区；这些是待探索方向，不是迁移已交付功能。
- 🛠️ **迁移方式**：与 Codex 合作，保留 Git 支持的 MDX，先迁移公开站点并尽量保持 URL、设计和交互，仪表盘与编辑界面暂缓。
- 🔍 **行为盘点**：旧站混合 Astro 页面、Preact 组件和 Hono 端点；迁移需把交互组件转为 React，并判断哪些旧行为值得保留，还发现询盘先入库后发邮件、失败重试可能重复写入的问题。
- 🧪 **原型验证**：先用富内容页面测试图表、响应式图片、对话框、视频、MDX、数据库和表单失败，并在 Cloudflare Workers 运行时验证；早期发现服务端图片 404、意外 Google Fonts 请求、重复 React runtime 等集成问题。
- 🧰 **技术栈**：锁定测试过的 Start、Router、React、Vite、Cloudflare 版本；Fuma Content 负责集合与 MDX 编译；vite-imagetools 配合原生 picture/img 处理响应式图片；发布规则、内容身份、图片策略和产物检查仍由应用负责。
- ⚛️ **渲染与交互**：公开内容继续预渲染，联系页和订阅结果页按请求 SSR；采用普通 React hydration 与定向懒加载，视频的可见性延迟、原生播放回退和清理需应用代码自行实现。
- 📝 **内容责任增加**：在导入和编译前排除草稿并检查产物；保护讨论 Astro 的 MDX 示例；把 AI 辅助编辑准备与发布构建分离，生成内容需人工审核提交；本地编辑需重启开发进程，仍有摩擦。
- 🔌 **API 与表单**：用原生 server routes 保留 HTTP 端点，新询盘用 server function，旧 contact 端点退役；询盘入库即视为接受，邮件失败单独报告；订阅使用条件写避免重复欢迎邮件和旧退订影响续订；增加“结果未知”状态，避免自动重试造成重复。
- 🧭 **导航状态**：持久化 React shell 让状态归属更明显；搜索查询应跨导航保留，画像或图片弹窗离开后必须关闭并只释放自身 overlay，同时测试键盘焦点与返回行为。
- 📉 **性能遗留**：发布前有 4 个页面指标未达标，包括 Blog 与 Newsletter Issue 的 CLS 约 0.196/0.213，以及 Exam Post 与 Avatar Post 的 LCP 2.931s/3.280s；作者选择先上线后修复，且不把原因全部归于 React。
- 🏗️ **构建优化**：冷构建从约 11.5 分钟降至 5 分 25 秒，热构建约 41 秒并复用 3,945 个缓存图片；降低 AVIF effort 6→4，并细化缓存身份，使 AVIF 设置变化不丢弃 WebP 缓存。
- 🌐 **部署验证**：检查重定向、搜索和旧页面资产；发现视频 Range 请求返回 200 而非 206，修复后通过字节检查与限速拖动，但 Worker 内部仍会读取前置字节；WebKit、真实 iPhone 和实时邮件未完全验证。
- ✅ **结论**：公开站已运行于 TanStack Start，作者获得了想维护的 React 应用；部分改动立即改善站点，部分则是留在 Astro 可避免的工作，后续营销页与客户流程需证明迁移价值。

---

### [掉进兔子洞——TanStack Start 迁移 | Sesam.hu](https://sesam.hu/post/down-the-rabbit-hole-tanstack-start-migration)

**原文标题**: [Down the rabbit hole — TanStack Start migration | Sesam.hu](https://sesam.hu/post/down-the-rabbit-hole-tanstack-start-migration)

作者记录了将 Lovable 项目从 Vite + React Router 单页应用迁移到支持 SSR 的 TanStack Start 的全过程；原本看似简单的迁移，最终引发性能优化、SEO 增强、代码清理、格式化基线和测试补全等一系列连锁工作，并几乎在一天内完成。

- 🚀 迁移起因：作者在 Lovable 项目设置中发现 “Migrate to TanStack Start (Advanced)”；自 2026 年 5 月 13 日起，新建项目默认使用支持 SSR 的 TanStack Start，而不是原来的 Vite + React Router SPA。
- ⬆️ 技术栈升级：React 18 → 19、Tailwind CSS 3 → 4，`react-helmet-async` 改为 React 19 原生文档元数据支持；`admin-upload-image` 后端函数改为应用内服务器函数。
- 🖼️ 修复文章图片闪烁：文章页改用路由 loader 预取文章及前后链接，再通过 `useSuspenseQuery` 读取数据；加载与错误状态交给 `pendingComponent` 和 `errorComponent`，Markdown 插件与组件映射提升为模块级常量。
- ⚡ 推广 TanStack 原生模式：首页、语言页、搜索页和管理页均在路由 loader 中加载数据，页面、查询和管理标签状态通过类型化 URL 搜索参数管理，悬停链接可预加载目标页，站点加载近乎即时。
- 🧹 全面清理代码：移除路由兼容层、旧重定向组件、`/404` 路由、重复的 toast 系统（仅保留 `sonner`）、大量未使用文件/hooks/依赖，以及无引用且不安全的重复 Supabase 浏览器客户端；并用 `no-restricted-imports` 防止误导入自动生成客户端。
- 🔗 支持每篇文章独立社交分享图：迁移后可通过 `head()` 为每篇文章设置 `og:image`，按 1200 × 630 生成预览图；无图文章回退到站点通用横幅。
- 📦 压缩社交预览图：端点输出小于 1 MB 的 JPEG，必要时缩放、将透明 PNG 展平到白底，并按 75、60、45、30 逐级降低质量；仍超限则拒绝并回退横幅，同时限制源文件大小和像素。
- 🧩 统一 Markdown 渲染：将 `ReactMarkdown` 组件映射和插件数组抽成共享组件，使后台预览与正式文章显示一致，并删除编辑器中约 140 行的重复映射。
- 🎨 建立 Prettier 格式化基线：创建 `.prettierrc.json` 贴近现有风格（双引号、分号、尾逗号、100 列），格式化约 98 个手工维护文件；排除生成文件、归档脚本、Deno 后端函数和归档文档。
- ✅ 增加本地与 CI 质量保障：用 Husky + lint-staged 在提交前自动格式化并运行 ESLint；GitHub Actions 在推送 `main` 和 PR 时执行类型检查、测试、lint、Prettier 检查与构建。
- 🕳️ 修复 Skitch 坏图：发现 91 篇文章中 124 张失效的 `img.skitch.com` 图片被存成 Evernote 首页 HTML，另有 3 篇仍热链 Skitch；移除坏图块、相关记录和占位文件，并添加支持本地化的丢失图片提示。
- 🧪 扩充测试：测试从 2 个文件扩展到 18 个文件、130 个测试，分三阶段覆盖纯逻辑、hooks 与校验、路由与组件冒烟测试，并纳入 CI 防止回归。
- 🌀 收尾感受：迁移像“掉进兔子洞”，不断发现新问题；作者在吃饭、买菜和面试之余，一天内完成了这些工作。

---

### [@ryansolid.bsky.social 在 Bluesky 上](https://bsky.app/profile/ryansolid.bsky.social/post/3mxrordjou22l)

**原文标题**: [@ryansolid.bsky.social on Bluesky](https://bsky.app/profile/ryansolid.bsky.social/post/3mxrordjou22l)

Ryan Carniato 在 Bluesky 上称赞一个 React 元框架，表示认可其架构，并指出该框架支持 SolidJS。

- ⚛️ 发帖者称赞该 React 元框架的架构“值得认可”
- ✅ 该框架明确支持 SolidJS
- 🔥 帖文使用火焰表情，表达积极与兴奋态度
- 🧩 原帖包含引用帖或其他嵌入内容
- 🕒 发帖时间为 2026 年 10 月 13 日

---

### [红迪](https://www.reddit.com/r/reactjs/comments/1x52hc9/tanstack_start_10_is_finally_stable/)

**原文标题**: [Reddit](https://www.reddit.com/r/reactjs/comments/1x52hc9/tanstack_start_10_is_finally_stable/)

您尚未提供需要总结的文章内容，因此目前无法生成要点摘要。
- 📄 请补充或粘贴需要总结的文本内容。
- ✍️ 收到内容后，我将按“概览摘要 + 表情符号要点”的格式输出。
- 🔍 摘要会保留关键信息和核心观点，并确保简洁清晰。

---

### [面向 AI 辅助开发的高级 TypeScript | Master.dev](https://master.dev/courses/typescript-ai/?utm_source=email&utm_medium=reactstatus&utm_content=typescriptcooper)

**原文标题**: [Advanced TypeScript for AI-Assisted Development | Master.dev](https://master.dev/courses/typescript-ai/?utm_source=email&utm_medium=reactstatus&utm_content=typescriptcooper)

本课程由 Adam Rackis 主讲，时长 4 小时 28 分钟，评分 4.9，面向已具备扎实 TypeScript 基础的学习者。课程聚焦 AI 时代下的 TypeScript 进阶能力：掌握泛型、条件类型、可辨识联合等高级特性，从而更有效地编写提示词、审查 AI 生成代码，并发现其中细微错误。

- 🎯 课程定位：帮助开发者驾驭复杂的 AI 生成代码，成为团队中的 TypeScript 类型系统专家。
- 🧱 基础巩固：讲解结构化类型与名义类型、类型即值集合、类型推断、`any`、`unknown`、`never`、函数类型、联合类型与字面量类型。
- 🛠️ 实用技巧：使用 `typeof` 提取运行时值的静态类型，依赖 TypeScript 的推断能力减少手写类型。
- 📝 表单与 API：通过 TanStack Form 实现类型安全表单，使用 `ReturnType`、`Parameters` 等工具类型导出公共 API 类型。
- 🧩 泛型深入：把类型作为参数传递，在 React 组件中使用泛型，处理泛型约束、代理层参数一致性、Zustand 选择器与 `groupBy` 的 `keyof T` 类型安全。
- 🤖 AI 协作：理解泛型和类型推断后，可更高效地让 AI 重构代码、生成泛型与条件类型，并引导 AI 输出更简单、可维护的方案。
- 🔗 联合类型与收窄：避免枚举、优先使用字符串字面量联合，掌握可辨识联合、`typeof`、`instanceof`、`Array.isArray`、自定义类型守卫与 `never` 穷尽检查。
- 🛡️ 类型完整性：学习多余属性检查、`satisfies`、条件类型与 `infer`、联合类型在条件类型中的分配行为，以及用类型断言辅助复杂类型测试。
- 🧮 高阶类型技术：涵盖元组子集递归判断、函数重载、模板字面量类型、型变（协变/逆变）以及映射类型的键重映射、过滤和投影。
- 🧠 核心心法：即使 TypeScript 能处理深层嵌套逻辑，也应退一步寻找更简单的解决方案，并确保真正理解 AI 生成的类型代码。

---

### [针对上游漏洞的 Next.js 安全更新 | Next.js](https://nextjs.org/blog/nextjs-security-update-october-14-2026)

**原文标题**: [Next.js Security Update for Upstream Vulnerabilities | Next.js](https://nextjs.org/blog/nextjs-security-update-october-14-2026)

Next.js 于 2026 年 10 月 14 日发布安全更新，修复多个上游依赖漏洞，并提供 v16.4.1（Active LTS）和 v15.5.28（Maintenance LTS）补丁版本，建议尽快升级以保障应用安全。

- 🔐 **更新版本**：v16.4.1 适用于 Active LTS，v15.5.28 适用于 Maintenance LTS，用户应尽快升级 Next.js 依赖。
- 🚨 **严重漏洞一**：使用 App Router 与 Cache Components 时，若 `use cache` 函数返回多个 typed arrays，可能导致未认证远程代码执行（Critical）。
- ⚠️ **无临时缓解**：针对上述 `use cache` 漏洞没有已知 workaround，即使应用没有类似函数，也建议立即升级。
- 🖼️ **严重漏洞二**：Image Optimization API 在使用 SVG 时存在未认证远程代码执行漏洞（Critical），与上游图像库的内存问题有关。
- 🛠️ **图像漏洞缓解**：可确保 Next.js 使用的 `sharp` 版本为 0.35.5 或更高；升级 Next.js 也会自动获得修复后的 `sharp`。
- 🧠 **高危漏洞三**：使用 App Router 且至少有一个 Server Action 的应用，可能遭构造请求导致 CPU 过度占用，从而引发拒绝服务（High）。
- ✅ **受影响范围**：使用 Pages Router 或未使用 Server Actions 的应用不受该 DoS 漏洞影响。
- 🛡️ **安全计划**：Vercel 通过 Open Source Bug Bounty 与研究人员合作维护 Next.js 等开源框架安全。
- 📧 **联系方式**：安全项目或漏洞管理相关问题可发送至 security@vercel.com。

---

### [](https://react.dev/reference/dev-tools/react-devtools-cdt-mcp)

**原文标题**: [React DevTools for agents – React](https://react.dev/reference/dev-tools/react-devtools-cdt-mcp)

概述总结：该文档介绍实验性的 `react-devtools-cdt-mcp`，它是一个面向 AI 编码代理的 React DevTools 浏览器库。导入页面后，它会让 Chrome DevTools MCP 自动发现并调用一组 React 工具，从而让代理查看组件树、props、Hooks、owner、源码位置和渲染耗时；该库仅适合开发环境，并且必须在 React 之前加载。

- 🧪 实验性功能：基于 Chrome DevTools MCP 的实验性第三方开发者工具 API，工具及其输出可能随版本变化。
- 🧩 核心作用：向页面注册 React 工具，Chrome DevTools MCP 连接页面后自动发现，代理可像调用普通 MCP 工具一样使用。
- ⚠️ 不是 MCP 服务器：它运行在页面内部，不需要加入 MCP 客户端配置；唯一需要配置的 MCP 服务器是 Chrome DevTools MCP。
- 📦 安装与导入：使用 `npm install --save-dev react-devtools-cdt-mcp` 安装；在应用入口文件最顶部、任何 `react-dom` 导入之前导入 `react-devtools-cdt-mcp/register`。
- 🐢 仅用于开发构建：它会像 React DevTools 扩展一样让 React 报告每次提交，导致应用变慢，因此不要用于生产环境。
- ⚙️ 前置条件：Chrome DevTools MCP 需启用 third-party developer tools；页面导入 register 后，代理才能列出并调用 React 工具。
- 🛠️ 核心工具：组件树快照、按名称查找组件、按 uid 获取 props/Hooks、按 DOM 元素找宿主组件、父级栈、owner 栈、owner 栈追踪、组件源码位置、开始/停止性能分析、trace 概览、commit 报告。
- 🔑 UID 规则：组件使用类似 `"r5"` 的短 uid，跨工具和重渲染保持稳定，但页面刷新后失效，需要重新获取。
- 📤 返回格式：所有工具返回可序列化的普通对象；失败时返回包含 `error` 信息的对象。
- 🧷 `register(target?)`：可手动安装 React DevTools hook 并注册工具；`target` 默认 `globalThis`，返回 `facade` 和 `unregister`；必须在 React 初始化前调用，同一 `target` 重复调用会返回已有注册。
- 🧭 排错要点：代理看不到工具时检查第三方工具开关和页面导入；组件树为空通常是导入太晚；服务端渲染或测试中导入会报浏览器环境错误；源码位置和 owner 栈仅开发构建可用；刷新后需重新获取 uid。
- 🧪 试用方式：文档提供沙盒工具控制台，可手动选择工具、编辑 JSON 参数并运行，演示查找组件、检查组件、从 DOM 元素定位、性能分析和查看 commit 渲染情况。

---

### [React Native 0.88 - 基于 Web 的事件分发、可变字体、SceneDelegate，无破坏性变更 · React Native](https://reactnative.dev/blog/2026/10/19/react-native-0.88)

**原文标题**: [React Native 0.88 - Web-Based Event Dispatching, Variable Fonts, SceneDelegate, no breaking changes · React Native](https://reactnative.dev/blog/2026/10/19/react-native-0.88)

React Native 0.88 于 2026 年 10 月 19 日发布。此次发布的核心变化包括：默认将事件分发切换到 Web 路径，为 Text/TextInput 引入可变字体，增加 iOS SceneDelegate 生命周期支持，并将 React 升级到 19.3.0、Metro 升级到 0.87。它也是继 0.83、0.86 之后第三个没有用户可见破坏性变更的版本，因此升级预期更平滑。

- 🚀 事件分发默认改用 W3C EventTarget API，支持捕获、冒泡、`stopPropagation()` 和 `preventDefault()`，公共事件 API 行为保持不变。
- 🧪 Canary 版本在原生 ref 上暴露 `addEventListener`、`removeEventListener`、`dispatchEvent`；旧插件注册表暂时保留在内部开关后，后续将移除。
- 🔤 `<Text>` 和 `<TextInput>` 在 Android/iOS 上支持 `fontVariationSettings`，接受 CSS 字符串和对象两种形式，对象键为四字符轴标签。
- 📦 Java TurboModules 可直接接收和返回 `ArrayBuffer`，Codegen 将其映射为 `com.facebook.react.bridge.ArrayBuffer`，减少二进制数据编码开销。
- ⚠️ 同步方法可借用 JavaScript 内存以避免复制，但借用字节仅在方法返回前有效；如需保留，应在调用期间复制。
- 📱 iOS 增加 SceneDelegate 生命周期支持，并兼容 AppDelegate；0.88 仅支持单场景，需保持 `UIApplicationSupportsMultipleScenes` 为 `false`。
- 🔁 迁移到 SceneDelegate 需移动 React Native 入口、将场景的 URL/用户活动回调转发给 `RCTLinkingManager`，并在 `Info.plist` 添加 `UIApplicationSceneManifest`。
- 🧰 Swift Package Manager 支持仍为实验性且需手动启用，CocoaPods 继续完整支持；计划 0.89 默认 SwiftPM 并保留 CocoaPods 退出选项。
- 🛠️ SwiftPM 工具链改进包括按 App 部署目标生成 iOS 版本、稳定 Xcode 构建、可移植项目、bash 构建脚本、`package.json` 的 `swiftpmConfig`、镜像优先下载。
- ✅ 0.88 无用户可见破坏性变更；从 0.87 升级通常无需修改应用代码。
- 🗑️ 弃用 `InitializeCore` 路径、`experimental_` 前缀背景样式、iOS `InputAccessoryView`、`ReactFragment.fabricEnabled` 及 `ReactImageManager` 的 `String?` 重载。
- 🎨 `backgroundSize`、`backgroundPosition`、`backgroundRepeat` 去掉 `experimental_` 前缀转为稳定；FileReader/Blob、RTL、Animated、ScrollView、Image 等有修复。
- 🧩 TypeScript/API 更新包括模块扩展增强、`requestIdleCallback` 声明、LogBox 方法、FlatList `strictMode` 与 VirtualizedList `ListItemComponent`。
- ⚙️ 依赖升级：React 19.3.0、Metro 0.87（最低 0.87.1）、Hermes 260318099.0.4；Android 默认 User-Agent 加入应用名和版本。
- 📊 该版本包含 568 个提交、91 位贡献者；0.88 为最新稳定版，0.85.x 转为不支持，Expo 项目将随 SDK 58 提供。
- ⬆️ 升级可使用 React Native Upgrade Helper 和升级文档；新项目可用 `npx @react-native-community/cli@latest init MyProject --version latest` 创建。

---

### [react-native-web 的维护与现代化 · necolas/react-native-web · 讨论 #2872 · GitHub](https://github.com/necolas/react-native-web/discussions/2872)

**原文标题**: [Maintenance and modernization of react-native-web · necolas/react-native-web · Discussion #2872 · GitHub](https://github.com/necolas/react-native-web/discussions/2872)

React Native Web 将由 Expo、necolas 与社区恢复活跃维护，并迁移至 React Foundation；整体方向是保守跟随 React Native，先处理维护积压，再在 0.22-dev 分支推进现代化，同时征集评审与预发布测试。

- 🛠️ 维护工作包括逐项处理开放 issue 和 PR，将其修复、合并或关闭，并通过常规版本发布 bug 修复。
- 🏛️ 仓库将迁至 React Foundation 的 GitHub 组织，与 React、React Native 并列；更广泛的 RN API 与原生/Web 融合问题仍归 React Native 和 react-strict-dom。
- 🌐 最低浏览器目标提升至 2021 年 10 月版本：Chrome/Edge 95+、Firefox 93+、Safari/iOS Safari 15.1+，以移除旧前缀、UA 嗅探和回退逻辑。
- ⚛️ 放弃 React 18 支持，react/react-dom peer 依赖改为 ^19.0.0，并移除 findDOMNode、forwardRef 用法。
- 🧰 代码库现代化包括从 Flow 迁移到 TypeScript，工具链转向 pnpm、tsdown、vitest、oxlint 等，发布为 ESM，并减少依赖。
- 🧹 移除 React Native 核心已不再提供的模块，如 CheckBox、Picker、ProgressBar、YellowBox、InteractionManager 和旧 Touchable mixin。
- ➕ 补充缺失的 React Native API，例如 PlatformColor、useAnimatedValue、usePressability，以及 Modal、Text、TextInput 的部分能力。
- 📦 弃用 babel-plugin-react-native-web；现代打包器已可通过别名和 tree shaking 实现类似效果。
- 🚧 “后续计划”包括打包器插件：配置 react-native→react-native-web 别名与 .web.js 解析、构建期替换 Platform.*、处理 @2x/@3x 资源，以及构建期抽取 CSS。
- 🙌 社区反馈显示 RNW 在生产中仍很重要，而 RSD 进展停滞；维护者建议先持续贡献补丁建立合作关系，当前急需 PR 评审者和预发布回归测试者。

---

### [宣布 TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/)

**原文标题**: [Announcing TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/)

TypeScript 7.1 Beta 已发布，重点包括导入属性、源码阶段导入、ES2026 目标、全新 API、内容映射器、性能与内存优化，以及更严格的分布式类型参数检查。可通过 `npm install -D typescript@beta` 试用。

- 🚀 **导入属性支持增强**：环境模块声明现在支持 `with { type: "css" | "text" | "bytes" }`，可根据导入属性提供正确类型，并在缺失属性时报错。
- 📦 **源码阶段导入**：新增 `import source` 与 `import.source()`，返回 `AbstractModuleSource`；WebAssembly 模块可直接传给 `WebAssembly.instantiate`。
- 🎯 **新增 `--target es2026`**：稳定支持 `Math.sumPrecise()`、`Iterator.concat()`、`JSON.rawJSON()`、`Error.isError()`、`Uint8Array` Base64/Hex 方法等。
- 🧰 **新 API 架构**：拆分为 `typescript/sync`、`typescript/async`、`typescript/fs`、`typescript/ast` 等入口，并提供可释放的 `API`、`Program`、`Snapshot` 对象。
- 🗂️ **快照与文件系统 API**：支持基于快照增量更新、虚拟文件系统、文件系统分层覆盖、内存中编译与 `emitToString()`。
- 🧩 **内容映射器（Content Mappers）**：让 Vue、Svelte、Astro、MDX、Ember、CSS Modules 等单文件组件格式获得一等支持；命令行需使用 `--runExternalCode`。
- ⚡ **性能与内存优化**：大量优化减少内存压力并加速构建；示例中最高约 **1.9x 加速**、内存最高减少约 **49.6%**。
- ⚠️ **行为变更**：对分布式类型参数检查更严格，部分依赖旧行为的代码可能需要调整。
- 🛣️ **后续计划**：接下来聚焦速度与稳定性，预计约一个月后发布 RC，随后发布正式版。

---

### [使用 Next.js 16.4 改善 v0 中的导航体验 | Next.js](https://nextjs.org/blog/improving-navigation-experience-in-v0-with-nextjs-16-4)

**原文标题**: [Improving navigation experience in v0 with Next.js 16.4 | Next.js](https://nextjs.org/blog/improving-navigation-experience-in-v0-with-nextjs-16-4)

文章介绍了 Vercel v0 如何借助 Next.js 16.4 的 Partial Prefetching 与新的 `next-partial-prefetching-optimizer` Skill，重构多处页面导航：让可复用内容和个性化内容在点击前或返回时可用，减少加载骨架，并通过 `instant()` Playwright 测试与生产指标持续优化，在控制成本的同时提升导航体验。

- 🚀 Next.js 16.3 引入 Partial Prefetching，16.4 增强缓存内容加载控制并提供优化 Skill；`create-next-app` 默认启用 Cache Components 与 Partial Prefetching。
- 🧩 传统 `prefetch={true}` 会抓取整页甚至动态内容；Partial Prefetching 只预取可复用部分，其余在导航时加载，并支持浏览器缓存中的个性化内容复用。
- 🧪 使用 `@next/playwright` 的 `instant()` 包裹点击，锁定导航期间才到达的内容，断言点击前标题、预览等 UI 已可用，使优化目标可测试。
- 🔁 优化 Skill 引导代理循环：选择导航与目标 UI → 编写 `instant()` 测试 → 确认断言失败 → 用缓存和预取重构 → 重跑测试 → 通过后保留回归测试。
- 🗂️ `/templates/[id]`：将公开模板数据用 `'use cache: remote'` 缓存，配合 `cacheTag()`、`cacheLife()`、`revalidateTag()`，并在卡片链接加 `prefetch={true}`，点击前准备好标题与预览。
- 🖱️ 大网格优化：避免为所有可见卡片立即富预取，改为在 hover、focus、touch 等用户意图触发；此前 `/templates/[id]` 预取请求曾增至 2.9 倍。
- 🔐 `/settings`：个性化内容用 `'use cache: private'` 存在浏览器中，`scope` 进入缓存 key 以隔离账户/团队；Advanced 页面缓存 5 分钟，保存自定义指令时用 `updateTag()` 立即失效。
- ⏳ `/projects`：用 Next.js 16.4 的 `navigation()` 将低优先级内容（如 Recent Chats）延迟到导航后加载，同时保留返回复用；项目标题和 Production Deployment 通过意图预取。
- 📊 整体指标：每日总成本降低 2.9%；Runtime Cache 支出增至 4.3 倍、约增加 $3.44/天；请求量、计算与传输下降使请求服务成本降低 14.4%。
- ✅ 同期流量变化使整体数据更适合视为“未增加成本”的确认，而非单纯节省；`instant()` 测试数量翻倍，覆盖改动导航并防止回归。
- 🛠️ 可通过 `npx skills add vercel/next.js --skill next-partial-prefetching-optimizer` 安装 Skill；前提是应用已使用 Cache Components 和 Partial Prefetching，也可参考官方优化预取指南。

---

### [](https://building.owner.com/project-speed)

**原文标题**: [Project Speed Â· Building @Owner](https://building.owner.com/project-speed)

项目 Speed 是 Owner 为本地餐厅网站进行的一次大型性能重构：用 Astro + Cloudflare Workers 构建的 Apollo 替换 Next.js 的 Mercury，通过边缘渲染、分层缓存、React 岛屿和预渲染显著提升速度，并带来可观的转化与收入增长。

- 🍕 背景：大型连锁餐厅投入巨资打造快速高转化网站，本地披萨店难以竞争；Owner 已扩展到 1 万多家餐厅网站，可用真实流量测试优化效果。
- 🚀 方案：Mercury 因往返渲染、过度取数、第三方脚本和部署清缓存而变慢；Apollo 采用 Astro，默认输出标记、按需加载 React，并深度集成 Cloudflare。
- ⚡ 架构：页面在边缘渲染并缓存，交互部分用 React 岛屿，按 `client:load`、`client:visible`、`client:idle` 水合；营销页少 JS，菜单下单流程集中在单个岛屿。
- 🧱 缓存：请求经过网关 Worker、Workers Cache/分层缓存、R2 HTML 存储，最后回退到 Astro 渲染器；支持 stale-while-revalidate、数据变更推送刷新和请求追踪。
- 📉 性能结果：菜单页 p75 LCP 从 5.4 秒降至 0.7 秒，TTFB 从 600ms+ 降至 200ms 以下，INP 从约 200ms 降至 100ms 以下，JS 包从约 1500KB 大幅降低。
- 📈 商业效果：首页到菜单点击率 +23%，单店收入 +4%，每月基础设施节省 8000–10000 美元；移动 Lighthouse 从 44 提升到 90–99，桌面达到 98–100。
- 🛒 转化提升：Apollo 购物车从“加入商品”到结账的转化约提升 10%；大型菜单餐厅 El Vaquero 的转化提升达 33%。
- 🧪 上线方式：Apollo 与 Mercury 以 50/50 实验并行，分阶段从 8 家、800 家、4800 家扩展到全量；2025 年 11 月完成首单，2026 年 1 月 26 日全量，2 月 9 日公开发布。
- 🛠️ 挑战：实验变体会放大缓存副本，采用随机分组控制；修复 Node 中重复 React 副本；启用 HTTP 103 Early Hints 加速首图加载。
- 🧭 后续：Apollo 已成为 Owner 的建站标准，相关经验复用到 Restaurant Grader 等前端，Owner 将继续借助 AI 加速平台优化。

---

### [死代码不应存在](https://tkdodo.eu/blog/dead-code-shouldnt-exist)

**原文标题**: [Dead Code Shouldn't Exist](https://tkdodo.eu/blog/dead-code-shouldnt-exist)

作者分享了其在多个技术会议上关于“死代码不应存在”的演讲资料，重点介绍如何借助 Knip 逐步删除 28,000 行代码，并提供幻灯片、文字稿及会议录像链接。

- 🎤 演讲主题为《Dead Code Shouldn't Exist: How We Removed 28k Lines of Code, One Knip at a Time》。
- 🌍 今年已在 React Paris、JSHeroes、JSNation、React Norway、React Alicante 和 ZurichJS 等会议演讲。
- 🔗 文中会议名称可链接至对应演讲录像。
- 📑 提供幻灯片与文字稿，支持左右滑动、箭头按钮或方向键切换。
- 🌓 幻灯片会自动适配浅色或深色主题。
- 💬 可通过 Bluesky 联系作者，或在文末留言提问。
- 🔤 文中还推广了代码块使用的等宽字体 Monolisa，并附有 GitHub 与 Bluesky 链接。

---

### [测试 AI 生成的代码：用 Lint 检查模式，测试决策 - Robin Wieruch](https://www.robinwieruch.de/testing-ai-generated-code/)

**原文标题**: [Testing AI-Generated Code: Lint the Pattern, Test the Decision - Robin Wieruch](https://www.robinwieruch.de/testing-ai-generated-code/)

文章主张 AI 生成代码的测试不应按文件堆砌，而应让测试结构匹配代码结构：用 lint 守住“骨架模式”，用共享测试夹具降低测试成本，只在文件作出超出骨架的关键决策时写行为测试，从而形成 agent 可自动执行的反馈闭环。

- 🤖 AI 代理会主动写测试，但常复制 mock、断言 lint 本可检查的模式细节、复述实现，测试很多却难以发现真正 bug。
- 🎯 目标不是“全量测试”，而是让覆盖跟随代码结构：每类文件先 lint 骨架，再有共享 harness，最后只测试有决策的文件。
- 🧱 大多数文件只是固定骨架，例如写处理器：检查会话、调用后端、映射错误、返回结果；纯骨架测试往往只是逐行复述实现。
- 🔍 第一步是用 TypeScript Compiler API 写 lint，检查每类文件的不变量，如会话优先、服务调用在 try 内、catch 映射错误、输入经 helper 返回，并覆盖所有文件，包括未来生成的。
- 🧪 lint 落地分四步：代理先普查候选规则命中情况，先修复所有违规，几乎不豁免地上线，删除已被 lint 覆盖的冗余测试；lint 能即时向 agent 反馈文件、行号和规则。
- 🧰 第二步是为每类文件建一个共享 harness，测试文件只保留场景；写处理器 harness 用内存传输替换网络，保留真实客户端的序列化/反序列化，并统一模拟后端、会话、重定向、缓存等。
- 🛡️ 假后端有三条规则：未实现方法返回 unimplemented；假实现崩溃则测试失败；请求解码遵循生产服务端限制。这还暴露了旧 mock 隐藏的嵌套深度不一致。
- 📜 第三步是在模式文档中写明哪些文件值得测试、测试断言什么；测试只断言离开处理器的请求、返回结果和副作用，不断言已由 lint 覆盖的会话检查或翻译键。
- ✅ 文件只有在作出“决策”时才值得测试，例如分支、读后写、多次写、安全决策、错误重映射；纯骨架文件不写独立测试，表格列、端点等可按需省略某些步骤。
- 🔁 运行闭环是：模式文档作为指令，agent 写/改代码，lint 与共享 harness 测试给出反馈，人类最后审查“变更是否正确、是否被要求”，模式匹配已自动完成。
- 🏭 这体现“软件工厂”思路：agent 按文档化模式生产代码，自动化检查守住规格，人类关注产线本身而非每个文件；测试是其中最容易严格化的工位。
- 💡 结果不是完全测试的代码库，而是每个文件受模式约束、每个存在的测试都有理由；这类测试还曾发现权限 bug，如空 scope 授权、服务端应决定的值来自表单。

---

### [获取失败](https://shift.infinite.red/apple-didnt-invent-the-foldable-it-might-make-you-support-one-7a00c142e77d)

**原文标题**: [Failed to retrieve](https://shift.infinite.red/apple-didnt-invent-the-foldable-it-might-make-you-support-one-7a00c142e77d)

无法总结：获取内容失败，状态码 403。

---

### [](https://bra31k.dev/en/blog/same-bytes-17-percent-faster)

**原文标题**: [How we made a 9 MB WebAssembly module feel faster without removing a single byte — Sergey Patrakeev](https://bra31k.dev/en/blog/same-bytes-17-percent-faster)

Recraft Studio 编辑器通过调整关键资源加载时机，在未删除、未压缩任何字节的情况下，让 9.2 MB 的 WebAssembly 渲染引擎更早开始加载，从而把画布首屏渲染速度提升约 15%–19%。优化约 300 行代码，并经过每组约 1.8 万用户的真实对照实验验证；核心结论是：最大文件不应最后才被发现，性能问题往往藏在指标和加载顺序里。

- 📊 通过自定义性能标记发现编辑器 p75 的画布完整渲染约 8.5 秒，问题此前没有用户投诉或事故暴露。
- 📦 页面下载体积几乎不变：16.75 MB → 16.71 MB；9.2 MB 的 Skia WASM 未删除、未压缩，只改变了开始加载的时间。
- 🐢 旧加载链路中，WASM 的 URL 明明一开始就知道，却要等 JS 解析、实时存储连接、项目数据、基础样式和 React 树遍历后才请求。
- ⚠️ `Stage` 中两个 hook 串行执行，第一个 Suspense 会阻塞第二个，导致字体请求要等 9.2 MB WASM 下载完才开始。
- 🚀 修复手段包括：在页面 head 中预加载 WASM 与字体、把 `initSkia()` 提升到模块作用域、让 `initKit()` 和 `initFont()` 并行、将字体缓存改为幂等 memoized promise、提前发起基础样式请求。
- 🔀 区分 `preload` 与 `prefetch`：编辑器页用 `preload`，项目列表页用 `prefetch`，避免列表页资源竞争。
- 📈 实验结果：Skia 加载 p50/p75/p90 分别 −19%/−18%/−19%，引擎初始化 −17%/−16%/−15%，画布渲染 −18%/−17%/−17%，图片加载 −16%/−16%/−18%。
- ⏱️ 最慢用户收益最大：中位数约节省 670 ms，p90 约节省 1900 ms；但 `loading-state-shown` 一度变差约 120 ms（p75）。
- 🔍 优化后瓶颈转移到网络侧：认证、WebSocket 连接、握手和房间数据获取；主线程大多空闲，WASM 已不在关键路径上。
- 🖱️ 通过代码分割和悬停项目卡片时预取编辑器 chunk，`loading-state-shown` 从 p50 239→36 ms、p75 631→193 ms、p90 1680→708 ms。
- 🧠 关键经验：先定义并埋点真正重要的用户场景指标；相同数据量可快 17%；WASM 体积问题仍存在，作者将在下一篇文章介绍进一步优化。

---

### [像素](https://pixelgui.com/)

**原文标题**: [pixel](https://pixelgui.com/)

Pixel 是一个用于在终端中构建图形应用的开发框架，提供高性能、可嵌入、跨平台的像素级图形能力，并配备 TypeScript React API 与面向 Agent 的开发工具。

- 🚀 快速开始：支持通过 npm、pnpm、bun 使用，命令为 `npm create @zenbu-labs/pixel@latest`
- 🖥️ 演示场景：提供浏览器、VS Code、Zed 等环境中的演示，相关页面包括 terminal-browser.com、terminal-code.com
- ⚡ 核心特性：终端内实现 120 fps 像素完美图形，可嵌入现有 TUI，内置 Chromium WebView 组件
- 🧩 开发体验：跨平台支持，提供 TypeScript React API，并包含 Agent-friendly 开发工具
- 🌍 平台支持：支持 macOS（Apple Silicon、Intel）与 Linux（arm64、x64）；Windows 原生支持仍在开发中，目前可通过 WSL 使用
- 🛠️ 生态应用：terminal-browser 可在终端内运行真实浏览器，显示 4.2k；terminal-code 可在终端内运行 VS Code，显示 2.2k
- 💻 终端兼容：支持 Ghostty、iTerm2、xterm.js、Konsole、WezTerm、Warp、VS Code、Cursor、Mobile SSH、st、wayst、cmux、tty7 等终端
- 📚 资源入口：页面提供 docs 与 examples，便于查阅文档和示例

---

### [TanStack 快捷键](https://tanstack.com/hotkeys/latest)

**原文标题**: [TanStack Hotkeys](https://tanstack.com/hotkeys/latest)

Hotkeys 是一个面向 Web 应用的类型安全键盘快捷键库，提供框架无关核心及 React、Vue、Solid、Svelte、Angular 等适配器，旨在用更少代码处理跨平台、输入框、弹窗、键盘布局和输入法等复杂场景。

- ⚡ **核心定位**：为普通用户提供良好默认体验，为高级用户提供强大快捷键能力，目前处于 beta 阶段。
- 📦 **生态与数据**：框架无关核心加多框架适配器；总下载量 17.6M、周下载量 978,146、GitHub 星标 749。
- 🧩 **解决原生监听痛点**：直接使用 `keydown` 监听很快会因输入框、Windows、德语键盘、弹窗等场景不断打补丁。
- ⌨️ **简化写法**：例如 `useHotkey('Mod+S', save)` 即可替代大量判断逻辑。
- 🖥️ **跨平台修饰键**：用 `Mod+S` 统一表达，Mac 上为 ⌘S，Windows 上为 Ctrl+S。
- 📝 **输入与焦点处理**：在文本框输入时字母快捷键不触发，但 ⌘S、Esc 等仍可用；按钮和菜单保留 Enter、Space、方向键等行为。
- 🌍 **键盘布局与输入法兼容**：支持 Dvorak、AZERTY、俄语等布局，并避免 AltGr、日文输入法等误触发快捷键。
- 🛡️ **类型安全**：快捷键字符串可由编辑器自动补全，错误或不可能的组合会在发布前报错。
- 🪟 **作用域管理**：可将对话框放入独占 scope，使 ⌘S、Esc 等只作用于当前对话框，不影响背后页面。
- 💡 **可发现性与可配置**：按住修饰键可提示快捷键；快捷键列表可同时生成速查表和设置页，并支持用户自定义。
- 🔧 **开发工具**：DevTools 可查看所有已注册快捷键及按键触发情况，便于调试。
- 🤝 **赞助生态**：提供 Gold、Silver、Bronze 合作伙伴及 OSS 赞助商权益，如私有 Discord、优先 issue 和直接支持。

---

### [](https://reactrouter.com/changelog#v850)

**原文标题**: [CHANGELOG.md  | React Router](https://reactrouter.com/changelog#v850)

该页面是 React Router 官方发布与变更日志，覆盖 v7.0.0 至 v8.5.0 的版本说明，汇总各版本的新功能、破坏性变更、不稳定实验特性、性能优化、安全修复和升级注意事项，便于开发者按版本追踪迁移与采用新能力。

- 📦 页面按版本列出发布记录，包括 v8.5.0、v8.4.0、v8.0.0 以及 v7.x 系列，并说明 v6 及更早版本需查看对应分支或 GitHub Releases。
- 🚀 v8 是重要主版本：采用年度主版本节奏，升级最低要求至 Node 22.22.0+、React 19.2.7+、Vite 7+，并改为 ESM-only。
- 🧹 v8 移除 `react-router-dom`，DOM 相关导入需改为 `react-router/dom`；同时移除已弃用的 `meta` 中 `data` 字段，改用 `loaderData`。
- 🧩 v8 将多个 v8 future flags 行为设为默认，包括尾斜杠感知数据请求、透传请求、中间件、Vite Environment API、路由模块拆分等。
- 🆕 v8.5.0 弃用 React Router 的 view transition API，推荐使用 React 19.3+ 的 `<ViewTransition>`；并引入 API-only 模式、自定义 fetch、应用控制路由发现等不稳定能力。
- ⚡ 多个版本包含性能优化：更细粒度路由上下文减少重渲染、更高效路由匹配、缓存路由分支、优化导航与数据请求路径。
- 🛡️ 日志中多次包含安全通告与修复，涉及 CSRF、开放重定向 XSS、ScrollRestoration XSS、文件会话访问、Host/X-Forwarded-Host 处理等。
- 🧪 多版本持续加入不稳定/实验性功能，如 RSC、中间件、路由发现、URL masking、instrumentation、`useRouterState`、`useRoute` 等，并逐步稳定为正式 API。

---

### [渲染策略 | React Router](https://reactrouter.com/start/framework/rendering#api-only-mode-unstable)

**原文标题**: [Rendering Strategies  | React Router](https://reactrouter.com/start/framework/rendering#api-only-mode-unstable)

React Router 文档介绍了三种核心渲染策略，以及实验性的 API-only 模式和独立 API 源配置，重点说明了各自的配置方式、适用场景与部署要点。

- 🧭 三种核心策略：客户端渲染（CSR）、服务端渲染（SSR）、静态预渲染。
- ⚙️ CSR：页面导航始终由客户端渲染；构建 SPA 时设置 `ssr: false`；SSR 设置 `ssr: true`，但需要支持服务端渲染的部署环境，仍可对单个路由进行预渲染或使用 `clientLoader` 在客户端加载数据。
- 🏗️ 静态预渲染：在构建时为指定 URL 列表生成静态 HTML 和客户端导航数据，利于 SEO 和性能，适合无服务端渲染的部署；预渲染时使用路由 `loader` 在构建期获取数据。
- 🧪 API-only 模式（不稳定）：设置 `ssr: "unstable_api-only"`，保留运行时服务器处理 `loader`、`action` 和路由发现，但禁用生产环境的服务端文档渲染；不支持 RSC Framework Mode。
- 📦 API-only 构建行为：未预渲染时生成仅含根 `index.html` 的 SPA 式壳，使用根 `HydrateFallback`；浏览器初始化时请求服务端 loader 数据；路由可直接使用服务端 `loader`/`action`，无需 `clientLoader`/`clientAction` 包装；懒路由发现默认开启。
- 🚀 API-only 部署：可与预渲染组合；需同时部署 `build/client` 和运行时服务端构建，静态资源、预渲染文档和 SPA fallback 由客户端构建提供，`.data` 与路由发现请求交给 React Router 请求处理器；`react-router-serve` 可自动处理。
- 🌐 独立 API 源：API-only 模式可设置 `unstable_apiServerOrigin`；仅作用于 `loader`、`action` 和路由发现请求；源不能包含路径、查询或哈希；需配置 CORS 和 `allowedActionOrigins`；默认使用同源凭据策略，不会自动跨源发送 Cookie；自定义认证头或跨源凭据需参考 Custom Fetch，原生数据预取会绕过自定义 fetch。

---

### [env.style | 环境网站图标](https://www.env.style/)

**原文标题**: [env.style | Environment favicons](https://www.env.style/)

env.style 可帮助你在开发、预览、预发布等不同环境中，通过颜色或自定义图标进行视觉区分，避免混淆当前所处环境，并支持在 Next.js 配置中集成使用。

- 🎨 可为每个环境设置独立颜色，编辑配置时预览会实时更新。
- 🖼️ 支持为任意环境设置自定义图标，缺失图标时会回退为颜色着色。
- ⚙️ 在 `next.config.ts` 中通过 `withEnvStyles` 包装 `nextConfig` 进行配置。
- 🌈 示例颜色包括：development `#3b82f6`、preview `#f59e0b`、staging `#6b7280`。
- 📦 安装命令为 `pnpm add env.style`，文中也列出了 yarn、npm、bun 等包管理器。
- 🧭 核心目标是让你始终清楚当前所处环境，避免环境切换时迷失。

---

### [Tamagui 3：全新的原生运行时、更多原生编译、扁平样式属性、React Strict DOM，以及用于单一跨平台 UI 代码库的 Tailwind 语法。](https://tamagui.dev/blog/version-three)

**原文标题**: [Tamagui 3: a new native runtime, more native compilation, flat style props, React Strict DOM, and Tailwind syntax for one cross-platform UI codebase.](https://tamagui.dev/blog/version-three)

Tamagui 3 以 C++ 原生样式运行时、强化编译器与扁平样式 props 为核心，把更多样式计算移出 React 渲染路径，同时保持 React Native 与 Web 共用一套 UI 代码；并引入 React Strict DOM、Tailwind 前端、Rust 语言服务器、明确优先级层级，同时移除或重命名多批旧 API。迁移时应先运行 codemod 报告，再按升级指南逐项验证。

- 🚀 新增 C++ 原生运行时 `@tamagui/native-registry`：Beta、需 RN 0.82+ 新架构，主题更新经 Fabric 直达原生视图，避免重渲染组件。
- 🧠 编译器增强：支持条件、嵌套三元、多个条件 props、静态 spread、`styled.dynamic()` 与 `.resolve()` 链；静态布局和颜色可提升，动态值保留。
- 🎨 扁平样式 props：base 值与条件写在同一属性中，支持字符串和对象形式，如 `bg="background hover:background-hover"`、`p="4 sm:6"`。
- 🔁 Config v6 将多词主题键改为 kebab-case（如 `border-color`）；提供 codemod，并可用 `settings.styleValueSyntax` 限定字符串或对象语法。
- 🌐 React Strict DOM：用语义化 `html` 元素编写，Web 输出 DOM，原生映射为 React Native 组件。
- 💨 Tamagui Tailwind：`className` 工具类与 Tamagui props 共用编译器、tokens 和 themes；Web 提取原子 CSS，原生解析为 RN 样式。
- 📦 按导入路径区分 styled/unstyled：`tamagui` 提供带默认皮肤组件；`@tamagui/button` 等提供行为与部件；`tamagui/unstyled` 汇总行为层。
- ⚡ 可选零运行时 Web 模式 `experimental.zeroRuntime`：先用 `report` 查看可降级范围，再决定强制；普通编译仍保留必要运行时。
- 🛠️ 新增 Rust 编写的 `@tamagui/lsp` 语言服务器：补全、诊断、hover token、颜色预览；跨编辑器，并用 tree-sitter 提升编辑中容错。
- 🧱 样式优先级分层：base < variants < resolvers < callsite props < `style`；Tailwind `className` 与 callsite 同层，冲突时按属性顺序决定。
- 🧩 引入 `style()`、`styled.dynamic()`、`.resolve()`：复用样式、按单个 prop 动态生成、按完整 props 解析，降低 v2 变体类型复杂度。
- 🗑️ 移除 `focusable`、`fullscreen`、`themeInverse` 等旧 API 与包装器；改用 `tabIndex`、显式布局、`theme="inverse"`、`Theme name="inverse"`。
- 🚫 移除 `$true` token 与运行时 token stepping；控件改用 `xs/sm/md/lg/xl`，间距用显式 token 或数字，`getSize` 等不再自动步进。
- 📏 字体大小区分数字与精确 px：`17` 走平台默认行高，`"17px"` 表示字面像素值。
- 🪟 Sheet 结构显式化：`Sheet.Frame` 拆为 `Sheet.Container` 与 `Sheet.Background`；`Sheet.Overlay` 必须是 `Sheet` 直接子节点。
- 🔄 Dialog/Popover/Select 统一 Adapt 交接：打开状态在 Adapt 之上，Sheet 内容滑出期间保持挂载，部件管理自身动画生命周期。
- 🎞️ 一等动画 API：导出 `useAnimationDriver`、`useAnimatedNumber` 等；`onDidAnimate` 由类型化 `onTransition` 替代；Sheet 支持拖动联动效果。
- ♿ 组件一致性与可访问性增强：更多 `data-state`；Select 支持 `multiple`、`onEscapeKeyDown`、`onInteractOutside`、Separator；Tabs 默认 automatic；Slider 参与表单；Avatar 使用 `delay`。
- 🧾 Field/Form 跨平台校验：自动关联 label/description/error；支持函数或 Standard Schema（Zod 4/Valibot/ArkType）；不延迟提交并聚焦首个无效控件。
- 🎯 Themed 图标按字体尺度解析：`size="4"` 对齐 `font.size.4`；不再直接支持 media/pseudo props；移除内置 `lucide-icons-2`，改用 CLI 按需生成。
- 📜 `@tamagui/scroll-view` 提供干净的 Web 实现，不再经由 react-native-web，覆盖 `scrollTo`、`onScroll`、`contentContainerStyle` 等。
- ⚙️ `optimizeFor` 明确渲染权衡：Web 默认 `updates`，Native 默认 `first-render`；`ThemeUpdate` 支持子树内联主题值，自定义 variables 替代 `defaultProps`。
- 🧰 迁移工具：`@tamagui/cli` 集成 Vite/Metro；先运行 `tamagui check`、flat-values codemod，再搜索旧 API、旧 token 检测与未转换条件，并在 CI 加 `tamagui check --strict`。

---

### [Hydrogen 2026-10 现已发布 - Shopify 开发者博客](https://shopify.dev/changelog/blog/hydrogen-2026-10-is-now-available)

**原文标题**: [Hydrogen 2026-10 is now available - Shopify developer blog](https://shopify.dev/changelog/blog/hydrogen-2026-10-is-now-available)

Hydrogen 2026-10 已正式发布，核心变化是从基于 React Router 的框架转型为框架无关的 JavaScript 商业库，让开发者无需重构即可在现有技术栈中接入 Shopify 商务能力；同时提供 React Router、Next.js 启动模板、面向编码代理的技能，以及可供购物代理使用的标准购物车操作。

- 🚀 2026 年 10 月 14 日发布 Hydrogen 2026-10，正式 GA；自 6 月开发者预览以来已发布 7 个版本。
- 🧩 Hydrogen 现在是框架无关的 JavaScript 库，可添加到任意 JavaScript 框架，无需更换平台。
- 🛒 内置购物车、商品变体、集合筛选、预测搜索、Markets、合规分析、Shop Pay 和客户账户等商务能力。
- ⚛️ 提供 React Router 和 Next.js 启动模板，可部署到任何地方，包括仍然免费的 Oxygen。
- 🤖 包含 20 个编码代理技能，可通过 `npx @shopify/hydrogen@latest setup` 安装，并让代理执行“Set up my store with Shopify”；升级后可用 `skills sync` 同步技能。
- 🛍️ 支持购物代理：在支持 WebMCP 的浏览器中可搜索目录、更新购物车，并由 Shopify Checkout 通过 `complete_checkout` 提交订单。
- 🔗 使用与 Liquid 主题相同的标准 storefront actions，使兼容应用、店面 UI 和代理共享同一购物车契约。
- 🔄 旧版 Hydrogen 店面继续正常工作；迁移时可使用 migration 技能，保留页面和路由，仅替换商务代码来源。
- 🚀 上手方式包括在现有项目中运行 setup 命令、从 Shopify 管理后台部署 React Router 模板到 Oxygen，或克隆 Vercel 维护的 Next.js 商店 Vercel Shop。

---

### [morphicons — 适用于 React、Vue 和 Svelte 的 SVG 图标变形库](https://www.morphicons.com/)

**原文标题**: [morphicons — SVG icon morphing library for React, Vue & Svelte](https://www.morphicons.com/)

Morphicons 是一个可将任意 SVG 图标平滑变形为另一图标的轻量库，支持跨图标库、跨网格以及描边与填充图标之间的转换；它采用弹簧物理动画，零依赖、无需配置，并提供多框架绑定。

- 🧩 支持 Lucide、Tabler、Heroicons、Iconoir、Material Symbols、Phosphor、Hugeicons 等图标集，描边和填充图标均可变形。
- ⚙️ 基于弹簧物理实现平滑、快速、弹跳等动画效果，可调节速度与描边粗细。
- 📦 安装方式为 `npm install morphicons`，运行时依赖为 0。
- 🔀 可在不同图标库、不同网格、描边与填充之间任意变形，并通过 `fitIcon` 适配任意图标集。
- 🎛️ 提供速度预设与参数控制，包括 0.25×、0.5×、1×、2×，以及 stroke 1–2.5。
- 🧮 使用闭式数学求解旋转、缩放和平移的最佳映射；旋转匹配的形状会直接旋转，填充图标按填充形状变形。
- 🧑‍💻 图标以数据形式消费，而非组件：支持 `d` 属性或 Lucide 的 `IconNode` 格式，无需按图标库配置。
- 🛠️ 提供 React、Vue、Svelte、React Native、Astro 绑定及原生 JS，共 5 个框架绑定。
- ✨ 代码使用极简：在 React 中仅需 `<MorphIcon icon={open ? X : Menu} />`，无需包装器、key 或额外配置。
- 📊 gzip 后约 10 KB（含框架绑定）；屏幕上所有图标共享 1 个 `requestAnimationFrame`。
- 🎨 支持 shadcn registry，并适用于任意图标集、任意网格，描边或填充均可。

---

### [Trigger.dev | 持久 AI 智能体的开源平台](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=react-weekly&utm_content=homepage)

**原文标题**: [Trigger.dev | The open source platform for durable AI agents](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=react-weekly&utm_content=homepage)

Trigger.dev 是一个基于 TypeScript 的开源平台，用于构建和部署可持久运行的 AI 智能体与工作流，重点解决长任务、重试、队列、可观测性和弹性扩缩容等问题，并支持实时流式输出与人类审批。

- 🚀 支持构建可承受刷新、重新部署和崩溃的持久 AI 聊天智能体。
- 🛠️ 提供工具调用、人在回路审批、上下文压缩、中途引导和遥测等能力。
- 📡 可将 LLM 响应和运行状态实时流式传输到前端，无需自建 API 路由。
- ⏳ 长任务无超时限制，按实际执行付费，无需管理服务器。
- 🔁 内置自动重试机制，支持按错误、请求响应及任务内部细粒度重试。
- 🧩 支持自主智能体、提示链、路由、并行化、编排器、评估器-优化器等 AI 工作流模式。
- 🐍 构建环境灵活，支持 Python、Prisma、Puppeteer、FFmpeg、apt-get 和自定义 esbuild 插件。
- 📊 提供日志追踪、LLM 可观测性、实时告警、运行筛选、元数据、批量操作和版本管理。
- 🌍 面向生产提供多区域 worker、静态 IP、AWS PrivateLink、并发队列、多环境和弹性基础设施。
- 🔓 Apache 2.0 开源，可自托管，拥有 16.6k+ GitHub stars 和 5.1k+ Discord 社区成员。
- 💬 被 Supabase、Cal.com、MagicSchool AI、Midday 等团队用于可靠运行大规模 AI 工作流。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=reactstatus&utm_term=home&utm_content=Cooperpress)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=reactstatus&utm_term=home&utm_content=Cooperpress)

Expo 是面向“代理式”移动开发的基础设施平台，整合 CLI、MCP、云模拟器、CI/CD、应用发布、OTA 更新与生产监控，帮助团队覆盖从开发、测试到部署和观察的全流程，构建 React Native 与原生应用。

- 🚀 定位为 agentic mobile infrastructure，覆盖开发、测试、部署、监控全流程。
- 🛠️ 提供 Expo CLI、Skills、MCP、Expo Go、Simulators、Launch、Build、Update、Observe、Workflows 等工具与服务。
- 📱 支持用单一代码库构建并发布到 Android、iOS 和 Web，并兼容 React Native、Swift、Jetpack Compose、Kotlin 等原生代码。
- ☁️ 云模拟器可由编码代理按需驱动，自动运行应用、验证结果，并附截图、录屏和日志作为证明，无需 Mac。
- 🔄 Update 支持快速 OTA 更新、渠道与逐步发布控制；Observe 提供崩溃、性能指标和更新采用率监控。
- 🤖 Workflows 可自动执行构建、测试、更新和发布，并支持常见测试套件模板。
- 📦 Expo SDK 发展 10+ 年，提供 100+ 生产级 API，一次安装即可使用。
- 📊 平台规模：300 万+ 开发者、5 万+ GitHub stars、每周 700 万+ 下载、10 万+ 活跃开发者、50 万+ 项目、每日 10 万+ 构建。
- 🌍 80% 的 React Native 开发者选择 Expo，Discord 社区 7 万+ 成员。
- ✅ 获得 Meta 推荐，是 React Foundation 成员，并符合 SOC 2 Type II、GDPR、CCPA、SSO 等要求。
- 💬 开发者评价普遍强调 Expo 简化 React Native 开发、跨平台高效、生态与文档完善、更新部署便捷。

---

