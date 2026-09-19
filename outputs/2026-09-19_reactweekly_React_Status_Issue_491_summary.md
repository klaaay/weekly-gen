### [框架还重要吗？](https://brookslybrand.com/posts/do-frameworks-matter-anymore/)

**原文标题**: [Do Frameworks Matter Anymore?](https://brookslybrand.com/posts/do-frameworks-matter-anymore/)

overview summary
作者在2026年“代理编程/氛围编程”背景下重新审视框架价值：他认为框架依然重要，因为其提供抽象、结构、约束、安全与文档；即便不用显式框架，AI 也会生成隐式框架。旧框架战争虽已结束，但新框架仍有必要，值得继续构建。

- 🧭 文章追问：在 AI 代理编程时代，Web 框架还重要吗？我们还应创造新框架吗？
- 🤖 流行观点认为模型已擅长前端，React 因训练数据多而占优，因此无需再尝试其他框架。
- ❓ 作者反驳：若框架不重要，为何还用 React？不如让 LLM 直接使用 Web 标准、HTML、CSS 和 JavaScript。
- 🧩 框架的核心价值被定义为：为建站提供抽象、结构与约束，帮助塑造代码和代理行为。
- ⚛️ React 胜出主要靠组合性、组件封装、生态与 SSR，而非某个组件库；shadcn/ui 是生态繁荣的结果。
- 🏗️ 不使用框架时，代理会自动生成自己的隐式框架，所以“用不用框架”并非真正选择。
- 🛡️ 好的开源框架能给代理护栏、测试、类型、文档和安全保障，优于代理自造的临时抽象。
- 🔁 HMR 对复杂交互仍有帮助；TypeScript 的类型约束也能提升 LLM 迭代代码的稳定性。
- ⚠️ useEffect 等抽象对代理风险较高，部分项目直接禁用；作者希望框架让正确做法显而易见。
- 🧭 作者想要的新框架：全栈、基于 Web 标准、AI 友好、代码可推理，并内置测试、工具与文档。
- 📉 框架战争已结束，人们不再热衷框架，但重要事物不必处于 hype 中心。
- 🧪 AI 正重塑软件开发，LLM 是工具；长期影响未知，质量仍取决于使用方法。
- ✅ 结论：框架仍重要，新框架也重要；现有问题未全部解决，应继续构建新框架。

---

### [](https://ondrejvelisek.github.io/the-cost-of-abstraction-for-humans-and-ai-agents/)

**原文标题**: [The Cost of Abstraction for Humans and AI Agents | Ondrej Velisek](https://ondrejvelisek.github.io/the-cost-of-abstraction-for-humans-and-ai-agents/)

overview summary
- 🧩 文章核心：抽象对可维护性和大型系统很关键，但过度抽象会同时增加人类理解成本和 AI 代理费用。
- 🧱 抽象是代码两部分之间的边界：一端隐藏实现，另一端通过有名称、可复用的接口使用它。
- ✅ 抽象的目的：隐藏复杂度、命名代码、复用代码；若这些收益不明显，就不该抽象。
- ⚠️ 过度抽象的四个原因：成本缓慢累积、开发者害怕修改旧抽象层、教育文化推崇 DRY/SOLID 等原则、团队中难以公开质疑抽象。
- 🤖 AI 从人类代码中学习，因此也继承了过度抽象倾向，并进一步放大成本。
- 💸 每个抽象都有成本：增加间接性、代码跳转、记忆负担、导航难度和新人上手成本。
- 🧾 例子里，只想查删除按钮颜色，却要跨越 6 个文件；AI 也必须把这些文件拉入上下文，消耗更多 token。
- 🧪 作者做了实验：两个功能相同的计算器应用，一个代码集中，一个额外增加 12 层抽象，用 Sonnet 5 改“=”按钮颜色。
- 📊 初步结果：过度抽象应用在金钱和时间上都贵约 5 倍；重复 10 次后结果仍一致。
- 📏 代码体积不是主因：控制到相同规模后，过度抽象仍贵约 3 倍。
- 🔁 AI 模型往返次数也增加约 2.2 倍，说明跨层查找和读取文件是主要成本来源。
- 📋 成本取决于任务：变化从 0.8 倍到 5 倍；改叶子值最贵，重样式多个按键时抽象反而可能更便宜。
- 🧭 钱主要花在读取文件和往返轮次上；同一文件内的抽象几乎免费，跨文件边界的抽象才昂贵。
- 🗂️ 命名良好的抽象有时像索引，能帮助 AI 搜索定位；在“查找并修复缺陷”任务中成本约降低 10%。
- 📈 基于 394 次代理运行，作者保守估计：真实中大型代码库中，过度抽象会让 AI 代理成本和时间增加约 30%。
- 🚫 不该抽象的例子包括：无意义常量、静态 JSX 列表映射、简单工厂函数、多余 CSS 类、错误放置的 Context、无逻辑翻译层。
- 🧠 结论：抽象仍不可或缺，但要“先思考再抽象”；在代码评审中识别过度使用，并明确告诉团队和 AI 代理。

---

### [](https://master.dev/sale/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=buildersale)

**原文标题**: [Build Better With AI Sale | Master.dev](https://master.dev/sale/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=buildersale)

秋季促销：立减 100 美元，主打掌握基础知识并用 AI 更好地构建，活动仅剩数天，可立即领取优惠。
- 💸 秋季促销立减 100 美元
- 🎯 核心主题：掌握基础知识
- 🤖 行动方向：借助 AI 更好地构建
- ⏳ 限时提醒：促销仅剩数天
- 🔗 立即行动：现在获取折扣 →

---

### [](https://lovable.dev/blog/faster-previews-oj)

**原文标题**: [Faster previews, soon powered by OJ | Lovable](https://lovable.dev/blog/faster-previews-oj)

Lovable 正在将预览引擎从 Vite 迁移到自研的 OJ（Orange Juice）：一个端到端用 Rust 编写、兼容现有 Vite 配置与插件的单一二进制。它针对每天约百万级沙箱规模优化，目标是更快冷启动、更低内存占用，并已在生产和开源中推进。

- ⚡ Lovable 预览是运行真实应用、支持热重载的开发服务器；Vite 虽为行业标准，但面向单开发者单机场景，难以支撑大规模沙箱。
- 🦀 OJ 是单个 Rust 二进制，可读取现有 `vite.config.ts` 或 `oj.config.ts`，通过兼容桥运行真实 Vite 插件，并原生重实现 React Fast Refresh、TanStack Start 等能力。
- 🧩 OJ 基于 Rolldown 与 Oxc，从文件监听、WebSocket 到编译管线端到端用 Rust，只在插件或服务端代码需要时启动小型 Node sidecar。
- 🎯 设计原则是兼容优先、不向项目安装工具链、面向 agent 批量编辑；突发编辑会被合并为一次完整更新，避免预览呈现半成品状态。
- 📊 基准测试：10,000 组件冷启动 1.2s 对比 Vite 4.9s，内存约 115MB 对比 >1.5GB；Excalidraw 为 0.8s/288MB 对比 2.3s/2.4GB；Twenty 为 10.2s/1.5GB 对比 11.3s/4.9GB。
- 🏭 生产数据：预览加载中位数从 17.4s 降至 8.0s，沙箱获取从 14.5s 降至 3.0s，P90 开发服务器从 15.8s 降至 9.6s，开发服务器内存约少 6.5 倍。
- 🧑‍💻 对构建者而言无需改动：现有插件和配置继续工作；OJ 会逐步扩大覆盖，若出现行为差异可反馈 bug，兼容性是核心承诺。
- 🌐 OJ 已从个人仓库迁至 Lovable GitHub 组织 `github.com/lovablelabs/oj`，保持 Vite 兼容、公开可读、可运行、可贡献。
- ✍️ 作者 Raphael Amorim 是 Lovable 工程师、OJ 创造者，专注 Rust 开发者工具；更多提速实验功能即将公布。

---

### [](https://reactrouter.com/changelog#v840)

**原文标题**: [CHANGELOG.md  | React Router](https://reactrouter.com/changelog#v840)

该文档是 React Router 官方更新日志，集中记录从 v7.0.0 到最新 v8.4.0（main 未发布）的版本说明，并提示 v6 及更早版本需查看旧分支或 GitHub Releases；集中维护是为了避免 GitHub 分页导致搜索困难与长说明被截断。整体重点包括 v8 的性能优化、Future Flags 默认化、破坏性变更、RSC/中间件/预渲染演进，以及 v7 各版本的安全修复、API 稳定化和迁移指引。

- 📌 版本入口：当前最新为 8.4.0，main 未发布；版本列表含 7.18.4、6.30.6、v4/5.x、v3.x；v7.0.0 起的发布说明在本页维护。
- 🚀 v8.4.0 性能：内部路由上下文更细粒度，减少无关路由组件重渲染；新增 `unstable_routePatternMatching`，路由匹配基准提升约 19–38%（100 条路由）和 71–88%（1000 条路由）。
- 🧪 v8.4.0 不稳定项：新增 `unstable_validateParams` 参数校验；弃用 `createStaticRouter({ branches })`；修复 stale route discovery、SPA 懒加载导入错误、RSC 重定向转义、视图过渡、内存泄漏等。
- 🩹 v8.3.1 修复：fetcher 中止、懒路由缓存、长路径匹配、action origin 校验、`ScrollRestoration` bfcache、相对 action 路径、URL 校验等；支持 `/.well-known/*` 静态文件。
- 🧩 v8.3.0 RSC：更新自定义 RSC 入口的 client version、SRI、CSP nonce；路径参数按 RFC 3986 编码；session ID 用 `crypto.randomUUID()`；支持 TypeScript 7；加固 RSC CSRF 与陈旧客户端检测。
- 🌊 v8.2.0 服务端渲染：非 Node 运行时默认 Web Streams `entry.server`；Node 应用可通过 `future.unstable_enableNodeReadableStream` 选用 `renderToReadableStream`；修复 `href`、可选静态段、路由排序等。
- 🤖 v8.1.0 工具与可观测性：`create-react-router` 可安装官方 Agent Skill；Instrumentation 结果增加 `result.meta`（URL、route pattern、params）与服务端 `statusCode`。
- 🎉 v8.0.0 大版本：最低 Node 22.22.0、React 19.2.7、Vite 7；ESM-only/ES2022；v8 Future Flags 全部转正；移除 `react-router-dom`、`meta` 的 `data`、Cloudflare dev proxy、architect `useRequestContextDomainName`；预渲染改用 Vite preview 流程。
- 🛡️ v7.18.0 安全/兼容：修复反向代理下 CSRF 检查逻辑；architect 新增 `useRequestContextDomainName`；建议测试 mutation 请求并配置 `allowedActionOrigins`。
- 📚 v7.17.0 文档：在 `react-router` 包内提供部分官方 Markdown 文档，便于 AI 编码代理/Agent Skill 本地读取；修复 future flag 警告。
- 🧭 v7.15.x 导航状态：v7.15.1 新增 `unstable_useRouterState()` 汇总 active/pending 路由状态；v7.15.0 稳定 `passThroughRequests`、`subResourceIntegrity`、`url`、`instrumentations`、`pattern`、`defaultShouldRevalidate`、`useTransitions`、`mask` 等并优化路由匹配。
- 🧪 v7.16–v7.14：v7.16 稳定 `future.unstable_trailingSlashAwareDataRequests`；v7.14 支持 Vite 8，并为 RSC Framework Mode 增加预渲染/SPA 支持。
- 🧱 v7.13–v7.12 能力与安全：v7.13 引入 URL masking（unstable）与 pass-through requests（unstable）；v7.12 修复 CSRF、开放重定向 XSS、`ScrollRestoration` XSS，并新增 `allowedActionOrigins`。
- ⚙️ v7.11–v7.10 稳定化：v7.11 支持 `vite preview`、稳定客户端 `onError`、试验 call-site revalidation opt-out；v7.10 稳定 `splitRouteModules`、`viteEnvironmentApi`、`fetcher.reset()`、`DataStrategyMatch.shouldCallHandler()`。
- 🧬 v7.9–v7.7 RSC/中间件：v7.9 稳定 Middleware 与 Context API，推出 RSC Framework Mode（unstable）、`useRoute()`、instrumentation；v7.8 统一 `loaderData` 命名并改进 middleware；v7.7 推出 Data Mode RSC unstable API。
- 🧰 v7.6–v7.2 开发体验：v7.6 新增 `routeDiscovery` 配置和 Future Flags 自动类型；v7.5 引入 `route.lazy` 对象 API；v7.3 引入客户端 context 与 middleware（unstable）；v7.2 提供类型安全 `href`、SPA fallback 预渲染、root loader、`splitRouteModules` 与 Vite Environment API（unstable）。
- 💥 v7.0.0 基础迁移：包结构合并为 `react-router`，移除 `json`/`defer` 等 API，最低 Node 20/React 18，采用 Vite 编译器，`routes.ts` 路由配置、路由模块类型生成、`prerender` SSG 等成为核心变化。

---

### [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3#view-transition)

**原文标题**: [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3#view-transition)

React 19.3 已在 npm 发布，将 View Transitions 和 Fragment Refs 从实验 API 转为稳定版，并新增 browser()、Trusted Types 支持、Server Components 直接渲染 Context 等能力，同时包含多项改进与错误修复。

- 🎉 React 19.3 正式发布，View Transitions 与 Fragment Refs 现已稳定可用。
- 🎬 `<ViewTransition>` 基于浏览器 View Transition API，可在元素进入、退出、更新、共享时触发动画，且仅由 Transition 更新驱动。
- 🎞️ `addTransitionType` 可为同一状态更新添加原因类型，从而为前进/后退等不同场景指定不同动画。
- ⏳ View Transitions 可与 Suspense 集成，动画化 fallback 到最终内容，也可让图片、字体加载触发 Suspense；但应避免缓存内容反复动画。
- 🧩 Fragment Refs 允许将 ref 传给 `<Fragment>` 并获得 `FragmentInstance`，无需修改子组件或额外 DOM 包装即可管理事件、焦点、观察器与测量。
- 🌐 React DOM 新增 `browser()`，通过 `use(browser())` 让组件在服务端触发 Suspense、在客户端正常渲染，适合时区、localStorage 等仅浏览器可用逻辑。
- 🔒 支持浏览器 Trusted Types API，React 不再强制把值转为字符串，使 TrustedHTML 等类型可在 CSP 下正常使用。
- 🧠 Server Components 现在可直接导入并渲染来自 `'use client'` 模块的 `<Context>`，无需额外 Provider 包装组件。
- ⚙️ 其他改进包括：独立渲染 Transitions、Strict Mode 水合时双调用 Effects、新增 `onFullscreenChange`/`onFullscreenError`、`maskType`、`fetchPriority`、`onReset` 等。
- 🐞 修复多项问题，如 `useDeferredValue` 卡住、Suspense 上下文传播、`useSyncExternalStore`、`useEffectEvent`、Fast Refresh、ViewTransition 崩溃与 hydration 不匹配等。

---

### [](https://expo.dev/changelog/sdk-58-beta)

**原文标题**: [Expo SDK 58 Beta is now available — Expo changelog](https://expo.dev/changelog/sdk-58-beta)

Expo SDK 58 Beta 已发布，测试期约三到四周；该版本面向 iOS 27，包含 React Native 0.88 RC，正式版将在 React Native 0.88 稳定后不久推出。开发者应借此验证兼容性、发现回归并反馈问题，Expo 会在 beta 期间持续发布修复与改进。

- 🚀 SDK 58 Beta 今日开始，持续约 3–4 周；正式发布将在 React Native 0.88 稳定版发布后不久。
- 📱 适配 iOS 27：使用 UIKit scene-based 生命周期，应用自动支持可调整大小；自定义 AppDelegate 需参考迁移指南。
- ⚛️ 包含 React Native 0.88 RC，并带上 0.87 的变更；稳定版发布后会切换并更新完整发布说明。
- 🧪 Expo Go for SDK 58 今日仅通过 Expo CLI 支持 Android 设备/模拟器与 iOS 模拟器，通过 eas go 支持 iOS 真机；商店版会在稳定版后更新。
- 🗓️ Expo 在 Discord 举办 office hours，邀请开发者协助测试。
- 🛠️ 支持 Xcode 27 的 EAS Build 镜像与 SDK 58 工具链即将推出；目前 latest 镜像仍使用 Xcode 26.6。
- 🖥️ Xcode 27 以 Device Hub 替代 Simulator.app；Expo CLI 已支持，并推出 expo-device-hub 浏览器本地设备面板。
- 🍎 expo-app-intents 以 alpha 形式暴露 Apple App Intents，支持 Siri、Shortcuts、Spotlight 与 Apple Intelligence。
- 🧭 Expo UI：新增 iOS 导航组件、SwiftUI 与 Jetpack Compose 新组件/修饰符，文档为每个组件提供视觉示例。
- 📊 EAS Observe 已 GA；SDK 58 增加 registerIntegration、ErrorBoundary、reportError、expo-image 集成等，AppMetrics 被弃用。
- 🤖 @expo/agent-cli 是面向 agent 的实验性 CLI，提供 status、dev、smoke、skills:sync，并整合 Expo CLI、EAS CLI、expo-doctor。
- 📦 expo-widgets 新增 Android 主屏小组件；iOS Live Activities 增加 staleDate、稳定标识符和运行时配置变更。
- 🧱 Swift Package Manager：SDK 58 为 Expo 应用使用 SwiftPM 打基础；CocoaPods 仍是默认且受支持的路径。
- ⚡ Android 构建加速：expo-modules-core 预编译 .so，空白项目干净 Android debug 构建从约 80 秒降至约 39 秒。
- 🚀 Expo Modules 调用更快：iOS 简单值、长字符串与 async promise 优化，所有 Expo 模块自动受益。
- 🧩 Expo Modules 2.0 Beta：改用 Swift/Kotlin 注解替代 DSL，同步调用显著快于 1.0，Android 部分微基准也快于 TurboModules。
- 🔍 指纹默认改为 balanced，减少因版本号或 node_modules 文件变化导致的不必要原生重建。
- 🦀 实验性 Rust transformer “Noxcturnal”：冷打包约快 2 倍，可通过 experiments.noxcturnalTransformWorker 开启。
- 🧭 Expo Router：data loaders、SSR、middleware、Native Tabs、Toolbars 等稳定；导航核心重构，自定义导航器需阅读迁移指南。
- 🌐 代理/隧道场景下开发服务器连接更可靠；新 @expo/ws-tunnel 2.0 隧道更快更稳定，不再需要 @expo/ngrok。
- ⚛️ React Native 0.88 RC 亮点：SwiftPM 工具、Text 的 fontVariationSettings、TurboModules ArrayBuffer、React Native DevTools 新检查能力。
- 📈 PostHog 集成：运行 eas integrations:posthog:connect 即可设置，并关联 EAS update/build/channel/runtime 信息。
- 📷 其他更新：expo-camera 文档扫描、expo-file-system digest/preview、expo-audio 锁屏与 WAV 录制、expo-image SVG 变量、expo-font 可变字体、expo-notifications 与 expo-location 预览等。
- ⚠️ 破坏性变更：React Native Strict TypeScript API 默认、移除 InteractionManager/Touchable 等、iOS scene 生命周期、NODE_ENV 行为变化、Android R8 默认、expo-file-system write 异步、expo-sqlite 移除 libSQL、expo-router 迁移等。
- 🧰 工具要求：Node.js 22.13+、24.3+ 或 26+；Expo 模块工具兼容 Android Gradle Plugin 9。
- ✅ 已知回归：暂无报告，beta 期间会更新。
- 🧪 试用方式：新建项目或运行 npx expo install expo@next --fix 升级；建议用 EAS Build 或本地 prebuild/run 测试。
- 🐛 反馈问题：使用正确 issue 模板，附最小复现，并注明你正在使用 SDK 58 beta；文档缺口也可反馈。

---

### [无](https://hackernoon.com/react-activity-when-a-render-no-longer-guarantees-an-effect)

**原文标题**: [None](https://hackernoon.com/react-activity-when-a-render-no-longer-guarantees-an-effect)

React 19.2 的 `<Activity>` 允许在隐藏 UI 时保留组件状态与 DOM，但也改变了生命周期预期：组件可能完成渲染却不挂载 Effect。文章通过订阅泄漏、WebSocket 断开、视频未暂停、表单状态保留、预加载与 E2E 定位等案例，说明旧代码若隐式依赖“渲染→Effect→清理”的序列，就可能在引入 Activity 后暴露问题，并给出修复与检查建议。

- ⚛️ `<Activity mode="visible/hidden">` 可在隐藏 UI 时保留 state 和 DOM，替代部分条件渲染。
- 🧠 hidden Activity 仍可因 props 变化而低优先级渲染，但其 Effects 不会挂载；visible 时 Effect 才创建。
- 🐞 旧 hook 在 render 中调用 `store.subscribe()`，依赖 Effect 清理；Activity 让 render 发生但 Effect 未挂载，导致订阅泄漏。
- 🛠️ 修复：订阅与清理应放在同一个 `useEffect` 中；外部 store 优先用 `useSyncExternalStore`。
- 🧪 StrictMode 会双调用 render 和额外 setup→cleanup→setup，可提前暴露不对称 Effect；建议在应用根部启用。
- 🔌 Effects 不等于组件生命周期；WebSocket 等后台连接若应在面板隐藏后继续，需把所有权移到 Activity 外或 Provider。
- 🎥 隐藏 Activity 不会移除 DOM，只加 `display:none`；video/audio/iframe 等需在 Effect/useLayoutEffect 中显式暂停或清理。
- 🧾 state 保留有利有弊：tab 可能受益，但表单关闭再打开会恢复旧输入/错误；必要时用普通 unmount 或改变 `key` 重置。
- 📦 hidden 子树仍可能渲染和保留 DOM，大量昂贵页面会带来内存、DOM 与后台渲染成本。
- 🚀 预加载有限制：`useEffect` 中的 `fetch` 不会在 hidden 时触发；Suspense + `use` 等 render 阶段加载可在预渲染时启动请求。
- 🧪 E2E 需注意：Activity 会让隐藏 tab 的 DOM 仍存在，`getByLabel('Email')` 可能匹配多个元素；应过滤 visible 或在可见 tabpanel 内定位。
- ✅ 使用 Activity 前检查：render 阶段副作用、资源应否随 UI 消失、清理是否依赖 DOM 移除、是否要恢复旧状态、子树保留成本。
- ⚠️ 核心结论：render、Effects、DOM、state 生命周期相关但不同；应检查子树是否隐式依赖旧的“render→mount→Effect→cleanup”序列。

---

### [实时与离线是同一个问题](https://marmelab.com/blog/2026/09/09/real-time-and-offline-are-the-same-problem.html)

**原文标题**: [Real-Time and Offline Are the Same Problem](https://marmelab.com/blog/2026/09/09/real-time-and-offline-are-the-same-problem.html)

overview summary
本文比较 Verdant、TanStack DB 与 Zero 三种本地优先方案，作者通过构建 Verdant 离线 CRM 和 TanStack DB/React Admin 集成，发现离线与实时同步本质相同，核心都是调和分歧状态；现有库能提供即时 UI 与离线能力，但在客户端 ID、变更失败恢复、冲突解决和用户反馈方面仍不完整。

- 🧪 作者构建两个项目：Verdant 离线优先 CRM，以及 TanStack DB 接入 React Admin 的集成库，并用 Zero 的 CRM 测试作对比。
- 🌐 传统 Web 应用依赖请求/响应：UI 速度受网络限制，断网即不可用，多用户编辑靠锁，而锁又依赖持续连接。
- 🗃️ 本地优先数据库将读写放在浏览器 IndexedDB，UI 即时更新，后台同步层负责重试、一致性与冲突调和。
- 🌿 Verdant 是端到端方案：schema、存储、同步开箱即用，冲突策略称“冲突避免”，实际多为最后写入者胜。
- 🧱 TanStack DB 是通用响应式查询基础：提供 live collections，但同步层留给开发者，适合逐步搭建可替换后端。
- ⚡ Zero 是完整同步引擎：客户端 + Postgres 服务端缓存，内置认证、权限和双向同步。
- 🧩 TanStack DB 与 React Admin 范式不匹配：React Admin 的 data provider 是 Promise 异步函数，TanStack DB 是响应式集合，实时查询难以直接接入。
- ⚙️ 集成还遇到 react-query 双客户端问题：React Admin 需要 networkMode always，TanStack DB 需要默认队列行为，二者需分开配置。
- 🆔 本地变更要求客户端生成 ID：UUID/ULID/Nanoid 等更合适；若现有模型用服务器 ID，支持离线写往往需要破坏性迁移。
- 🧨 变更失败与恢复缺少内置支持：TanStack DB 无回滚/重试/通知，Zero 可能静默回滚，Verdant 同步失败也需自行处理。
- ⚔️ 冲突解决普遍是 last-write-wins：Verdant 与 Zero 大体如此，TanStack DB 不表态；可能丢失更新，且缺少冲突提示、合并或丢弃界面。
- 🔄 核心发现：离线与实时同步是同一个问题；差异只是断网时长，二者都需同步协议、乐观变更与分歧状态调和。
- 🎯 适用场景：弱网/现场作业、实时协作最明显；作者认为本地优先架构普遍值得，因为它迫使团队正视冲突并提升韧性。
- 🧭 结论：Verdant 省心但需接受其冲突策略；TanStack DB 灵活但不解决同步本身；当前库仍缺失败反馈与冲突合并路径，如何告知用户“两个真相不一致”仍是核心挑战。

---

### [](https://dev.to/subito/from-1256ms-to-96ms-fixing-inp-in-a-massive-react-dropdown-16l7)

**原文标题**: [From 1,256ms to 96ms: Fixing INP in a Massive React Dropdown - DEV Community](https://dev.to/subito/from-1256ms-to-96ms-fixing-inp-in-a-massive-react-dropdown-16l7)

Subito 的 React MultiSelect 品牌筛选器包含约 1175 个选项，在移动端 4 倍 CPU 降速下打开下拉菜单时，因一次性挂载全部选项导致 INP 高达 1256ms；团队通过约 90 行 useVirtualScroll 虚拟滚动，只渲染可见行和少量缓冲，将 INP 降至 96ms，DOM 选项节点从约 1175 降到 13，但牺牲了 Ctrl+F 搜索离屏项的能力。

- ⚡ 场景：设计系统 MultiSelect 基于 react-select 重做，普通筛选仅十几项很快，但“Marca”品牌筛选在实时页面有约 1175 个选项。
- 🐌 问题：移动端 4x CPU 降速下打开该下拉菜单，INP 为 1256ms，评级“poor”，处于真实用户 INP 体验底部 6%，远超良好阈值 ≤200ms。
- 🔍 原因：INP 的 processing duration 被大量同步工作阻塞；MenuList 收到全部 1175 个品牌，React 一次性创建约 1175 个 Option 组件，而屏幕实际只显示约 6 行。
- 🧠 方案：不重写全部代码，也不引入大型虚拟化库，而是手写 useVirtualScroll，跟踪滚动位置，只挂载可见行，并用 OVERSCAN=5 防止快速滚动时空白闪烁。
- 📏 实现：菜单挂载后用 useLayoutEffect 测量单行高度；通过 totalHeight、startIdx、endIdx、offsetTop 计算渲染切片；外层容器高 1175×40=47000px，内层绝对定位仅渲染约 13 行。
- ⚠️ 前提：所有行必须等高，否则滚动会错位、重叠或无法到达某些项；可用 Set 检查 [role="option"] 的不同高度。若不等高，需统一行高/截断文本，或改用 TanStack Virtual、react-virtuoso。
- 📊 结果：本地 INP 从 1256ms 降至 96ms；[role="option"] DOM 节点从最多约 1175 降至 13。
- ♿ 权衡：虚拟化会移除离屏 DOM，浏览器原生 Ctrl+F 找不到未显示品牌，用户需依赖自定义搜索栏。
- ✅ 检查清单：检查实际挂载量；确认行高是否统一；只渲染可见行加缓冲；关注 DOM 节点数而非条目总数。
- 💬 评论补充：有评论强调“用 Set 检查行高”是核心结论；也有人提醒应区分实验室 4x 降速与真实 RUM/CrUX p75，并认真对待无障碍代价。

---

### [](https://www.elastic.co/search-labs/blog/redux-toolkit-v2-migration-kibana-monorepo)

**原文标题**: [Redux Toolkit v2 migration: 1,100 files, no code freeze | Elasticsearch Labs](https://www.elastic.co/search-labs/blog/redux-toolkit-v2-migration-kibana-monorepo)

Kibana 在不要求各插件团队暂停功能开发的情况下，将 monorepo 中约 1,100 个文件迁移到 Redux Toolkit v2。它反转了常见迁移顺序：默认包名解析到 v2，旧版通过 npm 别名保留，并借助 webpack/rspack、yarn resolutions 和 ESLint 规则隔离两套版本，让各团队按批次自助迁移。

- 🔄 **迁移规模**：约 1,100 个文件被迁移到 Redux Toolkit v2 别名，其中约 1,000 个是机械式的一行 import 替换。
- 🚀 **升级动机**：RTK v2 发布已近三年，带来 Redux core 5、React-Redux 9、Reselect 5、Redux Thunk 3，并要求 React 18，同时移除旧兼容 shim。
- ✨ **v2 新能力**：包括 `createSlice` 内联 selector、可选的 inline async thunk，以及适合代码分割的 `combineSlices` 和 slice reducer 注入。
- 🧩 **使用模式多样**：Kibana 中混用 RTK v1、纯 Redux v4、Kea、redux-saga、typescript-fsa 等，不同模块迁移需求差异很大。
- 📦 **双版本共存**：通过 npm alias 同时安装 v1 与 v2，例如 `redux-toolkit-v1`、`react-redux-v7`、`redux-v4`、`immer-v9`、`reselect-v4`、`redux-thunk-v2`。
- 🏗️ **打包器支持**：`kbn-ui-shared-deps-npm`、webpack externals 和 `NormalModuleReplacementPlugin` 让 v1/v2 在运行时同时可用。
- 📌 **处理 @elastic/charts**：用 yarn resolutions 将其内部依赖固定到 RTK v1，并把相关导入重定向到嵌套 v1 版本。
- 🪝 **保持 Kea 兼容**：通过 webpack/rspack 外部化与替换，让 Kea 继续使用 `react-redux-v7`，与消费者共享同一 React context。
- 🛡️ **ESLint 防错**：新增 `@kbn/imports/no_redux_toolkit_v2_imports` 规则，覆盖约 36 个未迁移路径，并支持自动修复。
- ⚠️ **Context 风险**：React Redux v7 与 v9 使用不同 context，混用会导致 `<Provider>` 匹配错误；插件必须显式固定某一版本。
- 🧭 **迁移分批**：独立内部 store 可单独迁移；共享 RTK 类型的包需一起迁移；Discover、Security Solution、Lens 等大模块按各自时间线推进。
- 🗑️ **范围边界**：已废弃功能可暂留 v1，删除时自然消失；纯 Redux v4 与 Kea 等不属于本次 RTK 迁移。
- 💡 **关键经验**：ESLint 自动约束是防回退的关键；大 monorepo 可考虑“新版本用默认名、旧版本用显式别名”的模式。
- 📈 **代价**：过渡期会增加一定 bundle 体积，但被认为在迁移阶段可以接受。

---

### [深入探究 StyleX](https://flaviocopes.com/stylex/)

**原文标题**: [A deep dive into StyleX](https://flaviocopes.com/stylex/)

StyleX 是 Meta 开发的编译期样式方案：用 JavaScript 对象写样式，构建时编译成普通、去重的原子 CSS 类，浏览器端不做样式注入。文章介绍了它要解决的问题、`stylex.create()` / `stylex.props()` 心智模型、React + Vite 与 Astro 集成，以及变体、主题、响应式、动态值、令牌、动画、静态约束、lint、对比和采用建议。

- 🎯 解决问题：大型项目中 CSS 命名冲突、覆盖关系、样式归属、安全复用、删除规则和未使用 CSS 难以管理。
- 🧠 心智模型：`stylex.create()` 定义样式对象，StyleX 编译器生成原子类，`stylex.props()` 把类名和必要的 `style` 应用到组件。
- ⚛️ React + Vite 设置：安装 `@stylexjs/stylex` 和 `@stylexjs/unplugin`，在 Vite 配置中让 `stylex.vite()` 位于 React 插件之前。
- 🧩 首个组件：样式与组件同文件定义，再用展开语法应用 `stylex.props(styles.card)`，大部分 API 都围绕 `create` 和 `props`。
- 🔍 调试：开发模式会加入 `data-style-src` 和可读标记类名，StyleX DevTools 可追踪样式来源、顺序和对应源码文件。
- 🚀 Astro 集成：Astro 使用 Vite，可复用同一 StyleX 插件；StyleX 主要服务于 React 组件，`.astro` 文件不能直接写 `stylex.create()`。
- ⚡ 原子 CSS：每条声明生成一个小类，跨组件去重复用；HTML 类名更多，但 CSS 重复更少，样式表增长更慢。
- 🧬 样式组合：`stylex.props(styles.card, styles.featured)` 中后传入的同属性样式生效，不依赖生成 CSS 的源顺序；默认长属性优先于简写属性。
- ❓ 条件样式：直接使用 JavaScript 的 `&&` 或三元表达式，`stylex.props()` 会忽略 `false`、`null`、`undefined`，但所有可能样式仍需让编译器看见。
- 🎛️ 变体：用对象查找实现，如 `colorStyles[color]`，TypeScript 可把变体键限制为已定义样式。
- 🖱️ 交互状态：`hover`、`focus-visible`、`active`、`disabled` 等伪类写在对应属性内；伪元素写在样式顶层，建议少用装饰性 `::before` / `::after`。
- 📱 响应式：媒体查询、容器查询和 `@supports` 都按属性嵌套，与默认值放在一起，也可和伪类组合。
- 📏 动态值：用样式函数生成静态类加 CSS 变量，运行时值写入元素 `style`；参数和函数体受限，已知状态应优先用变体。
- 🎨 设计令牌与主题：`stylex.defineVars()` 创建类型化 CSS 变量，需放在 `.stylex.ts` 等文件并命名导出；`stylex.createTheme()` 可覆盖某组变量。
- 🧵 父组件定制：组件可接收 `StyleXStyles`，父样式放在最后以允许覆盖；还可限制可传入属性，比任意 `className` 更安全。
- 🎞️ 动画：`stylex.keyframes()` 定义关键帧，再通过 `animationName` 引用，StyleX 负责生成并关联最终关键帧名。
- 🧪 inline atoms：可选 `@stylexjs/atoms` 提供类似工具类的原子样式，适合小例外；可复用组件仍推荐命名样式。
- 🧱 静态约束：样式对象不能运行任意 JavaScript，不能展开对象，也不能直接使用普通外部导入值；共享值应用 `defineVars()` 或 `defineConsts()`。
- 🌐 全局 CSS：只保留 reset、`body` 默认、字体、CMS 原始 HTML 等全局任务；启用 CSS layers 时，reset 应放独立 layer 并位于 StyleX 之前。
- ✅ Lint：`@stylexjs/eslint-plugin` 可检查有效样式、未使用样式、简写、排序，并用 `propLimits` 等规则限制设计取值。
- 🤖 对 Coding Agents 的价值：StyleX 更严格、类型化、可 lint，减少代理生成不一致代码的空间；但仍需 tokens、组件边界、示例和规则。
- ⚠️ 成本：配置比普通 CSS 复杂，语法更冗长，生态中大量组件基于 Tailwind，且可能需要放弃全局样式表和深层选择器模式。
- 📊 对比：普通 CSS 灵活但需管理作用域；Tailwind 编写快但标记膨胀；运行时 CSS-in-JS 动态但增加运行时；StyleX 组合可预测但约束更强。
- 🧭 采用建议：适合新 React 应用、增长中的组件库和大量代理参与的项目；先在一个真实功能中试点，不建议只为追新而迁移小项目或静态 Astro 站点。
- 🏗️ 生产构建：`npm run build` 后应看到哈希化的原子 CSS，应用代码中不应保留原始 `stylex.create()` 对象；StyleX 本质是编译器加约束，不替代 CSS 知识。

---

### [](https://github.com/shadcn-ui/lint)

**原文标题**: [GitHub - shadcn-ui/lint: An agent-first linter for Tailwind design systems. Write design system rules that agents can verify. · GitHub](https://github.com/shadcn-ui/lint)

overview summary
@shadcn/lint 是面向 AI 编码代理的 Tailwind 设计系统 linter，让团队用可编程规则定义组件允许或禁止的样式，并在违规时给出基于组件、变体和主题的修复指引。

- 🎯 **定位**：agent-first linter，用于 Tailwind 设计系统；定义什么允许，agent 违规时解释问题并建议修复。
- 🧱 **兼容性**：适用于 Tailwind v4，不要求使用 shadcn/ui；支持 ESLint 和 Oxlint。
- ⚖️ **与 TypeScript 的区别**：类型错误只说明“不允许”，@shadcn/lint 还会告诉 agent 应该用什么、去哪里找。
- 🛠️ **可配置规则**：通过 `allow`、`contracts`、自定义 `message` 为组件和子组件设置样式契约。
- 🧩 **contracts**：可按组件模式分别允许 layout、spacing、typography 等，例如 CardTitle 可改字号但不能改字体。
- 💬 **自定义消息与占位符**：错误可包含 `{{component}}`、`{{sizes}}`、`{{file}}` 等，指导 agent 使用设计系统值。
- 📏 **内置规则**：no-restyle、no-raw-colors、no-arbitrary-values、no-inline-styles、no-unknown-classes、require-static-classes。
- ⚙️ **settings.shadcn**：配置组件导入前缀、正则、忽略导入、合并函数、变体函数和共享提示。
- 🏢 **Monorepo 支持**：共享 UI 包可设 `ui` 前缀，并在包目录内关闭规则，各应用保留自己的主题。
- 🚀 **快速开始**：安装 `@shadcn/lint` + Oxlint/ESLint，配置规则，并把 `npm run lint` 写入 AGENTS.md。
- 📦 **版本要求**：Node.js 20.19+；Oxlint 1.80+（JS 插件 API alpha）；ESLint 9.30+。
- 🤖 **Agent 效果**：测试 150+ 任务，几乎都能一轮修正到零违规；多项模型任务 8/8 完成。
- 💰 **成本收益**：Claude 对照运行中，借助 lint 反馈修复违规比仅靠规则便宜 10%–48%。
- 📚 **文档与许可**：提供规则示例、配置、排错和 evals 文档；MIT 许可证。
- ⭐ **仓库状态**：2.1k stars、37 forks、13 issues、1 PR，主分支 13 次提交。

---

### [](https://konvajs.org/docs/react/index.html)

**原文标题**: [React Canvas Library — Getting Started with react-konva | Konva - JavaScript Canvas 2d Library](https://konvajs.org/docs/react/index.html)

react-konva 是一个用于绘制复杂二维图形的 React Canvas 库，为 Konva 框架提供声明式绑定，让开发者能用熟悉的 JSX 组件、props、state 和 hooks 来编写 canvas 图形，每个 Konva 图形（Rect、Circle、Line、Text、Image、Star 等）都可作为 React 组件使用并支持完整事件。它仅支持浏览器环境，不支持 React Native。

- 🎨 **核心概念**：react-konva 是 Konva 的 React 声明式绑定，可类比为“Konva 之于 react-konva，如同 DOM 之于 React”。
- ⚛️ **开发方式**：像写 React DOM 一样用 JSX 组件、props、state 和 hooks 编写 canvas 图形，所有 Konva 图形均提供 React 组件与事件支持。
- 🚫 **平台限制**：仅支持浏览器，不支持 React Native（无 DOM 与 `<canvas>`）；已有 Web 版 Konva 编辑器可嵌入 WebView，新原生应用建议使用 React Native Skia。
- 🔗 **资源与扩展**：konvajs.org 提供大量可交互示例；可通过 React 组件或 Konva 节点 ref 使用浏览器场景图功能；Node.js 渲染则直接使用 Konva。
- 📦 **安装版本要求**：react-konva 主版本必须与 React 主版本匹配——React 19 用 `npm install react-konva konva`，React 18 用 `npm install react-konva@18 konva`。
- 🧩 **基础示例**：通过 Stage、Layer、Rect、Circle、Text 等组件搭建画布，结合 useState 与 onDragEnd 实现可拖拽图形。
- 🛠️ **典型应用场景**：设计编辑器（选择、缩放手柄、历史记录、导出）、无限画布白板、节点编辑器、图像标注工具、楼层平面图与选座地图、图像编辑器、基于 Yjs 的多人协作白板。
- 🏢 **商业方案**：若需要完整编辑器而非基础组件，可使用 Konva 维护者开发的 Polotno 设计编辑器 SDK（UI 为 React，可作组件直接集成，`npm install polotno`）。

---

### [](https://www.react-simple-maps.io/)

**原文标题**: [React Simple Maps](https://www.react-simple-maps.io/)

React Simple Maps V5 已发布，这是一个用于 React 数据可视化的可组合 SVG 地图图表库，基于 d3-geo 与 TopoJSON，提供完全类型化、成熟且高测试覆盖率的 API，可像编写普通 React 布局一样组合地图并绑定地理数据。

- 🗺️ V5 发布：用可组合 SVG 地图图表在 React 中做数据可视化。
- 🧩 组合方式：像写其他 React 布局一样编写地图图表，使用 ComposableMap、Geographies、Geography 等小组件。
- 🧱 技术基础：基于 d3-geo 和 topojson，API 完全类型化、成熟，测试覆盖率超过 90%。
- 📦 安装使用：运行 `npm install react-simple-maps`，组合地图并绑定地理数据后即可可视化。
- 🌍 灵活性：支持自带地图文件；只要有坐标或 GeoJSON/TopoJSON，就能映射国家边界、州界线、河流、土地覆盖等。
- ⏳ 稳定性：项目自 2018 年以来发展近 10 年，核心思路和 API 基本保持不变。
- ⭐ 社区数据：GitHub 星标 3,306+，每周下载量 900k+，MIT 许可证，免费开源。
- ⚡ 体积：完整 gzip 后约 34.3kb，包含 d3-geo。
- 📚 资源：提供入门教程和文档。

---

### [Astryx v0.6.0：会响应的主题，会](https://astryx.atmeta.com/blog/astryx-v0-6-0)

**原文标题**: [Astryx v0.6.0: themes that respond, components that adapt · Astryx](https://astryx.atmeta.com/blog/astryx-v0-6-0)

Astryx v0.6.0 发布，带来响应式主题规则、自适应选择器、Neutral 主题视觉重制、六个新模板，以及以规范驱动迈向 v1 的加固路径；升级需先安装 0.6.0，再运行新版 CLI 升级命令。

- 🧩 将项目中所有稳定 Astryx 包升级到 0.6.0，并用 `npx @astryxdesign/cli upgrade --from "$OLD_VERSION" --apply` 执行升级。
- 🎨 主题现在可在 CSS 中响应视口宽度、指针精度、对比度偏好和减少动态效果等条件，支持多条件组合，规则重叠时后规则优先。
- 📱 AppShell 使用同一套主题宽度映射，新增 `xl` 和 `2xl` 移动导航断点，主题家族也可定义本地 token。
- 🧭 Selector 与 MultiSelector 支持 `presentation="adaptive"`：紧凑屏幕用底部弹窗，宽屏用锚定浮层，并新增空状态与 `isReadOnly`。
- 🧙 新增五个向导模板和一个工作项详情模板：Checkout、Form、Dialog、Inline、Vertical Wizard 与 Work Item Detail，可用 `astryx template <name>` 添加。
- 🌈 Neutral 主题围绕可复现的 OKLCH 调色板重制，语义、语法和分类颜色引用命名色阶，并有意调整亮暗模式、破坏性按钮、状态表面和信息横幅。
- 🛠 新增 OKLCH 调色板生成器，支持终端和 HTML 预览、类型化输出、自定义色阶、确定性生成记录与覆盖保护。
- 📜 为 v1 编写组件与共享系统规范，定义公共 API、行为、无障碍要求、结构、主题目标、状态表示和允许变化，减少实现与文档漂移。
- 🚚 迁移 codemod 处理 focus hook、IME 导入、Resizable 和 Astryx selector 等；CSS 改为 `data-*` 属性选择器，例如 `.astryx-button:is(.primary,[data-variant='primary'])`。
- ⚠️ 迁移后需检查自定义选择器、动态配置、非标准 `isImeKeyEvent` 导入、Stepper 集成、自定义主题工具和预构建主题；AppShell 移动断点边界行为也有变化。
- ✨ 其他改进包括 CheckboxListItem/RadioListItem 无障碍名称、TextInput/TextArea 的 `autoComplete`、Popover 焦点与重开保护、RTL Carousel、CLI 代理指导、doctor 集成、调试记录 `schemaVersion: 3`，以及 `withAstryx()` 拒绝 Turbopack 未样式构建。
- 🙏 感谢贡献者，完整包级说明见 Astryx v0.6.0 发布页。

---

### [Astryx 设计系统](https://astryx.atmeta.com/)

**原文标题**: [Astryx Design System](https://astryx.atmeta.com/)

这是一句关于订单状态的询问，通常用于顾客查询订单当前的位置或配送进度。

- ❓ 核心问题是“我的订单在哪里？”
- 📦 涉及订单查询与物流追踪。
- 🕒 可能表达对配送延迟或未收到商品的关切。
- 🛒 常见于电商购物、外卖或快递场景。
- 📩 期待获得订单最新状态或预计送达时间。

---

### [](https://ilamy.dev/)

**原文标题**: [ilamy Calendar - Lightweight, Pluggable React Calendar Component (Tailwind CSS & shadcn/ui) | Full Calendar Alternative](https://ilamy.dev/)

这是一个基于 TypeScript、Tailwind CSS 和 shadcn/ui 构建的轻量级 React 日历组件，定位为 FullCalendar 的替代方案；核心约 13 KB gzip，支持拖放、资源调度与按需插件，不附带 CSS，让设计系统完全控制外观，适用于 Next.js、Astro 和 React。

- 📅 多视图开箱即用：支持日、周、月、年视图，满足不同日历场景。
- 🖱️ 拖放交互：可直观创建、移动和调整事件大小。
- 🔁 重复事件：支持按日、周、月、年重复，并处理例外情况。
- ⏱️ 事件时长：支持多日、全天和精确时间事件，样式一致。
- 🌍 时区支持：面向国际应用与分布式团队。
- 🎨 样式可控：不附带 CSS，可接入自有设计系统并完全自定义品牌外观。
- 🧩 插件化架构：核心不含插件，通过按需插件扩展重复事件、议程视图等，并从独立子路径导入。
- 📦 轻量可摇树：核心约 13 KB gzip，插件按需启用且可 tree-shake，只打包实际使用功能。
- 🧑‍💻 开发者友好：API 简单，完整 TypeScript 类型支持，插件系统易集成。
- 🌙 生产级特性：内置明暗模式、响应式设计、本地化，并针对大量事件优化性能。
- 🚀 快速开始：可立即安装 ilamy Calendar，为用户提供顺畅的日程体验。

---

### [媒介](https://netil.medium.com/billboard-js-4-1-0-live-resizing-configurable-subchart-react-subpath-csp-safe-worker-e1a6fd0ece88)

**原文标题**: [Medium](https://netil.medium.com/billboard-js-4-1-0-live-resizing-configurable-subchart-react-subpath-csp-safe-worker-e1a6fd0ece88)

billboard.js 4.1.0 发布，重点把过去固定的行为交还给开发者控制：容器拖动时的实时缩放、可独立配置的子图渲染、Canvas 网格线样式、React 子路径导出，以及适配 CSP 的自托管 Worker；同时移除 TextOverlap 的 d3-delaunay 依赖并带来多项修复与优化。

- 🎉 发布 billboard.js v4.1.0，属于小版本更新，但聚焦实时缩放、子图、Worker 来源和 React 集成等控制力提升。
- 📐 新增 `resize.live`，让图表在容器被拖动时实时跟随尺寸，而不是等拖动结束后才重绘。
- ⚡ `resize.live` 会按图表测量重绘耗时，自动选择“逐帧精确重绘”或“拉伸渲染”；一次缩放中只能从重绘切到拉伸，不会来回切换。
- ⚠️ `resize.live` 仅在 `resize.auto` 为 `true` 或 `"parent"` 时生效；密集页面建议只对用户正在看的图表开启。
- 📊 子图现在可独立配置：支持 `subchart.type`、`subchart.types`、独立坐标轴 tick、关闭 brush、连续 focus 网格线等，可渲染为柱状、面积等不同概览。
- 🎨 Canvas 模式支持通过 `canvas.theme.selectors` 映射 `grid.x/y.lines[].class`，为可选网格线及其标签设置画布绘制样式。
- ⚛️ React 组件并入主包，以 `billboard.js/react` 子路径导出，并通过 `bb` prop 传入 billboard 命名空间，避免非 React bundle 拉入根包。
- 🧩 无打包器时可加载 UMD 版 `dist/billboard.react.js`，全局为 `BillboardReact`；注意 React 19 不再提供 UMD 构建。
- 🛡️ 新增 `boost.workerUrl`，可指定自托管 Worker 脚本，适配禁止 `blob:` 的 CSP；`dist/billboard.worker.js` 约 1.5KB，需作为真实资源发布。
- ⚙️ `boost.useWorker` 新增 `"auto"`，仅在超过约 5,000 个单元格时启用 Worker；加载失败、未知操作、超时或结果不匹配时回退主线程。
- 🧹 TextOverlap 插件移除 d3-delaunay 依赖，改用半平面裁剪有界 Voronoi 单元，标签定位恢复同步。
- 🔧 其他改进包括：ESM 构建迁移到 Rolldown、减少重绘时的数据聚合与图例更新、`chart.select()` 支持多选与焦点限制、修复 `bar.radius`、增强 TableView 参数校验和原型污染下的空对象检测。
- 💬 多数更新来自 GitHub 反馈，官方鼓励继续通过 GitHub、Medium 和 dev.to 提供反馈。

---

### [](https://github.com/Shopify/react-native-skia)

**原文标题**: [GitHub - Shopify/react-native-skia: High-performance React Native Graphics using Skia · GitHub](https://github.com/Shopify/react-native-skia)

React Native Skia 是 Shopify 维护的开源项目，将 Skia 图形库引入 React Native，用于实现高性能 2D 图形。仓库当前为公开项目，拥有 8.6k stars、647 forks，并采用 MIT 许可证。

- 🎨 核心功能：为 React Native 提供基于 Skia 的高性能 2D 图形能力。
- 🧩 Skia 背景：Skia 是 Google Chrome、Chrome OS、Android、Flutter、Firefox 等产品的图形引擎。
- 📚 文档资源：完整文档与安装说明见 shopify.github.io/react-native-skia。
- 🤝 贡献说明：开发、构建、测试与贡献指南详见 CONTRIBUTING.md。
- 🧪 Graphite 后端：Skia 有 Ganesh 与 Graphite 两个后端，Ganesh 为默认后端。
- ⚙️ Graphite 预览：可通过 `yarn add @shopify/react-native-skia@next` 安装实验版 Graphite。
- ⚠️ 使用限制：Graphite 高度实验性，不建议用于生产；Android 需 API Level 26 及以上。
- 🛠️ 自行构建：可用 `SK_GRAPHITE=1 yarn build-skia` 构建支持 Graphite 的 Skia；预构建库会通过标记文件自动检测。
- 📦 仓库结构：包含 .github、.vscode、.yarn、apps、externals、packages/skia 等目录，以及 package.json、turbo.json、yarn.lock 等文件。
- 🏷️ 项目主题：react、react-native、skia；提供 Readme、MIT 许可、行为准则与安全政策。
- 🔢 社区数据：8.6k stars、647 forks、256 watching、42 issues、51 pull requests、3,946 commits。

---

### [](https://github.com/margelo/react-native-nitro-sqlite)

**原文标题**: [GitHub - margelo/react-native-nitro-sqlite: 💽 Fast SQLite library for React Native built using Nitro Modules · GitHub](https://github.com/margelo/react-native-nitro-sqlite)

`react-native-nitro-sqlite` 是 Margelo 开发的高性能 React Native SQLite 库，基于 Nitro Modules 与 JSI API，提供同步/异步数据库操作，并取代已弃用的 `react-native-quick-sqlite`。

- 📦 公开仓库：`margelo/react-native-nitro-sqlite`，约 565 stars、53 forks、44 issues、35 PR，MIT 许可。
- ⚠️ 重要变化：`react-native-quick-sqlite` 已弃用，9.0.0 起改用 `react-native-nitro-sqlite`；8.x 仅有限期修复。
- 🚀 安装：`npm i react-native-nitro-sqlite react-native-nitro-modules`，再执行 `npx pod-install`；需要 Nitro Modules 与 React Native 0.75+。
- 🧩 核心特性：内嵌 SQLite，暴露 JSI API；每个操作有同步与异步版本，异步在 JS 线程外运行。
- 🗄️ 打开数据库：使用 `open({ name })`，连接绑定数据库名；`location` 为相对于平台数据库目录的路径。
- ⚙️ API 概览：`execute/executeAsync`、`executeBatch/executeBatchAsync`、`loadFile/loadFileAsync`、异步 `transaction`、`close/delete`、`attach/detach`。
- ⏱️ 同步 vs 异步：同步在 JS 线程执行，适合小任务；异步在 JS 线程外执行，适合大量或重查询，避免阻塞 UI。
- 🧵 并发规则：同一 `db` 上异步操作按调用顺序执行；异步会等待活动事务；冲突同步操作或 `close()` 会抛 busy 错误。
- 🧪 基础用法：结果含 `results`、`rowsAffected`、`insertId`；参数支持 boolean、number、string、ArrayBuffer、null；应参数化绑定用户输入。
- 🔐 事务：`db.transaction(async tx => ...)` 仅异步；回调内必须使用 `tx`，不要 await 同库的 `db.executeAsync` 等，以免死锁。
- 📦 批处理：命令数组含 `query` 与可选 `params`；也可用单条 query 加 params 数组批量执行。
- 📊 列元数据：查询结果可含 `metadata`，提供列名、类型与索引。
- 🔗 Attach/detach：可附加其他数据库文件用于跨库 JOIN，关闭主连接会分离所有。
- 📄 加载 SQL 文件：在独占事务中按行执行非空 SQL，每行一条命令，不支持多行语句；大文件宜用异步。
- 📁 数据库位置：默认在 iOS 文档目录或 Android files 目录；`location` 是相对目录；外部数据库需先复制/移动；删除前先关闭连接。
- ❗ 错误处理：JS 辅助方法会将数据库失败规范化为 `NitroSQLiteError`。
- 🧠 向量搜索：可选 `react-native-nitro-sqlite-vec`，静态链接 sqlite-vec；iOS 用 `NITRO_SQLITE_VEC=1 pod-install`，Android 设 `nitroSqliteVec=true`；提供 `createVectorTable`、`knnSearch` 等 helper。
- 🛠️ TypeORM：可作为 TypeORM driver；需暴露 TypeORM `package.json`、使用 patch-package、在 `babel.config.js` 中别名，并使用 `typeORMDriver`。
- ⚙️ 配置：默认 `SQLITE_THREADSAFE=1`，可在 `package.json` 设置 `nitroSQLite.threadSafe`；支持平台覆盖与 iOS 系统 SQLite。
- ⚡ 性能模式：默认启用 NitroSQLite 性能编译标志，可在 `package.json` 设 `performanceMode`；包含 `SQLITE_DQS=0`、`SQLITE_DEFAULT_WAL_SYNCHRONOUS=1` 等。
- 🧱 编译选项：可通过 iOS Podfile 的 `post_install` 和 Android `gradle.properties` 添加 FTS5、Geopoly 等标志。
- 🔐 iOS 配置：可设 `RNNitroSQLite_AppGroup`；默认 Documents，可设 `RNNitroSQLite_DatabaseLocation=ApplicationSupport` 并自动迁移；App Group 下该位置选项无效。
- 📤 导出：`open`、`NitroSQLite`、`NitroSQLiteError`、`typeORMDriver` 及相关类型；推荐优先使用 `open()`。
- 💬 社区与许可：可加入 Margelo Community Discord；项目采用 MIT License。

---

### [](https://jobs.fidelity.com/en/life-at-fidelity/our-stories/tech-careers/fidelity-tech-strategy-empowers-associates/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-sl2-txt)

**原文标题**: [Work where they invest in technology and technologists. | Fidelity Careers](https://jobs.fidelity.com/en/life-at-fidelity/our-stories/tech-careers/fidelity-tech-strategy-empowers-associates/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-sl2-txt)

Fidelity 认为，赋能技术人才的最佳方式是提供能帮助他们实现目标、服务客户的优质技术，并在职业生涯中持续投资其技能培训。因此公司既重视战略技术栈建设，也重视技术人员的成长与实践。

- 💡 Fidelity 大力投资技术，以赋能员工和客户，推动双方更好地发展。
- 🧰 技术员工可获得时间、资源和动手实践，不断提升技能水平。
- 🎯 技术采用强调实用且高质量，既帮助客户实现购房、提前退休等财务目标，也提升内部团队效率。
- 🤝 通过辅导、导师制和社交网络，帮助技术员工建立联系、共同成长。
- 🔍 评估和整合新技术时，关注行业趋势、最佳用例、真实场景测试、清晰路线图，并持续重估技术是否满足质量与业务需求。
- 🔐 以高效且安全的方式使用技术和金融科技，既帮助员工，也确保客户数据安全。
- 📚 技术落地后提供培训，但实时接触和实践才是提升能力的关键。
- 🚀 Fidelity 长期投资技术人才技能；有意者可加入 Talent Network，优先获取职位信息和求职建议。

---

### [](https://www.f5.com/labs/articles/cloud-takeover-mass-scanning-for-exposed-vite-endpoints-cve-2026-39364)

**原文标题**: [Cloud Takeover: Mass Scanning for Exposed Vite Endpoints (CVE-2026-39364) | F5 Labs](https://www.f5.com/labs/articles/cloud-takeover-mass-scanning-for-exposed-vite-endpoints-cve-2026-39364)

overview summary
2026年8月，F5 Labs 观察到针对暴露 Vite 开发服务器的大规模自动化扫描，核心是 CVE-2026-39364 文件读取/访问控制绕过，攻击者批量窃取 .env、云凭证、Azure 令牌与 Terraform 状态文件；活动约 807 组会话/32,000 原始事件，主要源自美国等地云基础设施，并伴随旧版 PHP、Exchange、WordPress 等 CVE 的持续利用。防御重点是消除开发端口外暴露、更新 Vite、WAF 拦截 /@fs/、验证爬虫来源并轮换可能泄露的密钥。

- 🚨 CVE-2026-39364：Vite 开发服务器未认证文件读取/ACL 绕过，CVSS 7.5，CWE-200，影响 Vite 7.1.0 至 7.3.2 前及 8.0.5 前。
- 🧩 利用方式：通过 ?raw、?import&raw、?import&url&inline 等查询参数绕过 server.fs.deny，经 /@fs/ 读取敏感文件。
- 🔗 相关 Vite 漏洞：CVE-2025-30208、CVE-2025-31125、CVE-2024-45811 可协同触发，只有 CVE-2025-31125 列入 CISA KEV。
- ⚙️ 攻击链：扫描器向 /@fs/ 发 GET，路径规范化/查询串校验失败，服务器以 HTTP 200 明文返回目标文件。
- 🎯 目标文件：.env 系列、AWS credentials/config/backup、Azure tokens、Terraform tfstate/tfvars、serverless 状态、/etc/passwd、/proc/self/environ。
- 🕵️ 探测特征：尾部分隔符、双编码路径穿越（%252f）绕过代理/WAF，伪造 Googlebot、ClaudeBot、GPTBot、PerplexityBot 等 User-Agent。
- 🌐 伪造头：注入 X-Forwarded-For/X-Real-IP（如 34.94.237.62、104.28.219.193）以绕过 IP 白名单并干扰日志。
- 📊 活动规模：807 组会话、约 32,000 原始事件；信息泄露 32,010、可预测资源位置 1,729、路径穿越 1,586。
- ☁️ 来源分布：美国 17,297、比利时 4,407、荷兰 4,011、新加坡 2,842、台湾 1,994、日本 1,353；大量来自 Google Cloud 34.x/35.x。
- 🧭 MITRE ATT&CK：侦察 T1595.002、初始访问 T1190、凭证访问 T1552.001、收集 T1005、发现 T1083。
- 🥇 2026年8月 Top CVE：CVE-2017-9841 居首 4,201 攻击/123,188 事件；CVE-2018-14028 激增至 4,102 升至第二。
- 📈 其他趋势：CVE-2018-20062 3,482；CVE-2024-4577 增 2,612 至 3,023；CVE-2021-26855 2,777；CVE-2022-41082 2,641。
- 🆕 新进榜：CVE-2021-34523（1,853）、CVE-2024-44000（1,079）、CVE-2016-4800（1,078）；CVE-2022-41040 掉出。
- 🧨 CVE-2018-14028：WordPress 插件 ZIP 校验绕过，单月最大激增，需审计插件版本与异常 ZIP 上传。
- 🐘 CVE-2024-4577：Windows PHP CGI 参数注入，CVSS 9.8，持续上升，需立即修补或迁移出 CGI。
- 🧱 长期趋势：CVE-2017-9841 与 CVE-2018-20062 从 2025 峰值回落但仍被持续利用；CVE-2018-14028 反弹至最高月总量。
- 📉 攻击类型：可预测资源位置 945,081（+153%）、信息泄露 620,931（+148%）、命令执行 234,256（+47%）、服务器端代码注入 249,433（+32%）。
- 🦠 恶意软件/扫描：Trojan/Backdoor/Spyware 增至 51,537（近 +700%），漏洞扫描增至 8,711（+184%）。
- 🌍 来源国家：美国超 450 万（+178%）、法国 250 万、德国 1,359,473、新加坡 911,605；中国微降至 816,154。
- 🗺️ 目标特征：韩国重目录遍历/文件泄露；加拿大重新披露框架绕过/注入；美国攻击混合最广；英国新增注入/RCE；日本旧漏洞长尾。
- ✅ 建议：升级 Vite 至 7.3.2、8.0.5 或最新补丁；确保开发端口（如 5173）不暴露公网。
- 🛡️ 防护：部署现代 WAF（如 F5 Advanced WAF）拦截 /@fs/ 与 Vite 利用模式；不要仅凭 User-Agent 放行爬虫，需反向 DNS 验证。
- 🔄 应急：若 2026年8月期间未修补 Vite 开发服务器曾暴露，立即轮换 .env、AWS、Azure、Terraform 等可能泄露的密钥。

---

### [](https://github.com/hemanth/functional-programming-jargon)

**原文标题**: [GitHub - hemanth/functional-programming-jargon: Jargon from the functional programming world in simple terms! · GitHub](https://github.com/hemanth/functional-programming-jargon)

这是一个由 hemanth 维护的开源项目 functional-programming-jargon，用通俗易懂的方式整理了函数式编程领域的专业术语表，帮助开发者更容易学习函数式编程。仓库使用 JavaScript（ES2015）示例，遵循 Fantasy Land 规范，并提供交互式图谱、AI/LLM 规范以及十余种语言的翻译版本。内容涵盖从基础概念到范畴论应用的完整术语体系，包括函数组合、柯里化、函子、单子、代数数据类型、光学（Lens/Prism/Iso/Traversal）等核心主题，并附有大量代码示例与延伸阅读链接。

- 📚 **项目定位**：函数式编程术语表（Glossary），旨在降低学习 FP 的门槛，让开发者快速理解 FP 特有的术语体系。
- ⭐ **社区热度**：GitHub 上获得约 18.7k Star、999 Fork、353 Watcher，采用 MIT 许可证，欢迎社区贡献。
- 💻 **示例语言**：所有示例用 JavaScript（ES2015）编写，并在适用处遵循 Fantasy Land 规范。
- 🌐 **多语言支持**：提供葡萄牙语、西班牙语、中文、印尼语、韩语、波兰语、法语、土耳其语、俄语等多语言翻译，另有 Python、Scala、Rust、Julia、Haskell 等生态版本。
- 🧮 **基础概念**：涵盖 Arity（元数）、高阶函数（HOF）、Closure（闭包）、Partial Application（偏应用）、Currying（柯里化）、函数组合（Composition）、Continuation（续延）、Trampoline（弹床）、Thunk（惰性包装）等。
- ✨ **纯度与可预测性**：Pure Function（纯函数）、Side Effects（副作用）、Idempotence（幂等性）、Referential Transparency（引用透明）、Equational Reasoning（等式推理）、Memoization（记忆化）。
- 🔄 **函子与单子体系**：Functor、Pointed Functor、Applicative Functor、Monad、Comonad、Monad Transformer、Free Monad、Kleisli Composition、Bifunctor、Contravariant Functor、Profunctor、Alternative。
- 🧠 **范畴论相关**：Category（范畴）、Semigroupoid、Morphism（态射）、Homomorphism、Endomorphism、Isomorphism、Catamorphism、Anamorphism、Hylomorphism、Paramorphism、Apomorphism、Natural Transformation。
- 🧩 **数据类型与代数结构**：Setoid、Semigroup、Monoid、Foldable、Traversable、Algebraic Data Type、Sum Type、Product Type、Option、Either、Total/Partial Function。
- 🔍 **光学与类型签名**：Lens（透镜）、Prism（棱镜）、Iso（同构）、Traversal（遍历）、Type Signatures（类型签名）等现代 FP 工具。
- 🛠️ **JS 生态库推荐**：列出 Mori、Immutable、Immer、Ramda、Folktale、monet.js、lodash、Sanctuary、Crocks、Fluture、fp-ts 等常用函数式编程库。
- 🎨 **附加资源**：提供交互式图谱、面向 Agent/LLM 的规范文件、贡献指南以及各类延伸阅读链接。

---

### [FP 术语 — 交互式函数式编程知识图谱](https://hemanth.github.io/functional-programming-jargon/)

**原文标题**: [FP Jargon — Interactive Functional Programming Knowledge Graph](https://hemanth.github.io/functional-programming-jargon/)

暂未收到需要总结的文章内容，因此无法生成有效摘要。请补充文本后，我会按中文要点列表格式提炼关键信息。

- 📭 当前输入中未包含可总结的正文内容。
- ✍️ 请粘贴文章或文本，我将立即整理摘要。
- 🧾 输出会使用“-”符号，并为每条要点搭配合适的 emoji。

---

### [](https://philipwalton.com/articles/modern-web-types/)

**原文标题**: [Modern Web Types â Philip Walton](https://philipwalton.com/articles/modern-web-types/)

文章介绍 modern-web-types：它通过将 TypeScript 官方 DOM/WebWorker 类型生成器的浏览器引擎支持阈值从两个降为一个，为已在新式浏览器中发布但尚未被 TS 官方类型覆盖的 Web API 提供完整类型，从而消除使用 startViewTransition、Long Animation Frame API、fetchLater 等时的类型错误。

- 😣 作者常见困扰：TypeScript 内置库缺少单引擎新 Web API 类型，导致本可安全渐进增强的功能被误报为错误。
- 🧩 原因是 TS 的 Web API 类型生成政策只纳入至少两个浏览器引擎支持的 API。
- 🚀 modern-web-types 是官方 DOM 与 WebWorker 库的替代品，基于 TypeScript 自己的生成器，但将引擎支持门槛降为 1。
- 📦 安装方式：npm install --save-dev @typescript/lib-dom@npm:modern-web-types；TypeScript 6+ 还需在 tsconfig.json 中设置 "libReplacement": true。
- 📈 新增声明很多：DOM 新增 433 个接口、96 个类型别名、223 个全局、311 个已有接口成员；WebWorker 分别为 144、35、56、64。
- 🔧 这些新增不只是冷门功能，也包括 Document、Element、Navigator、Request 等常用接口缺失的成员。
- 🤖 类型生成自动化：使用与 TS 相同的 TypeScript-DOM-lib-generator 和 w3c/webref 数据源，每周通过 GitHub Actions 对比更新并开 PR，批准后发布。
- ⚖️ 作者认为 two-engine 政策并不能防止代码在浏览器中失效；缺少官方类型反而促使用户使用 @ts-ignore、as any 或不准确类型。
- 🌐 单引擎 API 常可安全用于渐进增强，如部分 Core Web Vitals 性能 API 最初仅 Chrome 支持，却推动了 Web 性能提升。
- 🧪 使用单引擎 API 时，应在所有目标浏览器中测试，并可用 eslint-plugin-baseline-js 按 Baseline 目标提前发现问题。
- ✅ 如果从未遇到缺失类型，可不使用；若遇到，modern-web-types 比手动添加类型更省事、更少冲突。作者希望未来 TS 放宽政策后该库不再必要。

---

### [](https://github.com/philipwalton/modern-web-types)

**原文标题**: [GitHub - philipwalton/modern-web-types: TypeScript types for new web platform APIs that aren't yet in lib.dom. · GitHub](https://github.com/philipwalton/modern-web-types)

modern-web-types 是一个 GitHub 仓库，为已在至少一个稳定浏览器中发布、但尚未进入 TypeScript 内置 DOM 类型定义的 Web API 提供 TypeScript 类型。它复用 TypeScript 官方生成管线，填补官方类型因“两个或以上浏览器引擎”政策而留下的空白。

- 📦 项目定位：生成 `lib.dom`、`webworker` 等环境的完整替代类型库，质量与官方类型相同，区别是包含更多新 API。
- 🧩 存在原因：TypeScript 内置类型只收录两个及以上浏览器引擎已实现的 API，导致一些已可用且广泛使用的 API 没有官方类型。
- ⚙️ 安装方式：推荐用 `npm install --save-dev @typescript/lib-dom@npm:modern-web-types` 安装，让 TypeScript 的 DOM 库解析到本项目。
- 🛠️ 配置要求：TypeScript 6+ 需在 `tsconfig.json` 中开启 `"libReplacement": true`；TypeScript 4.5–5.x 默认支持库替换，无需额外设置。
- 👷 Workers 与其他环境：可从 `lib` 中移除对应库，并在 `types` 中引用 `modern-web-types/webworker`、`serviceworker`、`sharedworker`、`audioworklet` 等入口。
- 📚 入口对应关系：`modern-web-types/dom` 替代 `DOM`；`webworker` 替代 `WebWorker`；`serviceworker` 替代 `@types/serviceworker`；`sharedworker` 替代 `@types/sharedworker`；`audioworklet` 替代 `@types/audioworklet`。
- ⚠️ 重要提醒：如果项目原本没有设置 `types`，添加它会让 TypeScript 不再自动包含 `node_modules` 中所有 `@types/*` 包，只使用显式列出的包。
- 🔁 更新机制：每周一自动重新固定生成器和入口类型注册表，重新生成五个 lib、运行测试，并提交 PR；新 API 会在生成器数据收录后的下一个周一进入。
- 🧪 生成流程：固定并打补丁；分别按“两引擎”和“一引擎”构建两次；用 TypeScript 编译器 API 做结构化 diff；再为每个环境生成独立 lib。
- 🧰 开发命令：`npm run update` 执行获取上游、构建、diff、生成 lib、测试、README、报告等流程；`npm test` 对每个生成 lib 做类型检查并限制增量大小。
- 🧷 TypeScript 版本：项目同时安装 TypeScript 6 和 TypeScript 7 别名；`diff` 与 `emit-lib` 使用 TS 6，`npm test` 用最新版检查生成输出。
- 🚀 发布流程：修改 `pkg/package.json` 中的 `version` 并合并到 `main` 会触发发布工作流，将 `pkg/` 发布到 npm 并打标签；版本不变则不会发布。
- 🔗 相关项目：官方 `lib.dom.d.ts` / `@types/web` 来自同一生成器；`@types/dom-*` 是手写的单功能补丁，而本项目提供生成式完整 lib。
- 📄 许可证：Apache-2.0；生成输出源自 `TypeScript-DOM-lib-generator`，Web IDL 来自 `webref`，各自遵循相应许可证。
- ⭐ 仓库状态：该仓库约有 51 个 star、0 个 fork、30 次提交，当前 issues 和 pull requests 均为 0。

---

### [GitHub Actions 新增 cache-mode 以](https://socket.dev/blog/github-actions-cache-mode)

**原文标题**: [GitHub Actions Adds cache-mode to Limit Cache Poisoning Risk | Socket](https://socket.dev/blog/github-actions-cache-mode)

GitHub Actions 新增 cache-mode，为 Actions 缓存提供最小权限控制，以降低缓存投毒风险；该攻击曾影响 Ultralytics PyPI 和 TanStack npm 等供应链目标。

- 🔒 cache-mode 限制工作流或作业对 Actions 缓存的访问，防止一个上下文写入的缓存被另一上下文恢复并执行。
- 🧪 缓存投毒可让攻击者写入恶意构建产物或依赖，随后以可信工作流的权限和密钥运行；TanStack 攻击结合 pull_request_target pwn request，发布 84 个恶意版本，涉及 42 个 @tanstack/* 包。
- 📜 SLSA provenance 和 Sigstore 签名无法发现被污染的缓存，因为证明只覆盖构建来源，不验证从缓存拉取的输入完整性。
- ⚙️ cache-mode 支持四种值：read（可恢复、不可保存；低信任事件如 pull_request_target 的默认）、write（可恢复和保存；push 等受信任事件默认）、write-only（可保存、不可恢复）、none（禁止所有缓存访问）。
- 🧱 作业级设置覆盖工作流级设置，由缓存服务强制执行，并沿可复用工作流传导，调用方不能授予超出自身的缓存权限。
- ⚠️ 在低信任事件中声明 write 或 write-only 会重新引入投毒风险，GitHub 会添加警告注解。
- 🤖 GitHub 建议对 AI 代理工作流使用 cache-mode: none；设计提案提到代理处理 issue/PR 文本可能执行不可信输入，类似 Cline 事件中的提示注入导致疑似缓存投毒。
- 🗣️ write-only 模式源于公开反馈：安全研究员 Adnan Khan 推动增加该模式，使可信分支可填充缓存但不恢复。
- 🧩 cache-mode 不覆盖其他 Actions 风险；检出不可信代码、运行包生命周期脚本或在 runner 内铸造 OIDC token 仍可能暴露。
- ✅ GitHub 建议按工作流或作业授予所需的最小缓存访问权限。

---

### [](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

**原文标题**: [Postmortem: TanStack npm supply-chain compromise | TanStack Blog](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

2026年5月11日，TanStack 的 Router/Start 相关 npm 包遭遇供应链攻击。攻击者组合利用 GitHub Actions 的 `pull_request_target`、缓存投毒和 OIDC 令牌内存提取，在约 6 分钟内发布 84 个恶意版本，涉及 42 个 `@tanstack/*` 包。事件由外部安全研究员在约 20–26 分钟后发现，所有受影响版本已被废弃并由 npm 移除 tarball；其他 TanStack 包及当前所有可安装版本均安全。2026年5月15日官方发布全部安全确认，但曾安装受影响版本的主机应视为可能被入侵并轮换凭证。

- 🚨 事件时间：2026-05-11 19:20–19:26 UTC，攻击者发布 84 个恶意版本，覆盖 42 个 `@tanstack/*` 包，每包 2 个版本。
- 🎯 受影响范围：仅 Router/Start 仓库相关 monorepo 包受影响；Query、DB、Store、AI、Table、Form、HotKeys、Virtual、Pacer、Config、Devtools、CLI、Intent 等未受影响。
- 🧬 攻击链：`pull_request_target` “Pwn Request” + GitHub Actions 缓存投毒跨 fork/base 信任边界 + 从 runner 进程内存提取 OIDC token。
- 🔓 凭据情况：没有 npm token 被盗，npm 发布工作流本身未被攻破；恶意发布通过 OIDC 直接向 npm registry 发送请求。
- 🐴 恶意载荷：受影响包加入恶意 `optionalDependencies`，安装时执行约 2.3 MB 混淆脚本 `router_init.js`。
- 🕵️ 载荷行为：收集 AWS、GCP、Kubernetes、Vault、npm、GitHub、SSH 等凭证，通过 Session/Oxen 加密网络外传，并尝试自我传播到同一维护者的其他包。
- ⏱️ 检测响应：StepSecurity 研究员 ashishkurmi 在约 20–26 分钟后公开报告 issue #7383；团队随后开始废弃恶意版本。
- 🧹 清理进度：21:03 UTC 完成全部 84 个版本废弃；npm 在 22:13–23:55 UTC 移除受影响 tarball；5月12日 05:02 提交正式 IOC 邮件。
- ✅ 当前状态：2026-05-15 全部安全；所有当前可安装的 TanStack 包版本，包括 Router/Start，均可安全安装。
- ⚠️ 凭证建议：任何在 2026-05-11 安装过受影响版本的开发者或 CI 主机，应轮换 AWS、GCP、Kubernetes、Vault、GitHub、npm、SSH 等可达凭证。
- 🧱 根因一：`bundle-size.yml` 使用 `pull_request_target`，检出并运行 fork PR 合并引用代码，且 `actions/cache` 写入缓存不受 `permissions` 限制。
- 🧱 根因二：缓存作用域为仓库级，`pull_request_target` 可污染 main 上 `release.yml` 之后会恢复的缓存条目。
- 🧱 根因三：`release.yml` 的 `id-token: write` 使恶意代码可从 `/proc` 内存提取 OIDC token，绕过正常发布步骤直接写 npm。
- 🔎 IOC 指纹：恶意 `optionalDependencies` 含 `@tanstack/setup` 指向 `github:tanstack/router#79ac49ee...`，文件 `router_init.js`，缓存 key `Linux-pnpm-store-6f9233...`，外传域名包括 `filev2.getsession.org`、`seed{1,2,3}.getsession.org`。
- 🧑‍💻 攻击者信息：账号 `zblgg`、`voicproducoes`；伪造提交身份 `claude <claude@users.noreply.github.com>`；恶意 fork 为 `zblgg/configuration`。
- 📜 跟踪信息：跟踪 issue 为 `TanStack/router#7383`，GitHub Security Advisory 为 `GHSA-g7cv-rxg3-hmpx`。
- 📉 经验教训：缺少内部发布告警，`pull_request_target` 未审计，第三方 action 使用浮动引用，npm unpublish 受依赖限制，OIDC 发布缺少逐次审查。
- 🍀 幸运因素：恶意载荷破坏测试导致正常发布步骤跳过，使攻击较容易被发现；且攻击者复用公开 tradecraft，便于快速匹配 IOC。
- ❓ 未决问题：是否有 npm 缓存被污染、fork 网络中是否仍有孤儿提交、其他仓库是否有同类模式、实际下载人数等仍待调查。

---

### [推出固定费率 CDN - Vercel](https://vercel.com/blog/introducing-flat-rate-cdn)

**原文标题**: [Introducing Flat Rate CDN - Vercel](https://vercel.com/blog/introducing-flat-rate-cdn)

Vercel 为 Pro 团队推出 Flat Rate CDN，以固定月费、内置尖峰防护和分层容量替代按量计费，避免病毒式发布或流量突增带来意外高额账单，同时保持高质量 CDN 网络性能。

- 💡 背景：原有 CDN 按量计费难以预测，病毒式发布、流量爆发或错误路由可能导致意外高额账单。
- 📦 方案：Flat Rate CDN 是 Pro 团队的固定月费替代方案，账单可预测，并内置流量尖峰保护。
- ✅ 优势：固定月价、覆盖流量尖峰、无超额费用；CDN 请求、Fast Data Transfer 等不再直接计费。
- 🌐 性能：仍使用 Vercel 高级网络与私有光纤，可绕开公网拥塞，性能最高提升 60%，尖峰期间不降级。
- 👥 默认与范围：所有新 Pro 团队默认启用，现有 Pro 团队可自愿开启；按团队统计，覆盖所有项目。
- 💳 包含资源：一个固定月费覆盖 CDN 请求、Fast Data Transfer、Blob Data Transfer，以及 CDN 请求产生的可观测事件。
- 📊 档位：Pro 默认含 100 万请求 / 1TB；$20/月为 1000 万请求 / 50TB；$100/月为 5000 万请求 / 50TB；$300/月为 1.5 亿请求 / 50TB。
- ⚡ 尖峰处理：计费周期内档位固定；临时流量高峰不会造成额外费用，也不会导致账单上涨。
- 🛡️ 无上限无性能损失：系统识别并剔除临时尖峰来评估容量，每月按持续使用量调整档位，不会因流量走红而宕站。
- 📈 可观测：仍可在 Usage 页面或 CLI 监控所有覆盖资源，包括被 Vercel 吸收的流量尖峰。
- 🗣️ Beta 反馈：客户减少账单焦虑，不再频繁检查机器人流量，并更愿意采用缓存组件和缓存策略。
- 🚀 启用方式：新 Pro 默认开启；现有团队可在 Billing > Flat Rate CDN 中开启、选择档位并启用。
- ❓ FAQ：超容量不会中断或额外收费，可能被移至 Flex CDN 并在下个周期调整；可随时退出回按量付费；接近容量会收到通知。

---

