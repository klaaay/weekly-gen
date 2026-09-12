### [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3)

**原文标题**: [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3)

React 19.3 已发布，核心亮点是 View Transitions 与 Fragment Refs 正式稳定，并带来 React DOM、Server Components 的重要增强及多项修复。

- 🚀 React 19.3 现已在 npm 发布，View Transitions 和 Fragment Refs 从实验性 API 转为稳定功能。
- 🎬 `<ViewTransition>` 可基于 enter、exit、update、share 使用浏览器 View Transition API 动画 UI，默认交叉淡入淡出，也支持 CSS 和 Web Animations 自定义；目前仅支持 DOM，React Native 支持仍在开发。
- 🔀 `addTransitionType` 可标记过渡原因，让同一状态更新根据“前进/后退”等不同场景使用不同动画。
- ⏳ View Transitions 可与 Suspense 集成，动画 fallback 到最终内容；图片、字体等资源也可通过 `<ViewTransition>` 触发 Suspense，建议 fallback 立即出现、内容更新带动画。
- 🧩 Fragment Refs 允许把 ref 传给 `<Fragment>` 获得 `FragmentInstance`，对子 DOM 组执行 focus、事件监听、观察器、测量与滚动等操作，无需额外包装元素或修改组件。
- 🌐 React DOM 新增 `use(browser())`，可让组件在服务端退出 SSR 并触发 Suspense，在客户端不挂起，适合依赖 localStorage、时区等浏览器 API 的组件。
- 🔒 支持 Trusted Types API，避免将 `TrustedHTML` 等对象强制转成字符串，增强对 DOM 型 XSS 的防护。
- 🧠 React Server Components 现在可直接渲染从 `'use client'` 模块导入的 `<Context>`，无需额外 Provider 包装组件。
- 🛠️ 其他变化包括：独立渲染 Transitions、Strict Mode 水合时双调用 Effects、`use` 条件使用警告、`onFullscreenChange/onFullscreenError`、`maskType`、`fetchPriority`、`onReset`、submitter、credentialless、resize 事件批处理等。
- 🐛 修复多项问题，包括 `useDeferredValue` 卡旧值、Suspense fallback 上下文传播、`useSyncExternalStore` 漏更新、`useEffectEvent`、Fast Refresh、`<ViewTransition>` 崩溃、hydration mismatch、Deno 挂起等。
- 🙏 文章由 Sam Selikoff 撰写，Matt Carroll、Dan Abramov、Andrew Clark 审阅；完整变更见官方 Changelog。

---

### [](https://react.dev/blog/2026/09/09/react-19-3#new-react-server-components-features)

