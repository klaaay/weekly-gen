### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

React Digest 是一份面向 React 开发者的精选周报，汇集前端领域优质内容，帮助开发者高效获取行业新知。

- 📧 每周为 24,715+ 前端工程师推送精选文章合集
- ⏱️ 通过人工筛选与摘要提炼，节省用户搜寻有价值内容的时间
- 🌱 每周持续更新前沿知识，助力开发者技能成长
- 👍 获得用户积极反馈，内容涵盖并发模式等深度技术解析
- 🌍 服务全球前端开发者群体，由 Bonobo Press 专业运营

---

### [移山之路：从 Enzyme 迁移至 React Testing Library 的实践](https://product.hubspot.com/blog/migrated-from-enzyme-to-react-testing-library)

**原文标题**: [Moving Mountains: How We Migrated from Enzyme to React Testing Library](https://product.hubspot.com/blog/migrated-from-enzyme-to-react-testing-library)

本文详细介绍了团队如何用两年半时间将超过 76,000 个测试用例从 Enzyme 迁移到 React Testing Library 的完整过程，包括规划策略、教育推广、执行方法和规模化迁移经验。

- 🚨 **技术迭代**：Enzyme 因缺乏 React 18 官方支持而被淘汰，团队在 2022 年正式采用 React Testing Library 作为新测试框架
- 📊 **规模评估**：通过运行时监控将 500 多个代码包按测试量分为 6 个等级，优先处理低复杂度模块
- 🎯 **理念转变**：从测试组件内部实现转向模拟用户交互的测试哲学，通过内部讲座推广测试奖杯理论
- 🛠️ **执行策略**：禁止新增 Enzyme 测试，在 PR 中自动标注测试改动，通过测试报告器实时展示迁移进度
- 🤝 **协作模式**：采用专项小组 + 跨团队嵌入机制，为关键团队提供 1-2 周集中迁移支持
- ⚡ **效能提升**：专用工具链减少模拟数据创建成本，Monarch 系统统一管理跨团队迁移战役
- 🤖 **AI 应用**：虽未在本次迁移中大规模使用 AI，但后续已在设计系统升级等场景验证其价值
- ✅ **成果验收**：2025 年 2 月完成全部迁移，为 Suspense、React 编译器等现代特性铺平道路

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=react_digest)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=react_digest)

Meticulous AI 是一款通过记录用户操作自动生成测试用例的智能测试工具，无需编写或维护测试代码，可全面覆盖应用程序的所有边缘场景和用户流程。

- 🚀 **自动生成测试** - 通过记录开发过程中的用户交互行为，AI 自动创建持续演进的测试套件
- 🎯 **全面覆盖** - 追踪代码执行路径，覆盖所有用户流程、边缘案例和代码行
- ⚡ **零维护测试** - 测试套件随应用程序演进自动更新，无需手动修复或维护
- 🔒 **无干扰测试** - 通过模拟后端响应实现无副作用测试，避免误报
- 🏃 **极速执行** - 基于 Chromium 的确定性调度引擎，支持大规模并行测试
- 🔧 **轻松集成** - 支持 NextJS、React、Vue 等主流框架，几分钟即可完成配置
- 📊 **实时验证** - 在代码合并前预览对现有工作流程的影响
- 🏢 **企业认可** - 已被 Dropbox、Notion 等 100 多家机构采用

---

### [测试异步 React RSC 组件 | 前端测试方法](https://howtotestfrontend.com/resources/testing-async-react-rsc-components)

