### [React 状态周报第 438 期：2025 年 7 月 30 日](https://react.statuscode.com/issues/438)

**原文标题**: [React Status Issue 438: July 30, 2025](https://react.statuscode.com/issues/438)

概述总结  
本期简报涵盖了多个前端和 JavaScript 领域的最新动态，包括 TanStack DB 的发布、React 相关工具更新、开源项目推荐以及行业调查结果等。  

- ⚛️ **TanStack DB 发布** — 嵌入式客户端数据库，支持实时关系查询和增量更新，首个测试版已开放。  
- 🔍 **Reaper SDK** — 开源工具用于检测生产环境中的死代码，支持 iOS 和 Android。  
- 🛠 **useCallback 与 useMemo 讨论** — 探讨其局限性及 React Compiler 等新工具的可能改进。  
- 📊 **Stack Overflow 2025 调查** — React 成为最受欢迎的 Web 技术，Svelte 则更受“赞赏”。  
- 📦 **Parcel 支持 React Server Components** — 深入解析其实现原理及`use client`指令作用。  
- 🚀 **React Native 0.81 预编译 iOS 构建** — 构建速度提升高达 10 倍。  
- 🎥 **Reanimated 4 发布** — 结合 CSS 动画优势，为 React Native 提供强大动画能力。  
- 📚 **Rooks.js 8.4 更新** — 提供近 100 个自定义 Hook，覆盖多种应用场景。  
- 🌐 **JavaScript 运行时盘点** — 回顾历年 JavaScript 运行时和引擎的发展。  
- 🔒 **OSS Rebuild 计划** — Google 推出项目以提高 npm 等开源生态的安全性。

---

### [停止重复渲染 — TanStack DB，专为 TanStack Query 设计的嵌入式客户端数据库 | TanStack 博客](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query)

**原文标题**: [Stop Re-Rendering — TanStack DB, the Embedded Client Database for TanStack Query | TanStack Blog](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query)

TanStack DB 是一个客户端数据库层，旨在解决 React 应用中因数据更新导致的性能问题。它通过差异数据流技术，仅更新发生变化的部分，从而大幅提升性能。TanStack DB 可以与现有的 TanStack Query 集成，提供实时查询、乐观更新和简化的架构。

- 🚀 **性能优化**：TanStack DB 使用差异数据流技术，仅更新变化的部分，例如在 M1 Pro 上更新 10 万条数据中的一行仅需 0.7 毫秒。
- 🔄 **实时查询**：通过 `useLiveQuery` 实现自动更新，无需手动处理数据过滤和重新渲染。
- ⚡ **乐观更新**：自动处理乐观更新和错误回滚，减少样板代码。
- 📊 **简化架构**：TanStack DB 支持标准化数据集合和增量连接，减少 API 调用和网络依赖。
- 🔌 **后端灵活性**：支持 REST、GraphQL、WebSocket 等多种数据源，并可自定义集合。
- 🔄 **增量采用**：可以逐步采用，无需大规模迁移，适合现有项目。
- 🤝 **与 TanStack Query 集成**：TanStack Query 负责数据获取，TanStack DB 负责数据一致性和性能优化。
- 🛠 **同步引擎支持**：与 Electric、Trailblaze 和 Firebase 等同步引擎集成，实现实时更新和高效数据加载。
- 🎯 **目标**：提供真正的后端灵活性、增量采用、大规模查询性能、可靠的乐观更新和类型安全。
- 📅 **下一步**：TanStack DB 0.1 版本已发布，欢迎遇到性能问题的团队试用并提供反馈。

---

### [未找到标题](https://x.com/tannerlinsley/status/1950262878852043103)

**原文标题**: [No title found](https://x.com/tannerlinsley/status/1950262878852043103)

当前页面提示 JavaScript 未启用或浏览器不受支持，建议采取相应措施以继续使用 x.com。

- 🚫 JavaScript 未启用：检测到浏览器中 JavaScript 被禁用，需启用或更换支持浏览器。  
- 🌐 支持浏览器列表：可在帮助中心查看支持的浏览器详情。  
- 🔧 隐私扩展问题：部分隐私相关扩展可能导致问题，建议禁用后重试。  
- 📜 相关链接：提供帮助中心、服务条款、隐私政策等文档入口。  
- 🔄 操作建议：页面错误时可尝试点击“重试”按钮重新加载。  
- ©️ 版权信息：页面底部标注 2025 年 X 公司版权声明。

---

### [无用的 useCallback | TkDodo 的博客](https://tkdodo.eu/blog/the-useless-use-callback)

**原文标题**: [The Useless useCallback | TkDodo's blog](https://tkdodo.eu/blog/the-useless-use-callback)

文章讨论了在 React 中使用`useCallback`和`useMemo`进行记忆化的常见误区，指出在某些情况下这些优化是无效甚至有害的。

- 🚫 **记忆化的目的**：主要用于性能优化和防止 effect 过度触发，通过保持引用稳定来避免不必要的重新渲染或 effect 执行。
  
- 🤔 **无效记忆化场景**：当传递给非记忆化组件或 React 内置组件（如`<button>`）时，`useCallback`和`useMemo`不会带来任何性能提升，反而增加内部开销。

- 🔄 **依赖传递问题**：将非原始值 props 作为依赖项（如函数或对象）可能导致记忆化失效，因为父组件可能未记忆化这些 props，导致下游记忆化全部崩溃。

- 🏗️ **实际案例**：以 Sentry 代码库中的`useHotkeys`为例，展示了多层记忆化因底层数据未记忆化而完全失效的连锁反应，强调过度记忆化的复杂性。

- 🛠️ **解决方案**：
  - 使用**最新 Ref 模式**（`useRef`+`useEffect`）手动跟踪最新值，避免依赖数组问题。
  - 等待 React 官方提供的**`useEffectEvent`**原语，直接解决非响应式最新值访问需求。

- 💡 **核心建议**：除非明确需要引用稳定性，否则应避免滥用记忆化，优先依赖编译器优化或更健壮的模式（如`useEffectEvent`）来简化代码。

---

### [宣布 TypeScript 5.9 RC 版本 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/)

**原文标题**: [Announcing TypeScript 5.9 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/)

TypeScript 5.9 RC 发布，带来多项新功能和优化，包括更简洁的 `tsconfig.json` 初始化、`import defer` 支持、`--module node20` 选项、DOM API 摘要描述等。

- 🚀 **TypeScript 5.9 RC 发布**：可通过 `npm install -D typescript@rc` 安装。
- 🛠️ **更简洁的 `tsconfig.json` 初始化**：`tsc --init` 生成的配置文件更精简，默认启用常用选项（如 `strict`、`jsx` 等）。
- ⏳ **支持 `import defer`**：延迟模块执行，直到首次访问模块属性，适用于条件加载和高开销初始化。
- 📦 **新增 `--module node20` 选项**：稳定支持 Node.js v20 行为，默认目标为 `es2023`。
- 📚 **DOM API 摘要描述**：为 DOM API 添加基于 MDN 的简要说明，提升开发体验。
- 🔍 **可扩展的悬停提示（预览）**：在编辑器中展开类型详细信息，支持快速查看嵌套类型。
- 📏 **可配置悬停提示长度**：通过 `js/ts.hover.maximumLength` 设置调整悬停信息显示长度。
- ⚡ **性能优化**：缓存类型实例化、减少闭包创建，提升复杂项目类型检查速度。
- ⚠️ **行为变更**：`lib.d.ts` 调整可能导致 `ArrayBuffer` 相关类型错误，需更新 `@types/node` 或明确指定类型。
- 🔜 **后续计划**：TypeScript 7 原生版本开发中，5.9 正式版预计一周内发布。

---

### [2025 年 Stack Overflow 开发者调查](https://survey.stackoverflow.co/2025/)

**原文标题**: [2025 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025/)

Stack Overflow 2025 年开发者调查报告概述：全球 49,000+ 开发者参与，覆盖 177 个国家，聚焦 AI 工具、LLMs 及社区平台趋势。  

- 🏆 **技术拒绝主因**：安全隐私问题（第 1 位）、高价（第 2 位）、替代品（第 3 位），AI 缺失影响最小（第 9 位）。  
- 🤖 **AI 工具使用**：84% 开发者已用或计划使用 AI 工具，47% 专业人士每日使用，但对其准确性信任度低（仅 3% 高度信任）。  
- ⏱️ **AI 代理影响**：69% 用户认为提升效率，但仅 17% 认可团队协作改进，66% 抱怨“AI 输出近似但不准确”。  
- 📊 **开发者角色**：软件架构师首次进前四（6.1%），全栈开发者占比最高（27%）。  
- 🐍 **技术趋势**：Python 采用率激增（57.9%），VS Code 稳居 IDE 榜首（75.9%），Cargo（Rust 工具链）获 71% 开发者推崇。  
- 🌍 **地域分布**：美国（20.4%）、德国（8.6%）、印度（7.2%）为受访前三，乌克兰跌出前五。  
- 🏡 **远程办公**：32.4% 开发者远程工作，美国比例最高（45%），德国 21% 可自由选择办公模式。  
- 📉 **AI 情绪变化**：正面评价降至 60%（2023/2024 年为 70%+），新手开发者信任度低于专业人士。  
- 📚 **学习方式**：36% 为职业发展学习 AI 工具，YouTube 更受编程新手青睐（70% vs 专业人士 60%）。  
- 💼 **工作满意度**：24% 开发者对工作满意（去年 20%），薪资上涨或是主因。  

（注：数据节选自 Stack Overflow 2025 年度开发者调查报告，覆盖 314 项技术及 62 个核心问题。）

---

### [技术 | 2025 年 Stack Overflow 开发者调查](https://survey.stackoverflow.co/2025/technology#2-web-frameworks-and-technologies)

**原文标题**: [Technology | 2025 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025/technology#2-web-frameworks-and-technologies)

Stack Overflow 2025 年度开发者调查报告摘要，涵盖技术趋势、工具偏好及开发者行为数据。

- 🐍 **Python 使用率激增**：过去一年 Python 采用率增长 7%，成为 AI、数据科学和后端开发的首选语言。  
- 🏆 **最受欢迎技术**：JavaScript（66%）、HTML/CSS（61.9%）、SQL（58.6%）和 Python（57.9%）占据编程语言前列。  
- 🚀 **Rust 最受推崇**：连续多年成为开发者最喜爱的语言（72% 满意度），其次是 Gleam（70%）和 Elixir（66%）。  
- 🐳 **Docker 普及率飙升**：使用率一年内增长 17 个百分点，成为近云开发的标配工具。  
- 📊 **数据库趋势**：PostgreSQL（55.6%）是最常用数据库，Redis 使用率增长 8%，反映对高性能缓存的需求。  
- 🤖 **AI 工具主导**：OpenAI GPT 模型使用率达 82%，Claude Sonnet 是第二受欢迎的 LLM（45% 专业开发者使用）。  
- 💻 **开发环境**：VS Code 以 75.9% 使用率稳居第一，其次是 Visual Studio（29%）和 IntelliJ IDEA（27.1%）。  
- 🌐 **社区平台**：Stack Overflow（84.2%）和 GitHub（66.9%）是开发者主要聚集地，学习编程者更依赖 YouTube（70%）。  
- 🔄 **技术迁移趋势**：Python 开发者倾向转向 Rust 和 Go；MongoDB 用户希望学习 PostgreSQL；云平台用户普遍想掌握 Docker。  
- 📈 **新兴技术关注**：Google Gemini（29.2%）、大语言模型（27.6%）和 Tailwind CSS 4（21.8%）是增长最快的 Stack Overflow 标签。  

（数据覆盖 31,569 名受访者，完整报告可下载）

---

### [Parcel 如何打包 React 服务器组件](https://devongovett.me/blog/parcel-rsc.html)

**原文标题**: [How Parcel bundles React Server Components](https://devongovett.me/blog/parcel-rsc.html)

Parcel v2.14.0 新增了对 React Server Components (RSCs) 的支持，本文深入探讨了 RSCs 如何与打包工具集成、指令如 "use client" 的内部工作原理、代码分割机制及其优化等核心内容。

- 🚀 **Parcel 支持 RSCs**  
  Parcel v2.14.0 新增对 React Server Components 的支持，通过统一模块图实现跨环境代码分割。

- 📦 **打包工具基础功能**  
  打包工具将多个 JavaScript 模块合并为更少的文件，优化网络请求和压缩效率，解决 HTTP/2 并行请求限制问题。

- 🔄 **代码分割优化**  
  现代打包工具（如 Parcel）自动提取公共依赖到独立包中，平衡初始加载性能和缓存利用率，避免重复下载代码。

- ⚡ **动态加载问题**  
  单页应用 (SPA) 中动态 `import()` 会导致网络瀑布问题，嵌套路由和异步数据加载进一步加剧性能瓶颈。

- 🛠 **RSCs 的解决方案**  
  React Server Components 通过服务器端渲染和预加载机制，消除网络瀑布，实现代码和数据的并行加载。

- 🌐 **环境与指令**  
  Parcel 使用 `"use client"` 和 `"use server"` 指令标记模块环境，生成客户端引用 (Client References) 以实现 RSCs 的序列化与反序列化。

- 📂 **客户端组件打包**  
  多个客户端组件会被打包到同一文件中，减少 HTTP 请求，仅当条件渲染时才会按需代码分割。

- 🎨 **CSS 与资源预加载**  
  Parcel 自动注入 `<link>` 标签并利用 React 19 的 `precedence` 和 `Suspense` 优化 CSS 加载，避免 FOUC 并支持资源捆绑。

- 🔮 **未来展望**  
  后续将探讨 Server Actions 和渐进式加载导入映射等高级特性。

---

### [包裹 v2.14.0](https://parceljs.org/blog/v2-14-0/)

**原文标题**: [
      Parcel v2.14.0
    ](https://parceljs.org/blog/v2-14-0/)

Parcel v2.14.0 引入了 React Server Components 的 Beta 支持，新增了 MDX 的一流支持、用于创建新项目的 CLI 工具、新的 React 错误覆盖层，并优化了浏览器缓存机制。

- 🚀 **React Server Components 支持**：新增 Beta 支持，支持服务端渲染或静态渲染，减少客户端包大小。
- 📦 **MDX 一流支持**：深度集成 MDX，支持自定义代码块组件和自动生成目录。
- 🛠️ **create-parcel CLI**：新增 CLI 工具，快速搭建项目模板，支持 React Server Components 等多种模板。
- 🔄 **Create React App 迁移支持**：提供官方迁移文档和自动化脚本 `cra-to-parcel`，帮助用户从 CRA 迁移到 Parcel。
- 🚨 **新的 React 错误覆盖层**：优化错误显示，支持服务端代码错误和 React hydration 错误。
- 📜 **原生 HTML import maps**：使用原生 import maps 优化缓存机制，减少缓存失效问题。
- 🌐 **多环境支持**：统一模块图，支持跨环境代码拆分，包括 `"use client"` 和 `"use server"` 指令。
- 📂 **静态渲染支持**：新增静态站点生成器功能，支持预渲染静态页面。
- 🔧 **开发模式优化**：支持 Node 服务器开发模式，内置热重载功能。

---

### [预编译的 React Native iOS 版：0.81 版本将带来更快的构建速度](https://expo.dev/blog/precompiled-react-native-for-ios)

**原文标题**: [Precompiled React Native for iOS: Faster builds are coming in 0.81](https://expo.dev/blog/precompiled-react-native-for-ios)

Expo 是一个提供应用开发服务的平台，包含多种工具和资源，适用于开发者构建和管理应用。

- 📝 **博客与文档** - 提供博客和技术文档，帮助开发者获取最新信息和指南。  
- 🛠️ **产品与工具** - 包括 Expo CLI、EAS（Expo 应用服务）、Expo Go 和 Snack 等开发工具。  
- 📊 **仪表盘** - 提供 Dashboard 管理所有帖子及产品。  
- 🌟 **社区支持** - 鼓励在 GitHub 上 Star 项目，加入 Discord 社区获取支持。  
- 📚 **资源** - 包含更新日志、新闻通讯和信任中心等资源。  
- 🏢 **公司信息** - 提供关于公司、招聘、品牌和法律条款的详细信息。  
- ⚖️ **法律与合规** - 涵盖服务条款、隐私政策、安全合规和社区准则。  
- ©️ **版权声明** - 版权归 650 Industries, Inc. 所有，保留所有权利。

---

### [发布 0.81.0-rc.3 · facebook/react-native · GitHub](https://github.com/facebook/react-native/releases/tag/v0.81.0-rc.3)

**原文标题**: [Release 0.81.0-rc.3 · facebook/react-native · GitHub](https://github.com/facebook/react-native/releases/tag/v0.81.0-rc.3)

React Native 的 GitHub 仓库页面，展示了版本 v0.81.0-rc.3 的发布信息和相关社区互动。

- 🚀 React Native 发布了预发布版本 v0.81.0-rc.3，包含 335 次提交更新。  
- ⚙️ 提供了 Hermes 和 ReactNativeDependencies 的 dSYMS 文件，支持 Debug 和 Release 版本。  
- 📄 用户可以通过提供的链接提交问题或请求，并使用 Upgrade Helper 辅助升级。  
- 📝 完整的更新日志可在 CHANGELOG.md 文件中查看。  
- 👍 社区反应热烈，共有 10 个点赞、4 个大笑、8 个庆祝、7 个爱心和 4 个火箭表情。  
- 🔄 页面加载时出现错误提示，需重新加载页面以查看完整内容。

---

### [为使用 Clerk、Lovable 和 Supabase 构建的应用添加多租户功能](https://clerk.com/blog/multi-tenancy-clerk-lovable?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=lovable-mt&utm_content=07-30-25&dub_id=x0Mxq4Zgnaa3B2wx)

**原文标题**: [Add multi-tenancy to an app built with Clerk, Lovable, and Supabase](https://clerk.com/blog/multi-tenancy-clerk-lovable?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=lovable-mt&utm_content=07-30-25&dub_id=x0Mxq4Zgnaa3B2wx)

概述  
本文介绍了如何利用 Clerk Organizations、Lovable 和 Supabase 将单用户应用升级为支持多租户的 B2B 平台，实现数据隔离和团队管理功能。

- 🚀 **项目背景**：基于之前使用 Lovable 和 Supabase 构建的单用户应用，通过 Clerk Organizations 扩展为多租户应用。  
- 🔧 **启用 Clerk 组织功能**：在 Clerk 仪表板中开启 Organizations，并配置相关设置。  
- 🖥️ **添加组织切换器**：通过 Lovable 快速集成`<OrganizationSwitcher />`组件，支持用户创建和管理团队。  
- 🔒 **更新 RLS 策略**：修改 Supabase 的行级安全策略，确保数据按组织或用户 ID 隔离。  
- 📝 **数据创建逻辑**：根据用户当前活跃组织动态设置`owner_id`，确保数据归属正确。  
- ✅ **测试验证**：切换组织和个人账户，验证数据隔离及团队共享功能。  
- 🌟 **成果总结**：通过 Clerk、Supabase 和 Lovable 的协作，快速实现多租户架构，适合 B2B 产品开发。  
- 🔗 **扩展阅读**：提供相关文档和起始指南链接，方便进一步探索。

---

### [Remix 3 与以 React 为中心的架构时代的终结 - The New Stack](https://thenewstack.io/remix-3-and-the-end-of-react-centric-architectures/)

**原文标题**: [Remix 3 and the End of React-Centric Architectures - The New Stack](https://thenewstack.io/remix-3-and-the-end-of-react-centric-architectures/)

欢迎加入 The New Stack 社区，获取最新资讯和独家内容！以下是关键信息点：

- 📧 提供邮箱地址订阅，或重新订阅（若之前已退订）  
- 🔒 承诺不售卖或共享用户信息，需同意《使用条款》和《隐私政策》  
- 👤 需填写基本信息（姓名、公司、国家等）  
- 🌍 国家选项包含全球多国/地区列表  
- 💼 职业相关信息（职位级别、角色、公司规模等）需详细填写  
- 🏢 需选择所在行业类型  
- 🔗 可选填 LinkedIn 个人资料链接  
- 📬 订阅成功后，工作日将收到精选内容  
- 📌 后续步骤：查收确认邮件调整偏好、关注社交媒体、浏览热门故事  

祝您探索愉快！

---

### [使用运行时密钥注入对 Next.js 进行仪表化 | Phase 博客](https://phase.dev/blog/instrumenting-nextjs-with-runtime-secret-injection/)

**原文标题**: [Instrumenting Next.js with runtime secret injection | Phase Blog](https://phase.dev/blog/instrumenting-nextjs-with-runtime-secret-injection/)

Next.js 14 引入了 instrumentation 功能，允许在应用启动时注入运行时密钥，提升安全性和可移植性。

- 🛠️ **Instrumentation 文件**：Next.js 14 新增功能，通过根目录的 `instrumentation.ts/js` 文件在服务器启动时执行自定义逻辑（如初始化日志或遥测服务）。  
- 🔒 **运行时密钥注入**：避免密钥泄露到代码或构建产物中，相比 `.env` 文件更安全且易于管理。  
- ⚙️ **实现步骤**：  
  - 1️⃣ 创建 `instrumentation.ts` 文件，使用 `register()` 函数获取密钥（如通过 Phase 或 AWS Secrets Manager）。  
  - 2️⃣ 将密钥存储在 `globalThis` 或模块缓存中，供应用全局访问。  
  - 3️⃣ 客户端组件通过服务端组件传递的 props 获取密钥，避免使用 `NEXT_PUBLIC_` 前缀的环境变量。  
- 🌍 **优势**：支持多密钥管理工具（如 HashiCorp Vault），增强团队协作和审计能力。  
- ⚠️ **注意事项**：全局存储密钥需谨慎，可改用临时文件或模块封装以提高安全性。  
- 📚 **推荐阅读**：Next.js 官方文档、Phase SDK 及密钥管理最佳实践。

---

### [将 JSX 重写为 Astro 的笔记 | Carlos Neves / 博客](https://carlosn.com.br/blog/post/notes-on-rewriting-jsx-as-astro/)

**原文标题**: [Notes on rewriting JSX as Astro | Carlos Neves / Blog](https://carlosn.com.br/blog/post/notes-on-rewriting-jsx-as-astro/)

Astro 框架在开发体验上有其独特之处，虽然存在一些工具和架构上的不足，但整体上是一个高效且实用的静态站点生成工具。

- 🛠️ **VS Code 集成问题**：工具链有待改进，如自动导入和自动补全功能不稳定，部分指令触发 TypeScript 错误。
- 📦 **组件架构限制**：Astro 的 props 通过全局变量`Astro.props`访问，且每个.astro 文件只能导出一个组件，不支持组件组或常量导出。
- 🎨 **样式系统**：类似 Svelte，支持组件内嵌作用域样式，减少 CSS 文件依赖。
- 🔍 **图标库使用不便**：安装和导入图标组件不如预期简便，需手动处理。
- 🐞 **布局 Bug**：开发时偶尔出现框架 HTML 注入`<pre>`元素的问题，需重启服务解决。
- 📝 **语法差异**：使用`<slot/>`替代`{children}`，支持命名插槽；HTML 属性如`class`替代`className`；注释风格为 HTML 式。
- 📑 **Markdown/MDX痛点**：MDX 中非 Markdown 语法标题无法自动提取，且项目级自定义组件替换困难。
- 🏝️ **Astro Islands 概念**：支持多框架动态组件（如 React/Svelte），静态页面中仅动态部分需客户端渲染。
- 🏗️ **架构限制**：无法在 JS 代码块内操作组件，动态路由文件不能复用为常规组件，`getStaticPaths`闭包功能缺失。
- ⚪ **空格与格式化问题**：默认不修剪空格，Prettier 与 Astro 格式化规则冲突导致多余空格。
- 📜 **脚本优化不足**：内联脚本无法选择性压缩，全有或全无。
- ✅ **总结**：尽管存在瑕疵，Astro 通过清晰分离构建时/客户端代码，提供了高效的开发体验，适合博客等项目。  

Happy building! 🚀

---

### [Reanimated 4 稳定版发布 —— React Native 动画的未来 | 作者：Krzysztof Magiera | 2025 年 7 月 | Software Mansion](https://blog.swmansion.com/reanimated-4-stable-release-the-future-of-react-native-animations-ba68210c3713?gi=d6cb53f03190)

**原文标题**: [Reanimated 4 Stable Release — the Future of React Native Animations | by Krzysztof Magiera | Jul, 2025 | Software Mansion](https://blog.swmansion.com/reanimated-4-stable-release-the-future-of-react-native-animations-ba68210c3713?gi=d6cb53f03190)

Reanimated 4 稳定版发布，这是自 Reanimated 2 引入 worklets 概念以来最重要的一次更新，带来了全新的 CSS 兼容动画 API 和性能优化，同时保持与旧版本的兼容性。

- 🎉 **Reanimated 4 稳定版发布**：经过六个月的测试，首个稳定版本正式推出，这是自 Reanimated 2 以来最重要的更新。  
- 🎨 **CSS 动画与过渡 API**：新增声明式 CSS 兼容动画 API，简化状态驱动的动画代码，提升开发效率和性能优化空间。  
- ⚡ **Worklets 仍占重要地位**：复杂场景（如手势驱动动画、屏幕过渡）仍推荐使用 worklets，未来还将有更多性能优化。  
- 📦 **独立 Worklets 包**：worklets 代码已移至 `react-native-worklets` 包，提升开发灵活性，但对用户透明无影响。  
- 🔧 **兼容性与迁移**：API 兼容 Reanimated 3，但需应用已启用 React Native 新架构。部分废弃方法将被移除，详情参考迁移指南。  
- 🌀 **弹簧动画改进**：默认使用更自然的弹簧动画实现，减少参数敏感性问题，推荐仅设置时长和阻尼比。  
- 🙏 **致谢合作伙伴**：感谢 Shopify 和 Meta React Native 团队五年来的支持与合作。  
- 🔗 **相关资源**：提供 GitHub 发布说明、CSS 动画文档等链接，以及开发团队联系方式。

---

### [介绍 React Native Reanimated 4 - YouTube](https://www.youtube.com/watch?v=Wr2fOM_xD2I)

**原文标题**: [Introducing React Native Reanimated 4 - YouTube](https://www.youtube.com/watch?v=Wr2fOM_xD2I)

关于 YouTube 的相关信息与链接  
- 📢 关于 - 提供 YouTube 的基本信息和背景  
- 🗞️ 新闻 - 查看 YouTube 的最新动态和公告  
- ©️ 版权 - 了解 YouTube 的版权政策和相关内容  
- 📩 联系我们 - 获取与 YouTube 团队联系的途径  
- 🎨 创作者 - 资源和支持帮助内容创作者  
- 💼 广告 - 广告商相关信息和合作机会  
- 🛠️ 开发者 - 开发者工具和 API 资源  
- 📜 条款 - 使用 YouTube 的服务条款  
- 🔒 隐私 - 隐私政策和数据保护措施  
- ⚖️ 政策与安全 - 平台规则和安全指南  
- 🔧 YouTube 工作原理 - 了解平台的运作机制  
- � 测试新功能 - 体验和反馈 YouTube 的新功能  
- © 2025 Google LLC - 版权归属和年份声明

---

### [更优上传 - 为 React 打造的简单易用文件上传工具](https://better-upload.com/)

**原文标题**: [Better Upload - Simple and easy file uploads for React](https://better-upload.com/)

概述总结  
一个简单易用的 React 文件上传工具，支持直接上传至 S3 兼容服务，提供快速设置和美观的 UI 组件。  

- 🚀 **快速开始**：只需几分钟即可设置并直接上传文件至 S3 存储桶。  
- 🎨 **美观 UI**：使用 shadcn/ui 组件快速构建用户界面。  
- 🔒 **文件自主控制**：文件直接上传至您的 S3 存储桶，确保完全控制。  
- 📁 **文件限制**：每次最多上传 4 个文件，每个文件最大 2MB，支持 JPEG、PNG、GIF 格式。  
- ⚙️ **简单配置**：提供客户端和服务端代码示例，支持多文件上传和文件类型限制。  
- 🌐 **S3 兼容**：支持任何 S3 兼容服务，配置灵活方便。

---

### [快速入门 | 更优上传](https://better-upload.com/docs/quickstart)

**原文标题**: [Quickstart | Better Upload](https://better-upload.com/docs/quickstart)

概述：本文介绍了如何使用 Better Upload 在 React 应用中快速实现文件上传功能，包括安装、服务器设置、组件创建及配置步骤。

- 🚀 **快速开始**：通过 Better Upload 在几分钟内为 React 应用添加文件上传功能，支持多种 S3 兼容存储服务（如 AWS S3、Cloudflare R2）。
- 📦 **安装依赖**：需安装`better-upload`和 AWS S3 客户端包（通过 npm/pnpm/yarn/bun）。
- 🖥️ **服务器配置**：设置服务器生成预签名 URL，示例代码包含 Next.js 路由配置及 S3 客户端初始化（需替换桶名称）。
- 🛠️ **上传路由定义**：演示如何创建支持多文件（如最多 4 张图片）的上传路由`demo`，并限制文件类型为图像。
- 🔒 **进阶配置**：可选步骤如添加身份验证、修改 S3 对象键名。
- 📁 **UI 组件集成**：使用`<UploadDropzone />`和`useUploadFiles`钩子构建上传界面，支持文件类型、大小和数量限制。
- 🎯 **组件放置**：将上传组件嵌入应用页面（如 Next.js 的`page.tsx`），完成基础功能。
- 🎉 **完成提示**：运行应用即可上传文件至 S3 服务，超大文件（>5GB）需参考分片上传指南。
- 📚 **扩展学习**：提供更多概念（路由、钩子）、指南（表单集成、TanStack Query）和组件（按钮、带进度条拖放区）的链接。

---

### [Rooks.js](https://rooks.vercel.app/docs)

**原文标题**: [Rooks.js](https://rooks.vercel.app/docs)

Rooks.js 是一个提供多种实用 React 自定义钩子的库，旨在增强组件的功能性和开发效率。

- ⚓ **核心功能**：提供多样化的 React 自定义钩子，覆盖动画、浏览器 API、调试、事件处理等场景。  
- 🛠️ **开发工具**：包含性能优化（如防抖/节流）、生命周期日志、渲染计数等调试钩子。  
- 🌐 **浏览器集成**：支持地理位置、屏幕方向、网络状态、语音合成等浏览器 API 钩子。  
- 🖱️ **交互处理**：涵盖点击、悬停、长按、文件拖放等用户交互的钩子。  
- 📊 **状态管理**：提供数组、计数器、历史记录（如撤销/重做）、本地存储等状态管理工具。  
- 🎨 **UI 相关**：包含音视频控制、全屏、元素尺寸监测、视窗滚动等布局与媒体钩子。  
- 🔄 **实用工具**：提供 ref 合并、事件监听、定时器等辅助功能钩子。  
- 🧪 **实验特性**：如基于 Suspense 的电池状态和用户代理检测钩子。

---

### [简介 - viverse](https://pmndrs.github.io/viverse/getting-started/index)

**原文标题**: [Introduction - viverse](https://pmndrs.github.io/viverse/getting-started/index)

这是一个关于使用 Three.js 和 React Three Fiber 构建 VIVERSE 应用的开发工具包介绍。

- 📦 **工具包安装** - 通过 npm 安装 three、@react-three/fiber 和@react-three/viverse。
- 🎮 **示例原型** - 展示了一个包含<SimpleCharacter/>组件和默认模型的地图原型。
- 🌐� **代码示例** - 提供了使用 Sky、Canvas、Viverse 等组件的 React 代码示例。
- 🚀 **快速开始** - 建议具备 React、Three.js 和@react-three/fiber 基础，提供游戏构建、示例和教程链接。
- 🕹️ **教程主题** - 包括第一人称控制、AR/VR、角色装备、自定义动画和模型等。
- 🌐 **非 React 选项** - 提供使用 vanilla three.js 构建游戏的方案。
- 🙏 **致谢** - 感谢 Quaternius 的模型、kenney.nl 的纹理和 pixiv 团队的 three-vrm 项目。

---

### [VIVERSE - 通往沉浸式 3D 互联网的门户](https://www.viverse.com/)

**原文标题**: [VIVERSE - Your Portal to the Immersive 3D Internet](https://www.viverse.com/)

以下是按照您提供的模板总结的内容：

overview summary  
VIVERSE 是一个沉浸式 3D 内容平台，提供多样化的虚拟体验，包括游戏、艺术探索和社交空间。用户可以通过不同设备探索数字世界、创建个性化内容，并使用自定义头像表达自我。平台还支持创作者通过无代码或代码方式构建自己的虚拟空间，并优化了 3D 内容的流式传输技术。

- 🎨 **The Art Collector** - 通过四种不同艺术风格的画作拯救祖父，阻止反派抹去所有颜色的阴谋。  
- ⬡ **Platonic Frequency** - 探索几何发光乐园，激活祭坛开启超现实维度传送门。  
- ⚡ **Circuit Breaker** - 浏览器速通游戏，穿越障碍迷宫寻找最短时间。  
- 🌵 **Stranded At Saguaro Sands** - 沙漠小镇中揭开居民故事背后的秘密。  
- 🌌 **to the Limbs** - 混合游戏与音乐视频的 surreal 世界自由探索。  
- 🌊 **The Floods** - 半淹没城市中，反思环境崩溃的非线性空间诗篇。  
- 🌿 **Echos of Elsewhere** - 宁静浮岛世界中隐藏着未知观察者的梦境体验。  
- 📖 **Bib Goes Home Popup Adventure** - 帮助 Bib 回家的魔法立体书互动版本。  
- 🌸 **Bloom** - 夜间花园探索，发现深处的美丽秘密。  
- 🔶 **Club Mesh** - 以几何顶点、边和面为基础的彩色休闲空间。  
- 🏙️ **SECTOR-15** - 赛博朋克世界探索，充满隐藏彩蛋。  
- 🐱 **Pet Rescue: Venice** - 威尼斯运河中拯救猫咪的意大利风情冒险。  
- 🚀 **Ship Happens!** - 3025 年太空飞船谜题，工程师醒来发现全员失踪。  
- 🌐 **VIVERSE 核心功能**：  
  - 🕶️ **Worlds** - 多设备兼容的 3D 虚拟空间探索。  
  - 🛠️ **Create** - 无代码/代码创作工具实现个性化构建。  
  - 👤 **Avatar** - 高度自定义的虚拟形象系统。  
  - 📡 **Polygon Streaming** - 高性能 3D 内容即时传输技术。  
- ✨ **特色内容**：  
  - 化石奇观博物馆、中世纪大教堂、外星岛屿等多元场景。  
  - 合作体验、教程博客及创作者生态支持。

---

### [构建一个简单的游戏 - viverse](https://pmndrs.github.io/viverse/tutorials/simple-game)

**原文标题**: [Building a Simple Game - viverse](https://pmndrs.github.io/viverse/tutorials/simple-game)

本教程介绍了如何使用@react-three/viverse 创建一个简单的 3D 平台游戏，包括角色控制、跳跃机制、物理碰撞检测、平台关卡设计和重生系统。

- 🎮 使用@react-three/viverse 构建 3D 平台游戏，包含角色移动（WASD+ 鼠标视角）、跳跃和物理碰撞检测
- 🛠️ 开发环境准备：需安装 three、@react-three/fiber、@react-three/viverse 等依赖包
- 🖼️ 基础画布设置：配置 Canvas 组件，包含相机视角 (FOV 90) 和阴影效果
- 🌈 场景搭建：添加天空盒 (Sky 组件) 和基础光照 (方向光 + 环境光)
- 🧱 关卡设计：使用 PrototypeBox 创建不同颜色和大小的平台，形成跳跃路径
- 🏃 角色控制：引入 SimpleCharacter 组件实现 WASD 移动、鼠标视角和空格键跳跃
- ⚡ 重生系统：通过 useFrame 检测角色位置 (y<-10 时重置到起点)
- 👨💻 代码结构：主要组件包括 App.tsx(主入口) 和 Scene.tsx(游戏场景逻辑)
- 🚀 效果预览：最终游戏包含可探索的 3D 平台世界，具有完整的物理交互和失败重置机制

---

### [GitHub - pmndrs/viverse: ⟁ 为 VIVERSE 及其他平台构建 Three.js 和 React Three Fiber 应用的工具包](https://github.com/pmndrs/viverse)

**原文标题**: [GitHub - pmndrs/viverse: ⟁ Toolkit for building Three.js and React Three Fiber Apps for VIVERSE and beyond.](https://github.com/pmndrs/viverse)

pmndrs/viverse 是一个基于 Three.js 和 React Three Fiber 的工具包，专为 VIVERSE 及其他平台的应用开发设计。

- 🌟 **项目简介**: 提供构建 3D 应用的 React 组件和工具，支持 VIVERSE 平台。  
- 🛠️ **技术栈**: 基于 Three.js 和 React Three Fiber，需熟悉 React 和 Three.js。  
- 📦 **安装**: 通过 npm 安装 `three`、`@react-three/fiber` 和 `@react-three/viverse`。  
- 🎮 **功能示例**: 包含简单角色组件 (`SimpleCharacter`)、物理引擎 (`FixedBvhPhysicsBody`) 和原型模型 (`PrototypeBox`)。  
- 📚 **学习资源**: 提供教程（如第一人称控制、AR/VR 集成）和示例代码。  
- 🚀 **非 React 支持**: 支持纯 Three.js 开发（通过 `@pmndrs/viverse`）。  
- 🙏 **致谢**: 使用 Quaternius 的默认模型、kenney.nl 的纹理及开源项目 three-vrm 和 three-mesh-bvh。  
- 💡 **赞助**: 由 HTC Viverse 赞助开发。  
- 📜 **许可证**: 开源项目，可查看许可证详情。  
- ⚠️ **问题提示**: 页面加载错误时需刷新，部分功能需登录操作（如通知设置）。

---

### [发布 v6.5.0 · tinyplex/tinybase · GitHub](https://github.com/tinyplex/tinybase/releases/tag/v6.5.0)

**原文标题**: [Release v6.5.0 · tinyplex/tinybase · GitHub](https://github.com/tinyplex/tinybase/releases/tag/v6.5.0)

tinybase 发布了 v6.5.0 版本，新增了对 React Native MMKV 存储的支持。

- 🆕 新增 `persister-react-native-mmkv` 模块，支持通过 `react-native-mmkv` 库在 React Native 中持久化数据  
- 📱 使用示例展示了如何将 TinyBase 存储与 MMKV 集成  
- 👏 特别感谢贡献者 Jérémy Barbet 的这一新功能  
- 🔄 版本发布时出现加载错误提示，需重新加载页面  
- ⭐ 项目获得 4.6k 星标和 115 次 fork，显示其受欢迎程度  
- 🚀 社区成员对版本更新表示兴奋（火箭表情反应）

---

### [发布 v1.15.0 · TanStack/form · GitHub](https://github.com/TanStack/form/releases/tag/v1.15.0)

**原文标题**: [Release v1.15.0 · TanStack/form · GitHub](https://github.com/TanStack/form/releases/tag/v1.15.0)

TanStack Form 仓库的 v1.15.0 版本发布及错误提示页面  

- 🚨 页面加载错误提示，需重新加载页面  
- 🔍 仓库导航选项包括代码、问题、拉取请求等  
- 🏷️ 最新版本 v1.15.0 于 7 月 26 日发布  
- ✨ 新增功能：`react-form` 添加 `withFieldGroup`  
- 🔄 其他变更：同步仓库配置、依赖更新等  
- 📦 更新了多个框架的 Form 包（React、Angular、Solid 等）  
- 🎉 用户反应：2 人欢呼、1 人点赞、2 人表示支持

---

### [GitHub - irsyadadl/intentui: Intent UI 是一套轻松愉快的 React 组件集，基于 React Aria Components 和 Tailwind CSS 构建。易于定制，可直接复制粘贴到你的 React 项目中。](https://github.com/irsyadadl/intentui)

**原文标题**: [GitHub - irsyadadl/intentui: Intent UI is a chill set of React components, built on top of React Aria Components and Tailwind CSS. Easy to customize and just copy & paste into your React projects.](https://github.com/irsyadadl/intentui)

Intent UI 是一个基于 React Aria Components 和 Tailwind CSS 构建的 React 组件库，设计轻松易用，支持快速复制粘贴到 React 项目中。

- 🚀 **项目简介**：Intent UI 是一套基于 React Aria Components 和 Tailwind CSS 的 React 组件库，注重可访问性和易用性。  
- 📚 **文档与资源**：提供详细的文档和示例，可通过 [intentui.com](intentui.com) 查阅。  
- 🧩 **组件与模板**：包含预构建的组件和模板（Intent Blocks），支持快速设计和开发。  
- 🤝 **贡献指南**：欢迎社区贡献，提供贡献指南和开源协作支持。  
- 📜 **许可证**：采用 MIT 许可证，允许自由修改和共享。  
- ⭐ **项目数据**：获得 1.6k Stars 和 74 Forks，拥有活跃的开发者社区。  
- 🔧 **技术支持**：基于 TypeScript 和 Tailwind CSS，提供现代化的开发体验。

---

### [发布 10.27.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/10.27.0)

**原文标题**: [Release 10.27.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/10.27.0)

GitHub 上 Preact 项目的最新版本 10.27.0 发布，包含功能更新、错误修复及维护改进。

- 🚀 更新了`refcallback`类型以支持返回清理函数，并新增调试辅助导出 (#4860)  
- 🔧 修复了 Suspense hydration 边界抛出异常后的重新渲染问题 (#4856)  
- 📝 修改了`replaceNode`弃用注释，指向新 shim 文件 (#4844)  
- ⚡️ 减少了部分重复逻辑 (#4814, #4821)  
- 👥 贡献者：JoviDeCroock 和 rschristian  
- 🔖 版本发布时间：7 月 28 日，GPG 签名验证  
- ❗️ 页面加载时出现错误提示需刷新重试

---

### [GitHub - TypeCellOS/BlockNote: 基于块的 React 富文本编辑器（类似 Notion 风格），可扩展。构建于 Prosemirror 和 Tiptap 之上。](https://github.com/TypeCellOS/BlockNote)

**原文标题**: [GitHub - TypeCellOS/BlockNote: A React Rich Text Editor that's block-based (Notion style) and extensible. Built on top of Prosemirror and Tiptap.](https://github.com/TypeCellOS/BlockNote)

BlockNote 是一个基于块（类似 Notion 风格）且可扩展的 React 富文本编辑器，构建在 Prosemirror 和 Tiptap 之上，提供现代化的文本编辑体验。

- 🏠 **主页与文档**：项目主页为 [blocknotejs.org](https://www.blocknotejs.org/)，包含文档、快速入门指南和示例。  
- 🛠️ **功能特性**：支持动画占位符、拖拽块、嵌套/缩进、斜杠菜单、格式菜单及实时协作。  
- ⚡ **示例代码**：通过 `@blocknote/react` 和 `@blocknote/mantine` 可快速集成带样式的编辑器 UI。  
- 💬 **社区反馈**：鼓励用户通过 Discord 分享使用体验和建议。  
- 🤝 **开源贡献**：遵循 `CONTRIBUTING.md` 指南，使用 `pnpm start` 运行项目，测试基于 Vitest 和 Playwright。  
- 📜 **许可证**：核心代码采用 MPL-2.0 许可（允许商用），XL 包为 AGPL-3.0（需商业许可）。  
- ❤️ **致谢**：基于 Prosemirror 和 Tiptap 构建，获 NLNet 基金会赞助，托管于 Vercel。  
- 📊 **项目数据**：8.4k Stars、590 Forks、94 贡献者，主要语言为 TypeScript（89.1%）。

---

### [发布 v9.3.0 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.3.0)

**原文标题**: [Release v9.3.0 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.3.0)

react-three-fiber 发布了 v9.3.0 版本，包含重要修复和新功能。

- 🐛 **flushSync 修复**：修复了 `flushSync` 的工作机制，并新增示例支持通过 React props 截图 R3F 画布的最新状态，适用于视频或图像导出等高级场景。  
- 📱 **React Native 兼容性**：修复了与 React Native 0.79+ 及 Drei 的兼容性问题（感谢 @thejustinwalsh 的协助）。  
- ✨ **更新内容**：  
  - 导出 `flushSync`（#3551）  
  - 适配 RN 0.79 的深度导入（#3498）  
  - 新增 `flushSync` 示例（#3560）  
- 👋 **新贡献者**：欢迎 @s-pace 和 @huntie 首次提交代码。  
- 📜 **完整日志**：查看版本变更详情（v9.1.4...v9.3.0）。

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的命令行应用开发工具，允许开发者使用 React 组件构建交互式命令行界面。

- 🌈 Ink 是一个用于构建命令行应用的 React 渲染器，支持 Flexbox 布局。
- 🛠️ 提供类似 React 的开发体验，支持所有 React 特性。
- 📦 安装简单，通过 `npm install ink react` 即可开始使用。
- 📝 内置组件如 `<Text>`、`<Box>`、`<Newline>` 等，支持样式和布局控制。
- 🎮 提供多种钩子（Hooks）如 `useInput`、`useApp`、`useStdin` 等，用于处理用户输入和应用状态。
- 📊 支持静态输出（`<Static>`）和动态更新，适用于日志和任务列表等场景。
- 🔍 兼容 React Devtools，方便调试和开发。
- 🧪 提供测试支持，可使用 `ink-testing-library` 进行组件测试。
- 📚 包含丰富的示例和社区贡献的扩展组件，如输入框、进度条、表格等。

---

### [GitHub - glitternetwork/pinme：一键部署你的前端应用](https://github.com/glitternetwork/pinme)

**原文标题**: [GitHub - glitternetwork/pinme: Deploy Your Frontend in a Single Command](https://github.com/glitternetwork/pinme)

PinMe 是一个简单易用的命令行工具，用于将文件和目录上传到 IPFS 网络。

- 🌐 **功能概述**  
  - 🚀 快速上传文件和目录到 IPFS  
  - 📂 支持多种文件类型和大小  
  - 📊 查看和管理上传历史  
  - 🔗 自动生成可访问的 IPFS 链接  
  - 🌐 预览上传内容  

- 📥 **安装方式**  
  - ⚙️ 使用 npm：`npm install -g pinme`  
  - 🧶 使用 yarn：`yarn global add pinme`  

- 🛠️ **使用命令**  
  - 📤 上传文件或目录：`pinme upload [path]`  
  - 🗑️ 从 IPFS 删除文件：`pinme rm [hash]`  
  - 📜 查看上传历史：`pinme list` 或 `pinme ls`  
  - ❓ 获取帮助：`pinme help`  

- ⚠️ **上传限制**  
  - 📄 单文件大小限制：20MB  
  - 📁 目录总大小限制：500MB  

- 📍 **日志与配置**  
  - 🖥️ Linux/macOS：`~/.pinme/`  
  - 🪟 Windows：`%USERPROFILE%\.pinme\`  

- 📜 **许可证**  
  - ⚖️ MIT 许可证  

- 💡 **使用技巧**  
  - 🛠️ 上传 Vite 项目时，需在配置中添加 `base: "./"`  

- 📧 **联系我们**  
  - 📮 GitHub Issues：[链接](https://github.com/glitternetwork/pinme/issues)  
  - ✉️ 邮箱：pinme@glitterprotocol.io  

- 🌟 **开发团队**  
  - 👥 由 Glitter Protocol 团队开发和维护

---

### [KeyLines - JavaScript 开发者的图可视化 SDK](https://cambridge-intelligence.com/keylines/?utm_campaign=16812718-React%20Status%20newsletter%20ad&utm_source=NewsletterAd&utm_medium=SponsoredLink)

**原文标题**: [
		KeyLines - The Graph Visualization SDK for JavaScript Developers	](https://cambridge-intelligence.com/keylines/?utm_campaign=16812718-React%20Status%20newsletter%20ad&utm_source=NewsletterAd&utm_medium=SponsoredLink)

KeyLines 是一款专为 JavaScript 开发者设计的图可视化工具包，帮助用户快速构建强大、美观且交互性强的图可视化应用。

- 🚀 **快速开发**：KeyLines 提供清晰的教程、演示和 API 文档，支持开发者快速上手并构建应用。  
- 🌐 **跨平台兼容**：适配任何浏览器、设备、服务器或数据库，确保广泛的应用场景。  
- ⚡ **高性能引擎**：基于 HTML5 和 WebGL 技术，提供流畅且高效的图可视化体验。  
- 📊 **多功能分析**：支持时间序列分析、地理空间分析、社交网络分析及自动布局等高级功能。  
- 🔗 **无缝集成**：可轻松嵌入其他工具，并支持多种数据库集成，便于部署和共享。  
- 🤝 **专业支持**：提供从入门指导到深度技术支持的全程服务，确保项目顺利推进。  
- 🌍 **全球认可**：客户覆盖六大洲，包括初创企业、财富 500 强公司和政府机构。  
- 📚 **资源丰富**：提供白皮书下载、博客文章及客户案例，助力用户深入探索图可视化技术。

---

### [过去十年中众多、众多、众多的 JavaScript 运行时 • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

**原文标题**: [The many, many, many JavaScript runtimes of the last decade • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

过去十年中，JavaScript 运行时和引擎的多样化发展使其能够适应各种场景，从云端到边缘计算、微控制器、多语言互操作引擎，再到原生应用开发。以下是关键点的总结：

- 🌐 **边缘计算**：自 2016 年 Cloudflare Workers 推出后，JavaScript 在边缘计算领域迅速崛起，引发 Deno、Bun、WinterJS 等竞品涌现，引擎选择也从 V8 扩展到 JavaScriptCore、SpiderMonkey 等。
- 🔌 **微控制器**：为适应极低资源环境（如 RAM 仅几 KB），出现了 Duktape、JerryScript 等轻量引擎，支持 IoT 设备运行 JavaScript。
- 🏗️ **多语言引擎**：通过 JVM（Graal.js）、.NET（jint）、Python 等宿主语言实现 JavaScript 引擎，支持双向互操作，凸显生态灵活性。
- 📱 **原生应用**：
  - **Web 视图框架**：Cordova（移动）、Electron（桌面）主导跨平台开发，React Native 凭借 Hermes 引擎和 JSI 接口成为移动端主流（30% 顶级 iOS 应用采用）。
  - **Smart TV**：基于 Web 技术或 React Native 的解决方案覆盖亿级设备，如 HbbTV、Android TV 等。
- 🔄 **Node.js 的扩展**：通过 Node-API 支持多引擎（V8、JSC 等），但移动端渗透有限，桌面端仍依赖 Electron。
- 🏆 **竞争与多样化**：不同场景优化目标（启动速度、内存占用等）催生专用运行时，如 QuickJS（低延迟）、Hermes（移动 AOT 编译），打破 V8/JSC 垄断。

总结来看，JavaScript 凭借生态优势和语言灵活性，已渗透几乎所有计算领域，但碎片化场景注定“一刀切”的运行时无法存在。未来，引擎创新（如 Static Hermes）和标准化（如 Node-API）将继续推动其边界扩展。

（注：原文还提及 WASM、穿戴设备等未深入方向，以及 Lynx、LibWeb 等新运行时，因篇幅限制未纳入摘要。）

---

### [ES 工具包](https://es-toolkit.dev/)

**原文标题**: [es-toolkit](https://es-toolkit.dev/)

最佳性能  
es-toolkit 在现代 JavaScript 运行时中的性能比其他库高出 2-3 倍。  

- 🚀 **性能优势** - es-toolkit 在现代 JavaScript 运行时中表现卓越，性能是其他库的 2-3 倍。  
- ⚡ **高效运行** - 专为优化现代 JavaScript 环境设计，确保更快的执行速度。  
- 📊 **显著提升** - 与其他库相比，性能提升显著，适合高性能需求的应用场景。

---

### [Zod 对决 Valibot：JS/TS 验证器之战！- YouTube](https://www.youtube.com/watch?v=6P-2urhScwk)

**原文标题**: [Zod VS Valibot: JS/TS Validator Battle! - YouTube](https://www.youtube.com/watch?v=6P-2urhScwk)

关于 YouTube 平台的相关信息与资源  
- 📢 关于：了解 YouTube 的基本信息和背景  
- 🗞️ 新闻：获取 YouTube 的最新动态和公告  
- ©️ 版权：版权相关信息和政策  
- 📩 联系我们：与 YouTube 取得联系的方式  
- 🎨 创作者：为内容创作者提供的资源和支持  
- 💼 广告：广告合作和推广机会  
- 💻 开发者：开发者工具和资源  
- 📜 条款：平台使用条款和条件  
- 🔒 隐私：隐私政策和数据保护措施  
- ⚖️ 政策与安全：平台规则和安全指南  
- 🔧 YouTube 工作原理：平台运作机制解析  
- 🧪 测试新功能：体验和反馈最新功能  
- © 2025 Google LLC：版权归属和年份声明

---

### [GitHub - huggingface/transformers.js：面向网页的尖端机器学习。直接在浏览器中运行🤗 Transformers，无需服务器！](https://github.com/huggingface/transformers.js)

**原文标题**: [GitHub - huggingface/transformers.js: State-of-the-art Machine Learning for the web. Run 🤗 Transformers directly in your browser, with no need for a server!](https://github.com/huggingface/transformers.js)

Transformers.js 是一个基于浏览器的机器学习库，可直接在浏览器中运行 🤗 Transformers 模型，无需服务器支持。

- 🌐 **浏览器运行**：直接在浏览器中运行，无需服务器支持，使用 ONNX Runtime 进行模型推理。
- 🔧 **功能丰富**：支持多种任务，包括自然语言处理、计算机视觉、音频处理和多模态任务。
- 📥 **安装简单**：通过 NPM 或 CDN 快速安装，支持 ES Modules。
- 🚀 **快速上手**：提供与 Python 库类似的 `pipeline` API，易于迁移现有代码。
- ⚙️ **硬件加速**：支持 CPU（WASM）和 GPU（WebGPU）运行，优化性能。
- 📊 **量化支持**：提供模型量化选项（如 fp32、fp16、q8、q4），优化资源使用。
- 📚 **丰富示例**：提供多种示例应用，如语音识别、图像搜索、翻译等。
- 🔄 **模型转换**：支持将 PyTorch、TensorFlow 或 JAX 模型转换为 ONNX 格式。
- 📜 **详细文档**：提供完整的 API 参考和任务支持列表。

---

### [发布 3.7.0 版 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.7.0)

**原文标题**: [Release 3.7.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.7.0)

Transformers.js 发布了 3.7.0 版本，新增了对 Voxtral、LFM2 和 ModernBERT Decoder 三种新模型架构的支持，并包含其他改进。

- 🚀 **新模型支持**  
  - 新增 Voxtral、LFM2 和 ModernBERT Decoder 三种架构。  

- 🎙️ **Voxtral 模型**  
  - 基于 Ministral 3B 增强，支持音频输入，擅长语音转录、翻译和音频理解。  
  - 提供 ONNX 权重和在线演示。  

- ⚡ **LFM2 模型**  
  - 由 Liquid AI 开发，专为边缘 AI 和本地部署设计，提供 350M、700M 和 1.2B 三种参数规模。  

- 📊 **ModernBERT Decoder**  
  - 属于 Ettin 套件，提供编码器和解码器架构的公平比较，支持多种规模模型。  

- 🛠️ **其他改进**  
  - 在文本生成管道中添加了特殊令牌支持。  
  - 完整更新日志可查看 3.6.3 到 3.7.0 的变更。

---

### [流体计算：我们如何构建无服务器服务器 - Vercel](https://vercel.com/blog/fluid-how-we-built-serverless-servers)

**原文标题**: [Fluid compute: How we built serverless servers - Vercel](https://vercel.com/blog/fluid-how-we-built-serverless-servers)

概述：Vercel 推出的 Fluid compute 技术通过优化服务器资源使用、减少冷启动时间并显著降低成本，结合 Active CPU 定价模式，已实现每周处理超过 450 亿次请求，为客户节省高达 95% 的成本。该技术基于 React Server Components 和 Next.js App Router 构建，通过创新的传输协议和系统架构，实现了高效的资源利用和成本节约。

- 🚀 Fluid compute 技术优化服务器资源使用，减少冷启动时间，显著降低成本。
- 💡 基于 React Server Components 和 Next.js App Router 构建，支持 HTTP 流式传输。
- 🔄 创新传输协议：通过 TCP 隧道连接 Vercel 和 AWS Lambda，实现高效数据传输。
- 🏗️ 系统架构：使用 Rust 核心作为基础设施和用户代码之间的桥梁，支持多种功能扩展。
- 🔄 多路复用：通过 compute-resolver 服务实现请求路由优化，提高资源利用率。
- ⚙️ 健康监控：实时监控函数实例资源使用情况，确保性能和稳定性。
- 💰 Active CPU 定价：按实际使用的 CPU 时间和内存计费，进一步降低成本。
- 📈 成效：75% 的 Vercel Function 调用使用 Fluid compute，节省高达 95% 的成本。

---

### [谷歌在线安全博客：推出 OSS Rebuild 项目——开源重建，持久稳固](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html)

**原文标题**: [
Google Online Security Blog: Introducing OSS Rebuild: Open Source, Rebuilt to Last
](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html)

Google 宣布推出 OSS Rebuild 项目，旨在通过重建上游开源软件包来增强对开源生态系统的信任，应对供应链攻击的威胁。该项目提供自动化工具、SLSA 认证和构建可观测性功能，支持 PyPI、npm 和 Crates.io 等主流软件包仓库。

- 🛡️ **项目目标**：通过独立重建开源软件包，提供安全元数据，增强供应链透明度，无需维护者额外操作。  
- 🔧 **核心功能**：自动化构建定义生成、SLSA Build Level 3 认证、构建验证工具及可自托管的基础设施。  
- 🌍 **行业背景**：开源软件占现代应用的 77%，价值超 12 万亿美元，但频繁成为供应链攻击目标（如 xz-utils 事件）。  
- 🔍 **安全检测**：识别未提交的源代码、构建环境篡改和隐蔽后门等攻击，并支持动态分析异常行为。  
- 📦 **多生态支持**：初始覆盖 Python（PyPI）、JavaScript/TypeScript（npm）和 Rust（Crates.io）生态。  
- 🤖 **AI 辅助**：利用自然语言处理和 AI 模型解析复杂构建文档，提升自动化重建效率。  
- 🛠️ **用户价值**：企业可增强 SBOM、加速漏洞响应；维护者能提升历史包的可信度并简化 CI 安全负担。  
- 📥 **快速体验**：提供 Go 命令行工具，支持查询 SLSA 认证、列出重建版本或本地重建软件包。  
- 🤝 **社区参与**：鼓励开发者、企业和安全研究者通过 GitHub 贡献代码或反馈，共同提升开源安全。  

（注：原文中部分技术细节和案例已浓缩，如 SLSA 框架、具体攻击事件等，保留核心逻辑与用户价值。）

---

