### [React Email 6.0 · Resend](https://resend.com/blog/react-email-6)

**原文标题**: [React Email 6.0 · Resend](https://resend.com/blog/react-email-6)

React Email 6.0 发布，带来开源编辑器、新模板和统一包，下载量激增 108%。

- 🎉 核心亮点：React Email 6.0 正式发布，包含开源编辑器、自定义扩展、新模板和统一包，npm 周下载量达 200 万，较上版本增长 108%。
- ✍️ 开源编辑器：新增独立包`@react-email/editor`，可嵌入应用，输出兼容各大邮箱的 HTML，支持默认主题和自定义主题。
- 🔧 扩展架构：编辑器分核心层和扩展层，通过`EmailNode` API 构建自定义块（如图片上传、图表渲染），支持`renderToReactEmail`输出。
- 📧 新模板：与 Character Studio 合作推出认证和电商模板，提供 React Email 和 Figma 格式，可直接使用或拆解。
- 📦 统一包：所有组件整合至`react-email`包，无需多包安装（编辑器除外），`@react-email/preview-server`迁移至`@react-email/ui`。
- 🔄 升级指南：从 5.0 升级需移除旧包、安装新包并更新导入路径（从`@react-email/components`改为`react-email`）。
- 🙏 社区感谢：感谢 196 位开源贡献者，推动项目发展。

---

### [Vercel 2026 年 4 月安全事件 | Vercel 知识库](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)

**原文标题**: [Vercel April 2026 security incident | Vercel Knowledge Base](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)

### 概述总结
Vercel 在 2026 年 4 月遭遇一起安全事件，涉及对内部系统的未授权访问。攻击源自第三方 AI 工具 Context.ai 的泄露，攻击者借此入侵员工账户，进而访问 Vercel 环境并解密非敏感环境变量。Vercel 已展开调查、通知受影响客户、与执法部门合作，并发布了缓解建议和产品改进措施。

- 🔒 **事件起源**：攻击始于第三方 AI 工具 Context.ai 的泄露，攻击者利用该工具入侵员工 Google Workspace 账户，进而访问 Vercel 环境。
- 🎯 **受影响范围**：最初发现少量客户的非敏感环境变量被泄露；后续调查发现更多账户被入侵，但部分与本次事件无关。
- 🛡️ **供应链安全**：经与 GitHub、Microsoft、npm 和 Socket 合作确认，Vercel 发布的 npm 包未受篡改，供应链保持安全。
- 🚨 **攻击者特征**：攻击者操作速度快、对 Vercel 产品 API 有深入了解，被认为高度复杂。
- 📋 **建议措施**：启用多因素认证、轮换非敏感环境变量、使用敏感环境变量功能、检查活动日志和部署记录、设置部署保护。
- 🔍 **入侵指标**：发布了一个 Google Workspace OAuth 应用 ID，供社区检查潜在恶意活动。
- 🛠️ **产品改进**：已推出环境变量管理优化、团队级安全概览、更易用的活动日志等功能。

---

### [Clerk CLI](https://clerk.com/changelog/2026-04-22-clerk-cli?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=cli&utm_content=04-24-26&dub_id=f9iC8BQzwo6gq8Oh)

**原文标题**: [Clerk CLI](https://clerk.com/changelog/2026-04-22-clerk-cli?utm_source=nextjs-weekly&utm_medium=newsletter&utm_campaign=cli&utm_content=04-24-26&dub_id=f9iC8BQzwo6gq8Oh)

### 概述总结
Clerk CLI 是一款全新的命令行工具，帮助开发者和 AI 代理直接在终端管理认证、计费等操作，支持脚本化工作流，避免手动点击操作。

- 🛠️ **核心功能**：提供 `clerk init`（快速集成框架）、`clerk config`（管理应用设置）、`clerk api`（直接操作 API）等关键命令，简化开发流程。
- 📦 **安装方式**：支持 `bunx`、`npm`、`pnpm`、`yarn`、Homebrew 或 curl 脚本安装，灵活适配不同环境。
- 🚀 **未来计划**：即将推出 `clerk deploy` 命令，一键验证并部署认证配置，实现从开发到生产的无缝切换。
- 🌐 **开源与文档**：工具完全开源，提供完整文档和 `clerk --help` 命令，便于快速上手。

---

### [文档：添加避免水合闪烁的日期显示指南 (#92786) · vercel/next.js@931868b · GitHub](https://github.com/vercel/next.js/commit/931868b86c4079300d059dab4301e8dab8924249#diff-c7ddc7709fa2b3f7c68d45c10aa119f5250bb8f758525cedb0329f9972660c68)

**原文标题**: [docs: add guide for displaying dates without hydration flash (#92786) · vercel/next.js@931868b · GitHub](https://github.com/vercel/next.js/commit/931868b86c4079300d059dab4301e8dab8924249#diff-c7ddc7709fa2b3f7c68d45c10aa119f5250bb8f758525cedb0329f9972660c68)

此提交为 Next.js 文档新增了关于在预渲染页面上显示日期时避免水合闪烁的指南。

- 📅 **新增指南**：创建 `displaying-dates.mdx` 文档，解决服务端和客户端因区域设置不同导致的日期显示闪烁问题。
- 🛠️ **三步解决方案**：逐步展示问题、使用内联 `<script>` 配合 `suppressHydrationWarning` 修复、提取可复用的 `<LocalDate>` 组件。
- 📊 **方法对比表**：提供 `connection()`、客户端组件 `useEffect`、完全动态页面等替代方案的适用场景对比。
- 🔗 **交叉引用更新**：在 `public-static-pages.mdx` 和 `connection.mdx` 中添加相关提示和替代方案说明。
- ✨ **代码规范**：遵循文档惯例，使用 Prettier 格式化，包含 frontmatter、`switcher` 模式、`filename` 属性等。
- 🤖 **协作提交**：由 Cursor Agent 和 Joseph Chamochumbi 共同完成，共修改 3 个文件，新增 466 行代码。

---

### [如果你看不见边界，就无法推理系统 · Valentin Prugnaud](https://valentinprugnaud.dev/posts/2026/04/if-you-cant-see-the-boundary-you-cant-reason-about-the-system)

**原文标题**: [If you can't see the boundary, you can't reason about the system · Valentin Prugnaud](https://valentinprugnaud.dev/posts/2026/04/if-you-cant-see-the-boundary-you-cant-reason-about-the-system)

本文探討了 React Server Components (RSC) 在 Next.js 中的可觀測性問題，指出開發者因無法在運行時直觀看到伺服器與客戶端的邊界，而難以除錯與推理系統。作者介紹了其開發的開源工具「RSC Boundary」，旨在提供視覺化邊界覆蓋層，並呼籲框架原生整合此類工具以改善開發體驗。

- 🧩 **核心痛點：邊界不可見**：開發者無法在運行時直接觀察到 RSC 的伺服器/客戶端邊界，只能依賴 `'use client'` 標記和檔案結構推測，導致除錯效率低落。
- ⚖️ **取捨：放棄 RSC 換取可觀測性**：有經驗的開發者寧可選擇 React + Vite 的純客戶端模式，犧牲伺服器優先架構，換取更易於檢查和除錯的運行時環境。
- 🔍 **工具現狀：缺乏即時邊界地圖**：Next.js 的開發工具（如指示器、MCP）和 React DevTools 均無法在頁面層級即時顯示伺服器與客戶端的具體分割位置。
- 🛠️ **解決方案：RSC Boundary 開源工具**：這是一個開發專用的覆蓋層，可高亮顯示客戶端元件根節點與伺服器區域，讓開發者獲得具體的邊界地圖，而非純粹推測。
- 🏗️ **架構隱喻：看不見邊界就無法推理系統**：任何具有隱藏邊界的架構（如微服務、邊緣運算）都會導致開發者建立不完整的心理模型，增加除錯成本並讓框架被誤解為複雜。
- 🌟 **理想目標：原生整合邊界可視化**：作者建議 Next.js 提供穩定的擴充點，讓第三方工具能將邊界視圖整合進現有開發指示器，使可觀測性成為核心基礎設施而非選配功能。

---

### [Next.js 16 迁移指南：所有破坏性变更及修复方法 | Code With Seb](https://www.codewithseb.com/blog/nextjs-16-migration-guide-breaking-changes)

**原文标题**: [Next.js 16 Migration Guide: Everything That Breaks (And How to Fix It) | Code With Seb](https://www.codewithseb.com/blog/nextjs-16-migration-guide-breaking-changes)

以下是 Next.js 16 迁移指南的摘要，包含关键变更和修复方法：

Next.js 16 引入了重大变更，包括中间件重命名为代理、Turbopack 成为默认打包器、同步请求 API 完全移除，以及新的缓存组件。迁移过程有清晰的路径，并提供了代码示例。

- 🔄 **中间件重命名为代理**：`middleware.ts` 变为 `proxy.ts`，默认运行时从 Edge 切换为 Node.js，提供完整 Node API 访问。使用 `npx @next/codemod@latest proxy-upgrade` 自动迁移。
- ⚡ **同步请求 API 完全移除**：`cookies()`、`headers()`、`params` 和 `searchParams` 必须使用 `await`。运行 `npx @next/codemod@latest async-request-apis` 处理大部分情况，注意异步级联问题。
- 🚀 **Turbopack 成为默认打包器**：`next dev` 和 `next build` 默认使用 Turbopack，性能提升显著（如开发服务器启动快 4.4 倍）。自定义 webpack 加载器需迁移至 `turbopack.rules` 配置。
- 🗂️ **缓存组件与 'use cache' 指令**：移除隐式 fetch 缓存和 `unstable_cache`，改用显式 `'use cache'` 指令、`cacheLife()` 和 `cacheTag()` 进行细粒度缓存控制。提供预定义缓存生命周期配置文件。
- ⚛️ **React 19.2 与 React Compiler 1.0**：默认启用 React Compiler，自动处理大部分 `useMemo`/`useCallback`，提升性能。新增 `ViewTransition` 和 `Activity` 组件。
- 📋 **分步迁移指南**：升级依赖、运行代码转换工具、重新生成类型、更新 `next.config.ts`、修复类型错误、测试本地环境、验证缓存行为。注意常见陷阱，如忘记 `await params` 和第三方中间件包兼容性。

---

### [在 Next.js 中使用 LogLayer 进行日志记录：仪表化、控制台覆盖与结构化日志 | Yuri Mutti](https://yurimutti.com/posts/logging-nextjs-loglayer-instrumentation-console-override-structured-logs)

**原文标题**: [Logging in Next.js with LogLayer: Instrumentation, Console Override, and Structured Logs | Yuri Mutti | Yuri Mutti](https://yurimutti.com/posts/logging-nextjs-loglayer-instrumentation-console-override-structured-logs)

本文介紹如何在 Next.js 中使用 LogLayer 統一伺服器、客戶端和邊緣運行時的日誌記錄，並通過 `instrumentation.ts` 攔截 `console.*` 調用，實現結構化日誌輸出。

- 📋 **統一日誌模型**：LogLayer 提供一個共享 Logger 實例，讓伺服器、客戶端和邊緣日誌使用相同 API，解決 Next.js 多運行時日誌不一致問題。
- 🛠️ **攔截 console.* 調用**：在 `instrumentation.ts` 中覆蓋 `console.*` 方法（限 Node.js 運行時），將舊代碼和第三方庫的日誌導入 LogLayer，確保輸出結構化。
- 🔧 **靈活傳輸層**：開發環境使用 `SimplePrettyTerminal` 輸出可讀日誌，生產環境伺服器端切換到 `PinoTransport`，並預留 Datadog、OpenTelemetry 等擴展接口。
- 🏷️ **上下文與元數據管理**：`withContext()` 持久化上下文（如 `isServer`），`withMetadata()` 和 `withError()` 作用於單條日誌，支持錯誤序列化（`serialize-error`）。
- 🖥️ **伺服器端演示**：通過 `force-dynamic` 確保每次請求執行，展示 `console.log` 攔截、直接 LogLayer 調用、以及鏈式上下文/元數據/錯誤附加的效果。
- 📱 **客戶端演示**：在 `useEffect` 中使用相同 Logger API，客戶端日誌輸出到瀏覽器控制台，保持與伺服器端一致的開發體驗。
- 🚀 **未來擴展**：支持 Datadog、OpenTelemetry 追蹤、邊緣運行時（使用 `@loglayer/transport-http` 並啟用 `enableNextJsEdgeCompat`），保持供應商無關的 API 邊界。

---

### [着色器实验室 | 地下室工作室](https://eng.basement.studio/tools/shader-lab)

**原文标题**: [Shader Lab | basement.studio](https://eng.basement.studio/tools/shader-lab)

该文本描述了 CRT 显示效果的详细参数设置，包括失真、辉光、噪点等视觉特效的调节选项。

- 🖥️ **CRT 效果**：提供多种复古显示模式，如 Slot-Mask Monitor，可模拟老式显像管屏幕质感。
- ⚙️ **失真调节**：支持桶形失真（0.15）、汇聚（2）和暗角（0.45），调整画面几何与边缘暗影。
- 🌈 **色彩与亮度**：可控制色相、饱和度、亮度（1.2）、高光驱动（1）及阴影提升（0.16），优化画面色调。
- ✨ **辉光效果**：Bloom 参数包括强度（1.93）、阈值（0）、半径（24）和柔化（0.2），增强光晕感。
- 📺 **扫描线与遮罩**：扫描线强度（0.17）和遮罩缩放（6）可调节，模拟 CRT 像素结构。
- 🔄 **噪点与故障**：闪烁（0.2）、故障（0.13）及故障速度（5）可调，增加复古干扰效果。
- 🎚️ **图层与混合**：支持不透明度（100%）和正常混合模式，可叠加 CRT 效果于其他图层。

---

### [GitHub - icydotdev/nextmap: 你的 Next.js 所有路由的可视化交互地图。零配置。](https://github.com/icydotdev/nextmap)

**原文标题**: [GitHub - icydotdev/nextmap: A visual, interactive map of all your Next.js routes. Zero config. · GitHub](https://github.com/icydotdev/nextmap)

nextmap 是一个零配置的 Next.js 路由可视化工具，能自动扫描项目并生成交互式路由地图，支持 App Router、Pages Router 和混合项目。

- 🗺️ 一键启动：使用 `npx nextmap` 即可自动扫描并打开浏览器显示路由地图
- 🔍 全面路由支持：覆盖 App Router 和 Pages Router 的页面、API 路由、布局、中间件等
- 🎨 交互式图表：基于 React Flow 实现可缩放、可拖拽的路由图，包含小地图导航
- 🏷️ 智能识别：自动检测 HTTP 方法、动态路由、路由组、并行路由等特殊结构
- 📂 源代码查看：点击任意路由可在详情面板中查看带语法高亮的源代码
- 🔧 过滤与搜索：支持按类型、路由器筛选，以及按路径搜索
- 🌓 主题切换：支持深色/浅色模式，并跟随系统偏好
- 📸 SVG 导出：可通过 UI 或 CLI 命令导出静态 SVG 文件
- 🔒 本地运行：所有操作均在本地完成，代码不会上传至外部服务
- ⚡ 零配置：无需任何设置或注解，直接运行即可使用

---

### [免费开源动画 ReactJS 组件 | animata](https://animata.design/)

**原文标题**: [Free & Open Source Animated ReactJS Components | animata](https://animata.design/)

该页面介绍了一个包含 194+ 个动画 React 组件的开源库，旨在帮助开发者快速构建更美观、更高效的界面。

- 🚀 **加速开发**：提供 194+ 个可直接复制到项目中的动画 React 组件，无需安装，即拿即用。
- ⭐ **社区认可**：已获得 2,300+ 颗 GitHub 星标，受到全球开发者信赖，来自印度、德国、美国等多国用户好评。
- 🎨 **组件丰富**：涵盖背景、按钮、卡片、图表、导航、文本、进度条等 20+ 类别，满足多样界面需求。
- 🛠️ **实用优先**：所有组件均源自真实产品，确保实用性；内置键盘焦点、屏幕阅读器标签及减少动效回退，注重无障碍性。
- 🔓 **开源免费**：采用 MIT 许可证，永久免费，社区驱动，已有大量贡献者参与。
- 🌐 **广泛兼容**：支持 Next.js、Remix、Vite、Astro、Gatsby 等主流框架，灵活适配不同项目。

---

### [宣布 TypeScript 7.0 Beta 版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)

TypeScript 7.0 Beta 正式发布，基于 Go 语言重写，性能大幅提升，兼容性良好，并带来多项新特性与配置变更。

- 🚀 核心架构从 TypeScript 迁移至 Go，编译速度比 6.0 快约 10 倍，支持并行解析、类型检查和代码生成。
- 🧪 Beta 版已通过大规模测试，在微软及多家公司（如 Google、Figma、Vercel）的百万行级代码库中稳定运行，可立即用于日常开发。
- 📦 通过 npm 安装 `@typescript/native-preview@beta`，使用 `tsgo` 命令替代 `tsc`；VS Code 扩展提供编辑器支持，性能与命令行一致。
- 🔄 可与 TypeScript 6.0 并行运行，通过 `@typescript/typescript6` 包和 `tsc6` 入口点避免冲突，推荐使用 npm 别名过渡。
- ⚙️ 新增 `--checkers`（默认 4）和 `--builders` 控制并行度，`--singleThreaded` 用于调试或资源受限环境。
- 📋 默认配置变更：`strict` 为 true，`module` 默认为 `esnext`，`rootDir` 默认为 `./`，`types` 默认为 `[]` 等，需手动调整。
- ❌ 多项废弃功能变为硬错误：不再支持 `target: es5`、`downlevelIteration`、`module: amd` 等，需迁移至新方案。
- 📝 JavaScript 支持重写，更一致地分析 `.js` 文件，移除部分 JSDoc 特殊语法（如 `@enum`、`@class` 等）。
- 🛠 编辑器体验增强：支持自动导入、悬停提示、内联提示、代码镜头、JSX 链接编辑等，但仍有个别功能待完善。
- 📅 未来计划：改进 `--watch` 模式、完善 JavaScript 声明文件输出、稳定 API 预计在 7.1 版本，正式版预计两个月内发布。

---

### [无](https://expo.dev/blog/from-web-to-native-with-react?utm_source=Nextjsweekly&utm_medium=newsletter&utm_campaign=33087804-React%20to%20Native&utm_content=react_to_native_blog)

**原文标题**: [None](https://expo.dev/blog/from-web-to-native-with-react?utm_source=Nextjsweekly&utm_medium=newsletter&utm_campaign=33087804-React%20to%20Native&utm_content=react_to_native_blog)

概述摘要：本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了诊断、药物研发和个性化治疗等关键方面。

- 🩺 人工智能在医学影像分析中表现优异，能辅助医生更快速、准确地检测疾病，如癌症和视网膜病变。
- 💊 通过机器学习算法，AI 可加速新药研发过程，从海量数据中筛选潜在化合物，缩短临床试验周期。
- 🧬 个性化医疗借助 AI 分析患者基因、生活方式等数据，制定定制化治疗方案，提升疗效并减少副作用。
- 📊 电子健康记录系统结合 AI，能预测疾病风险、优化医院资源分配，并改善患者护理流程。
- ⚠️ 数据隐私、算法偏见及监管挑战仍是 AI 在医疗领域广泛应用的主要障碍，需谨慎应对。

---

### [构建无断点的用户界面 – 前端大师博客](https://frontendmasters.com/blog/building-a-ui-without-breakpoints/)

**原文标题**: [Building a UI Without Breakpoints – Frontend Masters Blog](https://frontendmasters.com/blog/building-a-ui-without-breakpoints/)

本文探讨了现代响应式设计从依赖断点转向基于组件、内在布局和容器查询的方法，以实现更灵活、可维护的界面。

- 📱 断点曾是响应式设计的主流方案，但现代组件化、嵌套式界面使其成为局部布局的“错误输入”
- 🧩 内在布局（如 `auto-fit` + `minmax()`）可让网格和弹性布局自动适应容器空间，无需断点
- 🔄 使用 `clamp()`、`min()`、`max()` 实现字号、间距等值的连续缩放，替代阶梯式断点
- 📦 容器单位（如 `cqi`）让组件尺寸基于自身容器而非视口，提升可复用性
- 🔧 容器查询用于真正的结构变化（如从列变行），且阈值绑定到组件自身
- 🎯 媒体查询应聚焦设备能力和用户偏好（如 `hover`、`prefers-reduced-motion`），而非布局
- ✅ 迁移清单：审计断点、替换标量分支、使用内在布局、引入容器单位、保留环境意图查询
- 💡 核心转变：从“断点编排”到“意图驱动”，组件默认自适应，断点仅作为精确的例外工具

---

### [我希望在批量制造 bug 之前有人告诉我的 10 个 React 技巧——Nechiu Dan](https://neciudan.dev/10-react-tips-that-actually-matter)

**原文标题**: [10 React tips I wish someone had told me before I mass-produced bugs — Neciu Dan](https://neciudan.dev/10-react-tips-that-actually-matter)

以下是对文章内容的总结：

本文分享了 10 个实用的 React 技巧，帮助开发者避免常见错误，提升代码质量和性能。

- 🧠 **使用 useReducer 管理复杂状态**：当多个 useState 状态相互依赖时，用 useReducer 确保状态组合始终有效，避免 UI 显示矛盾信息。
- ⏱️ **useTransition 处理渲染，debounce 处理网络**：useTransition 用于优化客户端渲染性能，debounce 用于减少网络请求频率，两者不可混用。
- 📍 **状态就近放置**：将状态下放到只依赖它的组件中，避免父组件重渲染影响无关子组件，比 React.memo 更简单有效。
- 🔄 **useEffect 是同步机制，不是生命周期**：useEffect 用于同步副作用与响应式值，而非模拟 componentDidMount；数据获取应交给专业库（如 React Query）。
- 🗝️ **不要用索引作为 key**：使用稳定唯一 ID 作为 key，避免列表操作（如删除）导致 DOM 节点错乱和输入状态丢失。
- 🔑 **key 属性可重置组件**：改变组件的 key 会强制卸载并重新挂载，省去手动重置状态的 useEffect。
- 🧩 **useMemo 并非免费**：对简单计算（如字符串拼接）使用 useMemo 反而增加开销，应通过性能分析后再决定是否使用。
- 📐 **单一职责原则：一个组件一个变更原因**：将数据获取与 UI 展示分离，让 API 变更只影响 hook，布局变更只影响组件。
- 🎨 **useLayoutEffect 消除闪烁**：在测量 DOM 并立即修改样式时用 useLayoutEffect，它在浏览器绘制前执行，避免视觉闪烁。
- 🧱 **使用复合组件模式替代复杂 props**：通过 Context 和子组件组合，让 API 更灵活，用户可自由定制每个部分的样式和内容。

---

### [一个基于 TypeScript 类的 React WebSocket 库](https://techhub.iodigital.com/articles/a-typescript-class-based-websocket-library-for-react/websockets)

**原文标题**: [A TypeScript Class-Based WebSocket Library for React](https://techhub.iodigital.com/articles/a-typescript-class-based-websocket-library-for-react/websockets)

本文介绍了一个基于 TypeScript 类和 TanStack Store 构建的 React WebSocket 库，旨在解决实时更新、订阅持久化和连接管理等实际问题。

- 📡 **单一连接复用**：每个 URL 只建立一个 WebSocket 连接，所有订阅和消息 API 共享该连接，减少资源浪费。
- 🔄 **自动重连与心跳**：支持指数退避重连、浏览器在线/离线事件处理，以及 40 秒心跳检测，确保连接稳定。
- 🧩 **类与钩子协同**：核心逻辑封装在 `WebsocketConnection`、`WebsocketSubscriptionApi` 和 `WebsocketMessageApi` 类中，React 钩子作为轻量包装，提供细粒度响应性。
- 🚀 **基于 TanStack Store 的响应性**：通过 Store 实现选择性订阅，仅当数据变化时触发重渲染，避免不必要的性能开销。
- 🔑 **订阅持久化**：订阅在页面间保持活跃，避免频繁订阅/取消订阅；最后一个钩子卸载后，延迟清除连接。
- 📨 **Promise 消息发送**：支持 `sendMessage` 和 `sendMessageNoWait`，可等待响应或即发即忘。
- 🛡️ **边缘情况处理**：包括缓存消息、`replaceUrl` 与 `reconnect` 防冲突、关闭码区分、请求覆盖、多初始化器警告等。
- 📦 **开源与安装**：库已开源在 GitHub，并发布为 npm 包 `@maxtroost/use-websocket`，方便集成。

---

### [AI 生成的用户界面默认不可访问 – 前端大师博客](https://frontendmasters.com/blog/ai-generated-ui-is-inaccessible-by-default/)

**原文标题**: [AI-Generated UI Is Inaccessible by Default – Frontend Masters Blog](https://frontendmasters.com/blog/ai-generated-ui-is-inaccessible-by-default/)

AI 生成的 UI 默认不可访问，但可通过五层强制系统确保语义正确性。

- 🧩 **问题核心**：AI 生成的 React 组件视觉完美，但无障碍树中元素角色、名称、状态缺失，导致屏幕阅读器用户无法使用。
- 🌳 **无障碍树原理**：浏览器构建独立于渲染树的无障碍树，包含角色、名称、状态、值四个属性，CSS 无法改变语义。
- 🤖 **AI 生成缺陷原因**：训练数据中语义 HTML 不足、视觉反馈循环、token 经济性、缺乏无障碍树模型。
- 📝 **第一层：提示约束**：通过项目级规则文件强制使用语义标签（如`<button>`、`<nav>`）、ARIA 属性、键盘交互和运动偏好。
- 🔍 **第二层：静态分析**：使用 ESLint 和 eslint-plugin-jsx-a11y 在编码阶段检测`<div onClick>`等常见错误。
- 🧪 **第三层：运行时测试**：通过 Playwright 和 axe-core 在浏览器中测试组件，验证无障碍树和键盘导航。
- 🔄 **第四层：CI 集成**：在 GitHub Actions 中运行 lint、单元测试和端到端测试，阻止不符合无障碍标准的 PR 合并。
- 🏗️ **第五层：组件抽象**：使用 Headless UI、Radix 或 React Aria 等库，将无障碍逻辑内置到组件 API 中。
- ⚠️ **常见失败模式**：模态框缺少焦点陷阱、图标按钮无标签、自定义下拉框无键盘导航，以及颜色对比度和运动敏感性问题。
- ⏱️ **成本与收益**：每组件增加 3-8 分钟检查，但可避免 45-90 分钟的后期修复，五层系统可覆盖 70-85% 的实际问题。

---

