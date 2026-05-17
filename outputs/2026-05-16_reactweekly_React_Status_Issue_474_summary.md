### [从延迟到即时：现代化GitHub Issues导航性能 - GitHub博客](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

**原文标题**: [From latency to instant: Modernizing GitHub Issues navigation performance - The GitHub Blog](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

GitHub Issues 团队通过客户端缓存、智能预取和服务工作线程，将导航延迟从秒级降至瞬时，显著提升了用户体验。

- 🚀 **核心策略**：采用“本地优先”架构，从本地缓存即时渲染，后台异步验证数据新鲜度，实现“瞬时”体验。
- 📦 **IndexedDB 缓存**：为 React 软导航建立持久化客户端缓存，使约22%的导航变为“瞬时”，缓存命中率达33%。
- 🔥 **预热机制**：从高意图页面（如列表、仪表盘）智能预取数据，仅当缓存缺失时才发起网络请求，将缓存命中率提升至96%，70%的React导航实现“瞬时”。
- 🛠️ **服务工作线程**：拦截硬导航和Turbo导航请求，利用缓存数据跳过服务器渲染，显著加速冷启动和跨页面跳转。
- 📊 **性能提升**：导航延迟的P10从600ms降至70ms，P50从1200ms降至700ms，整体分布向“快速”和“瞬时”区间大幅偏移。
- ⚖️ **权衡与局限**：接受约4.7%的数据陈旧率以换取速度；冷启动和JavaScript执行仍是主要瓶颈，需进一步优化后端和UI交付层。

---

### [React开发者为何从Next.js转向TanStack - YouTube](https://www.youtube.com/watch?v=6moPS3AAbe4)

**原文标题**: [Why React Developers Are Leaving Next.js for TanStack - YouTube](https://www.youtube.com/watch?v=6moPS3AAbe4)

本頁面概述了YouTube平台相關的各項基本資訊與政策。

- 📰 **新聞中心**：提供YouTube官方新聞與公告。
- ©️ **版權**：說明內容版權相關規範與保護機制。
- 📞 **聯絡我們**：提供用戶與平台聯繫的管道。
- 🎨 **創作者**：針對內容創作者提供的資源與支援。
- 💰 **刊登廣告**：說明廣告投放與合作機會。
- 👨‍💻 **開發人員**：提供API、工具等技術資源。
- 📜 **條款**：列出使用YouTube服務的條款與條件。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋平台安全與內容審核政策。
- ⚙️ **YouTube 的運作方式**：解釋推薦系統、演算法等運作原理。
- 🧪 **測試新功能**：介紹平台正在測試的新功能。
- 📅 **© 2026 Google LLC**：版權年份與所屬公司資訊。

---

### [npm 泄露事件后 TanStack 的加固措施 | TanStack 博客](https://tanstack.com/blog/incident-followup)

**原文标题**: [Hardening TanStack After the npm Compromise | TanStack Blog](https://tanstack.com/blog/incident-followup)

TanStack 在 npm 遭入侵后已全面清理并强化安全，所有包目前安全可安装。

- 🔒 所有 TanStack 包（包括 Router 和 Start）现已安全，可放心安装。
- 🚨 攻击仅影响 Router/Start 仓库的 42 个包，每个包两个版本，已在 1 小时内弃用并被 npm 移除。
- 🛡️ 攻击通过恶意 PR 触发 CI 缓存投毒，窃取短期发布令牌，而非窃取维护者凭证。
- ⚙️ 已采取多项修复措施：禁用 pnpm 缓存、移除所有 GitHub Actions 缓存、将操作固定到提交 SHA、强制非 SMS 双因素认证、移除 `pull_request_target`、升级到 pnpm 11。
- 🔧 正在推进更深入的改进：添加 zizmor 静态分析、对 `.github` 文件夹设置 CODEOWNERS、改用更保守的缓存恢复方式。
- 💬 正在考虑限制外部贡献者直接提 PR，改为通过 issue 和邀请制提交代码，以进一步降低风险。
- 📝 团队承认工作流中存在已知危险模式（`pull_request_target`）未被及时修复，是此次事件的根本原因。

---

### [事后分析：TanStack npm 供应链安全事件 | TanStack 博客](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

**原文标题**: [Postmortem: TanStack npm supply-chain compromise | TanStack Blog](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

概述总结：
TanStack在2026年5月11日遭受npm供应链攻击，攻击者通过组合利用GitHub Actions的pull_request_target漏洞、缓存投毒和OIDC令牌提取，在42个包中发布了84个恶意版本。攻击在约26分钟内被外部研究人员发现，团队在约1小时43分钟内完成了所有受影响版本的弃用处理。所有其他TanStack仓库和包均未受影响，当前所有版本均安全。

- 🔍 攻击手法：组合利用pull_request_target“Pwn Request”模式、GitHub Actions缓存投毒和OIDC令牌内存提取，三个漏洞链式利用
- 🎯 影响范围：42个@tanstack/*包，84个恶意版本，仅影响Router/Start仓库
- ⏱ 响应时间：攻击后~26分钟被外部发现，~1小时43分钟完成全部84个版本弃用，~4小时35分钟npm完成最后包移除
- 🛡 恶意行为：安装时执行router_init.js脚本，窃取AWS/GCP/K8s/Vault凭证、npm/GitHub令牌、SSH密钥等，并通过Session/Oxen加密网络外传
- ✅ 安全状态：所有其他TanStack仓库和包未受影响，当前所有已发布版本均安全可安装
- 📋 IOC特征：optionalDependencies中包含@tanstack/setup的GitHub引用，router_init.js文件，特定缓存键和payload URL
- 💡 经验教训：需加强内部监控告警、审计pull_request_target工作流、固定第三方Action版本引用、改进OIDC发布验证机制

---

### [大规模供应链攻击波及TanStack、Mistral AI的npm和PyPI包——实时开源软件供应链安全](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)

**原文标题**: [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI Packages - Real-time Open Source Software Supply Chain Security](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)

2026年5月11日发生了一场大规模供应链攻击，波及npm和PyPI两个生态系统，共涉及172个软件包、404个恶意版本。攻击者针对TanStack、Mistral AI、UiPath、OpenSearch和Guardrails AI等知名项目，通过窃取的发布凭证发布恶意版本，植入凭证窃取载荷，并通过Session协议和GitHub基础设施进行数据外泄和横向移动。

- 📦 **大规模范围攻击**：攻击者一次性针对整个npm组织范围（如@tanstack、@uipath、@squawk）和PyPI上的高价值包（mistralai、guardrails-ai）发布恶意版本，而非单个包。
- 🎯 **高价值目标**：受影响项目包括TanStack路由器生态（42个包）、Mistral AI SDK（npm和PyPI）、UiPath自动化工具（65个包）、OpenSearch（周下载130万）和Guardrails AI。
- 🛠️ **双重触发机制**：npm包通过`preinstall`钩子（Mistral AI）或`optionalDependencies`指向恶意GitHub提交（TanStack）触发；PyPI包则在`import`时执行，而非`pip install`时。
- 🔑 **模块化凭证窃取**：载荷包含针对AWS、HashiCorp Vault、GitHub令牌（ghp_、gho_、ghs_）和npm发布令牌的专用窃取模块，支持横向移动。
- 🌐 **去中心化外泄**：使用Session协议（基于Oxen网络）进行数据外泄，无固定C2域名，难以阻断；同时利用GitHub提交搜索和仓库作为辅助C2通道。
- 🧬 **IDE和AI代理中毒**：通过GitHub GraphQL API向受害者仓库提交恶意配置文件（.vscode/tasks.json、.claude/settings.json），当开发者克隆或拉取时自动触发，形成自我传播链。
- ⚙️ **PyPI载荷差异**：PyPI包（mistralai 2.4.6、guardrails-ai 0.10.1）使用`__init__.py`注入，从`git-tanstack.com`下载`transformers.pyz`并执行，仅影响Linux系统。
- 🕵️ **技术细节**：载荷经过双层混淆（十六进制变量名 + AES解密），大小约2.2MB；Mistral AI包中引用`tanstack_runner.js`文件名，表明载荷模板复用且定制不完整。
- 🛡️ **缓解措施**：检查锁文件中是否包含受影响版本，固定依赖到已知安全版本；检查`/tmp/transformers.pyz`文件；轮换可能暴露的CI/CD凭证；使用SafeDep vet扫描依赖树。

---

### [深入解析新版Raycast的技术细节 - Raycast博客](https://www.raycast.com/blog/a-technical-deep-dive-into-the-new-raycast)

**原文标题**: [A Technical Deep Dive Into the New Raycast - Raycast Blog](https://www.raycast.com/blog/a-technical-deep-dive-into-the-new-raycast)

Raycast 2.0 是一次从底层重写的跨平台版本，旨在同时支持 macOS 和 Windows，并保持快速、愉悦和熟悉的用户体验。

- 🚀 采用混合架构：使用 TypeScript、Swift、C#、Rust、Node 和 React 构建，结合原生外壳与系统 WebView，实现跨平台 UI 和深度 OS 集成。
- 🔄 重写原因：从启动器扩展到生产力平台后，原始架构限制开发速度，且为支持 Windows 和未来功能，必须重新设计。
- 🧩 四层结构：包括原生宿主应用（Swift/C#）、Web 前端（React + TypeScript）、Node 后端和 Rust 核心，各层通过类型化 IPC 通信。
- 🗂️ 新文件索引器：用 Rust 自建索引器，直接扫描文件系统，支持 NTFS MFT 快速扫描，摆脱 Spotlight 依赖。
- 🎯 原生体验优化：通过调整 WebKit 行为（如禁用节流、预渲染）、遵循平台惯例（无光标指针、无悬停高亮），消除闪烁和卡顿。
- 💾 内存权衡：v2 内存占用约 350-450 MB（高于 v1 的 200-300 MB），但通过压缩内存、共享框架和积极优化，确保系统压力绿色。
- ⚡ 性能提升：搜索更快（集成 Rust 文件索引），文本渲染更佳（WebKit 优化），开发速度因热重载显著加快。
- 🌍 跨平台优势：大多数产品工作在共享前端和后端完成，一次开发支持 macOS 和 Windows，扩展无需额外下载 Node。
- ⚖️ 挑战：内存基线高、栈复杂度增加、Windows 多样性需测试更多边缘情况、部分原生功能（如窗口冷启动）需额外工作。
- 🎉 公开测试：团队认为权衡值得，未来将专注降低内存、优化性能，并继续推动桌面生产力创新。

---

### [面向开发者的Ghost — 为你的代理提供无限Postgres](https://ghost.build/developers/?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [Ghost for developers â Unlimited Postgres for your agents](https://ghost.build/developers/?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

概述总结
- 🗄️ Ghost提供无限数据库，支持分支、测试和丢弃，解决传统Postgres供应商限制问题
- ⚡ 允许AI代理安全操作数据库，通过分支保护主数据，异常时直接丢弃分支
- 🔄 支持并行测试不同数据库架构，无需承诺，轻松比较并保留最佳方案
- 🧪 为每个LLM原型提供临时数据库，用完即弃，无需清理
- 🛡️ 可快速回滚不良迁移，通过分支恢复历史状态，降低生产事故影响
- 🔍 每个PR自动创建真实数据库预览环境，验证架构变更，减少沟通成本
- 📊 支持从生产数据分支进行本地测试，避免使用虚假数据
- ⏱️ 四阶段实验流程：分支创建（毫秒级）、并行运行、基线比较、保留最佳丢弃其余
- 💻 通过CLI命令实现嵌入模型评估等复杂任务，三个命令完成全流程
- 🏙️ 社区已构建Pac-Man数据库游戏、多人城市建造器、锦标赛预测器等创新项目
- 🚀 鼓励自由实验，无需担心环境搭建成本，快速迭代尝试

---

### [React应用中的安全性 - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

**原文标题**: [Security in React Applications - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

React 应用安全指南：从 XSS 防御到服务端验证的全面防护

- 🛡️ React 内置 XSS 防护：JSX 自动转义特殊字符（如 `<`、`>`），将用户输入视为文本而非 HTML，防止脚本注入
- ⚠️ 危险操作 `dangerouslySetInnerHTML`：直接设置 innerHTML 会绕过防护，必须先用 DOMPurify 库清理 HTML，移除危险标签和事件处理器
- 🔐 安全认证与 CSRF 防护：使用 HttpOnly、Secure、SameSite=Strict 属性的 Cookie 存储令牌，防止 XSS 窃取；配合 CSRF 令牌验证请求来源
- ✅ 服务端输入验证：用 Zod 模式验证 Server Functions 的输入数据，结合参数化查询（如 `$1` 占位符）防止 SQL 注入，并先验证用户权限
- 📜 内容安全策略（CSP）：通过 HTTP 头限制资源加载，使用 nonce 允许内联脚本，并用 `Content-Security-Policy-Report-Only` 测试策略
- 🔗 多层防御体系：结合 React 默认保护、安全认证模式、服务端验证和浏览器策略，形成完整安全防线

---

### [龙湖](https://longho.dev/posts/rsc-server-functions-are-not-an-api-boundary/)

**原文标题**: [Long Ho](https://longho.dev/posts/rsc-server-functions-are-not-an-api-boundary/)

概述：本文探讨了人工智能在医疗诊断中的应用，强调了其提高准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🤖 人工智能通过分析医学影像和患者数据，能辅助医生更快速、准确地诊断疾病。
- 📊 机器学习模型在处理大量病例时，可识别出人类医生可能忽略的细微模式。
- 🔒 数据隐私问题成为关键障碍，患者信息的安全存储和合规使用需严格规范。
- ⚖️ 算法偏见可能导致诊断结果不公平，需通过多样化训练数据来减少偏差。
- 🏥 尽管技术前景广阔，但人工智能目前仍需与人类专家协作，而非完全替代。

---

### [React.Activity 的隐性成本 | Peter Piekarczyk](https://www.peterp.me/articles/hidden-cost-of-react-activity/)

**原文标题**: [The hidden cost of React.Activity | Peter Piekarczyk](https://www.peterp.me/articles/hidden-cost-of-react-activity/)

### 概述总结
React.Activity 在隐藏子树时保留状态但销毁副作用，重新显示时重建副作用，这可能导致性能成本被转移到用户交互路径上，尤其在副作用密集的 React Native 应用中。

- 🎭 **隐藏成本真相**：Activity 保留状态但销毁并重建 Effects，并非简单的"保持挂载但不可见"，而是"保留状态，停止副作用，稍后重新启动"。

- ⚡ **副作用累积效应**：React Native 应用天然包含大量副作用（订阅、监听、测量、分析等），当复杂屏幕从 Activity 边界恢复时，会触发订阅重建、观察者重连、额外渲染等连锁反应。

- 🔄 **setState 乘数效应**：Effect 内同步调用 setState 会导致额外渲染循环，在密集屏幕中多个组件同时执行此模式时，性能成本会指数级放大。

- 📦 **生态库影响**：TanStack Query 和 Jotai 依赖 useEffect 管理订阅，Zustand 核心使用 useSyncExternalStore 更优，但自定义封装仍可能带来成本。

- 🏗️ **密集屏幕问题**：嵌套设计系统组件、查询消费者、测量逻辑、分析钩子等组合在一起时，Activity 恢复会触发大规模协调重建，而非简单恢复。

- ✅ **适用场景**：适合表单、小型详情面板等子树不大、副作用轻量、用户可能很快返回的内容。

- ⚠️ **谨慎场景**：避免用于嵌套组件多、副作用密集、重复订阅、昂贵挂载逻辑的复杂屏幕。

- 🔍 **实践建议**：使用 Activity 前审计子树，查找立即调用 setState 的 useEffect、挂载专属逻辑、可上移的重复订阅、隐藏在设计系统组件中的昂贵钩子。

- 💡 **核心洞察**：Activity 真正考验的是副作用管理质量，而非单纯的状态保留能力。

---

### [MDXEditor - 富文本Markdown编辑器React组件](https://mdxeditor.dev/)

**原文标题**: [MDXEditor - the Rich Text Markdown Editor React Component](https://mdxeditor.dev/)

## 概述总结
MDXEditor 是一个开源 React 组件，让用户像在 Google Docs 或 Notion 中一样自然编辑 Markdown 文档，实现所见即所得的编辑体验。

- 📝 **所见即所得编辑**：无需在编辑和预览模式间切换，直接编辑富文本内容，样式与最终页面一致
- 🎨 **内容样式自定义**：通过 `contentEditableClassName` 属性应用自己的 CSS 类来美化编辑区域
- 🔧 **代码块语法高亮**：支持语言感知编辑，可配置项目使用的代码语言，并集成 CodeMirror 实现可编辑代码块
- ⚙️ **可配置 Markdown 输出**：通过 `toMarkdownOptions` 调整项目符号、强调标记等格式设置，保持输出一致性
- 🛠️ **丰富功能特性**：包括表格编辑器、链接对话框、图片支持、Front-matter 编辑器、Markdown 快捷键、差异/源码视图、指令及 MDX 组件支持
- 🎯 **可定制工具栏**：提供灵活的工具条配置，满足不同编辑需求

---

### [命运 1.0 | 命运](https://fate.technology/posts/fate-1.0)

**原文标题**: [fate 1.0 | fate](https://fate.technology/posts/fate-1.0)

fate 1.0 正式发布，这是一个为生产环境设计的 React 数据框架，结合视图组合、标准化缓存、数据掩码和异步 React 功能，旨在消除命令式缓存管理和请求中心的状态处理。

- 🚀 **核心特性**：fate 通过组合视图（Views）在应用根节点生成单一请求，使用标准化对象缓存而非请求缓存，实现精确乐观更新、高效实时订阅和可预测缓存行为。
- 🔄 **实时视图**：1.0 引入 `useLiveView` 和 `useLiveListView` 钩子，通过服务器发送事件（SSE）零配置订阅后端实时更新，仅更新受影响组件。
- 🛠️ **新集成**：新增 Drizzle 支持，提供原生 HTTP 传输（无需 tRPC），并扩展 `@nkzw/fate/server` 以简化数据库和协议集成。
- ⚡ **Vite 插件**：替代手动代码生成，自动处理服务器 API 类型变化，同时保留 CLI 用于 CI 或自定义工作流。
- 🗑️ **垃圾回收**：受 Relay 启发，自动释放未挂载组件的数据，默认保留最近 10 个已释放请求的数据，实现即时导航与内存优化。
- 🐛 **修复与优化**：改进乐观更新排序、请求生命周期处理、稳定视图引用、大列表更新性能等多项修复。
- 🎨 **应用脚手架**：通过 `create-fate` 包快速启动，支持 Drizzle + tRPC、Drizzle + HTTP、Prisma + tRPC 等模板。
- 🌐 **未来方向**：与 Void Router 集成，构建首个专为异步 React 设计的元框架，探索声明式数据模型驱动的可扩展、可中断、响应式用户体验。

---

### [React 回顾](https://react.review/)

**原文标题**: [React Review](https://react.review/)

React Review 是一个通过 GitHub 集成自动审计 React 代码库、检查不良代码模式的工具，由 Million 团队开发，强调安全与只读访问。

- 🔍 自动审计 React 代码库，发现不良代码模式
- 📂 通过粘贴 GitHub 仓库 URL 或搜索关键词即可使用
- 🔒 仅请求只读权限，绝不写入代码库或存储源代码
- 🗑️ 分析后立即丢弃代码，不用于模型训练
- 🔄 可随时撤销授权，一键从 GitHub 卸载
- 🏢 由 Million 团队开发（React Doctor、React Scan 和 Million.js 的创建者）
- 🎯 获得 Y Combinator (W24) 支持，总部位于旧金山
- ❓ 提供常见问题解答，涵盖企业版、安全性和兼容性

---

### [GitHub - orval-labs/orval: orval 能够从任何有效的 OpenAPI v3 或 Swagger v2 规范（无论是 yaml 还是 json 格式）生成具有适当类型签名（TypeScript）的客户端。🍺](https://github.com/orval-labs/orval)

**原文标题**: [GitHub - orval-labs/orval: orval is able to generate client with appropriate type-signatures (TypeScript) from any valid OpenAPI v3 or Swagger v2 specification, either in yaml or json formats. 🍺 · GitHub](https://github.com/orval-labs/orval)

Orval 是一个从 OpenAPI 规范生成类型安全 TypeScript 客户端的开源工具，支持多种前端框架和库，并提供丰富的测试与开发工作流。

- ⚙️ 支持从 OpenAPI v3 或 Swagger v2 规范（YAML/JSON）生成类型安全的 JS/TS 客户端
- 🧩 兼容 React、Vue、Svelte、Solid、Angular、Hono 等多种框架及查询库（如 React Query、SWR）
- 🧪 提供完整的开发工作流：构建、类型检查、单元测试、快照测试和 CLI 验证
- 🛠️ 使用 Bun 作为包管理器和构建工具，支持一键清理、构建和测试
- 🤖 对 AI 生成代码持开放态度，但要求贡献者自行审查并理解变更
- 🌟 项目在 GitHub 上获得 5.8k 星标，拥有 603 个分支和 219 个发布版本
- 💰 通过 Open Collective 接受赞助，支持持续开发

---

### [内联日期时间选择器 | Mantine](https://mantine.dev/dates/inline-date-time-picker/)

**原文标题**: [InlineDateTimePicker | Mantine](https://mantine.dev/dates/inline-date-time-picker/)

InlineDateTimePicker 是一个支持日期和时间范围选择的内联组件，无需下拉菜单即可直接显示日历和时间选择器。

- 📅 内联显示：组件将日历和时间选择器直接渲染在页面上，无需下拉操作
- ⏱️ 秒数支持：通过 `withSeconds` 属性可启用秒数输入，满足精确时间需求
- 🔄 范围选择：设置 `type="range"` 后可选择日期时间范围，并显示两个时间输入框和范围摘要
- 🎛️ 受控模式：支持通过 `value` 和 `onChange` 属性实现受控状态管理
- 📝 格式自定义：使用 `valueFormat` 属性可自定义范围预览的 dayjs 格式，如 "MMMM YYYY, DD HH:mm"
- 🧩 兼容性：支持大多数 DatePicker 组件的属性，可参考 DatePicker 文档获取更多功能

---

### [发布 6.4.0 · ant-design/ant-design · GitHub](https://github.com/ant-design/ant-design/releases/tag/6.4.0)

**原文标题**: [Release 6.4.0 · ant-design/ant-design · GitHub](https://github.com/ant-design/ant-design/releases/tag/6.4.0)

Ant Design 6.4.0 版本发布，包含大量新组件、全局配置增强、语义化结构支持、无障碍改进和错误修复。

- 🔥 新增 BorderBeam 边框流光组件，在容器边框上呈现流动的高光动画效果
- 🆕 ConfigProvider 新增 Select、DatePicker、Modal、Upload、Mentions 等多个组件的全局配置支持
- 🆕 Input 新增 allowClear.disabled 属性、clear 语义化片段和 Search 图标自定义
- 🆕 Image 新增加载进度指示器、预览蒙层 closable 和 closeIcon 语义化节点
- 🆕 Splitter 新增 destroyOnHidden 属性、折叠面板平滑过渡动画
- 🐞 修复 Select 选中项样式优先级、error 状态颜色、字体 token 等问题
- 🆕 Theme 新增 colorErrorAffix 和 colorWarningAffix Design Token
- 🆕 Typography 新增 actions 位置配置、表格元素默认样式和灵活语义结构
- 🆕 Button 新增 solid 变体默认颜色支持
- 🆕 DatePicker 新增多选模式 tagRender 属性
- 🆕 Form 新增 ConfigProvider 下 labelAlign 全局控制和语义化 DOM 支持
- 🆕 Table 新增 column 配置和 scrollTo align 参数
- 🆕 Tag、Tree、Wave、Alert、Anchor、App、Badge、Calendar、Cascader、FloatButton、Modal、Popconfirm、Statistic、Tabs、Tour、Transfer 等多个组件新增功能或语义化支持
- 🐞 修复 Menu、Notification、Checkbox、Dropdown、Mentions、Watermark 等组件的布局或兼容性问题
- 🆕 新增 8 种语言的 Form 默认验证消息
- 📖 新增 Agent Readiness 文件提升 AI 代理友好度

---

### [GitHub - gre/react-native-view-shot: 对React Native视图进行快照并保存为图像 · GitHub](https://github.com/gre/react-native-view-shot)

**原文标题**: [GitHub - gre/react-native-view-shot: Snapshot a React Native view and save it to an image · GitHub](https://github.com/gre/react-native-view-shot)

react-native-view-shot 是一个用于将 React Native 视图捕获为图像的开源库，支持新旧架构，拥有 2.9k 星标和 368 个分支，兼容 iOS、Android、Windows 和 Web 平台。

- 📸 **核心功能**：通过 `ViewShot` 组件或 `captureRef` 方法，轻松将 React Native 视图捕获为图像，支持 PNG、JPG、WebM 和 RAW 格式。
- 🚀 **新架构支持**：从版本 4.0+ 起完全支持 React Native 的新架构（Fabric + TurboModules），要求 React Native >= 0.76.0 和 Node.js >= 20。
- 🛠️ **多种捕获模式**：提供 `mount`、`continuous`、`update` 等捕获模式，以及手动捕获方式，灵活满足不同场景需求。
- 📦 **安装简便**：通过 npm 或 yarn 安装，在 Expo 中也可使用，iOS 需要额外安装 CocoaPods 依赖。
- 🎯 **高级 API**：支持 `captureRef` 和 `captureScreen` 方法，可自定义文件名、格式、质量、结果类型（tmpfile、base64、data-uri）等参数。
- 🔄 **ScrollView 支持**：通过 `snapshotContentContainer` 选项可捕获整个滚动内容，但需注意 FlatList 的虚拟化限制和 Windows 平台不支持。
- ⚡ **性能优化**：引入 RAW 图像格式和 zip-base64 压缩，减少内存分配和 GC 压力，提升截图速度（RAW 格式下小于 16ms）。
- 🐛 **常见问题解决**：提供针对黑屏、空白结果、透明背景、GL 视图捕获等问题的解决方案，建议设置 `collapsable={false}` 和背景色。
- 🌐 **跨平台兼容性**：支持 iOS、Android、Windows 和 Web，但部分组件（如 react-native-video、react-native-camera）可能不兼容，详见互操作性表。

---

### [GitHub - yudielcurbelo/react-qr-scanner: 一个用于在React中扫描二维码的库](https://github.com/yudielcurbelo/react-qr-scanner)

**原文标题**: [GitHub - yudielcurbelo/react-qr-scanner: A library to scan QR Codes in react. · GitHub](https://github.com/yudielcurbelo/react-qr-scanner)

这是一个基于 React 的二维码和条码扫描库，支持多种格式、相机控制和自定义 UI。

- 📱 **多格式支持**：支持 QR 码、EAN、UPC、Code 128 等多种一维和二维条码格式
- 🎥 **相机控制**：内置闪光灯、变焦和摄像头切换功能
- 🔄 **灵活扫描模式**：支持连续扫描、单次扫描、暂停/恢复功能
- 🎨 **自定义追踪**：可在检测到的条码上绘制自定义覆盖层和追踪可视化
- 📋 **设备选择**：通过 `useDevices` 钩子选择特定摄像头
- 🎵 **音频反馈**：扫描成功时可播放提示音，支持自定义音效
- 🛠️ **TypeScript 支持**：完全类型化，提供优秀的开发体验
- 🌐 **跨浏览器兼容**：通过 `webrtc-adapter` 支持现代浏览器
- 📦 **轻量级**：依赖少，优化打包体积

---

### [styled-components v7 | styled-components](https://styled-components.com/docs/v7)

**原文标题**: [styled-components v7 | styled-components](https://styled-components.com/docs/v7)

### 概述摘要

styled-components v7 是一次重大的架构改革，引入了自研CSS解析器，重写了原生运行时，并致力于实现Web、iOS和Android上统一的CSS体验。该版本带来了许多新特性，包括现代CSS支持、原生动画、改进的插件系统等，但需要React 19+和React Native 0.85+作为依赖。

### 关键要点

- 🚀 **重大架构更新**：用自研CSS解析器替换了stylis，重写了原生运行时，旨在实现跨平台一致的CSS体验。
- 🎨 **React Native现代CSS支持**：支持`@media`、`@container`查询、现代颜色空间、数学函数、视口单位、渐变和滤镜等。
- 🔗 **React Native选择器和组合器**：支持属性选择器、`:not()`、`:has()`、树结构伪类以及组件间的组合器。
- ✨ **原生动画默认启用**：`transition`、`@keyframes`和`@starting-style`现在默认在React Native上通过内置的`Animated`适配器运行。
- 🎭 **原生平台`createTheme()`**：与Web版相同的`createTheme()`和`<ThemeProvider>`，支持主题深合并。
- 🔌 **插件系统重构**：插件移至`styled-components/plugins`子路径，提供了新的`SCPlugin`接口，替代了旧的stylis插件。
- 🏎️ **性能与SSR优化**：全局样式只生成一次，SSR在大规模场景下更快，并提供了`extractCSS()`方法。
- ⚠️ **破坏性变更与迁移**：移除了`defaultProps`、`disableCSSOMInjection`和`enableVendorPrefixes`，需要更新依赖版本（React 19+，React Native 0.85+）。
- 📱 **React Native的CSS重映射**：通过`.attrs((props, ast) => ...)`函数形式，可以将CSS声明映射到原生组件的props上。
- 🧩 **React Native的已知限制**：部分CSS特性（如`::before`/`::after`、`backdrop-filter`、CSS Grid等）在原生平台上尚不支持。

---

### [目录同步（SCIM）现已全面可用](https://clerk.com/changelog/2026-04-16-directory-sync?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=scim&utm_content=05-15-26&dub_id=f7AtfCv4VjiFVQuv)

**原文标题**: [Directory Sync (SCIM) is now generally available](https://clerk.com/changelog/2026-04-16-directory-sync?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=scim&utm_content=05-15-26&dub_id=f7AtfCv4VjiFVQuv)

概述摘要
- 📢 目录同步（SCIM）现已全面可用，所有用户均可使用。
- 🆕 新增自定义属性映射功能，可将IdP中的额外用户数据（如部门、员工ID）同步到Clerk用户对象的publicMetadata中。
- 🔄 支持基于IdP组的自动角色分配，用户加入或离开组时自动调整Clerk角色。
- ⚙️ 可在Clerk Dashboard中启用目录同步，生成SCIM URL和令牌以配置IdP。
- 📚 提供Okta和Microsoft Entra ID的设置指南，以及自定义属性映射的详细文档。
- ⚠️ 遵循SCIM 2.0协议，但可能与IdP不完全兼容，遇到问题可联系团队解决。
- 💰 目录同步包含在企业连接中，无需额外费用。

---

### [我对AI的思考，第一部分：恐惧、观点与心路历程 · Mark的开发博客](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-1-fears-opinions-journey/)

**原文标题**: [
     My Thoughts on AI, Part 1: Fears, Opinions, and Mental Journey ·  Mark's Dev Blog
  ](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-1-fears-opinions-journey/)

本文作者是一名资深软件工程师，分享了从最初对AI写代码充满恐惧、抵触，到后来逐渐尝试、接受，并最终将AI作为强大辅助工具的完整心路历程。作者承认许多对AI的担忧（如对行业、社会的影响）至今仍然存在，但个人通过实践发现，AI能极大地提升工作效率，并让自己重新找回编程的乐趣和创造力，关键在于如何正确引导和使用它。

- 🧠 **从恐惧到接纳**：作者最初坚信AI写代码不可靠、会毁掉编程工艺，甚至因此陷入轻度抑郁，但在一次会议后决心改变心态，开始尝试使用AI。
- 🛠️ **实践出真知**：通过让AI编写测试代码、实现复杂功能（如Rust库的流式支持）、优化开源库（如Immer）等具体任务，作者亲身体验到AI的强大和实用价值，彻底改变了看法。
- ⚡ **效率与创造力倍增**：AI让作者能快速生成大量代码、探索多种方案、甚至启动之前因时间不足而搁置的副项目，极大地提升了产出和创造力。
- 🎯 **人类仍是主导**：作者强调，AI的成功使用依赖于自身的深厚经验和判断力。人类负责提供愿景、意图和方向，AI则负责高效执行和扩展细节。
- ⚠️ **担忧并未消失**：作者依然对AI对行业新人、社会思考能力、以及资本主义驱动下的“无限制加速”感到忧虑，并呼吁业界应追求可持续、可维护的发展节奏。
- 🧩 **非确定性可控**：尽管AI输出具有非确定性，但通过提供充分的上下文、编写清晰的提示、设置自动化检查（如测试、lint）等“护栏”，可以使其结果足够可靠。
- 🎨 **工艺的演变**：作者认为，编程的“工艺”并未消失，而是从手写每一行代码，演变为更高层次的“设计”和“引导”——即如何利用AI工具来构建出符合自己品味的软件。

---

### [Jotai v2.20.0 与存储构建模块](https://newsletter.daishikato.com/p/jotai-v2-20-0-and-the-store-building-blocks)

**原文标题**: [Jotai v2.20.0 and the Store Building Blocks](https://newsletter.daishikato.com/p/jotai-v2-20-0-and-the-store-building-blocks)

Jotai v2.20.0 版本发布，重点改进了存储构建块的性能，并为未来 v3 版本做准备。

- 📦 引入存储构建块概念：在 v2.12.0 中，通过暴露内部机制允许生态系统库扩展核心功能，避免创建后修改存储导致的不一致问题。
- 🛠️ 构建块 API 演进：从最初有限的自定义能力，到 v2.15.0 版本实现灵活且安全的 API，减少误用风险。
- ⚡ 性能回归修复：因使用 WeakMap 导致性能下降，v2.20.0 改用参数传递方式解决，虽不完美但符合设计思路。
- 🚀 展望 v3 版本：v2.20.0 发布后，作者准备着手规划 Jotai v3 的重大更新。

---

### [别再等待JSON：用一个Schema流式输出结构化数据 | TanStack博客](https://tanstack.com/blog/streaming-structured-output)

**原文标题**: [Stop Waiting on JSON: Stream Structured Output with One Schema | TanStack Blog](https://tanstack.com/blog/streaming-structured-output)

TanStack AI 的 useChat 现在支持通过 outputSchema 参数直接获取类型安全的流式结构化输出，无需手动解析 JSON 或编写样板代码。

- 🎯 **核心改进**：`useChat({ outputSchema })` 现在直接返回类型安全的 `partial`（DeepPartial<T>）和 `final`（T | null），无需手动管理状态、解析 JSON 或类型转换。
- 🧹 **消除样板代码**：移除了手动累加字符串缓冲区、调用 `parsePartialJSON`、类型转换和 `onChunk` 处理器的需求，代码从 15+ 行减少到 3 行。
- 🔧 **底层增强**：`StructuredOutputStream<T>` 成为真正的判别联合类型；其他自定义事件（如 ApprovalRequestedEvent）也获得了类型标签；结构化路径现在支持逐块调试日志。
- 🌐 **框架与提供商支持**：在 React、Vue、Solid、Svelte 中一致工作；支持 OpenAI、OpenRouter、Grok、Groq、Ollama 等提供商；summarize 适配器也获得了端到端流式支持。
- 💡 **设计理念**：将 `outputSchema` 集成到现有 `useChat` 中，而非创建单独钩子，使得升级路径简单（只需添加一个 prop），并避免文档和用户混淆的成本。

---

### [Node.js 26 的新特性](https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-26/)

**原文标题**: [What's new in Node.js 26](https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-26/)

### 概述摘要
Node.js 26 引入了 Temporal API、Map 辅助方法、Iterator.concat() 等实用功能，并移除了多项旧版 API，提升了开发体验和性能。

- 🕐 **Temporal API 稳定**：默认启用，提供不可变、时区感知的日期时间处理，替代易错的 `Date` 对象。
- 📦 **Map 新方法**：`getOrInsert` 和 `getOrInsertComputed` 简化缓存和分组逻辑，减少样板代码。
- 🔗 **Iterator.concat()**：惰性组合多个迭代器，无需中间数组，支持链式操作（如 `filter`、`take`）。
- 🔐 **Crypto 原始 Ed25519 密钥**：支持直接导入原始密钥，移除繁琐的 PKCS#8 封装。
- ⚡ **V8 14.6 和 Undici 8**：提升运行时性能和 `fetch()` 效率。
- 🧹 **清理旧 API**：移除 `_stream_*` 模块、`writeHeader()`、`--experimental-transform-types`，`module.register()` 被弃用。
- 🚀 **升级建议**：新项目可立即使用，生产环境建议等待 2026 年 10 月 LTS 版本。

---
