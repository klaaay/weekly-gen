### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=this_week_in_react&utm_medium=newsletter&utm_campaign=26q4_1&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=this_week_in_react&utm_medium=newsletter&utm_campaign=26q4_1&utm_content=primary)

Meticulous 是一款面向复杂代码库的自动化端到端视觉测试平台，通过记录开发与用户交互，由 AI 持续生成并演化测试套件，实现零开发维护、确定性、无 flake 的回归验证，可在合并 PR 前评估变更影响，并支持补充或替代现有测试体系。

- 🚀 核心价值：自动化、穷尽式、确定性的验证，几乎无需开发者投入，支持按 AI/代理写代码的速度交付。
- 🧩 工作原理：在本地、预发布和预览环境加入 recorder script 记录会话，也可选记录生产环境以扩大覆盖。
- 🤖 AI 测试生成：根据交互执行到的代码分支，持续演化视觉端到端测试，覆盖每条代码路径、用户流程和边界情况。
- 🔍 PR 影响分析：提交合并请求前即可查看变更对用户工作流的影响；默认保存并回放后端响应，实现无副作用测试，避免数据变化造成误报，无需特殊测试账号或逐次造数。
- 🔁 自动维护：新功能或新边界自动新增测试，过时测试自动移除，测试套件随应用演进保持最新，无需人工编写、修复或维护。
- ⚡ 消除不稳定测试：基于 Chromium 底层构建的确定性调度引擎，消除 flake；测试高度并行化，可在约 120 秒内测试数千个页面。
- 🧪 灵活集成：可作为现有测试套件的补充或替代；提供 Next.js、React、Vue、Angular、Nuxt、SvelteKit 等接入方式及 CI 集成。
- 🏢 市场验证：已被 100+ 组织信任，Dropbox、Notion、Engine 等团队评价其能减少合并后调试、无需维护且适合复杂应用。

---

### [获取失败](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

