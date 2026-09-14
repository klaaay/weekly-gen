### [](https://react.dev/blog/2026/09/09/react-19-3)

**原文标题**: [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3)

React 19.3 已由 React Team 于 2026 年 9 月 9 日发布到 npm，核心亮点是 View Transitions 与 Fragment Refs 转为稳定，并新增 `browser()`、Trusted Types 支持，以及 Server Components 直接渲染 Context 等能力。

- 🎉 React 19.3 正式发布，View Transitions 和 Fragment Refs 从实验 API 升级为稳定 API。
- 🎬 新增 `<ViewTransition>`，基于浏览器 View Transition API 实现进入、退出、更新、共享元素动画，需在 Transition 中触发。
- 🎛️ 新增 `addTransitionType`，可为同一状态更新标注不同原因，如 `next`/`previous`，从而选择不同动画。
- ⏳ View Transitions 可与 Suspense 集成，用于 fallback、图片和字体加载，推荐 fallback 立即显示、最终内容更新时动画。
- 🧩 Fragment Refs 稳定：可将 `ref` 传给 `<Fragment>` 获得 `FragmentInstance`，对子 DOM 分组执行聚焦、事件、观察、测量和滚动等操作。
- 🌐 React DOM 新增 `browser()`，配合 `use()` 可在服务端触发 Suspense、客户端不挂起，并支持条件调用。
- 🔒 React DOM 支持 Trusted Types API，不再把 `TrustedHTML` 等对象强制转成字符串，有助于防止 DOM 型 XSS。
- 🧵 Server Components 现在可直接渲染从 `'use client'` 模块导入的 `<Context>`，无需额外 Provider 包装组件。
- ⚙️ 其他改进包括：独立渲染 Transition、水合时 Strict Mode 双重调用 Effect、新增 fullscreen、`maskType`、`fetchPriority` 等 DOM 支持。
- 🐛 多项修复：`useDeferredValue` 卡旧值、Suspense fallback 的 Context 传播、Activity 隐藏树问题、`<ViewTransition>` 在 Mobile Safari/SuspenseList 崩溃等。

---

### [扩展不可变性：删除而不丢失数据 | Tigris 对象存储](https://www.tigrisdata.com/blog/soft-delete-deep-dive/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-09-13)

