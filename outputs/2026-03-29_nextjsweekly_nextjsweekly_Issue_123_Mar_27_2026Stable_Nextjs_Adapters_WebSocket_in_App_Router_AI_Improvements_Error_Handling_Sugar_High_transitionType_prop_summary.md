### [Next.js 跨平台适配：适配器、OpenNext 与我们的承诺 | Next.js](https://nextjs.org/blog/nextjs-across-platforms)

**原文标题**: [Next.js Across Platforms: Adapters, OpenNext, and Our Commitments | Next.js](https://nextjs.org/blog/nextjs-across-platforms)

Next.js 16.2 推出了稳定的 Adapter API，通过与 OpenNext 及多家云平台合作，确保 Next.js 能在所有平台上良好运行。这一举措旨在为开发者提供统一的部署标准，并承诺通过公开测试套件和开源适配器来保障跨平台的兼容性和可靠性。

- 🔌 **Adapter API（稳定版）**：提供类型化、版本化的应用描述，供任何平台对接。
- 🧪 **测试套件**：为所有适配器（包括 Vercel）提供共享的正确性测试。
- ✅ **已验证适配器**：由社区维护的开源适配器，托管在 Next.js 组织下。
- 🤝 **生态系统工作组**：设立常设论坛，协调各提供商之间的变更。
- 🌉 **OpenNext 的桥梁作用**：将 Next.js 构建输出转化为平台可用的格式，推动了官方 Adapter API 的诞生。
- 📚 **完善的文档**：重新编写了大量文档，涵盖渲染理念、平台部署指南、PPR 平台指南等。
- 🔄 **公开协作机制**：通过工作组确保提供商提前获知变更，并与社区共同设计 API。
- 🚀 **当前进展**：已发布 Vercel 和 Bun 适配器，Netlify、Cloudflare 和 AWS 适配器正在开发中。

---

### [Next.js 16.2：AI 功能优化 | Next.js](https://nextjs.org/blog/next-16-2-ai)

**原文标题**: [Next.js 16.2: AI Improvements | Next.js](https://nextjs.org/blog/next-16-2-ai)

Next.js 16.2 版本推出了多项针对 AI 辅助开发的改进，旨在让 AI 代理能更轻松地理解项目、通过终端调试问题以及检查运行中的应用，而无需依赖浏览器。

- 🤖 **AI 就绪的 create-next-app**：默认包含 `AGENTS.md` 文件，为 AI 编码代理提供版本匹配的 Next.js 文档，确保项目从一开始就具备 AI 开发能力。
- 🔄 **浏览器日志转发**：开发时默认将浏览器错误转发至终端，便于主要通过终端操作的 AI 代理进行调试，无需切换至浏览器控制台。
- 🔒 **开发服务器锁文件**：当同一项目目录中启动第二个开发服务器时，会生成包含 PID、端口和 URL 的锁文件，并提供可操作的错误信息，指导 AI 代理停止现有进程或连接至它。
- 🛠️ **实验性代理开发者工具**：通过 `@vercel/next-browser` CLI，AI 代理可以检查运行中的 Next.js 应用，获取如 React 组件树、PPR 静态外壳、错误日志、网络活动和屏幕截图等结构化数据，从而进行诊断和优化。

---

### [核心 3](https://clerk.com/changelog/2026-03-03-core-3?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=core-3&utm_content=03-27-26&dub_id=x3g9I3BPOzQzUYv4)

**原文标题**: [Core 3](https://clerk.com/changelog/2026-03-03-core-3?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=core-3&utm_content=03-27-26&dub_id=x3g9I3BPOzQzUYv4)

Clerk 发布了其 SDK 的最新主要版本 Core 3，重点改进了自定义 API、主题编辑器、无密钥模式支持、现代 React 兼容性和性能优化。

- 🛠️ **改进的自定义 API**：重新设计了`useSignIn`、`useSignUp`和`useCheckout`钩子，并新增`useWaitlist`钩子，简化了自定义身份验证界面的构建。
- 🎨 **主题编辑器与交互式文档**：新增可视化主题编辑器，可实时调整预构建组件的样式，并支持在文档中交互式预览和复制代码。
- 🔑 **扩展的无密钥模式支持**：无密钥模式现已支持 TanStack Start、Astro 和 React Router 框架，允许用户无需账户或 API 密钥即可快速体验。
- ⚛️ **现代 React 兼容性**：优化了与 React 并发功能（如过渡、Suspense 和流式 SSR）的兼容性，解决了之前可能存在的状态同步问题。
- 🚀 **性能提升**：包括更小的捆绑包体积（约节省 50KB）、卫星域名加载优化、改进的离线处理以及令牌获取的背景自动刷新。
- 📦 **其他更新**：简化了包名称（如`@clerk/clerk-react`改为`@clerk/react`），引入了统一的`<Show>`组件替代多个旧组件，并新增了自动主题匹配、Vite 环境变量检测等功能。
- ⚠️ **弃用说明**：弃用了 Clerk Elements 和`@clerk/types`包，相关功能已整合到新版 SDK 中。升级需注意 Node.js 版本要求（20.9.0+），并可使用升级 CLI 工具辅助迁移。

---

### [Next.js 错误处理与 catchError | Aurora Scharff](https://aurorascharff.no/posts/error-handling-in-nextjs-with-catch-error)

**原文标题**: [Error Handling in Next.js with catchError | Aurora Scharff](https://aurorascharff.no/posts/error-handling-in-nextjs-with-catch-error)

本文介绍了在 Next.js App Router 中处理错误的演进过程，从 react-error-boundary 的局限到官方解决方案 unstable_catchError 的推出，重点解决了服务组件错误捕获与恢复的问题。

- 🚫 react-error-boundary 在服务组件中会错误捕获 Next.js 的控制流错误（如 notFound、redirect），且恢复机制无法重新获取服务端数据
- 🔧 临时解决方案需手动检测错误摘要并配合 router.refresh() 和组件 key 重置来实现正确恢复
- 🆕 unstable_catchError 是框架感知的错误边界，能自动区分框架错误与真实错误，并提供 retry() 函数重新获取服务端数据
- 🔄 retry() 函数在组件级和路由级（error.tsx）都可用，能真正重新获取服务端数据而非仅清除客户端状态
- 🎯 新方案简化了错误处理，无需维护错误摘要白名单和手动刷新逻辑，推荐在需要组件级错误边界时使用

---

### [理解 React 中的'key'属性 | React 内部解析](https://inside-react.vercel.app/blog/making-sense-of-key-prop-in-react)

**原文标题**: [Making sense of 'key' prop in react | Inside React](https://inside-react.vercel.app/blog/making-sense-of-key-prop-in-react)

React 的 `key` 属性用于在列表渲染中为每个元素提供稳定且唯一的标识，帮助 React 在组件更新时准确识别哪些元素被移动、添加或删除，从而避免不必要的 DOM 操作和状态错乱问题。

- 🔑 **`key` 的作用**：为列表中的每个元素提供唯一标识，使 React 能正确追踪元素变化，优化渲染性能。
- ⚠️ **无 `key` 的问题**：若不提供 `key`，React 仅依赖元素位置进行对比，可能导致状态错乱（如排序后组件状态附着错误）或性能下降。
- 📍 **索引作为 `key` 的局限**：使用数组索引作为 `key` 在列表顺序不变且无内部状态时可行，但若列表顺序变化或元素含状态（如输入框），会导致状态错乱。
- 🎲 **随机值作为 `key` 的危害**：如 `Math.random()` 每次渲染生成新值，导致 React 误判为全新元素，引发整个列表重建和状态丢失。
- 🔄 **`key` 对组件的影响**：对非列表的独立组件，通常无需 `key`；但若为相同位置的组件添加不同 `key`，会触发组件重新挂载（状态重置）。
- ✅ **正确使用 `key`**：应使用稳定、唯一的标识（如数据 ID），确保在重新渲染间保持不变，以维持组件状态和提升渲染效率。

---

### [feat(server): 为 App Router 路由处理器添加 WebSocket 支持 by ethanniser · Pull Request #89320 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/89320)

**原文标题**: [feat(server): add WebSocket support for App Router route handlers by ethanniser · Pull Request #89320 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/89320)

Next.js 正在为 App Router 的路由处理器添加实验性的 WebSocket 支持，通过新的 `NextResponse.upgrade()` API 实现，该功能需在配置中启用。

- 🚀 **新增实验性 WebSocket 支持**：通过 `NextResponse.upgrade()` API 为 App Router 的路由处理器提供 WebSocket 功能，需在 `next.config.js` 中设置 `experimental.webSockets: true` 来启用。
- 🔌 **完整的 WebSocket 接口**：实现了 `NextWebSocket` 类，提供标准的 WebSocket 接口，并包含额外的 `accept()` 方法用于连接验证。
- 🛡️ **中间件集成**：中间件可以处理 WebSocket 升级请求，支持添加/修改请求头、重写路由、重定向请求或阻止连接。
- 🌐 **支持多种环境**：该功能在开发模式 (`next dev`)、生产模式 (`next start`) 和独立构建中均可工作，并支持 `ws://` 和 `wss://` 协议。
- ✅ **全面的测试覆盖**：已添加端到端测试，涵盖基本连接建立、双向消息通信、多并发连接、连接关闭处理及中间件功能等场景。

---

### [未找到标题](https://x.com/shuding/status/2035666444919468354)

**原文标题**: [No title found](https://x.com/shuding/status/2035666444919468354)

该页面提示 JavaScript 被禁用或浏览器不受支持，导致无法正常使用 X 平台的功能，并提供了相应的解决建议。

- 🚫 JavaScript 未启用，导致网站功能受限
- 🌐 建议启用 JavaScript 或更换受支持的浏览器
- 🔧 可访问帮助中心查看支持的浏览器列表
- 🛡️ 隐私相关扩展可能导致问题，建议暂时禁用
- 🔄 页面提供“重试”选项供用户再次尝试加载

---

### [未找到标题](https://x.com/asidorenko_/status/2036125973062549532)

**原文标题**: [No title found](https://x.com/asidorenko_/status/2036125973062549532)

该页面提示 JavaScript 功能未启用，导致无法正常使用 X 平台，并提供了相应的解决建议与支持信息。

- 🔧 检测到浏览器中 JavaScript 被禁用，需启用或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致问题，建议暂时禁用后重试
- 📜 页面底部包含服务条款、隐私政策及版权声明等常规信息
- 🔄 提供“再试一次”的故障恢复选项

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

TypeScript 6.0 正式发布，这是一个过渡版本，旨在为基于 Go 重写的原生编译器 TypeScript 7.0 铺平道路。本次更新包含多项新特性、改进以及为迎接 7.0 而进行的重大变更和弃用。

- 🚀 **发布与定位**：TypeScript 6.0 是当前 JavaScript 代码库的最后一个主要版本，作为 5.9 和未来的原生版本 7.0 之间的桥梁。
- 🧠 **推断优化**：对于未使用 `this` 的函数，减少了其上下文敏感性，从而改善了泛型调用中的类型推断。
- 📁 **子路径导入**：现在支持以 `#/` 开头的子路径导入（Subpath Imports），与 Node.js 新特性保持一致。
- ⚙️ **模块解析组合**：`--moduleResolution bundler` 现在可与 `--module commonjs` 组合使用，为项目升级提供更合适的路径。
- 🔢 **稳定类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 一致，便于迁移对比，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的新选项，并引入了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 4 的 Temporal API 提供了内置类型支持。
- 🗺️ **Map 新增方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法类型。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数的类型支持，用于正则表达式字符转义。
- 🌐 **DOM 库更新**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：包含多项默认值变更（如 `strict` 默认为 `true`、`module` 默认为 `esnext`）和功能弃用（如弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等），旨在反映现代开发生态并提升性能。
- 🧭 **迁移准备**：强调 TypeScript 6.0 的弃用项在 7.0 中将被移除，鼓励开发者使用 `"ignoreDeprecations": "6.0"` 暂时过渡，并尽快解决所有弃用警告。

---

### [GitHub - RhysSullivan/nextjs-mobile-app-template · GitHub](https://github.com/RhysSullivan/nextjs-mobile-app-template)

**原文标题**: [GitHub - RhysSullivan/nextjs-mobile-app-template · GitHub](https://github.com/RhysSullivan/nextjs-mobile-app-template)

这是一个基于 Next.js 16 构建的移动端原生风格应用模板，采用单页面应用结构，通过水平滚动实现类似原生应用的标签页切换，并针对 iOS PWA 的特定行为进行了布局优化。

- 📱 项目是一个 Next.js 移动应用模板，使用水平滚动实现原生标签页切换体验
- 🛠️ 技术栈包括 Next.js 16、React 19、TypeScript、Tailwind CSS、SQLite 和 PWA 支持
- 📐 针对 iOS PWA 的布局优化：底部导航采用 flex 布局而非 fixed 定位，避免系统间隙问题
- 📏 标签页高度通过 ResizeObserver 动态测量，避免 CSS 单位在 iOS 上的兼容性问题
- 🎨 主题同步机制防止页面加载时的闪烁，通过内联脚本提前应用主题设置
- 🔧 包含完整的项目架构：数据层使用 SQLite 和 oRPC，客户端状态管理采用 TanStack Query
- 📱 支持独立页面（如设置页）和标签页两种导航模式，使用 View Transitions API 实现动画
- ⚙️ 提供详细的适配指南，指导用户如何修改类型定义、数据库模式、界面组件等
- ⚠️ 明确列出可能破坏布局的修改项，特别是针对 iOS PWA 的特定约束
- 🔄 包含 Service Worker 实现离线支持，并说明缓存更新策略

---

### [GitHub - 1bye/apiser：一套完全类型化的后端开发工具集，让后端工作更轻松。（进行中）· GitHub](https://github.com/1bye/apiser)

**原文标题**: [GitHub - 1bye/apiser: Collection of fully-typed tools to work in back-end with ease. (WIP) · GitHub](https://github.com/1bye/apiser)

这是一个为 Drizzle ORM 设计的类型安全、可链式调用的模型运行时库，旨在通过封装表逻辑、提供渐进式查询构建流程和统一的结果处理层，来简化后端应用的开发。

- 🛠️ **项目概述**：`@apisr/drizzle-model` 是一个基于 Drizzle ORM 的模型抽象层，为每个数据库表提供可复用的模型，并支持链式查询构建。
- 🚀 **核心价值**：在 Drizzle ORM 的基础上，增加了模型抽象、渐进式查询流程、内置结果格式化、安全的错误处理以及可组合的业务逻辑扩展。
- 📦 **快速上手**：通过 `modelBuilder` 创建模型，支持基本的增删改查操作，并使用 `esc()` 函数确保查询条件类型安全。
- 🔗 **关联加载**：通过 `.with()` 方法支持加载关联数据（包括嵌套关联），并使用 `.include()` 进行类型安全的嵌套关系指定。
- 🎯 **结果精炼**：提供 `.select()` 和 `.exclude()` 控制 SQL 查询字段，`.omit()` 在查询后程序化移除字段，以及 `.raw()` 跳过格式化函数。
- 🛡️ **安全执行**：通过 `.safe()` 方法将操作结果包装为 `{ data, error }` 对象，便于错误处理。
- 💼 **事务支持**：使用 `.db(tx)` 将模型绑定到事务实例，确保操作在事务中执行。
- ⚙️ **高级功能**：支持通过 `format` 函数格式化每一行数据，设置默认 `where` 条件，以及通过 `extend()` 扩展自定义方法。
- ⚡ **性能考量**：`.with()` 使用 JOIN 避免 N+1 查询，建议使用 `.select()` 减少查询负载，并为常用条件字段添加索引。
- ⚠️ **当前限制**：需要 Drizzle ORM relations v2，不支持懒加载，无查询缓存或中间件系统，且所有 `.where()` 条件值必须使用 `esc()` 包装。

---

### [GitHub - huozhi/sugar-high: ✏️ 超轻量级代码语法高亮器，压缩并 gzip 后仅约 1KB · GitHub](https://github.com/huozhi/sugar-high)

**原文标题**: [GitHub - huozhi/sugar-high: ✏️ Super lightweight code syntax highlighter, around 1KB after minified and gzipped · GitHub](https://github.com/huozhi/sugar-high)

Sugar High 是一个超轻量级的 JavaScript 和 JSX 语法高亮库，压缩后仅约 1KB，支持浏览器和任何可设置 HTML 字符串的 JS 运行时。

- 📦 **超轻量设计** – 压缩后仅约 1KB，适合性能敏感场景
- 🛠️ **多语言支持** – 核心支持 JavaScript 和 JSX，通过预设扩展支持 CSS、Rust、Python 等
- 🎨 **灵活样式** – 使用 CSS 自定义属性（如 `--sh-class`）轻松定制高亮颜色
- 📏 **行号与高亮** – 可通过 CSS 计数器添加行号，支持按行高亮背景
- 🔌 **生态集成** – 提供 remark 插件，便于在 Markdown 处理中自动高亮代码块
- 🌐 **详细文档** – 更多语言预设和主题可访问 sugar-high.vercel.app 查看

---

### [无](https://expo.dev/blog/from-web-to-native-with-react?utm_source=Nextjsweekly&utm_medium=newsletter&utm_campaign=33087804-React%20to%20Native&utm_content=react_to_native_blog)

**原文标题**: [None](https://expo.dev/blog/from-web-to-native-with-react?utm_source=Nextjsweekly&utm_medium=newsletter&utm_campaign=33087804-React%20to%20Native&utm_content=react_to_native_blog)

该网站是 Expo 平台的主页，提供 React Native 应用开发工具和服务的导航与资源。

- 📚 文档与资源：提供产品文档、博客、更新日志和新闻通讯等支持材料
- 🛠️ 开发工具：包括 Expo CLI、EAS 应用服务、Expo Go 应用和 Snack 在线编辑器
- 💼 企业服务：涵盖企业解决方案、定价信息、客户案例和咨询服务
- 🏢 公司信息：展示品牌介绍、招聘信息、法律条款和隐私政策
- 🤝 社区支持：通过 Discord 社区和信任中心提供用户支持与交流平台
- ⚖️ 法律合规：包含服务条款、可接受使用政策、隐私说明和 Cookie 政策等法律文件

---

### [提升退出动画效果的 React 技巧](https://barvian.me/react-exit-animations)

**原文标题**: [A React trick to improve exit animations](https://barvian.me/react-exit-animations)

本文介绍了一种利用 React 的 Suspense 特性来优化组件退出动画的方法，通过“冻结”组件在退出过程中的 DOM 更新，避免内容变化干扰动画效果。

- 🐛 **问题**：在 React 中，触发退出动画的更新常同时改变退出组件的内容，导致动画期间内容闪烁，分散注意力。
- 🔍 **探索**：尝试过保存状态或延迟更新等方法，但要么过于繁琐，要么处理动画中断时较复杂。理想方案是让 React 停止提交退出组件的 DOM 更改。
- 💡 **解决方案**：利用 Suspense 在挂起时暂停 DOM 提交的特性，创建`Freeze`组件包裹需冻结的部分，并移除 Suspense 自动添加的`display: none`样式，使组件在退出时保持视觉状态不变。
- ⚙️ **实现细节**：通过自定义`ElementsObserver`捕获子 DOM 节点，在`useInsertionEffect`中恢复显示样式，并用一个无限 Promise 触发 Suspense 挂起。
- 🚀 **应用示例**：结合 React Aria Components 使用，可有效冻结包括交互状态（如悬停）在内的整个组件，提升退出动画的平滑度。
- ⚠️ **注意事项**：此方法属于技巧性实现，可能随 React 版本更新而失效，目前兼容 React 18 和 19.2；作者希望 React 未来能原生支持类似的“可见但非活跃”状态。

---

### [如何测量和优化 React 性能 | DebugBear](https://www.debugbear.com/blog/measuring-react-app-performance)

**原文标题**: [How to Measure and Optimize React Performance | DebugBear](https://www.debugbear.com/blog/measuring-react-app-performance)

本文介绍了如何测量和优化 React 应用性能，涵盖从开发工具的使用到生产环境监控的全流程，旨在帮助开发者识别并解决性能瓶颈，提升用户体验。

- 🔍 **React 性能测量工具**：包括 React Performance Tracks、React Developer Tools Profiler、Profiler 组件 API、Chrome DevTools 性能面板和真实用户监控（RUM），用于可视化组件渲染、调度和服务器活动。
- 🛠️ **运行时优化技术**：通过`memo()`、`useMemo()`和`useCallback()`进行记忆化，避免不必要的重新渲染；使用代码分割和列表虚拟化减少初始加载和渲染开销。
- 🧠 **并发特性应用**：利用`useTransition`和`useDeferredValue`管理更新优先级，保持 UI 响应性，特别是在处理大量数据更新时。
- 📦 **包大小优化**：分析并减少 JavaScript 包体积，通过按需导入、使用轻量库和启用构建工具优化（如 tree shaking）来加速加载。
- ⚙️ **服务器端渲染与流式传输**：采用 SSR 和 React Server Components（RSC）提升首屏渲染速度，利用`renderToPipeableStream`和`<Suspense>`实现渐进式内容交付。
- 🤖 **React 编译器自动优化**：引入 React Compiler 在构建时自动添加记忆化，减少手动优化需求，但需遵循 React 纯函数规则。
- 📊 **生产环境监控**：通过真实用户监控工具（如 DebugBear RUM）跟踪核心 Web 指标，设置性能预算，持续优化用户体验。

---

### [给你的 useEffect 函数起个名字吧，以后你会感谢我的——Neciu Dan](https://neciudan.dev/name-your-effects)

**原文标题**: [Start naming your useEffect functions, you will thank me later — Neciu Dan](https://neciudan.dev/name-your-effects)

为 useEffect 函数命名能显著提升代码可读性、调试效率和组件结构清晰度，这一简单实践改变了开发者阅读和编写 React 组件的方式。

- 🚀 **提升可读性**：命名后的 useEffect 函数名直接揭示其意图，使开发者无需深入代码即可理解数据流和副作用逻辑。
- 🔍 **优化调试体验**：命名函数在错误堆栈和 React DevTools 中显示具体名称，帮助快速定位问题，尤其在监控工具中极为实用。
- 🧩 **暴露职责过多**：命名过程中若需使用“和”等连接词，提示副作用应拆分，促进代码按关注点分离。
- 🚫 **识别不必要的副作用**：难以命名的副作用往往意味着逻辑应移至渲染逻辑或事件处理中，避免多余渲染周期。
- 🛠️ **辅助重构决策**：命名有助于识别可合并或提取为自定义 Hook 的副作用，简化组件结构，但需避免过度抽象。

---

### [让 React ProseMirror 变得真正、真正快速](https://handlewithcare.dev/blog/making_react_prosemirror_really_really_fast/)

**原文标题**: [Making React ProseMirror really, really fast](https://handlewithcare.dev/blog/making_react_prosemirror_really_really_fast/)

React ProseMirror 是一个将 React 与 ProseMirror 集成的库，旨在解决两者结合时常见的性能问题。通过让 React 完全负责状态管理和渲染，它避免了状态撕裂问题，但带来了新的性能挑战。为了在 60Hz 显示器上实现流畅的 16 毫秒渲染目标，作者进行了深度优化，包括全面记忆化组件、重构位置传递机制以最小化重新渲染，并巧妙利用引用来稳定函数引用。这些改进将每次按键的渲染元素从约 15,000 个减少到仅 6 个，显著提升了性能，甚至在某些情况下超越了原生 ProseMirror 的实现。

- 🚀 **全面记忆化组件**：通过 `React.memo` 包裹所有组件，减少不必要的重新渲染，但需解决因位置变化导致的属性更新问题。
- 🔧 **重构位置传递机制**：将 `pos` 属性替换为 `getPos` 函数，避免因位置变动触发大规模重新渲染，并利用引用保持函数稳定性。
- ⚡ **性能大幅提升**：优化后，每次按键仅渲染受影响的文本节点及其祖先元素，渲染量从约 15,000 个元素降至 6 个，实现高效响应。
- 🧩 **巧妙利用引用**：通过引用更新位置数据，在遵循 React 规则的同时实现近乎完美的记忆化，平衡性能与安全性。
- 🌍 **跨浏览器表现**：优化后的 React ProseMirror 在 Firefox 上甚至超越了原生 ProseMirror 的编辑性能，展示了虚拟 DOM 算法的优势。
- 🔮 **未来项目预告**：作者团队正在开发新的富文本编辑框架 Pitter Patter，并邀请社区赞助支持，以构建更强大的编辑工具。

---

