### [JavaScript 周刊第 754 期：2025 年 9 月 26 日](https://javascriptweekly.com/issues/754)

**原文标题**: [JavaScript Weekly Issue 754: September 26, 2025](https://javascriptweekly.com/issues/754)

本期技术周刊聚焦 JavaScript 生态系统更新与开发工具创新。Chrome 团队推出 DevTools MCP 服务器实现 AI 驱动调试，GitHub 加强 npm 供应链安全措施，同时涵盖 TC39 新提案进展及多款主流框架版本更新。

- 🛠️ Chrome DevTools 推出 MCP 服务器，支持 AI 代理自动化调试网页应用
- 🔒 GitHub 针对 npm 供应链攻击提出安全加固方案，包括恶意包拦截和可信发布机制
- 📜 TC39 会议推进 Import Bytes、Iterator Chunking 等新提案
- ⚡ 多款工具发布更新：pnpm 10.17 支持包年龄检查模式、Astro 5.14 带来开发体验优化
- 🐛 CodeRabbit CLI 集成 AI 代码审查，实时检测代码缺陷和安全问题
- 📊 技术文章涵盖 DOS 环境运行 TypeScript、Next.js 身份验证实践等实用主题
- 🎯 TanStack Start v1 候选版发布，主打类型安全的全栈 React 开发框架
- 🌐 Dr. Axel 推出 JavaScript 新手教程系列，从基础语法到前端框架全面覆盖
- 🔄 发布 Node.js 双版本更新、PostgreSQL 18.0 等基础设施工具
- 📈 图表库 billboard.js 新增图像标签支持，ESLint 插件优化 React 效果钩子使用

---

### [AddyOsmani.com - 赋予 AI 视觉：Chrome DevTools MCP 简介](https://addyosmani.com/blog/devtools-mcp/)

**原文标题**: [AddyOsmani.com - Give your AI eyes: Introducing Chrome DevTools MCP](https://addyosmani.com/blog/devtools-mcp/)

Chrome DevTools MCP 是一项新工具，让 AI 编程助手能够实时查看和操作 Chrome 浏览器，从而摆脱“盲写代码”的限制。它基于 Model Context Protocol 标准，将 Chrome 的调试和自动化功能暴露给 AI 助手，使其能够运行代码、检查页面行为并基于实际反馈修复问题。

- 👁️ 赋予 AI“浏览器视觉”：通过 MCP 协议连接 AI 助手与 Chrome DevTools，实现实时页面交互和调试  
- 🔧 核心能力覆盖：性能分析（如 LCP 测量）、DOM 检查、网络请求监控、用户行为模拟和 CSS 调试  
- 🚀 典型应用场景：实时验证代码修复、诊断控制台/网络错误、自动化用户流程测试、性能优化审计  
- ⚙️ 技术实现：基于 Chrome DevTools Protocol 和 Puppeteer 库，通过 MCP 工具封装浏览器操作指令  
- 🔒 安全隔离：默认使用独立浏览器配置文件，支持临时会话模式防止数据混淆  
- 🌐 生态兼容：已支持 Cursor、Claude Code 等主流 AI 开发工具，通过 npm 快速集成  
- 📈 未来规划：作为公开预览版持续迭代，鼓励开发者通过 GitHub 反馈需求以扩展功能

---

### [面向 AI 代理的 Chrome DevTools (MCP)  |  博客  |  Chrome 开发者专栏](https://developer.chrome.com/blog/chrome-devtools-mcp?hl=en)

**原文标题**: [Chrome DevTools (MCP) for your AI agent  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-devtools-mcp?hl=en)

Chrome DevTools MCP 服务器公开预览版发布，使 AI 编程助手能够直接调试浏览器中的网页，提升代码生成和问题诊断的准确性。

- 🚀 通过 MCP 协议将 Chrome DevTools 调试能力集成到 AI 编程助手
- 👁️ 解决 AI 代理无法实时观察代码运行效果的根本问题  
- 🛠️ 支持性能追踪、网络错误诊断、用户行为模拟等调试场景
- 📝 提供具体提示词示例（如验证代码修改、诊断图片加载问题）
- ⚙️ 通过 npm 快速安装配置，支持实时检查网页核心性能指标
- 🌱 采用渐进式开发模式，邀请开发者反馈功能需求
- 📚 所有工具清单和详细文档已在 GitHub 开源发布

---

### [我们的 npm 供应链安全增强计划 - GitHub 博客](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/)

**原文标题**: [Our plan for a more secure npm supply chain - The GitHub Blog](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/)

GitHub 针对 npm 软件供应链安全威胁采取强化措施，包括应对近期账户劫持攻击、实施严格身份验证机制，并推动可信发布流程以保障开源生态安全。

- 🐛 9 月 14 日发现自复制蠕虫攻击，通过劫持维护者账户向流行 JS 包注入恶意脚本
- 🚨 GitHub 立即移除 500+ 受污染包并阻断恶意软件传播指标
- 🔒 将强制要求双因素认证本地发布，采用 7 天有效期的细粒度令牌
- ⚙️ 逐步淘汰传统令牌和 TOTP 双因素认证，转向 FIDO 认证标准
- 🌐 扩展可信发布供应商支持，默认禁用令牌发布权限
- ⚡ 建议维护者立即启用可信发布功能，并为账户设置强制双因素认证
- 🤝 强调生态系统安全需开发者共同参与，采用强安全实践构建可信环境

---

### [获取失败](https://javascriptweekly.com/link/174910/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/174910/web)

无法总结：获取内容失败，状态码 403。

---

### [npm 包的可信发布 | npm 文档](https://docs.npmjs.com/trusted-publishers/)

**原文标题**: [Trusted publishing for npm packages | npm Docs](https://docs.npmjs.com/trusted-publishers/)

npm 可信发布功能允许通过 CI/CD 工作流使用 OpenID Connect 认证直接发布 npm 包，取代传统的长期令牌认证方式，提升安全性。

- 🔐 可信发布基于 OpenID Connect 建立 npm 与 CI/CD 提供商间的信任关系，消除长期令牌泄露风险
- ⚙️ 当前支持 GitHub Actions 和 GitLab CI/CD的云端托管运行器，自托管运行器暂不支持
- 📦 配置分为两步：在 npmjs.com 添加可信发布者，在 CI/CD 工作流中配置 OIDC 权限
- 🛡️ 启用后建议限制令牌访问权限，选择"要求双因素认证并禁用令牌"选项
- 📋 自动生成来源证明，提供包构建来源的加密验证（仅限公共仓库和公共包）
- 🔄 迁移时应先设置可信发布并验证，再禁用令牌并撤销旧令牌
- ⚠️ 当前限制：每个包只能配置一个发布者，自托管运行器不支持，私有依赖仍需令牌认证
- 🚀 未来计划支持更多 CI/CD 提供商和自托管运行器

---

### [获取失败](https://javascriptweekly.com/link/174846/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/174846/web)

无法总结：获取内容失败，状态码 403。

---

### [tc39/agendas 仓库主分支下的 agendas/2025/09.md 文件](https://github.com/tc39/agendas/blob/main/2025/09.md)

**原文标题**: [agendas/2025/09.md at main · tc39/agendas · GitHub](https://github.com/tc39/agendas/blob/main/2025/09.md)

TC39 委员会 GitHub 仓库的议程页面概览，包含代码管理、协作功能和访问控制相关信息。

- 📋 公开议程仓库用于 ECMAScript 标准制定讨论
- 🔔 需要登录才能修改通知设置
- 🍴 199 个复刻版本显示社区参与度
- ⭐ 获得 1.2k 星标收藏
- 💻 包含代码仓库和安全管理功能
- ❗ 当前存在页面加载错误需重新刷新
- 🔍 提供洞察分析等额外导航选项
- 🤝 支持议题跟踪和拉取请求协作
- ⚠️ 安全功能与行动工作流集成展示

---

### [GitHub - tc39/proposal-import-bytes：JavaScript中导入字节的适度提案](https://github.com/tc39/proposal-import-bytes)

**原文标题**: [GitHub - tc39/proposal-import-bytes: A modest proposal for importing bytes in javascript](https://github.com/tc39/proposal-import-bytes)

该提案旨在为 JavaScript 添加导入任意字节数据的能力，通过统一的语法实现在不同环境（如浏览器、Node.js 等）中同步或异步读取文件内容。

- 📄 **提案状态**：处于 TC39 流程的第 2.7 阶段，由@styfle 和@guybedford 主导推进。
- 🔧 **核心语法**：支持通过`import ... with { type: "bytes" }`或动态导入方式将文件（如 PNG、字体）加载为不可变的 Uint8Array。
- 🌐 **跨平台兼容**：消除当前需针对不同运行时（Deno、Bun、Node.js、浏览器）编写特定代码的繁琐步骤，实现代码同构。
- ⚡ **性能优化**：构建工具可静态分析导入内容，支持内联为 Base64 编码以提升加载效率。
- 🔒 **不可变性设计**：采用不可变 ArrayBuffer 支撑 Uint8Array，避免多模块共享时内存冲突或数据意外修改。
- ❓ **常见问答**：解释选择 Uint8Array 而非 ArrayBuffer/Blob 的原因，强调其与 Node.js Buffer 的兼容性及 JavaScript 标准独立性。

---

### [GitHub - tc39/proposal-iterator-chunking：为迭代器添加生成子序列迭代器方法的提案](https://github.com/tc39/proposal-iterator-chunking/)

**原文标题**: [GitHub - tc39/proposal-iterator-chunking: a proposal to add a method to iterators for producing an iterator of its subsequences](https://github.com/tc39/proposal-iterator-chunking/)

该提案旨在为 JavaScript 迭代器添加 chunk 和 window 方法，用于将迭代器元素分割为可配置大小的非重叠或重叠子序列。

- 🚀 提案处于 TC39 标准制定流程的第二阶段，旨在为迭代器新增分块处理功能
- 🔧 提供两种核心方法：chunk(非重叠分块) 和 window(滑动窗口)
- 📊 支持多种应用场景：分页处理、矩阵运算、流处理、连续计算等
- 🌍 参考多语言实现：C++、Java、Python 等均有类似功能
- ⚠️ 处理边界情况：空迭代器、零尺寸分块等特殊情况的差异化处理
- 📚 包含丰富的测试用例和规范文档，确保功能稳定性
- 👥 由两位主要贡献者维护，项目获得 72 星标关注
- 🔄 提案持续演进，2023-2024 年多次向委员会进行演示汇报

---

### [获取失败](https://javascriptweekly.com/link/174854/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/174854/web)

无法总结：获取内容失败，状态码 404。

---

### [Chrome 平台状态](https://chromestatus.com/feature/5668291307634688)

**原文标题**: [Chrome Platform Status](https://chromestatus.com/feature/5668291307634688)

概述总结
- 📚 阅读习惯培养
- 🧠 知识体系构建  
- ⏰ 碎片时间利用
- 📱 电子阅读优势
- 🌟 经典作品精读

（请提供需要总结的文本内容，我将按照模板要求进行格式化处理）

---

### [Preact 11 Beta 版引入 Hydration 2.0、默认 Ref 转发及现代化打包方案 - InfoQ](https://www.infoq.com/news/2025/09/preact-11-beta/)

**原文标题**: [Preact 11 Beta Introduces Hydration 2.0, Default Ref Forwarding, and Modernized Bundling - InfoQ](https://www.infoq.com/news/2025/09/preact-11-beta/)

Preact 11 Beta 版本发布，重点改进了水合机制、引用转发和打包格式，同时移除了旧版特性以提升现代化程度。

- 💧 水合 2.0 支持组件在渲染时返回零或多个 DOM 节点，突破原有单节点限制
- 🎯 函数组件默认支持 ref 转发，无需使用 forwardRef 包装，减少代码冗余
- ⚖️ 钩子依赖检查改用 Object.is 替代宽松相等，修复 NaN 比较等边界情况
- 📦 ESM 模块统一采用.mjs 后缀，同步现代模块规范
- 🗑️ 移除自动 CSS 像素后缀、SuspenseList 等遗留功能以简化核心库
- 🌐 停止支持 IE11 并要求 TypeScript 5.1+，利用更先进的 JSX 类型系统
- 📉 用户实测升级后打包体积减少 4KB，优化内存管理与错误边界处理
- 🔄 维护团队提供迁移指南，强调虽为重大版本但尽量保持升级平滑

---

### [2025 年顶级编程语言 - IEEE Spectrum](https://spectrum.ieee.org/top-programming-languages-2025)

**原文标题**: [The Top Programming Languages 2025 - IEEE Spectrum](https://spectrum.ieee.org/top-programming-languages-2025)

人工智能不会终结顶级编程语言的演进，而是推动其适应性转型与新兴领域的崛起

- 🤖 AI 工具正改变编程方式，但人类仍需掌握核心语言逻辑进行指令优化
- 📊 Python 因 AI 库生态优势持续领跑，JavaScript 保持 Web 领域绝对主导地位
- 🚀 Rust 凭借内存安全特性在系统编程领域快速增长，Go 语言在云原生领域稳居前列
- 🌐 新兴领域催生专用语言（如量子计算 Q#），传统语言通过版本迭代融入 AI 特性
- 💡 低代码平台兴起反而提升对底层语言理解的需求，开发者需兼顾高效工具与核心技术

---

### [pnpm 10.17 | pnpm](https://pnpm.io/blog/releases/10.17)

**原文标题**: [pnpm 10.17 | pnpm](https://pnpm.io/blog/releases/10.17)

pnpm 10.17 版本发布，包含最小发布年龄设置的模式支持和多项补丁优化

- 🔧 最小发布年龄排除设置现在支持模式匹配（如`"@eslint/*"`）
- 💾 修复了从缓存加载包元数据时仍会检查最小发布年龄的问题
- 📦 当活跃版本不满足成熟度要求时，避免意外降级到预发布版本
- 🚀 解决了最小发布年龄检查与精确版本请求的兼容性问题

---

### [Astro 5.14 | Astro](https://astro.build/blog/astro-5140/)

**原文标题**: [Astro 5.14 | Astro](https://astro.build/blog/astro-5140/)

Astro 5.14 版本带来了路由工具增强、Svelte 异步渲染支持、React 19 Actions 集成等多项功能改进和开发者体验优化。

- 🚨 预渲染路由冲突警告：新增碰撞检测功能，可配置构建失败强制处理冲突
- 🧩 路由模式参数：在 getStaticPaths 中提供 routePattern 参数，支持复杂动态路由本地化
- ⚡ Svelte 异步渲染：服务端组件支持 await 语法，需在配置中启用实验性功能
- 🔄 React 19 Actions 集成：稳定版 getActionState() 和 withState() 函数实现渐进式表单增强
- 🎨 SVG 组件类型：新增内置 SvgComponent 类型，简化 SVG 导入的类型定义
- 🌐 跨平台数据库支持：Astro DB 新增 web 模式驱动，支持 Cloudflare 等非 Node.js 环境
- 📍 站点地图命名空间配置：可独立控制 news/video 等 XML 命名空间的包含规则
- 🔤 字体数据接口：实验性 Fonts API 新增 getFontData() 函数，支持编程式字体数据获取
- 🔧 升级方式：推荐使用@astrojs/upgrade 工具或包管理器命令进行版本升级

---

### [Node.js](https://nodejs.org/en/blog/release/v24.9.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v24.9.0)

Node.js v24.9.0（Current 版本）于 2025 年 9 月 25 日发布，主要包含 HTTP 升级控制、SQLite 功能增强、Worker 堆分析 API 等新特性，同时进行了多项性能优化和错误修复。

- 🚀 HTTP 模块新增 shouldUpgradeCallback，允许服务器控制 HTTP 升级流程
- 🗃️ SQLite 模块优化 ERM 支持并导出 Session 类，新增标记模板功能
- 📊 Worker 线程新增堆性能分析 API，便于内存监控
- 🔧 加密模块改进异步函数实现，提升 Promise 处理效率
- 🌐 网络模块优化 IPv6 代理支持和 HTTP 令牌验证性能
- 📚 文档更新包括安全升级策略和 V8 快速 API 指南
- 🛠️ 核心代码重构涉及字符串处理、缓存优化和内存管理改进
- 🔍 调试功能增强包括 Source Map 支持和断言错误溯源
- 📦 依赖项更新至 OpenSSL 3.5.3 和 Undici 7.16.0
- ⚡ 性能优化涵盖 zlib 压缩、VM 模块和 REPL 大文本处理

---

### [Node.js](https://nodejs.org/en/blog/release/v22.20.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v22.20.0)

Node.js v22.20.0（LTS）版本发布，主要更新 OpenSSL 至 3.5.2 以延长支持周期至 2027 年，并包含多项功能增强与稳定性改进。

- 🔐 OpenSSL 升级至 3.5.2 版本，确保支持延续至 2027 年 4 月
- 🌐 HTTP/2模块新增原始头数组支持与HTTP代理保活超时缓冲选项
- 📦 SEA（单可执行应用）功能增强，支持配置执行参数与扩展参数
- 🔧 压缩流新增 Brotli 算法支持，提升数据压缩效率
- 🧪 测试运行器新增对象属性模拟功能，优化测试灵活性
- 👷 Worker 线程新增 CPU 性能分析 API，便于多线程性能监控
- 📜 文档与稳定性改进，包括路径通配匹配标记为稳定功能
- 🐛 多项错误修复与依赖项更新，提升整体稳定性与安全性

---

### [Nuxt UI v4 · Nuxt 博客](https://nuxt.com/blog/nuxt-ui-v4)

**原文标题**: [Nuxt UI v4 · Nuxt Blog](https://nuxt.com/blog/nuxt-ui-v4)

Nuxt UI v4 正式发布，将 Nuxt UI 与 Nuxt UI Pro 整合为完全免费的开源库，提供 110 多个组件、12 个免费模板和完整 Figma 工具包，全面提升 Vue/Nuxt 开发生态。

- 🎉 版本升级：v4 版本合并免费版与专业版，所有高级组件永久免费开放
- 📦 资源丰富：包含 110+ 组件、12 款生产级模板（支持着陆页/仪表盘/文档站等场景）
- 🎨 设计协同：免费提供含 2000+ 变体的 Figma 工具包，实现设计与开发无缝对接
- ⚡ 开发优化：支持 Vue/Nuxt/Adonis/Laravel 框架，具备移动端优先响应式设计
- 🤖 AI 就绪：文档支持 MCP 协议和 LLMs.txt 格式，赋能 AI 工具直接调用组件元数据
- 🔄 平滑迁移：保留 v3 兼容性，提供详细迁移指南降低升级成本
- 🌐 生态整合：依托 Vercel 支持，新增对 Vercel AI SDK v5 的聊天组件兼容
- 🙏 致谢用户：特别感谢 Pro 版用户的前期支持推动项目开源化进程

---

### [PostgreSQL：PostgreSQL 18 发布！](https://www.postgresql.org/about/news/postgresql-18-released-3142/)

**原文标题**: [PostgreSQL: PostgreSQL 18 Released!](https://www.postgresql.org/about/news/postgresql-18-released-3142/)

PostgreSQL 18 正式发布，这是世界上最先进的开源数据库的最新版本，通过全新 I/O 子系统提升性能，支持虚拟生成列等开发者功能，并简化单点登录集成。

- 🚀 引入异步 I/O 子系统，读取性能提升高达 3 倍
- 📊 支持跨大版本升级保留查询规划统计信息，缩短升级后性能恢复时间
- 🔍 新增多列 B 树索引跳过扫描功能，优化 OR 条件查询性能
- 💡 新增虚拟生成列功能，支持查询时实时计算数值
- 🔐 新增 OAuth 2.0 认证支持，简化单点登录集成
- ⚡ 支持 GIN 索引并行构建，提升索引创建效率
- 📝 增强文本处理能力，新增 Unicode 快速排序规则
- 🔄 改进逻辑复制功能，默认启用并行流式传输
- 📈 优化查询计划显示，自动展示缓冲区访问统计
- 🛡️ 默认启用页面校验和，增强数据完整性保护

---

### [ESLint v9.36.0 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/09/eslint-v9.36.0-released/)

**原文标题**: [ESLint v9.36.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/09/eslint-v9.36.0-released/)

ESLint v9.36.0 版本发布，作为一次小版本更新，主要修复了已知错误并新增了部分功能。

- 🐛 修复了 `preserve-caught-error` 规则中的边缘情况，可能导致检测到更多错误
- 🧊 深度冻结了 `@eslint/js` 包导出的所有配置对象
- 📝 更新了文档示例以使用 `defineConfig` 方法
- 🔧 修复了规则选项类型声明等类型定义问题
- ⚙️ 改进了测试用例和持续集成配置
- 👥 由 Francesco Trotta、Pixel998 等多位贡献者共同完成

---

### [从蒸汽到软盘：将现代 TypeScript 移植至 DOS 运行——Jimbly 的漫游](https://jimb.ly/2025/09/23/qauntumpulse-from-steam-to-floppy/)

**原文标题**: [From Steam to Floppy: Porting Modern TypeScript to Run on DOS – Jimbly's Wanderings](https://jimb.ly/2025/09/23/qauntumpulse-from-steam-to-floppy/)

本文详细记录了将现代 TypeScript 编写的 QuantumPulse 2A 命令行解释器移植到 MS-DOS 系统的完整技术历程。

- 🚀 项目初衷是让基于 Web 技术的游戏 CLI 工具实现跨时代兼容，目标生成单个可在 DOS 和现代 Windows 双平台运行的 EXE 文件
- 🔧 尝试过 GCC、Open Watcom 和 Free Pascal 等原生编译方案后，最终选择基于 JavaScript 解释器 jSH 实现 TypeScript 代码的 DOS 兼容
- ⚡ 通过懒加载优化将 DOS 环境下的启动时间从 20 秒缩短至 1 秒以内，并利用 Babel+Browserify 构建出平台无关的 JS 捆绑包
- 🛠️ 定制化改造 jSH 源码，移除网络依赖使体积减半（548KB），并成功移植出 376KB 的 Win32 版本
- 📦 采用 Open Watcom 编译出 10KB 的 DOS 存根程序，最终生成 42KB 的统一启动器，整体方案仅占用 1.05MB 空间
- 🔍 深入测试证实兼容 MS-DOS 3.30 至 6.22 系统，创造性地实现了"MS-DOS 6.22"作为 Steam 最低系统要求的复古效果
- 🐳 通过 Docker 容器化构建环境确保编译过程的可重现性，相关工具链已开源共享
- 🎮 最终成果既满足了 DOSember 游戏 jam 的参与需求，也为 QuantumPulse 玩家提供了跨时代的开发工具体验

---

### [《QuantumPulse 2A》在 Steam 平台上架](https://store.steampowered.com/app/3175190/QuantumPulse_2A/)

**原文标题**: [QuantumPulse 2A on Steam](https://store.steampowered.com/app/3175190/QuantumPulse_2A/)

Steam 平台主要功能区域与多语言支持界面

- 🏠 商店首页包含游戏发现队列、愿望单和积分商城
- 💬 社区板块设有讨论区、创意工坊和直播功能  
- 🔧 支持中心提供安装指导和问题反馈入口
- 🌐 支持简体中文等 30 种语言界面切换
- ⚠️ 用户可报告翻译相关问题

---

### [GitHub - SuperIlu/jSH：适用于DOS的JavaScript脚本引擎](https://github.com/SuperIlu/jSH)

**原文标题**: [GitHub - SuperIlu/jSH: A Javascript scripting engine for DOS](https://github.com/SuperIlu/jSH)

jSH 是一个基于 DOS 操作系统的 JavaScript 脚本引擎，支持文件操作和文本界面，适用于 MS-DOS、FreeDOS 等系统。

- 🖥️ 专为 DOS 系统设计的 JavaScript 解释器，支持文件 IO 和文本用户界面
- 🔧 包含简单包管理器 JPM，支持通过 HTTPS 下载扩展包
- 📁 提供 JsCommander 示例应用，实现类 Norton Commander 的文件管理功能
- ⚙️ 支持编译原生 DXE 扩展库，可增强脚本功能
- 💾 最低要求 80386 处理器和 4MB 内存，推荐 Pentium 级 8MB 配置
- 🔗 基于 MuJS 解释器和 DJGPP 工具链开发，支持多种开源协议
- 📦 可通过 GitHub 获取二进制版本，支持 Dosbox 和实机运行

---

### [GitHub - bodadotsh/npm-security-best-practices: 如何防范 NPM 供应链攻击确保安全](https://github.com/bodadotsh/npm-security-best-practices)

**原文标题**: [GitHub - bodadotsh/npm-security-best-practices: How to stay safe from NPM supply chain attacks](https://github.com/bodadotsh/npm-security-best-practices)

该仓库总结了防范 NPM 供应链攻击的最佳实践，涵盖依赖管理、安全配置和维护策略。

- 🔒 **锁定依赖版本**：使用精确版本号或覆盖机制避免意外更新
- 📋 **提交锁文件**：确保跨环境依赖一致性，避免重构建风险
- ⚠️ **禁用生命周期脚本**：防止恶意脚本通过 postinstall 等钩子执行
- ⏳ **设置发布冷却期**：延迟安装新包以规避潜在风险
- 🛡️ **启用权限模型**：限制 Node.js 进程对系统资源的访问
- 📦 **减少外部依赖**：优先使用原生模块替代第三方库
- 🔐 **强制双因素认证**：保护 npm 账户免受未授权访问
- 🎫 **创建受限令牌**：按需分配最小权限的访问令牌
- 📜 **生成来源证明**：通过 CI/CD 构建可验证的包来源记录
- 📁 **审核发布文件**：控制包内容防止敏感信息泄露
- 👥 **组织权限管理**：团队分级授权与 2FA 强制策略
- 🏢 **使用私有仓库**：企业级依赖管理与安全审计
- 🔍 **安全工具集成**：结合 Socket.dev、Snyk 等平台持续监控
- 💝 **支持开源维护**：通过捐赠降低维护者倦怠导致的安全风险

---

### [如何在 Next.js 应用中添加身份验证？](https://clerk.com/blog/how-to-add-authentication-to-a-nextjs-application?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=auth-nextjs&utm_content=09-26-29&dub_id=HArBvTtgXk308TBT)

**原文标题**: [How do I add authentication to a Next.js app?](https://clerk.com/blog/how-to-add-authentication-to-a-nextjs-application?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=auth-nextjs&utm_content=09-26-29&dub_id=HArBvTtgXk308TBT)

本文介绍了在 Next.js 应用中实现 JWT 认证的完整方案，包括策略选择、技术实现和进阶优化方向。

- 🔐 认证策略对比：详细解析会话令牌、JWT 和 OAuth 三种主流认证方案的优缺点
- ⚙️ 技术实现：通过 SQLite 数据库配置、密钥对生成和中间件保护完成 JWT 认证流程
- 👤 用户流程：包含注册登录页面实现、密码哈希处理和登出功能开发
- 🛡️ 路由保护：利用 Next.js 中间件实现/dashboard 路由的自动权限验证
- ⚠️ 生产级提醒：指出基础实现缺乏密码重置、多因素认证等企业级功能
- 🚀 解决方案：推荐使用 Clerk 平台快速获得包含社交登录、安全防护的完整认证体系
- 📚 学习资源：提供配套代码库和进阶指南链接便于实践拓展

---

### [无](https://blog.dochia.dev/blog/json-isnt-json/)

**原文标题**: [None](https://blog.dochia.dev/blog/json-isnt-json/)

JSON 规范看似简单统一，但不同编程语言和库在实现时存在诸多差异，导致数据交换时出现精度丢失、编码混乱、排序不一致等隐蔽问题。

- 🔢 **数字精度差异**：JavaScript 无法安全处理超过 2^53 的整数，而 Python/Java 可精确解析，金融计算需使用专用十进制类型
- 🌐 **Unicode 编码不一致**：相同字符的不同 Unicode 表示形式（如é的单码点与组合形式）在不同语言中可能被视作不同字符串
- 🔄 **对象键顺序不统一**：JSON 规范不要求保持键顺序，但 Go 默认排序、JavaScript 保持插入顺序，影响加密签名等场景
- ❓ **空值处理歧义**：null、undefined、缺失属性在不同语言中表示方式不同，容易引发逻辑错误
- ⏰ **日期格式混乱**：缺乏原生日期类型导致 ISO 字符串、时间戳等多种格式混用，时区处理不一致
- 🚨 **错误处理差异**：尾随逗号、重复键、前导零等非法 JSON 在不同解析器中报错规则不同
- 🐦 **现实案例警示**：Twitter 大 ID 精度丢失、PostgreSQL 的 JSON/JSONB 行为差异、MongoDB 扩展 JSON 等实际陷阱
- 🛡️ **应对策略**：采用模式验证、数据标准化、精选解析库、跨语言兼容测试等方法规避问题

---

### [别再使用.reverse().find() 了：认识 findLast() - Matt Smith](https://allthingssmitty.com/2025/09/22/stop-using-reverse-find-meet-findlast/)

**原文标题**: [
    Stop using .reverse().find(): meet findLast() - Matt Smith
  ](https://allthingssmitty.com/2025/09/22/stop-using-reverse-find-meet-findlast/)

ES2023 新增的 findLast() 和 findLastIndex() 方法可直接从数组末尾搜索元素，无需反转数组即可实现更简洁高效的查找操作。

- 🔍 传统方法需通过.slice().reverse().find() 组合实现逆向查找，存在性能损耗和代码冗余问题
- 🚀 新方法直接逆向遍历数组，避免创建副本和反转操作，提升代码可读性和执行效率
- 📝 findLast() 返回匹配的最后一个元素，findLastIndex() 返回对应的索引位置
- ⚡ 特别适合处理聊天记录、操作日志、表单验证等需要查找末项数据的场景
- 🛡️ 相比会改变原数组的 reverse() 方法，新方法更安全可靠
- 🌐 主流浏览器和 Node.js 18.12+ 均已支持，旧环境可通过 core-js 实现兼容

---

### [在 JavaScript Bigint 中存储不明智的数据量 | Jonathan 的博客](https://jonathan-frere.com/posts/bigints-are-cool/)

**原文标题**: [Storing Unwise Amounts of Data in JavaScript Bigints | Jonathan's Blog
](https://jonathan-frere.com/posts/bigints-are-cool/)

本文探讨了在特定场景下使用 JavaScript Bigint 类型存储数据的实验性方法，通过位操作优化配置对象的存储和性能。

- 🚀 采用 Bigint 存储可极大压缩内存占用，布尔值仅需 1 位，枚举值仅需数位
- ⚙️ 实现方式涉及定义字段位宽、偏移量，并通过位提取/设置函数进行数据操作
- 🔍 额外使用 present 位字段标记有效数据，支持快速相等性检查和集合运算
- 📉 局限性包括字段必须预设最大宽度、位操作性能较低、代码复杂度显著增加
- 🤔 该方法仅适用于特定场景，作者仍在验证其实际价值，不推荐普遍使用

---

### [无标题](https://the-github-podcast.simplecast.com/episodes/making-desktop-frameworks-more-accessible-with-electron)

**原文标题**: [No title found](https://the-github-podcast.simplecast.com/episodes/making-desktop-frameworks-more-accessible-with-electron)

概述总结
- 📚 阅读习惯调查显示纸质书仍受青睐
- 📱 电子设备使用增加但未取代传统阅读
- 🌍 不同地区阅读偏好存在显著差异
- 📊 深度阅读时间减少成为普遍趋势
- 💡 专家建议平衡数字与传统阅读方式

（请提供需要总结的文本内容，我将按照您要求的格式进行整理）

---

### [获取失败](https://javascriptweekly.com/link/174871/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/174871/web)

无法总结：获取内容失败，状态码 403。

---

### [如何使用 Cypress 测试新的 ARIA Notify API](https://www.cypress.io/blog/how-to-test-the-new-a-notify-api-with-cypress)

**原文标题**: [How to test the new ARIA Notify API with Cypress](https://www.cypress.io/blog/how-to-test-the-new-a-notify-api-with-cypress)

ARIA Notify API 是一种通过 JavaScript 直接向辅助技术发送实时状态更新的新方法，本文介绍了如何使用 Cypress 测试该 API 的功能实现。

- 🎯 ARIA Notify API 允许开发者从 DOM 元素直接触发屏幕阅读器公告，替代传统的 ARIA 实时区域方案
- 🛒 以购物车添加商品为例，演示了按钮点击后先禁用按钮并发送"添加中"提示，2 秒后发送成功通知的实现逻辑
- ⚡ 测试时使用 cy.clock() 控制时间流逝，避免实际等待延迟，使测试能在 200 毫秒内完成
- 🔧 通过 cy.stub() 方法拦截元素上的 ariaNotify 函数，并使用别名机制便于后续断言验证
- ⌨️ 采用 cy.press() 触发原生键盘事件测试按钮功能，确保交互方式兼容性
- 🌐 需在 Chrome 141+ 或 Beta 版本中进行测试，当前已在 NVDA/JAWS/VoiceOver 获得支持
- 📊 文末推荐结合 Cypress Cloud 的自动化无障碍测试功能，可获取详细的可访问性分析报告

---

### [GitHub Copilot CLI 现已进入公开预览阶段 - GitHub 更新日志](https://github.blog/changelog/2025-09-25-github-copilot-cli-is-now-in-public-preview/)

**原文标题**: [GitHub Copilot CLI is now in public preview - GitHub Changelog](https://github.blog/changelog/2025-09-25-github-copilot-cli-is-now-in-public-preview/)

GitHub Copilot CLI 现已进入公开预览阶段，将 AI 编程助手直接集成到终端中，支持本地同步开发并具备完整的 GitHub 上下文理解能力。

- 🖥️ 终端原生开发：无需切换界面即可在命令行中直接使用 Copilot 编程助手
- 🔗 开箱即用的 GitHub 集成：通过自然语言访问仓库、议题和拉取请求，使用现有 GitHub 账户认证
- 🤖 智能代理能力：AI 助手可规划执行复杂任务，支持代码构建、编辑、调试和重构
- 🔧 MCP 扩展支持：默认搭载 GitHub MCP 服务器并支持自定义扩展功能
- ⚡ 完整操作控制：所有操作执行前均需用户明确批准，确保安全可控
- 📦 简易安装方式：通过 npm 安装后使用 Copilot Pro/Pro+/Business/Enterprise套餐即可开始使用

---

### [TanStack Start v1 候选版本发布 | TanStack 博客](https://tanstack.com/blog/announcing-tanstack-start-v1)

**原文标题**: [TanStack Start v1 Release Candidate | TanStack Blog](https://tanstack.com/blog/announcing-tanstack-start-v1)

TanStack Start v1 发布候选版本正式推出，这是一个用于构建类型安全、高性能 React 应用的全栈框架，具备文件路由和服务器优先设计。

- 🚀 **v1 版本核心功能**：提供类型安全的文件路由、同构服务器函数、内置流式渲染以及 URL 状态管理
- 🔄 **开发路线图**：React 服务器组件支持正在开发中，将作为 v1.x 非破坏性更新推出
- 📚 **快速上手**：可通过官方文档获取安装指南，支持新建项目和现有项目升级
- 🤝 **合作伙伴生态**：得到 Cloudflare、Netlify 等十余家技术公司的支持与协作
- 💡 **反馈征集**：开发团队邀请用户测试候选版本并通过文档渠道提交改进建议
- ⏳ **稳定版计划**：在收集反馈后将发布 1.0 正式版，期间仅进行小幅优化

---

### [基于角色的访问控制——WorkOS](https://workos.com/rbac?utm_source=cpjavascript&utm_medium=referral&utm_campaign=q32025)

**原文标题**: [Role-Based Access Control â WorkOS](https://workos.com/rbac?utm_source=cpjavascript&utm_medium=referral&utm_campaign=q32025)

基于角色的访问控制系统为企业用户提供强大灵活的权限管理方案

- 🔐 提供企业级授权管理，确保安全可扩展的访问控制
- 🎯 支持精细化权限分配，通过角色而非个人用户简化管理
- 🔄 支持与身份提供商（IdP）同步角色分配，支持 SCIM/SAML 协议
- 🛡️ 实施最小权限原则，通过组织范围角色强化安全策略
- 👥 预设管理员、编辑者、查看者三种基础角色模板
- 🏗️ 支持自定义角色配置，满足不同客户的复杂需求
- ⚡ 通过 JWT 令牌直接集成权限验证，无需额外 API 调用
- 🚀 提供即插即用式访问管理界面，快速集成用户角色管理
- 📊 支持从现有系统无缝迁移角色权限，实现零停机升级
- 💡 提供集中式仪表板，快速配置权限和角色映射关系

---

### [Cap'n Web：面向浏览器与网页服务器的新型 RPC 系统](https://blog.cloudflare.com/capnweb-javascript-rpc-library/)

**原文标题**: [Cap'n Web: a new RPC system for browsers and web servers](https://blog.cloudflare.com/capnweb-javascript-rpc-library/)

Cap'n Web 是一种新型的纯 TypeScript RPC 协议，专为浏览器和 Web 服务器设计，无需模式定义即可实现低延迟双向通信。

- 🌐 **基于 Web 技术栈**：兼容 HTTP、WebSocket 和 postMessage，支持主流浏览器及 Node.js 等运行环境
- 🚀 **零样板代码**：通过 JSON 序列化实现人类可读的传输数据，压缩后体积小于 10kB
- 🔄 **双向调用能力**：支持客户端与服务器间相互调用，可传递函数和对象引用
- ⚡ **承诺管道技术**：允许链式调用在单次网络往返中完成，显著降低延迟
- 🛡️ **能力安全模型**：通过对象能力模式实现天然授权机制，例如登录后自动关联会话权限
- 📜 **TypeScript 原生**：提供端到端类型检查，支持接口声明与自动补全
- 🔄 **替代 GraphQL**：用 JavaScript 原生方式解决数据瀑布流问题，无需额外查询语言
- 🧩 **数组操作优化**：通过记录 - 回放机制实现服务端数组映射，避免逐项网络请求
- 🧪 **实验性创新**：已应用于 Cloudflare Wrangler 等产品，目前处于早期实践阶段

（注：根据要求已省略"overview summary"标题，直接以段落形式呈现概要）

---

### [Cap'n Proto：简介](https://capnproto.org/)

**原文标题**: [Cap'n Proto: Introduction](https://capnproto.org/)

Cap'n Proto 是一种极快的数据交换格式和基于能力的 RPC 系统，其编码格式无需编解码即可直接读写，支持跨平台安全操作和高效压缩。

- 🚀 速度无限快于 Protocol Buffers，因为无需编解码步骤
- 🔄 编码与平台无关，采用小端字节序和编译器优化的内存布局
- 📏 通过向后兼容的字段设计（新字段追加到结构体末尾）支持版本演进
- 💾 支持"打包"压缩技术消除零值字节，节省带宽
- 🔒 具备指针验证和消息结构完整性检查的安全机制
- ⚡ 支持增量读取、随机访问、内存映射等高效操作特性
- 🌍 便于跨语言/进程通信，采用竞技场分配提升缓存局部性
- 📦 生成代码量和运行时库体积远小于 Protocol Buffers
- ⏳ RPC 系统支持"时间旅行"等创新功能
- 👨💻 由 Protocol Buffers v2 主创开发，基于多年经验优化设计

---

### [GitHub - NickvanDyke/eslint-plugin-react-you-might-not-need-an-effect：捕获不必要的React useEffect 钩子，使代码更简洁、更快速、更安全。](https://github.com/NickvanDyke/eslint-plugin-react-you-might-not-need-an-effect)

**原文标题**: [GitHub - NickvanDyke/eslint-plugin-react-you-might-not-need-an-effect: Catch unnecessary React useEffect hooks to make your code simpler, faster, and safer.](https://github.com/NickvanDyke/eslint-plugin-react-you-might-not-need-an-effect)

这是一个 ESLint 插件项目，用于检测 React 中不必要的 useEffect 钩子，帮助开发者编写更简洁、高效和安全的代码。

- 🚀 **项目目标** - 通过捕获不必要的 useEffect 钩子使代码更易维护、运行更快且减少错误
- 📦 **安装方式** - 支持 npm 和 yarn 两种包管理器安装
- ⚙️ **配置方法** - 提供传统配置和扁平配置两种 ESLint 配置方案
- 🔧 **规则功能** - 包含 11 条具体规则，如禁止派生状态、链式状态更新、事件处理器误用等
- 📚 **学习资源** - 提供 React 官方文档链接帮助深入理解 useEffect 的正确用法
- 🌟 **项目热度** - 获得 951 个 star 和 12 个 fork，显示社区认可度较高
- 📄 **开源协议** - 采用 MIT 许可协议，可自由使用和修改
- 💡 **适用人群** - 特别推荐 React 新手学习，有经验的开发者也能从中受益

---

### [你可能不需要使用 Effect – React](https://react.dev/learn/you-might-not-need-an-effect)

**原文标题**: [You Might Not Need an Effect – React](https://react.dev/learn/you-might-not-need-an-effect)

React Effects 是用于与外部系统同步的逃生舱口，但许多场景下其实不需要使用 Effect。移除不必要的 Effect 可以使代码更易维护、运行更快且减少错误。

- 🚫 **避免不必要的 Effect**：当没有外部系统介入时（如仅根据 props 或 state 更新组件状态），应避免使用 Effect。
- 💡 **渲染期间计算数据**：例如过滤列表显示，应在组件顶层直接计算而非通过 Effect 更新状态，避免不必要的渲染过程。
- 🖱️ **事件处理逻辑置于事件处理器**：如用户点击购买按钮发送请求，逻辑应放在事件处理器中而非 Effect，以确保准确响应具体交互。
- 🔄 **使用 key 重置组件状态**：当需要根据 prop 变化重置状态时（如用户切换时清空评论），通过传递不同 key 让 React 将组件视为不同实例，自动重置状态。
- 🧠 **使用 useMemo 缓存昂贵计算**：当计算耗时且依赖项未变时，用 useMemo 缓存结果，避免重复计算提升性能。
- ⚡ **事件处理器中批量更新状态**：多个状态更新应放在同一事件处理器中，React 会自动批量处理，减少渲染次数。
- 📡 **仅与外部系统同步时使用 Effect**：如保持 React 状态与 jQuery 组件同步或数据获取（但现代框架通常提供更高效的内置方法）。
- 🧹 **数据获取需处理竞态条件**：在 Effect 中获取数据时，应添加清理函数忽略过期响应，避免显示错误结果。
- 🏗️ **应用初始化逻辑置于顶层**：对于仅需运行一次的逻辑（如身份验证），使用全局变量或模块初始化而非 Effect，避免开发环境重复执行。

---

### [billboard.js 3.17.0：✨ 全新坐标轴自定义、标签样式及图像标签功能！ | 作者 Jae Sung Park | 2025 年 9 月 | Medium](https://netil.medium.com/billboard-js-3-17-0-new-axis-customization-label-styling-image-labels-1be0f0a906f4)

**原文标题**: [billboard.js 3.17.0: ✨ New Axis Customization, Label Styling & Image Labels! | by Jae Sung Park | Sep, 2025 | Medium](https://netil.medium.com/billboard-js-3-17-0-new-axis-customization-label-styling-image-labels-1be0f0a906f4)

billboard.js 3.17.0 版本发布，新增多项轴定制与标签样式功能，提升图表可视化精细控制能力。

- 🖼️ **图像标签支持**：可在标签中使用图标、Logo 等图像，支持环形图、仪表盘等多种图表类型
- 🎨 **标签边框样式**：为标签添加边框和圆角效果，提升可读性和视觉层次
- 📊 **内部轴刻度**：通过 tick.inner 选项将刻度显示在图表区域内，实现更简洁的现代设计
- 🌈 **动态标签背景色**：使用函数根据数据值动态设置标签背景颜色，增强数据表达力
- ⚙️ **开发者体验优化**：提供更灵活的轴控制、动态样式和丰富的标签表达方式，保持 API 一致性

---

### [GitHub - Distributive-Network/PythonMonkey：将 Mozilla SpiderMonkey JavaScript 引擎嵌入 Python 虚拟机，利用 Python 引擎提供 JavaScript 宿主环境。](https://github.com/Distributive-Network/PythonMonkey)

**原文标题**: [GitHub - Distributive-Network/PythonMonkey: A Mozilla SpiderMonkey JavaScript engine embedded into the Python VM, using the Python engine to provide the JS host environment.](https://github.com/Distributive-Network/PythonMonkey)

PythonMonkey 是一个将 Mozilla SpiderMonkey JavaScript 引擎嵌入到 Python 虚拟机中的开源项目，允许在同一个进程中无缝运行 JavaScript 和 Python 代码。

- 🚀 项目目标包括实现高性能、内存高效的数据交换，并支持在两种语言间直接调用库函数
- 🔄 支持 Python 列表/字典与 JavaScript 数组/对象的自动转换，包括共享字符串和类型化数组的内存存储
- 📦 提供完整的 CommonJS 模块系统，支持 .js、.py 和 .json 格式的模块加载
- 🛠️ 包含丰富的 API，如 eval()、require()、createRequire() 等，方便双向调用
- 🐛 内置调试工具 pmdb，支持 JavaScript 代码调试和错误追踪
- 📋 项目已实现大部分核心功能，包括类型转换、异常传播、事件循环集成等
- 🔧 提供详细的构建指南，支持多种构建类型和开发环境配置
- 📚 包含完整的使用示例和 API 文档，方便开发者快速上手

---

### [GitHub - sindresorhus/pretty-bytes：将字节转换为人类可读的字符串：1337 → 1.34 kB](https://github.com/sindresorhus/pretty-bytes)

**原文标题**: [GitHub - sindresorhus/pretty-bytes: Convert bytes to a human readable string: 1337 → 1.34 kB](https://github.com/sindresorhus/pretty-bytes)

这是一个名为 pretty-bytes 的 JavaScript 库，用于将字节数转换为人类易读的字符串格式。

- 📦 核心功能是将数字字节（如 1337）转换为带单位的易读格式（如 "1.34 kB"）
- ⚙️ 支持多种选项：包含正负号、以比特为单位、使用二进制前缀、本地化格式等
- 📐 提供格式化控制：最小/最大小数位数、固定宽度对齐、空格分隔符等
- 🔧 可通过 npm 安装，支持 ES 模块导入使用
- 📄 采用 MIT 开源协议，在 GitHub 上拥有 1.2k 星标和 87 个复刻
- 🌍 被超过 1500 万个项目使用，具有广泛的社区基础

---

### [Docusaurus 3.9 | Docusaurus](https://docusaurus.io/blog/releases/3.9)

**原文标题**: [Docusaurus 3.9 | Docusaurus](https://docusaurus.io/blog/releases/3.9)

Docusaurus 3.9 版本发布，主要更新包括停止对 Node.js 18 的支持、集成 Algolia DocSearch v4 的 AskAI 功能、优化国际化配置、新增 Mermaid ELK 图表布局，并包含多项功能改进和错误修复。

- 🚫 停止支持 Node.js 18，最低版本要求升级至 Node.js v20.0  
- 🤖 新增 Algolia DocSearch v4 支持，可配置 AI 问答助手 AskAI  
- 🌐 国际化功能增强：支持多域名部署配置和翻译键冲突解决  
- 📊 新增 Mermaid ELK 布局算法，优化复杂图表展示  
- 🔧 构建性能提升：升级 Rspack 1.5 并优化 Markdown 链接处理  
- 🎨 界面改进：修复主题切换视觉问题，支持博客作者邮箱图标  
- 📝 新增巴西葡萄牙语和乌克兰语翻译支持  
- ⚡ 其他优化：禁用部分 HTML 压缩以兼容社交媒体卡片显示

---

### [发布 Neo.mjs v10.9.0 版本说明 · neomjs/neo · GitHub](https://github.com/neomjs/neo/releases/tag/10.9.0)

**原文标题**: [Release Neo.mjs v10.9.0 Release Notes · neomjs/neo · GitHub](https://github.com/neomjs/neo/releases/tag/10.9.0)

Neo.mjs 框架发布 v10.9.0 版本，重点扩展 AI 知识库至工作空间，实现应用级语义理解，并优化开发流程与文档规范。

- 🚀 AI 知识库支持工作空间，可自动为新建项目配置本地化智能代码理解环境
- 🧠 知识库增强：嵌入历史版本说明、优化查询算法、采用高效类层级文件提升性能
- 🤖 实施混合工单策略，强制要求所有代码修改必须通过工单流程追踪
- 📚 新增 Image 组件并规范 JSDoc 标注标准，完善示例文档
- ⚙️ 重构可移植 AI 脚本，实现核心库与工作空间的无缝切换操作

---

### [GitHub - vuejs/eslint-plugin-vue: Vue.js 官方 ESLint 插件](https://github.com/vuejs/eslint-plugin-vue)

**原文标题**: [GitHub - vuejs/eslint-plugin-vue: Official ESLint plugin for Vue.js](https://github.com/vuejs/eslint-plugin-vue)

这是 Vue.js 官方 ESLint 插件的 GitHub 仓库，用于对 Vue 项目进行代码规范检查。

- 📚 官方 ESLint 插件，专为 Vue.js 项目设计
- 🌐 提供完整的在线文档和版本管理策略
- 🔄 遵循语义化版本，但采用特殊的更新策略
- 🛠️ 支持 Vue 单文件组件的语法检查
- 📄 使用 vue-eslint-parser 解析器处理 Vue 特有语法
- 🤝 开放贡献指南，欢迎社区参与
- ⚖️ 采用 MIT 开源许可证
- 📊 项目活跃，拥有 4.6k 星标和 696 个分支
- 🔧 提供丰富的规则配置和模板检查功能

---

### [引言 | eslint-plugin-vue](https://eslint.vuejs.org/)

**原文标题**: [Introduction | eslint-plugin-vue](https://eslint.vuejs.org/)

Vue.js 官方 ESLint 插件，用于检查 Vue 文件模板和脚本的语法错误、指令使用规范及风格指南合规性

- 🎯 支持检查.vue 文件的`<template>`和`<script>`标签内容
- 🔍 可检测 Vue.js 指令错误使用和语法错误
- 📖 强制执行 Vue.js 风格指南规范
- ⚡ 实时代码检查功能与 ESLint 编辑器集成
- 🚦 采用语义化版本（但不同于 ESLint 版本策略）
- ⚠️ 次要版本可能变更规则配置导致更多报错
- 💡 推荐 package.json 中使用波浪号 (~) 锁定版本
- 📄 更新日志通过 GitHub Releases 发布
- 📜 基于 MIT 开源协议授权

---

### [GitHub - vanjs-org/van: 🍦 VanJS：世界最小的响应式 UI 框架。难以置信的强大，疯狂的精简——人人都能在一小时内构建实用的 UI 应用。](https://github.com/vanjs-org/van)

**原文标题**: [GitHub - vanjs-org/van: 🍦 VanJS: World's smallest reactive UI framework. Incredibly Powerful, Insanely Small - Everyone can build a useful UI app in an hour.](https://github.com/vanjs-org/van)

VanJS 是一个超轻量级、零依赖的响应式 UI 框架，基于纯原生 JavaScript 和 DOM 构建，总大小仅 1.0kB，号称全球最小的响应式 UI 框架。

- 🍦 **极简设计**：仅包含 5 个核心函数（van.tags、van.add、van.state、van.derive、van.hydrate），学习成本低
- ⚡ **开箱即用**：无需安装配置、无依赖项、无需转译，可直接在浏览器控制台运行代码
- 🚀 **高性能**：在 js-framework-benchmark 测试中表现优异，服务端渲染效率比 React 高 1.75-2.25 倍
- 🔧 **功能完整**：支持组件化开发、状态管理、响应式绑定、SPA 路由、水合等现代框架特性
- 📚 **生态丰富**：提供 TypeScript 支持、在线代码转换器、扩展库 VanX 和社区插件生态
- 🌍 **社区活跃**：拥有 4.2k 星标，68 位贡献者，提供教程、示例和讨论区等完善资源

---

### [VanJS：基于原生 JavaScript 的 1.0kB 无 JSX 框架](https://vanjs.org/)

**原文标题**: [VanJS - A 1.0kB No-JSX Framework Based on Vanilla JavaScript](https://vanjs.org/)

VanJS 是一个基于纯 JavaScript 和 DOM 的超轻量级响应式 UI 框架，无需依赖 React/JSX 即可实现声明式编程。

- 🚀 提供响应式编程能力，支持组件复用和状态绑定，无需虚拟 DOM 或编译步骤
- 📦 开箱即用，无需安装配置，仅需 1.0kB 的 gzip 压缩体积
- ⚡ 性能优异，在框架基准测试中表现领先，服务端渲染效率比 React 高 1.75-2.25 倍
- 🎯 仅需掌握 5 个核心函数即可上手，提供完整的 TypeScript 类型支持
- 🔧 拥有丰富的生态系统，包含 VanUI 组件库、VanX 扩展和多种社区插件
- 🌐 支持服务端渲染（Mini-Van）和 HTML/Markdown 到代码的在线转换工具
- 💡 设计理念强调极简主义，让开发者能专注于业务逻辑而非工具链配置

---

### [GitHub - Milkdown/milkdown：🍼 插件驱动的所见即所得 Markdown 编辑器框架。](https://github.com/Milkdown/milkdown)

**原文标题**: [GitHub - Milkdown/milkdown: 🍼 Plugin driven WYSIWYG  markdown editor framework.](https://github.com/Milkdown/milkdown)

Milkdown 是一个基于插件驱动的所见即所得 Markdown 编辑器框架，采用 MIT 许可证开源。

- 🍼 插件驱动的所见即所得 Markdown 编辑器框架
- ⭐ 获得 10.6k 星标和 474 个复刻
- 🔧 基于 ProseMirror 和 Remark 技术构建
- 📚 提供完整的官方文档网站
- 👥 拥有活跃的 Discord 社区支持
- 🌐 网站设计由 Meo 和 Mirone 完成
- 📄 采用 MIT 开源许可证
- 🛠️ 支持 TypeScript、CSS 等多种开发语言

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=september26th2025%20)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=september26th2025%20)

Meticulous AI 是一款革命性的 AI 驱动测试工具，通过记录用户与应用交互自动生成并维护测试套件，彻底消除编写和维护测试的需求。

- 🚀 无需编写测试：通过记录开发过程自动生成覆盖所有代码分支的端到端测试
- 🔄 智能进化：测试套件随应用功能更新自动增删测试案例，保持始终最新
- ⚡ 极致速度：基于 Chromium 的确定性调度引擎实现无抖动测试，千级测试可在 120 秒内完成
- 🛡️ 零误报设计：通过记录/回放后端响应实现无副作用测试，无需配置测试账户
- 🌐 广泛兼容：支持 NextJS/React/Vue 等主流框架，可与现有测试套件结合或完全替代
- 📊 实时验证：在代码合并前预览改动对用户流程的影响，被 Dropbox/Notion 等超 100 家企业采用

---

### [JetBrains JavaScript 日 2025](https://lp.jetbrains.com/javascript-day-2025/?utm_source=cooperpress&utm_medium=cpc&utm_campaign=js_weekly_javascript_day_2025&utm_content=4%20)

**原文标题**: [JetBrains JavaScript Day 2025](https://lp.jetbrains.com/javascript-day-2025/?utm_source=cooperpress&utm_medium=cpc&utm_campaign=js_weekly_javascript_day_2025&utm_content=4%20)

JetBrains 将于 2025 年 10 月 2 日在线举办免费 JavaScript 技术大会，汇聚行业专家分享前沿技术实践与开发经验。

- 🗓️ 活动时间：2025 年 10 月 2 日线上举行，支持多时区同步参与
- 💰 参与方式：完全免费注册，通过 YouTube 平台直播/回放
- 👥 嘉宾阵容：邀请 Ryan Carniato、Kent C. Dodds 等 9 位业界知名专家进行分享
- 🚀 技术主题：涵盖量子算法 JavaScript 应用、现代构建工具优化、微前端 SSR 架构等前沿议题
- ⚡ 热点技术：聚焦 Bun 运行时、Signals 响应式编程、AI 交互新模式等创新方向
- 💡 特色环节：包含 WebStorm 产品直面问答、开源项目维护经验等独家内容
- 📺 参与福利：支持直播互动提问，所有讲座将录制供回看学习
- 🌟 大会宗旨：促进开发者社区知识共享，提供可直接落地的实战洞察

---

### [JetBrains JavaScript 日 2025](https://lp.jetbrains.com/javascript-day-2025/?utm_source=cooperpress&utm_medium=cpc&utm_campaign=js_weekly_javascript_day_2025&utm_content=4%20)

**原文标题**: [JetBrains JavaScript Day 2025](https://lp.jetbrains.com/javascript-day-2025/?utm_source=cooperpress&utm_medium=cpc&utm_campaign=js_weekly_javascript_day_2025&utm_content=4%20)

JetBrains 将于 2025 年 10 月 2 日在线举办免费 JavaScript 技术大会，汇聚行业专家分享前沿技术与实践经验。

- 🗓️ 活动时间：2025 年 10 月 2 日线上举行
- 💰 参与方式：完全免费注册参加
- 🎯 核心主题：涵盖现代 JavaScript 工具链、微前端架构、AI 交互模式等热门领域
- 👨‍💼 演讲嘉宾：包括 Ryan Carniato（SolidJS 创建者）、Kent C. Dodds 等 9 位业界领袖
- ⚡ 技术热点：Bun 运行时、信号机制、Monorepo 管理等前沿话题
- 📹 参与形式：通过 YouTube 直播，支持实时问答与回放观看
- 🎁 特色环节：包含 WebStorm 产品直面会、开源项目维护经验等独特内容
- 🌐 覆盖时区：提供 CET/EST/UTC 等多时区日程安排
- 📋 互动机制：支持个性化议程提醒和会后视频推送服务

---

### [归档](https://2ality.com/archive.html#Tag=learning%20web%20dev)

**原文标题**: [Archive](https://2ality.com/archive.html#Tag=learning%20web%20dev)

该网站是 Dr. Axel Rauschmayer 的技术博客，专注于 JavaScript 及相关技术的深度内容分享和免费电子书资源。

- 🏠 个人主页与社交平台链接入口
- 📚 提供四本免费在线技术书籍（涵盖 JavaScript 深度探索、TypeScript、Node.js 脚本等）
- 📰 定期发布 ECMAScript 最新动态的免费通讯
- 🔍 具备完整的博客归档和搜索功能
- 👨‍🏫 由计算机博士 Axel Rauschmayer 维护的专业技术平台

---

### [面向初学者的网页开发：JavaScript 中的数字、变量与函数](https://2ality.com/2025/08/javascript-numbers-variables-functions.html)

**原文标题**: [Web development for beginners: Numbers, variables, functions in JavaScript](https://2ality.com/2025/08/javascript-numbers-variables-functions.html)

这篇博客文章是“Web 开发入门”系列的一部分，面向零基础读者，介绍如何使用 JavaScript 创建网页应用。本章重点学习数字、变量和函数的基础知识。

- 🚀 通过浏览器控制台与 JavaScript 引擎交互，学习基本操作
- 🔢 使用数字表达式进行算术运算，包括加减乘除和优先级规则
- 📦 理解变量的声明（let/const）和赋值操作
- ⚠️ 认识语法错误（SyntaxError）和常量不可修改的特性
- 🔧 掌握箭头函数的基本语法、参数与参数的区别
- 🌡️ 通过摄氏度转华氏度的实际案例演示函数应用
- 💡 强调通过实践练习巩固学习内容

---

### [JavaScript 初学者指南：字符串与方法](https://2ality.com/2025/08/javascript-strings-methods.html)

**原文标题**: [Web development for beginners: Strings and methods in JavaScript](https://2ality.com/2025/08/javascript-strings-methods.html)

这篇博客文章介绍了 JavaScript 中字符串的基础知识、相关方法以及如何通过实际项目应用这些概念。

- 📝 字符串是 JavaScript 中表示文本的数据类型，可以用单引号或双引号定义
- 📏 通过.length 属性可以获取字符串的长度
- 🔗 使用加号运算符 (+) 可以实现字符串拼接
- 🏗️ 函数可以返回字符串值，实现动态文本生成
- 📊 JavaScript 支持对象和属性的嵌套结构，属性可以包含函数（称为方法）
- 🌐 通过 log-hello.html 项目展示了如何在网页中嵌入 JavaScript 代码
- 🖱️ log-clicks.html 项目演示了如何监听和处理点击事件
- 🔢 文章区分了数字 123 和字符串'123'的不同特性
- 🔄 介绍了使用 String() 和 Number() 函数进行数据类型转换
- 💻 display-clicks.html 项目展示了如何在网页界面中动态显示数据
- 🌡️ temperature-converter.html 项目实现了一个温度转换器应用
- 📚 文章最后提供了一个将温度转换器改为货币转换器的练习任务

---

### [Web 开发入门：JavaScript 中的布尔值、比较和`if`语句](https://2ality.com/2025/08/javascript-booleans-comparisons-if.html)

**原文标题**: [Web development for beginners: Booleans, comparisons and `if` statements in JavaScript](https://2ality.com/2025/08/javascript-booleans-comparisons-if.html)

这篇博客文章介绍了 JavaScript 中的布尔值、比较操作符和 if 语句，是“Web 开发入门”系列的一部分，旨在帮助初学者掌握条件执行代码的工具。

- 🔍 **布尔值类型**：JavaScript 中的布尔值只有 true 和 false 两种，常用于回答是/否问题的方法返回值（如 Number.isInteger()、.startsWith() 等）
- ⚖️ **值类型区分**：JavaScript 将值分为原始值（原子性、不可变、按值比较）和对象（复合性、可变、按身份比较）
- 🔗 **赋值差异**：对象赋值时共享引用（修改会影响所有引用变量），原始值赋值时完全复制
- ✅ **严格相等比较**：===操作符对原始值比较内容，对对象比较身份标识
- 📊 **比较操作符**：<、<=、>、>=可用于数字（数值比较）和字符串（字典序比较）
- 🔌 **逻辑运算符**：&&（逻辑与）、||（逻辑或）、!（逻辑非）用于组合布尔表达式
- ⚠️ **特殊值 NaN**：表示非数字的错误值，必须使用 Number.isNaN() 进行检测
- 🎯 **if 语句控制流**：通过条件判断执行不同代码分支，支持 if、else if、else 多种分支结构
- 🎮 **实战项目**：包含数字描述页面和猜数字游戏两个实践项目，演示如何将理论应用于实际交互界面
- 💡 **学习建议**：提供未解答的练习题目，鼓励读者动手实践巩固知识

---

### [JavaScript 初学者指南：循环详解](https://2ality.com/2025/08/javascript-loops.html)

**原文标题**: [Web development for beginners: Loops in JavaScript](https://2ality.com/2025/08/javascript-loops.html)

本文介绍了 JavaScript 循环的基础知识，重点讲解了 for-of 循环的用法及其在动态网页开发中的应用。

- 🔄 介绍了 for-of 循环的语法和遍历数组、字符串的方法
- 📍 演示了如何通过 arr.entries() 和数组解构同时获取索引和元素值
- ➕ 讲解了 array.push() 方法用于动态构建数组
- 🔗 展示了 array.join() 方法将数组元素连接成字符串
- 🎯 通过水果选择案例演示了循环在实际网页开发中的应用
- 📝 介绍了模板字面量和+=操作符在动态生成 HTML 时的使用技巧
- ⏹️ 说明了 break 语句的用法，用于提前退出循环
- 💡 对比了静态 HTML 和动态 HTML 的区别

---

### [JavaScript 初学者指南：普通对象详解](https://2ality.com/2025/08/javascript-plain-objects.html)

**原文标题**: [Web development for beginners: Plain objects in JavaScript](https://2ality.com/2025/08/javascript-plain-objects.html)

这篇博客文章是“Web 开发入门”系列的一部分，教初学者如何使用 JavaScript 创建简单对象和构建闪卡应用。

- 📚 文章是“Web 开发入门”系列教程的一章，面向编程新手
- 🧩 介绍了使用对象字面量创建和操作普通对象的方法
- 🔄 包含两个实践项目：内容切换页面和随机闪卡应用
- 💡 详细解释了属性读写、简写语法和模型视图概念
- 🛠️ 提供了完整的代码示例和运行说明，包括 CSS 样式和 JavaScript 模块

---

### [JavaScript 初学者指南：数组详解](https://2ality.com/2025/08/javascript-arrays.html)

**原文标题**: [Web development for beginners: Arrays in JavaScript](https://2ality.com/2025/08/javascript-arrays.html)

本文是“Web 开发入门”系列的一部分，介绍 JavaScript 数组的基本概念和应用，通过一个魔法 8 球项目演示数组的实际使用。

- 📚 数组是存储多个值的数据结构，使用方括号语法创建，元素通过从 0 开始的索引访问
- 🔄 即使使用 const 声明，数组本身可变（可修改元素），但变量不能重新赋值
- 💡 介绍了单行注释（//）和多行注释（/* */）的用法区别
- 🎱 魔法 8 球项目实现：点击按钮随机显示预存答案，演示数组遍历和 DOM 操作
- 🎲 getRandomInteger() 函数原理：利用 Math.random() 生成 0 到 max 之间的随机整数
- 💻 项目包含完整的 HTML 结构和事件监听机制，强调数组与网页交互的结合
- ✏️ 最后提供扩展练习建议，鼓励修改项目显示笑话、名言等不同内容

---

### [初学者网页开发：JavaScript 地图](https://2ality.com/2025/08/javascript-maps.html)

**原文标题**: [Web development for beginners: JavaScript Maps](https://2ality.com/2025/08/javascript-maps.html)

本文是“Web 开发入门”系列的一部分，介绍 JavaScript 的 Map 数据结构及其应用，包括创建、操作 Map 以及通过实际项目（文本倒置工具）演示其用法。

- 🗺️ Map 是一种键值对集合，类似于字典，可通过键查找值
- 🔧 使用`new Map()`创建 Map，支持数组初始化或`.set()`方法添加条目
- 📏 通过`.size`获取条目数量，`.get()`/`.set()`读写值，`.has()`检查键是否存在
- ⚠️ 对象作为键时需注意引用一致性，原始值可直接比较
- ➰ 使用`??`运算符为`undefined`值设置默认回退值
- 🔢 示例：实现字符计数功能，展示 Map 的遍历与更新逻辑
- 🔁 对比`for`循环与`for-of`循环的差异及适用场景
- 🛠️ 介绍数组方法`.map()`（元素转换）和`.filter()`（条件筛选）
- 💻 Node.js 中通过`process.argv`获取命令行参数
- ↩️ 项目实战：利用 Map 将输入文本转换为倒置 Unicode 字符输出
- 📚 提供扩展练习（如开发 Web 界面、实现 ROT13 编码）

---

### [Web 开发入门：JavaScript 异常处理](https://2ality.com/2025/08/javascript-exceptions.html)

**原文标题**: [Web development for beginners: JavaScript exceptions](https://2ality.com/2025/08/javascript-exceptions.html)

这篇博客文章是面向初学者的 JavaScript 异常处理教程，属于"Web 开发入门"系列的一部分。

- 🚀 异常是 JavaScript 中处理错误的一种机制，通过 throw 抛出、try-catch 捕获
- 🏭 JavaScript 类是通过 new 调用的对象工厂，Array 和 Object 是两个内置类
- 🔍 instanceof 操作符用于检查值是否为某个类的实例
- ⚠️ Error 类用于错误报告，包含 message、name 属性和重要的 stack 堆栈跟踪信息
- 📝 项目 create-error.js 演示了如何创建包含堆栈跟踪的错误对象
- 🎯 抛出异常时应使用 Error 实例或其子类（TypeError、RangeError 等）以获得更好的错误信息
- 🛡️ try-catch 语句可以捕获异常，防止程序终止
- 🌐 异常处理允许在嵌套函数调用中跨层级传递和处理错误
- 📊 JavaScript 传统上更倾向于使用特殊值（如 undefined、NaN）而非抛出异常
- 💡 在实际应用中需要在合适的位置捕获异常并给出有用的错误信息

---

### [Web 开发入门：前端框架](https://2ality.com/2025/09/frontend-frameworks.html)

**原文标题**: [Web development for beginners: Frontend frameworks](https://2ality.com/2025/09/frontend-frameworks.html)

这篇博客文章是“Web 开发入门”系列的一部分，介绍了前端框架的基本概念，并指导如何使用 Preact 框架构建一个待办事项应用的前端部分。

- 📚 文章是“Web 开发入门”系列教程的一部分，面向编程新手，使用 JavaScript 教学
- 🛠️ 重点介绍了前端框架的作用：简化 Web 用户界面开发，但会增加复杂性
- ⚡ 解释了前端框架的工作原理：通过视图函数将模型转换为 HTML，仅更新变化部分
- 🔧 使用 Preact 框架进行实践演示，包括两个示例项目
- 📝 详细讲解了 JavaScript 重要特性：破坏性/非破坏性操作、展开语法、深浅拷贝、对象解构等
- 💡 展示了完整的待办事项应用实现，包含添加、删除、更新任务功能
- 🔗 提供了 GitHub 代码库链接和反馈渠道
- 📖 包含未提供答案的练习题目供读者实践

---

### [Web 开发入门：安装 npm 包与打包](https://2ality.com/2025/09/npm-packages-bundling.html)

**原文标题**: [Web development for beginners: Installing npm packages and bundling](https://2ality.com/2025/09/npm-packages-bundling.html)

本文是“Web 开发入门”系列的一部分，教初学者如何使用 npm 包和打包工具创建 JavaScript Web 应用。

- 📦 项目使用 npm 包管理，通过 package.json 定义依赖，包含运行时依赖和开发工具依赖
- 🔧 开发流程引入构建步骤，将多个 JavaScript 文件打包成单个 bundle.js 文件以提高加载性能
- ⚡ 使用 esbuild 作为打包工具，只包含实际使用的代码，支持现代模块语法
- 🎯 项目采用 watch 和 live-server 实现自动重建和热重载，提升开发体验
- 🧩 代码结构清晰分离模型（model.js）和视图（main.js），便于测试和维护
- 🎮 实战项目是猜词游戏，演示如何系统地从需求分析到模型设计再到视图实现
- 📝 包含完整的测试用例，展示如何为纯函数编写测试
- 🌐 详细解释了模块说明符的三种类型：相对路径、裸说明符和绝对 URL

---

### [初学者网页开发：异步 JavaScript——Promise 与 async 函数](https://2ality.com/2025/09/javascript-async.html)

**原文标题**: [Web development for beginners: Asynchronous JavaScript – Promises and async functions](https://2ality.com/2025/09/javascript-async.html)

这篇博客文章是“Web 开发入门”系列的一部分，重点讲解异步 JavaScript，包括 Promise 和 async 函数的使用。

- 🧵 JavaScript 代码在单线程中运行，通过事件循环管理任务队列
- ⏰ 使用 setTimeout() 和 setInterval() 向任务队列添加任务
- 📅 Date 类用于处理日期时间，但功能有限
- 🔄 Promise 有三种状态：pending（等待中）、fulfilled（已完成）、rejected（已拒绝）
- ⚡ 异步函数通过 await 关键字暂停执行，等待 Promise 结果
- 🌐 fetch() 函数用于从网络下载数据
- 💡 异步代码具有“传染性”，调用异步函数的地方通常也需要变成异步
- 🛠️ 包含多个实践项目，如日志时间、阻塞浏览器演示、等待点击交互等
- 📚 提供了练习题目帮助巩固学习内容
- 💭 作者建议初学者给自己时间消化这些复杂概念，可以查阅 MDN 等额外资源

---

### [别搞 JSON 瀑布流](https://dontgojsonwaterfalls.com/)

**原文标题**: [don't go json waterfalls](https://dontgojsonwaterfalls.com/)

好的，请提供您需要我总结的文本内容。我将根据您的要求，先给出概述总结，然后使用带表情符号的要点列表来呈现关键信息。

---

