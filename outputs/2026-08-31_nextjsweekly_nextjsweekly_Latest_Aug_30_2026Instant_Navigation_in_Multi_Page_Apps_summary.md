### [](https://dev.to/alessandro-grosselle/what-nextjss-instant-navigation-looks-like-in-a-multipage-application-34dl)

**原文标题**: [What Next.js's instant navigation looks like in a multipage application - DEV Community](https://dev.to/alessandro-grosselle/what-nextjss-instant-navigation-looks-like-in-a-multipage-application-34dl)

概述：本文探討了 Next.js 16.3 的「即時導航」功能在傳統多頁應用（MPA）中的適用性。作者將 SPA 示範專案 next-beats 改寫為 MPA 版本，逐步對比各項新功能與瀏覽器原生替代方案，並指出記憶體洩漏、第三方腳本等遷移障礙，最終認為瀏覽器本身已提供多數 MPA 等效機制。

- 🚀 Next.js 16.3 的即時導航主打 SPA 形態，作者透過 fork next-beats 建立 MPA 版本，逐項驗證哪些功能對 MPA 真正有用。
- ⚠️ 為何不直接遷移到 SPA？第三方腳本（分析、廣告）依賴 DOMContentLoaded 與整頁重新整理；且 SPA 中未清理的監聽器與計時器會持續累積，記憶體問題只是被隱藏而非解決。
- 🔄 View Transitions：SPA 用 React 的 `<ViewTransition>` 做路由淡入淡出；MPA 可用純 CSS `@view-transition { navigation: auto; }` 達成跨文件過渡，無需 JavaScript。
- 🔍 懸停預取：next/link 的 hover 預取在 MPA 中不可用；改用瀏覽器原生的 BFCache（返回/前進快取）與 Speculation Rules API（基於懸停/指標意圖預取或預渲染）。
- ⚙️ Speculation Rules 僅 Chromium 支援，其他瀏覽器會忽略該 script 標籤，因此可優雅降級，但非 Chromium 用戶無法享受完整優勢。
- 🗃️ `use cache` 在 MPA 同樣適用，但若後端為外部微服務，建議先優化後端/API 層快取，再考慮在 Next.js 應用層加入此機制。
- 📊 總結表格：SPA 功能與 MPA 原生替代一目了然，完整 diff 可對照參考。
- 💬 留言指出「記憶體問題被掩蓋而非修復」是常見盲點，並質疑預渲染規則可能導致分析腳本重複觸發。

---

### [](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-08-30)

**原文标题**: [A fully-featured TypeScript SDK for storage — one portable interface across different providers](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-08-30)

storagesdk 是一个面向多存储提供商的统一 TypeScript SDK，内置快照与分支能力，为人类和 AI 代理提供一致的存储体验，并提供 CLI 与丰富集成。

- 🚀 统一 API：通过一个 SDK 访问 Tigris、S3、R2、GCS、Azure、MinIO、GitHub 等 12+ 提供商，切换只需更改导入，调用点不变。
- 📸 快照与分支：内置原生快照和分支功能，分支可作为代理独立沙箱，合并或丢弃轻松实现，快照确保每个运行可从冻结状态复现。
- 🤖 AI 代理集成：可直接对接 Vercel AI SDK、Mastra，或启动 MCP 服务器；工具描述会引导模型在风险编辑前快照、分叉尝试变体。
- 🖥️ 命令行工具：@storagesdk/cli 封装所有适配器，提供 ls、stat、cat、cp、mv、rm、sign 等熟悉命令，支持 storage:// 路径和 --adapter、--fork 参数。
- 🔄 流式传输：支持 Web ReadableStream 上传/下载，背压与中止信号端到端传播。
- 🔗 签名 URL：默认预签名 PUT，也支持 POST 并指定 maxSize/contentType 来增强安全边界。
- 🛠️ 逃逸口：通过 storage.raw 访问原生客户端，类型完全推断，无需类型断言或 any。
- ⏹️ 中止控制：所有操作支持 AbortSignal，取消上传、列表、快照等不会提交部分写入。
- 🧩 类型化错误：StorageError 提供 NotFound、Conflict、Aborted、NotSupported 等可移植错误码，方便跨适配器处理。
- 📦 现代轻量：ESM-only、Node 20+，核心零运行时依赖，各适配器原生 SDK 作为可选对等依赖。
- 🌟 开源免费：Apache 2.0 许可，由 Tigris 团队构建，旨在为所有人和代理提供更好的存储体验。

---

### [2026 年 8 月安全更新 | Next.js](https://nextjs.org/blog/august-2026-security-release)

**原文标题**: [August 2026 Security Release | Next.js](https://nextjs.org/blog/august-2026-security-release)

概述：Next.js 于 2026 年 8 月发布了紧急安全更新，修复两个严重漏洞。受影响版本包括 Active LTS v16.3.3 和 Maintenance LTS v15.5.24，建议用户立即升级。

- 🚨 紧急发布：因上游依赖中发现新的严重漏洞，原定安全更新提前发布。
- 🛠️ 修复版本：Next.js 16.3.3（Active LTS）和 15.5.24（Maintenance LTS）现已可用，请尽快升级。
- 🖼️ 漏洞一：Image Optimization API 在处理 AVIF 图像时存在未认证远程代码执行（严重）——依赖库 libheif 漏洞，修复版已禁用 AVIF 优化。
- 💻 漏洞二：Windows 服务器上的未认证远程代码执行（严重）——影响同时使用 Pages Router 和 App Router 且未启用 Cache Components 的应用；Linux/macOS 不受影响，暂无临时方案。
- 🛡️ 安全计划：Vercel 开源漏洞赏金计划招募研究人员，可通过 security@vercel.com 联系安全问题。

---

### [](https://aurorascharff.no/posts/avoiding-server-component-waterfall-fetching-with-react-19-cache/)

**原文标题**: [Avoiding Server Component Waterfall Fetching with React 19 cache() | Aurora Scharff](https://aurorascharff.no/posts/avoiding-server-component-waterfall-fetching-with-react-19-cache/)

本文介绍了 React 19 的 `cache()` API 在 Next.js App Router 中的应用，展示了如何通过缓存数据获取结果、减少数据耦合，并利用预加载模式避免服务器组件中的瀑布流请求，同时讨论了隐藏耦合问题及 Cache Components 的新方案。

- 🚀 React 19 的 `cache()` API 可缓存数据获取或计算结果，实现每次服务器渲染中的 memoization。
- 🔄 它能让你在多个组件中安全地重复调用同一数据请求，无需手动提升数据获取，从而保持组件解耦。
- 💧 典型问题：父组件 `await` 数据会阻塞子组件，即使子组件不依赖该数据，也会形成瀑布流请求。
- ⚠️ 简单修复（如 `Promise.all` 提升获取）会引入数据耦合，且慢请求仍可能阻塞页面。
- 🧠 核心解法：用 `cache()` 包裹数据函数，并在高层组件中调用（不 `await`）以预加载数据，子组件随后可复用结果。
- ⏳ 预加载时千万别 `await` 预取函数，否则会阻塞渲染，失去并行效果。
- 🔗 预加载模式存在隐藏耦合：重构时可能留下无用请求；建议导出 `preloadComments` 这类明确命名的辅助函数。
- 📌 若使用 Next.js 的 `fetch()`，其已内置请求 memoization，无需 `cache()`；后者更适合数据库或自定义请求。
- 🆕 Cache Components 提供了 `"use cache: private"` 作为新预加载方式，适用于需要请求特定值（如 session）的函数。
- 🔑 关键结论：`cache()` 能优化性能、减少耦合，但需谨慎选择使用位置，避免过度设计导致复杂度上升。

---

### [](https://svar.dev/blog/how-to-build-event-calendar-with-nextjs-and-svar/)

**原文标题**: [Build Event Calendar with Next.js & React | SVAR Blog](https://svar.dev/blog/how-to-build-event-calendar-with-nextjs-and-svar/)

overview summary  
- 📘 教程介绍如何在 Next.js 应用中集成 SVAR React Calendar，实现带日程管理的事件日历。  
- ⚙️ 涵盖安装、样式、布局修复、编辑器、后端集成、数据保存、错误处理等完整流程。  
- 🔗 最终实现具备日/周/月视图、拖拽事件、侧边编辑器和服务器同步的日历应用。  

- 🚀 SVAR React Calendar 是开源 React 日历库，支持自定义、多种视图、拖拽管理、内置编辑器及 PRO 扩展功能。  
- 🛠️ 使用 `create-next-app` 创建 Next.js 项目，并安装 `@svar-ui/react-calendar` 包。  
- 🎨 导入 `all.css` 获得完整样式，并用 `Willow` 主题包裹组件。  
- 📐 解决布局问题：设置 `html, body, .wx-theme` 高度为 100%，使日历填充容器。  
- ⚠️ 处理水合警告：通过 `useState` + `useEffect` 仅客户端渲染日历，避免 SSR 不匹配。  
- 🗂️ 添加 `Editor` 组件，通过 `init` 回调获取 API，实现事件详情编辑（描述、时间、全天）。  
- 🗄️ 使用 `better-sqlite3` 建立 SQLite 数据库，存储事件数据，并自动初始化示例数据。  
- 🌐 创建 REST API 路由（GET/POST/PUT/DELETE），供前端通过 `RestDataProvider` 交互。  
- 🔄 `RestDataProvider` 自动获取事件并转换日期，通过 `api.setNext(server)` 将创建、编辑、拖拽等操作映射为 HTTP 请求。  
- 🖱️ 拖拽/调整事件大小自动触发 `update-event`，发送至 `PUT /events/{id}`，无需额外处理。  
- 🧰 内置工具栏提供添加事件、日期导航、今日按钮和视图切换，所有操作走同一数据管道。  
- 🛡️ 错误处理：加载失败用 `.catch`，保存失败可监听错误动作或重载数据；可继承 `RestDataProvider` 覆写 `send` 集中处理。  
- 📋 完整组件代码示例，并提醒在 `next.config.ts` 中将 `better-sqlite3` 设为外部包。  
- ✅ 教程总结：仅需编写 REST 端点，日历 UI 和数据同步由组件与 Provider 负责。  
- 🔗 下一步：查看文档、演示和 GitHub 仓库，或探索 PRO 版高级功能（时间线、资源视图、循环事件等）。

---

### [](https://github.com/vercel/next.js/pull/96832)

**原文标题**: [Add experimental Variants by unstubbable · Pull Request #96832 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/96832)

该 PR 为 Next.js 引入实验性 Variants 功能的早期草稿实现，目标是把“按请求解析的变体值（主题、locale、功能开关等）”变成可预渲染的路由维度，并将原先需要手工 proxy 重写和路径编码的样板工作收进框架；附带大量路由、缓存、构建输出及测试改动。

- 🧪 新增 `experimental.variants` 特性开关，完全向后兼容，未启用的项目不受影响。
- 🔑 Variant 是每请求解析的值，在 `'use variants'` 模块中通过 `variant()` 声明，并用 `generateStaticVariants` 声明需要预渲染的组合。
- 🏗️ 每个声明的变体组合都会生成独立预渲染产物；未声明的值只作为动态洞保留，避免缓存条目随请求值无限膨胀。
- 🔀 方案取代手工 proxy 重写、将决策编码进路径、迁移 `[variantCode]` 段等做法，读取时只需在 Server Component 中 `import` 并 `await`。
- ⚠️ 当前为早期迭代：缺少 Client Components 支持，`decide` 签名、`variant()` 自身标识、`wrapProxy` 等临时脚手架后续会被 Turbopack transform 取代。
- 🛣️ 内部通过哈希路径与 `x-next-internal-variants` 头传递变体值，使 CDN 缓存可按组合分区，并支持 base path。
- 🧮 引入变体组合排序、哈希与校验，以及 `withVariants`/`generateStaticVariants` 等 API，使每个组合拥有独立缓存键和 manifest 条目。
- 🔒 安全修正：拒绝客户端伪造的变体前缀或查询参数，并要求变体读取必须位于 Suspense boundary 之下，避免空壳预渲染被意外复用。
- 📉 性能指标：Turbo 构建时间 -7%，Webpack 构建时间 +3%，`node_modules` 体积 +1.69MB，整体略有回归。
- 🧪 新增大量 e2e 测试，覆盖 dev/production/部署、base path、按需参数、adapter 路由折叠、外部 rewrite 等场景，并修复多处理失败测试。
- 🔄 PR 包含 34 个 commits，多次 force-push，过程中回退了一个提交，最终仍为草稿状态。

---

### [Zod 4.5](https://zod.dev/blog/zod-4-5)

**原文标题**: [Zod 4.5](https://zod.dev/blog/zod-4-5)

overview summary
- ⚡ 全新 `z.compile()` 可预编译任意 schema，解析速度提升约 3–9 倍，并支持全局自动编译（`import "zod/compile"`）。
- 💳 新增 `z.creditCard()` 字符串格式，校验 12–19 位数字及 Luhn 校验和。
- 🧩 新增 `z.properties()`，可对 `z.instanceof()` 等多属性 schema 批量添加检查。
- 📦 恢复 `z.deepPartial()` 函数形式，支持深层可选字段，并保持 `ZodObject` 特性。
- 🎯 新增 `.exactPartial()`，字段键可省略但显式 `undefined` 会被拒绝，匹配 TS 的 `exactOptionalPropertyTypes`。
- ✅ 新增 `z.validate()` 快速布尔校验，无效输入时比 `.safeParse()` 快最多 16 倍。
- 🔄 新增 `z.input()` / `z.output()`，可独立验证 codec 的输入/输出侧。
- 🏷️ 新增 `z.toZod<T>()`，帮助定义与静态类型完全一致的 schema。
- 🍎 新增 `z.getDiscriminatedOption()`，按判别值提取联合成员。
- 🔁 递归 schema 现支持循环输入（Zod Mini 需显式注册 memoizer）。
- 🧠 Schema 内存占用减少 9 倍（`z.string()` 从 7.5kb 降至 784 bytes）。
- ⚡ `.safeParse()` 失败路径不再捕获堆栈，速度提升约 7.5 倍。
- 🔑 `z.object()` 支持 symbol 键，TS 推断为 `unique symbol` 且必填。
- 🐛 多项破坏性修复：`z.iso.datetime()` 强制要求秒、字符串长度按 Unicode 码点计算、record 键与 TS 对齐、`__proto__` 始终剔除、IP/ULID/URL/emoji 等格式更严格。
- 🌍 新增 8 种语言区域：孟加拉语、中库尔德语、印地语、卡纳达语、新挪威语、巴西葡萄牙语、斯洛伐克语、土库曼语。
- 🤝 汇总 155 个提交，感谢所有贡献者。

---

### [](https://github.com/47ng/nuqs)

**原文标题**: [GitHub - 47ng/nuqs: Type-safe search params state manager for React frameworks - Like useState, but stored in the URL query string. · GitHub](https://github.com/47ng/nuqs)

nuqs 是一个用于 React 框架的类型安全 URL 查询字符串状态管理库，类似 useState 但将状态存储在 URL 中，支持 Next.js、Remix、React Router 等多种框架，提供解析器、默认值、历史模式、服务器缓存等功能。

- 🔀 支持多种框架：Next.js（app/pages 路由）、React SPA、Remix、React Router v6/v7/v8、TanStack Router，并可通过适配器自定义。
- 🧘‍♀️ 简单设计：URL 是唯一状态来源，使用 `useQueryState` 即可读写查询参数。
- 🕰 历史模式：默认替换历史记录，可设置为 `push` 以支持返回按钮导航状态更新。
- ⚡️ 内置解析器：提供字符串、整数、浮点数、布尔值、时间戳、ISO 日期、数组、JSON、枚举和字面量解析器，也可自定义 parse/serialize。
- 🎯 默认值：通过 `.withDefault()` 设置默认值，URL 缺失时返回默认值，设为 `null` 则移除查询键。
- 📡 Shallow 模式：默认仅客户端更新，可设为 `false` 通知服务器重新渲染（仅 Next.js）。
- 🚦 节流更新：内部更新 URL 默认节流 50ms，可通过 `throttleMs` 调整，保证 UI 响应即时。
- 🔄 过渡支持：结合 `shallow: false` 和 `startTransition` 获取服务器更新时的加载状态。
- 📦 批量更新：同一事件循环内多次 setState 会合并异步写入 URL，返回可等待的 Promise 获取最终 URLSearchParams。
- ♊️ useQueryStates：同时管理多个相关查询参数，支持一次性设置部分或全部键。
- 🗃 服务端加载器：`createLoader` 可一次性解析查询字符串；`createSearchParamsCache` 在嵌套服务端组件中类型安全地访问 searchParams。
- 🔗 序列化辅助：`createSerializer` 生成查询字符串，支持附加到基础 URL/路径，并处理 null 移除。
- 🧩 类型推断：`inferParserType` 可提取解析器返回的类型，用于对象描述时推断整体结构。
- 🧪 测试适配器：通过 `withNuqsTestingAdapter` 在单元测试中模拟 URL 更新，无需 mock 框架。
- 🐛 调试支持：导入 `nuqs/debug` 并设置 localStorage `debug=nuqs` 即可查看详细日志和性能标记。
- 🔍 SEO 建议：对于局部状态使用 canonical URL 忽略查询字符串；若查询定义内容则保留相关参数。
- ⚠️ 有损序列化：自定义序列化可能丢失精度，重载后状态可能不准确，需谨慎设计。
- 📄 开源协议：MIT 许可证，由 François Best 维护。

---

### [](https://github.com/heyo-sh/heyo-docs)

**原文标题**: [GitHub - heyo-sh/heyo-docs: Open-source documentation for developers · GitHub](https://github.com/heyo-sh/heyo-docs)

Heyo Docs 是一个开源、可主题化的文档工具包，支持 React Router、Next.js 和 Astro，可快速搭建包含 MDX、导航、搜索、OpenAPI 参考和 SEO 的独立文档站点。

- 📚 Heyo Docs 提供可主题化的文档解决方案，兼容 React Router、Next.js 和 Astro 框架。
- 🚀 通过 `pnpm create @heyo-sh/heyo-docs`、npm、Yarn 或 Bun 一键创建项目，并支持选择框架、主题及部署目标。
- 🔧 已有应用可参考框架专属指南（React Router、Next.js、Astro）进行集成。
- ⚙️ 唯一必需配置是 `heyo-docs.config.ts` 中的 `content` 字段，其他如标题、描述、品牌、分组、主题等均可选。
- 🎨 内置主题、模式、颜色等外观配置，以及站点标识和默认元数据设置。
- 🧭 支持通过 `groups` 定义侧边栏结构和页面顺序，并可配置页脚和自定义导航。
- 🌐 `siteUrl` 用于生成 SEO、RSS、sitemap 和 AI 发现文件。
- 📖 提供完整的配置指南，以及 MDX 组件、OpenAPI、部署和样式文档。
- 🤝 项目开源，采用 MIT 许可证，贡献指南见 CONTRIBUTING.md。

---

### [](https://github.com/aidenybai/tailwind-stylex)

**原文标题**: [GitHub - aidenybai/tailwind-stylex: Bring Tailwind design system to StyleX · GitHub](https://github.com/aidenybai/tailwind-stylex)

概述：tailwind-stylex 是一个开源工具库，用于将 Tailwind CSS 的默认设计令牌（设计变量）直接集成到 StyleX 中，提供类型安全、自动补全友好的常量，无需额外配置或生成步骤，同时附有详细的使用示例和全面的令牌分类。

- 📦 安装方式：通过 `pnpm add tailwind-stylex @stylexjs/stylex` 安装，并需在 StyleX 编译器中配置 `externalPackages` 或自定义 `include` 列表以处理该包。
- 🚀 使用示例：支持从 `tailwind-stylex/tokens.stylex` 导入 `colors`、`spacing`、`radii` 等令牌，直接在 `stylex.create` 中调用；数字命名的令牌（如 `spacing[4]`）需用中括号语法访问。
- 🎨 令牌分类：涵盖颜色、布局（间距/断点/容器）、排版（字体/字号/行高）、表面（圆角/阴影/模糊）、动效（缓动/动画/透视）及默认值等，类别全面。
- ✨ 开发者体验：所有令牌在编辑器中可自动补全，并能直接显示每个令牌对应的具体数值，提升开发效率。
- 📄 项目信息：仓库基于 MIT 许可证开源，支持 `stylex` 和 `tailwindcss` 主题标签，当前有 68 个星标，使用 pnpm 管理依赖。

---

### [深入探讨 StyleX](https://flaviocopes.com/stylex/)

**原文标题**: [A deep dive into StyleX](https://flaviocopes.com/stylex/)

StyleX 是一种编译型 CSS-in-JS 方案，将 JavaScript 样式对象在构建时转换为原子化 CSS 类，兼顾开发体验与运行时性能，适合大型组件库及 AI 编码场景。

- 🎯 StyleX 的核心：用 JS 对象写样式，构建时编译为普通 CSS 类，生产环境无运行时注入。
- ⚙️ 解决痛点：类名冲突、样式覆盖、删除安全、共享组件定制、CSS 冗余等问题。
- 🧠 心智模型：样式对象 → 编译器 → 原子类（每个声明一个类）→ 浏览器应用。
- ⚛️ React/Vite 配置：安装 `@stylexjs/stylex` 与 `@stylexjs/unplugin`，在 `vite.config.ts` 中先注册 StyleX 插件再 React 插件。
- 🧩 基本用法：`stylex.create()` 定义样式，`stylex.props()` 应用到组件，支持条件合并与变体对象映射。
- 🛠️ DevTools：开发模式下可查看样式来源、应用顺序并跳转到源文件。
- 🔧 Astro 集成：复用 Vite 插件，在 React 组件中使用；开发模式需引入 `virtual:stylex.css` 与运行时脚本。
- 📦 原子 CSS 优势：相同声明全局复用，减少重复，样式表随应用增长缓慢。
- 🎨 样式组合：`stylex.props()` 按传入顺序解决冲突，后续样式覆盖先前样式，避免特异性问题。
- 🧷 条件与变体：直接使用 JS 条件、三元表达式、对象查找；TypeScript 自动推导变体类型。
- 🖱️ 状态与响应式：伪类、媒体查询、`@supports` 均以属性为中心嵌套；支持 `null` 禁用优先级规则。
- ⚡ 动态值：通过样式函数生成 CSS 变量，运行时仅更新 `style` 属性；仅限返回值字面量的简单参数。
- 🎨 设计令牌：`stylex.defineVars()` 创建类型化 CSS 变量；`stylex.createTheme()` 覆盖变量组实现主题。
- 📤 接受父级样式：通过 `StyleXStyles` 类型限定可定制属性，提供比裸 `className` 更安全的扩展点。
- 🎬 动画：`stylex.keyframes()` 生成关键帧，通过 `animationName` 引用，避免全局命名冲突。
- 🧩 原子工具类：`@stylexjs/atoms` 提供 flex、对齐、间距等快捷原子样式，适合一次性小例外。
- 🔒 静态约束：样式对象不能包含任意 JS（如导入的普通值、对象展开）；共享值须用 `defineVars` 或 `defineConsts`。
- 🌍 全局 CSS 边界：建议仅保留 reset、字体、CMS 内容样式；配合 CSS Layers 避免全局覆盖组件。
- 🧹 代码检查：ESLint 插件可检测未用样式、缩写冲突、限制属性值范围，强化设计规范。
- 🤖 对 AI 编码友好：约束减少了等价写法的随意性，让代理生成的代码更一致，审查更容易。
- ⚖️ 成本权衡：配置复杂、语法较长（`paddingInline` vs `px-4`）、组件生态多为 Tailwind，需迁移。
- 📋 对比总结：StyleX 比普通 CSS/Tailwind/运行时 CSS-in-JS 在大型应用中提供更可预测的组合与类型安全。
- ✅ 适用场景：新 React 应用、组件库增长、AI 大量改动 UI；静态内容为主的 Astro 站点不建议迁移。
- 🔍 生产验证：构建后检查 `dist/assets`，应只有原子类与哈希类名，无原始 `stylex.create()` 对象。

---

### [](https://larsfaye.com/articles/ai-coding-will-prevent-expertise)

**原文标题**: [AI Coding will Prevent Expertise | Lars Faye](https://larsfaye.com/articles/ai-coding-will-prevent-expertise)

AI 编程助手看似提升了效率，却可能正在侵蚀编程专业能力的根基。文章指出，AI 工具越是强大，新手越容易跳过必要的“认知摩擦”，产生能力错觉，最终导致专家断代。作者主张将 AI 当作苏格拉底式导师而非代码生成器，并通过主动参与和验证，才能让技术真正服务于长期成长。

- 🤖 AI 编程带来“熟练编排者悖论”：管理 AI 所需的能力，恰恰是长期使用 AI 会削弱的能力，新手受影响最重。
- ⚠️ JetBrains 研究证实，重度依赖 AI 的新手常跳过规划、产生“能力错觉”，而屏蔽或限制 AI 的开发者反而掌握更扎实。
- 🔄 LLM 导致“倒置学习”：经验越丰富越能受益，新手却因不知该问什么而被模型误导，误以为自己懂了很多。
- 🔥 摩擦是学习的关键：UPenn 研究发现，用 AI 当拐杖的学生比用课本的学生差 17%，而“先求助后独立完成”的苏格拉底式学习则表现大幅提升。
- 🧩 若只追求代码生成而不建立深层理解，会引发“专家管道崩溃”，使下一代开发者无力接手日益复杂的系统。
- 📚 作者主张“摩擦优先”：把 LLM 当作互动文档、教程生成器和苏格拉底练习工具，而非直接生成最终代码。
- ✅ 提供自检清单：区分“认知债务”（放弃判断）与“认知卸载”（委托机械工作），确保每次使用都在增进理解。
- 💡 智力不是商品：技能必须靠主动参与、犯错和反复磨炼才能形成，否则未来开发者将沦为 AI 工具的依赖者。

---

### [让 React Testing Library](https://sigh.dev/posts/making-react-testing-library-faster/)

**原文标题**: [Making React Testing Library Tests 43% Faster • sigh.dev](https://sigh.dev/posts/making-react-testing-library-faster/)

本文介绍了作者在 Sentry HackWeek 中借助 Codex 优化 React Testing Library 测试性能的实践。通过剖析真实测试文件，针对 jsdom 等底层库实施三项关键修复，在不重写测试代码的前提下，使测试运行时间缩短 43%，并比当前 jsdom 26 快 21%。

- ⚡ 目标：不替换 `getByRole` 或 `userEvent`，仅优化底层库来加速现有测试。
- 📉 成果：jsdom 30 从 17.18s 降至 9.77s，比 jsdom 26 快 21%，整体提速 43%。
- 🤖 Codex 过程：微基准测试可能误导，必须将改动 patch 到真实项目验证；最终通过 Sentry 测试文件定位到约 29% 时间耗在角色查询上。
- 🏷️ 标签索引：jsdom 原先每次查询重复扫描整个 DOM 寻找 `input.labels`；修复后构建共享标签索引，读取 100 个控件标签从 60.52ms 降到 0.67ms，约 91 倍加速。
- 🔍 选择器快速路径：jsdom 内部实现对象与公共 document wrapper 用 `===` 比较恒为 false，导致快速路径从未生效；修复后匹配器基准快 89%，`getByRole('button')` 大基准快 42%。
- 🎯 事件路径优化：构建事件路径时记录有效目标，并跳过无监听器的元素，事件吞吐量提升 12%–36%。
- 📋 适用场景：大型表单、大量 `getByRole` 可访问名称查询、深 DOM 树、密集 `userEvent`/`fireEvent` 交互，以及依赖 `matches()` 的库。
- 🔄 现状：标签缓存和事件路径修复已合入 jsdom 但未发布，DOMSelector 快速路径修复仍在开放中。

---

