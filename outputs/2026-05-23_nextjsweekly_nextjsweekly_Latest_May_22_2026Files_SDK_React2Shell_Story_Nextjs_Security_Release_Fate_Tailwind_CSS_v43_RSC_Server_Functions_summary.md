### [Next.js 2026年5月安全发布 - Vercel](https://vercel.com/changelog/next-js-may-2026-security-release)

**原文标题**: [Next.js May 2026 security release - Vercel](https://vercel.com/changelog/next-js-may-2026-security-release)

Next.js 发布了协调安全更新，修复了 13 个安全公告，涵盖拒绝服务、中间件和代理绕过、服务器端请求伪造、缓存投毒和跨站脚本攻击。其中一个公告涉及上游 React 服务器组件漏洞（CVE-2026-23870）。所有受影响用户应立即升级到修补版本。

- 🛡️ **中间件和代理绕过**：影响依赖 middleware.js 或 proxy.js 进行授权的应用，包括通过 App Router 段预取 URL、动态路由参数注入等方式绕过认证，以及中间件重定向缓存投毒。
- 🚫 **拒绝服务**：影响使用 Server Functions、Partial Prerendering 或 Image Optimization API 的应用，包括 React 服务器组件中的 DoS（CVE-2026-23870）、连接耗尽和图片优化 API 导致的 DoS。
- 🌐 **服务器端请求伪造**：影响处理 WebSocket 升级请求的应用，存在 SSRF 风险。
- 🧪 **缓存投毒**：影响在 React 服务器组件响应前有缓存层的应用，包括缓存投毒和 RSC 缓存破坏碰撞。
- ⚠️ **跨站脚本**：影响在 App Router 中使用 CSP nonces 或 beforeInteractive 脚本处理不可信输入的应用，存在 XSS 风险。
- 🔧 **修复版本**：Next.js 15.5.18 和 16.2.6，React 19.0.6、19.1.7 和 19.2.6（针对 react-server-dom-* 包）。所有受影响用户应立即升级。

---

### [文档：跨文档的更多服务器操作安全指南，由icyJoseph提交 · 拉取请求 #90878 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/90878/files)

**原文标题**: [docs: More Server Actions security guidance across docs by icyJoseph · Pull Request #90878 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/90878/files)

该 PR (#90878) 在 Next.js 文档中增加了更多关于 Server Actions 安全性的指导，已合并到 canary 分支。

- 📝 强调 Server Actions 可通过直接 POST 请求访问，而不仅限于 UI 调用，必须始终在内部进行身份验证和授权检查
- 🔒 明确页面级身份验证检查不覆盖其内部定义的 Server Actions，需在 action 内重新验证用户身份
- 🛡️ 新增授权检查示例，防止不安全的直接对象引用（IDOR）漏洞，确保用户有权操作特定资源
- 🗂️ 推荐使用数据访问层（DAL）处理变更操作，将身份验证、授权和数据库逻辑集中在 server-only 模块中
- 🚫 控制 Server Actions 的返回值，仅返回客户端所需的数据，避免暴露内部字段
- ⏱️ 对耗时操作（如发送邮件、写入数据库）考虑添加速率限制以防止滥用
- 📋 更新审计清单，增加对 action 参数验证、资源所有权检查、返回值过滤及数据库访问委托的检查项

---

### [AI代码审查 | CodeRabbit | 免费试用](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=coderabbit_may&utm_term=erfannextjs&dub_id=3fmJrsmH2JiCVQXL)

**原文标题**: [AI Code Reviews | CodeRabbit | Try for Free.](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=coderabbit_may&utm_term=erfannextjs&dub_id=3fmJrsmH2JiCVQXL)

概述总结
- 🐰 CodeRabbit 引入前，代码质量取决于审查 PR 的人。
- 📏 CodeRabbit 引入后，所有 PR 都遵循统一的质量标准。

---

### [React2Shell 的故事 | Lachlan Davidson | 博客](https://lachlan.nz/blog/the-react2shell-story/)

**原文标题**: [The React2Shell Story | Lachlan Davidson | Blog](https://lachlan.nz/blog/the-react2shell-story/)

概述：安全研究员Lachlan Davidson在React的Flight协议中发现了一个严重远程代码执行漏洞（CVE-2025-55182），并报告给Meta。该漏洞影响了数百万网站，通过利用Flight协议中缺失的安全检查，攻击者可以构造恶意载荷实现任意代码执行。

- 🚀 **漏洞发现起源**：研究员出于好奇想理解Flight协议，却意外发现了一个影响数百万网站的关键漏洞。
- 🔍 **Flight协议缺陷**：协议允许引用对象原型上的属性，这是“一个明显缺失的安全检查”，攻击者可借此获取继承属性。
- 🛠️ **攻击向量**：开发者常忽视用户输入验证，Flight允许发送比JSON更复杂的对象，可被用于类型强制转换和显式函数调用攻击。
- 🧩 **利用链构建**：通过thenable对象和React内部Chunk对象，攻击者能链式调用函数，最终调用`Module._load`实现任意代码执行。
- 💡 **最终PoC**：研究员在Chunk代码中找到一处调用，通过控制`_formData.get()`的参数构造恶意函数，最终触发RCE。
- 📢 **披露与修复**：Meta在17小时内确认漏洞并修复，团队通宵工作开发补丁、协调通信，并准备CVE发布。
- 🌐 **影响范围**：从大型AI公司到加密货币交易平台，Next.js非常流行且面向公众，漏洞可能造成毁灭性影响。

---

### [Next.js 链接作为按钮 | Kitty Giraudel](https://kittygiraudel.com/2026/05/02/nextjs-link-as-a-button/)

**原文标题**: [Next.js Link as a Button | Kitty Giraudel](https://kittygiraudel.com/2026/05/02/nextjs-link-as-a-button/)

以下是对文章内容的总结：

在 Next.js 中使用第三方按钮组件（如 Ant Design）进行路由导航时，直接传递 `href` 会导致全页刷新，而非客户端路由导航。文章介绍了两种解决方案。

- 🚫 **方法一：命令式路由**：使用 `useRouter().push()` 实现导航，但会渲染 `<button>` 元素而非 `<a>`，不符合语义和可访问性标准。
- 🔗 **方法二：无头链接**：结合 Next.js 的 `passHref` 和 `legacyBehavior` 属性，使 `<Link>` 不渲染 DOM，而是将 `href` 传递给子组件，从而让 Ant Design 的 `Button` 渲染为 `<a>` 元素，实现正确的路由导航。
- ⚠️ **注意事项**：`legacyBehavior` 是旧版行为，未来可能被移除，此方法并非长期稳定方案。
- 🧩 **可复用组件**：创建 `RouterButton` 封装组件，统一处理 `href` 和链接属性，同时保留 Ant Design 按钮的所有样式和功能，确保渲染出单一的 `<a>` 元素，支持 Next.js 路由且无全页刷新。

---

### [龙湖](https://longho.dev/posts/rsc-server-functions-are-not-an-api-boundary/)

**原文标题**: [Long Ho](https://longho.dev/posts/rsc-server-functions-are-not-an-api-boundary/)

概述摘要：本文探讨了人工智能在医疗领域的应用，重点分析了诊断辅助、药物研发和个性化治疗方案的优势与挑战，并强调了数据隐私和伦理问题的重要性。

- 🩺 人工智能通过分析医学影像和病历数据，显著提升了疾病诊断的准确性和效率。
- 💊 在药物研发中，AI加速了候选药物筛选和临床试验设计，缩短了新药上市周期。
- 🧬 个性化治疗借助AI分析患者基因和生活习惯，制定更精准的医疗方案。
- 🔒 数据隐私和伦理问题成为AI医疗应用的关键挑战，需加强法规和透明度。
- ⚖️ 未来需平衡技术创新与患者权益，确保AI在医疗中的安全与公平性。

---

### [GitHub - haydenbleasel/files-sdk：一个统一的对象和Blob后端存储SDK。一个简洁、诚实的API。基于Web标准的I/O。](https://github.com/haydenbleasel/files-sdk)

**原文标题**: [GitHub - haydenbleasel/files-sdk: A unified storage SDK for object and blob backends. One small, honest API. Web-standards I/O. · GitHub](https://github.com/haydenbleasel/files-sdk)

Files SDK 是一个统一的存储 SDK，为对象和 blob 后端提供一致的小型 API，支持 Web 标准 I/O 并允许访问原生客户端。

- 📦 **统一 API** — 提供 upload、download、head、exists、delete、copy、list、url 等一致方法，跨 S3、GCS、Azure、Vercel Blob 等提供商使用相同接口
- 🔌 **可选依赖** — 仅安装实际使用的提供商原生 SDK（如 @aws-sdk/client-s3）作为可选对等依赖，减少冗余
- 🌐 **Web 标准 I/O** — 输入输出使用 Blob、File、ReadableStream、Uint8Array 等标准类型，无提供商特定类型泄漏
- 🚪 **逃生舱** — 通过 files.raw 直接访问原生客户端，随时使用提供商特有功能
- 🌳 **可摇树优化** — 每个适配器为独立入口点，仅打包导入的部分
- 📁 **文件句柄** — 使用 files.file(key) 重复操作同一对象，简化代码
- 🤖 **AI 工具集成** — 支持 Vercel AI SDK、OpenAI、Anthropic Claude 等 AI SDK，让模型浏览和操作存储
- 📋 **适配器目录** — 覆盖 S3、云平台、边缘服务、本地文件系统和消费级提供商，持续增长

---

### [GitHub - nkzw-tech/fate: fate 是一个面向 React 的现代数据客户端。](https://github.com/nkzw-tech/fate)

**原文标题**: [GitHub - nkzw-tech/fate: fate is a modern data client for React. · GitHub](https://github.com/nkzw-tech/fate)

fate 是一个受 Relay 和 GraphQL 启发、为 React 打造的现代数据客户端，它结合了视图组合、规范化缓存、数据屏蔽、Async React 特性以及类型安全的数据获取，旨在提供更可组合、声明式和可预测的数据获取与状态管理体验。

- 🎯 **核心特性**：支持视图组合（减少网络请求）、规范化缓存（避免数据重复与过时）、数据屏蔽与严格选择（防止组件间意外耦合）、Async React 特性（支持并发渲染）、列表分页、乐观更新、实时视图（通过 SSE）以及 AI 友好（API 简洁可预测）。
- 🧩 **视图概念**：组件通过 `view()` 声明数据需求，视图可向上组合至根节点发起请求。`useView` 用于从缓存读取数据，`useRequest` 用于声明屏幕级数据需求，`useListView` 支持连接式列表分页。
- 🔄 **请求与缓存**：支持 `cache-first`、`stale-while-revalidate`、`network-only` 三种请求模式。缓存通过 `__typename` 和 `id` 进行规范化存储，并设有释放缓冲区以优化路由切换性能。
- ⚡️ **操作与变更**：推荐使用 `fate.actions` 与 `useActionState` 集成 React Actions，支持乐观更新、新对象插入、删除记录及错误分类处理。`fate.mutations` 则用于命令式调用。
- 🌐 **实时视图**：`useLiveView` 和 `useLiveListView` 通过 SSE 保持数据实时更新，仅重渲染受影响的字段。服务端通过 `live.update` 和 `live.connection` 发送变更事件。
- 🔌 **服务器集成**：支持原生 fate 协议、tRPC 适配器和 GraphQL 传输。提供 Prisma 和 Drizzle 数据库适配器，通过 `dataView` 定义服务端数据视图，并支持计算字段与授权逻辑。
- 🛠 **开发体验**：提供 Vite 插件自动连接客户端与服务端类型，支持 GraphQL 映射，并内置模板快速启动项目。

---

### [Tailwind CSS v4.3：滚动条、新颜色及更多功能 - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-3)

**原文标题**: [Tailwind CSS v4.3: Scrollbars, new colors, and more - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-3)

Tailwind CSS v4.3 和 v4.2 版本带来了大量新功能和改进，包括新调色板、性能优化、实用工具和 CSS 功能支持。

- 🎨 新增四种中性调色板：mauve、olive、mist 和 taupe，为设计提供更多个性选择
- ⚡ 推出专为 webpack 优化的 @tailwindcss/webpack 加载器，构建速度提升超过 2 倍
- 📐 新增逻辑属性工具：支持 block-start/end 边距、内联/块尺寸和逻辑定位
- 🔤 新增 font-features-* 工具，可直接控制 OpenType 字体特性
- 🖱️ 新增滚动条样式工具：scrollbar-auto/thin/none 和颜色自定义
- 📦 新增 @container-size 工具，支持基于块尺寸的容器查询
- 🔍 新增 zoom-* 工具，支持 CSS zoom 属性（所有浏览器已支持）
- 📝 新增 tab-* 工具，控制制表符渲染宽度
- 🔗 增强 @variant 支持：堆叠变体和复合变体
- ⚙️ 函数式工具支持默认值，简化自定义工具 API 设计

---

### [v1.5.0 · 基础用户界面](https://base-ui.com/react/overview/releases/v1-5-0)

**原文标题**: [v1.5.0 · Base UI](https://base-ui.com/react/overview/releases/v1-5-0)

v1.5.0 版本发布，包含多项性能优化和组件修复。

- 🚀 提升挂载性能，关闭弹窗挂载性能提升50%，卸载性能提升85%
- 🖥️ 修复macOS Safari和Firefox关闭弹窗时全屏最小化问题
- 🔧 移除不必要的记忆化，优化代码效率
- 📋 Alert Dialog修复默认处理逻辑
- ✅ Checkbox支持回车提交关联表单
- 📂 Combobox修复多种输入场景问题，包括RTL支持
- 🔲 Dialog和Drawer改进状态检测和样式传递
- 📝 Field和Form避免验证时的flushSync
- 🎯 Menu修复子菜单指针事件和作用域支持
- 🔢 Number Field支持波斯数字输入和粘贴同步
- 🔑 OTP Field重大变更：重命名sanitizeValue为normalizeValue，支持快捷键
- 📌 Popover和Preview Card修复RTL和状态检测
- 📜 Scroll Area修复RTL行为
- 📋 Select修复多项交互问题，包括嵌套选择
- 📑 Tabs修复自动选择时的值变化触发
- 🔔 Toast移除本地实现，修复拖拽状态
- 💡 Tooltip修复嵌套闪烁和状态检测

---

### [几分钟内为你的AI-SDK代理添加技能 | Bluebag博客](https://www.bluebag.ai/blog/add-skills-to-your-ai-sdk-agent-in-minutes)

**原文标题**: [Add Skills to Your AI-SDK Agent in Minutes | Bluebag Blog](https://www.bluebag.ai/blog/add-skills-to-your-ai-sdk-agent-in-minutes)

Bluebag 讓你能在幾分鐘內為 Vercel AI SDK 代理添加技能，無需自行管理基礎設施。它解決了代理從「示範」到「生產」的關鍵痛點：執行腳本、管理依賴、處理文件儲存與下載。透過兩行程式碼整合，你的代理就能獲得沙盒 VM、按需技能發現、文件下載連結等生產級能力，讓你專注於業務邏輯與用戶體驗。

- 🚀 **兩行整合，立即賦能**：只需 `bluebag.enhance()` 與 `streamText()` 兩行程式碼，你的 AI SDK 代理就能獲得執行技能的能力，無需 Kubernetes 或 Docker。
- 🛡️ **免管理沙盒 VM**：代理在自動配置的隔離 VM 中執行，無需操心資源配置、依賴安裝、狀態保持與清理，VM 會自動恢復與終止。
- 📚 **漸進式技能發現**：代理先接收輕量級技能索引，需要時再讀取完整文檔，最後才執行腳本，有效節省 Token 與上下文空間。
- 🔗 **一鍵生成下載連結**：代理可呼叫 `bluebag_file_download_url` 工具，為 VM 內的輸出檔案生成有時效的簽名下載連結，用戶可直接點擊下載。
- 👥 **內建多租戶隔離**：透過 `stableId` 參數，自動為不同用戶隔離沙盒環境、檔案與會話狀態，確保資料安全。
- 🎯 **結構化技能，預測性高**：每個技能都包含經過測試的腳本、清晰文檔與定義好的輸出，讓代理的行為更可預測，輸出更一致。
- ⚡ **快速上手**：只需安裝 `@bluebag/ai-sdk` 與 `ai` 套件，初始化 Bluebag 並呼叫 `enhance`，即可在任何支援 AI SDK 的環境（如 Next.js、Express）中運行。

---

### [React 文件夹结构最佳实践 [2026] - Robin Wieruch](https://www.robinwieruch.de/react-folder-structure/)

**原文标题**: [React Folder Structure Best Practices [2026] - Robin Wieruch](https://www.robinwieruch.de/react-folder-structure/)

### 概述总结
本文详细介绍了React项目从单文件到多应用（Monorepo）的文件夹结构最佳实践，提供了一套可逐步扩展的架构指南。

- 📂 **从单文件起步**：小型项目可从单个`App`组件开始，随着复杂度增加自然拆分，避免过早优化。
- 📁 **多文件拆分**：将紧密耦合的组件（如`List`和`ListItem`）保留在同一文件中，仅将可复用组件独立为文件。
- 🗂️ **组件文件夹化**：为每个组件创建独立文件夹（含`component.js`、`test.js`、`style.css`），使用`index.js`作为公共API，但需注意避免过度使用barrel文件。
- 🔧 **技术文件夹分层**：引入`components/`、`hooks/`、`context/`、`utils/`等技术文件夹，将可复用逻辑与组件解耦。
- 🎯 **功能文件夹（Feature Folders）**：将业务相关组件放入`features/`文件夹，仅保留通用UI组件在`components/`中，实现功能内聚。
- 🚫 **边界规则**：代码单向流动（共享层→功能层→页面），功能间不直接相互导入，每个功能通过`index.js`暴露公共API。
- 🏢 **领域文件夹（Domain Folders）**：当功能过多时，按业务领域（如`workspace/`、`core/`）分组，进一步降低导航复杂度。
- 📦 **包文件夹（Packages）**：将共享代码提取为独立包（如`packages/shared/`），通过包名导入，强化边界。
- 🏗️ **多应用架构（Monorepo）**：引入`apps/`和`domains/`，实现多个独立应用共享领域逻辑和工具包，依赖规则清晰。
- 📄 **页面驱动结构**：在Next.js等框架中，页面文件夹（`app/`）与功能文件夹配合，实现路由与业务逻辑的分离。
- 🔍 **功能内部细节**：生产级功能包含`queries/`、`actions/`、`components/`等子文件夹，通过`relations/`处理跨功能耦合。
- 💡 **灵活演进**：所有结构均为指导而非规则，应根据项目规模自然演化，避免过度设计。

---

### [React中的无障碍性：常见错误及修复方法 - Certificates.dev](https://certificates.dev/blog/accessibility-in-react-common-mistakes-and-how-to-fix-them)

**原文标题**: [Accessibility in React: Common Mistakes and How to Fix Them - Certificates.dev](https://certificates.dev/blog/accessibility-in-react-common-mistakes-and-how-to-fix-them)

本次线上活动聚焦React应用中的可访问性常见错误及修复方法，涵盖语义化标签、焦点管理、标签标注和动态更新通知等关键点。

- 🎯 **使用正确的HTML元素**：用`<button>`和`<a>`替代`<div onClick>`，避免手动实现键盘交互和屏幕阅读器支持。
- 📐 **维护文档结构与标题层级**：按逻辑顺序使用`<h1>`至`<h6>`，并利用`<nav>`、`<main>`等地标元素辅助导航。
- 🏷️ **为所有交互元素添加标签**：表单输入需关联`<label>`，图标按钮使用`aria-label`或隐藏文本，图片必须包含`alt`属性。
- 🔗 **用`useId`连接标签和错误信息**：通过`aria-describedby`和`aria-invalid`将错误信息与输入框关联，确保屏幕阅读器能读出。
- 🎯 **管理焦点**：页面切换时聚焦新内容标题，模态框使用原生`<dialog>`自动处理焦点陷阱，删除元素后需将焦点移至合理位置。
- 📢 **通知动态更新**：使用`role="alert"`（紧急）或`role="status"`（非紧急）让屏幕阅读器播报变化，并保持容器常驻DOM。
- 🎨 **基于ARIA属性进行样式设计**：利用`aria-selected`、`aria-disabled`等属性直接设置样式，减少额外状态变量。
- 🔍 **快速审计清单**：检查`<div onClick>`、标题层级、表单标签、图标按钮、图片alt、错误关联、模态框焦点、条件渲染和动态更新，并用axe-core等工具自动化检测。

---

### [五个模型，一个React栈：为何每个LLM都构建相同的应用 | Sascha Becker](https://saschb2b.com/blog/llm-default-react-stack)

**原文标题**: [Five Models, One React Stack: Why Every LLM Builds the Same App | Sascha Becker](https://saschb2b.com/blog/llm-default-react-stack)

### 概述摘要  
所有主流LLM（Claude、GPT、Gemini、DeepSeek等）在生成React应用时，都默认使用几乎相同的技术栈：Next.js或Vite、TypeScript、Tailwind CSS、shadcn/ui、TanStack Query和Zustand。这种趋同并非巧合，而是由训练数据主导、Token经济效应和编码代理工具共同驱动的结果。它带来了技术栈单一化、版本滞后永久化、新手失去选择权等问题，但也提供了通过规则文件、MCP服务器等方式引导模型偏离默认路径的解决方案。

- 📊 **技术栈高度趋同**：八种主流AI工具在React开发中几乎全部默认使用Next.js/Vite、Tailwind、shadcn/ui，差异极小，甚至包括中国实验室的DeepSeek和Qwen。
- 🧠 **Token经济学驱动**：Tailwind的原子化类名（如`flex`、`p-4`）比CSS-in-JS更利于LLM预测，因为无需命名、减少跨文件依赖，且训练数据中出现频率极高。
- 🔓 **shadcn/ui的“开放代码”优势**：组件直接复制为JSX+Tailwind类，无黑箱库依赖，LLM可直接读取和修改，且提供MCP服务器和Claude Skill实时查询项目组件。
- 🔄 **训练数据飞轮效应**：流行栈→GitHub代码增多→LLM训练更充分→开发者更依赖LLM输出→更多该栈代码→进一步强化，形成自我强化的循环。
- ⚠️ **Vue/Svelte等框架被边缘化**：即使框架本身在改进，由于训练数据中React占主导，LLM输出倾向于React模式，导致开发者体验下降，形成“可见性即采用率”的困境。
- 🕰️ **版本滞后永久化**：LLM基于历史训练数据生成代码，旧模式（如`useEffect+fetch`）比新特性（如React Compiler）更常见，且AI生成代码又成为新训练数据，滞后难以缩小。
- 🧑‍🎓 **新手失去选择权**：初学者通过AI获得默认栈，不知有其他选项存在，无法形成技术品味和选择意识，比“选错栈”更糟糕。
- 🎨 **“AI slop”审美同质化**：无设计约束时，所有AI生成UI都呈现圆角、Inter字体、灰色调、蓝色按钮的通用样式，品牌差异化需主动对抗模型。
- 🛠️ **引导模型偏离默认的5个层级**：从最脆弱的提示词指令（Level 1），到项目规则文件（CLAUDE.md等，Level 2），再到代码库示例（Level 3）、Skills/MCP服务器（Level 4），最后是ESLint等工具护栏（Level 5）。
- 💡 **实用升级路径**：对大多数团队，先写CLAUDE.md（80%效果），再手写参考组件，添加`no-restricted-imports`规则，最后在必要时使用Skills/MCP。
- 🔮 **诚实结论**：默认栈本身并非错误，但选择权已被固化。每个放弃Vue/Svelte的决定都会强化React的统治地位。保持工具多样性需要主动投入，否则将导致同质化的网络未来。

---

### [从延迟到即时：现代化GitHub Issues导航性能 - GitHub博客](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

**原文标题**: [From latency to instant: Modernizing GitHub Issues navigation performance - The GitHub Blog](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

GitHub Issues 团队通过客户端缓存、智能预取和服务工作者技术，将导航延迟从秒级降至瞬间，显著提升了用户体验。

- 📉 **性能基准**：将HPC（最高优先级内容）指标分为“瞬间”（<200ms）、“快速”（<1000ms）和“慢速”（>=1000ms），并聚焦于提升整体分布质量而非仅优化尾部。
- 🗂️ **IndexedDB缓存**：为React软导航构建持久化客户端缓存，采用“stale-while-revalidate”策略，使约22%的React导航变为瞬间（从4%提升），缓存命中率约33%。
- 🔥 **预加热策略**：在用户点击前，从高意图页面（如问题列表）主动填充缓存，仅当数据缺失时才发起网络请求，将缓存命中率提升至约96%，React导航瞬间率升至约70%。
- ⚙️ **Service Worker优化**：拦截硬导航和Turbo导航请求，利用缓存数据让服务器跳过渲染，返回轻量HTML壳，由客户端React渲染，显著减少服务器响应时间。
- 📊 **实际效果**：HPC指标全面改善，P10从600ms降至70ms，P25从800ms降至120ms，P50从1200ms降至700ms，P75和P90也分别下降400ms和300ms。
- 🚧 **未来方向**：继续优化冷启动路径，计划重写后端堆栈以支持低延迟交付，并投资边缘UI交付层，目标是让“快速”成为所有导航路径的默认体验。

---

