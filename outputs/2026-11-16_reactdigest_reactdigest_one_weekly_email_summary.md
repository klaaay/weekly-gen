### [React 文摘：电子邮件简报](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

这是一份面向 React 开发者的精选周报，主打每周一封邮件、人工挑选文章并附简短摘要，帮助前端工程师节省筛选内容的时间并持续学习；已有超过 21,857 名前端软件工程师订阅，读者反馈积极。

- 📬 React Digest 是面向 React 开发者的精心策划的每周新闻简报。
- ⏱️ 每周发送一封邮件，帮助读者节省寻找有价值内容的时间。
- 📝 内容为人工精选文章，并配有简短摘要。
- 👩‍💻 已有超过 21,857 名前端软件工程师订阅。
- 📚 倡导每周学习新知识，跟上 React 的持续发展。
- 💬 读者评价积极，认为文章实用、写得很好，并能及时了解最新动态。
- ⚛️ 有读者特别提到从 React 并发模式相关文章中收获很大。
- 🏢 该简报被来自不同公司的前端工程师阅读。
- ©️ 网站版权归 Bonobo Press 所有，页面还包含 Newsletters、Privacy、Advertise 等链接。

---

### [我们如何将 Next.js](https://rohitpotato.xyz/thoughts/ssr-requests-still-alive)

**原文标题**: [How we cut Next.js memory from ~5GB to ~1GB: the react-query timer holding every SSR request Â· rohitpotato](https://rohitpotato.xyz/thoughts/ssr-requests-still-alive)

概览：Zepto 的 Next.js 服务每个 Pod 常驻约 5 GB 内存，强制 GC 后几乎不降。作者在生产构建上通过堆快照与从 GC roots 出发的 BFS 保留路径分析，定位到 react-query v3 在 SSR 时为每个 Query 立刻启动 2–5 分钟的 `setTimeout`，而 Node 会把当前 AsyncLocalStorage 的请求上下文挂到定时器上，于是已完成的请求连同响应、Buffer 和 OTel span 被一直 pin 住。用 `cacheTime: Infinity` 让定时器根本不启动，几行代码就把单 Pod 内存从约 4.8 GiB 降到约 1.2 GiB；但修复后自动扩缩容行为随之改变，还需一并调整扩容策略。

- 💾 **症状**：生产环境每个 Pod 稳定占约 5 GB，不飙升也不崩溃，GC 跑了内存也不回落，强推 GC 堆几乎不动。
- 🧪 **排查姿势**：别在 `next dev` 上查内存（被 webpack、HMR、source map 淹没），改用生产构建 + `--inspect`，并写了三个小脚本：真实 SSR 页面负载生成器、通过 CDP 强制 GC 后流式导出堆快照、快照解析器。
- 📊 **数据**：112 MB（预热后）→ 312 MB（+280 请求）→ 934 MB（约 1400 请求），全是强制 GC 后的数字，约等于每个请求滞留 1 MB。
- 🔎 **关键线索**：快照 diff 显示新增约百万字符串、1.6 万个 `ArrayBuffer`，而 `ServerResponse` 数量正好等于发出的请求数——每个已完成的响应都还活着，连带 socket 和上千个 OTel span。
- 🧩 **支配树失灵**：最大单对象仅约 2 MB（Next 自带的 fetch-cache LRU，本身有界），说明是成百上千个小引用各管一个请求，支配树这类问题看不出东西。
- 🕸️ **换问题**：不问“谁最大”，而问“从 GC root 到它最短的保留路径是什么”，用 BFS 跳过 weak 边遍历堆图。
- ⏱️ **真凶**：所有路径都指向 `timerListMap[300000]` → `Timeout._onTimeout` → `Query` → `QueryCache` → ALS store → `ServerResponse`，约 900 个 2/3/5 分钟定时器全部来自 react-query v3 的 `Query.scheduleGc`。
- 🧵 **三重叠加**：① v3 的 Query 构造函数立即 `scheduleGc()`；② 订阅发生在 `useEffect`，SSR 时 effect 不执行，定时器永不取消，而该 QueryClient 渲染完就丢弃；③ Node 给每个 timer 复制当前 AsyncLocalStorage store（Next 的 `cookies()`/`headers()`/`after()` 依赖它），而 pending timer 是 GC root。
- 🛠️ **修复**：继承 `QueryCache` 写 `ServerQueryCache`，在 `build` 里强制 `cacheTime: Infinity`；`isValidTimeout` 对 `Infinity` 返回 false，定时器就不会被创建。
- ✅ **为何安全**：服务端 QueryClient 本就按请求创建、渲染完即丢，“永不淘汰”等于“活到请求结束”；react-query 取 `Math.max`，hook 里传有限值也无法覆盖 `Infinity`；浏览器端完全不受影响。
- 🧪 **防回归**：加了一个在服务端构建查询时监听 `setTimeout` 的测试，旧代码失败、新代码通过。
- ⚠️ **升级不够**：v4/v5 仅在服务端把 `cacheTime`/`gcTime` 默认设为 `Infinity`，显式传有限值仍会起真定时器（TanStack/query#11320 未合并），所以 hook 自带 gcTime 时在 v5 也需同样的守卫。
- 📉 **效果**：本地堆平稳在 70/84 MB，应用定时器从约 900 个降到 0，GC 后滞留的响应 Buffer 从 373 MB 降到 7 MB；生产平均内存从约 4.8 GiB 降到约 1.2 GiB 并持续平稳。
- 🎯 **反转**：泄漏其实在“支撑”autoscaler——内存先触阈值决定了副本数；修复后只有 CPU 能触发扩容，副本减少、单 Pod 压力变大、延迟上升，需把 CPU 作为主扩容信号、内存阈值仅作安全网。
- 💡 **经验**：请求期间创建的任何 `setTimeout`（以及长期 pending 的 Promise）都会把请求攥住，不管回调是否用到上下文；"GC 不释放"就是"还有引用"；先 diff 快照找"什么在长"，再用保留路径找"为什么"；没有大对象时别盯支配树；务必在强制 GC 后测量；修内存前先读一遍 autoscaler 配置。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=react_digest&utm_medium=newsletter&utm_campaign=26q4&utm_term=primary+content)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=react_digest&utm_medium=newsletter&utm_campaign=26q4&utm_term=primary+content)

