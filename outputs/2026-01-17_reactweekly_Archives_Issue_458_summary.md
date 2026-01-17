### [React 状态问题 458:2026 年 1 月 16 日](https://react.statuscode.com/issues/458)

**原文标题**: [React Status Issue 458: January 16, 2026](https://react.statuscode.com/issues/458)

本期通讯聚焦于 React 生态的最新动态，包括 Vercel 推出的 React 最佳实践指南、Node.js 的关键安全修复、React 19 中 useOptimistic 钩子的局限性探讨，以及一系列新工具和库的发布，如 GTKX 用于构建原生 Linux 桌面应用、Voltra 用于 React Native 的 iOS 组件开发等。

- 🚀 Vercel 团队发布 React 最佳实践指南，旨在帮助编码代理或开发者编写更优的 React 代码。
- 🛠️ 引入 Pintura 图像编辑器组件，可轻松为 Web 应用添加图像编辑功能。
- 🔍 文章探讨如何通过 React 内部数据结构和 LLM“重构”生产环境中的 React 组件。
- ⚠️ Node.js 修复了 AsyncLocalStorage 中可能导致生产服务器崩溃的安全漏洞。
- 📦 Microsoft 的 Aspire 框架现在将 JavaScript 视为一等公民，支持 React 应用的全流程构建和部署。
- 🏢 Astro 框架背后的公司被 Cloudflare 收购，同时 Astro 6 测试版发布。
- ⚙️ Cursor 开发工具正考虑从 Solid 迁移到 React。
- 🎨 React Bits 创建者 David Haz 接受采访，分享动画组件的开发经验。
- ⚡ 文章指出 React 19 的 useOptimistic 钩子虽简化乐观更新，但仍存在复杂问题，建议由框架处理。
- 🧩 探讨如何构建类型安全的复合组件，以提供灵活且避免臃肿 API 的组件库设计。
- 🐧 GTKX 允许使用 React 和 GTK4 构建原生 Linux 桌面应用，无需 Webview 或 Electron。
- 📱 Voltra 支持在 React Native 中开发 iOS Live Activities 和 Widgets，无需编写 Swift 代码。
- 🔧 X-Ray React 提供布局调试工具，一键显示组件渲染层并快速定位源代码。
- 🎙️ gemini-live-react 钩子支持与 Google Gemini Live API 进行双向语音流处理。
- 📚 其他更新包括 React hCaptcha 组件 2.0、React Native Audio API 0.11、Zustand 5.0.10 等库的新版本发布。

---

### [介绍：React 最佳实践 - Vercel](https://vercel.com/blog/introducing-react-best-practices)

**原文标题**: [Introducing: React Best Practices - Vercel](https://vercel.com/blog/introducing-react-best-practices)

本文介绍了一个名为“react-best-practices”的结构化知识库，它总结了十多年 React 和 Next.js 性能优化的经验，旨在帮助开发者和 AI 代理系统性地识别和解决常见性能问题，避免被动优化。

- 🚀 **核心原则是优先级排序**：性能优化应从影响最大的层面开始，如消除异步瀑布流和减少包体积，再逐步处理其他问题。
- 📦 **涵盖八大性能类别**：包括消除异步瀑布、包体积优化、服务端性能、客户端数据获取、重渲染优化等，共 40 多条规则。
- ⚠️ **每条规则标注影响等级**：从“关键”到“低”帮助团队优先处理最重要的问题，并提供错误和正确代码示例。
- 🛠️ **源自真实生产案例**：规则基于实际项目经验，如合并循环迭代、并行化异步操作和惰性状态初始化。
- 🤖 **支持 AI 代理集成**：知识库可编译为单一文档供 AI 代理查询，并封装为“Agent Skills”插件，嵌入各种编程助手工具中。

---

### [agent-skills/skills/react-best-practices/rules at main · vercel-labs/agent-skills · GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices/rules)

**原文标题**: [agent-skills/skills/react-best-practices/rules at main · vercel-labs/agent-skills · GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices/rules)

这是一个由 Vercel Labs 维护的名为"agent-skills"的公共开源项目仓库。

- 🚀 **项目状态** - 这是一个公开的 GitHub 仓库，属于 Vercel Labs 组织
- ⭐ **受欢迎程度** - 获得了 9.5k 星标，有 777 个分支，表明项目很受欢迎
- 🔧 **开发活跃度** - 有 11 个未解决的问题和 8 个拉取请求，显示项目正在积极开发中
- 📁 **仓库结构** - 包含标准的 GitHub 仓库部分：代码、问题、拉取请求、操作、项目和安全设置
- ⚠️ **技术问题** - 页面加载时出现错误提示，需要重新加载页面
- 🔍 **导航选项** - 提供额外的导航选项来访问仓库的不同部分

---

### [OpenCode | 开源 AI 编程助手](https://opencode.ai/)

**原文标题**: [OpenCode | The open source AI coding agent](https://opencode.ai/)

OpenCode 是一款开源的 AI 编程助手，可在终端、IDE 或桌面应用中帮助开发者编写代码，支持多种模型和编辑器，注重隐私保护且完全免费。

- 🚀 **开源 AI 编程助手** – 提供终端、桌面应用及 IDE 扩展，支持多会话并行和 LSP 自动加载
- 🔗 **灵活模型集成** – 内置免费模型，可连接 Claude、GPT、Gemini 等 75+ 供应商或本地模型
- 🌟 **社区高度活跃** – 拥有 7 万 GitHub 星标、500 名贡献者，月均服务 65 万开发者
- 🛡️ **隐私优先设计** – 不存储用户代码或上下文数据，适用于敏感环境
- 💻 **多平台覆盖** – 支持 macOS、Windows 和 Linux 系统，提供桌面版测试应用
- 🔄 **便捷协作功能** – 支持生成会话链接供参考或调试，可共享工作进度
- 📊 **优化模型服务** – 通过 Zen 平台提供经测试验证的专用编码模型，保障性能稳定

---

### [React 图像编辑器，基于 Pintura SDK 驱动](https://pqina.nl/pintura/react-image-editor/?ref=cooperpress)

**原文标题**: [React Image Editor, Powered by Pintura SDK](https://pqina.nl/pintura/react-image-editor/?ref=cooperpress)

Pintura Image Editor 是一款功能强大、高度可配置的 React 图像编辑 SDK，可轻松集成到项目中，提供从基础裁剪到高级注释的全面编辑功能，并支持多框架使用。

- 🖼️ 提供全面的图像编辑功能，包括裁剪、旋转、调整、滤镜、注释、调整颜色等
- ⚙️ 高度可配置，支持自定义界面语言、图标、主题及各种编辑规则
- 📱 响应式设计，在移动端和桌面端均提供直观的触摸、鼠标和键盘交互支持
- 🔧 支持多种图像格式（JPEG、PNG、GIF、WEBP、BMP、SVG），并可扩展加载 HEIC、PDF 等格式
- 🧩 包含多种集成组件（模态框、内联、覆盖层），并支持与服务端或后台图像处理结合
- 🚀 易于集成，通过 npm 安装即可快速添加到 React 项目，也支持 Vue、Angular、Svelte 等其他框架
- 🌍 被全球数千家公司信任使用，拥有良好的用户评价和支持社区

---

### [如何窃取任意 React 组件](https://fant.io/react/)

**原文标题**: [How to Steal Any React Component](https://fant.io/react/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🩺 AI 在医学影像分析中表现出色，能辅助医生更精准地识别肿瘤等病变
- 💊 通过分析海量数据，AI 可帮助制定个性化治疗方案，提升治疗效果
- ⚙️ 智能系统能自动化处理行政流程，减轻医护人员负担，提高医院运营效率
- 🤖 聊天机器人和虚拟助手为患者提供 24 小时健康咨询与用药提醒服务
- ⚖️ 应用同时引发数据隐私、算法偏见及医患关系变化等伦理与社会议题

---

### [GitHub - acdlite/react-fiber-architecture: React 新核心算法 React Fiber 的解析](https://github.com/acdlite/react-fiber-architecture)

**原文标题**: [GitHub - acdlite/react-fiber-architecture: A description of React's new core algorithm, React Fiber](https://github.com/acdlite/react-fiber-architecture)

React Fiber 是 React 核心算法的重新实现，旨在通过增量渲染等特性提升动画、布局和手势处理的适用性，并引入优先级调度、可中断和重用工作等能力，以优化用户体验和性能。

- 🚀 **增量渲染**：将渲染工作拆分为多个块，分散到不同帧中执行，避免阻塞主线程。
- ⏸️ **可调度工作**：支持暂停、中止或重用任务，根据更新优先级灵活安排工作。
- 🎯 **优先级分配**：为不同类型的更新分配优先级，确保用户交互等高优先级任务及时响应。
- 🔄 **虚拟栈帧**：用 Fiber 作为虚拟栈帧，替代传统调用栈，实现手动控制任务执行时机。
- 🌳 **树结构表示**：Fiber 通过 child、sibling 和 return 字段描述组件树结构，支持递归遍历。
- 📦 **组件与属性**：Fiber 存储组件类型、key 和 props，通过比较 props 决定是否重用输出。
- 🔁 **双缓存机制**：使用 current 和 work-in-progress 两个 Fiber 交替工作，减少对象创建开销。
- 🎨 **渲染器分离**：协调器与渲染器解耦，使 React 能跨平台（如 DOM、React Native）使用同一协调算法。

---

### [Node.js 修复可能导致崩溃的 AsyncLocalStorage 异步本地存储错误](https://socket.dev/blog/node-js-fixes-asynclocalstorage-crash-bug-that-could-take-down-production-servers)

**原文标题**: [Node.js Fixes AsyncLocalStorage Crash Bug That Could Take Do...](https://socket.dev/blog/node-js-fixes-asynclocalstorage-crash-bug-that-could-take-down-production-servers)

近期发现五个协同作恶的 Chrome 扩展程序，能够劫持企业人力资源和 ERP 系统会话并绕过安全防护，对企业数据安全构成严重威胁。

- 🕵️ 五个恶意扩展程序协同攻击企业 HR 与 ERP 系统
- 🔓 通过会话劫持技术绕过平台安全控制机制
- ⚠️ 主要威胁对象为使用相关企业管理系统的大型机构
- 📅 该安全威胁于 2026 年 1 月 15 日由研究员 Kush Pandya 披露
- 🛡️ 企业需立即检查并移除可疑浏览器扩展以防范风险

---

### [Node.js — 2026 年 1 月 13 日星期二安全版本发布](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

**原文标题**: [Node.js — Tuesday, January 13, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

Node.js 项目于 2026 年 1 月 13 日发布了针对 20.x、22.x、24.x 和 25.x 版本线的安全更新，以解决多个安全漏洞。此次更新共修复了 3 个高危问题、4 个中危问题和 1 个低危问题，并更新了相关依赖项。所有处于活跃维护期的版本均受影响，建议用户尽快升级至最新版本以确保系统安全。

- 🚨 **高危漏洞**：修复了 3 个高危问题，包括缓冲区未初始化内存泄露（CVE-2025-55131）、权限模型绕过（CVE-2025-55130）和 HTTP/2 服务崩溃（CVE-2025-59465），可能造成数据泄露、权限提升或服务拒绝。
- ⚠️ **中危漏洞**：解决了 4 个中危问题，涉及不可捕获的调用栈溢出错误（CVE-2025-59466）、TLS 内存泄露（CVE-2025-59464）、Unix 域套接字权限绕过（CVE-2026-21636）和 TLS 回调异常处理缺陷（CVE-2026-21637），可能导致服务崩溃或资源耗尽。
- 📝 **低危漏洞**：修复了 1 个低危问题（CVE-2025-55132），涉及文件系统时间戳修改权限绕过，可能影响审计日志的可靠性。
- 🔄 **依赖更新**：安全版本包含了对 c-ares 和 undici 等依赖项的更新，以解决已公开的漏洞。
- 📅 **发布与支持**：新版本（20.20.0、22.22.0、24.13.0、25.3.0）已于 2025 年 12 月 15 日或之后发布。对于已结束维护的版本，可通过 OpenJS 生态系统可持续性计划合作伙伴获得商业支持。
- 📢 **后续行动**：建议所有用户升级至最新版本。安全策略和漏洞报告流程可在 Node.js 官方网站和 GitHub 仓库查看，用户可订阅安全邮件列表以获取更新。

---

### [Aspire —— 您的技术栈，精简高效](https://aspire.dev/)

**原文标题**: [Aspire â Your stack, streamlined](https://aspire.dev/)

Aspire 13.1 已正式发布，这是一个面向开发者的开源平台，旨在通过代码定义和编排应用栈，实现本地开发与生产部署的无缝衔接。

- 🚀 **版本发布**：Aspire 13.1 已正式发布，带来新功能和改进。
- 🧩 **模块化与可扩展**：可轻松编排前端、API、容器和数据库，无需重写代码，并能灵活扩展以适应任何技术栈。
- 💻 **代码中心化控制**：通过类型安全且可读的代码定义整个应用栈，支持本地运行并部署到任何环境，无需架构更改。
- 🔍 **开箱即用的可观测性**：内置 OpenTelemetry，自动提供日志、追踪和健康检查，无需额外设置即可快速调试。
- 🌐 **灵活的部署选项**：支持部署到 Kubernetes、云平台或本地环境，适应不同部署需求，保持一致性。
- 🗣️ **多语言支持**：原生支持 C#、Java、Python、JavaScript、TypeScript、Go 等多种编程语言。
- 🏠 **本地优先，生产就绪**：在本地模拟生产环境，消除“在我机器上能运行”的问题，确保平滑部署。
- 📊 **集成开发者仪表盘**：提供实时监控日志、指标和追踪的 OpenTelemetry 仪表盘，提升开发效率。
- ☁️ **多云与广泛集成**：支持连接 Azure、AWS 或自有基础设施，拥有丰富的集成生态。
- 🆓 **免费开源**：始终免费且开源，拥有活跃的社区，共同推动现代开发的发展。

---

### [JavaScript 开发者的追求 | Aspire 博客](https://devblogs.microsoft.com/aspire/aspire-for-javascript-developers/)

**原文标题**: [Aspire for JavaScript developers | Aspire Blog](https://devblogs.microsoft.com/aspire/aspire-for-javascript-developers/)

Aspire 13 为 JavaScript 和 TypeScript 开发者提供了一流的分布式应用编排支持，通过 `Aspire.Hosting.JavaScript` 包实现了对 JavaScript 应用的全面开发、调试和部署能力。

- 🚀 **支持多种运行方式**：提供 `AddJavaScriptApp()`、`AddNodeApp()` 和 `AddViteApp()` 三种方法，分别适用于 npm 脚本项目、直接 Node.js 执行和 Vite 前端框架。
- 📦 **包管理器兼容**：默认支持 npm，也可轻松切换至 Yarn 或 pnpm，并针对各包管理器在生产环境提供优化安装命令。
- ⚙️ **脚本灵活定制**：允许自定义开发与构建脚本，并支持传递参数，适应不同项目需求。
- 🔒 **HTTPS 自动配置**：Vite 应用可通过 `WithHttpsEndpoint()` 和 `WithHttpsDeveloperCertificate()` 启用 HTTPS，且不破坏现有配置。
- 🌐 **服务自动发现**：JavaScript 应用可无缝接入 Aspire 的服务发现，通过环境变量获取后端服务地址，无需硬编码。
- 🗄️ **数据库连接多样化**：提供 URI 和独立参数两种连接格式，兼容 Prisma、TypeORM、node-postgres 等主流数据库库。
- 🐳 **生产就绪的 Dockerfile**：自动生成优化过的单阶段或多阶段 Dockerfile，支持 BuildKit 缓存挂载，提升构建速度与安全性。
- 🔧 **开发体验增强**：集成 OpenTelemetry 实现可观测性，自动设置 `NODE_ENV`，并处理证书信任问题，简化本地开发。
- 📚 **TypeScript 原生支持**：完全支持 TypeScript 项目，依赖现有构建流程，无需额外配置。
- 🎯 **社区驱动发展**：功能基于 Aspire Community Toolkit 的贡献，体现了社区驱动的开发模式，未来可能支持多语言 AppHost。

---

### [Astro 科技公司加入 Cloudflare | Astro](https://astro.build/blog/joining-cloudflare/)

**原文标题**: [The Astro Technology Company joins Cloudflare | Astro](https://astro.build/blog/joining-cloudflare/)

Astro Technology Company 宣布加入 Cloudflare，以获取更多资源支持，专注于开发面向内容驱动网站的最佳框架，同时保持开源、跨平台兼容及现有发展路线不变。

- 🚀 Astro 框架加入 Cloudflare，获得更多资源支持，专注框架开发
- 🔓 保持开源 MIT 许可，继续跨平台部署支持
- 📈 年下载量近百万次，被数十万开发者用于构建高性能网站
- 🎯 专注于内容驱动网站框架，解决传统应用架构性能问题
- 💼 曾尝试商业化未果，现回归技术核心
- 🌐 与 Cloudflare 基础设施优势互补，共同推动网络发展
- 📅 Astro 6 即将发布，2026 年路线图持续更新
- 🙏 感谢投资者、社区及用户长期支持

---

### [Astro 6 Beta | Astro](https://astro.build/blog/astro-6-beta/)

**原文标题**: [Astro 6 Beta | Astro](https://astro.build/blog/astro-6-beta/)

Astro 6 Beta 发布，带来重新设计的开发服务器、显著的渲染性能提升以及用于处理 CSP、字体和实时内容集合的新内置 API。该版本专注于统一开发与生产环境，提升稳定性，并增强对 Cloudflare Workers 等平台的支持。

- 🚀 **开发服务器重构**：利用 Vite 环境 API，使开发与生产环境代码路径更接近，提升跨运行时的稳定性。
- ☁️ **Cloudflare Workers 原生支持**：开发时直接使用 workerd 运行时，支持 Durable Objects、KV 等真实平台 API，提供更贴近生产的开发体验。
- 🔄 **实时内容集合稳定**：支持实时更新数据而无需重新构建，适用于需要高数据新鲜度的场景，如实时股价或库存。
- 🛡️ **内容安全策略（CSP）稳定**：提供默认保护，可自定义策略，兼容所有官方适配器，自动生成 CSP 头或元元素。
- ⚠️ **重大变更与迁移**：移除已弃用 API，要求 Node 22+，更新集成 API 和 Cloudflare 适配器，升级至 Zod 4。
- 🧪 **测试与反馈**：当前为 Beta 版本，鼓励用户测试 workerd 支持并提供反馈，以完善功能。
- 📦 **快速开始**：可通过 create astro 命令新建项目，或使用 @astrojs/upgrade CLI 工具升级现有项目至 Beta 版本。

---

### [扩展长期自主编码能力 · Cursor](https://cursor.com/blog/scaling-agents#running-for-weeks)

**原文标题**: [Scaling long-running autonomous coding · Cursor](https://cursor.com/blog/scaling-agents#running-for-weeks)

本文探讨了如何通过多智能体协作来扩展长期自主编码项目，分享了从数百个并发智能体协作中获得的经验，包括协调机制、角色分工以及实际项目应用。

- 🧠 **单智能体的局限性**：当前智能体擅长专注任务，但在复杂项目中效率低下，并行运行多智能体面临协调挑战。
- 🔄 **协调学习的尝试**：初期采用动态协调和文件锁机制，但出现锁竞争、系统脆弱和智能体风险规避等问题。
- 👥 **规划者与执行者的分工**：引入分层结构，规划者负责探索和任务创建，执行者专注完成任务，解决了协调瓶颈并支持大规模项目。
- ⏳ **长期运行的实验**：智能体在构建浏览器、代码库迁移等项目中运行数周，生成数百万行代码，展示了协作的可行性和效率。
- 📊 **经验总结**：模型选择（如 GPT-5.2）对长期任务至关重要，简化系统结构比增加复杂性更有效，提示设计对智能体行为影响显著。
- 🚀 **未来展望**：多智能体协调仍是难题，但当前系统已证明数百智能体可协作完成雄心勃勃的项目，相关技术将用于提升 Cursor 的智能体能力。

---

### [专访：React Bits 创作者 David Haz - Motion 杂志](https://motion.dev/magazine/interview-david-haz-creator-of-react-bits)

**原文标题**: [Interview: David Haz, creator of React Bits - Motion Magazine](https://motion.dev/magazine/interview-david-haz-creator-of-react-bits)

React Bits 是一个开源项目，包含超过 100 个动画和交互式 React 组件，以其创意和实验性设计在众多组件库中脱颖而出。项目在 GitHub 上已获得超过 3 万星标，其专业版 React Bits Pro 即将发布。创始人 David Haz 分享了项目的起源、开发过程、技术选型以及对 AI 工具的看法。

- 🚀 **项目起源与性质**：React Bits 最初是 David 的业余开源项目，意外获得巨大关注。它并非计划中的商业产品，而是凭借其独特性和自由创意逐渐积累人气。
- 💼 **时间与收入分配**：David 的主要收入来源是全职前端工程师工作，他大约将 20% 的业余时间投入 React Bits 及其姊妹项目 Vue Bits 的开发，项目近期才开通赞助选项。
- 🌟 **成功关键**：项目的成功源于其独特性，不受单一风格限制。早期组件如 `<SplashCursor />` 吸引了大量关注，但整体增长是渐进的。
- 🛠️ **开发与测试流程**：组件的 TypeScript/JavaScript 和 CSS/Tailwind 版本主要通过手动和 AI 辅助转换完成，测试依赖手动和开源社区的帮助。David 使用自定义脚本自动生成多版本文件结构。
- 🔧 **技术栈选择**：早期多使用 GSAP，现在更倾向于 Motion，尤其是在 React Bits Pro 中。David 常用 Motion 的 `<AnimatePresence />`、运动组件及相关钩子来构建动画。
- 🤖 **AI 在开发中的作用**：AI 工具（如 Opus 4.5）极大地提升了 David 的工作效率，尤其在复杂 WebGL 组件开发和跨组件 bug 修复方面。他认为 AI 不会威胁组件库，反而能将其作为扩展工具，提升开发质量。
- 💡 **灵感来源**：David 从 CodePen、Awwwards、Dribbble 等网站获取设计灵感，将令人惊艳的效果转化为组件，并经过多次迭代完善。
- 🆕 **React Bits Pro 的推出**：专业版的推出是应社区需求而生，并非最初计划。它将是一个全新的、规模更大的组件集合，不会对现有免费组件设置付费墙。
- 🔮 **未来展望**：David 计划探索 WebGPU 以提升性能，并希望 Motion 能加强滚动动画的文档和示例。他认为组件库将与 AI 更深度结合，帮助开发者更高效地构建创意界面。

---

### [React Bits - React 动画 UI 组件](https://reactbits.dev/)

**原文标题**: [React Bits - Animated UI Components For React](https://reactbits.dev/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🩺 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可整合患者数据，为精准医疗提供支持
- 📊 智能医疗管理系统能自动化处理病历、优化医院资源分配，减轻行政负担
- ⚖️ 数据隐私保护与算法透明度成为 AI 医疗应用需要应对的重要伦理议题

---

### [useOptimistic 救不了你 | 科勒姆·凯利 | 科勒姆·凯利](https://www.columkelly.com/blog/use-optimistic)

**原文标题**: [useOptimistic Won't Save You | Colum Kelly | Colum Kelly](https://www.columkelly.com/blog/use-optimistic)

React 19 的 useOptimistic 钩子旨在简化乐观 UI 更新，但它并未完全解决竞态条件等问题，且需要结合 useTransition、useActionState 等 API 才能正确使用，导致实现依然复杂。作者建议将这些底层 API 留给框架开发者处理，普通开发者应依赖框架封装以降低复杂度。

- 🚀 **乐观 UI 更新**：通过立即响应用户操作提升界面响应速度，但传统手动实现容易导致界面闪烁或状态不同步。
- 🐛 **竞态条件问题**：在并发请求下，简单的乐观更新可能引发状态混乱，需额外逻辑（如请求 ID 跟踪）来避免。
- 🔄 **过渡（Transition）限制**：在 React 的过渡更新中，直接状态更新不会立即渲染，需依赖 useOptimistic 实现即时 UI 反馈。
- 🛠️ **useOptimistic 的局限**：该钩子虽支持过渡内的乐观更新，但无法单独处理竞态条件，需结合 useActionState 等 API。
- 📦 **框架推荐**：React 团队建议通过框架（如 Next.js）封装复杂 API，以减少开发者需处理的样板代码和潜在错误。

---

### [useOptimistic – React](https://react.dev/reference/react/useOptimistic)

**原文标题**: [useOptimistic – React](https://react.dev/reference/react/useOptimistic)

`useOptimistic` 是一个 React Hook，用于在异步操作（如网络请求）进行期间，乐观地更新用户界面以提升响应速度。它接受一个状态和一个更新函数，返回一个乐观状态和一个派发函数，允许界面在操作实际完成前立即显示预期结果。

- 🚀 **乐观更新 UI**：在异步操作进行时，立即显示预期结果，提升用户体验。
- 🔧 **基本用法**：`const [optimisticState, addOptimistic] = useOptimistic(state, updateFn)`，其中`updateFn`合并当前状态与乐观值。
- 📝 **表单应用示例**：用户发送消息时，消息立即显示“发送中”标签，无需等待服务器响应。
- ⚙️ **参数说明**：`state`为初始状态，`updateFn`为纯函数，接收当前状态和乐观值，返回合并后的乐观状态。
- 🔄 **返回值**：`optimisticState`为乐观状态，`addOptimistic`用于触发乐观更新。

---

### [构建类型安全的复合组件 | TkDodo 的博客](https://tkdodo.eu/blog/building-type-safe-compound-components)

**原文标题**: [Building Type-Safe Compound Components | TkDodo's blog](https://tkdodo.eu/blog/building-type-safe-compound-components)

本文探讨了在构建组件库时使用复合组件模式的优势与局限，并提出了通过组件工厂模式实现类型安全的方法。

- 🧩 复合组件模式在组件库设计中提供了灵活性，允许用户自由组合子组件，避免了单一组件因过度依赖属性而变得臃肿。
- ⚠️ 复合组件并非适用于所有场景，例如固定布局或动态内容较多的组件（如选择框）可能更适合使用属性传递。
- 🔧 通过组件工厂模式（如 `createRadioGroup`）可以实现复合组件的类型安全，确保父组件与子组件之间的类型一致性。
- 📐 对于需要严格布局和顺序的组件（如模态对话框），使用插槽（slots）模式比复合组件更合适，能保证一致性和结构。
- 🎯 复合组件最适合需要灵活布局且内容相对静态的场景，例如按钮组、标签栏或单选按钮组。

---

### [将静态网站部署到任意云端](https://www.cloud66.com/products/static-sites/)

**原文标题**: [Deploy Static Sites to Any Cloud](https://www.cloud66.com/products/static-sites/)

Cloud 66 提供静态网站部署服务，支持将网站部署到任何兼容 S3 的云存储，并与任意 CDN 配合使用，实现高可控性、高性价比的静态网站托管。

- 🚀 **灵活部署**：支持将静态网站部署到任何兼容 S3 的云存储（如 AWS、GCP、Azure 等），并可搭配任意 CDN 加速。
- 💰 **节省成本**：通过结合自有 S3 存储与 Cloud 66 服务，可节省高达 40% 的静态网站托管费用。
- 🛠️ **广泛兼容**：支持多种静态网站生成器（如 Jekyll、Hugo、Gatsby、Astro 等），并提供自定义构建选项。
- 🔒 **全面控制**：支持基于请求路径、IP、方法等条件，通过 CEL 语言配置流量规则，实现精细化的访问控制。
- 📊 **实时监控**：提供实时流量日志，可查看来源 IP、请求路径、响应状态等详细信息。
- 🔧 **生产就绪**：包含预览部署、自动 SSL 证书管理、密钥与变量管理等生产环境所需功能。
- 🌍 **高可用性**：依托 S3 存储的全球可靠性，结合 CDN 实现低延迟访问，确保网站高性能与高可用。

---

### [你能用 React 服务器操作获取数据吗？](https://www.developerway.com/posts/server-actions-for-data-fetching)

**原文标题**: [Can You Fetch Data with React Server Actions?](https://www.developerway.com/posts/server-actions-for-data-fetching)

本文探讨了是否可以使用 React Server Actions（现称 Server Functions）进行客户端数据获取。虽然技术上可行，但存在性能缺陷，特别是并行请求会变为串行，导致加载时间显著增加。文章建议在客户端数据获取时仍使用传统的 REST 请求配合数据获取库（如 TanStack Query），而非 Server Actions。

- 🧐 **技术可行性**：Server Actions 本质上是 POST 请求的封装，可用于数据获取，提供类型安全和 IDE 自动补全。
- ⚠️ **性能问题**：主要缺陷是并行请求会变为串行处理，大幅延长数据加载时间（例如从 1.7 秒增至 8 秒）。
- 🔍 **调试困难**：网络面板中所有请求名称相同，响应格式不易阅读，调试体验较差。
- 🚫 **缓存限制**：POST 请求无法利用浏览器或 CDN 的 HTTP 缓存机制，但客户端缓存仍可工作。
- 💡 **替代方案**：建议在客户端使用 REST 请求配合数据获取库（如 TanStack Query），而非 Server Actions。
- 📊 **渲染方式对比**：文章比较了不同渲染方式（SSR、Server Components）的性能数据，强调需根据场景选择。
- 🛠️ **正确使用场景**：Server Actions 更适合数据变更操作，而非数据获取；客户端获取数据仍具实际价值。

---

### [获取失败](https://react.statuscode.com/link/179417/web)

**原文标题**: [Failed to retrieve](https://react.statuscode.com/link/179417/web)

无法总结：获取内容失败，状态码 429。

---

### [在 React.js 中跨页面视图保持动画状态 - Andrew Magill，Web 工程师](https://magill.dev/post/persisting-animation-state-across-page-views-in-Reactjs)

**原文标题**: [Persisting Animation State Across Page-Views In React.js - Andrew Magill, Web Engineer](https://magill.dev/post/persisting-animation-state-across-page-views-in-Reactjs)

本文介绍了在 React.js 中通过种子随机化、确定性状态和 CSS 参数插值，实现跨页面视图保持动画状态的方法，解决了静态站点生成（SSG）中动画重置的问题。

- 🎯 使用本地存储跟踪随机值和当前外观，存储动画开始时间戳和种子，确保状态持久化
- ⚙️ 通过`requestAnimationFrame`更新动画状态，避免 React 同步渲染警告，保持动画同步
- 🎨 将 JavaScript 计算的状态值转换为 CSS 自定义属性，利用`@property`规则和关键帧实现平滑插值
- ⏪ 设置负的`animation-delay`值，让浏览器“快进”到动画当前应处位置，模拟持续播放效果
- 📱 采用`will-change`、`transform`和 GPU 驱动关键帧等技术，确保动画在各种设备上流畅运行
- 🌱 种子随机化确保每次会话动画参数一致，本地存储使返回用户能继续之前的动画进度
- 🔗 作者在 GitHub 上分享了完整实现代码，并提供了相关 CSS 自定义属性、种子随机数和 CSS Houdini 的参考资料

---

### [GTKX](https://eugeniodepalo.github.io/gtkx/)

**原文标题**: [GTKX](https://eugeniodepalo.github.io/gtkx/)

GTKX 是一个让开发者能够使用 React 构建原生 GTK4 桌面应用的框架，它结合了 React 的现代开发体验与 GTK4 的原生性能和功能。

- ⚛️ 完整支持 React 19，包括组件、钩子、状态和效果等熟悉的 React 模型
- 🚀 通过 Rust/Neon 直接绑定 GTK4，无需 Electron 或 WebView，实现真正的原生性能
- 🧩 提供完整的 GTK4、Libadwaita 和 GLib API 访问，所有绑定都经过类型化处理
- ⚡ 支持 Vite 驱动的热模块替换，开发时可获得即时反馈，实现快速迭代
- 🎨 采用 CSS-in-JS 样式方案，使用熟悉的 CSS-in-JS 模式编写样式，最终编译为 GTK CSS
- 🧪 提供类似 Testing Library 的测试 API，并内置 MCP 服务器以集成 AI 代理

---

### [沃尔特拉](https://www.use-voltra.dev/)

**原文标题**: [Voltra](https://www.use-voltra.dev/)

使用 JSX 中的 SwiftUI 原语，通过 VStack、HStack、Text、Symbol 和 LinearGradient 等组件直接构建实时活动，React 组件将渲染为原生 SwiftUI 元素。

- 🏗️ 在 JSX 中直接使用 SwiftUI 原语构建实时活动
- 🔗 React 组件可渲染为原生 SwiftUI 元素
- 📱 支持 VStack、HStack、Text、Symbol 和 LinearGradient 等组件

---

### [GitHub - callstackincubator/voltra: Voltra 让 React Native 开发者能够以 React 组件形式构建原生 iOS 实时活动、灵动岛布局和小部件，无需编写 Swift。它支持热重载、推送更新，并包含一个自动配置所有内容的插件。](https://github.com/callstackincubator/voltra)

**原文标题**: [GitHub - callstackincubator/voltra: Voltra lets React Native developers build native iOS Live Activities, Dynamic Island layouts, and widgets as React components without writing Swift. It supports hot reload, push updates, and includes a config plugin that wires everything automatically.](https://github.com/callstackincubator/voltra)

Voltra 是一个让 React Native 开发者能够使用 React 组件构建原生 iOS Live Activities、Dynamic Island 布局和小工具的开源库，无需编写 Swift 代码，并支持热重载和自动配置。

- 🚀 **无需原生开发**：使用 React 组件直接创建 iOS Live Activities、Dynamic Island 布局和静态小组件，无需 Swift 或 Xcode。
- ⚡ **高效开发体验**：支持热重载（Fast Refresh），JS 和原生层均遵循 ActivityKit 的有效负载预算限制。
- 📨 **生产级推送通知**：支持收集 ActivityKit 推送令牌和推送启动令牌，流式处理生命周期更新，并实现服务器驱动的刷新。
- 🎨 **熟悉的样式编写**：可使用 React Native 样式属性和有序的 SwiftUI 修饰符。
- 🔧 **类型安全与开发友好**：提供完整的 TypeScript 定义、测试和文档，便于开发者和 AI 编码助手使用。
- ⚙️ **兼容多种项目设置**：支持 Expo Dev Client 和裸 React Native 项目，配置插件会自动设置 iOS 扩展目标。
- 📚 **详细文档与示例**：提供快速入门指南、API 参考和示例代码，帮助开发者快速上手。
- 📱 **平台限制**：该库仅适用于 iOS 设备，不支持 Expo Go。
- ❤️ **开源与社区**：由 Callstack 团队维护，采用 MIT 许可证，鼓励社区参与和贡献。

---

### [GitHub - ultroned/xray-react: 🩻 一款 React 布局调试工具，点击 UI 元素即可在本地 IDE 中打开源代码。](https://github.com/ultroned/xray-react)

**原文标题**: [GitHub - ultroned/xray-react: 🩻 React layout debugging tool that lets you open source code in your local IDE by clicking UI elements.](https://github.com/ultroned/xray-react)

X-Ray React 是一款用于调试 React UI 布局的开发工具，它通过快捷键在界面上显示组件层级覆盖层，并允许点击组件在本地编辑器中打开对应的源代码文件。

- 🩻 **React 布局调试工具**：通过快捷键（Mac: Cmd+Shift+X，Windows/Linux: Ctrl+Shift+X）在 UI 上显示组件结构覆盖层。
- 🔗 **点击打开源代码**：点击覆盖层中的任意组件，即可在本地 IDE（如 VSCode、WebStorm 等）中打开其源文件。
- ⚛️ **支持 React 18+**：利用 React DevTools 协议，同时兼容 React 18 以下版本。
- 📦 **多打包器支持**：兼容 Webpack 和 Vite，并提供 Next.js 配置指南。
- 🧩 **智能组件过滤**：自动过滤外部库组件，仅显示项目自身的组件。
- 🌳 **显示组件层级**：展示从父组件到子组件的完整路径（例如：Page -> Layout -> Component）。
- 🔧 **编辑器集成**：自动检测 VSCode、WebStorm、Cursor、Sublime 等编辑器，支持通过环境变量自定义。
- 🚀 **轻量且快速**：对性能影响极小，专为开发环境设计。
- ⚙️ **灵活配置**：支持通过插件选项或环境变量（如 `XRAY_REACT_EDITOR`、`XRAY_REACT_PROJECT_ROOT`）进行配置。
- ❓ **提供故障排除指南**：针对组件不显示、文件无法打开、连接错误等常见问题提供了解决方案。

---

### [GitHub - loffloff/gemini-live-react](https://github.com/loffloff/gemini-live-react)

**原文标题**: [GitHub - loffloff/gemini-live-react](https://github.com/loffloff/gemini-live-react)

这是一个用于 React 的实时双向语音流库，通过代理连接 Google Gemini Live API，简化了音频格式处理、缓冲管理和播放链等复杂实现。

- 🎤 **核心功能**：提供全双工音频流、屏幕共享、工具调用和实时转录，支持语音活动检测以节省带宽。
- 🚀 **快速开始**：通过 npm 安装，部署 Deno 代理到 Supabase，使用 React 钩子即可集成语音对话功能。
- 🛠️ **工具调用**：允许 AI 执行自定义函数并获取结果，适合构建智能代理应用。
- 📱 **移动支持**：包含实用工具检测 iOS 等移动设备限制，提供摄像头回退方案。
- 🐛 **调试模式**：内置日志功能，可自定义回调，便于诊断连接问题。
- 🔄 **连接管理**：具备自动重连、会话恢复和统一状态机（空闲、连接中、已连接等）。
- 🎚️ **音频处理**：自动处理 16kHz 输入、24kHz 输出的音频格式转换和 48kHz 浏览器播放。
- 🌐 **架构设计**：浏览器通过代理与 Gemini API 通信，代理保护 API 密钥，处理音频数据转发。

---

### [GitHub - hCaptcha/react-hcaptcha: 适用于 ReactJS 和 Preact 的 hCaptcha 组件库](https://github.com/hCaptcha/react-hcaptcha)

**原文标题**: [GitHub - hCaptcha/react-hcaptcha: hCaptcha Component Library for ReactJS and Preact](https://github.com/hCaptcha/react-hcaptcha)

这是一个用于 ReactJS 和 Preact 的 hCaptcha 组件库，提供了一种保护用户隐私的验证码解决方案，可作为 reCAPTCHA 的替代品。

- 🛠️ **功能概述**：该库为 ReactJS 和 Preact 应用提供 hCaptcha 组件，支持标准嵌入和编程式调用，并包含 Provider/Hook 模式。
- 📦 **安装与使用**：可通过 npm 安装，使用需提供 sitekey，并支持与 Formik 或 React Hook Form 等表单库集成。
- ⚙️ **配置选项**：提供多种 props 如 size、theme、languageOverride 等，以自定义验证码的外观和行为。
- 🔄 **事件与方法**：包含 onVerify、onError 等事件监听，以及 execute()、resetCaptcha() 等控制方法。
- 🐛 **调试与问题**：文档列出了常见问题如无效 ID、重复导入脚本等，并提供了解决方案。
- 🧪 **开发与贡献**：支持本地开发，包含测试脚本，并说明了版本发布流程。
- 📄 **许可证与资源**：采用 MIT 许可证，项目在 GitHub 上开源，拥有活跃的社区贡献者。

---

### [GitHub - software-mansion/react-native-audio-api：高性能音频引擎](https://github.com/software-mansion/react-native-audio-api)

**原文标题**: [GitHub - software-mansion/react-native-audio-api: High-performance audio engine](https://github.com/software-mansion/react-native-audio-api)

这是一个基于 Web Audio API 规范的高性能 React Native 音频引擎库，允许开发者在移动端以与浏览器相同的方式生成和修改音频。

- 🎯 **高性能音频引擎** – 为 React Native 提供基于 Web Audio API 规范的音频处理系统
- 📦 **安装与起步** – 提供详细的安装指南和入门文档
- 🗺️ **功能规划** – 包括动态压缩节点、音频标签、MIDI 支持、空间音频、降噪、文件录制等多项计划功能
- 📄 **规范覆盖** – 当前已实现的 Web Audio API 规范功能可在专门页面查看
- 🧪 **示例应用** – 提供示例项目代码，便于快速体验和测试
- 💬 **反馈渠道** – 欢迎通过提交 issue 或直接联系维护者提供反馈和建议
- 📜 **开源许可** – 采用 MIT 许可证，部分代码基于 Webkit 和 FFmpeg
- 👥 **社区支持** – 由 Software Mansion 维护，提供 Discord 社区交流渠道
- ⭐ **项目数据** – 获得 655 颗星、40 次分叉，持续活跃更新

---

### [发布 v5.0.10 · pmndrs/zustand · GitHub](https://github.com/pmndrs/zustand/releases/tag/v5.0.10)

**原文标题**: [Release v5.0.10 · pmndrs/zustand · GitHub](https://github.com/pmndrs/zustand/releases/tag/v5.0.10)

Zustand 是一个状态管理库，本次发布了 v5.0.10 版本，主要修复了持久化中间件中的一个边缘情况问题，并引入了多位新贡献者的首次代码提交。

- 🐛 修复了 `persist` 中间件在并发重载调用时可能出现的竞态条件问题
- 👥 本次版本迎来了八位新贡献者的首次代码合并
- 📝 详细更新日志可查看 v5.0.9 到 v5.0.10 的完整变更记录
- 👍 发布后获得了社区用户的正向反馈与互动

---

### [现代 JavaScript 事件日历](https://schedule-x.dev/)

**原文标题**: [Modern JavaScript Event Calendar](https://schedule-x.dev/)

Schedule-X 是一款现代化的 JavaScript 事件日历库，提供高度可定制和易于集成的解决方案，支持多种前端框架，并包含丰富的交互功能如拖放、调整事件大小和多语言支持。

- 📅 跨框架兼容：提供 React、Vue、Angular、Svelte 和 Preact 组件，适配不同技术栈
- 🎨 高度可定制：支持自定义视图、主题切换（明暗模式）及插件扩展
- ⚡ 交互功能丰富：内置事件拖放调整、缩放创建、资源调度视图等交互操作
- 🌍 国际化支持：默认提供多语言功能，满足全球化需求
- 📱 响应式设计：全面适配从桌面到移动设备的各类屏幕
- 💎 专业版增强：提供高级功能如事件重复规则、资源视图等，显著减少开发时间
- 🛠️ 开发者友好：配置简单，提供详细文档和活跃社区支持

---

### [发布 v1.1.0 · mui/base-ui · GitHub](https://github.com/mui/base-ui/releases/tag/v1.1.0)

**原文标题**: [Release v1.1.0 · mui/base-ui · GitHub](https://github.com/mui/base-ui/releases/tag/v1.1.0)

Base-UI 发布了 v1.1.0 版本，主要包含一系列错误修复、功能增强和性能改进，涉及多个组件如 Autocomplete、Combobox、Select 等，并引入了 CSPProvider 新组件。

- 🐛 **修复多项组件问题**：包括 `onOpenChangeComplete` 时机、Safari 触摸事件、样式和类型错误等。
- ✨ **新增功能与属性**：为 Autocomplete 和 Combobox 添加 `loopFocus` 等属性，引入 `CSPProvider` 组件。
- 🔧 **组件特定优化**：改进 Select 的动画支持、Combobox 的多值标签解析，并修复 Slider、Toast 等组件的已知问题。
- 📦 **工具与类型更新**：公开 `mergeProps` 工具，导出缺失的类型，提升开发体验。
- 👥 **社区贡献**：由多位贡献者共同完成，包括修复和功能添加。

---

### [GitHub - shadcn-ui/ui：一套设计精美、易于访问的组件与代码分发平台。兼容您喜爱的框架。开源。开放代码。](https://github.com/shadcn-ui/ui)

**原文标题**: [GitHub - shadcn-ui/ui: A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Open Code.](https://github.com/shadcn-ui/ui)

这是一个名为 shadcn/ui 的开源 UI 组件库和代码分发平台，提供美观、可访问的组件，可与多种流行前端框架配合使用。

- 🎨 **组件设计精美且可定制** - 提供一套设计优雅、支持自定义和扩展的 UI 组件，方便用户构建自己的组件库。
- 🔗 **框架兼容性强** - 支持与 React、Next.js 等主流前端框架协同工作。
- 📚 **文档与资源齐全** - 拥有详细的在线文档（ui.shadcn.com/docs），便于开发者查阅和使用。
- 🌍 **完全开源** - 采用 MIT 许可证，代码公开，允许自由使用、修改和分发。
- ⭐ **社区活跃度高** - 在 GitHub 上获得超过 10.5 万颗星标和 7.7k 次分叉，拥有活跃的贡献者和用户社区。
- 🛠️ **技术栈现代** - 主要使用 TypeScript 开发，并整合了 Tailwind CSS、Radix UI 等流行技术。

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

Auth0 注册页面提供免费账户，包含多项安全与开发功能，旨在简化用户认证流程并支持 AI 代理集成。

- 🔐 免费套餐支持每月高达 2.5 万活跃用户，提供可定制的注册登录流程
- 🤖 新增 AI 代理连接外部应用功能，敏感操作需经人工批准
- 🔗 支持自定义社交登录与无密码连接，内置暴力破解防护和渐进式用户画像
- 👩💻 为各阶段开发者设计，提供 5 种操作与表单工具
- 📜 注册需同意自助服务条款和隐私政策，可选择邮箱或 GitHub 等第三方账户继续

---

### [使用 Vega 进行开发 | 设计与开发 Vega 应用](https://developer.amazon.com/docs/vega/latest/vega-develop.html?sc_category=PAI&sc_channel=3P&sc_publisher=RS&sc_campaign=ACQ_VG&sc_country=US&sc_detail=RSTATUS_VG_GEN)

**原文标题**: [Develop with Vega | Design and Develop Vega Apps ](https://developer.amazon.com/docs/vega/latest/vega-develop.html?sc_category=PAI&sc_channel=3P&sc_publisher=RS&sc_campaign=ACQ_VG&sc_country=US&sc_detail=RSTATUS_VG_GEN)

Vega 开发平台为电视应用开发者提供全面的资源、工具和指南，涵盖从创建、开发、调试到测试和集成的全流程。

- 🛠️ **开发资源**：提供示例、指南和 API 参考，支持应用开发者和库创建者
- 📺 **应用构建**：支持从零创建电视应用，可使用 Vega Studio 和 VS Code 扩展提升开发效率
- ⚡ **性能优化**：强调从设计阶段关注性能，提供 UI 流畅性、内存管理和性能最佳实践指南
- 🔧 **核心开发领域**：涵盖媒体播放、焦点管理、调试、性能测试、应用配置等关键主题
- 🌐 **Web 应用与模块**：支持基于 Chromium 的 Web 应用开发，提供 Turbo 模块实现 JS 与原生代码高效通信
- 🧪 **测试与运行**：支持模拟器、Fire TV Stick 设备测试，提供虚拟设备和真实用户测试方案
- 🔌 **集成扩展**：兼容 Fire TV 核心功能（如应用内购）并支持数十个社区和自定义库

---

### [Firefox 147 开发者版本发布说明（稳定版）- Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/147)

**原文标题**: [Firefox 147 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/147)

Firefox 147 于 2026 年 1 月 13 日发布，为开发者带来多项更新，涵盖开发者工具、CSS、JavaScript、API 及 WebDriver 等方面，旨在提升开发体验和功能兼容性。

- 🛠️ **开发者工具增强**：支持在检查器中编辑伪元素选择器，视图过渡期间显示相关伪元素和动画，为锚定元素添加标识，并支持从 JSON 查看器导入性能分析数据。
- 🎨 **CSS 功能扩展**：默认启用 CSS 锚点定位，新增`anchor-center`和`position-anchor: none`值，支持视图过渡类型、`::marker`伪元素的计数器属性，以及基于根元素字体的相对长度单位。
- 📜 **JavaScript 与 API 更新**：支持 CSS 模块脚本和`Iterator.concat()`方法，新增`Document.activeViewTransition`属性，扩展 WebGPU API 至所有 macOS Apple Silicon 设备，并引入 Navigation API 和 Brotli 压缩支持。
- 🔧 **WebDriver 改进**：修复新会话响应问题，实现`input.fileDialogOpened`事件和`emulation.setScreenSettingsOverride`命令，优化导航和脚本执行行为，并更新本地化覆盖功能。
- ⚙️ **附加组件开发**：临时加载的 Manifest V3 扩展现在允许从本地主机加载脚本，提升开发灵活性。
- 📄 **SVG 与 HTML 更新**：SVG 作为图像源时支持媒体片段，包括时间维度和空间维度语法，但 HTML 方面无显著变化。
- 🧪 **实验性功能**：此版本未添加新的实验性功能，开发者可参考其他版本的实验特性页面。

---

### [CSS 锚点定位 | Can I use... HTML5、CSS3 等支持表格](https://caniuse.com/css-anchor-positioning)

**原文标题**: [CSS Anchor Positioning | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/css-anchor-positioning)

CSS Anchor Positioning 是一种 CSS 功能，允许元素相对于“锚点元素”在页面任意位置定位，不受其他元素布局影响（除了其包含块）。目前全球使用率约为 75.86%，已在多个主流浏览器的最新版本中获得支持。

- 🌐 **全球使用率**：约 75.86%，表明该功能已被广泛采用。
- 📍 **功能描述**：允许元素相对于锚点元素自由定位，不受常规文档流限制。
- ✅ **浏览器支持**：Chrome（125+）、Edge（125+）、Safari（26.0+）、Firefox（147+）等现代浏览器已支持。
- 📱 **移动端支持**：Chrome for Android、Safari on iOS 等主流移动浏览器也已实现兼容。
- 🔧 **资源参考**：提供相关博客文章、Polyfill 方案及 WebKit 官方立场等资源链接。

---

### [锚点定位  |  web.dev](https://web.dev/learn/css/anchor-positioning)

**原文标题**: [Anchor positioning  |  web.dev](https://web.dev/learn/css/anchor-positioning)

CSS 锚点定位提供了一种声明式方法，使元素能够相对于页面上的另一个元素进行定位，无需依赖 JavaScript 即可实现复杂布局。

- 🎯 **锚点命名**：通过`anchor-name`属性为元素设置锚点标识符，例如`--my-anchor`，以便其他元素引用。
- 🔗 **元素绑定**：使用`position: absolute`或`position: fixed`使定位元素脱离文档流，并通过`position-anchor`指定要绑定的锚点。
- 🧭 **定位方式**：通过`position-area`属性或`anchor()`函数设置定位区域，支持物理关键词（如`top`、`left`）和逻辑关键词（如`block-start`、`inline-end`）。
- 🧩 **作用域控制**：使用`anchor-scope`限制锚点名称的匹配范围，确保在组件复用时准确定位。
- 🛠️ **高级定位**：`anchor()`函数允许更灵活的定位，可结合`calc()`等 CSS 函数进行计算，并支持回退值处理锚点缺失情况。
- 📏 **尺寸引用**：通过`anchor-size()`函数获取锚点元素的尺寸，用于设置定位元素的大小或边距。
- 🚧 **溢出处理**：使用`position-try-fallbacks`规则定义溢出时的备用定位方案，支持自定义回退选项（如`@position-try`）。
- 🔄 **滚动行为**：定位元素默认仅跟随默认锚点滚动，可通过`position-visibility: anchors-visible`在锚点不可见时隐藏定位元素。

---

### [引言 · Node.js 包配置指南](https://nodejs.github.io/package-examples/)

**原文标题**: [Introduction · Node.js package configuration guide](https://nodejs.github.io/package-examples/)

本文档是关于如何为 Node.js 配置包的指南，涵盖了包配置的基础知识，包括文件结构、package.json 文件的使用以及 CommonJS 和 ECMAScript 模块（ESM）的处理方法。

- 📚 指南介绍：提供 Node.js 包配置的全面指导，包含文件结构、package.json 使用及模块处理
- 🔧 模块系统：涵盖 CommonJS 和 ESM 两种模块系统的配置与互操作性
- 📦 包配置基础：介绍单文件包和多文件包的配置方法
- 📄 配置文件：详细讲解 package.json 在包配置中的关键作用
- 🔄 迁移指南：提供从 CommonJS 迁移到 ESM 的完整步骤和注意事项
- 💻 代码示例：所有主题均配有实际代码示例，可在项目仓库中查看完整实现

---

### [用于自动化与测试的 Chrome Headless 屏幕配置  | 博客  | Chrome 开发者](https://developer.chrome.com/blog/screen-configuration-with-chrome-headless)

**原文标题**: [Screen configuration for automation and testing with Chrome Headless  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/screen-configuration-with-chrome-headless)

Chrome Headless 模式和无头 Shell 现已支持完全可配置的虚拟无头屏幕，独立于物理显示器，可通过命令行参数 `--screen-info` 初始设置屏幕属性，并支持在运行时通过 Chrome DevTools Protocol 动态添加或移除屏幕。这些功能已集成到 Puppeteer 中，便于自动化测试复杂的多屏场景。

- 🖥️ Chrome Headless 和无头 Shell 现在使用可配置的虚拟无头屏幕，独立于物理显示器。
- ⚙️ 通过 `--screen-info` 命令行参数可设置屏幕的尺寸、缩放、方向和工作区域等属性。
- 🔄 运行时可通过 CDP 命令动态添加或移除虚拟屏幕，模拟显示器连接/断开。
- 🤖 Puppeteer 全面支持这些新功能，便于自动化测试多屏、高分辨率及全屏应用。
- 📏 静态屏幕配置可用于测试全屏模式、多屏窗口跨越及高 DPI 显示适配。
- 🖼️ 示例展示了如何配置双屏环境及动态调整窗口位置和状态。
- 🚀 该功能从 Chrome 142 稳定版开始提供，更多示例和问题反馈可在 pptr.dev 和 GitHub 上获取。

---

### [获取失败](https://react.statuscode.com/link/179437/web)

**原文标题**: [Failed to retrieve](https://react.statuscode.com/link/179437/web)

无法总结：获取内容失败，状态码 403。

---

### [GitHub - gibbok/typescript-book: 《简明 TypeScript 指南》：TypeScript 高效开发的简明指南。免费开源。](https://github.com/gibbok/typescript-book)

**原文标题**: [GitHub - gibbok/typescript-book: The Concise TypeScript Book: A Concise Guide to Effective Development in TypeScript. Free and Open Source.](https://github.com/gibbok/typescript-book)

《简明 TypeScript 手册》是一本免费开源的 TypeScript 指南，旨在提供高效开发 TypeScript 所需的关键知识和实用技能。本书涵盖了 TypeScript 5.2 的所有核心概念，从基础类型系统到高级特性，适合初学者和有经验的开发者，帮助编写清晰、健壮的代码。

- 📚 **免费开源**：本书完全免费开放，致力于让高质量技术教育普及化。
- 🌐 **多语言支持**：提供中文、意大利文等多种语言版本，方便全球开发者学习。
- 📖 **内容全面**：涵盖 TypeScript 类型系统、配置、类、泛型、装饰器等所有关键主题。
- 🛠️ **实用指南**：包含安装、配置、迁移建议及现代 JavaScript 特性（如 ES6/ES7）的详细说明。
- 🔍 **类型系统深入**：详细解释结构类型、类型推断、类型收窄、条件类型等高级概念。
- ⚙️ **工具与集成**：介绍 TypeScript 语言服务、编译器配置及与常见工具（如 VS Code、Babel）的集成。
- 🚀 **现代特性**：涵盖可选链、空值合并、模板字面量类型、递归类型等最新语言特性。
- 📦 **模块与异步**：支持 ES6 模块、动态导入、异步迭代及 Promise/async-await 等异步编程模式。
- 🧩 **高级主题**：包括混合类、错误处理、JSX 支持、泛型约束及类型操作（如映射类型、实用工具类型）。
- 🔄 **资源管理**：引入 `using` 声明和显式资源管理，帮助自动处理资源清理。
- 📄 **类型声明**：支持环境声明、类型导入/导出及 JSDoc 注释，便于与现有 JavaScript 代码协作。

---

### [错误](https://react.statuscode.com/link/179440/web)

**原文标题**: [Error](https://react.statuscode.com/link/179440/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='react.statuscode.com', port=443): Max retries exceeded with url: /link/179440/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

