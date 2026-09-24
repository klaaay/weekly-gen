### [WebKit 为 Safari 27.0 带来的功能 | WebKit](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/)

**原文标题**: [  WebKit Features for Safari 27.0 | WebKit](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/)

Safari 27.0 带来 83 项新功能与 844 项修复，重点提升既有功能质量，并加入 Safari MCP、可定制 Select、滚动锚定、HTML `<model>`、空间 Web 等；同时大量更新 CSS、JavaScript、SVG、WebAssembly、Web API、Web Inspector、媒体、WebGPU、WebRTC、WebDriver、Web 扩展与 WKWebView。

- 🚀 Safari 27.0 功能数量从首个测试版 58 项增至 83 项，修复达 844 项。
- 🧪 质量工程：修复兼容性、基础架构、深度技术、标准对齐和功能集成问题，如 ES 模块加载器、CSS Zoom、SVG 66 项修复。
- 🧑‍💻 Safari MCP：本地 MCP 服务器让 Claude Code、Codex 等代理查看 DOM、网络、截图、控制台，验证状态、样式、可访问性、性能。
- 🎛️ 可定制 Select：`appearance: base-select` 启用新 UA 默认样式，支持 `::picker-icon`、`::checkmark`、`<selectedcontent>` 和丰富自定义。
- 🧊 HTML `<model>`：3D 模型元素登陆 iOS/iPadOS/macOS，支持多源、环境贴图、`stagemode`、JS 交互与 HDR `dynamic-range-limit`。
- 🖼️ 响应式图片/Web Components：`sizes="auto"` 自动计算懒加载图片尺寸；声明式 shadow root 支持 `shadowrootslotassignment`。
- 🌌 空间 Web：visionOS 网站可用 Immersive API 提供沉浸环境；`<img controls>` 支持空间/全景照片；WebXR 支持 texture array projection layers。
- 📌 滚动锚定：自动调整滚动位置，避免上方注入内容导致页面跳动，可用 `overflow-anchor` 控制。
- 🎨 CSS 新能力：`stretch` 尺寸关键字；锚定位支持 transform、`anchor-valid/visible`；`alpha()`、多色 `color-mix()`、`image(<color>)`、`light-dark()` 图像、`:heading`、`revert-rule`、`progress(no-clamp)`、`s` 属性选择器、`:host:has()` 等。
- ✨ 动画与 SVG：`AnimationEvent`/`TransitionEvent` 暴露 `animation`；SVG 支持 `lang/xml:lang`、`<use>` 外部引用，移除旧接口并大量修复。
- ⚙️ WebAssembly：新增 JSPI，让 Wasm 同步式代码等待 JS Promise，便于移植 C/C++/Rust 代码。
- 📦 JavaScript：重写标准兼容 ESM 加载器，修复 top-level await、模块执行顺序与初始化问题。
- 🌐 Web API：Service Worker 静态路由；ReadableStream 支持 `for await...of`、`ReadableStream.from()` 和跨上下文传输。
- 🛠️ Web Inspector：颜色选择器内联对比度与格式/色域控件；Network 显示重定向链；Elements 增加 Subgrid/Grid-Lanes 徽章；Timeline 显示布局根与样式事件颜色。
- 🎬 媒体：`TextTrackCue.endTime` 可为 Infinity；macOS genlock 同步视频；HDR gain map 解码改进；WebCodecs VideoDecoder 可覆盖色彩空间。
- 🔐 网络/存储：loopback 主机支持 Secure cookie；Cookie Store API 支持 `maxAge`；HTTP 缓存更符合 `Cache-Control`。
- 🧮 WebGPU/Canvas/渲染：WGSL 支持 `clip_distances`；`roundRect` 的 radii 可选；新增 `srgb-linear` 与 `display-p3-linear` 预定义色彩空间。
- 📐 MathML：更新运算符字典、支持多字符运算符；元素支持 `tabindex`、`focus()`、`blur()`、`autofocus`；`href` 仅保留在 `<a>`。
- 📞 WebRTC：新增 `targetLatency`、`RTCRtpCodec`、`jitterBufferTarget`，统计包含视频宽高。
- ✍️ 编辑/自动化/扩展：中文简繁转换菜单；WebDriver 支持 Digital Credentials；Web 扩展支持 `runtime.getDocumentId`、异常上报、用户手势传播、`tabId`。
- 📱 WKWebView：新增 `WKJSHandle`、`WKContentWorldConfiguration`、`alternateRequest`、`willSubmitForm`、`load(url:)`、DOM 快照、按 URL 取 cookie、GPC 开关等。
- 🧾 已解决问题：覆盖无障碍、CSS、表单、HTML、图片、JavaScript、MathML、媒体、网络、渲染、SVG、滚动、安全、Web API、Web Inspector、WebAssembly、WebGL、WebGPU、WebRTC 等大量修复。
- ⬆️ 更新与反馈：Safari 27.0 随 macOS 27 Golden Gate、iOS 27、iPadOS 27、visionOS 27 推出，也可在 macOS 26 Tahoe 与 macOS 15 Sequoia 单独更新；欢迎通过反馈渠道提交问题。

---

### [Safari 27 发布说明 | Apple 开发者文档](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)

**原文标题**: [Safari 27 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)

该页面需要启用 JavaScript 才能查看内容，并为自动化工具和辅助工具提供了 Markdown 版本的替代访问方式。

- ⚠️ 页面内容依赖 JavaScript，未启用时无法正常显示。
- 🔄 需在浏览器中打开 JavaScript 并刷新页面。
- 🤖 该说明面向自动化工具和辅助工具。
- 📄 提供了页面内容的 Markdown 版本。
- 🔗 可通过“View Markdown”链接查看 Markdown 内容。

---

### [为 Web 开发者推出 Safari](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

