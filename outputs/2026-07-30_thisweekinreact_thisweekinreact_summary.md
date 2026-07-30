### [](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q3&utm_content=1st)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q3&utm_content=1st)

Meticulous 是一款自动化端到端测试工具，通过录制用户交互、AI 生成全量测试用例，并与 CI 集成，实现无需编写、维护测试即可快速安全地交付代码。

- 🚀 测试全自动生成：AI 引擎根据开发者日常操作生成覆盖所有代码分支和用户流程的测试用例，且测试随应用演化自动更新。
- 🔬 零假阳性：基于 Chromium 的确定性调度引擎，消除测试不稳定（flake）问题，并极速执行大规模测试。
- 🕒 闪电般的反馈：测试在计算集群上高度并行，1000+ 屏幕的测试结果可在 120 秒内返回。
- 🧩 集成简便：仅需在开发/预发布环境中添加脚本标签，无需特殊测试账号或模拟数据，即可开始录制。
- 🔁 与 CI 深度整合：打开 Pull Request 即可看到对用户工作流的影响，自动模拟后端响应，确保无副作用。
- 🏢 受众多企业信赖：包括 Dropbox、Notion 等组织已采用，工程师反馈“立即爱上，再无合并后调试问题”。
- 🎯 可替代或补充现有测试：既可补充已有测试套件，也可完全替换，降低维护成本。

---

### [](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q3&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q3&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

Meticulous 是一个自动化、详尽且确定性的端到端测试工具，能零开发工作量地持续生成和维护测试套件，帮助开发者在合并代码前快速发现回归问题，支持与现有测试套件互补或替代，已获多家知名组织信赖。

- 🚀 **零开发工作量**：只需添加脚本标签，即可自动记录用户在开发、暂存和预览环境中的交互，无需编写或维护测试代码。
- 🤖 **AI 引擎持续生成测试**：通过追踪代码分支执行路径，自动生成覆盖全部用户流程和边缘情况的视觉端到端测试套件，并随应用进化自动更新。
- 🔄 **合并前洞察影响**：PR 提交后，Meticulous 能模拟后端响应（无需特殊测试账户或模拟数据），展示变更对每个用户工作流的影响，无假阳性。
- ⚡ **极速回归测试**：测试高度并行化，1000 个屏幕在 120 秒内出结果；从 Chromium 底层构建的确定性调度引擎彻底消除测试闪烁（flakes），支持超复杂应用。
- 🏢 **无缝集成**：支持 Next.js / React / Vue / Angular / Nuxt / SvelteKit 等主流前端框架，提供代码示例；可与现有测试套件配合或直接替换。
- 🔒 **安全优先**：提供详细安全文档，代码片段仅记录非生产环境会话，可选记录生产会话以增加覆盖。
- 🏆 **广泛信任**：已被 Notion、Dropbox、Engine 等超 100 家组织采用，开发者反馈“一用就离不开”，大幅提升迭代速度并降低调试负担。

---

### [](https://octanejs.dev/)

