### [为 unstable_instant 添加 eval 和文档 by gaojude · Pull Request #91334 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/91334/files#diff-e7a7ed97e16a9c22e3db281bb932db53aebce3c142753b38ef5231ded846acfa)

**原文标题**: [Add eval and docs for unstable_instant by gaojude · Pull Request #91334 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/91334/files#diff-e7a7ed97e16a9c22e3db281bb932db53aebce3c142753b38ef5231ded846acfa)

该内容是关于 Next.js 框架中新增的 `unstable_instant` 功能的文档和代码更新，旨在通过验证缓存结构和优化 Suspense 边界，确保客户端导航的即时性。

- 📄 **新增了关于即时导航的详细指南**，解释了如何通过导出 `unstable_instant` 来验证和优化页面结构，以实现即时客户端导航。
- 🔧 **在多个现有文档中添加了提示**，提醒开发者在遇到客户端导航缓慢时，除了使用 Suspense 和流式传输外，还应导出 `unstable_instant`。
- 🛠️ **引入了开发工具开关**，允许在 Next.js 配置中启用即时导航开发工具，用于调试和验证即时导航效果。
- 🧪 **提供了端到端测试工具**，通过 `@next/playwright` 包中的 `instant()` 辅助函数，可以编写测试来断言即时静态外壳的内容。
- 🚫 **支持选择性退出验证**，对于无法实现即时导航的布局（如需要读取用户特定数据的仪表板），可以通过设置 `instant = false` 来免除验证。
- 🔍 **验证覆盖所有可能的入口点**，不仅检查初始页面加载，还模拟路由层次结构中每个共享布局边界的导航，确保结构正确。
- 📝 **更新了配置文件示例**，展示了如何在 `next.config.ts` 中启用即时导航开发工具开关。
- 🐛 **修复了可能导致导航阻塞的页面结构问题**，通过将数据获取包裹在适当的 Suspense 边界中并使用 `use cache` 进行缓存，确保即时导航的可行性。

---

### [你可以直接部署智能体：为智能体时代构建架构 | Dom Sipowicz, Vercel - YouTube](https://www.youtube.com/watch?v=_TRV6fPUMJw&feature=youtu.be)

**原文标题**: [You Can Just Ship Agents: Architecting for the Agentic Era | Dom Sipowicz, Vercel - YouTube](https://www.youtube.com/watch?v=_TRV6fPUMJw&feature=youtu.be)

YouTube 平台的功能与服务概览  
- 📜 平台简介与基本条款  
- 📰 新闻中心与最新动态  
- ©️ 版权保护与内容政策  
- 📞 用户联系与客服渠道  
- 🎨 创作者支持与资源  
- 📢 广告合作与投放服务  
- 💻 开发者工具与 API 接口  
- ⚖️ 使用条款与法律规范  
- 🔒 隐私保护与数据安全  
- ⚙️ 平台运作机制说明  
- 🧪 新功能测试与更新  
- 🏢 谷歌公司所有权声明（截至 2026 年）

---

### [Next.js 供应商锁定不再 - YouTube](https://www.youtube.com/watch?v=UCveltYOQIs)

**原文标题**: [Next.js Vendor Lock-in No More - YouTube](https://www.youtube.com/watch?v=UCveltYOQIs)

YouTube 平台的功能与服务概览  
- 🏠 簡介與聯絡資訊  
- 📰 新聞中心與版權說明  
- 👥 創作者與廣告合作  
- 🔧 開發者工具與平台運作  
- ⚖️ 條款、私隱與安全政策  
- 🧪 新功能測試與版本標註

---

### [未找到标题](https://x.com/ZaynHao/status/2042187522416242985)

**原文标题**: [No title found](https://x.com/ZaynHao/status/2042187522416242985)

该页面提示 JavaScript 被禁用或浏览器不受支持，导致无法正常使用 X 平台的功能，并提供了相应的解决建议。

- 🔧 检测到浏览器中 JavaScript 被禁用，需启用或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致问题，建议暂时禁用后重试
- 📄 页面底部包含服务条款、隐私政策等法律文件链接
- 🔄 提供“再试一次”功能供用户重新加载页面

---

### [Next.js 使用缓存：远程：一行代码实现分布式缓存](https://tigerabrodi.blog/next-js-use-cache-remote-a-distributed-cache-in-one-line)

**原文标题**: [Next.js use cache: remote: A Distributed Cache in One Line](https://tigerabrodi.blog/next-js-use-cache-remote-a-distributed-cache-in-one-line)

Next.js 16 的 `use cache: remote` 指令允许开发者在异步函数中轻松实现分布式缓存，无需额外配置或基础设施，特别适用于 Vercel 部署环境。它通过共享的远程键值存储，使所有服务器实例都能访问同一缓存，从而显著减少数据库负载和延迟。

- 🚀 **一键启用分布式缓存**：在异步函数中添加 `'use cache: remote'` 即可实现跨实例的共享缓存，无需 Redis 等额外配置。
- 🔄 **智能缓存失效机制**：通过 `cacheTag()` 标记缓存，使用 `revalidateTag()` 或 `updateTag()` 按需或立即失效缓存，支持精细控制。
- ⏱️ **灵活的时间过期设置**：内置 `minutes`、`hours`、`max` 等时间预设，或自定义 `stale`、`revalidate`、`expire` 参数管理缓存生命周期。
- 🌍 **区域化缓存存储**：在 Vercel 上，缓存按区域隔离，确保同一区域内的所有用户和实例共享缓存，提升性能。
- 🚫 **避免运行时 API 调用**：不能在缓存函数中使用 `cookies()` 或 `headers()`，需将动态值作为参数传递以生成缓存键。
- 🧠 **优化缓存键设计**：建议按维度（如类别、语言）而非细粒度值（如用户 ID）缓存，减少条目数量并提高命中率。
- 💡 **三大指令对比**：`use cache` 用于内存缓存，`use cache: remote` 用于远程共享缓存，`use cache: private` 用于浏览器端私有缓存，各有适用场景。
- 📉 **大幅降低数据库压力**：缓存后，数据库仅需在缓存失效时处理请求，有效减少负载、成本和延迟，提升应用性能。

---

### [docs: 由 aurorascharff 添加构建指南 · 拉取请求 #92507 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/92507)

**原文标题**: [docs: add Building guide by aurorascharff · Pull Request #92507 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/92507)

该拉取请求为 Next.js 文档新增了一个“构建指南”，详细解释了 `next build` 命令的执行过程、构建输出解读、动态路由预渲染以及常见错误的调试方法。

- 🏗️ **新增构建指南**：创建了新的文档页面（`building.mdx`），系统性地介绍了应用构建的各个阶段、输出符号含义以及调试技巧。
- 📖 **内容整合与澄清**：将原本分散在 API 参考和错误页面中的构建相关内容整合到本指南中，并对 `generateStaticParams`、PPR 符号等概念进行了更清晰的说明。
- 🔧 **涵盖调试工具**：指南中详细说明了如何使用 `--debug-prerender` 和 `--debug-build-paths` 等标志来诊断和修复构建时的预渲染错误。
- 🔗 **完善文档链接**：在现有的 CLI 参考、安装和部署指南中添加了指向此新构建指南的链接，以形成更好的文档网络。
- 🐛 **修复与迭代**：在 PR 过程中修复了错误的文档链接、更新了构建输出符号的说明，并根据代码审查反馈对内容进行了多轮优化和调整。

---

### [2026 年 3 月回顾 | varlock](https://varlock.dev/blog/march-2026-recap/)

**原文标题**: [March 2026 Recap | varlock](https://varlock.dev/blog/march-2026-recap/)

2026 年 3 月，Varlock 在核心功能、集成生态和社区互动方面取得显著进展，获得了广泛关注和积极反馈。

- 🚀 **核心功能增强**：发布了 varlock@0.7.0，支持单文件 ESM/TypeScript 插件、新增`ifs()`和`remap()`函数、改进类型生成命令，并提升了插件加载稳定性和容器兼容性。
- 🔧 **开发者体验优化**：强化了 Bun 运行时检查、改进了文档和帮助信息质量，并增加了对`XDG_CONFIG_HOME`的支持，提升了开发便利性。
- 🔌 **集成与插件扩展**：新增了 Cloudflare Workers、Expo、Dashlane、KeePass 等多款集成与插件，并对 Next.js 集成进行了重大更新以支持 Turbopack。
- 📢 **社区内容亮点**：在 Syntax 播客和 Better Stack 视频中被推荐，相关教程文章介绍了如何用 Varlock 替代传统`.env`文件管理密钥，社区参与度显著提升。
- 💬 **社区互动渠道**：通过 Discord、GitHub Discussions、X 和 Bluesky 等平台积极与用户交流，收集反馈并分享更新。

---

### [更好的认证 1.6](https://better-auth.com/blog/1-6)

**原文标题**: [Better Auth 1.6](https://better-auth.com/blog/1-6)

Better Auth 1.6 版本作为过渡版本发布，重点在于为项目奠定更坚实的基础，同时引入了新功能、性能改进和多项重要修复，并启用了新的双轨发布工作流程。

- 🎯 **OpenTelemetry 集成**：现在支持分布式追踪，自动为认证 API 调用、数据库操作和钩子生命周期生成追踪信息。
- 🔑 **Passkey 预认证注册**：Passkey 插件支持用户在无会话状态下注册，实现了以 Passkey 为先的登录流程。
- 🔍 **不区分大小写的查询**：所有数据库适配器现在都支持对字符串查询进行不区分大小写的比较。
- ⚠️ **会话新鲜度计算方式变更**：`freshAge` 现在基于会话的创建时间而非更新时间，敏感操作可能需要更近期的登录。
- 🛡️ **SAML 安全增强**：默认启用 `InResponseTo` 验证以防止重放攻击。
- ⚡ **性能优化**：密码哈希改用非阻塞的 `node:crypto` scrypt 实现，并大幅减少了发布包的体积。
- 🚀 **新的双轨发布流程**：引入 `main`（稳定版）和 `next`（测试版）两条发布轨道，以加速重要修复并安全地管理破坏性变更。
- 📋 **功能请求流程变更**：新功能请求需先在 GitHub 提交议题讨论，再进行代码开发。
- 📦 **可信发布**：所有包均通过 GitHub Actions 的 OIDC 可信发布流程发布，增强了供应链安全。

---

### [零配置代码检查：Biome、ESLint 与 Oxlint | Ultracite](https://www.ultracite.ai/)

**原文标题**: [Zero-Config Linting for Biome, ESLint, and Oxlint | Ultracite](https://www.ultracite.ai/)

Ultracite 是一个零配置预设工具，用于 ESLint、Biome 和 Oxlint，帮助团队和 AI 编写一致且类型安全的代码，支持多种编辑器、代理和框架集成，旨在提升代码质量和开发效率。

- 🚀 **零配置设计**：提供开箱即用的代码检查和格式化规则，支持自定义配置
- 🔧 **多工具集成**：兼容 ESLint、Biome、Oxlint 等主流代码检查工具
- 🤖 **AI 与代理支持**：为 40 多种 AI 代理提供规则和钩子，确保代码一致性
- 📝 **编辑器适配**：自动生成 VSCode、Cursor 等编辑器的配置文件
- ⚛️ **框架优化**：针对 React、Next.js 等框架提供数百条优化规则
- 🔗 **Git 钩子支持**：可集成 Husky、Lint-staged 等工具实现自动化检查
- 🌐 **社区驱动**：被数千个开源项目使用，支持 MCP 实现远程代码检查

---

### [v1.4.0 · 基础用户界面](https://base-ui.com/react/overview/releases/v1-4-0)

**原文标题**: [v1.4.0 · Base UI](https://base-ui.com/react/overview/releases/v1-4-0)

v1.4.0 版本主要进行了多项组件改进和错误修复，提升了整体稳定性和用户体验。

- 🛠️ 通用改进：优化了渲染属性警告，修复了多个底层问题，如表单处理、隐藏输入属性支持及弹窗定位等
- 🚨 弹窗与对话框：修复了热重载问题，改进了触摸滚动和模态弹窗的滚动锁定
- 🔧 表单组件：修复了复选框、数字字段、滑块等组件的状态管理和输入控制问题
- 🎯 交互优化：改进了自动完成、组合框、菜单等组件的焦点管理、键盘导航和触摸交互
- 🆕 新增功能：引入了 OTPField 组件用于一次性密码输入，并增强了 Toast 的通知管理能力
- 🐛 错误修复：解决了多个组件在特定场景下的渲染问题、动画异常和可访问性缺陷

---

### [提升差异行性能的艰难攀登 - GitHub 博客](https://github.blog/engineering/architecture-optimization/the-uphill-climb-of-making-diff-lines-performant/)

**原文标题**: [The uphill climb of making diff lines performant - The GitHub Blog](https://github.blog/engineering/architecture-optimization/the-uphill-climb-of-making-diff-lines-performant/)

GitHub 团队针对大型 Pull Request 中“文件变更”标签页性能下降的问题，通过简化 React 组件结构、优化 DOM 节点和事件处理、引入虚拟化技术等多项策略，显著提升了渲染速度和响应性，降低了内存消耗。

- 🚀 **性能优化策略分层实施**：针对不同规模的 PR，采取从基础组件优化到虚拟化渐进降级的组合策略，确保日常操作流畅，极端情况仍可稳定使用。
- 🔧 **简化组件与 DOM 结构**：将每行差异的 React 组件从 8-13 个减少至 2 个，DOM 元素从 10-15 个精简，移除冗余事件处理器，大幅降低内存与渲染开销。
- 📉 **内存与响应时间显著改善**：在万行代码的 PR 测试中，JavaScript 堆内存降低约 50%，交互到下次绘制时间缩短 78%，DOM 节点减少 10%，组件渲染量下降 74%。
- 🖥️ **虚拟化技术应对极端规模**：对超过 1 万行的大型 PR 引入窗口虚拟化，仅渲染可视区域，使 JavaScript 堆内存和 DOM 节点减少 90%，交互延迟降至 40-80 毫秒。
- 🛠️ **全栈深度优化**：通过减少 React 重渲染、优化 CSS 与拖拽处理、增强监控与分段加载等，全面提升 UI 响应速度与用户体验。

---

### [React：单例模式并非如你所想的那般邪恶 - DEV 社区](https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8)

**原文标题**: [React: Singletons aren't as evil as you think - DEV Community](https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8)

本文探讨了在 React 中单例模式常被误解为难以追踪和测试的全局状态管理方式，但实际上通过现代方法可以使其变得强大、轻量且易于实现。

- 🚀 单例模式在 React 中并非天生邪恶，通过合理设计可以成为轻量高效的全局状态管理方案
- 🔄 传统实现方式依赖轮询或手动刷新，而现代方法利用事件监听实现自动同步
- 🏗️ 通过扩展 JavaScript 原生类（如 EventTarget）可以创建类型安全的单例，无需额外依赖
- 🎯 使用 useSyncExternalStore 钩子将外部状态与 React 组件无缝连接，实现自动渲染更新
- 🔔 以 Toast 通知系统为例演示了单例模式的实际应用，展示了跨组件通信的简洁性
- 🌉 这种基于原生类的单例方案不依赖特定框架，可在微前端或多框架环境中共享逻辑
- ⚡ 单例模式配合 React 新特性（如服务器组件）也能良好工作，状态管理独立于渲染树

---

### [垂直代码库](https://tkdodo.eu/blog/the-vertical-codebase)

**原文标题**: [The Vertical Codebase](https://tkdodo.eu/blog/the-vertical-codebase)

本文讨论了代码库结构从水平分层（按文件类型分组）转向垂直分组（按功能域分组）的重要性，并探讨了这种转变的优势、实施方法及挑战。

- 🏗️ 作者反对常见的按类型（如 components、hooks、utils）水平分割代码库的做法，认为这会导致代码难以维护和导航。
- 📈 水平结构在项目初期可能方便，但随着代码量增长，会变得混乱，例如 Sentry 代码库中 components 目录包含 200 多个无关文件。
- 🤖 即使有 AI 辅助，良好的代码结构（如清晰的边界、约束和快速反馈循环）对人和 AI 代理都至关重要，能提升开发效率。
- 🧠 代码应遵循“高内聚、低耦合”原则，将逻辑相关的代码（如组件、工具函数、类型）放在同一垂直域中，减少认知负荷。
- 🔄 垂直分组（按功能或业务域组织代码）能更好地匹配产品团队结构，提高代码的可发现性和可维护性。
- 🧩 共享代码（如设计系统组件）可作为独立垂直域处理，并通过 monorepo 或 lint 规则明确边界，控制依赖关系。
- ⚠️ 实施垂直结构的挑战包括正确划分功能域、避免重复实现，以及需要团队间更多沟通协作。

---

### [朝鲜攻击开源软件的蓝图 | 卡斯柯](https://casco.com/blog/the-blueprint-of-a-north-korean-attack-on-open-source)

**原文标题**: [The Blueprint of a North Korean Attack on Open-Source | Casco](https://casco.com/blog/the-blueprint-of-a-north-korean-attack-on-open-source)

本文深入分析了针对开源项目的供应链攻击，特别是通过伪装成合法贡献的恶意代码注入。攻击者利用区块链作为不可移除的恶意代码存储库，通过多阶段载荷逐步控制受害机器，最终窃取敏感信息并建立持久控制。

- 🚨 **攻击手法**：攻击者通过提交看似正常的 PR，在构建配置文件中植入恶意代码，利用混淆技术逃避检测。
- 🔗 **多阶段载荷**：恶意代码分三个阶段执行，从下载第二阶段的僵尸进程到获取第三阶段的 C2 服务器连接，逐步控制目标系统。
- 🌐 **区块链利用**：攻击者使用区块链（如 TronGrid 和 Binance Smart Chain）存储恶意载荷，使其难以被移除或追踪。
- 🛡️ **隐蔽性高**：代码经过高度混淆，静态分析难以发现，且利用 JavaScript 的`constructor`等特性动态执行恶意代码。
- 💥 **影响广泛**：一旦在 CI/CD 环境中执行，可能泄露 AWS 密钥、数据库凭证等高权限信息，并可能横向传播至其他依赖包。
- 📊 **潜在危害**：攻击可能导致数千台机器被感染，并通过受污染的发布管道影响数万最终用户系统。
- ⚠️ **防御挑战**：传统安全措施（如关闭恶意服务器）对基于区块链的攻击无效，需依赖代码审查和运行时监控。

---

