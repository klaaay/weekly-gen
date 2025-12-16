### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份为 React 开发者精心策划的每周通讯，汇集了前端工程师精选文章与摘要，帮助读者高效学习新知、节省时间。

- 📰 每周为超过 24,760 名前端工程师推送精选文章摘要
- ⏱️ 提供手选内容与简短总结，帮助读者节省寻找优质信息的时间
- 🆕 每周更新，确保读者持续学习 React 领域新知识
- 👍 读者反馈积极，认可内容实用性与时效性（如并发模式等深度解析）
- 🌍 服务全球前端工程师群体，由 Bonobo Press 自 2013 年持续运营

---

### [React 2025 年度回顾摘要](https://docs.google.com/forms/d/e/1FAIpQLSem_IPgZ7LQskF49lKpkKycWsLFAxd4WEkC3TpHjpExSiJhLg/viewform?usp=dialog)

**原文标题**: [React Digest 2025 Review](https://docs.google.com/forms/d/e/1FAIpQLSem_IPgZ7LQskF49lKpkKycWsLFAxd4WEkC3TpHjpExSiJhLg/viewform?usp=dialog)

这是一份关于《React Digest 2025》的读者反馈调查问卷。

- 📝 **问卷目的**：收集读者反馈，以帮助改进 2026 年的通讯内容。
- ⏱️ **时间承诺**：所有问题均为选填，预计完成时间不超过 5 分钟。
- 🔐 **登录要求**：受访者需要登录 Google 账户以保存进度。
- ⭐ **核心问题**：调查内容包括对通讯整体价值、工作影响、最受欢迎的文章/主题、分享行为以及内容偏好（如技术深度、教程、库等）的评价。
- ✂️ **格式反馈**：包含对通讯长度的看法（太短、刚好、太长）。
- 📄 **问卷结构**：该页面为问卷的第一页（共三页），由 Bonobo Press 创建。

---

### [React 19.2：INP 优化再进一步 - 网页性能日历](https://calendar.perfplanet.com/2025/react-19-2-further-advances-inp-optimization/)

**原文标题**: [  React 19.2. Further Advances INP Optimization - Web Performance Calendar](https://calendar.perfplanet.com/2025/react-19-2-further-advances-inp-optimization/)

React 19.2 引入了新组件 `<Activity>` 和 Chrome DevTools 中的性能轨道，帮助开发者优化交互到下一次绘制（INP）指标，提升应用性能。

- 🎭 **Activity 组件**：通过 `mode` 参数（`hidden`/`visible`）管理组件可见性，隐藏时保留状态且避免卸载，减少渲染负担。
- 🚀 **状态与 DOM 保留**：隐藏组件时应用 `display:none`，保持本地状态和 DOM 状态（如输入内容），同时移除副作用以降低负载。
- ⏱️ **低优先级更新**：隐藏组件的更新被设为最低优先级，确保用户交互不受影响，提升响应速度。
- 🔄 **预渲染与选择性水合**：支持类似 `<Suspense>` 的预渲染和选择性水合，加速 UI 显示并优化性能。
- ⚠️ **SSR 注意事项**：服务器端渲染时不输出隐藏组件，可能影响 SEO，需谨慎用于关键内容。
- 📊 **性能轨道工具**：Chrome DevTools 新增集成时间线，可视化 React 事件、组件渲染和服务器操作，简化性能调试。
- 🔍 **调度器与组件轨道**：帮助识别级联更新和过度渲染问题，通过火焰图分析组件性能影响。
- 🌐 **服务器轨道**：支持 React 服务器组件，监控 SSR 期间的 Node.js 操作，优化混合应用性能。

---

### [雷达 — WorkOS](https://workos.com/radar?utm_source=reactdigest&utm_medium=newsletter&utm_campaign=q42025)

**原文标题**: [Radar â WorkOS](https://workos.com/radar?utm_source=reactdigest&utm_medium=newsletter&utm_campaign=q42025)

Radar 是一款实时威胁检测与防护工具，专为应用提供针对机器人、欺诈和滥用行为的全面安全防护，通过先进的设备指纹识别和自适应策略，保障用户账户与业务安全。

- 🤖 实时防护机器人、欺诈与滥用行为，检测并阻止 AI 机器人、账户滥用和凭证盗窃等威胁
- 🛡️ 自动拦截常见攻击如凭证填充和暴力破解，支持根据应用需求灵活定制防护设置
- 📱 通过设备指纹技术分析 20 多种信号，精准区分真实用户与恶意行为者
- 🔒 覆盖多种防护场景：未知设备登录挑战、休眠账户保护、免费试用滥用检测、异地登录识别等
- 💰 提供透明定价，首 1000 次检测免费，后续按量计费，支持企业级定制方案
- ⚡ 具备高可用性（99.99% 运行时间保证）和专家支持服务，可快速集成部署

---

### [奥斯卡 - 加布里埃尔 - 德夫](https://oscargabriel.dev/blog/skeletons-in-my-codebase)

**原文标题**: [oscar-gabriel-dev](https://oscargabriel.dev/blog/skeletons-in-my-codebase)

本文分享了在构建 Better Chat 应用时，结合 TanStack Router 和 Better Auth 库解决前端架构中常见问题的实践经验，重点介绍了路由组织、认证防闪烁和前端优化三个核心模式。

- 🗂️ **路由组织**：采用基于功能的`route.tsx`作为布局，通过父路由共享认证守卫、加载状态和错误处理，避免路径冲突并实现功能内聚。
- ⚡ **认证防闪烁**：使用异步守卫（`async beforeLoad`）等待认证状态解析，消除页面跳转时的闪烁问题，配合`pendingComponent`提供流畅加载体验。
- 🎨 **前端优化**：为所有路由设置`pendingComponent`和`errorComponent`，通过`validateSearch`验证搜索参数，并利用`loader`预取数据以提升性能。
- 🔒 **安全与性能**：在认证流程中验证并清理重定向参数，利用 Better Auth 的`cookieCache`将认证检查时间控制在 10 毫秒内，确保生产环境高效运行。
- 🛠️ **模式总结**：强调正确使用库的各项功能（如`beforeLoad`、`loader`、`validateSearch`等），避免职责重叠，以构建可维护且高性能的生产级应用。

---

### [React 中 useEffectEvent 的注意事项](https://slicker.me/react/useEffectEvent.html)

**原文标题**: [Do's and Don'ts of useEffectEvent in React](https://slicker.me/react/useEffectEvent.html)

useEffectEvent 是一个 React Hook，用于从 Effect 中提取非响应式逻辑，允许在 Effect 内读取最新的 props 或 state 值，而不会因这些值的变化导致 Effect 重新执行。

- 🎯 **解决核心问题**：在 Effect 中读取最新值（如主题或用户偏好）时，避免将其加入依赖数组，防止不必要的重新运行。
- 🔧 **关键机制**：创建一个稳定的函数引用，始终读取最新值，但不会触发 Effect 重新执行。
- ✅ **正确用法**：在 Effect 内直接调用、用于读取最新 props/state、分离响应式与非响应式逻辑、与清理逻辑结合使用。
- ❌ **避免用法**：在常规事件处理程序、渲染过程中、异步调用或延迟后调用，或将其作为 prop 传递给其他组件。
- 📊 **常见用例**：日志记录与分析、使用最新状态的回调、基于最新值的防抖处理。
- ⚠️ **注意事项**：仅在确实需要读取非响应式值时使用，保持函数目的单一，等待稳定版再用于生产环境。

---

### [TanStack Start：Next.js 的新竞争者 | 翁德雷·维利塞克](https://ondrejvelisek.github.io/tanstack-start-new-competitor-to-nextjs/)

**原文标题**: [TanStack Start: New competitor to Next.js | Ondrej Velisek](https://ondrejvelisek.github.io/tanstack-start-new-competitor-to-nextjs/)

TanStack Start 与 Next.js 在路由类型安全、数据获取和性能等方面各有优劣。Start 在开发体验和类型安全上更优，而 Next.js 在静态内容性能上表现更佳。

- 🛣️ **路由类型安全**：TanStack Start 提供全面的端到端类型安全，支持动态参数和查询参数的类型推断；Next.js 的 typedRoutes 功能虽已引入，但在动态路由和查询参数方面仍存在类型覆盖不全的问题。
- 🔄 **数据获取方式**：Next.js 使用异步组件，语法简洁；Start 推荐结合 TanStack Query，提升组件独立性和可复用性，但代码稍显冗长。
- ⚡ **性能与捆绑大小**：Next.js 支持 React 服务器组件，默认实现更小的客户端捆绑大小和更快的交互时间；Start 目前不支持服务器组件，所有代码均需发送至客户端。
- 🧩 **缓存与预渲染**：Next.js 提供完整的缓存层级和缓存组件支持，优化静态和动态混合页面的性能；Start 支持大部分缓存，但在缓存失效和缓存组件方面功能较弱。
- 🏗️ **适用场景**：Next.js 更适合静态网站或对性能要求极高的业务场景；TanStack Start 在开发体验和维护性上更优，适用于大多数动态应用。

---

### [React 代理抓取工具](https://www.react-grab.com/blog/agent)

**原文标题**: [React Grab for Agents](https://www.react-grab.com/blog/agent)

React Grab 现已推出面向智能编码代理的版本，允许用户直接在浏览器中与代理交互并编辑代码，无需切换工具或复制粘贴，大幅提升了前端开发的效率。

- 🚀 **功能升级**：React Grab 现在支持在浏览器中直接启动 Claude Code、Cursor 等智能代理，通过点击页面元素即可获取精确的 React 上下文和文件路径，并直接向代理发送编辑指令。
- ⚡ **效率提升**：新版本让代理能够直接编辑代码，无需离开浏览器，支持同时运行多个 UI 任务，每个任务都关联到用户点击的特定元素，使代理处理 UI 任务的速度平均提升了约 3 倍。
- 🛠️ **易于集成**：通过简单的 CLI 命令即可安装，支持多种主流编码代理（如 Claude Code、Cursor、OpenCode 等），并提供详细的服务器和客户端设置指南。
- 🔧 **工作原理**：React Grab 在用户选择元素时，会遍历 React 组件树，收集组件名称、源代码位置及周边 DOM 信息，然后将这些上下文与用户提示一起发送给代理服务器进行代码编辑。
- 🔮 **未来展望**：团队正在开发名为 Ami 的专用 UI 代理，旨在与 React Grab 深度集成，进一步优化对组件层次和设计系统的理解与编辑能力。

---

### [Frontegg AgentLink：为 SaaS 提供安全的 AI 代理访问](https://frontegg.com/product/agentlink?utm_source=react_digest&utm_medium=email&utm_campaign=agentlink_dec25)

**原文标题**: [AgentLink by Frontegg: Secure AI Agent Access for SaaS](https://frontegg.com/product/agentlink?utm_source=react_digest&utm_medium=email&utm_campaign=agentlink_dec25)

Frontegg 推出 AgentLink，这是一个低代码通信与控制层，旨在让 SaaS 产品安全地接入生成式 AI 代理（如 ChatGPT、Claude 和 Gemini），通过 MCP 协议转换 API 工具、执行代理专属的防护规则并提供完整的可视性与审计追踪，从而在拥抱 AI 新入口的同时确保企业级的安全管控。

- 🤖 **快速接入 AI 代理**：通过 Agent Connector 在几分钟内创建托管 MCP 服务器，让 ChatGPT 等平台安全连接至您的应用。
- 🛡️ **内置安全防护**：Agent IAM 提供细粒度的代理防护规则与数据保护，防止代理越权操作，无需对普通用户施加相同限制。
- 📊 **全面行为监控**：Agent Analytics 提供代理使用产品的详细观察能力，包括工具使用情况与异常检测，确保策略有效执行。
- 🚀 **一站式代理构建**：AI Agent Builder 集成身份管理、MCP 等功能，支持在几分钟内创建企业级 AI 代理，加速从概念到产品的转化。
- 🔗 **无缝集成现有产品**：可将现有 API 快速转换为代理可理解的 MCP 语言，助力企业安全、高效地参与 AI 革命。

---

### [Patterns.dev](https://www.patterns.dev/)

**原文标题**: [Patterns.dev](https://www.patterns.dev/)

本文介绍了 JavaScript、React 和 Vue.js 中的多种设计模式与优化技术，涵盖代码组织、性能提升和框架特性。

- 🏗️ JavaScript 设计模式：包括单例、代理、原型、观察者等，用于优化代码结构和对象管理
- ⚡ 加载优化策略：如动态导入、按需加载、代码分割和预加载，以提升应用性能
- 🔧 React 模式：涵盖容器/展示、高阶组件、钩子、服务端渲染等，用于构建可维护的 React 应用
- 🌳 Vue.js 模式：包括组件、组合式函数、依赖注入等，专注于 Vue 应用的模块化和状态管理
- 🚀 性能优化技术：如树摇、列表虚拟化、压缩脚本和第三方优化，以减少资源消耗并改善用户体验

---

### [使用 JSDoc 探索 JavaScript 类型化的细微差别 | That HTML 博客](https://thathtml.blog/2025/12/nuances-of-typing-with-jsdoc/)

**原文标题**: [The Nuances of JavaScript Typing using JSDoc | That HTML Blog](https://thathtml.blog/2025/12/nuances-of-typing-with-jsdoc/)

作者偏好使用 JavaScript 而非 TypeScript，认为代码应专注于行为，而类型信息应作为文档的一部分。通过 JSDoc 注释，可以在 JavaScript 中获得 TypeScript 的类型检查优势，无需编写.ts 文件。结合`// @ts-check`、`tsc`工具和配置文件（如`jsconfig.json`、`tsconfig.json`），可以在 IDE 和 CI 流程中实现类型提示与检查。JSDoc 支持多种类型标注场景，如类构造函数、对象记录、循环变量和类型导入，同时允许用`// @ts-ignore`忽略特定错误。作者主张将 JavaScript + JSDoc + tsc 作为行业默认，以保持代码的 Web 标准兼容性，同时享受类型系统的益处。

- 🚀 作者更偏爱 JavaScript，认为类型应作为文档而非代码的一部分，提倡用 JSDoc 进行注释
- 🔧 通过`// @ts-check`和 JSDoc 注释，在纯 JavaScript 中实现 TypeScript 的类型检查功能
- ⚙️ 配置`jsconfig.json`和`tsconfig.json`文件，结合`tsc`工具进行类型检查和声明文件生成
- 📝 JSDoc 支持多种类型标注，如类参数、对象记录、内联类型和类型导入（`@typedef`）
- 🛡️ 必要时可使用`// @ts-ignore`忽略类型错误，平衡灵活性与类型安全
- 🌐 主张以 JavaScript + JSDoc + tsc 为行业默认，减少构建依赖，保持 Web 标准兼容性

---

### [使用 Invoker Commands API 控制对话框和弹出层 - HTMHell](https://htmhell.dev/adventcalendar/2025/7/)

**原文标题**: [Controlling dialogs and popovers with the Invoker Commands API - HTMHell](https://htmhell.dev/adventcalendar/2025/7/)

Invoker Commands API 为 `<button>` 元素新增了 `command` 和 `commandfor` 属性，允许开发者无需编写 JavaScript 即可控制对话框和弹出层的显示与隐藏。该 API 简化了交互元素的实现，支持模态对话框和弹出层的标准操作，并允许创建自定义命令以扩展功能。

- 🚀 **无需 JavaScript**：通过新增的 `command` 和 `commandfor` 属性，可直接在 `<button>` 元素上控制对话框和弹出层，无需编写额外代码。
- 🗣️ **对话框与弹出层区别**：对话框通常包含需用户执行的操作，且必须显式关闭；弹出层则用于短暂信息展示，可点击外部轻量关闭。对话框支持模态/非模态，而弹出层默认为非模态。
- ⚙️ **支持的命令类型**：包括 `show-modal`、`close`、`request-close`（触发 `cancel` 事件）、`show-popover`、`hide-popover`、`toggle-popover`，以及以 `--` 前缀开头的自定义命令。
- 💡 **自定义命令扩展**：开发者可创建自定义命令（如 `--toggle-details`）并通过 JavaScript 事件监听器实现特定功能，扩展 API 的适用场景。
- 🌐 **浏览器支持与向前兼容**：截至 2025 年底，API 已在 Chrome、Edge、Opera、Firefox 及 Safari Technology Preview 中实现，并为旧版浏览器提供了 polyfill 以确保兼容性。
- 🔮 **未来展望**：API 作者已发布规划文档，未来可能增加对 `<details>` 元素、原生日期选择器及媒体控件的命令支持，并鼓励社区提交功能建议。

---

### [错误](https://www.maxdesign.com.au/articles/two-trees.html)

**原文标题**: [Error](https://www.maxdesign.com.au/articles/two-trees.html)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='www.maxdesign.com.au', port=443): Max retries exceeded with url: /articles/two-trees.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [非正方形图像模糊扩展 – Frontend Masters 博客](https://frontendmasters.com/blog/non-square-image-blur-extensions/)

**原文标题**: [Non-Square Image Blur Extensions – Frontend Masters Blog](https://frontendmasters.com/blog/non-square-image-blur-extensions/)

本文探讨了为非正方形图像创建模糊扩展效果的多种 CSS 技术，从简单的单元素解决方案到考虑浏览器兼容性和额外视觉效果的复杂实现。

- 🖼️ 通过设置 `width: min(100%, 23em)`、`aspect-ratio: 1`、`object-fit: contain` 和 `background` 属性，仅用四个 CSS 声明即可实现基础模糊扩展效果。
- 🚫 由于 `filter()`、`src()` 和增强版 `attr()` 函数的浏览器支持有限，上述理想方案目前无法跨浏览器使用。
- 🔄 当前可行的跨浏览器方案需要额外包装元素，使用 CSS 变量传递图像 URL，并通过 `backdrop-filter` 在包装层实现模糊效果。
- 🌫️ 若需添加图像边缘淡出效果，则需更复杂的结构，可能涉及伪元素、遮罩或 SVG 滤镜，并需处理图像方向未知的情况。
- 📐 当已知图像宽高比时，可使用 `sign()` 函数计算遮罩渐变角度；未知时，可通过额外元素和容器查询来动态获取并应用相应样式。

---

### [网页性能报告剖析 - 网页性能日历](https://calendar.perfplanet.com/2025/the-anatomy-of-a-web-performance-report/)

**原文标题**: [  The Anatomy of a Web Performance Report - Web Performance Calendar](https://calendar.perfplanet.com/2025/the-anatomy-of-a-web-performance-report/)

本文介绍了 Web 性能报告的结构与价值，强调优秀报告应通过清晰叙事将复杂数据转化为可操作的见解，帮助不同角色理解性能现状、问题根源及优化方向。

- 🖼️ **测试背景**：报告开篇明确测试环境（URL、地点、设备、时间），为后续指标提供解读框架，避免数据脱离实际意义。
- 📊 **优化评分**：通过压缩、缓存、CDN 使用等关键优化项的评分，快速识别是否遵循最佳实践及是否存在低垂果实。
- 📚 **学习资源**：报告包含精选文章与案例链接，鼓励团队持续学习，将技术报告转化为知识共享工具。
- ⚠️ **实验室核心性能指标**：展示 LCP、CLS、TBT 等受控环境数据，作为早期预警系统，快速发现性能回归。
- 🌍 **真实用户核心性能指标**：基于 CrUX 的现场数据反映全球用户实际体验，揭示网络、设备、地域等因素对性能的影响。
- 🤖 **AI 洞察**：整合所有数据生成易于理解的执行摘要，直接说明改进点、问题、影响及行动建议，降低决策门槛。
- 🧩 **Lighthouse 综合评分**：涵盖可访问性、最佳实践、SEO 等维度，揭示与性能相关的跨领域质量问题。
- ⏱️ **性能时间线**：列出 TTFB、首次渲染、速度指数等关键加载里程碑，帮助定位延迟累积的具体阶段。
- 📦 **资源构成分析**：按类型（JS、CSS、图片等）分解页面资源大小，直观暴露导致性能问题的资源权重分布。
- 🔗 **完整测试链接**：提供深入查看瀑布图、日志等详细数据的入口，在保持报告简洁的同时满足深度排查需求。

---

### [设计可访问性：'lang'属性的作用 - HTMHell](https://htmhell.dev/adventcalendar/2025/6/)

**原文标题**: [Accessible by Design: The Role of the 'lang' Attribute - HTMHell](https://htmhell.dev/adventcalendar/2025/6/)

文章讨论了 HTML 中`lang`属性的重要性，强调它是确保网页可访问性的关键细节，尤其对屏幕阅读器、盲文显示器和翻译工具的用户至关重要。缺少该属性会导致内容无法被正确解读，违反 WCAG 标准，并影响多种辅助技术的使用效果。

- 🌐 `lang`属性用于声明网页语言，帮助浏览器和屏幕阅读器正确解读内容，缺失会造成可访问性障碍
- 📊 根据 WebAIM 百万报告，缺失语言属性连续七年成为常见可访问性问题之一，影响 15.8% 的首页
- 🔊 屏幕阅读器依赖`lang`属性选择合适语音包，缺失会导致错误发音，使内容难以理解
- 📜 WCAG 3.1.1 准则要求明确页面语言，这是基础可访问性的强制标准
- 🔤 该属性还影响盲文显示器的翻译规则、自动翻译工具的准确性，以及引号和连字符的正确渲染
- 🌍 对于多语言页面，可在特定元素上设置`lang`属性，确保辅助技术能切换语言
- ⚙️ 在现代前端框架中，需在根模板文件（如`index.html`）的`<html>`标签中设置`lang`属性

---

### [React2Shell (CVE-2025-55182)：关键 React 漏洞 | Wiz 博客](https://www.wiz.io/blog/critical-vulnerability-in-react-cve-2025-55182)

**原文标题**: [React2Shell (CVE-2025-55182): Critical React Vulnerability | Wiz Blog](https://www.wiz.io/blog/critical-vulnerability-in-react-cve-2025-55182)

React2Shell（CVE-2025-55182）是一个影响 React 服务器组件（RSC）“Flight”协议的严重远程代码执行（RCE）漏洞，已在野外被积极利用。该漏洞源于不安全的反序列化，允许攻击者通过特制的 HTTP 请求在默认配置下执行任意代码。Wiz 数据显示，39% 的云环境中存在易受攻击的实例。攻击者已利用该漏洞进行云凭证窃取和加密货币挖矿等活动。建议立即升级 React 和 Next.js 至已修复的版本。

- 🚨 **漏洞概述**：CVE-2025-55182 是 React 服务器组件（RSC）中的严重未认证 RCE 漏洞，源于不安全的反序列化，默认配置即可被利用。
- 🌐 **影响范围**：主要影响 React 19 生态系统及 Next.js 等框架，Wiz 数据显示 39% 的云环境存在易受攻击实例。
- ⚠️ **野外利用**：自 2025 年 12 月 5 日起，攻击者已积极利用该漏洞进行云凭证窃取、部署恶意软件（如 Sliver 框架）和加密货币挖矿（如 XMRig）。
- 🔧 **受影响产品**：包括 React 19.0.x 至 19.2.x、Next.js 14.3.0-canary.77 及更高版本，以及 Vite、Parcel 等集成 RSC 的框架。
- 🛡️ **缓解措施**：立即升级 React 至 19.0.1/19.1.2/19.2.1，Next.js 至相应修复版本；使用 Wiz 等工具进行漏洞检测和运行时防护。
- 📊 **攻击趋势**：攻击始于 2025 年 12 月初，涉及自动化扫描和针对性入侵，中国关联组织及多起加密货币挖矿活动已被观测到。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份面向软件工程师的每周精选简报，旨在通过筛选优质内容帮助读者高效学习新知。

- 📬 超过 23,517 名软件工程师订阅这份每周邮件
- 🧠 每期提供附简短摘要的精选文章，节省寻找有价值内容的时间
- 🎯 内容涵盖 API 设计等实用主题，读者反馈能每周获得新知识
- 🌍 订阅者包括全球各地软件工程师，由 Bonobo Press 自 2013 年持续运营

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

该通讯为技术领导者提供精选内容，旨在帮助提升领导力，每周通过邮件推送，节省读者寻找优质信息的时间，并广受业界好评。

- 📰 每周为 CTO、工程经理和高级工程师推送精选领导力内容
- 👥 已吸引超过 27,959 名工程领导者订阅
- ⏱️ 通过文章摘要帮助读者高效获取有价值信息
- 📚 每周持续提供新知识，涵盖架构、会议、沟通等实用主题
- 🌟 用户反馈积极，特别认可其在软件领域领导力内容的独特汇编
- 🏢 服务由 Bonobo Press 运营，备受科技行业领导者信赖

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

《C# Digest》是一份专为.NET 开发者精心策划的每周通讯，提供精选文章与摘要，帮助读者高效学习新知并节省时间。

- 📰 每周为.NET 开发者推送精选文章与简短摘要
- ⏱️ 节省寻找有价值内容的时间，每周学习新知识
- 👥 已吸引超过19,511名C#工程师订阅
- 💬 读者反馈积极，内容包括功能标志、LINQ 等实用主题
- 🌍 受到全球.NET 工程师的广泛阅读

---

### [让开发者保持最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者、IT 专业人士和技术人员提供最新资讯的媒体公司，通过每周发布的精选简报服务超过 93,000 名订阅者，帮助读者高效获取行业动态，并为广告商提供精准触达技术决策者的渠道。

- 📰 自 2013 年起持续为超过 93,000 名软件开发者、IT 专业人士和技术人员提供最新行业资讯
- 📧 每周发布精选简报，内容简洁清晰，帮助工程师、技术主管和 CTO 高效节省时间
- 📢 为广告商提供精准广告服务，可触达软件工程师、技术团队领导和 IT 决策者等目标人群
- 📄 提供媒体资料包和广告合作渠道，支持产品与服务推广
- 📞 开放咨询、建议与广告合作联系渠道

---

### [过往通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

本期 React Digest 汇总了 2025 年 8 月至 12 月的关键内容，涵盖 React 19.2 的 INP 优化、性能提升、状态管理、安全漏洞及框架对比等前沿话题。

- 🚀 React 19.2 推出 INP 优化，提升交互性能
- ⚠️ 揭露 React 与 Next.js 的关键安全漏洞
- ♿ 探讨 React 自动化无障碍测试方案
- 🔄 分享从 Enzyme 迁移至 React Testing Library 的经验
- ⚛️ 深入 React 19.2 新特性，如自动优化与错误处理
- 🌐 分析 URL 作为状态管理的优势
- 🧩 解析 JavaScript 指令与平台边界问题
- ⚡ 评估 React 服务端组件的性能提升效果
- 🔄 探讨序列化与反序列化在状态管理中的应用
- ⏱️ 使用 useSyncExternalStore 优化并发水合过程
- 🎨 剖析 React 渲染行为的细微差别
- 📊 展望 2025 年 React 状态管理趋势
- 🏆 讨论 React 主导地位对创新的影响
- 🗃️ 介绍 TanStack DB 的交互式指南
- 🛠️ 探索无框架的 React 服务端组件支持
- 🔄 概述 React 并发功能
- ⏰ 分析非跳跃时钟与 hydration 影响
- 💾 强调缓存对 React 一致性的重要性
- 👷 利用 Web Workers 提升 React 性能
- 🎣 重新评估 useCallback 的实际效用

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了 React Digest 如何收集、使用和保护用户的个人信息，重点在于通过合法、透明的方式管理用户数据，并确保用户对其信息拥有控制权。

- 🎯 明确收集目的：在收集个人信息前，会明确告知收集目的。
- 🔒 限定使用范围：仅将信息用于指定或相关目的，未经同意不另作他用。
- ⏳ 限制保留时间：仅在实现目的所需时间内保留个人信息。
- ⚖️ 合法公平收集：通过合法、公平的方式，并在适当时征得用户同意后收集信息。
- 📊 确保数据质量：确保个人数据准确、完整且及时更新，以满足使用需求。
- 🛡️ 加强安全保护：采取合理安全措施，防止信息丢失、被盗或未经授权的访问、披露等。
- 📢 公开政策实践：向用户清晰说明个人信息管理相关的政策和做法。
- 📧 仅收集邮箱：为发送周刊，仅收集用户邮箱地址，不作他用。
- 🚫 禁止儿童数据：不故意收集或存储 13 岁以下儿童的信息，网站也不针对该年龄段设计。
- 📬 支持信息查询：用户可依据英国《数据保护法》要求获取所存储的个人信息。
- 🗑️ 允许数据删除：用户可请求删除其个人数据。
- 📭 反对垃圾邮件：仅将邮箱用于发送周刊，用户可随时退订，坚决反对任何形式的垃圾邮件。

---

### [媒体资料包 – 博诺博出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为技术专业人士提供高参与度的新闻简报广告服务，通过精准定位帮助广告商接触目标受众并提升转化率。

- 📧 **新闻简报与高参与度**：提供多个技术主题的周报，读者参与度远超行业基准，通过严格列表清理确保受众质量。
- 🎯 **精准受众定位**：简报覆盖软件开发者、工程经理、CTO 等决策者，订阅者多来自欧美，任职于 Google、Amazon 等知名公司。
- 💰 **详细广告报价**：包含四份主要简报的订阅数、打开率、点击率、赞助价格及点击成本，提供透明化的数据参考。
- 📝 **简洁广告格式**：采用纯文本广告形式，要求链接、标题和简短描述，强调文案需在发布前 4 天提交。
- 🔄 **标准化订购流程**：从需求沟通、排期规划、发票支付到广告上线与效果报告，提供清晰的合作步骤。
- 🤝 **广泛合作伙伴**：已与 Okta、GitLab、MongoDB 等多个领域的知名品牌成功合作，常见重复赞助。
- 📬 **联系与合作邀请**：鼓励广告商提前几周联系以确保排期，旨在共同优化广告效果并实现目标。

---