Meticulous 是一个面向复杂代码库的自动化、穷尽且确定性的测试平台，无需开发者投入即可生成随应用持续演进的端到端视觉测试，并在合并前展示代码变更对用户流程的影响。

- 🚀 零开发投入：实现自动化、穷尽且确定性的验证，让代码交付速度匹配代理编写代码的速度。
- 🧩 通过脚本标签记录开发、预发布和预览环境中的真实交互，也可仅依赖代理生成的会话。
- 🤖 AI 持续生成并演进测试套件，覆盖代码分支、用户流程和边缘案例。
- 🔍 每个 PR 自动评论，预览变更对现有工作流和新功能行为的影响，并按边缘案例拆分。
- 🔁 无需编写、修复或维护测试，测试随应用自动新增和淘汰，始终保持最新且完整。
- ⚡ 从 Chromium 层面构建确定性调度引擎，从根源消除 flaky，并支持极速执行。
- 🏎️ 测试在计算集群中高度并行，可测试数千屏幕并在 120 秒内获得结果。
- 🔗 可与现有测试套件组合使用或完全替代，支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit。
- 🏢 已被 100+ 组织信任，Dropbox、Notion、Engine 等团队给予积极评价。
- 🛡️ 提供集成、安全与文档支持，几分钟内即可通过 recorder script tag 开始使用。

---

### [六款 React 图表库与手写 SVG 对比：我的发现 - DEV Community](https://dev.to/gusevp/six-react-chart-libraries-against-hand-written-svg-what-i-found-46ib)