**原文标题**: [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3#new-react-server-components-features)

React 19.3 已发布到 npm，核心亮点是将 View Transitions 与 Fragment Refs 从实验性 API 升级为稳定功能，并带来浏览器端渲染、React DOM、Server Components 及大量问题修复。

- 🚀 React 19.3 正式发布，重点包括 View Transitions 和 Fragment Refs 稳定化。
- 🎞️ 新增稳定的 `<ViewTransition>`，可在元素进入、退出、移动、缩放或内容变化时使用浏览器 View Transition API 播放动画。
- 🔄 React 会根据树变化自动选择 `enter`、`exit`、`update`、`share` 动画；只有 Transition 中的更新才会触发动画。
- 🧭 新增 `addTransitionType`，可为同一次状态更新标注原因，从而为“下一页/上一页”等不同场景指定不同动画。
- ⏳ `<ViewTransition>` 可与 `<Suspense>` 集成，实现 fallback 到最终内容的平滑过渡。
- 🖼️ 将图片或字体包在 `<ViewTransition>` 中，可让它们加载时触发 Suspense，避免资源陆续加载造成闪烁。
- 🧩 Fragment Refs 稳定：可把 `ref` 传给 `<Fragment>`，获得 `FragmentInstance`，统一操作子 DOM 节点。
- 🛠️ `FragmentInstance` 支持事件监听、焦点管理、`IntersectionObserver`/`ResizeObserver`、测量与滚动等方法，无需额外包裹元素或修改子组件。
- 🌐 `react-dom` 新增 `browser()`，组件可用 `use(browser())` 选择退出服务端渲染；服务端触发 Suspense，客户端不触发。
- 🔐 支持浏览器 Trusted Types API，React 不再把 `TrustedHTML` 等对象强制转成字符串，有助于防御 DOM XSS。
- 🧵 Server Components 现在可以直接渲染从 `'use client'` 模块导入的 `<Context>`，不再必须导出 Provider 包装组件。
- ⚡ 其他改进包括：Transition 独立渲染、Strict Mode 水合时双调用 Effects、`useActionState` 文案调整、React DOM 新事件与属性支持等。
- 🐛 修复多项问题，如 `useDeferredValue` 卡旧值、Suspense fallback 上下文传播、`useSyncExternalStore` 丢失更新、Fast Refresh 问题、`<ViewTransition>` 在移动端 Safari 崩溃等。
- 📚 完整变更列表可查看官方 Changelog。

---

### [获取失败](https://blog.master.dev/reacts-viewtransition-element/)

**原文标题**: [Failed to retrieve](https://blog.master.dev/reacts-viewtransition-element/)

无法总结：获取内容失败，状态码 429。

---

### [](https://github.com/react/react/releases/tag/v19.3.0)

**原文标题**: [Release 19.3.0 (September 9, 2026) · react/react · GitHub](https://github.com/react/react/releases/tag/v19.3.0)

React 19.3.0 于 2026 年 9 月 9 日发布，新增 View Transition 动画 API、Fragment Refs、browser() DOM API 与 Trusted Types 集成，并带来 Transitions 独立渲染及大量 Fast Refresh、Activity、SSR、RSC 和传输层修复。

- 🚀 **版本发布**：React v19.3.0 发布，标记为最新版本，包含 6 个提交。
- ✨ **新 React 功能**：新增 `<ViewTransition />` 和 `addTransitionType` API，用于支持 View Transition 动画。
- 🧩 **Fragment Refs**：`<Fragment />` 现在支持 refs，以支持可组合的平台行为。
- 🌐 **browser() API**：新增 `react-dom` API，服务端渲染时报错，浏览器中解析；配合 `use(browser())` 可标记浏览器专用子树。
- 📡 **onBrowserBailout**：`react-dom/server` API 新增选项，用于观察子树何时延迟到浏览器处理。
- 🛡️ **Trusted Types**：启用 Trusted Types API 集成。
- ⚡ **Transitions 改进**：Transitions 现在独立渲染，不再纠缠成单次渲染，慢过渡不会阻塞无关过渡。
- ⚠️ **DEV 警告**：当组件疑似因条件调用 `use()` 而解除阻塞时，开发环境会给出警告。
- 🔄 **Fast Refresh 修复**：修复 `lazy()`、`memo()`、组件类型变化、StrictMode 效果重复调用等问题。
- 📊 **Performance Track 修复**：修复 `$$typeof`、非字符串函数名、大对象/数组、Typed Array、性能测量清理等问题。
- 🕵️ **Activity 修复**：修复隐藏树中的 store 变更、portal 内容、metadata hoisting、错误泄漏、Suspense 上下文传播等问题。
- 🧱 **React DOM 更新**：更新 `<select>` 解析、number 输入 `defaultValue`、`nonce`、`fetchPriority`、`credentialless`、全屏事件、表单 submit/reset 等行为。
- 🖥️ **React Server 更新**：支持 import map nonce、onBrowserBailout、Deno 挂起修复、hydration nonce 误报修复、abort 与重试改进等。
- 📦 **React Server Components / Flight**：改进 Flight 协议、调试信息、序列化性能、循环引用保护、DoS 缓解、Error.cause 传输等。
- 👥 **贡献者**：由 sophiebits、sebmarkbage 等 35 位贡献者共同完成。

---

### [Postgres 适用于任意规模的时序工作负载。](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

overview summary
- 🚀 Tiger Data 的 Tiger Cloud 提供面向任意规模时序工作负载的 Postgres 服务，适用于 IoT 等场景。
- 📈 单个 Tiger Cloud 服务可达：每天 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 🎁 新账户注册可得 1000 美元信用额度，30 天有效，无需信用卡。
- 🏭 受数千家 IoT 公司信赖。
- ⚙️ 核心能力包括弹性扩展：读写分离，副本集最多 10 节点，SSD/S3 分层存储，存储近乎无上限且成本高效。
- 💸 计算与存储分离，可独立扩展，避免为空闲容量付费。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复、跨区域备份。
- 🔐 企业级：符合 SOC 2、HIPAA、GDPR，默认加密，支持 SSO、RBAC、审计日志。
- 🔍 深度可观测性：查询下钻和仪表盘，指标可发送至 CloudWatch、Datadog、Prometheus。
- ⚡ 快速启动：几分钟内开通数据库，可用 SQL、CLI、Terraform、Cursor、Claude Code 管理。
- 🔌 集成：支持首选云厂商及更广泛的 Postgres 生态。
- 🏢 企业就绪：合同 SLA、区域数据隔离、合规认证，并有 24/7 全球 Postgres 专家支持。
- 📄 页脚包含隐私偏好、法律、隐私、网站地图，以及 2026 Timescale, Inc. d/b/a Tiger Data 版权信息。

---

### [](https://shopify.engineering/back-to-native)

**原文标题**: [Native is now the future of mobile at Shopify (2026) - Shopify](https://shopify.engineering/back-to-native)

Shopify 宣布移动端战略从 React Native 转向 Swift 和 Kotlin：2020 年 all-in React Native 曾是成功选择，但 LLM/编码代理大幅降低了双平台开发、翻译、测试与审查成本，改变了当初的核心假设；原生开发重新具备优势，因此公司将用 AI 辅助以 greenfield 方式重建核心移动应用。

- 🧭 2020 年 Shopify all-in React Native，收益包括避免重复开发、让非移动背景开发者跨栈贡献、减少功能对齐成本。
- 🤖 Shopify 自 2021 年使用 LLM，到 2025 年模型能力提升，使“在两个平台各建一次”不再等于双倍工作量。
- ⚖️ 重新评估后，原生 Swift/Kotlin 更贴近平台能力与第一方工具，减少框架和依赖层。
- 🧪 原型显示，编码代理可用 iOS 版本参考实现 Android，反之亦然，并降低维护双平台一致性的成本。
- 🏗️ 迁移选择 greenfield 重写，而非渐进式 brownfield，以摆脱历史约束并利用 AI 加速重建。
- 🛍️ Shop 应用已用 12 周从概念验证到完整原生应用上架；300+ 屏幕的 Shopify 应用正在迁移，预计年内发布。
- 🧵 自研 Helix 系统逐步重建界面：按检查点推进，每个检查点须通过测试、视觉对比、两轮对抗审查和人工确认。
- ⚡ 通过 CLI 和 headless 业务逻辑实现毫秒级反馈循环，代理无需模拟器即可迭代；必要时远程驱动模拟器做 E2E 测试。
- 📚 开源库安排：继续赞助 React Native Skia 至 2026 年底并由 William Candillon fork 更名；FlashList 继续关键修复并寻找长期维护方；Restyle 将在 2026 年底后归档。
- 🎯 迁移不是终点，目标是提升产品速度、应用质量和代理自主完成度，同时不降低性能、稳定性、可访问性与产品质量门槛。
- 🙏 文章感谢 Meta、William Candillon、Software Mansion、Shopify 工程师和 React Native 社区，并正在招聘移动、基础设施及 AI 软件工程人才。

---

### [将 Shop 应用从 React Native 迁移到原生（2026）- Shopify](https://shopify.engineering/shop-app-migration)

**原文标题**: [Migrating Shop app from React Native to native (2026) - Shopify](https://shopify.engineering/shop-app-migration)

Shop 应用在 AI 编码代理协助下，用 12 周从 React Native 迁移到 Swift 和 Kotlin 原生应用；迁移旨在利用编码代理改变共享代码库的权衡，并避开即将到来的 React Native 新架构投入。结果在启动速度、稳定性、Android 包体和构建时间上显著改善，同时保持用户登录、推送和关键分析事件的连续性。

- 📱 背景：Shop 自 2020 年起采用 React Native，服务数亿顾客和数百万商家；因编码代理进步，团队重新评估原生开发成本。
- 🧠 动因：原需为 React Native 新架构重访原生模块、渲染和共享/平台边界；先用编码代理验证 SwiftUI 与 Jetpack Compose 直接开发是否可行。
- 🧪 概念验证：一名工程师用一周和编码代理，将现有 React Native 应用尽可能迁移到 SwiftUI；虽未生产就绪，但证明逐功能迁移可行。
- 👥 全面迁移：六名核心工程师搭建原生基础和主要用户旅程，功能团队中途加入验证边缘情况；优先保持功能行为和分析事件。
- 🔄 用户体验：迁移像普通更新，用户保持登录、继续收到推送；交互仍发出下游系统所需事件，并借机精简部分屏幕。
- ⏱️ 启动时间：iOS 从 3200ms 降至 2466ms，减少 23%；Android 从 4433ms 降至 2233ms，减少 50%。
- 🛡️ 稳定性：会话稳定性从 99.5%+ 提升至 99.95%+，崩溃会话减少 10 倍。
- 📦 应用体积：Android 从 293MB 降至 184MB，减少 109MB（37.2%）；iOS 从 67MB 增至 68MB，增加 1MB（1.5%）。
- 🏗️ 构建时间：Android release 构建时间下降约 75%；iOS release 构建时间大致相同。
- 🎞️ 运行性能：原生 Android 在 Pixel 上滚动信息流和导航可达 120 FPS，且优化很少。
- 🤖 代理工作流：多代理会话/工作树并行；给代理清晰任务、快速构建测试循环、频繁评审；为 Pi 编码代理构建可复用迁移工作流。
- 🔍 校验工具：Tardis 让代理访问原生应用实时事件、日志、状态并发送命令；还能截屏和捕获事件窗口，对比 React Native 与原生应用的事件名称、数量和负载。
- 🧑💻 原生专长仍关键：生成代码可能引入重复、架构漂移和性能问题；需仓库指南、lint、测试、静态分析、性能检查和代码评审。
- 🔮 未来：坚持 Android 与 iOS 始终功能对等；当前版本是性能新基线，将继续优化工具和流程。

---

### [](https://www.reddit.com/r/reactnative/comments/1wd8b4d/whats_your_opinion_on_this/)

**原文标题**: [Reddit](https://www.reddit.com/r/reactnative/comments/1wd8b4d/whats_your_opinion_on_this/)

目前未收到需要总结的正文内容，因此无法生成文章摘要。
- 📄 请将文章或文本粘贴到“Use the following content:”之后
- 🧾 收到后我会提取核心信息并生成中文要点
- ✂️ 每个要点将使用“-”开头并配一个合适 emoji
- 🚫 不会编造未提供的内容

---

### [Tailwind Labs](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

**原文标题**: [Tailwind Labs is joining Shopify - Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

Tailwind CSS 创始人宣布 Tailwind 加入 Shopify：框架将获得长期稳定维护，继续以 MIT 开源并由原团队主导；商业业务不再扩展，现有客户保留权益，但停止新用户注册。

- 🚀 Tailwind 正式加入 Shopify，进入新的发展阶段。
- 📊 Tailwind 每周安装量超 1.1 亿次，被 ChatGPT、X、Cloudflare、Reddit、Shopify 等大型公司使用。
- 🏡 加入 Shopify 的核心原因：为 Tailwind 找到长期稳定的家，确保数百万依赖者持续获得维护。
- 🛍️ Shopify 提供真实复杂产品场景：商家店铺、管理后台、结账、Shop app，以及代理式商务探索。
- 🤝 Shopify 是最早大规模采用 Tailwind 的公司之一，不仅自用，也为客户押注，Tailwind 是其关键栈部分。
- 🌱 创始人认同 Shopify 帮助更多人创业的使命，并期待围绕真实产品改进框架。
- 🔓 开源承诺不变：Tailwind CSS 及其他开源项目仍为 MIT 许可，团队继续领导和维护。
- 💼 商业调整：不再围绕 Tailwind 增长商业业务，现有 Tailwind Plus 和 ui.sh 客户保留访问权，但关闭新用户注册，聚焦 Shopify 内的 Tailwind CSS。
- 🙏 感谢社区九年支持，相信 Shopify 是继续推进这项工作的最佳归宿。

---

### [](https://github.com/react/react/blob/main/packages/react-devtools/CHANGELOG.md#800)

**原文标题**: [react/packages/react-devtools/CHANGELOG.md at main · react/react · GitHub](https://github.com/react/react/blob/main/packages/react-devtools/CHANGELOG.md#800)

React DevTools 更新日志记录了从 4.x 到 8.0.0 的演进，核心围绕 Suspense/Server Components 支持、Profiler 能力增强、组件树与检查体验优化、性能提升以及大量缺陷修复。

- 📅 8.0.0（2026-09-08）默认启用 Suspense 标签页，可直接查看组件挂起原因；Timeline profiler 标签页被移除，推荐改用浏览器 Performance 面板。
- 🔍 新增浏览器 Elements 面板中的 React Element 窗格，检查 DOM 节点时可看到匹配的 React 组件。
- 🧭 Profiler 空状态围绕主操作重新设计，并加入组件搜索、父级堆栈工具、忽略列表堆栈帧展开等能力。
- ⌨️ 新增开始/停止 profiling 热键、commit 导航热键，支持自定义 host/port/path 连接，并可在 sandbox CSP 页面中最小支持。
- 🐞 8.0.0 修复大量问题：fallback Fiber 协调、嵌套 HOC 名称提取、重连消息缓冲、WhatChanged 滚动、HTML 注入、内存泄漏、控制台格式化等。
- 🚀 7.0.0（2025-10）新增 “suspended by” 区域，展示 Server Components `await`、`React.lazy`、`use()`、suspensey 图片/CSS/字体等挂起原因。
- ✏️ 7.0.0 新增 Chrome Sources 标签页中的代码编辑器侧边栏，并支持直接在外部编辑器中打开本地文件。
- 🧩 7.0.0 支持流式完成前检查 React 树、Thenables、Error 的 cause/name/message/stack 内省、React Element 与 React.lazy 内省。
- 🐛 6.0.0（2024-09）支持 Server Components 树、按环境名过滤、函数即时检查与点击跳转定义、元素检查更流畅。
- 🧪 5.x 系列加入 `useFormStatus`、`useOptimistic`、`use(Context)`、`useTransition` 挂起状态、Forget/React Compiler 徽章等。
- 🧰 4.x 系列是重大性能与体验升级：消除旧版 DevTools 性能开销，新增组件栈、组件过滤、无内联 props、rendered by 列表与 owners tree。
- 🪝 4.x 改进 hooks 支持：hooks 可像 props/state 一样编辑，可展开对象数组；搜索改为内联高亮，并支持 HOC 徽章。
- 📊 Profiler 持续增强：reload and profile、导入/导出、Why did this render、commit 列表、组件渲染耗时、时间线等。
- 🧵 新增 Scheduling Profiler，展示 React 调度、transition、Suspense、非 React JavaScript 对渲染的影响，并主动提示性能问题。
- 🧑💻 大量 UI/UX 改进：深色主题、面板布局、右键菜单、复制/粘贴、快捷键、可编辑值、主题同步、静态 Components 面板等。
- 🧱 版本兼容与协议：Bridge 协议版本检查、前后端版本不匹配提示、支持多 DevTools 实例与多后端。
- 🔐 扩展与安全：Manifest V3、Edge/Firefox/Chrome 支持、CSP sandbox 最小支持、权限清理、修复若干安全问题。
- 🧹 修复范围广泛：崩溃、内存泄漏、控制台格式化、source map、滚动、过滤、Strict Mode、React Native 等。
- 📦 包与工具更新：react-devtools-core、react-devtools-inline、独立版 Electron、Websocket 重连、NPM 发布说明等持续维护。

---

### [](https://github.com/react/react/tree/main/packages/react-devtools-cdt-mcp)

**原文标题**: [react/packages/react-devtools-cdt-mcp at main · react/react · GitHub](https://github.com/react/react/tree/main/packages/react-devtools-cdt-mcp)

react-devtools-cdt-mcp 是一个实验性浏览器库，用于向 chrome-devtools-mcp 注册 React 检查与性能分析工具；它不是 MCP 服务器，需要在被测试页面中、React 初始化前导入，并依赖新版 chrome-devtools-mcp 与实验性开关。

- 🧪 实验性库：基于 chrome-devtools-mcp 中的实验性第三方开发者工具 API。
- 🌐 用途：在浏览器页面中注册 React inspection 和 profiling 工具，由 chrome-devtools-mcp 发现。
- ⚠️ 非 MCP 服务器：不要放进 MCP 客户端配置；应导入到被测页面里。
- 📦 安装：`npm install react-devtools-cdt-mcp`。
- ⏱️ 使用：在 React 之前导入 `react-devtools-cdt-mcp/register`，确保 DevTools hook 先安装；该入口在非浏览器环境会抛错。
- 🧩 包根无副作用：导出 `register`、`buildToolGroup` 等底层 API，供自定义目标使用。
- ⚙️ 依赖要求：需要 chrome-devtools-mcp 1.3.0+，并启用 `--categoryExperimentalThirdParty=true`。
- 🔧 调用方式：页面运行在 chrome-devtools-mcp 下时，可通过 `list_3p_developer_tools` 列出工具，并通过 `execute_3p_developer_tool` 或 `evaluate_script(window.__dtmcp.executeTool(...))` 调用。
- 🔒 安全提示：工具可能向 MCP 客户端暴露组件 props 和 hook 值，只应在本地或可信调试会话中使用。
- 🆔 UID 约定：组件用稳定 uid 标识，如 `r5`；跨工具和重渲染一致，但页面刷新后不保留。
- 📤 输出约定：所有工具返回普通 JavaScript 值；失败时返回 `{error: string}`。
- ⏳ 时长约定：profiler 时长单位为毫秒；构建未收集 profiling 计时时为 `null`。
- 🌲 `react_get_component_tree`：获取组件树快照，可指定 `depth` 和 `rootUid`，返回节点数组。
- 🔍 `react_get_component_by_uid`：按 uid 获取组件详情，可选 `includeHooks`；检查 hooks 会重新渲染组件 render 函数，但不运行 effects。
- 🧭 `react_get_component_by_dom_element`：获取 DOM 元素对应的 React host 组件详情，元素引用以 `{uid: string}` 传入。
- 🔎 `react_find_components`：按名称子串、不区分大小写查找组件，支持子树限制和分页。
- 📍 `react_get_component_source`：获取组件定义源码位置；无法确定时返回 `source: null`。
- 🧵 `react_get_owner_stack_trace`：获取原始 owner 堆栈，即 JSX 创建位置链，DEV-only。
- 🪜 `react_get_parent_stack`：获取渲染父级列表，从直接父级到根。
- 👑 `react_get_owner_stack`：获取结构化 owner 列表，表示哪些组件通过 JSX 创建/渲染了该元素，DEV-only，且不是结构父级。
- 🟢 `react_start_profiling`：启动记录每次 commit 渲染计时的 profiling 会话。
- 🔴 `react_stop_profiling`：停止 profiling，返回 `traceName` 和记录的 commit 数量。
- 📊 `react_get_trace_overview`：获取某 trace 的逐 commit 概览，包括 render/layout/passive 时长和变更组件数。
- 📝 `react_get_commit_report`：获取单个 commit 的详细报告，组件按 `actualDuration` 降序排列。

---

### [](https://tanstack.com/blog/vercel-partnership)

**原文标题**: [TanStack + Vercel Partnership | TanStack Blog](https://tanstack.com/blog/vercel-partnership)

TanStack 宣布 Vercel 成为其金牌合作伙伴，双方已在多个层面展开深度集成。

- 🤝 Vercel 成为 TanStack 金牌合作伙伴，为其开源工作提供资金支持
- 🚀 TanStack Start 应用可部署至 Vercel，支持基于 Git 的部署和预览 URL
- 🔌 `@tanstack/ai-vercel-gateway` 适配器将 TanStack AI 连接至 Vercel AI Gateway，支持聊天、嵌入、图像生成和摘要功能，可通过单一 API 密钥路由多个模型提供商
- ⚙️ `@tanstack/ai-sandbox-vercel` 将 Vercel 托管微虚拟机接入 TanStack AI 沙箱系统，支持按 ID 恢复沙箱、保留文件及暴露开发服务器端口
- 📖 部署和 AI 集成文档可在 TanStack 的 Vercel 合作伙伴页面查看

---

### [](https://expo.dev/blog/an-early-look-at-expo-modules-2-0)

**原文标题**: [An early look at Expo Modules 2.0 â Expo blog](https://expo.dev/blog/an-early-look-at-expo-modules-2-0)

请提供需要总结的文本内容；当前消息中“Use the following content:”之后没有正文，因此暂时无法生成有效摘要。

- 📭 当前未收到可总结的文章、段落或材料。
- 🧾 收到内容后，我会用中文输出“概述摘要 + 要点列表”。
- ✅ 每个要点会以“-”开头，并配一个合适的 emoji。
- 📌 请直接粘贴正文，我会立即按要求整理。

---

### [获取失败](https://blog.master.dev/react-now-rusted-all-the-way-out/)

**原文标题**: [Failed to retrieve](https://blog.master.dev/react-now-rusted-all-the-way-out/)

无法总结：获取内容失败，状态码 429。

---

### [](https://swmansion.com/blog/what-it-actually-takes-to-migrate-discord-to-react-native-s-new-architecture/)

**原文标题**: [What It Takes to Migrate Discord to RN's New Architecture](https://swmansion.com/blog/what-it-actually-takes-to-migrate-discord-to-react-native-s-new-architecture/)

Discord 将移动端应用迁移至 React Native 新架构的真实经历：最难的不是“切换开关”，而是切换之后漫长的长尾问题。Software Mansion 团队嵌入 Discord 移动团队近一年，协助 iOS 完成迁移，期间处理了大量因底层架构变化而暴露的隐性假设失效问题。文章通过三个典型案例（坐标系原点变化、手势目标因视图扁平化失效、类名未加 Manager 后缀导致死锁）说明问题根源，并总结了排查方法、对社区的贡献以及给迁移团队的建议。

- 📊 **迁移工作的真实分布**：真正的基础设施迁移（构建系统、代码生成、依赖升级）仅占 14%；渲染/布局/视觉问题占 47%，崩溃与稳定性占 16%，性能占 13%，输入（键盘/手势）占 11%。
- 🧩 **核心问题不是“Bug”，而是隐性契约改变**：许多问题并非代码错误，而是旧架构下成立的隐含假设在新架构下不再成立——视图位置、原生节点是否存在、框架如何找到原生代码。
- 📐 **坐标系原点变化**：旧架构测量返回窗口坐标，Fabric 下视图相对于 Yoga 根节点测量，而模态框是独立根节点。Discord 的上下文菜单在 `FullWindowOverlay` 中渲染，从模态框内打开时坐标被误读，导致菜单偏移。
- ✋ **手势目标因视图扁平化而失效**：Fabric 的视图扁平化优化会根据 props 动态决定是否创建原生宿主节点。录音时辅助功能属性变化导致容器原生视图被替换，进行中的手势被取消，松开按钮无法停止录音。修复方式为添加 `collapsable={false}`。
- 🔒 **类名未加 Manager 后缀导致应用冻结**：遗留视图管理器 `NativeLottieNode` 未遵循 Fabric 快速查找路径所需的 `Manager` 后缀，触发慢路径，在后台线程与主线程之间形成死锁，滚动动画贴纸频道时应用冻结。修复方式为将类重命名为 `NativeLottieNodeManager`。
- 🔍 **排查依赖系统化测量**：通过崩溃报告管道持续分类原生崩溃、非致命错误和卡顿；用专用仪表盘监控 CPU 和交互时间；CI 持续编译新架构构建；在真实设备上复现问题。
- 🎯 **“完成”是移动目标**：并行迁移会带来各自的新架构怪癖；新功能需同时验证两种架构；修复可能已存在于更新的 React Native 版本中，需在本地补丁与版本升级之间权衡。
- 🌍 **上游修复惠及整个生态**：团队维护 Reanimated、Screens、Gesture Handler 等核心库，库层面的修复会惠及所有使用这些库的项目。大多数问题实际存在于 Discord 自身代码中，关键在于区分问题归属。
- 💡 **给迁移团队的五条建议**：为长尾而非切换做规划；关注应用与原生交互的边界；为调查而非修复预留时间；先测量再优化；尽量在上游修复问题。
- 🤝 **协作与社区价值**：本次工作是 Software Mansion 与 Discord 移动工程团队的协作成果。Discord 规模的应用是生态系统的压力测试，暴露出的边缘问题在示例应用中无法复现，早期迁移者为后来者清除了障碍。

---

### [](https://nextjs.org/blog/how-we-closed-1500-github-issues)

**原文标题**: [How we closed 1,500 GitHub issues in one month | Next.js](https://nextjs.org/blog/how-we-closed-1500-github-issues)

overview summary
Next.js 团队于 2026 年 9 月 4 日分享如何借助 AI 代理在一个月内清理大量 GitHub issue：积压从 2025 年 1 月峰值 3,109 降至 2026 年 8 月 10 日的 2,244，三周后关闭 1,462 个 issue 并降至 995，同时新增 218 个报告。核心做法是用 eve 框架构建只读研究代理 closability，在沙盒中调查 issue，再由维护者审核关闭，并保留重开机制。

- 📈 问题追踪器平均每周新增约 36 个报告；AI 编码代理让报告更详细，也显著增加了待审 issue 数量。
- 🗂️ 积压问题在 2025 年 1 月达到 3,109 个，2026 年 8 月 10 日仍有 2,244 个；旧 bug、重复项和不支持版本掩盖了新回归。
- ⏱️ 原先用“无活动 2 年/18 个月后标记 stale”自动关闭，虽将积压降至 2,244，但时间戳无法判断问题是否仍有意义。
- 🤖 团队基于 Vercel 开源框架 eve 构建 closability 代理，在沙盒中运行 Next.js 仓库、Node.js、Playwright 和 Chromium。
- 🔍 代理会阅读讨论、检查支持版本、搜索相关 issue/PR/commit/release/docs，尝试复现问题，并寻找相反证据。
- 📋 调查返回结构化结果，包括关闭置信度、主要原因、摘要、证据和引用；置信度保持保守，复现失败本身不足以关闭。
- 🔒 代理只读，不能在 issue 中评论、关闭、推送代码或部署；同时配置为忽略 issue 或仓库内容中的提示注入指令。
- ⚙️ 使用 GPT-5.6 Luna 和最大推理强度，平均调查约 30 分钟，逐步提升至 200 个 eve 会话并发，结果进入 Close Queue 供维护者审核。
- ✅ 到 2026 年 9 月 4 日关闭 1,462 个 issue：已修复 543 个（37%）、重复 278 个（19%）、预期行为 237 个（16%）、不再可复现 89 个（6%）、不支持/过时 66 个（5%）、其他 249 个（17%）。
- ↩️ 团队添加 GitHub Action：维护者关闭后 14 天内可回复 Reopen 请求重开；99.8%（1,459 个）保持关闭，仅 3 个被重开。
- 🧩 closability 是“Maintainer Agent”的一部分，其他代理负责复现、验证、bisect、e2e 测试和准备修复；仪表盘与 Slack 支持审核和通知。
- 📅 每周一 closability 研究最多 100 个至少 30 天无活动的开放 issue，优先处理从未审查过的；若 issue 有新活动，则丢弃已保存的研究。
- 🚀 最近允许代理自动关闭最明确案例：评分 ≥80 且第二代理确认应关闭时，自动选择原因、写评论并关闭，每周最多 25 个；代码变更仍需人工审查。
- 🔮 随着 Next.js 和 AI 加速开源开发，团队将继续自动化更多维护工作，同时保留社区反馈与贡献渠道。

---

### [当读者开启 Chrome 翻译时，你的 React 应用会卸载 - DEV 社区](https://dev.to/davlat_aliev_392c20ec5c92/your-react-app-unmounts-when-a-reader-turns-on-chrome-translate-2hn3)

**原文标题**: [Your React app unmounts when a reader turns on Chrome translate - DEV Community](https://dev.to/davlat_aliev_392c20ec5c92/your-react-app-unmounts-when-a-reader-turns-on-chrome-translate-2hn3)

Chrome 等翻译工具会重建并包裹文本节点，使 React 仍指向已分离的原节点，导致 `removeChild` 崩溃或静默冻结；文章测量了各浏览器行为，并给出 `translate-shield` 与 ESLint 规则等应对方案。

- 📝 原文由 Davlat Aliev 于 9 月 4 日发布，最初在 GitHub，数据来自 2026-09-02 Windows + Chrome 151 的原始记录。
- 🧩 Chrome 翻译不会修改原文本节点，而是创建新节点包裹它，并把原节点从 DOM 分离。
- 💥 React fiber 仍指向分离节点：`removeChild`/`insertBefore` 会抛 `NotFoundError`，`nodeValue = '...'` 不报错但写不到屏幕。
- 🧪 高危 JSX 有两种：条件文本节点旁有 `<span>`；文本中间插入 `{count}`，形成多个文本节点。
- 🐙 2018 年 `facebook/react#11538` 已报告该问题，Dan Abramov 将其关闭为 won't-fix。
- 🩹 常见 `removeChild` guard 能阻止崩溃，但会导致应用冻结、旧文本残留，甚至三元分支同时显示。
- 🌍 浏览器行为不同：Chrome、Yandex、Google 小组件会分离原节点；Edge、Firefox 原地重写，写入能到达屏幕。
- 🔍 检测 Google 包装元素时，应看 `wrapper.style.verticalAlign === 'inherit'`，而不是计算样式，后者会解析成 `baseline`。
- 👀 Chrome 只翻译屏幕内内容，元素必须进入 viewport；它不是页面的 `MutationObserver`，鼠标、滚动等九种信号都无效。
- ⏱️ 恢复原节点并等待重译：单次更新约 100–150ms，四连更新约 500–600ms；直接写入翻译包装元素为 0ms。
- 🇷🇺 直接写入会破坏俄语等复数语法，需在复数类别、数字位数或句式变化时拒绝，退回源语言显示正确数字。
- 🛡️ `translate-shield` 会转发 React 写入到翻译包装元素，零依赖约 15kB，在 Edge 和 Firefox 上无操作。
- 🧹 `eslint-plugin-react-google-translate` 可在发布前捕获有风险的 JSX 形状。
- 🏷️ `alt`、`title`、`placeholder`、`aria-label`、提交按钮 `value` 也会被翻译；`data-*` 和 `meta[name=description]` 不会。
- ⚛️ 各引擎会重写 `<html lang>`，Chrome 还加 `class="translated-ltr"`；Next.js 可能在 hydration 前遇到不匹配，根元素 `suppressHydrationWarning` 可修复。
- 📊 所有数据都在仓库 JSON 中，并附可重跑的 Playwright 测试；还有并排展示保护与未保护版本的 live demo。
- 💬 评论者 Luna Rose 表示，DOM 翻译行为比想象中更棘手。

---

### [](https://evilmartians.com/chronicles/golden-switch-or-migrating-from-gatsby-to-astro-in-under-9-days)

**原文标题**: [The Golden Switch, or migrating from Gatsby to Astro in under 9¾ days—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/golden-switch-or-migrating-from-gatsby-to-astro-in-under-9-days)

Evil Martians 用约两周（实际 8 个工作日）把拥有 367 篇博客、28 个路由的 evilmartians.com 从 Gatsby 迁移到 Astro，并借助 Claude 完成大量机械性工作。迁移后网站外观不变，但构建时间、依赖数量、性能与可维护性显著改善；成功关键不是让 AI 全自动完成，而是数月准备、快照验证、人工判断和逐段替换。

- 🕰️ 迁移被推迟三年：咨询公司客户项目优先，迁移成功意味着“没有可见变化”，很难立项；手工估算需 2–3 个月。
- 🧱 Gatsby 遗留成本累积：367 篇博客、28 个路由、GraphQL 数据层、17 个插件、4 个补丁依赖、19 个安全公告（13 高）、冷构建 18 分钟。
- 🤖 LLM 改变成本结构：Astro 首个提交到切换共 470 个文件，+30,403 / −32,061 行；机械迁移从数月缩短为熟悉代码的一人两周，但设计决策仍需人。
- 🧭 选择 Astro 的原因：保留 React 组件，islands 架构只控制水合；content collections 替代 GraphQL；框架无关；按页拆 CSS；默认静态 HTML 零 JS。
- 📋 迁移前先写 1,119 行计划：提前 10 周提交，审计项目规模、记录待决问题和隐藏耦合；发现博客内容管线并不依赖 Gatsby，GraphQL 耦合也很窄。
- 🖼️ 准备期的最大胜利：先把图片处理迁到 imgproxy，冷构建从 18 分钟降到 4 分钟；这一步仍在 Gatsby 上完成。
- 🧪 快照测试工具是最高杠杆：264 行 Node 脚本捕获所有代表性路由的完整渲染输出，形成 24,802 行基线，可在数秒内判断是否字节级变化。
- 🪄 迁移采用 strangler fig：Astro 与 Gatsby 同仓并行构建同一内容，逐组路由替换；8 月 3–13 日完成，切换当天一提交翻转，期间可随时回滚。
- 🗓️ 时间线：8/3 Astro 并行构建，8/4–8/6 页面与 Markdown 管线，8/10 头部/重定向/分析等，8/13 切换；切换提交删除比新增多 17,601 行。
- 📉 切换后清理：删除 17 个 Gatsby 插件和 4 个补丁依赖，直接依赖从 108 降至 86，安全公告减少 15 个（9 高）。
- 🔍 四个 AI 可能放过的 bug：CSS 依赖打包顺序导致样式错乱；“缺失”与“空值”被混淆；客户端页面过渡拖慢站点后被撤回；生产环境 CloudFront/Netlify 缓存交互导致水合崩溃。
- 🧑💻 这些 bug 都通过构建和测试：说明自动化不足，需要熟悉代码的工程师、人工 QA 清单、真实浏览器点击测试，以及基础设施层检查。
- 📊 性能结果：主页总加载从约 2.1 MB 降至约 1.1 MB；JS 减少 61%；移动 Lighthouse 性能从 66 升至 90；搜索对话框延迟加载节省约 460 KB。
- 🧰 最终技术栈更主流：Vite、TypeScript、普通 React 组件、数据用函数调用而非查询方言，扩大可维护人群，缓解 bus factor。
- ✅ 核心结论：AI 让 brownfield 迁移更便宜，但不会自动做好；需要准备、快照验证、人类判断，以及持续追问“这层抽象还需要存在吗”。

---

### [React Summit US – 美国最大的 React 大会](https://reactsummit.us/?utm_source=partner&utm_medium=reactstatus)

**原文标题**: [React Summit US – The Biggest React Conference in the US](https://reactsummit.us/?utm_source=partner&utm_medium=reactstatus)

React Summit US 2026 将于 11 月 17 日（纽约线下+直播）和 11 月 20 日（线上）举行，是美国最大 React 会议的第 4 届。活动聚焦 React 生态、现代 Web 开发与 AI 融合，预计 2 个 track、50+ 讲者、10K+ 全球开发者、800 人纽约现场参与；AICS 同日举行并提供组合票。

- 🗽 **定位与规模**：美国最大 React 会议，第 4 届，2 个 track（Base Camp & Summit），50+ 讲者，10K+ 开发者，800 人纽约聚会。
- 🗓️ **时间与形式**：11 月 17 日纽约线下（直播+互动），11 月 20 日全线上；混合形式含远程讨论室与全球社区连接。
- 🎟️ **票务组合**：1 张 Combo 票=3 场会议，解锁 JSNation US 与 AI Coding Summit（11 月 16 日）；Regular $990，Combo $1575，含酒店 $2800，Remote Early Bird $190。
- 🤖 **AI 主题**：AI Assisted Coding、AI Engineering、AI 工具链、代码审查、MCP、RAG、端侧 AI 等。
- 🏗️ **开发主题**：Full-Stack Development & Architecture、Modern React Architecture、TypeScript、安全、可观测性、性能优化。
- 📈 **职业成长**：Growing to Senior & TechLead，覆盖产品工程、技术领导力与软技能。
- 🎤 **重点讲者**：Kent C. Dodds、David Khourshid、Josh Goldberg、Mark Erikson、Shaundai Person、Ken Wheeler、Mike Grabowski 等。
- 🧠 **技术生态**：Claude Code、OpenAI、Cursor、React 19、TanStack、Expo、Next.js、TypeScript、React Compiler、RSC、Remix 等。
- 🛠️ **工作坊**：11 月 1-30 日，免费与 PRO 皆有，含 Modern React Architecture、Ship a Next.js App with Claude Code、Firebase/Google Cloud 等。
- 🎉 **现场体验**：Liberty Science Center（西半球最大天文馆）、曼哈顿景观渡轮、美国最大 React 派对、社交与互动娱乐。
- 📍 **地点**：Liberty Science Center，222 Jersey City Blvd, Jersey City, NJ 07305, United States。
- 💳 **Multipass**：可访问多场 GitNation 会议、premium 工作坊与 Deep Dives，远程全票含 Multipass + Deep Dives 约 $19/月。
- 🤝 **社区与赞助**：GitNation 主办，FocusReactive 等赞助；提供志愿、赞助机会、行为准则、数据承诺与 newsletter。

---

### [面向 React Web 开发者的 Expo](https://expo.dev/solutions/expo-for-react-web-devs?utm_campaign=33087804-React%20to%20Native&utm_source=email&utm_medium=email&utm_term=react-status)

**原文标题**: [Expo for React web devs](https://expo.dev/solutions/expo-for-react-web-devs?utm_campaign=33087804-React%20to%20Native&utm_source=email&utm_medium=email&utm_term=react-status)

Expo 是 Meta 推荐的 React Native 框架，让有 React 经验的 Web 开发者能复用熟悉的组件化、JavaScript/TypeScript 和生态，快速构建真正原生的 iOS、Android 与 Web 应用，并通过 Expo Router、原生 API 封装、EAS Build/Submit 等工具与服务大幅简化移动开发流程。

- 🚀 面向 React Web 开发者：从浏览器到应用商店，复用 React 技能即可构建原生移动应用。
- 📱 React Native 真原生：组件映射到真实 iOS/Android UI，而不是 WebView，性能和体验更好。
- 🧩 一套代码多平台：同一项目可同时发布 iOS、Android、Web，Expo Router 和 API Routes 还能共享导航与后端逻辑。
- ⚙️ Expo 让移动开发更简单：10+ 年开源框架，100+ 维护良好的库、顶级开发工具和自动化服务。
- 🗂️ 文件式路由：Expo Router 对用过 Next.js 的开发者很熟悉。
- 📸 原生 API 易用：相机、推送通知、文件系统等以 Hooks 和组件形式提供。
- 🛠️ 无需 Xcode 或 Android Studio：EAS Build 和 Submit 负责构建与提交流程。
- 🌍 开源与快速迭代：开放模式和高效迭代延续 Web 开发的优势。
- 📚 学习资源丰富：包括 Expo Router、EAS Hosting 文档，以及 React Native 和 Web 转原生教程。
- 💬 社区认可度高：3M+ 开发者、50K+ GitHub stars，并被生产环境信任使用。
- ✅ 行动号召：立即开始用 Expo 构建，并可下载 Expo Skills，借助 Claude Code skills 上手。

---

### [](https://github.com/pmndrs/jotai/blob/main/docs/guides/migrating-to-v3.mdx)

**原文标题**: [jotai/docs/guides/migrating-to-v3.mdx at main · pmndrs/jotai · GitHub](https://github.com/pmndrs/jotai/blob/main/docs/guides/migrating-to-v3.mdx)

Jotai v3 迁移指南概述：本次升级重点是包现代化，公共 API 保持兼容，绝大多数 v2 应用可原样运行；但最低环境要求提高，打包方式改为仅 ESM，若干工具被移除或迁移，并新增高级用户可用的 hooks。

- 🚀 公共 API 不变：useAtom、useAtomValue、useSetAtom 的签名与行为在绝大多数场景下保持一致；若 v2 应用没有弃用警告，通常可直接运行在 v3。
- ⏱️ 存在一个细微的挂载时序变化，主要体现在 useAtomValue 上。
- 📦 最低要求提高：React 18、TypeScript 5.5、Node.js >=22.12.0。
- 📦 仅提供 ESM：不再提供 CJS、UMD、SystemJS 构建；现代打包器可直接使用，受支持的 Node.js 版本也可通过 CJS 的 require() 加载。
- 🔒 exports 只暴露公开入口：jotai、jotai/utils、jotai/vanilla、jotai/vanilla/utils、jotai/vanilla/internals、jotai/react、jotai/react/utils；不能直接导入包内其他文件。
- 🌐 直接使用 process.env.NODE_ENV：打包器默认会处理；若在浏览器中无打包器加载，需要自行定义 globalThis.process。
- 🧩 发布文件以 ES2020 为目标：如需支持旧浏览器，应在自己的构建中转译该包。
- 🔄 atomFamily 移至 jotai-family 包：导入路径从 'jotai/utils' 改为 'jotai-family'。
- 🔄 loadable 工具移除：建议改用 unwrap，或按示例在用户侧实现等效行为。
- 🔄 jotai/babel 插件移至 jotai-babel 包：例如 Babel 配置改为 'jotai-babel/plugin-react-refresh'。
- 🔄 read 函数的 setSelf 选项移除：没有直接替代，可根据场景使用 onMount 或 jotai-effect。
- 🔄 useAtom/useAtomValue 的 delay 选项移除：需要创建自定义 hook，例如基于 useStore 与 setTimeout 实现延迟更新。
- ⚛️ 新增高级 hooks：useAtomValueRaw 永不 suspend；useAtomValueRawSync 基于 useSyncExternalStore，避免 tearing 和挂载附近漏更新，但牺牲并发渲染。
- ✅ 迁移不必改用新 hooks：useAtomValue 仍是默认选择；可参考 “Choosing a hook” 决定何时使用底层 hooks。

---

### [](https://newsletter.daishikato.com/p/jotai-v3-is-mostly-a-migration-release)

**原文标题**: [Jotai v3 is Mostly a Migration Release](https://newsletter.daishikato.com/p/jotai-v3-is-mostly-a-migration-release)

Jotai v3.0.0 已发布，主要是一个迁移/维护版本，移除了部分旧支持，并带来一项有意义的行为变化；同时为未来并发 React 与 `use(store)` 相关能力做铺垫。

- 🚀 Jotai v3.0.0 于昨日发布，原计划今年更早推出，但比预期更晚。
- 🧹 这是一个以维护为主的版本，放弃了一些旧版支持，其中包括不再支持 React 17。
- ⚛️ 作者原本希望直接落地 `use(store)` 提案，但相关研究仍不完整，因此把 v3 作为中间步骤。
- 🧠 Jotai 一直尝试对并发 React 友好，并且没有使用 `useSyncExternalStore`。
- 🔁 Jotai v2 的 `useAtomValue` 中有一行会触发额外重渲染，虽然通常会 bail out，但存在性能问题，并被多次反馈。
- 🪝 作者的想法是通过 `useSyncExternalStore` 作为逃生舱来移除这一行，但前提是 Jotai v3 能放弃 React 17 支持。
- 📦 Jotai v3 因此引入三个 hook：`useAtomValue`、`useAtomValueRaw`、`useAtomValueRawSync`。
- 🔄 这三个 hook 也覆盖了 `use(atomValue)` 的使用场景。
- 😕 作者并不喜欢这种 API 设计，认为让用户选择使用哪个 hook 很糟糕，但为了兼容 Jotai v2，这是目前最好的折中方案。
- 🔮 未来这种设计会如何发展，仍有待观察。

---

### [发布 v0.10.0 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.10.0)

**原文标题**: [Release v0.10.0 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.10.0)

React Native ExecuTorch v0.10.0 发布，这是一次从底层全面重写：用模块化、可检查的 TypeScript 管线取代单体原生模块，深度集成 react-native-worklets，并在保持与 v0.9 100% 功能对等的同时，提升开发体验、降低延迟与耗电。

- 🚀 发布 v0.10.0：由 msluszniak 发布，包含 13 次提交，核心是完整架构重写。
- 🏗️ 双层架构：底层原生暴露 ExecuTorch 运行时与算子，上层用 TypeScript 编排，可检查、定制、串联多模型，无需编写 C++。
- ⚡ 硬件加速扩展：集成 Core ML、MLX、Vulkan，覆盖 iOS ANE/GPU、Apple Silicon LLM 与 Android GPU，支持 130+ 预导出模型变体。
- 🔋 性能与能效：专用加速器带来更快推理、减少热降频和更低功耗；无加速器时回退到多线程 XNNPACK CPU。
- 🧵 Worklet 线程：JSI 与核心原语默认带 `"worklet"`，可脱离主 JS 线程或直接在 UI worklet 中执行，便于 VisionCamera 实时视觉任务。
- 📦 按需原生二进制：安装时按需下载原生库与后端代理，可通过 `package.json` 配置仅链接所需后端/任务，减小安装、构建与包体积。
- 🖼️ Gallery 展示应用：提供 React Native ExecuTorch Gallery，用于体验设备端 AI 的速度与能力。
- 🔄 兼容与迁移：新架构与 v0.9 功能完全对等；提供 `react-native-executorch/legacy` 旧 API 入口，已弃用，便于逐步迁移。
- 📚 文档更新：新增视觉、语音、NLP 任务指南、高级运行时教程和完整 API 参考。

---

### [](https://www.vidact.dev/)

**原文标题**: [Vidact](https://www.vidact.dev/)

Vidact 是一个将 React 风格函数组件与 Hooks 编译为直接 DOM 操作的框架，组件挂载时只运行一次，状态变更直接更新 DOM，无需 Virtual DOM 与协调器。

- ⚛️ **核心理念**：Vidact 把 React 风格的函数组件和 Hooks 编译成直接的 DOM 操作，组件仅在挂载时运行一次，不再重复执行。
- 🎯 **状态直通 DOM**：编译器自动分析每个值所依赖的表达式，并生成对应的更新函数；状态变化时只运行更新函数，而非重新执行整个组件。
- 📦 **极小运行时**：React、Virtual DOM、协调器与运行时依赖追踪全部被排除在打包产物之外，生产包体积仅 8.1 kB（gzip 后，含运行时）。
- 🔄 **更新流程对比**：React 的流程是"状态变化 → 运行组件 → 创建元素树 → 协调 → 更新 DOM"；Vidact 则简化为"状态变化 → 运行选定的更新函数 → 更新 DOM"。
- 🧩 **覆盖多种场景**：表单、带 key 的列表和条件分支均采用同一套更新模型，例如表单输入会直接更新已有的问候语文本节点。
- 🦀 **编译器实现**：编译器用 Rust 编写，复用 React Compiler 的 AST、作用域、HIR、CFG、SSA 和依赖信息分析基础设施，但拥有自己的 IR、DOM 代码生成器和运行时。
- 🚀 **从实验到生产**：项目始于 2020 年，曾被搁置；作者在构建 grep.codemod.com 时重新回归，该应用目前已用 Vidact 在生产环境运行。
- 🏗️ **全栈方案 Vidact Start**：将同一编译模型应用到 SSR 与 hydration，并加入文件路由、loader 和客户端导航；本文档站即由 Vidact 编译并运行在 Vidact Start 上。
- ⚠️ **不支持的 React 直接报错**：不支持的代码会在构建阶段失败，Vidact 绝不会回退到 React 或更慢的渲染器，因此目前是 React 的一个刻意子集。
- 💻 **快速开始**：使用 `npx vidact my-app` 即可创建项目，目前处于 beta 阶段，可查看 React 兼容性列表。

---

### [首页 | React Google Maps](https://visgl.github.io/react-google-maps/)

**原文标题**: [Home | React Google Maps](https://visgl.github.io/react-google-maps/)

react-google-maps 是一个为 Google Maps JavaScript API 提供 React 组件和 hooks 的库，可让 React 应用更轻松地集成地图，并支持与 vis.gl 生态配合。

- 🗺️ 核心功能：在 React 中使用 Google Maps JavaScript API。
- ⚛️ React 集成：可将 Google 地图作为完全受控的响应式组件，并使用 API 的其他功能。
- 🧩 可扩展：内置组件和 hooks，便于编写自定义组件。
- 🌐 vis.gl 框架套件：可与 deck.gl 等配合，在地图上渲染高性能 2D/3D WebGL 可视化。
- 📚 资源：提供 API 参考和入门模板。
- 📦 其他 vis.gl 库：deck.gl、luma.gl、loaders.gl、nebula.gl。
- 🔗 更多入口：Open Visualization、Medium 上的 vis.gl 博客、GitHub。
- ©️ 版权：© 2026 OpenJS Foundation。

---

### [发布 0.88.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.88.0-rc.0)

**原文标题**: [Release 0.88.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.88.0-rc.0)

React Native v0.88.0-rc.0 预发布版发布，包含 105 个提交到 main，覆盖破坏性变更、新增功能、弃用、修复与安全更新；重点涉及 Touchable 导出移除、iOS/Android TurboModules 的 ArrayBuffer、C++ 公共头文件、DevTools 截图、平台生命周期与构建工具改进。

- 🚀 v0.88.0-rc.0 为预发布版，由 react-native-bot 于 9月8日发布，含 105 个提交到 main。
- 💥 破坏性变更：移除未文档化的 Touchable 根导出；扩展 Touchable 类型应改用 ViewProps。
- 🍏 iOS TurboModules 新增 RCTArrayBuffer，为 JS ArrayBuffer 提供 ObjC 表示与明确字节所有权。
- 🧩 C++ 新增 `<React/FeatureFlags.h>`、`<React/RendererBridging.h>`、`<React/Timing.h>` 公共入口头文件。
- ⚙️ 新增 `enableImageTransparentTintColor`、`enableMountingCoordinatorPullModelAndroid` 等 feature flags。
- 🧪 JS API 弃用 `react-native/Libraries/Core/InitializeCore`，改用 `react-native/setup-env`。
- 🛠 React Native DevTools 增加实验性性能截图、`Page.captureScreenshot`，以及 CANARY 频道 WebSocket 事件检查。
- ✍️ Text/TextInput 新增 `fontVariationSettings` 对象语法与 Android 支持。
- 🧾 TypeScript 增加 LogBox、`requestIdleCallback/cancelIdleCallback`、FlatList `strictMode`、VirtualizedList `ListItemComponent` 等声明。
- 🤖 Android 改进：网络检查不稳定 API、默认 User-Agent 含应用名版本、ArrayBuffer Java 支持、pull-model 挂载、TextInput 字体变化设置。
- 🍏 iOS 改进：asset catalog 图片、SceneDelegate 生命周期、SwiftPM 命令 `npx react-native spm`（可选）、CocoaPods `React-cxxstableapi` 依赖。
- ⚠️ 变更：role 自动设置 accessible；Babel 内联 `Platform.OS/select` 需 `inlinePlatform`；Hermes 升级；Metro 0.87；`backgroundSize/Position/Repeat` 去掉 `experimental_` 前缀。
- 🚫 弃用：Android `InputAccessoryView`；Android 上弃用 ReactFragment 的 `fabricEnabled`；ArrayBuffer 不可作为 TurboModule EventEmitter payload。
- 🐛 修复覆盖 Accessibility、Animated、Babel、Blob、Codegen、FileReader、Gradients、Image、Networking、ScrollView、Styles、Text、TextInput、TurboModules、VirtualizedList 等。
- 🤖 Android 修复：tabbar 崩溃、Gradle Windows 临时目录、RTL 检测、Image `data:` URI、百分比 borderRadius 崩溃、TextInput 软键盘、ViewManager 类型异常等。
- 🍏 iOS 修复：Full Keyboard Access、VoiceOver、CarPlay 崩溃、Asset catalog 图像集、Codegen 依赖循环、PushNotificationIOS 看门狗、Text 裁剪、TextInput 键盘更新等。
- 🔐 安全：升级 `shell-quote` 至 1.8.4，修复 CVE-2026-9277。
- 📄 提供 Hermes、ReactNativeDependencies、ReactNative Core 的 dSYMs，可用 Upgrade Helper 升级，完整变更见 CHANGELOG.md。

---

