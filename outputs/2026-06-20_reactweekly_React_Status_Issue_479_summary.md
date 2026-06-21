### [React Router v8 | Remix](https://remix.run/blog/react-router-v8)

**原文标题**: [React Router v8 | Remix](https://remix.run/blog/react-router-v8)

## React Router v8 发布概述

- 🎉 **React Router v8 正式发布** - 这是继v7之后的又一个"无聊"大版本，团队致力于让升级过程尽可能平稳无痛
- 📅 **年度大版本发布计划** - 从v8开始采用每年一次的大版本发布节奏，让版本更新更加可预测和稳定
- 🔧 **v7回顾** - 引入了框架模式，支持类型安全路由模块API、智能代码分割、多种渲染策略（SPA/SSR/静态渲染）和数据加载/变更功能
- 🚀 **v8新增功能** - 包含中间件/上下文支持、分割路由模块、类型安全href、性能优化、RSC支持（不稳定）等40+个版本更新
- ⚠️ **破坏性变更** - 最低支持Node 22.22+、React 19.2.7+、Vite 7+；采用ESM-only模块；移除react-router-dom；部分API弃用
- 🔄 **升级指南** - 更新依赖、采用未来标志、移除弃用API，然后运行`pnpm i react-router@latest`即可
- 🛡️ **生命周期管理** - React Router v6和Remix v2正式进入EOL状态，不再接收安全更新；v7继续接收安全更新
- 🔮 **未来展望** - 计划稳定支持Server Components和Server Actions（目前仍为不稳定状态）；坚持"少即是多"的设计理念
- 💡 **Remix项目新方向** - Remix将发展为真正的全栈、零依赖JavaScript Web框架，而React Router继续专注于React生态

---

### [Remix 3 测试版预览 | Remix](https://remix.run/blog/remix-3-beta-preview)

**原文标题**: [Remix 3 Beta Preview | Remix](https://remix.run/blog/remix-3-beta-preview)

Remix 3 Beta 预览版发布，这是一个更简化、更贴近Web的全栈框架，强调组合性与开发体验。

- 🚀 Remix 3 Beta 预览版发布，但尚未生产就绪，欢迎测试反馈。
- 🧩 从“中心栈”转向“全栈”，覆盖路由、渲染、数据、认证、上传等所有环节。
- 🌐 路由基于 Fetch API，控制器返回响应，中间件管理请求生命周期，表单提交至URL。
- 🖼️ 引入“帧”（Frame）概念：服务端渲染的UI片段可独立加载、导航和更新。
- 💻 组件采用过程式风格，状态与异步逻辑清晰，支持可组合的混入行为。
- 📦 采用“去捆绑化”策略，运行时为真相源，不依赖预分析，对AI友好。
- 🔧 减少依赖，内置核心功能（路由、会话、认证、表单、上传等），开箱即用。
- 🧪 可通过 `npx remix@next new my-remix-app` 快速开始，鼓励实验与反馈。
- 📬 每周更新新功能，用户反馈将塑造 Remix 3 的最终形态。

---

### [[编译器] 将React编译器移植到Rust - josephsavona · 拉取请求 #36173 · react/react · GitHub](https://github.com/react/react/pull/36173)

**原文标题**: [[compiler] Port React Compiler to Rust by josephsavona · Pull Request #36173 · react/react · GitHub](https://github.com/react/react/pull/36173)

React 编译器已成功移植到 Rust，这是一个实验性的工作进展，旨在提升性能和集成灵活性。

- 🚀 **性能显著提升**：作为 Babel 插件运行时速度快了 3 倍，实际转换逻辑快了约 10 倍，原生集成（OXC、SWC）预计会更快。
- 🧩 **架构保持一致**：Rust 版本沿用了 TypeScript 版本的架构，使用相同的中间表示（HIR）、控制流图（CFG）和单静态赋值（SSA），并采用 arena 结构适配 Rust 的借用系统。
- ✅ **正确性验证充分**：所有 1725 个测试用例均通过，包括代码输出和每个编译 pass 中间状态的对比，OXC 和 SWC 集成也运行良好。
- 🔧 **提供多种集成方式**：目前支持 Babel 插件、OXC 和 SWC 三种集成，未来计划将 Babel 插件整合到主版本中。
- 🤖 **AI 辅助编码**：架构由人类主导，但大部分代码由 AI 生成，人类在架构、测试和代码质量上进行了严格把控。
- 📦 **未来计划**：考虑优化返回补丁而非整个程序、使用 arena 分配和 smol_str 优化字符串表示、实现自己的作用域解析。
- 🔗 **合作伙伴支持**：欢迎与 OXC、SWC 等工具团队合作，集成 Rust 版本的 React 编译器，并提供了示例代码供参考。

---

### [React Native 0.86 - 无边距与开发者工具改进，无破坏性变更 · React Native](https://reactnative.dev/blog/2026/06/11/react-native-0.86)

**原文标题**: [React Native 0.86 - Edge-to-Edge and DevTools Improvements, no breaking changes · React Native](https://reactnative.dev/blog/2026/06/11/react-native-0.86)

React Native 0.86 发布，带来 Android 15+ 全面边缘到边缘支持、DevTools 改进，且无用户端破坏性变更。

- 🏠 React Native 仓库已从 facebook 迁移至 react GitHub 组织，URL 自动重定向，无需手动操作。
- 📱 Android 15+ 边缘到边缘模式全面修复，包括 measureInWindow、KeyboardAvoidingView、Dimensions、StatusBar 和导航栏对比度。
- 🛠️ React Native DevTools 新增亮/暗模式模拟功能，可通过命令面板临时切换。
- ✅ 无用户端破坏性变更，从 0.85 升级无需修改应用代码。
- ⚠️ 弃用 ViewUtil.getUIManagerType 和 AppRegistry.setComponentProviderInstrumentationHook 的第二个参数。
- 🚀 运行时与 Web 规范对齐：ExceptionsManager 严格化、PerformanceObserver 默认阈值设为 104ms。
- 🎨 渲染与布局改进：Modal 支持 style 属性、修复动画闪烁、文本测量崩溃、非可逆变换触摸问题及 Yoga 布局回归。
- ♿ 无障碍修复：三个 AccessibilityInfo 方法在不受支持平台返回 false 而非挂起。
- 📦 依赖更新：Metro ^0.84.2，HeadlessJsTaskSupportModule 自动注册。
- 🔧 JSI 新增 IRuntime 接口、TypedArray 支持、ArrayBuffer.detached、Array.push、String.length、isInteger 及错误创建 API。
- 📲 Android 输入与导航改进：BackHandler 事件对象、修复 API 36+ 恢复问题、LogBox 返回键关闭、Samsung 键盘修复、IME 高度响应、Pressable 支持 PlatformColor、Image.getSize 返回真实尺寸。
- 🌐 Android 网络改进：修复大响应 OOM、WebSocket Cookie 头保留、Blob 内容提供器在新架构下正常工作。
- 👏 感谢 97 位贡献者的 596 次提交，特别致谢 Mathieu Acthernoene、Jakub Piasecki 等人。

---

### [WordPress 中的 React 19 升级——打造 WordPress 核心](https://make.wordpress.org/core/2026/05/27/react-19-upgrade-in-wordpress/)

**原文标题**: [React 19 Upgrade in WordPress – Make WordPress Core](https://make.wordpress.org/core/2026/05/27/react-19-upgrade-in-wordpress/)

WordPress 正在从 React 18 升级到 React 19，这项变更将首先在 Gutenberg 插件（版本 23.3）中推出，并预计在 WordPress 7.1 中正式发布。本文为插件和主题开发者提供了关于时间线、已移除 API、行为变更、新 API、TypeScript 类型变更以及测试指南的全面概述。

- 📅 **升级时间线**：React 19 将在 Gutenberg 7.0 版本后合并到主干，并计划在 WordPress 7.1 中发布，鼓励开发者尽早使用 Gutenberg 插件进行测试。
- 🗑️ **已移除的 API**：`render`、`hydrate`、`unmountComponentAtNode` 和 `findDOMNode` 已被移除，需改用 `createRoot`、`hydrateRoot` 或 `root.unmount()` 等方法；`defaultProps` 对函数组件不再支持，应使用 ES6 默认参数。
- 🔄 **行为变更**：`inert` 属性变为布尔类型；Ref 回调可返回清理函数；`forwardRef` 不再必需，`ref` 可作为常规 prop 传递。
- 🆕 **新增 API**：包括 `use`、`useActionState`、`useOptimistic`、`useFormStatus`、`Activity` 和 `useEffectEvent`，可通过 `@wordpress/element` 使用。
- 🏷️ **TypeScript 类型变更**：`MutableRefObject` 被弃用；`ReactElement` 的 props 类型从 `any` 改为 `unknown`；需注意 HTML 元素 prop 冲突问题。
- 🧪 **测试指南**：安装最新 Gutenberg 插件，启用开发模式，测试主要功能，检查浏览器控制台，并测试 iframe 交互。
- 📚 **进一步阅读**：官方 React 19 升级指南、博客文章、Gutenberg 跟踪问题及 PR 等资源可供参考。

---

### [React 19 升级在 Gutenberg 中暂时回滚 – 构建 WordPress 核心](https://make.wordpress.org/core/2026/06/05/react-19-upgrade-temporarily-reverted-in-gutenberg/)

**原文标题**: [React 19 upgrade temporarily reverted in Gutenberg – Make WordPress Core](https://make.wordpress.org/core/2026/06/05/react-19-upgrade-temporarily-reverted-in-gutenberg/)

Gutenberg 中的 React 19 升级因插件兼容性问题被暂时回退，团队将制定更稳妥的渐进式升级策略。

- 🔄 React 19 升级在 Gutenberg 23.3.0 发布后，因许多基于 React 18 构建的插件频繁崩溃而被回退
- ⚠️ 虽然 React 18 和 19 的 API 几乎没有变化，但运行时存在意外不兼容，例如 `react/jsx-runtime` 生成的元素对象形状不同
- 🛠️ 团队计划制定更优的升级策略，包括通过实验性功能标志在 React 18 和 19 之间切换，以及为已发布插件提供兼容层
- 📉 回退已在 Gutenberg 23.3.2 中实施，为团队争取时间彻底测试新策略
- 🎯 团队仍致力于在 WordPress 7.1 中完成升级

---

### [介绍 Observe：Expo 应用的性能监控](https://expo.dev/blog/introducing-observe)

**原文标题**: [Introducing Observe: Performance monitoring for Expo apps](https://expo.dev/blog/introducing-observe)

这篇内容探讨了人工智能对就业市场的影响，指出自动化将取代部分重复性工作，但也会创造新的岗位，并强调技能提升和终身学习的重要性。

- 🤖 自动化技术将取代制造业、客服等领域的重复性工作，导致部分岗位减少。
- 💼 人工智能同时会催生数据科学家、AI伦理顾问等新兴职业，带来就业机会。
- 📚 劳动者需要持续学习新技能，如编程、数据分析，以适应技术变革。
- 🌍 政府和企业应合作提供再培训计划，缓解失业冲击，确保公平转型。
- ⚖️ 政策制定需关注社会不平等问题，避免技术红利集中在少数人手中。

---

### [TypeScript 7.0 RC 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

**原文标题**: [Announcing TypeScript 7.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

TypeScript 7.0 RC 发布，基于Go重写，速度提升约10倍，兼容TypeScript 6.0，并带来多项新特性。

- 🚀 TypeScript 7.0 基于Go重写，速度比6.0快约10倍，通过原生代码速度和共享内存并行实现。
- ⚙️ 可通过 `npm install -D typescript@rc` 安装，并支持与TypeScript 6.0并行运行，使用 `@typescript/typescript6` 包避免冲突。
- 🧩 引入并行化检查器（默认4个）和项目构建器，通过 `--checkers` 和 `--builders` 标志控制，优化大型代码库性能。
- 👁️ 重写 `--watch` 模式，基于Parcel文件监视器，跨平台更高效稳定。
- 📜 默认配置变化：`strict` 默认true，`module` 默认 `esnext`，`target` 默认当前稳定ES版本，`types` 默认 `[]` 等。
- 🔧 弃用项变为硬错误：如 `target: es5`、`downlevelIteration`、`moduleResolution: node` 等不再支持。
- 🔤 模板字面量类型现在保留Unicode码点，避免代理对分割问题。
- 📝 JavaScript支持重写，更一致，移除旧JSDoc模式，如 `@enum`、`@class` 等不再特殊处理。
- 🛠️ 编辑器体验提升：VS Code扩展支持，基于LSP，多线程处理，减少命令失败率20倍以上。
- 🗓️ 计划一个月内发布稳定版，后续7.1将提供稳定API。

---

### [[DRAFT] 添加原型信号+路径追踪实现 by markerikson · 拉取请求 #2318 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/pull/2318)

**原文标题**: [[DRAFT] Add prototype signals+path-tracking implementation by markerikson · Pull Request #2318 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/pull/2318)

该PR为React-Redux添加了基于信号和路径追踪的原型实现，旨在优化大型应用中的订阅和选择器性能。

- 🚀 新增`SignalProvider`和`useSignalSelector`，作为`Provider`和`useSelector`的替代方案，通过代理和信号机制自动追踪状态依赖，减少不必要的回调执行
- ⚡ 性能提升显著：在14个基准测试场景中，12个场景的脚本执行时间比当前9.x版本快20-40%，仅在极端场景（单个组件订阅数百个切片）下表现稍差
- 🔍 实现原理：使用代理包装状态对象，追踪选择器访问的字段路径，每次dispatch后对比新旧状态差异，仅更新受影响的信号，触发相关组件重新渲染
- ⚠️ 已知限制：无法自动处理对象引用比较（如`===`），需要`unwrap()`辅助函数；数组方法调用会保守地标记整个数组为依赖，可能产生少量误报
- 📦 包体积增加约21KB（+61%），主要来自信号库和代理实现代码
- 🧪 当前为Alpha阶段，代码100%由AI生成但经过人工审查，已在基准测试套件中验证稳定性，欢迎在真实应用中测试反馈
- 🎯 定位为可选替代方案，不会替换现有`Provider`和`useSelector`，计划通过独立入口（如`react-redux/signals`）提供

---

### [Wasp 现在允许你用 TypeScript 编写全栈逻辑规范 | Wasp](https://wasp.sh/blog/2026/06/15/wasp-typescript-spec)

**原文标题**: [Wasp now lets you write your full-stack logic as a spec in TypeScript | Wasp](https://wasp.sh/blog/2026/06/15/wasp-typescript-spec)

Wasp 现在允许你使用 TypeScript 编写全栈逻辑规范，取代了之前的自定义 DSL 语言，使开发更灵活、可扩展。

- 🚀 **TypeScript 原生规范**：通过 `*.wasp.ts` 文件使用 `@wasp.sh/spec` 中的构造函数（如 `page`、`route`、`query`）定义全栈应用，并导出 `app` 规范对象。
- 🧩 **强大的 TypeScript 能力**：规范层完全使用 TypeScript，支持第三方库、多文件拆分、自定义函数、循环、文件读取等，甚至可实现文件路由等高级功能。
- 🔗 **规范与实现连接**：使用 `with { type: "ref" }` 导入将规范与 React、Node.js、Prisma 等实现关联，通过打包器转换为引用对象。
- 🎯 **规范作为一等公民**：规范是显式、可编程、独立、可扩展的，允许组织、重用和分发全栈逻辑，未来支持“全栈模块”（FSM）。
- 🤖 **AI 友好**：规范提供应用高级概览，避免实现细节干扰，支持规范驱动开发，且全栈模块可确保 AI 不破坏关键功能。
- 🛠️ **当前状态与未来**：Wasp 仍处于 Beta 阶段，计划改进规范设计、核心功能重构、支持更多 ORM 和前端库，以及扩展后端语言支持。

---

### [任意规模下的Postgres时间序列工作负载。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

此服务提供大规模时间序列数据处理的Postgres解决方案，支持企业级部署与灵活扩展。

- 📊 支持单日处理3万亿指标、3PB数据及1千万亿数据点
- 💰 新用户可获$1000额度（30天有效），无需信用卡
- 🚀 读写分离架构支持最多10节点副本集，SSD/S3分层存储
- ⚡ 计算与存储独立扩展，避免闲置资源付费
- 🔒 多可用区集群，自动故障转移、时间点恢复与跨区域备份
- 🛡️ 符合SOC 2、HIPAA、GDPR标准，支持加密、SSO、RBAC及审计日志
- 📈 深度可观测性：查询下钻与仪表盘，集成CloudWatch、Datadog、Prometheus
- 🛠️ 快速部署：数分钟完成数据库配置，支持SQL、CLI、Terraform、Cursor、Claude Code
- 🔗 与主流云提供商及Postgres生态集成
- 🏢 企业级支持：SLA保障、24/7专家支持、区域数据隔离

---

### [TanStack Start：Next.js 开发者的心智模型 | Adarsha Acharya](https://www.adarsha.dev/blog/tanstack-mental-model-for-nextjs-developers)

**原文标题**: [TanStack Start: A Mental Model for Next.js Developers | Adarsha Acharya](https://www.adarsha.dev/blog/tanstack-mental-model-for-nextjs-developers)

概述摘要  
TanStack Start 从Next.js开发者的视角切入，重点对比其路由优先架构、显式服务器边界、类型安全路由、缓存策略、渲染模式及服务器函数等核心特性。

- 🧭 路由优先架构：TanStack Start 以路由器为核心，与Next.js的文件系统路由不同，强调更灵活的路由定义方式  
- 🔒 显式服务器边界：通过明确标记服务器端代码与客户端代码，避免Next.js中隐式边界带来的混淆  
- 🛠️ 类型安全路由：提供完整的TypeScript类型推断，确保路由参数、查询和链接的类型安全  
- ⚡ 缓存策略：内置细粒度缓存控制，支持数据预取与状态同步，优于Next.js的默认缓存机制  
- 🖼️ 渲染模式：支持SSR、SSG及客户端渲染，但更注重开发者对渲染行为的显式控制  
- 📡 服务器函数：通过`server$`等API显式定义服务器端逻辑，简化数据获取与突变操作  
- 🔄 对比优势：适合需要高度自定义路由和服务器逻辑的Next.js开发者迁移

---

### [我们如何通过迁移到Next.js应用路由器将响应速度降低80% - DEV社区](https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da)

**原文标题**: [How We Cut Slow Responses by 80% Migrating to Next.js App Router - DEV Community](https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da)

Subito 是意大利领先的分类广告平台，其广告详情页面通过迁移到 Next.js App Router，成功将慢响应减少了约 80%。以下是关键要点总结：

- 📉 **性能大幅提升**：迁移后，超过 250ms 的响应比例从 25%-40% 降至接近零，视频游戏类别的快速 URL（<500ms）提升近 30%。
- 🛠️ **渐进式迁移策略**：通过并行运行 Pages Router 和 App Router，不冻结产品开发，使用服务器组件包装现有客户端组件，实现无重复代码的增量迁移。
- 🔄 **自定义 Express 服务器**：利用 Express 层实现按请求路由控制，支持渐进式发布（如按类别和查询参数 `?use-ar=1`），并解决框架缺失的 HTTP 410 状态码问题。
- 🌊 **HTML 流式传输挑战**：需要配置 Nginx（禁用缓冲）和 Akamai CDN（自定义元数据启用分块传输），才能实现端到端流式渲染，缓存命中时则返回完整 HTML。
- 📈 **SEO 安全发布**：分两阶段进行——先迁移到 App Router（关闭流式），再逐步启用流式，每个类别监控约两周 SEO 指标，确保无负面影响。
- 👨‍💻 **低投入高回报**：主要由一名开发者在日常功能交付间增量完成，借助 Claude Code 加速规划与实现，无需专职团队。
- 💡 **关键经验**：并行路由允许无冻结迁移；自定义服务器层提供灵活控制；HTML 流式需要在每一层（Nginx、CDN）明确配置；端到端和视觉回归测试提前捕获回归。

---

### [当React Hooks不再扩展：将复杂状态迁移至Zustand - Oren Farhi](https://orizens.com/blog/2026-06-18-zustand/)

**原文标题**: [When React Hooks Stop Scaling: Moving Complex State to Zustand - Oren Farhi](https://orizens.com/blog/2026-06-18-zustand/)

### 概述总结
当React Hooks不再适用于共享状态时，将复杂状态迁移至Zustand能显著提升代码清晰度和可维护性。

- 🎤 **初始方案**：使用自定义Hook管理语音识别状态，包括实时转录、说话状态和错误信息。
- 🐛 **问题浮现**：当状态需在多个组件间共享，且更新来自浏览器事件和外部服务时，出现数据陈旧和状态归属模糊的bug。
- ⚠️ **Hook过载**：Hook逐渐承担状态管理、事件同步、多消费者协调等职责，虽接口简洁但实现复杂。
- ❌ **Context不足**：React Context无法处理来自React组件外部的状态更新（如浏览器API异步事件）。
- 🏪 **迁移至Zustand**：将状态移至独立Store，语音识别服务直接更新Store，组件按需订阅所需数据片段。
- ✅ **显著改进**：消除状态归属歧义，形成单一数据源，使更新流向清晰可追踪。
- 🔄 **保留Hook场景**：组件私有状态或封装UI行为时仍优先使用Hook；跨组件共享且需外部更新的状态则视为应用状态。
- 💡 **核心启示**：问题不在于Hook本身，而在于当需求从局部变为全局时，需及时调整抽象层级，让复杂度显性化。

---

### [TanStack Table V9 中的 TypeScript 性能 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-typescript-performance)

**原文标题**: [TypeScript Performance in TanStack Table V9 | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-typescript-performance)

TanStack Table V9 通过模块化类型系统大幅提升性能，将 TypeScript 类型检查工作量减少 62-86%，同时保持更强的类型推断能力。

- 🚀 **性能飞跃**：从 V9 alpha 到 beta.12，核心包类型实例化从 1,230,007 降至 266,723（降幅 78.3%），所有框架适配器均实现 62-86% 的优化。
- 🧩 **模块化设计**：V9 采用特性映射（Feature Map）替代 V8 的全局合并，支持按需注册功能，类型和运行时仅包含所选特性。
- ⚡ **关键优化技术**：使用命名接口替代条件类型联合、为内部类型添加 `in out` 方差注解、在适配器钩子中显式传递类型参数。
- 📊 **测量方法**：通过 `tsc --extendedDiagnostics` 追踪类型实例化次数，结合 `--generateTrace` 精确定位性能瓶颈。
- 🛠️ **开发者体验**：编辑器响应恢复即时，真实应用类型检查时间减半，所有推断能力（特性选择、函数注册、元数据、插件）保持不变。
- 📝 **库作者建议**：测量类型实例化、命名类型需参数重复才有缓存效果、内部类型优先使用接口、为不变类型参数添加 `in out` 注解。

---

### [React Native 需要一个新的视频播放器 | Mux](https://www.mux.com/blog/react-native-needs-a-new-video-player)

**原文标题**: [React Native needs a new video player | Mux](https://www.mux.com/blog/react-native-needs-a-new-video-player)

本文章介绍了一个为 React Native 应用全新打造的 Mux 视频播放器，它整合了 Mux 原生播放器、升级版 UI、Mux Robots 和 Mux Data 功能。

- 🎬 **全新 React Native 播放器**：基于 Mux 现有的 Swift 和 Android 播放器，通过 React Native 封装，提供统一的视频播放体验。
- 🔧 **安装与使用**：可通过 npm 安装，并提供了示例应用和 GitHub 仓库链接，方便开发者快速上手。
- 📜 **历史背景**：作者从 2018 年开始关注跨平台框架，经历了从 React Native 到 Flutter 再回到 React Native 的历程，认为 Expo 极大地改善了开发体验。
- 🏗️ **架构设计**：采用三层架构——TypeScript 播放器状态、React 视图封装和原生视图，确保 API 简洁且播放路径原生。
- 🎥 **Mux 播放类型**：支持签名播放、DRM、带宽控制、剪辑、自定义域名和 Mux Data 等高级功能，远超普通 HLS 播放器。
- ⚡ **响应式播放器对象**：`MuxVideoPlayer` 类管理状态和命令，支持 `play`、`pause`、`seekTo` 等操作，并处理原生视图未挂载时的命令队列。
- 📡 **原生事件桥接**：通过 `useSyncExternalStore` 订阅播放器状态，原生事件通过事件处理器更新 JS 状态，实现双向通信。
- 🍏 **iOS 原生播放**：使用 `AVPlayerViewController` 和 Mux Player Swift，处理播放 ID、播放选项和监控选项。
- 🤖 **Android 原生播放**：使用 Mux Android 播放器和 Media3 UI 组件，配置 Mux Data 并处理媒体项。
- 📊 **Mux Data 集成**：首次在 React Native 播放器中支持 Mux Data，可获取视频播放指标和参与度数据，并可在 Mux 仪表板或终端中查看。
- 🤖 **Mux Robots UI**：新增 Mux Robots 功能，支持视频摘要、章节生成和关键时刻查找，通过简单 prop 即可启用，并支持画中画模式。

---

### [React Props 入门 - Visual Studio 市场](https://marketplace.visualstudio.com/items?itemName=yurii.react-props-first)

**原文标题**: [
        React Props First - Visual Studio Marketplace
    ](https://marketplace.visualstudio.com/items?itemName=yurii.react-props-first)

概述摘要  
React Props First 是一个VS Code扩展，用于优化React组件的IntelliSense自动补全，优先显示自定义props而非继承的DOM和ARIA属性。

- 🚀 核心功能：在JSX/TSX自动补全中，将自定义props（如variant、size）排在继承属性（如disabled、onClick）之前  
- ⚙️ 工作原理：通过TypeScript服务器插件修改completion项目的sortText，基于props声明位置重新排序  
- 📁 支持文件类型：主要支持.tsx文件，.jsx文件需通过JSDoc类型推断才有效  
- ❌ 不支持场景：纯无类型JSX组件（无法推断自定义props）  
- 🔧 设置选项：reactPropsFirst.enabled（启用/禁用）、reactPropsFirst.enableJavaScript（启用.jsx支持）、reactPropsFirst.debug（调试日志）  
- 🛠 开发方式：使用npm install和npm test，提交需遵循Conventional Commits规范  
- 📦 安装途径：可通过VS Code Marketplace安装或运行命令code --install-extension yurii.react-props-first

---

### [无样式UI组件，用于无障碍设计系统 · Base UI](https://base-ui.com/)

**原文标题**: [Unstyled UI components for accessible design systems · Base UI](https://base-ui.com/)

概述总结
- 🎨 Base UI 是一个无样式 UI 组件库，用于构建无障碍、可访问的 React 用户界面
- 📚 由 Radix、Floating UI 和 Material UI 的创建者开发，注重组合性、一致性和工艺
- 🔧 架构优先考虑灵活性，不施加视觉意见，帮助团队打造独特且可靠的无障碍界面
- 🏗️ 基于多年组件库开发经验，精心设计细节，旨在提供持久稳定的基础
- 👥 专为开发者打造，被 Paper、GitHub、Zed 等公司使用
- 🧑‍💻 由 Colm Tuite、Marija Najdova 等专业工程师团队维护
- 📋 支持 Tailwind、CSS Modules、CSS-in-JS 等任何样式库，以及 Motion 等动画库
- ♿ 遵循 ARIA Authoring Practices Guide 和 WCAG 2.2 标准，经过广泛测试确保无障碍
- 🔄 与 Radix UI API 设计相似，但提供更复杂组件（如 Combobox、Autocomplete）和更深功能支持（如输入擦洗、嵌套对话框）
- 🆓 基于 MIT 许可证，免费用于商业项目，但暂不提供企业 SLA 或正式支持保证

---

### [2026年1月 - Base UI 文档 - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-01-base-ui)

**原文标题**: [January 2026 - Base UI Documentation - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-01-base-ui)

以下是您提供的文本内容的总结：

概述：本文档介绍了Base UI组件的完整文档发布，包括新功能、组件列表以及如何开始使用。

- 📚 **完整Base UI文档**：所有组件现在都有专用文档，涵盖用法、属性和示例。
- 🔄 **重建示例**：所有组件示例已为Radix和Base UI重建，可切换查看实现差异。
- ⚖️ **并排比较**：文档便于比较两个库中组件的工作方式。
- 🎯 **一致API**：无论选择哪个底层库，组件外观和行为一致，仅实现不同。
- 🚀 **新项目启动**：运行`npx shadcn create`并选择首选库，CLI处理其余部分。
- 📋 **组件列表**：包括Accordion、Alert、Button、Calendar、Dialog等众多组件。
- 🛠️ **其他功能**：涵盖安装、主题、CLI、RTL、技能、MCP服务器、注册表、表单等。
- 🎨 **主题与暗黑模式**：支持自定义主题和暗黑模式。
- 📄 **API参考**：提供registry.json和registry-item.json等API参考。

---

### [手风琴 · 基础UI](https://base-ui.com/react/components/accordion)

**原文标题**: [Accordion · Base UI](https://base-ui.com/react/components/accordion)

Base UI 的 Accordion 组件是一个可折叠面板集合，提供多种配置和 API 来控制面板的展开与收起。

- 📦 **组件结构**：Accordion 由 `Root`、`Item`、`Header`、`Trigger` 和 `Panel` 五个子组件组成，支持灵活组装。
- 🎨 **无样式设计**：组件不包含预设样式，需通过 CSS Modules 或自定义类名进行样式化。
- 🔄 **多面板展开**：通过设置 `multiple` 属性，允许同时展开多个面板。
- 📋 **API 参考**：`Root` 组件支持 `defaultValue`、`value`、`onValueChange`、`disabled`、`keepMounted` 等属性；`Item` 组件提供 `value`、`onOpenChange`、`disabled` 等属性。
- 🎯 **面板控制**：`Panel` 组件支持 `hiddenUntilFound` 属性，允许浏览器搜索找到并展开面板内容，同时提供 `data-starting-style` 和 `data-ending-style` 属性用于动画控制。
- 🔧 **状态管理**：各组件提供 `State` 类型，包含 `open`、`hidden`、`disabled`、`index` 等状态，便于条件渲染和样式绑定。
- 🖱️ **交互事件**：`Trigger` 组件渲染为 `<button>` 元素，支持 `nativeButton` 属性控制是否使用原生按钮。
- 📐 **CSS 变量**：`Panel` 组件暴露 `--accordion-panel-height` 和 `--accordion-panel-width` 变量，方便自定义尺寸。

---

### [OTP 字段 · 基础 UI](https://base-ui.com/react/components/otp-field)

**原文标题**: [OTP Field · Base UI](https://base-ui.com/react/components/otp-field)

OTP字段是一个由单个字符槽组成的一次性密码输入组件。

- 📝 **概述**：OTP字段是一个由单个字符槽组成的一次性密码输入组件，用于输入验证码等一次性密码。
- 🔑 **使用指南**：表单控件必须具有可访问的名称，可以使用 `<label>` 元素或 Field 组件创建。
- 🧩 **组件结构**：由 `OTPField.Root`、`OTPField.Input` 和 `OTPField.Separator` 三部分组成。
- 🏷️ **标签示例**：通过 `id` 和 `htmlFor` 关联标签，第一个输入使用字段标签，其余输入使用 `aria-label` 标识槽位。
- 📋 **表单集成**：使用 Field 组件处理标签关联和表单集成，支持 `autoSubmit` 和 `onValueComplete` 属性。
- 🔤 **字母数字验证码**：使用 `validationType="alphanumeric"` 支持字母和数字混合的验证码。
- 📊 **分组布局**：使用 `OTPField.Separator` 将输入分组，如 123-456 格式。
- 💡 **占位符提示**：支持原生 `placeholder` 属性，示例中占位符在活动槽获得焦点前保持可见。
- 🔧 **自定义规范化**：使用 `normalizeValue` 规范化输入值，如将字母数字验证码转换为大写。
- 👁️ **掩码输入**：使用 `mask` 属性在输入时隐藏代码内容。
- ⚙️ **API 参考**：Root 组件管理状态，Input 组件为单个字符输入，Separator 组件为屏幕阅读器可访问的分隔符。

---

### [GitHub Actions 设置 - 文档 | React Doctor](https://www.react.doctor/docs/ci-and-prs/github-actions-setup)

**原文标题**: [GitHub Actions Setup - Docs | React Doctor](https://www.react.doctor/docs/ci-and-prs/github-actions-setup)

### 概述摘要
本文档详细说明了如何在GitHub仓库中设置React Doctor的CI/CD工作流，包括创建专用工作流文件、配置权限、处理PR反馈以及故障排除。

- 🔧 **创建专用工作流文件**：在`.github/workflows/`目录下创建`react-doctor.yml`文件，严格遵循指定YAML配置，包含`actions/checkout@v5`和`millionco/react-doctor@v2`步骤，并设置`fetch-depth: 0`以获取完整git历史。
- 📝 **权限与并发控制**：配置`permissions`块包含`contents: read`、`pull-requests: write`、`issues: write`和`statuses: write`，并使用`concurrency`组防止重复运行，确保评论和状态更新正常。
- 🔄 **PR触发与反馈机制**：工作流在PR的`opened/synchronize/reopened/ready_for_review`事件触发，创建或更新单个固定摘要评论，并在问题行添加内联审查评论，同时设置提交状态。
- 🚫 **避免修改现有代码**：仅创建或更新工作流文件，不修改其他文件、脚本或依赖，确保变更最小化。
- 🛠️ **配置选项与渐进式部署**：支持`blocking`（none/warning/error）和`scope`（full/changed）参数，可先以`blocking: none`运行全量扫描，再逐步收紧规则。
- 📂 **Monorepo支持**：通过`directory`和`project`输入指定子目录或项目，适应多应用仓库结构。
- 🧪 **故障排除指南**：常见问题包括缺少`fetch-depth: 0`导致旧问题误报、权限不足导致评论缺失、以及需要手动添加分支保护规则以阻止合并。

---

### [clerk 部署：引导式、可恢复、智能体就绪](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli-deploy&utm_content=06-19-26&dub_id=VIXhJXWTFXvBEo9P)

**原文标题**: [clerk deploy: guided, resumable, agent-ready](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli-deploy&utm_content=06-19-26&dub_id=VIXhJXWTFXvBEo9P)

### 概述总结
Clerk CLI 新增 `clerk deploy` 命令，可通过单命令将开发实例克隆至生产环境，并逐步引导完成 DNS 和 OAuth 配置，同时支持代理模式输出 JSON 状态。

- 🚀 **一键部署**：`clerk deploy` 命令将应用从开发环境直接部署到生产环境，自动创建生产实例并提示输入生产域名。
- 🔗 **DNS 配置**：显示需在 DNS 提供商处添加的 CNAME 记录，支持导出为 DNS 区域文件以便导入兼容提供商。
- 🔑 **OAuth 凭据**：自动检测开发中启用的社交登录，引导配置 Google 和 Apple 凭据（支持导入 JSON 或 .p8 密钥），其他提供商需在仪表盘手动设置。
- ✅ **验证循环**：自动检查 DNS、SSL 和邮件 DNS 状态，并报告待处理项。
- 🤖 **代理模式**：在非 TTY 环境或使用 `--mode agent` 时，输出只读 JSON 状态，便于自动化工具集成。
- 📋 **快速开始**：更新 CLI、链接项目后运行 `clerk deploy`，完整文档提供所有命令和选项。

---

### [AI原生工程团队如何进行代码审查——AgentField](https://agentfield.ai/blog/ai-native-code-review?utm_source=react&utm_medium=newsletter&utm_campaign=react-260619&utm_id=react-260619-blog-ai-native-code-review&utm_content=blog-ai-native-code-review)

**原文标题**: [How an AI-Native Engineering Team Does Code Review — AgentField](https://agentfield.ai/blog/ai-native-code-review?utm_source=react&utm_medium=newsletter&utm_campaign=react-260619&utm_id=react-260619-blog-ai-native-code-review&utm_content=blog-ai-native-code-review)

AgentField 团队重新设计了代码审查流程，以适应 AI 原生工程时代。传统 PR 审查的四个核心功能（正确性、知识传递、风险可见性、分布式问责）在 AI 编写代码速度大幅提升后已不再捆绑有效。团队将 PR 从“正确性验证门”转变为“风险地图”，通过开源工具 PR-AF 实现基于维度的风险阈值审查，而非二元通过/失败判定。

- 🚀 **AI 时代代码审查已过时**：当 AI 能同时编写和检查代码时，PR 审查的“正确性”功能变得廉价且并行，传统流程失去意义。
- 🔍 **PR 的四个隐藏功能**：正确性、知识传递、风险可见性、分布式问责，在 AI 时代被拆解，其中风险可见性变得至关重要。
- 📈 **三个审查时代**：从人类写人类审 → 人机协作写审 → AI 自主编写，AgentField 已进入第三时代，人类角色提升至系统级目标设定。
- 🗺️ **风险地图取代正确性判决**：PR 现在输出风险分布图，而非通过/失败；安全、命名一致性等维度各有独立阈值，可调且透明。
- ⚖️ **不对称原则**：发现风险成本高，修复风险成本低；审查重点应放在发现而非认证无风险。
- 🔧 **开源 PR-AF**：一个可定制的审查器，按维度并行分析 PR，生成风险地图（而非判决），每次深度审查成本约 80 美分。
- 🌐 **开源理由**：没有两个团队拥有相同的“智能栈”，PR-AF 允许团队根据自身风险维度和阈值进行定制，而非硬编码默认值。

---

### [介绍 | React Flow 智能边](https://tisoap.github.io/react-flow-smart-edge/docs/)

**原文标题**: [Introduction | React Flow Smart Edge](https://tisoap.github.io/react-flow-smart-edge/docs/)

本页介绍了 React Flow 的智能边缘库，支持节点间无交叉的路径规划。

- 📦 使用 npm 或 yarn 安装 `@tisoap/react-flow-smart-edge`，需配合 React Flow v12+ 使用
- 🔗 提供五种预设边缘：SmartBezierEdge、SmartStraightEdge、SmartStepEdge、SmartSmoothStepEdge 和 SmartFloatingEdge
- ✏️ SmartEditableEdge 支持拖拽路径点并自动寻路
- 🛠️ 提供 createSmartEdge 和 getSmartEdge 用于自定义配置
- ☕ 支持通过 Buy me a coffee 或 GitHub 赞助项目
- 📚 下一步可参考快速入门、边缘类型对比和 Storybook 交互示例

---

### [功能：添加suspendTerminal()以将终端交给子进程 - costajohnt · 拉取请求 #972 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/pull/972)

**原文标题**: [feat: add suspendTerminal() to hand the terminal to a child process by costajohnt · Pull Request #972 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/pull/972)

Ink 库新增了 `suspendTerminal()` 功能，允许应用临时将终端控制权交给子进程，并在完成后恢复自身状态。

- 🎯 **核心功能**：`useApp().suspendTerminal()` 让 Ink 应用能暂时释放终端给子进程（如编辑器、分页器），结束后自动恢复并重绘界面。
- 🔄 **两种使用形式**：支持回调形式（即使回调抛出异常也会恢复终端）和可释放对象形式（配合 `await using` 使用）。
- 🛡️ **状态管理**：挂起时刷新输出、停止输入、关闭原始模式、退出备用屏幕等；恢复时重新应用 Ink 的终端状态并强制完整重绘。
- ⚠️ **安全机制**：重复挂起会抛出错误；非交互模式下回调仍执行但不进行终端交接。
- 📚 **完整测试与文档**：包含多种场景的测试（回调、可释放对象、异常恢复、备用屏幕等）、可运行示例以及 API 文档。

---

### [发布 v4.0.0 · plotly/react-plotly.js · GitHub](https://github.com/plotly/react-plotly.js/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · plotly/react-plotly.js · GitHub](https://github.com/plotly/react-plotly.js/releases/tag/v4.0.0)

react-plotly.js 发布了 v4.0.0 版本，主要增加了原生 ESM 支持、TypeScript 声明文件，并将组件重构为函数式组件，同时修复了多个关键问题。

- 📦 新增原生 ESM 输出（与 CJS 并存），发布产物移至 `dist/` 目录，主入口改为 `./dist/index.cjs`
- 🗑️ 移除未压缩的 UMD 包，`import Plot from 'react-plotly.js'` 现在可在 Rolldown 等严格 ESM 环境中正确解析
- 📝 新增 TypeScript 声明文件（`index.d.ts` / `factory.d.ts`）
- 🔧 重构：将类组件改为基于 hooks 的函数式组件，`ref` 现在直接指向渲染的 `<div>` 元素（即 plotly 图表 div），迁移时需将 `ref.current.el` 替换为 `ref.current`
- 🐛 修复：`onPurge` 现在会在卸载时触发，且 `Plotly.purge` 正确运行；React StrictMode 下模拟的卸载/重新挂载后图表能正确重新初始化
- 🛠️ TypeScript 声明现在暴露 ref 转发功能，消费者可附加类型化的 `ref` 属性而不报错
- 🔄 更新了 linting 依赖

---

### [v1.19.0 | React Aria](https://react-aria.adobe.com/releases/v1-19-0)

**原文标题**: [v1.19.0 | React Aria](https://react-aria.adobe.com/releases/v1-19-0)

v1.19.0 版本发布，新增对 GridList 和 Tree 中嵌入式文本字段等交互元素的全键盘导航支持，Autocomplete 和 Popover 获得内联补全改进，Menu 回调新增键值对，DragTypes 支持多 MIME 类型和通配符。同时包含多项修复和优化，并引入破坏性变更。

- 🆕 GridList 和 Tree 新增 `keyboardNavigationBehavior` 属性，支持行内文本字段等交互元素
- 🔄 Autocomplete 修复 CJK 输入法虚拟焦点问题，并添加内联补全示例
- 📍 Popover 新增 `getTargetRect` 属性，支持相对于任意字符位置定位
- 📋 Menu 的 `onAction` 回调现在同时提供项的键和值
- 🖱️ DragTypes.has() 支持多个 MIME 类型和通配符（如 `image/*`）
- ⚠️ 破坏性变更：`@react-aria/optimize-locales-plugin` 升级至 v2，需 webpack 5 或更高版本
- 🐛 修复 `isFocusable` 和 `isElementVisible` 在脱离文档流的节点上崩溃的问题
- 🌳 优化 `optimizeLocales` 构建插件的摇树效果
- 📅 Calendar 修复年份选择器包含 `maxValue` 年份的问题
- 🧪 修复测试环境中 `HTMLElement.prototype.focus` 为只读 getter 导致的崩溃
- 🎨 tailwindcss-react-aria-components 支持 `not-*` 变体

---