**原文标题**: [  Introducing the Safari MCP server for web developers | WebKit](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

Safari 27 与 Safari Technology Preview 247 推出 Safari MCP 服务器，这是一个面向 Web 开发者的 Model Context Protocol 服务器，可将 AI agent 连接到 Safari 浏览器窗口，让它直接查看 DOM、网络请求、截图与控制台输出，从而更自主地调试，减少窗口切换和反复提示。它支持任何 MCP 兼容客户端，本地运行，不自行联网，也不访问 Safari 中的个人数据；捕获内容会发送给你使用的 agent，而非 Apple。

- 🚀 Safari MCP 服务器让 agent 能了解代码在 Safari 中的真实渲染效果，提升 Web 开发与调试效率。
- 🧩 任何兼容 MCP 的客户端都可连接，agent 可访问 DOM、网络请求、截图和 console 输出。
- 🐛 主要用途包括：Safari 网页开发、提升 Safari 兼容性、性能分析、无障碍检查和验证用户状态。
- ⚡ 性能分析方面，agent 可执行 JavaScript，获取导航计时与资源加载时间，定位拖慢网站的原因。
- ♿ 无障碍检查方面，可发现缺失标签、ARIA 属性不当和对比度不足等常见问题。
- ✅ 用户状态验证方面，可检查表单、元素选择器、交互结果以及结账流程的不同状态。
- 🛠️ 工具涵盖控制台消息、浏览器对话框、标签页管理、JavaScript 执行、网络请求详情、页面内容、页面信息、页面交互、截图、模拟媒体、视口大小和等待导航等。
- 🧪 在 Safari 27 中，需要启用 Web 开发者功能与远程自动化/外部代理，然后通过 Claude、Codex 或 `mcp.json` 配置连接。
- 💻 Claude 可运行：`claude mcp add safari-mcp -- "/usr/bin/safaridriver" --mcp`；Codex 可运行：`codex mcp add safari-mcp -- "/usr/bin/safaridriver" --mcp`。
- 🧭 Safari Technology Preview 247 也支持，需启用开发者功能与远程自动化，并使用对应 STP 的 `safaridriver` 路径配置。
- 💬 安装后可用简单提示启动，例如“Find bugs on my site in Safari”“How accessible is my site in Safari?”。
- 🔐 该服务器完全在本地运行，不进行自身网络调用，也不访问 AutoFill 等 Safari 个人数据；数据去向取决于你使用的 agent 与模型。
- 🎯 目标是让 AI 辅助的 Safari 测试与调试更简单，使开发者少做手动检查，更快修复问题并改善用户体验。

---

### [滚动锚定概述 - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring/Overview)

**原文标题**: [Overview of scroll anchoring - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring/Overview)

滚动锚定是浏览器默认启用的一项功能，用于解决长页面在慢速连接下因上方内容加载而导致阅读位置突然跳动的问题。它通过调整滚动位置来保持用户正在查看的内容稳定，自 2026 年 9 月起在最新设备和浏览器版本中可用，并可通过 CSS overflow-anchor 属性进行调试或禁用。

- 🌐 滚动锚定解决长页面中因上方内容（如图片）加载导致用户阅读位置突然跳动的体验问题。
- 📅 基线 2026：自 2026 年 9 月起，该功能在最新设备和浏览器版本中可用，旧设备或浏览器可能不支持。
- 🔄 工作原理：调整滚动位置以补偿视口外的布局变化，使用户正在查看的文档位置保持在视口中。
- ✅ 默认启用：支持该功能的浏览器中无需手动开启，自动生效，通常能减少内容跳动。
- 🐞 调试方法：若页面异常，可能是 scroll 事件监听器未处理额外滚动；Firefox 可在 about:config 中禁用 layout.css.scroll-anchoring.enabled，或用 layout.css.scroll-anchoring.highlight 显示紫色锚节点覆盖层。
- 🚫 禁用方式：通过 CSS overflow-anchor 属性，值为 auto（默认）或 none；在 body 或容器元素上设置 overflow-anchor: none 可退出；已退出区域的后代无法重新启用。
- ⚠️ 抑制触发器：锚节点或其祖先的 top/left/right/bottom、margin/padding、宽高相关属性、transform/translate/scale/rotate 的计算值变化，以及滚动容器内 position 变化都会禁用锚定。
- 📜 规范：CSS Scroll Anchoring Module Level 1 # exclusion-api。
- 🧪 兼容性测试：可使用 @supports 特性查询来检测 overflow-anchor 属性的支持情况。
- 🔗 另见：WICG 2016 年原始说明、Chromium 2017 年开发者文档等。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Data 的 Tiger Cloud 是面向任意规模时序工作负载的 PostgreSQL 服务，覆盖大规模指标、数据存储与数据点处理，并提供企业级高可用、合规、可观测性和快速部署能力。

- 📈 专为任意规模时序工作负载打造，单 Tiger Cloud 服务可达每日 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 🎁 新账户注册可获 1000 美元信用额度，30 天有效，无需信用卡，仅限新用户。
- 🏭 受数千家 IoT 公司信赖。
- ⚙️ 核心能力包括：读写分离，副本集最多 10 节点，SSD/S3 分层存储，实现高效弹性扩展。
- 💰 计算与存储分离，可独立扩展，避免为空闲容量付费，并优化成本与性能。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级合规：支持 SOC 2、HIPAA、GDPR，提供始终加密、SSO、RBAC 和审计日志。
- 📊 深度可观测性：查询下钻与仪表盘，指标可发送至 CloudWatch、Datadog、Prometheus。
- 🚀 快速启动：数分钟内部署数据库，可通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 集成能力：支持首选云提供商及更广泛的 Postgres 生态。
- 🏢 企业就绪：合同化 SLA、区域数据隔离、合规认证，以及 24/7 全球 Postgres 专家支持和企业响应时限。
- ©️ 页面还包含隐私偏好、法律、隐私、站点地图，以及 2026 年 Timescale, Inc. d/b/a Tiger Data 版权信息。

---

### [](https://flaviocopes.com/modern-css-features/)

**原文标题**: [12 CSS features you can use today with no build step](https://flaviocopes.com/modern-css-features/)

这篇博客文章介绍了 12 个如今可直接在浏览器中使用、无需构建步骤的现代 CSS 特性，它们取代了过去依赖 Sass、PostCSS 插件和各种 JavaScript 变通方案的功能。文章逐一给出了每个特性的代码片段、所替代的旧方案以及截至 2026 年 9 月的浏览器支持情况（依据 MDN 与 web-features），并说明了使用时的注意事项与陷阱。

- 🧩 **原生嵌套**：浏览器直接展开嵌套规则，`&` 表示父选择器，媒体和容器查询也可嵌套，无需 Sass 与监听进程；但 `&__title` 不会拼接类名
- 🎯 **:has()**：终于能向上查找 DOM 树，可按子元素状态为父级或兄弟元素设置样式，取代大量 JavaScript 类名切换；注意其特异性取决于最强参数
- 📐 **容器查询与 cqi 单位**：按组件容器宽度而非视口响应，1cqi 等于容器行内尺寸的 1%，可结合 `clamp()` 缩放字号；尺寸容器不能由内容决定自身尺寸
- 🔲 **Subgrid**：卡片保留自身标记即可借用父网格的行，让标题、段落、按钮跨卡片对齐，无需压平 DOM 或 JS 测量高度；`grid-row: span 3` 不可省略
- 🎨 **oklch() 与 color-mix()**：用感知均匀的色彩空间做变亮变暗与运行时混色，可配合自定义属性，取代 Sass 的颜色函数；注意超出色域的显示效果
- 📺 **aspect-ratio**：一行代码取代 `padding-top` 百分比黑科技，宽高自动推算；它是偏好而非强制，内容过高时盒子仍会撑大
- 🗂️ **级联层 @layer**：把样式优先级顺序写进 CSS 本身，后层规则无视特异性覆盖前层，文件顺序不再重要；未分层的样式会胜过所有层
- 🪄 **:is() 与 :where()**：在浏览器内展开选择器列表，`:where()` 零特异性，适合可被轻易覆盖的基础样式
- 🎬 **滚动驱动动画**：用 `animation-timeline: scroll()` 或 `view()` 让动画由滚动位置驱动，取代 GSAP、AOS 或手写 IntersectionObserver；**唯一非基线特性**，Firefox 仍仅在 Nightly 中实验支持，需用 `@supports` 兜底并尊重减弱动效设置
- 📱 **dvh、svh、lvh**：解决移动端 `100vh` 被工具栏裁切的经典 bug，无需 JS 写入 `--vh`；`dvh` 会随滚动变化，布局推荐默认用 `svh`
- 🌍 **逻辑属性**：用 `inline-start` 等描述书写方向，一套规则自动适配 RTL 语言，取代 PostCSS 生成的双份样式表；切勿与物理属性混用
- ✨ **@starting-style**：为从 `display: none` 出现的元素提供“初始”状态，实现淡入淡出，取代 `requestAnimationFrame` 技巧；只在首次渲染生效，Firefox 的淡出仍会跳变
- 🧪 **支持情况自查法**：打开 MDN 页面看顶部 Baseline 徽章，并用 `@supports` 包裹有风险的部分，让降级版本依然可用
- 📋 **值得一提但未列入正文**：`text-wrap: balance`、`@scope`、`field-sizing`、`@property`、`light-dark()`、`linear()` 缓动等，而 CSS 锚点定位仍属 Limited

---

### [获取失败](https://patrickbrosset.com/articles/2026-09-22-blurry-before-beautiful-image-previews-for-the-web/)

**原文标题**: [Failed to retrieve](https://patrickbrosset.com/articles/2026-09-22-blurry-before-beautiful-image-previews-for-the-web/)

无法总结：获取内容失败，状态码 403。

---

### [](https://developer.chrome.com/blog/new-in-devtools-october-2026)

**原文标题**: [New in DevTools - October 2026  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-devtools-october-2026)

Chrome 153 与 Chrome 154 已进入稳定版，DevTools 在代理、广告追踪、性能、元素、设备模拟、网络、内存与无障碍等方面带来多项更新；Chrome 改为每月两次发布，What's new in DevTools 也改为月度回顾。

- 🤖 DevTools for agents：Chrome DevTools MCP 服务器新增安全控制、性能调优与内存分析；支持 Agent Plugins 1.0、`--no-javascript-evaluation`、按需 source maps、可配置文件系统根与 CLI 路径权限、`query_heapsnapshot`、PWA 自动化，以及 `list_console_messages` 可选堆栈。
- 📢 Application：Ads 子面板集中调试广告相关信息，包括视口广告密度/数量、广告 CPU/网络用量仪表盘、按广告元素细分、主框架广告脚本表和高亮开关；标题还提及 Cookie 标志编辑。
- ⚡ Performance：完整支持软导航分析并进入 Insights；支持通过 CDP 覆盖 CPU 性能层级；火焰图 `Ctrl+F` 可搜索扩展自定义轨道；仅含 CPU profile 样本的线程也可显示。
- 🧩 Elements：可显示已不匹配但之前生效的 inactive styles；`View Source`、`Starting Style`、`Scroll Snap`、`Reveal` 等装饰器支持键盘访问；跨 Shadow DOM 拖拽排序更可靠；CSS 属性切换更流畅。
- 📱 Device Mode：设备预设按形态分组为 Mobile、Foldables、Tablets & Desktops、Smart Displays；新增 iPhone 16、Pixel 9/10、Galaxy Z Fold 6、iPad Pro 13"、Nest Hub Max 等，并淘汰旧设备。
- 🌐 Network：可将请求“Edit and resend as fetch”并自动填入 Console；本地覆盖防止路径遍历并限制非 http(s) 协议；Windows cmd 的 Copy as curl 转义括号与反引号；二进制 Payload 视图切换时保持滚动/光标位置。
- 🧠 Memory：堆快照支持按最小保留大小过滤边、过滤原始值、按保留/自身大小或名称排序；可按保留大小阈值或属性名查询对象；可分析 V8 执行上下文保留内存；损坏快照会给出清晰错误。
- ♿ Accessibility：VoiceOver 播报 DOM 树展开/折叠状态；修复 Issues 重复播报；交互式装饰器可键盘聚焦并激活；新增 `AccessibilityAnnouncementRecordingView` 记录调试实时公告与 `ariaNotify`。
- 🧪 AI 协助：简介提到支持源代码检查与性能跟踪记录。
- 🗓️ 发布说明：Chrome 改为每月两次发布，本系列改为月度功能回顾；可通过 X 上的 @ChromeDevTools 反馈。

---

### [获取失败](https://blogs.windows.com/msedgedev/2026/09/21/new-in-edge-for-developers-create-better-components-and-make-your-site-agent-ready/)

**原文标题**: [Failed to retrieve](https://blogs.windows.com/msedgedev/2026/09/21/new-in-edge-for-developers-create-better-components-and-make-your-site-agent-ready/)

无法总结：获取内容失败，状态码 403。

---

### [](https://github.com/MicrosoftEdge/MSEdgeExplainers/blob/main/OpaqueRange/explainer.md)

**原文标题**: [MSEdgeExplainers/OpaqueRange/explainer.md at main · MicrosoftEdge/MSEdgeExplainers · GitHub](https://github.com/MicrosoftEdge/MSEdgeExplainers/blob/main/OpaqueRange/explainer.md)

overview summary
- 📄 该提案来自 Microsoft Edge 的 MSEdgeExplainers，提出 `OpaqueRange`，用于为 `<textarea>` 和 `<input>` 等封装内容提供“值范围”。
- 🚧 当前 `Range` API 无法直接表示表单控件的 value 范围，导致定位插入符弹窗和用 Custom Highlight API 标记语法错误都需要绕路实现。
- 🧱 现有方案一：克隆表单控件到 `<div>` 并复制样式，难维护、易出现视觉滞后，也可能影响性能。
- ✏️ 现有方案二：改用 `contenteditable`，但表单集成、跨浏览器一致性和无障碍支持更复杂。
- 🎯 目标：让开发者获取表单控件 value 的 range，支持 `getBoundingClientRect()`、`getClientRects()` 和高亮，同时不暴露内部 DOM。
- 🚫 非目标：不修改现有 Range、Highlight 或 Selection API 来直接支持 `<textarea>` / `<input>` 内部范围。
- 🧩 `OpaqueRange` 继承 `AbstractRange`，是 live range，内容变化后自动更新偏移；`startContainer` 和 `endContainer` 返回 `null`。
- 📏 暴露 `startOffset`、`endOffset`（UTF-16，同 `selectionStart` / `selectionEnd`）和 `collapsed`，通过 `createValueRange(start, end)` 创建。
- ✅ 初始支持 `<textarea>` 和 `<input>` 的 `text`、`search`、`tel`、`url`、`password` 类型；关联范围会随编辑自动更新或断开。
- 🛠️ 可用方法包括 `disconnect()`、`getClientRects()`、`getBoundingClientRect()`；不提供会变更或暴露内部结构的 Range 方法。
- 💡 示例显示可直接定位 @ 提及弹窗、emoji picker，或为拼写/语法错误添加高亮，无需克隆控件。
- 🔄 替代方案包括 `getSelectionBoundingClientRect()`、`getRangeFromValue()`、扩展 Range API、`setOpaqueRange()`、`FormControlRange`，最终选择 `OpaqueRange` 以兼顾封装和扩展性。
- 🔮 未来可能引入 `DynamicRange` 作为 `Range` 与 `OpaqueRange` 的父类，并扩展到自定义元素；还可与 CSS Anchor Positioning 互补。
- 🔐 无预期隐私或安全顾虑；兼容接受 `AbstractRange` 的 API（如 Custom Highlight API），但不兼容要求普通 `Range` 的 API。

---

### [](https://developer.chrome.com/blog/chrome-155-beta)

**原文标题**: [Chrome 155 beta  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-155-beta)

Chrome 155 Beta 于 2026 年 9 月 16 日发布，适用于 Android、ChromeOS、Linux、macOS 和 Windows，带来 CSS/UI、JavaScript 与 Web API 多项更新，涵盖计数器样式、角落简写、窗口控制、后量子加密、数字凭证签发、JPEG XL 解码、不可见 iframe 媒体暂停、HTML 流式插入和 WebTransport 头支持等。

- 🚀 Chrome 155 于 2026 年 9 月 16 日进入 Beta，覆盖 Android、ChromeOS、Linux、macOS、Windows；可从 Google.com 下载桌面版，或从 Google Play 下载 Android 版。
- 🎨 CSS `symbols()` 支持内联定义匿名计数器样式，可用字符串符号和计数系统，并用于 `list-style-type`、`list-style`、`counter()`、`counters()`。
- 🧩 新增 CSS `corner` 简写及每角、物理/逻辑边缘子简写，可一次设置 `border-radius` 与 `corner-shape`；`corners` 作为兼容别名保留。
- 🎲 CSS `random()` 默认每次产生新值，可通过 `<random-key>` 控制随机值在属性与元素间的共享方式。
- ✂️ CSS `text-decoration-skip-spaces` 可控制下划线、上划线、删除线是否跳过空白字符。
- 📐 CSS `margin-trim` 可省略块容器或多列容器首尾子元素的外边距；不再适用于 flex 和 grid 容器。
- 🧱 JavaScript 不再缓存模块加载失败，开发者可再次调用 `import()` 重试失败模块，改善不稳定网络下的体验。
- 📄 支持 TC39 的文本模块提案：`import … with { type: "text" }`，可将文本数据作为字符串导入。
- 🪟 Window Management API 增强：在 `window-management` 权限下可 `maximize()`、`minimize()`、`restore()` 窗口，并用 `setResizable()` 阻止调整大小；新增 CSS 媒体特性 `display-state` 和 `resizable`。
- 🔐 WebCrypto 新增 NIST 后量子算法支持：ML-KEM（768、1024）、ML-DSA（44、65、87）、ChaCha20-Poly1305、X-Wing。
- 🆔 Digital Credentials API 支持凭证签发，发证网站可安全地将数字凭证置备到用户移动钱包；Android 使用 CredMan，桌面使用类似展示流程的 CTAP。
- 🖼️ Blink 支持 JPEG XL（`image/jxl`）解码，使用内存安全的纯 Rust 解码器 `jxl-rs`；JPEG XL 支持渐进解码、广色域、HDR、高色深和动画。
- ⏸️ 新增 `media-playback-while-not-visible` 权限策略，可阻止隐藏 iframe 播放可听媒体；iframe 再次可见后限制解除。
- 🌈 `PredefinedColorSpace` 新增 `srgb-linear` 与 `display-p3-linear`，可用于 canvas。
- 🧬 新增 HTML 插入与流式方法：位置方法 `before()`、`after()`、`append()`、`prepend()`、`replaceWith()`，流式方法 `streamAppendHTML()` 等；支持 `{runScripts}` 和 trusted types 的 `createParserOptions`。
- 🌐 WebTransport 支持通过 `WebTransportOptions` 传递自定义 HTTP 请求头，并可通过实例检查服务器响应头，用于 CONNECT 握手和连接后元数据。
- 📜 页面内容采用 CC BY 4.0 许可，代码示例采用 Apache 2.0 许可。

---

### [](https://polypane.app/blog/the-root-scroller-and-how-not-to-lose-it/)

**原文标题**: [The root scroller and how not to lose it | Polypane](https://polypane.app/blog/the-root-scroller-and-how-not-to-lose-it/)

本文来自 Polypane 博客，解释“根滚动容器”（root scroller）是负责整页滚动的视口滚动区域，标准模式下由 `<html>` 代表。若误用覆盖整个视口的嵌套滚动容器接管滚动，页面看似正常，却会失去浏览器自动提供的滚动恢复、键盘滚动、`window.scrollY`、移动端浏览器 UI 收起、下拉刷新、打印与整页截图等能力。文章介绍了成因、检测方法和常见布局的修复方式。

- 📜 滚动容器：元素在 `overflow` 为 `auto`、`scroll` 或 `hidden`，且有固定或受约束尺寸时，会成为可滚动溢出内容的滚动容器。
- 🌳 根滚动容器：当内容高于视口，整个视口成为滚动容器；`document.scrollingElement` 返回标准模式下的 `<html>` 或怪异模式下的 `<body>`。
- 🧬 样式传播：`html`/`body` 的 `background`、`overflow` 等可能传播到视口，影响页面主滚动由谁承担。
- 🎁 根滚动容器独有：浏览器滚动位置恢复、空格/Page Down/方向键滚动、`window.scrollY` 与 `window` 上的 scroll 事件、`window.scrollTo()`/`scrollBy()`。
- 🖨️ 打印与截图：打印和整页截图依赖根滚动容器高度；若由嵌套容器接管，可能只输出一屏并截断内容。
- 📱 移动端差异：地址栏/工具栏收起、iOS 点状态栏回顶、下拉刷新和过度滚动只对根滚动容器有效。
- ⚠️ 常见误退出：`html, body { height:100%; overflow:hidden }` 加 `.page-wrapper { height:100vh; overflow:auto }` 会让 wrapper 接管整页滚动。
- 🔁 overflow 传播陷阱：`html, body { height:100%; overflow-x:hidden }` 时，`html` 的 overflow 传播到视口，`body` 因一轴 `hidden` 另一轴计算为 `auto`，再配合 `height:100%` 后成为滚动容器。
- 🔍 检测方法：滚动页面后执行 `window.scrollY`，若明显已滚动却返回 `0`，说明已退出根滚动容器。
- 👂 找滚动元素：用 `document.addEventListener('scroll', e => console.log(e.target), { capture:true })`；日志为 `#document` 正常，为某元素则说明是嵌套滚动容器。
- 🧰 Polypane 辅助：Elements 面板显示 `scroll` 徽章，Polypane 31 会高亮正在滚动的元素，也可用脚本列出所有垂直滚动容器。
- 🧪 测试建议：用设备模拟触摸、仅用键盘滚动、运行捕获监听；Polypane 的滚动同步和全高截图可暴露特定断点下的问题。
- 🧱 保持根滚动容器：全屏布局用 `min-height:100svh/dvh`，而不是 `height:100vh`，并移除不必要的 `overflow:hidden` 和 wrapper。
- 📌 固定页头/侧栏：用 `position:sticky` 和 `min-height` 实现固定布局，而不是固定高度 grid 加内容区 `overflow:auto`；长侧栏可成为次级滚动容器。
- ✂️ 消除横向滚动：优先修复造成溢出的元素；快速方案可用 `overflow-x:clip` 替代 `hidden`，避免创建滚动容器。
- 🪟 模态锁定：仅在对话框打开时用 `html:has(dialog[open]) { overflow:hidden }`，并配合 `scrollbar-gutter:stable` 防止布局偏移。
- ✅ 合理使用：嵌套滚动容器适合聊天窗、长侧栏等局部场景；主页面滚动应保留给根滚动容器。

---

### [“AI，把网站做好”——zachleat.com](https://www.zachleat.com/web/ai-websites/)

**原文标题**: [“AI, make the website good”—zachleat.com](https://www.zachleat.com/web/ai-websites/)

文章讨论在 AI 与代理工具盛行的软件开发时代，开发者体验的提升与更多软件产出，并不必然带来更好的用户体验；作者强调“关心输出质量”的工艺精神比以往更重要，并以 Speedlify 的 AI 类别表现不佳为例，提醒人们关注真实用户所体验到的软件质量。

- 🤖 大量 LLM 生成内容在讨论软件开发工艺，如今有代理负责规划、写码、审查、编排任务与调度子代理。
- 🛠️ 软件公司常宣称：让开发更轻松，开发者就有更多精力提升软件质量；但作者怀疑这些工作流改进是否真正改善人们体验软件的方式。
- 📈 软件数量确实增加了，但是否变得更好仍不确定。
- 🌐 前端开发者经历过客户端渲染、单页应用等周期，常以改善开发者体验为名，承诺会“涓滴”提升用户体验。
- ⚠️ 近期有不少软件可靠性下降的轶事；GitHub 可能是二阶受害者，监控与状态页业务或许正迎来机会。
- ❤️ 作者主张 craft 就是关心输出质量，独立于生成工具；它比以往更重要，并对访客、消费者、用户等真实的人具有现实价值。
- 📊 Speedlify 的 AI 类别中位 Core Web Vitals 不及格，13 个站点中有 12 个未通过 Lighthouse 性能与 Axe 可访问性检查。
- 👤 作者 Zach Leatherman 是 Font Awesome 的 Web 构建者、Build Awesome（原 Eleventy/11ty）创建者，用 Speedlify 衡量网站性能，曾在多国演讲，并曾任职于 CloudCannon、Netlify、Filament Group 等。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_source=frontendfocus&utm_medium=email&utm_campaign=agentic-development)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_source=frontendfocus&utm_medium=email&utm_campaign=agentic-development)

Expo 是面向移动与 AI 原生应用开发的基础设施平台，提供 CLI、SDK、MCP、云模拟器、EAS 构建/提交/更新/托管与监控等工具，帮助开发者与智能体完成开发、测试、部署和运维。

- 🧰 提供 Expo CLI、Skills、MCP、Expo Go、Snack、Orbit 等开发工具，支持在任意环境构建应用。
- 🤖 定位为“移动 AI 基础设施”，支持代理式工作流：开发、测试、部署、监控。
- 🧪 测试可使用云模拟器和设备基础设施，Workflows 在每次变更时运行测试套件，并内置模板。
- 🚀 部署支持 TestFlight 与应用商店原生发布，Update 提供 OTA 更新、渠道与灰度发布。
- 📊 通过 Observe 查看崩溃、性能指标与 Update 采用情况，并用 Update 快速修复问题。
- 🧩 Expo SDK 已发展 10+ 年，提供 100+ 生产级 API，一次安装即可使用，欢迎所有原生代码。
- 🌐 支持 Expo、React Native、Swift、Jetpack Compose、Kotlin，可用单代码库发布 Android、iOS 和 Web。
- ⚡ Update 可向所有用户即时发送 OTA 更新，快速交付修复与改进。
- 🖥️ 云模拟器可供编码代理按需驱动，运行应用、验证工作并附截图、录屏和日志，无需 Mac。
- 🏪 Launch 简化 App Store 上架流程，无需配置或前置知识。
- 🔍 内置监控与可观测性，帮助了解生产环境中的性能表现。
- 🔄 Workflows 自动化构建、测试和发布，包括应用商店构建、测试与更新发送。
- 📈 数据规模：7M+ 周下载量、100K+ 活跃开发者、500K+ 项目、100K+ 每日构建；3M+ 开发者、50K+ GitHub stars。
- 👥 社区活跃：80% React Native 开发者选择 Expo，Discord 70K+ 成员，并有大量开发者好评。
- ✅ 合规与认可：Meta 推荐、React Foundation 成员、SOC 2 Type II、GDPR、CCPA、SSO 合规。

---

### [](https://noti.st/matuzo/OD53aV/slides)

**原文标题**: [	19½ things you didn’t know about accessibility in HTML and CSS
](https://noti.st/matuzo/OD53aV/slides)

这是一段简短的开场白，发言者先表达感谢，随后介绍自己的姓名。

- 🙏 感谢受邀出席或参与
- 👤 自我介绍为 Manuel Matuzovic

---

### [](https://cydstumpel.nl/css-scroll-triggered-animations-are-here-and-i-completely-missed-them/)

**原文标题**: [CSS scroll-triggered animations are here, and I completely missed them | Blog Cyd Stumpel](https://cydstumpel.nl/css-scroll-triggered-animations-are-here-and-i-completely-missed-them/)

CSS 滚动触发动画已在 Chromium 浏览器中可用（Chrome 145，2026 年 2 月发布），但作者直到 Bramus van Damme 指出后才得知，且该特性尚未在 MDN 上广泛记录。文章介绍了它与常规动画、滚动驱动动画的区别，语法与动画动作、适用范围、浏览器支持、渐进增强策略及注意事项。

- 🧭 滚动触发动画由触发器的激活/非激活状态控制，可执行播放、暂停、反向等动画动作。
- ⏱️ 三类 CSS 动画区别：常规动画按时间触发；滚动驱动动画由滚动位置决定进度；滚动触发动画在进入激活范围后按时间线播放，离开时可被中断。
- 🚀 适用场景：滚动驱动动画适合视差和滚动进度指示；滚动触发动画适合揭示动画和只播放一次的效果。
- ♿ 应使用 `@media (prefers-reduced-motion: no-preference)` 包裹动画，尊重用户的减少动态偏好。
- 🧩 核心语法包括 `timeline-trigger-name`、`timeline-trigger-source`、`timeline-trigger-activation-range`、可选 `active-range`，并用 `animation-trigger` 引用触发器并指定动作。
- 🎛️ animation actions 包括 `play`、`play-forwards`、`play-backwards`、`play-once`、`pause`、`replay`、`reset`、`none`；第一个动作控制进入活动范围，第二个控制离开。
- 🗺️ 激活范围决定触发器何时激活，活动范围决定激活后何时保持活动；默认 active range 继承 activation range。
- 🌐 触发器可设在任意元素上，默认作用域全局，可用 `trigger-scope` 限制；范围由触发元素而非动画元素决定。
- 🧪 支持度很低，目前仅 Chromium；应作为渐进增强，必要时配合 `@supports` 和回退，不要作为关键功能唯一依赖。
- 🧱 可在同一触发器上动画多个内部元素，形成分层动画；加入基于索引的 stagger delay 能提升效果。
- ⚠️ 局限包括：反向播放时单独调整 delay/easing 较难，`container scroll-state queries` 方案有 bug；范围由触发元素决定时可能需添加 dummy elements。
- 📚 进一步阅读可参考 Bramus、CSS-Tricks、MDN 概念版和 Chrome 开发者博客；作者在 Bramus 反馈后于 9 月 17 日编辑澄清。

---

### [](https://developer.chrome.com/blog/responsive-iframes)

**原文标题**: [Responsive iframes in Chrome 154  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/responsive-iframes)

Chrome 154 为 `<iframe>` 引入了“响应式尺寸”支持，允许 iframe 根据嵌入文档的固有尺寸自动调整自身大小。这一特性替代了过去需要手动测量内容、通过 `postMessage()` 传递尺寸并更新 iframe 大小的繁琐模式，非常适合嵌入第三方评论组件、高度多变社交媒体内容等场景。嵌入文档需通过 meta 标签显式选择启用，同时支持跨源限制和渐进增强，帮助开发者更无缝地嵌入外部内容。

- 📐 **核心新特性**：Chrome 154 支持响应式尺寸 iframe，iframe 可根据嵌入文档的内在尺寸自动调整大小，取代以往手动测量与 `postMessage()` 通信的方式。
- 🛠️ **使用方式**：宿主端设置 `frame-sizing: content-height`，嵌入文档需在加载前声明 `<meta name="responsive-embedded-sizing" content="allow-origins=*">`，该 meta 标签不能动态添加。
- 🎛️ **frame-sizing 属性值**：支持 `auto`、`content-width`、`content-height`、`content-inline-size`、`content-block-size`；水平书写模式下 `content-height` 与 `content-block-size` 最适合垂直扩展嵌入。
- 📏 **结合 CSS 约束**：可与 `max-height`、`width: 100%` 等属性搭配使用，实现灵活布局控制。
- 🔄 **动态内容调整**：浏览器不会持续监听内嵌文档布局变化，内容更新后需调用 `window.requestResize()` 请求重新计算尺寸，且建议在布局前调用以避免尺寸循环。
- 🔐 **跨源支持与安全**：可通过 `allow-origins=https://publisher.example` 限制允许的嵌入源，多个源以空格分隔，与 CSP 的 `frame-ancestors` 形成互补。
- 🧩 **渐进增强**：利用 `@supports (frame-sizing: content-height)` 和 `"requestResize" in window` 特性检测，为不支持新特性的浏览器保留旧有回退方案。
- ⚠️ **注意事项**：响应式 iframe 可能因嵌入文档后加载而导致内容偏移，可能影响 Core Web Vitals，尤其在首屏展示时需谨慎。
- 🧪 **试用渠道**：官方提供了 CodePen 演示，可立即体验响应式 iframe 的实际效果。

---

### [](https://piccalil.li/blog/a-decent-custom-checkbox-for-until-checkmark-is-ready/)

**原文标题**: [
  A decent custom checkbox pattern for until ::checkmark is ready - Piccalilli
](https://piccalil.li/blog/a-decent-custom-checkbox-for-until-checkmark-is-ready/)

这篇文章介绍在 CSS `::checkmark` 与 `appearance: base` 尚未被浏览器支持前，如何用语义化 HTML 和 CSS 构建可访问、可缩放的自定义复选框。核心是保留原生 `<input>` 的聚焦能力，同时用视觉容器和 SVG 勾号实现自定义选中状态。

- 🧩 未来可直接使用 `appearance: base` 和 `::checkmark` 定制复选框，但目前浏览器支持尚未到位。
- 🏗️ HTML 从语义化结构开始：`label` 包裹 `input`、视觉框 `span`、`aria-hidden` 的 SVG 勾号与文本标签。
- ♿ SVG 加上 `aria-hidden="true"` 和 `focusable="false"`，避免干扰辅助技术。
- 📐 `.checkbox` 使用 flex、基线对齐、`1em` 间距和 `text-wrap: balance`，改善换行与可读性。
- 🎯 `input` 设置 `appearance: none`、绝对定位、宽高 100%，仍保留可聚焦性与焦点环。
- 📦 `.checkbox__box` 使用 `relative`、`1.4em` 方形、边框和 `translateY(0.75ex)`，让视觉框与文字基线对齐。
- ✅ 勾号 SVG 绝对居中且默认隐藏；选中时用 `:has(input:checked)` 改变背景，用 `input:checked + svg` 显示勾号。
- 🔘 该模式也适用于单选按钮，只需将勾号图标换成圆形图标。
- 📏 除 `transform` 外大量使用 `em`，组件可随 `font-size` 整体缩放；作者也感谢 Jake Archibald 与 Heydon Pickering 审阅。

---

### [](https://www.sanity.io/engineering/we-fixed-wobbly-spinners-in-safari-without-ai)

**原文标题**: [We found a fix for wobbly spinners in Safari (without using AI) | Sanity](https://www.sanity.io/engineering/we-fixed-wobbly-spinners-in-safari-without-ai)

Sanity 工程师 Cody Olsen 分享了一个不用 AI、仅靠 CSS 修复 Safari/WebKit 中旋转加载图标“抖动”问题的经历：根因是 SVG 旋转时的子像素渲染，最终用 CSS `round()` 取整尺寸解决，并引出关于人类协作与跟进平台细节价值的思考。

- 🌀 Sanity 团队很喜欢 spinner，实时 API 应用常需要它提示用户“正在加载”。
- 🐛 Safari/WebKit 中的 CSS 旋转 SVG spinner 会出现抖动，且并非个例，Font Awesome 等也有类似问题报告。
- ⚙️ 常见方案如设置 `will-change: transform` 或交给 GPU 都无效。
- 🔍 根因在于 Safari 渲染 `rotate()` SVG 时的子像素处理：尺寸最好为偶数、能被 2 整除，但产品图标规范常用 `1em`。
- 💡 同事 Ash 提议尝试新的 CSS `round()` 函数，将尺寸设为 `round(1em, 2px)`。
- ✅ 该方案成功解决抖动：设置 `height` 和 `width` 为舍入后的尺寸，并提交了手工 PR。
- 🤖 AI 代理如 Fable 5.1、Astra 6、Muse Spark 1.3 都未能解决这个问题。
- 🧠 结论是：人类协作、保持对 CSS 等“无聊平台细节”的关注，以及 standup 中的闲聊都可能带来突破。
- 🍎 后续 Apple 系统更新后，macOS 27 的 Safari 已修复，但 iOS 27 仍有抖动。
- 🙏 文章致谢 Ash Stevens 提供解决思路，Knut Melvær 推动发布。

---

### [](https://molily.de/web-dev-education/)

**原文标题**: [The death of web development education – Rescuing a field from disappearing](https://molily.de/web-dev-education/)

生成式 AI 正在严重冲击 Web 开发教育，威胁写作者、教师、技术传播者和开源维护者的生计，甚至可能让整个领域消失。多位知名教育者报告收入归零或腰斩、内容被 AI 爬虫和模型吞噬、学习者转向大模型，而“适应 AI”的劝告忽视了劳动被挪用、知识被商品化以及人类教学价值被贬低的问题。文章呼吁承认危机、支持人类教育者，并通过开放技术、独立学习社区和公平报酬重建 Web 开发领域。

- 📉 Baldur Bjarnason 指出，自己横跨写作、出版、咨询、开发、教育等多个领域，但都难以长期维持经济生存；跨学科者还常被社区排斥。
- 🧑‍🏫 他观察到，生成式 AI 导致培训项目逐一消失，同行关闭课程业务，Web 开发电子书需求暴跌。
- 🤖 许多开发者没有完全用智能体写代码，却转向容易出错、非确定性的聊天机器人，把这当作 Web 开发“教育”。
- 📚 Axel Rauschmayer 表示，其书籍收入从 2024 年足以维生，到 2026 年归零；博客和免费书籍流量被 AI 爬虫推高，却几乎没有广告收入。
- 🛑 因此他暂时下架博客和书籍，以应对 AI 公司未经授权使用其作品的问题，但仍继续合理定价销售 JavaScript 和 TypeScript 书籍。
- 😞 Salma Alam-Naylor 因 DevRel 压力和倦怠离开，认为 AI 正在杀死开发者教育：开发者不再聚集学习分享，而是刷短视频、与聊天机器人对话。
- 🧠 她指出，精心设计的课程被预测算法盗用和 regurgitate，聊天机器人的谄媚语气抹除了教育者的人格、努力和技艺。
- 💸 Josh W. Comeau 报告课程创作者收入普遍下降 50% 以上，用户转向 LLM，作品被未经同意、无补偿地吞取和复述，高质量免费内容失去激励。
- 🎥 Kyle Cook（Web Dev Simplified）称编程教程观看量和收入几乎减半，做编程内容不再可持续，而做 AI 模型视频更轻松、更赚钱、流量更高。
- ✍️ Rachel Andrew 认为生成式 AI 破坏了作者与编辑之间的关系，AI 可能引入细微错误，编辑需额外审查，作者省时却给编辑团队增加工作。
- 🧾 她质疑 AI 是否真正提升生产力：很多自动化本可不用 AI 完成，所谓效率可能只是把工作转嫁给编辑或读者，并降低质量。
- 🌐 文章作者强调，生成式 AI 对 Web 开发教育有灾难性影响，威胁下一代 Web 作者和开发者的成长基础；短期没有明显解决方案。
- 🛑 作者反对“适应 AI”“AI 就在这里”等膝跳反应，认为这像在伤口上撒盐，并呼吁同情、承认 AI 公司挪用劳动、摧毁生计。
- 💰 作者主张，至少应迫使 AI 寡头为其造成的危机付费，甚至“剥夺剥夺者”，不能让大科技公司无偿占有 Web 教育者的工作。
- 🧑‍💻 过去志愿者驱动的非商业文档项目曾让 Web 民主化，帮助普通人、社群、学校和小企业建站；如今 AI 鼓吹的“民主化”实则集中权力、商品化知识。
- 🤝 重建 Web 开发领域需要相互支持的人际网络：掌握 Web 技术、挖掘并建立最佳实践、分享洞见，并确保人类学习和教学工作获得报酬。
- 🕳️ Baldur Bjarnason 的结论是：这个领域已经消失，所谓“变化带来的挫败感”其实是对一夜消失领域的怀旧；但作者仍相信 Web 具有韧性，可以靠社区重建。

---

### [](https://github.com/addyosmani/critical)

**原文标题**: [GitHub - addyosmani/critical: Extract & Inline Critical-path CSS in HTML pages · GitHub](https://github.com/addyosmani/critical)

overview summary
- ⚡ Critical 是 Addy Osmani 维护的开源工具，用于提取 HTML 首屏关键路径 CSS、内联到 `<head>`，并异步加载其余样式，从而移除渲染阻塞 CSS、改善 LCP 与首次渲染。
- 📦 通过 `npm install --save-dev critical` 安装；支持 CLI、Node API、Docker，适用于静态站点、MPA 和 SPA，也可用于构建流水线与编码代理。
- 🧠 两种引擎自动路由：`static` 无需浏览器，匹配已交付 DOM，适合 SSG/SSR/MPA；`render` 使用 Playwright 在真实视口测量，适合 SPA shell；默认 `engine: "auto"`。
- 🔧 工作原理：找出关键 CSS → 内联为 `<style data-critical>` 放在 `<head>` 首位 → 将 `<link rel="stylesheet">` 改为 `preload` 并移到 `<body>` 末尾；不添加内联脚本，兼容严格 CSP。
- 🖥️ CLI 示例：`critical ./dist --inline --write` 原地优化；`--explain` 查看决策；`--json` 输出机器可读报告；支持 `--width`、`--height`、`--dimensions` 多视口合并。
- 🧩 API：`critical(options)` 返回 `{ html, css, report }`，默认不写磁盘；`report` 包含引擎、原因、规则数、字节节省、警告、耗时与确定性信息。
- 🎯 调优：静态引擎可用 `[data-critical-fold]` 缩小首屏范围；渲染引擎可用多尺寸视口定义折叠线；保留被引用的 `@font-face`、`@keyframes`、自定义属性，并清理无用规则。
- 🤖 提供 MCP server，暴露 `optimize_critical_css` 工具，方便 AI/编码代理获取关键 CSS、重写后的 HTML 和结构化报告。
- 🐳 Docker 镜像包含 Playwright 与 Chromium，挂载站点到 `/site` 后可直接运行两个引擎。
- ✅ 要求 Node.js ≥ 22.13；渲染引擎需额外安装 `playwright` 与 Chromium，静态引擎不需要；设计原则强调自动路由、少依赖、确定性、可解释和安全默认。
- 📊 项目约 10.3k stars、390 forks，Apache-2.0 许可；创建者为 Addy Osmani，主要维护者 Ben Zörb；替代方案对比见 `COMPARISON.md`。

---

### [](https://github.com/addyosmani/critical/releases/tag/v9.0.0)

**原文标题**: [Release v9.0.0 · addyosmani/critical · GitHub](https://github.com/addyosmani/critical/releases/tag/v9.0.0)

Critical v9.0.0 是一次双引擎重写，目标是继续快速提取首屏关键 CSS、消除阻塞渲染样式表，并适配 2026 年由人类、构建流水线和编码代理共同驱动的 Web 构建方式。

- 🚀 **发布信息**：Critical v9.0.0 由 bezoerb 于 9 月 13 日 07:56 发布，带已验证签名，为最新版本。
- 🎯 **核心目标**：把首屏 CSS 立即送入页面，避免阻塞样式表拖慢首次绘制。
- ⚙️ **双引擎**：新增 `static` 与 `render` 两个引擎，并自动路由。
- 🧱 **static 引擎**：将 CSS 与交付的 DOM 匹配，无需浏览器，毫秒级完成，适合 SSG/SSR/MPA 输出。
- 🖥️ **render 引擎**：在真实视口加载页面并测量首屏实际绘制，适合 SPA shell 和需要视口精确的场景。
- 🤖 **auto 默认**：检查 HTML，有真实内容用 static，空 `div#root` 则升级到 render；会说明用了哪个及原因；Playwright 为可选 peer 依赖，按需懒加载。
- 📏 **确定性**：相同输入生成字节一致输出，便于 CI 与版本控制 diff，首屏只需 HTML。
- 🔒 **CSP 安全**：通过将 stylesheet 替换为 preload 并移出关键路径来延迟加载，不添加内联脚本，兼容严格 CSP。
- 🧠 **面向代理**：提供 MCP server、`--explain` 模式和结构化 report（引擎、字节、规则、警告、耗时）。
- 🧩 **现代核心**：基于 lightningcss、css-tree、linkedom 重建；静态路径和默认安装不拉浏览器；要求 Node.js 22+。
- ⬆️ **升级提示**：v9 是重大版本，API 与选项有变化，需查看 README 获取 CLI/API。
- 🛠️ **主要变更**：包含 v9 重写、CLI/API/MCP 测试、Docker 构建修复、vite-plus 升级等 PR。
- 👥 **贡献者**：addyosmani、fengmk2、bezoerb。

---

### [](https://plotly.com/blog/announcing-plotly-js-4-plotly-py-7/)

**原文标题**: [Announcing plotly.js 4.0 and plotly.py 7.0](https://plotly.com/blog/announcing-plotly-js-4-plotly-py-7/)

overview summary
Plotly.js 4.0 与 plotly.py 7.0 发布，Dash 升级 plotly 后即可使用新版渲染引擎。此次更新带来 quiver 图表、Sankey 增强、完整 CSS Color 4 支持、内置 TypeScript 类型、MathJax v4、地图缩放限制、Plotly Cloud 一键分享等新功能；同时因默认值调整和移除长期弃用功能而升级主版本，Mapbox 系列改为 Map/MapLibre 且无需 token。plotly.py 7.0 同步这些变化，并移除旧地图函数、废弃 figure factories、Orca 与 Kaleido 1.0 以下版本。

- 🚀 Plotly.js 4.0.0 是第 275 次开源发布；plotly.py 7.0 内置该版本，Dash 随 plotly 升级自动获得。
- 🏹 新增 quiver 迹类型：用箭头绘制矢量场，位置为 (x,y)，方向为 (u,v)，可按大小用 colorscale 着色。
- 🔀 Sankey 新增 direction（forward/reversed）与 sort（auto/input），可控制流向和节点排列顺序。
- 🎨 颜色解析改用 culori，支持全部 CSS Color 4 字符串：oklch、oklab、lab、lch、color()、hwb、8/4 位 hex、slash alpha、hsl 等。
- ⚠️ 颜色字符串有破坏性变化：rgb(0.5,0,0) 变为近黑，hsv() 不再解析，rgb(...,0.5) 支持透明度，逗号与空格混用无效。
- 🧩 官方包内置 TypeScript 类型，按 trace 分别定义并支持深度嵌套，可替代 @types/plotly.js。
- 🧮 支持 MathJax v3/v4，LaTeX 字符串无破坏变化；v4 需更换 script URL，v2 不再支持。
- 🗺️ geo 地图支持 minscale/maxscale 限制缩放；map、scattermap、densitymap 可按数据自动计算 center 和 zoom。
- ☁️ modebar 新增一键分享图表到 Plotly Cloud 按钮，默认开启，可用 showSendToCloud:false 关闭。
- 💾 下载图片默认按图表标题命名，例如“Espresso consumption vs. lines of code.png”。
- 🧭 其他新增：hover/click 事件带 xPixel/yPixel；hoveranywhere 离开时触发 plotly_unhover；shape dash 图例显示虚线。
- 🗑️ 移除 Mapbox traces：scattermapbox、choroplethmapbox、densitymapbox 改为 map 版本，底层换为 MapLibre，不再需要 access token。
- 📐 默认值变化：geo.fitbounds 默认“locations”；splom axis.matches 默认 true；双轴 tickmode 默认“sync”。
- 🌍 国家名解析改用 country-iso-search；历史国名和已不存在国家不再解析，Türkiye、Eswatini、中国、旗帜 emoji 等现在可解析；“Republic of Congo”目标变为 COD。
- 📊 hoveranywhere/clickanywhere 返回原始数据值（日期字符串、类别），而非 calcdata 中间值；线性/对数轴不变。
- 🏗️ Node 22 成为构建 plotly.js 的最低版本；移除 Chart Studio 配置、stream trace、*src 属性和 layout.hidesources。
- 🐍 plotly.py 7.0 同步 plotly.js 4.0，Mapbox graph_objects 与 Plotly Express 函数移除，改用 map 版本；废弃 figure factories 被移除。
- 🖼️ plotly.py 7.0 移除 Orca 和 Kaleido <1，write_image 等移除 engine 参数；建议安装 Kaleido 1.0+。
- 🛠️ plotly.py 修复：hex_to_rgb 支持 #FFF；px 地图自动适配数据；to_html 加 doctype；density_heatmap/contour 边际图应用 histfunc/z；mpl_to_plotly 支持更多图。
- 🧪 多项社区修复：histogram react autobin、指数刻度、scroll zoom automargin、空值类别排序、零长度条形文字位置、符号格式、浮点刻度、跨 180° 地图选择/适配、colorbar 负 domain、退化 MultiPolygon、parcats 数值颜色排序等。
- 🙏 22 位社区贡献者参与；可通过 CDN/npm 安装 plotly.js 4，Python 用 pip install -U plotly kaleido，Dash 用 pip install -U dash plotly。
- 📦 plotly.py 7.1.0 随后发布，使用 plotly.js 4.1.1，新增 density_heatmap 热力图边际、mpl_to_plotly 自定义刻度值等。

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=email)

SurveyJS 是一套面向客户端调查与表单管理的 JavaScript 库，可让开发者在自有应用中构建调查和表单，并保留全部数据所有权，避免数月定制开发。它包含 Form Library、Survey Creator、Dashboard、PDF Generator 等组件，支持多框架、自托管、无障碍、离线、AI 辅助，并提供一次性开发者许可与无限使用。

- 📝 核心组件：Form Library 解析 SurveyJS 表单 JSON 并即时渲染动态交互表单，MIT 许可，可收集响应并发送到数据库。
- 🛠️ Survey Creator：白标拖拽式表单构建器，自动生成 JSON schema，可视化创建和编辑调查/表单，并可深度定制。
- 📊 Dashboard：解析 JSON schema，实时可视化调查结果，用交互式图表和表格展示数据，支持表格视图分页与筛选。
- 📄 PDF Generator：根据表单 JSON 渲染 PDF，填充已收集响应，导出可编辑或预填 PDF。
- 🌐 框架兼容：支持 React、Angular、Vue 3 和原生 JS，并可匹配现有设计系统。
- ♿ 无障碍：Form Library v2.1.0+ 与 Survey Creator v2.2.2+ 符合 WCAG、Section 508、ARIA，并经 Axe 验证。
- ♾️ 无限使用：不限表单、响应、管理员、受访者、提交、上传或功能，所有数据存储在自己的数据库中。
- 🧩 自定义输入：支持自定义独立或复合题型，扩展内置组件，并集成 Angular、React、Vue 3 组件。
- 📴 离线收集：可完全离线运行，本地存储调查、主题和响应，联网后自动同步。
- ✅ 自定义验证：内置客户端验证之外，还支持自定义客户端规则和服务端检查。
- 🏷️ 白标与主题：共享设计令牌和可复用主题，支持 Bootstrap、Material UI、shadcn/ui 主题适配器。
- 🤖 AI 辅助：可通过 API 集成 AI，实现自然语言生成表单、翻译或智能内容建议。
- 🏢 行业场景：适用于保险、医疗、市场研究、教育、HR、电商、客户体验、非营利、银行等领域。
- 🛡️ 数据安全与合规：自托管可完全控制数据流，满足 HIPAA、FERPA、GDPR 等隐私与合规要求。
- 💳 许可模式：Survey Creator、PDF Generator、Dashboard 采用一次性开发者许可，含 12 个月免费维护，之后可续订。
- ⚙️ 前后端边界：SurveyJS 只负责前端 UI，不存储、访问或跟踪数据；后端存储、处理和用户管理需自行实现。
- ❓ 常见问题：一次性许可证可永久使用；续订仅延长维护和支持；可分配开发者席位；许可密钥在账户 License Manager 中获取。
- ⭐ 用户评价：普遍称赞其灵活、易用、可定制、支持复杂条件逻辑、开源且客户支持出色。

---

### [](https://rohanadwankar.github.io/posts/semfont.html)

**原文标题**: [A font that reads what you wrote — Rohan Adwankar](https://rohanadwankar.github.io/posts/semfont.html)

semfont 是一个小型自动排版库，通过逐词语义评分和主题映射，自动为文本着色、加粗、斜体和高亮，让长文本和 AI 流式输出更易读。

- 🧩 核心目标：自动改善排版与可读性，尤其适合大段 AI 流式文本。
- 🎨 内置主题：editorial、loud、monochrome、technical，也可只启用特定通道。
- 📊 每个词计算四个分数：valence（好坏）、salience（显著度）、surprise（意外/转折）、certainty（确定性）。
- 🔁 Valence：否定词可翻转并衰减分数，强化词可放大；例如“not great”是轻微抱怨，不是赞美。
- 📈 Salience：结合词频稀有度与文本内重复次数，反复出现的稀有词更值得注意。
- 💥 Surprise：来自 suddenly/ironically 等词、对比词后六词窗口，以及明显更罕见的词。
- 🤔 Certainty：处理 probably/definitely 等语气，并让整句共享句子的确定/模糊程度。
- 🖌️ 主题映射：valence→颜色，salience→字重，surprise→高亮，certainty→斜体；多数词因阈值保持不变。
- 🧠 改进算法：第二遍按从句整体分析，修复跨距离否定、动词影响后续对象、less/fewer 改善、too simple 抱怨、Great 讽刺等盲点。
- 🔍 可解释性：每个词记录改动 notes，例如“resolved by 'fixed'”，便于查询颜色原因。
- ⚖️ 性能：第二遍成本与第一遍相近，保持在预算内，无需开关。
- ⚛️ 使用方式：React 中可用 `<SemanticText>`，支持 theme、channels、自定义 lexicon，并可接入 AI SDK 聊天流。
- 🧮 非 React：可用 analyze 与 styleFor/themes，通过 import map 直接在浏览器运行。
- 🚧 局限与下一步：完美分类且快速不现实，但启发式足够提升可读性；未来可探索讽刺、嵌套否定、技术词汇。
- 🔗 代码与演示：github.com/RohanAdwankar/semfont。

---

### [](https://github.com/RohanAdwankar/semfont)

**原文标题**: [GitHub - RohanAdwankar/semfont · GitHub](https://github.com/RohanAdwankar/semfont)

semfont 是一个根据句子含义实时调制排版的轻量语义字体引擎，用同步、确定性规则和词典驱动，提供 React 组件与纯分析 API，无需模型、网络或异步请求，适合每次击键、SSR 和静态站点。

- 🧠 核心概念：排版是句子的函数，随句子变化重新计算；负面变红、重要变粗、意外高亮、模糊倾斜，而不是依赖手写标记。
- ⚛️ 提供 React 组件 `SemanticText`，放入纯文本即可自动分析并应用样式，无需手工加 `<em>` 或 `<strong>`。
- 🚫 明确不是语法高亮、Bionic Reading、情绪仪表盘、手写强调标签、LLM 或可变字体滑杆；它读取句子本身并就地设置排版。
- ⚡ `analyze()` 是纯同步函数，约 1ms 处理一页文本，无网络、无密钥、无异步，数据不出浏览器，输入相同输出相同。
- 🧩 五个语义通道：`valence` 控制颜色，`salience` 控制字重/字号，`surprise` 控制高亮，`certainty` 控制倾斜/透明度，`technicality` 控制等宽。
- 🎨 前四个通道在所有主题中默认开启；`technicality` 总是评分，但只有 `technical` 主题会映射为 `MONO`。
- 🔍 两条关键规则：否定会翻转并衰减情绪，例如 `not great` 只是轻度负面；稀有度相对于当前段落，而非全局语料。
- 🧮 分析分两遍：第一遍按词和固定邻窗评分；第二遍按从句重算 `valence`，处理否定、伤害解决、`less bad`、`too`、开头讽刺等。
- 📝 每条从句修正会写入 `token.notes`，方便调试面板解释某个词为何呈现该颜色。
- 📦 API 包括 `SemanticText`、`useSemanticText`、`analyze`、`themes`、`styleFor`；纯引擎可从 `semfont/analyze` 和 `semfont/theme` 导入，无需 React。
- ⚙️ `SemanticText` 支持 `text/children`、`theme`、`channels`、`sensitivity`、`lexicon`、`as`、`debug`、`onAnalyze` 等属性。
- 🎛 主题包括 `editorial` 安静、`loud` 放大、`monochrome` 无颜色、`technical` 增加等宽和 `CASL` 倾斜。
- 🛠 可定制性强：可只选通道、编辑主题 `map` 行选择排版轴、添加自定义词典、用 `useSemanticText` 自己渲染，或只用 `analyze` 获取每个 token 的四个分数。
- 🖥 静态站点友好：`src/analyze.js` 和 `src/theme.js` 无依赖，可直接加载；无打包器时用 import map；也可 `renderToStaticMarkup` 预渲染并发布零 JavaScript。
- ⏱ 性能预算：默认引擎低于 1ms/百词，线性扩展；2875 字符页五个通道约 1.43ms，九行主题映射约 0.47ms；更昂贵的规则会作为单独模型显式选择。
- 📚 词汇层：手写软件/事故词典加上 VADER 约 4000 个日常词，手写表优先；`node scripts/vader.mjs` 可重新生成。
- ▶️ 运行方式：`node --test` 跑引擎与主题测试，`npm install react react-dom` 跑 React 渲染测试，`python3 -m http.server` 打开 demo；demo 支持实时编辑、通道切换和悬停分数。
- ⚠️ 局限：不擅长讽刺、反讽和未教过的领域术语；只支持英语；读词不读论证，可能忽略平静句子描述灾难的情况。
- 📄 仓库为 `RohanAdwankar/semfont`，MIT 许可，39 stars、2 forks、33 commits，无额外描述或主题。

---

### [](https://sli.dev/)

**原文标题**: [Slidev](https://sli.dev/)

这是 Slidev 官方文档的导航目录，集中展示从入门、语法、界面、动画到主题组件、导出托管、AI 协作与 FAQ 的指南，并包含进阶开发、功能特性、配置参考、资源画廊及多语言版本入口。

- 🔍 顶部提供搜索入口，方便快速查找文档内容。
- 📖 Guide 覆盖 Why Slidev、Getting Started、Syntax Guide、User Interface、Animations、Theme & Addons、Components、Layouts、Exporting、Hosting、Work with AI、FAQ 等核心内容。
- ⚙️ Advanced 面向进阶开发，包含 Global Context、Writing Layouts、Writing Themes、Writing Addons。
- ✨ Features 单独列出 Slidev 的主要功能特性。
- 📚 Reference 提供 Built-in、CLI、Components、Layouts 及各类配置说明，如 Highlighter、Vite/Plugins、Vue App、UnoCSS、Code Runners、Transformers、Monaco、KaTeX、Mermaid、Routes、Shortcuts、Context Menu、Fonts、Pre-Parser。
- 🎨 Resources 汇集 Showcases、Theme Gallery、Addon Gallery、Learning Resources、Curated Covers、Release Notes。
- 🌐 支持语言切换：English (v53.0.0)、简体中文、日本語。

---

### [HTML 元素周期表](https://blog.alena.rocks/en/artifacts/html-elements/)

**原文标题**: [Periodic Table of HTML Elements](https://blog.alena.rocks/en/artifacts/html-elements/)

该页面来自 blog.alena.rocks，以“HTML 元素周期表”的形式梳理 HTML Living Standard，共收录 115 个元素、11 个规范章节，并可按分类、HTML5 后新增、空元素等条件筛选。

- 🧪 以周期表样式展示 HTML 元素，共 115 个元素，覆盖 11 个规范章节。
- 🆕 标注 7 个在 HTML5 之后新增的元素。
- 🕳️ 标注 13 个空元素（void），并用虚线边框表示：无内容、无闭合标签。
- 🧭 提供“Only new”与“Reset”筛选，可按新增元素等条件查看。
- 🗂️ 元素按类别分组：Root 1、Metadata 6、Sections 16、Grouping 15、Text-level 29、Edits 2、Embedded 13、Tabular 10、Forms 15、Interactive 3、Scripting 5、void 13。
- 📚 页面包含“Text-level semantics · §4.5 continued”，展示文本级语义相关元素。
- 🌳 根元素 html 属于 §4.1：它是文档树的根，恰好包含 head 和 body 两个子元素。
- 🔗 列出大量具体元素，如 html、head、body、title、meta、link、script、section、article、nav、form、input、table、video、canvas、svg、math 等。
- 🧩 math 和 svg 是进入 MathML 与 SVG 的入口，形式上属于其他命名空间。
- 📖 提供 MDN 链接，便于查阅元素定义。
- 🧱 分类还涵盖 root、metadata、sections、grouping、edits、embedded、tabular、forms、interactive、scripting 等结构或功能类别。

---

### [](https://atomicdesign.bradfrost.com/chapter-2/)

**原文标题**: [
		Atomic Design Methodology | Atomic Design by Brad Frost
	](https://atomicdesign.bradfrost.com/chapter-2/)

本章介绍“原子设计”方法论，借用化学与自然界的层级概念，将用户界面拆解为原子、分子、组织、模板和页面五个阶段，并把它们作为同时协作的思维模型，而非线性步骤，用来构建更清晰、可复用、能适应动态内容的界面设计系统。

- ⚛️ 原子设计受化学和自然界启发，认为界面也可分解为有限的基础元素，再逐层组合成完整系统。
- 🧪 五个阶段分别是：原子、分子、组织、模板、页面，它们共同构成界面设计系统的层级。
- 🔹 原子：界面中最基础、不可再分的 HTML 元素，如标签、输入框、按钮，展示基础样式与固有属性。
- 🔗 分子：由原子组合而成、作为单元运作的简单 UI 组件，例如“标签 + 输入框 + 按钮”组成的搜索表单。
- 🧩 组织：由分子、原子或其他组织组成的较复杂组件，形成界面中的独立区块，如页头、产品网格。
- 🖼️ 模板：页面级对象，把组件放入布局并表达底层内容结构，关注图像尺寸、标题长度等内容骨架。
- 📄 页面：模板的具体实例，填入真实代表性内容，展示最终 UI，并测试设计系统是否有效。
- 🧭 原子设计不是“第 1 步原子、第 2 步分子”的线性流程，而是帮助同时思考整体与部件的思维模型。
- 🎯 它让设计师和开发者能在抽象与具体之间切换，像画家一样在细节笔触与整体构图之间来回审视。
- 🏗️ 它清晰区分结构与内容：模板体现内容骨架，页面呈现最终内容，但二者会相互影响。
- 🏷️“原子、分子、组织”提供了直观层级感，但命名不是教条；团队可按自身文化调整术语。
- 📱 原子设计适用于所有用户界面，不限于 Web，也可用于原生 App、Photoshop、ATM 等软件界面。
- 📸 以 Instagram 为例：图标、文字、图片是原子；导航栏、操作栏是分子；照片流是组织；再组合成模板与页面。
- 🛠️ 原子设计不专指 CSS 或 JavaScript 架构，而是跨技术的 UI 设计系统方法论；后续章节将讨论落地工具与流程。

---

