### [React Status Issue 455: December 10, 2025](https://react.statuscode.com/issues/455)

**原文标题**: [React Status Issue 455: December 10, 2025](https://react.statuscode.com/issues/455)

总结失败：Error code: 503 - {'error': {'message': 'Service is too busy. We advise users to temporarily switch to alternative LLM API service providers.', 'type': 'service_unavailable_error', 'param': None, 'code': 'service_unavailable_error'}}

---

### [React Grab for Agents](https://www.react-grab.com/blog/agent)

**原文标题**: [React Grab for Agents](https://www.react-grab.com/blog/agent)

总结失败：Expecting value: line 10 column 1 (char 9)

---

### [GitHub - aidenybai/react-scan: Scan for React performance issues and eliminate slow renders in your app](https://github.com/aidenybai/react-scan)

**原文标题**: [GitHub - aidenybai/react-scan: Scan for React performance issues and eliminate slow renders in your app](https://github.com/aidenybai/react-scan)

React Scan 是一款用于自动检测 React 应用性能问题的工具，无需代码更改即可快速识别和优化慢渲染组件，提升应用性能。

- 🔍 **自动检测性能问题**：无需代码更改，直接集成即可扫描 React 应用中的渲染性能问题。
- 🚀 **快速上手**：支持通过 CLI 命令（如 `npx react-scan localhost:3000`）或包管理器安装，5 秒内即可试用。
- 🛠️ **可视化调试工具**：提供工具栏，支持渲染轮廓显示、组件重渲染原因分析，以及性能剖析功能。
- 📊 **智能性能剖析**：通过性能剖析器识别 FPS 下降或慢交互，提供组件渲染时间排名和优化建议。
- 🔧 **灵活配置选项**：支持自定义扫描选项，如启用/禁用扫描、动画速度控制，以及生产环境强制运行（不推荐）。
- 🌐 **多平台支持**：兼容 Next.js、Vite、Create React App 等多种框架，并提供浏览器扩展和 React Native 支持。
- 📈 **生产环境监控**：提供 React Scan Monitoring 服务，帮助在生产环境中持续监控性能问题。
- 🤝 **开源与社区**：基于 MIT 许可证开源，拥有活跃的社区和贡献者，提供 Discord 交流和 GitHub 协作。

---

### [React 19.2：INP 优化再进一步 - 网页性能日历](https://calendar.perfplanet.com/2025/react-19-2-further-advances-inp-optimization/)

**原文标题**: [  React 19.2. Further Advances INP Optimization - Web Performance Calendar](https://calendar.perfplanet.com/2025/react-19-2-further-advances-inp-optimization/)

React 19.2 版本引入了两项关键新功能，旨在帮助开发者优化应用性能，特别是改善 INP（Interaction to Next Paint）指标。新组件<Activity>通过状态保留和低优先级渲染来管理 UI 的显示与隐藏，减少不必要的渲染负担；同时，Chrome DevTools 中的 Performance Tracks 功能集成了 React 事件、组件渲染和服务器操作的可视化时间线，使性能调试更加直观高效。

- 🆕 **React 19.2 新组件<Activity>**：解决 UI 隐藏时状态丢失或无效渲染的问题，通过`mode`参数（`hidden`/`visible`）控制组件可见性，隐藏时保留本地状态和 DOM 状态，并暂停副作用执行。
- ⚡ **低优先级渲染与预渲染**：隐藏组件更新被设为最低优先级，避免阻塞用户交互；组件在 hydration 阶段预渲染，加速 UI 切换体验。
- 🔍 **选择性 Hydration 支持**：类似`<Suspense>`，将组件树分割为独立单元，实现按需水合，提升性能。
- ⚠️ **SSR 注意事项**：服务器渲染时隐藏的 Activity 组件不会输出 HTML，可能影响 SEO，需谨慎用于关键内容。
- 📊 **Performance Tracks 调试工具**：在 Chrome DevTools 中集成 React 调度、组件渲染和服务器操作的时间线，帮助识别性能瓶颈（如级联更新）和过度渲染问题。
- 🛠️ **组件与服务器跟踪**：Components Track 以火焰图展示组件渲染频率和时长；Server Track 监控 SSR 中的 Node.js 操作，适用于混合应用调试。
- 🚀 **性能优化结论**：结合 Activity 组件和 Performance Tracks，开发者可深入分析并优化 React 应用，实现更快的交互响应。

---

### [交互到下一次绘制 (INP)  |  文章  |  web.dev](https://web.dev/articles/inp)

**原文标题**: [Interaction to Next Paint (INP)  |  Articles  |  web.dev](https://web.dev/articles/inp)

Interaction to Next Paint (INP) 是一项用于评估网页响应速度的核心 Web 性能指标，它通过观察用户与页面所有交互的延迟情况，并报告一个代表绝大多数交互体验的单一数值。低 INP 值意味着页面能快速响应绝大多数用户交互。

- 📊 **INP 是一项核心 Web 性能指标**：它通过事件计时 API 数据评估页面的整体响应能力，关注从用户开始交互到浏览器绘制下一帧之间的总延迟。
- 🎯 **评估标准**：INP 值在 200 毫秒或以下表示响应良好，200 至 500 毫秒之间表示需要改进，超过 500 毫秒则表示响应较差。
- 🔄 **与 FID 的区别**：INP 是首次输入延迟（FID）的继任者。FID 仅测量页面首次交互的输入延迟，而 INP 观察页面生命周期内的所有交互（点击、轻触、按键），并涵盖从输入延迟、事件处理到下一帧绘制的完整过程。
- 📈 **测量方式**：可通过真实用户监控（RUM）在实地收集数据，或在实验室环境中模拟用户交互进行测量。Chrome 用户体验报告（CrUX）和 web-vitals JavaScript 库是常用的测量工具。
- ⚠️ **注意事项**：并非所有用户交互（如滚动、悬停）都被 INP 考量。如果页面没有发生被测量的交互，则可能无法报告 INP 值。此外，iframe 内的交互会影响顶级页面的 INP，但 JavaScript API 可能无法直接访问这些数据。
- 🛠️ **优化资源**：存在专门的指南合集帮助开发者识别并优化导致 INP 值过高的慢速交互，以提升用户体验。

---

### [2025 年 - 网页性能日历](https://calendar.perfplanet.com/2025/)

**原文标题**: [  2025 - Web Performance Calendar](https://calendar.perfplanet.com/2025/)

本文介绍了 2025 年 Web 性能日历中的一系列文章，涵盖了从性能优化工具、框架最佳实践、性能报告、技术趋势到具体优化技巧等多个方面，旨在帮助开发者提升网页性能。

- 🛠️ 回顾了经典性能工具 YSlow，并介绍了 React 19.2 中优化 INP（交互到下一次绘制）的进展
- 📊 讨论了如何通过有效的案例研究和性能报告向业务方传达性能价值，避免技术指标过于抽象
- 🔮 指出 2025 年 Web 性能的重点从优化转向预测，追求真正的即时加载体验
- ⚡ 提倡用 HTML 和 CSS 替代部分 JavaScript 工作负载（NoLoJS），以减少阻塞并提升性能
- 🖼️ 探讨了在 Canvas 中非阻塞渲染大图像的方法，以保持主线程响应性
- 🚀 强调“默认快速”的开发理念，通过持续监控避免性能问题累积
- 🤖 介绍了利用机器学习进行流量建模，以更准确地模拟真实用户场景
- 📄 分析了大型 HTML 文档的构成及优化方向，避免资源嵌入导致文档臃肿
- 🌊 提出通过 HTTP 流式传输提升 TTFB 和用户体验，特别是动态生成页面

---

### [代理专用 Postgres | 虎数据](https://www.tigerdata.com/blog/postgres-for-agents)

**原文标题**: [Postgres for Agents | Tiger Data](https://www.tigerdata.com/blog/postgres-for-agents)

Tiger Data 宣布推出专为 AI 代理设计的数据库 Agentic Postgres，旨在帮助开发者更高效地构建 AI 应用，将重复性工作交给代理处理，从而专注于更高层次的架构与创意。

- 🚀 **专为代理设计**：Agentic Postgres 是首个从零构建、专为 AI 代理优化的数据库，支持代理通过 MCP 服务器安全访问数据库，并内置高级工具用于模式设计、查询优化等。
- 🔍 **原生搜索与检索**：集成全文搜索（pg_textsearch）和语义搜索（pgvectorscale）扩展，支持混合搜索，让代理能直接在数据库中快速检索结构化和非结构化数据。
- ⚡ **快速零拷贝分支**：基于 Fluid Storage 存储层，支持秒级创建数据库分支，每个代理可拥有独立环境，无需复制数据或增加成本，适合实验、测试和并行任务。
- 🛠️ **新 CLI 与免费层**：提供全新命令行工具和免费服务层，开发者可通过简单命令快速安装和体验 Agentic Postgres，助力代理和开发者即时上手。
- 🌊 **弹性存储支持**：依托 Fluid Storage 分布式存储架构，实现即时快照、自动扩缩容和高性能 I/O，免费服务已全面采用此技术。
- 👥 **开发者与代理协同**：Agentic Postgres 旨在让开发者与 AI 代理协同工作，代理处理机械性任务，开发者聚焦于架构与创新，提升开发效率与应用质量。

---

### [React2Shell（CVE-2025-55182）](https://react2shell.com/)

**原文标题**: [React2Shell (CVE-2025-55182)](https://react2shell.com/)

React2Shell（CVE-2025-55182）是一个影响 React.js 服务器端使用的 10.0 级严重漏洞，Next.js 框架中对应编号为 CVE-2025-66478。该漏洞由安全研究员于 2025 年 11 月 29 日向 Meta 团队披露，官方于 12 月 3 日发布补丁。目前存在部分无效概念验证报告传播，建议用户及时参考官方公告确认影响并更新补丁。

- 🚨 **漏洞信息**：React.js 服务器端严重漏洞（CVE-2025-55182），Next.js 中编号为 CVE-2025-66478，危险等级 10.0
- 📅 **披露时间**：2025 年 11 月 29 日提交至 Meta，12 月 3 日由 React 和 Vercel 发布补丁
- ⚠️ **概念验证现状**：漏洞披露后出现大量无效 PoC 传播，真正有效的攻击代码尚未公开
- 🛡️ **防护说明**：部分安全供应商已部署运行时级防护，但建议所有用户及时更新补丁
- 🔍 **影响确认**：需参考 React 和 Next.js 官方公告，依赖扫描工具可能存在误报
- 📝 **技术说明**：Next.js 因采用代码打包方式，依赖工具可能无法自动识别漏洞
- 👥 **致谢名单**：感谢 Meta、Vercel 团队及安全研究员 Sylvie Mayer 在漏洞协调与防护中的贡献

---

### [React Server Components 中的关键安全漏洞 – React](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)

**原文标题**: [Critical Security Vulnerability in React Server Components – React](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)

React 团队披露了一个严重安全漏洞（CVE-2025-55182），影响 React Server Components 相关包，允许未经身份验证的远程代码执行，需立即升级修复版本。

- 🔓 **漏洞概述**：React Server Components 存在未授权远程代码执行漏洞，攻击者可通过恶意 HTTP 请求在服务器上执行代码
- ⚠️ **影响范围**：涉及 react-server-dom-webpack、react-server-dom-parcel、react-server-dom-turbopack 的 19.0.0 至 19.2.0 版本
- 🚨 **紧急措施**：必须立即升级至 19.0.1、19.1.2 或 19.2.1 修复版本
- 📦 **受影响框架**：Next.js、React Router、Waku、Parcel、Vite RSC 插件、Redwood SDK 等
- 🔧 **升级指南**：各框架提供具体升级命令，如 Next.js 需根据版本线安装对应补丁版本
- 🛡️ **临时缓解**：部分托管服务商已实施临时防护措施，但仍需尽快更新
- 📅 **时间线**：11 月 29 日报告→30 日确认→12 月 1 日开发修复→3 日公开发布补丁
- 👏 **致谢**：感谢 Lachlan Davidson 通过 Meta 漏洞赏金计划发现并报告此漏洞

---

### [React2Shell 安全公告 | Vercel 知识库](https://vercel.com/kb/bulletin/react2shell)

**原文标题**: [React2Shell Security Bulletin | Vercel Knowledge Base](https://vercel.com/kb/bulletin/react2shell)

React2Shell（CVE-2025-55182）是一个影响 React 19 及使用其服务器组件的框架（如 Next.js）的关键安全漏洞，可导致远程代码执行。公开漏洞利用已于 2025 年 12 月 4 日出现，需立即采取行动。

- 🚨 **影响范围**：Next.js 15.0.0 至 16.0.6 版本、Next.js 14 特定 Canary 版本及所有使用 React 服务器组件的框架均受影响。
- ⬆️ **立即升级**：强烈建议将 Next.js 升级至相应修补版本（如 15.3.6、16.0.7 等），这是唯一完整的修复方案。
- 🛡️ **额外防护**：Vercel WAF 已部署规则拦截已知攻击模式，但无法保证覆盖所有变种，建议同时为所有部署启用“标准保护”。
- 🔄 **环境变量轮换**：若应用在 12 月 4 日前在线且未打补丁，修补后应立即轮换所有应用密钥。
- 🤖 **自动升级**：可使用 Vercel Agent 自动检测漏洞项目并提交升级 PR，或通过`npx fix-react2shell-next`命令行工具快速更新。
- 📊 **检查漏洞**：通过 Vercel 控制台横幅提示或直接检查`next`、`react-server-dom-*`等包版本来确认是否受影响。
- ❓ **常见问题**：无法明确判断是否已被利用，建议审查日志；v0 应用需手动或等待自动更新修补；避免使用公开漏洞利用测试生产环境。

---

### [Cloudflare WAF 主动防护 React 漏洞](https://blog.cloudflare.com/waf-rules-react-vulnerability/)

**原文标题**: [Cloudflare WAF proactively protects against React vulnerability](https://blog.cloudflare.com/waf-rules-react-vulnerability/)

Cloudflare 已针对 React 服务器组件漏洞部署新防护，所有通过其 WAF 代理流量的客户均自动获得保护，同时强烈建议用户立即更新 React 至最新版本。

- 🛡️ Cloudflare WAF 已部署新规则，自动保护所有客户免受 React 漏洞攻击
- ⚠️ 漏洞影响 React 19.0-19.2 及 Next.js 15-16 版本，可导致远程代码执行
- 🔧 免费与付费规则集均包含防护规则，默认动作为拦截
- 📅 规则已于 2025 年 12 月 2 日部署，目前未监测到攻击尝试
- 🔄 Cloudflare 安全团队将持续监控攻击变体并更新防护措施
- ⬆️ 建议用户立即升级至 React 19.2.1 及 Next.js 最新安全版本

---

### [2025 年 12 月 5 日 Cloudflare 服务中断事件](https://blog.cloudflare.com/5-december-2025-outage/)

**原文标题**: [Cloudflare outage on December 5, 2025](https://blog.cloudflare.com/5-december-2025-outage/)

2025 年 12 月 5 日，Cloudflare 因内部配置变更触发代码缺陷，导致部分客户服务中断约 25 分钟，约 28% 的 HTTP 流量受影响。此次事件由修复 React 漏洞的缓冲区调整引发，非恶意攻击所致。

- 🚨 **事件概述**：2025 年 12 月 5 日 08:47 UTC，Cloudflare 网络部分故障，持续约 25 分钟，09:12 完全恢复，约 28% 的 HTTP 流量受影响。
- 🔧 **根本原因**：为应对 React 漏洞（CVE-2025-55182）调整 WAF 缓冲区至 1MB 时，关闭内部测试工具触发 FL1 代理代码缺陷，导致 HTTP 500 错误。
- 🐛 **技术细节**：规则集“执行”动作的禁用开关逻辑存在长期未发现的 Lua 代码错误，在跳过规则时引发空值索引异常。
- 🌍 **影响范围**：仅使用旧版 FL1 代理且部署 Cloudflare 托管规则集的客户受影响，中国网络流量未波及。
- ⏱️ **时间线**：08:47 配置变更发布，08:48 全面影响，09:11 变更回滚，09:12 服务恢复。
- 🛡️ **改进措施**：将加强配置部署的滚动更新与健康验证、优化故障应急能力，并实施“故障开放”错误处理逻辑。
- 📅 **后续计划**：下周公布详细韧性项目报告，目前冻结所有网络变更以确保系统稳定。

---

### [使用 Prisma 管理 Next.js Monorepo | AppSignal 博客](https://blog.appsignal.com/2025/11/26/manage-a-nextjs-monorepo-with-prisma.html)

**原文标题**: [Manage a Next.js Monorepo with Prisma | AppSignal Blog](https://blog.appsignal.com/2025/11/26/manage-a-nextjs-monorepo-with-prisma.html)

本文介绍了如何在 Next.js 单仓库（monorepo）中集成 Prisma 来构建一个披萨订购应用，涵盖项目初始化、Prisma 配置、数据库查询和订单管理的完整流程。

- 🚀 使用 Next.js 和 Prisma 在单仓库中构建全栈应用，实现前后端类型与逻辑共享
- 🛠️ 通过 Prisma 初始化数据库模型（用户、订单、订单项、披萨）并运行迁移
- 🌱 配置种子脚本预填充数据库数据，利用唯一约束避免重复条目
- 🔌 创建全局 Prisma 客户端实例，通过扩展优化性能并避免开发环境重复实例化
- 📊 在 Next.js 组件中直接查询数据库，展示用户和披萨列表，实现类型安全操作
- 📝 构建订单管理界面，支持查看订单详情、取消订单及创建新订单功能
- ⚡ 利用 Next.js 服务端操作处理表单提交，实现数据更新与页面重定向
- 🎯 单仓库架构减少后端分层，使用统一 TypeScript 栈提升开发效率与一致性

---

### [Next.js 图像优化 | DebugBear](https://www.debugbear.com/blog/nextjs-image-optimization)

**原文标题**: [Next.js Image Optimization | DebugBear](https://www.debugbear.com/blog/nextjs-image-optimization)

Next.js Image Optimization 是 Next.js 内置的强大功能，通过 `next/image` 组件自动优化图像，提升网页性能。它根据用户设备和浏览器动态调整图像格式、尺寸并压缩，支持懒加载、响应式布局和模糊占位符等特性，显著减少加载时间和带宽使用，改善用户体验和 SEO 评分。

- 🚀 **自动优化**：根据请求动态转换图像格式（如 WebP/AVIF）、调整尺寸并压缩，提升加载速度。
- 🖼️ **智能组件**：`next/image` 替代传统 `<img>` 标签，支持懒加载、响应式设计和模糊占位符，防止布局偏移。
- ⚡ **性能对比**：相比未优化图像，优化后图像大小减少约 70%，3G 网络下加载时间从 4–5 秒缩短至 1–2 秒。
- 📱 **响应式支持**：通过 `sizes` 属性适配不同视口，确保移动端仅加载所需尺寸，避免带宽浪费。
- 🔧 **高级配置**：可自定义图像加载器、允许外部域名，并利用 `loading="eager"` 和 `fetchPriority="high"` 优先加载关键图像。
- 🛠️ **替代方案**：Unpic 库提供统一 API 处理本地和 CDN 图像，简化配置并支持高级变换。
- 📊 **性能审计**：使用工具（如 DebugBear）监测 Core Web Vitals，优化 LCP 等指标，提升搜索引擎排名。
- ✅ **最佳实践**：始终定义宽高、为首屏图像设置 `priority`、配置 `sizes` 并允许外部域名，结合 CDN 进一步提升性能。

---

### [React 中 useEffectEvent 的注意事项](https://slicker.me/react/useEffectEvent.html)

**原文标题**: [Do's and Don'ts of useEffectEvent in React](https://slicker.me/react/useEffectEvent.html)

useEffectEvent 是一个实验性的 React Hook，用于从 Effect 中提取非响应式逻辑，允许在 Effect 内读取最新的 props 或 state 值，而不会因这些值的变化导致 Effect 重新执行。

- 🧩 **解决核心问题**：在 Effect 中读取最新值但避免不必要的重新运行，例如聊天室应用中记录房间切换时包含当前主题，而主题变化时不触发 Effect 重新执行。
- ✅ **正确用法**：在 Effect 内直接调用、用于读取最新 props/state 而不添加依赖、分离响应式与非响应式逻辑、同步调用。
- ❌ **错误用法**：在常规事件处理器或渲染中调用、作为 prop 传递、异步调用、替代正确的记忆化。
- 📊 **常见用例**：日志记录与数据分析、使用最新状态的回调、基于最新值的防抖处理。
- ⚠️ **注意事项**：仅用于真实需求，保持函数目的单一，等待稳定版再用于生产，优先考虑逻辑重构。

---

### [RGL 示例 00 - 展示](https://react-grid-layout.github.io/react-grid-layout/examples/00-showcase.html)

**原文标题**: [RGL Example 00 - Showcase](https://react-grid-layout.github.io/react-grid-layout/examples/00-showcase.html)

React-Grid-Layout 是一个用于 React 的网格布局系统，具备自动排列、可拖拽和调整大小的组件、静态组件、流体布局以及针对不同响应式断点的独立布局功能。

- 📦 自动排列组件，优化布局空间
- 🖱️ 支持拖拽和调整组件大小
- 📏 提供静态组件和流体布局选项
- 📱 针对不同响应式断点设置独立布局
- 🔧 可在展示中实时交互体验功能

---

### [GitHub - react-grid-layout/react-grid-layout: 一个适用于 React 的可拖拽、可调整大小且支持响应式断点的网格布局。](https://github.com/react-grid-layout/react-grid-layout)

**原文标题**: [GitHub - react-grid-layout/react-grid-layout: A draggable and resizable grid layout with responsive breakpoints, for React.](https://github.com/react-grid-layout/react-grid-layout)

React-Grid-Layout 是一个用于 React 的可拖拽、可调整大小且支持响应式断点的网格布局系统，完全基于 React 构建，无需 jQuery。

- 📦 **核心功能**：提供可拖拽、可调整大小的网格布局，支持响应式断点，布局可序列化与恢复。
- 🚀 **版本特性**：v2 版本为完整的 TypeScript 重写，提供 Hooks API、模块化架构和更小的打包体积。
- 🔄 **迁移支持**：提供 `legacy` 包装器以实现与 v1 的 100% API 兼容，同时鼓励新项目使用现代化的 v2 API。
- 🛠️ **配置灵活**：采用可组合的配置接口（如 `gridConfig`、`dragConfig`），并支持自定义压缩器与定位策略。
- 📏 **宽度管理**：推荐使用 `useContainerWidth` Hook 来获取容器宽度，也支持固定宽度或传统的 `WidthProvider` HOC。
- 🎛️ **Hooks API**：提供 `useContainerWidth`、`useGridLayout` 和 `useResponsiveLayout` 等 Hooks，用于不同场景的状态管理与控制。
- 📄 **丰富示例**：包含大量演示案例，如静态元素、动态增删、本地存储保存布局、边界限制等。
- 🌐 **实际应用**：被 BitMEX、Grafana、HubSpot 等多个知名项目用于构建仪表盘和界面。
- 📚 **安装与使用**：通过 npm 安装，需引入配套的 CSS 样式，并提供快速入门和响应式用法示例。
- ⚡ **性能优化**：建议对子组件进行记忆化，并避免在渲染中创建组件，以提升性能。
- 🔧 **扩展能力**：支持通过 `extras` 导入可选组件（如 `GridBackground`），并可从核心模块导入纯布局算法函数。

---

### [《命运》介绍 | 命运](https://fate.technology/posts/introducing-fate)

**原文标题**: [Introducing Fate | fate](https://fate.technology/posts/introducing-fate)

fate 是一个为 React 和 tRPC 设计的现代数据客户端，它结合了视图组合、规范化缓存、数据掩码、异步 React 特性以及 tRPC 的类型安全，旨在让 React 应用中的数据获取和状态管理更具可组合性、声明性和可预测性。

- 🚀 **发布公告**：fate 的初始 alpha 版本于 2025 年 12 月 9 日发布，由 Christoph Nakazawa 推出。
- 🔄 **设计理念**：借鉴 Relay 的核心思想（如片段组合、规范化缓存），但构建在 tRPC 之上，无需 GraphQL，提供类型安全和类似 GraphQL 的体验。
- 🛠️ **核心功能**：通过视图（View）声明数据需求，使用 `useRequest` 在根组件批量获取数据，并通过操作（Action）支持自动乐观更新和回滚。
- 📦 **技术栈**：基于 tRPC 后端，要求暴露 `byId` 和 `list` 查询，支持渐进式采用，无需重写现有架构。
- ⚡ **开发体验**：API 简洁（“只是 JavaScript”），减少样板代码，与异步 React、Suspense、React 编译器及热重载深度集成。
- 🧩 **代码示例**：组件通过视图选择字段，传递引用（ViewRef）解析数据，操作自动更新相关视图，无需手动缓存管理。
- 🚧 **当前状态**：仍处于早期阶段，缺少垃圾回收、静态编译等核心功能，但支持通过模板快速上手和贡献。
- 🤖 **开发背景**：80% 的代码由 OpenAI Codex 生成，20% 由人工编写，强调 AI 工具使用的透明度。
- 🌟 **未来愿景**：计划支持更多后端（如 Drizzle）、持久化存储、实时更新等，旨在提升数据处理的清晰度和可靠性。

---

### [元组·元组](https://tuple.app/l/pair-programming?utm_source=cooperpress&utm_medium=referral&utm_campaign=react_status_sponsored_20251210)

**原文标题**: [Tuple Â· Tuple](https://tuple.app/l/pair-programming?utm_source=cooperpress&utm_medium=referral&utm_campaign=react_status_sponsored_20251210)

Tuple 是一款专为远程结对编程设计的应用程序，提供高清屏幕共享、流畅音频和远程控制功能，旨在提升开发者的协作效率和体验。

- 🖥️ 专为开发者打造的远程结对编程工具，支持 macOS 和 Windows 系统
- 🎯 提供高达 5K 分辨率的超清晰屏幕共享，确保代码字体清晰可读
- 🔒 采用端到端加密技术，所有音频、视频和屏幕共享数据均不经过服务器
- 🔊 低延迟音频和流畅远程控制，营造身临其境的协作体验
- 🔄 一键切换屏幕共享者，方便双方轮流操作解决问题
- 🎨 内置屏幕标注工具、表情反应和动画效果，增强互动乐趣
- ⚡ 基于 C++ 开发，CPU 占用低，界面简洁无干扰
- 🆓 提供 14 天免费试用期，已被数千开发团队信任使用

---

### [TanStack AI](https://tanstack.com/ai/latest)

**原文标题**: [TanStack AI](https://tanstack.com/ai/latest)

TanStack AI 是一个开源的人工智能软件开发工具包（SDK），提供跨多个 AI 服务提供商的统一接口，旨在消除供应商锁定，让开发者能够自由选择并切换不同的 AI 服务，同时享受完整的类型安全和丰富的开发工具支持。

- 🛠️ **多提供商支持**：兼容 OpenAI、Anthropic、Ollama 和 Google Gemini 等主流 AI 服务，支持运行时切换，无需修改代码。
- 🔌 **统一 API 设计**：为所有提供商提供一致的接口，包含自动类型推断的独立函数，适用于任何 JavaScript 环境。
- 🧰 **工具/函数调用**：提供自动执行循环，无需手动管理工具，支持类型安全的工具定义与结构化输出及流式传输。
- 🌐 **完整的开源生态系统**：TanStack AI 是纯粹的开源库和标准集合，而非服务平台，直接连接用户选择的 AI 提供商，无中间商或服务费用。
- 🖥️ **服务器无关性**：支持任何后端服务器，提供 TypeScript、PHP、Python 等多种语言的协议库。
- 📱 **客户端无关性**：提供原生客户端库（@tanstack/ai-client）以及 React、Solid 等框架集成。
- 🔧 **全面工具支持**：完整支持客户端和服务器工具，包括工具审批和执行控制。
- 🧠 **思维与推理能力**：完全支持思维和推理模型，相关令牌可实时流式传输至客户端。
- 🎯 **端到端类型安全**：跨提供商、模型及模型选项实现完整的类型安全。
- 🔍 **新一代开发者工具**：提供实时显示 AI 连接状态的强大开发工具。
- 💚 **纯粹开源**：无隐藏服务、无费用、无追加销售，由社区支持，直接连接用户选择的提供商。

---

### [快速入门 | TanStack AI 文档](https://tanstack.com/ai/latest/docs/getting-started/quick-start)

**原文标题**: [Quick Start | TanStack AI Docs](https://tanstack.com/ai/latest/docs/getting-started/quick-start)

TanStack AI 是一个用于构建 AI 应用的 JavaScript 库，提供工具、适配器和 React 集成，支持快速创建具备流式响应和工具调用功能的聊天应用。

- 🚀 **快速开始**：通过安装核心包和适配器，结合 React 集成，可在几分钟内搭建一个简单的聊天应用。
- 🔌 **多模型适配**：提供 OpenAI、Anthropic、Google Gemini 和 Ollama 等主流 AI 服务的适配器，便于切换和集成。
- 🛠️ **工具调用支持**：框架支持定义和使用服务器端与客户端工具，实现函数调用和复杂交互逻辑。
- 🌊 **流式响应处理**：内置流式响应处理能力，支持实时显示 AI 的“思考过程”和回复内容。
- ⚛️ **框架无关与 React 集成**：核心库与框架无关，同时提供专门的 React 钩子（如 `useChat`）简化前端状态管理和交互。
- 🔧 **类型安全与可观察性**：强调类型安全，并提供开发工具和可观察性功能，便于调试和监控 AI 交互流程。

---

### [开源 Remix 商店 | Remix](https://remix.run/blog/oss-remix-store)

**原文标题**: [Open Sourcing the Remix Store | Remix](https://remix.run/blog/oss-remix-store)

Remix 团队开源了其官方商店的源代码，旨在为 React Router 和 Shopify 开发者提供学习资源，并展示如何构建一个基于 Hydrogen 和 Remix 的定制化电商平台。

- 🎉 Remix 团队宣布开源官方商店代码，供 React Router 和 Shopify 开发者学习与参考
- 🛍️ 商店基于 Hydrogen 和 Remix 构建，已运营半年并处理超过 200 笔订单，兼具宣传与实用功能
- 👥 目标用户包括 Remix 爱好者、Hydrogen 学习者及 Shopify 内部团队，用于教育、测试与品牌推广
- 🛠️ 开发历程涉及黑客马拉松、设计迭代、内部审批及多次产品改进，最终于 2025 年 5 月正式上线
- ✨ 商店包含多项特色功能：滚动同步的 3D 连帽衫展示、集合页面标题视差效果、图片模糊加载优化及乐观购物车更新
- 🐞 错误页面采用数字矩阵故障艺术效果，增强视觉体验
- 📅 未来计划包括推出新产品、优化国际运费、升级至 Remix 3，并鼓励社区通过 GitHub 参与贡献

---

### [首页 | 混音商店](https://shop.remix.run/)

**原文标题**: [Home | The Remix Store](https://shop.remix.run/)

Remix 品牌提供一系列面向工程师和网站开发者的服饰及周边产品，涵盖不同款式和价格。

- 👕 连帽衫和卫衣价格在 $48 至 $62 之间，如 Remix Engineering Hoodie 和 Run Club Hoodie
- 👚 长袖和短袖 T 恤价格约为 $29 至 $31，例如 Run Club L/S Shirt 和 Remix Engineering T-shirt
- 🧢 配件包括帽子、贴纸包和笔记本，价格从 $6 到 $29 不等
- 🏷️ 所有产品旨在满足工程师日常穿着和品牌支持需求，设计简洁实用

---

### [混音 - 打造更优网站](https://remix.run/)

**原文标题**: [Remix - Build Better Websites](https://remix.run/)

Remix 是一个全栈 Web 框架，专注于通过 Web 标准和现代用户体验来构建更好的网站。它利用分布式系统和原生浏览器功能，提供快速的页面加载和即时过渡，支持在多种环境中运行，并强调通过嵌套路由、并行数据加载和内置错误处理等功能，实现卓越的用户体验和开发效率。

- 🌐 **基于 Web 标准**：Remix 专注于 Web 标准和现代 Web 应用用户体验，旨在帮助开发者构建更出色的网站。
- 🚀 **全栈框架**：作为一个全栈 Web 框架，Remix 让开发者专注于用户界面，并通过 Web 标准提供快速、流畅且弹性的用户体验。
- 🔄 **嵌套路由**：通过嵌套路由，Remix 可以消除几乎所有的加载状态，实现并行数据加载，提升页面速度和用户体验。
- ⚡ **预取功能**：Remix 支持在用户点击链接前预取所有资源（包括数据、模块和 CSS），实现零加载状态和即时体验。
- 📝 **内置数据更新**：Remix 内置了弹性的、渐进增强的数据更新功能，简化表单处理和状态管理，支持乐观 UI 和过渡钩子。
- 🛡️ **错误处理**：Remix 内置了错误处理机制，包括路由错误边界，可以优雅地处理服务器端和客户端错误，避免页面刷新。
- 🌍 **多环境运行**：基于 Web Fetch API，Remix 可以在任何地方运行，包括 Cloudflare Workers、无服务器环境和传统 Node.js 环境。
- 💬 **开发者好评**：许多开发者赞扬 Remix 的直观性、生产力和对渐进增强的支持，认为它是游戏规则改变者，尤其适合企业团队。

---

### [Hydrogen：Shopify 的无头商务框架](https://hydrogen.shopify.dev/)

**原文标题**: [Hydrogen: Shopifyâs headless commerce framework](https://hydrogen.shopify.dev/)

Shopify Hydrogen 是一个无头电商解决方案，旨在提升开发效率和性能，通过快速搭建、优化的 UI 组件和内置的 Shopify 功能（如购物车、多市场支持和 Shop Pay）加速开发，并利用基于 Remix 的服务器端渲染实现即时反馈、流畅过渡和稳定体验，同时提供全球托管服务 Oxygen，支持即时部署和性能优化。

- 🚀 **快速启动**：通过命令行工具快速创建 Hydrogen 应用，几分钟内从零搭建到运行
- 🛒 **电商优化组件**：提供灵活的 UI 组件，专为电商场景设计，如产品展示、购物车和结账流程
- ⚡ **高性能体验**：基于 Remix 框架，支持服务器端渲染和嵌套路由，实现快速页面加载和流畅导航
- 🌍 **多市场支持**：轻松扩展国际市场，支持子文件夹、子域名或独立域名配置，无需修改代码
- 🔧 **内置 Shopify 功能**：集成购物车、分析、Shop Pay、客户账户等关键功能，提升转化率
- 🧩 **可组合设计**：兼容任何具有 API 的应用，支持灵活扩展和集成第三方工具
- ☁️ **全球托管服务**：通过 Oxygen 提供免费全球托管，300 多个节点确保低延迟访问
- 📚 **开源与学习资源**：Hydrogen 完全开源，提供详细文档、教程和社区支持，助力开发者快速上手

---

### [HackerOne 打造的 React 日期选择器](https://reactdatepicker.com/)

**原文标题**: [React Datepicker crafted by HackerOne](https://reactdatepicker.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发过程，大幅缩短化合物筛选与临床试验周期
- 📊 基于患者数据的个性化治疗方案正成为慢性病管理的新趋势
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任界定等伦理监管问题

---

### [发布 🎄 React Datepicker v9.0.0 - 节日版 🎁 · Hacker0x01/react-datepicker · GitHub](https://github.com/Hacker0x01/react-datepicker/releases/tag/v9.0.0)

**原文标题**: [Release 🎄 React Datepicker v9.0.0 - Holiday Release 🎁 · Hacker0x01/react-datepicker · GitHub](https://github.com/Hacker0x01/react-datepicker/releases/tag/v9.0.0)

React Datepicker v9.0.0 版本作为节日发布，引入了时区支持、时间选择与日期范围的兼容性、多项新属性、错误修复和性能改进，同时更新了依赖并提升了测试覆盖率。

- 🌍 新增时区支持，可通过 `timeZone` 属性处理任意时区的日期显示
- ⏰ 时间选择功能现在与 `selectsRange` 兼容，可独立设置开始和结束时间
- 🎁 添加多个新属性，如自定义弹出层定位、月份标题位置控制和日期格式化选项
- 🔧 修复了日历视图更新、时间选择器高度无限增长及月份跳转等问题
- 🛠️ 升级至 Node 24.x LTS，更新依赖并显著提升测试覆盖率
- 📚 新增时区相关文档，优化了源代码映射和 TypeScript 类型推断

---

### [又一个 React 灯箱 - 适用于 React 的现代灯箱组件](https://yet-another-react-lightbox.com/)

**原文标题**: [Yet Another React Lightbox - Modern lightbox component for React](https://yet-another-react-lightbox.com/)

Yet Another React Lightbox 是一个现代、高性能且易于定制的 React 灯箱组件，支持插件扩展和响应式图像。

- 🚀 **专为 React 构建**：兼容 React 19、18、17 及 16.8.0+ 版本
- 🖱️ **多设备导航**：支持键盘、鼠标、触摸板和触屏操作
- ⚡ **高性能预加载**：避免显示部分下载的图像，且预加载数量有限以平衡性能与体验
- 📱 **响应式支持**：开箱即用支持自动分辨率切换的响应式图像
- 🎬 **视频与缩放插件**：通过可选插件支持视频幻灯片和图像缩放功能
- 🎨 **高度可定制**：可自定义任何 UI 元素或添加自定义幻灯片
- 📦 **模块化设计**：核心功能轻量，通过插件按需添加额外特性
- 🔧 **TypeScript 友好**：内置类型定义，支持 RTL 布局
- 📚 **丰富资源**：提供详细文档、示例和更新日志，安装简便

---

### [发布 6.1.0 版本 · ant-design/ant-design · GitHub](https://github.com/ant-design/ant-design/releases/tag/6.1.0)

**原文标题**: [Release 6.1.0 · ant-design/ant-design · GitHub](https://github.com/ant-design/ant-design/releases/tag/6.1.0)

Ant Design 发布了 6.1.0 版本，包含多项新功能、问题修复和优化，涉及 ConfigProvider、Alert、Drawer、Select、Table、Button、Menu 等组件，并进行了依赖库迁移和 TypeScript 类型更新。

- 🆕 ConfigProvider 新增支持配置 Tooltip、Popover 和 Popconfirm 的 trigger 属性。
- 🆕 Alert 和 Drawer 新增语义化关闭按钮元素，Drawer 还支持 resizable 的布尔类型设置。
- 🆕 Select 新增 optionFilterProp 多字段搜索功能。
- 🐞 修复了 Select 在非搜索状态下显示输入光标、选项未打开等问题。
- 🐞 修复了 Table 的 cellFontSizeSM 和 cellFontSizeLG token 不生效的问题。
- 🐞 修复了 Button 部分 Token 在特定变体下不生效的问题。
- 💄 修复了 Menu 组件 item 中定义的 style 不生效的错误。
- 🛠 更新了 @ant-design/react-slick 版本以删除 classnames，并迁移了 rc-overflow 和 rc-virtual-list 以删除 rc-util。
- 🤖 TypeScript 方面，Alert 新增导出 ErrorBoundaryProps 类型，ConfigProvider 支持 Table rowKey 传入函数，Notification 的 title 属性改为可选。

---

### [GitHub - terrestris/react-geo：一套结合React、Ant Design 与 OpenLayers 使用的地理相关模块。](https://github.com/terrestris/react-geo)

**原文标题**: [GitHub - terrestris/react-geo: A set of geo related modules to use in combination with React, Ant Design and OpenLayers.](https://github.com/terrestris/react-geo)

react-geo 是一个基于 React、Ant Design 和 OpenLayers 的 JavaScript 库，提供丰富的组件用于构建现代地图应用。它支持动态主题配置，包含 TypeScript 声明，并提供了入门教程和快速启动工具。

- 🌍 结合 React、Ant Design 和 OpenLayers 的地理模块库
- 📦 通过 npm 安装，包含 TypeScript 类型声明
- 🎨 支持通过 Ant Design 的 ConfigProvider 进行动态主题配置
- 📚 提供详细教程和快速启动应用工具（create-react-geo-app）
- 🤝 鼓励贡献，遵循 BSD 2-Clause 开源协议
- ⭐ 项目拥有 403 个星标和 57 个分支，社区活跃

---

### [发布 v2.16.0 · pmndrs/jotai · GitHub](https://github.com/pmndrs/jotai/releases/tag/v2.16.0)

**原文标题**: [Release v2.16.0 · pmndrs/jotai · GitHub](https://github.com/pmndrs/jotai/releases/tag/v2.16.0)

该页面显示 Jotai 库的 GitHub 仓库界面，其中包含一个版本发布（v2.16.0）的详细信息，同时页面存在部分加载错误提示。

- 🚨 页面多次出现加载错误提示，需重新加载页面
- 🏷️ 最新版本 v2.16.0 于 2023 年 12 月 9 日发布
- ⚠️ 此版本弃用了`jotai/utils`中的`atomFamily`，建议迁移至`jotai-family`
- 🔧 包含内部存储机制调整和初始化函数重命名等多项修复
- 👥 由 dai-shi 和 dmaskasky 两位贡献者共同完成
- 📊 项目获得 20.8k 星标、700 个分支和 6 个拉取请求

---

### [npm 经典令牌已撤销，现提供基于会话的身份验证和 CLI 令牌管理 - GitHub 更新日志](https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available/)

**原文标题**: [npm classic tokens revoked, session-based auth and CLI token management now available - GitHub Changelog](https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available/)

npm 已完成经典令牌的全面淘汰，转向更安全的会话式认证与 CLI 令牌管理工具，同时默认启用新包的 2FA 保护。

- 🔐 所有 npm 经典令牌已永久撤销，无法再用于认证或恢复
- ⏳ 新登录将获得两小时会话令牌，到期需重新认证，且会话期间发布操作强制 2FA 验证
- 🛠️ 新增 CLI 令牌管理工具，支持在终端直接创建、查看和撤销精细权限令牌
- 🚀 新创建的包将默认启用双重认证（2FA），无需手动配置
- 🔄 临时恢复遗留 API 端点支持，但将在未来几个月内移除，建议尽快迁移至现代认证方式
- 🔧 本地开发需定期运行`npm login`重新认证；CI/CD 流程应使用 CLI 创建精细令牌或采用 OIDC 可信发布

---

### [2025 年回顾：网页性能有哪些新进展？ | DebugBear](https://www.debugbear.com/blog/2025-in-web-performance)

**原文标题**: [2025 In Review: Whatâs New In Web Performance? | DebugBear](https://www.debugbear.com/blog/2025-in-web-performance)

2025 年网页性能领域的关键进展包括跨浏览器对核心网页指标的逐步支持、性能工具的功能增强、新 API 的推广、图像格式的演进以及性能监控的持续改进，整体呈现稳步优化趋势。

- 🌐 核心网页指标（LCP、INP、CLS）开始获得 Firefox 和 Safari 的跨浏览器支持，打破 Chrome 独占局面
- 🔧 Lighthouse 与 Chrome DevTools 整合性能洞察审计，提供统一优化建议
- ⚙️ Firefox 新增支持 Scheduler API，帮助开发者优化任务调度以提升交互响应
- 🛠️ 新增免费性能测试工具（如全局 TTFB 测试、HTML 大小分析器），增强诊断能力
- 🤖 Chrome DevTools 集成 AI 功能与 MCP 协议，支持智能性能分析与代码优化
- 📊 Chrome 用户体验报告新增 LCP 子部分数据，帮助定位具体性能瓶颈
- 🛒 真实场景性能研究（如自助结账延迟分析）揭示实际用户体验差异
- 🖼️ JPEG XL 图像格式获 Apple 支持，Google 态度转向开放，未来可能普及
- 🌐 推测规则（Speculation Rules）被 Shopify 和 WordPress 等平台采用，预加载提升导航速度
- 📈 核心网页指标达标率逐年缓慢提升，桌面端达 57.1%，移动端 49.7%
- ⏱️ TTFB、LCP、INP 等指标测量方式调整，更准确反映真实性能
- 🔄 软导航性能测量启动新的源试验，填补单页应用性能监控盲区
- 📦 基线 API 持续扩展，容器查询、压缩流等新功能广泛可用
- 🔮 2026 年展望：软导航测量落地、AI 工具深化、节流模拟改进、浏览器支持持续推进

---

### [调度器 - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Scheduler)

**原文标题**: [Scheduler - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Scheduler)

Scheduler 接口是优先任务调度 API 的一部分，允许开发者安排具有优先级的任务，可通过全局对象或 Worker 环境访问，但浏览器兼容性有限。

- 🚧 **有限兼容性**：该功能并非基线功能，在某些广泛使用的浏览器中不可用。
- 🌐 **全局访问**：在主线程可通过`Window.scheduler`访问，在 Worker 中可通过`WorkerGlobalScope.scheduler`访问。
- ⚙️ **核心方法**：提供`postTask()`方法用于添加带优先级、延迟或中止信号的任务，以及`yield()`方法用于让出主线程控制权。
- 📝 **示例用法**：通过`scheduler.postTask()`执行任务，并使用 Promise 处理结果或错误，例如记录任务执行文本。
- 🔍 **规范与文档**：功能定义遵循优先任务调度规范，MDN 文档提供了详细说明和示例代码链接。

---

### [我想读的一些博客文章 – Frontend Masters 博客](https://frontendmasters.com/blog/some-blog-posts-id-like-to-read/)

**原文标题**: [Some Blog Posts I’d Like to Read – Frontend Masters Blog](https://frontendmasters.com/blog/some-blog-posts-id-like-to-read/)

本文介绍了作者希望阅读的一系列前端开发相关博客文章主题，并阐述了写作对巩固知识和提升职业信誉的价值，同时推广了 Frontend Masters 的学习资源。

- 📝 列举了多个具有吸引力的前端技术博客主题，涵盖框架选择、效果实现、工具使用等
- ✍️ 强调写作能帮助巩固所学知识并建立行业信誉
- 🎓 推广 Frontend Masters 平台，提供前端技术课程和 7 天免费试用
- 💬 包含读者对文章主题的积极反馈和评论互动界面

---

### [客座写作 – 前端大师博客](https://frontendmasters.com/blog/guest-writing/)

**原文标题**: [Guest Writing – Frontend Masters Blog](https://frontendmasters.com/blog/guest-writing/)

Frontend Masters 博客诚邀技术作者投稿，提供稿酬，旨在为读者、作者及网站创造三赢局面。投稿需原创、技术性强、以开发者视角分享实践经验，强调清晰易懂与实用，鼓励读者掌握核心原理而非依赖第三方工具。

- 📝 投稿带来三赢：读者获益于作者经验，作者获得稿酬与曝光，网站内容因优质贡献而增值。
- 🔍 内容需实用：撰写自己搜索时希望找到的文章，确保对开发者有实际帮助，避免空洞。
- 🛠️ 强调原创与深度：禁止使用 AI 生成，要求基于深厚知识，分享真正热衷的技术主题。
- 🎯 聚焦前端技术：内容需围绕 HTML、CSS、JavaScript 及相关工具，以教程类为主，避免评论性文章。
- 👥 面向广泛受众：针对不同经验的前端开发者，注重清晰表达，假定基础技术知识。
- ✍️ 风格与格式：要求全面、技术准确、实用、友好而正式，建议 600 词左右，配图及代码示例。
- 📬 提交完整草稿：需先提供完整文章以评估，可先发简短提案咨询意向，但最终决定基于完整稿件。

---

### [欢迎收听 VS Code 内幕播客](https://code.visualstudio.com/blogs/2025/12/03/introducing-vs-code-insiders-podcast)

**原文标题**: [Introducing the VS Code Insiders Podcast](https://code.visualstudio.com/blogs/2025/12/03/introducing-vs-code-insiders-podcast)

VS Code 团队推出官方播客“VS Code Insiders Podcast”，通过开发者访谈揭秘编辑器幕后开发故事、新功能设计与 AI 编程未来趋势，并提供最新内测版体验指引。

- 🎙️ 官方播客深入探讨 VS Code 功能设计、AI 集成及社区建设，邀请核心开发者分享幕后洞察
- ♿ 近期专题涵盖无障碍设计、AI 智能体规划、开源社区运营及 GitHub Universe 技术解读
- 📥 听众可通过播客主页订阅节目，同步获取内测版安装通道与实时更新日志
- 🔮 节目面向各类开发者群体，呈现代码编辑器演进趋势与现代化工作流实践

---

### [Cypress 测试技巧与窍门 | Gleb Bahmutov | Substack](https://cypresstips.substack.com/)

**原文标题**: [Cypress Testing Tips & Tricks | Gleb Bahmutov | Substack](https://cypresstips.substack.com/)

本文介绍了使用 Cypress 进行网页测试的实用技巧与策略，旨在帮助开发者提升测试效率与覆盖范围。

- 🧪 掌握 Cypress 的核心功能与高级测试方法
- 🚀 学习提升测试执行速度与可靠性的技巧
- 📚 了解如何构建可维护且全面的测试套件
- 🔧 探索调试测试问题与优化配置的实用工具
- 💡 获取来自超过 2000 名订阅者验证的实战经验

---

### [类型感知 Linting Alpha | JavaScript 氧化编译器](https://oxc.rs/blog/2025-12-08-type-aware-alpha)

**原文标题**: [Type-Aware Linting Alpha | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2025-12-08-type-aware-alpha)

Oxlint 宣布类型感知 linting 功能进入 alpha 阶段，该功能利用 TypeScript 类型系统实现强大的代码检查规则，现已支持 43 条规则，性能相比 ESLint 提升约 10 倍，并引入了类型检查、规则配置、内联禁用注释等新特性。

- 🚀 **快速开始**：通过安装 `oxlint` 和 `oxlint-tsgolint` 并使用 `--type-aware` 标志即可启用类型感知 linting。
- ⚡ **性能优势**：在基准测试中，Oxlint 的类型感知 linting 比 ESLint 快约 10 倍，并能同时进行类型检查。
- 🆕 **新增功能**：支持在 linting 过程中进行类型检查、规则配置、内联禁用注释，并新增了多条规则。
- 🛠️ **技术架构**：采用 Rust（oxlint CLI）和 Go（tsgolint）的双二进制架构，高效分离前端体验与后端类型分析。
- 📝 **兼容性说明**：基于 TypeScript 7.0+，不支持旧版语法和已弃用的 `tsconfig.json` 选项（如 `baseUrl`）。
- 🔧 **自动修复**：类型感知规则现支持通过 `--fix` 标志自动修复问题。
- 🚧 **已知问题**：在处理大型代码库时可能遇到内存不足的问题，团队正在优化中。
- 🎯 **未来计划**：继续扩展规则覆盖范围，优化性能与内存使用，为 beta 版本做准备。

---

