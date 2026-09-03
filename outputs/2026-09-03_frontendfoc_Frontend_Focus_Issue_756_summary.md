### [](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)

**原文标题**: [htmx 4.0.0 has been released! ~ htmx](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)

htmx 4.0.0 正式发布，历时八个月开发，核心内部从 XMLHttpRequest 迁移到 fetch()，行为与 2.x 基本兼容，但引入了显式属性继承、标准化事件、新历史机制及多项新特性和扩展。

- 🎉 发布背景：htmx 4.0.0 历经 8 个月开发，受 fixi 项目启发，并因 streaming HTML 需求决定改用 fetch()。
- 🏷️ 版本策略：2.x 仍保留为 NPM latest，4.0 暂时标记为 next，网站默认使用 4.0，htmx 2 将继续长期支持。
- 🔄 主要变化：属性继承改为显式（需添加 `:inherited`），事件命名标准化，历史记录不再默认使用 localStorage，内部迁移至 fetch()。
- 🧬 显式属性继承：htmx 2 的隐式继承改为显式声明，例如 `hx-confirm` 需写成 `hx-confirm:inherited`；这是升级时最大的改动。
- 🛠️ 升级辅助：提供命令行工具 `npx htmx.org@4.0.0 upgrade-check`，可扫描旧属性、事件名与 API，并支持多种模板文件扩展名。
- 📡 事件标准化：新事件命名遵循 `htmx:phase:action[:sub-action]`，如 `htmx:before:request`、`htmx:after:swap`，错误事件合并到 `htmx:error`。
- 📜 History 机制：不再使用 localStorage 做页面快照，返回时重新请求并替换 `<body>` 或 `[hx-history-elt]`，并提供 `hx-history-cache` 扩展支持本地缓存。
- 🧩 Morph Swaps：htmx 4 原生支持 morphing swap，集成 idiomorph 算法，让部分 DOM 更新更平滑。
- 🏷️ 新标签 `<hx-partial>`：可像 out-of-band 一样但更清晰地指定多个替换目标，如插入消息或更新计数。
- 🔌 新扩展生态：包括 `hx-preload`、`hx-download`、`hx-alpine-compat`、`hx-history-cache`，以及流式扩展 `hx-sse`、`hx-ws`、`hx-multipart`。
- 💡 hx-live 脚本方案：受 Alpine.js/jQuery/hyperscript 启发，主打与 htmx 紧密集成的前端脚本和 DOM 响应式。
- 📦 分发方式：可通过 npm 或 CDN 安装，也提供整合常用扩展的 `htmax.js` 单文件包。
- 🤖 LLM 支持：为 LLM 提供升级、调试、扩展开发与 htmx 引导等技能文件，如 `htmx-upgrade-from-htmx2`。
- ✅ 总结与致谢：htmx 2 会继续支持，用户无需强制升级；官方感谢多位核心贡献者的帮助。

---

### [htmx](https://four.htmx.org/)

