### [](https://planetscale.com/?utm_source=this_week_in_react&utm_medium=email&utm_campaign=2026_q3_this_week_in_react&utm_content=slot_1)

**原文标题**: [PlanetScale - the worldâs fastest and most scalable cloud hosting for Vitess, Neki, and Postgres](https://planetscale.com/?utm_source=this_week_in_react&utm_medium=email&utm_campaign=2026_q3_this_week_in_react&utm_content=slot_1)

PlanetScale 提供全球最快、最可扩展的云数据库，基于 Vitess 和 Neki 为 MySQL/Postgres 带来分片、NVMe 无限 IOPS、高可用、安全合规和成本优势，并被 Tier 0 工作负载采用。

- 🌐 PlanetScale 定位为云中最快、最可扩展数据库，覆盖 Vitess/MySQL、Neki 和 Postgres。
- ⚡ Vitess 通过显式分片让 MySQL 水平扩展，采用 shared-nothing 架构，可经单一连接路由到数千节点；源自 YouTube，曾支撑 PB 级数据和 70,000 节点、20 个数据中心。
- 🏢 Vitess 被 Slack、HubSpot、Blizzard、Etsy、GitHub、Block、Bloomberg、Yelp 等大型平台使用。
- 🧩 Neki 是下一代 Postgres 分片架构，借鉴 Vitess 经验，为大规模 Postgres 提供可预测性能和容错。
- 🐘 PlanetScale Postgres 起价 $5/月，全托管，支持 AWS/GCP，三可用区高可用和自动故障转移。
- 🚀 PlanetScale Metal 起价 $50/月，基于 NVMe 提供无限 IOPS，被基准测试为云中最快 Postgres，延迟低于 Aurora 和 Cloud SQL。
- 📈 性能：Metal 可提升 p50/p95/p99 延迟；客户 Cursor 用其承载每秒数百万查询和 PB 级数据。
- 🛡️ 可用性：多区域 SLA 99.999%，单区域 99.99%；支持在线 schema 变更、可回滚变更、读副本、在线版本更新、扩缩容和 resharding。
- 💰 成本：约 85% 迁移到 Metal 的负载比 RDS MySQL/Aurora 更便宜；支持 BYOC、AWS/GCP Marketplace，以及预留实例/节省计划。
- 🔐 安全合规：SOC 1 Type 2、SOC 2 Type 2+、HIPAA、PCI DSS 4.0 Level 1，提供 BAA 和 Trust Center。
- 🧰 共享功能：分支、读扩展、高可用、连接池、IP 限制、AWS PrivateLink、GCP Private Service Connect、Query Insights、备份、多区域、AI 优化和 MCP server。
- 🔀 Vitess 特有：部署请求实现零停机 schema 变更、回滚、Insights、显式分片工作流、只读区域/Global Edge，以及 Fivetran、Airbyte、Datadog 等集成。
- 🧱 Neki 特有：Postgres 水平分片、data topology、在线 schema 变更、分支、Query Insights 和备份。
- 🐘 Postgres 特有：$5 单节点、时间点恢复、Neki 横向扩展、灵活 CPU/存储/参数/磁盘自动扩展、pg_strict、Prometheus/Datadog/pganalyze、精选扩展、CDC 导入和 Database Traffic Control™。
- 🤝 客户信任：Anysphere/Cursor、Intercom、Cash App、Convex、MyFitnessPal 等认可其性能、成本、可靠性和专家支持。

---

### [自我改进数据库 - PlanetScale](https://planetscale.com/docs/self-improving-database)

**原文标题**: [Self-improving database - PlanetScale](https://planetscale.com/docs/self-improving-database)

PlanetScale MCP server 让 AI 编码代理访问生产 Insights 指标与 Schema Recommendations，并结合代码库持续发现、修复和验证数据库性能问题，形成自改进优化循环，适用于 Postgres 与 Vitess。

- 🤖 代理通过 MCP 连接 PlanetScale，拉取 Insights 数据或开放的 Schema Recommendations。
- 🎯 自动识别高影响查询或 schema 问题，如慢查询、高读取行数、高频访问和高出口流量。
- 🔍 在代码库中定位查询来源，修改代码，并在开发环境用基准测试验证改进。
- 📬 打开 PR，说明预期影响、潜在风险以及前后基准结果。
- ⏰ 可作为一次性任务，也可按每日或每周计划运行；Cursor Automations 适合云端定时代理。
- ✅ 前置条件：安装并认证 PlanetScale MCP；使用 Cursor Automations 或兼容 MCP 的 Claude Code 等代理。
- 🗄️ 需要带 Insights 数据的 PlanetScale 数据库，并在仓库的 AGENTS.md 中写明 org、database 和 branch。
- 🔐 可使用 insights-only MCP 端点，避免向代理暴露查询执行工具。
- 🧪 入门建议：先手动运行示例 prompt，审查 PR，再添加目录、ORM、linter、测试和迁移等护栏，反复迭代后再定时。
- 🛠️ Insights 优化 prompt：一次只修一个查询，避免重复已有 PR，用 EXPLAIN 建立基线并验证，运行 linter，PR 描述以“Implementing PlanetScale Insights improvement”开头。
- 📋 Schema 推荐 prompt：一次只实现一个最旧建议；无建议则不做；删除表或列分两步，先移除所有代码引用并部署生产，再执行 schema 变更。
- 🔎 最佳实践：一次修复一个问题、开发环境基准、用 AGENTS.md 提供上下文、按技术栈定制规则，并始终人工审查每个 PR 再合并。
- 💬 需要帮助可联系 PlanetScale Support 或加入 Discord 社区。

---

### [](https://react.dev/reference/react-dom/components/img)

**原文标题**: [<img> – React](https://react.dev/reference/react-dom/components/img)

React 内置浏览器 `<img>` 组件用于嵌入图片，支持常见元素属性，并涵盖服务端预加载、加载事件与 View Transition 等待行为。

- 🖼️ 基本用法：通过 `src` 指定图片 URL，`alt` 提供替代文本；装饰性图片设 `alt=""`。
- 📏 尺寸预留：已知宽高时传 `width` 和 `height`，帮助浏览器在加载前预留空间。
- 🧩 常用属性：支持 `crossOrigin`、`decoding`、`fetchPriority`、`loading`、`onError`、`onLoad`、`referrerPolicy`、`sizes`、`srcSet`、`useMap` 等。
- ⚠️ 核心注意：不要给 `src` 传空字符串，否则可能重新请求当前页；无图时应省略 `<img>` 或传 `null`。
- 🚫 限制：`<img>` 不能有子元素，也不能使用 `dangerouslySetInnerHTML`，否则 React 报错。
- 🚀 服务端预加载：React 默认自动生成 preload 提示；`loading="lazy"` 或 `fetchPriority="low"` 会阻止自动预加载。
- 📦 不自动预加载：图片在 `<picture>`/`<noscript>` 中，或 `src`/`srcSet` 为 data URL；可用 `preload` 显式创建预加载提示。
- 🎬 View Transition 等待：客户端 `<ViewTransition>` 更新中，React 可能等待新图片或 `src`/`srcSet` 变化的图片加载并解码；同步更新不等待。
- ⏳ 退出等待：图片需在 `<ViewTransition>` 子树且无 `loading="lazy"` 和 `onLoad`；Suspense 流式内容可见图片也可能等待，但有超时；`fetchPriority="low"` 不阻止该等待。
- 📚 示例：展示个人资料图；ProductPage 仅预加载 hero 图；ViewTransition + Suspense 先显示占位符直到肖像加载。

---

### [](https://github.com/react/react/pull/37636)

**原文标题**: [[Flight] Server References for arbitrary object types by acdlite · Pull Request #37636 · react/react · GitHub](https://github.com/react/react/pull/37636)

React 合并了由 acdlite 提交的 PR #37636《[Flight] Server References for arbitrary object types》，在实验标志 enableFlightObjectReferences 后，扩展 Flight 的 Server References，使其可引用任意对象，而不只是函数；主要场景是让框架按引用传递请求作用域值，从而避免在请求体中重复编码并提高响应可缓存性。

- 🧩 新增 API registerServerObjectReference，用模块 ID 标记对象，类似 registerServerReference 标记 Server Function。
- 🔒 客户端获得不透明句柄：读取属性或调用会抛错；只能通过 Server Function 传回服务器，由服务器清单解析。
- 🎯 动机：框架可按引用传递 request-scoped 值，例如将 searchParams 建模为模块导出，值从当前请求解析。
- ⚡ 好处：避免 searchParams 在 URL 和请求体重复编码；若响应体不包含它，响应缓存可将其排除在缓存键之外。
- 🧪 初期仅在 Turbopack 绑定中暴露该 API；若实验推进，再移植到其他打包器配置。
- 🔧 PR 含两次提交：先抽取 Server Reference 解析共享辅助函数，再实现任意对象类型引用。
- 🛡️ 评审关注：reply 解码的 getOutlinedModel 可能让去重路径遍历已解析的服务器对象，crafted reply 可选取属性传给 Server Action，若被回显则属性可能在客户端可读；需阻止 reply 属性路径遍历已解析服务器对象，并覆盖 $h 与 $H。
- 🧊 边界问题：若异步可迭代产出已注册的 TypedArray/ArrayBuffer，emitChunk 会在对象引用检查前序列化字节，导致同一响应内引用身份丢失；建议在二进制快速路径前检查已注册对象引用。
- 📦 体积影响：实验性 react-server-dom-* 包约 +2%~4%，Turbopack server 入口 +8%~11%；生产核心 react-dom 基本不变。
- ✅ 状态：已合并到 main，420/423 检查通过，unstubbable 批准；后续有 DiffTrain 构建和 Next.js 升级引用。

---

### [Next.js 严重上游问题安全更新 | Next.js](https://nextjs.org/blog/nextjs-security-update-september-22-2026)

**原文标题**: [Next.js Security Update for a Critical Upstream Issue | Next.js](https://nextjs.org/blog/nextjs-security-update-september-22-2026)

Next.js 发布带外安全更新，修复上游依赖（包括 Satori）导致的 Node.js `ImageResponse` 远程代码执行漏洞；建议升级至 v16.3.6（Active LTS），v15.5.26（Maintenance LTS）仅含相关加固，且 15.x 不受该 RCE 影响。

- 🚨 Next.js 发布带外安全更新，用于修复一个关键上游问题。
- 📦 更新版本为 v16.3.6（Active LTS）和 v15.5.26（Maintenance LTS）。
- 🛠️ 更新会升级上游依赖，包括 Satori。
- ⚠️ 漏洞可导致远程代码执行，严重级别为 Critical。
- 🧩 受影响的是 Node.js 版 `ImageResponse` 实现，位于 `next/og`。
- 📉 受影响的 Next.js 版本为 `>=16.2.0 <16.3.6`。
- 🛡️ 使用 Edge `ImageResponse` 实现的应用不受影响。
- 🔍 特定条件下，Satori 生成的 SVG 输出转义不当，结合其他上游依赖漏洞可能导致 RCE。
- ✅ v15.5.26 包含相关加固，但 Next.js 15.x 不受该远程代码执行问题影响。
- 💻 建议安装：`npm install next@16.3.6`；15.5 可安装 `npm install next@15.5.26` 以仅做加固。
- 🏆 Next.js 通过 Vercel 开源漏洞赏金计划与安全研究人员合作。
- 📧 安全问题可联系 `security@vercel.com`。
- 📅 该安全公告发布于 2026 年 9 月 22 日，作者为 Josh Story、Karim Rahal 和 Sebastian Silbermann。

---

### [](https://reactadvanced.com/?utm_source=thisweekinreact)

**原文标题**: [React Conference In London, October 23 & 26, 2026](https://reactadvanced.com/?utm_source=thisweekinreact)

React Advanced Conference 是面向 React 与 Web 开发者的年度高级技术大会，于 2026 年 10 月 23 日（伦敦线下 + 远程）和 10 月 26 日（远程）举行，主会场在伦敦 The Brewery，汇集 40+ 讲者、800+ 伦敦现场参与者与全球 5K 远程开发者，聚焦 React 生态、AI、全栈架构、性能、无障碍与工具链等前沿主题。

- 📅 会议时间：2026 年 10 月 23 日伦敦线下 + 远程，10 月 26 日全球远程，另设 5+ 免费与付费工作坊。
- 🌍 混合形式：第一天从伦敦场地直播并含混合社交互动，第二天及免费工作坊面向全球线上观众。
- 🎤 讲者阵容：来自 Vercel、Meta、Google DeepMind、Apollo、Shopify、OpenAI、Twilio、AG Grid 等公司的核心贡献者、社区领袖与资深工程师。
- 🧠 深度专题：全栈开发与架构、AI 智能体与辅助编程、AI 工程、晋升 Senior/TechLead 等 Multipass 专属 Deep Dives。
- 🛠️ 工作坊：Modern React Architecture、Claude Code: Black Belt、TanStack AI、DevOps for React Developers 等远程实战。
- 🗣️ 重点议题：Next.js 缓存组件、RSC、React Compiler、React 19、TanStack Query、AI 生成 UI、浏览器内 ML、性能优化、可访问性与测试等。
- 🤝 社交活动：线下/线上网络、专家 Q&A、主题讨论室（Build vs Buy、AI 时代就业力、Agentic Harness）、React 派对与卡拉 OK。
- 📍 地点：伦敦 The Brewery，位于科技创业与独角兽聚集的伦敦市中心。
- 💳 票务：Hybrid Full £640、Combo Full £790、Remote Full €180，GitNation Multipass 可 €17/月访问 10+ 会议。
- 🎓 社区与赞助：提供 100 个 diversity scholarships，并设 Gold/Silver/Partners/Tech Partners 赞助机会。

---

### [框架还重要吗？](https://brookslybrand.com/posts/do-frameworks-matter-anymore/)

**原文标题**: [Do Frameworks Matter Anymore?](https://brookslybrand.com/posts/do-frameworks-matter-anymore/)

overview summary
文章讨论在 2026 年代理式编程和“氛围编程”盛行的背景下，Web 框架是否仍然重要，以及是否还值得创造新框架。作者认为框架依然重要：行业实际依赖 React/Next.js，不用显式框架时 LLM 也会生成隐式框架，而且框架能提供抽象、结构与约束，帮助智能体产出更可靠、可维护的代码。但更关键的问题是“新框架还重要吗”，作者主张不应满足于现状，应继续构建真正全栈、基于 Web 标准、对 AI 友好且人类可理解的框架。

- 🤖 2026 年，代理式编程让“代码细节是否重要”成为焦点，但作者认为框架问题反而更值得认真思考。
- 🏆 传统观点认为 React 已胜出：生态最大、训练数据最多，因此没有理由尝试其他框架。
- 🧠 作者反驳：如果框架不重要，就不必用 React；如果 React 仍有优势，就说明框架重要。
- 🧩 框架的核心价值是提供抽象、结构和约束，让网站构建更可控、更易维护。
- ⚛️ React 的成功不只靠流行度，还因为组合性、易集成、组件化、生态和 SSR 等能力。
- 🛠️ 即使不使用显式框架，LLM 也会在项目中自动生成一套隐式框架，因此“是否用框架”并非真问题。
- 🧱 显式且成熟的框架通常比模型临时造出的框架更安全、更稳定、文档更好，也能给智能体更多护栏。
- 👀 作者仍看重代码形态、结构、类型、测试、lint、文档等约束，认为它们能提升智能体协作效果。
- ⚠️ HMR 和 TypeScript 对复杂开发仍有帮助，而 useEffect 等抽象对 LLM 来说风险较高。
- 📉 框架战争和元框架战争已结束，人们不再像过去那样热衷新框架，但重要性与炒作热度并不等同。
- 🚀 作者真正关心的是“新框架是否还重要”，并认为现有方案仍有改进空间：全栈、Web 标准、AI 易用、人类可推理。
- 🔨 结论：不要假设一切问题都已解决；只有继续构建新框架，才能验证新框架是否仍有价值。

---

### [](https://hackernoon.com/react-activity-when-a-render-no-longer-guarantees-an-effect)

**原文标题**: [None](https://hackernoon.com/react-activity-when-a-render-no-longer-guarantees-an-effect)

React 19.2 的 `<Activity>` 允许隐藏 UI 同时保留状态和 DOM，但它改变了生命周期：隐藏的组件仍可渲染，而 Effects 可能完全不挂载。这会让依赖“渲染后必有 Effect 清理”的旧代码在生产中暴露资源泄漏。作者通过一个在 render 中订阅外部 store 的旧 hook 发现，真正的问题不是 Activity，而是长期被 StrictMode 警告的不对称生命周期。

- 🧩 `<Activity mode="visible">` 保留状态、显示 DOM、正常渲染并挂载 Effects。
- 🙈 `<Activity mode="hidden">` 保留状态和 DOM，用 `display:none` 隐藏；组件仍可渲染，但 Effects 不挂载。
- ⚠️ 不能依赖 `render → Effect → cleanup` 序列；隐藏 Activity 可只渲染而不挂载 Effect。
- 🐞 旧 hook `useLegacyStore` 在 render 中调用 `store.subscribe()`，却只在 Effect 中 cleanup，导致订阅可能无人取消。
- 🔁 用 `<Activity>` 替换条件渲染后，隐藏标签页可提前渲染并创建订阅，但对应清理 Effect 可能永不出现，造成泄漏。
- ✅ 修复方式：把订阅创建和清理放在同一个 `useEffect` 中，保证 setup/cleanup 对称。
- 🧰 对外部 store 更推荐 `useSyncExternalStore`，显式提供 subscribe、getSnapshot 和 cleanup。
- 🧪 StrictMode 的双渲染和额外 setup→cleanup→setup 可提前暴露此类不对称；建议在应用根节点启用。
- 🧭 Effects 不再等同组件生命周期；WebSocket 等后台进程若应在隐藏后继续，其所有权应提升到 Activity 边界之上。
- 🎥 隐藏 Activity 不会移除 DOM，只加 `display:none`；`video`、`audio`、`iframe` 和第三方组件可能继续运行。
- ⏸️ 对依赖 DOM 移除停止的资源，要显式清理，例如在 `useLayoutEffect` cleanup 中暂停视频。
- 🧠 状态保留有利有弊：Tab 常需保留；创建表单关闭再打开可能应重置，不应机械替换所有条件渲染。
- 🔑 若仍想用 Activity 但重置表单，可改变组件 `key` 来创建新实例。
- 🏗️ 隐藏子树仍会低优先级渲染；保留大量大页面会消耗内存、DOM 和后台渲染，只在状态保留有真实收益时使用。
- ⏳ 预加载：若请求在 `useEffect` 中，隐藏 Activity 不会触发；若用 Suspense + `use` 在 render 中读数据，预渲染可提前启动请求。
- 🧪 E2E 影响：隐藏 DOM 仍存在，可能导致相同 `aria-label` 匹配多个元素；Playwright 需按可见性过滤或定位到可见 tabpanel。
- ❓ 使用 Activity 前检查：render 中是否有副作用、什么应在 UI 隐藏后继续、清理是否依赖 DOM 移除、是否真的要恢复旧状态、子树保留成本多高。
- 🎯 核心结论：Render、Effects、DOM、state 生命周期相关但不同；真正要问的是“子树是否隐式依赖旧生命周期序列”。

---

### [面向系统工程师的前端](https://tj-zhang.com/blog/frontend-for-systems-engineers/)

**原文标题**: [Frontend for systems engineers](https://tj-zhang.com/blog/frontend-for-systems-engineers/)

overview summary
本文用系统工程师熟悉的概念解释前端：关注状态所有权、派生视图、复制与同步边界。以 React 构建“一起看视频”房间为例，逐步加入播放列表、侧栏、播放器控制、持久化和跨设备共享，说明 React 负责从数据到 UI 的最后一英里，而真正难点在于设计数据关系与同步边界。

- 🧠 核心视角：把前端理解为状态所有权、派生视图、复制和同步边界；先想清每个事实归谁、如何传播。
- 🎬 示例场景：共享播放列表旁嵌入 YouTube 播放器；Alice 在手机选《沙丘 2》，Bob 的电脑应同步高亮并加载视频。
- 🌳 React 渲染：UI 是组件树，React 先 render 计算视图，再 commit 更新 DOM；组件是纯函数，JSX 描述元素。
- 🔁 派生视图：标题和高亮由 `selectedId` 与播放列表派生；DOM 可视为这些输入的物化视图，输入变化则重新推导。
- 📦 本地状态：React 用 `useState` 拥有选择与侧栏开关；事件处理器更新状态，下一次渲染派生新 UI。
- 👀 提交一致性：候选视图准备好后，React 一次性 commit DOM 变更，标题与高亮同时可见；props 和 state 应保持不可变。
- 🔌 Effect 同步：嵌入播放器状态在 React 之外；`useEffect` 在 commit 后调用 `loadVideoById`，依赖数组决定何时同步。
- ⚠️ 避免反模式：不要把派生值如 `title` 复制进 state 再用 Effect 同步，否则会分两次 commit，可能产生闪烁。
- 💾 持久化选择：IndexedDB 拥有跨刷新选择，客户端 store 提供同步内存快照并通知 React；写事务提交后刷新快照。
- 🪝 useSyncExternalStore：外部 store 需要订阅和快照契约；它解决订阅设置竞态，并在提交前验证快照，避免 tearing。
- 🌐 跨设备共享：后端拥有房间 `selectedId`，客户端保存副本；点击发送命令，后端接受后复制到各客户端，React 读取快照并派生。
- 🧭 本地与共享：侧栏可见性仍是本地 React 状态；Alice 打开侧栏不会影响 Bob。
- 📚 库的分工：同步层如 Electric、Convex、LiveStore 保持客户端状态最新；React 集成层如 TanStack DB 用 `useSyncExternalStore` 接入渲染。
- ✅ 结论：前端关键在数据关系——所有权、派生、同步边界；处理正确后，React 负责一致且及时地把数据渲染到 UI。

---

### [@astrojs/react | 文档](https://docs.astro.build/en/guides/integrations-guide/react/#upgrading-the-react-integration-to-v700)

**原文标题**: [@astrojs/react | Docs](https://docs.astro.build/en/guides/integrations-guide/react/#upgrading-the-react-integration-to-v700)

@astrojs/react v7.0.0 是 Astro 的 React 集成，用于渲染 React 组件并支持客户端 hydration；该版本移除了 `babel` 选项，改用 Oxc 编译 JSX 并支持 Fast Refresh。

- 📦 安装：可运行 `npx astro add react`，或使用 pnpm/Yarn 对应命令自动配置。
- 🛠️ 手动安装：安装 `@astrojs/react`，必要时还需安装 `react`、`react-dom`、`@types/react`、`@types/react-dom`。
- ⚙️ 配置：在 `astro.config.*` 的 `integrations` 中加入 `react()`，并在 `tsconfig.json` 设置 `jsx: react-jsx`、`jsxImportSource: react`。
- 🚀 入门：按 Astro UI 框架文档使用 React 组件，了解组件加载、客户端 hydration 与多框架混用。
- 🧩 Actions：`withState()` 和 `getActionState()` 可配合 React `useActionState()`，用于表单提交时读写客户端状态，并支持渐进增强。
- 🧵 多 JSX 框架：多个 JSX 框架共存时，需用 `include`（必填）和 `exclude`（可选）区分文件归属。
- ⚛️ React Compiler（v7.0.0 新增）：默认 `false`；设为 `true` 可用 Oxc React Compiler 自动 memo 化，减少不必要重渲染。
- 📥 Compiler 依赖：需安装 `oxc-transform-react`；React 17/18 还需安装 `react-compiler-runtime`。
- 🎛️ Compiler 配置：可传对象精细控制，例如 `compilationMode: 'annotation'` 仅编译带 `"use memo"` 的组件或 hook。
- 🧒 Children 解析：Astro 传给 React 的 children 默认解析为普通字符串；可用 `experimentalReactChildren` 改为 React 虚拟 DOM 节点。
- 🌊 禁用流式渲染：`experimentalDisableStreaming: true` 可关闭 React 流式输出，适合部分 CSS-in-JS 库。
- 🔁 v7 升级：Babel 被 Oxc 取代，并升级到 `@vitejs/plugin-react` v6；`babel` 选项已移除。
- 🧱 Babel 迁移：改用 `@rolldown/plugin-babel` 放在 `vite.plugins` 中配置自定义 Babel 转换；若含 `babel-plugin-react-compiler` 需移除以免重复编译。
- 🔗 更多集成：Astro 还提供 Preact、Solid、Svelte、Vue、Cloudflare、Netlify、Node、Vercel、MDX、Sitemap 等官方集成。

---

### [发布 v9.4.0-alpha.0 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/releases/tag/v9.4.0-alpha.0)

**原文标题**: [Release v9.4.0-alpha.0 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/releases/tag/v9.4.0-alpha.0)

React-Redux v9.4.0-alpha.0 预发布，新增可选启用的 `useSignalSelector` 与 `SignalProvider`，通过信号和路径跟踪只重跑依赖实际变化的状态选择器，面向大型应用的 dispatch 与渲染性能优化，但带来包体积和使用约束上的权衡。

- 🚀 新增 `useSignalSelector` hook 和 `SignalProvider` 组件，仅重新运行状态依赖实际变化的 selector。
- 📦 提供 `react-redux/signals` 入口，可全应用将 `SignalProvider` 别名成 `Provider`、`useSignalSelector` 别名成 `useSelector`，也可逐个组件增量采用。
- 🧠 背景：Redux 每次 dispatch 会 O(n) 调用大量 `useSelector` selector 并比较结果，大型应用中会成为主要性能瓶颈。
- ⚙️ 内部基于 `alien-signals` 构建路径键信号图，信号懒创建并在最后订阅者卸载时释放；依赖跟踪分两层，首次相关变化后才构建完整依赖图。
- ✅ 兼容性：`useSignalSelector` 签名和选项同 `useSelector`，通过现有测试；`connect`、`useDispatch`、`useStore`、原版 `useSelector`、Reselect 与 SSR 均照常工作。
- 📈 性能：16 个基准场景中 13 个脚本时间改善，12 个 `dispatch()` 内耗时下降 49–88%；例如 `derived-selectors` 渲染从 347 次降至 30 次。
- ⚠️ 成本：被跟踪 selector 求值比原始慢 3–4 倍，dispatch 需做状态树 diff；小应用挂载略慢，单个读取数千顶层键的场景脚本时间增加 36%。
- 📦 包体积：启用信号实现约增加 22.7 kB min / 7.2 kB min+gzip，总计约 32.9 kB / 10.9 kB；默认不用则无额外成本，并可由 tree-shaking 移除。
- 🧩 约束：状态必须是不可变普通对象或数组；`Map`、`Set`、`Date`、类实例仅按引用跟踪；selector 不得修改状态，开发环境会抛 `TypeError`。
- 🔍 约束：selector 接收代理，返回对象会自动 unwrap；`useSignalSelector(state => state)` 不会更新；数组迭代只跟踪一层。
- 📚 文档：Hooks API 页面拆分为 `useSelector`、`useDispatch`、`useStore` 等独立页面，并新增 `SignalProvider`、`useSignalSelector`、`unwrap` 页面。
- 🧪 状态：这是早期 alpha，实现完整且测试充分，但真实应用验证较少；作者尤其希望获得性能差异、selector 边界行为和包体积反馈。
- 👤 变更：由 @markerikson 在 #2318 加入原型实现。

---

### [错误](http://releases)

**原文标题**: [Error](http://releases)

无法总结：获取内容时出错 - HTTPConnectionPool(host='host.docker.internal', port=7897): Read timed out. (read timeout=30)

---

### [发布 v](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.8.0)

**原文标题**: [Release v9.8.0 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.8.0)

v9.8.0 是 pmndrs/react-three-fiber 的最新版本，核心亮点是兼容 React 19.3.0，并修复了根渲染同步、Strict Mode 及卸载期间重挂载等长期问题。

- 🚀 发布 v9.8.0，由 krispya 于 9 月 22 日 19:46 发布，提交号为 7db6056。
- ⚛️ 头条特性：R3F 现已兼容 React 19.3.0。
- 🧩 虽未完全支持所有新 API，但运行最新版 React 不再产生冲突。
- 🛠️ React roots 会先同步配置，再按需在渲染器上异步门控，例如 WebGPURenderer，避免状态不同步。
- ✅ Strict Mode 不再对 canvas 造成问题，此前问题与异步支持有关。
- 🔗 修复损坏链接（#3872），新增 React 19.3 支持（#3916）。
- 🧪 修复根在卸载宽限期内被重新挂载时遭拆毁的问题（#3869），核心改进为同步配置和渲染 roots（#3925）。
- 👥 新贡献者 @dor-rondel 和 @cades 首次参与，完整变更见 v9.7.0...v9.8.0。
- 📦 发布页包含 2 个资产，并获得 1 个 ❤️ 反应。

---

### [](https://github.com/pmndrs/glyph)

**原文标题**: [GitHub - pmndrs/glyph: ♠️ A typography engine for web graphics. · GitHub](https://github.com/pmndrs/glyph)

pmndrs/glyph 是一个面向 Web 图形的排版引擎，支持便携字体烘焙、Unicode 塑形、段落布局与批量文本渲染，并可集成 Three.js、React Three Fiber、TresJS、TypeGPU 等；目前为预发布版本，采用 MIT 许可且仅支持 ESM。

- 📦 仓库热度：pmndrs/glyph 当前约 354 stars、5 forks、26 issues、18 pull requests、331 commits。
- 🧰 核心能力：便携字体烘焙、Unicode shaping、段落布局、批量文本渲染等。
- ⚡ 安装方式：使用 `pnpm add @pmndrs/glyph three`，并通过 `glyph` CLI 将字体烘焙为 glb，支持 bitmap、msdf、slug。
- 🔤 字体烘焙：支持运行时与离线烘焙，可用 `--unicodes` 子集化，用 `--glyph-map` 生成图标字体名称映射。
- 📏 文本测量：`Text.measure()` 获取文本边界与字体度量；`Text.glyphs()` 获取逐字形位置与布局指标。
- ⚛️ React Three Fiber：通过 `@pmndrs/glyph/react` 集成，支持 R3F 9.7+/v10，提供 `GlyphProvider`、`Text`、`TextGroup`、`useSlug` 等。
- 🧪 TypeGPU：提供 `@pmndrs/glyph/typegpu` 与 `@pmndrs/glyph/three/typegpu`，支持 TypeGPU 配置与自定义渲染流程。
- 🖖 TresJS/Vue：通过 `@pmndrs/glyph/vue` 集成，需传入 `WebGPURenderer` 工厂，支持 Vue 组件与字体加载 composable。
- 🔌 自定义渲染器：核心引擎平台/框架中立，可用 `GlyphConfig` 定义 schema、字体格式、编码、资源解析、渲染器与根扩展。
- 🎨 独立着色器：可从 `@pmndrs/glyph/shaders/tsl` 和 `/typegpu` 导入 Bitmap、MSDF、Slug 着色器。
- ✅ 稳定功能：富文本样式、Unicode 塑形、对齐与两端对齐、换行与盒约束、测量、编辑流与多边形挖空、图标字体、拆字、Bitmap/MSDF/Slug 渲染、Three.js/R3F/TresJS、Wasm+SIMD、运行时/离线烘焙。
- 🟡 部分支持：编辑分栏无自动平衡；文本装饰仅实线；CJK 仅横向塑形与布局，大覆盖分页与竖排待后续。
- 🧪 实验性功能：TypeGPU 直接渲染与着色器、Three.js 中的 TypeGPU 着色器，尚未完全达到视觉一致。
- 🗺️ 路线图：彩色 emoji、彩色字形层与 bitmap 资源、微型 JS shaping 引擎、字形页缓存、语言感知断词、扩展编辑布局、垂直书写、实时逐字形变换。
- 🛠️ 开发贡献：需 Git LFS；可选 Mise；使用 pnpm install/dev；benchmark 位于 `benches/`；CI 构建测试前会拉取 LFS 对象。
- 📄 许可与模块：`@pmndrs/glyph` 为 ESM-only，采用 MIT 许可证。

---

### [发布 @tanstack/react-hotkeys@0.11.0 · TanStack/hotkeys · GitHub](https://github.com/TanStack/hotkeys/releases/tag/%40tanstack%2Freact-hotkeys%400.11.0)

**原文标题**: [Release @tanstack/react-hotkeys@0.11.0 · TanStack/hotkeys · GitHub](https://github.com/TanStack/hotkeys/releases/tag/%40tanstack%2Freact-hotkeys%400.11.0)

TanStack hotkeys 发布 @tanstack/react-hotkeys@0.11.0（9 月 21 日），包含多项破坏性变更、功能增强和修复，主要涉及热键类型、录制器、物理/逻辑键、冲突检测、显示格式化、跨键盘布局匹配及依赖更新。

- 🚨 破坏性变更：`RawHotkey` 与 `ParsedHotkey` 改为包含 `key` 或 `code` 的联合类型，需使用交叉类型而非接口扩展。
- 🎙️ 破坏性变更：录制器默认按物理 `code` 录制；若按逻辑键录制，需设置 `recordBy: 'key'`。
- 🧹 破坏性变更：清除录制只调用 `onClear`，不再以空值调用 `onRecord`。
- ⌨️ 新功能：支持类型化物理绑定，如 `Mod+[KeyS]`、`{ code: 'KeyS', mod: true }`，并支持 F1–F24、更多命名键和标点快捷键。
- ⚙️ 新功能：`parseKeyboardEvent` 新增 `platform` 选项；录制器新增 `recordBy`、`validate`、`detectConflicts`、`onReject`。
- 🔍 新功能：新增 `findHotkeyConflicts`（含序列前缀检查）、`HotkeyMeta.group`、`matchesHeldModifiers` 及各框架快捷键提示助手。
- 🏷️ 新功能：`formatForDisplay` 支持解析绑定、`parts`、独立修饰键/按键符号、`keyLabels` 和解析后的 `layoutMap`。
- 🛠️ 修复：改进跨键盘布局、macOS Option、Shift 标点、数字小键盘匹配；精确匹配优先于物理键回退。
- ➕ 修复：正确处理 `Mod++` 等字面加号与 Unicode 键名；避免 IME 组合和 AltGraph 输入时触发。
- 🔁 修复：正确清理按住键和 `requireReset` 状态；防止录制击键、重复、释放触发已注册快捷键。
- 🧩 修复：显示可读物理键标签（如 `S` 而非 `KeyS`），识别等价别名与冲突，避免 React/Preact 不必要注册更新及 Preact 连续重渲染。
- 📦 补丁变更：更新依赖 `@tanstack/hotkeys` 至 `0.9.0`。

---

### [React 简易地图](https://www.react-simple-maps.io/)

**原文标题**: [React Simple Maps](https://www.react-simple-maps.io/)

React Simple Maps V5 已发布，它是一个用于 React 数据可视化的可组合 SVG 地图图表库，像编写普通 React 布局一样组合地图，基于 d3-geo 和 TopoJSON，提供成熟、完全类型化且测试覆盖率高的 API。

- 🗺️ V5 发布：可组合 SVG 地图图表，用于 React 数据可视化。
- 🧩 组合式 API：像写普通 React 布局一样组合地图，而不是配置图表库。
- 🛡️ 技术底座：基于 d3-geo 与 topojson，API 成熟、完全类型化，测试覆盖率超过 90%。
- 🚀 快速开始：安装 `react-simple-maps`，组合地图、绑定地理数据并可视化；提供文档和快速教程。
- 💻 安装命令：`npm install react-simple-maps`。
- 🧱 代码示例：从 `react-simple-maps/core` 导入 `ComposableMap`、`Geographies`、`Geography`，设置投影（如 `geoAlbersUsa`）并加载地理数据。
- 🎨 简洁性：由小型辅助组件组成，构建地图更接近常规网页布局。
- 🌍 灵活性：支持自带地图文件，如国界、州界、河流、土地覆盖等，只要是有坐标的 GeoJSON/TopoJSON 数据即可。
- ⏳ 稳定性：经过近 10 年实战检验，核心思想与 API 基本不变，现在完全类型化且测试覆盖率超 90%。
- ⭐ 社区数据：自 2018 年以来 3,353 GitHub stars，每周下载量 900k+。
- 📜 许可与体积：MIT License，免费开源；完整 gzip 后约 34.3kb（含 d3-geo）。

---

### [@bvaughn.me 在 Bluesky 上](https://bsky.app/profile/bvaughn.me/post/3mvxpohs3vs2n)

**原文标题**: [@bvaughn.me on Bluesky](https://bsky.app/profile/bvaughn.me/post/3mvxpohs3vs2n)

该内容是一条来自 Bluesky 的帖子页面提示与动态摘要：页面因高度交互而需要启用 JavaScript；帖子由 Brian 发布，宣布 react-resizable-panels 4.13 已发布，并带来两项新功能，同时提供 Bluesky 与 AT Protocol 的相关链接。

- ⚠️ 页面需要启用 JavaScript，因为它是一个高度交互的 Web 应用，而不是简单的 HTML 界面。
- 🔗 提供了解 Bluesky 的链接：bsky.social，以及了解 AT Protocol 的链接：atproto.com。
- 👤 发布者为 Brian，个人站点为 bvaughn.me，DID 为 did:plc:dgbfbbzpfofxaqv42yj26xsd。
- ⚛️ 帖子宣布 react-resizable-panels 版本 4.13 刚刚发布。
- ✨ 该版本包含两项新功能。
- 🕒 发布时间为 2026-09-20T17:24:46.665Z。

---

### [发布 v4.2.0 · BetterTyped/react-zoom-pan](https://github.com/BetterTyped/react-zoom-pan-pinch/releases/tag/v4.2.0)

**原文标题**: [Release v4.2.0 · BetterTyped/react-zoom-pan-pinch · GitHub](https://github.com/BetterTyped/react-zoom-pan-pinch/releases/tag/v4.2.0)

这是 BetterTyped/react-zoom-pan-pinch 公开仓库的 v4.2.0 最新版本发布信息，主要包含核心功能增强、MiniMap 示例修复，并关联关闭多个 issue；仓库目前约有 1.9k star 和 303 fork。

- 🏷️ 版本发布：v4.2.0 为 Latest 版本，发布于 9 月 3 日 10:16，自该版本以来有 2 个提交合入 master。
- 🐛 Bug 修复：stories 中恢复 MiniMap 示例至已发布的 MiniMap API。
- ✨ 核心新功能：键盘导航、fit-to-view、panBy、可选择文本和跨窗口平移。
- 🔗 关联 issue：关闭 #254、#527、#252、#376、#530、#467、#552、#290、#537 等多个问题。
- 📊 仓库概况：公开仓库，约 1.9k star、303 fork、17 个 open issues、2 个 pull requests。
- ⚠️ 页面提示：内容加载时出现错误，部分信息需刷新页面才能正常查看。

---

### [React Native OTA 负载：利用](https://revopush.org/react-native-ota-payloads-binary-diffs?utm_source=this_week_in_react)

**原文标题**: [React Native OTA payloads: from 18 MB to 100-600 KB with binary diffs](https://revopush.org/react-native-ota-payloads-binary-diffs?utm_source=this_week_in_react)

overview summary
Revopush 2.0 的二进制 diff / Diff Updates 让 React Native OTA 只下载变更补丁，而不是完整 JS bundle。案例中完整 OTA 包为 18.7 MiB，补丁仅 117.26 KiB 至 611.49 KiB；迁移后出口流量下降、下载完成增加、发布频率提高。首次 OTA 也可直接作为 diff，并支持 React Native 0.83+ 与 Expo SDK 55。

- 📉 生产案例：6 月 7 日迁移到 Revopush Diff Updates 前，团队 OTA 发布较少，但仍有每天约 1–2 TB 的 egress；迁移后 egress 下降。
- 📈 迁移后下载量上升，团队也更高频地发布 OTA 更新。
- 📦 单次发布对比：完整 OTA 包为 18.7 MiB；生成的 JS 补丁分别为 117.26 KiB、586.94 KiB、611.49 KiB。
- 🔍 最大补丁仍比完整包小约 31 倍，最小补丁小超过 160 倍；实际缩减取决于改动内容。
- 🚀 好处：小修复不再下载完整 bundle，弱网、不稳定或计费网络下更易触达用户，减少中途关闭或后台下载受限导致的失败。
- 🧩 Revopush 2.0 解决基线问题：以原生应用二进制中的 JS bundle 和资源快照作为 base release，后续 OTA 可相对该基线生成补丁。
- ✅ 从 CodePush 风格迁移时，无需先推送一个完整 OTA 基线；首个基于原生版本的 OTA 即可为 diff。
- 🛠️ 发布流程：用 `revopush release-native` 从 IPA/APK 创建原生基线，再用 `release-react`（React Native）或 `release-expo`（Expo）发布更新。
- 📱 支持 React Native 0.83+ 与 Expo SDK 55；Expo 需原生配置，不能运行在 Expo Go 中，需使用 prebuild、EAS Build 或自有原生构建流程。
- 🎯 最适合大 JS bundle、资源密集页面、频繁热修、弱网用户或想降低 OTA egress 的团队；Expo SDK 55 项目可在纯 EAS Update 流程之外使用。

---

### [Revopush — 终极 React Native OTA 更新平台](https://revopush.org/)

**原文标题**: [Revopush — The Ultimate React Native OTA Update Platform](https://revopush.org/)

Revopush 2.0 是面向 React Native 的 OTA 更新平台，主打实时云更新、CodePush SDK 兼容与从 App Center 轻松迁移；它提供 CI/CD 集成、差分更新、发布分析、安全与多档定价，并已被 3000+ 应用使用。

- 🚀 核心定位：React Native OTA 实时更新，完整云支持，兼容 CodePush SDK，支持从 App Center 简单迁移。
- 🔗 集成生态：无缝对接 GitHub、Bitrise、CircleCI、Expo、Jenkins、Appcircle、Codemagic。
- 📊 规模指标：99.9% 历史正常运行时间，300M+ MAU，每月 10 亿 API 调用，3000+ 应用。
- 🧩 关键功能：开源客户端 SDK、移动 CI/CD、New Architecture 支持、扩展分析、DIFF 更新。
- 📦 差分更新：基于 IPA/APK 基础发布生成补丁，将 20–30 MB 包降至 100–300 KB，更新小 10–20 倍。
- ⚙️ 生产就绪：代码签名、灰度发布、回滚、团队协作与 CI/CD 自动化。
- 📈 分析能力：发布分析可查看灰度、安装和增量更新情况。
- 🛠️ 开发者体验：文档完善、易集成定制，支持 React Native 0.76+ 及新旧架构，持续更新。
- 💰 定价方案：Starter 免费；Startup $25/月；Growing $100/月；Business $250/月；Professional $500/月；Enterprise 定制。
- 📉 套餐额度：Startup 含 50K MAU 与 100GB 月流量；更高档位至 1M MAU、5TB；超额 $0.03/GB、$1/千用户。
- 🏢 企业能力：无限发布/更新、CI/CD、扩展安全与 SSO、优先支持，可部署在 AWS/GCP 或自有环境。
- 📰 最新动态：与 Vanta 推进 SOC 2 Type II；支持 AI agent 集成；Expo CodePush；OTA 安全最佳实践；CDN 优化提速 3.5 倍。
- 🔄 迁移与自动化：提供 App Center CodePush 迁移指南、自托管 CodePush Server、CircleCI Orb、Bitrise Step、GitHub Action。
- ❓ 常见问题：兼容现有 CodePush SDK，支持主流 CI/CD，通常无需大幅修改构建流程。

---

### [](https://posthog.com/newsletter/agent-autonomy?utm_source=twir&utm_campaign=sept23)

**原文标题**: [How much can you delegate to agents?](https://posthog.com/newsletter/agent-autonomy?utm_source=twir&utm_campaign=sept23)

overview summary
决定能委托多少工作给 agent 的关键不在模型能力，而在任务本身：是否容易检查、错误是否容易撤销。文章由此提出 4 个自主度级别，并给出每一级的升级路径。

- 🧭 核心观点：模型变强不等于可以盲目信任 agent，就像车更好也不能不系安全带；是否委托取决于任务。
- 🧪 判断因素一：agent 的工作是否容易检查？确定性检查如单元测试、集成测试更容易；主观任务需要人类品味与判断。
- ↩️ 判断因素二：agent 的错误是否便宜撤销？需要保证最坏情况有 Ctrl+Z；例如 StampHog 会把命中 deny-list 的 PR 转给人类。
- 0️⃣ Level 0 助手模式：难检查 + 难撤销。适合敏感、棘手代码；示例是手工完成 feature flag 核心迁移，只把风险较低的 SDK 传播交给 agent。
- 1️⃣ Level 1 人在回路：难检查 + 易撤销。适合主观评估，代码停留在草稿状态，人工验证后才合并；示例是可读性重构。
- ⬆️ Level 1 升级：使用 LLM-as-judge、定义可衡量的目标或契约、编写自定义技能。
- 2️⃣ Level 2 代理委托：易检查 + 难撤销。这是当前多数开发任务的默认上限；示例是 agent 重写 Rust SQL parser，但用 shadow mode 和分阶段切换把关。
- ⬆️ Level 2 升级：把策略与护栏编码进流水线，如默认 dry-run、限定凭据、使用 feature flags，避免人类成为瓶颈。
- 3️⃣ Level 3 自驾模式：易检查 + 易撤销。目前任务较少，如依赖升级、lint 修复、补测试，但增长很快；PostHog Scouts 可定期运行、调查信号并起草 PR。
- ⬆️ Level 3 升级：训练领域专用模型、构建专家级上下文库、为 scouts 设计清晰信号。
- 📏 规模不是判断自主级别的因素；先把任务级自主度做对，规模化会自然解决。
- 🧰 PostHog 的定位：提供 AI 可观测性、产品分析、会话回放、feature flags、实验、错误追踪、日志、数据仓库与 CDP 等，统一 agent 所需上下文，并可从 Slack、Web、桌面或 MCP 操作。

---

### [](https://github.com/react-native-community/discussions-and-proposals/pull/1023)

**原文标题**: [RFC: Secondary JavaScript runtimes in React Native by tjzel · Pull Request #1023 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1023)

该页面是 react-native-community/discussions-and-proposals 仓库中的开放 PR/RFC #1023，由 tjzel 提交，主题为“React Native 中的次级 JavaScript 运行时”，核心是让 React Native 提供第一方 C++ API，在 React 实例的主运行时之外创建额外的 Hermes 运行时。

- 📄 PR #1023 当前状态为 Open，目标分支为 react-native-community:main，来源分支为 tjzel:rfc/secondary-javascript-runtimes。
- 🧩 RFC 提案：React Native 将获得第一方 C++ API，用于创建主运行时之外的附加 Hermes 运行时。
- 👤 作者 tjzel 希望合并 1 个提交，并提供了可查看的渲染版 RFC 链接。
- 📅 2026 年 9 月 23 日期间，作者多次编辑、force-push 分支，并修改标题：从“owned by React Native”改为“supervised by React Native”，再改为“in React Native”。
- ✅ 该 PR 已被标记为 ready for review，提交记录为“Secondary Runtimes RFC”。
- 👀 当前没有审查、指派、标签、项目或里程碑，参与者仅 1 人。
- ⭐ 仓库页面显示约 1.8k Star、150 Fork、219 个 Issues、47 个 Pull Requests。

---

### [](https://shopify.engineering/helix)

**原文标题**: [Helix: The internal tool powering our Shopify app's native migration (2026) - Shopify](https://shopify.engineering/helix)

Helix 是 Shopify 的内部工具，用于让 LLM 按高度定制的架构，将 React Native 移动应用迁移为原生 Swift/Kotlin；它不追求一次生成完美，而是通过小检查点和严格质量门禁实现可靠收敛，让代码保持可发布。

- 📱 Shopify 正把移动应用从 React Native 迁回原生 Swift/Kotlin，Shop 已在 12 周内完成，现用同样方法重建 300+ 屏幕的 Shopify App。
- 🧰 Helix 是一套工具与技能，帮助 LLM 按既定架构迁移功能和屏幕。
- 🔁 它不假设首次输出正确，而是拆解工作、从工程师反馈中学习，并逐步自动化，目标是加速工程师同时保持高质量。
- 📋 流程从工程师指定一个屏幕开始，Helix 读取 React Native 代码并提出检查点序列，工程师几分钟内审核批准。
- 🧱 检查点是小的有序工作切片：通常先做屏幕骨架，再做小功能块，早期决策通过后才扩大范围。
- 🔍 小检查点便于快速审查并放入小上下文窗口，让代理直接读取参考代码，因为“参考就是规格”。
- 🧪 子代理为每个检查点生成测试用例，作为用户视角的集成测试，并探索边界情况。
- 🚦 每个检查点必须依次通过四道门禁：行为、UI 评审、对抗式代码评审、工程师确认；失败只能修复重试，不能跳过。
- 🖥️ 行为门禁通过 CLI 验证与 App 相同的屏幕状态和操作，无需模拟器，可快速迭代。
- 🎨 UI 门禁由 GPT 捕获匹配状态的实现/参考截图，Gemini 作为完美主义设计评审，列出每个差异及严重性和位置；可修复的视觉差异默认阻塞。
- 🕵️ 对抗式门禁由两个独立、上下文隔离的评审代理检查代码是否符合架构和 UI 规范；所有问题修复后重跑测试和 UI 评审，直到双方批准。
- 👨‍💻 工程师最终确认代码与运行效果；其反馈既修正当前工作，也存入记忆，提升后续检查点的自主性。
- 🤖 可启用自主模式：连续完成多个检查点或跳过审批，运行数小时甚至整夜；门禁不变，多屏幕可并行迁移。
- 📦 每个检查点最终形成提交，通常进入分支和 PR；自主运行后提供一系列带证据的提交，而非一个巨大 diff。
- 🚀 该循环也适用于新功能、架构迁移和重构；纯逻辑变更可跳过 UI 门禁。
- 💡 核心经验：从追求首次完美转向可靠收敛——尝试可以错，但未修好就不能发布。
- 📣 Shopify 正在招聘移动、基础设施以及 AI 与软件工程交叉领域的开发者。

---

### [](https://lynxjs.org/next/blog/reactlynx-instant-first-frame-rendering)

**原文标题**: [Deep Dive into ReactLynx: From Background Rendering to Instant First-Frame Rendering - Lynx](https://lynxjs.org/next/blog/reactlynx-instant-first-frame-rendering)

本文深入解析 ReactLynx 的双线程架构：React 逻辑运行在后台线程，主线程专注渲染原生视图；后台通过 Patch 跨线程提交，主线程用 Element PAPI 更新元素。为消除首帧等待，ReactLynx 引入 IFR：主线程先执行裁剪后的主线程产物绘制首屏，后台并行启动完整 React，随后通过 ID 映射交接已有视图，后续更新回归后台驱动的 Patch 流水线。

- 🧵 ReactLynx 将 React 的 render/commit 拆到后台线程，避免阻塞主线程渲染原生视图；但后台无法直接访问主线程 Element，因此需要跨线程异步提交。
- ⚛️ 后台运行时基于 Preact，拦截元素创建、属性变更和结构更新等 host 操作，不直接改视图，而是记录为 Patch。
- 📦 Patch 是扁平 opcode 流，主线程从左到右扫描执行；主要操作包括 CreateElement、InsertBefore、RemoveChild、SetAttribute、SetAttributes。
- 🔢 以计数器为例，count 从 0 变 1 只需发送 SetAttribute：实例 ID、编译期动态 slot 索引、新值，无需重发整个节点描述。
- 🧩 Patch 也能表达结构变化，如条件分支切换时在同一数字流中完成 RemoveChild、CreateElement、InsertBefore。
- 🖥️ 主线程解码 Patch 后，通过本地实例映射和编译期 slot 规则定位目标，再调用 Element PAPI（如 __CreateElement、__SetAttribute、__AppendElement 等）更新 Lynx Element 树。
- ⚡ 首帧不能只依赖后台 Patch，否则主线程要等后台初始化、执行应用代码和首次渲染；IFR 因此拆分快路径：主线程先运行裁剪后的主线程产物创建首屏原生视图，后台并行启动完整 React。
- 🛠️ Rspeedy 将每个入口编译为双线程产物：main-thread.js 负责首屏路径和创建 Element，background.js 保留完整 React 逻辑；二者最终打包进 lynx.bundle，由 Lynx 引擎按线程加载。
- ✂️ 编译期会按线程折叠 __MAIN_THREAD__ 分支，并把 useEffect、'background only' 等排除出主线程产物；主线程 runtime 更小，只保留首帧所需 Hook 行为与同步遍历，后台产物保留完整副作用、事件和状态更新逻辑。
- 🔄 交接采用类似 SSR hydration 的“认领”思路：主线程首帧树用负 ID，后台初始渲染用临时正 ID，递归匹配编译期动态 slot 和子结构；相同节点复用 ID，差异进入初始修正 Patch，事件先缓冲再按映射分发。
- ⏱️ ReactLynx 当前等两棵树都渲染完成，再由主线程把首帧树发回后台做匹配，避免阻塞主线程，并让后台初始渲染不等待主线程结果。
- 🚀 页面运行后，后台线程计算更新并发送 Patch，主线程继续通过 Element PAPI 更新已有 Element 树；架构核心是尽量把首屏表达为初始数据和可直接创建视图，缩短主线程路径。
- 💡 实践建议：可提前在宿主平台准备首屏数据以省去往返，并用 'background only' 等思路缩小主线程产物，追求即时首帧。

---

### [](https://andrei-calazans.com/posts/2026-09-19-the-kmp-ios-scaling-problem-rust-uniffi-fixes/)

**原文标题**: [The KMP-on-iOS Scaling Problem That Rust UniFFI Fixes • Andrei Calazans](https://andrei-calazans.com/posts/2026-09-19-the-kmp-ios-scaling-problem-rust-uniffi-fixes/)

overview summary
文章论证：KMP 在 iOS 因 Objective-C 导出而强制维护按领域划分的桥接/防腐层（约 30 个文件），负责 Sendable 包装、Flow→AsyncStream、类型重映射、依赖重建；Rust+UniFFI 直接生成原生 Swift/Kotlin 类型，不走 ObjC，消除大部分桥接，只留下流适配与 Kotlin 侧对象生命周期管理。

- 🧱 iOS 桥接层是防腐层：阻止 Kotlin 类型泄漏进 SwiftUI/功能代码，按领域一个文件。
- 🔒 F1：ObjC 导入的 Kotlin 类非 Sendable，需 @unchecked Sendable 包装并手写安全论证。
- 🌊 F2：Kotlin Flow 不能直接桥接，需 Task + AsyncStream 转发并处理取消。
- 🧭 F3：ObjC 擦除 value class、URL、枚举等，桥接层逐字段重映射并恢复校验，代码量最大。
- 🧩 F4：桥接层重建原生 Swift 闭包仓库供功能注入；功能代码不接触 Kotlin。
- 🤖 Android 全 Kotlin，可直接使用 Kotlin Flow，无需桥接；桥接是 iOS 专属税。
- ❓ KMP 强制桥接是因导出经 Objective-C：类型无 Sendable、Flow 有洞、类型擦除、引用语义。
- 🦀 Rust+UniFFI 编译为原生库（iOS .a / Android .so），生成薄 Swift/Kotlin 绑定，调用链为 Swift→wrapper→C ABI→Rust。
- 🧬 UniFFI 生成真实 Swift struct/enum 与 Kotlin data/sealed class；原生类型就是唯一类型，无二次映射。
- ✅ F1/F3 消失：无 ObjC 导入与擦除，生成类型可 Sendable，Rust 值跨边界后复制为原生值。
- ⚡ F2 对请求/响应消失：async fn 直接映射 async throws / suspend；连续流仍需少量适配。
- 🔁 F4 缩为普通 DI；生成对象已是原生可注入对象。
- 🆕 Rust 新成本：uniffi::Object 是 Rust 堆句柄，Kotlin GC 不释放，需确定性 close()；Cleaner 后备不及时且对 Rust 堆压力不敏感。
- 🧯 设计规则：返回 Record 而非 Object；Object 少且长生命周期，屏幕级用基类统一 close。
- 📡 流是唯一保留胶水层：Rust 用 callback_interface 推送，Swift 包 AsyncStream，Kotlin 包 callbackFlow，按流形状写一次而非按领域。
- 🏁 结论：Rust 删除 KMP 式按领域桥接模块，但不删除所有边界工作；仅保留有限流适配和 Kotlin 对象生命周期管理。

---

### [在 iOS 和 Android 上，Rust 中的共享业务逻辑是什么样的？• Andrei Calazans](https://andrei-calazans.com/posts/2026-09-18-shared-business-logic-in-rust/)

**原文标题**: [What Does Shared Business Logic in Rust Look Like on iOS & Android? • Andrei Calazans](https://andrei-calazans.com/posts/2026-09-18-shared-business-logic-in-rust/)

本文总结了一个移动端 Rust 共享业务逻辑的 PoC：SwiftUI 与 Compose 只保留原生 View/ViewModel，Rust 承载用例、仓库、数据源、HTTP/GraphQL、模型；通过 UniFFI 自动生成 Swift/Kotlin 绑定，在 iOS/Android 上调用同一个 AppCore。整体可行，但需接受若干明确成本：数据无原生行为与免费序列化、Kotlin 侧 Object 需手动关闭、单次链接步骤有固定开销；按 crate 拆分并缓存可扩展到大型模块。

- 🦀 核心思路：把原生/共享边界尽量上移，View/ViewModel 原生，其下全部用 Rust 共享。
- 🔌 AppCore：UniFFI Object 暴露 `login`、`define_words`、`fetch_bitcoin` 等；网络用 `reqwest` + `tokio`。
- 🌉 桥接必须自动生成：手写 JNI/Obj-C 不可行；`cbindgen` 无 async，Diplomat 无原生 async，UniFFI 支持 async→`suspend`/`async`。
- 🧬 生成物不入库：Kotlin/Swift 绑定在构建时由 `uniffi-bindgen` 生成，Android Gradle 与 iOS build phase 重新生成，git 只跟踪源码。
- 📱 调用点自然：Rust Record/Enum 生成 Swift struct/enum 与 Kotlin data class/sealed class；`async fn` 映射为 `async throws` / `suspend`。
- ⚠️ 工效损失：Record 只有字段，没有方法/计算属性；生成类型不自动 `Codable`/`Parcelable`/`kotlinx.serialization`。
- 🧹 Kotlin 对象需管理：`uniffi::Object` 是 Rust 句柄，Kotlin 侧 `AutoCloseable`，应 `close()`；Cleaner 只是不可靠兜底。
- 🧵 线程边界：Rust 回调可能在 `tokio` 线程触发，原生侧需切回主线程再碰 UI。
- ✅ 保留项：值语义、sealed/enum、可空性、`Result`→`throws`/异常、原生并发、模式匹配等仍接近原生体验。
- 📈 可扩展性：iOS 链一个 staticlib、Android 加载一个 `.so`；按 crate 拆分并利用 Cargo 增量缓存，`ffi` crate 保持薄，`uniffi_reexport_scaffolding!` 组合桥接。
- 🧱 性能规则：dev 开 incremental/codegen-units，release 用 thin LTO；单次链接是固定税，需控制导出符号并剥离死代码。
- 🧯 内存泄漏防治：Object 少而长命，尽量返回 Record；屏幕级对象用 `RustViewModel` 基类统一 close，Lint Recycle 仅覆盖简单局部对象。
- 📦 PoC 仓库：`github.com/AndreiCalazans/mobile-rust`，含 Rust core、生成绑定、iOS 与 Android 应用。
- 🏁 结论：该架构读起来像原生代码，成本窄且已知；按 crate 边界与单链接纪律，可扩展到 400+ 模块。

---

### [](https://www.callstack.com/blog/exploring-jev-for-mobile-qa-with-agent-device)

**原文标题**: [Exploring Jev for AI-Driven QA with agent-device](https://www.callstack.com/blog/exploring-jev-for-mobile-qa-with-agent-device)

TypeSafe 发布 Jev——一个用于快速、结构化决策的 System One 模型，并演示其与 Callstack 开源工具 agent-device 结合，构建 AI 驱动的移动 QA 代理：Jev 负责选择下一步动作，agent-device 负责读取并操作 App。

- ⚡ Jev 报告响应时间为 70–500 毫秒，基准测试中执行速度最高提升 193.6 倍，成本比所测试的 LLM 配置低 444.6 倍。
- 🤖 对 QA 代理而言，这意味着可在相同预算内运行更多测试，并更快获得反馈。
- 📱 agent-device 通过无障碍 API 读取按钮标签、文本、表单值等 UI 信息，生成带控件引用（如 @e4）的快照。
- 🧩 系统把快照转换为动作：按钮或开关变成 press，可编辑字段变成 fill，隐藏、禁用或被阻挡的控件会被排除。
- ✨ Jev 接收任务、当前屏幕、上一屏幕和上一动作，从预定义动作中选择；它不生成解释、不生成工具调用序列，也不生成文本字符串。
- 📊 Jev 返回所选答案及概率，应用可根据不确定性处理；文本输入值已包含在动作中，由 agent-device 执行填入。
- 🛠️ 使用 TypeSafe JavaScript SDK 的 systemOne 请求，把动作描述作为选项，让 Jev 输出选中的 action ID，例如 a10 表示 Add to cart。
- ✅ Jev 还能选择 pass、fail 或 incomplete，根据当前/上一屏幕和上一动作结束测试运行。
- 🧪 演示运行耗时 14 秒，模型推理成本为 $0.0023；项目已打包为 CLI，可设置 TYPESAFE_API_KEY 后试用。
- 🍎 示例任务是在 iOS 模拟器中打开设置，进入辅助功能与显示和文字大小，滚动到智能反转并验证开关可见，且不更改任何设置。
- 🔄 如果更想使用 LLM 而非 Jev，可参考 Callstack 基于 Vercel Eve 的 QA 演示。

---

### [Codemagic Patch | 适用于 React Native 的自托管 OTA 更新](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

**原文标题**: [Codemagic Patch | Self-hosted OTA updates for React Native](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

Patch 是 Codemagic 推出的自托管 OTA 更新方案，主打简单部署、可扩展、零停机，并面向百万级用户；它把现代托管 OTA 的能力带入可自行掌控的完整栈中。

- 🚀 最易自托管 OTA：基于数十亿次更新经验，提供高效架构与设置。
- 🐳 一键部署：在支持 Docker Compose 的任意机器上部署完整栈。
- 📈 轻松扩展：架构设计可扩展至数百万用户，无需额外工作。
- 🛡️ 零停机：检查和下载都走 CDN，崩溃不会中断更新交付。
- 🎛️ 完整控制：具备现代托管 OTA 的全部功能，但无需五位数费用。
- 👻 隐形更新：支持应用后台安装；紧急补丁可使用立即更新。
- 📡 可靠交付：CDN 实现 99% 送达率，小包体也适合弱网下载。
- 📊 发布监控：Web 仪表盘管理发布、指标和团队访问；支持受控发布与推广。
- 🧪 自行运行：一条命令启动本地评估栈，含演示应用；同栈可部署到 VM 用于生产。
- ⚖️ 对比优势：其他自托管 OTA 常需 DIY 自动扩缩与缓存；Patch 的检查和下载随 CDN 扩展。
- 🛑 停机差异：其他工具 API 故障会阻断检查；Patch 仅在 CDN 故障时受影响。
- 🔧 功能差异：Patch 提供即时、重启、恢复、暂停、挂起等安装模式，以及仪表盘、CLI、RBAC 和支持许可证；其他工具常较有限。
- 🏢 背景实力：Codemagic 10 余年移动 CI/CD 经验，已交付数十亿次 OTA 更新。

---

### [](https://developer.apple.com/documentation/xcode/updating-your-xcode-project-configuration-file-format)

**原文标题**: [Updating your Xcode project configuration file format | Apple Developer Documentation](https://developer.apple.com/documentation/xcode/updating-your-xcode-project-configuration-file-format)

该页面需要 JavaScript 才能正常显示内容；用户需在浏览器中启用 JavaScript 并刷新页面，而自动化工具和辅助工具可通过 Markdown 版本查看内容。

- ⚠️ 页面内容依赖 JavaScript 才能查看。
- 🔄 需在浏览器中开启 JavaScript 并刷新页面。
- 🤖 为自动化工具和辅助工具提供了访问方式。
- 📝 页面内容的 Markdown 版本可用。
- 🔗 可通过“View Markdown”查看 Markdown 内容。

---

### [](https://swmansion.com/changelog/reanimated-4-7-0/)

**原文标题**: [Reanimated 4.7.0](https://swmansion.com/changelog/reanimated-4-7-0/)

overview summary
- 🚀 Reanimated 4.7.0 于 2026 年 9 月 18 日发布，属于次要版本，核心变化是新布局动画引擎默认启用。
- 🧩 新的布局动画引擎成为默认；如遇回归可启用 `USE_LEGACY_LAYOUT_ANIMATIONS_PROXY` 回退，但不能与 `ENABLE_SHARED_ELEMENT_TRANSITIONS` 同时使用。
- 🎬 修复多项共享元素过渡问题，功能仍为实验性，需通过 `ENABLE_SHARED_ELEMENT_TRANSITIONS` 启用。
- 🖼️ `useAnimatedStyle` 新增 `backgroundImage` 支持，可传线性/径向渐变对象或 CSS 字符串，并在 UI 线程处理。
- 🎨 开启 `ANDROID_CSS_PLATFORM_TRANSITIONS` 后，Android 平台路径支持更多 CSS 过渡属性：`backgroundColor`、`borderColor`、数值 `borderRadius`、`shadowColor`（Android 9+），此前仅支持 `opacity`；该 flag 默认关闭。
- 📱 支持 React Native 0.86–0.88，搭配 Worklets 0.13.x；不再支持 React Native 0.83、0.84、0.85。
- ⚠️ 破坏性变更：Mutables 始终使用 Synchronizable，移除 `USE_SYNCHRONIZABLE_FOR_MUTABLES` flag。
- ⚠️ `AnimatedRefOnUI` 改为通过 `.value` 读取的 Shareable；`AnimatedRefOnJS` 更名为 `AnimatedRefOnRN`；未挂载 ref 上调用 `measure` 返回 `null` 并警告。
- 🛠️ 其他改进包括 CSS/动画修复、sticky header 修复、Jest 支持恢复、SPM 支持、Metro 类型修复、自定义 logger 回调、iOS reload 错误上报等。
- 👥 新增多位新贡献者，完整变更见 4.6.0...4.7.0 changelog。

---

### [](https://swmansion.com/changelog/worklets-0-13-0/)

**原文标题**: [Worklets 0.13.0 | Software Mansion](https://swmansion.com/changelog/worklets-0-13-0/)

Worklets 0.13.0 于 2026 年 9 月 18 日发布，是一次 Minor Release，重点增强 Bundle Mode 网络能力、引入 OXC/Rust Babel 插件、优化启动与微任务机制、精简序列化输出，并提升运行时稳定性；同时支持 React Native 0.88 和 iOS Swift Package Manager。后续补丁版本还修复了内存泄漏、崩溃、锁竞态与 babel-jest 缓存等问题。

- 🌐 Bundle Mode 的 Worklet Runtimes 现在内置独立网络模块，支持 XMLHttpRequest、fetch、Blob、FileReader、Headers、Request、Response、FormData、AbortController/AbortSignal，并取代 FETCH_PREVIEW_ENABLED 预览标志。
- ⚙️ createWorkletRuntime 新增 enableNetworking 选项，默认开启；没有 Event Loop 的运行时会被强制关闭。
- 🦀 Worklets Babel 插件新增基于 OXC 的 Rust 移植，用于 Bundle Mode，入口为 react-native-worklets/plugin-oxc/babel，并提供 macOS、Linux、Windows 的 x64/arm64 预编译二进制。
- 🔒 createSynchronizable 新增 fixedType，可用无序列化方式持有 number 或 boolean，并暴露 setDirty 非独占写入；C++ 端 Synchronizable 改为基于 std::variant，并引入 SynchronizableDynamic。
- ⚡ 启动更快：WorkletsModule 原生侧在模块创建时于后台线程构建，installTurboModule 只负责挂载；Bundle Mode 下 bundle 会在 UI Worklet Runtime 后台线程评估，同时 RN Runtime 也在评估。
- 🧵 Worklet Runtimes 改用 Hermes 内置微任务队列；queueMicrotask 入队原生 Hermes jobs，并在 UI Runtime 每次 requestAnimationFrame 回调后清空队列。
- 📦 序列化与 Babel 输出更精简：移除 Serializable handle，makeShareable 立即序列化并保留，RetainingSerializable 按运行时缓存；worklet 闭包用数组存储，无闭包 worklet 直接导出，移除隐式 worklet context，navigator 被视为已知全局。
- 🍎 iOS 可通过 Swift Package Manager 集成，包含 Package.swift 与 react-native.config.js 中的 SPM 元数据；同时支持 React Native 0.88。
- 🛡️ 提升 teardown 安全性，修复 Synchronizable 竞态与锁泄漏、Android 在 React 实例重建且动画运行时的崩溃、Babel 插件中 JSX、module.exports、workletized getter/setter/constructor 问题，以及 __proto__ 键序列化崩溃。
- 🧾 完整变更日志：worklets-0.12.2...worklets-0.13.0。
- 🗓️ 其他版本：0.12.2 修复 Android teardown 崩溃、__proto__ 序列化崩溃与 Synchronizable 锁卡住；0.12.1 新增 isOnUIThread；0.10.4/0.11.4 修复 iOS worklet runtime 线程内存泄漏并在后台暂停 Android UI loop；0.12.0 增加 WeakRef 支持并改进 Bundle Mode 脚本加载；0.11.3 恢复 babel-jest 转换缓存且不再修改共享选项。

---

### [](https://swmansion.com/changelog/react-native-screens-5-0-0-alpha-3/)

**原文标题**: [React Native Screens 5.0.0-alpha.3](https://swmansion.com/changelog/react-native-screens-5-0-0-alpha-3/)

本版本是 react-native-screens 5.0.0-alpha.3（预发布，2026-09-17），也是 5.0.0 的第三个 alpha，重点为 Stack v5 带来大量头部自定义能力、改进 Android FormSheet v5，并新增 iOS Swift Package Manager 支持与多项稳定性修复。

- 🚀 **版本定位**：5.0.0-alpha.3 预发布，聚焦 Stack v5 头部定制、FormSheet v5、Swift Package Manager 与 Stack/Tabs 稳定性。
- 📱 **Android Stack v5 头部增强**：新增副标题、标题/副标题定位、字体自定义、maxLines、溢出图标着色、工具栏 contentInset、头部背景色、状态栏遮罩色、宿主级配色方案。
- 🧰 **Android Stack v5 菜单与状态**：保留头部重建时的工具栏菜单状态，并支持运行时修改副标题的变通方案。
- 🍎 **iOS Stack v5 头部增强**：新增 backButtonTitle、backButtonDisplayMode、backButtonMenuEnabled、prompt、大标题/副标题外观、头部项 hidesSharedBackground、头部项动画标识。
- 🪟 **Android FormSheet v5**：新增 sheet 堆叠、拆分 onDismiss 与 onNativeDismiss，修复旋转后布局并使其位于键盘上方。
- 📦 **iOS 生态支持**：新增 Swift Package Manager 支持。
- 🐞 **Android Stack v5 修复**：修复工具栏菜单溢出顺序、原生视图状态恢复、配置变更后 forceLayout、头部返回按钮作用域等问题。
- 🧭 **iOS Stack v5 修复**：当未提供 headerConfig 时重构头部协调逻辑以隐藏头部。
- 🧩 **Android Stack v4/通用修复**：修复不透明到半透明屏幕弹出时的预加载/已关闭 fragment、SwipeRefreshLayout 过渡填充、RNSScreenRemovalListener 释放后使用崩溃。
- 🪟 **Android FormSheet v5 修复**：每次展示重建对话框、旋转时在测量阶段解析 sheet 指标、按原生容器尺寸计算 detents、防止 doOnStart 覆盖位移、将 sheet 移至键盘上方。
- 📑 **Android Tabs 修复**：防止 TabsScreen 原生视图状态恢复、配置变更后正确布局 tab bar、使用 ViewIdGenerator 标识 MenuItem、暴露 testID 为 viewIdResourceName。
- 🧪 **测试与维护**：新增多项 Stack/Tabs/FormSheet e2e 测试、测试目录脚本、共享 e2e-utils、发布测试自动化脚本，并更新 4.27.0 与 5.0.0-alpha.2 后的测试场景。
- 🔧 **其他改动**：支持 react-native@0.87.0，清理 iOS 构建警告、记录无效 SF Symbols/xcassets、重构 iOS 转换逻辑、SplitView 解耦、JS stack state config、示例与文档更新、CI 与依赖维护。
- 👥 **新贡献者**：欢迎 @mbSmaga、@Sullyvahnn-v2、@halskiszymon、@mackbrowne、@drhops、@kacperzolkiewski、@ilcato、@saddlepaddle 首次贡献。
- 📥 **来源**：GitHub 5.0.0-alpha.3 release notes；完整变更日志：5.0.0-alpha.2...5.0.0-alpha.3。

---

### [](https://github.com/rbayuokt/expo-infinite-media)

**原文标题**: [GitHub - rbayuokt/expo-infinite-media: Native paged media feed for Expo and React Native CLI. Vertical or horizontal paging of mixed video and images, with pooled players, predictive preloading and bounded caching. AVFoundation on iOS, Media3 on Android. · GitHub](https://github.com/rbayuokt/expo-infinite-media)

expo-infinite-media 是一个面向 Expo 与 React Native CLI 的原生分页媒体信息流组件，把视频和图片放进同一列表，默认垂直翻页，也可通过属性改为横向。它把播放、可见性判断、预加载、缓存、取消下载等核心逻辑交给 iOS/Android 原生代码处理，JS 只负责传数据、渲染覆盖层和接收事件，因此慢渲染或慢接口不会拖累视频播放。

- 📦 仓库为 `@rbayuokt/expo-infinite-media`，MIT 许可，支持 Expo SDK 55、RN 0.83 新架构、iOS 15.1、Android API 24；Web 不支持并抛 `UNSUPPORTED_PLATFORM`。
- 🎞️ 核心能力是视频与图片混合的分页信息流，垂直或水平滑动，每页一个帖子，媒体可按 `cover` 或 `contain` 显示。
- ⚙️ iOS 使用 AVFoundation/AVPlayer，Android 使用 Media3 ExoPlayer + DefaultPreloadManager；播放器池化，只有当前视频有声音。
- 🧠 原生侧负责判断当前屏幕项、切换播放器、准备下一个、管理缓存、取消已滑过帖子的下载，JS 不在播放路径中。
- 📥 Expo 安装：`npx expo install @rbayuokt/expo-infinite-media` 后执行 `npx expo prebuild`；需开发构建，Expo Go 不支持。
- 📥 React Native CLI 安装：先 `npx install-expo-modules@latest`，再 `npm install @rbayuokt/expo-infinite-media`，最后 `npx pod-install`。
- 🎚️ `scrubber` 可选，需要 `react-native-reanimated` 和 `react-native-gesture-handler`；未安装时其余功能可用，scrubber 会跳过并警告。
- 🧱 用法是 `<InfiniteMediaFeed data={items} onIndexChange renderOverlay ... />`；每个 item 必须有稳定 `id`，原生只接收 `id/type/uri/poster/headers/cacheKey`。
- 🪟 默认 `windowSize: 2`，只挂载当前页两侧少量页面；1000 项列表也只挂载少量 React 页面。
- 🎬 翻页基于 React Native `ScrollView` 分页，原生监听滚动并决定最可见页；poster 会一直显示到平台确认首帧渲染，避免黑帧。
- 🚀 预加载策略：下一项 P1 准备播放器并缓存启动范围，下下项 P2 只写磁盘；启动范围约 Wi-Fi 1.5MB、蜂窝 512KB，从不预载完整文件。
- 🛑 内存紧张、低端机、低数据模式、热压力、当前缓冲不健康、快速滑动、离线或后台时会降低或停止投机预加载。
- 🗃️ 缓存全局共享并按 LRU 淘汰，默认视频 500MB、图片 200MB；预载字节与播放字节相同，当前项和下一项会被固定避免误删。
- 📊 基准测试跑 1200 项、60 秒、每 3 秒一项；iPhone 11 Pro 冷启动约 107MB，OPPO Reno5 F 约 132MB，热缓存下 iPhone 0MB、Android 仍花 4.4MB 投机流量。
- 🧪 基准局限：样本约 30 个源文件重复，真实唯一内容、慢网或低端机表现可能更差；跨平台缓存命中率不可直接比较。
- 🧭 主要 Props 包括 `data`、`renderOverlay`、`initialIndex`、`horizontal`、`windowSize`、`active`、`autoplay`、`loop`、`muted`、`resizeMode`、`preload`、`diagnostics`、`scrubber` 等。
- 🔔 主要事件包括 `onIndexChange`、`onPlaybackStateChange`、`onFirstFrame`、`onProgress`、`onError`、`onEndReached`、`onSeek`、`onScrubStart`、`onScrubEnd`、`onMetrics`。
- 🧰 Ref 提供 `play()`、`pause()`、`seekTo()`、`setMuted()`、`scrollToIndex()`、`retry()`；模块函数包括 `configure`、`preload`、`cancelPreload`、`clearCache`、`removeFromCache`、`getCacheSize`、`getCacheStatus`。
- 🔁 数据追加只把新项发给原生，不打断当前播放；替换列表时原生按 `id` 保留状态；重复 `id` 会在开发环境警告。
- 🧯 错误类型为 `InfiniteMediaError`，含 `code`、`recoverable`、`attempt` 等；当前项按 0.5s、1s、2s 重试三次，4xx（除 408/429）和不支持格式不重试。
- 📱 示例应用包含 Feed、Stress、Layouts、Cache 四个屏幕；Stress 有 1200 项、自动滑动和挂载/卸载循环，内置 403 视频与缺失图片错误路径。
- 🛠️ 开发命令包括 `npm run build`、`lint`、`typecheck`、`test`、`test:ios`、`test:android`、`example:ios`、`example:android`；纯 Swift/Kotlin 核心有对应测试。
- ⚠️ 已知限制：JS 长时间阻塞可能导致空白页，可提高 `windowSize`；iOS 渐进式视频不能 AirPlay；Android Coil 无单请求优先级；不保证帧率；HLS 在 iOS 不走磁盘缓存，DASH 不支持 iOS 且 Android 未捆绑模块。
- ✅ 生产建议：稳定 `id`、为变化 URL 设置 `cacheKey`、每个视频配 poster、MP4 使用 `+faststart`、合理配置磁盘预算、离屏 feed 设 `active={false}`、覆盖层 memo、处理 `onError`、生产关闭 `diagnostics`，并在低端 Android 上做 release 性能测试。

---

### [](https://github.com/AmatoGiulio/react-native-numeric-text)

**原文标题**: [GitHub - AmatoGiulio/react-native-numeric-text: High-fidelity numeric text transitions for React Native, rendered natively on iOS and Android. · GitHub](https://github.com/AmatoGiulio/react-native-numeric-text)

react-native-numeric-text 是 AmatoGiulio 开发的开源 React Native 组件，用于在 iOS 和 Android 上以原生方式实现高保真数字文本过渡。iOS 17+ 直接使用 SwiftUI 的 `.contentTransition(.numericText())`，Android 则使用专门构建并逐帧对齐 iOS 效果的原生渲染器，面向 React Native 新架构 Fabric。它适合计数器、余额、价格、比分、计时器等数字频繁变化的场景。

- 📊 仓库信息：AmatoGiulio/react-native-numeric-text 为公开项目，约 81 Star、4 Fork、177 次提交，采用 MIT 许可证，并提供行为准则与贡献指南。
- 🎯 核心目标：把格式化数字视为有结构的过渡系统，而不是简单地在字符串之间淡入淡出。
- 📱 平台实现：iOS 17+ 使用 SwiftUI 原生 numericText；Android 使用专用原生渲染器，并以 iOS 输出为基准逐帧校准。
- ⚙️ 主要特性：原生渲染、无 JS 逐位动画、稳定中断、快速重定向、连续增减不重启。
- 🔢 结构处理：支持整数位、小数位、分组/小数点分隔符、符号，以及 `999 → 1,000`、`9.99 → 10.00` 等结构变化。
- 🌍 格式化能力：`format` 是 `Intl.NumberFormatOptions` 的子集，由各平台原生格式化器解析；`locale` 默认 `en-US`，避免设备语言改变布局。
- 💱 货币与百分比：`currency` 是 `format={{ style: 'currency', currency }}` 的简写，支持符号/ISO 代码、会计负数、百分比，并按货币自动决定小数位。
- 🎨 显示选项：支持 `fractionColor` 双色金额、`textAlign` 左/中/右对齐，以及 `direction` 控制向上或向下滚动。
- ♿ 动效可访问性：`reduceMotion` 支持 `system`、`always`、`never`，可跟随系统减弱动态效果设置。
- 🔗 Reanimated 集成：可选依赖 `react-native-reanimated >= 3`，可把 shared value 作为 `value`，从 UI 线程驱动且避免 JS 重渲染。
- 📦 安装方式：使用 npm 或 yarn 安装，包会自动链接；iOS 需执行 `cd ios && pod install`；不传 shared value 时无需 Reanimated。
- 🧩 快速使用：通过 `<NumericText value={...} style={...} />` 即可，首次渲染立即显示，后续值变化触发原生过渡。
- 📋 API 要点：支持 `value`、`locale`、`format`、`currency`、`direction`、`animationDuration`、`reduceMotion`、`useGrouping`、小数位、`fractionColor`、`style`、`testID` 等。
- 🧮 舍入一致性：iOS、Android 和 Web 统一使用 half-away-from-zero，确保不同渲染器不会对数字结果产生分歧。
- 🖥️ 平台行为：iOS 17+ 有原生过渡，旧 iOS 仍可原生格式化渲染；Android API 31+ 使用 RenderNode + RenderEffect 模糊，API 24–30 使用软件层模糊；Web 仅显示正确格式化文本，不播放过渡。
- 🔬 实现原理：Android 渲染器会排版整行数字，为数字和分隔符赋予结构身份，并逐帧解析运动；参数由 SwiftUI 动画逐帧反推，如 0.59375、0.3984375、0.15 秒级联等。
- 📚 文档与示例：`docs/ARCHITECTURE.md` 和 `docs/METHODOLOGY.md` 说明架构与方法；`example/` 展示 shared value 用法并打印 React 渲染次数。
- 🙏 致谢与许可：格式化 API 借鉴 number-flow；货币/百分比由 @Amanfromearth 贡献起步；灵感来自 Nathan Schroeder 的 Expo UI 演示；项目采用 MIT，Android 字体使用 SIL OFL 1.1。

---

### [](https://github.com/adnxy/react-native-secure-webview)

**原文标题**: [GitHub - adnxy/react-native-secure-webview: Secure WebView for React Native auth, checkout, OAuth, and other controlled web flows. · GitHub](https://github.com/adnxy/react-native-secure-webview)

react-native-secure-webview 是一个专为受控网页流程（如身份验证、结账、OAuth 重定向和 3-D Secure 挑战）设计的 Fabric 原生 WebView 组件。它采用“默认拒绝”的安全策略，所有顶层导航均在原生层依据精确的来源白名单进行校验，服务器重定向不会进入 JS，自定义 scheme 重定向会被拦截并以事件形式暴露，网页到原生的桥接仅支持单一字符串方法。该库仅支持新架构，要求 React Native 0.85+ 并启用 Fabric，无 Paper 回退方案。

- 🔒 **核心定位**：不是通用浏览器视图，而是默认拒绝的受控 WebView，用于认证、结账、OAuth 等安全敏感场景
- 🏗️ **真实 Fabric 组件**：iOS 使用 WKWebView，Android 使用 android.webkit.WebView，并非 react-native-webview 的封装
- 🎯 **精确来源匹配**：严格比对 scheme、host 和有效端口，不支持通配符、子串匹配或“开头匹配”
- 🛡️ **原生强制执行**：服务器重定向永远不进入 JS，策略在两端原生代码中执行
- ⛔ **失败即关闭**：无效配置项被丢弃、未知 URL 被阻止、不支持的功能直接报错而非静默降级
- 📋 **环境要求**：React Native 0.85+（启用新架构）、iOS 15.1+、Android minSdk 24
- 📦 **安装简便**：`npm install react-native-secure-webview` 后执行 `pod install`，无需手动原生配置，通过 Codegen 注册
- 🧪 **Jest 配置**：包以未转译 ESM 发布，需在 `transformIgnorePatterns` 中放行
- ⚙️ **主要 Props**：`source`、`allowedOrigins`、`allowedSchemes`、`session`、`onNavigation`、`onDeepLink`、`onMessage`、`onError`、`onSecurityViolation`
- 🕹️ **命令接口**：通过 ref 调用 `reload()`、`goBack()`、`goForward()`、`stopLoading()`，卸载后调用为无操作并给出开发警告
- 🧭 **导航策略**：白名单来源的 http(s) 加载；其他来源阻止并触发 `origin_not_allowed`；白名单自定义 scheme 阻止并触发 `onDeepLink`；未知 scheme 触发 `scheme_not_allowed`；无法解析或恶意 URL 触发 `invalid_url`
- 🍪 **会话行为**：iOS 支持 `persistent` 与 `ephemeral`；Android 因 CookieManager 为进程级共享，`ephemeral` 会失败关闭并报 `ephemeral_not_supported`
- 💬 **消息桥接**：仅支持页面调用 `window.ReactNativeSecureWebView.postMessage(string)`，仅接受主框架且白名单来源的消息，无 RN 到 Web 消息、无 JS 注入、无类型化 RPC
- 📱 **示例应用**：`example/` 目录提供每种行为的演示预设（允许浏览、阻止来源、深链与消息、临时会话、加载错误）
- 🚫 **不在范围内**：JS 注入、本地文件与 HTML 字符串、下载、弹窗与 window.open、媒体/摄像头/地理定位权限、RN 到 Web 消息、Cookie API、OAuth 或支付 SDK 集成
- 📄 **开源许可**：MIT 协议，GitHub 上获得 125 颗星，附带行为准则、贡献指南和安全策略文档

---

### [](https://github.com/DorianMazur/react-native-screen-choreography/releases/tag/v0.6.0)

**原文标题**: [Release 0.6.0 · DorianMazur/react-native-screen-choreography · GitHub](https://github.com/DorianMazur/react-native-screen-choreography/releases/tag/v0.6.0)

DorianMazur/react-native-screen-choreography 发布 v0.6.0，由 DorianMazur 于 9 月 17 日发布，包含 11 次提交；仓库当前有 195 个 Star、4 个 Fork，无开放 Issue 或 PR。该版本重点新增揭示动画、共享元素进度、屏幕淡入淡出、时长弹簧与交互手势生命周期，并强化转场中断与手势处理，同时移除旧版 useStaggeredReveal，带来破坏性变更。

- 📦 版本信息：v0.6.0 已发布至 main，发布时间为 9 月 17 日 14:29，包含 11 次提交。
- ✨ 新增 useRevealStyle 与作用域声明式 Enter/Exit 揭示，支持动态列表安全错峰、水平/垂直位移、缩放和减少动态效果。
- 🎬 演示范围揭示会跟随其保留的所有者，包括静止终点。
- 📊 useSharedElementPresentation 新增 presentationProgress，在无关转场期间保持稳定。
- 🖥️ ChoreographyScreen 新增 screenFade 和 keepVisible，可配置屏幕交叉淡入淡出与持久背景。
- ⏱️ 支持基于时长的弹簧参数 duration 和 dampingRatio，包括返回与交互式稳定。
- 👆 新增 useInteractiveGestureLifecycle，可在准备阶段缓冲移动与提前释放，并支持会话绑定交互句柄和可中止准备。
- 🧭 自定义转场渲染器可获得匹配的会话几何锚点。
- 🛠️ 修复：强化转场中断、交互手势取消与稳定、输入交接；Android 转场覆盖层支持触摸穿透；动画完成回调会保留至交付。
- 💥 破坏性变更：移除 useStaggeredReveal 及其 getItemStyle；需改用 useRevealStyle，或使用带 index 和 count 的声明式 Enter/Exit。
- 📚 提供 reveal 迁移指南和 interactive-back 指南，并包含 2 个发布资产。

---

### [发布 v6.0.0 · gre/react-native-view-shot · GitHub](https://github.com/gre/react-native-view-shot/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · gre/react-native-view-shot · GitHub](https://github.com/gre/react-native-view-shot/releases/tag/v6.0.0)

react-native-view-shot 发布 v6.0.0，这是一次包含破坏性变更的重要更新，并带来多项 Android、iOS、Windows 修复，以及文档、示例和 CI 改进。该仓库目前约有 2.9k stars、375 forks。

- 🚨 v6.0.0 为重大版本，包含 Breaking Changes
- 🌐 Web 端：`html2canvas-pro` 变为可选 peer dependency，若目标平台是 Web，需运行 `npm install html2canvas-pro`
- 📱 依赖要求：需要 `react-native >= 0.80`，以支持 RN 0.87 Strict TypeScript API
- 🛡️ 修复：拒绝非有限的 `width`、`height`、`quality` 选项
- 🤖 Android：捕获缓冲区线程安全，并按实际 bitmap 尺寸编码
- 🔍 Android：针对 TextureView/SurfaceView，围绕 view pivot 进行缩放
- 🍎 iOS：`releaseCapture` 仅限直接 tmp 文件
- 🪟 Windows：读取完整捕获流，修复 JPEG quality boxing
- 🧹 清理：移除未使用的 imports
- 📚 文档与示例：修复捕获示例和 README 中的 RAW 语义，并修复 example app
- ⚙️ 工具与 CI：更安全的示例安装、更严格的 snapshot import，以及 CI 和依赖升级
- 👥 贡献者：gadcam、Nodonisko 及另外 2 位贡献者；发布包含 2 个资产，并获得 1 个 ❤️ 反应

---

### [](https://github.com/margelo/react-native-nitro-sqlite/releases/tag/v9.8.0)

**原文标题**: [Release Release 9.8.0 · margelo/react-native-nitro-sqlite · GitHub](https://github.com/margelo/react-native-nitro-sqlite/releases/tag/v9.8.0)

react-native-nitro-sqlite v9.8.0 已发布，由 chrispader 于 9 月 17 日发布，自 v9.7.0 起包含 24 个提交，主要改进 iOS 数据库存储、SQLite 性能与线程安全，并更新示例应用、依赖和构建配置。

- 🚀 发布版本：v9.8.0（2026-09-17），发布者 chrispader，含 24 个提交至 main，提交已通过 GPG 验证。
- ⭐ 仓库概况：margelo/react-native-nitro-sqlite 为公开仓库，约 566 star、53 fork、30 个 issue、25 个 PR。
- ✨ 新功能：示例应用新增数据库迁移测试屏幕（#354）。
- 📁 iOS 存储：新增将数据库存储在 Library/Application Support 的选项（#323，关闭 #289）。
- 🔐 iOS 存储安全：安全地将数据库存储在 Application Support（#324，关闭 #289）。
- ⚙️ iOS 性能：支持配置 SQLite 性能模式（#328）。
- ⚡ 性能优化：查询结果仅物化一次（#320）。
- 🐛 Bug 修复：示例应用采用 iOS scene 生命周期（#355）。
- 🧵 线程安全：配置 SQLite 线程安全（#325），并序列化 SQLite 操作、保护连接生命周期（#326）。
- 🏗️ 构建配置：配置 TypeScript project references（#330），示例升级至 React Native 0.87.1（#356），更新 lockfiles。
- 📦 依赖升级：Nitro Modules 与 Nitrogen 升级至 0.37.1（#353）。
- 👥 新贡献者：@huytdps13400（#320）和 @NicolasBonet（#323）首次贡献。
- 🔗 其他信息：完整变更日志为 v9.7.0...v9.8.0，发布资产共 2 个。

---

### [](https://github.com/getsentry/sentry-react-native/releases/tag/8.27.0)

**原文标题**: [Release 8.27.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.27.0)

overview summary
Sentry React Native 8.27.0 已发布，重点新增 Session Replay 运行时手动控制、按类掩码和 iOS 实验性防前台恢复卡死选项；同时修复 Android 崩溃、iOS 新架构图像掩码、传播上下文与 NDK 兼容问题，并升级 CLI、JS、Android、Cocoa SDK。注意 iOS 原生崩溃分组哈希变化可能触发一次性重新分组。

- 📦 版本：8.27.0 为最新版本，由 sentry-release-bot 于 9 月 17 日发布。
- ⚠️ 警告：iOS 原生崩溃现在设置 mechanism.synthetic，并将 mach/signal 名称移出分组哈希，应用采用后预计会有一次性重新分组。
- 🎬 新增 Session Replay 运行时控制，可通过 Sentry.getReplay() 访问活动回放，并在 iOS、Android、Web 上使用相同 API 手动 start、startBuffering、stop、pause、resume、flush；pause/resume 在 Web 为 no-op。
- 🎭 在 mobileReplayIntegration 中新增 maskedViewClasses/unmaskedViewClasses，支持按类进行 Session Replay 掩码。
- 🧪 在 iOS 的 mobileReplayIntegration 中新增实验性 avoidForegroundResumeHang，以规避回到前台且视图层级繁重时 Session Replay 恢复捕获可能导致的致命 App Hang。
- 🐛 修复 Android 快速导航下 getNewScreenTimeToDisplay 导致的致命 "JavaCallback was already settled" 崩溃。
- 🖼️ 修复 iOS 新架构下启用 maskAllImages 时，Session Replay 未遮蔽 React Native <Image> 的问题。
- 🧭 修复后台根 span（app-start、expo-updates）不再覆盖活动导航 trace 的原生传播上下文。
- 🛠️ Android 现在尊重宿主应用固定的 ndkVersion，避免 AGP 为模块原生代码下载默认 NDK。
- ⬆️ 依赖升级：CLI v3.7.0→v3.8.0、JavaScript SDK v10.74.0→v10.75.0、Android SDK v8.56.0→v8.57.0、Cocoa SDK v9.28.0→v9.29.0。

---

### [](https://github.com/mdjastrzebski/test-renderer/releases/tag/v1.3.0)

**原文标题**: [Release v1.3.0 · mdjastrzebski/test-renderer · GitHub](https://github.com/mdjastrzebski/test-renderer/releases/tag/v1.3.0)

mdjastrzebski/test-renderer 的最新版本 v1.3.0 已发布，主要新增 React 19.3 支持，并更新了 changelog、React 19.3 支持说明及 async/act 测试文档；该公开仓库目前有 23 星、3 个 fork。

- 🏷️ 最新版本：v1.3.0，发布日期为 2026-09-17（页面显示 9 月 17 日 11:17）。
- 🚀 核心特性：新增 React 19.3 支持（#56，提交 1886ec5）。
- 📚 文档更新：更新 changelog、React 19.3 支持说明，以及使用 async 和 act 进行测试的文档（#55，提交 e8f23c4）。
- 📦 发布资源：v1.3.0 附带 2 个资源。
- ⭐ 仓库状态：mdjastrzebski/test-renderer 为公开项目，当前 23 星、3 个 fork。
- 🧾 协作状态：当前 Issues 为 0、Pull requests 为 0。
- 🧭 其他信息：页面包含 Code、Issues、Pull requests、Discussions、Actions、Projects、Security and quality、Insights 等导航入口。
- ⚠️ 页面提示：部分内容加载出错或没有筛选结果，建议重新加载页面。

---

### [](https://github.com/LegendApp/legend-list/releases/tag/v3.4.0)

**原文标题**: [Release v3.4.0 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.4.0)

LegendApp/legend-list 发布最新版 v3.4.0，由 jmeistrich 于 9 月 21 日发布；本次更新新增 onReady 回调，集中修复滚动跟随、到达回调、initialScrollIndex 相关问题，并优化快速滚动预加载。仓库当前约 3.4k stars、149 forks、63 个 issues、30 个 pull requests。

- 🆕 **新增 onReady**：在每次初始放置和滚动周期完成后调用，包括因 dataKey 变化而重新启动的周期。
- 🔧 **修复尾随跟随与动画程序化滚动**：在 footer、视口和原生布局变化时保持对齐，用户拖动会取消排队的跟随请求。
- ✅ **修复 onStartReached 和 onEndReached**：布局与数据集重置后可靠触发，包括短列表和跨多个事件越过阈值的手势。
- 📌 **修复 initialScrollIndex**：数字值指向最后一行时，从末尾打开会包含 footer。
- ⚡ **性能优化**：快速滚动会按移动方向准备行，包括向上和末尾对齐滚动，使下一内容更早就绪。
- 📦 **版本信息**：v3.4.0 为最新版本，提交 212bc13，含 2 个资产；获得 👍6、🎉3、❤️5、🚀3、👀2，共 10 人回应。
- 📊 **仓库状态**：Public 仓库，拥有 3.4k stars、149 forks、63 个 issues、30 个 pull requests，并提供 Discussions、Actions、Projects 等模块。

---

### [](https://github.com/thiagobrez/react-native-arrangement-view)

**原文标题**: [GitHub - thiagobrez/react-native-arrangement-view · GitHub](https://github.com/thiagobrez/react-native-arrangement-view)

这是一个面向 React Native 的可折叠设备自适应排列与铰链观察库，核心提供 `ArrangementView` 和 `useHingeChange`，支持 `split` / `overlay` 布局，目前主要面向 iOS，Android 支持即将推出。

- 📱 仓库为 `thiagobrez/react-native-arrangement-view`，用于折叠设备自适应排列视图和铰链观察。
- 📦 安装方式：`yarn add react-native-arrangement-view`，然后执行 `cd ios && pod install`。
- 🚫 不支持 Expo Go，需使用 development build，例如 `npx expo run:ios`。
- 🧩 `ArrangementView` 需要 `ArrangementView.Primary` 和 `ArrangementView.Secondary` 作为槽位标记；它们不自行渲染，也不影响布局。
- ⚙️ 主要 props：`children` 必填；`arrangement` 默认 `"split"`，可选 `"overlay"`；`axes` 默认 `"both"`，可选 `"horizontal"` / `"vertical"`；`observeHinge` 默认 `true`。
- 📐 布局要求：给 `ArrangementView` 有界尺寸，通常用 `flex: 1`；每个窗格根节点也用 `flex: 1` 填满空间。
- 🪟 在 `overlay` 模式中，primary 位于 secondary 前方；可用透明 primary 背景和 `pointerEvents="box-none"` 实现浮动控件。
- 🧷 隐藏窗格不会卸载其 React 树；组件本身不添加安全区内边距，需自行置于安全区域内或处理 insets。
- 🪝 `useHingeChange` 应在任一窗格内的组件中调用，观察最近的 `ArrangementView`，并非全局传感器订阅。
- 📊 铰链状态 `HingeState` 包含：`available`、`angle`（弧度或 `null`）、`status`（`unknown` / `closed` / `partiallyOpen` / `fullyOpen`）。
- 🍎 回退行为：iOS 27.1 以下或旧 SDK 构建时，`split` 仅显示 primary；`overlay` 全尺寸 primary 覆盖 secondary；`axes` 无效，铰链状态不可用。
- 📄 项目采用 MIT 许可证，仓库包含示例 Expo 应用、测试等；当前约 10 stars、0 forks、11 commits、0 issues、2 pull requests。

---

### [](https://github.com/ifeoluwak/react-native-skia-layout)

**原文标题**: [GitHub - ifeoluwak/react-native-skia-layout: Bring Flexbox layouts, positioning, and sizing to React Native Skia using Yoga. · GitHub](https://github.com/ifeoluwak/react-native-skia-layout)

`react-native-skia-layout` 是一个为 React Native Skia 提供 Flexbox 布局、定位与尺寸计算的开源库，基于 Yoga 布局引擎，让 Skia 图形、文本、图片和 SVG 能像 React Native 组件一样使用 flex 属性排版。

- 🧩 核心目标：用熟悉的 flexbox 属性定位和缩放 Skia 元素，避免手动计算 x/y。
- 📦 安装：`npm install react-native-skia-layout react-native-nitro-modules @shopify/react-native-skia`。
- 📱 Expo：支持开发构建与 EAS Build，不支持 Expo Go；Web 也不支持，无 JS/WASM 回退。
- ⚙️ 环境要求：需启用 New Architecture；旧版 Expo SDK 需 iOS 16.0+，建议用 `npx expo install` 对齐版本。
- 🚀 快速开始：用 `FlexCanvas` 作为根画布，`FlexLayout` 作为 flex 容器，内部放 `LayoutCircle`、`LayoutRect` 等布局组件。
- 🧱 工作原理：`FlexCanvas` 提供布局视口宽高；`FlexLayout` 像 `<View>` 一样嵌套；布局组件按计算位置渲染。
- 🧮 容器属性：支持 direction、flex、gap、wrap、justifyContent、alignContent、alignItems、padding、margin、position、debug 等。
- 🧩 布局组件：包含 Rect、RoundedRect、Circle、Oval、Path、Points、Image、Svg、Text、Paragraph 等。
- 🐞 调试：给 `FlexLayout` 或布局组件加 `debug` 可绘制计算边界描边，便于可视化布局。
- ⚠️ 限制：暂不支持动画属性；布局属性必须是普通 JS 值，不能是 Reanimated SharedValue 等动画类型。
- 🔄 性能注意：修改布局会触发 React 重渲染和完整布局过程，尚未实现 UI 线程逐帧驱动布局。
- 📚 示例与许可：`example/app` 演示 row/column、嵌套、绝对定位、文本/段落布局；项目为 MIT 许可。

---

### [](https://pulsar.swmansion.com/studio)

**原文标题**: [Create Custom Haptics | Pulsar Studio Visual Editor](https://pulsar.swmansion.com/studio)

未提供需要总结的文本，暂时无法生成文章摘要。请补充具体内容后，我将为你提炼关键要点。

- 📭 当前输入为空，没有可总结的信息。
- ✍️ 请粘贴或发送需要总结的文章、段落或链接。
- 🧾 收到内容后，我会按“- emoji 要点”的格式整理。
- 🎯 摘要将覆盖核心观点、关键信息与重要结论。

---

### [](https://raw.githubusercontent.com/software-mansion/enriched-markdown/main/packages/enriched-markdown-ios/README.md)

**原文标题**: [README.md](https://raw.githubusercontent.com/software-mansion/enriched-markdown/main/packages/enriched-markdown-ios/README.md)

Enriched Markdown iOS 是 Software Mansion 推出的独立 SwiftUI 库，用于在 iOS 上渲染增强 Markdown，以 Swift Package 形式分发，核心产品为 `EnrichedMarkdown`，并可选用 `EnrichedMarkdownLaTeX` 渲染数学公式。

- 📦 独立于 React Native npm 包，通过 Swift Package Manager 安装，要求 iOS 16+ 与 SwiftUI。
- 🧩 提供两个产品：`EnrichedMarkdown` 和可选的 `EnrichedMarkdownLaTeX`；不引入 LaTeX 可节省约 3–5 MB，`$…$` 会保持纯文本。
- 🚀 使用 `EnrichedMarkdownText` 快速渲染 Markdown，链接交互通过 `.onLinkPress` 等环境修饰符处理。
- 🎨 使用 `MarkdownTheme` 结果构建器 DSL 定制样式，主题可分层叠加，子层只覆盖自身设置的属性。
- 🌓 通过 `rememberMarkdownTheme` 响应深色模式与动态字体变化，推荐使用语义颜色实现自动明暗适配。
- 🧱 主题元素覆盖段落、标题、链接、粗体、斜体、删除线、下划线、上下标、高亮、剧透、代码、引用、提示、列表、任务列表、表格、图片、分割线和数学。
- 🧾 核心 API 为 `EnrichedMarkdownText(markdown, flags:)`；`Md4cFlags` 可控制下划线、软换行、空行保留、自动链接、上下标、高亮和 GitHub 提示等。
- 🔗 支持链接点击/长按、任务列表勾选切换，以及粒子/实心/自定义遮罩的剧透点击显示。
- 📋 选择菜单支持 Copy as Markdown、Copy Image URL(s)、Select All；系统复制同时输出纯文本和 HTML。
- 🖼️ 图片支持 http(s)、file、绝对路径、data: 和 Bundle 资源，下载会缓存并降采样；块图片可设置高度、最大高度、宽高比与填充模式。
- ♿ VoiceOver 按元素导航标题、链接、图片、列表、引用、表格、代码块、数学和转子，并可通过 `.markdownAccessibilityLabels` 本地化朗读字符串。
- 📊 GFM 表格为实时视图，列宽自适应，超宽可横向滚动，单元格支持内联样式，长按可复制为 TSV 或 Markdown。
- 🌍 逐段解析 RTL/LTR 方向，列表标记、复选框和引用条跟随段落方向，代码块始终从左到右；可用 `.markdownWritingDirection` 强制方向。
- 🧮 导入 `EnrichedMarkdownLaTeX` 后通过 `.markdownLaTeX()` 启用数学渲染：`$…$` 行内、`$$…$$` 块级并支持横向滚动，样式由 `MathBlock()` 与 `InlineMath()` 控制。
- 📝 支持标题、段落、粗斜体、行内代码、删除线、下划线、上下标、高亮、剧透、代码块、引用、GitHub alerts、列表、任务列表、GFM 表格、链接图片、自动链接、分割线和 LaTeX 数学。
- 🛠️ 开发命令通过 `yarn workspace @enriched-markdown/ios build/test/clean` 调用 `swift build`、`swift test`、`swift package clean`；monorepo 同步时需解引用符号链接。
- 🧩 非 SwiftUI 场景可使用 `MarkdownRenderer.render` 和 `renderLaTeX`，并传入写入方向与布局方向参数。

---

### [发布 v](https://github.com/callstack/agent-device/releases/tag/v0.21.12)

**原文标题**: [Release v0.21.12 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.21.12)

callstack/agent-device 的 GitHub 页面显示最新版本为 v0.21.12，由 thymikee 发布，主要包含两项 iOS 功能更新；仓库当前约有 4.8k Stars、312 Forks，同时页面存在部分加载错误提示。

- 📦 仓库：callstack/agent-device，公开仓库
- ⭐ 数据：约 4.8k Stars，312 Forks；85 个 Issues，18 个 Pull Requests
- 🏷️ 最新版本：v0.21.12（Latest），提交哈希为 01328de
- 👤 发布者：thymikee，发布时间为 9 月 22 日 19:19
- 🔁 自上一版本以来，共有 42 个提交合并到 main
- 🍎 iOS 更新：通过模拟器 HID 无头折叠 Duo，关联 #2762
- 🎬 iOS 更新：使用定时铰链关键帧实现折叠动画，关联 #2763
- 📜 完整变更日志：v0.21.11...v0.21.12
- 🙌 贡献者：thymikee
- 📎 发布资源：8 个 Assets
- ⚠️ 页面提示：部分内容加载出错，需重新加载页面

---

### [](https://github.com/delacournz/delacour-ui)

**原文标题**: [GitHub - delacournz/delacour-ui · GitHub](https://github.com/delacournz/delacour-ui)

overview summary
delacournz/delacour-ui 是一个公开的 React Native 组件库仓库，包含组件库与 Expo 演示应用，采用 Uniwind、Reanimated、Gesture Handler 和 Pulsar，MIT 许可，目前 9 星、0 fork、162 次提交。

- 📦 仓库公开，已有 9 stars、0 forks、162 commits、2 个 pull requests，Issues 为 0。
- 🧩 核心是 React Native 组件库，以及用于在设备上展示所有组件的 Expo 应用。
- 🎨 样式使用 Uniwind（面向 React Native 的 Tailwind v4），交互使用 Reanimated 和 Gesture Handler，触觉反馈使用 Pulsar。
- 🚫 组件库不依赖特定框架，也不使用第三方组件套件。
- 🗂️ 主要包包括 @delacour/react-native-ui（组件库，按组件子路径导出，无构建步骤）、@delacour/playground（Expo 演示应用）以及配置、类型、技能等辅助包。
- ⚙️ 入门需要 Bun 1.3+；playground 还需要 Xcode 或 Android Studio，并使用 expo-dev-client，不能在 Expo Go 中运行。
- 🧪 常用命令包括 bun install、bun expo prebuild、bun ios / bun android、bun dev；开发检查用 bun run typecheck、bun run check、bun test。
- 📝 库测试只覆盖纯逻辑；需要渲染器的内容在 playground 模拟器中验证。
- 📚 每个包的 AGENTS.md 是实际文档，记录设计决策、约束和理由，另有仓库规范、组件库规则和 playground 文档。
- 📦 许可为 MIT，发布包包括 delacour CLI、@delacour/react-native-ui、@delacour/react-native-charts，其余工作区包为私有。
- 🔗 仓库未提供描述、网站或主题，主要资源为 Readme、Activity 和自定义属性。

---

### [](https://apex.callstack.com/)

**原文标题**: [Apex â Frontier React Native LLM](https://apex.callstack.com/)

Apex 是一款针对 React Native 优化的高性价比 AI 模型；访问相关网站需启用 JavaScript，或向 Callstack 申请测试版访问权限。

- 💰 Apex 是兼顾成本效益的 AI 模型。
- ⚛️ 它专门针对 React Native 进行优化。
- 🌐 要查看该网站，需启用 JavaScript。
- 🔑 也可向 Callstack 申请 beta 访问权限。

---

### [Expo SDK 58：你的应用准备好迎接 iPhone Duo 了吗？ - YouTube](https://www.youtube.com/watch?v=mK6QKSyPCvk)

**原文标题**: [Expo SDK 58: Is Your App Ready for iPhone Duo? - YouTube](https://www.youtube.com/watch?v=mK6QKSyPCvk)

这是 YouTube 页面底部的导航链接与版权信息集合，涵盖平台介绍、政策条款、联系与开发者入口，以及 Google 的版权声明。

- ℹ️ 关于：了解 YouTube 平台信息
- 📰 新闻：查看媒体与新闻相关内容
- ©️ 版权：获取版权相关信息
- 📬 联系我们：提供联系方式入口
- 🎬 创作者：面向内容创作者的相关资源
- 📢 广告：广告投放与合作信息
- 💻 开发者：开发者相关资源与接口入口
- 📜 条款：查看服务条款
- 🔒 隐私：查看隐私政策
- 🛡️ 政策与安全：了解平台政策与安全内容
- ⚙️ YouTube 的运作方式：说明平台运作机制
- 🧪 测试新功能：参与或了解新功能测试
- © 2026 Google LLC：版权归属于 Google LLC

---

### [如果你的应用能自我修复呢？ - YouTube](https://www.youtube.com/watch?v=MUFlnOXi-o4)

**原文标题**: [What if your app could fix itself? - YouTube](https://www.youtube.com/watch?v=MUFlnOXi-o4)

该内容为 YouTube 页脚导航与法律信息，主要列出平台介绍、合作资源、政策条款及版权声明等入口。

- ℹ️ 提供关于、新闻、版权与联系我们等基础信息入口。
- 🎬 包含创作者、广告与开发者等合作及扩展资源。
- 📜 列出条款、隐私、政策与安全等法律合规链接。
- ⚙️ 说明 YouTube 的运作方式，并提供新功能测试入口。
- ©️ 版权归属标注为 © 2026 Google LLC。

---

### [09.md](https://raw.githubusercontent.com/tc39/agendas/main/2026/09.md)

**原文标题**: [09.md](https://raw.githubusercontent.com/tc39/agendas/main/2026/09.md)

Ecma TC39 第 116 次全会将于 2026 年 9 月 29 日至 10 月 1 日在日本东京由 Sony 主办，前两天为 10:00–17:00 JST、最后一天为 10:00–16:00 JST，预计会议容量约 15 小时。议程涵盖秘书/编辑/任务组报告、需共识规范 PR、各阶段提案推进和开放讨论，并规定了提案添加、晋级与材料提交的截止时间。

- 🏢 主办与地点：Sony 主办，日本东京；参会信息见 TC39 Reflector #586。
- 🗓️ 会期：2026 年 9 月 29 日–10 月 1 日；前两天 10:00–17:00 JST，最后一天 10:00–16:00 JST。
- ⏳ 总时长：动态计算，预计会议容量约 15:00 小时；容量只是估计，不应阻止添加议题。
- 📌 关键截止：提案晋级资格截止 9 月 19 日 10:00 JST；日程约束截止 9 月 26 日 10:00 JST。
- 📋 议题规则：不晋级提案可随时添加；Stage 0 反馈/Stage 1 须截止前添加；Stage 2/2.7/3/4 及规范变更须截止前添加并附支持材料；Stage 4 须有 spec PR。
- 🔢 排序：提案议题按 Stage 降序、timebox 升序、插入日期排序；⌛️/❄️/🔒/🔁 标记迟到、硬性/一般日程约束、续议。
- 🧾 开场与行政：点名、行为准则、参会者介绍、场地后勤、IPR 政策、沟通工具、GitHub Delegate 团队提醒、速记支持、笔记志愿者、议程通过、上次纪要批准、下次主办方、秘书报告。
- 👤 编辑事务：新增 Eemeli Aro 为 ECMA-402 编辑；项目编辑报告 ECMA262/402/404/Test262；TG3安全、TG4 Source Maps、TG5 实验、CoC 委员会更新。
- 🌐 需共识/Web 兼容 PR：DataView detached buffer、TypedArray RevalidateAtomicAccess、尾调用优化、RangeError vs TypeError 约定、WeakRef KeptAlive 语义、Intl 编号系统/周信息/toLocaleString 等。
- 💬 短时讨论：AI 辅助技术政策更新（15m）；TC39 结构化数据状态更新（30m）。
- 🚀 Stage 3：Iterator Join、Iterator Includes、Iterator Chunking、Dynamic Code Brand Checks 冲 Stage 4；禁止向不可扩展对象加私有字段；ESM Phase Imports 规范 PR；Thenable Curtailment 冲 Stage 3。
- 🧪 Stage 2/2.7：Intl Sequence Units、Intl Unit Protocol、Amount、export defer、JSON.parse Options、Async iterators 更新；Export * 含 default、BigInt from exponential、Private declarations、Composites 等晋级讨论。
- 🌱 Stage 0/1：Pulling in AbortController 争取 Stage 1 或类似阶段。
- 🗣️ 开放讨论：重做 Cover/Supplemental Grammars、议程截止时间、AI 政策、缺少 champion 或 Stage 2.7 reviewer 的提案。
- 📅 日程约束：KG 偏好 15:00 JST 前；Nicolò 偏好 export * 先于 export defer，且强烈偏好 15:00 后；Guy 最后一天 10:00–12:00 可演示；Matthew 第一天后 10:00–12:00 可演示。
- ✅ 结尾：其他事务、感谢主办方、休会。

---

### [Chrome 154 新功能：可根据内容自动调整自身大小的 iframe – Bram.us](https://www.bram.us/2026/09/23/responsive-iframes/)

**原文标题**: [New in Chrome 154: iframes that automatically resize themselves to their content – Bram.us](https://www.bram.us/2026/09/23/responsive-iframes/)

Chrome 154 新增了对响应式 iframe 的支持，允许 `<iframe>` 根据嵌入文档的固有尺寸自动调整大小，适合无缝嵌入第三方评论组件、高度不定的社交媒体内容等。

- 🚀 Chrome 154 引入 responsively-sized iframes，iframe 可随内嵌文档内容自动调整尺寸。
- 🔁 需要双向选择加入：嵌入方为 iframe 设置 `frame-sizing: auto | content-height | content-width`（或逻辑变体）。
- 🏷️ 被嵌入文档需在 `<head>` 中加入 `<meta name="responsive-embedded-sizing" content="allow-origins=*">`。
- 📐 被嵌入文档会在页面加载后上报尺寸；如需更新尺寸，可调用 `window.requestResize()`。
- 🔒 可通过 `allow-origins` 限制哪些来源能接收尺寸信息。
- 🧩 演示中，表单作为 iframe 在切换到下一步时会自动调整高度，不出现滚动条。
- 🌐 浏览器支持：Chrome 154（Chromium/Blink）已支持；Firefox 和 Safari 暂不支持，且暂无跟踪 bug。
- 📚 更多细节见 developer.chrome.com 上的《Responsive iframes in Chrome 154》。
- 📝 文章由 Bramus 于 2026-09-23 发布，标签为 iframe、resize；评论中有日期显示调侃，作者承认是复制粘贴失误。

---

### [](https://blogs.windows.com/msedgedev/2026/09/21/new-in-edge-for-developers-create-better-components-and-make-your-site-agent-ready/)

**原文标题**: [New in Edge for developers – Create better components and make your site agent-ready - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2026/09/21/new-in-edge-for-developers-create-better-components-and-make-your-site-agent-ready/)

本期 Microsoft Edge 开发者更新聚焦于让组件更易构建、更易访问，并让网站为浏览代理场景做好准备；重点介绍 OpaqueRange API、referenceTarget、aria-actions，同时汇总媒体伪类、PWA、性能、安装与 DevTools 等新能力。

- 🧩 OpaqueRange API 让开发者访问 `<textarea>` 和 `<input>` 中的实时文本范围，可配合 `getBoundingClientRect()` 等定位 UI，并支持 CSS Custom Highlight API 创建个性化高亮。
- ♿ `referenceTarget` 属性解决 Shadow DOM 跨根 ARIA 问题，可将 `for`、`aria-labelledby` 等 ID 引用转发到组件内部元素。
- 🗂️ `aria-actions` 属性可把复合组件（如标签页中的关闭按钮）的次要操作暴露给辅助技术。
- 🎬 媒体伪类 `:playing`、`:paused`、`:buffering`、`:muted`、`:stalled` 可根据播放状态样式化音视频元素。
- 🪟 `window-drag` CSS 属性为已安装 PWA 窗口提供标准化拖动方式，配合 Window Controls Overlay API 使用。
- 📱 Edge 151 起 Windows 上使用 Window Controls Overlay API 时，PWA 标题栏默认隐藏，应用外观更可控。
- 🔁 新 JavaScript Iterator 方法：`Iterator.join()` 拼接元素，`Iterator.zip()` 和 `Iterator.zipKeyed()` 聚合多个可迭代对象。
- ⚡ soft-navigation 与 interaction-contentful-paint 性能条目帮助衡量 SPA 软导航性能。
- 🎨 `alpha()` CSS 函数可通过调整透明度创建新颜色。
- 📥 `textStream()` 已可用于 Response、Request 和 Body 对象，便于增量处理文本。
- 📷 `<camera>` 和 `<microphone>` HTML 元素提供浏览器原生按钮，用于切换摄像头/麦克风流并绑定权限请求。
- 🤖 WebMCP 进入测试阶段，可复用前端代码并向浏览代理暴露结构化工具，助力人机协作任务。
- 🔍 JS Self-Profiling 新增样本标记，显示浏览器在样式、布局、绘制、GC 等阶段的活动，填补性能追踪空白。
- 🛠️ Edge 153 的 DevTools 网络工具支持“重新发送”和“编辑并以 fetch 重新发送”，将取代实验性 Network Console。
- 📲 更新版 Web Install API 和 `<install>` 元素支持安装当前或跨源 Web 应用，并可通过清单链接指定目标。
- 🧪 Interop 2027 提案征集即将截止，开发者可提交希望跨浏览器一致支持的 Web 功能。
- 📚 Microsoft Edge 连续第 7 年赞助 Open Web Docs，支持维护 Web 平台文档与数据。
- 📋 Open UI 社区推进原生菜单元素，`<menubar>` 已可由 Google 实现测试，减少自建菜单的无障碍与键盘导航负担。
- 💬 Edge Web 平台团队欢迎反馈，以改进 Edge、Chromium 和整个 Web 平台。

---

### [pnpm 12.6 | pnpm](https://pnpm.io/blog/releases/12.6)

**原文标题**: [pnpm 12.6 | pnpm](https://pnpm.io/blog/releases/12.6)

pnpm 12.6 于 2026 年 9 月 22 日发布，重点新增自动依赖去重、可迁移 node_modules、--save-types、package.yaml 清单编辑、catalogs 的 file:/link: 协议，并带来大量安装、解析、脚本、配置、Windows 与安全修复。

- 🚀 自动去重：在 pnpm-workspace.yaml 中设置 autoDedupe: true，安装时会为整个工作区选择满足所有版本范围的兼容版本；冻结安装不会修改 lockfile。
- 📦 可迁移 node_modules：macOS 和 Linux 上移动或复制项目后，pnpm install、pnpm run、pnpm exec 可复用 node_modules 与 bin shims，并记录新位置。
- 🧩 --save-types：pnpm add express --save-types 会把 @types/express 保存到 devDependencies；已自带类型的包会跳过，可用 saveTypes: true 默认开启。
- 📝 package.yaml 清单：pnpm add、update、remove、pkg、link、set-script、version 均可编辑 package.yaml，并保留注释和键顺序。
- 🔗 catalogs 支持 file:/link:：目录条目可使用相对路径或裸路径，路径相对于 pnpm-workspace.yaml 所在目录。
- 📋 pnpm tasks status：列出每个并发组中运行和等待的任务；等待任务按优先级降序占用空闲槽，到达顺序仅用于打破平局。
- 🍏 macOS Time Machine 排除：macosBackup.excludeModulesDir 和 excludeStoreDir 可将模块、虚拟存储、包存储目录排除出 Time Machine 备份。
- ⚙️ 小改进：pnpm add --tilde 等价于 --save-prefix=~；progress 与 --no-progress 可关闭进度；cache prune 清理旧元数据缓存并支持 --dry-run。
- 🔐 安全修复：POSIX bin shims 在 Cygwin、MSYS2、WSL2 上从系统默认路径获取 cygpath 和 wslpath；弃用警告不再包含通知正文；忽略 .npmrc 环境变量凭据时会警告。
- 🛠️ 安装修复：--frozen-lockfile 可处理已跳过的可选依赖，且不再安装已移除项目的依赖；pnpm ci 在声明 clean 脚本时清空 node_modules；--force 会重新导入并清理过时链接。
- 🔍 解析与链接：优先解析到未弃用的最新匹配版本；pnpm add <pkg> 会使用 catalog；overrides 裸路径相对工作区；peers check 支持命名注册表；outdated/update 保留注册表前缀。
- ⚡ 性能：通过并发检查 overrides，加速大量收敛覆盖项目中的 pnpm dedupe 和 pnpm install。
- 🖥️ Windows：支持从长全局虚拟存储路径运行构建脚本；共享全局虚拟存储不再报 Access is denied；Git Bash、MSYS2、Cygwin 启动更可靠；pipeline --watch 解析短路径。
- 🧹 其他修复：pnpm remove 运行卸载脚本；remove -r 先校验依赖；update --peer 更新 peerDependencies；publish 允许 CI 中 detached HEAD；store prune 清理未引用文件与 dlx 缓存；sbom 验证 SPDX 标识符。

---

### [Turborepo 2.11 | Turborepo](https://turborepo.dev/blog/2-11)

**原文标题**: [Turborepo 2.11 | Turborepo](https://turborepo.dev/blog/2-11)

Turborepo 2.11 于 2026 年 9 月 18 日发布，重点带来 Rust、Python、Go 的实验性原生支持、统一多语言任务图、启动速度大幅提升、现代包管理器兼容以及更可控的生产部署裁剪，并成为首个零已知 bug 的版本。

- 🧩 原生支持 Rust、Python、Go（实验性）：可从 Cargo、uv、go.work 工作区发现包与依赖，并纳入同一任务图。
- 🔗 支持跨工具链依赖：可在 `turbo.json` 中让 Python 测试等待 Rust 包构建完成，多语言任务并行且尊重依赖。
- ⚡ Time to First Task 最高比 Turborepo 2.9 快 4 倍；叠加 2.9 的提升后，最大基准仓库比 2.9 之前快 20 倍以上。
- 📦 支持 `devEngines.packageManager`：遵循现代 Node.js 约定声明包管理器，未来主版本将不再支持顶层 `packageManager`。
- 🆕 新增 nub 和 aube 包管理器支持：二者聚焦安装安全与速度，并复用现有 npm、pnpm、Yarn 或 Bun 锁文件。
- ✂️ 生产裁剪增强：`turbo prune --production` 可排除仅通过 `devDependencies` 可达的工作区包，优化生产镜像。
- 🐛 这是 Turborepo 首个零已知 bug 的版本。
- ⬆️ 可通过 `@turbo/codemod migrate` 升级，或用 `create-turbo@latest` 新建仓库，支持 pnpm、Yarn、npm、Bun、nub、aube。
- 📊 本次发布包含 91 项功能、109 项性能改进、195 项修复、40 项文档更新和 28 个示例。
- 🙌 感谢核心团队 Anthony、Tom 以及所有社区贡献者。

---

### [Node.js — 博客](https://nodejs.org/en/blog)

**原文标题**: [Node.js — Blog](https://nodejs.org/en/blog)

该页面是 Node.js 官方博客的最新动态索引，汇总版本发布、公告、安全漏洞、迁移指南与活动，并展示近期按时间排序的发布文章。

- 🗂️ 博客分类包括：全部、公告、版本发布、安全漏洞、迁移指南、活动。
- 🚀 最新 LTS 版本：Node.js 22.23.3 (LTS)，发布于 2026 年 9 月 23 日。
- ⚡ 最新 Current 版本：Node.js 26.10.0 (Current)，发布于 2026 年 9 月 22 日。
- 🔧 其他近期发布包括：26.9.0、26.8.2、24.21.0 (LTS)、26.8.1，主要集中在 2026 年 8 月至 9 月。
- ✍️ 当前列出的文章作者均为 Antoine du Hamel（ADH）。
- 📄 页面采用分页展示，当前为最新条目，共 177 页，并提供上一页与下一页导航。

---

### [发布 v30.1.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v30.1.0)

**原文标题**: [Release v30.1.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v30.1.0)

jsdom v30.1.0 发布，聚焦性能优化与正确性修复，并新增命名访问、QuotaExceededError、宽松 DOM 命名规则；大量改动来自 @scttcper 的 AI 辅助贡献。  
- 🚀 发布：v30.1.0 由 domenic 发布，含 23 个提交，贡献者包括 scttcper、soroushm 等 14 人。  
- 🆕 新特性：支持 `document.myForm` 命名访问；新增 `QuotaExceededError`；采用宽松 DOM 命名规则创建元素、属性和文档类型。  
- ⚡ 性能：优化 DOM 构建/变更、Range、实时集合、`getComputedStyle()`、样式、CSS 序列化、事件分发、表单查找、`<select>`/radio 更新。  
- 🧠 内存：降低 DOM 节点、属性、事件监听器、MutationObserver 的内存占用，修复相关泄漏。  
- 🎯 选择器：修复 `querySelectorAll()`/`querySelector()`、CSS 属性选择器大小写、shadow tree 中 `:focus` 匹配。  
- 🧩 DOM/脚本：修复插入替换、`replaceChildren()`、`replaceWith()`、脚本执行顺序、自定义元素回调、iframe 加载、MutationObserver 通知。  
- 🛑 生命周期：`window.close()` 后保留文档引用，销毁文档不再运行脚本/加载资源/定时器/动画帧/事件/导航。  
- 🌐 网络：修复重定向取消、`requestInterceptor()`、`XMLHttpRequest` 复用、`JSDOM.fromURL()` 挂起、缓存加载误判中止。  
- 🎨 CSS：修复样式表顺序、`@import`/`@media`、border 宽度、`font-weight`、CSS 数学函数、`min()`/`max()`、shorthand 解析。  
- 📝 文本/范围：修复 CDATA 的 Range/Selection 操作、`text.normalize()`、CDATA/处理指令克隆导入与序列化。  
- 🧷 表单/焦点：修复 radio 分组、select 选项移动、`input.indeterminate` 克隆、焦点移除状态、`input.list` 分离树。  
- 🧭 窗口/属性：修复 window 命名属性、空/命名空间 `id`/`name`、DOMParser 文档元素错误暴露与内存保留。  
- 🔐 事件/存储：修复 storage 事件、非节点事件目标、`window.event`、passive 监听、`volumechange`/`ratechange` 异步触发。  
- 🧪 其他：涵盖 XPath、NodeIterator、fileReader、时间输入、textarea、readyState、translate、XML 代理对、namespaceURI、`<base>`、SVG、blobEvent、CSS 对象形状。  
- 💬 社区：发布说明获 8 个 rocket 反应，并感谢所有人类与 AI 辅助贡献者。

---

### [宣布 Rstest 0.12 - Rstest](https://rstest.rs/blog/announcing-0-12)

**原文标题**: [Announcing Rstest 0.12 - Rstest](https://rstest.rs/blog/announcing-0-12)

Rstest 0.12 已于 2026 年 9 月 14 日发布，新增 E2E 与 Module Federation 测试支持，通过 VM 池和环境预打包显著加速大型测试套件，并推出全新 JavaScript API，同时带来多项开发体验与浏览器模式改进。

- 🚀 **发布重点**：Rstest 0.12 支持 E2E、Module Federation 测试，优化大型套件速度，并正式推出新 JavaScript API。
- 🌐 **E2E 测试**：通过 `@rstest/playwright` 集成 Playwright，可让单元、组件与 E2E 测试共享同一套配置、命令和报告器。
- 🧪 **E2E 使用方式**：可从 `@rstest/playwright` 导入 `test` 与 `expect`，测试真实页面、本地开发服务器、预览服务器或已部署 URL。
- 🔧 **Playwright 配置**：使用 `definePlaywrightConfig` 继承 Playwright 默认值，并可自定义视口、重试时 trace 等选项。
- 🔗 **Module Federation 测试**：通过 `@module-federation/rstest` 插件，在 Node、jsdom、happy-dom 和浏览器模式中测试联邦远程模块与共享依赖。
- 🧩 **联邦测试价值**：测试代码像消费方应用一样导入远程模块，让消费方与生产方之间的集成问题更早暴露在单元测试中。
- ⚡ **新增 VM 池**：新增 `vmThreads` 与 `vmForks`，复用 worker 并为每个测试文件创建独立 `vm.Context`，降低启动与模块加载成本。
- 📊 **性能基准**：在 2400 个文件、20000 个测试的 jsdom 项目中，`vmThreads` 约 33.22 秒，比 `forks` 的 315.17 秒快约 9.5 倍。
- 🛠️ **池选择**：`forks` 适合原生插件等场景；`threads` 适合轻量文件；`vmThreads` 最快但有跨 realm 限制；`vmForks` 兼具 VM 速度与进程能力。
- 🧠 **内存限制**：可用 `pool.memoryLimit` 限制单个 worker 内存，超限后 Rstest 会自动替换 worker。
- 📦 **环境预打包**：0.12 默认启用 `testEnvironment.prebundle: 'auto'`，将 jsdom / happy-dom 预构建为共享 ESM bundle，减少重复加载。
- ⏱️ **预打包性能**：jsdom 30.0.1 从 16.99 秒降至 10.57 秒，约 -37.8%；happy-dom 20.11.1 从 6.35 秒降至 2.98 秒，约 -53.0%。
- 🧩 **新 JavaScript API**：提供 `createRstest`，便于集成到工具、IDE 和其他 Node.js 程序，支持 `run`、`watch`、`listTests`、`mergeReports`。
- 🧰 **其他改进**：支持文件/worker 级 fixtures、`--onlyFailures`、Rspack 原生 watcher、超时 `context.signal`、任务元数据、`expect.poll` 默认值等。
- 🔌 **集成增强**：Rsbuild 插件可读取和修改 Rstest 配置，多项目可单独设置 `silent`，VS Code 扩展支持终端运行与调试设置。
- 📈 **报告与浏览器模式**：`--merge-reports` 支持完整 reporter 重放；浏览器模式支持 V8 覆盖、`rs.mock`、`includeSource`、`globalSetup`、Module Federation 和 watch 快捷键。
- ⬆️ **升级提醒**：将 `@rstest/*` 升级到 0.12；注意 JavaScript API 和部分 reporter 类型存在破坏性变更，使用 `@rstest/core/api` 或自定义 reporter 的项目需先检查。

---

### [](https://github.com/trpc/trpc/releases/tag/v11.19.0)

**原文标题**: [Release v11.19.0 · trpc/trpc · GitHub](https://github.com/trpc/trpc/releases/tag/v11.19.0)

tRPC 发布 v11.19.0，由 Nick-Lucas 于 9 月 16 日发布，是当前最新版本；本次更新集中在客户端/服务端修复、文档改进、依赖升级和安全补丁，并迎来多位新贡献者。

- 🚀 tRPC v11.19.0 已发布，包含 1 个提交，完整变更范围为 v11.18.0...v11.19.0。
- 🔧 修复客户端流处理：httpBatchStreamLink 取消订阅时中止 JSONL 流，WebSocket link 接入操作 AbortSignal，httpLink/httpBatchLink 取消订阅时中止请求。
- 🛡️ 修复服务端逻辑：中间件工厂声明可移植性、链式调用已有 dispose 时保留 this、assertIsRequestId 布尔判断、订阅任务拒绝时删除过期 clientSubscriptions。
- 🧭 修复 getProcedureAtPath 中惰性路由键需按路径边界匹配。
- 🧪 修复升级流程：每次 fixture 渲染时清空查询缓存；TanStack React Query 的 subscriptionOptions(skipToken).enabled 不再错误返回 true。
- 📚 文档修复：星标历史图表、llms.txt 中 19 个失效链接，并补充 subscriptions 参考项目的 observable 弃用说明。
- 🧩 生态与集成：新增 vscode-toolkit、Sury、Authier 到 awesome tRPC 或验证器集成列表。
- 🧱 CI/构建修复：解决示例 Playwright e2e ffmpeg 失败，批准 esbuild。
- ⬆️ 大量依赖升级：Node 24.21.0、@types/node v24、pnpm v12、tsdown 0.23.0、TypeScript v7、ESLint v10、Prettier 3.9.6、Vitest v5、Turbo 2.10.12、Lerna v10、Docusaurus 3.10.2、@hey-api/openapi-ts 0.99.0。
- 🔐 修补 packages/*、www 和 examples 中的安全公告。
- 🧬 OpenAPI 修复：从生成的 schema 中移除函数值属性。
- 👥 新增多位首次贡献者，仓库目前约 40.7k stars、1.7k forks、145 issues、57 PRs，发布资源 2 个。

---

### [](https://eslint.org/blog/2026/09/eslint-v10.11.0-released/)

**原文标题**: [ESLint v10.11.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/09/eslint-v10.11.0-released/)

ESLint v10.11.0 于 2026 年 9 月 18 日发布，这是一个小版本升级，带来了性能优化、新功能、错误修复以及文档和杂项更新。

- 🚀 性能提升：启动加载不再预先初始化 JSON Schema 验证器，减少约 45 个模块，包加载时间降低 20–25%
- ⚡ 规则执行优化：常见节点选择器使用快速路径，规则访问器直接调用，减少遍历开销
- 🧩 问题报告开销降低：占位符按需填充、自动修复验证不再序列化 JSON、共享修复器对象、跳过无指令文件的处理
- 🎨 默认格式化器：stylish 避免对不含控制字符的字符串进行剥离，不再对每条消息运行正则，提升大量问题打印速度
- ✨ 新功能：object-shorthand 支持带引号属性处理 ignoreConstructors；no-unsafe-finally 报告不安全的带标签 continue；new-cap 仅豁免引用全局的内置对象
- 🐛 错误修复：prefer-object-spread 忽略 __proto__ 属性；object-shorthand 不再报告 __proto__ 属性；TimePass.parse 在类型和文档中变为可选
- 📚 文档更新：说明 --cache 可能对跨文件规则提供过期结果；澄清 preserve-caught-error 已知限制；更新 README
- 🔧 杂项工作：在关键区域实现快速路径；更新 Node.js 26.9.0 兼容性测试；升级 GitHub Actions、pnpm 和 Stylelint；添加 AGENTS.md 披露要求；增加类型集成测试
- 👥 贡献者：Francesco Trotta（ESLint 技术指导委员会）等

---

