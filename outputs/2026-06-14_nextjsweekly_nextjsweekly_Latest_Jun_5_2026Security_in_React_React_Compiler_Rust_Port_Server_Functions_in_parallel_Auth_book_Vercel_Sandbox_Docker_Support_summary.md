### [React 应用程序中的安全性 - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

**原文标题**: [Security in React Applications - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

### 概述总结  
本文详细介绍了 React 应用中的关键安全实践，涵盖 XSS 防护、安全认证、CSRF 保护、服务端输入验证及内容安全策略（CSP），强调多层防御的重要性。

- 🛡️ **React 内置 XSS 防护**：JSX 默认转义特殊字符（如`<`、`>`），防止脚本注入；但需警惕`dangerouslySetInnerHTML`会绕过此保护。
- 🧹 **使用 DOMPurify 净化 HTML**：必须通过 DOMPurify 库清理用户输入的 HTML 内容，移除危险标签和属性，避免 XSS 攻击。
- 🔐 **安全令牌存储**：避免将令牌存于`localStorage`或`sessionStorage`（易被 XSS 窃取），应使用`HttpOnly`、`Secure`、`SameSite=Strict`属性的 Cookie。
- 🚫 **CSRF 防护**：通过`SameSite=Strict`和自定义 CSRF 令牌（如`X-CSRF-Token`请求头）防止跨站请求伪造。
- ✅ **服务端输入验证**：使用 Zod 库在 Server Functions 中验证用户输入，并始终结合参数化查询防止 SQL 注入。
- 📜 **内容安全策略（CSP）**：通过 HTTP 头限制资源加载（如`script-src 'self'`），使用 nonce 允许内联脚本，并先以`Content-Security-Policy-Report-Only`测试策略。
- 🔗 **多层防御整合**：结合 React 内置保护、安全认证模式、服务端验证和浏览器级策略，才能构建安全的 React 应用。

---

### [[编译器] 将 React 编译器移植到 Rust —— josephsavona 提交的拉取请求 #36173 · react/react · GitHub](https://github.com/react/react/pull/36173)

**原文标题**: [[compiler] Port React Compiler to Rust by josephsavona · Pull Request #36173 · react/react · GitHub](https://github.com/react/react/pull/36173)

React 编译器已成功移植到 Rust，这是一个实验性项目，旨在提升性能并支持更多工具链集成。

- 🚀 **性能大幅提升**：Rust 版作为 Babel 插件运行时速度快 3 倍，实际转换逻辑快约 10 倍，原生集成（OXC、SWC）预计更快。
- 🧩 **架构与 API**：采用与 TypeScript 版相同的架构（HIR、CFG、SSA），但使用 arena 式数据结构适配 Rust 借用系统。公共 API 基于 Rust 版 Babel AST，各集成工具负责转换。
- ✅ **正确性验证**：所有 1725 个测试用例通过，生成代码和中间表示与 TS 版几乎一致。提供了多种测试脚本（snap、e2e、详细内部状态对比）。
- 🛠️ **集成与开发**：已包含 Babel、OXC、SWC 三种集成示例。计划未来实现自己的作用域分析，并改进 AST 表示（如 arena 分配、smol_str）。
- 🔄 **未来改进方向**：考虑将输出从 `Option<Program>` 改为补丁形式以提升效率，并可能实现自己的作用域解析。

---

### [一个功能完备的 TypeScript 存储 SDK——跨不同提供商的统一可移植接口](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-06-05)

**原文标题**: [A fully-featured TypeScript SDK for storage — one portable interface across different providers](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-06-05)

这是一个统一的 TypeScript 存储 SDK，支持快照、分叉和多存储提供商，专为人类和 AI 代理设计。

- 🔄 **统一 API**：跨所有提供商使用相同 API，切换提供商只需更改导入，调用点无需移动
- 📸 **快照与分叉**：内置快照和分叉功能，支持为代理创建沙盒环境，可合并或丢弃分叉
- 🤖 **AI 代理集成**：可无缝接入 Vercel AI SDK、Mastra 和 MCP 服务器，支持模型在编辑前创建快照
- 🖥️ **命令行工具**：`@storagesdk/cli`提供熟悉的 shell 命令（ls、cp、mv 等），支持`storage://`方案和管道操作
- 🌊 **流式传输**：支持 Web 流输入输出，`ReadableStream<Uint8Array>`下载和上传，背压和中断端到端传播
- 🔗 **签名 URL**：默认预签名 PUT，支持 POST 并设置 maxSize/contentType 约束
- 🛠️ **逃生舱**：通过`storage.raw`访问原生客户端，完全类型推断，无需类型转换
- ⏹️ **中止支持**：每个操作支持`AbortSignal`，可取消上传、列表扫描和快照
- ❌ **类型化错误**：使用`StorageError`代码（NotFound、Conflict 等），跨提供商保持可移植性
- 📦 **轻量高效**：ESM-only，Node 20+，核心零运行时依赖，适配器可选作为对等依赖

---

### [错误](https://github.com/vercel/next.js/pull/94277/changes)

**原文标题**: [Error](https://github.com/vercel/next.js/pull/94277/changes)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /vercel/next.js/pull/94277/changes (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [React 编译器渲染指南 - Mark Erikson - YouTube](https://www.youtube.com/watch?v=WsAmM-sx9kA)

**原文标题**: [A Guide to React Compiler Rendering - Mark Erikson - YouTube](https://www.youtube.com/watch?v=WsAmM-sx9kA)

本頁面概述了 YouTube 平台的基本資訊與相關政策，包括版權、聯絡方式、創作者支援及法律條款等。

- 📰 **新聞中心**：提供 YouTube 最新消息與公告。
- ©️ **版權**：說明內容使用與版權相關的規範。
- 📞 **聯絡我們**：提供用戶與平台聯繫的管道。
- 🎨 **創作者**：針對內容創作者提供的資源與支援。
- 📢 **刊登廣告**：說明廣告投放選項與合作方式。
- 👨‍💻 **開發人員**：提供 API 及技術整合資訊。
- 📜 **條款**：列出使用 YouTube 服務的相關條款。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：規範內容審查與平台安全措施。
- ⚙️ **YouTube 的運作方式**：解釋推薦系統與平台機制。
- 🧪 **測試新功能**：介紹正在測試中的新功能。
- ©️ **© 2026 Google LLC**：版權聲明，歸屬 Google 公司。

---

### [React 性能：停止记忆化，开始优化——Depender Sethi](https://www.sethi.io/blog/react-performance-from-sluggish-to-lightning)

**原文标题**: [React Performance: Stop Memoizing, Start Optimizing — Depender Sethi](https://www.sethi.io/blog/react-performance-from-sluggish-to-lightning)

### 概述总结
本文通过高速公路交通类比，介绍了 2026 年 React 性能优化的核心策略，强调移除不必要的工作而非盲目添加优化钩子。

- 🚗 **状态下移是关键**：将状态移到实际使用的组件中，避免整个子树不必要地重新渲染，这是最有效的性能优化手段。
- 🛣️ **Children 模式**：通过将子组件作为 props 传递，避免父组件状态变化时重渲染子组件，无需记忆化。
- 🚫 **停止过度记忆化**：React 编译器（React 19+）自动处理记忆化，手动使用`useMemo`和`useCallback`在大多数情况下已过时且可能适得其反。
- 🚀 **使用并发特性**：`useTransition`和`useDeferredValue`可让非紧急状态更新在后台处理，保持用户输入流畅，是当前最被低估的性能工具。
- 📦 **代码分割与懒加载**：按需加载页面和重型组件，避免一次性加载全部代码，但注意不要过度分割。
- 🔍 **先分析再优化**：使用 React DevTools Profiler、Chrome Performance 标签和 Core Web Vitals 指标定位真正的瓶颈，而非猜测。
- ⚠️ **避免常见陷阱**：不在组件内定义组件、使用稳定 key、合理拆分 Context、避免`useEffect`链、将静态 JSX 属性提取到组件外部。
- 📋 **速查表**：状态下移、使用并发特性、代码分割、避免`useEffect`链、拆分 Context、静态属性提取、组件外定义子组件、使用稳定 key、先分析后优化、让编译器处理记忆化。

---

### [Aiden Bai 在 X 上：“React 的 useEffect 存在的问题 https://t.co/DQ7JALF4KW” / X](https://x.com/aidenybai/status/2062202659143115216)

**原文标题**: [Aiden Bai on X: "the problem with React's useEffect https://t.co/DQ7JALF4KW" / X](https://x.com/aidenybai/status/2062202659143115216)

React 的 useEffect 存在设计缺陷，可能导致性能问题和难以调试的副作用。

- 🐛 依赖数组管理复杂，容易遗漏或错误添加依赖项，引发意外行为
- ⚡ 每次渲染后都会执行清理和重新运行，造成不必要的性能开销
- 🔄 副作用逻辑分散在多个 useEffect 中，难以追踪数据流和状态变化
- 🧩 与 React 的并发模式不兼容，可能导致过时闭包和状态不一致问题
- 🛠️ 调试困难，因为副作用执行时机与渲染周期紧密耦合

---

### [Pilcrow 的认证手册](https://auth.pilcrowonpaper.com/)

**原文标题**: [Pilcrow's auth book](https://auth.pilcrowonpaper.com/)

本手册是一份关于 Web 应用身份验证（Auth）的免费个人指南，重点涵盖登录系统、安全实践及完整示例。

- 📖 手册为个人编写的免费 Auth 指南，无广告，旨在帮助学习认证与网络安全。
- 🔐 核心聚焦于应用的认证与登录系统，更广泛安全主题可参考 OWASP 备忘单系列。
- 💬 支持通过 Discord 服务器或 GitHub Discussions 提问，并欢迎在 GitHub Sponsors 上赞助支持。
- 👤 由 Pilcrow 编写维护，源代码托管于 GitHub。
- 🗂️ 涵盖认证方法、会话管理、密码、CSRF、Passkeys、WebAuthn、ECDSA/EdDSA/RSA 签名等主题。
- 🌐 提供两个完整开源 Go 示例：基础密码认证（含邮箱验证与密码重置）及无密码认证（含 Passkey 与邮箱验证码登录）。

---

### [在 Vercel 沙箱内运行 Docker 容器 - Vercel](https://vercel.com/changelog/run-docker-containers-inside-vercel-sandbox)

**原文标题**: [Run Docker containers inside Vercel Sandbox - Vercel](https://vercel.com/changelog/run-docker-containers-inside-vercel-sandbox)

Vercel Sandbox 现已支持在沙箱内运行 Docker，可安全构建容器、安装系统包及修改文件，且不影响宿主机。

- 🐳 支持在沙箱内安装并运行 Docker 守护进程，实现容器化应用部署
- 🔧 通过代码示例展示完整流程：安装 Docker、启动守护进程、运行 Redis 容器并验证
- 🧪 适用于运行 Redis/Postgres 等测试依赖、验证容器镜像、预览容器化应用
- 💾 结合持久化沙箱，Docker 安装和拉取的镜像可在会话间保留
- 🚀 新增 FUSE 文件系统驱动和 VPN 客户端支持，拓展沙箱功能边界

---

### [更新日志 - shadcn/ui](https://ui.shadcn.com/docs/changelog)

**原文标题**: [Changelog - shadcn/ui](https://ui.shadcn.com/docs/changelog)

shadcn/ui 近期发布了多项重要更新，包括 GitHub 注册表、新样式、CLI 增强和包管理改进，旨在提升组件分发、定制化和开发效率。

- 🗂️ **GitHub 注册表**：支持将任何公共 GitHub 仓库作为组件注册表，可直接通过 CLI 安装组件、钩子、工具等，无需额外服务器。
- 🚀 **shadcn eject 命令**：将共享的 Tailwind CSS 内联到全局样式文件中，移除对 shadcn 包的依赖，适合希望减少外部依赖的项目。
- 🎨 **新样式 Rhea**：推出更紧凑的 Luma 变体 Rhea，保持圆角设计但缩小间距和控件尺寸，适合高信息密度的产品界面，且不改变 Tailwind 间距比例。
- 🔧 **注册表包含与验证**：支持通过`include`字段组合多个`registry.json`文件，并新增`shadcn registry validate`命令用于发布前验证注册表结构。
- 📦 **包导入与目标别名**：支持`package.json`中的`#imports`和`files.target`中的`@ui`等别名，简化组件安装路径和导入管理。
- ⚡ **其他更新**：包括预设、指针光标、部分预设应用、Sera 样式、组件组合、Luma 样式、CLI v4、RTL 支持、Blocks 更新等大量功能改进。

---

### [概述](https://legendapp.com/open-source/list/v3/overview/)

**原文标题**: [Overview](https://legendapp.com/open-source/list/v3/overview/)

### 概述
Legend List 是一款高性能虚拟列表组件，支持 React Native 和 React DOM，可替代 FlatList/FlashList，提供动态尺寸、聊天优化、双向无限滚动等高级功能，并已发布 v3 版本。

- 🚀 **高性能与低资源占用**：支持超快滚动和复杂组件，CPU 和内存使用率低于同类方案
- 📏 **动态尺寸无需手动测量**：自动适应内容变化，减少开发工作量
- 💬 **聊天与信息流原生支持**：提供 `initialScrollAtEnd`、`maintainScrollAtEnd`、`anchoredEndSpace` 等聊天专用功能
- 🔄 **双向无限滚动**：支持锚定滚动和分页加载，适用于时间线或动态列表
- 🧲 **粘性头部与 SectionList**：支持分组列表和始终挂载的行
- 🌐 **跨平台兼容**：同时支持 React Native、React DOM 和 React Native Web
- 🆕 **v3 新特性**：新增 Web 支持、`KeyboardAwareLegendList`、`SectionList` 组件、`alwaysRender` 和 `stickyHeaderConfig` 等
- ⚡ **异步滚动方法**：提供 `scrollToIndex`、`scrollToEnd` 等异步命令式 API
- 📊 **高级集成**：支持 `viewabilityConfig`、`getState()`、滚动指标和缓存清理

---

### [世博会观察](https://expo.dev/solutions/expo-observe?utm_source=nextjsweekly&utm_medium=email&utm_campaign=observe-beta)

**原文标题**: [Expo Observe](https://expo.dev/solutions/expo-observe?utm_source=nextjsweekly&utm_medium=email&utm_campaign=observe-beta)

### 概述总结
EAS Observe 是一款深度集成移动应用发布流程的性能监控工具，能自动将每次构建和更新与性能指标关联，帮助开发者快速发现回归问题，并支持一键将上下文传递给 AI 代理进行分析。

- 📊 **自动捕获用户真实体验指标**：无需自定义追踪，自动测量 TTI、冷热启动、帧率下降和包加载时间等关键性能数据。
- 🏗️ **每次发布都可见**：每个构建和 OTA 更新在时间轴上显示为标记，悬停查看变化，点击即可查看该版本的所有会话。
- 🤖 **一键移交 AI 分析**：从仪表盘或 CLI 输出 JSON 到 AI 代理，获取基于真实会话的精准分析。
- 🔍 **快速定位问题会话**：按指标降序排序，深入单个会话查看设备、系统、地区和更新渠道，结合日志事件追踪关键流程。
- 📉 **按路由分析性能瓶颈**：通过 Expo Router 集成，将交互时间按路由分解，快速找到拖慢应用的页面。
- 📱 **覆盖全设备范围**：自动捕获 P50、P90、P99 指标，涵盖低端硬件、旧系统和不稳定网络环境。
- ⚙️ **一行代码集成**：安装包并添加两行代码即可开始收集性能数据。
- 🔒 **数据隐私保障**：仅收集匿名性能数据（设备型号、系统版本、应用版本和安装 ID），不包含个人身份信息。
- 🔄 **与 Sentry/Datadog 互补**：Observe 专注于发布管道视角，能直接关联性能问题与具体构建/更新，而其他工具负责错误追踪和通用 APM。
- 📊 **可配置采样率**：通过`sampleRate`参数控制采样比例，且采样决策基于安装 ID 确定，确保同一设备在多个版本中保持采样一致性。

---

### [导致 60 帧卡顿的 DOM 操作：基于 275 个仓库的布局抖动与反模式基准研究](https://stackinsight.dev/blog/dom-manipulation-empirical-study/)

**原文标题**: [DOM Manipulation That Kills Your 60fps: A Benchmarked Study of Layout Thrashing and Anti-Patterns Across 275 Repositories](https://stackinsight.dev/blog/dom-manipulation-empirical-study/)

这是一份关于 DOM 操作性能的基准测试研究，分析了 275 个代码仓库中的布局抖动和反模式问题。

- 📊 **研究概述**：通过对 275 个真实仓库的 AST 扫描，发现 54.9% 的代码库存在至少一种 DOM 性能反模式，共检测到 2789 个问题，其中 35.4% 为高严重性问题。
- 🔥 **innerHTML 循环是性能杀手**：在 1000 个节点时，`innerHTML +=` 比优化版本慢 570 倍（223ms vs 0.39ms），在 10000 个节点时慢近 8000 倍（24.8 秒 vs 3.12ms），这是最严重的反模式。
- ⚡ **强制同步布局（布局抖动）**：在循环中读写布局属性会导致浏览器同步刷新渲染管线，10000 个节点时基线版本耗时 4.25ms vs 优化版 1.89ms，在 60fps 动画中会累积为明显的卡顿。
- 🎨 **循环中修改样式**：逐个设置元素样式属性比使用 CSS 类切换慢约 3 倍，10000 个节点时基线 15.18ms 接近帧预算上限。
- 🔍 **循环中 DOM 查询**：现代浏览器对重复元素查询有高效缓存，10000 个节点时仅差 0.69ms，性能影响最小。
- 📦 **appendChild 与 DocumentFragment**：现代浏览器已自动批处理 DOM 插入，DocumentFragment 不再有性能优势，两者速度几乎相同。
- 📈 **框架分布**：Vanilla JS 仓库平均每个有 38.9 个问题（最多），React 平均 7.1 个（但总量 558 个，占 20%），Angular 仅 0.7 个（因抽象层避免直接 DOM 操作）。
- 🏭 **顶级问题仓库**：Three.js（195 个）、Highcharts（156 个）、SortableJS（134 个）、AG Grid（133 个）等流行库存在大量反模式，可能影响使用它们的应用性能。
- ✅ **核心建议**：永远不要在循环中使用`innerHTML +=`；在写之前先读取布局属性；用 CSS 类替代循环中多属性样式修改；无需为性能使用 DocumentFragment；对依赖库运行 AST 扫描检测问题。

---

### [2026 年前端技术栈 - T 型开发者](https://thetshaped.dev/p/my-frontend-stack-in-2026-react-nextjs-pnpm-vite-ts-tailwind-storybook-tanstack-zustand-zod-oxlint-oxfmt-msw-vitest-playright-sentry)

**原文标题**: [My Frontend Stack In 2026 - The T-Shaped Dev](https://thetshaped.dev/p/my-frontend-stack-in-2026-react-nextjs-pnpm-vite-ts-tailwind-storybook-tanstack-zustand-zod-oxlint-oxfmt-msw-vitest-playright-sentry)

以下是您提供的文章摘要，概述了 2026 年前端技术栈的核心工具与选择理由。

2026 年前端技术栈：聚焦于实际生产应用中高效、可靠且易于组合的工具，每个工具都专注于做好一件事，并与其他工具无缝协作。

- 🏗️ **基础框架**：内容型网站用 Next.js，SPA 用 Vite 8 + Rolldown + TypeScript，包管理统一用 pnpm，安装快、省磁盘、原生支持工作区。
- 🎨 **样式与组件**：Tailwind CSS 处理样式，shadcn/ui 提供可复用的无障碍组件，代码归你所有，无依赖锁定风险。
- 📚 **组件文档**：Storybook 用于组件库的开发和文档，尤其适合与 shadcn/ui 搭配，但小项目可能维护成本过高。
- 🔄 **数据与路由**：TanStack Query 管理服务端状态，TanStack Router 提供端到端类型安全的路由，是 SPA 的优选。
- 🗂️ **客户端状态**：Zustand 用于跨组件或路由的共享状态，简单无样板代码；单组件状态仍用 useState。
- ✅ **运行时验证**：Zod 验证所有跨信任边界的数据（API 响应、表单输入、环境变量），弥补 TypeScript 运行时缺失。
- ⚡ **代码检查与格式化**：Oxlint + Oxfmt 基于 Rust，速度比 ESLint 快 50-100 倍，改变开发习惯，在保存时即可运行。
- 🧪 **测试与模拟**：Vitest 用于单元/组件测试，Playwright 用于端到端测试，MSW 在服务层拦截请求，三者配合实现快速、可靠的测试。
- 🐛 **生产监控**：Sentry 提供错误监控和会话回放，能快速定位真实用户问题，AI 摘要功能可自动分析会话。

---

### [从 Radix UI 迁移到 Base UI 的 9 个简单步骤](https://shadcnstudio.com/blog/migrate-from-radix-ui-to-base-ui/)

**原文标题**: [Migrate from Radix UI to Base UI in 9 Easy Steps](https://shadcnstudio.com/blog/migrate-from-radix-ui-to-base-ui/)

React 生态持续演进，Base UI 作为 Radix UI、Floating UI 和 Material UI 团队的合作成果，正迅速成为开发者青睐的现代 UI 原语库，shadcn/ui 现已官方支持。本指南详细介绍了从 Radix UI 迁移到 Base UI 的完整流程，包括 API 变化、组件差异和常见陷阱。

- 🚀 **Base UI 是进化而非竞争**：由 Radix UI 创始人、Floating UI 创建者和 Material UI 团队共同打造，旨在提供更清晰、更稳定的 React 组件基础。
- 🎯 **API 更明确**：用 `render` prop 替代了 Radix 的 `asChild` 模式，消除了“魔法”组合，使组件层级更直观。
- 📦 **依赖更简单**：从 Radix 的多个独立包（如 `@radix-ui/react-dialog`）统一为单个 `@base-ui/react` 包，支持 tree-shaking，易于版本管理。
- 🛠️ **迁移步骤清晰**：包括创建分支、更新 `components.json`、重新生成组件、手动更新自定义组件、替换 `asChild` 为 `render`、处理组件特有 API 差异（如 Accordion、Select、Tooltip 等）。
- 🔄 **状态样式需调整**：Radix 使用 `data-*` 属性，Base UI 改用 ARIA 属性（如 `aria-expanded`、`aria-disabled`），需更新 Tailwind 或 CSS 选择器。
- ⚠️ **常见陷阱与解决**：涵盖 TypeScript 类型错误、残留 CSS 选择器、缺失组件 props、构建错误和运行时警告，并提供具体解决方案。
- ✅ **何时迁移**：新项目建议直接选 Base UI；现有项目若稳定且资源有限可暂缓，但 Base UI 是 shadcn/ui 的未来方向。
- 🌐 **生态支持**：shadcn/ui 文档已提供 Base UI 示例，社区活跃，团队承诺长期维护，适合生产环境使用。

---

### [深入解析新版 Raycast 的技术细节 - Raycast 博客](https://www.raycast.com/blog/a-technical-deep-dive-into-the-new-raycast)

**原文标题**: [A Technical Deep Dive Into the New Raycast - Raycast Blog](https://www.raycast.com/blog/a-technical-deep-dive-into-the-new-raycast)

Raycast 2.0 是一次从底层到上层的全面重写，旨在实现跨平台运行（macOS 和 Windows），同时保持其标志性的快速、愉悦和原生体验。这次重写采用了混合技术栈，将 Web 技术的灵活性与原生平台的控制力相结合，并引入了新的 Rust 文件索引器来提升性能。

- 🚀 **跨平台重写**：从零开始构建，采用混合架构（Swift/C# 原生壳 + React/TypeScript 前端 + Node.js 后端 + Rust 核心），使 Raycast 能在 macOS 和 Windows 上运行，并共享大部分代码。
- 🧩 **技术栈选择**：放弃了纯原生或 Electron/Tauri 方案，转而使用系统 WebView（macOS 的 WKWebView 和 Windows 的 WebView2）来渲染 UI，以获得对原生 API 的完全访问和精细控制。
- ⚡ **性能与内存权衡**：v2 的内存占用（约 350-450 MB）高于 v1（约 200-300 MB），但通过优化（如压缩内存、惰性加载）和 Rust 索引器，在搜索速度和文本渲染上实现了显著提升。
- 🖥️ **原生体验细节**：通过消除光标指针、悬停高亮和闪烁等 Web 习惯，并让弹出窗口和设置作为原生窗口运行，确保应用感觉像原生 Mac 应用。
- 🔧 **WebKit 优化**：针对 WebKit 的节流、窗口调整大小和渲染问题进行了大量工作，例如禁用遮挡检测、预渲染内容和使用 `_doAfterNextPresentationUpdate` 来避免闪烁。
- 🗂️ **新文件索引器**：用 Rust 构建了自定义文件索引器，可直接扫描文件系统（Windows 上通过读取 MFT），实现秒级全盘索引，无需依赖 Spotlight。
- 💡 **开发效率提升**：热重载使 UI 更改在 1 秒内生效，大部分产品工作（前端和后端）在共享代码中进行，显著加快了功能发布和问题修复速度。
- ⚖️ **权衡与挑战**：虽然开发速度和跨平台能力提升，但带来了更高的内存基线、更复杂的调试流程（涉及四个运行时）以及需要处理 Windows 的硬件多样性。

---

