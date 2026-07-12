### [逆向工程ChatGPT网页版：OpenAI如何为十亿用户构建](https://performance.dev/chatgpt)

**原文标题**: [Reverse Engineering ChatGPT Web:
How OpenAI Built for a Billion Users](https://performance.dev/chatgpt)

概述总结
- 🧠 文章深入逆向工程了ChatGPT网页应用的架构，揭示了其如何为十亿用户构建高性能、低门槛的AI交互体验
- 🏗️ 技术栈核心：React 19 + React Router 7（服务端渲染模式）+ Tailwind CSS + TanStack Query + Radix UI，使用主流开源库而非自研框架
- 🔄 迁移历程：从Next.js Pages Router → Remix（SPA模式）→ React Router 7框架模式，SSR程度逐步加深
- ⚡ 性能优先策略：服务端渲染完整HTML壳（84KB压缩，TTFB 50-65ms），内联主题脚本和性能监控，无认证墙直接使用
- 🎨 CSS方案：Tailwind + 语义化token变量层，按路由拆分CSS文件，无Web字体（使用系统字体栈）
- 🧩 组件选择：Radix UI可访问性原语 + ProseMirror编辑器 + CodeMirror代码块，避免重复造轮子
- 📡 数据流：TanStack Query管理客户端状态，服务端预填充缓存，SSE流式传输token，所有API请求在后台预执行
- 🚦 特性标志系统：556个服务端评估的标志（Statsig），哈希命名防止泄露，内联到HTML中避免网络请求
- 🔒 安全设计：Cloudflare工作量证明 + 自研Sentinel反滥用系统，在用户输入前完成所有安全检查
- 🎯 核心设计哲学：所有决策围绕"让用户最快开始输入"这一目标，从预取策略到延迟加载都以此为中心

---

### [2026年7月 - Base UI成为默认 - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)

**原文标题**: [July 2026 - Base UI as the Default - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)

shadcn/ui 宣布默认使用 Base UI 组件库，同时保持对 Radix 的全面支持。

- 🎯 **默认切换**：从 2026 年 7 月起，新项目默认使用 Base UI，Radix 仍可通过 `-b radix` 参数选择。
- 🚀 **Base UI 优势**：版本 1.6.0，周下载量超 600 万，团队持续更新，社区选择比例达 2:1。
- 🔄 **Radix 未弃用**：仍受支持，新组件会同时适配两个库，除非仅 Base UI 独有。
- 🛠️ **无需迁移**：现有 Radix 项目可继续运行，官方不强制迁移。
- 📦 **迁移工具**：提供技能（skill）支持渐进式迁移，可逐个组件转换，保留自定义修改。
- 📋 **迁移产出**：每次迁移生成工作代码、组件报告（`.migration/`）和清晰 Git 历史，支持回滚。
- 🤖 **Agent 兼容**：迁移技能适用于 Claude Code、Cursor 等编码代理，支持断点续传。
- 🧩 **注册表更新**：新注册表项目默认初始化为 Base UI，可指定 `registry:base` 配置。

---

### [Locize – 本地化与翻译管理平台](https://www.locize.com/?from=react-status)

**原文标题**: [Locize â Localization and Translation Management Platform](https://www.locize.com/?from=react-status)

以下是对所提供内容的概述和要点总结：

Locize 是一个本地化平台，连接代码与翻译流程，支持持续交付翻译更新，无需重新部署应用。

- 🌐 一站式本地化平台，无需重新部署即可发布翻译更新
- 🔧 专为 i18next 设计的原生翻译后端，支持任何 i18n 库
- 🤖 AI 自动翻译字符串，Locize 负责管理
- 🚀 开发者与翻译人员可并行工作，翻译更新持续交付，不阻塞发布
- 🇨🇭 由 i18next 创建者开发，瑞士公司提供
- ✅ 自动化工作流，加速全球产品发布
- 👨‍💻 开发者保持代码/CI 控制权，翻译人员在专用 UI 中工作
- 📦 通过 CDN/API 交付，翻译更新无需完整应用重新部署
- 🔄 典型流程：从代码同步密钥 → 翻译/审核 → 运行时交付
- 🛠️ 支持 CLI、API、原生 i18next 集成，零 JSON 文件管理
- 📊 为管理者提供基于使用量的成本控制、审核工作流和项目健康指标
- 🎯 为翻译人员提供 AI 辅助 CAT 工具、上下文编辑器和术语表管理
- 🔗 集成 i18next、React、Vue、Angular、Next.js 等框架
- 💰 按月固定定价，无按席位或按字数收费的意外
- 🔒 支持多租户、版本管理和客户特定翻译覆盖
- 🧠 可通过 MCP 服务器连接 AI 助手（如 Claude、Cursor）管理翻译
- ⏱️ 10 分钟内即可上手，提供 14 天免费试用，无需信用卡

---

### [<Suspense> – React](https://react.dev/reference/react/Suspense#what-activates-a-suspense-boundary)

**原文标题**: [<Suspense> – React](https://react.dev/reference/react/Suspense#what-activates-a-suspense-boundary)

<Suspense> 组件允许在子组件加载完成前显示备用内容，以优化用户体验。

- 📦 **核心功能**：通过 `fallback` 属性在子组件加载时显示占位内容，如加载动画或骨架屏
- ⏳ **触发加载状态**：当子组件使用 `lazy`、`use` 或流式服务器渲染时，Suspense 边界会激活
- 🔄 **统一显示**：同一 Suspense 边界内的所有组件会同时加载完成后再一起显示，避免碎片化
- 🪆 **嵌套加载序列**：通过嵌套多个 Suspense 边界，可实现内容的渐进式加载，提高感知性能
- 🕰️ **保留旧内容**：使用 `useDeferredValue` 或 `startTransition` 可在新数据加载时保持旧内容可见，避免界面闪烁
- 🚫 **防止内容隐藏**：通过 `startTransition` 标记非紧急更新，避免已显示内容被备用内容替换
- 🔑 **导航重置**：使用 `key` 属性可在导航到不同内容时重置 Suspense 边界，显示加载状态
- 🎨 **样式与字体等待**：Suspense 可等待样式表、字体和图片加载完成后再显示内容，确保视觉一致性
- 🖼️ **动画过渡**：与 `<ViewTransition>` 结合，可实现从备用内容到实际内容的平滑动画过渡
- ⚠️ **服务器错误处理**：服务器渲染错误时，Suspense 边界会显示备用内容，客户端再尝试重新渲染

---

### [Aurora Scharff 在 X 平台："我一直在编写 React Suspense 文档：现在有一份完整的列表，列出了哪些情况会触发 Suspense 边界，并为每个触发条件提供了实时示例！

感谢 @sebsilbermann 和 Dan Abramov 的审阅！

https://t.co/nblR4BcgHr

下方演示 ↓" / X](https://x.com/aurorascharff/status/2075222218099876260)

**原文标题**: [Aurora Scharff on X: "I've been working on the React Suspense docs: there's now a full list of what activates a Suspense boundary, with a live example for each trigger!

Thank you @sebsilbermann and Dan Abramov for reviews!

https://t.co/nblR4BcgHr

Demos below ↓" / X](https://x.com/aurorascharff/status/2075222218099876260)

概述摘要  
- 🚀 作者正在完善React Suspense文档，新增了触发Suspense边界的完整列表及每个触发的实时示例。  
- 🙏 感谢@sebsilbermann和Dan Abramov的审阅支持。  
- 📄 文档链接：react.dev/reference/react/Suspense  
- 📊 推文数据：2026年7月9日发布，浏览量8.5K，获5条回复、12次转发、148个赞、63次收藏。

---

### [TypeScript 7.0 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

**原文标题**: [Announcing TypeScript 7.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

TypeScript 7.0 正式发布，这是一个用 Go 语言重写的原生版本，速度提升高达 10 倍，并带来了多项性能优化和新特性。

- 🚀 **性能大幅提升**：完整构建速度提升 8-12 倍，例如 VS Code 代码库从 125.7 秒降至 10.6 秒，内存占用也减少 6-26%。
- ⚡ **编辑器体验革新**：打开文件到显示错误的时间从 17.5 秒降至 1.3 秒，语言服务器崩溃减少 60% 以上，命令失败率降低 80%。
- 🔧 **并行化控制**：新增 `--checkers`（类型检查器数量）和 `--builders`（项目构建器数量）标志，可精细调整并行度，最高可实现 16.7 倍加速。
- 🛠️ **改进的监视模式**：基于 Parcel 文件监视器重写，提供更高效稳定的跨平台文件监控，显著降低资源消耗。
- 🔄 **与 6.0 兼容**：提供 `@typescript/typescript6` 包，支持与 6.0 版本并行运行，方便工具链过渡。
- 📝 **默认配置变更**：`strict` 默认开启，`module` 默认为 `esnext`，`target` 默认为最新稳定 ECMAScript 版本，`types` 默认为 `[]` 等。
- 🌐 **模板字面量类型改进**：现在正确保留 Unicode 码点，例如 `"😀abc"` 的推断结果从 `["\ud83d", "\ude00abc"]` 变为 `["😀", "abc"]`。
- 📄 **JavaScript 支持重构**：与 TypeScript 文件分析更加一致，移除了对 JSDoc 中某些特殊模式的支持。
- 🏢 **生产环境验证**：已在微软内部团队（Loop、Office、PowerBI 等）及外部公司（Bloomberg、Canva、Figma、Google 等）大规模测试，反馈积极。
- 🎯 **未来规划**：7.1 版本将推出新 API，并继续每 3-4 个月发布新功能版本。

---

### [Vercel 收购 Better Auth，加速开源身份验证发展](https://vercel.com/blog/vercel-acquires-better-auth)

**原文标题**: [Vercel acquires Better Auth to accelerate open source auth - Vercel](https://vercel.com/blog/vercel-acquires-better-auth)

概述总结
- 🔐 Vercel 收购了 Better Auth，这是一款开源的 TypeScript 身份验证库，每周 npm 下载量超过 470 万次，拥有 850 多名贡献者
- 👥 创始人 Bereket Engida 和核心团队加入 Vercel，继续开发 Better Auth 和代理身份功能
- 🌐 Better Auth 遵循“开放网络”理念：框架无关、可移植、开发者拥有认证控制权
- 🤖 代理身份功能允许每个代理拥有独立身份和可撤销权限，解决多代理场景下的权限控制问题
- 🚀 Better Auth 团队将在 Vercel 继续开发代理身份，并集成到 Vercel Connect 和 eve 中
- 📚 Better Auth 库保持免费、开源（MIT 协议），保留原名，团队继续以开放贡献模式领导开发

---

### [Better Auth：简介](https://flaviocopes.com/better-auth/)

**原文标题**: [Better Auth: an introduction](https://flaviocopes.com/better-auth/)

以下是您提供的文章摘要：

Better Auth 是一个 TypeScript 身份验证库，它运行在您的应用内部，并将用户数据存储在您自己的数据库中，与托管服务不同，它没有供应商锁定。

- 🔑 **核心概念**：Better Auth 分为服务器实例（处理身份验证逻辑并与数据库交互）和客户端（用于前端用户注册、登录和会话读取）。
- 🗄️ **数据库架构**：需要 `user`、`session`、`account` 和 `verification` 表，可通过 CLI 自动生成，支持 Drizzle 或 Prisma ORM。
- 🌐 **路由挂载**：通过一个 HTTP 处理程序挂载在 `/api/auth/*` 路由上，适用于 Next.js 等框架，并兼容 Fetch API 环境（Node、Bun、Deno、Cloudflare Workers）。
- 📱 **客户端使用**：使用 `createAuthClient()` 创建客户端，提供 `signUp.email`、`signIn.email`、`signIn.social` 和 `signOut` 等方法，会话通过安全 Cookie 管理。
- 👤 **会话读取**：客户端使用 `useSession` 钩子（React/Vue）实现响应式更新；服务器端通过 `auth.api.getSession` 读取请求头中的 Cookie。
- 🧩 **插件扩展**：支持双因素认证、魔法链接、密钥、组织和团队等功能作为插件添加，保持核心简洁。
- 💡 **作者建议**：对于新的 TypeScript 项目且拥有自己数据库的情况，建议优先尝试 Better Auth，而非托管服务，以获得便利性和用户数据所有权。

---

### [Reddit - 请等待验证](https://www.reddit.com/r/reactjs/comments/1uqqy52/whats_one_react_pattern_you_stopped_using_after/)

**原文标题**: [Reddit - Please wait for verification](https://www.reddit.com/r/reactjs/comments/1uqqy52/whats_one_react_pattern_you_stopped_using_after/)

概述摘要  
- 📚 文章核心内容为对给定文本的概括与提炼  
- ✍️ 要求使用“-”符号列出要点，并配以表情符号  
- 🎯 需提取关键信息，精准传达文章主旨  
- 🔍 每个要点前需选择合适表情符号增强表达  
- 📝 顶部需添加无标题的概述摘要（使用ZH语言）

---

### [React 导航](https://reactnavigation.org/)

**原文标题**: [React Navigation](https://reactnavigation.org/)

React Navigation 是一个专为 React Native 和 Web 应用设计的路由和导航解决方案，提供易用、可定制且跨平台的导航功能。

- ✨ 支持 React Navigation 8.0 版本，并发布七月进度报告
- 📱 提供内置导航器，可快速实现 iOS 和 Android 平台的原生外观与流畅动画
- 🎨 完全可定制，开发者可使用 JavaScript 自定义导航的任意部分
- 🔧 扩展性强，支持编写自定义导航器或替换用户界面 API
- 💜 依赖社区支持，感谢 Software Mansion、Callstack、Expo 等贡献者和赞助商
- 🌐 基于 Docusaurus、GitHub Pages 和 Netlify 构建，提供文档、博客和帮助资源

---

### [React Navigation 8.0 - 七月进展报告 | React Navigation](https://reactnavigation.org/blog/2026/07/08/react-navigation-8.0-july-progress/)

**原文标题**: [React Navigation 8.0 - July Progress Report | React Navigation](https://reactnavigation.org/blog/2026/07/08/react-navigation-8.0-july-progress/)

React Navigation 8.0 七月进度报告概述了自2026年3月以来发布的多项改进和新功能。

- 📱 **最低依赖版本更新**：现在需要 react-native-screens 4.25.0+、react-native-gesture-handler 3.0.0+ 和 TypeScript 6.0.0+。
- 🔄 **支持 Suspense 的导航**：导航状态更新兼容并发渲染，用户发起的导航使用过渡，可中断且避免不必要的加载指示器。
- 🧪 **实验性数据加载器**：屏幕支持 `UNSTABLE_loader` 属性，用于在渲染前预取数据，支持嵌套导航并行加载，兼容现有数据获取库。
- 🎯 **动态导航器的类型化钩子**：`useNavigation` 和 `useNavigationState` 现在能识别所在导航器及其父导航器类型，减少样板代码。
- 🛠️ **简化自定义导航器类型**：自定义导航器工厂的类型定义更简洁，使用 `NavigatorTypeBagBase` 接口和 `createNavigatorFactory`。
- 🔗 **深度链接共享路径**：同一屏幕可在多个导航器中使用相同路径，React Navigation 根据用户位置自动导航。
- ⚡ **改进的堆栈导航器预加载**：预加载屏幕现在作为常规屏幕渲染，支持事件、参数更新和嵌套导航器，重复预加载会更新而非添加。
- 💾 **堆栈导航器屏幕保留**：屏幕可标记为保留（`retain(true)`），导航离开后仍保持渲染状态，适用于重屏幕或媒体播放场景。
- 🎨 **静态配置的动态属性**：新增 `with` 方法，允许基于动态状态（如屏幕尺寸）配置导航器属性，已回溯至 React Navigation 7。
- 🖌️ **Material 3 设计更新**：Material Top Tabs 和 Tab View 默认使用 Material Design 3 主色变体，指示器支持圆角等新设计。
- 🔣 **SF Symbols 内容过渡**：`SFSymbol` 组件支持 `contentTransition` 属性，在 iOS 17+ 上实现符号切换动画。
- 🌐 **流式服务器渲染支持**：服务器渲染现支持 `renderToPipeableStream` API，实现 HTML 流式传输。
- 📦 **标准导航库作者 API**：推出 `createStandardNavigator`，使自定义导航器能同时兼容 React Navigation 和 Expo Router，已回溯至 React Navigation 7。
- 🤖 **升级和迁移的 Agent 技能**：发布技能包用于从 6.x 升级到 7.x、7.x 到 8.x，以及动态到静态配置迁移。
- 🚀 **未来计划**：`@react-navigation/native-stack` 将使用下一版 react-native-screens，计划发布测试版。
- 🧪 **尝试最新版本**：可通过 `next` 标签安装，并欢迎在 GitHub 上反馈问题或建议。

---

### [RFC：路由处理器中的 WebSocket 升级 · vercel/next.js · 讨论 #95514 · GitHub](https://github.com/vercel/next.js/discussions/95514)

**原文标题**: [RFC: WebSocket Upgrades in Route Handlers · vercel/next.js · Discussion #95514 · GitHub](https://github.com/vercel/next.js/discussions/95514)

该RFC提案为Next.js App Router的路由处理器添加原生WebSocket支持，通过`NextResponse.upgrade()` API实现。

- 📜 **核心提案**：在App Router路由处理器中通过`NextResponse.upgrade()`实现WebSocket支持，允许在握手前检查请求、返回普通HTTP响应或接受升级。
- ⚙️ **API设计**：`NextResponse.upgrade()`接受包含`open`、`message`、`close`、`error`生命周期钩子的对象，返回携带钩子和响应头的框架响应。
- 🔗 **CrossWS集成**：每个路由模块拥有共享的CrossWS Node适配器，提供`send()`、`close()`、`subscribe()`、`publish()`等高级API，消息支持文本、二进制和JSON序列化。
- 🛡️ **安全与认证**：支持在握手前进行身份验证和授权，可返回401/403等HTTP响应，并设置响应头和Cookie。
- 🚀 **部署支持**：支持`next dev`、`next start`、独立输出和兼容适配器，但Edge运行时和静态导出不支持。
- ⚠️ **限制与注意事项**：连接生命周期钩子错误无法转为HTTP响应，静态生成和缓存不可用，初始版本不支持子协议选择、压缩配置和原始`ws`对象暴露。
- 🔄 **路由与代理**：升级请求遵循现有路由顺序，`proxy.ts`可处理、重写或拒绝握手，内部WebSocket路径优先于应用路由。
- 🛠️ **适配器行为**：完整Node.js服务器适配器自动支持，单个路由输出适配器需调用生成的`upgradeHandler`，不支持原始升级原语的适配器需通过`modifyConfig`禁用功能。
- 📊 **测试计划**：包括端到端测试、开发/生产模式验证、Turbopack/webpack支持、独立输出、各种响应场景、生命周期钩子、路由隔离、优雅关闭等。

---

### [React表单的正确做法 | 技能提升](https://upskills.dev/tutorials/react-forms-done-right)

**原文标题**: [React Forms Done Right | Upskills](https://upskills.dev/tutorials/react-forms-done-right)

概述总结
- 🎓 提供技能提升（Upskills）相关的教程与展示内容
- 🛠️ 包含实用工具资源，支持用户学习与创作
- 🇬🇧 网站支持多语言切换（以英国国旗标识）
- 🌗 提供主题切换功能（亮色/暗色模式）
- 🔑 用户可通过“登录”按钮访问个性化功能
- 📜 版权声明显示为2026年，并包含隐私政策与服务条款
- 💬 提供Discord和X（原Twitter）社群链接用于交流

---

### [Kotlin 多平台 vs React Native（2026 基准测试）](https://swmansion.com/blog/we-built-the-same-app-in-kmp-and-react-native-here-s-what-we-found/)

**原文标题**: [Kotlin Multiplatform vs React Native (2026 Benchmark)](https://swmansion.com/blog/we-built-the-same-app-in-kmp-and-react-native-here-s-what-we-found/)

本文通过构建相同的应用，比较了 Kotlin Multiplatform (KMP) 和 React Native (RN) 在 Android 和 iOS 上的性能差异，发现两者各有优劣，没有完美的框架。

- 📱 **应用大小对比**：Android 上 KMP 比 RN 小约 8 倍（2 MB vs 15.8 MB），iOS 上两者接近，RN 略小 1.3 MB。
- ⏱️ **启动时间**：Android 上 KMP 比 RN 快 2-4 倍；iOS 上两者几乎持平，现代设备差异仅 20-28 毫秒。
- 🧠 **内存使用**：Android 上 KMP 内存约为 RN 的一半；iOS 上 RN 内存比 KMP 少 3-4 倍，因使用原生 UIKit。
- 🔋 **CPU 使用**：两者在 Android 和 iOS 上均无明显优势，结果受设备和测试细节影响。
- 💡 **Flashlight 测试（仅 Android）**：整体得分相近，但 KMP 在 RAM 和 CPU 上更优，RN 的 CPU 峰值主要来自启动阶段。
- 🏆 **结论**：Android 上 KMP 全面领先（除 CPU），iOS 上两者平衡，RN 在内存上胜出。选择应基于团队和产品需求。

---

### [Cloudflare Workers 与 Hyperdrive 结合 TanStack Start – Master.dev 博客](https://master.dev/blog/cloudflare-workers-and-hyperdrive-with-tanstack-start/)

**原文标题**: [Cloudflare Workers and Hyperdrive with TanStack Start – Master.dev Blog](https://master.dev/blog/cloudflare-workers-and-hyperdrive-with-tanstack-start/)

本文介绍了如何在 Cloudflare Workers 上使用 Hyperdrive 和 TanStack Start 高效连接数据库，并解决了性能与请求清理问题。

- 🌐 **Cloudflare Workers 与数据库连接挑战**：直接连接数据库会导致性能下降和连接数过多，因为每个 Worker 实例会建立新连接。
- ⚡ **Hyperdrive 解决方案**：Cloudflare 的 Hyperdrive 提供预热的连接池，作为数据库代理，减少延迟和连接数。
- 🛠️ **正确配置 Hyperdrive**：在 Wrangler 文件中添加 Hyperdrive 绑定，并通过 `env.HYPERDRIVE.connectionString` 连接，同时设置本地开发环境变量。
- 🔄 **请求级连接管理**：使用 TanStack Start 的全局请求中间件，在每个请求中创建新的数据库对象，避免 I/O 资源跨请求持久化。
- 📍 **区域优化**：将 Cloudflare 应用部署在与数据库相同的区域（如 `aws:us-east-1`），可显著降低查询延迟（从 80ms 降至 7ms）。
- 📚 **实践步骤**：包括安装 Drizzle ORM、配置 `drizzle.config.ts`、生成 schema，以及通过中间件将 `db` 对象注入上下文供服务器函数使用。

---

### [用氛围重写我的博客 | Swizec Teller](https://swizec.com/blog/using-vibes-to-rewrite-my-blog/)

**原文标题**: [Using vibes to rewrite my blog | Swizec Teller](https://swizec.com/blog/using-vibes-to-rewrite-my-blog/)

### 概述总结
作者分享了他使用AI辅助工具（如Claude和Codex）以及新框架TimberJS重写个人博客的过程，强调“工程之死”被夸大，开发者仍需具备核心判断力。

- 📝 **博客重写背景**：旧博客基于Gatsby，部署一篇新文章需45分钟以上，导致长期拖延和内容衰退。
- 🚀 **新框架TimberJS**：基于React Server Components，部署时间缩短至3分钟，支持MDX文件、自动生成OpenGraph图像，并实现服务端代码高亮。
- 👶 **育儿与工作效率**：利用育儿间隙（如抱婴儿时）通过AI工具进行短时高效工作，无需长时间专注。
- 🤖 **AI辅助编程体验**：尝试“vibes”方法（AI自主循环），但发现AI易陷入死循环或错误假设，需人工监控和引导。
- 🧠 **开发者必备能力**：必须明确解决方案的“形状”，并识别AI何时陷入困境，避免盲目信任其输出。
- ⚠️ **AI局限性案例**：AI曾花30分钟循环调试，甚至试图读取`node_modules`代码，凸显人工判断的重要性。

---

### [SolidJS 2.0：React开发者对信号与异步的初探 | Dennis Morello](https://morello.dev/blog/solidjs-2-react-developers-first-look)

**原文标题**: [SolidJS 2.0: A React Developer's First Look at Signals and Async | Dennis Morello](https://morello.dev/blog/solidjs-2-react-developers-first-look)

SolidJS 2.0 是基於細粒度響應式的前端框架，專為 React 開發者介紹其信號（Signals）與非同步（Async）核心特性，並比較兩者差異。

- 🔍 **核心差異**：Solid 組件只執行一次，狀態變化直接更新 DOM 節點，無需虛擬 DOM 或依賴陣列；React 則需重新渲染整個組件。
- ⚡ **信號機制**：`count()` 是函數調用而非值，讀取時自動訂閱變化，消除閉包過時與依賴陣列 bug。
- 🌐 **原生非同步**：2.0 版支援 promise 直接流入響應式圖，用 `<Loading>` 取代 `<Suspense>`，區分「初始載入」與「刷新中」狀態。
- 🔄 **突變操作**：提供 `action`、`createOptimistic` 與 `refresh`，支援樂觀更新與服務器數據同步，與 React 19 的 Actions 趨同。
- ⏳ **確定性批處理**：寫入在微任務中批量處理，讀取需等待批次刷新，可調用 `flush()` 強制同步更新。
- 🏷️ **API 更名**：`<Suspense>` → `<Loading>`，`createEffect` 拆分為追蹤與執行兩階段，`onMount` → `onSettled`，`<Index>` → `<For keyed={false}>` 等。
- 📡 **信號標準化**：TC39 信號提案處於 Stage 1，Solid 影響但未直接實現，Svelte 5 已採用類似模式。
- 🤔 **實用建議**：目前仍是 beta 版，生態較小，但值得 React 開發者花時間學習，體驗無需過度警覺的開發方式。

---

### [首页 | React 谷歌地图](https://visgl.github.io/react-google-maps/)

**原文标题**: [Home | React Google Maps](https://visgl.github.io/react-google-maps/)

该页面介绍了 react-google-maps 库，用于在 React 应用中集成 Google Maps JavaScript API。

- 🗺️ 提供 React 组件和钩子，可轻松集成 Google Maps 功能
- ⚙️ 支持将 Google 地图作为完全受控的响应式组件使用
- 🔧 包含可扩展的组件和钩子，便于编写自定义功能
- 🌐 属于 vis.gl 框架套件，可配合 deck.gl 等实现高性能 WebGL 可视化
- 📚 提供 API 参考文档和入门模板资源
- 🔗 可与其他 vis.gl 库（如 deck.gl、luma.gl）协同使用

---

### [GitHub - cloudflare/vinext: 重新实现Next.js API接口的Vite插件——可部署至任何环境 · GitHub](https://github.com/cloudflare/vinext)

**原文标题**: [GitHub - cloudflare/vinext: Vite plugin that reimplements the Next.js API surface — deploy anywhere · GitHub](https://github.com/cloudflare/vinext)

vinext 是一个基于 Vite 的 Next.js API 重实现，主要部署目标为 Cloudflare Workers。

- 🚀 **核心功能**：在 Vite 上重写 Next.js API，支持 App Router、Pages Router、React Server Components、Server Actions、中间件、路由处理器、ISR 和静态导出。
- ☁️ **部署目标**：原生支持 Cloudflare Workers，通过 Nitro 插件可部署到 Vercel、Netlify、AWS 等平台。
- ⚡ **快速上手**：使用 `create-vinext-app` 创建新项目，或通过 `vinext init` 一键迁移现有 Next.js 项目，同时保留原有配置。
- ✅ **项目状态**：支持约 94% 的 Next.js 16 API，但尚未完全覆盖所有生产工作负载，特别是较新的 App Router 功能。
- 🧪 **测试与验证**：拥有超过 1,700 个 Vitest 测试和 380 个 Playwright E2E 测试，并集成 Vercel 的 App Router Playground 作为集成测试。
- 🎯 **设计原则**：追求实用兼容性而非逐行复刻，仅支持最新 Next.js 版本，支持渐进式采用。
- 📦 **CLI 工具**：提供 `dev`、`build`、`start`、`deploy`、`init`、`check`、`lint` 等命令，支持 Cloudflare Workers 一键部署。
- 🔧 **缓存系统**：可插拔缓存，支持内存缓存和 Cloudflare KV 缓存适配器，可在 Vite 配置中声明。
- 📊 **性能基准**：相比 Next.js (Turbopack)，vinext (Vite 8) 在构建速度和客户端包体积上通常更优。
- 🏗️ **架构**：作为 Vite 插件运行，重写 `next/*` 导入，构建文件系统路由器，并与 `@vitejs/plugin-rsc` 集成处理 React Server Components。

---

### [我们如何在一周内用AI重建了Next.js](https://blog.cloudflare.com/vinext/)

**原文标题**: [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)

### 概述总结
一位工程师与AI模型在一周内从零重建了Next.js，创建了基于Vite的替代品vinext，可部署到Cloudflare Workers，构建速度提升4倍，客户端包体积缩小57%。

- ⚡ **核心成果**：vinext作为Next.js的即插即用替代品，构建速度最高提升4.4倍，客户端包体积缩小57%，成本仅约1100美元。
- 🛠️ **解决部署难题**：通过直接基于Vite重建API（路由、RSC、服务端操作等），避免逆向工程Next.js输出，支持Cloudflare Workers一键部署。
- 📊 **性能对比**：在33路由的App Router测试中，vinext（Vite 8/Rolldown）构建时间1.67秒（Next.js 7.38秒），客户端包体积72.9KB（Next.js 168.9KB）。
- ☁️ **部署优势**：`vinext deploy`命令自动构建并部署到Workers，支持KV缓存实现ISR，兼容App Router和Pages Router。
- 🤖 **AI驱动开发**：利用Claude API生成代码，配合1700+单元测试和380个E2E测试确保质量，800多次会话完成开发。
- 🧩 **技术架构**：基于Vite插件系统实现，95%代码与平台无关，支持多供应商部署（如Vercel），测试覆盖Next.js 16 API的94%。
- 🔄 **创新功能**：实验性“流量感知预渲染”（TPR）根据实际访问数据智能预渲染热门页面，避免全量构建。
- ⚠️ **实验状态**：目前不支持构建时静态预渲染，但已用于生产环境（如CIO.gov），建议谨慎评估后使用。
- 🔮 **行业影响**：AI能直接根据规范和基础工具生成代码，可能减少中间抽象层，改变软件构建模式。

---

### [发布 v2.0.0 · unlayer/react-email-editor · GitHub](https://github.com/unlayer/react-email-editor/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · unlayer/react-email-editor · GitHub](https://github.com/unlayer/react-email-editor/releases/tag/v2.0.0)

以下是您提供的GitHub发布说明的摘要：

概述摘要  
- 📦 **版本升级**：v2.0.0 发布，组件API不变，React 16.8+ 用户可无缝升级。  
- 🔧 **重大变更**：最低要求 React 16.8+（原15+）、Node 18+（原10+），不再支持深层导入。  
- 🚫 **破坏性改动**：编辑器在卸载时销毁，修复了闭包泄漏问题；发布代码从ES5升级为ES2019。  
- ✨ **新增功能**：原生ESM构建（支持`import`）、Next.js App Router的`'use client'`指令、事件监听器正确重新注册。  
- 🛠 **工具链迁移**：构建工具从tsdx改为tsup，测试从Jest改为Vitest，CI覆盖React 16/17/18/19和Node 20/22/24。  
- 📄 **依赖调整**：`@unlayer/types` 从`latest`改为版本范围锁定。

---

### [React邮件编辑器演示](https://react-email-editor-demo.netlify.app/)

**原文标题**: [React Email Editor Playground](https://react-email-editor-demo.netlify.app/)

概述摘要  
- 📚 本文探讨了人工智能在医疗诊断中的应用，强调其提升准确性和效率的潜力。  
- 🩺 通过分析大量医学影像数据，AI能辅助医生快速识别疾病，如癌症和心血管问题。  
- ⚠️ 然而，AI系统面临数据隐私、算法偏见和监管挑战，需要谨慎部署。  
- 🤝 人机协作是关键，AI应作为工具增强而非替代医生的专业判断。  
- 🌍 未来需加强跨学科合作，制定伦理标准，以推动AI在医疗中的安全应用。

---

### [react-easy-crop](https://valentinh.github.io/react-easy-crop/)

**原文标题**: [react-easy-crop](https://valentinh.github.io/react-easy-crop/)

概述总结
- 🖼️ 支持缩放、旋转和基础裁剪功能
- 🔍 提供最小的实用设置，包含裁剪和缩放状态
- ✂️ 通过onCropComplete返回的像素裁剪输出结果
- 📤 用户可选择图片进行裁剪并上传

---

### [宣布 Vite+ Beta 版 | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-beta)

**原文标题**: [Announcing Vite+ Beta | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-beta)

Vite+ 现已进入Beta阶段，它统一了Web项目所需的运行时、包管理器和前端工具，提供一致且高效的工作流程。该工具链完全开源，框架无关，适用于各类Web项目。

- 🚀 **统一工具链**：Vite+整合了Vite、Vitest、Rolldown、tsdown、Oxlint和Oxfmt，并提供内置任务运行器，作为单一入口点简化开发流程。
- ⚡ **一致的工作流**：通过`vp dev`、`vp check`、`vp test`、`vp build`、`vp pack`和`vp run`等命令，开发者可在不同项目中获得统一体验。
- 🛠️ **智能缓存与迁移**：`vp run`结合自动数据跟踪和Vite元数据实现智能缓存；`vp migrate`支持多种应用设置和代理迁移。
- 🌍 **跨平台与企业支持**：已强化跨操作系统和Shell的兼容性，并提供组织模板和代理感知HTTP功能，满足企业需求。
- 📈 **社区与采用**：已有超过1300个公共仓库依赖Vite+，包括Dify、critical、BlockNote等项目，社区贡献超过500个拉取请求。
- 🎯 **1.0路线图**：未来将聚焦远程缓存、GitLab CI/CD支持、框架兼容性改进、更多迁移目标及文档优化。
- 🔧 **快速上手**：通过curl或PowerShell命令安装`vp`，然后使用`vp create`或`vp migrate`开始使用。

---

### [发布版本 7.81.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.81.0)

**原文标题**: [Release Version 7.81.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.81.0)

该页面是 react-hook-form 库的 GitHub 发布页面，展示了 v7.81.0 版本的更新内容。

- ⚜️ 新增功能：FieldArray 组件，支持通过 render prop 渲染字段数组
- 🐞 修复：useFieldArray 中 min 1 项验证错误在 errors 对象中的位置变化问题
- 🐞 修复：调用 reset 时触发 subscribe 使用最新名称而非 undefined
- 🐞 修复：useController 中清除父对象后受控字段的反映问题
- 🐞 修复：flatten 函数中保留 Date 值作为叶节点
- 🐛 修复：unset 函数防止原型关键字路径遍历的安全问题
- 🏸 改进：setValue API 支持收缩值功能
- 👝 优化：useFieldArray reset 时减少重新渲染次数
- 🐞 修复：clearErrors 改变 form.subscribe 中 name 值的问题

---

### [发布 0.87.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.87.0-rc.0)

**原文标题**: [Release 0.87.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.87.0-rc.0)

React Native 发布了 v0.87.0-rc.0 候选版本，但页面加载出现错误，需重新加载。

- ⚠️ 此版本为候选版，不建议用于生产环境
- 📦 安装命令：`npm install react-native@0.87.0-rc.0`
- 🐞 问题报告地址：https://github.com/react/react-native/issues
- 🔄 页面加载时出现错误，提示“请重新加载此页面”
- 📊 社区反应积极，获得 10 个赞、7 个火箭表情等多项互动

---

### [react-router/CHANGELOG.md 在 main 分支上 · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v820)

**原文标题**: [react-router/CHANGELOG.md at main · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v820)

该页面显示 React Router 仓库的 CHANGELOG.md 文件加载出错。

- ❌ 页面加载时出现错误，提示“Uh oh! There was an error while loading. Please reload this page.”
- 📂 页面内容指向 `react-router` 仓库的 `CHANGELOG.md` 文件，位于 `main` 分支。
- 🔢 该文件包含 3528 行代码，约 228 KB 大小，记录了版本变更历史。
- 🔧 页面提供了代码浏览、编辑、历史查看等操作选项，但当前无法正常显示内容。
- 🛠️ 建议用户重新加载页面以尝试解决问题。

---

### [无](https://expo.dev/blog/how-to-apply-professional-design-principles-in-ai-app-development?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [None](https://expo.dev/blog/how-to-apply-professional-design-principles-in-ai-app-development?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

概述摘要：本文探讨了人工智能在医疗领域的应用，重点介绍了AI辅助诊断、个性化治疗方案和药物研发中的突破，同时指出了数据隐私和伦理挑战。

- 🏥 AI辅助诊断系统通过分析医学影像，提高了疾病检测的准确性和效率。
- 💊 个性化治疗利用AI分析患者基因数据，定制更有效的治疗方案。
- 🔬 药物研发中，AI加速了候选药物的筛选和临床试验设计。
- 🔒 数据隐私问题成为AI医疗应用的主要障碍，需加强法规保护。
- ⚖️ 伦理挑战包括算法偏见和医生与AI的责任划分。

---

### [joint/packages/joint-react 在 master 分支 · clientIO/joint · GitHub](https://github.com/clientIO/joint/tree/master/packages/joint-react#readme)

**原文标题**: [joint/packages/joint-react at master · clientIO/joint · GitHub](https://github.com/clientIO/joint/tree/master/packages/joint-react#readme)

这是一个用于React的JointJS库的README文档，介绍了其功能、用法和适用场景。

- 🚀 **快速入门**：通过`GraphProvider`、`Paper`和`HTMLBox`组件，几行代码即可创建带节点和链接的交互式图表。
- 🧩 **真实数据模型**：提供可序列化的图形数据结构，支持查询、转换和持久化，适合复杂状态管理。
- 🎨 **完全控制**：开发者可自定义形状、端口、链接、路由和交互行为，灵活掌控渲染和交互细节。
- ⚡ **生产级用户体验**：内置连接吸附、避障路由、元素/链接工具和高亮器等特性，无需额外开发。
- 📈 **大规模性能**：支持数千节点的平滑交互，适用于大规模图表应用。
- 🛠️ **安装与依赖**：通过`npm install @joint/react`安装，需React 18或19作为对等依赖。
- 💼 **适用场景**：覆盖工作流、AI管道、BPMN、数据建模、UML、SCADA、能源网络、电子设计、组织架构图和时间线等多个领域。
- 🤖 **AI辅助开发**：提供MCP服务器，支持AI编码代理（如Claude Code）搜索官方文档和示例，提升开发效率。
- 💰 **商业版本**：JointJS+ for React提供高级插件（如模板、工具栏、撤销/重做等）和专业支持，可免费试用30天。
- 📜 **许可证**：基于Mozilla Public License 2.0开源，版权归client IO所有。

---

### [Geist Pixel - Google 字体](https://fonts.google.com/specimen/Geist+Pixel?preview.script=Latn)

**原文标题**: [Geist Pixel - Google Fonts](https://fonts.google.com/specimen/Geist+Pixel?preview.script=Latn)

概述总结  
- 📰 文章讨论了气候变化对全球农业的影响，指出极端天气事件导致作物减产，威胁粮食安全。  
- 🌾 重点提到干旱和洪水频发，破坏了主要产粮区，如美国中西部和印度平原。  
- 🌍 强调发展中国家受影响最严重，因缺乏适应气候变化的资源和基础设施。  
- 💡 提出解决方案包括推广耐旱作物品种、改进灌溉技术以及加强国际合作。  
- ⚠️ 警告如果不采取行动，到2050年全球粮食产量可能下降30%，引发社会动荡。

---

### [npm 安装时安全性与GAT绕过双因素认证弃用 - GitHub 变更日志](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/)

**原文标题**: [npm install-time security and GAT bypass2fa deprecation - GitHub Changelog](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/)

npm v12 发布，引入安装时安全默认设置并弃用2FA绕过功能。

- 🔒 安装时安全默认设置已启用：`allowScripts`默认关闭，`--allow-git`和`--allow-remote`默认设为`none`，依赖生命周期脚本和Git/远程URL依赖需明确允许。
- 📋 准备迁移：在npm 11.16.0+中可预览警告，使用`npm approve-scripts`审查并批准信任的脚本。
- 🚫 2FA绕过GAT将停止跳过2FA：2026年8月起，配置为绕过2FA的令牌无法执行敏感账户、包和组织管理操作。
- 📦 2FA绕过令牌无法直接发布：2027年1月起，此类令牌仅能读取私有包和暂存发布，需人工2FA批准。
- 🔄 建议迁移方案：转向受信发布（OIDC）或暂存发布，结合人工审批步骤，替代长期有效的发布令牌。

---

### [npm v12 默认关闭安装脚本，开始...](https://socket.dev/blog/npm-12)

**原文标题**: [npm v12 Ships With Install Scripts Off by Default, Begins De...](https://socket.dev/blog/npm-12)

概述总结：恶意NuGet包通过伪装成Braintree SDK，窃取信用卡数据、商户API密钥及主机机密信息，威胁生产环境应用安全。

- 🔍 恶意包利用拼写错误模仿Braintree SDK，诱骗开发者安装
- 💳 窃取实时支付卡数据，包括信用卡号、有效期等敏感信息
- 🔑 盗取商户API密钥，导致支付系统被非法控制
- 🖥️ 获取主机机密信息，可能进一步渗透生产环境
- ⚠️ 攻击目标明确针对.NET开发者和使用Braintree的应用程序

---

### [用Rust重写Bun | Bun博客](https://bun.com/blog/bun-in-rust)

**原文标题**: [Rewriting Bun in Rust | Bun Blog](https://bun.com/blog/bun-in-rust)

Bun 项目从 Zig 语言重写为 Rust 语言，通过 AI 辅助在 11 天内完成了原本需要一年的人工工作量，显著提升了稳定性和性能。

- 🚀 **项目起源**：Bun 始于 2021 年用 Zig 语言编写，最初是 esbuild 的逐行移植，一年内从零构建了包含 JavaScript/TypeScript 转译器、包管理器、测试运行器等庞大功能集。
- 🐛 **稳定性挑战**：Zig 的手动内存管理导致大量 use-after-free、内存泄漏和 double-free 错误，仅 v1.3.14 就修复了 15 个以上此类严重 bug。
- 🔄 **重写决策**：团队评估了 C++ 和 Zig 方案后，选择 Rust 因其编译器能自动捕获内存错误（如 use-after-free），且 RAII 机制通过 `Drop` 自动清理资源。
- 🤖 **AI 辅助流程**：使用 Claude Code 动态工作流，64 个 Claude 实例并行运行，通过“实现者 + 2 个对抗性审查者”的循环机制，每小时最高产出 695 次提交。
- 📊 **惊人数据**：11 天内产生 6,502 次提交，消耗 59 亿输入 token 和 6.9 亿输出 token，API 成本约 16.5 万美元，但避免了 3 名工程师一年的冻结开发期。
- ✅ **质量保障**：对抗性审查在合并前捕获了 3 个关键 bug（如异步 close 导致 use-after-free、负时间戳 nsec 无效、unwrap_or 急切求值 panic），最终 6 个平台全部通过测试。
- 📈 **性能提升**：HTTP 吞吐量提升 2.8%-4.8%，二进制体积缩小约 20%（Linux 从 88MB 降至 70MB），内存泄漏全面修复（如 `Bun.build()` 循环从 6.7GB 降至 609MB）。
- 🔧 **持续改进**：重写后新增 24/7 模糊测试、Miri 检查和 LeakSanitizer，4% 的代码在 `unsafe` 块中，计划逐步重构为更地道的 Rust 代码。

---

### [如何发起Ruby聚会 | RubyEvents指南](https://guides.rubyevents.org/meetups/)

**原文标题**: [How to Start a Ruby Meetup | RubyEvents Guides](https://guides.rubyevents.org/meetups/)

以下是您提供的文章摘要，涵盖从创办到维持Ruby聚会的关键步骤和要点。

概述摘要
本文提供了创办和维持本地Ruby聚会的实用指南，涵盖从寻找场地到长期运营的各个方面，强调社区建设、持续性和乐趣。

- 🎯 **为何要办聚会**：Ruby不仅是语言，更是社区。聚会能激发初级开发者、促成工作机会，并解决技术难题，这些是线上无法替代的。
- 🏁 **从零开始**：首次聚会最难，只需做到最低限度：确定场地（公司办公室、大学或共享空间）、创建活动页面（使用Luma或Meetup.com），并直接告知认识的人。即使只有5人参加也是好的开始。
- 📋 **确定形式**：最常见的格式是2-3场演讲加社交时间。备选方案包括黑客之夜、工作坊或纯社交聚会。演讲宜短，社交是留住人的关键。
- 📢 **宣传推广**：最有效的方式是直接邀请（如通过LinkedIn）。持续发布公告（报名开放、确认演讲者、活动当天），保持固定频率（如每月一次），并依靠口碑传播。
- 🎤 **演讲者与话题**：直接邀请有有趣项目的人，而非发布公开征集。闪电演讲（10-15分钟）适合新手，能降低门槛并培养未来会议演讲者。
- 💰 **资金与赞助**：多数聚会不需要太多资金。食物和饮料是主要开销，可通过单一赞助商（如场地提供方）换取开场提及。可使用usingrails.com寻找本地Ruby公司。
- 🏃 **活动执行**：确保投影仪可用（备好适配器），帮助参与者找到地点，使用姓名标签促进交流，并准时开始（10分钟内）。尊重时间能体现组织性。
- 🌱 **建立文化**：文化由行为塑造，而非书面规定。明确行为准则，欢迎新人，并以身作则（如尊重演讲者、感谢幕后贡献者）。这能营造包容氛围。
- 😊 **保持乐趣**：组织者倦怠是常见问题。最佳预防是找一位共同组织者分担工作。定期变换形式（如改为黑客之夜或添加节日元素）能保持自己和参与者的兴趣。
- 📈 **成长与演变**：聚会不一定要增长，稳定的20人聚会比百人但只办两次的更有价值。与Ruby Central等全球组织联系，可获取资源和支持。当准备退出时，应顺利交接给已参与组织工作的继任者。

---

### [为Web开发者介绍Safari MCP服务器 | WebKit](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

**原文标题**: [  Introducing the Safari MCP server for web developers | WebKit](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

Safari MCP 服务器为网页开发者推出，通过连接代理到Safari浏览器窗口，让代理能直接查看代码在浏览器中的实际渲染效果，从而加速调试流程。

- 🚀 提升调试效率：代理可直接访问DOM、网络请求、截图和控制台输出，减少窗口切换和重复提示。
- 🌐 增强Safari兼容性：代理可自动检查网站在Safari中的渲染、样式和布局，无需手动切换浏览器。
- ⚡ 分析性能瓶颈：代理能评估JavaScript性能指标，如导航和资源加载时间，精准定位问题。
- ♿ 检查可访问性：代理可检测缺失标签、ARIA属性错误和对比度问题，提升用户体验。
- ✅ 验证用户状态：代理能检查表单状态、元素交互和结账流程，减少手动测试。
- 🛠️ 提供丰富工具：包括控制台日志、截图、DOM交互、网络请求、视口设置等16种功能。
- 📦 快速开始：需安装Safari技术预览版，启用远程自动化，并通过Claude或Codex等代理配置。
- 🔒 本地运行安全：服务器完全在本地运行，不访问个人数据，截图和日志直接发送给代理。
- 💡 简化调试流程：只需简单提示如“在Safari中查找我网站的错误”，代理即可自主调试。

---

### [JS1024 - 年度JavaScript与着色器代码高尔夫大赛 - 主页](https://js1024.fun/#2026)

**原文标题**: [JS1024 - Annual Javascript & Shader Code Golfing Competition - Main Page](https://js1024.fun/#2026)

JS1024 是一年一度的 JavaScript 与 GLSL 代码体积竞赛，参赛者需在 1024 字节内创作程序，主题为“梦境”。

- 🎯 **竞赛核心**：参与者需在 15 天内用 JavaScript 或 GLSL 编写不超过 1024 字节的程序，主题为“梦境”。
- 📅 **关键时间**：7月1日公布主题并开放提交，7月19日截止，8月1日停止评分，8月5日左右公布结果。
- 📝 **提交规则**：代码体积不超过 1 KiB，禁止恶意代码、外部文件及提取用户数据；可选提交可读版本。
- 🏆 **评分机制**：参与者使用密钥对其他项目评分，按类别最高分决出名次。
- 🖥️ **演示类别**：包括经典 Canvas 模式、p5.js 演示、Shader 演示（WebGL1/GLSL ES 1.0）及无 shim 的空白 HTML 文件。
- 🔧 **工具与资源**：提供多种代码压缩工具（如 Terser、UglifyJS）及教程指南，帮助优化代码体积。
- 📚 **学习材料**：包含 JavaScript 高尔夫技巧、游戏开发教程、WebGL 指南及往届作品分析文章。
- 🎁 **捐赠与支持**：由 traian 创建，感谢 Frank Force、Evan Hahn 等捐赠者，并列出类似竞赛（如 js1k、js13kgames）。

---

