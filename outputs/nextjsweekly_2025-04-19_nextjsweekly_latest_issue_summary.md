### ["JSX 跨网络传输 —— overreacted"](https://overreacted.io/jsx-over-the-wire/)

**原文标题**: [JSX Over The Wire — overreacted](https://overreacted.io/jsx-over-the-wire/)

本文探讨了如何通过 JSX Over The Wire（即 React Server Components）来解决前端与后端数据交互的复杂性问题。以下是关键点总结：

- 🚀 **问题背景**：传统 REST API 在应对 UI 需求变化时难以维护，数据形状与 UI 需求不匹配。
- 🔄 **解决方案**：引入 Backend for Frontend (BFF) 层，将数据组装逻辑靠近 UI 需求，减少客户端请求次数。
- 🧩 **组件化数据加载**：将数据加载逻辑封装为可复用的 ViewModel 函数，与 UI 组件一一对应。
- 🌐 **跨平台能力**：通过 JSON 传递 UI 结构，支持 Web 和原生平台，类似 Server-Driven UI (SDUI) 模式。
- ⚡ **单次往返**：通过异步组件树解析，确保整个页面的数据在单次请求中完成加载。
- 🔗 **直接连接**：Server Components 与 Client Components 通过 Props 直接绑定，数据流清晰可追溯。
- 🛠️ **技术实现**：React Server Components 作为最终方案，融合了 ViewModel 和 Async XHP 的思想，支持富交互性。  

最终代码展示了如何将路由、数据加载和 UI 渲染统一为组件树，实现高效的数据流管理。

---

### ["React 服务器组件中的 Toast 消息"](https://buildui.com/posts/toast-messages-in-react-server-components)

**原文标题**: [Toast messages in React Server Components](https://buildui.com/posts/toast-messages-in-react-server-components)

本文介绍了如何在 Next.js 应用中利用 React Server Components 实现 Toast 消息系统，结合 Server Actions、Cookies 和 Sonner 库，实现跨页面/重定向的持久化提示。

- 🚀 **核心目标**：通过 Server Components 构建基于 Cookie 的 Toast 系统，支持服务端触发（如`toast("保存成功")`）
- 🛠️ **实现步骤**  
  - 1️⃣ 初始化 Next.js 应用并创建博客表单  
  - 2️⃣ 用 Cookie 存储 Toast（随机 ID 防覆盖）  
  - 3️⃣ 服务端组件`<Toaster />`读取 Cookie 渲染消息  
  - 4️⃣ 通过 Server Action 删除 Cookie 实现消息关闭  
  - 5️⃣ 用`useOptimistic`解决延迟问题（客户端即时更新）  
  - 6️⃣ 集成 Sonner 库美化 Toast 界面  
- 🔥 **技术亮点**  
  - 混合服务端/客户端状态管理  
  - `startTransition`处理乐观更新  
  - Cookie 实现跨页面/重定向持久化  
- ⚠️ **设计权衡**：选择服务端操作而非`document.cookie`的优缺点分析  
- 📦 **扩展应用**：该模式已用于开源框架 Twofold 的 Flash 消息系统

---

### [市政认证 | 无缝用户管理](https://www.civic.com/auth?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=civicauth-20250418)

**原文标题**: [Civic Auth | Seamless user management](https://www.civic.com/auth?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=civicauth-20250418)

概述总结  
Civic 提供无缝用户管理和数字身份解决方案，支持快速集成和多种登录方式，简化 Web2 和 Web3 的认证流程。  

- 🔐 **Civic Auth** - 提供免费计划，支持 5 分钟内实现无密码认证，无需复杂后端。  
- 🆔 **Civic Pass** - 可信数字身份解决方案，免费计划可用。  
- 🛠️ **快速集成** - 通过几行代码即可部署，支持多种框架。  
- 🔗 **多登录选项** - 集成 Google、X、Facebook 等社交登录和 Web3 钱包功能。  
- 🎮 **案例研究** - 如 Passport XYZ 和 Honeyland，展示 Civic 在提升 Web3 声誉和游戏完整性中的应用。  
- 🖥️ **拖拽式 UI 编辑器** - 自定义认证流程，无需额外代码。  
- 🔄 **三步入门** - 安装 SDK、获取客户端 ID、集成到应用。  
- 🔒 **用户数据控制** - 基于区块链，减少数据泄露风险，支持生物识别登录。  
- 📅 **免费演示** - 提供产品更新信息，可随时退订。  
- ⚖️ **法律与资源** - 包含隐私政策、帮助中心和法律披露等。

---

### ["View Transition API 及其在 NextJS 中的集成 - Agence Premier Octet"](https://www.premieroctet.com/blog/en/view-transition-api-in-next-js-and-react)

**原文标题**: [View Transition API and its Integration in NextJS - Agence Premier Octet](https://www.premieroctet.com/blog/en/view-transition-api-in-next-js-and-react)

View Transition API 是一项原生浏览器功能，允许无需依赖第三方库即可实现页面状态变化的动画效果。Next.js 已实验性集成此功能，尽管目前仍处于测试阶段且文档较少，但它为简化复杂动画提供了可能。  

- 🌐 **View Transition API 简介**：原生浏览器功能，无需依赖如 Framer Motion 或 GSAP 等第三方库即可实现页面状态变化的动画效果。  
- 🛠️ **核心方法**：通过 `startViewTransition` 方法触发视图过渡周期，捕获页面状态变化前后的 DOM 状态。  
- 🎨 **自定义过渡**：使用 CSS 伪选择器 `::view-transition...` 自定义动画效果，例如淡入淡出或其他复杂动画。  
- 🔍 **目标元素**：通过为元素分配 `view-transition-name`，可以针对特定元素应用过渡效果。  
- 📂 **两种过渡类型**：同一文档内的过渡和多文档（页面切换）过渡，后者由导航触发，无需调用 `startViewTransition`。  
- ⚙️ **Next.js 集成**：需在 `next.config.js` 中启用实验性标志 `viewTransition`，并使用 React 的 `unstable_viewTransition` 组件。  
- 🚧 **实验性阶段**：Next.js 的集成仍处于测试阶段，API 可能发生变化，文档较少。  
- 🎭 **演示示例**：通过多文档视图过渡实现页面切换动画，展示了简单的实现方式。  
- 🔮 **未来展望**：未来可能支持预定义的页面过渡配置，但目前功能尚未完全成熟。  
- ✨ **创意用例**：一些网站展示了 View Transition API 的创造性应用，如平滑过渡和动态效果。  
- 📚 **资源推荐**：MDN 文档、W3C 规范和相关文章可供进一步学习。

---

### ["React Query 内部揭秘：深入探索其工作机制 | 作者：Rohith Janardhan | 2025 年 4 月 | Medium"](https://medium.com/@janardhan.roh/under-the-hood-of-react-query-a-deep-dive-into-its-internal-mechanics-ee51c0ce076e)

**原文标题**: [Under the Hood of React Query: A Deep Dive into Its Internal Mechanics | by Rohith Janardhan | Apr, 2025 | Medium](https://medium.com/@janardhan.roh/under-the-hood-of-react-query-a-deep-dive-into-its-internal-mechanics-ee51c0ce076e)

React Query 是一个流行的 React 库，用于管理服务器状态，其内部机制基于观察者模式，通过缓存和状态管理优化数据获取和组件更新。

- 🚀 **核心模式**：采用观察者（发布 - 订阅）模式，允许多个组件订阅查询状态变化。
- 🔍 **查询结构**：查询对象包含状态和 Promise，通过 `subscribe` 和 `setState` 方法管理订阅和状态更新。
- ⚛️ **useQuery 钩子**：通过 `QueryClientContext` 获取查询客户端，使用 `createQueryObserver` 创建观察者并订阅重新渲染。
- 🔄 **查询触发**：仅在 `staleTime` 过期后触发查询，避免不必要的请求。
- 🏗️ **QueryClient**：管理应用中的查询，防止重复创建，并提供查询失效等功能。
- 🛠️ **查询获取**：通过 `fetch` 方法实现请求去重，确保并发请求只触发一次。
- 🗑️ **垃圾回收**：在 `cacheTime` 后自动清理未使用的查询，优化内存使用。
- 🔍 **窗口聚焦重新获取**：通过监听窗口聚焦事件，自动刷新数据以保持 UI 最新。
- 🎯 **开发者友好**：提供调试工具和灵活的配置选项，如 `staleTime` 和 `cacheTime`，便于优化性能。

---

### ["将 Grep 从 Create React App 迁移至 Next.js - Vercel"](https://vercel.com/blog/migrating-grep-from-create-react-app-to-next-js)

**原文标题**: [Migrating Grep from Create React App to Next.js - Vercel](https://vercel.com/blog/migrating-grep-from-create-react-app-to-next-js)

Grep 是一个极速代码搜索工具，能够在上百万个代码库中快速查找特定代码片段、文件或路径，搜索结果即时呈现，无需等待加载动画。最初基于 Create React App (CRA) 构建为客户端渲染的单页应用 (SPA)，随着 CRA 的弃用，团队决定迁移至 Next.js，以提升性能和可维护性，同时保留 SPA 的交互体验。

- 🚀 **极速搜索体验**：Grep 支持即时搜索，用户输入时无缝过渡到搜索结果页，保持输入焦点不丢失。
- 🔄 **从 CRA 迁移到 Next.js**：为了提升性能和可维护性，团队将 Grep 从 CRA 迁移至 Next.js，利用 React Server Components 优化加载速度。
- ⚡ **Next.js 的优势**：Next.js 通过预渲染和智能预加载，实现了快速的初始页面加载和页面间导航，同时减少了客户端 JavaScript 的负担。
- 🔍 **保留即时搜索体验**：通过条件渲染和共享状态，确保搜索输入在页面导航时保持一致，避免布局偏移和闪烁。
- 🔗 **状态同步**：通过 URL 参数和轻量级状态管理，保持搜索输入状态在多个页面间的同步。
- 📡 **服务器优先的数据获取**：使用 TanStack Query 和 SWR 在服务器端预取数据，然后在客户端继续查询，确保快速初始加载和实时搜索体验。
- 🔄 **客户端增量获取**：通过 `useDeferredValue` 和 `useSuspenseQuery` 实现客户端增量数据获取，避免不必要的网络请求。
- 🛠️ **防止过时结果**：结合 `useOptimistic` 和 TanStack Query 的缓存机制，确保 UI 始终反映最新的用户输入，避免过时或乱序结果。
- 📱 **移动端优化**：通过 `usePreventScroll` 钩子解决移动端 Safari 的滚动和缩放问题，保持搜索体验稳定。
- 🚀 **部分预渲染 (PPR)**：启用 Next.js 的实验性 PPR 功能，进一步提升了初始加载速度和交互性。
- 📊 **性能提升**：迁移至 Next.js 后，各项性能指标显著提升，包括首次内容绘制 (FCP)、最大内容绘制 (LCP) 等。
- 🔮 **未来计划**：探索私有代码库索引和高级查询语法支持，进一步提升 Grep 的功能和用户体验。

---

### [2025 年 React 趋势](https://www.robinwieruch.de/react-trends/)

**原文标题**: [React Trends in 2025](https://www.robinwieruch.de/react-trends/)

2025 年 React 生态将迎来重大变革，聚焦服务端组件、全栈能力与工具链升级，同时面临框架竞争与 AI 融合的新机遇。

- 🚀 **React 服务端组件（RSC）成为标准**  
  2025 年 RSC 将普及为 React 核心特性，Next.js、React Router 等框架全面支持，实现服务端渲染与客户端交互的无缝结合。

- 🔄 **React 服务端函数（RSF）统一数据操作**  
  整合数据获取（RSC）与变更（RSA），简化全栈开发流程，无需手动定义 API 路由。

- 📝 **React 19 表单强化**  
  新增`action`属性直接绑定服务端动作，配合`useFormStatus`等 Hook 提升表单处理效率。

- ⚖️ **框架选择复杂度增加**  
  Next.js 主导，但 TanStack Start 和 React Router（原 Remix）崛起，形成三足鼎立竞争格局。

- 🌐 **全栈 React 成为主流**  
  服务端能力扩展至数据库直连、身份验证等后端领域，推动 React 向一体化应用框架演进。

- 🎨 **UI 设计趋同化（Shadcn 风格）**  
  Shadcn UI 成为默认选择，但同质化可能催生新设计范式。

- 🤖 **AI 深度集成**  
  React 代码被广泛用于 AI 训练，同时 AI 工具（如 Vercel AI SDK）反哺 React 开发生态。

- ⚡ **工具链革新**  
  Biome 替代 ESLint+Prettier 趋势明显，提供更快的 Rust 工具链方案。

- 🔧 **React 编译器（自动优化）**  
   Beta 版编译器将自动处理`useMemo`等性能优化，减少手动干预。

- 📂 **组件命名规范优化**  
  社区有望推动更清晰的文件命名约定以提升可维护性。

---

### [Firebase 工作室](https://firebase.studio/)

**原文标题**: [Firebase Studio](https://firebase.studio/)

Firebase Studio 是一个全栈 AI 工作空间，通过 AI 代理加速整个开发生命周期，支持后端、前端和移动应用的构建。

- 🚀 **快速开发**：从浏览器打开到构建仅需几分钟，支持从 GitHub 等平台导入现有仓库或使用自然语言快速创建新应用。  
- 🛠️ **AI 驱动**：集成 Gemini AI 辅助编码、调试、测试和文档生成，并提供自定义模型选项。  
- 📱 **跨平台测试**：通过 Open VSX Registry 扩展和内置模拟器，实时预览和优化 API 及多平台应用。  
- 🚀 **一键部署**：支持 Firebase Hosting、Cloud Run 等部署方式，并提供应用监控功能。  
- 🆓 **免费预览**：预览期间免费提供 3 个工作空间，Google 开发者计划成员可享最多 30 个。  
- 🌟 **持续创新**：Firebase 结合生成式 AI，助力开发者构建 API、后端及移动应用等。  
- 🔗 **资源丰富**：提供开发者指南、SDK 参考、示例代码及社区支持（博客、Reddit、YouTube 等）。

---

### ["Anime.js | JavaScript 动画引擎"](https://animejs.com/)

**原文标题**: [Anime.js | JavaScript Animation Engine](https://animejs.com/)

overview summary  
Anime.js 是一个快速且多功能的 JavaScript 动画库，提供丰富的工具和 API，支持从基础动画到复杂交互效果的创建，适用于网页动画开发。  

- 🚀 **高性能动画引擎** - 快速、灵活的 JavaScript 库，支持网页动画开发。  
- 📦 **简单安装** - 通过 `npm i animejs` 即可安装使用。  
- 🛠️ **全面动画工具** - 提供完整的动画工具箱，突破浏览器限制，支持动画任何元素。  
- 🎛️ **直观 API** - 易于使用但功能强大的动画 API，支持逐属性参数和灵活的关键帧系统。  
- 🔄 **增强变换** - 通过组合 API 平滑混合独立的 CSS 变换属性。  
- 📐 **SVG 工具集** - 支持形状变形、路径跟随和线条绘制等 SVG 动画功能。  
- 📜 **滚动观察器** - 通过 Scroll Observer API 在滚动时同步和触发动画。  
- ⏱️ **高级错开效果** - 内置 Stagger 工具，快速创建时间、数值和位置错开效果。  
- 🖱️ **拖拽和弹簧效果** - 提供功能齐全的 Draggable API，支持拖拽、捕捉、轻弹和投掷效果。  
- ⏳ **时间线控制** - 通过 Timeline API 编排动画序列并保持回调同步。  
- 📱 **响应式动画** - 使用 Scope API 轻松响应媒体查询，适配不同设备。  
- 📦 **轻量模块化** - 按需导入功能，保持代码体积小巧，最小仅需 5.6KB。  
- ❤️ **免费开源** - 由赞助商支持，完全免费，提供详细文档和示例。  
- 🔗 **社区与资源** - 支持通过 GitHub、CodePen 等平台探索，提供社交媒体关注选项。

---

### ["Zod 4 测试版发布 | Zod 文档"](https://v4.zod.dev/v4)

**原文标题**: [Introducing Zod 4 beta | Zod Docs](https://v4.zod.dev/v4)

Zod 4 beta 版本发布，带来性能提升、新功能和架构改进，包括更快的解析速度、更小的包体积、元数据支持和 JSON Schema 转换等。

- 🚀 **性能提升**：Zod 4 在字符串解析、数组解析和对象解析方面分别快了 2.6 倍、3 倍和 7 倍。
- 📉 **包体积优化**：核心包体积减少了 2 倍，引入 `@zod/mini` 后进一步减少了 6.6 倍。
- 🏗️ **新架构**：采用全新内部架构，解决了长期存在的设计限制，为未来功能奠定基础。
- 📝 **元数据支持**：新增元数据系统，支持为 schema 添加强类型元数据，并自动包含在 JSON Schema 输出中。
- 🔄 **JSON Schema 转换**：新增 `z.toJSONSchema()` 方法，支持将 Zod schema 转换为 JSON Schema。
- 🛠️ **新 API**：引入 `z.interface()` 以更精确地表示可选属性，支持递归类型定义。
- 🌍 **国际化**：新增 `locales` API，支持全局翻译错误消息。
- ✨ **错误美化**：新增 `z.prettifyError` 方法，将 `ZodError` 转换为用户友好的格式化字符串。
- 📂 **文件验证**：新增 `z.file()` 方法，支持验证 `File` 实例。
- 🔢 **数字和字符串格式**：新增多种数字格式和字符串格式验证，如 `z.int()`、`z.email()` 等。
- 🔄 **简化错误定制**：统一 `error` 参数，简化错误消息定制。
- 🔗 **改进联合类型**：`z.discriminatedUnion()` 不再需要显式指定判别键，支持组合使用。
- 🔄 **覆盖方法**：新增 `.overwrite()` 方法，支持不改变推断类型的转换。
- 🏗️ **可扩展基础**：引入 `@zod/core` 包，为其他库提供快速验证基础。

Zod 4 将在 6 周的测试期内持续优化，鼓励用户升级并提供反馈。

---

### [WebTUI](https://webtui.ironclad.sh/)

**原文标题**: [WebTUI](https://webtui.ironclad.sh/)

WebTUI 是一个模块化的 CSS 库，旨在将终端用户界面（TUI）的美学带入浏览器。它提供了丰富的组件、插件和主题支持，帮助开发者快速构建具有终端风格的网页界面。

- 🖥️ **核心特性**：模块化设计，支持终端风格的 UI 组件，如按钮、输入框、徽章等。  
- 📦 **组件库**：包含复选框、弹出框、输入框、徽章、按钮、排版等多种组件，每个组件都有详细的导入和使用说明。  
- 🎨 **主题支持**：提供多种主题插件，如 Nord、Catppuccin 和 Gruvbox，支持自定义 CSS 变量和深色/浅色模式。  
- 🔌 **插件系统**：支持开发自定义插件，包括主题插件和功能插件（如 Nerd Font 插件）。  
- 📝 **文档丰富**：包含风格指南、插件开发指南、主题定制指南等，帮助开发者快速上手。  
- 🛠️ **安装灵活**：支持通过 ESM、CDN 或完整库导入，满足不同开发需求。  
- ✨ **特色功能**：ASCII 边框、排版组件、终端风格的 UI 设计等。

---

### [2025 年 4 月 11 日发布——React Spectrum 版本更新](https://react-spectrum.adobe.com/releases/2025-04-11.html)

**原文标题**: [April 11, 2025 Release â React Spectrum Releases](https://react-spectrum.adobe.com/releases/2025-04-11.html)

2025 年 4 月 11 日发布的 React Spectrum 更新，主要新增自定义日历支持、集合性能优化、生产包体积缩减及跨平台事件别名处理等改进。

- 📅 新增自定义日历支持，可扩展或从头实现业务逻辑（如 4-5-4 财年日历）  
- 🚀 集合组件增强：支持 React Suspense 并优化大型数据集渲染性能  
- 📦 生产包体积缩减（如@react-aria/interactions 减小 22%）  
- 🖱️ 将`onClick`作为`onPress`别名以提升跨库兼容性（仍推荐使用`onPress`）  
- 🛠️ 多项修复：日期选择器 CSS 选择器、表格行文本值处理等  
- 📚 文档更新与错误修正  
- 🏗️ 新增 Toast PortalProvider 配置功能（开发中）  
- 📦 发布多包版本更新（包括@adobe/react-spectrum@3.41.0 等）

---

### ["UI 组件 | Tiptap"](https://tiptap.dev/docs/ui-components/getting-started/overview)

**原文标题**: [UI Components | Tiptap](https://tiptap.dev/docs/ui-components/getting-started/overview)

Tiptap 提供模块化的 UI 组件库，支持快速集成与深度定制，涵盖开源和付费功能，设计简洁且易于扩展。

- 🧩 Tiptap UI 组件库提供预构建界面，支持即插即用或自定义开发  
- 🚀 提供快速启动模板和按需组件集成，适配现有 Tiptap 项目  
- 📜 开源组件遵循 MIT 协议（如 Bold/Heading/Image），付费组件需订阅 Tiptap Cloud 服务  
- 🎨 组件设计风格中性，支持无缝品牌定制，无需复杂样式覆盖  
- 🔧 包含三类构建块：功能组件（如 HeadingDropdownMenu）、节点组件和基础元素（Button/DropdownMenu 等）  
- ⚛️ 组件依赖对应 Tiptap 扩展，通过 React 钩子与编辑器状态联动  
- ✂️ 底层 Primitives 提供可访问性支持，支持自由组合创建自定义控件  
- 🌩 付费云功能组件（如评论/版本历史）将逐步推出，需后端服务支持

---

### ["2025 年人工智能发展报告"](https://2025.stateofai.dev/en-US/)

**原文标题**: [State of AI 2025](https://2025.stateofai.dev/en-US/)

AI 在开发中的应用现状及开发者调查概述  

- 🛌 小憩是否有助于缓解时差问题？  
- 🔧 应该购买哪种焊接工具？  
- 🍽️ 今晚去哪里吃饭？  
- 🤖 越来越多的人开始依赖 AI 解决日常问题，甚至包括编写代码。  
- ⌨️ 开发者们对于 AI 是否已准备好接管编码工作持有不同意见。  
- 📱 社交媒体上许多开发者分享他们如何轻松利用 AI 快速完成应用开发。  
- 💰 调查涉及开发者使用 AI 的花费、最有用的工具以及主要痛点。  
- 📊 首次《Web 开发 AI 现状》调查旨在全面了解 AI 在开发中的应用情况。  
- 🎯 调查还涵盖了那些对 AI 持保留态度的开发者，以呈现更全面的生态现状。  
- 📧 提供订阅选项，以便及时获取下一次调查的通知。  
- 🤝 感谢合作伙伴的支持，包括 Postgres、Google Chrome 团队等。  
- 🌍 提供多语言翻译支持，涵盖西班牙语、日语、韩语、中文等多种语言。

---

### ["您的前端、后端和数据库——现集成于一个 Cloudflare Worker 中"](https://blog.cloudflare.com/full-stack-development-on-cloudflare-workers/)

**原文标题**: [Your frontend, backend, and database â now in one Cloudflare Worker](https://blog.cloudflare.com/full-stack-development-on-cloudflare-workers/)

Cloudflare Workers 现在集成了前端、后端和数据库功能，支持全栈应用开发，并宣布了十项重大改进，包括框架支持、静态资源托管、数据库连接、Node.js API 兼容性等。

- 🚀 **全栈框架支持**：Cloudflare Workers 现已正式支持 React Router v7 (Remix)、Astro、Hono、Vue.js、Nuxt、Svelte (SvelteKit) 等框架，Next.js、Angular 和 SolidJS (SolidStart) 的支持将在 2025 年第二季度推出。
- ⚡ **Vite 集成**：Cloudflare Vite 插件现已正式发布，支持在 Workers 运行时中使用 Vite 的开发服务器，包括热模块替换（HMR）功能。
- 📂 **静态资源配置**：现在可以在 Workers 中使用 `_headers` 和 `_redirects` 配置文件，无需执行 Worker 代码即可配置简单的头部和重定向。
- 🗃️ **数据库连接**：除了 PostgreSQL，Workers 现在还可以通过 Hyperdrive 连接 MySQL 数据库，支持 Planetscale、AWS、GCP、Azure 等现有数据库。
- 🔧 **Node.js API 支持**：Workers 运行时现在支持更多 Node.js API，包括 `crypto`、`tls`、`net` 和 `dns` 模块，同时将单个请求的最大 CPU 时间从 30 秒增加到 5 分钟。
- 🔗 **Git 仓库集成**：现在可以直接从 GitHub 或 GitLab 导入包含 Worker 应用的仓库，Workers Builds 会自动将其部署为新的 Worker。
- ⏱️ **构建性能提升**：Workers Builds 的启动时间缩短了 6 秒，现在平均在 10 秒内启动，同时支持在非生产分支上运行构建，并将预览 URL 以评论形式发布到 GitHub。
- 🖼️ **图像处理 API**：Images 绑定现已正式可用，支持更灵活的编程式图像优化工作流。
- 🔄 **迁移指南**：提供了从 Cloudflare Pages 迁移到 Workers 的详细指南，帮助开发者平滑过渡。
- 📊 **全栈应用架构**：Workers 支持静态站点、单页应用（SPA）和服务器端渲染（SSR）等多种架构，开发者可以根据需求选择合适的渲染模式。

---

### [《Prisma ORM 6.6.0：ESM 支持、D1 迁移与 Prisma MCP 服务器》](https://www.prisma.io/blog/prisma-orm-6-6-0-esm-support-d1-migrations-and-prisma-mcp-server)

**原文标题**: [Prisma ORM 6.6.0: ESM Support, D1 Migrations & Prisma MCP Server](https://www.prisma.io/blog/prisma-orm-6-6-0-esm-support-d1-migrations-and-prisma-mcp-server)

Prisma ORM v6.6.0 发布，带来 ESM 支持、D1/Turso 迁移支持、MCP 服务器等多项新功能，优化开发者体验并增强与 AI 工具的集成。

- 🚀 Prisma ORM v6.6.0 发布，包含 ESM 支持、D1/Turso 迁移支持和 MCP 服务器等新功能  
- 🔄 新的`prisma-client`生成器支持 ESM 和 CommonJS，提供更灵活的项目配置  
- 🛠️ 生成器支持自定义输出路径、文件扩展名等，优化项目工作流  
- 🤖 MCP 服务器支持通过 AI 工具管理 Prisma Postgres，包括创建实例、设计数据模型等  
- ☁️ 新增对 Cloudflare D1 和 Turso/LibSQL 的迁移支持（早期访问）  
- 📝 `prisma init`新增`--prompt`选项，可快速搭建 Prisma 架构并部署  
- 🛣️ 未来计划包括拆分生成文件、优化编辑器性能等，详情见 3 个月路线图  
- 📢 用户可通过 X 和 Discord 反馈意见，关注更新动态

---

### ["React Query API 设计：经验分享 - Dominik Dorfmeister - YouTube"](https://www.youtube.com/watch?v=l3PxErcKeAI)

**原文标题**: [React Query API Design: Lessons Learned - Dominik Dorfmeister - YouTube](https://www.youtube.com/watch?v=l3PxErcKeAI)

YouTube 平台相关信息概览  

- 📜 簡介  
- 📺 媒體  
- ©️ 著作權  
- 📩 與我們聯絡  
- 🎨 創作者  
- 📢 廣告  
- 💻 開發人員  
- 📑 條款  
- 🔒 隱私權  
- ⚖️ 政策與安全性  
- ⚙️ YouTube 運作方式  
- 🧪 測試新功能  
- 🏛️ © 2025 Google LLC

---

### ["难以置信的优惠：订阅 Lenny's Newsletter 年费，立即免费获得 v0、Replit、Lovable 和 Bolt 专业版一年使用权"](https://www.lennysnewsletter.com/p/an-unbelievable-offer-now-get-one)

**原文标题**: [An unbelievable offer: Now get one free year of v0, Replit, Lovable, and Bolt pro plans with an annual subscription to Lenny’s Newsletter](https://www.lennysnewsletter.com/p/an-unbelievable-offer-now-get-one)

Lenny's Newsletter 推出了一项超值年度订阅优惠，订阅者可免费获得多款热门 AI 工具及生产力平台的一年高级会员服务，总价值超过 15,000 美元。

- 💥 年度订阅用户可免费获得 10 款产品的一年使用权，包括 v0、Replit、Lovable 等热门 AI 工具  
- 🎁 新增 5 款 AI 工具加入原有捆绑包（含 Linear、Notion 等知名平台）  
- 💰 单件产品价值已超订阅费（年费$120），使用任意一款即可回本  
- 📅 免费权益激活时间以兑换代码为准，非订阅购买时间  
- ⚠️ 仅限新付费用户使用，且需年度订阅（月费用户不适用）  
- 🔄 现有年费用户可立即兑换，月费用户需升级后领取  
- 🛑 若中途退款，所有代码将失效（无论是否已激活）  
- 📧 包含团队协作工具（如 Notion 团队版、Granola 100 席位等）  
- ⏳ 优惠可能随时终止，部分产品会因代码售罄移除  
- ✉️ 兑换后享附加权益：完整文章库+Slack 社区 + 线下活动邀请

---

