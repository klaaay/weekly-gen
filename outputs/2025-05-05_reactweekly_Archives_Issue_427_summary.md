### [React 状态周报第 427 期：2025 年 4 月 30 日](https://react.statuscode.com/issues/427)

**原文标题**: [React Status Issue 427: April 30, 2025](https://react.statuscode.com/issues/427)

React Labs 发布重大更新，包含新功能 View Transitions 和 <Activity> 组件，其他多项功能正在开发中。Dan Abramov 探讨了 React Server Components 中 use client 和 use server 指令的实用意义。此外，还有多个工具和库的更新发布，包括 Storybook 9 Beta 和 react-native-ai 等。  

- 🚀 **React Labs 重大更新**：发布 View Transitions 和 <Activity> 组件，其他功能开发中。  
- 📺 **视频解析**：Theo Browne 发布 40 分钟视频解析 React Labs 更新内容。  
- 📚 **新课程**：Frontend Masters 推出 Next.js Fundamentals v4 课程，涵盖 React Server Components 等。  
- 💡 **use client 指令解析**：Dan Abramov 探讨 use client 和 use server 指令的实用意义。  
- 🎮 **React Jam 游戏开发活动**：第六届活动即将开始，10 天内用 React 开发游戏。  
- 🛠 **工具更新**：Storybook 9 Beta 发布，支持组件测试；react-native-ai 支持本地运行 LLM。  
- 🌐 **Reactylon 框架**：基于 Babylon.js 和 React，用于构建 Web XR 体验。  
- 📦 **其他库更新**：React Modal Sheet 4.0、Gridstack.js 12.1、next-intl 4.1 等发布。  
- ⚡ **JavaScript 生态动态**：V8 新功能 Explicit Compile Hints、SolidJS 十年回顾、Bun 支持 LLM 文档等。  
- ⏰ **Node.js v18 终止支持**：v24 即将发布。

---

### [React 实验室：视图过渡、活动及其他 – React](https://react.dev/blog/2025/04/23/react-labs-view-transitions-activity-and-more)

**原文标题**: [React Labs: View Transitions, Activity, and more – React](https://react.dev/blog/2025/04/23/react-labs-view-transitions-activity-and-more)

React Labs 发布了两个新的实验性功能：视图过渡（View Transitions）和活动（Activity），并分享了其他正在开发中的功能更新。

- 🚀 **React Conf 2025**：将于 10 月 7 日至 8 日在内华达州亨德森举行，现招募演讲者。
- 🔍 **实验性功能**：
  - **视图过渡（View Transitions）**：通过 `<ViewTransition>` 组件实现 UI 过渡动画，支持导航、列表重排等场景。
  - **活动（Activity）**：通过 `<Activity>` 组件隐藏或显示部分 UI，保留状态并降低性能消耗。
- 📚 **文档发布**：新功能的文档已上线，鼓励开发者测试并提供反馈。
- ⚙️ **开发中的功能**：
  - **React 性能追踪**：为性能分析工具添加自定义追踪功能。
  - **编译器 IDE 扩展**：利用 React 编译器提供代码优化建议和调试信息。
  - **自动 Effect 依赖**：编译器自动插入 Effect 依赖，简化代码编写。
  - **Fragment Refs**：支持对多个 DOM 元素进行引用管理。
  - **手势动画**：增强视图过渡以支持手势操作（如滑动菜单）。
  - **并发存储**：通过 `use` API 支持并发外部存储。
- 🛠 **优化与改进**：
  - 视图过渡支持自定义动画和共享元素过渡。
  - 活动组件支持预渲染和状态恢复，提升用户体验。
- 📅 **未来计划**：继续研究手势动画和并发存储等高级功能，逐步完善 API 设计。

---

### [React 实验室：视图过渡、活动及其他 – React](https://react.dev/blog/2025/04/23/react-labs-view-transitions-activity-and-more#features-in-development)

**原文标题**: [React Labs: View Transitions, Activity, and more – React](https://react.dev/blog/2025/04/23/react-labs-view-transitions-activity-and-more#features-in-development)

React Labs 发布了两个新的实验性功能：View Transitions 和 Activity，并分享了其他正在开发中的功能更新。

- 🚀 **React Conf 2025**：将于 10 月 7 日至 8 日在内华达州亨德森举行，现招募演讲者。
- 🔍 **新实验性功能**：
  - **View Transitions**：通过 `<ViewTransition>` 组件实现 UI 过渡动画，支持导航、列表重排等场景。
  - **Activity**：通过 `<Activity>` 组件隐藏或显示部分 UI，保留状态并降低性能开销。
- 🛠 **开发中的功能**：
  - **React Performance Tracks**：性能分析工具，提供更详细的 React 应用性能数据。
  - **Compiler IDE Extension**：基于 React 编译器的 IDE 扩展，提供代码优化建议和调试信息。
  - **Automatic Effect Dependencies**：编译器自动插入 Effect 依赖，简化代码编写。
  - **Fragment Refs**：支持片段引用，简化多 DOM 元素管理。
  - **Gesture Animations**：增强 View Transitions 以支持手势动画。
  - **Concurrent Stores**：支持并发外部存储，优化状态管理。
- 📚 **文档与示例**：提供了详细的文档和示例代码，帮助开发者快速上手新功能。
- 🔧 **注意事项**：
  - View Transitions 不替代所有动画，适用于特定 UI 过渡场景。
  - Activity 隐藏时 Effects 会卸载，需注意副作用处理。
  - 实验性功能 API 可能变动，建议通过升级到最新实验版本尝试。

---

### [React 现在酷多了 - YouTube](https://www.youtube.com/watch?v=-dePNpdd44M)

**原文标题**: [React just got WAY cooler - YouTube](https://www.youtube.com/watch?v=-dePNpdd44M)

这是一个关于 YouTube 网站相关信息和政策的页面，列出了多个重要链接和声明。

- ℹ️ 关于：提供 YouTube 的基本信息和背景。  
- 📰 媒体：与新闻和媒体相关的资源。  
- ©️ 版权：涉及版权政策和相关内容。  
- 📞 联系我们：提供与 YouTube 联系的途径。  
- 🎨 创作者：为内容创作者提供的资源和支持。  
- 📢 广告：广告相关信息和合作机会。  
- 💻 开发者：面向开发者的工具和资源。  
- 📜 条款：YouTube 的使用条款和条件。  
- 🔒 隐私：隐私政策和数据保护措施。  
- ⚖️ 政策与安全：平台政策和安全指南。  
- 🔧 YouTube 工作原理：介绍 YouTube 的运作机制。  
- 🧪 测试新功能：新功能的测试和体验。  
- ©️ 2025 Google LLC：版权声明，归属 Google 公司。

---

### [在 Next.js 中使用视图过渡 | Jack Whiting](https://jackwhiting.co.uk/posts/using-view-transitions-in-next-js)

**原文标题**: [Using View Transitions in Next.js | Jack Whiting](https://jackwhiting.co.uk/posts/using-view-transitions-in-next-js)

概述：本文介绍了如何在 Next.js 中使用 View Transitions API 来实现页面过渡动画，包括启用实验性功能、代码结构设置以及通过 CSS 自定义动画效果。

- 🚀 **启用 Next.js 中的过渡功能**：需要在 Next.js 配置文件中启用实验性的 View Transitions 标志。
- � **代码结构设置**：展示了如何在布局、主页、卡片组件和单篇文章页面中设置 View Transitions，确保动态元素有唯一的`view-transition-name`。
- 🎨 **CSS 自定义动画**：通过 CSS 可以针对单个元素或一类元素设置过渡动画，利用`view-transition-class`简化代码。
- 🔗 **动态过渡名称**：使用文章 ID 动态生成`view-transition-name`，确保大量元素也能正确过渡。
- 📌 **保持简洁**：通过 CSS 的`view-transition-group`属性批量处理同类元素的动画，减少重复代码。

---

### ["use client" 有什么用？——过度解读](https://overreacted.io/what-does-use-client-do/)

**原文标题**: [What Does "use client" Do? — overreacted](https://overreacted.io/what-does-use-client-do/)

React Server Components 中的 `'use client'` 和 `'use server'` 指令通过模块系统抽象了客户端与服务器的交互，使开发者能够将跨环境的应用视为单一程序。

- 🚪 `'use server'`：标记服务器端函数，允许客户端通过异步调用直接触发 HTTP 请求，替代传统 `fetch` 的字符串化操作。  
- 🔄 `'use client'`：标记客户端组件，使服务器能通过引用生成 `<script>` 标签并传递初始数据，实现无缝渲染。  
- 🌐 **双向通信**：两个指令分别在模块系统中建立客户端与服务器的语法连接，支持类型检查和工具链集成。  
- 🧩 **组合抽象**：允许创建跨网络的复用逻辑，如封装前后端交互的独立组件，无需全局 API 设计。  
- ⚡ **性能优化**：支持服务端预渲染 HTML，同时保留客户端交互性，平衡加载速度与用户体验。  
- 🔮 **超越 React**：本质是模块级的 RPC 实现，可能影响未来 JavaScript 全栈开发范式。  

核心思想是将分布式应用建模为「单程序多环境」，通过语法糖弥合网络鸿沟。

---

### [React 果酱](https://reactjam.com/)

**原文标题**: [React Jam](https://reactjam.com/)

React Jam 是一个面向全球 React 开发者的在线活动，参与者需在 10 天内用 React 开发游戏，主题将于 2025 年 5 月 16 日公布，活动持续至 5 月 26 日。活动鼓励团队合作，提供多个奖项，并设有专门的多人游戏挑战。

- 🎮 **活动概述**：React Jam 是一个为期 10 天的在线游戏开发活动，开发者使用 React 构建游戏，主题在活动开始时公布。
- 🌍 **参与范围**：全球在线参与，时间为 2025 年 5 月 16 日至 26 日。
- 💡 **活动目的**：展示技能、实验创意、学习 React 社区经验，无论经验水平如何均可参与。
- 🏆 **奖项设置**：包括最佳游戏奖（基于趣味性、主题契合度和呈现效果）和多人游戏挑战奖（基于游戏时长）。
- 🕹️ **多人游戏挑战**：使用 React 和 Rune SDK 开发多人游戏，有机会赢得额外奖金。
- 👥 **团队合作**：允许个人或团队参与，甚至可以提交多个游戏。
- ⏳ **时间灵活**：可以在 10 天内的任何时间提交游戏，但必须在截止日期前完成。
- 📅 **重要日期**：主题公布（5 月 16 日），提交截止（5 月 26 日），获奖公布（6 月 10 日）。
- 📢 **宣传与赞助**：鼓励通过社交媒体宣传，企业可联系组织方赞助。
- 📜 **规则与资源**：提供详细的规则、FAQ 和资源链接，包括艺术、音频和工具推荐。

---

### [行为](https://bhvr.dev/)

**原文标题**: [bhvr](https://bhvr.dev/)

现代轻量级开放网络技术栈  

- 🚀 **Bun + Hono + Vite + React**：一套现代、轻量级的开发技术组合  
- 🌐 **开放网络**：专为现代 Web 应用设计，支持高效开发  
- ⚡ **快速启动**：使用命令 `bun create bhvr@latest` 即可快速创建项目  
- 🛠️ **工具整合**：结合 Bun 的快速运行时、Hono 的轻量级服务、Vite 的构建工具和 React 的 UI 框架

---

### [Hono - 基于 Web 标准的 Web 框架](https://hono.dev/)

**原文标题**: [Hono - Web framework built on Web Standards](https://hono.dev/)

超快速且轻量级的路由解决方案，性能卓越且体积小巧。

- 🚀 RegExpRouter 速度极快  
- 📦 hono/tiny 预设大小不足 14kB  
- 🌐 仅使用 Web 标准 API

---

### [Vite | 新一代前端构建工具](https://vite.dev/)

**原文标题**: [Vite | Next Generation Frontend Tooling](https://vite.dev/)

Vite 是一个现代化的前端构建工具，提供快速、高效的开发体验。

- 🔍 **搜索功能**：支持快速查找文档内容。
- 📖 **导航菜单**：包括指南、配置、插件、资源等主要部分。
- 🛠️ **工具与资源**：提供团队信息、博客、版本发布等资源。
- 🌐 **社区与支持**：链接到 Bluesky、Mastodon、X、Discord 等社区平台。
- 📚 **文档版本**：支持 Vite 5 及以下版本的文档查阅。
- 🌍 **多语言支持**：提供包括简体中文、英文、日语等在内的多语言选项。
- 🎨 **外观设置**：支持用户自定义界面外观。

---

### [React 与 Next.js 的完美光标 AI 设置](https://www.builder.io/blog/cursor-ai-tips-react-nextjs)

**原文标题**: [The Perfect Cursor AI setup for React and Next.js](https://www.builder.io/blog/cursor-ai-tips-react-nextjs)

AI 革命在软件开发中是一把双刃剑，过度依赖 LLM 可能导致“氛围编程”，而完全拒绝 AI 工具则会被同行甩在身后。Cursor 作为 AI 驱动的代码编辑器，能显著提升开发效率和技能。以下是优化 Cursor 设置的步骤和功能详解：

- 🚀 **核心功能启用**  
  - 启用 Cursor Tab、建议注释、自动导入，提升代码补全和文档效率。  
  - 设置聊天模式为 Agent，支持复杂任务和代码生成。  

- ⚙️ **自动化与保护**  
  - 开启自动刷新、滚动、文件编辑及运行模式，大幅提升效率。  
  - 启用删除文件保护等安全措施，防止意外操作。  

- 📚 **文档集成**  
  - 添加 React、Next.js 和 Tailwind CSS 官方文档链接，增强 AI 上下文理解。  

- 📝 **规则与笔记**  
  - 创建自定义规则（如 React/Next.js/Tailwind 规范），确保代码一致性。  
  - 使用 Notepads 存储开发标准，便于 AI 快速参考。  

- 🔍 **高级工具**  
  - 启用@web 实时搜索，获取最新库版本或 API 变更。  
  - 配置 ESLint 自动修复，提升代码质量。  

- 🔄 **测试驱动开发**  
  - 利用 Cursor 实现 TDD：生成测试用例后迭代代码直至通过。  

- 🔌 **扩展集成**  
  - 通过 MCP 连接数据库或 CMS，实现深度工具交互。  
  - 结合 Builder.io CLI，将 Figma 设计一键转为代码。  

- 🎯 **持续优化**  
  - 定期调整提示词、模型和上下文，适应项目需求。  

通过以上设置，Cursor 可成为 React/Next.js 开发的高效 AI 伙伴，平衡速度与代码质量。

---

### [2025 年打造卓越 React 组件的技巧！- YouTube](https://www.youtube.com/watch?v=SlW2FFBQjt8)

**原文标题**: [Make great React Components in 2025 with these tips! - YouTube](https://www.youtube.com/watch?v=SlW2FFBQjt8)

这是一个关于 YouTube 平台相关信息和链接的页面，涵盖了多个方面的内容。

- ℹ️ 关于 YouTube 的基本信息  
- 📰 新闻与媒体相关  
- ©️ 版权信息  
- 📞 联系方式  
- � 内容创作者相关  
- 💼 广告合作  
- 👩💻 开发者资源  
- 📜 使用条款  
- 🔒 隐私政策  
- ⚖️ 政策与安全  
- ▶️ YouTube 工作原理  
- 🧪 测试新功能  
- © 2025 Google LLC 版权声明

---

### [何时需要在 TanStack Query 中覆盖默认设置 | Kolade Afode](https://www.kxlaa.com/articles/when-you-might-need-to-override-the-defaults-in-tanstack-query)

**原文标题**: [When You Might Need to Override the Defaults in TanStack Query | Kolade Afode](https://www.kxlaa.com/articles/when-you-might-need-to-override-the-defaults-in-tanstack-query)

TanStack Query 默认配置通常适用，但在某些情况下需要覆盖默认设置，例如查询重试和缓存策略的调整。

- 🔄 **查询重试**：默认失败请求重试 3 次，但测试环境中可禁用（`retry: false`）以加速反馈。也可通过回调函数按错误类型（如 404、403）选择性重试。  
- ⏳ **缓存控制**：默认缓存数据被视为过期，可通过`staleTime`和`gcTime`设为无限大来避免重复请求，适合静态数据（如 OAuth 范围列表）。  
- 🚫 **窗口聚焦重试**：通过`refetchOnWindowFocus: false`禁用，减少不必要请求。  
- 📊 **其他配置**：如`refetchOnMount`和`refetchInterval`可进一步定制数据刷新频率。  
- 🔍 **开源参考**：许多项目通过灵活配置优化性能（附案例链接）。

---

### [在 React.js 中使用 AI SDK 从多个模型（LLM）中选择](https://www.robinwieruch.de/react-ai-sdk-multiple-models/)

**原文标题**: [Selecting from Multiple Models (LLMs) with AI SDK in React.js](https://www.robinwieruch.de/react-ai-sdk-multiple-models/)

AI 模型发展迅速，开发者需要将多种模型集成到应用中，以便用户根据需要选择最适合的模型。本文介绍了如何在 Next.js 中使用@ai-sdk 包构建一个多模型聊天界面，支持用户切换不同的 LLM（如 OpenAI 的 GPT-4 Turbo 和 Anthropic 的 Claude 3）。

- 🛠️ **模型配置**：通过`src/app/model.ts`文件定义支持的模型，便于扩展新模型。
- 🔄 **客户端实现**：使用 React 组件实现模型选择、消息发送和响应接收功能。
- 📡 **后端支持**：通过 API 路由处理聊天消息和所选模型，并流式返回 AI 响应。
- 🚀 **灵活扩展**：只需更新`MODELS`对象即可添加新模型，UI 自动更新。

---

### [你可以在 React 中序列化一个 promise](https://twofoldframework.com/blog/you-can-serialize-a-promise-in-react)

**原文标题**: [You can serialize a promise in React](https://twofoldframework.com/blog/you-can-serialize-a-promise-in-react)

React Server Components 中实现 Promise 序列化的巧妙模式，通过流式传输在服务端创建 Promise 并在客户端完成解析。

- 🚀 **服务端创建 Promise**：在服务端组件中创建 Promise，通过 `setTimeout` 模拟异步解析，并传递给客户端组件。
- ⏳ **Suspense 处理加载状态**：使用 `Suspense` 包裹客户端组件，提供 `fallback` 在 Promise 解析前显示等待状态。
- 🔄 **客户端解析 Promise**：客户端组件通过 `use` Hook 读取并解析来自服务端的 Promise，展示最终结果。
- 📦 **JSON 的局限性**：JSON 无法序列化 Promise，常规方法会导致 Promise 信息丢失。
- 🌊 **流式序列化方案**：通过 `ReadableStream` 创建自定义序列化格式，标记 Promise 的生命周期（创建/解析），实现网络共享。
- 🔗 **网络传输与响应**：利用 `Response` 和 `fetch` 实现流的服务端发送与客户端接收，类似实际网络请求。
- 🔄 **反序列化还原 Promise**：客户端通过解析流中的标记消息（如 `promise:create` 和 `promise:resolve`）重建 Promise 及其状态。
- ⚙️ **React 内置序列化**：React 19 的 `react-server` 和 `react-client` 包底层使用流式序列化，通过 `renderToReadableStream` 和 `createFromReadableStream` API 透明化处理。
- 🧩 **广泛的数据类型支持**：React 序列化格式支持原始类型、非原始类型（如 Date/Map）、React 元素及非常规类型（如异步迭代器）。
- 🌐 **RSC 的核心能力**：此机制是 React Server Components 的关键，实现服务端与客户端无缝数据传递，提升开发体验。

---

### [Storybook 9 现已进入测试版](https://storybook.js.org/blog/storybook-9-beta/)

**原文标题**: [Storybook 9 is now in beta](https://storybook.js.org/blog/storybook-9-beta/)

Storybook 9 现已进入测试阶段，这是一个功能完整且雄心勃勃的版本，旨在将 Storybook 打造成高效的 UI 测试工具。

- 🚥 **组件测试工具**：结合单元测试的速度和端到端测试的准确性，适合覆盖大量 UI 状态。  
- ▶️ **交互测试**：支持单独、批量或全局运行，可启用监视模式实时测试。  
- ♿️ **无障碍测试**：全新改进的工作流，支持跨所有故事运行并检查违规情况。  
- 👁️ **视觉测试**：一键测试所有故事，精确到像素级别。  
- 🛡️ **测试覆盖率**：一键计算组件测试的代码覆盖率。  
- 🪶 **体积减小 48%**：比 Storybook 8 更轻量，依赖结构更扁平，安装更快。  
- 🏷️ **基于标签的组织**：新的故事分类和过滤方式。  
- ⚛️ **React Native 全面支持**：支持 Web 和移动设备，兼容文档和测试功能。  
- 🔄 **轻松升级**：通过 `npx storybook@next upgrade` 命令自动迁移，提供代码修改指南。  
- 📢 **反馈需求**：团队欢迎用户测试并报告问题，以进一步完善版本。  

Storybook 9 测试版现已开放试用，期待开发者体验并提供反馈！

---

### [GitHub - callstackincubator/ai：在React Native 中使用 Vercel AI SDK 兼容的本地 LLM 执行](https://github.com/callstackincubator/ai)

**原文标题**: [GitHub - callstackincubator/ai: On-device LLM execution in React Native with Vercel AI SDK compatibility](https://github.com/callstackincubator/ai)

这是一个关于在 React Native 中通过 MLC LLM 引擎实现设备端 LLM 执行并与 Vercel AI SDK 兼容的开源项目。

- 🚀 项目名称：react-native-ai，支持在 React Native 设备端运行 LLM，兼容 Vercel AI SDK
- ⭐ GitHub 数据：301 星标，6 个 fork，MIT 许可证
- 📱 核心功能：通过 MLC LLM 引擎实现设备端 AI 模型执行
- 🔧 安装步骤：
  - 安装 react-native-ai 包
  - 克隆 MLC LLM 仓库并设置环境变量
  - 配置 mlc-config.json 模型文件
  - 平台特定设置（Android 需配置 NDK，iOS 需增加内存限制）
- 💻 主要 API：
  - getModels()：获取可用模型列表
  - downloadModel()：下载指定模型
  - prepareModel()：准备模型使用
  - getModel()：获取与 Vercel AI SDK 兼容的模型实例
- 🔌 与 Vercel AI SDK 集成：可直接使用 streamText 等 Vercel AI SDK 功能
- 🌐 贡献：欢迎贡献，需遵循贡献指南
- ❤️ 开发者：由 Callstack 团队开发维护

---

### [工程师在沟通中常犯的错误](https://newsletter.posthog.com/p/what-engineers-get-wrong-about-communication)

**原文标题**: [What engineers get wrong about communication](https://newsletter.posthog.com/p/what-engineers-get-wrong-about-communication)

工程师在沟通中常犯的错误及改进方法  

- 🎯 **忽视用户需求**：工程师常陷入技术细节，而忽略了解决用户最痛点和最有价值的问题。沟通应始终围绕用户问题或用户体验展开。  
- 🐿️ **信息囤积（松鼠模式）**：囤积信息会导致沟通障碍、重复工作和信任缺失。解决方案是公开记录信息并默认共享。  
- 💡 **缺乏明确观点**：模糊的意见容易被忽视。形成有证据支持的观点并自信表达，能推动更快决策和行动。  
- 📊 **缺少上下文**：低上下文的沟通会增加接收者的负担。应包含数据、用户反馈和具体问题背景，帮助对方高效解决问题。  
- 🕰️ **缺乏结构化沟通**：过度或不足的沟通都会影响效率。通过固定仪式（如周会、冲刺计划）确保信息有序流动。  
- 🚀 **沟通缺乏行动导向**：避免冗长流程，明确责任人、下一步和截止时间，确保沟通直接推动实际进展。  

通过避免这些错误，可以建立高效、透明的沟通文化，提升团队协作和产品交付效率。

---

### [获取失败](https://react.statuscode.com/link/168597/web)

**原文标题**: [Failed to retrieve](https://react.statuscode.com/link/168597/web)

无法总结：获取内容失败，状态码 429。

---

### [获取失败](https://react.statuscode.com/link/168598/web)

**原文标题**: [Failed to retrieve](https://react.statuscode.com/link/168598/web)

无法总结：获取内容失败，状态码 429。

---

### [GitHub - simonedevit/reactylon：基于Babylon.js和React构建的强大跨平台框架，专为创建交互式和沉浸式XR体验而设计。](https://github.com/simonedevit/reactylon)

**原文标题**: [GitHub - simonedevit/reactylon: A powerful multiplatform framework built on top of Babylon.js and React, designed to create interactive and immersive XR experiences.](https://github.com/simonedevit/reactylon)

Reactylon 是一个基于 Babylon.js 和 React 的跨平台框架，旨在创建交互式和沉浸式 XR 体验。它支持声明式语法、TypeScript、自动对象管理，并简化了场景管理和组件层次结构。

- 🚀 **跨平台框架**：基于 Babylon.js 和 React，支持创建交互式和沉浸式 XR 体验。  
- ✍️ **声明式语法**：通过 JSX 编写 3D 场景，无缝集成 Babylon.js 渲染引擎。  
- 🔍 **TypeScript 支持**：自动生成 Babylon.js 实体的对应 React 组件属性。  
- 🧹 **自动对象管理**：自动处理 Babylon.js 对象的销毁，防止内存泄漏。  
- 🌍 **跨平台支持**：支持桌面、移动浏览器（PWA）、VR/AR 头显及原生移动设备。  
- 🎭 **场景注入**：自动将 Babylon.js 场景对象注入每个组件，减少样板代码。  
- 👨‍👩‍👧‍👦 **父子关系管理**：自动处理组件层次结构，简化复杂场景图的构建。  
- ⚛️ **深度 React 集成**：支持状态管理、组件组合和钩子，提升开发体验。  
- 📚 **文档与支持**：提供详细文档和贡献指南，支持通过 contact@reactylon.com 联系。  
- 📜 **开源许可**：基于 MIT 许可证，依赖项如 Babylon.js 和 React 分别遵循 Apache 2.0 和 MIT 许可证。

---

### [又一个 React 灯箱 - 适用于 React 的现代灯箱组件](https://yet-another-react-lightbox.com/)

**原文标题**: [Yet Another React Lightbox - Modern lightbox component for React](https://yet-another-react-lightbox.com/)

概述：Yet Another React Lightbox 是一个现代、高性能且易于定制的 React 轻量级弹窗组件，支持多种功能和插件，适用于各种场景。

- 🚀 **React 兼容**：支持 React 18、17 和 16.8.0+ 版本。  
- 🖱️ **多样化导航**：支持键盘、鼠标、触摸板和触摸屏操作。  
- ⚡ **预加载优化**：避免显示未完全下载的图像，提升用户体验。  
- 🏎️ **性能优先**：智能预加载有限数量的图像，不影响性能。  
- 📱 **响应式支持**：自动适配不同分辨率，提供最佳显示效果。  
- 🎥 **视频支持**：通过插件支持视频幻灯片播放。  
- 🔍 **图像缩放**：通过插件实现图像缩放功能。  
- 🎨 **高度可定制**：可自定义 UI 元素或添加自定义幻灯片。  
- 📦 **模块化设计**：按需加载功能插件，避免代码冗余。  
- 📜 **TypeScript 支持**：内置类型定义。  
- ↔️ **RTL 兼容**：支持从右到左的布局。  

- 📚 **文档与示例**：  
  - 文档：[官网文档](https://yet-another-react-lightbox.com/documentation)  
  - 示例：[官网示例](https://yet-another-react-lightbox.com/examples)  
  - 更新日志：[GitHub Releases](https://github.com/igordanchenko/yet-another-react-lightbox/releases)  

- 💻 **安装与使用**：  
  - 安装命令：`npm install yet-another-react-lightbox`  
  - 支持响应式图像（自动切换分辨率）和第三方图像组件集成。  

- 🔌 **插件功能**：  
  - 标题（Captions）、计数器（Counter）、下载（Download）、全屏（Fullscreen）等。  
  - 内联模式（Inline）、分享（Share）、幻灯片播放（Slideshow）、缩略图（Thumbnails）等。  

- 📜 **许可证**：MIT © 2022 Igor Danchenko

---

### [游乐场 | 又一个 React 灯箱组件](https://yet-another-react-lightbox.com/examples/playground)

**原文标题**: [Playground | Yet Another React Lightbox](https://yet-another-react-lightbox.com/examples/playground)

这是一个交互式演示界面，用于实时调整和预览不同参数效果的展示平台。

- 🎮 实时交互：提供实时调整参数的互动功能  
- ⚙️ 参数设置：可调节幻灯片索引、预加载、淡入淡出时长等  
- 🖼️ 图片控制：支持图片填充模式（contain）、边距和间距设置  
- ♾ 循环播放：开启无限循环播放选项  
- 🛠️ 操作按钮：包含上一页/下一页按钮控制  
- 👆 手势关闭：支持上拉/下拉或背景点击关闭  
- 📁 示例切换：可跳转查看基础示例或相册案例  
- 💻 代码编辑：支持通过 StackBlitz 在线编辑代码

---

### [GitHub - igordanchenko/yet-another-react-lightbox: 又一个现代化的 React 灯箱组件](https://github.com/igordanchenko/yet-another-react-lightbox)

**原文标题**: [GitHub - igordanchenko/yet-another-react-lightbox: Modern React lightbox component](https://github.com/igordanchenko/yet-another-react-lightbox)

一个现代的 React 轻量级灯箱组件，支持多种功能和插件，适用于各种图片和视频展示需求。

- 🌟 项目名称：Yet Another React Lightbox  
- 🚀 功能特点：支持键盘、鼠标、触摸板及触摸屏导航  
- 🖼️ 图片预加载：避免显示未完全下载的图片  
- ⚡ 性能优化：预加载有限数量的图片，不影响性能  
- 📱 响应式设计：自动适应不同分辨率的图片  
- 🎥 视频支持：通过插件支持视频幻灯片  
- 🔍 缩放功能：通过插件支持图片缩放  
- � 高度可定制：可自定义 UI 元素或添加自定义幻灯片  
- 📦 无冗余功能：按需添加插件功能  
- 📜 文档齐全：提供详细文档和示例  
- 📥 安装方式：通过 npm 安装  
- 🛠️ 插件支持：包括标题、计数器、下载、全屏等多种插件  
- 📄 开源协议：MIT 许可证

---

### [GitHub - Temzasse/react-modal-sheet: 基于 Motion 构建的灵活底部面板组件，提供丝滑用户体验，同时兼顾无障碍性 🪐](https://github.com/Temzasse/react-modal-sheet)

**原文标题**: [GitHub - Temzasse/react-modal-sheet: Flexible bottom sheet component built with Motion to provide buttery smooth UX while keeping accessibility in mind 🪐](https://github.com/Temzasse/react-modal-sheet)

一个基于 Motion 构建的灵活底部弹窗组件，专注于流畅用户体验和可访问性。

- 🌟 项目亮点：943 星标 | 91 复刻 | MIT 许可
- 🛠️ 技术栈：React + Motion 动画库（需单独安装）
- 🪄 核心特性：支持平滑拖拽、自适应高度、多档位吸附点（snapPoints）
- 🧩 组件化设计：通过 Container/Header/Content/Backdrop 等子组件自由组合
- 📱 移动优化：自动处理触摸设备滚动冲突，支持虚拟键盘场景
- ♿️ 无障碍支持：可与 React Aria 等无障碍工具链集成
- 🎨 深度定制：支持自定义样式/头部/动画参数（如 iOS 模态效果）
- ⚠️ 已知问题：StrictMode 下动画可能异常（Motion 库限制）
- 🌐 示例演示：temzasse.github.io/react-modal-sheet/

---

### [Gridstack.js | 快速构建交互式仪表盘](https://gridstackjs.com/)

**原文标题**: [Gridstack.js | Build interactive dashboards in minutes.](https://gridstackjs.com/)

概述  
Gridstack.js 是一个简单易用的交互式网格布局工具，支持拖放、自定义配置，并提供基础与高级功能演示。它被多家公司采用，并受到开发者社区的广泛推荐。  

- 🛠️ **基础演示** - 简单易用，支持拖放和自定义配置，只需复制粘贴代码即可快速上手。  
- 📦 **安装与使用** - 通过 npm 安装，引入 JS 和 CSS 文件，即可创建交互式网格。  
- 🏗️ **代码示例** - 提供完整的 HTML+JS 示例，包括网格初始化、加载项目和样式设置。  
- 🎮 **高级演示** - 支持更复杂的功能，如删除部件、拖入部件等，展示 gridstack.js 的强大功能。  
- 📊 **受欢迎程度** - 在 npmjs.org 上统计表现良好，并被列入 2020 年最佳 jQuery 布局插件之一。  
- 🏢 **企业应用** - 被多家公司采用，鼓励更多企业加入并分享使用案例。  
- 💬 **社区支持** - 提供 Slack 社区，方便用户交流与反馈。

---

### [next-intl – Next.js 国际化（i18n）方案](https://next-intl.dev/)

**原文标题**: [next-intl – Internationalization (i18n) for Next.js](https://next-intl.dev/)

next-intl 是一个专为 Next.js 设计的国际化（i18n）解决方案，支持多语言、简化代码并提供丰富的功能。

- 🌍 **多语言支持**：轻松实现多语言切换，优化用户体验。
- 🛠️ **简洁 API**：提供最小化但功能齐全的 API，便于集成和使用。
- 📅 **日期、时间和数字格式化**：自动处理时区和本地化格式。
- 🔍 **类型安全**：通过编译时检查和自动补全提高开发效率。
- ⚛️ **Hooks 驱动**：统一的 API 适用于字符串和富文本翻译。
- ⚡ **高性能**：支持 App Router、Server Components 和静态渲染。
- 🛤️ **国际化路由**：为每种语言提供独特的路径名，支持 SEO 优化。
- 💡 **社区认可**：被多个知名项目和开发者广泛使用和推荐。

---

### [发布 v4.0.0 · chartbrew/chartbrew · GitHub](https://github.com/chartbrew/chartbrew/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · chartbrew/chartbrew · GitHub](https://github.com/chartbrew/chartbrew/releases/tag/v4.0.0)

Chartbrew 发布了 v4.0.0 版本，包含重要的更新、新功能、改进和错误修复，同时引入了新的双重许可模式。

- ⚠️ **重要变更**：需要 Node.js 22+ 环境运行，并采用双重许可（功能源许可证和商业许可证）。
- ✨ **新功能**：新增定时快照交付、长文本弹出查看、3 种更大断点布局、图表紧凑模式、KPI 增长反转选项。
- 🚀 **功能改进**：自动格式化 URL、优化连接搜索、支持单查询参数内日期变量、警报数字显示优化、新手引导增强。
- � **设计优化**：KPI 字体和标签视觉升级、数据标签和格式统一性提升。
- 🐛 **错误修复**：修复 Express 5 查询解析、用户面板宽度问题、仪表图计算错误等。
- 🛂 **权限调整**：限制部分角色对连接页面的访问。
- 📝 **其他更新**：新增 v4 博客公告、升级 Vite 至 v6、依赖项小幅更新。

---

### [发布 v8.1.0 · mui/mui-x · GitHub](https://github.com/mui/mui-x/releases/tag/v8.1.0)

**原文标题**: [Release v8.1.0 · mui/mui-x · GitHub](https://github.com/mui/mui-x/releases/tag/v8.1.0)

MUI-X 发布了 v8.1.0 版本，包含多项功能更新、Bug 修复和文档改进，特别感谢 14 位贡献者的努力。

- 🚀 **新功能**：新增图表打印或导出为 PDF 的 API `apiRef.exportAsPrint()`  
- 📊 **Data Grid 更新**：支持多选行取消选择、修复触摸设备列标题截断问题  
- 📅 **日期时间选择器改进**：优化类型定义和基础组件  
- 📈 **图表增强**：新增本地化支持、优化工具提示性能、雷达图进入预览阶段  
- 🌳 **Tree View 内部调整**：无显著功能变化，主要为内部优化  
- 📚 **文档优化**：修复演示问题、改进 StackOverflow 链接、移除付费页面广告  
- 🛠 **核心调整**：移除冗余依赖、更新支持表、优化代码基础设施  

特别鸣谢社区成员和团队贡献者，包括 @lhilgert9、@ArturAghakaryan 等。

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的交互式命令行应用开发工具，它允许开发者使用熟悉的 React 组件模型来构建 CLI 应用。Ink 使用 Yoga 引擎实现 Flexbox 布局，支持大多数类似 CSS 的样式属性。Ink 兼容 React 的所有特性，并提供了丰富的内置组件和钩子函数来简化 CLI 应用的开发。

- 🌈 **React for CLIs**：Ink 提供与浏览器中相同的基于组件的 UI 构建体验，但适用于命令行应用。
- 🛠 **Flexbox 布局**：使用 Yoga 引擎在终端中构建 Flexbox 布局，支持大多数 CSS 样式属性。
- 📦 **内置组件**：提供 `<Text>`、`<Box>`、`<Newline>`、`<Spacer>`、`<Static>` 和 `<Transform>` 等组件。
- 🎣 **钩子函数**：包括 `useInput`、`useApp`、`useStdin`、`useStdout`、`useStderr`、`useFocus` 和 `useFocusManager` 等。
- 📝 **API**：提供 `render`、`rerender`、`unmount`、`waitUntilExit` 和 `measureElement` 等方法。
- 🧪 **测试支持**：可以使用 `ink-testing-library` 进行测试。
- 🔧 **React Devtools 支持**：支持使用 React Devtools 进行调试。
- 📚 **丰富的示例**：包含计数器、表单、表格、焦点管理等示例。
- 🏆 **知名用户**：包括 Codex、GitHub Copilot for CLI、Cloudflare's Wrangler、Gatsby 等。
- 📜 **MIT 许可证**：开源且免费使用。

---

### [给 V8 一个提示：利用显式编译提示加速 JavaScript 启动 · V8](https://v8.dev/blog/explicit-compile-hints)

**原文标题**: [Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints · V8](https://v8.dev/blog/explicit-compile-hints)

V8 引擎通过显式编译提示优化 JavaScript 启动性能，开发者可指定关键函数或文件在初始阶段编译，从而减少页面加载时的解析和编译时间，提升网页响应速度。

- 🚀 **性能瓶颈**：V8 在启动时解析和编译关键 JavaScript 可能导致性能延迟，影响网页加载速度。  
- 🔧 **编译策略**：V8 需选择立即编译（eager）或延迟编译函数，后者在调用时触发但无法并行处理。  
- ⏳ **重复工作**：延迟编译需重新解析函数语法，而立即编译可利用后台线程与网络加载并行。  
- 📊 **实验效果**：测试显示 17/20 的网页性能提升，平均减少 630 毫秒前台解析编译时间。  
- 💡 **显式编译提示**：Chrome 136 支持通过`//# allFunctionsCalledOnLoad`注释标记需立即编译的文件。  
- ⚠️ **谨慎使用**：过度编译会消耗时间和内存，建议仅标记核心文件或关键函数。  
- 🔍 **验证方法**：通过 Chrome 命令行日志可观察函数编译事件，区分立即与延迟编译。  
- 🔮 **未来方向**：计划支持单个函数级别的编译控制，进一步优化性能。

---

### [未找到标题](https://www.solidjs.com/)

**原文标题**: [No title found](https://www.solidjs.com/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

（这里是概述总结）  
- 🌟 要点一  
- 📌 要点二  
- 🔍 要点三  

请提供具体文本，我会为您生成符合要求的中文摘要。

---

### [SolidJS 的十年历程 - DEV 社区](https://dev.to/this-is-learning/a-decade-of-solidjs-32f4)

**原文标题**: [A Decade of SolidJS - DEV Community](https://dev.to/this-is-learning/a-decade-of-solidjs-32f4)

Ryan Carniato 回顾了 SolidJS 从诞生至今的十年发展历程，从个人兴趣项目到影响前端生态的框架演变。

- 🚀 **开源初衷**：2015 年因对细粒度响应式编程的争议，Ryan 为验证性能优势开始开发 SolidJS，2018 年正式开源。  
- 💡 **技术突破**：早期借鉴 Knockout 信号机制，放弃虚拟 DOM，通过 JSX 实现高性能渲染，2019 年在各项基准测试中领先。  
- 🔄 **生态影响**：推动 Vue、Svelte 等框架转向信号机制，Angular、Preact 等也受其启发，形成行业趋势。  
- 🛠 **功能完善**：2 年内实现 Suspense、SSR 等现代框架特性，证明细粒度模型可覆盖 VDOM 所有能力。  
- 🌍 **社区建设**：从无人问津到获得 Netlify 等公司支持，通过 SolidHack 等活动培育生态，吸引开发者共建。  
- 🧠 **理念冲突**：早期遭遇质疑，React 生态开发者难以接受非 VDOM 方案，但最终用技术证明可行性。  
- 🔮 **未来展望**：认为信号机制仅是起点，将继续探索该模型独有的前沿能力，重塑 Web 开发体验。  

（注：评论区内容聚焦开发者对 SolidJS 的认可与 Ryan 坚持创新的赞赏，未纳入核心摘要）

---

### [SolidJS 正式发布：通往 1.0 版本的漫长之路 - DEV 社区](https://dev.to/ryansolid/solidjs-official-release-the-long-road-to-1-0-4ldd)

**原文标题**: [SolidJS Official Release: The long road to 1.0 - DEV Community](https://dev.to/ryansolid/solidjs-official-release-the-long-road-to-1-0-4ldd)

SolidJS 1.0 正式发布，这是一个经过五年多开发、数千小时投入的 JavaScript 框架，结合了 React 的灵活性和 Svelte 的简单性，同时提供了高性能和接近原生 DOM 的开发体验。

- 🚀 **开发历程**：SolidJS 始于 2016 年，经过多次原型迭代，最终在 2021 年发布 1.0 稳定版。
- 💡 **独特之处**：SolidJS 是一个无虚拟 DOM 的响应式框架，结合了 JSX 的灵活性和接近原生 DOM 的性能。
- ⚡ **高性能**：SolidJS 在浏览器和服务器端都是目前最快的 JavaScript 框架之一。
- 🔧 **强大功能**：支持并发渲染、过渡动画、流式服务器端渲染（SSR）和渐进式 hydration。
- 📦 **生态系统**：提供丰富的工具支持，包括 Vite 模板、TypeScript 支持和第三方库集成。
- 🌐 **未来计划**：正在开发 Solid Start（一个基于 Vite 的同构启动模板）和与 Astro 的集成。
- 🙏 **社区贡献**：SolidJS 的成功离不开社区的支持，特别是 S.js 和 Surplus.js 的创始人 Adam Haile 的贡献。

---

### [非 HTML 内容](https://bun.sh/llms-full.txt)

**原文标题**: [Non-HTML content](https://bun.sh/llms-full.txt)

无法总结：非 HTML 内容。

---

### [使用 pnpm 和 Yarn 添加 JSR 包](https://deno.com/blog/add-jsr-with-pnpm-yarn)

**原文标题**: [Add JSR packages with pnpm and Yarn](https://deno.com/blog/add-jsr-with-pnpm-yarn)

JSR 现在支持通过 pnpm 和 Yarn 直接安装包，并且可以处理带有 JSR 依赖的 npm 包，同时也支持发布带有 JSR 依赖的 npm 包。

- 📢 **JSR 支持 pnpm 和 Yarn**  
  现在可以通过 pnpm 和 Yarn 直接安装 JSR 包，并且支持处理带有 JSR 依赖的 npm 包。

- 📦 **pnpm 安装方法**  
  从 pnpm v10.9 开始，支持通过 `pnpm add jsr:<scope>/<pkg_name>` 安装 JSR 包，并自动更新 `package.json`。

- 🧶 **Yarn 安装方法**  
  从 Yarn v4.9.0 开始，支持通过 `yarn add jsr:<scope>/<pkg_name>` 安装 JSR 包，并自动更新 `package.json`。

- 🔗 **更多功能与社区**  
  JSR 是一个现代的 JavaScript 和 TypeScript 注册表，提供更多功能，并欢迎开发者加入 Discord、Twitter、Bluesky 或 YouTube 社区交流。

- 🚀 **未来计划**  
  JSR 将分享更多关于模块作者发布带有 JSR 依赖的包的信息，并定期举办双周办公时间讨论路线图和解答问题。

---

### [发布 electron v36.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v36.0.0)

**原文标题**: [Release electron v36.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v36.0.0)

Electron v36.0.0 版本发布，包含多项功能更新、改进和错误修复。

- 🚀 **核心升级**：Chromium 升级至 136.0.7103.48，Node.js 升级至 22.14.0，V8 引擎升级至 13.6。
- ⚠️ **重大变更**：废弃了 `NativeImage.getBitmap()`，移除了 `systemPreferences.isAeroGlassEnabled()` API。
- ✨ **新功能**：
  - 新增 `BrowserWindow.isSnapped()` 用于检测窗口是否已通过 Snap 排列。
  - 新增 `ServiceWorkerMain` 类以在主进程中与服务工作者交互。
  - 新增 `contextBridge.executeInMainWorld` 以安全地跨世界边界执行代码。
  - 支持 Windows 上的 `roundedCorners` 窗口选项。
- 🛠️ **改进**：
  - 改进了 Windows 上的 ASAR 完整性检查。
  - 优化了 macOS 上 `desktopCapturer.getSources` 的性能。
- 🐛 **错误修复**：
  - 修复了 macOS 上 `getNativeWindowHandle()` 的崩溃问题。
  - 修复了 Linux 上 `webContents.print()` 的崩溃问题。
  - 修复了 Windows 上拖放文件图标不显示的问题。
  - 修复了 macOS 上透明窗口的闪烁和重影问题。
- 📜 **其他变更**：
  - 更新了文档，标记 `Window.autoHideMenuBar` 在 Linux 和 Windows 上受支持。
  - 修复了多个崩溃和内存泄漏问题。

---

### [发布 pnpm 10.10 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.10.0)

**原文标题**: [Release pnpm 10.10 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.10.0)

pnpm 是一个流行的 JavaScript 包管理工具，最新版本为 v10.10.0，包含了一些功能改进和错误修复。

- 🚀 **最新版本**：pnpm 发布了 v10.10.0 版本，包含了一些次要更改和补丁修复。  
- 🔧 **功能改进**：允许从本地 pnpmfile 加载 `preResolution`、`importPackage` 和 `fetchers` 钩子。  
- 🐛 **错误修复**：修复了 `shellEmulator` 为 `true` 时的 `cd` 命令问题，优化了 `pnpm-workspace.yaml` 的键排序，并修正了 `--reporter=silent` 选项的描述错误。  
- ⚙️ **环境变量**：现在会将 `npm_package_json` 环境变量传递给执行的脚本。  
- 💖 **社区支持**：获得了铂金赞助商和黄金赞助商的支持，社区反应热烈，包括点赞、庆祝、爱心和火箭等表情。

---

### [Node.js — Node.js 版本发布](https://nodejs.org/en/about/previous-releases)

**原文标题**: [Node.js — Node.js Releases](https://nodejs.org/en/about/previous-releases)

Node.js 的版本发布和支持周期概述，以及官方与社区安装方法的分类标准。

- 🚀 **Node.js 版本发布周期**：主要版本发布后有 6 个月的当前支持期，之后奇数版本停止支持，偶数版本进入 Active LTS 阶段，适合生产环境使用。  
- 🛡️ **LTS 支持**：长期支持版本（LTS）提供 30 个月的关键 bug 修复，生产应用应使用 Active LTS 或 Maintenance LTS 版本。  
- 📅 **发布计划**：详细发布计划可在 GitHub 上查看。  
- 💼 **商业支持**：超过维护阶段的版本可通过 OpenJS Ecosystem Sustainability Program 合作伙伴 HeroDevs 获得商业支持。  
- 🔍 **版本状态查询**：提供多个版本的代号、首次发布日期、最后更新日期和当前状态（如 Maintenance、LTS、End-of-life 等）。  
- 📥 **安装方法分类**：Node.js 官网将安装方法分为“官方”和“社区”两类，以提供更多选择和灵活性。  
- ✅ **官方安装方法要求**：必须与 Node.js 项目保持紧密联系，提供官方二进制文件，且不修改或从源代码构建。  
- 🌍 **社区安装方法要求**：必须支持所有非 EOL 版本，兼容至少一个官方支持的操作系统，且不能限制特定的 OS 发行版或版本。  
- 🆓 **开源免费**：社区安装方法必须是免费和开源的，不能作为商业产品或付费服务提供。

---

### [Node 周刊](https://nodeweekly.com/)

**原文标题**: [Node Weekly](https://nodeweekly.com/)

Node Weekly 是一份免费的每周电子邮件简报，专注于 Node.js 的新闻和文章。  

- 📧 每周免费订阅，提供 Node.js 的最新动态和文章  
- 🧑‍🤝‍🧑 拥有 62,820 名订阅者，已发布 576 期  
- 📰 支持 RSS 订阅，可查看最新一期作为示例  
- 🏢 由 Cooperpress 发布，注重隐私和反垃圾邮件政策  
- ®️ Node.js 是 Joyent, Inc 的注册商标，经授权使用

---

