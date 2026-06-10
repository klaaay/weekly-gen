### [JavaScript 周刊第 789 期：2026 年 6 月 9 日](https://javascriptweekly.com/issues/789)

**原文标题**: [JavaScript Weekly Issue 789: June 9, 2026](https://javascriptweekly.com/issues/789)

以下是您提供的 JavaScript Weekly 第 789 期内容的总结：

VoidZero（Vite、Vitest 等工具的开发公司）加入 Cloudflare，所有项目保持 MIT 许可，Evan You 继续领导。Cloudflare 还设立了 100 万美元基金支持 Vite 生态。Angular v22 发布，带来了信号表单、Angular Aria 和异步响应式等稳定特性。Safari 27 beta 改进了 ESM 加载器和 WebAssembly 的 JSPI 支持。Electron 43 beta 性能大幅提升。React Compiler 的 Rust 端口即将合并。此外还有 TanStack Table v9 Beta、Node-RED 5.0 等新版本发布。

- 🚀 VoidZero 加入 Cloudflare，Evan You 坦言盈利困难，但项目保持 MIT 许可，团队继续自主运营
- 💰 Cloudflare 设立 100 万美元基金支持 Vite 生态维护者和贡献者
- 🅰️ Angular v22 正式版发布，信号表单、Angular Aria 和异步响应式三大特性稳定可用
- 🌐 Safari 27 beta 重写 ESM 加载器，提升 top-level await 支持，并新增 WebAssembly 的 JSPI 支持
- ⚡ Electron 43 beta 性能大幅提升，得益于嵌入式 Node.js 快照、V8 字节码缓存和链接时优化
- 🦀 React Compiler 的 Rust 端口即将合并，Meta 内部已看到“出色效果”
- 📊 TanStack Table v9 Beta 发布，支持 React、Vue、Angular、Svelte 等多种框架
- 🔧 Node-RED 5.0 发布，基于 Node.js 的低代码流程编程环境
- 📐 Geometric.js 库发布，用于处理多边形、边界框、旋转等几何运算
- 🪟 Micromodal.js 发布，轻量级无障碍模态对话框库，支持过渡动画和背景点击关闭
- 📄 PDFSlick 4.0 发布，支持 React、Solid、Svelte 等框架的 PDF 查看器，可处理多文档和注释
- ⚡ babel-plugin-zod-hoist 发布，将 Zod 模式定义提升到文件顶部以加速验证
- 🧪 eslint-plugin-functional 10.0 发布，禁止突变并鼓励函数式编程的 ESLint 规则
- 🧊 Draco.js 发布，mrdoob 为 three.js 开发的纯 JavaScript Draco 网格加载器

---

### [VoidZero 加入 Cloudflare | VoidZero](https://voidzero.dev/posts/voidzero-cloudflare)

**原文标题**: [VoidZero is Joining Cloudflare | VoidZero](https://voidzero.dev/posts/voidzero-cloudflare)

概述：VoidZero 宣布加入 Cloudflare，其开源项目将继续保持 MIT 许可，团队将专注于工具链开发，并与 Cloudflare 合作构建更好的开发者体验。

- 🚀 VoidZero 加入 Cloudflare，所有开源项目（Vite、Vitest、Rolldown、Oxc、Vite+）保持 MIT 许可，团队继续领导开发。
- 💡 核心目标：构建快速、统一的 JavaScript 工具链，解决生态系统中的性能问题。
- 📈 进展显著：Vite 周下载量超 1 亿次，Rolldown 成为 Vite 8 默认打包器，Oxc 工具链广泛使用。
- 🛠️ 推出新工具：Oxlint（50-100x 更快）、Oxfmt（30x 更快）、Vite+（统一 TypeScript 工具链）。
- 💰 盈利挑战：开源工具难以变现，尝试混合许可后放弃，最终开源 Vite+，并开发 Void 平台。
- 🤝 合作契机：与 Cloudflare 已有协作（Vite 环境 API、插件），收购后团队可专注工具开发，Cloudflare 成为 Vite 应用部署平台。
- 🌐 愿景一致：帮助开发者更高效，与 Cloudflare“构建更好互联网”使命契合，Cloudflare 承诺支持开源社区。
- 🤖 AI 趋势：工具被 AI 代理更多使用，未来将构建面向代理的工具，与 Cloudflare“代理云”战略协同。
- 🙏 致谢：感谢团队、投资者（Accel、Peak XV 等）和 Vite 社区的支持，将继续公开构建。

---

### [Cloudflare 支持 Vite 的使命 | Vite](https://vite.dev/blog/cloudflare-supports-vite)

**原文标题**: [Cloudflare supports Vite's mission | Vite](https://vite.dev/blog/cloudflare-supports-vite)

Cloudflare 宣布支持 Vite 的使命，并投资于 Vite 技术栈，Vite 保持开源、中立和社区治理不变。

- 🚀 Cloudflare 加入支持 Vite，VoidZero 团队加入 Cloudflare，继续推动 Vite 发展。
- 🔓 Vite 保持 MIT 开源许可，供应商中立，应用可运行在任何平台。
- 👥 Vite 团队由不同组织和独立成员组成，继续管理项目，Open Collective 资金由团队自主支配。
- 💰 Cloudflare 设立 100 万美元 Vite 生态系统开源基金，用于支持插件、工具、核心成员津贴等。
- 🛠️ 基金将加速生态改进：增强流行插件、支持独立成员、与 Rolldown/Oxc/Vite+ 团队合作、与框架/部署平台协作、采用新标准、提升安全审计速度。
- 🙏 感谢现有赞助商、贡献者（1250+）和社区反馈，推动 Vite 进步。
- 🔮 未来计划：Vite 8 的全捆绑模式、生态系统同步会议、Vite 9 稳定环境 API，持续构建 Web 平台。

---

### [POSETTE：Postgres 2026 活动 - POSETTE](https://posetteconf.com/2026)

**原文标题**: [POSETTE: An Event for Postgres 2026 - POSETTE](https://posetteconf.com/2026)

POSETTE 是由微软 Postgres 团队组织的免费虚拟开发者活动，将于 2026 年 6 月 16 日至 18 日举行，旨在汇聚 PostgreSQL 社区的知识与交流。

- 🐘 活动名称 POSETTE 代表 Postgres 开源生态系统讲座、培训与教育，包含 4 场独特直播
- 🎤 邀请顶尖 PostgreSQL 专家分享最新特性、性能技巧和实际应用案例
- 💬 通过 Microsoft Open Source Discord 的 #posetteconf 频道与演讲者实时互动
- 📅 四场直播时间：6 月 16 日 PDT、6 月 17 日 CEST 和 PDT、6 月 18 日 CEST，每场 8am–2pm
- 🗓️ 可查看日程、添加日历并注册获取更新，所有演讲会后可在线观看
- ❤️ 活动由热爱 PostgreSQL 的社区支持，可订阅新闻通讯获取最新消息
- 🌐 在 Discord、LinkedIn、X、Bluesky 和 Mastodon 上关注 #PosetteConf 加入对话
- 🏢 由微软 Postgres 团队主办，包括 Azure Database for PostgreSQL 和 Citus 等贡献者

---

### [宣布 Angular v22。今天，我们激动地宣布… | 作者：Angular | 2026 年 6 月 | Angular 博客](https://blog.angular.dev/announcing-angular-v22-c52bb83a4664?gi=e7404dd892d1)

**原文标题**: [Announcing Angular v22. Today, we are thrilled to announce the… | by Angular | Jun, 2026 | Angular Blog](https://blog.angular.dev/announcing-angular-v22-c52bb83a4664?gi=e7404dd892d1)

Angular v22 正式发布，带来多项生产就绪功能、AI 集成增强和 API 改进，旨在为开发者提供更稳定、高效和创新的开发体验。

- 🎉 三大核心功能进入生产就绪状态：Signal Forms（信号表单）、Angular Aria（无障碍原语）和 Asynchronous Reactivity（异步响应式 API，包括 resource 和 httpResource）
- 🤖 推出 Angular Agent Skills 和 WebMCP 实验性支持，增强 AI 代理在 Angular 开发中的能力，包括代码编写、浏览器工具和开发平台集成
- 🛠️ 路由增强：集成平台 Navigation API、新增 withExperimentalAutoCleanupInjectors 和 destroyDetachedRouteHandle 用于更好的内存管理
- ✨ 新装饰器 @Service 替代 @Injectable({ providedIn: 'root' })，简化全局单例定义
- ⚡ 引入 injectAsync 支持异步依赖注入，实现按需加载服务，提升应用性能
- 📝 模板改进：支持注释、宿主指令去重、展开语法、@switch 多 case 匹配和穷举检查、箭头函数
- 🔄 变更检测调整：OnPush 成为新应用默认策略，旧默认策略更名为 ChangeDetectionStrategy.Eager
- 🛡️ 预告 @boundary 错误边界 API（2026 年 Q3 开发者预览），可隔离组件故障并指定回退内容
- 🚫 弃用 Webpack 支持及相关构建工具，聚焦 TSGo 应用构建器
- 📅 官方发布活动将于 2026 年 6 月 5 日上午 9 点（太平洋时间）首映

---

### [带信号的表单 • Angular](https://angular.dev/essentials/signal-forms)

**原文标题**: [Forms with signals • Angular](https://angular.dev/essentials/signal-forms)

Angular Signal Forms 使用信号自动同步数据模型与 UI，提供响应式表单管理。

- 📝 **创建表单**：使用 `signal()` 创建数据模型，再通过 `form()` 函数生成字段树（FieldTree），支持点号访问字段。
- 🔗 **双向绑定**：通过 `[formField]` 指令将 HTML 输入与表单字段绑定，自动同步用户输入与数据模型。
- 📊 **读取字段值**：调用字段函数（如 `loginForm.email()`）获取 `FieldState` 对象，内含 `value()`、`valid()`、`touched()` 等信号。
- ✏️ **更新字段值**：使用 `value.set()` 方法编程更新字段值，自动同步底层模型信号。
- ✅ **验证与状态**：通过 `form()` 的第二参数（schema 函数）添加验证器（如 `required`、`email`），字段提供 `valid()`、`touched()`、`errors()` 等状态信号。
- 🎨 **支持多种输入**：兼容文本、数字、日期、复选框、单选按钮、下拉选择等标准 HTML 输入类型。
- 🔧 **自定义错误**：验证器支持自定义错误消息（如 `{message: 'Email is required'}`）。
- 🚀 **进阶功能**：支持去抖（`debounce`）、异步验证、依赖注入模块化设计，以及字段可见性管理。

---

### [Angular Aria • 概述 • Angular](https://angular.dev/guide/aria/overview)

**原文标题**: [Angular Aria • Overview • Angular](https://angular.dev/guide/aria/overview)

Angular Aria 是一套無頭、可存取的 Angular 指令，實作 WAI-ARIA 模式，讓開發者只需提供 HTML 結構、CSS 樣式和業務邏輯。

- 🧩 **無頭可存取指令**：Angular Aria 提供一系列無頭指令，自動處理鍵盤互動、ARIA 屬性、焦點管理和螢幕閱讀器支援。
- 📦 **簡易安裝**：可透過 npm、yarn、pnpm 或 bun 安裝 `@angular/aria` 套件。
- 🛠️ **實際範例**：以工具列選單為例，展示如何用 `ngToolbar`、`ngToolbarWidget` 和 `ngToolbarWidgetGroup` 指令建立可存取的文字格式化工具列。
- 🎨 **自訂樣式**：開發者只需提供 CSS 樣式（如材質、復古風格），即可打造符合品牌需求的介面。
- 🧠 **解決複雜問題**：自動處理鍵盤導航、螢幕閱讀器公告、焦點管理和從右至左語言支援等無障礙挑戰。
- 📋 **包含多種模式**：涵蓋搜尋與選擇（如自動完成、清單方塊）、導航與動作（如選單、工具列）、內容組織（如手風琴、分頁標籤、樹狀檢視）等常見互動模式。
- ✅ **適用場景**：適合建立設計系統、企業元件庫或需要自訂品牌樣式的無障礙元件。
- ❌ **不適用場景**：若需預先設計好樣式的元件（建議用 Angular Material）、簡單表單或快速原型開發，則不建議使用。

---

### [使用资源实现异步响应式 • Angular](https://angular.dev/guide/signals/resource)

**原文标题**: [Async reactivity with resources • Angular](https://angular.dev/guide/signals/resource)

### 概述总结
本文介绍了 Angular 中如何使用 `Resource` 实现异步数据的信号式响应式处理，包括创建资源、加载器配置、请求中止、手动重载、状态管理以及资源组合等核心功能。

- 🔄 **Resource 核心概念**：通过 `resource()` 函数将异步数据（如 HTTP 请求）集成到信号式代码中，支持同步访问 `value` 信号。
- ⚙️ **参数与加载器**：`params` 定义响应式计算，`loader` 是异步函数，当 `params` 变化时自动触发加载。
- 🛑 **请求中止**：利用 `abortSignal` 配合 `fetch` 等 API 自动取消过时的请求，提升性能。
- 🔁 **手动重载**：调用 `reload()` 方法可强制重新执行加载器，刷新数据。
- 📊 **状态管理**：通过 `status`、`hasValue`、`isLoading`、`error` 等信号获取加载状态（如 `'idle'`、`'loading'`、`'resolved'`），便于 UI 条件渲染。
- 🌐 **httpResource**：基于 `HttpClient` 的封装，提供信号化的 HTTP 请求状态和响应。
- 🧩 **资源组合**：利用 `snapshot` 属性和 `resourceFromSnapshots` 实现资源的状态组合，例如在加载新数据时保留旧值。

---

### [导航 API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API)

**原文标题**: [Navigation API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API)

Navigation API 是 2026 年 1 月起可用的新 Web 平台功能，用于管理浏览器导航，特别针对单页应用（SPA）的需求设计。

- 🌐 **核心功能**：通过 `Window.navigation` 属性访问全局 `Navigation` 对象，提供导航启动、拦截和管理能力。
- 🎯 **导航处理**：`navigate` 事件可集中控制所有导航，`intercept()` 方法允许自定义导航行为（如加载内容或重定向）。
- 📜 **历史记录管理**：每个导航创建 `NavigationHistoryEntry`，支持 `navigate()`、`reload()`、`back()` 等方法遍历和更新历史。
- 💾 **状态存储**：通过 `getState()` 和 `updateCurrentEntry()` 管理历史条目状态，支持独立于导航的状态更新。
- ⚠️ **局限性**：首次加载不触发 `navigate` 事件；仅限单帧操作；无法编程修改历史列表。
- 🛠️ **接口支持**：包含 `NavigateEvent`、`Navigation`、`NavigationHistoryEntry` 等接口，以及 `Window.navigation` 扩展。
- 📊 **浏览器兼容性**：2026 年 1 月起最新设备和浏览器版本支持，旧设备可能不兼容。
- 🔗 **相关资源**：提供实时演示、规范链接和“现代客户端路由”文章等参考资料。

---

### [WWDC26 新闻：Safari 27 测试版中的 WebKit | WebKit](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/#javascript)

**原文标题**: [  News from WWDC26: WebKit in Safari 27 beta | WebKit](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/#javascript)

Safari 27 beta 发布，包含 58 项新功能、525 项修复和 4 项弃用，重点提升现有功能的正确性和标准合规性。

- 🎨 **自定义 Select 元素**：新增 `appearance: base-select` 和伪元素，无需 JavaScript 即可完全自定义下拉菜单样式，同时保留原生可访问性和表单功能。
- 📌 **滚动锚定**：自动调整滚动位置，防止内容加载时页面跳动，提升用户体验。
- 🔗 **变换感知锚点定位**：锚点元素应用 CSS 变换后，定位元素能正确跟随其变换后的位置。
- 🏷️ **CSS 新特性**：新增 `:heading` 伪类、`revert-rule` 关键字、`stretch` 关键字等，简化样式编写并增强控制。
- ⚡ **WebAssembly JSPI**：支持 JavaScript Promise 集成，让 Wasm 代码能参与异步操作，简化移植。
- 📜 **ES 模块加载器重写**：完全符合标准的 C++ 实现，修复顶级 await 的执行顺序和初始化问题。
- 🌐 **WebGPU 与 WebXR**：支持 `clip_distances` 内置值和 visionOS 沉浸式网站环境，增强 3D 和空间计算能力。
- 📺 **媒体与 WebRTC 改进**：支持 `TextTrackCue.endTime = Infinity`、`targetLatency` 等，提升流媒体和实时通信能力。
- 🛠️ **Web Inspector 增强**：颜色选择器显示对比度信息、网络标签显示重定向链、元素标签添加子网格徽章等，简化调试。
- 🔒 **安全与网络**：支持 loopback 主机的 Secure cookie、修复 IDN 同形异义字攻击等。
- ♿ **可访问性修复**：大量修复 VoiceOver、`aria-labelledby`、`aria-owns` 等问题，提升辅助技术兼容性。

---

### [WWDC26 新闻：Safari 27 测试版中的 WebKit | WebKit](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/#webassembly)

**原文标题**: [  News from WWDC26: WebKit in Safari 27 beta | WebKit](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/#webassembly)

Safari 27 beta 版本发布，包含 58 项新功能、525 项修复和 4 项弃用，重点提升了 WebKit 的质量、标准合规性和跨浏览器兼容性。

- 🎨 **自定义 Select 元素**：新增 `appearance: base-select` 和伪元素，无需 JavaScript 即可完全自定义下拉菜单样式，同时保留原生可访问性和表单功能。
- 📌 **滚动锚定**：自动调整滚动位置，防止内容加载时页面跳跃，提升懒加载图片和动态内容页面的浏览体验。
- 🌐 **WebAssembly JSPI**：支持 JavaScript Promise 集成，让同步代码风格的 Wasm 模块能等待异步 Promise，简化 C/C++/Rust 代码移植。
- 🧩 **CSS 增强**：包括变换感知锚点定位、`:heading` 伪类、`revert-rule` 关键字、`stretch` 盒尺寸关键字，以及荷兰语 IJ 连字的正确大写处理。
- 🖥️ **子像素内联布局**：文本和内联元素可实现设备像素级精确定位，提升布局准确性。
- ⚡ **JavaScript 顶层 Await**：完全重写 ES 模块加载器，修复模块执行顺序和初始化问题，确保与标准兼容。
- 🎮 **空间 Web**：visionOS 支持沉浸式网站环境，iOS/iPadOS/macOS 新增 `<model>` 元素用于嵌入 3D 内容。
- 🛠️ **Web Inspector 改进**：颜色选择器内联显示对比度信息，网络标签显示完整重定向链，元素标签新增子网格和网格线徽章。
- 🔧 **大量修复**：涵盖 CSS、HTML、JavaScript、Web API、渲染、SVG、可访问性等领域的 525 项错误修复，提升稳定性和标准一致性。

---

### [发布 electron v43.0.0-beta.1 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v43.0.0-beta.1)

**原文标题**: [Release electron v43.0.0-beta.1 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v43.0.0-beta.1)

Electron v43.0.0-beta.1 版本发布，包含多项修复与性能优化。

- 🛠️ 修复：分离的 DevTools 窗口中右键菜单现在正确聚焦到 DevTools 窗口本身，而非被检查页面。
- ⚡ 性能：macOS 构建启用了 ThinLTO 优化，提升运行效率。
- 🐛 修复：解决了 Apple Silicon 上 `Buffer`/`TextEncoder` API 的静默数据截断问题，以及 `fs.writeFileSync` 处理非 ASCII 字符串时的崩溃。
- 🚀 启动优化：主进程从内嵌 Node.js 启动快照启动，框架包和预加载脚本缓存为编译后的 V8 字节码，沙盒渲染器启动数据提前推送，预加载堆栈跟踪显示正确的文件路径和行号。
- 🔧 构建优化：Linux 和 Windows 发布版启用了 ThinLTO 链接时优化。
- ⚙️ 运行时性能：整体运行时性能得到提升。
- 🗑️ 移除：Linux 上 `dialog` API 移除了 `showHiddenFiles` 支持。
- 🔄 更新：Chromium 升级至 150.0.7863.0。

---

### [[编译器] 由 josephsavona 将 React 编译器移植到 Rust · 拉取请求 #36173 · react/react · GitHub](https://github.com/react/react/pull/36173#issuecomment-4608356402)

**原文标题**: [[compiler] Port React Compiler to Rust by josephsavona · Pull Request #36173 · react/react · GitHub](https://github.com/react/react/pull/36173#issuecomment-4608356402)

React 编译器已成功从 TypeScript 移植到 Rust，这是一个实验性的工作版本，所有测试均已通过，性能显著提升。

- 🚀 **性能大幅提升**：作为 Babel 插件运行时速度提升 3 倍，实际转换逻辑快约 10 倍，与 OXC/SWC 原生集成将更快。
- 🧪 **全部测试通过**：1725 个 fixture 全部通过，包括代码输出和编译器中间状态的逐遍对比，与 TS 版本几乎一致。
- 🤖 **AI 辅助开发**：架构由人类主导，但大部分代码由 AI 编写，人类密切监督代码质量和测试策略。
- 🔧 **架构保持一致**：Rust 版本沿用与 TypeScript 版本相同的架构（HIR、CFG、SSA），主要区别在于使用 arena 结构适应 Rust 的借用系统。
- 🔗 **三种集成方式**：提供 Babel 插件、OXC 和 SWC 三种前端集成示例，未来计划移除 Babel 插件，仅保留原生集成。
- 🎯 **公共 API 设计**：使用 Rust 表示的 Babel AST 作为公共 API，各集成负责转换，未来编译器可能自行计算作用域信息。
- 🛠️ **未来改进方向**：计划返回补丁而非整个程序、优化 AST 表示（arena 分配、smol_str）、实现自己的作用域解析。
- 🤝 **合作伙伴邀请**：欢迎 OXC 和 SWC 等工具团队参与集成，每个集成将在 React 仓库中维护对应的 crate。

---

### [TanStack Table V9：成型 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-taking-form)

**原文标题**: [TanStack Table V9: Taking Form | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-taking-form)

TanStack Table V9 Beta 正式发布，带来多项重大改进，包括全新的状态管理系统、更好的性能和更灵活的扩展性。

- 🎉 **V9 Beta 发布**：经过长时间开发，TanStack Table V9 Beta 版本终于发布，解决了 V8 中的多个核心问题。
- 🔧 **状态管理革新**：采用 TanStack Store 作为底层状态管理，支持原子状态和选择器订阅，兼容 React Compiler 并提升性能。
- ⚡ **性能与内存优化**：通过共享原型、减少不必要分配和优化记忆化，大幅降低大型虚拟化表格的内存和 CPU 使用。
- 📦 **可摇树优化**：功能模块化设计，按需导入特性（如排序、分页），减少打包体积，同时保持类型安全。
- 🧩 **自定义扩展**：提供清晰的功能扩展模型，允许开发者创建自定义特性，与内置特性使用相同 API。
- 🔄 **可复用表格代码**：新增 `createTableHook` 和 `tableOptions`，便于跨项目共享表格配置、组件和默认选项。
- 🛠️ **全新开发者工具**：集成真实 Devtools 面板，支持表格状态、派生数据实时检查，且开发环境默认不打包到生产。
- 📚 **迁移与文档**：提供 V8 到 V9 的完整迁移指南，并重写文档，包含多个框架的 Kitchen Sink 示例。

---

### [版本 5.0 发布：Node-RED](https://nodered.org/blog/2026/06/09/version-5-0-released)

**原文标题**: [Version 5.0 released : Node-RED](https://nodered.org/blog/2026/06/09/version-5-0-released)

Node-RED 5.0 正式发布，这是项目历史上编辑器体验最大的一次变革，重点改进了用户界面、节点外观、功能增强和项目基础设施。

- 🎉 **编辑器全面现代化**：重新设计了侧边栏，支持垂直分割同时显示两个面板，并可直接拖拽面板进行布局调整。
- 🌗 **内置深色主题**：新增内置深色主题，可根据浏览器/系统偏好自动切换，也支持手动选择。
- ♿ **无障碍性大幅提升**：增加了 ARIA 属性、改进了下拉菜单的触摸和滚动体验，并优化了对比度。
- 🔍 **节点选择与导航优化**：选中节点显示蓝色光晕，新增“缩放至适配”按钮，支持空格键 + 左键平移。
- 📝 **节点文档徽章**：有额外文档的节点会显示徽章，点击即可弹出文档。
- 🚦 **功能增强**：新增调试侧栏暂停功能、Function 节点可调用 Link 节点并等待响应、节点选择列表按字母排序、Delay 节点支持突发模式。
- 🔒 **安全与 TLS 更新**：支持 PFX/P12 文件、环境变量加载证书，HTTP 请求节点可设置 SNI 服务器名，OAuth 改用令牌交换模式。
- ⚙️ **底层升级**：最低支持 Node.js 22.9.0，推荐使用 Node.js 24；npm 成为显式依赖；开发环境从 Grunt 迁移至 npm 脚本，并改用 ESLint。
- 🤝 **社区贡献**：感谢所有贡献者，包括错误修复、功能、文档和翻译。

---

### [发布 v1.1.0 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.1.0)

**原文标题**: [Release v1.1.0 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.1.0)

Rolldown v1.1.0 版本发布，包含默认行为变更、新功能、错误修复和性能优化。

- 🚀 **默认启用 lazyBarrel 优化**：跳过未使用的重导出模块编译，提升大型代码库构建速度，可通过 `experimental.lazyBarrel: false` 关闭。
- 📝 **tsconfig 项目引用解析对齐 TypeScript**：修复路径别名和 `allowJs` 优先级问题，更符合 `tsc` 行为，提供向后兼容方案。
- 🆕 **新增 import.meta.glob 支持 caseSensitive 选项**：允许在 glob 匹配中区分大小写。
- ⚠️ **增加 SOURCEMAP_BROKEN 警告**：在 `renderChunk` 和 `transform` 钩子中检测到源映射损坏时发出警告。
- 🐛 **修复多个错误**：包括缺失 tsconfig 文件报告、浏览器导出一致性、JSON 默认导入 `.default` 访问保留等。
- ⚡ **性能优化**：避免不必要的中间源映射生成，提升构建效率。
- 🔧 **依赖更新**：升级 oxc_resolver、oxc、pnpm、Rust 等核心依赖至最新版本。

---

### [pnpm 11.5 | pnpm](https://pnpm.io/blog/releases/11.5)

**原文标题**: [pnpm 11.5 | pnpm](https://pnpm.io/blog/releases/11.5)

pnpm 11.5 版本发布，新增 hoistingLimits 设置、替换交互提示库、改进信任机制，并修复多项安装与 dist-tag 问题。

- 🚀 新增 `hoistingLimits` 设置，控制依赖提升范围（支持 none、workspaces、dependencies 三种模式）
- 🖥️ 用 `@inquirer/prompts` 替换 `enquirer`，修复长列表滚动溢出问题，支持 Vim 风格导航键
- 🛡️ 分阶段发布在信任体系中获最高评级（高于可信发布者和来源证明），防止信任降级误报
- 🔧 修复别名安装时因深层依赖循环导致的 pnpm 挂起问题
- 🔑 修复 `dist-tag add/rm` 缺少 OTP 时的失败问题，现支持浏览器双因素认证
- 📦 修复 `minimumReleaseAgeExclude` 处理，避免排除包被锁定到过时版本
- 🔒 修复远程 tarball 依赖的 integrity 字段在后续安装中被丢弃的问题
- ♻️ 当 `pnpm-lock.yaml` 缺失但 `node_modules/.pnpm/lock.yaml` 存在时，跳过依赖重解析，直接复用快照

---

### [RunJS - 桌面端的 JavaScript 游乐场](https://runjs.app/)

**原文标题**: [RunJS - JavaScript Playground for Your Desktop](https://runjs.app/)

RunJS 是一款支持快速运行 JavaScript 代码的桌面应用，提供定价、文档、博客、联系和下载功能。

- 💻 提供桌面应用，支持快速运行 JavaScript 代码
- 💰 包含定价页面，可能提供免费或付费版本
- 📚 拥有文档、博客和联系功能，方便用户学习与支持
- ⬇️ 提供下载选项，便于用户安装使用

---

### [发布 6.0.0 · emscripten-core/emscripten · GitHub](https://github.com/emscripten-core/emscripten/releases/tag/6.0.0)

**原文标题**: [Release 6.0.0 · emscripten-core/emscripten · GitHub](https://github.com/emscripten-core/emscripten/releases/tag/6.0.0)

Emscripten 6.0.0 版本发布，包含多项重要更新和改进。

- 🖥️ Windows 平台改用 `.exe` 工具启动器，替代原有的 `.bat` 和 `.ps1` 文件，旧脚本需更新为 `emcc` 或 `emcc.exe`，但可通过运行 `tools/maint/create_entry_points.py --bat-files` 临时获取旧 `.bat` 文件。
- 📦 流式 Fetch 操作的最大块大小限制为 8 MB，防止大文件一次性传输导致 WebAssembly 内存溢出，确保流式传输持续进行。
- 🌐 提升最低浏览器引擎版本：Chrome 74→85、Firefox 68→79、Safari 12.2→14.1，移除 Babel 转译支持，默认启用 mutable-globals 和 sign-ext 特性，旧浏览器需手动转译输出。
- 📚 musl libc 从 v1.2.5 更新至 v1.2.6，libpng 端口从 1.6.55 更新至 1.6.58。
- 🔧 `-m64` 编译器标志现被支持，作为 `-sMEMORY64` 和/或 `--target=wasm64` 的别名。
- 💾 IDBFS 挂载的自动持久化功能新增全局回调 `IDBFS.onAutoPersistStateChanged = active => {}`，用于通知所有 IDBFS 同步开始和结束事件。
- 🛠️ google-closure-compiler 更新至 20260429.0.0，新增原生 macOS arm64 二进制文件，其他平台需下载 Java SE Development Kit 21.0.11。
- 🔗 `FAKE_DYLIBS` 设置默认禁用，`-shared` 默认生成真实动态库（隐含 `-sSIDE_MODULE`），链接真实动态库时自动生成动态链接程序（隐含 `-sMAIN_MODULE=2`）。
- 🧵 `PThread.runningWorkers` 字段已移除，可改用 `PThread.pthreads` 对象。
- ⏸️ POSIX `pause()` 函数现在返回 0 而非 EINTR。
- 👥 新贡献者：@HCL-JasonR、@vittorioromeo、@soilSpoon、@garymathews、@guybedford。

---

### [现代工程价值观 | 克里斯托夫·中泽](https://cpojer.net/posts/modern-engineering-values)

**原文标题**: [Modern Engineering Values | Christoph Nakazawa](https://cpojer.net/posts/modern-engineering-values)

### 概述总结
作者分享了在 2026 年使用 LLM（如 Codex CLI）进行编程的实践，强调 AI 代理已极大提升开发效率，并探讨了现代工程价值观：强所有权、品味、严格护栏与快速反馈、代码库上下文、自主掌控技术栈、选项价值。作者认为，编程已从手动编写代码转向指导 AI 系统，管理需更技术化，团队应小型化以保持速度。

- 🚀 **AI 代理大幅提升效率**：作者 90% 以上代码由 AI 编写，如修复 70 个 bug、实现新功能，日代码量从 1200 行增至十倍，质量更高。
- 🛠️ **工作流程优化**：使用 Codex CLI，每项目独立窗口，通过“先提案后执行”和“强制创建失败测试”确保正确性，使用 Codiff 审查代码。
- 👑 **强所有权**：工程师需深度理解产品、架构和方向，AI 放大所有权效应，小团队（2-3 人）配合独立仓库最有效。
- 🎨 **品味至关重要**：低容忍“废话”，聚焦于“值得做的事”，品味决定产品价值和团队时间分配。
- 🔒 **严格护栏与快速反馈**：强约束（如 lint、自动化测试）和快速工具（如基于变更文件操作）使 AI 代理迭代更快，从 1 分钟到 60 分钟不等。
- 📂 **代码库即上下文**：将所有相关上下文（设计、价值观、原则）放入仓库，减少分散信息，优化可读性，便于 AI 和人类理解。
- 🔧 **自主掌控技术栈**：减少第三方依赖，自建核心库（如数据、UI 库），降低复杂度，提升控制力。
- 💡 **选项价值**：任何变更应保留未来改进选项，避免“陷入死角”，适应持续变化。
- 👔 **管理需更技术化**：管理者必须保持领域专长，能自信修改代码，提供技术领导，而非仅负责方向。
- ⏱️ **速度对比**：过去 30 天 770 次提交，日均修改 15k 行代码（是两年前的 3 倍），但瓶颈从编码转向判断力。

---

### [命运](https://fate.technology/)

**原文标题**: [fate](https://fate.technology/)

概述总结  
视图组合通过将组件的数据需求声明在本地“视图”中，将每个屏幕的请求合并为单一请求，从而减少网络请求并消除瀑布效应。

- 🎑 视图组合：组件使用本地“视图”声明数据需求  
- 📦 单一请求：每个屏幕的视图被组合成一个请求  
- 🌐 减少网络请求：最小化网络请求数量  
- 🚫 消除瀑布效应：避免数据请求的连锁等待问题

---

### [我希望 Deno 能继续做它最擅长的事](https://hackers.pub/@hongminhee/2026/i-wish-deno-would-keep-doing-what-it-does-best)

**原文标题**: [I wish Deno would keep doing what it does best](https://hackers.pub/@hongminhee/2026/i-wish-deno-would-keep-doing-what-it-does-best)

### 概述总结
作者回顾了自己从 Python/Haskell 转向 TypeScript 的历程，最初被 Deno 零配置、基于 Web 标准的设计所吸引，但如今对 Deno 逐渐向 Node.js 兼容性靠拢感到失望。他认为 Deno 正在放弃最初的优势（工具链集成、Web 标准优先），转而追赶 Node.js，而 Node.js 反而正向 Deno 靠拢。作者担心 Deno 在投资者压力下偏离了初心，并坦言自己作为忠实用户也开始退缩。

- 🚫 **零配置的吸引力**：Deno 消除了 TypeScript 入门所需的繁琐配置（tsconfig.json、ESLint 等），只需`deno run main.ts`即可运行。
- 🌟 **Web 标准优先**：内置`fetch()`、Web Crypto API，支持 URL 导入 ESM，MDN 文档即官方文档，单二进制集成`deno fmt/lint/test/bench/check`。
- 🔄 **向 Node.js 靠拢**：支持 npm 说明符、`node_modules`、`node:*`模块，`deno add`默认添加 npm 包，JSR 被边缘化，导致 Deno 失去独特性。
- 🕰️ **时间压力**：Deno Land Inc.作为风投公司面临投资者压力，不得不追求短期可见成果（如 Node.js 兼容性），而非坚持长期战略。
- ⚔️ **错失的战场**：本可凭借`deno fmt/lint`等工具成为 Node.js 生态的“特洛伊木马”，但未抓住机会，而 Biome 等替代工具已崛起。
- 😟 **忠实用户的退缩**：作者自己也开始使用`node:test`、`node:sqlite`等跨运行时方案，对 JSR 和 Deno KV 的热情消退。
- 💔 **初心渐远**：Deno 最初设定议程（Web 标准、权限模型、URL 导入），如今却转向追赶生态，让早期支持者感到迷茫。

---

### [世博会观察](https://expo.dev/solutions/expo-observe?utm_source=jsweekly&utm_medium=email&utm_campaign=observe-beta)

**原文标题**: [Expo Observe](https://expo.dev/solutions/expo-observe?utm_source=jsweekly&utm_medium=email&utm_campaign=observe-beta)

### 概述总结
EAS Observe 是一款深度集成于移动应用发布流程的性能监控工具，能自动将每次构建和更新与性能指标关联，快速定位回归问题，并支持一键将数据传递给 AI 进行分析。

- 📊 **自动关联发布与性能**：每次构建和 OTA 更新都会在性能时间线上生成标记，悬停显示变化，点击即可查看该版本的所有会话数据。
- 📱 **真实用户感知测量**：自动捕获 TTI、冷/热启动、帧率、包加载时间等指标，无需自定义追踪代码。
- 🤖 **一键 AI 交接**：在仪表盘或 CLI 中一键将 JSON 数据传递给 Claude Code、Cursor 等 AI 代理，获得基于真实会话的精准分析。
- 🔍 **深入问题会话**：按指标排序筛选最慢的会话，查看设备、OS 版本、国家、更新渠道等详细信息，并追踪从启动到交互的完整事件时间线。
- 🧭 **屏幕级性能分析**：通过 Expo Router 集成，将交互时间分解到具体路由，快速定位导致卡顿的屏幕。
- 📈 **全面数据覆盖**：自动捕获 P50/P90/P99 百分位数据，涵盖低端设备、旧版 OS 和不稳定网络环境。
- ⚡ **极简集成**：只需安装 expo-observe 包并添加两行代码，即可开始采集 TTI 和路由性能数据。
- ❓ **常见问题解答**：Observe 与 Sentry/Datadog 互补，支持采样率设置（0-1），仅限 Expo SDK 55+ 和 EAS 用户，不收集个人身份信息。

---

### [关于 AI、开源与 Anthropic，Bun 能告诉我们什么——生态系统](https://redmonk.com/sogrady/2026/06/04/bun-two-lessons/)

**原文标题**: [What Bun Can Tell Us About AI, Open Source and Anthropic – tecosystems](https://redmonk.com/sogrady/2026/06/04/bun-two-lessons/)

Anthropic 收购 Bun 后，项目从人类主导转向 AI 主导开发，引发关于开源治理与 AI 影响的讨论。

- 🤖 **AI 贡献激增**：Bun 的代码提交从 2024 年 8 月起超半数由 AI 完成，收购后 AI 提交占比常超 80%，人类贡献者数量减半。
- 📈 **增长强劲但存疑**：Bun 的 npm 安装量从 44.5 万/月增长 16 倍至 730 万/月，TypeScript 类型定义增长超 50 倍，但增长可持续性受 AI 依赖影响。
- 🏢 **团队流失**：收购前约 7 名 Oven 员工中至少 4 人已离开，外部贡献者大幅减少，承诺的“同一团队”未兑现。
- 🔓 **开源承诺部分履行**：Bun 保持 MIT 开源、活跃维护和 GitHub 公开开发，但外部贡献下降，项目控制权集中于 Anthropic。
- ⚖️ **治理挑战**：Anthropic 对 MCP 标准化的拖延（历时 13 个月才捐赠）表明其开源成熟度不足，Bun 的未来可能面临类似治理困境。
- 🧩 **企业用户顾虑**：企业倾向选择基金会托管的项目以避免单供应商控制，Bun 若仅作为 Anthropic 内部基础设施，可能限制其外部采用。

---

### [17 个 TanStack 项目齐聚一个应用！- YouTube](https://www.youtube.com/watch?v=J4kzovOTNKw)

**原文标题**: [All 17 TanStack Projects In ONE App! - YouTube](https://www.youtube.com/watch?v=J4kzovOTNKw)

本頁面為 YouTube 平台的資訊與政策總覽，涵蓋版權、聯絡方式、條款及安全等核心內容，並標示為 Google 旗下服務。

- 📰 提供新聞中心與創作者相關資訊
- ©️ 明確版權歸屬與聯絡我們的方式
- 📢 說明廣告刊登與開發人員選項
- 📜 列出使用條款、私隱及安全政策
- ⚙️ 解釋 YouTube 的運作方式與新功能測試
- 🗓️ 版權標示為 © 2026 Google LLC

---

### [TanStack | 面向网络的开源应用栈。](https://tanstack.com/)

**原文标题**: [TanStack | The open-source application stack for the web.](https://tanstack.com/)

TanStack 是一个为现代网页应用打造的开源工具栈，提供无头、类型安全、可组合的开发工具，兼顾开发者和 AI 代理的需求。

- 🧩 **全面工具栈**：涵盖路由、数据管理、UI/UX、性能优化和开发工具等多个类别，包括 Router、Query、Table、Form 等核心库。
- 🔄 **框架无关**：所有库以框架无关的核心为基础，支持 React、Vue、Solid、Angular 或原生 JS，灵活选择。
- 🛡️ **类型安全**：原生支持 TypeScript，编译时捕获错误，提升重构信心。
- 🏭 **生产级质量**：经过大型应用实战检验，专为真实工作负载设计，非简单演示。
- 🗽 **无供应商锁定**：开源独立，无隐藏议程或平台偏见，专注为开发者提供优质工具。
- 🌐 **社区支持**：通过 Discord 和 YouTube 提供官方社区，便于提问、交流和获取最新资讯。

---

### [关于 Sourcemaps 你需要知道的一切 — Neciu Dan](https://neciudan.dev/everything-you-need-to-know-about-sourcemaps)

**原文标题**: [Everything you need to know about Sourcemaps — Neciu Dan](https://neciudan.dev/everything-you-need-to-know-about-sourcemaps)

以下是您提供的文章内容摘要：

Sourcemaps 是用于将压缩后的代码映射回原始代码的 JSON 文件，能极大提升调试效率，但若配置不当，会泄露整个源代码，带来严重安全风险。

- 🗺️ **Sourcemap 工作原理**：Sourcemap 是一个 JSON 文件，通过 `sources`、`sourcesContent`、`names` 和 `mappings` 字段，将压缩后的代码位置映射回原始文件、行、列和变量名。
- 🔄 **代码转换流程**：TypeScript 代码先被编译为 JavaScript，再经过压缩（重命名变量、删除空格等）成为难以阅读的压缩包，Sourcemap 则记录了这一逆向过程。
- ⚠️ **安全风险：源代码泄露**：默认情况下，许多构建工具会将原始源代码完整嵌入 Sourcemap 的 `sourcesContent` 字段。若 Sourcemap 文件被公开，任何人都能通过它还原出完整的、可读的源代码。
- 🍎 **案例一：苹果 App Store 泄露**：2025 年 11 月，苹果因在生产环境中启用了 Sourcemap，导致其全新网页版 App Store 的完整源代码被公开，暴露了文件夹结构、API 端点等敏感信息。
- 🤖 **案例二：Anthropic Claude Code 泄露**：2026 年 3 月，Anthropic 在 npm 包中意外包含了 59.8 MB 的 Sourcemap 文件，泄露了 Claude Code 近 2000 个 TypeScript 源文件，包括核心算法和未发布功能，且因 npm 的缓存特性导致泄露永久化。
- 🛡️ **防护措施**：在生产构建中禁用 Sourcemap 生成；若需用于错误追踪，应生成但设为隐藏（`hidden`），并仅上传至监控工具；在服务器端拦截所有 `.map` 文件请求；使用自动化脚本在 CI/CD 流程中检查并阻止包含源代码的 Sourcemap 文件被部署。

---

### [norswap · TypeScript 如何推断类型变量](https://norswap.com/typescript-type-variable-inference/)

**原文标题**: [
     norswap · How TypeScript infers type variables
  ](https://norswap.com/typescript-type-variable-inference/)

### 概述总结
TypeScript 通过一个复杂的算法推断函数中的类型变量，该算法包括候选收集和候选解析两个阶段，并受优先级、协变/逆变位置等因素影响。

- 🧩 **候选收集**：在源类型（参数）和目标类型（参数类型）之间并行遍历，每当遇到裸类型参数时，记录对应的源类型作为候选。候选分为协变（输出位置）和逆变（输入位置）两个列表。
- 🔄 **候选解析**：将协变候选列表合并为联合类型或公共超类型，逆变候选列表合并为交集类型或公共子类型。若两个列表均存在，逆变结果优先，除非协变结果是其子类型或逆变结果不满足约束。
- ⚡ **优先级机制**：候选收集时标记优先级（如`NakedTypeVariable`、`ReturnType`等），高优先级候选会清除低优先级候选。特定优先级下，解析时使用联合/交集而非超类型/子类型。
- 🚫 **不参与推断的元素**：类型参数的约束（`extends`）、默认值、条件类型的条件部分、源类型的超类型等均不贡献候选。
- 🔗 **联合与交集的处理**：源类型为联合时，遍历每个分支独立推断；源交集类型在结构匹配时合并对象形状。目标交集类型中的类型变量有时会“剥离”，有时不会，取决于启发式规则。
- 🧪 **特殊场景**：条件类型中的`infer`会创建新变量；泛型上下文中条件类型无法求值，需依赖结构匹配；`NoInfer<T>`可阻止特定位置的推断。
- 🛠️ **常见陷阱**：当需要同时捕获具体子类型及其结构子部分时（如`Map<K, V>`中的`V`），需使用提取器类型或额外参数绑定来绕过推断限制。

---

### [Geometric.js](https://www.harryjstevens.com/geometric/)

**原文标题**: [Geometric.js](https://www.harryjstevens.com/geometric/)

一个用于几何计算的 JavaScript 库，提供丰富的多边形和线条操作功能。

- 📐 反射角计算
- 📦 边界框检测
- 🧩 凸包生成
- 🔄 多边形相交判断
- 🎯 点在多边形内判断
- 📍 点与线位置关系判断
- ➖ 点在线上判断
- 🏠 点在多边形边界上判断
- 🗺️ 多边形包含关系判断
- ✂️ 线条相交计算
- 🔗 多边形线条相交
- 🎲 随机凸多边形生成
- ⭐ 正多边形生成
- 📊 平均中心与质心对比
- 📏 多边形周长测量
- 📐 像素距离测量
- 🎯 点到线距离
- 🏠 点到多边形距离
- 🔧 多边形布尔运算
- 🔄 多边形绕向判断
- ↔️ 多边形水平反射
- ↕️ 多边形垂直反射
- 🔄 线条旋转
- 🌀 点绕原点旋转
- 🔄 多边形旋转
- 📐 多边形缩放
- ↔️ 多边形水平缩放
- ↕️ 多边形垂直缩放
- 📏 多边形面积缩放
- 🗣️ 交互演示
- ➡️ 线条平移
- 🏠 多边形平移

---

### [示例 | Geometric.js](https://www.harryjstevens.com/geometric/examples/)

**原文标题**: [Examples | Geometric.js](https://www.harryjstevens.com/geometric/examples/)

本列表涵盖了与几何计算相关的多个功能和方法，包括多边形、线、点之间的各种操作与检测。

- 📐 反射角与边界框：包含角度反射和包围盒计算
- 🧩 多边形基础操作：如凸包、随机凸多边形、正多边形生成
- 🔍 包含关系检测：点与多边形、多边形与多边形之间的包含判断
- 📏 线与点关系：点在线左/右/上、点在线上的检测
- ✂️ 线与多边形交点：直线与多边形的交点计算
- 🎯 插值与测量：沿线/多边形插值、周长测量、像素距离
- ⚖️ 几何中心：平均中心与质心的区别
- 🔄 变换操作：平移、旋转、缩放（水平/垂直/面积）、反射
- 🧮 布尔运算与缠绕：多边形布尔操作与缠绕方向
- 💬 其他：包含“Talking Heads”等特殊功能

---

### [多边形是否与另一个多边形相交？示例 | Geometric.js](https://www.harryjstevens.com/geometric/examples/polygon-intersects-polygon/)

**原文标题**: [Does a Polygon Intersect Another Polygon? Example | Geometric.js](https://www.harryjstevens.com/geometric/examples/polygon-intersects-polygon/)

此内容介绍了如何判断两个多边形是否相交（但不包含）的几何函数。

- 🔵 函数 `geometric.polygonIntersectsPolygon(polygonA, polygonB)` 返回布尔值，表示 `polygonA` 是否与 `polygonB` 相交但不被包含。
- 🎮 可通过拖动蓝色多边形进行交互演示。
- ✅ 相交时显示 `true`。
- 📄 提供了相关代码文件：`Component.svelte`、`index.js`、`Scene.svelte`、`Controls.svelte`。
- 📋 支持复制功能。

---

### [适用于任意规模时间序列工作负载的 Postgres | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

概述摘要  
Tiger Cloud 提供免费试用，注册即获 $1,000 信用额度，支持弹性扩展、高可用性和企业级功能，适用于物联网等场景。

- 🚀 免费试用：注册即得 $1,000 信用额度，30 天有效，无需信用卡，仅限新用户。
- 📈 弹性扩展：通过最多 10 个节点的副本集分离读写，结合分层 SSD/S3 存储，实现成本优化。
- 💰 按需付费：计算与存储分离，独立扩展，避免闲置容量浪费。
- 🔒 高可用性：多可用区集群，支持自动故障切换、时间点恢复和跨区域备份。
- 🛡️ 企业级安全：符合 SOC 2、HIPAA、GDPR 标准，具备加密、SSO、RBAC 和审计日志功能。
- 👁️ 深度可观测性：提供查询钻取和仪表盘，监控性能与错误，集成 CloudWatch、Datadog、Prometheus。
- ⚡ 快速部署：分钟级数据库配置，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 集成生态：可与首选云提供商及 Postgres 生态系统无缝对接。
- 🏢 企业支持：提供合同性 SLA、区域数据隔离、合规认证及 24/7 全球专家支持。

---

### [Micromodal.js - 用于创建无障碍模态对话框的微型 JavaScript 库](https://micromodal.vercel.app/)

**原文标题**: [Micromodal.js - Tiny javascript library for creating accessible modal dialogs](https://micromodal.vercel.app/)

Micromodal.js 是一个轻量级、可配置且支持无障碍访问的纯 JavaScript 模态框库，遵循 WAI-ARIA 指南，最小化配置即可使用，体积仅 1.9kb。

- 🎯 核心功能：支持点击遮罩层关闭、按 Esc 键关闭、自动切换 aria-hidden 属性、焦点锁定、保持焦点位置、自动聚焦首个可聚焦元素
- 📦 安装方式：通过 npm 或 yarn 安装，也可使用 CDN 链接
- 🛠️ 使用步骤：添加特定 HTML 结构（含 data-micromodal-close 属性）、引入库、通过 data-micromodal-trigger 属性或 JavaScript 方法触发
- ⚙️ 配置选项：支持 onShow/onClose 回调、自定义触发属性、自定义打开类、禁用滚动、禁用自动聚焦、等待动画完成、调试模式等
- 🎨 样式自由：不提供任何默认样式，需自行添加 CSS 控制显示/隐藏，推荐使用 .modal.is-open 类切换 display 属性

---

### [<dialog> HTML 对话框元素 - HTML | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)

**原文标题**: [<dialog> HTML dialog element - HTML | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)

`<dialog>` HTML 元素用于创建模态或非模态对话框，支持多种打开和关闭方式，并可通过 JavaScript 和 CSS 进行控制与动画。

- 📋 **核心功能**：`<dialog>` 元素可创建模态（阻止页面交互）和非模态（允许页面交互）对话框，通过 `showModal()` 和 `show()` 方法控制。
- 🔑 **属性详解**：包括 `closedby`（控制关闭方式，如 `any`、`closerequest`、`none`）、`open`（表示对话框可见，但不推荐手动使用）。
- 🖱️ **打开方式**：支持 JavaScript 方法（`showModal()`/`show()`）、Invoker Commands API（`commandfor`/`command` 属性）、Popover API（`popover`/`popovertarget` 属性）。
- ❌ **关闭机制**：可通过表单提交（`method="dialog"`）、`Esc` 键、点击外部区域（light dismiss）、`close()` 方法或关闭按钮实现。
- 🎨 **CSS 样式**：可使用 `:modal`、`:open` 伪类选择器，并通过 `::backdrop` 伪元素设置模态对话框背景（如渐变、模糊效果）。
- 🔄 **动画支持**：通过 `@starting-style`、`display`、`overlay` 属性和 `allow-discrete` 实现过渡动画；或使用 CSS 关键帧动画（需在关键帧中设置 `display` 值）。
- ♿ **无障碍性**：默认聚焦于第一个可聚焦元素，建议使用 `autofocus`；模态对话框自动设置 `aria-modal="true"`，非模态为 `false`。
- 📝 **返回值处理**：通过 `returnValue` 获取对话框关闭时的值（如表单按钮值或 `close()` 传入的值）。
- 🌟 **示例应用**：包括 Invoker Command 打开模态对话框、Popover API 打开非模态对话框、表单验证关闭、不同 `closedby` 行为对比等。

---

### [PDFSlick](https://pdfslick.dev/)

**原文标题**: [PDFSlick](https://pdfslick.dev/)

概述摘要
- 🎉 宣布推出 PDFSlick Sync，可在应用中为 PDF 文档添加实时协作功能
- 📄 支持在 React、SolidJS、Svelte 及 JavaScript 应用中查看和交互 PDF
- 🖼️ 提供多种示例：完整查看器应用、评论功能、多文档支持、缩略图布局
- 🔄 包含水平缩略图、简单 PDF 查看器及错误处理等实用功能
- ©️ 2026 年由 Vancho Stojkov 开发，Vane Kosturanov 设计 Logo

---

### [PDFSlick 全功能查看器应用](https://pdfslick.dev/examples/pdf-viewer-app)

**原文标题**: [PDFSlick Full Viewer App](https://pdfslick.dev/examples/pdf-viewer-app)

概述总结：本文介绍了 PDFSlick 菜单的加载数据功能，可能涉及如何通过菜单选项加载 PDF 文件或相关数据。

- 📂 通过“Open PDFSlick menu”选项访问菜单功能
- 🔄 使用“Loading data”过程加载 PDF 文件或数据
- ⚙️ 菜单可能包含文件选择、数据导入等操作

---

### [GitHub - gajus/babel-plugin-zod-hoist: 将 Zod 模式定义提升到文件顶部。](https://github.com/gajus/babel-plugin-zod-hoist)

**原文标题**: [GitHub - gajus/babel-plugin-zod-hoist: Hoists Zod schema definitions to the top of the file. · GitHub](https://github.com/gajus/babel-plugin-zod-hoist)

babel-plugin-zod-hoist 是一个 Babel 插件，用于将 Zod 模式定义提升到文件顶部，从而避免重复初始化并大幅提升性能。

- 🚀 **性能大幅提升**：将 Zod 模式提升到文件顶部，避免重复初始化，速度提升 113–627 倍。
- 🧠 **零心智负担**：只需编写普通 Zod 代码，插件会自动完成提升，无需额外思考。
- 🔧 **无需修改代码**：与现有代码库无缝兼容，无需任何改动即可使用。
- 📦 **安装简单**：通过 `npm install --save-dev babel-plugin-zod-hoist` 安装，并在 Babel 配置中添加插件即可。
- 🔗 **支持派生模式**：可提升通过 `.extend()`、`.pick()`、`.omit()` 等组合器从导入基模式派生的模式。
- ⚠️ **安全提升规则**：仅提升仅由导入和字面量构建的模式，避免引用局部变量、`this` 或顶层绑定的模式，以防行为改变或暂时性死区错误。
- 🎯 **可配置模式匹配**：通过 `schemaNamePattern` 选项（默认 `/ZodSchema$/`）控制哪些标识符被视为 Zod 模式并提升，支持正则或字符串配置。

---

### [GitHub - gajus/slonik：一个具有运行时和构建时类型安全以及可组合SQL的Node.js PostgreSQL 客户端。](https://github.com/gajus/slonik)

**原文标题**: [GitHub - gajus/slonik: A Node.js PostgreSQL client with runtime and build time type safety, and composable SQL. · GitHub](https://github.com/gajus/slonik)

Slonik 是一个经过实战考验的 Node.js PostgreSQL 客户端，强调严格的类型安全、详细的日志记录和断言，鼓励编写原生 SQL 并避免动态生成 SQL。

- 🐘 **核心原则**：推广原生 SQL 编写，不鼓励临时动态生成 SQL，并建议停止使用 Knex.js。
- 🛡️ **安全防护**：通过强制使用 `sql` 标签模板字面量、禁止纯文本查询和提供安全的连接/事务处理模式，有效防止 SQL 注入和不安全的连接管理。
- 🎯 **类型安全与运行时验证**：集成 Zod 库，提供查询结果的运行时验证和静态类型推断，确保数据库模式与代码之间的契约始终得到遵守。
- 🧩 **丰富的查询构建方法**：提供 `sql.and`、`sql.or`、`sql.join`、`sql.json`、`sql.unnest` 等众多方法，用于安全、灵活地构建动态 SQL 查询片段。
- 🔄 **事务与重试机制**：支持事务嵌套（使用 SAVEPOINT）、事务事件监听以及自动重试因事务回滚类错误而失败的查询和事务。
- 🧪 **中间件与拦截器**：通过拦截器（中间件）机制，可以在查询生命周期的不同阶段（如连接、执行、结果转换）扩展功能，社区提供了多种现成拦截器。
- 📊 **详细的日志与调试**：使用 Roarr 进行日志记录，支持捕获堆栈跟踪，并可通过 `captureStackTrace` 配置在日志中包含调用堆栈信息，便于调试。
- 🔧 **灵活的配置**：提供丰富的客户端配置选项，包括连接超时、空闲超时、语句超时、连接池大小、SSL 设置等，并支持动态密码（如 IAM 认证）。
- 📦 **类型解析器**：内置了 `date`、`int8`、`interval`、`numeric`、`timestamp` 等 PostgreSQL 类型的解析器，并允许自定义或禁用默认解析器。

---

### [GitHub - eslint-functional/eslint-plugin-functional: 用于在 JavaScript 和 TypeScript 中禁用可变性并推广函数式编程的 ESLint 规则](https://github.com/eslint-functional/eslint-plugin-functional)

**原文标题**: [GitHub - eslint-functional/eslint-plugin-functional: ESLint rules to disable mutation and promote fp in JavaScript and TypeScript. · GitHub](https://github.com/eslint-functional/eslint-plugin-functional)

该 ESLint 插件旨在通过禁止数据变异和强制执行函数式编程风格，提升 JavaScript/TypeScript 代码的纯函数性和不可变性。

- 📦 **核心功能**：提供多个预设规则集（严格、推荐、精简），以及按类别划分的规则（如无异常、无变异、无语句等），全面支持函数式编程。
- 🛠️ **规则详情**：包含多项具体规则，例如`immutable-data`（强制数据不可变）、`no-let`（禁止可变变量）、`no-throw-statements`（禁止抛出异常）等，部分规则支持自动修复或需类型信息。
- 🎯 **预设配置**：提供`strict`、`recommended`、`lite`等预设，以及针对特定场景的类别配置（如 currying、noExceptions），方便用户按需启用。
- 🔧 **外部推荐**：额外推荐`no-var`、`no-param-reassign`等 Vanilla ESLint 规则，以及`@typescript-eslint/prefer-readonly`等 TypeScript 规则，增强不可变性。
- 📚 **文档与贡献**：包含详细的入门指南、贡献指南和安全策略，项目基于 MIT 许可证开源，并接受捐赠支持。

---

### [发布 v9.6.0 · TypeStrong/ts-loader · GitHub](https://github.com/TypeStrong/ts-loader/releases/tag/v9.6.0)

**原文标题**: [Release v9.6.0 · TypeStrong/ts-loader · GitHub](https://github.com/TypeStrong/ts-loader/releases/tag/v9.6.0)

概述总结  
- ⚙️ TypeStrong/ts-loader 是一个公共的 TypeScript 加载器项目，用于 Webpack。  
- ⭐ 该项目获得了 3.5k 星标和 437 个分支，社区关注度较高。  
- 🆕 最新版本 v9.6.0 于 5 月 29 日发布，由 acutmore 创建。  
- 🔄 该版本重新添加了对 Webpack 4 的支持，感谢贡献者 @johnnyreilly 和 @tweet。  
- 🔐 发布提交已通过 GitHub 验证签名，确保安全性。  
- 📋 项目包含代码、问题、拉取请求、操作、Wiki 和安全质量等管理功能。

---

### [ts-loader 再次支持 webpack 4...！ | johnnyreilly](https://johnnyreilly.com/ts-loader-goes-webpack-4-again)

**原文标题**: [ts-loader goes webpack 4... again! | johnnyreilly](https://johnnyreilly.com/ts-loader-goes-webpack-4-again)

概述摘要
ts-loader 在 2026 年重新支持 webpack 4，以应对 webpack 4 仍有大量用户（每周约 400 万次下载）的现状，并简化维护工作。

- 📦 **版本更新**：ts-loader v9.6.0 重新支持 webpack 4，此前 v9 版本只支持 webpack 5。
- 📉 **用户需求**：webpack 4 仍有每周约 400 万次下载，ts-loader@8 也有近 100 万次下载，迁移至 webpack 5 进程缓慢。
- 🔧 **维护简化**：通过 GitHub Copilot 辅助实验，成功在 ts-loader@9 中同时支持 webpack 4 和 5，无需大量代码改动。
- 🛠️ **技术调整**：主要改动包括适配 webpack 4 的不同 API、使用可选依赖 `loader-utils`，并更新测试包以支持两个版本。
- 🚀 **发布影响**：webpack 4 用户现可直接使用 ts-loader@9，无需依赖旧版 ts-loader@8，减轻维护负担。
- ❌ **不支持旧版**：明确不会恢复对 webpack 3、2 或 1 的支持，仅针对 webpack 4。

---

### [GitHub - mrdoob/draco.js：一个用于three.js的小型、即插即用、纯JavaScript的Draco网格加载器。](https://github.com/mrdoob/draco.js)

**原文标题**: [GitHub - mrdoob/draco.js: A small, drop-in, pure-JavaScript Draco mesh loader for three.js. · GitHub](https://github.com/mrdoob/draco.js)

概述：Draco.js 是一个为 three.js 设计的纯 JavaScript Draco 网格加载器，比官方 WASM 版本更小、更易部署，解码速度接近，适合单模型页面。

- 📦 **体积小巧** — 仅约 20 KB gzipped（62 KB minified），比官方 WASM 版本小 5 倍。
- 🚀 **部署简单** — 单一 ES 模块，无需 fetch .wasm、worker 或跨域配置。
- ⚡ **性能接近** — 解码速度约为 WASM 版本的 1.0–1.4 倍，大模型几乎持平，输出一致。
- 🎯 **目标明确** — 支持 Draco 比特流 2.2 版本，仅处理三角形网格，不解析点云或元数据。
- 🔧 **即插即用** — 可直接替换 three.js 的 DRACOLoader，无需额外配置。
- 🌐 **支持格式** — 可加载 glTF 压缩网格和独立 .drc 文件。
- 🏆 **适用场景** — 单模型页面受益最大，网络节省抵消了额外解码时间。

---

### [draco.js](https://mrdoob.github.io/draco.js/#bunny.drc)

**原文标题**: [draco.js](https://mrdoob.github.io/draco.js/#bunny.drc)

该内容列出了 Draco 压缩格式（.drc）与 GLB/GLTF 格式的 3D 模型示例及其顶点/几何体数量，并提供了一个性能指标表格框架（WASM 与 JS 对比），用于评估加载、初始化和解析时间。

- 🐰 bunny.drc：1 个几何体，3.5 万顶点
- 🏛️ nemetona.glb：1 个几何体，34.9 万顶点
- 🚗 ferrari.glb：51 个几何体，33.8 万顶点
- 🏙️ LittlestTokyo.glb：71 个几何体，19.3 万顶点
- 🎭 venice_mask.glb：5 个几何体，17.4 万顶点
- ⌚ rolex.glb：24 个几何体，10.2 万顶点
- 👘 kira.glb：43 个几何体，5.5 万顶点
- ⚙️ gears.glb：3 个几何体，2.3 万顶点
- 🛁 bath_day.glb：22 个几何体，2.2 万顶点
- 🫒 IridescentDishWithOlives.glb：4 个几何体，1.5 万顶点
- 🛏️ minimalistic_modern_bedroom.glb：4 个几何体，1.4 万顶点
- 🏊 pool.glb：2 个几何体，1.4 万顶点
- 🌲 forest_house.glb：12 个几何体，1.2 万顶点
- 🎨 ShaderBall2.glb：3 个几何体，8 千顶点
- 🦆 duck.drc：1 个几何体，2 千顶点
- 🦆 duck.glb：1 个几何体，2 千顶点
- 📦 cube-edgebreaker.drc：1 个几何体，24 顶点
- 📦 cube.drc：1 个几何体，24 顶点
- 📊 性能指标：WASM 与 JS 对比，包括加载器大小、加载 + 初始化时间、解析时间和总时间（均待填）
- 💻 交互提示：可拖拽.drc/.glb/.gltf 文件进行加载测试

---

### [Taiga UI](https://taiga-ui.dev/)

**原文标题**: [Taiga UI](https://taiga-ui.dev/)

概述摘要  
Taiga UI 是一个强大的开源组件库，支持高度自定义设计，用户可自由浏览和选用组件。  

- 🎨 支持个性化定制设计，满足不同需求  
- 🚀 提供强大的开源组件集合  
- 🔍 可自由浏览并选用各类组件

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified)

Meticulous 是一个自动化测试平台，能够零开发者投入地生成详尽、确定性的测试，帮助团队快速交付代码，尤其适用于复杂代码库。

- 🚀 **零开发者投入的详尽验证**：自动化生成测试，无需手动编写、修复或维护，测试随应用自动演进。
- 🎯 **确定性测试，杜绝假阳性**：通过模拟后端响应和确定性调度引擎，消除测试不稳定因素，实现快速执行。
- ⚡ **闪电般速度与规模化并行**：测试在计算集群中高度并行化，支持在 120 秒内完成数千屏幕的测试。
- 🔄 **无缝集成与持续演进**：监控日常开发交互，AI 引擎自动生成覆盖所有代码分支和用户流程的测试套件。
- 🛡️ **从底层消除不稳定**：基于 Chromium 构建的确定性调度引擎，专为消除假阳性而设计，适用于最复杂的应用。
- 📊 **即时代码影响分析**：在合并前，通过拉取请求即可看到更改对用户工作流的影响。
- 🔌 **广泛框架支持**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流框架，集成简单。
- 🤝 **可补充或替代现有测试**：能与现有测试套件配合使用，或完全替代传统测试。
- 🏢 **受知名组织信赖**：包括 Dropbox、Notion、Engine 等在内的 100 多家组织已采用。

---

### [最大组织报告](https://clerk.com/changelog/2026-05-26-largest-organizations-report?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=orgs-report&utm_content=06-09-26&dub_id=xTjmSegpnAt0rbAW)

**原文标题**: [Largest organizations report](https://clerk.com/changelog/2026-05-26-largest-organizations-report?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=orgs-report&utm_content=06-09-26&dub_id=xTjmSegpnAt0rbAW)

概述摘要
- 📊 新增“最大组织”报告，按成员数排序显示实例中的最大组织。
- 👁️ 快速概览：按成员数降序排列，附链接至组织详情页。
- 📏 可视化对比：每个组织以条形图显示，按成员数缩放，便于比较。
- 🔍 发现异常与增长：查看租户间的使用分布，捕捉异常增长模式。
- 🚀 使用方式：前往 Clerk 仪表盘的“概览”页面查看。
- ✅ 适用性：对所有启用了组织的实例即时可用。

---

### [使用福昕 DocGen API 从 Word 模板生成 PDF](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/dynamic-pdf-generation-foxit-docgen-api/?utm_source=draftdev&utm_medium=referral&utm_campaign=jsweekly_20260609)

**原文标题**: [Generate PDFs from Word Templates with Foxit DocGen API](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/dynamic-pdf-generation-foxit-docgen-api/?utm_source=draftdev&utm_medium=referral&utm_campaign=jsweekly_20260609)

本指南介绍如何构建一个可验证质量的 PDF 翻译管道，结合 Foxit API 进行结构提取和布局保留渲染，以及 Straker.ai 进行翻译和逐段质量评分，解决机器翻译中缺乏可信度信号的问题，尤其适用于合同、医疗表格和监管文件。

- 📄 使用 Foxit API 提取 PDF 的结构（如段落、表格、标题），并保留原始布局进行渲染
- 🔍 利用 Straker.ai 对每个文本段进行翻译，并输出逐段的质量评分（如置信度分数）
- ⚠️ 质量评分帮助用户识别哪些部分翻译可靠、哪些需要人工审核，避免盲目信任
- 🛠️ 构建的管道在最终输出 PDF 前，先对每个片段进行评分，确保翻译质量可验证
- 📋 特别适用于高风险的文档类型，如法律合同、医疗表单和监管申报文件

---

### [Trigger.dev | 构建和部署完全托管的人工智能代理与工作流。](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=june&utm_term=js-weekly&utm_content=homepage)

**原文标题**: [Trigger.dev | Build and deploy fully-managed AI agents and workflows.](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=june&utm_term=js-weekly&utm_content=homepage)

Trigger.dev 现已符合 HIPAA 标准，提供一个用于构建和部署完全托管的 AI 代理与工作流的平台。它支持 TypeScript，具备重试、队列、可观测性和弹性扩展等功能，并受到全球开发者的信赖。

- 🏥 符合 HIPAA 标准，可用于医疗健康等敏感数据处理
- 🤖 支持构建生产级 AI 代理，具备工具调用、自动重试和全面可观测性
- ⏱️ 无超时限制，按实际执行付费，无需管理服务器
- 🔍 提供错误警报、高级过滤和版本控制，便于快速发现和修复问题
- 📡 支持实时更新 UI 和流式传输 LLM 响应到前端
- 🐍 允许自由定制构建过程，包括运行 Python 脚本、集成 Prisma 和 Puppeteer 等
- 🔧 提供重试配置、并发控制、人工审核和多种开发与生产工具
- 💬 受到 Supabase、Magic Patterns 等众多公司开发者的好评
- 💰 定价简单，仅按使用量付费，并支持开源自托管

---

### [Mitos ASCII 工具](https://mitos-pied.vercel.app/)

**原文标题**: [Mitos ASCII Tool](https://mitos-pied.vercel.app/)

概述：本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了其在诊断、治疗和患者管理方面的关键进展与挑战。

- 🩺 人工智能在医学影像分析中展现出高准确性，可辅助医生快速识别肿瘤、骨折等病变。
- 💊 通过机器学习算法，AI 能根据患者基因和病史个性化推荐药物方案，提升治疗效果。
- 📊 智能健康监测系统利用可穿戴设备数据，实时预警慢性病患者病情变化，减少急诊风险。
- 🤖 手术机器人结合 AI 视觉与精密控制，实现微创操作，降低手术并发症率。
- ⚖️ 数据隐私、算法偏见和监管滞后仍是 AI 医疗普及的主要障碍，需加强伦理规范与法规建设。

---

### [玩耍](https://play.ertdfgcvb.xyz/)

**原文标题**: [Play](https://play.ertdfgcvb.xyz/)

### 概述
ASCII Play 是一个基于文本字符的创意编程项目，提供交互式控制台和丰富示例。

- 🎮 **项目简介**：ASCII Play 是一个 ASCII 艺术编程项目，由 ertdfgcvb 创建
- ⌨️ **快捷键操作**：支持运行（Cmd+Enter）、全屏（Cmd+Shift+F）、保存（Cmd+S）等多种快捷键
- 📂 **示例分类**：包含基础示例（如坐标、画圆、性能测试）、演示（如 Donut、Plasma、Spiral）和相机功能
- 🎨 **功能特性**：支持即时模式、视图切换、帧复制、脚本下载和分享
- 🌐 **社区贡献**：包含用户贡献的彩色波浪、表情波浪、沙盒游戏等创意作品
- 📷 **相机集成**：支持摄像头灰度、RGB 和双分辨率模式

---

### [replacements.fyi - 高性能、更安全的 npm 包替代方案](https://replacements.fyi/)

**原文标题**: [replacements.fyi - performant, safer npm package alternatives](https://replacements.fyi/)

该工具可帮助开发者识别并移除项目中不必要的依赖包，优化项目体积和性能。

- 🔍 输入包名即可检测：输入任意 npm 包名，工具会分析其是否可被替代或移除
- 🚫 推荐移除冗余包：例如 is-number、left-pad、is-odd 等常见但已过时的工具包
- ⚡ 基于 e18e.dev 技术：利用 e18e.dev 的数据库和算法进行智能分析
- 📦 支持批量扫描：可上传 package.json 文件，一键扫描所有依赖
- 🌐 浏览完整列表：提供所有可移除包的浏览功能，方便开发者自查

---

### [Obs.js – 面向所有人的上下文感知网页性能优化](https://csswizardry.com/Obs.js/demo/)

**原文标题**: [Obs.js – context-aware web performance for everyone](https://csswizardry.com/Obs.js/demo/)

无法总结：未找到主要内容。

---

### [使用 Obs.js 在用户所在之处与他们相遇 – CSS 魔法](https://csswizardry.com/2026/05/meet-your-users-where-they-are-with-obs-js/)

**原文标题**: [Meet Your Users Where They Are with Obs.js – CSS Wizardry](https://csswizardry.com/2026/05/meet-your-users-where-they-are-with-obs-js/)

### 概述摘要
Obs.js 是一款轻量级库，通过读取浏览器信号（连接、设备、电池等）帮助开发者根据用户实际环境调整前端体验，实现更体贴的性能优化，而非一刀切的“聪明”设计。

- 📱 **核心功能**：Obs.js 读取浏览器信号（延迟、带宽、数据节省、电池、CPU、内存），在 `<html>` 元素上添加类，并通过 `window.obs` 对象暴露数据，让开发者根据用户环境做出决策。
- 🖼️ **实际案例**：作者在主页根据 Obs.js 的 `deliveryMode` 信号，为高速用户提供高清图片堆栈，为低性能用户仅显示 LQIP 版本，且 LCP 仅差 80ms，体验几乎一致。
- 🔋 **电池优化**：低电量用户会禁用多余动画，仅保留简单开关导航，体现“每一点帮助都很重要”的理念。
- 📊 **状态与立场**：库区分“状态”（如电池低、连接慢）和“立场”（如建议使用轻量模式），开发者可自行选择基于原始信号或库的推荐决策。
- 🤝 **体贴而非聪明**：重点不是让网站显得“聪明”，而是更“体贴”——根据用户实际条件，问“是否应该”而非“能否”提供某些功能。
- 📈 **分析分段**：Obs.js 可作为分析工具的分段层，帮助区分“我们问题”还是“他们问题”，例如发现低电量用户转化率更高，可简化结账流程。
- ⚠️ **浏览器支持**：主要依赖 Chromium 内核，Safari 支持有限，但作为渐进增强方案，开发者可自行决定默认体验（丰富或轻量）。
- 🛠️ **实用主义**：库体积小、易集成，只需放入 `<head>` 即可开始调整（如缩小图片、跳过自动播放、减少动画），强调“小调整带来大不同”。

---

### [AI 对决格鲁](https://www.raymondcamden.com/2026/06/02/ai-versus-a-grue)

**原文标题**: [AI versus a Grue](https://www.raymondcamden.com/2026/06/02/ai-versus-a-grue)

### 概述摘要
作者尝试让 Chrome 内置 AI 玩经典文字冒险游戏《Zork 1》，虽然 AI 表现不佳，但过程有趣。文章详细介绍了技术实现、代码示例和测试结果。

- 🎮 作者用 Chrome 的 Prompt API 让 AI 玩《Zork 1》，但 AI 始终无法突破游戏初期区域
- 🛠️ 通过 Claude 辅助构建了基于 ifvms.js 的交互式游戏引擎，实现 AI 与游戏的循环交互
- 📝 设计了包含系统提示词和游戏循环的完整架构，但未处理会话管理问题
- 🚫 AI 在测试中只会重复探索房屋周围区域，无法有效推进游戏进程
- 💡 作者承认代码存在缺陷（如缺乏会话管理），但认为尝试过程很有趣
- 🔗 提供了在线演示和完整代码仓库供读者自行测试

---

