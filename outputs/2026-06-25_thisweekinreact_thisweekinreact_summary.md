### [设置亚马逊设备构建工具以进行 AI 驱动开发 | 设计与开发 Vega 应用](https://developer.amazon.com/docs/vega/0.22/mcp-server.html?sc_category=&sc_channel=3P&sc_publisher=TWR&sc_campaign=ACQ_VG&sc_country=US&sc_detail=SLORBER-5_VG_PROD)

**原文标题**: [Set Up Amazon Devices Builder Tools for AI-Powered Development | Design and Develop Vega Apps ](https://developer.amazon.com/docs/vega/0.22/mcp-server.html?sc_category=&sc_channel=3P&sc_publisher=TWR&sc_campaign=ACQ_VG&sc_country=US&sc_detail=SLORBER-5_VG_PROD)

本文件介绍了 Amazon Devices Builder Tools for AI-Powered Development，这是一套为 Fire TV（Vega OS）开发者提供的 AI 辅助开发工具，包括 MCP 服务器、Agent 技能和指导文档，旨在帮助开发者更高效地构建、调试和优化应用。

- 🤖 **核心组件**：包含 Builder Tools MCP Server（提供元数据与工具）、Agent Skills（模块化指令集）和 Steering Documents（最佳实践指南），三者协同工作。
- 🛠️ **快速开始**：通过终端运行 `npx @amazon-devices/amazon-devices-buildertools-mcp@latest init-context` 命令即可自动安装配置，支持交互式和非交互式模式。
- ✅ **验证设置**：使用 `check-status` 命令检查配置状态，然后在 AI 代理中尝试“列出工具”或“设置 Vega SDK”等提示，确认工具正常运行。
- 📋 **Agent Skills**：提供多种预设技能，如 SDK 安装、构建运行、导航、焦点管理、媒体播放、性能调试等，可自动触发。
- 🔧 **MCP 工具**：包括性能分析（analyze_perfetto_traces）、CPU 热点检测（get_app_hot_functions）、文档搜索（search_documentation）、崩溃符号化（symbolicate_acr）等实用功能。
- 💡 **支持的工作流**：涵盖入门设置、应用移植、功能集成、UI 开发、性能优化、崩溃分析等多个开发阶段，并提供示例提示。
- 🔒 **隐私保护**：工具不收集代码、查询或项目文件，仅在本地运行；文档搜索查询会发送至 Amazon 服务，但匿名遥测数据可禁用。
- 📚 **相关资源**：提供 ReadMe、构建指南、性能最佳实践、崩溃调试等文档链接，以及社区支持和隐私政策。

---

### [<Fragment>（<>...</>）– React](https://react.dev/reference/react/Fragment)

**原文标题**: [<Fragment> (<>...</>) – React](https://react.dev/reference/react/Fragment)

### 概述摘要
`<Fragment>`（常写作 `<>...</>`）用于在不添加额外 DOM 节点的情况下对元素进行分组。Canary 版本支持 `ref`，允许直接操作 Fragment 内的 DOM 节点。

- 📦 **核心用途**：使用 `<>...</>` 或 `<Fragment>` 将多个元素分组，无需包装节点，且不影响布局样式。
- 🔑 **Key 属性**：在循环中渲染 Fragment 列表时，必须使用显式 `<Fragment key={...}>` 语法，不能使用 `<>...</>`。
- 🆕 **Canary 特性**：Fragment 支持 `ref`，提供 `FragmentInstance` 对象，用于操作内部 DOM 节点。
- 🎯 **事件监听**：通过 `addEventListener` 和 `removeEventListener` 管理 Fragment 内所有第一级 DOM 子元素的事件。
- 🔄 **焦点管理**：`focus()`、`focusLast()` 和 `blur()` 方法可深度优先搜索并管理 Fragment 内所有嵌套子元素的焦点。
- 📜 **滚动控制**：`scrollIntoView(true/false)` 可滚动 Fragment 的第一个或最后一个子元素到视图中。
- 👁️ **可见性观察**：使用 `observeUsing` 和 `unobserveUsing` 附加或分离 `IntersectionObserver` 或 `ResizeObserver`。
- 🗂️ **缓存优化**：通过 `reactFragments` 属性（每个 DOM 子元素上的 `Set`）实现全局 `IntersectionObserver` 共享，避免重复创建。
- ⚠️ **注意事项**：`scrollIntoView` 不接受对象参数；`observeUsing` 不适用于纯文本子元素；`addEventListener` 不会应用于隐藏的 `<Activity>` 树。

---

### [发布 Fragment 引用到 Canary 版本 · 拉取请求 #34720 · react/react · GitHub](https://github.com/react/react/pull/34720)

**原文标题**: [Release Fragment refs to Canary by eps1lon · Pull Request #34720 · react/react · GitHub](https://github.com/react/react/pull/34720)

React 的 `<Fragment>` 组件现在支持 `ref` 属性，并已发布到 canary 版本，为未来的稳定版发布做准备。

- 🚀 **Fragment 新增 ref 支持**：`<Fragment>` 组件现在可以接收 `ref` 属性，该功能已合并到 `react@canary` 中。
- ✅ **经过生产测试**：此 API 已通过广泛的生产环境测试，团队对其稳定性充满信心。
- 📦 **Canary 工作流**：鼓励库和框架遵循 Canary 工作流，使用 `react@canary` 测试 Fragment refs，以提前发现兼容性问题。
- 🧪 **框架可先行采用**：遵循 Canary 工作流的框架可以开始采用此功能，并承诺在稳定版发布前保持 API 变更对用户透明且无破坏性。
- ⏳ **应用建议**：不依赖框架的应用可以自由采用，但建议等待 semver 稳定版发布，除非有精力跟进 canary 变更和调试兼容性问题。
- 📚 **文档与资源**：更多信息可查看 "React Labs: View Transitions, Activity, and more" 博客文章和 Fragment refs 的新文档。

---

### [jackpope 提交的拉取请求 #5012 · react/react-native-website · GitHub：为 RN 片段引用操作添加文档](https://github.com/react/react-native-website/pull/5012)

**原文标题**: [Add docs for RN fragment ref operations by jackpope · Pull Request #5012 · react/react-native-website · GitHub](https://github.com/react/react-native-website/pull/5012)

这是一个针对 React Native 文档仓库的 Pull Request，旨在为 Fragment Ref 操作添加文档。

概述总结
- 📄 该 PR 为 React Native 的 Fragment Ref 操作新增文档内容。
- 🔀 由 jackpope 发起，请求将分支 `fr-documentation` 合并到主分支 `main`。
- 🏷️ 已添加“CLA Signed”和“p: Facebook Partner”标签。
- ✅ Netlify 已生成部署预览链接，可供审查。
- 🔗 该 PR 被 slorber 在另一个项目中引用，用于实现冻结非活动屏幕的功能。
- ⏳ 目前无审查人员、无指派人员，且未设置里程碑。

---

### [开源 React 甘特图 | SVAR 甘特图](https://svar.dev/react/gantt/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=june_2026/)

**原文标题**: [Open-Source React Gantt Chart | SVAR Gantt](https://svar.dev/react/gantt/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=june_2026/)

这是一个用于项目调度的原生 React 甘特图组件，支持交互式时间线、任务和依赖关系管理，采用 TypeScript 构建，易于集成和自定义。

- 🚀 高性能甘特图组件，专为 React 设计
- 📅 支持交互式时间线和任务管理
- 🔗 具备依赖关系管理功能
- 🛠️ 使用 TypeScript 构建，提供完整类型支持
- 🆓 提供免费版和专业版（PRO Edition）
- 👀 可查看在线演示和示例
- 🔄 也支持其他平台/框架

---

### [React 编译器集成 by Jarred-Sumner · 拉取请求 #32504 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/32504)

**原文标题**: [React Compiler integration by Jarred-Sumner · Pull Request #32504 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/32504)

Bun 集成了 React 编译器，作为内置转换功能，通过 `bun build --react-compiler` 或 `Bun.build({ reactCompiler: true })` 启用。

- 🚀 **性能卓越**：在大型 React 代码库上，比 Babel 插件快约 20 倍（465ms vs 9.15s），原生 `--compile` 构建快 3.6 倍。
- 🧩 **零依赖架构**：将上游 React 编译器 Rust 工作区直接移植为单一 crate（~62k LOC），无需 Babel/SWC/OXC 中间 AST，且不引入 `serde`、`indexmap` 等新依赖。
- ⚙️ **构建时自动记忆化**：在构建过程中，对组件和钩子函数自动运行 React 的自动记忆化编译器，无需额外工具链。
- 🛠️ **新增构建选项**：包括 `reactCompiler`（启用）、`reactCompilerOutputMode`（client/ssr）、`treeShaking` 和 `reactCompilerParseTestPragmas`（测试用）。
- 📐 **智能架构设计**：编译钩子在 `visit_stmts` 内部触发，非 RC 路径仅增加一次 `is_some()` 检查，性能开销极小。
- ✅ **全面测试覆盖**：通过 1,647 个上游测试用例（160 个跳过，0 个失败），二进制体积仅增加约 1.0 MB。

---

### [肯尼斯·斯科夫胡斯 | 将 Linear 从 styled-components 迁移至 StyleX](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

**原文标题**: [Kenneth Skovhus | Moving Linear from styled‑components to StyleX](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

### 概述总结
Linear 团队将 React 应用从 styled-components 迁移到 StyleX，主要出于性能优化和更严格的样式封装需求。迁移过程采用代理辅助的工作流，通过 codemod 工具逐步替换，目前已完成 58% 的代码转换，页面渲染速度提升约 30%。

- 📉 **性能优先**：运行时 CSS-in-JS 导致客户端渲染时产生样式生成和规则注入开销，StyleX 将样式生成移至构建阶段，减少运行时负担。
- 🔒 **强化封装**：styled-components 允许外部随意覆盖组件样式，导致维护困难；StyleX 通过严格约束使组件样式契约更清晰，减少“远距离样式”问题。
- ⚙️ **确定性解析**：StyleX 提供可预测的样式合并机制，避免 CSS 特异性游戏，提升跨文件样式一致性。
- 🛠️ **代理辅助迁移**：开发了 500+ PR 的 codemod 工具（含在线 playground），通过定义样式基础、从叶节点开始迁移、严格 lint 规则和 CSS Modules 逃生舱，实现渐进式替换。
- 📈 **显著性能提升**：迁移后页面导航渲染速度提升约 30%，同时通过自定义 lint 规则和 Oxlint 扩展，有效防止旧模式扩散。
- 🧩 **生态与未来**：StyleX 由 Meta 积极维护，已被 Figma、Cursor 等采用，兼容现代 React 模式，且提供类型安全样式契约。

---

### [一次被低估的重构如何节省了 90% 的内存使用 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

**原文标题**: [How an Underrated Refactor Saved 90% Memory Usage | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

TanStack Table V9 通过共享原型重构，在处理百万级数据时内存使用量降低高达 90%，最大支持行数从约 100 万提升至 1000-1600 万行。

- 🚀 **性能飞跃**：V9 相比 V8 在处理 100 万行 x8 列数据时，内存占用从 2.7GB 降至 257MB，节省超过 2.4GB，提升幅度达 90.5%。
- 💡 **核心优化**：通过将行、列、单元格等对象的方法移至共享原型，避免为每个实例重复创建函数和闭包，大幅减少内存开销。
- 📊 **基准测试**：在分页、虚拟滚动等场景下，内存节省随数据量增长而显著放大；小数据量时差异可忽略，但大数据量时优势极其明显。
- 🔧 **实现细节**：使用`Object.create()`创建原型链，方法仅创建一次并缓存于表格实例，每个对象只存储唯一数据（如 ID、缓存），方法通过`this`访问实例。
- ⚠️ **破坏性变更**：方法不再支持解构调用（如`const { getValue } = row`），必须通过对象调用（`row.getValue()`），且方法不会出现在`Object.keys()`或浅拷贝中。
- 🧩 **动态特性系统**：采用手动原型而非 JavaScript 类，因为表格功能（排序、筛选、分页等）需动态组合，类继承难以灵活适配不同功能组合。
- 📈 **扩展性提升**：V9 最大可处理 1000-1600 万行数据（4GB 内存限制），而 V8 仅约 100 万行，实现 10 倍扩展性提升。

---

### [Waku 的独特功能：切片](https://newsletter.daishikato.com/p/waku-s-unique-feature-slices)

**原文标题**: [Waku’s Unique Feature: Slices](https://newsletter.daishikato.com/p/waku-s-unique-feature-slices)

概述总结
- 🧩 Waku 框架的 Slices 功能是受 Gatsby 的 Slice API 启发而创建的独特特性
- 📁 Slices 是位于`src/pages/_slices`目录下的可重用组件，文件路径即为其 ID
- ⚙️ 每个 Slice 可独立配置渲染方式（如静态渲染），通过`getConfig`函数定义
- 🔗 使用`Slice`组件按 ID 引用 Slice，但必须在页面配置中显式列出所用 Slice
- 🚀 Lazy Slices 支持懒加载，独立于页面加载，类似 Astro 的服务器岛屿，无需在页面配置中列出
- 💡 Slices 支持静态/动态组合（如静态页面中使用动态 Slice），概念简单且符合 Waku 的极简哲学

---

### [迁移到 Next.js 应用路由器后，慢响应减少了 80% - DEV 社区](https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da)

**原文标题**: [How We Cut Slow Responses by 80% Migrating to Next.js App Router - DEV Community](https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da)

Subito 通过迁移到 Next.js App Router，将慢响应减少了约 80%，同时提升了 SEO 性能。

- 📉 **慢响应大幅减少**：迁移后，超过 250ms 的响应比例从 25-40% 降至接近零，视频游戏类别页面加载速度提升近 30%。
- 🚀 **增量迁移策略**：采用并行路由，让 Pages Router 和 App Router 共存，开发者无需冻结产品开发，客户端组件可被两版复用。
- 🧩 **解决 410 状态码问题**：通过自定义 Express 服务器拦截响应，在 App Router 不支持 410 时，确保过期广告正确返回“已删除”状态。
- 🌐 **HTML 流式传输挑战**：需关闭 Nginx 和 Akamai 的缓冲，配置分块传输编码，才能实现骨架屏即时显示和内容流式加载。
- 📊 **SEO 安全分阶段部署**：先迁移路由（关闭流式），再逐步启用流式，每个类别监控两周 SEO 指标，确保无负面影响。
- 💻 **单人高效完成**：迁移主要由一名开发者在日常功能开发间隙完成，借助 Claude Code 加速规划与实现。
- ⚙️ **自定义服务器层优势**：Express 提供按请求路由控制、渐进式发布开关，并解决框架限制（如 410 状态码），无需等待上游修复。

---

### [React 应用中的组件通信模式 — Neciu Dan](https://neciudan.dev/component-communication-patterns-in-react)

**原文标题**: [Component Communication Patterns in React Applications — Neciu Dan](https://neciudan.dev/component-communication-patterns-in-react)

本文概述了 React 应用中组件通信的不同模式，从最简单的父子组件通信到复杂的全局事件驱动通信，并提供了如何根据组件距离和数据类型选择合适模式的实用指南。

- 📡 **Props 和回调**：最直接的父子组件通信方式，数据通过 props 向下传递，通过回调向上传递，适用于组件距离近的场景。
- 🗺️ **状态提升**：当兄弟组件需要共享状态时，将状态提升到最近的共同父组件中管理。
- 🧩 **组合模式**：通过将组件作为 children 传递，避免不必要的 prop drilling，让数据直达需要的组件。
- 📍 **状态就近放置**：将状态放在最接近使用它的组件中，避免不必要的全局状态和性能问题。
- 🎮 **命令式调用**：使用`ref`和`useImperativeHandle`让父组件直接调用子组件的方法，适用于“做某事”而非“共享数据”的场景。
- 🌐 **Context**：适用于全局但变化不频繁的值（如主题、用户），但要注意性能陷阱——所有消费者在值变化时都会重新渲染。
- 🗄️ **全局状态管理库**：当 Context 不够用时，使用 Zustand、Jotai 或 Redux Toolkit 管理频繁变化的全局状态，并支持精确的组件级订阅。
- 🖥️ **服务端状态**：使用 TanStack Query 管理来自服务器的数据，自动处理缓存、加载、错误和重新获取，避免将服务端数据混入客户端状态管理。
- 🔗 **URL 状态**：将描述当前视图的状态（如筛选、分页）放入 URL，实现可分享、可刷新、支持浏览器前进后退。
- 📢 **事件驱动通信**：使用发布 - 订阅模式（如 EventTarget 或自定义事件总线）处理跨组件、无关联的“事件”通知（如 toast），但应作为最后手段使用。
- 🧠 **选择指南**：始终从最接近的通信方式开始（props），只有当问题明确需要时才向外扩展，避免过度使用全局工具。

---

### [修复 React Native 应用：不要让 Bug 滋生 | Sentry](https://sentry.io/resources/react-native-workshop-2026/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=mobile-fy27q2-reactnativeworkshop&utm_content=newsletter-react-link-simon-grimm-register)

**原文标题**: [Fixing React Native Apps: Don't Let Bugs Crop Up | Sentry](https://sentry.io/resources/react-native-workshop-2026/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=mobile-fy27q2-reactnativeworkshop&utm_content=newsletter-react-link-simon-grimm-register)

概述摘要  
- 🛠️ 参与 Simon Grimm 主持的互动工作坊，学习如何监控和调试生产环境中的 React Native 应用  
- 🔍 通过堆栈跟踪、面包屑、日志、标签、重放和 Seer 工具，从警报到假设逐步排查真实生产崩溃  
- 📊 为尚未发现的错误埋点，决定记录、标记或追踪哪些数据  
- 📈 构建发布次日早晨即可提供关键信息的生产仪表盘  
- ⚠️ 设置监控和警报，在用户报告前捕捉问题，同时避免警报疲劳  
- 🎯 无论开发游戏、应用还是面向真实用户的产品，都能获得实用的生产监控框架  
- 🎧 推荐收听 Syntax 播客，获取更多开发者见解

---

### [React Router v8 | Remix](https://remix.run/blog/react-router-v8)

**原文标题**: [React Router v8 | Remix](https://remix.run/blog/react-router-v8)

## 概述总结

React Router v8 发布，主打"最无聊"的升级体验，采用年度主版本发布计划，并宣布 v6 和 Remix v2 停止维护。

- 🎉 **React Router v8 正式发布** - 采用年度主版本发布计划，追求"最无聊"的升级体验
- 📦 **v7 回顾** - 引入框架模式，支持类型安全路由模块 API、智能代码分割、多种渲染策略
- 🚀 **40+ 次更新** - 包括中间件、路由模块拆分、类型安全 href、性能优化等众多新特性
- 🔧 **破坏性变更极少** - 最低支持 Node 22.22+、React 19.2.7+、Vite 7+，采用 ESM-only 模块
- 🗑️ **废弃项清理** - 移除 react-router-dom、data 参数、Cloudflare 代理等
- ⬆️ **升级指南** - 更新依赖、采用未来标志、移除废弃 API，然后执行 pnpm i react-router@latest
- 📅 **未来规划** - 年度主版本发布，v6 和 Remix v2 正式停止维护
- 🔮 **Server Components 支持** - 仍在开发中，不稳定但已有模板和文档
- 🏗️ **Remix 新方向** - React Router 作为元框架，Remix 转向零依赖全栈框架
- 💡 **设计理念** - 少即是多、专注路由和数据、简单迁移路径、最低通用模式

---

### [GitHub - aidenybai/cnfast: `cn` 的快速替代方案](https://github.com/aidenybai/cnfast)

**原文标题**: [GitHub - aidenybai/cnfast: Fast drop in replacement for `cn` · GitHub](https://github.com/aidenybai/cnfast)

cnfast 是一个比 tailwind-merge 快 3.8 倍的 cn 函数替代品，兼容现有 API，无需修改代码即可提升性能。

- ⚡ 平均速度快 3.8 倍，组件密集型场景最高快 7 倍，输出字节完全相同
- 📦 通过 `npx cnfast migrate` 一键迁移 clsx、classnames 或 tailwind-merge 项目
- 🎨 支持 shadcn/ui 集成，通过 `npx shadcn@latest add aidenybai/cnfast/cn` 快速替换
- 🔧 提供标签模板语法，缓存调用站点身份，重复渲染时速度提升 4.3 倍
- 📊 在 65 个工作负载中几何平均速度提升 3.8 倍，113,291 个真实调用组中零不匹配
- 💡 包体积 9.43 KB（gzip），略高于 tailwind-merge 的 8.45 KB，但性能优势显著
- 🧩 导出 clsx、twMerge 和 twJoin，兼容现有代码库
- 📜 基于 MIT 许可证，改编自 clsx 和 tailwind-merge 的代码

---

### [发布 0.19.0 | StyleX](https://stylexjs.com/blog/v0.19.0)

**原文标题**: [Release 0.19.0 | StyleX](https://stylexjs.com/blog/v0.19.0)

本摘要概述了 StyleX v0.19.0 版本的主要更新内容，包括新包发布、ESLint 兼容性改进以及多项修复和优化。

- 🚀 **新包@stylexjs/atoms**：提供简洁的内联原子样式写法，编译后与`stylex.create`输出一致，支持静态属性访问和动态函数调用，并保持与现有 StyleX 样式的去重和合并语义。
- 🔧 **ESLint 更新**：StyleX v0.19 兼容 ESLint 10，新增`gap`自动修复功能，优化`legacy-expand-shorthands`样式解析，并扩展`textWrap`校验器以接受`pretty`和`stable`新值。
- 🐛 **修复与优化**：修复 JSX `sx`属性的运行时注入、伪元素与伪类组合时的选择器排序、别名主题文件解析、`sort-keys`自动修复顺序，以及媒体查询解析中的括号问题。

---

### [v1.6.0 · 基础用户界面](https://base-ui.com/react/overview/releases/v1-6-0)

**原文标题**: [v1.6.0 · Base UI](https://base-ui.com/react/overview/releases/v1-6-0)

## 总体概述

v1.6.0 版本于 2026 年 6 月 18 日发布，主要包含多个组件的问题修复和功能改进，涉及通用变更、无障碍优化、状态管理、表单验证、键盘导航和性能提升等方面。

- 🛠️ **通用改进**：修复了不准确的 prop JSDoc、更新 hook 值、恢复弹出窗口视口变形、修复伪元素边界问题
- 📱 **手风琴组件**：修复触发器行为错误、移除根元素区域角色、对齐 APG 键盘导航
- ⚠️ **警告对话框**：修复编程式焦点返回问题
- 🔍 **自动完成**：保留网格模式下输入光标的左右箭头功能、记录内联属性要求
- 👤 **头像组件**：修复图片状态边界情况
- ☑️ **复选框**：修复父组取消和不确定状态、忽略禁用时的聚焦属性、减少额外验证调用
- 🔲 **复选框组**：修复父组取消和不确定状态、自定义验证函数、多选框验证、转发组 ID
- 📂 **折叠面板**：修复触发器和面板状态错误
- 🔽 **组合框**：修复芯片上下文错误、保留输入光标箭头、优化键盘输入渲染、修复自动填充和选中状态
- 💬 **对话框**：修复确认焦点返回、编程式焦点返回、定位和视口边界情况、非模态焦点管理
- 🎨 **抽屉组件**：修复确认焦点返回、优化滑动关闭性能、原生驱动滑动手势、添加虚拟键盘支持
- 📝 **字段组件**：修复表单验证错误、反映禁用状态到标签和描述、修复值缺失重新验证
- 🏷️ **字段集**：修复禁用字段集的表单错误
- 📋 **表单组件**：修复表单验证错误
- 📑 **菜单组件**：修复子菜单触发器交互、悬停延迟打开、控制悬停关闭、定位和视口边界
- 📊 **计量表**：同步值文本与指示器
- 🧭 **导航菜单**：控制时保留退出过渡、修复交互和样式钩子错误
- 🔢 **数字字段**：处理不可读剪贴板粘贴、修复提交值和键盘步进、尊重 Intl 舍入选项、修复格式化缓存、保留数值精度
- 🔑 **OTP 字段**：重大变更：命名空间导出重命名、避免密码管理器弹出
- 🗨️ **弹出框**：修复控制悬停关闭、编程式焦点返回、定位和视口边界、非模态焦点管理
- 🃏 **预览卡片**：修复控制悬停关闭、定位和视口边界、保持内联预览锚定、触发器卸载时关闭
- 🔘 **单选组**：转发组 ID、修复空格键选择、禁用选中表单提交、尊重取消值更改
- 📜 **滚动区域**：修复溢出和滚动状态、添加拇指滚动状态
- 📋 **选择组件**：修复自动填充和选中状态、多选模式脏状态清除、跳过禁用项类型查找
- 🎚️ **滑块**：减少额外验证调用、修复交互边界情况、修复触摸事件监听泄漏
- 🔄 **开关**：减少额外验证调用
- 📑 **标签页**：修复状态边界情况、修复挂起面板激活
- 🔔 **通知组件**：修复计时器和限制边界情况
- 🔄 **切换开关**：修复分组取消和文档注释
- 🔄 **切换组**：修复分组取消、移除无效无障碍属性、修复禁用状态和漫游焦点
- 🛠️ **工具栏**：不转发禁用属性到默认按钮、修复禁用状态和漫游焦点
- 💡 **工具提示**：修复定位和视口边界、修复提供者延迟组生命周期、重置卸载保护、触发器卸载时关闭

---

### [效果 | Remotion | 以编程方式制作视频](https://www.remotion.dev/docs/effects)

**原文标题**: [Effects | Remotion | Make videos programmatically](https://www.remotion.dev/docs/effects)

### 概述
Remotion 支持对基于 Canvas 的组件（如 `<Video>`、`<Img>` 等）应用视觉效果，可通过编程、交互或智能代理方式添加，并支持多种内置效果与自定义效果。

- 🎨 **支持组件**：效果适用于 `<Solid>`、`<Video>`、`<Img>`、`<CanvasImage>` 等组件。
- 🛠️ **三种添加方式**：编程（通过 `effects` 属性传入效果函数）、交互（在 Remotion Studio 中拖拽效果）、智能代理（安装 Remotion Skills 后通过提示添加）。
- 🔄 **多效果组合**：可同时应用多个效果，按指定顺序叠加。
- 🌈 **丰富效果库**：包括颜色调整（亮度、对比度、色相）、模糊与阴影（高斯模糊、投影）、变换（镜像、缩放）、扭曲（鱼眼、波浪）、风格化（像素化、浮雕）及生成类效果（网格线、光晕）等。
- 🖥️ **可视化编辑**：在 Remotion Studio 中选中组件后，可在时间线中调整效果参数并切换开关。
- 🔧 **自定义效果**：使用 `createEffect()` 创建自定义效果，支持 2D Canvas、WebGL2 和 WebGPU。

---

### [v1.19.0 | React Aria](https://react-aria.adobe.com/releases/v1-19-0)

**原文标题**: [v1.19.0 | React Aria](https://react-aria.adobe.com/releases/v1-19-0)

v1.19.0 版本发布，新增对 GridList 和 Tree 中嵌入文本字段等交互元素的全键盘导航支持，Autocomplete 和 Popover 获得内联补全改进，Menu 的 onAction 回调现在提供键和值，DragTypes.has() 支持多 MIME 类型和通配符。同时包含破坏性变更和多项修复。

- 🚀 **GridList 和 Tree**：新增 `keyboardNavigationBehavior` 属性，支持行内文本字段等交互元素的全键盘导航
- ✨ **Autocomplete**：修复 CJK 输入法下虚拟焦点未应用于首个匹配项的问题，并添加内联补全示例文档
- 📌 **Popover**：新增 `getTargetRect` 属性，支持相对于文本字段中任意字符位置定位覆盖层
- 🧩 **Menu**：`onAction` 回调现在同时提供项的 `key` 和 `value` 作为参数
- 🖱️ **拖放**：`DragTypes.has()` 现在接受多个 MIME 类型和通配符模式（如 `image/*`）
- ⚠️ **破坏性变更**：`@react-aria/optimize-locales-plugin` 升级至 v2.0.0，以支持 Node 26，需注意 webpack 4 兼容性
- 🛠️ **通用修复**：修复 `isFocusable` 在脱离文档节点上的崩溃、测试环境中 `HTMLElement.prototype.focus` 的 getter 问题，以及优化树摇和 Node 26 兼容性
- 📅 **日历**：修复 CalendarYearPicker 中 `maxValue` 年份未被包含在可选范围内的问题
- 🎨 **Tailwind CSS**：支持 `not-*` 变体在 `tailwindcss-react-aria-components` 中

---

### [发布版本 7.80.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.80.0)

**原文标题**: [Release Version 7.80.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.80.0)

概述摘要
- 🧄 新增功能：`useFieldArray` 支持禁用字段（#13535），字段对象现在包含 `disabled` 属性
- 🛺 性能优化：提升 react-hook-form 的整体性能（#13524）
- 🐞 修复缺陷：`deepEqual` 函数中，空数组和空普通对象不应被视为相等（#13533），感谢 @JSap0914 的贡献
- ❤️ 社区反响：获得 5 个爱心表情和 1 个火箭表情的积极反馈

---

### [ForesightJS](https://foresightjs.com/)

**原文标题**: [ForesightJS](https://foresightjs.com/)

## 概述总结
ForesightJS 是一款智能预取工具，通过预测用户意图在内容被需要前进行预加载，支持桌面端和移动端的不同策略，并提供完整配置与调试功能。

- 🖱️ **鼠标轨迹预测**：分析光标移动模式，预判用户即将点击的链接并提前加载内容
- ⌨️ **键盘导航预取**：监测 Tab 键使用，在用户距离注册元素 N 个 Tab 时触发预取
- 📜 **滚动方向预取**：根据滚动方向预判用户将到达的元素并提前加载
- 📱 **触控设备支持**：提供视口进入和触摸开始两种预取策略（v3.3.0+）
- 🎮 **实时调试工具**：官方开发工具可可视化预测触发过程，支持鼠标/滚动/Tab 操作
- ⚡ **高性能架构**：基于事件驱动，无轮询、无重排，优化性能表现
- 🛠️ **多框架支持**：提供 JavaScript、React、Vue 快速集成方案（5 分钟内完成）
- 🔍 **完整预测类型**：支持鼠标、键盘、滚动、触控四种用户意图检测
- 📦 **TypeScript 支持**：开箱即用的完整类型安全
- 📚 **丰富文档资源**：提供完整文档和移动端支持说明

---

### [PolyCSS - 面向 DOM 的 CSS 3D 引擎](https://polycss.com/)

**原文标题**: [PolyCSS - CSS 3D Engine for the DOM](https://polycss.com/)

PolyCSS 让你在 DOM 中渲染带纹理的 3D 网格，无需 WebGL 或 Canvas，每个多边形都是一个真实的 DOM 元素。

- 🎨 支持 OBJ、glTF、GLB 和 MagicaVoxel VOX 格式，包括 UV 纹理和材质颜色
- 🧩 兼容 vanilla JS、React 和 Vue，提供自定义元素和框架绑定
- 📦 可通过 npm 或 CDN 安装，如 `npm install @layoutit/polycss`
- 🔧 每个多边形独立可寻址，支持点击处理、CSS 类和过渡动画
- 🌐 使用 `transform: matrix3d(...)` 定位多边形，浏览器合成器处理 3D 分层
- 🚀 提供 `<poly-camera>`、`<poly-scene>`、`<poly-mesh>` 等自定义元素和 API
- 📖 包含 Hello World 示例，支持轨道控制、旋转和颜色设置

---

### [React Hooks 本质上就是一个链表 - YouTube](https://www.youtube.com/watch?v=FneS7tCWBMU)

**原文标题**: [React Hooks Are Just a Linked List - YouTube](https://www.youtube.com/watch?v=FneS7tCWBMU)

本頁面概述了 YouTube 平台的相關資訊與政策，包括版權、聯絡方式、創作者支援、廣告、開發者條款、隱私與安全，以及平台運作方式與測試新功能等。

- 📰 **新聞中心**：提供 YouTube 的最新消息與官方公告。
- ©️ **版權**：說明版權相關規範與權利保護機制。
- 📞 **聯絡我們**：列出與 YouTube 團隊聯繫的方式。
- 🎥 **創作者**：為內容創作者提供資源與支援。
- 📢 **刊登廣告**：介紹在 YouTube 上投放廣告的選項。
- 👨‍💻 **開發人員**：提供 API 與開發工具資訊。
- 📜 **條款**：包含使用 YouTube 服務的條款與條件。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋平台安全規範與內容政策。
- ⚙️ **YouTube 的運作方式**：解釋平台功能與推薦系統。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新特性。
- 📅 **© 2026 Google LLC**：版權歸屬與年份標示。

---

### [Next.js 16.3 变得不错（如果你在意的话） - YouTube](https://www.youtube.com/watch?v=cSDKkD_6kCo)

**原文标题**: [Next.js 16.3 got good (if you care) - YouTube](https://www.youtube.com/watch?v=cSDKkD_6kCo)

本頁面列出了 YouTube 平台相關的資訊與政策連結，包括版權、聯絡方式、創作者資源、廣告、條款、隱私及安全等核心內容。
- 📰 新聞中心：提供最新平台動態與公告
- ©️ 版權：說明內容使用與版權相關規範
- 📞 聯絡我們：提供與 YouTube 團隊聯繫的管道
- 🎬 創作者：為內容創作者提供的資源與支援
- 📢 刊登廣告：介紹廣告投放選項與合作方式
- 👨‍💻 開發人員：提供 API 與開發工具資訊
- 📜 條款：列出服務使用條款與條件
- 🔒 私隱：說明個人資料保護與隱私權政策
- 🛡️ 政策及安全：涵蓋社群規範與安全措施
- ⚙️ YouTube 的運作方式：解釋平台推薦與審核機制
- 🧪 測試新功能：預告正在測試中的新功能
- ©️ 2026 Google LLC：版權歸屬與法律聲明

---

### [使用 Sebastian Lorber 大规模发布新闻通讯（本周 React）| RSS 策展、获取、RSC - YouTube](https://www.youtube.com/watch?v=YVs2KWvMjLM)

**原文标题**: [Newsletters at Scale with Sebastian Lorber (This Week in React) | RSS Curation, Acquisition, RSC - YouTube](https://www.youtube.com/watch?v=YVs2KWvMjLM)

本頁面列出了 YouTube 平台相關的資訊與政策連結，涵蓋法律、創作與營運等面向。

- 📄 **版權與條款**：提供版權資訊、服務條款及私隱政策，保障使用者權益。
- 🔒 **安全與政策**：包含平台安全規範、政策說明及運作方式，確保使用環境安全。
- 👤 **創作者與廣告**：為創作者提供資源，並說明廣告刊登選項。
- 📞 **聯絡與開發**：提供聯絡方式、新聞中心及開發者相關資訊。
- 🆕 **功能與測試**：介紹 YouTube 運作方式及新功能測試。
- © **版權所有**：標示 © 2026 Google LLC，確認版權歸屬。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=2nd)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=2nd)

该平台通过自动化测试工具帮助开发者高效交付可靠代码，无需手动编写或维护测试用例。

- 🚀 自动化测试：无需开发者编写或维护测试，工具自动生成并更新测试用例
- 🎯 零干扰集成：通过添加脚本标签即可记录开发环境交互，支持本地、预览和生产环境
- 🧠 AI 驱动测试：AI 引擎持续分析代码分支，生成覆盖所有用户流程和边缘情况的测试套件
- ⚡ 快速反馈：模拟后端响应，避免数据变更导致的误报，测试结果可在 120 秒内返回
- 🔒 确定性执行：基于 Chromium 的确定性调度引擎，彻底消除测试不稳定问题
- 📊 广泛兼容：支持 NextJS、React、Vue、Angular 等主流框架，可补充或替代现有测试套件
- 🏢 企业级验证：已获 Dropbox、Notion 等 100+ 组织信任，开发者反馈“无法想象没有它的工作”

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

该产品提供了一种革命性的自动化测试解决方案，让开发者无需编写或维护测试代码，即可实现全面、无干扰的回归测试。

- 🚀 **零开发者工作量**：自动记录开发中的用户交互，AI 生成并持续更新测试用例，覆盖所有代码分支和边缘情况。
- 🔬 **彻底且无干扰**：通过确定性调度引擎从底层消除测试不稳定问题，并模拟后端响应，避免假阳性结果。
- ⚡ **高速迭代**：测试高度并行化，可在 120 秒内完成数千屏幕的测试，支持快速发布可靠代码。
- 🛡️ **无缝集成**：支持 NextJS、React、Vue 等主流框架，只需添加脚本标签即可在开发、预览和生产环境中运行。
- 🌟 **业界认可**：被 Dropbox、Notion 等企业采用，工程师称赞其“无需调试、零维护、无干扰”，是软件开发的关键防护栏。
- 💡 **灵活使用**：可补充或替代现有测试套件，自动适应应用演进，无需手动更新测试。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

Meticulous 是一款无需开发者编写代码即可自动生成全面、确定性测试的自动化测试工具，专为复杂代码库设计，能极大提升代码发布速度并消除测试中的不稳定因素。

- 🚀 **零开发工作量**：自动记录开发者日常操作，AI 引擎生成覆盖所有代码分支和用户流程的测试套件，无需手动编写、修复或维护测试。
- 🔍 **全面且确定性的验证**：通过模拟后端响应，实现无副作用测试，消除因数据变化导致的误报，无需设置特殊测试账户或模拟数据。
- ⚡ **闪电般快速测试**：测试在计算集群上高度并行化，可在 120 秒内完成数千个屏幕的测试，并集成到 CI 流程中，在合并前预览变更影响。
- 🛡️ **从底层消除测试不稳定**：基于 Chromium 构建的确定性调度引擎，从根源杜绝测试不稳定，且测试速度极快，适用于最复杂的应用。
- 🔄 **测试自动进化**：测试套件随应用演变自动更新，自动添加新测试并移除过时测试，确保测试始终完整且最新。
- 🏢 **受众多组织信赖**：包括 Dropbox、Notion、Engine 等知名企业，开发者反馈“立即爱上，无法想象没有它的工作”。
- 🧩 **灵活集成**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流框架，可补充或替代现有测试套件。
- 🔒 **安全与集成**：提供详细文档，通过添加脚本标签即可快速开始，记录开发、预发布和生产环境中的会话。

---

### [我们把 PostHog 放进 Slack，现在人人都是工程师 - PostHog](https://posthog.com/blog/slack-app-beta?utm_source=twir&utm_campaign=jun24)

**原文标题**: [We put PostHog in Slack and now everyone's an engineer - PostHog](https://posthog.com/blog/slack-app-beta?utm_source=twir&utm_campaign=jun24)

以下是您提供内容的摘要：

PostHog 推出了 Slack 应用，让任何人都能通过 @提及的方式，将小问题或功能请求直接转化为代码，从而将整个团队赋能为“工程师”。

- 🤖 **Slack 中的编码代理**：@PostHog 机器人可以理解问题，创建沙箱，编写代码，运行检查，并直接在你的 Slack 线程中提交拉取请求 (PR)。
- 🛠️ **赋能非技术角色**：销售、市场和客户支持人员现在都可以通过简单的 @提及，修复 UI 小问题、添加功能或更新文档，无需编写代码。
- 📊 **数据驱动的上下文**：机器人会利用你的产品数据（如分析、会话回放）作为上下文来解决问题，而不是凭空猜测。
- ✅ **严格的审查流程**：机器人不会自行合并代码。它会处理代码审查意见、修复失败的 CI 检查，并持续跟进 PR，直到可以合并为止。
- 🧠 **智能任务分类**：并非所有 @提及都会生成代码。机器人会先判断请求是需要代码变更还是数据分析，并路由到正确的仓库。
- 📈 **实际应用案例**：从为网站添加“脚部照片”到为产品经理准备用户访谈简报，再到更新公司手册，机器人处理了各种任务。
- 🔄 **持续跟进**：机器人会“守护”其创建的 PR，处理故障和重试，直到 CI 通过，这通常比编写代码本身更耗时。
- 💡 **核心价值**：它弥合了“发现问题”和“解决问题”之间的鸿沟，将 Slack 从一个沟通工具转变为一个行动平台。

---

### [使用滤镜构建视频通话应用 — Margelo 博客](https://blog.margelo.com/building-videocall-app-with-filters)

**原文标题**: [Building a Video Call App with Filters — Margelo Blog](https://blog.margelo.com/building-videocall-app-with-filters)

### 概述摘要
本文详细介绍了如何利用 VisionCamera 和帧处理器在 React Native 中实现实时视频滤镜（如背景模糊、虚拟背景、人物居中、空中绘图），并将其无缝集成到 LiveKit 视频通话中，从而替代默认的相机功能，实现完全可编程的视频流。

- 📹 **核心思路**：用 VisionCamera 接管相机，通过原生引擎处理每一帧，再注入 LiveKit 的 WebRTC 视频源，实现滤镜效果，而不改变编码、传输和信令。
- 🔧 **后端简化**：使用 LiveKit 开源项目搭建后端，仅需两个路由（创建和加入房间），保持简单，专注于应用层开发。
- 📱 **基础视频通话**：使用 `@livekit/react-native` 和 `@react-native-vision-camera` 构建，但 LiveKit SDK 对相机控制有限，因此需要替换为 VisionCamera。
- 🔄 **帧注入机制**：通过替换 LiveKit 的相机捕获器，将 VisionCamera 的帧直接推入 WebRTC 视频源的 `onFrameCaptured`（Android）或 `didCaptureVideoFrame`（iOS）接口，实现帧流控制。
- 🎨 **滤镜实现**：所有滤镜（背景模糊、颜色/照片背景、人物居中、空中绘图）都基于相同的管道：转换帧 → 合成（混合背景、相机和遮罩）→ 推送。不同滤镜仅改变背景或遮罩的生成方式。
- 🧠 **性能优化**：遵循“不让相机等待”原则，将分割和面部检测等耗时操作放在独立线程上，使用“最新帧获胜”策略，确保视频帧率稳定。iOS 使用 GPU（Metal），Android 使用 CPU（Kotlin），未来可迁移到 NEON SIMD 或 GPU 着色器。
- 📊 **性能数据**：iPhone 13 在 GPU 下支持所有效果以 30 fps 运行；低端三星 Galaxy F14 在 CPU 下，轻量效果约 30 fps，复杂效果（如人物居中 + 分割 + 模糊）降至 15-20 fps。
- ✏️ **空中绘图**：通过 Skia 渲染手指笔触，并合成到帧上，使所有通话参与者实时看到绘图内容，实现共享白板功能。
- 🔓 **开源与未来**：将开源完整示例，方便克隆和尝试。新滤镜只需改变帧的填充或合成方式，核心管道已就绪。

---

### [为 React 编写自定义渲染器](https://www.callstack.com/blog/writing-custom-renderers-for-react)

**原文标题**: [Writing Custom Renderers for React](https://www.callstack.com/blog/writing-custom-renderers-for-react)

本文介绍了作者为 React Native Testing Library 构建自定义测试渲染器的原因、过程和经验教训。

- 🎯 **背景与动机**：React 19 弃用了 React Test Renderer (RTR)，迫使作者为 React Native Testing Library (RNTL) 寻找新方案，以维持轻量级、纯 JavaScript 的测试环境。
- 🤔 **三种备选方案**：作者考虑了编写新测试渲染器、使用 Fantom（React 内部测试渲染器）或转向设备/模拟器端到端测试，最终选择了构建新渲染器，因其能保留现有测试库的设计与兼容性。
- 🧩 **React 渲染器核心概念**：React 通过元素树、Fiber 树和平台视图树三层结构工作，由 React、Reconciler 和 Renderer 三个包协作，Renderer 通过 HostConfig 接口实现平台特定操作。
- 🔧 **新测试渲染器构建**：作者设计了简单的宿主实例树（容器、实例、文本实例），并实现了创建、添加、更新和删除等基本操作，利用 Reconciler 的通用逻辑简化开发。
- ⚡ **挑战与解决方案**：为支持 RNTL 的 Fire Event API（需访问复合元素 props），作者添加了 `unstable_fiber` 逃生舱口，以弥补新渲染器仅管理宿主元素树的限制。
- 💡 **经验教训**：构建渲染器让作者深入理解了 React 的树结构关系、HostConfig 的作用以及 React 版本与渲染器的紧密耦合，强调了 Reconciler 分离通用渲染逻辑的优势。

---

### [iOS 小组件和实时活动在 Expo SDK 56 中保持稳定](https://expo.dev/blog/ios-widgets-and-live-activities-in-expo)

**原文标题**: [iOS widgets and Live Activities are stable in Expo SDK 56](https://expo.dev/blog/ios-widgets-and-live-activities-in-expo)

概述摘要：本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了诊断辅助、药物研发和个性化治疗等关键方向，同时指出了数据隐私、算法偏见和监管挑战等核心问题。

- 🤖 人工智能在医疗影像分析中表现出色，能辅助医生更快速、准确地识别疾病，如癌症早期筛查。
- 💊 通过机器学习加速药物研发流程，可大幅缩短新药临床试验周期，降低研发成本。
- 🧬 基于患者基因组数据和病史的个性化治疗方案，能提升疗效并减少副作用。
- 🔒 医疗数据隐私保护是重大挑战，需建立严格的数据加密和匿名化处理机制。
- ⚖️ 算法偏见可能导致诊断结果不公平，需通过多样化训练数据和伦理审查来缓解。
- 📜 监管框架尚不完善，需平衡创新速度与患者安全，制定清晰的审批标准。

---

### [如何在 AI 应用开发中应用专业设计原则](https://expo.dev/blog/how-to-apply-professional-design-principles-in-ai-app-development)

**原文标题**: [How to apply professional design principles in AI app development](https://expo.dev/blog/how-to-apply-professional-design-principles-in-ai-app-development)

概述：本文探讨了人工智能在医疗诊断中的应用，强调了其提高准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🩺 人工智能可辅助医生分析医学影像，提升疾病早期检测的准确率。
- 📊 通过处理大量患者数据，AI 能识别模式并预测疾病风险，优化治疗方案。
- 🔒 数据隐私问题需重点关注，确保患者信息在 AI 系统中的安全使用。
- ⚖️ 算法偏见可能导致诊断不公，需通过多样化训练数据来缓解这一风险。
- 💡 AI 与医疗专家的协作模式，有望在减少误诊的同时提升医疗效率。

---

### [Drizz Vision AI 移动应用测试（iOS 与 Android）](https://www.drizz.dev/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=wave1_rn)

**原文标题**: [Drizz Vision AI Mobile App Testing for iOS & Android](https://www.drizz.dev/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=wave1_rn)

Drizz 是一个基于视觉 AI 的移动端测试自动化平台，已获 270 万美元种子轮融资，并登上福布斯。其核心价值在于用自然语言编写测试，通过 AI 实现自我修复，大幅降低传统自动化测试的脆弱性、维护成本和编写时间。

- 💰 **融资与认可**：Drizz 完成 270 万美元种子轮融资，并获福布斯报道。
- 🧠 **AI 驱动核心**：使用视觉 AI 技术，测试能像人类一样理解 UI，并具备自我修复能力，适应界面变化，无需手动维护。
- 📝 **自然语言编写**：支持用纯英文描述测试步骤，无需编程，几分钟内即可完成测试创建。
- 📱 **跨平台支持**：同时支持 Android 和 iOS 应用在真实设备上的自动化测试。
- ⚙️ **CI/CD 集成**：可无缝集成到 CI 管道中，提供可靠、可重复的测试执行。
- 🛡️ **企业级安全**：提供 SOC 2、HIPAA、GDPR 合规支持，支持本地部署和 VPC，确保数据安全。
- 📊 **显著效率提升**：测试编写速度提升 10 倍，测试总时间节省 25-30%，并将测试不稳定性从 15% 降至 5%。
- 🎯 **解决行业痛点**：针对传统工具（如 Appium）的高编写周期、高脆弱性和低覆盖率问题，提供有效解决方案。
- 🏢 **行业应用广泛**：适用于电商、金融科技、娱乐、导航、健康等多个行业，保障关键流程稳定。

---

### [发布 Reanimated - 4.5.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.5.0)

**原文标题**: [Release Reanimated - 4.5.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.5.0)

React Native Reanimated 函式庫發布了 4.5.0 版本，主要新增了 CSS 核心動畫支援更多屬性、偽選擇器、SVG 動畫以及新的共享轉場邊界元件，並修復了多項錯誤。

- 🎨 **CSS 核心動畫支援陰影、背景與邊框**：iOS 上可透過 `shadowColor`、`backgroundColor`、`borderColor` 等屬性實現流暢的 CSS 轉場動畫，需啟用 `IOS_CSS_CORE_ANIMATION` 功能旗標。
- 🖱️ **CSS 動畫新增偽選擇器**：支援 `:hover`、`:active` 和 `:focus`，並在 Apple、Android 及 Web 後端皆有實作。
- 🌐 **Web 支援 SVG 動畫**：`react-native-svg` 元件現在可在 Web 上進行 CSS 動畫。
- 🔲 **新增 SharedTransitionBoundary 元件**：可將共享元素轉場限制在特定子樹內，避免不同畫面間的轉場互相干擾。
- 🐛 **多項錯誤修復**：包含 iOS 雙重重載崩潰、Android ANR 死結、30fps 佈局動畫、記憶體洩漏等問題，並改善 CSS 樣式型別與建置流程。
- 🆕 **新貢獻者加入**：`finloop`、`sorinc03`、`audrius-savickas`、`kasperski95`、`enisdenjo`、`Warabi1915181` 和 `patrickwehbe` 首次貢獻程式碼。

---

### [发布 v2.0.0 · callstackincubator/voltra · GitHub](https://github.com/callstackincubator/voltra/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · callstackincubator/voltra · GitHub](https://github.com/callstackincubator/voltra/releases/tag/v2.0.0)

概述摘要  
- 🚀 Voltra v2.0.0 发布，重点引入重大架构变更，为未来功能奠定基础。  
- 📱 现在可在纯 React Native 项目中使用 Voltra，不再依赖 Expo 模块。  
- 🔧 代码已完全重构，采用 React Native 内置的 Turbo Modules。  
- 📦 Voltra 被拆分为多个小包，减少服务器安装时的移动端依赖。  
- 🔄 Live Activities 使用的 Voltra 协议未变，新旧版本均可正确解码同一负载。  
- ⚠️ 需要进行迁移，详情请参阅迁移指南。

---

### [发布 v0.85.0 · react/metro · GitHub](https://github.com/react/metro/releases/tag/v0.85.0)

**原文标题**: [Release v0.85.0 · react/metro · GitHub](https://github.com/react/metro/releases/tag/v0.85.0)

Metro v0.85.0 版本发布，包含多项重要更新和修复。

- 🚀 最低 Node.js 版本提升至 22（破坏性变更）
- ✨ 新增 `PACKAGE_SELF_RESOLVE` 功能，支持解析器中的自引用导入
- 🔧 修复所有 CommonJS `require` 调用的 ESM 解包问题
- 🖥️ 修复 Windows 跨驱动器路径解析问题
- 📦 修复嵌套和一级 `package.json` 的浏览器规范重定向问题
- 🚫 优雅拒绝浏览器规范中非法重定向到绝对路径的情况
- 🔒 修复传递依赖中的安全漏洞
- ⚡ 优化 `matchSubpathFromMainFields` 性能，解析器整体提升约 5%

---

### [发布 v1.14.0 · zykeco/react-native-ble-nitro · GitHub](https://github.com/zykeco/react-native-ble-nitro/releases/tag/v1.14.0)

**原文标题**: [Release v1.14.0 · zykeco/react-native-ble-nitro · GitHub](https://github.com/zykeco/react-native-ble-nitro/releases/tag/v1.14.0)

以下是您提供的 GitHub 发布说明的摘要：

概述摘要：react-native-ble-nitro v1.14.0 版本发布，主要新增了扫描结果中暴露广播服务数据的功能，并更新了相关类型定义。

- 📡 **新增服务数据暴露**：扫描结果现在通过`BLEDevice.serviceData`提供广播服务数据，包含`{ uuid, data }`列表，其中`data`为`ArrayBuffer`类型。
- 🍏 **跨平台支持**：该功能在 iOS（Core Bluetooth）和 Android 上均可使用，由@ps73 贡献（PR #21，解决 issue #20）。
- 🛠️ **技术细节更新**：在 Nitro 规范中新增了`ServiceData`和`ServiceDataEntry`类型，与现有的`ManufacturerData`结构保持一致。
- 🔄 **数据来源说明**：服务数据来自扫描期间的实时广播数据；对于已连接或恢复的外设（无广播数据），该字段为空。
- 📜 **完整变更日志**：涵盖从 v1.13.0 到 v1.14.0 的所有更改。

---

### [GitHub - EvanBacon/serve-sim: Apple 模拟器的`npx serve`。](https://github.com/EvanBacon/serve-sim)

**原文标题**: [GitHub - EvanBacon/serve-sim: The `npx serve` of Apple Simulators. · GitHub](https://github.com/EvanBacon/serve-sim)

serve-sim 是 Apple 模拟器的 `npx serve`，可在本地或远程主机上提供模拟器流媒体和控制功能，支持 AI 代理工具和开发服务器集成。

- 📱 **核心功能**：通过 `simctl io` 捕获模拟器帧缓冲，提供 60 FPS MJPEG 视频流和 WebSocket 控制通道，支持 iOS、iPad 和 Apple Watch
- 🖱️ **交互能力**：支持浏览器内滑动、捏合缩放、键盘快捷键、拖放文件、模拟按钮和手势操作
- 🎥 **摄像头注入**：通过 `serve-sim camera` 替换模拟器摄像头源，支持占位图、文件、网络摄像头，并可热切换源
- 🤖 **AI 代理集成**：提供 Agent Skill 技能包，支持 Claude Code、Cursor、Codex CLI 等工具直接驱动模拟器
- 🔌 **开发服务器嵌入**：提供 Connect 风格中间件，可集成到 Metro、Vite、Next 等服务器中，支持单端口代理和远程访问
- 🛠️ **安装与要求**：需要 macOS 14+、Xcode 命令行工具、Node.js 20+，仅支持 Apple Silicon (arm64)
- 📦 **CLI 命令丰富**：支持启动预览、发送手势、按钮、文本输入、旋转、摄像头操作、内存警告等多种命令

---

### [GitHub - watadarkstar/react-native-nsfw-detector: 一个用于 React Native/Expo的快速设备端AI图像安全检测器，使用CoreML模型检测图像中的裸露及不安全视觉内容。](https://github.com/watadarkstar/react-native-nsfw-detector)

**原文标题**: [GitHub - watadarkstar/react-native-nsfw-detector: A fast on device AI image safety detector for React Native / Expo using a CoreML model to detect nudity and unsafe visual content in images. · GitHub](https://github.com/watadarkstar/react-native-nsfw-detector)

这是一个基于 CoreML 的 React Native / Expo 图片安全检测库，用于在设备端快速检测 NSFW（不宜工作场合）内容。

- 🚀 利用 CoreML 在 iOS 设备上实现快速、离线的 AI 图片安全检测
- 📱 支持 React Native 0.70+ 和 iOS 13+，需 Xcode 10+ 编译
- ⚠️ 强烈建议在物理 iOS 设备上测试，模拟器检测精度显著降低
- 🛠️ 安装简单：`npm install react-native-nsfw-detector` 或 `yarn add react-native-nsfw-detector`
- 💻 提供简洁的 Promise API，示例代码可检测图片并输出安全/不安全结果
- 🔒 无需网络请求，所有推理在设备本地完成
- 📄 基于 MIT 许可证开源，由 Adrian 开发，灵感来自 LOVOO 的 NSFWDetector
- ⭐ 获得 27 颗星，0 个 fork，有 5 个发布版本

---

### [发布 v14.0.0 · react-native-webview/react-native-webview · GitHub](https://github.com/react-native-webview/react-native-webview/releases/tag/v14.0.0)

**原文标题**: [Release v14.0.0 · react-native-webview/react-native-webview · GitHub](https://github.com/react-native-webview/react-native-webview/releases/tag/v14.0.0)

该页面显示的是 react-native-webview 库的 v14.0.0 版本发布信息。

- 🚀 发布了 v14.0.0 版本，包含重要更新
- 📱 Android 最低支持版本提升至 API 24（Android 7.0 Nougat）
- 🗑️ 移除了旧版 Android 的原生文件上传路径和兼容代码
- ⚠️ 此版本包含破坏性变更（BREAKING CHANGES）
- 🔄 页面加载时出现错误，需重新加载

---

### [发布 0.4.0 版本 · AppAndFlow/react-native-transformer-text-input · GitHub](https://github.com/AppAndFlow/react-native-transformer-text-input/releases/tag/v0.4.0)

**原文标题**: [Release Release 0.4.0 · AppAndFlow/react-native-transformer-text-input · GitHub](https://github.com/AppAndFlow/react-native-transformer-text-input/releases/tag/v0.4.0)

以下是根据您提供的内容生成的摘要：

该页面为 react-native-transformer-text-input 库的 v0.4.0 版本发布页面，但加载时出现错误，需重新加载。页面显示该版本包含错误修复和新功能。

- 🐛 修复 Android 上 RN >= 0.84 的 JNI 构建问题（#8）
- 🌐 新增 TransformerTextInput 的 Web 支持（#12）
- 🔄 页面加载错误，需重新加载以查看完整标签和发布内容

---

### [发布 8.15.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.15.0)

**原文标题**: [Release 8.15.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.15.0)

### 概述总结
Sentry React Native 发布了 8.15.0 版本，包含新功能、修复和依赖更新。

- 🆕 **新增功能**：为 `NativeLinkedErrors` 添加 `nativeStackAndroid` 支持，捕获被拒绝的原生模块 Promise 的 JVM 堆栈跟踪作为链接异常。
- 📱 **移动端会话重放增强**：支持录制 XHR 请求/响应头部和可选正文，通过 `mobileReplayIntegration` 配置，需设置 `networkDetailAllowUrls` 和 `networkCaptureBodies: true`，自动过滤授权类头部，正文限制约 150 KB。
- ⚠️ **开发警告**：检测到多个 Sentry JS SDK 版本时发出警告。
- 🐛 **修复**：修复 Android 中同步带数字时间戳的面包屑到原生作用域时出现的 `ClassCastException`。
- 📦 **依赖更新**：Android SDK 升级至 v8.44.0，Cocoa SDK 升级至 v9.18.0，JavaScript SDK 升级至 v10.58.0，CLI 升级至 v3.5.1。

---

### [发布 Worklets - 0.10.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/worklets-0.10.0)

**原文标题**: [Release Worklets - 0.10.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/worklets-0.10.0)

以下是 react-native-reanimated 的 Worklets 0.10.0 版本发布摘要：

Worklets 0.10.0 版本发布，主要带来 Bundle Mode 稳定化、API 增强及多项修复。

- 🎉 **Bundle Mode 稳定化**：Bundle Mode 现被认定为稳定版本，推荐使用；旧版 Legacy Eval Mode 仍为默认启用。
- 🔄 **模块导入转发 API**：用更灵活的 `importForwarding` 替代了旧的 `workletizableModules` API，并提供了详细文档。
- 🚀 **原生 ArrayBufferView 序列化**：TypedArrays 等对象现在通过原生代码路径序列化，减少开销。
- 🛠️ **其他关键修复**：包括保留 JSX 导入、修复 Metro 配置、优化运行时测试、解决内存循环问题等。
- 👥 **新贡献者加入**：8 位新贡献者首次参与项目，贡献了多项修复和改进。

---

### [发布 · kuatsu/react-native-boost · GitHub](https://github.com/kuatsu/react-native-boost/releases)

**原文标题**: [Releases · kuatsu/react-native-boost · GitHub](https://github.com/kuatsu/react-native-boost/releases)

这是一个 React Native Boost 库的版本发布记录。以下是摘要：

React Native Boost 已稳定发布，包含多个版本的修复、新功能和性能改进。

- 🎉 v1.5.0 修复了嵌套优化错误，并新增了对 Unistyles v3 的支持。
- 🚀 v1.4.0 改进了文本无障碍属性和性能，如使用对象字面量替代 Object.assign。
- ⚡ v1.3.0 实现了文本样式的构建时内联，并修复了动态行数及用户选择属性问题。
- 🔧 v1.2.0 优化了视图和文本组件，新增了 FPS 基准测试和示例应用。
- 💪 v1.1.0 添加了 @boost-force 装饰器以强制优化。
- ✅ v1.0.0 正式稳定版，修复了基准测试和节点模块优化问题。
- 🛠️ v0.7.0 改进了属性处理和日志记录，并增加了未知祖先的退出机制。
- 📦 v0.6.2 修复了 React Native 0.79 的样式扁平化问题。
- 🔄 v0.6.1 重命名了运行时函数，并修复了类型错误。
- 🌐 v0.6.0 修复了 Web 打包问题，并将运行时库移至独立导入路径。

---

### [True Sheet 3.11 | React Native 真表单](https://sheet.lodev09.com/blog/release-3-11)

**原文标题**: [True Sheet 3.11 | React Native True Sheet](https://sheet.lodev09.com/blog/release-3-11)

True Sheet 3.11 版本发布，带来重大更新，包括 Web 渲染器重写、更清晰的展示 API、iOS 辅助功能改进和 Android 手势修复。

- 🌐 **全新 Web 渲染器**：基于 vaul 重写，取代@gorhom/bottom-sheet，提供与 iOS 和 Android 更一致的体验，支持所有原生功能、事件和堆叠。
- 🎨 **展示属性替换 pageSizing**：用更清晰的`presentation`属性（"page"或"form"）替代`pageSizing`布尔值，其中"form"模式忽略`maxContentWidth`。
- ♿ **iOS 辅助功能提升**：Sheet 内容、底部控件和覆盖层（如警告框、操作列表）现在可被 XCTest 和 VoiceOver 可靠访问，底部辅助功能在重装后依然有效。
- 🛠️ **Android 手势修复**：修复水平子手势被取消的问题，底部触摸在 ACTION_DOWN 时锁定，水平手势绕过 Sheet 拖动；Sheet 拖动不再窃取 TextInput 上的触摸，垂直子手势正确激活。
- 🐛 **更多错误修复**：包括 iOS Mac Catalyst 构建问题、底部视图渲染位置错误、Android resize() 中断问题、以及 Expo Router SDK 56 下的导航问题。

---

### [发布 v3.1.0 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.1.0)

**原文标题**: [Release v3.1.0 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.1.0)

该页面为 LegendApp/legend-list 的 v3.1.0 版本发布说明，包含多项新功能、修复和性能优化。

- 🚀 新增实验性 `experimental_adaptiveRender` 功能，支持列表在快速滚动时渲染轻量版本，滚动减慢后恢复
- 📏 新增 `setItemSize` 方法，允许直接更新已知项目的测量尺寸，适用于内容变化场景
- 🐛 修复 Web 端 `maintainVisibleContentPosition` 在头部变化、浏览器滚动锚定或动画 `scrollToEnd` 时的锚点保持问题
- 🔧 修复 `initialScrollIndex` 和 `initialScrollAtEnd` 在数据延迟加载时使用最新初始滚动参数，避免滚动到旧目标
- 🛠 修复更改 `gap` 属性后刷新缓存的项目测量值，并确保固定大小行包含间距
- 📋 修复 SectionList 在区块数据变化后粘性头部的更新问题
- ➡️ 修复水平列表在末端对齐时正确放置项目，而非忽略对齐设置
- ⏰ 修复列表卸载时清除定时器，防止延迟的适配渲染或滚动操作在列表消失后运行
- ⚡ 性能优化：首次渲染使用较小绘制距离，稍后扩展，减少初始内容出现前的离屏工作
- ⚡ 性能优化：`alignItemsAtEnd` 的间距更新减少 ScrollView 的重新渲染次数
- 📦 类型导出：从 React Native 和 Web 类型入口点导出 `AdaptiveRender` 和 `AdaptiveRenderConfig`

---

### [发布 v0.2.0 · software-mansion-labs/react-native-nano-icons · GitHub](https://github.com/software-mansion-labs/react-native-nano-icons/releases/tag/v0.2.0)

**原文标题**: [Release v0.2.0 · software-mansion-labs/react-native-nano-icons · GitHub](https://github.com/software-mansion-labs/react-native-nano-icons/releases/tag/v0.2.0)

react-native-nano-icons 发布 v0.2.0 版本，包含多项修复和新功能。

- 🛠️ 修复：多 info.plist 项目中的库兼容性问题
- ♿ 新增：无障碍属性支持
- 📱 修复：iOS 渲染错误
- 🔧 修复：RN <=0.79 版本中的代码生成类型别名解析
- 📦 优化：减少依赖包体积
- ⚡ 修复：iOS 增量构建问题
- 📺 新增：tvOS 支持
- 🔗 新增：动态字体链接（支持 OTA 更新）
- 🌐 新增：Web 专用 createIconSet 功能
- 👥 感谢贡献者：@lursz 和 @stachbial 的首次贡献

---

### [GitHub - hryhoriiK97/expo-paperkit: 适用于 Expo/React Native 的 Apple PaperKit · GitHub](https://github.com/hryhoriiK97/expo-paperkit)

**原文标题**: [GitHub - hryhoriiK97/expo-paperkit: Apple PaperKit for Expo/React Native · GitHub](https://github.com/hryhoriiK97/expo-paperkit)

expo-paperkit 是一个为 Expo/React Native 提供 Apple PaperKit 标记体验的库，支持在 iOS 和 macOS 上实现绘图、形状和注释功能。

- ✏️ 支持完整 PaperKit 绘图画布和 Apple Pencil 触控笔
- 🔶 可插入形状、文本框和箭头/线条
- 💾 支持保存和恢复标记数据（base64 序列化）
- 🖼️ 可将画布导出为 PNG 或 JPG 格式
- ↩️ 提供撤销和重做功能
- ⚙️ 可配置功能集、缩放和画布大小
- 🎨 集成 PKToolPicker（iOS）和 MarkupToolbar（macOS）
- 🏞️ 支持背景图像
- 👁️ 提供只读模式用于查看已保存的标记
- 📱 要求 iOS 26.0+、macOS 26.0+、Expo SDK 54+ 和 React Native 0.81+
- 🛠️ 需要原生代码，不支持 Expo Go
- 🚀 快速集成示例代码，包含保存和导出功能
- 📚 提供完整 API 文档和 MIT 许可证

---

### [发布 v1.13.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v1.13.0)

**原文标题**: [Release v1.13.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v1.13.0)

以下是您提供的文本内容的中文摘要：

页面加载时出现错误，提示重新加载。展示了开源项目“rozenite”的公共仓库页面，包含通知、分支、星标、代码、问题、拉取请求、讨论、操作、安全与质量、洞察等导航选项，以及最新发布版本 v1.13.0 的详细信息。

- 😱 页面加载错误，提示用户重新加载页面。
- 📂 项目“rozenite”为公开仓库，拥有 620 个星标和 46 个分支。
- 🚀 最新版本 v1.13.0 已发布，包含多项功能更新和修复。
- 🔧 主要更新包括：Redux DevTools 插件状态快照流式处理、WebSocket 来源对齐、Vite 插件开发导出修复、跟踪符号化、React 组件树代理工具等。
- 👥 新贡献者@michaelapollopimentel-svg 加入，贡献了 Vite 插件相关修复。
- 📝 完整更新日志涵盖 v1.12.0 至 v1.13.0 的变更，由 V3RON、draggie 和 michaelapollopimentel-svg 共同完成。

---

### [React Native Radio - RNR 366 - 在人工智能时代保护 React Native 应用](https://infinite.red/react-native-radio/rnr-366-securing-react-native-apps-in-the-ai-era)

**原文标题**: [React Native Radio - RNR 366 - Securing React Native Apps in the AI Era](https://infinite.red/react-native-radio/rnr-366-securing-react-native-apps-in-the-ai-era)

### 概述总结
本集播客探讨了 AI 时代 React Native 应用面临的新兴安全威胁，包括 TanStack 漏洞、GitHub 供应链攻击和恶意 React Native 包，并提供了实用的安全防护建议。

- 🎯 **AI 加速安全威胁**：AI 工具使攻击者能更快发现和利用漏洞，安全事件频率和严重性显著增加
- 🔒 **TanStack 攻击案例**：攻击者利用 GitHub Actions 的`pull_request_target`触发器和缓存投毒，20 分钟内污染了多个 npm 包
- 📦 **React Native 包被攻破**：`react-native-international-phone-number`和`react-native-country-select`等包被植入恶意预安装钩子，攻击者与维护者反复博弈
- ⚠️ **Metro 服务器漏洞**：React Native 的 Metro 暴露未认证的 URL 端点，允许命令注入，影响版本 4.8 至 20 alpha 2
- 🛡️ **依赖管理最佳实践**：设置最小发布年龄（如 24-48 小时）、使用自托管注册表、定期审计 VS Code 扩展和 GitHub 令牌
- 🔑 **应用安全要点**：使用安全存储（如 Keychain/Expo Secure Store）而非 AsyncStorage 或.env 文件；实施 SSL/TLS 证书固定；保持令牌短生命周期
- 🤖 **AI 代理安全**：使用 Agent Safe House 等工具限制 AI 代理权限，创建标准用户而非管理员账户进行开发
- 📋 **GitHub Actions 安全**：避免使用`pull_request_target`触发器，确保 CI/CD 工作流使用正确的权限设置

---

### [CSS 链接参数模块第一级](https://drafts.csswg.org/css-link-params-1/)

**原文标题**: [CSS Linked Parameters Module Level 1](https://drafts.csswg.org/css-link-params-1/)

本规范介绍了一种让外部 SVG 图像（如通过`<img>`或 CSS `url()`引用的图像）也能像内联 SVG 一样被 CSS 动态定制颜色的方法，通过“链接参数”实现。

- 🎨 **核心概念**：链接参数允许通过 CSS 属性或 URL 片段，向外部资源传递自定义环境变量（如`--color`），资源内部通过`env()`函数读取，实现动态样式。
- 🔧 **三种设置方式**：可通过 CSS 的`link-parameters`属性、URL 中的`param()`片段标识符、或 CSS `url()`中的`param()`修饰符来指定链接参数。
- 📦 **参数优先级**：当多种方式同时指定时，按`link-parameters`属性、URL 片段、`url()`修饰符的顺序合并，同名参数以最后出现的为准。
- 🌐 **在资源中使用**：外部资源（如 SVG）通过`env(--color, fallback)`访问参数，可设置默认值以确保无参数时仍可用。
- 🛡️ **安全与隐私**：该规范不引入新的隐私问题；安全方面，参数仅影响资源显式声明的 CSS 属性，降低了被恶意利用的风险。

---

### [交付策略，而非代码](https://www.jayfreestone.com/writing/share-the-policy-not-the-code/)

**原文标题**: [Ship the policy, not the code](https://www.jayfreestone.com/writing/share-the-policy-not-the-code/)

### 概述总结
本文探讨了在前后端分离架构中，如何避免业务规则（如订单取消条件）在两端重复实现导致的不一致问题，并提出了三种解决方案：共享代码、传输决策结果、传输策略本身。

- 📜 **问题核心**：前后端各自实现相同规则（如`canCancelOrder`），极易因版本不同步导致逻辑分歧。
- 🔗 **共享代码的局限**：即使使用 monorepo 或共享包，独立部署仍会导致版本差异；跨语言场景（如 Go+TypeScript）难以直接共享函数。
- 📦 **传输决策结果**：后端直接返回`allowedActions`等字段，前端仅渲染状态而非重新推导规则，避免重复逻辑。
- 🧠 **传输策略本身**：使用 CASL 权限库或 JSON Schema 等标准化格式，将策略序列化后传输，前后端共享稳定的评估器。
- ⚠️ **注意事项**：纯布尔值可能不够，需提供`disabledReasons`等上下文信息；复杂规则（如 zod schema）目前难以完全序列化。
- ✅ **核心原则**：无论如何，必须共享规则（代码或数据），避免同一领域规则在两端独立存在。

---

### [未找到标题](https://casl.js.org/v7/en/)

**原文标题**: [No title found](https://casl.js.org/v7/en/)

抱歉，我无法总结未提供的内容。请提供需要总结的文本，我将按照您要求的格式生成中文摘要。

---

### [Vite 8.1 发布！| Vite](https://vite.dev/blog/announcing-vite8-1)

**原文标题**: [Vite 8.1 is out! | Vite](https://vite.dev/blog/announcing-vite8-1)

Vite 8.1 正式发布，带来多项实验性功能与性能改进，旨在提升大型应用的开发体验。

- 🚀 **实验性打包开发模式**：针对大型应用，通过预打包模块实现约 15 倍启动加速和 10 倍页面重载加速，同时保持即时 HMR，解决无打包开发模式下的网络请求瓶颈。
- 🧩 **实验性 Chunk Import Map**：利用 import maps 避免哈希级联，提升缓存效率，减少因内容变更导致的连锁重新哈希。
- 🖥️ **Wasm ESM 集成支持**：可直接导入 `.wasm` 文件并调用导出函数，无需额外插件。
- 🎨 **更接近默认使用 Lightning CSS**：新增对外部 CSS 导入和插件文件依赖的支持，为下个主要版本默认切换做准备。
- 🔍 **import.meta.glob 忽略大小写匹配**：新增 `caseSensitive: false` 选项，支持不区分大小写的文件匹配。
- 🖼️ **自定义 HTML 元素与属性资源发现**：通过 `html.additionalAssetSources` 配置，支持自定义标签和属性的资源提取。

---

### [Astro 7.0 | Astro](https://astro.build/blog/astro-7/)

**原文标题**: [Astro 7.0 | Astro](https://astro.build/blog/astro-7/)

Astro 7 正式发布，专注于性能提升，包括 Rust 重写的编译器、更快的 Markdown 处理、新的渲染引擎，以及 Vite 8 和 Rolldown 打包器，构建速度提升 15-61%。此外，还引入了高级路由、路由缓存、CDN 缓存提供程序、AI 增强功能（如后台开发服务器和 JSON 日志记录）。

- 🚀 **性能大幅提升**：Rust 重写的 `.astro` 编译器和 Markdown/MDX 处理管道，结合 Vite 8 的 Rolldown 打包器，构建速度提升 15-61%，部分站点快两倍以上。
- ⚡ **Rust 编译器**：新编译器不再自动修正 HTML，采用 JSX 式严格错误处理，并优化空白符处理，构建速度提升约 6%。
- 📝 **Markdown & MDX 在 Rust 中**：默认使用 Rust 驱动的 Sätteri 处理器，内置 GFM、数学公式、标题 ID 等多项功能，无需额外插件，构建时间可减少一分钟以上。
- 🔄 **队列渲染**：新的队列式渲染引擎替代递归方法，速度提升约 2.4 倍，内存占用更少。
- 🗺️ **高级路由**：新增 `src/fetch.ts` 入口点，支持标准 fetch 处理程序模式，可完全控制请求管道，并与 Hono 兼容。
- 💾 **路由缓存**：稳定的平台无关缓存 API，支持 `Astro.cache.set()` 和 `cache.invalidate()`，可基于标签或路径清除缓存。
- 🌐 **CDN 缓存提供程序**：实验性支持 Netlify、Vercel 和 Cloudflare 的 CDN 缓存，将缓存指令推送到边缘网络。
- 🤖 **AI 增强**：后台开发服务器 (`astro dev --background`) 和 JSON 日志记录，优化 AI 编码代理的工作流程。
- 🛠️ **升级与社区**：使用 `@astrojs/upgrade` 升级，感谢所有贡献者，新版本带来更快、更智能的开发体验。

---

### [TypeScript 7.0 RC 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

**原文标题**: [Announcing TypeScript 7.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

TypeScript 7.0 RC 发布，基于全新 Go 语言构建，速度提升约 10 倍，并带来大量新特性和改进。

- 🚀 **性能飞跃**：TypeScript 7.0 将代码库从 TypeScript 移植到 Go，利用原生速度和共享内存并行，速度比 6.0 快约 10 倍。
- 🔧 **安装与试用**：可通过 `npm install -D typescript@rc` 安装，或安装 VS Code 的 `TypeScript Native Preview` 扩展在编辑器中体验。
- 🔄 **与 6.0 并行运行**：提供 `@typescript/typescript6` 包，通过 npm 别名可让 7.0 和 6.0 并存，避免冲突。
- ⚙️ **并行化控制**：新增 `--checkers`（默认 4）和 `--builders` 标志，可分别控制类型检查和工作区构建的并行度，并支持 `--singleThreaded` 单线程模式。
- 👁️ **改进的 --watch 模式**：基于 Parcel 文件监听器移植到 Go，提供高效稳定的跨平台文件监控，显著降低资源消耗。
- 📋 **6.0 新默认值**：7.0 采用 6.0 的默认设置，如 `strict: true`、`module: esnext`、`target` 为当前稳定 ES 版本等，并废弃了 ES5、AMD 等旧选项。
- 🧩 **模板字面量类型改进**：现在正确处理 Unicode 码点，不再将表情符号拆分为代理对，行为更符合直觉。
- 📝 **JavaScript 支持重构**：统一了 JS 和 TS 文件的分析方式，废弃了 `@enum`、`@class` 等 JSDoc 模式，并更新了类型推断规则。
- 🖥️ **编辑器体验提升**：基于 LSP 构建，支持多线程处理请求，新增语义高亮、排序导入、移除未用导入等功能，命令失败率降低 20 倍以上。
- 🗓️ **发布计划**：RC 版已可用，稳定版预计一个月内发布，后续 7.1 将提供稳定 API。

---

### [介绍 Nub：Node.js 的一体化工具包 — Nub](https://nubjs.com/blog/introducing-nub)

**原文标题**: [Introducing Nub: an all-in-one toolkit for Node.js — Nub](https://nubjs.com/blog/introducing-nub)

### 概述摘要
Nub 是一个基于 Rust 构建的 Node.js 一体化工具包，旨在增强而非替代 Node.js，提供 TypeScript 运行、脚本执行、包管理等功能，同时保持与现有生态系统的兼容性。

- 🚀 **核心定位**：Nub 通过 Rust CLI 增强 Node.js，而非替代它，支持 TypeScript 文件直接运行、脚本执行和二进制工具调用，性能远超传统工具（如 `pnpm run` 快 24 倍，`npx` 快 19 倍）。
- 🛠️ **全能工具**：整合 `node`、`npm run`、`npx` 等功能，支持 TypeScript 编译、依赖安装、版本管理、文件监听等，无需额外配置。
- ⚡ **高性能**：脚本执行（`nub run`）比 `pnpm run` 快 30 倍，二进制工具调用（`nubx`）比 `npx` 快 20 倍，TypeScript 文件运行比 `tsx` 快 2.9 倍。
- 🔧 **TypeScript 优先**：原生支持 TypeScript、JSX、装饰器、路径别名（`tsconfig.json#paths`），无需构建步骤，兼容 Node 不支持的非可擦除语法（如枚举、命名空间）。
- 🌐 **现代 API 支持**：内置 Web Worker、Temporal、URLPattern、WebSocket 等 API 的 polyfill 或标志注入，确保跨 Node 版本兼容性。
- 📦 **包管理**：兼容 pnpm、npm、Yarn 和 Bun 的锁文件，支持工作区、过滤器（`--filter`），默认启用安全策略（如阻止生命周期脚本、新版本冷却期）。
- 🔄 **零锁定**：无 Nub 专属 API 或配置，移除 Nub 后代码仍可正常运行，完全兼容现有 Node 生态。
- 🛡️ **安全默认**：安装时默认禁用生命周期脚本、阻止非注册表依赖、要求新版本发布 24 小时后才可使用，并提供 `paranoid` 模式强化安全。
- 🏗️ **版本管理**：自动从 `.node-version` 或 `package.json#engines` 解析 Node 版本，按需下载并缓存，无需手动管理。

---

### [v0.35.0 - 2026 年 6 月 10 日 | sharp](https://sharp.pixelplumbing.com/changelog/v0.35.0/)

**原文标题**: [v0.35.0 - 10th June 2026 | sharp](https://sharp.pixelplumbing.com/changelog/v0.35.0/)

v0.35.0 版本更新，包含多项重大变更、新功能和改进，重点在于提升性能、稳定性和兼容性。

- 🔥 重大变更：停止支持 Node.js 18，要求 Node.js >= 20.9.0；移除 `install` 脚本，需手动使用 WebAssembly 或从源码构建
- 🎨 图像质量改进：有损 AVIF 输出改用 SSIMULACRA2 的 `iq` 质量指标；新增 AVIF/HEIF 的 `tune` 选项控制质量度量
- 🚀 新功能：新增 `limitInputChannels`（默认值 5）、`keepGainMap` 和 `withGainMap` 处理 HDR JPEG 增益图、`toUint8Array` 输出可传输 TypedArray
- 🛠 性能和兼容性：升级 libvips v8.18.3 修复上游 bug；WebAssembly 二进制文件移除实验状态；新增 FreeBSD 预编译二进制
- 📦 弃用和移除：弃用 Windows 32-bit 预编译二进制；移除已弃用的 `failOnError`、`paletteBitDepth` 等属性；重命名 `format.jp2k` 为 `format.jp2`
- 🖼 元数据和格式：新增图像 MIME 类型到元数据；`trim` 操作添加 `margin` 选项；`withDensity` 设置 EXIF 密度；WebP 新增 `exact` 选项控制透明像素颜色
- 🔧 其他改进：确保 HEIF 主项目为默认页/帧；改进 `pkg-config` 路径发现；支持 ECMAScript 模块（ESM）；要求预编译二进制使用静态路径以辅助代码打包

---

### [考虑移除`@swc/core`的 postinstall 脚本 · 问题 #11898 · swc-project/swc · GitHub](https://github.com/swc-project/swc/issues/11898)

**原文标题**: [Consider removing the `@swc/core` postinstall script · Issue #11898 · swc-project/swc · GitHub](https://github.com/swc-project/swc/issues/11898)

swc 项目计划移除 @swc/core 的 postinstall 脚本，以应对 npm 可能的生命周期脚本变更，并改用运行时回退机制。

- 🎯 **背景与动机**：npm 正考虑将生命周期脚本（如 postinstall）改为 opt-in 模式，为防范供应链攻击并保持安装便捷性，swc 计划移除 postinstall 脚本。
- 🔄 **当前行为**：现有 postinstall 脚本会在安装时验证原生绑定是否可用，若不可用则尝试安装 @swc/wasm 作为回退，并输出诊断信息。
- 📦 **新方案**：移除 postinstall 脚本，将 @swc/wasm 设为 @swc/core 的依赖或可选依赖，在运行时优先加载原生绑定，失败时自动回退到 @swc/wasm。
- ⚠️ **影响一：安装体积增加**：即使未使用 @swc/wasm，它也会被安装，增加依赖树大小；在 Linux 上可能同时安装 musl 和 glibc 原生包，进一步增大体积。
- 🛠️ **缓解措施**：npm 10.3.0 引入的 libc 字段可帮助包管理器优化，减少不必要的原生包安装。
- 📉 **影响二：诊断信息丢失**：移除 postinstall 脚本后，安装时的原生绑定验证和诊断功能将失效，需通过运行时 API、独立命令或文档来提供等效诊断能力。

---

### [重新考虑移除 postinstall 脚本 · 问题 #4475 · evanw/esbuild · GitHub](https://github.com/evanw/esbuild/issues/4475)

**原文标题**: [Reconsidering the removal the postinstall script · Issue #4475 · evanw/esbuild · GitHub](https://github.com/evanw/esbuild/issues/4475)

概述摘要  
esbuild 用户提出重新考虑移除 postinstall 脚本的决定，因为 pnpm 和 npm 的默认行为已改变，可能导致安装失败。建议将包拆分为 esbuild（CLI）和 esbuild-lib（库）以简化迁移。

- 🔄 重新评估移除 postinstall 脚本的决定，因 pnpm 默认不安装带 postinstall 脚本的包，导致失败而非警告  
- 📉 npm 也将逐步跟进，使安装脚本变为可选（参考 RFC #868）  
- ⚠️ 对通过 tsx 等间接依赖 esbuild 的用户影响更大，直接安装者较易调整设置  
- 🧩 建议将 esbuild 拆分为两个包：esbuild（CLI）和 esbuild-lib（库），以简化变更

---

### [GitHub Actions checkout 更安全的 pull_request_target 默认设置 - GitHub 更新日志](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)

**原文标题**: [Safer pull_request_target defaults for GitHub Actions checkout - GitHub Changelog](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)

概述：GitHub Actions 的 `actions/checkout` 工具更新了默认安全设置，以防止常见的“pwn request”攻击，同时允许工作流选择退出保护。

- 🛡️ **默认安全强化**：`actions/checkout` v7 默认拒绝在 `pull_request_target` 和 `workflow_run` 工作流中从 fork 拉取请求检出代码，以防范常见攻击。
- ⚠️ **常见风险模式**：阻止使用 `ref: refs/pull/.../head` 或 `repository: ${{ github.event.pull_request.head.repo.full_name }}` 等不安全输入，防止恶意代码执行。
- 📅 **自动更新计划**：2026 年 7 月 16 日，保护将回溯至所有受支持的主要版本，浮动标签（如 `@v4`）会自动更新。
- 🔓 **可选退出机制**：通过添加 `allow-unsafe-pr-checkout` 输入可退出保护，但需谨慎评估安全风险。
- 🚫 **未覆盖范围**：其他事件类型（如 `issue_comment`）或手动 `git`/`gh` 命令仍可能引入风险，需额外审查。
- 📚 **更多资源**：建议阅读安全指南和文档，以安全使用 `pull_request_target` 事件。

---

