### [](https://linear.app/now/styling-linear-for-the-future-stylex)

**原文标题**: [Styling Linear for the future with StyleX](https://linear.app/now/styling-linear-for-the-future-stylex)

overview summary
由 Linear 工程团队撰写的这篇文章，完整回顾了他们如何将 React 代码库从 styled-components 迁移到 StyleX。项目历经 1000 多个 PR，结合确定性 codemod、编码代理与人工审查，最终解决了性能退化、远程样式覆盖难以约束等问题，建立起一套更清晰、更适合 AI 代理协作的样式系统。

- ⏳ 迁移耗时极长，累计超过 1000 个 PR，才把 Linear 的 React 应用从 styled-components 全面迁移到 StyleX。
- 🚨 旧方案难以为继：styled-components 曾因 API 灵活而好用，但在 React 18 并发渲染下出现性能回退，并进入维护模式；Redesign 后不断追查 UI 回归，也暴露出从外部重开组件样式的模式极难维护。
- 🧭 选择 StyleX 的主要原因：样式在构建期生成而非渲染期注入；让远距离改样式变得“刻意困难”；提供确定性的样式合并；同时类型安全、与 React 协作良好、维护活跃。
- ⚖️ 与 vanilla-extract 对比后胜出：vanilla-extract 虽有静态提取和强类型，但 API 较碎片化，且样式文件与组件分离不符合 Linear 的习惯；StyleX 允许样式与组件共存，API 更小、更平衡。
- 🛠️ 迁移挑战极高：styled-components 几乎是图灵完备的 CSS 表达方式，同一个意图有无数种写法；加上 Linear 没有正式设计系统，导致早期自动化迁移非常容易产出“看似正确实则错误”的结果。
- 🔁 可落地的组合策略：先后续构建 StyleX 变量、常量与共享原语；从叶子组件开始迁移，减少样式级联影响；再用 styled-components-to-stylex-codemod 做确定性转换，并引入编码代理扩充覆盖面，最终由人工处理边缘情况。
- 🤖 代理与人工的分工演变：代理擅长处理重复性工作，但早期很难可靠验证视觉差异，如复杂 hover、主题分支和小布局变化；直到 Fable 与 Sol 模型发布，代理能力增强后，才在迁移中承担起更多核心任务。
- 📊 推动团队落地的手段：在开发工具栏加入“剩余 styled-components”计数器；开发高亮工具区分已迁移与未迁移组件；持续生成每周迁移图表；机器人也会在 PR 中提醒新增 styled-components，防止旧模式回流。
- 🧹 用自定义工具锁定新规范：新增 lint 规则与仓库级检查器，禁止 styled-components 导入、清理废弃 className/style props，并确保组件通过 sx 暴露样式契约且能跨组件正确传播。
- 🎨 强制设计一致性：用共享变量替代硬编码颜色、字体、阴影等；统一 hover、press、link 行为；并拦截 shorthand、条件样式等因 StyleX 属性优先级而可能“静默丢失”的写法。
- 🛡️ 保留必要的逃生舱：对全局选择器、第三方 DOM 等仍属“CSS 问题”的场景，使用 CSS Modules 作为显式回退；同时通过嵌套 ThemeProvider 动态注入 CSS 规则，扩展出符合 Linear 需求的复杂主题系统。
- ⚡ 性能收益显著：在视图密集型页面，移除运行时样式注入后，主线程 CPU 工作量约减少 20%–35%；中端机器上整体约快 30%；每次导航从注入数百条 CSS 规则降为 0 条。
- 🧩 最终最大价值不是性能：样式边界变得清晰，组件拥有明确样式契约与确定性优先级，许多过去依赖约定或级联的写法现在由工具强制约束；这套体系也更适合越来越依赖 AI 代理编写的现代代码库。

---

### [](https://www.youtube.com/watch?v=NIG9GbVU5po)

**原文标题**: [Why is everyone moving to Stylex? - YouTube](https://www.youtube.com/watch?v=NIG9GbVU5po)

overview summary
- 📄 涵蓋 YouTube 基本資訊與服務條款連結，包括版權、聯絡方式與政策規範。
- 📰 提供新聞中心與開發人員入口，供媒體及技術人員獲取資源。
- 🎬 針對創作者與廣告刊登者，說明合作與內容推廣管道。
- 🛡️ 詳列私隱、安全及平台運作機制，強化使用者信任與透明度。
- 🧪 開放測試新功能，展示持續優化服務的承諾。
- ⚖️ 標註 © 2026 Google LLC，明確版權歸屬與法律依據。

---

### [如何评估会话重放软件：开发者指南 | Sentry博客](https://blog.sentry.io/evaluate-session-replay-software/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=replay-fy27q3-evergreen&utm_content=newsletter-primary-blog-replay-guide-learnmore)

**原文标题**: [How to evaluate session replay software: a developer's guide | Sentry Blog](https://blog.sentry.io/evaluate-session-replay-software/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=replay-fy27q3-evergreen&utm_content=newsletter-primary-blog-replay-guide-learnmore)

本文为开发者评估会话重放（Session Replay）工具提供了实用指南，核心聚焦架构层面的关键差异：数据捕获方式、隐私屏蔽位置、与可观测性平台的集成深度、性能开销与采样策略、AI代理可读性、移动端支持成熟度等。文章强调应根据团队实际场景（用户体验分析或工程调试）选择匹配的工具，并提供了具体的评估检查表。

- 📊 先分清工具定位：UX分析工具适合产品团队，调试工具适合工程团队；热力图再漂亮，弱错误集成也无助于排查生产事故。
- 🧬 录制方法决定能力边界：DOM快照+变更记录体积小、易脱敏、可结构化分析；像素捕获更还原复杂CSS与canvas，但只能生成视频帧。
- 🔒 隐私设计看屏蔽位置与默认策略：客户端屏蔽优于服务端处理（数据不出浏览器）；“默认全屏蔽、显式放行”比“默认全记录”更安全，且需关注欧盟数据驻留支持。
- 🔗 集成深度是调试场景的胜负手：独立工具需靠时间戳切换查找回放；原生集成（如Sentry）可从错误直达回放、关联后端trace，无需手工关联。
- ⚡ 性能开销要自测而非看厂商演示：随机采样+错误采样+关键路径全录，能以最小成本覆盖高频调试价值。
- 🤖 AI可读性依赖结构化和数据：DOM事件流可供AI代理分析异常序列与根因；像素视频无法被解析。需确认工具是否提供结构化导出API。
- 📱 移动端支持需验“真伪”：确认是否有原生iOS/Android SDK、移动端遮蔽成熟度、与后端错误联动能力，并查看真实生产环境回放样例。
- ✅ 决策参考：若以调试为主，优先选择与现有可观测平台原生集成、默认屏蔽、可自动关联错误的工具；若以UX研究为主，专用分析工具更合适。

---

### [](https://nextjs.org/blog/turbopack-chunking)

**原文标题**: [How Turbopack chunks your JavaScript | Next.js](https://nextjs.org/blog/turbopack-chunking)

Turbopack 在 Next.js 中通过权衡请求数量与下载体积来切分 JavaScript 代码；文章介绍了不同分块策略的利弊，并详细说明了 Next.js 16.3 推出的运行时按需加载、基于真实站点的分块配置以及减少代码体积等新特性。

- 🧩 分块核心挑战：在“更少请求”和“更少代码下载”之间做取舍，不可能同时最优。
- 📦 三种基础策略对比：单一大 chunk 缓存友好但首屏过度加载；每页一 chunk 不冗余但共享代码会重复下载；每模块一 chunk 几乎没有冗余但会产生数百个网络请求。
- 🔗 引入 chunk group 概念：同组 chunk 总会一起加载，因此只在组内合并，避免跨页面额外下载无用代码。
- ⚖️ 合并代价需用访问场景评估：例如合并 A、B 两个 chunk 后，若用户从需要 A+B 的页面跳到只含 A 的页面，就会重复下载 A；算法会按单页/多页访问概率给不同结果加权。
- 📊 nextjs.org 实测：不合并请求多、全组合并会多传约 10% 代码；默认设置削减了约 60% 请求，同时下载体积略降，是较平衡选择。
- 🆕 generateComponentChunks：构建时同时生成合并版和未合并版，运行时根据浏览器已有缓存动态选用合并 chunk 或缺失片段，优化软导航体验。
- 🧭 only-if-cached 实验：帮助回访用户根据本地缓存决定加载方式，进一步减少重复请求。
- 📈 Analytics 分块配置：通过 firstPageLoadPriority、priorityRoutes、clusters 等参数，让分块策略适配真实用户路径与重要页面。
- ✂️ 降低传输量：新增 CJS 模块 tree-shaking、改进 barrel 文件动态导入分析，并拆分共享 runtime，减少约 10KB 后续导航体积。
- ⚙️ 默认 runtime 更轻量：默认不再包含 WebAssembly 和 Web Worker 代码，只在用户实际使用这些模块时再动态插入加载代码。
- ✅ 这些实验性能力均可通过 next.config.js 在 Next.js 16.3+ 中开启试用，部分功能将在未来版本默认启用。

---

### [](https://vitest.dev/blog/vitest-5.html)

**原文标题**: [Vitest 5.0 is out! | Vitest](https://vitest.dev/blog/vitest-5.html)

Vitest 5 正式发布，以性能优化为核心，同时带来 Trace View、嵌套项目、vi.when API、基准测试重写、更严格断言等多项新功能与改进。该版本要求 Vite ≥ 6.4.0 和 Node.js ≥ 22.12.0，并包含若干破坏性变更。

- 🚀 性能大幅提升：通过新基准测试框架优化，vm pools、Browser Mode 及大型隔离测试套件提速最明显，部分场景提升超 50%
- ⚙️ 基础性能改进：内联项目共享 Vite 服务器、稳定的文件系统模块缓存、减少主进程与 worker 间通信、加速 vm pools、预打包依赖以缩小安装体积
- 🔍 新增 Trace View：Browser Mode 可记录每一步交互/断言/快照，支持在浏览器 UI、Vitest UI 和 HTML 报告中逐步回放，便于本地调试和 CI 失败分析
- 📂 嵌套项目与配置继承：内联项目默认继承根配置，支持引用自带子项目的配置文件，--project/-p 支持层级过滤
- 🎯 新增 vi.when API：可按参数深度匹配及非对称匹配器定义 spy 行为，并支持 thenReturnOnce/次数限制及 toHaveBeenExhausted 断言
- ⏱️ 基准测试重写：bench 改为测试上下文内可用，支持比较、断言、持久化结果、自定义提供者，且输出集成到默认/json 报告器
- ♿ Locator 错误显示 ARIA 树：更易定位元素问题，locators 默认严格模式，避免意外误匹配
- 🕐 Mocking 支持 Temporal：假计时器和 setSystemTime 可模拟 Temporal API，也可通过 toNotFake 排除
- 🔒 断言更严格：未 await 的异步断言直接失败；expect.poll 支持超时拒绝及 AbortSignal；扩展 Matchers 类型更完善
- 🧹 clearMocks 默认开启：每个测试前自动清空 mock 调用记录，减少顺序相关测试问题
- 📝 报告器更新：统一输出至 .vitest 目录，第三方报告器可用 createReport API，HTML 报告支持 singleFile 单文件导出
- 🛠️ 其他改进：新增 --repeats 选项、可配置 CJS 全局变量注入、扩展覆盖率选项（子进程/阈值）、json/junit 报告器新选项、更美观的测试标题格式等
- ⚠️ 破坏性变更：需升级至 Vite ≥ 6.4.0、Node.js ≥ 22.12.0，升级前请阅读迁移指南

---

### [迁移指南 | 指南 | Vitest](https://vitest.dev/guide/migration/)

**原文标题**: [Migration Guide | Guide | Vitest](https://vitest.dev/guide/migration/)

Vitest 5.0 的迁移指南，介绍了从环境要求、Mock 行为、项目配置、浏览器测试、覆盖率、报告输出，到包结构和已移除 API 的主要破坏性变更与应对方式。

- ⚙️ 环境要求提升：Vitest 5.0 需要 Vite ≥ 6.4.0 和 Node.js ≥ 22.12.0，旧版本不受支持。
- 🧹 `clearMocks` 默认开启：每个测试前会调用 `vi.clearAllMocks()` 清空 mock 调用记录，但保留实现；如要保留旧行为，可设 `clearMocks: false`。
- 🔍 `testNamePattern`（`-t`）现在匹配以 `" > "` 连接套件名和测试名的完整名称，而非空格连接；需改用 `"math > adds"` 或通配符。
- 🧩 内联项目默认继承根配置：`test.projects` 中的内联项目默认 `extends: true`，继承插件、别名等 Vite 配置和根级 test 选项；数组选项会合并而不是覆盖，可用 `extends: false` 关闭。
- 📂 被引用的配置文件现在可以声明自己的 `projects` 并作为嵌套项目运行；注意避免因合并根配置而意外带入 `projects` 字段。
- 🔄 内联项目默认共享 Vite 服务器：通过 `sharedViteServer` 控制；共享后声明文件只执行一次，插件 `config` 钩子不会为每个项目重跑。
- 🚨 `vi.mock`、`vi.unmock`、`vi.hoisted` 必须在模块顶层调用；写在函数、代码块或 `describe`/`test` 回调中现在会直接抛出错误。
- 🤖 浏览器模式中自动 mock 的模块不再调用真实实现，导出默认返回 `undefined`；需要保留原行为时可传 `{ spy: true }` 或提供 factory。
- 🐕 类 mock 的 `prototype` 会链接到原实现类的原型，因此实例保留类方法，`instanceof` 判断也更符合预期。
- 📊 基准测试 API 重写：`bench` 不再是顶层导入，需从 `test()` 上下文获取；`bench.skip/only/todo`、旧 report 配置和 `--compare` 等均移除。
- 🔑 Vitest UI 现在需要带 token 的 URL 进行认证，不再允许直接访问裸 `/__vitest__/` 地址。
- 🕒 假定时器和 `setSystemTime` 会同时 mock `Temporal` API；如果不想 mock，可把它加入 `fakeTimers.toNotFake`。
- ⛔ `toThrow("")` 语义改变：空字符串作为子串现在可匹配任何非空错误消息；要断言空消息请使用 `/^$/`。
- 🔤 断言类型改为 `Matchers<R, T>` 双参数形式：同步断言返回 `void`，`.resolves`、`.rejects`、`expect.poll` 等返回 `Promise<void>`；不再读取全局 `jest.Matchers`。
- ⏱️ `expect.poll` 超时后会失败，且回调会收到用于取消正在执行任务的 `AbortSignal`。
- ⚠️ 未 await 的异步断言（如 `.resolves`、`.rejects`、`toMatchFileSnapshot`）现在会直接导致测试失败，不再自动等待。
- 🎨 值格式化改用 `pretty-format` 替代 `loupe`；`test.each`/`test.for` 标题中的字符串不再带引号，截断长度由 `taskTitleValueFormatTruncate` 控制。
- 🚮 移除 `test.sequential`、`describe.sequential` 和 `sequential` 选项，改用 `concurrent: false`。
- 🖱️ 浏览器命令的 locator 参数现在序列化为 `SerializedLocator` 对象，需从中解构 `selector`；浏览器 locator 默认按精确文本匹配，可用 `browser.locators.exact: false` 关闭。
- 📝 `toHaveTextContent` 改为严格相等匹配，不再支持正则和部分匹配；部分匹配或正则请改用新的 `toMatchTextContent`。
- 🔧 `vitest-browser-vue` 和 `vitest-browser-svelte` 的 `render` 变为异步，调用前需要 `await`。
- 📈 覆盖率 glob 阈值的 `perFile` 不再从顶层自动继承，需在每个 glob 上显式设置；`coverage.include`/`exclude` 的匹配方式也更严格，使用相对项目根路径且无 `contains` 语义。
- 📁 不再从父目录向上查找配置文件；从子目录运行时需显式用 `--config` 指定。
- 🌐 jsdom/happy-dom 中对 `globalThis` 或 `window` 的属性赋值现在会同步到底层 DOM 实现；`populateGlobal` 返回的 `originals` 改为属性描述符，恢复时需用 `Object.defineProperty`。
- 🔐 浏览器 orchestrator URL 需要包含 `sessionId`，不能使用裸 `/__vitest_test__/`。
- 🌍 `browser.api` 被顶层 `api` 选项取代，`browser.isolate` 也改为顶层 `isolate`。
- 🗂️ 报告和产物默认输出到项目根的 `.vitest` 目录；JSON 和 JUnit reporter 默认写入文件而非 stdout，如需 stdout 可配置 `reporters: [['json', { stdout: true }]]`。
- 🖼️ `toMatchScreenshot` 现在使用独立的 `browser.expect.toMatchScreenshot.screenshotDirectory` 配置，默认 `__screenshots__`。
- 🔢 Worker 和并发 ID 从 1 开始编号，`VITEST_POOL_ID`、`VITEST_WORKER_ID` 的范围也随之变化。
- 🛠️ `resolveConfig` 现在直接返回已解析的 Vite config，Vitest 完整配置在其 `test` 属性上，不再返回 `{ vitestConfig, viteConfig }`。
- 📦 包迁移：`@vitest/runner` 和 `@vitest/ws-client` 弃用；`vitest` 不再依赖 `@vitest/expect`；WebdriverIO provider 移至 `vitest-community` 组织。
- 🧹 已彻底移除多个弃用入口，如 `vitest/coverage`、`vitest/reporters`、`vitest/environments`、`vitest/snapshot`、`vitest/suite`、`vitest/mocker` 等。

---

### [](https://x.com/tan_stack/status/2094888852607652280)

**原文标题**: [TANSTACK on X: "🏝️ + ▲ = 🚀

TanStack and @Vercel are officially teaming up!

We’re working together to make Vercel a first-class home for TanStack Start with better support for deploying and running anything you can dream up with TanStack on Vercel.

Start here! 👇

https://t.co/cKNJ6z70gr" / X](https://x.com/tan_stack/status/2094888852607652280)

TanStack 与 Vercel 正式宣布合作，旨在将 Vercel 打造成 TanStack Start 的一流部署与运行平台，全面优化相关支持与服务，让开发者能更轻松地在 Vercel 上部署各种基于 TanStack 构建的应用。
- 🤝 官宣联手：TanStack 与 Vercel 正式达成官方合作
- 🎯 平台升级：Vercel 将成为 TanStack Start 的一流承载平台
- 🚀 能力增强：提升部署与运行支持，助力更多创意落地
- 📘 快速启动：附有专属指南，方便开发者立即上手参考

---

### [如何将TanStack Start应用部署到Vercel | Vercel知识库](https://vercel.com/kb/guide/deploy-a-tanstack-start-app-to-vercel)

**原文标题**: [How to Deploy a TanStack Start app to Vercel | Vercel Knowledge Base](https://vercel.com/kb/guide/deploy-a-tanstack-start-app-to-vercel)

使用 Nitro Vite 插件即可将 TanStack Start 应用部署到 Vercel：Vercel 会自动检测 TanStack Start 与 Nitro，配置好插件后可直接通过 Git 或 CLI 部署，默认运行在 Fluid compute 上，并涵盖环境变量设置、部署验证与故障排查要点。

- ⚛️ TanStack Start 是基于 TanStack Router 的全栈框架，支持 SSR、流式渲染与服务端函数，通过 Nitro 编译为 Vercel Functions。
- 🔍 Vercel 提供零配置检测，可自动识别 TanStack Start 和 Nitro，无需手动指定构建命令或输出目录。
- ✅ 准备前提：Vercel 账号、Vercel CLI、Node.js 24+、包管理器、TanStack Start 项目以及 Git 仓库。
- 📦 在项目根目录安装 `nitro`；若通过 Vercel 模板创建，通常已预装，可跳过。
- 🧩 在 `vite.config.ts` 的 `plugins` 数组中加入 `nitro()`，与 `tanstackStart()` 及 React/Solid 插件并存。
- 🔐 环境变量要注意：不带 `VITE_` 前缀的变量仅供服务端使用；带 `VITE_` 前缀会进入客户端，绝不能存放秘密值。
- 🛠️ 可用 `vercel env add` 添加环境变量，用 `vercel env pull` 同步到本地；变量修改后需重新部署才生效。
- 🌿 Git 部署：将仓库导入 Vercel，确认框架预设为 TanStack Start 后点击 Deploy，后续 push 到 main 会自动触发生产部署。
- 💻 CLI 部署：运行 `vercel` 创建预览部署，也可用 `vercel --prod` 直接部署生产或用 `vercel promote` 提升现有部署。
- 🔎 部署后验证：确保页面 SSR 内容可显示、路由切换正常、服务端函数返回正确；出现 404 通常需检查 `nitro()` 是否配置正确。
- 🛠️ 若框架未自动检测（如 monorepo），可通过 Vercel 仪表盘、`vercel.json` 设置 `"framework": "tanstack-start"`，或使用 CLI 更新项目。
- ⚡ 默认使用 Fluid compute，按活跃 CPU 时间计费，可随流量自动扩缩，减少冷启动和空闲成本。
- 📚 更多信息可参考 TanStack Start on Vercel 官方文档、Vercel Functions、Fluid compute 及相关 FAQ。

---

### [](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/75429)

**原文标题**: [[react] 19.3 by eps1lon · Pull Request #75429 · DefinitelyTyped/DefinitelyTyped · GitHub](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/75429)

该拉取请求旨在为 React 19.3 版本更新类型定义，将原本仅存在于 canary 通道的类型提升为稳定类型，并同步调整相关测试与包版本。

- 🔄 将 React 19.3 中从 canary 转为稳定的类型移到主入口，例如 `react-dom` 的 `browser()` 函数及 `BrowserUsable` 返回类型。
- ⚛️ 将 `<ViewTransition>` 组件、`ViewTransitionProps/Instance/Class`、`addTransitionType`、`FragmentProps` 的 `ref` 属性及 `SubmitEvent.submitter` 等类型声明从 canary 移至稳定入口。
- 📦 保留 `react/canary` 与 `react-dom/canary` 入口以确保旧引用可用，其中 `react-dom/canary` 被清空为外壳；`unstable_useCacheRefresh` 仍留在 canary。
- 🧪 将相关测试从 canary 测试文件移到稳定测试文件，并修复一条过时的注释，改为真实的 `$ExpectType` 断言。
- 🔢 为匹配 React 19.3 预发布版本，将 `@types/react`、`@types/react-dom`、`@types/react-is`、`@types/react-test-renderer` 等包版本提升至 19.3.9999，`@types/scheduler` 至 0.28.9999 等，同时提高 `@types/react-dom` 对 `@types/react` 的 peer dependency 下限至 `^19.3.0`。
- 🧹 更新 `react-refresh` 类型：移除运行时已删除的 `findAffectedHostInstances` 及其 `Instance` 类型，新增导出的 `_getMountedRootCount`。

---

### [](https://margelo.com/blog/margelo-joins-callstack)

**原文标题**: [Margelo Joins Callstack to Advance High-Performance React Native Engineering - Margelo](https://margelo.com/blog/margelo-joins-callstack)

Margelo 宣布加入 Callstack，交易估值超 2000 万欧元，双方将整合高性能 React Native 工程能力与企业级交付经验。

- 💰 交易估值超过 2000 万欧元，Margelo 正式加入 Callstack。
- 🔗 结合 Margelo 的性能优先 React Native 技术与 Callstack 的企业级交付经验。
- ⚙️ 代表项目包括 Nitro Modules、VisionCamera 和 react-native-mmkv。
- 🏢 客户将同时受益于 Margelo 的前沿技术与 Callstack 十年规模化服务经验。
- 🚀 在 AI 加速开发的背景下，更聚焦架构、性能、原生集成、验证与发布安全。
- 🌍 现有开源库将继续保持开源，Marc Rousavy 仍主导相关开发。

---

### [](https://maxleiter.com/blog/thank-u-next)

**原文标题**: [thank u, next | Max Leiter](https://maxleiter.com/blog/thank-u-next)

这篇文章记录了作者将自己的个人网站从 Next.js 迁移到一个由 AI 按需“vibe-coding”出来的定制框架的完整过程：由 Claude 模型（Fable 负责架构、Opus 负责实现）在约 3 小时内完成可运行的初版。新框架大幅降低了页面体积和 JavaScript 加载量，显著提升性能，同时引发了关于 AI 对软件框架未来影响的思考。

- ✨ 作者用 AI 为自己网站打造了“专属框架”：Fable 设计架构、Opus 负责实现，替代 Next.js 并部署在 Vercel 上。
- 📉 性能提升显著：首页 HTML 减少 34%，博客页减少 44%；JavaScript 从约 200KB 降至 2.3KB，减少约 99%。
- ⚡ Lighthouse 移动端评分从 98/99 提升至 100，LCP 缩短约一半，页面总重量降低 86%–93%。
- 🧱 新框架本质上只是一个构建脚本：用 React 在服务端渲染所有路由，输出 Vercel Build Output；MDX 和 Shiki 代码高亮也在构建期完成。
- 🧩 交互采用 Preact “岛屿”架构：桌面窗口管理器、命令面板等按需水合加载，普通内容页几乎零 JavaScript，仅内联约 2KB 脚本。
- 📦 依赖从 706 个减至 550 个；本地完整构建从 2.4s 缩短到 0.5s，Vercel 构建从 28s 缩短到 11s。
- 🤖 AI 编写了“同构测试工具”，对 101 条路由的新旧站点做自动对比，发现并修复了 8 篇未发布文章泄露到 RSS、OG 图片 404 等问题。
- 🎯 动机包括：降低供应链攻击风险、只保留真正需要的依赖；约 5000 行的框架比 Next.js/React 数十万行更容易被人和 AI 审查。
- ⚠️ 代价明显：缺少 Next.js 内建的大量隐式优化和上游安全更新；自己承担维护责任；还遇到 Chrome 与 WebKit 两个浏览器兼容怪癖。
- 🔮 作者认为这种 Agent 驱动的“自主重写/内部化”会越来越多，并预言传统框架可能走向消亡，框架内积累的知识会被蒸馏成可复用的“技能”或新标准。
- 💰 实验投入约 $669，代码变更含 20914 行新增、2022 行删除；约占其 Claude Code 订阅额度的 10%。

---

### [](https://www.robinwieruch.de/agentic-coding-bet-on-primitives/)

**原文标题**: [Agentic Coding: Bet on the Primitives - Robin Wieruch](https://www.robinwieruch.de/agentic-coding-bet-on-primitives/)

本文探讨了Agentic Coding如何改变开发者对高层库与底层原语的选择逻辑。作者通过一个定制图表实验发现：当AI让实现成本暴跌后，“原语+自有薄层”往往比直接采用高层库更划算，并分析了这种转变背后的经济学本质与适用边界。

- 🧪 实验对比：用D3数学原语+React自研图表，完美匹配设计系统；而Recharts版本最后20%仍需自写SVG，且动画在项目中冻结。
- ⚙️ 抽象的本质：高层库是编码好的预付实现劳动，用灵活性换取速度；需求一旦偏离其“快乐路径”，就会在样式、行为和配置上持续付出代价。
- 📜 二十年的抽象堆叠：从jQuery、框架、组件库、ORM到meta-framework，每一步都因“人力便宜、抽象贵”而被合理化。
- ↩️ 反向信号早已出现：Bootstrap转向Tailwind、shadcn/ui直接复制源码，都是团队重新追求拥有权的先兆。
- 🤖 Agentic coding让实现成本坍塌，使“拥有并维护自己的薄层”第一次变得经济可行，理性选择因此向原语回归。
- 🧱 关键澄清：这不是回到手写一切，而是从“租用框架的观点”转向“拥有一层自写代码”；原语+定制薄层成为新平衡点。
- 🔍 核心区别：原语（如d3-scale）只负责计算、不做决策；框架（如Recharts）替你拥有渲染、动画和交互，一旦需求越界就要“谈判”。
- 📦 原语不等于零依赖：d3-scale、date-fns、zod等解决硬问题的依赖仍应保留；真正要自拥有的是承载产品身份的渲染与交互层。
- ✅ 高层库依然胜出的场景：团队还没有成熟的agentic工作流、UI完全商品化、或涉及无障碍、键盘交互等需要长期成熟测试的领域。
- 🎯 结论：Agentic coding没有改变“贴近快乐路径时用库更划算”的启发式，只是把交叉点强烈推向“原语+薄层”一侧。
- 💡 未来最有价值的代码层，可能不是安装来的框架，而是团队基于原语写出的那几百行“自己的层”——因为现在终于承担得起拥有它了。

---

### [](https://shopify.engineering/mobile-e2e-testing)

**原文标题**: [How we raised mobile end-to-end test stability to 98% (2026) - Shopify](https://shopify.engineering/mobile-e2e-testing)

Shopify移动团队通过重建端到端测试框架，用严格API与计算机视觉取代了松散的旧方案，将测试稳定性从约50%提升到98%，使E2E套件重新成为可靠的CI质量门槛。

- 📱 Shopify最大的移动应用E2E测试曾因脆弱而阻挡了大量正常PR，最终被迫从PR检查中撤下。
- 🔍 旧框架基于Appium、WebdriverIO和Test ID，过度灵活且缺少规范，容易产生“元素未找到”以及固定pause导致的flaky问题。
- 🚫 旧测试即使通过，也常常只是验证组件树节点存在，而非真实可见性与可用性；例如被底部inset遮挡的单元格仍能被点击并错误通过。
- 🧱 团队没有修补Appium本身，而是构建了一个有主见的封装层：底层继续由Appium驱动，但开发者无法绕过上层约束。
- ✅ 新API强制“每步都必须携带断言”，点击、等待或输入前必须声明屏幕预期状态，错误会在发生的那一步立即暴露。
- 👁️ 采用计算机视觉定位元素：PaddleOCR识别文字，OpenCV匹配Polaris SVG图标，像真实用户一样“看屏幕”操作；Test ID仅作为后备，且需显式使用UNSAFE_testID。
- ✍️ 视觉定位大幅提高编写效率：直接写 `touch({ text: 'Save' })` 即可完成交互；对AI agent而言，屏幕文本与API语法一一对应，首次生成正确测试的概率更高。
- 🎥 每次测试运行都会生成标注视频，展示每一步在寻找什么、实际点击了哪里，失败时能快速自诊断，无需重复运行。
- 📟 统一CLI可通过同一命令在本地模拟器、CI模拟器或远程真机农场运行相同测试，保证各环境一致性。
- 📈 迁移后测试稳定性达到98%，剩余失败主要来自偶发网络问题和模拟器启动故障；同时新增预晋升flakiness门禁，新测试需多次稳定通过才能进入阻塞套件。
- 🧠 结论是E2E测试的不稳定很大程度源于API设计而非测试本身；坚持“每步断言、像用户那样查找元素、移除易错项”可让套件长期可信。
- 💡 给团队的实践建议：限制API命令集（deeplink、滑动、输入、点击、断言、重启应用），使用计算机视觉交互，要求每个动作带断言或反证，并在合入前验证测试稳定性。

---

### [](https://alfy.blog/2026/07/25/modern-web-guidance.html)

**原文标题**: [Testing Google's "modern-web-guidance" skill against a real React app](https://alfy.blog/2026/07/25/modern-web-guidance.html)

这份评测将 Chrome 的 `modern-web-guidance` 技能当作审计工具，用于一个真实的 React 表单应用中。结果显示：它并非自动修复工具，而是一套能提供“当前最佳实践”、“Baseline 浏览器支持”及具体代码模式的高质量指南索引；它能有效纠正 LLM 或开发者常见的“过时三年前”的前端写法，但仍需要人或 Agent 主动读取代码、发起检索并判断是否适用。

- 🧭 背景问题：LLM 常常生成 2021 年风格的前端代码，如滥用 `100vh`、手写暗色模式、禁用提交按钮等；`modern-web-guidance` 正是为此设计的检索型技能，而非 linter 或代码生成器。
- 🔬 测试方法：作者用自建的 Vite + React 18 “问卷评估”应用（42 个源文件，表单密集、无图片）作为审计对象，通过 `npx modern-web-guidance search/retrieve` 检查问题并对照实际代码。
- 🌙 发现 1——暗色模式：应用完全没有 `color-scheme`，只需在 `<head>` 加 `<meta name="color-scheme" content="light dark">`，在 `:root` 声明 `color-scheme: light dark`，再用 `light-dark(#light, #dark)` 定义颜色 token，即可修复原生控件、滚动条和首屏白闪。
- 🎛️ 暗色模式的 UX 建议：指南明确指出不要做“系统/浅色/深色”三态切换，因为总有两个选项结果相同；应做成“跟随系统”和“跟随系统的相反状态”两态，并处理用户固定深色后系统切深色时不应翻转的边界情况。
- 📅 Baseline 纪律：`color-scheme` 自 2022 年起已是 Baseline Widely available，可直接使用；`light-dark()` 是 2024 年新特性，需用 `@media (prefers-color-scheme: dark)` 和 `@supports` 逐级降级，并提供内联脚本防止主题闪烁。
- 📝 发现 2——表单不是真表单：应用里全是 `<div>` + `<button type="button" onClick>`，没有 `<form>`，导致回车无法提交；应包裹为 `<form onSubmit>` 并使用 `type="submit"`，配合 `e.preventDefault()` 继续走前端逻辑。
- ✅ 指南也公平：它认可“提交后禁用按钮防止重复提交”是正确做法；真正该避免的是“一开始就禁用按钮来阻止不完整表单”。
- ⏱️ 发现 3——验证时机：指南推荐“blur 时校验，input 时清除错误，submit 时拦截”，而不是用户输入一个字符就马上报错；现代平台可通过 `:user-valid` / `:user-invalid` 免费实现，优于手写 `onChange` 提示逻辑。
- ⌨️ 发现 4——输入属性不完全适用：该应用几乎全是 radio，`autocomplete`、`inputmode`、`enterkeyhint` 大多无用武之地；但指南中“文本输入 `font-size: 1rem` 或更大，否则 iOS Safari 聚焦时自动缩放”这一条仍然通用。
- 📱 发现 5——`100vh` 问题：移动端浏览器会因 URL 栏展开/收起导致 `100vh` 超高，应改用 `100dvh`；但本次语义搜索没有直接返回专门的 “dvh” 结果，只能去大而全的 CSS 指南里寻找。
- 💪 主要优点：指南内容质量高，区分强制项与可选项，包含真实产品判断；能针对较新特性提供 Baseline 对应的精确 fallback；框架无关，易于迁移到 React；本地运行、无 API 密钥、无额外依赖、可离线使用。
- ⚠️ 主要局限：它不读你的代码，需要人工或 Agent 把模式转化搜索词并对比代码；语义搜索存在召回上限，可能只给出宽泛指南；指南本身的 token 量不小（例如 `forms` 约 4500、`accessibility` 约 7100），会明显占用上下文窗口。
- 🔑 总结定位：它不能抓 bug，也不会替你重写组件；最好的用法是在“写组件之前”咨询，而不是等到代码完成后做清理——它能低成本拦截那些“自信但过时”的默认模式。

---

### [版本 v9.6.0 | Mantine](https://mantine.dev/changelog/9-6-0/)

**原文标题**: [Version v9.6.0 | Mantine](https://mantine.dev/changelog/9-6-0/)

overview summary
- 🎉 Mantine v9.6.0 于 2026 年 9 月 1 日发布，带来全新 Lightbox 组件、多个图表组件、通知系统增强及编辑器、调度视图等多项关键升级。
- 🖼️ 新增 `@mantine/lightbox` 包：支持图片/视频/自定义幻灯片的全屏灯箱，具备缩放、缩略图、过渡动画、键盘快捷键及基于 Store 的 API。
- 🔔 Notifications 新增 `renderNotification` 属性支持完全自定义内容，并保留所有动画效果；另新增 `layout="stacked"` 堆叠布局模式。
- 🛠️ 新增 `ActionBar` 组件：用于批量选择操作的固定底部工具栏，可与表格/复选框联动并包含关闭按钮。
- 📝 RichTextEditor 新增表格编辑控件（插入、增删行列、合并/拆分单元格）、可折叠 Details 折叠区块控件，以及显示空格和段落标记的 InvisibleCharacters 隐形字符开关。
- 📊 Charts 新增 4 个图表组件：用于 KPI 的 `GaugeChart` 径向仪表图、`WaffleChart` 网格占比图、`MatrixChart` 热力图和 `CandlestickChart` 金融蜡烛图。
- 📈 现有图表（Area/Bar/Line/Composite/Scatter）新增 `referenceAreas` 区域高亮和 `referenceDots` 点标记功能；AreaChart 新增 `type="stream"` 流图支持，参考线渲染层级也调整至系列之上。
- 📅 调度组件持续增强：`Stepper` 支持 `labelPosition`；`Cascader` 悬停时支持安全区域多边形；`YearView` 支持 `renderDay` 与 `withWeekendDays`；时间网格视图支持事件拖拽/缩放的独立时间间隔设置。
- 🧩 其他改进包括：Dropzone 升级至 react-dropzone 20（需 Node.js 22，批量文件接受逻辑变化）、ColorInput 全宽模式、FloatingWindow 大小变化回调、PasswordInput 可聚焦切换按钮、可交互背景事件及 use-scroll-spy 对 ref 对象支持。

---

### [GitHub - shadcn-ui/cn：cn 是用于 Tailwind 类合并和冲突解析的新引擎。它取代了 tailwind-merge 和 clsx。相同的 API。完全一致。而且速度快 30 倍。· GitHub](https://github.com/shadcn-ui/cn)

**原文标题**: [GitHub - shadcn-ui/cn: cn is a new engine for Tailwind class merging and conflict resolution. It replaces tailwind-merge and clsx. Same APIs. Full parity. And it is 30× faster. · GitHub](https://github.com/shadcn-ui/cn)

cn 是一个为 Tailwind CSS 类合并与冲突解决而生的新引擎，用于直接替代 `tailwind-merge` 和 `clsx`。它提供相同的 API 与完全兼容的输出，同时通过缓存和编译优化实现极高性能提升（官方宣称快 30 倍以上）；零依赖、框架无关，并可在各类现代 JS 运行时中运行，还附带 CLI 迁移工具和灵活的扩展配置接口。

- ⚡ 速度提升：cn 比“clsx + tailwind-merge”典型场景快约 30 倍，在 58 个真实开源仓库的 14 万多次调用测试中，几何平均快 37 倍。
- 🔁 直接替代：API 与 `clsx`、`tailwind-merge` 一一对应，输出经过 356,000 次差分测试验证与 tailwind-merge 完全一致。
- 📦 零依赖与通用性：无依赖、框架无关，支持 React、Vue、Svelte、Solid、Astro 等，也能运行在浏览器、Node、Bun、Deno 及边缘运行时。
- 🚀 快速上手：通过 `npm i cn` 安装并直接导入 `{ cn }` 使用；现有 shadcn/ui 项目可通过 `npx shadcn@latest migrate cn` 自动迁移。
- 🗜️ 轻量体积：minified 后仅 26 KB，比常见组合更小；还可用 `cn build` 进一步压缩产物。
- 🎨 自定义主题：`cn/config` 支持与 `extendTailwindMerge` 相同的 `{ extend, override, prefix }` 配置，可扩展 class groups、校验器并兼容 Tailwind v4 前缀。
- 🧩 丰富 API：核心提供 `cn`、`twMerge`、`twJoin`、`clsx`；另有 `cn/engine`、`cn/lite` 以及 CLI `npx cn build` 满足不同场景。
- ⚠️ 注意事项：Tailwind v3 项目应继续使用 tailwind-merge v2；`cn build` 无法识别动态拼接类名；CLI 需要 Node 20+。
- 🤝 致谢与兼容：合并语义遵循 tailwind-merge，clsx 兼容层遵循 clsx，参数身份缓存优化参考 cnfast，并感谢三位作者。

---

### [](https://github.com/shadcn-ui/cn/blob/main/docs/how-it-works.md)

**原文标题**: [cn/docs/how-it-works.md at main · shadcn-ui/cn · GitHub](https://github.com/shadcn-ui/cn/blob/main/docs/how-it-works.md)

概述：本文介绍 `cn` 的工作原理，它通过编译期预生成查找表，替代 tailwind-merge 的运行时期配置解释，从而大幅提升速度，同时保持输出完全兼容并支持按项目裁剪。

- ⚙️ 核心机制：`tailwind-merge` 在运行时解释约 380 个类组的配置对象，而 `cn` 在编译期将同一配置编译为扁平查找表，运行时只做一次遍历，避免逐类拆分、正则和内存分配。
- 🚀 性能优势：若合并结果无变化则直接返回原始字符串；不产生子串、不跑正则、每个类零分配，启动时间仅约 0.4 毫秒（对比 tailwind-merge 的 3.2 毫秒）。
- 🧠 三层缓存：参数缓存（指针比较相同字符串实例并学习调用序列，预测命中约 10 纳秒）；整字符串缓存（需重复出现两次才缓存，避免污染 SSR 一次性字符串）；令牌记忆（让新字符串中的重复类也保持低成本）。
- 📦 项目定制：`cn build` 会根据项目实际用到的类重新生成表并丢弃未用组，安全且不改变合并结果；未知类直接透传，与 Tailwind 内容扫描契约一致。
- ✅ 完全兼容：与 tailwind-merge 对每个输入输出一致，CI 强制验证 56,346 个差分用例、300,000 个语法模糊类字符串、5,054 个自定义配置用例等。
- 📏 体积权衡：默认入口约 10.5 KB min+gzip（表 5.4 KB + 引擎 5.1 KB），对比 clsx + tailwind-merge 的 8.6 KB 多约 1.9 KB，但解析量略少；可用 `cn build` 按项目裁剪以减小体积。
- 🧪 基准方法：每个实现与工作负载对在独立子进程运行，各自预热并取 5 次最优，避免共享进程带来的 GC 或 V8 分级污染；微基准存在数百分比波动，冷负载是合成最坏情况，真实渲染以缓存命中为主。

---

### [](https://gpuix.dev/)

**原文标题**: [React bindings for GPUI, Zed's GPU-accelerated UI framework — GPUIX](https://gpuix.dev/)

overview summary：GPUIX 是一个将 React 与 GPUI（Zed 的 GPU 加速 UI 框架）绑定的工具，允许用 React/TypeScript 构建原生 GPU 加速桌面应用，无需 Electron 或 WebView。核心特性包括从头搭建或基于示例启动、支持热重载、提供虚拟列表和原生文本组件、丰富的样式与事件系统，以及用于自动化测试与截图的内置 API。
- ⚡ 功能概述：GPUIX 是 Zed GPUI 框架的 React 绑定，组件通过 Metal/DirectX/Vulkan 直接渲染到 GPU。
- 🚀 快速开始：可通过 `bunx @gpuix/cli new my-app` 创建应用并运行 `bun run dev`。
- 📦 包结构：核心包为 `@gpuix/native`（Rust 绑定）、`@gpuix/react`（协调器与类型）以及 `@gpuix/cli`（脚手架）。
- 🛠️ 构建从零开始：需配置 TypeScript 指向 GPUIX JSX 类型，入口文件通过 `render()` 创建窗口并挂载 React。
- 🔥 热重载：使用 `bun --hot` 可在保存时重挂载 React 树，而无须重建窗口或 GPU 设备。
- 📜 架构：采用基于变更（mutation）的协议，React 批量发送原子变更至 Rust 端的 RetainedTree，每帧由 GPUI 渲染。
- 🧩 原生元素：支持 `<div>`、`<text>`、`<code>`、`<diff>`、`<markdown>`、`<input>`、`<textarea>`、`<img>`、`<svg>` 等。
- 📄 虚拟列表：`<virtual-list>` 仅构建/绘制可见行，支持底部对齐与跟随尾部等聊天场景特性。
- 🎨 样式系统：类似 CSS 但非 CSS，需注意 `display:flex` 显式声明、无简写、`boxShadow` 为对象等差异。
- 🖱️ 事件处理：支持鼠标、键盘、滚动、聚焦、变更等事件，并内置指针捕获机制。
- 🧪 自动化测试：提供 `testId`、定位器（getByTestId/getByText）、截图、虚拟时钟、真实窗口进程 launch 等，可驱动真实 GPU 渲染。
- ⚙️ 额外功能：含 macOS 菜单栏集成、背景启动（focus/show 控制）、帧调试叠加层、文本搜索与高亮、原生动效（motion.div）等。
- ⏱️ 性能设计：通过保留树、虚拟化、memo 与剪裁，避免重复全量布局与绘制。

---

### [](https://zed.dev/)

**原文标题**: [Zed — Your last next editor](https://zed.dev/)

overview summary
- 🚀 Delta 是一个专为编码智能体打造的多玩家协作环境，被称为“你的下一个编辑器”。
- ⚡ Zed 是一款以速度和协作为核心的极简代码编辑器，支持人类与 AI 无缝协作，并提供 macOS、Linux 和 Windows 版本。
- 🦀 Zed 使用 Rust 从零编写，能高效利用多核 CPU 和 GPU，带来极快的启动、交互与输入延迟表现。
- 🤖 支持并行运行多个编码智能体，让代理流畅地编辑文件、导航代码并以原生速度执行工具。
- 👥 支持与团队成员聊天、结对编程、共享屏幕和项目，实现深度协同。
- 📝 编辑器内可直接查看真实开发动态，包括修复缓冲区粘贴大文件时的崩溃、添加 Vim 环绕键操作、改进 LSP 悬停提示位置等。
- 🔍 开发团队正为 GPUI 添加 AccessKit 辅助功能支持，以便屏幕阅读器遍历元素树，并重构项目面板树对比逻辑。
- 💻 示例代码展示了一个“会议调度器” React 组件，其中包含大量刻意设计的类型错误和反模式，如变量拼写错误、类型不匹配、死代码等，用于演示编辑器的检查与提示能力。
- 🧩 Zed 提供 Parallel Agents、调试器、智能体编辑、原生 Git 支持、编辑预测（由 Zeta2 驱动）、远程开发、多缓冲区编辑及 Vim 友好等高级特性。
- 🗣️ 受到 José Valim、Ethan Perez、Dan Abramov、Mike Bostock 等知名开发者的高度评价，称赞其速度、设计精妙和强大功能。
- 🔌 拥有丰富的扩展生态，涵盖 HTML、Java、SQL、PHP、Vue、Ruby、C#、Lua、Terraform 等多种语言支持，以及主题和图标扩展。
- 🛠️ 内置语言服务器协议支持、大纲视图、文本操作、诊断多缓冲区、开发容器、CLI、彩虹括号、REPL、语法感知选择和内联提示等生产力工具。
- ✍️ 团队认为软件开发的未来在于人类与 AI 的流畅协作，Zed 正是为实现这一愿景而从头打造的产品。

---

### [](https://react-aria.adobe.com/releases/v1-21-0)

**原文标题**: [v1.21.0 | React Aria](https://react-aria.adobe.com/releases/v1-21-0)

v1.21.0 版本发布了全新 NavigationTree 组件、Menu 异步加载与空状态支持，以及 TokenField 选择范围 API 更新，并包含多项常规修复与依赖升级。

- 🌳 新增 NavigationTree 组件：支持层级链接、键盘导航与嵌套路由，适合侧边栏与复杂导航。
- 📂 Menu 大幅升级：新增 MenuLoadMoreItem 支持异步滚动加载，renderEmptyState 支持加载/空状态展示。
- 🎯 TokenField 选择逻辑更新：selectedRange 取代 caretPosition，记录完整选择范围，并支持撤销重做后恢复选区。
- 🔄 常规更新：重新导出 react-aria-components 类型、添加 setInteractionModality、优化 focus 处理，并升级至 TypeScript 7。
- 📅 Calendar 支持在设置 isDateUnavailable 时选择可见范围外日期。
- ✅ 多个输入类组件（Checkbox、RadioGroup、Switch）的 inputRef 类型支持回调 ref。
- ⌨️ 修复 Date and Time 中 Ethiopic/Coptic 年份估算、Dialog 嵌套 Tabs、以及表格拖放、Tabs RTL 方向一致性等问题。
- 🧩 Menu 和 docs 示例增加类型前导支持；Overlay 修复 iOS 26 定位及 FocusScope 恢复焦点兼容问题。
- 📦 发布了一系列更新包，包括 react-aria@3.52.0、react-aria-components@1.21.0 等。

---

### [发布 v3.0.0 · pughpugh/react-countdown-clock · GitHub](https://github.com/pughpugh/react-countdown-clock/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · pughpugh/react-countdown-clock · GitHub](https://github.com/pughpugh/react-countdown-clock/releases/tag/v3.0.0)

这是一个关于 react-countdown-clock 组件 v3.0.0 版本的发布说明，总结了本次更新在代码重写、构建方式、React 兼容性、测试、渲染性能及界面等方面的主要改进。

- 📝 使用现代 JavaScript 和 Hooks 重写了整个组件。
- 📦 改用 esbuild 构建，并支持 ESM 与 CJS 模块格式。
- ⚛️ 升级兼容 React 18，同时适配 React 19。
- 🧪 新增 Vitest 测试套件，并配置 GitHub Actions 进行持续集成。
- ✨ 引入 Biome 用于代码检查与格式统一。
- ⏱️ 用 requestAnimationFrame 替代 setTimeout，实现 60fps 的流畅渲染。
- 🐛 修复了 canvas 渲染错误和可访问性焦点轮廓问题。
- 🎨 对演示页面进行了全新的 UI 改版。

---

### [](https://uppy.io/docs/react/)

**原文标题**: [React | Uppy](https://uppy.io/docs/react/)

overview summary
- 📦 `@uppy/react` 为 Uppy UI 插件提供 React 组件与 Hooks，可通过 NPM 或 Yarn 安装，并需注意同时安装 `@uppy/dashboard` 等同级依赖。
- 🧩 提供三种构建 UI 的方式：预组合组件（如 `<Dashboard />`、`<DragDrop />`）、无头组件（更灵活可自定义样式）以及 Hooks（完全自定义 UI）。
- ⚙️ 预组合组件包括 Dashboard、DashboardModal、ProgressBar、StatusBar 等，其中部分组件在 Uppy 5.0 中已被移除（如 DragDrop 和 ProgressBar）。
- 🧠 无头组件需包裹在 `UppyContextProvider` 中，通过 data 属性可覆盖样式，例如 `UploadButton`、`Thumbnail`、`ProviderIcon`、`FilesList`、`FilesGrid`、`Dropzone` 等。
- 🔌 Hooks 必须配合 `UppyContextProvider` 使用（`useUppyState` 与 `useUppyEvent` 除外），包括 `useUppyState`（响应式获取状态）、`useUppyEvent`（监听事件）、`useDropzone`、`useFileInput`、`useRemoteSource`、`useWebcam`、`useScreenCapture` 等。
- 💡 组件初始化时推荐用 `useState(() => new Uppy())` 避免重复创建实例；多个实例需指定唯一 `id`。
- 🔄 若要在页面切换时保留状态与上传进度，可将 Uppy 实例提升至页面组件之上，通过 props 传递。
- 🔧 可通过 `useEffect` 根据 props 动态更新 Uppy 或插件选项（如 `restrictions`、`webcamModes`）。
- 🔐 使用 Transloadit 时，生产环境必须配置签名认证，建议通过 `assemblyOptions` 在服务端获取签名参数，避免泄露密钥。

---

### [](https://github.com/wcandillon/react-native-webgpu)

**原文标题**: [GitHub - wcandillon/react-native-webgpu: React Native WebGPU powered by Dawn · GitHub](https://github.com/wcandillon/react-native-webgpu)

该仓库是 React Native WebGPU，一个为 React Native 提供 WebGPU 支持的库，底层由 Dawn 驱动。页面包含项目介绍、安装文档、贡献指南及 MIT 许可证等，并展示了社区活跃信息。

- ⚛️ React Native WebGPU：基于 Dawn 为 React Native 带来 WebGPU 能力
- 🔗 官方文档与演示：wcandillon.github.io/react-native-webgpu
- 📥 提供“Getting Started”安装指引
- 🤝 贡献指南：涵盖开发、构建、测试及贡献流程（CONTRIBUTING.md）
- 📄 采用 MIT 开源许可证
- ⭐ 项目热度：1.2k Stars、68 Forks、19 Watchers
- 🏷️ 主题标签：#dawn #react-native #webgpu
- 🗂️ 仓库包含代码、Issues、Pull Requests 等标准 GitHub 功能

---

### [](https://github.com/wcandillon/react-native-webgpu/tree/main/apps/expo-webgpu)

**原文标题**: [react-native-webgpu/apps/expo-webgpu at main · wcandillon/react-native-webgpu · GitHub](https://github.com/wcandillon/react-native-webgpu/tree/main/apps/expo-webgpu)

这是一个 react-native-webgpu 的 Expo 示例模板，演示了在 Expo 应用中集成 WebGPU 的三种方式：直接使用 WebGPU API 与 WGSL、通过 Three.js（three/webgpu）命令式渲染、以及使用 React Three Fiber 声明式渲染。同时提供了快速创建项目的命令，并说明了原生构建环境要求和 React Native 特有的帧提交注意事项。

- 🚀 该模板展示如何在 Expo 中使用 react-native-webgpu 构建 WebGPU 应用
- 📦 使用 `npx create-expo-app` 并指定 GitHub 模板即可快速创建项目
- ⚙️ 运行命令为 `npx expo run`，需要原生开发构建，不支持 Expo Go
- 🎨 支持直接编写 WebGPU API 和 WGSL 着色器代码
- 🖼️ 可通过 Three.js 的 `three/webgpu` 模块进行命令式 3D 渲染
- ⚛️ 也支持 React Three Fiber 声明式场景编写
- 🔀 Metro 解析器会将 Three.js 自动重定向到 WebGPU 构建版本
- 📲 在 React Native 中，提交或渲染帧后需要手动调用 `context.present()`

---

### [面向React Web开发者的Expo](https://expo.dev/solutions/expo-for-react-web-devs?utm_campaign=33087804-React%20to%20Native&utm_source=email&utm_medium=email&utm_term=react-status)

**原文标题**: [Expo for React web devs](https://expo.dev/solutions/expo-for-react-web-devs?utm_campaign=33087804-React%20to%20Native&utm_source=email&utm_medium=email&utm_term=react-status)

Expo 是一个基于 React Native 的框架，让熟悉 React 的网页开发者无需学习新工具即可构建原生 iOS 和 Android 应用。它提供文件路由、原生 API、云端构建与托管服务，并支持一套代码多平台运行，受到 Meta 推荐和大量开发者喜爱。

- 📱 将 React 技能直接用于移动端：React Native 采用与 React 相同的组件模型，大部分代码使用 JS/TS，已有模式与库可继续沿用。
- ⚛️ 真正原生渲染：React Native 映射到 iOS/Android 原生 UI 元素，而非 WebView，性能与体验更佳。
- 🌍 一套代码多平台：支持 iOS、Android 和 Web，并通过 Expo Router 和 API Routes 共享导航与后端逻辑。
- 🧩 简化移动开发：开源框架包含 100+ 维护良好的库、顶级开发工具及自动化服务，减轻 Xcode 和 Android Studio 负担。
- 🗂️ 文件式路由：Expo Router 的文件式路由对用过 Next.js 的开发者非常熟悉。
- 🔧 原生 API 抽象：相机、推送通知、文件系统等原生能力以 Hooks 和组件形式暴露，易于调用。
- ☁️ 免本地原生环境：EAS Build 和 Submit 负责处理原本繁琐的 Xcode 与 Android Studio 构建提交工作。
- 🚀 快速迭代与开源：开源模型和快速反馈循环体现了 Web 开发的最佳实践。
- 📚 丰富学习资源：提供从 React 转 React Native 的 12 分钟指南、Expo Router 文档、EAS Hosting 文档及多种教程。
- ❤️ 开发者社区认可：大量开发者公开表达对 Expo 的喜爱，认为其更新便捷、体验优秀，是构建 RN 应用的最佳选择。

---

### [](https://zod.dev/blog/zod-4-5)

**原文标题**: [Zod 4.5](https://zod.dev/blog/zod-4-5)

Zod 4.5 版本正式发布，核心亮点是全新的 `z.compile()` 预编译机制，可将解析性能提升 3~9 倍；同时还带来了信用卡号校验、更丰富的部分类型工具、极速布尔校验等新 API，并将 schema 内存占用压缩了约 9 倍，另有多项修复。

- 🚀 核心特性：`z.compile(schema)` 可预编译任意 schema，使用时与普通 schema 完全一致，但解析速度提升约 3~9 倍（对象/数组/联合类型收益最大）
- ⚡ 全量编译：在入口导入 `zod/compile` 即可让所有后续构建的 schema 首次解析时自动编译；也支持 Node CLI `--import zod/compile` 或 Bun/Nub 的 preload 配置
- 💳 新增 `z.creditCard()` 字符串格式：接受 12~19 位数字（可用空格或连字符分隔），并校验 Luhn 校验和
- 🧩 新增 `z.properties()`：作为 `z.property()` 的多属性版本，可与 `z.instanceof()` 配合快速校验对象实例的多个字段
- 📦 回归 `z.deepPartial()` 顶层函数，可递归将对象所有层级字段变为可选，且结果仍是功能完整的 `ZodObject`
- 🎯 新增 `.exactPartial()`：字段可省略但不可显式设为 `undefined`，与 TypeScript 的 `exactOptionalPropertyTypes` 语义一致
- ✅ 新增 `z.validate()` / `z.validateAsync()`：跳过完整解析、直接返回布尔值，无效输入时比 `.safeParse()` 快最多 16 倍
- 🔄 新增 `z.input()` / `z.output()`：可将 schema 投影到输入或输出侧，便于独立校验 codec/pipe 的上下半场
- 🏷️ 新增 `z.toZod<T>()`：借助静态类型定义与类型完全一致的 schema，不改变原有 schema 实例
- 🔑 新增 `z.getDiscriminatedOption()`：按判别值从 discriminated union 中提取对应成员 schema，非法键会触发 TS 报错
- ♻️ 递归 schema 现已支持循环输入数据；Zod 自动处理，Zod Mini 需额外注册 memoizer
- 🧠 内存占用大幅削减：单个 `z.string()` 从 4.4 的 7.5KB 降至 784 字节（降幅约 90%），归功于方法记忆化与原型共享
- 🐢 失败路径提速：`.safeParse()` 不再捕获堆栈踪迹，校验失败场景比 Zod 4.4 快约 7.5 倍
- 🏷️ `z.object()` 支持 symbol 键：TS 会将 `const` symbol 推断为 `unique symbol`，schema 声明后该键变为必填且类型受检
- ⚠️ 破坏性修复：`z.iso.datetime()` 及带 offset 形式现在强制要求秒（RFC 3339）；`local: true` 不受影响
- ⚠️ 破坏性修复：字符串 `.max()` / `.min()` / `.length()` 由 UTF-16 码元改为按 Unicode 码点计数，影响含 emoji 等星芒字符的校验
- ⚠️ 破坏性修复：record key schema 只约束匹配到的键（对齐 TS 索引签名语义）；对象与 pattern record 求交集时不再误伤自身键
- 🔒 安全加固：`__proto__` 键在对象/record 解析时一律剥离；`.strict()` 会将其报告为 `unrecognized_keys`；错误格式化与 JSON Schema 转换均改用自有属性写入，防原型链污染
- ⚠️ 格式校验收紧：`z.ipv6()` 改为直接校验地址字符、`z.ulid()` 首位限定 `0-7`、`z.httpUrl()` 执行 RFC 1035 主机名长度限制、`z.emoji()` 消除指数回溯等
- 🌐 新增 8 种语言环境：孟加拉语、中库尔德语、印地语、卡纳达语、挪威尼诺斯克语、巴西葡萄牙语、斯洛伐克语、土库曼语
- 🙏 本版本共合并 155 个提交，感谢所有贡献者；更新日志与完整提交列表见官方发布页

---

### [](https://bun.com/blog/bun-v1.4)

**原文标题**: [Bun 1.4 | Bun Blog](https://bun.com/blog/bun-v1.4)

Bun 1.4 是一次重大版本更新：大幅提升 Node.js 兼容性、性能和内置能力，并将运行时从 Zig 重写为 Rust。它新增大量内置 API、全面改进包管理器与测试工具，并强化生产环境下的资源效率与安全性。

- 🚀 兼容性大幅跃升：新增 1,517 项 Node.js 测试通过，node:http、node:fs、node:cluster 等模块通过率达 97% 以上；node:quic、node:events、node:sqlite 达 99–100%。
- 📉 生产性能显著优化：空闲 CPU 使用率降低 5 倍，内存占用最高减少 48%，Linux 启动速度提升 2 倍、Windows 提升 2.5 倍，二进制体积缩小 17%。
- 🦀 核心重写为 Rust：这是首个基于 Rust 移植的正式版本，后续发布将延续此架构。
- 🧰 新增大量内置 API：Bun.Image（图像处理）、Bun.WebView（无头浏览器）、Bun.markdown、Bun.cron()、Bun.Terminal、Bun.JSON5/XML/TOML/Archive 等，免去 npm 依赖。
- ⚡ 流式处理与背压优化：ReadableStream 等原生化，吞吐和内存均优于 Node.js/Deno；Bun.serve 自动暂停慢速客户端，避免 OOM。
- 🛠️ 开发工具增强：新增 --cpu-prof-md、--heap-prof-md、--metafile-md，支持 Markdown 格式的性能与包体积分析。
- 📦 包管理器升级：bun install 更快，支持全局虚拟存储、bun audit fix、bun dedupe、bun prune、bun pm diff 与 licenses 等命令。
- 🧪 测试工具强化：bun test --parallel / --isolate / --shard / --timings / --changed / --retry，并支持 jest.useFakeTimers()。
- 🔨 构建系统进步：内置 React Compiler（比 Babel 快约 20 倍）、TC39 装饰器、barrel import 优化、--asset 单文件打包、代码分割提速 14 倍。
- ⚡ 核心性能提速：URL 解析快 4.6 倍、RegExp 大幅加速、Promise 快 1.5–2.4 倍、zlib-ng 解压快 20%、SIMD 加速 hex/base64url 解码。
- 🔒 安全加固：TLS 证书校验更严格、fetch 请求头发送前执行 checkServerIdentity、修复多项请求解析与 tarball 提取漏洞。
- 🖥️ 平台扩展：原生 FreeBSD 与 Windows ARM64 构建、实验性 Android 支持、最低 glibc 降至 2.17、Windows 定时器精度达 1.4ms。
- 🔄 行为变更提醒：Node.js 版本报告为 26（NODE_MODULE_VERSION=147）、默认 .env 加载规则调整、YAML/TOML 解析更严格，建议阅读升级指南。

---

### [Bun 1.4 | Bun 博客](https://bun.com/blog/bun-v1.4#built-in-react-compiler)

**原文标题**: [Bun 1.4 | Bun Blog](https://bun.com/blog/bun-v1.4#built-in-react-compiler)

Bun 1.4 是一次重大发布：用 Rust 重写，显著提升 Node.js 兼容性与性能，同时带来大量内置 API 和工程化能力。

- 🚀 性能大幅优化：空闲 CPU 使用率降低 5 倍，内存最多减少 35%，Linux 启动加快约 50%，HTTP 服务内存占用在多场景下降低 13–48%。
- ✅ Node.js 兼容性显著提升：新增通过 1,517 项 Node.js 测试，node:http、node:fs、node:stream 等模块通过率超过 96%，多个模块达到 100%。
- 🦀 核心引擎重写为 Rust：Bun 从 Zig 迁移到 Rust，本版本是首个正式发布，并在底层稳定性上投入了大量工作。
- 🧰 内置 API 大幅扩充：内置 Bun.Image、Bun.WebView、Bun.markdown、Bun.cron()、Bun.Terminal、Bun.XML、Bun.Archive、Bun.JSON5/JSONL/TOML 等，替代常见第三方依赖。
- ⚡ 开发工具与包管理完善：新增 bun run/test --parallel、bun audit fix、bun dedupe、bun prune、bun pm diff；隔离安装通过全局虚拟存储最高提速 7 倍。
- 🌐 Web 服务能力增强：原生流类型全面提速并对齐标准，支持 HTTP/3 实验特性、静态文件目录服务、Range/条件请求、请求背压与压缩流。
- 📊 可观测性与调试升级：--cpu-prof-md、--heap-prof-md、bun build --metafile-md 输出 Markdown 报告，并兼容 Datadog 与 OpenTelemetry trace/pprof。
- 🧪 测试与构建工具进步：内置 React Compiler（比 Babel 插件快约 20 倍）、优化 barrel imports、支持标准 TC39 decorators；bun test 新增 parallel、shard、timings、retry、isolate 等能力。
- 🔒 安全与平台扩展：大量安全加固、TLS 证书校验更严格；新增原生 FreeBSD、Windows ARM64 构建，并提供实验性 Android 支持。
- 📚 生态兼容改善：Playwright、Next.js 16、vitest、Fastify、TypeORM、OpenTelemetry、dd-trace 等主流工具和框架已能在 Bun 上运行。

---

### [Bun 1.4 | Bun 博客](https://bun.com/blog/bun-v1.4#bun-markdown)

**原文标题**: [Bun 1.4 | Bun Blog](https://bun.com/blog/bun-v1.4#bun-markdown)

Bun 1.4 是 Bun 自 1.0 以来最大的一次更新：运行时核心从 Zig 重写为 Rust，Node.js 兼容性大幅提升，同时引入大量内置 API、开发工具与性能优化。它新增了 1,517 个来自 Node.js 官方套件的测试，修复超过 2,900 个问题，并让许多原本需要依赖 npm 包的能力直接内建于二进制中。

- 🔧 核心重写：Bun 已从 Zig 迁移至 Rust，这是该版本的基础性重构，Claude Code、Prisma Compute 等已在生产环境中使用。
- ⚡ 性能大幅提升：空闲 CPU 使用率降低最多 5 倍；内存占用最高降低 35%；Linux 启动快约 2 倍，Windows 启动快 2.5 倍；二进制体积最多缩小 17%。
- ✅ Node.js 兼容性跃升：新增 1,517 个 Node 官方测试；http、fs、http2、stream 等模块通过率达 93% 以上，node:quic、sqlite、events 等接近或达到 100%。
- 🧩 生态兼容：Playwright、Next.js 16、vitest、OpenTelemetry、dd-trace、TypeORM、Fastify、happy-dom 等更多主流工具/库可以直接运行在 Bun 上。
- 🧰 内置 API 扩展：新增 Bun.Image、Bun.WebView、Bun.markdown、Bun.cron()、Bun.Terminal 等，可替代 sharp、puppeteer、marked、node-cron、node-pty 等约 15 个常用 npm 依赖。
- 🛠️ 并行与包管理：新增 `bun run --parallel`、`bun test --parallel`，以及 `bun audit fix`、`bun dedupe`、`bun prune`、`bun pm diff`、`bun pm licenses` 等实用命令。
- 📦 安装器优化：bun install 速度依旧领先；isolated linker 的全局虚拟存储在 CI 场景下可提速 7 倍，并加入嵌套 overrides、catalog、GitHub/tarball 锁文件完整性等能力。
- 🧪 测试工具增强：支持 `--isolate`、`--shard`、`--timings`、`--changed`、`--retry`、`jest.useFakeTimers()` 等，进一步提升 Jest/Vitest 兼容性。
- ⚙️ 构建能力：内置 React Compiler，比 Babel 插件约快 20 倍；支持 TC39 decorators、barrel import 优化、内存文件构建、`--asset` 单文件编译、ESM bytecode 等。
- 🌊 流与网络：ReadableStream/WritableStream/TransformStream 原生化；新增 CompressionStream/DecompressionStream；流管线吞吐显著优于 Node/Deno，并实现请求/响应背压。
- 🌐 fetch() / HTTP：fetch() 实验性支持 HTTP/2 与 HTTP/3，新增请求体压缩、代理头、TLS 会话恢复、连接复用；Bun.serve 支持静态目录、Range/条件请求和 HTTP/3。
- 📊 可观测性：提供 `--cpu-prof-md`、`--heap-prof-md`、`--metafile-md` 等 Markdown 报告，兼容 V8 .cpuprofile/.heapsnapshot，并新增 `process.on("memoryPressure")` 事件。
- 🚀 运行性能：RegExp 问题大幅修复（如 marked 快 138 倍、isbot 快 200 倍）；`new URL()` 快 4.6 倍；Promise 快 1.5–2.4 倍；Buffer、zlib、sourcemap 解码等也有明显提升。
- 🔒 安全加固：大量涉及 TLS 证书校验、HTTP 请求解析、tarball 提取和凭据处理的修复，修改了多项默认安全行为，官方建议所有用户升级。
- 🌍 平台覆盖：新增原生 FreeBSD、Windows ARM64 与实验性 Android 构建；Linux 最低 glibc 降至 2.17；Windows 下支持 AppContainer 和亚 15ms 定时器精度。
- 🗂️ Node API 补齐：重写 node:http 客户端，完善 node:http2、node:quic、node:sqlite、node:repl、node:trace_events、node:domain 等模块，通过率大幅提升。
- ⚠️ 升级注意：Node.js 版本报告为 v26（NODE_MODULE_VERSION 147）；新 monorepo 默认 isolated linker；Bun 以 `node` 身份调用时不再自动加载 .env；另有若干破坏性行为变更需关注。

---

### [](https://ronaldsvilcins.com/2026/08/30/native-html-and-css-features-that-replaced-javascript/)

**原文标题**: [Native HTML and CSS Features That Replaced JavaScript Â· Ronalds VilciÅÅ¡](https://ronaldsvilcins.com/2026/08/30/native-html-and-css-features-that-replaced-javascript/)

现代 HTML 与 CSS 已逐渐替代许多以往必须依靠 JavaScript 才能实现的界面交互，例如折叠面板、模态框、弹出层、父元素选择、容器响应、自适应输入框和主题切换等。文章主张优先使用浏览器原生能力，以此减少代码量和依赖，仅在真正必要时才用少量 JavaScript 进行“粘合”，而不是从一开始就引入复杂脚本或库。

- 📌 原生 HTML/CSS 让开发者从“默认写 JavaScript”转变为“先从平台已有能力开始思考”。
- 🪗 使用 `<details>` 和 `<summary>` 即可实现手风琴或 FAQ 展开收起，无需点击侦听和类名切换。
- 💬 `<dialog>` 元素原生支持模态框，自动处理焦点、Esc 关闭和背景遮罩，JavaScript 只承担少量触发逻辑。
- 🎛️ Popover API 可用 `popover` 与 `popovertarget` 直接创建菜单、提示等弹出层，浏览器负责开合和关闭行为。
- 🧬 CSS `:has()` 允许根据子元素状态选择父元素，减少了过去用 JavaScript 动态切换辅助类的做法。
- 📦 Container queries 让组件能根据自身容器宽度响应布局，取代了许多用 `ResizeObserver` 或滚动事件计算的场景。
- ✍️ `field-sizing: content` 可让 textarea 随内容自动增高，免去手动监听 input 并计算 scrollHeight 的脚本。
- 🌓 `light-dark()` 配合 `color-scheme` 与 `prefers-color-scheme` 能原生适配深浅主题，无需 JavaScript 检测系统偏好。
- 🔄 CSS 还接管了平滑滚动、滚动捕捉、`position: sticky`、`aspect-ratio` 以及基于滚动时间线的动画，大幅简化滚动相关逻辑。
- ✅ 原生表单验证、`loading="lazy"`、`srcset`/`<picture>` 响应式图片也减少了浏览器本身已能处理的自定义脚本需求。
- 🏗️ 开发优先级应调整为：HTML → CSS → 少量 JavaScript → 框架或库；只有业务逻辑、复杂数据与真实状态管理仍应交给 JavaScript。
- 🧹 结论是：能删除的脚本才是最好的脚本，优先利用平台原生能力通常意味着更少维护、更少依赖和更好的浏览器集成。

---

