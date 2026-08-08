### [](https://tanstack.com/blog/announcing-tanstack-table-v9)

**原文标题**: [Announcing TanStack Table V9 | TanStack Blog](https://tanstack.com/blog/announcing-tanstack-table-v9)

TanStack Table V9 是自 V8 以来时隔四年多的重大版本，重写了内部架构，支持十种框架适配器，性能大幅提升，并引入基于 TanStack Store 的树摇式插件系统与细粒度状态管理，同时带来多项新功能与更好的扩展性。

- 🏗️ 架构重写：推出基于 TanStack Store 的系统，支持十种框架适配器（React、Preact、Vue、Solid、Svelte、Angular、Lit、Alpine、Ember、Octane），各适配器均原生对接信号、refs、runes 等响应式模型。
- ⚡ 性能大幅提升：共享原型减少内存占用，保留堆最高降低 86%（百万行场景从约 2.71 GB 降至约 380 MB）；核心行模型处理均提速 1.5–3.9 倍。
- 🗃️ 状态管理重构：表格状态由 TanStack Store 驱动，基于 alien-signals 实现细粒度响应式，组件可只订阅所用数据切片，并支持外部可写 atom 共享状态。
- 🛡️ 类型安全增强：新增列、过滤、排序、聚合等类型辅助，支持按表声明元数据类型，类型系统能感知已注册功能并提前校验前置条件。
- 🌳 树摇与模块化：功能通过 tableFeatures() 显式注册，仅引入所需功能与行模型，未使用的代码可被摇掉，减少应用打包体积。
- 🧩 可组合性提升：提供 tableOptions() 和 createTableHook()，可复用配置、功能与组件约定，方便构建统一的产品级表格系统。
- ✨ 新功能与升级：新增单元格选择（矩形范围、拖拽、Shift 扩展、多选区）、单元格跨行跨列合并、列多聚合、行选择 Shift 范围等，并优化列宽调整。
- 🚀 未来展望：V9 为后续版本打下基础，V10 不会等太久，计划支持 Solid 2、完整透视表、高级过滤表达式等，并以可组合功能方式推出。
- 📖 迁移支持：各框架提供专属迁移指南（React、Preact、Vue、Solid、Svelte、Angular、Lit 等），无专用指南的适配器可参考 V9 快速入门。

---

### [](https://tanstack.com/blog/tanstack-table-v9-reactivity)

**原文标题**: [Inside TanStack Table V9 Reactivity | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-reactivity)

概述：本文深入探讨了 TanStack Table V9 的响应式重构历程，从 V8 的适配器同步问题、Angular 信号代理尝试，到最终将响应式边界下沉到核心层，通过共享原子契约实现多框架适配与精细渲染。

- 🔄 TanStack Table V9 重构的核心动力：解决数据网格中局部状态更新（如行选择）导致整个表格不必要重渲染的性能问题。
- 🧩 从 V8 到 V9：V8 依赖适配器在框架与 Table 实例之间同步 `setOptions`/`setState`，框架无法感知方法内部读取的依赖。
- 📡 Angular 信号适配器探索：通过 Proxy 包装 `get*` 方法并创建 computed，但响应式边界仍局限于表格实例，`flexRender` 需要宽泛重检。
- ⚛️ React Compiler 暴露相似问题：稳定 `row` 引用下方法内部状态变化无法被编译器察觉，促使响应式必须下沉到 Table API 之下。
- 🧠 核心响应式设计：每个功能状态切片（分页、行选择、列宽等）使用独立原子，`table.store` 派生聚合状态视图。
- ⚙️ 选项响应式：新增 `optionsStore`，使 `data`、`enableRowSelection` 等选项成为实时输入，而非构造时配置。
- 🔗 双响应图同步的痛点：Store 与框架信号桥接导致调度遗漏或重复渲染，最终采用「每个适配器一个响应式图」方案。
- 📐 最终契约：核心依赖共享的 `Atom`/`ReadonlyAtom` 接口（`TableReactivityBindings`），适配器可用原生信号、computed 或 `@tanstack/store` 实现。
- 🌱 适配器多样性：Angular、Solid、Vue 使用原生响应式原语；Ember 通过 `@tracked`/`@cached` 适配；React 使用 Store 选择器与 `Subscribe` 实现精细渲染。
- ⚡ 信号原生适配器自动追踪：在 computed/effect 中调用 Table 方法即可自动记录依赖，无需显式订阅。
- 🎯 React 精细渲染方案：`useTable` 支持选择器，`Subscribe` 组件可为独立单元格（如行选择框）建立边界，避免整个表格重渲染。
- 🧩 开发体验不变：应用代码仍传递普通值、调用相同 Table 方法，复杂度由库内部消化。

---

### [](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

**原文标题**: [How an Underrated Refactor Saved 90% Memory Usage | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

TanStack Table V9 通过共享原型重构，将大表格处理的内存占用降低最多约 90%，同时将可处理行数上限提升了约 10 倍；文章详细介绍了基准结果、实现方式、与类的对比，以及带来的少量破坏性变更。

- 📊 基准测试显示，处理 100 万行 × 8 列时，V9 比 V8 少用约 2.4GB 内存，内存节省最高达 90.5%。
- 🚀 该改进使 TanStack Table 在浏览器中可处理的最大行数从约 100–150 万提升至 1000–1600 万。
- 🔬 内存测量方法基于 Playwright 与 Chrome DevTools Protocol，强制垃圾回收后记录保留的 JS 堆大小。
- 🧠 V8 中每个 row、cell 等对象都会复制自己的方法并携带闭包，导致大量重复函数和巨大内存开销。
- ⚙️ V9 改为创建共享的原型对象，再通过 Object.create() 让每个对象继承方法，从而消除重复方法和闭包作用域。
- ❓ 不使用 JavaScript 类，是因为 Table V9 的 API 由多种可选特性动态组合，手动原型方式比类继承更灵活、更适应插件系统。
- ⚠️ 主要的破坏性变更：像 `const { getValue } = row` 这样的解构方法不再可用，因为方法依赖 `this` 上下文；方法也不再作为自有属性存在，浅拷贝（如 `{ ...row }`）会丢失方法。
- ✅ 整体而言，这是一个几乎无副作用的优化，未来甚至释放了更多内存预算，让 V9 可以继续为速度而牺牲少量内存。

---

### [AI代码审查 | CodeRabbit | 免费试用](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=cooperpress&utm_content=ad-cooperpress-001&ref=cooperpress&dub_id=WCUuMKRxx6qIzQId)

**原文标题**: [AI Code Reviews | CodeRabbit | Try for Free.](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=cooperpress&utm_content=ad-cooperpress-001&ref=cooperpress&dub_id=WCUuMKRxx6qIzQId)

overview summary
- 📧 新增 `Invitation` 数据模型，包含邮箱、角色、令牌、状态等字段，用于管理队友邀请流程。
- 🔑 引入 `MemberRole` 枚举（ADMIN、MEMBER、VIEWER），定义团队成员的不同权限级别。
- 📊 新增 `InvitationStatus` 枚举（PENDING、ACCEPTED、REVOKED），跟踪邀请的当前状态。
- 🗄️ 创建邀请数据表的迁移文件，为后续 API 和 UI 开发奠定数据库基础。
- 🔗 邀请记录关联组织（Organization），并通过 `orgId` 与 `status` 建立索引以优化查询性能。
- ⏳ 包含 `expiresAt` 过期时间字段，确保邀请链接具有时效性。
- 👤 记录 `invitedBy` 字段，标明发起邀请的用户，增强可追溯性。

---

### [](https://nextjs.org/blog/next-16-3)

**原文标题**: [Next.js 16.3 | Next.js](https://nextjs.org/blog/next-16-3)

Next.js 16.3 正式发布，带来多项对现有应用零代码改进的性能优化，并推出“Instant Navigations”可选功能套件，以及 Rust 版 React 编译器、离线支持等实验特性。

- 🚀 开发服务器内存占用最高降低 90%，长时开发会话更流畅。
- ⚡ 构建速度大幅提升，重复构建可复用磁盘缓存，部分项目 CI 最快加速 5.5 倍。
- 🧠 支持 TypeScript 7 进行类型检查，`next build` 阶段类型检查速度提升 10 倍。
- 📈 服务端渲染改用原生 Node.js 流，同等负载下请求处理能力提升约 22%。
- 📚 AI 编码代理可自动读取与项目版本匹配的文档，无需额外设置。
- 🔗 预取请求按需合并，减少链接触发的请求数量。
- 💾 不可变静态资源可在部署间复用，避免版本偏差问题。
- 🛡️ 新增 `catchError` 自定义错误边界，支持重试 Server Components，不与 `notFound`/`redirect` 冲突。
- 📂 内置 Vite 兼容的 `import.meta.glob` 导入，方便批量加载本地文件模块。
- 🌍 新增 Root Params，任意 Server Component 可直接访问 `[lang]` 等根级动态参数，告别 prop drilling。
- ⚡ 推出 “Instant Navigations” 功能套件，包含 Instant Insights、Partial Prefetching、改进的 ISR、Navigation Inspector 和 Playwright 测试助手。
- 🔍 Instant Insights 自动发现并提示慢导航，帮助开发者定位加载瓶颈。
- 🧩 Partial Prefetching 允许按需提取加载壳与页面内容，使导航响应接近 SPA。
- ♻️ 改进的 ISR 可为未预渲染页面先提供即时加载壳，并在后台升级为完整预渲染内容。
- 🛠️ Navigation Inspector 可视化检查导航加载壳，Playwright 的 `instant()` 助手可防止回归。
- 🧪 实验性 Rust 版 React Compiler 直接在 Turbopack 运行，冷启动提速约 34%，热启动提速约 46%。
- 📡 实验性 `useOffline` 功能在断网时保持请求挂起，恢复连接后自动重试，并可通过新 Hook 提示用户。
- ⬆️ 可通过 `npm install next@latest` 升级到 Next.js 16.3，体验全部改进与新特性。

---

### [](https://nextjs.org/blog/next-16-3-instant-navigations)

**原文标题**: [Next.js 16.3: Instant Navigations | Next.js](https://nextjs.org/blog/next-16-3-instant-navigations)

Next.js 16.3 发布，重点推出“Instant Navigations”功能，旨在让服务端驱动的应用也能拥有类似 SPA 的即时响应体验，同时保留服务端渲染的优势。

- 🚀 新版本引入 Instant Navigations，解决服务端应用导航延迟、点击后需等待网络往返的问题。
- ⚙️ 需先启用 `cacheComponents: true` 标志，该功能未来将成为默认行为。
- 🔀 路由在服务端 await 数据时，可选择三种模式：`Stream`（用 Suspense 显示加载状态）、`Cache`（用 'use cache' 复用缓存）、`Block`（用 `export const instant = false` 保持服务端阻塞）。
- 🛠️ 新增 Instant Insights 面板，在开发环境中将慢导航视为错误，并提供 `instant()` Playwright 测试助手防止回归。
- 📦 重构预取机制：不再为每个链接发送预取请求，改为按路由预取可复用的“shell”，并在客户端缓存；启用需 `partialPrefetching: true`。
- 🔍 新增 Navigation Inspector 开发工具，可暂停导航查看每个路由预取的 shell 内容。
- ⚡ 可通过 `<Link prefetch={true}>` 结合 `'use cache'` 实现更深度的按链接预取，但默认仍只渲染同步可用内容。
- 📉 该团队已在 v0 产品中应用这些工具，显著缩短了导航时间，并计划继续优化。
- 🎵 提供了开源示例项目 Next Beats（Next.js 16.3 预览版）展示即时导航效果。
- ✅ 总结要点：Stream/Cache 使导航即时，Block 可退出强制即时；自动生成可复用 shell 并只预取一次；支持测试助手和可视化检查；相关功能由两个配置标志控制。
- 📥 可通过 `npm install next@preview` 试用，已知问题包括 Safari 中 Instant Insights 工具异常等，建议开发时使用 Chrome 或 Firefox。

---

### [Next.js 16.3：AI 改进 | Next.js](https://nextjs.org/blog/next-16-3-ai-improvements)

**原文标题**: [Next.js 16.3: AI Improvements | Next.js](https://nextjs.org/blog/next-16-3-ai-improvements)

Next.js 16.3 正式发布，本次更新聚焦 AI 辅助开发体验，为 AI 编程代理提供版本匹配的文档、官方 Skills、浏览器驱动与 React 内省能力、可操作的错误提示，以及更精简的 MCP 服务器，使代理驱动的开发流程更加顺畅高效。

- 🚀 Next.js 16.3 发布，重点面向 AI 代理驱动开发，安装方式为 `npm install next@latest`
- 📚 通过 AGENTS.md 自动捆绑文档：`next dev` 自动写入并更新指针，确保代理读取与版本匹配的文档而非训练数据；旧版本可通过 `agents-md` codemod 手动迁移
- 🛠️ 新增多个第一方 Skills：`next-dev-loop`（驱动完整开发反馈循环）、`next-cache-components-adoption`（分步采用 Cache Components）、`next-cache-components-optimizer`（优化即时渲染），稳定版还新增 `next-partial-prefetching-adoption`
- 🌐 agent-browser CLI 合并了原先的 next-browser，v0.27 起支持 React DevTools 内省，可列出组件树、检查组件、分析重渲染及 Suspense 状态
- ⚡ 可操作错误提示（Actionable errors）：Instant Insights 在 overlay 和终端中显示带标签的修复菜单（Stream / Cache / Block），并提供 Copy prompt 按钮生成可直接粘贴给代理的修复提示
- 📖 错误文档专为代理撰写：每个错误有独立页面，包含规范模式（Patterns）、权衡（Trade-offs）和易错点（Gotchas），帮助代理正确应用修复
- 🖥️ 结构化控制台输出：`next build` 和 CI 日志中同样输出带标签的修复选项及对应文档链接，即使没有 dev overlay 也能获得相同信息
- 🔧 MCP 服务器更精简聚焦：移除知识库工具，新增 `get_compilation_issues`（全项目编译问题）和 `compile_route`（单路由编译）两个快速诊断工具
- 📝 文档支持 Markdown 格式：在任何 docs URL 后追加 `.md` 即可获取纯文本版本，并提供 `/docs/llms.txt` 和 `/docs/llms-full.txt` 遵循 llms.txt 约定，方便代理读取

---

### [](https://vercel.com/blog/vercel-supports-next-js-16-3)

**原文标题**: [Next.js 16.3 support on Vercel - Vercel](https://vercel.com/blog/vercel-supports-next-js-16-3)

overview summary  
Next.js 16.3 正式发布，Vercel 全面支持该版本，带来更精简的预取、不可变静态资源、更快的大规模路由性能以及更强的可观测性。升级后的应用平均减少 45% 预取请求，静态内容 CDN 请求减少 17%、字节传输减少 24%，大型站点 p99 路由解析速度提升约 2 倍。

- 🚀 预取请求大幅减少：从 16.2 升级到 16.3 的应用平均减少 45% 预取请求，部分应用减少超过 70%。
- 📦 不可变静态资产：Next.js 16.3 默认启用不可变静态资产，CDN 请求减少 17%，静态内容传输字节减少 24%，部署速度平均提升 30%，并支持跨部署复用。
- ⚡ 路由性能提升：通过优化路由元数据缓存，采用 JSONL 分片格式，p99 路由解析速度提升约 2 倍，缓存未命中减少约 10 倍。
- 🔍 可观测性增强：可在 Vercel Observability 和 Runtime Logs 中查询预取请求；ISR 观测页面新增缓存原因与写入利用率；新增 PPR 可观测页面，区分静态、动态及混合内容请求。
- 📈 平台级收益：路由元数据优化对所有通过 Build Output API 部署的框架自动生效，无需额外操作。
- 🆙 升级方式：立即运行 `pnpm add next@16.3.0` 升级，并阅读 Next.js 16.3 公告获取完整发布说明。

---

### [](https://remix.run/blog/react-router-v8)

**原文标题**: [React Router v8 | Remix](https://remix.run/blog/react-router-v8)

React Router v8 正式发布！这次升级以“无聊”为最大特色，延续 v7 的平稳演进，大幅减少破坏性变更，引入年度主版本发布节奏。文章回顾了 v7 以来的 40+ 版本更新，列出 v8 的主要新特性、最低依赖要求、必要的破坏性改动、简单的升级步骤，并展望未来对 Server Components 的支持以及 Remix 项目的独立发展方向。

- 🎉 宣布 React Router v8 发布，主打“最无聊”升级，并计划改为每年一次主版本发布，让升级更可预测。
- 🏗️ 回顾 v7 的 Framework Mode：提供类型安全路由 API、智能代码分割、SPA/SSR/SSG 渲染策略、数据加载与变更等能力。
- 🧩 继续支持三种使用模式：纯客户端路由、自定义数据模式、全栈框架模式，保持灵活性。
- ✨ 列举 v8 新特性：中间件、Split Route Modules、类型安全 `href`、`fetcher.reset`、Vite Environment API、Link masking、可配置懒路由发现、子资源完整性、性能改进等。
- 🖥️ 新增 `useRoute` / `useRouterState` / `useTransitions` 等 API，并加强 SPA 模式与预渲染能力。
- 🧪 提供不稳定的 Server Components 和 Server Actions 支持，仍在迭代中，计划在 minor 版本稳定。
- 🔧 最低依赖基线提升：Node 22.22.0+、React 19.2.7+、Vite 7+，并改为 ESM-only，tsconfig 目标更新为 ES2022。
- 📅 Node 支持策略调整：官方支持所有 Active LTS 版本，以及 Maintenance LTS 的最新 minor 分支，安全补丁会触发最低版本提升。
- 🚦 多个 v7 future flag 转为默认行为，包括 middleware、pass-through requests、Vite Environment API、Split Route Modules 等。
- 🧹 弃用项清理：移除 `react-router-dom`、meta API 的 `data` 参数改用 `loaderData`、移除 Cloudflare dev proxy 等。
- 🔄 升级只需三步：更新 peer dependencies、启用/确认 future flags、删除弃用 API，然后执行 `pnpm i react-router@latest`。
- ⏳ React Router v6 和 Remix v2 正式进入 EOL，不再接收安全更新；v7 仍会继续获得安全维护。
- 🌍 项目采用开放治理模式，鼓励社区提交提案和修复，继续坚持“少即是多、聚焦路由与数据、简单迁移路径、最低共同模式”的设计目标。
- 🧭 Remix 将走向独立方向，成为全栈零依赖 JavaScript 框架；React Router 则继续作为成熟的 React meta-framework，两者并行发展。
- 💡 选择建议：追求稳定就用 React Router；希望尝试前沿技术可关注 Remix 3 beta。

---

### [](https://github.com/remix-run/react-router/discussions/15371)

**原文标题**: [React Router v9 · remix-run/react-router · Discussion #15371 · GitHub](https://github.com/remix-run/react-router/discussions/15371)

React Router v9 的 GitHub 提案讨论，概述了下一个主版本的计划方向、设计原则、未来标志、新 API、弃用项目以及社区反馈，预计于 2027 年中发布。

- 📅 v9 预计于 2027 年中发布，时间点在 Node 22 结束支持（约 2027 年 5 月）之后，v8 已于 2026 年 6 月发布。
- 🎯 设计原则强调“少即是多”，减少 API 表面但保留能力；提供简单迁移路径（用未来标志和弃用警告）；保持约一年一次的主版本节奏。
- 🚩 未来标志 `unstable_enableNodeReadableStream` 正在等待社区和指导委员会反馈，可能用于运行时特定的默认服务端入口。
- 🆕 新 API 方面，计划稳定 `useRoute` 和 `useRouterState`，以整合路由数据访问和路由器状态访问，未来可能弃用相关旧 hooks。
- 🗑️ 弃用计划包括：将 Node 最低版本提升至 24.x；移除 `react-router reveal --no-typescript` 标志（TypeScript 为默认）；若 React 的 `ViewTransition` 组件稳定，则弃用现有 View Transition APIs。
- 🤔 正在讨论是否提升最低 React 和 Vite 版本，以及是否调整声明式模式（Declarative mode）的存废（`useRouterState` 可能需兼容该模式）。
- 💬 社区提问涉及 SPA 下的预取模式（类似 TanStack Router）以及是否添加第一方客户端 loader 数据缓存，维护者回应称预取模式有开放 RFC 可接受贡献，缓存问题暂无明确计划。
- ✅ 目前“好点子”列表为空，说明未来标志中无已确定的新增不稳定功能，主要聚焦于清理和稳定现有能力。

---

### [问卷 - shadcn/ui](https://ui.shadcn.com/docs/components/base/questionnaire)

**原文标题**: [Questionnaire - shadcn/ui](https://ui.shadcn.com/docs/components/base/questionnaire)

该文档介绍 shadcn/ui 的 Questionnaire 组件，这是一个多步骤问卷，支持单选、多选、自由文本和可跳过问题。文档涵盖安装、用法、组合结构、服务端渲染、自定义验证、受控模式、无障碍支持等，并展示如何与 Card、Dialog 等组件组合使用。

- 📥 安装：通过 `pnpm dlx shadcn@latest add questionnaire` 命令安装。
- 🧩 组合结构：Questionnaire 由 Progress、Item、Title、Description、Choices、Choice、Input、Error 和 Actions（Previous/Skip/Next/Submit）构成。
- ⚙️ 核心能力：支持单选、多选（multiple）、自由文本输入和显式跳过（Skip）问题。
- 🖥️ 服务端渲染：传入 items 即可服务端渲染活动项、进度、操作和答案快捷键。
- ⌨️ 快捷键：通过 shortcuts 为每个答案分配字母或数字键。
- 🔄 受控模式：可由宿主状态控制当前活动项，便于实现返回无效步骤等场景。
- 💾 恢复草稿：可恢复已保存的活动项和默认答案，并支持重置更改。
- 🚦 条件项：可根据用户先前答案禁用不适用的问题项。
- 🧭 导航状态：读取项目状态可自定义禁用导航和操作样式。
- 📊 自定义进度：使用 Progress 渲染状态构建自定义进度指示器。
- 🎨 自定义验证：可与 Zod 等外部 schema 结合，实现受控导航和错误展示。
- 📦 组合扩展：可与 Card、Dialog 等组合，保持宿主拥有关闭、取消等逻辑。
- ♿ 无障碍：采用 fieldset/legend 语义，原生 radio/checkbox 行为，暴露 aria-invalid 和 progressbar，并支持键盘操作。
- 🧪 无样式版本：行为来自 @shadcn/react 包，可自定义标记与样式；API 文档包含完整 props、data attributes 和 render states。

---

### [](https://expo.dev/blog/fable-5-vs-gpt-5-6-sol-expo-apps)

**原文标题**: [Fable 5 vs GPT-5.6 Sol: I spent $2,000 and 2 billion tokens to find out who wins â Expo blog](https://expo.dev/blog/fable-5-vs-gpt-5-6-sol-expo-apps)

作者花了 2,000 美元和 20 亿 tokens，让 Fable 5、GPT-5.6 Sol 与 GPT-5.5 三款 AI 模型在完全相同的规则下，一次性开发三款 Expo 应用，并全程不碰代码进行对比实测。结果显示 Fable 5 在代码质量、速度与效率上几乎全面胜出，而 GPT-5.6 Sol 则在长时间自主攻坚与自动化任务上展现出独特优势。

- 🧪 实验设计: 三款 AI 模型（Fable 5、GPT-5.6 Sol、GPT-5.5）以相同提示、模板与规则，分别从头构建三款 Expo 应用，作者全程零代码介入。
- ⚖️ 统一规则: 每个模型都采用“高努力”模式，并被要求每完成一个功能就必须在 iOS 模拟器上自主验证通过后才能继续。
- 📱 App 1（AI 卡路里追踪器）: Fable 5 在 UI 一致性上最佳，GPT-5.6 在首页细节（预算用量、餐次统计）上最贴心，GPT-5.5 则残留了模板自带的“探索”页面。
- 📊 App 1 指标: Fable 5 成本 $276.95 但仅花 3h45m、代码健康度 88 分；GPT 两模型耗时超 5 小时，健康度均只有 79 分。
- 💬 App 2（ChatGPT 克隆）: GPT-5.5 完全无法回复消息，直接失败；Fable 5 和 GPT-5.6 均能正常对话且支持流式输出。
- 📊 App 2 指标: Fable 5 再次以 2 小时、2,000 行代码、85 分健康度碾压对手；GPT 两模型均耗时 3.5 小时以上、写了超 3,500 行代码。
- 😴 App 3（SwiftUI 睡眠追踪器重写）: 这是最惊人的部分——Fable 5 几乎完美复刻了原版 SwiftUI 应用，包括图表、色彩、实时活动，甚至修复了原版 Swift app 里的一个 bug。
- 📊 App 3 指标: Fable 5 仅 3h25m 完成、代码健康度 88 分，但成本高达 $558；GPT-5.6 耗时 13h34m 才完成，但仍拿下 86 分，是最接近的一次。
- 🔥 Token 消耗主因: 绝大多数 tokens 被模拟器验证环节吃掉——模型每实现一个功能就截图、点击、回传元数据，17 个任务 × 每模型 × 每轮修复循环，积少成多。
- 🏆 结论: Fable 5 像“资深同事”，更聪明、代码更少、质量更高，适合完整 PR 和产品级开发；GPT-5.6 是“耐力型磨工”，适合定义清晰的自动化任务。
- 🚀 实用建议: 创业者与产品验证首选 Fable 5；计划自动化流程或写简单脚本用 GPT-5.6；两者可按场景搭配使用。
- 🔗 相关资源: 作者开源了全部代码、提示词、技能与指标仪表盘，并推荐了 Expo API Routes、OpenAI Agents SDK 及 Argent 模拟器验证工具。

---

### [](https://www.jxd.dev/blog/tsrx-tanstack-start)

**原文标题**: [TSRX in TanStack Start: what we like, and three bugs we filed · JXD](https://www.jxd.dev/blog/tsrx-tanstack-start)

overview summary  
- 🧩 TanStack Start 是作者團隊新 TypeScript 專案的預設框架，TSRX 作為 JSX 的後繼者，能編譯成相同的 React 元件樹，但提供更接近直覺的陳述式語法。  
- 📦 TSRX 將結構、樣式與控制流集中於單一檔案：支援 `@if`、`@for`、`@switch` 等真實控制流，內建 `<style>` 區塊，減少查找表、CSS module 與多檔案切換。  
- 🤖 這對人類與 AI 模型都更友善——相關資訊在同一處，用 Claude Code 產生 TSRX 元件時減少幻覺與錯誤 prop drilling。  
- 🔧 整合 TanStack Start 只要四步：安裝 `@tsrx/react` 與 Vite 外掛、安裝 TypeScript 外掛、設定 `tsconfig.json`、安裝 VS Code 擴充功能。  
- 🐛 壓力測試發現三個 SSR 接縫問題：開發模式 SSR CSS 會遺失（用 build/preview 驗證）、`.tsrx` 不能當路由檔（用 `.tsx` 路由匯入元件）、`@try/@catch` 在 SSR 無效（錯誤邊界僅客戶端可用）。  
- ✅ 總體而言客戶端 TSRX 是明確勝利，問題都在 TanStack Start 的 SSR 握手細節，且都有簡單替代方案；團隊選擇公開回報並修復，而非默默繞過。

---

### [你不应该对所有事情都使用Relay • Andrei Calazans](https://andrei-calazans.com/posts/2026-07-30-dont-use-relay-for-everything/)

**原文标题**: [You Should Not Use Relay for Everything • Andrei Calazans](https://andrei-calazans.com/posts/2026-07-30-dont-use-relay-for-everything/)

Relay 虽然强大，但并非所有数据都适合放入其规范化存储中；部分数据无法从中获益，却仍需承担全部成本，应理性区分使用场景。

- 🔄 **Relay 的核心价值**：通过全局 ID 归一化缓存，重复实体只存一份，跨查询自动同步更新，省去手写 reducer 和数据同步逻辑。
- 💰 **双重成本之一——归一化 CPU**：每次响应需规范化处理，且每次读取都要做随存储规模增长的引用相等性维护，存储越大，读取越慢。
- 💾 **双重成本之二——持久化 CPU**：离线缓存每次持久化都要对整张记录表执行 `JSON.stringify` 和深拷贝；实测存储可膨胀至 18 MB，导致读写全面变慢。
- 📦 **不获益的数据类型**：客户端配置、实验开关、易变行情序列、服务端驱动 UI、内联资源等，均无跨查询引用或原地更新需求，却因合成 ID 占用 16–29% 存储空间。
- 🧩 **核心规则**：真正的实体（用户、资产、投资组合）应留在 Relay；只读、无重叠的数据应移至普通 store（如 Zustand），按需取用，避免无谓开销。
- ✅ **结论**：根据数据特性选择缓存方案，只在 Relay 能体现价值的地方使用，否则只会徒增成本。

---

### [构建你的富文本编辑器 - Plate](https://platejs.org/)

**原文标题**: [Build your rich-text editor - Plate](https://platejs.org/)

该文本介绍了基于 Plate 的富文本编辑器构建方式，强调插件、组件与 AI 功能的集成，并提供了快速开始与预览操作指引。

- 🧩 核心概念：以“插件输入规则”为入口，支持构建自定义富文本编辑器。
- 🏗️ 架构组成：编辑器由框架、插件和组件三部分协同构成。
- ⚡ 快速启动：通过 `npx shadcn@latest add @plate/editor-ai` 命令安装 AI 编辑器模块。
- 👁️ 预览与调试：提供“在新标签页打开”和“刷新预览”功能，便于实时查看编辑效果。
- 🤖 AI 集成：示例展示了一个具备 AI 能力的编辑器，可将智能功能嵌入文本编辑流程。

---

### [](https://github.com/GoogleChromeLabs/use-webmcp-tool)

**原文标题**: [GitHub - GoogleChromeLabs/use-webmcp-tool · GitHub](https://github.com/GoogleChromeLabs/use-webmcp-tool)

overview summary
use-webmcp-tool 是一个由 Chrome 维护的 React Hook，用于将 WebMCP 工具注册到浏览器，并使其生命周期与 React 组件绑定。该 Hook 封装了底层的 imperative API，提供声明式接口，支持工具在组件挂载时注册、卸载时自动注销，并处理结果规范化、错误处理等。目前实验性，可通过特性检测降级为无操作。

- 🧪 实验性：由 Chrome 维护，随规范更新，API 不存在时自动降级为 no-op。
- 📦 安装：npm install use-webmcp-tool，需要 React 18+，ESM + TypeScript 类型，无运行时依赖。
- 🤖 功能：通过 WebMCP 将页面功能暴露为 AI 代理可发现和调用的工具，替代 DOM 抓取。
- 🔧 底层 API：使用 document.modelContext.registerTool + AbortSignal 实现注册和注销。
- ⚛️ React 封装：useWebMCP 提供声明式接口，组件挂载时注册，卸载时自动注销，与屏幕内容保持同步。
- 📋 参数与返回值：支持 name/description/inputSchema/annotations/execute/enabled 等选项，返回 supported/registered/error。
- 🔄 结果规范化：字符串→文本块，undefined→空，已格式化内容透传，抛错或返回 Error 标记 isError，其他对象 JSON 序列化。
- ✅ 测试覆盖：21 个测试涵盖生命周期、重注册、结果/错误规范化等。

---

### [](https://www.rshono.com/)

**原文标题**: [rshono — Hono + Rspack + React Server Components](https://www.rshono.com/)

rshono 是一个极简的 React Server Components 框架，整合 Hono（服务器）、Rspack（构建）与 RSC（渲染），仅需一个必需文件、九个导出值，无强制目录约定。它强调服务端与客户端组件协同开发、简洁的路由表和直接的数据库访问，并提供快速脚手架、多部署目标及显著的性能优势。

- 📦 极简设计：仅 1 个必需文件、9 个导出值、5 个直接依赖，不包装 HTML 元素，Hono 与 Rspack 保持底层可及。
- 🗂️ 统一路由表：所有页面和端点集中在 `src/routes.ts`，按顺序匹配，无文件系统路由，移动页面只需改一行。
- ⚡ 服务端页面直取数据：页面组件接收 `{ url, params, ctx }`，直接 await 数据库查询，无需 API 层。
- 🧭 单一导航 Hook：`useNavigation()` 返回 URL、params 和 router；链接用 `<a>`、图片用 `<img>`、表单用 `<form action>`。
- 🔧 Actions 即函数：`'use server'` 函数可从客户端以类型安全方式调用，支持 hydration 前表单提交及禁用 JS 场景。
- 🛠️ 完全掌控 Hono 应用：`src/server.ts` 是挂载在页面之前的 Hono 子应用，中间件可包裹页面，支持端点、流、cookie 和端到端客户端类型。
- ⚙️ 可定制 Rspack 配置：提供一次编译钩子，可在编译前修改生成配置，例如接入 Tailwind 等加载器。
- 🚀 三条命令完成开发部署：`rshono dev`（生产 bundle + HMR）、`rshono build`、`rshono start`。
- 🎯 脚手架交互简单：六个问题（位置、部署目标、样式、格式化/规范、安装、git），支持非交互 `--yes` 和自动识别包管理器。
- 📈 性能亮眼：相比 Next.js，初始载荷小 2.7 倍；相比 TanStack Start，冷构建快 7.1 倍；首绘前请求数少 3.7 倍。

---

### [](https://www.morphicons.com/)

**原文标题**: [morphicons — SVG icon morphing library for React, Vue & Svelte](https://www.morphicons.com/)

Morphicons 是一个轻量级图标变形库，可将任意 SVG 图标平滑变形为其他图标，支持多种主流图标集。它以闭式解处理旋转对齐，采用弹簧物理与零依赖设计，体积小、性能高，并提供极简 API 适配主流前端框架。

- 🧩 支持任意 SVG 图标互变，覆盖 Lucide、Tabler、Heroicons 等主流图标集
- ⚙️ 以闭式解（2D Procrustes）求最优旋转，弹簧物理驱动，且零运行时依赖
- 📦 通过 npm 安装，核心 gzipped 仅 6.5KB，无适配器或每库额外配置
- 🔄 极简 API：仅需一个组件，无需包装器、键或 from/to 配对
- ⚛️ 第一等支持 React、Vue、Svelte、React Native、Next.js 及纯 JavaScript
- 🎯 图标以数据形式消费（d 属性或 Lucide IconNode），结构类型化
- 🚀 规划任意变形对耗时 <1ms，屏幕全部图标共享单一 rAF 驱动
- ✨ 弹簧可中断，静止时保持尖角；通过 fitIcon 适配任意网格的 stroke 图标集

---

### [](https://react-aria.adobe.com/releases/v1-20-0)

**原文标题**: [v1.20.0 | React Aria](https://react-aria.adobe.com/releases/v1-20-0)

v1.20.0 版本于 2026 年 7 月 31 日发布，带来多项新组件、功能改进与文档重写，主要亮点包括 PreviewTrigger、TokenField、右键菜单支持、键盘快捷键增强以及表格内交互组件支持。

- 🆕 新增 PreviewTrigger 组件：悬停、聚焦或长按显示弹出内容，支持交互式内容与无障碍键盘操作，包含延迟、安全区域及进出动画。
- ✨ 推出 TokenField（alpha）：支持内联令牌输入、自动补全与自动分词，适用于 AI 提示、标签输入、提及等场景。
- 🖱️ MenuTrigger 新增 trigger="contextMenu"，支持鼠标、键盘与触摸的无障碍上下文菜单。
- ⌨️ useKeyboard 提供更简单的快捷键 API，并支持控制事件传播与默认行为。
- 📋 Table 支持在行内使用 TextField 等交互组件，通过 keyboardNavigationBehavior="tab" 实现。
- 📚 React Aria 与 React Stately 钩子文档全面重写，采用与组件示例一致的样式，展示组件与钩子协同用法。
- 🧹 多项修复：Checkbox/Radio 回车键不再阻止隐式表单提交，DropZone 点击隐藏文件输入不再转移焦点，Virtualizer 新增 shouldObserveItemSize 等。
- 📦 发布多个更新包，包括 react-aria-components@1.20.0、react-aria@3.51.0、react-stately@3.49.0 等。

---

### [React 拖放区](https://react-dropzone.js.org/)

**原文标题**: [react-dropzone](https://react-dropzone.js.org/)

overview summary
- 🧩 一款基于 React 的简易 HTML5 拖放区域库，采用 hooks-first 设计，便于集成。
- 📁 支持文件夹拖放，方便处理多文件及递归目录结构。
- ✅ 内置文件验证功能，可自定义接受类型、大小等规则。
- 🎨 允许完全控制页面标记与样式，不强制渲染特定 UI。
- 📦 可通过 npm 安装，命令为：npm install react-dropzone。
- 🚀 提供快速开始指南、示例代码及 GitHub 仓库链接，方便上手与扩展。

---

### [2026年7月 - 默认使用Base UI](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)

**原文标题**: [July 2026 - Base UI as the Default - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)

overview summary
- 🏛️ shadcn/ui 宣布新项目默认使用 Base UI，取代 Radix 作为默认组件库。
- 📜 历史背景：2023 年 shadcn/ui 基于 Radix 构建，如今 Radix 团队的新项目 Base UI 成为新默认。
- ⚖️ 官方强调“不要切换库”的旧观点，但通过重建组件、保持抽象，让用户自行选择，现在社区已偏向 Base UI。
- 🆕 新增 `npx shadcn create` 和完整 Base UI 文档，项目创建时 Base UI 与 Radix 的选择比例为 2:1。

- ✅ Base UI 已稳定（1.6.0，周下载量 6M+），团队持续改进，官方新项目均使用 Base UI。
- 🔄 改变内容：新项目默认 Base UI，`shadcn init` 默认选 Base UI，文档标签页默认显示 Base UI，Radix 仍一键可切换。
- 🛡️ Radix 并未弃用：仍支持，所有更新和新组件都会同步发布到两个库（除非仅限 Base UI）。
- 🚫 无需强制迁移：Radix 成熟稳定，官方仍在生产环境使用；现有项目可继续运行。
- 🧩 偏好 Radix 的新项目可用 `-b radix` 标志，CI 脚本需加该参数以保持原有行为。
- 📦 注册表构建者可通过 `registry:base` 配置指定库，未配置项默认初始化为 Base UI。

- 🛠️ 提供迁移技能（skill）：通过 `pnpm dlx skills add shadcn/ui` 安装，可用自然语言指令如“迁移 accordion 到 base-ui”。
- 📈 迁移是渐进式的：可逐组件迁移，两个库可共存，随时停止并继续。
- 🤔 选择技能而非 codemod 的原因：用户代码已定制化，codemod 只能处理未修改组件，技能则携带两种库的差异知识，由代理理解用户改动并迁移。
- ⚙️ 机械性改动（如 `asChild` 变为 `render`）自动修复，行为差异会被标记而非静默修补。
- 📝 迁移产物：可工作的代码（通过类型检查和构建）、每组件报告（存放于 `.migration/`）、干净的 git 历史（每组件一个提交，便于回滚）。
- 📋 报告包含变更、未改动文件、行为差异、手动验证清单，无隐藏状态，可跨会话继续。
- 🧪 兼容 Claude Code、Cursor 等支持技能的代理，实测 60+ 组件（其中 36 个 Radix）的全量迁移约 25 分钟，每个组件约 10k tokens。
- 🚀 文末附带 Vercel 部署推广。

---

### [](https://github.com/mui/material-ui/releases/tag/v9.3.0)

**原文标题**: [Release v9.3.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v9.3.0)

MUI v9.3.0 版本发布，汇集了 18 位贡献者的改进，重点增强无障碍支持、修复多个组件问题，并同步更新文档与核心基础设施。

- 🎉 发布 v9.3.0，感谢 18 位贡献者，主要聚焦无障碍与组件行为优化
- ♿️ Toggle Button Group 键盘导航改为 roving tabindex 模式，提升可访问性
- ♿️ Autocomplete 新增 status 槽，可播报加载中及无选项消息
- 🔧 @mui/material：修复 Autocomplete aria live、按钮组/复选框/单选按钮的全局 ripple 设置、Modal/Dialog 滚动条补偿、Select 装饰重叠等问题
- 🛡️ @mui/system：修复 cssVarsParser 中的原型污染风险
- 🧹 @mui/codemod：修复文件间状态泄漏、移除 eval()、完整转换样式导出
- 📚 文档：更新 Shadow DOM、CSP、Grid 升级指南、TransferList 示例，并修复链接与拼写错误
- 🛠️ 核心：修复 Dependabot 警报、固定 CI 的 Node 版本、优化团队同步与发布流程

---

### [](https://github.com/hCaptcha/react-hcaptcha)

**原文标题**: [GitHub - hCaptcha/react-hcaptcha: hCaptcha Component Library for ReactJS and Preact · GitHub](https://github.com/hCaptcha/react-hcaptcha)

本文介绍了 @hcaptcha/react-hcaptcha，这是一个用于 React 和 Preact 的 hCaptcha 组件库，旨在作为 reCAPTCHA 的隐私友好替代品。文章详细说明了安装方法、多种使用方式（标准表单、编程调用、Provider/Hook 模式）、完整的 API 参考（Props、事件、方法），以及调试建议和贡献指南。

- 📦 安装：通过 npm 安装 `@hcaptcha/react-hcaptcha`，需先注册 hCaptcha 获取 sitekey。
- ⚛️ 基本使用：将 `<HCaptcha>` 放在 `<form>` 等父组件中，传入 `sitekey` 和 `onVerify` 回调即可自动加载 API。
- 🛠️ 编程调用：通过 `useRef` 和 `onLoad` 事件，在 hCaptcha API 就绪后调用 `execute()` 方法。
- 🎣 Provider/Hook 模式：使用 `HCaptchaProvider` 和 `useHCaptcha`，可便捷获取 `executeInstance`、`token`、`ready` 等状态。
- 📝 配置项：支持 `sitekey`、`size`、`theme`、`languageOverride`、`onVerify`、`onError` 等众多 props。
- 🔔 事件回调：包括 `onVerify`、`onError`、`onExpire`、`onLoad`、`onReady` 等，用于处理验证生命周期。
- 🧩 实例方法：提供 `execute()`、`resetCaptcha()`、`getResponse()` 等方法，注意提交表单后需重置验证状态。
- 🚀 高级用法：可与 Formik、React Hook Form 集成，通过 ref 操作底层 API，并支持 Enterprise 特性（如 `rqdata`）。
- 🐛 调试要点：避免双重导入 api.js；若同时使用 reCAPTCHA 需设置 `reCaptchaCompat=false`；Sentry SDK 需 8.x 以上版本。
- 🔒 安全提示：对控制 API 地址的 props（如 `scriptSource`、`apihost` 等）应做白名单验证，防止恶意配置注入。
- 👥 贡献与开发：使用 pnpm 脚本进行开发、测试和构建，通过 GitHub Release 触发自动发布流程。
- 📄 许可证：项目基于 MIT 协议开源。

---

### [](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.7.0)

**原文标题**: [Release v9.7.0 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.7.0)

react-three-fiber v9.7.0 版本发布，重点修复了 reconciler 相关问题，并增强了与 react-dom 的一致性。

- 🔧 修复内部子元素重排同步问题，避免 React 重排子元素时内部映射失步导致微妙 bug
- 🎯 修复 pierced 属性重置逻辑，防止取消属性时错误重置为基础对象值
- ⚙️ 修复 host props（如 dispose、onUpdate）更新，避免命令式更新值被意外覆盖
- 🧩 强化实例重建批处理，修复因 React.memo 导致的边缘情况
- 🚀 事件优先级与 react-dom 对齐，例如滚轮事件优先级高于指针事件
- ⏳ 支持 reconciler 微任务，可根据优先级延迟工作
- 📦 包含多项文档、CI 和代码清理更新，并新增多位贡献者

---

### [无](https://expo.dev/blog/how-to-apply-professional-design-principles-in-ai-app-development?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [None](https://expo.dev/blog/how-to-apply-professional-design-principles-in-ai-app-development?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

您没有提供需要总结的文本内容，请补充后我会按照模板为您生成中文要点总结。

---

### [](https://flueframework.com/blog/flue-2/)

**原文标题**: [Flue 2.0 | Flue](https://flueframework.com/blog/flue-2/)

Flue 2.0 正式发布，这是一个基于全新 hooks 架构重建的智能体框架，让智能体可以在运行时动态进化能力、管理状态和生命周期，解决了传统静态定义方式在复杂工作流中的局限性。

- 🎣 核心创新是 Agent Hooks：借鉴 React Hooks 设计，让智能体拥有持久状态、生命周期事件和按需挂载工具/模型的能力。
- 🔄 从静态到动态：相比 Flue 1.0 及主流 SDK 的静态“配置式”智能体，2.0 支持条件化工具、动态模型升级和逐步解锁能力。
- 🧩 内置 16 个 hooks：包括 useSkill()、useTool()、useSubagent() 等，并支持自定义 hooks 打包分享到 npm。
- ⚙️ 工作流即状态机：通过 usePersistentState 加条件工具实现多步骤流程，每个步骤可挂载专属模型、技能和工具。
- 🛠️ 新增 CLI 与 Vite 架构：本地使用 `flue run` 运行，构建改为标准 Vite + Hono，`flue init` 脚手架，并集成 Cloudflare 部署。
- 📡 内置无状态 MCP 支持：useMcpConnection() 挂载远程 MCP 工具，支持可选连接，降级优雅，可嵌入自定义 hooks。
- 🧱 简化 Workflows 与 Actions：删除 defineWorkflow()，改用持久化消息保证恰好一次处理，工具可通过 durable: true 实现检查点副作用。
- 💬 新的会话级 SDK：@flue/sdk 封装单会话的 send/read/observe/abort，消息携带类型化元数据；@flue/react 提供前端 UI 流式接入。
- 🔍 Cloudflare 零配置追踪：部署后启用 Workers Traces 即可得到全量会话内容、元数据与成本追踪。
- 🚀 首个稳定版：包含 200+ 修复和改进，提供快速开始提示词、迁移指南，并鼓励 GitHub Star 支持和关注 @flueai。

---

### [](https://astro.build/blog/astro-720/)

**原文标题**: [Astro 7.2 | Astro](https://astro.build/blog/astro-720/)

Astro 7.2 正式发布，核心亮点是实验性的增量静态构建功能，可跳过未变更页面的重新生成，大幅提升大型静态站点的构建效率。同时新增了会话支持关闭选项、`astro preview` 后台模式、相对路径的自定义日志入口，并包含多项社区贡献与改进。

- 🚀 实验性增量静态构建：通过 `experimental.incrementalBuild` 标志启用，路由在 `getStaticPaths()` 中返回 `cacheKey`（如内容集合的 `digest`），结合模块哈希，仅在数据或代码变化时重新渲染页面，缓存位于 `node_modules/.astro/`。
- 🔒 可完全关闭会话支持：配置 `session: false` 即可移除 SSR 输出中的会话运行时，适配器不再挂载默认驱动，`Astro.session` 变为 `undefined`；未配置驱动时也会自动摇树优化。
- 🖥️ `astro preview` 新增后台模式：使用 `astro preview --background` 启动，支持 `status`、`logs`、`stop` 子命令，与 `astro dev` 的后台机制一致，方便开发者或 AI 代理管理。
- 📝 相对路径自定义日志入口：`logger.entrypoint` 现在可直接填写相对路径字符串（如 `'./src/custom-logger.js'`），无需再使用 `new URL(..., import.meta.url)`，原有 URL 形式仍有效。
- ⚙️ 其他改进与升级方式：包含多项错误修复和细节优化，完整变更见官方 changelog；可通过 `npx @astrojs/upgrade` 或各包管理器命令升级至最新版。
- 👥 社区致谢：感谢核心团队及众多贡献者（代码、文档、测试等），并预告新周边商品上线，欢迎通过 Discord、GitHub 等渠道反馈。

---

### [](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack)

**原文标题**: [Keyv and friends compromised in npm supply chain attack](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack)

2026年8月4日，npm 生态爆发一起大规模供应链攻击：攻击者入侵了 keyv 库维护者的 GitHub 账户，在 keyv 及整个缓存工具包家族中注入窃密蠕虫“Shai-Hulud”。截至8月5日，已有 444 个包、1381 个版本被感染，受影响包月度安装量合计超过 20 亿次，其中 keyv 本身月下载量约 6 亿次、flat-cache 约 5.8 亿次。

- 🎯 攻击者入侵 keyv 维护者的 GitHub 账户，直接向 main 分支推送恶意文件并立即发布新版本，成功利用 GitHub Actions 签名的有效 provenance 将带毒包发布到 npm
- 📦 受影响包包括 keyv、flat-cache、file-entry-cache、cacheable-request、cacheable、@cacheable/memory、cache-manager、@cacheable/node-cache、@cacheable/utils、@cacheable/net、ecto 等，每个包都注入了 setup.mjs、Math_Symbol.js 两个恶意文件
- ⚙️ 恶意包通过 package.json 中的 “preinstall”: “node setup.mjs” 钩子，在用户执行 npm install 时自动触发，无需用户任何额外操作
- 🧬 setup.mjs 是一个混淆的下载器，会静默下载 Bun JavaScript 运行时（v1.3.13），然后用它来执行真正的 728 KB 重混淆 payload —— Math_Symbol.js
- 🔑 Math_Symbol.js 包含多种凭证窃取器：读取 ~/.npmrc 并验证 npm token、窃取 GitHub PAT/OAuth/App token、在 GitHub Actions runner 上直接转储进程内存获取 OIDC token
- ☁️ 窃取目标覆盖 AWS 凭证（含 IMDSv1/v2、ECS 元数据端点，还会枚举所有 AWS Secrets Manager 机密）、Kubernetes secrets（利用 service account token 查询 API）、HashiCorp Vault token（六个来源按优先级依次尝试）
- 💳 还专门扫描 Stripe API 密钥（sk_/pk_ 前缀）和 Slack token（xox[baprs]- 前缀），并通过约 200 个 glob 模式进行全盘文件扫描，覆盖 .env、私钥文件、SSH 密钥、Terraform 状态、Docker registry 凭证、KeePass 数据库、VPN 配置和 IDE 配置
- 🔐 所有窃取数据经 RSA 公钥加密后才外传，导致数据虽存放在公共基础设施上却无人能读；主要外传给一个描述为 “Shai-Hulud: Here We Go Again” 的公共 GitHub 仓库（超 1300 个），GitHub 上传失败时回退到 npm-cache[.]com:443/router
- 🔄 为基础设施提供轮换能力：回退域名地址从以太坊智能合约 0xE1f2395e...93103 动态获取，攻击者可随时更换服务器而无需更新恶意代码
- 🪱 自带蠕虫式自我传播：利用偷来的 npm token 列出所有可写权限的包，自动升 patch 版本、注入恶意脚本和 setup.mjs/math_init.js（二季度生成感染的特征是 math_init.js），重新打包发布到 npm，已造成超 400 个包被社区传播感染
- 🐙 第二个传播向量是 GitHub 仓库感染：发现 ghs_ token 后，在最多 50 个分支（跳过 dependabot/copilot）上提交恶意钩子，写入 .claude/settings.json 和 .vscode/tasks.json，开发者一打开项目或启动 Claude Code 即被感染，提交伪装为 “chore: update config” 且作者为 claude
- 🛡️ Aikido 检测建议：用户可在中央 feed 中按 malware 类别筛选，此问题显示为 100/100 严重级别；建议立即手动重扫；非用户可创建免费账户连接仓库，Device Protection 可覆盖团队设备，Safe Chain（开源）可在安装前拦截 npm/npx/yarn/pnpm/pnpx 命令检查包安全性
- 🔍 关键 IOC：setup.mjs 哈希 54dc7ea5...、社区版 fd3ca400...？Math_Symbol.js/math_init.js 哈希 9fc2570b...，网络端点为 npm-cache[.]com:443/router，以及所有描述含 “Shai-Hulud: Here We Go Again” 的公开 GitHub 仓库都可视为攻击者基础设施

---

### [](https://github.com/wiz-sec-public/wiz-research-iocs/blob/main/reports/keyv-packages.csv)

**原文标题**: [wiz-research-iocs/reports/keyv-packages.csv at main · wiz-sec-public/wiz-research-iocs · GitHub](https://github.com/wiz-sec-public/wiz-research-iocs/blob/main/reports/keyv-packages.csv)

该页面是 Wiz Research 公开的威胁情报仓库中一个 CSV 文件的 GitHub 浏览界面，文件记录了与 KeyV 相关的恶意软件包指标（IOC），供安全社区参考。

- 📁 仓库名为 `wiz-sec-public/wiz-research-iocs`，属于公开研究项目
- 📄 当前浏览的文件是 `reports/keyv-packages.csv`，内容为 KeyV 相关软件包 IOC 列表
- 🔢 文件共 447 行，大小约 31 KB
- ⭐ 仓库获得 111 个 Star，说明受到一定关注
- 🍴 有 11 个 Fork，便于社区复制和二次分析
- 🔒 需要登录才能修改通知设置，但文件本身可直接查看或下载
- 📥 提供预览、代码、Blame、Raw 下载等操作入口，方便研究人员获取原始数据

---

