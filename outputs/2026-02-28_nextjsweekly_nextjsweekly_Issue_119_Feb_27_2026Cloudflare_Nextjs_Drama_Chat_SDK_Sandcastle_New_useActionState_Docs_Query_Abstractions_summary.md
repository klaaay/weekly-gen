### [我们如何在一周内用 AI 重建 Next.js](https://blog.cloudflare.com/vinext/)

**原文标题**: [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)

上周，一位工程师与 AI 模型在一周内从零重建了最流行的前端框架 Next.js，推出了基于 Vite 的替代品 vinext。它可一键部署至 Cloudflare Workers，生产构建速度提升最高 4 倍，客户端包体积缩小达 57%，且已有客户在生产环境中使用。整个项目仅消耗约 1100 美元的 AI 令牌成本。

- 🚀 **vinext 诞生**：基于 Vite 重建 Next.js API，实现无缝替换，支持一键部署至 Cloudflare Workers。
- ⚡ **性能提升**：生产构建速度最快提升 4.4 倍，客户端包体积减少 57%。
- 🔧 **部署简化**：无需适配器，直接利用 Vite 环境 API 兼容多平台，专注 Cloudflare Workers 集成。
- 🧩 **功能覆盖**：完整支持路由、服务端渲染、React 服务端组件、中间件等 Next.js 核心特性。
- 🧪 **实验阶段**：项目虽新，但已通过 1700+ 单元测试和 380+ 端到端测试，覆盖 94% 的 Next.js 16 API。
- 🤖 **AI 驱动开发**：借助 Claude 等 AI 模型，在测试套件和规范指导下高效完成代码编写与验证。
- 📊 **流量感知预渲染**：实验性功能，根据实际访问流量智能预渲染页面，优化构建效率。
- 🌐 **生态开放**：项目开源，欢迎其他平台贡献，旨在与多托管服务商合作推广。
- 🛠️ **迁移工具**：提供 AI 技能和命令行工具，支持现有 Next.js 项目快速迁移至 vinext。

---

### [定价 — 免费支持高达 5 万用户 | 月费从 0 美元起](https://clerk.com/pricing?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=pricing-rollout&utm_content=02-13-26&dub_id=7LidVrzIhznB66G0)

