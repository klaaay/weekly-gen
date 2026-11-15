### [daisyUI 更新日志 — daisyUI Tailwind CSS 组件 UI 库](https://daisyui.com/docs/changelog/?ref=tailwindweekly.com)

**原文标题**: [daisyUI Changelog — daisyUI Tailwind CSS Component UI Library](https://daisyui.com/docs/changelog/?ref=tailwindweekly.com)

daisyUI 5.0 至 5.8.0 更新日志覆盖新组件、破坏性变更、可访问性与 RTL 修复、CSS 选择器优化及文档改进，整体聚焦主题化、响应式布局和跨浏览器兼容性提升。

- 🚀 5.8.0 新增 `prefers-reduced-motion` 防护、Alert 图标缺失布局适配、Join 圆角设置、Megamenu 普通链接/按钮样式、Menu 分页过渡、Range 简化计算，并允许跳过 theme-controller 和 scroll lock 的 `:root:has()` 选择器。
- 🐛 5.8.0 修复 Tailwind CSS 4.3.3 重复 CSS、`daisyui.css` 响应式选择器前缀、插件 include/exclude 完整组件名匹配，以及 Avatar、FAB、Footer、Join、Megamenu、Menu、OTP、Tab、Timeline 等组件问题。
- ♿ 5.8.0 与 5.7.x 集中修复大量强制颜色模式可见性问题，涉及 Divider、Loading、Progress、Rating、Timeline、Menu、Modal、Tooltip、Select、Skeleton、Status、Steps、Tab 等组件。
- 🧭 5.7.0 新增 `menu-paged` 修饰符，用于嵌套菜单内外导航；5.7.x 持续修复 RTL 布局、Tooltip 位置、OTP 边框/对齐、Checkbox 勾选、Badge/FAB 收缩及 Join 边框重叠等。
- 🆕 5.6.0 新增 Aura、OTP、Megamenu 组件，垂直 Range 滑块，HTML popover 模态框，Tooltip 对齐工具类，Vanilla Calendar Pro 集成，以及响应式 Rating 尺寸和可选中卡片样式。
- 🎨 5.6.0 重写按钮样式，改进 checked/disabled/soft/ghost/link/focus 状态；简化 Join 并防止嵌套泄漏；支持 `menu` 元素作为菜单容器；新增可自定义 Select 的 `selectedcontent` 默认样式。
- 🛠️ 5.6.0 修复 `prefers-reduced-motion` 加载动画、Dropdown 溢出裁剪、水平/垂直菜单对齐、CSS 变量前缀、卡片 `focus-visible` 轮廓、Collapse 过渡、Safari 日期输入、Mockup-code 高亮及 React Day Picker/Pikaday 主题色等问题。
- 🧩 5.5.x 新增 `hover-3d`、`text-rotate`、`skeleton-text`、`dropdown-close`，改进 Diff 拖拽区域、Prose 代码内边距和 Menu details 平滑过渡，按钮选择器优化使 CSS 体积减小约 7%。
- 🐞 5.5.x 修复 Drawer 在 Chrome/Windows 上的模糊渲染、Modal 内 Dropdown 动画、面包屑 RTL 逻辑边距、Tab focus z-index、Join 焦点层级、Range 超宽屏颜色、`drawer-end` 规则优先级及 Safari 聊天气泡高度等。
- 🧱 5.3.0 新增 CSS 图层以改善特异性，使 Card 修饰类和 `btn-disabled` 支持 Tailwind 变体；5.3.x 修复 Tab 样式泄漏、Range 滑块 Safari 颜色、Collapse 文本查找、背景色渗透及 Select multiple 溢出。
- 🎛️ 5.2.0 新增 Drawer 的 `is-drawer-open`/`is-drawer-close` 变体，支持图标式侧边栏；Countdown 支持 0–999 动态宽度与双数字独立动画；自动检测垂直滚动条并设置 `scrollbar-gutter`。
- 🖱️ 5.1.0 新增 Hover Gallery、FAB/Speed Dial、原生 Select 样式，并为所有动画支持 `prefers-reduced-motion`；同时修复 Modal 隐藏/焦点、iOS 输入缩放、FAB 子元素可见性、Collapse 动画和 Tooltip 动画。
- 💥 5.0.0 为重大重构版本：Alert 新增 outline/dash/soft 及垂直/水平布局；Avatar 类名改为 `avatar-online`/`avatar-offline`/`avatar-placeholder`；Bottom Navigation 移除并改用 Dock；Card 的 `card-bordered` 改为 `card-border` 并新增尺寸。
- 🔄 5.0.0 重命名 Menu 的 `disabled`/`active`/`focus` 为 `menu-disabled`/`menu-active`/`menu-focus`，默认不再 `w-full`；Mockup 的 `camera`/`display` 改为 `mockup-phone-camera`/`mockup-phone-display`；Tab 的 `tabs-lifted` 改为 `tabs-lift` 并由 Grid 改 Flex。
- 🧹 5.0.0 移除 Artboard 的 `artboard`/`phone-*`（改用 Tailwind 宽高）、Mask 的 parallelogram、`form-control`/`label-text`/`label-text-alt`（改用 fieldset/legend）、`btn-group`/`input-group`（改用 Join），并让 Input/Select/Textarea/FileInput 默认带边框和 20rem 宽度。
- 🐛 5.0.1 至 5.0.55 持续修复 CDN 颜色透明度、Dropdown 位置、Diff 轮廓、checked 按钮、Alert 响应式、Join 圆角、iOS 缩放、Tooltip 空内容、table-zebra 行色、Drawer z-index 及 Tailwind Play 兼容性等问题。
- 🌍 多个版本持续改进 RTL 支持，包括 Dropdown、Toast、Breadcrumbs、Join、Input/Email、Modal-start/end、Avatar 指示点、Floating Label 和 Skeleton 动画等方向与定位。
- 📚 文档新增 daisyUI 5.6 博客及 Aura、OTP、Megamenu、垂直 Range、Tooltip 对齐、Popover Modal、可选中卡片等文档，增加代码复制按钮，主题生成器支持连字符/空格，搜索覆盖所有类名和变量。
- ⚙️ 依赖与工具链更新 Bun、Tailwind CSS、Lightning CSS、PostCSS、Prettier 等，新增 `daisyui` 包导出并更新技能文件以覆盖新增和变更组件。

---

### [Preline UI 更新日志 | Tailwind CSS 组件库更新](https://preline.co/docs/changelog.html?ref=tailwindweekly.com)

**原文标题**: [Preline UI Changelog | Tailwind CSS Component Library Updates](https://preline.co/docs/changelog.html?ref=tailwindweekly.com)

本文是 Preline UI 的更新日志，记录 Tailwind CSS 组件、JavaScript 插件、模板、修复、改进与版本发布；内容从 v1.0.0 初始版一直覆盖到 2026 年的 v5.1.0，重点体现可访问性、框架集成、主题化、AI/MCP 能力与插件架构的持续演进。

- 🚀 v5.1.0（2026-11-12）发布 10 项修复与新选项，涉及 Advanced Select、Advanced Datepicker、Overlay 和 npm 包；新增 Changelog Timeline 区块。
- 🧩 v5.1.0 修复 npm `engines.node` 版本锁定问题，修复 Advanced Select 选中项标题的 HTML 注入风险、tags 模式 `setValue()` 初始化报错，以及 Datepicker 非 UTC 时区日期偏移、内联初始化失败、禁用日期交互等问题。
- ⌨️ v5.1.0 还修复 Overlay 内链接/按钮按 Enter 被拦截的问题，并新增 `optionValueAsTitle`、`showTodayButton`、`inputModeOptions.closeOnSelect` 等选项。
- 🤖 v5.0（2026-08-21）引入 Preline MCP、AI Prompts、Animated Icons，并将 Tailwind CSS 升级至 v4.3；MCP 与动画图标目前仅限 Preline Pro。
- 🛠️ v5.0 修复 Datepicker 周标签与日期行对齐、Range Slider 图表主题同步、Advanced Select 相对路径 `apiUrl` 报错，并为 Advanced Select 增加 `request`/`requestCompleted` 事件。
- 🎨 v4.2.0（2026-05-10）新增 Marquee 组件，扩展 Stepper 与 Spinner 示例，新增 13 个框架指南，支持 Tailwind CSS v4.2.x，并修复 dropdown 与 scrollspy 行为。
- 🧱 v4.1.x（2026-02）重点修复插件导出问题、补充 NPM 包 Themes 文件，并改进插件模块架构以支持 tree-shaking，新增 `preline/non-auto` 显式初始化入口。
- 🌈 v4.0.0（2026-01-28）推出 Preline Themes、10+ 框架指南，新增 Tabs、Mega Menu、Advanced Select optgroup 等组件示例，并修复可访问性、搜索、分页、URL 编码、Datepicker 定位等问题。
- ♿ v3.2（2025-07-30）新增 CMS 与 AI Chat 模板、15+ 示例，引入集中式 Accessibility Management，为 Tooltip/Popover 增加自动定位，并改进 Advanced Select、Combobox、Carousel 等插件。
- ⚡ v3.0.0（2025-03-04）升级至 Tailwind CSS v4，新增 Advanced Datepicker、Scroll Nav 插件与 TimePicker、Mega Menu 等组件，并用 Floating UI 替换 Popper.js。
- 🧭 v2.7–v2.6（2024-12 至 2025-01）新增 Sidebar、Maps、JSX 复制、Textarea Autoheight、Layout Splitter、Toast、Confetti、Leaflet Maps 等能力，并完善插件 `destroy` 生命周期。
- 🌳 v2.5–v2.0（2024-2023）陆续加入 Tree View、Advanced Range Slider、ComboBox、File Upload、Datatables、Stepper、Carousel 等插件，v2.0 还引入 TypeScript 支持并改用 Lucide 图标。
- 🧪 v1.x（2022）为早期阶段，包含初始发布、Starter Pages & Examples、Figma 资源、框架指南与基础组件/插件体系搭建。

---

### [发布 v4.11.0 · schoero/eslint-plugin-better-tailwindcss · GitHub](https://github.com/schoero/eslint-plugin-better-tailwindcss/releases/tag/v4.11.0?ref=tailwindweekly.com)

**原文标题**: [Release v4.11.0 · schoero/eslint-plugin-better-tailwindcss · GitHub](https://github.com/schoero/eslint-plugin-better-tailwindcss/releases/tag/v4.11.0?ref=tailwindweekly.com)

本次发布为 eslint-plugin-better-tailwindcss 的 v4.11.0 最新版本，由 schoero 于 11 月 9 日发布，包含 3 个提交，主要带来选择器扩展能力，并修复类名排序、规则提示、构建配置和测试相关问题。

- 🚀 **版本发布**：v4.11.0 为最新版本，发布于 11 月 9 日，包含 3 个提交。
- ✨ **新增功能**：允许 selectors 扩展默认选择器（#412）。
- 🛠️ **规则修复**：更新未知类名排序与定位的描述信息。
- 📝 **文档与提示优化**：改进规则文档和警告信息，并更新 enforce-consistent-class-order 相关说明（#432）。
- ⚙️ **构建配置修复**：修复构建配置问题（#433）。
- 🔢 **排序处理改进**：改进重复类名和数字类名的严格排序处理（#431）。
- ✅ **测试修复**：修复 CI 测试选项（54451e7）。
- ❤️ **贡献者**：感谢 Simon.b（@gamegee）等贡献者。
- 📦 **发布资源**：该版本包含 2 个资源文件。

---

### [下载适用于 Mac、Windows 和 Linux 的 DuckyHelper](https://www.duckyhelper.com/download/?utm_source=tailwindweekly&utm_medium=newsletter&utm_campaign=nov26)

**原文标题**: [Download DuckyHelper for Mac, Windows and Linux](https://www.duckyhelper.com/download/?utm_source=tailwindweekly&utm_medium=newsletter&utm_campaign=nov26)

这是一则 DuckyHelper for Mac 的下载页面信息，主要提供软件下载入口，并注明适用于搭载 Apple 芯片的 Mac 设备。

- 💻 DuckyHelper 提供 Mac 版本下载
- ⬇️ 页面包含“Download for Mac”下载入口
- 🍎 系统要求为 macOS 14 或更高版本
- 🖥️ 仅支持 Apple silicon 芯片设备
- 🏠 提供“Back to home”返回首页导航

---

### [CSS 的未来 ✨ • Josh W. Comeau](https://www.joshwcomeau.com/css/interop-2027/?ref=tailwindweekly.com)

**原文标题**: [The Future of CSS ✨ • Josh W. Comeau](https://www.joshwcomeau.com/css/interop-2027/?ref=tailwindweekly.com)

文章介绍 Interop 项目如何推动主流浏览器统一支持 Web 技术，并以 Subgrid 为例说明其成效；随着 Interop 2027 规划启动，Mozilla 推出功能排名系统，作者据此列出自己投票的 10 项 CSS 新特性，展望未来一年 CSS 的发展方向。

- ✨ **Interop 成效显著**：Chrome、Apple、Microsoft、Mozilla 等共同参与，聚焦功能通常能在一年内接近全浏览器支持。
- 🧮 **CSS 函数**：通过 `@function` 和 `result` 定义可复用函数，可实现极坐标转笛卡尔坐标等复杂计算。
- 🔲 **corner-shape**：提供 `squircle`、`bevel`、`notch`、`scoop` 等圆角替代形状，且边框、轮廓和阴影会跟随新形状。
- 🖋️ **border-shape**：可用直线、弧线和贝塞尔曲线自定义边框形状，并支持动画过渡。
- ⚓ **锚定容器查询**：在 Anchor Positioning 基础上检测元素是否使用回退位置，便于处理 tooltip 翻转等场景。
- 🧬 **inherit() 函数**：允许取出继承值并用 `calc()` 修改，解决嵌套圆角等需要变换继承值的场景。
- 🎬 **滚动触发动画**：与滚动驱动动画互补，可在滚动到特定位置时触发关键帧动画，减少对 JavaScript 的依赖。
- ♿ **reading-flow / reading-order**：让 Tab 焦点顺序跟随响应式视觉布局，改善动态网格和移动端可访问性。
- 📏 **interpolate-size 与 calc-size()**：支持在 `height: 0` 和 `height: auto` 等关键字尺寸之间过渡，便于实现折叠面板动画。
- 🧱 **gap decorations**：通过 `rule`、`row-rule`、`column-rule` 在网格间隙绘制边框式线条，避免空单元格和复杂变通方案。
- 📌 **滚动状态容器查询**：可检测 `position: sticky` 是否“粘住”，以及滚动容器是否可向上/向下滚动，用于动态样式和滚动提示。
- 🚀 **结论与建议**：截至 2026 年 10 月，多数特性已在 Chrome/Edge 支持，Firefox/Safari 尚未支持；作者建议以渐进增强方式使用，并强调在 LLM/智能体时代仍应掌握现代 CSS，同时鼓励开发者参与 Interop 2027 投票。

---

### [使用 CSS 网格通道的原生瀑布流布局 - Piccalilli](https://piccalil.li/blog/native-masonry-layouts-with-css-grid-lanes/?ref=tailwindweekly.com)

**原文标题**: [
  Native masonry layouts with CSS grid lanes - Piccalilli
](https://piccalil.li/blog/native-masonry-layouts-with-css-grid-lanes/?ref=tailwindweekly.com)

文章回顾了原生 CSS 瀑布流布局的长期演进，介绍最终采用的 `display: grid-lanes` 方案，并说明其工作方式、自动填充算法、`fit-tolerance`、方向切换、`subgrid` 支持及当前浏览器兼容情况。

- 🧱 原生 masonry 布局最终以 `display: grid-lanes` 落地，而不是早先讨论的 `display: masonry` 或 `grid-template-rows: masonry`。
- 🕰️ 过去只能借助多栏布局、需预知高度的 Grid hack，或依赖 `Masonry.js`；CSSWG 长期争论它应属于 Flexbox、Grid 还是独立布局。
- 🧩 2025 年 CSSWG 同意复用 Grid 的轨道定义与放置属性，并于 2025 年 12 月确定 `grid-lanes` 名称。
- 📐 使用 `grid-template-columns` 或 `grid-template-rows` 定义轨道：定义列时纵向填充，定义行时横向填充。
- ⚙️ 浏览器会跟踪每条 lane 的已占用空间，通常把下一项放入最短 lane，更新位置后重复该过程。
- 🎛️ 仍支持 `grid-column: span 2` 等显式放置；跨列项和显式定位项会先放置，再对剩余项目运行自动填充。
- 📏 `fit-tolerance` 控制高度相近的 lane 是否视为“足够接近”；默认 `normal` 约为 `1em`，`0` 更紧凑，`infinite` 更优先源码顺序。
- ♿ 视觉顺序可能与 DOM 源码顺序不同，需检查可访问性；屏幕阅读器通常按文档顺序读取。
- 🧱 支持 `subgrid`，可让卡片内部元素与父级轨道对齐，适合食谱卡等嵌套布局。
- 🧪 规范仍为 Editor’s Draft，细节可能变化；Safari 26.4+ 已支持，其他浏览器支持仍在推进。
- 🛟 对不支持 `grid-lanes` 的浏览器，建议提供更简单的回退布局。

---

### [图片懒加载：loading="lazy" 与 eager 的工作原理 | Calibre](https://calibreapp.com/blog/native-lazy-loading?ref=tailwindweekly.com)

**原文标题**: [Lazy Loading Images: How loading="lazy" and eager Work | Calibre](https://calibreapp.com/blog/native-lazy-loading?ref=tailwindweekly.com)

懒加载通过 `loading="lazy"` 等少量 HTML 属性延迟首屏外媒体加载，减少初始下载并加快首屏渲染；但若误用，尤其懒加载 LCP 首屏大图，反而会拖慢性能。文章总结了用法、使用现状、浏览器行为、常见错误与优化建议。

- 🚀 `loading="lazy"` 可延迟图片、iframe、视频和音频；未设置时默认是 `eager`，浏览器会立即获取。
- 🖼️ 图片和 iframe 的懒加载支持广泛；视频和音频支持仍有限，Firefox、Safari 尚未支持。
- 📊 实际使用率偏低：Chrome 页面加载中约 26% 的图片、1.5% 的 iframe、0.06% 的视频使用懒加载；HTTP Archive 显示 44% 页面使用。
- ⚠️ 17% 页面懒加载了 LCP 首屏大图，导致 LCP 约延迟 262ms，应避免。
- 📏 浏览器预取距离不同：Chrome 会按网速调整，慢网最多约 8000px；Firefox 固定 600px；Safari 约一个视口，iframe 进入屏幕才加载。
- ❌ 常见错误有三类：懒加载 LCP 图片、未设置宽高或 `aspect-ratio` 导致布局偏移、以及模板中全量懒加载。
- ✅ 推荐策略：LCP 图片用 `fetchpriority="high"`；首屏其他图片保持默认 eager；首屏以下媒体再用 `loading="lazy"`。
- 🧩 使用 `<picture>` 时，把 `loading` 和 `fetchpriority` 放在 `<img>` 上，而非 `<source>`；并审查 SSR 框架实际输出的 HTML。
- 🎨 可用 `content-visibility: auto` 跳过离屏内容布局与绘制，配合 `contain-intrinsic-size` 防止滚动条跳动，且不影响查找和键盘导航。
- 🔍 对地图、聊天组件、CSS 背景图、Firefox/Safari 视频音频、按需 JS 等，可用 `IntersectionObserver` 实现更灵活的懒加载。
- 🛠️ 检查是否生效：DevTools Network 过滤 Img/Media/Doc，禁用缓存刷新且不滚动，再滚动对比新增请求，并检查 Elements 中的实际 HTML。
- 🎯 正确组合 `preload`、`loading="lazy"` 和 `fetchpriority` 几乎是免费的性能收益；用错则可能损害性能。

---

### [Phone.inc – 将你的个人手机变成商务手机](https://www.phone.inc/?ref=tailwindweekly.com)

**原文标题**: [Phone.inc â Turn your personal phone into a business phone](https://www.phone.inc/?ref=tailwindweekly.com)

Phone.inc 可将个人手机变成商务电话：无需第二张 SIM 卡或额外手机，即可获得独立工作号码，并在接听前查看来电者的订单、历史对话和相关信息；支持 iPhone、Android，个人使用可免费接听，且可连接多种业务工具。

- 📱 将个人手机转为商务电话，无需购买新手机或携带两部设备。
- ☎️ 在应用内接听商务来电，个人号码保持私密，商务号码可分享到网站和名片。
- 👤 接听前显示来电者信息、上次通话内容、订单等，帮助提前准备。
- 🌍 可选择欧盟、英国、美国或加拿大的本地商务号码，并设置欢迎语和营业时间。
- 💻 提供 iPhone 和 Android 原生应用，团队成员可继续使用现有手机。
- 🆓 个人使用可免费：含一个商务号码和无限接听来电，但不能外呼，仅限一人使用。
- 🔗 可连接 Shopify、Stripe、HubSpot、Zendesk、Calendly 等 23 个工具，通话时显示订单、发票、预约等信息。
- ⏰ 即将推出：自动生成跟进提醒、保存来电者姓名、接听时播报来电者介绍。
- 🎯 专注小企业，避免复杂呼叫中心功能、捆绑手机、强制销售电话和长期合同。
- 📝 可通过加入等待名单获取邀请，并在轮到时选择号码。

---

### [MicroKit UI - 复制粘贴即可使用的 React 与 CSS 微交互](https://microkit.co/?ref=tailwindweekly.com)

**原文标题**: [MicroKit UI - Copy-paste React & CSS microinteractions](https://microkit.co/?ref=tailwindweekly.com)

MicroKit UI 是面向重视交互体验开发者的组件库，通过官方 shadcn registry 提供 57 个微交互组件，强调“细节很重要”，并采用复制代码而非安装 npm 包的使用方式。

- 🧩 MicroKit UI 是专注交互体验细节的组件库，适合在意每次交互体验的开发者。
- ⚙️ 可通过 `npx shadcn@latest add @microkit/...` 从官方 shadcn registry 添加组件，并鼓励在 GitHub 上 Star 支持。
- 🎛️ 提供 57 个微交互组件，支持 React、CSS 筛选，并可按最新、热门、A–Z 浏览。
- ✨ 组件覆盖点击反馈、悬停、输入、数据展示、导航等场景，例如 Cursor Edge Glow Button、Count Up Number、Glide Pill Tabs、Blur Glide Menu。
- 📦 不提供 npm 包安装，用户可选择 TypeScript/JavaScript 与 CSS/Tailwind 后复制代码自行修改。
- 🧠 57 个交互中 29 个无需额外依赖；其余 28 个使用 `lucide-react` 渲染图标，组件页面会注明安装要求。
- 🎨 每个交互都提供 Tailwind 版本，兼容 Tailwind v3 和 v4，官网本身基于 Tailwind v4 构建。
- ⚛️ 多数组件是无客户端状态的标记和 CSS，可直接用于 Next.js App Router 服务端组件；使用状态、ref 或事件处理时需添加 `"use client"`。
- 🪪 代码采用 MIT 许可，可用于商业项目；部分交互改编自公开示例和 Webflow 导出，归属需明确时可提 issue。
- 🚀 支持提交自己的交互：提交页接收组件代码和可选截图，并预填 GitHub issue 供审核和发布。
- 🔗 灵感来源包括 21st.dev、morphin.dev、huly.io、oryzo.ai。

---

### [RenderPixels · 来自AI助手的像素级精确图像](https://renderpixels.com/?ref=tailwindweekly.com)

**原文标题**: [RenderPixels · Pixel-exact images from your AI assistant](https://renderpixels.com/?ref=tailwindweekly.com)

RenderPixels 是一款让 AI 助手按精确尺寸生成营销图片的工具，用户可通过 MCP 连接 Claude、ChatGPT 等主流 AI 助手，用自然语言描述需求即可获得 Instagram 帖、横幅、Logo、网站图标等可直接使用的文件。它支持品牌套件、一次生成多平台尺寸、永久链接，并提供每月 50 次免费渲染额度。

- 🖼️ **核心功能**：向 AI 助手描述需求，RenderPixels 按各平台要求的精确尺寸生成图片，并返回可直接使用的文件
- 🔌 **广泛兼容**：支持 Claude、Claude Code、ChatGPT、GrokBot 及所有支持远程 MCP 与 OAuth 的 AI 助手，无需 API 密钥
- ✍️ **工作方式**：AI 助手用代码写设计，RenderPixels 在真实浏览器中渲染，并自动检查文字裁切、字体或图片缺失
- 🔗 **永久链接**：每个文件都有永久 URL，可直接放入网页、meta 标签或消息中
- ⚖️ **与 ChatGPT 对比**：同一提示下，ChatGPT 返回 1731×909、2.5MB 的图片，需二次处理；RenderPixels 输出精确的 1200×630、85KB 文件，可直接上传
- 🎨 **品牌套件**：保存颜色、字体和 Logo 后按名称调用，一次请求即可生成多个平台尺寸，风格统一
- 📐 **多格式支持**：Instagram 帖、X 横幅、Logo、网站图标集、Open Graph 链接预览等均可生成
- 💰 **免费额度**：每月 50 次免费渲染，无需绑卡，每月 1 日 UTC 重置
- 💳 **积分定价**：2,000 次 10 美元起，最低约 $0.0025/次；积分永不过期，无订阅
- 🛠️ **快速设置**：添加 MCP 服务器 URL，通过 OAuth 登录授权即可，约一分钟完成
- 📸 **能力边界**：不生成照片或插画，只渲染 HTML/CSS 和 SVG，可通过 HTTPS URL 引用外部照片
- ✏️ **计费规则**：每次编辑算一次渲染；一次生成多尺寸（如整套 favicon）只算一次
- 📄 **商用与数据**：用户拥有生成图片的版权，但需确保字体、Logo、照片等素材权利；删除账户后渲染文件及链接会被清除

---

### [Cloudup](https://cloudup.com/?ref=tailwindweekly.com)

**原文标题**: [Cloudup](https://cloudup.com/?ref=tailwindweekly.com)

未提供可总结的正文内容，因此暂时无法提取文章要点；请补充需要总结的文本，我将按要求生成中文概览和带表情符号的项目符号列表。

- 📄 当前输入缺少文章正文
- ✍️ 请粘贴或发送需要总结的内容
- ✅ 收到内容后将输出中文概览与“-”项目符号要点

---

### [BatFi：macOS 电池充电限制 | micropixels](https://micropixels.software/batfi/?ref=tailwindweekly.com)

**原文标题**: [BatFi: Battery Charge Limit for macOS | micropixels](https://micropixels.software/batfi/?ref=tailwindweekly.com)

BatFi 是一款适用于 Mac 的电池充电限制工具，可将充电上限设为 80% 或任意值，并支持按时间、地点自动执行规则；同时提供电池监控、菜单栏显示、电源模式快捷键等功能，一次性购买 $15，需许可证。

- 🔋 可将 Mac 充电限制在 80% 或其他自定义上限，必要时一键充至 100%。
- 🕒 支持按时间和地点设置充电规则，例如办公桌保持 60%、出门前补电、周末充满。
- 📊 相比 macOS 仅支持 80%–100%，BatFi 支持 50%–100%，并可在 macOS 27 上使用 BatFi 4 设置更低限制。
- 🌡️ 支持温度超过 40°C 时暂停充电；使用时应关闭 macOS 自带充电限制和优化电池充电。
- 📈 菜单栏可查看功率输入/输出、耗电应用、循环次数、温度和电池健康等 macOS 隐藏信息。
- ⌨️ 可通过全局快捷键切换低电量、高电量或自动电源模式。
- 💡 建议多数用户默认设为 80%，并每月左右让电池耗尽后充满一次；macOS 偶尔充至 100% 用于校准，BatFi 会暂时让路。
- ✅ BatFi 使用与 macOS 相同的充电控制，官方称安全，可减少长期电池损耗。
- 💻 要求 macOS Sonoma 14.8 或更高版本及 Apple silicon；需许可证，$15 一次性购买，非订阅，一份许可证覆盖所有 Mac。
- ⬇️ 可通过官网下载，或使用 `brew install --cask batfi` 安装。

---

### [MFlare：在菜单栏中查看 Cloudflare 用量与部署](https://mflare.yuy1n.io/?ref=tailwindweekly.com)

**原文标题**: [MFlare: Cloudflare usage and deploys in your menu bar](https://mflare.yuy1n.io/?ref=tailwindweekly.com)

MFlare 是一款常驻 macOS 菜单栏的 Cloudflare 监控与通知工具，可集中查看 Workers、Durable Objects、KV、R2、D1 的用量与配额，及时提醒配额即将用尽、构建和部署状态，并支持桌面小组件、AI 助手和 Raycast 集成。应用数据本地存储，免费版限 1 个账户，Pro 一次性付费解锁多账户等高级功能。

- 📊 在菜单栏直接查看 Workers、Durable Objects、KV、R2、D1 的使用量与配额，无需反复打开 Cloudflare 仪表盘。
- 🔔 配额快用完时提前提醒；无论是 `git push` 还是 `wrangler deploy`，构建到部署各阶段都会推送通知。
- 🖥️ 提供小、中、大三种桌面小组件，按使用率从高到低展示当前账户资源情况，并支持查看实时构建日志和跳转 Cloudflare。
- 🤖 可让 AI 助手查询用量、Workers 和构建日志；Pro 版包含面向 AI 代理的 MCP 服务器。
- ⌨️ 支持 Raycast 扩展，可在不离开键盘的情况下搜索用量与日志，Pro 版附带。
- 💰 免费版 $0，含核心用量/配额提醒、构建部署通知，限 1 个账户；Pro 原价 $5，现价 $3 一次性买断（40% off），含无限账户、MCP、小组件和 Raycast 扩展，可激活 1 台 Mac。
- 🔐 数据保存在本机，登录信息存于 Keychain；应用无自建服务器，直接与 Cloudflare 通信。
- 🧾 许可证由 Dodo Payments 处理；换 Mac 或重装前可在设置中停用许可证，再在新设备激活；找不到许可证可查邮件或联系支持。
- 💳 中国大陆用户结账时选择人民币并切换中文，可在第二页使用微信支付；许可证会发送到结账邮箱。
- ⚙️ 要求 macOS 14 或更高，支持 Apple 芯片与 Intel；当前版本 0.11.0，大小 8.13 MB。

---

