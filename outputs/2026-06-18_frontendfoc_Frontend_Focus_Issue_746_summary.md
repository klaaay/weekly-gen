### [介绍 MDN MCP 服务器](https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/)

**原文标题**: [Introducing the MDN MCP server](https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/)

MDN MCP 服务器发布，为 AI 工具提供实时、准确的 Web 平台文档和浏览器兼容性数据。

- 🚀 **发布 MDN MCP 服务器**：基于模型上下文协议（MCP），将 MDN 文档和浏览器兼容性数据直接集成到 AI 代理或 IDE 中。
- 🎯 **解决 AI 知识过时问题**：AI 工具常因训练数据截止而提供过时的 Web 平台信息，MCP 可提供最新、准确的文档和兼容性数据。
- 🛠️ **支持多种客户端**：兼容 VS Code、Zed、Cursor 等编辑器，Claude Code、Codex CLI 等代理 CLI，以及 Claude Desktop 等聊天应用。
- 📊 **测试结果显著提升**：与未启用 MCP 的 Claude Code 相比，启用后浏览器兼容性信息更准确（如正确识别 Firefox 151 对 Web Serial API 的支持），响应速度约快一倍。
- 🔍 **具体案例对比**：在 light-dark() CSS 函数、:buffering 伪类、shadowrootslotassignment 属性和 Web Serial API 的测试中，MCP 版本提供了更完整、更可靠的浏览器支持表格。
- 💬 **邀请社区参与**：欢迎通过 Discord 平台频道或 GitHub 仓库反馈问题、建议或使用场景。
- 🔮 **未来计划**：随着 AI 在 Web 开发中的普及，Mozilla 致力于让 MDN 文档随处可用，并持续改进 MCP 体验。

---

### [clerk 部署：引导式、可恢复、支持代理](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli-deploy&utm_content=06-17-26&dub_id=8aTFXCJxYvf6DYta)

**原文标题**: [clerk deploy: guided, resumable, agent-ready](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli-deploy&utm_content=06-17-26&dub_id=8aTFXCJxYvf6DYta)

### 概述总结  
Clerk CLI 新增 `clerk deploy` 命令，支持一键将应用从开发环境部署到生产环境，并提供引导式流程、可恢复操作及代理模式。  

- 🚀 **单命令部署**：`clerk deploy` 从开发实例克隆配置至生产环境，自动引导 DNS 和 OAuth 设置。  
- 🛠️ **生产实例创建**：基于开发配置生成生产实例，并提示输入生产域名。  
- 📋 **DNS 记录管理**：显示需添加的 CNAME 记录，支持导出为 DNS 区域文件，便于导入兼容提供商。  
- 🔑 **OAuth 凭据配置**：检测已启用的社交登录，引导设置 Google 和 Apple 凭据（支持导入 JSON 或 .p8 文件），其他提供商标记为待处理。  
- ✅ **验证循环**：自动检查 DNS、SSL 和邮件 DNS，实时报告未完成项。  
- 🤖 **代理模式支持**：在非 TTY 环境或 `--mode agent` 下，输出只读 JSON 状态，而非交互提示。  
- 📖 **快速入门**：更新 CLI、链接项目后执行 `clerk deploy`，完整文档提供所有命令和选项。

---

### [CSS @function 的作用范围 – Master.dev 博客](https://master.dev/blog/the-scope-of-css-function/)