**原文标题**: [Octane — React's programming model, compiled](https://octanejs.dev/)

Octane 是一个编译后的 React 替代框架，去除了虚拟 DOM 和 hooks 规则，通过编译器自动优化依赖和性能，同时保持与 React 相似的使用体验，并提供了增量迁移、完善的 CLI 工具和丰富的生态绑定。

- 🚀 无虚拟 DOM、无 hooks 规则，编译器自动推断依赖，性能优先
- ⚡ 改进的异步处理：独立 use() 调用并行启动，流式 SSR 更快
- 🔧 熟悉模型：hooks、memo、context、Suspense 等行为与 React 一致，事件原生、ref 作为 prop
- 📊 基准测试中，Octane 在多数套件（如 js-framework、todomvc、chat-stream）中显著优于 React 19 和 Preact 10
- 🛠️ 支持逐步迁移：组件可逐个从 TSX 转为 TSRX，并通过 OctaneCompat 在 React 19 中使用
- 🧪 11,500+ 测试用例，0 条 hooks 规则限制，规则可放在条件或早期返回之后
- 🔗 46 个第一方生态绑定（状态、数据、路由、UI、Three.js 等）
- 📦 CLI 工具（octane init、doctor、add、explain）帮助检查配置和修复常见问题
- 🏗️ 增量迁移：用 OctaneCompat 将编译后的岛组件嵌入现有 React 19 应用，保持 SSR 和 hydration

---

### [TSRX](https://tsrx.dev/)

**原文标题**: [TSRX](https://tsrx.dev/)

概述总结
TSRX 是一个 TypeScript 语言扩展，旨在以声明式方式构建 UI，作为 JSX 的精神继承者，它通过协定位、框架无关编译和智能工具链，让代码更可读、更易维护，同时兼容现有 TypeScript/JSX 生态。

- 🧩 TSRX 是 TypeScript Render Extensions，将结构、样式和控制流协定位在同一文件中，完全向后兼容 TypeScript 和 JSX。
- 🔄 框架无关且可互操作，能编译到 Octane、React、Preact、Ripple、Solid、Vue 等多种运行时，且可导入 .tsrx 模块到 JS/TS/TSX 文件。
- 📦 协定位设计：TypeScript 设置在前，作用域解析到一个输出节点，减少三目运算符、map 链和渲染辅助函数，使重构和上手更轻松。
- ⚡ 改善人体工程学：Solid 的 `&{ ... }` 模式编译为惰性 getter，保持响应性；语句容器让局部变量紧邻使用的 JSX，减少数据流追踪负担。
- 🛠️ 工具集成丰富：提供语言服务器（诊断、导航、补全），支持 Prettier、ESLint 插件，兼容 VS Code、Zed、Neovim、IntelliJ、Sublime 等编辑器。
- 🧠 智能编译：解析组件源码为 AST，通过框架专属插件（如 @tsrx/react、@tsrx/solid 等）生成目标运行时的惯用输出，包括作用域 CSS。
- 🚧 处于活跃 beta 阶段，欢迎在 issue 追踪器上反馈，已通过 MIT 许可发布。

---

### [什么时候该记录什么？| Sentry 博客](https://blog.sentry.io/logging-best-practices/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=logs-fy27q2-evergreen&utm_content=newsletter-react-link-logging-blog-learnmore)

**原文标题**: [When and what should I be logging? | Sentry Blog](https://blog.sentry.io/logging-best-practices/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=logs-fy27q2-evergreen&utm_content=newsletter-react-link-logging-blog-learnmore)

本文章提供了选择日志内容的实用指南，强调日志是调试和验证功能的快捷工具，并介绍了如何编写结构化的日志消息以及应避免记录的内容。

- 📝 日志可用于记录重要的运行时决策（如功能开关、用户分流），帮助理解不同用户的行为差异
- 🔄 记录功能或算法的中间结果与最终状态，便于定位流程中断或数据解析问题
- 🔐 审计与访问事件（创建、更新、删除、权限）有助于排查支持案例和满足合规要求
- ❌ 对于异常，优先使用 Sentry 的 Capture Error 而非日志；非关键错误可记录重试次数、状态码等上下文
- 🧱 使用结构化的键值对日志（如 user_id、request_id），并随请求演进持续添加上下文（如 Trace ID）
- 🎯 合理选择日志级别：debug 用于开发诊断，info 用于正常事件，warn 用于可恢复问题，error 用于已处理的意外失败
- 🚫 避免记录每个函数调用（应使用 profiling/tracing）、PII 与敏感信息、以及无特定目的的大数据块
- 🛠️ 在 allaboard.dev 项目中应用了这些实践，包括记录功能开关、算法步骤、审计事件和错误上下文
- 🚀 可借助 getsentry/sentry-for-ai 工具自动分析代码库并建议高价值的结构化日志

---

### [指南：离线支持 | Next.js](https://preview.nextjs.org/docs/app/guides/offline-support)

**原文标题**: [Guides: Offline support | Next.js](https://preview.nextjs.org/docs/app/guides/offline-support)

概述摘要：Next.js 的离线支持功能（实验性）允许在网络中断时自动重试导航、数据获取和 Server Actions，无需手动处理错误，通过 `useOffline` 钩子可向用户显示连接状态。

- 🌐 启用 `experimental.useOffline` 后，网络失败不会抛出错误，请求保持等待状态，连接恢复后自动重试。
- 🧩 搭配 Cache Components 和 Partial Prefetching，离线导航时渲染静态外壳，数据区域显示加载状态。
- 📡 使用 `useOffline` 钩子检测离线状态，在 Suspense 回退或全局横幅中告知用户连接情况。
- 🔄 离线时调用的 Server Actions 会暂挂，连接恢复后自动执行，无需手动重试。
- 🧪 测试需用 `next build && next start` 生产模式，通过 DevTools 模拟离线。
- ⚙️ 无需 Cache Components 时，路由级 `loading.tsx` 可提供类似离线行为。
- 📘 更多参考：`useOffline` API 文档、配置选项、渐进式 Web 应用指南。

---

### [伦敦 React 大会，2026 年 10 月 23 日及 26 日](https://reactadvanced.com/?utm_source=thisweekinreact)

**原文标题**: [React Conference In London, October 23 & 26, 2026](https://reactadvanced.com/?utm_source=thisweekinreact)

React Advanced Conference London 2026 是一场混合式的高阶 React 与 Web 工程峰会，于 2026 年 10 月 23 日（线下 + 远程）和 26 日（纯远程）举行，涵盖深度技术演讲、实战工作坊与社交活动。

- 📅 时间与形式：10 月 23 日伦敦现场 + 全球远程，10 月 26 日纯远程，共两天深度议程。
- 🎤 演讲阵容：40+ 位核心贡献者、社区领袖与高级工程师，聚焦 React 19、RSC、AI、全栈等前沿主题。
- 🛠 工作坊：5+ 场免费及专业工作坊（含远程），主题涵盖现代 React 架构、AI 应用构建、DevOps 等。
- 🧠 深度专题：四大 Deep Dive 方向——全栈与架构、AI Agents 与辅助编码、AI 工程、成长到 Tech Lead。
- 🌐 混合体验：线下社交、Q&A 讨论室、远程互动流、卡拉 OK 派对等特色活动。
- 💰 票价选择：混合票 £540、团队折扣、远程票 €180、订阅制 Multipass（月付 €17）含多个会议访问。
- 🏛 会场：伦敦 The Brewery，位于科技中心，交通便利。
- 🤝 社区福利：参与转发可获免费远程票，提供 100 个多样性奖学金名额，团队推荐有优惠。

---

### [我们已停止在 TanStack.com 上使用 RSC | TanStack 博客](https://tanstack.com/blog/we-stopped-using-rsc-on-tanstack-com)

**原文标题**: [We Stopped Using RSC on TanStack.com | TanStack Blog](https://tanstack.com/blog/we-stopped-using-rsc-on-tanstack-com)

TanStack.com 的 RSC（React Server Components）架构实践经历了一次重大转变：从最初依赖 RSC 解决客户端 JavaScript 过大的问题，到最终放弃 RSC 回归常规 SSR。核心原因是：通过自研轻量库来压缩渲染依赖，使得 RSC 的架构复杂性不再“物有所值”。

- 🧩 **RSC 最初确实解决了大依赖问题**：当时一个文档页面携带约 358 KiB 的代码渲染和语法高亮依赖，RSC 将这些工作移到服务端，客户端 JS 减少约 153 KiB gzipped，Lighthouse 得分和性能显著提升（例如博客页面 TBT 从 1200ms 降到 260ms）。

- 🔧 **团队创建了更轻量的解决方案**：用 `@tanstack/markdown` 和 `@tanstack/highlight` 替代了旧的大依赖栈，将渲染器大小压缩到 27 KiB transferred（仅比 RSC 版本多了约 18 KiB）。这使得直接在客户端渲染变得可行。

- 📊 **性能对比显示新方案更优**：在当前生产环境中，移除 RSC 后，博客和文档页面的总字节数、总阻塞时间均低于旧 RSC 版本（例如博客总字节从 1,086 KiB 降到 889 KiB，TBT 从 139ms 降到 66ms）。Lighthouse 分数相近甚至持平。

- 🔄 **多页面场景下 SSR 更具优势**：用户平均每次会话访问 6 页，RSC 每导航都要传输渲染的 Flight payload（因页面而异，每页多出 1.5–5.6 KiB），而常规 SSR 只需加载一次小渲染器（27 KiB），后续仅传输纯内容数据，累计节省更多。

- 🧠 **代码复杂性降低**：RSC 导致上下游边界复杂——内容文件需区分服务器/客户端、组件需了解序列化、依赖图问题频出。移除后的代码更直观，服务器函数直接返回原始数据，客户端组件直接渲染 Markdown，不再需要混合 Flight payload。

- ❌ **RSC 停止“物有所值”**：RSC 解决依赖问题后，留下的运行边界、序列化、特殊文件等开销失去了合理性。团队更倾向于直接缩小依赖，而非用架构隐藏依赖。

- 🤝 **RSC 支持与使用分离**：TanStack Start 将继续支持 RSC 作为可选能力，但不再默认强制使用。该框架允许不同应用自行选择，团队认为大多数应用当前不需要 RSC。

---

### [TanStack | 面向网络的开源应用栈](http://tanstack.com/)

**原文标题**: [TanStack | The open-source application stack for the web.](http://tanstack.com/)

TanStack 是一个开源的全栈应用工具集，提供类型安全、框架无关、生产级、无供应商锁定的库，帮助开发者高效构建现代 Web 应用。

- 📚 丰富的库生态：涵盖 Router、Query、Form、Store、Virtual、AI、DB、Markdown 等，覆盖路由、数据获取、状态管理、UI 组件等核心领域。
- 🔧 核心设计原则：框架无关（支持 React、Vue、Svelte、Solid、Angular 等）、类型安全（TypeScript 原生）、生产级（经大厂验证）、无供应商锁定（MIT 许可、社区驱动）。
- 🌐 活跃的社区与支持：提供 Discord 实时交流、GitHub 源码与问题讨论、YouTube 官方教程，以及企业支持和合作伙伴赞助。
- 👥 核心维护者团队：由 Tanner Linsley、Dominik Dorfmeister 等资深开发者主导，覆盖 React、Solid、Vue 等多个框架的维护和文档建设。
- 📝 最新动态：推出全新品牌设计（Logo、设计系统）、发布 TanStack Markdown 和 Highlight 两个轻量库，以及关于 React Server Components 的实践分享。

---

### [介绍 TanStack Markdown 与 TanStack Highlight | TanStack 博客](https://tanstack.com/blog/introducing-tanstack-markdown-and-highlight)

**原文标题**: [Introducing TanStack Markdown and TanStack Highlight | TanStack Blog](https://tanstack.com/blog/introducing-tanstack-markdown-and-highlight)

TanStack 发布了两个精简库：TanStack Markdown 和 TanStack Highlight，旨在解决技术文档页面因 Markdown 解析和语法高亮导致的体积臃肿问题。通过将解析与高亮分离、采用纯数据 AST、最小化依赖和流式支持，使前端渲染体积大幅降低，并已用于 tanstack.com 生产环境。

- 📦 背景：过去 tanstack.com 的文档页传输约 1.1 MiB 脚本，其中 358 KiB 仅用于语法高亮；团队放弃用 RSC 隐藏问题，转而让依赖变得小巧。
- 🔧 核心原则：解析和高亮是两个独立任务，TanStack Markdown 负责解析成可序列化的文档树，TanStack Highlight 负责将代码转成语义 HTML，互不导入，通过回调连接。
- 🌲 Markdown AST 是纯数据：解析结果就是普通对象/数组，可跨服务端、缓存、搜索索引，并支持 React、HTML 等多种渲染方式；包体积约 4.9 KB（gzip）解析器加 6.7 KB 渲染器。
- ⚡ 流式优化：AI 流式输出时，TanStack Markdown 采用重新解析策略而非维护增量状态，避免中间态协调问题，额外体积仅 0.2 KB。
- 🚀 高亮极致精简：TanStack Highlight 专为网页展示设计（非编辑器），核心 1.7 KB，9 种语言文档集 5.8 KB，全部 25 种语言约 8 KB；无初始化 Promise、无自动检测、无隐式全语言注册。
- 🎨 主题分离：输出仅含语义类名（`th-*`），无内联颜色；主题生成 CSS 变量，切换亮暗仅需 CSS 操作，无需重新高亮。
- ✅ 测试驱动：基于 2940 个真实文档文件（333 个固定样本）做回回归测试，覆盖令牌准确性、体积预算、渲染一致性。
- 🏢 实际效果：tanstack.com 使用后，页面传输体积降至约 27 KiB，移除了内容专属的 RSC 路径，浏览器可复用渲染器。
- 🔄 当前状态：alpha 阶段，合约可能变动；适用于已知技术内容的网页渲染，不支持完整 CommonMark、MDX 评估或编辑器级高亮。

---

### [将引用稳定性作为一种类型](https://www.jovidecroock.com/blog/referential-stability-types/)

**原文标题**: [Making Referential Stability a Type](https://www.jovidecroock.com/blog/referential-stability-types/)

overview summary  
本文提出将引用的稳定性（referential stability）作为类型系统的一部分，通过一个私有 phantom brand（`Stable<T>`）来标记对象、数组和函数，使其在跨渲染中保持相同引用。作者设计了一个独立的导入入口，为 `useMemo`、`useCallback` 等 hooks 提供更严格的依赖检查，并在依赖不稳定时给出明确的类型错误。同时支持 `createStableContext` 和 `stable()` 辅助函数，将稳定性契约从运行时提升到类型层面，对人类开发者与编码代理均有帮助。

- 🔗 **问题背景**：大型 (P)React 项目中，引用稳定性常靠 `useMemo`/`useCallback` 手动维护，缺乏类型保证，易引发不必要的重渲染或副作用执行。  
- 🛡️ **Stable 类型**：使用 `unique symbol` 作为 phantom brand，对对象、数组、函数进行标记，原语类型（如 `string`）直接通过；品牌表示引用在无关渲染间保持稳定，并非永不改变。  
- 📦 **独立导入入口**：从 `stableref/react` 而非模块增强方式引入 hooks，避免因回退到原始宽松重载而丢失稳定性证明；依赖列表不满足时直接报错，错误信息包含修复提示。  
- 🔁 **hooks 增强**：`useMemo`、`useCallback` 的依赖元组严格推断，未证明稳定的依赖会触发类型错误，确保稳定性契约在源头失效。  
- 🎁 **React 自带稳定源**：`useState` 返回的 state 和 dispatcher、`useRef` 返回的 ref 对象自动标记为 `Stable`；初始化闭包无需证明（它们不构成依赖列表）。  
- 🌐 **Context 集成**：`createStableContext` 要求 Provider 的值必须为 `Stable<T>`，将稳定性责任集中在值所有者处，消费者无需关心实现细节。  
- ⚡ **Preact 支持**：提供 `stableref/preact` 入口，应用相同机制，保持与渲染库无关的证明契约。  
- ⚠️ **局限性**：类型断言 `as Stable<T>` 可以绕过品牌，无法完全阻止；`stable()` 辅助函数用于模块级常量，不应随意使用。  
- 🤖 **对编码代理的价值**：代理难以察觉隐性重渲染，但能响应类型错误；显式的错误信息让构建保持红色直到依赖稳定，适合代码生成时代。  
- 💡 **更大意义**：将通常靠注释、lint 规则、隐性知识的属性（如引用稳定性）纳入类型系统，让契约在组件层级间传递，而不仅仅是运行时工作。

---

### [在 Next.js 中尝试 RSC 以提升性能和用户体验 | Aurora Scharff](https://aurorascharff.no/posts/experimenting-with-rsc-for-performance-and-ux-in-nextjs/)

**原文标题**: [Experimenting with RSCs for Performance and UX in Next.js | Aurora Scharff](https://aurorascharff.no/posts/experimenting-with-rsc-for-performance-and-ux-in-nextjs/)

本文介绍了在 Next.js App Router 中利用 React Server Components 和 Server Functions 优化用户体验和性能的三种实验性模式，包括 URL 驱动的“加载更多”、静态壳的即时搜索以及服务端渲染的草稿预览。

- 🚀 使用 Server Components 在服务端获取和渲染数据，减少客户端代码和请求，提升初始加载速度。
- 🔗 “加载更多”功能通过 URL 参数驱动：客户端按钮仅更新 URL，服务端根据 `?page=` 参数流式渲染新页面，支持刷新保留和分享。
- 🔍 搜索输入框作为静态壳即时渲染，不依赖 `searchParams`，通过内联脚本和布局效果在冷加载和软导航后填充查询值。
- 🌊 搜索结果在 `<Suspense>` 边界内流式加载，过渡期间用 `useTransition` 提供全局 pending 状态，支持结果列表淡入淡出。
- 📝 消息编辑器中的预览通过 Server Function 返回 `JSX`，让服务端用 `Shiki` 高亮代码块，保持客户端轻量，且与正式发布效果一致。
- 🧩 关键原则：将分页参数和搜索查询放入 URL，利用 `Suspense` 边界分离动态部分，把服务端渲染的输出作为 `children` 传入客户端组件。
- ⚡ 使用 `Partial Prerendering` 将静态壳预渲染到 CDN，动态部分流式填充，最大化首次绘制速度。
- 🛠️ 另一种“加载更多”方案用客户端状态配合 Server Function 请求单页，适合临时预览，但失去 URL 可分享性。

---

### [如何在生产环境中发现 Next.js 内存泄漏](https://xabierlameiro.com/blog/nextjs/nextjs-memory-leak-in-production)

**原文标题**: [How to find a Next.js memory leak in production](https://xabierlameiro.com/blog/nextjs/nextjs-memory-leak-in-production)

该文章深入探讨了 Next.js 中三种已确认的内存泄漏问题及其诊断与缓解方法，并涵盖了服务器端与 Serverless 环境下的不同表现，同时分享了作者自用的优化技巧与测量工具。

- 🔍 **三大框架泄漏根源**：文章明确指出截至 2026 年 7 月，Next.js 15.5 至 16.3 版本存在三个已知内存泄漏——路由器 LRU 缓存不计数 Key（缓慢积累）、RSC 渲染树在客户端断开时残留（按流量增长）、以及中间件中未被释放的 setTimeout ID（阶梯式增长）。

- 📈 **内存趋势关联定位法**：通过绘制 heapUsed 随时间的变化曲线，并与唯一 URL 数、总请求量、中间件路径进行关联，可快速判断是哪个泄漏在作祟：单调漂移对应 LRU 缓存，流量相关且受客户端断开影响对应 RSC 树，阶梯式增长对应中间件超时。

- 💾 **确认诊断的利器：堆快照**：使用`NODE_OPTIONS='--inspect' next start`暴露 Node 调试器，在负载前后分别抓取堆快照并对比，若 retainer 链中出现`LRUNode`、`reactServerStream`或`TimeoutsManager`，即可确认属于框架泄漏，而非用户代码。

- 🛠️ **针对性缓解方案**：针对 LRU 缓存泄漏，可在代理/CDN 层归一化或过滤恶意 URL 以减少独特路由数；针对 RSC 树泄漏，可裁剪重型页面的 RSC 负载（如分页列表）；针对中间件泄漏，则应在 setTimeout 回调中显式调用 clearTimeout 以释放 ID。

- ⚡ **Serverless 下的伪装：504 超时**：在 Vercel 等 Serverless 平台上，内存泄漏通常不会直接导致 OOM，而是转化为 504 函数调用超时。作者遇到的真实案例是自身的 MDX 解析算法低效（O(N²)），通过模块级缓存将 tag 页渲染从 32 秒降至 134 毫秒。

- 🧪 **自动化测量工具：next-leak**：作者将手动堆快照对比过程封装为 CLI 工具`next-leak`，可在 3 分钟内自动运行负载、强制 GC、输出 post-GC 曲线并识别 retainer 链，大幅降低诊断门槛。

- ✅ **重要检查清单**：遇到 Next.js 内存问题，先看 retainer 链而非猜测；将内存趋势与唯一 URL、流量、中间件进行关联；调整--max-old-space-size 无法解决根本泄漏；Serverless 环境下改为分析执行时间而非内存；若 retainer 指向自建模块的 closure 或结构，则是用户代码问题。

---

### [](https://dx-styles.dev/blog/state-of-zero-runtime-css-in-js/)

**原文标题**: [The state of zero-runtime CSS-in-JS, mid-2026 â dx-styles blog](https://dx-styles.dev/blog/state-of-zero-runtime-css-in-js/)

2026 年零运行时 CSS-in-JS 的生态地图：从运行时到编译时的演进，各库特点、适用场景与未来趋势。

- 📜 **背景转变**：运行时 CSS-in-JS（如 styled-components）因 React 并发渲染和服务端组件而失势，Tailwind 成为主流但存在爱恨争议。
- 🚀 **编译时分支存活**：样式在构建时编译为 .css 文件，运行时仅保留类名字符串，保留类型安全与组件内联，但需构建步骤和静态评估约束。
- 🗺️ **生态地图**：主要库包括 vanilla-extract（TypeScript CSS Modules，文件分离）、Panda CSS（原子化、配置优先）、StyleX（大规模确定性合并）、next-yak（styled 语法编译，快速构建）、Linaria（原零运行时库，稳定）、dx-styles（面向设计系统，具语义类名与解释工具）。
- ⚖️ **选择指南**：大型 styled-components 代码库→next-yak（快）或 Linaria（可过渡）；新建应用→vanilla-extract（文件分离）或 Panda（原子化）；组件库/设计系统→dx-styles（语义稳定）；超大规模团队→StyleX（约束防冲突）；想省心→Tailwind 或 CSS Modules。
- 🔮 **未来方向**：各家趋向收敛，均编译为“纯元素 + 类名”；构建成本成为下个竞争点，已有基准测试工具，作者将发布可复现的构建时数据。

---

### [](https://sergiodxa.com/tutorials/think-in-remix-ui-instead-of-react)

**原文标题**: [Think in Remix UI Instead of React](https://sergiodxa.com/tutorials/think-in-remix-ui-instead-of-react)

Remix UI 的思维方式与 React 不同：组件只运行一次，返回一个渲染闭包，通过调用 `handle.update()` 显式触发更新，使用局部变量、`handle.props` 和 `handle.context` 管理状态。

- 🎯 组件思维转变：不再像 React 那样每次状态变化都重新执行函数，而是设置一次状态，返回渲染闭包，通过 `handle.update()` 触发视图更新。
- 🧩 局部变量管理状态：在组件设置作用域中用普通变量（如 `view`、`selectedId`）存储状态，避免使用 hooks。
- 🔄 显式更新：修改状态后必须调用 `handle.update()` 才会重新渲染，不像 React 自动重新执行组件函数。
- 🤝 上下文共享状态：使用 `handle.context` 让子组件读取和修改共享状态，上下文以组件标识为键，而不是字符串。
- 🖼️ 示例画廊组件：展示了如何在 Remix UI 中构建包含网格/列表切换、照片选择和预览的画廊岛屿组件。
- 🚀 服务端渲染优先：`clientEntry` 在服务端渲染，客户端水合后变为交互式，JavaScript 不必须才能显示初始内容。
- 📦 入口文件：通过 `run` 函数加载模块并水合所有客户端条目，确保浏览器端交互生效。
- 🔧 更多控制权：相比 React hooks，Remix UI 要求更多手动操作，但换来了服务端渲染优先和按需水合的优势。

---

### [](https://infrequently.org/2026/07/state-management/)

**原文标题**: [The Absolute State of Management - Infrequently Noted](https://infrequently.org/2026/07/state-management/)

React 生态系统中的“状态管理”概念存在严重误解。大多数被称作状态管理库的工具实际上只是状态传播机制，不具备时间感知和冲突解决能力。真正的状态管理需要内置时间与顺序概念，才能处理离线同步和实时协作。

- 🚫 大部分“状态管理”库（如 Redux、MobX、Zustand 等）实际上只是事件总线或发布订阅系统，并不真正管理状态。
- ⏰ 真正的状态管理必须包含时间维度和顺序概念，能够处理冲突和重新排序更新。
- 🔄 这些库缺少向量时钟或类似机制，无法确定更新的全局顺序，因此无法可靠地处理离线或实时协作场景。
- ⚡ React 本身也被误称为状态管理系统，实际上它只是 UI 框架，不提供跨时间的一致状态管理。
- 🧩 真正有用的状态管理工具包括 Y.js（CRDT 文本编辑）、Zero（实时同步与协作）和 Fluid（微软的 OT 系统），它们内置了时间感知和冲突解决。
- 🌐 采用这些工具后，离线优先和实时协作成为自然结果，不再需要凑合使用 Apollo 或 Redux 作为同步引擎。
- 💡 文章呼吁开发者认清“状态管理”术语的误导性，转向真正能处理时间与冲突的解决方案。

---

### [Canvas UI：创意画布和 WebGL 组件库](https://canvasui.dev/)

**原文标题**: [Canvas UI: Creative Canvas and WebGL Component Library](https://canvasui.dev/)

Canvas UI 是一套在 Canvas 和 WebGL 中运行的创意组件库，开源、框架无关，支持复制粘贴直接使用。

- 🎨 提供 25 多种精美组件，100% 开源免费，可商用（但禁止转售组件本身）
- 📦 通过 shadcn CLI 一条命令安装（如 `npx shadcn@latest add @canvas-ui/particle-reveal-react`），代码直接放入项目
- 🖱️ 三步使用：挑选组件 → 运行命令 → 自定义（代码归你所有，可随意修改）
- 🔧 每种组件支持 React、Solid、Preact、Vue、Svelte 和原生 TypeScript 六种版本
- 🤖 AI 就绪：支持 shadcn MCP 协议，AI 助手可浏览、安装组件
- ⚙️ 性能优秀：GPU 渲染、脱离 React 循环、离屏暂停、完全卸载，并尊重减少动效偏好
- 🌐 浏览器支持：实时 HTML-in-canvas 需 Chrome 实验标志；其他浏览器中 WebGL 部分正常运作，HTML 兜底渲染
- 🔄 更新方式：代码复制到仓库后不会自动更新，需要时重新运行安装命令

---

### [单元格选择（React）指南 | TanStack Table React 文档](https://tanstack.com/table/beta/docs/framework/react/guide/cell-selection)

**原文标题**: [Cell Selection (React) Guide | TanStack Table React Docs](https://tanstack.com/table/beta/docs/framework/react/guide/cell-selection)

TanStack 是一個集庫、工具、社群與支援於一體的前端生態系統，其核心庫如 React Table 支援進階的表格功能，例如電子表單風格的單元格選取、鍵盤導航與高效能渲染。

- 📚 涵蓋多種函式庫，包括 Framework、Router、Data & State、Query、DB、Store、AI、UI & UX、Table、Charts、Form、Hotkeys 等。
- 🎓 提供豐富社群資源：Discord 即時支援、GitHub 原始碼與議題、官方 YouTube、工作坊及版本發佈說明。
- 🛠️ 開發工具與生態：Builder 起步套件、NPM 統計、Devtools、CLI 工具、合作夥伴與贊助支援。
- 📖 核心指南：涵蓋 Cell Selection 功能，支援矩形選取、Shift 擴展、Ctrl/Cmd 多重選取。
- 🖱️ 滑鼠互動：透過 `onMouseDown` 與 `onMouseEnter` 綁定選取處理器，自動處理拖曳與跨表格邊界放開。
- ⌨️ 鍵盤導航：提供 `moveCellSelection()`、`extendCellSelection()` 等 API，可搭配 TanStack Hotkeys 實現方向鍵與快捷鍵操作。
- 📋 選取複製：`getSelectedCellRangesData()` 回傳原始值陣列，應用層可自行轉換為 TSV 或 CSV 格式。
- 🔄 選取穩定性：以行/列 ID 而非位置儲存選取區塊，排序、篩選、分頁或隱藏欄位後仍能正確保留。
- ⚡ 效能優化：使用 `table.Subscribe` 搭配自訂選擇器，僅重新渲染邊界行，避免大表格拖曳時全量更新。

---

### [更新日志.md](https://raw.githubusercontent.com/remix-run/react-router/main/CHANGELOG.md)

**原文标题**: [CHANGELOG.md](https://raw.githubusercontent.com/remix-run/react-router/main/CHANGELOG.md)

React Router v8.3.0 版本发布，重点更新包括 RSC 自定义入口的调整、路径参数编码改进、会话 ID 生成优化、NavLink 修复以及全面的 TypeScript 7 支持，同时引入多项不稳定功能。

- 📦 **RSC 入口更新** – 自定义 `entry.rsc.tsx` 需传递生成的客户端版本；`entry.ssr.tsx` 需传递完整性哈希和 CSP nonce
- 🔧 **路径编码改进** – 使用 RFC 3986 路径段规则，保留 `$ & + , ; = : @` 等合法字符，不再百分号编码（如 semver 构建号 `1.0.0+1`）
- 🆔 **内存会话 ID 生成** – 改用 `crypto.randomUUID()` 生成 session ID，仅用于本地开发/测试
- 🛠️ **NavLink 修复** – 修复 `to` 结尾带斜杠时 pending 状态不生效的问题
- 🎯 **TypeScript 7 支持** – 多个包（`@react-router/dev`, `@react-router/express` 等）允许使用 TypeScript 7
- ⚠️ **不稳定：RSC 元数据保留** – 路由带有 `clientLoader` 时可跳过不必要的服务器请求
- 🔒 **不稳定：CSRF 加固** – 增强 RSC 的 CSRF 防护代码路径
- 🐛 **不稳定：服务器崩溃修复** – 请求中断时 RSC HTML 流挂起导致的 `TypeError` 已被修复
- 🔄 **不稳定：客户端过期检测** – 在懒路由发现时检测过期 RSC 客户端并重新加载文档
- 🧩 **不稳定：CSP nonce 支持** – 新增 `nonce` 选项，应用于 RSC 文档渲染和组件
- 📦 **不稳定：虚拟模块** – `@react-router/dev` 新增 `unstable_rsc/client-version` 和子资源完整性支持

---

### [发布 v1.6.0 · callstack/reassure · GitHub](https://github.com/callstack/reassure/releases/tag/reassure%401.6.0)

**原文标题**: [Release v1.6.0 · callstack/reassure · GitHub](https://github.com/callstack/reassure/releases/tag/reassure%401.6.0)

overview summary  
reassure 项目发布了 v1.6.0 版本，主要新增了稳定性度量计算以及通过禁用所有者栈来提升渲染稳定性，但页面加载过程中出现了错误提示。

- 🌟 新增稳定性度量计算功能，用于测试运行分析  
- 🔧 禁用所有者栈，改善渲染持续时间稳定性  
- ⚠️ 页面加载时出现错误信息，需手动重新加载

---

### [发布 · facebook/astryx · GitHub](https://github.com/facebook/astryx/releases#release-v0.1.9)

**原文标题**: [Releases · facebook/astryx · GitHub](https://github.com/facebook/astryx/releases#release-v0.1.9)

Astryx 组件库发布了 v0.1.1 至 v0.1.9 多个版本，主要聚焦于新功能增强、可访问性改进、国际化支持、CLI 工具链升级以及大量错误修复，同时完成了从旧命名 XDS 到 Astryx 的品牌迁移。

- 🆕 v0.1.9：新增 Avatar tooltip 属性、Calendar 主题目标、ChatComposer 自定义输入、Table 行状态插件、OverflowList maxVisibleItems 等；修复多组件无障碍和样式问题。
- 🌐 v0.1.8：引入国际化支持（i18n），组件可通过 <InternationalizationProvider> 翻译；新增 DropdownMenu 可选择项、键盘导航 Outline；修复大小冲突、循环数据等。
- 🧱 v0.1.7：新增 useTableGroupedRows、useTableRowIndex 等表格插件；修复生产构建中 jsxDEV 崩溃的问题；CLI 增加 init --features agents 智能体文档生成。
- ♿ v0.1.6：大量无障碍修复，包括 Calendar 屏幕阅读器、Chat 组件 ARIA 属性、键盘焦点管理等；新增 useAnnounce、useKeyboardHint、VisuallyHidden 等辅助钩子。
- 📦 v0.1.5：新增 useTableStickyColumns 粘性列插件；修复 SSR 水合、移动端导航、Slider 轨道可见性等；UMD 构建支持 CDN 直接使用。
- ⚙️ v0.1.4：提供 CDN 预构建包（astryx.umd.js）；新增 prebuilt UMD、astryx build CLI 命令（自然语言搜索页面组合）；修复大量布局和主题错误。
- 🔄 v0.1.3：弃用 old xds 名称，重命名 tokenDefaults、xdsTokenDefaults；新增 ToggleButton 中断式过渡；修复 Layout content 渲染、Selector 双重焦点等。
- 📝 v0.1.2：增强文档，补充缺失的 prop 示例和 playground 默认值；Markdown 组件不再默认使用 <p>；调整颜色 token 映射（active→accent）。
- 🧹 v0.1.1：完成 xds 命名清理，所有集成导出（vite、next）重命名为 Astryx；新增 astryx build 命令；修复 DateInput 页面崩溃等关键问题。

---

### [](https://www.youtube.com/watch?v=2aKGR4RECj0)

**原文标题**: [TanStack is Doing What? - YouTube](https://www.youtube.com/watch?v=2aKGR4RECj0)

这是 YouTube 网站底部常见的链接与版权信息列表，涵盖平台介绍、法律条款和功能说明。

- ℹ️ 关于：提供平台基本信息
- 📰 新闻：发布官方动态与更新
- ©️ 版权：说明内容版权相关事项
- 📞 联系我们：提供联系方式与渠道
- 🎬 创作者：针对内容创作者的资源
- 📢 广告：展示广告合作与投放信息
- 💻 开发者：面向开发者的接口与工具
- 📜 条款：用户使用协议与服务条款
- 🔒 隐私：说明数据收集与隐私保护
- 🛡️ 政策与安全：平台规则与行为准则
- ⚙️ YouTube 运作方式：解释平台机制与算法
- 🧪 测试新功能：介绍正在测试的实验性功能
- 📅 版权归属：© 2026 Google LLC 版权声明

---

### [TanStack 全新亮相 | TanStack 博客](https://tanstack.com/blog/tanstack-has-a-new-look)

**原文标题**: [TanStack Has a New Look | TanStack Blog](https://tanstack.com/blog/tanstack-has-a-new-look)

TanStack 近期进行了全面的品牌视觉更新，由首位首席设计师 Andy Beutler 主导，从 logo、字体、设计令牌到组件库全部焕新。文章阐述了这次升级背后的思考：希望在 AI 能轻易做出“干净”设计的时代，保持人性化的温度与克制，让工具和品牌都传达出“让开发者把时间还给生活”的理念。

- 🌴 品牌焕新：TanStack 推出全新视觉系统，包括新 logo、全局字体、设计令牌和组件库，由首席设计师 Andy Beutler 全职打造。
- 🎨 设计理念：拒绝 AI 式的“完美”，追求有温度、克制的设计，希望品牌“感觉有人在乎过”，而非机器生成。
- ⏳ 核心价值：“把时间还给你”——无论是 Query、Router 还是 Start 等库，目标都是减少开发者的重复劳动，让他们能多陪伴家人、享受生活。
- 🏝️ 海滩元素延续：棕榈树、岛屿等轻松意象并非装饰，而是象征“你尽可放心，去好好生活”。
- 🧩 设计系统 /ds：建立统一的颜色、类型和组件规范，让决策有据可依，长期维护更一致、更可持续。
- 🤖 应对 AI 时代：在 AI 能快速生成常规设计的当下，坚持“宁可少做，但要做对”，避免品牌显得廉价或机械。
- 🔧 开源初心不变：品牌升级不牺牲库、文档和社区质量，仍由真实开发者维护真实问题。

---

### [使用性能追踪进行 React 调试 - YouTube](https://www.youtube.com/watch?v=B_w1xFbRvCg)

**原文标题**: [React Debugging with Performance Tracks - YouTube](https://www.youtube.com/watch?v=B_w1xFbRvCg)

YouTube 页脚区域列出了网站的核心导航链接，包括关于、新闻、版权、联系方式、创作者、广告、开发者、使用条款、隐私政策、平台安全、运作机制、新功能测试以及版权归属等信息。

- 📖 关于与新闻（About & Press）  
- ©️ 版权声明（Copyright）  
- 📞 联系我们（Contact us）  
- 🎬 创作者（Creators）  
- 📢 广告合作（Advertise）  
- 💻 开发者（Developers）  
- ⚖️ 条款与隐私（Terms & Privacy）  
- 🛡️ 政策与安全（Policy & Safety）  
- ⚙️ YouTube 运作方式（How YouTube works）  
- 🧪 新功能测试（Test new features）  
- ©️ 版权年份（© 2026 Google LLC）

---

### [](https://surveyjs.io/?utm_source=this-week-in-react&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=this-week-in-react&utm_medium=email)

SurveyJS 是一套开源、可自托管的 JavaScript 表单与调查管理库，提供表单渲染、拖拽创建、数据可视化和 PDF 导出等功能，让开发者完全掌控数据所有权和隐私合规。

- 📝 **核心组件**：Form Library（MIT 许可的交互表单渲染）、Survey Creator（拖拽生成 JSON 配置）、Dashboard（交互式图表与表格分析）、PDF Generator（导出可编辑或预填的 PDF）。
- 🔓 **开源与自托管**：全部库开源在 GitHub，数据存储在自有数据库，无第三方介入，保障隐私与合规（HIPAA、GDPR 等）。
- ♿ **无障碍**：符合 WCAG、Section 508、ARIA 标准，支持键盘导航与屏幕阅读器。
- ♾️ **无限使用**：无管理员、受访者、表单数、提交量等任何限制。
- 🛠️ **高度可扩展**：支持自定义输入字段、复合问题类型，可集成 React/Vue/Angular 组件。
- 📴 **离线能力**：支持离线创建、编辑和收集数据，联网后自动同步。
- 💰 **一次性授权**：开发者许可一次购买永久使用，含 12 个月维护与技术支持。
- ✅ **灵活验证**：内置及自定义客户端/服务器端验证规则。
- 🎨 **白标与主题**：完全控制 UI 外观，使用 CSS 变量自定义主题，支持多设计复用。
- 🤖 **AI 辅助**：通过 API 集成自然语言表单生成、翻译和智能建议。
- 🏥 **行业适用**：保险、医疗、教育、HR、电商、银行等，满足敏感数据收集需求。
- 📦 **后端无关**：仅提供前端 UI 库，需自行构建后端处理数据存储与用户管理。

---

### [React 的 JSON 表单库 | 拖放界面，任意后端](https://surveyjs.io/try/reactjs)

**原文标题**: [JSON Form Libraries for React | Drag-and-Drop Interface, Any Backend](https://surveyjs.io/try/reactjs)

SurveyJS for React 是一套客户端 JavaScript 库，用于在 React 应用中构建表单和调查管理系统，包含表单渲染、可视化设计、数据分析与 PDF 导出四大模块。

- 📝 **Form Library（表单库）**：从 JSON 渲染动态表单和调查，支持多页、条件逻辑、验证、计算值、文件上传等多种功能
- 🎨 **Survey Creator（调查创建器）**：拖拽式可视化表单构建器，可嵌入应用，用户无需编码即可设计表单，自动生成 JSON 结构
- 📊 **Dashboard（仪表盘）**：通过图表、表格等方式分析调查结果，支持实时更新、筛选排序、自定义可视化及导出
- 📄 **PDF 生成器**：将相同 JSON 表单转换为可打印、可编辑或只读的 PDF 文件，支持自定义字体、页面布局与主题
- 🔗 **后端无关**：SurveyJS 仅运行于客户端，表单模式和响应数据完全由用户自己的后端存储，不受限于特定数据库或服务器
- 🔧 **支持 Next.js**：可与 Next.js 应用无缝集成，使用 React 包即可
- 💡 **开源与商用**：Form Library 采用 MIT 开源许可，其他组件（Survey Creator、Dashboard、PDF Generator）为商业库，但源代码可在 GitHub 获取

---

### [最小可行产品营销的注意事项 - PostHog](https://posthog.com/blog/minimum-viable-product-marketing?utm_source=twir&utm_campaign=jul29)

**原文标题**: [The do's and don'ts of minimum viable product marketing - PostHog](https://posthog.com/blog/minimum-viable-product-marketing?utm_source=twir&utm_campaign=jul29)

PostHog 采用“最小可行产品营销”方法，强调快速发布和实际行动，而非繁琐计划。通过个性化清单、聚焦冲突、简化沟通等策略高效发布产品，避免销售赋能材料、营销剧场和不必要的共识。

- 🎯 聚焦行动，为每次发布定制个性化清单，而非统一流程  
- ✍️ 先写标题，标题不明确则说明发布方向不清  
- ⚔️ 聚焦冲突，用冲突（如与股东或行业的矛盾）吸引眼球  
- 📢 内部提前通知团队，确保支持部门做好应对  
- 📧 以邮件为起点，优先简洁清晰，再扩展至博客等渠道  
- ⏳ 不因制作计划或视频调色等拖延发布  
- 🚫 避免营销剧场，如倒计时、预购等损害用户体验的做法  
- 📄 不做一页纸或作战手册，销售团队直接阅读文档  
- 🗑️ 删除冗余背景，直接切入主题，不说“兴奋地宣布”  
- 📮 不依赖新闻稿，直接联系记者，用六句话加简短视频  
- 💬 避免为达成共识而接受所有反馈，不必让非专业人士当编辑  
- 📈 销售内容（如案例）在发布后三周再写，更真实持久  
- 🔗 将新功能嵌入用户入职流程，利用自动化触发邮件  
- 🔄 尝试不同渠道（如 Hacker News、实时人物社交），放弃无效方式

---

### [](https://github.com/react-native-community/discussions-and-proposals/pull/1014)

**原文标题**: [RFC: CSS calc() in React Native by paradowstack · Pull Request #1014 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1014)

该提案旨在为 React Native 引入 CSS `calc()` 支持，但当前页面加载时发生错误，导致内容无法正常显示。提案编号为#1014，由 paradowstack 发起，社区成员已有多项反应（点赞、爱心等）。

- 🧮 提议在 React Native 中支持 CSS `calc()` 函数，以实现动态尺寸计算
- 📱 该 RFC 属于 react-native-community/discussions-and-proposals 仓库
- 📝 提案由 paradowstack 提交，当前处于开放状态
- ⚠️ 页面加载时出现错误，提示“请重新加载此页面”，可能影响内容查看
- 👍 社区反应：9 个点赞、6 个爱心、2 个关注表情

---

### [](https://github.com/react/react-native/pull/57500)

**原文标题**: [SafeAreaProvider, safe-area hooks, and SafeAreaView edges/mode by Abbondanzo · Pull Request #57500 · react/react-native · GitHub](https://github.com/react/react-native/pull/57500)

此拉取请求将 React Native 核心的安全区域 API 与 `react-native-safe-area-context` 功能对齐，新增 SafeAreaProvider、Hooks（`useSafeAreaInsets` / `useSafeAreaFrame`）及 SafeAreaView 的 `edges` 与 `mode` 属性，并完成 Android 原生实现（iOS 后续跟进），目标架构为 Fabric。

- 📱 新增 `SafeAreaProvider` 组件，测量窗口安全区域并透过 Context 提供边距与框架。
- 🔧 新增 `useSafeAreaInsets()` / `useSafeAreaFrame()` Hooks，以及 Context、HOC 和监听器。
- ⚡ 提供 `initialWindowMetrics` 用于同步预填边距/框架，避免首帧跳跃。
- ✂️ `SafeAreaView` 新增 `edges`（每边可选 off / additive / maximum）和 `mode`（padding / margin）属性，边距转换逻辑由共享 C++ 节点实现，iOS 与 Android 共用。
- 🧩 Android 上 `SafeAreaView` 将边距报告给 Fabric 状态但不消耗，保证嵌套 Provider/View 计算正确；新增原生 `SafeAreaProvider` 通过 `onInsetsChange` 事件向 JS 报告边距与框架。
- 💬 作者与社区讨论：保留并改进 SafeAreaView 而非移除，仍属概念验证阶段，未计划合并以防止用户反复变动。

---

### [发布 5.0.0-alpha.1 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/5.0.0-alpha.1)

**原文标题**: [Release 5.0.0-alpha.1 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/5.0.0-alpha.1)

react-native-screens 5.0.0-alpha.1 版本发布，新组件从实验包移出可直接导入，旧组件标为遗留但继续支持，同时修复多项问题并优化测试与依赖。

- 🚀 新版本发布：5.0.0-alpha.1 首次 alpha，新组件（Stack、Split、FormSheet 等）可直接导入，旧组件分为遗留但仍可引用。
- ✅ 功能改进：Android 升级 Material 库、增加 FormSheet v5 的 initialDetentIndex/onDetentChanged 支持、iOS 菜单新增 displayAsPalette/displayInline 标志、重构代码目录结构。
- 🐛 错误修复：修复 Android 快速导航导致屏幕卸载、iOS Split 视图 ShadowState 故障、Android Stack v4 默认 inset 属性、类型依赖问题等。
- 📋 其他优化：更新 react-navigation 子模块、聚合 Dependabot 更新、完善测试场景及导出。

---

### [](https://github.com/react/react-native-website/pull/5191)

**原文标题**: [feat(style): remove experimental_ prefix from backgroundImage RN 0.87.x by retyui · Pull Request #5191 · react/react-native-website · GitHub](https://github.com/react/react-native-website/pull/5191)

概述：Pull Request #5191 成功合并，移除了 React Native 0.87.x 中 `backgroundImage` 属性的 `experimental_` 前缀。

- 📦 合并了来自 `retyui` 的 PR，移除了 `backgroundImage` 的 `experimental_` 前缀，适用于 RN 0.87.x 版本
- 🔗 引用上游 commit：`react/react-native@58688bf`
- 👀 评论指出未来可能有更多 API 会移除该前缀（如 `react/react-native#57563`）
- ✅ 代码审核由 `Simek` 完成并合并到 `react:main` 分支

---

### [](https://github.com/react-navigation/react-navigation/pull/13195)

**原文标题**: [feat: make native package work without react-native-web by satya164 · Pull Request #13195 · react-navigation/react-navigation · GitHub](https://github.com/react-navigation/react-navigation/pull/13195)

该 PR 使 `@react-navigation/native` 无需依赖 `react-native-web` 即可在普通 React Web 应用中使用，并对 `Link` 组件 API 做出多项调整与破坏性变更。

- 🚀 核心改进：`@react-navigation/native` 现在无需安装或别名 `react-native-web` 即可在标准 React Web 应用上运行
- 🔧 `Link` 组件新增硬编码的受支持 prop 列表，仅接受声明内的属性
- ⚠️ `numberOfLines` 仅在原生端受支持，Web 端需使用样式替代
- ⚠️ `target` 不再自动标准化（如不再为 `_blank` 自动添加 `_`），需直接传递带 `_` 的值
- ✨ `className` 现为 Web 端有效 prop，可通过类名自定义样式
- 🛠 `style` 仅接受普通对象，不再支持嵌套数组；如需组合样式应使用 `StyleSheet.compose`
- 🗑 移除了 `accessibilityX` 等废弃 prop，改用 `aria-x` 系列 prop

---

### [Suspense 和待处理 UI | React Navigation](https://reactnavigation.org/docs/8.x/suspense/)

**原文标题**: [Suspense and pending UI | React Navigation](https://reactnavigation.org/docs/8.x/suspense/)

React Navigation 8.x 中，Suspense 用于处理导航时的加载状态，导航会作为 React 过渡运行，保持当前屏幕可见直至目标就绪。通过选择合适的 Suspense 边界位置（导航器、屏幕或屏幕内部分区），可以控制加载 UI 的显示方式，同时利用 `useTransition` 显示待处理状态，并用错误边界处理加载失败。

- 🧩 **Suspense 边界**：内容未就绪时显示 fallback，只有通过 `React.lazy`、`React.use` 或集成 Suspense 的框架读取的数据才能触发。
- 🚦 **导航行为**：导航作为 React 过渡执行，期间当前屏幕保持可见和交互，直到目标内容加载完成；非过渡操作（如原生返回）则直接显示 fallback。
- 📍 **边界位置选择**：围绕导航器的边界保持当前屏幕可见（适合堆栈导航器）；围绕每个屏幕的边界立即显示加载 UI（适合标签导航器）；屏幕内部分区边界允许部分内容先渲染。
- ⏳ **显示待处理 UI**：使用 `useTransition` 和 `useDeferredValue` 在按钮等控件上显示加载指示器，避免闪烁；推荐封装成可复用组件。
- ❌ **错误处理**：结合错误边界捕获加载失败或渲染异常，提供恢复选项（如重试或返回）。

---

### [从 Expo Router 到 Detour：正确实现延迟深度链接 — Expo 博客](https://expo.dev/blog/deferred-deep-linking-the-right-way)

**原文标题**: [From Expo Router to Detour: Deferred deep linking the right way â Expo blog](https://expo.dev/blog/deferred-deep-linking-the-right-way)

我注意到您没有提供需要总结的文本内容。请您提供具体文章或段落，我将立即按照要求生成中文概述和带表情符号的要点列表。

---

### [](https://expo.dev/blog/app-variants-side-by-side)

**原文标题**: [Install dev and production side by side with app variants â Expo blog](https://expo.dev/blog/app-variants-side-by-side)

您没有提供需要总结的文本内容，请粘贴文章或段落，我将按照以下模板为您生成中文要点：

概述总结  
- 🔑 关键点 1  
- 📌 关键点 2  
- ...

---

### [我们为何未将 MMKV 写入移至工作线程：序列化成本 • Andrei Calazans](https://andrei-calazans.com/posts/2026-07-28-mmkv-writes-worklet-serialization-cost/)

**原文标题**: [Why We Did Not Move MMKV Writes to a Worklet: The Serialization Cost • Andrei Calazans](https://andrei-calazans.com/posts/2026-07-28-mmkv-writes-worklet-serialization-cost/)

将同步 MMKV 写入移到后台工作线程，因序列化成本过高而失败，三个实验证明：仅移动写入无效，移动全部处理成本更高，Bundle 模式不改变数据拷贝成本。

- ❌ 问题：JS 线程上的同步 MMKV 写入（约 29.56ms）阻塞了线程，导致动画和手势丢帧。
- 💡 想法：利用 Nitro Modules 特性，将写入移到后台工作线程，但数据拷贝到工作线程有序列化成本。
- 🧪 实验 1：仅将 MMKV 写入移到工作线程，但字符串拷贝（createSerializableString）耗时与原始写入相同（约 29.56ms），无节省。
- 📦 实验 2：将整个数据对象移到工作线程处理，但拷贝大对象耗时约 132ms，比原始写入更差。
- 🚀 实验 3：开启 Bundle 模式后，拷贝成本仍约 136ms，证明序列化成本来自数据而非代码构建模式。
- 📋 结论：工作线程不是免费方案，序列化大对象成本高昂。建议先测量序列化成本，只发送小数据。

---

### [在 React Native 中使用功能标志 | ConfigCat 博客](https://configcat.com/blog/using-feature-flags-in-react-native/?utm_source=thisweekinreact_newsletter&utm_medium=sponsor&utm_campaign=reactnative_202607)

**原文标题**: [Using Feature Flags in React Native | ConfigCat Blog](https://configcat.com/blog/using-feature-flags-in-react-native/?utm_source=thisweekinreact_newsletter&utm_medium=sponsor&utm_campaign=reactnative_202607)

本文介绍了如何在 React Native 应用中使用 ConfigCat 特性标志，实现无需重新部署即可远程控制功能开关，从而加快发布节奏、降低风险。

- 📱 特性标志允许远程控制应用行为，无需等待应用商店审核即可开启或关闭功能。
- 🚀 在 React Native 中特别有用，因为移动端更新需提交构建、等待审核，特性标志可即时禁用问题功能或逐步向部分用户发布。
- 🛠️ 演示场景：使用 `signupButton` 标志控制注册按钮的显示，实现随时暂停新用户注册。
- 📦 步骤包括：创建 React Native 项目、安装 `configcat-react` SDK、在 ConfigCat 仪表盘添加特性标志、用 `ConfigCatProvider` 包裹根组件、通过 `useFeatureFlag` hook 控制按钮渲染。
- ⏱️ 设置 `pollIntervalSeconds: 10` 实现快速查看标志变化效果。
- ✅ 最终效果：在仪表盘切换标志时，无需重新部署即可动态显示或隐藏注册按钮。

---

### [react-native-workers 1.0.0-alpha: React Native 的真正多线程 | react-native-workers](https://ammarahm-ed.github.io/react-native-workers/blog/introducing-react-native-workers/)

**原文标题**: [react-native-workers 1.0.0-alpha: real multithreading for React Native | react-native-workers](https://ammarahm-ed.github.io/react-native-workers/blog/introducing-react-native-workers/)

react-native-workers 1.0.0-alpha 为 React Native 带来了真正多线程支持，允许 JavaScript 在独立后台线程运行，同时保持与主线程的通信、共享内存和原生模块访问。

- 💡 核心思路：每个 Worker 拥有独立的 Hermes 运行时和 OS 线程，遵循 Web Worker API（`new Worker`、`postMessage`、`onmessage`）。
- 🧵 原生模块访问：可启用 `nativeModules: true` 让 Worker 调用 Java/Objective-C 原生模块；Expo 中 `requireNativeModule` 直接可用。
- 🔄 消息传递：通过结构化克隆序列化数据，支持对象、数组、`Date`、类型数组、`ArrayBuffer`及循环引用（暂不支持 `Map`、`Set`、`RegExp`、`Error`、`BigInt`）。
- 📦 共享状态：提供 `SharedStore`（键值存储）、`SharedValue`（可观察单值）和 `SharedBuffer`（零拷贝共享内存，含锁机制），支持跨运行时订阅与同步。
- 🖥️ UIWorker：允许 Worker 直接渲染和更新原生组件，事件由原生层传递而非绕回主线程 JS 线程；运行时可复用或独立。
- 🧪 实验性 Thread API：通过 `enableMultiThreadingExperimental()` 启用，允许同一运行时临时在不同线程（如主线程或自定义线程）执行闭包，无需序列化，保持变量一致。
- 🛠 调试支持：`console.*` 输出带 `[Worker:<name>]` 标签；每个后台 Worker 在 DevTools 中独立可调试（断点、单步）；UIWorker 需显式 `inspectable: true`。
- 🔧 兼容性：支持 React Native 0.81.4+ 新架构（桥接模式、Hermes、JSI）；已测试 RN 0.81–0.86 及 Expo SDK 54–latest；含设备端符合性测试套件和性能基准屏。
- ⚠️ Alpha 状态：核心功能实现并测试，但 API 可能调整；结构化克隆类型有限；发布构建需额外构建步骤；Thread API 仍为实验性，可能变更形状。
- 🚀 未来方向：扩展结构化克隆范围（`Map`、`Set` 等）；实现传输列表（零拷贝移交）；将 Thread API 定型或调整。

---

### [](https://wcandillon.github.io/react-native-webgpu/docs/integrations/react-native-skia)

**原文标题**: [React Native Skia](https://wcandillon.github.io/react-native-webgpu/docs/integrations/react-native-skia)

React Native WebGPU 与 React Native Skia 的 Graphite 构建能共享同一个 Dawn 实例和 GPU 设备，实现无缝集成与零拷贝纹理互操作。两者版本必须锁定在同一 Dawn 标签下，构建时校验，确保兼容性。

- 🔗 **共享 Dawn 库**：两者使用完全相同的预构建 Dawn 工件，Skia 安装时检测并复用 WebGPU 的 Dawn 副本，避免重复加载。
- ⚙️ **共享 wgpu::Instance**：WebGPU 自动采用 Skia 的实例，所有设备（包括通过 navigator.gpu 创建的）均位于同一实例上。
- 🖥️ **设备互操作**：通过 `Skia.getNativeDevice()` 获取 Graphite 的设备指针，`importDevice()` 包装成标准 `GPUDevice`，设备生命周期由 Skia 管理。
- 🔄 **零拷贝纹理共享**：WebGPU 纹理通过 `nativePointer` 传入 Skia 的 `MakeImageFromNativeTexture` 生成 SkImage；Skia 纹理通过 `MakeNativeTextureFromImage` 输出指针，`adoptTexture()` 包装为 GPUTexture，全程无需数据拷贝。
- 📌 **版本锁定**：Graphite 构建的 Skia 必须与 WebGPU 使用相同 Dawn 标签，构建时自动校验，不匹配则原生构建失败。
- 🧵 **线程安全**：导入的设备遵循相同线程模型，Dawn 内部同步设备访问，Graphite 可并发记录与提交工作。
- 💡 **其他集成**：平台表面（CVPixelBuffer/AHardwareBuffer）可通过 `importSharedTextureMemory` 或 `RNWebGPU.createVideoFrameFromNativeBuffer` 跨边界共享。

---

### [发布 v2.10.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.10.0)

**原文标题**: [Release v2.10.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.10.0)

Shopify/react-native-skia 库发布了 v2.10.0 版本，主要特性是从 host objects 迁移到 native states。

- 🎉 发布 v2.10.0 版本
- 🚀 特性：从 host objects 迁移到 native states（#3964）
- ⏰ 发布于 2026 年 7 月 23 日
- 📦 仓库：Shopify/react-native-skia，Stars 8.5k，Forks 622

---

### [](https://github.com/mrousavy/react-native-vision-camera/releases/tag/v5.2.0)

**原文标题**: [Release Release 5.2.0 · mrousavy/react-native-vision-camera · GitHub](https://github.com/mrousavy/react-native-vision-camera/releases/tag/v5.2.0)

react-native-vision-camera v5.2.0 发布了，主要新增 GPU 缩放模式、SkiaCamera 的目标分辨率和控制属性，并修复了预览分辨率、麦克风检测以及 Nitro 兼容性等问题。

- ✨ 新增 GPU 缩放器中的 `stretch` 缩放模式
- 🌟 为 `<SkiaCamera>` 添加 `targetResolution` 属性
- 📱 为 `<SkiaCamera>` 添加 `zoom`、`exposure` 和 `torchMode` 属性
- ✅ 添加针对 `focus(…, { adaptiveness: 'locked' })` 的 Harness 测试
- 🔧 修复预览分辨率协商偏向 4K 的问题
- 🎤 简化麦克风检测与启用逻辑
- ⬆️ 升级 Nitro 以修复 `@FastNative` 问题（版本 0.36.3）

---

### [发布 · mrousavy/nitro · GitHub](https://github.com/mrousavy/nitro/releases#release-v0.36.3)

**原文标题**: [Releases · mrousavy/nitro · GitHub](https://github.com/mrousavy/nitro/releases#release-v0.36.3)

这是 mrousavy/nitro 项目的版本发布记录，涵盖了从 v0.35.4 到 v0.36.3 的多个版本，主要包含 Bug 修复、性能改进、新功能以及文档更新等内容。以下列出关键版本的核心变更。

- 🐛 **v0.36.3**：修复 `Sync<..>` 函数非 `@FastNative` 的问题。
- ⚡ **v0.36.2**：性能优化（复用缓存的 `PropNameIDs`），并新增对 RN 0.87+ 的支持，同时修复了硬件缓冲区计算等问题。
- 🐛 **v0.36.1**：修复联合内联合并不生成枚举的错误。
- ✨ **v0.36.0**：支持联合样式枚举的变体。
- 🐛 **v0.35.11**：修复 Swift 睡眠、线程池队列同步以及 Promise 状态访问的竞态问题。
- ⚡ **v0.35.9**：提高 Swift Promise 性能，修复 `Promise<void>` 销毁竞争和 `ByteBuffer` 安全复制。
- 🐛 **v0.35.7**：修复 Kotlin 结构体中的泛型警告，并重置 C++ 状态。
- 🐛 **v0.35.6**：修复氮气生成代码的缩进和嵌套数组赋值问题。
- 🐛 **v0.35.5**：让所有 Kotlin 结构体可比较（重写 equals/hashCode），并修复 UI 线程运行方法。
- ✨ **v0.35.4**：为 Swift 和 Kotlin 的 Variant 添加 `asType<T>()` 和 `isType<T>()` 方法，同时修复 Xcode 静态链接问题。

---

### [Expo Open OTA v3: 一台服务器，管理所有 Expo 应用 · Mercure Technologies](https://www.mercuretechnologies.com/blog/expo-open-ota-v3)

**原文标题**: [Expo Open OTA v3: One Server, All Your Expo Apps · Mercure Technologies](https://www.mercuretechnologies.com/blog/expo-open-ota-v3)

Expo Open OTA v3 发布，这是一个开源的自托管 OTA 更新服务器重大更新，支持多应用、渐进式推出、A/B 测试，并引入基于 PostgreSQL 的控制平面模式，同时保留简单的无状态模式，企业版增加 RBAC 和 SSO 等功能，核心仍为 MIT 许可。

- 🚀 发布 Expo Open OTA v3，实现与 Expo 完全解耦，支持多应用单服务器部署
- ⚙️ 新增控制平面模式，基于 PostgreSQL 提供仪表盘、独立认证、API 密钥和应用隔离
- 📊 支持渐进式推出和 A/B 测试，可在服务器层实时回滚，无需应用商店审核
- 🔒 企业版增加 RBAC、OIDC 单点登录、受保护分支和 IP 白名单
- ☁️ 新增 Azure Blob 存储支持，CDN 前端支持任意存储后端
- 📈 所有指标带 appId 标签，便于 Prometheus 和 Grafana 监控
- 🛠️ 无状态模式保留，迁移平滑，现有客户端无需重建
- 📖 提供快速开始指南和 v2 到 v3 迁移说明

---

### [](https://github.com/software-mansion/argent/releases/tag/v0.17.0)

**原文标题**: [Release v0.17.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.17.0)

该版本是软件项目 "argent" 的 v0.17.0 更新，主要包含功能增强、错误修复、内部优化以及新贡献者加入。

- ⚙️ 新增主要功能：`argent config` 大幅改进、`pinch` 手势指令、录制自动拼接、可见触摸效果、远程录制链接等
- 🐛 修复多个 Bug：手势标签在运行序列中标记为 iOS/Android、iOS 分析器停止时崩溃、服务端口冲突处理、移除自引用 node_modules 符号链接
- 🔧 内部优化：更新文档与脚本注释、升级工作区包版本、增加 Windows 支持（Android + Chromium 控制平面）
- ❤️ 感谢新贡献者 @L65FREAD 的首次贡献

---

### [](https://github.com/adithyavis/react-native-canvas-kit)

**原文标题**: [GitHub - adithyavis/react-native-canvas-kit: Skia based 2D canvas framework for react-native · GitHub](https://github.com/adithyavis/react-native-canvas-kit)

这是一个基于 React Native Skia 构建的 2D canvas 框架，内置场景图、形状、手势、变换器和画笔，灵感来自 Konva。

- 📐 **内置多种形状**：提供 Rect、Circle、Ellipse、Line、Text、Image 等，共享统一的变换和样式属性。
- 🤏 **交互与手势**：支持点击、拖拽、捏合缩放和旋转，并在 UI 线程处理多点触控。
- 🎨 **画笔系统**：包含 BrushLayer 和预置画笔（笔、铅笔、马克笔、荧光笔、胶带、橡皮擦）。
- 📦 **安装依赖**：需同时安装 @shopify/react-native-skia、react-native-gesture-handler、react-native-reanimated 和 react-native-worklets。
- 🔖 **版本选择**：1.x 仅支持 Reanimated 4 和新架构；0.x 适用于 Reanimated 3/旧架构。
- 💻 **简洁用法**：通过 Stage → Layer → Group → Shape 层次结构构建画布，示例展示矩形和圆形。
- 🌳 **树状结构**：Stage 是画布表面，Layer 和 Group 提供逻辑分组与变换，Shape 为具体图形。
- 📄 **完整文档**：官方文档网站覆盖安装、核心概念、形状样式、手势、变换器和画笔。
- 📜 **MIT 许可证**：开源且可自由使用。

---

### [React](https://thoughtbot.com/blog/sign-in-with-google-for-react-native)

**原文标题**: [
        Sign in with Google for React Native
    ](https://thoughtbot.com/blog/sign-in-with-google-for-react-native)

这篇文章介绍了 thoughtbot 新发布的 React Native 库 @thoughtbot/react-native-social-auth，它基于 Android 的 Credential Manager 和最新的 iOS SDK 实现现代 Google 登录，提供品牌按钮、Expo 支持以及 TypeScript 优先的 API，填补了现有库对新一代平台 API 支持的空白。

- 🚀 thoughtbot 推出了 @thoughtbot/react-native-social-auth，是一个专为 React Native 打造的现代 Google 登录库，全面支持 Android Credential Manager 和最新 iOS SDK。
- 📱 该库包含符合 Google 品牌规范的按钮组件、第一方 Expo 配置插件和 TypeScript 优先的 API，使用简单。
- 🔄 Google 正在更新 Android 和 iOS 上的登录技术栈：Android 上旧版 GoogleSignInClient 已弃用，推荐迁移到 Credential Manager；iOS 上最新 SDK 增加了 Firebase App Check 和自定义 nonce 支持以增强安全。
- 🧩 现有的 React Native 库仍依赖旧的 Android API 或旧版 iOS SDK，无法利用 Credential Manager 底部弹窗、自动登录和结构化错误处理等新功能。
- ✅ 新库正好弥补了这一差距，为开发者提供了面向未来的 Google 登录解决方案。

---

### [](https://github.com/mdjastrzebski/react-native-memory-footprint)

**原文标题**: [GitHub - mdjastrzebski/react-native-memory-footprint: Measure your React Native app's memory footprint on iOS and Android. · GitHub](https://github.com/mdjastrzebski/react-native-memory-footprint)

这是一个轻量级的 React Native 库，用于读取 iOS 和 Android 上应用的真实内存占用，采用各平台官方定义的内存量度标准。

- 📦 **安装**：通过 `npm install react-native-memory-footprint` 完成集成。
- 🚀 **用法**：调用 `getMemoryFootprint()` 即可获取当前进程内存占用（字节），示例代码输出 MB 值。
- 📊 **API**：`getMemoryFootprint(): number` 返回字节数；iOS 基于 `phys_footprint`（与 Xcode 内存表一致，Jetsam 使用），Android 基于匿名 RSS + swap（与 Play Vitals 一致）。
- 🍎 **iOS 计算原理**：采用脏页 + 压缩内存（不含干净内存），公式来自 XNU 内核，是 Jetsam 终止应用的直接依据。
- 🤖 **Android 计算原理**：读取 `/proc/self/status` 中的 `RssAnon` + `VmSwap`，避免 PSS 的共享分摊偏差，更接近实际被 kill 的风险。
- 🎯 **选择该指标的原因**：iOS 与 Xcode/Jetsam 同步；Android 与 Play Console 性能指标一致，且低内存杀死守护进程（lmkd）也基于 RSS。
- 📚 **延伸阅读**：提供官方文档、内核源码、WWDC 演讲、AOSP lmkd 源码等链接供深入理解。
- 🤝 **贡献指南**：包含开发流程、PR 提交、行为准则和 MIT 许可证。
- 🌟 **项目信息**：9 颗星，0 forks，基于 create-react-native-library 创建。

---

### [Maestro CLI 2.7.0：使用 AI 代理调试云端运行](https://maestro.dev/blog/maestro-cli-2-7-0)

**原文标题**: [Maestro CLI 2.7.0: debug Cloud runs with your AI agent](https://maestro.dev/blog/maestro-cli-2-7-0)

Maestro CLI 2.7.0 版本发布，核心亮点是 AI 代理能自动调试 Cloud 运行失败，并新增每个流程的调试包，同时修复了 iOS、Android 和 Web 的多项可靠性问题。

- 🤖 AI 代理现在可通过 Maestro MCP 工具自动调试失败的 Cloud 运行，获取录制、日志和视图层次，解释根因并提出修复方案。
- 📦 每个流程生成独立的调试包，包含 `manifest.json`、`commands.json`、失败截图、视图层次、设备日志及崩溃/ANR 报告。
- 🧠 视图层次独立为文件，`commands.json` 更精简（示例从 246KB 降至 4KB）；步骤文件按人类可读命名（如 `step-003-tapOnElement-submit.png`）。
- 📱 Android 改进：支持任意 Unicode 文本输入（无需外部 APK）、WebView socket 超时（10 秒）、原生 SIGSEGV 崩溃检测、完整云录屏时长、断开连接明确报错。
- 📱 iOS 改进：`scrollUntilVisible` 后点击稳定、UI 错误信息更详细、长流程高可靠性、瞬态错误自动恢复、假崩溃检测修复、iPad/iOS 26 可检查、`setOrientation` 优雅降级、simulator 录制时长一致。
- 🌐 Web/Flutter web 改进：`id` 选择器支持 Flutter web、CSS 选择器匹配包裹子元素、远程浏览器无录制时快速失败、瞬态 JS 错误自动重试。
- 🛠️ CLI 与工具改进：`maestro chat` 停用（改用 Maestro MCP）、`--verbose` 一致输出、并发运行不冲突、Windows 输出正确、文件名含 `/` 时 HTML 报告不崩溃。
- 🚀 贡献者体验：驱动二进制自动更新（无需 PR 提交），macOS 上 E2E 约 3 分钟。

---

### [](https://github.com/software-mansion/radon-ide/releases/tag/v1.18.0)

**原文标题**: [Release v1.18.0 · software-mansion/radon-ide · GitHub](https://github.com/software-mansion/radon-ide/releases/tag/v1.18.0)

该版本 v1.18.0 主要新增了 AI 聊天集成、支持最新版 React Native、Expo 和 Xcode，并修复了多项 Bug。

- 🤖 AI 聊天集成：可在聊天中直接修复运行时错误和引用被检查的组件
- 📱 支持 React Native 0.86 / 0.87 以及 Expo 56 / 57
- 🍎 支持 Xcode 27
- 🐞 修复：网络检查器禁用再启用后日志不丢失等问题
- 🔧 修复：`Set-Cookie` 响应头未传播、缺失 `Content-Type` 头部等多项 Bug

---

### [](https://github.com/callstack/agent-device/releases/tag/v0.20.1)

**原文标题**: [Release v0.20.1 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.20.1)

此版本 v0.20.1 扩展了平台支持，增强了重放录制安全性和验证可靠性，并改进了诊断与恢复指导。

- 📺 新增亚马逊 Vega OS TV 支持：可控制 Vega 虚拟设备中的应用
- 📱 扩展物理 iOS 设备支持：通过 usbmux 支持仅 xctrace 设备的 XCTest 自动化
- 🔒 秘密安全录制：`fill --record-as <VAR>` 在脚本中仅存储占位符，保护敏感输入
- ✅ 更强的重放验证：录制的 `wait` 地标保留元素身份，避免相同标签的误报
- 🔄 更弹性的重放启动：在应用启动时有限重试处理瞬态捕获，不掩盖永久故障
- 🎯 更智能的设备选择：重放能自动选择包含目标应用的模拟器，保留平台与深度链接意图
- 🧭 更好的恢复指导：屏幕外交互错误推荐方向、边界移动和基于选择器的重试
- 🖥️ iOS 系统 UI 指导：新增 SpringBoard 和模拟器小组件添加、编辑、删除工作流帮助
- 🔍 改进的诊断：更丰富、更清洁的会话事件详情便于调查自动化失败
- 🚀 更强的发布信心：大幅扩展基于注册表的 iOS 模拟器覆盖、重放场景、架构门和帮助一致性检查
- ⚠️ 兼容性注意：旧版手势格式（含已移除的 duration/velocity 位置参数）将在解析时失败并提示迁移指导

---

### [3.9 新功能 | 屏幕过渡](https://screen-transitions.esjr.org/changelog/updating-to-3-9/)

**原文标题**: [New in 3.9 | Screen Transitions](https://screen-transitions.esjr.org/changelog/updating-to-3-9/)

v3.9 聚焦于使边界测量更确定、改进重定向、引入简化的 Boundary API 以及新增 contentComponent，同时优化了导航缩放和 transition 协调能力。

- 🎯 边界测量更确定，重定向改进：系统现在更贴近最新测量的源与目标，使动画更精确，并简化了边界交接的公开模型
- 🔄 Transition.Boundary 成为主要边界组件：统一了按压式与被动式边界，废弃之前的 View/Trigger 别名
- 📤 handoff 支持实时负载迁移：在匹配边界间移动 live payload，用于视频、地图等原生视图，需安装可选依赖 react-native-teleport
- 🚀 escapeClipping 允许边界在过渡期间渲染到裁切外：突破局部裁切或布局约束，可与 handoff 组合使用
- 🔍 navigation.zoom() 新增控制参数：暴露外观和拖拽响应控制（drag.translation / drag.scale），并新增 pinchOriginX/pinchOriginY
- 🖼️ contentComponent 自定义屏幕内容渲染：替代已弃用的 surfaceComponent，用于自定义屏幕外壳
- ⏳ blockTransition/unblockTransition 协调过渡启动：参考计数，可保持待定过渡至目标就绪
- 📐 作用域边界 API 统一：bounds(id).styles()/.values()/.link() 替代旧版 helpers，生成动画样式或数值几何，支持 motion 自定义路径
- 🔄 行为变化：屏幕等待目标解析后再应用样式，避免早期帧跳动
- 🧹 迁移重点：优先使用 Transition.Boundary，用 motions 代替手动实现弧形/旋转，移除已弃用 zoom 选项

---

### [发布 8.20.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.20.0)

**原文标题**: [Release 8.20.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.20.0)

概述摘要：Sentry React Native v8.20.0 发布，主要修复 iOS 截图问题、清理 TurboModule 标签、兼容 Gradle 配置缓存，并更新 JavaScript SDK 和 CLI 依赖。  
- 🐛 修复 iOS 8.19.0 起截图失效的问题（反馈小部件截图、attachScreenshot、Sentry.captureScreenshot()），回滚 iOS SentrySDK.internal 迁移  
- 🧹 清除 turboModuleContextIntegration 中空的 turbo_module.name/turbo_module.method 标签，避免活动调用外的事件出现“处理错误”  
- ⚙️ 使 copySentryJsonConfiguration 和 *_SentryUpload Gradle 任务兼容 Gradle 配置缓存，解决 org.gradle.configuration-cache=true 下的构建失败  
- 🔧 依赖更新：JavaScript SDK 从 v10.65.0 升至 v10.67.0  
- 🔧 依赖更新：CLI 从 v3.6.0 升至 v3.6.1

---

### [版本发布 1.5.3 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.5.3)

**原文标题**: [Release Release 1.5.3 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.5.3)

该页面显示 react-native-nitro-fetch 仓库的 v1.5.3 版本发布信息，包含性能优化和依赖更新，但页面加载时出现错误，需要刷新。

- 🚀 发布 v1.5.3 版本
- 🤝 性能优化：复用共享 URLSession 处理流式请求
- 🔧 维护更新：锁定依赖文件
- ⚠️ 页面加载错误，提示“请重新加载页面”
- 📊 项目已获 923 个星标和 37 个 forks
- 👍 收到 3 个点赞反应

---

### [](https://maestro.dev/blog/maestro-mcp-for-ai-coding-agents)

**原文标题**: [Maestro MCP for AI Coding Agents](https://maestro.dev/blog/maestro-mcp-for-ai-coding-agents)

Maestro MCP 让 AI 编码代理（如 Claude Code、Cursor 等）能直接操作真实设备上的应用，检查 UI、运行流程、截图，所有操作都在聊天会话中完成，无需离开 IDE。

- 🤖 **代理操作真实应用**：Maestro MCP 让代理在聊天中直接运行和检查你的应用，结合 Model Context Protocol，支持多种流行编码工具。
- 🛠️ **完整工具集**：包括 `list_devices`（列出设备）、`inspect_screen`（检查屏幕层级）、`take_screenshot`（截图）、`run`（执行流程）、`open_maestro_viewer`（实时镜像）等，方便代理自动化操作。
- 🖥️ **Maestro Viewer 实时观察**：显示设备屏幕和 Maestro 命令流，人类可在 IDE 内跟踪代理操作全过程。
- 🚀 **快速上手**：安装 Maestro CLI，只需一条命令添加 MCP 服务器，启动模拟器或连接物理设备，然后以自然语言提问即可。
- 🔄 **同一会话迭代**：代理可在编码和 UI 检查间无缝切换，当 UI 变更或测试失败时，能自动调整并重试，反馈速度快。
- 📸 **截图与 Viewer 提供证据**：截图和 Viewer 面板记录每一步操作，方便分享到 PR 或团队审查。

---

### [错误](https://www.youtube.com/watch?v=3r_OHePTCcI)

**原文标题**: [Error](https://www.youtube.com/watch?v=3r_OHePTCcI)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=3r_OHePTCcI (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [React Native 电台 - RNR 368 - RNR 讲解：Fabric](https://infinite.red/react-native-radio/rnr-368-rnr-explains-fabric)

**原文标题**: [React Native Radio - RNR 368 - RNR Explains: Fabric](https://infinite.red/react-native-radio/rnr-368-rnr-explains-fabric)

本文介绍了 React Native Radio 播客第 368 集的内容，主持人 Robin Heinze 和嘉宾 Tyler Williams 深入浅出地解释了 Fabric——React Native 的现代渲染系统。Fabric 替代了旧的渲染系统 Paper，通过同步通信和 C++ 影子树，提升了性能并支持 React 的并发特性，使开发更高效、灵活。

- 🧵 Fabric 是 React Native 新架构中的渲染系统，取代了旧版 Paper，实现了更高效的 UI 更新。
- 📡 旧架构依赖异步消息传递（如“纸片传信”），新架构通过同步方法调用和 C++ 对象直接交互，解决了延迟和优先级问题。
- 🚀 Fabric 支持 React 18 的并发特性（如 Suspense 和过渡），能暂停、丢弃或重启渲染树，提升应用流畅度。
- 📘 在渲染过程中，React 生成组件树，通过 JSI（JavaScript 接口）传递到 C++ 层，构建“影子树”，再由 Yoga 计算 Flexbox 布局，最终提交到原生平台。
- ⚡ Fabric 由多个子系统组成，核心是同步通信和直接操作原生对象，从而带来性能提升和更可控的渲染流程。
- 🎙️ 该集是“RNR Explains”系列的一部分，旨在用简单易懂的方式解读 React Native 文档中的关键概念。

---

### [Bluesky 上的@tc39.es](https://bsky.app/profile/tc39.es/post/3mrdjr6uq2t2i)

**原文标题**: [@tc39.es on Bluesky](https://bsky.app/profile/tc39.es/post/3mrdjr6uq2t2i)

TC39 第 115 次会议推进了多项 ECMAScript 提案，涵盖从阶段 1 到阶段 3 的不同特性，进一步丰富了 JavaScript 语言的功能与标准一致性。

- ⏳ Await dictionary（阶段三）—— 引入字典式异步等待，简化异步流程控制  
- 🪜 Thenable curtailment（阶段二。七）—— 优化 thenable 对象的处理规则  
- 🐛 Error code property（阶段二）—— 为标准错误对象添加错误码属性  
- ➕ Fused multiply-add（阶段二）—— 新增融合乘加运算，提升浮点计算精度  
- 📅 Intl.DateTimeFormat alignment（阶段一）—— 与其他标准对齐日期时间格式化  
- 🔍 Linear matching（阶段一）—— 实现线性匹配算法，增强字符串匹配能力  
- 🗺️ Map.take（阶段一）—— 提供从 Map 中按条件提取元素的方法  
- 📆 2026-07-23 —— 会议日期与提案状态更新

---

### [衡量软导航 | Web 平台 | Chrome 开发者](https://developer.chrome.com/docs/web-platform/soft-navigations)

**原文标题**: [Measuring soft navigations  |  Web Platform  |  Chrome for Developers](https://developer.chrome.com/docs/web-platform/soft-navigations)

Chrome 团队计划在 Chrome 151 中默认启用“软导航”功能，通过新的性能 API 来测量单页应用（SPA）中的 Core Web Vitals 指标，以更准确地反映用户体验。

- 🧭 软导航定义为：由用户操作发起、导致 URL 可见变化并产生新绘制的页面过渡，用于解决 SPA 中传统“硬导航”无法测量的性能问题。
- 🚀 该功能将从 Chrome 151 起默认启用，开发者可通过 `chrome://flags/#soft-navigation-heuristics` 或命令行提前测试。
- 📊 新增 `soft-navigation` 和 `interaction-contentful-paint` 性能条目，用于标识软导航并测量 LCP、FCP、CLS 和 INP 等指标。
- 🛠️ 使用 `PerformanceObserver` 监听软导航事件，并通过 `navigationId` 和 `interactionId` 将性能数据正确关联到对应 URL。
- 📦 `web-vitals` 库 v6.0.0 已内置软导航支持，简化测量流程，自动处理 URL 映射和计时偏移。
- ⚠️ 注意：软导航的 TTFB 推荐报告为 0；LCP 仅考虑与交互相关的新绘制；CLS 和 INP 需在每次导航时重置并重新测量。
- 🌐 由于目前仅 Chromium 浏览器支持，建议同时保留传统硬导航测量方式以进行跨浏览器对比和历史趋势分析。
- 💬 欢迎通过 GitHub issue 和 Chrome 问题跟踪器提供反馈，帮助优化 API 设计。

---

### [](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata/)

**原文标题**: [npm publish-time malware scanning and dual-use metadata - GitHub Changelog](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata/)

npm 引入发布时恶意软件自动扫描，并新增双用途内容元数据要求，以增强供应链安全。

- 🔍 新包发布后需经自动扫描才能可用，通常延迟约 5 分钟，高峰时可能长达 15 分钟以上
- ⛔ 扫描结果可能阻止有害包，被阻止的发布者可收到通知并有权申诉
- 📝 双用途包须在 package.json 中添加 `contentPolicy` 字段，并在根目录附上 DISCLOSURE 文件说明用途
- 🔐 双用途包必须通过强制 2FA 的方式发布（如可信发布、交互式 2FA 或分阶段发布），且声明须持续保留

---

### [CSS 2026 现状](https://2026.stateofcss.com/en-US)

**原文标题**: [State of CSS 2026](https://2026.stateofcss.com/en-US)

2026 年 CSS 調查結果顯示，CSS 功能大幅進化，但瀏覽器支援滯後仍是主要問題。開發者最青睞 Anchor Positioning 等新特性，但無法廣泛使用。與 AI 趨勢不同，CSS 仍主要依賴手工編碼。

- 🚀 CSS 已具備動畫頁面過渡、Masonry 佈局甚至模擬微處理器等強大功能
- 📌 Anchor Positioning 成為最受歡迎但同時因瀏覽器支援問題最多被迴避的新特性
- ⚠️ 瀏覽器相容性問題嚴重限制了 View Transitions、if() 等新特性的實際應用
- 🤖 AI 生成的 CSS 程式碼比例僅 28%，開發者普遍認為 AI 尚未能勝任 CSS 編寫
- 💎 CSS 作為一門獨特語言，歷經數十年演變仍保持其原創性與活力

---

### [ECMAScript - 介绍使用 import defer 的延迟模块评估 | Nitay Neeman 的网站](https://nitayneeman.com/blog/introducing-import-defer-in-ecmascript/)

**原文标题**: [ECMAScript - Introducing Deferred Module Evaluation with import defer | Nitay Neeman's Website](https://nitayneeman.com/blog/introducing-import-defer-in-ecmascript/)

ECMAScript 的 "import defer" 提案是一种新的模块导入形式，它在模块加载和链接时保持同步，但将顶层代码的评估推迟到首次访问其命名空间属性时，旨在解决执行成本问题且不改变同步 API。

- 🚀 **提案状态**：处于 TC39 stage 3，语法和语义已基本确定。
- ⏱️ **核心机制**：`import defer * as ns from "module"` 会立即加载并链接模块，但顶层代码仅在首次读取 `ns` 的属性时才同步执行。
- 🔄 **解决痛点**：相比动态 `import()`，它避免引入异步 API，同时实现延迟执行而非仅延迟加载。
- ⚡ **顶层 await 限制**：如果被延迟的模块或其依赖使用了顶层 `await`，则这些模块会立即评估，仅同步部分可被延迟。
- 🛡️ **错误处理差异**：延迟命名空间在每次访问时都会重新抛出评估错误，与常规命名空间行为不同，确保一致性。
- 🛠️ **引擎支持**：Deno 和 Bun 默认启用，Chrome 在标志后可用，V8、JavaScriptCore 和 SpiderMonkey 均有进展，Babel 提供转换插件。

---

### [](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

**原文标题**: [
      Your SPA Is Leaking Memory. Soak Test It — Den Odell
    ](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

单页应用 (SPA) 因不重新加载页面而容易发生内存泄漏，传统测试难以检测。本文介绍使用 Playwright 进行浸泡测试的方法：通过重复用户流程、测量 DOM 节点和监听器数量来发现泄漏，并建议伪装时钟和网络以加速测试，从而在问题进入生产前修复。

- 💻 SPA 不重新加载页面，导致内存泄漏持续累积，可能使浏览器标签页崩溃
- 🧪 传统端到端测试每次新建浏览器上下文，无法发现长时间运行后的泄漏
- 🔄 浸泡测试在单个浏览器上下文中重复执行用户流程（如打开/关闭抽屉）数百次
- 📊 通过 Chrome DevTools Protocol 获取堆大小、DOM 节点数和监听器计数
- 🔥 测试前需要 5 次预热循环，并执行两次垃圾回收以确保计数稳定
- 📈 比较基线（预热后）与结束时的节点数和监听器数，检查是否增长
- ⏱️ 伪装时钟（`page.clock`）和网络（`page.route`）可压缩时间，模拟数小时真实使用
- 🎯 节点数允许浮动上限（如 100 个），监听器数严格比较，用于检测不同类型泄漏
- 🔧 若测试失败，使用 Chrome 堆快照和"Detached"过滤器定位泄漏来源
- 📘 作者提倡"Fast by Default"理念，主张在问题出现前编写测试，由全团队负责性能

---

### [发布 v1.62.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.62.0)

**原文标题**: [Release v1.62.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.62.0)

Playwright v1.62.0 发布，引入了组件测试新模型、AbortSignal 取消操作、WebP 截图支持、自定义测试过滤、隔离重试机制以及多项新 API 和命令行工具更新。

- 🧱 组件测试采用“故事和画廊”新模型，通过 `mount` 挂载故事并返回作用域定位器
- 🛑 大多数操作和 Web 优先断言支持 `AbortSignal` 参数，可取消长时间运行的操作
- 🖼️ `toHaveScreenshot` 和 `screenshot()` 支持 WebP 格式截图，可控制有损/无损压缩
- 🧩 新增 `reporter.preprocess()` 钩子，允许报告器在运行前标记测试为跳过、排除等
- 🔁 新增 `retryStrategy: 'isolated'` 配置，隔离重试失败测试以减少与其他测试的干扰
- 🔑 新选项 `credentials` 可将 WebAuthn 凭据包含在存储状态中并持久化
- 📜 操作新增 `scroll` 选项（`"auto"` 或 `"none"`），可关闭自动滚动到视图
- ⏱️ `apiResponse.timing()` 返回 API 响应的资源时序信息
- 🔍 `locator.waitForFunction()` 等待元素上的函数返回真值
- 💻 支持 `page.evaluate()` 等函数参数，以及 `addInitScript()` 接受函数
- 🛠️ 捆绑 Playwright MCP 服务器和 CLI，可通过 `npx playwright mcp` 和 `npx playwright cli` 运行
- 📁 HTML 报告新增 `mergeFiles` 配置选项，可合并文件分组
- ⚠️ Debian 11 不再受支持
- 🌐 浏览器版本：Chromium 151.0.7922.34、Firefox 153.0、WebKit 26.5，并测试了 Google Chrome 151 和 Edge 151

---

### [](https://webpack.js.org/blog/2026-07-24-webpack-5-109/)

**原文标题**: [Webpack 5.109 | webpack](https://webpack.js.org/blog/2026-07-24-webpack-5-109/)

Webpack 5.109 是一次重大更新，主要亮点包括将内置的 CSS、HTML、TypeScript 和异步 WebAssembly 支持默认设为 "auto"（无冲突时零配置启用），HTML 原生支持大幅增强以接近 html-webpack-plugin，新增资源提示系统、Vite 兼容模块 API、CommonJS 作用域提升、内置进度条，以及大量性能优化和错误修复。

- 🚀 内置支持默认 "auto": 除非已有 loader 匹配，否则自动启用 CSS、HTML、TypeScript 和 Wasm，实现零配置使用。
- 🧩 HTML 支持接近 html-webpack-plugin: 支持 title/meta/base 头部生成、标签注入控制、内联块、favicon/Web App Manifest、Content-Security-Policy 和 Subresource Integrity，并提供插件钩子。
- 🔗 资源提示 (Resource Hints): 原生支持 preload/prefetch/modulepreload/preconnect，ESM 输出默认启用 modulepreload，并提供 URL 级提示和 SSR 清单。
- 🧩 Vite 兼容模块 API: 支持 import.meta.glob、import.meta.env 默认常量、import.meta.resolve，以及 ?raw/?url/?inline 等资产查询后缀。
- ⚡ CommonJS 作用域提升：将模块连接（scope hoisting）扩展到可静态分析的 CommonJS 模块，减少大型依赖树的捆绑开销。
- 📊 内置构建进度条：通过 infrastructureLogging.progress 提供交互式进度条，替代第三方插件。
- 🎨 CSS 改进：原生支持 @custom-media 和 @custom-selector，CSS Modules 范围化 view-transition 相关属性。
- 🔧 其他：支持 zstd 压缩缓存、AMD 异步 externals 类型、strictModeViolations 检查、更快的解析器和更低的峰值内存。
- 🛠️ webpack-dev-server 6: 原生 ES 模块、支持作为 webpack 插件、Express 5 等更新，需要 Node.js >= 22.15。
- 🔧 错误修复与性能：大量 bug 修复，JavaScript/CSS/HTML 解析速度更快，内存更少，未来将迁移到自定义结构数组 AST。

---

### [](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/153)

**原文标题**: [Firefox 153 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/153)

Firefox 153 为开发者带来了多项更新，涵盖开发者工具、HTML/CSS/JavaScript 解析、API 扩展、WebDriver 兼容性以及扩展权限管理，并新增了多个实验性特性。

- 🔧 辅助功能检查器现在显示标题元素的标题级别，而非仅标识为标题
- 📄 `<select>` 元素解析规则更新，允许嵌套元素进入 DOM，为未来可定制下拉菜单铺路
- 🎨 `::-webkit-scrollbar` 选择器在 `@supports` 中返回 `true`，修复嵌套滚动条堆叠问题
- 📊 支持 `Intl.Locale` 所有 `get*()` 实例方法（如 `getCalendars()`、`getTimeZones()`）
- ⚙️ 新增 `Error.stackTraceLimit` 静态属性，可限制堆栈帧数以提升性能
- 🔤 支持 `with { type: "text" }` 导入文本模块，忽略响应媒体类型
- 🧩 支持 `import source` 语法（源阶段导入提案），仅语法支持，WebAssembly 源尚未实现
- 📦 新增 `IDBObjectStore.getAllRecords()` 和 `IDBIndex.getAllRecords()` 方法
- 🖥️ Picture-in-Picture API 现已在桌面平台可用
- 🔄 Popover API 中 `hint` 与 `auto` 弹出行为更一致
- 📞 `RTCDtlsTransport.getRemoteCertificates()` 可获取 DTLS 远程证书
- 🎥 `MediaCapabilities.decodingInfo()` 和 `encodingInfo()` 支持 `"webrtc"` 配置类型，移除 `transmission` 别名
- 📊 WebRTC 传输统计信息现可通过 `RTCTransportStats` 报告
- 🧬 JavaScript Promise 集成 (JS-PI) 已启用，WebAssembly 可与异步 JS API 互操作
- 🖱️ 窗口操作命令支持独立调整 x、y、width、height
- 🌐 新增 `publicSuffix` API，获取 eTLD+1 和公共后缀
- 📄 扩展需明确申请 `file://` URL 权限，默认关闭
- 📜 支持 `userScripts.execute()` 按需注入用户脚本
- 🆔 多个 WebExtension API 新增 `documentId` 属性
- 🎨 主题支持 `additional_backgrounds` 接受 CSS 渐变，新增 `additional_backgrounds_size` 属性
- 🔒 容器身份新增 `getSupportedColors()`、`getSupportedIcons()` 方法
- 🧪 实验特性：JPEG XL（Nightly 默认开启）、`sibling-count()`/`sibling-index()` CSS 函数、`link-parameters` CSS 属性和 `param()` 函数、`farthest-corner`/`closest-corner` 关键词（Nightly）

---

