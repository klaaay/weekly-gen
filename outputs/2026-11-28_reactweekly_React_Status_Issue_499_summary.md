# [Issue #499: Ricky Hanlon leaves Meta (but not React) — React Status](https://react.statuscode.com/issues/499)

### [@ricky.fm 在 Bluesky 上](https://bsky.app/profile/ricky.fm/post/3n35lo3frik2z)

React 核心团队成员 Ricky 宣布从 Meta/Facebook 离职，结束 8 年任期；他回顾了 React 周下载量从 400 万增长到 2.5 亿的历程，并指出多数 React Core 团队成员已离开 Meta。他下周将加入新公司，继续从事 React 相关工作。

- 🏢 **结束 Meta 任期**：Ricky 表示今天是他在 Facebook 的最后一天，已在 Meta 工作 8 年，主要投入 React 生态。
- 📈 **下载量增长**：他任期内 React 周下载量从 400 万增长到 2.5 亿，这是其回顾的核心成果数据。
- 🔄 **核心团队流失**：Ricky 提到 React Core 团队的大部分成员已离开 Meta，这也是他决定离开的背景之一。
- 🚀 **新公司继续 React**：他将于下周入职新公司，并继续参与 React 的开发工作，具体公司未在原文披露。

### [React 基金会：由 Linux 基金会托管，React 的新家 – React](https://react.dev/blog/2026/02/24/the-react-foundation)

React Foundation 于 2026 年 2 月 24 日正式成立，由 Linux Foundation 托管，这距离去年 10 月宣布筹组意向已有数月。React、React Native 以及 JSX 等配套项目不再由 Meta 所有，转由这个独立基金会持有；同时公布了八家白金创始成员，并设立临时领导委员会来设计技术治理结构。基金会董事会负责治理事务，React 的技术方向仍由维护者与贡献者决定。仓库、网站等基础设施的移交和生态支持计划将在未来数月推进。

- 🏢 **正式成立**：React Foundation 正式启动，由 Linux Foundation 托管；React、React Native 及 JSX 等配套项目的所有权从 Meta 转移至该独立基金会，具体信息见 Linux Foundation 新闻稿。
- 🎯 **八家创始成员**：八家白金创始成员为 Amazon、Callstack、Expo、Huawei、Meta、Microsoft、Software Mansion 和 Vercel，其中 Huawei 是在 10 月公布之后新加入的；基金会由各成员代表组成的董事会治理，Seth Webster 担任执行董事。
- 🧭 **技术治理独立**：React 的技术治理始终独立于基金会董事会，技术方向仍由贡献者和维护者决定；目前已成立临时领导委员会来确定治理结构，并将在未来数月公布进展。
- 🔄 **过渡期待办**：过渡尚未完成，后续工作包括敲定 React 技术治理结构、把代码仓库、网站及其他基础设施移交给 React Foundation、探索支持 React 生态的项目，以及启动下一届 React Conf 的筹备。

### [错误](https://zpao.com/posts/14-years-at-meta/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='zpao.com', port=443): Max retries exceeded with url: /posts/14-years-at-meta/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

### [Trigger.dev | 面向持久化 AI 智能体的开源平台](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=react-weekly&utm_content=homepage)

Trigger.dev 是一个 Apache 2.0 开源、可自托管的 TypeScript 平台，用于构建可持久运行的 AI agents 与工作流。它把长时任务、自动重试、队列、AI 可观测性和弹性伸缩整合到同一套基础设施中，使任务在刷新、重新部署或崩溃后仍能继续运行；同时提供 durable chat agents、工具调用、human-in-the-loop、实时流式输出和运行状态展示，支持无超时、按实际执行计费、无需自管服务器的部署方式。

- 🚀 **开源平台**：Trigger.dev 采用 Apache 2.0 许可证，可查看源码、贡献和自托管；官网称已有 16.8k+ GitHub stars、5.1k+ Discord 成员，并提供 SOC 2 Type II、HIPAA BAA 和 GDPR 合规信息。
- 🧩 **持久执行**：任务可在刷新、重新部署和崩溃后继续运行，支持长时间异步 AI 任务、无超时、自动重试、队列、并发控制、弹性伸缩，按代码实际执行付费且无需管理服务器。
- 🧠 **AI 聊天 Agent**：示例 `supportAgent` 使用 `chat.agent` 声明 `searchDocs`、`refundOrder` 等工具，并在 `run()` 中通过 `chat.toStreamTextOptions({ tools })` 接入系统提示、工具审批、压缩、回合中 steering 和遥测；示例模型为 `claude-sonnet-4-5`，并设置 `stopWhen: stepCountIs(15)`。
- 🛡️ **人工审批**：工具可设置 `needsApproval: true`，例如退款工具在调用前暂停等待人工批准，运行保持存活，从而支持 human-in-the-loop。
- ⚡ **实时流与状态**：Realtime API 可把任意提供商的 LLM 流转发到前端，无需 API routes；Realtime 还能展示运行状态（进行中、完成、失败）和元数据，便于前端实时更新。
- 🎯 **工作流模式**：文档列出自主 agent、提示链、路由、并行化、orchestrator、evaluator-optimizer 六种 AI 工作流模式，分别用于开放式任务、多阶段处理、按内容分派模型、并发分析、多 agent 协调和迭代优化输出。
- 🛠️ **构建扩展**：构建阶段可执行 Python 脚本并通过 `requirements.txt` 自动装包，生成 Prisma Client、运行数据库迁移，使用 Puppeteer、FFmpeg、apt-get 安装系统包、添加额外包、生成音频波形，以及接入自定义 esbuild 插件和构建扩展。
- 🔄 **重试策略**：任务级 `retry` 可配置 `maxAttempts`、`minTimeoutInMs`、`maxTimeoutInMs`、`factor`、`randomize`，示例为 3 次、1000ms 到 5000ms、指数退避 2 并随机化；还提供 `catchError()`、`retry.onThrow()`、`retry.fetch()` 和 `trigger.config` 默认重试。
- 📊 **可观测性**：提供 LLM 可观测性、日志与追踪、tags、运行元数据、高级筛选、批量操作、查询和仪表盘；失败可通过 email、Slack 或 webhooks 告警；每次部署是原子版本，已启动任务不受代码变更影响。
- 🔗 **基础设施集成**：支持 MCP Server、durable cron、waits、durable webhooks、Input Streams、preview/dev branches、多区域 workers、静态 IP、AWS PrivateLink、多环境、Vercel 和 GitHub 集成及版本偏移保护。
- 📝 **近期更新**：Changelog 列出可跨环境搜索所有运行日志并用 Ask Trigger 检查、GitHub Actions trusted publishing、API key 自定义权限与保存预设、以及 workload identity (OIDC) 让任务向 Anthropic 等服务证明身份而无需存储 API key。

### [🗺️ Query v6 路线图 · TanStack/query · 讨论 #12669 · GitHub](https://github.com/TanStack/query/discussions/12669)

TanStack Query 已启动 v6 开发，但维护者强调主版本主要用于移除和破坏而非新增功能，v6 不打算大规模重写公共 API，重点放在内部整理、工具链与支持范围更新；路线图逐项跟踪已实现、计划和讨论中事项，开发在 `query-v6` 分支进行，发布时间不做承诺。

