### [](https://octanejs.dev/)

**原文标题**: [Octane — React's programming model, compiled](https://octanejs.dev/)

Octane 是一个 React 的编译型继任框架，继承 Inferno 的性能优先理念，将 React 的 hooks、Suspense 和 actions 提前编译，去掉虚拟 DOM 与 hooks 规则，同时保持 React 熟悉的编程模型，支持增量迁移与现有生态绑定。

- ⚡ 编译时优化：无虚拟 DOM，模板编译为克隆节点与直接 DOM 写入，keyed @for 列表最小化节点移动。
- 🔓 无 hooks 规则：不再需要依赖数组或调用顺序限制，编译器自动推断捕获值，hooks 可放在条件或提前返回之后。
- 🌊 异步改进：独立 use() 调用并行启动，嵌套 fetch 提前预热，流式 SSR 按边界就绪即发送。
- 🧩 熟悉模型：hooks、memo、context、portals、transitions、actions、受控表单与 Suspense 行为符合 React 预期，事件为原生，refs 为普通 props。
- 🔄 渐进迁移：保留现有 TSX，可将组件逐个改为 TSRX；OctaneCompat 允许在 React 19 应用中嵌入编译岛屿，但 React Server Components 不兼容。
- ❓ 为何不用 signals：信号仍是可用工具，但 Octane 保持普通函数自上而下读取，由编译器承担额外工作；在 signal 偏重负载下也能保持竞争力。
- 🛠️ CLI 诊断：octane doctor 提供 20 项静默故障检查，可修复重复运行时、JSX import source 缺失、tsc 误处理等问题；支持安装绑定、解码生产错误、为 AI 代理添加工具。
- 📦 生态绑定：52 个第一方绑定，覆盖状态、数据、路由、UI、表单、图表、3D 等，包括 React Three Fiber 的移植 @octanejs/three。
- 📊 性能实测：在多样套件中相对 Octane 为 1×，整体 geomean 上 Vue Vapor 0.86×、Ripple 1.0×、Solid 1.1×、Svelte 1.3×、Preact 2.7×、React 2.9×，验证快速体验而非重写思维。
- ✅ 测试保障：11,500+ 次测试执行，核心套件含 3,900+ 不同用例，React 派生覆盖逐例跟踪。

---

### [](https://octanejs.dev/docs/differences-from-react)

**原文标题**: [Octane — React's programming model, compiled](https://octanejs.dev/docs/differences-from-react)

Octane 在保留 React 组件与 Hook 心智模型的同时，借助编译器让依赖推断、状态跟踪和事件处理更贴近原生 Web 行为，并在渲染、错误边界和 API 上做了有针对性的简化与差异调整。

- 🧩 整体兼容：除非文档另有说明，Octane 行为与 React 一致，未解释的差异视为 bug。
- 📍 Hooks 按源码位置追踪，因此可放在条件或早退之后；但普通 JS 循环中基于槽位的 Hook 会报错，`use()`/`useContext` 除外。
- 🔧 `useEffect`/`useMemo`/`useCallback` 等省略依赖数组时，编译器会根据回调捕获自动推断；显式数组仍与 React 语义一致，传 `null` 表示每次执行。
- 🔗 `useState`/`useReducer` 可解构出第三个稳定函数用于读取最新状态，替代 `await` 后的 ref；新增 `useLinkedState` 让本地状态跟随 key 变化而重置/调整。
- 🛡️ 可选强模式（`"use strong"` 或配置）会拒绝渲染期间直接更新状态、在 effect 设置期间更新状态及渲染中写 `ref.current`。
- ⚡ 事件采用浏览器原生 `Event`，文本输入使用 `onInput`（原生 `change` 在 blur 时触发）；受控 `value`/`checked` 仍由 React 逻辑驱动 DOM。
- ⚠️ `OCTANE_NATIVE_TEXT_ONCHANGE` 警告会提示文本输入框上的原生 `onChange`，可通过 `suppressNativeChangeWarning` 或改用 `onInput` 处理；checkbox/radio 的原生 `change` 不可取消，需在 `click` 阶段做回滚。
- 🎨 `class`/`className` 支持 clsx 风格组合（数组、对象、嵌套），React 的 `['a','b']` 会输出 `"a,b"`，Octane 输出 `"a b"`。
- ⏱️ 更新在微任务中批量完成，一次渲染跑完；没有时间切片，但保留 transition 的 `isPending` 和 Suspense 行为，`flushSync` 会排空队列。
- 🔀 编译器会并行化可独立开始的 `use()` 请求，瀑布依赖保持顺序；渲染期间创建的 Promise 会自动记忆，无需 `cache()`。
- 🛑 错误边界通过模板 `@try/@catch` 或函数式 `ErrorBoundary`；未捕获错误走 `console.error`，生产环境错误消息替换为代码链接。
- 🖥️ 缓冲式 SSR 返回 `{ html, css }`（含作用域样式），流式 SSR 正常；hydration 时的值/结构不匹配以补丁/重建方式修复，不抛给边界。
- 🚫 省略类组件、StrictMode、`Profiler`、`SuspenseList`、`forwardRef`/`createRef`、`React.Children` 等；不支持 RSC/`cache()`，但支持资源提示（preload、preinit 等）。
- 🔬 其他差异：同值状态更新可能少跑一次组件体；`useSyncExternalStore` 快照行为更简洁；表单 action 拒绝后继续执行后续动作；keyed reconciler 采用 LIS 算法，最终 DOM 结果一致但移动路径可能不同。

---

### [](https://sentry.io/resources/etsy-workshop/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=ecommerce-fy27q3-etsyworkshop&utm_content=newsletter-primary-register)

**原文标题**: [How Etsy's Engineers Keep Their App Crash-Free During Traffic Spikes | Sentry](https://sentry.io/resources/etsy-workshop/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=ecommerce-fy27q3-etsyworkshop&utm_content=newsletter-primary-register)

概述：本內容介紹 Etsy 工程團隊如何在流量高峰（如假日購物季）維持 App 穩定，強調當機不僅是技術問題，更直接影響營收；透過與 Sentry 合作的研討會，分享即時除錯、衡量當機商業影響的實戰經驗，並提供多項相關資源。

- 📈 假日購物期間的 App 當機，會直接造成營收損失，是嚴重的商業問題。
- 🛠️ Etsy 與 Sentry 的工程專家（Jay Henry 與 Sergiy Dybskiy）聯手分享高峰流量準備策略。
- ⚡ 重點涵蓋即時除錯、效能監控，以及量化當機對業務影響的具體方法。
- 📖 收錄真實高流量事件的案例與可實作的建議，而非單純理論。
- 📋 提供「監控關鍵電商體驗開發者檢查清單」，協助開發者逐項檢核。
- 🔍 透過「Session Replay」工具，深入診斷電商效能問題與使用者在過程中的實際操作。
- 🎯 另有「如何監控與修復關鍵用戶體驗」指南，強化對核心流程的掌握與優化。

---

### [](https://tanstack.com/blog/we-stopped-using-rsc-on-tanstack-com)

**原文标题**: [We Stopped Using RSC on TanStack.com | TanStack Blog](https://tanstack.com/blog/we-stopped-using-rsc-on-tanstack-com)

TanStack.com 最初借助 React Server Components（RSC）将大型 markdown 与语法高亮渲染移往服务器，显著减少了客户端 JavaScript 体积。但作者发现真正的问题在于依赖本身过大，于是开发了轻量级替代库，最终决定放弃 RSC、回归常规 SSR，在保持性能提升的同时，也让代码与数据流变得更简单直接。

- 📘 初始痛点：内容页面需加载约 1.1 MiB 脚本，其中约 358 KiB 与语法高亮（Shiki 等）有关，浏览器不得不下载庞大的渲染管线来阅读文档。  
- 🚀 RSC 带来的收益：将 markdown 和代码渲染移至服务器后，博客页与文档页客户端 JS 减少约 153 KB，Lighthouse 分数提升，TBT 大幅下降（如博客页从 1200ms 降至 260ms）。  
- 🔍 关键反思：RSC 只是把重量级依赖藏在服务器端，并未让渲染器变小；如果依赖本身变轻，是否还需要这套复杂架构？  
- ✨ 新方案：开发了 @tanstack/markdown 与 @tanstack/highlight 两个小型包，明确窄化的渲染契约，使显式渲染代码仅约 27 KiB transferred。  
- 🗂️ 回归 SSR：服务器函数直接返回原始 markdown 和代码数据，客户端用自有包渲染，不再需要 Flight 序列化、特殊文件或服务器边界概念。  
- 📊 性能对比：常规 SSR 版在总字节和 TBT 上依然占优，例如博客页 TBT 从 139ms 降至 66ms，传输从 1086 KiB 降至 889 KiB。  
- 🔁 多页面优势：SSR 只一次性支付 18–19 KiB 渲染器成本，之后每次导航只发送改变的数据（1.5–5.6 KB），而 RSC 每次都需要重新发送渲染好的 Flight payload。  
- 🧹 代码简化：删除了整套 contentRsc 专用管道，路由不再收到序列化后的 React 节点，而是普通内容；开发者不需要再理解 RSC 边界与打包器上下文。  
- 🤔 核心结论：RSC 解决的是依赖过大的问题，一旦依赖变小，其架构开销就不再划算；TanStack.com 更适合“让内容保持内容”的常规 SSR。  
- 🧩 支持但不强制：TanStack Start 仍将 RSC 作为可选能力，但不会再将其视为默认架构；生态中“是否支持 RSC”更像一个检查项，多数应用可能并不真正需要它。

---

### [](https://tanstack.com/blog/tanstack-has-a-new-look)

**原文标题**: [TanStack Has a New Look | TanStack Blog](https://tanstack.com/blog/tanstack-has-a-new-look)

TanStack 发布了全新品牌形象，由首位设计负责人 Andy Beutler 主导，从 Logo 到设计系统全面升级，强调在 AI 时代下保留人性化质感与“时间归还”的理念。

- 🌴 全新品牌形象上线：TanStack 更新了 Logo、字体、设计令牌（tokens）与组件库，整体风格更温暖、克制而有人味。
- 🎨 首任设计负责人加入：Andy Beutler 成为 TanStack 首位全职设计负责人，将过去分散的设计直觉系统化，形成可共享的 `/ds` 设计系统。
- 😅 旧设计“够用但不再够好”：过去的界面干净整齐，但在 AI 能轻易生成标准开发者网站的 2026 年，这种“标准化的精致”已无法体现独特价值。
- 🤖 对抗 AI 的“机器感”：TanStack 在构建面向 AI 的工具，但希望产品与品牌能传递真实人类的用心，而非机器批量生成的痕迹。
- ⏳ “归还时间”是核心理念：无论是 Query、Router 还是 Table/Form，Tanner 认为 TanStack 的真正产品是帮开发者省下时间，去享受生活。
- 🏖️ 海滩意象的意义：棕榈树与岛屿不是装饰，而是传达“你被照顾好了，去过你的人生”的态度，新品牌延续并强化了这一情绪。
- 🧭 克制胜于堆砌：在 AI 让人“什么都能做”的年代，选择少而重要的东西并用心打磨，才是新品牌的质量标准。
- 📁 设计系统 `/ds` 是重点：颜色、字体、组件终于有了统一的家，让后续维护与决策有据可依，避免每次重复造轮子。
- 🚧 尚未完成，持续演进：部分页面仍处于新旧过渡状态，团队选择先打好真实根基，而非等待一次不切实际的“完美重启”。

---

### [](https://tanstack.com/)

**原文标题**: [TanStack | The open-source application stack for the web.](https://tanstack.com/)

overview summary
TanStack 是一个开源 Web 应用技术栈，提供无头、类型安全、可组合的库，帮助开发者构建现代、可扩展的应用。其核心库覆盖路由、数据获取、状态管理、表单、虚拟化、Markdown 等场景，强调框架无关、生产级质量与社区驱动，并拥有活跃的社区和核心维护者团队。

- 📚 提供无头、类型安全、可组合的工具集，适用于现代 Web 应用开发
- 🔄 核心框架无关，支持 React、Vue、Svelte、Solid、Angular 及 Vanilla
- 🛡️ 从底层采用 TypeScript 构建，提供出色的类型安全与自动补全
- 🚀 经过大规模生产验证：总下载量超 150 亿次，周下载量超 1.33 亿次
- 🔓 MIT 许可，无供应商锁定，可自托管，社区驱动
- 🧭 主要库包括 Router、Query、Form、Store、Virtual、Pacer、Markdown、Highlight 等
- 🧑‍💻 社区渠道丰富：Discord 实时支持、GitHub 开源协作、YouTube 官方频道
- 📝 最新博客动态：TanStack 品牌焕新、发布 Markdown 与 Highlight 库、弃用 RSC 的实践分享
- 👥 核心维护者包括 Tanner Linsley、Dominik Dorfmeister、Corbin Crutchley 等
- 🤝 提供合作伙伴计划、OSS 赞助商支持，以及企业级支持服务

---

### [](https://www.youtube.com/watch?v=B_w1xFbRvCg)

**原文标题**: [React Debugging with Performance Tracks - YouTube](https://www.youtube.com/watch?v=B_w1xFbRvCg)

overview summary
- 📺 這是 YouTube 網站底部的標準資訊與服務連結清單，涵蓋媒體、著作權、聯絡方式、創作者資源、廣告、開發人員、條款、隱私權及平台運作說明。
- ⚖️ 包含法律與政策相關項目：著作權、條款、隱私權、政策與安全性，保障使用者與創作者的權益。
- 👤 提供創作者與廣告相關入口，方便內容創作者與品牌合作推廣。
- 🔧 列出平台技術與營運細節，如開發人員選項、YouTube 運作方式與測試新功能。
- 📅 版權標示為 © 2026 Google LLC，確認所有權歸屬與年份。

---

### [](https://react.dev/reference/dev-tools/react-performance-tracks)

**原文标题**: [React Performance tracks – React](https://react.dev/reference/dev-tools/react-performance-tracks)

overview summary
- 🎯 React Performance tracks 是浏览器开发者工具 Performance 面板中的专用自定义条目，用于可视化 React 特定事件与指标，并与网络请求、JavaScript 执行、事件循环等数据同步展示。
- ⚙️ 仅在开发版（默认启用）和 profiling 构建中可用；生产构建默认关闭以避免性能开销。Server 相关轨道仅在开发版可用。
- 📦 使用 profiling 构建时，需将 `react-dom/client` 别名指向 `react-dom/profiling`，可通过打包器别名或框架内置支持实现。
- 🗂️ Scheduler 轨道包含 4 个子轨道：Blocking（同步更新）、Transition（后台非阻塞）、Suspense（边界相关）、Idle（低优先级）。每次渲染分为 Update、Render、Commit、Remaining Effects 等阶段。
- 🔁 级联更新可能导致性能回退；开发版中点击“Cascading update”可查看调度更新的组件及堆栈。
- 📊 Components 轨道以火焰图展示组件渲染时长及 effect 时长（仅显示 ≥0.05ms 或触发更新的 effect），并支持挂载/卸载/重连/断开事件；开发版点击可检查 props 变化。
- 🌐 Server Requests 轨道显示所有最终进入 React Server Component 的 Promise，合并第三方库内部请求，点击可查看堆栈和 resolved/rejected 值。
- 🖥️ Server Components 轨道以火焰图展示组件等待 Promise 的耗时，颜色越深耗时越长；包含一个“Primary”轨道，并发时显示“Parallel”轨道（最多 8 个并发）。

---

### [](https://aurorascharff.no/posts/experimenting-with-rsc-for-performance-and-ux-in-nextjs/)

**原文标题**: [Experimenting with RSCs for Performance and UX in Next.js | Aurora Scharff](https://aurorascharff.no/posts/experimenting-with-rsc-for-performance-and-ux-in-nextjs/)

overview summary
- 🧪 文章探索了在 Next.js App Router 中运用 React Server Components (RSCs) 与 Server Functions 来优化性能与用户体验的三个实践案例：URL 驱动的“加载更多”、流式搜索及服务端渲染的草稿预览。
- 🖥️ 核心思路是尽可能将数据获取与渲染工作留在服务端，仅将必要的交互交给小型客户端组件，同时利用 URL 和 Suspense 保持页面状态与即时反馈。
- ⚙️ 通过 `?page=` 参数驱动分页，服务端按需流式渲染新页面，让“加载更多”按钮无需自行抓取数据，且页码可分享、刷新后仍保留。
- ⌨️ 搜索输入框被设计为静态外壳的一部分，仅负责写入 URL，查询结果在 `Suspense` 边界内流式更新，从而保证输入框始终聚焦且不阻塞渲染。
- 🚀 使用内联脚本与 layout effect 预填输入框，并在过渡期间用 `isPending` 状态轻微淡化旧结果，以提供流畅的视觉反馈。
- 📝 消息撰写器通过 Server Function 按需返回 JSX，让预览内容与真实帖子的渲染逻辑完全一致，同时将 Shiki 高亮等重活留在服务端。
- 🔄 文章也对比了“基于客户端状态的分页”方案，虽然可避免重发旧数据，但牺牲了 URL 共享、持久化与缓存能力，更适用于草稿预览这类场景。
- 💡 关键要点：善用服务端能力、利用 URL 保存状态、将动态读取隔离在 Suspense 之后，并通过 `children` 或 Server Functions 将服务端输出传递给客户端组件。
- ✨ 这些实验并非必需模式，但展示了 RSC 的潜力，鼓励开发者从服务端思维出发构建交互功能，以获得更快的首屏与更流畅的体验。

---

### [](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

**原文标题**: [
      Your SPA Is Leaking Memory. Soak Test It — Den Odell
    ](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

概述：这篇文章介绍了单页应用（SPA）内存泄漏的问题，并详细说明了如何用 Playwright 进行前端浸泡测试（Soak Test）来检测内存泄漏。文章解释了内存泄漏的成因、测试方法、关键代码实现，以及如何通过伪造时钟和网络来加速测试，使测试结果更贴近真实使用场景。

- 🔍 内存泄漏是 SPA 的常见问题：页面不刷新，监听器、定时器和缓存不断累积，最终导致浏览器标签页崩溃或卡顿。
- 🧪 后端团队早已用浸泡测试检测内存泄漏，前端同样需要此类测试，因为 SPA 长期运行，内存不会自动释放。
- 📊 一项对 500 个 React、Vue 和 Angular 仓库的分析发现，86% 的代码存在未移除的监听器、定时器或订阅。
- 🛠️ 使用 Playwright 构建前端浸泡测试：在单一浏览器上下文中重复运行同一用户流程，对比测试前后的内存指标。
- 📈 通过 Chrome DevTools 协议（CDP）收集页面指标，包括堆大小、DOM 节点数和监听器数量，用于判断是否存在泄漏。
- ⏳ 测试前需进行数次预热循环，避免首次加载代码和数据造成的假阳性；同时需执行两次垃圾回收以确保节点计数准确。
- 🔁 断言通常关注监听器数量不增长，以及 DOM 节点数的增长控制在允许范围内（例如 100 个节点）。
- ⏱️ 使用 Playwright 的时钟伪造功能模拟时间流逝，可在短时间内覆盖数小时的真实使用场景，从而检测定时器泄漏。
- 📡 还需模拟网络请求（如 API 响应和 WebSocket），确保定时器频率与真实情况一致，并避免真实网络延迟干扰测试。
- 🧩 若检测到泄漏，可通过 Chrome DevTools 的堆快照和“Detached”过滤器定位持有已删除 DOM 节点的引用。
- ✅ 浸泡测试应纳入夜间自动化任务，以便在问题进入生产环境前及时发现并修复，而不是等用户反馈后紧急处理。

---

### [](https://dx-styles.dev/blog/state-of-zero-runtime-css-in-js/)

**原文标题**: [The state of zero-runtime CSS-in-JS, mid-2026 â dx-styles blog](https://dx-styles.dev/blog/state-of-zero-runtime-css-in-js/)

2026 年零运行时 CSS-in-JS 生态已全面转向编译时方案，运行时库（如 styled-components）逐步退场，各库在原子化、语义化、构建成本等维度分化，选择取决于项目规模与团队结构。

- 📉 运行时 CSS-in-JS 衰退：React 并发渲染与 Server Components 使运行时注入低效，styled-components 2025 年进入维护模式，MUI 的 Pigment CSS 暂停在 alpha 阶段。
- ⚙️ 编译时成为主流：样式在构建期求值为真实 CSS 文件，JS 只剩类名字符串，无运行时、无 Provider、天然兼容 RSC，保留类型安全与就近书写优势。
- 🧩 vanilla-extract：TypeScript 版 CSS Modules，成熟稳定，主题与 recipes 完善，缺点是样式必须放独立 `.css.ts` 文件，无法与组件同文件。
- 🐼 Panda CSS：配置优先、原子化输出，生态最丰富，类 Chakra 体验；代价是代码生成产物与 DevTools 中难以阅读的 class 堆叠。
- 🎯 StyleX：Meta 生产级方案，强约束与确定性合并，适合数千贡献者的大规模代码库防止样式冲突，小团队会感到束缚。
- 🚀 next-yak：保留 styled-components 语法，Rust 编译器转为静态 CSS，动态值用 CSS 自定义属性，适合大型存量代码库无重写迁移，构建速度快。
- 🌿 Linaria：零运行时鼻祖，仍是 drop-in 替代，底层 wyw-in-js 引擎支持与 dx-styles 共存，可逐文件渐进迁移，但新项目推荐新一代方案。
- 🏛️ dx-styles（作者项目）：基于同一引擎，API 面向设计系统，语义化确定性类名、类型化 recipes/slot recipes、token 契约、编译时 RTL，并带 class 溯源工具。
- 🏢 Griffel：微软 Fluent UI 的原子引擎，源于早期 Linaria fork，自成一派，外部互操作少。
- 🚪 诚实的出口：Tailwind 与 CSS Modules 虽不属于 CSS-in-JS，但对很多团队就是正确答案，离开该范畴也是合理迁移目标。
- 🗺️ 选型指南：大存量 styled-components 选 next-yak 或 Linaria→dx-styles 渐进迁移；应用项目选 vanilla-extract 或 Panda；组件库/设计系统选 dx-styles 或 vanilla-extract；超大规模防冲突选 StyleX；想省心就 Tailwind/CSS Modules。
- 🔮 未来趋势：所有幸存库都收敛到“普通元素 + 类名”，差异只在原子 vs 语义、配置 vs 代码、设计系统能力是否一等公民；构建成本成为下一个竞争焦点，作者将发布可复现的构建时基准测试。

---

### [使用VisionCamera在React Native中构建实时人脸识别应用 — Margelo博客](https://blog.margelo.com/on-device-face-recognition-react-native)

**原文标题**: [Building a Real-Time Face Recognition App in React Native with VisionCamera — Margelo Blog](https://blog.margelo.com/on-device-face-recognition-react-native)

概述：本文详细拆解了在 React Native 手机端实现实时人脸识别签到系统的完整计算机视觉流水线，涵盖检测、对齐、活体检测、嵌入、匹配、优化及真实世界中的工程陷阱，强调全流程端侧运行以保护隐私。

- 📱 需求看似简单（无徽章/二维码刷脸签到），背后却是实时 CV 流水线：检测、跟踪、对齐、嵌入、匹配、防伪必须在几十毫秒内完成。
- 🔒 人脸数据敏感，全程端侧运行，不调用云端 API，在隐私、延迟、离线可用性上全面占优。
- 🧩 人脸识别不是单个模型，而是多阶段接力赛：检测、对齐、活体、嵌入、匹配各有专责，彼此独立，便于优化和升级。
- 📷 使用 VisionCamera v5 的帧输出 API 获取相机帧，需注意分辨率（640×480 足够）、像素格式（直接用 YUV）、背压处理（dropFramesWhileBusy），并且每帧必须 dispose。
- 🔍 人脸检测模型首选 YuNet（约 230 KB，5 个关键点，MIT 许可），也可用 BlazeFace、SCRFD、RetinaFace；输入尺寸和置信度阈值是主要调优参数。
- 📐 对齐是关键且成本极低：用检测到的 5 个关键点做相似变换，将人脸映射到 112×112 的规范模板；前摄镜像帧需用翻转模板，否则会导致错误接受。
- 🛡️ 活体检测区分真实人脸和照片/屏幕：被动活体（MiniFASNet 风格）零摩擦，仅在匹配成功时运行；主动活体（眨眼/转头）用于高安全场景。
- 🧬 嵌入模型将对齐后人脸映射为向量：SFace（Apache-2.0，128 维）是默认选择；ArcFace 系权重仅限研究使用，商业发布需谨慎许可证。
- 👥 注册时每人采集多张样本并合并为质心，显著提升真实准确率；注册时严格质检（拒绝模糊/小脸/极端角度）；只存向量不存照片，保护隐私。
- ⚖️ 匹配用余弦相似度加阈值和最小领先 margin；阈值是产品决策，需在真实设备/光照下用评估集校准，权衡误拒与误认。
- 🎯 用 5 帧新鲜嵌入合成质心进行搜索，每帧独立投票、取中位数分数，将未知率控制在 4% 以下，错误认人率低至 0.14%（5000 人库）。
- 🔄 结果回传 JS：用 Reanimated 共享值免 JS 线程更新 UI；坐标转换要用 VisionCamera 的转换函数，否则框会飘。
- ⏱️ 性能优化：不必每帧都跑检测——每 N 帧跑检测，中间帧用 IoU 跟踪器；识别命中后缓存并周期复核，极大降低计算量。
- 🧪 真实设备经验：用 release 构建和真实剖析器（Perfetto/Instruments）；jank 可能是屏幕刷新率与相机帧率拍频导致；注意模型原生内存占用；模型加载在 debug/release 行为不同；热降频需动态调帧率。
- 🚀 整个流水线已开源（margelo/face-recognition-demo），可从 GitHub 克隆体验；项目可扩展到活动签到、门禁、KYC 等场景。

---

### [](https://flaviocopes.com/storybook-tutorial/)

**原文标题**: [Storybook tutorial: build and test UI components in isolation](https://flaviocopes.com/storybook-tutorial/)

本文介绍了如何用 Storybook 在 React 项目中隔离开发 UI 组件，通过 stories 模拟各种状态（加载、错误、长内容等），并加入交互测试、可访问性检查和 CI 集成，让隐藏 UI 状态变得易于创建、检查和测试。

- 📦 安装 Storybook：在现有 Vite React 项目中运行 `npm create storybook@latest`，自动检测框架、创建 `.storybook` 并生成示例 stories，然后通过 `npm run storybook` 启动。
- 🧩 构建组件：创建 `UserCard.jsx` 作为真实应用使用的组件，stories 必须直接引用该组件，避免制作 Storybook 专用副本。
- 📝 编写第一个 story：`UserCard.stories.jsx` 默认导出 meta（title、component、args），命名导出 story；`fn()` 作为间谍函数，记录按钮交互并支持测试断言。
- 🎭 模拟重要状态：为无头像、加载中、错误、超长内容分别创建 story，无需等待真实 API 或修改数据库，即可重现关键 UI 状态。
- 🎛️ 使用控件：Storybook 根据 args 自动生成 Controls 面板，可实时编辑 props；当推断不足时，用 `argTypes` 补充控件类型和描述。
- 🧩 添加装饰器：用 decorator 包裹 story 以提供布局或上下文，全局装饰器放在 `.storybook/preview.js`；复用应用所需的 providers 和全局 CSS，但不要重建整个应用外壳。
- 🧪 编写交互测试：通过 `play` 函数使用 `canvas.getByRole` 和 `userEvent.click` 模拟点击，并用 `expect` 断言回调参数；Interactions 面板帮助调试。
- ⌨️ 测试键盘行为：用 `userEvent.tab()` 验证焦点顺序，用 `keyboard('{Enter}')` 测试回车激活；不要用强制聚焦掩盖 tab 顺序问题。
- ♿ 可访问性检查：安装 `@storybook/addon-a11y` 自动检测对比度、表单标签、ARIA 等问题；但自动检查不能替代真实键盘和屏幕阅读器手动测试。
- 📱 移动和暗色状态：使用 viewport 参数预设手机宽度，比如 `mobile1`；主题变化通过 decorator 添加类或 data 属性，而不是创建单独的暗色组件。
- 🌐 网络边界模拟：组件 fetch 数据时，用 Mock Service Worker 模拟成功、空响应、慢请求和服务器错误，而不是添加生产环境不存在的 `fakeError` prop。
- 🤖 作为测试运行：使用 `@storybook/addon-vitest` 将 stories 转为浏览器测试，CLI 中运行 `npm run test-storybook`；CI 还需安装浏览器并执行 `npm run build-storybook` 捕获静态构建问题。
- ✅ 什么值得创建 story：正常态、加载/空/错误态、重要变体、边界内容、响应式布局、权限差异、交互流程和回归 bug；修复 bug 时先写 story 复现，再保留为回归测试。
- 📂 保持 stories 在组件旁：目录结构如 `UserCard/` 放 `UserCard.jsx`、CSS、stories 和测试文件；stories 是文档和测试的一部分，组件 API 变化时需同步审查。
- 💡 核心收益：Storybook 的主要价值不是侧边栏列表，而是让隐藏 UI 状态变得廉价、可检查、可讨论，并在完整应用中发现前提前测试。

---

### [](https://tanstack.com/blog/introducing-tanstack-markdown-and-highlight)

**原文标题**: [Introducing TanStack Markdown and TanStack Highlight | TanStack Blog](https://tanstack.com/blog/introducing-tanstack-markdown-and-highlight)

TanStack 发布了两款专注于极简与性能的开源库：TanStack Markdown 与 TanStack Highlight。它们针对技术博客、文档及 AI 流式内容而设计，通过“解析与高亮分离”“普通数据结构”“按需语言注册”等理念，将 tanstack.com 文档页传输量从 1.1 MiB 降至约 27 KiB，成功移除原先为隐藏依赖问题而引入的 RSC 架构，目前在官方站点生产环境中使用。

- 📚 推出两个新库：TanStack Markdown（解析 Markdown 为文档树）与 TanStack Highlight（生成语义化高亮 HTML），聚焦技术内容场景。
- 💡 原始痛点：旧方案中单篇文档页传输约 1.1 MiB，其中 358 KiB 仅用于语法高亮；团队决定“让依赖变小”，而非用架构掩盖问题。
- 🔧 解析与高亮彻底解耦：Markdown 解析器输出公开、可序列化的 AST；高亮器独立处理代码；两者通过回调衔接，互不依赖。
- 📦 Markdown 极轻量：解析器约 4.9 KB（gzip），HTML 渲染器与框架适配器约 6.7 KB，零运行时依赖；覆盖常用语法，不承诺所有 CommonMark 边缘特性。
- ⚡ 流式输出简化：可选 stream 扩展每次同步重新解析累积文本，无解析器状态，仅增重 0.2 KB，适合 AI 增量内容。
- 🎨 Highlight 按需加载：空核 1.7 KB，核心+TSX 3.9 KB，全部 25 种语言约 8 KB；无初始化 Promise、无自动语言检测，未知语言回退为纯文本。
- 🌐 支持 Web 语言嵌套：HTML 中的 `<script>`/`<style>` 可委派给已注册的 JavaScript/CSS 语法，Vue/Svelte 等也能复用 TypeScript 高亮。
- 🌓 主题与代码树分离：只输出 `th-*` 语义类与一个代码树，主题通过 CSS 变量注入，暗色/亮色切换无需重新高亮。
- 🧪 测试体系作为核心保障：已提交 333 个语料样本（来自 2940 个文档文件），覆盖 token 保真度、确定性 HTML、导出、体积预算、吞吐量及回归测试。
- 🚀 生产验证：tanstack.com 文档与博客已采用两库，替换原有 RSC 内容管线，传输量降至约 27 KiB，同时保留性能收益。
- ⚠️ Alpha 声明：API 契约仍可能变动；若你只需将已知技术内容渲染为网页，可尝试并用自身语料测试，反馈未知边角案例。

---

### [TanStack Markdown](https://tanstack.com/markdown/latest)

**原文标题**: [TanStack Markdown](https://tanstack.com/markdown/latest)

这段内容介绍了一个名为TanStack的Markdown解析库，其设计理念聚焦于“一次性解析、持久化AST、流式处理AI输出、精简语法范围、默认安全、体积可控，以及将语法高亮等重功能外部化”。

- 📄 **核心定位**：将Markdown解析为可序列化的AST，实现“一次解析，多端渲染”（HTML/React/Octane），让内容不绑定在某个特定渲染器上。
- 🌳 **AST作为产品核心**：解析结果可缓存、可索引、可检查，渲染器可以更换，但文档树保持不变，形成持久化内容层。
- 🧩 **流式AI响应支持**：解析器无状态，追加文本后同步重新解析，无需协调增量状态；已完成的块保持稳定，未完成标记不干扰输出。
- 🎯 **刻意精简语法**：专注技术文档常用元素（标题、列表、表格、脚注、代码块、链接、frontmatter等），不陷入所有CommonMark边缘情况或重型插件生态。
- 🔒 **边界安全默认开启**：原始HTML默认转义、可执行URL被剥离，文本、属性和代码在渲染时编码；不安全行为需显式选择加入。
- 📦 **轻量与按需加载**：通过拆分入口点保持解析器、渲染器、框架适配器独立；解析器仅4.9KB，远小于marked（12.5KB）、unified（36.8KB）和markdown-it（52.7KB）。
- 🎨 **语法高亮外部化**：代码围栏仅保留语言和元数据，由配套的TanStack Highlight在渲染阶段处理，核心不隐式引入语法引擎。
- 🤝 **社区与赞助**：提供Gold/Silver/Bronze及OSS Sponsor伙伴层级，赞助者可获得私有Discord频道、优先问题请求和直接支持。

---

### [错误](https://tanstack.com/charts/latest)

**原文标题**: [Error](https://tanstack.com/charts/latest)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='tanstack.com', port=443): Max retries exceeded with url: /charts/latest (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [](https://thoughtbot.com/blog/sign-in-with-google-for-react-native)

**原文标题**: [
        Sign in with Google for React Native
    ](https://thoughtbot.com/blog/sign-in-with-google-for-react-native)

overview summary  
- 📱 发布了一款全新的 React Native Google 登录库 `@thoughtbot/react-native-social-auth`，基于 Android Credential Manager 和最新 iOS GoogleSignIn SDK 构建。  
- 🔑 提供符合 Google 品牌规范的按钮组件、Expo 配置插件以及 TypeScript 优先的 API，简化集成流程。  
- ⚙️ Google 正推动认证现代化：Android 弃用旧版 GoogleSignInClient，推荐迁移至 Credential Manager；iOS SDK 新增 App Check 与自定义 nonce 支持，提升安全性。  
- 🧩 现有 React Native 库仍基于旧代 Android API 或旧版 iOS SDK，无法支持新特性如底部弹窗、自动登录与结构化错误处理。  
- 🚀 该库旨在填补这一空白，让开发者轻松接入最新平台能力，并附带了完整的使用示例代码。

---

### [OverflowGuard — 围绕内容构建，而非断点](https://overflowguard.dev/)

**原文标题**: [OverflowGuard — Build around content, not breakpoints](https://overflowguard.dev/)

您尚未提供需要总结的文本内容。请发送文章或段落，我会按照模板为您生成中文概述和带表情符号的要点列表。

---

### [](https://github.com/mobxjs/mobx/releases/tag/mobx-react%4010.0.0)

**原文标题**: [Release mobx-react@10.0.0 · mobxjs/mobx · GitHub](https://github.com/mobxjs/mobx/releases/tag/mobx-react%4010.0.0)

本次发布是 MobX 生态的一次重要更新，正式推出 MobX 7、mobx-react-lite 5 和 mobx-react 10，旨在清理过时 API、拥抱现代 React 与 Proxy 运行时，并显著减小打包体积。

- 📦 发布 mobx-react@10.0.0，同时发布 MobX 7 和 mobx-react-lite 5；ESM 生产包 gzip 从 17.02 KiB 降至 13.96 KiB，tree-shaken 最小示例为 10.32 KiB。
- 🧹 MobX 7 是清理版，聚焦现代运行时和装饰器模型，移除 ES5/non-proxy 回退，始终使用 Proxy 支持的 observable 对象和数组。
- 🚫 不再支持 `configure({ useProxies: ... })` 以及 `observable`、`observable.object`、`observable.array` 的 `proxy: false` 选项，也不再支持旧式装饰器。
- 🏷️ 命名空间注解和比较器属性改为命名导出（如 `observable.ref` → `observableRef`、`computed.struct` → `computedStruct` 等），以减小包体积。
- 🔍 移除公共 `trace` API，建议改用 `toJS`、`getDependencyTree`、`getObserverTree`、`spy` 或 `mobx-log` 进行调试。
- ⚛️ mobx-react-lite 5 和 mobx-react 10 要求 MobX 7 和 React 18+；lite 负责函数组件和 `forwardRef`，mobx-react 负责类组件和 Stage 3 `@observer` 类装饰器。
- 🧩 两个包推荐公开的 React 绑定表面为：`observer`、`Observer`、`useLocalObservable`、`enableStaticRendering`、`isUsingStaticRendering`。
- 🗑️ 移除一系列已弃用 API：`Provider`/`inject`/`MobXProviderContext`（改用 `React.createContext`）、`disposeOnUnmount`、`PropTypes`、`useObserver`、`useLocalStore`、`useAsObservableSource`、`useStaticRendering` 等。
- 🧼 移除 React batching 相关导入（`observerBatching`、`isObserverBatched`、`batchingForReactDom` 等），React 18+ 渲染器会自动处理 batching。
- ⚠️ 弃用 `observer(fn, { forwardRef: true })` 写法，应改为将已创建的 `React.forwardRef(...)` 组件传给 `observer`；同时移除旧式函数组件 `contextTypes` 处理。
- 🔗 补丁更新：依赖 `mobx-react-lite@5.0.0`。

---

### [发布 5.2.0 · mrousavy/react-native-vision-camera · GitHub](https://github.com/mrousavy/react-native-vision-camera/releases/tag/v5.2.0)

**原文标题**: [Release Release 5.2.0 · mrousavy/react-native-vision-camera · GitHub](https://github.com/mrousavy/react-native-vision-camera/releases/tag/v5.2.0)

react-native-vision-camera 发布了 v5.2.0 版本，主要带来了 GPU 图像缩放器的新缩放模式、SkiaCamera 组件的功能增强，并修复了预览分辨率、麦克风检测及 Nitro 相关问题。

- ✨ 为 GPU Resizer 新增 `'stretch'` ScaleMode（#4085）
- ✨ 为 `<SkiaCamera>` 添加 `targetResolution` 属性（#4089）
- ✨ 为 `<SkiaCamera>` 添加 `zoom`、`exposure` 和 `torchMode` 控制（#4101）
- 🐛 为 `focus(…, { adaptiveness: 'locked' })` 补充 Harness 测试（#4078）
- 🐛 修复预览分辨率协商偏向 4k 的问题（#4083）
- 🐛 简化麦克风检测与添加逻辑（#4092）
- 🐛 升级 Nitro 至 0.36.3 以修复 `@FastNative` 问题（#4102）

---

### [](https://github.com/rphlmr/react-router-hono-server/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · rphlmr/react-router-hono-server · GitHub](https://github.com/rphlmr/react-router-hono-server/releases/tag/v3.0.0)

react-router-hono-server 发布了 v3.0.0 版本，该版本将 React Router 升级到 v8，并更新了 Vite 配置和包路径以保持兼容，同时获得了社区反馈。

- 🚀 发布 v3.0.0 最新版本
- ⭐ 重大变更：升级至 React Router v8
- 🔧 更新 Vite 配置和包路径以支持 React Router v8
- ❤️ 获得 1 个社区爱心反应

---

### [无](https://expo.dev/blog/how-to-build-mobile-apps-with-ai-the-three-tools-that-actually-matter?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [None](https://expo.dev/blog/how-to-build-mobile-apps-with-ai-the-three-tools-that-actually-matter?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

我没有收到您提供的内容，请重新发送需要总结的文本，我会按照模板为您提炼要点。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

Tiger Data（Timescale旗下）为任意规模的时序工作负载提供Postgres数据库服务，强调超大规模数据处理能力、企业级安全合规、弹性扩展与快速部署，并面向物联网场景受到数千家公司信赖。

- 📊 规模能力：支持每天处理3万亿条指标、存储3PB数据，总计达1千万亿数据点
- 🎁 优惠活动：新账户可获$1000额度，30天有效，无需信用卡
- 🏢 客户信任：被数千家物联网企业广泛采用
- ⚙️ 弹性扩展：读写分离，副本节点最多10个，SSD/S3分层存储实现低成本无限扩展
- 💰 节省成本：计算与存储分离，可独立扩展，避免为空闲容量付费
- 🔒 高可用性：多可用区集群、自动故障切换、时间点恢复与跨区域备份
- 🛡️ 企业级安全：符合SOC 2、HIPAA、GDPR，支持加密、SSO、RBAC与审计日志
- 📈 深度可观测：查询下钻与仪表盘，可集成CloudWatch、Datadog、Prometheus
- ⚡ 快速启动：几分钟内完成数据库部署，支持SQL、CLI、Terraform、Cursor或Claude Code管理
- 🔗 生态集成：兼容主流云提供商及广泛Postgres生态
- 🕐 企业支持：提供合同化SLA、区域数据隔离、合规认证，以及7x24小时全球专家支持

---

### [](https://microcharts.dev/)

**原文标题**: [microcharts â Word-sized charts for React. Tiny sparklines & micro charts.](https://microcharts.dev/)

Microcharts 是一个 React 微型图表库，专为在句子、表格单元格、KPI 卡片和打印报告等小空间内呈现数据而设计。它提供 106 种图表类型，包体积中位数仅 5.24 kB，零依赖，并具备完善的无障碍支持和主题系统。

- 📦 体积极小：中位数 5.24 kB，最大不到 7 kB，共 106 种图表，分为 4 个集合。
- 🔧 零依赖，仅需 React 作为 peer dependency；安装命令：`pnpm add @microcharts/react`。
- ♿ 无障碍完善：每张图表一个 tab 停靠点，方向键浏览，alt 文本由数据自动生成，不依赖颜色传达信息。
- 🧩 统一 API：传入 `data` 即可渲染，`domain`、`color`、`title` 在所有图表中含义一致，类型完备。
- 📝 可在句子、表格、KPI 卡片和打印报告中使用；静态渲染时客户端 JS 为 0 kB。
- 🤖 支持“图表围栏”：模型只需写文本，闭合后就能渲染出对应组件，适合 AI 生成。
- 📊 提供 106 种图表类型，包括 sparkline、sparkbar、delta、bullet、activity-grid 等，替代小尺寸下不可读的饼图、仪表盘、小提琴图。
- 📏 当图表需要坐标轴和网格线（约 200 px 以上）时，建议使用 Recharts 等完整工具包；Recharts 核心包约 106 kB。
- 🛡️ 坏数据也能渲染：NaN、空数组、负数等都有合理表现，页面无需 try/catch。
- 🎨 主题系统：`defineTheme` 传入一个强调色，自动生成色盲安全色阶和暗色版；正负语义色固定为绿/朱红。
- 🖥️ 七个示例应用覆盖全部 106 种图表类型，并展示不同主题风格（现代、编辑、等宽等）。

---

