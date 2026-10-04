### [](https://github.com/fluttersdk/wind/releases?ref=tailwindweekly.com)

**原文标题**: [Releases · fluttersdk/wind · GitHub](https://github.com/fluttersdk/wind/releases?ref=tailwindweekly.com)

fluttersdk/wind 发布页显示该公开仓库有 39 stars、2 forks、0 issues/PR，最新版本为 1.8.0；版本列表覆盖 1.5.1 到 1.8.0，主要围绕性能诊断、焦点与键盘可访问性、颜色与透明色修复、布局渲染优化，以及 WSelect/WInput 行为修复。

- 📦 1.8.0（最新）：新增 WAnchor.trackFocus 与性能计数器 widgetBuilds、wrapperEmissions、inheritedReads；recordInheritedRead 改用枚举；调试/性能 resolver 扩展到非 release 构建；WDiv 改用基础组件构建并减少 MediaQuery 重建。
- 🎨 1.7.0：新增 contrastRatio 和 contrastForeground，用于按 WCAG 计算对比度并选择前景色。
- 🧩 1.6.4：修复圆角、带边框、overflow-hidden 盒子裁剪时角部边框消失的问题。
- 🩹 1.6.3：修复 transparent 色值从未解析；修正 WButton/WCheckbox/WSelect 因此受到的影响；规范 ring/shadow 与 bg/text/decoration/渐变的 hex 颜色位数和 alpha 支持。
- ⌨️ 1.6.2：修复聚焦 WInput 在路由过渡期间因 RenderBox 未布局而崩溃，改为不依赖像素对齐的 caret 计算。
- 🌗 1.6.1：让 ThemeData.scaffoldBackgroundColor 与 bg-surface 别名一致，避免页面背景色错误，尤其暗色模式。
- 📄 1.6.0：新增 WSelect.onOpen；重写 README；修复多行 WInput 键盘遮挡和工具栏遮挡；修复 WSelect 重开后的异步响应、加载状态与分页问题；改进圆角裁剪抗锯齿。
- ♿ 1.5.3：WAnchor 支持键盘/遥控器激活；新增 hasPrimaryFocus；修复焦点环、遍历停靠和禁用状态继承。
- 📐 1.5.2：修复 max-h/max-w 对 h-full 无效；h-full 改为渲染层 WindFullHeightBox，支持 IntrinsicHeight，并减少 LayoutBuilder 开销。
- 🔤 1.5.1：修复 capitalize 只大写首字母；WText 的 uppercase/lowercase/capitalize 改为 locale-aware；链接检查接受 429 和 5xx。
- 🧪 质量与维护：多个版本补充测试、文档和技能说明；链路检查、性能统计和布局行为被持续加固。

---

### [浏览粒子 - coss ui](https://coss.com/ui/particles?ref=tailwindweekly.com)

**原文标题**: [Browse Particles - coss ui](https://coss.com/ui/particles?ref=tailwindweekly.com)

这是 coss.com UI 的 Particles 浏览页，用于发现 510 个可直接使用的设计系统基础组件，并支持按分类筛选，页面还包含导航、文档、搜索和主题切换等功能。

- 🧭 顶部导航可切换 coss.com、UI、Docs、Particles
- 🔎 提供 ⌘K 快捷搜索入口
- 🌗 支持明暗主题切换
- 🧱 包含 510 个即用型 Particles，作为设计系统构建块
- 🗂️ 可按类别筛选，快速找到项目所需组件
- 🔢 页面显示 10.6k，可能为数量或热度指标

---

### [](https://animateicons.in/?ref=tailwindweekly.com)

**原文标题**: [AnimateIcons | 1170+ Free Animated React Icons](https://animateicons.in/?ref=tailwindweekly.com)

AnimateIcons 是专为 React 打造的开源动画 SVG 图标库，共 1170 个图标，涵盖 Lucide 与 Huge 两种风格；组件可直接嵌入，支持悬停、聚焦或自定义代码触发动画，并便于搜索、调参、复制和集成到真实界面。

- 🎯 提供 1170 个开源动画 SVG 图标，面向 React，包含 Lucide 和 Huge 两种风格。
- 🧩 图标为即插即用组件，可在悬停、聚焦或由自有代码触发时播放动画。
- 📦 支持 `npm install @animateicons/react` 安装，也可用 `npx shadcn@latest add @animateicons/lu-x` 添加 shadcn 组件。
- 🔎 可按键搜索全部 1170 个图标，搜索结果悬停即可预览动画，如 heart、cart、lock、camera。
- 🎛️ 可复制并调整图标，支持设置尺寸、颜色、时长，并提供复制、重播、重置等操作。
- 🌀 Lucide 含 669 个极简精准图标；Huge 含 501 个大胆表现力图标，共用同一套动效系统。
- 🛠️ 面向真实界面，可放入工具栏、播放器、购物车、产品卡和点赞按钮等场景。

---

### [](https://www.cozywatch.com/?ref=tailwindweekly.com&aff=lVeE1)

**原文标题**: [Cozy Watch - Clear GitHub Notifications for macOS](https://www.cozywatch.com/?ref=tailwindweekly.com&aff=lVeE1)

Cozy Watch 是一款开源、MIT 许可的 macOS GitHub 通知与 PR 管理工具，帮助过滤 GitHub 邮箱和动态噪音，只在 PR、评审、提及或 CI 结果真正需要你时提醒，让你保持专注并快速采取下一步。

- 🔔 只提示真正需要关注的 GitHub 动态：PR、评审、提及和 CI 更新。
- 🍎 支持 macOS 12 Monterey 或更高版本，可从官网下载。
- 🧘 在需要时给出清晰下一步，其余时间保持安静、不打扰。
- 📌 通过菜单栏和 Cozy Watch 应用快速查看当前 PR 状态。
- 🔐 开源、默认隐私优先，可随时查看源码；采用 MIT 许可证。
- 🆓 个人使用 $0 永久免费，包含全部功能、无限仓库、所有通知类型和免费更新。
- 💼 商业使用（工作、客户项目、企业、非营利）为 $29/年，含 30 天商业试用和许可证管理。
- 🧾 商业许可证通过 Lemon Squeezy 安全销售。
- 🚀 更新透明：0.8.6 改进包括保留 PR 缓存、修复超 2000 仓库的 ENOTFOUND DNS 错误和仓库选择缓慢，并迁移至 GitHub App。
- 📬 可订阅 newsletter 获取偶发更新，避免 GitHub 噪音与垃圾邮件。

---

### [](https://www.cozywatch.com/download/?ref=tailwindweekly.com&aff=lVeE1)

**原文标题**: [Download | Cozy Watch](https://www.cozywatch.com/download/?ref=tailwindweekly.com&aff=lVeE1)

Cozy Watch 是一款 macOS 桌面应用，旨在以更轻松的方式跟踪 GitHub 拉取请求、评审、提及和 CI 更新，避免频繁陷入 GitHub 收件箱。官网提供下载、定价、更新日志、GitHub App、源码等入口。

- 🖥️ 支持 macOS 12 Monterey 或更高版本，提供 Apple Universal 版本下载。
- 💵 采用商业许可证，按年收费 29 美元。
- 🔔 让你随时掌握拉取请求、评审、提及和 CI 更新，而不必一直查看 GitHub 收件箱。
- ⬇️ 可下载最新版、浏览所有版本，并查看 GitHub 源码。
- 📰 可加入新闻通讯，了解 Cozy Watch 最新动态。
- 🔗 网站包含首页、关于、下载、源码、GitHub App、路线图、EULA、条款、隐私政策、更新日志、博客、联盟计划、招聘等页面。
- 🐦 社交媒体账号为 @cozy_watch。
- 🧩 开源项目，采用 MIT 许可证，并标注“Made in a cozy armchair”。

---

### [深入剖析 StyleX](https://flaviocopes.com/stylex/?ref=tailwindweekly.com)

**原文标题**: [A deep dive into StyleX](https://flaviocopes.com/stylex/?ref=tailwindweekly.com)

StyleX 是 Meta 开发的 JavaScript 样式语法与编译器，构建时把类型化 JS 样式对象编译为去重后的原子 CSS 类，浏览器只收到普通 CSS，生产环境没有运行时样式注入。文章从问题模型、React/Vite 与 Astro 配置、核心 API、组合与变体、响应式、主题、动画、静态约束、Lint、编码代理价值、成本与方案对比、适用场景和生产构建等方面全面讲解 StyleX。

- 🧠 StyleX 写作体验像 CSS-in-JS，但构建产物是普通 CSS 文件和哈希类名。
- 🧱 它主要解决大型应用中的类名冲突、作用域、删除安全、覆盖来源、共享组件定制和未使用 CSS 等问题。
- 🧩 核心心智模型：样式对象 → StyleX 编译器 → 可复用原子类名与常规 CSS → 浏览器按普通 CSS 应用。
- ⚙️ React + Vite 设置需安装 `@stylexjs/stylex` 和 `@stylexjs/unplugin`，并在 `vite.config.ts` 中把 `stylex.vite()` 放在 `react()` 前。
- 🧪 核心工作流是用 `stylex.create()` 定义命名样式组，再用 `stylex.props()` 展开并应用 `className` 和 `style`。
- 🔍 开发模式会生成 `data-style-src` 和可读标记类，配合 StyleX DevTools Chrome 扩展可追踪样式来源。
- 🚀 Astro 可复用同一套 StyleX Vite 插件，主要封装 React 组件；开发时需引入虚拟样式表和运行时，`.astro` 文件不能直接转换。
- 🧬 StyleX 生成原子 CSS：每个类通常只含一个声明，公共声明可去重复用，因此 HTML 类名更多但样式表增长更慢。
- 🧷 组合样式可避免特异性之争：`stylex.props(styles.a, styles.b)` 中后者在直接冲突时胜出，浏览器看到类名之前冲突已解决。
- 🎛️ 条件样式使用普通 JavaScript 的 `&&` 或三元表达式，`false`、`null`、`undefined` 会被忽略，且所有可能样式对编译器可见。
- 🏷️ 变体通过对象查找实现，例如用 `keyof typeof colorStyles` 限制 `primary`、`secondary`、`danger` 等值。
- 🖱️ 悬停、聚焦、激活等状态写在属性值内部，伪元素放在样式顶层，推荐使用 `:focus-visible` 等现代做法。
- 📱 响应式样式也写在属性内部，用默认值和媒体查询条件并列；同样支持 `@supports`、容器查询，并可与伪类组合。
- ⏱️ 动态值应少用：样式函数可处理运行时值，编译器生成静态类加 CSS 变量，并把具体值放入元素 `style` 属性。
- 🎨 设计令牌用 `stylex.defineVars()` 在 `.stylex.ts` 等文件中命名导出，组件引用类型化 CSS 变量，而不是硬编码值。
- 🌗 主题通过 `stylex.createTheme()` 覆盖变量组，在子树应用后，后代组件继续消费同一套语义令牌。
- 📦 父组件传入样式时，可用 `StyleXStyles` 类型接收 `style`，还可限制允许覆盖的属性，比不受限的 `className` 更安全。
- 🎞️ 动画用 `stylex.keyframes()` 定义关键帧，再在样式中引用，StyleX 会生成并引用最终关键帧名称。
- ⚛️ 可选 `@stylexjs/atoms` 包提供小型内联原子样式，适合一次性例外；可复用组件仍推荐命名样式。
- 🧱 静态约束要求样式对象不能任意执行 JS、使用导入的普通值或对象展开；共享值应用 `defineVars` 或 `defineConsts`。
- 🌐 全局 CSS 仍应保留给 reset、body 默认样式、字体和 CMS 原始 HTML；启用 CSS layers 时要注意未分层规则的优先级。
- ✅ `@stylexjs/eslint-plugin` 可校验样式、发现未使用样式、检查简写并限制属性值，把设计决策变成自动检查。
- 🤖 对编码代理而言，StyleX 约束了选择空间，减少随意值和不一致；Tailwind 更适合人类快速输入，但 StyleX 在代理大量写 UI 时更有优势。
- ⚖️ 成本包括配置更复杂、语法更冗长、生态大量基于 Tailwind，以及需要放弃部分全局样式和深层选择器模式。
- 🆚 对比纯 CSS、Tailwind、运行时 CSS-in-JS，StyleX 的优势是构建时原子 CSS 和可预测组合，代价是更严格的编译器与规则。
- 🧭 适合新 React 应用和成长中的组件库，尤其适合编码代理频繁修改组件的场景；不建议仅为跟风迁移小项目或静态内容站。
- 🚀 生产构建后检查 `dist/assets`，应看到带哈希的原子 CSS，不应在应用代码中看到原始 `stylex.create()` 对象。
- 📚 结论：StyleX 应被视为编译器与约束体系，而不是另一种 CSS 拼写方式；它不替代对布局、继承、响应式和可访问性的理解。

---

### [HTTP 缓存完全指南 - Jono Alderson](https://www.jonoalderson.com/performance/http-caching/?ref=tailwindweekly.com)

**原文标题**: [A complete guide to HTTP caching - Jono Alderson](https://www.jonoalderson.com/performance/http-caching/?ref=tailwindweekly.com)

HTTP 缓存是 Web 性能、韧性与成本控制的隐形基础设施；它贯穿浏览器、CDN、代理、反向代理、应用与数据库多层，既影响用户体验、SEO 和服务器负载，也影响 AI 爬虫、训练数据与代理助手对站点的理解。本文系统讲解 HTTP 缓存机制、头部、误区、实践配方、Cloudflare、调试方法与战略意义。

- ⚡ 缓存价值：降低延迟、提升韧性、节省成本、改善 SEO；命中率提升可直接减少源站请求与基础设施支出。
- 🧭 缓存是一个分层生态：浏览器内存/磁盘缓存、代理、共享缓存、CDN、反向代理、应用缓存、数据库缓存各有规则。
- 🔑 缓存键决定“哪些请求算同一个资源”：默认包含 scheme、host、path、query；浏览器还采用双键/三键缓存隔离站点与 iframe。
- 🧼 `Vary` 可把请求头纳入缓存键，但滥用 `Vary: Cookie`、`Vary: User-Agent`、`Vary: *` 会导致严重碎片化。
- 🧪 `No-Vary-Search` 等新机制尝试忽略 `utm_*` 等无关参数，减少缓存碎片，但目前支持有限。
- ⏳ 缓存核心权衡是“新鲜度”与“验证”：新鲜可直接返回，过期则需回源校验。
- 📅 `Date` 是服务器生成响应的时间戳，也是所有新鲜度与年龄计算的基线。
- 🛠️ `Cache-Control` 是最重要的响应头，包含 `max-age`、`s-maxage`、`immutable`、`stale-while-revalidate`、`stale-if-error`、`public`、`private`、`no-cache`、`no-store`、`must-revalidate` 等。
- 📨 请求侧 `Cache-Control` 也能影响缓存行为：`no-cache`、`no-store`、`only-if-cached`、`max-age`、`min-fresh`、`max-stale` 等。
- 🕰️ `Expires` 是旧的绝对过期时间；若同时存在 `Cache-Control: max-age`，则会被忽略，且易受时钟偏差影响。
- 🧾 `Pragma` 是 HTTP/1.0 遗留头，主要用 `Pragma: no-cache` 兼容老代理与旧系统。
- 📊 `Age` 表示响应在共享缓存中已存放多久；浏览器不会发送它，CDN/代理常用。
- 🏷️ `ETag` 与 `Last-Modified` 用于条件请求；强 ETag 表示字节级一致，弱 ETag 表示语义一致；`304 Not Modified` 可节省带宽。
- 🧮 新鲜度寿命优先级：`s-maxage`/`max-age` > `Expires` > 启发式；当前年龄由 `Date`、`Age` 与缓存驻留时间共同估算。
- 🌲 决策树：未过期直接命中；过期后可用 `stale-while-revalidate` 后台刷新、`stale-if-error` 源故障兜底，否则发起条件请求回源。
- ❌ 常见误区：`no-cache` 不是“不缓存”，而是“可存但每次复用前验证”；`no-store` 才是完全不存；`max-age=0` 不等于 `must-revalidate`。
- ⚠️ `s-maxage` 只作用于共享缓存并覆盖 `max-age`；`immutable` 只适合指纹化静态资源，别用于 HTML；重定向与错误响应也可能被缓存。
- 🧱 设备与地域拆分易造成碎片化：按原始 `User-Agent` 或 `Accept-Language` 缓存会爆炸，应归一化或使用 Client Hints + 受控 `Vary`。
- 📦 静态资源配方：`Cache-Control: public, max-age=31536000, immutable`，配合文件名指纹可长期缓存。
- 📰 HTML 配方：高频页面用短 `max-age` + `s-maxage` + `stale-while-revalidate` + `stale-if-error`；低频页面可用长 CDN TTL + 发布时按 Cache Tags 主动清除。
- 🔌 API 配方：`public, s-maxage=30, stale-while-revalidate=30, stale-if-error=300` + `ETag`，兼顾低延迟、低源站负载与韧性。
- 🔐 登录/用户页面配方：`private, no-cache` + `ETag`；敏感数据建议 `private, no-store`，避免本地泄露。
- 🖼️ 图片媒体配方：`public, max-age=86400`，配合 `Vary: Accept-Encoding, DPR, Width`，并规范 DPR/Width 防碎片化。
- 🌐 浏览器额外行为：BFCache 保存整页状态；硬刷新绕过缓存，软刷新仍可能用缓存；prefetch/preload/prerender 可预热缓存但不改缓存策略；SXG 增加签名过期与 Cookie 变体。
- ☁️ Cloudflare 实践：默认不缓存 HTML；Edge TTL 可与浏览器 TTL 分离；缓存键默认完整 URL，需规范化参数；支持设备/地理拆分与 Cache Tags。
- 🧩 其他缓存层：Redis/Memcached、Varnish/NGINX、Service Worker 都可能覆盖或绕过 HTTP 头，多层缓存容易失步。
- 🔍 调试方法：检查 `Cache-Control`、`Age`、`ETag`、`Expires`，以及 `X-Cache`、`cf-cache-status`、`Cache-Status`；用 DevTools 区分 memory/disk/network/304，并沿浏览器→CDN→代理→应用→数据库追踪。
- 🤖 AI 时代：缓存影响爬虫效率、训练数据新鲜度与一致性，也影响代理助手对站点速度与可靠性的判断；碎片化会污染机器理解。
- 🧠 结论：缓存不是优化技巧，而是基础架构与战略；需跨浏览器、CDN、代理、应用、数据库统一设计，兼顾性能、成本、韧性与机器可读性。
- 💬 评论区补充：`Pragma: no-cache` 仍可用于兼容；敏感页面优先 `private, no-store`；`stale-while-revalidate` 下 304 表示后台验证；Firefox 的 RCWN 会赛跑缓存与网络。

---

### [](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/?ref=tailwindweekly.com)

**原文标题**: [A Friendly Introduction to SVG • Josh W. Comeau](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/?ref=tailwindweekly.com)

overview summary
- 📌 本文是 SVG 入门指南，介绍 SVG 的核心概念、基础形状、viewBox、表现属性与描边动画，并说明它为何强大且适合用 CSS/JS 操作。
- 🖼️ SVG 是可缩放矢量图形，采用 XML 语法，既能像图片一样嵌入，也能直接内联到 HTML 中。
- ✨ 内联 SVG 的真正魔力在于它是 DOM 的一等公民，可用 CSS 和 JavaScript 选择、修改与动画化。
- 🎛️ 许多 SVG 属性（如 `fill`、`r`）也可当作 CSS 属性使用，因此能结合过渡和动画。
- 🔧 作者常手写 SVG；设计软件导出的 SVG 常合并成单个 `<path>`，不利于单独控制元素。
- 📐 基础形状包括 `<line>`、`<rect>`、`<circle>`、`<ellipse>`、`<polygon>`；几何属性负责定位，表现属性负责上色与描边。
- 📏 `<line>` 用 `x1/y1/x2/y2` 定义起终点，默认不可见，需要 `stroke` 和 `stroke-width` 才会绘制。
- ▭ `<rect>` 用 `x/y/width/height` 定位与定尺寸；描边画在路径中心；宽或高为 0 会成为退化形状而不渲染；`rx/ry` 可做圆角。
- ⭕ `<circle>` 用 `cx/cy/r`，`<ellipse>` 用 `cx/cy/rx/ry`；半径或尺寸为 0 时形状会消失。
- 🔺 `<polygon>` 用 `points` 定义多个点并自动闭合；正多边形需要三角函数计算顶点。
- 📝 SVG 中的逗号和换行属于“多余”但有效；在 gzip 压缩下不必为省字节牺牲可读性。
- 📦 `viewBox` 定义内部坐标系统，使 SVG 可响应式缩放；前两个值控制视图位置，后两个值控制缩放范围。
- ♾️ SVG 理论上无限延伸，`viewBox` 决定查看哪一部分；实际使用中通常保持 `viewBox` 静态以便复用。
- 🔍 矢量图由数学指令构成，任意放大仍清晰，不像 JPG/PNG 会像素化。
- 🖌️ 表现属性控制 `fill` 与 `stroke`；`stroke` 支持 `stroke-width`、`stroke-dasharray`、`stroke-linecap`，并且可用 CSS 动画。
- 🏃 `stroke-dashoffset` 可制作跑马灯、加载 spinner 和“自绘制”动画；可用 `getTotalLength()` 或 `pathLength` 处理路径长度。
- 🧭 本文未深入覆盖 `<path>` 元素；它能用贝塞尔曲线和弧线 DSL 绘制复杂图形，另有专门教程。
- 🎓 作者希望提供 SVG 基础与实用技巧，并推广其关于 whimsical 动画的课程。

---

### [Bruno - Git 原生 API 客户端](https://www.usebruno.com/?ref=tailwindweekly.com)

**原文标题**: [Bruno - The Git-Native API Client](https://www.usebruno.com/?ref=tailwindweekly.com)

Bruno 是一款“Git 原生”的开源 API 客户端，主张把 API 集合当作代码来管理：集合以纯文本文件形式存放在项目仓库中，与 Git、IDE 及 AI 代理无缝协作，完全本地运行、无需账号与云同步。它定位为臃肿且被云锁定的“平台型”工具的挑战者，强调开发者优先、可扩展、隐私安全与企业级能力，已获得 400 万用户、46K stars 和 500+ 贡献者，并被大量团队从 Postman、Insomnia 迁移采用。

- 🐶 核心理念：集合即代码——所有 API 集合都是仓库中的纯文本文件，其余能力由此自然衍生
- 🧩 开发者优先：不是平台而是 API 客户端，可与现有技术栈协作而非对抗
- 📄 基于 OpenCollection 开放标准，采用人类可读、diff 友好的 YAML 格式
- ⌨️ 可在 IDE、终端和 AI 代理中运行，支持导入 Postman 集合与环境
- 🔀 协作靠 Git：文件夹与文本文件随代码共置，用分支、diff、评审、合并完成协作
- 🔒 安全本地：无云同步、无账号、无登录，数据永不离开本机，零可见性且不用于训练 AI
- ✅ 通过 SOC 2 Type II 独立审计
- 🏢 企业就绪：运行在既有安全边界内，无云租户、无新管理台、无新增攻击面
- 🛡️ 自动继承设备与 MDM 策略、Git 仓库权限、VPN/代理/防火墙规则及数据驻留要求
- 🔑 内置 SSO/SAML、SCIM 供给与角色映射，以及 Vault、Azure Key Vault、AWS 密钥管理
- 📈 社区规模：400 万用户、46K GitHub stars、500+ 贡献者
- 💬 用户普遍称赞轻量、启动快、低内存占用，UI/UX 与搜索（Ctrl+K）体验佳
- 🚀 大量用户从 Postman/Insomnia 迁移，主因是免费、离线、Git 友好与无按用户授权费
- 🧪 支持 pre-request/post-request 脚本、测试、变量与可复用 JS 工具函数
- 🌐 支持 WebSocket、gRPC、GraphQL、OpenAPI 同步与 SPARQL 查询
- 🤖 AI 代理友好：.bru 文件便于 Claude 等工具生成、批量创建请求并搭建环境
- 🖥️ 跨平台（macOS、Windows、Linux），提供 CLI、内置终端、工作区与免费请求历史
- 🎁 免费开源，无需账号，一分钟内即可在本地跑起自己的 API 工作流
- ❓ 提供常见问题解答，涵盖数据同步、协作方式、支持计划、企业协议与 SSO/RBAC

---

### [错误](https://www.ogimagecn.com/?ref=tailwindweekly.com)

**原文标题**: [Error](https://www.ogimagecn.com/?ref=tailwindweekly.com)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='www.ogimagecn.com', port=443): Read timed out. (read timeout=30)

---

### [tiiny.host - 在线分享作品的最简单方式](https://tiiny.host/?fpr=vivian32&ref=tailwindweekly.com)

**原文标题**: [tiiny.host - The simplest way to share your work online](https://tiiny.host/?fpr=vivian32&ref=tailwindweekly.com)

概览总结
- ⚠️ 您尚未提供需要总结的正文内容，因此暂时无法生成摘要。
- 📝 请将文章或文本粘贴发送，我会按“- 表情符号 要点”的格式输出中文总结。

---

### [Blip – 发送文件的最快方式](https://blip.net/?ref=tailwindweekly.com)

**原文标题**: [Blip â The fastest way to send files](https://blip.net/?ref=tailwindweekly.com)

overview summary
Blip 是一款跨平台、极速、直连的文件传输应用，支持任意大小文件和文件夹，无需上传/下载两步，具备断点续传、LAN 加速和端到端加密；非商业用途免费、无广告，适合创作者全球协作。

- 🚀 一键直传：从桌面直接发送，无需先上传再下载，速度可至少快一倍。
- 📁 无大小限制：支持 99TB 乃至无限大小文件；文件夹无需压缩即可发送。
- 🔄 断点续传：网络中断、硬盘拔出、磁盘满等情况后仍可恢复进度。
- 💻 原生轻量：有 Windows、Mac、Android、iPhone/iPad、Linux 应用，省电且不占资源。
- 🌍 跨设备全球发送：类似 AirDrop 但跨平台，可发往世界各地任意设备。
- 🎞️ 原画质与加速：照片视频不模糊，速度取决于连接，并支持同网络 LAN 直连加速。
- 🔐 私密安全：文件不存云端/公共链接，端到端加密，使用 mTLS over TLS 1.3。
- 🆓 免费与无广告：非商业活动免费；商业用途需查看付费计划；完全没有广告。
- ⚡ 速度说明：快中继支持多吉比特；实际受双方网络影响，同 Wi-Fi 下可超互联网套餐速度。
- 🧩 对比优势：不同于 WeTransfer 的公共链接、Dropbox 的云存储、Aspera 的复杂企业方案、AirDrop 的近距离限制。
- 🎬 创作者友好：可发送 Final Cut Pro/Premiere 项目与 .fcpbundle，保留文件夹结构和链接。
- ⭐ 用户口碑：视频/音频制作、4K 大文件、跨设备传输被评价为“游戏规则改变者”。

---

### [Dozzle | 实时 Docker 日志查看器](https://dozzle.dev/?ref=tailwindweekly.com)

**原文标题**: [Dozzle | Real-time Docker Log Viewer](https://dozzle.dev/?ref=tailwindweekly.com)

实时日志功能支持按发生顺序流式查看容器日志，无需登录宿主机即可跨容器搜索、筛选并持续跟踪日志内容。

- 📡 实时流式传输容器日志，日志产生时可立即查看。
- 🔍 支持搜索、筛选和跨容器跟踪日志。
- 🖥️ 无需访问或操作宿主机即可完成日志查看。
- 📘 提供“了解更多”入口以获取详细信息。

---

### [](https://getmoshi.app/?ref=tailwindweekly.com)

**原文标题**: [Moshi — SSH & MOSH Terminal for Claude Code & AI Agents](https://getmoshi.app/?ref=tailwindweekly.com)

Moshi 是一款专为手机原生打造的 AI 编程代理终端应用，让你在沙发、海滩、咖啡馆或床上随时连接并查看自家电脑上的 AI 代理运行状态。它通过 SSH、Mosh 或 ET 直连你自己的 Mac、Linux、WSL 或 VPS，无需中转服务器，免费起步、无需账号或信用卡，App Store 评分 4.8（750+ 评价）。

- 📱 **产品定位**：Moshi 是 AI 代理的"婴儿监视器"，一款为手机而生、而非从桌面缩小移植的终端
- ⭐ **上架信息**：App Store 评分 4.8，免费开始，无需注册账号或绑卡
- 💻 **本地优先架构**：直连自己的 Mac、Linux、WSL 或 VPS，支持 SSH / Mosh / ET，无会话中继，Shell、仓库、文件与代理进程始终留在自有机器上
- 🤖 **广泛兼容代理**：支持 Claude Code、Codex、OpenCode、Cursor、Kimi Code、Grok Build、Pi 等 20 余种 CLI 代理
- 🔋 **连接稳定性**：Mosh 与 ET 连接可跨休眠、网络切换甚至应用被杀后保持存活
- 🎤 **核心操作能力**：设备端语音转终端输入、图片粘贴与标注、可自定义快捷面板、终端手势（滑动窗口、捏合缩放、双击 Tab）
- ⌨️ **进阶特性**：硬件键盘支持（⌘K、⌘O、⌘1-9）、最近目录快速跳转、主题字体图标联动、Face ID 解锁 SSH 密钥、会话恢复、CJK 输入、OSC 52 远程剪贴板、长按可点击链接
- 🪝 **moshi-hook 扩展**：可选安装的机器端钩子，不替换原有代理，新增手机原生聊天视图、代理任务看板、锁屏与 Apple Watch 实时活动、Diff 查看器、文件浏览器、浏览器预览、Webhook 提醒
- 🛠️ **安装方式**：一条命令 `curl -fsSL https://getmoshi.app/install.sh | sh`，覆盖 macOS、Linux 及 Windows 上的 WSL，支持 Homebrew、systemd 与手动安装
- 💬 **开发者口碑**：可在地铁、通勤途中或日常琐事间隙指挥 AI 编码；后台会话耗电明显优于 Termius，衔接手机与桌面工作流顺畅
- 🏗️ **与 ADE/IDE 的差异**：不锁定运行时，Moshi 以 11 MB 的体积叠加在 tmux 或 Herdr 之上，可随时切换工具，保留整台机器的完整控制权
- 📰 **订阅通讯**：约每月一封，涵盖新功能、AI 编码工作流与幕后笔记，可随时退订

---

