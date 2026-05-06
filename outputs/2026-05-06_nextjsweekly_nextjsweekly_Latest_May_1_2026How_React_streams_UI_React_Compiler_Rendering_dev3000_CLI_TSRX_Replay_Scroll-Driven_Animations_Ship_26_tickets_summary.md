### [React 如何无序流式输出 UI 却依然保持有序 | React 内部探秘](https://inside-react.vercel.app/blog/how-react-streams-ui-out-of-order)

**原文标题**: [How React streams UI out of order and still manages to keep order | Inside React](https://inside-react.vercel.app/blog/how-react-streams-ui-out-of-order)

React通过Suspense边界实现无序流式渲染，同时确保最终DOM顺序正确，其核心机制是：先发送可用HTML和占位符，待数据就绪后通过JavaScript脚本将隐藏的组件内容替换到正确位置。

- 🚀 **无序流式渲染**：React Server Components和Suspense允许组件按数据就绪顺序流式传输，而非传统HTML的线性顺序，从而避免阻塞无关组件（如Navbar和Footer）。
- 🔄 **传统SSR的局限性**：即使并行请求数据，页面仍需等待所有组件完成才发送HTML；而流式渲染虽能部分解决，但若组件顺序依赖，仍会阻塞后续内容（如Footer因Recommendations未完成而延迟）。
- 🧩 **Suspense边界标记**：React在HTML中插入`<!--$?-->`和`<!--/$-->`作为边界，并用`<template id="B:0">`作为占位符，`id`唯一标识待替换位置。
- 📦 **隐藏组件传输**：数据就绪后，React将组件内容包裹在`<div hidden id="S:0">`中流式传输，避免直接插入DOM，而是暂存于隐藏元素。
- ⚡ **$RC函数执行替换**：通过`$RC("B:0", "S:0")`脚本，React查找占位符和隐藏组件，将两者配对后推入`$RB`队列，等待下一帧执行实际DOM交换。
- 🗑️ **清除回退UI**：`$RV`函数遍历Suspense边界内的所有兄弟节点（如加载动画），逐一移除，再将隐藏组件的子节点插入正确位置，并更新边界状态从`$?`（待定）→`$~`（排队）→`$`（完成）。
- 🔍 **生命周期状态**：Suspense边界通过注释标记状态：`$?`表示回退UI显示中，`$~`表示内容已就绪待渲染，`$`表示最终内容已插入DOM。
- ⚠️ **潜在风险**：若手动插入相同`id`的`<template>`标签，React可能误替换错误元素，破坏流式渲染逻辑。

---

### [Vercel 发布 26](https://vercel.com/ship)

**原文标题**: [Vercel Ship 26](https://vercel.com/ship)

该内容为一份城市与日期对应的时间表，列出了不同城市及其对应的日期（可能是活动、发货或行程安排）。

- 🚢 伦敦：6月17日
- 🚢 柏林：6月25日
- 🗽 纽约市：6月30日
- 🏖️ 悉尼：7月30日
- 🌉 旧金山：10月15日

---

### [GitHub - Blazity/next-migration-skills · GitHub](https://github.com/Blazity/next-migration-skills)

**原文标题**: [GitHub - Blazity/next-migration-skills · GitHub](https://github.com/Blazity/next-migration-skills)

该仓库是一个专为将 Next.js 从 Pages Router 迁移到 App Router 而设计的智能工具集，基于 Skills.sh 平台构建。

- 🛠️ **核心工具包**：`nextjs-migration-toolkit` 提供 AST 分析和转换功能，是所有其他技能的基础依赖
- 📊 **迁移评估**：`migration-assessment` 技能可分析代码库复杂度与迁移就绪程度
- 🗺️ **迁移规划**：`migration-planning` 技能用于创建分阶段迁移计划
- 🔗 **依赖映射**：`dependency-mapping` 技能将旧依赖映射到 App Router 等效项
- 🛣️ **路由转换**：`route-conversion` 技能将 `pages/` 路由转换为 `app/` 路由
- 🔄 **组件迁移**：`component-migration` 技能使组件兼容 React Server Components (RSC)
- 📡 **数据层迁移**：`data-layer-migration` 技能处理数据获取和 API 路由迁移
- ✅ **验证测试**：`validation-testing` 技能确保每个阶段后的正确性
- 🏗️ **项目结构**：采用 TypeScript 为主（97.9%），并包含 Handlebars 模板和 Shell 脚本
- 📦 **安装简便**：通过 `npx skills add blazity/next-migration-skills` 即可一键安装

---

### [React 编译器渲染指南，2026年4月](https://blog.isquaredsoftware.com/presentations/2026-04-react-compiler-rendering/?slideIndex=0&stepIndex=0)

**原文标题**: [A Guide to React Compiler Rendering, April 2026](https://blog.isquaredsoftware.com/presentations/2026-04-react-compiler-rendering/?slideIndex=0&stepIndex=0)

概述摘要：此内容为一条提示信息，表明需要启用JavaScript才能运行该应用。

- 🚫 当前应用无法运行，因为JavaScript未启用。
- ⚙️ 用户需在浏览器设置中启用JavaScript功能。
- 📱 此提示适用于网页或在线应用环境。

---

### [React 客户端与服务器端状态 | 技能提升](https://upskills.dev/tutorials/react-client-and-server-state?sections=1,2,3,4,5,6)

**原文标题**: [React Client And Server State | Upskills](https://upskills.dev/tutorials/react-client-and-server-state?sections=1,2,3,4,5,6)

本教程深入探讨了React应用中服务端状态与客户端状态的分离管理，阐述了为何以及如何使用TanStack Query和Zustand等库来分别处理这两种状态，并提供了从理论到实践的完整指南。

- 📖 **状态分离的起源**：早期React开发将所有状态（包括API响应、UI标志等）都放在同一个全局存储（如Redux）中，导致代码臃肿、缓存管理困难、组件间不必要的重渲染等问题。
- 🖥️ **服务端状态的定义与特性**：服务端状态是指从网络获取的数据，具有远程所有权、异步访问、最终一致性、跨客户端共享和持久化等特点。它需要一个专门的层来管理获取、缓存、去重、重新验证、变更和失效等完整生命周期。
- ⚙️ **服务端状态实践**：使用TanStack Query库，通过`queryKey`实现数据缓存共享，一个`['users']`缓存可同时服务于仪表盘、用户列表和详情抽屉等多个组件。通过`useMutation`和乐观更新模式，实现即时响应的用户角色修改体验。
- 🧩 **客户端状态的定义与特性**：客户端状态是本地、同步、仅属于当前会话和设备的状态，如侧边栏折叠、主题、模态框开关、表单草稿等。它不需要网络层的复杂基础设施，只需作用域管理纪律。
- 🗺️ **客户端状态处理层级**：从最轻量的组件内`useState`开始，依次尝试提升到父组件、模块/全局存储、URL和浏览器存储。大多数状态不需要全局存储，URL状态（如筛选、排序、页码）应优先考虑。
- 🛠️ **客户端状态实践**：使用Zustand库管理全局UI状态（如主题、侧边栏），通过选择器避免不必要的重渲染。使用`nuqs`库将筛选、分页等状态同步到URL，实现刷新持久化和深度链接。
- 🧠 **库的选择与核心模型**：服务端状态推荐TanStack Query（或SWR、RTK Query），客户端状态推荐Zustand（或Jotai、Valtio）。更重要的是理解状态分离的底层模型，而非盲目追随特定库。

---

### [在Next.js渲染期间对请求体进行黑客攻击](https://robertjwebb.substack.com/p/draft-hacking-in-request-body-during)

**原文标题**: [Hacking in request body during render in Next.js](https://robertjwebb.substack.com/p/draft-hacking-in-request-body-during)

### 概述总结
本文作者通过修改Next.js源码，成功实现了在渲染阶段读取POST请求体（body）的功能，并探讨了其实现原理、潜在问题及框架设计考量。

- 🔧 **核心挑战**：Next.js默认在渲染时仅提供请求头（headers），无法直接读取请求体（body），作者通过修改源码绕过此限制。
- 🛠️ **实现方法**：在Node原生请求中手动读取body流，将其注入到`NextRequest`对象，并修改`headers.ts`使其返回body数据。
- 🧪 **开发模式与生产模式**：开发模式直接利用`req.body`；生产模式需处理`workUnitStore`分支，最终通过修改`headers.ts`返回body。
- 🐛 **`cacheComponents` 兼容问题**：启用`cacheComponents`后，POST请求渲染导致空白页，原因是`postponedState`逻辑与POST方法冲突，需添加条件`req.method !== 'POST'`绕过。
- ⚠️ **潜在风险**：此修改可能破坏Next.js的SPA特性、引发渲染bug，且不符合现代Web开发最佳实践（如使用`fetch` POST后导航）。
- 📝 **作者建议**：不推荐框架官方支持此功能，因为99%的用户场景可通过查询参数或JWT等方案解决，且实现复杂、易出错。

---

### [未找到标题](https://x.com/iamncdai/status/2048085088974618849)

**原文标题**: [No title found](https://x.com/iamncdai/status/2048085088974618849)

此页面提示用户浏览器中未启用JavaScript，导致无法正常访问x.com（原Twitter）。建议启用JavaScript或更换支持的浏览器，并提供了相关帮助链接和政策信息。若问题持续，可尝试禁用隐私相关扩展或重新加载页面。

- 🔒 检测到浏览器JavaScript被禁用，需启用或更换支持的浏览器以继续访问x.com
- 📚 提供帮助中心、服务条款、隐私政策、Cookie政策等链接供用户参考
- ⚠️ 页面加载失败时显示“再试一次”按钮，并提示隐私扩展可能造成干扰
- 🚫 页面底部显示版权信息（© 2026 X Corp.）及法律声明

---

### [GitHub - vercel-labs/dev3000: 捕获Web应用的完整开发时间线——服务器日志、浏览器事件、控制台消息、网络请求及自动截图——统一为带时间戳的流，供AI调试使用。](https://github.com/vercel-labs/dev3000)

**原文标题**: [GitHub - vercel-labs/dev3000: Captures your web app's complete development timeline - server logs, browser events, console messages, network requests, and automatic screenshots - in a unified, timestamped feed for AI debugging. · GitHub](https://github.com/vercel-labs/dev3000)

d3k（dev3000）是一个开源的AI调试助手，能自动捕获Web应用开发过程中的服务器日志、浏览器事件、网络请求和屏幕截图，并以时间线形式组织，供AI理解并辅助修复问题。

- 🚀 **快速启动**：通过 `bun install -g dev3000` 安装，运行 `d3k` 命令即可开始调试，支持与Claude、Codex等AI代理协同工作。
- 📋 **全面捕获**：自动记录服务器日志、浏览器控制台消息、网络请求、用户交互（点击、表单提交）以及自动屏幕截图（导航、错误等）。
- 🛠️ **丰富CLI命令**：包括 `d3k errors`（查看错误）、`d3k logs`（查看日志）、`d3k fix`（深度分析错误）、`d3k crawl`（爬取应用URL）等，支持多种选项如端口、脚本、浏览器路径等。
- 🔧 **灵活运行模式**：支持分屏模式（`--with-agent`）、无代理模式（`--no-agent`）、无头模式（`--headless`，适合CI/CD）、仅服务器模式（`--servers-only`）等。
- 🌐 **多框架支持**：兼容JavaScript/TypeScript（Next.js、Vite等）、Python（Django、Flask）、Ruby（Rails）等任何Web框架。
- 📂 **文件存储**：日志、屏幕截图、Chrome配置文件等存储在 `~/.d3k/{project}/` 目录下，便于AI读取。
- 🔄 **持续开发**：项目活跃维护，有2,197次提交，支持贡献，遵循MIT许可证。

---

### [TSRX](https://tsrx.dev/)

**原文标题**: [TSRX](https://tsrx.dev/)

### 概述总结
TSRX 是一种 TypeScript 语言扩展，用于在智能体时代构建声明式 UI，它通过将结构、样式和控制流共置在同一文件中，提供更清晰、可维护的代码编写方式，并支持编译到多种主流框架。

- 🚀 **核心概念**：TSRX 是 JSX 的精神继承者，将 UI 直接嵌入 TypeScript，支持控制流、作用域样式和局部变量作为一等语法，而非通过表达式插槽实现。
- 🔄 **框架无关与互操作性**：可编译到 React、Preact、Ripple、Solid 和 Vue 等框架，支持从 JS、TS 和 TSX 文件导入 `.tsrx` 模块，无需重写现有代码。
- 🧩 **共置优势**：结构、控制流、样式和组件形状共存于同一文件，减少三元表达式、映射链和渲染辅助函数，使代码更接近所描述的界面，便于人类和 AI 理解。
- ⚙️ **人体工程学改进**：自动处理框架的“陷阱”，如条件性调用 React hooks（编译器自动提升分支为独立组件）、Solid props 的惰性解构、局部变量与 JSX 共置，减少数据流追踪负担。
- 🛠️ **工具链集成**：提供语言服务器（编辑器诊断、导航、补全）、Prettier 和 ESLint 插件，支持 VS Code、Zed、Neovim、IntelliJ 和 Sublime 等 IDE，可渐进式采用。
- 🧠 **智能编译**：通过 AST 解析和框架特定插件（如 `@tsrx/react`）生成惯用输出，支持作用域 CSS，可扩展新编译目标。
- 🌐 **开源与状态**：采用 MIT 许可证，处于活跃 Alpha 开发阶段，欢迎在问题追踪器反馈。

---

### [GitHub - vercel-labs/防止水合前闪烁 · GitHub](https://github.com/vercel-labs/preventing-flash-before-hydration)

**原文标题**: [GitHub - vercel-labs/preventing-flash-before-hydration · GitHub](https://github.com/vercel-labs/preventing-flash-before-hydration)

该存储库是Vercel Labs提供的演示项目，展示了如何在Next.js中防止水合（hydration）前的闪烁问题，并提供了多种解决模式的示例代码。

- 🚀 项目概述：演示防止水合前闪烁的配套示例，基于Next.js构建，模拟服务器与客户端区域设置不匹配的场景。
- 🌐 路由示例：包含/inline-script（内联脚本无闪烁）、/hydration-error（水合错误演示）和/accordion（手风琴状态持久化）三个关键路由。
- 🛠️ 核心模式：InlineScript辅助组件在服务端和客户端使用不同type属性避免React警告；LocalDate组件结合useId和suppressHydrationWarning处理日期格式化。
- 📦 本地运行：使用pnpm install和pnpm dev命令启动，通过LANG环境变量模拟区域设置不匹配，便于测试不同客户端区域设置下的行为。
- ⚙️ 技术栈：基于TypeScript（91.8%）、JavaScript（4.4%）和CSS（3.8%）构建，聚焦React和Next.js的水合优化。

---

### [GitHub - skillsynchq/replay · GitHub](https://github.com/skillsynchq/replay)

**原文标题**: [GitHub - skillsynchq/replay · GitHub](https://github.com/skillsynchq/replay)

Replay 是一个用于分享 AI 编程会话的开源 Web 应用，支持上传 Claude Code 或 Codex 的对话记录，生成可浏览的永久链接。

- 📤 支持从 Claude Code 和 Codex 上传会话，并生成永久链接
- 💬 完整渲染对话内容，包括内联差异、工具调用和思考块
- 🔒 提供公开、不公开或私有的可见性设置
- 🔍 支持全文搜索所有会话线程
- 🤖 决策追踪功能，从对话历史生成 AI 叙述
- ⭐ 可对线程进行星标和标签分类
- 🛠️ 用例包括决策记录、作品集展示、代码审查和技能创建
- 🖥️ 配套 CLI 工具（replay-cli）用于上传会话
- 💻 技术栈：Next.js 16、React 19、Tailwind CSS 4、Drizzle ORM、Better Auth 等
- 📜 使用 Apache 2.0 许可证，欢迎贡献

---

### [几分钟内为你的AI-SDK代理添加技能 | Bluebag博客](https://www.bluebag.ai/blog/add-skills-to-your-ai-sdk-agent-in-minutes)

**原文标题**: [Add Skills to Your AI-SDK Agent in Minutes | Bluebag Blog](https://www.bluebag.ai/blog/add-skills-to-your-ai-sdk-agent-in-minutes)

### 概述总结
Bluebag 通过两行集成代码，为 Vercel AI SDK 构建的 AI 代理提供即用型技能（Skills），无需管理沙箱、虚拟机、依赖或文件存储等基础设施，让代理能直接执行 PDF 处理、数据分析等复杂任务。

- 🚀 **两行集成**：只需 `bluebag.enhance()` 和 `streamText()` 即可为代理添加技能，无需 Kubernetes 或 Docker 等基础设施。
- ⚙️ **渐进式技能发现**：系统通过三级加载（元数据、完整文档、执行）最小化 token 使用，代理按需读取技能手册。
- 🖥️ **托管运行时 VM**：沙箱化虚拟机自动管理配置、持久化、清理和恢复，开发者无需关注底层。
- 🛠️ **五大工具**：集成后获得 `bluebag_bash`、`bluebag_code_execution`、`bluebag_text_editor`、`bluebag_computer_use` 和 `bluebag_file_download_url` 等工具。
- 🔗 **文件下载简化**：通过 `bluebag_file_download_url` 生成带签名的下载链接，无需自建文件存储和分发系统。
- 🔒 **多租户隔离**：使用 `stableId` 自动隔离不同用户的沙箱、文件和会话状态。
- 📋 **可预测输出**：技能包含经过测试的脚本和清晰文档，确保代理行为一致、调试更简单。
- 🏗️ **专注业务逻辑**：开发者只需关注提示词、用户体验和业务逻辑，Bluebag 处理所有执行基础设施。

---

### [React 编译器十八个月：历程、争议与未来展望 | Sascha Becker](https://saschb2b.com/blog/react-compiler-year-in-review)

**原文标题**: [The React Compiler at Eighteen Months: The Arc, the Debates, and What's Next | Sascha Becker](https://saschb2b.com/blog/react-compiler-year-in-review)

React 编译器在发布18个月后，已从初期集成进入生态成熟与社区辩论阶段。它主要解决了手动记忆化带来的bug，并强制执行React规则，但并非万能药。迁移路径已明确，但社区对部分问题仍有争议，未来将聚焦更细粒度控制、服务端组件优化和工具改进。

- 📅 **18个月发展历程**：从2024年底Beta发布，经历框架集成、工具成熟，到2025年底进入生态反思阶段。新项目已完美解决，旧项目迁移仍是工程任务。
- ⚙️ **编译器核心功能**：构建时自动插入记忆化，消除`useMemo`/`useCallback`/`memo`等手动代码。能优化子表达式粒度，但会增加构建时间和少量包体积。
- ❌ **编译器失效场景**：包括渲染时修改props/闭包、渲染时读取ref、类组件、不支持的语法（如解构prop重赋值、try/catch中的条件链），以及需要谨慎使用的`"use no memo"`逃逸机制。
- 🛠️ **推荐迁移步骤**：先升级React 19+，安装ESLint插件并提升规则为error，启用注解模式测试，再切换到推理模式，最后批量删除手动记忆化代码。
- 🔍 **严格规则实践**：开启`react-hooks/todo`等隐藏规则可捕获更多编译器内部失败模式（如循环中突变计数器、effect内动态import），但需注意静默跳过会级联，需迭代修复。
- 💬 **社区三大争议**：React规则是否过于严格、`"use no memo"`是否成为技术债、编译器与运行时优化器（如Million.js）的关系尚未定论。
- 🚀 **未来发展方向**：更细粒度的编译控制、编译器感知的服务端组件、`useEvent`原语、React Native优化，以及缺失的DevTools可视化面板。

---

### [滚动驱动动画 • 乔什·W·科莫](https://www.joshwcomeau.com/animation/scroll-driven-animations/)

**原文标题**: [Scroll-Driven Animations • Josh W. Comeau](https://www.joshwcomeau.com/animation/scroll-driven-animations/)

以下是您提供的文章内容的摘要：

该文章介绍了CSS Animation Timeline API，这是一种无需JavaScript即可实现滚动驱动动画的新技术。它通过将关键帧动画映射到滚动进度上，使元素在滚动时平滑变化。

- 🎯 **核心概念**：使用`animation-timeline: view()`将关键帧动画与元素在视口中的滚动进度绑定，替代传统的基于时间的动画。
- ⏱ **时间函数**：支持自定义缓动曲线（如`cubic-bezier`）和弹簧效果（`linear()`），增强动画的流畅性和表现力。
- 📏 **动画范围**：通过`animation-range`属性（如`cover`、`contain`、`entry`、`exit`）精确控制动画开始和结束的滚动位置。
- 🔄 **进入与退出**：利用`entry`和`exit`范围实现元素进入或离开视口时的动画效果，并可组合多个关键帧动画。
- 🎯 **范围百分比**：使用`animation-range-start`和`animation-range-end`自定义动画的精确起始和结束点，提供更精细的控制。
- 📊 **滚动进度时间线**：通过`animation-timeline: scroll()`跟踪整体滚动进度，适用于阅读进度指示器等场景。
- 🔗 **链接时间线**：使用`view-timeline`和`timeline-scope`将一个元素的滚动进度应用到另一个元素的动画上，实现分离测量与动画。
- 🚀 **未来展望**：文章还提及了`animation-trigger`属性（用于滚动触发动画）等新特性，但当前浏览器支持有限。

---

### [在她生命的早期。而且他们都不是六岁。我已经。](https://www.readwriterachel.com/things-i-learned/2026/04/23/back-to-basics-react-variables.html)

**原文标题**: [Early in her life. And all of them isnât six years old. Iâve.](https://www.readwriterachel.com/things-i-learned/2026/04/23/back-to-basics-react-variables.html)

概述摘要
- 😢 她早年生活坎坷，六岁时便经历不幸。
- 🌍 她站在那里感叹：“啊，美丽的新世界。”
- 🎭 人应在保持坚定目标的同时，运用有意识的欺骗。
- ⏳ 伯纳德匆忙赶到，立体影像中传来惊叹声。
- 🧵 那人说：“缝的针数越多……”，并提到约翰。
- 🤔 他痛苦地说：“有趣你提起他们，同样的事发生了。”
- 📚 参见：一切皆偶然发生。

---

### [错误](https://itnext.io/backend-for-frontend-bff-what-it-is-and-when-to-use-it-6e8edb72e32c)

**原文标题**: [Error](https://itnext.io/backend-for-frontend-bff-what-it-is-and-when-to-use-it-6e8edb72e32c)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='itnext.io', port=443): Max retries exceeded with url: /backend-for-frontend-bff-what-it-is-and-when-to-use-it-6e8edb72e32c (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

---

