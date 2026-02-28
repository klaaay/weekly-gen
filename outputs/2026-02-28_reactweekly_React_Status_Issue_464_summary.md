### [我们如何在一周内用 AI 重建 Next.js](https://blog.cloudflare.com/vinext/)

**原文标题**: [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)

Cloudflare 团队在短短一周内，借助 AI 辅助，成功构建了名为 vinext 的 Next.js 替代框架。该框架基于 Vite 构建，可无缝部署至 Cloudflare Workers，在早期测试中展现出更快的构建速度和更小的客户端包体积。

- 🚀 **快速构建与部署**：vinext 构建生产应用速度提升高达 4 倍，客户端包体积减少 57%，并支持一键部署至 Cloudflare Workers。
- 🔄 **全面兼容 Next.js API**：作为 Next.js 的直接替代品，它完整支持路由、服务端渲染、React 服务器组件等核心功能，现有项目可轻松迁移。
- ⚡ **基于 Vite 的现代化架构**：利用 Vite 及其高性能捆绑工具 Rolldown，提供更优的开发体验和构建性能。
- 🌐 **原生云平台集成**：深度集成 Cloudflare Workers，支持 KV、R2、Durable Objects 等原生服务，开发与生产环境一致。
- 🤖 **AI 驱动的高效开发**：项目主要由 AI 编写代码，配合全面测试套件，在短时间内实现高质量输出，开发成本仅约 1100 美元。
- 📊 **流量感知预渲染（实验性）**：创新性地根据实际访问流量智能预渲染页面，避免构建时全量渲染的资源浪费。
- ⚠️ **实验性阶段**：目前仍处于早期，尚未经过大规模流量验证，建议生产环境谨慎评估。

---

### [GitHub - cloudflare/vinext: 重新实现 Next.js API 界面的 Vite 插件——随处部署](https://github.com/cloudflare/vinext#whats-not-supported-and-wont-be)

