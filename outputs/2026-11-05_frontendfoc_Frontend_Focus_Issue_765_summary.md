### [推出自适应深色模式 | WebKit](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/)

**原文标题**: [  Introducing Adaptive Dark Mode | WebKit](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/)

Safari 27.3 beta 推出“自适应深色模式”，可在用户开启深色外观后，自动将原本只有浅色版本的网站转换为深色显示，弥补深色模式用户需求与网站支持不足之间的差距。该功能深入 WebKit 引擎实现，兼顾显示效果、性能与隐私保护，同时为网站开发者提供了适配建议和完整深色模式支持方案。

- 🌙 Safari 27.3 beta 新增自适应深色模式，用户启用后 Safari 会把浅色网站呈现为深色。
- 📊 约 40% 的网页加载来自深色模式用户，但仅约 10% 的网页加载支持深色模式。
- ⚙️ 启用方式：将系统外观设为深色，访问亮色背景网站，点击 Safari 提供的预览中的“Try”。
- 🎨 已通过 `color-scheme` 声明支持深色模式的网站不会被改动；其余页面会被分析，偏暗页面保持不变，浅色页面自动适配。
- 🔄 核心是颜色变换：使用颜色矩阵反转明度并保留色相，目标达到 WCAG 4.5:1 对比度，并处理渐变、按钮、文字与背景对比。
- 🖼️ 图片大多保持不变；会检查 SVG 并在需要时转换颜色，对简单黑白位图 Logo 可分析像素直方图后反转。
- 🧩 某些情况下会关闭遮罩和 `mix-blend-mode` 等效果以避免异常；`<canvas>` 内容保持不变。
- 🛠️ 网站若采用现代实践效果更好：用 SVG 替代位图图标、用 CSS 纯色/渐变替代平铺背景图、使用透明背景内容图、增加容器内边距等。
- 🧑‍💻 完整深色模式支持可使用 `color-scheme` 元标签、`:root`/`body` 的 `color-scheme`、`prefers-color-scheme` 媒体查询、`<picture>`、`light-dark()`、`color-mix()`、`contrast-color()` 和 CSS 变量，并应尽早声明而非依赖 JavaScript 后注入。
- 🚫 若不想被转换，可用 `color-scheme: light only`；但 `only` 关键字在 Safari 27.3 beta 1 中尚不支持。
- 🔒 Safari 阻止网站检测自适应深色模式是否启用；JavaScript 查询 CSS 颜色会得到原始颜色，绘制到 canvas 的图像也保持原样，以减少指纹识别风险。
- ✉️ 网站管理者可通过 `web-evangelist@apple.com` 反馈；用户可通过 Feedback Assistant 报告适配不佳的网站。

---

### [Meticulous AI——无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q4_1&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q4_1&utm_content=primary)

Meticulous 是一款面向复杂代码库的自动化端到端测试工具，通过记录用户交互并由 AI 生成持续演进的视觉测试，在合并前展示代码变更影响；主打零开发维护、确定性执行、消除 flaky 与高速并行测试。

- 🚀 零开发投入：添加 recorder 脚本即可记录本地、预发布和预览环境会话，生产环境可选记录。
- 🤖 AI 自动生成并维护测试：覆盖代码分支、用户流程和边缘案例，测试随应用演进自动增删。
- 🔍 PR 合并前影响分析：提交拉取请求时即可查看变更对用户工作流的影响。
- 🧪 后端响应保存与回放：默认 mock 后端响应，测试无副作用、减少误报，无需测试账号或测试数据。
- ⚡ 确定性执行消除 flaky：从 Chromium 层构建调度引擎，执行速度快，适合复杂应用。
- 🧩 可补充或替代现有测试套件。
- 🏎️ 大规模并行测试：数千个屏幕可在 120 秒内返回结果。
- 🏢 受 100+ 组织信任，客户包括 Dropbox、Notion、Engine 等，并获得工程团队好评。
- 🔌 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit，并提供集成、安全与文档支持。
- ✅ 几分钟即可完成设置，开始自动生成覆盖全应用的测试。

---

### [现代 CSS 可能会让你的前端变得更复杂 — Smashing Magazine](https://www.smashingmagazine.com/2026/11/modern-css-might-make-your-front-end-more-complex/)

