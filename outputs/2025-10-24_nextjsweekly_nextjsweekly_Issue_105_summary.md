### [Next.js 2025 开发者大会](https://nextjs.org/conf)

**原文标题**: [Next.js Conf 2025](https://nextjs.org/conf)

Next.js Conf 2025 大会日程与亮点概览

- 🗓️ 大会聚焦 Next.js 16 最新功能与 AI 创新应用，汇聚开发者社区
- 🎤 主题演讲涵盖应用架构优化（10:45-11:10）、教育平台实战（11:10-11:35）、AI 开发实践（13:30-13:55）等核心议题
- 👥 演讲嘉宾包括 Vercel CEO、Bun 技术布道师、Databricks 开发者倡导者等行业专家
- ❓ 常见问题覆盖线上线下参会差异、议程发布、赞助合作等实用信息
- 💎 设有钻石/白金/黄金三级赞助合作体系，支持企业生态建设
- 🌐 提供线上直播与往期内容回放，可通过官方渠道持续关注

---

### [Next.js Conf 2025 - YouTube](https://www.youtube.com/watch?v=IdIgkiDu-94)

**原文标题**: [Next.js Conf 2025 - YouTube](https://www.youtube.com/watch?v=IdIgkiDu-94)

这是一个关于 YouTube 平台相关信息和服务的概述。

- ℹ️ 关于平台的基本信息
- 📢 新闻与媒体联系渠道
- ©️ 版权相关事项
- 📞 用户联系与反馈方式
- 🎬 内容创作者资源
- 💼 广告合作机会
- 💻 开发者工具与 API
- 📋 使用条款与协议
- 🔒 隐私保护政策
- ⚖️ 平台政策与安全指南
- 🔧 平台运作机制说明
- 🧪 新功能测试体验
- ⏰ 2025 年谷歌公司版权所有

---

### [入门指南：缓存组件 | Next.js](https://nextjs.org/docs/app/getting-started/cache-components)

**原文标题**: [Getting Started: Cache Components | Next.js](https://nextjs.org/docs/app/getting-started/cache-components)

Next.js Cache Components 是一种新的渲染和缓存方法，通过细粒度控制缓存内容与时机，结合部分预渲染（PPR）实现快速初始加载与动态内容流式传输的平衡。

- 🚀 **动态默认**：所有路由默认动态渲染，确保数据实时性
- 🎯 **缓存控制**：使用 `use cache` 指令标记可缓存组件和数据
- ⏳ **流式渲染**：通过 Suspense 边界管理动态内容，静态外壳立即显示
- 🔄 **缓存更新**：支持 `cacheTag` 标签化和 `updateTag`/`revalidateTag` 重新验证
- ⚙️ **配置启用**：在 next.config.js 中设置 `cacheComponents: true` 开启功能
- 📊 **数据分类**：运行时数据（cookies/headers）和动态数据（fetch/数据库查询）需包裹在 Suspense 中
- 🚫 **限制说明**：缓存函数参数需可序列化，不支持 Edge Runtime
- 🔄 **迁移指南**：替代原有的 dynamic、revalidate、fetchCache 等路由配置选项

---

### [next.config.js: experimental.adapterPath | Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath)

**原文标题**: [next.config.js: experimental.adapterPath | Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath)

Next.js 实验性适配器功能允许通过自定义模块介入构建过程，用于部署平台集成或自定义构建流程。

- 🔧 **配置方式**：在 next.config.js 中通过 experimental.adapterPath 指定适配器路径
- 📦 **核心接口**：适配器需实现 modifyConfig（修改配置）和 onBuildComplete（构建完成回调）方法
- 🗂️ **输出类型**：支持页面、API 路由、应用路由、预渲染文件、静态资源、中间件等六类构建产物
- 🛣️ **路由信息**：提供完整的路由配置（重定向/重写/动态路由），包含编译后的正则表达式
- 🏗️ **应用场景**：适用于部署平台集成、资源处理、构建监控、自定义打包等定制化需求

---

### [Vercel 出品 Next.js —— React 框架](https://nextjs.org/evals)

**原文标题**: [Next.js by Vercel - The React Framework](https://nextjs.org/evals)

本文档展示了多种 AI 模型在 Next.js 代码生成与迁移任务中的性能评估结果，涵盖成功率、执行时间及资源消耗等关键指标。

- 🏆 **GPT-5-Codex 模型表现最佳** - 成功率最高达 42%，但执行时间较长（42.8 秒）
- ⚡ **Kimi-K2-0905 速度最快** - 仅需 1.82 秒完成处理，成功率 36%
- 📊 **成功率分布集中** - 多数模型成功率落在 30%-40% 区间
- 🔋 **资源消耗差异显著** - Gemini-2.5-Pro 消耗最多令牌（322,147），Qwen3-Max 最节省（87,364）
- 🤖 **智能代理表现突出** - Claude 代理以 42% 成功率领先其他代理
- ⏱️ **效率平衡典范** - Grok-4-Fast-Reasoning 在速度（6.02 秒）与成功率（38%）间取得良好平衡
- 📈 **版本迭代进步** - Claude 系列从 Haiku 到 Opus 版本呈现性能提升趋势
- 🎯 **专业模型优势** - 代码专用模型（如 Qwen3-Coder）在响应速度方面表现亮眼

---

### [船舶人工智能 2025](https://vercel.com/ship/ai)

**原文标题**: [Ship AI 2025](https://vercel.com/ship/ai)

这是一场面向 AI 开发者的技术大会，聚焦 AI 工具与商业应用创新

- 🚀 开幕主题演讲将发布 AI SDK、AI 网关和智能体等最新技术进展
- 💳 专题讨论探索智能体系统如何重塑数字交易与商业生态
- 🛠️ 工作流开发工具包工作坊展示构建持久化应用与 AI 智能体的开源框架
- 🌉 技术分会详解通过统一 AI 网关接入数百种模型的实践案例
- 👥 汇聚 VercelCEO、Anthropic 销售总监等行业领袖进行深度分享
- ❓ 提供线上线下参与方式、议程安排、赞助合作等常见问题解答
- 🤝 设置钻石/白金/黄金等多级赞助体系，支持开发者生态建设

---

### [使任何 TypeScript 函数持久化](https://useworkflow.dev/)

**原文标题**: [Make any TypeScript Function Durable](https://useworkflow.dev/)

Workflow DevKit 是一个处于测试阶段的开发工具包，旨在为异步 JavaScript 应用提供持久性、可靠性和可观测性，使开发者能够轻松构建可暂停、恢复和保持状态的应用程序及 AI 代理。

- 🛠️ **简单声明式 API**：通过简单的指令定义和使用工作流，无需手动配置队列或自定义重试机制。
- ⏳ **资源高效暂停**：使用 `sleep` 函数暂停工作流，例如暂停 7 天发送后续邮件，期间不消耗资源。
- 📧 **步骤定义与错误处理**：通过 `"use step"` 定义步骤，支持错误处理，如发送邮件失败时抛出致命错误。
- 🔍 **全面可观测性**：自动捕获跟踪、日志和指标，支持端到端检查、暂停、重放和时间旅行调试。
- 🔄 **框架兼容性**：当前支持 Next.js 和 Nitro，未来将扩展至 Svelte、Nuxt、Hono 和 Bun 等框架。
- 🚀 **零配置部署**：代码可在本地、Docker、Vercel 或其他云平台运行，开源设计避免供应商锁定。
- 🤖 **多功能应用场景**：适用于实时流式代理、CI/CD 管道和多日邮件订阅工作流等多种应用。
- 📦 **快速入门模板**：提供故事生成 Slack 机器人、航班预订应用和自然语言图像搜索等模板，帮助快速上手。

---

### [Vercel AI 云上的零配置后端 - Vercel](https://vercel.com/blog/zero-config-backends-on-vercel-ai-cloud)

**原文标题**: [Zero-config backends on Vercel AI Cloud - Vercel](https://vercel.com/blog/zero-config-backends-on-vercel-ai-cloud)

Vercel 扩展其平台功能，现支持零配置部署 Python 与 TypeScript 后端框架，为复杂 AI 应用提供全栈解决方案。通过框架定义基础设施自动优化计算资源，新增流体计费模式降低长时任务成本，并推出可持久化编排工具与生产级模板库。

- 🚀 支持 FastAPI/Express 等主流框架，无需配置即可自动部署与扩缩容
- 🛠️ 推出原生 Python SDK，集成沙箱/缓存/存储等云服务功能
- ⚡ 流体计算按有效 CPU 时间计费，大幅降低长时 LLM 任务成本
- 🔄 持久化编排工具支持多步骤 AI 工作流与数据管道
- 📚 提供聊天机器人/编程助手/RAG 等生产级后端模板
- 🌐 统一平台管理前后端，实现全链路可观测性

---

### [介绍 Vercel Agent：您的新 Vercel 队友 - Vercel](https://vercel.com/blog/introducing-vercel-agent)

**原文标题**: [Introducing Vercel Agent: Your new Vercel teammate - Vercel](https://vercel.com/blog/introducing-vercel-agent)

Vercel 推出了一款名为 Vercel Agent 的 AI 协作工具，现以公开测试版形式发布，旨在通过集成 AI 技术与平台深度知识，结合用户代码和遥测数据来提升开发效率与质量。

- 🚀 智能代码审查：直接在 GitHub 工作流中运行模拟构建验证，提供经过测试的代码优化建议
- 🔍 生产问题调查：基于实时数据自动分析异常事件根源，将调试时间从数小时缩短至数秒
- 🛠️ 平台深度融合：依托框架定义的基础设施，全面理解应用程序代码、框架和运行环境
- 📦 服务化代理模式：无需自行构建托管，通过安全集成的智能代理服务提升开发体验
- 🎯 验证驱动决策：所有建议均通过端到端验证，确保输出结果具备可操作性
- ⚡ 效能提升：同步推出代理市场，未来将扩展至自动创建 PR 和实施修复等全流程自动化

---

### [Vercel Agent Investigations 现已进入公开测试阶段 - Vercel](https://vercel.com/changelog/vercel-agent-investigations-now-in-public-beta)

**原文标题**: [Vercel Agent Investigations now in Public Beta - Vercel](https://vercel.com/changelog/vercel-agent-investigations-now-in-public-beta)

Vercel Agent 现已推出 AI 调查功能，可自动分析异常警报，帮助团队快速诊断和解决生产环境问题。该功能通过智能根因分析提升系统稳定性，同时降低人工警报处理负担。

- 🔍 自动触发 AI 调查异常警报（如流量突增或错误激增），实现根因分析与影响评估
- 🚀 支持手动启动调查功能，用户可在警报详情页主动发起诊断
- 💡 通过智能研判加速事故处理，提升系统稳定性并减少警报疲劳
- 🌐 现已面向 Pro 及 Enterprise 用户开放公开测试版（需 Observability Plus 订阅）
- 💰 采用用量计费模式，新用户可获 100 美元体验额度

---

### [React Server 组件：它们真的能提升性能吗？](https://www.developerway.com/posts/react-server-components-performance)

**原文标题**: [React Server Components: Do They Really Improve Performance?](https://www.developerway.com/posts/react-server-components-performance)

本文通过数据驱动的方式比较了客户端渲染 (CSR)、服务端渲染 (SSR) 和 React 服务端组件 (RSC) 在相同应用和测试环境下的性能表现，重点关注初始加载性能以及客户端与服务端数据获取的影响。

- 📊 **客户端渲染 (CSR)**：初始加载最慢 (LCP 4.1s)，但页面一旦显示即可交互，页面间切换最快
- ⚡ **服务端渲染 (SSR)**：显著改善初始加载 (LCP 1.61s)，但存在"无交互间隙"问题
- 🚀 **服务端数据获取**：虽然会降低初始加载速度，但能让完整页面体验更早可见
- 🔄 **Next.js 迁移**：从 Pages 迁移到 App Router 可能使性能变差，需要重写数据获取逻辑
- ⚠️ **React 服务端组件**：单独使用时性能改善有限，必须配合 Streaming 和 Suspense 才能发挥优势
- 📉 **无交互间隙**：App Router 版本的无交互间隙最大 (2.52s)，这是服务端渲染的主要代价
- 🔧 **Suspense 关键性**：忘记使用 Suspense 边界会导致流式渲染失效，性能表现与普通 SSR 无异
- 💡 **性能优化**：真正的性能提升来自于完全重写为服务端组件优先的数据获取架构

---

### [React 定义了 Web，AI SDK 将定义 AI | egghead.io](https://egghead.io/react-defined-the-web-the-ai-sdk-will-define-ai~ugbyu)

**原文标题**: [React Defined the Web. The AI SDK Will Define AI | egghead.io](https://egghead.io/react-defined-the-web-the-ai-sdk-will-define-ai~ugbyu)

AI SDK 正在引领从命令式编程到声明式编程的思维模式转变，就像 React 当年重新定义前端开发范式一样。它通过统一的流式处理和工具调用抽象层，让开发者专注于智能功能本身而非底层集成细节。

- 🧠 **思维模式革新** - 从手动处理 API 响应转向声明式的流式交互和智能界面构建
- ⚡ **声明式抽象** - 提供`useChat`和`streamText`等原语，自动处理连接、状态管理和重新渲染
- 🔄 **统一接口** - 作为 AI 领域的"虚拟 DOM"，提供模型无关的 API，支持快速切换 LLM 提供商
- 🌐 **全栈覆盖** - 相同 API 可在浏览器、Node.js 和 CLI 中无缝使用，支持从个人工具到企业级多智能体编排
- 🎯 **生成式 UI** - 超越文本流式传输，让 AI 能够动态决定渲染哪个交互组件
- 📈 **生态主导** - 每周超 360 万次下载，获得 Cloudflare、Anthropic、OpenAI 等主流厂商官方支持
- 🚀 **快速开发** - 20 行代码构建 CLI 工具，80 行代码实现多智能体编排系统
- 🔧 **工具调用** - 统一的工具调用接口，任何模型都能自动使用定义的工具

---

### [使用 useSyncExternalStore 进行并发水合 | Jacob 'Kurt' Groß](https://kurtextrem.de/posts/react-uses-hydration)

**原文标题**: [Concurrent Hydration with useSyncExternalStore | Jacob 'Kurt' Groß](https://kurtextrem.de/posts/react-uses-hydration)

本文探讨了在 React 服务端渲染中使用 Suspense 时如何通过改进 useSyncExternalStore 实现并发水合，避免水合不匹配问题并提升用户体验。

- 🚧 useSyncExternalStore 在 Suspense 边界会导致同步阻塞渲染，引发加载状态闪烁和水合错误
- ⚡ 通过 useDeferredValue 包装 useSyncExternalStore 返回值可实现并发渲染，避免阻塞主线程
- 🎯 配合 useMemo 优化组件渲染，确保在水合期间返回稳定值
- 📈 这种模式能显著改善 INP 指标，让 React 调度器能够优先处理用户交互
- 💡 该方案已获 React 团队认可，可有效替代 useEffect 的水合处理方案
- 🔧 需要注意在水合期间保持返回值的稳定性，并使用 useMemoOne 进行正确性保障的记忆化

---

### [在 ChatGPT 中运行 Next.js：深入探讨原生应用集成 - Vercel](https://vercel.com/blog/running-next-js-inside-chatgpt-a-deep-dive-into-native-app-integration)

**原文标题**: [Running Next.js inside ChatGPT: A deep dive into native app integration - Vercel](https://vercel.com/blog/running-next-js-inside-chatgpt-a-deep-dive-into-native-app-integration)

本文介绍了如何将完整的 Next.js 应用嵌入 ChatGPT 中运行，通过解决嵌套 iframe 架构带来的技术挑战，实现了原生导航和现代框架功能的完整支持。

- 🚪 通过 Model Context Protocol（MCP）协议，Next.js 应用可直接嵌入 ChatGPT 对话中，触达 8 亿用户
- 🛡️ ChatGPT 采用三层 iframe 安全架构隔离应用，但导致 Next.js 多项核心功能失效
- 🔧 配置 assetPrefix 和<base>元素解决静态资源和相对路径加载问题
- 📜 重写 history API 防止真实域名泄露，保持沙箱安全边界
- 🔄 修补 fetch 请求实现客户端导航，重写跨域请求至正确域名
- 🌐 添加 CORS 中间件处理预检请求，支持跨域 RSC 请求
- 👀 使用 MutationObserver 防止父框架修改 HTML 导致的 React 水合错误
- 🔗 拦截外部链接点击，通过 openai.openExternal() 在用户浏览器中打开
- ⚙️ MCP 服务器通过资源和工具机制连接 Next.js 应用与 ChatGPT
- 🎣 提供 React hooks 管理 ChatGPT 集成，支持消息发送和工具输出访问
- ⚡ 完整保留 Next.js 所有特性，包括服务端组件、流式渲染和动态路由
- 🚀 提供启动模板，开发者可快速部署功能完整的 ChatGPT 应用

---

### [Next.js 16 | Next.js](https://nextjs.org/blog/next-16)

**原文标题**: [Next.js 16 | Next.js](https://nextjs.org/blog/next-16)

Next.js 16 正式发布，带来多项性能优化和架构改进，包括缓存组件、Turbopack 稳定版、增强路由等核心功能升级，同时引入代理文件替代中间件并优化开发体验。

- 🚀 **Turbopack 稳定版**：默认打包工具，生产构建提速 2-5 倍，热更新快 10 倍
- 💾 **缓存组件**：通过 `use cache` 指令实现显式缓存，完善部分预渲染（PPR）能力
- 🔄 **增强路由**：布局去重与增量预加载减少网络传输量，提升页面切换速度
- 🛠️ **开发工具集成**：Next.js DevTools MCP 支持 AI 辅助调试，提供上下文日志和错误追踪
- 📁 **代理文件**：`proxy.ts` 替代 `middleware.ts`，明确网络边界并统一 Node.js 运行时
- ⚡ **React 19.2 支持**：内置视图过渡、useEffectEvent 等新特性
- 🗑️ **缓存 API 升级**：`revalidateTag()` 需指定缓存策略，新增 `updateTag()` 实现"即写即读"
- 📊 **日志优化**：开发阶段显示编译/渲染时间，构建过程展示各环节耗时
- ⚠️ **破坏性变更**：移除 AMP 支持、要求 Node.js 20.9+、异步化 params/cookies 等 API
- 🔧 **体验改进**：简化项目创建流程、文件系统缓存测试版、构建适配器 Alpha 版

---

### [civic-auth-examples/packages/civic-auth/nextjs 位于主分支 · civicteam/civic-auth-examples · GitHub](https://github.com/civicteam/civic-auth-examples/tree/main/packages/civic-auth/nextjs)

**原文标题**: [civic-auth-examples/packages/civic-auth/nextjs at main · civicteam/civic-auth-examples · GitHub](https://github.com/civicteam/civic-auth-examples/tree/main/packages/civic-auth/nextjs)

这是一个 GitHub 仓库页面，显示 civicteam 组织下的 civic-auth-examples 项目

- 🔓 公开仓库，任何人都可以查看
- 🔔 需要登录才能更改通知设置
- 🍴 项目已被分叉 3 次
- ⭐ 获得 3 个星标收藏
- 📝 存在 5 个未解决的问题
- 🔄 有 17 个拉取请求待处理
- ⚠️ 页面加载时出现错误提示
- 📊 提供代码、问题、安全等详细导航选项

---

### [引言 | 更优的 Fetch 方法](https://better-fetch.vercel.app/docs)

**原文标题**: [Introduction | Better Fetch](https://better-fetch.vercel.app/docs)

Better Fetch 是一个用于 TypeScript 的高级 fetch 封装库，支持使用符合 Standard Schema 规范的验证器进行运行时验证和类型推断，具备错误值处理、预定义路由、钩子函数和插件等功能，兼容浏览器、Node.js 18+、Worker、Deno 和 Bun 环境。

- 🎯 支持多种验证器（如 Zod、Valibot、ArkType 等），实现运行时验证和类型安全
- 🧠 智能响应解析器，自动处理不同内容类型的数据
- 📋 提供预定义路由和模式验证功能
- 🔌 支持插件和钩子机制，可扩展功能
- 🔄 内置高级重试机制，提升请求可靠性
- 🌐 完全兼容 fetch API，适用于多种 JavaScript 运行环境

---

### [GitHub - doganarif/fastapi-ai-sdk：用于Vercel AI SDK 后端实现的 FastAPI 辅助库 - 通过完全类型安全与 SSE 支持，将 AI 响应从 FastAPI 流式传输至 Next.js](https://github.com/doganarif/fastapi-ai-sdk)

**原文标题**: [GitHub - doganarif/fastapi-ai-sdk: FastAPI helper library for Vercel AI SDK backend implementation - Stream AI responses from FastAPI to Next.js with full type safety and SSE support](https://github.com/doganarif/fastapi-ai-sdk)

这是一个用于在 FastAPI 后端集成 Vercel AI SDK 的 Python 辅助库，支持从 FastAPI 向 Next.js 前端流式传输 AI 响应，具备完整类型安全和 SSE 支持。

- 🚀 **完全兼容 Vercel AI SDK** - 实现完整的 AI SDK 协议规范
- 🛡️ **Pydantic 类型安全** - 所有事件具有完整类型提示和验证
- 🌊 **流式传输支持** - 内置服务器发送事件（SSE）流式传输
- 🔧 **简单集成** - 提供 FastAPI 的简单装饰器和工具
- 🏗️ **灵活构建器模式** - 直观的 API 用于构建 AI 流
- ✅ **全面测试** - 具有完整的测试覆盖率
- 📚 **完整文档** - 包含示例的完整文档
- 📦 **MIT 许可证** - 开源项目，可自由使用
- 👥 **社区贡献** - 欢迎提交 Pull Request 进行功能改进

---

### [GitHub - andrewk17/vercel-deployment-menu-bar：开源macOS菜单栏应用，实时监控Vercel部署状态（构建/就绪/错误）。](https://github.com/andrewk17/vercel-deployment-menu-bar)

**原文标题**: [GitHub - andrewk17/vercel-deployment-menu-bar: Open-source macOS menu bar app to monitor Vercel deployment status in real time (build/ready/error).](https://github.com/andrewk17/vercel-deployment-menu-bar)

这是一个开源的 macOS 菜单栏应用程序，用于实时监控 Vercel 部署状态，支持构建/就绪/错误状态显示，并提供快速访问部署详情的功能。

- 🚀 实时监控 Vercel 部署状态（构建/就绪/错误）
- 🍎 专为 macOS 设计的原生 Swift 应用，轻量快速
- 🔐 支持个人账户和团队账户令牌配置
- 📱 已进行代码签名和公证，无 Gatekeeper 警告
- ⚙️ 提供预构建二进制文件和源码编译两种安装方式
- 🔑 需要 Vercel API 令牌进行配置
- 📋 团队使用需额外配置团队 ID
- 📄 采用 MIT 开源许可证
- 🛠️ 支持开发者进行代码签名和公证分发
- 🔄 自动轮询 Vercel API 更新部署状态

---

### [使用 Strapi AI 与 Vercel v0 进行内容建模](https://strapi.io/blog/building-a-page-builder-via-content-modeling-best-practices-in-strapi5?utm_campaign=19282052-Newsletter%20Sponsorships&utm_source=Nextjs&utm_medium=2nd-sponsor&utm_term=Strapi%20AI)

**原文标题**: [Content Modeling with Strapi AI and Vercel v0](https://strapi.io/blog/building-a-page-builder-via-content-modeling-best-practices-in-strapi5?utm_campaign=19282052-Newsletter%20Sponsorships&utm_source=Nextjs&utm_medium=2nd-sponsor&utm_term=Strapi%20AI)

本教程详细介绍了如何使用 Strapi 5 构建企业网站内容模型，结合 AI 工具提升开发效率。

- 🏗️ 内容建模基础：通过定义内容结构实现跨平台内容管理和复用，涵盖集合类型、单一类型、组件和动态区域等核心概念
- 🚀 Strapi 5 特性：深入解析内容类型分类系统，包括用于多实例的集合类型和单实例的单一类型，以及可复用的组件系统
- 🧩 动态区域应用：通过动态区域实现页面构建器功能，允许编辑者自由组合预定义组件（如 Hero 区块、FAQ 区块等）
- 🔗 关系管理：建立六种内容类型间的关系连接，实现内容跨上下文复用，避免数据冗余
- 📐 最佳实践：强调前期规划重要性，区分内容意图与视觉设计，合理使用关系和组件，避免过度嵌套
- 🤖 AI 加速开发：演示使用 Strapi AI 通过对话或上传图表快速生成内容模型，配合 Vercel v0 自动生成前端界面
- 🛠️ 实操指南：提供完整的企业网站建模步骤，包含 12 个集合类型、6 个可复用组件和动态区域配置实例

---

### [现代浏览器工作原理 - 作者：艾迪·奥斯马尼 - 进阶版](https://addyo.substack.com/p/how-modern-browsers-work)

**原文标题**: [How modern browsers work - by Addy Osmani - Elevate](https://addyo.substack.com/p/how-modern-browsers-work)

现代浏览器工作原理概述：从输入 URL 到页面渲染的完整流程，涵盖网络请求、HTML/CSS 解析、布局计算、渲染绘制、JavaScript 执行等核心环节，采用多进程架构确保安全性与稳定性。

- 🌐 **网络请求与资源加载**：浏览器通过独立网络进程处理 DNS 解析、TLS 握手、HTTP 请求，支持 HTTP/2/3 多路复用与预加载优化
- 📄 **HTML 解析与 DOM 构建**：流式解析 HTML 生成 DOM 树，遇到脚本标签会阻塞解析（可通过 async/defer 优化）
- 🎨 **CSS 解析与样式计算**：解析 CSS 规则生成 CSSOM，结合 DOM 计算每个节点的最终样式
- 📐 **布局计算**：根据盒模型和 CSS 布局算法计算每个元素的位置和尺寸，生成布局树
- 🖌️ **绘制与合成**：将布局树转换为绘制指令，通过分层和 GPU 加速合成最终画面
- ⚡ **JavaScript 执行**：V8 引擎采用多级 JIT 编译（Ignition→Sparkplug→Maglev→TurboFan）和并发垃圾回收
- 🔄 **模块加载**：ES 模块通过依赖图静态分析，支持动态 import() 和 import map 解析
- 🏗️ **多进程架构**：浏览器进程、渲染进程、GPU 进程、网络进程相互隔离，提升安全性和稳定性
- 🛡️ **安全沙箱**：渲染进程运行在受限环境中，结合站点隔离防止跨站数据泄露
- 🔧 **引擎差异**：Chromium(Blink)、Firefox(Gecko)、Safari(WebKit) 在样式计算、渲染流水线等方面各有优化策略

---

### [如何修复任何 Bug —— overreacted](https://overreacted.io/how-to-fix-any-bug/)

**原文标题**: [How to Fix Any Bug — overreacted](https://overreacted.io/how-to-fix-any-bug/)

在 React Router 应用中，滚动功能因网络请求调用而失效，通过系统化调试流程定位到 ScrollRestoration 组件与 scrollIntoView 的冲突问题。

- 🐛 滚动抖动问题出现在调用服务器请求后，原本正常的 scrollIntoView 功能失效
- 🤖 使用 Claude 调试时因缺乏可验证的复现步骤而多次失败
- 📋 通过创建可量化的复现步骤（测量滚动位置变化）建立有效测试基准
- 🔍 采用逐步删除代码策略，保持 bug 始终可复现的同时缩小问题范围
- ⚠️ 注意避免在简化过程中偏离原始问题，需验证修改与原始 bug 的关联性
- 🧩 最终发现是 React Router 旧版 ScrollRestoration 组件在路由验证时与滚动冲突
- 💡 通过将组件移出路由嵌套层临时解决，根本解决方案是更新依赖版本

---

### [better-auth 中未经认证 API 密钥创建导致的严重账户接管漏洞（CVE-2025-61928） - ZeroPath 博客 | ZeroPath](https://zeropath.com/blog/breaking-authentication-unauthenticated-api-key-creation-in-better-auth-cve-2025-61928)

**原文标题**: [Critical Account Takeover via Unauthenticated API Key Creation in better-auth (CVE-2025-61928) - ZeroPath Blog | ZeroPath](https://zeropath.com/blog/breaking-authentication-unauthenticated-api-key-creation-in-better-auth-cve-2025-61928)

ZeroPath 在 better-auth 的 API 密钥插件中发现了一个关键账户接管漏洞（CVE-2025-61928），允许攻击者未经认证为任意用户创建高权限凭证，该库每周下载量约 30 万次。漏洞存在于 API 密钥创建和更新端点，当请求缺少会话但包含用户 ID 时，系统会绕过权限验证直接使用攻击者控制的输入创建用户对象。攻击者可通过简单 POST 请求生成任意用户的 API 密钥，导致账户完全被接管。better-auth 已在 1.3.26 版本修复该漏洞，建议用户立即升级并轮换所有现有 API 密钥。

- 🔍 漏洞影响：攻击者可未经授权为任意用户创建 API 密钥，直接导致账户接管
- ⚙️ 技术原理：当请求缺少会话但包含 userId 时，系统绕过服务端验证直接使用攻击者提供的数据
- 🛡️ 修复方案：升级至 better-auth 1.3.26 或更高版本，并轮换所有现有 API 密钥
- 📅 时间线：10 月 1 日发现，10 月 3 日发布修复版本，10 月 9 日分配 CVE 编号
- 📊 检测方法：检查日志中未经认证的/api/auth/api-key/create 或 update 请求
- 🔬 发现过程：ZeroPath SAST 工具通过数据流分析识别出用户输入直接流入数据库操作

---

### [React Conf 2025 回顾 – React](https://react.dev/blog/2025/10/16/react-conf-2025-recap)

**原文标题**: [React Conf 2025 Recap – React](https://react.dev/blog/2025/10/16/react-conf-2025-recap)

React Conf 2025 于 10 月 7-8 日在美国内华达州亨德森举办，宣布成立 React 基金会并推出多项 React 与 React Native 新功能。

- 🎤 首日主题演讲发布 React 19.2 新特性：Activity 组件管理可见性、useEffectEvent 事件触发、性能追踪工具及部分预渲染功能
- 🚀 金丝雀版本推出 ViewTransition 页面过渡动画组件与 Fragment Refs 片段引用新交互方式
- ⚙️ React Compiler v1.0 正式发布，具备自动记忆化、智能检测规则、主流框架默认支持及迁移指南
- 🌉 React Native 0.82 将仅支持新架构，实验性 Hermes V1 引擎，新增 Web 对齐 DOM API 与性能监控 API
- 🎯 技术专题涵盖异步 React、性能优化、虚拟视图列表、性能追踪调试、Web 代码原生应用等前沿实践
- 🤝 设立 React 基金会统筹开源发展，社区案例覆盖电商、AI 应用、邮件开发、用户体验等多元场景

---

