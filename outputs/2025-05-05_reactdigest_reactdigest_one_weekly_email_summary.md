### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份专为 React 开发者精心策划的周报，汇集优质内容，帮助开发者节省时间并持续学习。

- 📰 每周精选文章：为前端工程师提供经过筛选的高质量文章和简短摘要。  
- ⏳ 节省时间：免去自行搜寻有价值内容的繁琐过程。  
- 🎓 持续学习：每周更新，助你掌握 React 领域的新知识。  
- 👥 庞大社区：超过 24,190 名前端工程师订阅，共同成长。  
- 👍 读者好评：用户称赞内容实用、更新及时，尤其对 React 并发模式等深度文章表示认可。  
- 🌍 广泛认可：受到全球前端工程师的信任与阅读。  
- ©️ 品牌信息：由 Bonobo Press 发行，涵盖隐私政策及广告合作信息。

---

### [React 实验室：视图过渡、活动及其他 – React](https://react.dev/blog/2025/04/23/react-labs-view-transitions-activity-and-more)

**原文标题**: [React Labs: View Transitions, Activity, and more – React](https://react.dev/blog/2025/04/23/react-labs-view-transitions-activity-and-more)

React Labs 发布了关于新实验性功能 View Transitions 和 Activity 的更新，并分享了其他正在开发中的功能进展。

- 🚀 **React Conf 2025**：将于 10 月 7-8 日在内华达州亨德森举行，现招募演讲者。  
- 🧪 **新实验性功能**：  
  - **View Transitions**：通过 `<ViewTransition>` 组件实现 UI 过渡动画，支持导航、列表重排等场景。  
  - **Activity**：通过 `<Activity>` 组件隐藏/显示 UI 部分，保留状态并降低性能开销。  
- 🔧 **开发中的功能**：  
  - **React 性能追踪**：增强性能分析工具。  
  - **自动 Effect 依赖**：编译器自动插入依赖项，简化代码。  
  - **Fragment Refs**：支持多 DOM 元素引用管理。  
  - **手势动画**：扩展 View Transitions 以支持滑动等交互。  
  - **并发存储**：改进外部状态库的并发支持。  
- 📚 **文档与示例**：已发布 View Transitions 和 Activity 的详细使用指南，包含动画定制和状态恢复示例。  
- ⚙️ **IDE 扩展探索**：基于 React 编译器的实验性 IDE 插件，提供代码分析与优化建议。

---

### [Clerk 如何通过 Supabase 与 Next.js 应用集成](https://clerk.com/blog/how-clerk-integrates-nextjs-supabase?utm_source=react-digest&utm_medium=newsletter&utm_campaign=supabase-clerk&utm_content=04-21-25&dub_id=ch8bBw55ErNmsbCy)

**原文标题**: [How Clerk integrates with a Next.js application using Supabase](https://clerk.com/blog/how-clerk-integrates-nextjs-supabase?utm_source=react-digest&utm_medium=newsletter&utm_campaign=supabase-clerk&utm_content=04-21-25&dub_id=ch8bBw55ErNmsbCy)

概述  
本文介绍了如何在 Next.js 应用中集成 Supabase 和 Clerk，以提升安全性和开发效率。Supabase 允许直接通过客户端访问数据库，而无需传统后端，同时通过 Postgres 的行级安全（RLS）保护数据。Clerk 作为身份验证提供者，通过 JWT 与 Supabase 集成，确保请求的安全性和用户身份验证。文章还通过实际项目 Quillmate 的代码示例展示了具体实现方法。

- 🚀 **Supabase 与 Next.js 的集成**：Supabase 允许客户端直接通过 API 访问数据库，结合 Next.js 的全栈能力，简化开发流程。  
- 🔒 **行级安全（RLS）**：Supabase 利用 Postgres 的 RLS 功能，通过策略控制用户对数据的访问权限，确保数据安全。  
- 🔑 **Clerk 的身份验证**：Clerk 生成短期有效的 JWT，用于 Supabase 请求的身份验证，通过 JWKS 端点验证令牌。  
- ⚙️ **JWT 配置**：在 Supabase 中，JWT 需包含`role: authenticated`声明，以确保请求具有正确的安全级别。  
- 🔄 **代码示例**：通过 Quillmate 项目的代码展示了如何在 Next.js 中配置 Supabase 客户端，并使用 Clerk 的`getToken`函数传递 JWT。  
- 📜 **RLS 策略示例**：通过`auth.jwt()->>'sub'`提取用户 ID，并在 RLS 策略中限制用户只能访问自己的数据。  
- 🛠️ **实际应用**：Quillmate 项目展示了如何在实际应用中实现 Clerk 和 Supabase 的集成，包括配置和代码实现。  
- 📌 **总结**：Supabase 和 Clerk 的集成挑战了传统架构，但通过 RLS 和 JWT 验证，既能节省开发时间，又能增强数据安全性。

---

### [React 中的父组件与所有者：Context Providers | JulesBlom.com](https://julesblom.com/writing/parent-owners-context)

**原文标题**: [Parents & Owners in React: Context Providers | JulesBlom.com](https://julesblom.com/writing/parent-owners-context)

文章讨论了 React 中父组件和所有者组件的区别，以及如何通过自定义上下文提供者优化性能。

- 📌 文章强调了父组件树和所有者组件树的区别，这对于理解组件更新机制至关重要。
- 🔄 组件重新渲染的三个原因：自身更新、上下文更新和所有者更新。
- ⚡ 使用自定义上下文提供者（如`CounterProvider`）可以避免不必要的重新渲染，提高性能。
- 🧩 通过插槽组件（使用`children`）分离变化和不变化的部分，优化更新单元。
- 🚀 理解父组件和所有者组件的区别有助于编写更高效、更清晰的 React 应用。
- 📚 推荐阅读 Josh Comeau 和 Brad Westfall 的相关文章，深入了解渲染机制和服务器组件中的应用。

---

### [React 内部机制：哪个 useEffect 会先运行？ – Frontend Masters 博客](https://frontendmasters.com/blog/react-internals-which-useeffect-runs-first/)

**原文标题**: [React Internals: Which useEffect runs first? – Frontend Masters Blog](https://frontendmasters.com/blog/react-internals-which-useeffect-runs-first/)

文章探讨了 React 中`useEffect`的执行顺序问题，通过示例代码和 React 内部机制解析了子组件和父组件的`useEffect`执行顺序。

- 🔍 `useEffect`是 React 中最常用的 Hook 之一，但其执行顺序在多层级组件中可能出人意料。
- 🧩 示例代码展示了子组件的`useEffect`会在父组件之前执行，这与渲染顺序相反。
- 🌳 React 内部使用 Fiber 树结构来管理组件层次和更新，每个节点包含子节点、兄弟节点和父节点信息。
- 🔄 React 的生命周期分为三个阶段：触发 → 渲染 → 提交，其中`useEffect`在提交阶段执行。
- 📊 Fiber 树的遍历采用深度优先算法，每个节点会被访问两次，分别用于开始工作和完成工作。
- ⚡ 提交阶段中，React 会再次遍历 Fiber 树来执行`useEffect`，子组件的`useEffect`会先于父组件执行。
- 🤔 文章通过第二个示例进一步验证了这种执行顺序，并解答了读者的疑问。
- 📚 推荐通过 Frontend Masters 的课程深入学习 React 内部机制。

---

### [你可以在 React 中序列化一个 promise](https://twofoldframework.com/blog/you-can-serialize-a-promise-in-react)

**原文标题**: [You can serialize a promise in React](https://twofoldframework.com/blog/you-can-serialize-a-promise-in-react)

React Server Components 中实现 Promise 的序列化传输，通过流式数据在服务端与客户端之间共享异步状态。

- 🚀 **服务端创建 Promise**：在服务端组件中创建 Promise，并通过 `<Suspense>` 和客户端组件传递，实现异步值的跨网络传输。
- 🔄 **序列化限制**：JSON 无法序列化 Promise（输出 `{}`），需自定义流式序列化格式标记 Promise 生命周期（如 `promise:create` 和 `promise:resolve:`）。
- 🌐 **流式传输**：利用 `ReadableStream` 和 `Response` 实现 Promise 状态的网络共享，类似 `fetch` 的流式响应机制。
- ⚙️ **反序列化逻辑**：客户端通过解析流中的标记消息重建 Promise，并确保读取时处理未完成/已解决状态。
- ⚛️ **React 内置支持**：React 19 的 `react-server` 和 `react-client` 包底层使用流式序列化（如 `renderToReadableStream` 和 `createFromReadableStream`），支持 20+ 数据类型（包括非原始类型和 React 元素）。
- 🧩 **开发透明性**：框架层自动调用序列化 API，开发者只需编写常规组件逻辑即可实现服务端到客户端的数据流动。
- 🔗 **扩展阅读**：作者邀请通过 Twitter/Bluesky 进一步讨论 RSC 技术细节。

---

### ["use client" 有什么用？——过度反应](https://overreacted.io/what-does-use-client-do/)

**原文标题**: [What Does "use client" Do? — overreacted](https://overreacted.io/what-does-use-client-do/)

React Server Components 中的 `'use client'` 和 `'use server'` 指令通过模块系统抽象了客户端与服务器的交互，使跨环境编程更直观和类型安全。

- 🚪 `'use server'`：标记服务器端函数，允许客户端通过异步调用直接触发 HTTP 请求，替代手动 `fetch` 调用，实现类型安全的 RPC。
- 💻 `'use client'`：标记客户端组件，允许服务器端通过引用生成 `<script>` 标签并传递初始数据，实现声明式渲染与状态同步。
- 🔗 **模块化网络边界**：两个指令将网络通信嵌入模块系统，支持类型检查、引用查找和跨环境组合，使前后端成为“单程序”。
- 🌐 **双向通信模型**：`'use server'` 为客户端开“门”调用服务端逻辑；`'use client'` 为服务端开“门”注入客户端代码，形成闭环。
- 🔄 **超越 React**：本质是模块级的 RPC 与代码分发范式，可能影响未来全栈框架设计。

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=react_digest)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=react_digest)

Meticulous AI 提供了一种无需编写和维护测试的自动化测试解决方案，通过记录用户交互并生成持续演化的测试套件，覆盖所有代码分支和边缘情况，帮助团队快速迭代并确保代码质量。

- 🚀 **无需编写测试** - Meticulous AI 通过记录用户交互自动生成测试，无需手动编写或维护测试用例。  
- 🔍 **全面覆盖** - 监控代码分支和用户流程，确保覆盖所有边缘情况和功能。  
- ⚡ **快速反馈** - 在合并代码前查看改动对用户流程的影响，避免回归问题。  
- 🛠️ **无缝集成** - 支持与现有测试套件结合使用或完全替代，轻松集成到开发流程中。  
- ⏱️ **高效执行** - 测试高度并行化，可在 120 秒内完成数千次测试。  
- 🏆 **用户认可** - 被 Dropbox、WithPower、Lattice 等 100 多家组织信任，显著提升开发效率和代码质量。  
- 📦 **多框架支持** - 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流前端框架。  
- 🔒 **安全可靠** - 从底层消除测试波动，确保测试结果稳定可信。

---

### [使用行高单位优化你的排版 | WebKit](https://webkit.org/blog/16831/line-height-units/)

**原文标题**: [  Polishing your typography with line height units | WebKit](https://webkit.org/blog/16831/line-height-units/)

网页排版中行高单位（lh）的应用与优势  

- 🎨 **CSS 新工具**：近年来 CSS 新增了许多简化设计细节的工具，如 lh 和 rlh 单位，使排版更精细且易于实现。  
- 📏 **行高单位介绍**：lh 代表当前字体行高（1lh=一行文字高度），rlh 则类似 rem，指向根元素行高。  
- ✨ **实用场景**：用`margin-block: 1lh`设置段落间距，比传统`1em`更协调，视觉上更精致（对比示例图可见差异）。  
- 🔍 **视觉对比**：通过网格线辅助观察，lh 单位能精准对齐文本垂直节奏，提升整体排版韵律感。  
- 🛠️ **广泛应用**：除边距外，lh 还可用于内边距、间隙、宽高等任何布局尺寸的设定。  
- 🌐 **浏览器支持**：94% 以上浏览器已兼容 lh 单位，可通过渐进增强（如`padding: 1em; padding: 1lh;`）兼容旧版本。  
- 💡 **设计趋势**：结合近年其他排版新特性，开发者能更轻松实现专业级网页 Typography 效果。  
- 💬 **反馈邀请**：作者鼓励在 Bluesky 或 Mastodon 平台分享使用体验与疑问。

---

### [《用 JavaScript 实现时间旅行 - Jhey ʕ•ᴥ•ʔ 著》](https://craftofui.substack.com/p/time-travel-with-javascript)

**原文标题**: [Time Travel with JavaScript - by Jhey ʕ•ᴥ•ʔ](https://craftofui.substack.com/p/time-travel-with-javascript)

这篇文章介绍了如何使用 JavaScript 和动画技巧创建一个类似 Vestaboard 的 3D 翻页显示效果。

- 🎨 使用 clip-path 和 CSS 动画创建单个翻页元素的结构和样式  
- 🔄 通过 GSAP 实现时间轴动画控制，模拟翻页效果  
- ⏱️ 利用时间轴 scrubbing 技术实现字符间的平滑过渡  
- 📜 支持自定义字符序列循环显示，包括字母和 emoji  
- 🧩 可扩展为多模块组合的完整显示板  
- ⚙️ 提供了 GSAP 和 WAAPI 两种实现方案对比  
- 🛠️ 演示了如何通过类封装创建可复用的翻页组件  
- 📚 作者预告将推出相关 UI 设计课程  

文章包含详细的代码示例和实现思路，展示了前端动画开发的创造性技巧。

---

### [异步代码解密：Promise、Fetch 与 useEffect](https://blog.codeminer42.com/async-code-demystified-promises-fetch-and-reacts-useeffect/)

**原文标题**: [Async Code Demystified: Promises, Fetch, and useEffect](https://blog.codeminer42.com/async-code-demystified-promises-fetch-and-reacts-useeffect/)

文章概述了异步编程的核心概念，包括同步与异步的区别、回调地狱问题、Promise 的使用、Async/Await 语法、Fetch API 以及 React 中的 useEffect 钩子。通过制作咖啡的比喻，生动地解释了这些技术如何优化代码结构和提高效率。

- ☕ 同步代码按顺序逐行执行，会阻塞后续操作；异步代码允许多任务并行，不阻塞其他操作。
- ⏳ 回调地狱指过度嵌套回调函数导致的代码难以维护，形成“末日金字塔”。
- 🤝 Promise 通过三种状态（Pending、Fulfilled、Rejected）管理异步操作，支持链式调用.then() 和.catch() 避免嵌套。
- 🔗 Promise.all() 可并行执行多个异步任务，提升效率。
- ⏱️ Async/Await用同步写法处理异步操作，await会暂停执行直到Promise解决。
- 🌐 Fetch API 基于 Promise，用于 HTTP 请求，结合 Async/Await 可简化数据获取流程。
- ⚛️ React 的 useEffect 钩子管理副作用（如数据获取），依赖数组控制执行时机，避免不必要的重渲染。
- 🚀 异步编程是现代 Web 开发的核心，能提升应用性能和用户体验。

---

### [不可能实现的组件——过度反应](https://overreacted.io/impossible-components/)

**原文标题**: [Impossible Components — overreacted](https://overreacted.io/impossible-components/)

React 组件的前后端分离与组合模式探索，通过“不可能组件”案例展示如何将数据加载与交互逻辑解耦，实现自包含的跨栈抽象。

- 🌈 **数据与交互分离**：前端组件处理用户交互状态（如输入框），后端组件加载本地数据（如文件读取），两者无法直接混合。
- 🔄 **组件拆分方案**：将组件拆分为 `GreetingBackend`（数据加载）和 `GreetingFrontend`（交互逻辑），通过 props 传递数据。
- 📦 **自包含抽象**：组合后的 `<GreetingBackend/>` 封装了跨栈逻辑，用户只需调用单一组件。
- 🧩 **独立性与复用**：多个实例可独立管理状态（如不同颜色文件），后端数据加载与前端状态互不干扰。
- 🌐 **动态交互示例**：点击卡片展开内容时，后端传递的 `extraContent` 直接用于前端事件处理，无额外请求。
- 📚 **复杂场景实践**：可排序/过滤的博客列表组件，复用 `SortableList` 并嵌套 `PostPreview`，展示前后端逻辑的深度组合。
- 🚀 **模式优势**：单次往返数据加载、局部状态管理、无全局冲突，符合用户心智模型（如 `<PostPreview slug="...">`）。
- 🔮 **未来方向**：支持动态路由参数、动画刷新、服务端动作等扩展，强调“跨栈组合”优于传统前后端分层思维。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《Programming Digest》是一份专为软件工程师精心挑选的每周通讯，旨在为订阅者提供高质量的技术文章和资源。  

- 📧 **订阅人数**：超过 18,334 名软件工程师每周接收这份邮件。  
- 📖 **内容精选**：每期包含人工筛选的文章，并附有简短摘要，节省读者寻找优质内容的时间。  
- 🎯 **学习价值**：每周都能学到新知识，涵盖 API 设计等技术话题。  
- 👍 **读者反馈**：用户称赞其内容实用，如“每期都能学到东西”“感谢推荐优质文章”。  
- 🌍 **受众范围**：受到全球软件工程师的阅读和认可。  
- ©️ **版权信息**：由 Bonobo Press 发行（2013-2025），提供其他通讯、隐私和广告相关选项。

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

《Leadership in Tech》是一份为技术领导者精心打造的每周通讯，旨在帮助 CTO、工程经理和高级工程师提升领导力。

- 📰 每周精选文章：为 26,128+ 工程领导者提供精选内容与简短摘要  
- ⏱️ 节省时间：直接呈现有价值的内容，免去自行筛选的麻烦  
- 🌱 持续学习：每周更新，确保读者获得新知识  
- ❤️ 读者好评：用户称赞其领导力建设文章（如架构讨论、会议沟通、任务委派等）的独特性和实用性  
- 🌍 广泛认可：受到全球科技领域领导者的阅读与信赖  
- ©️ 由 Bonobo Press 出品（2013-2025），涵盖多类通讯，注重隐私与广告透明度

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份为.NET 开发者精心策划的每周通讯，提供精选文章和简短摘要，帮助开发者节省时间并每周学习新知识。

- 📧 超过19,702名C#工程师订阅这份每周电子邮件
- 📖 提供精选文章和简短摘要，节省寻找有价值内容的时间
- 🌱 每周学习新知识，保持技术更新
- 💼 读者反馈在实际工作中应用了通讯中的内容
- 🔍 介绍了标准功能标志、LINQ 和 DiagnosticListener 等实用技术
- 👍 特别推荐了"操作结果模式"文章，甚至促使读者迁移 Azure Function
- 🌍 被全球.NET 工程师阅读
- © 2013-2025 Bonobo Press 版权所有

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家专注于为软件开发者和技术专业人士提供新闻资讯的出版商，自 2013 年以来服务超过 89,000 名读者，提供简洁高效的每日和每周通讯。

- 📧 提供面向开发者、工程经理、技术主管和 CTO 的精选通讯，内容简洁省时  
- 🎯 广告服务可精准触达软件工程师、团队领导、工程经理及 IT 决策者等目标受众  
- 📩 欢迎订阅其出版物或通过媒体资料包了解广告合作详情  
- 📞 如有疑问、建议或广告需求，可通过网站联系他们

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 是一份涵盖 React 生态系统最新动态和技术的新闻简报，内容涉及 React 新特性、性能优化、架构设计、状态管理、服务器端渲染等多个方面。

- 🌟 2025 年 5 月 4 日：探讨 React 的新 View Transitions 和 Activity 组件，优化 UI 动画和上下文提供者。
- 🧩 2025 年 4 月 27 日：Dan Abramov 分享“不可能组件”，React Query 简化状态管理，React 编译器优化生产环境。
- 🔗 2025 年 4 月 20 日：深入服务器端渲染，解决状态管理挑战，构建全栈 AI 聊天应用。
- 🛠️ 2025 年 4 月 13 日：高级 React 技术，包括 React Query 机制和协调算法，动态表单挑战。
- ⚖️ 2025 年 4 月 6 日：React 架构权衡，Zustand 和 Immer 最佳实践，无库表单创建方法。
- 🔐 2025 年 3 月 30 日：Next.js 授权机制，View Transition API，React 内部工作原理。
- 📡 2025 年 3 月 23 日：服务器端渲染深入探讨，React 库架构，TanStack 实时数据更新。
- 🚀 2025 年 3 月 16 日：Next.js 性能优化，React 通知实现，替代 React.memo 的方案。
- ⚡ 2025 年 3 月 9 日：React 中使用信号的挑战，状态管理工具比较，布局效果和状态转换。
- 🔄 2025 年 3 月 2 日：React 中的函数式编程，React 19 缓存 API 优化数据获取，迁移到 Vite。
- 🏗️ 2025 年 2 月 23 日：Create React App 弃用，转向现代框架，自定义钩子和设计技巧。
- ✍️ 2025 年 2 月 16 日：用 React 重建 ProseMirror 渲染器，升级类组件，React Router 内部机制。
- 🧠 2025 年 2 月 9 日：常见 React 设计模式，动态样式表加载，单一职责原则。
- 💡 2025 年 2 月 2 日：React Server Components 优势，Next.js 14 的优缺点，可扩展组件和 WebSockets。
- ⏱️ 2025 年 1 月 26 日：React 初始加载性能，View Transitions API，服务器函数进展。
- 🛒 2025 年 1 月 20 日：Shopify 五年 React Native 经验，React Router 路由分割，无障碍开发。
- ⚠️ 2025 年 1 月 12 日：避免自定义钩子问题，React 渲染周期，Next.js 缓存改进。
- 🎯 2025 年 1 月 5 日：实例钩子模式，React Router 见解，提升 React 技能。
- 🎄 2024 年 12 月 22 日：React 19 特性，表单优化，开发中常见陷阱。
- 🏙️ 2024 年 12 月 15 日：现代前端架构，SSR 误区，3D 地形渲染器，2025 推荐技术栈。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

React Digest 的隐私政策概述，强调保护用户隐私的重要性，并详细说明了信息收集、使用和保护的原则。

- 🔒 隐私至关重要，因此制定了明确的政策来说明如何收集、使用和披露个人信息。  
- 🎯 在收集个人信息前会明确目的，并仅用于指定或兼容的目的，除非获得同意或法律要求。  
- ⏳ 仅在必要时保留个人信息，以完成既定目的。  
- 📜 通过合法和公正的手段收集信息，并在适当情况下获得用户知情或同意。  
- ✔️ 确保个人数据与使用目的相关，并尽可能准确、完整和最新。  
- 🛡️ 采取合理的安全措施保护个人信息，防止丢失、盗窃或未经授权的访问。  
- 📢 向用户公开关于个人信息管理的政策和实践。  
- ✉️ 仅收集电子邮件地址用于发送每周通讯，不用于其他目的。  
- � 严格遵守 COPPA，不收集或存储 13 岁以下儿童的信息。  
- 📧 用户可根据《数据保护法》要求获取或删除存储的个人信息，联系邮箱：[email protected]。  
- 🚫 坚决反对垃圾邮件，用户可随时通过邮件中的链接退订。  
- ©️ 版权归 Bonobo Press 所有，涵盖 2013 至 2025 年。

---

### [媒体资料包——Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 是一家专注于为程序员和技术人员提供最新趋势、工具和技术更新的媒体平台，通过每日和每周的新闻简报服务于软件开发人员、工程经理、CTO 等技术人员。其广告合作伙伴涵盖软件工具、招聘、会议等多个领域，致力于帮助广告商精准触达目标受众并提升转化率。

- 🎯 **受众定位**：主要订阅用户位于美国和欧洲，以软件开发者为主，同时包含大量工程经理、技术副总裁及 CTO 等决策者。  
- ✉️ **高互动简报**：简报互动率远超行业平均水平，定期清理不活跃用户以确保高质量读者群。  
- 📊 **简报数据**：  
  - **Leadership in Tech**：24,616 订阅，58.95% 打开率，$1,620/期  
  - **Programming Digest**：15,535 订阅，52.39% 打开率，$760/期  
  - **C# Digest**：21,467 订阅，51.82% 打开率，$1,080/期  
  - **React Digest**：27,849 订阅，46.35% 打开率，$1,320/期  
- 📝 **广告格式**：纯文本内嵌广告，需包含链接、标题（<100 字符）和描述（<400 字符），提交截止时间为发布前 4 天。  
- 🤝 **合作流程**：提前数周预约广告位 → 确认日期与发票 → 支付后锁定档期 → 内容优化 → 广告发布。  
- 🌟 **知名合作伙伴**：Okta、GitLab、MongoDB、Twilio 等，多数广告商会重复预订。  
- 📩 **联系方式**：通过官网提交需求，团队将提供定制化受众建议与档期支持。

---