- 📦 **构建改为纯 ESM**：v6 将放弃 CJS 和早期为 webpack4 等准备的 legacy 构建，以简化构建并推动生态转向 ESM；该项状态为已实现。
- 🚀 **React 最低版本升至 v19**：React 适配器最低要求提升到 v19，以便在 suspense 集成中内部使用 `use()`，替代已弃用的 `throw promise`；已实现。
- ⚡ **默认调度器改为 microtask**：默认调度器从 `setTimeout(0)` 切换为 microtask，以获得略好的批处理效果，改善 await 失效后 setState 有时用旧 query data 渲染新状态的问题；已实现。
- 🐛 **移除 v5 废弃 API**：清理 v5 标记为 deprecated 的 API，包括 query-core 的 `context.direction`、`isInitialLoading`、`queryClient.fetch(Infinite)Query`、`queryClient.prefetch(Infinite)Query`、`queryClient.ensure(Infinite)QueryData`、`queryObserver.getOptimisticResult`，solid-query 的 `suspense` 选项，sync-storage-persister、vue-query 的 Vue 2 支持，以及 devtools 的 `styleNonce`；已实现。
- ✅ **查询函数改为必填**：`useQuery` 等框架适配器将要求传入查询函数，避免依赖隐式全局默认；为保留 `defaultQueryFn` 用法，导出 `defaultQueryFn` 供显式传入，`queryOptions` 原本已要求；已实现。
- 🎯 **指数退避加入 jitter**：默认指数退避加入 jitter，以缓解 thundering herd 问题；该行为变化只在 v6 发布，已实现。
- 🔍 **讨论用 skipToken 替代 enabled**：正在讨论用 `skipToken` 替代 `enabled`，但永久禁用后通过 `refetch()` 按需取数的场景无法用 `skipToken` 复现；维护者希望先确认实际使用情况，状态为讨论中需反馈。
- ⚙️ **调整 gcTime 合并规则**：计划把 `gcTime` 的合并规则从最高值获胜改为最后设置获胜，与其他选项的确定性覆盖保持一致；仍在 planned。讨论中还提出按最晚 GC 截止时间作为 tie-breaker 的替代方案，并请协作者提交草案 PR。
- 🌐 **讨论服务端 gcTime 行为**：服务端默认 `gcTime` 为 `Infinity`，但若在 `useQuery` 显式传入有限值仍会在服务端设置 GC 定时器，可能钉住整个 SSR async context；此问题仍在讨论，维护者倾向通过 `QueryClient` 的 `Symbol.dispose` 调用 `clear()` 清理定时器，并配合 `using` 使用。
- 🔑 **全局 hashFn 与 equalityFn**：v6 将 `queryKeyHashFn` 替换为全局 `hashFn` 并移出 `queryOptions`，同时新增 `equalityFn` 扩展 `replaceEqualDeep` 的结构共享到非 JSON 类型；已实现。讨论指出全局 hash 会失去按查询覆盖能力，维护者建议用静态前缀配合全局 `hashFn`，并指出 exact lookup 与多 hash 存在固有缺陷。
- 🧩 **queryOptions 移入 query-core**：计划将 `queryOptions` 移到 `query-core`，各框架适配器只重导出，减少重复实现并处理类型层问题；React 等适配器仍可能用自身实现覆盖以保留框架特有选项，状态为 planned。
- 🧪 **streamedQuery 转正**：`experimental_streamedQuery` 将提升为稳定 API，结束实验状态；已实现。
- 🌐 **提高浏览器支持门槛**：v6 提高浏览器目标：Chrome、Edge >=119，Firefox >=121，Safari/iOS >=17.4，Opera >=105，以便使用 `promise.withResolvers` 等现代 API；已实现。
- ⚠️ **HydrationBoundary 清理防御检查**：已实现移除 `HydrationBoundary` 中由类型保护的防御性检查，作为早期无类型时期的遗留清理；讨论指出 pages router 使用 `pageProps.dehydratedState` 时用户可能需要额外守卫，维护者表示可以轻松回退。
- 💬 **协作与时间线政策**：维护者不承诺发布时间，鼓励试用 beta/pre-release 并给反馈，但明确不接受未经沟通的全自动代理 PR；贡献前应先在 TanStack Discord 询问维护者，并遵守 contributing 与 AI policy。

### [@tkdodo.eu 在 Bluesky 上](https://bsky.app/profile/tkdodo.eu/post/3n2vgpfgayk2g)

TanStack Query 已开始开发 v6，目前尚未发布；团队预告会引入破坏性变更但数量有限，意味着未来升级需要关注迁移影响，相关讨论已在 GitHub 开放。

- 🚀 **启动 v6 开发**：TanStack Query 已开始开发 v6，当前仍处于早期阶段，尚未发布。
- ⚠️ **有限破坏性变更**：团队表示 v6 会带来破坏性变更，但不会太多，后续升级需关注迁移影响。
- 💬 **开放讨论**：团队已在 GitHub 开放相关讨论，供社区跟进 v6 的开发进展。

### [你的工具正在对你隐瞒 npm 审计结果——zachleat.com](https://www.zachleat.com/web/npm-audit-report/)

文章指出，npm audit 的结果可能被工具的实现方式掩盖：Next.js 将自身依赖打包进 node_modules/next/dist/compiled，使标准审计看不到其中的漏洞，而全新 Gatsby 项目会显示大量漏洞；多个 create-* CLI 以及 pnpm、yarn 也会隐藏或省略安装后的审计输出。作者因此推出约每日更新的 Prototype Pollution Report，用于横向比较不同生态的漏洞状况，并强调透明度和可见性才是安全审计的核心。

- 🔍 **审计结果误导**：文章对比同一天生成的两个全新项目：create-gatsby 项目的 npm audit 报告 78 个漏洞（7 low、23 moderate、46 high、2 critical），create-next-app 项目显示 0 个漏洞，但 0 并不代表更安全。
- 📦 **Next.js 依赖打包**：Next.js（写作时 v16.4.6）把自身依赖放在 node_modules/next/dist/compiled，绕过 node_modules 常规审计；其中 139 个唯一依赖被审计出 11 low、2 moderate、19 high、3 critical，这些漏洞不会出现在标准 npm audit 报告中。
- ⚠️ **Gatsby 对比**：Gatsby 已不再维护，但其全新 create-gatsby 项目仍显示 2 个 critical 漏洞；Next.js 隐藏的 critical 漏洞反而更多，说明两者安全足迹相近但可见性不同。
- 🧩 **Vite 打包差异**：Vite 也在 node_modules/vite/dist 中打包依赖，但属于 bundler 生成输出；文章认为其作为本地开发工具较易解释，且 Vite 保持打包依赖更新的记录很好，但完全将依赖排除在审计之外仍像过度修正。
- 🛠️ **CLI 隐藏审计输出**：create-gatsby 使用 npm install --no-audit；create-astro、TanStack CLI、create-preact 不显示控制台输出；create-nuxt 与 ng new（Angular）仅在安装失败时输出；sv create（Svelte）短暂显示后清空日志。
- 💻 **包管理器差异**：npm 在 npm install 后显示审计报告，pnpm 和 yarn 不显示；作者认为这会降低安装步骤的透明度。
- 📊 **生态对比报告**：Prototype Pollution Report 约每日更新，将上述差异归一化后比较不同框架生态；Ecosystem Scoreboard 统计各项目发布的全部非弃用包，并主张维护者应弃用不再维护的包，Core-only Scoreboard 只统计核心包，文末列出带审计计数的完整包列表。

### [原型污染报告](https://ppr.zachleat.dev/)

总结失败：模型未返回符合格式的摘要。

### [React 表单：不止于 onSubmit](https://www.gmoniava.com/blog/react-forms-beyond-onsubmit)

文章以延迟 1 秒、对 test@example.com 返回已订阅错误的模拟 subscribe API 为例，对比 React 表单提交的三种方式：传统 onSubmit、React 19 的 action prop，以及 onSubmit 配合 useTransition；重点说明 action 会自动阻止浏览器导航、接收 FormData、自动重置非受控字段并在 Transition 中运行，同时指出现行 React 中 await 后的状态更新需再用 startTransition 包裹，且只有向 action 传入 Server Function 才能在兼容框架中实现 JavaScript 加载前的渐进增强。

- 🚀 **React 19 action**：React 19 支持向 form 的 action 传入函数来处理提交；文章用同一个模拟 subscribe API 对比三种写法，该 API 延迟 1 秒，test@example.com 返回已订阅错误，其他邮箱返回成功。
- 🧩 **onSubmit 基线**：传统 onSubmit 需调用 event.preventDefault()、从 event.currentTarget 构造 FormData，并自行维护 isSubmitting 和错误/成功状态；示例仅在订阅成功后调用 form.reset()，失败时保留邮箱。
- 🔄 **action 自动处理**：action 无需 preventDefault，直接接收 FormData；React 在 action 未抛异常结束时自动重置非受控字段，因此即使订阅失败但错误被处理而未抛出，邮箱也会被清空；若需保留值，可用 state 配合 defaultValue 或参考 React 的重置控制文档。
- ⚙️ **Transition 运行**：传给 action 的函数由 React 在 Transition 中运行，支持 useOptimistic 和错误边界；首个 await 前的同步 setState 可能被延迟，loading 标志未必显示，前一条消息也可能继续可见。
- 🛠️ **useFormStatus 子组件**：action 示例把提交按钮与消息拆成 SubmitButton 和 FormMessages，在 form 内部的子组件调用 useFormStatus 读取 pending，用于禁用按钮、显示 Subscribing... 并隐藏旧消息；在 NewsletterForm 自身调用无法追踪其返回的 form。
- ⚠️ **await 后更新限制**：当前 React 中，await 之后的状态更新不会自动标记为 Transition，而是紧急更新，可能在 Transition 仍 pending 时渲染；需用额外的 startTransition 包裹 setError 和 setSuccess，文章示例对成功和错误更新均这样处理。
- ⚡ **useTransition 写法**：也可在 onSubmit 中手动调用 startTransition，并用 useTransition 返回的 isPending 控制按钮；示例在 startTransition 前清空旧错误/成功消息以立即隐藏，成功后 form.reset()，且 await 后更新仍需再包 startTransition。
- 🌐 **渐进增强差异**：onSubmit 与 onSubmit 加 useTransition 的处理器都在客户端运行，需 JavaScript 加载并完成 hydration；把 Server Function 传给 action 时，在兼容框架中可在 JavaScript 加载前支持提交，这是 onSubmit 加 useTransition 无法提供的。
- 📝 **受控输入补充**：示例均使用非受控输入；三种方式也适用于受控输入，此时用 value 和 onChange 管理邮箱，从 state 读取值而非 FormData，并用 setEmail 清空；action 的自动重置只适用于非受控字段，pending 与 Transition 行为不变。

