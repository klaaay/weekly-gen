### [](https://marmelab.com/atomic-crm/)

**原文标题**: [Atomic CRM](https://marmelab.com/atomic-crm/)

Atomic CRM 是一个面向开发者的开源 CRM 工具包，可构建契合公司愿景的个性化 CRM，兼具全功能、代码级定制、现代技术栈、AI 辅助与合规托管能力。

- 🧩 全功能 CRM：集中管理联系人、任务提醒、笔记、导入导出、交易管道和活动历史。
- 🚀 高级能力：支持 SSO、看板、邮件转笔记、联系人头像、API 集成、移动应用、MCP 服务器和国际化。
- 🎨 代码驱动定制：可自定义 UI、主题、组件、自定义页面和可扩展数据模型。
- 🛠️ 现代技术栈：基于 React、TypeScript、Shadcn UI、Tailwind CSS、shadcn-admin-kit、TanStack Query、Supabase 和 Postgres。
- 🤖 AI 辅助：内置 Claude Code 专用角色，开发者、审查者、测试者、文档者，用简单提示即可重塑 CRM。
- ⚡ 快速开始：克隆仓库、安装依赖、本地开发，并一行命令部署到 Supabase 和 GitHub Pages。
- 🏗️ 选择理由：强基础、完全开源、数据所有权、无限扩展，避免供应商锁定。
- 🔐 安全合规：Supabase 提供 SOC 2 Type II、ISO 27001、HIPAA 合规托管，并支持加密与行级安全。
- ☁️ 灵活托管：可使用 Supabase 多云管理，或自托管实现完全数据主权。
- 💰 定价：开源版免费自托管；Starter 25€/月；Team 50€/月且最受欢迎；Enterprise 支持定制。
- 👩💻 专家服务：提供 CRM 范围规划、定制开发、培训和代码审计。
- 📥 立即行动：克隆仓库，开始体验 Atomic CRM。

---

### [GitHub - marmelab/atomic-crm](https://github.com/marmelab/atomic-crm)

**原文标题**: [GitHub - marmelab/atomic-crm: A full-featured CRM built with React, shadcn/ui, and Supabase. · GitHub](https://github.com/marmelab/atomic-crm)

Atomic CRM 是 Marmelab 开源的完整 CRM 项目，基于 React、shadcn-admin-kit/shadcn/ui 和 Supabase 构建，提供在线演示，采用 MIT 许可证；仓库包含源码、文档、测试和 shadcn registry，目前约 1.2k stars、792 forks，适合本地运行、二次开发与组件同步。

- 📇 联系人管理：将所有联系人集中在一个易于访问的地方。
- ⏰ 任务与提醒：创建任务并设置提醒，避免错过跟进或截止日期。
- 📝 笔记与邮件捕获：记录重要信息；抄送 Atomic CRM 可自动将通信保存为笔记。
- 📊 销售管道：用 Kanban 看板可视化并跟踪交易。
- 🔄 导入导出：轻松将联系人移入或移出系统。
- 🔐 访问控制：支持 Google、Azure、Keycloak 和 Auth0 登录。
- 📜 活动历史与 API：查看聚合活动日志，并通过 API 与其他系统集成。
- 🛠️ 高度可定制：可添加自定义字段、更改主题、替换任意组件。
- 📦 更新机制：可通过 Atomic CRM shadcn registry 将最新组件更新拉取到 fork 中。
- 🧰 安装要求：需要 Make、Node 22 LTS 和 Docker（Supabase 依赖）。
- 🚀 本地运行：Fork 并克隆仓库后执行 `make install`、`make start`，访问 `http://localhost:5173/` 并创建首个用户。
- 🖥️ 后端服务：Supabase 面板 `localhost:54323`、REST API `127.0.0.1:54321`、附件存储、Inbucket 邮件测试 `localhost:54324`。
- 📚 文档：位于 `doc/` 目录，也可在线访问 `https://marmelab.com/atomic-crm/doc/`。
- ✅ 测试：`make test` 运行单元测试；`make test-e2e` 运行 e2e；CI 针对构建版应用运行，本地可用 `make start-e2e-ci` 后执行 `npx playwright test --ui`。
- 🧪 自定义测试：单元测试可放在 `src` 中，命名为 `*.test.tsx` 或 `*.test.ts`；e2e 测试放在 `./e2e`。
- 🧩 shadcn registry 用户：执行 `npx shadcn add https://marmelab.com/atomic-crm/r/atomic-crm.json -o -y` 获取更新，运行前先提交工作。
- ⚙️ shadcn registry 贡献者：`registry.json` 由 `scripts/generate-registry.mjs` 自动生成，CI/CD 负责构建发布；若遗漏变更需更新该脚本。
- 📜 许可证：MIT，由 Marmelab 提供。
- ⚠️ 页面提示：文本开头出现加载错误提示，建议重新加载页面。

---

### [](https://react.dev/blog/2026/09/09/react-19-3)

**原文标题**: [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3)

React 19.3 已发布到 npm，重点是将 View Transitions 和 Fragment Refs 从实验性 API 转为稳定，并带来 React DOM、React Server Components 的新能力与多项修复。

- 🚀 React 19.3 正式发布，`<ViewTransition>` 和 Fragment Refs 现已稳定可用。
- 🎞️ 新增稳定的 `<ViewTransition>`，基于浏览器 View Transition API，可处理进入、退出、更新、共享元素动画；只有 Transition 更新会触发动画。
- 🧭 新增 `addTransitionType`，可标记 transition 的原因，例如 `next` / `previous`，从而为同一状态更新定制不同动画。
- ⏳ View Transitions 可与 Suspense 集成，动画化 fallback 到最终内容，也可让图片、字体加载触发 Suspense；建议 fallback 立即显示，最终内容带动画，已缓存内容不动画。
- 🔗 Fragment Refs 稳定，可将 ref 传给 `<Fragment>` 获得 `FragmentInstance`，统一操作一组兄弟 DOM 节点，如事件、焦点、观察器、测量和滚动。
- 🖥️ 新增 `browser()`，通过 `use(browser())` 让组件跳过服务端渲染：服务端触发 Suspense，客户端不触发，适合时区、`localStorage` 等浏览器专属逻辑。
- 🔐 支持 Trusted Types，React 不再把 `TrustedHTML` 等对象强制转成字符串，配合 CSP 帮助防止 DOM XSS。
- 🧩 Server Components 可直接渲染从 `'use client'` 模块导入的 `<Context>`，不再必须额外导出 Provider 包装组件。
- 🛠️ 其他改进包括：Transition 独立渲染、`use` 条件使用警告、`onFullscreenChange` / `onFullscreenError`、`maskType`、`fetchPriority`、表单重置与 submit 事件、错误信息传输等。
- 🐞 修复多项问题，包括 `useDeferredValue` 卡旧值、Suspense fallback 上下文传播、`ViewTransition` 在 Mobile Safari / SuspenseList 崩溃、hydration `nonce` 误报、Deno 服务端挂起等。

---

### [](https://sentry.io/cookbook/custom-metrics-dashboard-alerts-nextjs/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=nextjs-fy27q3-cookbook&utm_content=newsletter-react-link-nextjs-metrics-dashboard-trysentry)

**原文标题**: [Build a dashboard and alert from Next.js custom metrics | Sentry](https://sentry.io/cookbook/custom-metrics-dashboard-alerts-nextjs/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=nextjs-fy27q3-cookbook&utm_content=newsletter-react-link-nextjs-metrics-dashboard-trysentry)

本文介绍如何在 Next.js 应用中通过 Sentry 从自定义指标出发，快速搭建仪表盘与告警。只需从 Server Action 中发出一个自定义指标，就能把它变成可视化仪表盘组件，并配置阈值或异常检测告警；所有数据都与追踪关联，指标异常时一键跳转到对应的请求。教程约需 20-25 分钟，共 6 个步骤，适合具备 Next.js Route Handlers 或 Server Actions 基础的开发者。

- 🚀 **前提条件**：需要一个 Next.js 应用（推荐 v13+ 的 App Router）、`@sentry/nextjs` 10.25.0 或更高版本（该版本起指标默认开启），以及 Sentry 账号和项目；使用异常检测告警需 Trial、Business 或 Enterprise 套餐
- 🛠️ **第一步：安装 SDK**：在项目根目录运行 `npx @sentry/wizard@latest -i nextjs`，向导会自动配置 instrumentation 文件，指标默认开启，如需关闭可设置 `enableMetrics: false`
- 📊 **第二步：发出自定义指标**：用 `Sentry.metrics.count()` 统计计数类事件，用 `Sentry.metrics.distribution()` 记录需要百分位的数值；示例中每次用户增删演讲都会统计 `schedule.event`，并附带 `action` 和 `result` 属性
- 🔍 **第三步：在指标浏览器中查看**：触发几次代码路径后打开 Metrics explorer，选择 `schedule.event`，按 `result` 属性分组查看成功、重复和失败情况；Samples 标签页可查看单个指标事件并直接跳转到对应追踪
- 📈 **第四步：搭建仪表盘**：从浏览器中点击 Save As 将查询固定为仪表盘组件，再加入第二个相关指标（如 `ai.tokens.total` 的 p95 或 `page.view` 吞吐量）并排展示
- 🚨 **第五步：添加阈值告警**：通过 Save As 菜单将其转为 Monitor，选择 Threshold 检测方式并设置明确的数值（如每小时 token 费用上限），通知可发送至 Slack、PagerDuty 或邮件
- 🤖 **第六步：改用异常检测**：当尚不清楚"正常"基线时，创建第二个告警并选择 Anomaly 检测方式，Sentry 会学习指标的季节性和日/周规律，只需调整灵敏度滑块，适合流量自然起伏的指标
- 💡 **命名建议**：使用一致的点分命名约定（如 `schedule.event`、`ai.tokens.total`），便于团队查找和分组
- 💡 **善用属性**：把业务上下文（action、result、套餐等级）放入 attributes 而非指标名称中，高基数事件的属性不额外收费，且能提供更多切分和告警维度
- 💡 **百分位用分布**：需要 p95 或 p99 时应使用分布而非 gauge，因为 gauge 只保留最新快照
- ⚠️ **常见误区**：不要把维度写进指标名（如 `schedule.event.success`），否则会爆炸基数导致无法分组；不要指望从 counter 或 gauge 中得到百分位；不要在强季节性指标上使用静态阈值；SDK 版本低于 10.25.0 会静默忽略指标调用
- ❓ **常见问题**：指标无需额外配置；count 用于计数、gauge 用于即时值、distribution 用于百分位；静态阈值适合已知危险数值，异常检测适合无基线或强季节性场景；指标按量计费，免费套餐足够入门；阈值和异常告警均可通知 Slack、PagerDuty 或邮件
- 🔗 **后续方向**：可进一步探索 Tracing（分布式追踪）、Logs（结构化日志），并查看本教程基于的 Sentry 工作坊示例应用源码

---

### [](https://raw.githubusercontent.com/react/react/main/packages/react-devtools/CHANGELOG.md)

**原文标题**: [CHANGELOG.md](https://raw.githubusercontent.com/react/react/main/packages/react-devtools/CHANGELOG.md)

React DevTools 8.0.0 于 2026 年 9 月 8 日发布，重点是将 Suspense 标签页默认开启、移除 Timeline Profiler 并转向浏览器 Performance 面板，同时让 Elements 面板能显示对应 React 组件。本次更新还包含大量功能改进与错误修复，涉及 Profiler、Suspense、搜索导航、连接、过滤器、CSP 兼容性等。

- 🧩 Suspense 标签页默认开启，可直接检查组件挂起原因，无需额外开启。
- ⏱️ 移除 Timeline Profiler 标签页及相关代码；React 性能分析改用浏览器 Performance 面板中的 React 轨道。
- 🔍 在浏览器 Elements 面板检查 DOM 节点时，可看到匹配的 React 组件，并新增 React Element 窗格。
- 📊 Profiler 空状态围绕主操作重新设计；新增提交视图组件搜索、开始/停止分析快捷键、提交导航快捷键、父级堆栈工具。
- 🧵 Suspense 标签页支持列出命名 Activity、按结束时间排序时间线、与主文档同步滚动；Activity 子树在隐藏模式下显示并变暗。
- 🛠️ 新增组件搜索结果直接导航、忽略列表堆栈帧披露、显示 React.optimisticKey、允许重命名 Host Component props。
- 🌐 支持 React DevTools 客户端连接自定义 host/port/path；在 sandbox CSP 页面中提供最小支持；在 React 检测前创建扩展面板。
- 🔄 初始加载即应用组件过滤器，并在过滤器变化时更新检查元素；改进 changed hooks 检测；禁用 Strict Mode 日志变暗设置。
- 🐛 修复 fallback Fiber 内容协调、嵌套 HOC 名称提取、prerender 时连接/重连、WhatChanged 滚出视图、控制台占位符与转义、独立错误 HTML 注入等问题。
- 🐛 修复 -Infinity 保留、鼠标离开 DevTools 清除高亮、空 Suspended By 区块、旧 React 页面忽略新生产 renderer、类组件错误模拟崩溃、ContextMenu 空列表崩溃、AMD 模块、hoistables 内存泄漏。
- 🐛 修复性能分析相关问题：断开子树时长、过滤 Activity 子节点崩溃、过滤节点误报重渲染、初始操作提交树构建、切换 profiler 根时提交索引重置、console 链接、useSyncExternalStore hook 索引、Activity slice 解码等。

---

### [](https://github.com/react/react/tree/main/packages/react-devtools-cdt-mcp)

**原文标题**: [react/packages/react-devtools-cdt-mcp at main · react/react · GitHub](https://github.com/react/react/tree/main/packages/react-devtools-cdt-mcp)

这是 React 仓库中 `react-devtools-cdt-mcp` 包的说明，属于实验性浏览器库，用于把 React 检查与性能分析工具注册到 `chrome-devtools-mcp`，本身不是 MCP 服务器，需在页面中于 React 之前导入，并依赖实验性第三方工具支持。

- 🧪 实验性库：基于 `chrome-devtools-mcp` 的实验性第三方开发者工具 API，用于向 MCP 客户端暴露 React 检查与性能分析能力。
- 🌐 浏览器库定位：需在受测页面中导入，`chrome-devtools-mcp` 会从页面发现 React 工具；它不是 MCP 服务器，不应放入 MCP 客户端配置。
- 📦 安装方式：`npm install react-devtools-cdt-mcp`。
- ⚙️ 使用要求：在 React 之前导入 `react-devtools-cdt-mcp/register`，以确保 DevTools hook 先于 React 初始化安装；该入口在非浏览器环境会抛错。
- 🔌 自定义目标：包根无副作用，并导出 `register`、`buildToolGroup` 等底层 API。
- 🛠️ MCP 配置：需在 MCP 客户端配置中加入 `--categoryExperimentalThirdParty=true`，并要求 `chrome-devtools-mcp 1.3.0+`。
- 🔍 工具调用：React 工具会出现在 `list_3p_developer_tools` 中，可通过 `execute_3p_developer_tool({toolName, params})` 或 `evaluate_script(window.__dtmcp.executeTool(toolName, params))` 调用。
- 🔐 隐私提示：这些工具可能向 MCP 客户端暴露组件 props 和 hook 值，仅建议在本地或可信调试会话中使用。
- 🆔 UID 约定：组件以稳定 uid（如 `r5`）标识，跨工具和重渲染保持一致，但页面重载后失效。
- 📤 输出约定：工具返回普通 JavaScript 值；失败时返回 `{error: string}`。
- ⏱️ 时长约定：性能分析时长单位为毫秒；若构建未收集性能计时则返回 `null`。
- 🌳 `react_get_component_tree`：获取组件树快照，支持 `depth` 和 `rootUid`，返回节点数组。
- 🔎 `react_get_component_by_uid`：获取单个组件详情，可选 `includeHooks`；检查 hooks 会重新渲染组件渲染函数，但不运行 effects。
- 🧩 `react_get_component_by_dom_element`：根据页面 DOM 元素引用获取对应 React host 组件详情。
- 🔤 `react_find_components`：按名称子串不区分大小写查找组件，支持分页和限定子树。
- 📍 `react_get_component_source`：获取组件定义源码位置；host 组件或生产构建可能返回 `null`。
- 🧵 `react_get_owner_stack_trace`：获取原始 owner 栈追踪，仅 DEV 环境有值。
- 🪜 `react_get_parent_stack`：获取已渲染父级列表，从直接父级到根，包含 host DOM 组件。
- 🧭 `react_get_owner_stack`：获取结构化 owner 列表，表示通过 JSX 创建该元素的组件链；仅 DEV 可用，owner 不等于结构父级。
- 🟢 `react_start_profiling`：启动性能分析会话，记录每次提交的渲染耗时，可选 `traceName`。
- 🔴 `react_stop_profiling`：停止当前性能分析会话，返回 trace 名称和提交次数。
- 📊 `react_get_trace_overview`：获取某次 trace 的逐提交概览，包括渲染、布局、被动耗时和变更组件数。
- 📈 `react_get_commit_report`：获取单次提交的详细报告，组件按 `actualDuration` 降序排列。

---

### [](https://github.com/reactjs/react.dev/pull/8632)

**原文标题**: [Document missing react-dom server rendering and hydration options by eps1lon · Pull Request #8632 · reactjs/react.dev · GitHub](https://github.com/reactjs/react.dev/pull/8632)

overview summary
该 PR（#8632）由 eps1lon 合并到 reactjs/react.dev，用于补充 React DOM 服务端渲染与 hydration 中缺失的稳定选项文档，并修复 resume 相关引用、实验标签和参数命名问题。

- 📝 为 hydrateRoot 增加 formState 文档：用于 Server Function 表单提交后的 hydration 状态，使 useActionState + permalink 在 hydration 时返回已提交状态，而非初始状态；该选项自 React 19.0 起已发布但此前未记录。
- 🌊 renderToPipeableStream 与 renderToReadableStream 新增 formState、importMap、onHeaders、maxHeadersLength，以及用于区分脚本/样式 nonce 的对象形式 nonce。
- ⚙️ prerender 与 prerenderToNodeStream 新增 importMap、onHeaders、maxHeadersLength。
- 🏷️ 移除 react-dom/static 索引中 resumeAndPrerender 的“仅实验性”标记，因为它已在稳定版发布。
- 🐛 修正 resumeAndPrerender 介绍中错误解构的 postpone，应为 postponed。
- 🔄 resumeToPipeableStream 页面不再记录 signal 选项，因为 Node.js 实现未类型化也未读取它；改为记录实际支持的 onAllReady 回调。
- 🔗 修正该页面错误提及 resume 但实际指 resumeToPipeableStream 的问题，并让 react-dom/server 索引中的两个 resume 条目链接到各自页面。
- ✅ PR 合并到 main，5 项检查通过，预览部署成功；Next.js 包分析显示 JavaScript bundle 无变化。

---

### [](https://github.com/vercel/next.js/pull/97232)

**原文标题**: [Upgrade web-vitals to v6 and report soft navigations by timneutkens · Pull Request #97232 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/97232)

Next.js 仓库 PR #97232 已合并到 canary，核心是将内置 `web-vitals` 升级到 v6，并为 CLS、INP、LCP 启用软导航上报。

- 🚀 升级 vendored `web-vitals` 依赖到 v6，后续按审查建议跟进到 6.2.0/6.2.1。
- 📊 启用 CLS、INP、LCP 的 soft-navigation 上报，让 `useReportWebVitals` 将指标归因到实际发生的导航。
- 🔗 支持 `navigationURL`，用于路由归因。
- 🧹 移除过时的 FID 集成与兼容补丁，重新生成标准与 attribution bundles。
- 📝 更新公共 metric types 和文档，匹配当前上游 API。
- 🧪 增加生产模式测试，覆盖初始与软导航 Web Vitals 上报，同时包含 Turbopack 和 Webpack。
- ⚡ 性能统计：`node_modules` 减少约 560 kB，Webpack 构建时间减少约 2.746 秒（-11%）。
- ⚠️ 体积变化：Turbopack 客户端主包总量增加约 102 kB，Webpack 客户端主包增加约 5.87 kB，存在体积回归。
- 👀 审查：tunetheweb 建议直接升级到最新 v6，eps1lon 批准；之后补充 6.2.0/6.2.1、合并 canary、简化测试并恢复交互覆盖。
- ✅ 合并状态：2026-09-03 合并到 canary，226/229 项检查通过，相关分支已删除。
- 📌 关联：#97161、#97238、#58672，以及 Cloudflare/vinext #3166 跟进。

---

### [获取失败](https://blog.master.dev/react-now-rusted-all-the-way-out/)

**原文标题**: [Failed to retrieve](https://blog.master.dev/react-now-rusted-all-the-way-out/)

无法总结：获取内容失败，状态码 429。

---

### [](https://maxleiter.com/blog/thank-u-next)

**原文标题**: [thank u, next | Max Leiter](https://maxleiter.com/blog/thank-u-next)

2026年9月1日，作者宣布个人网站不再使用 Next.js，而是迁移到由 Fable 设计、Opus 实现的定制“氛围编码”框架；这是一个静态站点，约 3 小时产出可用版本，总成本 669.45 美元，展示了 LLM 按需生成专属框架并大幅优化性能的可能性。

- 📅 文章标题《thank u, next》，宣布网站从 Next.js 切换到定制框架；这是个完全静态、构建时编译为 HTML 的站点，但包含 React 与 MDX 等非平凡处理。
- 🧠 框架由 Fable 5 规划、Opus 子代理实现，约 3 小时出现可用版本；总成本 669.45 美元，代码新增 20,914 行、删除 2,022 行，约用 Claude Code 20x 订阅的 10%。
- 📉 首页 HTML 从 24.7 KB 降到 16.3 KB（-34%），eager JavaScript 从 208 KB/11 文件降到 2.3 KB（-99%）；博客 HTML 从 20.6 KB 降到 11.6 KB（-44%）。
- ⚡ Lighthouse 移动端提升明显：首页 98→100，LCP 2.4s→1.3s，页面重量 1,153 KB→78 KB；博客 LCP 2.2s→1.1s，重量 405 KB→57 KB。
- 🏗️ 构建更快：本地 warm build 2.4s→0.5s（-79%），Vercel 平均构建 28s→11s（-61%），lockfile 包数量 706→550（-22%）。
- 🧩 实现更像构建脚本：`build.ts` 读取 `posts/`，用 React 在服务端渲染所有路由为静态 `index.html`，并输出 Vercel Build Output 目录。
- 🗂️ MDX 在构建时用相同 remark/rehype 插件编译；Shiki 语法高亮在构建时输出双主题 HTML，主题切换无需 JavaScript。
- 🏝️ 内容页几乎零 JS，仅约 2 KB 内联脚本处理主题切换、Cmd+K 和懒加载 islands；桌面窗口管理器与命令面板用 Preact 按需 hydrate，Preact 约 7 KB，而 React 约 52 KB。
- 🧪 Claude 还写了“parity harness”，对比旧站 101 条路由的 head、正文和代码块，发现并修复 RSS 泄露 8 篇未发布文章、OG 图片 404 等问题。
- 💡 动机包括：递归替换依赖、减少供应链攻击、只 vendor 所需部分；新框架约 5,000 行，易于人类和模型审查，而 Next.js 与 React 有数十万行。
- ⚠️ 缺点很多：缺少 Next.js 大量边缘优化；需自行维护 bug、安全和功能；可能失去上游安全修复；也省略了框架 MCP 等特性。
- 🐛 还遇到浏览器坑：Chrome 跨文档视图过渡在目标页有外部 module script 时会跳过入场；WebKit 对 Speculation Rules 的 prerender 检测不可靠，需要双重检查。
- 🔮 作者认为会出现更多 vendoring 与 agentic rewrite，例如 Bun 从 Zig 重写为 Rust、Cloudflare 的 Vinext；更远看框架可能消亡，但其内嵌知识会蒸馏成技能或未来标准。

---

### [Turbopack 如何对你的 JavaScript 进行分块 | Next.js](https://nextjs.org/blog/turbopack-chunking)

**原文标题**: [How Turbopack chunks your JavaScript | Next.js](https://nextjs.org/blog/turbopack-chunking)

Turbopack 的分块核心是在“减少请求数”和“减少下载代码量”之间做权衡；它通过 chunk group、合并策略和 Next.js 16.3 新特性，让不同页面共享代码的同时尽量避免重复下载。

- 🧩 Turbopack 会把 Next.js 应用拆成许多 JavaScript chunk，包含业务代码、依赖包和运行时。
- ⚖️ 分块的最大矛盾是：chunk 越大请求越少但复用性越差；chunk 越小复用性越好但请求开销和压缩损失越大。
- 📦 全部代码打成一个 chunk 时缓存友好、导航快，但每个页面都会加载所有 JavaScript。
- 📄 每页一个 chunk 能避免过度下发，但共享代码会重复打包，访问多个页面时会重复下载。
- 🔬 每模块一个 chunk 几乎不会过度下发，但会产生数百个请求，HTTP/2 和 gzip 也无法完全解决开销。
- 🧱 Turbopack 引入 chunk group：同一组内的 chunk 总是一起加载，只允许组内合并，避免给页面增加原本不需要的代码。
- 📊 合并决策会估算访问概率：约 2/3 是单页访问，1/3 涉及两页或更多；只有两页都需要合并后的 chunk 时，合并才明显划算。
- 🧪 nextjs.org 实测：不合并为 561.6 KiB / 96 请求，Turbopack 默认为 554.8 KiB / 38 请求，每组一个 chunk 为 610.0 KiB / 15 请求。
- ⚙️ 默认策略在请求数和代码量之间较均衡；最大合并能加快首次加载，但整体可能多下发约 10% 代码。
- 🧠 Next.js 16.3 新增 `experimental.turbopackChunking.generateComponentChunks`：同时生成合并与未合并版本，运行时根据缓存选择更便宜的加载方式。
- 🔮 Turbopack 还在实验 `only-if-cached`，用于检查回访用户已缓存内容，从而优化重复访问。
- 📈 可基于分析配置分块：`firstPageLoadPriority`、`priorityRoutes`、`clusters`，让合并策略更贴合真实访问路径。
- 🌳 为减少代码体积，Turbopack 支持 CJS tree-shaking、增强 ESM/barrel 文件分析、共享运行时和更轻的默认运行时。
- 🚀 共享运行时可在首次导航后每次节省约 10 KB 客户端 JS 和一个阻塞请求；这些功能可在 Next.js 16.3+ 中试用，部分未来会默认开启。

---

### [](https://nextjs.org/blog/how-we-closed-1500-github-issues)

**原文标题**: [How we closed 1,500 GitHub issues in one month | Next.js](https://nextjs.org/blog/how-we-closed-1500-github-issues)

2026年9月4日，Next.js 团队分享如何用基于 eve 的 AI 研究代理 closability 清理 GitHub issue 积压，在约三周内关闭 1,462 个 issue，将开放 issue 从 2,244 降至 995，并建立人工审查、14 天重开窗口与每周自动清理机制。

- 📈 Next.js issue tracker 平均每周收到 36 个新报告，AI 编码代理让提交详细报告更容易，但也增加了审查量。
- ⚠️ 积压曾在 2025 年 1 月达到 3,109，2026 年 8 月 10 日仍有 2,244，旧问题、重复报告和过时版本掩盖了新回归。
- 🎯 约三周后，团队关闭 1,462 个 issue，积压降至 995，期间还新增了 218 个报告。
- 🕰️ 曾用 stale 自动关闭：2 年无活动后标记并关闭，后来改为 18 个月；但时间戳无法区分已修复、重复、预期行为、不再支持还是仍有效的 bug。
- 🤖 团队基于 eve 框架构建 closability 研究代理，在 Vercel Sandbox 中运行 Next.js 仓库、Node.js、Playwright 和 Chromium。
- 🔍 代理会阅读 GitHub 对话、检查支持版本，搜索相关 issue、PR、commit、release 和文档；必要时在报告版本、最新稳定版和 canary 上复现，并寻找反证。
- 📋 调查返回结构化结果：closeConfidence、primaryReason、summary、evidence、references；置信度保守，复现失败不足以关闭，高分需要强证据且没有可信反证。
- 🔒 代理在沙箱外只读，不能评论、关闭、推代码或部署，并忽略 issue 或仓库内容中的指令以防 prompt injection。
- ⚙️ 使用 GPT-5.6 Luna 和最高 reasoning effort 运行，平均调查 30 分钟，并发逐步提升到 200 个 eve 会话。
- ✅ 结果进入 Close Queue 由维护者审查；关闭原因包括已修复 543 个（37%）、重复 278 个（19%）、预期行为 237 个（16%）、不再可复现 89 个（6%）、不支持或过时 66 个（5%）、其他 249 个（17%）。
- 🔁 新增 GitHub Action：关闭后 14 天内可请求重开；原发者或关闭前评论者回复 Reopen: <原因> 会自动重开。99.8% 保持关闭，仅 3 个重开。
- 🧩 Maintainer Agent 由多个 eve 代理组成，包括 closability、reproduction、verification、e2e_test、fix 等；配套 dashboard 用于审查 Close Queue、启动调查、聊天问答，并向 Slack 发送高优先级发现和每日摘要。
- 🗓️ 每周一 closability 研究最多 100 个至少 30 天无活动的 issue，优先从未审过的开始；如果 issue 有新活动，就丢弃已保存的研究。
- 🚦 最近允许代理自动关闭最清晰案例：closability 评分 ≥80，第二个代理寻找应保持开放证据；两者都建议关闭后，第二个代理选择原因并写评论，GitHub Action 发布并关闭；每周最多 25 个。
- 🛡️ 自动化只关闭 issue，仍可重开；所有代码变更仍需人工审查后合并。团队计划继续自动化，以管理增长并保留社区反馈。

---

### [](https://www.cloudways.com/en/prepathon.php?utm_source=weekinreact&utm_medium=newsletter&utm_campaign=Prepathon&utm_content=Community)

**原文标题**: [Prepathon 2026 | Build, Ship & Scale at Velocity](https://www.cloudways.com/en/prepathon.php?utm_source=weekinreact&utm_medium=newsletter&utm_campaign=Prepathon&utm_content=Community)

Prepathon 2026 将于 2026 年 9 月 22–23 日以免费线上形式举行，面向开发者、代理商、店主和中小企业，围绕 AI 辅助开发、现代基础设施、WordPress/JavaScript、电商与代理业务增长，探讨如何更快构建、发布和扩展线上业务；另有 Bengaluru、Mexico City、Karachi 线下场次，名额有限。

- 🗓️ 活动时间：2026 年 9 月 22–23 日，免费在线活动，需注册，名额有限。
- 🚀 核心主题：“未来已来”——以速度构建、发布、扩展，AI 辅助且不再局限于网站。
- 👥 目标人群：开发者、代理商、店主和中小企业，适合任何在线业务建设者。
- 📈 活动规模：1500+ 参会者、8+ 直播场次、20+ 专家讲者、100% 免费。
- 🧑‍💻 Day 1 重点：主题演讲“Deploy with Velocity”、AI 代码所有权、API 经济、AI 辅助 JavaScript 应用从提示到生产、WordPress 与 AI 开发生态。
- 🧩 Day 2 重点：WordPress 之后代理商如何拓展、AI 客户、电商/WooCommerce、AI 建站与代理商交付、AI 时代的获客与服务化转型。
- 🎤 讲者阵容：Katie Keith、Jason Swenk、Valentin Radu、Miriam Schwab、Suhaib Zaheer、Brent Weaver 等 20+ 行业专家。
- 🛠️ 形式内容：专家 session、实操活动、小组讨论、现场演示和挑战，强调实际可用技能。
- 🌍 线下延伸：Bengaluru（9 月 26 日）、Mexico City（9 月 25 日）、Karachi（9 月 25 日）提供线下交流与活动。
- 📝 注册信息：免费注册，有限名额；推荐尽早锁定席位。
- 🏷️ 主办与社交：由 Cloudways 支持，话题标签 #Prepathon。
- ⚡ 核心价值：帮助参与者掌握 AI、现代技术栈、自动化和增长策略，在构建、销售和竞争中获得优势。

---

### [发布 v1.10.0 · visgl/react-google-maps · GitHub](https://github.com/visgl/react-google-maps/releases/tag/v1.10.0)

**原文标题**: [Release v1.10.0 · visgl/react-google-maps · GitHub](https://github.com/visgl/react-google-maps/releases/tag/v1.10.0)

GitHub 上 visgl/react-google-maps 的 v1.10.0 发布摘要：仓库公开，约 1.9k Star、192 Fork、60 Issues、6 Pull Requests；最新版本于 2026-09-05 发布，包含新功能与多项修复，页面部分内容加载出错需刷新。

- ⭐ 仓库 visgl/react-google-maps 为公开项目，拥有约 1.9k Star、192 Fork、60 Issues、6 Pull Requests。
- 🚀 最新版本 v1.10.0 于 2026-09-05 发布，由 github-actions 创建，提交为 956c8f5，并带有 GitHub 验证签名。
- ✨ 功能更新：map-control 新增 style prop（#1052，关闭 #379）；新增 3D 组件（#1009）。
- 🐛 修复：geometry 仅向 Maps API 发送已变更选项（#1061，关闭 #524）；防止地图事件中的无效相机值（#1023）；地图实例清理时使用最新 reuseMaps 值（#1042）。
- 📦 发布资源包含 2 个 Assets；页面出现 “Uh oh! There was an error while loading. Please reload this page.”，可能需要重新加载。

---

### [React 谷歌地图](https://visgl.github.io/react-google-maps/examples/map-3d-markers)

**原文标题**: [React Google Maps](https://visgl.github.io/react-google-maps/examples/map-3d-markers)

此示例展示了如何使用 Map3D、Marker3D 和 Pin 组件，基于 Google Maps 3D Web 组件渲染 3D 地图，并呈现多种标记类型。

- 🗺️ 使用 Map3D、Marker3D 和 Pin 组件创建 3D 地图。
- 🌐 基于 Google Maps 3D Web 组件进行地图渲染。
- 📍 展示多种标记类型：基础标记、拉伸标记、自定义图钉标记。
- 🖼️ 支持 SVG/图片标记以及 3D 模型标记。
- 🔗 可进一步了解如何向 3D 地图添加标记，并在 CodeSandbox 中试用或查看代码。

---

### [](https://github.com/shadcn-ui/cn)

**原文标题**: [GitHub - shadcn-ui/cn: cn is a new engine for Tailwind class merging and conflict resolution. It replaces tailwind-merge and clsx. Same APIs. Full parity. And it is 30× faster. · GitHub](https://github.com/shadcn-ui/cn)

overview summary
- 🚀 cn 是 aidenybai 与 shadcn 构建的新 Tailwind class 合并与冲突解决引擎，用于替代 tailwind-merge 和 clsx。
- ✅ 保持相同 API、完全对齐，可作为 drop-in replacement 立即替换。
- ⚡ 官方称常见组件调用快 30×；58 个开源仓库的 144,265 次真实调用中，几何平均快 37×。
- 🧩 零依赖且框架无关，支持 React、Vue、Svelte、Solid、Astro、纯服务端模板等。
- 🌐 可在浏览器、Node、Bun、Deno 和边缘运行时使用；适用于任何 Tailwind CSS 项目，无需 shadcn/ui。
- 📦 安装：npm i cn；迁移命令：npx shadcn@latest migrate cn。
- 🛠️ 新项目导入 { cn } from "cn" 即可；现有 shadcn/ui 项目可手动将 @/lib/utils 的 cn 改为 export { cn } from "cn"。
- 🧹 之后移除 clsx 与 tailwind-merge；若其他包仍引用，可 alias 到 cn，避免打包重复实现。
- 📊 性能示例：常见调用 320ns→10ns（30×），重复字符串 2.4µs→14ns（172×），首次调用 3.2ms→0.4ms（7×）。
- 📦 最精简版 26 KB minified；cn build 可进一步减小体积。
- 🎨 cn/config 支持与 tailwind-merge 相同的 { extend, override, prefix }，可用 createCn 自定义主题和前缀。
- 🔍 输出与 tailwind-merge 一致，通过 356,000 个差异测试；twMerge、twJoin 从 "cn" 导出，配置 API 从 "cn/config" 导出。
- ⚠️ 支持 Tailwind CSS v4；Tailwind v3 建议继续用 tailwind-merge v2；experimentalParseClassName 不支持。
- 🧷 注意：看似 Tailwind 工具的类名会被当作工具类；cn build 不检测动态拼接类名，需 --safelist；CLI 需 Node 20+。
- 📚 API 分组包括 cn、cn/config、cn/engine、cn/lite、cn/build，以及 CLI npx cn build。
- 🙏 合并引擎、编译器和表格式为原创；语义匹配 tailwind-merge，join 层兼容 clsx，重复调用缓存重实现 cnfast。
- ⭐ 仓库约 1.4k stars、14 forks、5 issues、4 PR，MIT 许可。

---

### [发布 shadcn@4.21.0 · shadcn-ui/ui · GitHub](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.21.0)

**原文标题**: [Release shadcn@4.21.0 · shadcn-ui/ui · GitHub](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.21.0)

shadcn-ui/ui 发布了最新版本 shadcn@4.21.0，主要调整 cn 工具的安装、导出与组件导入方式，并改用 cn 包内部的 twMerge。

- 📦 最新版本为 shadcn@4.21.0，发布于 9 月 4 日 05:32，包含 7 个提交合并到 main。
- ⭐ 仓库数据：约 123k Star、10.1k Fork、848 个 Issues、1.1k 个 Pull Requests。
- ✨ Minor Changes #11758：初始化时安装 cn，并为 lib/utils 生成 `export { cn } from "cn"`；Registry 组件改为从 cn 包导入 cn。
- 🔧 Patch Changes 8720dec：内部使用 cn 中的 twMerge，取代 tailwind-merge。
- 🔐 标签与提交均有已验证签名，GPG key ID 分别为 83DCF2B8D1804B6F 和 B5690EEEBB952194。
- 👍 获得 5 个点赞：slymntrm、felipeadeildo、DavdGao、maciejcieslar、Sailok25。
- ⚠️ 页面存在加载错误提示，需重新加载页面。

---

### [介绍 effective-rsc | Nikhil S](https://www.nikhilsnayak.dev/blog/introducing-effective-rsc)

**原文标题**: [Introducing effective-rsc | Nikhil S](https://www.nikhilsnayak.dev/blog/introducing-effective-rsc)

effective-rsc 0.1.0 发布：一个将 React Server Components 作为应用模型、Effect 作为运行时的全栈框架，内置基于浏览器 Navigation API 的客户端路由器。

- 🚀 作者发布 effective-rsc 0.1.0，文档站点已上线，且该站点本身就用 effective-rsc 构建，仓库还包含 Vercel 部署适配器与 hello-world 示例
- 🧠 核心理念是「React 拥有 UI，Effect 拥有运行时」：React Server Components 负责应用模型，Effect 统一处理后端服务、错误、并发、取消与资源生命周期
- 🛠️ 技术栈组合为 React Server Components、Effect、Rspack（原生 RSC 集成）、Bun（服务端运行时）和 Navigation API（客户端导航）
- ✨ 页面即 Effect，路由参数通过 Schema 解码；组件内用 `yield*` 而非 `await` 获取数据，服务依赖在类型中可见，应用 Layer 提供实现
- 🔄 请求被中止时其 Effect 工作会被中断并清理资源；Server Functions 以带 Schema 校验的 Effect 运行，同时保留 React 原生 `use server` 协议
- 🌐 客户端路由器直接构建于浏览器 Navigation API，导航在目标首次 UI 提交时即结算，从而协调 URL、UI、Suspense、滚动、焦点与视图过渡
- 🧩 不提供 History API 兼容层；若浏览器缺少 Navigation API 或 NavigationPrecommitController，链接会退化为整页导航，无 JavaScript 时仍保留浏览器原生行为
- 📦 可通过 `bunx create-ersc-app` 快速创建项目，包内含供 AI 代理阅读的 LLMS.md 参考文件
- ☁️ 可直接部署在 Bun 上，或使用 Vercel 适配器（官方文档站点即运行在 Vercel）
- ⚠️ 框架仍处于实验阶段，使用 React Canary、Effect v4 RC、TypeScript 7、Rspack 的 RSC 实现及现代浏览器 API，目前仅支持 Bun 服务端运行时
- 🙏 项目借鉴了 Rspack、react-server-dom-rspack、rsc-html-stream、Waku、Twofold、Next.js、Vite RSC 等社区成果

---

### [](https://www.vidact.dev/)

**原文标题**: [Vidact](https://www.vidact.dev/)

Vidact 是一个将 React 风格函数组件与 Hooks 编译为直接 DOM 操作的框架,组件仅在挂载时执行一次,状态变更直接更新 DOM 而非重新运行组件,从而将 React、虚拟 DOM、协调器和运行时依赖追踪排除在打包体积之外,并借助基于 Rust 编写、复用 React Compiler 分析能力的编译器实现这一目标。它目前处于测试阶段,是 React 的一个刻意子集,不支持的模式会在构建时报错,同时其配套的 Vidact Start 将同一编译器模型扩展到 SSR、水合、文件路由、加载器和客户端导航。

- ⚙️ Vidact 将 React 式函数组件和 Hooks 编译为直接 DOM 操作,组件在挂载时只运行一次。
- 🧠 编译器会识别每个值所依赖的表达式,并为其生成对应的更新函数。
- 🔄 状态变化时执行该更新函数,而不是像 React 那样重新运行整个组件。
- 📦 浏览器只运行 Vidact 的小型运行时,React、虚拟 DOM、协调器和运行时依赖追踪都不会进入打包产物。
- 🚀 示例中 `Counter` 组件被编译为手写风格的 DOM 创建、文本节点更新和事件监听代码。
- 📊 演示显示一次 Increment 点击只触发 1 次组件运行和 0 次虚拟 DOM 变更,生产包(含运行时,gzip 后)约 8.1 kB。
- 🧩 表单、带 key 的列表和条件分支都使用同一套更新模型,例如输入时直接更新已有问候语文本节点。
- 🛠️ 项目始于 2020 年的实验,作者借 codemod 工作之机重建,并借助 React Compiler 的分析基础设施承担大量工作。
- 🦀 编译器用 Rust 编写,复用 React Compiler 的 AST、作用域、HIR、CFG、SSA 和依赖信息,Vidact 自有的 IR、DOM 代码生成器和运行时。
- 🌐 Vidact Start 将同一编译器模型应用到 SSR 和水合,并加入文件路由、加载器和客户端导航,本文档站即由它运行。
- ⛔ 不支持的 React 代码会在构建时报编译错误,Vidact 不会退回到 React 或更慢的渲染器,因此目前是 React 的一个有意子集。
- 🧪 若发现应当被编译的 React 模式,可以通过提交 issue 反馈,也可查阅支持的 API 列表。

---

### [](https://docs.uniflowed.dev/)

**原文标题**: [uf â Unified Toolchain for Flow](https://docs.uniflowed.dev/)

uf 是一个面向 Flow 的 React 统一工具链，目前处于 0.0.0-alpha 预发布阶段。它用一个原生命令覆盖开发、构建、测试、格式化和 lint，将官方 Flow 解析器、React Compiler 与 oxc 集成到同一 Rust 管道和单一配置中，并基于 Vite 8 支持 Node.js、Bun、Deno，但接口和稳定性尚未保证。

- 🚧 处于 0.0.0-alpha 预发布，接口可能随时变动，npm 上 `@uniflowed/*` 均为 alpha 预发布版本。
- 📦 提供单一二进制安装方式，可通过 curl 脚本安装，并会在写入前校验发布清单中的 checksum。
- ⚡ 快速开始只需 `uf new my-site`，然后 `cd my-site && uf dev`，无需安装工具链或复制配置。
- 🏗️ `uf build` 展示各阶段耗时；示例总耗时 6.44s，使用 Vite 引擎、Node 宿主，预渲染 14 页、12 个模块。
- 🧹 不需要 `vite.config.ts`、`babel.config.js` 或 `@babel/preset-flow`，Flow 通过 Meta 的 Rust 解析器和 React Compiler 处理。
- 🔧 主打“无 Babel 的 Flow”：官方 Flow 解析器、React Compiler 和 oxc 合并在一个 Rust 管道，`component`、`hook`、`match` 和枚举在解析处降级。
- 🧩 开发服务器和生产构建使用 Vite 8，而非 fork；通过 JSON 协议驱动，保留 Vite 插件生态。
- 🧪 测试由 Rust 负责发现、排序、worker 池和报告，宿主执行测试体；1000 个测试比 Vitest 快约 9 倍，但比 Bun 慢约 3 倍。
- ⚙️ 单一 `uf.config.js` 配置运行时、路由、构建、测试和格式化，且本身是 Flow 代码并接受类型检查。
- 🌐 Node.js、Bun、Deno 是能力探测而非目标，同一项目可在三者上构建和测试。
- 📜 MIT 许可且预发布，尚不稳定；本站本身也是使用 uf、Flow 编写的 `docs/` 项目。

---

### [GitHub - huozhi/devjar：React 实时预览与静态站点导出 · GitHub](https://github.com/huozhi/devjar)

**原文标题**: [GitHub - huozhi/devjar: React live preview & Static sites export · GitHub](https://github.com/huozhi/devjar)

Devjar 是 huozhi 的开源项目，用于在应用中嵌入可编辑的 React 实时预览，也可通过零配置 CLI 构建静态网站；支持 React 19、Tailwind、静态 API 与 Vercel 部署。

- 🚀 安装：`pnpm add devjar`，使用 `<DevJar files={...} title="Live preview" />` 嵌入实时 React 预览，需 React 19。
- 🔄 传入新的 `files` 对象即可更新预览；Devjar 会编译文件并在 iframe 中渲染，尽可能启用 React Fast Refresh。
- ✍️ 可搭配 `@sugar-high/react` 的 `Editor` 组件做实时代码编辑器；在服务端组件框架中使用 `'use client'`。
- 🔒 预览运行在宿主 origin，只应运行可信代码；无需跨域隔离头或服务端编译器。
- 🛠️ CLI 命令：`npx devjar dev` 开发、`build` 导出到 `dist/`、`start` 预览构建；需要 Node.js 22+。
- 📁 `pages/` 文件即路由：`pages/index.tsx` → `/`，`pages/about.tsx` → `/about`，`pages/404.tsx` 处理未匹配路由。
- 🚫 下划线前缀文件/文件夹（如 `_helpers.tsx`、`_drafts/`）不作为路由，但仍可导入；`_layout.tsx` 没有自动布局行为。
- 📌 可在 `package.json` 中固定依赖版本；构建时会将 CDN 包 vendoring 到输出。
- 🧾 支持导入 JSON、文本（`type: 'text'`）、CSS、图片/字体/音视频/PDF URL；JSON 必须合法。
- 📦 支持本地包开发：`file:../my-library`，解析 `exports`、`module` 或 `main`，编译 TS/JSX 并监听修改。
- 🌐 `public/` 文件会复制到构建；`api/` 可提供静态 JSON 或文本，但不支持可执行 API 路由。
- 🎨 添加 `tailwindcss` 或 `@tailwindcss/browser` 可启用 Tailwind；开发时浏览器编译，构建时输出 CSS，不支持 `@theme`、`@apply` 等指令。
- 🔧 常用标志：`--host`、`--port`、`--cdn`、`--exclude`、`--base`、`--out-dir`、`--help`、`--version`。
- 📱 `npx devjar dev --host 0.0.0.0` 可在同一 Wi-Fi 下用手机打开 Network URL，`start` 也适用。
- 🏗️ 构建输出包含预渲染 HTML、CSS、public 文件、哈希资源和 vendored 依赖；只有导入 devjar 的站点才包含其 runtime/compiler。
- ▲ 在 Vercel 上 `devjar build` 还会生成 `.vercel/output`，内容哈希资源使用不可变缓存；使用 Other 预设即可。
- 🖼️ 将 `icon.svg`、`opengraph-image.jpg` 等放在项目根可加入所有页面；页面可设置 `<title>`/`<meta>`，构建时渲染一次并在浏览器 hydration。
- 🧪 示例包括 Basic、Dashboard、SWR、Personal résumé；可用 `--exclude pages/playground.tsx` 导出站点但不含 playground。
- 📜 许可证为 MIT；文档在 `devjar.vercel.app/docs`，可运行 `npx skills add huozhi/devjar --skill devjar` 安装 agent skill。

---

### [开始使用 Bamboo | Bamboo CSS](https://bamboocss.com/docs/overview/getting-started/)

**原文标题**: [Get started with Bamboo | Bamboo CSS](https://bamboocss.com/docs/overview/getting-started/)

Bamboo 是构建时、类型安全、零运行时的 CSS-in-JS，通过 Vite 将样式调用编译为全局共享的声明原子，并在构建时完成校验、裁剪与类型生成。

- ⚡ Bamboo 是构建时、类型安全、零运行时的 CSS-in-JS，核心依赖 Vite 集成。
- 🧩 `css()`、`cva()`、`sva()`、patterns 和 recipes 会编译为全局共享的 declaration atoms，相同声明只生成一条 CSS 规则。
- 🚫 Recipe 名称和文件不参与 atom 身份；开放运行时样式值会导致编译失败。
- ❌ 当调用不存在的 pattern 或 token 时会构建失败，例如 `ERR_BAMBOO_DEAD_IMPORT`。
- ✂️ 会修剪未使用的 tokens、keyframes 和 reset 规则；示例中 `styles.css` 减少 36–78%，从 18,032 字节降至 3,959 字节。
- 🏭 已被 Contra 用于生产环境，超过 20,000 个 `css()` 调用点，并有 3,000+ 测试覆盖。
- 🍴 Bamboo CSS 是 Panda CSS 的 fork，API 更小、输出更精简，迁移主要是重命名。
- 🦀 工作原理：Rust/Oxc extractor 扫描源码图，Vite 编译样式调用，全局池化 recipe/utility atoms，并按模块图修剪样式表。
- 🛠 CLI 用于生成类型化 `styled-system` 创作界面，可检查或预组装 CSS；它不是样式集成，PostCSS 不输出 Bamboo CSS。
- 🎛 样式以普通对象编写，tokens、recipes、variants 从配置生成类型，支持编辑器自动补全和编译器检查。
- 🚀 特性包括按路由 CSS、开发 source maps、现代 CSS 输出（`@layer`、自定义属性）、可预测组合、recipes/variants、类型安全、同步主题、`fallback()`、`viewTransition()`、MCP server，以及多数 JS 框架兼容。
- 📚 指南覆盖 Vite 集成、Bamboo CLI、Solid/Preact/Svelte/Astro/React Router/Qwik/Vue/Nuxt/Storybook，以及 Tokens、Recipes、Patterns、Utilities 等后续主题。
- 🙏 Bamboo CSS 最初源自 Panda CSS 的 fork。

---

### [](https://base-ui.com/react/overview/releases/v1-8-0)

**原文标题**: [v1.8.0 · Base UI](https://base-ui.com/react/overview/releases/v1-8-0)

v1.8.0（2026年9月4日）是一次覆盖全库的维护更新，重点修复无障碍语义、焦点与悬停交互、受控状态和 ID 稳定性、弹层外部点击处理、动画与挂载性能，并涉及多个表单、菜单、选择器、浮层和反馈组件。

- 🔧 通用：修复控件注销时的 label 关联；优化动画完成；修复懒渲染元素的 prop/ref 合并；修复增删项时的 roving focus；改善 hover/focus 交互；提升 trigger 挂载性能；修复滚动时禁用锚点跟踪；修复 start/end 对齐的 transform origin；移除 arrow middleware 重复 options key；注册 passive touch 监听。
- 🪟 Alert Dialog、Dialog 与 Popover：忽略打开前已开始按压所触发的外部点击；Popover 另修复 detached trigger store 迁移。
- 🔍 Autocomplete 与 Combobox：grid 模式下 group 使用 rowgroup role；readOnly 时允许打开和浏览弹层；将 aria-orientation 移到 role 所有者；从无障碍树隐藏组标签和滚动条；Combobox 修复 data-readonly 应用、新增 createItems 集合 API、修复选择后保留过滤的取消、修复 label 查找读取 Object.prototype、多选锚定首个选中项。
- 👤 Avatar：为 `<Avatar.Image>` 增加 `keepMounted` 属性。
- ☑️ Checkbox 与 Checkbox Group：修复陈旧和重复的 control ID；Checkbox 修复受控 blur 验证与陈旧 filled 状态。
- 🧾 Field 与 Form：修复自定义 validity 所有权和验证生命周期；同步受控值变化与 field 状态；修复 control ID 重复；Form 内按 Enter 只验证一次；异步验证中发布 neutral validity；修复受控 blur 验证与陈旧 filled 状态；Form 修复 `clearErrors` 在多字段同时变更时丢失更新。
- 📋 Menu 与 Menubar：初始打开的子菜单播放进入过渡；将 aria-orientation 移到 role 所有者；隐藏组标签和滚动条；Menubar 修复无障碍树以满足 `aria-required-children`。
- 🧭 Navigation Menu：修复快速扫过 trigger 时的 pointer-events 锁；打开时保持焦点在 trigger；为 `<NavigationMenu.Trigger>` 增加 disabled data 属性。
- 📱 Drawer：使用 snap points 时忽略无方向滑动；尊重已取消的 snap point 关闭；开始滑动时忽略页面滚动容器。
- 🔢 Number Field：长按期间被禁用时停止递增；阻止水平滚轮事件触发 scrubbing；聚焦输入时保留原生和消费者控制的选择。
- 🖱️ Scroll Area：从无障碍树隐藏组标签和滚动条；防止滚动条抢焦点。
- 🎛️ Select：将 aria-orientation 移到 role 所有者；多选锚定首个选中项；隐藏组标签和滚动条；修复 Field 内 root ID 被忽略；移除 `<Select.Positioner>` 冗余 size 检查；readOnly 时允许打开和浏览弹层；修复 label 查找读取 Object.prototype。
- 🎚️ Slider 与 Tabs：防止不稳定 ref 导致更新循环；Tabs 定位指示器时考虑 3D transforms。
- 🔔 Switch：修复受控 blur 验证与陈旧 filled 状态。
- 🍞 Toast：支持基于当前 toast 的函数式更新。
- 💬 Tooltip：在 provider delay 为零时仍尊重 trigger delay。

---

### [发布 rsbuild-plugin-react-router@0.6.0 · rstackjs/rsbuild-plugin-react-router · GitHub](https://github.com/rstackjs/rsbuild-plugin-react-router/releases/tag/rsbuild-plugin-react-router%400.6.0)

**原文标题**: [Release rsbuild-plugin-react-router@0.6.0 · rstackjs/rsbuild-plugin-react-router · GitHub](https://github.com/rstackjs/rsbuild-plugin-react-router/releases/tag/rsbuild-plugin-react-router%400.6.0)

本页是 `rsbuild-plugin-react-router@0.6.0` 的 GitHub 发布说明，重点加入 React Router 8 与 RSC 支持，并修复开发服务器、HMR、CSS 输出及构建稳定性相关问题。

- 📦 发布 `rsbuild-plugin-react-router@0.6.0`，由 `github-actions` 发布，包含 17 个提交并合入 `main`。
- 🧩 新增 React Router 8 兼容，同时保留 React Router 7 行为。
- ⚙️ 支持 React Router 8 稳定配置字段、按已安装主版本解析预渲染数据请求、RSC 模式，以及分析转换后的 MDX 路由模块以生成 manifest。
- 🧷 生产环境保留 Flight client-reference 导出与名称，并支持 React Router 8.3 过期客户端检测。
- 🔥 避免初始 RSC 客户端 loader hydration 竞争；合并客户端与服务端 RSC 热更新，同时保持客户端状态挂载且不重新验证普通懒编译。
- 🚦 路由拓扑变化时可可靠重启开发服务器；路由 watcher 启动不再打断早期开发热更新，临时无效路由配置也不再拆毁活跃 HMR 编译器。
- 🎨 当 RSC 路由模块导入 CSS 时，React Router 的 `handle`、`links`、`meta`、`shouldRevalidate` 导出仍可正常工作；要求 Rsbuild 2.2，并依赖 Rspack 2.2 的直接客户端引用输出。
- 🧹 每个插件设置共享一个作用域 Effect 运行时，使路由 watcher、懒编译预热、类型生成、预渲染等后台资源按确定性、幂等顺序关闭；Effect 不进入转换 loader 与浏览器/运行时模板。
- 🧭 路由客户端入口导入改为相对请求，使同一项目从不同路径构建时输出和内容哈希更稳定。
- 💅 RSC 渲染期间流式输出服务端优先路由 CSS；服务端组件模块会标记 `'use server-entry'`，使 rspack RSC 运行时记录 `entryCssFiles`，并以 precedence 样式表链接发送，修复样式缺失和 FOUC。
- 🐛 在传播首个失败前运行所有合并的 `buildEnd` 钩子。
- ⭐ 仓库当前有 141 star、12 fork、3 issue、1 PR，发布资产 2 个，并获得 1 个 👍。

---

### [发布 v10.6.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v10.6.0)

**原文标题**: [Release v10.6.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v10.6.0)

Storybook v10.6.0 是 GitHub 上的最新发布，主打面向代理工作流的新技能架构、CLI/MCP 工具集成，并包含数百项修复与性能改进；Angular、Vue、TanStack/Next.js-Vite 等生态也获得大量更新。

- 📦 发布 v10.6.0，标记为 Latest，包含数百项修复和改进，由 3 个提交生成。
- 🤖 引入面向代理工作流的新技能架构，并为代理工具/技能提供 CLI 绑定。
- 🅰️ Angular-Vite 新增实验性 MCP/技能支持，并改进 docgen 与故事片段生成。
- 🟢 Vue 新增实验性 MCP/技能支持，改进 docgen/片段，并弃用 vue-docgen-api。
- 🧩 修复 TanStack 与 Next.js-Vite 框架问题，提升路由、配置和集成稳定性。
- ⚡ 性能优化并减小包体积，工具 CLI 冷启动时间减半。
- 🧪 Addon Vitest 修复测试 glob、依赖预打包、失败上报和堆栈过滤。
- 🛠️ CLI 新增 storybook skills/tools 命令，改进 attach、端口选择、telemetry 与 JSON 输出。
- 🧱 Core 更新包括组件 API manifest、安全令牌、工具 SDK、模块解析和 docgen 恢复。
- 📝 文档与 docgen 改进：TypeScript JSDoc 语义、Angular/Vue 元数据、story-docs 片段及警告。
- 🔍 搜索与 UI 改进：文档标题加入搜索、文档故事作为文档结果、修复侧边栏和面包屑等问题。
- 🧑🤝🧑 由 ghengeveld、kasperpeulen 等 23 多位贡献者参与发布。
- ⚠️ 页面多处显示加载错误，需刷新；但发布说明主体仍完整列出更新。

---

### [](https://github.com/bvaughn/react-window/releases/tag/2.3.0)

**原文标题**: [Release 2.3.0 · bvaughn/react-window · GitHub](https://github.com/bvaughn/react-window/releases/tag/2.3.0)

这是 bvaughn/react-window 的 2.3.0 版本发布页面，仓库为公共项目，拥有约 17.2k stars 和 815 forks，包含 1 个 issue、0 个 pull request。版本由 bvaughn 于 9 月 5 日 13:20 发布，自发布以来有 2 个提交进入 main，版本提交为 4d9eebb；主要更新是为 List 新增可选 rowKey 属性，并为 Grid 新增可选 rowKey/columnKey 属性。

- ⭐ 仓库：bvaughn/react-window，公共项目，约 17.2k stars、815 forks。
- 🐞 Issues 1 个，Pull requests 0 个。
- 🚀 发布版本：2.3.0，由 bvaughn 于 9 月 5 日 13:20 发布。
- 📦 自该版本以来有 2 个提交到 main，版本提交为 4d9eebb。
- ✨ 为 List 添加可选 rowKey 属性。
- 🧩 为 Grid 添加可选 rowKey / columnKey 属性。
- 📎 发布资产：2 个。
- 🔐 页面包含 Actions、Security and quality、Insights 等导航项；更改通知设置需登录。
- ⚠️ 页面部分内容加载时出现错误提示，需重新加载。

---

### [发布 v3.0.0 · pmndrs/jotai · GitHub](https://github.com/pmndrs/jotai/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · pmndrs/jotai · GitHub](https://github.com/pmndrs/jotai/releases/tag/v3.0.0)

Jotai v3.0.0 已发布，由 dai-shi 于 9 月 8 日 13:45 发布。该版本整体保持向后兼容，但移除了部分旧版支持和已弃用 API，并提供迁移指南。

- 👻 Jotai v3.0.0 正式发布，官方称“Jotai v3 is here! 🎉”
- 📦 兼容性：大多是向后兼容更新，同时放弃部分旧版支持与已弃用 API
- 🧭 迁移指南：https://github.com/pmndrs/jotai/blob/main/docs/guides/migrating-to-v3.mdx
- 🛠️ 主要变更：v3 由 @dai-shi 在 PR #3337 中实现
- ⚙️ 依赖更新：开发依赖更新，v3 的破坏性变更包括放弃 Node 20，PR #3367
- 📜 完整变更日志：v2.20.3...v3.0.0
- 👤 贡献者：dai-shi
- ⭐ 仓库信息：pmndrs/jotai 为公开仓库，约 21.3k stars、726 forks
- 🎉 社区反应：发布获得 10 个 🎉、5 个 ❤️ 等反馈

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=this-week-in-react&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=this-week-in-react&utm_medium=email)

SurveyJS 是一套开源 JavaScript 客户端调查与表单管理库，帮助开发者在自己的应用中构建、展示、分析并导出动态表单，同时完全掌控数据存储与隐私。它包含 Form Library、Survey Creator、Dashboard、PDF Generator 四大核心组件，支持 React、Angular、Vue 3 与原生 JS，适用于自托管、安全合规、多行业表单管理，并提供一次性开发者许可证。

- 🧱 **Form Library**：MIT 许可的 UI 组件，解析 SurveyJS JSON 并即时渲染动态交互表单，收集用户回答并发送到自有数据库。
- 🛠️ **Survey Creator**：白标拖拽式表单构建器，自动生成 JSON schema，支持主题编辑、逻辑分支、默认值与计算，无需写代码。
- 📊 **Dashboard**：解析 JSON schema，识别数据类型，用交互式图表和表格展示调查结果，支持表格视图、分页与筛选。
- 📄 **PDF Generator**：根据表单 JSON schema 将网页表单渲染为可编辑或预填 PDF，便于导出和打印。
- 🔓 **开源与数据自主**：所有库均在 GitHub 上开源，支持自托管，SurveyJS 不存储、访问或追踪数据。
- ♿ **无障碍支持**：Form Library v2.1.0+ 与 Survey Creator v2.2.2+ 符合 WCAG、Section 508 和 ARIA 标准，支持键盘与屏幕阅读器。
- ♾️ **无使用限制**：不限制表单数量、回答数量、管理员、受访者、提交量、上传量或功能使用。
- 🧩 **自定义输入字段**：可定义独立或复合问题类型，扩展内置组件，或集成 Angular、React、Vue 3 组件。
- 📴 **离线数据收集**：调查、主题和回答可本地存储，离线创建与收集，恢复联网后自动同步。
- 💳 **一次性许可证**：Survey Creator、PDF Generator、Dashboard 可一次性购买永久使用，含 12 个月免费维护与期间版本永久权利。
- ✅ **自定义数据验证**：除内置客户端验证器外，还可用 JavaScript 函数和事件处理器实现客户端与服务器端校验。
- 🎨 **白标与主题适配**：共享设计令牌与可复用主题，支持 Bootstrap、Material UI、shadcn/ui 主题适配器。
- 🤖 **AI 辅助**：通过 API 集成 AI，实现自然语言生成表单、翻译和智能内容建议。
- 🏢 **多行业适用**：保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利、银行等均可自托管使用。
- 🔐 **敏感数据安全**：自托管可确保隐私与合规，如 HIPAA、FERPA、GDPR，完全控制服务器与客户端之间的数据流。
- ⚙️ **仅专注前端**：SurveyJS 不提供后端、存储或用户管理，可连接任意服务器或数据库，审批流与认证需自行实现。
- 💬 **用户评价**：灵活、支持多种 JS 环境、可访问性强、条件逻辑复杂、客户支持快速且出色。
- ❓ **常见问题**：许可证永久有效，维护订阅可续订；使用量无限制；支持后端集成；许可证可分配给开发者；许可证密钥可在账户中查看。

---

### [别再成为代码审查的瓶颈](https://posthog.com/newsletter/code-review-tips?utm_source=twir&utm_campaign=sept9)

**原文标题**: [Stop being the code review bottleneck](https://posthog.com/newsletter/code-review-tips?utm_source=twir&utm_campaign=sept9)

AI生成的代码正以超过人工审查的速度产出，PostHog工程师分享四种去瓶颈化工作流：让代理互审、循环托管PR、自动盖章低风险PR、用观察而非推理验证，从而减少人工介入并保持交付速度。

- 🚧 核心问题：如果需要参与每个PR审查，你就会一直是瓶颈；高杠杆做法是尽量少审，把审查任务委托给代理流水线。
- 🤖 让代理审查代码：把简单审查交给代理，只标记真正需要人类介入的问题；写代码的代理不能审查自己的代码。
- 🧩 多代理审查系统：Paul D'Ambra 用 qa-swarm 生成 qa-team、security-audit、paul-reviewer、xp-reviewer 等审查员，再用 review-triage 将问题分为可执行、小问题、模糊三类，外层循环最多迭代3次。
- 💸 成本提醒：多代理审查可能很耗token；Paul称约60%的token花费用于自动化CI和审查杂务，但觉得值得；无法多代理时可考虑单代理方案。
- 🔁 托管PR杂务：把监控CI、重跑不稳定测试、查看评论、保持分支更新等 babysitting 任务交给循环/代理，减少上下文切换与疲劳。
- ✅ 自动盖章低风险PR：PostHog 的 StampHog 代理可通过 stamphog 标签批准小、低风险PR；检查PR状态、爆炸半径 deny-list、diff大小和简单LLM检查。
- 📉 StampHog效果：批准则留下无行评论的GitHub approval，否则拒绝或升级并给原因、风险等级、下一步；一个季度约1/3合并到主仓库PR由它最终盖章，上月处理1.6K PR，减少Slack打扰。
- 👀 观察优于推理：不要接受代理“代码能工作”的解释；运行真实请求、查看输出，直接观察行为，避免被有说服力但错误的理由误导。
- 🧱 用堆叠小PR验证：把大改动用 Graphite 拆成一系列小于400行、单一目的、可独立运行观察的小PR；自底向上合并，防止早期错误累积，便于调试。
- 🖥️ 前端验证：确定性测试不足以覆盖视觉或行为功能；可让代理运行代码并截图、录GIF，例如 qa-frontend skill。
- 🛠️ 可复制的提示词：文章为每个工作流提供可用的 LLM prompt 和 PostHog 开源实现链接，可按自己的仓库、工具链、安全边界定制。

---

### [发布 0.88.0-rc.0](https://github.com/react/react-native/releases/tag/v0.88.0-rc.0)

**原文标题**: [Release 0.88.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.88.0-rc.0)

React Native v0.88.0-rc.0 已作为预发布版发布，包含 55 个提交；本次更新涵盖破坏性变更、跨平台与平台专属新增、架构与工具链调整、弃用项、大量缺陷修复和安全升级，重点包括 Touchable 根导出移除、ArrayBuffer TurboModules 支持、DevTools 截图/网络检查、Android pull-model 挂载、SwiftPM 与 SceneDelegate 等。

- ⚠️ 破坏性变更：移除未文档化的 `Touchable` 根导出；若扩展 `Touchable` 类型，请改用 `ViewProps`。
- 🍎 iOS TurboModules：新增 `RCTArrayBuffer`，为 JS `ArrayBuffer` 提供 ObjC 表示与显式字节所有权约定。
- 🧩 新增 C++ API：提供 `<React/FeatureFlags.h>`、`<React/RendererBridging.h>`、`<React/Timing.h>` 等公共伞形头文件。
- 🎛️ 特性开关：新增 `enableImageTransparentTintColor`、Android `enableMountingCoordinatorPullModelAndroid`。
- 🧪 JS API：弃用 `react-native/Libraries/Core/InitializeCore`，改用 `react-native/setup-env`。
- 🎨 样式与文本：`PlatformColor` 支持惰性原始颜色回退；`Text`/`TextInput` 支持 `fontVariationSettings`，并增加对象语法。
- 🛠️ React Native DevTools：实验性性能截图、`Page.captureScreenshot`；CANARY 频道支持 WebSocket 事件网络面板检查。
- 📱 Android：网络事件可上报给第三方网络栈（不稳定 API）；默认 `User-Agent` 加入应用名和版本；Java TurboModules 支持 `ArrayBuffer`。
- 🍏 iOS：图片改用 asset catalog；CocoaPods 增加 `React-cxxstableapi`；新增 SceneDelegate 生命周期支持。
- 🔄 架构与工具链：Legacy Architecture 可 opt-in 移除旧 interop；SwiftPM 提供 `npx react-native spm`；Metro 升至 0.87.0，Hermes 升级。
- 🧹 行为变更：设置 `role` 时自动设置 `accessible`；Babel 平台内联需 `inlinePlatform`；`backgroundSize/Position/Repeat` 去掉 `experimental_` 前缀。
- 🗑️ 弃用：Android `InputAccessoryView` 弃用；ReactFragment 的 `fabricEnabled` 弃用。
- ♿ 无障碍修复：列表 role 转换、Android `tabbar` 崩溃、iOS Full Keyboard Access 角色可达性、VoiceOver 异步更新等。
- 🖼️ 图像修复：保留 source headers、支持 `data:` URI、修复百分比 `borderRadius` 崩溃、`tintColor` 支持透明。
- ⌨️ 输入修复：TextInput 卸载时 blur 避免键盘残留、聚焦时更新键盘类型、占位符省略行为对齐 iOS。
- 📐 滚动/列表修复：`maintainVisibleContentPosition` 快速更新、方向变化、零尺寸列表 viewable items、VirtualizedList 指标清理等。
- 🐞 其他修复：覆盖 Animated、Babel、Codegen、FileReader、Networking、ScrollView、Text、TurboModules、TypeScript 等。
- 🔐 安全：升级 `shell-quote` 至 1.8.4，修复 CVE-2026-9277。
- 📄 其他：提供 Hermes V1、ReactNativeDependencies、ReactNative Core 的 dSYM；可使用 Upgrade Helper 升级。

---

### [现在在 Expo Go 中运行项目需要登录 — Expo 变更日志](https://expo.dev/changelog/expo-go-57-login)

**原文标题**: [Login now required for running projects in Expo Go — Expo changelog](https://expo.dev/changelog/expo-go-57-login)

Expo Go 最近在 Apple App Store 更新，现已支持 Expo SDK 57。开发模式下，用户需要同时在终端运行的 Expo CLI 和 Expo Go 应用中使用同一账号登录；该要求目前仅适用于最新版 iOS Expo Go，未来将扩展到 Android，模拟器与 development builds 不受影响。

- 📱 Expo Go 已更新，支持运行 Expo SDK 57 的项目。
- 🔐 在开发模式下运行应用，必须同时登录终端中的 Expo CLI 和 Expo Go 应用。
- 📷 若终端或应用未登录，运行 `npx expo start` 并用相机扫描二维码时，可能会看到登录提示。
- 🧭 Expo Go 会告知你需要登录终端、应用，还是两者都需要登录。
- 💻 终端登录方式：运行 `npx expo login`，并按链接在浏览器中登录账号。
- 📲 Expo Go 登录方式：进入首页，点击右上角头像，输入 Expo 用户名和密码。
- ✅ 两端登录同一账号后，重新扫描二维码，或在 Home 标签点击开发服务器地址，应用即可加载。
- 🍎 此要求目前仅适用于最新版 iOS Expo Go，未来会扩展到 Android；模拟器版本不受影响。
- 🤖 建议登录 Android 版 Expo Go，这可自动显示运行中的开发服务器，并允许加载已发布项目。
- 🛠️ development builds 不需要登录。

---

### [React Native 导航基准测试 • Andrei Calazans](https://andrei-calazans.com/posts/2026-06-05-state-of-rn-navigation/)

**原文标题**: [React Native Navigation Benchmarks • Andrei Calazans](https://andrei-calazans.com/posts/2026-06-05-state-of-rn-navigation/)

四个主流 React Native 导航库（react-native-navigation、React Navigation v7、navigation router、Expo Router）在 Android 上的性能基准测试对比，涵盖冷启动、FPS、CPU 和内存等关键指标。

- 📊 **四种导航库对比**：react-native-navigation (Wix)、React Navigation v7、navigation (Graham Mendick)、Expo Router 在同一应用上分别构建测试
- ⏱️ **冷启动时间差异显著**：rn-navigation 仅 316ms，React Navigation 358ms，navigation router 398ms，而 Expo Router 高达 917ms（约 3 倍）
- 🎯 **FPS 表现一致**：四者均稳定在约 60 FPS，差异主要体现在启动成本和内存占用上
- 💾 **内存占用差距大**：rn-navigation 峰值 195MB，React Navigation 214MB，navigation router 241MB，Expo Router 308MB
- 🔥 **CPU 使用率**：rn-navigation 最低（31.2%），React Navigation v7 最高（37.8%）
- 😲 **意外发现一**：Expo Router 冷启动慢并非 Reanimated 主因（仅 +62ms），而是更大的 bundle 和路由分层导致启动时需评估 106 个 JS 模块
- 😲 **意外发现二**：Reanimated 是内存问题的核心，单独添加会增加 125MB 内存（源于第二个 Hermes 运行时）
- 😲 **意外发现三**：rn-navigation 胜在导航逻辑原生实现（Kotlin 视图），JS 线程启动时几乎不运行，但在大屏幕上会掉帧
- 📱 **测试环境**：Expo SDK 56、RN 0.85、Hermes、新架构、三星 Galaxy A16、Android 14
- ⚠️ **注意事项**：rn-navigation 是裸 RN 应用，其他三个是 Expo 应用，部分优势来自无 expo-modules-core
- 📈 **数据局限性**：单一设备、简单 UI、Hermes 采样较粗略，冷启动中位数为 3 次运行
- 🎁 **Expo Router 的额外价值**：深度链接、懒加载屏幕、基于文件的路由、Web 支持等，测试未评估这些功能是否值得
- 📚 **系列文章**：深入探讨时间去向、Expo 税、导航到屏幕的成本等主题
- 🔗 **数据可复现**：所有数据和工具位于 StateOfReactNativeNavigation 仓库

---

### [Expo Modules 2.0 抢先看 — Expo 博客](https://expo.dev/blog/an-early-look-at-expo-modules-2-0)

**原文标题**: [An early look at Expo Modules 2.0 â Expo blog](https://expo.dev/blog/an-early-look-at-expo-modules-2-0)

尚未收到需要总结的文本，因此暂时无法生成文章摘要与关键要点。

- 📭 当前消息中“Use the following content:”后没有附带任何文章或文本内容。
- ✍️ 请直接粘贴需要总结的文章、段落或资料。
- 🧾 收到内容后，我会用中文生成概述摘要，并以“- + emoji”列出关键要点。
- ✅ 摘要将保持简洁，突出核心信息、重要细节和结论。

---

### [Codemagic Patch | 适用于 React](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

**原文标题**: [Codemagic Patch | Self-hosted OTA updates for React Native](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

overview summary
- 🚀 Patch 是 Codemagic 推出的自托管 OTA 更新方案，目标是让自托管更简单、可扩展且完全可控。
- 🐳 支持在任何有 Docker Compose 的机器上一条命令部署全栈，架构可轻松扩展到百万用户。
- ⚡ 检查与下载都走 CDN，提供零停机和 99% 交付可靠性，即使服务崩溃也不中断更新分发。
- 📦 支持后台静默安装更新，也可对紧急补丁或热修复使用立即更新。
- 📊 通过 Web 仪表盘发布和监控版本、指标与团队访问，支持受控发布、推广和版本采用图表。
- 🧪 一条命令可启动本地评估栈，内含演示应用可试用 OTA；同一栈也能部署到 VM 用于生产。
- 🔍 与其他自托管 OTA 工具相比，Patch 在吞吐量、停机影响、安装时机、发布指标、仪表盘、用户角色和支持方面更有优势。
- 🧩 Patch 支持立即、重启、恢复、暂停等安装时机；其他工具常见为 sync() 安装模式。
- 📈 Patch 提供仪表盘和 CLI 指标、Web 团队仪表盘与 RBAC；其他工具指标往往有限，仪表盘和角色权限因工具而异。
- 🛟 其他自托管 OTA 通常只有 GitHub issues 支持，Patch 可提供支持许可证。
- 🏢 由 Codemagic/Nevercode 构建，团队有 10 多年移动 CI/CD 经验，并已交付数十亿次 OTA 更新。

---

### [](https://github.com/react-native-quickjs/quickjs)

**原文标题**: [GitHub - react-native-quickjs/quickjs: A Small and Fast JS Engine for React Native apps · GitHub](https://github.com/react-native-quickjs/quickjs)

react-native-quickjs/quickjs 是一个为 React Native 提供 QuickJS JSI 运行时的 Alpha 项目，基于 quickjs-ng 从源码编译，不链接 Hermes 或 JavaScriptCore，并内置安装、调试、字节码与 Hermes 兼容支持。

- 🚀 项目提供由 quickjs-ng 支持的 `jsi::Runtime`，以及 React Native 选择运行时所需的 `JSRuntimeFactory`。
- ⚠️ 当前为 Alpha 阶段，存在已知限制，预计会有破坏性变更。
- ✅ 要求 React Native 0.85+、启用新架构，iOS 15.1+，Android 7.0/API 24+。
- 📦 安装方式：`npm install @react-native-quickjs/quickjs@alpha`，运行 `npx react-native-quickjs install`，iOS 再执行 `pod install`。
- 📱 Expo 用户需添加 config plugin，并运行 `expo prebuild`。
- 🧪 `npx react-native-quickjs doctor` 可检查配置，`revert` 可恢复使用 Hermes。
- 🍎 iOS 需修改 Podfile 使用 `use_quickjs!`，并在 AppDelegate 中返回 `jsrt_create_quickjs_factory()`。
- 🤖 Android 需设置 `hermesEnabled=false`，移除 Hermes/JSC 引擎选择，应用 `quickjs.gradle`，并使用 `QuickJSInstance()`。
- 🧩 Lazy JSON 解析默认关闭，可在 `package.json` 中设置 `"react-native-quickjs": { "lazyJson": true }` 开启。
- 🐞 Chrome DevTools 可通过 React Native inspector 调试，支持断点、步进、调用栈、作用域检查和 console，仅 debug 构建包含后端。
- 📦 Release 构建会把 JS bundle 编译成 QuickJS 字节码，debug 构建仍从 Metro 加载；可用环境变量或 Gradle 参数关闭。
- 🔄 默认启用 Hermes 兼容 shim，提供 `hermes/hermes.h` 和 `libhermesvm.so`，让直接依赖 Hermes 的库如 worklets/reanimated 可运行。
- ⛔ 已知限制包括：iOS 会从源码编译 React Native core，首次和冷 CI 较慢；条件断点总会停止；为 RN 0.85 非 Hermes 路径应用了多个补丁。
- 🛠️ 构建仓库需使用 `git clone --recurse-submodules`，然后 `npm install` 和 `npm test`。
- 📁 主要目录包括 `src/`、`android/`、`apple/`、`engine/quickjs-ng/`、`modules/cdp/`、`tools/bytecode/`、`tests/` 和 `example/`。
- ⚖️ 许可证为 MIT，quickjs-ng 同样为 MIT，版权归 Fabrice Bellard、Charlie Gordon 及贡献者。

---

### [](https://github.com/kacperkapusciak/goldie)

**原文标题**: [GitHub - kacperkapusciak/goldie: ✨ agentic app store previews and screenshots · GitHub](https://github.com/kacperkapusciak/goldie)

goldie 是一个面向编码代理和人类用户的 App Store 与 Google Play 截图及预览视频生成工具，支持多种开发框架，通过模拟器或模拟机驱动应用完成截图与视频制作。

- 📱 goldie 能为移动应用生成 App Store 和 Google Play 的截图及预览视频
- 🔄 通过 argent 在 iOS 模拟器或 Android 模拟器上重放流程，并加入设备边框、背景和标题
- 🧩 框架无关，支持 SwiftUI、UIKit、Jetpack Compose、Flutter、React Native 和 Kotlin Multiplatform
- 🛠️ 需要 Node 20+ 和 ffmpeg，App Store 截图需 macOS 与 Xcode，Google Play 截图需 Android 模拟器
- 🤖 可配合编码代理使用，代理会探索应用、编写流程和配置，并打开工作室
- ✍️ 也可手动使用，复制示例配置并指向 argent 流程，运行 doctor、all 和 studio 命令
- 📐 输出到指定目录，iPhone 截图 1320x2868，预览视频 886x1920 H.264，Google Play 截图 1080x1920
- ⏱️ Apple 预览视频需 15 到 30 秒，Google Play 预览视频为 YouTube 链接，无时长限制
- 🎨 工作室可切换设备、背景、模板、边框、字体和每块文案，并保存为设计文件
- ⚙️ 配置支持边框、主题模板、字体族和装饰等选项，内置多种字体和模板
- ⚠️ 使用 Release 构建，Debug 构建会留下 LogBox 横幅；应用变更后流程可能失败，需修复或重新录制
- 💼 goldie 由 Software Mansion 赞助，该公司也是 Argent 的创建者

---

### [](https://github.com/mahdidavoodi7/react-native-continued-task)

**原文标题**: [GitHub - mahdidavoodi7/react-native-continued-task: Background tasks that keep running after your app is backgrounded, for React Native and Expo. Wraps iOS 26 BGContinuedProcessingTask (Live Activity) and Android WorkManager foreground services behind one typed API. Swift + Kotlin via Nitro Modules. · GitHub](https://github.com/mahdidavoodi7/react-native-continued-task)

react-native-continued-task 是一个 React Native / Expo 库，用于让用户发起的长任务在应用进入后台后继续运行。它封装 iOS 26 的 BGContinuedProcessingTask 和 Android 的 WorkManager 前台服务，提供统一类型化 API、系统进度 UI 与取消能力，基于 Nitro Modules 用 Swift / Kotlin 实现。

- 📱 跨平台 API：统一封装 iOS 26 BGContinuedProcessingTask 与 Android WorkManager 前台服务。
- 🔔 系统 UI：iOS 显示 Live Activity，Android 显示前台服务通知，展示进度并允许用户取消。
- 📊 进度上报是硬性要求：iOS 会终止不上报进度的任务，totalUnitCount 为 submit 必填项。
- ♻️ getKnownTasks() 用于在应用被滑动关闭后协调丢失任务，这是 iOS 检测此类终止的唯一方式。
- 🧭 类型化提交错误和停止原因：保留原始平台 domain、code 和名称，便于真机调试。
- 🧩 提供 Expo 配置插件，自动写入 Info.plist、GPU entitlement 和 AndroidManifest 相关配置。
- ✅ 已在真机验证：iOS 26.6.1 上 13/13 测试通过。
- 🔥 基于 Nitro Modules：需要开发构建，不支持 Expo Go；react-native-nitro-modules 为可选 peer 依赖。
- 📦 安装：npm install react-native-continued-task react-native-nitro-modules，然后配置 Expo 插件并执行 prebuild。
- ⚙️ 使用方式：ContinuedTasks.submit 必须在前台由用户操作触发，返回 ContinuedTask 句柄。
- 🧰 ContinuedTask 支持 updateTitle、setProgress、complete、cancel，以及开始 / 停止监听器。
- 🚫 iOS 限制：模拟器不支持；无法区分用户取消和系统过期，均报告 expired；提交必须由用户操作触发。
- 🤖 Android 注意：13+ 需运行时请求 POST_NOTIFICATIONS，否则通知被静默抑制但任务仍可能运行。
- ⏳ Android 限制：dataSync 前台服务共享 6 小时 / 24 小时预算，Android 16+ 还受 JobScheduler 配额限制。
- 🧹 应用被滑掉后：iOS 不提供取消通知，需下次启动调用 getKnownTasks() 并处理 app-terminated 记录。
- 🔁 Android 支持 attachToTask 重新附着到仍运行的 WorkManager 任务；iOS 不支持重附着。
- 🧪 测试覆盖：Jest、Kotlin JUnit、Android instrumented；RN Harness 已接线但尚未通过；iOS 后台任务需真机手动 QA。
- 📋 要求：RN 0.75+、iOS 26+、Xcode 16.4+、Android minSdk 24 / compileSdk 34+ / NDK 27+、Nitro 0.37.1。
- 🛠 配置插件选项：identifierPrefixes、enableGPU、androidForegroundServiceTypes；裸工作流需手动添加 Info.plist 和 AndroidManifest 条目。
- 🛑 停止原因包括：user-cancelled、app-cancelled、expired、fgs-timeout、quota、app-terminated、unknown。
- 👤 由 motionary.dev 的 Mehdi 构建和维护，MIT 许可，欢迎贡献 issue 和 PR。

---

### [](https://github.com/kuatsu/react-native-boost/releases/tag/v1.7.0)

**原文标题**: [Release Release 1.7.0 · kuatsu/react-native-boost · GitHub](https://github.com/kuatsu/react-native-boost/releases/tag/v1.7.0)

kuatsu/react-native-boost 发布 v1.7.0，主要带来 React Native 0.86 支持、Image 组件优化，以及无障碍、运行时和文本样式相关修复；页面多次出现加载错误提示。

- 📦 仓库：kuatsu/react-native-boost，公开项目，约 558 Star、14 Fork、1 Issue、4 Pull Request。
- 🏷️ 版本：v1.7.0，页面显示发布于 2026-09-03，包含自上一版本以来 7 个提交，提交号为 5729a2d。
- 🐛 修复：修复 changelog 生成、Image 无障碍对等问题、旧版 Android 无障碍处理、runtime 用版本默认值替换 feature flag 导入、Text 避免修改扁平化样式。
- ✨ 新功能：Image 手动注册 host，并将 optimizer 提升为默认；更新至 React Native 0.86（#77）。
- 📎 其他：提供 2 个 Assets；收到 1 个 👍 反应。
- ⚠️ 页面：多处出现 “Uh oh! There was an error while loading. Please reload this page.” 加载错误。

---

### [](https://github.com/callstackincubator/rozenite/releases/tag/v2.4.0)

**原文标题**: [Release v2.4.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v2.4.0)

callstackincubator/rozenite 发布最新版本 v2.4.0，由 github-actions 于 9 月 3 日 12:47 发布，包含 1 个提交并合并到 main。主要更新涉及 Lynx 设备运行时注入，以及通过单一 Rozenite endpoint 发现调试目标，贡献者为 @V3RON。页面同时多次出现加载错误提示，需要重新加载。

- 🚀 发布版本 v2.4.0，标记为 Latest，并可对比 v2.3.0...v2.4.0。
- 🧩 feat(lynx)：合并 @rozenite/lynx-dev，并注入设备运行时，由 @V3RON 提交于 #489。
- 🔍 feat(middleware)：通过一个 Rozenite endpoint 发现调试目标，由 @V3RON 提交于 #490。
- 📦 本版本包含 3 个资产，贡献者列出 V3RON。
- 🏷️ 发布提交为 a2c7776，发布时间为 03 Sep 12:47，包含 1 个提交到 main。
- 📊 仓库 callstackincubator/rozenite 为公开项目，有 48 个 Fork、656 个 Star、14 个 Issue、4 个 Pull Request、4 个 Discussions。
- 🔔 通知设置需要登录后才能修改。
- ⚠️ 页面多次提示加载出错，建议重新加载页面。

---

### [Release 8.25.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.25.0)

**原文标题**: [Release 8.25.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.25.0)

Sentry React Native 发布 8.25.0，主要增强了 app.vitals 与 app.start 的关联、将 feature flags 评估转发到原生 SDK，并修复了 iOS、Expo、Metro 及显示时间测量相关问题；同时升级了 Android、Cocoa、CLI 和 JavaScript SDK 等依赖。

- 📦 版本：8.25.0 最新版，由 sentry-release-bot 于 9 月 3 日 11:37 发布，提交为 600ec24。
- ✨ 功能：将 `app.vitals.start.screen` 和 `app.vitals.start.type` 复制到独立的 `app.start` 子项上，包括 `app.start.extended` 下的用户 span。
- 🚩 功能：`featureFlagsIntegration` 现在会把 flag 评估转发给原生 SDK，因此 flags 也能附加到原生崩溃上。
- 🐛 修复：防止 iOS 上 React Native >= 0.86 因 `performance.timeOrigin` 不可靠而静默丢弃日志和 span。
- 🛠️ 修复：解决 Expo 静态/EAS Update 导出时 Metro bundler 崩溃的问题。
- 🧹 修复：新架构下清除 scope context 时，iOS 不再记录 `NSNull cannot be converted` 警告。
- ⏱️ 修复：对于首次导航远晚于应用启动的应用，`time_to_initial_display` / `time_to_full_display` 现在测量实际屏幕渲染。
- 🔧 内部：生成 source maps 时，从应用项目根目录解析 Metro。
- ⬆️ 依赖：Android SDK 升级到 v8.55.0，Cocoa SDK 升级到 v9.26.1，CLI 升级到 v3.7.0，JavaScript SDK 升级到 v10.73.0。
- 👍 社区反应：有 1 人点了赞。

---

### [发布 v0.24.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.24.0)

**原文标题**: [Release v0.24.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.24.0)

该发布说明介绍 software-mansion/argent v0.24.0，重点新增实体 iOS 设备支持，并修复网络、工具客户端与测试相关问题；由 senicko 发布，含 41 个提交和 3 位贡献者。

- ⚠️ 页面多次提示加载错误，需刷新，部分内容可能未完整显示。
- 📦 v0.24.0 由 senicko 于 03 Sep 12:54 发布，包含 41 个提交到 main。
- ✅ 提交 1068430 带有 GitHub 验证签名，GPG 密钥 ID：B5690EEEBB952194。
- 🧪 测试：固定 run-sequence 序列返回的唯一观察结果（#934，@latekvo）。
- 🌐 网络：报告 UTF-8 响应字节大小（#783，@mjq2020）。
- 📱 iOS 设备：新增物理 iOS 支持（#944，@senicko），并修复相关小问题（#1031）。
- 🛡️ 工具客户端：服务器身份保护可应对 ps 被截断和 PATH 被清理（#713，@latekvo）。
- 👥 新贡献者：@mjq2020（#783）和 @senicko（#944）首次贡献。
- 🧑💻 贡献者：senicko、latekvo、mjq2020；完整变更日志：v0.23.0...v0.24.0。
- 📊 仓库：software-mansion/argent，Fork 114、Star 2.7k、Issues 226、PR 133，发布资源 2 个。
- 👍 反应：lin72h 点赞 1 次。

---

### [](https://github.com/uni-stack/uniwind/releases/tag/v1.12.0)

**原文标题**: [Release Release v1.12.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.12.0)

uni-stack/uniwind 发布 v1.12.0（最新版），由 github-actions 于 9 月 4 日 10:11 发布，提交为 44388b4。此次更新包含新功能、多项 Bug 修复、测试迁移和杂项改进，并迎来 3 位新贡献者。

- 🚀 新功能：支持 drop-shadow filter 函数（@feri-irawan，#645）。
- 🐛 修复：从扁平化类选择器中读取 variant tokens（@juliusmarminge，#662）。
- 🧊 修复：丢弃 frozen listeners（@Brentlok，#660）。
- ⚛️ 修复：withUniwind 改用 useSyncExternalStore，提升 React 生命周期兼容性（@Brentlok，#657）。
- 🧵 修复：跳过未变化的 native stylesheet 重新初始化（@juliusmarminge，#652）。
- 🪝 修复：state hooks 改用 useSyncExternalStore，提升 React 生命周期兼容性（@Brentlok，#650）。
- 🔥 修复：Web 懒加载组件无法热重载 CSS 的问题（@Brentlok，#646）。
- 🔗 修复：Metro resolver 处理符号链接的 uniwind origins（@joedeleeuw，#609）。
- 🧪 测试：Web 测试迁移到 Vitest（@Brentlok，#647）。
- 🧹 杂项：修复测试类型检查（@Brentlok，#637）。
- 🎉 新贡献者：@juliusmarminge、@feri-irawan、@joedeleeuw。
- 🧾 完整变更日志：v1.11.0...v1.12.0。
- 📈 仓库热度：Star 1.7k、Fork 51、Issues 7、Pull requests 3；Release 收获 3 个 🚀 反应。

---

### [发布 v0.3.0 · software-mansion-labs/react-native-streamdown · GitHub](https://github.com/software-mansion-labs/react-native-streamdown/releases/tag/0.3.0)

**原文标题**: [Release v0.3.0 · software-mansion-labs/react-native-streamdown · GitHub](https://github.com/software-mansion-labs/react-native-streamdown/releases/tag/0.3.0)

react-native-streamdown v0.3.0 已发布，重点支持 react-native-worklets 0.10，修复 Web 环境与 remendConfig 相关问题，并更新文档、依赖与测试；由 eszlamczyk 于 9 月 4 日发布并合入 main。

- 🚀 发布 v0.3.0：eszlamczyk 发布，包含 1 个提交并合入 main，为最新版本。
- ✨ 新增支持 react-native-worklets 0.10（#23）。
- 🐛 修复 Web 上 worklet runtime 不可用时导致的崩溃（#28）。
- 🐛 修复依赖 remendConfig 内容而非其身份标识的问题（#30）。
- 📝 更新 Worklets import forwarding 文档（#22），并更新 package.json 的 homepage URL（#26）。
- ⬆️ 将 react-native-enriched-markdown 依赖升级至 1.0.2（#32）。
- 🧪 增加 remendWorklet Web/native 平台分支测试（#31），并修复 typecheck（#33）。
- 👥 新贡献者包括：@eliotgevers、@tomekzaw、@Xuepoo、@MaryanPrydatko、@eszlamczyk。
- 📦 完整变更日志：0.2.0...0.3.0；贡献者包括 tomekzaw、tjzel 等 4 位。
- ⭐ 仓库当前 399 Star、11 Fork、2 Issues、0 Pull Requests；发布包含 2 个资产。

---

### [发布 Metro MCP 0.15.0 · steve228uk/metro-mcp · GitHub](https://github.com/steve228uk/metro-mcp/releases/tag/v0.15.0)

**原文标题**: [Release Metro MCP 0.15.0 · steve228uk/metro-mcp · GitHub](https://github.com/steve228uk/metro-mcp/releases/tag/v0.15.0)

Metro MCP 0.15.0 是面向 React Native 与 Expo 应用的最新版本，重点改进运行时检查与自动化能力，并包含多项设备发现、Hermes、导航、录制、无障碍与 AsyncStorage 相关修复。该版本收录 PR #90 至 #100，并通过大量自动化测试、MCP 协议检查和本地验收，但原生 AsyncStorage 持久化尚未验证。

- 🚀 Metro MCP 0.15.0 为最新版本，发布于 9 月 4 日 20:37，提交为 09b27c7。
- 📦 仓库 steve228uk/metro-mcp 公开，80 星、7 次 fork，0 个 issue/PR。
- 📲 修复原生设备发现与目标选择，并验证 SimView 与 IDB 输入。
- 🧠 可靠等待 Hermes JavaScript 求值，避免重放脚本。
- 🧭 可发现未访问的已注册路由与已安装应用 URL scheme，并等待聚焦的导航路由。
- ⚙️ 可通过已连接应用打开应用设置，并验证重载且无重复派发。
- 🎥 捕获前等待 recorder instrumentation，并为单个 WebdriverIO runner 会话生成 Appium 测试。
- ♿ 更准确报告不完整的无障碍树。
- 💾 在 Hermes 上解析已初始化的 AsyncStorage 导出，并解释 AsyncStorage 不可用的场景。
- 🔀 包含 PR #90–#100。
- ✅ 验证：462 个自动化测试通过，类型检查、包与文档构建通过；打包版本通过 9 项 MCP 协议检查，含现代/旧版协议与共享守护进程客户端。
- 🧪 本地验收覆盖全部 88 个工具；3 个 AsyncStorage 工具因验收应用不含 AsyncStorage，在实时 Hermes 中使用临时兼容 fixture；原生 AsyncStorage 持久化未验证。
- 📎 发布资产 2 个。

---

### [发布 v0.21.0 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.21.0)

**原文标题**: [Release v0.21.0 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.21.0)

v0.21.0 是 agent-device 的最新版本，主打更快、更易控制的设备自动化：iOS 模拟器冷启动提速 27%–40%，安装体积从 9.89 MB 降至 4.44 MB，并新增远程人工接管、更清晰的快照/断言结果、更少测试步骤与更好的远程调试；升级前需注意破坏性变更。

- 🚀 v0.21.0 已发布，包含 24 个提交，重点是提升设备自动化速度与控制力。
- ⚡ iOS Simulator 应用冷启动更快，六个基准场景耗时减少 27%–40%；快照也更快，冷启动命令会遵守设定超时。
- 🎮 支持远程接管设备而不结束 agent 会话：可暂停其操作，手动处理步骤，再让 agent 继续。
- ✅ Agent 获得更清晰结果：缺失检查可区分“元素不存在”和“捕获失败”；Android 快照会暴露字段详情，如是否可编辑或显示占位文本。
- 🧪 测试步骤更少：截图可裁剪到选中元素，可用 `fill <target> ""` 清空字段，可重置整个 Simulator keychain；Maestro 增加更多选择器与 `clearState` 支持。
- 🌐 远程运行更易调试：取消操作可到达 daemon，失败日志可通过代理访问，不兼容版本会更早失败。
- 📦 安装体积更小：依赖打包使实测安装大小从 9.89 MB 降至 4.44 MB。
- 🧱 底层改进：命令改用平台自有运行时和共享快照处理，减少重复逻辑。
- ⚠️ 升级前注意破坏性变更：批处理步骤改用结构化 `input`；`perf` 需指定 `frames` 或 `memory` 等具体操作；已移除废弃的 SDK rotate 包装器。
- 🧩 本次变更覆盖大量重构、修复与测试，涉及 daemon、iOS/Android/Web、快照、录制、Maestro、CI、安全与平台拆分等领域。
- 👥 新贡献者包括 @kkkhs、@NicolasBataille、@AdzeB、@PrinceD96、@dvd233、@Rohit3523。
- 🔗 完整变更对比为 `v0.20.10...v0.21.0`，由 thymikee、thiagobrez 等 10 位贡献者参与。

---

### [](https://github.com/lynx-family/lynx-stack/releases/tag/@lynx-js/react@0.126.0)

**原文标题**: [Release @lynx-js/react@0.126.0 · lynx-family/lynx-stack · GitHub](https://github.com/lynx-family/lynx-stack/releases/tag/@lynx-js/react@0.126.0)

@lynx-js/react 0.126.0 发布说明显示，本次更新核心是升级到 Preact 11，新增 compat 导出，并带来卸载清理时机、Context 渲染、列表 diff、运行时配置与 lynx.getApp() 等改动。  
- 🚀 发布信息：@lynx-js/react@0.126.0 由 github-actions 于 9 月 4 日 17:25 发布，包含 35 个提交到 main，commit cdc6a8c 已通过 GPG 验证。  
- 📦 从 @lynx-js/react/compat 导出 useInsertionEffect，目前是 useEffect 的别名（#3784）。  
- 🧩 从 @lynx-js/react/compat 导出 use（#3672）。  
- ⚛️ 捆绑的 Preact fork 升级到 Preact 11，@lynx-js/internal-preact 基于 11.0.0-rc.1（#3450）。  
- ⚠️ 破坏性变更：卸载组件的 useEffect 清理不再在 unmount 时同步执行，而是改为绘制后刷新阶段执行，以匹配 React；useLayoutEffect 也适用，因为 ReactLynx 将其导出为 useEffect 别名。  
- 🧹 页面销毁不受影响：会同步清空清理函数，释放原生资源的清理仍会在运行时消失前执行；若代码假设清理已在重新渲染移除组件后立即运行，需要等待一次刷新。ReactLynx 当前未导出清理逻辑留在 unmount commit 内的 hook。  
- 🧠 Context 消费者在 provider 更新时不再双重渲染，减少 rLynxChange 刷新，补丁会合并到首次刷新中。  
- 🔄 列表重排采用 Preact 11 的最长递增子序列 diff，可能选择等价但不同的最少移动集合。  
- 🧭 通过 lynx.getApp() 访问 lynx-core 的 app 对象，替代 AMD wrapper 注入的 lynxCoreInject 全局；同一实例且行为不变，多卡共享 runtime chunk 时也保持正确；@lynx-js/testing-environment 也已暴露 lynx.getApp()。  
- ⚙️ 运行时属性名配置移至页面作用域的 lynx 对象，并通过独立 webpack 插件从宿主编译注入；懒加载与外部 bundle 复用宿主配置，无需自行应用插件；runtime-config webpack 插件通过 DSL 中立入口发布，接受任意运行时配置键，不依赖 ReactLynx；合并后的顶层配置被浅冻结，防止宿主初始化后被意外修改。  
- 📐 主线程函数组件的 props 中保留 ref，与后台线程保持一致。  
- 🛠️ transform 中的 swc_core 更新至 77（#3793）。  
- 📎 资源：2 个。

---

### [GitHub - DorianMazur/react-native-screen-choreography：为 React Native 编排的共享元素过渡，支持](https://github.com/DorianMazur/react-native-screen-choreography)

**原文标题**: [GitHub - DorianMazur/react-native-screen-choreography: Choreographed shared element transitions for React Native with multi-element coordination · GitHub](https://github.com/DorianMazur/react-native-screen-choreography)

overview summary
- 📦 **项目定位**：`DorianMazur/react-native-screen-choreography` 是一个 React Native 多元素共享元素转场库，当前为 pre-1.0，GitHub 约 132 stars、2 forks。
- 🎬 **核心能力**：用一个 progress 值协调容器、图标、标签、背景变暗、渐进内容揭示与中断处理，支持前进、后退和转场打断。
- 🧱 **原生叠层**：通过位于 native-stack 容器之上的原生 overlay host 掌控可见转场，避免与导航器自身动画竞争。
- ⚙️ **环境要求**：RN >= 0.76 且启用 New Architecture/Fabric，React >= 18，React Navigation native/native-stack >= 6，Reanimated >= 4，Screens >= 4，Teleport >= 1.2，Worklets >= 0.8。
- 📥 **安装配置**：安装库及其 peers；Babel 必须加入 `react-native-worklets/plugin`；iOS 需执行 `pod install`。
- 🧭 **入口选择**：根入口用于 React Navigation，`/expo-router` 用于 Expo Router，`/core` 用于不绑定具体导航的共享组件。
- 🛠️ **推荐导航设置**：native-stack 使用 `animation: 'none'`，详情页透明呈现，并用透明 `contentStyle` 让 overlay 接管转场。
- 📱 **Expo Router**：需要原生开发构建，不支持 Expo Go；使用 `useChoreographyRouter`，且 `targetScreenId` 必须匹配目标 `ChoreographyScreen`。
- 🐞 **调试**：`ChoreographyProvider` 支持结构化 `debug` 配置，可按 error/warn/info/trace 输出，也可合并重复日志或逐帧记录。
- 🧩 **核心组件**：`ChoreographyProvider`、`ChoreographyScreen`、`SharedElement`、`SharedElement.Target`、`SharedElement.Live/LiveTarget`、`createSharedElementComponent()`。
- 🪝 **核心 Hooks**：`useChoreographyNavigation`、`useChoreographyBlocker`、`useInteractiveTransition`、`useChoreographyProgress`、`useChoreographyControls`、`useLatchedReveal`、`useStaggeredReveal`。
- 🧵 **会话匹配**：导航时通过 `transitionConfig.group` 匹配共享元素组，可传 `spring` 或 `duration` 覆盖默认动画；Back 会沿用自定义打开 spring。
- 🎞️ **转场配方**：提供 `makeSurfaceTransition`、`makeStretchTransition`、`textMorphTransition`，以及 `StandInContainer`、`StandInElement`、`resolveSurfaceStyle` 等底层原语。
- 🧠 **心智模型**：Provider 管理注册表、协调器、overlay 和会话；屏幕按 progress 0–0.4 交叉淡入淡出；共享元素由 overlay 接管位置。
- ⚠️ **已知限制**：最佳支持 native-stack/Expo Router 原生 Stack 且关闭 stack 动画；内置原生滑动手势未自动接入进度；普通 renderer 接收冻结 React 内容、样式和测量数据，而非像素截图。
- 📚 **文档与示例**：包含架构、性能、React Navigation 与 Expo Router 示例文档；示例覆盖 RN 0.83、Expo SDK 57、React 19、Reanimated 4。
- 📄 **许可**：MIT。

---

### [使用 Transformers.js 在浏览器中运行 AI](https://www.callstack.com/podcasts/running-ai-in-the-browser-with-transformers-js)

**原文标题**: [Running AI in the Browser With Transformers.js](https://www.callstack.com/podcasts/running-ai-in-the-browser-with-transformers-js)

overview summary
本期播客由 Mike Grabowski 主持，Hugging Face 开源 ML 工程师 Nico Martin 分享《Running AI in the Browser With Transformers.js》，讨论如何用 JavaScript 在浏览器本地运行 AI 模型，以及其管线、执行后端、缓存与设备限制、适用场景、浏览器 Agent 和未来方向。

- 🎧 核心主题：Transformers.js 让 Web 开发者用 JavaScript 在浏览器中运行预训练模型。
- 🧠 覆盖任务包括文本嵌入、自动语音识别、语音活动检测、图像背景移除、深度估计、文本生成和多模态处理。
- 🧩 Pipeline API 封装任务特定的预处理、模型推理和后处理，把文本、图像、音频等应用数据转换为张量并返回可用结果。
- 🧾 TypeScript 类型描述各 pipeline 的输入输出；需要自定义管线或未支持架构时，可使用更低层 API。
- ⚙️ 模型采用 ONNX 格式，由 ONNX Runtime Web 在浏览器中执行，使模型格式与运行后端分离。
- 🚀 WebGPU 可获得 GPU 加速，推荐在支持时使用；生产代码可检测支持并回退到 CPU。
- 💻 Transformers.js 也可运行在 Node.js、Deno 和 Bun，但浏览器推理是项目存在的主要原因，用户可通过 URL 直接使用、无需安装。
- 📥 首次运行会从 Hugging Face Hub 下载模型并存入浏览器持久缓存；模型大小从几 MB 到数 GB 不等。
- 🗂️ 浏览器缓存按源隔离，不同网站使用同一模型目前会各自下载和存储；跨源存储仍处于实验阶段。
- 📱 硬件差异明显：新笔记本可能流畅运行较大模型，旧手机或旧 Windows 笔记本可能很慢；当时缺少跨浏览器内存检测 helper。
- 🔐 重模型需要明确下载步骤，本地 AI 更适合作为用户知情的 opt-in。
- ⚡ 本地推理省去网络传输，对音频和图像尤其有利；示例中 30–32ms 音频约 1ms 完成推理，背景移除可避免上传图片和下载 PNG。
- 🌐 本地处理有利于隐私并可支持离线功能；云端仍适合过大或过慢的模型，本地与云可按任务混合选择。
- 🤖 浏览器 Agent：本地 LLM 可选择工具，应用执行对应 JavaScript 函数并把结果返回对话；完全本地 Agent 目前更偏 demo，混合方案更现实。
- 🛠️ Hugging Face 正在探索结构化输出，通过 JSON、正则或 XML 约束解码，让本地生成结果更可控。
- 🧬 早期 WebGPU 推理引擎由 agentic 系统编写优化 GPU kernel、融合算子并做设备特定优化，报告约 5x–10x 加速，但仍处早期。
- 🔮 跨源模型存储与 WebNN 是未来可能方向，但依赖浏览器厂商和标准进展。

---

### [](https://web.dev/blog/interop-2027-proposals)

**原文标题**: [Submit your proposals for Interop 2027  |  Blog  |  web.dev](https://web.dev/blog/interop-2027-proposals)

概述
Interop 2027 正式启动并公开征集提案，截止 2026 年 9 月 23 日；项目旨在推动已进入标准流程的 Web 平台特性实现互操作性。优秀提案需具备稳定规范、无浏览器厂商重大反对、至少一个浏览器已实现以及良好测试套件，同时可参考 Interop 2026 进展、开发者调查和工具寻找灵感，并参与社区反馈。

- 📢 Interop 2027 于 2026 年 9 月 3 日启动，首先向社区征集提案。
- 🗓️ 提案期截至 2026 年 9 月 23 日，之后所有特性将按既定流程评估。
- ✅ 好提案的关键：规范稳定、无主要浏览器厂商未决反对。
- 🌐 特性通常应已在至少一个浏览器中实现。
- 🧪 成功还依赖完善的测试套件，因为项目按浏览器通过测试情况衡量。
- 📚 可阅读《Proposal Guide》了解提升提案成功率的额外信号。
- 📈 Interop 2026 进展良好，所有浏览器达到 100% 的进度均优于去年同期。
- 🔍 2026 年许多特性来自 State of CSS 等开发者调查或 developer signals 前 20。
- 🛠️ 可用 webstatus.dev 寻找符合要求的特性，并在 developer signals 仓库查找用例。
- 🤝 即使没有提案，也可关注、点赞和评论提案，并在社交媒体和开发者社区分享征集信息。
- 📄 页面内容采用 CC BY 4.0 许可，代码示例采用 Apache 2.0 许可，最后更新于 2026-09-03 UTC。

---

### [在 simdjson 上运行 zod Schemas](https://altinmert.co/blog/running-zod-schemas-on-simdjson/)

**原文标题**: [Running zod Schemas on simdjson](https://altinmert.co/blog/running-zod-schemas-on-simdjson/)

`@ata-project/zod` 是一个桥接库，让开发者继续用 zod 定义 schema，但把验证判定交给基于 simdjson 的 ata 引擎执行。它在保留 zod 语义的前提下，大幅优化了“拒绝”这一热路径：拒绝一个大对象时，zod 需约 1,419ns 急切构建错误对象，而桥接可降到 6.7ns。为避免失真，它不盲目运行 zod 转换出的 JSON Schema，而是先对 zod 定义树分类，精确模式走 ata、混合模式由 zod 确认接受，未知特性一律退回 zod，从而保证“可以变慢，但永远不会变错”。0.2.0 还新增 `isValidBytes`，可直接从原始字节给出判定。

- ⚡ **zod 的痛点**：`safeParse` 接受九字段对象约 526ns，拒绝约 1,419ns；拒绝更贵，因为 zod 会急切构建永远可能不被读取的错误对象
- 🌉 **桥接方式**：schema 仍是 zod，判定来自 ata 引擎；`compile(user)` 后可用 `isValid`、`safeParse`、`isValidBytes`
- 🧭 **不盲跑转换结果**：zod 4 转 JSON Schema 有损（refinement/transform 被丢、coercion 被丢），桥接改为遍历 zod 定义树并分类
- 🎭 **三种运行模式**：精确转换只跑 ata；可证明更宽松的走混合模式（ata 拒绝为最终、zod 确认接受）；coercion、catch、preprocess 及未知节点一律走 zod
- 🔬 **差分验证**：对 13,030 个生成值与 zod 本身做差分测试，并在阻止代码生成的情况下把整个测试套件再跑一遍
- 🚫 **拒绝才是产品**：`isValid` 不构建任何对象；被拒的 `safeParse` 返回惰性结果，`ZodError` 在首次属性读取时才构造，大多数拒绝仅 6.7ns
- ✅ **接受仍归 zod**：`z.object` 的剥离未知键、默认值填充、transform 重写等由 zod 负责，`safeParse` 返回的正是 zod 的返回值
- 🆕 **0.2.0 新 API `isValidBytes`**：接收 Buffer/Uint8Array/JSON 字符串，无需 `JSON.parse`、无需物化 JS 对象；非法 JSON 视为拒绝而非异常
- 📊 **字节级判定对比**（parse+safeParse vs isValidBytes）：0.2KB 拒绝 1.6µs→0.6µs；22.7KB 拒绝 81µs→46µs；229KB 拒绝 791µs→482µs
- 🐛 **修复的 bug**：缓冲区路径上拒绝曾比接受贵近两倍，原因是字节码计划对“约束违反”和“遇到组合关键字无法判定”都返回同一个 false，导致二次全量遍历；现在让计划区分 false 的含义
- 🛡️ **无代码生成时的回退**：在严格 CSP 或受限边缘运行时，`z.compile` 以未编译 zod 速度运行（每次拒绝 2,250ns），桥接则回退到 ata 解释引擎，拒绝仅 112ns
- 📈 **性能汇总**：verdict 接受 526ns→21ns，拒绝 1,419ns→5ns；safeParse 拒绝 1,419ns→6.7ns；接受 526ns→542ns（设计上保持 zod 速度）
- 🔗 **可自行验证**：在线对比测试、npm 包、GitHub 代码与差分测试套件均已公开；作者表示若测得不同结果，欢迎反馈

---

### [](https://blog.gaborkoos.com/posts/2026-09-08-Half-Past-Fetch/)

**原文标题**: [Half Past Fetch](https://blog.gaborkoos.com/posts/2026-09-08-Half-Past-Fetch/)

这篇文章的核心是：`await fetch(url)` 只等到 HTTP 响应头，而不是整个响应。promise 在最后一个响应头字节到达时即刻 settle，此时 body 仍是一个正在接收数据的活跃 ReadableStream。这个看似微小的间隙带来一连串后果——连接被占用、`clone()` 只是对活跃流做 tee、abort 在 promise resolve 后仍然生效、基于 race 的超时只覆盖头部阶段——文章用 Node 与浏览器实验逐一验证，并指出正是这个特性让流式进度等能力成为可能。

- 🔍 **await fetch 只等到了一半**：promise 在响应头完成时 settle，body 仍在传输，所以通常需要 await 两次
- 📜 **规范层面**：HTTP-network fetch 在最后一个 header 字节处退出循环，挂上新的 ReadableStream；processResponse 被排为任务，规范明确注明 body 的流此后仍在被 enqueue
- 🧪 **实测差距**：httpbin drip 示例中 headers 在 250ms 可读，body 在 3445ms 才结束；普通端点上两者只差不到 1ms，因此极易被忽视
- 🚫 **例外情况**：HEAD 请求与 null body 状态码（101、103、204、205、304）的 body 为 null，没有后续传输
- 🔌 **连接仍归你所有**：状态码不合意就提前返回而不读 body，HTTP/1.1 下连接无法交回连接池，只能被关闭
- 📊 **Node 基准**：16KB 以下响应已被完全缓冲，读不读都一样；16KB 以上每忽略一次就多耗一条连接（10 个请求用 10 条而非 2 条）
- 🌐 **运行时差异**：Chrome 可容忍 512KB 乃至更大的未读 body，比 Node 的边界高两个数量级，两边都依赖底层缓冲区大小，不能作为可靠保证
- 🚫 **cancel() 换不回连接**：显式取消流与直接无视 body 的计数完全相同，只有读到末尾才能把连接还给连接池
- 📈 **失败是渐进的**：不会卡死或报错，只是连接数增长、文件描述符堆积，客户端池随压力涨落，因此可在生产环境潜伏很久
- 💧 **根因是背压**：网络层填满内部缓冲后停止从 socket 拉取，等待一个永远不会到来的读者
- 👥 **clone() 什么都不复制**：规范定义就是"tee body's stream"，相当于在仍在运行的管道上分叉，两个分支被绑在一起
- 💾 **代价是内存**：60MB 响应下，放弃一个分支约多占 55MB（116.1MB → 169.3MB），与响应体大小相当
- 📦 **数据被保留而非重取**：读完第一分支、等 500ms 后再读被弃分支，仍在 32.5ms 内拿到完整 60MB
- ⏱️ **顺序规则**：必须在任何 pull 之前调用 clone()，读取后再 clone 会抛 "Body has already been consumed"；bodyUsed 按对象区分
- ⚠️ **取消克隆的陷阱**：await copy.body.cancel() 会死锁，它要等另一分支读完；不 await 也要等原分支结束才 settle
- 🛑 **Abort 比 promise 活得久**：resolve 后 abort 仍会在下一次 body 读取时抛 AbortError，已到手的 chunk 依然有效；写入端会收到 aborted，是真正的断连
- 🧩 **便捷方法无法给出部分结果**：arrayBuffer/json/text 被 abort 就直接 reject，想保留已收数据必须用 getReader()
- ✅ **读取完成后 abort() 是空操作**：不抛错，可安全放在清理路径，但调用成功并不代表真的取消了什么
- ⏰ **Promise.race 超时只覆盖头部阶段**：慢 body 场景下 race 在 59.7ms 结束，请求却在 1251ms 才真正完成，200ms 预算在关键部分开始前就用尽了
- ⏳ **AbortSignal.timeout 覆盖全程**：作为请求信号传入并附着到 body，在哪个阶段超时就在哪个阶段生效，慢 body 与慢 headers 都在约 200ms 被切断
- 🖥️ **Chrome 后台标签页陷阱**：后台标签的 setTimeout 被钳制到约 1 秒，200ms 预算要 800ms 后才触发，正确行为看起来像坏了
- 🔗 **组合信号**：用 AbortSignal.any 合并调用方信号、转换器信号、超时信号与内部控制器信号，任一方触发都会中止请求
- 🔄 **读取 body 才是真正的工作**：也是这一切的正面价值——仍是活跃流才能被 pipeThrough 观察进度，示例中 promise 在 52ms settle，25%/50%/75%/100% 分布在随后的 1257ms 里
- 📐 **包装很重要**：pipeThrough 返回的是流，需用原 status 与 headers 重建 Response，下游调用方对此毫无感知（ffetch 的 download-progress 插件即此思路）
- 🧭 **结论**：await fetch(url) 应读作"头部已完成、body 即将开始"的那一刻；连接、内存、取消与超时都属于它之后的部分，之后写的代码才决定这一部分如何收场

---

### [未找到标题](https://www.solidjs.com/blog/async-solid-one-graph-two-machines)

**原文标题**: [No title found](https://www.solidjs.com/blog/async-solid-one-graph-two-machines)

目前尚未提供需要总结的正文内容，因此无法生成有效摘要。请粘贴文章、链接内容或需要总结的文字，我会立即按中文格式整理。

- 📄 未检测到可总结的文本内容。
- ✍️ 请提供文章正文、链接内容或需要摘要的文字。
- 🌐 摘要将使用中文输出，并包含概览与要点列表。
- ✅ 每条要点会使用“-”符号，并搭配合适 emoji。

---

### [27.4KB 语言无关的 WebGPU 语法高亮器](https://gpu-lexer.vercel.app/)

**原文标题**: [27.4KB language-agnostic WebGPU syntax highlighter](https://gpu-lexer.vercel.app/)

gpu-lexer 是 Vercel Labs 的 Shu Ding 开发的一款基于 WebGPU 的实验性语法高亮器，采用语言无关的设计思路：用统一的 tokenizer 和分类器，从上下文推测每个代码片段的类型，而不是为每种语言编写语法规则。它在留出集上与 Shiki 的标签一致率为 88.02%，速度远快于主流高亮库，体积也更小，但官方强调这是概率性实验工具，并非解析器或编译器、linter 的替代品。

- 🧠 **核心原理**：gpu-lexer 先把源码拆成词、空白、换行和符号等简单单元，再用一个仅 41,321 参数的小型 WebGPU 模型结合局部与全文件上下文，为每个单元打上 9 类标签（plain、comment、string、number、keyword、type、function、constant、operator），相邻同标签片段合并为语法 span。
- 🌐 **语言无关**：不依赖具体语法，即使训练时从未见过该语言或语法也能推测标签类型；"语言无关"指共享同一套 tokenizer 和分类器，并不代表每种语言准确率相同。
- 📊 **准确率**：在未参与训练的文件上，88.02% 的 token 标签与 Shiki 一致（11.98% 不同）；该指标衡量的是与 Shiki 的一致性而非客观正确性，未见语言或真实代码的差异可能更大。
- 🧩 **混合语言支持**：可处理 HTML、Vue、Svelte 中嵌入的 `<script>` 和 `<style>` 区域等多语言混排代码。
- 📈 **分语言表现**：91 种已验证语言中，actionscript-3、angular-html、angular-ts、dart、jsx、python、svelte、tsx 等达到 95–100%；javascript、typescript、css、html、go、rust 等在 80–95%；jinja、vb 低于 50%；样本较少的语言结果不太稳定。
- ⚡ **性能优势**：高亮 10 份拼接的 three.min.js（5.56M 字符）时，gpu-lexer 仅需 402.0ms，远快于 Sugar High（836.2ms）、Prism.js（1.16s）、Highlight.js（1.29s）、Starry Night（11.0s）和 Shiki（29.6s）。
- 📦 **体积小巧**：gpu-lexer 单一模型仅 27.4KB，且所有语言共用同一 bundle；相比之下 Shiki 的 6 种主要 Web 语言包为 213.9KB，全语法包高达 991.5KB。
- 🏆 **流行度加权一致性**：在 GitHub Innovation Graph 2026-Q1 前 25 语言的 1,103 个留出文件上，gpu-lexer 得分 90.35%，高于 Prism.js（86.93%）、Highlight.js（84.31%）、Starry Night（81.89%）和 Sugar High（75.93%）。
- 🧪 **实验性质**：官方明确提示高亮结果是概率性的，可能与 Shiki 存在差异，不能当作解析器，也不能替代编译器、linter 或安全分析工具。
- 🎮 **在线体验**：提供覆盖 75 种语言的实时演示，包含 react.development.js、lodash.js、three.min.js、各类框架与配置文件等丰富样本。

---

### [](https://rslib.rs/blog/v1-0)

**原文标题**: [Announcing Rslib 1.0 - Rslib](https://rslib.rs/blog/v1-0)

Rslib 1.0 正式发布：这是一个基于 Rsbuild 的 JavaScript 库开发工具，面向工具库、UI 组件库、CLI 和 Agent 应用，旨在用统一、简单的方式完成构建、声明生成与发布准备。

- 🎉 Rslib 1.0 于 2026 年 9 月 3 日发布，标志着配置模型与 JavaScript API 趋于稳定，并将遵循 SemVer。
- 🧱 基于 Rspack/webpack 生态，支持 Rsbuild、Rspack、webpack 的插件和 loader，便于与应用工程共享配置。
- 🌐 除 ESM、CJS、UMD、IIFE 外，还支持 Module Federation 输出，可让库作为远程模块被多个应用运行时加载。
- 🛠️ 提供统一库构建管线：一次构建内完成 JS 编译、框架语法转换、声明生成和静态资源处理。
- ⚡ 相比 0.7.0，1.0 在 1 万个 React 组件基准中：无缓存构建快约 24.3%，缓存构建快约 56.7%，Gzip 前体积减少约 32.2%，Gzip 后减少约 4.1%。
- 🔄 自 0.7 公开发布以来已推出 16 个 minor 版本，1.0 在持续改进后稳定了公共 API。
- 📦 支持 bundle 与 bundleless 两种构建模式，分别适合 SDK/CLI 与组件库、工具库、monorepo 内部包。
- 🧩 可构建 React、Vue、Svelte、Solid 组件库，并通过 create-rslib 模板和 Rsbuild 插件开箱即用。
- 🧾 支持 dts 声明生成；可用 TypeScript 7 或 isolated declarations 加速，示例中分别约提升 2.4× 和 4.2×。
- 🧪 提供实验性可执行文件生成能力，基于 Node.js SEA，适合分发未安装 Node.js 环境下的 CLI。
- 🎨 内置 CSS Modules、PostCSS、样式提取/内联/压缩，并支持 Sass、Less、Stylus、Tailwind CSS。
- 🖼️ 支持静态资源、JSON import attributes、new URL()、Web Workers、Wasm 及 ESM Wasm 集成。
- ⚙️ 使用灵活：可 CLI 无配置构建，也可用配置文件；提供 JavaScript API，支持 Node.js、Deno、Bun。
- 🔍 与 Rstest、Rspress、Rsdoctor、publint、arethetypeswrong 集成，覆盖测试、文档、构建分析和发布前检查。
- 🤖 提供 Agent Skills、llms.txt/llms-full.txt 和 AGENTS.md，方便 Coding Agent 获取最佳实践与项目上下文。
- 🚀 新手可通过 StackBlitz 或 Quick start 上手；0.x 升级到 1.0 需注意破坏性变更并参考迁移指南。
- 🔭 未来将继续优化 ESM/CJS 输出、Node.js 打包、声明生成效率，并加强测试、文档、质量检查与发布流程集成。

---

### [](https://vitest.dev/blog/vitest-5)

**原文标题**: [Vitest 5.0 is out! | Vitest](https://vitest.dev/blog/vitest-5)

Vitest 5 于 2026 年 9 月 3 日发布，核心亮点是大幅性能优化，并带来 Trace View、嵌套项目、vi.when、基准测试重写、更严格断言等新特性；升级需 Vite >= 6.4.0 和 Node.js >= 22.12.0。

- 🚀 Vitest 5 是新的主版本，感谢 790+ 贡献者，并提供文档、迁移指南和 GitHub Changelog。
- ⚡ 性能是本次重点：基于真实项目基准测试，vm pools、Browser Mode 和大型隔离套件提升显著，例如 deps-heavy 降低 53%、long-haul 降低 25%、enterprise-monolith 降低 19%。
- 🧩 性能改进包括：内联项目共享 Vite server、稳定 fsModuleCache、减少主进程与 worker 往返、更快 vm pools、更快 Browser Mode、更小安装体积和更快覆盖率。
- 🔍 新增内置 Trace View：Browser Mode 可记录交互、断言和 page.mark 为 DOM 快照，并在浏览器 UI、Vitest UI、HTML reporter 中逐步回放，适合本地调试和 CI 失败排查。
- 🗂️ 嵌套项目与配置继承：内联项目默认继承根配置；test.projects 中的配置可再声明 projects，形成嵌套项目；--project 支持层级并新增 -p 简写。
- 🎭 新增 vi.when：可按参数为 spy 定义不同行为，支持深度相等和 expect.any() 等非对称匹配，可用 thenReturnOnce/times 限制，并用 toHaveBeenExhausted 检查行为是否耗尽。
- 🧪 基准测试 API 重写：bench 成为 test() 上下文 fixture，可用 fixtures、hooks、retries、过滤和断言；支持 writeResult、bench.from()、自定义 provider，并进入默认和 json reporter。
- ♿ Locator 错误显示 ARIA 树：找不到元素时打印 ARIA 快照，可通过 browser.locators.errorFormat 控制；locators.exact 默认开启，匹配更严格。
- ⏳ 假定时器现在也 mock Temporal API，适用于 vi.useFakeTimers() 和 vi.setSystemTime()，可通过 toNotFake 排除。
- ✅ 断言更严格：resolves/rejects/toMatchFileSnapshot 未 await 会失败；expect.poll 超时拒绝并传 AbortSignal；matcher 类型暴露返回类型和接收类型。
- 🧹 clearMocks 默认开启：每个测试前自动 vi.clearAllMocks()，避免 mock 调用历史跨测试污染，可通过 clearMocks:false 恢复旧行为。
- 📦 报告器默认写入单个 .vitest 目录；HTML reporter 支持 singleFile 单文件报告；新增 vitest.createReport(scope) 供第三方报告器使用。
- 🛠️ 其他改进包括：--repeats 重复测试找 flaky、injectCjsGlobals 可关闭 CJS 全局注入、coverage.autoAttachSubprocess、perFile 阈值、json filterMeta、junit 命名选项、TestCase.logs() 等。
- ⚠️ 破坏性变更：要求 Vite >= 6.4.0、Node.js >= 22.12.0，升级前建议查看迁移指南和完整 changelog。
- 🙏 致谢 Vitest 团队、贡献者、VoidZero、Chromatic 及所有赞助者。

---

### [htmx 4 有哪些新特性 ~ htmx](https://four.htmx.org/docs/whats-new-in-htmx-4)

**原文标题**: [What's New in htmx 4 ~ htmx](https://four.htmx.org/docs/whats-new-in-htmx-4)

htmx 4.0 是一次全面升级：包含破坏性变更、重命名与移除，以及大量新属性、事件、配置、交换能力和核心扩展；核心变化是改用 fetch()、显式继承、统一命名与更强的扩展/安全支持。

- 🚀 破坏性变更：所有请求改用原生 fetch() 替代 XMLHttpRequest，且不可回退。
- 🧬 显式继承：属性需加 :inherited 才向下继承，:append 可追加到继承值；可用 config.implicitInheritance 恢复旧行为。
- ⚠️ 错误响应：htmx 4 会交换所有 HTTP 响应，仅 204/304 不交换；4xx/5xx 的 HTML 也会进入目标，可用 hx-status 或 noSwap 控制。
- 📝 表单/触发：hx-delete 不再包含所在表单数据，需加 hx-include="closest form"；hx-trigger 的 queue 修饰符移除，改用 hx-sync。
- 🧭 历史/OOB：历史不再用 localStorage 缓存，回退时重新请求并交换；OOB 与 hx-partial 改为在主内容之后交换。
- ⏱️ 默认与扩展：默认超时改为 60 秒（defaultTimeout=60000）；扩展脚本直接引入，不再用 hx-ext，可用 meta 的 htmx-config 限制扩展。
- 🔤 属性重命名：hx-disable→hx-ignore，hx-disabled-elt→hx-disable（升级前先做前者）；hx-vars/hx-params/hx-prompt/hx-ext/hx-disinherit/hx-inherit/hx-request/hx-history 等移除或替代。
- 📣 事件重命名：统一为 htmx:phase:action[:sub-action]，如 htmx:afterRequest→htmx:after:request；错误多合并为 htmx:error，HTTP 错误用 htmx:response:error。
- ⚙️ 配置重命名：defaultSwapStyle→defaultSwap、globalViewTransitions→transitions、historyEnabled→history、includeIndicatorStyles→includeIndicatorCSS、timeout→defaultTimeout；defaultSettleDelay 改为 1，多个旧配置移除。
- 📨 请求/响应头：HX-Trigger→HX-Source 且格式为 tagName#id，HX-Target 也用该格式；新增 HX-Request-Type、Accept；HX-Trigger-After-Swap/Settle 移除，HX-Trigger 不变。
- 🧩 JS API：移除 addClass/removeClass/toggleClass/closest/remove/off/location/logAll/logNone/logger 等，defineExtension→registerExtension；保留 ajax/config/find/findAll/on/onLoad/process/swap/trigger 等。
- 🆕 新属性：hx-action、hx-method、hx-query、hx-config、hx-ignore、hx-validate 等。
- 🔄 交换增强：show/scroll 改为 show:top showTarget:#other 等分离语法；新增 innerMorph/outerMorph、textContent、delete；before/after/prepend/append 为旧别名。
- 🎯 状态码交换：用 hx-status:422 或 hx-status:5xx 按状态码配置 swap/target/select/push/replace/transition，支持精确、单数字和范围通配。
- 🧩 <hx-partial>：一次响应可显式更新多个目标，每个 hx-partial 自带 hx-target 和 hx-swap，适合替代 hx-swap-oob 的复杂场景。
- ✨ 新能力：支持 View Transitions（默认关闭）、JSX 兼容 metaCharacter、htmx.timeout()、自动控制台日志、事件 ctx 请求上下文。
- 📅 新事件：htmx:after:cleanup、htmx:after:history:update、htmx:after:process、htmx:before:response、htmx:before:settle、htmx:after:settle、htmx:before:viewTransition、htmx:after:viewTransition、htmx:finally:request 等。
- ⚙️ 新配置：extensions、mode、inlineScriptNonce、metaCharacter、morphIgnore、morphScanLimit、morphSkip、morphSkipChildren 等。
- 🧱 核心扩展：新增/重写 hx-multipart、hx-sse、hx-ws、hx-browser-indicator、hx-live、hx-pending、hx-prompt、hx-preload、hx-history-cache、hx-ptag、hx-download、hx-head、hx-targets、hx-upsert、htmx-2-compat、hx-alpine-compat、hx-csp 等。

---

### [NestJS v12 现已发布 - Trilon Consulting](https://trilon.io/blog/nestjs-12-is-now-available)

**原文标题**: [NestJS v12 is Now Available - Trilon Consulting](https://trilon.io/blog/nestjs-12-is-now-available)

NestJS 12 正式发布，这是多年来最重大的平台更新，覆盖框架、CLI、默认工具链和文档；核心转向 ESM-first，但 CommonJS 仍可平滑升级，并带来 Standard Schema、原生可观测性、微服务、GraphQL/WebSocket、CLI 与官网文档等大量改进。

- 🚀 NestJS 12 是多年来最重要的平台更新，涉及核心框架、CLI、默认工具链和官方文档。
- 📦 核心包转为 ESM-first，这是社区长期呼声；但应用代码迁移到 ESM 是可选的。
- 🛠️ CLI 新增 `nest upgrade`，可更新依赖并保留现有模块格式，不会自动把源码改成 ESM。
- 🆕 `nest new` 可选择 CommonJS 或 ESM；ESM 项目默认使用 Vitest 和 oxlint，CJS 项目继续使用 Jest 和 ESLint。
- ⚙️ Rspack 取代 webpack 成为 monorepo 默认打包器；`--webpack`/`--webpackPath` 弃用，新增 `--rspackPath`，但 `tsc` 仍是标准项目默认编译器。
- 🧰 CLI 还新增 `--emit-declarations`、`--no-type-check`、`--silent`、`--parallel`、`includeLibraryAssets` 和 `nest deploy`。
- ✅ 支持 Standard Schema：`@Body()`、`@Query()`、`@Param()` 可传入 schema，兼容 Zod、Valibot、ArkType；`@nestjs/config` 的 `validationSchema` 也支持。
- ⚠️ Standard Schema 不替代 class-validator，而是额外选项；Joi 用户需升级到 Joi v18+ 并调整 `validationOptions.libraryOptions`。
- 🧾 `ConsoleLogger` 支持结构化日志参数；JSON 模式下默认放入 `params`，可用 `flattenParams` 展平。
- 🧩 `HttpExceptionOptions` 新增 `errorCode`，错误响应可包含机器可读错误码。
- 🛣️ 路由器可检测影子路由和重复路由，新增 `routeConflictPolicy` 与 `routeResolutionStrategy` 选项。
- 🔭 推出 `@nestjs/observe`，通过 `instrument` 选项原生接入请求生命周期，自动采集请求、后台任务、错误、日志和追踪。
- 🧵 微服务改进包括 NATS v3、Kafka 正则主题、预请求钩子、gRPC 异常过滤器。
- 🌐 GraphQL 默认使用 GraphiQL，移除 `subscriptions-transport-ws` 并转向 `graphql-ws`；WebSocket 支持请求作用域网关和断开原因。
- 🛑 Express 应用支持优雅关闭；生命周期钩子按组件层级调用；`PipeTransform` 类型更安全。
- 💻 运行 NestJS 12 需要 Node.js v20.19+ 或 v22.12+。
- 🎨 nestjs.com 与官方文档迎来近九年首次大改版，阅读体验和导航更清晰。
- 🔄 迁移方式：安装最新 CLI 和 schematics 后运行 `nest upgrade`；如需 ESM，可添加 `type: module`、`nodenext`、显式 `.js` 扩展名并替换 `__dirname`。

---

### [](https://github.com/microsoft/playwright/releases/tag/v1.63.0)

**原文标题**: [Release v1.63.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.63.0)

Playwright v1.63.0 已发布，重点增强测试并行控制、跨 iframe/可见元素定位、步骤报告、Trace 调试与快照能力，并带来多项 API、测试运行器、CLI、报告器及平台支持更新。

- 📦 **发布信息**：v1.63.0 由 yury-s 于 9 月 4 日 22:40 发布，提交通过 GitHub 验证签名。
- 🔒 **测试锁**：测试可声明命名 `lock`；同名锁测试不会跨文件、worker、项目并发，支持多个锁和 `test.describe()` 组级锁。
- 🪟 **跨 frame 定位**：`page.frameLocator()` 与 `frame.frameLocator()` 无选择器时会在子树任意 frame 中搜索；若匹配多个 frame 会报错。
- 👁️ **仅可见定位器**：新增 `locator.visible()`，只匹配可见元素，推荐替代 `:visible` CSS 伪类。
- 🧾 **步骤参数与字幕**：Playwright API 步骤报告目标 locator 与调用参数；`test.step()` 支持 `subtitle` 和 `params`，并在 Trace Viewer/HTML 报告中显示。
- 🖼️ **Trace 增强**：`tracing.start()` 与 `testOptions.trace` 的 `snapshots` 可对象选择 `dom`、`aria`、`screen`；Trace Viewer 新增 Display Aria 模式，可悬停高亮。
- 🆕 **新 API**：`httpCredentials` 支持凭据数组；`opfs` 纳入存储状态；新增 `dialogclosed` 事件；新增 `ariaSnapshotJSON()`；请求方法支持响应类型泛型。
- 🧪 **测试运行器**：新增 `reducedMotion`、`forcedColors`、`contrast` 选项；`--add-reporter` 追加报告器；报告器新增 `omitTags` 隐藏自动附加标签。
- 💻 **命令行**：`playwright install --no-remove` 保留其他安装的浏览器；`playwright codegen --http-credentials` 可录制 HTTP 认证页面。
- 🧰 **杂项**：新增内置 `perfetto` 报告器输出 Trace Event Format；HTML 报告在测试步骤旁显示时长瀑布。
- ⚠️ **公告**：`@playwright/experimental-ct-react`、`ct-react17`、`ct-vue` 不再更新，需按迁移指南转向 stories 模型；Ubuntu 20.04 不再支持；Linux arm64 改用 Chrome for Testing Chromium。
- 🌐 **浏览器版本**：Chromium 153.0.8010.12、Firefox 155.0、WebKit 26.6；并测试兼容 Google Chrome 153 与 Microsoft Edge 153。

---

