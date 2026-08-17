### [](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

这是一份面向 React 开发者的每周精选通讯，已吸引超过 2.2 万名前端工程师订阅，旨在通过精读文章与短摘要，帮助开发者节省时间并持续学习。

- 📬 每周一封精选邮件，为 React 开发者量身定制内容
- 👥 超过 22,075 名前端工程师已加入订阅
- ✍️ 手选优质文章并附简短摘要，节省筛选时间
- 🧠 每周都能学到新知识，紧跟 React 生态演进
- 💬 读者好评：文章实用、内容有深度，尤其对并发模式等主题收获很大
- 🏢 读者遍布各大公司，影响力广泛
- ©️ 版权信息：2013-2026 Bonobo Press，包含新闻通讯、隐私与广告条款

---

### [](https://alfy.blog/2026/07/25/modern-web-guidance.html)

**原文标题**: [Testing Google's "modern-web-guidance" skill against a real React app](https://alfy.blog/2026/07/25/modern-web-guidance.html)

overview summary  
- 🧭 本文实测了 Google 的 modern-web-guidance 技能，将其用作真实 React 应用的前端审计工具，重点检验它能否纠正过时的 Web 实践。  
- 🔍 该技能本质是一个语义搜索索引，通过 npx 命令检索和获取精选最佳实践指南，本身不读代码，需要人工或 Agent 配合。  
- 📋 审计发现应用存在多项问题：缺少 <form>、无 autocomplete/inputmode、硬编码浅色主题、使用 100vh 等，并逐一给出了现代方案。  
- ✅ 技能亮点包括：指南质量高、以 Baseline 为基准提供回退方案、能公正评价已有正确代码、框架无关、本地无密钥运行。  
- ⚠️ 局限也很明显：不自动分析代码、语义搜索存在召回上限、指南 token 消耗较大，需主动决定何时使用。  

- 🎯 核心发现 1：暗色模式是最大失误，应用未设置 color-scheme，导致原生控件、滚动条和首屏背景永远停留在浅色；指南要求 <meta name="color-scheme" content="light dark"> 与 :root { color-scheme: light dark; }，并建议用 light-dark() 管理配对颜色。  
- 🖱️ 核心发现 2：表单不是真正的表单，应用用 div + onClick 替代 <form> 提交，导致回车无法提交；指南明确要求用 <form> 包裹控件，按钮用 type="submit"，并推荐 e.preventDefault() 的 AJAX 提交方式。  
- ⏱️ 核心发现 3：验证时机需要讲究，指南提供“输入时清除错误、失焦时验证、提交时拦截”的矩阵，并推荐使用 :user-invalid 伪类，而非 onChange 中立即报错。  
- 📱 核心发现 4：autocomplete/inputmode 等属性在单选为主的表单中大多不适用，但文本输入框至少应设置 font-size: 1rem 以上，避免 iOS Safari 自动缩放。  
- 📏 核心发现 5：应用中的 min-height: 100vh 应改为 100dvh，以适配移动端动态视口，避免内容被浏览器地址栏遮挡。  
- 🧠 技能真正的价值是提供一个“标准”供开发前查询，时机是在写组件之前，而不是等到事后清理；能有效防止模型使用过时模式。  
- 📊 评分：dark-mode 指南相似度最高达 0.75，dvh 相关查询则未能精准命中，说明语义搜索有时只能返回笼统分类指南。  
- 🔒 指南都基于 Baseline 分类：广泛可用的功能可直接使用，较新的功能会附带 @supports 回退方案，让“是否安全”变成明确的决策依据。  
- 🔄 技能会公平地肯定已有的好代码，如实名验证 role="alert"、保存期间禁用按钮等做法，确实能赢得开发者的长期信任。

---

### [](https://www.sonarsource.com/blog/introducing-sonar-vortex/?utm_source=fnf&utm_medium=paid&utm_campaign=ss-vortex26&utm_term=newsletter-jchodounsky&utm_content=v1https%3A%2F%2Fwww.sonarsource.com%2Fsem%2Fvibe-then-verify%2F%3Futm_source%3Dfnf&utm_medium=paid&utm_campaign=ss-vibethenverify-25&utm_term=youtube-svaldarrama&utm_content=v1&s_category=Paid&s_source=Paid+Other&s_origin=influencer)

**原文标题**: [Introducing Sonar Vortex and the SonarQube Remediation Agent | Sonar](https://www.sonarsource.com/blog/introducing-sonar-vortex/?utm_source=fnf&utm_medium=paid&utm_campaign=ss-vortex26&utm_term=newsletter-jchodounsky&utm_content=v1https%3A%2F%2Fwww.sonarsource.com%2Fsem%2Fvibe-then-verify%2F%3Futm_source%3Dfnf&utm_medium=paid&utm_campaign=ss-vibethenverify-25&utm_term=youtube-svaldarrama&utm_content=v1&s_category=Paid&s_source=Paid+Other&s_origin=influencer)

Sonar 官方博客宣布推出两款面向 AI 智能体开发的新产品：Sonar Vortex 和 SonarQube Remediation Agent（正式 GA）。文章指出现有代码验证方式跟不上 AI 生成代码的速度，并提出“Guide（引导）、Verify（验证）、Solve（解决）”三阶段闭环方案，将代码质量与安全检查嵌入智能体的工作循环中，从而减少缺陷、降低 Token 消耗，并自动清理技术债务。

- 🚀 发布两款新品：Sonar Vortex 正式上线，SonarQube Remediation Agent 从 Beta 转为 GA
- 🧠 Sonar Vortex 在智能体编码循环内工作，编写前提供架构上下文，编写时实时验证输出
- 🐛 解决三大问题：上下文盲区、后期验证、技术债务规模累积
- 📉 测试数据显示：Sonar Vortex 可减少 92% 的缺陷产生，并降低最高 36% 的 Token 消耗
- 🧩 整合 Sonar Context Augmentation 与 SonarQube Agentic Analysis，提供架构感知、智能指南、语义导航和第三方依赖指导
- ⚡ 采用两阶段验证，在保持完整 CI 分析精度的同时实现秒级响应，兼顾速度与准确性
- 🔒 遵循“maker-checker split”零信任原则：智能体写码，SonarQube 独立验证，结果可审计、可解释且可重复
- 🤖 SonarQube Remediation Agent 自动修复可靠性、安全性和可维护性问题，并处理依赖漏洞，支持 GitHub 和 Azure DevOps
- ✅ 保持人工控制：按项目启用，工程师逐条审查并批准修复拉取请求
- 📦 两者组合为 Sonar Agent Essentials 套件，面向 AI 与工程领导者，完整落地 ACDC 框架
- 🏢 信任基础：超过 75% 的财富 100 强公司及 700 多万开发者使用 Sonar 验证代码，低至 3.2% 的误报率使自动化可靠

---

### [](https://granat.blog/posts/2026-07-24-react-arven/)

**原文标题**: [React doesn't need a state management tool, I said. Then I built one.](https://granat.blog/posts/2026-07-24-react-arven/)

overview summary
- 🧠 作者曾主张 React 不需要状态管理库，但后来开发了 react-arven，用于解决 20% 复杂场景下的状态组合问题。
- ⚙️ 80% 场景用本地状态配合专用工具（如 react-query、formik）足够；但复杂表单或编辑器等场景需要集中式状态来组合多个状态源。
- ❌ 现有方案如 zustand 需复制数据到 store，破坏单一数据源；jotai 要求一切变为 atom，仍是新增状态源而非组合已有状态。
- 📦 React Context 概念上正确，但性能差：Context 值变化会强制所有订阅者重渲染，且父组件状态变化会连累整个子树。
- 🔧 react-arven 通过三个改进解决：支持 selector 选择状态、利用 children prop 隔离重渲染、用 ref 技巧让 actions 保持稳定。
- 📝 使用方式是让一个普通 React hook 返回`{ state, actions }`，`createProvider`生成 Provider 和订阅 hooks，类型自动推断。
- 🚀 命名为`use...` hook 而非内联回调，能受益于 React Compiler 自动记忆化，并能被 eslint-plugin-react-hooks 规则检查。
- ⚡ 性能取决于选择器：只订阅需要的状态即可避免多余重渲染；仅使用 actions 的组件（如提交按钮）不会随输入重渲染。
- 📏 库仅约 1.4 kB（gzip），无依赖，需要 React 18+，已在大型项目中验证，整个应用只需约 4 个 context。

---

### [](https://aurorascharff.no/posts/experimenting-with-rsc-for-performance-and-ux-in-nextjs/)

**原文标题**: [Experimenting with RSCs for Performance and UX in Next.js | Aurora Scharff](https://aurorascharff.no/posts/experimenting-with-rsc-for-performance-and-ux-in-nextjs/)

本文通过三个实际案例，展示了在 Next.js App Router 中如何巧妙地运用 React Server Components（RSC）与 Server Functions，将数据获取和重渲染尽量保留在服务器端，同时保持客户端界面的即时响应与流畅体验。文章从 URL 驱动的“加载更多”、静态壳中的即时搜索，到按需渲染的消息预览，逐步拆解了实现方式、权衡取舍与适用场景，并总结了可落地的架构原则。

- 🚀 **服务器优先**：让 RSC 负责数据获取与渲染，客户端只保留最小交互组件，充分利用服务器靠近数据库的优势。
- 🔗 **URL 驱动加载更多**：将页码放入`?page=`，由服务器流式渲染新页面，支持刷新/分享，但会重新发送已有内容。
- ⚡️ **即时搜索体验**：输入框独立于动态查询，作为静态壳的一部分，配合内联脚本与`useLayoutEffect`保证值同步，且不丢失焦点。
- 🔍 **流式搜索结果**：通过`searchParams`的 promise 在`Suspense`内解析，配合 transition 的`isPending`，让旧结果淡出、新结果无缝替换。
- 📝 **服务器渲染预览**：用 Server Function 返回 JSX，客户端通过`use()`读取 Promise，确保代码高亮等预览效果与最终发布完全一致。
- 🧩 **客户端状态备选方案**：`Paginator`模式适合临时预览场景，但没有可分享 URL，且刷新/变更后需重置状态。
- 💡 **最大化静态外壳**：将动态读取放在`Suspense`边界之后，让页面头部和输入框等静态部分从 CDN 即时呈现。
- 🧱 **缓存与失效策略**：配合`cacheTag`和`'use cache'`，服务端渲染的页面可被复用，并在数据变化时精准失效。
- ⏳ **本地反馈**：利用 transition 的 pending 状态或乐观更新，在服务器处理期间提供视觉反馈，避免用户困惑。
- ✅ **总结**：这些模式并非必需，但能拓展 RSC 的边界；设计交互时不妨先从服务器开始，再看看哪些部分真正需要下放到客户端。

---

### [](https://jovidecroock.com/blog/referential-stability-types/)

**原文标题**: [Making Referential Stability a Type](https://jovidecroock.com/blog/referential-stability-types/)

overview summary
本文提出将 React/Preact 的“引用稳定性”纳入 TypeScript 类型系统：通过私有 phantom brand 定义 `Stable<T>`，并借助独立类型入口让不稳定的依赖在编译期报错，从而把性能优化转化为可验证的契约，并兼顾代码生成代理的反馈需求。

- 💡 **核心创意**：用类型承载引用稳定性，`Stable<T>` 通过私有 `unique symbol` 标记对象/数组/函数，原始类型因按值比较而直接通过。
- 🏷️ **稳定定义**：稳定不等于不可变，而是引用在无关渲染间保持，只在来源失效（如 state 更新、依赖变化）时改变。
- 📜 **组件边界示例**：`ItemListProps` 中 `items` 和 `onSelect` 标注为 `Stable`，内联数组或回调会立即产生类型错误，将责任推回调用方。
- 🔗 **强化 memo 契约**：`memo()`/`PureComponent` 依赖值稳定性作为优化前提，`Stable<T>` 使该假设显式化，避免优化被新数组/新函数悄然破坏。
- 🛠️ **实现策略**：模块增强因 React 原始重载会静默回落而放弃，改为独立入口 `stableref/react`，严格依赖签名让错误精准定位到失败的依赖项。
- ⚛️ **React 自带保证**：`useState` 的 state/setState、`useRef` 容器等被标为 `Stable`；`Stable<State>` 表示身份稳定而非不可变。
- 🪪 **stable() 助手**：运行时恒等函数 `x => x`，用于模块作用域常量（如 `EMPTY_ITEMS`），只提供类型证明，不改变值。
- 🌳 **Context 场景**：`createStableContext` 要求 Provider 的 value 为 `Stable`，让值所有者负责记忆化，子树消费者无需知道组装细节。
- ⚡ **Preact 支持**：独立入口 `stableref/preact` 沿用原始 hooks 引用并应用相同严格签名，证明与渲染库无关。
- ⚠️ **已知局限**：类型断言可绕过品牌；`stable()` 不应滥用；React Compiler 关注自动保留身份，`Stable<T>` 关注组件间契约，二者不冲突。
- 🤖 **AI 代理价值**：类型错误提供了可操作的反馈循环，内联不稳定引用会被构建拦截，并附带具体修复建议，比人工 review 更可靠。
- 🌐 **更广意义**：证明承载（proof-carrying）的类型能携带更多隐性属性，使约定从注释和 lint 规则升级为编译器强制保障。

---

### [](https://tanstack.com/blog/we-stopped-using-rsc-on-tanstack-com)

**原文标题**: [We Stopped Using RSC on TanStack.com | TanStack Blog](https://tanstack.com/blog/we-stopped-using-rsc-on-tanstack-com)

overview summary  
本文是 TanStack 团队关于从 React Server Components (RSC) 迁移回传统 SSR 的经验总结。最初 RSC 成功消除了浏览器中大型 markdown 与语法高亮依赖，带来显著性能提升；但团队后来将渲染依赖压缩到极小体积后，RSC 的架构复杂度变得不再值得，最终在保持性能优势的同时，用更简单的 SSR 方案取代了 RSC。

- 📉 最初采用 RSC 是因为 docs 页面需传输约 1.1 MiB 脚本，其中语法高亮占 358 KiB；RSC 将渲染移到服务端，大幅减少客户端 JS，Lighthouse 与 TBT 均有改善。
- 🔧 团队开发了小型包 `@tanstack/markdown` 和 `@tanstack/highlight`，将显式渲染器体积降到约 27 KiB，比 RSC 版本仅多 18-19 KiB，使客户端渲染不再“不负责任”。
- ⚖️ 对比新旧生产环境：当前非 RSC 站点在 /blog 与 /docs 上字节数和 TBT 均更低，虽然 Lighthouse 分数持平或略降，但整体性能优势保留。
- 📦 负载分解显示，移除 RSC 后新增了约 18-19 KiB 渲染器，但应用 JS 减少约 177 KiB，总体传输量仍下降。
- 🔁 每次导航时，RSC 会重复发送序列化 Flight 负载；而传统 SSR 只需一次性加载小型渲染器，后续请求仅传输内容数据，平均六次页面访问让节省更明显。
- 🧠 代码复杂度大幅下降：RSC 时代 markdown 需经过 `renderMarkdownToRsc`、Flight 序列化等多层特殊处理；迁移后服务端函数直接返回原始内容，路由组件直接渲染普通 Markdown 组件，代码更直观。
- 🗑️ 迁移提交删除了大量 RSC 专用文件与旧渲染插件，共移除约 1500 行代码，内容管道回归简单。
- 🤔 作者认为 RSC 的核心价值仅在“依赖体积巨大且不应发送到浏览器”时成立；一旦依赖变小，RSC 的边界、序列化与打包复杂性便不再划算。
- 🚪 TanStack Start 将 RSC 保持为可选能力而非默认架构，因此 tanstack.com 可以脱离 RSC 而不影响框架支持；这种“可选而非必需”的设计是本次决策能够顺利实施的关键。

---

### [](https://www.nirtamir.com/articles/advanced-react-questions)

**原文标题**: [Advanced React State Boundaries in a Real Next.js App](https://www.nirtamir.com/articles/advanced-react-questions)

概述：本文以一个真实 Next.js 应用为例，探讨了 React 状态在服务端渲染、客户端缓存、浏览器 API 与 URL 状态交汇处的边界设计。核心问题是：状态由谁拥有、如何响应变化、变更后应通知谁。文章通过多个具体案例展示了避免 Effect、使用 useSyncExternalStore、跨 RSC 与 TanStack Query 同步等进阶模式。

- 🌐 URL 变更时关闭 Popover：不要用 Effect 延迟修正状态，而应记录打开时对应的 pathname，并在渲染时直接判断是否关闭，避免多余的渲染提交。
- 🔑 使用 key 重置子树虽然简单，但会卸载整个组件，导致子状态丢失、焦点丢失和动画中断，只适合真正需要整体重置的场景。
- 🖥️ 检测浏览器专属 API（如 navigator.share）：用 useSyncExternalStore 搭配 getServerSnapshot 返回 false，让服务端渲染安全、客户端 hydration 后自动获得真实值。
- 📡 从无限查询缓存中派生“上一项/下一项”：仅用 getQueriesData 是读取而非订阅，需用 InfiniteQueryObserver 作为订阅层，再通过 useSyncExternalStore 桥接 React 更新。
- 🔄 RSC 快照传入客户端 Context：适合服务端独有的 auth 数据，但要注意这是请求时快照而非实时状态；若库提供官方客户端 API，应优先使用。
- ⚡ 跨 RSC 与 TanStack Query 的乐观更新：用 useOptimistic 提供即时反馈，成功后提交服务端结果并失效查询缓存，失败时回滚；上下文提供统一的行动入口。
- 🧭 核心教训：高级边界场景的关键不是记住 Hooks，而是明确状态的归属、可观测性及通知机制；当值有两个“家”且无人负责同步时，正是最难排查的 Bug 源头。

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

这是一份面向软件工程师的精选周刊，每周一封邮件，提供高质量文章摘要，帮助读者节省时间并持续学习，已有超过两万一千名工程师订阅。

- 📧 每周精选一封邮件，发送给超过 21,153 名软件工程师
- 🔍 人工筛选高质量文章，并附简短摘要，节省查找时间
- 🧠 每周都能学到新东西，内容覆盖 API 设计等前沿话题
- ⭐ 读者反馈：每期都有收获，“Moving Faster”等文章备受好评
- 🌍 读者来自全球各大科技公司，订阅者覆盖广泛
- 📅 持续运营至 2026 年，由 Bonobo Press 出品，提供隐私与广告选项

---

### [科技领域领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一份为 CTO、工程经理和资深工程师打造的科技领导力新闻通讯，已有超过 29,128 位技术领导者订阅。每周一和周四发送邮件，精选文章并附简短摘要，帮助读者节省时间、学习新知，获得读者高度评价。

- 📧 每周两次（周一、周四）发送一封精选邮件，面向 CTO、工程经理和资深工程师
- 👥 已有超过 29,128 位工程领导者订阅，内容经精心策划
- ✂️ 提供手选文章与短摘要，帮你节省筛选优质内容的宝贵时间
- 📚 每周都能学到新东西，持续提升领导力
- ⭐ 读者反馈：领导力构建文章无人能比，软件领域尤其出色
- 🎯 内容精准覆盖架构讨论、会议、规划以及最重要的沟通技巧
- 🤝 特别强调“委派”这一关键技能，读者认为其重要性常被低估
- 🌍 读者群遍布全球科技公司，并附有版权、文章、隐私与广告信息

---

### [C# 文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

overview summary  
这是一份面向 .NET 开发者的每周精选通讯介绍，强调其精选文章、节省时间、学习新知识，并附上读者好评及影响力范围。  

- 📧 每周为超过 21,639 名 C# 工程师发送一封精选邮件  
- ✍️ 手工挑选文章并附简短摘要，帮助节省寻找内容的时间  
- 🧠 每周都能学到新东西，覆盖实用技巧与前沿主题  
- 💬 读者反馈：实际工作中用到了其中多个技巧，如 LINQ、标准功能开关、DiagnosticListener  
- ⭐ 有读者因文章推荐迁移了 Azure Function，并向朋友同事分享  
- 🌍 读者来自全球 .NET 工程师群体，通讯由 Bonobo Press 运营（2013-2026）  
- 🔒 提供隐私政策与广告选项，订阅与阅读体验规范清晰

---

### [让](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

overview summary
- 📰 Bonobo Press 自 2013 年起发布软件行业新闻通讯，服务超过 94,000 名开发者、IT 专业人士和技术从业者。
- ✉️ 提供面向软件开发者、工程经理、技术主管和 CTO 的多种新闻通讯，内容简洁省时，深受技术人员喜爱。
- 📢 提供广告服务，帮助客户触达技术领域的专业受众，包括软件工程师、团队领导、CTO 和 IT 决策者。
- 📋 可通过媒体工具包了解详情并开始广告合作。
- 📧 如有任何问题、建议或广告需求，可随时联系团队。

---

### [过往通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

本次摘要汇总了 React Digest 2026 年 4 月至 8 月的多期内容，涵盖 React 19 新特性、性能优化、状态管理与表单处理、框架生态演进、安全性及可访问性等主题，为 React 开发者梳理了近期值得关注的技术实践与风险警示。

- 🔥 React 19 的 `useActionState` 与 `useTransition` 简化了异步状态和表单样板，但需用 per-item 锁避免本地 pending 标志导致的重复提交。
- ⚡️ React Compiler 在构建时自动添加记忆化，让手动 `useMemo`/`useCallback` 大多成为多余；性能优化重点转向状态放置与并发特性。
- 🚀 Google 的 modern-web-guidance 工具能发现 React 应用中的真实问题（如深色模式缺失、表单无原生提交），并关联 Baseline 日期判断安全发布时机。
- 🛡️ 安全警钟：React Flight 协议曝出严重 RCE 漏洞，影响默认 Next.js 应用；TanStack 的 npm 包遭 GitHub Actions 链式攻击，30 分钟内被拦截。
- ⚛️ React Router v8 将认证、日志、重定向集中到中间件，需 React 19 + Node 22；Router 7 的对话框模式可避免用 `useEffect` 管理模态框。
- 🧠 状态管理因地制宜：props 用于邻近组件，context 承载主题等慢变值，Zustand 应对高频更新；TanStack Query 以最小设置处理缓存与竞态，也有人认为状态管理只是缓存的华丽外衣，CRDTs 更优。
- 🖥️ 性能迁移案例：Railway 弃 Next.js 转 Vite（构建从 10 分钟降至 2 分钟）；MDN 改用 Lit 组件（开发启动从 2 分钟降至 2 秒）。
- ⚡️ 渲染与体验优化：React Fiber 将渲染拆成约 5ms 切片；ChatGPT 前端被逆向工程，采用标准 React 栈 + SSR + 流式，<100ms 渲染；Linear 将数据存浏览器本地并后台同步，实现无 spinner 的即时 UI。
- 📡 RSC 与渲染策略：React Server Components 让组件自取数据，取代 prop drilling；React 19 移除 Test Renderer，有团队用 reconciler 自建渲染器；Next.js 16.3 预览即时导航，通过预取与流式缩短点击反馈。
- 💻 开发工具与 AI 工作流：Mark Erikson 分享 AI 编码设置（父会话派生子任务、插件精简上下文）；GitHub Issues 用 IndexedDB 与 Service Worker 将加载从 1200ms 降至 700ms。
- ♿️ 可访问性：常见错误为缺失语义、焦点破坏、动态更新无提示；同时警惕 DOM 模式拖垮 60fps 性能。
- 🧪 表单与乐观 UI：表单是复杂状态机，需权衡 React 19 服务端动作与客户端库；乐观更新需按项目加 pending 锁防乱序，且 `useMemo` 常无价值。
- 📚 开发者教育：指南为初级开发者补全“未言明的知识”；信号（signals）并不能解决 React 的怪癖；Next.js App Router 错误处理需要专门驯服。
- 🔍 其他洞察：大多数 `useEffect` 问题源于不稳定对象引用，移除 effect 往往最有效；500 个仓库研究发现只有 lodash 和 moment.js 是真正的包体负担。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本政策概述了 React Digest 对用户隐私的重视与保护措施，涵盖信息收集、使用、存储、安全、儿童隐私、用户权利及反垃圾邮件承诺。我们仅收集邮箱用于发送订阅邮件，不向 13 岁以下儿童收集信息，并允许用户访问或删除个人数据。

- 🔒 隐私至上：我们承诺合法、公正地收集个人信息，并仅在明确告知目的后使用，除非获得同意或法律要求。
- 📧 收集信息有限：仅收集您的电子邮件地址，用于发送新闻邮件，绝不用于其他用途。
- 👶 儿童保护（COPPA）：不故意收集或存储 13 岁以下儿童信息，网站也不以儿童为设计目标；若发现请联系我们。
- 📂 数据保留与准确性：仅在实现目的所需时间内保留信息，并确保数据相关、准确、完整且最新。
- 🛡️ 安全防护：采用合理安全措施，防止信息丢失、被盗、未经授权访问、披露、复制、使用或修改。
- 📋 政策透明：随时向客户公开我们关于个人信息管理政策和实践的相关信息。
- 📝 用户访问权（英国数据保护法）：您可以按要求发送邮件至指定地址，申请获取我们存储的您的全部信息（受法律限制）。
- 🗑️ 数据删除请求：如需删除您的数据，可发送邮件至指定地址，我们将处理您的请求。
- 🚫 反垃圾邮件：我们强烈反对垃圾邮件，不参与任何垃圾邮件行为；您可随时通过邮件中的退订链接取消订阅。
- ⚖️ 合规承诺：严格遵循上述原则开展业务，确保个人信息的机密性得到保护与维护。

---

### [](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 媒体工具包汇总：该平台为软件开发者和技术管理者提供高参与度（打开率远高于行业基准）的新闻通讯赞助服务，覆盖 Leadership in Tech、Programming Digest、C# Digest 和 React Digest 四份刊物，并公布订阅数据、费率、广告形式、合作伙伴及订购流程。

- 📧 使命与受众：为程序员、工程经理、CTO 等技术从业者提供精选趋势内容，合作伙伴广告涵盖工具、职位、会议、书籍等，帮助精准触达目标客户并提升转化。
- 📘 Leadership in Tech：29,158 订阅者，打开率 51.47%，点击率 11.38%，每期 $2,235，预计点击 365-585，CPC $3.82-$6.12；受众多为决策者（CTO、VP、工程经理等），40% 欧洲、35% 美国；另有次要广告位 $1,565/期。
- 💻 Programming Digest：21,149 订阅者，打开率 45.57%，点击率 14.83%，每期 $985，预计点击 273-493，CPC $2.00-$3.61；面向软件工程师、全栈/后端开发者，30% 初级、30% 中级、25% 高级。
- 🔷 C# Digest：21,077 订阅者，打开率 53.41%，点击率 21.63%，每期 $1,220，预计点击 411-631，CPC $1.93-$2.97；面向 .NET/C# 开发者，偏向企业级（医疗、金融、政府等）。
- ⚛️ React Digest：22,463 订阅者，打开率 49.86%，点击率 12.17%，每期 $1,375，预计点击 180-400，CPC $3.44-$7.64；面向 React/前端开发者；另有次要广告位 $962/期。
- 🤝 主要合作伙伴：包括 Okta、GitLab、Datadog、MongoDB、Twilio、Pluralsight、Retool、Posthog 等，不少客户会长期重复投放。
- 📝 广告形式：纯文本嵌入邮件正文，包含 URL、标题（<100 字符）、描述（<400 字符），截稿日为发布前 4 天，并提供文案撰写建议。
- 📅 订购流程：首先联系并介绍产品/活动，接着排期；付款锁定档期，之后提交素材，经文案优化后上线，最后提供投放效果报告。
- ⏳ 提示：广告位排程紧张，如期敏感请提前数周联系；也可通过官网获取媒体资料、合作案例及条款。

---

