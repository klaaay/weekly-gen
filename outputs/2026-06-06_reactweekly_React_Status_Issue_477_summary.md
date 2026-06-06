### [指挥家重写：他们为提速所做的改动](https://performance.dev/the-conductor-rewrite)

**原文标题**: [The Conductor Rewrite:
What They Changed to Make It Fast](https://performance.dev/the-conductor-rewrite)

概述总结  
Conductor团队通过全面重写，将应用速度提升了一倍，核心优化包括技术栈迁移、渲染性能改进和架构调整。  

- 🔄 从react-router迁移到@tanstack/react-router，解决了导航时组件不必要的重渲染问题  
- ⚡ 使用react-virtuoso实现聊天列表虚拟化，仅渲染视口内的消息，大幅减少DOM操作  
- 🗂️ 采用SQLite作为本地数据源，消除网络延迟，实现真正的本地优先架构  
- 🖥️ 选择Tauri而非Electron，利用原生WebKit webview获得更快的冷启动和更小的包体积  
- 🧠 将代理进程运行时从Node切换到Bun，减少150MB包体积并提升启动速度  
- 🔍 通过桥接Chrome DevTools解决Tauri中React性能分析难题，精准定位瓶颈  
- 💾 空闲代理进程自动关闭并支持按需恢复，优化内存管理  
- ⏱️ 将检查点操作移出关键路径，确保用户按下回车后立即获得首个token响应  
- 🛠️ 采用React.memo和稳定引用减少不必要的重渲染，提升整体流畅度

---

### [线性回归为何如此快速？技术解析](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

**原文标题**: [How's Linear so fast? A technical breakdown](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

本文深入分析了Linear应用为何如此快速，揭示了其从架构到细节的全面优化策略。

- 🚀 **浏览器即数据库**：Linear将IndexedDB作为本地数据库，UI直接读取本地数据，避免网络请求延迟，实现即时响应。
- ⚡ **乐观更新**：所有变更先本地应用，再异步同步到服务器，用户无需等待网络，体验流畅无卡顿。
- 📦 **极致代码拆分**：通过多次重构构建工具，将21MB的JS拆分为数百个按需加载的chunk，并利用`modulepreload`并行预加载，大幅提升首屏速度。
- 🔄 **同步引擎三支柱**：本地数据已存在、变更不等待网络、增量更新只影响单个单元格，确保操作即时且高效。
- 🎨 **设计驱动速度**：键盘快捷键、全局命令面板（⌘K）等设计，缩短用户操作路径，让交互本身更快速。
- 🖥️ **动画性能优化**：仅使用`transform`和`opacity`等GPU加速属性，避免布局触发，且动画时长极短（如0.1s），保持界面丝滑。
- 🔐 **渲染优先于认证**：首屏直接渲染本地缓存内容，认证在后台异步验证，避免等待登录流程。
- 💡 **简单技术栈**：基于React、MobX、Postgres等基础技术，无复杂框架，强调客户端渲染的简洁与高效。

---

### [[编译器] 将React编译器移植到Rust —— 作者：josephsavona · 拉取请求 #36173 · facebook/react · GitHub](https://github.com/facebook/react/pull/36173#issuecomment-4608356402)

**原文标题**: [[compiler] Port React Compiler to Rust by josephsavona · Pull Request #36173 · facebook/react · GitHub](https://github.com/facebook/react/pull/36173#issuecomment-4608356402)

React 编译器正在被移植到 Rust，这是一个实验性的工作，旨在提升性能和集成能力。

- 🚀 **性能提升显著**：Rust 版本作为 Babel 插件运行时速度提升 3 倍，实际转换逻辑快约 10 倍，在 Meta 内部测试中后端性能提升 25%。
- ✅ **高兼容性与正确性**：所有 1725 个测试用例均通过，与 TypeScript 版本输出一致，Meta 99.9% 的代码库输出相同，剩余差异为改进或 bug 修复。
- 🧩 **多工具集成**：已提供 Babel、OXC 和 SWC 三种集成方式，并计划未来支持更多工具，如 Biome。
- 🛠️ **架构与设计**：内部使用与 TS 版本相同的架构（HIR、CFG、SSA），但采用 arena 结构适配 Rust 的借用系统；公共 API 基于 Rust 表示的 Babel AST。
- 🧪 **测试与验证**：提供多种测试脚本，包括详细对比每个编译 pass 内部状态的测试，确保逻辑一致性。
- 🔮 **未来计划**：计划将输出从替换整个程序改为返回补丁；优化 AST 表示和字符串处理；实现自己的作用域解析；并计划将 crate 发布到 crates.io。

---

### [Next.js + Supabase 全栈可观测性 | Sentry 博客](https://blog.sentry.io/nextjs-supabase-observability/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-evergreen&utm_content=newsletter-primary-supabase-nextjs-blog-learnmore)

**原文标题**: [Full-stack observability for Next.js + Supabase | Sentry Blog](https://blog.sentry.io/nextjs-supabase-observability/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-evergreen&utm_content=newsletter-primary-supabase-nextjs-blog-learnmore)

### 概述摘要
本文介绍了如何为使用 Next.js 和 Supabase 构建的应用实现生产级可观测性，通过集成 Sentry 来弥合 Supabase 内置监控的局限性，从而实现全栈分布式追踪、自动问题检测和 AI 辅助修复。

- 📊 **Supabase 内置监控的局限**：Supabase 提供查询性能、RLS 建议和日志，但无法追踪跨全栈（如从 Next.js 前端到 Postgres）的请求链路。
- 🔗 **连接 Supabase 日志到 Sentry**：通过日志导出功能将 Supabase 日志导入 Sentry，并建议单独项目存储，以便关联基础设施日志与应用层追踪。
- 🛠️ **正确配置 Next.js 和 Edge Functions**：Next.js 和 Deno 运行时需分别设置 Sentry 项目和 SDK，并集成 Supabase 客户端以自动记录数据库查询为命名跨度。
- 🤖 **自动检测 N+1 查询和性能问题**：Sentry 可自动识别 N+1 查询、慢跨度及 Web 核心指标（LCP、INP、CLS），无需手动配置。
- 📝 **指导 AI 代理正确配置**：使用 MCP（模型上下文协议）服务器获取实时配置，并通过技能文件（如 `.claude/`）提供项目特定上下文，避免代理生成过时配置。
- 📈 **超越错误的监控**：利用日志监控（如连接数下降）和动态告警（异常检测），并通过 Sentry CLI 快速构建自定义仪表板。
- 🤯 **Seer：从告警到修复**：Sentry 的 AI 调试器 Seer 可自动分析问题根因，甚至生成修复 PR，结合 Supabase MCP 可将安全建议转化为可追踪问题。
- 🚀 **快速入门三步**：运行 `npx sentry@latest init` 检测 Next.js 应用，添加 Supabase 集成获取查询级跨度，设置日志导出到独立 Sentry 项目，最后连接仓库启用 Seer 自动修复。

---

### [使用 TanStack Start 构建应用 | Lovable](https://lovable.dev/blog/building-apps-using-tanstack-start)

**原文标题**: [Building apps using TanStack Start | Lovable](https://lovable.dev/blog/building-apps-using-tanstack-start)

Lovable 平台已将其应用构建框架从 React + Vite（客户端渲染）升级为 TanStack Start（服务端渲染），以提升性能和 SEO。

- 🚀 **新框架核心**：新项目默认使用 TanStack Start，支持服务端渲染 (SSR)、静态站点生成 (SSG) 和客户端渲染 (CSR)，无需手动配置。
- ⚙️ **技术栈对比**：旧栈使用 Vite + React Router 和静态托管；新栈采用 TanStack Start、Cloudflare Workers，并集成了服务端函数。
- 🧩 **选择 TanStack Start 的原因**：它基于 React、开源、可独立部署、支持 SSR，并由成熟的团队维护，同时提供强大的类型系统，便于 AI 生成代码。
- 📈 **SEO 显著提升**：SSR 使页面内容直接包含在 HTML 中，对爬虫更友好，现有应用通过预渲染已实现有机搜索流量增长 2.9%，AI 工具流量增长 98.5%。
- 🛠️ **代码执行模型**：`createServerFn` 允许在组件文件中编写服务端逻辑，构建过程自动处理客户端/服务端分离，简化了开发流程。
- 🚢 **发布流程不变**：发布操作与之前相同，但后台构建的是服务端渲染的应用，并自动预生成静态路由，部署为边缘 Worker。
- 🔐 **密钥管理优化**：服务端密钥独立于代码包存储，作为绑定注入，可即时轮换，无需重新构建或部署。
- 🤖 **AI 适配新框架**：Lovable 的 AI 已通过注入 TanStack 特定规则，学习并生成符合新框架模式的代码，确保准确性。
- 🎯 **对现有项目的影响**：现有项目无需迁移，仍正常运行，并已从预渲染中受益。未来将逐步为新旧项目提供更多新栈功能。

---

### [GitHub 注册表 - shadcn/ui](https://ui.shadcn.com/docs/registry/github)

**原文标题**: [GitHub Registries - shadcn/ui](https://ui.shadcn.com/docs/registry/github)

本指南介绍了如何将任何公开 GitHub 仓库转变为 shadcn 注册表，以分发组件、配置、文档等文件。

- 📝 **核心概念**：将 `registry.json` 文件添加到公开 GitHub 仓库的根目录，描述要共享的文件，用户即可通过 `shadcn` CLI 安装。
- 📦 **分发任意文件**：注册表项不限于组件或 React 代码，可包含源文件、配置、文档、模板、工作流、规则等。
- ✅ **使用场景**：适合已有公开仓库、希望用户通过 `owner/repo/item` 直接安装、分发配置文件或规则等场景。
- 🔧 **要求**：必须是公开的 `github.com` 仓库，根目录有 `registry.json`，且遵循有效 schema。
- 📝 **步骤**：添加 `registry.json` → 定义文件（支持 `target` 指定目标路径）→ 验证注册表 → 列出/搜索/查看项目。
- 🧩 **组织方式**：使用 `include` 字段将嵌套的 `registry.json` 文件合并到根注册表，保持项目定义靠近源文件。
- 🔗 **依赖管理**：通过 `registryDependencies` 支持同一仓库或外部注册表的依赖，并可指定 ref（分支、标签或提交 SHA）锁定版本。
- 💻 **CLI 命令**：提供 `list`、`search`、`view`、`add`、`registry validate` 等命令，支持 `--dry-run`、`--diff`、`--view` 预览安装。
- 🔒 **安全建议**：安装前审查仓库和 `registry.json`，优先使用固定 ref（如完整 40 字符 SHA），使用 `view` 和 `--dry-run` 检查内容。

---

### [安全公告 · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/security/advisories)

**原文标题**: [Security Advisories · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/security/advisories)

该页面展示了 remix-run/react-router 项目的安全公告列表，涵盖了多个已发布的安全漏洞。

- 🔒 项目安全概览：包含安全策略、漏洞报告和公告查看功能
- ⚠️ 共列出10个安全公告，严重程度从低到高不等
- 🚨 最高严重级别为High，涉及RCE、XSS、DoS等漏洞
- 📅 所有公告发布于2026年1月至6月期间
- 🛡️ 漏洞类型包括CSRF、XSS、开放重定向、DoS和RCE
- 👤 所有漏洞均由brophdawg11报告
- 🔢 公告分页显示，当前为第1页，共2页
- 📊 项目拥有56.4k星标和10.9k分支，社区活跃

---

### [VoidZero 加入 Cloudflare](https://blog.cloudflare.com/voidzero-joins-cloudflare/)

**原文标题**: [VoidZero is joining Cloudflare](https://blog.cloudflare.com/voidzero-joins-cloudflare/)

### 概述总结
VoidZero 团队（包括 Vite、Vitest、Rolldown、Oxc 和 Vite+ 的创建者）正式加入 Cloudflare，所有项目保持开源、供应商中立和社区驱动。Cloudflare 承诺投入 100 万美元支持 Vite 生态系统，并计划将自身工具链迁移至 Vite 之上，同时推动 Vite 成为全栈应用和 AI 代理的通用基础。

- 🚀 **核心不变**：Vite 等所有项目保持 MIT 开源、供应商中立、社区驱动，Evan You 团队继续领导开发。
- 💰 **资金支持**：Cloudflare 承诺 100 万美元 Vite 生态系统基金，用于支持维护者和贡献者。
- 🔗 **生态基础**：Vite 已成为 Vue、SvelteKit、Nuxt、Astro、Next.js 等众多框架的共享基础，Cloudflare 将强化其中立性。
- 🤖 **AI 驱动**：Vite 因快速反馈循环（构建、测试、格式化）成为 AI 生成代码的默认工具链，VoidZero 工具链（Oxc、Oxlint 等）专为代理优化。
- 🛠️ **技术整合**：Cloudflare 将把自身 CLI（如 `cf`）迁移至 Vite 之上，实现 `cf dev` 作为 `vite dev` 的超集，提供原生部署体验。
- 🌐 **全栈演进**：Vite 将新增供应商中立的原语（后端、API、代理、部署钩子），支持全栈应用和 AI 代理，Cloudflare 提供一流实现。
- 📈 **增长数据**：Vite 周下载量达 1.29 亿，Cloudflare Vite 插件周下载量近 1400 万（占 Vite 的 10%+）。
- 🔓 **开源承诺**：Void 平台未来将开源，供社区学习并构建自己的平台。
- 🏢 **团队加入**：VoidZero 全体成员加入 Cloudflare，继续领导项目开发，Cloudflare 投入工程资源而非重定向。
- ⚡ **现有协作**：Vite Environment API 已支持非 Node.js 运行时（如 workerd），Cloudflare 插件已实现本地模拟生产环境。

---

### [17个TanStack项目齐聚一个应用！- YouTube](https://www.youtube.com/watch?v=J4kzovOTNKw)

**原文标题**: [All 17 TanStack Projects In ONE App! - YouTube](https://www.youtube.com/watch?v=J4kzovOTNKw)

本頁面為 YouTube 的資訊與政策總覽，涵蓋版權、條款、私隱及開發者資源等核心內容。
- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：規範內容使用與版權保護機制
- 📞 聯絡我們：提供用戶與創作者聯繫管道
- 🎬 創作者：專為內容創作者設計的資源與支援
- 📢 刊登廣告：說明廣告合作與收益模式
- 💻 開發人員：提供 API 與技術開發工具
- 📜 條款：明確用戶使用平台的規則與義務
- 🔒 私隱：保護用戶個人資料的相關政策
- 🛡️ 政策及安全：確保平台內容合規與用戶安全
- ⚙️ YouTube 的運作方式：解釋平台推薦與審核機制
- 🧪 測試新功能：介紹平台正在實驗的新功能
- ©️ 2026 Google LLC：版權歸屬與法律聲明

---

### [关于Sourcemaps你需要知道的一切 — Neciu Dan](https://neciudan.dev/everything-you-need-to-know-about-sourcemaps)

**原文标题**: [Everything you need to know about Sourcemaps — Neciu Dan](https://neciudan.dev/everything-you-need-to-know-about-sourcemaps)

概述摘要
本文详细介绍了Sourcemaps的工作原理、安全风险以及如何防止源代码泄露。

- 🔍 Sourcemaps是什么：一个JSON文件，将压缩后的代码映射回原始文件、行、列和变量名，包含sources、sourcesContent、names和mappings等关键字段。
- ⚙️ 正向转换流程：TypeScript代码先编译为JavaScript，再经过压缩器重命名变量、删除空格，最终生成一行难以阅读的生产代码。
- 🔄 反向映射机制：浏览器通过sourcemap的mappings表解码VLQ段，将压缩代码位置还原为原始代码，便于调试。
- ⚠️ 安全风险：默认情况下，sourcemaps会内嵌原始源代码（sourcesContent），若公开部署，任何人都能通过.map文件完全还原代码库。
- 🍎 Apple案例（2025年11月）：苹果因生产环境启用sourcemaps，导致新Web App Store的完整源代码被泄露，并被Chrome扩展重建。
- 🐜 Anthropic案例（2026年3月）：Claude Code的npm包因未排除.map文件，泄露了1900个文件、51.2万行TypeScript代码，且因包缓存永久暴露。
- 🛡️ 防护措施：禁用生产环境sourcemap生成；若需用于错误追踪，使用hidden模式并仅上传到监控工具；服务器返回404拦截.map请求；部署前检查网络面板或npm包tarball。
- 🤖 自动化检查：在CI/CD中集成脚本（如check-sourcemaps.mjs），扫描dist目录中内嵌sourcesContent的.map文件，构建失败时阻止部署。
- 💡 关键教训：两大公司均有安全团队，但因手动配置疏忽导致泄露；唯一可靠防护是自动化检查，在构建或部署阶段自动拦截问题。

---

### [适用于任何规模的时间序列工作负载的Postgres | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

### 概述总结  
Timescale 的 Tiger Cloud 提供专为时间序列工作负载优化的 Postgres 服务，支持每秒处理 3 万亿指标、3 PB 数据和 1 千万亿数据点，具备弹性扩展、高可用性和企业级合规性。

- 🚀 **弹性扩展**：通过最多 10 个节点的副本集分离读写，结合分层 SSD/S3 存储实现无限且经济高效的扩展。  
- 💰 **避免闲置成本**：计算与存储分离，可独立扩展，优化性能与成本，无需过度配置。  
- 🔒 **高可用性**：多可用区集群，支持自动故障转移、时间点恢复和跨区域备份。  
- 🏢 **企业级合规**：符合 SOC 2、HIPAA、GDPR 标准，提供始终加密、SSO 集成、RBAC 和审计日志。  
- 📊 **深度可观测性**：查询钻取和仪表盘提供性能与错误可见性，支持集成 CloudWatch、Datadog、Prometheus 等工具。  
- ⚡ **快速部署**：数分钟内完成数据库配置，支持通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。  
- 🔌 **即插即用**：默认企业就绪，支持合同级 SLA、区域数据隔离和 24/7 全球专家支持。

---

### [React服务端组件的组件架构 | Aurora Scharff](https://aurorascharff.no/posts/component-architecture-for-react-server-components/)

**原文标题**: [Component Architecture for React Server Components | Aurora Scharff](https://aurorascharff.no/posts/component-architecture-for-react-server-components/)

### 概述总结
本文探讨了从传统数据获取模式（useEffect、React Query、路由加载器）向React Server Components（RSC）架构的演进，强调了通过组件自包含数据获取和Suspense边界设计加载体验的优势，最终实现更易维护、可组合的代码库。

- 📜 **传统数据获取的痛点**：useEffect和React Query导致客户端数据获取延迟，组件耦合度高，易产生“爆米花UI”（内容随机弹出）。
- 🔗 **路由加载器的局限**：虽然将数据获取移至服务端，但组件与路由加载器强耦合，复用需重复获取数据并传递props，增加维护成本。
- 🚀 **RSC的核心优势**：组件可异步获取自身数据（服务端执行），无需加载器传递props，实现自包含与高复用性，同时利用`cache()`避免重复请求。
- 🧩 **Suspense与加载设计**：通过Suspense边界和骨架屏（与组件同文件导出）控制加载顺序，避免布局偏移，提升用户体验。
- ⚡ **参数化页面与交互性**：使用`.then()`处理异步参数（如`params`），保持页面同步；客户端组件（如点赞按钮）通过Server Functions和`useOptimistic`实现即时反馈。
- 🗂️ **代码组织原则**：按功能分组组件（如`features/post/`），组件仅接收最小props（如ID），便于跨页面复用。
- 🎯 **总结原则**：页面作为同步组合器（不获取数据）、异步组件自获取数据、骨架屏与组件共存、Suspense边界由页面控制、客户端边界尽量下沉。

---

### [告别世博会 | 埃文·培根](https://evanbacon.dev/blog/expo)

**原文标题**: [Farewell Expo | Evan Bacon](https://evanbacon.dev/blog/expo)

概述总结
在Expo工作的九年里，我从一名青少年爱好者成长为团队领导者，学到了许多宝贵经验。以下是我在构建Expo过程中领悟的关键要点。

- 🚀 成为产品最大的粉丝：持续使用自己的产品，感受每一个粗糙的边缘，并不断优化用户体验。将"不可逆"决策转变为可快速撤销的决策，消除摩擦。
- 👂 倾听请求背后的真正需求：人们通常知道问题所在，但难以准确描述解决方案。不要盲目接受所有请求，而是深入理解他们真正需要的东西，从根本上解决问题。
- 🤝 建立开发者信任：通过诚实、开放地构建，并持续不断地出现来赢得开发者信任。竞争对手可以复制你的代码，但无法复制多年不辜负用户的承诺。
- 📊 数据驱动决策：收集正确的数据来了解产品实际使用情况，发现"无聊"功能的重要性，并识别增长机会。数据也能解决团队内部的争论，推动决策。
- ⏰ 注意力是你最宝贵的资源：通过解决最复杂的问题来吸引优秀人才，形成良性循环。保持健康（阳光、水分、锻炼）能显著提升招聘效果，因为人际交往需要最佳状态。

---

### [我们如何通过删除CMS将构建时间缩短三分之二 | Sentry博客](https://blog.sentry.io/cut-build-times-delete-cms/)

**原文标题**: [How we cut build times by two-thirds by deleting our CMS | Sentry Blog](https://blog.sentry.io/cut-build-times-delete-cms/)

### 概述总结
Sentry 团队通过将传统无头CMS替换为Astro、Markdown和AI驱动的自动化，成功将构建时间缩短三分之二，并大幅提升了网站可靠性和开发效率。

- 🚀 **核心问题**：旧有Gatsby + 无头CMS架构导致构建时间长（约14分钟/次）、CMS模式受限、外部API频繁故障（每日3-5次插件失败）。
- 💡 **解决方案**：迁移至Astro框架，使用Markdown和Frontmatter管理内容，并集成Claude Skills实现AI原生内容管理，消除对CMS的依赖。
- ⏱️ **显著成果**：构建时间从14分钟降至4分钟以下，每日节省约15.8小时构建时间；Web Vitals评分从89提升至97；故障减少95%。
- 🤖 **AI驱动流程**：利用Claude Code进行编码、Playwright和DOM Inspector MCP进行视觉回归测试，以及自定义Claude技能实现非技术人员的内容更新（如创建分支、本地预览、自动PR）。
- 🛠️ **关键优化**：通过Vercel Blob存储表单字段解决API限流问题；使用PreToolUse钩子保护敏感配置（如CSP）；压缩图片至250KB以下提升性能。
- 🏆 **文化契合**：将内容作为代码管理（版本控制、代码审查），符合Sentry的开发者优先文化，并实现无限内容模式和无外部依赖。

---

### [v1.4.0 | React Spectrum](https://react-spectrum.adobe.com/releases/v1-4-0)

**原文标题**: [v1.4.0 | React Spectrum](https://react-spectrum.adobe.com/releases/v1-4-0)

v1.4.0 版本发布，带来多项新功能和改进，包括拖放支持、新组件和测试工具 RC 版本。

- 📦 新增 ListView、TableView 和 TreeView 的拖放支持
- ✨ TableView 新增高亮选择和 TableFooter 组件
- 🏷️ ComboBox、TextField 等表单组件支持自定义前缀，新增 LabeledValue 组件
- ✅ Checkbox、Radio、Switch 可配置描述和错误消息
- 📅 Calendar 支持多日期选择
- 🧪 测试工具升级至 RC 版本，API 一致性和破坏性变更，提供迁移 codemod
- 🔧 通用改进：添加 pressScale 属性文档，提升代理技能
- 🎨 Button 更新文本颜色对比度
- 🗓️ Calendar 支持 selectionMode="multiple" 和 anchorDate 参数
- ⚙️ 修复集合中假值键处理，允许非对象值作为 items
- 🖱️ 优化 ComboBox、Menu、Picker 的悬停过渡效果
- 🎯 ColorField、NumberField、TextField 添加 prefix 属性
- 📋 ListView 和 TableView 修复 HCM 下的边框颜色
- 🔘 Menu 添加长按触发器的保持手势图标
- 📊 TableView 添加 TableFooter 和高亮选择样式
- 🌳 TreeView 添加拖放支持

---

### [GitHub - desko27/react-call: 调用与等待 React 组件 · GitHub](https://github.com/desko27/react-call)

**原文标题**: [GitHub - desko27/react-call: Call & Await React Components · GitHub](https://github.com/desko27/react-call)

react-call 是一个轻量级 React 库，允许你将组件像异步函数一样调用，并通过 `await` 获取返回值。它体积小于 1KB，无外部依赖，支持 SSR 和 React Native，适用于对话框、确认弹窗、表单、通知等场景。

- ⚛️ **核心功能**：通过 `createCallable()` 将组件转为可 `await` 的调用，使用 `call.end()` 返回响应值
- 📡 **挂载方式**：将 Callable 组件作为 Root 挂载在应用顶层（如 App.tsx），所有调用自动渲染
- ▶️ **调用与等待**：使用 `Confirm.call({ message: 'Continue?' })` 并 `await` 获取布尔结果
- 🔄 **高级用法**：支持从调用者作用域结束调用、动态更新 props、使用 `upsert()` 确保单实例
- 🎨 **动画支持**：通过 `call.ended` 布尔值和延迟卸载参数实现退出动画
- 🧩 **Root 属性**：可传递 Root 专属 props（如用户名），通过 `call.root` 访问
- ⚡ **突变流程**：`useMutationFlow` 钩子管理异步操作，支持可选的 `mutationFn` 和 payload 类型
- 🔥 **热重载**：支持 Fast Refresh，可通过 `displayName` 或 Vite 插件保留打开对话框状态
- 🏗️ **多预览环境**：提供 `mount()` 辅助函数，在 Storybook 等工具中避免 Root 冲突
- ❓ **常见问题**：Root 作为调用栈支持多调用；只能有一个 Root 实例；TypeScript 类型完整导出
- 📦 **懒加载**：支持 `React.lazy` 包裹组件，首次调用时按需加载代码块
- 🖥️ **SSR 支持**：兼容服务端渲染，但 `call()` 方法需在客户端触发
- 🤖 **AI 辅助**：提供官方 skill 插件，帮助 AI 编码助手正确生成 Callable 代码

---

### [GitHub - nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect: 捕获不必要的React副作用，实现更简洁、更快速、更安全的代码。 · GitHub](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect)

**原文标题**: [GitHub - nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect: Catch unnecessary React effects for simpler, faster, safer code. · GitHub](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect)

这是一个 ESLint 插件，旨在帮助 React 开发者识别并避免不必要的 `useEffect` 使用，从而写出更简洁、高效、不易出错的代码。

- ⚡ **核心目标**：自动检测并提示 React 中不必要的副作用（Effects），遵循“你可能不需要 Effect”的理念。
- 📦 **安装与配置**：支持 NPM/Yarn 安装，提供 Flat Config、Legacy Config 和 Oxlint 三种配置方式，可启用推荐或严格规则集。
- 🔍 **深度分析**：不仅检查同步的 `setState`，还能分析状态、属性、ref 及其上游来源，并结合依赖项判断 Effect 是否冗余。
- 🛠️ **具体规则**：包含 9 条规则，如禁止在 Effect 中存储派生状态、链式更新状态、模拟事件处理、调整/重置状态等。
- 🧪 **测试与反馈**：每个规则都附有大量有效/无效示例，鼓励用户通过 Issue 或 PR 反馈问题，持续改进插件。
- 📚 **学习资源**：提供 React 官方文档链接，帮助开发者深入理解何时不需要 Effect。

---

### [你可能不需要 Effect – React](https://react.dev/learn/you-might-not-need-an-effect)

**原文标题**: [You Might Not Need an Effect – React](https://react.dev/learn/you-might-not-need-an-effect)

### 概述摘要
本文详细解释了React中何时应该避免使用Effect，以及如何通过更高效的方式处理状态更新、数据计算和事件逻辑。

- 🚫 **避免不必要的Effect**：Effect仅用于与外部系统同步（如非React组件、网络或浏览器DOM），无需用于数据转换或处理用户事件。
- 🔄 **渲染时计算数据**：如`fullName`由`firstName`和`lastName`拼接而成，应直接在渲染时计算，而非通过Effect更新状态。
- ⚡ **缓存昂贵计算**：使用`useMemo`替代Effect来缓存复杂计算（如过滤列表），避免不必要的重复执行。
- 🔑 **重置组件状态**：通过给组件传递不同的`key`属性（如`userId`），在prop变化时自动重置整个组件树的状态。
- 🎯 **在渲染中调整状态**：当prop变化时，可在渲染过程中直接调整状态（如设置`selection`为`null`），而非通过Effect。
- 📢 **事件逻辑放在事件处理器中**：如购买按钮的`POST`请求或通知显示，应直接写在事件处理器中，而非Effect。
- ⛓️ **避免Effect链**：多个Effect相互触发会导致性能问题和代码脆弱性，应尽量在事件处理器中一次性更新所有状态。
- 📊 **通知父组件状态变化**：在事件处理器中同时更新子组件和父组件的状态，避免Effect造成的延迟渲染。
- 🔌 **订阅外部存储**：使用`useSyncExternalStore`代替Effect来订阅浏览器API或第三方库数据。
- 🌐 **数据获取**：在Effect中获取数据时需添加清理函数（如`ignore`标志）以防止竞态条件，或考虑使用框架内置的数据获取机制。

---

### [以开发者优先的同意横幅](https://c15t.com/)

**原文标题**: [The Developer-First Consent Banner](https://c15t.com/)

c15t 是一个面向开发者的开源同意管理横幅工具，专注于高性能、可定制和隐私合规，支持多种前端框架和脚本集成。

- 🚀 **高性能优先**：c15t 的加载速度（89ms）远超 OneTrust（514ms）和 Ketch（709ms），最小化包体积并支持 tree-shaking。
- 🎨 **完全 CSS 自定义**：允许开发者使用自己的设计系统或主题，不限制样式实现。
- 🌐 **国际化支持**：内置多语言处理，使同意横幅能自动适应用户的语言偏好。
- 📍 **地理定位功能**：根据用户所在地区（如 GDPR、CCPA 等 15+ 司法管辖区）自动显示合适的法律配置或隐藏横幅。
- 🔌 **框架兼容性强**：核心无头设计，支持 React、Vue、Svelte、Next.js、Astro 等主流框架。
- 🛠️ **快速集成**：通过 CLI 或代码片段（如 `npx @c15t/cli`）在 30 秒内搭建完整同意管理方案。
- 🧩 **17 种脚本集成**：v2.1 版本新增大量第三方脚本支持，如 Meta Pixel。
- 💬 **社区好评**：开发者称赞其解决了现有解决方案臃肿或体验差的问题，期待用于实际项目。

---

### [GitHub - svar-widgets/react-gantt: 高性能React甘特图，支持TypeScript和灵活的时间线配置。](https://github.com/svar-widgets/react-gantt)

**原文标题**: [GitHub - svar-widgets/react-gantt: High-performance React Gantt chart with TypeScript support and flexible timeline configuration. · GitHub](https://github.com/svar-widgets/react-gantt)

SVAR React Gantt 是一个高性能、可定制的 React 甘特图组件，支持 TypeScript 和 React 19，提供拖拽交互、多任务类型和灵活的时间刻度配置。

- 🚀 核心功能：任务与依赖可视化、拖拽交互、可配置时间刻度（小时/天/周/冲刺）、层级子任务、进度追踪、排序过滤、虚拟化支持大数据量
- 💼 PRO 版特色：工作日历、关键路径、资源规划、自动排程、基线对比、导出为 PNG/PDF/Excel/MS Project、撤销重做
- 🛠️ 快速入门：通过 npm 安装 `@svar-ui/react-gantt`，导入组件和 CSS，传入任务数据即可使用，支持 Next.js 和多种状态管理库
- ⭐ 社区支持：GitHub 上已获 172 星，提供问题追踪和社区论坛，MIT 许可证开源

---

### [发布 react-email@6.5.0 · resend/react-email · GitHub](https://github.com/resend/react-email/releases/tag/react-email%406.5.0)

**原文标题**: [Release react-email@6.5.0 · resend/react-email · GitHub](https://github.com/resend/react-email/releases/tag/react-email%406.5.0)

概述总结  
- 📦 **版本发布**：react-email@6.5.0 已发布，包含 3 次提交至 canary 分支。  
- 🎯 **新增功能**：`email dev` 添加 `--clients` 选项，支持通过环境变量 `COMPATIBILITY_EMAIL_CLIENTS` 指定兼容性警告的邮件客户端（默认：gmail、apple-mail、outlook、yahoo）。  
- 🔧 **优化体验**：团队可针对特定客户端（如 `--clients outlook,apple-mail`）减少警告噪音，空或无效列表回退至默认设置。  
- ♿ **可访问性改进**：为组件添加默认无障碍属性，包括 `Body` 的 `dir`/`lang`、`Img` 的空 `alt` 备用、`Markdown` 表格的 `role="presentation"`，以及 `Preview` 的 `<title>`。  
- 👥 **贡献者**：感谢 @ReemX 的贡献（基于 #2797）。

---

### [GitHub - AndrewPrifer/liquid-dom: 液态玻璃网页效果 · GitHub](https://github.com/AndrewPrifer/liquid-dom)

**原文标题**: [GitHub - AndrewPrifer/liquid-dom: Liquid Glass for the Web · GitHub](https://github.com/AndrewPrifer/liquid-dom)

Liquid DOM 是一个用于 WebGPU 液体玻璃渲染的 monorepo 项目，提供多层次的集成包，包括 React 绑定、Three.js 集成和渲染器无关的布局引擎。

- 🎨 **核心包 (@liquid-dom/core)**：提供命令式场景图、WebGPU 渲染器和可复用的玻璃核心，适合需要直接控制场景图的开发者。
- ⚛️ **React 绑定 (@liquid-dom/react)**：为 React 19 提供布局和玻璃 API 的声明式组件，让你在 React 中轻松描述玻璃 UI。
- 🎭 **Three.js 适配器 (@liquid-dom/three)**：将液体玻璃合成到 Three.js 的 WebGPU 渲染器上，适合已有 Three.js 场景的用户。
- 🖼️ **React Three Fiber 桥接 (@liquid-dom/r3f)**：基于 @liquid-dom/three 和 @liquid-dom/react，为 R3F 用户提供液体玻璃 UI。
- 📐 **布局引擎 (@liquid-dom/layout)**：渲染器无关的布局引擎，支持 SwiftUI 风格的测量和放置，独立于任何渲染器。
- 🌐 **浏览器要求**：需要 WebGPU 支持，DOM 内容渲染需 Chrome 的 Canvas Draw Element 标志，Three.js 集成需 WebGPU 渲染器。

---

### [介绍HTML-in-Canvas API源试用  |  博客  |  Chrome for开发者](https://developer.chrome.com/blog/html-in-canvas-origin-trial)

**原文标题**: [Introducing the HTML-in-Canvas API origin trial  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/html-in-canvas-origin-trial)

Chrome 推出 HTML-in-Canvas API 实验性功能，让开发者能在 Canvas 中直接渲染 DOM 内容，兼具 Canvas 的高性能和 DOM 的丰富交互特性。

- 🎨 **DOM 与 Canvas 的融合**：新 API 允许在 2D Canvas 或 WebGL/WebGPU 纹理中绘制 DOM 元素，同时保持交互性、无障碍性和浏览器功能集成。
- ✅ **保留原生功能**：支持文本选择、复制粘贴、右键菜单、无障碍树、页面内查找、扩展集成和 DevTools 检查等 DOM 原生特性。
- 🚀 **高性能图形处理**：结合 Canvas 的低级像素控制，实现复杂 2D/3D 图形渲染，无需为 UI 构建自定义逻辑。
- 🛠️ **三步骤使用流程**：设置 Canvas（添加 `layoutsubtree` 属性）→ 渲染（使用 `drawElementImage`、`texElementImage2D` 或 `copyElementImageToTexture`）→ 更新 CSS 变换以同步位置。
- 🔄 **WebGL/WebGPU 支持**：通过 `getElementTransform()` 函数计算变换矩阵，确保 3D 场景中 DOM 元素与渲染位置对齐。
- 📚 **框架集成**：Three.js 和 PlayCanvas 已提供实验性支持，简化 API 使用。
- 💡 **应用场景广泛**：适用于大型 Canvas 应用（如 Google Docs、Figma）、3D 场景和游戏，实现可交互 UI 组件。
- 🌟 **社区演示**：包括可翻译的 3D 书籍、折射 UI 滑块、动态 SVG 纹理等创意示例。
- ⚠️ **当前限制**：不支持跨域 iframe 内容，滚动和动画依赖主线程，可能影响性能。
- 📢 **反馈与资源**：可通过 Origin Trial 测试，提供反馈，并参考官方文档和社区演示集合。

---

