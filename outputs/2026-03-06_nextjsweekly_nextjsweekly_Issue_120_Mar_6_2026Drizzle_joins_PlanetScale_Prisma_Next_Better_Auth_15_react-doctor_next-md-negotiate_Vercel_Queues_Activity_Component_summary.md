### [Prisma ORM 的下一阶段进化](https://www.prisma.io/blog/the-next-evolution-of-prisma-orm?ref=nextjsweeky)

**原文标题**: [The Next Evolution of Prisma ORM](https://www.prisma.io/blog/the-next-evolution-of-prisma-orm?ref=nextjsweeky)

Prisma 团队宣布正在开发 Prisma Next，这是 Prisma ORM 的下一代 TypeScript 重构版本，旨在通过可扩展和可组合的架构解决现有代码库的限制，同时保留声明式模式和模型优先查询体验。它引入了新的查询构建器、对 AI 工作流的优化、更安全的迁移系统，并计划支持 MongoDB。Prisma 7 将继续维护，而 Prisma Next 成熟后将作为 Prisma 8 发布。

- 🚀 **Prisma Next 发布**：Prisma ORM 的下一代 TypeScript 重构版本，旨在提升可扩展性和性能。
- 🔧 **架构革新**：通过完全重写解决现有代码库的限制，支持模块化扩展和组合。
- 📝 **查询优化**：改进查询 API，减少深层嵌套的复杂性，引入类型安全的 SQL 查询构建器。
- 🗂️ **灵活模式定义**：支持传统的 Prisma 模式语言和新的 TypeScript 模式定义方式。
- 🧩 **扩展生态系统**：允许通过插件（如 PGVector）扩展数据模型和查询功能。
- 🤖 **AI 与代理支持**：为 AI 代理工作流设计，提供编译时检查、机器可读错误和快速反馈循环。
- 🛡️ **中间件与验证**：新增查询中间件（如查询检查和预算控制），并在各层进行严格验证以确保安全。
- 🌐 **数据库支持**：初始支持 PostgreSQL，未来将扩展至 MongoDB 等非 SQL 数据库，提供原生体验。
- 📊 **高级查询功能**：新增 GROUP BY 聚合、流式处理大数据集和自定义模型方法。
- 🗺️ **迁移改进**：采用图结构管理迁移，支持分支、压缩和基线功能，未来将加入数据迁移。
- ⏳ **版本规划**：Prisma 7 继续维护并更新路线图，Prisma Next 将在稳定后作为 Prisma 8 发布。
- 🌍 **开源协作**：代码库已公开，鼓励社区通过 GitHub 和 Discord 参与讨论和贡献。

---

### [你可以直接部署智能体：为智能体时代构建架构 | Dom Sipowicz, Vercel - YouTube](https://www.youtube.com/watch?v=_TRV6fPUMJw&feature=youtu.be)

**原文标题**: [You Can Just Ship Agents: Architecting for the Agentic Era | Dom Sipowicz, Vercel - YouTube](https://www.youtube.com/watch?v=_TRV6fPUMJw&feature=youtu.be)

该内容为 YouTube 平台页脚导航链接，概述了网站的功能、政策与法律信息。

- 📄 关于平台的基本信息与介绍
- 📰 新闻发布与媒体相关资源
- ©️ 版权声明与知识产权保护
- 📧 联系渠道与用户沟通方式
- 🧑‍🎨 创作者相关资源与支持
- 📢 广告合作与商业推广
- 👨‍💻 开发者工具与技术支持
- ⚖️ 服务条款与使用协议
- 🔒 隐私政策与数据保护
- 🛡️ 平台安全与内容政策
- ⚙️ 产品功能与运作机制
- 🆕 新功能测试与更新动态
- 🏢 公司信息与版权年份声明

---

### [React 通过 Activity 组件改变流媒体应用的游戏规则 | Mux](https://www.mux.com/blog/react-is-changing-the-game-for-streaming-apps-with-the-activity-component)

**原文标题**: [React is changing the game for streaming apps with the Activity component | Mux](https://www.mux.com/blog/react-is-changing-the-game-for-streaming-apps-with-the-activity-component)

视频流应用界面复杂，包含播放器、聊天、笔记等多个视图。传统导航方式因组件卸载导致状态丢失，影响用户体验。React 19.2 的 `<Activity>` 组件通过保持组件挂载并切换可见性，解决了状态保存问题。

- 🎬 **条件渲染导致状态丢失**：传统方式隐藏组件时会卸载并重置播放进度
- 🚀 **Activity 组件基础用法**：通过 `mode` 属性控制组件可见性，保持组件挂载状态
- ⚠️ **Activity 的播放控制缺陷**：组件隐藏时视频仍在后台播放，需额外处理
- ✅ **完整解决方案**：结合 `useLayoutEffect` 实现隐藏时自动暂停，完美保存播放状态
- 🔗 **引用传递关键性**：必须正确转发引用才能控制底层视频元素
- 📊 **三种方案对比**：从完全卸载到智能暂停，逐步优化用户体验
- 🎯 **应用场景扩展**：适用于表单、数据表格、画图应用等多种需要状态保存的场景
- 📋 **实施清单**：升级 React 版本、包装组件、转发引用、添加暂停逻辑
- 💡 **开发启示**：Activity 组件为复杂界面状态管理提供了优雅解决方案

---

### [RSC 渲染错误](https://twofoldframework.com/blog/error-rendering-with-rsc)

**原文标题**: [Error rendering with RSC](https://twofoldframework.com/blog/error-rendering-with-rsc)

本文探讨了 React Server Components（RSC）在渲染过程中抛出错误时的处理机制，分析了错误在 RSC、SSR 和浏览器三种渲染环境中的不同表现及应对策略。

- 🚨 **RSC 环境中的错误处理**：错误被序列化为数据嵌入 RSC 流中，不会导致渲染崩溃，而是作为流的一部分传递。
- 🌐 **SSR 环境中的错误影响**：若错误发生在 Suspense 边界外，SSR 会崩溃；边界内则暂停渲染并保留 fallback 状态。
- 🖥️ **浏览器环境的最佳容错**：唯一支持 Error Boundaries 的环境，可捕获错误并显示友好提示，是处理错误的理想场所。
- 🔄 **Suspense 对错误处理的改变**：在流式渲染中，错误延迟触发时，SSR 会先输出部分 HTML，错误后转为客户端渲染。
- 🛠️ **错误传递的核心策略**：应尽快将错误传递至浏览器环境，以便利用 React 的 Error Boundaries 向用户展示有效信息。

---

### [脉搏：Cloudflare 重写 Next.js，AI 重塑商业开源格局](https://newsletter.pragmaticengineer.com/p/the-pulse-cloudflare-rewrites-nextjs)

**原文标题**: [The Pulse: Cloudflare rewrites Next.js as AI rewrites commercial open source](https://newsletter.pragmaticengineer.com/p/the-pulse-cloudflare-rewrites-nextjs)

Cloudflare 工程师利用 AI 代理在一周内重写了 Vercel 的 Next.js 框架，推出基于 Vite 的替代方案 vinext，成本仅 1100 美元。这一事件揭示了 AI 如何颠覆商业开源项目的护城河和商业模式，引发对代码可维护性、测试套件私有化及开源项目防御策略的广泛讨论。

- 🚀 **AI 实现高效重写**：Cloudflare 单名工程师借助 AI 代理在一周内完成 Next.js 核心功能重写，成本极低，效率提升约 100 倍。
- 🔧 **技术实现**：将 Next.js 原有的 Turbopack 构建工具替换为 Vite，使应用能标准化部署至 Cloudflare，但当前版本仍处于实验阶段。
- ⚠️ **质量与安全争议**：Vercel 指出 vinext 存在安全漏洞且未经过大规模测试，质疑其生产环境可靠性。
- 🛡️ **商业开源面临挑战**：AI 使“搭便车”行为更容易，竞争对手可快速复制开源项目，削弱原项目的商业优势。
- 🧪 **测试套件成为关键**：全面的测试套件助力 AI 高效重写，部分项目考虑将测试私有化以增加复制难度。
- 🌍 **行业影响**：AI 可能推动更多非商业开源项目的繁荣，同时加速技术竞争，促使企业聚焦支持、社区和基础设施等新护城河。

---

### [未找到标题](https://x.com/nextjs/status/2019098858236833825)

**原文标题**: [No title found](https://x.com/nextjs/status/2019098858236833825)

该页面提示用户浏览器中 JavaScript 功能未启用或存在兼容性问题，导致无法正常使用 X 平台（原 Twitter），并提供了相应的解决建议。

- 🔧 检测到浏览器已禁用 JavaScript，需启用该功能或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表及相关服务条款
- 🛡️ 部分隐私扩展可能导致加载异常，建议暂时禁用后重试
- 🔄 页面提供“重试”功能供用户手动刷新尝试
- 📜 页脚包含平台服务条款、隐私政策及版权声明等法律信息

---

### [React 峰会——全球最大的 React 开发者大会](https://reactsummit.com/?utm_source=partners&utm_medium=nextjsweekly)

**原文标题**: [React Summit – The Biggest React Conference Worldwide](https://reactsummit.com/?utm_source=partners&utm_medium=nextjsweekly)

React Summit 是全球最大的 React 年度会议，聚焦 React 生态系统与现代 Web 开发，汇集全球前端与全栈工程师，提供线下阿姆斯特丹参与及线上远程互动体验。

- 🗓️ **时间与地点**：2026 年 6 月 12 日与 16 日于荷兰阿姆斯特丹举行，包含会前工作坊与社区活动。
- 🎤 **演讲阵容**：60 多位 React 专家分享最新见解，涵盖全栈开发、AI 辅助编程、技术成长等深度专题。
- 🌍 **参与规模**：吸引全球超过 10,000 名开发者，其中 1,500 名可线下相聚。
- 🎟️ **票务选项**：提供线下混合票、远程票及包含 JSNation 会议的联票，支持团队优惠与分期付款。
- 🛠️ **工作坊与培训**：设有免费与付费工作坊，主题包括 React Server Components、React Query、DevOps 等。
- 🏆 **社区贡献**：设立 JS 开源奖项，并为技术领域 underrepresented 群体提供 100 个奖学金名额。
- 🎉 **社交活动**：包含阿姆斯特丹城市游览、船上派对、美食节及全球最大的 React 社交聚会。
- 📺 **远程体验**：提供高清直播、演讲者问答、讨论室及会后录像，确保线上参与者充分互动。
- 🤝 **合作伙伴与赞助**：得到多家科技公司支持，包括 FocusReactive 等 Next.js 与 Headless CMS 专家机构。

---

### [更好的认证 1.5](https://better-auth.com/blog/1-5)

**原文标题**: [Better Auth 1.5](https://better-auth.com/blog/1-5)

Better Auth 1.5 版本发布，这是迄今为止最大的更新，包含超过 600 次提交、70 项新功能、200 个错误修复和 7 个全新软件包。此次更新引入了新的独立 CLI、MCP 远程认证客户端、OAuth 2.1 提供程序、Electron 桌面应用集成、国际化支持、适配器提取、动态基础 URL、Cloudflare D1 数据库支持、CLI 初始化向导、基于席位的计费、SAML 单点登出、测试工具、密钥轮换等。同时宣布了新的基础设施产品，提供完整的用户管理和分析仪表板、安全工具、审计日志及自助式 SSO 界面。SSO 插件现已为生产环境做好准备，并配备了自助服务仪表板。此外，还包括多项安全改进、性能优化和开发者体验提升。

- 🚀 **全新独立 CLI**：引入 `npx auth` 命令，替代旧版 CLI 包，支持通过 `npx auth init` 交互式搭建完整项目。
- 🔐 **MCP 远程认证客户端**：提供框架无关的远程认证客户端，支持在独立 MCP 服务器上验证令牌和保护资源。
- 🔑 **OAuth 2.1 提供程序**：新增插件可将 Better Auth 实例转换为完整的 OAuth 2.1 授权服务器，支持 OIDC 兼容性。
- 🖥️ **Electron 集成**：为 Electron 桌面应用提供完整的 OAuth 流程支持，包括系统浏览器打开和回调处理。
- 🌐 **国际化支持**：新增 i18n 插件，提供类型安全的错误消息翻译和自动区域检测。
- 🛠️ **适配器提取**：数据库适配器已提取到独立包中，减少捆绑包大小并支持独立版本管理。
- 🔗 **动态基础 URL**：支持根据传入请求动态解析基础 URL，便于 Vercel 预览部署和多域名设置。
- ☁️ **Cloudflare D1 支持**：原生支持 Cloudflare D1 作为一等数据库选项，无需自定义适配器设置。
- 🧪 **测试工具插件**：新增 `testUtils` 插件，提供工厂函数、数据库助手和认证工具，便于集成和 E2E 测试。
- 🔄 **非破坏性密钥轮换**：支持轮换 `BETTER_AUTH_SECRET` 而不使现有会话、令牌或加密数据失效。
- 💺 **基于席位的计费**：Stripe 插件新增支持按席位计费，成员变更自动同步席位数量。
- 🚪 **SAML 单点登出**：SSO 插件新增完整支持 SP 发起和 IdP 发起的 SAML 单点登出。
- 📊 **自助式 SSO 仪表板**：作为新基础设施产品的一部分，SSO 插件现配备自助服务仪表板，便于企业客户自行配置 SAML 身份提供程序。
- 🐛 **大量错误修复与改进**：包括超过 220 个错误修复，涵盖 Drizzle 适配器、Cookie 处理、数据库钩子、事务死锁预防、OAuth、组织管理等方面。

---

### [React 医生](https://www.react.doctor/)

**原文标题**: [React Doctor](https://www.react.doctor/)

本文介绍了人工智能（AI）在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发、个性化治疗和医疗管理等方面的具体实践，并分析了面临的挑战与未来发展趋势。

- 🩺 AI 在医学影像分析中表现突出，能辅助医生更准确地识别肿瘤、病变等，提升诊断效率与精度。
- 💊 通过机器学习加速药物筛选与化合物设计，大幅缩短新药研发周期，降低研发成本。
- 🧬 基于患者基因数据和生活习惯，AI 可制定个性化治疗方案，推动精准医疗发展。
- 📊 智能系统优化医院资源调度、病历管理及患者随访，提升医疗运营效率。
- ⚠️ 数据隐私、算法偏见及法规缺失仍是 AI 医疗落地的主要挑战，需跨领域协作解决。
- 🔮 未来 AI 将与物联网、机器人技术深度融合，实现更智能、普惠的医疗服务体系。

---

### [GitHub - kasin-it/next-md-negotiate: Next.js 内容协商 —— 同一 URL 下为 LLM 提供 Markdown，为浏览器提供 HTML。 · GitHub](https://github.com/kasin-it/next-md-negotiate)

**原文标题**: [GitHub - kasin-it/next-md-negotiate: Content negotiation for Next.js — serve Markdown to LLMs and HTML to browsers from the same URL. · GitHub](https://github.com/kasin-it/next-md-negotiate)

next-md-negotiate 是一个 Next.js 内容协商库，允许从同一 URL 为浏览器提供 HTML，为 LLM 和爬虫提供 Markdown，无需创建重复路由或端点。

- 🚀 **解决内容协商问题**：通过 HTTP `Accept` 头自动区分请求，浏览器获取 HTML，LLM 获取 Markdown。
- ⚙️ **快速集成**：支持 App Router 和 Pages Router，提供 CLI 工具自动初始化配置和路由重写。
- 🔗 **统一路由管理**：基于配置文件定义 Markdown 版本，避免路由重复和维护不一致。
- 🤖 **LLM 可发现性**：提供 `LlmHint` 组件，引导 LLM 代理通过 `Accept: text/markdown` 请求 Markdown 版本。
- 🛠️ **灵活部署选项**：支持通过 `next.config` 重写或中间件/代理层实现内容协商，适应不同项目需求。
- 📦 **类型安全与自动化**：提供类型安全的参数推断和 CLI 命令，简化提示添加、移除和项目脚手架搭建。

---

### [GitHub - icoretech/airbroke: 🔥 轻量级、兼容 Airbrake/Sentry、基于 PostgreSQL 的开源错误捕获器 · GitHub](https://github.com/icoretech/airbroke)

**原文标题**: [GitHub - icoretech/airbroke: 🔥 Lightweight, Airbrake/Sentry-compatible, PostgreSQL-based Open Source Error Catcher · GitHub](https://github.com/icoretech/airbroke)

Airbroke 是一款轻量级、开源的错误捕获工具，兼容 Airbrake 和 Sentry，基于 PostgreSQL 构建，提供现代化的错误管理界面和多种部署选项。

- 💾 **基于 PostgreSQL** – 使用 PostgreSQL 15+ 数据库进行数据存储，保持较小的数据库占用。
- 🌐 **兼容多种错误收集端点** – 支持 Airbrake 和 Sentry 的 HTTP 收集器端点，便于集成现有工具。
- 💻 **现代化前端界面** – 采用 React 和 Next.js 构建，提供直观的错误管理和分析界面。
- 🚀 **部署灵活** – 支持从源码构建、Docker 镜像、Helm Chart 以及多种云平台（Vercel、Render、Railway 等）。
- 🔧 **高性能数据收集** – 数据收集 API 直接处理请求，无需队列系统，在高流量下仍保持良好性能。
- 🤖 **AI 集成支持** – 提供 MCP API，支持 LLM/代理集成，便于错误分类和查询。
- 🔑 **多认证提供商** – 支持 GitHub、Google、Okta 等多种 OAuth 提供商进行用户认证。
- 📊 **错误分组与图表** – 自动根据错误类型和消息进行分组，提供发生次数图表，帮助快速定位问题。
- 🔌 **连接池优化建议** – 推荐使用 PgBouncer 优化数据库连接，并提供连接数计算公式。
- 📋 **错误收集最佳实践** – 建议使用通用错误消息并结合参数字段提供详细信息，避免因动态内容导致错误分组失效。

---

### [终端用户的下一个对象存储界面 | Tigris 对象存储](https://www.tigrisdata.com/blog/tigris-cli/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-03-06)

**原文标题**: [A terminal user's next interface to object storage | Tigris Object Storage](https://www.tigrisdata.com/blog/tigris-cli/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-03-06)

Tigris 推出全新的命令行界面（CLI），专为终端用户设计，让开发者能够直接从 shell 管理对象存储，遵循 UNIX 哲学，提供直观且易于使用的命令。

- 🚀 **全新 Tigris CLI 发布**：专为终端用户设计，可通过 `npm install -g @tigrisdata/cli` 安装，支持跨平台（包括 Windows），提供类似 AWS S3 但更简洁的命令。
- 🔄 **遵循 UNIX 哲学**：每个子命令（如 `tigris login`、`tigris buckets list`）都尽可能简单，支持通过链式组合实现复杂功能，模式为 `tigris DOMAIN OPERATION <ARGUMENT>`。
- 📄 **规范驱动开发**：使用 `specs.yaml` 文件定义 CLI 规范，并自动生成代码框架，确保设计与实现一致，便于迭代和反馈。
- 📊 **命令对比示例**：提供与 AWS S3 命令的对比表，显示 Tigris 命令更简洁直观（如 `tigris cp` 替代 `aws s3 cp`），支持 `t3://` URL 方案。
- ❓ **常见问题解答**：CLI 免费开源，支持 Windows/macOS/Linux，兼容 S3 API，易于 AI 助手使用，通过 `tigris login` 或 `tigris configure` 认证。
- 🌟 **核心功能 `tigris cp`**：支持复制文件到/从 Tigris 存储，包括递归复制和通配符操作，行为与本地 `cp` 命令一致，简化对象存储管理。

---

### [Drizzle 加入 PlanetScale —— PlanetScale](https://planetscale.com/blog/drizzle-joins-planetscale)

**原文标题**: [Drizzle joins PlanetScale â PlanetScale](https://planetscale.com/blog/drizzle-joins-planetscale)

PlanetScale 宣布 Drizzle 团队加入，共同致力于提升 JavaScript 和 TypeScript 的数据库工具性能与开发者体验，同时保持 Drizzle 作为独立开源项目的地位。

- 🚀 Drizzle 团队加入 PlanetScale，专注于优化 JavaScript 和 TypeScript 的数据库工具性能与开发者体验
- 🔧 Drizzle ORM 因卓越性能和开发者体验成为默认选择，与 PlanetScale 理念高度契合
- 🌐 Drizzle 将保持独立开源项目身份，拥有自主路线图和目标
- 💪 PlanetScale 将支持 Drizzle 团队专注于核心工作，推动项目发展
- 🙏 PlanetScale 感谢 Drizzle 团队对社区的贡献，欢迎成为同事

---

### [TypeScript 的未来 - YouTube](https://www.youtube.com/watch?v=wvt5JNUXXLM)

**原文标题**: [The Future of TypeScript - YouTube](https://www.youtube.com/watch?v=wvt5JNUXXLM)

该页面为 YouTube 平台的官方信息与政策说明区域，涵盖平台介绍、联系渠道、用户协议及功能动态等内容。

- 📄 关于平台的基本介绍与背景信息
- 📢 媒体与新闻发布相关资源
- ©️ 版权政策与保护机制说明
- 📞 用户联系与反馈渠道
- 👥 内容创作者专属信息
- 💼 广告合作与商业推广服务
- 🔧 开发者工具与资源支持
- 📜 平台使用条款与协议
- 🔒 隐私政策与数据保护措施
- ⚖️ 平台政策与安全规范
- 🔄 YouTube 功能运作机制说明
- 🆕 新功能测试与更新动态
- ™️ 谷歌公司版权标识（至 2026 年）

---

### [Radix UI → Base UI（3 分钟内）- YouTube](https://www.youtube.com/watch?v=9_Bf6atmX3g)

**原文标题**: [Radix UI → Base UI (in 3min) - YouTube](https://www.youtube.com/watch?v=9_Bf6atmX3g)

该页面为 YouTube 平台的官方信息与政策说明区域，涵盖服务条款、功能指南及法律声明等内容。

- 📄 关于平台的基本信息与介绍
- 📢 新闻发布与媒体相关资源
- ©️ 版权政策与保护说明
- 📞 用户联系与反馈渠道
- 🛠️ 创作者工具与资源支持
- 📈 广告合作与商业化选项
- 💻 开发者接口与技术文档
- ⚖️ 服务条款与使用协议
- 🔒 隐私保护与数据政策
- 🛡️ 平台安全与内容规范
- 🔄 功能测试与更新动态
- ⏳ 版权年份与公司标识

---

### [Vercel Queues 现已进入公开测试阶段 - Vercel](https://vercel.com/changelog/vercel-queues-now-in-public-beta)

**原文标题**: [Vercel Queues now in public beta - Vercel](https://vercel.com/changelog/vercel-queues-now-in-public-beta)

Vercel Queues 现已进入公开测试阶段，它是一个基于 Fluid compute 构建的持久事件流系统，旨在为函数提供可靠的后台任务处理能力，确保任务在函数崩溃或部署更新时仍能完成。该系统支持异步消息处理，具备自动重试和至少一次投递保证，并可与 Workflow 结合使用以实现多步骤编排。

- 🚀 Vercel Queues 进入公开测试，为所有团队提供基于 Fluid compute 的持久事件流处理
- ⚙️ 通过队列实现异步消息处理，支持自动重试和至少一次投递语义，确保任务可靠性
- 📨 可从任何路由处理器发布消息，并通过消费者组独立处理，支持消息重投直至成功或过期
- 🔧 消费者通过 `handleCallback` 创建，配置触发器后路由变为私有，仅队列基础设施可调用
- 💰 按 API 操作次数计费，起价为每百万次 60 美元，包含多可用区同步复制、延迟投递等功能
- 📚 提供详细文档，帮助开发者快速上手并集成队列到现有项目中

---

