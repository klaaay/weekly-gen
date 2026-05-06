### [JavaScript 周刊第 784 期：2026 年 5 月 5 日](https://javascriptweekly.com/issues/784)

**原文标题**: [JavaScript Weekly Issue 784: May 5, 2026](https://javascriptweekly.com/issues/784)

以下是您提供的JavaScript Weekly第784期内容的摘要概述和要点列表：

本期JavaScript Weekly涵盖了Remix 3转向非React框架、Node.js 26.0.0发布、Bun从Zig移植到Rust的讨论、以及多个新工具和库的更新。

- 🚀 Remix 3进入测试版，不再是一个React框架，转向全栈、Web标准优先的UI组件模型。
- 🆕 Node.js 26.0.0（当前版）发布，默认启用Temporal API，包含V8 14.6和Undici 8。
- 🔄 Vitest被提议成为“框架无关”，以支持其他构建工具和运行时。
- 🦀 Bun的Jarred Sumner尝试将Bun从Zig移植到Rust，但短期内无意完全切换。
- 📦 PM2 7.0发布，重构减少依赖，扩展集群模式到Bun应用。
- 🧪 Deno获得实验性import defer支持，可能成为首个支持该特性的运行时。
- 📖 文章《测试Vue组件在浏览器中》展示了无需额外工具的运行集成测试方法。
- 🔒 Mozilla推出WAICT规范，用于加密验证JavaScript的完整性。
- 🎨 Anime.js 4.4发布，新增scrambleText效果和自动网格布局模式。
- 📝 Formisch：一个模块化、类型安全的表单库，支持多个框架。
- 🖋️ opentype.js 1.3.5发布，支持读写OpenType字体，可创建自定义字体。
- 🎬 Mediabunny v1.42.0增加HTTP直播流（HLS）读写支持。
- 🛠️ 其他工具更新：pnpm v11.0.5、Electrobun 1.18、useHotkeys 5.3、RxDB 17.2.0。
- 📰 分类广告：Command Code编码代理、Meticulous测试工具、Clerk CLI、Handsontable主题构建器。
- 🌐 生态圈动态：Crashcat 3D物理库、Cloudflare开源Agentic Inbox邮件应用、Ladybird浏览器更新、Vercel Portless本地开发工具、Thales TypeScript到Lean编译器。

---

### [Remix 3 测试版预览 | Remix](https://remix.run/blog/remix-3-beta-preview)

**原文标题**: [Remix 3 Beta Preview | Remix](https://remix.run/blog/remix-3-beta-preview)

Remix 3 测试版预览发布，这是一个更简单、更快速、更贴近Web本身的完整框架。

- 🚀 Remix 3 测试版发布，但尚未准备好用于生产环境，欢迎开发者试用并提供反馈
- 🧩 采用全栈方法，涵盖路由、请求处理、中间件、会话、认证、表单、上传等所有环节
- 📦 由可独立使用的小型可组合包构建，但安装后即可直接开始构建应用
- 🌐 路由基于Fetch API，控制器返回响应，中间件管理请求生命周期，表单提交到URL
- 🖼️ 引入“帧”概念，支持服务器渲染的UI独立加载、导航和刷新
- 📝 组件代码采用过程式风格，状态和异步行为直观可见
- 🎨 采用“去捆绑”方法，运行时是事实来源，不依赖大型预分析步骤
- 🤖 清晰的框架结构对AI代理更友好，提供稳定的构建块
- 🔧 减少对外部依赖的依赖，内置路由、会话、认证、表单、上传等核心功能
- 🎯 默认体验应保持一致，框架在让你做决策之前先提供杠杆作用
- 🧪 可通过 `npx remix@next new my-remix-app` 开始体验
- 💬 鼓励用户提供反馈，团队将每周发布新功能和更新

---

### [Remix 与 Next.js 对比 - Bejamas](https://bejamas.com/hub/guides/remix-vs-nextjs)

**原文标题**: [Remix vs Next.js - Bejamas](https://bejamas.com/hub/guides/remix-vs-nextjs)

本文章比较了 Remix 与 Next.js 两个 React 服务端渲染框架的差异，涵盖渲染策略、数据加载、路由、样式、部署等方面，帮助开发者根据项目需求做出选择。

- 📚 **框架诞生背景**：为了解决传统客户端渲染（CSR）导致的 SEO 差、首屏加载慢和缓存问题，Next.js 和 Remix 应运而生，专注于服务端渲染（SSR）。
- 🎯 **渲染策略分歧**：Next.js 提供 SSR、SSG（静态生成）和 ISR（增量静态再生）三种策略，灵活性强；Remix 则只押注 SSR，认为 SSG/ISR 在动态数据场景下不实用，并建议用 CDN 缓存或边缘计算替代。
- ⚡ **开发体验差异**：Next.js 默认支持 React Fast Refresh（热模块替换），开发时即时反馈；Remix 默认不支持热模块替换，但支持 Live Reload，且构建速度极快。
- 🧩 **路由系统对比**：两者均采用文件系统路由，但 Remix 基于 React Router，支持强大的嵌套路由（通过 `<Outlet>` 组件），能实现类似 SPA 的局部更新；Next.js 嵌套路由实现较复杂。
- 📡 **数据加载机制**：Next.js 通过 `getServerSideProps`、`getStaticProps` 等函数按策略加载数据；Remix 则使用 `loader` 函数 + `useLoaderData` 钩子，所有数据在服务端并行加载。
- 📝 **表单与数据变更**：Next.js 无内置表单处理方案，需开发者手动管理状态、提交和错误；Remix 则拥抱原生 HTML 表单，通过 `action` 函数在服务端处理数据变更，支持渐进增强。
- 🎨 **样式方案**：Next.js 内置支持 styled-jsx、CSS Modules 和普通 CSS；Remix 则通过 `links` 函数按需加载 CSS 文件，不依赖 CSS-in-JS 库的打包器集成。
- 🖼️ **图像与 SEO**：Next.js 内置 `next/image` 组件实现自动优化，并通过 `<Head>` 组件管理 SEO 元数据；Remix 无内置图像优化，通过 `meta` 函数导出元数据。
- 🛡️ **错误处理**：Remix 利用 React Error Boundary 实现组件级错误隔离，错误可向上冒泡，不会导致整个页面崩溃；Next.js 仅支持 404/500 等自定义错误页面。
- 🚀 **部署灵活性**：Next.js 主要部署在 Node.js 环境（如 Vercel）；Remix 基于 Web Fetch API，可原生部署到 Cloudflare Workers、Deno Deploy 等边缘环境，且使用 esbuild 构建速度更快。

---

### [Shopify收购Remix以强化其店面设计工具 | TechCrunch](https://techcrunch.com/2022/10/31/shopify-acquires-remix-to-bolster-its-storefront-design-tools/)

**原文标题**: [Shopify acquires Remix to bolster its storefront design tools | TechCrunch](https://techcrunch.com/2022/10/31/shopify-acquires-remix-to-bolster-its-storefront-design-tools/)

Shopify 收购了开源 Web 框架 Remix，旨在提升其开发者平台和 Hydrogen 框架的性能与可扩展性，同时 Remix 将继续保持独立和开源。

- 🛒 Shopify 收购了开源 Web 框架 Remix，具体财务条款未披露
- 🚀 Remix CEO 表示，收购将带来长期支持，助其专注于性能与可扩展性
- 🧩 Remix 由前 Twitter 工程师 Michael Jackson 和 Ryan Florence 于 2020 年共同创立，以 React Router 闻名
- ⚡ Remix 是一个全栈 Web 框架，支持预取功能，可并行加载页面元素以减少加载时间
- ☁️ 框架兼容 AWS、Google Cloud、Netlify、Vercel 和 Cloudflare Workers 等云环境
- 💰 收购前，Remix 已从 OSS Capital 和天使投资人处筹集 300 万美元种子资金
- 🔧 Shopify 计划将 Remix 用于 Hydrogen 框架，改善数据加载、路由和错误处理
- 📈 这是 Shopify 自收购 Deliverr 后的首次收购，此前还收购了 Dovetail 并投资了 Single、Sanity 和 Klaviyo
- 📉 Shopify 在经历 Q2 动荡后，Q3 亏损小于预期，股价上涨 17%

---

### [React Router v7 | Remix](https://remix.run/blog/react-router-v7)

**原文标题**: [React Router v7 | Remix](https://remix.run/blog/react-router-v7)

React Router v7 稳定版发布，整合 Remix 功能，支持 React 18 到 19 的过渡，并提供升级指南和新应用模板。

- 🎉 宣布 React Router v7 稳定版发布，整合 Remix 核心功能
- 🔄 鼓励 Remix v2 用户升级，v6 用户可通过“框架模式”获得新特性
- 🛠️ v7 新增 Vite 编译器、服务端渲染、HMR、类型安全等增强
- 📘 提供 v6 和 Remix v2 的升级指南，简化迁移路径
- 🚀 新应用可选择库模式或框架模式，框架模式支持 Docker、Cloudflare Workers 部署
- 📦 提供 create-react-router 和 create-vite 快速启动模板，包含 Tailwind 样式和部署流水线
- 📚 完整文档可查阅官方指南，获取所有新功能详情

---

### [通过上下文工程、RAG和可靠评估框架构建可靠的AI功能。| 前端大师](https://frontendmasters.com/courses/ai-engineering/?utm_source=email&utm_medium=javascriptweekly&utm_content=aiengineering)

**原文标题**: [Build reliable AI features through context engineering, RAG, and reliable eval harnesses. | Frontend Masters](https://frontendmasters.com/courses/ai-engineering/?utm_source=email&utm_medium=javascriptweekly&utm_content=aiengineering)

本课程深入讲解AI工程的核心实践，从零构建可评估、可迭代的AI代理系统。

- 🤖 **AI工程核心概念**：AI工程是构建在基础模型之上的新学科，强调处理非确定性系统，需在自然语言行为与工程规范间取得平衡
- 🛠️ **Cloudflare代理架构**：基于Durable Objects构建有状态服务端代理，通过WebSocket实现流式通信，使用Zod Schemas定义工具接口
- 📝 **聊天界面实现**：利用useAgent/useAgentChat React Hooks处理WebSocket连接，实现工具调用状态跟踪与画布实时集成
- 📊 **评估体系构建**：建立类似单元测试的评估框架，包含黄金数据集、代码评分器（验证元素有效性）和Braintrust可观测性平台
- 🔧 **上下文工程**：通过TOON格式序列化画布状态（比JSON节省token），优化系统提示词（含少样本示例、硬规则、负面提示），建立基线评估
- 🎯 **高级工具开发**：将原始工具重构为CRUD操作（add/update/remove），实现客户端工具执行，集成Tavily网络搜索工具
- 🔄 **改进循环方法论**：运行评估→检查产品→形成假设→单变量修改→重新评估，强调隔离变量和最终制品评估
- 📚 **RAG检索增强生成**：使用Upstash Vector建立向量数据库，创建可重用的索引脚本，实现内部文档检索工具
- 🏭 **生产级实践**：强调人工审批架构、持久化执行、数据飞轮、遥测技术和真实用户反馈循环

---

### [Node.js — Node.js 26.0.0（当前版本）](https://nodejs.org/en/blog/release/v26.0.0)

**原文标题**: [Node.js — Node.js 26.0.0 (Current)](https://nodejs.org/en/blog/release/v26.0.0)

Node.js 26.0.0 正式发布，带来多项重大更新，包括默认启用 Temporal API、V8 引擎升级至 14.6、Undici 更新至 8.0，以及多项弃用和移除。该版本目前为 Current 版本，将于 10 月进入长期支持 (LTS)。

- 🕐 Temporal API 默认启用：提供现代化日期/时间 API，替代传统 Date 对象
- ⚙️ V8 引擎升级至 14.6：新增 `WeakMap.prototype.getOrInsert()` 和 `Iterator.concat()` 等特性
- 🌐 Undici 更新至 8.0.2：HTTP 客户端实现获得新功能和改进
- ❌ 多项弃用和移除：包括 `crypto`、`http`、`stream` 和 `module` 模块的旧 API 清理
- 🛠️ 构建系统更新：GCC 要求提升至 13.2，Python 3.9 支持被移除
- 🔒 安全修复：包含 CVE-2026-21717 的修复
- 📦 支持多种平台：提供 Windows、macOS、Linux、AIX 等平台的安装包

---

### [《时间修复：JavaScript中处理时间的九年历程》| 彭博JS博客](https://bloomberg.github.io/js-blog/post/temporal/)

**原文标题**: [Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/temporal/)

## 历时九年，JavaScript 终于迎来全新时间日期 API Temporal

- 🕰️ **Date 的先天缺陷**：1995 年 Brendan Eich 在 10 天内直接移植了 Java 的 Date 实现，导致其存在可变性、月份算术不一致、解析歧义等长期问题
- 📦 **库生态的困境**：Moment.js 等第三方库虽解决了部分问题，但带来了巨大的包体积（含全部时区和语言数据），且维护成本越来越高
- 🏛️ **TC39 标准化进程**：Temporal 从 2018 年的 Stage 1 提案开始，历经 Stage 2、Stage 2.7、Stage 3，最终于 2026 年达到 Stage 4，纳入 ES2026 规范
- 🤝 **多方协作的冠军团队**：Microsoft、Bloomberg、Igalia、Google 等公司的工程师（包括 Maggie Johnson-Pint、Philipp Dunkel、Philip Chimento 等）共同推动提案
- 🧩 **核心类型设计**：Temporal 提供 `ZonedDateTime`（带时区/日历的精确时刻）、`Instant`（纳秒精度的时间点）、`PlainDate/PlainTime/PlainDateTime`（纯日期/时间）、`Duration`（时间段）等不可变类型
- 🌍 **日历与时区支持**：原生支持希伯来历等多种日历系统，算术运算按日历规则执行；`ZonedDateTime` 能正确处理夏令时转换
- ⚡ **跨引擎共享实现**：Google 和 Boa 合作开发 `temporal_rs` Rust 库，降低实现门槛，提高维护效率，目前通过 100% 测试
- 🚀 **浏览器支持现状**：Firefox v139、Chrome v144、Edge v144、TypeScript 6.0 Beta 已支持，Safari 部分支持
- 🔮 **未来整合方向**：需与日期选择器、`DOMHighResTimeStamp`、Cookie 过期等 Web API 集成，让 Temporal 替代 Date 的现有使用场景

---

### [Vitest | 下一代测试框架](https://vitest.dev/)

**原文标题**: [Vitest | Next Generation testing framework](https://vitest.dev/)

概述摘要  
Vitest 是一个基于 Vite 的原生测试框架，具有快速、轻量、集成度高的特点，兼容 Jest，支持 ESM、TypeScript 和 JSX，并且免费开源。  

- ⚡ 基于 Vite 构建：原生复用 Vite 配置和插件，确保应用与测试一致性，但不强制使用 Vite  
- 🔄 Jest 兼容：支持 Expect、快照、覆盖率等功能，从 Jest 迁移简单直接  
- 🧠 智能即时监听：仅重新运行相关变更，类似测试版的 HMR，提升效率  
- 🛠️ 开箱即用：原生支持 ESM、TypeScript 和 JSX，由 Oxc 提供动力  
- 💰 免费开源：由赞助商支持，可自由使用和贡献

---

### [[提案] 框架无关的 Vitest · vitest-dev/vitest · 讨论 #10271 · GitHub](https://github.com/vitest-dev/vitest/discussions/10271)

**原文标题**: [[Proposal] Framework-Agnostic Vitest · vitest-dev/vitest · Discussion #10271 · GitHub](https://github.com/vitest-dev/vitest/discussions/10271)

Vitest 提出框架无关化提案，旨在解耦 Vite 依赖，使其能适配更多构建工具和运行环境。

- 🚀 **核心提案**：新增 `--framework` CLI 标志，用户可指定适配器（如 `@vitest/framework-node`），让 Vitest 核心与具体构建/运行时环境解耦。
- 🔗 **动机**：Vitest 的测试运行、断言、快照等核心功能已独立，但转换、模块解析等仍强依赖 Vite。解耦后，用户无需安装 Vite 即可使用其他工具（如 esbuild、Deno、Bun）。
- 📦 **框架适配器**：框架包负责配置加载、模块转换、文件监听等，通过稳定接口与 Vitest 核心交互。Vite 作为默认框架，其他可独立开发。
- 🔧 **迁移兼容**：无破坏性变更，默认行为不变（`--framework` 省略时使用 `@vitest/framework-vite`），现有 `viteModuleRunner: false` 模式可作为 Node 适配器原型。
- ❓ **待定问题**：框架接口的具体形状、`--framework` 的非 CLI 指定方式（如环境变量或标记文件）、框架选项类型隔离、报告器/覆盖率等组件的兼容性声明。
- 🎯 **非目标**：不取代 Vite 默认地位，不定义通用插件格式，不要求首日支持所有构建工具，仅需一个替代框架即可验证接口。

---

### [Zig → Rust 移植指南 | Hacker News](https://news.ycombinator.com/item?id=48016880)

**原文标题**: [Zig → Rust porting guide | Hacker News](https://news.ycombinator.com/item?id=48016880)

Bun 团队正在探索将项目从 Zig 迁移到 Rust 的可能性，目前处于实验阶段，尚未做出最终决定。该实验主要由 AI 工具（如 Claude）驱动，旨在评估 Rust 版本的可行性、性能和可维护性。此举引发了社区的热烈讨论，涉及对 AI 生成代码质量、项目方向以及语言选择的担忧。

- 🧪 **实验性质**：Bun 的创建者 Jarred 明确表示这只是一个实验性分支，代码尚未运行，很可能被完全废弃。他强调团队没有承诺重写。
- 🤖 **AI 驱动**：该迁移主要由 AI 模型（如 Claude）完成，通过提示词将 Zig 代码逐行翻译为 Rust。这引发了关于代码质量、可审查性和可维护性的争议。
- ⚡ **性能与稳定性**：Bun 在 Zig 中遇到了一些问题，如内存泄漏、段错误和编译速度慢。Rust 的强类型系统和内存安全特性被认为可能有助于解决这些问题。
- 🗣️ **社区反应**：社区反应两极分化。一些人认为这是对技术问题的合理探索，另一些人则批评这是“氛围编码”（vibe coding），并担心项目质量下降。
- 🔄 **语言生态**：Zig 仍处于开发阶段，变化频繁，且其反 AI 政策可能限制了 Bun 的贡献。Rust 则更成熟、稳定，拥有更大的社区和更好的 AI 支持。
- 🏢 **收购背景**：Bun 被 Anthropic 收购后，其开发方向可能受到影响。Anthropic 是 Claude 的开发者，因此对 Rust 和 AI 辅助开发有更强的倾向。
- 📉 **用户担忧**：一些用户对 Bun 的未来表示担忧，认为其开发方向不稳定，并考虑迁移回 Node.js 或 Deno。

---

### [文档：添加Phase-A移植指南 · oven-sh/bun@46d3bc2 · GitHub](https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd5730ef1549e88407701a5)

**原文标题**: [docs: add Phase-A porting guide · oven-sh/bun@46d3bc2 · GitHub](https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd5730ef1549e88407701a5)

概述总结
- 📘 新增了 Phase-A 移植指南文档（docs/PORTING.md）
- 🛠️ 添加了批量移植脚本（scripts/port-batch.ts）
- 📊 总共变更了 622 行代码，均为新增内容
- 🔗 提交基于父提交 0a7bed5，由 Jarred-Sumner 完成
- ⭐ 项目拥有 89.7k 星标和 4.4k 分支，社区活跃度高

---

### [我在 Bun 工作，这是我的分支。整个帖子反应过度了。302 co... | Hacker News](https://news.ycombinator.com/item?id=48019226)

**原文标题**: [I work on Bun and this is my branch This whole thread is an overreaction. 302 co... | Hacker News](https://news.ycombinator.com/item?id=48019226)

概述摘要
Bun项目创始人Jarred Sumner澄清，将Bun从Zig移植到Rust仅是一个实验性分支，尚未承诺重写，代码很可能被废弃。社区对此反应过度，引发大量讨论，涉及项目方向、AI辅助代码生成、开源维护者责任等话题。

- 🧪 实验性分支：Jarred强调分支代码尚未编译，仅是探索性工作，高概率被丢弃。
- 🔥 社区反应过度：302条评论针对不工作的代码，许多讨论基于标题而非实际内容。
- 🤖 AI辅助移植：使用Claude等AI模型进行语言翻译，展示AI在代码重构中的潜力。
- 🗣️ 语言之争：Zig与Rust的社区分歧被点燃，但项目方认为两者可共存。
- ⚠️ 项目质量担忧：用户指出Bun存在长期未修复的bug，质疑为何优先进行实验而非修复问题。
- 🛠️ 开源维护挑战：维护者面临用户期望与实验自由之间的张力，需平衡透明度与创新。
- 📈 实验价值：即使代码被丢弃，这种对比实验也能提供关于项目结构和语言选择的宝贵见解。

---

### [错误](https://javascriptweekly.com/link/184707/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184707/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184707/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184708/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184708/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184708/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184759/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184759/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184759/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184760/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184760/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184760/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184709/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184709/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184709/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184710/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184710/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184710/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184711/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184711/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184711/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184712/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184712/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184712/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184713/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184713/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184713/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184714/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184714/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184714/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184715/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184715/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184715/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184716/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184716/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184716/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184717/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184717/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184717/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184771/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184771/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184771/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184772/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184772/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184772/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184719/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184719/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184719/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184720/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184720/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184720/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184768/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184768/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184768/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184769/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184769/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184769/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184722/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184722/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184722/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184723/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184723/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184723/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184724/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184724/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184724/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184725/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184725/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184725/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184727/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184727/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184727/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184728/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184728/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184728/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184729/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184729/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184729/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184730/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184730/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184730/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184731/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184731/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184731/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184732/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184732/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184732/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184733/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184733/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184733/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184734/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184734/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184734/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184735/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184735/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184735/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184736/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184736/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184736/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184737/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184737/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184737/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184738/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184738/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184738/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184739/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184739/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184739/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184740/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184740/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184740/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184741/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184741/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184741/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184770/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184770/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184770/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184743/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184743/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184743/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184744/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184744/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184744/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184745/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184745/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184745/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184746/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184746/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184746/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184747/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184747/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184747/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184748/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184748/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184748/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184749/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184749/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184749/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184750/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184750/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184750/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184751/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184751/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184751/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184761/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184761/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184761/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/184762/web)

**原文标题**: [Error](https://javascriptweekly.com/link/184762/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/184762/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