### [你能放心地从手机发布到生产环境吗？](https://expo.dev/blog/ship-to-production-from-your-phone)

总结失败：模型未返回符合格式的摘要。

### [Base44 应用如何借助 TanStack Start 实现全栈](https://base44.com/blog/base44-apps-full-stack)

Base44 将新应用从 Vite 单页应用加独立后端函数的架构，切换为基于 TanStack Start 的全栈应用：页面与服务端代码同库共享，并内建服务端渲染。为支撑这一核心替换，团队在每个开发沙箱中运行新服务器、改造 Cloudflare Workers for Platforms 托管与代理链路、重训 builder agent，并通过功能开关和 AI 监控灰度上线；开发服务器启动失败率从修复前约 4% 降至 0.1% 以下。

- 🚀 **全栈切换**：新 Base44 应用现在从第一天就是 TanStack Start 全栈应用，不再采用 Vite 单页应用加独立后端函数；团队放弃了先按需把单页应用原地转换为全栈的中间路径，现有应用迁移另立项目，单页应用仍将长期支持。
- 🧩 **选型约束**：TanStack Start 满足基于 Vite、使用 React、同时覆盖登录型单页应用和需要 SEO 的公开 SSR 网站等硬性要求，并提供 `server functions` 和 `server routes`；团队此前已通过 React Query 使用 TanStack。
- ⚙️ **沙箱修复**：开发沙箱改用 TanStack Start 的 dev server 后，原探活逻辑通过请求应用首页判断存活，会把应用异常误判为 dev server 崩溃，而实际多数运行正常；改为检查 Vite 自身 `health ping` 后，只判断 Web 服务器是否响应。
- 🌐 **托管改造**：新 TanStack Start 应用托管在 Cloudflare Workers for Platforms，与单页应用的后端函数同平台，因此托管侧需同时支持两套模式；由于全栈应用的服务端代码也会访问后端，API 调用来源变为 Cloudflare，需经代理层校验调用者身份和权限。
- 🧠 **Agent 重训**：builder agent 需学习服务端代码放在哪里、改用 `server functions` 而非 `backend functions`，同时继续生成单页应用；相关改动经过 `evals` 验证，确保 TanStack 应用不回归并与单页应用对齐后再扩大范围。
- 🧪 **水合防护**：服务端渲染 HTML 与客户端渲染结果不一致会触发 hydration 失败，并进入自动修复轮次，消耗 builder 时间和 credits；Agent 指令因此覆盖随机值、日期等可能造成差异的代码来源。
- 🛡️ **安全约束**：团队增加简化鉴权的中间件并教 Agent 使用，同时要求应用数据配置行级和字段级安全规则；随后检查 Agent 生成的应用是否真的不会泄漏数据。
- 🔄 **灰度监控**：新代码直接进入生产并置于 `feature flag` 后，避免长期分支漂移；AI agent 联合监控技术和业务指标，异常时可自行关闭开关，数据良好时经批准扩大曝光。一次依赖更新破坏 SSR 后，agent 自动关闭开关，修复在数小时内上线。
- 📊 **效果与成本**：TanStack 新应用的 dev server 启动失败率从健康检查修复前约 4% 降至 0.1% 以下，低于单页应用约 0.5% 的水平；但 TanStack 应用单次 `builder turn` 成本略高，团队仍在优化。
- 🧭 **推进策略**：最难的是在平台高速演进中做核心替换：其他工程师的新功能需要全栈支持，而每项新功能又要兼容两套架构；团队借助 AI agent 跟踪代码库并为新功能补支持，以工作流和循环推进，而非只盯单个任务。
- 🔮 **后续方向**：Base44 计划让 TanStack 应用构建更便宜、更快，增加更多脚手架以帮助 builder agent 更快构建复杂应用，并提升最终应用的使用性能。

### [构建坚不可摧的 React 组件 - Shu Ding](https://shud.in/thoughts/build-bulletproof-react-components)

文章以主题组件为例，讨论 React 组件如何从只跑通 happy path 变为能在 SSR、hydration、多实例、并发渲染、异步 children、Portal、View Transition、Activity、服务端数据泄漏和未来 React 变化下存活，强调健壮性要在未知使用环境和他人的使用方式中成立。

- 🛡️ **SSR 安全**：在 useState 初始化时读取 localStorage 会在 Next.js、Remix 等 SSR 构建中崩溃，因为服务端没有 localStorage；改为先用 light 初始化，再在 useEffect 中读取客户端偏好。
- 🔄 **Hydration 无闪烁**：只用 useEffect 会在 hydration 后切换主题，造成错误主题闪烁；通过 dangerouslySetInnerHTML 注入同步脚本，在浏览器绘制和 React hydration 前读取 localStorage 并设置元素 className，避免 mismatch 和闪烁。
- 🧩 **多实例隔离**：硬编码 id=theme 会让多个 ThemeProvider 的内联脚本争用同一元素；用 useId 为每个实例生成稳定唯一 ID，并让脚本定位对应元素，使多实例安全共存。
- ⚙️ **并发请求去重**：Server Component 在多处渲染时可能重复执行相同数据库查询；用 React.cache 包装 getPreferences(userId)，在同一请求内去重，同一查询只访问数据库一次。
- 🧠 **组合兼容**：React.cloneElement 向 children 注入 props 在 RSC、React.lazy 或 use cache 下可能失效，因为 children 可能是 Promise 或不透明引用；改用 Context 和 useContext 传递 theme，兼容服务端、客户端和异步 children。
- 🌐 **Portal 窗口感知**：全局 keydown 监听绑定父 window，在弹窗、iframe 或 createPortal 场景会失效；通过 ref.current.ownerDocument.defaultView 找到组件所在窗口并注册监听，卸载时在正确窗口清理。
- 🎨 **View Transition 配合**：在 React 19 的 ViewTransition 中直接 setState 切换面板不会播放动画；必须把状态更新包进 startTransition，过渡才会平滑。
- 🔧 **Activity 副作用**：Activity 会保留隐藏组件的 DOM，而 style 标签修改 :root 的全局 CSS 变量不会被 React 自动清理，暗色主题会继续生效；用 useLayoutEffect 在挂载时把 ref.current.media 设为 all，在清理时设为 not all 以禁用隐藏样式。
- 🔑 **服务端数据防泄漏**：Server Component 把含 token 的 user 对象传给不受控组件，可能被下游序列化进客户端；用实验性 experimental_taintUniqueValue 标记 user.token 仅服务端，传入 Client Component 时 React 抛错，整对象可用 taintObjectReference 阻断。
- 🔮 **未来防御**：useMemo 只是性能提示而非语义保证，React 可能在 HMR、离屏组件或未来特性中丢弃缓存，导致随机强调色变化；当正确性依赖持久化时改用 useState，并在 baseTheme 变化时显式重新生成颜色。

### [React Testing Library 成为 DOM 的一部分后速度更快 • sigh.dev](https://sigh.dev/posts/vibecoding-faster-react-tests/)

Scott Cooper 此前把单个 React Testing Library 测试文件提速 43%，相关 jsdom 修复大多已随 jsdom 30.1.0 发布；在此之后，他进一步验证「为 Testing Library 定制的 DOM 会快得多」，并实现 @ctrl/dom：一个面向 React 组件测试、内建改写版 Testing Library 的 DOM 实现。它在 Sentry、Base UI、React Router、React Hook Form 未改动的测试套件上带来 32%–54% 的提速，合成基准中 Vitest 下可达 5.2×；代价是仅支持 Node 26+ 与 React 19，且不实现脚本、导航、fetch、图片加载、iframe src 和真实布局，目前仍为 0.x。

