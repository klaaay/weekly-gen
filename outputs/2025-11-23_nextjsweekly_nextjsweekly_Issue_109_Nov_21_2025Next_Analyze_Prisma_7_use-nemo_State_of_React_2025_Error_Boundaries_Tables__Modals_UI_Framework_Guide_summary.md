### [React 错误处理：使用 react-error-boundary - Certificates.dev 博客](https://certificates.dev/blog/error-handling-in-react-with-react-error-boundary)

**原文标题**: [Error Handling in React with react-error-boundary - Certificates.dev Blog](https://certificates.dev/blog/error-handling-in-react-with-react-error-boundary)

本文介绍了如何使用 react-error-boundary 库处理 React 应用中的错误，包括展示备用 UI、处理异步错误以及 React 19 的自动错误边界集成。

- 🛡️ 通过 ErrorBoundary 组件捕获渲染错误并显示备用界面
- 🎯 提供三种备用 UI 渲染方式：静态元素、组件形式和渲染属性
- 📍 建议在路由和功能级别战略性地放置错误边界
- ⚡ 使用 useErrorBoundary 钩子处理异步操作中的错误
- 🔄 React 19 通过表单操作和 useTransition 自动集成错误边界
- 📊 可通过 onError 回调实现错误日志记录和监控
- 🎨 错误边界可与 Suspense 等功能组合使用，构建声明式 UI

---

### [React 2025 现状报告](https://survey.devographics.com/en-US/survey/state-of-react/2025)

**原文标题**: [State of React 2025](https://survey.devographics.com/en-US/survey/state-of-react/2025)

React 2025 年度调查现已开放，旨在收集开发者对 React 生态系统的使用反馈，推动框架未来发展。

- 🐢 React 从“快速迭代”转变为“稳步演进”，逐步引入服务端组件等创新
- 🚀 2025 年将正式推出备受期待的 React 编译器，并成立 React 基金会
- 📊 调查目标：衡量 React API 及生态库的认知度与流行度
- ⏱️ 耗时约 15-20 分钟，所有问题均为选填
- 🌍 面向所有 React 使用者（职业/学习/兴趣）
- 📅 调查时间：10 月 25 日至 11 月 25 日，结果将公开释放
- 🤝 由 Devographics 联合社区志愿者运营，支持多语言翻译
- 📈 数据将公开供开发者与企业参考，用于技术规划

---

### [Turbopack：在 Next.js 16 中内联 SVG 的更优方案 | 作者：Vitaliy Potapov | 2025 年 11 月 | 简明 JavaScript](https://javascript.plainenglish.io/turbopack-a-better-way-to-inline-svg-in-next-js-16-e72486286f63?gi=91fa438a74e1)

**原文标题**: [Turbopack: A Better Way to Inline SVG in Next.js 16 | by Vitaliy Potapov | Nov, 2025 | JavaScript in Plain English](https://javascript.plainenglish.io/turbopack-a-better-way-to-inline-svg-in-next-js-16-e72486286f63?gi=91fa438a74e1)

Next.js 16 默认启用 Turbopack 作为打包工具，作者在集成 SVG 图标时发现现有方案无法满足需求：需要内联显示避免额外网络请求、规避 SVG-in-JS 性能损耗、支持 CSS 颜色定制且兼容 Turbopack。通过分析三种主流方案（Next.js 内置 Image 组件、SVGR、雪碧图）的局限性，最终开发出自定义 Turbopack 加载器，结合 CSS 遮罩技术实现高效 SVG 图标解决方案。

- 🚫 Next.js Image 组件会生成独立 HTTP 请求且无法通过 CSS 修改颜色
- ⚡ SVGR 虽支持内联但会导致 SVG 标记注入 JS 包引发性能问题
- 🧩 雪碧图存在 Safari 兼容性问题且 Turbopack 暂不支持生成逻辑
- 🔧 自定义加载器通过 SVGO 优化、mini-svg-data-uri 转换和 image-size 提取尺寸
- 📏 利用 Turbopack 条件规则实现 4KB 以下 SVG 自动内联
- 🎨 通过 CSS mask 属性配合空 SVG 实现单色图标颜色定制
- 📦 最终方案已封装为 npm 包 turbopack-inline-svg-loader

---

### [React 19.2：React 进入其巅峰时代 - DEV 社区](https://dev.to/sagi0312/react-192-react-in-its-sigma-era-op7)

**原文标题**: [React 19.2: React in its sigma era - DEV Community](https://dev.to/sagi0312/react-192-react-in-its-sigma-era-op7)

React 19.2 版本以幽默拟人化方式介绍了其新特性，标志着框架进入更成熟高效的"sigma 时代"，通过自动优化编译器、新增组件和 API 来提升开发体验与性能。

- 🎭 **Activity 组件** - 允许组件在隐藏时保持状态不卸载，类似后台保留 NPC 状态，提升组件切换效率
- 🧘‍♀️ **useEventEffect 钩子** - 减少不必要的重渲染，像设定界限的 Gen-Z，避免依赖项过度更新
- 🫠 **cacheSignal API** - 为服务端组件缓存提供中止信号，适用于高流量应用边缘场景
- 📊 **性能追踪功能** - 在 Chrome DevTools 中可视化渲染性能，类似 Spotify Wrapped 分析报告
- 🍱 **部分预渲染 (PPR)** - 支持静态壳与动态内容分离渲染，需配合框架 (如 Next.js) 简化配置
- 🤝 **Suspense 边界批处理** - SSR 时同步加载多个异步组件，避免 staggered 加载闪烁
- 🔧 **工具链更新** - eslint-plugin-react-hooks v6 支持新钩子，useID 前缀改为_r_适配 View Transitions API

---

### [精通 Next.js 16 中的表格与模态框：保持状态的模式](https://dsheiko.com/weblog/mastering-tables-and-modals-nextjs-16/)

**原文标题**: [Mastering Tables and Modals in Next.js 16: Patterns That Preserve State](https://dsheiko.com/weblog/mastering-tables-and-modals-nextjs-16/)

本文探讨了在 Next.js 中实现表格与模态框交互的三种模式，重点解决在编辑记录时保持表格状态（如分页、排序）的挑战。

- 🗂️ **简约路由方案**：使用可选动态路由在同一页面渲染表格和编辑模态框，但导航会导致表格状态重置
- 🛡️ **拦截路由方案**：通过@modal 插槽在布局层渲染模态框，完美保持表格状态，但无法直接通过 URL 访问详情页
- 🔄 **混合布局方案**：结合动态路由与共享布局，既保持表格状态又支持直接 URL 访问，配合 Redux 实现数据更新同步
- ⚡ **状态管理优化**：通过 Redux 分发时间戳哈希信号，触发表格数据更新而无需重新挂载组件
- 🎯 **最佳实践**：推荐混合方案平衡路由清晰度、状态保持和可访问性，适用于管理后台等数据密集型场景

---

### [工具提示组件不应存在 | TkDodo 的博客](https://tkdodo.eu/blog/tooltip-components-should-not-exist)

**原文标题**: [Tooltip Components Should Not Exist | TkDodo's blog](https://tkdodo.eu/blog/tooltip-components-should-not-exist)

作者认为工具提示组件不应作为独立组件存在，而应通过更高级别的模式组件来提供，以确保一致性和可访问性。

- 🚫 独立工具提示组件易被滥用，导致不一致的用户体验
- ⌨️ 非交互元素上的工具提示无法通过键盘访问，违背无障碍原则
- 🎯 应通过模式组件（如带 title 属性的按钮、信息图标等）强制实施最佳实践
- 🔧 限制低层级工具提示组件能促进更创新的设计解决方案
- 📱 设计系统应提供高层级模式而非基础工具提示组件

---

### [Prisma 7 发布：无锈、更快速、兼容性更强](https://www.prisma.io/blog/announcing-prisma-orm-7-0-0)

**原文标题**: [Prisma 7 Release: Rust-Free, Faster, and More Compatible](https://www.prisma.io/blog/announcing-prisma-orm-7-0-0)

Prisma ORM 7 与 Prisma Postgres 正式发布，聚焦开发者体验提升与性能优化，通过迁移至 TypeScript 客户端、重构代码生成机制及强化类型系统实现更高效的开发流程。

- 🚀 客户端从 Rust 迁移至 TypeScript，查询速度提升 3 倍，打包体积减少 90%
- 🛠️ 代码生成默认输出至项目源码目录，提升开发工具链兼容性
- ⚡ 与 ArkType 合作优化类型系统，类型检查速度提升 70%，所需类型数量减少 45-98%
- 🗄️ Prisma Postgres 支持标准 Postgres 连接协议，兼容主流开发工具
- 🔧 新增 JavaScript/TypeScript 配置文件，支持动态环境变量配置
- 🌐 原生支持边缘计算部署（Vercel Edge/Cloudflare Workers）
- 📦 内置枚举映射支持，更新 Node.js 与 TypeScript 最低版本要求
- 🎯 采用裸机基础设施与 unikernel 微虚拟机，保障数据库性能
- 📢 提供 CLI 一键创建数据库，集成 AI 工作流 API 与 MCP 服务端

---

### [civic-auth-examples/packages/civic-auth/nextjs 位于主分支 · civicteam/civic-auth-examples · GitHub](https://github.com/civicteam/civic-auth-examples/tree/main/packages/civic-auth/nextjs)

**原文标题**: [civic-auth-examples/packages/civic-auth/nextjs at main · civicteam/civic-auth-examples · GitHub](https://github.com/civicteam/civic-auth-examples/tree/main/packages/civic-auth/nextjs)

这是一个 GitHub 仓库页面，展示 civicteam 组织下的 civic-auth-examples 项目

- 🔐 公开认证示例项目库
- 🔔 需要登录才能调整通知设置
- 🍴 项目已被复刻 3 次
- ⭐ 获得 4 个星标收藏
- 📝 存在 5 个待处理问题
- 🔀 有 17 个拉取请求等待合并
- ⚠️ 页面加载时出现错误提示
- 📊 提供代码、安全分析等导航选项

---

### [未找到标题](https://x.com/timneutkens/status/1990841104552357905)

**原文标题**: [No title found](https://x.com/timneutkens/status/1990841104552357905)

检测到浏览器中 JavaScript 功能未启用，建议启用 JavaScript 或更换受支持浏览器以正常使用 X 平台。受支持浏览器列表可查阅帮助中心，同时请检查是否因隐私扩展程序导致功能异常。

- 🚫 JavaScript 未启用导致功能受限
- 🌐 建议启用 JavaScript 或更换受支持浏览器  
- 📖 支持浏览器列表详见帮助中心  
- 🔒 隐私扩展程序可能引发访问问题  
- 🔄 提供重新尝试操作选项

---

### [GitHub - Ademking/use-nemo：自定义React指令集](https://github.com/Ademking/use-nemo)

**原文标题**: [GitHub - Ademking/use-nemo: Custom React directives](https://github.com/Ademking/use-nemo)

这是一个名为 use-nemo 的 Vite 插件库，允许开发者在 React 项目中创建自定义指令，实现代码转换和功能注入。

- 🐟 支持创建任意自定义指令（如 "use nemo"、"use cat" 等）
- ⚡ 基于 Vite 构建工具，通过插件机制实现代码转换
- 🔧 提供完整的 API 接口和辅助函数（injectCode、injectComment、injectImport）
- 📁 采用模块化设计，通过指令注册表管理自定义指令
- 🐱 内置 useMeow 示例指令，展示基本使用方法
- 📚 支持 TypeScript 类型定义，确保开发体验
- 🔄 指令处理流程包括发现、解析、转换和清理四个阶段
- 📄 采用 MIT 开源协议，目前获得 48 星标和 1 个分支

---

### [GitHub - MusKRI/pure-ui：基于Base UI 构建的设计系统](https://github.com/MusKRI/pure-ui)

**原文标题**: [GitHub - MusKRI/pure-ui: A design system built with Base UI](https://github.com/MusKRI/pure-ui)

Pure UI 是一个基于 Base UI 构建、采用 Tailwind CSS 样式设计的 React 组件库，提供美观、可访问且可组合的组件供开发者直接复制使用。

- 🎨 基于 Base UI 构建并采用 Tailwind CSS 样式设计
- ⚛️ 专为 React 应用提供的可组合组件集合
- 📋 支持直接复制粘贴使用组件代码
- 🚀 使用 bun 运行开发服务器：bun run dev
- 🔍 提供代码检查和格式化命令：bun run lint / bun run format
- 🌐 项目官网：pure.kam-ui.com
- 📊 项目获得 37 个星标，暂无复刻分支
- 💻 主要使用 TypeScript 开发（占比 86.8%）

---

### [Sevalla® - 云应用平台，数分钟内部署应用。](https://sevalla.com/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

**原文标题**: [SevallaÂ® - Cloud Application Platform. Deploy Apps in Minutes.](https://sevalla.com/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

Sevalla 是一个简化应用部署的 PaaS 平台，让开发者无需关注基础设施即可快速部署各类网络项目。

- 🚀 快速部署应用，支持任意技术栈和 Docker 镜像
- 💰 提供 50 美元信用额度，按用量付费无隐藏费用
- 🌍 全球 25 个数据中心与 260+ 边缘节点确保低延迟
- 🛠️ 全栈服务：应用托管、对象存储、数据库和静态网站托管
- 📊 客户案例：Stepler 公司月成本从 3000 美元降至 650 美元
- 🔓 无限制资源：免费流量、并行构建、数据库使用和团队成员
- ⚡ 基于 Kubernetes 和 Cloudflare，提供自动扩展与安全保障
- 🎯 专注开发：无需运维管理，支持私有 Git 仓库和灵活部署

---

### [2025 年 11 月 18 日 Cloudflare 服务中断事件](https://blog.cloudflare.com/18-november-2025-outage/)

**原文标题**: [Cloudflare outage on November 18, 2025](https://blog.cloudflare.com/18-november-2025-outage/)

2025 年 11 月 18 日 Cloudflare 发生全球服务中断，起因是数据库权限变更导致机器人管理系统配置文件异常增大，触发核心代理系统内存限制而崩溃，造成大规模 HTTP 5xx 错误。经过紧急回滚和系统修复，服务在 6 小时内逐步恢复。

- 🚨 故障始于 11:28 UTC，核心 CDN、安全服务、Workers KV 等多产品出现 HTTP 5xx 错误
- 🔄 根本原因为数据库权限变更导致机器人管理特征文件出现重复条目，文件体积倍增
- 💥 核心代理系统对特征文件存在 200 条内存预分配限制，异常文件触发系统崩溃
- 🌐 初期误判为超大规模 DDoS 攻击，13:05 通过绕过核心代理临时缓解部分服务影响
- ⚙️ 14:30 通过回滚正常配置文件解决核心问题，17:06 所有服务完全恢复
- 📊 仪表盘登录因 Turnstile 服务中断受影响，邮件安全防护出现短暂功能降级
- 🔧 后续改进包括强化配置验证机制、增加全局功能开关、优化错误处理流程
- 📉 此次是 Cloudflare 自 2019 年以来最严重的全球性服务中断

---

### [错误](https://angiejones.tech/how-i-taught-github-copilot-code-review-to-think-like-a-maintainer/)

**原文标题**: [Error](https://angiejones.tech/how-i-taught-github-copilot-code-review-to-think-like-a-maintainer/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='angiejones.tech', port=443): Max retries exceeded with url: /how-i-taught-github-copilot-code-review-to-think-like-a-maintainer/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [我们在 Vercel 构建智能助手的经验总结 - Vercel](https://vercel.com/blog/what-we-learned-building-agents-at-vercel)

**原文标题**: [What we learned building agents at Vercel - Vercel](https://vercel.com/blog/what-we-learned-building-agents-at-vercel)

企业通过构建智能体提升生产力，当前应聚焦低认知负荷、高重复性任务实现高效自动化

- 🤖 智能体在客户支持、代码审查等场景展现潜力，企业需筛选成本合理的应用场景
- 🎯 当前 AI 应用最佳领域是低认知负荷的高重复工作（如数据录入、线索筛选），这类任务既超越传统自动化能力又具备 AI 可靠性
- 👥 通过访谈员工"最厌恶的重复工作"挖掘需求，维赛尔已实现销售线索自动分类和安全审核自动化
- 📈 实际案例证明：销售线索处理效率提升 10 倍，安全工单处理时长减少 59%
- 🛠️ 开源智能体模板涵盖商机处理、数据分析等场景，提供从发现到落地的全流程支持
- 🔄 所有自动化流程保留人工审核环节，确保关键决策的准确性

---

### [构建 UI 框架 - Google 文档](https://docs.google.com/document/d/1qFrNa3wmeTn_HDj0C4nhGWy5T1DlF5J8zTrlhA0vEAc/preview)

**原文标题**: [Building a UI framework - Google 文档](https://docs.google.com/document/d/1qFrNa3wmeTn_HDj0C4nhGWy5T1DlF5J8zTrlhA0vEAc/preview)

由于浏览器未启用 JavaScript，导致无法打开文件，请启用后重新加载页面。

- 🚫 浏览器 JavaScript 未启用
- 📄 文件无法正常打开
- ⚙️ 需启用 JavaScript 功能
- 🔄 重新加载页面以生效

---