**原文标题**: [Six React chart libraries against hand-written SVG: what I found - DEV Community](https://dev.to/gusevp/six-react-chart-libraries-against-hand-written-svg-what-i-found-46ib)

作者通过同一规格、同一合成数据，将生存曲线与散点图分别用 nivo、Recharts、ECharts、visx、TanStack Charts、Chart.js 和手写 React+SVG 实现，比较挂载性能、交互卡顿、包体积与代码量，并给出选型建议。

- 📊 典型规模下（3×200 生存曲线、500 点散点）七种实现差距不到一帧，无法明确排名。
- 🚀 10,000 点散点拉开差距：手写 SVG 约 24 ms，visx 33 ms，TanStack 53 ms，Chart.js/ECharts 80–86 ms，Recharts 310 ms，nivo SVG 达 3.2 秒。
- 🖼️ Canvas 实现并未在 10k 散点上胜出，ECharts 与 Chart.js 挂载反而约为 visx/手写 SVG 的两倍或更慢。
- ⏱️ 测量在 headless Chromium 中进行，使用双 requestAnimationFrame 等图表真正绘制后再停表；空页基线约 22–26 ms，小于一帧视为平局。
- 📦 包体积与代码量差异明显：无库 2.2 KB/3134 tokens；visx 25 KB/1683；Chart.js 55.6 KB/1214；TanStack 56.8 KB/720；nivo 103.1 KB/993；Recharts 106.2 KB/1064；ECharts 164.2 KB/1117。
- 🧩 各库有实现坑：nivo 需自定义图层且默认 nice 会拉伸坐标轴；Recharts 生存数据需重塑且动画要逐元素关闭；ECharts 顶层拼写错误可能静默通过类型检查；visx 命中测试需自己写；TanStack 语法新但表达简洁；Chart.js 命名与 d3 不同。
- 🎯 若追求更少代码，可优先试验 TanStack Charts，但需注意其发布较新带来的成熟度风险。
- 🛠️ 若追求控制力与小包体，可选 visx 或手写 SVG，代价是代码量更高。
- ⚠️ 不建议将大散点放在 nivo SVG 渲染器上；Recharts 需先验证数据重塑与重载/悬停性能。
- 🧪 作者提醒自测图表性能时，应在浏览器真正绘制后再停表，并让 SVG 与 Canvas 走同样的最后计时步骤。
- 📌 结论受限于单机、单浏览器引擎、headless、机器繁忙、仅两种图表类型及脚本化悬停测试，实际产品可能不同。

---

### [获取失败](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

**原文标题**: [Failed to retrieve](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

无法总结：获取内容失败，状态码 403。

---

### [可写派生状态：停止同步状态 | 趣味编程](https://playfulprogramming.com/posts/writable-derived-state/)

**原文标题**: [
	Writable Derived State: Stop Synchronizing State | Playful Programming
](https://playfulprogramming.com/posts/writable-derived-state/)

文章指出，常见的“用 Effect 把服务端状态同步到客户端状态”会导致刷新或重新获取数据时覆盖用户修改；更可取的模型是“可写派生状态”：客户端有修改就用客户端数据，否则回退到服务端数据，从而减少同步逻辑和不必要的 Effect。

- 🔁 典型场景：应用需要从服务端提供默认值，同时允许用户覆盖这些默认值。
- ⚠️ 直观做法是在服务端数据到达时执行 `setTodos(serverState.payload)`，看似简单，但会让服务端状态在每次更新时“获胜”。
- 🐞 当加入“用户回到标签页时刷新服务端数据”后，问题暴露：刷新会重置用户数据，因为同步逻辑覆盖了客户端修改。
- 💡 更好的心智模型不是“同步客户端数据”，而是“客户端数据缺失时才使用服务端数据”。
- 🧩 代码可改为：`userTodos` 初始为 `null`，`todos = userTodos ?? (serverState.status === "data" ? serverState.payload : [])`。
- ⚛️ 该模式也适用于 TanStack Query：使用 `manualTodos ?? serverTodos ?? []`，保存成功后 `refetch`，并在成功时 `setTodos(null)` 以回退到最新服务端数据。
- ✅ 好处：移除不必要的 `useEffect`，符合 React“你可能不需要 Effect”的建议，让客户端与服务端状态管理更可预测、高效，组件也更简单易推理。

---

### [Text.js | 控制台框架](https://textjs.org/)

**原文标题**: [Text.js | The Console Framework](https://textjs.org/)

Text.js 是一个把全栈 React 应用渲染到 `console.log` 中的控制台框架。它结合 React 19、自定义 reconciler、Yoga 布局和 Turbolog 引擎，将每一帧编码为 `%c` 样式片段输出，并支持 App Router、服务端渲染、终端运行和 AI 编码代理等场景。

- 🖥️ 可直接在浏览器 DevTools 控制台构建和交互全栈 React 应用，使用 `bunx create-text-app` 快速创建项目。
- ⚛️ 基于 React 19，支持并发渲染、Suspense、错误边界和 App Router；`app/` 目录自动映射路由与布局。
- 🧩 提供 `Box`、`Text`、`Table`、`Chart`、`Input` 等组件，以及 `useInput`、`useKeymap`、`useFocus` 等键盘交互能力。
- 🚀 渲染管线为：React 自定义 reconciler → Yoga 单元格布局 → CellBuffer 仅重绘受损行 → 行哈希去重 → RLE 编码 → 每帧一次 `console.log`。
- 📉 性能示例：3,200 个单元格编码为 149 个 `%c` span；空闲帧 0 次 `console.log`；完整重绘 0.163ms，单行编辑 0.011ms。
- 🧠 支持 `runtime = "server"` 服务端渲染，浏览器只加载 21kB gzip 的帧播放器，并通过 SSE 接收行增量。
- 🌐 支持中间件、`revalidate`/`unstable_cache` 缓存、Partial Prerendering，以及 `static`、`bun`、`vercel`、`cloudflare` 部署适配器。
- 💻 同一 App Router 应用可通过 `text run` 在终端以真彩色 ANSI 运行；通过 `text mcp` 可让编码代理导航路由、按键并读取帧文本。
- 🛠️ 工具链包括 DevTools 扩展、VS Code 预览、ESLint 插件、`@textjs/app/testing` 测试工具和 `TX` 错误码。
- 🔤 额外能力包括控制台 REPL `window.text`、Unicode 双向文本算法、FIGlet 字体解析。
- 🤖 OpenCode Lite 使用 Text.js 在浏览器控制台重建 TUI，并提供沙盒演示与本地 OpenCode 服务器连接。
- 🎓 提供 10 章、约 65 分钟的免费课程，覆盖入门、布局、样式、输入、路由、数据、图表、测试、终端运行和发布。

---

### [The AI cost of JavaScript frameworks | Read the Tea Leaves](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)

**原文标题**: [The AI cost of JavaScript frameworks | Read the Tea Leaves](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)

Nolan Lawson 为反驳“凭感觉选框架”，让 AI 代理在 12 个 JavaScript 框架/元框架中构建同一个 Pokémon 应用，并重复多次，以成本、耗时、token、Lighthouse 指标和代码行数进行评估。结果显示，MPA/轻量方案在成本、JS 体积、LCP 和代码量上通常更占优，但 Lighthouse 分数接近饱和且实验存在随机性；核心结论是：在 AI 编程时代，技术选型仍应基于证据而非直觉。

- 🧪 基准方法：使用 PokéAPI 构建小型但非平凡的应用，让 Opus 5.5 以高 effort 运行，尽量使用各框架官方 MCP/skills，并用规范测试防止代理“作弊”。
- 💰 构建成本最低的是 Hono+htmx（约 $2.67）、Astro（$2.76）和 Nuxt（$2.82）；Angular 最高（$4.97），SvelteKit（$4.28）与 Gracile+Lit（$4.65）也偏贵。
- ⏱️ 构建最快的是 Astro（8.2 分钟）、Hono+htmx（8.6 分钟）和 Nuxt（9.0 分钟）；Angular 最慢（17.2 分钟），React Router 为 12.5 分钟。
- 🔢 token 消耗最低的是 Nuxt（3.85M）、Astro（4.13M）和 Hono+htmx（4.26M）；Angular 最高（9.76M），Gracile+Lit（9.04M）和 SvelteKit（8.53M）也较高。
- 🧭 Lighthouse 的性能、可访问性和 CLS 几乎饱和：性能分数多为 97–100，可访问性均为 100，CLS 大多为 0，难以区分框架优劣。
- 📦 JavaScript 传输量差异明显：Astro 约 0KiB、Vanilla 7KiB、Gracile+Lit 8KiB、Hono+htmx 18KiB；Next.js 142KiB、TanStack Start 118KiB、React Router 115KiB、Angular 93KiB。
- ⚡ Total Blocking Time 方面，Astro、Gracile+Lit、Hono+htmx、SvelteKit、Vanilla 接近 0ms；Next.js 为 71ms，Angular 为 103ms。
- 🖼️ LCP 通常奖励 MPA、惩罚 SPA：Astro 810ms、Gracile+Lit 956ms、Hono+htmx 978ms、Qwik 979ms；Next.js 2090ms、TanStack Start 2028ms、Angular 1954ms。
- 📏 代码行数最少的是 Hono+htmx（1370 行）、Nuxt（1415 行）和 Astro（1461 行）；Angular 最多（2009 行）。Hono+htmx 用约 70% 的代码实现类似 Angular 的功能，且更快。
- ⚠️ 实验局限包括：只测一个小型内容型应用、LLM 与 Lighthouse 结果波动大、Lighthouse 本身偏向 MPA、并非所有代理都使用 MCP/skills、Angular 有两次 SSR 构建失败未计入部分指标。
- 🧠 作者结论：不应把该基准视为“终极答案”，但它证明 AI 编程时代仍可基于证据做决策；基准已开源，鼓励复现、改进，并重新审视 `npm install` 后的框架选择。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

Programming Digest 是一份面向软件工程师的精选每周通讯，主打人工挑选文章与简短摘要，帮助读者节省筛选内容的时间，并持续学习新知识。

- 📬 每周发送一封邮件，内容由人工精心策划，面向软件工程师。
- 👨‍💻 已有超过 20,351 名软件工程师订阅。
- 📝 提供精选文章及简短摘要，减少寻找优质内容的时间。
- 📚 强调每周都能学到新东西，持续获取有价值的信息。
- 💬 读者反馈积极，认为内容涉及 API 设计等主题，且常有好文章推荐。
- 🌍 读者群体为软件工程师，网站版权归 Bonobo Press 所有（2013-2026）。
- 🔗 页面包含 Newsletters、Privacy、Advertise 等链接。

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一份面向 CTO、工程经理和资深工程师的精选通讯，旨在帮助技术领导者提升领导力，通过每周两封邮件提供精选文章与摘要，节省筛选内容的时间并持续学习。

- 🎯 目标读者：CTO、工程经理和资深工程师。
- 📬 订阅规模：已有超过 28,360 名工程领导者加入。
- 🗓️ 发送频率：每周一和周四各发送一封邮件。
- 📚 内容形式：精选文章并附简短摘要，节省寻找优质内容的时间。
- 🚀 核心价值：帮助读者每周学习新知识，提升技术领导力。
- 💬 读者反馈：领导力建设、架构讨论、会议、规划、沟通和授权等主题深受认可。
- 👥 受众背书：该通讯被多位技术领导者阅读。

---

### [C# 文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

概述总结
C# Digest 是一份面向 .NET 开发者的精选每周通讯，提供人工挑选的文章与简短摘要，帮助读者节省筛选内容的时间，并持续学习新知识。

- 📬 每周发送一封邮件，内容经过精心策划，面向 .NET 开发者。
- 👥 已有超过 22,123 名 C# 工程师订阅。
- 📝 每期包含精选文章和简短摘要，便于快速获取有价值的信息。
- ⏱️ 核心价值是节省寻找优质内容的时间，并帮助读者每周学到新东西。
- 💬 读者反馈提到内容可用于实际工作，涉及功能标志、LINQ、DiagnosticListener、Operation Result Pattern 和 Azure Function 迁移等主题。
- 🏢 该通讯受到 .NET 工程师阅读，由 Bonobo Press 运营，版权范围为 2013–2026。
- 🔗 页面还包含 Newsletters、Privacy、Advertise 等链接。

---

### [让开发者及时了解最新动态 – Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 自 2013 年起发布软件行业新闻简报，覆盖超过 94,000 名软件开发人员、IT 专业人士和技术人员，并提供面向技术细分受众的广告与联系服务。

- 📰 Bonobo Press 发布软件行业新闻简报，帮助开发者及时了解最新动态。
- 👥 受众包括超过 94,000 名软件开发人员、IT 专业人士和技术人员。
- 🧑‍💻 简报面向开发者、工程经理、技术负责人和 CTO，主打简洁、精炼、省时。
- 📢 提供广告服务，可触达软件工程师、团队负责人、工程经理、CTO 和 IT 决策者等细分技术人群。
- 📦 用户可查看具体出版物并订阅，也可通过媒体资料包了解广告合作。
- ✉️ 如有问题、建议或广告需求，可通过联系页面取得联系。
- ©️ 网站版权标注为 2013-2026，并附有条款链接。

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

本期内容聚焦 React/Next.js 的性能与内存优化、hydration 与渲染策略、React Compiler 的实际收益，以及框架选型、表单状态管理、设计系统、CSS 和图片格式等工程实践，并穿插 AI 编程代理对成本与抽象层的影响。

- 📉 Next.js 内存优化：一个 React Query 配置问题让 SSR 请求在内存中滞留最长 5 分钟；调整后单 Pod 内存从 4.8GB 降至 1.2GB，整体从 5GB 降到 1GB。
- ⚡ 性能案例：X 重构 Web 应用后，帖子加载时间从 22 秒降到 3 秒以内；React 中隐藏的 300ms 延迟可通过占位符修复节省 240ms。
- 🧩 框架与渲染取舍：用 Astro 替换 Next.js 后页面加载时间下降 87%、每月节省 1 万美元；AI 代理写代码时，Astro 等 MPA 在速度与成本上优于 SPA。
- 💧 Hydration 问题：React hydration mismatch 和 UI 闪烁常因客户端数据过早渲染，等待挂载后再渲染可修复；hydration 问题也可能影响 LCP。
- 🧠 React Compiler：通过构建期内联和更智能的 memoization 减少 useMemo/useCallback 需求，并让 Context 更便宜，因为未变更的 JSX 可被复用。
- 🎨 CSS 与可访问性：Interop 2027 将带来 squircles、滚动动画和新 CSS 函数；可过滤菜单需谨慎处理 role 与焦点管理，兼顾键盘和屏幕阅读器用户。
- 🖼️ 图片格式：对多数 Web 图片而言，AVIF 比 JPEG XL 文件更小、编码更快、内存占用更低。
- 🧱 设计系统与抽象成本：在组件上随意接受 className 会带来一致性隐患；过度抽象让 AI 代理费用高 30%，部分任务高至 5 倍。
- 🧮 大列表性能：含 1,175 个选项的 React 下拉框 INP 达 1,256ms，仅渲染可见行后降至 96ms。
- 📱 技术栈迁移：Shopify 放弃 React Native，转向原生 Swift 和 Kotlin；浏览器翻译可能分离文本节点并破坏 React 应用；Vidact 可将 React 编译为直接 DOM 操作。
- 🧵 浏览器主线程：每帧约 10ms 预算，批处理更新和把工作转移到 Web Worker 很重要；React 19.3 增加 ViewTransition 和 Fragment Refs。
- 🧪 测试与类型安全：三项 React 修复让 React Testing Library 测试运行时间减少 43%；TypeScript 可在编译期约束稳定 prop 引用，提前发现失效的 memoization。
- 🕵️ Next.js 内存泄漏：15.3–16.2 存在三类内存泄漏模式，均在 16.3 修复；客户端提示可用一次 Cookie 重载解决服务端时区渲染。
- 📋 表单与状态：React 19 的 useActionState 减少表单样板代码，但需防范 pending 标志导致重复提交；乐观 UI 在快速连点下会请求乱序，可用逐项 pending 锁修复。
- 🧭 框架与工具趋势：Google modern-web-guidance 能发现暗色模式、校验过期、表单原生提交等问题；TanStack 在精简依赖后放弃 RSC；React Router v8 用中间件集中处理鉴权、日志和重定向。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

React Digest 的隐私政策说明了其收集、使用、披露和保护个人信息的承诺，重点在于仅收集邮箱地址用于发送新闻通讯，并提供访问、删除、退订等用户权利。
- 🔍 收集个人信息前或收集时，会明确说明收集目的。
- 🎯 个人信息仅用于已说明的目的或兼容用途，除非获得个人同意或法律要求。
- ⏳ 仅在实现目的所需期限内保留个人信息。
- ✅ 通过合法、公平方式收集信息，并在适当情况下告知或征得同意。
- 📌 数据应与使用目的相关，并在必要范围内准确、完整、最新。
- 🔒 采取合理安全措施，防止信息丢失、被盗、未经授权访问、披露、复制、使用或修改。
- 📧 收集邮箱地址仅用于发送邮件新闻通讯，不用于其他目的；用户可随时通过邮件中的退订链接取消订阅。
- 🚫 强烈反对垃圾邮件，不推广也不参与任何形式的垃圾邮件。
- 👶 遵守美国 COPPA，不会故意收集或存储 13 岁以下儿童的信息；若发现相关情况可立即联系。
- 🇬🇧 依据英国《1998 年数据保护法》，用户可申请获取所持有的其个人信息；也可通过文中指定邮箱申请删除数据。
- 🌐 承诺公开相关政策和实践信息，并按这些原则开展业务，以保护个人信息的机密性。

---

### [媒体资料包 – Bonobo Press](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 面向程序员和技术人员发布精选通讯，覆盖开发者、工程经理、CTO 等软件交付人群；其互动率超过行业基准两倍以上，强调严格清理名单、优先活跃读者，并帮助广告主精准触达目标受众、获得线索与转化。

- 📬 四份主通讯为 Leadership in Tech、Programming Digest、C# Digest、React Digest，订阅数约 2.1 万–2.9 万，开放率 45.57%–53.41%，自然点击率 11.38%–21.63%。
- 💼 Leadership in Tech：面向技术领导与决策者，周一和周四发布；29,158 订阅，开放率 51.47%，CTR 11.38%，单期 $2,570，预估点击 365–585，CPC $4.39–$7.04；二次投放 $1,799。
- 💻 Programming Digest：面向软件、Web 与桌面开发者，周更；21,149 订阅，开放率 45.57%，CTR 14.83%，单期 $1,135，预估点击 273–493，CPC $2.3–$4.16。
- ⚙️ C# Digest：面向 Windows/.NET 与 C# 开发者，周更；21,077 订阅，开放率 53.41%，CTR 21.63%，单期 $1,345，预估点击 411–631，CPC $2.13–$3.27；受众偏企业级和大型公司。
- ⚛️ React Digest：面向前端 React 开发者，周更；22,463 订阅，开放率 49.86%，CTR 12.17%，单期 $1,375，预估点击 180–400，CPC $3.44–$7.64；二次投放 $962。
- 🌍 受众主要来自欧洲（约 35%–48%）和美国（约 30%–35%），涵盖 Google、Amazon、Netflix、Dropbox、Shopify 等公司及多种行业。
- 📝 广告为纯文本并嵌入通讯正文；需提供 URL、标题（少于 100 字符更佳）和描述（少于 400 字符一段），文案截止为发布前 4 天。
- 🗓️ 多数广告位需提前 1–2 个月预订；时间敏感活动建议至少提前 6–8 周联系，流程包括需求沟通、排期、付款锁档、素材交付、上线和效果报告。
- 🤝 近期合作方包括 Okta、GitLab、Datadog、OWASP、MongoDB、Twilio、Pluralsight、Monday、Retool、Webflow 等，复投较常见。
- 📩 可通过 Bonobo Press 联系洽谈，以精准覆盖目标受众并提升线索和转化；页面还包含条款、赞助内容示例和文案写作建议。

---