- 🚀 **发布 @ctrl/dom**：发布 @ctrl/dom 0.x，一个专为 React 组件测试设计的 DOM 实现，并自带一版 Testing Library；Vitest 插件 `ctrlDom()` 会把 `@testing-library/*` 的导入重定向到 @ctrl/dom 的版本。
- 📈 **真实项目提速**：四个项目未改动的测试套件：Sentry 138.2 s→94.2 s（32%）、Base UI 59.7 s→34.5 s（42%）、React Router 17.1 s→8.9 s（48%）、React Hook Form 5.9 s→2.7 s（54%）。
- 🧩 **单对象节点模型**：jsdom 每个节点由生成的包装对象和隐藏实现对象组成，`div.getAttribute` 需先经过 wrapper；@ctrl/dom 所有节点共用同一个 `NodeImpl` 普通对象形状，类在 window 间共享，V8 可优化属性访问。首个测试后堆内存 41 MB→16 MB，Vitest worker 结束时 171 MB→111 MB；每个测试文件环境搭建从 jsdom 259 ms、happy-dom 147 ms 降至 5.13 ms。
- ⚡ **查询走内部结构**：`getByRole` 不再用 `querySelectorAll` 抓取 role~=button、input、button 再对 aria-query 的 113 个选择器逐个 `matches()`（文本输入需 12 次、按钮 41 次、`<p>` 96 次）；每个元素创建时分配数字 tag id，角色表是按 id 索引、模块加载时构建一次的数组。可见性只在命中后计算，`getComputedStyle()` 结果缓存在节点上；任何变更递增文档版本，版本不变即复用查询结果、可访问名称、计算样式和 live collection。20 字段表单 10 次 `getByRole`：jsdom + Testing Library 4.55 ms，原版 Testing Library 跑在 @ctrl/dom 上 798 µs，@ctrl/dom 自带 Testing Library 182 µs。
- 🐛 **消除二次复杂度**：`*ByRole` 候选元素原本要爬完所有祖先判断可见性，1000 层嵌套的 `getByRole` 从 6.1 ms 降到 0.09 ms，改为遇到最近的带样式祖先即停止、无样式页面直接跳过；`getAllByLabelText` 对每个 `aria-labelledby` 元素跑 `[id="x"]` 选择器而没走 id 索引 `#x`，10,000 个此类元素时一次查询从 720 ms 降到 14 ms。
- 🔄 **虚拟时钟**：jsdom 定时器按真实时间等待，`findBy*`、`waitFor`、`user-event` 都在真实毫秒上空转，Sentry 套件 13% 的时间花在等待；@ctrl/dom 改用虚拟时钟，只剩定时器时立即触发并同步推进 `Date.now()` 与 `performance.now()`，顺序不变，可用 `timeSkip: false` 按项目或文件关闭。20 ms 定时器后的 `findByRole` 23.3 ms→108 µs（216×），`user.click` 连点 10 次 53.2 ms→249 µs（213×），`user.type('hello world')` 22.9 ms→285 µs（80×）。
- 📊 **合成基准与开销分布**：100 个 React 测试文件：Vitest 下 jsdom 12.59 s，仅换 DOM 用原版 Testing Library 6.55 s（1.9×），加自带 Testing Library 2.42 s（5.2×）；Jest 2.34 s→1.80 s（1.3×）→741 ms（3.2×）；Bun 1.69 s→465 ms（3.6×）→271 ms（6.2×）。Base UI 套件剖析中 Node 模块加载占 23.1%、Vitest 14.1%、Base UI 自身代码 14.1%、react-dom 11.9%、@ctrl/dom 的 DOM 7.3%、testing 约 3%，@ctrl/dom 整体约 10%，因此 Sentry 提升 32% 而非 5.2×。
- ⚠️ **限制与风险**：只面向 React 组件测试，跳过 scripts、导航、`fetch`、图片加载、iframe `src` 和真实布局，仅支持 Node 26+ 与 React 19，需要这些能力应继续用 jsdom；项目处于 0.x，几乎肯定会在某些测试套件中暴露问题。
- 🛠️ **接入方式**：`pnpm add -D @ctrl/dom`，在 `vitest.config.ts` 中加入 `ctrlDom()` 插件即可重定向 `@testing-library/*` 导入；`ctrlDom({ testingLibrary: false })` 只替换 DOM、保留原版 Testing Library，较慢但适合依赖原版行为的测试先行迁移，Jest 配置见 README。

### [Generative Loaders — 面向 React 的文本、内联和图像加载器](https://generativeloaders.com/)

Generative Loaders 是一个面向生成式 UI 的 React 加载器集合，页面提供安装命令、文档与 GitHub 入口，并展示文本、内联和图片三类加载组件；其中文本加载器包含 16 种动画样式，页面还标注了 218k+ installs。

- 🚀 **安装入口**：提供 `npm install generative-loaders` 安装命令，并链接 Docs、GitHub 和 Sponsor。
- 🧩 **组件范围**：包含 Text loaders 16 个、Inline loaders 18 个、Image loaders 12 个，用于 React 生成式 UI 的加载状态。
- 🎨 **文本动画**：Text loaders 提供 Decode、Typewriter、Skeleton、Cascade、Focus、Wipe、Flip、Redact、Line by line、Terminal、Wave、Dissolve、Slice、Tracking、Coalesce、Fragments 共 16 种样式。
- ⚙️ **动画控制**：Text loaders 支持 0.75×、1×、1.5× 动画速度，并提供 Pause 和 Restart 操作。
- 📈 **使用量**：页面显示 218k+ installs。
- 🏢 **作者信息**：页面标注 Created by Kasturi Khanke。

### [Button Sounds — 为你的 UI 带来触感音效](https://buttons.joshwcomeau.com/)

总结失败：模型未返回符合格式的摘要。

### [button-sounds/docs/react.md（位于 main 分支） · joshwcomeau/button-sounds · GitHub](https://github.com/joshwcomeau/button-sounds/blob/main/docs/react.md)

button-sounds 的 React 文档围绕两个自定义 Hook 展开：高层 `useButtonSounds` 负责把元素 ref 与声音名绑定，在点击和释放时自动播放随机样本并预加载资源；低层 `useImperativeButtonSounds` 暴露 `press`、`release` 供调用方手动控制。文档同时说明音量、音高变化、lofi 位深/降采样参数，低层 API 下的嵌套 `pointerUp` 监听方案，以及音频文件默认走 JSDelivr CDN 或改为自托管的做法。

- 🧩 **高层 Hook**：`useButtonSounds` 接收元素 ref、声音名和可选参数；内部为每次 click 和 release 触发所选声音的随机样本，并预加载指定声音，声音名列表见 Sound Playground。
- ⚙️ **播放参数**：`volume` 默认 0.5，范围 0 到 1；`pitchVariation` 默认 0，按 +/- 调整 `playbackRate`，如 0.1 对应 0.9 到 1.1，也可传元组如 `[0.8, 1.5]` 手动设定随机最小/最大播放速度。文档建议音量取 0.25 到 0.5，音高变化少即是多，0.05 也能产生不错的变化，具体取决于声音。
- 🎨 **lofi 效果**：`lofi` 默认 false，启用后 `lofiOptions.bits` 默认 4，位深越低量化误差使声音更粗糙；`lofiOptions.downsample` 默认 0.25，降低采样率后声音更深更浑浊；`lofiOptions` 仅在 `lofi` 为 true 时生效。
- 🔄 **低层 Hook**：`useImperativeButtonSounds` 返回 `press` 和 `release`，由调用方决定何时触发；两者可选参数包括 `sampleIndex`（指定样本，省略则随机）、`volume`（默认 0.5）、`playbackRate`（默认 1）以及与高层 API 相同的 `lofi`/`lofiOptions`；低层 API 不提供 `pitchVariation`，而是每次调用直接指定实际 `playbackRate`。
- ⚠️ **嵌套事件**：低层 API 文档建议不要并列添加 `pointerDown`/`pointerUp`，而要在 `pointerDown` 处理器内嵌套 `pointerUp` 逻辑，并用 `window.addEventListener('pointerup', ..., { once: true })` 注册全局一次性监听；这样可避免在按钮上释放选中文本的鼠标时误播释放音，以及按下后移出按钮再释放时漏播释放音。
- 🌐 **自托管音频**：默认会从 JSDelivr CDN 下载 .mp3，例如 `https://cdn.jsdelivr.net/npm/button-sounds@0.0.0/assets/hi75-soft.mp3`；也可自行下载音频文件并把库指向自有副本，详见 “Self-hosting the audio files” 文档。
- 💡 **使用范围**：技术上 `useButtonSounds` 可作用于任意有效 DOM 节点，但文档强烈建议仅用于 `<button>`、`<a>`、`<input>` 等交互元素。

### [错误](https://vcarl.com/sashay/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='vcarl.com', port=443): Max retries exceeded with url: /sashay/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

### [GitHub - expo/exact：Agent 原生、基于 Rust 的高性能应用构建方式，适用于 Web、iOS、macOS、Android、Linux 及其他平台 · GitHub](https://github.com/expo/exact)

Expo 的 Exact 是一个面向 Web、iOS、macOS、Android、Linux 等平台的 all-platform 应用框架，以 Agent Native 和 Rust 高性能实现为核心，主张在每个平台按原生方式构建而非跨平台折中。项目当前处于 pre-1.0、每日变化且无打包发布和 API 稳定性承诺的状态，强调代理可驱动的开发闭环、100 ms 级启动与热重载预算，以及可保留平台原生外观又支持深度定制的统一源码方案。

