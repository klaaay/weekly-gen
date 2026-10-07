### [](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=twir&utm_content=ad-twir-003&ref=twir&dub_id=UmMN5XfJgV8mTSEJ)

**原文标题**: [CodeRabbit | Governance & Control for Agentic Development](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=twir&utm_content=ad-twir-003&ref=twir&dub_id=UmMN5XfJgV8mTSEJ)

机器人审查指出：项目记录更新后未清除缓存，导致 Redis 中残留过期的 project key。建议在 mutation 后使缓存失效，并用 `updateProjectAndInvalidate` 替代直接更新。

- 🤖 coderabbitai 机器人于 2 分钟前完成审查
- ⚠️ 问题：记录虽已更新，但 Redis 中仍保留旧的 project key
- 🔄 建议：在 mutation 后执行缓存失效
- ✏️ 将 `await db.project.update(input)` 替换为 `await updateProjectAndInvalidate(input)`
- ✅ 确保数据更新后缓存保持同步

---

### [Next.js 16.4 | Next.js](https://nextjs.org/blog/next-16-4)

**原文标题**: [Next.js 16.4 | Next.js](https://nextjs.org/blog/next-16-4)

Next.js 16.4 发布，核心是正式推荐 Cache Components 作为所有 Next.js 应用的最佳选择，并计划在 Next.js 17 成为默认模型；新应用默认启用，现有应用可通过代理工具迁移，同时带来 Turbopack、构建性能、React 19.3 和多项实验功能改进。

- 🧩 Cache Components 是新的编程模型：用 `'use cache'` 将组件树部分标记为可缓存，组合客户端缓存、服务端缓存与请求时渲染，替代旧版 App Router 的隐式缓存。
- ⚙️ 启用方式为 `cacheComponents: true` 与 `partialPrefetching: true`；`create-next-app` 新应用默认启用，现有应用可用 `next upgrade --agent` 和相关 Skills 迁移。
- 🛡️ `ensureStatic` 可保证路由的 shell、预取或完整导航为静态，支持 `"shell"`、`"prefetch"`、`"navigation"`，也可在布局中统一设置，防止动态内容意外混入。
- ⏳ 新增 `navigation()` 与 `prefetch()` API：可在预取阶段排除缓存内容，延迟到实际导航或显式预取时再加载，平衡用户体验与服务器成本。
- 🤖 代理升级：`next upgrade --agent=latest` 让代理端到端升级应用；`experimental.agentUpgrade` 可在开发或构建时提醒安全或最新版本升级。
- 📝 代理反馈：`experimental.agentFeedback` 让代理收集问题草稿，用户审核后可发送；默认省略源码、日志和密钥，需启用遥测且不在 CI 中运行。
- 💾 开发体验优化：Turbopack 磁盘缓存减少 20–25% 空间，采用 Zstandard 压缩；Lazy server HMR 只编译和更新当前请求需要的服务端模块。
- 📦 构建体积优化：Turbopack 共享 runtime、生产环境更短 CSS Module 类名、export mangling，降低生产包体积并提升缓存命中率。
- ⚛️ 内置 React 19.3：带来稳定的 View Transitions、Fragment Refs、`browser()` API 等更新。
- 🦀 实验性 Rust React Compiler：新增快速检查，跳过无需优化文件；内存使用降低 30%，编译时间减少 15%。
- 🧹 实验性清理与懒编译：`turbopackGc` 清理内存和磁盘缓存；`turbopackLazyDynamicImports` 按浏览器请求编译动态导入；worker threads 降低资源占用。
- 🔗 实验性工作区支持：`turbopackAdditionalRoots` 支持项目外符号链接依赖，并可手动集成 pnpm、Bun、Nub、aube 的全局虚拟存储。
- 📊 Turbopack Bundle Analyzer 增强：新增路由摘要首页、表格视图、快照与 diff、关键渲染路径区分，并提供 `next-bundle-optimizer` 代理技能。
- 🌐 反馈与社区：可通过 GitHub Discussions、GitHub Issues 和 Discord 反馈；版本由 Next.js 与 Turbopack 团队及众多社区贡献者共同完成。

---

### [TanStack Charts 1.0 | TanStack 博客](https://tanstack.com/blog/tanstack-charts-1-0)

**原文标题**: [TanStack Charts 1.0 | TanStack Blog](https://tanstack.com/blog/tanstack-charts-1-0)

overview summary
TanStack Charts 1.0 正式发布，主打“无需长大后更换”的可组合、类型安全图表方案，让图表能随产品与数据可视化需求持续演进。

- 🚀 **1.0 发布**：Tanner Linsley 于 2026 年 10 月 5 日宣布 TanStack Charts 1.0，表示已准备好支持生产使用。
- 🧩 **可组合架构**：图表由 marks（线、点、柱等）、scales、坐标轴与交互组合而成，受 Grammar of Graphics 与 Observable Plot 启发。
- ➕ **按需叠加**：可在折线图上加柱、点、高亮、注释或自定义 tooltip，而不用寻找或重建特定图表类型。
- 🛠️ **高度可定制**：支持自定义 marks、scales、交互、渲染器，并可深入 scene contracts 做特殊可视化。
- 🔒 **类型安全贯穿**：从选数据、过 scales 到映射 marks 与交互，类型信息尽量不丢失，复杂图表和 AI 辅助都更可靠。
- 🖼️ **渲染可选**：默认 SVG，Canvas 作为单独导入与渲染器按需启用；动画与 Motion 也是可选集成。
- 📦 **轻量模块化**：支持紧凑 scales 与 D3 scales，尽量拆成最小部件；有 bundle budgets、测试和浏览器测试控制体积。
- 🧭 **作者经验**：作者有 D3、Chart.js 2.0、react-charts、Observable Plot 等十年图表经验，AI 辅助实现了大量设计想法。
- ✅ **1.0 含义**：代表 API 可依赖，升级不应导致重建；未来变更会考虑从旧 API 到新 API 的迁移，自定义 mark/renderer 也纳入支持。
- 🤖 **行动号召**：鼓励用 AI 把实际应用中的图表改为 TanStack Charts，尝试以前难实现的奇怪图表，并反馈哪里不顺手。
- 🔗 **资源入口**：可浏览图表目录或直接开始使用 TanStack Charts。

---

### [React 适配器 | TanStack Charts React 文档](https://tanstack.com/charts/latest/docs/framework/react/adapter)

**原文标题**: [React Adapter | TanStack Charts React Docs](https://tanstack.com/charts/latest/docs/framework/react/adapter)

TanStack Charts 的 React 适配器 `@tanstack/charts/react` 是一个轻量的生命周期与 SSR 适配层，图表定义、比例解析、指南布局、场景、渲染、动画和交互仍由框架无关的核心 `@tanstack/charts` 负责。文档涵盖公共导出、渲染生命周期、SSR 与水合、尺寸布局、样式、Tooltip 组合、定义标识、回调新鲜度及核心边界。

- 🧩 **定位**：适配器只负责 React 生命周期与 SSR，不重新定义 marks、比例、Tooltip、动画等核心语义。
- 📦 **公共导出**：从 `@tanstack/charts/react` 导出 `Chart` 及 `ChartCommonProps`、`ChartProps`、`ChartDefinition`、`ChartPoint` 等类型。
- 🖼️ **渲染器选择**：通过子路径区分；默认 `Chart` 为 SVG；`/canvas` 使用内置 Canvas 渲染器；`/core` 需传入 `renderer`；定义中也可混用 `canvasChartRenderer` 形成 SVG + Canvas 混合表面。
- 💬 **Tooltip 入口**：使用 `renderTooltipBody` 时应从 `@tanstack/charts/react/tooltip` 导入；现有默认导入需迁移到该入口。
- 🔄 **渲染生命周期**：每个挂载组件创建一个 `ChartRuntime`；提交后通过布局副作用挂载共享 DOM host、转发最新选项；后续提交调用 `host.update`；定义标识变化会重建场景。
- 🧠 **记忆化建议**：捕获组件值的定义应用 `useMemo` 包裹；模块级固定定义无需组件内记忆化。
- 🖥️ **SSR 与水合**：默认 SVG 入口输出外层 host、surface 及完整可访问 SVG；Canvas 入口输出命名 Canvas 根与五个 `aria-hidden` canvas，服务端不绘制像素，客户端挂载后绘制。
- 🧪 **确定性要求**：服务端与客户端应使用相同的数据、比例域、定义、尺寸和自定义渲染器；`idPrefix` 未提供时由 `React.useId()` 生成。
- ⌨️ **可访问性**：`tabIndex` 默认 `0`；设置 `keyboard: false` 时强制为 `-1`。
- 📐 **尺寸与布局**：渲染 `.ts-chart-host` 与 `.ts-chart-surface` 两层容器；`height` 优先于 `aspectRatio`；`initialWidth` 默认 `640`；无高度与宽高比时回退为 `320px`；非正或非有限比例回退默认高度。
- 🎨 **className 与 style**：React 展示属性作用于外层 host；`className` 追加在 `ts-chart-host` 后；`style` 为 `React.CSSProperties` 且最后展开，会覆盖适配器计算的位置、宽高和比例。
- 🧷 **Tooltip 内容组合**：`renderTooltipBody` 将 React 内容挂载到内置 Tooltip 表面，上下文提供 `points`、`content`、`defaultBody`、`pinned`、`dismiss`；组合 `defaultBody` 可保留核心标题、行、格式与色块。
- ⚠️ **交互内容限制**：自定义 body 在瞬态时为惰性，仅展示内容可保持可见，控件应仅在 `pinned` 为 true 时渲染；添加 `portal` 扩展可提升整个表面。
- 🔒 **定义标识**：用 `defineChart` 在组件外定义固定图表；实时状态需按捕获值记忆化完整定义，定义标识即应用更新边界。
- 🔔 **回调新鲜度**：每次提交的完整 prop 集都会转发给 host，焦点、分组焦点、选择与渲染回调始终使用最新提交的函数。
- 🧱 **核心边界**：适配器不重定义 marks 或图表规格、比例选择与数据准备、Tooltip 与焦点语义、动画与协调、自定义 marks 或渲染器。

---

### [](https://thisweekinreact.com/newsletter/285#react)

**原文标题**: [This Week In React #285: React.foundation, Rust Compiler, Sätteri, Motion, TanStack Table, React Router, Flow, NavLink | Runtimes, JSI, Standard Navigation, Testing Library, Static Hermes, BottomTabs, AGP, AI, Windows | VoidZero, npm, Rolldown, Angular | This Week In React](https://thisweekinreact.com/newsletter/285#react)

本期《This Week In React》#285 汇总 React、React Native 与前端基础设施的重要动态：React 基金会官网与仓库迁移落地，React Compiler 正式合并 Rust 移植；React Native 推出多运行时方案，Static Hermes 与标准导航继续演进；Cloudflare 收购 VoidZero，npm v12 将默认阻止安装脚本；多个核心库发布新版本。

- ⚛️ **React 基金会**：官网已上线，计划资助关键库维护者、开设周边商店并将利润回馈维护者、发布季度透明报告、推出贡献者状态页；React、React Native、Yoga、JSX、Metro、CRA 等仓库从 facebook 迁移至 react GitHub 组织。
- 🦀 **React Compiler Rust 移植 PR 已合并**：尚未发布 Rust crate/npm 包，Oxc 集成已进入 v0.135，并在 Rolldown、Oxlint、SWC、Bun 中推进。
- 🧹 **React RFC**：提议让 `useEffect` 清理函数支持 disposable / `using`，即返回带 `Symbol.dispose` 的资源。
- 🔄 **Flow for TypeScript Users in 2026**：Flow 语法与 TS 趋同但更严格，支持模式匹配、component/hook/renders 语法，编译器也在移植到 Rust。
- 🧭 **Next.js Active NavLink**：构建生产级 `NavLink`，提供 `isActive/className` 渲染 prop，需处理首帧闪烁与 Suspense Cache Components。
- ⏳ **加载状态优化**：通过路由过渡、loader、预加载和全局 fallback，让加载状态尽量消失；另有 RSC 与打包器集成、父组件获知子组件、`useEffect` 问题等文章。
- 📦 **React 相关包**：Sätteri 推出 Rust Markdown/MDX 引擎；Motion 12.40 支持 `arc()` 曲线动画；TanStack Table 9 beta 重构状态管理并兼容 React Compiler；React Router 8 预发布、7.17 为 AI agent 提供 Markdown 文档；React 19.2.7 等修复 Server Actions FormData 回归。
- 📱 **React Native Runtimes**：Margelo 与 Callstack 推出多运行时层，可运行选定组件/页面/无头任务，通过原生 Zustand 风格 C++ 单例共享状态，支持预热、类型化跨运行时调用和 Expo 配置插件。
- 🤖 **React Native RFC - AGP v9**：制定三阶段采用策略，在 AGP v10 移除选择退出前支持内置 Kotlin。
- ⚡ **Static Hermes**：下一稳定版将原生支持 Set 操作、Iterator helpers、`groupBy`、`TextDecoder` 等，并更快、支持内置 TypeScript 类型剥离。
- 🧭 **Standard Navigation**：React Navigation 与 Expo Router 已集成共享导航抽象，减少生态碎片化。
- 🍎 **JSI in Swift**：SDK 56 中 Expo 原生模块在 Apple 平台直接调用 JSI，移除 Objective-C++ 层，调用速度提升 1.6–2.3 倍。
- 🧩 **React Native 生态**：`@expo/vector-icons` 弃用；Metro `inlineRequires` 系列；WWDC 2026 后设备端 AI；棕地迁移到 RN；AppJS 2026 回顾。
- 📦 **React Native 包更新**：Testing Library 14.0 支持 React 19/异步 API；Windows 0.83；DocuSign；Lynx 3.8；Livechart；Nitro Fetch 1.4；Data Scanner；Agent Device 0.17；Rozenite 1.12；Bottom Tabs 1.3。
- ☁️ **Cloudflare 收购 VoidZero**：Vite、Vitest、Rolldown、Oxc、Oxfmt、Oxlint、Vite+ 保持开源 MIT 与社区驱动，Cloudflare 承诺无锁定，并围绕 Vite 构建新 cf CLI。
- 🔐 **npm v12 安全变更**：计划 7 月默认阻止 install 生命周期脚本，提升供应链安全。
- 🛠️ **其他工具更新**：tsgo 每线程运行一个类型检查器导致高内存；Rolldown 1.1 支持 lazy barrel 优化并与 tsc 对齐 references；Angular 22 带来 Signal Forms、Angular Aria、默认 OnPush、异步 DI 等。
- 🎤 **会议与社区**：React Advanced London、Chain React、React Native Connection、Agent Conf 等开放 CFP/早鸟票；并附多场 React Native 相关演讲视频。

---

### [React 基金会贡献者峰会 2026 · React 基金会](https://www.react.foundation/summit)

**原文标题**: [React Foundation Contributors Summit 2026 · React Foundation](https://www.react.foundation/summit)

overview summary
- 🗓️ React Foundation Summit 2026 将于 2026 年 11 月 10–12 日在伦敦举行，9 日和 13 日为旅行日。
- 🎯 这是 React Foundation 工作组的首次线下聚会，目标是连接各小组并决定下一步。
- 🔒 活动为仅限邀请的工作峰会，面向 React Foundation 工作组成员，非公开会议；其他人可自我提名。
- 🧭 四大目的：确立身份、制定路线图、建立信任、正式化治理。
- 🗓️ 议程：11 月 10 日为全体会议，11 月 11–12 日为工作组日，聚焦路线图规划、深入讨论与协作。
- 📍 场地：Meta King's Cross，地址 11-21 Canal Reach, London，靠近 King's Cross St Pancras 车站。
- 🧑‍🤝‍🧑 重叠工作组成员需协调日程，特别是 DevX 与 React Native 之间；可合并或拆分会议，鼓励跨组会议。
- 🛠️ 计划参与的工作组包括 React Native 的 Core Runtime & Renderer、Platform Expertise、Stable API、Distribution 子团队，以及 React Fiber、DevX / Developer Tools、Server、Compiler。
- ✈️ 基金会无法为所有参与者赞助差旅；希望雇主承担费用，需要额外支持者可直接联系基金会。
- 🍽️ 餐饮和饮食需求详情将在后勤计划确认后公布。
- 📅 详细议程将适时发布；本页面是参与者的权威信息来源，最后更新于 2026 年 10 月 2 日。
- 🗺️ 建议参与者 11 月 9 日抵达、11 月 13 日离开，并可将活动加入日历。

---

### [](https://reactghana.react.foundation/)

**原文标题**: [React Conf Ghana · Coming Soon](https://reactghana.react.foundation/)

React Conf Ghana 将于 2026 年 11 月 4–5 日在加纳阿克拉举行，由 React Foundation 主办，地点在加纳大学健康科学学院西非遗传医学中心。活动面向 React 开发者、设计师、教育者与社区建设者，结合演讲、工作坊和社区交流，连接西非与全球 React 社区。

- 📅 时间地点：2026 年 11 月 4–5 日，加纳阿克拉，加纳大学校园内的西非遗传医学中心。
- 🎯 主题口号：React、文化与社区；Build the future. Inspire the world. / #GhanaBeAwesome。
- 🧑‍💻 参会人群：工程师、设计师、教育者和社区建设者；从生产环境 React 老手到初学者都欢迎。
- 🎤 活动内容：两天演讲、动手工作坊和社区时刻，核心价值为学习、连接、构建、启发。
- 🎟️ 门票与参与：门票 200 GHS；可购票、成为演讲者或赞助商。
- 📣 演讲者：阵容即将公布；CFP 开放至 2026 年 10 月 18 日，可提交演讲。
- 🌍 多样性奖学金：为科技领域弱势群体及无法参会者提供会议通行；学生、转行者、首次参会者均可申请，截止 2026 年 10 月 15 日。
- 🤝 赞助机会：面向西非活跃 React 工程师、设计师和社区建设者，可展示工具、接触人才；详情见赞助方案。
- 📧 联系与定位：events@react.foundation；西非最大 React 开发者、设计师和社区建设者聚会。

---

### [](https://www.meticulous.ai/blog/lessons-from-a-decade)

**原文标题**: [Testing Frontend — Lessons from over a million lines of TypeScript at Palantir](https://www.meticulous.ai/blog/lessons-from-a-decade)

作者基于在 Palantir 十年、数百万行 TypeScript 前端经验，总结高效前端测试的核心：测试策略决定工程速度，维护成本是关键；应选择最小切割和稳定 API 边界，避免脆弱组件测试，用可扩展集成测试降低维护；手动测试无法覆盖海量边界，Meticulous AI 通过录制交互自动生成并维护端到端视觉测试，接近零维护。

- 🧪 测试是少数可能让工程速度翻倍的工程投资；多数自动化前端测试因编写和维护成本过高反而拖慢团队。
- 💰 维护成本决定可负担测试数量：单测维护成本降低可指数级提升测试总价值；要么让更新极快，要么让测试几乎不需更新。
- ✂️ 单元测试应测试“合适大小”的单元，并按最小切割选择边界：只 mock 最小、最稳定的 API 表面。
- 🚫 通常不要写 Enzyme/组件测试：它们慢且脆弱；把复杂逻辑抽到工具函数中测试更可靠。前端手动单测覆盖率超 50% 可能已过度投资。
- 🔌 可扩展集成测试应寻找应用中稳定的 API，把变化值作为复杂度来源；让新增测试只需丢文件，成本接近零。
- 🗺️ 示例：MapboxGL 用 style spec JSON 映射到截图；Palantir 后端用“数据+查询+预期快照”三元组，测试写一次不再改。
- ✅ 值得写：复杂逻辑的单元测试、少量关键集成测试、极少数端到端冒烟测试；不要追求 100% 覆盖率。
- 📉 大型 Web 应用有数万边缘情况，手动维护测试无法接近 100%；开发者本地、预览和生产交互形成关键数据流，可自动回归测试。
- 🤖 Meticulous AI 录制交互并理解每段执行代码，自动维护接近 100% 覆盖的视觉快照测试，跨分支、配置、屏幕尺寸等，且确定性环境无 flaky。
- 🚀 结果：测试分母归零，最大可维护测试数不受限；开发者可自信快速重构，持续保持高工程速度。

---

### [](https://github.com/vercel/next.js/pull/97393)

**原文标题**: [Add unstable parameter matching APIs by gnoff · Pull Request #97393 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/97393)

本 PR #97393 已合并，为 Next.js Cache Components 引入不稳定的参数匹配 API：在保留 `generateStaticParams` 示例的同时，按参数分别控制新值是返回 404、阻塞生成、返回 fallback shell，还是保持 dynamic。

- 🚀 新增 `unstable_paramMatching` 与 `unstable_generateParamMatching`，无需额外配置开关，仅要求 `cacheComponents: true`。
- 🧩 支持四种策略：`not-found`、`blocking`、`fallback`、`dynamic`；其中 `dynamic` 会让参数不进入预渲染。
- 🧱 `generateStaticParams` 继续提供具体示例；例如 `/en/catalog/t1/items/b1` 会被预渲染，其他语言返回 404，缓存未命中时按策略阻塞或立即返回 fallback UI。
- 🪜 策略从 layout 向 page 合并，后代只覆盖已提供的键；显式模式必须遵循 URL 顺序：`not-found → blocking → fallback → dynamic`。
- ⚠️ `not-found` 要求其前面的参数也显式设为 `not-found`；同一参数定义的 route 或 parallel branch 必须保持一致。
- 🧠 未配置参数保留推断；无示例的未配置尾部保持 dynamic；显式 dynamic 参数不能进入预渲染。
- 🛡️ Shell 校验遵循显式 fallback 边界，`instant = false` 可退出该校验；`output: 'export'` 要求所有参数显式 `not-found`。
- 🚦 `unstable_ensureStatic = 'navigation'` 允许 `blocking` 与 `not-found`，但拒绝有效 `fallback` 和 `dynamic`，并仍要求完整 `generateStaticParams` 与完全静态服务输出。
- 🧪 覆盖策略合并、校验、类型生成、shell 选择、阻塞/回退行为、导航、参数编码、重新验证、根缓存隔离，并覆盖两个 bundler、Partial Prefetching 开/关及真实 adapter 部署测试。
- 👀 审查中 `unstubbable` 批准；`lubieowoce` 留下评论并推动简化；`gnoff` 合并 7 个提交。
- 📉 性能统计显示：node_modules +483 kB，Webpack 构建时间 +731ms/+559ms，Turbo 缓存构建 -265ms；Bundle 总体基本稳定，Build Cache 有波动。
- ✅ 该 PR 属于四层堆栈的一部分：先以行为保持方式建模预渲染候选，再加入 API、复杂路由测试与前台策略测试。

---

### [TanStack Start 安全更新：CVE-2026-102989 | TanStack 博客](https://tanstack.com/blog/tanstack-start-security-update-cve-2026-102989)

**原文标题**: [TanStack Start security update: CVE-2026-102989 | TanStack Blog](https://tanstack.com/blog/tanstack-start-security-update-cve-2026-102989)

TanStack 发布 CVE-2026-102989 安全更新，修复 TanStack Start 服务器函数响应处理中的严重反射型 XSS 漏洞，并建议立即升级和重新部署受影响应用。

- 🚨 该漏洞为严重反射型跨站脚本（XSS），影响 TanStack Start 的服务器函数响应处理。
- ⚠️ 未认证攻击者可构造服务器函数 URL，使应用源返回攻击者控制的 HTML；用户打开链接后，恶意 JavaScript 可能以该用户权限运行。
- 🛠️ 修复措施包括限制客户端输入，并在服务器边界验证响应。
- 📦 受影响版本从 1.143.12 起，至各包首个修复版本之前；修复版本为 @tanstack/react-start 1.168.60、@tanstack/solid-start 1.168.57、@tanstack/vue-start 1.168.56、@tanstack/start-server-core 1.169.39。
- ✅ 需更新 Start 依赖与 lockfile，确认 @tanstack/start-server-core 解析为 1.169.39 或更高，然后重新构建并部署；仅更新本地安装无法修复已部署应用。
- 🧱 边缘缓解措施可在升级期间提供帮助，但不能替代正式修复。
- 🤝 TanStack 已提前私下通知托管商、发行商和合作伙伴，并感谢 Lovable 帮助发现与修复问题。
- 🔗 可通过 GitHub 安全公告查看影响范围、严重性及缓解细节。
- 🧭 页面还展示 TanStack 生态与社区入口，包括 Libraries、Blog、Community、TanChat、Tools、Merch、Support、Partners 等。

---

### [](https://jjenzz.com/making-react-context-cheap/)

**原文标题**: [Making React Context Cheap with React Compiler :: jjenzz](https://jjenzz.com/making-react-context-cheap/)

React Context 在任意值更新时会重渲染所有消费者，社区长期期待 `useContextSelector`；文章通过 5,000 个 radio 的基准测试比较 `useSyncExternalStore` store、Context + `React.memo` 和 React Compiler，发现 React Compiler 能自动记忆化 JSX 与中间值，使普通 Context 消费者达到与专用 store 相近的性能，并建议关注让渲染变便宜，而不只是减少渲染次数。

- ⚠️ 核心问题：React Context 没有内置 selector，任何 context 值变化都会让所有 consumer 重渲染；5,000 个 radio 一次点击可能触发 5,000 次渲染。
- 🕰️ React 曾支持 `calculateChangedBits` / `unstable_observedBits` 做细粒度更新，但在 PR #20953 中移除；Josh Story 于 2019 年提出 context selectors RFC。
- 📘 React 文档推荐模式：外层组件读取 context，把所需值作为 props 传给 `React.memo` 子组件，从而让未变化视图跳过渲染。
- 🧪 基准测试条件：生产构建、5,000 个 radio、Chrome、MacBook Pro M3 Pro，并包含 4× CPU slowdown，使用 p95 计时。
- 📊 点击性能 4× slowdown：`useSyncExternalStore` store 64.9 ms，Context + memoized view 72.6 ms，Context + Compiler 63.6 ms；Compiler 在各列均未落后。
- 🧠 React Compiler 可复用未变化的 JSX，并记忆化组件内中间值，无需额外 view 组件或 selector，就能实现类似细粒度更新的效果。
- 🧵 `useSyncExternalStore` 更适合桥接外部 store，文档建议优先使用内置 state；偏离 React 原语可能失去并发渲染等能力，一些 store 无法中断渲染或在 transition 中分支状态。
- 🛠️ 未使用 Compiler 时，仍可用 `React.memo` 模式；作者演示了 `withContextSelector` 组件工厂封装，但 lint 规则不鼓励组件工厂，未来迁移 Compiler 后需移除。
- 💡 结论：不要只数渲染次数，关键是每次渲染实际做的工作；让渲染变便宜比避免渲染更重要，而 React Compiler 正在帮助实现这一点。

---

### [React 的新浏览器 API：仅在浏览器中渲染组件 - Certificates.dev](https://certificates.dev/blog/reacts-new-browser-api-rendering-components-only-in-the-browser)

**原文标题**: [React's New browser API: Rendering Components Only in the Browser - Certificates.dev](https://certificates.dev/blog/reacts-new-browser-api-rendering-components-only-in-the-browser)

React Canary 新增 `browser` API，配合 `use()` 和 Suspense，让组件跳过服务端渲染、只在浏览器中渲染，从而避免 `localStorage`、`window`、DOM 等浏览器专属值引发的 hydration 不匹配。
- 🌐 SSR 要求服务端 HTML 与首次客户端渲染一致；组件渲染时读取 `localStorage` 或 `window` 会导致服务端失败或 hydration 问题。
- 🧩 `browser()` 从 `react-dom` 导入，必须与 `use()` 搭配使用：`use(browser('原因'))`；单独调用没有效果。
- ⏳ 服务端遇到 `use(browser())` 时会停止渲染该子树，并使用最近的 Suspense fallback；浏览器中则返回 `undefined` 并继续渲染。
- 🚧 Suspense 边界是必需的；浏览器 API 在服务端永远不会可用，没有 fallback 会导致服务端渲染失败。
- 🔍 可选字符串用于说明组件为何需要浏览器，便于在日志中识别有意的浏览器专属渲染。
- 🧱 fallback 会进入初始 HTML 并持续到 hydration，应提供有用状态并预留空间；边界应尽量靠近浏览器专属组件。
- ⚠️ 旧方案有局限：`typeof window` 分支可能造成 hydration 不匹配；`isMounted` + Effect 会增加状态和额外渲染。
- 🧭 与 `'use client'` 不同：`'use client'` 标记客户端组件边界但仍可在服务端出 HTML；`use(browser())` 明确让该子树跳过服务端渲染。
- 💾 典型用例包括：从 `localStorage` 读取草稿、依赖 DOM 的代码编辑器、显示用户时区等浏览器专属数据。
- 🧪 该 API 目前仅在 React Canary/Experimental 中可用；可安装 `react@canary` 和 `react-dom@canary`，并用 `--save-exact` 固定版本。
- ✅ 结论：`browser` API 为首次有意义渲染依赖浏览器状态的组件提供了明确路径；服务端完成其余页面并发送有意 fallback，代价是 hydration 前显示 fallback。

---

### [发布 v8.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v8.0.0)

**原文标题**: [Release v8.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v8.0.0)

Ink v8.0.0 是一次重大版本更新，包含破坏性变更、新功能和大量修复，核心变化包括要求 React 19.3+、调整 `<Box>` 尺寸与流类型、改进输入控制序列处理，并增强滚动、增量渲染和终端兼容性。  
- ⚠️ 破坏性变更：要求 React 19.3+，需升级 `react` 与 `@types/react`。  
- 📏 `<Box>` 的 `minWidth`/`maxWidth` 仅接受数字，百分比字符串不再支持，相对尺寸需自行计算。  
- 🌊 `stdin`/`stdout`/`stderr` 改为通用 Node.js 流类型，TTY 属性如 `stdout.columns` 不再出现在类型中。  
- ⌨️ `useInput` 不再接收未识别终端控制序列，鼠标报告、焦点事件、光标位置报告等会被丢弃。  
- 🧭 新增 `<Box>` 的 `contentOffsetX`/`contentOffsetY`，配合 `overflow="hidden"` 可构建可滚动视图。  
- 📐 `useBoxMetrics()` 和 `measureElement()` 新增 `clientWidth`/`clientHeight`，表示不含边框的内容区域尺寸。  
- 🔌 `render()` 的 `stdin`/`stdout`/`stderr` 可接受任意 Node.js 流，如 `PassThrough`、`Readable`、`Writable`。  
- ⚡ `incrementalRendering` 会跳过未变化的行前缀，仅写入变化部分，减少输出和闪烁。  
- 🌐 React DevTools 改用原生 `WebSocket`，移除 `ws`；应用小键盘 Enter 识别为 `key.return`。  
- 🛠️ 修复大量渲染、清屏、scrollback、`<Static>`、文本换行/截断/样式、输入解析、焦点和屏幕阅读器输出问题。  
- 📘 迁移指南：升级 React 19.3+；`minWidth/maxWidth` 用数字；用 `useWindowSize()` 替代 `stdout.columns`；`useInput` 不再解析鼠标报告等控制序列。

---

### [发布 streamdown@2.7.0 · vercel/streamdown · GitHub](https://github.com/vercel/streamdown/releases/tag/streamdown%402.7.0)

**原文标题**: [Release streamdown@2.7.0 · vercel/streamdown · GitHub](https://github.com/vercel/streamdown/releases/tag/streamdown%402.7.0)

streamdown@2.7.0 发布，重点提升流式渲染速度，并新增 fallbackComponent、disableAutolinkProtocols、portal、defaultComponents 导出等能力；同时修复 Mermaid、数学公式、代码块按钮、列表与 CJK 链接等问题，remend 1.4.0 也同步更新。

- 🚀 版本信息：streamdown@2.7.0 为最新版本，9 月 30 日发布，包含 5 个提交，主要围绕流式速度、新 props 与大量修复。
- ⚡ 性能提升：代码块只高亮新增行，复用已解析块且只对块 token 做词法分析；代码/表格自动滚动每帧一次；光标显隐不再重排全文；高亮缓存改为 LRU 有界；Mermaid 流式围栏逐个渲染，避免阻塞。
- ✨ 新增能力：加入 fallbackComponent、disableAutolinkProtocols、portal 等 props；导出 defaultComponents；默认代码与 Mermaid 复制按钮支持 onCopy/onError。
- 🖼️ 流式占位：不完整图片显示加载骨架，而不是直接消失。
- 🐛 关键修复：Mermaid 图自适应容器且文字可读；数学公式中的 `<` 不再截断后续内容；嵌套滚动容器中代码块按钮可点击；表格复制/下载为 Markdown 时保留 HTML 标签与实体；松散列表项不再多出间距；CJK 全角标点后的裸 URL 可再次链接化。
- 🧩 remend 1.4.0：新增单遍扫描器，支持 `~~~`、引用/列表中的围栏、CRLF、多反引号 span；修复大量分隔符导致的二次复杂度、`snake__case` 假强调，并使 healing 幂等。
- ⚠️ 兼容提醒：@streamdown/code@2.0.0 迁移到 Shiki v4，需 Node 20 或更高；marked 升级到 v18。
- 📦 解析调整：marked v18 改变了空白 token 行为，parseMarkdownIntoBlocks 现在将 space token 折叠进前一块，保持块边界与 v17 一致。

---

### [](https://github.com/JoviDeCroock/stableref/releases/tag/v0.2.0)

**原文标题**: [Release v0.2.0 · JoviDeCroock/stableref · GitHub](https://github.com/JoviDeCroock/stableref/releases/tag/v0.2.0)

stableref v0.2.0 发布说明概述：这是最新版本，核心是导出 React 原生 useSyncExternalStore、增强严格 React/Preact hooks 的类型契约，并补充 React Compiler、快照缓存与水合等文档。

- 🚀 v0.2.0 为 Latest 版本，发布于 10 月 02 日 04:28，自该版本以来 main 有 1 次提交；发布标记为 Immutable。
- 📦 Minor #12：导出 React 原生 useSyncExternalStore hook，提供 branded 快照结果和稳定订阅契约，并记录快照缓存与水合义务。
- 🧩 Patch c687189：说明 stableref 的类型级稳定性契约如何与 React Compiler 优化、hook 识别和穷举依赖 lint 交互。
- 🛡️ Patch #4：支持 strict React/Preact 的 useMemo<T>、useCallback<F>、useImperativeHandle<T,R> 使用普通显式类型参数，依赖类型默认设为 StableDeps；显式调用仍拒绝未证明的引用依赖，并给出 StableDependency 诊断。
- ♻️ Patch #4 续：推断调用保留原有可操作依赖诊断，hook 身份与稳定性 branding 不变。
- 🧷 Patch #5：在 React 18 声明中保留可变初始化 ref 与精确 current-value 类型，同时兼容 React 19，且仅对 ref 容器进行 branding。
- ✅ Patch #10：strict React/Preact 的 effect 和 imperative handle hooks 可接受可选稳定依赖列表，同时继续拒绝未证明的引用依赖。
- 📝 贡献者：@JoviDeCroock、@ayden94；发布资源共 3 个。

---

### [](https://github.com/posva/medula)

**原文标题**: [GitHub - posva/medula: 🧬 devtools for agents · GitHub](https://github.com/posva/medula)

medula 是面向 AI 编码代理的无头开发工具，通过 MCP 让代理检查并修改正在运行的 Web 应用内部状态，适合在生产问题修复后验证，或探索难以用自动化测试复现的边界情况。

- 🧬 支持 Vue 3、React、Svelte 5、Solid 1.9 / 2 RC，并通过 devframe 连接应用与代理。
- 🔍 Vue 3 可检查组件树、读写组件状态与 Pinia store，并通过 Vue Router 导航。
- ⚛️ React 可检查组件、读写 hook 状态、覆盖 props；Svelte 5 可读 props 和派生值、编辑 `$state`。
- 🧩 Solid 可检查组件、读 props 和 memos、编辑 signals 与 stores。
- 📦 Vite 集成：安装 `medula` 和 `@vitejs/devtools`，启用 `devtools`，并在框架插件旁添加 `medula()`。
- 🟢 Nuxt 集成：安装 `medula`，要求 Nuxt DevTools 4，并在 `modules` 中加入 `'medula/nuxt'`。
- ▲ Next.js App Router 集成：安装 medula 与 devframe 包，用 `withDevframe` 包装配置，创建 `app/%5F_devframes/[[...path]]/route.ts`，并在根布局加入 `<Medula />` 和开发脚本。
- 🔌 连接代理：在 MCP 配置中加入 `npx devframe connect`，它会发现运行中的开发服务器并用端口选择应用。
- 🧪 使用时启动开发服务器并在浏览器保持应用页面打开，即可让代理查看组件状态、修改状态、打开路由等。
- 🛡️ 代理可调用 `medula_help`；改动只影响运行页面，不会编辑源文件。
- 📄 项目采用 MIT 许可证，贡献说明见 `CONTRIBUTING.md`；仓库有 91 stars、0 forks、0 watchers、71 commits。

---

### [Shaders 现已开源 — Shaders](https://shaders.com/updates/shaders-is-open-source)

**原文标题**: [Shaders is now open source — Shaders](https://shaders.com/updates/shaders-is-open-source)

overview summary  
Shaders 宣布其渲染引擎、所有着色器组件和框架绑定以 MIT 许可证开源，旨在让设计工程师更轻松地创建和发布创意 WebGPU 效果，同时保留 Pro 订阅的高级资源、效率和支持。

- 🚀 2026年10月6日起，Shaders 渲染引擎、全部 shader 组件与框架绑定正式开源，采用 MIT 许可证。
- ✨ 初衷是让设计工程师无需成为图形程序员，也能使用创意 shader 效果；AI 时代开放基础更具价值。
- 🧱 开发者可基于生产级组件和高度优化的 WebGPU 运行时构建，而不必从原始 shader 代码开始。
- 🆓 组件可用于个人、商业客户项目、SaaS 产品和内部工具，无需额外许可证。
- 🎨 可从设计编辑器免费导出代码，设计 shader 后即可发布，无限制。
- 🧩 defineShader 语言已公开并附文档；可编写自定义组件（实验性），也可提交 PR 贡献。
- ⭐ Shaders Pro 仍是发现、定制和发布精美 WebGPU 效果的最快方式。
- 💎 Pro 订阅权益保留：1000+ 预设、55+ 预制区块、无水印渲染视频与图片、独家 Discord 角色与频道、优先支持。
- 💰 Pro 价格不变；过去 30 天因商业用途或代码导出购买 Pro 若受影响可联系团队；早前购买 Core 订阅者将免费获得 Pro 权益。
- 💬 欢迎通过 Discord 交流，创始人 Simon 感谢社区参与并期待社区推动项目发展。

---

### [](https://github.com/pmndrs/klipp)

**原文标题**: [GitHub - pmndrs/klipp: 📹 A camera toolkit for the web, inspired by Unity Cinemachine. · GitHub](https://github.com/pmndrs/klipp)

Klipp 是 pmndrs 旗下一款面向 Web 的摄像机工具包，灵感来自 Unity Cinemachine，可通过描述镜头来自动选择并混合合适视角，目前处于早期实验阶段。

- 📹 Klipp 是 Web 相机工具包，灵感来自 Unity Cinemachine，能描述镜头、自动选择并混合镜头。
- 🧩 核心不绑定渲染器或框架，可独立运行；目前提供 three.js 和 React Three Fiber 集成，未来计划支持 TresJS。
- 📦 通过 npm 安装：`npm install @kvvasuu/klipp`，提供核心、three、react、dom 等入口。
- 🎥 支持带优先级的虚拟相机、镜头混合、Body/Aim 跟随与注视、环绕观察、Extension/Noise/Impulse 构图与抖动。
- 🐞 提供调试功能：取景区域、相机视锥体；DOM 入口支持鼠标、触摸、滚轮输入和调试覆盖层。
- ⚠️ 项目仍属早期实验阶段，API 可能变化；仓库采用 MIT 许可证。
- 📊 仓库数据：约 24 stars、0 forks、0 watchers、396 commits。
- 🔗 文档与示例：pmndrs.github.io/klipp/examples。

---

### [](https://sentry.io/resources/agent-tracing-series/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=agenttracing-fy27q3-agenttracingseries&utm_content=newsletter-secondary-workshop-2-register)

**原文标题**: [Debugging agents in different environments | Sentry](https://sentry.io/resources/agent-tracing-series/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=agenttracing-fy27q3-agenttracingseries&utm_content=newsletter-secondary-workshop-2-register)

这是一场由 Sentry 主办的两部分工作坊系列，主题是使用 Sentry Agent Tracing 来理解和调试 AI 代理；内容涵盖 trace/span 基础、不同环境中的代理调试，以及 Sentry 在生产中调试自有 AI 代理的实践。

- 🧭 当 AI 代理回答不佳、调用错误工具或响应过慢时，需要追踪其执行过程来定位问题。
- 🛠️ 两部分工作坊由 Serge 和 Ryan 主讲，展示如何用 Sentry Agent Tracing 理解和调试代理。
- 📅 第一场 10 月 7 日：调试不同环境中的代理，包括电商聊天机器人、Slack 代理和 GitHub Actions 中的 PR 审查代理。
- 🔍 第一场从 trace 和 span 基础讲起，通过实时演示跟随代理执行、检查模型与工具调用并找出出错点；无需追踪经验。
- 🛒 学习为电商聊天机器人、自定义 Slack 代理和 GitHub Actions 中的 PR 审查代理添加代理追踪。
- 📊 检查输入、输出、工具调用和 token 使用量，以调查错误和慢响应。
- 🧪 第二场 10 月 14 日：Sentry 如何调试自己的 AI 代理，介绍其工程师在生产中使用 Agent Tracing 的方法。
- 📈 内容包括收集 trace、调查代理行为，并在海量生产 trace 中找出值得排查的失败。
- 🚨 团队利用用户沮丧等信号，在大规模场景中发现代理问题。
- 🎙️ 还推荐收听 Syntax Podcast，可在常用平台收听。

---

### [](https://www.youtube.com/watch?v=L-PNQi1nBSA)

**原文标题**: [Hello Graphite - YouTube](https://www.youtube.com/watch?v=L-PNQi1nBSA)

该文本是 YouTube 页脚导航与版权信息，主要列出平台相关入口、政策条款、功能测试及 Google 版权声明。

- 📄 关于
- 📰 新闻
- ©️ 版权
- 📞 联系我们
- 🎬 创作者
- 📢 广告
- 👨‍💻 开发者
- 📜 条款
- 🔒 隐私
- 🛡️ 政策与安全
- ⚙️ YouTube 如何运作
- 🧪 测试新功能
- © 2026 Google LLC

---

### [](https://posthog.com/blog/why-we-rebuilt-our-data-warehouse?utm_source=twir&utm_campaign=oct7)

**原文标题**: [Why we rebuilt our data warehouse and how it unlocks self-driving products](https://posthog.com/blog/why-we-rebuilt-our-data-warehouse?utm_source=twir&utm_campaign=oct7)

PostHog 将数据仓库从 ClickHouse 重建到 DuckDB：原有方案适合早期公司，但当公司扩张并聘请数据工程师后，ClickHouse 的多租户限制、通用仓库能力不足和数据工具生态欠缺，导致数据被导出到外部仓库；新架构用单租户 DuckDB、Postgres 协议端点、DuckHog 与 DuckLake，把 PostHog 事件和外部数据统一成 AI 代理可用的上下文层。

- 🎯 原目标：让公司尽可能晚聘首位数据工程师，无需六个月数据基建即可做仪表盘和业务分析。
- 📈 成长瓶颈：公司达到 30–50 人后数据问题变复杂，数据工程师无法在 PostHog 内完成需求，开始导出数据，PostHog 沦为中间件。
- 🏢 挑战 1 多租户：共享 ClickHouse 集群适合浏览器内较快查询，不适合运行数小时或数天的建模查询，节点重启和无限查询会影响整个应用。
- 🧮 挑战 2 ClickHouse 作查询引擎：它擅长大规模事件分析，但作为通用仓库有短板：缺少基于成本的优化器、S3/Delta/Iceberg 支持成熟慢、跨版本查询结果可能不一致。
- 🛠️ 挑战 3 数据工具：难以接入 dbt 等成熟工具，无法直接暴露 ClickHouse 连接，HogQL 生态有限，复杂数据团队缺乏长期信心。
- 🦆 DuckDB 重建：每个组织使用独立单租户 DuckDB 实例，生命周期服务空闲休眠、查询唤醒，并提供 Postgres Wire 协议端点兼容现代数据工具。
- 🔌 DuckHog 与 DuckLake：DuckHog 支持本地拉取数据子集并用 DuckDB、pandas、polars 处理再写回；DuckLake 将存储与计算分离，数据存 S3，避免锁定 DuckDB。
- 📦 数据统一：PostHog 事件数据已按组织镜像到 S3，Stripe、Postgres 等外部数据源也可进入同一仓库，无需额外搭建管道。
- 🤖 代理上下文：统一仓库成为 AI 代理的上下文层，让代理基于完整可信数据给出收入影响、受影响群组和修复方案。
- 🚀 下一步：Managed Warehouse beta 可加入等待名单；PostHog 定位为产品上下文层，整合分析、会话回放、功能开关、实验、错误跟踪、日志和 CDP。

---

### [为什么 Shopify 放弃了 React Native？—— 作者：Gergely Orosz](https://newsletter.pragmaticengineer.com/p/shopify-native-mobile)

**原文标题**: [Why has Shopify dropped React Native? - by Gergely Orosz](https://newsletter.pragmaticengineer.com/p/shopify-native-mobile)

Shopify 曾在2020年为了更快推出 Android 版、共享 iOS/Android 代码而全面采用 React Native，并在五年内迁移六款应用、取得良好效果；但到2026年，其宣布转向原生开发，核心原因是 AI 编码代理已能高效编写、移植、测试 Swift/Kotlin，削弱了跨平台共享实现的主要优势。Shop 应用已在12周内重写为全原生，Shopify 计划用 AI 将其余应用迁移到 Swift/Kotlin，同时继续强调性能、稳定性和质量。

- 🏬 2020年 Shopify 选择 React Native：移动端销售占比高，Android 原生开发慢，希望一套代码覆盖 iOS/Android、提升人才流动和交付速度。
- 📱 2018年 Shop/Arrive 先用 RN 成功上线 Android，共享约95%代码，减少崩溃；2025年总结称五年迁移六款应用成功。
- 🤖 2026年宣布“原生才是未来”：AI 代理大幅提升 Swift/Kotlin 编码、翻译、测试和审查能力，构建双平台不再像过去那样昂贵。
- ⚡ 原生优势：更贴近平台能力与一方工具，减少框架和依赖层，可完全控制渲染栈，性能和架构优化空间更大。
- 🛠️ RN 痛点仍在：调试不稳定、需原生代码处理高性能/动画/后台任务/特殊 API、依赖更多第三方库。
- 🚀 Shop 应用用 AI 仅12周完成全原生重写；Shopify 应用进行中，其余应用将陆续迁移到 Swift 和 Kotlin。
- 🧪 共享验证测试套件：同一业务逻辑在 Swift/Kotlin 上通过完全相同测试，否则不能发布；桌面无头运行给代理快速反馈。
- 👩‍💻 AI 让一名工程师可跨 iOS/Android 开发，替代 RN 的“共享语言”优势；代理也擅长跨平台移植功能、比较实现并找差距。
- 📊 New Architecture 迁移带来 modest 性能提升：Android 启动约快10%，iOS 约快3%，部分复杂页面调优前反而更慢。
- 🕰️ 类似反复：Airbnb 2016年采用 RN，两年后因性能回归原生；Notion 原生迁移已持续七年。
- 🌍 Kotlin Multiplatform 仍相关：可共享业务逻辑，同时各平台保持原生，未来可能因 AI 更受欢迎。
- 🔮 结论：原生与 RN/Flutter/KMP 都因 AI 更易开发，但 Shopify 认为代理降低了共享实现优势，而原生保留平台控制优势。

---

### [TypeScript 中的原生视图：来自 Lucent 的 SwiftUI 和 Jetpack Compose | Lucent](https://www.lucent-lang.dev/blog/native-views/)

**原文标题**: [Native views in TypeScript: SwiftUI and Jetpack Compose from Lucent | Lucent](https://www.lucent-lang.dev/blog/native-views/)

Lucent 推出了一项实验性功能，允许开发者用 TypeScript 编写原生视图，通过一个 `.lucent.tsx` 文件同时为 iOS 渲染 SwiftUI、为 Android 渲染 Jetpack Compose，并由 React 统一导入使用。该功能目前仍处于极早期阶段，API 随时可能变动，官方明确警告不要用于生产环境。编译器会将 JSX 视图体转换为 Swift 或 Kotlin 源码，将逻辑（信号、事件处理、效果等）编译为 C++ 并在主线程运行，两者通过可观察状态衔接。视图相关声明直接从已安装的 Xcode SDK 和 Compose 库的 Kotlin 元数据中生成，保证使用平台真实的 API 与参数名。UI 在主线程运行，不会等待 JavaScript，因此即使 JS 被长时间阻塞，原生动画依然流畅。

- ⚠️ 极度早期且实验性：语言、生成的原生代码和包 API 都可能随时变更，禁止用于生产环境
- 🧩 一份组件文件即可为每个平台编写各自原生 UI，通过 `PLATFORM` 变量选择 iOS（SwiftUI）或 Android（Jetpack Compose）分支
- 🔄 React 只需导入一次组件即可使用，无需编写任何 Swift 或 Kotlin 代码，也没有共享组件词汇的妥协
- ⚙️ 编译器将组件拆分为两部分：视图体转成 Swift `View` 或 Kotlin `@Composable`，逻辑编译为 C++ 并在主线程运行
- 🌉 逻辑与视图通过可观察状态衔接：如 `liked.get()` 推送到 Swift 的 `@Published` 或 Compose 的快照状态，`toggle` 等函数更新状态后由平台自行 diff、动画和布局
- 📐 SwiftUI 属性规则简单：与初始化参数同名的作为参数，其余按书写顺序作为修饰符；修饰符可链式调用
- 🧱 Compose 中需在组合期间运行的调用（如 `animateFloatAsState`、`remember`、`LaunchedEffect`）会被编译器识别并移入生成的可组合函数
- 📚 `lucent:swiftui` 和 `lucent:compose` 分别从已安装的 Xcode 与 Compose 库元数据生成，API 可用性取决于 SDK 是否声明，无法表达的 API 会附带原因
- 🚀 UI 运行于主线程且不等待 JavaScript：测试中 3 秒 JS 阻塞期间，原生计时器仍能持续翻转和动画
- 🧰 事件、命令、带返回值请求、视图回收、按内容尺寸布局以及原生容器中的 React 子元素在两端均可用
- 🔒 视图默认关闭，需设置 `LUCENT_VIEWS=fabric` 启用；后续计划包括真机测试、性能预算和更多工具包支持

---

### [](https://expo.dev/blog/live-activities-with-expo-end-to-end-client-and-backend)

**原文标题**: [Live Activities with Expo, End to End: Client and Backend â Expo blog](https://expo.dev/blog/live-activities-with-expo-end-to-end-client-and-backend)

当前未检测到需要总结的文本内容，因此无法提炼文章要点。
- 📭 输入内容为空，无法识别文章主题或关键信息。
- 📝 请提供具体文本，我会按“概述 + 要点”格式生成中文摘要。
- ✅ 收到内容后，我会为每条要点配上合适 emoji，并保持简洁准确。

---

### [](https://www.callstack.com/blog/introducing-mobile-dev-full-mobile-dev-tooling-right-in-your-codex-app)

**原文标题**: [Introducing Mobile Dev for Codex](https://www.callstack.com/blog/introducing-mobile-dev-full-mobile-dev-tooling-right-in-your-codex-app)

Callstack 发布 Codex 的 Mobile Dev 初始预览，将移动端开发、调试、日志与性能分析工具直接集成到 Codex 应用，并让 AI agent 能与开发者一起操作设备与应用。
- 📱 Codex 现已支持内嵌交互界面的插件，Mobile Dev 借此把设备预览、反馈、日志和性能分析带入同一工作区。
- 🛠️ 支持 Expo、React Native、SwiftUI 及其他原生移动项目，并内置 agent-device 支持，便于 agent 与开发者协同。
- 👀 可在聊天旁串流 iOS 模拟器、Android 模拟器和已连接的 iPhone、iPad、Android 设备，也支持 iOS/Android 并排全屏预览。
- 🎮 支持选择与启动模拟器/仿真器、点击拖拽、输入文字；Codex 可通过 MCP 工具检查无障碍元素并控制应用，还可对元素或屏幕区域标注并留言。
- 📜 统一查看 iOS 统一日志、Android logcat 和 Metro 控制台消息，支持跟随前台应用、搜索过滤，并把错误及堆栈发送到聊天。
- 📈 可监控应用 CPU、内存、线程图表和 Display FPS；让 Codex 录制交互、在聊天中查看图表、比较运行、分析区间，并叠加基线与更新录制；Android 录制还包含帧节奏与卡顿统计。
- 🧩 构建在 MCP、MCP Apps 和 OpenAI 扩展之上，提供侧边栏视图与对话面板等集成点；先面向 Codex 桌面端，底层工具仍可通过 MCP 使用。
- 🚀 预览版已可通过 GitHub 安装说明获取，即将登陆 Codex marketplace；打开 Codex 新聊天后从侧边栏启动 Mobile Dev、选择设备并按项目流程运行应用。
- 🔮 团队将持续扩展移动开发、调试与审查能力，目标是在 agent 工作流中打造完整的移动开发工作区。

---

### [Codemagic Patch | 适用于 React Native 的自托管 OTA 更新](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

**原文标题**: [Codemagic Patch | Self-hosted OTA updates for React Native](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

Patch 是面向 React Native 的自托管 OTA 更新方案，主打快速部署、完整更新控制与低成本扩展，可服务从少量到数百万用户，并降低不兼容发布风险。

- 🚀 自托管 OTA：为 React Native 提供高效架构的空中更新，适合大规模用户。
- ⚙️ 20 分钟安装：一条 `cmpatch selfhost install` 启动向导，自动配置 OAuth、CDN 缓存规则、TLS，并用 Docker Compose 启动服务。
- 💰 现代 OTA 功能：具备托管 OTA 服务的完整能力，同时避免高额费用。
- 🛡️ 防止不兼容发布：通过 fingerprinting 检查目标原生二进制，阻止不兼容版本发布。
- 📦 小体积差分更新：设备只下载二进制 diff 中变化的部分，不依赖优质移动信号。
- 📊 发布与监控：仪表板提供发布指标、安装监控、rollout 和 rollback 控制。
- ☁️ 高扩展性：设备向 CDN 发起检查和下载请求，服务器不会因用户量过大而过载。
- 🔍 对比优势：Patch 的检查与下载随 CDN 扩展，仅 CDN 故障才停机；支持 fingerprinting、bundle diff、立即/重启/恢复/暂停安装、仪表板与 CLI、团队 Web 仪表板、RBAC 和支持许可。
- 🏢 Codemagic 背景：Codemagic 有 10 年以上移动 CI/CD 经验，已交付数十亿次生产 OTA 更新，并将经验带入自托管 Patch 堆栈。

---

### [](https://stim.appandflow.com/docs/desktop)

**原文标题**: [Stim Desktop | Stim](https://stim.appandflow.com/docs/desktop)

Stim Desktop 是 macOS 上用于观察和操控 Stim 工作流的应用，集中展示工作区、实时模拟器/仿真器、构建、日志以及驱动它们的代理，并代表你运行 stim CLI。它支持下载、远程 iOS、回放、日志、构建详情、机器管理、手机配对与首次设置，同时保持后台通知和手机服务运行。

- 🖥️ 安装与要求：下载 Stim.dmg 拖入 Applications，或用 Homebrew 安装；需 macOS 14 或更高版本，支持 Apple silicon 或 Intel。
- ⚙️ CLI 配置：stim CLI 需在登录 shell 的 PATH 中，或在 Stim > Settings > App 指定；Desktop 使用 STIM_HOME、登录 shell 值或 ~/.stim。
- 📱 远程 iOS：用 stim ios --remote <machine> 启动的托管模拟器会显示为设备块并标注 on <machine>；开启 Serve to phones 可经 stim-server 中继查看和控制。
- 🧩 工作区视图：每个工作区显示阶段、设备、分支和 PR 状态；同一 linked worktree 中的应用共享详情页和侧边栏行，并带平台徽章。
- 🎛️ 设备控制：打开设备查看大屏、用鼠标键盘接管，并查看代理操作和时间；本地 iOS 输入在后台连接，失败时最多等待 10 秒并保持响应。
- ⏪ 回放：可回滚设备最近屏幕，时间线标记代理操作和错误；需要开启 Serve to phones。
- 🎚️ 模拟器选项：控制本地运行中 iOS 模拟器时，可改外观、文字大小、对比度、动态、透明度、按钮边框等；需 Xcode 模拟器外观 API。
- 📜 日志：Metro 与 App/native inspector 共用查看器，支持来源筛选、可编辑过滤器、重复错误分组，以及 Readable/Raw 输出切换。
- 🏗️ 构建：检查器卡片显示进度和上次/下次构建摘要；详情表含平台切换、历史、耗时估算、阶段、缓存、诊断、输出和下次构建计划。
- 💾 存储：Storage 页报告 agent-device runner 构建、会话和日志，以及用户级 SwiftPM 缓存；仅报告，Stim 不提供清理动作。
- 🖧 机器：可选择 This Mac 或配置的构建机器，查看就绪、容量和构建历史；支持安装本机构建并经 tailnet 更新，无需 ssh。
- 🔀 工作区变更：点击 Git chip 的 Review changes 浏览 staged、unstaged 和新文件；可用内置查看器或 VS Code 打开，有 200 文件和 256 KiB 预览限制。
- 📞 手机：配对 Stim 手机应用后，可观看租用手机；Android 可控，USB iPhone 只读。手机端按 linked checkout 分组项目，并显示设备、构建、日志和命令。
- 🔔 通知与清理：卡住代理和持续失败构建会告警，PR 合并后自动移除 worktree；Needs you 只列代理无法处理项，默认静默，收件箱分批加载。
- 📐 布局：工作区设备卡片自适应宽度至 640 点并居中换行；屏幕保持比例，高度上限 900 点；停止设备用紧凑卡片。
- ▶️ 启动与控制：Boot 会通过 Stim 构建并启动；Control 用于可控设备，View 用于其他情况；物理 iOS 设备和远程预览只读，Android 手机需有效租约。
- 🖼️ 设备边框：本地模拟器/仿真器可显示设备边框；Apple 用 DeviceKit，Android 用 AVD 皮肤或硬件配置；缺图或不受支持时保持无边框。
- 🔍 缩放：缩放菜单默认 Fit，另有 Point Accurate、Pixel Accurate、Physical Size；多显示器切换会更新，Duo 等部分预览保持 Fit。
- 🤏 手势与剪贴板：控制本地 iOS/Android 时，Option 拖拽可双指捏合/旋转，Option-Shift 平移；可粘贴 Mac 文本到设备，或复制设备剪贴板。
- 🧭 界面行为：关闭窗口后 Stim Desktop 仍在后台运行，Dock 图标可重开，Command-Q 退出；Command-1/2/3 切换 All devices、Notifications、Machine。
- 🔄 更新与隐私：每日检查 npm 上的 stim 更新，仅当由 npm/pnpm/bun 安装且较旧时提示，从不自动更新；发布版崩溃报告会移除路径、主机名、地址和凭据，不发送截图或性能追踪。
- 🚀 首次设置：首次启动引导安装 stim CLI 和 agent skill、请求通知权限、可选开启 Serve to phones 并配对手机，并检查 Xcode、Android SDK 和项目 stim doctor。
- 🧪 贡献者：DEBUG 构建提供 Window > SwiftUI Playground，可运行 swift run StimDesktop --playground，检查加载、空、错误、长文本和大数据等状态与布局。

---

### [](https://github.com/JoaoPauloCMarra/react-native-nitro-markdown/releases/tag/v0.14.0)

**原文标题**: [Release v0.14.0 · JoaoPauloCMarra/react-native-nitro-markdown · GitHub](https://github.com/JoaoPauloCMarra/react-native-nitro-markdown/releases/tag/v0.14.0)

react-native-nitro-markdown 发布 v0.14.0，包含一项破坏性变更和一项流式状态修复，主要影响图片主机白名单策略以及 MarkdownStream / useMarkdownStreamState 会话切换时的数据隔离。

- 🚀 发布 v0.14.0 最新版本，时间为 10 月 3 日 21:56，提交 a20892b 已通过 GitHub 验证签名。
- ⚠️ 破坏性变更：`imageOptions.allowedHosts: []` 现在会拒绝所有图片主机，而不是禁用允许列表。
- 🔧 迁移方式：省略 `allowedHosts` 以保留默认主机策略，或提供图片可使用的具体主机名；协议限制仍然适用。
- 🐛 修复：将 `MarkdownStream` 或 `useMarkdownStreamState` 切换到另一个会话时，新会话初始化期间不再暴露上一会话的文本或 AST。
- 🧹 旧订阅排队的工作不能替换新会话的状态。
- 📦 该发布包含 2 个资产。

---

### [Maestro CLI 2.11.0：在 Android 17 上进行测试](https://maestro.dev/blog/maestro-cli-2-11-0)

**原文标题**: [Maestro CLI 2.11.0: test on Android 17](https://maestro.dev/blog/maestro-cli-2-11-0)

Maestro CLI 2.11.0 于 2026 年 10 月 1 日发布，核心是支持 Android 17（API 37）在本地和 Maestro Cloud 上测试，并修复云视频回放、Windows 上传及调整部分 YAML 行为。

- 📱 现已支持 Android 17（API 37），可在本地和 Maestro Cloud 上运行测试。
- 🖥️ 本地运行：`maestro start-device --platform android --device-os android-37.1` 即可使用；Google 改为发布带小版本号、仅 16 KB 页面大小的系统镜像，Maestro 会自动查找正确镜像或提示需使用的确切 `--device-os`。
- ☁️ 云设备：`android-37.1` 已上线 pixel_2、pixel_6、pixel_6_stock、pixel_9、pixel_9_pro_xl 和 pixel_tablet；使用 `maestro cloud --device-os android-37.1`，需先更新到 2.11.0。
- 🎬 云视频拖动定位可高亮正确步骤：屏幕录制会在产物清单中记录真实开始时间，使视频与 `commands.json` 对齐，无需时间偏移；Web 录制也按真实速度回放。
- 🪟 Windows 上传修复：当流程使用带复杂路径的 `runFlow` 时，`maestro cloud <flow.yaml>` 可正常上传。
- 📵 已连接的真实 iPhone 不再列为设备；若指定真实 iOS 设备会立即退出并提示“Physical iOS devices are not yet supported”。目前支持 iOS 模拟器。
- ⚙️ YAML 行为变更一：`optional: true` 现在适用于 `setDarkMode` 和 `setAirplaneMode`，无法执行的步骤会跳过并继续；两者只接受 `enabled` 或 `disabled`，拼写错误会在解析时报错。
- ⚠️ YAML 行为变更二：元素选择器中的 `start` 和 `end` 被拒绝；它们属于 `swipe`，之前在其他操作中被静默忽略，需从 `tapOn` 等中移除。
- 🧑‍💻 包含这些改动的 Maestro Studio 版本将随后发布。
- ⬆️ 更新方式：运行 `curl -fsSL "https://get.maestro.mobile.dev" | bash`，或按更新指南操作 macOS、Windows 和 Homebrew。

---

### [](https://github.com/jpudysz/react-native-unistyles/releases/tag/v3.5.0)

**原文标题**: [Release Release v3.5.0 · jpudysz/react-native-unistyles · GitHub](https://github.com/jpudysz/react-native-unistyles/releases/tag/v3.5.0)

react-native-unistyles v3.5.0 是一个稳定性版本，重点修复主题与样式同步、冻结屏幕、内存与重载、构建兼容、类型和性能问题，并更新内部测试与文档。

- 🎨 修复重新渲染后主题更新未应用到部分动态样式的问题。
- 🔄 Unistyles 提交不再覆盖 React 刚渲染的内容，修复 `updateTheme` 丢失和内联 props 被丢弃。
- 🌈 修复 `Animated` 视图、动画变体、`TouchableHighlight` 等主题色陈旧或不一致问题。
- 📐 `ActivityIndicator` 样式现在与包裹它的 `View` 关联。
- 🧭 `useUnistyles`、`withUnistyles`、`Display`、`Hide` 重新响应屏幕方向变化。
- 🧊 解冻冻结屏幕时不再长时间阻塞 JS，恢复挂起节点更高效。
- 🧠 修复 `StyleSheet` ↔ `Unistyle` 引用循环导致的重载内存泄漏。
- ♻️ 运行时所有权改用代际追踪，避免 OTA 或开发重载后旧运行时清除新状态。
- 🌐 Web 端释放 `Pressable` 和 `ScrollView`，避免 CSS 规则与 DOM 节点累积。
- 🛠 修复旧版 React Native 的构建错误，并兼容 AGP 9 内置 Kotlin 扩展。
- 🧾 类型改进：嵌套样式和输出侧支持只读数组。
- ⚡ 性能优化：加快链接路径上的 unistyles 查找。
- 🧪 内部更新：新增带 C++ 诊断的 e2e 测试套件，并刷新文档。
- ❤️ 感谢 @dennytosp、@gabrieldonadel、@christianjuth、@safaiyeh 等贡献者。

---

### [](https://reactnativefeel.com/deploy)

**原文标题**: [React Native Deploy — unlimited free EAS-compatible builds on GitHub](https://reactnativefeel.com/deploy)

尚未收到需要总结的文本内容，因此无法生成摘要。请提供文章或原文内容。

- 📄 当前输入为空
- 📝 无法提取关键信息或要点
- 📌 请粘贴原文后，我将按模板生成中文摘要

---

### [](https://swmansion.com/changelog/react-native-enriched-markdown-1-1-0/)

**原文标题**: [React Native Enriched Markdown 1.1.0 | Software Mansion](https://swmansion.com/changelog/react-native-enriched-markdown-1-1-0/)

React Native Enriched Markdown 1.1.0 于 2026 年 10 月 1 日发布，带来 Notion 风格输入、原生视频渲染、GitHub 提示框、块引用嵌套等多项新功能，并包含大量错误修复与性能提升；同页还列出后续补丁与历史版本更新。

- 🎃 1.1.0 为小版本更新，主打多项新特性与体验改进。
- ⌨️ 支持 Notion 风格输入快捷方式：无需工具栏或菜单，输入前缀即可继续编辑。
- 🎬 支持原生视频渲染：Markdown 中的 video 标签会变成真实播放器，无需额外依赖。
- 💬 支持 GitHub admonitions：五种 `> [!NOTE]` 提示框类型，均可自定义主题。
- 🧱 块引用原生渲染为容器，可嵌套其他块元素，并更贴近 CommonMark 规范。
- ✂️ 新增 numberOfLines + ellipsizeMode，可按指定行数截断 Markdown，适合摘要和描述；目前仅支持 CommonMark。
- 🔄 preserveBlankLines 标志让 EnrichedMarkdownText 与 EnrichedMarkdownTextInput 逐行同步，适合就地编辑消息流。
- 🖱️ 新增 onImagePress、onCodeBlockPress、onLatexError 回调，便于维护应用状态和实现特殊交互。
- 🚫 可禁用块上下文菜单，使 Android 与 iOS 行为更一致。
- 🔗 支持按链接变体设置字体，进一步自定义不同链接样式。
- 🐛 包含多项错误修复和性能改进，可查看完整发布说明。
- 📦 其他版本：1.1.1 修复上一版引入的问题并提升性能；1.0.2 支持从 package.json 读取 feature flags，修复 Windows Expo、monorepo 和字体缩放；1.0.1 将包体积降至几 MB；1.0.0 为首个稳定版，支持 GFM 代码块与 tree-sitter 语法高亮。

---

### [](https://github.com/getsentry/sentry-react-native/releases/tag/8.29.0)

**原文标题**: [Release 8.29.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.29.0)

sentry-react-native 8.29.0 已发布，重点新增移动回放 trace ID 搜索与 React Native Swift Package Manager 集成支持，并带来多项 iOS、Android、Expo 与回放相关修复，同时升级 Android 和 Cocoa SDK 依赖。

- 🚀 发布：8.29.0（Latest，提交 7d4150b）由 sentry-release-bot 于 10 月 1 日发布。
- 🔍 新功能：移动回放填充 `trace_ids`，支持按 trace ID 搜索回放（#6786）。
- 🧩 新功能：支持 React Native 的 Swift Package Manager 集成（#6784）。
- 📦 SwiftPM 细节：SDK 自带 `Package.swift`，`npx react-native spm` 可通过 SwiftPM autolinking 识别，不再报 `Package.swift is missing for library "@sentry/react-native"`；需 RN 0.87+，SwiftPM 为 opt-in 预览，CocoaPods 仍是默认且不受影响；仅 iOS，macOS/tvOS/visionOS 继续用 CocoaPods。
- 🧹 修复：`AsyncExpiringMap` 清理定时器不在导入时启动，并在 map 清空后重启（#6811）。
- 🔗 修复：防止 Sentry iOS `-force_load` 在其他 pod 设置 `OTHER_LDFLAGS[sdk=…]` 时被丢弃（#6801）。
- 🤖 修复：排除 `sentry-android-replay` 时，Android 构建不再报 `cannot find symbol ReplayIntegration`（#6803）。
- 🧷 修复：Expo iOS 插件保留已加引号的 React Native bundle 脚本路径（#6796）。
- 🎭 修复：通过 iOS codegen component provider 注册回放遮罩组件（#6810）；`RNSentryReplayMask`/`RNSentryReplayUnmask` 映射到 view classes，不再回退 legacy interop，并设置 typed default props 以避免挂载崩溃。
- ⬆️ 依赖：Android SDK 从 8.57.0 升至 8.59.0（#6778、#6814）。
- ⬆️ 依赖：Cocoa SDK 从 9.29.0 升至 9.30.0（#6785、#6787、#6813）。
- 👍 反馈：该发布获得 1 个点赞。

---

### [发布 v2.4.0 · callstackincubator/voltra · GitHub](https://github.com/callstackincubator/voltra/releases/tag/v2.4.0)

**原文标题**: [Release v2.4.0 · callstackincubator/voltra · GitHub](https://github.com/callstackincubator/voltra/releases/tag/v2.4.0)

overview summary  
Voltra v2.4.0 发布，重点优化 Android 16/17 常驻通知与实时更新，新增 SwiftUI、Jetpack Glance 原生修饰符和动态组件/实时活动本地化，并修复 iOS、Android 构建与权限问题。

- 🚀 发布 v2.4.0，由 github-actions 于 10 月 6 日 07:56 发布，贡献者为 @V3RON。
- 🤖 Android 16 常驻通知 Live Updates 体验优化。
- 📐 Android 17 MetricStyle 指标布局用于常驻通知。
- 🍎 iOS 修复独立 pod 模块名与 CI 示例构建。
- 🧩 新增 SwiftUI 和 Jetpack Glance 原生修饰符。
- 🌍 动态小组件与 Dynamic Live Activities 支持本地化。
- 🧪 示例项目通过 Appduct 向 agents 暴露 Voltra E2E 工具。
- 📥 Android 新增 BigPicture 与 Inbox 常驻通知 payload。
- ⚙️ Android 暴露常驻通知展示选项。
- 🛠️ 修复 compileSdk 36 应用与 Metric 布局的构建兼容性。
- 🔐 修复 Android 16.0 不强制要求 promoted-notification 权限。
- 🔗 完整变更日志：v2.3.2...v2.4.0。

---

### [](https://github.com/shergin/baton)

**原文标题**: [GitHub - shergin/baton: 🥖 Relay for SwiftUI and Compose · GitHub](https://github.com/shergin/baton)

Baton 是面向 SwiftUI 与 Compose 的 Relay 风格 GraphQL 客户端：视图旁声明 fragment，编译期聚合并校验，运行时以可观察记录提供缓存数据，实现首帧读取与字段级重渲染。它与 Relay 对齐而非 Apollo，强调小体积、声明式、模型友好，并已在 0.6.0 中打通读、写、列表、错误与持久化。

- 🥖 Baton 把 Relay 带到 SwiftUI 和 Compose：每个视图一个 fragment，每个屏幕一个请求，首帧读缓存，只重渲染字段变化的视图。
- 🧩 编译期把屏幕 fragment 聚合成一个 operation，按 schema 校验，并为每个 fragment 生成类型化 lens；运行时把响应规范化成 UI 框架可观察的记录。
- ⚛️ 与 Relay 的指令、约定和编译器谱系一致，但去掉 React 特有的 snapshot、re-read、抛 Promise 挂起，改用 SwiftUI Observation 与 Compose snapshot state。
- 🧱 核心原则：视图只读自己声明的字段；nullability 忠实于 schema；支持 @required、@catch、字段错误、staleness；生成代码小，运行时依赖 Foundation、Observation、系统 SQLite。
- 🚫 它不是运行时 GraphQL 客户端、不是模型层、不是策略对象配置、不是离线同步引擎/本地状态框架/服务器/React Native/Web 客户端；Swift 与 Kotlin 运行时独立，但共享编译器、产物格式、词汇与一致性测试。
- ✍️ 对人类和语言模型都友好：GraphQL 与视图同文件且完整有效；schema 决定存在性，生成 lens 决定可读字段，指令决定数据移动；无缓存策略、规范化器与 updater，错误在编译期定位到字符。
- 🚀 当前 0.6.0“Anchor Leg”：读、写、列表、错误、持久化全链路可用；支持乐观响应、connection 分页合并、字段错误、@defer、subscription、跨启动 store；1.0 前 API 会自由变动。
- 🧭 版本演进：0.1 编译器/lens/store/@Fragment/@Query；0.2 retained roots/释放缓冲/fetch 策略；0.3 @Mutation/乐观层/抽象类型；0.4 @connection/@refetchable/fragment 参数；0.5 字段错误/@required/@catch/@defer/subscriptions；0.6 磁盘 image/SQLite/跨启动。
- 🛠️ 使用方式：给 target 添加包与插件，放置 baton.json，构建时插件运行 batonc，为含 GraphQL 的 Swift 文件生成代码与 Baton.report.json。
- 🔐 持久化：通过 Environment(..., persistence: Persistence(name:version:)) 配置，Types.schemaDigest 让新 schema 重开 image；支持 protection、environment.log、await environment.end() 登出清理。
- 🧪 测试与预览：BatonTesting 提供 RecordedTransport/ScriptedTransport；BatonInspector 提供 store 调试视图；commitPayload 可从 payload 种子化 store，无需 transport。
- 🧵 非 SwiftUI 场景：模型/ViewController 用 handle.retain() 返回的 Retention 保持数据；revalidate() 在回前台时重取 stale/failed；传输层包装处理鉴权挑战、退避重试、截止时间，且 mutation 不重发。
- 🖥️ 仓库示例：swift run RickAndMorty 打开只读示例；GITHUB_TOKEN=... swift run GitHubTriage 打开含写、connection、union、1800 定义 schema、跨启动 image 与登出的示例；swift test 运行验证；release benchmarks 打印性能数据。
- ⚡ 性能：对比 Apollo iOS 2.4，Rick and Morty 686 KB/899 records 在 M1 Pro 上，入 store 3.4 ms vs 318 ms，同 payload 165 µs vs 3.99 ms，单字段 26 ns vs 296 ns；Apollo 需重建 query 为模型，Baton 首帧即有缓存。
- 📊 对比 Apollo：Baton 在视图内声明 GraphQL 并接收 lens；Apollo 用 .graphql 文件和 snapshot/嵌套模型；Baton 同步首帧读缓存，Apollo 异步/主线程外；Baton 只重渲染读该字段的视图，Apollo 重建整查询；Baton connection 在 store 合并分页，Apollo 每页 watcher。
- 🧳 内存与磁盘：Baton 滚动时内存趋于平稳，约 42 页 +5 MB；Apollo 保留所有记录。Baton 用系统 SQLite 一行一记录，Apollo iOS 每记录一个 JSON 字符串。
- 🍞 名字来源：baton 是接力棒，俄语 батон 是面包，因此符号是 🥖，logo 是面包。
- ⚖️ 许可证：MIT 或 Apache-2.0，二选一。
- 🧰 Caton 是演示 app：macOS 菜单栏 GitHub 通知 inbox，把通知与 PR/issue 实时状态连接起来，菜单栏数字表示等待你处理的数量。

---

### [发布 0.7.0 · DorianMazur/react-native-screen-choreography · GitHub](https://github.com/DorianMazur/react-native-screen-choreography/releases/tag/v0.7.0)

**原文标题**: [Release 0.7.0 · DorianMazur/react-native-screen-choreography · GitHub](https://github.com/DorianMazur/react-native-screen-choreography/releases/tag/v0.7.0)

这是 react-native-screen-choreography 仓库 v0.7.0 的发布说明，重点新增混合过渡交接、原生过渡准备与持久覆盖层，并修复 Expo Router 返回导航、更新文档和升级依赖要求。

- 🚀 发布 v0.7.0，由 DorianMazur 于 10 月 1 日 09:18 发布。
- 🤝 新增 hybrid transition handoff（#28）。
- 🧩 新增原生过渡准备和持久覆盖层，包括用于共享过渡上方交互控件的 ChoreographyOverlay（#20）。
- 🔙 恢复 Expo Router 58 的返回导航（#24）。
- ⚙️ 改进过渡启动、呈现就绪和交互拾取行为。
- 📚 刷新集成指南与 API 文档。
- ⬆️ 升级要求：react-native-teleport >=1.2.2；仍需 React Native 0.81+ 及新架构/Fabric。

---

### [](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.8.0)

**原文标题**: [Release Release 1.8.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.8.0)

React Native Nitro Fetch 发布 v1.8.0，带来超时传递、urlencoded 表单数据支持、中止请求处理、请求优先级等功能与修复，并升级 React Native，新增贡献者 eduardoborges。

- 🚀 最新版本 v1.8.0 已发布，由 riteshshukla04 于 9 月 30 日 17:58 发布到 main，包含 2 个提交。
- 🛠️ 修复：将 init.timeoutMs 转发到原生请求，由 @eduardoborges 提交于 #239。
- 📦 功能：为 urlencoded 请求和响应体支持 formData()，由 @riteshshukla04 提交于 #240。
- ⛔ 修复：使用 signal.reason 拒绝已中止的请求，由 @riteshshukla04 提交于 #242。
- ⬆️ 维护：将 React Native 升级至 0.88.0-rc.3，由 @riteshshukla04 提交于 #241。
- ⚡ 功能：支持请求优先级，由 @riteshshukla04 提交于 #243。
- 👏 新贡献者：@eduardoborges 在 #239 完成首次贡献。
- 📜 完整变更日志范围：v1.7.0...v1.8.0，贡献者包括 eduardoborges 和 riteshshukla04。
- ❤️ 该发布获得 1 个爱心反应。

---

### [](https://www.callstack.com/blog/apex-agetic-coding-for-mobile-and-web-spcialied-in-react)

**原文标题**: [Apex Is Now Generally Available: Agentic Coding Model for Mobile and Web, Specialized in React](https://www.callstack.com/blog/apex-agetic-coding-for-mobile-and-web-spcialied-in-react)

Callstack 正式发布 Apex——一个面向移动与 Web、专精 React 的高性价比 agentic 编码模型，主打 React Native 与 Next.js，并同步公布评测、定价、自托管方案与后续专用模型路线。

- 🚀 **Apex 正式 GA**：由 Callstack 打造，定位为日常 agent 工作的低成本模型，可在现有编码工具中用于开发、调试、审查和测试。
- 📱 **专精 React 生态**：首批发力 React Native，同时在 Next.js 任务上表现强劲；后续将推出原生 iOS 与 Android 专用模型。
- 🕵️ **曾以 Pixel Canary 匿名预览**：在 Vercel AI Gateway 上压力测试，5 天内处理超过 2000 亿 tokens。
- 🧠 **基于开放权重与自建流程**：早期基于 Gemma 4，现转向 Qwen；Callstack 负责领域数据、训练、评估与部署。
- 📊 **评测表现突出**：React Native Evals 达前沿水平；Next.js 评测完成 28/31 任务，结合 AGENTS.md 后达 30/31。
- ⚡ **代码审查对比亮眼**：在 Expensify React Native 仓库任务中，Apex 用 2 分 16 秒、$0.09 完成；Claude Opus 5.5 用 13 分 30 秒、$0.60。
- 💰 **成本最多降低 85%**：Apex 输入 $0.50/百万 tokens，缓存输入 $0.20，输出 $3.00；输出价格比 GPT-6 Sol 低 70%，比 Opus 5.5 低 85%。
- 🔁 **为反复迭代而定价**：更低成本让 agent 可多轮读代码、改代码、跑检查和修正错误。
- 🛠️ **配套 agent-device 验证工具**：让 agent 操作移动应用并收集证据，强调“专用模型 + 领域工具 + 验证”的价值。
- ☁️ **获取与部署方式**：可通过 Apex API 使用，Vercel AI Gateway 即将支持；企业可商业自托管，也可联系 Callstack 评估。
- 🧪 **快速开始**：访问 apex.callstack.com，并运行 `npx @callstack/apex init` 在支持的编码工具中配置。

---

### [](https://infinite.red/react-native-radio/rnr-374-building-dreaming-language-learning-with-react-native)

**原文标题**: [React Native Radio - RNR 374 - Building "Dreaming: Language Learning" with React Native](https://infinite.red/react-native-radio/rnr-374-building-dreaming-language-learning-with-react-native)

Mazen Chami 在 React Native Radio 第 374 集“Real Life React Native”中采访 Brains & Beards 的 Wojciech Ogrodowczyk，讨论如何用 React Native 构建通过“可理解输入”学习语言的应用 Dreaming: Language Learning。
- 🎙️ 节目聚焦真实生产中的 React Native 应用，分享离线视频、移动性能、原生模块和 AI 辅助开发经验。
- 🗣️ Dreaming 通过可理解输入学习语言，不做词汇表和语法练习，目前支持西班牙语和法语。
- 📱 应用是独立 React Native 项目，与 Web 平台分开，但共用后端 API；团队接手并继续开发约一年半。
- 🧱 技术栈包括 Expo、EAS、TanStack Query、React Navigation、Redux、TypeScript、FxJS、Wonka、XState、React Native Video、Sentry 和 Reactotron。
- ⚙️ 选择 Expo 主要为自动生成原生目录和简化 EAS 部署；TanStack Query 支撑离线缓存、乐观更新和数据持久化。
- 📶 离线播放是核心需求，用户常在飞机或跑步时使用，因此需处理大视频下载、文件缓冲落盘和后台播放。
- 🎬 视频播放是最大挑战之一：自定义控制层、全屏、旋转、Android 按钮、耳机按键、通知控制和后台运行都需深入原生代码。
- 🐛 团队曾向 React Native Video 提交约 10 个 PR，并维护 React Native Video 与 React Native Background Downloader 的自定义 fork。
- 🚀 性能教训：为让列表内视频即时播放曾采用“单个隐藏播放器+滚动同步”方案，提升性能但增加复杂度和残留状态 bug。
- 🧊 另一性能事故是持久化时用 SuperJSON 序列化大量日期，在慢 Android 上拖垮应用，最终回退为普通 JSON/手动处理。
- 🧪 测试策略：重视单元测试，慎用组件测试；因团队小且端到端测试维护成本高，未采用 E2E。
- 🤖 AI 用于生成基础测试、调查依赖库 bug、快速验证改进方案和辅助代码审查，但代码仍需达到人工可接受标准。
- 💡 给公司建议：移动开发没有明显坏选择，关键是团队接受；给新开发者建议：编程仍是手艺，复杂问题仍需开发者思考。
- ✅ Wojciech 表示若重来仍会选择 React Native，认为生态和工具已大幅成熟。

---

### [](https://github.com/microsoft/TypeScript/issues/63703)

**原文标题**: [TypeScript 7.1 Iteration Plan · Issue #63703 · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/issues/63703)

这是 TypeScript 7.1 的迭代计划（issue #63703），由 Daniel Rosenwasser 于 2026-07-31 创建，当前为 Open，标签为 Planning 和 Iteration plans and roadmapping。计划涵盖 Beta/RC/Stable 时间表，以及语言与编译器、编辑器、性能、基础设施和网站等重点工作。

- 📅 发布节奏：2026-10-02 Beta Prep、10-06 7.1 Beta、11-06 RC Prep、11-10 7.1 RC、11-20 Stable Prep、11-24 7.1 Stable。
- 🧩 语言与编译器：稳定 Content Mapper、Emit、Language Service 等 API；支持 Import Attributes 上的 type；调查 Node 26 Package Maps；为 lib 和 target 添加 es2026；支持 Source Phase Imports。
- 📚 lib.d.ts 更新：新增迭代器方法；Promise.allKeyed 与 Promise.allSettledKeyed；DOM 更新。
- 🧑‍💻 编辑器生产力：替换 VS Code 现有 API 集成；调查 LSP 可展开悬停、多文档高亮和区域诊断 API。
- ⚡ 性能：加快联合类型构造；延迟收集源文件标识符；联合类型赋值/相等/switch-case 收窄快速路径；优化检查器副表表示；试验跨类型检查器分发文件算法；可能还有更多。
- 🏗️ 基础设施：nil 检查与类型转换静态分析；仓库迁移到 microsoft/TypeScript；发布管线大修；发布 wasm（wasip1?）和 Android ARM64 构建；检测不稳定诊断。
- 🌐 网站：收集 Monaco LSP 反馈；让 Playground 基于 wasm 运行；加速网站构建。
- 📌 当前元数据：暂无指派者、里程碑、项目、关联分支或 PR。

---

### [](https://github.com/typescript-eslint/typescript-eslint/issues/10940#issuecomment-5900712238)

**原文标题**: [Enhancement: Use TS 7 (tsgo / typescript-go) for type information · Issue #10940 · typescript-eslint/typescript-eslint · GitHub](https://github.com/typescript-eslint/typescript-eslint/issues/10940#issuecomment-5900712238)

该 issue 提出让 typescript-eslint 利用 TypeScript 的 Go 移植版（tsgo / typescript-go，即 TS 7）来提供类型信息，从而大幅提升 typed linting 性能。该想法仍处于早期探索阶段，面临异步解析、tsgo 稳定性、JS 与 Go/WASM 间 AST/类型信息通信等挑战，但欢迎社区实验和提交 PR。

- 🚀 目标：使用 TS 7（tsgo / typescript-go）为 typescript-eslint 提供类型信息，把 typed linting 的类型检查瓶颈提速约 10 倍。
- 🧩 相关包：typescript-estree；issue #10940 由 JoshuaKGoldberg 于 2025-03-11 创建。
- 🏷️ 状态：标签为 accepting prs、enhancement、team assigned，表示欢迎 PR 且已有团队成员负责。
- ⏳ 难点一：ESLint 尚不支持异步解析器，而 tsgo 很可能通过原生绑定/WASM 异步使用；不过评论认为这可能不会长期成为阻碍。
- 📉 难点二：tsgo 尚不稳定，可能还需数月；未来约 1–2 个 typescript-eslint 大版本内不太可能成为 TypeScript 主稳定版本。
- 🔄 难点三：ESLint 规则仍依赖 JS 侧 AST，需要设计如何把 AST 节点和类型信息从 Go/WASM 传回 JS。
- 🛠️ 推进方式：需要大量设计探索；欢迎提交 PR 或实验，以帮助未来采用更快的 typed linting。
- 📚 附加建议：若 typed linting 慢，先查看官方性能故障排除指南；正确配置时不应显著慢于类型检查。
- 📌 元数据：暂无里程碑、项目、分支或 PR，关系项暂无。

---

### [Bluesky 上的 @robpalmer.bsky.social](https://bsky.app/profile/robpalmer.bsky.social/post/3mwshmpvhak24)

**原文标题**: [@robpalmer.bsky.social on Bluesky](https://bsky.app/profile/robpalmer.bsky.social/post/3mwshmpvhak24)

Rob Palmer（robpalmer.bsky.social）在 Bluesky 发帖表达对 ECMAScript 的期待，并汇总本周 TC39 推进的多项提案，涉及第 4、3、2.7、2、1 阶段。

- 🎉 本周 @tc39.es 推进了多项 ECMAScript 提案。
- 4️⃣ Dynamic Code Brand Checks（动态代码品牌检查）进入第 4 阶段。
- 4️⃣ Iterator Chunking/Includes/Join（迭代器分块/包含/连接）进入第 4 阶段。
- 3️⃣ Thenable Curtailment（Thenable 限制）进入第 3 阶段。
- 2️⃣.7️⃣ export * from "mod" 中的 default 进入第 2.7 阶段。
- 2️⃣.7️⃣ export defer 进入第 2.7 阶段。
- 2️⃣.7️⃣ JSON.parse options（JSON.parse 选项）进入第 2.7 阶段。
- 2️⃣ BigInt from Exponential 进入第 2 阶段。
- 2️⃣ Composites 进入第 2 阶段。
- 1️⃣ Pulling in AbortController（引入 AbortController）进入第 1 阶段。
- 🕒 帖子发布时间为 2026-10-01T08:44:13.861Z。
- 🌐 原帖来自 Bluesky；需启用 JavaScript 才能使用，详情见 bsky.social 与 atproto.com。

---

### [混音之道](https://sergiodxa.com/articles/the-remix-way)

**原文标题**: [The Remix Way](https://sergiodxa.com/articles/the-remix-way)

作者用六个月、约 88 个自建包和 11 个应用，把“使用 Remix”推进为“按 Remix 的方式构建”：契约优先、尽量基于 Web 标准、近零依赖，并把路由、MCP、后台任务统一成 Request→Response 映射，最后用招聘板 Demo 和开源 monorepo 展示整套思路。

- 🧪 约半年前作者尝试 Remix v3 alpha，并重建拥有近 650 篇文章、D1 数据库、RSS/Atom/JSON Feed、缓存、Markdown 与代码高亮的博客。
- 🧩 原 monorepo 包含 React Router 博客、Auth 书落地页、Uptime 监控应用和身份提供器，以及约 20 个共享包。
- 🛠️ 迁移中先自建 XML 库和 Remix helpers，后来被 remix/router 官方 helpers 取代。
- 🗄️ 想使用 remix/data-table，但官方只提供 Postgres/MySQL/SQLite 适配器，于是基于 Database 契约实现 D1 与 Durable Object SQL storage。
- 📜 Remix v3 强调“契约而非仅实现”：Database、SessionStorage 等接口可自定义实现，促成了 Worker KV Session Storage 和 Cache 契约。
- 💾 @sdxc/cache 提供内存缓存用于测试，Worker KV 缓存用于生产，体现契约驱动设计。
- ✉️ 邮件 Transport 契约让 Resend 切换到 Cloudflare 只需改一行；计费 Billing 契约也有 Memory、Stripe、Polar 实现。
- 🎨 组件模型基于 remix/component，尽量少客户端 JS：博客零水合组件，Uptime 仅水合必要组件。
- 🧱 作者自建 @sdxc/u 和 @sdxc/ui，用 mixin 实现类似 Tailwind 的样式系统，并支持容器查询、暗色模式等。
- 📦 追求近零依赖，自建大量包覆盖 api-client、auth、billing、cache、cron、crypto、csv、i18n、jobs、jwt、markdown、mcp、rss、sitemap、validate、webhooks、xml、yaml 等。
- 🛣️ 路由定义与请求处理器映射分离，使服务端和客户端都能共用路由表，解析 URL 并获得类型错误。
- 🤖 将 Request→Response 模式扩展到 MCP：定义 tools/resources，用 createTool/createHandler 映射到同一 router，并支持中间件与限流。
- ⚙️ 后台任务用 jobs 表声明 cron 与输入 schema，createJobHandler 类型安全处理，dispatcher 配置中间件并映射作业，enqueue 也类型安全。
- 🌐 遵循“构建于 Web API 上”：Dialog 用 command/commandfor，i18n 用 Unicode MessageFormat 2 与 Intl.MessageFormat，许多包直接实现标准。
- 🧪 Demo 是招聘板应用，数千行代码约半数为 JSDoc，使用 19 个自建包；列表页只水合一个组件，详情按需解析 Markdown，island 仅 846 字节。
- 📮 发布表单用 HTML 属性打开 dialog，captcha 与限流作为中间件；发布入队任务，邮件经 Transport 契约进入内存 outbox。
- 🔗 MCP 与普通路由共用同一路由器，使 agent 能像浏览器一样读取招聘板。
- 🏁 六个月、88 个包、11 个应用后，作者从“用 Remix 构建”转向“以 Remix 的方式构建”。
- 💰 文末邀请通过 GitHub 赞助，以支持更多教程、文章和开源工具。

---

### [使用 Jev 作为 Linter 强制执行最佳实践 | Nicolas Charpentier](https://charpeni.com/blog/enforcing-best-practices-with-jev-as-a-linter)

**原文标题**: [Enforcing Best Practices with Jev as a Linter | Nicolas Charpentier](https://charpeni.com/blog/enforcing-best-practices-with-jev-as-a-linter)

这是 Nicolas Charpentier 的个人博客页面，包含其前端基础设施与开发工具背景、以 git log 形式展示的 39 篇博客归档，以及最新文章《Enforcing Best Practices with Jev as a Linter》的正文。文章核心是：在 AI 代理大量生成代码的时代，最佳实践若不能自动强制执行，就只是建议；作者用 Jev 将自然语言规则变成可在 PR 中运行的 lint 检查。

- 👤 作者 Nicolas Charpentier 是 Staff Software Engineer，专注前端基础设施与开发工具，技术栈包括 TypeScript、React Native、React、GraphQL、CI/CD。
- 🗂️ 博客归档以 git log 呈现，共 39 篇文章、6 个分支，主题覆盖 tooling、testing、typescript、react、graphql、homelab 等。
- ⚠️ 文章指出：AI 代理不会记住过去的 PR 评论，重复提醒最佳实践会浪费审查时间；能强制执行才算最佳实践，否则只是建议。
- 📄 单靠 AI-REVIEW.md 文档并不可靠，代理或 AI 审查者可能漏读、漏报，而 AST 规则也难以覆盖“测试命名要反映目的”这类非语法规则。
- 🧠 Jev 是 TypeSafe 模型：输入状态和类型化问题，返回带校准概率的类型化答案；oxlint-plugin-jev 把每条规则变成问题、目标和 cutoff。
- ✍️ 示例规则 prefer-use-boolean-state 用自然英语描述：优先用 useBooleanState，而不是布尔型 useState 加 memoized setter-only 回调，并明确列出例外。
- 🎯 通过可选 location 问题定位具体行号，解决 target:file 时所有问题都报在第 1 行的情况；若不确定，则保留文件级诊断。
- 🤖 与 Oxlint 的 GitHub formatter 集成，在 PR 中生成注解，附带简短解释和指南链接，方便代理迭代修复直到检查通过。
- 💰 成本极低：前 175 次运行 Jev 总共花费 $0.35，约每次 0.2 美分；同期 GitHub Actions 运行约 167 分钟，花费约 $0.67，运行成本反而高于模型本身。
- ✅ 结论：Jev 让团队用英语编写含例外的最佳实践规则，把重复代码审查转化为可执行、可自动修复的检查。

---

### [GitHub - tester-army/e2e：面向 Web 和移动应用的下一代](https://github.com/tester-army/e2e)

**原文标题**: [GitHub - tester-army/e2e: Next generation e2e testing framework for web and mobile apps. · GitHub](https://github.com/tester-army/e2e)

e2e 是由 TesterArmy 开发的面向 Web 与移动应用的新一代端到端测试框架，支持用自然语言描述目标、由 agent 驱动应用执行，并在同一测试中用 locator 和断言验证结果；项目采用 Apache-2.0 许可，目前处于活跃开发阶段。

- 🧪 核心能力：用自然语言描述目标，agent 驱动应用达成目标，再用 locator 与断言检查结果。
- 🤖 智能执行：agent 步骤会记录动作，后续运行可重放，除非应用发生变化才需要模型调用；不含 agent 步骤的测试无需模型。
- 🔌 模型支持：可自带订阅、API key 或本地模型。
- 🚀 快速开始：运行 `npx e2e init`，选择 Web 或移动引擎及模型提供商，生成配置和示例测试。
- 🧩 示例项目：提供 Vite、Next.js、Expo、SwiftUI 等独立示例，均包含可通过的测试套件。
- 📦 包与引擎：`e2e` 提供 SDK、运行器和 CLI；`@e2e-dev/web` 通过 Playwright 支持 Chromium、Firefox、WebKit；`@e2e-dev/mobile` 通过 agent-device 支持 iOS/Android 模拟器；另有 GitHub 报告器、托管浏览器、EAS 托管模拟器、决策模型执行器等包。
- 📚 文档：见 e2e.tester.army/docs，`e2e` 包内含完整页面，便于编码 agent 在 `node_modules/e2e/docs` 离线阅读。
- 🤝 贡献与安全：贡献指南见 `CONTRIBUTING.md`，问题可到 Discord；安全漏洞请按 `SECURITY.md` 报告至 security@tester.army，不要公开开 issue。
- 📡 遥测：CLI 会发送匿名使用数据，如命令、引擎和失败位置，但不含测试内容、应用内容或凭据；可用 `npx e2e telemetry disable` 或 `E2E_TELEMETRY_DISABLED=1` 退出。
- 📈 仓库状态：约 6.3k stars、284 forks、17 watchers、669 commits、20 issues、53 pull requests；项目正朝 1.0 开发，API 和配置仍可能在小版本间变化。
- 🏢 背后团队：由 TesterArmy 构建，其 agentic 测试平台可在每次 PR 或按计划运行 Web 与移动端自然语言测试。

---

### [Effect 4.0 | Effect 博客](https://effect.website/blog/releases/effect/40)

**原文标题**: [Effect 4.0 | Effect Blog](https://effect.website/blog/releases/effect/40)

Effect 4.0 是迄今最雄心勃勃的版本，从底层重写，带来显著性能提升、统一零依赖生态和长期支持承诺；它覆盖从单函数到分布式集群的完整开发场景，并已在生产环境中获得主流采用。

- 🚀 Effect 4.0 正式发布：核心从底层重建，速度更快、内存占用更低、打包体积更小。
- ⚡ 性能大幅提升：包体缩小 5 倍（35.6 kB→7.1 kB），并发吞吐提升 6.4 倍（0.71M→4.57M 任务/秒），每 fiber 内存减少 86%（5 万 fibers 157.5 MB→21.8 MB）。
- 📦 统一生态与零依赖：许多原独立包并入 `effect`，共享版本并同步发布；核心包零运行时依赖，降低第三方依赖链与供应链风险。
- 🧩 覆盖从函数到集群：基于同一编程模型提供类型化错误、依赖注入、资源管理、结构化并发和可观测性，并扩展到持久工作流与集群。
- 📈 主流采用：2026 年 9 月 21 日当周 npm 下载量达 43.9M，较 3.x 增长 179 倍；过去 7 天 4.x 采用率 56%，3.x 为 44%。
- 🏢 生产与社区：大型企业已在生产中使用 Effect；Alchemy（云基础设施）和 Foldkit（前端）等社区项目正在成长。
- 🛡️ 长期支持：从 4.x 起每个大版本都有 LTS；4.x 的 bug 修复持续至 2029 年 9 月或 5.0 发布后一年，安全修复持续至 2029 年 9 月或 5.0 发布后两年，取较晚者，至少 3 年。
- 🧭 下一步：优先稳定更多模块，将标记为 unstable/experimental 的功能逐步提升为 stable，并扩展为覆盖整个应用的单一编程模型，增强原生平台支持与高层原语。
- 🔄 迁移与资源：建议从迁移指南开始，可交给编码代理完成大部分工作；文档、X、Bluesky 和 Discord 可获取更多帮助。

---

### [@effect/atom-react API 参考 | Effect](https://effect.website/docs/v4/api/atom-react)

**原文标题**: [@effect/atom-react API Reference | Effect](https://effect.website/docs/v4/api/atom-react)

这是 Effect 生态中 `@effect/atom-react` 的 v4 API 参考页，说明其为 Effect Atom 模块提供 React 绑定，并列出相关模块与资源入口。

- 📦 包名：`@effect/atom-react`
- ⚛️ 用途：为 Effect Atom 模块提供 React 绑定
- 🧩 页面显示包含 4 个模块
- 📚 列出的模块/条目包括：Core、Hooks、ReactHydration、RegistryContext、ScopedAtom
- 🔍 支持搜索 `atom-react` 模块
- 🚫 当前搜索结果为：无匹配模块
- 🛠️ 提供 npm 与源码入口
- 📍 页面位置：API Reference / v4 / atom-react

---

### [博客 | pnpm](https://pnpm.io/blog)

**原文标题**: [Blog | pnpm](https://pnpm.io/blog)

2026年9月25日至10月6日，pnpm 密集发布 12.x 与 11.28.x 多个版本，重点涵盖实验性 loaded 链接器、锁文件与缓存元数据增强、WebContainer/WASM 拆分、安装与发布流程修复、多平台性能优化，以及针对凭据泄露、包归档、Git 依赖和配置依赖的安全修复。

- 🐛 **pnpm 12.10.1（2026-10-06）**：修复 overrides 变更后 `pnpm install` 失败、带 `catalogPrune` 的过滤冻结安装失败，并修复实验性 `nodeLinker.type: loaded` 的多个问题，生成文件现保留在 `node_modules`。
- 🧪 **pnpm 12.10.0（2026-10-06）**：引入实验性 `loaded` 节点链接器，让 `pnpm-lock.yaml` 记录解析设置，加快读取缓存 registry 元数据；含安全修复，阻止依赖版本写入全局虚拟存储之外。
- 🔒 **pnpm 11.28.5（2026-10-06）**：加快缓存 registry 元数据读取，使 `pnpm config get --global` 忽略项目设置；修复包归档、git 依赖和配置依赖的安全问题。
- 📦 **pnpm 12.9.1（2026-10-03）**：将 WebContainer 构建移至独立 `@pnpm/wasm` 包，把 `pnpm` 包缩回约 4 MB，修复 GitLab CI 中带 provenance 的 `pnpm publish`。
- 🛡️ **pnpm 11.28.4（2026-10-03）**：修复两处凭据泄露，`pnpm install --frozen-lockfile` 接受更多此前拒绝的锁文件，可选依赖拉取失败时告警，并避免 `pnpm self-update` 在 Homebrew 版旁再装一个 pnpm。
- 🚀 **pnpm 12.9.0（2026-10-02）**：支持在 StackBlitz WebContainers 中运行，新增按 registry 的 `networkConcurrency` 设置，并在 store 中记录每个已安装项目；修复 `pnpm login` 安全问题。
- ⚡ **pnpm 12.8.2（2026-09-30）**：修复 Linux ppc64le 启动崩溃和无 CA 证书系统的 `UnknownIssuer` 错误；启用 `autoDedupe` 时 CI 上 `pnpm run` 不再每次脚本前安装，macOS 解析和 hoisted 安装更快。
- 🧹 **pnpm 12.8（2026-09-28）**：当 `pnpm pack` 或 `pnpm publish` 可能打包 `.env` 时告警，并发安装 `sharedWorkspaceLockfile: false` 工作区，应用所有 `--config.<name>=<value>` 设置，修复 Windows 脚本中 Ctrl+C 后终端卡住等问题。
- 🧩 **pnpm 12.7（2026-09-25）**：全局 `node` shim 支持 `.nvmrc` 和 `.node-version`，新增 `pnpm install --allow-build` 与 `pnpm publish --publish-wait-timeout`，可从 `package.json` 的 `workspaces` 字段创建 `pnpm-workspace.yaml`；`pnpm install --force` 不再安装其他平台的可选依赖。
- 🔧 **pnpm 11.28（2026-09-25）**：新增 `forceIgnoresPlatform` 设置和 `pnpm update --peer`，从 pnpm 12 移植大量修复，改善 `pnpm deploy`、`--filter`、`nodeLinker: hoisted` 和自定义 `modulesDir`；含 shell 补全、Nix bin shims、自定义 `modulesDir` 生命周期脚本和 `userAgent` 占位符等安全修复。

---

### [](https://h3.dev/blog/v2)

**原文标题**: [H3 v2 - H3](https://h3.dev/blog/v2)

H3 v2 于 2026-10-03 稳定发布，是基于 Web 标准的完整重写，兼容大多数 v1 工具，并比 v1 更快、更小；它支持多运行时、现代路由、中间件与插件、类型安全、路由规则和丰富内置工具，升级门槛较低，但 Node.js 需 >= 20.19。
- 🎉 H3 v2 现已稳定：完整重写，基于 Web 标准，兼容大多数 v1 工具，性能更快、体积更小。
- 🌐 Web 标准优先：基于 Request、Response、URL、Headers；处理器接收 event.req 和 event.url，通过 event.res 设置响应头，返回值会自动转换为 Response。
- 🚀 到处运行：同一应用可运行在 Node.js、Bun、Deno、Cloudflare Workers、Service Workers 和浏览器；srvx 提供通用服务器层，event.req.runtime 可访问运行时细节。
- 🌳 URLPattern 风格路由：使用 rou3 v1，支持命名参数、正则约束、可选/重复参数、分组和通配符；按树逐段匹配，查找快速。
- 🧩 中间件与插件：支持 (event, next) 中间件，内置 onRequest、onResponse、onError、basicAuth、bodyLimit 等辅助函数，并可用 definePlugin() 定义可复用插件。
- 🔒 类型安全：处理器、响应和 HTTPError 均有类型；验证处理器及 body/query/params 验证支持任意 Standard Schema 库。
- 📏 路由规则：h3/rules 引擎可用一个配置对象为路由组添加 headers、重定向、CORS、缓存和代理。
- 🧰 内置工具：包括 cookies（含分块）、sessions、CORS、代理、静态文件、缓存头、SSE、通过 crossws 的 WebSocket、JSON-RPC/MCP 助手和 h3/tracing 插件。
- ⬆️ 升级友好：大多数 v1 工具继续可用，废弃的 v1 名称仍导出；在 Node.js 上需 >= 20.19。
- ❤️ 特别感谢：感谢贡献者、beta/RC 测试者、社区、Nitro 社区和赞助商；可加入 Discord 分享反馈。

---

### [SvelteKit 3 来了](https://svelte.dev/blog/sveltekit-3-is-here)

**原文标题**: [SvelteKit 3 is here](https://svelte.dev/blog/sveltekit-3-is-here)

SvelteKit 3.0 已发布，作为 Svelte 官方应用框架，它更精致、更类型安全、更精简；提供自动迁移与新应用创建命令，但有若干破坏性变更，远程函数仍未正式就绪，Svelte Summit 将于 11 月在卢布尔雅那举行。

- 🚀 SvelteKit 3.0 于 2026 年 10 月 1 日发布，是 Svelte 的官方应用框架。
- 🧹 整体体验依旧熟悉，但更完善、类型安全更强、冗余更少。
- 🛠️ 可用 `sv migrate sveltekit-3 --tasks all --confirm` 自动迁移，并生成待办清单。
- ✨ 创建新应用可运行 `sv create my-new-app`。
- ⚠️ 重大版本升级带来一些破坏性变更，详情见迁移指南或候选发布公告。
- ⚙️ 配置从 `svelte.config.js` 移到 `vite.config.ts`。
- 📦 `$lib` 别名改为 `#lib`，改用标准子路径导入。
- 🌱 环境变量更强大、更易用。
- 🧩 Service worker 模板代码更少。
- 🐞 错误处理全面改进。
- 🔐 Remote functions 尚未就绪，但已是最高优先级；使用需 Async Svelte 和实验性标志。
- 🎂 下一届线下 Svelte Summit 将于 11 月 19-20 日在斯洛文尼亚卢布尔雅那举行，并庆祝 Svelte 十周年。

---

### [](https://www.youtube.com/watch?v=TaKBQnYm9tM)

**原文标题**: [Remix Jam 2026 - YouTube](https://www.youtube.com/watch?v=TaKBQnYm9tM)

这是一组 YouTube 页面底部的导航链接与版权信息，涵盖平台介绍、商业合作、开发者资源、法律政策及功能测试入口。

- ℹ️ 基础信息：关于、新闻、联系我们。
- 🎬 创作者与商业：创作者、广告、开发者。
- 📜 法律与安全：版权、条款、隐私、政策与安全。
- ⚙️ 平台说明与测试：YouTube 运作方式、测试新功能。
- ©️ 版权归属：© 2026 Google LLC。

---