**原文标题**: [Testing async React RSC components | How To Test Frontend](https://howtotestfrontend.com/resources/testing-async-react-rsc-components)

本文探讨了在单元测试中测试 React Server Components (RSC) 的多种方法，重点介绍了由于组件异步行为带来的挑战，并提供了几种可行的测试策略。

- 🧪 **测试简单 RSC 组件**：对于没有嵌套异步组件或 Suspense 的简单 RSC 组件，可以使用`render(await Component())`的方式直接测试
- 🎭 **处理 Suspense 边界**：当组件包含 Suspense 时，简单的 await 方式无法渲染超出 fallback 的内容，需要更复杂的处理
- 🔧 **使用辅助渲染函数**：`renderServerComponent`辅助函数可以正确渲染 RSC 组件及其嵌套的异步子组件
- 📦 **特定 React 版本**：React 19.0.0-rc-380f5d67-20241113 这个特定版本能较好地支持 RSC 测试，但版本管理可能存在问题
- ⚡ **use() 与 act() 结合**：使用`use()`包装 promise，并结合`await act(() => render(...))`是目前较为推荐的测试方法
- 🌐 **端到端测试建议**：对于复杂的嵌套异步 RSC 组件，使用 Cypress 或 Playwright 进行 E2E 测试能获得更高的测试置信度
- 🔄 **组件重构建议**：新建项目建议使用`use()`而非 async/await，这样测试会更加简单直接

---

### [佩德罗·卡托里](https://pedrocattori.com/posts/just-javascript/)

**原文标题**: [Pedro Cattori](https://pedrocattori.com/posts/just-javascript/)

作者对"纯粹 JavaScript"的定义是代码无需自定义转换即可运行，强调程序行为的可预测性和开发技能的无缝迁移。虽然接受 TypeScript 和 JSX 这类普遍性转换，但反对通过构建工具改变运行时语义的非标准方式。

- 🔍 核心标准：代码无需自定义转换即可运行，确保程序行为可预测
- 🛠️ 开发体验：支持常规重构操作，移动代码时不应出现意外错误
- ✅ 例外情况：接受 TypeScript 和 JSX 这类普遍且明确的转换
- ⚠️ 框架评估：React Router 因特殊导出语义接近标准，Svelte 明确作为 DSL 存在，React 因指令和 Hook 规则偏离标准
- 🎯 实践典范：Remix 3 严格遵循运行时设计原则，构建工具仅作为优化层存在

---

### [工具提示组件不应存在 | TkDodo 的博客](https://tkdodo.eu/blog/tooltip-components-should-not-exist)

**原文标题**: [Tooltip Components Should Not Exist | TkDodo's blog](https://tkdodo.eu/blog/tooltip-components-should-not-exist)

作者认为工具提示组件不应作为独立组件存在，而应通过更高级别的模式组件来实现，以确保一致性和可访问性。

- 🚫 独立工具提示组件易被误用，导致键盘交互问题和非交互元素无法聚焦
- ⌨️ 键盘可访问性常被忽视，非交互元素上的工具提示无法通过键盘触发
- 🎯 用户体验不一致，可能出现无提示的图标按钮或隐藏关键信息的文本
- 🧩 建议采用模式组件：为交互组件提供可选 title 属性、图标按钮强制要求标题、提供预置的信息图标和文本组件
- 🔒 限制低层级工具提示组件能促进更好的 UX 设计和创造性解决方案

---

### [ChatGPT 成为我的编程导师：初级开发者如何学习 React 与 Next.js](https://techhub.iodigital.com/articles/chatgpt-as-my-coding-mentor)

**原文标题**: [ChatGPT as My Coding Mentor: How I Learned React and Next.js as a Junior Developer](https://techhub.iodigital.com/articles/chatgpt-as-my-coding-mentor)

一位初级开发者通过将 AI 转化为编程导师，学习使用"向 5 岁孩子解释"的提问方式，逐步掌握 React 和 Next.js 的开发技能。

- 🧠 使用"向 5 岁孩子解释"的提问方式突破学习障碍，如将 useState 比作"记忆盒子"
- 🗣️ 建立有效提问系统：设定背景、知识水平、期望结果，并请求类比和示例
- 📚 从 React 基础概念开始渐进学习，逐步过渡到 Next.js 的服务器组件与客户端组件
- 💡 通过针对性对话解决具体问题，比阅读文档更高效理解技术概念
- 🔍 避免泛泛提问，专注于单一概念并确保理解代码实现原理
- 📝 养成验证习惯，交叉核对 AI 提供的信息与官方文档
- 🎯 明确说明自身经验水平，请求分步讲解和原理说明
- 🤝 将 AI 视为对话伙伴而非搜索引擎，通过改进沟通获得更好帮助

---

### [豚骨拉面](https://www.tonkotsu.ai/?utm_source=reactdigest&utm_campaign=nov24)

**原文标题**: [Tonkotsu](https://www.tonkotsu.ai/?utm_source=reactdigest&utm_campaign=nov24)

文章概述了人工智能在现代社会中的广泛应用及其带来的影响。

- 🤖 人工智能技术正迅速渗透到各行各业，提升生产效率
- 💡 机器学习算法通过数据分析为决策提供支持，优化业务流程
- 🌐 自然语言处理技术改善了人机交互体验，使沟通更便捷
- ⚠️ 同时也引发了对就业结构变化和数据隐私保护的关注
- 🔮 未来需要建立完善的法律法规来规范人工智能的发展应用

---

### [深度优先 | Esbuild 中存活于 50 亿次下载并绕过 HTML 净化的 XSS 漏洞](https://www.depthfirst.com/post/esbuilds-xss-bug-that-survived-5-billion-downloads-and-bypassed-html-sanitization)

**原文标题**: [DepthFirst | Esbuild's XSS Bug that Survived 5 Billion Downloads and Bypassed HTML Sanitization](https://www.depthfirst.com/post/esbuilds-xss-bug-that-survived-5-billion-downloads-and-bypassed-html-sanitization)

Esbuild 开发服务器中存在一个 XSS 漏洞，该漏洞自 2022 年引入后已被下载 50 亿次。虽然 escapeForHTML 函数承诺对 HTML 进行转义，但未能转义双引号字符，导致攻击者可通过恶意文件夹名称注入脚本。该漏洞仅影响开发环境，维护者迅速合并了单行修复方案。

- 🔍 漏洞存在于 esbuild 开发服务器的目录列表功能中，escapeForHTML 函数未转义双引号字符
- 🚨 攻击者可通过包含双引号的文件夹名称突破 href 属性限制，注入全屏不可见 div 和 JavaScript 代码
- ⚙️ 漏洞利用方式：创建特殊命名的文件夹，当用户鼠标移动时触发任意 JavaScript 执行
- 🛠️ 修复方案仅需将 escapeForHTML 替换为具备引号转义功能的 escapeForAttribute 函数
- 📊 深度防御系统自动识别此低危漏洞并生成修复补丁，展示自动化安全检测的有效性
- 💡 该案例凸显上下文安全意识：即使单个函数正确，在错误上下文中使用仍会导致安全漏洞

---

### [JavaScript 中的错误链：利用 Error.cause 实现更清晰的调试 - Matt Smith](https://allthingssmitty.com/2025/11/10/error-chaining-in-javascript-cleaner-debugging-with-error-cause/)

**原文标题**: [
    Error chaining in JavaScript: cleaner debugging with Error.cause - Matt Smith
  ](https://allthingssmitty.com/2025/11/10/error-chaining-in-javascript-cleaner-debugging-with-error-cause/)

JavaScript 中的错误链式处理：通过 Error.cause 实现更清晰的调试

- 🎯 传统错误处理在多层代码中容易丢失原始错误信息和堆栈跟踪
- 🆕 ES2022 引入 Error.cause 属性，可保留原始错误上下文
- 🔧 使用方法：`throw new Error('消息', { cause: 原始错误 })`
- 📝 支持自定义错误类，可通过继承 Error 使用 cause 参数
- 🧪 在测试中可断言错误链，如 `expect(err.cause).toBeInstanceOf(ValidationError)`
- ⚠️ 控制台默认不显示 cause 链，需手动记录错误原因
- 🔄 提供递归记录完整错误链的辅助函数示例
- 🌐 所有现代环境均支持：Chrome 93+、Firefox 91+、Safari 15+、Node.js 16.9+
- 💡 TypeScript 需配置 `"target": "es2022"` 和 `"lib": ["es2022"]`
- 📚 适用于服务调用、数据库操作等分层系统的错误处理

---

### [范围语法现已应用于容器样式查询与 if() 函数 | CSS 技巧](https://css-tricks.com/the-range-syntax-has-come-to-container-style-queries-and-if/)

**原文标题**: [The Range Syntax Has Come to Container Style Queries and if() | CSS-Tricks](https://css-tricks.com/the-range-syntax-has-come-to-container-style-queries-and-if/)

CSS 容器样式查询和 if() 函数现已支持范围语法，允许开发者通过比较数值和自定义属性实现动态样式控制。

- 🔍 范围语法支持在容器样式查询中比较数值、自定义属性和 attr() 函数值
- ⚡ if() 函数内可直接使用范围语法进行条件样式声明
- 🎯 容器查询支持通过 container-name 创建特定作用域，if() 则自动查找当前规则
- 📊 演示案例展示如何根据--lightness 自定义属性动态切换文本颜色
- 🔢 使用 attr(data-notifs type<number>) 将属性值解析为数字进行比较
- 📏 支持比较不同单位但相同数据类型的值（如 1em 与 32px）
- 🎨 范围语法适用于<length>/<number>/<percentage>等 CSS 数据类型
- 🌐 该功能需 Chrome 142+ 支持，可与媒体查询等其他查询类型组合使用

---

### [我打赌你还不知道 Chrome 开发者工具的这六种用法，第一部分](https://www.readwriterachel.com/things-i-learned/2025/11/09/devtools-1.html)

**原文标题**: [Six Things I Bet You Didn't Know You Could Do With Chrome's Devtools, Part 1](https://www.readwriterachel.com/things-i-learned/2025/11/09/devtools-1.html)

本文介绍了 Chrome 开发者工具的三种隐藏功能，包括性能计时、DOM 监听和函数监控。

- ⏱️ 使用 console.time() 和 console.timeEnd() 精确测量代码执行时间
- 🔍 通过 DOM 断点功能监控元素变化并自动暂停代码执行
- 📡 使用 monitor() 方法监听第三方脚本的函数调用
- 🛠️ 这些功能可帮助开发者更高效地进行调试和性能优化
- 🌐 部分功能仅限 Chrome 浏览器使用，其他浏览器支持程度不同
- 📚 内容源自 TechBash 会议分享和官方文档

---

### [React 19.2：React 进入其巅峰时代 - DEV 社区](https://dev.to/sagi0312/react-192-react-in-its-sigma-era-op7)

**原文标题**: [React 19.2: React in its sigma era - DEV Community](https://dev.to/sagi0312/react-192-react-in-its-sigma-era-op7)

React 19.2 版本以幽默拟人化的方式介绍了其新特性和改进，强调框架在性能优化、开发体验和状态管理方面的提升，标志着进入更成熟高效的"sigma 时代"。

- 🎭 **Activity 组件** - 提供后台保留组件状态的能力，组件隐藏而非卸载，保持状态持久化
- 🧘‍♀️ **useEventEffect Hook** - 减少依赖项引发的重渲染问题，提供更稳定的副作用处理
- 🫠 **cacheSignal API** - 为服务器组件缓存提供中止信号，适用于边缘场景但日常使用频率较低
- 📊 **性能追踪工具** - 在 Chrome 开发者工具中直观显示渲染性能，帮助调试优化
- 🍱 **部分预渲染 (PPR)** - 支持静态外壳预渲染和动态内容流式传输，需要框架配合
- 🤝 **Suspense 边界批处理** - SSR 时同步渲染多个异步组件，改善加载体验
- 🔧 **工具链更新** - eslint-plugin-react-hooks v6 支持新特性，useID 前缀更新兼容 View Transitions API

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

一份为软件工程师精心筛选的每周通讯，帮助专业人士节省时间并持续学习新知识
- 📧 超过 23,394 名软件工程师订阅的每周邮件推送
- 🔍 每期包含带摘要的精选文章，节省寻找优质内容的时间
- 🎯 每周学习新知识，内容精准匹配工程师需求
- 💬 读者反馈证实其内容实用性强，能持续带来启发
- 🌍 被全球知名科技企业的软件工程师广泛阅读

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

每周为技术主管精心筛选的领导力提升资讯，帮助工程管理者通过精选内容高效成长

- 📧 汇聚 27,984+ 名工程领导者订阅的每周邮件推送
- 🎯 精选附摘要的优质文章，节省筛选时间
- 🌱 每周持续学习领导力建设与架构规划新知
- 💬 用户好评聚焦沟通技巧与授权管理等核心能力
- 🌍 受到全球科技企业领导者的广泛阅读认可

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

这是一份为.NET开发者精心策划的每周C#技术简报，帮助工程师高效获取优质内容。

- 📧 超过19,704名C#工程师订阅的每周邮件推送
- 🔍 精选文章配摘要，节省筛选内容时间
- 🎯 每周学习新技术，包含特性开关、LINQ 等实用主题
- 💡 实际应用案例：操作结果模式已成功应用于工作项目迁移
- 🌍 受到全球.NET 工程师认可，涵盖诊断监听器等进阶内容

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者和技术专业人士提供资讯服务的媒体公司，拥有超过 93,000 名订阅用户。

- 📧 每周发布简洁实用的技术简报，涵盖开发者、工程经理和 CTO 等专业群体
- 👥 服务超过 9.3 万名技术人员，帮助用户高效获取行业最新动态
- 💼 提供精准广告投放服务，连接软件工程师和 IT 决策者等专业受众
- 📞 支持业务咨询、广告合作与建议反馈等多种联系方式

---

### [过往简讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 是一份专注于 React 技术发展的电子报，涵盖版本更新、性能优化、状态管理和最佳实践等内容。

- 🚀 从 Enzyme 迁移至 React Testing Library，提升测试体验
- ⚡ React 19.2 引入自动优化和改进错误处理
- 🌐 利用 URL 进行状态管理，探索多语言应用优化
- 🔧 深入研究 JavaScript 指令和 React.createPortal 构建浮动 UI
- 🚄 React 服务端组件性能提升与 Rari SSR 突破
- 💾 序列化技术和 useContext 避免属性钻取
- 🔄 useSyncExternalStore 优化 Suspense 并发水合
- 🎭 解析 React 渲染行为与 useEffectEvent 新钩子
- 📊 2025 年状态管理前沿技术与 Elm 架构启示
- 🏆 React 主导地位对创新的影响与中间件实践
- 💡 TanStack DB 响应式客户端存储与 Next.js SEO
- 🛠️ 无框架实现 React 服务端组件支持
- ⏱️ 并发特性概览与表单提交修改新钩子
- ⚗️ 水合作用分析与本地存储与状态管理对比
- 🗂️ 缓存一致性重要性与 useCallback/useMemo 陷阱
- 👷 Web Workers 性能优化与 React 键的隐藏力量
- 📝 useCallback 最佳实践与钩子编写教程
- 🐻 Zustand 状态管理库深度解析
- 🧩 模块联邦与 React 并发 API 应用
- 📜 通过代码回顾 React 演进史与服务端组件测试

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策详细说明了 React Digest 如何收集、使用和保护用户的个人信息，重点阐述了数据收集原则、用户权利保障措施以及反垃圾邮件政策。

- 🔐 仅为实现指定目的收集个人信息，且须经用户同意或法律要求
- 📧 收集邮箱地址仅用于发送周刊，不作其他用途
- 🗑️ 用户可随时通过指定邮箱申请查询或删除个人数据
- ⏱️ 个人信息仅在实现目的必要期限内保留
- 🛡️ 采取合理安全措施防止数据丢失、盗用或未授权访问
- 👶 严格遵守儿童隐私保护法规，不收集 13 岁以下儿童信息
- 📮 提供明确退订渠道，坚决反对垃圾邮件行为
- 🌐 定期公开个人信息管理政策与实践

---

### [媒体资料包——Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为技术领域专业人士提供精准营销服务，通过四个专业电子报覆盖不同技术岗位受众，帮助广告主对接高质量目标群体并提升转化效果。

- 📧 科技领导力周报：面向工程经理/CTO 等决策者，2.7 万订阅者，开信率 58%，单期赞助$2,235
- 💻 编程文摘周报：针对全栈与后端开发者，2.1 万订阅者，点击率 14.8%，赞助单价$985
- 🔷 C#技术周报：专注.NET开发领域，2万订阅者，点击率21.6%，欧洲用户占比最高达48%
- ⚛️ React 前端周报：服务前端工程师，2.3 万订阅者，赞助价格$1,375，支持次级广告位
- 📊 广告优势：纯文本格式，用户参与度超行业标准 2 倍，覆盖谷歌/亚马逊等企业员工
- 🌍 受众分布：主要集中于欧美地区（合计占比 70%-80%），含各层级技术岗位
- 📋 合作流程：需提前预约档期，提供产品介绍→确定方案→支付锁定→内容优化→效果追踪
- 🤝 合作案例：已服务 Okta、MongoDB、GitLab 等知名技术企业，重复合作率高

---