- 🚀 **项目定位**：Exact 用一份源码覆盖 Web、iOS、macOS、Android、Linux，并推进 Windows、tvOS、watchOS、Android TV 和终端宿主；它把自己定义为 all-platform 而非 lowest-common-denominator 的 cross-platform，各宿主分别使用真实 DOM、UIKit、AppKit、Material 3/原生控件或 GPU/CPU 绘制。
- 🧠 **代理循环**：统一代理驱动脚本 `scripts/agent.mjs` 提供 `tree`、`screenshot`、`tap`、`type`、`state`、`layout`、`logs`、`clock`、`prefer`、`perf` 10 个操作，覆盖 web、macOS、iOS 模拟器/真机、Linux、Android 和 Windows；驱动模式使用可寻址时钟，只有 `clock +60000` 或 `clock settle` 才推进时间，避免动画和网络定时器导致测试抖动。`bun exact.mjs verify` 可一次构建并检查测试、明暗模式、多屏宽、可访问性树、动态字体溢出和滚动手感。
- ⚡ **性能预算**：硬预算包括冷启动到可交互首帧 100 ms p50、保存到呈现 100 ms p50、首像素前执行的应用 JavaScript 为零，以及约 20 KB 的 Web 运行时；常量数据在构建时烘入 plan，TypeScript 预编译为 Hermes 字节码并在首帧后加载。RealWorld 基准中 Web 构建为 26 KB，对比 React 19 的 81 KB，并比 React SSR 完成 hydration 约早 300 ms 可交互。
- 🎨 **原生与定制**：呈现优先级为 author → platform → default：未指定颜色、字号和控件外观时，iOS/macOS/Web/Android 使用 UIKit、AppKit、浏览器 DOM、Material 3 等原生控件、字体、手势、触感、键盘和无障碍行为；需要定制时可用经 Chrome 校验的 Web 标准 CSS、完整 SVG、各宿主 Canvas 2D、弹簧物理、文字绕排、自定义字体和 `wgpu` 着色器。平台能力由 60 多个一方包、Swift/Kotlin/Rust 原生模块和 `hatch="name"` 访问舱暴露。
- 🧩 **Contract 架构**：UI 用严格类型、无隐藏副作用的 `Contract` 声明，数据逻辑可用 TypeScript（原生 Hermes/Web 浏览器引擎）、Rust（原生或 Wasm，可热替换），或直接在 Contract 中声明 HTTP/GraphQL source 以实现零 JS 引擎。编译器经 syntax → types → analyze → lower 四遍生成 tables+bytecode 的 plan，原生由 Rust VM 执行并用补丁版 Taffy 布局，Web 则预编译为单个 ES module；单次构建最多报告 20 条带稳定 ID 和建议的诊断。
- 🛠️ **快速开始**：前置条件为 Rust、固定版本 Bun 1.4.2、以及 Apple 目标所需的 Swift 6.4+ 与 macOS 26.0/iOS 27.1/tvOS 27.0 SDK；`bun scripts/exact.mjs setup` 负责工具链、wasm-bindgen、Binaryen、Playwright Chromium、离线 crate 缓存和 Hermes 包。`exact new` 生成 `app.contract`、`app.ts`、`app.json`、`app.test.contract`，首次原生构建约 10–15 分钟，后续 1–2 分钟，Web 热重载约 100 ms。
- 📱 **Android 进展**：Android 可在模拟器和真机运行，支持 Material 3（Android 12+ 动态色）、真实 `EditText`、原生 Dialog/PopupWindow、Compose 日期时间选择器、`wgpu`、RenderEffect、主屏小组件、同一 APK 的 Android TV、42 个一方包和签名 Play Store App Bundle，冷启动中位数约 90 ms。仍待完成 Material 3 控件完全对齐、真机完整 TalkBack 验证，以及 `verify android` 的布局、最大字体和滚动检查。
- 💻 **Windows 早期**：Windows 11 x64 已可构建、运行和驱动，默认使用 DirectX 11 合成交换链上的 `ink` GPU painter，也可配置 CPU painter；已有原生文件对话框、AccessKit UI Automation、IME、系统主题/高对比度、托盘、Jump Lists、剪贴板、全局热键、触摸/缩放、手柄和 11 个一方包。尚未提供更新商店/OTA、`--variant` 构建，`verify windows` 也缺布局、可访问性树和最大字体检查，Fluent 2 控件样式、集成标题栏和 Mica 仍在开发。
- ⚠️ **当前限制**：项目明确尚无 JSX/React 层、无打包 CLI，且 pre-1.0 不提供兼容层；签名 OTA 只能同时覆盖 plan、资源和一个模块类型，TypeScript 与 Rust 混合生产更新尚未实现。Markdown 编辑器在 Linux/Windows/Android 仅显示纯源码，Linux 缺泰/老/高棉/缅文分词；gesture arenas、通用布局动画、grid/masonry 虚拟化、iframe 之外的通用 webview 和 GUI devtools 被有意推迟到 v1 之后。
- 🌐 **iOS 交叉构建**：可在 Linux 或 WSL 2 Ubuntu 24.04 上交叉编译、打包和签名 iOS bundle，无需运行 Xcode，但执行仍需 macOS 上的模拟器或 iPhone；需 Swift 6.4.2、xtool 1.24.0、LLVM 23、apple-codesign 0.29.0 和 Xcode 27.1 SDK。设备签名通过 `EXACT_IDENTITY`、`EXACT_APPLE_SIGN_PASSWORD_FILE`、`EXACT_PROFILE` 等环境变量配置，Linux 默认构建 ARM64 模拟器目标。

### [GitHub - flyfish-dev/file-viewer：在浏览器中预览 275+ 种文件格式：Office、PDF、OFD、CAD、3D、压缩包。纯前端，无需服务器转换。支持 Vue / React / Svelte / Web Components。· GitHub](https://github.com/flyfish-dev/file-viewer)

flyfish-dev 的 file-viewer 是面向浏览器的纯前端文件预览库，宣称可预览 275+ 种文件格式，覆盖 Office、PDF/OFD、CAD、3D、压缩包等，并通过 Web Component 与 Vue、React、Svelte、jQuery 等统一 API 接入；其核心卖点是不依赖转换服务器，按格式懒加载渲染引擎，并支持 Worker、WASM 与字体等运行时资源自托管。

- 📦 **格式覆盖**：提供 275 个已注册扩展名（225 个稳定、50 个实验性），分属 47 条预览管线，覆盖 Word、Excel、PowerPoint、PDF、OFD、DWG/DXF、STEP/IFC、压缩包、邮件、图片、媒体、代码和 DICOM 等。
- 🧩 **纯前端渲染**：文件在浏览器中解析和渲染，内置渲染器不需要转换服务器；Workers、WASM 和字体可自托管，以支持离线网络部署。
- ⚡ **按需加载**：PDF、CAD、Office、3D 等重型引擎按文件格式懒加载，只加载当前文件所需资源。
- 🌐 **多框架接入**：Web Component、Vue 3、Vue 2.7/2.6、React 16.8–19、Svelte 和 jQuery 共享 options、events 与 controller 方法；示例通过 `mountViewer` 传入 `url` 和 `filename` 挂载预览器。
- 💬 **离线国际化**：当前源码在所有框架和 Full 包中内置 7 种离线 UI 语言：`zh-CN`、`en-US`、`ja-JP`、`zh-TW`、`zh-HK`、`de-DE` 和 `ru-RU`；切换 `options.locale` 可更换 UI 文案并保留当前文件和阅读状态。
- 🛠️ **安装与预设**：可用 `npm create file-viewer@latest` 新建示例，或在现有项目运行 `npx file-viewer-cli@latest add .`；轻量组件可搭配 `@file-viewer/preset-lite`、`preset-office`、`preset-engineering` 或单个渲染器扩展格式支持。
- 🧪 **Flutter 预览**：独立 Flutter SDK 以开发预览 `0.1.0-dev.2` 发布在 pub.dev，提供离线资源、应用级预热和可复用 viewer 会话，目标平台包括 Android、iOS、Web、Windows、macOS 和 Linux，但支持仍需按平台指南确认。
- 📊 **Full 包基线**：8 个 `*-full` 包保留已发布 v2.4 `preset-all` 兼容基线，即 32 条预览管线下的 221 个扩展名；Adobe 设计文件、DICOM、二进制检查等新专用渲染器需显式安装，不会自动加入现有 Full 包。
- 🔍 **可选专业渲染器**：`@file-viewer/renderer-drawing/bpmn` 和 `@file-viewer/renderer-text/xml-profiles` 自 3.1.2 起发布在 npm，分别用于 BPMN 图和 XML 校验/转换配置，且未加入 Full 包。
- 🔧 **运行时资源**：Full 包包含版本匹配的 Workers、WASM、字体和厂商资源，但必须随应用一起提供，默认资源路径为 `<deployment-base>/file-viewer/`；Vite 可配置 `fileViewerRenderers({ copyAssets: true })`，其他构建工具可运行 `npx --no-install file-viewer-copy-assets ./public/file-viewer`。
- 🔗 **PDF URL 加载**：标准组件 PDF URL 默认在同源流式加载；CORS 签名 URL 可用 `pdf.streaming: true` 并显式传入 filename/type，或设为 `false` 一次性缓冲；需要 Range 读取时同时设置 `pdf.disableStream` 和 `pdf.disableAutoFetch` 为 `true`，且服务器需支持 Range/CORS。
- ⚠️ **限制与许可**：它是只读查看器而非编辑器，字体、厂商特性、加密文件和超大输入可能影响保真度或内存；自身源码为 Apache-2.0，但 DWG/DWF/DWFX 运行时 `@flyfish-dev/cad-viewer` 和 `dwf-viewer` 采用 AGPL-3.0-only，使用或分发 CAD 支持需遵守该许可。

