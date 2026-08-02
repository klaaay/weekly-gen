### [](https://aurorascharff.no/posts/experimenting-with-rsc-for-performance-and-ux-in-nextjs/)

**原文标题**: [Experimenting with RSCs for Performance and UX in Next.js | Aurora Scharff](https://aurorascharff.no/posts/experimenting-with-rsc-for-performance-and-ux-in-nextjs/)

本文围绕 Next.js 16.3 中的 React Server Components 与 Server Functions 实践，展示了三种交互模式：URL 驱动的加载更多、保持静态壳的流式搜索，以及服务端按需渲染的消息预览，核心思路是尽可能把数据获取和渲染留在服务端，只在必要时使用客户端代码。

- 🚀 核心原则：把数据获取与渲染放在服务端，让浏览器直接接收渲染结果，减少客户端逻辑和额外请求。
- 🔗 加载更多按钮：客户端只负责把 `?page=` 写入 URL，服务端按页码渲染多个带 `Suspense` 边界的页面，新内容流式插入而不影响已有列表。
- 🔄 URL 驱动的取舍：刷新或分享链接可保留页码，但服务端会重新渲染之前的页，响应中会重复发送已展示的内容。
- 🔍 搜索输入框：输入组件只写 URL 不读 query，因此能留在静态 shell 中即时渲染；通过内联脚本在 HTML 解析时预填值，并用 layout effect 同步软导航。
- 📡 流式搜索结果：将 `searchParams` 的 promise 放在 `Suspense` 内解析，结果以 `children` 传给客户端组件；配合 transition 的 `isPending` 让旧结果变暗，提供即时反馈。
- 💬 消息预览：客户端 composer 通过 Server Function 按需请求服务端渲染的 JSX，并用 `use()` 读取，保证预览与真实帖子完全一致，Shiki 高亮也留在服务端。
- ⚠️ 客户端预览替代方案：可把 Server Function 返回的页面节点保存在客户端 state 中实现 Paginator，每次只请求新页，但无法共享或刷新保留，更适合临时预览。
- ✨ 实践要点：用 `children` 传递服务端输出、把分页/查询状态放在 URL、用独立 `Suspense` 边界流式更新、用 transition 提供本地反馈，从而最大化静态 shell 并保持流畅体验。

---

### [共享存储桶 | Tigris 对象存储文档](https://www.tigrisdata.com/docs/buckets/sharing/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-08-02)

**原文标题**: [Sharing Buckets | Tigris Object Storage Documentation](https://www.tigrisdata.com/docs/buckets/sharing/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-08-02)

overview summary
- 🔑 分享桶给组织内用户：需为桶拥有者或管理员，通过 Dashboard 的 Share 按钮，选择用户并分配只读或编辑角色。
- 👥 角色权限：Read Only 只能读取内容，Editor 可读写；共享用户可为桶创建访问密钥，撤销共享后密钥立即失效。
- 🧑‍🤝‍🧑 分享给团队：可一次分享给整个团队，新加入的成员自动获得访问权限；移除成员或撤销团队分享后，对应访问立即失效。
- 🏢 分享给整个组织：通过“Organization Access”设置权限，所有组织用户都能访问并可创建密钥，撤销后密钥不再有效。
- 🌐 分享给外部组织：需外部用户提供以 `tid_` 开头的访问密钥 ID，添加为外部 ID，角色固定为 External，外部用户可用该密钥访问桶。
- 🛡️ 外部用户权限：拥有类似 Editor 的广泛操作权限（如上传、下载、复制、删除对象及多项配置操作），但没有删除桶等管理权限。

---

### [](https://github.com/react/react/pull/37143)

**原文标题**: [Add ReactDOM `browser()` API by gnoff · Pull Request #37143 · react/react · GitHub](https://github.com/react/react/pull/37143)

React 核心团队合入了一个新 PR，为 react-dom 新增 `browser()` API，用于表达“组件应在服务端挂起、在浏览器中渲染”的意图，从而规范化“仅浏览器”渲染模式。

- 🆕 新增 `browser()` API：从 `react-dom` 导入，返回一个“可用”（usable）对象，在 SSR 渲染时会报错，在浏览器渲染时正常解析。
- 💻 客户端专用特性：此 API 在 `react-server` 环境中不可用，因为“浏览器”概念不适用于通用 React，因此归属于 `react-dom`。
- 🔄 典型用法：通过 `use(browser())` 配合 `Suspense`，让组件在服务端进入挂起状态，并在浏览器端渲染实际内容，避免服务端渲染无关组件。
- ⚠️ 使用限制：`use(browser())` 必须在 Suspense 边界内使用，否则会因其无法从根恢复而报错，未来可能放宽该限制。
- 🧠 实现机制：将该场景建模为“可恢复错误”，同时刻意抑制错误日志；也支持 `abort(browser())` 以中止服务端流式渲染，且不会在浏览器水合时记录错误。
- 🔖 设计权衡：选择“可用的对象”而非 `useBrowser()` hook，是为了支持按条件调用；也避免了直接抛出导致被任意捕获的风险。
- 🚦 特性开关：实现带有 kill switch，可在稳定版发布前快速禁用；目前以无前缀形式进入代码库。
- 📦 体积影响：PR 包含 sizebot 报告，多个 bundle（如 react-dom 生产版）有 0.02%–3.78% 不等的体积增加。

---

### [指南：离线支持 | Next.js](https://preview.nextjs.org/docs/app/guides/offline-support)

**原文标题**: [Guides: Offline support | Next.js](https://preview.nextjs.org/docs/app/guides/offline-support)

Next.js 的实验性离线支持功能可在网络断开时自动挂起并重试导航、数据获取和 Server Action，避免 UI 报错，并可通过 useOffline hook 向用户反馈连接状态。

- 🧪 实验性功能：需在 next.config.ts 中启用 `experimental.useOffline`，目前不建议用于生产环境。
- 🌐 断网不报错：软导航、RSC 数据获取、预取或 Server Action 失败时保持 pending，连接恢复后自动重试。
- ⏳ UI 呈现加载态：请求挂起时显示 Suspense 回退或 pending transition，效果与慢服务器一致。
- 📡 useOffline hook：返回离线状态，触发条件包括浏览器 offline 事件或请求失败；比 `navigator.onLine` 更可靠。
- 🧩 示例应用：构建实时指标页面和 ping 表单，演示默认行为与带反馈的 UI。
- ⚙️ 建议配合 Cache Components 和 Partial Prefetching，使 App Shell 成为离线预取单元。
- 🔄 Server Action 自动重试：离线调用不再抛出异常，连接恢复后自动执行并 resolve，无需手动 try/catch。
- 🧪 测试方法：使用 `next build && next start`，通过 Chrome DevTools 或 Firefox 网络模拟离线状态。
- 📄 无 Cache Components 时：route-level 的 `loading.tsx` 也能提供相同的离线行为。
- 🔗 相关资源：可参考 useOffline hook API、配置项、loading.tsx 约定及 PWA 指南。

---

### [如何在生产环境中发现 Next.js 内存泄漏](https://xabierlameiro.com/blog/nextjs/nextjs-memory-leak-in-production)

**原文标题**: [How to find a Next.js memory leak in production](https://xabierlameiro.com/blog/nextjs/nextjs-memory-leak-in-production)

本文介绍了如何定位 Next.js 生产环境中的内存泄漏问题，详细分析了三个框架级泄漏的成因、特征与排查方法，并分享了作者在 Vercel 上遇到的 504 超时案例及自动化诊断工具，最后给出了实用的检查清单。

- 🚨 已发现三个框架级内存泄漏：路由 LRU 缓存不计键（#94890）、RSC 渲染树随请求保留（#94919）、中间件 setTimeout id 永不释放（#95094），覆盖 Next.js 15.5 至 16.3。
- 📈 泄漏 1 的特征：随唯一 URL 数量缓慢漂移，retainer 为 `LRUNode`；可通过 CDN 规范化垃圾 URL 缓解。
- 🌊 泄漏 2 的特征：随流量增长，客户端中途断连时加剧，Node 22/24 上更严重，retainer 为 `reactServerStream`；建议精简 RSC 负载或分页。
- ⏳ 泄漏 3 的特征：中间件中未显式清除的 `setTimeout` 造成步进式增长，retainer 为沙箱 `TimeoutsManager`；在回调中调用 `clearTimeout` 可规避。
- ☁️ 在 serverless 环境中，内存泄漏常以 504 FUNCTION_INVOCATION_TIMEOUT 而非 OOM 形式出现，需要分析的是耗时而非内存。
- 📊 诊断方法：绘制 `heapUsed`、`rss`、`external` 曲线，对照唯一 URL、流量和特定路由；用 `NODE_OPTIONS='--inspect'` 抓堆快照并对比 retainers。
- 🧠 作者自身的 504 并非泄漏，而是 MDX 解析的 O(N²) 算法问题；通过模块级缓存将构建从 17.5 分钟降至 34 秒，页面预渲染从约 32 秒降至 1.6 秒。
- 🛠️ 自动化工具 `next-leak`（`npx next-leak . --quick`）可自动驱动负载、强制 GC、判断增长形状并命名 retainer，几分钟内复现泄漏诊断。
- ⚠️ 真实测量提示：#94890 很容易复现，#94919 则可能在快速响应的最小复现中不显现，需用真实最重页面测试。
- ✅ 检查清单：先看 retainer 而非猜测；先关联相关指标再归因；`--max-old-space-size` 无法根治单调泄漏；serverless 上优先分析时间消耗。

---

### [](https://github.com/evilrabbit/lifeline)

**原文标题**: [GitHub - evilrabbit/lifeline: A timeline component for the stories that unfold over time. Ships as a shadcn registry. · GitHub](https://github.com/evilrabbit/lifeline)

Lifeline 是一个用于展示随时间展开的故事（如职业、公司、旅程）的 shadcn 时间线组件，支持桌面端水平滚动与移动端垂直滚动，并且以 registry 方式分发，让开发者获得完全可控的源码。

- 📜 在单一轨道上呈现里程碑：桌面端由滚动控制水平推进，移动端自动切换为垂直滚动。
- 🧩 以 shadcn registry 形式安装，源码直接进入项目，所有缓动、断点和样式类均可自由修改。
- 📦 提供多种安装选项：完整页面、外壳（shell）、个人/公司/旅程数据模板、纯组件系统及主题切换器。
- ⚙️ 安装后自动配置 components/lifeline/、lib/lifeline-data.ts、CSS 关键帧，并安装 lucide-react 和 next-themes。
- 🚀 通过 defineLifeline 定义数据，传入 birthYear 和 milestones 即可渲染完整时间线。
- 🖼️ 里程碑支持事件文本、悬停/点击图片、视频、常驻照片卡片、徽章、公司图标、人物行及年龄覆盖。
- 🧭 核心 props 有 markers、birthYear、title、mode、className；mode 支持 "auto"、"page"、"embed"，适配整页或嵌入场景。
- 🖱️ 嵌入模式只借用滚轮交互而不锁定页面滚动，并支持键盘方向键以及 prefers-reduced-motion。
- 📏 可通过 data-site-nav-logo 和 data-site-nav-inner 属性与网站导航对齐，使时间线宽度与页面内容一致。
- 🌐 需要 Next.js App Router 与 Tailwind CSS，兼容 Tailwind v3/v4，采用 MIT 许可证。

---

### [](https://github.com/TheOrcDev/shadscan)

**原文标题**: [GitHub - TheOrcDev/shadscan: Deterministic UI audits for shadcn apps, built for your terminal, your CI, and your AI agent. · GitHub](https://github.com/TheOrcDev/shadscan)

Shadscan 是一个针对 React shadcn 应用的确定性 UI 审计工具，通过 59 条静态规则从 0 到 100 评分并展示每项发现的证据，支持本地命令行、CI 集成、AI Agent 工作流以及 Web 扫描，帮助开发团队发现容易被忽略的界面细节。

- 🔍 审计范围：检查命令菜单、主题快捷键、路由状态、无障碍控件、表单反馈、元数据和移动端行为等易被推迟的产品细节
- ⚡ 快速开始：通过 `pnpm dlx @shadscan/cli`、`npx` 或 `bunx` 即可运行，默认扫描当前目录，也可指定目标路径
- 🛡️ 安全默认：扫描是确定性且只读的，不启动应用、不修改文件、不调用 AI 模型、不上传源码，也无需应用密钥
- 📋 报告格式：支持交互式、JSON、prompt、CI 等输出模式，报告分为修复（Fixes）、决策（Decisions）、建议（Advisories）和不适用（Not applicable）四类
- 🚀 GitHub Action：可直接作为复合 Action 使用，写入 job summary、强制分数下限，并可创建或更新包含 AI 修复方案的 issue
- 🤖 Agent 交接：`--prompt` 生成粘贴即用的修复计划，包含优先级分组、规则 ID、证据、建议修复和验收标准；`--apply` 可显式启动已安装的编码 Agent
- 📊 评分模型：六类加权类别（基础、交互、状态、无障碍、表单与数据输入、生产优化），高/中置信度失败扣分，低置信度作为不影响分数的建议
- 🧩 框架兼容：支持 Next.js App Router、Pages Router、混合模式、React Router、TanStack Start、Laravel+Inertia、Astro、Vite React 及通用 React 应用
- 📦 Monorepo 支持：自动发现并审计工作区中所有 React 应用并合并评分，库包仅扫描不计分，支持 pnpm、npm、yarn、bun 等包管理器
- 🌐 Web 扫描与托管 API：通过 Web 扫描器可在浏览器中审计公共 GitHub 仓库，另有版本化托管 API 供 Agent 和服务集成
- 🔧 开发与许可证：仓库使用 Node.js 24 和 pnpm 11.15.1 开发，发布的 CLI 兼容 Node.js 18，项目基于 MIT 许可证

---

### [](https://github.com/RoyBkker/next-nuke)

**原文标题**: [GitHub - RoyBkker/next-nuke: npkill for Next.js — nuke bloated .next folders and reinstall a fresh instance. Monorepo & pnpm aware. · GitHub](https://github.com/RoyBkker/next-nuke)

next-nuke 是一个用于重置 Next.js 项目构建状态的命令行工具，支持多仓库和 pnpm，能安全删除 .next、node_modules 等目录，并可选重新安装依赖。

- 🧹 一条命令即可重置 Next.js 构建状态，自动查找仓库中所有 .next 目录并显示可回收的磁盘空间。
- 🔄 支持 `--full` 模式：删除 node_modules 与 .next 后自动识别包管理器并重新安装依赖。
- 🚀 专门解决 Turborepo 缓存回填问题，`--turbo` 可同时清除 .turbo 缓存，避免“假干净”重建。
- 📁 多仓库感知：在仓库根目录运行可发现所有应用的 .next，并提供清单让你选择要重置哪些应用。
- 🛡️ 安全设计：只删除白名单目录（.next、node_modules、.turbo 等），拒绝在 home/root 运行，不追踪符号链接，支持 `--dry-run` 预览和确认提示。
- 🔏 每个版本均通过 npm OIDC 可信发布，带有可验证的 GitHub Actions 构建来源证明。
- ⚙️ 常用命令覆盖全面：`--cache` 只清缓存、`--full` 删除并重装、`--build` 清理后构建、`--exclude` 跳过指定路径、`-y` 跳过确认用于 CI。
- 🔍 与 npkill 的区别：npkill 适合跨项目批量清理磁盘，next-nuke 专注于“重置当前项目”，并额外提供重装依赖和 Turbo 缓存处理。
- 📦 要求 Node.js 20 以上，代码采用 MIT 许可证。

---

### [](https://github.com/mobxjs/mobx/releases/tag/mobx%407.0.0)

**原文标题**: [Release mobx@7.0.0 · mobxjs/mobx · GitHub](https://github.com/mobxjs/mobx/releases/tag/mobx%407.0.0)

overview summary  
MobX 7 是一次重大版本更新，主打現代化執行環境與精簡套件，移除長期棄用的相容路徑，並同步推出 mobx-react-lite 5 與 mobx-react 10，以對應 React 18+ 的生態。

- 📦 套件體積明顯下降：ESM production gzip 從 17.02 KiB 降至 13.96 KiB，最小 tree-shaking 範例為 10.32 KiB gzip。
- 🚫 全面使用 Proxy 實作 observable 物件與陣列，移除 ES5/non-proxy fallback，也不再支援 `configure({ useProxies })` 或 `proxy: false` 選項。
- 🗑️ 不再支援 legacy decorators，專注於現代 decorator 模型。
- 🔄 命名空間屬性改為 named exports 以減少 bundle：例如 `observable.ref` → `observableRef`、`computed.struct` → `computedStruct`、`comparer.identity` → `compareIdentity` 等。
- 🔍 移除公開 `trace` API，建議改用 `toJS`、`getDependencyTree`、`getObserverTree`、`spy` 或 mobx-log 套件除錯。
- ⚛️ mobx-react-lite 5 與 mobx-react 10 皆要求 MobX 7 與 React 18 以上版本。
- 📄 mobx-react-lite 負責 function components；mobx-react 則包裝 mobx-react-lite，額外支援 class components 與 Stage 3 `@observer` class decorator。
- ❌ 移除 `Provider`、`inject`、`MobXProviderContext`、`disposeOnUnmount`、`useObserver`、`useLocalStore`、`useAsObservableSource` 等 API，並改用 React 原生或明確同步方式。
- 🆕 React 綁定的建議公開面收斂為 `observer`、`Observer`、`useLocalObservable`、`enableStaticRendering`、`isUsingStaticRendering`。
- 🧹 移除 React batching imports（含 React Native deep import），因 React 18+ renderer 已自行處理 batching。
- 🐛 補丁變更：縮短 minified error URL，以降低 production bundle size。

---

### [](https://octanejs.dev/)

**原文标题**: [Octane — React's programming model, compiled](https://octanejs.dev/)

Octane 是一个面向 React 生态的编译型框架，继承 Inferno 的性能优先理念，通过预先编译消除虚拟 DOM、“hooks 规则”和手写依赖数组，同时保持 React 熟悉的编程模型，支持逐步迁移和广泛生态绑定，并提供 CLI 与诊断工具。

- ⚛️ **编译型 React 继任者**：Octane 是 Inferno 的继任者，将 React 的 hooks、Suspense 和 actions 提前编译，没有虚拟 DOM，也没有“rules of hooks”。
- 🔧 **编译器自动推断依赖**：开发者无需手动维护依赖数组，编译器会跟踪 effect、memo 和 callback 实际捕获的内容；hooks 可以放在条件或提前返回之后。
- ⚡ **性能表现领先**：基准测试显示 Octane 几乎全面优于 React 19 和 Preact 10，与 Solid、Svelte、Vue Vapor 等现代框架互有胜负，综合几何平均约 1×（对比 React 19 为 2.5×）。
- 📦 **支持渐进式迁移**：可保留现有 TSX，逐个将组件改为 `.tsrx`；通过 `OctaneCompat` 组件还能在 React 19 应用中嵌入编译后的 Octane“孤岛”，无需重写。
- 🧩 **熟悉且兼容**：Hooks、memo、context、portals、transitions、actions、受控表单和 Suspense 行为符合直觉；事件为原生事件，refs 只是 props。
- 🔌 **52 个生态绑定**：覆盖状态、数据、路由、UI、表单、图表、3D 等常用库，如 Three.js 通过 `@octanejs/three` 提供 React Three Fiber 的移植版。
- 🛠️ **CLI 工具链完善**：提供 `octane init`、`octane doctor --fix`、`octane add`、`octane explain`、`octane mcp add` 等命令，便于脚手架搭建、问题诊断和 AI 辅助。
- 🔍 **诊断静默问题**：`octane doctor` 检查重复运行时、JSX import source、tsc 配置、`.tsrx` 通配符声明等问题，避免配置错误导致 hooks 或 context 静默失效。
- 🧪 **测试覆盖广泛**：运行时、编译器、SSR 和绑定共有 11,500+ 次测试执行，核心套件包含 3,900+ 个独立用例；React 衍生覆盖逐项追踪。
- 🚀 **SSR 和异步优化**：独立的 `use()` 调用可同时启动，嵌套请求提前预热，流式 SSR 按边界就绪即发送。

---

### [](https://infrequently.org/2026/07/state-management/)

**原文标题**: [The Absolute State of Management - Infrequently Noted](https://infrequently.org/2026/07/state-management/)

## 概述总结

本文尖锐批判了 React 生态中“状态管理”（state management）一词的滥用。作者指出，诸如 MobX、Redux、Zustand、Recoil 等主流库本质上并不“管理”状态，它们只是传播、过滤或缓存状态更新，在概念上等同于事件总线或发布/订阅系统。真正的状态管理需要内置时间与顺序概念（如向量时钟），才能处理冲突解决、离线同步与实时协作。文章推荐了 Y.js、Zero、Fluid 等基于 CRDT 或 OT 的现代方案，认为这才是真正“管理”状态的工具，并呼吁业界正视这一概念混淆。

- 📛 “状态管理”一词是 React 时代最刺耳的语言滥用之一，概念混乱至极
- 🔄 MobX、Redux、Zustand、Recoil、XState、Apollo、Jotai 等众多库都在声称“管理状态”，但彼此矛盾
- 🤔 文章提出三元悖论：React 要么是状态管理系统（则无需额外库），要么是不合格的状态管理系统（则不该信任它），要么根本不是（则不该假装）
- 📡 这些库实际上只是“局部传播”状态变更通知，本质等同事件总线与发布/订阅系统，并未真正“管理”任何东西
- ⏳ 状态管理与状态传播的核心区别在于时间维度——真正的管理意味着随时间正确应用变更并解决冲突
- 🕰️ 纯传播系统缺乏时间与排序概念，面对多来源、多频率的更新时极易崩溃，乐观 UI 更新也会变成负担
- 🌐 跨时间管理数据与跨机器管理数据本质是同一问题：未来重启的本地应用等同于一台全新计算机上的应用
- 🧭 区分真假状态管理的关键标志：内部是否使用向量时钟（vector clocks）等时间与顺序元数据机制
- 🏗️ 真正管理状态的系统（如 CRDT、操作变换 OT、Prolly Trees）在前端讨论中仍然罕见
- 🚀 实用方案已经成熟：Y.js（CRDT 文本编辑）、Zero（Replicache 继任者，数据同步与实时协作）、Fluid（微软开源，基于 OT）
- 💡 这些时间感知系统天然支持实时协作与离线优先（local-first）开发，是“免费的午餐”
- 🔧 PouchDB、RxDB、Replicache 等虽涉足同步，但冲突处理策略各有不足，仅作参考
- 🎯 作者呼吁：承认“状态管理”的说法是错的，并采用真正能管理时间与冲突的工具——这是今天就能实现的未来

---

### [](https://backstage.orus.eu/react-composition-patterns-at-orus/)

**原文标题**: [Props, Composers, and Providers: the composition pattern we're converging on | Orus Engineering Blog](https://backstage.orus.eu/react-composition-patterns-at-orus/)

这篇文章介绍了 React 前端中一种渐进的组件组合模式，将其视为“阶梯”：从最简单的 props 出发，只有在遇到具体痛点时，才逐级上升到复合组件、Composer/Providers，再到提升状态。作者强调了默认采用低层级方案、避免过度抽象，并通过命名约定让代码意图更清晰。

- 📍 团队因 props 层层透传、组件职责过重等问题，决定统一采用“组合阶梯”模式，并作为应对复杂度的准则。
- 🪜 阶梯共有四级：普通 props、复合组件、Composer 与 Providers、提升状态；每一级都有收益和成本（引入间接性）。
- 🟢 第一级“普通 props”：可复用的 UI 应只是 props 的函数，大多数组件应停留在这一级，避免过早抽象。
- 🔧 第二级“复合组件”：当组件为适配各种形态而 props 爆炸时，改为暴露子组件（如 Item.Root、Item.Media），让调用方自由装配，并通过内部 context 协调组内状态。
- 📦 第三级“Composer 与 Providers”：当同一 UI 需要渲染来自不同或可延迟加载的数据源时，用 Context 定义契约，Composer 只消费数据，Provider 则提供可互换的数据来源，测试也更方便。
- 🚀 第四级“提升状态”：当状态需要跨组件边界传递时，用 Provider 暴露 { state, actions } 契约，消除 prop drilling，让布局保持纯净，任何组件都能按需使用操作。
- 🏷️ 命名约定：普通名称表示 props 组件；`Composer` 后缀表示读取契约的消费者；`Provider` 后缀表示填充契约的数据源。
- ⚖️ 何时升级：默认停留在第一级；只有当 props 膨胀、数据源多变或状态真正需要跨界时才升级；不要为了“统一性”“单一数据源”或“局部状态”而盲目升级。
- 🔁 每级在理论上可回退，但实践中回退很麻烦，因此宁可从最低层级开始，遇到具体问题再逐步攀登。

---

### [](https://www.smashingmagazine.com/2026/07/weaponizing-defending-react-flight-protocol/)

**原文标题**: [Weaponizing And Defending The React Flight Protocol: Deserialization Sinks In RSCs — Smashing Magazine](https://www.smashingmagazine.com/2026/07/weaponizing-defending-react-flight-protocol/)

本文深入剖析了React Flight协议作为反序列化系统的安全风险，重点讲解了CVSS 10.0的CVE-2025-55182（React2Shell）远程代码执行漏洞的根因、攻击链、后续相关CVE，并给出了按影响程度排序的实用防御建议与残余风险提醒。

- ✈️ Flight协议：React Server Components使用的流式自定义格式，可传输模块引用、Server Action、Promise等“行为”数据，本质上是反序列化系统。
- 💣 React2Shell（CVE-2025-55182）：CVSS 10.0未认证RCE，根因是getOutlinedModel在解析`$:`路径时缺少hasOwnProperty检查，可沿原型链抵达Function构造函数。
- 🧬 攻击链：利用`$:__proto__:constructor:constructor`遍历、`$@0`获取原始Chunk对象、篡改`.then`劫持Thenable、覆盖`_response._formData.get`，最终通过`$B0` blob处理器触发任意代码执行。
- 🔧 修复方式：缓存原生`Object.prototype.hasOwnProperty`后通过`.call()`验证属性所有权，已随React 19.0.1、19.1.2、19.2.1发布。
- 🗂️ 后续漏洞：包括多个DoS（CVE-2025-55184、CVE-2025-67779、CVE-2026-23864）、源码泄漏（CVE-2025-55183）以及Next.js的`Origin: null` CSRF绕过（CVE-2026-27978）。
- 🥇 首要防御：每个Server Action开头使用Zod/Valibot做完整schema验证（`.safeParse()`），验证前切勿解构或记录参数，避免触发未验证属性访问。
- 📦 server-only包：有效阻止服务器代码被客户端导入，但无法防止返回数据中的敏感字段泄漏；需注意barrel文件导致的边界混淆。
- 🔒 CSRF加固：设置`SameSite=Strict/Lax`、使用显式CSRF token，并绝对不要在`allowedOrigins`中加入`'null'`字符串。
- 🩺 Taint API只是开发期护栏，基于对象引用追踪，spread、序列化等派生操作会绕过；WAF可拦截扫描器，但易被padding或编码绕过，不能作为安全边界。
- 🕳️ 残余风险：MITM可篡改Flight流、Server Action ID可从manifest枚举、加密闭包密钥泄露后可被篡改、供应链中休眠模块可能通过`$I`导入被激活。
- 🏛️ 结论：暴露`$:`、`$@`、`$B`等内部原语属设计失误；仅修补已知漏洞不够，未来需要签名、完整性校验等更强机制，开发者应主动阅读源码并理解信任边界。

---

