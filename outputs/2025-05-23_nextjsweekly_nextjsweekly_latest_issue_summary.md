### [Next.js 服务器操作是对外公开的 API 端点](https://growl.dev/blog/nextjs-server-actions/)

**原文标题**: [Next.js Server Actions are public-facing API endpoints](https://growl.dev/blog/nextjs-server-actions/)

Next.js 的 Server Actions 实际上是公开的 API 端点，开发者无需自行创建 API 端点即可通过用户交互执行服务器端代码。尽管官方文档强调了安全性，但缺乏详细示例。本文通过实验展示了 Server Actions 的工作原理及潜在风险。

- 🚀 **Server Actions 本质**：是公开的 API 端点，开发者无需手动创建 API 即可执行服务器代码。  
- 🔍 **调用方式**：通过 POST 请求和`Next-Action`头调用，端点即触发动作的页面路径。  
- 🛠 **实验验证**：使用`curl`发送请求，成功触发服务器端的`console.log`输出。  
- 📦 **参数传递**：参数需可序列化为 JSON，通过请求体传递。  
- 🔐 **安全隐患**：动作 ID 可通过客户端代码暴露，即使有条件渲染也可能泄露。  
- 🛡 **内置安全**：Next.js 提供加密 ID 和死代码消除，但开发者仍需主动添加认证层。  
- 📚 **结论**：Server Actions 应像传统 API 一样严格防护，开发者需深入理解框架抽象。

---

### [直接用 React 就完了](https://justfuckingusereact.com/)

**原文标题**: [Just Fucking Use React](https://justfuckingusereact.com/)

这篇文章以激烈幽默的语言，阐述了在现代 Web 开发中使用框架（如 React）的必要性，并批判了过度依赖纯 HTML 和原生 JavaScript 的固执态度。

- 🚀 **框架的必要性**：现代 Web 应用需要处理复杂交互和动态内容，纯 HTML 已无法满足需求。  
- 🔄 **组件化开发**：框架提供可复用的组件，避免重复代码和维护噩梦。  
- ⚡ **智能 UI 更新**：框架自动处理 DOM 更新，减少手动操作的繁琐和错误。  
- ♿ **可访问性**：框架帮助实现复杂的无障碍功能，而纯 HTML 难以规模化。  
- 🛠️ **开发者体验**：框架生态提供高效工具（如热更新、TypeScript），提升开发效率。  
- ⚖️ **性能权衡**：框架的“臃肿”是为复杂功能付出的合理代价，可通过优化手段缓解。  
- 🤔 **适用场景**：框架适合有复杂状态管理、团队协作或高交互需求的应用，而非简单静态页面。  
- 🔥 **核心问题**：滥用工具（如用 React 做静态页）是开发者的问题，而非框架本身。  

文章最终呼吁开发者根据实际需求选择工具，而非盲目抵制现代技术。

---

### [Next.js 超时问题的 4 种解决方案 - Inngest 博客](https://www.inngest.com/blog/vercel-function-timeout?ref=nextjs-weekly-1)

**原文标题**: [4 solutions to Next.js timeouts - Inngest Blog](https://www.inngest.com/blog/vercel-function-timeout?ref=nextjs-weekly-1)

Next.js 超时问题的四种解决方案，包括调整超时设置、使用新工具以及升级计划等。

- ⏱️ 增加 Vercel 函数最大持续时间：通过修改 `vercel.json` 文件，可将单个函数的超时时间从默认的 10 秒延长至 60 秒。不建议全局设置，以免消耗免费额度或难以排查问题。  
- 💧 启用 Vercel Fluid Compute：该功能优化了网络密集型函数的计算资源分配，使长时间运行的代码（如数据导入）在免费计划下可运行 1 分钟，付费计划下可达 14 分钟。  
- 🔄 使用持久化函数（Durable Functions）：将同步代码转为异步执行，结合 Fluid Compute 可延长运行时间至数小时，并支持进度流式更新、自动重试等功能。  
- 🚀 升级至 Vercel 付费计划：Pro 计划支持最高 5 分钟超时（默认 15 秒），企业计划可达 15 分钟（默认 15 秒），适合必须同步返回响应的场景。

---

### [复杂 React/Next.js 应用的健壮数据获取架构](https://www.trevorlasn.com/blog/fetching-data-for-complex-next-and-react-apps)

**原文标题**: [Robust Data Fetching Architecture For Complex React/Next.js Apps](https://www.trevorlasn.com/blog/fetching-data-for-complex-next-and-react-apps)

文章概述了在复杂 React/Next.js 应用中采用"三层数据架构"模式来优化数据获取、避免技术债务和提升性能的方法。作者指出了常见的数据获取问题，并提出了解决方案。

- 🏗️ 数据获取复杂性常被低估，导致项目后期出现诸多问题  
- 🚨 常见问题包括重复请求、状态管理混乱、缓存失效、竞态条件等  
- 💡 提出"三层数据架构"模式：服务端组件、React Query 客户端缓存、乐观更新  
- 🔄 架构流程：服务端初始获取 → 客户端状态管理 → 即时 UI 反馈  
- 🛠️ 推荐使用 React Query 处理客户端状态和缓存  
- ⚡ 乐观更新可提供即时用户体验  
- 📁 通过上下文提供者集中管理数据访问  
- ⚖️ 该架构适合复杂应用，简单应用可能过度设计  
- 🔗 类似架构可应用于 Vue.js 等其他框架  
- 📚 作者提供相关技术文章推荐和资源链接

---

### [大卫·克里米，软件工程师](https://www.david-crimi.com/blog/user-auth)

**原文标题**: [David Crimi, Software Engineer.](https://www.david-crimi.com/blog/user-auth)

概述：本文详细介绍了如何在 FastAPI 后端和 Next.js 前端应用中实现安全、高效的 JWT 认证与授权方案，涵盖核心策略、前后端实现及常见问题的解决方案。

- 🔐 核心策略：基于 JWT 的无状态认证、HTTP-only Cookie 存储令牌、FastAPI 依赖注入与 Next.js 路由保护的无缝集成  
- 🏗️ 后端实现：通过 JWT 类生成访问/刷新令牌，登录流程包含用户查询、密码验证和令牌签发  
- 🛡️ 端点保护：利用 OAuth2 依赖验证令牌，自动处理 401 未授权和令牌过期情况  
- 🔄 刷新机制：单次使用的刷新令牌存储于数据库，刷新时生成新令牌并更新数据库记录  
- 🌐 前端集成：使用 NextAuth.js 管理会话，CredentialsProvider 对接后端登录接口  
- ⚙️ 自定义 Hook：封装 JWT 认证流程，自动处理令牌刷新和请求重试逻辑  
- 🏎️ 并发问题：解决多请求同时刷新令牌的竞态条件，建议采用请求重试策略  
- 🔄 会话更新：通过 NextAuth 的 jwt/session 回调实现令牌更新与用户数据同步  
- 🛠️ 实用示例：提供登录表单组件和 API 请求 Hook 的具体实现代码  
- 💡 优化建议：推荐结合 TanStack Query 实现自动重试机制提升并发场景稳定性

---

### [这个 Next.js 数据获取模式对每个开发者都至关重要 - YouTube](https://www.youtube.com/watch?v=bKm1rNaCFOo&ab_channel=ByteGrad)

**原文标题**: [This Next.js Data Fetching Pattern Is CRITICAL For Every Developer - YouTube](https://www.youtube.com/watch?v=bKm1rNaCFOo&ab_channel=ByteGrad)

这是一个关于 YouTube 相关服务和政策的页面概览。

- 📰 プレスルーム - 媒体和新闻相关资源  
- ©️ 著作権 - 版权信息  
- 📧 お問い合わせ - 联系与支持渠道  
- 🎨 クリエイター向け - 创作者专属资源与服务  
- 💰 広告掲載 - 广告投放与合作  
- 💻 開発者向け - 开发者工具与支持  
- 📜 利用規約 - 平台使用条款  
- 🔒 プライバシー - 隐私保护政策  
- 🛡️ ポリシーとセキュリティ - 政策与安全指南  
- ⚙️ YouTube の仕組み - 平台运作机制说明  
- 🆕 新機能を試してみる - 体验最新功能  
- 🏢 © 2025 Google LLC - 公司版权声明

---

### [React 中的依赖倒置：构建真正可测试的组件 · cekrem.github.io](https://cekrem.github.io/posts/dependency-inversion-in-react/)

**原文标题**: [Dependency Inversion in React: Building Truly Testable Components · cekrem.github.io](https://cekrem.github.io/posts/dependency-inversion-in-react/)

概述  
本文探讨了如何在 React 开发中应用依赖倒置原则（DIP），以构建更易测试和维护的组件。通过解耦组件与具体依赖的关系，依赖抽象接口，可以显著提升代码的灵活性和可测试性。

- 🏗️ **依赖倒置原则（DIP）**：高層模塊不應依賴低層模塊，兩者都應依賴抽象。在 React 中，組件應依賴接口而非具體實現。  
- 🔗 **緊耦合問題**：常見的 React 組件直接調用 API（如`fetch`），導致測試困難、數據源難以更換，且無法輕鬆模擬加載狀態。  
- 🛠️ **解決方案**：通過抽象接口（如`UserRepository`）定義依賴，並將具體實現（如`ApiUserRepository`或`MockUserRepository`）注入組件。  
- 🧪 **測試優勢**：使用模擬倉庫（Mock）可輕鬆測試組件的加載狀態、數據渲染及異常場景，無需真實 API 調用。  
- 📚 **最佳實踐**：  
  - 明確定義接口（如`getUser`方法）。  
  - 通過 Props 或 Context 注入依賴（或使用`TSyringe`等庫）。  
  - 隔離測試組件，避免依賴具體實現。  
- 🎯 **效益**：提升代碼可測試性、可維護性、關注點分離，並增強靈活性。  
- 📖 **延伸閱讀**：推薦《Clean Architecture》、React Testing Library 文檔，以及關於單一職責原則的相關文章。  
- ⚠️ **注意**：本文未深入依賴注入的具體實現，但提及`TSyringe`等工具可進一步管理依賴。

---

### [AI 聊天机器人](https://www.kibo-ui.com/blocks/ai-chatbot)

**原文标题**: [AI Chatbot](https://www.kibo-ui.com/blocks/ai-chatbot)

React Hooks 使用指南与性能优化技巧  

- 📌 **React Hooks 核心作用**：无需编写类组件即可使用状态和其他 React 功能。  
- ⚠️ **Hooks 使用规则**：  
  - 仅在组件或自定义 Hooks 的顶层调用  
  - 避免在循环、条件或嵌套函数中使用  
- 🔧 **常用 Hooks 功能**：  
  - `useState`：管理本地组件状态  
  - `useEffect`：处理数据获取等副作用  
  - `useContext`：消费上下文  
  - `useReducer`：处理复杂状态逻辑  
- 🔄 **useCallback 与 useMemo 对比**：  
  - `useCallback`：缓存函数，避免子组件因引用变化重复渲染  
  - `useMemo`：缓存计算结果，减少昂贵重复运算  
- 📊 **性能优化建议**：  
  - 仅在确有必要时使用 `useCallback`/`useMemo`（如子组件依赖引用相等性或高计算开销场景）  
  - 过度使用可能增加额外性能负担  
- 🌟 **示例代码**：  
  - 结合 `useState` 和 `useEffect` 实现数据获取与渲染  
  - 通过依赖数组（如 `[userId]`）控制 Hook 执行时机

---

### [Zod 4 发布公告 | Zod](https://zod.dev/v4)

**原文标题**: [Introducing Zod 4 | Zod](https://zod.dev/v4)

Zod 4 正式发布，带来多项性能提升和新功能，包括更快的解析速度、更小的包体积以及改进的类型推断。

- 🚀 **性能提升**：Zod 4 在字符串解析、数组解析和对象解析方面分别比 Zod 3 快 14 倍、7 倍和 6.5 倍。
- 📦 **包体积优化**：核心包体积减少 2 倍，引入 Zod Mini 后进一步减少 6.6 倍。
- 🔧 **新功能**：支持递归对象、文件验证、国际化错误消息、JSON Schema 转换等。
- 📝 **错误处理改进**：简化错误定制 API，引入全局错误美化功能。
- 🛠 **开发者体验**：优化类型推断，减少 TypeScript 实例化次数，提升编译速度。
- 🌍 **国际化支持**：新增 locales API，支持多语言错误消息。
- 🔄 **兼容性**：Zod 4 与 Zod 3 并行发布，便于逐步迁移。

---

### [发布 v1.3.0 · unnoq/orpc · GitHub](https://github.com/unnoq/orpc/releases/tag/v1.3.0)

**原文标题**: [Release v1.3.0 · unnoq/orpc · GitHub](https://github.com/unnoq/orpc/releases/tag/v1.3.0)

oRPC 发布了 v1.3.0 版本，新增多项功能与改进，包括消息端口适配器、NestJS 集成、多成功响应支持等，并修复了一些错误。

- 🚀 **消息端口适配器** - 支持窗口、标签页、进程间的通信，提供 Electron、浏览器扩展和 Worker Threads 的集成指南。  
- 🏗 **NestJS 集成** - 可直接在 NestJS 控制器中实现 oRPC 合约。  
- 📊 **多成功响应支持** - 使用 `detailed` 结构定义多个成功响应状态。  
- 🔄 **TanStack 流式查询支持** - 新增 `.streamedOptions` 方法，支持在 TanStack Query 中使用 oRPC 事件迭代器。  
- 🛠 **实用工具新增** - 提供 `parseFormData` 和 `getIssueMessage` 工具函数，简化表单数据处理。  
- 🐞 **错误修复** - 包括依赖更新、查询兼容性改进和空 body 解析行为统一。  
- 👥 **贡献者** - 由 greg-schrammel 和 unnoq 共同完成。  
- 🎉 **社区反响热烈** - 获得大量表情符号互动（火箭、点赞、庆祝等）。

---

### [GitHub - jellydn/next-validations: NextJS API 验证工具，支持 Zod、Yup、Fastest-Validator、Joi 等](https://github.com/jellydn/next-validations)

**原文标题**: [GitHub - jellydn/next-validations: NextJS API Validations,  support Zod, Yup, Fastest-Validator, Joi, and more](https://github.com/jellydn/next-validations)

next-validations 是一个支持多种验证库的 NextJS API 验证工具，兼容 Zod、Yup、Fastest-Validator、Joi 等，提供灵活的验证模式和 TypeScript 集成。

- 🏠 **项目主页**: [next-validations.productsway.com/](https://next-validations.productsway.com/)  
- ✨ **功能亮点**: 支持多种验证库（Zod、Yup、Joi 等），集成 TypeSchema 实现通用适配  
- 📦 **安装**: `yarn add next-validations`  
- 🔧 **使用示例**: 支持查询参数（query）、请求体（body）等多模式验证  
- 🧪 **测试**: 运行 `yarn test` 进行测试  
- 👤 **作者**: Dung Huynh ([@jellydn](https://github.com/jellydn))  
- ⭐ **支持项目**: 如果觉得有用，可以给个 Star 支持  
- 📜 **许可证**: MIT  
- 🌍 **社区**: 欢迎贡献，遵循 all-contributors 规范

---

### [React 并发渲染的故事 - YouTube](https://www.youtube.com/watch?v=edN42P_vfCI)

**原文标题**: [The Story of Concurrent Rendering in React - YouTube](https://www.youtube.com/watch?v=edN42P_vfCI)

这是一个关于 YouTube 网站相关服务和政策链接的列表。  

- 📢 プレスルーム - 媒体和新闻相关信息的官方发布渠道  
- ©️ 著作権 - 版权信息和相关保护政策  
- 📩 お問い合わせ - 用户联系与客服支持  
- 🎨 クリエイター向け - 面向内容创作者的工具和资源  
- 💰 広告掲載 - 广告投放和商业合作信息  
- 💻 開発者向け - 开发者工具和 API 支持  
- 📜 利用規約 - 平台使用条款和条件  
- 🔒 プライバシー - 用户隐私保护政策  
- ⚖️ ポリシーとセキュリティ - 平台政策与安全措施  
- ⚙️ YouTube の仕組み - YouTube 的运作机制说明  
- 🆕 新機能を試してみる - 尝试平台新推出的功能  
- ®️ © 2025 Google LLC - 版权归属和年份声明

---

### [VS Code：开源 AI 编辑器](https://code.visualstudio.com/blogs/2025/05/19/openSourceAIEditor)

**原文标题**: [VS Code: Open Source AI Editor](https://code.visualstudio.com/blogs/2025/05/19/openSourceAIEditor)

VS Code 团队宣布将开源 GitHub Copilot Chat 扩展的代码，并逐步将其 AI 功能整合到 VS Code 核心中，以推动其成为开源 AI 编辑器。此举旨在保持透明性、促进社区协作，并适应 AI 开发工具的快速发展。

- 🚀 VS Code 宣布开源 GitHub Copilot Chat 扩展代码，并逐步将 AI 功能整合到核心中  
- 🔓 坚持开源原则：开放、协作、社区驱动，确保 AI 工具透明可信  
- 🤖 开源动机：大语言模型进步、通用 AI 交互模式成熟、开源生态兴起  
- 🔍 提升透明度：开源后用户可查看数据收集情况，减少隐私担忧  
- 🛡️ 安全增强：社区协作有助于快速发现并修复 AI 工具的安全漏洞  
- 🛠️ 后续计划：重构 AI 功能至核心，开源提示测试基础设施，简化社区贡献流程  
- 🌐 社区参与：通过迭代计划和 FAQ 保持沟通，邀请用户共同构建开源 AI 编辑器

---

### [CSS 变换](https://emilkowal.ski/ui/css-transforms)

**原文标题**: [CSS Transforms](https://emilkowal.ski/ui/css-transforms)

概述总结  
CSS 的`transform`属性是网页动画的基础，广泛应用于各种库和实际项目中。本文详细介绍了`transform`的几种核心功能及其应用场景，包括平移、缩放、旋转和 3D 变换，并通过实际案例展示了如何利用这些功能创建流畅的动画效果。  

- 🚀 **CSS Transform 基础**：`transform`属性是网页动画的核心，被广泛应用于 Sonner、Motion 等库。  
- 📏 **平移（Translation）**：`translate()`函数通过 X/Y 轴移动元素，百分比值基于元素自身尺寸，不影响文档流。  
- 🔄 **百分比动画优势**：`translateY(-100%)`确保元素按自身高度移动，适用于高度不固定的场景（如 Sonner 的 Toast）。  
- 🎯 **缩放（Scale）**：`scale()`按倍数调整元素大小，默认同时缩放子元素，适合按钮点击效果或 iOS 卡片动画。  
- ⚠️ **缩放动画技巧**：避免从`scale(0)`开始，结合`opacity`提升视觉效果（如 Clerk 的 Toast）。  
- 🔄 **旋转（Rotate）**：`rotate()`实现元素旋转，`rotateX/Y()`结合 3D 设置可创建立体效果（如 Aave 的硬币动画）。  
- 📍 **变换原点（Transform Origin）**：通过调整锚点（默认中心）控制动画行为，支持原点感知动画。  
- 💡 **实战案例**：Sonner 库利用`translateY()`按 Toast 索引定位；Vaul 抽屉动画依赖百分比隐藏。  
- 🛠️ **学习建议**：通过逆向工程（如 Aave 动画）深入理解`transform`的 3D 应用。  
- 📚 **延伸学习**：推荐作者动画课程，包含交互示例和练习以巩固知识。  

（注：原文中的代码示例和部分交互描述已简化为关键点，完整实现可参考原文或课程。）

---

### [Vercel Blob 现已全面开放：高性价比、持久耐用的存储方案 - Vercel](https://vercel.com/blog/vercel-blob-now-generally-available)

**原文标题**: [Vercel Blob is now generally available: Cost-efficient, durable storage - Vercel](https://vercel.com/blog/vercel-blob-now-generally-available)

Vercel Blob 现已正式发布，提供与 Vercel 应用交付网络深度集成的持久存储解决方案，支持高性能、低成本的大规模文件存储与分发。

- 🚀 **正式发布**：Vercel Blob 已全面开放，存储并服务超过 4 亿文件，应用于 v0 和 Vercel Dashboard 等生产环境。  
- 🌍 **全球高性能存储**：基于 AWS S3 基础设施，提供 99.999999999% 的可靠性，支持从少量文件到 TB 级媒体内容的高负载。  
- 💡 **智能数据传输策略**：  
  - **Blob Data Transfer**：针对大容量优化的低成本分发（18 个枢纽）。  
  - **Fast Data Transfer**：低延迟优先（覆盖 94 个城市）。  
- 🔄 **无缝缓存集成**：自动与 Vercel CDN 协作，请求优先从缓存响应，未命中时通过 Fast Origin Transfer 获取并缓存。  
- 📁 **简易开发集成**：  
  - 通过 `@vercel/blob` SDK 实现一键上传（支持 5TB 大文件、分片上传和进度跟踪）。  
  - 文件路径标准化，支持 Next.js 等框架的图片优化（如自动调整尺寸/格式）。  
- 💰 **透明定价**：  
  - 免费层含 1GB 存储/10GB 流量，按需付费与 S3 价格一致，Blob Data Transfer 成本平均低至 Fast Data Transfer 的 1/3。  
- 📊 **新增可观测性**：控制台提供存储用量、API 操作及缓存命中率等数据分析，支持按区域/用户代理细分。  
- 🔜 **未来计划**：即将推出私有 Blob 授权访问、数据驻留控制及本地开发工具增强。  

Vercel Blob 专为现代 Web 应用设计，兼顾速度、成本与易用性，适合用户生成内容、媒体资产等场景。

---