### [React-PDF](https://projects.wojtekmaj.pl/react-pdf/)

未收到可整理的文章正文，因此无法生成简体中文技术周刊摘要。

- ⚠️ **缺少正文**：请提供需要整理的文章正文后再生成摘要。

### [hustcc/echarts-for-react 发布 v3.1.0 · GitHub](https://github.com/hustcc/echarts-for-react/releases/tag/v3.1.0)

echarts-for-react 发布 v3.1.0，并将其标记为最新版本。本次更新覆盖 v3.0.5 至 v3.1.0，集中修复事件监听清理、React 19 类型兼容、tslib 运行时依赖、ESM 导出解析和 ECharts 初始化选项类型，同时增加 OIDC npm 发布工作流，以提升组件生命周期可靠性、类型兼容性和打包发布质量。

- 🚀 **正式发布**：`echarts-for-react` 发布 `v3.1.0` 并标记为 Latest，变更范围覆盖 `v3.0.5...v3.1.0`，由 hustcc 于 17 Nov 发布，汇总多项修复与发布流程更新。
- 🐛 **事件监听清理**：通过 #618（@gggritso）清理上一次渲染留下的事件监听，降低重复绑定和监听泄漏风险。
- 🧩 **React 19 类型**：通过 #629（@Sam-Razavi）将 render 返回类型改为 `React.ReactElement`，以兼容 React 19 的类型要求。
- 📦 **运行时依赖**：通过 #630（@Sam-Razavi）将 `tslib` 声明为运行时依赖，避免使用方缺失该依赖导致运行问题。
- 🔗 **导出映射**：通过 #631（@Sam-Razavi）新增 `exports` 映射，使打包器把 `lib/*` 解析到 ESM 构建产物。
- ⚙️ **初始化选项类型**：通过 #632（@Sam-Razavi）让 `opts` 类型接受所有 ECharts 初始化选项，提升初始化配置的类型覆盖。
- 🔑 **OIDC 发布流程**：通过 #633（hustcc 与 @Copilot）新增 OIDC npm 发布工作流，用于 npm 包发布流程。

### [mui/material-ui 发布 v9.6.0 · GitHub](https://github.com/mui/material-ui/releases/tag/v9.6.0)

MUI 发布 v9.6.0，由 37 位贡献者完成，重点引入实验性 `unstable_enhanceDensity` 主题增强器，以统一且可调的组件密度、扩展焦点可见样式定制，并新增乌兹别克语（uz-UZ）本地化；同时集中修复 Material UI、System、styled-engine、codemod 等包中的类型、可访问性、React 17/19 兼容和运行时样式问题。

- 🚀 **正式发布**：发布 `v9.6.0`，覆盖 `@mui/material`、`@mui/system`、`@mui/utils`、`@mui/styled-engine`、`@mui/styled-engine-sc`、`@mui/private-theming` 和 `@mui/codemod` 等包，共有 37 位贡献者参与。
- 🧩 **密度增强器**：`@mui/material@9.6.0` 新增实验性 `unstable_enhanceDensity` 主题增强器，用于在组件间应用一致且可调的尺寸与密度设置。
- 🎯 **焦点样式**：新增 `focusVisible.insetOverrides` 和 `theme.applyFocusVisible`，允许进一步定制 focus visible 样式；同时修复输入框上的 `theme.focusVisible` 焦点环渲染。
- 🌐 **本地化**：新增乌兹别克语 `uz-UZ` locale，并通过主题测试本地化。
- 🛠️ **组件修复**：修复多个组件问题，包括 Autocomplete 内联自动补全高亮选项、Escape 清空时遵守 `readOnly`、ButtonBase 通过 `defaultMuiPrevented` 跳过内置键盘处理、ButtonGroup 子项重挂载、MenuList 在 ArrowUp 无焦点项时的无限循环、Popper 在 React 19 下的 “Maximum update depth exceeded”、InputBase 起始装饰下的最大更新深度错误，以及 Slider 键盘步进浮点值和 `onChangeCommitted` 旧值等问题。
- ⚙️ **主题与系统**：修复 `theme.vars` 的 `zIndex`、`opacity` 和 action opacity 类型；修复第二次 `createTheme()` 调用添加的调色板颜色在 CSS 主题变量下的问题；`@mui/system` 修复命名容器查询、标量返回类型、`color()` alpha 保留、容器查询单位保留，并在运行时创建的 style 标签上设置 CSP nonce。
- 📦 **styled-engine 与 codemod**：`@mui/styled-engine` 与 `@mui/styled-engine-sc` 保留 styled wrapper 的 prop filtering，`styled-engine-sc` 保留 styled-components 下独立的 `sx`；codemod 修复 yargs 18 CLI 崩溃和包外运行 `v5.0.0/top-level-imports`、`v5.0.0/path-imports` 的问题。
- 📚 **文档与示例**：文档新增 Next.js App Router + Tailwind CSS v4 示例，并修复 react-window 虚拟化演示的可访问性与键盘滚动、Drawer 的 `allowSwipeInChildren` 说明、Radio 使用 fieldset/legend 标注分组，以及暗色模式下 TextField 主题覆盖示例等。
- 🧪 **测试与支持**：核心侧启用一致的 type imports、API 文档在未记录 props/slots/classes 时失败、nightly 运行 React 17 测试，并记录和测试 TypeScript 5 支持策略；另新增渲染基准测试。

### [React Native OTA 更新：2026 年完整指南](https://bitrise.io/guides/react-native-ota-updates-complete-guide?utm_campaign=cp_guide_the-complete-guide-to-react-native-ota-updates_all_2026-11-09&utm_source=React%20status&utm_medium=newsletter-11-27&utm_content=classified-slot-1)

React Native OTA 更新允许绕过应用商店分发 JavaScript 变更。在 2026 年商店审核量上升、拒绝风险和审核时长不可预测的背景下，它能把修复在数分钟内送达用户，并支持对所有用户统一回滚；但粗心发布也可能同时导致所有用户崩溃。本文基于 Bitrise 构建和运营 OTA 服务的经验，给出合规性、适用性、工具选型和安全发布指南。

- 📊 **审核现状**：Apple 称截至 10 月中旬的 12 周内小版本更新平均审核 14 小时，但 App Review 每周平均处理 378,000 次提交，AI 编程工具涌入队列后，部分审核可能耗时数天或数周，且无法提前判断哪些发布会被延迟。
- ⚠️ **拒绝与安装**：2025 年 Apple 拒绝了近 800,000 次现有应用更新，被拒更新会重新进入队列；即使更新获批，用户也会按自己的时间安装。
- 🔄 **核心机制**：OTA 更新针对应用 JavaScript 变更跳过商店，可在数分钟内把修复推送给用户，并支持对所有用户撤销错误更新。
- 🛡️ **发布风险**：粗心的 OTA 更新可能同时让所有用户的应用崩溃，因此指南重点说明如何获得速度而不引入风险。
- 🧭 **指南范围**：内容涵盖 OTA 更新是什么及商店是否允许、团队是否值得采用及应做到什么程度、工具选择与搭建耗时、如何快速且安全地发布更新。

### [推出 eve 1.0 - Vercel](https://vercel.com/blog/eve-is-now-generally-available)

eve 1.0 正式发布，从 6 月的公开预览进入通用可用阶段。这是一个用于构建生产级 agent 的开源框架，预览期间发布了 230+ 个版本并合并数千个 PR。1.0 重点提升了运行速度、扩展集成和可观测性，加入审批与数据采集等安全控制，并改善了编码 agent 的开发体验；其目标是把 harness 和基础设施交给 eve，让开发者专注业务本身。

