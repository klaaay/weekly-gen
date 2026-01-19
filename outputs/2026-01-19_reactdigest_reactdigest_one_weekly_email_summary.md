### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

React Digest 是一份面向 React 开发者的精选周刊，汇集高质量文章，帮助开发者节省时间并持续学习新知识。

- 📧 每周向超过 25,478 名前端工程师发送一封邮件
- 📚 精选文章并附简短摘要，节省寻找有价值内容的时间
- 🧠 每周学习新知识，紧跟技术发展
- 👍 读者反馈积极，认可内容实用且更新及时
- 🌍 受到全球前端工程师的广泛阅读

---

### [如何窃取任何 React 组件](https://fant.io/react/)

**原文标题**: [How to Steal Any React Component](https://fant.io/react/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于算法的个性化治疗方案可整合患者数据，为精准医疗提供支持
- ⚙️ 智能管理系统自动化处理挂号、病历整理等流程，减轻医护行政负担
- 🧬 基因组学与 AI 结合加速新药研发，缩短药物临床试验周期
- ⚖️ 数据隐私与算法透明度成为 AI 医疗推广中亟待解决的伦理议题

---

### [免费 React UI 库 - KendoReact](https://www.telerik.com/kendo-react-ui/components/free?utm_medium=cpm&utm_source=reactdigest&utm_campaign=dt_kendoreact_freemium)

**原文标题**: [Free React UI Library - KendoReact](https://www.telerik.com/kendo-react-ui/components/free?utm_medium=cpm&utm_source=reactdigest&utm_campaign=dt_kendoreact_freemium)

KendoReact Free 是 KendoReact UI 库的免费版本，提供超过 50 个可自定义的企业级 React 组件，无需许可证即可用于生产环境。它包含数据网格、日期输入、下拉菜单等核心组件，并支持主题、无障碍访问和本地化。用户可通过 npm 直接安装使用，部分组件提供免费和高级功能的混合。如需完整库的 120+ 组件及高级功能（如图表、表单、调度器）和技术支持，可申请 30 天免费试用或购买商业许可证。

- 📦 **免费组件库**：提供 50 多个企业级 React UI 组件，包括数据网格、按钮、输入框等，无需注册或许可证即可用于生产。
- 🔧 **安装便捷**：通过 npm 直接安装组件包，无需填写表单或添加许可证密钥，即可在项目中快速集成。
- 🆓 **免费与高级功能混合**：部分组件（如数据网格、下拉列表）同时包含免费和高级功能，高级功能需商业许可证或试用许可证解锁。
- 🆚 **版本对比**：免费版包含基础组件和主题；完整版（KendoReact）提供 120+ 组件、专业主题、设计工具、源代码访问及专属技术支持。
- 📥 **升级路径**：可通过 30 天免费试用或购买商业许可证升级到完整版，解锁高级组件、源代码、Page Templates 和 ThemeBuilder Ultimate 工具。
- 🛠️ **支持资源**：免费用户可使用社区论坛、反馈门户和 GitHub 问题追踪；商业许可证用户可获得由开发团队提供的专业技术支持。
- 📄 **许可与使用**：免费组件遵循 KendoReact EULA，允许在原型开发、测试和生产中使用，但销售包含高级功能的应用程序需商业许可证。
- 🔄 **持续更新**：免费组件作为 KendoReact 库的一部分，定期获得错误修复、功能改进和新组件更新，由同一团队维护。

---

### [React 性能问题的起源 | 趣味编程](https://playfulprogramming.com/posts/where-react-performance-issues-start)

**原文标题**: [
	Where React performance issues start | Playful Programming
](https://playfulprogramming.com/posts/where-react-performance-issues-start)

本文解释了 React 中“渲染”的真正含义，它指的是 React 调用组件函数以确定 UI 应如何显示的过程，而非浏览器绘制像素。文章通过一个故意低效的组件示例，说明性能问题通常源于渲染阶段组件函数执行过多工作，而非 DOM 更新本身。

- 🧠 React 中的“渲染”是指调用组件函数生成虚拟 DOM 树的过程，而非直接更新屏幕显示
- 🔄 状态或属性变化会触发重新渲染，React 会比较新旧虚拟 DOM 以最小化实际 DOM 更新
- ⏳ 渲染阶段的同步耗时操作（如示例中的 1.5 秒循环）会阻塞主线程，导致界面响应延迟
- 📝 性能问题常源于渲染期间的计算开销、不必要的组件重渲染或重复的派生值计算
- 🎯 理解渲染本质是 JavaScript 执行而非浏览器绘制，是识别和解决 React 性能问题的关键

---

### [你能用 React 服务器操作获取数据吗？](https://www.developerway.com/posts/server-actions-for-data-fetching)

**原文标题**: [Can You Fetch Data with React Server Actions?](https://www.developerway.com/posts/server-actions-for-data-fetching)

本文探讨了是否可以使用 React Server Actions（现称 Server Functions）进行客户端数据获取。虽然技术上可行，但存在性能问题，特别是并行请求会变成串行处理，导致数据加载时间显著增加。因此，不建议将其用于数据获取，而应使用传统的 REST 请求配合数据获取库（如 TanStack Query）。

- 🚫 **不适用于数据获取**：Server Actions 本质上是 POST 请求的封装，虽然可实现类型安全，但设计初衷并非用于获取数据。
- ⚠️ **性能问题**：在大型应用中，使用 Server Actions 获取数据会导致并行请求转为串行，大幅延长加载时间（例如从 1.7 秒增至 8 秒）。
- 🔍 **调试困难**：网络面板中所有请求名称相同，且响应格式不易阅读，增加了调试复杂度。
- 🛡️ **缓存限制**：POST 请求无法通过 HTTP 头部进行浏览器或 CDN 缓存，但客户端缓存（如 TanStack Query）仍可正常使用。
- 🔄 **替代方案**：客户端数据获取应使用简单的 REST 请求配合数据获取库，而非 Server Actions 或过度依赖 Server Components。
- 📊 **性能对比**：实验显示，传统 fetch 方式在数据可见时间上（1.7 秒）远优于 Server Actions（8 秒），而 SSR 和 Server Components 各有优劣。
- 💡 **学习建议**：开发者应掌握服务端渲染（SSR）、Server Components 及数据获取的基础原理，结合实际需求选择合适方案。

---

### [理解 React 的 useEffectEvent：彻底解决闭包过时问题的完整指南 | Peter Kellner 的博客](https://peterkellner.net/2026/01/09/understanding-react-useeffectevent-vs-useeffect/)

**原文标题**: [Understanding React's useEffectEvent: A Complete Guide to Solving Stale Closures | Peter Kellner's Blog](https://peterkellner.net/2026/01/09/understanding-react-useeffectevent-vs-useeffect/)

React 19.2 引入的 useEffectEvent 钩子解决了在 Effect 中访问最新状态/属性而不触发不必要重新运行的问题，它通过创建一个稳定的函数来替代传统的 useRef 模式，从而简化代码并减少错误。

- 🎯 **解决闭包过时问题**：useEffectEvent 允许在 Effect 中读取最新的 props/state，而无需将它们添加到依赖数组中，避免了因依赖变化导致的 Effect 重复执行。
- 🔄 **替代 useRef 模式**：传统方法需使用 useRef 和同步 Effect 来保持值更新，代码冗长且易错；useEffectEvent 自动处理这一过程，减少样板代码。
- 📚 **明确职责分离**：依赖项决定 Effect 何时重新运行，Effect Event 则负责在 Effect 执行时读取最新值，使逻辑更清晰。
- ⚠️ **使用规则与限制**：Effect Event 应仅在 Effect 内部调用，不应传递给其他组件，且不应用于抑制 lint 警告，而应基于意图区分响应式与非响应式逻辑。
- 🛠️ **适用场景**：适用于订阅、计时器或外部库的回调，这些回调需要读取最新值但不触发 Effect 重新运行，如聊天室连接、分析日志等。
- 🔧 **版本兼容性**：React 19.2 及以上版本稳定支持；早期版本需使用 useRef 模式作为替代方案。

---

### [React Conf 2025 - YouTube](https://www.youtube.com/playlist?list=PLNG_1j3cPCaZ-pYFoA9WUwDgvMmVUi1eu)

**原文标题**: [React Conf 2025 - YouTube](https://www.youtube.com/playlist?list=PLNG_1j3cPCaZ-pYFoA9WUwDgvMmVUi1eu)

该文本为 YouTube 平台页脚导航链接列表，概述了网站的功能、政策与公司信息。

- 📄 关于平台的基本信息与介绍
- 📰 新闻与媒体相关资源
- ©️ 版权声明与知识产权
- 📞 联系与用户支持渠道
- 🧑‍🎨 内容创作者相关资源
- 📢 广告与商业合作信息
- 👨‍💻 开发者工具与资源
- 📜 服务条款与使用协议
- 🔒 隐私政策与数据保护
- ⚙️ 平台政策与安全指南
- 🔧 YouTube 功能运作说明
- 🧪 新功能测试与更新
- 🏢 谷歌公司所有权信息（截至 2026 年）

---

### [JavaScript 日期计算能离谱到什么程度？](https://philna.sh/blog/2026/01/11/javascript-date-calculation/)

**原文标题**: [How wrong can a JavaScript Date calculation go?](https://philna.sh/blog/2026/01/11/javascript-date-calculation/)

JavaScript 的 Date 对象在处理日期时容易因时区问题导致意外结果，例如在特定时区下进行月份加减可能产生错误日期。文章通过一个实际案例展示了该问题，并介绍了使用 setUTC 方法或即将推出的 Temporal API 来避免此类错误。

- 🕰️ JavaScript 的 Date 对象同时处理日期和时间，时区差异可能导致日期计算错误
- 🌍 作者在太平洋时区尝试将 2024 年 1 月 1 日加一个月，意外得到 2023 年 3 月 4 日
- 🔧 问题根源：UTC 午夜在太平洋时区是前一天的下午，导致月份设置时日期溢出
- ✅ 解决方案：使用 setUTCMonth 等 UTC 专用方法，确保时区一致性
- 🚀 Temporal API 提供了更直观的日期处理方式，支持纯日期对象和不可变操作
- 📅 Temporal 目前仅在 Firefox 原生支持，Chrome 144+ 开始逐步推出
- 💡 建议开发者提前学习 Temporal，或在使用 Date 时特别注意时区影响

---

### [网络依赖关系已断裂，我们能否修复？ • 莉亚·维鲁](https://lea.verou.me/blog/2026/web-deps/)

**原文标题**: [
		Web dependencies are broken. Can we fix them? • Lea Verou](https://lea.verou.me/blog/2026/web-deps/)

当前 Web 平台依赖管理存在严重问题，依赖管理这一基础功能被外包给第三方工具（如打包器），导致开发者面临不必要的复杂性和学习曲线。健康的生态系统应使依赖成为正常、廉价且一等公民的功能，但 Web 平台缺乏端到端的原生解决方案，迫使开发者依赖打包器处理基本需求，造成可用性悬崖。尽管存在多种无打包器使用依赖的方法（如直接引用 node_modules、使用公共 CDN、本地重写等），但各自存在安全、封装或可维护性缺陷。导入映射（import maps）虽提供浏览器原生支持，但当前形式仍依赖 HTML、缺乏可组合性，且未解决 URL 映射的根本问题。未来需改进导入映射（如外部映射、JS 导入支持）、探索依赖部署到 URL 的机制，并可能通过将标识符视为特殊 URL 类型来桥接标识符与 URL 的鸿沟，以实现真正的一等公民依赖管理。

- 🚫 **依赖管理被外包**：Web 平台将依赖管理这一基础功能外包给第三方打包工具，导致开发者必须使用高级工具处理基本需求。
- 📉 **可用性悬崖**：添加第一个依赖时，开发者需面对选择、配置和部署打包器的复杂决策，对新手尤其不友好。
- 🔧 **现有无打包器方案均不理想**：直接引用 node_modules、使用公共 CDN、本地重写或复制文件等方法存在安全风险、破坏封装或可维护性差。
- 🔗 **依赖的依赖问题**：当包本身依赖其他包时，无打包器方案几乎无法处理，迫使开发者回归打包器或导入映射。
- 🗺️ **导入映射的局限性**：当前导入映射需内嵌在 HTML 中，缺乏外部文件支持，且需手动映射每个传递依赖，工具链复杂。
- 🌐 **公共 CDN 的弊端**：引入第三方域的安全风险、单点故障，且由于双键缓存（double-keyed caching）无法跨站点共享缓存。
- 📦 **“浏览器”捆绑包的代价**：库提供的捆绑包虽可无打包器使用，但会重复打包相同依赖，增加代码体积并阻碍共享。
- 🛠️ **打包器虽普及但满意度下降**：尽管打包器如 Webpack 被广泛使用，但开发者对其满意度逐年降低，反映出生态不健康。
- 🌍 **平台架构受损**：打包器的普及导致 Web 平台设计围绕工具而非原生功能，影响组件资源引用等基础能力。
- 🚀 **未来改进方向**：需改进导入映射（如支持外部文件、JS 导入）、探索依赖部署机制，并可能通过将标识符视为 URL 类型来统一导入方式。

---

### [日期已过，时代已来 - Piccalilli](https://piccalil.li/blog/date-is-out-and-temporal-is-in/)

**原文标题**: [
  Date is out, Temporal is in  - Piccalilli
](https://piccalil.li/blog/date-is-out-and-temporal-is-in/)

JavaScript 传统的 Date 对象存在诸多问题，如不一致的日期解析、时区支持有限、内部表示混乱以及可变性导致的意外修改风险。即将推出的 Temporal API 作为现代化替代方案，提供了更直观、不可变且功能强大的日期时间处理方式，支持多种日历系统和时区，并已进入浏览器实验阶段。

- 📅 **Date 对象的问题**：月份从 0 开始计数，年份和日期解析规则混乱，时区支持仅限于本地和 GMT，且内部使用可变对象表示日期，容易引发意外修改。
- 🔄 **可变性风险**：Date 实例是可变对象，多个引用指向同一内存地址，修改一个实例会影响所有引用，违背了日期作为固定概念的本质。
- 🆕 **Temporal 的优势**：作为命名空间对象，提供 PlainDate、ZonedDateTime 等多种不可变类型，方法如 `add()` 和 `subtract()` 返回新对象，避免副作用，并内置国际化支持。
- 🛠️ **使用示例**：Temporal 提供清晰的方法链式操作，如 `today.add({ days: 1 })`，直接输出格式化日期，无需额外转换，代码更简洁安全。
- 🚀 **发展现状**：Temporal 规范已进入第三阶段，Chrome 和 Firefox 等浏览器开始实验性支持，开发者可提前测试，为未来取代 Date 做准备。

---

### [未找到标题](https://chromium-review.googlesource.com/c/chromium/src/+/7184969)

**原文标题**: [No title found](https://chromium-review.googlesource.com/c/chromium/src/+/7184969)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能整合病历信息，减少行政负担并降低人为失误
- ⚖️ 数据隐私与算法透明度等伦理问题仍需建立相应规范与监管框架

---

### [2026 年前端开发者必须掌握的 4 个 CSS 特性 · 2026 年 1 月 7 日](https://nerdy.dev/4-css-features-every-front-end-developer-should-know-in-2026)

**原文标题**: [4 CSS Features Every Front-End Developer Should Know In 2026 · January 7, 2026](https://nerdy.dev/4-css-features-every-front-end-developer-should-know-in-2026)

本文介绍了 2025 年发布的四个关键 CSS 新特性，这些特性对前端开发者至关重要，包括查询滚动状态、精确控制文本间距、基于兄弟元素位置进行动画延迟以及类型安全的属性值使用。

- 🧑‍💻 **sibling-index() 和 sibling-count()**：允许根据元素在兄弟元素中的位置进行样式计算，例如实现动画延迟效果。
- 📜 **@container scroll-state()**：查询滚动容器的状态（如 stuck、snapped、scrollable、scrolled），用于增强滚动交互体验。
- ✂️ **text-box**：精确控制文本的上下间距，实现像素级对齐，适用于排版和网格布局。
- 🔧 **typed attr()**：类型安全的属性值传递，允许在 CSS 中直接使用 HTML 属性并进行类型验证。

---

### [AI 在编写 React 代码方面究竟有多出色？——Addy Osmani 著](https://addyo.substack.com/p/how-good-is-ai-at-coding-react-really)

**原文标题**: [How Good Is AI at Coding React (Really)? - by Addy Osmani](https://addyo.substack.com/p/how-good-is-ai-at-coding-react-really)

AI 在 React 开发中已具备实用价值，但其能力分布不均，尤其在复杂任务中存在明显“复杂性悬崖”。开发者可通过优化上下文、明确约束和结构化流程，将 AI 从“代码生成器”转变为可控的“协作者”，从而有效提升开发效率与代码质量。

- 📊 **AI 在 React 任务中的表现呈两极分化**：在独立组件、脚手架等简单任务上成功率约 40%，但在多步骤集成任务中骤降至 25%，主要受限于状态管理和设计审美
- 🧠 **逻辑与审美的能力鸿沟**：AI 擅长实现明确需求与数据流，但在设计品味、用户体验等需要审美判断的领域表现较弱
- 🛠️ **工具链与上下文工程是关键杠杆**：通过 MCP 工具（如 Context7、Next.js DevTools）提供实时文档和运行环境信息，可显著提升 AI 输出的准确性和实用性
- 📝 **提示词质量决定输出水平**：具体、结构化的提示（包含组件 API、设计约束、可访问性要求）比模糊指令能产生更高质量的代码
- 🔄 **迭代式工作流优于单次生成**：要求 AI 先提供实施计划，再分步骤生成代码，结合测试和评审，能有效规避“复杂性悬崖”
- 🎨 **设计系统是抵御 AI 审美局限的护城河**：通过固化色彩、间距、组件库等设计令牌，可确保 AI 输出符合团队设计规范
- 🤖 **将 AI 视为需监督的初级工程师**：为其设定明确的任务简报、验收标准和操作沙箱，并保留最终审核权，避免技术债务累积
- 📈 **React 主流技术栈享有 AI 红利**：由于训练数据集中，AI 对 React、TypeScript、Tailwind 等主流组合的支持度最高，偏离该栈则需要更多人工干预
- ⚙️ **性能与可访问性需显式要求**：AI 不会自动优化性能或实现可访问性，必须在提示中明确指定缓存策略、懒加载、ARIA 标签等要求
- 🧪 **测试驱动开发与 AI 协同增效**：先编写测试用例再让 AI 实现功能，既能明确需求，又能自动验证输出正确性

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份为软件工程师精心筛选的每周通讯，汇集高质量技术文章，帮助读者高效获取有价值内容，持续学习新知识。

- 📬 超过 25,505 名软件工程师订阅的每周电子邮件通讯
- 🎯 精选文章并附简短摘要，节省寻找优质内容的时间
- 🌱 每周学习新知识，读者反馈每期都能获得启发
- 👥 涵盖 API 设计等行业热点，受到全球软件工程师认可
- 📅 由 Bonobo Press 自 2013 年持续运营，提供隐私保护服务

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

《Leadership in Tech》是一份面向技术领域领导者的精选通讯，旨在通过每周两期的邮件内容，帮助 CTO、工程经理和高级工程师提升领导力，节省寻找优质内容的时间，并持续学习新知识。

- 📧 每周一和周四发送，已吸引超过 28,876 名工程领导者订阅  
- 🎯 内容经人工精选，附简短摘要，聚焦领导力建设、架构讨论和沟通技巧等主题  
- ⏱️ 帮助读者节省筛选内容的时间，每周都能学到新知识  
- 💬 读者反馈积极，特别赞赏其对授权技能等关键领导力话题的深入探讨  
- 🌍 受到全球科技领域领导者的广泛阅读与认可

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

《C#文摘》是一份面向.NET开发者精心策划的每周通讯，提供精选文章与摘要，帮助超过20,369名工程师高效学习新知、节省时间。

- 📰 每周精选推送：为.NET 开发者精心筛选文章，附简短摘要
- ⏱️ 高效省时：帮助用户快速获取有价值内容，避免信息过载
- 🧠 持续学习：每周更新，让开发者不断掌握新知识技能
- 👥 社群认可：读者反馈在实际工作中应用推荐内容，分享给同行
- 🌍 广泛受众：受到全球.NET 工程师群体的订阅与阅读

---

### [让开发者保持最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为超过 93,000 名软件开发者、IT 专业人士和技术人员提供最新资讯的软件通讯出版商。

- 📰 发布面向开发者、工程经理、技术主管和 CTO 的精选通讯，以简洁清晰的内容节省读者时间
- 🎯 提供广告服务，帮助客户触达软件工程师、团队领导、工程经理、CTO 等精准技术受众
- 📬 支持通过媒体资料包了解广告合作详情，并提供联系渠道供咨询、建议或合作洽谈

---

### [过往通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

《React Digest》是一份专注于 React 生态的电子简报，汇总了 2025 年 8 月至 2026 年 1 月期间的关键技术动态、性能优化、安全更新及开发实践。

- 🛠️ 探讨 React 组件逆向、状态管理优化（如 useEffectEvent）及 React Conf 2025 的最新分享
- 🤖 分析 AI 在 React 编码中的实际能力与局限，涵盖前端测试和类型安全组件
- 🏆 精选 2025 年热门文章，聚焦设计模式、状态管理与函数式编程
- 🚨 总结 React 漏洞教训，介绍服务端组件与性能优化策略
- ⚡ 详解 React 19.2 的 INP 优化，对比 TanStack 与 Next.js 等框架
- 🔒 关注 React 与 Next.js 的安全漏洞，探讨设计系统与 Hook 改进
- ♿ 介绍自动化无障碍测试、派生状态简化及 API 抽象实践
- 🧪 分享从 Enzyme 迁移至 React 测试库的经验与异步测试方案
- 🚀 解析 React 19.2 新特性，如自动优化、错误处理与定时器同步
- 🌐 探讨 URL 状态管理、多语言应用优化与原子状态性能提升
- ⚙️ 深入 JavaScript 指令、React 与 Remix 演进，以及 Portal 浮层 UI 技术
- ⚡ 评估服务端组件的性能影响，介绍 Rari SSR 与 GraphQL 实践
- 🔄 探索状态序列化技巧、useContext 应用与 TanStack 路由继承
- ⚡ 优化 Suspense 与 useSyncExternalStore，改进数据获取策略
- 🎨 剖析渲染行为细节，掌握 useEffectEvent 与 useState 机制
- 📊 展望 2025 年状态管理趋势，融合 Elm 理念与 3D 应用开发
- 🏆 反思 React 生态垄断，分析样式库性能与服务端组件案例
- 💾 引入 TanStack DB 响应式存储，分享 React Native 迁移与 SEO 优化
- 🛠️ 探索无框架服务端组件支持、AI 代码审查与 Astro 中间件
- ⚡ 综述并发特性，介绍全栈框架、Next.js 自托管及表单 Hook

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了 React Digest 如何收集、使用和保护用户的个人信息，重点在于透明、合法和有限度的数据处理，并提供了用户行使权利的具体途径。

- 🔍 在收集个人信息前会明确告知收集目的，并仅用于指定或兼容的目的。
- 📧 仅收集用户的电子邮件地址，用于发送新闻简报，不作他用。
- 🛡️ 采取合理的安全措施保护个人信息，防止丢失、盗窃或未经授权的访问。
- 📜 遵循数据最小化原则，仅在必要时保留个人信息，并确保其准确、完整和最新。
- 👶 严格遵守 COPPA，不收集或存储 13 岁以下儿童的信息。
- 📬 用户可随时通过邮件联系以获取、更正或删除其存储的个人信息。
- 🚫 坚决反对垃圾邮件，提供明确的退订方式，尊重用户选择。

---

### [媒体资料包 – 博诺博出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为技术专业人士提供高参与度的新闻通讯广告服务，通过精心策划的内容连接广告商与目标受众，涵盖软件工具、招聘、会议等多种广告类型，旨在提升品牌曝光、潜在客户和转化率。

- 📧 **新闻通讯表现卓越**：各新闻通讯的打开率和点击率均高于行业基准，通过严格的列表清理确保读者高参与度。
- 👥 **精准定位受众**：提供四类新闻通讯，分别针对技术领导者、全栈开发者、C#/.NET 开发者和 React 前端开发者，受众覆盖决策者和各级别工程师。
- 💰 **透明计价与高性价比**：提供详细的费率卡，包括订阅数、打开率、点击率、赞助价格和每次点击成本，其中 C# Digest 的 CPC 最低（$1.93-$2.97）。
- 🌍 **全球受众分布**：订阅者主要来自欧洲和美国，在科技、金融、医疗等多个行业的知名公司任职。
- 📝 **简洁广告格式**：采用纯文本广告，包含链接、标题和描述，强调内容简洁性以优化互动效果。
- 🔄 **系统化合作流程**：从需求沟通、档期规划、付款锁定到广告上线和效果报告，提供完整的赞助合作流程。
- 🤝 **知名合作伙伴**：与 Okta、GitLab、MongoDB 等众多行业领先品牌有成功合作案例，且重复赞助率高。

---