**原文标题**: [Pricing — Free Up to 50K Users | Plans from $0/mo](https://clerk.com/pricing?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=pricing-rollout&utm_content=02-13-26&dub_id=7LidVrzIhznB66G0)

Clerk 提供分层定价方案，支持无限应用，从免费到企业级，满足不同规模团队的需求，并提供 B2B 认证、管理和计费等附加功能。

- 🆓 **免费方案**：适合起步项目，包含 5 万月留存用户、3 个仪表板席位及基本认证功能，无需信用卡。
- 💼 **专业方案**：每月 20 美元起，增加多因素认证、企业连接、自定义会话时长等高级功能。
- 🏢 **商业方案**：每月 250 美元起，专为合规和成长团队设计，提供 SOC2 报告、增强角色和优先支持。
- 🏛️ **企业方案**：定制价格，包含高可用性 SLA、HIPAA 合规和专属迁移支持。
- 🔗 **附加功能**：B2B 认证、高级管理和集成计费服务，部分免费提供，增强版需额外付费。
- 📊 **清晰计价**：按实际使用量收费，提供阶梯折扣，数据可随时导出，支持初创公司通过合作伙伴获得优惠。

---

### [使用异步 React 构建具有动作属性的设计组件 | Aurora Scharff](https://aurorascharff.no/posts/building-design-components-with-action-props-using-async-react)

**原文标题**: [Building Design Components with Action Props using Async React | Aurora Scharff](https://aurorascharff.no/posts/building-design-components-with-action-props-using-async-react)

本文介绍了如何利用 Async React 的`useTransition`和`useOptimistic`钩子，通过“Action Props”模式构建具有乐观更新和加载状态管理的可复用 UI 组件（如 TabList 和 EditableText），从而提升异步操作时的用户体验，同时保持消费者代码的简洁性。

- 🚀 **Async React 核心**：基于 React Conf 2025 提出的 Async React 三层架构（异步设计、路由、数据），重点实践设计层，通过`useTransition`协调异步操作、`useOptimistic`管理乐观状态。
- 🔧 **Action Props 模式**：组件内部封装`useTransition`和`useOptimistic`，通过`action`属性接收异步函数，自动处理加载状态、乐观更新及错误回滚，消费者无需手动管理过渡状态。
- 📊 **TabList 组件示例**：通过添加`changeAction`属性、`useOptimistic`实现标签即时切换，并内置加载指示器（如旋转图标），提升用户交互反馈。
- ✏️ **EditableText 组件示例**：支持内联编辑的文本字段，利用`action`属性处理异步保存，结合`displayValue`函数格式化乐观状态下的显示内容（如货币格式）。
- 🎨 **用户体验优化**：组件内部管理乐观更新和加载状态，避免 UI 闪烁；支持通过`hideSpinner`属性或 CSS 选择器（如`group-has-data-pending:`）自定义加载效果。
- 🔗 **实际应用场景**：演示了在博客仪表盘中过滤文章状态（TabList）和销售仪表盘中编辑收入目标（EditableText）的用法，强调与 Next.js App Router 及 Server Functions 的集成。
- 💡 **关键优势**：异步操作自动批处理为稳定提交、乐观状态与数据源同步、错误冒泡至边界处理，组件库未来可内置此模式以统一异步交互体验。

---

### [指南：AI 编程助手 | Next.js](https://nextjs.org/docs/app/guides/ai-agents)

**原文标题**: [Guides: AI Coding Agents | Next.js](https://nextjs.org/docs/app/guides/ai-agents)

Next.js 为 AI 编程助手提供版本匹配的本地文档，通过在项目根目录添加 `AGENTS.md` 文件，引导助手优先读取 `node_modules/next/dist/docs/` 中的最新文档，而非依赖可能过时的训练数据，从而确保代码建议的准确性。

- 📦 **内置文档** - Next.js 将完整文档打包至 `node_modules/next/dist/docs/`，结构与官网一致，确保与安装版本完全匹配。
- 📄 **引导文件** - 项目根目录的 `AGENTS.md` 文件指示 AI 助手在编码前优先查阅本地捆绑文档，避免使用过时信息。
- 🚀 **快速设置** - 使用 `create-next-app` 创建新项目时会自动生成 `AGENTS.md` 和 `CLAUDE.md`；现有项目升级至 v16.2.0-canary.37+ 后手动添加即可。
- 🔧 **灵活配置** - `AGENTS.md` 中的指令简洁专注，开发者可在特定注释标记外添加项目自定义说明，不影响核心规则。
- 📈 **效果验证** - 该机制能显著提升 AI 助手在路由、数据获取等 Next.js 任务中的表现，具体效果可参考官方基准测试结果。

---

### [useActionState – React](https://react.dev/reference/react/useActionState)

**原文标题**: [useActionState – React](https://react.dev/reference/react/useActionState)

`useActionState` 是 React 的一个 Hook，用于在 Action 中管理状态并处理副作用。它接收一个 reducer 函数和初始状态，返回当前状态、一个派发 Action 的函数以及一个表示 Action 是否在处理中的标志。该 Hook 允许 reducer 执行异步操作（如 API 调用），并确保多个 Action 按顺序执行。它常用于表单提交、与 `useOptimistic` 结合提供即时 UI 反馈，以及通过 `AbortController` 取消排队中的 Action。

- 🎯 **核心功能**：`useActionState` 允许在 Action 中更新状态并执行副作用，返回状态、派发函数和 pending 标志。
- 📝 **基本用法**：在组件顶层调用，传入 reducer 函数和初始状态，reducer 可同步或异步，并接收前一个状态和负载。
- 🔄 **顺序执行**：多次调用派发函数时，React 会按顺序排队执行，确保每个 reducer 调用都能接收到前一次调用的结果作为输入。
- ⚡ **与 Transition 集成**：派发函数必须在 Transition 内调用（如通过 `startTransition` 包装或传递给 Action prop），否则会报错。
- 🤝 **配合 `useOptimistic`**：可结合 `useOptimistic` 在等待服务器响应时立即乐观更新 UI，提升用户体验。
- 🛠️ **处理多种操作**：通过向派发函数传递负载（通常是包含 `type` 属性的对象），在 reducer 中使用 switch 语句处理不同的 Action 类型。
- 🚫 **取消操作**：可通过 `AbortController` 向 Action 传递信号来取消排队中的操作，但需确保副作用可安全忽略或重试。
- 📋 **与表单集成**：可将派发函数作为 `action` prop 传递给 `<form>`，React 会自动将提交包装在 Transition 中，reducer 会接收到表单数据。
- 🚨 **错误处理**：已知错误可作为状态的一部分从 reducer 返回并显示；未知错误可抛出，React 将取消所有排队操作并显示最近的错误边界。
- ⚠️ **注意事项**：`useActionState` 必须在组件顶层调用；其派发函数身份稳定，通常可从 Effect 依赖中安全省略；在严格模式下，reducer 不会被调用两次。

---

### [获取失败](https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4)

**原文标题**: [Failed to retrieve](https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4)

无法总结：获取内容失败，状态码 403。

---

### [Vercel](https://www.chat-sdk.dev/)

**原文标题**: [Vercel](https://www.chat-sdk.dev/)

Chat SDK 是一个开源的 TypeScript SDK，用于构建跨平台聊天机器人，支持 Slack、Microsoft Teams、Google Chat、Discord 等多个平台，允许开发者用一套代码部署到不同服务。

- 🚀 **跨平台部署**：一次编写，即可在 Slack、Teams、Google Chat、Discord、GitHub 和 Linear 等多个平台上部署机器人。
- ⚙️ **事件驱动设计**：通过实时聊天事件（如提及、反应、订阅消息）触发处理程序，实现交互响应。
- 🔒 **类型安全**：提供完整的 TypeScript 支持，包括类型安全的适配器、事件处理程序和 JSX 卡片组件。
- 🌊 **AI 流式响应**：原生支持流式传输 LLM 响应，并在各平台上优化渲染效果。
- 📚 **丰富功能**：支持消息发送、卡片、模态框、文件上传、表情符号、斜杠命令等多样化聊天功能。
- 🔌 **适配器与状态管理**：提供 Slack、Microsoft Teams 等平台适配器，以及 Redis、内存等状态管理解决方案，便于集成和扩展。
- 🛠️ **实用指南**：包含逐步教程，如使用 Next.js 构建 Slack 机器人、用 Nuxt 创建 Discord 支持机器人，以及用 Hono 开发 GitHub 代码审查机器人，帮助快速上手常见应用场景。

---

### [发布 styled-components@6.3.0 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.3.0)

**原文标题**: [Release styled-components@6.3.0 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.3.0)

styled-components 发布 6.3.0 版本，主要新增对 React Server Components (RSC) 的原生支持，并扩展了内置元素别名，同时修复了 TypeScript 中 CSS 自定义属性的类型支持。

- 🚀 新增 React Server Components (RSC) 支持：自动检测 RSC 环境，无需 `'use client'` 指令，CSS 通过内联 `<style>` 标签注入，兼容 Next.js App Router 等框架。
- 🔧 扩展内置元素别名：新增现代 HTML（如 `search`、`slot`）和 SVG 元素（如 `feBlend`、`linearGradient`）支持，覆盖更全面的浏览器与 React 元素。
- 🛠️ 修复 TypeScript 类型：完整支持 CSS 自定义属性（如 `--primary-color`）在 `style` 属性和 `.attrs` 中的使用，消除类型错误。
- ⚙️ 更新构建工具：升级共享 CSS 属性处理工具至最新版本，优化内部处理逻辑。

---

### [GitHub - ramonmalcolm10/next-bun-compile](https://github.com/ramonmalcolm10/next-bun-compile)

**原文标题**: [GitHub - ramonmalcolm10/next-bun-compile](https://github.com/ramonmalcolm10/next-bun-compile)

这是一个用于将 Next.js 应用编译成单文件 Bun 可执行文件的构建适配器，能够生成独立、无运行时依赖的二进制程序。

- 🛠️ **适配器功能**：`next-bun-compile` 是一个 Next.js 构建适配器，可将应用编译为单个 Bun 可执行文件，无需额外依赖。
- 📦 **安装与配置**：通过 Bun 安装，并在 `next.config.ts` 中配置 `experimental.adapterPath` 即可启用。
- 🚀 **使用流程**：运行 `bun run build` 后，直接执行生成的 `./server` 二进制文件即可启动服务（默认端口 3000）。
- 🌍 **跨平台编译**：支持通过 `--target` 参数（如 `bun-linux-x64`）进行跨平台编译。
- ⚙️ **环境变量**：支持配置 `PORT`、`HOSTNAME` 等服务器环境变量。
- 📡 **CDN 集成**：如果配置了 `assetPrefix`，静态资源将从 CDN 加载，从而减小二进制文件体积。
- ⚡ **性能优化**：利用 Bun 的 `--bytecode` 标志预编译代码，提升启动速度（示例中启动时间从 84ms 缩短至 45ms）。
- 🔧 **工作原理**：自动设置 `output: "standalone"`，扫描并嵌入静态资源，生成服务器入口文件，并通过编译消除未使用的代码路径。
- 🐛 **故障排除**：对于使用动态 `require()` 的包（如 `pino`），需在 `next.config.ts` 的 `transpilePackages` 中配置以强制编译。
- 📄 **许可与支持**：项目采用 MIT 许可证，并欢迎支持。

---

### [GitHub - vercel-labs/sandcastle: Sandcastle：基于 Vercel 沙箱的网页版 Linux 桌面环境（概念验证）](https://github.com/vercel-labs/sandcastle)

**原文标题**: [GitHub - vercel-labs/sandcastle: Sandcastle: a web-based linux desktop environment on top of Vercel Sandbox (PoC)](https://github.com/vercel-labs/sandcastle)

Sandcastle 是一个基于 Vercel Sandbox 构建的云端 Linux 桌面环境概念验证项目，用户可通过浏览器访问独立的 Linux 工作空间，包含窗口管理器、终端、文件浏览器、代码编辑器及 X11 应用流式传输功能。

- 🏗️ **架构**：采用三层架构，前端为 React 桌面 UI，通过 Next.js API 路由与 Vercel Sandbox 的微虚拟机服务通信，后端使用 Neon Postgres 数据库存储用户数据。
- ⚠️ **性质**：这是一个由 AI 辅助生成的实验性仓库，仅为概念验证演示，不适用于生产环境。
- 🖥️ **核心功能**：提供完整的窗口管理、键盘快捷键、应用启动器、内置应用（终端、文件管理器、VS Code 等）、X11 应用流式传输（如 Firefox、GIMP）、多工作空间及主题同步。
- 📱 **跨平台**：支持移动端触控操作与 iOS 键盘处理，具备桌面通知系统。
- 🛠️ **技术栈**：基于 Next.js 14、TypeScript、Tailwind CSS、Zustand 状态管理，集成 Drizzle ORM、Ghostty 终端、code-server 及 Xpra 流式传输。
- ⚙️ **部署与配置**：依赖 Vercel 账户与 Postgres 数据库，提供环境变量配置脚本，包含数据库初始化、黄金快照构建及开发服务器启动流程。
- 🔄 **自动化运维**：通过 Vercel Cron 作业实现每日快照重建、沙箱生命周期管理及预热池维护，确保快速启动（约 5 秒）。
- 📜 **许可**：项目采用 MIT 开源协议，致谢 Xpra、code-server、Ghostty 等相关技术贡献者。

---

### [无](https://expo.dev/blog/from-web-to-native-with-react?utm_source=Nextjsweekly&utm_medium=newsletter&utm_campaign=33087804-React%20to%20Native&utm_content=react_to_native_blog)

**原文标题**: [None](https://expo.dev/blog/from-web-to-native-with-react?utm_source=Nextjsweekly&utm_medium=newsletter&utm_campaign=33087804-React%20to%20Native&utm_content=react_to_native_blog)

Expo 是一个用于构建跨平台移动应用的开发框架，提供一系列工具和服务来简化开发流程。

- 📚 **文档** – 提供详细的技术文档和资源
- 🛠️ **产品与服务** – 包括 Expo CLI、EAS（应用服务）、Expo Go 应用和 Snack 在线编辑器
- 💼 **企业方案** – 面向企业的解决方案和信任中心
- 💰 **定价信息** – 提供不同版本的定价详情
- 📢 **社区与支持** – 博客、更新日志、新闻通讯和 Discord 社区
- 🏢 **公司信息** – 关于品牌、招聘和法律条款等内容

---

### [我们让 Ralph Wiggum 优化 WebStreams，使其速度提升 10 倍 - Vercel](https://vercel.com/blog/we-ralph-wiggumed-webstreams-to-make-them-10x-faster)

**原文标题**: [We Ralph Wiggumed WebStreams to make them 10x faster - Vercel](https://vercel.com/blog/we-ralph-wiggumed-webstreams-to-make-them-10x-faster)

本文介绍了针对 Node.js 中 WebStreams 性能瓶颈的优化工作，通过开发 fast-webstreams 库显著提升了流处理速度，并推动改进上游至 Node.js 核心。

- 🚀 **性能瓶颈分析**：原生 WebStreams 在服务器端因 Promise 链、对象分配和微任务队列导致高开销，pipeThrough 速度仅为 630 MB/s，比Node.js传统流慢12倍。
- 🔧 **fast-webstreams 解决方案**：通过内部使用 Node.js 流实现 WHATWG 标准 API，优化常见操作路径，如管道连接时调用单个 pipeline() 实现零 Promise 开销，速度提升至 6,200 MB/s。
- ⚡ **同步读取优化**：当数据已缓冲时，reader.read() 直接返回已解决的 Promise，避免事件循环延迟，读取速度达 12,400 MB/s，比原生快3.7倍。
- 🧩 **React Flight 模式优化**：针对 React 服务器组件字节流模式，使用 LiteReadable 替换 Node.js Readable，速度从 110 MB/s提升至1,600 MB/s，加速14.6倍。
- 🌐 **Fetch 响应体处理**：通过延迟解析和轻量级包装优化 fetch() 响应流的转换链，三转换场景速度从 260 MB/s提升至830 MB/s，加速3.2倍。
- 📊 **全面性能提升**：在多种操作和场景中实现显著加速，如管道传输快 9.8 倍、多转换链快 9.7 倍，同时通过 1,100 项 Web 平台测试确保规范兼容。
- 🔄 **上游集成进展**：部分优化已通过 Matteo Collina 的 PR 提交至 Node.js 核心，如 read() 快速路径和 pipeTo() 批量读取，带来 17-20% 的性能提升。
- 🤖 **AI 辅助开发**：借助 Web 平台测试套件和基准测试，以测试驱动方式实现优化，确保符合规范同时提升性能。
- 🛠️ **部署与使用**：库支持全局补丁，可自动优化 fetch() 响应流，Vercel 正逐步在生产环境中应用，并鼓励社区试用和贡献。

---

### [Vercel Blob 私有存储现已开放公测](https://vercel.com/changelog/private-storage-for-vercel-blob-now-available-in-public-beta)

**原文标题**: [Private storage for Vercel Blob, now available in public beta - Vercel](https://vercel.com/changelog/private-storage-for-vercel-blob-now-available-in-public-beta)

Vercel Blob 现已支持私有存储功能，适用于合同、发票和内部报告等敏感文件，所有操作均需身份验证，防止通过公开链接泄露数据。

- 🔒 私有存储需身份验证，公开存储允许公开读取媒体资源
- 🛠️ 可通过控制面板或 CLI 创建私有存储，CLI 命令为 `vercel blob create-store [name] --access private`
- 🔗 在关联的 Vercel 项目中创建存储时，CLI 会自动添加 `BLOB_READ_WRITE_TOKEN` 环境变量用于身份验证
- 📦 安装 SDK 后，使用 `put` 或 `upload` 方法并设置 `access: 'private'` 选项上传文件
- 📥 通过 `get` 方法流式下载私有文件，需在请求中验证身份
- 🧪 私有存储功能目前处于测试阶段，适用于所有套餐，按标准 Vercel Blob 定价计费

---

### [创建查询抽象](https://tkdodo.eu/blog/creating-query-abstractions)

**原文标题**: [Creating Query Abstractions](https://tkdodo.eu/blog/creating-query-abstractions)

本文探讨了在 React Query 中创建查询抽象的最佳实践，指出自定义钩子作为抽象方式存在局限性，并推荐使用`queryOptions`函数来构建更灵活、类型安全的查询配置。

- 🛠️ 自定义钩子作为查询抽象存在限制，如无法在非组件环境使用、难以适应不同钩子（如`useSuspenseQuery`）和类型推断复杂化。
- 🔧 使用`UseQueryOptions`类型进行抽象时，若处理不当会导致数据类型变为`unknown`，且难以支持如`select`等依赖类型参数的选项。
- 🚀 React Query v5 引入的`queryOptions`函数成为更优抽象方案，它仅是类型层面的工具，允许在不同钩子和非钩子环境中共享查询配置。
- 🧩 通过`queryOptions`创建的配置可与其他选项组合使用，保持完整的类型推断和代码简洁性，同时支持如`select`等高级功能。
- 👑 推荐以`queryOptions`为基础构建查询抽象，而非直接依赖自定义钩子，以实现更简单、灵活且类型安全的代码结构。

---

### [React 基金会：Linux 基金会托管下的 React 新家园](https://react.dev/blog/2026/02/24/the-react-foundation)

**原文标题**: [The React Foundation: A New Home for React Hosted by the Linux Foundation – React](https://react.dev/blog/2026/02/24/the-react-foundation)

React Foundation 正式成立，由 Linux Foundation 托管，标志着 React、React Native 及相关项目脱离 Meta，转为独立基金会所有。该基金会由八家白金创始成员支持，将设立董事会进行管理，同时技术治理保持独立，由贡献者社区主导。未来几个月将完成治理结构制定、资产转移及生态支持计划等工作。

- 🏛️ React Foundation 正式启动，由 Linux Foundation 托管，React、React Native 和 JSX 等项目不再归 Meta 所有
- 🤝 八家白金创始成员包括 Amazon、Callstack、Expo、Huawei、Meta、Microsoft、Software Mansion 和 Vercel
- 🧑‍💼 基金会由成员代表组成的董事会管理，Seth Webster 担任执行董事
- 🔧 技术治理独立于董事会，临时领导委员会将制定技术方向结构
- 📅 未来几个月将完成技术治理结构、资产转移、生态支持计划和下一届 React Conf 的筹备工作
- 🙏 感谢全球贡献者和开发者社区，React Foundation 的成立源于社区的支持与协作

---