**原文标题**: [The Scope of CSS @function – Master.dev Blog](https://master.dev/blog/the-scope-of-css-function/)

CSS 自定义函数的作用域特性非常强大，支持“可移植求值作用域”模式，允许函数从调用位置继承变量，从而解耦 DOM 结构，实现复杂逻辑封装与优雅的开发者体验。

- 🧩 **变量继承机制**：CSS 函数在调用时会继承调用处的所有 `--var` 变量，类似 JavaScript 的闭包作用域，但基于求值作用域而非 DOM 结构。
- 🔄 **可移植求值作用域**：通过将函数定义在特定上下文中，子函数可以安全地使用父函数计算的中间变量，实现逻辑隔离与复用。
- 🎛️ **开关函数模式**：使用 `if(style())` 创建父函数，根据参数分支调用不同子函数，隐藏内部复杂性，对外提供简洁 API。
- 🧪 **部分应用与柯里化**：通过外层函数封装开关函数，预设参数，形成更易用的接口，类似函数式编程中的部分应用。
- 🛠️ **实际案例**：`doubledash` 库利用此模式实现 16 位整数位运算和纯 CSS 循环，内部通过多层求值作用域拆分逻辑，对外仅暴露简单函数。
- 🚫 **动态函数传递限制**：CSS 当前不支持动态引用函数，需通过预定义函数槽位（如 64 个循环 ID）让用户实现自定义逻辑。
- 📦 **用户扩展性**：库作者可提供“可移植求值作用域”，让用户定义子函数，利用库提供的变量（如循环索引）实现自定义行为。
- 🧩 **参数重载技巧**：通过默认值 `initial` 和 `if(style())` 检查，实现类似函数签名重载的效果，提升 API 灵活性。
- 🌟 **最终价值**：尽管 CSS 函数存在基础限制，但求值作用域模式让组件库作者能提供简洁文档，用户无需了解底层复杂度即可高效使用。

---

### [今日发布 Babel 8：仅支持 ESM，放弃 ES5 默认，并提供平滑迁移路径 · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

**原文标题**: [Releasing Babel 8 today: ESM-only, drop ES5 default, and a smooth migration path · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

Babel 8 今日正式发布，专注于核心现代化，为未来 8 年做准备，同时提供平滑迁移路径。

- 🚀 Babel 8 现在仅支持 ESM，不再默认编译为 ES5 和 CommonJS，推动 JavaScript 生态系统向前发展。
- 📦 所有 Babel 包现在都提供 TypeScript 类型，无需额外安装 `@types/babel__*` 包。
- 🔧 默认目标从 ES5 变为基于 Browserslist 的“默认”查询（当前约为 ES2023），并自动适应新浏览器。
- ⚠️ 弃用 `loose` 和 `spec` 选项，建议使用更细粒度的 `assumptions` 配置。
- 🧩 将 polyfill 注入功能提取到独立包 `babel-plugin-polyfill-corejs3`，替代 `corejs`/`useBuiltIns` 选项。
- 📉 尽管下载量激增（从 2018 年 170 万到 2026 年 6.51 亿/周），但捐款持续下降，项目需要社区支持。
- 🛡️ Babel 7 将停止功能更新，但提供一年安全支持（至 2027 年 6 月）。
- 💡 核心团队强调，若无德国主权技术机构和 Igalia 的资助，项目难以维持高质量标准。

---

### [Firefox 152 开发者版本发布说明（稳定版） - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/152)

**原文标题**: [Firefox 152 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/152)

以下是 Firefox 152 开发者版本更新的要点总结：

- 🛠️ **开发者工具新增“显示注释”选项**：可在设置面板中切换，用于在检查器中显示或隐藏 HTML 注释节点。
- 📐 **SVG 支持 `SVGTextPathElement.side` 属性**：只读属性，指示文本绘制在路径的左侧还是右侧。
- 🎨 **CSS 新增 `field-sizing` 属性**：控制表单元素尺寸，支持 `content`（自适应内容）和 `fixed`（固定尺寸）两个值。
- ⏱️ **性能 API 新增两个属性**：`firstInterimResponseStart` 和 `finalResponseHeadersStart`，用于测量 HTTP 响应时间。
- 🎞️ **动画事件新增 `animation` 属性**：`AnimationEvent.animation` 和 `TransitionEvent.animation` 提供更便捷的动画访问方式。
- 🔔 **DOM 支持通知操作**：包括 `ServiceWorkerRegistration.showNotification()` 的 `actions` 参数，以及 `Notification` 接口的 `actions` 和 `maxActions` 属性。
- 🎯 **`Element.getAnimations()` 支持伪元素参数**：通过 `options.pseudoElement` 直接定位特定伪元素。
- 🖱️ **`requestPointerLock()` 支持无加速模式**：通过 `options.unadjustedMovement` 禁用操作系统鼠标加速，实现精确控制。
- 📡 **WebRTC 元数据新增 `receiveTime` 属性**：用于 `RTCEncodedVideoFrame` 和 `RTCEncodedAudioFrame` 的获取和构造。
- 🧩 **WebDriver 改进**：优化截图命令尺寸限制、支持隐私模式安装扩展、改进下载行为设置、修复网络事件转发。
- 🚫 **扩展动态代码执行功能移除**：在 `moz-extension:` 文档中使用 `tabs.executeScript` 等 API 动态执行代码的功能已被移除，建议改用 `runtime.onMessage` 监听器。
- 🔬 **实验性功能（默认禁用）**：
  - 📺 WebRTC 媒体能力检测（`media.mediacapabilities.webrtc.enabled`）
  - 🔄 `Iterator.prototype.includes()` 方法（`javascript.options.experimental.iterator_includes`）
  - 🌐 `Intl.Locale` 信息提案（`javascript.options.experimental.intl_locale_info`）
  - 📜 文本模块导入（`javascript.options.experimental.import_text`）
  - 🎬 `@keyframes` 选择器支持时间线范围（`layout.css.scroll-driven-animations.enabled`）

---

### [field-sizing CSS 属性 - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing)

**原文标题**: [field-sizing CSS property - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing)

### 概述摘要
`field-sizing` CSS 属性允许表单控件根据内容自动调整尺寸，覆盖默认固定大小行为，适用于文本输入框、文本域、文件输入和选择框等元素，并可与最小/最大尺寸属性配合使用。

- 📏 **核心功能**：通过 `field-sizing: content` 让表单控件（如 `<input>`、`<textarea>`）根据内容自动收缩或扩展尺寸，替代默认的固定大小。
- 🎯 **适用元素**：影响文本输入类型（email、password、text 等）、文件输入、文本域和选择框（`<select>`），其中选择框会根据类型（下拉或列表框）动态调整宽度或显示全部选项。
- ⚙️ **属性值**：`content` 使元素自适应内容；`fixed` 为固定大小（默认值）。
- 🔗 **与其他属性交互**：避免同时设置固定 `width`/`height`，但可结合 `min-width`/`max-width` 控制范围；`maxlength` 属性可限制输入框最大尺寸。
- 📝 **文本域行为**：宽度受限时自动增加高度；`rows`/`cols` 属性在 `field-sizing: content` 下无效。
- 📋 **选择框效果**：下拉菜单始终匹配当前选项宽度；多选列表框显示所有选项无需滚动；`size` 属性仅用于判断下拉或列表模式。
- 🖥️ **浏览器支持**：此功能非 Baseline，部分浏览器尚未完全实现，需查看兼容性表。
- 📚 **实际示例**：通过 HTML/CSS 展示文本字段和选择框在 `field-sizing: content` 下的动态尺寸变化，包括占位符、最大长度限制等场景。

---

### [无需 JavaScript 的本地化时间格式化 · Issue #12591 · whatwg/html · GitHub](https://github.com/whatwg/html/issues/12591)

**原文标题**: [Localized time formatting without JavaScript · Issue #12591 · whatwg/html · GitHub](https://github.com/whatwg/html/issues/12591)

该提案旨在通过扩展 HTML `<time>` 元素，实现无需 JavaScript 即可在服务端渲染时进行本地化时间格式化，解决时区未知和性能问题。

- 🎯 **核心问题**：服务端渲染的 HTML 无法获知用户时区，导致无法正确显示绝对时间，现有方案（相对时间、固定时区、IP 猜测、JS 脚本）均有缺陷。
- 💡 **解决方案**：扩展`<time>`元素，通过新增`format`属性（`"date"`、`"time"`、`"datetime"`）触发本地化格式化，并使用 UA 影子根（Shadow Root）渲染结果。
- ⚙️ **格式化属性**：提供`datefields`、`datelength`、`timeprecision`、`timezonestyle`、`hour12`、`calendar`、`timezone`等属性，精细控制日期、时间、时区、日历的显示方式。
- 🌐 **本地化机制**：通过 DOM 向上遍历查找最近的`lang`属性来确定用户区域，并利用`Intl.DateTimeFormat`进行格式化，确保兼容现有国际化标准。
- 🛡️ **技术实现**：使用 UA 影子根而非 CSS `content`，以简化文本选择并支持对日期/时间各部分的独立样式控制（通过 CSS 伪元素选择器）。
- 📅 **解析支持**：`datetime`属性将支持 RFC 9557 格式，解析为`Temporal`对象（如`PlainDateTime`、`ZonedDateTime`等），并支持时区和日历转换。
- 🔮 **未来扩展**：预计未来将支持实时相对时间格式化（如“2 秒前”），且格式化选项与 Unicode MessageFormat 2 和 ECMA-402 标准对齐。

---

### [字节码联盟 — WASI 0.3 发布](https://bytecodealliance.org/articles/WASI-0.3)

**原文标题**: [Bytecode Alliance — WASI 0.3 Launched](https://bytecodealliance.org/articles/WASI-0.3)

WASI 0.3 正式发布，异步操作成为 WebAssembly 组件的原生特性。

- 🎉 WASI 0.3 已通过投票并正式稳定，运行时和工具链支持正在落地。
- ⚡ 异步操作现为组件模型规范 ABI 的原生部分，简化了流和未来值的处理。
- 🔄 主机管理统一事件循环，取代了 WASI 0.2 中每个组件各自运行事件循环的方式。
- 🆕 新增 `stream<T>`、`future<T>` 和 `async` 作为一等公民，支持基于完成的异步模型。
- 📉 WASI 0.3 接口大幅简化，例如 `pollable` 变为 `future<T>`，`input-stream` 变为 `stream<u8>`。
- 🛠️ 流现在返回独立的 `future` 来指示终端错误，解决了 WASI 0.2 中的问题。
- 🌐 语言绑定生成器可生成原生异步绑定，如 Rust 的 `async fn handle` 和 Go 的 goroutine 支持。
- 🔗 `wasi:http` 新增 `middleware` 世界，支持服务链式组合，延迟从毫秒降至纳秒。
- ✅ 已获 Wasmtime 45 和 Jco 支持，Wasmtime 46 将默认启用 WASI 0.3。
- 🚀 未来将支持更多语言（Rust、Go、JavaScript、Python 等）的 WASI 0.3 组件开发。

---

### [今天，Frontend Masters 更名为 Master.dev – Master.dev 博客](https://master.dev/blog/today-frontend-masters-becomes-master-dev/)

**原文标题**: [Today, Frontend Masters becomes Master.dev – Master.dev Blog](https://master.dev/blog/today-frontend-masters-becomes-master-dev/)

Frontend Masters 正式更名为 Master.dev，以反映其课程已从仅前端扩展到全栈、DevOps 和 AI 领域。

- 🎓 更名源于用户反馈：用户指出原名“Frontend Masters”已无法体现平台日益丰富的课程内容。
- 📚 热门课程已远超前端：包括 Go、Rust、数据库、云基础设施、Java、Linux、Git、DevOps、SQL、Python 等。
- 🤖 AI 课程增长迅猛：当前十大热门课程中有四门与 AI 相关，如 Claude Code、AI 工程基础、AI 代理基础等。
- 🚀 使命扩展：从帮助工程师掌握前端，升级为助力掌握整个技术栈，涵盖编程语言、系统及 AI 工具。
- 🔗 域名选择：因 masters.dev 域名不可得，最终选用 Master.dev，寓意“掌握”这一动词。
- 🎉 服务不变：原有课程、讲师和高质量教学标准均保持不变，并新增全栈、DevOps 和 AI 方向内容。
- 💻 优惠活动：订阅 300+ 课程可享 20% 折扣，并支持个性化学习路径和直播工作坊。

---

### [可定制选择器的黄金法则 | WebKit](https://webkit.org/blog/18117/the-golden-rule-of-customizable-select/)

**原文标题**: [  The golden rule of Customizable Select | WebKit](https://webkit.org/blog/18117/the-golden-rule-of-customizable-select/)

### 概述总结
自定义`<select>`元素即将在 Safari 27 中支持，开发者可完全控制其样式，无需依赖 JavaScript 库或大量`<div>`元素。但核心规则是：**始终为`<option>`元素提供文本内容或可访问文本属性**，否则会导致可用性、无障碍性和渐进增强问题。

- 🎨 **更好的用户体验**：仅用图标（如建筑、花、蜂鸟）表示选项时，用户可能无法识别含义；添加文本标签后，选项一目了然，选择状态清晰可辨。
- ♿ **更好的无障碍性**：屏幕阅读器依赖文本标签；即使文本被视觉隐藏（如`.visually-hidden`类），仍保留在无障碍树中；图标需配合`alt`或`aria-label`属性，避免空选项。
- 🔄 **更好的渐进增强**：不支持自定义 select 的浏览器会回退到原生控件；若选项无文本，旧浏览器会显示空下拉菜单；应使用`@supports (appearance: base-select)`包裹增强样式，并保留纯文本作为基线。
- ⚠️ **核心规则**：文本必须存在，可视觉隐藏或缩小，但不可缺失；图标、色块等只是补充，不能替代文本。遵循此规则，即可充分发挥自定义 select 的潜力。

---

### [为什么我的 3D 视图过渡不工作？| CSS 技巧](https://css-tricks.com/why-isnt-my-3d-view-transition-working/)

**原文标题**: [Why Isn't My 3D View Transition Working? | CSS-Tricks](https://css-tricks.com/why-isnt-my-3d-view-transition-working/)

### 概述总结
文章解释了为什么跨文档 3D 视图过渡（View Transitions）在 CSS 中无法正常工作，并提供了使用`perspective()`函数而非`perspective`属性的解决方案。

- 🎥 **问题背景**：3D 视图过渡（如翻转效果）在跨页面导航时失败，因为浏览器会先“扁平化”元素，导致`perspective`属性无效。
- 🔍 **关键原因**：视图过渡的伪元素树（`::view-transition-*`）渲染在 DOM 之外，没有真正的父元素，因此`perspective`属性无法作用于子元素。
- ❌ **无效尝试**：在`html`、`:root`、`body`或`::view-transition-group`上设置`perspective`属性均不生效。
- ✅ **解决方案**：在`@keyframes`动画的`transform`属性中直接使用`perspective()`函数（如`transform: perspective(1100px) rotateY(-90deg)`），而非单独的`perspective`属性。
- ⚙️ **原理差异**：`perspective`属性需要父元素传递效果，而`perspective()`作为变换函数直接作用于元素自身，绕过了父元素缺失的问题。
- 💡 **实用建议**：若需实现 3D 视图过渡，始终在动画关键帧中嵌入`perspective()`函数，避免依赖父元素层级。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Cloud 提供专为时间序列工作负载优化的 PostgreSQL 服务，具备大规模处理能力（日处理 3 万亿指标、1 千万亿数据点），并提供免费试用（$1000 额度，30 天有效）。

- 🚀 **弹性扩展**：支持最多 10 节点的读写分离副本集，搭配分层 SSD/S3 实现无限且经济的存储。
- 💰 **按需付费**：计算与存储分离，可独立扩展，避免为闲置容量付费，优化成本与性能。
- 🔒 **高可用与企业级**：多可用区集群自动故障转移、时间点恢复、跨区域备份；符合 SOC 2、HIPAA、GDPR 标准，支持加密、SSO、RBAC 和审计日志。
- 📊 **深度可观测性**：提供查询钻取和仪表盘，监控性能与错误，并集成 CloudWatch、Datadog、Prometheus 等工具。
- ⚡ **快速部署**：通过 SQL、CLI、Terraform、Cursor 或 Claude Code 在数分钟内完成数据库配置。
- 🔌 **生态集成**：与主流云提供商及 PostgreSQL 生态系统无缝对接。
- 🛡️ **企业级支持**：提供合同性 SLA、区域数据隔离、合规认证及 24/7 全球专家支持。

---

### [揭秘视图过渡伪树 – Master.dev 博客](https://master.dev/blog/demystifying-the-view-transition-pseudo-tree/)

**原文标题**: [Demystifying the View Transition Pseudo Tree – Master.dev Blog](https://master.dev/blog/demystifying-the-view-transition-pseudo-tree/)

本文深入解析了 CSS View Transitions API 中的伪元素树结构，帮助开发者理解各层作用并自定义过渡动画。

- 🌳 **伪元素树结构**：每次视图过渡时，HTML 元素上会生成伪元素树，包含`::view-transition`、`::view-transition-group`、`::view-transition-image-pair`、`::view-transition-old`和`::view-transition-new`，其中根元素默认覆盖所有交互内容。
- 🎯 **view-transition-group 的作用**：负责位置、大小和旋转的动画，浏览器自动生成矩阵动画（如从`(8,8)`到`(108,108)`），建议用独立 CSS 属性自定义时长、延迟和缓动，避免覆盖默认值。
- 🧩 **view-transition-image-pair 的隔离**：仅应用`isolation: isolate`属性，创建新堆叠上下文，确保子元素的混合模式互不干扰。
- 🔄 **old 与 new 的动画**：默认添加淡入淡出和混合模式动画（`plus-lighter`），当新旧状态尺寸或内容不同时，动画可能异常，需额外代码修复（如调整宽高比）。
- 💡 **自定义技巧**：理解伪树层级可精准控制动画，利用浏览器默认行为简化开发，例如通过修改`view-transition-name`分离元素并置于顶层。

---

### [WWDC26：HTML 模型元素入门 | Apple - YouTube](https://www.youtube.com/watch?v=AwAn6dgcq4c)

**原文标题**: [WWDC26: Get started with the HTML Model Element | Apple - YouTube](https://www.youtube.com/watch?v=AwAn6dgcq4c)

本頁面概述了 YouTube 平台的相關資訊與政策。

- 📰 **新聞中心**：提供 YouTube 的最新消息與公告。
- ©️ **版權**：說明內容創作者的版權相關規定。
- 📞 **聯絡我們**：提供用戶與 YouTube 聯繫的方式。
- 🎬 **創作者**：針對內容創作者的資源與支援。
- 📢 **刊登廣告**：說明在 YouTube 上投放廣告的選項。
- 👨‍💻 **開發人員**：提供給開發者的技術文件與工具。
- 📜 **條款**：規範用戶使用服務的條款與條件。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋平台內容政策與安全措施。
- ⚙️ **YouTube 的運作方式**：解釋平台的功能與機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能。
- ©️ **版權資訊**：顯示版權年份與所屬公司（2026 Google LLC）。

---

### [步入空间网络：Apple Vision Pro 中的 HTML 模型元素 | WebKit](https://webkit.org/blog/17118/a-step-into-the-spatial-web-the-html-model-element-in-apple-vision-pro/)

**原文标题**: [  A step into the spatial web: The HTML model element in Apple Vision Pro | WebKit](https://webkit.org/blog/17118/a-step-into-the-spatial-web-the-html-model-element-in-apple-vision-pro/)

## 概述总结

Apple Vision Pro 的 visionOS 26 默认启用 HTML `<model>` 元素，为空间网页提供简单易用的 3D 模型集成方案。

- 🌐 **空间网页新基石**：`<model>` 元素让现有网页轻松嵌入 3D 模型（如 USDZ 文件），在 Vision Pro 上以立体方式呈现，无需复杂 JavaScript 库。
- ⏳ **加载状态管理**：通过 `ready` Promise 确保模型下载和处理完成；环境贴图加载则依赖 `environmentMapReady` Promise。
- 🔄 **交互模式简化**：设置 `stagemode="orbit"` 即可让用户通过捏合拖拽旋转模型，类似 AR Quick Look 体验。
- 🎛️ **精细控制**：使用 `entityTransform`（基于 DOMMatrix）调整模型位置、旋转和缩放；支持 `play()`/`pause()` 等 API 控制动画播放。
- 💡 **光影真实感**：通过 `environmentmap` 属性指定高动态范围（HDR）环境贴图（如 OpenEXR 格式），让模型在不同光照下更逼真。
- 📐 **尺寸与边界**：模型加载后提供 `boundingBoxCenter` 和 `boundingBoxExtents`，便于开发者自定义初始变换。
- 🛠️ **创作工具**：支持 USDZ 格式，可通过 Reality Composer、Blender 等工具创建模型；Polyhaven 等网站提供免费环境贴图。
- 📢 **开放标准与反馈**：该元素遵循 W3C 和 WHATWG 提案，欢迎通过 Mastodon、X 或 WebKit 漏洞追踪器提交反馈。

---

### [打造难忘的网页体验：现代 CSS 工具包 | CSS 技巧](https://css-tricks.com/creating-memorable-web-experiences-a-modern-css-toolkit/)

**原文标题**: [Creating Memorable Web Experiences: A Modern CSS Toolkit | CSS-Tricks](https://css-tricks.com/creating-memorable-web-experiences-a-modern-css-toolkit/)

### 概述摘要
本文介绍了使用现代 CSS 技术创建令人难忘的网页体验的方法，强调通过运动设计、文本动画、遮罩裁剪、滚动驱动动画、3D 变换和自定义光标等工具，在无需复杂 JavaScript 的情况下实现生动、可访问且高性能的交互效果。

- 🎨 **运动即沟通**：通过关键词列表（如“迷幻蘑菇派对”与“精神蘑菇静修”）定义设计意图，确保动画支持信息传达，避免过度装饰。
- ✂️ **拆分文本动画**：使用 CSS 自定义属性实现字符逐帧动画（如`slideUp`），并需注意辅助技术兼容性（如`aria-hidden`与屏幕阅读器测试）。
- 🖼️ **遮罩与裁剪**：`clip-path`用于几何形状的二进制隐藏，`mask`支持渐变透明度，例如用`circle(0%)`到`circle(100%)`实现圆形展开效果。
- 🌀 **滚动驱动动画**：通过`animation-timeline: view()`将动画与滚动进度绑定，利用自定义属性`--offset`控制不同元素的速度差异（如视差效果）。
- 🎲 **3D 变换**：使用`perspective`和`transform-style: preserve-3d`创建深度场景，结合滚动驱动动画实现旋转和 Z 轴平移（如`rotateY`）。
- 🖱️ **自定义光标**：通过`cursor`属性替换默认光标（建议 32×32px PNG/SVG），但需谨慎应用以避免破坏默认交互行为。
- 🔗 **锚点定位**：利用 CSS 锚点定位将单个伪元素附着到悬停元素，实现流畅的卡片高亮过渡（如`linear()`缓动函数）。
- ⚡ **性能与可访问性**：优先使用 GPU 加速的 CSS 动画，尊重用户运动偏好（`prefers-reduced-motion`），并测试屏幕阅读器兼容性。

---

### [获取失败](https://cloudfour.com/thinks/improvements-to-web-for-ai-should-benefit-all-users/)

**原文标题**: [Failed to retrieve](https://cloudfour.com/thinks/improvements-to-web-for-ai-should-benefit-all-users/)

无法总结：获取内容失败，状态码 403。

---

### [WebMCP · 议题 #670 · WebKit/standards-positions · GitHub](https://github.com/WebKit/standards-positions/issues/670#issuecomment-4608432694)

**原文标题**: [WebMCP · Issue #670 · WebKit/standards-positions · GitHub](https://github.com/WebKit/standards-positions/issues/670#issuecomment-4608432694)

WebMCP 提案在 WebKit 标准立场中被标记为反对，涉及多项设计、隐私和安全顾虑，主要面向浏览器内置 AI 代理和跨域 iframe 中的脚本代理。

- 🤖 **AI 代理双场景**：提案支持两种用例——浏览器内置原生代理（如 Chrome 侧边栏的 Gemini）和跨域 iframe 中的 JavaScript 代理，后者因开发者需求而新增。
- ❌ **API 设计问题**：被标记为“API 设计”顾虑，指出该 API 易出错、命名不佳或与平台不一致。
- 🔄 **功能重复**：存在“重复”顾虑，认为提案复制了现有 Web 平台功能。
- 🌐 **国际化不足**：未充分考虑不同语言或区域设置，引发“国际化”担忧。
- 📱 **可移植性困难**：可能难以在重要平台上实现，涉及“可移植性”问题。
- 🔒 **隐私与安全风险**：实施后可能带来隐私和安全风险，分别被标记为“隐私”和“安全”顾虑。
- 📝 **用例不明确**：用例陈述不清或模糊，导致“用例”顾虑。
- 🏢 **标准场所不当**：提案处于错误的标准或孵化场所，引发“场所”顾虑。
- 🏷️ **来源与立场**：由 Google 和 Microsoft 共同编辑，但 WebKit 立场为“反对”，涉及 AI、表单、用户同意和 Web API 等主题。

---

### [再次挑战完美 CSS 饼图...无需 JavaScript！ | CSS 技巧](https://css-tricks.com/another-stab-at-the-perfect-css-pie-chart-sans-javascript/)

**原文标题**: [Another Stab at the Perfect CSS Pie Chart... Sans JavaScript! | CSS-Tricks](https://css-tricks.com/another-stab-at-the-perfect-css-pie-chart-sans-javascript/)

本篇文章探讨了如何用纯 CSS 实现饼图，完全摒弃 JavaScript，同时保持语义化和可定制性。

- 📊 核心挑战：CSS 无法直接获取子元素状态，需将数据从子元素移至父元素，通过索引变量实现
- 🧩 解决方案：在父元素上定义 `data-percentage-N` 属性，利用 `attr()` 和 `nth-child()` 将值传递给对应切片
- 🔄 累积计算：通过 `--accum-N` 变量在父级逐步累加前 N-1 个切片值，再分配给子元素
- 🎨 默认颜色：使用 `sibling-index()` 和 `sibling-count()` 自动生成色相，支持自定义颜色覆盖
- ♿ 无障碍：保留语义化标签（如 `<li>` 和 `<span>`），通过 `counter()` 显示百分比数据
- 🧪 扩展性：相同方法可应用于柱状图，并支持 Web Component 渐进增强（需 JavaScript 时再启用）
- ⚠️ 局限性：当前需重复编写 CSS 规则，未来 CSS `@function` 或可简化，目前可用预处理器优化

---

### [用于此的道具 · 2026 年 6 月 13 日](https://nerdy.dev/prop-for-that)

**原文标题**: [Prop For That · June 13, 2026](https://nerdy.dev/prop-for-that)

### 概述摘要
Prop For That 是一个 JS 库，通过将动态信息（如输入值、指针位置、滚动条大小等）实时映射为 CSS 自定义属性，弥补 CSS 无法直接获取 JS 数据的短板，让开发者无需编写繁琐的 JS 代码即可在 CSS 中实现动态效果。

- 🎯 **核心动机**：解决 CSS 无法直接使用 JS 动态信息（如输入值、指针位置、滚动条大小等）的常见痛点，避免重复编写 JS 代码。
- 🧩 **支持的属性**：涵盖指针位置、视口大小、元素可见性、输入状态、图像颜色、视频进度、设备信息（电池、网络、CPU）等数十种动态属性，且采用插件化按需加载。
- 🛠️ **使用方式**：通过 `data-props-for` 属性声明所需属性，自动生成实时 CSS 自定义属性，支持与 CSS 样式查询（Style Queries）结合，如 `@container style(--live-all-valid: 1)`。
- 🚀 **性能优化**：所有属性以插件形式按需加载，避免不必要的资源消耗，确保轻量高效。
- 💡 **社区反馈**：用户赞赏其优雅的桥接能力（如指针位置、图像颜色提取），但需注意 Firefox 开发者版可能存在稳定性问题；开发者已快速响应修复（如键盘几何属性支持）。

---

### [prop-for-that：CSS 响应，JS 仅监听](https://prop-for-that.netlify.app/)

**原文标题**: [prop-for-that: CSS reacts, JS just listens](https://prop-for-that.netlify.app/)

该工具库"prop-for-that"通过自定义属性`data-props-for`，让 CSS 直接读取各种实时状态，无需 JavaScript 处理。

- 🚀 **快速入门**：只需导入一次`prop-for-that/auto`，在元素上添加`data-props-for`属性并列出所需属性名即可。
- 👆 **指针追踪**：`pointer-local`为元素提供`--live-local-pointer-x-ratio`等属性，实现鼠标跟随、倾斜效果。
- 📜 **滚动触发**：`visibility`提供`--const-has-entered`（进入后锁定）和`--live-visible`（实时可见），实现一次性显示动画。
- 🎚️ **范围滑块**：`range`绑定滑块值，多个元素可读取同一`--live-value`，并通过`@container style()`查询实现离散状态。
- 🎨 **样式查询**：`@container style()`可根据精确值切换整块 CSS 规则，替代`var()`无法实现的逻辑分支。
- ✏️ **输入字段**：`field`实时提供`--live-length`等属性，配合`minlength`/`maxlength`实现字符计数和状态反馈。
- 📐 **三角函数**：`pointer-local`结合 CSS 的`atan2()`、`cos()`、`sin()`，实现纯 CSS 的眼球追踪效果。
- ⏰ **时钟**：`clock`每秒更新`--live-seconds`，配合`calc()`旋转指针，仅需一个`setInterval`。
- 🌐 **全局状态**：`online`、`battery`、`fps`等全局属性写入`:root`，CSS 可直接读取网络、电量等环境信息。
- ⚡ **滚动速度**：`scroll-velocity`提供带惯性的`--live-scroll-velocity`，实现滚动跟随动画。
- 📏 **元素尺寸**：`size`通过 ResizeObserver 提供`--live-aspect`，无需媒体查询即可判断横竖屏。
- 🎬 **媒体播放**：`media`提供`--live-progress`，配合`@property`实现平滑的进度环动画。
- 🔋 **省电模式**：`battery`结合`@container style()`，在低电量时自动移除动画和重绘。
- 🖱️ **拖拽**：`pointer-local`和`size`结合，实现纯 CSS 拖拽，松开后自动回弹。
- 📋 **表单状态**：`form-state`和`field-state`追踪表单交互历史（脏、触摸、更改、提交），驱动进度条和提交按钮。
- 🖼️ **图片色彩**：`img-color`提取图片主色、强调色等 5 种颜色，用于阴影、背景等效果。
- 🎥 **视频色彩**：`video-color`实时采样视频主色，实现动态背光效果。
- 📚 **参考列表**：提供所有可用属性源（全局/元素）及其对应的`--live-*`变量名和功能说明。

---

### [Handsontable - 适用于 JavaScript、React、Angular 和 Vue 的 Handsontable 数据网格](https://handsontable.com/evaluation?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=frontendnation&utm_term=frontendnation)

**原文标题**: [Handsontable - Handsontable data grid for JavaScript, React, Angular, and Vue.](https://handsontable.com/evaluation?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=frontendnation&utm_term=frontendnation)

本页面介绍了 Handsontable 数据网格组件的试用与支持服务，强调 45 天试用期内的专家协助和全面功能体验。

- 🚀 **45 天试用期**：提供完整功能访问，支持实际数据和用例测试
- 🛠️ **专家支持**：由技术团队直接解答问题，协助验证可访问性、兼容性和合规性
- 📧 **专属客户经理**：Anna Bednarek 将在试用期间提供一对一服务
- 🎨 **主题构建器**：支持自定义数据网格外观
- 🔗 **多框架支持**：提供 JavaScript、React、Vue、Angular 版本
- 📚 **丰富资源**：包括文档、API 参考、案例研究、知识库和开发者论坛
- 🏆 **权威认证**：通过 ISO/IEC 27001:2023-08 安全审计
- 💼 **商业支持**：提供许可证审查、定价咨询和转售商合作选项

---

### [Mitos ASCII 工具](https://mitos-pied.vercel.app/)

**原文标题**: [Mitos ASCII Tool](https://mitos-pied.vercel.app/)

概述摘要：本文探讨了人工智能在医疗诊断中的应用，强调了其提高准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🩺 人工智能通过分析医学影像和病历数据，能辅助医生更快速、准确地诊断疾病。
- 📊 机器学习模型可识别早期病变迹象，如癌症，提升早期干预的成功率。
- 🔒 数据隐私问题突出，患者信息的安全存储和使用需严格规范。
- ⚖️ 算法偏见可能导致诊断不公，需要多样化训练数据来减少偏差。
- 🚀 人工智能有望降低医疗成本，但需平衡技术发展与伦理考量。

---

### [GitHub - oxidecomputer/mitos: 品牌资产 ASCII 艺术生成器 · GitHub](https://github.com/oxidecomputer/mitos/)

**原文标题**: [GitHub - oxidecomputer/mitos: ASCII art generator for brand assets · GitHub](https://github.com/oxidecomputer/mitos/)

Mitos 是 Oxide Computer Company 开发的 ASCII 艺术生成器，可将图像、GIF 和代码转换为 ASCII 文字插图，支持实时预览和多种导出选项。

- 🎨 支持从图像、GIF 和自定义 JavaScript 代码生成 ASCII 艺术
- ⚙️ 提供亮度、对比度、抖动和反转等预处理控制
- 🔤 可自定义 ASCII 字符集，实现个性化输出
- 👁️ 实时预览功能，支持缩放和平移操作
- 🎬 动画支持，包含播放控制功能
- 📤 多种导出选项，并带有网格覆盖功能
- 🛠️ 基于 React、TypeScript、Vite 和 TailwindCSS 构建
- 📚 使用 CodeMirror 作为代码编辑器，gifuct-js 处理 GIF
- 🏢 基于 play.core 库，API 受 GLSL 编程启发
- 🔒 当前为内部工具，与 Oxide 设计系统紧密集成

---

### [探索 MapKit JS 6：为现代 Web 开发者重建 | WebKit](https://webkit.org/blog/18027/discover-mapkit-js-6-rebuilt-for-todays-web-developer/)

**原文标题**: [  Discover MapKit JS 6: Rebuilt for Today’s Web Developer | WebKit](https://webkit.org/blog/18027/discover-mapkit-js-6-rebuilt-for-todays-web-developer/)

MapKit JS 6 为现代网页开发者重新构建，带来更简洁的集成方式与更强大的功能，让你轻松将 Apple Maps 的强大功能融入网站或网页应用。

- 🗺️ **新版亮点**：MapKit JS 6 针对现代网页开发模式进行了重构，支持 NPM 包加载、标准 EventTarget 事件模型和原生 Promise，简化开发流程。
- 🔑 **简化令牌设置**：现在可直接从 Apple Developer 网站生成静态令牌，绑定域名即可使用，无需管理私钥或自签名。
- 📦 **NPM 包加载**：通过 `npm install @apple/mapkit-loader` 安装，自动集成 TypeScript 支持，并可按需加载库以优化性能。
- 🏞️ **快速创建地图**：只需几行代码即可创建交互式地图，支持通过坐标和相机距离设置视图，并兼容 React 等 UI 框架。
- 📍 **增强地点标注**：新增 `PlaceAnnotation` 和 `PlaceLookup`，支持通过 Place ID 获取地点信息并自动添加标注，同时可显示详细信息的 `PlaceSelectionAccessory`。
- 🔄 **标准事件处理**：采用浏览器原生 `addEventListener` 模式，轻松实现地图与列表的双向交互，如选择标注时更新列表项。
- 🌐 **全面网页集成**：从令牌配置到 NPM 加载，再到事件处理和地点查找，v6 让 Apple Maps 的网页集成更自然、更高效。

---

### [优胜美地探险者](https://webkit.org/demos/yosemite/)

**原文标题**: [Yosemite Explorer](https://webkit.org/demos/yosemite/)

优胜美地国家公园是一个以壮丽山谷、古老红杉和花岗岩峰顶闻名的自然奇观，提供实时兴趣点导航，方便游客规划行程。
- 🗺️ 公园地图：提供卫星视图和实时兴趣点，帮助探索公园
- 🛰️ 卫星视角：从高空俯瞰公园全貌，定位关键地标
- 🌲 加州国家公园：聚焦优胜美地，展示其独特地理环境
- ⛰️ 探索经典山谷：深入体验标志性的峡谷景观
- 🌳 古老红杉林：欣赏千年巨杉的雄伟与历史
- 🪨 花岗岩峰顶：仰望如半圆顶等著名岩石地貌
- 📍 实时兴趣点：获取公园内景点、步道和服务设施的即时信息
- 🗓️ 规划游览：利用这些资源高效安排行程

---

### [Templatical — 开源邮件编辑器 SDK](https://templatical.com/)

**原文标题**: [Templatical — Open-Source Email Editor SDK](https://templatical.com/)

这是一个开源、拖拽式邮件编辑器 SDK 的概述。

- ⭐ 开源且免费：基于 FSL-1.1-MIT 许可证，可商用、自托管，两年后自动转为 MIT 协议。
- 🧩 核心功能完整：包括自定义区块、合并标签、显示条件、主题系统、暗黑模式、MJML 输出等，无付费墙。
- 🔌 框架无关：支持 React、Svelte、Angular、Vue 和原生 JS，只需一次 `init()` 调用，零依赖。
- 🎨 可完全定制：支持白标、设计令牌、可插拔媒体库（S3、Cloudinary 等），样式隔离（Shadow DOM）。
- 🚀 快速集成：`npm install` 后即可嵌入应用，输出 JSON 和 MJML，可在任何地方渲染。
- 🏢 对比 SaaS 构建器：无需按席位付费，无功能限制，可审计和扩展，适合需要深度嵌入的产品。
- ☁️ Templatical Cloud（付费）：提供 AI 改写、实时协作、版本历史、多租户等云端功能，与开源 SDK 互补。
- 📦 体积小：初始 155 kB，懒加载 273 kB，无遥测，注重隐私。
- ♿ 可访问性：内置 WCAG 无障碍检查与自动修复，支持键盘导航和屏幕阅读器。

---

### [模板化游乐场](https://play.templatical.com/)

**原文标题**: [Templatical Playground](https://play.templatical.com/)

中国在科技创新领域取得显著进展，人工智能、5G 通信和新能源技术发展迅速，推动了经济高质量发展。政府加大对基础研究的投入，鼓励企业创新，并加强知识产权保护。同时，中国积极参与全球科技合作，推动构建开放型世界经济。这些举措有助于提升国家竞争力，并应对全球性挑战。

- 🤖 人工智能与 5G 通信技术快速发展，成为经济增长新引擎。
- 🌱 新能源技术取得突破，助力绿色低碳转型。
- 💰 政府增加基础研究投入，支持企业创新与知识产权保护。
- 🌍 中国积极参与全球科技合作，推动开放型世界经济构建。
- 🚀 科技创新提升国家竞争力，有效应对气候变化等全球挑战。

---

### [GitHub - templatical/sdk: 开源拖放式邮件编辑器。支持 JSON 模板、MJML 渲染、框架无关。内置 Vue + TipTap。](https://github.com/templatical/sdk)

**原文标题**: [GitHub - templatical/sdk: Open-source drag-and-drop email editor. JSON templates, MJML rendering, framework-agnostic. Vue + TipTap inside. · GitHub](https://github.com/templatical/sdk)

Templatical 是一个开源拖拽式邮件编辑器，可嵌入任何 Web 应用，支持 JSON 模板和 MJML 输出，提供 14 种区块类型和高级功能。

- 📧 **核心功能**：开源拖拽式邮件编辑器，支持 JSON 模板和 MJML 输出，确保邮件在各客户端正确渲染
- 🔌 **框架无关**：基于 Vue 但可嵌入 React、Svelte、Angular 或原生 JS，通过单一`init()`函数调用
- ⚡ **高级特性**：自定义区块（支持 API 数据源）、可插拔合并标签语法、显示条件、完整主题设计令牌
- ☁️ **云服务**：开发中的付费云层包括 AI 重写、实时协作、评论、快照、多租户等功能
- 🛠️ **技术栈**：14 种区块类型、Shadow DOM 样式隔离、TypeScript 严格类型、~1400 单元测试+Playwright E2E 测试
- 📦 **包结构**：编辑器包（FSL-1.1-MIT 许可，2 年后转 MIT）、渲染器/类型/导入器（纯 MIT 许可）
- 🚀 **快速开始**：`npm install @templatical/editor @templatical/renderer`，简单初始化即可使用
- 🌐 **多语言支持**：内置英文和德文，易于添加更多语言
- 🤝 **开源贡献**：欢迎贡献代码、报告问题，由个人开发者维护并接受 GitHub 赞助

---

### [GitHub - SikandarJODD/animations: 使用 Tailwind CSS 和 Motion SV 构建的 Svelte 5 动画，包含 Magic UI 和 Spell UI · GitHub](https://github.com/SikandarJODD/animations)

**原文标题**: [GitHub - SikandarJODD/animations: Svelte 5 Animations includes Magic UI, Spell UI build using Tailwind CSS & Motion SV · GitHub](https://github.com/SikandarJODD/animations)

概述：这是一个专为 Svelte 5 设计的动画组件库，包含 Magic UI、Spell UI 和 Fancy Components 三类组件，基于 motion-sv、Tailwind CSS 和 Shadcn Svelte 构建，提供免费、可复制粘贴的动画解决方案。

- 🎨 包含 88 个动画组件：Magic UI 57 个、Spell UI 21 个、Fancy Components 10 个
- 🚀 快速安装：通过 pnpm 创建项目，选择 Tailwind CSS，安装 motion-sv 和 shadcn-svelte，即可添加组件
- 📂 注册表结构：使用/r/访问 Magic UI，/s/访问 Spell UI，/f/访问 Fancy Components
- 🙏 致谢原创者：灵感来自 Tom（Spell UI）、Daniel Petho（Fancy Components）和 Dillon Verma（Magic UI）
- 🔧 开源贡献：支持创建 Issue、赞助项目，遵循 MIT 许可证
- 🌐 在线文档：主文档、Spell UI 和 Fancy Components 均可在 sv-animations.vercel.app 查看

---

### [Svelte 动画组件](https://sv-animations.vercel.app/)

**原文标题**: [Svelte Animations Components](https://sv-animations.vercel.app/)

概述摘要
Svelte Animations 是一个提供 50 多种免费开源动画组件和效果的项目，基于 Svelte、TypeScript、Tailwind CSS 和 Motion SV 构建，支持 CLI 和响应式设计。

- 🎨 提供 50 多种免费开源的动画组件和效果
- 🔧 基于 Svelte、TypeScript、Tailwind CSS 和 Motion SV 构建
- 💻 支持 CLI 命令行工具，便于快速集成
- 📱 组件完全响应式，适配不同设备
- 🆕 包含新推出的 Fancy Components 功能
- 🔍 内置搜索和主题切换功能（如命令面板、深色/浅色主题）

---

### [OneGlanse | 开源地理空间与人工智能可见性追踪器](https://oneglanse.com/)

**原文标题**: [OneGlanse | Open-source GEO & AI Visibility Tracker](https://oneglanse.com/)

### 概述总结
OneGlanse 是一款开源 AI 可见性与 GEO（生成引擎优化）追踪工具，可监控品牌在 ChatGPT、Gemini、Perplexity、Claude 和 Google AI Overview 中的表现，并提供可见性、排名、情感和推荐强度等指标。

- 🔍 **品牌可见性追踪**：监控品牌在主流 AI 产品中的出现率、排名和情感，如 HubSpot 可见性达 86%，排名第一。
- 📊 **竞争对比看板**：展示竞争对手在可见性、提及次数和情感上的对比，如 HubSpot 领先于 Salesforce、Adobe Marketo 等。
- 🧠 **真实 AI 响应分析**：查看 AI 生成的完整回答，包括来源归属和分析指标，如 ChatGPT 和 Gemini 的 GEO 评分和排名。
- 📈 **来源与引用追踪**：识别影响 AI 决策的发布者，如 g2.com 占引用份额 19.3%，共追踪 259 个 URL。
- 💡 **AI 感知洞察**：提取 AI 对品牌的定价定位、核心差异化和叙述主题，如 HubSpot 被描述为“统一 CRM 和营销自动化”。
- 🛠️ **自托管架构**：支持本地或 VPS 部署，使用自有账户和 API 密钥，数据完全由用户控制。
- 🆓 **完全免费开源**：MIT 许可，无订阅或使用限制，可审计的代码库和 Docker 部署。
- 📋 **多提供商支持**：统一追踪 ChatGPT、Gemini、Perplexity、Claude 和 AI Overview，通过真实 UI 而非 API 采集数据。

---

### [STRICH | 网页应用条形码扫描](https://strich.io/?ref=frontend-focus)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=frontend-focus)

STRICH 是一款专为网页应用设计的 JavaScript 条码扫描库，支持实时扫描 1D/2D 条码，无需原生应用或后端，提供透明定价和开发者友好体验。

- 📱 **无需原生应用**：直接在网页浏览器中扫描条码，兼容所有主流框架，零依赖。
- 💰 **透明定价**：基础版 $99/月（1 万次扫描），专业版 $249/月（10 万次扫描），企业版可定制，支持免费试用 30 天。
- 🚀 **高性能扫描**：采用 WebAssembly 和 WebGL 技术，速度快，能读取模糊、破损、反光或反向的条码。
- 🌐 **网页优势**：无应用商店限制，通过链接或二维码分发，一次开发覆盖所有平台，降低开发成本。
- 📋 **广泛条码支持**：支持 Code 128、EAN、QR Code、Data Matrix、PDF417 等 1D/2D 条码，包括美国驾照扫描。
- 🛠️ **开发者友好**：提供 TypeScript 绑定、详细文档、示例代码，支持 Angular/Vue/React 等框架。
- 🏢 **企业级功能**：定期更新、技术支持、白标定制、离线操作（零网络请求），符合 GS1 标准。
- ⭐ **客户好评**：用户称赞其速度快、集成简单、性能稳定，优于 ZXing-JS 和 Quagga 等免费替代品。

---

### [使用 Foxit 实现 API 驱动的文档工作流自动化](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/api-driven-document-workflow-automation/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260617)

**原文标题**: [API-Driven Document Workflow Automation with Foxit](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/api-driven-document-workflow-automation/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260617)

文档生成技术通过模板驱动 API 实现自动化，取代了低效的手动流程，核心流程是从 Word 模板和 JSON 数据生成 PDF 文件。

- 📄 **核心概念**：文档生成是将模板与数据动态合并，自动创建结构化文档（如 PDF）的技术。
- ⚙️ **模板驱动 API**：通过 API 接口，用 Word 模板和 JSON 数据作为输入，替代人工重复操作。
- 🔄 **完整流水线**：从 Word 模板+JSON 载荷 → 模板引擎解析 → 数据填充 → 生成最终 PDF 文件。
- 🚀 **解决痛点**：当文档量激增时，手动工作流效率低下，自动化生成可大幅提升速度与准确性。

---

### [色彩故事](https://storiedcolors.com/)

**原文标题**: [Storied Colors](https://storiedcolors.com/)

本内容是关于一个名为“颜色索引”的持续更新项目，从 2026 年开始，每天介绍一种颜色，包括其来源、化学性质及相关历史。项目强调真实记录，不回避不光彩的部分，每周日更新新条目，并不断修正旧条目。

- 📚 项目概述：从 2026 年起，每天记录一种颜色的来源、化学性质及历史，强调真实性和透明度
- 🗓️ 更新频率：每周日格林威治时间 06:00 发布新条目，旧条目根据实验室修正持续更新
- 📊 数据统计：已收录 252 个条目，引用 1160 个来源
- 🟡 本周标本：包括唐代御用黄（矿物，禁止平民使用）、印度黄（动物，来自牛尿，1908 年因虐待动物被禁）、靛蓝（植物，与 1859 年孟加拉靛蓝起义相关）
- 🆕 最新收录：6 种新颜色，如 1936 年铀红、1145 年沙特尔蓝、2016 年粉红粉等
- 🎨 收藏概览：共 252 个条目，提供浏览所有条目的入口
- 📧 订阅服务：提供偶尔的通讯，包含新条目、争议归因等内容，无广告，可随时退订

---