**原文标题**: [Modern CSS Might Make Your Front-End More Complex — Smashing Magazine](https://www.smashingmagazine.com/2026/11/modern-css-might-make-your-front-end-more-complex/)

现代 CSS 能让局部代码更简洁，却可能把复杂度转移到 CSS 与 JavaScript、布局、级联和渲染性能之间的交互中。文章通过四个真实迁移场景说明：只有明确归属、检查作用域、理解级联并测量性能，现代化 CSS 才真正降低系统复杂度，而不是制造更难排查的问题。

- 🧩 局部简洁不等于系统简单：删除大量 JavaScript 只减少单文件代码量，却可能增加需要理解和维护的交互关系。
- 👥 行为不能有两个主人：容器查询与 `ResizeObserver` 并存、断点更新不一致时，会出现没人写过却真实存在的混合状态；迁移后应删除旧观察器、类名和相关选择器。
- 📐 `container-type: inline-size` 不只启用容器查询：它还会创建新的块格式化上下文并施加尺寸包含，可能改变外边距折叠、浮动环绕和内容自适应宽度。
- 🃏 内容撑宽的卡片可能塌陷：若元素宽度来自内容，加入尺寸包含后可能变成 `0px`；应把 `container-type` 放到已有明确宽度的包装元素上，并在真实布局中测试。
- 🎯 `:has()` 选择器容易匹配过宽：`.card:has(img) p` 可能误伤评论头像和内部段落，并通过更高特异性覆盖组件自身规则；应使用 `>` 等组合器限制范围。
- ⚖️ 原生嵌套会借用选择器列表中的最高特异性：`&` 类似 `:is()`，可能让无关的 ID 权重影响组件；可用 `:where()` 将权重归零。
- 🧱 级联层不是默认救星：未分层的旧样式通常优先于分层的新样式；只有冲突双方都纳入分层时，层的作用才稳定可预期。
- ⏱️ 从 JavaScript 搬到 CSS 不代表更快：性能成本取决于属性、选择器和 DOM 规模；`:has()` 锚定大子树或与其他规则组合时可能产生意外重绘成本。
- 🔬 性能优化要测量：用 DevTools 记录交互前后“Recalculate Style / Layout / Paint”，启用选择器统计，并使用生产规模数据验证。
- 🧪 真实迁移常同时触发多个问题：一个 PR 可能同时造成断点逻辑残留、卡片消失、文本间距异常和列表选择卡顿；修复方向不是退回 JavaScript，而是修正归属、容器和选择器范围。
- ✅ 迁移前应回答六个问题：行为归属是否唯一？格式化上下文和周边布局会受何影响？哪些级联规则会冲突？旧实现是否彻底删除并测试所有状态？性能是否实测？下一位开发者能否理解规则边界？
- 🏁 结论：现代 CSS 很强，但新能力不会自动带来更简单的系统；只有具备单一所有者、经过检查的作用域、有意设计的级联位置和可验证的性能收益，迁移才算完成。

---

### [设计系统应默认快速 | Den Odell](https://denodell.com/blog/design-systems-should-be-fast-by-default)

**原文标题**: [
      Design Systems Should Be Fast by Default | Den Odell
    ](https://denodell.com/blog/design-systems-should-be-fast-by-default)

文章主张设计系统应把性能放在与可访问性同等重要的位置：组件一旦在真实数据量下变慢，所有使用它的应用都会受影响。作者实测 10 个流行开源设计系统，用 249 项国家下拉框和 100 个复选框揭示性能差异，剖析 Ionic、Material UI、UI5、React Spectrum、Ant Design 等慢因，并建议通过性能预算、自动化测试、虚拟化与“默认快速”设计防止回退。

- 🎯 核心主张：设计系统组件慢，使用它的所有应用都会慢；性能应进入设计系统团队优先级。
- 🧱 架构背景：浏览器主线程同时负责 JavaScript、用户事件和屏幕绘制，底层设计系统占用越少，应用可用时间越多。
- ⚠️ 当前问题：组件常在少量数据下隔离测试，真实应用用大量数据时才暴露变慢，应用团队又难以自行修复。
- 🧪 测试方法：2026 年 10 月测试 10 个开源设计系统，使用生产构建、Chrome v155、M1 Pro、CPU 降速 4 倍，测 249 项国家下拉框和 100 个复选框。
- 📊 下拉结果：Fluent 61ms、Carbon 63ms 最快；Ionic 1266ms 最慢，约为次慢 React Spectrum 227ms 的五倍多。
- ☑️ 复选框结果：Fluent 29ms、Carbon 41ms 最快；Ant Design 421ms 最慢，是 Material UI 70ms 的六倍。
- 🧩 框架非决定因素：同为 Lit，Carbon 与 Spectrum Web Components 差异明显；Ionic 下拉最慢，但复选框表现不差。
- 🐌 Ionic 原因：无 shadow DOM 的 ion-radio-group 触发 Stencil slot 修复，每新增选项重复检查已有子项，导致非线性变慢；建议改用 shadow DOM 或优化 Stencil 检查逻辑。
- 📦 Material UI/UI5原因：Material UI 一次渲染约 250 个选项未虚拟化；UI5 在隐藏 popover 中预置全部选项，打开时一次性计算约 1500 个元素样式。
- ⚙️ React Spectrum 原因：React Aria 打开时逐项清除高度并读取尺寸，造成布局抖动；应批量读写以减少重排。
- 🎞️ Ant Design 原因：100 个复选框逐个动画带来大量样式与绘制；应仅在直接选择时动画、批量选择时关闭动画，或改用合成器友好的透明度动画。
- 🧪 测试建议：用 Playwright 测量主线程 TaskDuration 与 LoAF 长帧，设置性能预算；关键测试是比较 250 项与 125 项的打开耗时比例。
- 🚀 默认快速：组件应在超过预算时自动虚拟化，默认采用快速行为，并在文档中标注已验证的容量上限。
- 📈 落地实践：每个 PR 自动跑性能测试，收集真实页面 Profiler，发布说明给出前后指标，持续防止性能回退。
- 📚 配套资源：作者开源了 design-system-performance-tests 仓库，包含各设计系统测试与 GitHub Actions 工作流，便于团队复制适配。

---

### [重新审视按钮与光标](https://www.abeautifulsite.net/posts/revisiting-buttons-and-cursors/)

**原文标题**: [Revisiting Buttons and Cursors](https://www.abeautifulsite.net/posts/revisiting-buttons-and-cursors/)

CSS 工作组已决定在 `appearance: base` 的默认样式中，为按钮及其他可点击表单控件使用 `cursor: pointer`，由此引发“手型光标是否只应代表链接”的争论；作者支持这一决定，认为 Web 用户已习惯可点击元素显示手型，而且目前这仅是未来默认值，不影响现有页面。

- 🖱️ 2026 年 10 月 21 日，CSS 工作组决议：在 `appearance: base` 新默认样式中，按钮和可点击表单控件使用 `cursor: pointer`。
- 📜 相关规则位于 CSS Forms Level 1 的“Cursors For Base Appearance”，覆盖按钮、选择框、复选框、单选框、文件选择按钮等。
- ⚖️ 争议类似“制表符 vs 空格”：有人支持手型光标提升可点击性的提示，有人认为手型应专属于链接。
- 📊 Nicole Sullivan 的设计系统数据曾显示 33 个系统中 27 个使用 `pointer`，扩充样本后接近 50/50。
- ♿ Elika Etemad 从可用性角度支持手型光标，认为它能让用户一悬停就明白该控件可点击。
- 🔗 Haz 担心手型光标会让人误以为按钮像链接一样可 ⌘-点击打开新窗口，且按钮可能不会改变 URL。
- 💬 作者自 2022 年起倾向跟随用户预期；并指出触屏没有光标，桌面浏览器悬停链接时还会在角落显示 URL。
- 🖥️ Jacob Paris 认为按钮使用标准光标更像桌面应用而非网站，但作者认为 Web 用户已学会“手型=可点击”。
- 🚧 目前不会立即改变现状：`appearance: base` 尚未被浏览器普遍支持，现有按钮和选择框仍多为 `appearance: auto` 与默认光标。
- 🛠️ 若现有 CSS reset、设计系统或 Web Components 已给按钮设置 `cursor: pointer`，可以继续保留；未来 `appearance: base` 只提供默认值，仍可自定义。
- ✨ 作者认为 Web 应更个性化、更有表达力，但涉及可访问性和整体用户体验时不宜过度。

---

### [Chrome 158 发行说明 - Chrome 平台状态](https://chromestatus.com/release-notes/158)

**原文标题**: [Chrome 158 Release Notes - Chrome Platform Status](https://chromestatus.com/release-notes/158)

Chrome 159 更新覆盖 CSS、Web 应用安装、媒体、权限策略、隔离式 Web 应用、设备与网络等方向，重点包括自定义高亮通用选择器、流式对齐关键字、SVG 嵌入对象适配、声明式 Web 应用安装、媒体状态伪类、OfflineAudioContext 增量渲染、焦点权限策略，以及 WebHID 与 WebTransport 增强。

- 🎨 CSS 新增 `::highlight(*)` 通用选择器，可匹配所有自定义高亮伪元素；其 `*` 参数不贡献优先级，适合作为基础样式，再由具名高亮规则覆盖。
- 🧭 CSS 新增 `flow-start` / `flow-end` 对齐关键字，作为 `flex-start` / `flex-end` 的别名，支持放置方向反转场景；序列化时优先返回 `flow-start/end`。
- 🖼️ `<object>` 和 `<embed>` 中的 SVG 文档开始支持 `object-fit` 与 `object-position`，行为类似 `<img>`，不再总是拉伸至整个内容框。
- 📲 新增 HTML `<install>` 元素，可通过清单 URL 和可选清单 ID 触发 Web 应用安装，无需 JavaScript；与 Web Install API 的 `navigator.install()` 并行提供声明式和命令式入口。
- 🌐 自 Chrome 158 起，Web Install API 允许网站提示用户安装跨源 Web 应用；管理员可通过 `WebAppInstallByUserEnabled` 企业策略和 `web-app-installation` 权限策略进行控制。
- 🎬 新增 `:playing`、`:paused`、`:seeking`、`:buffering`、`:stalled`、`:muted`、`:volume-locked` 等媒体元素伪类，用于根据 `<audio>` / `<video>` 状态匹配元素，属于 Interop 2026 重点方向。
- 🎧 `OfflineAudioContext` 支持增量渲染，通过分块处理音频图数据，避免一次性分配完整音频缓冲区，降低高数据量处理时的内存需求。
- 🔐 新增 `focus-without-user-activation` 权限策略，限制嵌入内容在无用户激活时进行程序化聚焦；不影响点击、Tab 等用户发起的聚焦，并支持焦点委托。
- ✍️ SVG `textPath` 新增 `side` 属性，可选择文字沿路径哪一侧排列；`side="right"` 可反转路径方向，便于在圆形路径内外放置文字而无需修改路径数据。
- ⭕ `circle()` 和 `ellipse()` 基础形状新增 `closest-corner` 与 `farthest-corner` 半径关键字，可用于 `clip-path`、`shape-outside` 和 `offset-path`，与径向渐变行为一致。
- 📦 隔离式 Web 应用的 Direct Sockets API 新增源特定多播（SSM）支持，加入多播组时可指定源地址，仅接收该源 UDP 数据，有助于简化路由并缓解欺骗与拒绝服务攻击。
- 🔌 WebHID API 扩展至 Android 版 Chrome 158，依赖 Android 17 / API 37 及以上系统支持，Web 暴露 API 不变；桌面平台自 Chrome 89 起已支持，WebView 不支持，并提供多项企业策略控制。
- 🚀 WebTransport 增强包括：构造提示可声明预期并发传入流数量；`draining` Promise 可在服务端优雅退役会话时通知应用；新增可靠性属性，用于指示是否支持仅可靠连接及不可靠数据报传输。

---

### [非 HTML 内容](https://xslt.rip/)

**原文标题**: [Non-HTML content](https://xslt.rip/)

无法总结：非 HTML 内容。

---

### [十月 Web 平台新动态 | 博客 | web.dev](https://web.dev/blog/web-platform-10-2026?hl=en)

**原文标题**: [New to the web platform in October  |  Blog  |  web.dev](https://web.dev/blog/web-platform-10-2026?hl=en)

2026 年 10 月，Chrome、Firefox 和 Safari 的稳定版与测试版带来多项 Web 平台更新，其中滚动驱动动画、作用域自定义元素注册表、JPEG XL、CSS 类型化算术等进入 Baseline 新近可用；模块、WebTransport、通知、HTML Sanitizer 及多个 CSS/安装 API 也有新进展。

- 🧭 稳定版发布：Chrome 155/156、Firefox 158/159、Safari 27.1/27.2 在 2026 年 10 月进入稳定版。
- 🎞️ 滚动驱动动画：Firefox 159 默认启用，可将 CSS/Web Animations 动画进度绑定到滚动偏移或元素可见性；Chrome、Safari、Firefox 均支持，达到 Baseline 新近可用。
- 🧩 作用域自定义元素注册表：Firefox 159 支持独立的 CustomElementRegistry 并限定到 Shadow Tree，减少全局命名冲突，达到 Baseline。
- 🖼️ JPEG XL：Chrome 155 和 Firefox 158 默认支持 image/jxl，涵盖有损/无损、渐进解码、HDR、透明、动画及 JPEG 无损转码；Firefox 同时更新 Accept 请求头。
- ➗ CSS 类型化算术：Firefox 158 支持在 calc() 等数学函数中把同类型不同单位相除得到无单位数值，达到 Baseline。
- ⏱️ PerformanceResourceTiming.deliveryType：Firefox 158 支持，可识别资源是否由缓存等方式交付。
- 🎲 CSS random()：Chrome 156 支持按范围和可选步长生成随机值，并可用 random-key 在属性/元素间共享随机值。
- 📐 CSS margin-trim：Chrome 155 支持在块容器和多列容器中裁掉子元素贴合边缘的外边距，避免首尾多余间距。
- 🔢 CSS symbols()：Chrome 155 支持在 list-style-type、counter() 等中内联定义匿名计数器样式，无需单独的 @counter-style。
- ✂️ text-decoration-skip-spaces：Chrome 155 支持让下划线、上划线、删除线跳过空白字符。
- 🧭 :navigation-source：Chrome 156 新增，匹配发起导航的链接、按钮或表单，并在导航期间保持选中。
- 📄 JS 文本模块导入：Chrome 155 支持 import ... with { type: "text" }，将模块内容作为字符串加载，加入 Firefox 行列。
- 🔁 模块加载重试：Chrome 156 不再永久缓存失败的模块加载，可在临时网络故障后再次调用 import()。
- 🌐 WebTransport：Firefox 158 增加 getStats() 和 supportsReliableOnly；Chrome 156 支持 CONNECT 握手自定义请求头并读取响应头。
- 🔔 Notification navigate：Firefox 158 支持 navigate 选项和 Notification.navigate，点击系统通知可跳转指定 URL，加入 Safari。
- 🧼 HTML Sanitizer API：Firefox 158 增加 javascriptURLs 配置和 setJavascriptURLs()；Firefox 159 让 setHTML() 等安全方法在解析阶段移除不需要的元素/属性。
- 🏷️ Safari 27.2：将 grid lanes 布局的 flow-tolerance 重命名为 fit-tolerance，保留 flow-tolerance 作为废弃别名。
- 🧪 Chrome 157 Beta：预览 CSS corner 简写/边缘子简写、text-decoration-inset、text-overflow:<string>、position-visibility 新值、HTML-in-canvas 渲染及能力元素 icon-only displaymode。
- 🧪 Chrome 158 Beta：预览 <install> 元素与 Web Install API（navigator.install()），以及 ::highlight(*)、媒体元素状态伪类、flow-start/flow-end、circle()/ellipse() 的 closest-corner/farthest-corner 半径。
- 🧪 Firefox 160 Beta：WebExtensions runtime.PlatformInfo 在 ARM64 上将 arch 返回为 arm64 而非 aarch64，与 Chrome 对齐。
- ⚠️ 兼容性说明：文章中的浏览器兼容数据来自 MDN，最新版本的数据可能尚未更新。

---

### [](https://developer.chrome.com/blog/new-in-devtools-november-2026)

**原文标题**: [New in DevTools - November 2026  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-devtools-november-2026)

Chrome 155 和 156 已于 2026 年 10 月进入稳定版；11 月 DevTools 更新重点包括面向编码代理的 CSS 样式检查、Elements 中的锚点定位可视化编辑、Application 中的 Web Install 与广告来源诊断，以及 Network、Memory、Performance 和可访问性等多面板改进。

- 🤖 **DevTools for agents**：新增 `get_css_styles` 检查计算样式与匹配样式，支持分页、继承规则、伪元素、`@keyframes` 和 `@` 规则；加入配置文件、路径控制、分块 trace 解析、对话框自动处理、控制台历史保留及菜单入口。
- 🧩 **Modern Web Guidance**：10 月新增无障碍生成内容、系统文字缩放、`@rule` 条件、响应式设计、短信验证码表单、交互绘制计时等指南，帮助编码代理使用平台新特性。
- ⚓ **Elements 锚点定位编辑器**：可在 Styles 面板点击 `position-area` 旁的色块，可视化选择锚点网格区域、同时或单独配置轴、切换 `self` 关键字并缩短无轴关键字。
- 🎯 **Elements 锚点调试**：支持从 popover 装饰器右键选择隐式锚点、在视口覆盖层检查 IMCB 的 margin、padding、border、content box，并可在 Flexbox 编辑器中切换 `wrap-reverse`。
- 🧹 **Elements CSS 改进**：可检查未生效的 `@starting-style` 与继承规则、编辑以三个及以上连字符开头的自定义属性，类名自动补全不再推荐已应用类。
- 📦 **Application Web Install 诊断**：Issues 面板可诊断 Web Install 清单错误，包括获取失败、语法错误、无效 `start_url`、缺少名称或 ID、缺少清单文件，并提供清单文件链接。
- 📢 **Application 广告与存储**：Ads 区新增 Ad provenance 列和指标说明；IndexedDB 支持动态行高展开嵌套对象并保留滚动位置；Cookies 表支持键盘或右键删除选中行。
- 🌐 **Network**：禁用缓存时，若 103 Early Hints 包含预加载链接会显示警告；本地响应覆盖、自定义请求/响应头列及排序在导航和重载后保留；可复制截断的原始请求负载。
- 🧠 **Memory**：堆快照可检测被共享 V8 执行上下文和长期存活闭包保留、但无活跃闭包访问的死上下文变量，并按内存影响排序。
- ⏱️ **Performance**：时间线缩放、平移和小地图拖动更流畅；切换面板后，Call tree 与 Bottom-up 的展开节点、选择和滚动位置保持不变。
- 🎛️ **其他改进**：Sensors 可覆盖 `navigator.cpuPerformance`；Device Mode 按模拟设备保留缩放并持久化 Save-Data；Color Picker 支持 APCA 对比度建议与 `oklab()`/`oklch()` 转换；无障碍改进包括非颜色指示点、屏幕阅读器播报和键盘焦点环。

---

### [支持为网站提供共享的 AI 训练控制 | Google 搜索中心博客 | Google for Developers](https://developers.google.com/search/blog/2026/10/ai-training-control)

**原文标题**: [Supporting a shared AI training control for websites  |  Google Search Central Blog  |  Google for Developers](https://developers.google.com/search/blog/2026/10/ai-training-control)

谷歌计划在 robots.txt 中支持共享的 AI 训练控制信号，帮助网站通过一次设置向多家 AI 提供商表达 AI 训练偏好。该机制基于 IETF AIPREF 工作组的工作，并将与 Google-Extended 等现有公司专属控制方式并行使用。若网站使用共享政策令牌选择退出训练且未明确指定 Google-Extended，谷歌计划将其视为禁止 Google-Extended；明确允许 Google-Extended 的网站仍可出现在 Gemini 应用的相关回答和点击中。该提案旨在回应出版商、民间社会、监管机构等对行业级 AI 训练控制的呼吁，并与欧盟《通用人工智能行为准则》保持一致。谷歌计划于 2027 年与其他 AI 提供商共同支持该新控制方式。

- 📅 公告日期为 2026 年 10 月 30 日，由 Google Search Advocate John Mueller 发布。
- 🤖 谷歌计划支持 robots.txt 中的共享 AI 训练控制，让网站一次性向多个 AI 提供商表达偏好。
- 🧩 新机制基于 IETF AIPREF 工作组成果，并建立在 Google-Extended 等现有控制措施之上。
- 🔤 网站可使用共享“政策令牌”设置广泛偏好，无需为每个 AI 开发者分别管理指令。
- 🚫 若网站用政策令牌选择退出训练且未明确指定 Google-Extended，谷歌计划将其视为禁止 Google-Extended。
- 🔁 现有公司专属控制将继续有效，网站可同时使用行业共享信号和针对个别 AI 开发者的定制指令。
- ✅ 明确允许 Google-Extended 的网站有资格出现在 Gemini 应用的相关回答中并获得点击。
- 🌍 该提案反映出版商、民间社会、监管机构等对行业级 AI 训练控制的呼吁，并与欧盟 GPAI 行为准则一致。
- 🗓️ 谷歌目标是在 2027 年与其他 AI 提供商共同支持该新控制，并持续更新进展。

---

### [](https://piccalil.li/blog/native-masonry-layouts-with-css-grid-lanes/)

**原文标题**: [
  Native masonry layouts with CSS grid lanes - Piccalilli
](https://piccalil.li/blog/native-masonry-layouts-with-css-grid-lanes/)

CSS 原生瀑布流布局终于通过 `display: grid-lanes` 落地：它复用 Grid 的轨道定义与放置属性，由浏览器自动把项目放入最合适的“泳道”，无需手动计算高度或依赖 Masonry.js。文章回顾了从 2017 年提案、Grid hack、语法争论到 2025 年确定 `grid-lanes` 的过程，并说明当前规范与浏览器支持仍在演进。

- 🧱 原生瀑布流长期是 CSS 难题，早期只能用多列布局或依赖精确高度的 Grid hack 近似。
- 🕰️ 2017 年 Rachel Andrew 提出 CSSWG 议题，Tab Atkins-Bittner 也给出过 Grid hack，但不适合动态内容。
- ⚔️ 语法争论持续多年：Mozilla/WebKit 倾向扩展 Grid，Chromium 曾主张独立的 `display: masonry`。
- ✅ 2025 年 CSSWG 决定复用 Grid 的轨道与放置属性，并在 12 月确定新布局模式名为 `grid-lanes`。
- ⚙️ 基本用法是 `display: grid-lanes` 配合 `grid-template-columns`、`repeat()`、`minmax()`、`gap` 等属性。
- 📦 浏览器按“最短泳道优先”的填充算法自动放置项目，各泳道可独立增长，不必共享行高。
- 🎛️ 仍可用 `grid-column: span 2` 等显式放置；显式定位和跨列项目会先被放置，再处理自动放置项目。
- ⚖️ `fit-tolerance` 由 `flow-tolerance` 更名而来，用于控制高度相近泳道是否视为平局；默认 `normal` 解析为 `1em`，`0` 偏向紧凑，`infinite` 更重源顺序。
- 🔄 定义列时项目纵向填充成 Pinterest 式布局；定义行时项目横向填充成砖墙式布局。
- 🧩 因复用 Grid 模型，`subgrid` 可与瀑布流配合，便于卡片内部元素对齐父级轨道。
- 🚧 目前规范仍是 Editor’s Draft，Safari 26.4+ 已支持，其他浏览器支持仍在推进，建议为不支持浏览器提供回退布局。
- ♿ 视觉顺序可能不同于 DOM 源顺序，需注意阅读顺序与屏幕阅读器可访问性。

---

### [](https://rachelandrew.co.uk/archives/2026/11/02/making-features-generic-in-css/)

**原文标题**: [Making features generic in CSS | Rachel Andrew](https://rachelandrew.co.uk/archives/2026/11/02/making-features-generic-in-css/)

文章介绍了 CSS 工作组如何将原本绑定于特定布局方式的功能逐步通用化，并以新关键字、`reading-flow`、`grid lanes` 子网格及特性检测为例，说明 CSS 设计中的兼容性、复杂性与真实用例的重要性。

- 🔄 CSS Box Alignment Level 3 新增 `flow-start` 和 `flow-end`，作为 `flex-start` 和 `flex-end` 的别名，也可用于 grid lanes（原 masonry/瀑布流）布局。
- 🧩 这种“先专用、后通用”的做法并非首次：`grid-gap` 后来泛化为 `gap`，旧名称仍保留为别名以避免破坏现有网站。
- 🧭 `reading-flow` 用于控制 grid、flex、block 布局中元素的焦点顺序；针对 grid lanes 已确定使用 `grid-lanes-flow` 和 `grid-lanes-track` 等专用值。
- ⚠️ 为不同布局保留专用值，是因为各布局需求不同，且 `reading-flow` 会改变焦点顺序，需要开发者谨慎、明确地使用。
- 🏗️ `grid lanes` 虽是独立的 `display` 值，却复用了 grid 属性，因此也带来了 `subgrid` 等复杂性。
- 🧱 关于 grid lanes 中的 `subgrid`，讨论正趋向只允许与父级同类型的子网格，但是否存在足够有价值的用例仍待确认，相关讨论见 Issue 14380。
- 🧪 独立的属性名或属性值组合更便于用 `@supports` 检测支持情况；`gap` 在 flexbox 中的检测曾遇到困难，`named-feature()` 可帮助解决此类问题。
- 🛠️ 文章最后强调，向 CSS 添加功能很困难，真实用例对设计至关重要；如果开发者有相关使用场景，应积极反馈给 CSS 工作组。

---

### [适用于静态网站的托管表单，无需后端 | CraftForms Cloud](https://craftforms.app/developers/?utm_source=frontendfocus&utm_medium=newsletter&utm_campaign=ff-2026-11-04-sponsored)

**原文标题**: [Hosted Forms for Static Sites, No Backend | CraftForms Cloud](https://craftforms.app/developers/?utm_source=frontendfocus&utm_medium=newsletter&utm_campaign=ff-2026-11-04-sponsored)

CraftForms 是一款面向静态网站的在线表单工具：无需后端，通过可视化编辑器建表，再把两行 HTML 嵌入任意网站即可收集提交；免费计划也支持无限提交，并具备预约、实时价格、押金和无验证码防垃圾功能。

- 🛠️ 无需后端即可运行，两行 HTML 嵌入任意静态站点，免费计划也可无限收集提交。
- 📅 支持预约、实时价格与押金，适合租赁等需要动态计价的场景。
- 🔒 每个表单密钥绑定网站，防止他人复制表单；嵌入代码内联渲染，无 iframe 尺寸问题。
- ⚡ 字段和价格运行时加载，表单编辑器中的修改会立即生效，无需重建静态站点。
- 💻 支持 localhost 和 127.0.0.1 测试，任意端口可用且不占用套餐网站名额。
- 🧩 兼容 Astro、Hugo、Eleventy、Next 等可输出 HTML 的框架，提供组件/短代码示例。
- 📡 也可自定义 HTML 并用 `fetch()` 以 JSON 提交；浏览器仅允许已注册网站或 localhost，服务器端无 Origin 可任意提交。
- 🚫 暂不支持普通 `<form action="...">` 重定向到感谢页，返回结果为 JSON。
- 🛡️ 通过填写行为、地址与表单频率限制防垃圾，无第三方验证码，访客无需解题。
- 🆓 免费版：1 个表单、1 个网站加 localhost，每月 100 封通知邮件、每小时最多 30 封，不支持支付和文件上传。
- 💳 Solo 版 €6/月，前 30 天免费：25 个表单、1 个网站，每月 2,000 封邮件或自有 SMTP，支持 Stripe/PayPal 支付与文件上传。
- 🏢 Studio 版 €22/月：200 个表单、25 个网站，每月 10,000 封邮件、每网站每小时 500 封，含 PDF 构建器。
- ⚠️ 当前限制：表单链接仅在你的 forms 地址上，尚不支持自有域名；内置集成仅 Mailchimp 和 Brevo，其余需 webhook；不支持纯 HTML 表单 POST。
- ✅ 可免费开始，无需信用卡；注册并确认邮箱后即可建表、添加 localhost 并在开发服务器中试用。

---

### [CSS 表格显示的怪癖与复古用途 | Vale.Rocks](https://vale.rocks/posts/table-display-values)

**原文标题**: [Quirks and Vintage Uses of CSS Table Display | Vale.Rocks](https://vale.rocks/posts/table-display-values)

文章回顾了 CSS 中表格相关 `display` 值的历史与怪异用途：它们只提供表格布局能力，不赋予表格语义；语义表格应继续用 `<table>` 标记表格数据，而 `display: table` 等曾在 flexbox/grid 之前用于布局技巧，如今多数应避免。

- 🧩 CSS `display` 提供 `table`、`table-row`、`table-cell`、`table-caption`、`table-column(-group)`、`table-header/footer-group` 等值，用于模拟表格元素的布局行为而非语义角色。
- ♿ 原生表格元素具有浏览器和辅助技术可识别的 ARIA 角色，适合二维表格数据；不要用 `div` 等元素随意重实现表格语义。
- 📱 在 flexbox 和 grid 普及前，表格布局值可让同一份 HTML 在桌面端显示为表格、移动端切换为内联布局，避免标记改动。
- 📏 常见历史技巧包括：用 `display: table` + `table-cell` 实现等高列，以及用 `table-cell` + `vertical-align: middle` 实现垂直居中。
- ⚡ `table-layout: fixed` 使用更简单快速的算法，某些超长数据列表等利基场景可获性能或溢出控制收益，但一般性能优化不应优先考虑 CSS 布局。
- ⚠️ 今天通常不应使用这些表格显示属性；若需要复杂布局，flexbox/grid 更合适，且表格 display 可能带来无障碍缺陷，作者引用 Adrian Roselli 的相关文章作现代说明。

---

### [错误](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/)

**原文标题**: [Error](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='blog.mistys-internet.website', port=443): Max retries exceeded with url: /post/2026/10/29/if-you-love-a-website-back-it-up/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [使用 three.js 扩散液体 | mofu](https://mofu-dev.com/en/blog/fluid-foundation/)

**原文标题**: [Spreading Liquid with three.js | mofu](https://mofu-dev.com/en/blog/fluid-foundation/)

本文回顾了作者为日本化妆品品牌粉底推广项目开发的“液体铺展”效果：它基于 three.js 流体模拟，通过速度图、高度图、透明度历史、法线计算和 Matcap 渲染，实现可拖拽、会残留、能混合的视觉化液体，并强调该方法追求观感而非物理精确。

- 🌊 该效果最初用于 2021 年粉底液推广项目，后在 Vue Fes Japan 2026 分享；演示用蓝色液体，可拖拽鼠标或手指体验。
- 🧪 核心复用此前的 three.js 稳定流体模拟速度图；高度图记录液体厚度，初始形态为中心凸起的半球形液滴。
- 🔁 厚度更新时，每个像素按速度回溯源 UV，从源位置采样高度，并减去/加上受限厚度；低速区域几乎不流动，以聚焦拖拽影响范围。
- ⚠️ 该方法不守恒液体体积，圆形拖拽会因采样偏差累积厚度；实现优先视觉效果，而非物理准确。
- 🖌️ 透明度图保存历史最大值与当前值的混合，使液体变薄后仍留有痕迹，模拟附着/残留，并非真实干燥或吸收。
- 💡 片元着色器通过高度图邻域采样计算法线，用 Matcap 提供颜色和高光，alpha 图控制透明度与残留。
- 🧮 附加实验显示：8 位纹理会造成高度量化和明暗阶梯，32 位浮点纹理的轮廓与光照更平滑。
- 🎨 还实现三种彩色液体混合：各自拥有高度图和 alpha 历史，共享速度图，并用简化 Kubelka–Munk 模型按厚度混色。
- 🤖 作者此时整理发布，是为记录自己推导出的实现方法，并感慨 AI 在坐标、空间和视觉实现方面进步迅速。

---

### [为什么拆分 Web 字体会拖慢文本布局和 INP——Ivan Kristianto](https://www.ivankristianto.com/split-webfont-text-layout/)

**原文标题**: [Why a split webfont slows text layout and INP - Ivan Kristianto](https://www.ivankristianto.com/split-webfont-text-layout/)

文章记录了一次多语言 WordPress 站点因拆分 Web 字体而导致文本布局变慢的排查与修复：字体拆分工具把基础拉丁字母分散到多个文件，浏览器需要多次字形整形和布局，从而拖慢交互呈现；修复重点是让基础拉丁字符集中在一个文件、避免 `unicode-range` 重叠，并为缺失脚本优先使用系统字体。

- 🔍 问题表现为部分站点 LCP、INP 上升，移动端 INP 超过 200 ms，但点击后的处理逻辑和 JavaScript 并不是主要原因，耗时集中在文本布局。
- ✂️ `cn-font-split` 默认拆分 Noto Sans SC 时生成 293 个文件，基础拉丁字符被分到两个文件，其中 `i`、`j` 等 11 个字符单独落在另一个文件里。
- ⚙️ Chromium 的字形整形一次只处理一个字体文件；一个单词跨多个字体文件时，需要多轮整形再拼接，因此字体文件越多，布局越慢。
- 📈 实验显示：拉丁字符在一个文件时布局约 3.2 ms，三个文件时约 6.0 ms；Noto Sans SC 拆分后也从约 3.3 ms 增至 4.7 ms。
- 🌍 阿拉伯语页面更严重：Web 字体不含阿拉伯字母但包含空格，导致空格和字母来自不同字体，每个单词都被分段整形。
- 🧩 修复时若把“干净拉丁文件”放在前面反而更慢；因为重叠的 `unicode-range` 规则会按倒序检查，最后声明的规则优先，所以应避免重叠，或把真正包含字形的规则放在最后。
- ✅ 生产修复包括：每个西方脚本使用一个字体文件、在生成的 CSS 中最后声明、阿拉伯语页面改用系统阿拉伯字体栈、无中文页面不再加载大型 CJK 样式表。
- 🧪 建议先用 `web-vitals` attribution 版本定位真实 INP，再用文章提供的脚本检查字体 CSS，确保常见单词不跨文件。
- ⚠️ 作者尚未获得字段数据，也未在真实手机上测试；实验数据来自降速 CPU 的 Mac，且测量的是布局时间而非 INP，结论仍需线上验证。
- 🔮 字体切片之间无法互相做字距调整，`Incremental Font Transfer` 可能改善该问题，但目前仍是 W3C 草案。

---

### [错误](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Error](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='www.tigerdata.com', port=443): Max retries exceeded with url: /go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [多列不同速度滚动 – Master.dev 博客](https://blog.master.dev/multi-column-different-speed-scrolling/)

**原文标题**: [Multi-Column Different-Speed Scrolling – Master.dev Blog](https://blog.master.dev/multi-column-different-speed-scrolling/)

本文介绍如何主要用 CSS 和 Scroll-Driven Animations 做出照片画廊的“多列不同速度滚动”效果：通过双列网格与随滚动变化的 translateY 动画，让右列看起来比左列滚得更快，甚至反向滚动；同时用 view() 动画为图片增加缩放漂移，并支持 popover 打开图片。文中强调渐进增强、响应式布局和无需 JavaScript 的主效果，也提到更复杂的反向滚动实现与 Codrops 的类似案例。

- 🖼️ 核心理念：在画廊中滚动只是探索图片的机制，不必局限于常规滚动方式，但应保留滚动条提示剩余内容。
- 🧩 使用 CSS Grid 搭建两列照片布局，并可通过自定义媒体查询在小屏下切换为单列。
- 🎞️ 利用 Scroll-Driven Animations 的 scroll() 时间线，让右列随页面滚动应用 translateY 动画，制造“滚得更快”的视觉错觉。
- 🛡️ 通过 @supports 做渐进增强，不支持滚动驱动动画的浏览器仍能正常浏览。
- 🔍 再用 view() 时间线为每张图片添加缩放和位移动画，让图片在进入视口时产生漂移效果。
- 🪟 图片还可通过 popover 打开，展示 Web 平台的新交互能力。
- 🔄 反向滚动方案更复杂：右列需要上移并配合 sticky 定位，还要根据滚动位置单独计算图片变换。
- 🧪 文章提供多个 CodePen 演示，并提到 Codrops 五年前有类似但基于 JavaScript 的实现；本文主效果无需 JavaScript。

---

### [获取失败](https://blog.master.dev/useful-custom-media-presets/)

**原文标题**: [Failed to retrieve](https://blog.master.dev/useful-custom-media-presets/)

无法总结：获取内容失败，状态码 429。

---

### [](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)

**原文标题**: [DeadTag: How Forgotten Website Tags Became a Delivery Network for iPhone Spyware](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)

Report URI 与 iVerify 联合调查发现，名为 DeadTag 的大规模恶意流量体系正利用网站遗留的过期第三方标签域名，向访客分发诈骗内容及 iPhone 漏洞利用工具；其中 Coruna 与 DarkSword 可零点击感染 iPhone 并窃取钥匙串密码和加密钱包资产。

- 🧩 **攻击入口**：网站长期保留已停用 analytics、广告等第三方标签；攻击者抢注过期域名后，所有仍加载该标签的页面会自动执行恶意脚本，无需入侵网站本身。
- 📊 **影响规模**：已确认 660+ 个过期再注册域名，嵌入数千个网站，保守估计每月影响约 1.35 亿次访问。
- 🕵️ **高度选择性规避**：恶意脚本仅约 2KB，会过滤搜索引擎、安全扫描器和机器人；由攻击者服务器逐个访客决定是否攻击，数据中心 IP 或频繁访问者常被静默忽略。
- 💰 **流量变现**：被选中的访客会被竞价重定向至假 VPN 弹窗、假调查/中奖页面、搜索广告、赌博与加密赌场骗局，以及 iPhone 漏洞利用页面。
- 📱 **iPhone 双漏洞套件**：同一广告网关将访客导向假 Polymarket 页面，并按 iOS 版本分发 Coruna（iOS 13–17.2.1）或 P7 DarkSword（iOS 18.4–18.7）。
- ☠️ **零点击间谍软件**：仅打开页面即可触发浏览器漏洞，无需点击或安装；植入后窃取钥匙串密码、加密钱包（Binance、Coinbase Wallet、OKX、Bitget、Trust Wallet、Exodus、TronLink、Bitpie 等）及设备/账户信息。两套工具均回传至同一服务器。
- 🏭 **其他传播途径**：该团伙还入侵数百家 PrestaShop 电商网站植入 DarkSword 加载器，并发现同时加载 Coruna 与 DarkSword 的零售商及数百个相关恶意站点。
- 🧭 **归因判断**：DeadTag 看似来源不明的商业化流量买卖；iPhone 漏洞团伙代码含简体中文注释，关联大量中文加密交易所、USDT/Tron 支付、赌博及仿冒站点，疑似中文语系、财务动机的加密盗窃行动。
- 🛡️ **网站防护建议**：审计并删除不再使用的第三方标签，监控脚本与域名变化，部署内容安全策略（CSP），并利用威胁情报识别 DeadTag、Coruna 和 DarkSword 基础设施。
- 📲 **iPhone 用户建议**：保持 iOS 最新；高风险用户开启锁定模式；若怀疑中招，应重启手机、更改钥匙串中保存的密码，并用新助记词将加密资产迁移至新钱包。
- 🔍 **核心提醒**：网站攻击面不限于自身代码，每个遗留第三方标签都是对他人域名持续安全的承诺；域名易主后，旧标签可能变成面向 iPhone 用户的投毒入口。

---

### [Polymarket 的 CSP 使这起 260 万美元加密货币盗窃的每个环节都得以](https://blog.report-uri.com/polymarkets-csp-allowed-every-part-of-the-2-6-million-crypto-theft/)

**原文标题**: [Polymarket's CSP Allowed Every Part of the $2.6 Million Crypto Theft](https://blog.report-uri.com/polymarkets-csp-allowed-every-part-of-the-2-6-million-crypto-theft/)

文章复盘了 Polymarket 因第三方监控脚本被篡改而损失约 260 万美元的链上盗窃事件，指出 CSP 的 URL 白名单无法阻止可信域名下脚本内容被替换，并介绍 SRI、Integrity Policy、CSP 哈希上报与 Script Watch 等完整性监控手段如何检测和阻断此类攻击。

- 🚨 2026 年 10 月 29 日，Polymarket 使用的 DebugBear RUM 内联加载脚本被篡改，约 50 分钟内盗走 2863 万枚 POL，价值约 260 万美元。
- 🧩 正常 JS 文件为 60,493 字节，攻击时被替换为 15,187 字节恶意文件；响应头从 Google Cloud Storage 特征变为 nginx ETag，显示文件在 10 月 27 日被修改。
- 🎯 恶意脚本专门针对 Polymarket：读取 localStorage 中的 auth params、proxyWallet 和 poly_clob_api_key_map，遍历 React 组件树找到订单客户端，并用 postOrder/createOrder 执行盗窃。
- 💸 自托管钱包用户的 outcome tokens 被 safeBatchTransferFrom 批量转至攻击者地址；邮箱登录用户持仓以 97%、50%、最低 tick 的 fill-and-kill 卖单抛售，现金经 Collateral Offramp 换成 POL 并通过 fun.xyz/Relay 转出。
- 🕵️ 所有交易经 Polymarket relayer 和 Deposit Wallet Factory，外观正常；脚本还向 data.debugbear.com 上报受害者组合、IP、国家、OS。
- ⛓️ 链上时间线：17:10:23 首笔 POL 到账；17:26:29–18:02:17 收到 36 笔批量转账，来自 33 个 deposit wallets、31 个 relayer 地址；18:19:58 钱包持有 28,636,284 POL。
- 🛡️ CSP 未阻止攻击：策略允许 cdn.debugbear.com 作为 script-src-elem，并在 connect-src 允许 data.debugbear.com、*.polymarket.com、*.alchemy.com、*.fun.xyz，正好覆盖所有请求；且没有 report-uri/report-to。
- ⚠️ CSP 基于 URL 白名单，只能判断主机是否可信，无法发现同一 URL 下脚本字节被替换；攻击前后脚本地址完全相同。
- 🔐 解决方案一：用 SRI 固定脚本哈希并配合 Integrity Policy 强制执行；可先用 Integrity-Policy-Report-Only 发现未加 SRI 的脚本，再阻断未加 SRI 或不匹配哈希的脚本。
- 📡 解决方案二：CSP 加入 'report-sha256'，让浏览器上报每个脚本的 SHA-256；Script Watch 按 URL 记录哈希并在文件变化时告警，Script Vault 可保存并下载实际执行的确切字节。
- 🌐 DebugBear 被数千网站以类似方式加载，攻击者理论上可在这些站点执行任意 JS；目前恶意脚本似乎只针对 Polymarket，其他站点暂未见被利用。
- ✅ 建议：立即移除 DebugBear RUM 嵌入代码；对所有第三方脚本使用 crossorigin、SRI、Integrity Policy、'report-sha256' 和 CSP 上报指令，持续监控脚本完整性。
- 🙌 事件由 Hudson Rock 发现载荷和钱包，DeFi Prime 发布早期技术分析；Report URI 提供 CSP Integrity、Script Watch、Script Vault 和 Integrity Policy 等完整性监控能力。

---

### [子资源完整性 - 安全 | MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity)

**原文标题**: [Subresource Integrity - Security | MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity)

子资源完整性（SRI）是一种浏览器安全机制，用于验证从 CDN 等第三方获取的资源未被意外篡改，从而防御供应链攻击。它通过要求资源内容匹配指定的加密哈希来工作，并涉及 CORS、策略头以及多种哈希生成工具。

- 🔐 SRI 允许浏览器在加载脚本或样式表前校验资源内容是否与预期哈希一致。
- 🛡️ 主要作用是防止第三方托管资源被攻击者替换或注入恶意内容，即防御供应链攻击。
- 📌 可用于 `<script>` 元素，以及 `rel` 为 `stylesheet`、`preload` 或 `modulepreload` 的 `<link>` 元素。
- 🧩 通过在元素上添加 `integrity` 属性，并提供以 `sha256-`、`sha384-` 或 `sha512-` 开头的 Base64 编码哈希值。
- ⚖️ 浏览器会优先使用 `integrity` 中最强的哈希算法；若资源哈希匹配任一指定值则加载，否则返回网络错误。
- 🌐 跨源使用 SRI 时必须遵循 CORS，通常需要添加 `crossorigin="anonymous"`，服务器也应发送相应的 `Access-Control-Allow-Origin` 响应头。
- 🚫 出于防止信息泄露的考虑，浏览器不允许 `no-cors` 请求使用 SRI，此类请求会失败。
- 📜 可通过 `Integrity-Policy` 头强制要求脚本和样式表具备完整性元数据，或用 `Integrity-Policy-Report-Only` 仅报告违规。
- 📝 违规报告类型为 `integrity-violation`，可包含文档 URL、被阻止资源 URL、目标类型及是否仅报告等信息。
- 🛠️ 可使用 SRI Hash Generator、OpenSSL 或 `shasum` 等工具生成 SRI 哈希；Windows 环境也可通过批处理脚本辅助生成。
- 💡 示例展示了在 `<script>` 上设置多个 SHA-384/SHA-512 哈希，以及通过 `Integrity-Policy` 头实施完整性策略的方式。

---

### [Integrity-Policy-Report-Only 标头 - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only)

**原文标题**: [Integrity-Policy-Report-Only header - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only)

该 HTTP 响应头用于在不强制执行子资源完整性策略的情况下，报告可能违反完整性策略的资源加载，帮助开发者在正式部署 `Integrity-Policy` 前测试策略并修复内容问题。

- 📌 `Integrity-Policy-Report-Only` 是 HTTP 响应头，仅在报告模式下工作；若策略被强制执行（使用 `Integrity-Policy`），它会报告原本会违反子资源完整性（SRI）保证的资源。
- 🌐 该功能不属于 Baseline，部分最常用浏览器对其支持有限。
- 🧩 违规报告可通过 Reporting API 发送；可在页面中使用 `ReportingObserver` 观察，也可发送到由 `Reporting-Endpoints` 定义、并通过 `endpoints` 选择的服务器端点。
- ⚙️ 头部值是结构化字段字典，键包括：`blocked-destinations`（必需，允许 `script`、`style`）、`sources`（可选，默认且唯一值为 `inline`）、`endpoints`（可选，报告端点名称）。
- 🧪 主要用途是让开发者先测试完整性策略、修复内容问题，再部署 `Integrity-Policy` 强制执行。
- 📨 示例中通过 `Reporting-Endpoints` 定义 `integrity-endpoint` 等端点，并用 `Integrity-Policy-Report-Only: blocked-destinations=(script), endpoints=(...)` 报告缺少 `integrity` 属性或 `no-cors` 模式请求脚本的情况。
- 📝 报告负载类型为 `integrity-violation`，包含 `documentURL`、`blockedURL`、`destination`，且 `body.reportOnly` 为 `true`。
- 🔗 相关主题包括 `Integrity-Policy`、`Reporting-Endpoints`、`ReportingObserver`、`IntegrityViolationReport`、Subresource Integrity 和 Reporting API。

---

### [错误](https://calendar.perfplanet.com/2019/self-hosting-third-party-resources-the-good-the-bad-and-the-ugly/)

**原文标题**: [Error](https://calendar.perfplanet.com/2019/self-hosting-third-party-resources-the-good-the-bad-and-the-ugly/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='calendar.perfplanet.com', port=443): Max retries exceeded with url: /2019/self-hosting-third-party-resources-the-good-the-bad-and-the-ugly/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://requestmetrics.com/web-performance/how-we-protect-our-javascript-agent/)

**原文标题**: [Error](https://requestmetrics.com/web-performance/how-we-protect-our-javascript-agent/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='requestmetrics.com', port=443): Max retries exceeded with url: /web-performance/how-we-protect-our-javascript-agent/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [加载第三方 JavaScript | 文章 | web.dev](https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript)

**原文标题**: [Load third-party JavaScript  |  Articles  |  web.dev](https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript)

本文说明第三方 JavaScript 虽能提供社交分享、视频、广告、分析、A/B 测试等功能，却可能拖慢页面性能、带来隐私与安全风险，并产生难以预料的行为；文章系统介绍了如何识别、测量、优化和安全加载第三方脚本。

- ⚠️ 常见第三方脚本包括社交分享按钮、视频嵌入、广告 iframe、分析与指标脚本、A/B 测试脚本及工具库。
- 🐢 主要风险：请求过多、JavaScript 过大占用主线程、未优化图片视频、缓存与压缩不足、阻塞渲染、使用 `document.write()`、重复加载框架等。
- 🔍 可用 Chrome DevTools、PageSpeed Insights、WebPageTest 识别耗时第三方脚本，并通过瀑布图和域名分解查看影响。
- 🧪 Lighthouse 的 JavaScript 启动时间审计可发现解析、编译、执行成本高的脚本，网络负载审计可发现大请求。
- 🚫 DevTools 网络请求阻断功能可屏蔽指定 URL，对比移除第三方资源前后的页面表现。
- 📊 在 Performance 面板录制并按产品分组排序，可找出加载时间最长的第三方脚本；建议开启网络与 CPU 节流并多次测量。
- 🌐 WebPageTest 支持 Block、`blockDomains`、`blockDomainsExcept` 和 SPOF，用于模拟屏蔽域名、超时或加载失败。
- ⏱️ 使用 `PerformanceObserver` 观察 `longtask`，其 attribution 信息可帮助定位昂贵 iframe 引发的长任务。
- ⚡ 非关键脚本应使用 `async` 或 `defer` 避免阻塞 DOM 解析；`async` 下载后尽快执行，`defer` 等解析完成再执行。
- 🔗 使用 `dns-prefetch` 和 `preconnect` 提前进行 DNS、TCP 和 TLS 连接，减少第三方域名连接建立时间。
- 📦 关键脚本可考虑自托管以控制 DNS 和缓存，但需自行维护更新与安全修复；也可用 Service Worker 缓存或节流非关键请求。
- 🧩 用 iframe 沙箱隔离第三方脚本，结合 Permissions Policy 限制浏览器特性；注意 iframe 仍可能阻塞 `onload`。
- 🖼️ 对广告、视频等非首屏资源懒加载，优先使用 IntersectionObserver，避免低效的 scroll/resize 加 `getBoundingClientRect()`。
- 🧪 A/B 测试尽量服务端决定版本或只向小样本用户下发脚本，避免延迟所有用户的页面渲染。
- 🛡️ 避免 `document.write()`；谨慎使用标签管理器，限制访问权限并减少标签和自动事件监听。
- 🔐 通过 HTTPS、sandbox、CSP、SRI、自测和定期审计降低安全风险、全局污染及第三方代码异常行为。

---

### [简介](https://partytown.qwik.dev/)

**原文标题**: [Introduction](https://partytown.qwik.dev/)

Partytown 是由 QwikDev 维护的懒加载库，旨在将分析、广告、追踪器等资源密集型第三方脚本迁移到 Web Worker 中运行，从而释放主线程资源、提升网站性能；但它并不保证适用于所有场景，使用前需参考 FAQ 与权衡说明。

- 🚀 **核心目标**：让主线程专注于核心应用代码，把非关键路径脚本移到 Web Worker。
- 🧩 **主要能力**：支持沙箱化第三方脚本、隔离长任务、批量处理 DOM 读写以减少布局抖动，并节流其对主线程 API 的访问。
- ⚙️ **兼容方式**：尽量让第三方脚本按原始编写方式运行，并支持在 Worker 中同步读写主线程 DOM。
- ⚠️ **常见问题**：第三方脚本可能带来过多网络请求、阻塞 DOM 构建、CPU 解析执行负担、单点故障、缓存不足、旧 API 和重复加载框架等问题。
- 🎯 **适用场景**：更适合不在关键渲染路径中的脚本，如 Google Tag Manager、Google Analytics、Facebook Pixel、Mixpanel、HubSpot、Segment、Amplitude 等。
- 🧪 **集成生态**：文档列出 Angular、Astro、Gatsby、Next.js、Nuxt、React、Remix、SvelteKit、WordPress、Shopify 等多种集成方式。
- 🔧 **配置内容**：涵盖请求代理、事件转发、沙箱、调试、第三方服务与常见服务配置。
- 👥 **社区支持**：可通过 Discord 和 @QwikDev 参与社区交流。
- 📚 **延伸阅读**：官方提供多篇文章介绍 Partytown 的同步通信机制、性能优化实践及 Beta 进展。

---

### [请求映射生成器](https://requestmap.webperf.tools/)

**原文标题**: [Request Map Generator](https://requestmap.webperf.tools/)

overview summary  
Request Map Generator 可提交目标 URL，生成页面所有请求的节点图，帮助快速识别第三方资源、字节传输来源及域名速度表现；页面还提供博客说明、示例、多地点浏览器测试选项和各地待处理测试数量。

- 🧭 核心功能：输入 URL 后生成页面请求节点图，直观展示请求关系。
- 🔍 分析价值：快速识别站点中的第三方、传输字节来源以及缓慢域名。
- 🖥️ 测试配置：可选择测试地点，并支持 Chrome、Chrome Beta、Chrome Canary。
- 🌍 覆盖范围：测试节点遍布北美、南美、欧洲、非洲、中东、亚洲和大洋洲。
- ⏳ 队列情况：不同地点待处理测试数不同，如 Dulles 72、Frankfurt 69、London 44、Los Angeles 34、Paris 33，Bangkok 仅 1。
- 🚀 使用流程：填写 Target URL、选择 Test Location，然后点击 Submit Test。
- ℹ️ 其他信息：提供 Read more on my blog 和 see an example 链接，页面由 Simon 构建。

---

### [数据 | 第三方 Web](https://www.thirdpartyweb.today/)

**原文标题**: [Data | Third-Party Web](https://www.thirdpartyweb.today/)

该内容说明了一个可视化图表，用于展示实体脚本的平均执行时长，并涉及“平均成本”“总影响”和“流行度”等指标；其中规模最大的实体对所在页面的性能影响最差。

- ⏱️ 该图表用于可视化实体脚本的平均执行时长。
- 📊 关键指标包括“平均成本”“总影响”和“流行度”。
- 🚨 图表中规模最大的实体通常对所在页面的性能造成最严重的影响。

---

### [我们如何保护我们的分析脚本 - Fathom Analytics](https://usefathom.com/blog/how-we-secure-our-analytics-script)

**原文标题**: [How we secure our analytics script - Fathom Analytics](https://usefathom.com/blog/how-we-secure-our-analytics-script)

2026 年 10 月 29 日，Polymarket 因第三方监控脚本被篡改，约 260 万美元从 700 个用户账户中被盗；攻击者专门替换了 DebugBear 为 Polymarket 定制的 JavaScript 文件。Fathom 随后说明其分析脚本的多层防护措施，包括限制生产权限、锁定域名与 CDN、使用只读静态文件、统一脚本以及全天候监控。

- 🎯 攻击事件：Polymarket 使用的第三方脚本被替换为恶意版本，造成约 260 万美元损失，影响 700 个账户。
- 🧩 攻击特点：DebugBear 为 Polymarket 单独提供定制脚本，攻击者只篡改该文件，使攻击更具针对性且更隐蔽。
- 🔐 生产权限：Fathom 仅允许创始人一人向生产环境推送代码，其他人只能通过 Pull Request 贡献。
- 🌐 域名与 DNS：域名和 DNS 放在专用 AWS 账户的 Route 53 中，仅一人可访问，并启用转移锁。
- 📡 CDN 防护：CDN 仅一个账户可访问，使用随机密码和 2FA，定期轮换 API Key，且只从自有服务器拉取 script.js。
- 🗂️ 静态只读文件：script.js 打包进部署包，运行时文件系统只读，生产环境无法修改，只有创始人可授权部署。
- 🧬 统一脚本：所有客户使用完全相同的 script.js，不做客户定制；若被篡改会影响所有站点并被快速发现。
- 🚫 不执行额外代码：脚本不会下载或运行其他代码，数据接收端点只能接收数据，不能下发指令。
- 👁️ 持续监控：外部服务每 5 分钟从全球多个位置检查脚本内容，任一字符变化即触发告警、重新部署、轮换凭据并通知客户。
- 🔭 后续计划：Fathom 将继续评估自托管脚本、Subresource Integrity 等方案，以进一步增强安全性。

---

### [侧边距修剪 — 面向网页的光学文本对齐](https://sidebearing-trim.js.org/)

**原文标题**: [sidebearing-trim — Optical text alignment for the web](https://sidebearing-trim.js.org/)

未提供可总结的正文内容，因此暂时无法提取文章要点。
- 📄 请在“Use the following content”后粘贴需要总结的文章内容。
- 🧾 收到内容后，我会按“概述 + 要点列表”的格式进行总结。
- ✅ 每条要点将使用“-”符号，并配上合适的表情符号。

---

### [错误](https://sidebearing-trim.js.org/preface)

**原文标题**: [Error](https://sidebearing-trim.js.org/preface)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='sidebearing-trim.js.org', port=443): Max retries exceeded with url: /preface (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [GitHub - peksi/sidebearing-trim：按可见墨迹而非字形框原点对齐文本。读取 OpenType 度量，测量每行首个墨迹的落点，并将元素向左精确移动相应距离。](https://github.com/peksi/sidebearing-trim)

**原文标题**: [GitHub - peksi/sidebearing-trim: Align text by visible ink, not by glyph box origin. Reads OpenType metrics to measure where the first ink lands on each line and shifts the element left by exactly that amount. · GitHub](https://github.com/peksi/sidebearing-trim)

sidebearing-trim 是一个前端文本对齐工具，依据 OpenType 度量读取每行首个可见墨迹的位置，并将元素左移相应距离，使文本按可见字形而非字形框原点对齐；仓库提供原生 JS 与 React 用法。

- 🎯 核心目标：按可见墨迹对齐文本，读取 OpenType 度量并测量每行首个墨迹落点。
- 📦 安装方式：使用 `npm install sidebearing-trim`。
- 🧩 原生 JS API：`trimSidebearings(targets, fontSource, options?)` 返回 `SidebearingController`。
- ⚙️ 控制器方法：`recompute()` 重新测量并应用，`destroy()` 清理注入元素和监听器，`getState()` 返回统计状态。
- 🛠️ 主要选项：支持 `trimEnabled`、`observeResize`、`applyOverlayVariable`、`overlayVariable`、`spanClassName`。
- ⚛️ React 组件：`<Sidebearing>` 支持 `as`、`fontSource`、`trim`、`overlay`、`glyphClassName`、`observeResize` 等属性，并会在内容或字体变化时自动重跑。
- 🧪 开发方式：仓库使用 pnpm workspace，提供 `pnpm build`、`pnpm test`、`pnpm dev:docs` 等命令。
- ⚠️ 已知限制：仅支持 `.woff` 字体；WOFF2 会因 Brotli 解压显著增加包体积；需已挂载且可见的 DOM 节点；CSS 字体与 `fontSource` 必须指向同一文件；暂不支持 RTL。

---

### [错误](https://colorsym.com/)

**原文标题**: [Error](https://colorsym.com/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='colorsym.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Astro 的字体搭配 - Astrotypes](https://astrotypes.com/)

**原文标题**: [Font pairings for Astro - Astrotypes](https://astrotypes.com/)

overview summary
该页面是面向 Astro 的字体排版资源站，汇集精选字体配对与字体库，支持通过 Astro Fonts API 用一条 CLI 命令安装，并兼容 Tailwind 或纯 CSS。

- 🎯 收录 209 组字体配对、2026 个字体家族，整合 3 家字体提供商。
- 🔤 提供商包括 Google Fonts、Bunny CDN、Fontshare，可按提供商筛选。
- 🗂️ 可按 Serif、Sans Serif、Mono、Display、Handwriting 等类别浏览字体。
- ⚡ 每组配对展示标题字体、正文字体、提供商及 Type tester 预览。
- 💻 配对可用类似 `npx astrotype add plus-jakarta-sans+inter --cdn google` 的命令安装。
- 🧱 字体库支持单独安装字体，命令形式如 `npx astrotype add:font inter --cdn google`。
- 🎨 示例涵盖 Plus Jakarta Sans + Inter、Playfair Display + DM Sans、IBM Plex Sans + Inter、Geist、EB Garamond + Inter、Lora + Nunito Sans 等。
- 🧩 页面还包含大量 Google Fonts 与 Fontshare 字体，并提供“Load more”继续加载。

---

### [GitHub - flyfish-dev/file-viewer：在浏览器中预览 275+ 种文件格式：Office、PDF、OFD、CAD](https://github.com/flyfish-dev/file-viewer)

**原文标题**: [GitHub - flyfish-dev/file-viewer: Preview 275+ file formats in the browser: Office, PDF, OFD, CAD, 3D, archives. Pure frontend, no server conversion. Vue / React / Svelte / Web Components. · GitHub](https://github.com/flyfish-dev/file-viewer)

File Viewer 是 flyfish-dev 开源的浏览器端只读文件预览项目，支持 Office、PDF/OFD、CAD、3D、压缩包、邮件等 275+ 扩展名，采用纯前端解析渲染，无需转换服务器，并提供 Web Component、Vue、React、Svelte、jQuery 等多框架接入及离线自托管能力。

- 📦 仓库约 2.7k Star、286 Fork，核心自有源码采用 Apache-2.0，定位为多格式浏览器预览组件。
- 🧩 覆盖 275 个注册扩展名（225 稳定、50 实验）和 47 条预览管线，含 Word、Excel、PPT、PDF、OFD、DWG/DXF、STEP/IFC、压缩包、邮件、图像、媒体、代码、DICOM 等。
- 🚫 文件在浏览器中解析渲染，无需转换服务器；Workers、WASM 和字体可自托管，支持离线网络。
- ⚡ 重型引擎按格式懒加载，只加载文件所需资源，降低初始负担。
- 🧑‍💻 一套 API 覆盖 Web Component、Vue 3、Vue 2.7/2.6、React 16.8–19、Svelte 和 jQuery。
- 🚀 快速开始可安装 `@file-viewer/web-full` 并调用 `mountViewer`，或用 `npm create file-viewer@latest` 创建示例、CLI 接入现有项目。
- 🧱 可按需选择轻量组件、`preset-office`、`preset-lite`、`preset-engineering` 或独立渲染器；`*-full` 包保留 v2.4 兼容基线（221 扩展名/32 管线）。
- 📱 提供 Flutter SDK 开发预览 0.1.0-dev.2，目标平台包括 Android、iOS、Web、Windows、macOS 和 Linux。
- ⚠️ 它是查看器而非编辑器；字体、厂商特性、加密文件和超大输入可能影响保真度或内存，生产使用前应查格式矩阵并用真实文件测试。
- 🛠️ Full 包需随应用提供版本匹配的 Workers、WASM、字体等运行时资源，默认路径为 `<deployment-base>/file-viewer/`；Vite 可用插件复制资源，其他构建可用 `file-viewer-copy-assets`。
- 🤝 格式问题反馈需附脱敏样本或复现链接、浏览器版本和预期结果；贡献前阅读 `CONTRIBUTING.md`，安全问题按 `SECURITY.md` 报告。
- ⚖️ DWG/DWF/DWFX 运行时 `@flyfish-dev/cad-viewer` 和 `dwf-viewer` 采用 AGPL-3.0-only，使用或分发 CAD 支持需遵守该许可。

---

### [文件查看器演示 — 在浏览器中查看 Office、PDF 和 CAD](https://demo.file-viewer.app/?lang=en-US)

**原文标题**: [File Viewer Demo — Office, PDF & CAD in Your Browser](https://demo.file-viewer.app/?lang=en-US)

这是“文件查看器演示”，当前正在准备文件预览环境。

- 🗂️ 内容为文件查看器演示。
- ⏳ 正在准备文件预览环境。
- 🖥️ 当前可能处于加载或初始化状态。

---

### [Expo：用于构建应用软件的智能体移动基础设施](https://expo.dev/)

**原文标题**: [Expo: Agentic Mobile Infrastructure for building application software](https://expo.dev/)

Expo 定位为面向 AI/Agent 时代的移动应用基础设施，提供从开发、测试、部署、更新到监控的完整工具链，帮助团队用单一代码库构建并发布 Android、iOS 和 Web 应用，同时以庞大开发者社区和成熟 SDK 支撑生产级应用。

- 🚀 核心主张：Agentic mobile infrastructure，结合 CLI、Skills、MCP，让开发者和编码 Agent 更高效地构建移动应用。
- 🧱 工作流覆盖：Develop、Test、Deploy、Monitor，形成从开发到生产观测的闭环。
- 📱 开发与测试：支持 Expo Go、云端 Simulators 和设备基础设施，Agent 可运行应用、验证结果并附截图、录屏和日志。
- 📦 发布与更新：Build 发布原生版本至 TestFlight/应用商店，Hosting 覆盖 Web，Update 提供 OTA 更新、渠道与灰度控制。
- 👁️ 监控与修复：Observe 提供崩溃信息、性能指标和 Update 采用率，并可推送修复。
- 🤖 AI 与 SDK：Expo SDK 积淀 10+ 年，提供 100+ 生产 API，支持 MCP 和 Claude Code connector，兼容 React Native、Swift、Jetpack Compose、Kotlin 等。
- ☁️ 自动化与 Agent 支持：Workflows 自动化构建、测试和发布；云模拟器可由编码 Agent 按需驱动，无需 Mac。
- 📊 规模与社区：3M+ 开发者、50K+ GitHub stars、7M+ 周下载、100K+ 活跃开发者、500K+ 项目、100K+ 日构建，80% React Native 开发者选择 Expo。
- 💬 用户口碑：开发者普遍认可 Expo 简化 React Native 开发、跨平台能力、低门槛设备调试、OTA 更新和生态文档。
- 🔐 信任与合规：获 Meta 推荐，React Foundation 成员，符合 SOC 2 Type II、GDPR、CCPA，并支持 SSO。

---

### [TWD - 开发时测试 | 浏览器内前端测试 | TWD](https://twd.dev/?utm_source=frontendfocus&utm_medium=newsletter&utm_campaign=cooperpress-q4-2026)

**原文标题**: [TWD - Test While Developing | In-browser frontend testing | TWD](https://twd.dev/?utm_source=frontendfocus&utm_medium=newsletter&utm_campaign=cooperpress-q4-2026)

TWD 是一款开源前端测试工具，让你在正在开发的浏览器和 dev server 内直接对真实应用运行组件与流程测试；AI 代理可编写、无头运行、读取失败并修复测试，mock 也会在合并前对真实 API 校验。

- 🧪 通过 dev server 侧边栏，对真实应用运行组件测试与流程测试，并在合并前用真实 API 校验 mock。
- ⚙️ 上手只需安装 `npm install twd-js` 和一个插件，无需额外保持第二个浏览器打开。
- 🤖 支持 Claude Code 插件及通用 Agent Skills；AI 可自动检测技术栈、安装 `twd-js`/`twd-cli`、配置 Vite 插件、生成测试并循环修复至通过。
- 🧩 支持 React、Vue、Angular、Solid、Astro、Nuxt、HTMX 和 vanilla JS，适配 Vite、Webpack 与 CDN。
- 🚀 `twd-cli` 可无头运行测试并返回结构化文本，而非截图或 DOM 快照，显著降低 token 消耗；`twd-relay` 可让代理运行过程在自己的标签页中可见。
- 🎥 GitHub Action 的 `record` 标签可为 PR 新增或修改的每个测试生成视频 artifact，由 CI 录制，确定性强且不额外消耗模型 token。
- 🆚 与 Playwright/Cypress 互补：TWD 用 mocked boundaries 提供快速、确定性的 UI 逻辑反馈，端到端测试负责完整系统集成验证。
- 🧱 不同于 Vitest Browser Mode：TWD 运行在真实 dev server 中，可走真实路由测试整个应用，也可用 Testing Library `render()` 挂载单组件，并共享覆盖率报告。
- 📚 不替代 Testing Library（底层使用它），也不必丢弃 jsdom 中的纯函数、reducer、formatter 和 hooks 测试；更值得迁移的是为渲染而 mock 自身 `src/` 的组件测试。
- 🔒 TWD 代码由 `import.meta.env.DEV` 守卫，不会进入生产包；项目 MIT 许可，个人和企业均可免费使用。
- ⚠️ 不面向服务器主导渲染的场景，例如 Next.js App Router 中的 React Server Components。

---

### [推出 Geist Serif - Vercel](https://vercel.com/blog/introducing-geist-serif)

**原文标题**: [Introducing Geist Serif - Vercel](https://vercel.com/blog/introducing-geist-serif)

Geist Serif 是 Geist 字体家族的最新成员：一款基于 Geist Sans、Geist Mono、Geist Pixel 共同基础打造的高对比度展示衬线字体，面向标题、海报与现代高密度屏幕，在延续同一系统的同时加入编辑设计与时尚杂志气质。

- 🆕 **家族新成员**：Geist 从开发者使用的等宽字体起步，发展为 Geist Sans、Geist Pixel，如今新增 Geist Serif。
- ✨ **展示型衬线**：Geist Serif 具有细密锯齿状衬线、锐利发丝线和强对比，适合在现实世界与高密度屏幕上传达强烈信息。
- 🎨 **编辑设计灵感**：不同于不少科技品牌借用复古电脑广告风格，Geist Serif 更偏向时尚、编辑设计和杂志标题，致敬《Rolling Stone》与《Harper's Bazaar》背后的艺术家。
- 🖋️ **同一系统，新声音**：Geist Sans 负责产品界面，Geist Serif 为标题提供第二声音；其字干与 Geist Sans 匹配，并共享宽度与姿态。
- 📐 **度量兼容**：Geist Serif 与 Geist Sans 使用相同的大写高度和 x 高度，可混排 Sans、Mono、Pixel、Serif 而不改变行高与视觉大小。
- 🎛️ **四种变体，一个轴**：通过 Element Shape（ELSH）可变轴切换圆点、方形、三角形、心形四种点状造型，每種也有独立静态文件。
- 🔤 **规格一览**：首版包含 1 个字重（Regular）、4 种变体、894 个字形、5 个样式集（ss01–ss05），支持 352 种拉丁文字语言，并处理了超过 52,000 个字距配对。
- 📦 **开箱即用**：Geist Serif 与家族其他字体同包发布，可通过 `npm i geist` 安装；提供 `GeistSerif`、`GeistSerifRegular`、`GeistSerifSquare`、`GeistSerifTriangle`、`GeistSerifHeart` 等导出与 CSS 变量。
- 🚀 **未来路线**：Regular 只是首款样式，后续将扩展 Thin 到 Black 的可变字重，并探索文本字体、规则化生成的斜体、西里尔文支持及登陆 Google Fonts。
- 🤝 **团队协作**：Geist Serif 从 Evil Rabbit 的草图开始，由 Andrés Briganti 扩展，Mark Davis 以精细工艺完成字形、可变轴与字距等细节，并由多位贡献者共同完成海报、动效、打包与页面等工作。

---

### [Geist - Google 字体](https://fonts.google.com/specimen/Geist)

**原文标题**: [Geist - Google Fonts](https://fonts.google.com/specimen/Geist)

未提供可总结的文章正文，因此无法准确提炼内容；请粘贴原文后再生成概览与要点。

- 📄 当前消息只有总结要求，没有文章内容。
- ✍️ 请补充完整文本，以便进行准确概括。
- 🧭 收到内容后，将按“概览总结 + 带表情符号的要点”格式输出。

---

### [Geist Mono - Google 字体](https://fonts.google.com/specimen/Geist+Mono)

**原文标题**: [Geist Mono - Google Fonts](https://fonts.google.com/specimen/Geist+Mono)

您尚未提供需要总结的文章正文，因此暂时无法提取关键信息或生成内容摘要。

- 📄 请补充文章全文或主要段落，以便进行准确总结。
- 🧭 收到内容后，我将提炼核心观点与关键信息。
- ✂️ 输出会保持简洁，并使用“-”符号和合适的 emoji 进行格式化。

---

### [Geist Pixel - Google 字体](https://fonts.google.com/specimen/Geist+Pixel)

**原文标题**: [Geist Pixel - Google Fonts](https://fonts.google.com/specimen/Geist+Pixel)

未收到需要总结的文章内容，因此暂时无法生成具体摘要。

- 📄 请提供完整文本或明确需要总结的内容。
- 🧾 收到内容后，我会提炼关键信息并生成简洁要点。
- ✅ 输出将使用中文，并以“-”符号和合适表情符号呈现。
- 🔍 也可按主题、结论或行动项进行分类总结。

---