**原文标题**: [GitHub - cloudflare/vinext: Vite plugin that reimplements the Next.js API surface — deploy anywhere](https://github.com/cloudflare/vinext#whats-not-supported-and-wont-be)

Vinext 是一个基于 Vite 构建的实验性插件，旨在重新实现 Next.js 的 API 接口，使现有的 Next.js 应用能够在 Vite 工具链上运行，并主要部署到 Cloudflare Workers 平台。它支持 App Router 和 Pages Router，提供与 Next.js 相似的开发体验，但强调快速构建、轻量级捆绑和 AI 驱动的开发模式。项目目前处于积极开发阶段，适合探索和演示，生产环境使用需谨慎。

- 🧪 **实验性项目** – 由 AI 驱动开发，大部分代码未经人工逐行审查，可能存在错误，使用时需自行承担风险。
- ⚡ **基于 Vite 构建** – 利用 Vite 的快速 HMR、原生 ESM 支持和丰富插件生态，重新实现 Next.js 的 API 接口。
- 🚀 **部署到 Cloudflare Workers** – 主要目标平台为零冷启动、全球分布的 Cloudflare Workers，支持通过 `vinext deploy` 一键部署。
- 🔄 **兼容 Next.js API** – 约 94% 的 Next.js 16 API 已实现，支持路由、SSR、RSC、Server Actions、缓存等核心功能。
- 🛠️ **简化迁移流程** – 提供 `vinext init` 命令和 AI Agent Skill，可自动化检查兼容性、安装依赖并生成配置，实现非破坏性迁移。
- 📦 **轻量级捆绑** – 得益于 Vite/Rollup 的树摇优化，生成的客户端包体积通常比 Next.js 更小。
- 🧪 **测试覆盖广泛** – 包含超过 1,700 个 Vitest 单元测试和 380 个 Playwright E2E 测试，确保功能稳定性。
- ⚠️ **已知限制** – 不支持 Vercel 特定功能、AMP 等；图片优化和 Google Fonts 处理方式与 Next.js 不同，部分功能为运行时实现。

---

### [从 Cloudflare 迁移到 Vercel | Vercel 知识库](https://vercel.com/kb/guide/migrate-to-vercel-from-cloudflare)

**原文标题**: [Migrate to Vercel from Cloudflare | Vercel Knowledge Base](https://vercel.com/kb/guide/migrate-to-vercel-from-cloudflare)

本文概述了从 Cloudflare Pages 或 Workers 迁移到 Vercel 的完整指南，涵盖项目设置、域名迁移、配置转换、环境变量迁移、URL 重定向、自定义头规则、Worker 函数迁移，以及 Cloudflare KV、R2、Durable Objects 等服务的替代方案，最后提供了功能映射和迁移后的测试建议。

- 🚀 **项目设置**：在 Vercel 仪表板中导入 Git 仓库，自动检测框架并部署，支持持续集成/部署。
- 🌐 **域名迁移**：在 Vercel 添加域名，更新 DNS 记录（A/CNAME），可零停机迁移，支持 SSL 证书预生成。
- ⚙️ **构建配置转换**：将 Cloudflare 的构建命令和输出目录迁移到 Vercel，可通过 `vercel.json` 或项目设置自定义。
- 🔐 **环境变量迁移**：收集 Cloudflare 的环境变量和密钥，在 Vercel 项目设置中添加，并支持多环境（开发、预览、生产）。
- 🔀 **URL 重定向与重写**：使用 `vercel.json` 或框架配置（如 Next.js）替代 Cloudflare 的 `_redirects` 文件，实现 301 重定向和路径重写。
- 🛡️ **自定义头规则迁移**：通过 `vercel.json` 或框架配置（如 Next.js 的 `headers()` 函数）设置 HTTP 头，替代 Cloudflare 的 `_headers` 文件。
- ⚡ **Worker 函数迁移**：将 Cloudflare Workers 代码转换为 Vercel Functions，支持 Node.js 等运行时，并利用 Fluid 计算提升并发性能。
- 🗃️ **KV 替换为 Redis**：使用 Redis（如通过 Vercel Marketplace）替代 Cloudflare Workers KV，需迁移数据并调整客户端代码。
- 📦 **R2 替换为 Vercel Blob**：使用 Vercel Blob 存储替代 Cloudflare R2，集成简单，支持公开或私有文件访问。
- 🔄 **Durable Objects 替换为 Redis**：结合 Redis 和开源库（如 `resumable-stream`）实现状态管理，替代 Cloudflare Durable Objects 的功能。
- 🛠️ **中间件转换**：使用 Vercel Routing Middleware 或 Next.js 中间件替代 Cloudflare Workers 的中间件功能，处理请求前逻辑。
- 🗺️ **功能映射参考**：提供 Cloudflare 功能（如 Pages、Workers、KV、R2 等）到 Vercel 对应服务（如 Functions、Redis、Blob 等）的映射表。
- ✅ **迁移后步骤**：完成迁移后全面测试应用，确保功能正常，并可利用 Vercel 社区获取支持。

---

### [未找到标题](https://x.com/rauchg/status/2026864132423823499)

**原文标题**: [No title found](https://x.com/rauchg/status/2026864132423823499)

该页面提示用户浏览器中 JavaScript 功能未启用或受阻，导致无法正常使用 X 平台（原 Twitter），并提供了相应的解决方案和支持信息。

- 🚫 JavaScript 未启用导致功能受限
- 🌐 建议启用 JavaScript 或更换受支持浏览器
- 🔧 可访问帮助中心查看浏览器兼容列表
- 🛡️ 隐私扩展插件可能影响访问，建议暂时禁用
- 🔄 提供“重试”功能应对加载故障
- 📜 页面底部包含平台服务条款与版权声明

---

### [TimescaleDB：PostgreSQL 时序数据库 | 虎数据 | 虎数据](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [TimescaleDB: PostgreSQL Time-Series DB | Tiger Data | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=react-status-newsletter)

TimescaleDB 是一个基于 Postgres 构建的时序数据库，提供高性能时序数据处理、实时分析和事件管理，适用于物联网、金融科技和实时分析等场景。它具备自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图等核心功能，并提供开源自托管和全托管云服务（Tiger Cloud）两种部署方式，支持弹性扩展、高可用性和安全合规。

- 🚀 **高性能时序处理**：通过自动分区（Hypertables）和行列混合存储，实现快速数据摄入与高效查询，支持海量时序数据管理。
- 📊 **智能数据压缩**：采用列式编码和时序感知压缩技术，最高可节省 95% 存储空间，并支持在压缩数据上直接进行过滤与聚合。
- 🔄 **实时分析优化**：提供增量物化视图（连续聚合）和时序专用函数，实现实时数据汇总与快速分析，支持延迟数据处理。
- ☁️ **全托管云服务优势**：Tiger Cloud 提供一键部署、自动分层存储、弹性计算、多可用区高可用及安全合规支持，降低运维复杂度。
- 🔧 **开源与自托管灵活**：支持在任何 PostgreSQL 环境中自部署，包含核心时序功能，但云服务特有功能需自行管理。
- 🌐 **多场景应用**：广泛用于物联网设备监控、金融科技市场数据、实时客户分析等领域，受 Cloudflare、Replicated 等企业信赖。
- ⚙️ **自动化管理**：内置任务调度器，支持数据保留、压缩、分层存储等策略自动化，并提供作业监控与告警功能。
- 🛠️ **开发与支持**：拥有活跃开发者社区，提供 24/7 专家技术支持、详细文档和性能优化工具，助力从原型到生产级部署。

---

### [React 基金会：由 Linux 基金会托管的新 React 家园](https://react.dev/blog/2026/02/24/the-react-foundation)

**原文标题**: [The React Foundation: A New Home for React Hosted by the Linux Foundation – React](https://react.dev/blog/2026/02/24/the-react-foundation)

React Foundation 正式成立，由 Linux Foundation 托管，标志着 React、React Native 及相关项目脱离 Meta，成为独立开源项目。该基金会由八家铂金创始成员支持，并设立临时领导委员会以确立技术治理结构，未来将逐步完成基础设施转移并规划生态支持计划。

- 🏛️ React Foundation 正式启动，由 Linux Foundation 托管，React、React Native 和 JSX 等项目不再属于 Meta
- 🤝 八家铂金创始成员包括 Amazon、Callstack、Expo、Huawei、Meta、Microsoft、Software Mansion 和 Vercel
- 🧑‍💼 基金会由各成员代表组成的董事会管理，Seth Webster 担任执行董事
- 🛠️ 设立临时领导委员会，独立制定 React 技术治理结构，未来几个月将公布进展
- 📅 后续步骤包括完善技术治理、转移代码库与基础设施、规划生态支持项目及筹备下一届 React Conf
- 🙏 感谢全球贡献者与开发者社区，React Foundation 的成立源于社区的共同努力

---

### [创建查询抽象](https://tkdodo.eu/blog/creating-query-abstractions)

**原文标题**: [Creating Query Abstractions](https://tkdodo.eu/blog/creating-query-abstractions)

本文探讨了在 React Query 中创建查询抽象的最佳实践，指出自定义钩子作为抽象方式存在局限性，并推荐使用`queryOptions` API 来更灵活、类型安全地共享查询配置。

- 🛠️ 自定义钩子作为查询抽象存在限制，如无法在非组件环境使用、难以适应不同钩子变体（如`useSuspenseQuery`）
- 🔧 使用`UseQueryOptions`类型传递选项时，容易导致类型推断问题，如返回数据变为`unknown`
- 🚀 React Query v5 引入的`queryOptions` API 成为更优抽象方案，它仅是纯函数，可在任何环境使用
- 🧩 `queryOptions`支持灵活组合，基础配置（如`queryKey`和`queryFn`）可共享，具体选项可在调用时覆盖
- ✅ 该方法保持完整类型推断，代码简洁如 JavaScript，解决了自定义钩子的所有痛点

---

### [React Native 登陆 Meta Quest · React Native](https://reactnative.dev/blog/2026/02/24/react-native-comes-to-meta-quest)

**原文标题**: [React Native Comes to Meta Quest · React Native](https://reactnative.dev/blog/2026/02/24/react-native-comes-to-meta-quest)

React Native 现已正式支持 Meta Quest 设备，允许开发者使用熟悉的 React Native 工具和模式构建 VR 应用。Meta Quest 运行基于 Android 的 Meta Horizon OS，因此现有的 Android 工具链和开发流程基本适用。开发者可通过 Expo Go 快速开始开发，并通过开发构建访问原生功能。项目需进行一些平台特定配置，并注意设计时需考虑 VR 的交互和显示特性。

- 🚀 **React Native 扩展至 VR 平台**：在 React Conf 2025 上宣布正式支持 Meta Quest，延续其跨平台愿景。
- 🛠️ **开发流程与 Android 相似**：基于 Meta Horizon OS（Android 衍生系统），可使用现有 Android 工具链进行开发和调试。
- 📱 **快速入门使用 Expo Go**：在头显上安装 Expo Go 后，通过扫描 QR 码即可运行和实时迭代应用。
- ⚙️ **开发构建访问原生功能**：需通过 Expo 开发构建来集成原生模块或深度平台功能。
- 🔧 **平台特定配置要求**：需使用 `expo-horizon-core` 插件配置应用 ID、默认面板尺寸和支持的设备等。
- 📚 **库兼容性需注意**：大多数 React Native 库可用，但依赖移动设备硬件或 Google 服务的库可能需要调整。
- 🎨 **VR 设计需特殊考量**：界面需适应头戴显示，使用更大点击目标、清晰排版，并支持控制器和手势等多种输入方式。
- 🔗 **提供丰富参考资料**：包括示例项目、官方设计指南、文档和社区资源，帮助开发者深入学习和实践。

---

### [生命短暂，何必手写 API 类型：OpenAPI 驱动的 React——火星编年史，邪恶火星人团队博客](https://evilmartians.com/chronicles/lifes-too-short-to-hand-write-api-types-openapi-driven-react)

**原文标题**: [Life's too short to hand-write API types: OpenAPI-driven React—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/lifes-too-short-to-hand-write-api-types-openapi-driven-react)

本文介绍了如何通过 OpenAPI 规范驱动 React 前端开发，实现前后端类型自动同步，避免手动维护 API 类型导致的错误。通过工具链自动生成类型、客户端和验证模式，并结合状态管理与 API 模拟，提升开发效率和代码质量。

- 🛠️ **使用 OpenAPI 作为唯一数据源**：通过 Hey API 工具从 OpenAPI 规范自动生成 TypeScript 类型、SDK 函数和 Zod 验证模式，确保前后端类型一致。
- 🔄 **状态管理优化**：采用 Nanostores 和 Nanoquery 管理 API 状态，实现数据缓存、共享和自动更新，减少组件内的重复逻辑。
- 📝 **表单与验证集成**：利用生成的 Zod 模式与 React Hook Form 结合，实现基于 API 合约的自动表单验证，提升开发体验。
- 🎭 **网络层 API 模拟**：使用 MSW（Mock Service Worker）拦截网络请求，提供真实的 API 模拟环境，支持并行开发和边缘情况测试。
- ⚙️ **配置驱动开发**：通过环境变量动态切换模拟与真实 API，确保开发、测试和生产环境的一致性。

---

### [Cloud 66 - 将您的应用程序部署至任意云端](https://www.cloud66.com/)

**原文标题**: [Cloud 66 - Deploy Your Applications to Any Cloud](https://www.cloud66.com/)

Cloud 66 是一个应用部署与管理平台，支持在任何云服务商或自有服务器上构建、部署和扩展应用，提供从安全到监控的全方位服务，无需改变现有架构。

- 🚀 **支持任意部署**：可在任何云平台或自有服务器上部署应用，无供应商锁定。
- 🛠️ **兼容多样架构**：支持向量数据库、AI 代理、时序数据库、PostgreSQL 自定义扩展、遗留软件、机器学习模型等多种技术栈。
- 📦 **全流程管理**：涵盖从代码连接到部署的完整流程，并提供复杂的部署策略如零停机、蓝绿部署等。
- 🔧 **高级运维功能**：包括自动扩展、团队权限管理、预览部署、托管数据库、服务器加固、SSL 证书和监控告警。
- ⚙️ **完全控制权**：用户对服务器拥有完全控制，可自定义配置和安装任意软件。
- 🤝 **协同工作平台**：为开发者和运维人员提供无缝协作工具，简化基础设施管理。

---

### [使用异步 React 构建具有动作属性的设计组件 | 奥罗拉·沙尔夫](https://aurorascharff.no/posts/building-design-components-with-action-props-using-async-react/)

**原文标题**: [Building Design Components with Action Props using Async React | Aurora Scharff](https://aurorascharff.no/posts/building-design-components-with-action-props-using-async-react/)

本文介绍了如何利用 Async React 的 `useTransition` 和 `useOptimistic` 钩子，通过“操作属性（action props）”模式构建具备乐观更新和加载状态管理的可复用组件，从而提升用户体验并简化消费者代码。

- 🚀 **Async React 核心概念**：React Conf 2025 提出的 Async React 包含异步设计、路由和数据三层，本文聚焦设计层，通过操作属性模式封装异步逻辑。
- 🔧 **操作属性模式基础**：组件内部使用 `useTransition` 管理异步操作的挂起状态，`useOptimistic` 实现乐观更新，消费者只需传入值和操作函数，无需处理复杂状态。
- 📑 **TabList 组件示例**：通过逐步添加挂起状态指示器和乐观更新，使标签切换即时响应，并在异步操作期间显示加载反馈，最终提供完整的可定制实现。
- ✏️ **EditableText 组件示例**：为内联编辑文本字段集成乐观更新，支持自定义格式化显示值，确保用户编辑后界面立即更新，同时处理异步保存状态。
- 🎯 **关键优势**：操作属性模式将异步协调、错误处理和状态回滚封装在组件内部，消费者代码保持简洁，同时获得一致的交互反馈和更流畅的用户体验。
- 🔮 **未来展望**：该模式适用于各种交互组件，理想情况下应由组件库内置支持，目前开发者可自行实现以提升应用响应性和可维护性。

---

### [指南：AI 编程助手 | Next.js](https://nextjs.org/docs/app/guides/ai-agents)

**原文标题**: [Guides: AI Coding Agents | Next.js](https://nextjs.org/docs/app/guides/ai-agents)

Next.js 为 AI 编程助手提供版本匹配的本地文档，通过在项目根目录添加 `AGENTS.md` 文件，引导助手优先读取 `node_modules/next/dist/docs/` 中的最新文档，而非依赖可能过时的训练数据，从而确保代码建议的准确性和时效性。

- 📦 **内置版本匹配文档** - Next.js 将官方文档打包至 `node_modules/next/dist/docs/`，结构与线上文档一致，确保助手始终访问与项目版本完全对应的准确 API 参考。
- 📄 **引导文件配置简单** - 在项目根目录创建 `AGENTS.md` 文件，其中包含明确指令，要求助手在编写任何 Next.js 代码前必须先查阅本地捆绑的文档。
- 🚀 **新项目自动生成** - 使用 `create-next-app` 创建新项目时会自动生成 `AGENTS.md` 和 `CLAUDE.md` 文件；也可通过 `--no-agents-md` 参数跳过生成。
- 🔧 **现有项目轻松升级** - 确保 Next.js 版本在 v16.2.0-canary.37 或更高，然后手动添加上述引导文件即可启用该功能。
- 🎯 **指令精炼专注** - `AGENTS.md` 的核心指令简洁明确，专注于将助手从过时的训练数据重定向到准确的本地文档，开发者还可在此文件的规定标记外添加项目特定的说明。

---

### [获取失败](https://surveyjs.hashnode.dev/build-dynamic-json-driven-forms-react)

**原文标题**: [Failed to retrieve](https://surveyjs.hashnode.dev/build-dynamic-json-driven-forms-react)

无法总结：获取内容失败，状态码 403。

---

### [Yoopta 编辑器 | 适用于 React 的无头富文本编辑器](https://yoopta.dev/)

**原文标题**: [Yoopta Editor | Headless Rich Text Editor for React](https://yoopta.dev/)

Yoopta 是一款免费开源的富文本编辑器框架，提供 20 多种插件、拖放功能、主题预设和完整的 API 控制，支持构建类似 Notion 的编辑器或自定义 CMS 应用，具备高性能、移动友好和 TypeScript 支持等特点。

- 🆓 **免费开源** – 完全免费，MIT 许可，可用于商业项目
- 🧩 **插件丰富** – 内置 20+ 插件（段落、表格、代码、媒体等），支持自定义插件
- 🎨 **主题预设** – 提供浅色/深色主题及 Shadcn UI 等预设
- 🖱️ **交互灵活** – 支持拖放排序、多块选择、键盘快捷键和触摸优化
- 📤 **多格式导出** – 可导出为 HTML、Markdown、纯文本等格式
- 📱 **跨平台兼容** – 响应式设计，适配移动设备，性能优异
- 🔧 **开发友好** – 基于 TypeScript，提供完整 API 和撤销/重做功能
- 🚀 **未来规划** – 即将推出实时协作、AI 编辑、插件市场等高级功能

---

### [互动游乐场 | Yoopta 编辑器](https://yoopta.dev/playground)

**原文标题**: [Interactive Playground | Yoopta Editor](https://yoopta.dev/playground)

Yoopta 是一款用于构建富文本编辑器的开源 React 库，目前处于 Beta 版本，提供示例、文档和交互式演示。

- 🚀 提供交互式演示（Playground v6 Beta），可实时体验编辑器功能
- 📚 包含详细文档和代码示例，帮助开发者快速上手
- 🔧 支持查看源代码，便于自定义和扩展
- ⭐ 鼓励用户关注项目仓库，获取最新更新
- ⏱️ 宣称可在几分钟内开始使用，降低开发门槛

---

### [Expo SDK 55 - 更新日志](https://expo.dev/changelog/sdk-55)

**原文标题**: [Expo SDK 55 - Expo Changelog](https://expo.dev/changelog/sdk-55)

Expo SDK 55 正式发布，包含 React Native 0.83 和 React 19.2，引入了多项新功能与改进，包括项目模板重构、Hermes v1 可选支持、AI 工具扩展、Brownfield 应用支持增强、Expo Router 原生功能优化以及多个模块的更新与性能提升。

- 🚀 **SDK 55 发布**：包含 React Native 0.83 和 React 19.2，感谢所有参与测试的人员。
- ⏳ **过渡期安排**：Expo Go 应用商店版本暂留 SDK 54，新项目默认使用 SDK 54，建议迁移至开发构建以获得完整功能。
- 🎨 **项目模板重构**：采用原生标签页 API，优化设计，引入 `/src` 文件夹结构，提升开发体验。
- 🏗️ **弃用旧架构**：SDK 55 起不再支持旧架构，相关配置选项已移除。
- ⚡ **Hermes v1 可选**：提供性能改进和现代 JavaScript 功能支持，但需从源码构建 React Native，可能增加构建时间。
- 📦 **Hermes 字节码差分**：通过 `expo-updates` 和 EAS Update 优化更新包大小，减少下载时间和带宽使用。
- 🤖 **AI 工具扩展**：Expo MCP 支持 CLI 操作和 EAS 查询，新增官方 AI 技能库，帮助构建和调试应用。
- 🔗 **Brownfield 应用增强**：引入 `expo-brownfield` 包，支持集成和隔离两种开发模式，改进现有原生应用整合。
- 📱 **Expo Router 功能**：新增 Colors API、Apple Zoom 过渡、Stack.Toolbar API、实验性 SplitView 支持等，提升原生体验。
- 🛠️ **Expo UI 进展**：Jetpack Compose API 升级至 Beta，SwiftUI 组件 API 更新，更贴近原生开发模式。
- 📦 **包版本统一**：所有 Expo SDK 包版本与 SDK 主版本一致，便于兼容性管理。
- 🔧 **Expo Modules Core 改进**：采用 Swift 6，增加 ArrayBuffer 支持，优化模块开发。
- 🖥️ **Expo CLI 更新**：改进开发服务器启动界面，支持环境文件，修复本地网络访问问题。
- 📲 **实验性功能**：`expo-widgets` 支持 iOS 主屏幕小组件，`expo-blur` 在 Android 上稳定，`expo-sharing` 支持接收共享数据。
- 🌐 **Web 与模块更新**：Expo Web 支持服务器端渲染，多个模块（如 `expo-audio`、`expo-sqlite`）新增功能与优化。
- ⚠️ **弃用与破坏性变更**：移除旧配置字段，更新工具链，调整最低 iOS 版本计划，详细变更请参考日志。
- 🔄 **升级指南**：提供升级步骤，包括依赖更新、检查问题、处理破坏性变更，并推荐使用 AI 技能辅助升级。

---

### [如何升级到 Expo SDK 55](https://expo.dev/blog/upgrading-to-sdk-55)

**原文标题**: [How to upgrade to Expo SDK 55](https://expo.dev/blog/upgrading-to-sdk-55)

Expo SDK 55 已发布，支持 React Native 0.83.2 和 React 19.2，最低支持 Android 7+ 和 iOS 15.1+。升级时需注意新架构迁移、expo-av 包替换为 expo-video/expo-audio，并建议使用开发构建而非 Expo Go。本文提供了逐步升级指南、常见问题排查建议以及社区支持资源。

- 🚀 **Expo SDK 55 核心更新**：基于 React Native 0.83.2 和 React 19.2，支持 Android API 36+ 和 Xcode 16.1+，最低系统要求为 Android 7 和 iOS 15.1。
- ⚠️ **强制迁移新架构**：SDK 55 不再支持旧架构，需升级至新架构（默认从 SDK 53 开始），建议先在新架构下测试 SDK 54，再单独升级至 SDK 55。
- 🤖 **AI 辅助升级工具**：可通过 Claude Code 安装 Expo 技能库，使用自然语言指令自动化处理包版本更新、破坏性变更和配置清理。
- 📱 **Expo Go 过渡期安排**：应用商店的 Expo Go 暂保留 SDK 54，新项目默认使用 SDK 54；建议在此期间迁移至开发构建，以更稳定地测试和生产部署。
- 🎬 **多媒体包替换**：expo-av 包已移除，需迁移至新版 expo-video 和 expo-audio 包。
- ⚡ **Hermes v1 性能优化**：可选启用 Hermes v1 编译器以提升性能，但可能增加构建时间（需从源码编译 React Native）。
- 🔍 **升级前必读变更日志**：升级前后务必查阅 SDK 55 变更日志，了解破坏性变更和配置调整，避免常见错误。
- 🛠️ **推荐使用开发构建**：开发构建能避免 Expo Go 自动升级的干扰，支持完整应用配置，且免费计划提供足够构建额度。
- 🐛 **系统化故障排查**：遇到问题时，参考官方故障排查指南，按错误类型（构建失败、崩溃等）采取对应措施，并利用日志工具定位原生错误。
- 👥 **社区支持与反馈**：通过 GitHub 提交最小化复现问题，或在 Discord、Reddit 等社区讨论升级难题，Expo 团队提供多渠道支持。

---

### [发布 v0.3.0 · software-mansion-labs/react-native-enriched-markdown · GitHub](https://github.com/software-mansion-labs/react-native-enriched-markdown/releases/tag/0.3.0)

**原文标题**: [Release v0.3.0 · software-mansion-labs/react-native-enriched-markdown · GitHub](https://github.com/software-mansion-labs/react-native-enriched-markdown/releases/tag/0.3.0)

React Native Enriched Markdown 库发布了 0.3.0 版本，引入了表格支持、自动链接、任务列表、RTL 支持等新功能，并进行了多项错误修复和性能优化。

- 📊 新增表格支持，提升 Markdown 内容的结构化展示能力
- 🔗 添加自动链接功能，自动识别并转换文本中的链接
- ✅ 实现任务列表支持，便于创建和管理待办事项
- 📱 改进 iOS 文本测量，使其与 React Native 的 Text 组件对齐
- 🔧 修复多项问题，包括行间距渲染、默认字体大小调整等
- 🌐 增强 RTL（从右到左）支持，优化有序/无序列表和引用块的显示
- 🏗️ 重构代码结构，移除已弃用的工具类并优化导入
- 📚 更新文档，包含夜间构建安装说明和 README 增强
- 🚀 引入持续集成工作流，支持夜间构建
- 👥 新增两位贡献者，共同推动项目发展

---

### [发布 v9.14.0 · gpbl/react-day-picker · GitHub](https://github.com/gpbl/react-day-picker/releases/tag/v9.14.0)

**原文标题**: [Release v9.14.0 · gpbl/react-day-picker · GitHub](https://github.com/gpbl/react-day-picker/releases/tag/v9.14.0)

react-day-picker 发布了 v9.14.0 版本，引入了重置选择功能与伊斯兰历支持，并包含多项改进。

- 📅 新增 `resetOnSelect` 属性，可在范围选择模式下重置已选范围
- 🌙 新增对伊斯兰历（希吉来历，Umm al-Qura）的支持
- 🌐 为 DayPicker 根元素添加默认 `lang` 属性
- 👥 本次更新包含三位贡献者的提交，其中一位为首次贡献
- 🔗 详细更新内容与示例可查阅官方文档与演示平台

---

### [GitHub - MatthewHerbst/react-to-print: 在浏览器中打印 React 组件](https://github.com/MatthewHerbst/react-to-print)

**原文标题**: [GitHub - MatthewHerbst/react-to-print: Print React components in the browser](https://github.com/MatthewHerbst/react-to-print)

react-to-print 是一个用于在浏览器中打印 React 组件的库，支持动态内容、自定义样式和多种打印配置，兼容现代浏览器，但在移动端 WebView 中存在限制。

- 📦 **功能概述**：react-to-print 允许开发者直接打印 React 组件内容，支持通过 ref 引用动态内容，并提供丰富的 API 配置选项。
- 🛠️ **核心用法**：通过 `useReactToPrint` hook 设置打印内容引用，触发打印按钮即可调用浏览器打印对话框。
- ⚙️ **API 特性**：支持自定义打印样式、字体加载、错误处理、前后回调函数，以及通过 `print` 属性适配非浏览器环境如 Electron。
- 📱 **兼容性说明**：兼容大多数现代浏览器，但在移动端 WebView 中可能无法正常工作，且 Firefox Android 不支持。
- ⚠️ **常见问题**：包括样式继承限制、动态标题设置、Class 组件支持需手动转发 ref，以及打印对话框设置不可修改等。
- 🖨️ **样式与布局**：提供 CSS 媒体查询控制打印内容显示，支持页面方向、尺寸、边距设置，并处理滚动容器和分页问题。
- 🔧 **故障排除**：针对空白页、样式错乱、分页异常等问题提供解决方案，如调整 CSS 属性或使用 `preserveAfterPrint`。
- 📚 **本地运行与资源**：项目使用 Node ^20 构建，提供本地运行指南，并列出相关包如 vue-to-print 和贡献者信息。

---

### [STRICH | 网页应用条码扫描](https://strich.io/?ref=react-status)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=react-status)

STRICH 是一款用于网页应用的 JavaScript 条码扫描库，支持实时扫描一维和二维条码，无需原生应用或后端支持。

- 📦 通过 npm 安装，提供免费 30 天试用和透明定价
- 🚀 基于现代 Web 技术（WebAssembly/WebGL），兼容主流浏览器与框架
- 🎯 支持多种一维/二维条码类型，内置扫描 UI 和弹窗扫描器
- 💪 可读取磨损、低光照、反色等复杂场景条码，性能优于免费方案
- 🏢 提供企业级功能：白标定制、离线部署、GS1 认证支持
- 💬 包含多行业客户实证，展示图书馆、医疗、零售等成功案例
- 🌐 网页应用优势：无应用商店限制、跨平台、低成本开发、PWA 支持
- 💰 分层定价方案（基础版$99/月起），支持银行转账和企业定制

---

### [React Native 2025 现状](https://results.stateofreactnative.com/en-US/)

**原文标题**: [State of React Native 2025](https://results.stateofreactnative.com/en-US/)

2025 年 React Native 社区调查结果显示，新架构采用率已达 80%，生态系统持续成熟，显著改善了调试等常见痛点，调查不仅帮助开发者掌握最新工具与最佳实践，还通过追踪采用情况和社区反馈引导生态发展方向。

- 📊 新架构采用率达 80%，为众多库开启新可能
- 🛠️ 生态系统日益成熟，显著改善调试等痛点
- 📈 调查成为社区重要资源，助力开发者紧跟前沿
- 🧭 通过追踪采用情况与社区反馈，引导生态未来改进
- 📧 鼓励留下邮箱订阅，以便获取下一次调查结果

---

### [React Native 2025 现状：React Native 架构](https://results.stateofreactnative.com/en-US/react-native-architecture/)

**原文标题**: [State of React Native 2025: React Native architecture](https://results.stateofreactnative.com/en-US/react-native-architecture/)

本文基于 React Native 社区调查数据，分析了开发者对架构 API 的使用情况、版本升级策略、新架构迁移现状以及跨平台开发实践。

- 🏗️ 大多数开发者已迁移或计划迁移至新架构，生态正逐步淘汰旧方案，Nitro 模块等新 API 日益普及
- 📊 版本升级策略中，近半数开发者选择跟随 Expo SDK 发布进行升级，保持最新版本或偶尔升级也占较高比例
- 🔄 新架构迁移率高达 79%，仅少数项目尚未计划迁移，显示社区已广泛接纳新架构
- 🏢 项目类型以独立新应用为主（占 79%），集成现有应用或两者混合的项目占比较小
- 🛠️ 开发框架中 Expo CLI 占据主导地位（86%），React Native 社区 CLI 也有近半数使用率
- 📱 平台 API 使用率前三名为新架构（74%）、Hermes 运行时（60%）和 Expo 模块 API（53%）
- ☁️ 空中更新方案中 EAS Update 以 80% 使用率遥遥领先，CodePush 等替代方案占比较低
- 🌐 跨平台代码共享方面，42% 项目未采用共享策略，React Native Web（39%）是最流行的共享方案

---

### [Bun v1.3.10 | Bun 博客](https://bun.com/blog/bun-v1.3.10)

**原文标题**: [Bun v1.3.10 | Bun Blog](https://bun.com/blog/bun-v1.3.10)

Bun v1.3.1 版本发布，带来了全新的原生 REPL、更快的构建与性能优化、对现代 ES 装饰器的完整支持、Windows ARM64 原生支持，以及多项错误修复与改进。

- 🚀 **全新原生 REPL**：用 Zig 重写，启动迅速，支持语法高亮、多行输入、持久历史记录和 Tab 自动补全等丰富功能。
- 📦 **构建优化**：新增 `--compile --target=browser` 选项，可生成内联所有资源的独立 HTML 文件；引入 Barrel 导入优化，提升大型库的构建速度。
- 🛠 **完整支持 TC39 标准 ES 装饰器**：包括 `accessor` 关键字、装饰器元数据和正确的求值顺序，满足了长期以来的社区需求。
- ⚡ **性能大幅提升**：包括更快的 `structuredClone`（对数组最高提速 25 倍）、`Buffer.slice()`、`path.parse()` 以及 JavaScriptCore 引擎的多项优化。
- 🪟 **新增 Windows ARM64 原生支持**：可在 ARM64 Windows 设备上安装运行，并支持交叉编译为独立可执行文件。
- 🔧 **多项功能增强**：`bun test` 新增 `--retry` 标志；TLS 自定义配置现支持连接复用；更新了根证书列表。
- 🐛 **大量错误修复**：涵盖了 Node.js 兼容性、Bun API、Web API、`bun install`、JavaScript 打包器、CSS 解析器、Bun Shell 和 Windows 平台等方面的诸多问题。

---

### [Deno 2.7：Temporal API、Windows ARM 支持与 npm 覆盖功能 | Deno](https://deno.com/blog/v2.7)

**原文标题**: [Deno 2.7: Temporal API, Windows ARM, and npm overrides | Deno](https://deno.com/blog/v2.7)

Deno 2.7 版本发布，带来多项重要更新，包括 Temporal API 稳定化、Windows ARM 原生支持、npm overrides 支持，以及大量 Node.js 兼容性改进和开发者体验优化。

- 🗓️ **Temporal API 稳定化**：Temporal API 现已稳定，无需 `--unstable-temporal` 标志，提供更强大的日期时间处理能力。
- 🪟 **Windows ARM 原生支持**：提供官方 Windows ARM 构建版本，可在 Surface Pro X 等设备上实现原生性能运行。
- 📦 **package.json overrides 支持**：支持 `overrides` 字段，允许精确控制依赖树中深层包的版本，便于修复安全漏洞或强制兼容性。
- ⚙️ **新的子进程 API**：新增 `Deno.spawn()`、`Deno.spawnAndWait()` 等简化函数（目前标记为不稳定），用于更方便地运行子进程。
- 🔧 **Node.js 兼容性大幅提升**：修复了 `node:worker_threads`、`node:child_process`、`node:zlib`、`node:sqlite` 等模块的数十个问题。
- 🚀 **性能与 API 增强**：包括 `navigator.platform` 支持、Brotli 压缩流、非阻塞文件锁 `FsFile.tryLock()`、SHA3 加密算法支持以及 GIF/WebP 图像解码。
- 📦 **包管理器功能改进**：新增 `deno create` 命令、`deno install --compile` 编译独立可执行文件、`--save-exact` 精确版本锁定、`jsr:` 协议支持以及 `deno audit --ignore` 忽略特定安全建议。
- ✨ **开发者体验优化**：`deno compile` 新增 `--self-extracting` 自解压模式、`deno task` 支持更多 Shell 配置、`deno check --check-js` 支持纯 JavaScript 类型检查、调试器增强支持 Web Workers、`deno upgrade` 加入缓存和校验和验证、支持 `SSLKEYLOGFILE` 环境变量以及为 `Deno.cron` 集成 OpenTelemetry 追踪。
- ⚡ **引擎升级**：V8 引擎升级至 14.5 版本，带来性能提升和新特性。
- 🙏 **致谢社区**：感谢众多贡献者的代码提交、问题反馈和社区支持。

---

### [Tailwind CSS v4.2 新增的四种新配色方案](https://superhighway.dev/tailwind-v4-2-new-palettes)

**原文标题**: [The Four New Color Palettes added to Tailwind CSS v4.2](https://superhighway.dev/tailwind-v4-2-new-palettes)

Tailwind CSS v4.2 新增了四种中性色调色板，为开发者提供了更柔和、低调的颜色选择，适用于需要细微色彩而非鲜明对比的设计场景。

- 🎨 **新增四种中性色调色板**：包括 Mauve（淡紫粉调）、Olive（黄绿调）、Mist（蓝青调）和 Taupe（棕灰调），均为低饱和度、柔和的色调。
- 🌫️ **设计定位为中性色系**：这些调色板与现有的 Slate、Zinc 类似，提供“温和”的色彩选项，适合需要低调配色的界面设计。
- 🎯 **基于 OKLCH 色彩空间**：所有颜色均使用 OKLCH（亮度、色度、色调角）定义，确保色彩过渡视觉均匀，且色度极低（约 0.031–0.034），保持中性特质。
- 🖼️ **提供完整色彩阶梯示例**：每种调色板均展示从 50 到 950 的渐变色阶，并附有组件（如卡片、按钮、徽章）应用效果，方便直观对比。
- 📊 **包含详细色彩参数**：文章列出了每个色阶的 HEX 色值和 OKLCH 具体数值，供开发者直接参考使用。

---

### [导航 API - 更优导航方式，现已基线新可用 | 博客 | web.dev](https://web.dev/blog/baseline-navigation-api?hl=en)

**原文标题**: [Navigation API - a better way to navigate, is now Baseline Newly Available  |  Blog  |  web.dev](https://web.dev/blog/baseline-navigation-api?hl=en)

单页应用（SPA）的导航长期以来依赖不完善的 History API，存在诸多限制。新的 Navigation API 现已全面可用，它通过统一的事件处理机制，简化了客户端路由，支持程序化导航、表单提交、异步滚动和视图过渡，为现代 Web 应用提供了更强大、更可靠的导航解决方案。

- 🚀 Navigation API 已全面可用，解决了 History API 在单页应用导航中的长期痛点
- 🔄 通过统一的 `navigate` 事件处理所有导航（链接点击、前进/后退、程序调用）
- ⚡ 自动处理 URL 更新、历史栈管理和可访问性，无需手动调用 `pushState`
- 📝 支持拦截表单提交，通过 `formData` 属性直接获取数据，避免页面重载
- 🧭 提供手动滚动控制（`scroll: 'manual'`），确保内容加载后再恢复滚动位置
- 🎬 与 View Transitions API 无缝集成，可实现流畅的视觉过渡效果
- 🛠️ 简化了路由器的构建，减少了边缘情况处理，提高了开发效率和可靠性

---