- 🚀 **正式发布**：eve 1.0 结束公开预览并正式 GA。官方称与早期采用者合作完成了 230+ 个版本和数千个 PR；已有 agent 的用户需要先按 1.0 升级指南处理 extension 构建、agent API、session 事件、客户端和保存历史等变更。
- 🧩 **自有 harness**：eve 的 harness 是调用模型、运行工具并将任务委派给 subagent 的循环。你可以选择模型、增删工具、修改指令，并决定哪些动作需要审批。开源 Workflow SDK 会在 agent 运行时保存进度，崩溃后可从最后完成的步骤继续；多人会话和 agent 间调用为内置能力。部署到 Vercel 时，Vercel Workflows 负责持久执行，Vercel Sandbox 隔离运行 agent 生成的代码。
- 💬 **多人会话**：Multiplayer 允许多人共享一个 agent 会话，eve 记录谁说了什么，并把审批和登录请求路由给正确的人，还可为单个用户或整个团队设置记忆。在 Slack 中，每个 thread 就是一个共享会话，审批按钮只允许对应用户回答，实时任务卡展示进度和耗时；用户可在 thread 内继续追问而无需再次 @ agent、取消当前轮次或重置会话。Ambient mode 让 agent 监听指定频道，即使未被提及；它按每个频道设置的目标决定何时发言或接手任务，并先用小型决策模型筛选消息以控制模型成本。
- 🌐 **原生渠道**：原生渠道包括 Slack、Microsoft Teams、Discord、Telegram、GitHub、Linear、Twilio、Web Chat 和 iMessage；Chat SDK channel 还支持任何 Chat SDK 平台适配器，包括 WhatsApp、Messenger、Google Chat 和 email。每个渠道对应一个文件，同一个 agent 可以跨所有渠道工作。
- 🎨 **前端框架集成**：1.0 扩展了 Next.js、Nuxt、SvelteKit、TanStack Start 和 Vite 的原生集成，可在构建应用时一并构建 agent 并配置路由；在 Vercel 上可把 agent 与站点部署为同一项目，也可分开托管。客户端库统一处理工具调用、审批请求和提问，便于把回复流式接入 agent 聊天、把 agent 嵌入页面或在自有组件中展示工具调用。使用 `eve add channel/web` 可基于 AI Elements 组件生成聊天应用，也可为现有 UI 添加 React、Vue 或 Svelte 绑定。
- 🏢 **多租户**：一个客服 agent 部署可用各客户自己的凭证连接其工单系统，并应用该客户的审批规则。应用负责认证用户并确定其所属租户，然后为该租户和用户设置 memory、连接凭证和审批策略。主 agent 循环每次调用模型前，dynamic definitions 会从会话和外部数据加载 agent 能力；1.0 中它覆盖模型、连接和 subagent，以及工具、技能和指令。
- 🧠 **跨会话记忆**：新增原生 memory，让 agent 把上下文从一个会话带到下一个。你可以选择记忆作用域，使用内置 file memory、记忆提供商或自行构建。内置 `fileMemory` 在 `eve dev` 中把数据保存在内存，在 Vercel 上保存到你配置的私有 Vercel Blob store。其他提供商包括 `claude-mem`、Hindsight、Kybernesis Arcana、Memanto、memco、Supermemory 和 Upstash AgentKit。
- 🔍 **OpenTelemetry 追踪**：eve 的追踪已围绕 OpenTelemetry 重建，可接入现有追踪工具。`eve dev` 默认本地记录 trace；自托管时可导出到包括自建在内的 OpenTelemetry 后端。集成包括 Raindrop，可用 `eve add instrumentation/<name>` 添加，或用 instrumentation API 自建。Trace 会显示 agent 等待人工的时段，包括工具审批、提问、预算提示和登录，并记录模型选择、审批决定、模型用量与成本，还能跟踪进入 MCP server 和远程 agent 的调用。你可以决定采集内容，按目标过滤 span 或脱敏输入输出；生产环境的私密对话默认只发送元数据，不含 prompt 或工具结果。在 Vercel 上，Agent Runs 用同一批 trace 在仪表盘展示会话、模型调用、工具执行、subagent 活动和审批决定，`eve deploy` 创建项目时会自动配置 trace 采样。
- ⚡ **降低延迟**：9 月的 Vercel Workflows 托管压力测试中，每轮中位耗时为 3.036s；1.0 在同样 100 轮工作负载下降至 414ms，p95 从 3.692s 降至 633ms，约快 7.3 倍。该测试逐条发送消息，使用立即返回的 mock 模型响应且每轮无工具调用，统计 eve 与 Workflow 开销而不含模型生成时间。改进包括 Workflow spec 9 为每次运行提供单一 orchestrator，避免后台步骤重放工作流；事件和流写入改用 WebSocket，减少冗余历史读取；eve 缓存会话路由信息，可在轮次之间把空闲会话迁移到更新部署，Web UI 还能在首条消息到达前 prewarm 会话。
- 📊 **降低工作流成本**：对一个 50 轮的 Evo Docs 会话，估算 Vercel Workflows 成本从 5.4¢ 降至 1.3¢，约降低 76%，假设每轮约两个模型步骤并保留 30 天。eve 现使用 Workflow SDK 5.5，只保存轮次间发生变化的对话数据；工作流步骤改为引用已存数据，不需要历史的步骤不再接收历史；checkpoint 保存工具返回图片的引用而非复制图片字节；prepared snapshot 跳过重复沙箱初始化，沙箱停止后可保留文件复用，会话结束时才清理。上述存储改动位于开源 Workflow SDK 中，自托管在其他 Workflow 后端的 agent 也能减少重复会话数据。模型调用方面，工具和技能清单可推迟到需要时再进入初始 prompt，连接工具通过 `eve__search` 和 `eve__tool` 运行，prompt 缓存标记方式也已调整以提高复用。Evisions 工程师称迁移到 eve 后删除 2.5 万行代码、AI 成本减半、运行时提升 66%。
- 📦 **扩展机制**：Extensions 让团队共享工具、技能、指令、连接、渠道、定时任务、hooks 和 subagent，无需在 agent 之间复制文件。可使用 extensions directory 中的扩展，或用 `npx eve@latest extension init <name>` 创建自己的扩展。示例包括 `agent-browser` 增加浏览器自动化、Mux Video 增加视频资产与剪辑工具、Link 增加钱包与购买工具。eve 会从源码构建 workspace extension，并在开发中热重载改动。
- 🛠️ **编码扩展**：1.0 的 code extension 基于 eve 默认文件工具，增加遵循仓库 `AGENTS.md` 的编码指令和技能，已包含在 `eve` 包中无需额外安装。给沙箱一个仓库后，agent 可调查代码、编辑文件并运行项目检查；它复用同一 harness 和扩展系统，因此可替换或禁用工具、覆盖技能、添加自定义指令。用 `eve add extension/code` 添加。配套的 `eve/extensions/git` 使用你配置的凭证和授权增加 GitHub 与 PR 工作流；在 Vercel 上，可选的远程 self-modification 扩展可让 agent 以 draft PR 形式修改自身源码，由人审核、合并后再部署。
- 🔗 **公共 API**：eve 的 subagent、sleep 和 question 工具构建在用户也能使用的 workflow 系统之上，入口是 `defineWorkflowTool`。工具可以返回结果、启动后台任务，或作为可恢复任务继续接收消息；它们能等待人工、webhook 或定时器而不持续占用计算资源，运行过程可跨重启存活，因此无需另建后台任务系统来协调这些工作。
- ✅ **升级与上手**：1.0 升级指南覆盖 extension 构建、agent API、session 事件、客户端和保存历史的变更，并建议部署前完成迁移；eve 遵循语义化版本，稳定 API 的破坏性变更只发生在大版本，实验性和内部 API（含实验字段）可能在大版本之间变化。新用户可用 Node.js 24 或更高版本运行 `npx eve@latest init my-agent`，也可从 Vercel 仪表盘的 agent builder 创建并部署，或选用 coding、company brain、Slack、memory、内容营销等场景模板。

### [DevTools 新功能 - 2026 年 12 月 | 博客 | Chrome for Developers](https://developer.chrome.com/blog/new-in-devtools-december-2026#sources_original_scopes_view_stack_traces_and_expression_evaluation_with_ecma-426_source_map_scopes)

Chrome DevTools 2026 年 12 月更新汇总了 Chrome 157 和 Chrome 158 在 11 月进入稳定版的变化，重点覆盖面向编码代理的 DevTools MCP 服务器、AI assistance 中的多类别 Lighthouse 审计、Elements、Sources、Application、Performance、Memory 调试能力，以及网络、控制台、设备截图和无障碍改进；同时 Modern Web Guidance 已进入稳定阶段。

