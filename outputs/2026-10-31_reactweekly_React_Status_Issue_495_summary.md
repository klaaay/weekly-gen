### [设计系统应默认保持快速 | Den Odell](https://denodell.com/blog/design-systems-should-be-fast-by-default)

**原文标题**: [
      Design Systems Should Be Fast by Default | Den Odell
    ](https://denodell.com/blog/design-systems-should-be-fast-by-default)

设计系统是应用性能的基础层；若组件在真实数据量下响应缓慢，所有使用它的应用都会受影响。作者像重视可访问性一样重视性能，实测 10 个流行开源设计系统，分析慢因并提出测试、性能预算与“默认快”的改进方案。

- 🧱 设计系统位于浏览器、框架和应用代码之间，组件在主线程上的开销会直接挤占应用性能。
- ⏱️ 作者用生产构建、Chrome、4 倍 CPU 节流测试两个高频重任务：打开含 249 个国家的下拉框、一次勾选 100 个复选框。
- 📊 结果差异明显：Fluent、Carbon 打开国家选择器最快；Ionic 最慢，约 1266ms，且最长无响应约 1133ms；Ant Design 勾选 100 个复选框最慢，约 421ms。
- 🧩 性能不由框架单独决定：同用 Lit 的组件表现差异很大，同一设计系统也可能一个任务慢、另一个任务较快。
- 🔍 Ionic 慢因是 Stencil 在非 Shadow DOM 的 radio group 中处理 slot，新增选项时反复检查已有子项，呈 O(n²) 增长；可通过改用 Shadow DOM 或优化 Stencil 检查逻辑修复。
- 🪟 Material UI 国家选择器一次性渲染约 250 个元素；Ant Design 采用虚拟化，只渲染可见选项，因此明显更快，但需兼顾键盘导航和屏幕阅读器。
- 🎨 UI5 在隐藏 popover 中预置全部选项及内部 Shadow DOM，打开时一次性计算约 1500 个元素样式；React Spectrum/React Aria 存在逐个读写布局导致的 layout thrashing。
- ✨ Ant Design 复选框慢因是 100 个动画同时执行样式计算与绘制；建议仅在用户直接选择时动画，或“全选”时关闭动画，并用 opacity 合成层动画替代高成本重绘。
- 🧪 作者提供 Playwright 性能测试仓库，使用 TaskDuration 与 Long Animation Frames API，设置性能预算：总耗时低于 300ms、最长阻塞低于 100ms、选项翻倍耗时增长低于 2.5 倍。
- 🚀 建议设计系统团队把性能测试纳入每次 PR，默认提供快行为，在文档标注组件测试过的数据量上限，收集真实页面性能剖面，并在发布说明中公布性能前后指标。

---

### [性能：由 nwidynski 实现更快的虚拟化条目测量 · Pull Request](https://github.com/adobe/react-spectrum/pull/10886)

**原文标题**: [perf: faster virtualized item measurement by nwidynski · Pull Request #10886 · adobe/react-spectrum · GitHub](https://github.com/adobe/react-spectrum/pull/10886)

该 PR 旨在优化 React Spectrum 虚拟化列表的测量性能：将每次提交中分散的清除高度、读取尺寸和恢复高度操作合并为一次样式/布局处理，以减少重复布局计算；目前 PR 仍处于开放状态，尚未合并，需要至少 2 位审核者批准。

- 🚀 **PR 信息**：adobe/react-spectrum #10886，标题为 “perf: faster virtualized item measurement”，由 nwidynski 发起，计划将 4 个提交合并到 `adobe:main`。
- 🧩 **关联问题**：该 PR 关闭 #10858，即“Virtualized Picker 打开时会为每个可见选项多次重新计算布局”。
- ⚡ **性能优化**：此前每个带预估尺寸的项会触发两次样式与布局计算：一次用于前一项恢复 `style.height` 后的 `isElementVisible`，一次用于清除高度后的 `getSize`。
- 🔄 **实现方式**：`useVirtualizer` 现在会在每次提交中统一清除所有高度、读取所有尺寸，再恢复高度，从而合并为单次处理。
- 🏷️ **标签与提交**：PR 被添加 `RAC` 标签；提交包括合并 `main`、修复 lint、接口重命名等。
- 💬 **审核讨论**：审核者 devongovett 担心尺寸只在整个虚拟化器重新渲染时更新，而非单个子项更新时更新；作者认为这仅影响初始测量，且子项尺寸变化可由 ResizeObserver 标志控制。
- ✅ **合并条件**：至少需要 2 个批准审核；当前有 2 位参与者，尚未分配负责人或里程碑。

---

### [GitHub - denodell/design-system-performance-tests：用于检查设计系统交互速度的性能测试 · GitHub](https://github.com/denodell/design-system-performance-tests)

**原文标题**: [GitHub - denodell/design-system-performance-tests: Performance tests for checking design systems for interaction speed · GitHub](https://github.com/denodell/design-system-performance-tests)

该仓库提供一套针对设计系统组件交互速度的性能测试，在 Chrome 中模拟真实应用常见操作：打开包含 249 个选项的国家选择器、一次性勾选 100 个复选框，并支持多设计系统对比、扩展自定义设计系统及 CI 集成。

- 🎯 测试目标：衡量设计系统组件处理“打开大选项列表”和“批量勾选复选框”两项高频任务的速度与响应性。
- 🧩 覆盖范围：已包含 Mantine、Ant Design、Material UI、React Spectrum 等 React 方案，以及 Carbon、Fluent、Web Awesome、UI5、Spectrum Web Components、Ionic 等 Web Components 方案；可复制文件夹添加自己的设计系统。
- 🧪 测试条件：CPU 降速 4 倍以近似中端手机；国家选择器需在 300ms 内打开且期间无超过 100ms 的无响应；250 个选项耗时不超过 125 个的约 2 倍；勾选 100 个复选框需在 300ms 内完成且无超过 100ms 的卡顿。
- 🚀 运行方式：需 Node.js 22+，执行 `npm install`、`npx playwright install chromium`；`npm test` 跑全部，`npx playwright test design-systems/ionic` 跑单个；`REPORT_ONLY=1` 仅输出测量值，但页面失效仍会失败。
- 🛠 添加设计系统：每个设计系统文件夹包含 `index.html`、`setup.js`、`performance.spec.js`、`package.json`；复制同类框架文件夹后修改，`setup.js` 定义下拉框/复选框 HTML、打开与勾选方式，可自定义 `openMs`、`selectAllMs`、`unresponsiveMs`、`doublingRatio` 阈值。
- 🔁 CI 集成：提供 GitHub Actions 示例在 PR 时运行测试；CI 机器可能更慢，建议先多次运行再设阈值；125 与 250 选项对比最可靠；本仓库工作流按设计系统拆分 job，使用 `REPORT_ONLY=1`，仅页面失效时失败并展示测量结果。
- 🌐 浏览器查看：运行 `npx vite` 后打开对应 `index.html`，在控制台调用 `__build()` 可添加下拉框和复选框。
- 📊 对比测量：`npm start` 会构建并测量所有设计系统，输出对比表格并保存到 `results.json`，完整运行约 1.5 小时；支持 `RUNS`、`THROTTLE`、`ONLY`、`EXTRAS` 参数；`npm run measure` 复用上次构建，修改包版本后需重新运行 `npm start`。

---

### [](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=reactstatus&utm_term=home&utm_content=Cooperpress)

**原文标题**: [Expo: Agentic Mobile Infrastructure for building application software](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=reactstatus&utm_term=home&utm_content=Cooperpress)

Expo 是面向“代理式移动开发”的一体化基础设施：用 CLI、Skills、MCP 等工具开发，借助云模拟器与设备基础设施测试，通过 Build、Update、Hosting 部署发布，并用 Observe 监控生产表现，覆盖从开发到上线的完整移动应用工作流。

- 🚀 定位为 Agentic mobile infrastructure，服务开发者、团队和 AI 编码代理的移动开发流程。
- 🧰 开发工具包括 Expo CLI、Skills、MCP、Expo Go、Snack、Orbit 等，可在任意设备上开发与预览。
- 🧪 测试环节提供云模拟器和设备基础设施，Workflows 可在每次变更时运行测试套件，并支持现成模板。
- 📦 部署支持 TestFlight 与应用商店原生发布，Update 负责后续 OTA 更新，并提供渠道和灰度发布控制。
- 📈 Observe 提供崩溃信息、性能指标和 Update 采用率监控，发现问题后可用 Update 快速修复。
- 🧱 Expo SDK 已发展 10 年以上，提供 100+ 生产级 API，一次安装即可使用，并欢迎原生代码集成。
- 📱 支持用单一代码库构建并分发到 Android、iOS 和 Web，结合 Build 与 Hosting 覆盖多端发布。
- ☁️ 云模拟器可由编码代理按需驱动，自动运行应用、验证结果，并附截图、录屏和日志作为证明，无需 Mac。
- 🏪 Launch 通过引导式流程帮助应用上架 App Store，降低配置和前置知识门槛。
- ⚙️ Workflows 可自动化构建、测试、发送更新和发布，提升移动 CI/CD 效率。
- 📊 平台数据亮眼：3M+ 开发者、50K+ GitHub stars、7M+ 周下载、100K+ 活跃开发者、500K+ 项目和 100K+ 日构建。
- 👥 社区影响力强：80% 的 React Native 开发者选择 Expo，Discord 社区成员超过 70K。
- 💬 开发者评价普遍强调 Expo 易用、跨平台、开发环境顺滑、OTA 更新方便、生态和文档完善。
- 🔐 合规与信任包括 Meta 推荐、React Foundation 成员，以及 SOC 2 Type II、GDPR、CCPA 和 SSO 支持。

---

### [推出 TanStack Redact | TanStack 博客](https://tanstack.com/blog/introducing-tanstack-redact)

**原文标题**: [Introducing TanStack Redact | TanStack Blog](https://tanstack.com/blog/introducing-tanstack-redact)

TanStack 发布 Redact 0.2.0：它是 React 和 React DOM 在浏览器端的更小替代实现，可在不改应用代码的情况下通过构建配置接入，兼容 TanStack Start、Vite、Vinext 和 Next.js，以更小体积换取同步渲染带来的调度取舍。

- 🚀 Redact 0.2.0 由 Tanner Linsley 于 2026 年 10 月 26 日发布，已从实验项目转为值得维护的生产级方案。
- 🧩 它实现了应用渲染和更新 UI 所需的 React API，现有 React 导入、组件、Hooks 和依赖可继续使用。
- 🔧 只需加入构建配置，无需修改应用代码；支持 TanStack Start、Vite、Vinext 和 Next.js。
- 🖥️ 在 Vinext 和 Next.js 中，React 仍负责服务端渲染和 Server Components，框架仍掌管路由、缓存和 Server Action 传输，Redact 接管水合与客户端渲染。
- ⚡ Redact 采用同步渲染，不包含 React 的时间切片或可中断渲染。
- 📦 官方对比默认构建的客户端 JS/CSS gzip 体积：TanStack Start 从 109.3 KB 降至 62.3 KB，节省 43.0%；Vite 从 68.3 KB 降至 20.1 KB，节省 70.5%；Vinext 从 138.1 KB 降至 98.8 KB，节省 28.5%；Next.js 从 175.6 KB 降至 139.9 KB，节省 20.4%。
- 📉 Start 和 Vite 在关闭未使用的可选功能后可进一步缩小，示例中分别降至 59.8 KB 和 12.6 KB；上述为包含懒加载 chunk 的整包体积，不代表单页下载量承诺。
- 🧪 Vinext 基准测试六轮结果显示，应用体积从 154.9 KB 降至 115.5 KB，减少 39.4 KB；生产构建时间基本不变，开发启动略快，但该基准未衡量浏览器渲染或水合速度。
- ⚠️ 主要取舍是同步渲染可能让重型渲染延迟输入；Suspense 过渡、待处理表单和乐观状态已覆盖，但仍建议用应用最繁忙的页面实测，并参考兼容性指南。
- 💡 作者仍看好 React 生态，同时认为为继续使用 React 的团队和个人提供更小、更快的实现很有价值。
- 🛠️ 官方鼓励在 TanStack Start、Vite、Vinext 或 Next.js 中试用 0.2.0，测量变化并反馈兼容性问题。

---

### [兼容性 | TanStack Redact 文档](https://tanstack.com/redact/latest/docs/compatibility)

**原文标题**: [Compatibility | TanStack Redact Docs](https://tanstack.com/redact/latest/docs/compatibility)

本文档介绍了 TanStack 的 Redact 库在兼容性方面的设计：它以 React 的 API 与行为为参照，默认 Vite 配置采用同步渲染，因此在部分 API 上与 React 的并发实现存在运行时差异；文档同时列出了各功能领域的支持范围、已知限制，以及测试中等待 hydration 的推荐做法。

- 🎯 兼容基准：Redact 以 React 的 API 与行为为参照；默认 Vite 配置使用同步渲染，部分 API 与 React 并发实现存在差异，这属于运行时取舍，并不建议改变 React 的工作方式。
- 🔄 版本适配：Vite 插件在构建时检测 React 18 版本并适配 element/context 标记，使 react-is 等库的检查继续有效；React 19 运行时代码保持不变。
- 🧪 打包与体积测试：对 React 18.0.0/18.2.0/18.3.1/19.0.0/19.3.1 的开发与生产包进行 Chromium 检查，覆盖 createRoot、SSR、hydration、refs、context、portals、懒加载与外部 store；`pnpm test:compatibility:size` 对比 origin/main 并拒绝 full/default/nano 三档的 minified、gzip、Brotli 体积增长。
- 🚫 废弃 API：未实现 `ReactDOM.render`、`hydrate`、`unmountComponentAtNode` 及公共 `findDOMNode`；应使用 `react-dom/client` 的 `createRoot` 与 `hydrateRoot`。React 18 检测仅适用于 Vite 集成，不适用于直接导入或 Next.js 适配器。
- 🧱 核心与 DOM：支持 JSX、hooks（含 `use`、`useEffectEvent`、`useId`、`useSyncExternalStore`）、context、refs、memo、lazy、portals、错误边界及现代类生命周期，旧版类生命周期为空操作；受控输入、表单重置、事件处理与 hydration 期间保留编辑均与 React 共享测试。
- ⏳ Suspense/Transition/Activity：Suspense 支持 fallback、保留主 DOM、重试、流式边界与事件重放，但无优先级调度；`useTransition` 保留已提交内容与 pending 状态，渲染仍同步、无时间切片；Activity 保留隐藏 DOM/状态并断开效果、refs 与订阅，隐藏工作同步执行。
- 🧾 表单相关 hooks：`useActionState` 按上一次结果排队 action 并跟踪 pending、将失败送入错误边界；`useOptimistic` 基于当前状态重基并在 action 完成后回滚；`useFormStatus` 向表单后代传递 pending 状态与提交数据。
- 🖼️ View Transitions：`ViewTransition` 保留状态；`addTransitionType` 默认不触发动画；原生快照、样式与回调为实验性 opt-in，动画提交等待浏览器快照回调，无并发调度器。
- 🌐 浏览器专用渲染与资源：`browser()` 请求服务端到客户端的 Suspense fallback，`onBrowserBailout` 单独上报，客户端 `use(browser())` 返回 `undefined`；支持 preload/preinit/preconnect/DNS hints 及声明式样式/脚本，并处理 document/ShadowRoot 归属与流式样式表覆盖。
- 🗄️ SSR 与缓存：SSR 提供 `renderToString`、`renderToStaticMarkup`、可读与可管道流，但未实现完整 Fizz prerender/resume；`cache` 返回其函数，`cacheSignal` 返回 `null`，`unstable_useCacheRefresh` 为稳定的客户端空操作，调用服务端刷新会抛错。
- 🧠 Compiler/RSC/调试：实现 `react/compiler-runtime` 记忆缓存入口并做别名，但不等于验证所有编译器输出模式；Server Components/Flight 保留在上游 React，未由 Redact 重实现；Fast Refresh 对兼容编辑保留状态，React DevTools 开发模式支持组件/hook 检查、编辑、owners、错误与 Suspense 控制及提交分析，生产环境移除全部 DevTools 代码。
- ⚠️ 已知限制：StrictMode 仍避免双重调用，`<Profiler>` 回调为空操作；原生动画并非完全视觉一致，生产动画、隐藏标签页行为、更广泛的资源/导航竞态及 Safari/Firefox 尚未验证。
- 🧪 测试等待 hydration：Redact 不暴露私有 `__reactFiber$`/`__reactProps$` 节点属性，建议在 effect 中为节点设置应用自有的 data 标记（如 `data-app-ready`），供 Playwright 等待；该标记仅表示该组件已提交，不代表页面所有 Suspense 边界已完成 hydrate。

---

### [即将发布的 Next.js 11 月安全版本 | Next.js](https://nextjs.org/blog/upcoming-nextjs-security-release-november-2026)

**原文标题**: [Upcoming Next.js November Security Release | Next.js](https://nextjs.org/blog/upcoming-nextjs-security-release-november-2026)

Next.js 计划于 2026 年 11 月 3 日（星期二）发布预定安全版本，提前通知以便团队规划升级；该版本将修复 7 个中危漏洞，并同步公布完整安全公告。

- 📅 安全版本定于 2026 年 11 月 3 日发布，提前通知让团队有时间规划升级。
- 🛡️ 此次发布将修复 Next.js 中的 7 个中危漏洞。
- 📄 完整公告将随版本发布，包含影响范围、受影响版本和升级说明。
- ⬆️ 建议在补丁版本发布后尽快升级到已修复版本。
- 🤝 Next.js 通过 Vercel 开源漏洞赏金计划与安全研究人员合作。
- 📧 有关安全计划或漏洞管理的问题可发送至 security@vercel.com。

---

### [](https://github.com/react/react/pull/37936)

**原文标题**: [[Flight] Add reader fuzz tests by gaearon · Pull Request #37936 · react/react · GitHub](https://github.com/react/react/pull/37936)

该 PR 为 React Flight 客户端新增模糊测试：随机生成值图，通过真实服务端和客户端进行流式传输，并按随机顺序释放数据包、模块加载、Promise 解析、流条目和组件渲染等事件，检查客户端是否在依赖全部到达后交付正确且完整的值，以捕获循环引用、共享值及异步顺序导致的提前交付或永久等待问题。

- 🧪 新增 Flight 客户端 fuzz 测试，覆盖随机值图的完整流式读写与交付校验。
- 🧩 用例由命名节点组成图，节点可为叶子值、容器或延迟到达的句柄，如 Promise、流、异步可迭代对象和服务端组件。
- 🔀 生成器通过随机操作制造循环、共享引用、函数绑定、模块加载失败、Promise 失败等复杂场景。
- ⏱️ 每个图会多次运行，随机打乱事件顺序、切分数据包，并改变消费者接入时机；支持 `FUZZ_TEST_SEED` 和 `FLIGHT_FUZZ_CASES=128` 控制测试。
- 🐞 失败时会输出可粘贴复现的测试用例，便于删减节点定位最小失败图。
- 📌 本 PR 包含 31 个已知失败用例，作为后续修复的回归测试；未跳过时 74 个已知用例中开发环境失败 47 个、生产环境失败 29 个。
- 🚧 当前大部分随机和已知测试被暂时跳过，因为依赖栈上后续修复。
- 🛠️ 已定位问题分布在 Reader、Reader streams、Writer、Reply decoder 及双端逻辑，并拆分到多个后续 PR 修复。
- 📦 体积检查显示无显著体积变化。

---

### [](https://github.com/react/react/pull/37937)

**原文标题**: [[Flight] Fix six stream bugs found by the reader fuzz by gaearon · Pull Request #37937 · react/react · GitHub](https://github.com/react/react/pull/37937)

该 PR（#37937，作者 gaearon）旨在修复 React Flight 读取器模糊测试发现的 6 个相互独立的流处理 bug。PR 当前处于开放状态，包含 6 个提交，目标分支为 `gaearon-flight-reader-fuzz`，源分支为 `gaearon-flight-stream-fixes`。由于服务端 `decodeReply` 拥有与客户端类似的流控制器，相同问题会在同一提交中一并修复。

- 🧭 **队列未清空即关闭流**：当流项目仍在等待模块加载时，如果服务端关闭流，客户端会立即关闭，导致排队项目丢失；现在关闭操作会等待队列排空，回复解码器也同步修复。
- 🧱 **字节流分离传输缓冲区**：字节流行恰好结束于传输块末尾时，客户端曾以视图方式入队以避免复制，但入队会分离底层缓冲区；Node 池化 Buffer 切片无法分离，可能导致抛错或后续块被清空。现在仅在块就是完整缓冲区时走零拷贝路径。
- 🚫 **取消后仍到达的项目**：服务端不知道消费者调用了 `reader.cancel()`，仍会发送数据；客户端曾把数据入队到已取消流中并抛错，拖垮整个响应。现在控制器记录取消状态并丢弃后续项目，回复解码器同样处理。
- ⚠️ **DEV 下项目失败产生未处理拒绝**：DEV 中 `then()` 通过原生 Promise 执行回调，四处仅传 resolve 回调，导致模块加载失败时留下未处理拒绝；现在在调用方未提供拒绝处理时传入忽略错误的 reject 处理器。
- ⏳ **BYOB 读取在字节流结束时挂起**：`controller.close()` 不会结算已等待的 BYOB 读取，规范要求源调用 `byobRequest.respond(0)`；现在两个读取器在关闭后都会响应待处理请求，修复关闭行晚于最后字节到达时的挂起问题。
- 🧩 **同一传输块中类型化数组被清空**：类型化数组行以传输块缓冲区视图交付后，同块末尾的字节流行入队会分离缓冲区，使已交付数组变空；现在若此前已从该块读出类型化数组行，则复制字节流行。
- 🧪 **测试与验证**：前五个问题均重新启用对应模糊测试用例，并添加针对性 Edge 测试；第六个问题添加“同一传输块中字节流行结束时保持类型化数组完整”的测试。

---

### [](https://github.com/react/react/pull/37939)

**原文标题**: [[Flight] Fix three writer bugs found by the reader fuzz by gaearon · Pull Request #37939 · react/react · GitHub](https://github.com/react/react/pull/37939)

该 PR 由 gaearon 提交，旨在修复 reader fuzz 测试发现的三个 React Flight writer 缺陷，涉及重复引用、调试信息序列化和大型二进制数据写入；每个缺陷都配有针对性测试，并扩展了 fuzz 覆盖范围。

- 🧪 PR #37939 当前处于开放状态，包含 3 个提交，计划从 `gaearon-flight-writer-fixes` 合并到 `gaearon-flight-reader-completion`；标签为 CLA Signed、React Core Team，暂无评审、指派和里程碑。
- 🧩 缺陷一：共享服务端组件会阻塞模型。DEV 中，被 outline 的任务若未同步完成，元素会按普通引用注册，导致第二次出现时模型必须等待渲染；修复为注册惰性引用。Prod 中，因行超限被延迟的元素，以及被 `outlineModel` 单独成行的 Error cause，也存在同类问题并一并修复。
- 🧠 缺陷二：DEV 调试信息会消耗迭代器。`renderDebugModel` 使用 `Array.from` 处理可迭代对象，会把同步迭代器读到末尾，导致后续模型拿到空迭代器；修复为仅展开可迭代对象，迭代器本身走通用对象描述。
- 💾 缺陷三：大型 typed array/ArrayBuffer 被多处持有时会重复写入。writer 未记录首次写入位置，第二次写入时因 4KB 视图和字节流转移导致空视图，两个流项持有同一个 5000 字节数组时第二个为空；修复为首次写入时按行注册，后续持有者引用该行。
- ✅ 测试与覆盖：每个 bug 都有聚焦测试；首个 bug 启用相关 fuzz 用例并允许服务端组件进入随机图，第三个 bug 允许大型二进制叶子进入 fuzz。
- 🔁 过程信息：分支经历多次 force-push，标题从“两个 DEV writer bug”改为“三个 writer bug”；该分支尚未部署。

---

### [](https://tanstack.com/blog/tanstack-ai-1-0)

**原文标题**: [TanStack AI 1.0: Still Your AI, Still Your Way | TanStack Blog](https://tanstack.com/blog/tanstack-ai-1-0)

2026 年 10 月 23 日，TanStack AI 正式发布 1.0：核心 API 进入稳定、可用于生产的阶段，并延续“仍由你掌控 AI 技术选型”的承诺——provider、框架、沙箱和通信协议均可自选。与此同时，TanStack AI 推出实验性的 Agent Harness；相比 alpha 阶段，它已扩展为覆盖聊天、工具、媒体、MCP、持久化、沙箱和 Agent 的完整工具集。

- 🚀 1.0 是正式的 API 承诺：核心 API 稳定；新的 Agent Harness 仍属于实验性功能，API 为 0.x。
- ⚠️ 升级时需同步进行：1.0 客户端需要搭配 1.0 服务端，所有稳定的 `@tanstack/ai*` 包应一起升级；实验性的 Harness 包仍保留在 0.x。
- 🔄 常见迁移包括：把 `body` 改为 `forwardedProps`，把 `conversationId` 改为 `threadId`；`threadId` 在浏览器和服务端都必填。
- 🧹 工具审批 API 也有变化：`addToolApprovalResponse()` 被移除，改为通过 `interrupts` 解析 `tool-approval`。
- 🧱 其他升级注意事项：移除 `@tanstack/ai-react-ui`、`@tanstack/ai-solid-ui`、`@tanstack/ai-vue-ui`；自建流式服务端应以 `RUN_FINISHED` 结束，不再发送 `data: [DONE]`；已存储数据需按指南迁移。
- 🧠 RC 后新增 Agent 能力：子代理、`decide()` 类型化决策、可移植 Agent Skills、上下文压缩、computer use。
- 🔧 模型能力增强：统一 `reasoning` 选项、自动 prompt caching、`retry`、跨模型历史回放、统一 Files API。
- 🔑 密钥与登录更灵活：支持 BYOK/`defineByok`，也可用 ChatGPT、GitHub Copilot、OpenRouter 或 Claude OAuth 登录。
- 🔌 MCP/WebMCP 支持增强：`createMCPServer` 可将 TanStack 工具暴露为 MCP 服务；支持工具过滤、审批、任务型工具及双向 WebMCP。
- 🌐 生态扩展：新增 Cloudflare Workers AI、AI Gateway、Azure OpenAI、Lovable AI Gateway、World Labs Marble 等适配器；新增 Remix 3、Svelte devtools 和多个沙箱 provider。
- 🧪 开发与测试：提供类型化 headless chat UI factories、自定义适配器、`fakeText()`，以及面向编码助手的 Agent Skills。
- 📚 文档按 1.0 重写：每页先讲问题与可运行设置，高级细节后置；适配器页面结构统一，Quick Start 约 5 分钟完成流式聊天。
- 🧩 新 Agent Harness：`@tanstack/ai-harness` 提供持久会话、重启后等待恢复、类型化代理、插件、多用户、后台任务；可在终端、脚本/CI、Web、ACP、MCP 中运行。
- 🛠️ 可快速构建编码代理：通过 permissions、workspaceTools、snapshots、todos、compact、usage 等插件配合 `runCli`，搭建终端 coding agent。
- 🙌 社区与伙伴：143 位贡献者参与建设，OpenRouter 等伙伴持续支持。
- 🎯 下一步：打磨核心 API、支持团队落地各类 AI 功能，并推动 Harness 稳定、增加更多 provider 和沙箱。
- 📦 快速开始：`pnpm add @tanstack/ai @tanstack/ai-react @tanstack/ai-openai`，随后按 Quick Start 或升级指南操作。

---

### [](https://devblogs.microsoft.com/react-native/react-native-windows-v0-85-is-here/)

**原文标题**: [🚀 React Native Windows v0.85 is here React Native](https://devblogs.microsoft.com/react-native/react-native-windows-v0-85-is-here/)

React Native Windows 0.85 已发布，基于 React Native 0.85.3，完成向新架构迁移并更新 Windows 构建工具链，同时带来组件能力、触摸、文本、无障碍与渲染修复，以及文本渲染性能提升。

- 🚀 发布版本为 React Native Windows 0.85.0，底层使用 React Native 0.85.3，提交范围覆盖 2026 年 4 月 1 日至 10 月 19 日。
- 🏗️ 仅支持新架构：旧架构已被移除，仍使用旧架构的应用需先迁移到 Fabric 才能升级到 0.85。
- 🛠️ 工具链要求更新为 Visual Studio 2026、.NET 10 和 Windows App SDK 1.8，升级前需先更新构建环境。
- 🪟 新增组件能力：Modal 支持 `hideTitleBar` 和 `hideBorder`，View 支持 `outline` 样式属性。
- ⌨️ 交互与无障碍改进：TurboModule 可选择提前初始化，Tooltip 可在键盘聚焦时显示且同一时间仅显示一个。
- 🔗 Win32 支持增强：`ReactNativeWindow` 现可从 `ReactNativeWin32App` 暴露，便于直接访问宿主窗口。
- 🐛 稳定性修复覆盖 TextInput 缩放、Unicode 长度计算、多行输入崩溃、高 DPI 触摸、ScrollView 键盘滚动、圆角边框、Image 更新和无障碍选中事件等。
- ⚡ 性能方面，文本渲染性能得到提升。
- 🧰 CLI 与模板更新：`run-windows` 可让 Metro 使用自定义端口，模板配置更一致，并调整了 `Microsoft.Cpp.Default.props` 的导入顺序。
- 🖼️ Gallery 应用已更新到 0.85，Microsoft Store 包版本为 2.1.10.0，可用于体验新功能和组件改进。

---

### [React.lazy、Suspense 与隐藏的 300 毫秒启动延迟 • 标签页小组件](https://tabwidgets.com/blog/react-lazy-suspense-delay)

**原文标题**: [React.lazy, Suspense and the Hidden 300 ms Startup Delay • Tab Widgets](https://tabwidgets.com/blog/react-lazy-suspense-delay)

文章讲述 Tab Widgets 新标签页扩展在优化启动性能时发现：缩小 bundle 并不是关键，真正延迟来自 React.lazy 首次渲染必然 suspend，以及 Suspense 对已就绪内容统一施加 300ms 揭示节流；最终通过预加载并自行渲染占位、避免组件触发 Suspense，使首个组件内容显示提前约 240ms。

- 🔍 **瓶颈不在字节数**：把所有脚本加载并执行完约需 100ms，但组件到约 380ms 才出现，中间大量时间浏览器空闲。
- ⏱️ **React 的隐藏延迟**：`React.lazy` 首次渲染即使代码已加载也会 suspend；React 用 `FALLBACK_THROTTLE_MS` 将 suspended 内容最多每 300ms 批量揭示一次。
- 📦 **缩小包体无效**：移出约 100KB modal 代码并缩小主文件，对内容出现时间没有可测影响；扩展从本地磁盘读取，额外几百 KB 成本很低。
- 🛠️ **初步修复**：利用 React 私有字段 `_init/_payload` 预加载 lazy 组件，并在首屏渲染前最多等待 100ms；无头 Chromium 中组件从约 380ms 提前到约 95ms，但慢磁盘下可能反而更慢。
- ✅ **最终方案**：不再让组件因代码加载而 suspend；先渲染普通占位内容并启动加载，代码到达后用普通 state update 替换为真实组件，从而绕开 300ms 节流。
- 📊 **实测效果**：Chrome/Windows 下首个组件内容从 540ms 降至 298ms，85% 内容从 540ms 降至 336ms；全部内容约 544ms，基本不变。
- ⚠️ **仍有限制**：Weather 和 Word of the Day 还会因数据请求 suspend，继续受 300ms 节流影响；导航栏测量变晚约 52ms 是淡入动画导致，并非真实渲染更晚。
- 🧠 **经验总结**：应测量“内容何时出现”而非只看文件大小；关注主线程空闲；理解框架刻意行为；先在实验室定位机制，再到真实环境确认。
- 🧩 **替代实现**：若不想依赖 React 私有字段，可维护自己的已加载组件缓存：提前 `import()`，未完成时渲染占位，完成后通过 state update 渲染组件。

---

### [](https://tanstack.com/blog/tanstack-db-1.0-rc1-going-all-in-on-oracles)

**原文标题**: [TanStack DB 1.0 RC1: Going All In on Oracles | TanStack Blog](https://tanstack.com/blog/tanstack-db-1.0-rc1-going-all-in-on-oracles)

TanStack DB 1.0 RC1 正式发布，经过 18 个月开发、Beta 测试和用户反馈，API 已稳定并可用于生产。它让后端 API 或同步引擎的数据像本地数据一样可查询、可编辑，支持实时联表查询、过滤结果和乐观更新；文章重点讲述团队如何借助“Oracles”（独立模型/测试预言）与编码代理强化 DB，在大量边缘场景和交互组合中提前发现缺陷。

- 🚀 **1.0 RC1 发布**：TanStack DB 进入生产就绪阶段，现有应用可按迁移指南升级，处理包更新和破坏性 API 变更。
- 🧩 **核心能力**：把 API/同步数据转为类型化集合，组件可查询联表、过滤后的实时结果，乐观编辑立即显示并与服务器最终协调。
- 🔄 **增量采用**：可从现有 REST API 和 TanStack Query 起步，逐步加入本地持久化、离线变更和实时同步，无需重写整个应用。
- 🧪 **Oracle 测试方法**：用独立模型计算“正确结果”，结合属性测试生成大量变更历史，对比 DB 实际行为，替代零散示例测试。
- 🧭 **可执行设计**：Oracle 把查询排序、分页、集合消息等承诺写成可验证规则，帮助代理理解哪些行为是保证、哪些只是实现细节。
- 🐞 **强化 DB 为 1.0**：团队用数百个 PR 和数月工作修复大量未知边缘 bug；例如集合删除后同键重插、乐观编辑期间服务器刷新等消息顺序问题。
- 🧷 **Oracle 覆盖扩大**：已有 211 个 Oracle 测试文件、覆盖 15 个包；仓库新增约 42 万行测试代码，用于验证消息、查询组装、分页等行为。
- 🛠️ **Oracle 设计配方**：选择一个精确承诺、独立计算答案、在正确位置观察生产行为、生成有意义序列、主动尝试欺骗 Oracle，并先诊断分歧再改预期。
- 🧮 **形式化验证关联**：复杂设计可先用 TLA+ 建可执行规范并检查操作顺序，再翻译为 TypeScript Oracle 对真实实现进行生成式测试。
- 🏗️ **“Cranes” 隐喻**：Oracle 是帮助代理触及更大设计空间的“起重机”，让代理能安全替换实现、探索组合，并由独立模型守住已有设计知识。
- 🤖 **代理工作环境**：通过 Oracle、覆盖率地图、技能文档、敌对评审和 AGENTS.md 约束，让新代理快速获得反馈并避免“修得过多”。
- 📈 **采用与生态**：@tanstack/db 周下载量超过 100 万，约为 React 的 0.6%，一年增长约 10 倍；Prisma Studio、Unkey、Skylight 等已在使用。
- 🌱 **未来方向**：探索从普通服务器函数自动生成客户端集合与动作的 API，并强调“可演化性”——让后续代理继承更好的工具与设计，从而尝试更雄心勃勃的软件。

---

### [迁移到 1.0 RC | TanStack DB 文档](https://tanstack.com/db/latest/docs/guides/migrate-to-1-0-rc)

**原文标题**: [Migrating to the 1.0 RC | TanStack DB Docs](https://tanstack.com/db/latest/docs/guides/migrate-to-1-0-rc)

该文档说明 TanStack DB 从 0.9.2 升级到 1.0.0-rc.1 的破坏性变更，涵盖包版本、事务与同步、查询与 Hooks、SSR、持久化、适配器迁移，以及可选新功能。

- 📦 **统一升级包版本**：相关 TanStack DB 包需一起升级到 npm 的 `rc` 标签；`query-db-collection` 与 `offline-transactions` 保持最新 1.x，并与 RC 的 `@tanstack/db` 配套。
- 🔁 **替换 `$synced`**：删除 `row.$synced`，改用语义相反的 `$hasPendingWrites`；自定义虚拟行也必须包含该字段。
- 🧱 **保留行元数据字段名**：`$hasPendingWrites`、`$origin`、`$key`、`$collectionId` 为保留字段，应用数据字段冲突时需重命名。
- ⏳ **等待事务结算**：用 `transaction.when('settled')` 替代 `transaction.isPersisted.promise`。
- 🔗 **Mutation handler 需显式等待同步**：handler 返回 `Promise<void>`，必须 `await` 后端确认；Electric 用 `awaitTxId`，Query Collection 不再自动 refetch，需手动 `refetch()` 或写入确认结果。
- 📥 **操作符需显式导入**：`includes` 与分组操作符需导入；嵌套子查询用 `include()` 包裹；无聚合的 `groupBy` 用 `groupKeys()`。
- ⚛️ **React live-query Hooks 变更**：移除依赖数组；结构化查询依赖 query identity，`.fn.where` 等不透明子句需提供可序列化的 `queryKey`。
- 🧭 **其他框架的身份规则**：Preact、Svelte 及基于 `DbClient` 的 Hooks 也需非空 `queryKey`；保持源 Collection 稳定，避免 `SourceCollectionIdReuseError`。
- 🧩 **Solid 读取方式变更**：`useLiveQuery` 不再暴露 `.data`，改用返回的 accessor 读取数据。
- 🚦 **区分加载失败与同步问题**：`status` 表示数据是否可展示，`health` 记录同步问题；Hooks 用 `isLoadingError`、`isCrashed`、`isSyncError` 替代 `isError`。
- 🧹 **重试与清理更新**：失败加载或停止的同步适配器用 `reload()`；有活跃订阅时 `cleanup()` 会拒绝，可用 `cleanup({ dependents: true })`；崩溃的 Collection 需清理后重启。
- 🖥️ **SSR 需显式准备**：服务端渲染行数据需 `preloadLiveQuery()` 或显式准备源 Collection；Svelte 使用 `hydrate()` 的根需标记 `hydrating`。
- 🌱 **Hydration 数据是临时种子**：`DbClient` hydration 与 `initialData` 提供的行可被源写入覆盖；行数据与元数据分开跟踪。
- ✍️ **Query Collection 直接写入需 await**：`writeInsert`、`writeUpdate`、`writeDelete`、`writeUpsert`、`writeBatch` 返回 Promise，需捕获验证错误；需要最新服务端数据时调用 `refetch()`。
- 🔌 **自定义 sync adapter 迁移**：`begin({ immediate: true })` 改为 `begin()`；`markError` 改为 `fail`；就绪后用 `reportError`/`reportHealthy`，并正确处理 reload、`loadSubset` 与中止信号。
- 💾 **持久化与浏览器资源调整**：自定义 SQLite 适配器需实现 `loadResumeSnapshot`，使用 `PersistedStorageTarget`；浏览器 SQLite 分别部署 `wa-sqlite.wasm` 与 OPFS worker。
- 🔍 **查询窗口、连接与聚合更严格**：有序 `findOne` 保留 limit；连接行 key 使用 JSON 数组；聚合验证扩展到无 `groupBy`、混合表达式与 `having` 等场景。
- 🔑 **统一使用字符串或数字键**：`getKey` 必须返回 string/number；分组结果 key 可能被编码，读取已发布行的 `$key` 更安全；`SortedMap` 不再导出。
- 🧪 **更严格的输入与适配器要求**：比较器不能返回 `NaN`；重复加载 `@tanstack/db` 会报错；PowerSync 需先升到 2，RxDB 需先升到 17；Vue `data.value` 为快照。
- 🚀 **可选新功能**：`pooledLiveQueries` 可池化大量同形查询；新增 IndexedDB Collection；SQLite 持久化新增 `initialRender` 以离线或慢网时渲染恢复数据。

---

### [](https://nextjs.org/blog/ship-less-javascript-with-ai)

**原文标题**: [Ship less JavaScript in Next.js with your AI agent | Next.js](https://nextjs.org/blog/ship-less-javascript-with-ai)

Next.js 16.4 为 AI agent 引入 JavaScript 包体优化能力，通过 Turbopack 模块图分析导入关系并自动给出优化建议；Vercel 已在 v0 和 vercel.com 上减少近 2 MB 压缩后的 JavaScript。同时，面向开发者的 Bundle Analyzer 新增路由概览、快照对比、关键渲染路径过滤等功能，帮助定位和验证包体优化效果。

- 🤖 Next.js 16.4 新增 `next-bundle-optimizer` agent skill，可自动分析并优化应用 JavaScript 包体。
- 🧩 该技能依赖 Turbopack 的详细模块图，能发现意外导入关系、重复依赖、未生效的 tree shaking，以及可迁移到 React Server Components 的逻辑。
- ✂️ Agent 会识别大型连通模块组，追踪导入链，并用 minimum cut 找出可延迟加载的导入边界，再结合源码和组件交互方式验证修改。
- 📦 在 Vercel 的实践中，agent 为 v0 和 vercel.com 找出多处优化点，累计节省近 2 MB 压缩 JavaScript，部分页面节省数百 KB。
- 💡 示例包括：实验性代码编辑器被几乎所有页面急切加载、集中式 dialog registry 引入重型组件、未使用的 trace viewer、Vercel Agent 相关渲染代码提前加载、自然语言日期库和 URL 解析代码被过早打包等。
- 🛠️ 使用方式：升级到 Next.js 16.4，运行 `npx skills add vercel/next.js --skill next-bundle-optimizer`，然后在 AI agent 中执行 `/next-bundle-optimizer`；使用 `/next-bundle-optimizer fix` 可应用建议并重新分析对比。
- 📊 面向开发者的 Bundle Analyzer 可通过 `next analyze` 启动，新增最大客户端路由摘要、按大小排序的表格视图，以及包内模块展开查看。
- 🔍 Analyzer 会自动保存分析快照，支持对比不同构建，衡量优化影响或调查功能/依赖更新后的包体增长。
- 🚀 新增关键渲染路径高亮和“仅初始加载”过滤，可排除异步依赖，聚焦首屏同步加载代码，并支持 treemap 视图。
- 💬 官方建议在应用中试用 analyzer 和 optimizer skill，并通过 GitHub Discussion、GitHub Issues 或 Discord 反馈。

---

### [](https://maple.dev/blog/react-to-foldkit/)

**原文标题**: [Porting 287,000 lines of React in 3 days. The hard part was proving nothing changed. â Maple Blog](https://maple.dev/blog/react-to-foldkit/)

Maple 用 Claude 在三天内将 287,000 行、131 个路由的 React Web 应用迁移到 Foldkit；真正困难的是用像素、行为和可访问性对比工具证明迁移前后几乎完全一致。

- 🚨 离开 React 的原因：约 520 个 atom hook 调用散布在 208 个文件中，状态与缓存分散；生产环境曾因 React error #301 崩溃，且 agent 容易重复 hook 错误。
- 🧠 选择 Foldkit：基于 Effect 的 Elm Architecture，所有状态集中在一个 Model，只有 `update` 能修改；点击、响应、定时器变成 Message，网络请求仅由 Command 发起。
- ✅ 可测试与可观测：无 hooks 和组件状态；Scene 测试可在 Node 无 DOM 运行；Command 自带 Effect span，并通过适配器接入 OpenTelemetry，HTTP 请求携带 `traceparent`。
- ⚖️ 代价：Foldkit 不能按路由拆包，启动包预计从 703 KB 增至 1.43–1.58 MB gzip。
- 🎯 “完成”标准：每个路由场景必须像素一致或 0 感知差异、0 行为差异、无 console error、无未 mock 的端点。
- 🛠️ 对比工具 `@maple/ui-parity`：构建两个生产版本，用 Playwright 驱动，共用真实 domain API 与 chDB/ClickHouse fixture 后端；未知请求直接失败。
- 🔒 确定性：冻结时间、种子化 `Math.random`、UTC/DPR 1、动画停在末态、隐藏光标和滚动条；selfcheck 先要求旧应用对比自身零差异。
- 📸 稳定截图：等待字体和图片、400ms 无 DOM 变化、两帧 canvas 哈希不变，并持续截图直到连续两张字节一致。
- 🔍 四类比较：严格/感知像素、结构与计算样式、按端点比较请求日志、ARIA 可访问性快照；50+ 场景覆盖明暗、移动、加载和错误态，超过 2,600 个变体。
- 🤖 移植方式：先做 8 个关键 spike 并产出页面模板；最多 4 个 agent 在独立 worktree 并行，另有 integrator 合并并重跑 parity，三天用了近 40 个 agent。
- 🚫 防作弊规则：agent 不得修改 baseline、场景或容差来消除 diff，修复只能进入移植代码。
- 🐞 暴露旧 React bug：基础设施视图在 workload 加载前发送空名称查询；Dashboards Reconnect 按钮无可见效果；两个 dashboard 编辑器会崩溃。
- 🕳️ harness 的盲区：合并后首轮审查发现约 40 个截图间缺陷，最终 6 个 agent 又发现约 140 个，其中 4 个严重且位于 checkout/settings；首次部署还暴露 Clerk 预构建组件与分析埋点问题。
- 📊 最终 parity：2,682 个变体中 2,188 个完全一致，485 个仅抗锯齿差异且 0 感知像素变化，9 个失败，包含时序竞争和请求日志差异。
- 📈 预览对比：Foldkit 389 次请求 vs React 393 次；p50 133ms vs 121ms。
- 🔢 规模数据：迁移分支约 700 commits；Foldkit 应用 2,000+ TS 文件、1,200+ 无 DOM 测试；parity harness 约 30k 行。
- 🔗 相关代码：移植与 harness 在 PR #1539，删除 React 并移除 harness 的 cutover 在 PR #1589；harness 源码公开在 MapleTechLabs/maple-ui-parity。

---

### [异步 React 与渐进式服务器操作 | ebey.dev](https://ebey.dev/blog/3myyseusgd22h)

**原文标题**: [Async React & Progressive Server Actions | ebey.dev](https://ebey.dev/blog/3myyseusgd22h)

文章围绕 React 异步能力与渐进式服务器操作展开，强调“JavaScript 前可用，增强后惊艳”的渐进增强理念，并说明如何用服务端 action、useActionState、useOptimistic 与 useHydrated 同时保留无 JS 表单提交和现代交互体验。

- 🧱 React Router 推动真实 `<form>`、`useNavigation()` 和 `useFetcher()`，让原生浏览器行为与增强体验并存。
- ⚡ `"use server"` 让 `<form action>` 能直接声明服务端表单操作，由打包工具完成接线，使表单在 JavaScript 加载前也能发起真实 POST。
- ⏳ `useTransition` 可用于判断异步工作是否正在进行，从而管理 pending 状态。
- 🧮 `useActionState` 可理解为异步版 `useReducer`，减少手动处理提交、状态与 loading 的样板代码。
- ✨ `useOptimistic` 在异步工作期间乐观更新 UI，其状态只存在于 transition 生命周期内。
- 🖥️ 将服务端 action 直接传给 `useActionState`，表单仍能在无 JavaScript 时提交，并获得即时 pending 反馈。
- 🚫 若用客户端函数包裹 `serverAction` 再传入 `useActionState`，hydration 后可运行，但会破坏 JavaScript 加载前的提交能力。
- 🔁 乐观服务端 action 需要 `useHydrated`：hydration 前把 `<form action>` 指向服务端 action，hydration 后再切换到增强 action。
- ✅ 核心规则是服务端 action 必须最终作为 `<form action>`，这样才能在 JavaScript 前运行；React 的统一组件模型由此支持渐进增强的异步体验。

---

### [Next.js 16.4 中的 React 编译器：Babel 与 Rust 对比及基准测试 | Waseem Anjum](https://fabwaseem.com/blog/react-compiler-nextjs)

**原文标题**: [React Compiler in Next.js 16.4: Babel vs Rust, Benchmarked | Waseem Anjum](https://fabwaseem.com/blog/react-compiler-nextjs)

文章基于 Next.js 16.4.2 + React 19.3.1 的实测，对比关闭编译器、Babel React Compiler 与实验性 Rust React Compiler 对重渲染、构建时间和包体积的影响。结论是多数 App Router 项目值得启用，但大列表仍需配合 memo()，并且应先跑 lint 规则排查不兼容代码。

- ⚙️ React Compiler 1.0 是构建时自动记忆化工具，可减少手写 useMemo、useCallback 和 memo。
- ✅ Next.js 16 通过 reactCompiler: true 启用；大型项目可先用 compilationMode: "annotation" 和 "use memo" 逐步接入。
- 📉 实测 20 次计数器点击：列表行重渲染从 20,000 次降到 0 次，JS 时间从约 60ms 降到约 7ms。
- 🧩 编译器不会自动把子组件变成 React.memo；大列表行仍会随父组件重渲染，需要给行组件包 memo()。
- 🧠 配合 memo(Row) 后，选择 10 行的行渲染从 10,000 次降到 19 次；编译器稳定 props，memo 决定列表项是否渲染。
- ⏱️ 编译步骤耗时：关闭 2.25s，Babel 5.65s（约 2.5 倍），Rust 2.5s；完整 next build 分别为 7.7s、11.1s、8.2s。
- 🦀 Rust 编译器是实验性 turbopackRustReactCompiler，需同时开启 reactCompiler: true，仅支持 Turbopack，不需要 Babel 插件。
- 📦 Babel 与 Rust 产物字节级一致；gzip 后仅增加约 1.7%，原始体积增加约 28.9%。
- 🧪 启用前先运行 eslint-plugin-react-hooks 的 recommended 规则；违反 Rules of React 的组件会被静默跳过，构建不报错。
- 🚫 常见坑：render 期间写 ref/global/prop 会导致组件被跳过；Rust 标志配 webpack 会报错；未跑 lint 难以发现被跳过组件。
- 🧱 不要急于删除现有 useMemo/useCallback；它们仍可作为逃生阀，删除可能改变编译输出。
- 🧹 对比构建性能时要删除 .next，避免 Turbopack 磁盘缓存掩盖编译成本；编译器主要优化客户端重渲染，不针对 Server Components。

---

### [Puck 0.24：字段组、选项卡和复选框 | Puck](https://puckeditor.com/blog/puck-024)

**原文标题**: [Puck 0.24: Field groups, tabs & checkboxes | Puck](https://puckeditor.com/blog/puck-024)

Puck 0.24 主要增强了字段布局与编辑器交互能力：新增 `renderFields` API，可将组件字段组织为分组和标签页；加入复选框字段、拖拽手柄，并改进对象字段、覆盖项、渲染与内联编辑等 API。官方提醒升级前查看升级指南中的破坏性变更与迁移提示。

- 🧩 新增 `renderFields` API，可自定义组件字段的排列方式。
- 🗂️ 新增 `FieldGroup`，支持字段分组、可折叠，并可用 `card` 变体显示边框容器。
- 📑 新增 `FieldTab`，可将字段组织到不同标签页中。
- ☑️ 新增 `checkbox` 字段，支持从多个选项中多选。
- 🖱️ 新增拖拽手柄，通过 `dnd.enableDragHandle` 启用，便于在深层嵌套布局中移动组件。
- 📦 `object` 字段新增 `collapsible` 与 `variant` 属性，支持折叠及 `card`/`flush` 样式。
- 🧱 `fields` 覆盖项现在按字段名接收 React 节点，便于创建自定义字段布局。
- 🎛️ `actionBar` 覆盖项新增 `dragHandle`、`dragHandleRef`，并提供 `ActionBar.DragHandle` 组件。
- 🔄 `<Render>` 新增 `fieldTransforms`，可在渲染时转换字段值而不修改原始数据。
- ✍️ 新增 `InlineTextField`，可为自定义字段类型添加画布内联文本编辑。
- 🙈 可通过 `fieldTypes` 覆盖项将某类字段设为 `null`，从而隐藏该类型所有字段。
- 🔗 `Slot` 的额外属性现在会转发给通过 `as` 指定的元素或组件。
- 💬 启用内联编辑时，`text` 与 `textarea` 字段的 `placeholder` 会显示在画布中。
- 🚀 文章还提供升级指南、完整变更日志和贡献者列表，并鼓励查看演示、文档及 GitHub。

---

### [发布 2.5.0 · bv](https://github.com/bvaughn/react-window/releases/tag/2.5.0)

**原文标题**: [Release 2.5.0 · bvaughn/react-window · GitHub](https://github.com/bvaughn/react-window/releases/tag/2.5.0)

React Window 2.5.0 于 10 月 22 日发布，包含 15 个提交，重点新增滚动容器支持、无头虚拟化 Hook、滚动状态 Hook、对 CSS scroll-padding 的支持，以及文档站点更新。

- 🚀 发布 2.5.0 版本，新增多项面向虚拟列表与网格的能力。
- 📜 `List` 和 `Grid` 新增 `scrollElement` 属性，支持随页面或祖先滚动元素一起滚动，并仅渲染可见行。
- 🧩 新增 `useVirtualizer` Hook，用于自定义无头虚拟化内容，返回渲染项、偏移与尺寸、总尺寸、可见范围及 `scrollToIndex` 方法。
- 👀 新增 `useIsScrolling` Hook，用于跟踪列表、网格或滚动元素是否正在滚动，并在支持时使用 `scrollend` 事件。
- 📐 `scrollToRow`、`scrollToColumn`、`scrollToCell` 和 `scrollToIndex` 会遵循被滚动元素的 CSS `scroll-padding`，类似浏览器 `scrollIntoView`。
- 📚 文档站点新增“随页面滚动”、“useVirtualizer”、“useIsScrolling”和“无限加载”页面。

---

### [](https://vinext.dev/blog/vinext-1-4)

**原文标题**: [Vinext 1.4: less server work, faster hydration, and lighter prefetching | Vinext blog](https://vinext.dev/blog/vinext-1-4)

Vinext 1.4 是一次以性能为核心的更新，重点减少服务端冗余工作、加快浏览器 hydration、降低预取开销，并让 HTML/RSC 缓存行为更接近 Next.js。在 Hacker News 基准中，它全面优于 1.3，服务端与浏览器指标略优于 Next.js；但大型内容站仍在首屏和服务端 CPU 上落后于 Next.js。升级需安装 `vinext@1.4.0`、`@vinext/cloudflare@1.3.0`、`@cloudflare/workers-response-store@1.1.4`，独立部署的 Response Store 也需同步部署。

- 🚀 升级与部署：安装新版本依赖；若 Workers Response Store 以独立 Worker 运行，也要部署，以修复重叠刷新处理问题。
- 🖥️ 服务端性能：Hacker News 1500 评论故事页 CPU 从 54.4ms 降至 31.1ms（-43%），吞吐提升 40% 至 22.9/s，中位响应时间下降 28%，峰值内存下降 10%，略优于 Next.js。
- 🧩 服务端优化：合并多层流式响应包装器，减少 RSC 流处理与样式提示开销；Node 端改用 React Node 构建，RSC payload 保持 UTF-8；布局每请求只运行一次。
- ⚡ 浏览器 hydration：启动 chunk 使用 V8 显式编译提示，启动脚本改为低优先级，App Router 浏览器入口更小；故事页脚本时间从 193ms 降至 143ms（-26%），LCP 从 712ms 降至 628ms。
- 📱 Lighthouse：移动端分数从 81 提升至 88，FCP 从 3.31s 降至 2.11s，TBT 从 110ms 降至 56ms，与 Next.js 的 87 分接近并略高。
- 🔗 预取优化：动态页面只预取路由的 loading 状态，不再为视口内每个链接渲染整页；内容站原型预取量从 3.9MB 降至 10.7kB，约减少 364 倍。
- 🗂️ 缓存同步：HTML 与 RSC payload 现在一起填充和再生成，并跨域名共享缓存；Workers Cache 下会后台补取另一部分，页面未命中或刷新时可能多一次请求。
- 📊 大型内容站：FCP 为 1.67s，仍落后 Next.js 的 1.21s；Lighthouse 84 对 80，JavaScript 382kB 对 623kB，峰值内存 968MB 对 2193MB，但服务端 CPU 130ms 对 102ms。
- 🧪 TanStack Redact 实验：JavaScript 下载减少 25%，首页脚本时间从 51ms 降至 14ms；但 HN 故事页脚本从 143ms 升至 264ms，TBT 从 56ms 升至 666ms，Lighthouse 从 88 降至 70，主要因 hydration 阶段进行大量 prop/HTML 对比。
- 🛠️ 其他修复：生产命令正确设置 `NODE_ENV=production`；动态 chunk 加载失败进入最近 `error.tsx`；`revalidateTag` 支持 stale 策略；Response Store 不再消耗常规刷新清理预算；布局 `notFound()` 返回 404；GA4/GTM 恢复记录客户端导航；生产服务器记录渲染错误等。

---

### [发布版本 7.91.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.91.0)

**原文标题**: [Release Version 7.91.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.91.0)

react-hook-form v7.91.0 已发布，重点修复 `useFieldArray`、验证状态、表单提交解析和表单状态同步等问题，同时包含性能优化、内部重构、测试增强与依赖更新。

- 🚀 发布 v7.91.0，包含 14 个提交，由 bluebill1049 于 10 月 23 日发布。
- 🐞 集中修复 `useFieldArray`：`setValue/setValues` 行更新、卸载注销、无值注册误增行、数组规则重索引、`reset()` 后规则丢失、提交后 `onBlur` 验证等。
- ✅ 修复验证相关问题：异步验证结果过期、`Controller` 使用旧 DOM 值、`reset()` 后 `isValid` 不更新、`handleSubmit` 验证抛错后 `isSubmitting` 未恢复、空消息数组误判为错误。
- 📋 修复表单状态问题：脏状态跟踪、`resetField()` 假值处理、`unregister` 保留验证规则、`useWatch` 默认值更新、表单未就绪时 select 选项丢失、`useForm` 残留已移除选项和禁用状态。
- 🧩 修复边界场景：渐进式 required 属性、数值 0 的 `maxLength` 验证、null 原型对象/稀疏数组比较、`constructor` 键对象克隆、外部 `errors` 对象被修改、`NaN` 和无效日期验证结果过期。
- 📨 修复 `<Form />` 对 JSON、URL 编码、multipart 和纯文本提交的处理。
- ⚡ 性能优化：调用 `getValues()` 时避免不必要复制，减少 `<Form />` 不必要的重渲染。
- 🧹 重构与文档：简化 multipart Content-Type 处理、改进内部类型、清理 memo 组件显示名、修正 JSDoc 示例。
- 🧪 测试增强：增加禁用字段数组操作覆盖，并扩展 `useFieldArray`、`reset`、验证和表单状态的回归测试。
- 📦 依赖更新：升级 `joi`、`browserslist`、`baseline-browser-mapping`、`follow-redirects` 和 `vite`。
- ❤️ 感谢 19 位贡献者及 Pennylane 团队的支持。

---

### [发布 v11.2.0 · fkhadra/react-toastify · GitHub](https://github.com/fkhadra/react-toastify/releases/tag/v11.2.0)

**原文标题**: [Release v11.2.0 · fkhadra/react-toastify · GitHub](https://github.com/fkhadra/react-toastify/releases/tag/v11.2.0)

react-toastify 发布 v11.2.0（10 月 28 日），新增自动主题、动画关闭与样式表追加选项，并修复 11.1.0 的样式注入回归，同时更新构建工具与 CI。

- 🎨 `theme="auto"` 可跟随系统配色（`prefers-color-scheme`），需主动启用，默认仍为 `light`。
- 🎞️ `transition={false}` 可关闭容器或单个 toast 的进入/退出动画。
- 📎 `<ToastContainer>` 新增 `appendStyleSheet`，将注入的 `<style>` 追加到 `<head>`，而非前置。
- 🛠️ 修复注入样式表重新前置到 `<head>` 的回归，使 CSS 变量覆盖无需 `!important`（11.1.0 回归）。
- 🏗️ 构建从 tsup 迁移至 tsdown，发布结构不变；tsconfig 移除废弃 `baseUrl` 并限定库源码。
- ⚙️ CI 使用最新 Node LTS、pnpm 12；Playground 修复类型并增加 `none` transition 选项。
- 🙌 感谢贡献者 @Aakashpai 及相关问题报告者。

---

### [](https://github.com/ealush/emoji-picker-react)

**原文标题**: [GitHub - ealush/emoji-picker-react: The most popular emoji picker for React — plug and play out of the box, or bring your own style system (Tailwind, shadcn/ui, CSS Modules, Emotion, styled-components, MUI). · GitHub](https://github.com/ealush/emoji-picker-react)

emoji-picker-react 是 React 生态中流行的表情选择器组件，既提供开箱即用的完整选择器，也支持通过 `unstyled` 或 `primitives` 按自有设计系统自由组合；内置搜索、分类、肤色、最近使用、键盘导航和无障碍能力，并适配多种样式方案与本地化需求。

- 🧩 双模式使用：完整 `<EmojiPicker />` 即插即用；`unstyled` 与 `emoji-picker-react/primitives` 支持自带设计、布局和组件。
- 📦 安装简单：`npm install emoji-picker-react`；shadcn/ui 可通过 registry 组件安装，要求 React 16.8+、Node 18+。
- ♿ 功能完整：搜索、分类导航、肤色选择、最近使用、Reactions 模式、键盘导航、ARIA、RTL、减少动画与 axe 检查。
- 🌍 本地化友好：内置 28 种语言表情数据集，可翻译搜索、分类、预览、肤色、错误提示及无障碍播报。
- 🎨 样式灵活：支持 `--epr-*` CSS 变量和 `[data-epr-part]` 选择器，适配 Tailwind、shadcn/ui、CSS Modules、Emotion、styled-components、MUI。
- 🖼️ 表情样式丰富：支持原生、Apple、Google、Facebook、Twitter 样式，以及图片自定义 emoji 和自定义分组。
- 🔒 离线与 CSP 友好：无第三方请求，样式注入支持 `nonce`；图片样式默认走 jsDelivr，也可通过 `getEmojiUrl` 自托管。
- ⚛️ 现代 React 支持：兼容 React 16.8–19、SSR、React Server Components、TypeScript；primitives 入口按需加载数据集。
- 🔍 数据 API：提供 `searchEmojis`、`getEmojiByUnified` 等无框架接口，可用于服务端或无 UI 场景。
- 🧪 质量保障：每个 PR 会将打包产物安装到 Vite、CommonJS、shadcn/ui 应用并在严格 CSP 下测试，内置 25 个可运行设计示例。
- 🔁 迁移支持：提供 v4 与 emoji-mart 迁移文档，并与 Emoji Mart、Frimousse、emoji-picker-element 进行能力对比。
- 🤖 AI 友好：附带 `llms.txt`、`llms-full.txt` 和 AI 集成指南；项目采用 MIT 许可，约 1.5k stars、215 forks，欢迎贡献与赞助。

---

### [墓地弹球](https://graveyard-pinball.vercel.app/)

**原文标题**: [Graveyard Pinball | Free 3D pinball game in WebGPU & Three.js by Anderson Mancini](https://graveyard-pinball.vercel.app/)

《Graveyard Pinball》是一款由 Anderson Mancini 制作的免费 3D 弹球游戏，基于 WebGPU 与 Three.js 构建；玩家需要启用 JavaScript 才能游玩。

- 🎮 游戏名称：Graveyard Pinball
- 🆓 可免费游玩
- 🧊 提供 3D 弹球体验
- ⚙️ 使用 WebGPU 和 Three.js 技术
- 👤 作者：Anderson Mancini
- 🌐 需启用 JavaScript 才能运行

---

### [墓地弹球：二维模拟，三维渲染](https://andersonmancini.dev/blog/graveyard-pinball)

**原文标题**: [Graveyard Pinball: simulated in 2D, rendered in 3D](https://andersonmancini.dev/blog/graveyard-pinball)

《墓地弹球》是一款免费的万圣节主题 3D 弹球游戏，可在浏览器中运行；它采用 Three.js、React Three Fiber、WebGPU 与 TSL。游戏的画面和模型是 3D 的，但物理模拟改用俯视 2D，以确保球的手感稳定一致。

- 🎮 游戏设定在闹鬼墓穴弹球台，包含骷髅传送门、三个坩埚、墓碑阵列、骷髅法师和琥珀色点阵记分屏。
- 🧱 首版使用 3D 物理引擎时，球会穿墙、越过薄墙，并因渲染帧率不同而出现不同弹球力度。
- 🛠️ 解决方案是将球、墙、缓冲器和挡板放入 Rapier2D 的俯视 2D 世界，Three.js 只负责渲染。
- ⏱️ 物理以固定 1/240 秒步长运行，并在渲染帧间插值，因此 30、60、144、240 Hz 下表现一致。
- 🚫 测试显示，球速最高 30 单位/秒时无穿墙，也没有球卡进挡板。
- 🤖 用带人类误差的机器人打数百球，结合热力图、挡板射门扇形图和通道宽度测量来调表。
- 📈 调整后，左轨道到达率从 16% 升至 32%，顶部拱门从 7% 升至 30%，右侧斜通道从 5% 升至 26%，死胡同口袋从 2 个降为 0。
- 📏 经验规则：主要通道至少 1.5 个球直径，通道口至少 1.7 个球直径，避免水平平台。
- 🧩 模拟层只发出事件，规则层再处理得分、锁定、多球和法师触发等逻辑。
- 🧙 骷髅传送门会吞球再吐出并加倍坩埚得分；第三个锁球触发三球多球，得分乘三并结算头奖。
- 📺 点阵屏使用 128×32 琥珀色纹理，单次绘制调用，几乎不增加渲染成本。
- 📱 手机端左右半屏分别控制左右挡板，并带自适应分辨率以保证帧率。
- 🔗 游戏免费发布于 graveyard-pinball.vercel.app。
- 💡 核心经验：当觉得“手感不对”时，先把它量化，再动手修改。

---

