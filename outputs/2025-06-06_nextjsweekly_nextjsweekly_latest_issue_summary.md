### [RSC 中的导入机制解析——过度反应](https://overreacted.io/how-imports-work-in-rsc/)

**原文标题**: [How Imports Work in RSC — overreacted](https://overreacted.io/how-imports-work-in-rsc/)

React Server Components（RSC）通过扩展模块系统（`import`/`export`）实现了前后端代码的统一编程范式，核心机制包括环境隔离标记和模块引用控制。以下是关键点总结：

- 🚪 **环境分割指令**：`'use client'`和`'use server'`标记代码运行环境，允许跨环境引用而非直接导入代码。
- 🧩 **模块单例性**：JavaScript 模块在各自环境（前端/后端）中是单例的，多次导入不会重复执行。
- ⚠️ **环境隔离保护**：`server-only`和`client-only`作为“毒丸”标记，阻止模块被错误环境导入（如后端敏感代码泄露到前端）。
- 🔄 **传统共享模式**：常规共享代码会同时存在于前后端，类似两份独立副本，需手动确保兼容性。
- 🛠️ **构建时验证**：利用构建工具（如 Next.js）在编译阶段捕获环境不兼容问题（如前端误用`fs`模块）。
- 🔗 **跨环境通信**：RSC 通过指令建立“门”，实现前后端数据传递（如后端生成`<script>`调用前端函数）。
- 🧠 **心智模型**：将应用视为跨越两台计算机的单程序，模块系统独立但可通过标记安全交互。

RSC 的创新在于通过编译时约束和引用机制，既保留了代码复用的灵活性，又解决了传统全栈开发中的环境边界模糊问题。开发者只需专注模块的本地环境声明（如标记`client-only`），工具链会自动处理跨环境依赖的传播与验证。

---

### [渐进式 JSON —— 过度反应](https://overreacted.io/progressive-json/)

**原文标题**: [Progressive JSON — overreacted](https://overreacted.io/progressive-json/)

渐进式 JSON 是一种改进数据传输效率的方法，通过分块和广度优先的方式传输数据，使客户端能够逐步处理部分数据，而不必等待整个 JSON 加载完成。

- 🌐 **渐进式 JSON 概念**：类似于渐进式 JPEG，JSON 数据分块传输，客户端可以逐步解析和处理部分数据。
- 🔄 **传统 JSON 问题**：客户端必须等待整个 JSON 加载完成后才能解析和处理，效率低下。
- ⚡ **流式 JSON 解析**：通过流式解析器，客户端可以逐步构建对象树，但存在数据不完整的问题。
- 🔍 **广度优先传输**：通过占位符（如`$1`、`$2`）和 Promise，客户端可以逐步填充数据，避免深度优先传输的延迟问题。
- 📦 **数据分块优化**：服务器可以根据需要决定分块大小，平衡传输效率和客户端处理能力。
- ♻ **数据去重**：通过占位符引用重复数据，减少传输量，支持循环对象的序列化。
- ⚛ **React 服务器组件（RSC）**：使用渐进式 JSON 流传输 UI 树，结合`<Suspense>`控制加载状态的显示。
- 🎯 **用户体验优化**：通过`<Suspense>`边界，开发者可以控制数据加载时的 UI 展示，避免页面跳动。
- 🚀 **应用场景**：适用于需要高效数据传输和逐步渲染的场景，如大型应用或慢速网络环境。

---

### [每次导航往返一次——过度反应](https://overreacted.io/one-roundtrip-per-navigation/)

**原文标题**: [One Roundtrip Per Navigation — overreacted](https://overreacted.io/one-roundtrip-per-navigation/)

本文探讨了网页导航过程中数据请求的最佳实践，从传统 HTML 应用到现代客户端渲染的演变，分析了不同数据获取方式的优缺点，并提出了 React Server Components（RSC）作为兼顾效率与模块化的解决方案。

- 🌐 传统 HTML 应用通过单次请求获取完整页面内容，数据直接嵌入 HTML 中，无需额外 API 请求。
- 🔄 REST 架构将数据获取移至客户端，导致多次请求和客户端/服务器瀑布问题，降低了效率。
- 🧩 组件内数据获取（如 useEffect）虽实现代码共置，但难以优化请求效率，可能导致性能问题。
- 🔍 结构化数据获取工具（如 React Query）改善了缓存但未解决请求数量和瀑布问题。
- 🚀 服务器加载器（Server Loaders）集中管理路由数据，减少请求次数，但牺牲了代码共置性。
- ⚡ 服务器函数（Server Functions）简化了 API 调用，但未解决数据获取效率问题。
- 🧩 GraphQL 片段通过声明式数据需求实现共置与单次请求，但学习曲线较高。
- 🔄 React Server Components（RSC）结合服务器加载器的效率和组件的共置性，通过服务器端组件树生成实现单次请求。
- 🛠️ RSC 提供类似传统 HTML 应用的简洁模型，同时支持现代 React 的组件化开发，兼顾性能与开发体验。

---

### [为什么 RSC 要与打包工具集成？—— overreacted](https://overreacted.io/why-does-rsc-integrate-with-a-bundler/)

**原文标题**: [Why Does RSC Integrate with a Bundler? — overreacted](https://overreacted.io/why-does-rsc-integrate-with-a-bundler/)

React Server Components（RSC）是一种编程范式，通过扩展模块系统，将服务器/客户端应用表达为跨越两个运行时的单一程序。其核心实现包括序列化和反序列化 React 树的工具，并与打包工具集成以优化模块加载效率。

- 🧩 RSC 通过`react-server`和`react-client`包实现 React 树的序列化与反序列化，但未直接发布到 npm，因缺少模块系统集成。  
- 📦 RSC 需处理代码而不仅是数据序列化，例如如何序列化包含交互逻辑的组件（如`<Counter>`）。  
- 🔄 直接嵌入代码字符串低效，RSC 采用引用静态 JS 资源的方式（如`/src/client.js#Counter`），类似`<script>`标签。  
- ⚡ 为避免网络请求瀑布，RSC 与打包工具（如 Parcel、Webpack）集成，预构建客户端模块并优化加载。  
- 🔌 打包工具绑定在构建时标记`'use client'`文件，生成代码块；服务器端序列化模块引用，客户端按需加载。  
- 📡 通过`serialize`和`deserialize`API（名称因打包工具而异），RSC 框架（如 Next.js）实现树的传输与重建，支持流式处理。  
- 🛠️ 开发者可通过底层 API（如 Parcel RSC 实现）实验 RSC 的序列化与反序列化流程。

---

### [Trigger.dev v4 测试版 | Trigger.dev](https://trigger.dev/blog/v4-beta-launch/?ref=nextjsweekly)

**原文标题**: [Trigger.dev v4 beta | Trigger.dev](https://trigger.dev/blog/v4-beta-launch/?ref=nextjsweekly)

Trigger.dev 发布了一系列公告、客户案例和技术文章，展示了其平台在自动化、AI 代理和任务部署方面的应用。

- 🚀 2025 年 4 月 9 日：Trigger.dev v4 beta 版本发布，由 CEO Matt Aitken 宣布  
- 🔒 2025 年 5 月 27 日：客户案例——Lewis Carhart 分享如何利用 AI 代理自动化安全合规  
- 🎥 2025 年 4 月 15 日：客户案例——Max Sidebotham 介绍 Icon 如何用 Trigger.dev 革新视频广告创作  
- ✍️ 2025 年 3 月 27 日：技术文章——James Ritchie 撰写关于如何编写优秀的 Cursor Rules  
- 🤖 2025 年 3 月 4 日：客户案例——Sam Wright 讲述 Trigger.dev 如何驱动 Huntr 的内部 AI 代理  
- 🎓 2025 年 2 月 12 日：客户案例——Ben Duggan 分享 MagicSchool AI 如何用 Trigger.dev 开发洞察  
- 🛠️ 2025 年 2 月 6 日：技术文章——James Ritchie 探讨如何用 Trigger.dev 构建高效的 AI 代理  
- ⏱️ 宣传语：3 分钟内即可构建并部署首个任务，立即开始使用

---

### [组合服务器与客户端组件：现代 React 的超能力 | Kent C. Dodds 的 Epic React](https://www.epicreact.dev/composing-server-and-client-components-the-modern-reacts-superpower-08yn9)

**原文标题**: [Composing Server and Client Components: The Modern React's Superpower | Epic React by Kent C. Dodds](https://www.epicreact.dev/composing-server-and-client-components-the-modern-reacts-superpower-08yn9)

现代 React 通过服务器组件和客户端组件的组合，实现了无缝的 UI 构建方式，避免了传统开发中的脚本标签混乱和数据传递问题，同时提升了性能和开发体验。

- 🕰️ 传统开发方式依赖脚本标签和全局变量，难以维护和扩展。
- 🔄 React 服务器组件（RSCs）允许服务器和客户端组件混合使用，各自发挥优势。
- 🧩 服务器组件负责数据获取和静态渲染，客户端组件处理交互和状态管理。
- 🚀 优势包括：无需手动连接脚本、组件封装性更好、性能更优（仅发送必要的 JS 代码）。
- 🌊 支持流式渲染和 Suspense，提升用户体验。
- 🛠️ 实际案例：在 EpicReact.dev 工作坊中，通过服务器组件获取数据，客户端组件处理搜索交互。
- 🔄 新旧对比：RSCs 避免了 DOM 操作、手动数据传递和复杂的 hydration 过程。
- 🎯 解决了 React 中常见的 prop drilling 问题，数据可以直接在需要的地方获取。
- 📚 推荐通过 EpicReact.dev 的服务器组件工作坊深入学习。

---

### [为你的 Next.js 应用添加 Google 登录的最简单方法 ✍️ - Tom Dekan](https://tomdekan.com/articles/google-sign-in-nextjs)

**原文标题**: [The simplest way to add Google sign-in to your Next.js app ✍️ - Tom Dekan](https://tomdekan.com/articles/google-sign-in-nextjs)

本文介绍了如何在 Next.js 应用中集成 Google 登录功能，使用 Prisma ORM 和 BetterAuth 工具实现自托管认证。

- 🚀 **项目初始化**：使用`npx create-next-app`创建 Next.js 项目，并配置 TypeScript、Tailwind 等。
- 📦 **依赖安装**：添加`better-auth`和`prisma`相关依赖，用于认证和数据库管理。
- 🔑 **环境变量配置**：设置`BETTER_AUTH_SECRET`、Google OAuth 的`CLIENT_ID`和`CLIENT_SECRET`，以及数据库连接字符串。
- 🛠 **数据库设置**：安装 PostgreSQL 并创建用户和数据库，更新`.env`文件中的`DATABASE_URL`。
- 🔄 **Prisma 初始化**：运行`npx prisma init`初始化 Prisma，并生成客户端代码。
- 🔗 **BetterAuth 连接**：创建`auth.ts`文件，配置 BetterAuth 实例并连接到 Prisma 数据库。
- 📝 **生成 Prisma Schema**：使用 CLI 工具生成必要的认证模型，并运行迁移。
- 🌐 **Next.js 路由配置**：创建 API 路由处理认证请求，并设置客户端包装器。
- 🖥 **登录页面**：创建登录页面，使用 Google OAuth 进行认证。
- 🏠 **受保护页面**：创建仪表盘页面，仅允许已认证用户访问。
- 🔒 **全局中间件**：使用中间件检查用户认证状态，未认证用户重定向到登录页。
- 🎨 **界面优化**：使用 Framer Motion 和 Tailwind 优化登录和主页的 UI。
- 🚦 **本地测试**：运行开发服务器测试登录功能。
- 🚀 **部署准备**：提供部署到 Vercel 的关键步骤，包括环境变量和回调 URL 的更新。

---

### [删除边缘函数示例 by leerob · Pull Request #1135 · vercel/examples · GitHub](https://github.com/vercel/examples/pull/1135)

**原文标题**: [Delete edge functions examples by leerob · Pull Request #1135 · vercel/examples · GitHub](https://github.com/vercel/examples/pull/1135)

Vercel 删除了边缘函数示例，并推荐使用 Fluid compute 和完整的 Node.js 运行时，同时更新了相关模板链接。

- 🚀 **边缘函数即将弃用** - Vercel 宣布边缘函数将在未来被弃用，建议用户转向 Fluid compute 和完整的 Node.js 运行时。  
- 🔄 **推荐迁移** - 使用 Fluid 可以保留边缘函数的优势，同时避免边缘运行时的限制。  
- 🌍 **区域一致性建议** - 建议将 Vercel 函数区域与数据库区域保持一致，以提高性能。  
- 📅 **逐步推进** - 此次删除是准备工作，未来几个月会有更多官方通知，现有用户无需立即行动。  
- 📂 **模板更新** - 相关模板链接已更新，新账户将默认使用 Fluid。  
- ❤️ **社区反应** - 有开发者对此变更表示支持（StarKnightt 点赞）。

---

### [RFC: 下一个 URL 验证 | Daniel Saewitz](https://saewitz.com/rfc-next-url-validation)

**原文标题**: [RFC: Next URL Validation | Daniel Saewitz](https://saewitz.com/rfc-next-url-validation)

概述：Daniel Saewitz 提出了一种改进 Next.js 中 URL 参数处理的方案，旨在通过类型化和验证机制提升开发体验（DX），并鼓励开发者更多地将状态存储在 URL 中，以增强 UI 的持久性和稳定性。

- 🔗 URL 作为状态管理工具被低估，当前缺乏类型和验证，导致开发体验不佳。
- 💡 灵感来源于 nuqs 和 tanstack router，目标是使 URL 成为类型化接口，提升开发效率。
- 📜 提出通过 schema 验证（如 Zod）对 URL 参数进行类型化和验证，确保数据安全性和一致性。
- 🛠️ 示例代码展示了如何通过 schema 定义和验证 searchParams 和 params，并在页面组件中使用类型化的参数。
- 🔄 建议在验证失败时返回 400 错误，以鼓励开发者更谨慎地处理 URL 参数。
- 🌳 支持在布局或页面中集中定义验证规则，以便子组件复用。
- 🔧 改进了 useSearchParams 钩子，使其返回类型化对象，并提供类似 useState 的 API 来管理 URL 状态。
- 📌 链接（Link）组件支持对象形式的 href，使路径和参数类型化且易于维护。
- 🔄 统一 searchParams 和 query 的命名，减少混淆。
- 📖 通过开发者故事展示了如何在实际项目中应用这些改进，提升代码简洁性和可维护性。
- ⚠️ 讨论了潜在问题，如第三方参数（如推广跟踪）可能被破坏，建议忽略或清理未列出的参数。
- 🔄 建议将验证逻辑移至独立的 validation.ts 文件，以便在客户端和服务器端复用。
- 🤔 反思了当前 await searchParams 的设计，认为可能有更优的启发式方法。
- 🚀 最终目标是让 Next.js 更自然地利用 URL 的强大功能，减少对 useState 的过度依赖，提升状态持久性。

---

### [GitHub - vercel-labs/在Vercel上运行的FFmpeg](https://github.com/vercel-labs/ffmpeg-on-vercel)

**原文标题**: [GitHub - vercel-labs/ffmpeg-on-vercel](https://github.com/vercel-labs/ffmpeg-on-vercel)

这是一个关于在 Vercel 平台上原生运行 FFmpeg 的项目介绍。

- 🚀 **项目名称**: vercel-labs/ffmpeg-on-vercel  
- 🌟 **星标数**: 55  
- 🍴 **复刻数**: 2  
- 🔧 **主要功能**: FFmpeg 可在 Vercel 的 Fluid 计算环境中原生运行，无需修改  
- 📂 **关键文件**: `route.ts` 提供了基于`ffmpeg-static` npm 包的示例用法  
- ⚙️ **配置建议**: 建议增加 CPU/RAM 配置以充分利用 FFmpeg 的多核性能，例如设置内存为 3009MB  
- 📝 **配置文件示例**: 提供了`vercel.json`的配置示例  
- 🔗 **演示链接**: [ffmpeg-demo-gamma.vercel.app](ffmpeg-demo-gamma.vercel.app)  
- 📜 **语言**: 项目使用 TypeScript 编写  
- 👥 **贡献者**: 包括 cramforce、Malte Ubl 等

---

### [Next.js + React Router](https://nexfaster.rdsx.dev/)

**原文标题**: [Next.js + React Router](https://nexfaster.rdsx.dev/)

好的，请提供需要总结的文本内容，我会按照您要求的模板生成概述和带表情符号的要点列表。  

示例模板：  

概述总结  
- 🌟 要点 1  
- 📌 要点 2  
- 🔍 要点 3  

请提供具体文本，我会为您生成符合要求的总结！

---

### [发布 v1.4.0 · unnoq/orpc · GitHub](https://github.com/unnoq/orpc/releases/tag/v1.4.0)

**原文标题**: [Release v1.4.0 · unnoq/orpc · GitHub](https://github.com/unnoq/orpc/releases/tag/v1.4.0)

oRPC 发布了 v1.4.0 版本，包含多项新特性、优化和 Bug 修复，主要涉及请求去重插件、批处理模式切换、Hey API 集成、AWS Lambda 适配器支持、TanStack Query 统一集成等更新。

- 🛠 **请求去重插件** - 新增 `DedupeRequestsPlugin`，通过过滤相似请求减少冗余服务器请求。  
- 🔄 **批处理模式切换** - `BatchLinkPlugin` 支持 `streaming`（默认）和 `buffered` 模式，适配不同环境需求。  
- 🔌 **Hey API 集成** - 提供工具将 Hey API 生成的客户端转换为 oRPC 客户端，兼容 oRPC 生态。  
- ☁️ **AWS Lambda 适配器** - 新增对 AWS Lambda 响应流的支持，需配合 Hono 适配器使用。  
- 🔄 **TanStack Query 统一集成** - 支持所有 TanStack Query 库（React/Vue/Angular 等），优化选项配置结构。  
- 📦 **数组解析优化** - 同名查询参数（如 `color=red&color=blue`）现在自动解析为数组。  
- 📜 **路由方法推断** - 通过 `inferRPCMethodFromContractRouter` 自动从合约中提取请求方法。  
- 📝 **路由规范覆盖** - 支持通过 `route.spec` 完全覆盖自动生成的 OpenAPI 操作配置。  
- 🔍 **验证库更新** - Zod 升级至 3.25.49，Valibot 新增输出策略支持。  
- 🐞 **Bug 修复** - 修复 Node.js 中信号和流的行为问题。  

（注：原文中部分加载错误提示和 GitHub 交互数据未列入摘要）

---

### [发布 v9.0.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v9.0.0)

**原文标题**: [Release v9.0.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v9.0.0)

Storybook 9.0 是一个重大版本更新，专注于测试和包体积优化，引入了多项新功能和改进，同时进行了大量错误修复和依赖项更新。

- 🚀 **核心改进**：Storybook 9.0 主要关注测试和包体积优化，包体积减少了 48%。
- � **测试增强**：新增组件测试功能，包括交互测试、无障碍测试、视觉测试和覆盖率测试。
- 🏷️ **组织方式**：引入了基于标签的故事组织方式，支持全局故事变量。
- 🔄 **框架升级**：对 Svelte、Next.js、React Native 和 Angular 进行了重大升级。
- 📚 **迁移指南**：提供了详细的迁移指南，帮助用户从旧版本升级到 9.0。
- 🛠️ **错误修复**：修复了大量问题，包括无障碍测试、控件加载状态、文档布局等。
- 🔄 **依赖更新**：更新了多个依赖项，包括升级到 Vitest 3 和移除旧版支持。
- 📦 **包管理**：移除了多个过时的插件，并将一些插件整合到核心中。
- 📊 **性能优化**：通过预打包和语法最小化等方式优化了性能。
- 🤖 **自动化迁移**：改进了自动化迁移脚本，处理了多种边缘情况和配置问题。

---

### [为您的 SaaS 添加订阅服务——Clerk Billing](https://clerk.com/blog/add-subscriptions-to-your-saas-with-clerk-billing?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=billing-guide&utm_content=06-06-25&dub_id=9dEv9qZFTJ6ySD1V)

**原文标题**: [Add subscriptions to your SaaS with Clerk Billing](https://clerk.com/blog/add-subscriptions-to-your-saas-with-clerk-billing?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=billing-guide&utm_content=06-06-25&dub_id=9dEv9qZFTJ6ySD1V)

Clerk Billing 是一项集成订阅管理的服务，帮助 SaaS 应用快速实现付费功能，无需从零开发复杂的计费系统。

- 💡 Clerk Billing 提供现成的订阅管理界面和逻辑，简化 SaaS 应用的付费功能实现  
- 🛒 通过 Clerk 仪表盘定义订阅计划和功能，使用 `<PricingTable />` 组件展示给用户  
- 💳 集成 Stripe 处理支付，支持沙盒环境开发  
- 🔑 使用 `has()` 函数轻松控制用户对高级功能的访问权限  
- 📊 用户可通过 `<UserProfile />` 组件管理订阅，包括查看发票和支付方式  
- 🚀 演示项目 Quillmate 展示了如何保护 AI 聊天功能仅供付费用户使用  
- ⚡ 后端 API 也可用 `has()` 函数验证用户订阅状态  
- 🔄 订阅管理包括取消自动续费等功能，支持管理员查看用户订阅状态

---

### [将 try/catch 扔进🗑️：使用 Result 类型提升你的 React 错误处理能力 - Dillon Mulroy - YouTube](https://www.youtube.com/watch?v=VcOIz7tOBoM)

**原文标题**: [Throw Try/Catch in the 🗑️ Level up your React error handling with the Result type - Dillon Mulroy - YouTube](https://www.youtube.com/watch?v=VcOIz7tOBoM)

该文本列出了 YouTube 平台的相关链接和信息，包括关于、新闻、版权、联系方式等内容，以及创作者、广告商和开发者的资源，同时涵盖了条款、隐私、政策安全和平台运作方式等法律和技术细节。

- 📢 Press - 新闻  
- © Copyright - 版权信息  
- 📞 Contact us - 联系我们  
- 🎨 Creators - 创作者相关  
- 💼 Advertise - 广告合作  
- 💻 Developers - 开发者资源  
- 📜 Terms - 使用条款  
- 🔒 Privacy - 隐私政策  
- ⚖️ Policy & Safety - 政策与安全  
- 🔧 How YouTube works - 平台运作方式  
- 🧪 Test new features - 测试新功能  
- © 2025 Google LLC - 版权归属

---

### [AI 代理开发的务实之道 - Vercel](https://vercel.com/blog/the-no-nonsense-approach-to-ai-agent-development)

**原文标题**: [The no-nonsense approach to AI agent development - Vercel](https://vercel.com/blog/the-no-nonsense-approach-to-ai-agent-development)

AI 代理是能够接管由手动、多步骤流程组成的任务的软件系统，它们通过上下文判断和自适应能力，提供比传统规则型自动化更灵活的解决方案。  

- 🤖 **AI 代理的核心特点**：依赖上下文决策，减少重复性操作，同时保留关键步骤的人工审核。  
- 🎯 **有效代理的关键**：专注狭窄、特定领域，避免过度宽泛的设计。  
- 🛠️ **构建步骤 1：手动模拟原型**  
  - 先人工模拟任务流程，使用真实输入（如截图、API 响应）测试 LLM 的可行性。  
  - 识别可自动化环节，若模型表现不佳则调整或放弃。  
- ⚙️ **构建步骤 2：自动化循环**  
  - 编写代码框架，结合确定性计算（如解析、排序）和 LLM 推理（需判断的步骤）。  
  - 示例：股票分析代理通过工具调用获取数据，生成技术/基本面分析与投资建议。  
- 🔧 **构建步骤 3：优化可靠性**  
  - 精简提示词、精确工具调用，用确定性代码替代部分模型交互。  
  - 引入结构化评估，确保代理在多样化输入中表现稳定。  
- 📌 **核心原则**：  
  - 任务需难以用传统代码实现，且手动测试显示 LLM 潜力。  
  - 基于扎实的软件工程实践，逐步优化而非追求复杂抽象。  
- ✨ **结果**：成功的代理像“魔法”，实则依赖清晰的逻辑与迭代优化。  
- 🚀 **行动建议**：使用 AI SDK，结合常规编程模式构建可靠代理。

---

### [IE6、人工智能与网页浏览的未来 - RL Nabors](https://agenticweb.nearestnabors.com/p/ai-future-web)

**原文标题**: [IE6, AI, and the future of browsing the Web - by RL Nabors](https://agenticweb.nearestnabors.com/p/ai-future-web)

谷歌浏览器（Chrome）正步入类似 IE6 的停滞期，AI 技术或将重塑互联网的未来。  

- 🏙️ **Chrome 的 IE6 时代**：谷歌削减对 W3C 标准的支持，浏览器用户体验多年未显著改进，类似微软 IE6 垄断后的停滞。  
- 📉 **搜索业务下滑**：谷歌搜索量首次下降，用户转向 AI 服务（如 Perplexity），威胁其广告核心收入。  
- 🔍 **战略重心转移**：谷歌重组团队，裁撤 Chrome 核心成员，资源向 AI（如 Gemini）倾斜，而非传统网页生态。  
- 🍏 **浏览器市场竞争**：谷歌试图通过游说打破 Safari 在 iOS 的垄断，实为争夺市场份额，非为用户选择权。  
- 🍪 **广告与数据争议**：谷歌推迟淘汰第三方 Cookie，暴露其对广告和数据收集的依赖，与隐私趋势背道而驰。  
- 🤖 **代理式网络（Agentic Web）崛起**：AI 直接提供答案，绕过广告和网页跳转，颠覆传统广告支撑的互联网经济。  
- 💡 **未来挑战**：作者提出需探索后广告时代的经济模型、身份认证、内容触达及安全协议等新方向。  
- 🌐 **社区的力量**：强调开发者与用户才是互联网的真正塑造者，而非巨头或标准组织。  

（注：Emoji 选择基于每点核心意象，如🏙️表停滞、📉表衰退、🤖表 AI 颠覆等。）

---

### [构建长按删除组件](https://emilkowal.ski/ui/building-a-hold-to-delete-component)

**原文标题**: [Building a Hold to Delete Component](https://emilkowal.ski/ui/building-a-hold-to-delete-component)

Emil Kowalski 是一名设计工程师，分享了如何构建一个“按住删除”组件的详细教程，通过 CSS 的 clip-path 和过渡效果实现按钮的动画交互。

- 🛠️ **组件介绍**：Emil Kowalski 设计了一个“按住删除”按钮组件，并在 X 平台上分享，获得了很多喜爱。
- 🎨 **初始设计**：从一个简单的样式化按钮开始，包含一个 SVG 图标和文本。
- � **结构设置**：创建两个版本的按钮，一个默认单色，另一个用于逐渐显示，通过绝对定位和 clip-path 实现覆盖效果。
- ✂️ **隐藏覆盖层**：使用 clip-path 的 inset 属性将覆盖层从右侧隐藏，准备后续的显示过渡。
- 🎭 **显示过渡**：通过:active 伪类和 clip-path 属性实现按住时覆盖层的逐渐显示，使用 2 秒的线性过渡效果。
- ⚡ **优化过渡**：释放按钮时使用 200 毫秒的快速过渡，提升用户体验，同时保持按住时的慢速过渡以确认操作。
- 🔍 **微调效果**：添加按下时的缩放动画（transform: scale(0.97)），增强按钮的交互反馈。
- 📜 **最终代码**：提供了完整的代码示例，包括 App.js 和 styles.css，展示了如何实现这一效果。
- 📚 **更多资源**：Emil 提到这一组件来自他的网页动画课程，课程涵盖从简单 CSS 动画到复杂 Framer Motion 组件的构建。

---

### [Vercel 可观测性现已支持中间件洞察功能](https://vercel.com/changelog/middleware-insights-now-available-in-vercel-observability)

**原文标题**: [Middleware insights now available in Vercel Observability - Vercel](https://vercel.com/changelog/middleware-insights-now-available-in-vercel-observability)

Vercel Observability 仪表板新增了中间件专用视图，提供调用次数和性能指标，Plus 用户可解锁高级分析工具。

- 🔍 中间件专用视图：展示调用次数和性能指标  
- 📊 Plus 用户特权：按请求路径分析中间件调用，匹配配置  
- 🔧 操作分类统计：按类型（如重定向/改写）分解中间件行为  
- 🎯 改写目标追踪：查看改写目标地址及触发频率  
- 🔎 查询构建器：支持自定义中间件调用查询  
- 🌐 快速入口：可直接访问仪表板或查阅 Observability 功能文档

---

### [Vercel Blob 分析现已集成至可观测性功能中 - Vercel](https://vercel.com/changelog/vercel-blob-insights-now-available-in-observability)

**原文标题**: [Vercel Blob insights now available in Observability - Vercel](https://vercel.com/changelog/vercel-blob-insights-now-available-in-observability)

Vercel Blob 的可观测性仪表板新增了专属标签页，帮助用户全面监控 Blob 存储的使用情况。

- 👁️ 新增 Vercel Blob 专属标签页，提供存储使用可视化监控
- 📊 支持团队级数据查看：包括总数据传输量、下载量、缓存活动及 API 操作
- 🔍 可深入分析用户代理、边缘区域和客户端 IP 的活动数据
- 💡 帮助识别使用模式，发现低效环节，优化资产存储和分发
- 🚀 提供"立即试用"和"了解更多"选项，方便用户快速体验和获取详细信息

---