**原文标题**: [Extending immutability: deletion without losing data | Tigris Object Storage](https://www.tigrisdata.com/blog/soft-delete-deep-dive/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-09-13)

overview summary
Tigris 工程博客介绍在全局复制、主动 - 主动对象存储中实现软删除与回收站：删除不会真正丢失数据，而是把元数据移入独立命名空间，可随时恢复；同时用 anti-resurrection 解决跨区域删除与写入冲突，适合误删、勒索软件和代理误删等场景。

- 🗑️ 分布式系统中删除很难：Tigris 是地理复制、主动 - 主动数据库，删除需要墓碑，但还要支持撤销误删。
- ♻️ 软删除让 DELETE 不真正移除数据，数据仍在但主流程不可见，类似 Windows/macOS 的回收站。
- 🧠 S3 的 delete marker 像泄露内部实现；Tigris 选择更高层 API，把软删除做成外部引用而非墓碑。
- 📦 删除对象时，元数据移动到 soft-delete keyspace；数据字节不动，恢复是把同一元数据移回去。
- 🌊 对象和桶是“数据海洋”中的垃圾回收根；软删除元数据仍是 GC 根，只是不出现在普通 ListObjectsV2。
- ⏱️ 跨区域冲突用 Unix 纳秒时间戳和 Last-Write-Wins 处理；如果删除比远端更新新，删除获胜。
- 🛡️ Anti-resurrection 要求任何写入必须证明比删除标记更新；更旧或时间戳相等都会被丢弃，防止对象复活。
- 🧩 通过 S3 API 扩展使用：CreateBucketWithSoftDelete 可设保留天数（默认 7 天，最多 90 天），并支持 ListSoftDeletedObjects、RestoreObject、PermanentlyDeleteObject。
- ⚠️ ForceDeleteBucket 在未启用软删除的桶上会永久删除，需谨慎；软删除桶可列出并恢复整个桶。
- 🚨 重要用例包括防勒索软件、代理误删生产数据、备份误操作；“撤销”按钮让对象存储更安全可信。
- 🌿 若需真正隔离而非恢复，可用 bucket forking，但需在创建桶前启用；软删除可随时在仪表盘开启。
- ✅ 结论：Tigris 为桶启用软删除后，删除最多可恢复 90 天，恢复整个桶只需一次调用。

---

### [玩转 Vercel 的 AI SDK 和 AI Gateway – Master.dev 博客](https://blog.master.dev/having-fun-with-vercels-ai-sdk-and-ai-gateway/)

**原文标题**: [Having Fun with Vercel’s AI SDK and AI Gateway – Master.dev Blog](https://blog.master.dev/having-fun-with-vercels-ai-sdk-and-ai-gateway/)

本文介绍如何使用 Vercel AI SDK 与 AI Gateway 在应用中集成 AI 能力，并以生成健身训练模板为例，展示从安装、调用模型、直连提供商，到用 Zod 约束输出、复用现有 UI 和保存逻辑的完整流程，同时总结免费额度、Azure 报错和可选字段等实践坑点。

- 🧰 Vercel AI SDK 是一个 TypeScript 工具，模型无关，可对接 Claude、GPT 等多种模型，适合把 AI 请求直接集成进应用。
- 🚀 安装简单：`npm i ai`，再通过 Vercel AI Gateway 创建 API Key，并放入 `.env`。
- 🔑 AI Gateway 提供统一入口、集中计费、模型/提供商切换与 fallback，且按官方价格收费、无加价。
- 🧪 第一次请求使用 `generateText`，传入模型名和 prompt，但必须在服务端调用，否则会触发 CORS 错误。
- 🔌 也可以绕过 AI Gateway，直连提供商，例如安装 `@ai-sdk/anthropic` 并使用 Anthropic API Key。
- 🏋️ 真实案例不是做聊天机器人，而是让 AI 生成健身训练模板，并保存到数据库中。
- 📐 通过 Zod schema 约束 AI 输出结构，使生成结果能匹配现有 TypeScript 类型、组件和后端保存逻辑。
- 🛡️ `generateText` 的 `output: Output.object({ schema })` 可指定输出校验结构，返回后还能再次用 Zod parse 做额外验证。
- ✍️ 使用 `instructions` 系统指令限制模型只做训练生成，并在 prompt 中用 XML 标签清晰提供参考训练和用户请求。
- 🖥️ 生成结果复用已有 UI 组件和保存 server function，体现 AI 功能不应破坏组件复用。
- ⚠️ 注意事项：AI Gateway 免费模式有 5 美元额度，但可能无法使用 Anthropic 等模型；购买 credits 最低 10 美元。
- ☁️ 使用 OpenAI 模型时可能遇到 Azure 报错，可通过 `providerOptions.gateway.only` 限制为 `openai`、`anthropic` 等自有提供商。
- 🚫 OpenAI 模型可能因 Zod schema 中存在可选字段而报错，解决方式是移除可选字段或改为必填。
- 🧾 返回结果包含 `usage` 和 `finalStep.providerMetadata?.gateway?.cost`，可用于统计 token 与请求成本。
- ✅ 总体而言，Vercel AI SDK 与 AI Gateway 集成顺畅，输出校验很实用；但慢速 AI 请求更适合放到后台任务而非直接在浏览器等待。

---

### [](https://x.com/aurorascharff/status/2094435532910563659)

**原文标题**: [Aurora Scharff on X: "I rebuilt an older Vercel book search demo with Next.js 16.3 Instant Navigations: https://t.co/aBZonn0E7r

Instant Navigations lets server-rendered routes respond immediately when you click, even on a throttled connection:

𝚌𝚘𝚗𝚜𝚝 𝚗𝚎𝚡𝚝𝙲𝚘𝚗𝚏𝚒𝚐 = {
    𝚌𝚊𝚌𝚑𝚎𝙲… / X](https://x.com/aurorascharff/status/2094435532910563659)

Aurora Scharff 在 X 上分享：她用 Next.js 16.3 Instant Navigations 重建了旧版 Vercel 图书搜索演示，让服务器渲染路由在点击时立即响应，即使网络受限；同时显著优化了首屏加载性能。

- 🚀 使用 Next.js 16.3 的 Instant Navigations 重建 Vercel 图书搜索演示。
- ⚙️ 配置 `cacheComponents: true` 与 `partialPrefetching: true`，启用缓存组件和部分预取。
- 🧩 Cache Components 会预渲染静态、缓存和降级 UI；Partial Prefetching 在导航前把可复用路由 UI 带到浏览器。
- 🔗 对链接添加 `prefetch={true}`，可在点击前解析依赖 URL 的内容；其余内容在服务器加载并流式传入 Suspense 边界。
- ⚡ 筛选器使用 `useTransition` 在服务器更新时淡出目录，并用 `useOptimistic` 立即应用下一组筛选值。
- 📈 重建后初始加载提升：First Contentful Paint 快 44%，Largest Contentful Paint 快 33%。
- 📚 可查看源码并了解更多：next-books.dev。

---

### [Browserslist 在](https://dev.to/alessandro-grosselle/what-browserslist-actually-does-in-nextjs-2hlm)

**原文标题**: [What Browserslist Actually Does in Next.js - DEV Community](https://dev.to/alessandro-grosselle/what-browserslist-actually-does-in-nextjs-2hlm)

文章测试了 Next.js 16 中 browserslist 的实际作用：JS 侧 SWC 只做 legacy/modern 二分且不注入 API polyfill，CSS 侧 Lightning CSS 会按特性细化，但 JS/CSS 的兼容性 lint 都有明显盲区。

- 🧪 实验设置：三个几乎相同的 Next.js 16 项目，唯一差异是 browserslist 目标为 `ie 11`、`chrome 116`、`chrome 139`；均带 `eslint-plugin-compat` 与 `postcss-preset-env`，并逐字节对比构建产物。
- ⚙️ JS 结果：IE 11 被真实降级到 ES5，例如箭头函数、`let/const`、`for...of`、可选链等都被改写；Chrome 116 与 Chrome 139 的输出语法逐字节相同。
- 🧱 SWC 目标逻辑：Next.js/SWC 不按连续 ECMAScript 版本映射，而是二分：legacy 是不支持原生 ES modules 的浏览器，如 IE11；modern 约从 Chrome 61、Safari 11、Firefox 60 起。
- 📉 因此 browserslist 对 JS 只在最旧目标跨过“支持 ES modules”线时有意义；两个现代 Chrome 版本即使相隔几年，也不会改变 JS 输出。
- 🚨 无 API polyfill：即使 IE11 构建，`Array.at`、`Object.hasOwn`、`structuredClone`、`Error.isError` 等仍被直接调用；SWC 只降语法，不注入 `core-js` 等 polyfill，需自行提供。
- 🎨 CSS 结果：Lightning CSS 按特性解析 browserslist，Chrome 116 与 Chrome 139 的 CSS 输出确实不同；例如 `color-scheme: light dark` 在 116 生成 fallback 变量与 `prefers-color-scheme`，在 139 保留原样。
- 🧩 其他 CSS 差异：IE11 会把 `font-family: system-ui` 展开为完整 fallback 栈；CSS nesting 在所有目标中都被展平。
- 🕳️ CSS 盲区：`color-mix()`、`:has()`、`@container` 等缺少机械 fallback 的特性会原样发给所有目标，包括 IE11，可能被静默忽略并造成布局问题。
- ✅ JS lint：`eslint-plugin-compat` 在 `ie 11` 目标下能标记 `Object.hasOwn` 和 `structuredClone`，但对 Chrome 116/139 无报错；`Error.isError` 在三个目标下都漏报。
- ⏳ 局限原因：兼容性插件依赖自身检测数据更新，存在维护滞后，新语法或 API 可能完全漏检。
- 🧼 CSS lint：项目没有配置 browserslist 感知的 CSS linter，`color-mix()`、`:has()`、`@container` 不会被检查。
- 🔭 下一步：作者计划寻找更跟得上新 JS 语法/API 的方案，以及真正的 CSS browserslist linter，来补齐 lint 这一环。

---

### [](https://github.com/vercel/next.js/pull/97864/files)

**原文标题**: [docs: document preloading with Cache Components by aurorascharff · Pull Request #97864 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/97864/files)

overview summary
- 📦 PR #97864“docs: document preloading with Cache Components”已合并到 Next.js canary，包含 12 个提交、改动 3 个文件（+129/−15）。
- 📝 更新 fetching-data 文档：`React.cache` 示例改为用于 ORM/数据库等非 `fetch` 数据访问，同一请求内相同参数调用会复用结果。
- ⚠️ `React.cache` 只在当前请求内生效，不跨请求共享；每次请求都有独立的记忆作用域。
- ⚡ 新增预加载指南：在阻塞工作前不 `await` 调用数据获取函数，让请求提前开始并与阻塞工作并行，避免请求瀑布。
- 🔁 预加载依赖去重：`fetch` 自动 memoize；ORM/数据库用 `React.cache`；Cache Components 用 `'use cache'`，若读取 `cookies()`/`headers()` 等运行时 API 则用 `'use cache: private'`。
- 🧩 预加载函数应靠近消费组件；示例先在页面调用 `preload(id)`，再执行 `checkIsAvailable(id)`，随后 `Item` 渲染时复用同一请求。
- 🗂️ 迁移文档补充：`React.cache` 通常无需改动，但不同 Cache Function 不共享 React cache 结果；跨作用域共享请求工作应改用 `'use cache: private'`。
- 🕒 若仅需请求级去重，可用 `cacheLife({ stale: Infinity })` 避免降低路由 stale 时间；私有缓存结果不会跨生产请求存入服务器缓存。
- 🔐 use-cache-private 文档说明：`'use cache: private'` 可访问 `cookies()`、`headers()`、`searchParams`，结果不存服务器，只保留在浏览器内存且不跨页面刷新。
- 🧱 私有 Cache Function 在请求时运行并排除于静态 shell 生成；stale 至少 30 秒支持 per-link prefetch，至少 5 分钟纳入 App Shell，且不支持自定义缓存处理器。

---

### [Bencho - UI 交互式区块](https://bencho.dev/)

**原文标题**: [Bencho - UI interactive blocks](https://bencho.dev/)

概述：您尚未提供需要总结的文章正文，因此暂时无法提炼关键要点。
- 📭 当前输入为空，未检测到可总结的文本内容。
- 📝 请在下一条消息中粘贴完整文章或内容。
- ✅ 收到内容后，我会按“概述 + Emoji 要点”的格式生成中文摘要。

---

### [](https://next-safe-action.dev/)

**原文标题**: [next-safe-action](https://next-safe-action.dev/)

next-safe-action 是一个面向 Next.js 的类型安全、带验证与中间件支持的 Server Actions 库，支持所有符合 Standard Schema 规范的验证器，旨在提供端到端类型安全与更佳开发体验，GitHub 约 3.1K stars，可通过 `npm i next-safe-action` 快速安装。

- 🛡️ 为 Next.js Server Actions 提供端到端 TypeScript 类型安全，从 schema 定义到 React hooks 均可自动推断，无需手动连接类型。
- ✅ 支持 Standard Schema v1，兼容 Zod、Valibot、ArkType、Yup 等验证器。
- 🧩 提供可链式 `.use()` 中间件，支持类型化 context 传播，可实现鉴权、限流、分析等逻辑。
- ⚛️ 提供 `useAction` 与 `useOptimisticAction` React hooks，支持丰富状态跟踪与回调。
- ⚠️ 智能错误处理：优雅处理验证错误、服务器错误和 Next.js 导航错误，并返回类型化结果。
- 🔄 内置乐观更新，支持服务器 action 失败时自动回滚。
- 🚀 上手简单：创建 action client、定义 action、配合 hooks 使用即可。
- 💬 开发者评价积极：常与 react-hook-form、zod、shadcn/ui、Sentry 等搭配，被誉为 Next.js 表单与 Server Actions 的绝佳组合，甚至可替代 tRPC 的类型安全方案。
- ❤️ 项目由赞助者支持，包括 Vercel 及多位个人赞助者，官网、GitHub 与 npm 提供文档和安装方式。

---

### [pdfcn - 精美的 PDF，轻松制作](https://www.pdfcn.dev/)

**原文标题**: [pdfcn - Beautiful PDFs, made simple](https://www.pdfcn.dev/)

overview summary
这是一套面向 React 的即用型、可定制 PDF 组件，基于 Takumi 与 Forme 构建，通过 shadcn 分发；新增主题构建器，让美观 PDF 的制作更简单。

- 🆕 新增主题构建器：简化美观 PDF 的创建流程。
- 📄 提供 React 即用型、可自定义的 PDF 组件。
- 🛠️ 基于 Takumi 和 Forme，通过 shadcn 分发。
- 💻 支持 bun、npm、pnpm、yarn 安装与使用。
- ⌨️ 示例命令：`pnpm dlx shadcn add @pdfcn/forme/alert`。
- 🚀 提供 Get Started 与 Browse Components 入口。
- 🧾 可选基础文档：企业发票、财务报告、极简发票。
- 👀 支持模板选择、预览与代码查看。
- 🧱 使用 6 个组件：页眉、键值、表格、区块、文本、页脚。
- 🏷️ 页眉组件：带品牌 logo、公司信息与文档标题的文档头。
- 📥 安装页眉示例：`pnpm dlx shadcn@latest add @pdfcn/takumi/page-header`。

---

### [](https://github.com/shadcn-ui/cn)

**原文标题**: [GitHub - shadcn-ui/cn: cn is a new engine for Tailwind class merging and conflict resolution. It replaces tailwind-merge and clsx. Same APIs. Full parity. And it is 30× faster. · GitHub](https://github.com/shadcn-ui/cn)

cn 是 shadcn 与 aidenybai 联合打造的全新 Tailwind 类名合并与冲突解决引擎，作为 tailwind-merge 和 clsx 的直接替代品，保持完全相同的 API 与输出，同时性能提升约 30 倍。

- 🚀 **全新引擎**：cn 是用于 Tailwind 类名合并和冲突解析的新引擎，完全替代 tailwind-merge 与 clsx
- ⚡ **性能飞跃**：组件常见调用从 320ns 降至 10ns，实际代码库几何平均快 37 倍，最快场景达 172 倍
- 🧩 **API 完全兼容**：twMerge、twJoin、clsx 等函数同名同行为，356,000 个差分测试验证输出一致
- 🪶 **零依赖且框架无关**：适用于 React、Vue、Svelte、Solid、Astro 及纯服务端模板，支持浏览器、Node、Bun、Deno 和边缘运行时
- 📦 **开箱即用**：`npm i cn` 后直接导入即可，无需额外配置；迁移命令为 `npx shadcn@latest migrate cn`
- 🔁 **平滑迁移**：可一键替换 shadcn/ui 项目中 `@/lib/utils` 的 cn 包装，或手动将导出行改为 `export { cn } from "cn"`
- 🎨 **自定义主题支持**：cn/config 接受与 tailwind-merge 相同的 `{ extend, override, prefix }` 结构，自定义校验函数照常使用
- 🧮 **内置学习缓存**：能识别重复调用序列，命中缓存时按引用校验直接跳过计算
- 🛠️ **多样化模块**：提供 cn/engine、cn/lite、cn/build、cn/vite、cn/next 等，支持构建期编译与打包插件
- ⚠️ **注意事项**：支持 Tailwind v4；v3 项目应继续使用 tailwind-merge v2；Cn build 无法识别动态拼接类名，需用 `--safelist`；CLI 需 Node 20+
- 📜 **开源与致谢**：MIT 许可，合并语义沿用 tailwind-merge（Dany Castillo），join 层实现 clsx（Luke Edwards）语义，并重写了 cnfast（Aiden Bai）的缓存优化

---

### [Tailwind](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

**原文标题**: [Tailwind Labs is joining Shopify - Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

Tailwind CSS 创始人宣布 Tailwind 正式加入 Shopify。此举旨在为这个每周安装量超过 1.1 亿次、被众多大型公司使用的框架提供稳定长期的归属，并继续积极维护。开源项目与许可方式不变，商业业务将不再扩张，团队会更聚焦于在 Shopify 内开发 Tailwind CSS。

- 🚀 Tailwind 加入 Shopify，为其提供长期稳定的发展家园。
- 📈 从九年前的个人项目起步，如今每周安装超 1.1 亿次，被 ChatGPT、X、Cloudflare、Reddit、Shopify 等采用。
- 🏠 加入 Shopify 是为了让 Tailwind 持续被积极维护，服务数百万依赖它的开发者。
- 🛍️ Shopify 提供真实复杂的产品场景：商家店铺与后台、顾客购物结账、Shop App，以及代理式商务探索。
- 🤝 Shopify 是最早大规模采用 Tailwind 的公司之一，并将其视为技术栈中的关键部分。
- 💡 创始人认同 Shopify 帮助更多人创业的使命，认为创业改变了自己的人生。
- 🔓 Tailwind CSS 及其他开源项目不会改变，仍保持 MIT 许可，团队将在 Shopify 支持下继续主导维护。
- 💼 商业侧不再围绕 Tailwind 扩张业务；现有客户保留 Tailwind Plus 和 ui.sh 访问权，但关闭新用户注册，聚焦 Tailwind CSS。
- 🙏 感谢过去九年里所有使用和支持 Tailwind 的人。

---

### [Prisma 8 是否已为长期运行的生产应用做好准备？](https://www.prisma.io/blog/is-prisma-8-ready-for-long-lived-production-apps)

**原文标题**: [Is Prisma 8 Ready for Long-Lived Production Apps?](https://www.prisma.io/blog/is-prisma-8-ready-for-long-lived-production-apps)

Prisma 8 首席开发者 Will Madden 回应 Reddit 关于其架构重写、商业动机和迁移模型的担忧，强调 Prisma 8 是面向智能体时代的可扩展 ORM，核心组件可替换，ORM 仍将保持 Apache-2.0 且不与商业产品耦合；迁移系统更透明、可审查，并适合多分支并行开发。

- 🧭 Prisma 8 是全新产品架构，目标是成为“首个智能体原生 ORM”，面向开发者与 AI 智能体协作开发。
- 🧱 Prisma 7 是单体 Rust 引擎，复杂难维护，核心团队成为瓶颈；Prisma 8 用可扩展框架取代它。
- 🔌 Prisma 8 核心默认不了解任何数据库，Postgres、MongoDB 等都是扩展；查询构建器、ORM 客户端和契约源也可替换。
- 🧩 社区和第三方可自行添加数据库支持、中间件、验证库集成或契约格式，不再完全依赖 Prisma 核心团队。
- 💰 商业产品用于资助开源开发，但 ORM 将保持 Apache-2.0，不会闭源、不会削弱功能，也不会被限制来衬托付费产品。
- 🛡️ ORM 本身不含 Prisma Cloud 逻辑；核心不耦合商业服务，托管工具始终是可选项。
- 🗃️ 迁移系统强调透明：每个迁移目录都有 ops.json，Postgres 操作是字面 SQL，可用 migration show 查看。
- 🧾 引入 migration.ts 简化并增强自定义迁移，pre-checks 和 post-checks 让操作幂等，降低常见迁移风险。
- 🌳 通过契约签名哈希将迁移组织为图，而非线性列表，减少多分支开发中的迁移顺序冲突。
- 🔄 迁移可机械地合并或拆分，未来 squash/split 命令尚未发布，但格式已为此设计。
- ⏳ 作者认为 Prisma 8 的范式不会再发生根本性变化，未来大版本可能改 API，但不会重写架构。
- ⚠️ Prisma 8 目前是 RC，正式 8.0.0 预计 4 至 8 周后发布；RC 仍可能有破坏性变更，但会提供升级配方。
- ☁️ Prisma 自家云平台 API 已运行在 Prisma 8 上，作者认为实际使用值得。
- 🔄 使用 Prisma 7 + PostgreSQL 的团队可增量迁移，Prisma 8 与旧版本可并行运行；Prisma 7 将继续获得 12 个月修复与安全更新。
- 💬 更多问题可在 Prisma 公共社区 Discord 中讨论。

---

### [](https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md)

**原文标题**: [How our agents build on-brand pages with design.md - Vercel](https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md)

Vercel 团队分享了他们如何打造 design.md——一个公开的设计指导文件，让代码库之外的编码代理也能生成符合 Vercel 品牌风格的报告、提案和一次性页面。文章讲述了从 product-design 技能到公开文件的演进、由指导文件 + 样式表 + 评估循环组成的三部分系统、基于真实场景的迭代验证，以及如何用实际反馈持续维护这套机制。

- 🎨 Vercel 广泛使用编码代理设计和构建页面，字体、色彩与构图都必须承载与官方页面相同的设计判断。
- 📁 原有的 product-design 技能存放在各代码库中，代理可读取设计系统与产品指南，但无法用于代码库外、在无法读取这些文件的工具中制作的报告、提案和一次性页面。
- 🔗 为此推出 design.md：一个任何代理都能通过单一公开 URL 加载的公共文件。
- ⚠️ 最初直接把 product-design 移植成公开提示词，但不同模型对同一描述解读迥异，生成页面差异巨大；设计语言本就主观（如“简洁”含义模糊），且缺少真实组件与已发布示例的语境。
- 🧪 于是搁置移植、从头重写，并用 7 个取自真实用例的评估提示反复测试：使用与性能报告、续约提案、基准报告、交互规划页、自建对比购买简报、安全治理简报、演示文稿。
- 🔄 首次对比中，相同提示、数据、模型与视口下，无 design.md 生成通用 SaaS 仪表盘；有则让页面以续约建议开头、整合商业证据、统一对比尺度，证明它改变的不只是样式，还有结构与层级。
- 🧩 系统最终形成三部分：design.md 提供指导，公开样式表定义受限且文档化的类与 token 词汇，评估循环把人工反馈转为规则与确定性检查。
- 📝 design.md 编码的判断涵盖：兼顾快速执行阅读与详细审计的页面塑造、具体声明与诚实注意事项的文案、层级排版色彩的协调，以及发布规范（含字标与三角 logo 的资产规则）。
- 🚫 它还明确命名应避免的生成式设计模式，让代理更可靠地识别并规避。
- 💾 样式表把设计系统基元（标题、表格、数据条、图表样式）打包为公开 CSS，代理只需在 HTML 中使用文档化的类名而非重造；且代理本身不读取样式表，节省上下文空间。
- ✅ 评估循环中，确定性检查捕捉机械故障（如表格忽略可用宽度），人工则判断层级、构图等无法自动化的主观部分。
- 🔁 每条指导都经评估循环赢得位置：提示与模拟输入冻结为场景，完整轮次覆盖全部 7 个场景并跑 Claude Opus 4.8 与 Codex with GPT-5.5，比较显示同一视觉语言下各页面结构围绕读者任务而变，而非被推向同一模板。
- 🛠️ 审查用本地应用展示全页渲染并做盲测 A/B，每次运行记录提示、输入、模型配置、design.md 版本、截图与反馈。
- 📌 修正落在最窄且能持续强制执行处：判断进 design.md 散文，可复用机制进样式表，可机械检查的写成代码检查；单模型失败除非重复出现否则不入规则。
- 📊 例如商业条款表被挤成正文宽度后，同一问题在历史输出中普遍存在，便同时加入 design.md 规则与确定性检查，后续续约提案页面恢复全宽表格。
- 📈 效果测量：超过 200 次运行后，3 个桌面场景各由 Codex with GPT-5.5 生成两次（有/无 design.md），已知失败从 91 次降至 39 次，减少 57%；但检查只能发现已记录的失败，6 页样本过小，且每页都仍有至少一个严重到阻止发布的失败。
- 💬 保持更新靠真实使用：Slack 中的 @design-agent（基于 eve）接受设计评审、文案替代、图标推荐、粘贴数据生成报告站点等请求，自动加载当前 design.md 并回传截图与部署 URL。
- 🗂️ 每周汇总 Slack 线程、GitHub 评审与 Figma 评论，自动化归类重复意见为提议变更，由人决定归属（agent、product-design 技能、design.md、样式表或检查），新页面类型成为新评估场景；通过追踪同类投诉数量是否下降验证效果。
- 🧭 自建指南：选一个重复人工制品并写下评分标准；先保存无新上下文的基线；把最近十次修正改写成可观察规则汇入一个文件；用样式表约束可重复机制；用相同输入做一次有/无文件的盲测对比；根据输出与后续人工干预编码修正。
- ⚙️ 手动循环见效后再加工具：纳入该适用与不该适用的场景、保留隐藏测试集、记录模型与指导版本、自动化机械检查、多盲审，但最终变更仍需人工审查。
- 🌐 Vercel 的 design.md 已公开，日常加载进 v0、Codex 与 Claude，并提供 eve 设计代理模板。
- 🙌 贡献者：Kevin Corbett。

---

### [](https://x.com/tan_stack/status/2094888852607652280)

**原文标题**: [TANSTACK on X: "🏝️ + ▲ = 🚀

TanStack and @Vercel are officially teaming up!

We’re working together to make Vercel a first-class home for TanStack Start with better support for deploying and running anything you can dream up with TanStack on Vercel.

Start here! 👇

https://t.co/cKNJ6z70gr" / X](https://x.com/tan_stack/status/2094888852607652280)

TanStack 与 Vercel 宣布正式合作，将共同把 Vercel 打造为 TanStack Start 的一流平台，并增强在 Vercel 上部署与运行 TanStack 项目的支持。

- 🤝 TanStack 与 Vercel 正式联手合作。
- 🏝️ + ▲ = 🚀 用表情符号宣告合作，寓意双方结合带来加速体验。
- 🎯 目标是将 Vercel 打造成 TanStack Start 的首选家园。
- 🛠️ 双方将改善在 Vercel 上部署和运行各类 TanStack 应用的支持。
- 🔗 推文附有入门链接：vercel.com/kb/guide/deplo…。
- 📅 推文发布于 2026 年 9 月 1 日晚 8:43。
- 📊 该推文浏览量约 262.6K，互动包括 110 条回复、150 次转发、2.4K 点赞和 261 次收藏。

---