- 🚀 **MCP 服务器升级**：Chrome DevTools MCP 服务器 v1.11.0 至 v1.13.0 引入 logpoint 调试、虚拟 WebAuthn 认证器、配置热重载、离线堆快照分析、并行工具执行和浏览器端录屏，面向使用编码代理的开发者。
- 🧩 **MCP 调试机制**：set_logpoints 可在脚本 URL 或源映射路径注入日志，并用原始变量名输出到 list_console_messages，且不暂停执行；configure_webauthn 可配置虚拟 ctap2 或 u2f 认证器来测试 passkey 与安全密钥流程；--watchConfig 可热重载 blockedUrlPattern 和 allowedUrlPattern 等配置。
- 📦 **MCP 快照与执行**：可在无浏览器连接时分析 .heapsnapshot，使用 analyze_heapsnapshot_contexts 检查 V8 执行上下文保留的内存，并默认分页堆快照查询和 compare_heapsnapshots 差异；不同页面的独立工具调用可并行执行，录屏默认按设备像素分辨率生成且无需外部依赖。
- 🧠 **AI Lighthouse 审计**：AI assistance 可按请求运行覆盖性能、无障碍、最佳实践和 SEO 的多类别 all Lighthouse 报告及 agentic-browsing 审计，并在报告上下文中获得失败审计标题和分数的结构化摘要；单类别报告以内联仪表显示分数。
- 🎨 **Elements 媒体状态**：Elements 面板的 :hov 窗格可在 video 和 audio 上强制 :buffering 与 :stalled 伪类，便于在不限制网络的情况下测试加载和播放回退样式。
- 🧩 **锚点定位与层叠**：position-try-fallbacks 声明新增交互式色块，可通过上下文菜单强制单个回退选项；position-area 可视化编辑器可配置 justify-self 与 align-self，悬停定位属性或 DOM 节点会高亮 IMCB。Styles 还识别 ::highlight(*) 并尊重 @layer 与来源顺序判定 !important 优先级。
- 🔍 **Sources 源映射作用域**：DevTools 支持 ECMA-426 source map scopes，在 Scope 视图重建原始词法作用域树并显示原始变量名和值；堆栈跟踪解析原始函数名、合并 outlined 辅助帧并过滤编译器生成帧；Step 系列使用源映射作用域逻辑步进；Console、Watch、条件断点和 logpoint 可用原始变量名求值并获得补全。
- 🏢 **Application 检查增强**：Application 新增 Sub apps 节点以数据网格显示 Sub apps 和 Sibling sub apps，Manifest 的 Identity 显示 Isolated Web App 的 Bundle ID 和 Parent app name；Frames 中可选帧检查自定义拼写词典；Clear site data 现同时清除 File System，Local Storage 和 Session Storage 在帧加载后可靠重新获取存储键。
- ⚠️ **问题面板与广告**：Issues 面板会标记没有用户手势触发的地理定位权限请求；Ads 面板区分主展示广告与广告相关 DOM 高亮。
- ⚡ **Performance 优化**：trace 引擎优化使大型 trace 解析速度约提升 26% 并降低峰值内存，火焰图画布重绘优化且 Treemap 去重脚本大小；Lantern 模拟在连续请求间重置 HTTP/2 溢出字节、将 HTTP/3 连接视为多路复用，并计入 ES module 编译与求值 trace 事件。
- 🧠 **Memory 上下文分析**：Memory 面板的死上下文字段分析将挂起的 generator 和 async 函数视为存活闭包，忽略已完成 ES module 的顶层函数，将未编译函数的 ScopeInfos 归因到父脚本，并把实时堆时间线统计限定在活动录制视图。
- 🌐 **Network 与 Console 修复**：WebSocket 的 Messages 标签对非 ASCII 文本帧计算准确 UTF-8 字节长度，网络搜索先检查本地缓存响应体；请求载荷参数的 Copy value 与显示值一致；Console 选择复制只包含可见文本并保留可展开对象预览，长错误类字符串不再显示为 [object Object]。
- 📱 **设备模式与截图**：设备截图会直接复制到剪贴板并显示确认通知，同时仍下载文件；Fit to window 缩放选择最大适配百分比，显式设备缩放调整在页面重载后保留。
- ♿ **无障碍改进**：点击 Accessibility 实时公告表中的 ariaNotify 公告可跳转到 Sources 中的 JavaScript 调用点，右键可在 Elements 或 Accessibility 树中显示关联节点，公告窗格可拖动调整；Quick Open、数据网格表头和工具栏下拉菜单的键盘焦点轮廓对比度提升，Settings、Service Workers 和 Recorder 的屏幕阅读器语义也得到增强。
- 🚀 **Modern Web Guidance 稳定**：Modern Web Guidance 已稳定，可通过指南帮助编码代理使用平台新特性；11 月新增 content-first-noise-reduction 指南，并更新 accessible-generated-content、faster-spa-view-transitions 和 cpp-on-the-web。

### [ecma426/proposals/scopes.md（main 分支）· tc39/ecma426 · GitHub](https://github.com/tc39/ecma426/blob/main/proposals/scopes.md)

TC39 ecma426 的 scopes.md 提出在 source map 中编码生成代码与原始源码的作用域及绑定信息，以弥补现有 source map 只能做位置映射、难以重建原始栈帧、作用域和变量绑定的问题。该提案目前处于 stage 3，包含概念数据模型、`scopes` 字段的 VLQ 编码设计、内联函数 callsite 和绑定表达式等机制，并给出示例；讨论仍标注为 WORK IN PROGRESS。

- 🧩 **提案目标**：在 source map 中新增作用域和绑定信息，让调试器在生成代码与原始源码之间重建原始帧、作用域和绑定，并隐藏或恢复编译器增删的作用域与变量。
- 🎯 **关键场景**：支持为内联函数还原栈帧和函数名、执行 Step Over/Step Out，重建被折叠或擦除的变量（如 Python 推导式编译为 JS、terser/closure 常量折叠），以及自定义值表示（如用 JSBI 模拟 BigInt）。
- ⚠️ **与另一提案差异**：文中提到另一个 env 提案解决同一问题但作用域信息更少，因此不支持本提案覆盖的全部场景，例如内联函数，以及压缩引入的变量遮蔽。
- 🧩 **概念模型**：`SourceMap` 可带 `originalScopes` 和 `generatedRanges`；`OriginalScope` 含起止位置、`kind`、`name`、`isStackFrame`、`variables` 和子作用域，`GeneratedRange` 含起止位置、`isStackFrame`、`isHidden`、关联的原始作用域、内联 callsite、绑定表达式及子范围。
- ⚙️ **编码结构**：新增字符串字段 `scopes`，由逗号分隔的带标签项构成树；原始作用域用 `B`/`C`/`D` 表示开始/结束/变量，生成范围用 `E`/`F`/`G`/`H`/`I` 表示开始/结束/绑定/子范围绑定/callsite，未知标签项可跳过。
- 📦 **编码约束**：每个 `sources` 文件最多一个顶层原始作用域树，第 n 个对应 `sources[n]`，空项表示无信息；允许多个顶层生成范围树以支持拼接 bundle。使用相对 VLQ 压缩行列、名称、kind 和变量索引，callsite 的 source/line/column 始终绝对编码。
- 🔍 **绑定机制**：绑定通过 `names` 数组中的 1-based 索引引用 JS 表达式，索引 0 表示变量不可用；`GeneratedRange.bindings` 长度需与对应原始作用域的变量列表一致，`BindingRange` 可为变量在不同子范围提供不同表达式或标记不可用。
- 🧪 **状态与示例**：提案标注为 stage 3，附 draft spec 和 prototype 链接；示例展示生成代码中 `_x`、`_z`、`_m`、`_y` 与原始 `x`、`z`、`message`、`y` 的映射，并为内联的 `console.log("Hello World2")` 记录 callsite 与绑定。

### [2026 年 JavaScript 现状](https://survey.devographics.com/en-US/survey/state-of-js/2026)

总结失败：模型未返回符合格式的摘要。

### [庆祝 Svelte 十周年](https://svelte.dev/blog/ten-years-of-svelte)

Svelte 迎来诞生十周年，社区在卢布尔雅那举办第三届 Svelte Summit，公布自定义渲染器、异步 Svelte、Rust 工具链 rsvelte、开发工具与 Storybook 集成等多项进展，显示这一前端框架正把能力扩展到原生应用、终端界面和 AI 代理开发等场景。

- 🗓️ **十周年峰会**：从首个提交算起十年后，第三届线下 Svelte Summit 在卢布尔雅那举行，为期两天；官方称将后续详解会上发布的内容，演讲会陆续发布在 Svelte Society YouTube 频道。
- 🧩 **自定义渲染器**：`Custom renderers` 已在 `experimental` 标志后获得支持，开发者可用 Svelte 构建原生应用、终端 UI、PDF 以及其他可想象的目标。
- ⚡ **异步与 Rust 工具链**：`Async Svelte` 正朝生产可用推进；核心团队成员 Yuichiro Yamashita 的 Rust 统一工具链 `rsvelte` 尚未生产就绪，但速度远快于 JavaScript 同类实现。
- 🛠️ **开发工具**：`vite-devtools-svelte` 已迁入 Svelte 组织，集成 `Vite DevTools`，正推进 1.0 版本；开发工具还暴露 MCP server，服务代理式开发。
- 🔗 **生态集成**：Svelte 成为 `Storybook` 的核心框架；面向 Svelte 组件的 Markdown 工具包 `mdsvex` 达到 1.0。
- 🧠 **AI 与代理开发**：多项发布直接服务代理式开发：开发工具提供 MCP server，`rsvelte` 让大量代理并发处理大型应用更可行；与会者普遍已频繁使用 AI，但也强调线下协作仍有无法自动化之处。
