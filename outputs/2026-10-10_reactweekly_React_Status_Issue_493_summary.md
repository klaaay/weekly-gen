### [](https://julesblom.com/writing/react-visual-notation)

**原文标题**: [A visual notation for React's parent and owner trees | JulesBlom.com](https://julesblom.com/writing/react-visual-notation)

本文介绍一种面向 React 的父级树与所有者树的可视化表示法，通过将组件呈现为图表，帮助开发者获得仅凭代码难以看清的结构性概览。

- ✍️ 作者：Jules Blom
- ⚛️ 核心主题：React 父级树与所有者树的可视化表示法
- 🗺️ 提出内容：用可视化记法把 React 组件展示为图表
- 🧭 主要目的：提供更清晰的结构性概览
- 💡 关键价值：弥补仅靠代码无法呈现的组件层级与关系信息
- 📅 发布日期：8-10-2026
- 📚 相关栏目：Writing、Notebooks、Libraries

---

### [调查和表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=react_status&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=react_status&utm_medium=email)

SurveyJS 是一套可自托管、面向企业的 JavaScript 客户端表单与调查管理方案，覆盖创建、渲染、收集、分析和 PDF 导出，让开发者在自有应用与基础设施中实现完整数据所有权、安全合规与深度定制。

- 🧩 核心组件包括 Form Library、Survey Creator、Dashboard 和 PDF Generator，覆盖表单渲染、拖拽创建、数据可视化和 PDF 导出。
- 🆓 Form Library 是 MIT 许可的 UI 组件，解析 SurveyJS 表单 JSON 并即时渲染动态交互表单，支持验证和条件逻辑，用于收集响应并发送到自有数据库。
- 🛠️ Survey Creator 是白标拖拽式表单构建器，自动生成描述结构、布局、样式和行为的 JSON schema，可全定制并支持逻辑、默认值、计算。
- 📊 Dashboard 读取 JSON schema 识别数据类型，用交互式图表和表格展示结果；Table View 支持客户端/服务器分页和过滤。
- 📄 PDF Generator 根据表单 JSON 渲染 PDF，可用已收集响应填充，导出可编辑或预填 PDF。
- 🔗 仅专注前端，提供 React、Angular、Vue3 和 vanilla JS 的 npm 包；不存储或追踪数据，也不提供后端、存储或用户管理，需自行连接/搭建服务器和数据库。
- ⚙️ 可连接任意后端技术栈，如 REST API，并提供 ASP.NET Core、Node.js、PHP、Python、WordPress、PostgreSQL、MongoDB 等集成示例。
- 🧱 JSON Schema 驱动表单，可由后端按用户角色、流程状态或外部数据程序化生成/修改，实现动态、版本化、数据驱动的表单工作流。
- 🔐 数据所有权和合规由设计保障：用户决定存储、加密和访问，SurveyJS 不将数据发送到外部服务，有助于满足 GDPR、HIPAA 等要求。
- 🎨 可完全定制界面、本地化、配置/隐藏设置，并扩展自定义问题类型、验证规则和操作，打造原生般体验。
- 🏢 适用行业包括保险、医疗、市场研究、教育、HR、电商、客户体验、非营利和银行。
- ♾️ 无使用限制：不限制管理员、受访者、表单数量、月提交量、文件上传或所用功能，数据存储在自有数据库。
- 💳 开发者许可证为一次性购买，含首 12 个月维护和支持；续费可延长 12–24 个月，且仅限同一套餐持证人。
- 🧑💻 许可证可分配给内部或外包开发者；开发者可访问许可密钥和 Help Desk，但不能查看账单、续费或管理团队。
- 📚 提供产品文档、现场演示、后端集成示例、FAQ、All-in-One Demo 和多种定价计划，便于试用和落地。

---

### [Next.js 16.4 | Next.js](https://nextjs.org/blog/next-16-4)

**原文标题**: [Next.js 16.4 | Next.js](https://nextjs.org/blog/next-16-4)

Next.js 16.4 发布，核心是全面推荐 Cache Components 新编程模型：以 `'use cache'` 实现显式、可组合的组件级缓存，支持静态与动态内容混合渲染；新项目默认启用，Next.js 17 将成默认，现有应用可用代理工具迁移。同时带来 `ensureStatic`、`navigation`/`prefetch` 控制、代理升级与反馈机制、Turbopack 多项优化、React 19.3 及实验特性。

- 🧩 Cache Components 让缓存变成声明式、可组合，可混合客户端缓存、服务端缓存和请求时渲染，替代旧版 App Router 的隐式缓存行为。
- ⚙️ 在 `next.config.ts` 中启用 `cacheComponents: true` 和 `partialPrefetching: true`；`create-next-app` 新项目默认开启。
- 🔮 Next.js 17 将把 Cache Components 设为默认，16.4 起推荐所有 Next.js 应用采用。
- 🤖 `next upgrade --agent` 为代理提供版本化升级指导，Skills 可协助迁移到 Cache Components 和 Partial Prefetching。
- 🛡️ `ensureStatic` 可保证路由的 shell、prefetch 或完整导航为静态，支持 `navigation`、`prefetch`、`shell`，可设置在页面或布局。
- ⏳ `navigation()` 和 `prefetch()` API 能把缓存内容排除在预取或 shell 外，延迟到实际导航时再渲染。
- 🧑💻 实验性 `agentUpgrade` 会在 `next dev` 或 `next build` 时提醒升级；策略包括 `security`、`latest`、`false`。
- 🗣️ 实验性 `agentFeedback` 让编码代理生成问题报告草稿，用户审核后才发送；需启用遥测且不在 CI 运行。
- 💾 Turbopack 磁盘缓存减少 20–25% 空间，数据使用 Zstandard 压缩，元数据保留 LZ4，并改进压缩清理。
- ⚡ Lazy server HMR 只在请求需要时编译和应用服务端更新；共享 Turbopack 运行时减少下载并提高缓存命中。
- 📦 生产包更小：Turbopack 缩短 CSS Module 类名，并使用 export mangling 缩短内部 JavaScript 导出名。
- ⚛️ 内置 React 19.3，带来稳定的 View Transitions、Fragment Refs、`browser()` API 等。
- 🦀 实验性 Rust React Compiler 可跳过无需优化文件，减少重复优化；内存使用降低 30%，编译时间降低 15%。
- 🧹 实验性 `turbopackGc` 可清理内存和磁盘缓存中不再需要的编译工作。
- 🦥 `turbopackLazyDynamicImports` 让客户端动态导入仅在浏览器请求时编译。
- 🧵 `turbopackPluginRuntimeStrategy: 'workerThreads'` 让 Babel、PostCSS、webpack loaders 在单进程 worker 线程中运行，降低内存与 CPU。
- 🔗 支持额外根目录，并可与 pnpm、Bun、Nub、aube 的全局虚拟存储手动集成。
- 📊 Turbopack Bundle Analyzer 新增路由摘要、表视图、快照/差异、关键路径过滤，并提供 `next-bundle-optimizer` 代理技能。
- 💬 可通过 GitHub Discussions、GitHub Issues、Discord 反馈；版本由 Next.js、Turbopack 团队及社区贡献者共同完成。

---

### [入门：缓存 | Next.js](https://nextjs.org/docs/app/getting-started/caching)

**原文标题**: [Getting Started: Caching | Next.js](https://nextjs.org/docs/app/getting-started/caching)

Next.js 缓存机制文档概述，介绍通过 Cache Components 实现数据与 UI 缓存的完整方案，涵盖 `use cache` 指令、Suspense 边界、运行时 API 处理、部分预渲染（PPR）、预取优化及缓存存储策略。

- 🚀 **启用方式**：在 `next.config.ts` 中设置 `cacheComponents: true` 和 `partialPrefetching: true`；新建 App Router 项目默认已启用
- 📦 **`use cache` 指令**：可作用于数据层（缓存函数）或 UI 层（缓存组件/页面），推荐搭配 `cacheLife` 设置生命周期
- 🔑 **缓存键机制**：函数参数及父作用域捕获的值自动成为缓存键的一部分，不同输入产生独立缓存条目
- ⏳ **流式未缓存数据**：需用 `<Suspense>` 包裹并提供 fallback UI，fallback 会进入静态 shell，异步内容在请求时流式传输
- 🔐 **运行时 API**：`cookies`、`headers`、`searchParams`、`params` 必须用 `<Suspense>` 包裹，否则开发环境会提示 `blocking-route`
- 🗝️ **`use cache: private`**：为直接读取运行时 API 的函数赋予缓存生命周期，可被预取包含
- 🎯 **参数传递模式**：可从运行时 API 提取值作为 props 传给缓存函数，值会进入缓存键
- 🎲 **随机值与时间戳**：`Math.random()`、`Date.now()`、`crypto.randomUUID()` 需显式处理——用 `connection()` + `<Suspense>` 每次请求生成，或用 `use cache` 缓存共享
- ✅ **可预测值自动预渲染**：模块导入、`fs.readFileSync`、纯计算在构建时完成并进入静态 HTML
- 🏗️ **部分预渲染（PPR）**：Cache Components 的默认行为，生成包含初始 HTML 和 RSC Payload 的静态 shell，可从 CDN 直接提供服务
- 📐 **最大化静态 shell**：将异步工作尽量下移到组件树深处，避免在 layout 顶层 await params，让更多内容进入静态 shell
- ⚡ **即时导航**：Cache Components 会验证客户端导航，引导你通过缓存或 Suspense 使导航变得即时
- 🔄 **预取机制**：默认预取 App Shell；设置 `<Link prefetch={true}>` 可额外预取依赖 URL 数据的缓存内容（每次服务器调用）
- 💾 **缓存内容存储**：预渲染 HTML（磁盘/CDN）、共享存储（`use cache: remote`）、浏览器（`use cache: private`），所有存储仅限单次部署
- 🔁 **增量静态再生（ISR）**：`generateStaticParams` 预渲染已知 URL，未知 URL 先返回 App Shell 再后台升级
- 🤖 **机器人处理**：不识别动态元数据的爬虫会被检测并强制动态渲染，需确保构建时数据源在请求时也可用

---

### [Next.js 16.4 | Next.js](https://nextjs.org/blog/next-16-4#new-agent-features)

**原文标题**: [Next.js 16.4 | Next.js](https://nextjs.org/blog/next-16-4#new-agent-features)

Next.js 16.4 于 2026 年 10 月 6 日发布，核心是推荐并默认启用 Cache Components，作为面向 App Router 的新编程模型；同时带来代理升级/反馈工具、Turbopack 优化、React 19.3 及多项实验特性。

- 🚀 Cache Components 将在 Next.js 17 默认启用，新 create-next-app 项目也已默认开启。
- 🧩 通过 'use cache' 在组件级声明缓存，像 Cache-Control 一样组合客户端、服务端和请求时渲染。
- ⚡ 目标是实现个性化页面快速首屏、服务端渲染应用即时客户端导航，以及 opt-in、声明式、可组合的缓存。
- 🛠️ 现有应用可用 next upgrade --agent 与专用 Skills 迁移到 Cache Components。
- 🛡️ 新增 ensureStatic，可要求路由 shell、prefetch 或完整导航静态化，避免意外动态渲染。
- 📬 新增 navigation() 和 prefetch() API，可从预取/壳层排除缓存内容，推迟到真实导航或显式预取时加载。
- 🤖 next upgrade --agent 让代理自动升级、应用迁移指南/codemod 并验证应用。
- 🔔 experimental.agentUpgrade 在 next dev/build 时提醒升级，策略为 security、latest 或 false。
- 📝 experimental.agentFeedback 让代理生成问题报告草稿，用户审核后发送；默认不发送源码/日志/密钥，需遥测且 CI 不运行。
- 💾 Turbopack 磁盘缓存减少 20–25%，数据用 Zstandard 压缩、元数据用 LZ4，并改进压缩清理。
- ⏱️ 懒服务端 HMR、共享运行时单 chunk、更小生产包与更短 CSS Module 类名/export mangling。
- ⚛️ 内置 React 19.3，包含稳定 View Transitions、Fragment Refs、browser() API 等。
- 🦀 实验性 Rust React Compiler：跳过无需优化文件，内存使用降 30%、编译时间降 15%。
- 🧹 实验性 turbopackGc 清理内存/磁盘缓存中无用编译产物和旧会话/已删路由数据。
- 🐢 实验性 turbopackLazyDynamicImports 按浏览器请求延迟编译客户端动态导入。
- 🧵 实验性 worker threads 让 Babel、PostCSS、webpack loaders 在单进程运行，降低开销。
- 🔗 支持 additional roots 及 pnpm、Bun、Nub、aube 全局虚拟存储，便于链接本地包。
- 📊 Turbopack Bundle Analyzer 新增路由概览、表格视图、快照/diff、关键路径过滤，并提供 next-bundle-optimizer 技能。
- 🙌 可用 npx next@canary upgrade --agent=latest 或 npm install next@latest 升级，并通过 GitHub/Discord 反馈。

---

### [Next.js 16.4 | Next.js](https://nextjs.org/blog/next-16-4#improvements-for-all-apps)

**原文标题**: [Next.js 16.4 | Next.js](https://nextjs.org/blog/next-16-4#improvements-for-all-apps)

Next.js 16.4 发布，核心是推荐 Cache Components 作为所有 Next.js 应用的最佳选择；新项目通过 create-next-app 默认启用，并将在 Next.js 17 成为默认。该版本还带来 ensureStatic、navigation/prefetch、代理升级与反馈、Turbopack 优化、React 19.3 及多项实验特性。

- 🚀 Cache Components 是新的编程模型，解决 App Router 的初始加载、个性化页面、即时客户端导航和缓存声明式等问题。
- 🧩 `'use cache'` 像组件级 Cache-Control，可缓存组件 UI，并混合浏览器端缓存、服务器端缓存和请求时渲染。
- 📦 启用需在 `next.config.ts` 设置 `cacheComponents: true` 和 `partialPrefetching: true`；Partial Prefetching 已属于该模型。
- 🔮 Cache Components 将在 Next.js 17 默认；从 16.4 起推荐用于所有应用，create-next-app 新应用默认启用。
- 🛠️ 现有应用可用 `next upgrade --agent` 和专用 Skills 帮助迁移到 Cache Components。
- 🧱 `ensureStatic` 可保证路由 shell、prefetch 或 navigation 静态，支持页面或 layout 配置，动态内容会导致构建失败。
- ⏭️ `navigation()` 可将缓存内容排除出 prefetch，延迟到实际导航；`prefetch()` 可排除路由 shell 中的缓存内容。
- 🤖 `next upgrade --agent=latest` 让代理端到端升级；`experimental.agentUpgrade` 可自动提醒升级，策略为 security、latest 或 false。
- 📝 实验性 agentFeedback 让代理生成问题报告草案，用户审核后发送；需启用 Telemetry，且不在 CI 运行。
- 💾 Turbopack 磁盘缓存占用减少 20–25%，使用 Zstandard 压缩数据、LZ4 保留元数据，并改进清理。
- ⚡ Lazy server HMR 仅在请求需要时编译并应用服务器更新，减少不必要的后台工作。
- 🧵 Turbopack 运行时改为跨路由共享单个 chunk，降低下载量并提高缓存命中率。
- 📉 生产包更小：CSS Module 类名更短，并使用 export mangling 缩短内部导出名。
- ⚛️ 内置 React 19.3，带来稳定 View Transitions、Fragment Refs、`browser()` API 等。
- 🦀 实验性 Rust React Compiler：快速检查跳过无需优化文件，内存使用降低 30%，编译时间降低 15%。
- 🧹 实验性 `turbopackGc` 清理内存和磁盘缓存中未用工作；`turbopackLazyDynamicImports` 延迟编译客户端动态导入。
- 🧰 实验性 worker threads 让工具在单进程运行；additional roots 支持链接包和 pnpm、Bun 等全局虚拟存储。
- 📊 Turbopack Bundle Analyzer 新增路由摘要、表格视图、快照/差异、关键渲染路径过滤，并提供 next-bundle-optimizer agent skill。
- 💬 可通过 GitHub Discussions、GitHub Issues、Discord 反馈，社区与 Next.js/Turbopack 团队共同贡献。

---

### [React 基金会贡献者峰会 2026 · React 基金会](https://www.react.foundation/summit)

**原文标题**: [React Foundation Contributors Summit 2026 · React Foundation](https://www.react.foundation/summit)

React Foundation 将于 2026 年 11 月 10–12 日在伦敦举办邀请制工作峰会，面向各技术工作组成员，目标是首次线下建立身份、协调路线图、建立信任并推进治理。

- 📅 日期：2026 年 11 月 10–12 日；11 月 9 日抵达、11 月 13 日离开。
- 📍 地点：伦敦 Meta King’s Cross，11-21 Canal Reach。
- 🎟️ 参与：仅限 React Foundation 工作组成员受邀参加，也开放自我提名。
- 🚫 性质：这是工作峰会，不是公开会议。
- 🎯 目的：让基金会成员首次面对面连接，并决定下一步方向。
- 🧭 目标：确立身份、塑造路线图、建立信任、正式化治理。
- 🗓️ 日程：周二全体会议；周三和周四为工作组日；周一和周五为旅行日。
- 👥 工作组：包括 React Native 核心运行时与渲染器、平台专家、稳定 API、分发，以及 React Fiber、DevX/开发者工具、Server、Compiler。
- 🔀 重叠成员：跨组重叠是已知排期约束，鼓励合并/拆分会议和跨组协作。
- 💰 差旅住宿：基金会无法赞助所有参与者，期望雇主支持；有需要可直接联系基金会。
- 🍽️ 餐饮：细节将在后勤确认后公布。
- 📝 议程与更新：详细议程待发布；本页是参与者信息来源，最后更新于 2026 年 10 月 2 日。

---

### [](https://docs.google.com/forms/d/e/1FAIpQLSf-ATKZ0np5wFvWEOJlFeNp52BazYF5_fT7ubuvr3C0IHxheQ/viewform?pli=1)

**原文标题**: [React Foundation Summit 2026 - Self-candidation](https://docs.google.com/forms/d/e/1FAIpQLSf-ATKZ0np5wFvWEOJlFeNp52BazYF5_fT7ubuvr3C0IHxheQ/viewform?pli=1)

这是 React Foundation Summit 2026 的自荐/自申请表单，面向 React Foundation 成员及 React/React Native 生态贡献者；活动为邀请制，但贡献者可提交申请，组织方会审核以确保社区代表性。

- 🧾 这是 React Foundation Summit 2026 的自我提名表单，活动仅限受邀的 React Foundation 成员参加。
- 🌐 若你长期为 React/React Native 生态做贡献并希望加入，可提交此自荐表，组织方将审核申请以保障社区代表性。
- 🔐 页面提示需启用 JavaScript；登录 Google 可保存进度，回复副本会发送至填写的电子邮箱。
- 👤 必填信息包括：电子邮件地址、姓名、组织/所属机构、职位/头衔。
- 🧩 需选择最相关的工作组：React Fiber、DevX/开发者工具、React Native、Server、Compiler、React Foundation Board，或其他。
- ✍️ 需说明你对 React 生态的贡献，以及希望参加峰会的原因。
- 📝 还可补充组织者应知的其他信息。
- ⚠️ 表单由 Meta 内部创建，使用 reCAPTCHA，并提醒不要通过 Google 表单提交密码；如觉可疑可报告。

---

### [高级软件工程师，原生移动端，远程 - 美国 - Coinbase | Adam Wolf | 25 条评论](https://www.linkedin.com/posts/adamawolf_senior-software-engineer-native-mobile-activity-7511201803389186048-JV6b)

**原文标题**: [Senior Software Engineer, Native Mobile, Remote - USA - Coinbase | Adam Wolf | 25 comments](https://www.linkedin.com/posts/adamawolf_senior-software-engineer-native-mobile-activity-7511201803389186048-JV6b)

overview summary
- 🚀 Adam Wolf 宣布 Coinbase 消费者交易应用将全面原生化：从 React Native 迁移到 Swift 和 Kotlin 重建。
- 🤖 两大关键动因：AI 编码代理大幅降低“同一功能写两遍”的成本；原生应用没有中间层，产品体验更佳。
- ⚡ 原生优势包括启动更快、崩溃更少、首日接入 iOS 与 Android 新能力，这对数百万用户交易真实资金的应用非常重要。
- 🧭 这也被视为 2026 年重新定义移动工程师角色的机会：少写样板和桥接代码，多关注架构与用户体验，重活交给 AI 代理。
- 📣 该团队正在主导迁移，并招聘 Native Mobile 与 Mobile QA，级别覆盖 Senior 到 Senior Staff，含美国远程岗位。
- 💬 评论区有人建议改用 Kotlin/Compose Multiplatform 或 Flutter，并质疑为何不共享跨平台逻辑。
- 🧩 Justin Mancinelli 表示，当年选 React Native 合理，因为 KMP 尚早、Flutter 社区小；如今原生阻力消失，AI 降低了双代码库成本。
- ❓ Vladislav Baranov 询问是否完全原生，还是保留 Rust/KMP 核心并仅用 SwiftUI/Compose 做 UI。
- 🛡️ Joel Diaz 认为用代理吸收重复开发是 2026 年的好策略，但需快速静态分析、密钥扫描和架构规则来防范代理生成错误代码。
- 📊 有人要求 Coinbase 在迁移过程中公开 UX 与技术性能对比基准。
- 🔄 Shamita Pisal 关注原生发布周期，指出 SDUI 架构曾帮助 React Native 解耦产品迭代与 App Store 发布。
- 🌊 评论还提到 Shopify 等也在“回归原生”浪潮中，多数人看好 Coinbase 应用会因此变得更好。

---

### [](https://x.com/sethwebster/status/2105422444529963495)

**原文标题**: [Seth Webster on X: "FANTASTIC news: the incomparable @barbara_markie is joining the React Foundation as our Director of Community. ❤️

She cares deeply about React, knows this community inside and out, and has an uncanny ability to get the right people together and make things happen.

Couldn’t be … / X](https://x.com/sethwebster/status/2105422444529963495)

Seth Webster 在 X 上宣布，Barbara Markie（Basia）将加入 React Foundation，担任社区总监。他高度赞扬她对 React 的关心、对社区的深入了解，以及促成合作、推动事情发生的能力，并表达欢迎与喜悦。

- 🎉 Seth Webster 宣布 Barbara Markie 加入 React Foundation，担任社区总监。
- ❤️ 他称她“无与伦比”，并说她深切关心 React。
- 🧠 她非常了解 React 社区，擅长把合适的人聚在一起并推动事情发生。
- 🤝 Seth 表示自己无比开心，并欢迎 Basia 加入。
- 📅 该帖发布于 2026 年 9 月 30 日晚上 10:20，获得约 2.8 万次浏览及若干互动。

---

### [](https://jimmyhmiller.com/what-does-the-react-compiler-even-do)

**原文标题**: [Can we Make React Faster using the React Compiler? — Jimmy Miller](https://jimmyhmiller.com/what-does-the-react-compiler-even-do)

文章通过一系列实验探索 React Compiler 如何让 React 更快：它已能自动缓存 JSX 与逻辑，作者又原型化了内联、块 DOM、列表缓存、选择器感知缓存、Context 与外部 store 优化，在 13 个基准上取得显著提速，最高约 51×；但这些都只是概念验证，不代表生产可用或应该被 React 直接采纳。

- 🧠 作者以“先看输出、再深入内部”的方式学习 코드库，本文目标是解释 React Compiler 的行为，并分享自己尝试的优化。
- ⚙️ React Compiler 输出常用 `_c` 缓存槽和 `react.memo_cache_sentinel`，把 JSX 对象和函数缓存起来，首次初始化后直接复用。
- 🪝 编译器能绕过 Hooks 限制：例如在条件分支后做缓存，而手写 `useMemo` 很难做到同样灵活。
- 🔗 编译器基于 SSA 静态单赋值形式，经过多轮 pass 简化语言、推断信息并转换优化，例如把 `props.method_call()` 规范化为先取函数再调用。
- 🚀 答案是“可以”：React Compiler 本身已能让 React 更快，作者还能在此基础上原型化更多优化。
- 🧩 单独内联可能让性能变差：把 `Row` 内联进 `List` 后失去每行缓存，Append 2k 从 444.1ms 变为 1038.1ms。
- 🧱 块 DOM 将静态与动态部分分离，按状态差异更新，使内联优势显现：加法与块结合后 Append 2k 可到 164.2ms。
- 📋 列表 memoization 为每个列表项加缓存，Append 2k 可降到 294.6ms；配合内联、块和列表缓存可到 158.8ms。
- 🎯 选择优化记录前后 `selectedId`，类似 Solid 的 `createSelector`；200 次选择跨 2000 行从约 250ms 降到 5.4ms，约 51×。
- 🌐 Context 优化可只重渲染真正依赖的部分：200 次 typing、2000 条消息从 103.6/80.0ms 降到 11.7ms；但该优化未进入 React，说明基准胜利不等于生产采用。
- 🏬 外部 store/Zustand 优化可把比较移入 selector，减少重渲染；store selectors 让 200 次选择跨 2000 张卡片从 474.6/311.5ms 降到 48.9ms。
- 📊 13 个负载整体显示：全原型相对无编译器最高 51×，Append 16.2×，Todo toggle 14.9×，Rows select 15.9× 等。
- 🔭 仍有许多未探索方向：SSR、服务端到客户端通信、hydration、跨组件优化；生产采用还需验证真实负载、内存与生态影响。

---

### [](https://react-aria.adobe.com/blog/sheet)

**原文标题**: [Scrolling is All You Need: Building a Swipeable Sheet | React Aria](https://react-aria.adobe.com/blog/sheet)

React Aria 发布 Sheet 组件：一个从视口边缘滑入、可滑动关闭的覆盖层，完全基于原生 CSS 滚动吸附与 view timelines 构建，支持手势同步动画、吸附点、堆叠、软键盘适配及多方向摆放。

- 🧩 Sheet 支持手势同步动画、snap points、堆叠、overscroll padding、软件键盘感知，以及多种位置和滑动方向。
- ⚙️ 实现基于原生 CSS scroll snapping 和 view timelines，并构建在既有 Modal 组件上；滑动手势无需 JavaScript 触摸处理，可在主线程外以原生刷新率运行，自带动量滚动与弹性物理。
- 📐 视口设置利用普通 CSS overflow 滚动制造开关错觉：overlay 高度为窗口两倍并隐藏滚动条，stage 为视口大小 flex 容器，顶部和底部吸附点确保 Sheet 完全打开或关闭。
- 🧵 关闭时 scrollTop=0，打开时平滑滚动到 100%；滑动关闭即滚回顶部，IntersectionObserver 检测到完全离屏后卸载 Sheet。
- 🎞️ swipeAnimation 使用与滑动手势同步的 CSS keyframe 动画，可控制背景透明度、Sheet transform 或圆角；view-timeline 跟踪可见比例，view-timeline-inset: 0 100dvh 让动画从 Sheet 可见时开始。
- 📍 snapPoints 支持半开吸附：在 Sheet 内渲染不可见 1px 标记，scroll-margin-top:100dvh 让标记吸附到视口底部；半可见时内部内容禁用滚动，全开后内容可滚动，overscroll-behavior: auto 启用滚动链以便下拉关闭。
- 🚫 preventDismissal 为 true 时不能滑走，但仍可在吸附点间滑动；进入动画后调整 stage，使 scrollTop=0 对齐首个吸附点，避免滑出屏幕并保留原生弹跳。
- 🗂️ 多个 Sheet 可堆叠，stackAnimation 由 view timelines 驱动；在根 html 上通过 timeline-scope 定义，并用 animation-composition: accumulate 叠加前方 Sheet 的时间线效果，表现堆叠深度。
- ⌨️ 软键盘适配通过 padding-bottom: calc(100dvh - var(--visual-viewport-height)) 让用户触达底部内容；改进 usePreventScroll 减少布局偏移，点击输入框时键盘打开并平滑滚动输入框到视图，不滚动整页。
- ✨ 结论：现代 CSS 结合滚动吸附、view timeline 动画、overscroll-behavior 和动态视口单位，可实现原生滑动手势与流畅动画；几年前难以做到。

---

### [](https://react-aria.adobe.com/Sheet)

**原文标题**: [Sheet | React Aria](https://react-aria.adobe.com/Sheet)

Sheet 是一种从视口边缘滑入的可滑动覆盖层，适合移动端弹层、导航抽屉、通知横幅与嵌套流程；支持 React Aria 组件、CSS/Tailwind、主题定制、吸附点、手势动画和堆叠。
- 📱 **定位**：`position` 决定 Sheet 锚定在屏幕哪一边，支持 `bottom`、`top`、`left`、`right`、`start`、`end`、`center`。
- ↔️ **方向与 RTL**：`start`/`end` 会在从右到左语言环境中自动镜像，`left`/`right` 始终表示物理方向。
- 👆 **滑动关闭**：`swipeDirection` 控制可滑动方向，默认与 `position` 一致，也可设为 `vertical`、`horizontal` 等。
- 🧩 **常见用途**：`start`/`end` 适合导航抽屉，`bottom` 适合移动端底部面板，`top` 适合通知横幅。
- 📐 **吸附点**：`snapPoints` 让 Sheet 停在部分打开位置，支持像素、CSS 长度和相对 Sheet 尺寸的百分比；初始打开到第一个吸附点，可拖至全高或下滑关闭。
- 🎞️ **动画**：`swipeAnimation` 可与滑动手势及进入/退出动画同步，`swipeAnimationRange` 指定动画播放的吸附点区间。
- 🗂️ **堆叠**：Sheet 可嵌套以构建多级流程，`stackAnimation` 可在子 Sheet 打开时让父 Sheet 后退缩放。
- ⛔ **关闭控制**：`preventDismissal` 可阻止滑动、Esc 或外部交互关闭；`shouldCloseOnInteractOutside` 可自定义外部交互是否触发关闭。
- 🧱 **组件结构**：主要 API 包括 `SheetTrigger`、`SheetOverlay`、`SheetBackdrop`、`Sheet`、`SheetContent`；`Heading slot="title"`、`Text slot="description"`、`Button slot="close"` 用于内容与关闭操作。
- 🎨 **样式与状态**：提供 `data-position`、`data-swipe-direction`、`data-stack-index`、`data-expanded`、`data-entering`、`data-exiting` 等 CSS 选择器，以及 `--sheet-scroll-padding-y/x`、`--visual-viewport-height/width` 等 CSS 变量处理滚动和键盘遮挡。
- 🛒 **示例覆盖**：文档包含购物车、菜单、地点详情、设置、账户与高级设置等示例，并支持 Vanilla CSS、Tailwind 和主题色选择。

---

### [](https://jjenzz.com/making-react-context-cheap/)

**原文标题**: [Making React Context Cheap with React Compiler :: jjenzz](https://jjenzz.com/making-react-context-cheap/)

React Context 的每次更新都会让所有消费者重新渲染，社区长期想要官方的 `useContextSelector`，但 React 移除了旧的位控制方案且至今未提供该 API。文章用 5000 个 radio 的基准测试说明：React 官方推荐的“外层读 Context + memo 子组件”已能跳过大量无用工作，而 React Compiler 能在组件内部复用 JSX 和中间值，让普通组件也接近 context selector 的细粒度更新效果。因此重点或许不是减少渲染次数，而是让每次渲染足够便宜。

- 🧠 核心痛点：Context 中任意值更新会导致所有 consumer 重渲染，一次选择变化可能让 5000 个 radio 全部重渲染。
- 🚫 历史方案：React 曾支持 `calculateChangedBits` / `unstable_observedBits` 来控制消费者更新，但在 PR #20953 中被移除；2019 年虽有 context selectors RFC，官方仍未落地。
- 📘 官方替代：React 文档建议把组件拆成两层，外层读取需要的 Context，再把值作为 props 传给 memo 化子组件，从而只让相关子组件重渲染。
- 🔌 常见替代：`useSyncExternalStore` 常被用来实现细粒度订阅，但文档更建议优先使用内置 state，它更像桥接外部 store 的工具，且偏离 React 原语可能错过并发渲染等能力。
- 📊 基准结果：在 5000 个 radio 的生产构建测试中，`useSyncExternalStore` store、Context + memoized view、React Compiler 三种方案 p95 点击性能接近；Compiler 版不输甚至略优。
- ⚙️ React Compiler 的作用：它让单个 `Radio` 组件无需额外 view 组件或 selector，也能在 `checked`、`onSelect`、`value` 不变时复用之前的 JSX 和中间计算。
- 🧰 未用 Compiler 时：可以用 `withContextSelector` 这类 `React.memo` 抽象封装选择逻辑，但它是组件工厂，与 React lint 规则有摩擦，未来迁移 Compiler 后应移除。
- 🔍 结论：不要只数 render 次数；用户真正等待的是 render 中执行的工作。与其执着于避免渲染，不如借助 React Compiler 让渲染变得便宜。

---

### [React 文件夹结构最佳实践 [2026] - Robin Wieruch](https://www.robinwieruch.de/react-folder-structure/)

**原文标题**: [React Folder Structure Best Practices [2026] - Robin Wieruch](https://www.robinwieruch.de/react-folder-structure/)

React 文件夹结构没有唯一“正确”答案。Robin Wieruch 结合十多年 React 项目经验，按项目从小到大的演进路径，分享从单文件、多文件、组件文件夹、技术文件夹、功能文件夹，到域、包、应用与 monorepo 的结构思路，并强调边界、复用与按需演进。

- 🧱 起点是单文件：小型项目可从 `src/App` 开始，组件变大后再拆分。
- 📄 多文件拆分：相关组件可拆到多个文件，但只导出公开 API；强耦合子组件可暂留同一文件。
- 🗂️ 组件文件夹：每个组件一个文件夹，放 `index`、`component`、`test`、`style` 等文件，避免 `src/` 根目录膨胀。
- 📦 barrel 文件：`index` 可作为模块公开 API，只暴露必要内容；全量 re-export 会影响 tree shaking。
- 🧪 技术关注点：组件文件夹内可横向扩展 `types`、`hooks`、`stories`、`utils`、`constants` 等。
- 🪆 嵌套限制：组件文件夹嵌套建议不超过两层，避免结构过深。
- 🧰 技术文件夹：中大型项目按技术类型分组，如 `components/`、`hooks/`、`context/`、`utils/`。
- 🔌 复用逻辑上移：可复用 Hook 放 `hooks/`，Context 放 `context/`，通用工具放 `utils/`；仅单组件使用的留在组件内。
- 🧾 常见技术文件夹：`lib/`、`api/`、`stores/`、`config/`、`types/`、`providers/`、`layouts/`、`assets/`、`routes/`、`testing/` 按需采用。
- 🧭 功能文件夹：大型项目把功能组件放 `features/<feature>/`，`components/` 只保留通用 UI 组件。
- 🔤 命名约定：文件夹与组件名多用单数；顶层集合文件夹和 bundle 文件可用复数；现代项目常用 kebab-case 与 `.tsx`。
- 🔗 功能边界：代码单向流动；功能之间不直接互相导入；每个功能通过 `index` 暴露公开 API。
- 🧪 边界测试：想象删除某功能，若大量模块崩溃说明边界泄漏；理想情况只影响组合它的页面。
- 🏢 域文件夹：功能过多时用 `domains/<domain>/features/` 按业务领域分组，域之间不直接依赖。
- 📦 包文件夹：共享代码可抽成 `packages/shared` 等独立包，通过包名导入，获得更强边界与版本管理。
- 🚀 应用文件夹：多应用场景用 monorepo，`apps/` 放可部署应用，`domains/` 放业务逻辑，`packages/` 放共享包。
- 🖥️ 页面驱动：客户端 React 可用 `pages/`；Next.js 用 `app/` 文件路由；页面负责组合功能与通用组件。
- 🧩 功能内部规模：生产级功能可含 `types`、`enums`、`queries`、`actions`、`components`、`relations/` 等，`relations/` 显式表达跨功能耦合。
- ↩️ 提升与降级：一个功能用则留在功能内；两个以上功能用则提升到共享层；反向也适用。
- 💡 核心结论：结构应随项目增长自然演进，没有固定答案，关键是保持一致性、明确边界，并加入团队自己的风格。

---

### [](https://tanstack.com/blog/tanstack-charts-1-0)

**原文标题**: [TanStack Charts 1.0 | TanStack Blog](https://tanstack.com/blog/tanstack-charts-1-0)

TanStack Charts 1.0 已发布，作者 Tanner Linsley 于 2026 年 10 月 5 日宣布，目标是提供“不必随产品增长而被淘汰”的图表方案：用可组合的 marks、scales、axes 和 interactions 构建图表，兼顾类型安全、按需渲染、轻量模块化与长期 API 支持。

- 📊 TanStack Charts 1.0 正式发布，强调图表应能随应用和数据可视化需求持续演进，而不是一开始就选错、后来重写。
- 🧩 核心模型基于 marks：线、点、条都是 mark，scales 负责映射数据，再与坐标轴和交互组合成图表。
- 🔁 可以逐步添加元素，例如在线图上加点、加柱、加高亮、加注释、定制 tooltip，无需寻找或新建一个刚好满足组合的图表类型。
- 🧠 强烈关注类型安全，让数据值、scales、marks 和交互之间的类型信息贯穿始终，也便于 AI 辅助开发。
- 🎨 默认使用 SVG 渲染；Canvas 作为独立导入和独立渲染器，在需要高性能时按需启用。
- 🎞️ 动画与动效不强制内置，但可在需要时无缝集成。
- 📦 支持紧凑 scales 和 D3 scales，可按最小必要模块引入，保持轻量，并有 bundle 预算与测试保障。
- 🛠️ 支持自定义 marks、scales、交互和渲染器，既可复用现成部分，也可深入场景契约实现特殊需求。
- 🚀 1.0 意味着作者准备好支持用户基于该 API 构建：升级不应导致重建、AI 开发受阻或站点构建失败，自定义扩展也应被考虑。
- 🤖 文章邀请用户把真实应用中的图表交给 AI 用 TanStack Charts 重写，尝试复杂或奇怪图表，并反馈不顺手之处。
- 🔗 文末提供浏览图表目录和开始使用 TanStack Charts 的入口。

---

### [图表目录 | TanStack](https://tanstack.com/charts/catalog)

**原文标题**: [Charts Catalog | TanStack](https://tanstack.com/charts/catalog)

shadcn/ui Charts 汇集了 188 个图表示例，按多种图表族别分类，涵盖从基础统计图形到交互式、动效、地理空间等丰富场景，并提供可直接打开查看的示例。

- 📊 共收录 188 个图表示例，覆盖应用、面积、柱状、变化、比较、组成、装饰、分布、金融、地理、层级、交互、区间、折线、矩阵、动效、多变量、网络、部分与整体、性能、饼图、极坐标、雷达、径向、范围、排名、关系、小倍数、空间、调查、主题、时间、提示框、趋势、不确定性等众多类别
- 🧩 提供多类基础图表，如面积图、柱状图、折线图、饼图、雷达图、径向图，并配有多种变体（渐变、堆叠、交互、标签、图例等）
- 📈 包含趋势与时间序列示例，例如苹果股价折线、季节性缺口、移动平均、布林带、指数化失业率等
- 🗂️ 支持分布与不确定性可视化，如直方图、箱线图、小提琴图、蜂群图、误差条、百分位带等
- 🔗 呈现关系与多变量图表，如散点图、气泡图、平行坐标、自相关、回归线等
- 🗺️ 涵盖地理与空间可视化，包括分级统计图、气泡地图、正射投影地球、密度等高线、矢量场、德劳内网络等
- 🕸️ 提供层级与网络图，如树图、矩形树图、旭日图、桑基图、角色网络等
- 🎛️ 强调交互能力，包括工具提示、刷选、缩放平移、联动图表、同步光标、播放擦洗、可编辑区间等
- 🎬 包含动效示例，如交错入场、弹簧更新、跨图表几何变形、焦点与十字准线动效
- 🎨 提供主题与样式定制，如主题调色板矩阵、交互式面积卡片、KPI 迷你图、仪表盘等
- 🧭 支持极坐标与雷达类图表，如饼图、甜甜圈图、玫瑰图、雷达图、同心柱、极线图等
- 🧱 还包含大量 shadcn 官方风格示例，覆盖面积、柱状、折线、饼图、雷达、径向、提示框等组件的多种配置与用法

---

### [发布 v8.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v8.0.0)

**原文标题**: [Release v8.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v8.0.0)

Ink v8.0.0 是一次重大版本更新，包含破坏性变更、新功能与大量渲染/文本/输入/焦点修复，并附迁移指南；核心变化包括要求 React 19.3+、收窄 Box 尺寸与流类型、让 useInput 忽略未识别终端控制序列，同时新增滚动与内容区尺寸测量能力。

- 🚀 v8.0.0 于 10 月 3 日发布，是 Ink 的重大版本，含破坏性变更、新功能、修复与迁移指南。
- ⚛️ 破坏性变更：要求 React 19.3+。
- 📏 破坏性变更：`<Box>` 的 `minWidth` 和 `maxWidth` 只接受数字；百分比字符串从未被文档支持，迁移时可用 `useWindowSize()` 或父级 `useBoxMetrics()` 计算。
- 🔌 破坏性变更：`stdin`、`stdout`、`stderr` 改为通用 Node.js 流类型；`useStdout().stdout` 不再暴露 `columns`/`rows` 等 TTY 属性，需改用 `useWindowSize()`。
- ⌨️ 破坏性变更：`useInput` 不再接收鼠标报告、焦点事件、光标位置报告等未识别终端控制序列；Ink 能识别的按键与 Kitty 协议事件不受影响。
- 🆕 新增：`<Box>` 支持 `contentOffsetX`/`contentOffsetY` 构建滚动视图，可配合 `overflow="hidden"`。
- 📐 新增：`useBoxMetrics()` 与 `measureElement()` 增加 `clientWidth`/`clientHeight`，表示元素排除边框后的内容可用尺寸。
- 🌊 新增：`render()` 的 `stdin`/`stdout`/`stderr` 可接受任意 Node.js 流；仅当 `stdin` 是 TTY 且调用 `setRawMode()` 时使用 raw mode。
- ⚡ 新增与优化：`incrementalRendering` 模式跳过未变动行前缀，减少输出和闪烁；React DevTools 用原生 WebSocket 替代 `ws`；应用小键盘 Enter 识别为 `key.return`。
- 🐛 渲染修复：保留 scrollback、`clear()` 后恢复历史与未变帧、终端行数变化重绘、光标位置保持、增量渲染、溢出裁剪、背景继承、Suspense 可见性、`onRender` 时序等。
- 📝 文本修复：多行文本逐行截断、无空间换行时保持自然宽度、顶部外多行文本消失、剥离控制字符、制表符/CRLF、ANSI 样式跨换行、组合标记、SGR 归一化、宽字符裁剪/覆盖保留样式等。
- ⌨️ 输入修复：传统键盘修饰符、SS3/Kitty 解析与检测、`reportAssociatedText`、Ctrl+C 与普通输入同时到达、Meta 键缓冲区不变异、`onKittyQueryResponse` 稳定、暂停时副作用延迟、`suspendTerminal()` 幂等。
- 🎯 焦点修复：共享 focus ID 视为一个 Tab stop、`disableFocus()` 按文档模糊焦点、自动 focus ID 防冲突、空字符串可作为有效 focus ID。
- 🛠️ 其他修复：屏幕阅读器输出、错误源码摘录、`renderToString()`、`useWindowSize()` 漏掉订阅前 resize、盒模型指标跟踪、`useAnimation()` 暂停值、文本缓存与 `wrapText` 缓存、Yoga 根节点释放、`waitUntilExit()` 监听器等。
- 📘 迁移指南：升级 `react`/`@types/react` 到 19.3+；`minWidth`/`maxWidth` 用数字；流类型改用 `useWindowSize()`；若用 `useInput` 解析未识别控制序列需调整逻辑。

---

### [发布 v2.13.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.13.0)

**原文标题**: [Release v2.13.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.13.0)

Redux Toolkit v2.13.0 已发布，这是一次功能版本，主要更新构建工具链、合并文档站、加入 TypeScript 7 支持，并集中修复 RTK Query、createAsyncThunk、createEntityAdapter、combineSlices 等问题；包布局、exports 与导出 API 保持与 2.12 一致。

- 🚀 v2.13.0 由 markerikson 于 9 月 29 日发布，包含大量跨模块 bugfix。
- 🛠️ 构建工具链现代化：从 Yarn、ESLint、Prettier、TSUp 迁移到 PNPM、Oxlint、Oxfmt、TSDown。
- 📦 新构建使用 TSDown，包布局、exports 和 API 不变；已验证 CJS/ESM 在开发与生产构建中可加载，legacy-esm 仍面向 ES2017。
- 🔐 首个通过 PNPM 工作流与 NPM Trusted Publishing 发布的版本，并为每次提交提供 pkg.pr.new 预览。
- 📚 推出合并文档站 redux.js.org，统一 Redux core、Redux Toolkit、React Redux、Reselect 文档；旧站重定向，RTK 文档位于 /toolkit/。
- 🧹 文档大幅清理去重并更新过时内容，默认展示 RTK 与 hooks 模式。
- 🧩 增加官方 TypeScript 7 支持，修复 TS 7.0/7.1 类型错误并纳入 CI；支持矩阵更新为 TS 5.6+。
- ⚛️ RTK Query 修复 useQueryState/useQuery 选择器未记忆化和渲染期直接读取 store，并修复错误后重取时 isSuccess 误翻转。
- 🔄 RTK Query 还修复 data 反映 updateQueryData 缓存更新、轮询读取当前缓存状态、标签失效竞态、falsy id 标签清理、惰性查询重新订阅、无限查询与 fetchBaseQuery URL 判断等问题。
- ⏳ createAsyncThunk 不再吞掉 pending 前的中止，并正确标记 falsy rejectWithValue；createEntityAdapter、combineSlices、immutability 与动态中间件也有修复。
- 🙌 感谢 markerikson、chatman-media 等 16 位贡献者。

---

### [](https://redux.js.org/toolkit)

**原文标题**: [Redux Toolkit - The official, opinionated, batteries-included toolset for efficient Redux development | Redux](https://redux.js.org/toolkit)

该工具通过简化常见用例、提供默认配置和强大能力，帮助开发者减少样板代码，更专注于核心业务逻辑。

- 🧩 **简单**：内置工具简化常见用例，如 store 设置、创建 reducer、不可变更新逻辑等。
- ⚙️ **有主见**：开箱即用地提供良好的 store 设置默认值，并内置最常用的 Redux 插件。
- 💪 **强大**：借鉴 Immer 和 Autodux，支持“可变式”不可变更新逻辑，甚至自动创建完整的 state“切片”。
- 🚀 **高效**：让开发者专注应用核心逻辑，用更少代码完成更多工作。

---

### [迁移到 v3 | React Native Skia](https://wcandillon.github.io/react-native-skia/docs/getting-started/migration/)

**原文标题**: [Migrating to v3 | React Native Skia](https://wcandillon.github.io/react-native-skia/docs/getting-started/migration/)

React Native Skia v3 迁移指南，重点介绍了从 v2 升级到 v3 的步骤、平台要求变化、API 调整以及新特性。

- 🚀 **全新渲染后端**：v3 在 iOS、macOS 和 Android 上使用 Skia Graphite 渲染，基于 Google 的 WebGPU 实现 Dawn（Apple 平台用 Metal，Android 用 Vulkan）。
- 📌 **v2 仍受维护**：若需支持 Android API 26 以下、无 Vulkan 设备、tvOS、Android TV、Mac Catalyst 或 Expo Go，请继续使用 v2（`yarn add react-native-skia@2`）。
- 📦 **第一步：重命名包**：包名由 `@shopify/react-native-skia` 改为 `react-native-skia`，需更新所有导入语句及 Jest 配置，两个包不可同时安装。
- ⚙️ **第二步：检查平台要求**：Android 需 API 26+ 并将 `minSdkVersion` 设为 26；iOS/macOS 最低部署目标为 iOS 15.1，升级后需重跑 `pod install`；Expo 需使用 development build 而非 Expo Go。
- 🖼️ **第三步：更新 Canvas 属性**：移除 `debug`、`colorSpace`、`androidWarmup` 三个 props 及 `NativeSkiaViewProps` 类型，画布色彩空间自动选择（Apple 宽色域设备为 Display P3，其余为 sRGB）。
- 🧵 **渲染脱离 JS 与 UI 线程**：场景每次 React 提交时记录一次，由专用原生线程池重放为 Graphite 帧，UI 线程只应用动画值。
- 🎨 **纹理可跨线程使用**：Graphite 下 GPU 图像可共享，JS 线程创建的图像可被任意画布或 worklet 运行时绘制。
- 🖥️ **新增 SkiaGraphiteView**：可从任意 JavaScript 运行时逐帧驱动的视图。
- 🔗 **WebGPU 互操作**：与 `react-native-webgpu` 共享同一 GPU 设备，可在 Skia 与 WebGPU 之间零拷贝读写纹理，也兼容 three.js。
- 🌈 **Android 高色深**：`highBitDepth` prop 现已在 Android 上支持 10 位表面渲染。
- 🛠️ **故障排查**：Android 构建失败请确认 minSdkVersion 并清理构建；iOS 构建失败请重跑 pod install；Dawn 版本不匹配需同步升级两个包；截图测试差异属正常，需更新参考图。

---

### [](https://www.youtube.com/watch?v=L-PNQi1nBSA)

**原文标题**: [Hello Graphite - YouTube](https://www.youtube.com/watch?v=L-PNQi1nBSA)

这是 YouTube 页面底部导航与版权信息，主要提供平台介绍、政策条款、合作资源、功能说明及 Google LLC 版权声明等链接入口。

- ℹ️ 基础信息入口包括：关于、新闻、版权、联系我们
- 👥 面向创作者、广告主与开发者的合作及资源链接
- 📜 法律与安全相关链接包括：条款、隐私、政策与安全
- ⚙️ 提供 YouTube 工作原理说明以及新功能测试入口
- ©️ 版权信息显示为 © 2026 Google LLC

---

### [发布 v14.1.0 · callstack/react-native-testing-library · GitHub](https://github.com/callstack/react-native-testing-library/releases/tag/v14.1.0)

**原文标题**: [Release v14.1.0 · callstack/react-native-testing-library · GitHub](https://github.com/callstack/react-native-testing-library/releases/tag/v14.1.0)

Callstack 的 react-native-testing-library 发布 v14.1.0（最新版，2026-10-08），重点增强事件与 UserEvent 能力，支持 React Native 0.88 / React 19.3，并修复多项事件、假定时器问题及更新文档。  
- 🚀 v14.1.0 由 mdjastrzebski 发布，并标记为 Latest  
- ✨ 新增 `fireEvent.layout`，并支持 React Native 0.88（React 19.3）  
- 👆 UserEvent 新增 `accessibilityAction` 和 `pullToRefresh()`  
- ⚠️ 在禁用元素上触发事件时会发出警告  
- 🐛 修复 `fireEvent.layout` 直接事件、`fireEvent` 直接事件冒泡弃用、nightly RN 0.88 等问题  
- ⏱️ 修复 `scroll to event seq` 与 jsdom 下 `setImmediate` 假定时器问题  
- 📚 文档更新：可访问名称说明、贡献者文档、v14.1.0 发布说明  
- 📦 发布页面含 2 个资源；仓库导航显示 Issues 1、Pull requests 7，以及 Discussions、Actions、Wiki、Security and quality、Insights 等入口

---

### [v1.22.0 | React Aria](https://react-aria.adobe.com/releases/v1-22-0)

**原文标题**: [v1.22.0 | React Aria](https://react-aria.adobe.com/releases/v1-22-0)

React Aria v1.22.0 于 2026 年 10 月 8 日发布，核心新增 Sheet 组件，并带来 Turbopack 支持、虚拟键盘覆盖层定位以及多项修复与文档更新。

- 🧩 新增 Sheet 组件：可从视口边缘滑入的可滑动覆盖层，基于原生浏览器滚动手势，适合移动端面板、导航抽屉和通知横幅。
- ⚡ 为 `@react-aria/optimize-locales-plugin` 增加 Turbopack 支持。
- ⌨️ 覆盖层定位现可感知虚拟键盘等交互式组件。
- 🛠️ 常规修复：`suppressHydrationWarning` 转发、`preventFocus` 的 `TypeError`、开发环境下隐藏子树警告、无效 `rgb()`/`rgba()` 报错、React Native `useControlledState` 早期副作用等。
- 🧭 组件改进：ComboBox 异步空结果后重新打开弹层；Date/Time 年份选择器包含最终约束年份并支持 CLDR 默认纪元；Forms 增加无效焦点移动警告；Link 支持 `aria-current`；Table、Tree、TokenField 等也有修复。
- 📦 发布包包括：`@internationalized/number@3.6.9`、`@react-types/shared@3.37.0`、`@react-aria/optimize-locales-plugin@2.1.0`、`react-aria@3.53.0`、`react-aria-components@1.22.0`、`react-stately@3.51.0`。
- 🙏 官方感谢所有贡献者。

---

### [](https://github.com/mui/material-ui/releases/tag/v9.5.0)

**原文标题**: [Release v9.5.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v9.5.0)

MUI Material UI v9.5.0 于 10 月 9 日发布，由 28 位贡献者参与，重点增强 Autocomplete 对非原始选项值的支持，并修复组件类型、插槽、主题、无障碍、测试与基础设施等多项问题。

- 🚀 发布：MUI Material UI v9.5.0 正式发布，感谢 28 位贡献者。
- ⚙️ Autocomplete：新增 `getOptionValue`，支持非原始选项值；修复 `groupBy` 变更崩溃、结果上限后继续过滤、初始输入值懒计算。
- 🧩 Material 类型/插槽：补充 `slotProps` override 接口；修复 Menu、Snackbar、SwipeableDrawer 的 `onClose` 类型；修复 Autocomplete chips、TextField `inputLabel`、NativeSelect `input` 的 slot 处理。
- 🎨 主题/样式：修复 `theme.alpha()` 对 CSS 变量和原始颜色；保留 CSS 变量回退；修复 Paper、Breadcrumbs、TablePagination、Tooltip 等主题异常与 Skeleton 背景回退。
- ♿ 无障碍：改进表格分页按钮、Drawer 关闭按钮、checkbox 列表等；新增无障碍合规报告页面，并自动化 WCAG 2.4.7 焦点可见检查。
- 🛠️ 组件修复：Button loading 样式泄漏、Checkbox indeterminate、Modal `aria-hidden`、Slider `disableSwap`、SpeedDial 提示位置、Tabs 滚动、TextField autofill 阴影等。
- 🧪 测试：为 Accordion、Avatar、Button、Checkbox、LinearProgress、Radio、Switch、TextField、ToggleButton 等增加 axe/WCAG 测试与报告；修复 DocSearch 视觉回归及 Vitest 导入。
- 📦 其他包：icons-material 居中 WarningRounded；system 清理重复 `filterProps` 并序列化 InitColorSchemeScript；utils 提升 `mergeSlotProps` 性能；types 移除无效 `number`；lab 修复 Masonry/Timeline。
- 📚 文档：新增 v10 下一版本、Cookie 偏好 URL 重开、v7 迁移图标 `data-testid`、Next.js 字体优化、NumberField `format`、Snackbar 对话框内 Escape 示例等。
- 🏗️ 核心/基础设施：CI 加入 Claude PR 审查、迁移 Babel 8、多项 TypeScript 转换、发布流程与 docs-infra 更新，包括限流、部署、OG 图像加固。
- 👥 贡献者：brijeshb42、Janpot 等 28 人；涉及 `@mui/material`、`icons-material`、`system`、`utils`、`types`、`lab`、`codemod`。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=reactstatus&utm_term=home&utm_content=Cooperpress)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=reactstatus&utm_term=home&utm_content=Cooperpress)

Expo 是面向代理式/AI 原生移动开发的基础设施平台，提供 CLI、SDK、EAS、云模拟器、OTA 更新与监控能力，帮助团队用单一代码库完成 Android、iOS 和 Web 应用的开发、测试、部署与发布。

- 🚀 定位为“代理式移动基础设施”，覆盖从开发到监控的完整工作流。
- 🛠️ 开发工具包括 Expo CLI、Skills、MCP、Expo Go、Simulators、Launch 和 Builds。
- 🧪 测试能力提供云模拟器与设备基础设施，Workflows 可在每次变更时运行测试套件。
- 📦 部署通过 Build 发布到 TestFlight 和应用商店，通过 Update 推送后续 OTA 更新。
- 📈 监控通过 Observe 展示崩溃信息、性能指标和 Update 采用率，并可快速发布修复。
- 🧩 Expo SDK 已打磨 10 年以上，包含 100+ 生产级 API，一次安装即可使用，也兼容原生代码。
- 📱 支持用同一代码库构建 Android、iOS 和 Web，并通过 Build 与 Hosting 分发。
- 🤖 云模拟器可由编码代理按需驱动，自动运行应用、验证工作，并附带截图、录屏和日志。
- ⚙️ Workflows 可自动化构建、测试、发送更新和发布流程。
- 📊 规模数据包括 3M+ 开发者、50K+ GitHub stars、7M+ 周下载、100K+ 活跃开发者、500K+ 项目和 100K+ 日构建。
- 🗣️ 社区反馈显示 80% 的 React Native 开发者选择 Expo，并称赞其易用、跨平台、库丰富和 OTA 更新能力。
- ✅ 获得 Meta 推荐、React Foundation 成员身份，并符合 SOC 2 Type II、GDPR、CCPA，支持 SSO。

---

### [](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=react-weekly&utm_content=homepage)

**原文标题**: [Trigger.dev | The open source platform for durable AI agents](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=react-weekly&utm_content=homepage)

Trigger.dev 是 Apache 2.0 开源平台，用于在 TypeScript 中构建可持久运行的 AI 智能体与工作流，并推出 Ask Trigger 帮助在仪表盘中通过聊天调试、调查运行并生成报告。  
- 🚀 支持长时任务、重试、队列、AI 可观测性与弹性扩展，构建能抵御刷新、重部署和崩溃的 AI 智能体。  
- 🛠️ 提供 chat.agent 能力：工具调用、人机协同审批、流式输出、遥测，并可直接流式传输到前端而无需 API 路由。  
- 🧩 覆盖自主智能体、提示链、路由、并行化、编排器、评估优化器等 AI 工作流模式。  
- ⏳ 将长时异步 AI 任务卸载到基础设施，避免超时；按实际执行付费，无需管理服务器。  
- 🔁 默认可靠：支持自动重试、条件重试、retry.onThrow、retry.fetch 和配置默认重试策略。  
- 📡 Realtime 可展示运行状态与元数据、实时更新 UI，并将 LLM 响应流从运行转发到前端。  
- 🐍 运行时自由：支持 Python、Prisma、Puppeteer、esbuild、FFmpeg、apt-get、附加包、音频波形和自定义构建扩展。  
- 📊 开发与生产功能包括 cron、React hooks、MCP、批量触发、等待、Webhook、多区域、静态 IP、AWS PrivateLink、并发队列、检查点、Vercel/GitHub 集成等。  
- 🔍 可观测性包括 LLM 监控、日志追踪、标签、高级运行筛选、批量操作、实时告警和仪表盘。  
- 🌍 客户案例包括 Supabase、Cal.com、Magic Patterns、MagicSchool AI、Pallet、Comp AI、HeroUI、Midday 等，用于规模化 AI 工作流。  
- 🆕 Changelog：Ask Trigger 仪表盘聊天、预览分支自动归档、并发与队列健康指标、主题与无障碍选项。  
- 💰 定价按使用量付费并可弹性扩展；开源可自托管，GitHub 16.5k+ stars，Discord 5.1k+ 成员。

---

### [Mozilla 节 - Mozilla 基金会](https://www.mozillafoundation.org/en/festival/?utm_medium=paid&utm_source=newsletter&utm_campaign=26-mozfest&utm_content=ad_react-status&utm_term=cooperpress)

**原文标题**: [
            
                
                    Mozilla Festival
                
            
            
                
                - Mozilla Foundation
            
        ](https://www.mozillafoundation.org/en/festival/?utm_medium=paid&utm_source=newsletter&utm_campaign=26-mozfest&utm_content=ad_react-status&utm_term=cooperpress)

内容仅为“Debates”一词，未提供完整文章或上下文，因此只能概括其核心主题为“辩论”，无法提取更多具体论点、背景或结论。

- 🗣️ 核心主题是“辩论”。
- 📄 未提供具体文章内容、背景或上下文。
- ❓ 缺少具体论点、论据与结论。
- 🔍 无法进一步提炼关键信息或细节。
- ✅ 可理解为围绕“辩论”展开的议题，但具体内容不详。

---

### [组件 — 着色器文档](https://shaders.com/docs/components)

**原文标题**: [Components — Shaders Documentation](https://shaders.com/docs/components)

此内容展示一个包含 190+（筛选显示 All 199）个视觉特效组件的组件库，按纹理、形状、形状效果、风格化、交互、扭曲、转场、模糊和调整分类，支持搜索与类别筛选，组件以 `<ComponentName />` 形式呈现。

- 🧩 组件库总览：190+ 个组件，实际列出 199 个，覆盖 9 大类别，适合生成、修饰、变形和转场视觉内容。
- 🎨 纹理 55 个：独立生成整帧画面，如极光、光束、有机斑点、噪声、渐变、网格、粒子、大理石、等离子、波纹、绸缎、文字、视频/摄像头纹理等。
- 📐 形状 16 个：清晰 SDF 形状，支持任意分辨率，如弧、圆、月牙、十字、椭圆、花、心、线、多边形、环、圆角矩形、星、泪滴、梯形、Vesica。
- ✨ 形状效果 23 个：为形状添加玻璃、金属、光效和材质，如拉丝金属、碳纤维、铬、水晶、浮雕、霜、玻璃、黏液、热图、全息、霓虹、黑曜石、粒子、塑料、烟雾填充、薄膜、体素、水。
- 🖌️ 风格化 31 个：处理下方图层外观，如 ASCII、黑板、色差、压缩伪影、等高线、CRT、数据毛刺、抖动、投影、雕刻、胶片颗粒、故障、辉光、渐变映射、半调、关键帧、镜头扭曲/光晕、光漏、物体追踪、纸张、粒子场、像素化、反射平面、闪光、石材、时间拖尾、VHS、晕影、水彩、羊毛。
- 🖱️ 交互 16 个：响应光标或模拟动态，如鸟群、ChromaFlow、光标涟漪/轨迹、雾、网格扭曲、墨流、液化、磁屑、粒子流、像素排序/投掷、反应扩散、破碎、烟雾/烟雾流。
- 🌀 扭曲 22 个：弯曲、置换和重映射内容，如条带位移、弯曲、膨胀、同心旋转、角点固定、置换贴图、翻转、流场、槽纹玻璃、3D 形体、玻璃砖、万花筒、镜像、透视、极坐标/直角坐标、重复器、球化、拉伸、3D 表面、旋转扭曲、波浪扭曲。
- 🎞️ 转场 13 个：两层之间的擦除、溶解和揭示，如谷仓门、块溶解、棋盘擦除、菱形擦除、虹膜擦除、线性擦除、噪声溶解、翻页、径向擦除、随机条、波纹擦除、切片擦除、百叶窗。
- 🌫️ 模糊 9 个：高斯、散景、通道、扩散、线性、渐进、移轴、缩放、角度模糊。
- 🎛️ 调整 14 个：颜色与色调修正，如亮度对比、双色调、曝光、胶片风格、灰度、色相偏移、反相、海报化、饱和度、锐度、日光化、着色、三色调、自然饱和度。
- ⚙️ 特别说明：HTMLInCanvas 需要 Chrome Canary 并启用 `chrome://flags/#canvas-draw-element`；Heatmap、LightEdge、LensDistortion 等部分效果由 Paper Shaders 支持。

---

### [Preact 11 – Preact](https://preactjs.com/blog/preact-11/)

**原文标题**: [Preact 11 – Preact](https://preactjs.com/blog/preact-11/)

Preact 11 已正式发布，这是基于 Preact X 稳定性与可靠性的重大版本更新，带来 Hydration 2.0、自动 ref 转发、hook 参数中的 Object.is 相等性检查等新功能，并提供迁移指南与第一方生态兼容支持。

- 🚀 Preact 11 正式发布，作为 Preact X 的增量更新，延续其稳定性与可靠性。
- ✨ 新功能包括 Hydration 2.0、自动 ref 转发，以及 hook 参数中的 Object.is 相等性检查。
- ⏳ “Road to Preact 11”议题始于六年多前，Preact X 的寿命被大幅延长，许多原本可能需破坏性变更的改进被纳入 X。
- 🧱 为避免影响性能与体积，团队最终决定汇总多年积累的破坏性变更，发布新主版本 Preact 11。
- 🌐 Preact 11 面向现代 Web，清理未完全成熟的功能，并更高效地支持未来用户。
- 📘 升级指南包含从 Preact X 迁移所需信息、新功能列表和支持的浏览器版本；多数用户升级应快速直接，改动多与更严格的类型相关。
- 📦 @preact/signals、preact-render-to-string、preact-iso、prefresh、@preact/preset-vite 等第一方包自预发布起已支持 Preact 11，依赖很可能已兼容。
- 🙏 团队感谢多年来为 Preact 及其生态做出贡献的人，并希望大家喜欢 Preact 11。
- 💙 署名：The Preact Team；页面日期：2026/9/29。

---

### [](https://sergiodxa.com/articles/the-remix-way)

**原文标题**: [The Remix Way](https://sergiodxa.com/articles/the-remix-way)

作者用近半年时间把博客和多个应用从 React Router 迁移到 Remix v3，通过"契约优先""少依赖""贴近 Web 标准"的方式自建了 88 个包、11 个应用，最终从"用 Remix 构建"转变为"以 Remix 之道构建"。

- 🧪 起点是重建约 650 篇文章的博客，涉及 D1 数据库、RSS/Atom/JSON Feed、缓存、Markdown 解析与代码高亮，原 monorepo 还含认证、监控等多个项目
- 📜 契约优先是核心思路：Remix 只提供 Postgres/MySQL/SQLite 适配器，但暴露 `Database` 接口，于是自建 D1 与 Durable Object 实现
- 🔌 同一模式复制到 `Cache`、`SessionStorage`、`Transport`、`Billing` 等：先写接口，再做内存版、Resend/Cloudflare、Polar/Stripe 等多套实现
- ✉️ 换邮件服务商只需改一行 `transport`，因为业务代码只依赖契约而非具体 SDK
- 🧩 基于 `remix/component` 重建 UI 库，尽量少用客户端 JS，博客实现零 hydration、无客户端入口
- 🎨 在 `css` mixin 上仿造 Tailwind 写出 `@sdxc/u`，支持嵌套、容器查询、颜色方案与选择器
- 📦 追求"近零依赖"，自建 rss、atom、markdown、highlight、jwt、saml、scim、mcp、jobs、i18n 等大量包，第三方依赖仅剩 Vite、Cloudflare 类型等开发依赖
- 🛣️ 路由定义与处理程序映射分离，路由表可同时用于服务端与客户端，从而解析真实 URL 并在路由消失时获得类型错误
- 🤖 应用整体是 `Request -> Response` 函数，因此 MCP 的工具与资源可直接复用路由处理程序，并支持中间件与限流
- ⏰ 后台任务同样采用"表 + 处理器 + 调度器"结构，通过 jobs 表获得输入类型校验与类型安全的入队方式
- 🌐 坚持"构建于 Web API 之上"：用 `command`/`commandfor` 原生属性连接 Button 与 Dialog，i18n 采用 MessageFormat 2 与 `Intl.MessageFormat`
- 🧭 多数自建包都是标准实现，避免重复造轮子
- 🧪 演示项目是一个招聘板：几千行代码（约半数是 JSDoc），复用了 19 个包
- ⚡ 列表页只 hydrate 一个 846 字节的 island，职位详情以 frame 按需加载 Markdown；验证码与限流是中间件，发布触发任务，邮件走内存 Transport 进入 outbox
- 🔗 全部代码位于 github.com/sergiodxa/monorepo，演示在 apps/demo
- 🏁 六个月、88 个包、11 个应用之后，作者表示自己不再只是"用 Remix 构建"，而是开始"以 Remix 的方式构建"

---

### [Deno 加入 Cloudflare | Cloudflare 博客](https://blog.cloudflare.com/deno-joins-cloudflare/)

**原文标题**: [Deno is joining Cloudflare | Cloudflare Blog](https://blog.cloudflare.com/deno-joins-cloudflare/)

Deno 团队加入 Cloudflare，双方计划将 celld 与 workerd 合并，让 Workers 和 Durable Objects 的自托管变得极其简单，并使同一套编程模型可在更多环境中运行。

- 🤝 Deno 团队加入 Cloudflare，由 Ryan Dahl 与 Kenton Varda 共同宣布这一消息。
- 🧩 核心目标：把 Deno 的 celld 与 Cloudflare 的 workerd 合并，简化 Workers 和 Durable Objects 的自托管。
- 🧠 Ryan Dahl 回顾 Node.js 与 Deno 经历，认为分布式计算、状态协调、数据存储和自动扩缩容才是更大的难题。
- 🗄️ Durable Objects 提供“分布式单例 + SQLite”抽象：每个对象像可寻址的小型服务器，单线程执行 JavaScript，支持 WebSocket 和同步 SQLite。
- 📈 每个聊天频道使用一个 Durable Object，就能自然分片数据和连接，实现可扩展性；还可构建 Queues、KV、Workflow、Git 存储等服务。
- 🌐 但在 Cloudflare 之外运行 Durable Objects 一直很难，workerd 虽已开源，Durable Objects 却只支持单实例，适合本地测试但不适合扩展。
- 🦀 Ryan 因此发起 celld：一个 Rust 编写的单二进制方案，仅依赖对象存储，面向自托管和分布式扩展。
- 🔓 Kenton 反驳“Workers 锁定用户”的说法：Workers 与众不同是因为它更好，而不是为了制造迁移壁垒。
- 💡 Workers 的优势包括全球多地点低成本部署、bindings 更易配置且更安全，以及 Durable Objects 对实时协作和分布式系统的支持。
- 🧑‍💻 2022 年 Shopify 等客户要求开源 Workers Runtime，Cloudflare 因此开源 workerd；已有客户通过 workerd 迁移离开。
- ⚠️ workerd 的生产就绪缺口是 Durable Objects：其生产级路由实现复杂，依赖大量外部服务，不适合自托管场景。
- 🎯 Deno 的 celld 与 Workers/Durable Objects 兼容，同时专注自托管与扩展，因此 Cloudflare 非常高兴与其合作。
- 🚀 Ryan 和 Bert 将领导把 celld 的代码与思路合并回 workerd，使自托管成为一等支持方式。
- 📅 未来数月会有更多公告；目前已经可以开始自托管 celld 或 workerd。

---