**原文标题**: [Failed to retrieve](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

无法总结：获取内容失败，状态码 403。

---

### [Don't Trust Your AI Agent. Scope It. | PropelAuth](https://www.propelauth.com/post/dont-trust-your-ai-agent-scope-it?utm_source=twir&utm_campaign=nov11&utm_medium=newsletter)

**原文标题**: [Don't Trust Your AI Agent. Scope It. | PropelAuth](https://www.propelauth.com/post/dont-trust-your-ai-agent-scope-it?utm_source=twir&utm_campaign=nov11&utm_medium=newsletter)

文章主张，与其纠结 AI 代理是否值得信任，不如通过权限范围限制它能接触什么。这样团队无需等待模型变得完美，而是用访问控制把风险控制在可接受范围内。PropelAuth 的 MCP Authentication 通过 OAuth 2.1、用户授权、作用域、角色限制、令牌校验和审计日志，让代理权限可配置、可执行、可逐步放开。

- 🔐 核心观点：不要先问“能否信任代理”，而要问“代理应该能访问什么”，权限比模型可靠性更可控。
- 🧱 访问控制并非新问题：像给新员工或承包商分配系统权限一样，AI 代理也应按需授权，而不是默认全权访问。
- 🎯 只读权限的代理和只读权限的不可靠代理拥有相同爆炸半径，因此限制接触面能显著降低风险。
- 🛡️ PropelAuth MCP Authentication 位于 MCP 服务器前，处理代理身份、代表用户及允许操作。
- 🔑 用户通过标准 OAuth 2.1 流程连接 Claude、ChatGPT、Cursor 等 MCP 客户端，并看到明确列出权限的同意屏幕。
- 📚 支持两类作用域：用户作用域覆盖个人数据，组织作用域覆盖共享资源并绑定现有角色，例如 `write:org_config` 可仅限 Owner。
- 🧾 每次工具调用携带令牌，Introspection API 返回已授予作用域、用户组织、角色和权限，服务器在模型参与前执行检查。
- 📝 提供审计日志记录客户端创建、更新、删除及授权/撤销，并可设置会话时长强制代理定期重新认证。
- ⚙️ 对信任度高的用户，可授予覆盖产品完整功能的作用域，但代理权限仍受用户自身角色上限约束，不会因模型请求而越权。
- ✅ 对谨慎用户，可在同意屏幕取消个别作用域；服务器会拒绝缺少所需作用域的调用，模型无法通过提示词绕过。
- 🏢 管理员可将敏感组织作用域限制给特定角色、允许列表指定 MCP 客户端、缩短会话时长并审查审计日志。
- 📈 大多数团队可采用渐进路径：先只读试用，再逐步增加写入作用域；产品团队也可先发布少量只读作用域，再按敏感性添加带角色限制的组织作用域。
- 🎛️ 结论：权限让 AI 信心从“必须通过的门槛”变成“可调节的旋钮”，从舒适范围开始，观察表现，再逐步放开。

---

### [<form> – React](https://react.dev/reference/react-dom/components/form#preserve-form-values-after-an-action)

**原文标题**: [<form> – React](https://react.dev/reference/react-dom/components/form#preserve-form-values-after-an-action)

该文档是 React 内置 `<form>` 组件的 API 参考，说明如何创建交互式表单提交控件，并覆盖 `action`、`method`、`onSubmit`、Server Function、提交状态、乐观更新、错误处理、表单值保留及常见问题。

- 📝 `<form>` 用于创建可交互的信息提交控件，支持所有通用元素属性。
- 🔗 `action` 可传 URL 或函数：传 URL 时按标准 HTML 表单提交；传函数时由 React 在 Transition 中处理提交，并接收 `FormData`。
- 🧩 `<button>`、`<input type="submit">` 或 `<input type="image">` 上的 `formAction` 会覆盖表单的 `action`。
- ⚙️ `method` 仅在 `action` 为 URL 时生效，默认是 `get`；若 `action` 或 `formAction` 为函数，HTTP 方法会变为 `POST`。
- 🖱️ `onSubmit` 是提交事件处理器，可用于手动处理提交；调用 `e.preventDefault()` 可阻止浏览器默认刷新行为。
- ⏳ React 19 起更推荐使用 `action` 处理提交：React 会在 Transition 中运行它，提供 pending 状态并支持并发提交。
- 🖥️ `action` 可接收 Server Function（带 `'use server'`），即使 JavaScript 尚未加载或禁用也可提交，并接收表单的 `FormData`。
- 🧷 向 Action 传递额外数据可用隐藏字段、`bind` 绑定参数，或在客户端组件函数中读取 props/state；服务端需校验权限。
- ⌛ 使用 `useFormStatus` 可在子组件中读取 `pending`，展示“提交中”状态并禁用按钮。
- ⚡ 使用 `useOptimistic` 可在请求完成前乐观更新界面，提升表单交互的即时感。
- 🛟 `action` 函数抛出的错误可由最近的 Error Boundary 捕获；若需在 JavaScript 加载前显示错误，可结合 Client Component、Server Function 和 `useActionState`。
- 💾 函数型 `action` 成功后，React 会重置非受控字段；若需保留值，可用 `useState` 保存并传给 `defaultValue`，或用 `useActionState` 在水合前保留返回值。
- 🔀 一个表单可有多个提交按钮，通过不同 `formAction` 执行不同 Action，例如“发布”和“保存草稿”。
- 🧹 表单提交后字段被清空是成功后的默认重置行为；保存提交值到 state 并设置 `defaultValue` 即可保留。

---

### [启动框架性能项目 | e18e](https://e18e.dev/blog/launching-the-framework-performance-project.html)

**原文标题**: [Launching the Framework Performance project | e18e](https://e18e.dev/blog/launching-the-framework-performance-project.html)

2026年11月10日，Framework Performance 项目正式发布，旨在通过持续、透明、多维度的基准测试比较元框架性能，帮助维护者发现并修复瓶颈，同时为社区提供更公平的参考。

- 🚀 项目初衷：解决各元框架自测标准不一、目标场景不同导致难以公平比较的问题，并提供持续测量数据。
- 🧩 首批覆盖：Nuxt、Next.js、TanStack Start (React)、Solid Start、Solid 2.0、Astro、SvelteKit、React Router、Pracht；可提 issue 增加框架。
- ⏱️ DevTime 基准：关注依赖数量、node_modules 大小、构建/安装时间、开发服务器启动、Core-JS polyfills、浏览器基线、最低 Node 版本。
- 🌐 RunTime 基准：用同一应用测试 CSR/SSR Lighthouse（FP、FCP、INP）、首屏加载 KB、SSR 吞吐与负载、框架 Link 组件下的 SSR 负载等，并经多次运行记录 min、max、median、variance。
- 📊 真实数据：引入 HTTP Archive 数据，按桌面和移动端展示 Core Web Vitals，并补充 TanStack 检测；提醒样本量和使用方式会影响结论。
- 🔍 持续跟踪：记录每个主要/次要版本，展示框架随时间的进步，而非单次 X 与 Y 的胜负。
- 💡 实际影响：Nuxt 内部 `<NuxtLink>` 服务端直出使内部链接渲染时间约降 58%；Next.js 的 RSC payload 解析约快 75%；Solid 2.0 上游修复将 SSR 负载测试从 170 提升到 280 req/s（单连接），并发约 200 到 390 req/s；Vue Router 链接服务端渲染快 1.5–2.2 倍。
- 🛠️ 后续计划：继续新增基准和框架，欢迎反馈测试公平性与缺失项，并通过 issue 提交想法。
- 🙏 致谢与支持：感谢各框架团队、核心贡献者及 Depot 赞助；项目开源，可通过 Open Collective 赞助 e18e。

---

### [【服务器组件】遍历已解析的 JSON，而不是使用 reviver 解析 RSC 负载，作者 timneutkens ·](https://github.com/react/react/pull/35776)

**原文标题**: [[Server Components] Walk parsed JSON instead of using reviver for parsing RSC payload by timneutkens · Pull Request #35776 · react/react · GitHub](https://github.com/react/react/pull/35776)

overview summary  
React PR #35776 将 RSC 负载反序列化从 `JSON.parse` 的 reviver 回调改为“先纯 `JSON.parse`，再用纯 JavaScript 递归 `reviveModel` 遍历”，避免每个键值对触发 C++→JS 边界调用，使 RSC chunk 解析速度提升约 75%，并已在 Next.js 基准和完整测试中验证。

- ⚠️ 原有问题：reviver 会对每个键值对回调 JavaScript，主要开销来自 V8 的 C++ 与 JavaScript 边界切换；即使空 reviver 也会让解析慢约 4 倍。
- 🔄 核心改动：在 `initializeModelChunk` 中先用无回调的 `JSON.parse` 解析整个负载，再递归调用 `reviveModel` 在纯 JavaScript 中应用 RSC 转换。
- ⚡ 性能提升：不同规模 RSC 负载解析加速约 72%–78%，其中 1000 行表格 payload 从 3.0862ms 降至 0.6887ms。
- 🧠 `reviveModel` 优化：普通字符串直接短路，仅当字符串以 `$` 开头时才调用 `parseModelString`，跳过大量无关字符串处理。
- 📊 Next.js 基准：1000 项服务端组件表格平均从 17.12ms 降至 13.54ms；客户端组件从 4.65ms 降至 4.14ms。
- 🌀 Suspense 场景：嵌套 Suspense 平均从 78ms 降至 59ms；双层嵌套 Suspense 从 169ms 降至 134ms。
- 🧪 验证情况：在多个 Next.js 基准应用中测试，整个 Next.js 测试套件通过，PR 合并时 235 项检查通过。
- 📦 体积影响：多数生产包体积变化很小，部分相关包约增加 0.27%–0.79%，核心 `react-dom` 生产包基本不变。
- 🔙 后续影响：该优化已合并进 React main，并被回移到 v19.0.3 等分支和项目中使用。

---

### [React 基金会贡献者峰会 2026 · React 基金会](https://www.react.foundation/summit)

**原文标题**: [React Foundation Contributors Summit 2026 · React Foundation](https://www.react.foundation/summit)

本次内容介绍 React 基金会将于 2026 年在伦敦举办的首届线下工作峰会，旨在让各工作组成员面对面连接、对齐路线图并推进治理与协作。

- 🗓️ 峰会时间为 2026 年 11 月 10–12 日，地点在伦敦 Meta King's Cross。
- 📍 正式会议在 Meta King's Cross 办公室举行，地址为 11-21 Canal Reach, London, UK。
- 🎯 核心目标包括：确立身份、制定路线图、建立信任、正式化治理。
- 👥 这是仅限邀请的工作峰会，面向 React 基金会工作组成员，非公开会议。
- ✍️ 有兴趣参与者可通过页面提供的自荐表单申请。
- 🧭 日程安排：11 月 9 日为旅行日，11 月 10 日为全体会议日，11 月 11–12 日为工作组日，11 月 13 日为返程日。
- 🛠️ 全体会议涵盖基金会背景、工作组更新、路线图对齐和跨组优先事项；工作组日侧重路线图规划、深入讨论和协作。
- 🧩 当前计划涉及 React Native 核心运行时与渲染器、平台专家、稳定 API、分发等子团队，以及 React Fiber、DevX/开发者工具、Server、Compiler 等工作组。
- 💼 基金会无法为所有参与者赞助差旅；鼓励参与者雇主承担差旅和住宿费用，如有额外支持需求可直接联系基金会。
- 📌 餐饮与详细议程将在后勤计划确认后公布；该页面是参与者信息源，最后更新于 2026 年 10 月 2 日。

---

### [How we cut Next.js memory from ~5GB to ~1GB: the react-query timer holding every SSR request Â· rohitpotato](https://rohitpotato.xyz/thoughts/ssr-requests-still-alive)

**原文标题**: [How we cut Next.js memory from ~5GB to ~1GB: the react-query timer holding every SSR request Â· rohitpotato](https://rohitpotato.xyz/thoughts/ssr-requests-still-alive)

文章记录了 Zepto 在 Next.js SSR 服务中定位内存驻留问题的过程：react-query v3 在服务端为每个查询创建 2–5 分钟的 GC 定时器，而 Node 会把该请求的 AsyncLocalStorage 上下文挂到定时器上，导致已完成的请求无法回收；仅在服务端强制 `cacheTime: Infinity` 后，单 Pod 内存从约 4.8 GiB 降至约 1.2 GiB。

- 🔍 现象：Next.js 生产环境 Pod 内存长期停在约 5 GB，强制 GC 后仍不下降。
- 🧪 方法：不要 profile dev server；使用 production build、inspector、负载生成、堆快照和解析脚本，并在快照前强制 GC。
- 📈 证据：每处理一次请求约多保留 1 MB；336 个已完成的 `ServerResponse` 仍存活。
- 🌳 排查陷阱：dominator tree 找不到大对象；问题由大量小引用共同保活，需要从 GC roots 做 BFS 找最短 retainer path。
- 🧭 根因路径：`timerListMap[300000]` → react-query `Timeout` → `Query/QueryCache` → AsyncLocalStorage store → `ServerResponse`。
- ⏱️ 机制一：react-query v3 的 `Query` 构造时立即 `scheduleGc()`；SSR 中 `useEffect` 不运行，查询无人订阅，定时器跑满 `cacheTime`。
- 🔗 机制二：Node 会把当前 AsyncLocalStorage 上下文附加到 `setTimeout`、promise、socket 等异步资源上，定时器因此持有整个请求上下文。
- 🪝 机制三：pending timer 是 GC root，定时器可达的请求、响应缓冲和 span 都无法回收。
- 🛠️ 修复：服务端自定义 `ServerQueryCache`，在 `build` 时强制 `cacheTime: Infinity`，避免启动 GC 定时器；客户端缓存行为不变。
- 🧪 防回归：增加测试监听 `setTimeout`，确保服务端构建查询时不再创建定时器。
- ⬆️ 版本注意：v4/v5 服务端默认 `gcTime: Infinity`，但显式传入有限值仍会启动定时器，因此仍需 guard。
- 📊 结果：本地堆稳定在 70–84 MB；约 900 个应用定时器消失；保留响应缓冲从 373 MB 降至 7 MB；生产 Pod 平均内存从约 4.8 GiB 降至约 1.2 GiB。
- ⚖️ 副作用：内存泄漏此前先触发基于内存的 autoscaler；修复后副本数和延迟会变化，应改为 CPU 为主、内存阈值作安全网，并持续观察。
- 💡 结论：请求期间创建的 `setTimeout` 或长期 pending promise 会保活整个请求；GC 不释放说明仍有引用，应结合快照 diff 与根路径分析定位。

---

### [为什么我们最终离开 NextJS，转向 TanStack Start · Harrison Milbradt](https://harrisonmilbradt.com/writing/nextjs-to-tanstack-start)

**原文标题**: [Why we finally left NextJS for TanStack Start Â· Harrison Milbradt](https://harrisonmilbradt.com/writing/nextjs-to-tanstack-start)

作者讲述了将一个大型生产应用从 Next.js 迁移到 Cloudflare Workers 上的 TanStack Start 的全过程：因内存泄漏、版本锁定和构建问题决定离开 Next.js，放弃 OpenNext，通过兼容层、双框架并行和自动化验证实现平滑切换，并总结了成本、性能、踩坑与迁移经验。

- 📉 离开 Next.js 的主因是 16.3.0 和 16.3.4 出现不同原因的内存泄漏，以及 Turbopack 构建 bug 导致的反复锁定版本和回滚。
- 🧪 先尝试 OpenNext，但在大型应用上受 bundle size 限制，运行缓慢且不稳定，最终放弃。
- 🧱 迁移核心是建立“缝隙层”：把所有 `next/*` 相关导入封装到自有模块，用构建时别名兼容 Next.js 与 TanStack Start，并用 lint 禁止业务代码直接引用 `next/*`。
- ✅ 迁移前先写验证脚本：将 Next.js 路由树转成 URL 模式检查覆盖率，并对比数百个 URL 的状态码、重定向、headers、cookies 和 SEO 标签。
- 📊 先跑“生产 vs 生产”建立噪声基线，避免把原本就存在的 307/301、404/200 波动误判为迁移 bug。
- 🚀 两个应用从同一分支并行发布，Next.js 版本保持与 `main` 一致；10 月 1 日切换 DNS，随后删除旧 ECS 和约 4.2 万行 Next.js 代码，10 月 6 日 monorepo 完全移除 Next.js。
- ⚠️ 迁移后遇到 Zod 错误信息因 Vite tree-shaking 丢失 locale、旧标签页请求已删除的 JS chunk、测试覆盖缺口，以及 TanStack Start 较年轻生态的安全公告等问题。
- 💰 成本明显下降：Next.js 的 SSR 每月约 500–1000 美元，另被报价约 1400 美元/月才能获得基础日志查询；迁移后开发服务器和构建都更快。
- 📈 作者提交频率从迁移前每周约 40 次升至迁移期间约 130 次，切流后约 210 次；依赖升级更稳定，应用保持流畅。
- 📱 切流后通过小 PR 减少首屏不需要的客户端 JS，登录页和首页移动端 Lighthouse 分数提升，但作者提醒这是本地生产构建测试，需谨慎解读。
- 🧭 关键经验：先明确目标并据此验证；保持框架边界干净；迁移前建立验证流程；先做原型，不要假设一切会顺利。

---

### [WTF 是前置部署工程师吗？（以及为什么大家都在招聘他们）- PostHog](https://posthog.com/blog/forward-deployed-engineer?utm_source=twir&utm_campaign=nov11)

**原文标题**: [WTF is a forward deployed engineer? (and why everyone is hiring them) - PostHog](https://posthog.com/blog/forward-deployed-engineer?utm_source=twir&utm_campaign=nov11)

前向部署工程师（FDE）是被嵌入客户团队、弥合产品标准能力与客户实际需求之间差距的工程师。该角色起源于 Palantir，近年因 AI 企业级落地、强定制需求和高额合同而快速升温，并逐渐演化出产品、销售、技术咨询等不同变体。

- 🚀 FDE 被视为创业公司“最热岗位”之一，a16z 称其 2025 年增长达 800%，OpenAI、Anthropic、Databricks、Ramp、PostHog 等都在招聘。
- 🏢 核心定义：FDE 深入客户团队、办公室、Slack 或基础设施，参与 onboarding、实施、产品发现与开发，填补“产品能做什么”和“客户需要什么”之间的差距。
- 🧬 角色起源：Palantir 为应对情报客户的复杂审批与安全流程，把工程师“前向部署”到客户现场，与客户并肩发现和开发产品。
- 🛠️ 日常工作：大量客户会议、按需求设计开发测试、配置现有产品、把客户反馈带回核心产品团队；通常需要 20%–50% 出差。
- 🔄 价值闭环：客户获得高度定制方案，FDE 获得一线经验，核心产品团队再把经验泛化为可复用的通用能力；OpenAI 语音模型落地案例即为例证。
- 🤖 当前火热主因是 AI：基础模型能力与企业实际应用之间存在落地鸿沟，FDE 能帮助 AI 公司探索“应用层”并完成企业交付。
- 🔐 其他推动因素：AI 隐私与数据访问要求高、合同金额可达六到八位数、传统企业决策者需要看到真实结果才相信 AI 的价值。
- ⚖️ 与软件工程师的区别：FDE 聚焦单客户、快速原型和客户满意度；软件工程师聚焦可规模化、可维护的通用功能和系统稳定性。
- 🧑‍💻 与产品工程师的区别：两者都快速构建并接触用户，但产品工程师追求可复用的大众问题解决方案，FDE 一次专注一个客户。
- 🎯 适合人群：5 年以上工程或技术部署经验、客户同理心、优秀沟通与高管沟通能力、低 ego、产品感、领域专长，以及热爱工程、咨询和交付的混合工作。
- ✅ 何时该招：产品需要大量手工实施且毛利足以覆盖成本；行业监管严格；进入新垂直或新客群需要产品发现；若常规 PMF 打法已奏效，则通常不该招。
- 🧪 PostHog 案例：为大型企业分析栈迁移招聘首位 FDE，但采用远程、异步、自动化导向的“PostHog 式”实验，利用现有使用数据而非从零做产品发现。

---

### [mobx/packages/mobx-react-plugin at main · mobxjs/mobx · GitHub](https://github.com/mobxjs/mobx/tree/main/packages/mobx-react-plugin)

**原文标题**: [mobx/packages/mobx-react-plugin at main · mobxjs/mobx · GitHub](https://github.com/mobxjs/mobx/tree/main/packages/mobx-react-plugin)

mobx-react-plugin 是一个构建期插件，让开发者编写普通 React 组件和普通异步 store 方法，由插件自动完成 MobX 接线；它默认启用三项能力，并支持 Babel、Vite、React Native/Expo、webpack 等环境。

- 🧩 自动将 React 组件包装为 `observer`，避免手动遗漏。
- 🚫 为组件和自定义 hooks 添加 `"use no memo"`，防止 React Compiler 缓存导致 MobX 响应式更新失效。
- 🔄 将可观察类/对象中的 `async` 方法转换为 MobX `flow`，使 `await` 后的状态修改无需手动 `runInAction`。
- 📦 安装方式为 `npm install mobx-react-lite mobx-react-plugin`，要求 MobX 7+、mobx-react-lite 5+、React 18+；Vite 插件要求 Vite 8+。
- ⚙️ Babel 插件入口为 `mobx-react-plugin/babel`；Vite 插件入口为 `mobx-react-plugin/vite`，需放在其他插件之前，与 React Compiler 共用时应先于编译器。
- 📱 React Native/Expo 在 `babel.config.js` 中配置；webpack/Rspack/Rsbuild 通过 `babel-loader` 配置；Metro 修改后需清理缓存。
- 🎛️ 主要选项包括 `observer`、`flow`、`include`、`exclude`；`observer` 还可配置 `useNoMemo` 和 `useNoMemoHooks`。
- 🧠 组件识别规则：名称大写、创建 JSX 或调用 hooks、参数不超过两个且不返回对象/类/函数；自定义 hooks 按 `useXxx` 识别。
- ⚠️ 异步转换仅针对可静态分析、会被 MobX 转为 flow 的方法；不转换无 `await`、`for await`、静态/私有方法、箭头函数属性等。
- 🔒 React Compiler 与 `observer` 直接组合可能返回缓存 JSX 导致 DOM 不更新；插件的 `"use no memo"` 指令用于规避该问题。
- 🚪 可通过 `exclude`、组件/hook 开头 `"use memo"`、关闭 `useNoMemoHooks` 等方式选择退出自动转换。
- ✅ 使用该插件后，被转换文件中不再需要 `eslint-plugin-mobx` 的 `mobx/missing-observer` 规则；自动 `observer` 思路源自 Christian Alfoni 的 `mobx-react-observer`。

---

### [Storybook 11 beta](https://storybook.js.org/blog/storybook-11-beta/)

**原文标题**: [Storybook 11 beta](https://storybook.js.org/blog/storybook-11-beta/)

Storybook 11 Beta 发布，定位为面向编码代理的 UI 开发中心，为 React、Vue、Angular、Web Components 和 Svelte 提供代理就绪的设计系统支持。它带来官方 Skills、无头 CLI、类型安全 stories 和核心框架升级，同时包体积更小、上下文交付更快。

- 🤖 官方 Skills 和无头 CLI 帮助编码代理自主构建、测试和评审 UI，减少重复组件、错误 API 和缺失状态。
- 📦 Storybook 11 包体积比 v10 小 25%，上下文交付速度最高提升 10 倍。
- 🧭 核心 Skills 包括 `ui-workflow` 和 `component-docs`，可指导代理查找组件、查询 API、编写 stories、测试并准备人工评审。
- 🧪 通过 `storybook tools test run` 运行基于 Vitest 的功能与可访问性测试，代理可检查失败、修复并重跑。
- 👀 通过 `storybook tools review create` 生成浏览器评审页面，按变更组件和受影响页面分组展示变更摘要与关键状态。
- 🛠️ 新增 `storybook tools` 命令，提供快速无头 Storybook，支持自定义 skills、工具和工作流，并按需连接开发服务器。
- 🧩 继续支持 MCP，但推荐使用 Skills 作为本地代理使用 Storybook 的更顺手方式。
- 🧱 CSF 4 提供完全类型安全的 stories 工厂 API，支持增量升级 codemod，CSF 3 仍受支持。
- ⚛️ 核心框架全面升级：React 使用 `react-component-meta`，Vue 升级 `vue-component-meta`，Angular 推出 `@storybook/angular-vite`，Web Components 集成 CEM，Svelte 升为核心框架并支持 Svelte 5/SvelteKit 3。
- 🚀 计划 12 月正式发布，可用 `npx storybook@next upgrade` 升级项目，或用 `npm create storybook@next` 新建项目。

---

### [发布 v5.1.0 · pmndrs/zustand · GitHub](https://github.com/pmndrs/zustand/releases/tag/v5.1.0)

**原文标题**: [Release v5.1.0 · pmndrs/zustand · GitHub](https://github.com/pmndrs/zustand/releases/tag/v5.1.0)

Zustand v5.1.0 已发布，主要改进了 `persist` 和 `devtools` 中间件，并增强了 Promise 兼容性与 Redux DevTools 操作分发能力。

- 🚀 最新版本为 v5.1.0，由 dai-shi 于 11 月 6 日发布。
- 💾 `persist` 中间件现在支持来自存储读取、迁移及迁移写入的 `PromiseLike` 结果。
- ⏳ `persist.rehydrate()` 现在返回原生 `Promise<void>`，可等待水合完成。
- 🛠️ `devtools` 中间件新增 `actionCreators` 选项，支持直接从 Redux DevTools 分发 store actions。
- 🧩 `devtools` 还支持嵌套 actions 及其参数。
- 🔧 相关变更包括修复 persist 迁移的 Promise-like 支持（#3583）和 devtools action 分发（#3595）。
- 👥 贡献者包括 dai-shi、dgesteves 和 Tnalxmsk。

---

### [宣布 XState v6 Beta | Stately](https://stately.ai/blog/2026-11-05-xstate-v6-beta)

**原文标题**: [Announcing XState v6 beta | Stately](https://stately.ai/blog/2026-11-05-xstate-v6-beta)

XState v6 首个 beta 正式发布，重点让状态机更易读、易写、易验证，并可在任何环境运行；核心 API 已稳定，持久化执行等少数能力仍为实验性。此次版本大幅简化 API、强化类型安全，并围绕 AI agent、CLI、可视化编辑和 durable execution 做了专门设计。

- 🚀 **版本定位**：XState 是 MIT、零依赖的状态管理与编排方案，基于状态机、状态图与 actor 模型，可编排 Promise、状态机等任意逻辑；目前已有 30k+ stars、800 万+ 周下载量。
- ⚙️ **Transition 变为普通函数**：接收 `context`、`event`，返回目标状态与上下文更新；副作用通过 `enq.emit`、`enq.raise`、`enq.sendTo`、`enq.spawn` 等入队，不再需要 action creators 和独立 guard。
- 🛡️ **更强类型安全**：使用 Zod 或 Standard Schema 声明 `schemas`，让 `actor.send(...)`、事件 key、上下文更新都获得类型检查；新增 typestates 与 state input，使上下文在特定状态中更精确。
- 🧩 **轻量 FSM 回归**：`xstate/fsm` 回归，约 0.5KB min+gzip，语法与完整状态机一致，不引入 actor runtime；需要升级时可平滑改用 `createMachine`。
- 🤖 **面向 Agent 优化**：安装包内置对应版本文档，包括面向 agent 的指南；开发环境会对 v5 旧写法给出替换提示，生产环境使用错误码；还会冻结 context 并警告未处理事件。
- 🛠️ **新增 CLI 工具**：`inspect`、`validate`、`simulate`、`test`、`replay`、`diff` 可对 JSON 状态机定义进行检查、模拟与测试，不运行应用代码；支持 `machineToJSON` / `machineFromJSON`。
- 🖥️ **可视化编辑器支持 v6**：编辑器可读写 v6 代码，支持 Editor Sync 双向同步；可通过 VS Code 扩展或 `statelyai open` 使用，视觉修改会确定性写回源码。
- 🔁 **Durable execution**：纯 transition、稳定 effect ID、确定性 actor 地址，方便持久化宿主记录与重放；实验性 `xstate/durable` 提供适配器，面向 Temporal、Restate、Inngest、Cloudflare 等。
- 🧠 **用状态机构建 Agent**：仓库新增工具循环、人审、模型回退、流式响应、RAG、MCP、多 agent 编排等示例；Stately Agent 2.0 alpha 可检查不安全状态、重放事件日志并支持自我改进。
- ✨ **其他新特性**：并行区域不再误重置兄弟区域、状态级 `onError`、未处理事件检测、choice states、状态超时、时长字符串、route states、`actor.select`、内部事件、`createAsyncLogic`、`createStepLogic`、actor registry、快照版本化、`createStateConfig`、`@xstate/effect` beta。
- 🧹 **移除旧 API**：删除 action creators、高阶 guard、字符串 transition、`types`/typegen、`fromPromise` 等工厂、`@xstate/immer`、`snapshot` 恢复选项、`@xstate/inspect`、`interpret(...)`，以统一写法。
- 🔄 **迁移支持**：提供 `npx xstate migrate 'src/**/*.ts' --dry` codemod，可转换导入、目标、schemas、actions/guards 等；支持 v5 与 v6 并存、逐机迁移，v5 仍受支持。
- 🧪 **Beta 状态**：自 2026 年 6 月以来已发布 70+ alpha；核心 API 稳定，除非大量反馈要求，否则稳定版前只做必要破坏性变更；React、Vue、Svelte、Solid、test、scxml 集成也有 beta。
- 📦 **试用方式**：`npm i xstate@beta`；可在真实项目中试用或让 agent 使用，并通过 Discord、GitHub Discussions 反馈问题。
- 🧭 **为何建模更重要**：AI 能快速生成大量代码，人类需要更高层的行为模型来理解和验证系统；状态图适合表达状态、事件与转移，也便于安全检查、可达性测试和未来形式化验证。

---

### [Text.js | 控制台框架](https://textjs.org/)

**原文标题**: [Text.js | The Console Framework](https://textjs.org/)

概述：Text.js 让全栈 React 应用直接渲染在浏览器 `console.log` 中，并提供组件、路由、服务端渲染、终端运行和代理协作等完整工具链。

- 🚀 快速开始：运行 `bunx create-text-app` 创建应用；页面在 DevTools 控制台预览，并支持方向键等键盘交互。
- ⚛️ 基于 React 19：支持并发渲染、Suspense 和错误边界；App Router 中 `app/` 目录即路由与布局，支持前进、后退和深链。
- 🧱 内置终端 UI 组件：包含 Box/Stack/Grid/SplitPane/ScrollBox、List/Table/Tree/Markdown/Code/Diff、图表、表单控件，以及 `useKeymap`、`useFocus` 等键盘能力。
- 🎨 自定义渲染管线：React reconciler → Yoga 单元格布局 → CellBuffer 仅重绘脏行 → 行哈希脏门控 → RLE 编码为 `%c` span → 单次 `console.log` 输出帧。
- ⚡ 性能优化：未变化帧产生 0 次 log；3200 个单元格可压缩为 149 个 `%c` spans；全量重绘 0.163ms，单行编辑 0.011ms；追加帧比 `clear()+log()` 的空屏率更低（1.0% vs 70.6%），帧至少间隔 66ms 追加。
- 🖥️ 服务端渲染：设置 `runtime = "server"` 可在服务端渲染路由和异步组件，浏览器仅加载 21kB gzip 帧播放器，并通过 SSE 行增量更新。
- 🧩 框架能力：支持 Partial Prerendering、`middleware.ts`、`revalidate`/`unstable_cache`/`revalidateTag` 缓存，以及 static、bun、vercel、cloudflare 部署适配器。
- 💻 多环境运行：`text run` 在终端以 ANSI 真彩运行同一 App Router 应用；`text mcp` 让编码代理导航路由、按键并读取帧文本；OpenCode Lite 也被重建为可在浏览器控制台运行的 TUI。
- 🛠️ 开发工具：DevTools 扩展提供组件树、帧检查器和逐帧时间线；另有 VS Code 预览与脚手架、ESLint 插件、`@textjs/app/testing`、TX 错误码、`window.text` REPL、RTL 和 FIGlet 字体支持。
- 🎓 学习资源：免费课程共 10 章、约 65 分钟，涵盖入门、布局、文本样式、输入、路由、数据、表格图表、测试、终端运行与发布。

---

### [发布 11.2.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.2.0)

**原文标题**: [Release 11.2.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.2.0)

Preact 11.2.0 已发布，主要带来 Shadow Root 下的作用域自定义元素注册表支持、事件处理与错误边界修复，以及 core、hooks、compat 的包体积优化。

- 🚀 最新版本 Preact 11.2.0 于 11 月 6 日发布。
- 🧩 新功能：渲染到 Shadow Root 时支持作用域自定义元素注册表（#5342，感谢 @JoviDeCroock）。
- 🛠️ 修复：忽略 `on*` 属性中的非函数值，避免注册无效事件处理器（#5345）。
- ⚠️ 修复：错误边界可接收抛出的 `null`/`undefined`，不再替换为 `TypeError`（#5347，感谢 @jonkwheeler）。
- 🔄 修复：保留已卸载节点上的事件处理器，使已冒泡事件能够完成处理（#5349）。
- ⚡ 性能：减少 core、hooks 和 compat 的包体积（#5343）。
- 🙌 贡献者包括 @jonkwheeler 和 @JoviDeCroock，该版本获得 5 个 🎉 反应。

---

### [GitHub - remcohaszing/mdx-content-mapper：用于 MDX 内容的 TypeScript 内容映射器 · GitHub](https://github.com/remcohaszing/mdx-content-mapper)

**原文标题**: [GitHub - remcohaszing/mdx-content-mapper: A TypeScript content mapper for MDX content · GitHub](https://github.com/remcohaszing/mdx-content-mapper)

mdx-content-mapper 是 Remco Haszing 开发的用于 MDX 内容的 TypeScript 内容映射器，目标是最终并入 mdx-analyzer，以替代 @mdx-js/typescript-plugin；它通过 tsconfig 配置让 tsc 对 MDX（及可选 Markdown）进行类型检查，并支持代码块检查、框架预设、组件 provider 和插件扩展。

- 📦 安装与使用：运行 `npm install mdx-content-mapper`，完成配置后使用 `tsc --runExternalCode` 对项目（含 MDX 文件）做类型检查。
- ⚙️ 配置方式：在 `tsconfig.json` 的 `contentMappers` 数组中添加包 `mdx-content-mapper`，并指定 `extensions`（通常为 `.mdx`，也可加入 `.md`）和 `options`。
- ✅ `checkCodeBlocks`：可对 `cjs`、`cts`、`js`、`jsx`、`json`、`ts`、`tsx` 等语言的代码块做类型检查，需启用 `allowJs` 或 `checkJs`。
- 🧩 `checkMdx`：未设置 `checkJs` 时，可用该选项启用 MDX 内容类型检查，但需要在编译器选项中设置 `allowJs`。
- 📝 `mdExtensions`：用于覆盖 MDX 编译器识别普通 Markdown 的扩展名；新增需检查的扩展名也要加入 `extensions`。
- 🧭 `preset`：支持 `next`（推断 Next.js App Router 的 props）和 `@react-router/fs-routes`（推断 React Router 文件路由 props）。
- 🔌 `providerImportSource`：指定 `useMDXComponents` 的导入源，以检查提供给 MDX 的组件类型；Next.js 可设为 `./mdx-components` 或 `./src/mdx-components`。
- 🛠 若只使用单一 provider，可通过 `#mdx-components` 子路径导入，并在打包器和 content mapper 中统一设置 `providerImportSource`。
- 🧱 插件支持：`recmaPlugins` 目前仅支持 `recma-export-filepath`；`rehypePlugins` 仅支持 `rehype-mdx-title`；`remarkPlugins` 支持 `remark-mdx-frontmatter` 以及 `remark-directives`、`remark-frontmatter`、`remark-gfm`、`remark-math` 等解析级插件。
- 🧪 兼容性：需要 TypeScript 7.1+ 与 Node.js 22+；项目采用 MIT 许可证。
- 📊 仓库概况：约 25 stars、0 forks、1 watcher、107 commits。

---

### [发布版本 7.92.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.92.0)

**原文标题**: [Release Version 7.92.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.92.0)

React Hook Form v7.92.0 已发布，本次更新集中修复表单状态同步、脏状态跟踪、验证结果、字段数组、Controller/useWatch、handleSubmit/reset 等核心问题，同时包含性能优化、重构、测试扩展和依赖升级。

- 🐞 修复 `useFormState` 和 `Controller` 在挂载/卸载时不必要地克隆表单状态，以及 `setValues` 未更新未注册字段脏状态等问题。
- ✅ 修复 `setValue` 对空字符串复选框选项、异步表单级验证结果过期、`useFieldArray` 在提交前应用 `reValidateMode: 'onSubmit'` 等问题。
- 📋 修复禁用 `optgroup` 的 `select` 默认值应用不正确、`useController` 读取过期 `shouldUnregister`、聚焦禁用单选/复选框等问题。
- 🧩 修复 `trigger` 丢失嵌套字段数组根错误、未按 `shouldTouch` 标记嵌套字段、`unregister` 删除父级时保留后代注册等问题。
- 👀 修复 `useWatch` 在 React Native 挂载时缺失 `reset()` 更新、`compute` 移除后缓存不同步、字段数组通知使用过期值等问题。
- 🧾 修复 `handleSubmit` 在异步回调中 `reset()` 后错误更新表单状态、禁用字段下对 nullish/原始转换值支持，以及 `<Form />` 未遵循 `encType` 构造请求体。
- 🛠️ 修复 `reset` 取消待处理验证后未更新 `isValid`、重复 `reset()` 与 `keepFieldsRef`/memoized inputs 的错误聚焦、`setValues` 值未变时忽略选项等。
- ⚡ 性能优化：避免 `useFormState` 和 `Controller` 中不必要的表单状态克隆。
- 🧹 重构：收集脏字段名时跳过非脏数组空洞，构建 resolver 选项时避免修改字段元数据。
- 🧪 测试：扩展 `reset`、`useController`、`useFieldArray`、验证、脏状态、表单提交、禁用输入、React Native 等回归覆盖。
- 📦 依赖：升级 `fast-uri` 3.1.9、`follow-redirects` 1.16.2、`vite` 6.4.5、`joi` 18.3.1。
- ❤️ 致谢：感谢 `@bluebill1049` 等贡献者以及 Pennylane 团队的支持。

---

### [版本发布 · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases)

**原文标题**: [Releases · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases)

该内容梳理了 bvaughn/react-resizable-panels 仓库从 4.15.3 到 4.21.0 的版本发布记录，核心围绕 `Workspace` 标签页布局系统的持续增强，包括浮动标签集、标签集整体拖拽、折叠/展开、跨窗口拖拽、剩余空间 API、RTL 支持、性能优化以及多项缺陷修复。

- 🚀 **4.21.0（最新）**：新增 `TabsetCollapseButton` 和 `TabsetMaximizeButton` 组件，支持折叠/展开与最大化/还原标签集，并带有 `aria-expanded`、`aria-controls`、`aria-pressed` 等无障碍属性；多个组件的 `children`、`className`、`style`、`title` 可基于组件状态动态生成；修复 `preserve-pixel-size` 下分数像素导致的面板漂移问题。
- 🪟 **4.20.0**：`Workspace` 支持浮动标签集，用户可通过标题移动、通过边缘缩放，并在其中拖入/拖出标签；标签和标签集可拖放到工作区边缘，形成侧边栏或底部面板；`TabDropTarget` 新增 `{ edge }` 变体。
- ⚡ **4.19.1**：优化调整大小和拖拽性能，无 `onResize` 的 `Panel` 不再被观察，拖拽标签时仅重新渲染变化部分；生产构建移除开发警告；`disableDrop` 仅在放置目标变化时调用。
- 🧲 **4.19.0**：新增 `onTearOff` 属性，支持将标签或整个标签集拖出窗口以打开弹窗；新增 `dragGroup`，支持在多个工作区之间（包括跨窗口和跨应用实例）拖拽标签；改进空工作区放置指示器，并支持指示器在标签集之间动画过渡。
- 🌐 **4.18.1**：修复标签列表被压缩至 0px 后剩余空间不更新的问题；修复 RTL 布局下的标签拖拽、键盘导航和边缘放置行为。
- 🧩 **4.18.0**：新增 `normalizeWorkspaceModel` 用于校验和整理模型；新增标签列表剩余空间相关 API（`useTabListFreeSpace`、`getTabListFreeSpace` 等）；修复标签集最小尺寸不匹配时的显示问题；标签集新增 `maxWidth` 和 `maxHeight`。
- 🗂️ **4.17.0**：支持拖拽整个标签集，可移动到其他标签集边缘或合并其标签；新增可折叠标签集及 `collapseTabset`、`expandTabset` 方法；新增 `tabRemovalSelectionBehavior`，用于控制关闭标签后的选中行为。
- 🛠️ **4.16.1**：新增 `split` 样式入口，用于设置标签集间距；修复分隔条拖拽中断、元素 ID 冲突，以及标签边缘同时触发缩放和拖拽的问题。
- 🏗️ **4.16.0**：新增 `Workspace` 组件，支持标签集拖拽重排、缩放和最大化，布局由可序列化模型描述，移动标签时内容不会重新挂载；支持鼠标、触摸和键盘交互；修复 CSS `zoom` 或缩放变换下的分隔条移动偏差。
- 📦 **4.15.3**：修复部分打包器（如 esbuild）未移除未使用组件的问题，通过纯注解表达式设置 `displayName`，并在 `package.json` 中声明 `"sideEffects": false`。

---

### [版本发布 · meta/astryx · GitHub](https://github.com/meta/astryx/releases)

**原文标题**: [Releases · meta/astryx · GitHub](https://github.com/meta/astryx/releases)

该页面汇总 Astryx 从 v0.7.5 到 v0.7.14 的发布说明：所有 `@astryxdesign/*` 包同步发版，内容以组件功能增强、触控与手势优化、动效主题化、无障碍修复和大量缺陷修复为主，同时包含 CLI、主题工具与实验性 API 的更新及性能改进。

- 🚀 **版本与升级**：v0.7.5–v0.7.14 连续发布，Core、CLI、主题等包统一版本；升级使用 `npm install @astryxdesign/core@版本 @astryxdesign/cli@版本`，并运行 `npx @astryxdesign/cli upgrade --from "$OLD_VERSION" --apply --path .`。
- 🧱 **BottomSheet 重点升级**：支持多 Sheet 堆叠与平滑交接，改进触摸拖拽、关闭速度、滚动边缘、键盘弹出及 Safari/iOS 行为；`BottomSheetSwitcher` 已弃用但保持兼容。
- 👆 **触控与手势增强**：Popover、DropdownMenu、MoreMenu 支持按压即开；Lightbox 增加下拉关闭、双指缩放和 iOS 相册式翻页；Carousel、SegmentedControl、Switch、List 等改进拖拽、吸附与弹簧动画。
- ♿ **无障碍与焦点管理**：Banner 的 `role="alert"` 收窄到消息本身，FieldLabel 信息按钮可用键盘访问，Dialog 自动聚焦支持回退，禁用字段仍可 Tab 到达，并减少重复 live region、重复 ID 和 ARIA 覆盖问题。
- 🎞️ **动效主题化**：主题新增 `tempo` 与 `character` 配置，统一 `--ease-entrance`、`--ease-move` 等动效令牌；动画布局、弹层入场、Sheet 关闭等遵循主题节奏，并尊重 Reduce Motion。
- 📦 **组件能力扩展**：Tokenizer 支持 InputGroup、菜单转发和开关方法；PowerSearch 新增 adaptive/bottom-sheet 触控流程；CodeBlock 支持更多语言、自定义控件和起始行号；Table 支持行虚拟化；List 支持动画布局与可重排。
- 🧭 **布局与交互修复**：AppShell 改进安全区、重复 main id 和键盘滚动；LayoutPanel 折叠滑动、ResizeHandle 越界阻力、ChatLayout 软键盘避让、Kbd 平台键名显示等均有更新。
- 🐞 **关键缺陷修复**：覆盖 Safari/iOS 触摸拖拽、BottomSheet 误判与重绘、Carousel 焦点环和滚轮重复滚动、Calendar/Date 输入 hydration mismatch、Selector/Dialog/Popover 焦点与关闭行为、复制失败提示等。
- 🧪 **CLI 与实验 API**：`astryx discover` 增加实验组件发现；图标集支持主/备选择与缺失占位符；主题构建保留 `componentIcons`；`astryx experimental render` 可生成自包含 HTML；搜索与构建性能明显优化。
- 🎨 **主题与视觉调整**：提升状态色、对比度和暗色模式可读性，修复 Avatar、Banner、CodeBlock 等视觉问题；主题可按 variant/尺寸选择图标，主题模板同步更新。
- ⚠️ **兼容性注意**：部分默认行为变化需显式回退，如 TimeInput `hourFormat` 跟随 locale、NumberInput 粗指针隐藏 stepper、Popover/PowerSearch/Tokenizer 的 adaptive 默认、BottomSheetSwitcher 与 FieldStatus tooltip variant 弃用等。
- 🛠️ **升级建议**：升级前查看各版本默认行为变化，重点回归 BottomSheet、表单与日期组件、触控菜单、无障碍焦点、SSR hydration 和主题动效。

---

### [dx-styles 1.5.0：构建时间减半，以及一个可以重新运行的基准测试——dx-styles 博客](https://dx-styles.dev/blog/dx-styles-1-5-build-time/)

**原文标题**: [dx-styles 1.5.0: half the build time, and a benchmark you can rerun â dx-styles blog](https://dx-styles.dev/blog/dx-styles-1-5-build-time/)

dx-styles 1.5.0 已发布，最低要求 wyw-in-js 2.7.1；此次升级把生产构建时间大约减半，并随版本提供了一套可重新运行的构建基准，用来对比 dx-styles、其他 CSS-in-JS 库和纯 CSS Modules 的性能与产物。

- ⚡ **构建提速**：在包含 1,308 个 recipe 变体的生成式设计系统场景中，预热生产构建从 1.34 秒降至 0.68 秒（−49%）；所有样式集中在单个模块时，从 1.79 秒降至 0.78 秒（−56%）。
- 📦 **版本要求**：dx-styles 1.5.0 要求 wyw-in-js 2.7.1；在 2.7.1 上，dx-styles 1.4.1 与 1.5.0 构建出的 bundle 字节完全一致且耗时相同，1.5.0 的意义在于把 2.7.1 设为最低版本。
- 🧪 **可复现基准**：基准位于 `dx-styles/benchmarks`，同一场景对比 dx-styles、8 个其他库和纯 CSS Modules，并包含 dx-styles 不占优的案例。
- 🛠️ **提速来源**：dx-styles 是 wyw-in-js 之上的一组处理器，大部分构建时间花在引擎上；wyw-in-js 2.5 降低大项目解析成本并共享解析结果，2.6 避免按每个样式声明重复执行多轮处理，改为就地合并规则、每个文件只构建一次 Stylis 插件链、标签引用检查只遍历一次。
- 📊 **各版本耗时**：按组件分模块时，wyw-in-js 2.3.0/2.4.4/2.5.1/2.6.0/2.7.1 分别为 1.43/1.35/0.91/0.68/0.68 秒；单样式模块时为 1.94/1.78/1.34/0.78/0.78 秒，均为 7 次预热构建的中位数。
- 🏁 **横向对比**：预热构建耗时方面，styled-components 0.16 秒、Emotion 0.17 秒、Panda 0.21 秒、next-yak 0.30 秒、vanilla-extract 0.56 秒、CSS Modules 0.66 秒、dx-styles 0.68 秒、Linaria 1.86 秒、StyleX 2.06 秒、Compiled 5.93 秒。
- 🎨 **运行时库特点**：styled-components 和 Emotion 构建最快，是因为不在构建期做 CSS 工作，样式随 JavaScript 在运行时注入，因此首屏绘制比 dx-styles 晚约 45–50 毫秒；在构建期提取 CSS 的库中，dx-styles 与纯 CSS Modules 构建耗时相当，0.02 秒差异属于噪声。
- 🧩 **Linaria 对比**：Linaria 同样运行在 wyw-in-js 2.7.1 上，但该场景中每个样式模块都会插值共享 token 对象，导致引擎重复求值，构建耗时 1.86 秒；dx-styles 以 contract 形式声明 token，处理器无需求值即可解析。若 Linaria 改用静态 CSS 变量，构建耗时 0.38 秒，说明 dx-styles 的 token contract 与 recipes 层在该场景增加约 0.3 秒。
- ✅ **渲染正确性**：浏览器中对比 3,642 个元素的 22 个计算属性，除 Compiled 2.0.0 外均与 dx-styles 渲染一致；Compiled 默认 class hash 发生碰撞，使 5 个元素颜色错误，启用 `collisionResistantHash` 可修复，构建时间不变，gzip 增加 1.4 KB。
- ⚠️ **不占优之处**：Panda、next-yak、vanilla-extract 和使用静态 CSS 变量的 Linaria 构建更快，纯 CSS Modules 与 dx-styles 耗时相同；dx-styles 总 gzip 为 99.4 KB，高于除 Linaria 和纯 CSS Modules 外的大多数方案；CSS 原始体积 382 KB，高于 vanilla-extract 的 314 KB，但保留可读的 token 变量名作为主题契约。
- 🔬 **测量方法**：场景由 104 个设计 token、45 个结构槽位、34 个 recipe 家族和 1,308 个变体生成，渲染为问题追踪界面加全变体画廊，共 3,642 个元素、41 个样式模块；使用 Apple M3 Max、macOS 26.6.2、Node 24.4.1、Vite 8.3.5、React 19.3.1，Chromium 156 测首屏；所有项目精确锁版本，等待 90 秒文件索引后预热，再跑 7 轮交替冷/热构建，取预热中位数。
- ⬆️ **升级方式**：运行 `npm install dx-styles@^1.5.0` 和 `npm install -D @wyw-in-js/vite@2.7.1`；Next.js 项目将 `@wyw-in-js/nextjs` 更新到 2.7.1；其他 bundler 更新对应 wyw-in-js 集成，并与 dx-styles 一起升级，因为 1.5.0 需要 wyw-in-js 2.7.1 或更新版本。

---

### [发布 v4.15.0 · amannn/next-intl · GitHub](https://github.com/amannn/next-intl/releases/tag/v4.15.0)

**原文标题**: [Release v4.15.0 · amannn/next-intl · GitHub](https://github.com/amannn/next-intl/releases/tag/v4.15.0)

overview summary  
next-intl 发布 v4.15.0，包含 1 项功能更新和 6 项修复，主要提升消息提取、路径匹配和中间件重定向的稳定性与可靠性。

- 🚀 发布 v4.15.0（2026-11-11），为最新版本，包含 3 个提交。
- ✅ 新增支持：允许在 use-intl 中使用 intl-messageformat@12。
- 📁 修复：提取目录内容未变化时跳过写入，减少不必要的文件操作。
- 🔒 修复：以原子方式写入提取目录，避免读取方看到截断文件。
- ⚡ 修复：消息提取器中懒加载 @swc/core，优化加载行为。
- 🧭 修复：优先使用静态内部路径，而非重叠的动态路径。
- 🔗 修复：在中间件重定向和重写目标中保留编码的百分号。
- 🧩 修复：useExtracted 对象形式支持简写值和 formats。

---

### [ChatGPT](https://chatgpt.com/plugins/plugins_6ac4c117f76881918d3676e851fa4005?open_in_app)

**原文标题**: [ChatGPT](https://chatgpt.com/plugins/plugins_6ac4c117f76881918d3676e851fa4005?open_in_app)

您尚未提供任何文章正文，因此我无法生成摘要或提取关键要点。

- 📄 请将需要总结的文本粘贴在“Use the following content:”之后。
- ✅ 收到内容后，我会用中文输出简洁的概述摘要，并用“-”符号和合适的 emoji 列出关键要点。

---

### [A preview of Exact Â· Wholly Unreasonable](https://ccheever.expo.app/)

**原文标题**: [A preview of Exact Â· Wholly Unreasonable](https://ccheever.expo.app/)

Exact 是由 Charlie Cheever 推出的全新 Agent Native 应用框架，使用 Rust 编写，目标是让开发者以极高性能构建完全定制化的体验。它通过专为 AI 智能体设计的 Contract 语言统一 UI、状态与数据流，在 Web、原生移动端和桌面端提供接近静态站点速度与 React 式动态更新能力，目前为 pre-alpha 预览。

- 🚀 **Exact 预览**：基于 Rust 的 Agent Native 应用框架，强调极快性能、无妥协的定制体验，并让智能体更易构建和调试。
- 📊 **Web 性能**：在 Pokédex 基准中与 Astro 接近，明显领先 Next.js 和 SvelteKit；作者体验基准中生成正确结果的速度快于 Next.js，成本相近。
- 🧠 **Contract 语言**：类似 Python、强类型、显式且约束严格，同时描述 UI、状态和数据流；可完整分析，避免递归循环、useEffect 和任意 JS/TS 等常见问题。
- 🤖 **为智能体优化**：编译器提供按需、针对性的错误信息来教智能体学习语法；智能体可控制时钟、读取 UI 状态、截图/录屏、检查布局属性，减少调试竞态。
- ⚡ **快速更新**：编译期掌握数据布局与关系，无虚拟 DOM、重渲染或独立 hydration；Contract 变更通常 10–20ms 并保留状态，支持 OTA。
- 🦀 **Rust + TypeScript**：业务逻辑可用 Rust 或 TS，也可混用；Rust 可纯原生运行，TS 便于大型应用迭代；首帧可由 Rust 绘制而不等待 JS VM。
- 🪟 **Access Hatches**：可接管矩形区域写原生代码，也可访问框架生成的 UIKit 等原生节点，精细控制细节，例如修复 Liquid Glass 示例中的长按闪烁问题。
- 📱 **原生性能**：富内容滚动中 Exact 保持 120fps 零掉帧，SwiftUI 降至 30–50fps；启动时可预烘焙首屏 UI 与可计算数据，Rust 先绘制首帧。
- 🎨 **布局与图形**：用 Rust 和基于 CSS 的 Taffy 做布局，样式偏 Web 形态；支持文本测量、GPU、shader 内实时 UI，以及类似 HTML-in-Canvas 的能力。
- 💻 **多平台策略**：iOS/macOS/Web 尽量使用系统熟悉元素；Android/Windows/Linux 更碎片化，Exact 通过自研 Ink 渲染器接管更多像素绘制。
- 🕹️ **更多能力**：包含面向智能体的游戏引擎，支持 Metal/Vulkan/WebGPU、TUI，并提供 API 与无障碍元数据方便智能体使用应用。
- 🧪 **试用状态**：iOS 最成熟，Web 和 macOS 较好，Android/Windows/Linux 可用但较不成熟；仓库为 github.com/expo/exact，模板为 github.com/expo/exact-templates。
- 📜 **发布与生态**：目前是 pre-alpha，采用 MIT License；Expo 框架与公司仍会持续支持，Exact 将接入 Expo 云服务；鼓励反馈问题并让智能体提交使用日记。

---

### [Expo Exact 初印象：一个由 Rust 驱动的新应用运行时 | React Native 周刊](https://rnw.kazutoyo.jp/en/posts/expo-exact-first-impression/)

**原文标题**: [First Impressions of Expo Exact, a New Rust-Powered App Runtime | React Native Weekly](https://rnw.kazutoyo.jp/en/posts/expo-exact-first-impression/)

概述总结
作者试用了 Expo 推出的全新跨平台应用运行时 Exact（Rust 驱动、预 1.0 版本），并用它重做了一个天气应用，与之前的 SwiftUI 和 React Native (Expo) 版本进行了对比。Exact 用声明式语言 Contract 描述 UI 和状态，编译成 plan 后，在原生平台由 Rust runner、Taffy 布局内核和 Swift host（UIKit/AppKit）渲染，在 Web 端则由小型 JS runtime 直接操作 DOM，两者都不使用 WebView。文章详细记录了架构、TypeScript 数据模块、内置 agent 命令与冻结时钟测试、包体积与启动时间数据，以及早期阶段的粗糙之处，整体评价相当积极。

- 🧭 **定位**：Exact 是 Expo 发布的新跨平台运行时，可“写一次，在 web、macOS、iOS、Linux 原生运行”，Android/Windows 尚未完善，项目处于 pre-1.0、几乎每天更新
- 🏗️ **架构**：UI 用小型声明式语言 Contract 编写，构建时编译为 plan；原生端由 Rust runner 执行、Taffy 布局内核计算、Swift host 用 UIKit/AppKit 绘制；Web 端用约 20KB 的 JS runtime 驱动真实 DOM
- 🔌 **数据层**：Contract 不能做网络或文件 I/O，数据模块用 TypeScript（或 Rust）编写，通过 `grants` 限定可访问的 URL 与文件，返回值在运行时按 shape 校验
- 📱 **实战规模**：整个天气应用仅 `app.contract`（356 行）+ `app.ts`（126 行）+ 38 行测试，即产出 iOS、macOS、Web 三端构建
- 🤖 **Agent 友好**：内置 `tree`、`screenshot`、`tap`、`type`、`state`、`clock` 等命令，三端行为一致，用 Claude Code 基本可端到端完成开发
- ⏱️ **冻结时钟**：`clock` 把时间交给 agent 控制，测试无需 `sleep`，不会因时序抖动，还能跨三端录制帧同步视频
- 🧪 **自动验证**：`verify` 会复访测试触达的每个界面，检查明暗模式、不同宽度和最大字号下的对比度与文字溢出并给出修复建议
- 💬 **友好报错**：编译错误不仅指出问题，还会给出应写的声明，例如提示“`submit=search` … declare `action search`”
- 📦 **体积**：Exact 应用 IPA 11.7MB / 解压 24.5MB，约为 Expo（19MB / 56.6MB）的一半，而 SwiftUI 仅 0.25MB / 1.1MB；应用自身代码仅约 60KB
- ⚡ **启动**：到首屏 SwiftUI 333ms、Exact 350ms、Expo 333ms，三者相差约一帧；到天气加载完成分别为 917ms、1000ms、1017ms
- ⚠️ **粗糙之处**：部分平台细节缺失（SF Symbols 仅限 Apple、图标尺寸由宽度决定）、测试无法 stub 网络、Web 初始 `app.js` 343KB、首次配置有摩擦
- 🔮 **结论**：把“逻辑独立于 UI”和“agent 可操作可验证”内建进运行时是 Exact 最大亮点，虽仍早期，但完成度令人意外，值得持续关注

---

### [Expo 的 CEO 刚刚打造了一个 React Native 替代方案 - YouTube](https://www.youtube.com/watch?v=l738pHcezds)

**原文标题**: [Expo's CEO Just Built a React Native Alternative - YouTube](https://www.youtube.com/watch?v=l738pHcezds)

该内容为 YouTube 页脚导航与版权信息汇总，涵盖平台介绍、联系渠道、创作者/广告/开发者资源、法律政策及功能说明等链接。

- ℹ️ 提供“关于”“新闻”“版权”“联系我们”等基础信息入口
- 👥 面向创作者、广告主和开发者提供相关入口
- 📜 包含条款、隐私、政策与安全等法律与规范链接
- 🛠️ 提供“YouTube 如何运作”和“测试新功能”入口
- ©️ 版权声明标注为 © 2026 Google LLC

---

### [我们如何在12周内重建 Shopify 应用（2026） - Shopify](https://shopify.engineering/shopify-app-rebuild)

**原文标题**: [How we rebuilt the Shopify app in 12 weeks (2026) - Shopify](https://shopify.engineering/shopify-app-rebuild)

Shopify 用约30名工程师在12周内将300+屏幕的移动应用从 React Native 重建为 Swift/Kotlin 原生应用，大部分实现代码由 AI 代理编写；核心经验是围绕代理重构架构、工具链、测试反馈、评审与协作流程，而非单纯追求生成速度。

- 🚀 30人、12周完成300+屏幕迁移，覆盖主屏/锁屏小组件、Apple Watch、Siri Shortcuts。
- 🤖 代理承担大部分编码，但人类保留架构、产品行为和最终发布判断；强调“不是 vibe coding”。
- 🧱 先改造系统再迁屏幕：业务逻辑可脱离设备运行、采用 Reflex 架构、CLI 毫秒级加载屏幕、iOS/Android 共享架构、示例与 Architecture.md、仓库护栏。
- ⚡ 快反馈是核心：代理可在终端加载 ViewModel、触发动作、检查状态并运行确定性检查，避免模拟器/截图式慢循环。
- 🧩 组织为两人小组按产品域端到端负责；每对同时驱动多个代理，一个 PR 同时包含 iOS 和 Android 改动，便于对比评审。
- 📏 一致性优先于平台特定惯用写法；CI 会在 iOS/Android 架构漂移时失败，使每个迁移屏幕成为下一个示例。
- 📚 规格驱动开发失败，因规格很快过期；改为把现有 React Native 应用当“活规格”，由 Helix 拆分小 checkpoint 并对照验证。
- 🚦 瓶颈从写代码转向机器、评审、合并和协调；通过远程开发环境、代理初审、小 PR、代理处理 rebase/CI/冲突、按领域 ownership 应对。
- 🔁 自愈循环每15分钟扫描新崩溃，River 在远程环境复现并开修复 PR；每日 review 评论回写 skills 和 Architecture.md。
- 📈 用户侧收益显著：Android 启动时间下降约50%（1.71s→0.87s），iOS 下降14%（0.70s→0.60s）；Android 包体缩小40%（80.4MB→47.6MB）；Android 内存470MB→200MB，iOS 峰值730MB→190MB；Android 崩溃免费会话99.66%→99.98%。
- 🧠 经验包括：前期投资快速测试、让架构可执行、小步收敛、跨平台一致、代理先审人类终审、把评审容量当系统约束、预期瓶颈移动、明确 ownership。
- ✅ 结论：代理会放大环境；产品质量取决于架构、护栏、反馈回路和人类判断，而不是代理生成代码的速度本身。

---

### [Reflex：一种使用智能体构建移动应用的架构（2026）——Shopify](https://shopify.engineering/reflex)

**原文标题**: [Reflex: an architecture for building mobile apps with agents (2026) - Shopify](https://shopify.engineering/reflex)

Reflex 是 Shopify 提出的一种移动应用架构，目标是让 AI 代理在没有模拟器/仿真器的情况下直接驱动、测试和探索原生 iOS 与 Android 应用。它通过分离 Core 与 UI、统一 ViewModel 契约、JSON 内省节点和跨平台 CLI，实现极快的反馈循环，并用“共享测试而非共享代码”的方式保持双端同步。

- 🧠 **核心问题**：代理写界面很快，但验证界面需要构建、模拟器、点击脚本和等待，反馈循环成为最大瓶颈。
- 🏗️ **四大支柱**：无 UI 的 Core 模块、严格的 ViewModel 契约、ViewModel 内省、平台无关 CLI。
- 📦 **模块拆分**：Core 包含 ViewModel、导航、服务、GraphQL、持久化等逻辑，不依赖 UIKit 或 Android；Mobile 负责 SwiftUI/Compose、Keychain、推送、相机等平台能力。
- 🔁 **ViewModel 形状**：采用 Elm 风格，`Action` 输入、`State` 输出，所有状态变化集中在一个 `update(state, message)` 中。
- 🔍 **Introspection Kit**：每个 ViewModel 暴露一个 JSON 节点，包含屏幕名、状态、可执行动作和子节点；CLI 只通过这一层与应用交互。
- 🌳 **节点树与焦点**：应用根节点、导航器、屏幕 ViewModel 组成树；CLI 聚焦最深节点，容器可向下传递 `goBack`、`selectTab` 等动作。
- 🧪 **共享测试，不共享代码**：iOS 用 Swift、Android 用 Kotlin，各自原生实现；行为测试只写一份，同时跑双端，PR 不能只在单端通过。
- 🏆 **测试奖杯**：少量单元测试、大量 CLI 行为测试、少量真实集成与性能测试；1,700+ 行为测试约 4 分钟跑完双端。
- ⚡ **无渲染、无设备依赖**：测试直接读写 ViewModel 状态和动作，不经过布局、动画或真实 UI，因此更快、更稳定。
- 🔒 **强制无网络**：行为测试会阻止 HTTP 请求，所有网络和外部依赖都必须用 fixture，保证确定性和低 flakiness。
- 🤖 **Agentic-first**：同一套状态与动作接口不仅供 CLI 和测试使用，也供 Shopify 的 AI 助手 Sidekick 在应用内执行操作。
- 🧩 **落地要点**：Core 去除 UI 依赖、统一 ViewModel、添加内省节点、构建节点树、任何网络请求都失败、为代理写技能而非文档、去掉面向人的复杂交互。
- 📖 **开源态度**：文章本身就是“开源”；真正可迁移的是架构，而不是 Shopify 内部的 Introspection Kit 代码，代理可根据文章为你的代码库实现。

---

### [在 Swift 和 Kotlin 中尝试 Shopify 的 Reflex 架构 | React Native 周刊](https://rnw.kazutoyo.jp/en/posts/reflex-native-swift-kotlin/)

**原文标题**: [Trying Shopify's Reflex Architecture in Swift and Kotlin | React Native Weekly](https://rnw.kazutoyo.jp/en/posts/reflex-native-swift-kotlin/)

文章介绍 Shopify 从 React Native 回归原生开发后推出的 Reflex 架构，并记录作者用 Swift、Kotlin 和 TypeScript 复刻该方案的实践。Reflex 通过无 UI 的 Core、跨平台共享行为测试和 CLI 驱动，让两套原生实现保持行为一致，并便于编码代理测试和操作应用。

- 🧱 Reflex 是基于 MVVM 的移动应用架构，不是现成库，博客文章本身即规范；核心目标是让代理无需模拟器即可测试应用，并用一套测试同步 iOS 与 Android。
- 🔁 Shopify 于 2020 年转向 React Native，2026 年又回归原生 Swift/Kotlin；主要原因是编码代理降低了双端实现成本，但“每个界面写两遍”的同步问题仍需解决。
- 🧪 核心理念是“共享测试，而非共享代码”：Core 分别用 Swift 和 Kotlin 实现，行为测试只用 TypeScript 编写一次，通过 Bun 同时跑双端；CI 中 1700+ 测试约 4 分钟完成。
- 🚫 测试规则严格：阻断所有 HTTP，任何联网尝试都失败；设备状态和 API 响应作为 fixtures 传入构造函数；不使用 mocking 框架。
- 🧠 Core 与 UI 完全解耦：iOS 为纯 Swift package，Android 为纯 JVM module，不依赖 UIKit、SwiftUI 或 `android.*`；ViewModel、服务和导航状态都在 Core 中，平台能力通过协议/接口注入，无 DI 框架。
- 🔄 ViewModel 采用 Elm 架构：外部 `send(action:)` 和服务结果都转为内部消息，交给 `update(state, message)`；`update` 是唯一修改状态的地方，View 只负责读取状态并发送动作。
- 🔍 Reflex 的 Introspection 暴露 `name`、`state`、`actions`、`child`，CLI 通过 `ls` 查看当前屏幕、通过 `do Action [json]` 执行动作；作者用 `AppRoot.focused` 替代 `child` 来定位当前屏幕。
- 📱 示例天气应用包含当前天气、城市搜索和收藏三个标签页，共 21 个 TypeScript 行为测试；iOS 用 SwiftUI，Android 用 Jetpack Compose，CLI 分别运行于 macOS 和 JVM。
- 🧩 双端 ViewModel 形状固定，第二版实现接近机械翻译；状态 JSON 需保持一致：联合类型用 `status` 标记，`null` 始终显式写出。
- 🧭 导航逻辑也放在 Core：`AppRoot` 管理选中标签和各标签页栈；`send` 等待异步副作用完成，因此 `do` 返回的是稳定后的状态，测试无需 sleep 或轮询。
- 🖥️ CLI 协议支持 `launch`、`do`、`env`、`open` 等命令；调试版应用通过本地 socket 接收相同 NDJSON 命令，可快速切换天气、离线等场景，便于人工检查和代理操作。
- 🛠️ 无头测试全部通过后，设备运行仍暴露定位超时、SwiftUI 加载背景异常、Android 协程取消被误报等问题；这些属于平台集成与外观问题，而非 Core 缺陷。
- ⚖️ 作者结论：共享测试同步两套实现非常有效；但原生方案代码量约为跨平台两倍，UI 一致性仍需额外验证。可先用 React Native，后续迁移原生，并用同一套测试降低迁移风险。

---

### [Discord 正在离开 React Native。这次不一样。 - YouTube](https://www.youtube.com/watch?v=XpEMvOXQ1Wo)

**原文标题**: [Discord Is Leaving React Native. This Time It's Different. - YouTube](https://www.youtube.com/watch?v=XpEMvOXQ1Wo)

该文本主要是 YouTube 页面底部的导航与法律信息，包含平台相关入口、政策条款及版权声明，未涉及具体文章正文内容。

- 🧭 提供“关于、新闻、联系我们”等基础导航入口
- 🎬 包含创作者、广告投放和开发者相关链接
- ⚖️ 列出版权、条款、隐私、政策与安全等法律合规信息
- 🛠️ 提供 YouTube 工作原理及测试新功能入口
- ©️ 版权声明为 © 2026 Google LLC

---

### [修复缓慢结账流程中的 React Native 性能问题 | Sentry](https://sentry.io/cookbook/track-checkout-performance-react-native/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=mobile-fy27q4-cookbook&utm_content=newsletter-rn-link-rn-checkout-trysentry)

**原文标题**: [Fix React Native Performance in a Slow Checkout Flow | Sentry](https://sentry.io/cookbook/track-checkout-performance-react-native/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=mobile-fy27q4-cookbook&utm_content=newsletter-rn-link-rn-checkout-trysentry)

本文介绍了如何通过 Sentry 分布式追踪，在 React Native 前端与 Python 后端之间监控、定位并修复结账流程中的性能瓶颈，并配置告警与仪表盘防止问题回归。整篇教程约需 20–30 分钟，难度为中级，共 9 个步骤。

- 🎯 目标：串联 React Native 应用与 Python 后端追踪，找出结账流程中的慢 HTTP 请求并修复。
- ⚙️ 第一步：在 React Native 中启用追踪，设置 `tracesSampleRate > 0`，并将后端 URL 加入 `tracePropagationTargets`。
- 📱 第二步：使用 React Navigation 集成自动追踪 TTID，并通过 `Sentry.TimeToFullDisplay` 记录 TTFD。
- 🧩 第三步：用 `Sentry.startSpan` 为商品目录加载、结账处理等关键操作创建自定义 span，并添加可筛选属性。
- 📊 第四步：在 Mobile Insights 和 Mobile Vitals 中查看平均显示时间、冷启动、TTID、TTFD 与交易耗时。
- 🔍 第五步：进入慢交易详情，通过 Transaction Summary 瀑布图定位耗时最长的 HTTP 请求或自定义 span。
- 🧭 第六步：在 Trace Explorer 中搜索导航 span、查看完整链路，并按属性分组、对比 P50/P95 耗时。
- 🛠️ 第七步：优化慢后端接口后重新部署，回到 Trace Explorer 对比优化前后的 span 耗时。
- 🚨 第八步：从 Trace Explorer 保存查询为告警，设置如平均 span 耗时超过 1 秒的阈值，并配置邮件或 Slack 通知。
- 📈 第九步：在 Dashboard 中添加 Spans 数据集组件，使用 `avg(span.duration)` 和 `span.op:checkout.process` 展示结账处理时间。
- 💡 建议：为自定义 span 添加购物车金额、商品数量等属性；开发环境可用 `1.0` 采样率，生产环境再降低。
- ⚠️ 注意：遗漏 `tracePropagationTargets` 会导致前后端链路断开；TTFD 需将 `record` 置为 `true` 才会记录。
- 🧠 关键概念：TTID 是首帧显示时间，TTFD 是内容完全加载时间；span 是追踪中的最小工作单元，trace 是完整操作的 span 集合。
- 🔔 补充：前后端都需安装 Sentry SDK 并启用追踪；Trace Explorer 可直接保存为告警或仪表盘组件。

---

### [深入探索 Expo Modules 2.0 中全新的 JNI 层](https://expo.dev/blog/expo-modules-2-0-new-jni-layer)

**原文标题**: [Inside the new JNI layer in Expo Modules 2.0](https://expo.dev/blog/expo-modules-2-0-new-jni-layer)

尚未收到需要总结的文章正文，暂时无法提取关键信息与核心要点。请补充原文内容，我将按指定格式生成中文摘要。

- 📄 当前输入为空，缺少可总结的文章内容。
- 📝 请粘贴原文，以便提炼核心要点。
- ✅ 收到内容后，我会用“- + 表情符号 + 要点”的格式输出。

---

### [React Native 与 Swift 和 Kotlin：我们如何选择技术栈](https://swmansion.com/blog/react-native-vs-native/)

**原文标题**: [React Native vs Swift and Kotlin: How We Choose the Stack](https://swmansion.com/blog/react-native-vs-native/)

这篇文章的核心观点是：React Native、原生开发或混合方案并没有绝对优劣，选择应基于产品功能、发布节奏、性能需求、增长方向和团队维护能力；Gobi 的案例说明，当原生模块与桥接维护成本持续上升时，可以分阶段从 React Native 迁移到原生，而多数应用仍适合以 React Native 为基础，仅在关键功能上引入原生能力。

- 🧭 技术栈选择不是一次性决定，应随产品阶段、性能要求、预算和团队能力动态调整。
- ❓ 选型前重点回答五个问题：要交付什么及时间、当前应用瓶颈、核心功能复杂度、产品未来方向、现有代码与维护团队。
- 📱 React Native 作为基础方案：共享 UI 和逻辑，生态成熟，配合 Expo/EAS 可加快构建、分发和热更新，适合双端共性高的产品。
- 🧩 React Native + 原生模块：适合地图、媒体处理、复杂手势等特定功能，用原生补齐性能或平台能力，其余部分继续共享。
- 🛠️ 完全原生开发：适合大量复杂交互、深度平台集成、重数据处理和需要全面控制渲染、并发与动画的产品。
- 🗺️ Gobi 起初使用 React Native，但地图、拖拽、滚动、键盘和导航等交互存在性能问题，团队先通过原生 Bottom Sheet 和原生地图模块做针对性优化。
- 🔁 随着原生模块增多，桥接层、共享状态和双端行为一致性维护成本上升，Gobi 最终选择分阶段迁移到 Swift 和 Kotlin。
- 🏝️ 迁移过程中采用“React islands”策略：原生容器逐步接管导航和页面，旧 React Native 视图保留到原生替代完成，再移除 React 运行时。
- ✅ 并非所有应用都需要迁移：Filament 保留 React Native 并加入原生富文本和通知处理；SeaPeople 的问题并非技术栈导致，在 React Native 内修复后显著降低 CPU 占用并提升稳定性。
- 🤖 Vibecode 则采用原生 SwiftUI 宿主并嵌入 React Native，把运行时加载用户生成应用作为产品能力本身。
- 📌 决策建议：需要共享 UI/逻辑和快速迭代时选 React Native；特定功能需要原生能力时加原生集成；大量核心体验依赖平台控制时考虑全原生；确需迁移时优先渐进式推进。

---

### [如何加速你的 Maestro 测试 | Maestro](https://maestro.dev/blog/speed-up-maestro-tests)

**原文标题**: [How to Speed Up Your Maestro Tests | Maestro](https://maestro.dev/blog/speed-up-maestro-tests)

本文介绍如何在不牺牲覆盖率和可靠性的前提下，定位并优化 Maestro 测试套件的性能瓶颈，核心思路是减少重复操作、跳过不必要步骤，并利用 Maestro Cloud 并行执行。
- 🚫 **禁用动画**：动画会拖慢等待稳定状态的步骤；Maestro Cloud 默认禁用，也可通过 `disableAnimations: true` 显式设置，本地 Android/iOS 可用命令关闭。
- ⚡ **加快滚动**：`scrollUntilVisible` 的 `speed` 范围为 0–100，默认 40；确认目标在底部时可调高，但 100 在 Android 模拟器上可能误触为点击。
- 🔗 **用深链接直达页面**：通过 `openLink` 直接跳转到待测页面，再用 `assertVisible` 验证位置，避免重复点击导航；同时保留少量真实导航流程以确保覆盖。
- 🔐 **预填登录信息**：为登录页添加可接收邮箱和密码的深链接，让应用自动填充，减少每个流程开头逐字输入的时间；仅用于测试构建，并保留真实登录流程。
- 🎟️ **跳过登录页**：用 `runScript` 通过 HTTP 获取认证 token，再作为启动参数传给应用，让应用直接以已登录状态启动；仍需保留至少一个真实登录流程。
- ☁️ **并行运行测试套件**：使用 `maestro cloud --app-file app.apk --flows .maestro/` 在 Maestro Cloud 多设备并行执行；40 个各 90 秒的流程从约 1 小时缩短到约 6 分钟。
- 🧩 **保持流程独立**：为最大化并行收益，各流程应独立、幂等，能在干净设备上使用自己的测试数据运行，不依赖其他流程状态。
- ✅ **结论**：最大收益来自消除重复工作——禁用动画、加速滚动、深链接跳过导航、避免不必要登录，并在 Maestro Cloud 上并行执行独立流程。

---

### [React Native OTA 更新：安全发布的最佳实践 - Bitrise 博客](https://bitrise.io/blog/post/react-native-ota-updates-best-practices?utm_campaign=cp_promotion_2026-sponsorships_all_2026-09-09&utm_source=thisweekinreact&utm_medium=newsletter-1-20261111)

**原文标题**: [React Native OTA updates: best practices for shipping safely - Bitrise Blog](https://bitrise.io/blog/post/react-native-ota-updates-best-practices?utm_campaign=cp_promotion_2026-sponsorships_all_2026-09-09&utm_source=thisweekinreact&utm_medium=newsletter-1-20261111)

overview summary
本文系统讲解 React Native OTA 更新的安全发布实践：先确定 OTA 使用策略，再精准匹配兼容版本、选择安装方式、建立渠道与自动化、渐进发布并持续监控，同时做好回滚/前滚、签名审计和包体积优化，最后给出发布检查清单。

- 🎯 明确 OTA 策略：可按“仅热修复”“商店版本间增量发布”“持续部署 JS 变更”三档权衡复杂度和发布频率。
- 📱 精准定位版本：每条 OTA 更新应限定兼容的原生 App 版本，使用 semver，优先指定明确版本，避免无上限开放范围导致未来版本崩溃。
- 🔍 版本读取注意：CodePush 在 iOS 读取 CFBundleShortVersionString，在 Android 读取 PackageInfo.versionName，而非 versionCode；非 semver 可用 overrideAppVersion 覆盖。
- ⚙️ 安装模式取舍：默认后台下载、下次启动生效；立即安装只用于关键修复，且要清晰提示用户，绝不能因检查/下载更新阻塞 App 启动。
- 🚦 建立部署渠道：为调试、QA、PR 预览和生产建立独立渠道；生产发布仅允许从 CI 等受控、可审计环境进行。
- 📈 渐进式发布：先小比例用户，再按 5%、25%、50%、100% 逐步扩大；每一步观察崩溃率、OTA 更新与回滚指标，并预先设定暂停/停止条件。
- 🛰️ 全面监控：把 OTA 错误接入现有崩溃上报工具，并将更新生命周期事件记录为面包屑，便于定位崩溃时更新流程状态。
- ↩️ 回滚与前滚：出现严重问题时可选择回滚或前滚；能前滚优先前滚以减少清理成本，同时注意数据库 schema 等状态变更可能使回滚不可行。
- 🔐 安全与审计：对 OTA 更新进行代码签名，像保护原生签名证书一样保护私钥；保留发布和部署变更审计日志。
- 📦 优化更新包：启用 delta 更新，仅下载变更内容；二进制 diff 可显著减小包体积，降低用户流量和传输成本。
- ✅ 发布检查清单：确定 OTA 用途、使用 semver 明确目标版本、默认静默安装、不阻塞启动、生产仅 CI 发布、小比例渐进发布、监控指标、优先前滚、签名并保护密钥。
- 🚀 Bitrise CodePush：提供分阶段发布、一键回滚、delta 更新和代码签名，所有套餐均包含，每月最多 10 万活跃用户免费。

---

### [发布 v0.19.0 · googlemaps/react-native-navigation-sdk · GitHub](https://github.com/googlemaps/react-native-navigation-sdk/releases/tag/v0.19.0)

**原文标题**: [Release v0.19.0 · googlemaps/react-native-navigation-sdk · GitHub](https://github.com/googlemaps/react-native-navigation-sdk/releases/tag/v0.19.0)

该内容为 googlemaps/react-native-navigation-sdk 的 v0.19.0 版本发布说明，重点包含破坏性变更、平台 SDK 升级及迁移注意事项。

- 📦 v0.19.0 为最新版本，发布说明标注日期为 2026-11-05。
- 📱 iOS 最低版本要求提升至 17.0，以适配 iOS Navigation SDK 11.3.0。
- ⚠️ iOS 上重复航点将返回 `RouteStatus.DUPLICATE_WAYPOINTS_ERROR`，不再返回 `RouteStatus.UNKNOWN`；设置 `routeTokenOptions` 时不会向 SDK 发送航点。
- 🧹 两个平台均移除 `DisplayOptions.showStopSigns` 和 `showTrafficLights`，同时从目的地选项中移除这些字段。
- 🆕 新增对 `RouteStatus.ROUTING_TIMEOUT` 结果的处理。
- 🗺️ Android 地形地图在导航期间将回退为普通地图。
- ⬆️ Android Navigation SDK 升级至 8.0.0（#688）。
- ⬆️ iOS Navigation SDK 升级至 11.3.0（#697）。
- 📘 升级说明和构建要求需参阅 `MIGRATING.md`。

---

### [Version 1.23 — precise input tracking, fewer preload artifacts, and transparent KeyboardExtender 🎯 | Keyboard Controller](https://kirillzyusko.github.io/react-native-keyboard-controller/blog/release-1-23)

**原文标题**: [Version 1.23 — precise input tracking, fewer preload artifacts, and transparent KeyboardExtender 🎯 | Keyboard Controller](https://kirillzyusko.github.io/react-native-keyboard-controller/blog/release-1-23)

1.23.0 是一个小版本更新，重点提升键盘相关组件的精确性、减少预加载视觉残留，并让 KeyboardExtender 支持透明背景。

- 🎯 KeyboardAwareScrollView 现在更精确地跟踪聚焦输入框的光标位置，iOS 会报告与 Android 类似的几何信息，跨平台表现更一致。
- 📏 修复了 iOS 单行 TextInput 的光标位置忽略 paddingTop 的问题，避免滚动过早结束、文本可能被键盘遮挡；此前用更大 bottomOffset 补偿的开发者现在可尝试调小。
- 🧹 修复了 KeyboardProvider 在 iOS 默认预加载键盘时可能出现的闪烁和视觉残留，例如从 Spotlight 启动且 Spotlight 键盘仍打开时键盘闪过首屏。
- 🔄 如果曾因预加载问题禁用 preload 或手动调用 KeyboardController.preload()，建议重新尝试默认行为。
- ⬜ KeyboardExtender 新增 transparent 属性，可移除默认的键盘样式容器，让内容自行绘制表面，适合单个“Done”胶囊或类似 WhatsApp 的按钮行。
- 📱 transparent 在 iOS 26+ 会跳过玻璃胶囊，iOS <26 不绘制键盘背景，Android 跳过键盘背景视图；默认值为 false，不影响现有用法，并支持运行时切换。
- 🤝 该属性由 kylesuss 提议并实现（#1714）。
- 🐞 作者表示会优先处理高 👍 的 issue，带“sponsor 💖”标签的 issue 获得最高优先级，并会持续开发新功能、在 Twitter 发布预览。

---

### [react-native-gesture-handler 3.5.0](https://swmansion.com/changelog/react-native-gesture-handler-3-5-0/)

**原文标题**: [react-native-gesture-handler 3.5.0](https://swmansion.com/changelog/react-native-gesture-handler-3-5-0/)

react-native-gesture-handler 3.5.0 是 2026 年 11 月 5 日发布的小版本更新，核心是为 v3 手势新增 Begin、Deactivate、Finalize 事件类型，并集中修复 iOS、Android、Web 上按钮、Pan 速度、Pressable、ReanimatedSwipeable、ReanimatedDrawerLayout、指针处理和 Jest 配置等问题；同时更新文档与依赖，并新增 6 位贡献者。

- 🆕 为 v3 手势新增 Begin、Deactivate、Finalize 事件类型（#4668）。
- 🐛 修复 iOS 按钮子元素挂载顺序、StatefulPressable 缺失 onPressOut、无障碍标签推断及 Manual 手势触摸延迟。
- ↩️ 修复取消后的 ReanimatedSwipeable 与 ReanimatedDrawerLayout 平移回滚。
- 🖱️ 修复 Web/iOS 指针静止后释放时 Pan 速度应为 0，并改进 Web 悬停与越界移动处理。
- 📱 修复 Android/Web 仅检查同一指针的处理器，以及 Android Pressable 长按计时、手势等待和原生触摸清理。
- 🧩 修复替换已挂载手势时 Reanimated 订阅问题，并调整 JS responder 事件标记。
- 📚 文档补充视图重排导致手势取消的说明，并修正 ReanimatedSwipeable 示例操作区域。
- 🧹 移除 disableReanimated 属性、为 Jest 的 GestureHandlerRootView 检查增加退出选项，并清理未用监听器。
- 📦 更新兼容表与 Expo SDK 58，升级多项文档/开发依赖，避免 Reanimated 深层导入进入 Web 包。
- 👏 新增 @chocky335、@collectioneur、@RaphaelFakhri、@Elehiggle、@mkantautas、@huamurui 六位贡献者。
- 🔗 完整变更日志：v3.4.0...v3.5.0。

---

### [发布 v11.0.0 · oblador/react-native-keychain · GitHub](https://github.com/oblador/react-native-keychain/releases/tag/v11.0.0)

**原文标题**: [Release v11.0.0 · oblador/react-native-keychain · GitHub](https://github.com/oblador/react-native-keychain/releases/tag/v11.0.0)

react-native-keychain v11.0.0 发布，主要迁移到 TurboModules 和新架构，加入 Swift Package Manager 集成预览与互联网凭证服务器列表能力，并修复凭证作用域和认证行为问题。

- 🚀 核心升级：迁移至 TurboModules 和新架构，新增 SPM 集成预览及互联网凭证服务器列表功能。
- ⚠️ 破坏性变更：要求 React Native 0.82+、React 19.1.1+，不再支持旧架构。
- 🛠️ 环境要求：Node.js 20.19.4+、Android API 24+，iOS 最低 15.1，应用可按需使用更高目标版本。
- 🔑 API 调整：`hasInternetCredentials` 改为接收选项对象，例如 `{ server: 'https://example.com' }`。
- 🍎 iOS 行为：`cloudSync` 省略或为 `false` 时仅选择非同步项，`true` 选择同步项，读写/检查/重置需保持一致。
- 📘 类型改进：TypeScript 结果类型更准确反映原生响应，包括 iOS `storage: 'keychain'`、服务器/服务字段及布尔返回值。
- 📦 安装方式：安装 `react-native-keychain@11.0.0`，更新原生依赖并重新构建应用。
- 🧩 新功能：iOS 支持 React Native 0.88+ 实验性 SPM 自动链接预览，CocoaPods 仍受支持，不支持直接将仓库添加为 Xcode 包。
- 🌐 服务器列表：`getAllInternetCredentialServers()` 可列出不同服务器且不返回用户名或密码；Android 默认排除旧条目，可用 `includeLegacy: true` 包含。
- 🧯 错误处理：新增 `ERROR_CODE` 常量，便于处理原生错误而无需解析本地化消息。
- 🐞 修复内容：Android 凭证枚举与认证策略保留、弱生物识别提示、DataStore RELRO 对齐、iOS 同步/非同步凭证隔离、认证提示选项规范化等。
- 📚 文档与测试：新增深色 VitePress 文档、升级与存储指引、刷新示例应用，并拆分原生存储/查询回归测试与 Detox 流程测试。

---

### [更新日志 | 屏幕过渡](https://screen-transitions.esjr.org/changelog/)

**原文标题**: [Changelog | Screen Transitions](https://screen-transitions.esjr.org/changelog/)

该内容为项目更新日志，汇总最新公告、Version 4 当前发布线的功能与迁移说明，以及 Version 3 的维护修复记录。

- 📌 最新更新与公告集中在 Version 4，当前发布线包含新能力与迁移注意事项。
- 🚀 Version 4.2（2026年11月）支持 Expo SDK 58，Expo Router 集成不再处于 Alpha。
- 🧭 Version 4.1（2026年11月）优化快速输入下的 push/pop 与手势流畅度，加入内置裁剪、公开 motion providers、命名转场和 native-stack 静态配置。
- 🧱 Version 4.0（2026年8月）引入基于步骤的 sheet 手势、显式 handoff 所有权、更强全局边界协调，并缩小公共 API。
- 🛠️ Version 3 仅继续提供修复补丁，不再增加新功能。
- 🔄 Version 3.13 让 Boundary 转场更可预测，并减少深层保留栈中的动画开销。
- 🪟 Version 3.12 为浮动 overlay 提供独立栈，屏幕插值器可动画它们而无需重建 transition provider 树。
- 🐞 Version 3.11.3 修复分组 Boundary 重定向、长列表中的逃逸源及 dismissal 生命周期冲突。
- 📐 Version 3.11.1 修复复杂路由布局中的边界配对与 escape-clipping 可靠性。
- ⏱️ Version 3.11 收紧转场生命周期时序，改进变换 Boundary 测量，并提升实时 handoff 可靠性。
- 🧩 Version 3.10 提升 Boundary handoff、escape clipping、导航缩放与手势驱动转场的可靠性，并降低挂载开销。
- 📏 Version 3.9 使 bounds 测量更确定，改进重定向，引入简化 Boundary API 和 contentComponent。
- ✨ Version 3.8 简化手势进度、默认手势重置、transitionProgress、bounds 进度与手势 handoff。
- 🧵 Version 3.7 覆盖 native-stack 集成、blank-stack 生命周期、reveal、transition scopes 与嵌套手势正确性。
- 🔧 Version 3.6 涉及手势、snap points、bounds、reveal 与迁移兼容性。
- 🧳 Version 3.4 帮助旧设置迁移到 3.4 时代的分层转场表面。

---

### [8.34.0 版本 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.34.0)

**原文标题**: [Release 8.34.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.34.0)

sentry-react-native 8.34.0 已发布，重点增强性能分析与 JS 线程监控：Android 15+ 可将 Hermes JS 样本纳入原生性能分析，iOS 新增实验性 JS 卡顿错误上报，并新增 JS 长任务指标集成；同时修复 Expo Router fetch 检测、Android 原生日志、iOS 截图遮罩等问题，并升级相关 SDK 依赖。

- 🚀 Android 15+ 性能分析支持加入 JavaScript（Hermes）样本：启用 `_experiments.profilingOptions` 后，Hermes 样本会作为原生 profiler 会话的 profile 分块发送，使事务性能分析中可展示 JS 函数。
- ⚠️ iOS 新增实验性 `enableJsHangTracking`：当 JS 线程阻塞超过 `jsHangTimeoutInterval`（默认 2 秒）时上报错误；Hermes 下包含 JS 堆栈和 bundle Debug ID，便于 source map 符号化；开发构建中不运行。
- 📊 新增 `longTaskIntegration`：将 JS 长任务以 `react_native.long_task.duration` 指标上报，也支持事务外上报；需 React Native 0.82+ 新架构，可配置 `minDurationMs`（默认 200）和 `sampleRate`（默认 1）。
- 🛠️ 修复 Expo Router 应用中的 `expo/fetch` 检测：即使 `@expo/metro-runtime` 版本隐藏该能力，也能默认启用 fetch 追踪和 fetch 面包屑。
- 📝 修复 Android 在设置 `enableLogs` 时启用原生日志；修复 iOS 错误截图遵循 `<Sentry.Mask>`。
- ⬆️ 依赖升级：JavaScript SDK 从 v10.77.1 升至 v10.78.0，Cocoa SDK 从 v9.32.0 升至 v9.33.0。
- 📦 8.34.0 为最新版本，由 sentry-release-bot 于 11 月 5 日发布。

---

### [发布 v3.10.0 · wcandillon/react-native-skia · GitHub](https://github.com/wcandillon/react-native-skia/releases/tag/v3.10.0)

**原文标题**: [Release v3.10.0 · wcandillon/react-native-skia · GitHub](https://github.com/wcandillon/react-native-skia/releases/tag/v3.10.0)

React Native Skia 发布 v3.10.0（2026-11-10），主要包含 Skia 升级、macOS 兼容性修复、新增绘图能力、Graphite 状态暴露，以及多项渲染性能优化。

- 🚀 版本更新：发布 v3.10.0，为当前最新版本，包含自上一版本以来的 5 个提交。
- ⬆️ 底层升级：更新至 Skia m158。
- 🍎 macOS 修复：在 macOS 上针对 react-native-macos 的 API 构建 react-native-svg，修复 #4405。
- 🐙 文本修复：首次使用时匹配基准测试文本字体。
- 🖼️ TextureView 修复：窗口重新可见时锁定其保留缓冲区，修复 #2135。
- 🔷 新增功能：加入 SkShapeBlob 和 canvas.drawShapes。
- 🧵 Graphite 增强：在 SkGraphiteContext 上暴露 pendingFrames。
- 🎨 性能优化：重放 recorder 命令时避免复制和分配，修复 #4423。
- 🎨 着色器优化：每次重放时不复制 runtime shader 的 uniforms。
- 🏞️ 字体优化：使用设备无关字体记录视图。

---

### [Release Release 4.1.0 · lodev09/react-native-true-sheet · GitHub](https://github.com/lodev09/react-native-true-sheet/releases/tag/v4.1.0)

**原文标题**: [Release Release 4.1.0 · lodev09/react-native-true-sheet · GitHub](https://github.com/lodev09/react-native-true-sheet/releases/tag/v4.1.0)

本次发布为 react-native-true-sheet v4.1.0（11 月 7 日），新增背景模糊功能 dimBlur，并集中修复 iOS、Android 上弹层显示、手势、返回键与键盘联动等问题，同时更新文档、Jest mock 和导航 mock。

- 🎉 新增 `dimBlur`：可模糊 sheet 后方内容，替代仅用 `dimColor` 着色；`dimOpacity` 控制模糊强度。
- 📱 平台表现：iOS 会叠加匹配的材质色调；Android 12 及以上支持模糊，若系统关闭窗口模糊则仅着色。
- 🍎 iOS 修复：sheet 在另一 sheet 上展示后快速关闭时，不再短暂隐藏后方 sheet。
- 🎨 iOS 修复：设置 `backgroundColor` 的 sheet 在特定 Xcode 26 / iOS 27 兼容模式下不再透明。
- 🤖 Android 修复：`draggable={false}` 的 sheet 不再抢占内容区的垂直手势，地图可正常缩放和平移。
- ⬅️ Android 修复：关闭动画期间的返回键可传递到下层 sheet 或导航，不再被正在关闭的 sheet 吞掉。
- 📜 修复 `ScrollView` 中 `TrueSheetPeek` 下拖后无法稳定停在完整 peek detent 的问题。
- ⌨️ Android 修复：键盘消失后 sheet 会无动画回到原 detent，取消隐藏键盘的返回手势也会让 sheet 回到键盘上方。
- 🧪 测试与文档：更新 Jest mock、导航 mock 的 `pop()` / `popTo` 行为，并补充 `dimBlur` 与 iOS 27 相关文档。
- 👏 新贡献者：@VladyslavMartynov10、@MarkusWendorf、@TheInkedEngineer、@idlework 首次参与贡献。

---

### [发布 v0.18.0 · software-mansion-labs/react-native-bottom-sheet · GitHub](https://github.com/software-mansion-labs/react-native-bottom-sheet/releases/tag/v0.18.0)

**原文标题**: [Release v0.18.0 · software-mansion-labs/react-native-bottom-sheet · GitHub](https://github.com/software-mansion-labs/react-native-bottom-sheet/releases/tag/v0.18.0)

React Native Bottom Sheet v0.18.0 发布，重点新增 Web 支持、浮动卡片与 `surfaceStyle`，引入 `lazy`、`settleDuration`，改进吸附体验和无障碍关闭，并修复滚动协调、Android 返回键、iOS 遮罩透明度等问题；同时包含多项迁移变更和最低版本要求。

- 🚀 发布 v0.18.0，处理了 #18、#46、#52、#55、#103，外部贡献者包括 @dkulakov、@falcondpr、@NicholasBoccuzzi。
- 🌐 为 `BottomSheet` 和 `ModalBottomSheet` 增加 Web 支持，使用时需同时安装 `react-dom` 与 `react-native-web`。
- 🃏 新增浮动卡片，可通过每个 detent 的 `insets` 设置左右和底部间隙，间隙随 sheet 移动平滑变化，点击间隙可触达遮罩或内联 sheet 后方视图。
- 🎨 新增 `surfaceStyle` 用于圆角和阴影，sheet 会将背景与内容裁剪到同一轮廓，同时允许阴影外扩；`borderCurve` 仅 iOS，`elevation` 仅 Android。
- ⚡ 两个 sheet 组件新增 `lazy`，默认 `false`，仅在存在关闭 detent 时生效；开启后 sheet 在打开前挂载、关闭动画结束后卸载，动画中重新打开保留状态，完全关闭后重新打开为全新状态，未挂载时不触发 `onPositionChange`。
- ⏱️ 新增 `settleDuration`，接受大于 0 的有限秒数；从静止开始的动画使用完整时长，所有平台默认 `0.45` 秒，Android 从约 `0.2` 秒提升。
- 🧲 改进全平台吸附：轻扫可在越过中点前到达下一 detent，释放前停顿会选择最近 detent，快速滑动会将速度带入动画且不越界。
- ♿ 为 `ModalBottomSheet` 增加无障碍关闭：屏幕阅读器用户可通过 Dismiss 按钮、iOS VoiceOver 退出手势或 Android TalkBack Dismiss 操作直接选择关闭 detent，可用 `scrimAccessibilityLabel` 本地化按钮标签。
- 🗂️ 调整模态堆叠：最近打开或重新打开的 sheet 显示在最上层；`nativeOverlay` sheet 保持在 portal sheet 之上，Android 返回键和 Android/Web 的 Escape 会路由到最上层可用 sheet。
- 🛠️ 修复 Android 系统返回键绕过 portal sheet 的 `onCloseRequest` 问题，避免 Android 10 上 sheet 打开时应用被切到后台。
- 🛠️ 修复 iOS 和 Android 上在垂直滚动区域内侧向或斜向开始拖动的问题，使其遵循 `scrollCoordination`；水平滚动仍处理侧向手势。
- 🛠️ 修复 iOS 拖动反向时的滚动交接、弹跳或下拉刷新清除后同一触摸可移动 sheet、中断吸附但未移动 sheet 时吸附恢复，以及模态 sheet 重新打开时遮罩透明度错误。
- ⚠️ 迁移要求：`0.18.0` 需要 React Native `0.82.0` 或更高、React `19.1.1` 或更高；将 detent 选项移入 `detents`，用 `{ value, programmatic: true }` 替代 `programmatic(value)`，用每个 detent 的 `scrimOpacity` 替代 `scrimOpacities`。
- ⚠️ 其他迁移：`extendUnderStatusBar={true}` 改为 `topInset={0}`；圆角和阴影从 `surface` 移到 `surfaceStyle`；`scrollableNegotiation` 重命名为 `scrollCoordination`，类型名同步改为 `ScrollCoordination` 和 `ScrollCoordinationMode`，`disableScrollableNegotiation={true}` 改为 `scrollCoordination="none"`。

---

### [react-native-audio-api 1.0.0](https://swmansion.com/changelog/react-native-audio-api-1-0-0/)

**原文标题**: [react-native-audio-api 1.0.0](https://swmansion.com/changelog/react-native-audio-api-1-0-0/)

Audio API 1.0.0 是首个稳定版，核心目标是更贴近 Web Audio API 规范、将可选功能移出默认构建，并清理 0.x 期间逐步形成的 API；从 0.13.x 升级需要改代码，空间音频、独立 worklets 包、FFmpeg 可选化和性能优化是主要变化。

- 🔥 1.0.0 于 2026-11-03 发布，为首个稳定版；提供迁移指南，TypeScript 项目可先运行 `tsc` 发现多数升级项。
- ⚠️ FFmpeg 默认关闭：本地文件、资源、`ArrayBuffer`（含 `m4a`、`aac`、`mp4`）改用平台解码；远程 URL 流、HLS 和远程 `getAudioDuration` 仍需 FFmpeg。构建选项迁至 `package.json`，Expo 的 `disableFFmpeg` 改为 `enableFFmpeg`。
- 🧩 Worklets 拆分为 `react-native-audio-worklets`：`WorkletNode` 等改为从新包导入，需 `react-native-worklets` ≥0.10.0 和新架构。
- 🔤 事件处理器改为规范小写名（如 `onEnded`→`onended`、`onPositionChanged`→`onpositionchanged`），无别名；重新赋值会替换旧回调。
- ⚙️ `setAudioSessionOptions` 改为 `setSystemOptions`，iOS 选项放入 `ios` 字段；新增可选 `android` 通信会话配置。
- 🎙 录音器直接连接音频图：`recorder.connect(ctx, ctx.destination)` 替代适配节点；`pause()`、`resume()`、`disableFileOutput()` 返回 Promise 并与 `start()`/`stop()` 串行化；`enableFileOutput` 抛 `NotSupportedError`。
- 🎚 `AudioBufferQueueSourceNode` 引入播放状态机：`pause()` 后应调用 `resume()`，重复 `start()` 抛 `InvalidStateError`；`start(when, offset)` 默认 `offset` 从 `-1` 改为 `0`；`StreamerNode` 移除。
- 📦 不再支持深层导入，需从包根导入；`useAudioInput` 的 `onSelectInput` 改为 `selectInput`，并支持 `'default'`。
- 📱 Android 录音可在 UI 结束后继续（`androidFSStopWithTask: false`）；`setInputDevice` 已实现，含蓝牙 SCO；Android 录制 `Caf` 会抛错，部分类型移除。
- 🧪 规范符合度提升：WPT 断言通过率从 1758/2503（70.2%）升至 2643/3109（85.0%）；`AudioBuffer`、`ChannelMergerNode`、`ChannelSplitterNode`、`GainNode`、`OscillatorNode`、`PeriodicWave` 全部通过。
- 🎧 新增空间音频 `PannerNode`/`AudioListener`、`ChannelMergerNode`/`ChannelSplitterNode`、`baseLatency`/`outputLatency`、`ended` 事件监听，并重写音频图。
- 🎛 Worklets 新包提供 `WorkletAudioContext`、`'frequency-domain'` 模式和通道数回调；录音新增编码层（Opus、ADTS AAC）及 `androidInputPreset`。
- 📱 Android 新增通信会话、输出配置、`latencyHint` 支持，异步 `MediaCodec` 与 WAV 路径加快解码；支持 SPM、React Native 0.88、缓冲状态、`isLiveStream`、`getSystemVolume()`。
- ⚡ 性能：卷积器共享 4 个工作线程且音频线程不等待；缓冲区跨渲染量子复用，上下文线程从 7 个降至 2 个；内存压力按缓冲区上报，音频引擎惰性初始化。
- 🛠 修复 iOS 死锁、释放后使用、语音处理驱动循环、中断后录音恢复，Android 前台服务销毁时录音收尾，以及指数 ramp、`ConvolverNode.buffer` 限制、内存泄漏和通道数协商等问题。
- 📚 文档新增全双工语音 AI 助手指南与示例、版本化文档（`latest`/`next`）及 C++ 引擎内部文档。

---

### [发布 v0.6.0 · callstackincubator/simlock · GitHub](https://github.com/callstackincubator/simlock/releases/tag/v0.6.0)

**原文标题**: [Release v0.6.0 · callstackincubator/simlock · GitHub](https://github.com/callstackincubator/simlock/releases/tag/v0.6.0)

本次发布为 simlock v0.6.0，自上一版本以来共有 104 次提交，主要围绕虚拟设备“种子/基线”机制、租赁流程、安全加固、Android/iOS 驱动重构与问题修复展开，贡献者为 V3RON 和 leonardoxr。

- 🚀 发布 v0.6.0，包含 104 次提交，重点增强虚拟设备复制、基线租赁与系统安全性。
- 🧬 引入“基线/种子”模型：每个虚拟设备都是某个源设备的副本，租约会指定基线并获得其副本。
- 📱 支持从持有的租约保存、列出和删除基线，并在 UI 中新增 Baselines 页面及设备基线展示。
- 🛰️ 网关可将基线租赁请求路由到持有该基线的工作节点，提升分布式调度能力。
- 🔒 安全修复：拒绝不安全的 worker ID、转发前移除代理认证头与 Cookie、限制 SIMLOCK_HOME 仅所有者可访问、校验请求归属。
- 🛡️ 加固网关与输入处理：防止 worker 导致网关崩溃/卡死/损坏，限制输入大小并保证解析线性，转义远程文本控制字符。
- 🤖 Android 改进：模拟器基于种子副本与启动快照启动，限制模拟器标记读取的时间与大小，完善 passthrough 拒绝规则与崩溃报告处理。
- 🍏 iOS 改进：模拟器基于种子副本，支持静音所有模拟器、headless=false 显示窗口，并修复 seed 删除识别问题。
- 🧩 新增 MCP list_devices 能力，可列出已注册手机设备。
- 🧪 大量 Android 驱动重构：拆分为 adb-tools、ownership、console-ports、avd-config、emulator、device-table 等模块。
- 📚 文档与规范：新增多项 ADR，重写面向用户的任务式文档，并加强源码/测试文件行数卫生检查。
- 🐛 其他修复：守护进程停止时返回 DAEMON_STOPPING、CLI 等待守护进程退出、隧道连接清理、屏幕流按身份过期时间结束等。

---

### [发布 v0.32.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.32.0)

**原文标题**: [Release v0.32.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.32.0)

Argent v0.32.0 已发布，是当前最新版本；本次更新涵盖 Android/iOS 工具链、网络检查、安装器、安全转发、文档与兼容性修复，并包含一项破坏性重命名变更。

- 🚀 发布 v0.32.0，包含 20 个提交，汇总多项功能、修复和文档更新。
- ⚙️ 新增 `android.adbServerPort` 配置，可在不使用环境变量的情况下选择 adb 服务器；CLI 提示修改后需重启 tool-server。
- 🔐 新增 `forward-secrets` 标志，支持将客户端密钥转发给关联的 tool-server。
- 📱 iOS 能力增强：支持通过 simulator-server 录制远程 iOS 模拟器，并支持在物理 iPhone 上执行捏合、旋转和多指路径手势。
- 🌐 Android 网络检查器已打包并提供服务；同时修复网络日志指向问题和畸形 `android-` 请求 ID 的处理。
- 🧰 安装器改进：卸载时移除 Devin skill 链接，识别 `pnpm dlx`、`yarn dlx`、`bunx` 安装方式，并清理不再随 Argent 发布的文件。
- 🛠️ 修复 tool-server 与模拟器监控：限制 `simctl` 轮询、回收进程组，并在 Xcode 组件安装待处理时停止或拒绝相关调用。
- 📝 文档与兼容性：新增日文和简体中文 README，支持更名后的 Devin Desktop/Windsurf，并改进 MCP schema 描述兼容性。
- ⚠️ 破坏性变更：重命名剩余 e2e 流程名称，旧名称保留为别名。
- 👏 新增 6 位贡献者；完整变更见 `v0.31.0...v0.32.0`。

---

### [Node.js — Wednesday, November 11, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases)

**原文标题**: [Node.js — Wednesday, November 11, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases)

Node.js 于 2026 年 11 月 11 日发布安全更新，修复 22.x、24.x、26.x 发布线的多个安全漏洞，最高严重级别为 HIGH。受影响用户应尽快升级至 v22.23.5、v24.22.3、v26.13.1，并注意已停止维护（EOL）的版本在安全发布中始终受影响。

- 🛡️ 本次更新覆盖 Node.js 22.x、24.x、26.x，修复多项可导致拒绝服务、内存泄露、认证绕过或进程崩溃的问题。
- ⚠️ 三个发布线中修复的最高严重级别均为 HIGH。
- 📦 安全更新包含依赖更新：llhttp（22.x、24.x、26.x）、undici（24.x、26.x）、sqlite（22.x、24.x）。
- 🚨 高危 HTTP/2 问题：远程未认证客户端可触发断言失败导致服务器中止（CVE-2026-123863），影响 24.x、26.x。
- 🔐 高危 HTTPS 问题：零长度 TLS 写入可重入 llhttp 解析器，造成释放后使用和堆越界读取，可能泄露其他连接内存、TLS 私钥等（CVE-2026-123864）。
- 🧨 高危 HTTP/2 问题：连接关闭期间触发协议错误会导致会话永不清理，持续泄露内存和文件描述符（CVE-2026-123865）。
- 💥 高危 HTTP/2 问题：流拆除时可能将已释放的响应内存发送给对端（CVE-2026-123866）。
- 🧯 高危 TLS 问题：延迟握手回调可被远程触发未捕获异常，导致 TLS 服务器进程终止（CVE-2026-126051）。
- 🕵️ 高危 TLS 1.2 问题：重协商时客户端可单方面更改 servername，绕过按主机名配置的客户端证书认证策略（CVE-2026-123872）。
- 📂 高危 HTTP/2 问题：使用 respondWithFile()/respondWithFD() 时，流在待处理写入期间被重置可导致 Http2Stream 释放后使用（CVE-2026-123874）。
- 🟠 中危 HTTP/2 问题：session.altsvc() 处理长 origin 时存在单字节堆缓冲区溢出（CVE-2026-123828）。
- 🟠 中危 TLS/mTLS 问题：仅 CA 的 SNI 客户端 CA 配置会失败开放到默认 CA，绕过按主机 mTLS 授权（CVE-2026-123867）。
- 🟠 中危 HTTP/2 问题：未排空流上的入站数据不计入会话预算，maxSessionMemory 无法限制内存增长或拒绝新流（CVE-2026-123868）。
- 🟠 中危信息泄露：ERR_PROXY_INVALID_CONFIG 错误消息可能披露代理凭据（CVE-2026-123871）。
- 🟠 中危证书验证问题：https.Agent 因跨策略 TLS 会话复用可绕过证书验证（CVE-2026-123877）。
- 🟠 中危 HTTP/2 问题：取消 respondWithFile() 下载可触发 StreamPipe 空指针解引用并崩溃服务器（CVE-2026-123875）。
- 🟡 低危权限模型问题：递归 fs.watch 可泄露被拒绝访问的后代文件/目录名称（CVE-2026-123829）。
- 🟡 低危 zlib 问题：params() 与 destroy() 组合可能抛出不可捕获的 ERR_INTERNAL_ASSERTION（CVE-2026-123862）。
- 🟡 低危权限模型问题：通配符 --allow-fs-read/--allow-fs-write 规则可能过度授权路径（CVE-2026-106071）。
- 📅 新版本计划于 2026 年 11 月 11 日或之后不久发布，建议使用受支持的最新版本以确保系统安全。
- 🔗 可通过 Node.js 安全策略页面、SECURITY.md 流程及 nodejs-sec 邮件列表获取后续安全信息。

---

### [Mermaid v13：开始瘦身，我们需要你的意见 · mermaid-js · 讨论 #8685 · GitHub](https://github.com/orgs/mermaid-js/discussions/8685)

**原文标题**: [Mermaid v13: going on a diet, and we want your input · mermaid-js · Discussion #8685 · GitHub](https://github.com/orgs/mermaid-js/discussions/8685)

Mermaid 维护者发起 v13 讨论，征集社区在“彻底重写”与“渐进升级 v12”之间作选择。v13 alpha 主打插件化、无 DOM、更小更快，但目前仅支持流程图，尚不适合生产使用；评论者认可无浏览器依赖方向，并集中反馈图表类型、布局质量、插件契约缺口与 alpha 缺陷。

- 🧭 路线未定：v13 全重写与 v12 渐进更新两条路径尚未选择，本次讨论用于辅助决策。
- ⚙️ v13 alpha 亮点：图表类型、布局和可选功能改为插件，按需打包；无需 DOM，可在服务器、worker、CLI 渲染；仅流程图时约 80 KiB，速度提升 100 倍；语法保持不变。
- 🧪 试用与限制：可通过 `npm install mermaid@v13-alpha` 体验，但当前只渲染流程图，且未达生产就绪。
- ❓ 维护者征集反馈：常用图表/功能、可接受 bundle 预算、布局与字体问题（CJK/RTL/emoji）、CSS 变量与 SVG 1.1 工具兼容性、HTML labels 是否可被 Markdown/SVG labels 替代。
- 👤 lex-gsynergy 反馈：既写图也嵌入项目；曾因 Node 测试遭遇浏览器依赖而转向 Graphviz；认为浏览器作库慢且增加攻击面；需求多为简单节点连线、自动布局及半手动行列/嵌套控制。
- 🧱 filipsajdak 反馈：使用 C4、BPMN、swimlane、ELK flowchart 及常见流程图/状态/时序/ER/类图；最重视布局质量，可接受更慢渲染；主要痛点是边路由重叠、穿过标签、箭头堆叠和图表过宽。
- 🧩 插件移植实验：C4、BPMN、swimlane 可在 v13 alpha 的 Node 无 DOM 环境渲染，但发现插件契约四个缺口：不能扩展核心配置/主题变量；`LayoutGraph` 缺 lanes/pools/bands/边方向；legacy 类型替换与 aliases 支持不足；后写主题 paint 未声明导致黑色填充。
- 🐞 alpha 缺陷：提交了 `#8714`–`#8720`，涉及 C4 检测误匹配、front-matter title、ER markdown、courier 字体裁剪、插件懒加载、ELK 挂起、`themeCSS` 被忽略等问题。
- 📬 后续互动：维护者回复 filipsajdak “Check your email”；相关 v12 PR 索引在 `#8713`，社区插件实验仓库为非官方项目。

---

### [2026 年 JavaScript 现状](https://survey.devographics.com/en-US/survey/state-of-js/2026?source=thisweekinreact)

**原文标题**: [State of JavaScript 2026](https://survey.devographics.com/en-US/survey/state-of-js/2026?source=thisweekinreact)

当前提供的文本仅为“Loading...”，尚未包含可总结的文章正文或关键信息，因此无法生成有效摘要。

- ⏳ 内容仍处于加载状态，暂无可提取的文章信息。
- 📄 未提供正文、主题或具体细节，无法进行准确总结。
- 🔄 建议待内容完整加载后重新提交，以便生成有效摘要。

---

### [Node.js — Node.js 26 至 27（Alpha）版本中值得注意的 V8 变更](https://nodejs.org/en/blog/announcements/notable-v8-changes-from-node-js-26-to-27-alpha)

**原文标题**: [Node.js — Notable V8 changes from Node.js 26 to 27 (Alpha)](https://nodejs.org/en/blog/announcements/notable-v8-changes-from-node-js-26-to-27-alpha)

概述总结：Node.js 27 Alpha 将 V8 从 Node.js 26 的 14.6 升级至 15.6，带来默认启用的新 JavaScript 特性、多项语义与行为修正、内存和性能优化，以及 WebAssembly、诊断工具和标志变更；Alpha/Current 阶段可能出现破坏性 V8 更新，涉及原生插件 ABI 时会提升 NODE_MODULE_VERSION，进入 LTS 后 V8 版本预计保持稳定。

- 🚀 V8 升级至 15.6；Alpha/Current 可能引入破坏性变更，ABI 变化会提升 NODE_MODULE_VERSION，LTS 后预计稳定。
- ✨ 默认新增 Math.sumPrecise()，减少浮点累加误差；新增 Intl.Locale.prototype.variants。
- 🔁 新增 Iterator.prototype.join/includes 和 Iterator.zip/zipKeyed 等迭代器方法。
- 🧪 实验特性包括 --js-import-bytes、--js-regexp-buffer-boundaries，并修复 import defer 与 Immutable ArrayBuffer 相关问题。
- 🧮 Math 改用 LLVM libm，部分 Math 方法结果最后一位可能不同；Math.random() 直接运行 xorshift128+，给定 --random-seed 的序列改变。
- 🕰️ Date.prototype.getTimezoneOffset() 不再截断到整分钟，历史日期可返回小数。
- 📊 Array.prototype.sort() 对大数组改用 PowerSort，排序仍稳定，但比较器调用次数或副作用相关测试可能变化。
- 🧱 error.stack getter 不再沿原型链查找捕获的堆栈；顶层 await 的 ESM 求值不再以查找 constructor/Symbol.species 的方式调用 Promise.prototype.then()。
- ⏳ Promise.try 在同 realm 且返回 Promise 时直接返回该 Promise；已阻塞的 worker 再次调用 Atomics.wait() 抛 TypeError 而非崩溃。
- ⚛️ Atomics 方法按规范先读取 TypedArray 长度再强制转换索引；Iterator helpers 对超过 2^53-1 的 take/drop 限制抛 RangeError；asyncDispose 调用 return() 时不传参数。
- 📦 new import(...).x 正确抛 SyntaxError；部分模块加载崩溃边界改为拒绝并报错；负向 lookaround 在 /u 和 /v 模式下不再匹配代理对内部。
- 🧮 TypedArray 行为修正：subarray 省略第三个 undefined 长度参数；Float16Array 的 indexOf/lastIndexOf/includes 支持负值；不可变缓冲区 set 负偏移先抛 TypeError。
- 🧾 语法语义修正：static 初始化块中实例成员后的 await/return 报 SyntaxError；for 初始化器中的 using 只释放一次且视为不可变；转义 get/set 字段名后换行支持 ASI；delete super[key] 先检查 this；new Function 先检查代码生成策略。
- 🛟 更多致命 V8 错误由 Node.js 致命错误处理接管，--report-on-fatalerror 可生成诊断报告；极端语言用法可能抛 RangeError 而非崩溃。
- 💾 v8.serialize()/structuredClone()/postMessage() 使用新序列化格式，旧版 Node.js 无法反序列化；structuredClone/postMessage 支持超过 4GB 的 TypedArray/可调整 ArrayBuffer，v8.serialize 仍限 4GB。
- 🧠 内存变化：4–15GB RAM 机器默认老生代上限提高；Buffer/ArrayBuffer 计入 V8 全局分配限制；未用字节码约 3 分钟未运行后可在 major GC 中回收；原生对象和 isolate 属性缓存占用增加。
- ⚡ 性能改进覆盖 Array、String、对象属性读取、异步/await、正则、JSON.parse、BigInt 模除、模块解析和 Maglev 等。
- 🧰 诊断与工具：堆快照更详细且约两倍大小/耗时，包含内部对象、数值和完整源码；全局对象命名改变；CPU/heap profile 名称转义修复；Inspector 实时编辑功能完全移除。
- 📈 Tracing 迁移 Perfetto 后多数 V8 trace 事件不再出现在 --trace-event-categories 文件；--trace-gc 和 perf_hooks 的 gc 不受影响；GC 额外事件移至 disabled-by-default-v8.gc_extra。
- 🧩 WebAssembly：asm.js 不再编译为 Wasm；移除 WebAssembly.Function；--experimental-wasm-<name> 改为 --wasm-<name>；移除 lazy-validation/async-compilation 等标志；memory.copy/fill 内联和 Table 填充等优化。
- 🏷️ 移除或重命名多项 V8 标志，如 --js-upsert、--js-promise-try、--inspector-live-edit、--wasm-lazy-validation 等，旧标志不再接受。

---

### [发布 v1.3.0 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.3.0)

**原文标题**: [Release v1.3.0 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.3.0)

Rolldown v1.3.0 是一次小版本发布，重点新增实验性 import attributes 支持、面向编码代理的构建报告和 @rolldown/perf-kit，同时包含若干破坏性变更与大量修复；升级前需阅读破坏性变更，Vite 用户暂勿强制覆盖 rolldown 版本。

- 🌟 实验性支持 import attributes（`with { ... }`），JSON、`text`、`bytes` 类型无需插件；启用 `experimental.importAttributes` 后，同一文件不同属性会成为不同模块。
- 🔌 插件可在 `resolveId`、`load`、`transform` 中读取 import attributes，并可在 `resolveId` 中修改；设计遵循 Rollup 5。
- ⚠️ import attributes 默认关闭，因为会改变带属性模块的 id，可能破坏把 id 当文件路径的插件；Rolldown dev mode 与 Vite 尚未支持。
- 🛑 Vite 用户注意：不要用 `overrides` 或 `resolutions` 强制安装 `rolldown@1.3.0`；Vite 8.3.6 及更早版本需改动才能兼容，应等待支持 Rolldown 1.3 的 Vite 发布。
- 📝 新增实验性 agent 友好构建报告：`devtools: { mode: 'report' }` 会在 `node_modules/.rolldown/report/` 生成 Markdown/JSON，涵盖耗时、chunk、模块、包、依赖图、变更和原始指标。
- 🚀 新增实验性 `@rolldown/perf-kit`，可消费构建报告并测量页面 LCP/FCP、Node.js/Deno 服务启动时间、Cloudflare Worker 全局作用域耗时。
- 💥 破坏性变更：`preserveModules` 文件名遵循 Rollup，`[name]` 保留非 JS 扩展名，如 `data.json` 变为 `data.json.js`、`Comp.vue` 变为 `Comp.vue.js`，依赖旧文件名的 `exports` 需更新。
- 💥 CLI 破坏性变更：`--input` 不能再与位置参数入口同时使用；应使用 `rolldown 1.js 2.js` 或 `rolldown --input 1.js --input 2.js`。
- 🩹 重要修复：外部导入会正确保留 import attributes，避免不同属性导入被合并丢失；旧 `assert` 关键字会转为 `with` 并产生 `DEPRECATED_IMPORT_ASSERTION` 警告。
- 🔧 其他修复覆盖 tree-shaking、sourcemap、watch/dev、Vite 插件、JSON、错误诊断与性能等；文档新增构建报告、perf-kit 和 import attributes 指南。

---

### [性能工具包 | Rolldown](https://rolldown.rs/in-depth/perf-kit)

**原文标题**: [Perf Kit | Rolldown](https://rolldown.rs/in-depth/perf-kit)

overview summary  
@rolldown/perf-kit 是一个实验性性能优化工具，帮助编码代理让应用启动更快。它能测量浏览器页面、Node.js/Deno 服务器和 Cloudflare Worker，建立固定基线、校验渲染输出，并列出所有待处理线索；代理负责改代码，最终由测量数据决定哪些改动保留。

- 🧪 **实验性工具**：perf-kit 的命令和输出可能随版本变化，最低要求 Rolldown 1.3.0。
- 🎯 **解决三大问题**：单次构建无法证明性能提升；页面被改坏也可能显得更快；代理可能因一个工具无信号而过早停止。
- 🧰 **环境要求**：Node.js 22+、已构建好的应用；页面测试需要 Chrome/Edge，可用 `CHROME_PATH` 指定浏览器；Worker 测试需要 `@cloudflare/vite-plugin` 和 `wrangler`，覆盖率功能需 Wrangler 4.108.0+。
- ⚡ **无需安装即可运行**：可用 `npx @rolldown/perf-kit help` 或 `vp dlx @rolldown/perf-kit help`；也可作为开发依赖安装。
- 📁 **状态目录**：perf-kit 在当前目录的 `.perf-kit/` 保存状态，并写入 `.gitignore`，避免提交。
- ⚙️ **构建配置**：页面项目需开启 `sourcemap: true`，并开启 `devtools: { mode: 'report' }` 以生成构建报告；Vite 8 使用 Rolldown，Vite manifest 也可用。
- 🧵 **Worker 配置更简单**：Worker 目标可跳过手动构建配置，`worker-config` 会自动设置 sourcemap 和构建报告选项。
- 🤖 **配合编码代理**：复制浏览器、服务器或 Worker 的提示词，填入 `<...>` 后交给代理；提示词要求先运行 `help`，其会指向 `AGENTS.md` 手册。
- 🚫 **不要重复指导测量**：浏览器和服务器提示词不应额外加入如何测量或分析的步骤，否则会把代理带离官方手册。
- ☁️ **Worker 提示词前置条件**：应用必须用 Rolldown 构建；安装 perf-kit；将 `dist-attrib/` 和 `perf-kit.vite.config.ts` 加入 `.gitignore`。
- 📊 **结果查看**：代理需报告修改前后数字及所有尝试过的改动；页面还需查看 verdict 清单和 `scan --parity` 渲染输出校验。
- ✅ **页面判定规则**：FCP 和 LCP 中至少一个下降超过噪声，且两者都不得上升超过噪声；噪声阈值为 30ms 或基线的 2%，取较大者。
- 🖥️ **服务器判定规则**：`runtime.app_startup_ms` 下降超过 8ms 或基线的 2%，取较大者；启动时间很小时参考字节数和模块数。
- 🧱 **Worker 判定规则**：比较 `worker.app_startup_ms` 的配对运行结果，受 3ms 下限和多轮配对规则约束；若在噪声内，减少至少 32KB 或 10% 模块也可能打印 `KEEP`。
- 🔁 **一次只改一处**：两个改动同时存在时无法判断哪个带来收益，一个改动的损失也可能被另一个掩盖；Worker 在每个导入低于下限时可成组延迟 2–3 个导入。
- 🔍 **页面线索**：`scan` 会给出渲染阻塞 CSS、LCP 晚于 load、延迟加载候选、绘制前 CPU、冷字节、静态预绘制传输、大模块、兄弟变体组、静态保留导入等线索。
- 🩺 **先修前两类线索**：优先处理 render-blocking CSS 和 LCP after load；页面若等待它们，延迟加载的测量可能失真。
- 🧭 **人工确认渲染差异**：`scan --parity` 比较最终构建与原始构建；只有用户可批准差异或添加遮罩，代理不能自行接受，否则可能掩盖页面损坏。
- 🛠️ **常用命令**：页面用 `scan --app <dir>`；服务器用 `node-scan --entry dist/server.js --ready ...`；Worker 用 `worker-config`、`vite build --config perf-kit.vite.config.ts`、`worker-scan --request /`。
- 🧮 **静态分析命令**：`graph`、`what-if`、`cut`、`why`、`graph-diff` 需要构建报告，用于发现可延迟加载的代码；其结果是线索而非最终测量。
- ⚠️ **局限性**：实验室数据只对同一机器和固定节流有效；延迟加载只是移动工作而非删除工作；渲染校验不覆盖点击、登录或实时数据状态；field 模式仅测量一个账户、网络和机器。

---

### [Safari 27.3 Beta 发布说明 | Apple 开发者文档](https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes)

**原文标题**: [Safari 27.3 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes)

该页面依赖 JavaScript 才能显示内容；当前无法直接查看正文，但提供了 Markdown 版本，方便自动化工具和辅助工具访问。

- ⚠️ 页面需要启用 JavaScript 才能查看内容。
- 🔄 请在浏览器中开启 JavaScript 并刷新页面。
- 🤖 页面为自动化工具和辅助工具提供了访问方式。
- 📄 可查看该页面内容的 Markdown 版本。

---

### [发布 v1.65.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.65.0)

**原文标题**: [Release v1.65.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.65.0)

Playwright v1.65.0 发布，重点新增 Bun 测试运行支持、失败专用报告与 `onlyFailures` 选项，并改进测试锁、API、Cookie/代理/无障碍名称等行为，同时更新 Node.js 与浏览器版本要求。

- 🥟 新增 Bun 支持：需使用 `bunx --bun playwright test`；Bun 自行转译 TypeScript，不使用 Babel/编译缓存；无 watch 模式，`--tsconfig`/JSX 设置和自定义 ESM loader 不生效，堆栈、API 名称和控制台输出行为有差异。
- 🚨 新增 `failures` reporter，按发生顺序打印失败与成功重试并附摘要；HTML/JSON/JUnit reporter 新增 `onlyFailures`，仅保留意外结果、flaky 和中断测试。
- 🎯 测试运行器新增 `-exclusive-` 锁，使测试独占运行；`skip/fixme/fail/slow` 现在只接受描述并记录为注解；新增 `PLAYWRIGHT_TRANSFORM_CACHE_DIR`。
- 🧩 新 API/选项：`cdpSession.send()` 支持 `timeout` 和 `signal`；`testRun.mode()` 可在 reporter 预处理阶段返回执行模式。
- ⚠️ TypeScript 类字段遵循 `useDefineForClassFields`，ES2022+ 或未指定 target 时启用；读取构造参数属性的字段初始化可能失败，需移到构造函数或关闭该选项。
- 🖱️ `click/check/tap/fill/clear/selectOption` 等操作会等待元素不再 `inert`；持续 inert 会超时。
- 🔀 分片运行在所有分片都无匹配测试时以“No tests found”失败，可用 `--pass-with-no-tests` 允许；空分片在其他分片有测试时仍通过。
- 🍪 Cookie 匹配遵循 RFC 6265；带 URL 查询时不再错误返回子域 host-only cookie 或 `/apiv2` 的 `Path=/api` cookie；无名 cookie 发送/存储行为调整。
- 🔐 代理凭据不再发送给网站，仅用于代理挑战；网站认证应使用 `httpCredentials`。无障碍名称/aria 快照不再包含浏览器未渲染文本。
- 🔧 `APIRequestContext` 的 `params` 字符串/URLSearchParams 会追加到已有查询；`.css/.less/.scss` 导入必须存在并作为空模块加载；blob reporter 再次先清空输出目录。
- 🧪 CommonJS 输出中导入调用的测试位置改为指向被调用者开头，与 ESM 一致。
- 📦 不再测试 Node.js 20，建议 Node.js 22/24/26；Docker 镜像升级到 Node.js 26；浏览器版本为 Chromium 158.0.8127.18、Firefox 159.0、WebKit 27.2，并测试 Chrome 157/Edge 156。

---

### [Prettier 3.10：新的 Flow 语法、新的 JavaScript 语法，以及由 Yuku 提供支持的新插件 · Prettier](https://prettier.io/blog/2026/11/11/3.10.0)

**原文标题**: [Prettier 3.10: New Flow syntax, new JavaScript syntax, and new plugin powered by Yuku · Prettier](https://prettier.io/blog/2026/11/11/3.10.0)

Prettier 3.10 正式发布，重点包括对全新 Flow 语法和最新 JavaScript 提案的支持，并推出由高性能 Yuku 工具链驱动的官方插件 `@prettier/plugin-yuku`；同时修复了 JavaScript、TypeScript、Markdown、HTML、CSS、Vue、Angular、GraphQL、YAML 等多语言格式化中的大量稳定性与边界问题。

- 🚀 发布 Prettier 3.10，带来新语法支持、新官方插件及跨语言修复与改进。
- 🔌 新增官方插件 `@prettier/plugin-yuku`，由 Zig 编写的高性能 JavaScript/TypeScript 工具链 Yuku 驱动。
- 🧩 插件提供 `yuku` 和 `yuku-ts` 两个解析器，分别用于 JavaScript 和 TypeScript。
- 📦 由于包体积限制，该插件不随主 `prettier` 包捆绑，需要单独安装并加入 `.prettierrc` 的 `plugins`。
- 🧬 Flow 支持 `flow-parser 0.332.0` 新增语法，包括模板字面量类型、构造器类型、映射类型修饰符与键重映射、抽象/重写类成员、内联导入类型、CommonJS 导入导出绑定和 `unique symbol` 类型。
- 🛠️ 修复 Flow 中构造参数属性、`in out` 可变性、非空断言、`export as namespace`、可选元组成员、声明类私有字段及 mixin 继承等格式化问题。
- 🧪 JavaScript 新增对 Structs、Import Sync、Deferred re-exports 等提案语法的支持。
- 🧷 修复大量注释稳定性、括号保留、`prettier-ignore`、JSX、`yield`、范围格式化等 JavaScript/TypeScript 问题。
- ⚡ 提升含大量注释文件的格式化性能，并避免超长二元表达式导致调用栈溢出。
- 🎨 改进 CSS、SCSS、Less、HTML、Vue、Angular、Ember/Handlebars、GraphQL、YAML 等语言的格式化和边界处理。
- ⚙️ API/CLI 改进包括支持带 UTF-8 BOM 的配置文件、注释挂载辅助函数返回 `true`、更新实验性 CLI。
- 📈 杂项优化包括 Unicode 零宽标记处理、缓存并共享 `.editorconfig` 解析结果，提升 monorepo 配置解析速度。
- ❤️ 官方鼓励通过 OpenCollective 赞助 Prettier 或支持其依赖的上游项目。

---

### [博客 | pnpm](https://pnpm.io/blog?type=releases)

**原文标题**: [Blog | pnpm](https://pnpm.io/blog?type=releases)

本批发布说明覆盖 pnpm 12.20.0 至 11.28.8 的更新，重点包括实验性锁文件与 JSON 锁文件、hoisted linker/peer 依赖/overrides 修复、新增 `pnpm fund`、`pnpm store add`、`pnpm peers check --global`、平台变体与 pnpr registry 支持，以及凭据泄露、zstd 解压、签名等安全修复。旧版 pnpr 0.1.0-alpha.19 及更早版本不再支持远程解析和共享构建缓存。

- 📦 pnpm 12.20.0（2026-11-12）：在实验性 v13 lockfile 中记录本地目录依赖的 specifier；修复 hoisted linker、peer 依赖和 overrides 问题；捆绑的 node-gyp 不再包含被安全扫描器标记的 undici；pnpr 0.1.0-alpha.19 或更早版本不再支持远程解析和共享构建缓存。
- 💰 pnpm 12.19.0（2026-11-10）：新增 `pnpm fund`、`projectScopedOptionalPeers` 设置和实验性 JSON 锁文件；loaded node linker 可处理需要构建的包；修复离线安装错误打印 registry 凭据的安全问题；检查所有 workspace 项目的 engines 和 platform 字段，并修复多项 hoisted-linker 与 frozen-lockfile bug。
- 🧩 pnpm 12.18.0（2026-11-05）：支持在 pnpr registry 上打包、发布和安装带平台变体的包；新增 agent skills 按技能审批和 `pnpm store add` 离线 tarball 安装；重复安装及 `verifyDepsBeforeRun` 不再读取未变更 workspace 项目的 `package.json`；修复多项 peer 依赖解析 bug。
- 🔗 pnpm 11.28.11（2026-11-05）：修复 `excludeLinksFromLockfile` 冻结安装、workspace 中的 `pnpm link`、带悬空符号链接的 `pnpm deploy`，以及 `verifyDepsBeforeRun` 触发不必要安装的问题。
- 🧭 pnpm 12.17.0（2026-10-30）：新增 `pnpm peers check --global`、overrides 中的依赖组选择器和通配符，以及 `pnpm outdated`/`pnpm update` 对 runtime、包管理器、Cargo 和 Python 的更新；修复 Docker 镜像中其他用户无法读取文件、重复安装漏掉本地依赖变更的问题。
- 🧹 pnpm 11.28.10（2026-10-30）：防止 `pnpm store prune` 在 `cacheDir` 指向父目录时误删其他 store；修复全局安装命令加载 hoisted 依赖、重复安装漏掉本地依赖变更的问题。
- 🐛 pnpm 12.16.1（2026-10-27）：修复在安装 Cargo crates 的 workspace 中冷 store 下 `pnpm install` 卡住的问题；修复 `pnpm pack` 打包被 `files` 按名称排除的文件的问题。
- ⚙️ pnpm 12.16.0（2026-10-27）：新增全局 `--env-file` 标志、symlinked `pnpm-lock.yaml`、`pnpm setup --no-modify-path`；修复 zstd 解压和签名两个安全问题。
- 🛡️ pnpm 11.28.9（2026-10-27）：修复注册表响应 content encodings 过多导致崩溃的问题（GHSA-xjj6-f33q-929c）；按容器 CPU 配额设置安装 worker 池；重复 `pnpm install` 会响应更多设置变化。
- 🗓️ pnpm 11.28.8（2026-10-22）：原文仅列出发布日期，未提供具体变更内容。

---

### [ESLint 现在正式支持对 Shell 脚本进行 lint 检查 - ESLint - 可插拔的 JavaScript Linter](https://eslint.org/blog/2026/11/eslint-shell-plugin-announcement/)

**原文标题**: [ESLint now officially supports linting of shell scripts - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/11/eslint-shell-plugin-announcement/)

ESLint 宣布正式支持对 shell 脚本进行 lint，并推出官方语言插件 `@eslint/shell`；这是其向通用、语言无关 lint 平台发展的重要一步，此前已支持 JSON、Markdown 和 CSS。

- 📅 该公告发布于 2026 年 11 月 6 日，属于 Announcements 类别。
- 🧩 `@eslint/shell` 是 ESLint 官方支持的语言插件，提供 shell 脚本解析、受 ShellCheck 启发的规则集以及推荐配置。
- ⚙️ 可通过 `npm install @eslint/shell -D` 安装，并在 `eslint.config.js` 中启用 `shell/recommended`。
- 🐚 插件支持 Bash、POSIX `sh` 和 MirBSD Korn shell（mksh），也可手动配置 shell 方言和规则。
- 🛡️ 推荐规则可捕获未加引号的展开、未使用变量、不安全的 `read` 用法等常见问题。
- 🔍 规则还覆盖旧式命令替换、遍历 `ls` 输出、`printf` 格式字符串中的变量等问题。
- 🌳 插件将 shell 脚本解析为 ESTree 风格语法树，便于编写自定义规则；解析器基于 `mvdan-sh`，即 `shfmt` 使用的解析器。
- 🧪 可在 ESLint Code Explorer 中探索 shell 语法树。
- ✅ 目标是在 ESLint 统一配置和规则 API 下，与项目其他代码一起 lint shell 脚本，提升脚本质量与一致性。
- 💚 ESLint 是独立开源项目，由志愿者维护，并鼓励企业赞助支持。

---

### [现代 Web 指南 1.0](https://developer.chrome.com/blog/modern-web-guidance-v1)

**原文标题**: [Modern Web Guidance 1.0: The web platform expertise your coding agent is missing  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/modern-web-guidance-v1)

Chrome for Developers 宣布 Modern Web Guidance 1.0 正式稳定，这套技能集把 Web 平台专业知识、最佳实践与浏览器兼容性数据嵌入编码代理，帮助 AI 生成的 Web 代码更快、更易访问、更安全。该项目的协作范围已从 Chrome 扩展到 Firefox 和 Edge，并基于 Baseline 数据持续演进。

- 🚀 1.0 稳定版发布：在 Google I/O 预览后正式推出，适用于不同模型和代理框架的 Web 开发工作流。
- 🛠️ 新增现代化工作流：扫描现有 HTML、CSS、JavaScript 和 package.json，帮助代理发现可安全升级的旧模式、依赖和 polyfill。
- 📚 扩展指南数据库：覆盖数百个经核实的 AI 知识缺口，提供专家审核的跨浏览器解决方案。
- ♿ 加强人工审核：每份指南由内容领域技术负责人签核，用户侧指南还经过无障碍专家和真实辅助技术测试。
- 📊 完整评估覆盖：提供公开评估仪表盘，展示相较未使用 Modern Web Guidance 的代理所取得的可量化提升。
- 🌐 跨浏览器协作：Firefox 和 Edge 加入 Chrome，共同改善兼容性并贡献项目。
- 🧠 补齐模型短板：重点覆盖无障碍、用户体验、性能和安全，例如键盘焦点、inert 管理、减少动态效果、表单验证、HTML 清理、CSP 和 Passkey。
- ⚡ 推荐最佳 Web 特性：优先使用原生 HTML/CSS 而非多余 JavaScript，如 Popover/Dialog 动画、滚动与滑动交互、页面过渡、Passkey 和自动填充。
- 🔍 结合 Chrome DevTools for agents：前者提供编码前知识，后者提供运行时验证、调试与优化，减少反复轮次。
- 📈 客户成效显著：Pensionbazaar 交付周期缩短 90%+、UI 缺陷减少 90%+；Policybazaar 人工审计工作量减少 92%；WeTV 自动解决 90% 性能检查失败、调试时间减少 87%；note 通过率从 61% 升至 94%；MetaMask 机器人审查约 480 个 PR，推动修复 43 个问题。
- 🧩 安装与更新：运行 `npx modern-web-guidance@latest install`，旧版本用 `npx modern-web-guidance@latest update`；也可通过 Claude Code、Codex、Cursor、Copilot 等插件市场安装。
- 🤝 社区共建：由浏览器工程师、Web 标准与无障碍专家维护，并开放 GitHub 贡献，帮助代理持续跟进 Web 平台演进。

---

