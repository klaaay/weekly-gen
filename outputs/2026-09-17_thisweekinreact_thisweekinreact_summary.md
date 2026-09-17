### [](https://sentry.io/resources/agent-tracing-series/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=agenttracing-fy27q3-agenttracingseries&utm_content=newsletter-primary-workshop-series-register)

**原文标题**: [Debugging agents in different environments | Sentry](https://sentry.io/resources/agent-tracing-series/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=agenttracing-fy27q3-agenttracingseries&utm_content=newsletter-primary-workshop-series-register)

Sentry 推出两场 Workshop 系列，聚焦如何使用 Sentry Agent Tracing 理解并调试在不同环境中运行的 AI agent；首场面向入门，介绍 traces 和 spans，并实机演示电商聊天机器人、Slack agent 和 GitHub Actions 中的 PR 审查 agent；第二场深入 Sentry 生产实践，展示工程师如何收集、调查大量 traces，并利用用户挫败等信号发现问题。

- 🔍 当 AI agent 回答不佳、调用错误工具或响应过慢时，需要追踪其执行过程。
- 🧭 两场 Workshop 由 Serge 和 Ryan 主讲，主题是用 Sentry Agent Tracing 调试 agent。
- 🧱 第一场 10 月 7 日：从 traces 和 spans 基础开始，无需追踪经验。
- 🛍️ 通过实机演示，跟踪电商聊天机器人、Slack agent、GitHub Actions 中 PR 审查 agent 的执行。
- 💬 学习读取 traces/spans，理解 agent tracing 提供的额外上下文。
- ⚙️ 学习为不同环境中的 agent 添加追踪，并检查输入、输出、工具调用和 token 使用。
- 🐛 用这些信息排查错误与缓慢响应，定位多步骤失败中的问题。
- 📈 第二场 10 月 14 日：Sentry 工程师如何在其 AI 功能背后调试自己的 agent。
- 🧑‍💻 展示生产环境如何收集 traces、调查 agent 行为，并在海量 traces 中找出值得关注的失败。
- 🚨 介绍如何利用用户挫败等信号，在大规模场景下发现问题，并开始自己的 agent tracing。
- 🎙️ Sentry 赞助 Syntax Podcast，可在常用收听平台收听。

---

### [](https://sentry.io/product/tracing/ai-agent/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=agenttracing-fy27q3-evergreen&utm_content=newsletter-primary-product-learnmore)

**原文标题**: [Agent Tracing: See Every Step of Your AI Agent Run | Sentry](https://sentry.io/product/tracing/ai-agent/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=agenttracing-fy27q3-evergreen&utm_content=newsletter-primary-product-learnmore)

Sentry Agent Tracing 可追踪 AI agent 从系统提示到最终输出的完整执行，把会话、运行和故障点关联到应用上下文，帮助定位数据库慢查询、API 失败或前端超时等问题，让不可靠的 AI 构建过程变得可观测、可调试。

- 🧭 全栈 agent trace：模型调用、工具执行、handoff 与 HTTP、数据库、队列 spans 处于同一 trace 层级。
- 💬 Conversations：把原始 AI spans 转成聊天式回放，按用户顺序查看输入、响应和工具调用，并可点击跳转到底层 LLM/工具 span。
- 💰 成本与 token：仪表盘展示 agent runs、错误率、模型费用、token 细分（输入/输出/缓存/推理）及每工具执行统计。
- 🛠️ 工具可靠性：监控每工具错误率、P95 延迟和调用频率，发现低频但会导致坏输出的工具。
- 🔌 自动埋点：支持 OpenAI Agents、Vercel AI SDK、LangChain、LangGraph、Pydantic AI、Anthropic、Google GenAI、Laravel AI 等 10+ 框架。
- 🌐 MCP 可观测性：MCP 工具调用作为 span，显示服务器、返回值、耗时、失败，并关联到 agent run。
- 📊 自定义成本监控：按用户层级、功能或 agent 建仪表盘，用 user_tier、feature_flag 等标签查询。
- 🧪 集成场景：支持 Vercel AI SDK + Next.js、OpenTelemetry、Claude Code、OpenCode、pi、MCP server、Neon Functions。
- 🤖 自动排查：可用 Claude Routines + Sentry MCP 自动 triage nightly agent 错误并开票。
- 📚 评估数据集：通过 CLI 或 MCP 导出真实 agent 会话，用于 Braintrust、Langfuse、promptfoo、Phoenix 等 eval 工具。
- 🏢 Anthropic 案例：Sentry 在帮助开发 Claude Sonnet 中发挥了重要作用。
- 🚀 快速开始：Python/JS 安装 SDK、开启 tracing 即可自动生成 spans 和仪表盘，文档提供更多框架说明。
- 🆓 免费计划：agent tracing、仪表盘、成本追踪均在所有计划中可用，包括免费 Developer 计划。
- 🎓 工作坊：10 月 7 日不同环境调试 agent，10 月 14 日 Sentry 如何调试自家 AI agent。
- ❓ FAQ：解释 agent tracing 与 LLM monitoring、eval 工具、现有 Sentry 设置、支持框架、MCP、Conversations 的关系。

---

### [](https://posthog.com/newsletter/2030-shaped-software?utm_source=twir&utm_campaign=sept16)

**原文标题**: [2030-shaped software](https://posthog.com/newsletter/2030-shaped-software?utm_source=twir&utm_campaign=sept16)

文章认为：到 2030 年，AI 代理将成为软件的主要用户，因此现在就要按“代理优先”构建产品——让代理负责执行，人类专注判断、决策、信任与验证；聊天是入口，生成式 UI 与必要专用界面补足交互，并以云端和多触点实现无处不在。

- 🤖 核心判断：2030 年 AI 代理会成为软件的首要用户，要构建“2030-shaped software”，而不是只给现有产品加 AI。
- 🧠 人与代理分工：代理负责“做”，人类负责判断、决定、排序、消除歧义，以及理解与信任结果。
- 🧱 传统“操作型”UI 如按钮和表单将减少，转而支持审批、优先级、方向选择、验收与安全确认。
- 🛠️ 产品基础设施要代理优先：人类能做的事，代理也应能做，需完整 API、MCP 服务器、工具和权限。
- ⚠️ 缺少能力是失败模式：如果代理无法创建实验或完成关键步骤，就仍需人类补位，削弱代理价值。
- 🧩 不能只依赖模型提供商；自建代理运行框架可保证质量、保护品牌并持续改进，而上下文是护城河。
- 📚 上下文工程很关键：把源代码、使用数据、客户数据和产品技能，在合适时机输入代理。
- 💬 聊天是前门，生成式 UI 在内部：聊天适合指挥代理，但图表、开关等生成式 UI 能弥补文本低带宽问题。
- 📄 生成式 UI 大多一次性，部分会成为可保留、分享、复制的工件，如报告、文档、代码、PR、配置甚至应用。
- 🔍 文本不够时仍需专用 UI：信任与验证界面、分诊与收件箱界面，用于检查代理工作与处理需人类决策的事项。
- 🚩 不是简单删按钮：若只是查看状态，代理一句话即可；若涉及信任、判断或行动，应分别交给专用 UI 或代理能力。
- 🌐 代理不按应用方式工作：产品应主动到达用户，覆盖桌面、Slack、移动端、邮件、API、语音等。
- ☁️ 云优先是方向：人类与代理共享控制平面，薄客户端接共享后端，支持并发运行大量代理并随处优化输出。
- 🧪 云基础设施必须优秀：沙盒要快速、稳定、不崩溃，让应用无处不在而基础设施隐形。
- 🚀 落地策略：2026 不是 2030。PostHog 选择“半新”路线，先用现有数据与基础设施扩展 PostHog Desktop，再迁移其他界面。
- ⏳ 若不改变，风险是做出“2026 形态 + AI 补丁”的软件；2030 重要的公司会提前多年开始构建。

---

### [React 开发者工具 - Chrome 网上应用店](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)

**原文标题**: [React Developer Tools - Chrome Web Store](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)

React Developer Tools 是 Meta 推出的 Chrome 开发者工具扩展，用于调试开源 React JavaScript 库应用；它新增 Components 与 Profiler 两个面板，可检查组件树、编辑 props/state 并记录性能信息，且开源、声明不远程传输数据。目前约 500 万用户、评分 3.9/5（约 1.6K 条评分）。

- ⚛️ 为 Chrome DevTools 添加 React 调试工具，安装后出现“Components ⚛”和“Profiler ⚛”两个新标签。
- 🌳 Components 标签展示页面渲染的根 React 组件及其子组件层级树。
- 🛠️ 选中组件后可在右侧面板查看并编辑当前 props 与 state，并通过面包屑查看父级组件链。
- 🔗 在 Elements 标签中检查 React 元素后切换到 React 标签，该元素会在 React 树中自动选中。
- 📈 Profiler 标签用于记录性能信息。
- 🔒 需要权限访问页面 React 树，但不会远程传输任何数据；扩展完全开源，源码位于 GitHub。
- ⭐ 评分 3.9/5，约 1.6K 条评分；约 5,000,000 用户。
- 👤 由 Meta 提供，版本 8.0.0，更新于 2026 年 9 月 11 日，大小 655KiB，语言为英语。
- 🛡️ 隐私声明：不收集或使用数据，不向第三方出售，不用于无关目的或信用/贷款评估。
- ✅ 遵循 Chrome 扩展推荐做法。
- 🧩 相关扩展包括 Vue.js devtools、Angular DevTools/state inspector、MobX、Redux DevTools、React Context DevTool、JSON Formatter、GraphQL Network Inspector、LocatorJS、Ember Inspector 等。

---

### [](https://github.com/facebook/stylex/pull/1865)

**原文标题**: [[RFC] Add compile-time CSS enums and exhaustive matching by nmn · Pull Request #1865 · facebook/stylex · GitHub](https://github.com/facebook/stylex/pull/1865)

这是 facebook/stylex 的 RFC PR #1865，计划添加编译时 CSS 枚举与穷尽匹配：用 `stylex.defineEnum` 定义有限状态，用 `stylex.match` 在样式中映射状态，并可在元素上覆盖枚举。PR 目前为草稿，属于 6 个 PR 中的第 1 个。

- 🧩 `stylex.defineEnum` 定义 CSS 变量式有限状态，可设置默认值以及 `@media` 等条件映射。
- 🎯 `stylex.match` 根据当前枚举状态选择对应值，适用于任意 CSS 值，不限于颜色。
- 🎨 典型用例包括自定义 `color-scheme` / `light-dark`、`density` 等可切换状态。
- 🧬 枚举可通过 `stylex.props(colorScheme('dark'))` 在元素上覆盖，并继承给后代；本地赋值优先于继承或媒体默认值。
- 🔀 多个赋值经 `stylex.props` 组合时，最后一个赋值整体替换之前选择；运行时值需用条件选择编译后的调用，不支持 `density(runtimeValue)`。
- ✅ TypeScript 和 Flow 会跨导入检查合法状态，并要求 `match` 映射覆盖所有状态。
- 🖱️ 可在 `match` 外层使用伪类和 at-rules，例如 `:hover` 只改变当前元素，不改变继承给其他消费者的枚举。
- 🧱 本 PR 支持标量枚举赋值；条件赋值和展开语法计划在 #1870 中实现。
- 🛠️ 实现基于 CSS space hack：每个状态一个自定义属性，仅一个处于 active；`initial` 触发 `var()` fallback，其他变量为空白，因此无需原生 CSS `if()`。
- 🧪 已通过编译器快照、TypeScript/Flow 检查，以及默认值、继承、根覆盖、原始与压缩 CSS 的浏览器验证。
- 📉 性能与体积影响较小；压缩后的 `stylex.js` 略有增加。
- 💬 讨论认为未来可用 CSS `if()` 在底层实现；可能倾向只支持字符串枚举，并需更新 `@stylex/enforce-extension`；组件 variants 仍由 `stylex.create` 处理。

---

### [](https://ondrejvelisek.github.io/the-cost-of-abstraction-for-humans-and-ai-agents/)

**原文标题**: [The Cost of Abstraction for Humans and AI Agents | Ondrej Velisek](https://ondrejvelisek.github.io/the-cost-of-abstraction-for-humans-and-ai-agents/)

过度抽象看似提升可维护性，实则给人类和 AI Agent 增加隐性成本；作者通过实验估计，过度抽象的代码库会让 AI Agent 成本与耗时增加约 30%，最差任务达 5 倍，因此应只在真正需要时抽象。

- 🧠 抽象是隐藏实现并提供可复用接口的边界，如函数、类、组件、CSS 类、文件、包等。
- ✅ 抽象对大型系统至关重要，可隐藏复杂度、命名和复用代码，但必须权衡成本与收益。
- ⚠️ 过度抽象很难察觉，会逐渐累积；开发者常因害怕修改旧抽象、时间压力、教育训练和团队文化而不断添加新层。
- 💸 每次抽象都带来间接成本：代码分散、跳转增多、心智负担上升；人类和 AI 每次读代码都要付出。
- 🤖 AI 从人类代码中学会过度抽象，因此也会复制这一反模式，并推高使用成本。
- 📊 实验用 4 个代码库、394 次 Agent 运行测量：过度抽象任务成本在 0.8x 到 5x 之间，最差是改按钮颜色，成本高 5 倍、时间高 4.3 倍。
- 🔍 成本主因不是代码量，而是跨文件抽象层：读取文件和模型往返轮次显著增加；同文件内抽象对 AI 几乎免费。
- 🧾 对真实中大型代码库的保守外推：过度抽象使 AI Agent 账单约增加 30%。
- 🧩 不应抽象的例子包括：无意义常量、静态 JSX 列表映射、简单工厂函数、多余 CSS 类、父组件提前消费 context、只做重命名的翻译层。
- 🛠️ 建议：用类型系统保护值表达式；从最接近使用处消费 context；遵循现有库/后端命名；优先共置代码，避免不必要跨文件边界。
- 🧭 结论：抽象不可少，但每个抽象都有成本；应“先思考再抽象”，在代码审查中识别过度使用，并明确指导团队和 AI Agent。
- 📜 作者公开了 no-over-abstraction.md 规则，希望降低人类心智负担和 AI 账单。

---

### [](https://www.nikhilsnayak.dev/blog/react-server-functions)

**原文标题**: [React Server Functions Are More Than Mutations | Nikhil S](https://www.nikhilsnayak.dev/blog/react-server-functions)

概述总结
文章探讨 React Server Functions 不止用于 mutation，也可作为查询与流式读取原语。作者在 effective-rsc 中保留 React 的 encodeReply/Flight 协议，用 HTTP QUERY 表达读取语义，并用 ServerFn.stream 流式传输条目、React 元素和未完成的 Server Components，最后解决流结束与 Flight 响应未完成之间的生命周期问题。

- 🧩 核心问题：水合后获取数据会偏离初始服务端渲染路径，无限滚动尤其明显，因为需要保留已展开/交互过的条目并追加新内容。
- 🔁 常见方案如 SWR 或 TanStack Query 能解决客户端获取，但会在数据库操作与客户端缓存之间引入第二套数据抽象。
- 🧪 作者构建 Fieldnotes 阅读流作为示例，数据来自 SQLite，包含 10,000 条虚构条目。
- 🧷 目标：复用 React Server Function 的参数编码与结果解码，不另建 URL 参数和 JSON 契约。
- 🚫 POST 会走 mutation 路径并触发路由刷新；GET 的请求体又没有通用语义。
- ✅ 使用 HTTP QUERY：安全、幂等、请求体可携带输入，同时保留 Server Function 引用、encodeReply 与 Flight 响应。
- 🛠️ 同一 handler，不同消费方式：ServerFn.query(getPage) 选择读取语义，ServerFn.queryAtom 连接 Effect Atom 的 value、pending 和 failure 状态。
- 🌊 Flight 可序列化 ReadableStream；ServerFn.stream 让条目逐个到达，而不必先收集整页。
- ⚛️ 流中可传 React 元素：renderStory 返回 <StoryCard />，客户端无需导入组件，也无需自定义 JSON 重建格式。
- 🧵 卡片内可包含 Client Component 与 Effectful Server Component；StoryNote 通过 Suspense 在展开时加载。
- ⏳ 关键问题：条目流 EOF 不等于 Flight 响应完成，最后一张卡片可能仍有 pending Server Component；过早取消会中断已显示卡片所需内容。
- 🧮 解决方式：适配器在流结束后等待 Flight 完成；中断仍可取消，晚到的传输错误仍可失败。
- 🧭 生命周期归属：流消费者对请求负责至 Flight 完成；keepAlive 只保留已收条目，卸载时需显式中断活动请求。
- 🔄 恢复机制：用查询原语单独重试失败的 note，不重置整个 feed；新请求可基于最后收到 ID 继续分页。
- 📚 组合方式：ServerFn.stream + Stream.scan + Atom.fn 实现追加列表；首屏由服务端渲染卡片，滚动后流式追加。
- 🧠 结论：React owns UI, Effect owns runtime；查询与流仍操作普通 Server Function 引用，相关 API 已在 effective-rsc 0.2.0 提供。

---

### [](https://www.brenelz.com/posts/solidjs-its-the-little-things/)

**原文标题**: [SolidJS, It’s the Little Things](https://www.brenelz.com/posts/solidjs-its-the-little-things/)

SolidJS 2.0 的六个小改进共同提升了开发体验：可查询数据是否 pending、更少接线的乐观更新、可覆盖的派生状态、按数据源选择计算位置、把服务端读取当作函数调用，以及更会解释自身行为的运行时。

- ⏳ `isPending` 可直接询问数据或表达式是否处于进行中，例如 `isPending(user)` 或 `isPending(() => user().name)`，比 React 只能观察 transition pending 更贴近数据。
- ⚡ `createOptimisticStore`、`action` 和 `refresh` 让乐观更新更简单：从 API 派生服务器真相，在 store 上局部突变，完成后移除乐观层并用刷新后的服务器数据校准。
- 🔁 Solid 的乐观更新可用 generator 恢复上下文，并用 `m.push(message)` 这类 mutation 让 store 细粒度追踪变化；React `useOptimistic` 需自行连接获取和刷新，还要额外 `startTransition`。
- ✍️ `createSignal(() => props.name)` 提供可写的派生状态：本地可覆盖，来源 prop 变化时自动重置；React 需要用受保护的 state 更新模式进行更多接线。
- 🌐 Solid 2 可对单个响应式源配置 SSR/水合，如 `ssrSource: "client"` 让 `localStorage` 只在浏览器计算，服务端渲染 fallback；决策贴近数据源，而 React 类似能力常作用于组件层面。
- 📡 通过 `GET` 辅助函数，服务端函数可像普通异步函数一样被客户端调用，用于读取；Solid 负责 endpoint、序列化、解码和类型传递，统一读写模型。
- 🧠 React Server Functions 主要面向 mutation，Next.js 中读取常走 Server Components 或 API 路由；文章也提到 TanStack Start 为 React 提供 GET server functions。
- 🛠️ Solid 2 开发期会警告常见错误，如组件顶层读取响应式值产生 `STRICT_READ_UNTRACKED`，并提示把读取移入 JSX 的追踪作用域。
- 🔍 可选的 attribution engine 能追踪计算为何重跑，并标记过度订阅、顺序异步瀑布、effect 反馈自身输入等问题。
- ✅ 结论：每个细节单独看很小，但共同让 Solid 2.0 更贴合数据、更具良好 DX，并在出错时提供有用解释和修复路径。

---

### [](https://dev.to/subito/from-1256ms-to-96ms-fixing-inp-in-a-massive-react-dropdown-16l7)

**原文标题**: [From 1,256ms to 96ms: Fixing INP in a Massive React Dropdown - DEV Community](https://dev.to/subito/from-1256ms-to-96ms-fixing-inp-in-a-massive-react-dropdown-16l7)

Subito 团队为拥有约 1,175 个品牌选项的 MultiSelect 下拉框修复移动端打开卡顿：根因是一次性挂载全部选项组件，导致 INP 达到 1,256ms；他们用手写约 90 行的 useVirtualScroll 只渲染可见行与缓冲区，并依赖所有行等高，最终把 INP 降至 96ms、DOM 选项节点从约 1,175 降至 13。

- 🧩 背景：Subito 设计系统的 MultiSelect 基于 react-select 重构，常用于搜索、勾选、Apply 的筛选器。
- 📦 规模差异：普通筛选项约十几项，体验即时；但“Marca”品牌筛选有约 1,175 个选项。
- 🐌 问题：在移动端 4x CPU 降速下打开品牌下拉框，本地 INP 为 1,256ms，评级“poor”，远高于良好阈值 ≤200ms。
- 🔍 根因：打开菜单时 React 同步创建约 1,175 个 Option 组件及其 DOM 节点，而可视区域一次只能显示约 6 行。
- ⏱️ INP 分解：INP 包含输入延迟、处理耗时、呈现延迟；此处处理耗时形成巨大同步阻塞，阻止下一帧绘制。
- 🪟 虚拟化方案：不重写全部也不引入大型库，手写约 90 行 useVirtualScroll，仅渲染可见行和 OVERSCAN=5 的缓冲行。
- 📏 核心计算：菜单挂载后测量一次单行高度，用 itemHeight 计算总高度、startIdx、endIdx 和 offsetTop。
- 🏗️ DOM 结构：外层容器高度为 1,175×40px≈47,000px 以保留滚动条，内层绝对定位，只挂载约 13 行。
- ⚠️ 关键前提：所有选项行必须等高；行高不一致会导致滚动错位、重叠或无法访问。
- 🧪 检查方法：用 Set 收集 [role="option"] 的高度；若只有一个高度则适用，若多个高度则需统一或改用测量库。
- 🧩 非等高替代：统一行高并截断长文本，或使用 TanStack Virtual / react-virtuoso 逐行测量。
- 📉 结果：本地 INP 从 1,256ms 降至 96ms；[role="option"] DOM 节点从最多约 1,175 降至 13。
- ♿ 权衡：虚拟化移除屏幕外 DOM，浏览器原生 Ctrl+F 找不到不可见品牌，用户需依赖自定义搜索。
- ✅ 实践清单：检查实际挂载量、确认行高一致、只挂载可见行 + 缓冲区、关注 DOM 节点数而非总条目数。
- 💬 评论补充：固定高度虚拟化只是“一个测量值 + 算术”；真正关键的是先判断行高是否统一，并诚实说明可访问性代价。

---

### [](https://tsrx.dev/blog/removing-lazy-destructuring)

**原文标题**: [TSRX](https://tsrx.dev/blog/removing-lazy-destructuring)

TSRX 在 2026 年 9 月 14 日的发布中移除了惰性解构语法 `&{...}` 和 `&[...]`；现在绑定位置中的 `&` 会像 TypeScript 一样报语法错误，且没有替代语法。响应式状态改为通过各框架自己的 API 读取，详情见 RFC #106。

- 📅 2026 年 9 月 14 日起，`&{ ... }` 与 `&[ ... ]` 从 TSRX 语言中移除，写 `&` 前缀解构会直接触发语法错误。
- 🧬 该特性最初为 Ripple 旧 props 访问器和 `track()` 语法糖而设；Ripple props 变为普通对象后已无必要，其他目标框架也不需要。
- ⚠️ 它导致同一模式产生两种绑定，使用处无法看出是否响应式，类型系统也隐藏了响应性。
- 🧩 惰性绑定不是普通变量，`{ name }`、`count++` 等语义会因远端的 `&` 改变，读者和工具难以追踪。
- 🧹 语法对空格敏感且非 TypeScript，解析器、Prettier、ESLint、编辑器语法、语言服务器和 LLM 都需额外适配。
- ✅ 替代方案：React/Preact/Octane 用普通解构；Solid 用 `props.name` 或 `splitProps`；Vue 用响应式代理或 `toRefs`；Ripple 用 `track()` 对象并读写 `.value`。
- 🔧 迁移是机械性的：旧写法会编译失败并指向 `&`，不会静默改变含义。
- 🛠️ 配套清理：移除 `tsrx/no-lazy-destructuring-in-modules` ESLint 规则，Prettier 不再打印前缀，编辑器语法不再高亮，Ripple 的 `Tracked<V>` 将变为 `{ value: V }`。
- 🎯 这是 TSRX 早期独有设计的最后一项；现在 TSRX 仅是在 TypeScript + JSX 上增加语句容器、标记控制流、作用域样式和子模块，语言更小、更易学、更符合工具和模型预期。

---

### [](https://amazonappdev2026.devpost.com/?utm_source=amzn-dev_pai&utm_campaign=ref&utm_medium=nl&utm_content=twr)

**原文标题**: [Build, Ship, Shape: Amazon Developer Hackathon: Build across Amazon Devices and shape what's next. - Devpost](https://amazonappdev2026.devpost.com/?utm_source=amzn-dev_pai&utm_campaign=ref&utm_medium=nl&utm_content=twr)

亚马逊开发者黑客松首次将 Fire TV、Alexa+、Ring 和 Bee 汇聚于同一全球赛事，开发者可针对单一产品或跨产品构建，连接客厅、前门与云端，并借助 SDK、模拟器、示例代码、文档、实时办公时间和 AI 工具，从创意走向提交。

- 🚀 首次开放：Fire TV、Alexa+、Ring 和 Bee 同时向外部开发者开放，可构建单一产品或组合方案。
- 🛠️ 开发支持：提供 SDK、模拟器、示例代码、文档、实时办公时间和 AI 工具，帮助原型设计与排错。
- 🎯 参赛收益：产品反馈直达相关团队；可争夺价值 19 万美元的现金与 AWS 积分，赛道获胜者还可与 Amazon Developer 团队 1:1 交流。
- 🧭 开始步骤：选择 Fire TV、Alexa+、Bee 或 Ring 赛道，配置对应开发环境，查看资源及赛道详情与要求。
- 📦 提交内容：在截止日期前提交可运行的演示、代码仓库和产品反馈。

---

### [](https://motion.dev/docs/react-animate-view)

**原文标题**: [AnimateView - Animated page transitions in React | Motion for React](https://motion.dev/docs/react-animate-view)

AnimateView 是 Motion 面向 React 的视图过渡组件，基于浏览器原生 View Transition API、Motion 的 mini animate() 和 React 的 ViewTransition，用于进入/退出、更新、共享元素及 Suspense 过渡。它要求 React 与 React DOM 19.3+，从 `motion/react-animate-view` 导入；适合页面级过渡，而可中断的微交互更适合布局动画。

- 🧩 核心用途：在不同视图间动画化元素，并配置 `clipPath` 等值与 Motion transitions。
- ⚛️ 依赖版本：需要 React 和 React DOM 19.3 或更高版本，更新时需一起升级。
- 📦 安装方式：先安装 Motion：`npm install motion`。
- 📥 导入方式：从单独入口 `motion/react-animate-view` 导入，不从 `motion/react` 导出。
- 🚚 从 Motion+ 迁移：将 `motion-plus/animate-view` 替换为 `motion/react-animate-view`，API 不变，无需会员或 access token。
- 🎬 基础用法：用 `<AnimateView>` 包裹元素，并在 `startTransition` 中改变状态以触发视图过渡。
- 🌫️ 默认动画：元素进入/离开 DOM 时，默认执行浏览器淡入/淡出动画。
- ⚙️ 过渡配置：可用 `transition` 设置全局过渡，也可分别为 `enter`、`exit`、`share`、`update` 设置。
- 🌊 弹簧与布局：可导入 `spring` 配置弹簧动画，并用 `transition.layout` 单独控制尺寸与位置变化。
- 🎨 自定义值：设置自己的值会禁用默认透明度交叉淡入；显式传入 `opacity` 可重新启用。
- 🔄 更新动画：内容、样式、尺寸或位置变化时可动画化，适合列表重排等场景。
- 🔗 共享元素：当具有相同 `name` 的元素在同一过渡中一进一出时触发；`name` 在每个视图中必须唯一。
- 🧭 过渡类型：配合 React `addTransitionType`，让 `enter`、`exit`、`share`、`update` 根据上下文动态生成动画。
- ⏳ Suspense：用 `AnimateView` 包裹 `Suspense` 边界，可在内容与 fallback 之间交叉淡入。
- 🚀 性能观点：视图过渡会创建位图与伪 DOM，可能比布局动画更耗内存、更慢；且不可中断，更适合页面级过渡。
- 🧱 主要 Props：`children`、`name`、`transition`、`enter`、`exit`、`update`、`share`、`onAnimationStart`、`onAnimationComplete`。
- 🧼 其他特点：`AnimateView` 使用 React 的 `ViewTransition` 边界，不会向 DOM 添加额外包装元素。

---

### [](https://github.com/shadcn-ui/lint)

**原文标题**: [GitHub - shadcn-ui/lint: An agent-first linter for Tailwind design systems. Write design system rules that agents can verify. · GitHub](https://github.com/shadcn-ui/lint)

@shadcn/lint 是面向 AI 代理的 Tailwind 设计系统 linter，让团队用可验证规则约束 UI 生成，并在违规时给出基于组件、变体和主题的修复建议；兼容现有设计系统、Tailwind v4，不要求使用 shadcn/ui，并支持 ESLint 与 Oxlint。

- 🧭 核心目标：让代理编写 UI 时能验证设计系统规则，定义“什么允许、什么不允许”。
- 🛠️ 错误不仅指出违规，还会解释问题并建议符合组件、变体和主题的修复方式。
- 🔄 无需重写现有项目，适用于 Tailwind v4，shadcn/ui 不是必需条件。
- ⚡ 快速开始：让编码代理读取 SETUP.md 并完成安装配置，再选择规则和允许项。
- 🧩 对比 TypeScript：类型只能提示“不允许”，@shadcn/lint 会进一步告诉代理“应该怎么做”。
- 🧱 支持通过 allow、deny、contracts 为 Button、CardTitle、CardContent 等设置细粒度规则。
- 🤖 面向代理设计：错误包含问题、替代方案和查找位置，并支持自定义消息与占位符。
- 📊 超 150 次代理任务测试中，几乎都能在一轮修正后达到零违规。
- 📉 示例测试中，多个模型错误数从 42–117 降至 0，GPT 5.6 Sol 完成 6/8 任务。
- 💰 Claude 对照运行显示，使用 lint 反馈修复违规比仅靠规则便宜 10%–48%。
- 🧮 选择 linter 的原因：可编程、无需改组件、同一组件可配不同规则、可约束第三方组件、规则可跨项目共享。
- 📜 核心规则包括：no-restyle、no-raw-colors、no-arbitrary-values、no-inline-styles、no-unknown-classes、require-static-classes。
- ⚙️ settings.shadcn 可配置 ui、componentImports、ignoreImports、mergeFunctions、variantFunctions、note，并内置 cn、cva、tv 等函数支持。
- 🏢 Monorepo 可通过共享 UI 包前缀复用组件，并在包目录内覆盖或关闭规则。
- 📦 安装要求：Node.js 20.19+；Oxlint 1.80+ 或 ESLint 9.30+。
- 🪪 项目采用 MIT 许可，约 1.9k stars、31 forks、2 次提交。

---

### [发布 oxlint v1.83.0 与 oxfmt v0.68.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/apps_v1.83.0)

**原文标题**: [Release oxlint v1.83.0 & oxfmt v0.68.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/apps_v1.83.0)

oxc 项目发布 apps_v1.83.0，涵盖 Oxlint v1.83.0 与 Oxfmt v0.68.0；本次更新主要集中在 lint 规则适配与修复、性能优化、格式化器改进及文档更新。
- 🚀 发布：apps_v1.83.0 为最新版本，包含 Oxlint v1.83.0 和 Oxfmt v0.68.0，发布日期为 9 月 14 日，属不可变 release。
- ⚛️ Oxlint 特性：更新 React lint 规则，以适配 React 19.3 的变化。
- 🐛 Oxlint 修复：改进 unicorn 规则，如 prefer-array-flat-map 报告 `.filter().flatMap()`，prefer-at 报告单字符 `substring`，prefer-default-parameters 报告 `??=` 和 `||=`，prefer-array-flat 跳过普通 `concat` 归一化，prefer-global-this 保留 window 事件方法引用。
- 🧹 Oxlint 修复：eslint/no-unused-vars 尊重 rest params after-used 并保留 ambient implicit exports；typescript/prefer-for-of 处理计算集合；parser 拒绝构造函数重载的返回类型。
- ✅ Oxlint 其他：标记 no-unnecessary-type-parameters 与 prefer-find 建议为已实现，并改进诊断断言、文件路径和标签文本比较。
- ⚡ Oxlint 性能：大量规则减少临时向量与分配、惰性计算删除范围、短路检查，覆盖 jsx-pascal-case、catch-or-return、exhaustive-deps、no-unused-vars、no-undef 等。
- 📚 Oxlint 文档：为 typescript/await-thenable 的 Markdown 文档注释补充缺失的 lang。
- 🧩 Oxfmt 特性：formatter_core 新增 prefix_align builder 与 `Tag::(Start|End)Prefix`；formatter_test 增加 Prettier 动态 snippet 测试。
- 🔧 Oxfmt 修复：保留 enum member 尾随 suppress comment、统一 suppress comment 行为、JSX 单行注释保持 group flat、YAML `tab_width: 0` 夹为 1、`align(0)` 不 panic。
- 🛠️ Oxfmt 其他：修复 this_param、cast 目标赋值、注释参数模式、tsx-in-vue Fill；升级 oxc-yaml-parser 至 0.0.6；处理 less-test-suites 失败；更新文档说明。
- 📊 仓库状态：oxc 公开仓库约有 22.8k stars、1.3k forks、571 issues、343 PRs；页面多处显示加载错误，需刷新。
- 🎉 社区反应：发布获得 4 个 🎉、4 个 ❤️、2 个 🚀 反应，共 10 人参与。

---

### [更新日志.md | React Router](https://reactrouter.com/changelog#v840)

**原文标题**: [CHANGELOG.md  | React Router](https://reactrouter.com/changelog#v840)

这份文档是 React Router 官方发布记录，覆盖从 v7.0.0 到最新 v8.4.0 的变更日志，集中整理各版本新功能、破坏性变更、补丁、安全公告与实验性 API，便于跨大量版本搜索并避免 GitHub Releases 分页截断。

- 📚 文档说明：发布说明集中维护在本文件中，而不是 GitHub Releases 分页，以便搜索大跨度版本并查看完整长说明。
- 🏷️ 版本状态：最新稳定版为 8.4.0，main 未发布；版本导航包含 8.4.0、7.18.4、6.30.6、v4/5.x、v3.x。
- ⚡ v8.4.0：通过更细粒度的内部 data router contexts 减少路由组件重渲染，只有相关状态变化时才触发对应 hook 组件更新。
- 🧪 v8.4.0：新增 unstable 路由匹配优化，基于 @remix-run/route-pattern，100 路由约提升 19–38%，1000 路由约提升 71–88%。
- 🚧 v8.4.0：新增 unstable_validateParams 与 future.unstable_routePatternMatching，需调用 unstable_preloadRoutePattern()，参数校验失败会继续匹配后续路由。
- 🩹 v8.4.0：修复 stale route discovery、SPA 导航 lazy import 错误、RSC 重定向转义、视图过渡、内存泄漏、HTTPS 反向代理 action 提交等问题。
- ⚠️ v8.4.0：UNSAFE_ contexts 有破坏性变化；RSC Server Functions 应视为公开端点并自行做访问控制。
- 🔧 v8.3.1：修复 fetcher 中止、懒发现缓存、滚动恢复、useSubmit relative、URL 验证等；@react-router/serve 支持 .well-known/* 静态文件。
- 🧬 v8.3.0：更新不稳定 RSC 入口，支持 client version、子资源完整性、CSP nonce；路径参数编码按 RFC 3986 调整。
- 🌐 v8.2.0：非 Node 运行时框架模式默认使用 Web Streams 服务端入口；Node 应用可选 unstable_enableNodeReadableStream。
- 🤖 v8.1.0：create-react-router 可安装 React Router Agent Skill；可观测性元数据增强，instrumentation result.meta 提供 URL、pattern、params、statusCode。
- 🚀 v8.0.0：年度大版本，最低 Node 22.22.0、React 19.2.7、Vite 7；包改为 ESM-only，tsconfig target/lib 更新为 ES2022。
- 🔁 v8.0.0：多个 v8 future flags 行为成为默认，包括 trailingSlashAwareDataRequests、passThroughRequests、middleware、viteEnvironmentApi、splitRouteModules 等。
- ❌ v8.0.0：移除 react-router-dom，需改用 react-router 和 react-router/dom；同时移除 meta data 字段、Cloudflare dev proxy、architect useRequestContextDomainName 等。
- 🔐 v7.18.0：修复 CSRF 检查逻辑，改为基于 request URL host；反向代理部署可能需配置 allowedActionOrigins。
- 📈 v7.15.0：稳定大量 API，如 defaultShouldRevalidate、instrumentations、mask、passThroughRequests、url、useTransitions；路由匹配性能提升约 10–30%。
- 🛡️ v7.12.0：安全公告修复 CSRF、开放重定向 XSS、ScrollRestoration SSR XSS；新增 allowedActionOrigins。
- 🧱 v7.9.0：稳定 Middleware 和 Context API，包括 RouterContextProvider、createContext、getContext；修复 meta JSON-LD XSS。
- 🧪 v7.7.0：引入实验性 RSC Data Mode API，如 unstable_RSCHydratedRouter、RSCStaticRouter、createCallServer 等。
- 🧰 v7.5.0：新增 route.lazy 对象 API，可分别懒加载 loader、action、Component 等；移除 route.unstable_lazyMiddleware。
- 🔎 v7.2.0：新增类型安全 href 工具；预渲染支持 SPA fallback，并允许 SPA 模式根路由使用 loader。
- 🧭 v7.0.0：将 react-router-dom、@remix-run/* 等合并进 react-router，移除 json/defer 等 API，最低 Node 20、React 18，Remix Vite 插件成为标准。
- 🧯 安全修复贯穿多个版本，尤其 v7.12.0、v7.9.0、v7.5.2、v7.4.1、v7.9.6 等版本包含安全公告或 CVE 修复。
- 🧪 实验性功能汇总：RSC、middleware、高效路由匹配、URL masking、instrumentation、useRoute、useRouterState、fetcher.reset() 等均在 changelog 中持续演进。

---

### [Apollo Client 4.3 有哪些新功能 - Apollo GraphQL 博客](https://www.apollographql.com/blog/whats-new-in-apollo-client-4-3)

**原文标题**: [What's New in Apollo Client 4.3 - Apollo GraphQL Blog](https://www.apollographql.com/blog/whats-new-in-apollo-client-4-3)

overview summary
- 🚀 Apollo Client 4.3 于 2026 年 9 月 15 日发布，重点带来 TypeScript 改进与社区最期待的自定义标量支持。
- 🧠 新增类型安全缓存：通过扩展 `TypeOverrides` 并声明 `cache` 类型，访问 `client.cache`、`update(cache)` 等位置可获得准确缓存类型，无需反复类型断言。
- 📦 改进 GraphQL Codegen 增量类型：对 `@defer` 查询，在 `dataState` 为 `complete` 时移除条件分支，使用 `GraphQLCodegenIncremental.TypeOverrides` 即可获得更安全的数据类型。
- 🔧 支持自定义标量：可用 `Scalar` 集中定义 `parse`、`serialize`、`is`，并在 `InMemoryCache` 的 `scalars` 中注册，实现 JSON 值到原生对象的转换。
- ✅ 自定义标量可自动用于字段解析和变量输入：通过字段策略 `scalar` 选项解析字段，通过 `inputObjects` 配置复杂输入对象，使变量也可使用 `Date` 等解析后类型。
- ⚙️ 提供代码生成插件：`@apollo/client-graphql-codegen/custom-scalars` 可生成 `inputObjects` 与 `scalarTypePolicies`，减少手写配置和错误。
- 📡 为支持自定义标量，4.3 重做 `@defer`/`@stream` 缓存读取：引入数据剪枝，确保中间增量结果返回解析后的标量值，并让流式数据更可预测。
- 🔁 重写缓存冲突检测：不再跳过缓存写入，而是记录并比较缺失字段，避免无限重新获取，同时修复长期存在的相关问题，并新增警告辅助调试。
- 🧪 其他值得注意：最低 TypeScript 版本升至 5.9，`useSubscription` 支持 `skipToken`，`from` 选项可覆盖为更严格值。
- 📥 升级方式：运行 `npm install @apollo/client@latest`，完整变更可查看发布说明。

---

### [](https://react-hook-form.com/docs/useformstate/errormessage)

**原文标题**: [ErrorMessage | React Hook Form](https://react-hook-form.com/docs/useformstate/errormessage)

React Hook Form 自 v7.88.0 起提供 ErrorMessage 组件，用于渲染关联输入框的错误消息。它优先读取传入的 control prop，否则从最近的 FormProvider 获取表单状态，并支持通过 as 或 render 自定义错误展示，还可在 criteriaMode='all' 时渲染多条错误。

- 🧩 **组件用途**：自 v7.88.0 起提供，用于渲染关联 input 的错误消息。
- 🔌 **数据来源**：传入 control prop 时从该对象读取，否则从最近的 FormProvider 读取。
- 🏷️ **name**：必填 string，表示字段名，也可使用全局错误路径 root 或 root.*。
- 🎛️ **control**：可选 Control 对象，由 useForm 提供；使用 FormProvider 时可不传。
- 🏗️ **as**：可选 React.ElementType，用于包装组件或 HTML 标签，如 as="span" 或 as={Text}。
- 🖼️ **render**：渲染 prop，接收 { message: string, messages?: Object }，返回 React.ReactNode，用于自定义错误消息。
- ⚠️ **多条错误**：若要在 render 中使用 messages，需要将 useForm 的 criteriaMode 设置为 'all'。
- 📚 **示例覆盖**：包含单条错误消息、多条错误消息，以及与 FormProvider 搭配使用的示例。
- ⭐ **项目支持**：文档末尾邀请用户为 React Hook Form 在 GitHub 上点星支持。

---

### [Astryx v0.6.0：可响应的主题，可自适应的组件 · Astryx](https://astryx.atmeta.com/blog/astryx-v0-6-0)

**原文标题**: [Astryx v0.6.0: themes that respond, components that adapt · Astryx](https://astryx.atmeta.com/blog/astryx-v0-6-0)

Astryx v0.6.0 发布，带来响应式主题规则、可自适应选择器、Neutral 配色重做和六个新模板，并以规范驱动方式迈向 v1；升级需先将 Core 等稳定包安装到 0.6.0，再运行 CLI upgrade。

- 🎨 主题可在 CSS 中按视口宽度、指针精度、对比度和减少动态效果偏好调整令牌、组件样式、排版、颜色、圆角和动效，重叠规则以后者优先。
- 🧩 Selector 与 MultiSelector 新增 `presentation="adaptive"`，窄屏用底部弹层和触控行高，宽屏保持锚定弹窗，并支持空状态与 `isReadOnly`。
- 📦 新增五个向导模板和一个工作项详情模板：Checkout、Form、Dialog、Inline、Vertical Wizard 与 Work Item Detail。
- 🌈 Neutral 基于可复现的 OKLCH 调色板重建，语义、语法和分类色引用命名色阶，并更新按钮、状态面和信息横幅等视觉。
- 🛠️ 新增 OKLCH 调色板生成器，支持终端与 HTML 预览、类型化输出、自定义色阶、确定性生成记录和防覆盖。
- 📘 为迈向 v1，团队为组件和共享系统编写持久规范，明确公共 API、行为、无障碍、结构、主题目标和允许变化，作为审查与 agent 校验依据。
- ⬆️ 迁移需先安装 `@astryxdesign/core@0.6.0`、CLI 和相关主题到 0.6.0，再运行 `npx @astryxdesign/cli upgrade --from "$OLD_VERSION" --apply`。
- 🔄 迁移 codemod 处理焦点 Hook、IME 导入、Resizable 和 Selector；视觉属性和状态改用反射 `data-*` 属性，需检查自定义或动态选择器、Stepper、主题工具和预构建主题。
- 🐛 其他改进包括 Checkbox/Radio 列表项无障碍名称、TextInput/TextArea 转发 `autoComplete`、Popover 焦点保护、RTL 轮播渐变、CLI agent 指南与 doctor 检查、调试记录 `schemaVersion: 3` 等。
- 🙌 感谢 @AKnassa、@Astro-Han 等众多贡献者；完整包级说明见 Astryx v0.6.0 发布页。

---

### [](https://revopush.org/react-native-ota-payloads-binary-diffs?utm_source=this_week_in_react)

**原文标题**: [React Native OTA payloads: from 18 MB to 100-600 KB with binary diffs](https://revopush.org/react-native-ota-payloads-binary-diffs?utm_source=this_week_in_react)

Revopush Diff Updates 将 React Native OTA 从完整 JavaScript bundle 改为基于原生二进制的二进制补丁。某生产应用在 6 月 7 日迁移后，OTA 出口流量下降、下载增加、发布更频繁；一次发布中完整包为 18.7 MiB，而补丁仅为 117.26 KiB 到 611.49 KiB。Revopush 2.0 支持首个 OTA 即为 diff，并兼容 React Native 0.83+ 与 Expo SDK 55。

- 📉 迁移效果：某生产应用于 6 月 7 日采用 Revopush Diff Updates；此前偶有约 1–2 TB/天的出口流量，迁移后出口下降、下载上升、OTA 发布更频繁。
- 📦 单次发布体积：完整 OTA 包 18.7 MiB；生成的 JS 补丁为 117.26 KiB、586.94 KiB、611.49 KiB。
- 🔍 缩减幅度：最大补丁仍比完整包小约 31 倍，最小补丁小超过 160 倍；具体取决于版本改动。
- 🐢 OTA 初衷：OTA 本应让 React Native 发布更快，但每次推送完整 JS bundle 会让小修复变成大下载。
- 🚀 用户下载：100 KB 级补丁比 19 MB 包更容易在弱网、不稳定或计量网络中送达用户。
- ⚠️ 大包痛点：大 OTA 包在弱网、下载中断、后台下载受移动数据限制时易失败，小修复也会变成高带宽成本。
- 🧩 首包即 diff：Revopush 2.0 以 IPA/APK/AAB 中的原生 JS bundle 与资源快照为基线，首个 OTA 可直接生成补丁，无需先推完整 OTA 基线。
- 🛠️ 发布流程：先用 `release-native` 从原生二进制创建基础发布，再用 `release-react` 或 `release-expo` 发布 JS/资源更新；系统对比基线并生成补丁。
- ✅ 兼容支持：支持 React Native 0.83+ 与 Expo SDK 55；Expo 需原生配置，不能在 Expo Go 中运行，可用 prebuild、EAS Build 或自有原生流水线。
- 🎯 适用场景：大型 JS bundle、资源密集页面、频繁热修、用户网络弱，或希望降低 OTA 出口流量的团队。
- 📚 参考资料：Revopush 2.0 用户指南、Revopush Expo 集成文档、Expo CodePush with Revopush 2.0 指南。

---

### [Revopush — 终极 React Native OTA 更新平台](https://revopush.org/)

**原文标题**: [Revopush — The Ultimate React Native OTA Update Platform](https://revopush.org/)

Revopush 2.0 是面向 React Native 的 OTA 实时更新平台，提供完整云支持、CodePush SDK 兼容和从 App Center 的简单迁移，主打生产级 CI/CD、Diff 更新与发布分析能力。

- 🚀 核心定位：React Native OTA 终极方案，支持实时更新、全云支持、兼容 CodePush SDK，可从 App Center 轻松迁移。
- 🔌 广泛集成：支持 GitHub、Bitrise、CircleCI、Expo、Jenkins、Appcircle、Codemagic 等 CI/CD 工具。
- 📈 平台规模：99.9% 历史可用性，服务 3 亿 + MAU，每月 10 亿 + API 调用，3000+ 应用使用。
- 🧩 关键能力：开源客户端 SDK、CI/CD 集成、React Native 新架构支持、扩展发布分析、Diff 更新。
- 📦 Diff 更新：以应用商店二进制为基线生成快照，服务端只下发差异补丁；OTA 从 20–30 MB 降至 100–300 KB，更新体积小 10–20 倍。
- ⚙️ 生产就绪：代码签名、灰度发布、回滚、团队协作、CI/CD 自动化；支持 RN 0.76+ 与新旧架构。
- 📊 发布分析：提供清晰的灰度、安装和增量更新可见性，便于监控采用与回滚。
- 💰 定价：Starter 免费（1K MAU/10GB）；Startup $25/月（50K MAU/100GB）；Growing $100/月（300K MAU/1TB）；Business $250/月（500K MAU/2TB）；Professional $500/月（1M MAU/5TB）；Enterprise 定制。
- 💳 计费规则：按 MAU 和流量计费，超出后 $0.03/GB、$1/1000 额外用户；各付费档含 CI/CD 集成与部署分析。
- 🏢 Enterprise：不限发布/更新，CI/CD 集成，扩展安全与 SSO，优先支持，可部署在 AWS、GCP 或自有提供商。
- 📰 博客重点：与 Vanta 推进 SOC 2 Type II；AI Agent 集成；OTA 包从 18 MB 降至 100–600 KB；Expo CodePush；OTA vs 服务端驱动 UI；OTA 安全实践。
- 🔧 自动化更新：推出 CircleCI Orb、Bitrise Step、GitHub Action；CDN 优化使 OTA 更新快 3.5 倍。
- 🔄 迁移与自托管：提供从 App Center CodePush 迁移指南、CodePush 替代方案对比，以及独立 CodePush Server 安装指南。
- ❓ FAQ：兼容现有 CodePush SDK，支持流行 CI/CD；通常无需大幅修改 RN 应用或构建流程；有疑问可联系支持。
- ✅ 行动入口：可免费开始、预约演示、查看文档、访问 GitHub 仓库或联系团队选择 OTA 方案/规划迁移。

---

### [](https://shopify.engineering/back-to-native)

**原文标题**: [Native is now the future of mobile at Shopify (2026) - Shopify](https://shopify.engineering/back-to-native)

overview summary  
Shopify 宣布移动端战略转向：从 React Native 回归 Swift 和 Kotlin，因为编码智能体大幅降低原生双端开发成本；Shop 应用已在 12 周内完成原生重写，其他应用将陆续迁移，并同步调整开源库、构建 Helix 与 CLI 工具链。

- 📱 2020 年 Shopify 全力投入 React Native，成功节省重复开发、让非移动开发者参与、减少双端功能对齐成本。
- 🧠 2025 年仍看好 React Native，但 LLM 能力跃升改变核心假设，促使 Shopify 从第一性原理重新评估移动技术栈。
- 🤖 代理可用 iOS 版实现 Android 功能，反之亦然；帮助开发者跨栈上手，并通过共享规格、测试与审查降低双端对齐成本。
- 🧩 原生仍需双平台开发，但代理承担实现、翻译、测试和审查后，双端成本不再是决定性因素；原生更贴近平台能力与一方工具。
- 📦 React Native Skia：Shopify 赞助至 2026 年底，William Candillon 将继续开发并 fork 更名；FlashList 继续修复关键兼容问题并寻找长期维护者；Restyle 2026 年底后归档。
- 🚀 迁移选择 greenfield 从零重建，而非渐进式 brownfield；LLM 可参考 React Native 版本，清空历史约束，原型显示重建显著更快。
- 🛍️ Shop 应用首个迁移，借助 AI 从概念验证到发布原生版仅 12 周；Shopify 主应用（300+ 屏幕、小组件、Apple Watch、Siri Shortcuts 等）正在迁移，今年晚些发布；其他应用随后。
- 🧱 为防止 AI 生成不可维护的“slop”，构建 Helix：将屏幕拆成可审查 checkpoint，每个需测试、视觉匹配、两名对抗审查者及人工批准，反馈持续复用。
- ⚡ 模拟器控制是瓶颈；新架构将业务逻辑与 UI 解耦，可在桌面 headless 运行，并通过 CLI 让代理毫秒级检查状态、导航与操作；必要时远程驱动模拟器做快速 E2E。
- ✅ 目标迁移所有移动应用至 Swift/Kotlin，全程用 AI，但不降低性能、稳定性、可访问性与产品质量标准。
- 📈 成功指标包括产品交付速度、应用质量，以及代理能自主完成的工作量；将分享 Helix、代理可寻址架构等经验。
- 🙏 致谢 Meta React Native 团队、William Candillon、Software Mansion、Shopify 工程师及 React Native 社区，肯定 React Native 曾是 2020 年的正确选择。

---

### [](https://shopify.engineering/shop-app-migration)

**原文标题**: [Migrating Shop app from React Native to native (2026) - Shopify](https://shopify.engineering/shop-app-migration)

Shopify 将 Shop 应用从 React Native 迁移到原生 Swift 与 Kotlin，借助 AI 编码代理，仅用 12 周便从概念验证推进到正式发布；迁移显著改善了启动速度、稳定性、体积和性能，同时保持了用户连续性与分析事件兼容。

- 📱 Shop 应用服务数亿客户和数百万商家，自 2020 年起深度采用 React Native。
- 🤖 编码代理的进步改变了共享移动代码库的权衡，使团队重新评估完全原生开发。
- 🧪 一周概念验证：一名工程师用编码代理将现有 React Native 应用迁移为 SwiftUI 原生 iOS 应用，证明可行。
- 👥 正式迁移由 6 名核心工程师搭建原生基础与主要用户旅程，功能团队中途加入验证边缘情况。
- 🔁 迁移需像普通更新：用户保持登录、继续收到推送，交互与分析事件需兼容下游系统。
- 🧹 团队借迁移简化应用，退役部分屏幕并精简其他界面。
- ⚡ 冷启动：iOS 从 3200ms 降至 2466ms，减少 23%；Android 从 4433ms 降至 2233ms，减少 50%。
- 🛡️ 会话稳定性从 99.5%+ 提升至 99.95%+，崩溃会话减少约 10 倍。
- 📦 应用体积：Android 减少 109MB（-37.2%），iOS 增加 1MB（+1.5%）。
- 🏗️ 构建时间：Android 发布构建约减少 75%，iOS 大致持平。
- 🎞️ Android 在滚动信息流和导航时达到 120 FPS，且优化极少。
- 🧭 经验：采用多代理会话、清晰任务、快速构建测试循环与频繁审查，并构建可复用迁移工作流和 Pi 扩展。
- 🔍 开发 Tardis 调试工具，让代理访问实时事件、日志和状态，并支持截图与事件窗口对比。
- 🧠 原生专业知识仍不可或缺，用于避免重复代码、架构漂移和性能问题。
- 🚀 未来 iOS 与 Android 必须始终保持功能对等，当前原生版成为性能新基线，团队将继续优化。

---

### [](https://codewithbeto.dev/blog/is-react-native-dead-shopify-native)

**原文标题**: [Is React Native Dead? What Shopify's Move to Native Actually Means | Code with Beto | Code with Beto](https://codewithbeto.dev/blog/is-react-native-dead-shopify-native)

overview summary
Shopify 宣布将移动应用从 React Native 迁回 Swift 和 Kotlin，引发“React Native 是否已死”的讨论。作者认为 React Native 并未死亡；Shopify 的迁移是 AI 降低双原生实现成本、平台 API 价值上升下的个案，数据亮眼但变量混杂，AI 工作流仍离不开原生专业知识和严格验证。

- 🏢 Shopify 宣布把移动应用从 React Native 迁回 Swift/Kotlin，Shop 应用已完成迁移，其余应用随后跟进。
- 📱 Shop 的迁移从概念验证到上架仅用 12 周：1 周 iOS 原型、6 名核心工程师，部分屏幕被删除或简化，并保留登录、推送和分析行为。
- 📊 Shopify 报告称：iOS 冷启动 3200ms→2466ms，Android 冷启动 4433ms→2233ms，Android 包体 293MB→184MB，Android 构建时间约缩短 75%，iOS 包体仅增加 1MB，稳定性提升到 99.95%+。
- ⚠️ 这组比较同时改变语言、架构、依赖和产品，且未与采用 New Architecture 的 React Native 版本对比，因此不能当作通用 React Native 基准。
- 🤖 迁移原因之一是 AI 代理降低了分别维护 Swift 和 Kotlin 实现的成本，同时直接访问平台 API 与工具变得更重要；但 Shopify 2020 年迁向 React Native 曾成功，2025 年回顾仍积极。
- 🧩 代理工作流不能一次性重写整个应用；Helix 将工作拆成小检查点，要求测试、视觉对比、两名代码审查者和人工批准，并把业务逻辑与 UI 分离。
- 📈 AI 也可能提高对工程师的期望：实现变快后，工程师可能被期待跨 iOS/Android 审查维护，节省的时间可能转为学习、审查和承担更多职责。
- 🛠️ Expo、Software Mansion、Codemagic、Bitrise 等同时支持原生与 React Native；Expo UI 可用 SwiftUI/Jetpack Compose，SDK 56 支持内联原生模块，说明支持原生不等于放弃 React Native。
- 📱 Apple 的 iPhone Duo 折叠屏显示平台集成的重要性：系统组件更易适配，但自定义 UI、新 SDK 和具体新 API 仍需实际验证。
- 📦 开源包方面：React Native Skia 的 Shopify 赞助持续到 2026，William Candillon 计划 fork 并换新包名；FlashList 会修复关键兼容问题并讨论长期维护；Restyle 计划归档，2026 年后停止维护。
- ✅ 作者结论是 React Native 未死：深度依赖平台集成可考虑 Swift/Kotlin，受益于共享代码则 React Native 仍合理；已有应用应先测量具体问题，再决定是否重写。
- 🎯 最值得保持的技能，是无论实现放在哪里，都能发布并维护一个优秀的移动应用。

---

### [面向所有企业的 AI 客户支持平台 - Crisp](https://crisp.chat/en/?utm_source=twir&utm_medium=newsletter&utm_campaign=crisp_q3_nl&utm_content=16sep26)

**原文标题**: [The AI Customer Support Platform for Every Business - Crisp](https://crisp.chat/en/?utm_source=twir&utm_medium=newsletter&utm_campaign=crisp_q3_nl&utm_content=16sep26)

Crisp 是一个 AI 优先的全方位客户支持平台，核心 AI 支持代理 Hugo 可帮助企业自动化客户服务，整合全渠道沟通、知识库、CRM、分析与自动化，让支持、营销和销售团队更高效地服务客户，已有 10,000 家公司使用。

- 🤖 全新 AI 支持代理 Hugo：作为团队最得力的 AI 支持队友，自动处理客户咨询。
- ⚡ AI 可自动化约 50% 的客户咨询，让团队专注于更重要的事务。
- 🧩 一体化套件：覆盖 AI Agent、AI 聊天机器人、共享收件箱、CRM、营销活动、分析、知识库、工单系统和状态页。
- 📥 全渠道共享收件箱：集中网站、邮件、WhatsApp、Messenger、Instagram 等渠道消息，团队可协作管理并高效回复。
- 🛠️ 4 步构建 AI Agent：训练 AI、创建工作流、测试并部署、验证与衡量，支持无代码构建器和模板库。
- 💬 聊天组件：几分钟内嵌入网站或 Web/移动应用，实时支持访客和客户，引导转化。
- 📚 知识库：创建和管理帮助文章，打造符合品牌的自助帮助中心。
- ⚙️ 自动化：通过无代码内部工作流加速团队回复并减少重复性人工操作。
- 🗂️ 支持 CRM：同步潜在客户和客户数据，结合历史互动实现更个性化的沟通。
- 📊 支持分析：按日监控团队支持表现，发现优化点，提升服务质量。
- 👥 适用场景：客户支持、入站销售和营销团队，可跨渠道支持、自动化销售流程、再营销客户。
- 🏢 客户信任：Emma、Hoxton Mix、Reedsy 等公司给出积极评价，认为 Crisp 灵活、自动化强、聊天组件出色。
- 🚀 试用与定价：14 天免费试用，无需信用卡，包含所有 Crisp 功能；采用扁平定价，降低每代理成本。
- 🇫🇷 欧洲制造：Crisp 来自法国，在欧洲构建。

---

### [发布 0.88.0-rc.1 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.88.0-rc.1)

**原文标题**: [Release 0.88.0-rc.1 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.88.0-rc.1)

React Native v0.88.0-rc.1 是预发布版本，由 react-native-bot 于 9 月 16 日发布，包含 main 分支 153 次提交，重点涉及 EventTarget API、Web 事件派发、Hermes/React 升级以及 iOS Codegen/SwiftPM 修复。
- 🚀 版本为 v0.88.0-rc.1 预发布，提交哈希 05a41cd，发布时间 9 月 16 日 09:35。
- 📊 仓库约有 127k Star、25.3k Fork、703 个 Issue、437 个 PR。
- ✨ 新增：在 canary 的原生视图 ref 上启用命令式 EventTarget API：addEventListener、removeEventListener、dispatchEvent。
- 🔁 更改：启用基于 Web 的事件派发重构，Hermes 升级至 260318099.0.3，React 同步至 19.3.0。
- 🍏 iOS Codegen：发现组件时不再爬取 node_modules 或跟随符号链接。
- 📱 SwiftPM：生成的 manifest 从 IPHONEOS_DEPLOYMENT_TARGET 推导 iOS 最低版本，不再硬编码 iOS 15，支持 Expo 16.4 等依赖自动链接。
- 🧩 SwiftPM：从 podspec 读取 SwiftPM 名称并写入 package.json；生成构建脚本改用 bash 运行，避免 /bin/sh 非 bash 环境问题。
- 🐞 提供 Hermes V1、ReactNativeDependencies、ReactNative Core 的 Debug/Release dSYMs。
- 🛠️ 可通过 Upgrade Helper 升级，完整变更见 CHANGELOG.md；问题或 PR 可提交到发布页。
- ⚠️ 页面多次提示加载错误，需要重新加载。

---

### [](https://expo.dev/blog/build-ios-apps-on-windows-with-cloud-simulators)

**原文标题**: [You don't need a Mac to develop iOS apps anymore â Expo blog](https://expo.dev/blog/build-ios-apps-on-windows-with-cloud-simulators)

未检测到需要总结的正文内容，因此无法提炼文章要点。请提供文本后，我会生成简洁的中文摘要。

- 📭 当前消息在“Use following content:”之后为空，没有可总结的文章。
- 📝 请补充或粘贴完整文本，我将提取核心信息并生成摘要。
- 📌 摘要将采用“概述 + - emoji 要点”的指定格式。
- 🌐 输出语言为中文，确保简洁、准确、易读。

---

### [](https://shift.infinite.red/legend-state-the-fastest-react-state-library-youre-probably-not-using-e791171a61b7?gi=61d3ea11a05f)

**原文标题**: [Medium](https://shift.infinite.red/legend-state-the-fastest-react-state-library-youre-probably-not-using-e791171a61b7?gi=61d3ea11a05f)

Legend State 是由 Jay Meistrich 开发的 React Native 状态管理库（现处于 3.0 beta 阶段），旨在解决 React 内置状态管理（useState、useContext）在性能上的根本性缺陷。作者 Darin Wilson 通过 Jay 在 Chain React 2026 的演讲内容，深入介绍了该库的设计理念、性能优势及延伸功能，并认为它有望成为开发者未来选择状态库时的重要竞争者。

- 🚨 **问题根源在于状态**：Jay 在为多家公司优化性能后发现，列表并非最大瓶颈，React 内置的 useState 和 useContext 才是严重性能问题的源头。

- ⚠️ **useState 的双重身份缺陷**：它同时"创建"和"订阅"状态，导致父组件即使只是传递值、并不使用该状态，也会被迫随状态变化而重渲染，memo 和编译器优化都无能为力。

- 🌐 **useContext 的"广而不深"**：任何 context 值变化都会让所有消费者重渲染，即便它们并不使用变化的那部分；拆分 provider 又会陷入层层嵌套的"Provider 地狱"。

- 📉 **性能差距惊人**：在每秒更新四次的计时器基准测试中，把 useState 放在应用根部的版本比放在叶子组件的版本慢了 10 倍。

- 🔄 **核心思路：状态不该住在 React 里**：Legend State 将"创建状态"和"订阅状态"彻底分离，用 observable（也称 signal）承载状态，observable 本身稳定不变，只通过 set() 或 assign() 变更内部节点。

- 🎯 **精细订阅机制**：通过 useValue 配合选择器函数，组件只订阅自己真正需要的那部分状态；在 500 首歌曲的播放列表中切换曲目时，500 个选择器都会重跑（纯字符串比较，在 React 之外执行），但只有结果变化的两个组件会触发渲染。

- 🧩 **更细粒度的响应式组件**：Legend State 提供以 `$` 为前缀的响应式内置组件（如 `$View`），可接收响应式 props（如 `$style`），使组件仅在挂载时渲染一次，之后只更新内部的小片段，彻底改变"组件"的传统定义。

- 🎨 **语法虽怪但非必须**：Jay 本人承认高性能特性语法"看起来陌生甚至吓人"，但这些只是可选优化项，默认的标准用法已经足够快，仅建议在热路径组件上使用。

- 🔧 **额外能力**：`useObserveEffect` 替代 useEffect，由状态更新（而非渲染）触发，消除易错的依赖数组；状态变更携带新旧值与路径，由此衍生出撤销/重做功能（由 Infinite Red 的 Jamon Holmgren 贡献）以及离线优先的同步引擎，支持多种后端且配置代码极少。

---

### [](https://andrei-calazans.com/posts/2026-09-14-how-kmp-with-swiftui-scales-on-ios/)

**原文标题**: [How Does KMP with SwiftUI Scale on iOS? • Andrei Calazans](https://andrei-calazans.com/posts/2026-09-14-how-kmp-with-swiftui-scales-on-ios/)

overview summary
- 🧩 iOS 上的 KMP 共享层无论拆成多少 Gradle 模块，最终都链接成一个静态 XCFramework，因为多个框架会各自嵌入 Kotlin/Native 运行时与 GC。
- 🧪 实测环境：Apple M4 Pro、Xcode 26.5、Kotlin 2.4.0、Gradle 9.6.1，真实项目约 750 个 Kotlin 文件 + 700 个 Swift 文件，并辅以合成项目验证。
- 🏗️ 冷启动构建模拟器框架约 80 秒、74 个任务；无操作热构建约 0.5 秒，但配置缓存失效会升至约 14 秒。
- 🔁 改一个共享 Kotlin 文件时，编译按模块 fan-out 只重编译变更模块及其依赖者：1 个依赖者约重编 2 个模块，7 个依赖者约重编 8 个模块。
- ⛓️ 但 umbrella link 每次变更都完整重链接，固定约 12 秒，构建缓存无法避免，因为链接输出不能像编译输出那样跨输入变化复用。
- 📈 链接成本随总链接代码线性增长：约 9 ms/1000 symbols，R²=0.996；模块数量本身不影响，第三方依赖也计入链接预算。
- 📱 真实框架约 93 MB、289k symbols，其中约 50k 来自 ktor、coroutines、serialization、SQLDelight 等依赖。
- 🛡️ SwiftUI 功能层只依赖 Swift closure-struct 合约；699 个 Swift 文件中仅 78 个 import Shared，其中 26 个在 SharedBridge，因此 Kotlin ABI 变化只重建约 10% 的 Swift 文件（91/932）。
- ⚡ 开发循环：改 SwiftUI 约 4 秒；改共享 Kotlin 约 30 秒，其中约 12 秒模拟器链接、约 10 秒设备架构链接、约 8 秒 Xcode/Swift 边界重建。
- 🧰 最大杠杆是保持功能层不 import 框架；其次本地只构建模拟器 slice 可省约 6 秒、为编译缓存拆分模块、稳定高 fan-out 叶子模块、保持配置缓存健康、修剪共享依赖。
- ❌ 已验证无效：静态与动态框架对链接时间几乎无差；把固定代码拆成更多小模块不会缩小链接。
- 🧭 结论：单框架链接是真实且随共享层增长的成本，但通过 Swift 合约边界可把 Kotlin 变更的爆炸半径限制在约 10% 应用代码内；未来若需突破，可考虑运行时隔离的多框架或 Bazel/远程链接缓存。

---

### [](https://codewithbeto.dev/blog/is-your-app-ready-for-iphone-duo)

**原文标题**: [Is Your App Ready for iPhone Duo? | Code with Beto | Code with Beto](https://codewithbeto.dev/blog/is-your-app-ready-for-iphone-duo)

苹果推出首款折叠 iPhone——iPhone Duo，为 iOS 应用带来可变屏幕空间、折叠折痕、安全区与多任务分屏等新适配挑战。开发者应使用 Xcode 27.1 和 iOS 27.1 SDK 重建应用，并借助响应式布局、系统组件和真实场景测试，让应用在开合、旋转、分屏和折叠状态下都自然可用。

- 📱 Apple 正式推出首款折叠 iPhone：iPhone Duo，折叠硬件首次进入 Apple 移动生态。
- 🛠️ 新应用或现有应用都应先用 Xcode 27.1 与 iOS 27.1 SDK 重建；旧 SDK 应用可能只占内屏窄区域，浪费空间。
- 📐 不要依赖固定宽度，使用尺寸类和响应式布局，让侧边栏、多列视图随可用空间出现或收起。
- 🔄 支持旋转、部分折叠、分屏等变化；同一产品在不同窗口形态下应保持熟悉，而非重做多个界面。
- 🧭 重视安全区：按钮、输入框和导航控件应留在安全区内，背景等视觉元素可延伸到边缘。
- 🧩 使用 SwiftUI 的 ConcentricRectangle 或 UIKit 的 UICornerConfiguration 等同心性 API，让 UI 曲线贴合屏幕。
- 📖 折叠时避免把重要控件放在折痕附近；文章、列表等可滚动内容更适合穿过该区域。
- 🧱 优先使用系统组件：工具栏、标签栏、表单、分栏视图、弹出菜单、警告等可自动适应设备形态。
- ✅ 按真实使用方式测试：打开、合上、折叠、旋转、分屏，并检查侧边栏残留、按钮靠近折痕、空白过多或不必要导航。
- ⚛️ React Native 开发者可使用 Expo Router 和 Expo UI 的原生 API，无需自行检测折叠状态。

---

### [](https://swmansion.com/blog/what-it-actually-takes-to-migrate-discord-to-react-native-s-new-architecture/)

**原文标题**: [What It Takes to Migrate Discord to RN's New Architecture](https://swmansion.com/blog/what-it-actually-takes-to-migrate-discord-to-react-native-s-new-architecture/)

Discord 将 iOS 应用迁移到 React Native 新架构的实战复盘。文章重点不在如何"打开开关"，而在于切换之后的长尾问题：数百个问题被归结为渲染/布局、崩溃稳定性、构建基础设施、性能和输入五大类，其中渲染与布局独占 47%，而真正的迁移工作仅占 14%。核心洞见是：老代码并没有错，是脚下的地基变了——坐标系原点、视图原生标识、原生类名查找这些隐式契约在新架构下被打破。作者通过三个典型案例（模态框坐标偏移、手势目标视图失效、类名后缀缺失导致死锁）说明症状与根因往往相隔甚远，真正的成本在于定位而非修复。文章最后给出迁移团队的五条建议：为长尾做准备、关注原生边界、为调查而非修复留出预算、先测量再优化、尽可能在上游修复问题。

- 🏗️ Discord 的 RN 应用规模罕见，迁移按平台推进（先 Android 后 iOS），Software Mansion 团队耗时近一年协助 iOS 端完成新架构迁移
- 📊 迁移后的问题分布揭示了真相：渲染/布局/视觉占 47%，崩溃稳定性 16%，构建/基础设施 14%，性能 13%，输入 11%——真正的架构切换只占约七分之一
- 📐 "相同坐标，不同原点"：旧架构下视图测量基于窗口，Fabric 下相对于 Yoga root（模态框自成一个 root），导致 FullWindowOverlay 中的上下文菜单在模态框内打开时位置偏移
- 🎙️ "未完成的手势"：视图扁平化按 props 每次提交重新评估，辅助功能属性的切换会让容器在原生树中"消失又出现"，导致录音手势中途失效、松手后无法停止
- 🥶 "冻结应用的类名"：遗留 view manager 类名缺少 Manager 后缀，interop 层快路径查找失败，背景线程与主线程因注册表读写锁互相等待而死锁，靠三行重命名规避
- 🧭 三个契约被打破的共同本质：代码本身没变，是位置原点、原生视图身份、原生类名查找这些隐式假设在新架构下不再成立
- 🔬 排查方法闭环：崩溃报告管道按签名分类、专用性能仪表盘对比前后版本、CI 持续编译新架构、用真实设备复现而非"代码合并即算修复"
- 🔁 "完成"是移动目标：并行的其他迁移会带来新架构特有的怪癖，修复往往需要本地打补丁或升级 RN 版本，两者各有权衡
- 🌍 回馈生态：作为 Reanimated、Screens、Gesture Handler 的维护者，问题若出自库便在上游修复，惠及所有依赖项目；但多数问题其实在 Discord 自有代码中
- ✅ 给迁移团队的五条建议：为长尾而非切换本身做规划、盯紧与原生交互的边界、预算花在调查而非修复上、先埋点测量再优化、尽可能把修复推到上游

---

### [](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

**原文标题**: [Codemagic Patch | Self-hosted OTA updates for React Native](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

Patch 是 Codemagic 推出的自托管 OTA 更新方案，基于其运行数十亿次 OTA 更新的经验，主打一键部署、CDN 级扩展、零停机和完整的发布管理。

- 🚀 定位：以最简单的方式自托管 OTA 更新，高效架构可轻松服务数百万用户。
- 🐳 一键部署：使用 Docker Compose，一条命令即可在任意机器部署完整技术栈。
- 📈 轻松扩展：架构专为百万级用户设计，无需额外扩容工作。
- 🛡️ 零停机：检查和下载都走 CDN，即使服务崩溃也不会中断更新交付。
- ⚙️ 完整控制：提供现代托管 OTA 服务的全部功能，同时避免高额费用。
- 📲 灵活更新：支持应用后台静默安装，也可对紧急补丁使用立即更新。
- 🌐 可靠交付：CDN 带来 99% 可交付率，小包体适合弱网下载。
- 📊 发布监控：Web 仪表板支持发布、指标、团队访问、受控推广和版本采用图表。
- 🧪 自行运行：一条命令启动本地评估栈，附演示应用，并可部署到 VM 用于生产。
- 🆚 对比优势：其他自托管 OTA 常需自行处理扩展与缓存，API 故障会阻塞检查；Patch 通过 CDN 扩展，仅 CDN 故障才影响交付，并支持立即、重启、恢复、暂停等安装时机。
- 🏢 背景：由拥有 10 年以上移动 CI/CD 经验的 Codemagic 构建。

---

### [](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.10.0)

**原文标题**: [Release v0.10.0 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.10.0)

React Native ExecuTorch v0.10.0 是一次从底层重写的重大版本，围绕模块化 TypeScript 流水线、硬件加速、Worklet 线程和按需原生二进制进行重构，同时保持与 v0.9 的 100% 功能对等并提供迁移路径。
- 🚀 发布 v0.10.0：全面重写整个库，旨在提升开发体验、降低延迟并减少电池消耗。
- 🏗️ 两层架构：透明 TypeScript 流水线与任务 Hooks，加上低层 Core API；可检查每一步、定制流程、串联多模型，无需编写 C++。
- ⚡ 硬件加速：iOS 支持 Core ML（ANE/GPU，70+ 模型变体）和 MLX（Metal，近 40 个 LLM 导出），Android 支持 Vulkan（25+ 导出），并保留优化多线程 XNNPACK CPU 回退。
- 🧵 Worklet 线程：与 react-native-worklets 紧密集成，原生 JSI 函数和核心原语默认带 `"worklet"`，可脱离主 JS 线程或直接在 UI worklet 中执行，便于 VisionCamera 实时视觉。
- 📦 按需二进制：安装时按需下载原生二进制和后端委托，默认零配置；可在 package.json 中仅选择所需后端或任务，减少安装、构建时间和应用包体积。
- 📱 展示应用：新增 React Native ExecuTorch Gallery，用于体验端侧 AI 的实际运行速度。
- ⚠️ 迁移兼容：提供 `react-native-executorch/legacy` 入口保留旧 API，支持逐步迁移，但该模块已弃用并将在未来版本移除；官方附有迁移指南。
- 📚 文档更新：新增视觉、语音、NLP 任务指南，高级运行时教程和完整 API 参考。

---

### [](https://expo.dev/changelog/sdk-58-beta)

**原文标题**: [Expo SDK 58 Beta is now available — Expo changelog](https://expo.dev/changelog/sdk-58-beta)

SDK 58 beta 今天开始，预计持续 3 至 4 周，面向 iOS 27，内置 React Native 0.88 RC，并带来场景生命周期、Expo UI、Expo Router、Expo Modules 2.0 beta、EAS Observe、Agent CLI、Android 小组件、SwiftPM 基础、构建与调用性能提升，以及多项破坏性变更。开发者应尽快升级测试，并用正确模板反馈问题。

- 🚀 **Beta 周期**：SDK 58 beta 持续 3 至 4 周，期间持续发布修复与改进，供开发者验证兼容性与回归。
- 📱 **iOS 27 支持**：SDK 58 为 iOS 27 构建，可立即上架支持 iOS 27；包含 React Native 0.88 RC，稳定版发布后将很快推出正式 SDK 58。
- 🧪 **Expo Go**：SDK 58 版 Expo Go 今天仅通过 Expo CLI 支持 Android 设备/模拟器和 iOS 模拟器，通过 `eas go` 支持 iOS 真机；商店版将在稳定版后更新。
- 🍎 **iOS 27 适配**：iOS 27 要求 UIKit 场景生命周期并支持应用调整大小；Expo 已采用场景生命周期，需阅读迁移指南，且 `requireFullScreen` 与方向锁定行为有变化。
- 🛠️ **EAS Build**：带 Xcode 27 和 SDK 58 工具链的 EAS Build 镜像即将推出，目前最新镜像仍使用 Xcode 26.6。
- 🖥️ **Device Hub**：Xcode 27 用 Device Hub 替代 Simulator.app；Expo CLI 可检测并启动它，`expo-device-hub` 插件可在浏览器中管理模拟器/模拟器流。
- 🗣️ **App Intents**：`expo-app-intents` alpha 可将 Siri、快捷指令、Spotlight 和 Apple Intelligence 的 App Intents 暴露给 Expo 应用。
- 🎨 **Expo UI**：文档新增组件截图；iOS 增加 NavigationStack、Toolbar 等，SwiftUI/Compose 增加多种修饰符与组件，并修复 RNHostView 测量与触摸问题。
- 📊 **EAS Observe**：已正式可用；`expo-observe` 新增集成、错误边界、`expo-image` 集成与 `Observe.clientId`，`AppMetrics` 被弃用。
- 🤖 **Agent CLI**：新实验性 `@expo/agent-cli` 面向 AI agent，提供 `status`、`dev`、`smoke`、`skills:sync` 等命令，基于 Expo CLI、EAS CLI 和 expo-doctor。
- 📦 **Android 小组件**：`expo-widgets` 新增 Android 实现，小组件使用独立 Hermes 运行 JS bundle；iOS Live Activities 增加 `staleDate` 等能力。
- 🧩 **Swift Package Manager**：SDK 58 为 Expo 应用使用 SwiftPM 打基础，Expo iOS 源码已拆分 SwiftPM targets；CocoaPods 仍是默认且受支持路径。
- ⚡ **Expo Modules 性能**：Android `expo-modules-core` 提供预编译 `.so`，清洁构建约减半；iOS 简单值调用、长字符串与 Promise 创建/解析均更快。
- 🧬 **Expo Modules 2.0 beta**：可用普通 Swift/Kotlin 类加注解暴露原生模块，替代 DSL；同步调用比 1.0 快 2.5 至 5.6 倍，Android 微基准也优于 TurboModules。
- 🔍 **Fingerprint 默认**：SDK 58 默认使用 `balanced` 预设，减少因版本号或 `node_modules` 文件变化导致的不必要原生重建。
- 🦀 **Rust 转换器实验**：实验性“Noxcturnal”基于 Rust/oxc，单模块转换约快 3 倍，冷打包约快 2 倍；通过 `experiments.noxcturnalTransformWorker` 开启。
- 🧭 **Expo Router**：data loaders、SSR、middleware、原生 tabs、toolbars 和标准导航集成均已稳定；导航核心重构，部分 API 移动或移除，需看迁移指南。
- 🌐 **开发服务器与隧道**：代理/隧道连接更可靠；新隧道基于 `@expo/ws-tunnel` 2.0，更快更稳且不再需要 `@expo/ngrok`；端口选择更一致。
- ⚛️ **React Native 0.88 RC**：从 0.86 升级到 0.88 RC，涵盖 0.87 与 0.88 RC 变化，包括 SPM 工具、`fontVariationSettings`、TurboModules 的 ArrayBuffer、DevTools 等。
- 📈 **PostHog 集成**：可用 `eas integrations:posthog:connect` 一键接入，事件可关联 EAS update、build、channel 和 runtime version。
- 📝 **其他更新**：相机文档扫描、文件摘要/预览、音频锁屏与 WAV 录制、图片 SVG 变量、SecureStore 确认、通知改进、定位重写预览等。
- 🗑️ **弃用项**：`File.md5`、`NativeArrayBuffer`、`AppMetrics`、`useLibSQL`、`backgroundOverlay` 等被弃用或替换。
- ⚠️ **破坏性变更**：RN 严格 TypeScript API 默认、iOS 场景生命周期、`NODE_ENV` 与环境文件行为、Android R8 默认开启、`File.write()` 异步、libSQL 移除、前台通知默认显示等。
- 🔧 **工具版本**：Expo 工具要求 Node.js 22.13+、24.3+ 或 26+，不支持 23/25 等奇数版；Expo modules 工具兼容 AGP 9。
- ✅ **已知回归**：目前暂无报告，beta 期间会更新。
- 📣 **试用与反馈**：可用 `create-expo-app` 新建项目，或用 `npx expo install expo@next --fix` 升级；建议 `prebuild --clean` 后运行 iOS/Android，并用正确模板提交最小复现问题。

---

### [屏幕地图](https://screenmap.dev/)

**原文标题**: [Screenmap](https://screenmap.dev/)

Screenmap 是一个面向 Expo / React Native 应用的 GitHub Action 与本地工具，可自动映射应用全部屏幕，并在 PR 中展示改动涉及的屏幕截图、交互式全图与前后对比；它运行在现有 CI 中，支持 iOS/Android，并可通过多种编码代理与配置灵活使用。

- 🗺️ 核心功能：自动发现路由与屏幕，截图 PR 触及的屏幕，并发布带完整地图链接的 PR 评论。
- 📸 PR 评论：列出新增、修改、删除的屏幕，并标注变化来自哪个路由或源文件。
- 🔍 交互式地图：点击任意屏幕可查看路由和源文件，改动屏幕会被高亮。
- ↔️ 前后对比：展示旧版与新版截图，并标出发生移动或变化的部分。
- 🧩 全应用覆盖：地图包含所有屏幕，而不只是写了 Storybook 或测试的组件。
- 🤖 CI 集成：在 GitHub Actions 中运行，截图包可推送到仓库分支或保留为运行产物。
- 🆓 开源免费：MIT 许可，只需支付 CI 分钟数和代理 API 费用。
- 📱 平台支持：iOS 在 macOS runner 上捕获，Android 在 ubuntu-latest 上捕获，后者成本约为前者的十分之一。
- 🔀 双平台合并：CI 中每个作业只跑一个平台，之后可把 iOS/Android 包合并为一张带切换器的地图。
- 🧠 代理支持：默认 Claude Code，也支持 Codex、Gemini、OpenCode，或自定义命令与 API key 变量。
- ☁️ 即将支持：可通过 argent cloud 与 Expo 托管模拟器运行 iOS，无需自建 macOS runner。
- ⚙️ 安装方式：让代理添加两个工作流：screenmap-pr.yml 与 screenmap-baseline.yml。
- 🔐 必需秘密：EXPO_TOKEN 用于 EAS 构建或复用 dev client；代理 API key 可选，用于探索无记录路径。
- 🧪 EAS 准备：项目需链接 EAS，并具备可产出 iOS 模拟器 .app 或 Android .apk 的构建配置；也可直接传 app_path 跳过 EAS。
- 📁 Monorepo/私有仓库：用 project: apps/mobile 指向子目录；私有仓库设 publish: "false" 保留为运行产物。
- 🧭 配置：.screenmap/config.json 可设置 scheme、平台、设备、参数、等待时间、agent、effort 等，所有键都可选。
- 🔗 路由参数：/brew/[id] 等路由需要真实 id，否则会落到 not-found；可在 params 中按全局或单路由配置。
- 📝 SKILL.md：可选，用于告诉代理如何登录测试账号、避免危险操作、处理慢屏等待等。
- 🎚️ Effort 等级：deterministic 不耗 token；fast 只查无记录路径；balanced 为默认；thorough 检查所有截图屏幕。
- 💻 本地使用：通过 Claude Code 插件运行 /screenmap，生成 .scrmap 文件并在查看器打开；支持 --static、--platform both、replay、pr 等。
- ⏱️ 运行时间：仅 JavaScript 改动约 12 分钟；若原生代码变化，需额外加 EAS 构建。
- ✅ FAQ：无需先写测试；不会破坏构建；兼容 bare React Native（需 expo-router 或 react-navigation 路由表）；Linux 上用 tesseract OCR，识别词较少。
- 🆚 与 Storybook 区别：Storybook 测你写 story 的组件，Screenmap 测真实应用，包括没有 story 的屏幕。
- 🌐 试用：提供 Bluesky 客户端的在线演示地图，可直接在浏览器查看。

---

### [](https://github.com/software-mansion/react-native-screens/releases/tag/4.28.0)

**原文标题**: [Release 4.28.0 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/4.28.0)

react-native-screens 发布了 4.28.0 最新版本，由 kmichalikk 于 9 月 14 日 11:10 发布（提交 2381ed8，已验证签名），自上一版本以来主分支有 136 个提交。此次为小型版本，主要带来多项 Bug 修复和少量杂项维护。仓库 software-mansion/react-native-screens 为公开项目，当前约 3.7k Star、712 Fork、178 Issues、124 PR。

- 🐞 修复 Android Tabs：处理 forceLayout，确保配置变更后标签栏正确布局（#4582）
- 🐞 修复 Android Stack v4+：追加 SwipeRefreshLayout 过渡填充（#4519）
- 🐞 修复 Android Tabs：使用 ViewIdGenerator 识别 MenuItems，替代顺序 ID（#4558）
- 🐞 修复 Android Stack v4：从不透明屏弹出到半透明屏时，阻止添加预加载和已关闭的 Fragment（#4571）
- 🐞 修复 Android Tabs：将 tab item 的 testID 暴露为 viewIdResourceName（#4497）
- 🐞 修复示例：将 Kotlin 升级到 2.3.*（#4536）
- 🐞 修复 Android：RNSScreenRemovalListener 作为 mounting override delegate 注册后的 use-after-free 问题（#4413）
- 🧹 杂项：修复 FormSheet 场景中的 import type（#4647）
- 🧹 杂项：消除 iOS release 构建警告（#4486）
- 📦 该版本包含 2 个 Assets
- 🚀 版本获得反应：❤️ 2、🚀 5，共 5 人参与
- ⚠️ 页面多次出现加载错误提示，需重新加载页面

---

### [Swift 6.4 发布 | Swift.org](https://www.swift.org/blog/swift-6.4-released/)

**原文标题**: [
       Swift 6.4 Released | Swift.org 
    ](https://www.swift.org/blog/swift-6.4-released/)

Swift 6.4 于 2026 年 9 月 15 日发布，旨在让 Swift 更适合从应用到服务器、系统代码、嵌入式设备和浏览器的全栈开发，并让日常代码更易写；重点包括 Swift Build 成为 SwiftPM 默认构建系统、Subprocess 1.0、互操作扩展、WebAssembly 加速、嵌入式能力增强、性能与内存安全改进，以及调试、IDE 和测试工具更新。

- 🗓️ Swift 6.4 正式发布，由 Joe Heck 与 Holly Borla 撰写，发布日期为 2026 年 9 月 15 日。
- 🧱 Swift Build 成为 Swift Package Manager 默认构建系统，使 Linux、macOS、Windows 项目构建方式一致。
- ⚙️ Subprocess 库达到 1.0，提供稳定、跨平台的方式运行和交互子进程，并基于 Swift 并发构建。
- 🌉 互操作增强：Swift 的 Span 可直接桥接 C++20 的 std::span；Swift/Java 互操作扩展 async、回调、Runnable、可变参数和 record 支持。
- 🌐 WebAssembly 性能提升：JavaScriptKit 到 Wasm 的安全桥接最高快 40 倍，Wasm SDK 可直接从 Swift.org 安装。
- 📟 Embedded Swift 更强大：支持 existential types（如 any Protocol）和更丰富的错误处理，并新增 EmbeddedRestrictions 警告。
- 🧹 代码更简洁：可选 some/any 类型无需括号；@diagnose 控制警告；模块选择器解决 API 冲突；defer 块可等待 async；withTaskCancellationShield 保护清理任务不被取消。
- 📚 核心库与测试：ProgressManager 支持 async/await，@Observable 支持细粒度通知；Swift Testing 与 XCTest 更易迁移混用，支持重复测试和附件。
- 🧠 性能与内存安全：UniqueBox、UniqueArray、Iterable、Ref/MutableRef、withTemporaryAllocation、RawSpan 安全加载等减少拷贝与分配，同时保持内存安全。
- 🐞 工具链改进：LLDB 精确跟踪 Swift 模块，调试构建和 dSYM 显著缩小；SwiftPM 支持生成 SPDX/CycloneDX 格式 SBOM。
- 💻 IDE 支持扩大：VS Code Swift 扩展上线 Open VSX，兼容 Cursor、Antigravity、Kiro 等，并集成 Swiftly 管理工具链。
- 🤖 Android 支持推进：Swift SDK for Android 使用 LTS NDK 30，Swift Build 在 SwiftPM 中支持 Android，无需安装后脚本。
- 📖 文档与获取：Swift 文档站点上线，标准库文档开源；可通过 Install Swift 页面或 Swiftly 下载 6.4 工具链。
- 🙏 感谢社区贡献；可通过 Swift 论坛参与后续开发。

---

### [](https://github.com/react/metro/releases/tag/v0.87.1)

**原文标题**: [Release v0.87.1 · react/metro · GitHub](https://github.com/react/metro/releases/tag/v0.87.1)

Metro v0.87.1 是 react/metro 的最新发布版，由 robhogan 于 9 月 13 日发布，对比 v0.87.0...v0.87.1，包含新功能、修复、性能优化、类型改进和实验性变更；贡献者为 robhogan、vzaidman 和 OskarEichler。

- 🚀 发布：v0.87.1 为最新标签，commit c7597f8，发布于 9 月 13 日 10:34，页面提供 2 个 assets。
- ✨ 新功能：新增 resolver.schemeResolvers，可用自定义解析器解析 URI scheme 前缀说明符（如 foo:bar）。
- ✨ 新功能：将 metro:babel-runtime/<path> 导入解析到 Metro 自带的 @babel/runtime。
- ✨ 新功能：metro-babel-transformer 通过 caller 向 Babel 预设传递 inlinePlatform。
- 🔐 修复：用 vendored 解析器替换 image-size 依赖，修复 CVE 告警。
- 🌐 修复：开发服务器为文本资产和源文件设置 Content-Type 时包含 charset=utf-8。
- 🐛 修复：常量内联时保留 Platform.OS 写入目标，并内联静态 Platform.select 对象字面量中最后一个重复键。
- 👀 修复：FallbackWatcher 不再漏掉目录爬取期间写入该目录的文件。
- 🔄 修复：HttpStore 处理写入期间的 socket 错误并重试，避免进程崩溃。
- ⚙️ 修复：CI=false 和 CI=0 视为非 CI；仅从 process.env.CI 检测 CI，移除 ci-info 依赖。
- 🔥 修复：开发环境中使用 lazy（分段）bundle 时，Fast Refresh 不再命中未定义模块。
- ⚡ 性能：FallbackWatcher 移除 walker 依赖，爬取 RSS 降低约 34%，峰值堆降低约 41%。
- ⚡ 性能：不再为无依赖模块生成冗余空依赖映射数组。
- 🧩 类型：恢复发布 TypeScript 声明中的私有（下划线前缀）字段；修复 async 函数被推断为返回 void；整理生成类型并允许更多可空属性省略。
- 🧪 实验性：metro-file-map 新增 crawlerFactory；serializer 新增 unstable_inlineDependencyMap 和 unstable_getAsyncDependencyPath；移除 transformer.unstable_renameRequire；修复 experimentalImportSupport 的 export * from 默认导出再导出。
- ⚠️ 实验性功能不受 semver 保障，可能随时变化。
- 👥 贡献者：robhogan、vzaidman、OskarEichler；完整变更日志见 v0.87.0...v0.87.1。

---

### [](https://github.com/margelo/react-native-nitro-zxing)

**原文标题**: [GitHub - margelo/react-native-nitro-zxing: ZXing Barcode Scanner for react-native-vision-camera written in C++ · GitHub](https://github.com/margelo/react-native-nitro-zxing)

margelo/react-native-nitro-zxing 是一个为 react-native-vision-camera v5 提供条码扫描的 React Native 库，基于 zxing-cpp 和纯 C++ Nitro HybridObjects 实现，主打高性能、原地解码且无需 ML Kit。

- 📷 面向 VisionCamera v5，可直接在相机帧上扫描条码。
- ⚙️ 纯 C++ Nitro HybridObjects，在相机亮度平面上原地解码；无需 ML Kit、base64 或临时文件。
- 📦 安装命令：npm install react-native-nitro-zxing react-native-vision-camera react-native-nitro-modules react-native-nitro-image。
- 🧩 使用 useBarcodeScanner 与 useFrameOutput，pixelFormat 设为 yuv，在 worklet 中调用 scanner.scanCodes(frame) 并 dispose。
- 🔄 API 与 react-native-vision-camera-barcode-scanner 类似。
- ⚡ 基准：实时 1280×720 YUV 13.1ms 对比 ML Kit 34.4ms（快 2.6 倍）；3060×4080 照片 21.7ms 对比 59.3ms（快 2.7 倍）；256×256 QR 0.95ms 对比 9.7ms（快 10.2 倍）。
- 📊 仓库数据：74 stars、5 forks、0 issues、3 PR、6 commits；MIT 许可证。
- 📁 主要目录包括 packages/react-native-nitro-zxing、apps/example、config、scripts、agents、.github 等。

---

### [](https://lynxjs.org/blog/lynx-4-0)

**原文标题**: [Lynx 4.0: AI-Generated UI, ReactLynx Dynamic Elements, Foldable Device Support, and More Open-Source Elements - Lynx](https://lynxjs.org/blog/lynx-4-0)

Lynx 4.0 已发布，重点带来 AI 生成 UI、ReactLynx 动态元素、统一调试元数据、折叠设备适配、CSS 与桌面端能力增强，并将 `<webview>`、`<blur-view>` 等元素开源，帮助开发者更高效地构建跨平台原生体验。

- 🚀 Lynx 4.0 正式发布，支持用 AI 构建界面、在 ReactLynx 中动态创建元素，并能追踪生产错误与运行时 UI 节点。
- 🤖 `lynx-api-docs` Agent Skill 让 AI 代理查阅 Lynx API、CSS、布局和 Elements 文档，减少生成不支持的 Web 写法。
- 🧩 Lynx A2UI 让模型输出结构化协议消息，Lynx 在运行时渐进渲染为原生 UI，并支持用户交互回传。
- ✨ `lynx-a2ui` Skill 可读取应用能力目录，生成符合组件、函数和参数约束的 A2UI 消息。
- 🧠 OpenUI 技能可用自然语言生成 OpenUI Lang v0.5 程序，并通过 `<OpenUiRenderer>` 支持流式生成、响应式状态和工具调用。
- ⚛️ ReactLynx 新增 `createElement` 和 `cloneElement`，可在运行时动态创建或克隆元素；已知静态结构仍推荐 JSX 以优化渲染。
- 🐞 统一 `debug-metadata.json` 汇集 JS/CSS source map、字节码调试信息和 UI source map，可将生产错误和 UI 节点映射回源码或 JSX。
- 🧭 UI source map 默认关闭，需在 `pluginReactLynx` 中设置 `enableUiSourceMap: true`；生产构建默认删除元数据，需自行保留并托管。
- 📱 折叠设备支持：宿主同步 screen metrics、viewport 和 GlobalProps，前端继续用 Flex 布局与相对单位自动适配，已在 TikTok 生产使用。
- 🎨 CSS 媒体查询实现 CSS Media Queries Level 4 子集，支持 `@media`、`min-`/`max-`、`and`/`or`/`not`、范围语法如 `width >= 768px`。
- 🖥️ 桌面端 CSS 在 macOS 和 Windows 的 Clay 后端新增 `-x-caret-*` 自定义文本光标与 `mask-composite` 多层蒙版合成。
- 🌐 `<webview>` 开源，可在 Android、iOS、HarmonyOS、macOS、Windows 嵌入网页，支持 `src` URL 或 `html` 字符串，需显式设置宽高。
- 💧 `<blur-view>` 开源，支持 Android、iOS、HarmonyOS，可为覆盖层后方内容添加高斯模糊；Android 需配合 `android-capture-target` 和 `flatten={false}`。
- 📊 全局 Lynx 内存查询在 iOS 和 Android 可用，可异步收集存活实例内存，并按 Elements、UI/Views、主线程/后台线程 runtime 等分类。
- 🛠️ 升级方式：将 Lynx 与 PrimJS 依赖更新至 `4.0.x`，并安装目标平台支持依赖；完整更新见 Lynx 4.0 release notes。

---

### [发布 v0.10.0 · wcandillon/react-native-webgpu · GitHub](https://github.com/wcandillon/react-native-webgpu/releases/tag/v0.10.0)

**原文标题**: [Release v0.10.0 · wcandillon/react-native-webgpu · GitHub](https://github.com/wcandillon/react-native-webgpu/releases/tag/v0.10.0)

概述：react-native-webgpu 发布 v0.10.0，主要包含 Chrome/154 与 SPM 支持、Android view 选项更新，以及设备同步和销毁示例相关修复。仓库热度为 1.2k Star、70 Fork、30 Issue、11 PR。

- 🚀 发布 wcandillon/react-native-webgpu v0.10.0，由 github-actions 于 2026-09-10 发布，包含 8 个提交并合并至 main。
- ⭐ 仓库数据：1.2k Star、70 Fork、30 Issue、11 Pull Request、0 安全与质量项。
- 🐛 修复：升级至 Chrome/154 并支持 SPM（#471）。
- 💥 修复：新增“detach 前设备销毁失败”的示例（#470），关闭 #468。
- 📲 修复：默认开启隐式设备同步（#467）。
- 🤖 功能：更新 Android view 选项（#457）。
- 📦 资源：本次发布附带 3 个资源。
- ⚠️ 页面部分区域提示加载错误，可重新加载后查看。

---

### [发布 v3.3.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v3.3.0)

**原文标题**: [Release v3.3.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v3.3.0)

react-native-gesture-handler 发布 v3.3.0 版本，由 m-bert 于 9 月 11 日发布，包含 7 个提交。本次更新以大量缺陷修复为主，覆盖 iOS、Android、Web 及 Reanimated 集成等多个平台，同时包含若干杂项改进、测试增强、文档更新和依赖升级。该仓库目前拥有 6.8k 星标和 1.1k 分支，本次发布还迎来了 8 位新贡献者。

- 🆕 发布版本为 v3.3.0，标记为 Latest 最新版本，基于主分支的 7 个提交
- 🐛 核心修复：保持 ReanimatedSwipeable 原生处理器在事件回调变化时的稳定性
- 📱 修复 PressableWithTouchable 中将按压处理器转发为 testOnly_* 的问题
- ⚙️ 仅在启用 Reanimated 检测器时才传入 reanimatedEventHandler
- 🤖 Android 修复：滚动接管触摸时按钮误触发按压事件
- 🤖 Android 修复：原生处理器错误地附加到嵌套按钮而非检测器子组件
- 🎨 修复 ReanimatedDrawerLayout 重新渲染后的动画速度问题
- ⌨️ 修复键盘属于原生输入框时 "never" 模式下按压失效的问题
- 🪝 原生端不再向 Reanimated hooks 传递依赖项
- 🌐 Web 端改为依据真实滚动（而非指针距离）激活 ScrollView 原生手势
- 🍎 iOS 修复：检测器视图被回收时分离手势处理器
- 🔲 转发 android_ripple 的 borderless 和 foreground 属性
- 🤖 Android 修复：避免等待中的父处理器取消其等待的子处理器
- 🌐 Web 修复：完整配置替换时重置 NativeViewGestureHandler 配置、恢复 enabled 状态并刷新 DOM
- 👆 useTapGesture 中 shouldCancelWhenOutside 默认为 true
- 🔄 重置 LongPressGestureHandler 中的 numberOfPointers
- 🖱️ 重置 Web 端 PanGestureHandler 的 enableTrackpadTwoFingerGesture
- 🍎 iOS 修复：按钮命中测试限制在自身子树内，并在按钮禁用时取消进行中的按压
- 🤖 Android 修复：按钮被禁用时释放按压
- 🌐 Web 修复：手势进行中处理器被禁用或从未启动时从编排器中移除
- 🧹 修复 Web 端 GestureStateManagerType 的循环导入问题
- 🍎 iOS 修复：在 box-none 父级下保留禁用的按钮目标
- 🎡 重置 Web WheelEventManager 中累积的滚轮增量
- 🤖 Android 修复：原生处理器手势结束时停止嵌套滚动
- 🔢 杂项：移除旧版 Reanimated 检查、提前初始化 Handler 字段、使用稳定版 Reanimated 与 Worklets
- 🧪 测试增强：新增基础点击、长按、嵌套触摸、共享值、计时器等 e2e 测试，并加入 Argent 端到端测试流程
- 📚 文档更新：增加 JSON-LD 和 llms.txt 以支持 AI 搜索、更新兼容性表格、添加隐私政策链接
- ⬆️ 依赖升级：joi、svgo、colord、nanoid、fast-uri 等多个包由 Dependabot 更新
- 🎉 新贡献者：antFrancon、Sullyvahnn-v2、halskiszymon、ngocdevv、giaBaoJS、AlexRixten、rileysay、roryabraham 共 8 人首次贡献
- 👥 本次发布共有 j-piasecki、huextrat 等 12 位贡献者参与

---

### [发布 v2.12.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.12.0)

**原文标题**: [Release v2.12.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.12.0)

这是 Shopify/react-native-skia 的 GitHub Releases 页面，显示最新版本 v2.12.0（2026-09-16）的发布信息；仓库热度较高，页面部分内容因加载错误未能正常显示。该版本主要包含多项 Bug 修复，并新增 iOS Swift Package Manager 支持，同时附带 3 个资源文件。

- 📦 Shopify/react-native-skia 发布最新版本 v2.12.0，由 github-actions 于 2026-09-16 08:38 发布（commit 172fcad，已签名验证）。
- ⭐ 仓库数据：约 8.6k Star、646 Fork，另有 42 个 Issues、49 个 Pull Requests。
- 🍏 新特性：为 iOS 增加 Swift Package Manager（SPM）支持（#4043）。
- 🌎 Bug 修复：修正虚假的 undefined 测试（#4053）。
- 🌐 Bug 修复：布局效果清理时不再丢失 Canvas WebGL 上下文（#4002）。
- 🌐 Bug 修复：向 PathBuilder 添加圆形时正确传递 isCCW（#4047）。
- 🐛 Bug 修复：当 x 或 y 为 0 时不再丢弃 ImageSVG 偏移量（#4050）。
- 🐯 Bug 修复：处理无效的 SVG 解析结果（#4065）。
- 🗿 Bug 修复：修复默认 Skia graphite 纹理用法（#4064）。
- 📎 发布版本附带 3 个资源文件；页面出现“加载错误，请重新加载”的提示。

---

### [](https://github.com/kuatsu/react-native-boost/releases/tag/v2.0.0)

**原文标题**: [Release Release 2.0.0 · kuatsu/react-native-boost · GitHub](https://github.com/kuatsu/react-native-boost/releases/tag/v2.0.0)

React Native Boost v2.0.0 是一次重大版本发布，核心变化是从 Babel 插件迁移到新的 Metro 配置插件，并带来多项优化器、Uniwind 支持、React Native 0.88 兼容以及运行时一致性改进。
- ⚠️ 从 Boost 1.x 升级时，需要将 Babel 插件迁移到新的 Metro 插件，详见文档。
- ⚙️ 引入 Metro 配置插件，取代 Babel 插件，为实现多项新功能打基础。
- 🚀 新增五个优化器，覆盖 Animated、ActivityIndicator、StyleSheet、Platform 等组件与代码。
- 🎨 新增 Uniwind 支持，在优化组件时保留样式。
- 🧠 减少 bail-out，可跨文件分析祖先组件和辅助函数。
- 🖼️ 改进 Image 优化，更好支持静态源、回调和无障碍属性。
- 🛡️ 提升运行时行为一致性，修复大量边缘情况以贴近纯 React Native。
- 📱 支持 React Native 0.88，并基于最新 RC 验证运行时一致性。
- 🧰 配置更清晰，优化器、集成、假设与日志统一为开发者友好的 API。
- ✨ 其他特性包括 ActivityIndicator 优化、动画值懒创建、Platform 分支折叠、静态无障碍属性预计算等。
- ⚡ 性能改进包括减少 Metro 冗余转换与分析、优化静态图片源、预处理 selectionColor、构建时解析版本行为。
- 🐛 修复类型错误、文本上下文保留、平台折叠、React Compiler 兼容及 RN 版本矩阵兼容等问题。
- 📊 仓库当前约 565 stars、14 forks、2 issues、0 个 pull requests。

---

### [](https://github.com/DorianMazur/react-native-screen-choreography/releases/tag/v0.5.0)

**原文标题**: [Release 0.5.0 · DorianMazur/react-native-screen-choreography · GitHub](https://github.com/DorianMazur/react-native-screen-choreography/releases/tag/v0.5.0)

react-native-screen-choreography v0.5.0 已发布，重点引入类型化共享元素过渡、原生正向准备与性能追踪，并改用实时共享内容模型；同时修复过渡稳定性问题，并包含从 0.4.x 迁移的破坏性 API 变更。

- 📅 DorianMazur 于 9 月 10 日发布 v0.5.0，包含 19 个提交到 main。
- ⭐ 仓库当前有 166 Star、4 Fork、0 Issues、4 Pull Requests。
- 🧩 新增 `defineTransition`，用于类型化共享元素角色和伴随进入/退出动画，并提供可复用导航选项。
- 🎛️ 新增 `useSharedElementPresentation`，让保留内容可根据折叠/展开端点和过渡进度调整内部布局。
- 📱 新增 iOS/Android 原生正向准备，包括目标布局稳定性检查和批量目标测量。
- 📊 新增准备追踪、Android 性能基准与 CI 报告。
- 🛠️ 改进过渡启动、保留内容布局和反向导航协调。
- 🛡️ 强化原生准备取消、待处理目标可见性及中断过渡处理。
- 🖼️ 更新 Gallery、Wallet、Wallet Setup 示例与集成文档。
- ⚠️ 0.4.x 升级为破坏性变更：全程使用实时共享内容，只保留一个内容所有者和空接收端点。
- 🔁 API 重命名：`SharedElement.Live`→`SharedElement`、`SharedElement.LiveTarget`→`SharedElement.Target`、`makeLiveTransition`→`makeTransition`、`StandInContainer`→`TransitionSurface`、`StandInElement`→`TransitionFrame`。
- 🏷️ 类型重命名：`LiveSharedElementProps`→`SharedElementProps`、`LiveSharedElementTargetProps`→`SharedElementTargetProps`、`MakeLiveTransitionOptions`→`MakeTransitionOptions`、`LiveTransition`→`Transition`、`LiveTransitionRendererProps`→`TransitionRendererProps`、`LiveTransitionSide`→`TransitionEndpoint`。
- 🧹 移除 `createSharedElementComponent`、`makeSurfaceTransition`、`makeStretchTransition`、`textMorphTransition`，改用 `defineTransition` 或 `makeTransition` 自定义渲染器。
- 🧱 过渡展示不再携带复制的 React 内容或 stand-in/live 模式；自定义渲染器必须精确渲染库持有的 portal host `children` 一次。
- 🔄 升级后需重建原生应用以启用原生正向准备；iOS 需重装 pods，旧二进制仍保留 readiness fallback。

---

### [发布 v](https://github.com/callstackincubator/react-native-harness/releases/tag/v1.5.0)

**原文标题**: [Release v1.5.0 · callstackincubator/react-native-harness · GitHub](https://github.com/callstackincubator/react-native-harness/releases/tag/v1.5.0)

react-native-harness v1.5.0 发布，重点增强可测试性、CI CLI、平台级 Metro 配置，并修复进程清理、跳过测试显示、Windows 支持与资源锁并发问题。

- 🚀 新增可注入文件系统上下文和内存文件系统辅助，用于封闭式 Harness 集成与测试（#169、#165）。
- 🧰 CLI 新增 `harness ci <subcommand>`，包括 `load-config`、`plan-metro-restore`、`snapshot-metro`、`plan-metro-save`，供官方 GitHub Action 通过项目已安装的 CLI 执行配置与 Metro 缓存步骤。
- 🔐 GitHub Action 通过安装包能力标记检查 CLI 是否支持该接口，而非版本号；需保持 Action ref 与 `react-native-harness` 包版本同步。
- 🧩 平台包可通过 `metroConfigEnhancer` 调整 Harness 组装的 Metro 配置，把模块解析重定向、resolver platforms 和核心初始化放入平台包；未设置者无变化（#190、#187）。
- 🧹 修复：限制 Harness 拥有的 CLI 进程，取消运行后不会残留 console、logcat 或 XCTest 子进程（#181）。
- ✅ 跳过测试现在会在 Jest 输出及兼容结果消费者中显示为 skipped（#182）。
- 🪟 支持 Windows 主机和 React Native Windows 平台：Windows 上可加载 ESM 配置，`Platform.OS === 'windows'` 可完成 bridge 握手（#187）。
- 📦 新增 `@react-native-harness/platform-windows`，可配置 `windowsPlatform({ name, packageName })`，通过 `Get-AppxPackage` 解析包族名、按 AUMID 激活并按进程名跟踪；需先部署应用（#187）。
- 🔧 Windows 平台包自带 Metro wiring：`react-native -> react-native-windows` 重定向、`windows`/`native` resolver.platforms 和 `InitializeCore`；`windowsPlatform()` 不再需手改 `metro.config.js`，iOS/Android 不受影响（#187）。
- 🔒 资源锁改进：心跳刷新写入失败不再触发 unhandled rejection，锁会过期回收；`getResourceLockKey` 现在生效，同平台不同设备可并发，仅共享设备等待（#187）。
- ❤️ 感谢贡献者 Marc Rousavy、Stanislav Doskalenko、Szymon Chmal 等。

---

### [](https://github.com/callstackincubator/voltra/releases/tag/v2.3.0)

**原文标题**: [Release v2.3.0 · callstackincubator/voltra · GitHub](https://github.com/callstackincubator/voltra/releases/tag/v2.3.0)

v2.3.0 是 callstackincubator/voltra 的版本发布，核心是服务端驱动的动态小组件、Android 可配置小组件、实验性 iOS 动态实时活动，以及 Android ArcProgressIndicator；同时包含大量 Android/iOS/CLI/CI 修复、文档与重构更新。

- 🚀 发布 v2.3.0：由 github-actions 于 9 月 15 日 06:42 发布，自上一版以来 main 分支有 6 个提交，发布提交为 e14e70c。
- 🌐 服务端驱动动态小组件：小组件可按计划、按放置位置从服务器获取自身 props，不再依赖 App 推送更新。
- ⚙️ Android 可配置小组件：每个已放置小组件可通过 setWidgetInstanceConfiguration 保存独立设置（如伦敦/纽约），并在启动器备份/恢复后保留。
- 📱 iOS 动态实时活动（实验性）：实时活动可由小型 JSON prop 更新驱动，而非每次完整重新渲染，并支持构建时热重载。
- 📊 Android ArcProgressIndicator：新增确定性弧形仪表组件，支持配置描边宽度、角度、圆头/平头与渐变填充。
- 🐛 Android 修复：支持 Android 7.0-11（API 24-30）小组件，修复 NewApi lint、minSdk、widget minWidth/minHeight、resize bounds、applicationId/namespace、widget kind 与 Dynamic 占位读取等问题。
- 🍏 iOS 修复：在小组件时间线重载期间保留上次服务器响应、将 activityBackgroundTint 应用到小尺寸 Dynamic Live Activities、新增 widget kind 选项以跨迁移保留小组件、修复配置插件丢弃 URL schemes。
- 🛠️ CLI/构建改进：按构建配置应用/接受 iOS 值、生成 widget bundle 时导入 VoltraRuntime、从包元数据推导 Voltra 版本。
- 🧹 文档与重构：精简/去重/拆分 v2 文档，新增服务端驱动 Dynamic Widgets ADR，拆分 payload-driven 与 Dynamic widget 代码，支持在 widget 代码中导入 react-native。
- 📈 图表：y 轴按数据缩放，并新增 yScale prop。
- ✅ CI：对任意 base 分支的 PR 运行 CI，Android Lint 失败会使构建失败。
- 👥 贡献者：新贡献者 @Minishlink（#259）与 @rlods（#272），主要贡献者包括 V3RON。
- ⭐ 仓库状态：公开仓库，824 stars、41 forks、31 issues、9 pull requests；2 个资源，1 个 👍 反应。
- ⚠️ 页面多次出现加载错误提示，需刷新页面。

---

### [](https://github.com/software-mansion/radon-ide/releases/tag/v1.19.0)

**原文标题**: [Release v1.19.0 · software-mansion/radon-ide · GitHub](https://github.com/software-mansion/radon-ide/releases/tag/v1.19.0)

Radon IDE v1.19.0 已发布（9 月 10 日 16:04，commit 33ed58f），核心亮点是让 AI agent 共享 Radon 已启动的设备，并带来 Expo/依赖处理、构建重试与多项稳定性修复。

- ✨ **发布信息**：software-mansion/radon-ide 发布 v1.19.0 最新版，由 mateuszaliyev 发布，commit 为 33ed58f，并带有 GitHub 验证签名。
- 🤝 **AI agent 设备共享**：Radon 现将已启动设备共享给 Argent，agent 会连接当前正在查看的模拟器，而不是再启动第二个模拟器。
- 📸 **Agent 能力**：通过 Radon 已有连接，agent 可使用截图、手势、粘贴文本、无障碍树、原生 profiler 和原生视图层级。
- 📦 **Expo Prebuild 调整**：不再覆盖 git 跟踪的 `ios/` 或 `android/` 原生目录，并支持一键将偏好保存到启动配置；也可用 `usePrebuild` 强制行为。
- 🧪 **Expo Go 依赖检查**：选择 Expo Go 前会检查依赖；若应用使用 Expo Go 不包含的原生模块，则改用 development build，并警告相关包。
- ✅ **启动参数支持**：`expoStartArgs` 或 `start` 脚本中的 `--dev-client` 和 `--go` 现在会被正确遵循。
- 🔁 **依赖安装纳入构建流程**：`node_modules` 安装成为构建管线一部分；`Retry` 会安装依赖，Pod 失败也会提示缺失依赖是根因。
- 🛠️ **Expo 配置修复**：修复使用 `app.config.ts` 等配置文件名时被误判为 bare React Native，导致 config plugins 未运行的问题。
- 🔗 **iOS 深链修复**：修复深链被 `Open in "App"?` 确认框拦截，无法到达应用的问题。
- 🧰 **Redux DevTools 修复**：修复 Redux DevTools 面板完全不渲染的问题。
- ⚙️ **nvm 修复**：修复项目没有 `.nvmrc` 时，项目命令从不使用 nvm 的问题。
- 🚑 **Retry 修复**：修复 `Retry` 无法恢复早期启动失败，且真实错误被内部错误替代的问题。
- 📊 **React Profiler 修复**：修复会话未记录 re-render 时 React Profiler 静默无响应，现在会明确提示。
- 🧱 **安装错误修复**：修复 `node_modules` 安装失败被误报为成功，并在之后才以构建错误暴露的问题。
- ⌨️ **远程输入修复**：修复在远程流式设备上打字时按键丢失和卡住的问题。
- 🧯 **模拟器/视频修复**：修复模拟器服务器关闭崩溃、视频管线内存所有权 bug，以及服务器存活并 reset 所有连接的问题。

---

### [发布 v0.25.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.25.0)

**原文标题**: [Release v0.25.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.25.0)

overview summary
- 🚀 software-mansion/argent 发布 v0.25.0，由 github-actions 于 09 Sep 15:10 发布，包含自上一版以来的 45 个提交。
- 🔀 多项 flow 更新：重构每个步骤类型的读取方式，并让目录中运行的每个 flow 都在 stdout 给出判定。
- 🧩 新增能力：连接外部提供商提供的设备，将本地或外部脚本作为 flow 步骤运行，并记录脚本步骤。
- 📱 Android 支持在 `describe` 中读取 WebView 内的 Web DOM；tool-server 的 await 工具支持 ios-remote。
- 📊 遥测增强：在工具事件的 platform 旁报告 device_kind。
- 🧪 测试改进：调整空闲与 type-focus 等待测试，减少测试与进程环境、系统临时目录之间的污染，并固定遥测 wire format。
- 📝 文档与优化：精简 README 和 flow-run 描述，将部分指令移至参考文件，禁用 CodeRabbit 高层摘要。
- 🔢 所有版本号提升至 0.25.0。
- 👥 新贡献者包括 @mateuszaliyev 和 @kasperski95；主要贡献者包括 kasperski95、latekvo 等 6 人。
- 📦 发布包含 2 个资产，完整变更对比为 v0.24.0...v0.25.0。

---

### [](https://github.com/callstack/agent-device/releases/tag/v0.21.2)

**原文标题**: [Release v0.21.2 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.21.2)

overview summary
- 🚀 callstack/agent-device 发布 v0.21.2，重点是减少导航步骤，并提升捕获、录制和会话出错后的恢复能力。
- 🧭 新增 `scroll <direction> --until <selector>`，可用一条命令查找屏外元素；滚动保持在键盘上方，卡住时停止边缘滚动。
- 🔐 iOS 可原地自动化 `ASWebAuthenticationSession` 登录表，无需离开应用或取消认证会话。
- 📸 快照与等待结果更有用：跨平台披露截断捕获，iOS 常规快照遵循 `--depth`，等待遇到可重试拒绝会继续轮询。
- 🎥 录制恢复更可靠：重试 `record stop` 会返回已完成导出，模拟器启停更安全，Android 陈旧录制证据不再阻塞下一次录制，并报告实际捕获时长。
- 🧩 Maestro 支持 `evalScript` 内联 JavaScript 表达式；导出流程保留 `tel:` 和 `mailto:` 链接，回放结果生成规范 JUnit XML。
- 🔄 会话更能承受中断：匹配已安装版本可复用同一 daemon，重启设备可清除陈旧声明，已接纳任务保留租约；BrowserStack 分配和取消云屏幕读取处理更一致。
- 🛠️ 此版本包含大量修复、重构、性能优化和文档更新，并迎来多位新贡献者；完整变更见 v0.21.1...v0.21.2。

---

### [](https://github.com/appandflow/stim/releases)

**原文标题**: [Releases · appandflow/stim · GitHub](https://github.com/appandflow/stim/releases)

该内容为 appandflow/stim 的 GitHub Releases 页面，汇总了从 v1.4.0 到 v1.0.0-rc.20 的版本发布说明、功能更新、修复、迁移注意事项与 QA 情况；页面加载时出现错误提示，但版本列表与资产信息仍可见。

- 📦 仓库 appandflow/stim 当前显示 47 stars、1 fork、4 issues，发布列表包含 v1.4.0 至多个 v1.0.0-rc 预发布版本。
- 🚀 v1.4.0 为最新稳定版，新增命名端口预留与管理：`stim ports get <label>`、`stim ports`、`stop`、`release`，支持 `--dry-run`，Metro 仍独立运行。
- 🔧 v1.4.0 修复包括：兼容 EAS 开发构建的 `app.id`/`project.id`，提供 iOS 重启补救，恢复设备操作声明，支持中断的 Android AVD 创建恢复，并改进目录锁所有权。
- 🧩 v1.3.1 修复 Android 模拟器内存压力下的额外启动等待、关闭匹配的 agent-device 会话、worktree 刷新与复制重叠，以及无 timeline 时日志查询返回 `STIM_NO_PROJECT`。
- 📱 v1.3.0 支持通过 `--slot <name>` 在同一 workspace 运行多个模拟器/仿真器/真机，并支持 `--eas-profile` 下载兼容的 EAS 开发构建。
- ⚡ v1.2.0 允许原生构建期间预热 Metro，增强 Android 模拟器恢复，改进 iOS 停滞检测与有界等待，doctor 不再强制要求 `expo-dev-client`。
- 🛠️ v1.1.0 引入 `worktree warm --refresh`，统一 ownership claim 原语，增强 doctor 对机器配置和源 checkout 的检查，并修复 `gc --delete`、`stim reload`、设备标签冲突、CAS 回退等问题。
- 🎉 v1.0.0 是首个稳定版，CLI 发布为 `stim`，新增 `ios --scheme`、`start --reset-cache`、monorepo 每应用 `.stim.json`，并让 worktree warm 直接进行 COW 复制。
- 🧪 预发布亮点：rc.23 改进错误栈与符号化；rc.22 支持 Android 模拟器池回收、readiness 等待、移除 `caches.injectMetroStore`；rc.21 使用持久进程身份、移除 `stop --force`；rc.20 增加构建优化与 Android CAS/PCH 实验支持。
- ⚠️ 迁移注意：升级应保留现有 Stim 状态；旧版本无法管理命名端口分配；`npx stim-cli` 应替换为 `npx stim`；worktree warm 完成前不要写入目标目录；monorepo 运行时设置应移到各应用 `.stim.json`。
- ✅ QA 说明：部分版本因仅版本号或文档变更而复用已完成 QA，省略 native/manual 矩阵；保留格式、lint、构建、类型检查、单元测试、E2E、runtime、tarball 与精确提交 CI 检查。
- 🌐 页面本身出现“Uh oh! There was an error while loading. Please reload this page.”，表明部分动态内容加载失败，需要刷新页面。

---

### [](https://github.com/FerRiv3ra/react-native-nitro-wakeword)

**原文标题**: [GitHub - FerRiv3ra/react-native-nitro-wakeword · GitHub](https://github.com/FerRiv3ra/react-native-nitro-wakeword)

开源设备端 React Native 唤醒词检测库，基于 openWakeWord 与 ONNX Runtime，通过 Nitro Modules 实现原生音频采集与推理，无需许可证密钥、云服务或供应商锁定，支持多关键词、Silero VAD、自定义训练及 Expo / Bare RN。

- 🎙️ 在设备端运行 openWakeWord 管线：mel 频谱图 → 语音嵌入 → 关键词分类器，使用 ONNX Runtime。
- 🧩 基于 Nitro Modules（Swift + Kotlin，无桥接），原生音频捕获，JS 只接收检测事件。
- 🔑 支持多关键词同时检测，共享一个音频前端；可选 Silero VAD 门控降低误报。
- 🧠 可用免费 Colab 笔记本训练任意语言自定义关键词，输出小型 `.onnx` 分类器。
- ⚖️ MIT 许可；内置模型为 Apache 2.0 / MIT，详情见 `NOTICE`。
- 📦 安装：`yarn add react-native-nitro-wakeword react-native-nitro-modules`；bare 运行 `pod install`，Expo 运行 `npx expo prebuild`。
- ⚙️ 支持 Expo 配置插件：`microphonePermission`、`iosBackgroundAudio`、`androidForegroundService`、`modelsDir`；`*.onnx` 放入 `modelsDir` 后 prebuild 自动复制。
- 📱 Bare RN：autolinking 接入；iOS 需 `NSMicrophoneUsageDescription` 和 Copy Bundle Resources，Android 需权限与 assets。
- 🚀 用法：`WakeWordEngine.load` / `addDetectionListener` / `start` / `stop`；也可用 `useWakeWord` Hook。
- 📂 `model` 可来自内置模型、Expo `modelsDir`、iOS bundle / Android assets、绝对路径/file URL 或 `expo-asset` localUri；需 openWakeWord 格式 `[1,N,96]` → `[1,1]`。
- 🎚️ 调参：`threshold` 从 `0.5` 起，`patience` 2–3，`vadThreshold` 0.3，`refractoryMs` 控制同关键词最小间隔。
- 🌙 后台监听：iOS 启用 `audio` 背景模式；Android 用 `foregroundService` 前台服务与通知。
- 🧰 API：`load`、`start/stop`、`unload`、`setThreshold`、检测/分数/错误监听、麦克风权限方法。
- ⏱️ 每 80ms 处理 1280 样本 @16kHz；三次小推理，CPU 占用通常低于单核 5%。
- 🧪 `example/` 是 minimal Expo 示例应用，可测试模型复制流程与设备运行。
- ✅ 要求：React Native ≥0.76 新架构、`react-native-nitro-modules` ≥0.35、iOS 15.1+、Android API 24+。

---

### [](https://github.com/luicfrr/react-native-vision-camera-face-detector/releases/tag/v2.1.0)

**原文标题**: [Release Release 2.1.0 · luicfrr/react-native-vision-camera-face-detector · GitHub](https://github.com/luicfrr/react-native-vision-camera-face-detector/releases/tag/v2.1.0)

react-native-vision-camera-face-detector 发布 v2.1.0，由 luicfrr 于 9 月 11 日发布，重点修复 FaceDetector 的 autoMode 缩放，使其在不同设备和帧/屏幕分辨率下按预期工作。

- 🎉 FaceDetector 已更新，v2.1.0 为最新版本。
- 📱 auto mode 转换修复：现在可在任意帧/屏幕分辨率下正常工作。
- 🐛 修复 #242：在 ImageFaceDetector 中解包生成的 InputImage variant，感谢 @faculoyarte。
- 🧹 移除 TypeScript 错误相关 props。
- 🔗 更新 URL。
- 🤖 Android 修复：当 AGP 注册 kotlin extension 时跳过显式 Kotlin 插件，感谢 @gabrieldonadel。
- 👥 贡献者：gabrieldonadel、faculoyarte。
- 📦 发布包含 2 个 Assets；仓库公开，当前约 342 星、60 Fork、2 个 Issue。

---

### [](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.7.0)

**原文标题**: [Release Release 1.7.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.7.0)

react-native-nitro-fetch 的 v1.7.0 发布页展示了最新版本与多项变更，但页面多处出现加载错误；仓库公开，星标 996、Fork 51。

- 🚀 v1.7.0 标记为 Latest，发布于 9 月 12 日 21:20，由 riteshshukla04 发布；主提交 967ee28 经 GitHub 验证签名，GPG 密钥 ID 为 B5690EEEBB952194。
- 📊 仓库 margelo/react-native-nitro-fetch 公开：996 Star、51 Fork、9 Issue、6 PR，另有 Actions、Projects、Security and quality、Insights 等导航。
- ⚠️ 页面多次提示“Uh oh! There was an error while loading. Please reload this page.”、“Sorry, something went wrong.”，筛选、结果与 Assets 区域加载失败。
- 🛠️ CI/重构：端到端测试运行失败最多重试 3 次（#237）；将 fetch.ts 拆分为 fetch-core 模块（#236）。
- 🐛 修复：原生先完成时拒绝已中止请求（#235）；AGP 注册 Kotlin 扩展时跳过显式 Kotlin 插件（#230）；修复并回滚 multipart 名称与换行编码（#229）；podspec 指向 tagged 源仓库（#212）；Android token-refresh 连接在每次退出时关闭（#215）；text-decoder 使用具体 polyfill 路径以便 Metro 解析（#228）。
- ✨ 功能/文档：示例新增 worklet JSON benchmark（#227）；文档新增 React Query 与 RTK Query 示例。
- 👍 反馈：获得 2 个 👍 反应，来自 Splicer97 和 slymntrm。

---

### [](https://www.youtube.com/watch?v=0A4aehDmOXk)

**原文标题**: [How Marc Rousavy Turned Open Source Into a €20M+ Agency - YouTube](https://www.youtube.com/watch?v=0A4aehDmOXk)

這是 YouTube 網站頁尾的導覽與法律資訊，涵蓋平台簡介、新聞、聯絡方式、創作者/廣告/開發者資源、條款、私隱與安全政策、運作方式、測試功能，以及版權與 © 2026 Google LLC 標示。

- ℹ️ 簡介：平台基本介紹。
- 📰 新聞中心：官方新聞與公告。
- ©️ 版權：版權相關資訊。
- 📬 聯絡我們：聯絡管道。
- 🎬 創作者：創作者資源。
- 📢 刊登廣告：廣告投放資訊。
- 👨‍💻 開發人員：開發者資源。
- 📜 條款：服務條款。
- 🔒 私隱：私隱相關政策。
- 🛡️ 政策及安全：政策與安全資訊。
- ⚙️ YouTube 的運作方式：平台運作說明。
- 🧪 測試新功能：新功能測試資訊。
- 🏢 © 2026 Google LLC：版權所有者標示。

---

### [](https://infinite.red/react-native-radio/rnr-373-real-life-react-native-mark-goldstein)

**原文标题**: [React Native Radio - RNR 373 - Real Life React Native: Chime](https://infinite.red/react-native-radio/rnr-373-real-life-react-native-mark-goldstein)

overview summary
本期播客中，Chime 移动平台负责人 Mark Goldstein 分享了该公司在 React Native 上的实战经验，涵盖技术栈演进、性能挑战与优化、测试策略、AI 辅助开发及对人类监督的重视，并为考虑采用 React Native 的公司和新开发者提供了宝贵建议。

- 🏦 Chime 是美国金融科技公司，提供免费易用的银行服务，拥有超过 1000 万月活跃用户
- 🔄 应用于 2014 年推出，2017 年转向 React Native，主要为了整合与简化——统一产品界面、心智模型、审核流程和发布周期
- ⚙️ 技术栈包括 Hermes、新架构、TypeScript、Expo Modules、React Navigation、Redux、GraphQL 与 Apollo，以及共享组件库和设计系统
- 🎨 复杂动画使用 Reanimated、Skia 和 Filament 实现
- 🐛 性能挑战之一：Android 主题切换会触发生命周期钩子，导致冷启动遥测数据异常；React Native Performance 包未清除观察者
- 📦 GraphQL fragments 默认运行时编译开销大，使用 Babel Plugin GraphQL Tag 预编译后性能大幅提升
- 🌐 跨平台差异明显，尤其在键盘处理、日期选择器、动画、生命周期和性能分析工具方面
- 🧪 测试策略：内部狗粮应用、单元测试、选择性快照测试、Detox 端到端测试及动态 CI 流水线
- 🚀 性能优化核心：先测量再优化；利用 Expo Fingerprint 和远程构建缓存，使 95% 的 PR 无需重建
- 🧩 自建原生模块用于原生小组件、生命周期观察器、动画、认证及分析隐私屏
- 🤖 84% 的代码变更由 AI 辅助完成，工具包括 Cursor、Codex，并自建“软件工厂”Archimedes
- 🔍 AI 还用于代码审查、分诊监控、对抗性用户验收测试及分析验证
- 👤 强调人类在环路中：即使 AI 生成代码且测试通过，仍需人工在狗粮应用中验证实际行为
- ⚠️ AI 的局限：意图与行为不匹配（如复制整个 Markdown、列表仅一项可点击）、过度复杂化、缺乏业务上下文
- 💡 对公司的建议：React Native 在 AI 时代具有优势，热重载和 OTA 更新带来独特生产力提升
- 🎓 对新开发者的建议：参加 ChainReact 等会议、深入学习一个原生平台、真机测试、建立特性标志/遥测/所有权策略
- ✅ Mark 表示即使重新来过仍会选择 React Native，并看好 React Foundation 成立后的未来发展
- 📬 Chime 移动平台团队正在招聘跨平台工程师，可联系 mark.goldstein@chime.com

---

### [](https://nubjs.com/blog/phantom-dependencies-package-extensions)

**原文标题**: [De-phantoming the npm ecosystem — Nub](https://nubjs.com/blog/phantom-dependencies-package-extensions)

Nub 对 npm 下载量前 10,000 的包进行扫描，识别其中未声明的“幻影依赖”，并将结果发布为 @nubjs/extensions。该数据库覆盖 791 个包，其中 649 个不在 @yarnpkg/extensions 中，目标是作为现代、100% 兼容的替代方案，并已被 Nub 解析引擎采用。

- 🔍 Nub 使用内置 phantom detector 扫描 npm 高下载包，查找 package.json 中未声明的依赖，尤其是 peer dependencies。
- 🧩 这类未声明依赖在 npm/Yarn 的扁平 node_modules 下常被掩盖，但在 pnpm、Nub 等隔离布局中会导致 ERR_MODULE_NOT_FOUND。
- 🛠️ Yarn PnP 曾用 @yarnpkg/extensions 手工维护修补列表，但更新少且不完整；Nub 新增 649 个包，总覆盖从 142 增至 791。
- 📊 扫描按最严重问题分类：声明文件引用 341 个、受保护加载 114 个、未声明框架 peer 101 个、遗忘依赖 104 个。
- ⚠️ 声明文件引用会在类型检查时报 TS2307，skipLibCheck 下静默变为 any；遗忘依赖在运行时未受保护，其中 25 个已在 Yarn PnP 下复现失败。
- 📦 每个条目以 optional peer 发布，默认不安装；25 个复现失败案例以 dependencies 发布。
- 🧷 部分规则限定版本范围，例如 redux-thunk<=2.3.0；2.4.0+ 已自行声明。95/791 个包仅由当前版本已修复的旧规则覆盖，默认隐藏。
- 🔁 @nubjs/extensions 1.0.4 是 @yarnpkg/extensions 的 100% 兼容替代，保留所有 Yarn 规则、依赖范围和 peer 元数据。
- 📚 导出格式不变，仍为 packageExtensions 数组，支持 CommonJS 和 ESM，其他工具可一行替换导入源即可采用。
- ⚙️ Nub 已将该列表集成到解析引擎，并通过静态源码分析实时识别 phantom dependencies；该数据集正由这个 finder 生成。
- 🤖 数据库通过 CI 自动更新：定期刷新 npm 下载排名、每日扫描当前发布版本、手写覆盖可经 PR 更新。
- 🐾 Bun 1.4 的 opt-in global virtual store 没有基于扩展的修补，可能安装成功但运行时 MODULE_NOT_FOUND；Aube 与 pnpm v12 的全局虚拟存储也依赖此类扩展。
- 📥 安装方式：npm install @nubjs/extensions。

---

### [获取失败](https://blog.master.dev/new-things-you-should-know-about-html-here-in-mid-2026/)

**原文标题**: [Failed to retrieve](https://blog.master.dev/new-things-you-should-know-about-html-here-in-mid-2026/)

无法总结：获取内容失败，状态码 429。

---

### [pnpm 12.4 | pnpm](https://pnpm.io/blog/releases/12.4)

**原文标题**: [pnpm 12.4 | pnpm](https://pnpm.io/blog/releases/12.4)

pnpm 12.4 于 2026 年 9 月 10 日发布，核心是在同一工作区中管理 npm、Python 和 Cargo 依赖，新增 pnpm pipeline 任务运行器、更多平台二进制及多项缓存/注册表/锁文件改进；12.4.1 随后修复安装兼容性并提升重复安装速度；同期 pnpr 0.1.0-alpha.11 将服务扩展到 Cargo、Python 与容器 registry，支持跨生态单事务发布和 OIDC 登录。

- 🧩 一个工作区三种生态：在 `pnpm-workspace.yaml` 开启 `cargo.enabled` 或 `python.enabled`，即可用一次 `pnpm install` 安装 npm、Cargo、Python 依赖。
- 📁 各生态保留自身语义：Cargo 使用 `Cargo.toml`/`Cargo.lock`、crates.io 或稀疏 registry、`cargo vendor` 布局与 Cargo 认证；Python 使用 `pyproject.toml`/`pylock.toml`、`.venv`，锁文件格式经 uv 独立验证。
- 🔗 生态边界之下共享：统一 HTTP/认证预算、制品校验摄取、内容寻址存储；冻结与离线安装均可用，也可把解析交给 `pnprServer` 并回退本地。
- ⚠️ Cargo 与 Python 支持仍属早期，设置和 pnpm 写入的布局可能继续变化。
- 🚀 `pnpm pipeline [name]`：安装冻结依赖并运行命名工作区任务集，选择受影响项目、执行任务图，任务失败后继续以报告所有失败。
- 🧠 任务缓存：声明 `outputs` 才可缓存，`outputs: []` 表示不写文件；`inputs`/`env` 调整缓存键，`cache: false` 退出；命中后恢复输出并重放日志，Cargo 任务可用 `cargoTargetDir` 复用构建状态。
- 🖥️ 新增六平台二进制：Android arm64/x64、FreeBSD x64、Linux ppc64le、s390x、RISC-V。
- 🧹 `trustPolicyExcludePrune`：默认关闭，清理新 lockfile 不再解析的 `trustPolicyExclude` 条目；保留 `@scope/*` 模式，`sharedWorkspaceLockfile=false` 时跳过。
- ✅ `pnpm change check`：按 `versioning.epics` 与 `versioning.fixed` 校验已提交版本，不读 change intents，适合每个 PR 的 CI，并报告所有违规。
- 🗂️ Registry 元数据按完整 URL 隔离：不同路径或协议不再混用版本/tarball，防止 HTTP 元数据复用于 HTTPS；升级后首次安装会重新获取元数据。
- 🧾 `pnpm cache view` 显示完整 registry URL，解析 `cache list-registries` 或 `cache list` 目录名的脚本需更新。
- 🔧 安装/构建行为：patch 增加构建脚本或 `binding.gyp` 后包变为可构建；`pnpm add --allow-build=!<pkg>` 预拒绝构建；`pnpm approve-builds` 可保存决定；`.npmrc` registry 优先于全局登录路由。
- ⏱️ 兼容性与体验：`fetchTimeout` 限制无进展时间；`pnpm add --workspace` 恢复并支持 `workspace:` 协议；接受 `jsr:@scope/pkg`、`npm:pkg@^1.0.0`、`workspace:pkg@*`；布尔标志可内联赋值；命令从子目录查找最近祖先 manifest。
- 🩹 Patch/版本/工作区修复：`patch-commit` 支持增删文件和 CRLF；`<=16` 包含 16.x；workspace 模式支持 `.` 与 `..`；`packageConfigs` 在非共享锁文件时生效；无效 CA 证书不再整体失败；`audit` 忽略项单独报告；补全 `pn` 别名。
- ⚡ 性能：多项目工作区热安装更快，`pnpm deploy` 更快并修复 `.pnpmfile.mjs` 下的 `ERR_PNPM_LOCKFILE_CONFIG_MISMATCH`。
- 🛠️ 12.4.1 修复：在拒绝硬链接/写时克隆的文件系统、Android、`nodeLinker: hoisted` 下安装失败；自动回退复制，Android 使用内置 CA。
- 🔁 12.4.1 行为/性能：hoisted 重复安装不再重建整个 `node_modules`；副作用缓存无可恢复文件时重新运行构建；`ignoredOptionalDependencies` 在 install/add/dedupe 生效；Ctrl+C 转发给子脚本；`dedupe` 默认处理所有 workspace；`updateConfig` 钩子收到解析配置；重复安装约减少 1500 次文件系统调用。
- 📦 pnpr 0.1.0-alpha.11：单实例同时服务 npm、Cargo、Python 与容器 registry；托管 Cargo 支持 publish/yank/search/download，Python 支持 `pip install --index-url` 与 `twine upload`，并可代理 crates.io/PyPI。
- 🐳 容器 registry：声明 `ecosystem: oci` 后可 push，支持 `/v2/`、ranged blob、跨仓库 mount、referrers API、分页列表，并可缓存 Docker Hub/GHCR 拉取。
- 🧾 跨生态单事务发布：`PUT /-/pnpr/v0/publish` 可一次发布 npm 包、crate 与 Python 分发包；批次检查失败则全不发布，服务中断可续完。
- 🔐 OIDC：支持 OpenID Connect 浏览器登录，管理员映射 subject 到用户，GitHub Actions 可无需长期 token 发布 npm 包。
- 🏗️ pnpr 能力与修复：sccache 共享 Cargo 编译缓存；存储/查看 `pnpm pipeline` 报告；浏览器 UI 带 allowlist、分页搜索、维护者过滤、组织列表与上游发现；所有选项可用 `PNPR_` 环境变量；拒绝危险包名；JSR 内置解析；分阶段发布只批准一次，写竞争报 `document_write_conflict`。

---

### [Safari](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)

**原文标题**: [Safari 27 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)

本页面依赖 JavaScript 才能显示内容；用户需在浏览器中启用 JavaScript 并刷新页面。页面还为自动化工具和辅助工具提供了 Markdown 版本内容入口。
- ⚙️ 页面内容需要 JavaScript 才能正常显示。
- 🔄 需在浏览器中开启 JavaScript 并刷新页面。
- 🤖 页面面向自动化工具和辅助工具提供支持。
- 📄 提供 Markdown 版页面内容，可通过“View Markdown”查看。

---

### [](https://webkit.org/blog/18227/fixing-top-level-await-in-safari/)

**原文标题**: [  Fixing Top-Level Await in Safari | WebKit](https://webkit.org/blog/18227/fixing-top-level-await-in-safari/)

WebKit 为 Safari 27 重写了模块加载器，以完整符合 ECMAScript 规范，修复顶层 await 长期存在的“初始化前访问”等错误；新实现改用原生 C++，并通过大量测试与模糊测试验证，让开发者可放心在生产中使用顶层 await 和 ES 模块。

- 🚀 Safari 27 新增对顶层 await 的完整规范支持，此前部分用户会遇到意外的“accessed before initialization”错误。
- 🧩 顶层 await 允许在模块顶层直接使用 await，把复杂 Promise 链简化为线性代码，类似 async 函数中的 await。
- ⏸️ 当模块遇到顶层 await 时，导入它的模块会被暂停，直到 await 完成；不依赖它的兄弟模块仍可并发执行。
- 🧪 现在可下载 Safari Technology Preview 251 或 Safari 27 beta 试用；Safari 27 正式发布后可用于生产环境。
- 🐞 旧模块加载器基于已过时的 WHATWG Loader 提案，早于 async/await 和顶层 await，与 ECMAScript 2022 规范不匹配，导致微妙且长期未解的 bug。
- 📉 示例中动态导入同一模块三次，旧加载器输出顺序错误为 2、3、1，并访问未初始化的 someArray；新加载器正确输出 1、2、3，导出访问正常。
- ⚙️ 旧加载器是自托管 JavaScript builtin，虽有内联与减少跨边界开销等优势，但启动更慢、JIT 难以优化、非热路径性能不稳定。
- 🛠️ WebKit 于 2026 年 1 月开始重写：删除旧 JS 文件，按 ECMAScript 规范把伪代码翻译为 C++，先实现叶函数并梳理调用流程图。
- 🧪 测试包括 Bun 提供的用例、JavaScriptCore 的 jsc 集成测试、自研 fuzzer 生成复杂模块图并与其他引擎逐字节对比，以及 test262 和 WPT 通过且无回归。
- ✅ 新模块加载器已被每日使用数周无问题；Safari 27 发布后可放心依赖顶层 await 和 ES 模块，反馈可提交至 bugs.webkit.org。

---

### [](https://developer.apple.com/documentation/safari-developer-tools/connecting-an-ai-agent-to-safari)

**原文标题**: [Connecting an AI agent to Safari | Apple Developer Documentation](https://developer.apple.com/documentation/safari-developer-tools/connecting-an-ai-agent-to-safari)

该页面依赖 JavaScript 才能正常显示内容；如果未启用，需要先在浏览器中开启 JavaScript 并刷新页面。页面也为自动化工具和辅助工具提供了 Markdown 版本的内容访问方式。

- ⚠️ 页面内容需要 JavaScript 才能查看。
- 🔄 请在浏览器中启用 JavaScript，然后刷新页面。
- 🤖 该页面面向自动化工具和辅助工具提供支持。
- 📄 可访问 Markdown 版本的页面内容。
- 🔗 页面提示可通过“查看 Markdown”进入该版本。

---

### [](https://philipwalton.com/articles/modern-web-types/)

**原文标题**: [Modern Web Types â Philip Walton](https://philipwalton.com/articles/modern-web-types/)

文章介绍 TypeScript 官方 DOM/WebWorker 类型库只收录至少两个浏览器引擎支持的 API，导致许多已在 Chrome 可用、可作为渐进增强的新 Web API 在使用时报类型错误。作者因此创建 modern-web-types，用同一套生成器和 w3c/webref 数据，将支持阈值降为单引擎，提供更完整且自动更新的类型定义。

- 😤 TypeScript 常对新 Web API 报错，例如 startViewTransition、PerformanceEntry.scripts、fetchLater 不存在。
- 🧩 根因是官方类型生成政策：只纳入至少两个浏览器引擎支持的 API。
- 📦 modern-web-types 是官方 DOM/WebWorker 类型的替代品，支持任一稳定浏览器已发布的 API。
- 💻 推荐通过 @typescript/lib-dom 别名安装：npm install --save-dev @typescript/lib-dom@npm:modern-web-types。
- ⚙️ 使用 TypeScript 6 或更新版本时，需在 tsconfig.json 中设置 "libReplacement": true。
- 📊 额外类型数量可观：DOM 新增 433 个接口、96 个类型别名、223 个全局、311 个已有接口成员；WebWorker 新增 144 个接口、35 个类型别名、56 个全局、64 个成员。
- 🤖 类型由 TypeScript-DOM-lib-generator 和 w3c/webref 自动生成，GitHub Actions 每周检查更新并创建 PR。
- ⚖️ 作者认为双引擎规则不等于 Web 兼容安全；很多双引擎 API 不能无条件部署，很多单引擎 API 却可安全渐进增强。
- 🚀 单引擎 API 曾显著推动性能优化，例如 LargestContentfulPaint、PerformanceEventTiming、LayoutShift、fetchpriority 和 Speculation Rules。
- ✅ 若从未遇到缺失类型问题，可能不需要 modern-web-types；若遇到，用它比自己手写类型更省事、更安全。
- 🔮 若采用者足够多，可能促使 TypeScript 放宽双引擎政策，届时该库将不再必要。
- 📣 文章最后鼓励读者在 Bluesky 上分享。

---

### [](https://rapha.land/introducing-oj/)

**原文标题**: [Introducing oj: your Rust native replacement for Vite — Raphael Amorim](https://rapha.land/introducing-oj/)

oj 是一个用 Rust 编写的 Vite 原生替代开发服务器与打包器，可直接运行现有 Vite + React 项目而无需重写配置。它基于 rolldown 和 oxc 构建，主打极低内存占用与亚秒级冷启动，已能跑通 Excalidraw、Twenty 等真实生产级应用，目前仍属实验性项目。

- 🦀 **核心定位**：oj 是 Rust 原生的 Vite 替代品，可直接指向现有 Vite + React 项目，沿用同一份 `vite.config.ts` 和插件，无需任何改写。
- 🎯 **两大目标**：一是"说 Vite 语言"而非 webpack，通过兼容桥接层运行真实 Vite 插件，并原生重实现 React Fast Refresh 与 TanStack Start；二是摆脱 Node 与 `node_modules`，仅需一个约 28MB 的单一二进制文件。
- 📦 **沙箱场景优势**：Node 开发服务器每个预览环境约需 295MB 磁盘、冷启动约 18 秒；oj 仅约 28MB、启动不到 1 秒。500 个沙箱下磁盘占用从约 144GB 降至约 14GB。
- ⚡ **性能数据**：在 10,000 组件项目上，oj 冷启动 1211ms vs Vite 4917ms（快 4.1 倍），热启动 1067ms vs 4516ms，重载 223ms vs 1474ms。
- 🧠 **内存表现**：同一应用 oj 约占用 115MB，Vite 超过 1.5GB；有用户反馈 12GB 的 Vite 应用降到 1.8GB。内存差距随应用规模扩大而加剧。
- 🎨 **真实项目验证**：未经修改配置便跑通 Excalidraw（处理了正则 `resolve.alias`、`.module.scss`、根目录外 TS 源码、`import.meta.env` 等难题）。
- 🏢 **大型应用测试**：约 15,000 模块的 Twenty（含 `@wyw-in-js`、Linaria/SWC 宏、CommonJS/UMD 依赖）冷启动约 10.2s vs 11.3s，内存约 1.5GB vs 4.9GB，且请求量约为 Vite 的二十倍仍领先。
- 🌐 **部分打包（实验性）**：通过标志开启后可将某依赖的 962 个请求合并为 18 个；在 50ms 网络延迟下首屏渲染从 8.8s 降至 0.33s（快 27 倍），对远程或沙箱开发服务器意义重大。
- ⚠️ **已知缺口**：不支持 `vite-plugin-checker`（会跳过并记录日志），Svelte 支持仍在开发中，整体为实验性项目，README 明确"风险自负"。
- 💾 **持久化缓存（实验性）**：将模块编译结果按源码哈希存入磁盘，热启动直接复用；默认关闭，可用 `oj dev --enable-cache` 或 `OJ_ENABLE_CACHE=1` 开启。
- 🔧 **缓存正确性难题**：像 `wyw-in-js` 这类插件会在内存中存状态并生成虚拟 CSS 模块，全量缓存会导致 404；oj 只对导入不存在路径的模块重新执行转换，其余走缓存。
- 🏢 **项目起源**：源于作者在 Lovable 工作中被 Vite 高内存与多 worktree 代理并行耗尽的痛点，现已有多位贡献者加入，代码在公开仓库中。
- 🚀 **上手方式**：MIT 许可，已发布至 crates.io，执行 `cargo install oj --locked`，进入 Vite 项目后运行 `oj dev` 即可。

---

### [](https://lovable.dev/blog/faster-previews-oj)

**原文标题**: [Faster previews, soon powered by OJ | Lovable](https://lovable.dev/blog/faster-previews-oj)

概述总结  
Lovable 宣布其预览引擎 OJ（Orange Juice）即将逐步取代 Vite，带来更快冷启动、更低内存占用的预览体验，并已在 GitHub 开源。

- ⚡ **背景**：Lovable 预览是带热重载的真实开发服务器，目前底层引擎是 Vite。
- 🧱 **问题**：Vite 面向单开发者单机设计；Lovable 每天运行约百万沙盒，Vite 每个实例都带 JS 运行时、工具链和高内存，导致冷启动慢、资源占用重。
- 🦀 **OJ 是什么**：OJ（Orange Juice）是单一 Rust 二进制，兼容 Vite，读取 `vite.config.ts` 或 `oj.config.ts`，并通过兼容桥运行真实 Vite 插件。
- 🔁 **核心能力**：用 Rust 原生重实现 React Fast Refresh、TanStack Start 等；基于 Rolldown 和 Oxc；仅当插件或服务端需要 JS 时才启动小型 Node sidecar。
- 🧩 **设计原则**：兼容优先，应用无需改动；无需 JS 运行时驱动，不向项目安装工具链；为智能体批量编辑优化，合并突发编辑并批量应用更新。
- 📊 **基准测试**：1 万组件合成应用冷启动 1.2s，对比 Vite 4.9s；内存约 115MB，对比 Vite >1.5GB。
- 🖼️ **真实应用**：Excalidraw 约 0.8s 对比 2.3s，内存 288MB 对比 2.4GB；Twenty CRM 约 10.2s 对比 11.3s，内存 1.5GB 对比 4.9GB。
- ⚖️ **注意**：Vite 数据包含 `vite-plugin-checker` 运行 tsc，OJ 尚未托管该插件，因此并非完全对等；最关键指标是内存，决定可同时运行多少预览。
- 🏭 **生产表现**：预览可用时间中位数从 17.4s 降至 8.0s；沙盒获取中位数从 14.5s 降至 3.0s，约快 5 倍；90 分位 dev-server 从 15.8s 降至 9.6s；沙盒内 dev server 内存约为 node/Vite 的 1/6.5。
- 👩‍💻 **对开发者影响**：无需操作；预览更快、编辑到预览循环更紧；现有插件和配置继续工作；兼容问题是 bug；OJ 将逐步扩大发布。
- 🌐 **开源**：OJ 已从个人仓库迁移到 Lovable GitHub 组织：`github.com/lovablelabs/oj`，保持 Vite 兼容、公开透明、欢迎贡献。
- 🔮 **后续**：正在开发更多实验性功能以进一步加速预览，后续会公布。

---

### [](https://devfra.me/posts/pluggable-extensible-playful-devtools)

**原文标题**: [Pluggable, Extensible, and Playful DevTools | Devframe](https://devfra.me/posts/pluggable-extensible-playful-devtools)

概述总结
- 🧱 多个 DevTools（UnoCSS Inspector、Vite Plugin Inspect、Vitest UI、Nuxt DevTools 等）虽目标不同，却反复重建 RPC、状态同步、序列化、静态托管和 Web UI 等基础设施。
- 🌐 愿景是 Universal DevTools Ecosystem：让 DevTools 摆脱特定框架与开发服务器边界，实现模块化、可组合、社区协作。
- 🧩 Devframe 是框架中立的 DevTools 基础/框架，类似 unplugin 之于打包器插件，定义一次即可适配多种宿主、独立适配器和编码代理。
- 📦 通过 defineDevframe() 定义工具身份、能力、RPC、共享状态、SPA、诊断和编码代理接口；initDevframe() 将其变为可运行实例。
- 🔌 核心是 Web Standard Request→Response handler，也提供 Connect 风格 nodeMiddleware，可挂载到 Hono、Nitro、Next.js、SvelteKit、Vite、Rsbuild 等。
- 🧰 适配器可将同一 devframe 打包为 CLI、独立 dev server、Vite DevTools 插件、MCP server、静态报告等；一个包可同时提供多个入口。
- 🗂️ 该模型已用于 Node Modules Inspector、ESLint Config Inspector、Vite Plugin Inspect；浏览器 UI 可选任意框架，内置示例覆盖 Vue、Svelte、Solid、React、Next.js。
- 👨‍💻 视觉界面与编码代理界面共享同一事实来源：前者适合探索、概览、比较，后者可获取上下文、关联代码并执行多步操作。
- 🔐 RPC 默认私有，需显式通过 MCP adapter 暴露；支持 Vercel json-render，便于编码代理生成可预测的仪表板和交互工具。
- 🧪 内置 devframes 包括 Data Inspector、Terminals、Accessibility Inspector，以及 VS Code Web、资产管理、Git 面板、Open Graph 预览、RPC/状态检查器等。
- 🧭 @devframes/hub 是 headless、框架中立的组合层，initHub() 可统一挂载多个 devframes，并共享 RPC、状态、连接、认证、终端、消息和可选聚合 MCP。
- 🏠 Vite DevTools 是首个旗舰 DevTools 宿主；Nuxt DevTools v4 基于 Devframe + Vite DevTools，Vue DevTools 正在迁移，Next.js DevTools 有内部原型。
- 🧱 架构分层为共享基础 Devframe Hub → Vite DevTools → 框架专属 DevTools；基础设施共享，框架层保留专属外观与更丰富能力。
- 🛠️ Devframe v1.0 稳定社区接口；未来将继续连接更多宿主、完善挂载约定，并探索编码代理、权限与跨工具协作最佳实践。
- 🙏 文章感谢 webfansplz、Akryum、hyfdev、Atinux、danielroe、posva 等贡献者，以及 Vercel 对统一 DevTools 计划的支持。

---

### [Zod 4.6](https://zod.dev/blog/zod-4-6)

**原文标题**: [Zod 4.6](https://zod.dev/blog/zod-4-6)

Zod 4.6 已于 2026 年 9 月 9 日发布，可通过 `npm install zod@latest` 安装。本次更新包含验证性能优化、内存修复、JSON Schema 支持扩展、新字符串格式与多项破坏性修复，共汇总 72 个提交。

- 🚀 `.validate()`：仅检查输入是否有效，不构建结果；在编译 schema 上，无效输入可比 `.safeParse().success` 快至多 35 倍，异步场景用 `.validateAsync()`。
- 🧩 `z.instanceof().properties()`：可就地验证实例的指定属性，保留原型和类方法，弥补 `z.object()` 会剥离实例的问题。
- 📋 `fromJSONSchema()`：新增支持 `minProperties`/`maxProperties`、`uniqueItems`、`contains`、`minContains`/`maxContains` 六个 JSON Schema 关键词。
- 🏦 `z.iban()`：新增电子格式 IBAN 校验，内置 ISO 7064 MOD 97-10 校验和检查。
- 🌍 塔吉克语 locale：4.6.1 加入 `z.locales.tg()`。
- 🧰 `z.withParser()`：可安装外部生成的解析器，适合禁用 `new Function` 的严格 CSP 环境。
- ⚡ CommonJS 提速：移除每个导出上的 getter，在 `require` 下编译 schema 的 `z.validate()` 约快 3 倍。
- 🔗 `z.url()` 拒绝更快：4.6.4 起使用 `URL.canParse()`，无效 URL 约 90 ns，相比原来的 4.6 µs 快约 50 倍。
- 🧠 递归 schema 内存修复：释放已解析输入，修复 4.5 的 OOM 回归；29k 节点树保留 2.2 MB，此前为 10.1 MB，递归解析约慢 6%。
- 📦 `@zod/mini`：Zod Mini 成为独立包，自 4.5 起与 `zod` 同步版本发布。
- ⚠️ 错误映射延迟：`safeParse()` 懒构建错误，错误映射在首次读取 `result.error` 时运行，期间配置变化会影响结果。
- 😀 `z.emoji()` 修复：拒绝仅由组件组成的字符串，如 `"123"`、`"#"`、`"*"`、孤立 ZWJ、变体选择符或肤色修饰符。
- 🔢 数字枚举：`.options` 不再包含 TypeScript 数字枚举的反向映射键。
- 🧱 base64 正则：运行时 pattern 改为线性，长度和填充在代码中检查，避免多兆字节输入导致正则栈溢出。
- 📧 email 正则：移除 lookahead，空本地段规则改为结构化表达；有效地址校验约快 2 倍，相关 pattern 输出改变。
- 🧮 JSON Schema 链式检查：检查按合取方式折叠，`min`/`max` 等不再被后续格式检查覆盖；修复 `multipleOf`、`min`/`length` 等输出错误。
- 🗂️ 元数据成员：`format`、`minLength`、`maxLength` 等改为首次读取时物化，`Object.keys()` 与复制行为发生变化。
- 🛠️ 本次发布包含 72 个提交，涉及性能、文档、CI、测试和多个缺陷修复。

---

### [Webpack 5.111](https://webpack.js.org/blog/2026-09-14-webpack-5-111/)

**原文标题**: [Webpack 5.111 | webpack](https://webpack.js.org/blog/2026-09-14-webpack-5-111/)

Webpack 5.111 发布，重点包括稳定 ESM 输出、自动复制静态文件、按浏览器目标处理 CSS、发现未使用代码，并带来更小 chunk 加载运行时、更少依赖、缓存与热更新修复，以及面向插件作者的新能力。

- 🚀 ESM 输出稳定：可移除 `experiments.outputModule`，改用 `output.module`；`module`/`modern-module` 库类型和 `externalsType: "module"` 不再需要实验标志。
- 📦 ESM 库与 externals 改进：星号重导出保留 live bindings、遵循 externals 映射、保留 import attributes、修复循环与转义；数组 externals 会报错。
- 🔗 配置支持 `file:` URL：ESM 配置中可直接用于 `context`、`output.path` 及规则条件，无需 `fileURLToPath()`。
- 📁 新增 `output.copy`：可复制 `public` 等静态文件，支持多模式、watch 更新、构建统计、`output.clean` 保留，并警告空匹配或覆盖。
- 🎨 CSS 按浏览器目标降级：内置 CSS minimizer 默认启用 `lowerUnsupported`、`colorFallbacks`，扩展支持 inset、媒体范围、CSS 嵌套；修复 CSS Modules `@value` 重复作用域。
- 🧩 HTML/嵌入内容：minifier 修剪 URL 空白、可合并脚本、折叠布尔属性、统一属性值处理；支持 `renderEmbeddedSource` 与插件复用 CSS/HTML minifier。
- 📊 新性能提示：`sourceMaps`、`unusedAssets`、`unusedModules`、`analyzableBailouts`；多个配置检查合并为 `unusedConfig`，并支持 `hints: "stats"`。
- 🧠 更小输出与内存：chunk 加载运行时更小，ESM chunk imports 移入 loader，减少重建失效；空闲堆内存降低约 6.3 MB。
- 🛠 自有 JS 解析器：不再依赖 `acorn` 和 `neo-async`，可读取构建 Node 无法执行的 regex，缓存恢复时保留语法错误位置。
- 🗂 可选缓存依赖：`cache.buildDependencies` 支持 `optional: true`，缺失 `tailwind.config.js` 等文件仍可保存和复用缓存。
- 📚 模块命名空间对象：`specNamespaceObject` 提供 null 原型、排序导出名、实时绑定和防修改，接近原生 ESM；默认关闭，有性能权衡。
- ⚙️ 其他配置改进：`resolve.fileSystem` 被遵循；`module.exprContextCritical` 移至 parser 配置；`DefinePlugin` 的 `undefined` 属性读取会按原生行为抛错。
- 🐞 Bug 修复：改进 CSS 热更新/缓存失效、异步初始化、构建错误提示、作用域提升与缓存重建正确性。

---

