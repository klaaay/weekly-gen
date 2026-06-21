### [Vercel Ship 2026 回顾 - Vercel](https://vercel.com/blog/vercel-ship-2026-recap)

**原文标题**: [Vercel Ship 2026 recap - Vercel](https://vercel.com/blog/vercel-ship-2026-recap)

Vercel 在伦敦 Ship 2026 大会上发布了面向 AI 代理时代的基础设施平台，涵盖从开发、部署到企业级安全的全栈能力。

- 🤖 **代理基础设施三要素**：Vercel 成为编码代理部署软件的首选平台；提供构建和运行自主代理的全套工具；自身也由代理自动化运维，能自主调查异常并提交修复 PR。

- 🧩 **代理栈完整发布**：包含 AI SDK（统一模型调用）、AI Gateway（智能路由与故障转移）、Workflow SDK（持久化执行）、Sandbox（隔离测试环境）、Chat SDK（多平台部署）五大核心组件。

- 🔗 **Vercel Connect 安全连接**：新推出的代理连接方案，通过临时凭证替代长期存储的 API 密钥，为每个任务提供最小权限的临时访问令牌。

- 🏗️ **eve 开源框架**：Vercel 内部代理架构的标准化开源版本，支持单目录开发、Markdown 指令、TypeScript 工具、持久执行、沙箱计算和审批流程。

- 🌐 **全栈应用支持扩展**：新增 FastAPI、Flask 等后端框架支持；推出 Vercel Services 微服务架构（7 月 1 日上线）；集成 Amazon Aurora、DynamoDB 等数据库。

- 🔒 **企业级安全方案**：Enterprise Managed Users（私有测试）、Vercel Passport（内部应用私有化）、BYOC on AWS（私有测试）三大功能，满足企业身份、访问和治理需求。

- 🕵️ **Vercel Agent 智能运维**：基于 eve 构建的智能层（私有测试），采用首创的"计划 + 权限"安全模型，能自主监控生产环境、调查告警并生成修复 PR。

- 🎉 **伦敦活动亮点**：200 人黑客松（获奖项目 Stella、Oscar、Phone Jail）、400 人 Builder Night、行业领袖圆桌讨论（Anthropic、Currys、Auth0 等），以及 AI Social Club 等社区活动。

---

### [React 服务器组件如何与打包器集成 | reactjs maxxing](https://reactjs-maxxing.vercel.app/blog/how-react-server-component-integrate-with-bundler)

**原文标题**: [How React Server Components Integrate with Bundler | reactjs maxxing](https://reactjs-maxxing.vercel.app/blog/how-react-server-component-integrate-with-bundler)

### 概述总结
本文深入探讨了 React 服务器组件（RSC）在构建时如何通过打包工具将服务器端和客户端代码分离，重点介绍了 Flight 协议、条件导出、服务器构建与客户端构建的差异。

- 🛠️ **Flight 协议**：RSC 使用自定义的 Flight 流协议（非纯 JSON），支持异步边界和服务器端计算，可增量解析流式数据。
- 🔄 **条件导出**：React 根据`react-server`条件为服务器和客户端提供不同运行时，服务器版本不支持 hooks 等客户端特性。
- 🏗️ **服务器构建**：遇到客户端组件（如`Counter`）时，打包工具将其替换为`registerClientReference`存根，仅注册组件标识，不渲染实际代码。
- 🌐 **客户端构建**：客户端打包时正常编译客户端组件，生成连接服务器引用的清单（manifest），映射 Flight 流中的`$L1`引用到实际模块。
- 📦 **集成机制**：`react-server-dom-webpack`包负责将 Flight 协议与 webpack 集成，提供服务器端`renderToPipeableStream`和客户端`createFromFetch`。
- 💡 **未来方向**：文章提及 SSR（服务器端渲染）和服务器操作（Server Actions）将作为后续主题。

---

### [一个功能完备的 TypeScript 存储 SDK——跨不同提供商的统一便携接口](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-06-19)

**原文标题**: [A fully-featured TypeScript SDK for storage — one portable interface across different providers](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-06-19)

这是一个统一的 TypeScript SDK，支持多种存储提供商，具备快照、分支和 AI 集成等高级功能。

- 🔄 **统一 API**：跨所有提供商使用相同 API，只需更改导入即可切换后端，动词命名直观易懂。
- 📸 **快照与分支**：内置快照和分支功能，支持为代理创建沙盒环境，可合并或丢弃分支，确保每次运行可复现。
- 🤖 **AI 集成**：可直接集成到 Vercel AI SDK、Mastra 或 MCP 服务器，让模型在编辑前自动快照，尝试变体时自动分支。
- 🖥️ **命令行工具**：`@storagesdk/cli` 提供熟悉的 shell 命令（如 ls、cp、mv），支持 `storage://` 协议和适配器切换。
- 🌊 **流式传输**：支持 Web 流（ReadableStream）的上传和下载，背压和中断端到端传播。
- 🔗 **签名 URL**：默认提供预签名 PUT URL，也可根据提供商限制使用 POST 方式。
- 🛠️ **逃生舱**：通过 `storage.raw` 直接访问原生客户端，类型完全推断，无需强制转换。
- ⏹️ **取消操作**：每个操作支持 AbortSignal，可取消上传、列表扫描和快照等任务。
- ❌ **错误处理**：使用类型化的 StorageError 代码（如 NotFound、Conflict），跨适配器保持可移植性。
- 📦 **轻量设计**：ESM 仅限，Node 20+，核心零运行时依赖，适配器作为可选对等依赖。

---

### [文档：添加《Next.js 思维指南》由 aurorascharff 提交 · 拉取请求 #93442 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/93442)

**原文标题**: [docs: add Thinking in Next.js guide by aurorascharff · Pull Request #93442 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/93442)

该 Pull Request 为 Next.js 文档新增了一份名为“Thinking in Next.js”的指南，通过构建一个小型项目仪表盘，帮助读者建立关于 App Router 应用的心智模型。

- 📖 **新增指南**：一份名为“Thinking in Next.js”的 MDX 指南，逐步引导读者构建一个 Vercel 风格的项目仪表盘。
- 🧠 **构建心智模型**：帮助读者理解 App Router 应用中的组件如何决定数据来源、复用内容以及浏览器端行为。
- 📝 **八步决策**：指南涵盖每个组件需要回答的八个关键决策：层次结构、静态 JSX、数据获取、流式传输、变更、客户端交互、缓存和预取。
- 🛠️ **配套可运行应用**：每个步骤都配有可运行的演示应用，部署在 `*.labs.vercel.dev`，并通过 `<Demo />` 组件嵌入。
- 🔗 **修复链接问题**：机器人检测到指南中存在多个损坏的链接，需要修复后才能合并。
- 👨‍💻 **协作与审查**：该 PR 由 aurorascharff 提交，Copilot 和 vercel 机器人已进行代码审查，并提出了修改意见。
- 🏷️ **标签分类**：该 PR 被标记为“created-by: Next.js DevEx team”和“Documentation”。

---

### [使用异步 React 设计中间状态 - Aurora Scharff - YouTube](https://www.youtube.com/watch?v=QljQDwAwA2Y)

**原文标题**: [Designing the In-Between States with Async React - Aurora Scharff - YouTube](https://www.youtube.com/watch?v=QljQDwAwA2Y)

本頁面提供 YouTube 平台相關的資訊與政策連結，包括版權、條款、私隱及開發者資源等。
- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明內容版權相關規範與申訴機制
- 📞 聯絡我們：提供用戶與創作者聯繫 YouTube 的方式
- 🎬 創作者：針對內容創作者提供的資源與指南
- 📢 刊登廣告：介紹在 YouTube 上投放廣告的選項
- 💻 開發人員：提供 API 與技術整合資源
- 📜 條款：列出使用 YouTube 服務的條款與條件
- 🔒 私隱：說明用戶資料收集與使用方式
- 🛡️ 政策及安全：涵蓋內容政策與平台安全規範
- ⚙️ YouTube 的運作方式：解釋平台推薦與內容管理機制
- 🧪 測試新功能：介紹正在實驗中的平台功能
- ©️ 2026 Google LLC：版權歸屬 Google 公司

---

### [在 Next.js 中构建活跃的导航链接组件 | Aurora Scharff](https://aurorascharff.no/posts/building-an-active-navlink-component-in-nextjs/)

**原文标题**: [Building an Active NavLink Component in Next.js | Aurora Scharff](https://aurorascharff.no/posts/building-an-active-navlink-component-in-nextjs/)

本篇文章详细介绍了如何在 Next.js App Router 中构建一个功能完善的`NavLink`组件，支持活动状态样式、渲染属性、pending 状态、前缀匹配、无障碍访问、TypeScript 类型、防止首屏闪烁以及兼容`cacheComponents`。

- 🧭 **核心思路**：基于`usePathname()`或`useSelectedLayoutSegments()`读取当前路由，与链接的`href`比较，从而决定是否应用活动样式。
- ⚙️ **渲染属性模式**：`className`和`children`支持传入函数，接收`{ isActive, isPending }`，让消费者灵活控制样式和内容。
- ⏳ **Pending 状态**：利用`useLinkStatus`在`<Link>`内部获取导航加载状态，通过`children`渲染属性暴露`isPending`。
- 🔗 **前缀匹配**：默认对`/search`等链接进行前缀匹配（如`/search?q=react`），并通过`exact`属性支持精确匹配，`/`始终精确匹配。
- ♿ **无障碍访问**：自动为活动链接添加`aria-current="page"`属性，既支持辅助技术，也便于 CSS/Tailwind 样式定位。
- 🛡️ **TypeScript 支持**：通过泛型和类型推导，确保`href`类型安全（支持`typedRoutes`），并保留`next/link`的所有原生属性。
- 💡 **防止首屏闪烁**：通过内联脚本在 HTML 解析阶段读取`location.pathname`并设置`aria-current`，确保活动样式在 React 水合前就已生效。
- 🧩 **兼容 cacheComponents**：将`Suspense`边界内置于组件中，fallback 渲染与真实链接布局一致的`<Link>`，避免布局偏移；同时导出`NavLinkSkeleton`供异步 Server Component 使用。
- 🔄 **两种路由读取方案**：`usePathname()`直接比较 URL 字符串，简单但可能因重写导致水合不匹配；`useSelectedLayoutSegments()`比较路由段，更稳定但依赖路由结构。

---

### [当 React 父组件需要了解其子组件时](https://www.jayfreestone.com/writing/updating-react-parents-in-response-to-changes-in-children/)

**原文标题**: [When React parent components need to know their children](https://www.jayfreestone.com/writing/updating-react-parents-in-response-to-changes-in-children/)

### 概述总结
当 React 父组件需要了解子组件信息时，通常应保持单向数据流，但某些场景下需要打破这一规则。

- 🧩 **组合式复合组件**：通过组件树而非 props 传递数据，例如`<List>`需要统计子项数量或提取属性，但直接遍历 children 的方法无法处理任意嵌套子组件。
- 🏗️ **嵌套复合组件方案**：React ARIA/Spectrum采用“假DOM”技术，通过portal将集合渲染到微型虚拟DOM中，从而获取完整组件树信息，同时支持服务端渲染。
- 🏷️ **管理<head/>标签**：子路由需要控制页面标题/描述等元数据，可通过 React Helmet 或 Unhead 库实现，利用上下文和状态初始化器在 SSR 时同步更新 head 标签。
- 🧭 **路由树匹配**：React Router 的`useMatches`钩子允许父路由读取子路由的元数据（如面包屑），通过路由的`handle`属性传递动态数据，实现层级感知的布局控制。
- ⚠️ **谨慎使用**：大多数情况下应优先通过 props 传递数据，仅在确实需要时才采用上述方案。

---

### [重塑](https://www.reshaped.so/)

**原文标题**: [Reshaped](https://www.reshaped.so/)

概述摘要
Reshaped 是一个现代化的设计系统，提供可访问的 React 和 Figma 组件，用于构建美观的产品或创建自己的设计系统。

- 🎨 **v4.0 更新**：推出 Figma 库改造、Storybook MCP 等新功能
- 📦 **安装方式**：通过 `npm install reshaped` 快速集成
- 🧩 **组件库**：提供 React 和 Figma 库，支持完全对齐的设置和最新 Figma 特性
- 📱 **响应式样式**：组件属性支持响应式语法，根据视口大小调整行为
- ♿ **无障碍性**：符合 WAI-ARIA 标准，内置屏幕阅读器支持和无障碍工具
- 🎯 **语义化设计令牌**：易于学习的主题层和暗色模式支持，可从单一颜色值自动生成主题
- 🛠️ **TailwindCSS 集成**：主题层可轻松导入 Tailwind 设置，支持暗色模式
- 🌐 **国际化**：支持任何语言和 RTL 语言
- 🤖 **AI 工作流**：React 库支持 Storybook MCP，Figma 库无缝集成设计代理
- 📘 **TypeScript 支持**：完整类型定义，支持自动补全和类型检查
- ⚙️ **框架支持**：兼容 Next.js、Vite 等框架，内置 RSC 支持
- 💬 **用户评价**：被团队和个人信赖，称赞其原子化组件方法、Figma 库与 React 库完美匹配、主题架构灵活且提供自动暗色模式支持
- 📚 **资源**：提供文档、设计令牌、主题游乐场、变更日志、路线图、博客等

---

### [GitHub - aurorascharff/nextjs-app-architecture-skill: Next.js 16 应用路由架构模式。功能切片设计、Suspense 流式渲染、缓存组件、用户体验模式。](https://github.com/aurorascharff/nextjs-app-architecture-skill)

**原文标题**: [GitHub - aurorascharff/nextjs-app-architecture-skill: Architecture patterns for Next.js 16 App Router apps. Feature-sliced design, Suspense streaming, Cache Components, UX patterns. · GitHub](https://github.com/aurorascharff/nextjs-app-architecture-skill)

该仓库提供了一个面向 AI 编码代理的 Next.js 16+ App Router 架构技能包，基于组件架构原则优化 RSC 应用开发。

- 📦 核心原则：页面是同步组合器（不直接获取数据），异步组件自行获取数据，骨架屏与组件同文件导出，Suspense 边界设在页面层，客户端边界尽可能下沉为叶节点
- ⚙️ 安装方式：通过 `npx skills install` 命令即可快速集成到项目中
- 📂 文件结构：`SKILL.md` 为核心文件始终加载，`references/` 目录按需加载，包含功能文件夹、查询操作、组件、页面 Suspense 等模块
- 🚀 即时应用：提供缓存组件和 UX 模式作为可选增强，用于实现即时响应的应用体验
- 📚 扩展阅读：包含服务端与客户端组件组合实践、Action Props 设计组件、Next.js 错误处理、避免瀑布流获取等进阶资源
- 🔗 配套演示：附有 `next16-social-media` 示例应用，展示架构模式的实际应用

---

### [GitHub - shadcn/improve：使用你最强大的模型审计代码库，并为更便宜的模型编写执行计划。](https://github.com/shadcn/improve)

**原文标题**: [GitHub - shadcn/improve: Use your most capable model to audit your codebase and write plans for cheaper models to execute. · GitHub](https://github.com/shadcn/improve)

shadcn/improve 是一个智能代理技能，用于审计代码库并生成执行计划，让更便宜的模型来执行。

- 📋 **核心理念**：用最强大的模型理解代码库、判断优先级、编写规范，而将执行交给更便宜的模型。计划本身就是产品。
- 🛠️ **安装与使用**：通过 `npx skills add shadcn/improve` 安装，支持多种命令如 `/improve`（全面审计）、`/improve quick`（快速审计）、`/improve deep`（深度审计）等。
- 🔍 **工作流程**：首先映射仓库（Recon），然后并行审计九个类别（正确性、安全、性能等），接着筛选和优先级排序，最后生成可执行计划。
- 📝 **计划特点**：每个计划都是自包含的 Markdown 文件，包含精确文件路径、代码示例、验证命令和停止条件，确保即使是弱模型也能执行。
- 🔄 **闭环机制**：支持执行计划（`/improve execute`）、协调更新（`/improve reconcile`）、作为 GitHub Issues 发布（`--issues`），确保计划不会石沉大海。
- 🚫 **硬性规则**：从不直接修改源代码，只写入 `plans/` 目录；从不运行改变工作树的命令；从不复制秘密值；被要求实现时会拒绝并指向计划。
- ⭐ **项目状态**：拥有 5.5k 星标、210 个分支，采用 MIT 许可证，由 shadcn 开发。

---

### [GitHub - vercel-labs/nextjs-nights-shader: WebGPU 星系着色器 — Next.js + Three.js TSL（WebGPU 渲染器）· GitHub](https://github.com/vercel-labs/nextjs-nights-shader)

**原文标题**: [GitHub - vercel-labs/nextjs-nights-shader: WebGPU galaxy shader — Next.js + Three.js TSL (WebGPURenderer) · GitHub](https://github.com/vercel-labs/nextjs-nights-shader)

这是一个基于 WebGPU 的实时银河着色器项目，使用 Next.js 和 Three.js TSL 构建，可作为独立组件嵌入任何页面。

- 🌌 **实时 WebGPU 银河着色器** - 使用 Three.js TSL 渲染程序化银河天空，包含约 14.6 万颗星星的实例化星空
- 🖱️ **交互式悬停流体效果** - 半拉格朗日密度 + 速度场，鼠标悬停时星星亮度随光标位置变化
- ✨ **后处理特效管线** - 包含 Bloom 辉光、有序 Bayer 抖动、SVG 徽标遮罩和边缘淡入淡出
- 🎨 **DOM 驱动定位** - 通过`data-galaxy-logo-target`占位元素自动对齐徽标位置，支持响应式布局
- 🔧 **调试 GUI** - 添加`?debug`参数可实时调整所有参数（Bloom、抖动、粒子、相机等）
- 🚀 **技术栈** - Next.js 16 + React 19 + Three.js 0.184 + Tailwind CSS v4 + Geist 字体
- 📝 **MIT 开源许可** - 支持自定义 SVG 徽标（红色通道控制亮度，绿色通道控制轮廓高光）

---

### [几分钟内为您的 AI-SDK 代理添加技能 | Bluebag 博客](https://www.bluebag.ai/blog/add-skills-to-your-ai-sdk-agent-in-minutes)

**原文标题**: [Add Skills to Your AI-SDK Agent in Minutes | Bluebag Blog](https://www.bluebag.ai/blog/add-skills-to-your-ai-sdk-agent-in-minutes)

Bluebag 通过两行集成代码，为 Vercel AI SDK 构建的 AI 代理提供即用型技能，无需管理任何基础设施。

- 🚀 **消除基础设施负担**：AI 代理需要执行 PDF 处理、数据分析等任务时，无需自行构建沙箱、虚拟机、依赖管理和文件存储等基础设施。
- 🧩 **技能即用**：代理可像人类一样发现和使用预打包的技能（如 PDF、数据分析、图像生成），通过 `bluebag.enhance()` 一行代码即可集成。
- 📚 **渐进式技能加载**：采用三级加载系统（元数据→完整文档→执行），最小化 token 消耗，只在需要时加载详细内容。
- 🖥️ **免管理运行时虚拟机**：虚拟机自动按需创建、预配置依赖、跨消息持久化（30 分钟自动刷新）、空闲自动终止，无需手动管理。
- 🛠️ **五大工具**：`bluebag_bash`、`bluebag_code_execution`、`bluebag_text_editor`、`bluebag_computer_use`、`bluebag_file_download_url`，覆盖执行、编辑、下载等需求。
- 🔗 **解决下载链接问题**：代理生成文件后，通过 `bluebag_file_download_url` 工具自动生成带签名的限时下载 URL，无需自行搭建文件存储。
- 🏢 **多租户隔离**：通过 `stableId` 参数自动隔离不同用户的沙箱、文件和会话状态，保障数据安全。
- 🎯 **可预测的代理行为**：技能包含经过测试的脚本、清晰的文档和定义的输出，使代理执行更稳定、结果更一致。
- ⚡ **快速集成**：安装 `@bluebag/ai-sdk` 包后，只需初始化 Bluebag 并调用 `enhance()` 即可获得技能增强的代理，兼容 Next.js、Express 等环境。

---

### [VoidZero 加入 Cloudflare](https://blog.cloudflare.com/voidzero-joins-cloudflare/)

**原文标题**: [VoidZero is joining Cloudflare](https://blog.cloudflare.com/voidzero-joins-cloudflare/)

VoidZero（Vite、Vitest、Rolldown、Oxc 和 Vite+ 背后的公司）加入 Cloudflare，所有团队成员也一同加入。所有项目保持 MIT 开源、供应商中立和社区驱动。Cloudflare 承诺投入 100 万美元的 Vite 生态系统基金，并计划将 Cloudflare 的工具链迁移到 Vite 之上。

- 🤝 **团队与项目不变**：VoidZero 全员加入 Cloudflare，但 Vite 等核心项目保持 MIT 开源、供应商中立，由原团队和社区继续主导。
- 🛡️ **中立承诺与资金支持**：Cloudflare 承诺不改变项目方向，并投入 100 万美元设立 Vite 生态系统基金，支持维护者和贡献者。
- 🔧 **技术合作深化**：基于 Vite Environment API 的 Cloudflare 插件下载量已达 Vite 的 10% 以上，未来将提供更多供应商无关的通用原语。
- 🤖 **AI 驱动的工具链**：VoidZero 工具链（Vitest、Rolldown、Oxc 等）专为 AI 代理的高频迭代设计，已成为 AI 生成应用的首选基础。
- 🚀 **Cloudflare 工具迁移**：Cloudflare 将把 CLI（如 `cf`）构建在 Vite 之上，实现 `cf dev` 作为 `vite dev` 的超集，统一开发体验。
- 🌐 **全栈与平台开源**：Vite 将扩展为支持全栈应用和代理的通用基础，Cloudflare 计划未来开源 Void 平台，促进生态共建。
- 📈 **立即体验**：用户可通过 `npm create vite@latest` 和 `npx wrangler deploy` 在 Cloudflare 上运行 Vite 应用。

---

### [为网页构建玻璃效果](https://aave.com/design/building-glass-for-the-web)

**原文标题**: [Building Glass for the Web](https://aave.com/design/building-glass-for-the-web)

本文介绍了 Aave 团队将 Apple 的 Liquid Glass 设计语言移植到 Web 端的技术实现，并构建了一套跨浏览器兼容的玻璃效果组件。

- 🍎 Apple 在 WWDC 上发布了 Liquid Glass 设计语言，灵感来自光穿过曲面玻璃的物理效果
- 🚀 Aave 团队受此启发，在 iOS/Android 应用中实现了 Aave Glass 效果，并希望将其带到 Web 端
- ⚠️ 现有 Web 实现仅支持 Chromium 浏览器，且依赖 SVG backdrop-filter 或实验性 API，兼容性差
- ✅ Aave 团队开发的技术可在所有现代浏览器（Chrome、Safari、Firefox）上运行，无需特殊设置
- 🎛️ 构建了开关、滑块、切换组等组件，玻璃效果增强了交互的深度和触感
- 📱 滑块和开关通过位移映射实现实时玻璃折射，保持流畅动画和内容可读性
- 🖼️ QR 码组件通过 WebGL 着色器实现玻璃效果，适用于无 DOM 内容的场景
- 🎬 视频播放器控件使用 WebGL 实现玻璃折射，解决了 Safari 不支持 SVG 滤镜处理实时视频的问题
- 🔧 核心技术基于 SVG feDisplacementMap 滤镜，通过位移映射实时弯曲像素，保持内容可交互
- 🧩 位移映射利用四分之一对称性计算，优化性能；针对 Safari 缓存和大小限制做了特殊处理
- 🔮 未来计划扩展玻璃组件库，统一 Aave 全平台用户体验
- 👏 感谢 Abhijeet Singh 领导研发、Lochie Axon 撰写文章，以及整个 Aave Labs 团队的贡献

---

### [一个核心，六个框架，零运行时抽象 | Formisch](https://formisch.dev/blog/one-core-six-frameworks/)

**原文标题**: [One core, six frameworks, zero runtime abstraction | Formisch](https://formisch.dev/blog/one-core-six-frameworks/)

### 概述  
Formisch 是一个无运行时抽象的表单库，支持 SolidJS、React、Vue、Svelte、Preact 和 Qwik，通过构建时替换框架原生响应式原语实现零开销集成。

- 🎯 **核心设计**：仅依赖四个函数（`createSignal`、`batch`、`untrack`、`createId`），无运行时适配层，构建时自动切换框架原生信号。
- 🔄 **构建时替换**：通过 Rolldown 插件在构建时重定向导入，每个框架生成独立包，无运行时检测或适配器加载。
- 🧩 **适配器示例**：Vue 直接导出 `shallowRef`，Preact 导出 `signal`，Qwik 导出原生信号，Solid 和 Svelte 仅需少量包装代码（<20 行），React 需约 100 行 pub/sub 实现。
- ⚡ **框架原生集成**：表单状态直接使用框架信号（如 Solid 的 `createMemo`、Vue 的 `computed`、Svelte 的 `$derived`），自动获得批处理、调度和细粒度跟踪。
- 📦 **可摇树优化**：每个表单操作（如 `reset`、`validate`）独立模块，未使用时不打包，核心保持轻量。
- 🛡️ **类型安全**：基于 Valibot 模式驱动运行时解析和 TypeScript 类型推断，字段重命名后自动类型检查所有 `<Field>` 组件。
- 🌍 **跨框架共享**：核心代码完全共享，改进、修复和性能优化同时惠及所有六个框架社区。

---

### [TSRX](https://tsrx.dev/blog/rethinking-tsrx)

**原文标题**: [TSRX](https://tsrx.dev/blog/rethinking-tsrx)

TSRX 重新回归 JSX，并用`@`前缀明确区分模板语法与普通 JavaScript，使代码更易读、更易维护。

- 🔄 **回归 JSX 基础**：静态文本不再需要引号包裹，直接使用 JSX 原生语法，动态值通过`{}`表达式插入，与 React/JSX 保持一致。
- 💬 **支持 JS 注释**：允许在 JSX 子元素中使用单行和多行 JavaScript 注释，便于在复杂标记旁保留意图说明。
- 📦 **新增 JSX 语句容器`@{...}`**：允许在 JSX 表达式中嵌入 JavaScript 语句，并以一个 JSX 节点作为输出结尾，可赋值给变量或作为组件体。
- 🏗️ **组件体直接返回语句容器**：当组件需要局部设置时，可直接返回`@{...}`容器，无需额外包裹空片段，并支持顶部提前返回。
- ⚛️ **React/Preact Hooks 保持显式**：不自动将条件分支中的 hooks 迁移到子组件，要求开发者显式创建命名组件来管理 hook 状态和顺序。
- 🏷️ **JSX 控制流显式化**：使用`@if`、`@for`、`@switch`、`@try`等前缀标记模板控制流，避免与普通 JavaScript 控制流混淆，并支持`@empty`空列表分支。
- 🎯 **控制流可赋值给变量**：显式模板控制流可以直接存储在变量中，无需额外包装函数，配合`JSX.Element`类型注解更精确。
- ✅ **总结**：通过`@`前缀明确模板语法边界，保留 JavaScript 的普通性，使代码更易扫描、编写和工具理解，准备进入 beta 阶段。

---

