### [React 服务端组件的组件架构 | Aurora Scharff](https://aurorascharff.no/posts/component-architecture-for-react-server-components/)

**原文标题**: [Component Architecture for React Server Components | Aurora Scharff](https://aurorascharff.no/posts/component-architecture-for-react-server-components/)

## 概述总结

本文探讨了 React Server Components 如何改变数据获取架构，从传统的客户端获取模式演进到服务器端组件自取数据，从而实现更好的组件组合性和加载体验设计。

- 🚀 **服务器端数据获取更高效**：服务器靠近数据库，可在渲染时并行获取数据，无需等待 JavaScript 下载执行，减少网络往返
- 🔄 **从 useEffect 到 React Query 的演进**：解决了状态提升和属性钻取问题，但仍有"爆米花 UI"和客户端等待的缺点
- 📦 **路由级加载器的局限性**：虽然将数据获取移至服务器，但导致组件与特定路由的数据形状耦合，难以复用
- 🧩 **RSC 的核心优势**：每个组件可自行在服务器端获取数据，只需最小属性（如 ID），实现真正的自包含和可复用性
- ⏳ **Suspense 边界设计加载体验**：页面决定用户等待的位置，可分组流式加载，避免布局偏移
- 📐 **骨架屏与组件同文件**：保持加载状态与实际渲染状态同步，减少布局抖动
- 🔧 **页面作为同步组合器**：页面不负责获取数据，只负责组合组件和放置 Suspense 边界
- 🎯 **代码组织按功能分组**：自包含组件自然形成功能文件夹结构，便于复用和维护
- 🛠 **交互性通过客户端组件实现**：使用 Server Functions 和 useOptimistic 实现即时反馈，保持服务器端数据获取优势
- 🏗 **为 Partial Prerendering 做好准备**：组件自取数据 + 明确 Suspense 边界的架构，天然适配 Next.js 16 的缓存组件模式

---

### [我测试了 Next.js Dev MCP（你无需亲自尝试）- YouTube](https://www.youtube.com/watch?v=OODK3KGUjDA)

**原文标题**: [I Tested Next.js Dev MCP (So You Don't Have To) - YouTube](https://www.youtube.com/watch?v=OODK3KGUjDA)

本頁面列出了 YouTube 平台的核心資訊與政策，涵蓋版權、聯絡方式、創作者支援及法律條款等面向。
- 📰 提供新聞中心，發布平台最新動態與公告
- ©️ 說明版權相關政策，保障內容創作者權益
- 📞 提供聯絡我們方式，供用戶回饋與查詢
- 🎬 為創作者提供資源與支援，協助內容產出
- 📢 說明廣告刊登選項，供品牌與企業合作
- 📜 列出使用條款，規範用戶行為與責任
- 🔒 強調私隱政策，保護用戶個人資料
- 🛡️ 說明政策及安全措施，維護平台環境
- ⚙️ 解釋 YouTube 的運作方式，包括演算法與推薦
- 🧪 測試新功能，持續優化用戶體驗
- ©️ 標示版權所有 © 2026 Google LLC

---

### [GitHub - Blazity/next-migration-skills · GitHub](https://github.com/Blazity/next-migration-skills)

**原文标题**: [GitHub - Blazity/next-migration-skills · GitHub](https://github.com/Blazity/next-migration-skills)

Blazity 的 next-migration-skills 是一个基于代理的工具包，用于将 Next.js 从 Pages Router 迁移到 App Router，专为 Skills.sh 构建。

- 🛠️ **核心工具**：`nextjs-migration-toolkit` 是依赖技能，提供 AST 分析和转换功能（基于 ts-morph）。
- 📊 **评估技能**：`migration-assessment` 分析代码库复杂度和迁移就绪状态。
- 📋 **规划技能**：`migration-planning` 创建分阶段迁移计划。
- 🔗 **依赖映射**：`dependency-mapping` 将旧依赖映射到 App Router 等效项。
- 🛣️ **路由转换**：`route-conversion` 将 `pages/` 路由转换为 `app/` 路由。
- 🧩 **组件迁移**：`component-migration` 迁移组件以兼容 RSC（React 服务器组件）。
- 📡 **数据层迁移**：`data-layer-migration` 迁移数据获取和 API 路由。
- ✅ **验证测试**：`validation-testing` 验证每个阶段后的正确性。
- 📂 **架构清晰**：技能目录结构包含 AST 分析器、转换器、模板和测试，支持 TypeScript 和 Handlebars。

---

### [文档：通过 aurorascharff 添加交互式应用指南 · 拉取请求 #94020 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/94020/files)

**原文标题**: [docs: add Interactive Apps guide by aurorascharff · Pull Request #94020 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/94020/files)

该 Pull Request 为 Next.js 文档新增了“交互式应用指南”。

- 📖 新增了一份完整的“交互式应用指南”文档，包含 18 次提交的逐步完善。
- 🧩 指南内容涵盖 Suspense、切换、过滤等交互模式，并假设使用缓存组件。
- 🔧 修复了文档链接错误、调整了内容顺序，并移除了未使用的导入。
- 📝 更新了数据库示例，并采用了更规范的指南语言。
- ⚠️ 澄清了异步上下文的限制，并添加了指向现有文档的链接。
- 🔀 最终合并到主分支（canary），共修改了 1 个 .mdx 文件，新增 734 行代码。

---

### [acdlite 在客户端预取应用外壳 · 拉取请求 #93999 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/93999)

**原文标题**: [Prefetch App Shells on the client by acdlite · Pull Request #93999 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/93999)

此 PR 在 Next.js 客户端实现了 App Shell 预取机制，确保用户导航时能立即渲染路由外壳，无需等待具体参数的预取完成。

- 🚀 **核心目标**：实现“点击即渲染”的导航体验，即使目标路由的具体预取尚未完成，也能立即显示路由的 App Shell，消除阻塞导航。
- 🧩 **关键机制**：引入新的 `Shell` 预取阶段，为每个路由（而非每个链接）发起一次外壳请求。同一路由下多个链接共享同一个外壳请求，大幅减少网络请求量。
- 🗂️ **缓存优化**：导航时采用“两遍查找”策略，优先使用任何已完成的条目（包括较不具体的外壳），而非阻塞于正在进行的更具体预取请求。
- 🎯 **适用范围**：当前仅针对运行时（PPRRuntime）预取路径。静态（PPR）路径将采用不同的策略（将单个响应拆分为外壳前缀和具体后缀），将在后续 PR 中实现。
- ⚙️ **配置开关**：该功能通过 `experimental.appShells` 标志控制。

---

### [飞行协议让你的拒绝服务攻击成了我的问题 | 萨沙·贝克尔](https://saschb2b.com/blog/flight-protocol-dos)

**原文标题**: [The Flight Protocol Made Your DoS My Problem | Sascha Becker](https://saschb2b.com/blog/flight-protocol-dos)

2026 年 5 月 6 日，React 和 Next.js 修复了 12 个漏洞，其中 CVE-2026-23870 是一个严重拒绝服务漏洞，通过单个 HTTP 请求即可耗尽 Node 进程 CPU。问题本质在于框架边界一直是网络边界，但开发者未将其视为威胁模型。

- 🔒 **Flight 协议本质**：React Server Components 依赖 Flight 协议序列化组件树并流式传输到客户端，这是一个自定义的换行分隔协议，支持引用和去重，但解析器缺乏严格验证。
- ⚠️ **漏洞核心**：CVE-2026-23870 影响多个 react-server-dom-*包，解析器接受畸形 Flight 负载（如结构错误、标签不匹配、引用嵌套过深），导致 CPU 耗尽，无需认证即可利用。
- 🛡️ **修复与影响范围**：已修复版本 19.0.6、19.1.7、19.2.6，覆盖 Next.js App Router 13.x 至 16.x。所有使用 Server Actions 或 RSC 缓存的 App Router 应用均受影响，即使未直接使用 Server Actions。
- 📋 **自查步骤**：检查 react-server-dom-*版本是否低于修复版本，运行包管理器审计确认 CVE，升级 Next.js 或直接依赖的 react-server-dom-*包。
- 🧠 **框架边界误解**：Server Components 被宣传为渲染优化，但运行时边界是序列化边界。每个 Server Action 都是未经验证的 RPC 端点，'use server'指令实为 HTTP 处理程序。
- 🔍 **为何被忽视**：协议早期未文档化、错误表面在调用点不可见、框架默认将解析视为性能而非安全。三者叠加使漏洞看似不可避免。
- 🛠️ **行动建议**：1) 将 Server Actions 视为 RPC 端点，添加显式参数验证（如 Zod）。2) 在反向代理处设置请求体大小限制。3) 保持 WAF 规则更新。4) 不信任缓存 RSC 负载。5) 阅读 Flight 协议以理解威胁模型。
- 🔄 **模式总结**：框架魔法常隐式创建新协议边界，如 tRPC、GraphQL、WebSocket。当框架溶解网络边界为开发便利时，威胁模型仍需事后分析。函数若可从互联网访问，即为端点，解析器不会争论。

---

### [如何使用 Antigravity 与多智能体编排实现现代化自动化 | 作者：James O'Reilly | 2026 年 5 月 | JavaScript 简明教程](https://javascript.plainenglish.io/migrating-express-to-next-js-using-ai-agents-antigravity-f48b4c206a8e?gi=af17d6f2d533)

**原文标题**: [How to automate modernization with Antigravity and multi-agent orchestration | by James O'Reilly | May, 2026 | JavaScript in Plain English](https://javascript.plainenglish.io/migrating-express-to-next-js-using-ai-agents-antigravity-f48b4c206a8e?gi=af17d6f2d533)

### 概述总结
本文详细介绍了如何使用 Google Antigravity 和多智能体编排来自动化现代化改造遗留的 Express 单体应用，将其迁移到现代的 Next.js 架构。

- 🔄 **核心挑战**：现代化改造遗留的 Express/Mongoose 单体应用，解决技术债务问题
- 🏗️ **目标架构**：从 Express 单体迁移到 Next.js App Router，使用 TypeScript、Zod 验证、ShadCN UI 和 Auth.js
- 🤖 **Antigravity 平台**：基于 VS Code 的智能体优先开发平台，可并行编排多个自主 AI 智能体
- ⚖️ **任务分类**：区分确定性任务（如 npm install）和启发式任务（如重构回调），优化 AI 工作流
- 📋 **技能包设计**：遵循简洁性和渐进式披露原则，使用 YAML 元数据和编号清单引导智能体执行
- 🧩 **智能体设计模式**：路由器模式（任务分类）、计划与执行（硬编码清单）、反思循环（自我修正）
- 🔍 **五阶段工作流**：审计逆向工程、基础与 TDD、数据脚手架、UI 脚手架、验证与对抗审计
- 🛠️ **子智能体角色**：包括 API 合同审计、业务逻辑审计、数据模型审计、UI 考古等专用智能体
- ✅ **验证机制**：使用 Vitest 测试套件和对抗性验证，确保功能一致性和安全性
- ⏱️ **效率提升**：将数周的手动重构工作缩短到几分钟，通过严格架构护栏保证代码质量

---

### [GitHub - millionco/react-doctor: 你的代理编写糟糕的 React 代码。这个工具能捕捉到它 · GitHub](https://github.com/millionco/react-doctor)

**原文标题**: [GitHub - millionco/react-doctor: Your agent writes bad React. This catches it · GitHub](https://github.com/millionco/react-doctor)

React Doctor 是一个用于扫描 React 代码库、发现状态与副作用、性能、架构、安全性和可访问性问题的工具。

- 🔍 确定性扫描：能自动检测 React 代码中的各类问题，覆盖状态管理、性能、安全等多个方面
- 🚀 快速安装：通过 `npx react-doctor@latest` 即可在项目根目录运行审计
- 🤖 智能代理集成：支持 Claude Code、Cursor、Codex 等编码代理，安装技能后可自动修复问题
- 🔄 CI/CD 集成：提供 GitHub Actions，可在每次 Pull Request 中自动扫描并显示内联注释
- 🌐 框架兼容：适用于 Next.js、Vite、TanStack、React Native、Expo 等所有 React 框架
- 📊 开源社区：拥有 11.4k Star、369 Fork，采用 MIT 许可证，社区活跃

---

### [GitHub - SukkaW/sekisho: 任何 React 应用的身份验证与访问控制 · GitHub](https://github.com/SukkaW/sekisho)

**原文标题**: [GitHub - SukkaW/sekisho: Authentication and Access Control for any React app · GitHub](https://github.com/SukkaW/sekisho)

⛩️ sekisho 是一个为 React 应用提供身份验证和访问控制的开源库，基于 React 错误边界机制实现，支持 Next.js、React Router 等框架。

- 🔐 使用 `NotAuthenticatedContainer` 和 `needLogin()` 处理未认证用户的登录重定向，类似 `<Suspense />` 但用于登录控制
- 🚫 使用 `AccessRestrictedContainer` 和 `accessRestricted()` 限制部分 UI 的访问权限，仅渲染后备内容而非全局重定向
- 🔧 支持 Next.js App Router 和 React Router，需配合 `NotAuthenticatedErrorWrapper` 处理框架错误边界
- 🛠️ 提供 `createSekisho` 工厂函数，可自定义守卫（如新用户引导流程），返回 5 元组：抛出函数、容器组件、错误包装器、类型守卫和错误类
- 🧩 每个守卫独立嵌套，互不干扰，不影响自定义错误边界
- 📦 基于 React 错误边界，`needLogin()` 和 `accessRestricted()` 在渲染阶段抛出特殊错误，由最近边界捕获
- 📘 包含完整示例（example-nextjs-app）和在线演示（sekisho-demo.pages.dev）
- 📜 使用 TypeScript 编写（80.4%），MIT 许可证，由 Sukka 维护

---

### [GitHub - bklit/bklit-ui: 开源 UI 与图表库 · GitHub](https://github.com/bklit/bklit-ui)

**原文标题**: [GitHub - bklit/bklit-ui: Open-source UI & Charts library · GitHub](https://github.com/bklit/bklit-ui)

Bklit UI 是一个开源图表和工具组件库，支持自定义和扩展，基于 shadcn 注册表构建，提供多种图表类型和交互式 Studio 工具。

- 📊 提供多种图表组件：面积图、柱状图、K 线图、地图、组合图、漏斗图、仪表盘、折线图、实时折线图、饼图、雷达图、环形图、散点图、桑基图等
- 🎨 Studio 交互式工具：实时调整图表样式和动画，生成 React 代码或导出 registry JSON
- 🚀 基于 shadcn 注册表：通过 `npx shadcn@latest add @bklit/line-chart` 快速安装
- 💻 技术栈：React、TypeScript、Motion、数据可视化，支持 shadcn 生态
- 🔒 开源许可：MIT 许可证，社区活跃（751 星标、50 分支）
- 🏆 赞助商支持：由 OpenPanel 等赞助，注重隐私的开放分析平台

---

### [聊天 SDK 社区代理 - Vercel](https://vercel.com/templates/next.js/chat-sdk-community-agent)

**原文标题**: [Chat SDK Community Agent - Vercel](https://vercel.com/templates/next.js/chat-sdk-community-agent)

这是一个开源 AI 驱动的 Slack 社区管理机器人模板，内置 Next.js 管理面板，基于 Chat SDK、AI SDK 和 Vercel Workflow 构建。

- 🤖 **AI 社区经理** — 自动路由问题、欢迎新成员、标记未回复线程并上报问题，由 AI SDK 驱动
- 🗺️ **频道感知路由** — 可配置的频道映射，让机器人了解工作区布局并正确引导用户
- ⚡ **持久化工作流** — 每次 LLM 调用和工具执行都有检查点和自动重试，基于 Vercel Workflow
- 🌐 **网络搜索** — 支持 Anthropic 原生网络搜索工具，可限定搜索域，通过 AI Gateway 运行
- 🖥️ **沙箱执行** — 可选 bash/bash_batch 工具，用于在沙箱环境中运行命令
- 💬 **原生 Slack UI** — 支持打字指示器、线程回复和私信，由 Chat SDK 驱动
- 📊 **管理面板** — 实时仪表盘，包含流式指示器、ViewTransition 动画、活动源、类型筛选、文本搜索、内联对话预览和活动趋势
- 🔐 **认证** — 通过 Better Auth 实现 Slack OAuth，限制管理面板仅供工作区成员使用
- 🚀 **快速启动** — 支持演示模式，无需设置 Slack 即可体验管理面板
- 🛠️ **高度可定制** — 可修改机器人个性、频道映射、欢迎消息、工具集和认证配置
- 📚 **知识库集成** — 可与 Knowledge Agent Template 配合，提供 bash 和 bash_batch 工具进行远程文档搜索
- 📝 **完整文档** — 包含设置指南、架构说明、管理面板文档和测试指南
- 🧩 **技术栈** — Next.js 16、Chat SDK、AI SDK 6、Vercel Workflow、Better Auth、shadcn/ui、Upstash Redis
- 📄 **MIT 许可** — 开源，可自由使用和修改

---

### [几分钟内为你的 AI-SDK 代理添加技能 | Bluebag 博客](https://www.bluebag.ai/blog/add-skills-to-your-ai-sdk-agent-in-minutes)

**原文标题**: [Add Skills to Your AI-SDK Agent in Minutes | Bluebag Blog](https://www.bluebag.ai/blog/add-skills-to-your-ai-sdk-agent-in-minutes)

### 概述总结
Bluebag 通过两行集成代码，为 Vercel AI SDK 构建的 AI Agent 提供即用型技能（Skills），无需管理基础设施（沙箱、虚拟机、依赖、文件存储等），实现从“演示代理”到“生产代理”的跨越。

- 🧩 **核心问题**：AI Agent 需要执行实际任务（如处理 PDF、运行脚本），但开发者常陷入构建沙箱、依赖管理、文件存储等基础设施的困境，偏离核心产品价值。
- ⚡ **解决方案**：Bluebag 提供两行集成（`bluebag.enhance()`），让 Agent 即时获得 PDF 处理、数据分析、图像生成等预封装技能，无需管理 Kubernetes 或 Docker。
- 📚 **渐进式技能加载**：采用三级系统节省 Token：元数据索引（轻量级描述）→ 按需读取完整文档（`SKILL.md`）→ 实际执行脚本，避免上下文浪费。
- 🖥️ **无管理运行时 VM**：自动配置依赖、跨消息持久化（30 分钟 TTL 自动刷新）、空闲自动终止，从代码角度看执行“即开即用”。
- 🛠️ **五大工具**：通过 `bluebag.enhance()` 获得 `bash`、`代码执行`、`文本编辑器`、`GUI 自动化`、`文件下载链接` 等工具，支持错误处理和流式集成。
- 🔗 **文件下载简化**：Agent 通过单一工具生成带签名的下载链接（如 `bluebag_file_download_url`），无需自行处理存储、安全与过期管理。
- 🏢 **多租户隔离**：通过 `stableId` 自动隔离用户沙箱、文件和会话状态，确保数据安全。
- 🎯 **可预测性**：技能提供经过测试的脚本和清晰文档，使 Agent 输出更一致、易调试，避免自由代码执行带来的不确定性。
- 🚀 **快速上手**：安装 `@bluebag/ai-sdk` 后，两行代码即可在 Next.js API 路由、Express 或 Serverless 环境中启用技能，专注提示词与业务逻辑。

---

### [Linear 为何如此快速？技术解析](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

**原文标题**: [How's Linear so fast? A technical breakdown](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

### 概述总结
Linear 通过将数据库置于浏览器、优化首次加载、同步引擎、设计速度和动画等综合手段，实现了极致的应用速度，其核心理念是尽可能消除网络请求对用户体验的影响。

- 🚀 **浏览器即数据库**：Linear 将 IndexedDB 作为本地数据库，UI 直接读取本地数据，变更先本地应用再异步同步到服务器，彻底消除网络等待。
- ⚡ **首次加载瞬间完成**：通过极致代码拆分（21MB 拆成数百块）、模块预加载、Service Worker 预缓存、内联关键 CSS/JS，以及“先渲染后认证”策略，让应用在用户感知前就绪。
- 🔄 **同步引擎三支柱**：数据已存在于本地（从 IndexedDB 水合）、变更不等待网络（乐观更新）、细粒度响应式更新（每个属性独立 MobX 可观察对象，只重绘受影响组件）。
- ⌨️ **设计即速度**：键盘快捷键优先，全局命令面板（⌘K）搜索本地内存数据，所有操作路径极短，减少用户操作步骤。
- 🎨 **动画克制且高效**：仅对 `transform`、`opacity` 等 GPU 合成属性动画，避免布局触发属性（如 `margin`），动画时长极短（默认 0.1-0.25 秒），且出入动画不对称（出现快、消失慢）。
- 🧩 **简单技术栈**：使用 React + MobX + TypeScript + Postgres 等基础技术，无边缘数据库或服务器组件，坚持客户端渲染以简化架构。
- 📦 **构建管道持续优化**：从 Parcel 到 Rolldown 四次重写构建流程，减少 50% 代码量，冷缓存加载速度提升 10-30%，内存使用降低 70-80%。
- 🔐 **认证乐观化**：假设用户已登录，直接渲染本地数据，若后续请求 401 再重定向到登录页，避免首次加载时的认证等待。

---

### [我对 AI 的思考，第二部分：智能体设置、工作流程与工具 · Mark 的开发博客](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/)

**原文标题**: [
     My Thoughts on AI, Part 2: Agent Setup, Workflow, and Tools ·  Mark's Dev Blog
  ](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/)

本文详细介绍了作者个人在 AI 辅助开发中的代理设置、工作流程及工具配置，强调以开发者为主导、保持心智参与和确定性自动化。

- 🤖 **代理选择**：作者选用 OpenCode 作为开发代理，并通过第三方 Web UI CodeNomad 进行交互，避免使用 TUI，支持多标签页和便捷复制粘贴。
- 🧠 **模型偏好**：主要使用 Anthropic 的 Opus 4.5/4.6模型，通过API调用，认为其效果足够好，不追求频繁切换模型以微调性能。
- 🛠️ **开发环境**：使用 VS Code 作为文件查看器和差异比较工具，Fork 作为 Git GUI 客户端，但实际开发主要在 CodeNomad 的 Web UI 中完成。
- 📋 **核心工作流**：采用“父协调器 + 子任务”模式，父会话管理整体项目上下文，子任务负责具体开发、研究或编码，作者全程主导并审核。
- 🔒 **权限管理**：通过自定义 OpenCode 插件实现命令的确定性自动批准或阻止，避免频繁弹窗，同时保留对危险命令的拦截。
- 📂 **文件读取优化**：使用 cachebro 缓存文件读取，结合 grepika 和 tilth 等 MCP 工具进行代码结构查询，大幅减少上下文膨胀。
- 🧩 **上下文管理**：利用 OpenCode 动态上下文修剪插件，允许代理在会话中主动压缩早期内容，避免接近上下文限制时的全量压缩。
- 📁 **个人开发计划仓库**：建立独立的 dev-plans 仓库，存储架构文档、功能计划、进度更新等，避免污染共享代码库的 Git 历史。
- ⚙️ **自动化脚本**：通过 devplans.ts 脚本自动化进度记录、子任务交接、文档创建等重复性工作，减少代理的上下文负担。
- 📝 **AGENTS.md 指令**：包含约 250 行的代理行为指南，涵盖交互模式、编码规范、代码导航、任务管理及工作流规则，持续优化中。
- 🔄 **持续改进**：定期根据使用痛点调整配置，如重写 AGENTS.md、尝试新工具，但保持“先工作后优化”的平衡。
- 🚀 **未来方向**：计划改进长期记忆与上下文索引，自动扫描会话提取模式，并增强代码审查工具 diffloupe 的功能。

---

### [React 测试库教程（使用 Jest 和 Vitest）- Robin Wieruch](https://www.robinwieruch.de/react-testing-library/)

**原文标题**: [React Testing Library Tutorial (with Jest & Vitest) - Robin Wieruch](https://www.robinwieruch.de/react-testing-library/)

本教程全面介绍了如何使用 React Testing Library（RTL）配合 Jest 或 Vitest 测试 React 组件，强调以用户行为为中心而非实现细节。内容涵盖组件渲染、元素查询、用户交互模拟、异步测试及回调处理，并提供了丰富的代码示例。

- 📚 **核心概念**：React Testing Library 是测试 React 组件的首选库，它鼓励测试用户可见的行为（如渲染输出、按钮点击、文本阅读），而非组件内部实现。
- 🧪 **测试框架**：Jest 和 Vitest 作为测试运行器，提供测试套件（describe）、测试用例（it/test）和断言（expect）。Vitest 是 Vite 项目的推荐选择。
- 🔍 **组件渲染**：使用`render`函数渲染组件，并通过`screen.debug()`查看 HTML 输出，确保测试环境正确。
- 🎯 **元素选择**：通过`getByText`、`getByRole`等搜索类型选择元素。推荐优先使用`getByRole`（利用隐式角色）和`getByText`，并支持正则表达式匹配。
- ⚖️ **搜索变体**：`getBy`（元素存在时使用）、`queryBy`（断言元素不存在时使用）、`findBy`（等待异步元素出现时使用）。对于多个元素，使用`getAllBy`、`queryAllBy`、`findAllBy`。
- ✅ **断言函数**：RTL 扩展了 Jest/Vitest 的断言，如`toBeInTheDocument`、`toBeDisabled`等，用于检查元素状态。
- 🖱️ **用户交互**：使用`fireEvent`或更推荐的`userEvent`模拟用户操作（如输入、点击）。`userEvent`更贴近真实浏览器行为（触发更多事件）。
- ⏳ **异步测试**：通过`findBy`或`waitFor`处理异步操作（如数据获取）。使用`vi.mock`（Vitest）或`jest.mock`（Jest）模拟外部 API，测试成功和失败场景。
- 🔄 **回调测试**：使用`vi.fn()`（Vitest）或`jest.fn()`（Jest）模拟回调函数，验证其被调用的次数和参数。
- 🌟 **最佳实践**：优先进行集成测试而非单元测试，以验证状态变化和副作用。推荐使用`userEvent`替代`fireEvent`，并利用`getByRole`提高可访问性测试。

---

### [Prisma Next 早期访问：编写合约，提示智能体，发布应用](https://www.prisma.io/blog/prisma-next-early-access-write-your-contract-prompt-your-agent-ship-your-app)

**原文标题**: [Prisma Next Early Access: Write Your Contract, Prompt Your Agent, Ship Your App](https://www.prisma.io/blog/prisma-next-early-access-write-your-contract-prompt-your-agent-ship-your-app)

Prisma Next 赋予你超能力，让你可以安全地将任务委托给 AI 代理，专注于应用开发。它通过定义数据层契约，自动处理数据库迁移、类型检查查询和错误报告，同时支持 Postgres 和 MongoDB 的早期访问。

- 🚀 **一键启动**：通过`npm create prisma@next`命令，无需学习曲线即可搭建项目，AI 代理即时成为专家。
- 📜 **契约即核心**：使用 Prisma 模型文件定义数据层契约，自动处理迁移、类型检查和查询，确保数据库与应用一致。
- 🔄 **快速迭代**：AI 代理通过类型安全查询和紧密反馈循环，快速实现功能，如添加数据表或编写查询。
- 🛡️ **安全迁移**：框架自动生成可审查的 TypeScript 迁移文件，支持事务回滚，确保数据安全，无需手动编写 SQL。
- 🌿 **无冲突协作**：类似 Git 的迁移历史管理，支持并行分支合并，AI 代理自动处理迁移冲突，无需人工干预。
- ⬆️ **轻松升级**：通过简单指令让 AI 代理自动完成版本升级，包括代码修改和类型检查。
- 💬 **即时反馈**：AI 代理可收集用户反馈并自动提交结构化报告，帮助改进框架。
- 🎯 **聚焦应用**：开发者可随时切换手动或代理模式，通过自然语言指令构建应用，如“创建图书追踪应用”。

---