**原文标题**: [htmx](https://four.htmx.org/)

概述摘要：htmx 是一个轻量级 JavaScript 库，通过自定义 HTML 属性扩展超文本功能，使网页具备现代动态交互能力，无需依赖其他框架。
- 🚀 仅约 11KB（min.br'd），零依赖，可直接通过 script 标签引入。
- ⚙️ 核心机制：使用`hx-post`、`hx-swap`等属性发送 AJAX 请求，并用响应 HTML 替换页面元素。
- 📖 配套书籍《Hypermedia Systems》免费在线阅读，指导基于 htmx 的应用开发。
- 💖 由赞助商支持，分为铂金、黄金、白银等级，并欢迎赞助。
- 🦉 作为 intercooler.js 的继任者，源自蒙大拿。

---

### [](https://four.htmx.org/docs/morphing-swaps-guide)

**原文标题**: [Morphing Guide ~ htmx](https://four.htmx.org/docs/morphing-swaps-guide)

htmx 4 已将 idiomorph 变形算法内置于核心，可通过 hx-swap 使用 innerMorph 和 outerMorph 实现 DOM 形态合并；本文说明了变形原理、稳定节点的方法、跳过规则、输入焦点保留及相关配置。

- 🔄 DOM Morphing 会将旧 DOM 编辑成新 DOM 形状，保留未变化节点的身份，从而不中断焦点、选区、滚动、视频播放以及脚本/组件状态。
- 🧩 在 hx-swap 中直接指定 innerMorph 或 outerMorph 即可使用，无需引入扩展；例如 <div hx-get="/status" hx-swap="innerMorph">。
- 📐 innerMorph 只变形目标元素的子节点，目标本身不动；outerMorph 则连同目标一起变形，类似 innerHTML 与 outerHTML 的区别。
- 🗺️ Idiomorph 算法利用新旧内容中的 id 建立映射，以最少移动重构 DOM；给重要元素添加稳定 id 有助于保持节点不被重建。
- 🚫 使用 hx-morph-skip 可冻结元素（属性和子节点都不变），hx-morph-skip-children 则只更新属性而保留子节点；也可通过 htmx.config.morphSkip / morphSkipChildren 扩展全局选择器。
- ⌨️ 变形时当前聚焦输入框/文本域的值会被自动保留，避免服务端旧回复覆盖用户输入；未聚焦的输入框在 value 属性未变时也会保留用户值。
- ⚙️ 可用 htmx.config.morphIgnore 配置不处理的属性前缀（默认 ["data-htmx-powered"]），通过 htmx.config.morphScanLimit（默认 10）控制算法在兄弟节点中查找匹配的深度。
- 📄 相关 API 包括 hx-swap、hx-preserve、hx-morph-skip、hx-morph-skip-children 等。

---

### [](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released#hx-partial)

**原文标题**: [htmx 4.0.0 has been released! ~ htmx](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released#hx-partial)

htmx 4.0.0 正式发布，历经 8 个月开发，内部从 XMLHttpRequest 迁移到 fetch()，行为与 2.x 高度兼容，但引入显式属性继承、事件命名标准化和新的历史记录机制，同时新增 morph 交换和 `<hx-partial>` 标签，并扩展了大量新扩展与工具支持。

- 🚀 发布背景：htmx 4.0.0 经过 8 个月开发，核心迁移到 fetch() API，为流式 HTML 和现代异步编程铺路，但仍保持与 2.x 相近的用户体验。
- 🔄 主要变化：属性继承从“默认隐式”改为“默认显式”，需在属性名后加 `:inherited` 才能让父级属性作用于子元素，这是最大的升级负担。
- 📝 事件重命名：所有事件统一为 `htmx:phase:action[:sub-action]` 格式，例如 `htmx:afterRequest` 变为 `htmx:after:request`，旧的 xhr/validation 事件被移除或替换。
- 🕰️ 历史记录：不再默认使用 localStorage 缓存页面，后退时重新抓取页面并替换 `<body>`；可选 `hx-history-cache` 扩展恢复 sessionStorage 缓存行为。
- ✨ 新特性 1：内置 morphing 交换（基于 idiomorph 算法），支持更平滑的 DOM 更新。
- 🧩 新特性 2：新增 `<hx-partial>` 标签，可更清晰地指定多个目标区域的响应内容，替代复杂的 out-of-band 操作。
- 🧰 扩展生态：因 fetch() 重构，新增 hx-preload、hx-download、hx-history-cache、hx-alpine-compat 等，并更新 SSE/WebSocket/multipart 流式扩展，还推出 hx-live 脚本方案和整合包 htmax.js。
- 🛠️ 升级工具：提供 `npx htmx.org@4.0.0 upgrade-check` 命令行工具，扫描模板并标记继承、事件名、废弃属性等迁移问题；还提供面向 LLM 的技能文件。
- 📦 安装方式：可通过 npm 指定 4.0.0 版本或 CDN 链接（如 unpkg）加载；NPM 上 2.x 仍为 `latest`，4.0 为 `next`，直到 2027 年初。
- 👥 致谢与兼容：htmx 2 将继续无限期支持，用户无强制升级压力；团队对多位贡献者表达了感谢。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Cloud 是一个基于 PostgreSQL 的时间序列数据托管平台，具备大规模处理能力、弹性架构和企业级合规特性，满足物联网等场景需求。

- 📊 支持单个服务承载每天 3 万亿指标、3PB 数据及 1 千万亿数据点，适合超大规模时序工作负载。
- 🎁 新用户注册即可获得 30 天有效期的 $1000 账户信用额度，无需信用卡。
- 🤝 受到数千家物联网企业的信任和采用。
- ⚖️ 通过副本集实现读写分离，最多可扩展至 10 个节点，并结合分层 SSD/S3 存储实现无限扩展。
- 💰 计算与存储分离，可独立伸缩，避免为闲置容量付费，降低成本和优化性能。
- 🛡️ 提供多可用区集群、自动故障转移、时间点恢复及跨区域备份，保障高可用性。
- 🔒 符合 SOC 2、HIPAA 与 GDPR 标准，支持始终加密、SSO、RBAC 和审计日志等企业级安全能力。
- 📉 内置查询钻取和仪表板，可将指标导出至 CloudWatch、Datadog、Prometheus，实现深度可观测性。
- ⚡ 数据库可在数分钟内完成部署，支持通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 可与主流云提供商及 PostgreSQL 生态进行集成。
- 🏢 提供合同化正常运行时间 SLA、区域数据隔离和企业级合规认证。
- 🎧 提供 24/7 全球专家支持，并保证企业级响应时间。

---

### [](https://css-tricks.com/css-random-function-polyfill/)

**原文标题**: [Let’s Use the Emergent CSS random() Function in all the Browsers | CSS-Tricks](https://css-tricks.com/css-random-function-polyfill/)

CSS 的 `random()` 函数正从 Safari 预览走向跨浏览器支持；作者通过开源 polyfill 让 Chrome/Firefox 也能体验受控随机 UI，并演示了多个案例与实现原理。

- 🎲 开篇从“运气与随机性”切入，认为网页设计中适度的受控随机（如品牌化 confetti）很有吸引力，但生成式 UI 等过度随机需谨慎。
- 🌱 2025 年底 Safari 首个支持 CSS `random()`；Chrome/Firefox 进展不明，作者决定用 polyfill 提前享用该特性。
- 🧩 具体做法：在 HTML 引入 `css-random-polyfill` 脚本，并为需要处理的元素加 `randomized` 类。
- ✨ 星场 demo 展示 `random()` 用于大小、位置、色相、动画速度与延迟；第三个参数作为步长，`element-shared` 可让同类元素共享随机角度。
- 🎨 彩色网格 demo 验证 `random()` 可嵌入 `grid-area` 等缩写属性，复数调用可出现在同一值中。
- 🎡 转盘 demo 演示不同角度单位可混用，如 `random(2turn, 10turn, 20deg)`，只要属于同一数据类别。
- 🟦 随机方块 demo 使用自定义 key（如 `--side`）让多个属性的随机值保持一致。
- 🧪 延伸试验：在 Chromium 中用 CSS `@function` 和 inline conditional 自制 `--item`，模拟尚未通用的 `random-item()` 从列表随机选值。
- ⚙️ polyfill 原理：先用 `CSS.supports()` 判断是否原生支持；否则临时隐藏 `.randomized` 元素，遍历所有以 `--random` 开头的自定义属性。
- 🔬 它让浏览器把含 `random()` 的表达式作为字符串传入计算样式，再由 `@csstools/css-calc` 解析成具体值，并写回内联样式；同时生成 document/element 标识以支持缓存语义。
- 💡 因无需重新抓取或解析完整样式表，该方案规避了许多传统 CSS polyfill 的坑；若浏览器原生支持 `random()`，polyfill 会直接放行，未来删除脚本仍可运行。
- 🚀 作者将 polyfill 开源并提供 CodePen 示例，呼吁大家趁等待原生支持时尝试随机化创意。

---

### [](https://www.bram.us/2026/08/27/feature-detecting-undetectable-css-features-with-supports-named-feature/)

**原文标题**: [Feature Detecting “Undetectable” CSS Features with @supports named-feature() – Bram.us](https://www.bram.us/2026/08/27/feature-detecting-undetectable-css-features-with-supports-named-feature/)

CSS 传统上使用 `@supports` 检测选择器、属性与值等支持情况，但无法检测底层实现变化或两个属性组合后的新行为。为此新引入 `@supports named-feature()` 函数，通过预设关键词来暴露这些“原本无法检测”的能力，解决了诸如 Flexbox gap、变换感知锚点定位等历史难题。

- 📖 **背景问题**：`@supports` 仅检查声明能否被解析，不验证组合效果，导致过去无法用 `@supports (display:flex) and (gap:1em)` 检测“Flexbox 是否支持 gap”。
- 🧩 **解决方案**：CSS 工作组采纳 David Baron 的提议，定义 `named-feature()` 函数，使用规范预设的关键词，可精准检测特定行为变化；目前只定义了少量关键词。
- 🎯 **关键词一：`anchor-position-follows-transforms`**：用于检测锚点定位是否支持变换感知（即锚点受 transform 影响）；解决了此前需要 hacky 变通方法才能判断的问题。
- 🎯 **关键词二：`single-axis-scroll-container`**：用于检测单轴滚动容器支持，让 `position: sticky` 可逐轴生效，避免被另一轴无关滚动容器困住；此前只能靠大量 JavaScript 检测。
- 🌐 **浏览器支持概况**：`named-feature()` 本身 Chromium Chrome 150、Firefox 156（即将 beta）、Safari Technology Preview 已支持；`anchor-position-follows-transforms` 三引擎大致同步，`single-axis-scroll-container` 目前仅 Chrome 153 支持。
- ⚠️ **注意假阴性**：例如 Chrome 144–150 与 Safari 27 已支持转换感知锚点定位，但因 `named-feature()` 支持滞后，会出现误判为不支持的情况。
- 🧹 **旧特性未加关键词**：`gap` 用于 Flexbox 已普及且时间久远，`align-content` 影响 `block` 容器经测试无大碍；因此没有必要新增关键词。
- 🔮 **未来方向**：样式查询等仍难检测，不过有变通方法；`@supports-condition`（自定义 supports 条件）有望彻底解决这类问题，但目前仅有 WG 决议。

---

### [](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/155)

**原文标题**: [Firefox 155 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/155)

Firefox 155（2026 年 9 月 1 日发布）为开发者带来多项更新：开发者工具增强，CSS 新增函数与属性，JavaScript 新增 Promise 方法并修复模块缓存，HTTP/WebTransport/WebGPU 等 API 扩展，WebAssembly 与 WebDriver 也有改进，另有若干默认禁用的实验性特性。

- 🛠️ 开发者工具：规则视图新增仿真面板，支持模拟 `prefers-reduced-motion`；JSON Viewer 支持逐行解析 JSON Lines（NDJSON）；调试器新增禁用断点的键盘快捷键。
- 🎨 CSS：`attr()` 现可用于任意 CSS 属性，并支持类型单位、回退值和命名空间属性；新增 `progress()` 与 `alpha()` 函数；`font-width` 取代 `font-stretch`（旧名仍作为别名）。
- 🧩 JavaScript：支持 `Promise.allKeyed()` 和 `Promise.allSettledKeyed()`；因网络错误或 MIME 类型错误而失败的模块加载不再被缓存为失败，后续可成功导入；`modulepreload` 的 `load`/`error` 事件行为已修正。
- 🌐 HTTP/网络：连接建立采用 Happy Eyeballs version 3，并行尝试 IPv6/IPv4；支持 QUIC 版本协商，使 HTTP/3 可使用 QUIC version 2。
- 📡 API/WebTransport：新增发送组（send groups）、`exportKeyingMaterial()`、`createWritable()` 及 `protocols` 选项；`draining` 属性指示服务器请求优雅关闭会话。
- 🎮 WebGPU：桌面端支持 dual-source-blending 特性，渲染管线中可用 `src1`、`one-minus-src1` 等混合因子，并支持 WGSL `dual_source_blending` 扩展。
- 🗺️ DOM/SVG：`SVGAElement` 现暴露 URL 组件属性；SVG 列表接口（如 `SVGTransformList`）支持索引赋值；`getBBox()` 支持 `fill`、`stroke`、`markers`、`clipped` 选项；未渲染元素不再返回错误的边界盒。
- 🎥 WebRTC/媒体：`RTCDataChannel` 的 error 事件可报告 `sctp-failure`；`RTCPeerConnection.sctp` 在规范要求的信令阶段返回传输对象；支持双字节 RTP 头扩展 ID；`getStats()` 的传输统计在协商前更准确。
- ⚙️ WebAssembly：支持 compact import section 二进制格式扩展，减小含大量导入的模块体积；实现 wide arithmetic 提案，新增 `i64.add128`、`i64.mul_wide_s` 等产生 128 位结果的指令。
- 🕹️ WebDriver：修复下载面板导致当前文档失焦以及 Ctrl+ 双击不触发 `dblclick` 的问题；WebDriver BiDi 的 `moz:debugging` 模块不再依赖 DevTools 嵌套事件循环；`session.unsubscribe` 移除 `contexts` 参数支持。
- 🔌 附加组件开发者：该版本未列出面向附加组件的特定更改。
- 🧪 实验性 Web 特性（默认禁用，可在 `about:config` 开启）：滚动驱动动画、CSS Typed Object Model Level 1、`@supports` 中的 `at-rule()` 查询、Audio Session API、`line-clamp` 无前缀版及 `no-ellipsis` 支持、scoped custom element registries、正则表达式缓冲区边界断言（仅 Nightly）、`background-clip` 的 `border-area` 值。

---

### [](https://webiterate.dev/google-removed-extensions-ublock-origin-108/)

**原文标题**: [Google Has Removed Manifest V2 Extensions From the Chrome Web Store, Including uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/)

Google 今日正式从 Chrome 网上应用店移除所有 Manifest V2 扩展，包括广受好评的 uBlock Origin，并停止更新与重新安装；此举也影响依赖 Chrome 商店的其它 Chromium 浏览器，但 Brave 自行托管了部分 MV2 扩展；Google 宣称 MV3 更安全、隐私和高效，但遭用户质疑其真实动机。

- 🗑️ Google 已从 Chrome 网上应用店移除全部 Manifest V2 扩展，uBlock Origin 等知名内容拦截器均在列。
- 🕐 已安装在 Chrome 138 或更早版本的 MV2 扩展仍可使用，但无法再接收更新或从商店重新安装。
- 🌐 Chrome 网上应用店是多数 Chromium 浏览器的默认扩展来源，移除操作的影响不止于 Chrome，Brave 等浏览器用户也无法再安装这些扩展。
- 🦁 Brave 团队选择自行托管 AdGuard、uBlock Origin、uMatrix 和 NoScript 四款热门 MV2 扩展，并允许用户轻松启用。
- 🔒 Google 给出的理由是新版 Manifest V3 能带来更强安全性、隐私保护、性能提升，并更严格限制扩展权限。
- 💬 评论区用户强烈反对，认为移除 MV2 与用户安全无关，而是为了维护 Google 及其广告伙伴对用户活动的监控与获利。

---

### [](https://web.dev/blog/web-platform-08-2026)

**原文标题**: [New to the web platform in August  |  Blog  |  web.dev](https://web.dev/blog/web-platform-08-2026)

2026 年 8 月期间，Web 平台迎来多项稳定版浏览器新特性与 Beta 版更新。Chrome 152 和 Firefox 154 先后发布稳定版，Safari 本月无稳定版更新。许多 CSS 与 HTML 功能落地并成为 Baseline 新可用状态，同时新 Beta 版也已推出供开发者预览测试。

- 🌐 Chrome 152、Firefox 154 于 8 月发布至稳定版，Safari 本月无稳定版更新，多款新功能正式成为 Baseline 新可用。
- 📐 text-box 相关属性（text-box-trim、text-box-edge 及简写）获 Firefox 154 支持，可精细控制文字在块方向的对齐与间距，现为 Baseline 新可用。
- 🔢 sibling-count() 与 sibling-index()CSS 函数随 Firefox 154 新增，支持以纯 CSS 实现动态布局尺寸、交错动画延迟及颜色变化，现为 Baseline 新可用。
- ⌨️ 全局 HTML 属性 autocorrect（可控制拼写与标点自动修正）获 Chrome 152 支持，现为 Baseline 新可用。
- 🎭 Chrome 152 将 CSSPseudoElement 支持扩展至::backdrop、::scroll-marker 和::view-transition，便于直接监听伪元素事件。
- 🎨 Chrome 152 引入 CSS Color 5 的 alpha() 函数，用于调整原色透明度并保留颜色通道，支持在各色彩空间中无缝使用。
- 🖱️ Chrome 152 新增标准 window-drag CSS 属性，为安装版桌面 Web 应用自定义标题栏或头部设置可拖拽区域，替代旧有 app-region 属性。
- 📝 Chrome 152 推出 OpaqueRange API，用于在表单控件文本上执行范围相关操作（如定位、高亮），同时保持组件封装性。
- ➕ Firefox 154 为 Iterator.prototype 新增 includes()、join()、chunks() 与 windows() 等方法，提供更便捷的迭代器处理能力。
- 📡 Firefox 154 增强 WebRTC 传输能力，包括 getSelectedCandidatePair()、DTLS 错误事件、RTCP 参数支持及传输统计信息；部分功能现为 Baseline 新可用。
- 🔍 Chrome 153 与 Firefox 155Beta 版已发布，可预览下一波新功能。
- 🧪 Chrome 153Beta 包含单轴滚动容器（overflow: scroll clip）、scroll-axis-lock 属性、Iterator join() 与 zip()，以及专用<camera>和<microphone>元素。
- 🔗 Firefox 155Beta 为 SVG <a>元素引入 HyperlinkElementUtils 属性，并为 SVG 列表接口新增索引设置器，提升 URL 属性访问与列表操作能力。

---

### [获取失败](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/)

**原文标题**: [Failed to retrieve](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/)

无法总结：获取内容失败，状态码 403。

---

### [CSS 单位——完整参考](https://cssunits.com/)

**原文标题**: [CSS Units â The Complete Reference](https://cssunits.com/)

该文章全面介绍了 CSS 中所有 63 种单位，按类别划分并配有实例，帮助你理解每种单位的用途与适用场景。

- 📏 **绝对单位**：包含 px、cm、mm 等固定单位，不受上下文影响，是 CSS 尺寸的基础。
- 🔤 **字体相对单位**：em、rem、ch、ex 等基于当前或根元素字体属性，适合实现可伸缩的排版。
- 💯 **百分比**：本质上是相对值，具体含义由所作用的 CSS 属性决定。
- 🖥️ **视口单位**：vw、vh 以及现代新增的 svh、lvh、dvh 等，根据浏览器视口尺寸动态变化。
- 📦 **容器单位**：cqw、cqh、cqi 等，基于最近的容器查询祖先，适合组件化布局。
- 🔗 **弹性单位**：fr 是网格特有的分数单位，表示剩余空间的份额，而非固定长度。
- ⚙️ **特殊单位**：覆盖角度（deg、turn）、时间（s、ms）、分辨率（dpi 等），用于动画、变换和媒体查询。
- 🧮 **数学函数**：calc、min、max 和 clamp 可组合各种单位进行灵活计算。
- 🌳 **决策树与速查表**：提供按任务选单位的路径、每种单位的公式与参考，以及专业术语解释。

---

### [如何使用 CSS Grid 构建平铺图案](https://www.carmenansio.com/articles/modernist-tiles-css-grid/)

**原文标题**: [How to Build Tile Patterns with CSS Grid](https://www.carmenansio.com/articles/modernist-tiles-css-grid/)

文章展示了如何运用 CSS Grid 重新创作巴塞罗那常见的现代主义水压瓷砖地板，并深入解释图案生成、旋转规则、subgrid 跨缝绘制以及三角函数在 CSS 网格中的高级运用。

- 🏠 现代主义地砖遍布巴塞罗那，作者家中保留着六种不同的原始花纹，不少房间各有专属图案。
- 🔲 核心机制是“同一块瓷砖按固定规则旋转”，由 CSS Grid 自动铺设成 45 块地砖，无需绘制新形状。
- 🌰 Fan、Lens、Wedge 属于基础造型：分别利用 radial-gradient、border-radius 与伪元素圆角制作。
- ⭐ Star 以 linear-gradient 切出双色三角形，通过旋转组合出风车纹样；Bloom 与 Weave 保持全对称，不随旋转变化。
- 🌐 Weave 的边缘刻意设计得能首尾相接，相邻瓦片的弧线会连成一条连续线条，形成“跨瓷砖”的新图形。
- 🧩 使用 subgrid 让装饰层继承底层网格线，能精准把星形放在接缝交叉点上；position:absolute 可避免遮挡瓦片布局。
- 🎨 配色源自真实历史颜料：红、黄由廉价氧化铁与赭石制成；蓝、绿因含钴和铬成本更高。
- 📐 CSS 原生支持 sin()、cos()、atan2()，可在 calc() 中动态计算旋转角度，让瓷砖像磁针一样指向网格中心。
- ⚠️ 在 grid-template-columns 里混用 fr 单位和三角函数 calc() 会被浏览器视为无效，导致列全部塌缩。
- ✅ 改用百分比（如 calc(11.1111% + 4% * sin(...))）就能正常工作，轨道宽度可由三角函数实时控制。
- 🧠 同一个正弦数学还可用于扭曲整张网格的列宽，让 CSS Grid 的轨道本身也“参与计算”，而不只是瓦片内部变形。
- ✨ 文章强调，真正吸引人的是 CSS Grid 可以突破瓷砖本身的对称限制，让现代数学与百年传统图案自然结合。

---

### [](https://dbushell.com/2026/09/01/text-editor/)

**原文标题**: [Fine, Iâll build my own text editor! â David Bushell â Web Dev (UK)](https://dbushell.com/2026/09/01/text-editor/)

作者通过比较 `<canvas>`、`contenteditable` 与 `<textarea>` 三条技术路线，亲手尝试构建一个文本编辑器。文章记录了每种方案的性能、无障碍与功能取舍，并给出后续优化方向，最终认为 `textarea` 在长文本上表现最好，但仍需解决语法高亮和虚拟滚动等复杂问题。

- 💭 受“现在的软件都是垃圾”的吐槽鼓舞，作者决定自己造一个文本编辑器，验证“我有很大容错空间”。
- 🖥️ 最初用 `<canvas>` 渲染全部内容：CPU 负担高、无法交互，且缺少选区、撤销、多行粘贴、溢出滚动等核心功能。
- 🖥️ 为补足滚动，作者用隐藏 `<div>` 配合原生 overflow 计算偏移；但 `<canvas>` 从根本上无法解决无障碍问题，因此放弃。
- 📝 改用 `contenteditable="plaintext-only"` 的 `<div>`，天然获得文本选择、撤销历史及大量无障碍支持。
- 📝 必须显式关闭 `spellcheck`、`autocorrect` 等属性，否则会有输入延迟；作者花了数天才发现这个修复。
- 📝 但 `contenteditable` 在字符数较多时性能不稳定，Chromium、WebKit 与 Firefox 的表现差异很大。
- ✍️ 改用 `<textarea>` 处理长文本性能最佳；但因无法用 CSS 自定义高亮，作者额外增加了一层 `<div>` 来渲染可见行的语法高亮。
- 🚀 文中提到了 `OpaqueRange API`（可给 textarea 加自定义高亮）和 `EditContext API`（改善 canvas 输入），作为后续优化空间。
- 🎨 大量 CSS 高亮也可能成为性能瓶颈；更稳健的方案是用 Tree-sitter 生成语法树，只给可见行生成高亮，再结合 inverse sticky technique 做虚拟化滚动。
- ⚗️ 作者承认目前成品“看起来像 90% 的编辑器，但功能只有 1%”，剩下一堆细节如 Tab 缩进等尚待完善。
- 🔤 最后提醒：JavaScript 字符串按 UTF-16 码元计算长度，直接处理 emoji 或组合字符极易出错，需用 `Intl.Segmenter` 按字素进行正确分割。

---

### [](https://expo.dev/solutions/expo-for-react-web-devs?utm_campaign=33087804-React%20to%20Native&utm_source=email&utm_term=front-end-focus)

**原文标题**: [Expo for React web devs](https://expo.dev/solutions/expo-for-react-web-devs?utm_campaign=33087804-React%20to%20Native&utm_source=email&utm_term=front-end-focus)

Expo 是一个面向 React 开发者的原生移动应用框架，让开发者无需学习全新工具即可将现有 React 技能延伸至 iOS 和 Android 应用开发。它强调真正的原生渲染、多平台共享代码，并通过各类工具和服务简化移动开发流程，获得大量开发者社区认可。

- 📱 使用 React 技能即可构建 iOS/Android 原生应用，无需重学工具或从零开始
- 🧩 沿用组件化模型，大部分代码为 JavaScript/TypeScript，可直接复用已有 React 知识
- ⚛️ React Native 渲染真实平台 UI 而非 WebView，提供原生级性能与体验
- 🌐 单一代码库可同时发布 iOS、Android 和 Web，导航及后端逻辑也可跨平台共享
- 🛠️ Expo 提供 100+ 维护良好的库、文件路由（类似 Next.js）以及原生 API 的 hooks/components
- 🏗️ EAS Build 与 Submit 自动化处理 Xcode/Android Studio 的构建提交步骤
- 📂 Expo Router 文件路由和 EAS Hosting 等方案让 React 开发者快速上手全栈移动开发
- 📚 提供多个教程和文档资源，帮助开发者从 Web 平稳过渡到原生应用
- ❤️ 大量开发者社区反馈表达了对 Expo 的喜爱，认为其更新快速且使用简单
- 🔗 页面同时提供文档、博客、定价、企业方案等更多导航入口供用户探索

---

### [网页上的增强拼写检查](https://bkardell.com/blog/EnhancedSpellchecking.html)

**原文标题**: [Enhanced Spell Checking on the Web](https://bkardell.com/blog/EnhancedSpellchecking.html)

Overview summary：  
文章介紹了瀏覽器拼寫檢查的現有機制與限制，並提出一個新 API「SpellCheck Custom Dictionary」來解決領域特定詞彙被誤判為錯誤的問題，同時說明實作狀態、相關的輕量載入函式庫，以及未來展望。

- 🔍 現有拼寫檢查功能會依賴各作業系統、瀏覽器甚至設定檔的字典，導致標記結果不一致，且為了避免指紋風險，實際運作細節並未標準化。
- 🧩 網頁應用常涉及專業領域（如數學、法律、股票、醫療等），這些詞彙不在一般字典中，容易造成大量誤判與干擾。
- 📜 新提案推出 `document.spellCheckCustomDictionary` API，僅包含 `addWords()` 與 `removeWords()` 兩個方法，將詞彙加入臨時的 Set，且只影響目前文件生命週期。
- 🚀 此 API 由 Igalia 實作，並由 Bloomberg Tech 資助；目前在 Chrome Canary 的實驗性旗標下可用，預計 2026 年 9 月 8 日隨旗標正式推出。
- 📦 API 設計簡潔，可直接 fetch JSON 陣列後呼叫 `addWords()`；作者建議採用漸進增強方式載入，並形容未來若能提供宣告式 API 會更理想。
- 🛠 作者提供一個小型函式庫，可透過帶有 `data-spellcheck-dictionary` 屬性的 `<link>` 標籤載入 JSON 詞彙，原始版本僅 441 bytes（Brotli 壓縮後）。
- 📁 另有功能較完整的「-complete」版本（約 770 bytes），並提供 repo 內含初步的領域字典範例，歡迎以 PR 貢獻更多詞彙。
- 💡 目前實作仍有粗陋之處，例如移除 link 不會移除詞彙、變更 href 不會更新；真正的標準實作未來應能處理這些情況。
- 🙏 文末感謝 Bloomberg Tech 的資金贊助，並邀請社群試用與回饋想法。

---

### [获取失败](https://github.com/Igalia/explainers/blob/main/spell-check-dictionary/README.md)

**原文标题**: [Failed to retrieve](https://github.com/Igalia/explainers/blob/main/spell-check-dictionary/README.md)

无法总结：获取内容失败，状态码 429。

---

### [邮件验证 API · Resend](https://resend.com/blog/email-verification-api)

**原文标题**: [The Email Verification API · Resend](https://resend.com/blog/email-verification-api)

这篇文章介绍了一个全新的浏览器 API——Email Verification API，它让邮箱所有者验证能够在浏览器中直接完成，避免传统跳转到收件箱操作的麻烦，从而改善用户体验并保护发件方信誉。目前该提案仍在早期阶段，但可通过逐步增强的方式尝试。

- ✉️ 背景：收集邮箱时应验证所有权，传统做法是发送一次性密码或魔法链接，但需要用户离开页面，增加摩擦并容易流失用户。
- 🚀 API 优势：如果浏览器和邮箱服务商能直接验证地址，用户无需离开表单即可完成验证，流程更流畅，同时减少无效或拼写错误的邮箱所带来的退信风险。
- 🧪 实现现状：API 仍处于提案阶段；Chrome 通过 origin trial 支持，Gmail 目前可做邮箱验证；建议作为渐进增强功能使用，也可利用其他验证 API（如检查语法、MX 记录和 SMTP）作为替代。
- 🔄 工作原理：用户先在邮箱提供商处登录；之后在站点提交邮箱时，浏览器会判断该邮箱是否属于当前登录用户，若是则协同生成令牌写入隐藏字段；服务器收到邮箱和令牌后，通过解密和校验确认所有权。
- 💻 前端实现：表单的邮箱输入需要设置 `type="email"` 和 `autocomplete="email"`；还需一个带有 `autocomplete="email-verification-token"` 的隐藏输入，并绑定随机 nonce 到用户会话。
- 📦 服务端验证：可使用 npm 包 `email-verification-api`，调用 `verifyEmailToken({ email, token, audience, nonce })` 来简化验证流程；官方还提供了 Next.js 示例应用参考。
- 😊 双重收益：对用户而言无需离开页面、不改变习惯；对应用而言能确认邮箱确实是用户本人，并能避免不存在地址带来的硬退信，保护发件人信誉。
- 📌 后续关注：可在 GitHub 上 star 该提案，关注 Chrome 开发者博客获取更新；如需实现，可查看 `email-verification-api` 仓库。

---

### [](https://www.bram.us/2026/08/18/the-case-for-tri-state-dark-mode-toggles/)

**原文标题**: [The Case for Tri-State Dark Mode Toggles – Bram.us](https://www.bram.us/2026/08/18/the-case-for-tri-state-dark-mode-toggles/)

暗色模式切换开关应提供“系统、浅色、深色”三态，而非仅有“浅色/深色”的两态。作者通过与 Lea Verou 的争论、社交平台投票及具体使用场景论证：两态开关会让用户在系统自动切换时感到困惑；三态开关虽多一个选项，却能提供更清晰、可预测的控制体验，真正做到以用户意图优先。

- 🌓 作者主张暗色模式切换应使用三态控制（系统 / 浅色 / 深色），而非简单的两态切换。
- ⚔️ 新潮文章起因于《Modern Web Guidance》建议采用两态控制，作者与指南作者 Lea Verou 因此展开辩论。
- 📊 社交平台投票结果显示：43 人支持三态，仅 7 人支持两态，许多受访者还补充了支持三态的实际理由。
- 🕖 两态控制的典型问题：当用户系统设置为随日夜自动切换时，用户白天显式选择“浅色”，夜间重新访问却可能自动变成“深色”，违背用户明确选择。
- 🏷️ 作者认为两态控制并非完全不可用，但必须清晰标注“Auto”或将真正的数值写入存储，并提供重置入口——而这几乎等同于最终需要三态。
- 💡 文章也介绍了 Vale 的折中设计方案：只显示“浅色”和“深色”两个按钮，默认都不选中以隐含“跟随系统”，点击已选按钮可回到系统状态。
- ✅ 三态控制的核心价值是“清晰优于简洁”：用户完成一次选择后，就能确定并维持自己的偏好，不会因时间或系统变化产生意外结果。
- 🗣️ 评论区还围绕“额外点击是否值得”进行讨论，作者坚持认为对不常访问的网站而言，明确而可预测的三态选择更加友好。

---

### [深色模式切换：两种状态就够了 • Lea Verou](https://lea.verou.me/blog/2026/dark-mode-toggles/)

**原文标题**: [
		Dark mode toggles: two states are enough • Lea Verou](https://lea.verou.me/blog/2026/dark-mode-toggles/)

这篇文章认为，常见的“亮色/暗色/系统”三态主题切换是“实现驱动”的界面设计，会增加不必要的 UX 摩擦。一个好的两态开关其实能表达全部三态，只需在第一次点击时生成相反值的覆盖，再次点击则恢复跟随系统。真正值得使用三态的场景只有独立设置面板，以及颜色实现确实受系统环境影响的特殊设计。核心原则是：不要拿用户当前没有遇到的问题去打扰他们。

- 🌗 三态切换（Light/Dark/System）看似合理，但用户只在页面“看起来不对”时才会去寻找主题开关，因此“保持系统状态”并不是真实的用户目标。
- ⚙️ 这种设计属于“数据模型泄漏”：底层确实需要三态存储，但界面应该暴露与用户目标相关的状态，而不是把所有实现状态都堆出来。
- 😵‍💫 三态控件会增加认知负担与操作成本：要么用三个图标占据更多空间，要么收起成下拉菜单，把一键操作变成两步，还要让用户在没有可见差异的选项之间做选择。
- 🎯 好的两态开关可以这样实现：平时显示系统解析出的当前主题图标；点击后切换为相反主题并保存覆盖值；再次点击则清除覆盖，回到跟随系统。
- ⚡ 常见错误是系统主题变化时“好心”清除用户显式设置的覆盖值，这会让用户无法真正固定主题；覆盖是否已等于系统默认，只能由用户在交互时决定，不能后台悄悄清理。
- 😌 即使出现某次点击意图被误解的“混淆”，也只会在系统切换时发生一次，而且一次点击就能修复；为这种罕见问题引入永久 UI 复杂度并不划算。
- 🗂️ 合理的三态例外包括：主题选择放在独立设置面板中（用户正处于决策模式、需要面向未来选择）；以及同一颜色方案在不同系统设置下实现确实不同、必须让用户分辨时。
- 💡 更通用的经验是：不要让用户对尚未遇到的问题表态；未来才可能相关的选项，应该留到真正相关时再出现，始终要“尊重用户努力”。
- 🚫 作者最后补充：最好的暗色模式开关也许根本不是“开关”；如果浏览器未来能原生提供这套机制，会比每个网站各自造轮子更好。

---

### [](https://jakearchibald.com/2026/css-custom-property-compute-time/)

**原文标题**: [Controlling when CSS custom property values are computed - JakeArchibald.com](https://jakearchibald.com/2026/css-custom-property-compute-time/)

CSS 自定义属性值的计算时机并不总是直观：是否通过 `@property` 注册并指定 `syntax`，会决定变量是保留为 token 流到使用处再求值，还是在声明它的元素上立即计算。文章用 `sibling-index()` 的示例对比了这两种行为，并说明 `var()`、URL 等情况也受此影响。

- 🔍 默认情况下，未注册的 CSS 自定义属性按 token 流存储，例如 `--index: sibling-index()` 不会立即求值。
- 📍 当通过 `var(--index)` 在子元素中使用时，`sibling-index()` 在子元素上下文计算，因此作为第一个子元素时 `scale` 为 1。
- 🖥️ `getComputedStyle()` 会返回未计算的原始字符串 `"sibling-index()"`，反映默认“延迟计算”的特点。
- 🏷️ 如果通过 `@property` 将 `--index` 注册为 `syntax: '<number>'`，它会在声明它的元素上立即计算出数字结果（示例中为 2）。
- 🌐 注册 `@property` 会把计算上下文从“使用变量处”改为“声明变量处”，从而改变最终样式，也影响相对字体单位、容器查询单位等。
- 🔗 URL 解析也有类似差异：默认按引用该变量的样式表位置解析，注册为 `<url>` 后则固定在声明它的样式表上。
- 🔧 `var()` 属于“任意替换函数”（如 `if()`、`attr()` 等），在自定义属性内部展开时会先被替换，导致子元素上的 `--multiplier: 3` 被忽略，而使用声明处的值 1。
- 🧩 理解 `@property` 的 `syntax` 对计算时机的影响，能更准确地预测和控制自定义属性产生的样式结果。

---

### [](https://ronaldsvilcins.com/2026/08/30/native-html-and-css-features-that-replaced-javascript/)

**原文标题**: [Native HTML and CSS Features That Replaced JavaScript Â· Ronalds VilciÅÅ¡](https://ronaldsvilcins.com/2026/08/30/native-html-and-css-features-that-replaced-javascript/)

现代 HTML 与 CSS 已具备大量原本需要 JavaScript 才能实现的交互与布局能力，作者建议优先使用浏览器原生方案，只在必要的时候才引入 JavaScript。这样能减少代码量、依赖和维护成本，也让行为更贴近平台本身。

- 📂 使用原生 `<details>` + `<summary>` 就能实现手风琴/FAQ，无需编写点击切换和显隐逻辑。
- 🪟 原生 `<dialog>` 大幅简化模态框，打开、关闭、遮罩与焦点管理大多由浏览器接管。
- 📌 Popover API 让按钮通过 `popovertarget` 就能控制弹出层，很多菜单和小组件完全不需要 JavaScript。
- 🔗 CSS `:has()` 允许根据子元素状态改变父级样式，取代了过去用 JavaScript 添加 class 的方式。
- 📐 容器查询让组件根据自身可用宽度响应式布局，替代了原来使用 `ResizeObserver` 等测量脚本的做法。
- 📏 `field-sizing: content` 可以让 textarea 随内容自动增高，一行 CSS 取代手动测量高度的脚本。
- 🌗 `light-dark()` 配合 `color-scheme` 即可跟随系统明暗主题，无需再用 JavaScript 探测主题偏好。
- 📜 `scroll-behavior: smooth` 和 `position: sticky` 分别替代了平滑滚动与滚动监听的吸顶实现。
- 🎠 CSS Scroll Snap 能实现横向滚动卡片自然吸附，满足简单轮播需求时不必引入轮播库。
- 🖼️ `aspect-ratio` 能保持图片、视频或容器的宽高比，取代了大量百分比 padding trick 和 JS 计算。
- 🎞️ CSS 滚动驱动动画可以用 `animation-timeline: scroll()` 实现滚动进度条等效果，无需监听 scroll 事件。
- ✨ CSS 过渡配合 `@starting-style` 可以更自然地处理 popover、dialog 等元素的显隐动画，减少脚本协调。
- ✅ 原生表单验证（如 `required`、`pattern`、`min`/`max`）配合 `:user-invalid` 等选择器，已能处理大量验证需求。
- ⚡ `loading="lazy"` 让图片和 iframe 能由浏览器决定加载时机；`srcset`/`picture` 则原生解决了响应式图片问题。
- 🎨 CSS 自定义属性让 JavaScript 只需要改变一个主题变量或 class，而不必逐条修改元素的内联样式。
- ⚙️ `prefers-reduced-motion`、`prefers-color-scheme` 等用户偏好媒体查询，原本很多也可直接交由 CSS 处理。
- 💡 作者的决策顺序是：先问 HTML 能否实现，再问 CSS 能否实现，然后才是少量 JavaScript，最后才考虑库或框架；原生并不永远更优，但能删除的代码就是最好维护的代码。

---

### [Web 性能星期三 006 – 更快的浏览器发布改变你的 RUM 用户群体](https://csswizardry.com/2026/08/web-perf-wednesday-006-faster-browser-releases-change-your-rum-population/)

**原文标题**: [Web-Perf Wednesday 006 – Faster Browser Releases Change Your RUM Population – CSS Wizardry](https://csswizardry.com/2026/08/web-perf-wednesday-006-faster-browser-releases-change-your-rum-population/)

浏览器发布节奏的加快正在重塑 RUM（真实用户监控）分析方式：Chrome 和 Firefox 双双转向双周发布，DevTools 新增软导航指标，而 TTFB 分析则揭示了此前被忽略的导航开销。这篇文章解释了这些变化如何影响性能数据解读，并给出了应对建议。

- 🌐 Chrome 从 153 版开始将发布周期由四周缩短为两周，首个 Stable 版定于 9 月 8 日；Beta 比 Stable 早三周，Extended Stable 仍保持八周。
- 🦊 Firefox 也宣布转向双周发布，Firefox 155 提前至 9 月 1 日，桌面端和 Android 端作为实验性调整。
- 📊 更快的浏览器版本使“浏览器主版本”成为变化更快的 RUM 维度：按精确版本切分会产生更小、更短暂的样本群，28 天图表内会出现更多发布边界，容易与网站自身改动混淆。
- 🧠 分析建议：在按版本切分前设置最小样本量和完成率阈值；当精确版本数据过薄时，回退到更宽的浏览器版本群体；同时保留未切分的总体趋势视角。
- 📅 应将 Chrome/Firefox 发布日期纳入与站点部署、CDN、标签管理器相同的发布日历，并指定专人负责版本注释；Beta 阶段需测试真实用户旅程和埋点，而非当作晚期兼容性检查。
- 🛠️ Chrome 152 DevTools 的 Live Metrics 默认报告软导航（SPA 路由切换）的 Core Web Vitals，由 web-vitals v6 驱动；Network 面板也新增了固定的“Request #”列，便于调试。
- ⏱️ 新文章《Unattributed Navigation Overhead》提出计算 TTFB 中未被重定向、DNS、连接和请求响应阶段覆盖的“缺失时间”（UNO）；某客户数据中发现 713 万次 UNO 观测，而仅 166 次可见重定向。
- 📈 建议将 UNO 作为持续时间和发生次数加入 RUM，并按落地页、活动、来源、浏览器、连接方式拆分；UNO 升高时需通过性能调查复现流程，而不是简单归咎于服务器。
- ⚠️ 浏览器发布周期加快意味着 RUM 数据变动未必是站点部署引起的；在判定回归前，应对比 Chrome 主版本分布、样本数、设备比例和指标完成率。
- 💡 若浏览器发布导致 RUM 人群结构变化快到团队难以解释，可考虑建立包含浏览器、埋点、应用和交付变更的完整测量模型，避免把每次莫名波动都当成产品事故。

---

### [](https://ambientcss.vercel.app/)

**原文标题**: [Ambient CSS — a physics-based lighting system for CSS](https://ambientcss.vercel.app/)

请提供您需要总结的文本内容，我会按照模板为您生成“概述摘要 + 项目符号列表”的中文总结。

---

### [](https://kikkupico.github.io/ambientcss/ambient-css/grounded/)

**原文标题**: [Grounded on Blender renders | Ambient CSS](https://kikkupico.github.io/ambientcss/ambient-css/grounded/)

Ambient CSS 的这次重写真正实现了“physically based”：ambient.css 中的每个系数都由 Blender Cycles 对等效物理场景的渲染测量拟合而来，并以“左侧实时 CSS、右侧 Blender 基准”的对照作为真实标准；文章逐项说明了表面、倒角、圆角、抬升、厚度、凹槽、曲面及其他材质的建模方法，也坦率记录了某些 CSS 效果在屏幕光栅化后偏离基准、以及部分指标无法被测量而只能目视调校的情况。

- 🌍 核心原则：CSS 中的光照曝光模型在线性光下拟合，采用无截距的两参数公式 `0.6396·key + 0.5496·fill`，可在所有反照率下把亮度误差控制在 0.03 以内，因此只需一个 `.amb-surface` 类加 `--amb-albedo` 变量，而不是为每种色调单独建类。
- 🔬 验证装置统一：物理场景为毫米级平板、参考地面、经过校准的主光和补光，并让 CSS 与渲染使用同一套提取器测量，每次发布都会经过对照检查。
- 📐 Chamfer 倒角：两侧 band 的 alpha 呈仿射关系；45° 面即便 key=fill 也保留残余 band，边沿处理暗含材料厚度。
- 🔄 Fillet 圆角：高光集中在每单位宽度 1.5px 处，比倒角更柔和。
- 📏 Elevation 抬升：纸张厚度的薄片静止时像嵌入表面的贴花、不产生渲染；只有抬升后才通过顶部轮廓的投影显现，且高度越大阴影模糊越强、alpha 越淡。
- 🧱 Thickness 厚度：按钮尺度板材的阴影是“底部到顶部轮廓的扫掠投影”，呈楔形并包裹阴影侧边缘、给角落做斜接，而不是简单的偏移方块；四层叠加的 box-shadow 采样整个扫掠并产生向外淡出。
- 🕳️ Groove 凹槽：负空间槽的深度复用厚度语义；槽底与周围地面同材质但曝光略高，受光侧墙会在槽底投下清晰阴影带，远墙则反射主光形成柔和提亮——这正是经典内嵌高光的物理来源。
- 🍥 曲面：柱面碟与穹顶的渐变只绘制着色部分，色调继续使用面板自身的 `--amb-albedo`；末端渐变增量与光照对比度呈仿射关系。
- 🎨 其他材质：不同反射率只是同一个 `.amb-surface` 配上不同的 `--amb-albedo`；5 种反照率、54 帧渲染全部由同一曝光定律复现，误差小于 0.03 亮度点；Lambertian 表面亮度上限接近反照率 1.0，所以浅色板之间比深色梯级更接近。
- ✨ Shiny 光泽：以产品摄影式的白色摄影棚环境为基底，包含头顶柔光箱、中性墙面和较暗地面；镜面反射包含掠射 Fresnel 边缘、主光在约 30% 处的镜像带，以及柔光箱和地面反射的软渐变。
- 🔩 拉丝、旋纹与喷砂金属：这类材质不是简单渐变，而是用噪声高度场做凹凸映射的微观起伏材质；CSS 侧用一对 SVG 噪声贴图（screen + multiply 沿光向反向偏移）求方向导数来模拟浮雕，并另外用渐变表现光泽。
- ⚖️ 反照率独立拟合：拉丝与旋纹的参考反照率分别为 0.4819 和 0.4795，相差不到 0.5%，从而验证了“同一种反射率、两种加工表面”的说法；喷砂则重新接地为珠击铝材，反照率 0.4457，与前两者相差约 8%。
- 🧹 喷砂材质的重要修正：该材质原本由旧 `.amb-mat-rubber` 改名而来且未重新接地，曾错误地停留在 0.0594 的深色电介质状态；现作为导体建模后，颗粒目标从 1.27 大幅升到 11.74 RMS L*。CSS 的叠加透明度在 1.0 处饱和而无法达到目标，因此以 0.666 发布，约为目标的 52%；0.666 是永不触碰饱和上限的最大 alpha，剩余差距记录在 `blasted.md` 中。
- ⚠️ 拉丝各向异性的光栅化教训：CSS 端原本按 rig 匹配为 7.60，但实际 Chrome 光栅化后只测到 1.55，几乎各向同性；原因是噪声图案要求每 CSS 像素 20 个湍流周期，而 `feTurbulence` 按设备分辨率栅格化，导致屏幕看到的只是无方向的混叠。修复后重新调整为细长条纹，现测得 12.15，是有意选择的过冲而不是偶然。
- 🔍 关键洞察：问题不在频率过高，而在“每像素整数个周期”——这会让噪声格点与采样网格重合，每个样本都落在格点上，而梯度噪声格点处严格为零，因此贴图比规格更弱、更不具方向性；闭环 CSS 拟合必须在真实发布环境、多种 devicePixelRatio 下测量。
- 🛠️ 光泽振幅是装置无法测量的指标：校准相机为正交投影，平行视线反射到环境中的同一点，无法形成宽位置高光；24 次渲染的低频起伏最高仅 1.04，而参考照片为 16.2，去掉凹凸后更是精确为 0.00。因此光泽振幅只能对照参考图目视拟合，并刻意按量拆分接地：浮雕幅度和各向异性来自渲染装置，扫掠幅度和颗粒形状靠人工判断。
- 🎯 拉丝光泽带的位置确实可以通过装置接地：它能随光源移动，只是速率与 CSS 假设不同；带宽和旋纹的整体锥形瓣仍为手调。此前认为“旋纹缺少方向性是经过验证的结果”这一说法已被撤回，因为正交相机论证对两种表面都成立，拉丝能测出峰值是依赖扰动法线，而旋纹的径向纹理没有对应机制。
- 💡 Glow 辉光：光晕半径直接来自发光板经测量得到的泛光衰减曲线；lume 颜色的明暗切换则是在此之上叠加的设计语义。

---

### [](https://kikkupico.github.io/ambientcss/guide/concept/)

**原文标题**: [Concept | Ambient CSS](https://kikkupico.github.io/ambientcss/guide/concept/)

文章針對傳統 CSS 陰影系統提出另一種方法：與其為每個元件手動挑選 shadow-sm/lg 數值，不如先定義整體照明環境（光源位置、強度、高度），讓陰影、高光和表面漸層從同一套參數自然產生。以下為重點摘要。

- 💡 傳統 shadow 體系缺乏光源概念，陰影只是裝飾；Ambient CSS 改以環境光照型塑一致性深度。
- 🔦 元件被視為平面 UI，以正投影模擬立體感，深度來自打光與邊緣處理。
- 🎛️ 所有元素共用同一組 CSS 自訂屬性，如 --amb-light-x/y、key/fill 光強度、色相與飽和度，修改即可同步更新場景。
- ☀️ 採用雙光源：主光（key light）負責主要高光與深影，補光（fill light）提亮暗部；兩者強度比例決定整體對比。
- 📦 `ambient` class 產生五層 box-shadow：外投影、內部邊緣高光/陰影、斜面高光/陰影，全由光源參數驅動。
- 🧱 Surface grammar 整合四層語法：Structure（ambient）、Surface（flat/concave/convex）、Edge（chamfer/fillet）、Depth（elevation-0 至 3），可任意組合並保持一致。
- 📐 這套模型讓「高起、凹陷、受光、背光」有共通規則，協助設計系統表現出更多空間語意。

---

### [](https://kikkupico.github.io/ambientcss/)

**原文标题**: [Ambient CSS](https://kikkupico.github.io/ambientcss/)

Ambient CSS 是一个轻量级设计系统，分为 CSS 工具包和 React 组件包，通过模拟正面硬件设备的双光源照明效果，实现风格统一、具有立体感的 UI 控件与面板，并提供文档、演示和开源仓库。

- 💡 Ambient CSS 由两个包组成：`@ambientcss/css` 提供光照基础与工具类，`@ambientcss/components` 提供基于这些基础的 React 控件。
- 🎛️ 将 UI 视为正面视角的物理硬件，深度靠阴影而非透视表现，整体采用正交前视图。
- 🔦 使用方向光（`lightX`、`lightY`）统一控制所有控件的高光与阴影方向，保证视觉一致性。
- ⚖️ 通过调节主光与补光的强度平衡，可呈现从柔和磨砂到高对比工业风的不同质感。
- 🕹️ 可构建硬件风格的按钮、开关、混音器式旋钮、滑杆、推子以及随光照方向变化的面板和表面。
- 🧭 文档入口：从「Guide > Getting Started」开始，用「Guide > Concept」理解光照/阴影模型，组件与 CSS 页面分别查看属性、示例和工具类配方。
- 🔗 快速链接：演示应用及 GitHub 开源仓库可供直接体验与参考。

---

### [](https://www.zachleat.com/web/speedlify2/)

**原文标题**: [Use Speedlify2 to Continuously Measure Website Performance—zachleat.com](https://www.zachleat.com/web/speedlify2/)

overview summary  
- 🚀 Speedlify2 是原 Speedlify 的重大升级，用于持续测量網站性能，現已測量 1565 個網站，無需手動操作。  
- ⚙️ 測量改為小批次並行處理，與排名解耦；每次建置時取最新數據排名，更穩健且可自動部署至 GitHub Pages。  
- 📊 新增 Core Web Vitals 現場資料與更詳細的 Axe CLI 無障礙檢測，並提供新版 `<speedlify2-score>` 元件及向後兼容舊版 API。  
- 🏆 分數全綠的優秀網站會特別標示，表現不佳者僅在溢位清單隨機顯示，避免對個人網站造成負面標籤；企業類別則會公開低分以問責。  
- 🖼️ 新增 No-JavaScript 與啟用 JavaScript 的截圖比對，可視化呈現差異，有助於發現 CSR、暗色模式錯誤或版面位移等問題。  
- 👑 新增「Perfect Site of the Day」隨機選出滿分網站，且類別不再互斥，單一測量可跨類別重複使用以節省流量。  
- 💤 已移出 showcase 的網站會自動列入未排名的 Emeritus 類別，目前回填了 92 個站點。  
- ✍️ 作者 Zach Leatherman 持續維護 Eleventy/Build Awesome，並將整個服務以靜態方式建置，提升效率並降低維護成本。

---

### [](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

overview summary  
Eleventy（又稱 11ty）是一個簡單、高效且靈活的靜態網站生成器，強調快速建置、極低客戶端 JavaScript、零追蹤與零設定起步，支援多種模板語言，可與既有專案結構整合，並擁有活躍社群與長期穩定性，適合從小型部落格到大型企業網站使用。

- ⚡️ 效能卓越：建置 4000 個 Markdown 檔案僅需 1.93 秒，遠快於 Astro、Gatsby、Next.js 等工具。  
- 🚀 快速起步：需 Node.js 18+，建立 index.md 後執行 `npx @11ty/eleventy --serve`，即可在本機預覽網站。  
- 📦 自動輸出：目前目錄中符合副檔名的檔案會自動編譯至 `_site` 資料夾。  
- 🧩 多模板支援：可使用 HTML、Markdown、WebC、JavaScript、Liquid、Nunjucks、Handlebars、EJS、Pug、TypeScript、JSX、Sass 等，甚至混合使用。  
- 🛡️ 零追蹤與零遙測：不收集使用者資料，也無需手動退出數據收集。  
- 🌱 零設定與彈性擴充：預設即可運作，同時提供設定檔與外掛機制以便擴展。  
- 📁 尊重專案結構：不需強制使用特定目錄，可逐步採用，僅處理指定檔案或忽略特定檔案。  
- 🧱 不綁定前端框架：預設零客戶端 JavaScript，利於漸進增強與長期維護。  
- 🏭 生產環境可靠：受 NASA、CERN、Google、Microsoft、Mozilla、Font Awesome 等組織採用。  
- 📈 下載量與社群：已超過 2000 萬次下載、88,000+ GitHub 儲存庫使用，具備活躍且友善的社群。  
- 🎯 穩定版本：自 2017 年以來歷經 226 次釋出，僅少數需開發者調整，長期依賴安全。  
- 💬 開發者好評：Mina Markham、Lea Verou、Addy Osmani、Mathias Bynens 等知名開發者皆公開推薦。  
- 🏆 獎項肯定：2022 年 Google Open Source Peer Bonus 得主、Product Hunt 當日產品第一名。  
- 📚 豐富文件與資源：提供教學、快速提示、外掛、部署服務、範例專案等完整指南。  
- 🔧 獨立模板語言：內容與工具解耦，日後轉換語法或遷移更容易。  
- 🖼️ 實際案例眾多：包括 developer.chrome.com、v8.dev、a11yproject.com、eslint.org、freecodecamp.org 等知名網站。

---

### [问卷与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=email)

SurveyJS 是一套開源、可自託管的 JavaScript 前端表單與問卷管理工具，提供表單建立、發佈、資料收集與視覺化等完整功能，讓開發者能完全掌控資料，不受第三方 SaaS 平台限制。

- 📦 **四大核心元件**：Form Library（動態表單渲染）、Survey Creator（拖曳式表單建構器）、Dashboard（互動式圖表與數據視覺化）、PDF Generator（表單匯出為 PDF）。
- ♿ **無障礙與標準合規**：表單與建構器符合 WCAG、Section 508 與 ARIA 標準，並以 Axe® 驗證，支援鍵盤與螢幕閱讀器。
- ∞ **無限使用無上限**：管理員、受訪者、表單數量、每月提交次數、檔案上傳與功能皆無限制，所有資料儲存於自有資料庫。
- 🔧 **高度自訂與擴充性**：可自訂題型、複合問題，或整合 Angular、React、Vue 3 元件；也支援自訂資料驗證與伺服器端檢查。
- 📴 **離線資料收集**：支援離線建立與填寫表單，恢復連線後自動同步資料與更新，實現 local-first 體驗。
- 💰 **一次付費永久授權**：開發者授權為單次購買，可永久使用；前 12 個月包含免費維護與支援，之後可選購續約。
- 🔓 **完全開源**：所有程式庫皆為開放原始碼，支援 React、Angular、Vue 3 與 Vanilla JS，可自行修改整合。
- 🎨 **白標與主題化**：內建設計權杖與主題，可搭配 Bootstrap、Material UI、shadcn/ui 等設計系統，打造一致化品牌介面。
- 🤖 **AI 輔助建表**：可透過 API 整合生成式 AI，輸入自然語言即可產生結構化表單與 JSON schema。
- 🏢 **多產業適用**：涵蓋保險、醫療、市場研究、教育、人資、電商、客戶體驗、非營利與銀行等敏感資料收集場景。
- 🔒 **資料安全與自託管**：採用自架方式可確保匿名性與隱私，符合 HIPAA、FERPA、GDPR 等法規，完全掌控伺服器與用戶端資料流。
- ❓ **常見問題重點**：授權指開發者、無使用限制、僅提供前端 UI 需自建後端、授權可指派給團隊成員並於 License Manager 管理。

---

### [](https://github.com/GoogleChromeLabs/quicklink)

**原文标题**: [GitHub - GoogleChromeLabs/quicklink: ⚡️Faster subsequent page-loads by prefetching in-viewport links during idle time · GitHub](https://github.com/GoogleChromeLabs/quicklink)

Quicklink 是 GoogleChromeLabs 发布的一个轻量级开源库，旨在通过预取或预渲染用户视口内的链接来显著加速后续页面加载。它利用浏览器空闲时间智能检测可见链接，体积不足 2KB，支持多页面应用和 React 单页应用，并提供丰富的配置与扩展选项。

- ⚡️ 核心机制：使用 Intersection Observer 检测当前视口内的链接，并在浏览器空闲时通过 requestIdleCallback 自动预取或预渲染这些 URL。
- 🚦 智能降级：通过 navigator.connection 检查用户是否处于慢速连接或开启了 Data Saver，从而避免在不良网络条件下浪费流量。
- 🖥️ 预取与预渲染：默认采用 `<link rel=prefetch>` 或 XHR 预取，也支持 Speculation Rules API 进行预渲染；设置 priority 后可使用 fetch() 提升请求优先级。
- 📏 极简体积：压缩并 gzip 后小于 2KB，是面向多页面站点的“即插即用”型性能优化方案。
- 🛠️ 安装与使用：支持 npm 或 unpkg CDN 引入，执行 `quicklink.listen()` 即可自动监听视口链接；也可在 `load` 事件后初始化。
- ⚛️ React 支持：提供 `withQuicklink()` HOC，可结合 webpack-route-manifest 在单页应用中预取路由级 JavaScript 块。
- 🔧 灵活 API：`listen()` 支持 delay、el、limit、threshold、throttle、timeout、origins、ignores、priority、hrefFn、onError 等参数；另有 `prefetch()` 和 `prerender()` 允许编程式预取或预渲染指定 URL。
- 🌐 浏览器兼容：核心需要 IntersectionObserver，支持 Chrome、Firefox、Safari 12.1+ 等现代浏览器；搭配 Polyfill 可兼容 IE11 及更早版本。
- ⚠️ 注意事项：跨域预取可能遇到 CORS/CORB 和 session-stitching 问题；广告类网站应避免预取广告链接，可使用 ignores 规则过滤特定 URL、正则或 DOM 属性。
- 🔗 相关生态：受 Gatsby 启发；Guess.js 提供基于机器学习的预取；WordPress、Drupal、Magento 2 均有相应插件；instant.page 则提供更保守的鼠标悬停预取方案。

---

### [](https://particlecharts.com/)

**原文标题**: [Particle Charts — JavaScript charts made of light](https://particlecharts.com/)

Particle Charts 是一个零依赖的 JavaScript 图表库，将数据渲染成动态粒子云，支持条形图、折线图、气泡图、雷达图、饼图和环形图等多种类型。所有图表共用同一粒子引擎，只需纯 JSON 配置即可生成响应式、可访问且具有发光效果的交互图表。

- 📊 支持条形、折线、气泡、雷达、饼图和环形图六种类型，每种都有对应简写配置
- ✨ 所有图表基于同一套粒子系统，仅通过不同排列方式呈现
- 🖱️ 悬停时自动显示工具提示与十字线，图例支持键盘切换系列显示
- 📦 零依赖，单文件即可运行，无需构建步骤，支持 CDN 和 npm 两种引入方式
- 📥 数据采用纯 JSON，接受数字数组、`{label, value}` 记录、多系列对象或 `{x, y}` 点集
- 💫 粒子通过离屏层累加合成并两次模糊形成真实辉光效果
- 🎛️ 提供丰富的粒子控制选项：大小、密度、抖动、速度、形状、透明度等
- 📐 坐标轴、刻度、网格和图例自动生成，并自动处理标签稀疏和边距
- ♿ 内置屏幕阅读器数据表格，支持 `prefers-reduced-motion`，滚出视口时自动暂停
- 🚀 快速上手：容器指定高度后三行代码即可创建图表，支持实时更新与配置
- 🎨 主题可切换明暗，并支持自定义颜色、字体、轴范围、曲线类型等多项配置
- 🧩 提供 `update`、`setOptions`、`resize`、`toDataURL` 和 `destroy` 等便捷方法

---

### [首页 | Cropper.js](https://fengyuanchen.github.io/cropperjs/)

**原文标题**: [Home | Cropper.js](https://fengyuanchen.github.io/cropperjs/)

该工具主打可定制性，让用户能轻松打造属于自己的图像裁剪器。

- ✂️ 高度可定制：支持按需自定义裁剪器的各项功能与样式  
- ⚡️ 简单易用：定制过程轻松便捷，无需复杂操作

---

### [游乐场 | Cropper.js](https://fengyuanchen.github.io/cropperjs/playground.html)

**原文标题**: [Playground | Cropper.js](https://fengyuanchen.github.io/cropperjs/playground.html)

本文档为 Vue 官方中文站点的导航与版本信息概览，涵盖指南、API、示例等核心入口，并支持多语言切换。

- 🔍 提供站内搜索功能，便于快速查找文档
- 🧭 主导航包含指南、API、Playground、示例等核心模块
- 👋 设有“Hello World”快速上手示例
- 📦 展示当前版本及更新日志（2.2.0），支持旧版（1.x）切换
- 🤝 提供贡献指南与迁移说明
- 🌐 支持中英文界面切换及外观主题调整

---

### [](https://github.com/fengyuanchen/cropperjs)

**原文标题**: [GitHub - fengyuanchen/cropperjs: JavaScript image cropper. · GitHub](https://github.com/fengyuanchen/cropperjs)

Cropper.js 是一个基于 JavaScript 的图像裁剪器库，当前页面展示的是 v2.x 分支的内容。该项目在 GitHub 上拥有较高关注度，采用 MIT 许可证，提供丰富的框架封装和生态支持，并遵循规范的版本管理与提交约定。

- 📦 Cropper.js 是一个 JavaScript 图像裁剪器，支持图像的裁剪与处理。
- 🌿 当前为 v2.x 分支，v1.x 分支仍然可访问。
- ⭐ GitHub 上获得约 13.9k star、2.4k fork、166 watchers。
- 🌐 官方演示与文档网站位于 fengyuanchen.github.io/cropperjs/。
- 📐 版本管理遵循语义化版本（Semantic Versioning），Git 提交遵循 Conventional Commits 规范。
- 📜 采用 MIT 许可证，作者为 Chen Fengyuan。
- 🔧 仓库包含 docs、packages、types 等核心目录，以及 rollup、jest、lerna 等工程化配置。
- 🔗 提供 Angular、React、Vue、Blazor 等多种框架的集成封装项目。
- 🏷️ 项目主题标签包括 cropper、cropperjs、image-cropper、image-processing、javascript。

---

### [](https://contemporary-home-computing.org/prof-dr-style/)

**原文标题**: [Prof. Dr. Style](https://contemporary-home-computing.org/prof-dr-style/)

overview summary
本文回顾了 1993 年前后万维网早期的真实设计风格，以“Prof. Dr. Style”为例，探讨了由学者、非专业网页作者创造的原始且统一的页面美学。这种风格植根于浏览器作为编辑器和“最终用户即设计者”的理念，体现了用户对网页外观的高度自主权。文章还追溯了这种风格如何随浏览器演进逐步变异，并指出其对理解当代超文本衰落与独立网络文化的重要意义。

- 🧑‍🏫 “Prof. Dr.”是搜索早期网页风格的暗号，因最早的网页多出自大学学者之手，其页面至今保留着 1993 年的原始形态。
- 📜 真正的早期网页以“原始且千篇一律”著称：浏览器默认样式、纯 HTML 标记、几乎无视觉定制，反映了“用户即设计者”的早期信念。
- 🌐 早期浏览器（如 Mosaic）允许用户自行设定全局颜色与字体，每个用户都能决定整个互联网的观感，这是“偏好自由”的巅峰。
- 🔄 当网页走向大众后，浏览器逐渐剥夺用户定制权，转而让作者控制外观，Netscape 和 CSS 的普及终结了这种共享设计范式。
- ✏️ Prof. Dr.风格并非纯复古，页面常更新课程与科研信息，却能完美运行在 Mosaic 1.0 中，兼具“当代性”与“历史感”。
- 💻 许多学者用文本编辑器或 Word 制作页面，错误使用`<pre>`、`<font>`等标签，无意中形成了一种独特的非专业编码视觉语言。
- 🎨 从修改链接默认颜色开始，学者们逐渐尝试改变背景色、背景图、字体、项目符号、水平线和动画 GIF，一步步走向“业余网页”的怀抱。
- 🖼️ 背景图案常暗示研究领域，如大气化学家用云朵、天体物理家用星空，展示了形式与内容的偶然统一。
- 🧩 表格布局、嵌套框架、导航菜单陷阱等早期网页常见手法，也大量出现在 Prof. Dr.页面中，构成了一部活生生的网页设计演变史。
- 🏛️ Prof. Dr.页面传递的核心信息是“独立性”：不随波逐流于大学品牌或内容管理系统，是学者对体制化网络空间的无声反抗。
- 🔗 当代超文本已衰落：链接常是“僵尸链接”，点击后仍指向同一页；浏览器更像操作系统，页面隐喻被应用界面吞噬。
- 💡 这些手工制作的链接和页面，是真正的“网络国家公园”，为后代保留了关于自由、信任与网络早期乌托邦的珍贵体验。

---

### [获取失败](https://www.webdesignmuseum.org/all-websites)

**原文标题**: [Failed to retrieve](https://www.webdesignmuseum.org/all-websites)

无法总结：获取内容失败，状态码 403。

---

