### [<Suspense> – React](https://react.dev/reference/react/Suspense#what-activates-a-suspense-boundary)

**原文标题**: [<Suspense> – React](https://react.dev/reference/react/Suspense#what-activates-a-suspense-boundary)

<Suspense> 组件允许你在子组件加载完成前显示后备内容，通过包裹需要异步加载的内容并指定 fallback 来实现。

- ⏳ 当子组件因 lazy 加载、use 读取 Promise 或流式渲染而挂起时，Suspense 边界会显示 fallback 占位内容。
- 🎯 默认情况下，同一 Suspense 边界内的所有子组件会作为一个整体同时显示，不会逐个弹出。
- 🔄 通过嵌套多个 Suspense 边界，可以创建渐进式加载序列，让不同层级的内容按顺序显示。
- 📄 使用 useDeferredValue 或 startTransition 可以避免已显示内容被 fallback 替换，保持用户体验流畅。
- 🚦 useTransition 提供 isPending 状态，用于在过渡期间显示加载指示器（如改变标题样式）。
- 🔑 在导航到不同内容时，使用 key 属性重置 Suspense 边界，确保显示新内容的 fallback 而非旧内容。
- 🛡️ 流式服务器渲染中，Suspense 边界可处理服务器错误，显示 fallback 并在客户端重试渲染。
- 🎨 与 <ViewTransition> 结合使用时，Suspense 边界会等待字体、图片和样式表加载完成后再显示内容，避免闪烁。
- ⚙️ Suspense 不会检测 Effect 或事件处理器中的数据获取，仅对特定情况（如 lazy、use、流式渲染）生效。

---

### [一个功能完备的 TypeScript 存储 SDK——跨不同提供商的统一便携接口](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-07-18)

**原文标题**: [A fully-featured TypeScript SDK for storage — one portable interface across different providers](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-07-18)

这是一个统一的 TypeScript 存储 SDK，支持快照和分支，可在多个存储提供商之间切换。

- 🔄 **统一 API**：在所有提供商（Tigris、S3、R2、GCS、Azure 等）上使用相同的 API，只需更改导入即可切换提供商。
- 📸 **快照与分支**：内置快照和分支功能，支持冻结状态、创建沙盒环境，并在完成后合并或丢弃分支。
- 🤖 **AI 集成**：可直接与 Vercel AI SDK、Mastra 或 MCP 服务器集成，让模型自动进行快照和分支操作。
- 🖥️ **CLI 工具**：通过 `@storagesdk/cli` 在命令行中使用熟悉的 `ls`、`cp`、`mv` 等命令，支持 `storage://` 协议。
- 🌊 **流式传输**：支持 Web 流（`ReadableStream<Uint8Array>`）的上传和下载，背压和中断端到端传播。
- 🔗 **签名 URL**：支持预签名 PUT 和 POST，可设置 `maxSize` / `contentType` 限制。
- 🛠️ **逃生口**：通过 `storage.raw` 访问原生客户端，支持提供商特定功能，类型安全。
- 🚫 **中止信号**：每个操作支持 `AbortSignal`，可取消上传、列表扫描和快照。
- ❌ **类型化错误**：使用 `StorageError` 代码（如 `NotFound`、`Conflict`、`Aborted`）保持可移植性。
- 📦 **轻量级**：ESM 仅限，Node 20+，核心零运行时依赖，适配器作为可选对等依赖。
- 🌟 **开源**：Apache 2.0 许可，由 Tigris 团队构建，适用于所有人。

---

### [我让 React 编译器处理记忆化：实际出问题的地方 - LogRocket 博客](https://blog.logrocket.com/react-compiler-memoization-what-actually-broke/)

**原文标题**: [I let React Compiler handle memoization: Here's what actually broke - LogRocket Blog](https://blog.logrocket.com/react-compiler-memoization-what-actually-broke/)

本文记录了作者在生产环境的 Next.js 应用中启用 React 编译器（v1.0）的实际迁移经验，重点揭示了编译器并非一键式解决方案，而是会暴露隐藏的 bug 和兼容性问题。

- 🧠 **编译器原理**：React 编译器是一个 Babel 插件，自动为组件应用细粒度的 memoization，但要求代码严格遵循 React 规则，否则会暴露 bug 或静默跳过优化。
- ⚠️ **迁移前准备**：必须先安装并启用 ESLint 规则（如 `eslint-plugin-react-hooks` v7+），将 `unsupported-syntax` 等规则设为 error，在启用编译器前修复大部分问题。
- 🔥 **关键故障 1：表单预览冻结**：React Hook Form 的 `watch()` 函数因内部可变性与编译器不兼容，导致实时预览停止更新。需使用 `"use no memo"` 指令包裹该函数以绕过编译器优化。
- 🕰️ **关键故障 2：图表回调数据陈旧**：移除 `useCallback` 后，Chart.js 的点击处理函数出现引用旧数据的问题。编译器暴露了 `useEffect` 注册时机与数据更新的时序 bug，最终需保留 `useCallback` 并添加注释说明。
- 🏷️ **DevTools 徽章误导**：Memo ✨ 徽章仅表示编译器“处理”了组件，不代表优化成功或组件无违规。例如，直接修改 props 的组件仍有徽章，而使用了 `"use no memo"` 的组件则没有。
- ✅ **删除 useMemo/useCallback 的决策指南**：大部分场景可删除，但需保留的情况包括：依赖函数标识的第三方库（如图表库）、直接操作 DOM API 或外部 SDK、以及经性能分析确认的昂贵计算。每个保留的 hook 都应有明确注释说明原因。
- 📋 **迁移检查清单**：按顺序执行：升级 ESLint 规则 → 在功能分支启用 → 锁定编译器版本 → 不依赖徽章 → 审计含内部可变性的库 → 运行 E2E 测试 → 定期审查 `"use no memo"` 指令。

---

### [水合不匹配的隐性成本·PerfPerfPerf](https://3perf.com/blog/hydration-mismatch/)

**原文标题**: [Hidden Cost of Hydration Mismatches · PerfPerfPerf](https://3perf.com/blog/hydration-mismatch/)

### 概述总结
React 应用中的水合不匹配问题会严重拖慢 Largest Contentful Paint (LCP) 性能，从绿色直接降至红色。理解这一现象需要结合三个关键事实：水合不匹配导致 DOM 重建、字体加载引发文本尺寸变化、以及 LCP 仅测量新 DOM 节点。通过避免水合不匹配或使用 `<Suspense>` 包裹问题元素，可有效解决该问题。

- 🔍 **水合不匹配强制重建 DOM**：当客户端与服务器渲染的 DOM 不同时，React 会从最近的 `<Suspense>` 边界开始重新挂载整个 DOM，若无边界则重建整个页面。
- 📏 **字体加载导致文本尺寸变化**：使用 `font-display: swap` 时，网页字体加载后文本尺寸会改变（如变宽或变窄），但浏览器忽略现有元素的尺寸变化。
- ⏱️ **LCP 仅测量新 DOM 节点**：LCP 只记录新添加到 DOM 中的元素尺寸，忽略现有元素的尺寸变化，因此重建 DOM 会触发新的 LCP 测量。
- 💥 **组合效应导致 LCP 延迟**：水合不匹配重建 DOM 后，字体加载使文本变大，浏览器误认为这是新元素，导致 LCP 时间推迟到水合完成（通常 5 秒以上），性能从绿色跌至红色。
- 🛠️ **解决方案**：避免水合不匹配；若无法避免，用 `<Suspense>` 包裹问题元素，限制 DOM 重建范围，防止 LCP 元素被影响。

---

### [使用 Vercel 的 Aurora Scharff 实现异步 React - YouTube](https://www.youtube.com/watch?v=tFZjRdDnxzc)

**原文标题**: [Async React with Vercel's Aurora Scharff - YouTube](https://www.youtube.com/watch?v=tFZjRdDnxzc)

Google LLC 的資訊頁面概述了其服務條款、版權政策、隱私保護及聯絡方式等核心內容。

- 📰 **新聞中心**：提供 Google 最新消息與動態。
- ©️ **版權**：說明內容使用與版權相關規範。
- 📞 **聯絡我們**：提供用戶與 Google 聯繫的管道。
- 🎨 **創作者**：針對內容創作者提供的資源與指南。
- 📢 **刊登廣告**：說明在 YouTube 投放廣告的選項。
- 👨‍💻 **開發人員**：為開發者提供的技術文件與工具。
- 📜 **條款**：使用 YouTube 服務時需遵守的條款與細則。
- 🔒 **私隱**：說明 Google 如何收集與處理用戶資料。
- 🛡️ **政策及安全**：平台的安全規範與內容審核政策。
- ⚙️ **YouTube 的運作方式**：解釋推薦系統與平台功能。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能。
- 📅 **© 2026 Google LLC**：版權聲明與年份。

---

### [GitHub - QuadDepo/env.style · GitHub](https://github.com/QuadDepo/env.style)

**原文标题**: [GitHub - QuadDepo/env.style · GitHub](https://github.com/QuadDepo/env.style)

env.style 是一个开源工具，能在构建时为不同环境（如开发、预览、生产）自动给现有网站图标（favicon）添加不同颜色，帮助开发者避免混淆环境。它采用 Vercel 风格，生产环境图标保持不变。项目使用 TypeScript 编写，支持 Next.js 和 Vite 框架，已获得 192 个星标和 3 个复刻。

- 🎨 自动为不同环境（开发、预览、生产）的网站图标添加不同颜色，避免混淆
- 🚀 支持 Next.js 和 Vite 框架，通过简单配置即可集成
- 🔧 构建时处理，生产环境图标不受影响
- 📦 使用 pnpm 管理依赖，包含示例和开发指南
- ⭐ 开源项目，MIT 许可证，拥有 192 个星标和 3 个复刻
- 🛠️ 主要使用 TypeScript（98.8%），少量 CSS 和 JavaScript

---

### [GitHub - cloudflare/vinext: 重新实现 Next.js API 接口的 Vite 插件——可部署至任何环境 · GitHub](https://github.com/cloudflare/vinext)

**原文标题**: [GitHub - cloudflare/vinext: Vite plugin that reimplements the Next.js API surface — deploy anywhere · GitHub](https://github.com/cloudflare/vinext)

概述：vinext 是一个 Vite 插件，重新实现了 Next.js 的 API 接口，支持在 Vite 上运行 Next.js 应用，并以 Cloudflare Workers 为主要部署目标，兼容 App Router 和 Pages Router。

- 🚀 **核心功能**：支持 App Router、Pages Router、React Server Components、Server Actions、中间件、路由处理器、ISR、静态导出和常用 next/*模块
- ☁️ **部署目标**：原生支持 Cloudflare Workers 部署，通过 Nitro 插件可部署到 Vercel、Netlify、AWS、Deno Deploy 等平台
- ⚡ **性能优势**：相比 Next.js/Turbopack，生产构建更快，客户端包体积更小（通过更积极的树摇和更轻量的框架运行时）
- 🔧 **迁移工具**：提供`vinext init`一键迁移命令和`vinext check`兼容性扫描，支持 AI 代理辅助迁移
- 📊 **API 覆盖**：约 94% 的 Next.js 16 API 表面已实现，包括 next/link、next/image、next/navigation 等核心模块
- 🧪 **测试体系**：超过 1700 个 Vitest 单元测试和 380 个 Playwright E2E 测试，包含从 Next.js 测试套件移植的测试
- 🏗️ **架构特点**：作为 Vite 插件工作，解析 next/*导入到本地 shim 模块，扫描 pages/和 app/目录构建文件系统路由，生成虚拟入口模块
- 🎯 **设计原则**：部署无关性、实用兼容性（非 bug-for-bug 一致）、仅支持最新 Next.js 16.x、渐进式采用
- ⚠️ **已知限制**：缓存组件和部分预渲染不完整，构建时图片和字体优化缺失，原生模块在 App Router 开发中可能失败
- 📚 **快速开始**：使用`pnpm create vinext-app@latest my-app`创建新项目，或`npx vinext init`迁移现有项目

---

### [2026 年 7 月 - Base UI 成为默认 - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)

**原文标题**: [July 2026 - Base UI as the Default - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)

shadcn/ui 宣布默认组件库从 Radix 切换为 Base UI，但 Radix 仍受支持且无需迁移。新项目默认使用 Base UI，并提供迁移技能以逐步过渡。

- 🚀 **Base UI 成为默认**：新项目运行 `npx shadcn init` 时，Base UI 为默认选择，Radix 可通过 `-b radix` 参数指定。
- 🔄 **Radix 仍受支持**：Radix 不会被弃用，所有更新和新组件会同时支持两个库，除非某组件仅存在于 Base UI。
- ✅ **无需迁移**：现有项目无需迁移，Radix 是成熟库，可继续使用；新项目建议使用 Base UI。
- 🛠️ **迁移技能可用**：通过 `pnpm dlx skills add shadcn/ui` 添加技能，可逐步迁移单个组件，支持与编码代理协作。
- 📝 **迁移产出清晰**：每次迁移生成工作代码、组件报告（位于 `.migration/`）和干净 Git 历史，便于回滚和验证。
- 🧠 **技能优于代码转换**：技能能处理自定义变体和属性，保留用户修改，而非机械替换。
- 📊 **社区已选择**：新项目中 Base UI 与 Radix 的使用比例为 2:1，社区已做出决定。

---

### [Typeset - shadcn/ui](https://ui.shadcn.com/typeset)

**原文标题**: [Typeset - shadcn/ui](https://ui.shadcn.com/typeset)

本摘要概述了文章的核心内容，通过简洁的要点提炼关键信息。

- 📝 文章主要讨论了如何高效总结内容，强调使用简洁的要点形式。
- 🎯 每个要点需以“-”符号开头，并搭配一个合适的表情符号。
- 🔑 要点应涵盖关键信息和核心内容，确保抓住文章精髓。
- 🌟 在要点列表前，需添加一个无标题的概述总结，概括文章主题。

---

### [世博会观察](https://expo.dev/solutions/expo-observe?utm_source=nextjsweekly&utm_medium=email&utm_campaign=observe-beta)

**原文标题**: [Expo Observe](https://expo.dev/solutions/expo-observe?utm_source=nextjsweekly&utm_medium=email&utm_campaign=observe-beta)

本页面介绍了 EAS Observe 服务，它将性能指标与每次构建和更新直接关联，帮助开发者快速定位问题。

- 📊 **即时洞察每次发布影响**：Observe 将每个性能指标与具体的构建和更新绑定，能在几分钟内发现回归问题，而非数天。
- ⏱️ **自动测量用户真实体验**：自动捕获 TTI、冷/热启动、帧率下降等指标，无需自定义追踪。
- 🏷️ **可视化每次构建**：每次发布在时间线上显示为标记，悬停查看变化，点击查看该构建的所有事件。
- 🤖 **一键交接给 AI**：通过仪表盘或 CLI 将数据导入 AI 代理（如 Claude Code），获取真实会话的答案。
- 🔍 **精准定位问题用户**：按最慢指标排序，深入单个会话，查看设备、系统版本、国家等信息，追踪完整事件时间线。
- 📋 **AI 获取完整上下文**：Observe 预览发送给 AI 的提示，包含指标、受影响会话、构建和回归变化，无需手动复制。
- 🚀 **监控每次发布表现**：每次构建和 OTA 更新在性能时间线上显示为标记，EAS 更新标签页显示下载和应用时间，防止误判。
- 🗺️ **识别慢速屏幕**：通过 Expo Router 集成，按路由分解交互时间，多选路线直接比较。
- 📈 **覆盖全范围性能**：P50、P90、P99 统计自动捕获所有设备、系统版本和网络条件。
- ❓ **常见问题解答**：Observe 与 Sentry/Datadog 互补，支持采样率设置，仅适用于 Expo SDK 55+ 和 EAS，不收集个人身份信息。

---

### [无法维护 — React 组件 API 游戏](https://cant-maintain.saschb2b.com/)

**原文标题**: [Can't Maintain — React Component API Game](https://cant-maintain.saschb2b.com/)

以下是对所提供内容的总结摘要：

- 🎯 通过 10 个代码挑战，训练识别更优组件 API 的能力，无需注册，仅需 3 分钟
- 📝 对比两种 API 设计：使用`data`/`active`/`click`（较差）与`user`/`isActive`/`onClick`（更优）
- 🧠 学习回调命名、布尔属性、属性特异性等模式，每个模式都展示正反两面及其重要性
- 🛠️ 基于 React、MUI 及生产代码库的真实惯例进行实践训练
- 🔗 该系列还涵盖其他主题，如响应式设计（Can't Resize）、TypeScript 模式（Can't Type）、容器编排（Can't Orchestrate）等
- 🌐 开源且社区驱动，欢迎贡献新挑战、类别和改进

---

### [逆向工程 ChatGPT 网页版：OpenAI 如何为十亿用户构建](https://performance.dev/chatgpt)

**原文标题**: [Reverse Engineering ChatGPT Web:
How OpenAI Built for a Billion Users](https://performance.dev/chatgpt)

概述总结  
- 🏗️ ChatGPT 网页应用采用 React Router 7 框架模式，实现服务端流式渲染，首字节时间仅 50-65ms。  
- 🚀 从 Next.js Pages Router 迁移至 Remix 再到 React Router，最终实现完整的服务端渲染，登录用户和匿名用户均获得极速体验。  
- 🎨 使用 Tailwind CSS 配合语义化设计令牌，按路由拆分样式文件，无网页字体加载，性能优先。  
- 🧩 大量采用 Radix UI、ProseMirror、CodeMirror 等开源组件，避免重复造轮子，保持代码简洁。  
- ⚡ 所有决策围绕“让用户尽快开始输入”这一核心目标，通过延迟非关键加载、预取数据、服务端评估特性标志等方式优化。  
- 🔒 匿名用户无需登录即可使用，背后通过 Cloudflare 工作量证明、Sentinel 反滥用系统、预检查机制实现安全防护。  
- 📊 内置 556 个特性标志和 192 个实验层，服务端评估后内联到 HTML 中，支持大规模 A/B 测试和功能发布。  
- 📝 答案渲染采用流式 SSE，每个 token 实时解析 Markdown 并渲染，代码块使用 CodeMirror，数学公式使用 KaTeX。  
- 🌐 所有资源从 chatgpt.com/cdn/assets 自托管，无第三方 CDN，减少 DNS 查询和 TLS 握手。  
- 🎯 与 Claude 的对比显示，ChatGPT 选择面向消费者，牺牲复杂性换取零摩擦体验；Claude 面向企业，采用客户端渲染和登录墙。

---

### [Vercel 与 Shopify 正在重构 Hydrogen](https://vercel.com/blog/vercel-and-shopify-are-rebuilding-hydrogen)

**原文标题**: [Vercel and Shopify are rebuilding Hydrogen - Vercel](https://vercel.com/blog/vercel-and-shopify-are-rebuilding-hydrogen)

### 概述总结
Shopify 与 Vercel 合作重构了 Hydrogen，使其成为开源、运行时无关的框架，可在任何支持 JavaScript 的环境运行。新版本通过三层架构（核心、客户端、服务器）简化了 Shopify 开发，提供可复用组件、最佳实践和框架集成指导，并计划将 vercel.shop 的经验融入其中。

- 🔧 **核心层统一**：将原本分散的 Shopify API 绑定代码集中管理，例如 `formatMoney` 函数，开发者无需再编写和维护胶水代码，API 升级更简单。
- 🛒 **客户端层简化**：购物车状态管理作为单一导入提供，开发者无需重复编写自定义代码，即可获得最佳实践和跨标签同步等功能。
- 🌐 **服务器层开放**：与 Next.js、Nuxt、SvelteKit 等全栈框架集成，提供类型安全客户端和缓存指导，无需锁定专有运行时。
- 📘 **文档与技能**：提供详细文档、模板和技能（如 i18n 国际化），指导开发者和 AI 代理正确使用框架功能，避免重复造轮子。
- 🏗️ **vercel.shop 融合**：将 vercel.shop 模板的实践经验整合到 Hydrogen 客户端和服务器层，使其成为 Hydrogen 与 Next.js 的参考实现。
- 🚀 **开放开发**：项目在 GitHub 上开源，开发者可试用、复刻并参与塑造未来，目标是提供最佳开发者体验且无平台锁定。

---

### [当 React Hooks 不再扩展：将复杂状态迁移至 Zustand - Oren Farhi](https://orizens.com/blog/2026-06-18-zustand/)

**原文标题**: [When React Hooks Stop Scaling: Moving Complex State to Zustand - Oren Farhi](https://orizens.com/blog/2026-06-18-zustand/)

### 概述摘要
本文讨论了在 React 应用中，当自定义 Hook 的复杂性和共享需求超出其设计范围时，如何通过将状态迁移到 Zustand 来简化架构。

- 🐛 **Bug 暴露问题**：用户遇到陈旧转录数据，根源是多个组件依赖同一状态，但状态仍隐藏在最初为单一 UI 流设计的 Hook 中。
- 📦 **Hook 过度膨胀**：Hook 从封装 UI 逻辑演变为管理应用共享状态，承担了生命周期、事件处理、数据同步等多重责任。
- ❌ **Context 不够用**：React Context 无法处理来自浏览器 API 等外部源的状态更新，且无法独立于组件树进行更新。
- 🚀 **迁移到 Zustand**：将状态移至 Zustand 存储，服务直接更新 store，组件按需订阅，消除状态所有权歧义。
- ✅ **核心改进**：不再需要追问“哪个组件拥有状态？”或“为何更新不可见？”，单一数据源使数据流清晰可追踪。
- 🔄 **保留 Hook 场景**：组件私有状态或封装 UI 行为时仍用 useState 和自定义 Hook，但跨组件共享且外部更新的状态视为应用状态。
- 💡 **架构启示**：问题不在于原始 Hook，而在于需求变化后未及时调整抽象层次。迁移未减少复杂度，而是使其显性化并赋予合理位置。

---

