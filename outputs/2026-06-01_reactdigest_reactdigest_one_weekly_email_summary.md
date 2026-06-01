### [React 文摘：邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

React Digest 是一份为 React 开发者精心策划的每周通讯，已有超过 22,439 名前端软件工程师订阅，旨在通过精选文章和简短摘要帮助读者节省时间、每周学习新知识。

- 📬 每周一封邮件，精选 React 相关文章并附简短摘要
- ⏱ 帮助开发者节省筛选内容的时间，专注有价值的信息
- 🧠 每周都能学到新知识，保持技术更新
- 👍 读者反馈积极，认为文章实用、紧跟技术演进（如 React 并发模式）
- 👥 读者来自全球知名前端工程师团队
- 📅 持续运营多年（2013-2026），提供通讯、隐私及广告服务

---

### [我的 2026 年前端技术栈 - T 型开发者](https://thetshaped.dev/p/my-frontend-stack-in-2026-react-nextjs-pnpm-vite-ts-tailwind-storybook-tanstack-zustand-zod-oxlint-oxfmt-msw-vitest-playright-sentry)

**原文标题**: [My Frontend Stack In 2026 - The T-Shaped Dev](https://thetshaped.dev/p/my-frontend-stack-in-2026-react-nextjs-pnpm-vite-ts-tailwind-storybook-tanstack-zustand-zod-oxlint-oxfmt-msw-vitest-playright-sentry)

以下是根据您提供的文章内容整理的摘要：

2026 年前端技术栈总结：一套经过实战检验的工具组合，强调工具间的良好协作、高效性能与低维护成本，旨在让开发者专注于业务逻辑而非工具本身。

- 🚀 **基础框架按需选择**：内容型网站（如营销页、博客）用 **Next.js**；内部工具、仪表盘等 SPA 用 **Vite 8 + Rolldown + TypeScript**，构建速度提升显著。
- 🎨 **样式与组件零摩擦**：**Tailwind CSS** 处理样式，**shadcn/ui** 提供可复制、可定制的组件原语，无需额外依赖，实现“无需构建设计系统的设计系统”。
- 📚 **组件文档与开发利器**：当组件库超过 20 个时，**Storybook** 的价值凸显，尤其与 shadcn/ui 配合，可直观展示所有状态变体，降低沟通成本。
- 🔄 **服务端与客户端状态分离**：**TanStack Query** 管理服务端状态（缓存、后台刷新、乐观更新），**TanStack Router** 提供全类型安全的路由；**Zustand** 处理需要共享的轻量客户端状态。
- 🛡️ **运行时安全无死角**：**Zod** 对所有跨信任边界的数据（API 响应、表单输入、环境变量等）进行运行时验证，弥补 TypeScript 仅在编译时生效的不足。
- ⚡ **极致速度的代码质量工具**：**Oxlint + Oxfmt** 基于 Rust，比 ESLint 快 50-100 倍，格式化与 linting 共享语法树，极速反馈改变开发习惯。
- 🧪 **分层测试体系**：**Vitest** 负责单元/组件测试（毫秒级反馈），**Playwright** 负责端到端测试（含追踪查看器），**MSW** 作为统一网络模拟层，贯穿测试、开发与 Storybook。
- 🔍 **生产环境问题追踪**：**Sentry** 提供错误监控与**会话回放**，可精确复现用户操作步骤，结合 AI 摘要快速定位问题根源。

---

### [如何在 React Router 中取消 `useFetcher().load()` 的卸载操作](https://sergiodxa.com/tutorials/cancel-usefetcher-load-on-unmount-in-react-router)

**原文标题**: [How to Cancel `useFetcher().load()` on Unmount in React Router by sergiodxa](https://sergiodxa.com/tutorials/cancel-usefetcher-load-on-unmount-in-react-router)

本教程介绍了如何在 React Router v7 中取消组件卸载时的 `useFetcher().load()` 请求，以避免不必要的上游 HTTP 请求。

- 📋 **核心问题**：当拥有 fetcher 的组件卸载时，`fetcher.load()` 发起的 HTTP 请求仍会继续运行，造成资源浪费，尤其是在 loader 作为 BFF 转发请求时。
- 🔗 **关键解法**：在 loader 中传递 `request.signal` 给上游 `fetch()`，使请求能通过 Fetch API 的标准流程被取消。
- 🛠️ **实现步骤**：创建接受 `AbortSignal` 的服务端辅助函数；在资源路由 loader 中转发 `request.signal`；在组件中使用 `fetcher.load()` 加载数据。
- 🧹 **卸载清理**：在 `useEffect` 的清理函数中调用 `fetcher.reset()`，依赖项设为稳定的 `reset` 函数而非整个 fetcher 对象。
- ⚠️ **注意事项**：React Router v7 默认持久化 fetcher 状态，不会在卸载时自动取消请求；`reset()` 是合理的变通方案，但需配合 loader 中的信号传递才能完全取消上游请求。

---

### [React 服务端组件的组件架构 | Aurora Scharff](https://aurorascharff.no/posts/component-architecture-for-react-server-components/)

**原文标题**: [Component Architecture for React Server Components | Aurora Scharff](https://aurorascharff.no/posts/component-architecture-for-react-server-components/)

### 概述总结
本文探讨了从传统数据获取方式（如 `useEffect`、React Query、路由加载器）到 React Server Components（RSC）的演进，并展示了如何利用 RSC 构建可组合、高性能的页面架构，同时通过 Suspense 和骨架屏设计流畅的加载体验。

- 📜 **背景**：服务器端数据获取比客户端更快，因为避免了 JS 下载和瀑布流请求；RSC 允许组件在服务器上自主获取数据，兼具服务器速度和组件可组合性。
- 🔧 **本地数据获取**：`useEffect` 和 React Query 虽能实现组件级数据获取，但存在“爆米花 UI”和客户端延迟问题；React Query 通过集中缓存解决了状态提升，但依然依赖客户端。
- 🚀 **路由级加载器**：通过 `loader` 或 `getServerSideProps` 将数据获取移至服务器，但导致组件与路由耦合，复用需重复获取数据。
- ✨ **异步服务器组件**：RSC 让每个组件在服务器上自主获取数据（如 `WhoToFollow` 无需外部 props），通过 `cache()` 去重，实现高度可复用和自包含。
- 🏗️ **构建 Next.js 应用**：利用 Suspense 边界避免阻塞渲染，骨架屏与组件同文件导出以保持同步；页面通过组合 Suspense 边界设计加载序列（如分组或独立流式加载）。
- 🧩 **参数化页面**：通过 `.then()` 处理 `params` Promise，保持页面同步，并支持独立流式加载（如帖子详情和回复）。
- 🖱️ **交互性**：客户端组件（如 `LikeButton`）使用 Server Function 和 `useOptimistic` 实现即时反馈，与服务端组件无缝组合。
- 📁 **代码组织**：按功能分组（如 `features/post/`），组件仅接受最小 props（如 ID），便于跨页面复用和重构。
- 🎨 **加载体验设计**：Suspense 边界、ErrorBoundary 和 ViewTransition 结合，实现区域独立加载、错误隔离和平滑动画。
- 💡 **缓存组件**：Next.js 16 的 `cacheComponents` 支持部分预渲染，静态部分即时服务，动态部分流式加载；RSC 架构天然适配此模型。
- 📝 **核心原则**：页面是同步组合器（不获取数据），异步组件自主获取数据，骨架屏与组件同文件，Suspense 边界在页面层级，客户端边界尽量下沉。

---

### [TanStack 路由器和查询](https://tkdodo.eu/blog/tan-stack-router-and-query)

**原文标题**: [TanStack Router and Query](https://tkdodo.eu/blog/tan-stack-router-and-query)

TanStack Router 與 TanStack Query 的整合指南

- 🔗 TanStack Router 與 TanStack Query 同屬一個技術棧，整合順暢，但 Router 內建快取僅限於特定路由，而 Query 快取是全域性的
- ⚡ 在路由加載器中使用 Query 可提前啟動資料獲取，甚至支援預先懸停獲取，確保元件渲染前資料已就緒
- 🛠️ 使用 `queryClient.ensureQueryData` 或 `prefetchQuery` 在加載器中觸發查詢，元件中再用 `useSuspenseQuery` 或 `useQuery` 取得資料
- 🔧 需將 QueryClient 加入 Router 上下文，並關閉 Router 內建快取（設 `defaultPreloadStaleTime: 0`），避免快取衝突
- 🎯 建議將加載器視為「事件處理器」，僅用於觸發快取預填，元件應使用 `use(Suspense)Query` 而非 `useLoaderData`，以確保查詢活躍狀態
- 🌀 使用 `useSuspenseQuery` 可與 Router 的 Suspense 邊界完美整合，簡化元件邏輯，並支援延遲資料載入
- 🖥️ 在 SSR 場景下，TanStack Start 提供 `setupRouterSsrQueryIntegration`，自動將伺服器資料串流至客戶端快取，無需修改程式碼
- ⚠️ 不使用 `use(SuspenseQuery)` 會導致查詢被視為非活躍，無法自動重新獲取、無效化後不重新載入，甚至可能被垃圾回收

---

### [Next.js 布隆过滤器及其如何破坏 App Router 迁移 — Dario Djuric](https://darios.blog/posts/the-ghost-in-your-nextjs-router)

**原文标题**: [The Next.js bloom filter and how it can break App Router migrations — Dario Djuric](https://darios.blog/posts/the-ghost-in-your-nextjs-router)

## 概述总结

本文介绍了 Next.js 中客户端路由器过滤器（bloom filter）在 Pages Router 向 App Router 增量迁移时可能引发的导航问题，特别是当应用配置了 basePath 时，可能导致 404 错误或 URL 重复。

- 🧩 **双路由器并行机制**：Next.js 允许 Pages Router 和 App Router 共存，但客户端需要判断路由归属，bloom filter 用于区分路由属于哪个路由器
- ⚠️ **Bloom filter 的局限性**：该数据结构可能产生误报（false positive），将 Pages Router 路由错误标记为 App Router 路由，触发不必要的硬导航
- 🔄 **basePath 导致 URL 重复**：当 bloom filter 误报时，硬导航代码会重复添加 basePath，导致 URL 变成`/dashboard/dashboard/activities`，引发 404 错误
- 🔍 **问题诊断方法**：检查是否同时使用两个路由器、是否配置 basePath、是否只有部分链接异常、URL 是否重复、关闭 appDir 后问题是否消失
- 🛠️ **解决方案**：设置`experimental.clientRouterFilter: false`禁用 bloom filter，或降低`clientRouterFilterAllowedRate`减少误报率（但会增加客户端包体积）
- 📝 **官方文档缺失**：该功能在 Next.js 官方文档中几乎没有说明，增加了调试难度

---

### [CSS 与 JavaScript • Josh W. Comeau](https://www.joshwcomeau.com/animation/css-vs-javascript/)

**原文标题**: [CSS vs. JavaScript • Josh W. Comeau](https://www.joshwcomeau.com/animation/css-vs-javascript/)

本文探讨了 CSS 与 JavaScript 动画的性能差异，并提供了选择合适工具的建议。

- 🎯 **CSS 动画优势**：CSS 关键帧和过渡在独立线程运行，不受主线程阻塞影响，性能更稳定。
- ⚙️ **JS 动画局限**：基于`requestAnimationFrame`的 JS 动画在主线程执行，易被其他任务干扰导致卡顿。
- 🚀 **Motion 库亮点**：Motion 利用 Web Animations API，实现与 CSS 类似的独立线程动画，避免主线程问题。
- 🔄 **GSAP 特性**：GSAP 动画在帧延迟后不自动同步时间，可能导致动画时长不准确，但可提供更平滑的视觉体验。
- 📦 **库加载成本**：JS 动画库（如 Motion 48kB、GSAP 27kB）需下载解析，但通常不影响用户交互初期的体验。
- 🛠️ **工具选择策略**：优先使用原生 CSS 动画；复杂场景选 Motion 类库；避免使用仅封装 CSS 功能的 JS 库。
- 🌟 **现代 CSS 能力**：View Transitions、`linear()`、Animation Timeline 等新 API 减少了对 JS 库的依赖。

---

### [你可以像其他文本一样设置替代文本的样式 - Piccalilli](https://piccalil.li/blog/you-can-style-alt-text-like-any-other-text/)

**原文标题**: [
  You can style alt text like any other text - Piccalilli
](https://piccalil.li/blog/you-can-style-alt-text-like-any-other-text/)

以下是对文章内容的总结：

本文介绍了如何通过 CSS 和 JavaScript 增强图片 alt 文本的显示效果，使其在图片加载失败时更美观易读。

- 🎨 通过 CSS 样式化`<img>`元素，可以为 alt 文本设置斜体、平衡换行等视觉风格，提升用户体验
- 📐 使用`display: block`和`max-width: 100%`确保图片容器填充父元素，避免底部空白
- 🔧 利用 JavaScript 的`onerror`事件监听图片加载失败，动态添加`data-img-loading-error`属性
- ✨ 通过 CSS 属性选择器`img[data-img-loading-error]`为加载失败的图片添加边框、内边距和宽度限制
- ⚠️ Safari 浏览器存在限制，仅当 alt 文本“适合一行”时才渲染，需注意兼容性
- 💡 这是一种渐进增强技术，可在不影响正常图片显示的前提下优化加载失败时的视觉反馈

---

### [关于 `<dl>` | Ben Myers](https://benmyers.dev/blog/on-the-dl/)

**原文标题**: [On the <dl> | Ben Myers](https://benmyers.dev/blog/on-the-dl/)

HTML 描述列表（`<dl>`）元素是标记名称 - 值对列表的语义化方式，比嵌套 `<div>` 更易用且更具可访问性。

- 📋 **核心结构**：`<dl>` 包裹整个列表，`<dt>` 表示名称，`<dd>` 表示值，一个 `<dt>` 可对应多个 `<dd>`。
- 🔄 **分组包装**：允许用 `<div>` 包裹 `<dt>` 和其对应的 `<dd>` 组，便于样式控制。
- ♿ **无障碍优势**：屏幕阅读器可识别列表数量、当前位置，并允许用户跳过整个列表，提升可用性。
- 🎲 **灵活应用**：从书籍详情到《龙与地下城》属性块，该模式能适配多种视觉差异大的名称 - 值对场景。
- 💡 **语义价值**：即使浏览器支持不完美，语义化标记仍为用户设备提供结构化信息，创造更优体验。

---

### [声明式部分更新 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/declarative-partial-updates)

**原文标题**: [Declarative partial updates  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/declarative-partial-updates)

Chrome 团队推出了声明式局部更新（Declarative Partial Updates）API，旨在解决 HTML 线性传输的局限性，提升网页性能和开发体验。该方案包含两个核心部分：无序流式处理（Out-of-order streaming）和增强的 HTML 插入与流式处理方法。

- 🔄 **无序流式处理**：通过新的 `<template for>` 属性和处理指令（如 `<?marker>`），允许 HTML 内容在文档中以非顺序方式加载和替换，支持“孤岛架构”和按需加载，优化首屏性能。
- 🧩 **增强的 HTML 插入 API**：引入一套命名一致的新方法（如 `setHTML`、`streamHTML` 等），支持静态和流式插入 HTML，并内置安全清理（Sanitizer）和脚本执行控制，简化动态内容更新。
- 🚀 **流式性能优化**：流式 API（如 `streamHTMLUnsafe`）允许在内容未完全下载时逐步插入，避免等待，适用于单页应用（SPA）和大内容动态加载。
- 🛡️ **安全与兼容性**：默认启用安全清理，提供“Unsafe”版本供信任场景使用；支持 Trusted Types 集成，并已发布 polyfill 供开发者提前使用。
- 🌐 **标准化与未来扩展**：API 正在标准化中，获得其他浏览器厂商积极反馈；未来可能支持客户端包含、批处理更新、内容版本控制等高级功能。

---

### [JS 填字游戏](https://lyra.horse/fun/jscrossword/)

**原文标题**: [JS Crossword](https://lyra.horse/fun/jscrossword/)

这是一个关于 JS 填字游戏的介绍，其中每个线索都是对答案进行 JavaScript eval() 运算的结果。

- 🧩 游戏规则：每个线索都是对答案执行 JS eval() 的结果，例如线索"7"可填入"3+4"，线索"[object Object]"可填入"[]+{}"
- 🔤 允许字符：仅限 A-Za-z0-9!"()*+-./<=>[]`{}，不能使用空格、逗号或分号
- 🎯 最终答案：由英文单词组成，仅匹配 A-Za-z
- 🛡️ 安全机制：答案在 eval() 沙箱中执行，提供 playground 供测试
- 💡 难度定位：使用了一些冷门和“诅咒”级别的 JS 特性，适合熟悉 JavaScript 的玩家
- 🖱️ 操作方式：点击格子或按 ctrl 可切换填写方向，进度自动保存
- 🎨 颜色提示：绿色为正确，红色为无效字符，黄色为错误，灰色为预填
- 📢 分享渠道：支持在 fedi、bsky、twitter 上分享，并提供清除和隐藏字母功能

---

### [我对 AI 的思考，第二部分：智能体设置、工作流程与工具 · Mark 的开发博客](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/)

**原文标题**: [
     My Thoughts on AI, Part 2: Agent Setup, Workflow, and Tools ·  Mark's Dev Blog
  ](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/)

## 概述总结
作者详细介绍了个人 AI 开发工作流，强调以人为核心的控制、确定性脚本和工具链优化，通过 Orchestrator 父会话与子任务分离的架构实现高效且可控的 AI 辅助编程。

- 🤖 **核心工具链**：使用 OpenCode 作为代理，CodeNomad 作为 Web UI，Opus 4.6 模型，VS Code 和 Fork 作为 IDE/版本控制工具
- 🧠 **工作流架构**：采用"Orchestrator 父会话"管理全局上下文，子任务专门处理具体开发工作，确保开发者始终掌控方向
- 🔒 **权限管理**：自定义插件实现确定性命令审批，避免 YOLO 模式，同时减少不必要的权限提示
- 📂 **文件读取优化**：使用 cachebro 缓存文件读取，grepika 和 tilth 进行代码结构搜索，大幅减少上下文膨胀
- 📝 **开发计划管理**：建立独立的 dev-plans 知识库，包含架构文档、功能计划、进度更新和子任务交接文件
- ⚙️ **自动化脚本**：通过 devplans.ts 统一管理进度记录、子任务交接、文档创建等确定性操作
- 📏 **AGENTS.md 配置**：约 250 行的详细指令文件，涵盖交互模式、编码规范、代码导航、任务管理等方面
- 🔄 **上下文管理**：使用 OpenCode 动态上下文修剪插件，避免达到上下文限制，保持会话在 100K 以内
- 🚀 **未来改进**：计划增强长期记忆和上下文检索能力，自动扫描会话提取学习模式，改进代码审查工具

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

概述摘要  
- 📬 每周精心策划的编程文摘，专为软件工程师设计  
- 👥 已有超过 22,127 名软件工程师订阅，每周仅发一封邮件  
- 📖 精选文章并附简短摘要，节省寻找优质内容的时间  
- 🧠 每周学习新知识，持续提升技能  
- 💬 读者反馈：内容切中要点，如 API 设计相关文章深受好评  
- 🌍 读者来自全球知名科技公司  
- 📅 版权归 Bonobo Press 所有（2013-2026），提供新闻通讯、隐私及广告选项

---

### [科技领导力：邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一份面向 CTO、工程经理及资深工程师的科技领导力周刊，每周一和周四发送，旨在帮助技术领导者提升管理能力。

- 📧 每周两封邮件，精选领导力文章并附简短摘要，帮你节省筛选时间
- 🎯 内容涵盖架构讨论、会议规划、沟通技巧及授权等关键领导力主题
- 👥 已吸引超过 28,887 名工程领导者订阅，读者来自多家知名科技公司
- 📚 读者反馈：文章精准聚焦软件领域的领导力建设，尤其是关于授权的深度内容备受好评
- 🏢 被众多科技公司技术领导广泛阅读，覆盖行业广泛

---

### [C# 摘要：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

本内容介绍了一份专为.NET 开发者设计的每周精选通讯《C# Digest》，旨在帮助工程师高效获取优质技术内容。

- 📬 每周一封邮件，精选 C#/.NET 技术文章，附带简短摘要
- ⏱️ 节省筛选优质内容的时间，专注学习新知识
- 💼 读者反馈：文章内容实用，已在实际工作中应用，如 LINQ、操作结果模式等
- 🌍 读者来自全球.NET 工程师社区，已吸引超过 20,578 名订阅者
- 🔒 提供隐私保护与广告服务，由 Bonobo Press 运营（2013-2026）

---

### [让开发者保持最新动态 – Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 自 2013 年起通过软件新闻通讯，为超过 8 万名开发者、IT 专家和技术人员提供最新资讯。

- 📰 提供面向软件开发者、技术主管和 CTO 的简洁新闻通讯，深受技术人员喜爱
- 🎯 提供广告服务，精准触达软件工程师、团队领导及 IT 决策者等专业受众
- 📋 提供媒体工具包，方便客户了解并开始投放广告
- ✉️ 欢迎通过联系页面咨询问题、提出建议或洽谈广告合作
- ©️ 版权归 Bonobo Press 所有，涵盖 2013 至 2026 年，并附有使用条款

---

### [过往简报：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是对您提供的 React Digest 2026 年 1 月至 5 月各期内容的摘要：

React Digest 2026 年 1 月至 5 月涵盖了 React 生态系统的重大更新、安全漏洞、性能优化、最佳实践以及行业趋势，包括 React Server Components、Fiber 架构、新 hooks、AI 调试、虚拟滚动和内存泄漏等关键主题。

- 🚀 **React Server Components 与 Suspense**：RSC 允许组件自主获取数据，结合 Suspense 精确控制加载时序，取代传统 prop drilling。
- 🔒 **安全漏洞警示**：React Flight 协议存在严重 RCE 漏洞，影响默认 Next.js 应用；TanStack npm 包遭 GitHub Actions 链式攻击，30 分钟内泄露云密钥。
- ⚡ **性能优化实践**：Railway 从 Next.js 迁移到 Vite，构建时间从 10 分钟降至 2 分钟；MDN 改用 Lit Web 组件，开发构建从 2 分钟缩短至 2 秒。
- 🧠 **新 hooks 与异步处理**：React 19 的 useTransition 和 useActionState 简化异步代码，自动管理 pending 状态和错误处理；use() hook 跳过传统规则，直接读取 promise。
- 🐛 **常见错误与调试**：86% 前端项目存在内存泄漏，主要源于定时器和事件清理缺失；Bloom filter bug 可导致 Next.js 页面静默 404。
- 🎨 **可访问性与 UI**：常见 a11y 错误包括缺失语义、焦点丢失和动态更新无声；骨架屏通过渲染真实组件与假数据实现自我同步。
- 🛠️ **架构与工具**：Feature-based 架构强调异步状态更新；AsyncLocalStorage 使任何函数都能获取 React Router 上下文；Bippy 工具可运行时探查 React fiber 树。
- 📦 **包管理与构建**：研究 500 个仓库发现仅 lodash 和 moment.js 导致真正包体积膨胀，而非 barrel imports；React Fiber 将渲染拆分为~5ms 块，保持浏览器响应。
- 🤖 **AI 与开发效率**：Mark Erikson 的 AI 编码设置通过父会话生成子任务，自定义插件保持上下文精简；AI 调试能力、React Doctor 代码诊断工具和 vinext 框架被探讨。
- 🧪 **测试与稳定性**：未测试代码库的重建教训；test IDs 可能暗示可访问性问题；为 useEffect 函数命名被推荐。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了 React Digest 如何收集、使用和保护您的个人信息，强调透明度和数据安全。

- 🔒 我们仅在收集前明确目的，并仅用于实现这些目的或法律要求的情况。
- 📧 我们仅收集您的电子邮件地址，用于发送新闻通讯，不用于其他用途。
- 🛡️ 我们通过合理的安全措施保护个人信息，防止丢失、盗窃或未经授权的访问。
- 👶 我们不会故意收集 13 岁以下儿童的信息，网站也不针对该年龄段设计。
- 📋 根据英国《数据保护法》，您可以请求访问我们存储的您的所有信息（需发送邮件至指定地址）。
- ❌ 您可随时通过邮件请求删除您的数据，我们支持数据删除权。
- 🚫 我们坚决反对垃圾邮件，仅通过邮件发送新闻通讯，并提供一键退订功能。
- 📅 本政策适用于 2013-2026 年，由 Bonobo Press 运营。

---

### [媒体资料包 – 倭黑猩猩出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

本媒体套件介绍 Bonobo Press 旗下四份面向技术人员的新闻通讯的订阅数据、广告价格及合作流程，旨在帮助广告主精准触达目标受众。

- 📊 **高互动率受众**：所有新闻通讯的打开率和点击率均高于行业基准，且定期清理订阅列表以保持读者活跃度。
- 👔 **Leadership in Tech**：面向技术领导者的双周通讯，订阅者 22,325 人，打开率 57.95%，单期赞助费$2,235，预估点击 365-585 次，CPC $3.82-$6.12。
- 💻 **Programming Digest**：面向软件工程师的每周通讯，订阅者 20,032 人，打开率 50.41%，单期赞助费$985，预估点击 273-493 次，CPC $2.00-$3.61。
- 🖥️ **C# Digest**：面向.NET 开发者的每周通讯，订阅者 17,098 人，打开率 54.92%，单期赞助费$1,220，预估点击 411-631 次，CPC $1.93-$2.97。
- 🌐 **React Digest**：面向前端开发者的每周通讯，订阅者 20,075 人，打开率 54.06%，单期赞助费$1,375，预估点击 303-523 次，CPC $2.63-$4.54。
- 📝 **纯文本广告格式**：广告以纯文本嵌入通讯内容，需提供链接、标题（<100 字符）和描述（<400 字符），截止日期为发布前 4 天。
- 🚀 **简单订购流程**：联系告知产品需求 → 确定排期 → 付款锁定 → 提交素材 → 广告上线 → 提供效果报告。因排期紧张，建议提前几周联系。
- 🤝 **成功合作案例**：过往合作伙伴包括 Okta、GitLab、Datadog、MongoDB、Pluralsight 等知名企业，且常重复投放。

---

