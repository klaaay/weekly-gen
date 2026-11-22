### [React Flow 13 - xyflow](https://xyflow.com/blog/react-flow-13-major-release)

**原文标题**: [React Flow 13 - xyflow](https://xyflow.com/blog/react-flow-13-major-release)

React Flow 13 于 2026 年 11 月 16 日发布，距离上一个主要版本已有两年。此次更新不仅升级了底层依赖，还带来了显著的性能优化、开发体验改进、样式与主题能力增强，并同步展示了 React Flow 生态、Strudel Flow 和 Pro 内容的最新进展。

- 📅 **版本发布**：React Flow 13 正式发布，官方提供迁移指南，帮助开发者升级。
- 📈 **生态增长**：npm 月下载量从 2024 年的 100 万增长到本月预计超过 6000 万，约占 React 下载量的 6–8%。
- 🏗️ **应用案例**：Google Stitch、Figma Weave、Supabase 的 database.build 等项目都在使用 React Flow；社区 showcase 欢迎提交作品。
- 🎛️ **Strudel Flow**：基于 Strudel 实时编程语言的音频 playground，支持模块化硬件风格的音乐创作，并新增社区 patch 投稿。
- 💎 **Pro 内容扩展**：Pro 示例和模板已直接上线 reactflow.dev，包含自由手绘、基于 libavoid 的复杂边路由、AI 工作流构建器模板等。
- ⚙️ **升级动因**：主要动机是升级到 Zustand 5，以解决 Vite 8 和现代构建环境的问题，最终演变为一次大幅性能更新。
- 🚀 **性能优化**：拆分单一状态 store，用专用 hooks 管理 options、nodes、edges、selections、connections；新增 useNode/useEdge 精准订阅，减少不必要的重渲染。
- 🧑‍💻 **开发体验**：不再发布 UMD 包，转向 ESM；最低要求 React 18，可利用 React Compiler；包内包含 src/ 和 source maps，支持跳转源码。
- 🧩 **父子节点改进**：父节点不再必须出现在子节点之前；新增 useReactFlow 的 changeParentNode，自动更新父节点边界以包含新子节点。
- 🎨 **样式与主题**：自动检测明暗模式，样式支持分层控制；导出 xy-theme.css，可通过 @xyflow/react/xy-theme.css 引入。
- 🔭 **后续计划**：可通过 React Flow Pro 支持项目开发；官方预告将有针对非 React/Svelte 用户的特别消息。
- 📰 **相关动态**：Vue Flow 加入 xyflow 并发布 Vue Flow 2；Strudel Flow 2 也已发布。

---

### [迁移到 React Flow 13 - React Flow](https://reactflow.dev/learn/troubleshooting/migrate-to-v13)

**原文标题**: [Migrate to React Flow 13 - React Flow](https://reactflow.dev/learn/troubleshooting/migrate-to-v13)

overview summary  
React Flow 13 以性能为核心，主要要求升级到 React 18 和 Zustand 5，并移除 UMD 构建；多数应用只需少量修改即可迁移。重点变更包括变更集处理、拆分 Store hooks、自动颜色模式与 CSS layer、拖拽阈值、视口动画返回值、连接/句柄 API 调整，以及新增 hooks 和辅助函数。

- 🚀 升级前提：需 React 18+ 与 Zustand 5；不再提供 UMD 构建；安装 `@xyflow/react@latest`。
- 🔄 `onNodesChange` 和 `onEdgesChange` 现在接收 `NodeChangeset`/`EdgeChangeset`，用 `changes.applyTo()` 应用变更；不再导出 `applyNodeChanges`/`applyEdgeChanges`。
- 🏷️ 变更类型去掉 Node/Edge 前缀并重命名，如 `NodeDimensionChange` → `DimensionChange`、`NodePositionChange` → `PositionChange`；`NodeChange`/`EdgeChange` 联合类型仍存在。
- 🏪 `useStore`、`useStoreApi` 被专用 Store hooks 取代：`useNodesStore`、`useEdgesStore`、`useViewportStore`、`useOptionsStore`、`useConnectionStore`、`useSelectionStore`；`useStoreApi` 改名为 `useReactFlowStoreApi`。
- 🧮 `use...Store` 不再接收相等性函数，多值选择应使用 `useShallow` 或 `useEqualSelector`。
- 🎨 移除 `colorMode` prop，自动通过 `data-theme` 或 dark/light class 检测；可用 `forceColorMode` 强制指定。
- 🧩 样式现在位于 `xyflow` CSS layer 中，需注意与 Tailwind 等 layer 的顺序；支持 `@xyflow/react/style.css`，并新增 `xy-theme.css` 主题。
- 🖱️ 面板光标样式移到 `::before` 伪元素，定制时需改为 `.react-flow__pane.draggable::before` 等选择器。
- 🧲 `nodeClickDistance` 被移除，改用 `nodeDragThreshold`；`paneClickDistance` 改为 `paneDragThreshold`，超过阈值才开始拖拽/平移，否则视为点击。
- 🎬 视口动画被中断时会 resolve 为 `false`；`fitViewOptions.padding` 无单位时按像素解释。
- 🔗 `onConnectEnd`/`onReconnectEnd` 的 `to` 改为 flow 坐标；`useHandleConnections`/`getHandleConnections` 移除，改用 `useNodeConnections`/`getNodeConnections`；`Handle` 类型改名为 `HandleBounds`；`elevateEdgesOnSelect` 默认 `true`。
- ⚡ 性能优化：内部 Store 拆分、单节点/边订阅减少重渲染、使用 React Compiler 编译；配合 `useNode`、`useEdge` 按需订阅效果更佳。
- 🧰 Changeset 提供 `getForNode`、`getByType` 等工具方法，便于获取指定节点或类型的变更。
- 🪝 新增 hooks：`useNode`、`useEdge`、`useInternalNodes`、`useEqualSelector`；`useReactFlow` 新增 `changeParent` 辅助函数。
- 🌲 子流程中父节点不再必须先出现，父节点可排在子节点之后；`changeParent` 会保持节点在屏幕上的位置。

---

### [自动化调试与 AI 根因分析 | Sentry](https://sentry.io/resources/automated-debugging/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-evergreen&utm_content=newsletter-primary-resource-hub-learnmore)

**原文标题**: [Automated Debugging & AI Root Cause Analysis | Sentry](https://sentry.io/resources/automated-debugging/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-evergreen&utm_content=newsletter-primary-resource-hub-learnmore)

Sentry 提出“自动化调试”：通过 AI 智能体把生产环境中的错误检测、根因诊断和修复生成串联成闭环，让开发者从重复的复现、追踪、打补丁工作中解放出来，只需审查和合并修复。其核心能力由 Seer、Sentry MCP、Seer Autofix 等组成，并强调生产上下文是准确修复的关键。

- 🐞 自动化调试覆盖“检测—诊断—修复”全流程：发现 PR 或生产中的 Bug，定位根因，生成补丁并发起 PR。
- 🤖 AI 智能体可自动接收 Sentry 问题，获取 Seer 的根因分析，创建修复，并让工程师作为审查者介入。
- 🧠 Seer 能利用堆栈跟踪、提交历史、Source Map、会话回放、日志和指标等生产上下文快速定位问题。
- ⚡ 自动根因分析把过去可能需要一小时的本地复现缩短到数秒，并追踪到具体代码行。
- 🔧 Seer Autofix 可自动完成根因分析、生成修复 PR，并解释问题原因。
- 🔌 Sentry MCP 支持接入 Claude Code、Cursor、Windsurf 等兼容智能体，让自有 AI 代理查询生产问题并提交修复。
- 🗣️ Seer Agent 支持用自然语言询问应用状况，并基于生产数据给出答案或执行操作。
- 🔗 通过 SCM 连接 GitHub、GitLab、Bitbucket、Azure DevOps，实现代码追踪和修复 PR 创建。
- 💬 可与 Slack、Linear、Jira、PagerDuty 集成，在团队现有工作流中启动和跟踪修复。
- 🎚️ 自动化程度可调：从开发者点击“查找修复”并审查 AI PR，到智能体夜间自动分诊并提交修复 PR。
- 🧩 文章还提供博客、工作坊、客户案例和操作配方等资源，展示 Bolt、Supabase、Anthropic、Factory 等团队的实践。
- 🚀 使用方式：在付费 Sentry 计划中启用 Seer，连接代码仓库并开启，即可开始自动发现和修复 Bug。

---

### [我们如何利用 AI 让 Next.js 更安全 | Next.js](https://nextjs.org/blog/how-were-using-ai-to-make-nextjs-more-secure)

**原文标题**: [How we're using AI to make Next.js more secure | Next.js](https://nextjs.org/blog/how-were-using-ai-to-make-nextjs-more-secure)

Next.js 团队在 2026 年 11 月 17 日的博客中说明：安全公告数量上升（2024 年 6 个、2025 年 14 个、2026 年至今 51 个）并不代表 Next.js 变得更不安全，而是 AI 让旧代码中的潜在漏洞更容易被发现。团队正通过漏洞赏金、内部安全机器人、外部审计、每月安全发布、AI 对抗式 PR 审查、Adapters 边界加固、替换高风险依赖，以及开发/构建期漏洞提示和代理升级工具，系统性提升安全性并帮助用户保持最新安全版本。

- 📈 安全公告数量持续上升：2024 年 6 个、2025 年 14 个、2026 年至今 51 个，但团队称 Next.js 实际比以往更安全。
- 🤖 AI 降低了发现和利用漏洞的成本；今年 70% 的漏洞来自至少一年前的代码，43% 来自三年以上的代码。
- 🖼️ 上游依赖也带来风险，尤其是图片优化相关库；部分严重漏洞并非来自 Next.js 本体。
- 💰 漏洞赏金计划让研究者更愿意私下报告漏洞，许多安全公告源自赏金报告。
- 🛠️ 团队用 Eve 开发内部安全机器人，辅助发现漏洞、分诊报告、复现问题、评估严重性并验证修复。
- 🔎 聘请独立安全公司 Trail of Bits 进行人工审计，发现其他来源遗漏的问题。
- 📅 建立月度安全发布计划并提前公布，方便用户和托管商安排升级与防护。
- 🛡️ Vercel Agent 的 Security Review 会在每个 PR 上以攻击者视角审查，已拦截通过代码审查和 CI 的潜在问题。
- 🧱 通过 Adapters 明确托管层与 Next.js 的契约，减少代理、CDN、运行时等边界不一致导致的绕过风险。
- 📦 替换高风险依赖，例如图片优化采用内存安全编解码器，并用 AI 加速集成和沙箱迭代。
- ⬆️ 从 Next.js 16.4 起，`next dev` 和 `next build` 会提示已知漏洞；DevTools 还提供 Vulnerability Insight 和可复制给编码代理的提示。
- 🚀 `npx next@canary upgrade --agent` 可检查安全公告，选择有修复的最旧主版本内的最新安全版本，并交给编码代理执行升级和验证。
- 🔮 团队将继续调查漏洞报告、用安全代理强化 PR 审查、简化升级流程；漏洞可通过赏金计划报告，安全问题可联系 security@vercel.com。

---

### [React2STEAL：它是什么以及需要检查什么](https://www.chainguard.dev/unchained/react2steal-what-it-is-and-what-to-check)

**原文标题**: [React2STEAL: What it is and what to check](https://www.chainguard.dev/unchained/react2steal-what-it-is-and-what-to-check)

React2STEAL 是 2026 年 11 月 18 日由 OpenSourceMalware 披露的自动化利用活动：攻击者利用被劫持的 GitHub 账户和 GitHub Actions 扫描互联网上的 React/Next.js 服务器，并利用两个已修复但未及时升级的漏洞窃取凭据，再将数据公开提交到 GitHub 仓库。它不是供应链攻击，未篡改 npm 包、GitHub Action 或维护者账户。

- 🚨 **活动性质**：React2STEAL 使用 GitHub 托管运行器作为免费算力，通过 `ci-wk-<number>` 仓库和 `scan.yml` 工作流批量扫描、利用目标。
- 🧬 **利用漏洞**：主要利用 React2Shell（CVE-2025-55182，CVSS 10.0，预认证 RCE）和 Next.js 中间件授权绕过（CVE-2025-29927）；还会尝试 `/_next/image` SSRF 读取云元数据凭据。
- ⚙️ **攻击流程**：提交目标列表 → 触发工作流 → 预筛选 Next.js 主机 → 并发尝试多种漏洞变体 → 在受害者 Node.js 进程中运行 `fast_recon.js` → 回传并提交窃取结果。
- 🎯 **影响规模**：发现 45 个仓库、44 个 GitHub 账户；至少 1,281 个受害者主机名、约 1,100 个域名；抽样 11 个仓库中约有 7.4 GB 数据。
- 🗂️ **窃取内容**：环境变量、`.env` 和配置文件、数据库连接串、Stripe 密钥、云凭据、Kubernetes Token、AI 提供商密钥；还会用受害者服务器测试 AI 密钥并可能产生费用。
- 🧪 **自查指标**：日志中出现重复 5 次的 `x-middleware-subrequest` 头、指向 `169.254.169.254` 的 `/_next/image?url=` 请求、带 `Next-Action: x` 和 `bissa_cve_boundary` 边界的请求，或 Web 服务器向 OpenAI/Anthropic/Gemini 等发起异常调用。
- 🛠️ **修复建议**：升级 React/Next.js 到所在版本线的最新补丁；检查 lockfile 和 SBOM；若命中指标，轮换服务器进程可访问的所有密钥和配置。
- 🧱 **临时缓解**：在代理/WAF/CDN 层剥离或拒绝 `x-middleware-subrequest` 头；启用 IMDSv2；限制 `images.remotePatterns`；为 Server Function 端点增加 WAF 规则，但不能替代补丁。
- 👤 **GitHub 账户检查**：查找未创建的 `ci-wk-<number>` 仓库、`wfx-docs` 分支、名为 “docs: dependency audit notes” 的 PR、工作流运行编号缺口；发现后应视为账户失陷并撤销 Token、轮换密钥。
- 🔗 **与 wfx-loot 关联**：多数运行 React2STEAL 的账户此前也遭 wfx-loot 凭据窃取活动影响；被盗 GitHub Token 未被吊销，随后被再次利用。
- 🛡️ **Chainguard 状态**：Chainguard 审查后称自身不受影响，React/Next.js 版本均不低于修复版本；其 JavaScript 库、SBOM/来源证明、Chainguard Actions 和 Checks 可帮助确认实际运行版本并降低 CI Token 被盗风险。

---

### [以编程、交互和智能体方式制作视频 | Remotion | 以编程方式制作视频](https://www.remotion.dev/blog/make-videos-programmatically-interactively-and-agentically)

**原文标题**: [Make videos programmatically, interactively and agentically | Remotion | Make videos programmatically](https://www.remotion.dev/blog/make-videos-programmatically-interactively-and-agentically)

Remotion 在 2026 年转向更智能、更交互的视频制作方式：Agent Skills 成为默认工作流，Remotion Studio 支持全面交互编辑，帮助用户更快速迭代视频。
- 🤖 Agent Skills 已成为使用 Remotion 制作视频的默认方式。
- ⚡ 视频制作变得更快、更强，支持程序化、交互式和智能体式创作。
- 🖱️ Remotion Studio 实现全面交互化，可选择、拖拽、修剪、裁剪和编辑内容。
- 🎬 官方视频展示了 Remotion 当前最先进的制作流程，以及如何快速迭代视频。

---

### [让组件具有交互性 | Remotion](https://www.remotion.dev/docs/studio/make-component-interactive)

**原文标题**: [Make a component interactive | Remotion](https://www.remotion.dev/docs/studio/make-component-interactive)

Remotion 文档说明如何通过 `Interactive.create()` 和 `InteractivitySchema` 让自定义组件在 Studio 中可选中、可编辑，并涵盖布局、字幕字段与内置交互 schema。

- 🧩 使用 `Interactive.create()` 包装组件即可启用交互；Remotion 默认组件本身已支持在 Studio 中选择和编辑。
- 🖼️ 填充父级的场景建议使用 `layout: 'absolute-fill'`，内部组件可返回 fragment，由包装器处理样式、变换、预挂载和裁剪。
- 📐 有自身尺寸的组件（如 Badge）保留默认布局，并将 `style` 转发到视觉根元素。
- 🛠️ 通过 `InteractivitySchema` 声明可交互编辑的 props，例如 `color`、`padding` 等。
- ⚙️ `Interactive.create()` 内置多类 schema：基础字段、预挂载、裁剪和变换字段，如 `from`、`durationInFrames`、`cropLeft`、`translate`、`scale`、`opacity` 等。
- 💬 当组件接收 `captions: Caption[]` 时，可加入 `Interactive.captionsSchema`，让字幕在 Studio 中可编辑。
- 🔗 调用 `Interactive.create({ Component, schema })` 将 schema 与组件关联后，即可正常使用组件；Studio 中会显示轮廓且 props 可编辑。
- 📚 相关参考包括 Interactivity 最佳实践、`Interactive.create()`、`InteractivitySchema`、`Interactive` 和 Studio interactivity。

---

### [When an import becomes a zip bomb: bundle regressions in Next.js — Sergey Patrakeev](https://bra31k.dev/en/blog/bundle-size-regressions/)

**原文标题**: [When an import becomes a zip bomb: bundle regressions in Next.js — Sergey Patrakeev](https://bra31k.dev/en/blog/bundle-size-regressions/)

概述：文章讲述团队如何用自研 CLI 工具 route-bundle-size 防止 Next.js 路由包体回归。一次 AI 参与的 PR 中，新增代码仅 7 KiB，却让页面体积增加 153 KiB；人工审查未发现，包体检查捕获了问题。团队利用构建产物实现体积测量与对比，改用 merge-base 基线降低误报，并通过案例说明包体守卫既能拦截坏变更，也能验证重构收益，最终将工具开源，并与 Next.js 官方分析器配合定位原因。

- 🤖 AI 辅助编码产生的 PR 表面正常，但一次页面 First Load JS 增加 153 KiB，而新增代码仅 7 KiB。
- 🧰 现有工具不适用：nextjs-bundle-analysis 只支持 Pages Router；@next/bundle-analyzer 只支持 webpack；next experimental-analyze 仅供人工分析，难以接入 CI。
- 🔎 团队发现未文档化的 route-bundle-stats.json，其中包含 routes、chunks 等构建产物数据，成为自研 CLI 的数据源。
- ⚙️ route-bundle-size 提供 measure 与 diff 两个命令：前者解析并压缩 chunks，后者比较结果、高亮超阈值路由并在需要时失败退出。
- 🧪 v1 基线存在误报：与 main 比较时受 e2e 失败和分支未同步影响；约一半失败为假阳性，落后 20+ commits 的分支失败率为 43%，同步分支为 5.7%。
- 🔁 团队改用 merge-base 流程：获取当前构建产物与 merge-base 产物（缓存或重建），再由 CLI 比较并更新摘要；公共 GitHub Action 会重建 merge-base 且无缓存。
- 💣 典型案例是两个独立合法变更叠加：barrel 导出把 engine 代码带入样式页并造成重复模块；若无守卫，应用整体将增大 200 KiB。AI 代理通过报告定位问题，改为独立 slice 导入。
- 📉 包体监控也能量化收益：移除旧 UI 后删除 220 个文件、19,354 行代码，/projects 首屏 JS 降低 26%，22 条路由变轻。
- 🧭 route-bundle-size 说明“发生了什么”，next analyze 说明“为什么”：开启 analyze: true 可附加官方分析报告并查看 treemap，例如首页误引入整包 lodash。
- 📦 工具已开源到 npm 与 GitHub；注意 Next.js 产物格式未文档化、目前主要关注 first-load JS，按路由预算从 0.2.0 起支持。
- 📊 文中数字因 CI 日志过期，在相同 commit 上本地重建；v1 误报比例是基于 GitHub API 的统计估算。

---

### [React 19.3 让 View Transitions 稳定了，setState 仍然不会触发动画。——Esteban Trillo](https://devtrillo.com/writing/react-19-3-view-transitions/)

**原文标题**: [React 19.3 made View Transitions stable. setState still won't animate. â Esteban Trillo](https://devtrillo.com/writing/react-19-3-view-transitions/)

React 19.3 将 `<ViewTransition>`、`addTransitionType` 等 API 稳定化，但文章强调：普通 `setState` 不会触发视图过渡，必须把更新放进 `startTransition` 等 React 认可的触发路径；作者通过实验还记录了共享元素、方向动画、Suspense、Fragment ref、`use(browser())`、Next.js 与浏览器兼容性等关键细节。

- 🎯 普通 `setState` 不触发动画：`<ViewTransition>` 只会在 Transition、Suspense reveal 或 `useDeferredValue` 更新中激活；实验里 `startTransition` 调用 `startViewTransition` 1 次，普通 `setState` 为 0 次。
- 🔁 四种触发类型：`enter`、`exit`、`update`、`share`，可用同名 props 设为 `"auto"`、`"none"` 或 View Transition Class，也可用 `onEnter`、`onExit`、`onUpdate`、`onShare`；每次 Transition 每个组件只触发一个事件，`onShare` 优先。
- 🧩 共享元素过渡：列表缩略图和详情大图使用相同 `name`，在 Transition 中切换时由浏览器对快照做移动和缩放；它不是布局动画库那种子元素独立动画。
- 🧭 方向动画：在 `startTransition` 内用 `addTransitionType("next" / "previous")`，再通过按类型键控的 `enter` / `exit` props 或 CSS `:active-view-transition-type()` 控制方向；`default: "none"` 可让无匹配类型的 Transition 不参与动画。
- ⏳ Suspense 用法：`<ViewTransition update="auto" default="none">` 包裹 Suspense 时，fallback 立即出现且不淡入，fallback 到内容交叉淡入，不 suspend 的子节点即时更新。
- 🧷 Fragment ref：`<Fragment ref={ref}>` 提供 `FragmentInstance`，无需额外 DOM 包裹；`observeUsing`、`addEventListener`、`getClientRects` 面向第一层宿主子节点，`focus()` / `focusLast()` 深度优先查找可聚焦后代，但它不是焦点陷阱。
- 🖥️ `use(browser())`：`react-dom` 新增 `browser()`，在 Suspense 中标记仅浏览器渲染的子树，替代 mounted flag；服务端只输出 fallback，适合地图、图表等依赖 `window` 的组件，不适合需要进入 HTML 的内容。
- 🧪 服务端行为：`browser()` 在 `renderToString` 和 `renderToReadableStream` 中都返回 fallback，且没有 recoverable error；`onBrowserBailout` 在 `renderToReadableStream` 触发，在 `renderToString` 未触发（作者未确认原因）。
- ⚠️ Next.js 注意：Next.js 16.4 宣称内置 React 19.3，但 App Router 使用 `next` 内置的 vendored canary 版本；建议使用 16.4.2 或更高版本（16.4.1 修复了关键 RCE），作者未在 App Router 实测。
- 🚢 上线前：所有 transition 还会触发 root 的全局交叉淡入，可用 `:root { view-transition-name: none; }` 移除（作者未测试）；减少动态效果需自行处理，React 不会自动禁用动画。
- 🧭 限制与兼容性：`popstate` 动画默认跳过（除非 router 使用 Navigation API）；`<ViewTransition>` 目前仅支持 DOM renderer。浏览器支持是生产可用关键：基础 View Transition 需 Chrome/Edge 111、Safari 18、Firefox 144；过渡类型和方向动画需 Chrome 125、Safari 18.2、Firefox 147。
- 📝 结论：React 稳定的是“何时请求浏览器执行 View Transition”的调度层，动画本身仍由浏览器完成；常见修复是把 `setState` 放进 `startTransition`。

---

### [Reanimated 4.8.0 中的共享元素过渡](https://swmansion.com/blog/shared-element-transitions-in-reanimated-4-8-0/)

**原文标题**: [Shared Element Transitions in Reanimated 4.8.0](https://swmansion.com/blog/shared-element-transitions-in-reanimated-4-8-0/)

Reanimated 4.8.0 正式推出共享元素过渡（Shared Element Transitions），通过标记关联视图并在边界切换时让组件在屏幕间“视觉移动”，为用户提供连续动画体验；同时新增更灵活的边界控制、子内容淡入淡出和真实视图连续动画能力，并带来 Animated.Text、CSS 动画增强及底层性能优化。

- 🧩 使用 `sharedTransitionTag` 关联两个视图，再用 `SharedTransitionBoundary` 和 `isActive` 触发过渡，可结合 react-navigation 或 expo-router 的 `useIsFocused` 在页面切换时运行动画。
- 🚪 新增 `SharedTransitionBoundary`，将过渡生命周期与导航解耦，支持同一屏幕内两个容器、Tab Navigator 标签页切换以及自定义导航流程。
- 🌗 新增 `fadeContent`，用于处理共享元素在源视图和目标视图中子组件不同的情况：源视图子内容淡出、目标视图子内容淡入，避免生硬跳变。
- 🎞️ 过渡动画直接操作真实视图而非快照，因此源视图和目标视图共享的原生状态可在动画期间继续运行，保持连续性。
- 🏗️ 早期实现基于旧架构，Android/iOS 逻辑分离、边界情况多且维护困难；新架构通过共享 C++ 层和 `isActive` 渲染信息简化了导航边界处理与调试。
- ✍️ 4.8 支持将共享值直接作为 `Animated.Text` 的子内容，由 UI 线程直接更新文本，无需每帧触发 React 重渲染，并可结合 `useDerivedValue` 做格式化。
- 🎨 CSS 动画/过渡继续增强：支持 `backgroundImage` 渐变动画插值，新增 `borderCurve`、`writingDirection`、`verticalAlign`、`objectFit`，且 `PlatformColor` 不再导致动画崩溃。
- ⚡ 底层优化减少了 UI 线程和 JS 线程每帧的不必要工作，整体动画性能更轻量。

---

### [React 解剖 — 3D React 组件检查器](https://react-anatomy.com/)

**原文标题**: [React Anatomy â 3D React component inspector](https://react-anatomy.com/)

React Anatomy 是一个浏览器扩展，为开发者工具增加 Anatomy 面板，将当前 React 页面拆分为 3D 图层，展示真实组件树和组件收到的 props，帮助理解页面结构、排查问题并解释变更。

- 🧩 核心功能：连接浏览器中正在显示的页面与 React 渲染的组件，支持分层查看、组件树追踪和 props 读取。
- 🧭 使用场景：快速理解陌生布局、学习 React 如何组合页面、排查异常区域、向评审者解释改动，以及阅读 AI 生成的代码。
- 🔍 自动生成结构图：过去需要手动在 Excalidraw 画框，现在可直接从运行中的页面生成图层、名称和嵌套关系。
- 🧱 展示范围：只显示 React 实际渲染的组件，不显示导入图；未出现在屏幕上的组件不会出现，重复渲染的组件会重复出现并各自带有 props。
- 🪟 3D 视图：根据页面形状自动分层，输出相同的包装器共享平面，所有捕获的组件都会保留在组件树中。
- 🛠️ 安装与体验：提供 Chrome Web Store、Firefox Add-ons 安装入口，也适用于 Brave 和 Edge；交互示例无需安装扩展，但需要 JavaScript。
- ⚠️ 定位说明：它是结构检查器，不是代码审查器，不评判结构好坏，结构是否正确仍由使用者判断。
- 🔧 技术限制：无需修改包或代码，检查在浏览器内完成；但依赖 React 私有内部实现，兼容性和视觉保真度可能变化，详情见文档。
- 📚 文档支持：包含示例、指南、截图、分层与深度说明，以及关于 React DevTools、生产构建和隐私的常见问题。

---

### [步进化](https://www.stepperize.com/)

**原文标题**: [Stepperize](https://www.stepperize.com/)

Stepperize 是一个面向 React 的类型安全多步骤流程构建库：只需定义一次步骤，即可获得步骤 ID 推断、导航守卫、失败原因和类型化结果，同时保留你自己的页面结构、表单和设计系统。新版 Stepper Studio 支持构建流程并通过一条命令安装。

- 🚀 一条命令安装：`npm i @stepperize/react`，支持 npm、pnpm、yarn、bun。
- 🧩 使用 `defineStepper` 一次定义步骤，步骤 ID 自动成为字面量联合类型，拼写错误会在编译期报错。
- 🛡️ `useStepper` 提供 `next/prev/goTo` 和异步 `guard`，自动处理边界并决定导航是否允许。
- ✅ 每次导航返回类型化结果，可检查 `accepted` 及失败原因：invalid、guard、policy、pending。
- 🔀 支持阻止式校验、声明式分支路径、异步过渡与重试，并暴露 `isPending` 状态。
- 🧠 `match()` 穷尽渲染步骤，漏写分支会报错；集中管理步骤状态，避免手写索引和 switch。
- 🪶 核心仅 2.6 kB（min+gzip，hooks only），0 个第三方依赖，开源。
- 🧱 提供无样式可访问原语（roles、ARIA、键盘导航）以及本地/共享 Provider，支持选择器细粒度订阅。
- 🔌 每个步骤可接入 Standard Schema，`next()` 自动校验；兼容 React Hook Form、TanStack Form、Conform、Zod、Valibot、ArkType。
- 🎨 提供 28 个基于 Tailwind 和 shadcn/ui 的可复制区块，覆盖审批、套餐选择、AI 工作流、2FA、CI/CD 等场景，复制即拥有、无需 eject。
- 🖥️ 提供实时预览与演示：输入邮箱、逐步导航、下单等，左侧代码直接驱动右侧面板。

---

### [fate 2.0 有什么新变化？ | fate](https://fate.technology/posts/whats-new-in-fate-2.0)

**原文标题**: [What's new in fate 2.0? | fate](https://fate.technology/posts/whats-new-in-fate-2.0)

fate 2.0 发布，将原本面向 Async React 的数据客户端扩展为支持 GraphQL、Vue、客户端状态、离线 mutation、SSR 水合与性能优化的完整数据层，并已在 Athena Crisis 生产环境验证，推荐通过 Vite+ 创建并部署到 Cloudflare。

- 🚀 fate 2.0 从 Async React 数据客户端升级为现代数据客户端，覆盖远程、本地与离线数据。
- 🔌 新增 GraphQL 支持：读取 schema 生成 TypeScript 类型，支持标量、联合、接口、Relay 连接、订阅及 `@defer` 流式增量交付。
- 🧩 支持客户端状态：可扩展服务端类型、创建纯客户端应用、执行客户端 mutation，并用 IndexedDB 持久化数据和运行迁移。
- 🧠 新增 Memo 字段：在数据类型上定义派生值，多个视图共享计算结果，依赖变化时自动更新。
- 📴 离线 mutation：先在设备本地保存变更，联网后重试；支持等待 `locallyPersisted`、关联变更原子提交和幂等键。
- 🖥️ 支持 Vue：`vue-fate` 提供视图、请求、mutation、实时更新与 `<Suspense>` 集成。
- 🧭 新视图 API：支持参数、条件选择 `when`、别名 `alias`，以及用 `viewFor` 处理联合/接口等不同结果类型。
- ✍️ Actions/Mutations 增强：可显式插入/移除列表项、定向失效、用 `.with()` 组合结果选择，失败时回滚。
- 💧 SSR 缓存水合：通过 `dehydrate()`/`hydrate()` 复用服务端数据；新增 `useViews`、`useRefetch`、`cache-only` 等读取与刷新能力。
- ⚡ 性能与可靠性提升：请求处理时间约降低 35%，保留内存约降低 45%，并修复并发 mutation、分页、实时更新、鉴权与错误恢复等问题。
- 🏭 生产验证：Athena Crisis 用 fate 替换 Relay 和 TinyBase，统一本地/服务端/离线数据 API，减少代码并提升性能与页面切换体验。
- 🛠️ 上手与部署：可用 `vp create fate` 或 `pnpm create fate` 创建项目，默认通过 Void 部署到 Cloudflare；官方呼吁测试并反馈。

---

### [Detent — React 滚轮选择器，带动画文本和数字](https://detent.hayder.sh/)

**原文标题**: [Detent — React wheel picker, animated text and numbers](https://detent.hayder.sh/)

Detent 是一个面向 React 的滚轮选择器，强调真实的惯性滚动、精准停靠到某一行、支持任意行内容，并提供垂直/水平、可访问和无依赖的使用体验。它同时提供开箱即用的样式组件与无头 hook，适用于时间选择、富列表、自定义交互等场景。

- 🎯 **核心定位**：Detent 是“点击感”正确的 React 滚轮选择器，支持惯性、投掷后精确落在某一行，以及任意内容放入行内。
- 🧭 **方向与可访问性**：支持垂直或水平滚轮，内置键盘与屏幕阅读器支持，是可访问的 listbox。
- 📦 **零运行时依赖**：除 React 和 React DOM 外无额外依赖；无头 hook gzip 后 7.4 kB，带全部预设的样式组件 17.9 kB。
- 🚀 **快速开始**：安装 `npm i @hayderkg/detent`，用 `items`、`value`、`onChange`、`label` 渲染即可得到可用的选择器；目前为预发布版，1.0 前 API 可能变化。
- 🧩 **两种用法**：`<Detent>` 自带样式与物理效果；`useDetent` 提供相同运动、输入与可访问性，由你自行渲染标记，适合设计系统或特殊需求。
- 🕒 **典型场景**：iOS 风格时间选择器（时、分、AM/PM 三个循环轮）、带 Logo/价格/迷你图的富列表、横向反应条等自定义设计。
- ♿ **工程能力**：支持方向键、Page Up/Down、Home/End、typeahead；尊重减少动态效果设置；支持服务端渲染初始选中项；已在 React 18 和 19、Chromium 与 WebKit 中测试。
- 🔤 **扩展组件**：Detent Text 可用滚轮式滚动动画切换文本；Detent Number 可用于价格、计数器、百分比，按小数位滚动并用 `Intl.NumberFormat` 格式化。
- 🎠 **不止选择器**：惯性、吸附与实时位置也适用于 Carousel 等浏览交互，支持平面卡片、封面流、无限循环和 RTL 镜像。
- 🛠️ **自定义扩展**：无头 hook 通过 `subscribe` 每帧报告位置与速度，可基于此实现 Liquid、Dust、Riso 等效果；这些示例效果不属于 npm 包本身。

---

### [Recharts](https://recharts.github.io/en-US/guide/theming/)

**原文标题**: [Recharts](https://recharts.github.io/en-US/guide/theming/)

Recharts 3.11 起提供主题系统：一个主题对象可为 React 树下所有图表集中设置默认颜色、字体、描边、Tooltip 与 Legend 样式，减少在每个组件上重复写 props。主题只是“默认值层”，显式 props 始终优先；若没有 Provider，则回退到旧版默认样式，v4 计划默认使用 autoTheme 并移除旧默认。

- 🎨 **主题定位**：主题统一设置图表默认视觉样式，适合作为全局设计 token；单个图表需要差异时仍用组件 props 覆盖。
- ⚙️ **快速使用**：用 `RechartsThemeProvider` 包裹图表并传入主题，例如 `autoTheme`，即可让树下图表继承默认样式。
- 🧩 **内置主题**：`lightTheme` 适合白底，`darkTheme` 适合深色页面，`autoTheme` 跟随页面 `color-scheme` 自动切换，`emptyTheme` 清除内置样式便于完全自定义。
- 🥇 **样式解析顺序**：依次检查 data 中的 SVG 属性、JSX props、主题；若完全没有主题 Provider，则使用 Recharts 2.x 以来的旧版默认样式。
- 🎯 **图形项颜色例外**：主题的 `fill` 与 `stroke` 成对设计，不混用；图形项若自定义 `fill` 或 `stroke`，会忽略主题对应颜色，但 `strokeWidth`、`strokeDasharray` 等非颜色样式仍逐字段合并。
- 🖼️ **图表背景**：`pageBackground` 不会被绘制，只用于间隙、光晕等“挖空”效果；`chart.backgroundColor` 会绘制在图表包裹元素上并覆盖 Legend；内置主题设置 `pageBackground` 但不绘制图表背景。
- 🏷️ **标签样式**：数据标签从对应 `graphicalItems` 条目的 `label` 取样式，其他标签取顶层 `label`；若主题和标签都未设颜色，数据标签会自动选色。
- 📐 **默认图表尺寸**：自定义主题可通过 `chart.width` 和 `chart.height` 提供默认尺寸，但仅在图表自身没有尺寸时生效；`width`、`height`、`style` 和 `ResponsiveContainer` 均优先。
- 🌈 **多系列配色**：主题按图形项的 `dataKey` 分配 `graphicalItems` 颜色，相同 `dataKey` 使用相同颜色；无 `dataKey` 时使用值轴 `dataKey`；`fill` 还可使用图案以满足不只靠颜色区分系列。
- 🛠️ **自定义主题**：`RechartsTheme` 是普通对象，可从内置主题展开并覆盖所需字段，也可完全从零定义；嵌套对象建议一并展开以保留未覆盖样式。
- 🌓 **autoTheme 切换**：`autoTheme` 的颜色使用 CSS `light-dark()`，跟随页面 `color-scheme`，无需 React state 或重渲染；需要较新浏览器支持，旧浏览器可改用 state 切换或 CSS 变量。
- 🔄 **React state 切换**：可通过普通 state 在 `lightTheme`、`darkTheme` 或自定义主题间切换，图表标记无需改动；同时要同步切换页面背景。
- 🎛️ **CSS 变量与设计系统**：主题值会原样传给 DOM，因此支持 `var(--token)`；也可用 `useMemo` 将 MUI、Mantine、Chakra、Ant Design 等设计系统 token 映射为 Recharts 主题。
- 🔍 **读取主题**：自定义 shape、Tooltip 内容、Legend 等组件可用 `useRechartsTheme` 读取最近的主题；无 Provider 时返回 `undefined`。
- 📜 **API 约定**：3.11 起主题整体形状属于公共 API，但具体颜色、描边宽度、虚线、`graphicalItems` 数量等不保证稳定；如需锁定颜色应创建自定义主题。
- 🗺️ **路线图**：Recharts v4 将把 `autoTheme` 设为默认主题，并移除“无 Provider 时”的旧版默认样式。

---

### [发布 v8.5.2 · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/releases/tag/react-router%408.5.2)

**原文标题**: [Release v8.5.2 · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/releases/tag/react-router%408.5.2)

这是一份关于 remix-run/react-router 仓库发布页面的摘要：该页面显示的最新版本为 react-router@8.5.2（v8.5.2），由 github-actions 于 11 月 18 日 16:11 发布。该版本基于 main 分支，自上一版本以来共合并 20 次提交，发布提交已通过 GitHub 验证签名。页面还列出仓库的 Issues、Pull Request、安全与质量等状态信息，以及变更日志和相关资源的入口。

- 📦 仓库为 remix-run/react-router，涵盖代码、Issues、Pull Requests、Discussions、Actions 等板块
- 🚀 最新发布版本为 react-router@8.5.2，标记为 Latest，即最新版
- 🕒 由 github-actions 于 11 月 18 日 16:11 发布，包含自该版本以来向 main 分支提交的 20 次 commit
- ✅ 发布对应提交 95d5037，带有 GitHub 验证签名，GPG 密钥 ID 为 B5690EEEBB952194
- 📝 发布说明可参见仓库 CHANGELOG.md 中 v8.5.2 章节
- 📎 该版本附带 2 个资源文件（Assets）
- 📊 仓库当前有 99 个 Issue、106 个 Pull Request，以及安全和质量相关条目 29 个
- ⚠️ 页面部分区域（标签筛选、资源加载）出现加载错误，提示需刷新页面重试

---

### [概览 · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/security)

**原文标题**: [Overview · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/security)

React Router 安全策略页面说明了受支持版本、漏洞报告流程与近期安全公告。项目当前支持 8.x 和 7.x 的安全更新，6.x 及以下不再支持；漏洞应通过 GitHub Security Advisory 的“Report a Vulnerability”功能私下报告。团队会确认报告、调查并通知托管平台，修复后发布新版本，并在一段时间后公开公告；第三方模块漏洞应联系维护者或通过 npm 表单报告。

- 🔐 当前受安全更新支持的版本为 8.x 和 7.x，6.x 及以下不受支持。
- 📣 报告漏洞需使用 GitHub Security Advisory 的“Report a Vulnerability”功能，不要公开披露。
- 🛠️ 处理流程包括确认报告、进入 Draft 调查、通知托管平台、发布修复版本、更新官方站点，并可能最多约一个月后公开公告。
- 📧 托管服务商如需提前获知漏洞，可发邮件至 hello@remix.run 申请加入通知。
- 📦 第三方模块的安全问题应报告给对应维护者，也可通过 npm 联系表单选择“I'm reporting a security vulnerability”提交。
- 🚨 高危公告包括：服务端路由发现 DoS、数据反序列化原型污染、Node.js 请求处理 DoS、路由匹配 DoS、__manifest 端点未认证 DoS。
- ⚠️ 中危公告包括：RSC 重定向 XSS、服务端 action CSRF 绕过、loader/action 响应开放重定向、RSC 模式 CSRF 绕过导致 400 前执行 action、开放重定向导致 XSS。
- 🗓️ 上述公告均由 brophdawg11 发布，部分发布于 2026 年 11 月 18 日，部分发布于 2026 年 7 月 22 日。

---

### [Release v1.2.0 · nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect · GitHub](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect/releases/tag/v1.2.0)

**原文标题**: [Release v1.2.0 · nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect · GitHub](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect/releases/tag/v1.2.0)

该文本是 `eslint-plugin-react-you-might-not-need-an-effect` 的 **v1.2.0** 版本发布说明。该版本为最新版本，发布于 **2026-11-08**，相关提交已通过 GitHub 验证签名。主要内容包括新增功能与多项 Bug 修复，重点提升对 TypeScript 语法、第三方 effect 包装器、context 值以及 useEffect 依赖分析的兼容性和准确性。

- 📦 **版本信息**：发布 v1.2.0，标记为 Latest，提交 `ff0e4a0` 经 GitHub 验证签名。
- 🆕 **TypeScript 支持**：可识别并分析仅用于 TypeScript 的语法。
- 🔌 **第三方 effect 包装器**：支持流行的第三方 effect 包装器。
- 🧩 **Context 处理**：将 context 值视为 props 进行分析。
- 🛠️ **组件识别修复**：修复对 `const Component = function() {}` 形式组件的分析问题。
- 🔍 **依赖分析修复**：改进对省略依赖或变量依赖的 effect 分析。
- 🚫 **避免误判**：当 `useEffect` 函数参数不透明时，不再错误落入整个外层函数体。
- 🔗 **别名与调用链**：改进成员访问别名追踪，并仅跟随稳定且被调用的别名。
- ⚙️ **useState 相关修复**：处理 useState 解构默认值，并将别名 setter 视为 setter。
- 🧹 **规则修复**：修复 `no-initialize-state`、`no-pass-live-state-to-parent`、`no-reset-all-state-on-prop-change` 等规则中的重复引号、重复调用 setter、包装 setter 和状态统计问题。
- 🧪 **回调过滤**：忽略非函数类型的 effect 回调，减少误报。

---

### [发布 v2.15.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.15.0)

**原文标题**: [Release v2.15.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.15.0)

v2.15.0 是 Redux Toolkit 的功能版本，继续推进 RTK 3.0 路线图，核心包括让 RTK Query 运行时按 store 隔离、修复 `initiate()` Promise 返回错误结果的问题，并新增多项 RTK Query 与 Listener Middleware 能力及行为修正。

- 🏪 每个 store 现在拥有独立的 RTK Query middleware runtime，`resetApiState` 只重置当前 store；缺失 middleware 的检查也更严格。
- ✅ `initiate()` Promise 现在解析为自身请求的结果，修复缓存条目被移除、重置、失效或替换时返回 `undefined` 或其它请求数据的问题。
- ⚠️ 行为变更：请求运行中移除缓存条目会中止请求，`unwrap()` 和 `queryFulfilled` 会 reject；`onQueryStarted` 中 `await queryFulfilled` 需加 `try/catch`。
- 🔁 失效正在运行的请求会等待其完成；运行中 refetch 会加入现有请求；从持久化状态恢复的 pending 条目会重新拉取。
- 🧭 查询请求新增 `startReason`，可区分 `initial`、`refetch`、`invalidation`、`poll`、`focus`、`reconnect` 等拉取原因。
- ⏱️ `pollingInterval` 可为函数，根据当前缓存条目返回轮询间隔，支持“任务运行时轮询，结束后停止”。
- 🔎 新增 `endpoint.getRunningQuery` 和 `initiate` 的 `retainFor` 选项，便于获取运行中请求 Promise 及预取后保留缓存。
- 🧩 新增 `api.util.getMiddlewareState()` 和 `initiate` 结果的 `isSubscribed()`；`internal_getRTKQSubscriptions` 被弃用。
- 🌿 Listener Middleware 的 `ForkedTaskAPI` 新增 `getState`、`dispatch`、`fork`，支持嵌套 fork 与 `autoJoin`。
- 🪄 新增具名类型改善编辑器悬停显示，减少 `Slice$1`、`IsAny` 等难读类型名和超长提示。
- 🛠️ 修复多订阅者共享查询时的 refetch 与轮询选项合并问题，包括 `refetchOnMountOrArgChange`、`forceRefetch`、`refetchOnFocus`、`refetchOnReconnect` 等。
- 🐞 其他修复包括 `maxRetries` 与 `retryCondition`、`retry.fail()`、`fetchBaseQuery` 的 `timeout`/`signal`、URL fragment 参数、headers 布尔/数字、entity adapter 的 ids 顺序、`createSlice` 的 `prepare` 类型等。
- 📚 文档更新覆盖 `getCacheEntryRemovedReason`、`startReason`、`getRunningQuery`、`retainFor`、`getMiddlewareState`、`isSubscribed`、函数式 `pollingInterval` 和嵌套 fork。

---

### [React Native 底部弹窗 1.0.0](https://swmansion.com/changelog/react-native-bottom-sheet-1-0-0/)

**原文标题**: [React Native Bottom Sheet 1.0.0](https://swmansion.com/changelog/react-native-bottom-sheet-1-0-0/)

React Native Bottom Sheet 1.0.0 是 2026 年 11 月 13 日发布的大版本，重点包括 API 重命名、关闭请求统一、`settleDuration` 单位改为毫秒，以及多平台关闭行为、RTL、颜色类型和类型导出等改进，并提供了从 0.18.1 迁移的步骤。

- 🚀 1.0.0 大版本发布于 2026 年 11 月 13 日。
- 🔄 `ModalBottomSheet` 的 `nativeOverlay` 重命名为 `windowOverlay`，行为保持不变。
- ⏱️ `settleDuration` 改为毫秒，默认 `450`；低于 `10` 会触发开发警告，避免仍按秒传值。
- 🧩 统一 `ModalBottomSheet` 关闭请求：遮罩点击、屏幕阅读器关闭、Android 返回键、Android/Web Escape 在提供 `onCloseRequest` 时均调用它；面板保持原位直到处理器改变 `index`；拖拽关闭仍通过 `onIndexChange` 上报。
- 📱 iOS 也支持 `onCloseRequest`：遮罩点击、遮罩 Dismiss 按钮和 VoiceOver 退出手势。
- 🚪 默认关闭行为调整：无处理器时，在遮罩可见且关闭档位允许交互的情况下，请求会吸附到关闭档位并通过 `onIndexChange` 上报；Android 返回键与 Escape 在关闭动画期间保持消费；Web 仅最上层 modal 接收 Escape，即使它不执行操作。
- ↔️ detent `insets` 新增 `start`/`end`，遵循布局方向并覆盖对应 `left`/`right`；Web 使用文档方向；修复 RTL Web 文档中 `surfaceStyle` 的 start/end 圆角。
- 🎨 `scrimColor` 扩展为任意 `ColorValue`，包括 `PlatformColor` 和 `DynamicColorIOS`。
- 🛠️ `wrapNativeView` 类型更新以隐藏内部原生 props，`Animated.createAnimatedComponent` 仍可用；新增 `BottomSheetProviderProps` 类型导出。
- 📦 `react-dom` 与 `react-native-web` 声明为可选 peer dependencies。
- 🔀 迁移：`nativeOverlay` 改为 `windowOverlay`；显式 `settleDuration` 值乘以 `1000`；检查 `onCloseRequest` 处理器并在需要关闭时将 `index` 设为关闭档位；无处理器的面板如需在 Android 返回/Escape 时保持打开，添加空操作处理器或将关闭档位标记为 `programmatic`；`wrapNativeView` 参数若显式标注原生 props，改用 `ComponentType<any>`。
- 🆕 后续版本：1.1.0 支持宽屏最大宽度与对齐并优化停靠动画；0.18.0 支持 Web、按档位 insets 的浮动卡片和懒加载。

---

### [推出 Expo 模拟器：专为智能体打造的云端模拟器](https://expo.dev/blog/introducing-expo-simulators-cloud-simulators-built-for-agents?utm_campaign=agentic-development&utm_source=ReactStatus&utm_medium=awareness&utm_term=newsletter&utm_content=simulators)

**原文标题**: [Introducing Expo Simulators: cloud simulators built for agents](https://expo.dev/blog/introducing-expo-simulators-cloud-simulators-built-for-agents?utm_campaign=agentic-development&utm_source=ReactStatus&utm_medium=awareness&utm_term=newsletter&utm_content=simulators)

你尚未提供文章正文，因此暂时无法提炼内容要点；请粘贴文本后再试。
- 📄 当前未收到可总结的文章内容。
- ✍️ 请提供正文，我会生成中文精简要点。
- ✅ 输出将包含概览总结与带 emoji 的“-”项目符号。

---

### [面向开发者的视频后端 — 快速添加视频 | Hyperserve](https://hyperserve.io/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=classified_nov20)

**原文标题**: [Video backend for Developers — Add Video Fast | Hyperserve](https://hyperserve.io/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=classified_nov20)

Hyperserve 是面向开发者的视频托管 API，提供上传、转码、CDN 托管与播放 URL 输出的一站式能力，帮助应用快速加入视频功能，避免复杂后端、专有播放器锁定和意外账单。

- 🚀 三步快速集成：后端创建上传、客户端直传文件、后端完成上传并触发转码。
- 🎞️ 接受用户上传的多种格式，自动转码为设备优化的 MP4；支持 MP4、MOV、AVI、MKV、WEBM、WMV、M4V、MPG，单文件最高 5 GB。
- 📺 输出分辨率覆盖 144p 到 8K，并通过 CDN 提供全球低延迟播放。
- 🔔 通过 Webhook 通知处理结果，例如 `video-processing-success` 返回可用分辨率和 `videoUrl`。
- 🧩 不绑定专有播放器：平台提供 URL，开发者自由控制 UI。
- 🧠 无需视频专业团队，上传内容会自动转换为适合设备的输出。
- 💰 定价可预测、按用量付费；免费版含 10 个视频、单文件 200 MB、每月 50 GB 带宽和免费编码。
- 📦 付费版按量计费：存储 $0.04/GB，带宽 $0.025/GB，免费编码，无最低消费或承诺。
- 🛠️ 提供清晰文档、复制粘贴代码、API 参考和实时演示；核心接口包括创建、上传、查询和删除视频。
- 🎯 适用于社交与创作者内容、市场平台、SaaS 与内部工具、健康与健身等需要视频能力的应用场景。

---

### [为 next](https://github.com/vercel/next.js/pull/101695)

**原文标题**: [Add an experimental Go front server for next start by jamiboym · Pull Request #101695 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/101695)

该 PR 在 Next.js 的 `next start` 中引入实验性的 Go 前端服务器（后更名为 Switchyard），通过环境变量启用。启用后，Go 程序占用公开端口，将请求原样转发到私有回环端口上的现有 Node 服务器，不参与路由决策；目标是逐步把路由等职责从 Node 迁移到 Go，同时保持默认行为不变。该 PR 已合并到 `canary`，并伴随重命名与后续 `route.go` 直连 worker 的系列改动。

- 🚦 实验开关：设置 `__NEXT_EXPERIMENTAL_FRONT_SERVER=1` 后，`next start` 启动 Go 的 `next-front`；未设置时行为完全不变。
- 🏗 架构：`client → next-front :3000 → Node 127.0.0.1:<OS选择端口>`，Go 作为 Node 子进程，仅做反向代理。
- 🔁 转发实现：使用 Go `httputil.ReverseProxy` 与 `Rewrite`，保留 `Host` 和原始请求目标，仅在缺失时补 `X-Forwarded-For`、`X-Forwarded-Port`，每次写入 flush，无压缩。
- ⏱ 超时策略：沿用 Node 的 `keepAliveTimeout`、`headersTimeout`、`requestTimeout`，前端无默认值；连接池空闲时间比 Node keep-alive 少 1 秒。
- 🧩 生命周期：Node 在 `127.0.0.1:0` 启动，spawn Go 前端并等待 `NEXT_FRONT_READY <port>`，再打印 `Local`/`Ready`；关闭时通过 stdin EOF、SIGINT、SIGTERM 优雅退出，任一侧崩溃会影响另一侧。
- 🌐 地址语义：公开 URL、`PORT` 保持不变；`__NEXT_PRIVATE_ORIGIN` 指向私有监听地址，使 server action 自请求跳过额外转发。
- 📦 二进制分发：实验阶段不随 `next` 发布；可用 `__NEXT_EXPERIMENTAL_FRONT_SERVER_BINARY` 指定，或 `NEXT_BUILD_FRONT_SERVER=1` 构建本机二进制；支持 Linux/macOS 的 amd64/arm64，Windows 或未知架构报错。
- ⚠️ 与普通 `next start` 的差异：状态码和响应体不变，但自定义 reason phrase 变为 Go 标准文案；`/%zz` 由 Go 先返回 400；absolute-form 目标、无 `Host` 请求、WebSocket 关闭、响应头大小写等存在差异；Node 私有端口本机可访问，后续迁移决策前需加 token。
- 📊 性能：基准显示每请求约 50µs 开销；简单 route handler 并发 1 时 RPS 从 10,319 降至 6,582，并发 64 时从 13,338 降至 11,655（-12.6%）；动态/流式页面影响很小；Go 进程 RSS 约 18–25MB。
- 🧪 测试与 CI：新增 `test-front-server-prod`，构建 Go 二进制并在启用变量下重跑 routing gate 和 front-server 套件；仅在 canary push 或前端文件变更时运行，实验期不阻塞合并。
- ✅ 验证：Go proxy 回归、race detector、TS/ESLint/Prettier 通过；启用时 103 passed、1 skipped，禁用时 behavior suite 22 passed。
- 🔄 后续演进：该实现后重命名为 Switchyard（#102035），环境变量、文件名、CI job 等同步改名；后续系列 PR 让 Switchyard 将 `route.go` 请求直接发给 Go worker，而非全部经过 Node。

---

### [Rename the experimental next start front server to Switchyard by jamiboym · Pull Request #102035 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/102035)

**原文标题**: [Rename the experimental next start front server to Switchyard by jamiboym · Pull Request #102035 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/102035)

该 PR #102035 已合并到 Next.js 的 canary 分支，将 `next start` 前的实验性 Go 前端服务器从 “front server” 重命名为 **Switchyard**，并修复客户端身份识别与请求头大小限制问题，同时改进 Switchyard 到 Node 的连接复用与数量控制。

- 🏷️ 重命名范围包括代码目录、Go 模块路径、二进制文件、启动模块、环境变量和 ready 行：`front` 改为 `switchyard`，相关变量改为 `__NEXT_EXPERIMENTAL_SWITCHYARD*`、`NEXT_BUILD_SWITCHYARD`、`NEXT_SWITCHYARD_READY`。
- 🧪 测试与 CI 同步改名：生产测试目录改为 `test/production/app-dir/switchyard/`，单元测试改为 `switchyard-watch.test.ts`，CI job 改为 `test-switchyard-prod`，taskfile、change group 和 gate 也一并更新。
- 🔐 改名动机之一是避免 “front” 与其他项目混淆；安全审查还发现外部客户端在 Pages API 路由中看似本地，且公共解析器接受的请求头预算大于 Node。
- 🛡️ 为保留客户端身份，Switchyard 会向 Node 发送经过认证的 TCP peer metadata；Node 在路由或升级前恢复 socket 地址，并移除内部 metadata；上游连接按客户端地址隔离，避免同一 socket 在不同客户端之间改变身份。
- 📏 公共监听器现在执行 Node 的有效请求头大小限制，包括 `--max-http-header-size`，并考虑 Go 的 4 KiB 读缓冲余量；配置预算小于等于 4 KiB 时会被拒绝，因为标准 Go server 无法强制执行。
- 🔁 连接管理改为每个客户端使用独立到 Node 的 transport，最多保留一个空闲连接；引入 512 个共享 keep-alive 槽位，按到 Node 的连接而非客户端计数；无槽位的空闲连接会关闭，升级连接会释放槽位，最多保留 512 个到 Node 的连接。
- ✅ 验证结果：启用 Switchyard 时 53 个生产/进程测试通过，禁用时 24 个行为测试通过；Go race suite 通过，覆盖伪造 metadata、连接隔离和不完整超大请求头；`pnpm typescript` 与 `pnpm --filter=next types` 通过；共 129 项检查通过。
- 🤖 审查方面，Vercel Agent 未发现新问题，但按 `REVIEW.md` 仍需人工审查；`timneutkens` 批准并合并，GitHub Actions 标记测试通过。
- 🧭 该 PR 基于 #101695，后续工作继续推进 `route.go` 请求直连 Go worker、查询字符串、动态路由、`basePath`、请求体、Early Hints、压缩和 worker 线程等能力。

---

### [Solid 2.0 - 长期持有 | Solid](https://www.solidjs.com/blog/solid-2-0-the-long-hold/)

**原文标题**: [Solid 2.0 - The Long Hold | Solid](https://www.solidjs.com/blog/solid-2-0-the-long-hold/)

Solid 2.0 在五年开发后正式稳定发布，核心围绕异步反应图、服务器函数、面向智能体的诊断和更小 API 展开；信号已从少数派方案成为行业主流，Solid 2.0 试图为后续框架明确一条可跟随的路径。

- 🧠 异步进入反应图：计算可返回 Promise 或 async iterator，下游自动理解 pending/stale，竞态条件与推测状态回滚由框架处理，服务器仍是真相来源。
- 🌐 Server Functions 回归核心：支持基于 Request/Response 的 RPC 和基于 Server Sent Events 的持久连接，示例中可直接用 `live()` 消费股票价格流；后续还将公布响应式 Server Components 等能力。
- 🤖 面向 Agent 的诊断：开发构建会报告稳定错误码、源码位置和修复建议，如 `STRICT_READ_UNTRACKED`，并提供 agent repair guide；还能检测瀑布、effect 循环、图扇入扇出等问题，并接入 Chrome Performance Tracks 与 Sentry 生产观测。
- 🧪 实验性语法支持：加入 ReactiveScript 和 TSRX，尝试通过编译进一步改善智能体编写体验。
- 🧩 一个框架适配所有：退休元框架 SolidStart，改由核心和框架无关的 Vite 插件提供构建元框架所需原语；支持任意 router 与缓存方案，生态插件也更统一。
- 📉 更小 API：移除 `createResource`、`batch`、`startTransition`、`on`、`produce`、`createComputed`、`createMutable` 等；加载状态、竞态和取消逻辑更多由框架保证，代码更短、意图更清晰。
- 🛠 发布历程：2024 年末启动实际工作，2025 年进入 beta/RC，API 冻结后 14 周内发布 23 个 RC，合并 971 个 PR、关闭 753 个 issue；稳定标准是一周内普通应用无回归、无崩溃或挂起。
- 🏷 “The Long Hold”：是 Solid 2.0 的诊断警告名，指 `isPending` 已显示但距上次输入已过足够时间；也呼应异步 hold 机制历经较长时间才落地。
- 🙏 社区与安装：感谢贡献者、测试者和赞助商（Sentry、Netlify、Google Chrome、JetBrains、Anomaly、Cursor、Code Rabbit、Anthropic、Tembo 等）；可通过 `npm create solid@latest` 开始使用。

---

### [我们如何将注册表元数据缩减了70% | vlt /vōlt/](https://www.vlt.io/blog/registry-metadata-70-percent-smaller)

**原文标题**: [How we made registry metadata 70% smaller | vlt /vōlt/](https://www.vlt.io/blog/registry-metadata-70-percent-smaller)

overview summary
- 📦 vlt.io 将 registry 元数据（packument）体积相比 npmjs.org 降低约 70%，干净安装中元数据占比从 25–45% 降至 5–15%。
- ⏱️ 五次运行中位数显示，vlt.io 安装耗时比 npmjs.org 少 20–70%，在 Next.js、Express 等场景中均有明显提升。
- 📄 Packument 是包所有版本 manifest 的聚合元数据；无 lockfile 或新增包时，包管理器需下载它以解析正确版本。
- 🧹 vlt 默认提供“install packument”：保留安装所需字段（如 time、license、libc），仅保留 dist.integrity，移除难以压缩的 signatures、shasum 和 attestation 文档。
- 📉 以 vite 为例，完整 gzip packument 从 npm 完整版 4.41 MB、缩写版 391 KB 降至 vlt 默认 104 KB。
- 🔢 npm 全量场景四项目传输 163.39 MB → 34.80 MB（-78.7%）；pnpm 默认 167.38 MB → 26.43 MB（-84.2%）；bun 缩写场景 93.89 MB → 26.35 MB（-71.9%）。
- 🏆 下载量前 1000 包：完整 packument 81.50 MB → 17.47 MB（-78.6%），缩写 62.46 MB → 15.70 MB（-74.9%）。
- 🚀 vlt 客户端与 registry 支持 `?stable`，在版本范围不可能匹配预发布版时只请求稳定版本；四个 fixture 总传输 136.57 MB → 7.49 MB（-94.5%）。
- 💰 对按带宽/出口计费的托管 registry，切到 vlt.io 可减少约 70% 元数据出口流量和相关费用。
- 🧪 数据来自 `vltpkg/vlt-registry-packument-size` 基准，记录解压前传输大小；测试版本含 npm 12.1.0、pnpm 12.6.0、bun 1.4.2、vlt 1.3.0。

---

### [vlt 对所有人开放：免费的 npm 注册表，无需账号，无需令牌 | vlt /vōlt/](https://www.vlt.io/blog/free-public-npm-mirror)

**原文标题**: [vlt is open to everyone: a free npm registry, no account, no token | vlt /vōlt/](https://www.vlt.io/blog/free-public-npm-mirror)

vlt 宣布其公共 npm 镜像向所有人免费开放：无需账号、token 或认证配置，兼容 npm、pnpm、yarn、bun 和 deno，并自 v1.8.0 起成为 vlt 的默认 registry。

- 🎉 免费开放：公共 npm 镜像无需注册、无需 token、无需添加认证行，但适用使用限制。
- 📦 广泛兼容：npm、pnpm、yarn、bun 和 deno 均可通过配置项目 registry 使用该镜像。
- ⚙️ 默认集成：自 vlt v1.8.0 起，安装 vlt 后直接运行 `vlt install` 即可使用默认镜像，无需额外配置。
- 🔄 简化流程：此前需要注册 vlt.io 账号、创建 token 并在 `.npmrc` 等配置中添加认证；新机器还需运行 `vlt setup` 解决缺少 registry 配置的问题。
- 🔐 忽略凭据：公共镜像会剥离 `Authorization` 请求头，过期或撤销的 token 不会导致 401，减少 CI 密钥管理和排错成本。
- ⚡ 性能更快：基准测试显示其安装相同依赖比 npm 更快；基准每晚运行，数据截至 2026 年 11 月 17 日，可查看 registry leaderboard。
- 🤝 公平使用：该镜像是共享的免费服务，适合项目、CI 和实验使用，但设有使用限制。
- 🙌 官方致谢：感谢贡献者和工程师，称这是 JavaScript 打包生态的重要进展，未来将继续推动更快、更安全的 npm 包消费与发布方式。

---

### [PostgreSQL：PostgreSQL 19 发布！](https://www.postgresql.org/about/news/postgresql-19-released-3449/)

**原文标题**: [PostgreSQL: PostgreSQL 19 Released!](https://www.postgresql.org/about/news/postgresql-19-released-3449/)

PostgreSQL 19 于 2026 年 11 月 19 日发布，面向大规模关键业务简化管理与开发，重点包括无阻塞表重组、查询计划稳定控制、逻辑复制和备库读写一致性增强，以及性能、监控和安全改进。

- 🚀 PostgreSQL 19 正式发布，延续 30 多年开源开发，定位为全球最先进的开源关系数据库。
- 🧹 新增 REPACK 命令及 REPACK (CONCURRENTLY)，可回收空间、按索引重排数据且不阻塞读写，替代 VACUUM FULL/CLUSTER（旧命令仍保留兼容）。
- 🧠 新增 pg_plan_advice 扩展和配套 pg_stash_advice，可稳定查询计划并按 query identifier 自动应用建议，无需修改应用即可修复慢计划。
- ⚙️ autovacuum 支持并行索引清理（autovacuum_max_parallel_workers）、新评分系统决定处理优先级；查询可自动标记 all-visible 页；vacuumdb --analyze-only 可分析分区表。
- 📊 新增 pg_stat_lock、pg_stat_recovery、pg_stat_autovacuum_scores 等监控视图；EXPLAIN ANALYZE 和 auto_explain 增加 IO 选项报告异步 I/O；pg_stat_wal 等报告全页镜像 WAL 量。
- 🔄 逻辑复制简化：创建首个逻辑复制槽时自动提升 WAL 级别至 logical（effective_wal_level 可查看）；支持序列值复制、CREATE PUBLICATION EXCEPT、CREATE SUBSCRIPTION SERVER 及 retain_dead_tuples；postgres_fdw 新增 import_stats，ANALYZE 时可导入远端表统计信息。
- 📖 新增 WAIT FOR LSN 命令，使备库支持“读己之写”一致性：等待 WAL 回放至指定 LSN 后再查询。
- 🛠️ 开发者体验增强：INSERT ... ON CONFLICT DO SELECT 简化 get-or-create；COPY 可输出 JSON；SQL/JSON 路径语言增加 lower/upper/replace/split_part/btrim；窗口函数支持 IGNORE NULLS；random() 可生成范围内日期/时间戳。
- ⚡ 性能提升：外键检查优化使批量插入测试中快近 2 倍；NOT IN 可转反连接、连接前 eager aggregation；异步 I/O worker 数量在 io_min_workers/io_max_workers 间自动调整；LISTEN/NOTIFY 多通道扩展性改善。
- 🔐 安全与其他：支持 SNI（pg_hosts.conf 映射主机名到证书）；md5 认证成功后告警（md5_password_warnings），RADIUS 认证移除；JIT 默认关闭；构建支持 LZ4 时 TOAST 默认压缩改为 lz4；新增 password_expiration_warning_threshold 密码过期提醒。

---

### [第674期：Postgres 19 来了（G](https://postgresweekly.com/issues/674)

**原文标题**: [Issue #674: Postgres 19 is here (GTA VI can wait) — Postgres Weekly](https://postgresweekly.com/issues/674)

本期 Postgres Weekly 聚焦 PostgreSQL 19 正式发布，重点包括在线表重打包、查询计划稳定化、逻辑复制与开发者体验改进；同时汇总升级注意事项、安全更新、生态工具与社区动态。

- 🚀 PostgreSQL 19 发布：`REPACK` / `REPACK CONCURRENTLY` 可在线回收膨胀并支持按索引重排，取代 `VACUUM FULL` 与 `CLUSTER`（旧命令保留兼容）。
- 🧑‍💻 开发者新特性：`INSERT ... ON CONFLICT DO SELECT` 支持“获取或创建”，`COPY` 可输出 JSON，窗口函数支持 `IGNORE NULLS`。
- 🧠 查询计划管理：`pg_plan_advice` 可试验和引导计划选择，`pg_stash_advice` 可按 query ID 自动应用建议，无需修改应用。
- 🔄 复制与一致性：逻辑复制可免重启开启，序列可复制，`WAIT FOR LSN` 在备库实现读己之写一致性。
- ⚠️ 升级前注意：全文检索、`pg_trgm`、`fuzzystrmatch` 索引升级后可能需要重建；`pg_upgrade --check` 可能通过后仍失败，例如 `standard_conforming_strings = off` 或自定义 `uuid` 到 `bytea` 转换。
- 🧹 恢复后维护：`pg_restore` 后应运行 `VACUUM ANALYZE`，否则首次查询可能极慢；JIT 在 19 中默认关闭，大型分析负载可考虑重新开启。
- 🔐 安全更新：18.7、17.12、16.16、15.20、14.25 修复 52 个安全问题，Postgres 14 已 EOL；另披露类型混淆导致 RCE 的 CVE-2026-6460。
- 🤖 社区动态：AI 生成缺陷报告泛滥，维护者呼吁停止提交未核查报告；`osm2pgsql` 迎 20 周年；PG DATA 2027 征稿开放。
- 🦀 `pgrust` 尝试用 Rust 重实现 PostgreSQL，解决存储需 `VACUUM`、优化器学习等痛点；`pgrx 0.20` 支持自动生成 C 宏/内联函数绑定并适配 PG19。
- 🌿 工具与扩展：Gnomon 为 Postgres 数据提供 Git 式分支/合并/撤销；PgDog 0.1.65、Atlas 1.4、Postbird 0.9、pgAudit 19.0 等更新。
- 📊 基准测试：DigitalOcean 新“Advanced”托管 Postgres 经 59 小时、100+ 数据库测试，表现与宣传相反。

---

