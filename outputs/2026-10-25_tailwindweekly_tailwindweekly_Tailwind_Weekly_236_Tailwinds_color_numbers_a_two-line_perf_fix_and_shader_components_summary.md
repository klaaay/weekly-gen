### [发布 1.1.0 · hunvreus/basecoat · GitHub](https://github.com/hunvreus/basecoat/releases/tag/1.1.0?ref=tailwindweekly.com)

**原文标题**: [Release 1.1.0 · hunvreus/basecoat · GitHub](https://github.com/hunvreus/basecoat/releases/tag/1.1.0?ref=tailwindweekly.com)

Basecoat 1.1.0 已发布，本次更新重点包括 Toast 默认转义、单文件 CSS 构建、字体调整，以及大量组件与 CDN 构建问题修复。

- 🚀 **版本发布**：Basecoat 1.1.0 由 grugbraindev 于 10 月 23 日发布。
- ⚠️ **升级注意**：Toast 的 `title`、`description`、`action.label` 和 `cancel.label` 默认按文本转义；如需传 HTML，需在 `toaster.toast()` 中添加 `html: true`。
- ➕ **新增垂直分隔线**：`<hr aria-orientation="vertical">` 可渲染为填满所在行的 1px 竖线。
- 📦 **新增单文件构建**：提供 `dist/basecoat.bundle.css` 和 `dist/basecoat-{style}.bundle.css`，内联全部 Basecoat 导入，便于独立 Tailwind CLI 在无 npm 场景使用。
- 🧩 **Toast 新增 HTML 选项**：`toaster.toast()` 支持 `html: true`，用于传入原始 HTML。
- 🔤 **默认字体调整**：`--font-sans` 默认以 `"Geist"` 开头，并保留 `"Geist Sans"` 作为回退；文档改为安装 `@fontsource/geist`。
- 📚 **文档改进**：升级到 `reallysimpledocs@^1.0.14`，`llms.txt` 链接到各页面的 Markdown 版本；补充 Tailwind 工具类与主题色、CDN 构建及 Tailwind Play CDN 的用法。
- 🐞 **交互修复**：关闭 Combobox 弹窗时，Escape 不再误关外层 Dialog。
- 🖱️ **滚动与嵌套修复**：Dialog、Alert Dialog、Command Dialog、Drawer 打开时锁定页面滚动；嵌套 Popover、Dropdown Menu、Select、Combobox 打开时保持父级开启。
- 🧭 **Sidebar 样式修复**：导航样式限定为 `.sidebar > nav`，避免侧边栏内 Tabs 等其他 `nav` 元素被固定和堆叠。
- 📱 **移动端与样式修复**：修复 iOS 点击 Combobox、Command 搜索、原生 Select、Input Group 等输入框时的自动缩放；修复 Slider 焦点环、RTL Sidebar 子菜单箭头、暗色模式和 Tooltip 箭头样式。
- 🛠️ **CDN 与模板修复**：CDN `.min.css` 改用 esbuild 压缩，避免规则丢失；修复 Toast 文档示例通过 HTMX 写入浏览器历史的问题，并更新 1.0.0 迁移片段以兼容 Tailwind v4。
- 🙌 **贡献者致谢**：感谢 @ytsruh、@PhilipdeRijk、@sgruendel、@alexander-posztos 和 @Jezda1337 等贡献者。

---

### [Kokonut UI - 面向 React 和 Tailwind CSS 的免费开源 UI 组件](https://kokonutui.com/?ref=tailwindweekly.com)

**原文标题**: [Kokonut UI - Free Open Source UI Components for React and Tailwind CSS](https://kokonutui.com/?ref=tailwindweekly.com)

Kokonut UI 是一个免费开源的 React 组件目录，基于 Tailwind CSS、Motion 和 shadcn/ui 构建，提供可实时交互的组件演示，并支持通过一条命令或一句提示词快速安装。

- 🧩 组件库收录 102 个组件，覆盖背景、卡片、导航、输入、AI、媒体、文字和按钮等类别。
- ⚡ 每个组件都提供实时演示，安装后以单文件源码形式归开发者所有。
- 🤖 支持 AI Agent 集成，可通过 shadcn MCP 连接 Claude Code、Cursor、VS Code、Codex 等编辑器。
- 🛠️ 安装方式灵活：可用 AI 代理描述需求、使用 shadcn CLI 命令，或配置注册表命名空间。
- 💬 获得 shadcn/ui 创作者及多位开发者推荐，突出动画效果、视觉表现及与 shadcn/Next.js 生态的兼容性。
- 💎 Kokonut UI Pro 是付费扩展目录，包含 120+ 组件、20+ 分类和 6 个模板，$119 终身访问，限时 25% 折扣。
- 🚀 Pro 还提供 Heroes、App UI、Kanban Board、Slash Command Menu、Onboarding Checklist，以及作品集、AI Agent、创业公司等完整模板。

---

### [适用于 React、Next.js 和 React Native 的动画组件 · beUI](https://beui.dev/?ref=tailwindweekly.com)

**原文标题**: [Animated Components for React, Next.js and React Native · beUI](https://beui.dev/?ref=tailwindweekly.com)

beUI 是一个面向 React、Next.js 和 React Native 的动画组件库，提供可复制源码或通过 CLI 安装的免费开源组件，并有 Pro 高级资源扩展。

- 🧩 包含 146 个 React 组件和 71 个 React Native 组件，覆盖按钮、模态框、Toast、Dock、Tabs、时间线、图表等。
- ⚙️ 基于 Motion（Framer Motion）与 Tailwind CSS 构建，通过 shadcn 分发，支持 bun、npm、pnpm、yarn 安装。
- 🆓 公共库采用 MIT 许可，可免费用于个人和商业项目，并允许修改源码、样式、动效和行为。
- 📱 beUI Native 将组件带到 Expo 和裸 React Native，使用 Reanimated、Gesture Handler 与 Uniwind，针对触控重新构建。
- 📦 安装示例包括 `bunx --bun shadcn add @beui/timeline` 和 `npx beui-native add button`，React Native 组件还支持 Expo Go 扫码体验。
- ✨ 新组件包括 Card Dealer、Sankey Chart、Timeline，以及 Pause clips、Tabs、Color Picker、Alert、Swipeable List 等。
- 🚀 beUI Pro 提供 300+ 高级区块和动画组件、完整落地页模板、动画插画、Agent Skill/MCP、私有 registry、终身更新及无限个人/客户项目。
- ✅ FAQ 说明项目需要 React 19、Tailwind CSS 4 和 Motion；Pro 是独立付费产品，不影响免费组件使用。
- 💬 社区评价集中称赞其动效流畅、设计干净、交互细节用心，并表示会用于实际项目。
- 🛠️ 组件源码位于用户项目中，便于按产品主题和需求直接定制。

---

### [React Bits — 免费动画 React 组件](https://reactbits.dev/?ref=tailwindweekly.com)

**原文标题**: [React Bits â Free Animated React Components](https://reactbits.dev/?ref=tailwindweekly.com)

这是一套面向创意开发者的 React 组件库，提供可安装并拥有源码的动画组件与背景，所有数值均可调节，并支持按需选择技术栈和安装方式。

- 🎨 面向创意开发者，提供动画组件与动态背景。
- 🛠️ 组件以源码形式安装，源码归你所有，所有参数均可自定义调节。
- 🧩 资源分类包括文字动画、动画、组件、背景和微交互。
- ⚙️ 可选择 JavaScript 或 TypeScript，以及纯 CSS 或 Tailwind。
- 📦 支持复制源码或通过 CLI 安装所需组件，并提供安装指南。

---

### [Vue Bits - 面向 Vue 的动画 UI 组件](https://vue-bits.dev/?ref=tailwindweekly.com)

**原文标题**: [Vue Bits - Animated UI Components For Vue](https://vue-bits.dev/?ref=tailwindweekly.com)

未提供可总结的正文内容，暂时无法生成文章摘要。
- 📄 请粘贴或发送需要总结的文章文本。
- ✅ 收到内容后，我会按中文格式提炼关键信息，并为每条要点配上合适表情符号。

---

### [一个构建于 Base UI 之上的全新现代 UI 组件库 - coss ui](https://coss.com/ui?ref=tailwindweekly.com)

**原文标题**: [A new, modern UI component library built on top of Base UI - coss ui](https://coss.com/ui?ref=tailwindweekly.com)

coss.com UI 是一个基于 Base UI 构建的现代 UI 组件库，面向开发者与 AI，提供 529 个 particles（组件），覆盖从基础控件到复杂交互的完整界面需求，并以开源方式发布。

- 🧱 基于 Base UI 构建，定位为面向开发者和 AI 的现代组件库
- 📦 收录 529 个 particles/组件，组件数量丰富
- 🧩 基础控件齐全：按钮、输入框、标签、复选框、开关、滑块等
- 🪟 弹层与导航组件完善：对话框、抽屉、菜单、弹出层、提示框、标签页、面包屑
- 📅 日期与选择能力突出：日历、日期选择器、下拉选择、组合框、自动完成
- 📝 表单支持完整：Field、Fieldset、Form，简化校验与提交
- 💬 面向 AI/聊天场景：新增 Composer，支持增长输入、持续操作、提及与斜杠命令
- 🔍 提供效率型组件：Command 命令面板、Kbd 快捷键展示
- 📊 数据与反馈组件丰富：表格、进度、仪表、骨架屏、加载器、Toast
- ♿ 注重可访问性：无障碍标签、键盘导航、屏幕阅读器友好
- 🌍 开源项目：2026 coss.com，倡导 open source, open heart, open mind

---

### [Animate UI - 适用于 React 的动画基础组件](https://animate-ui.com/?ref=tailwindweekly.com)

**原文标题**: [Animate UI - Animated primitives for React](https://animate-ui.com/?ref=tailwindweekly.com)

Animate UI 提供可即插即用的动画基础组件，目标是用一条命令为 shadcn/ui 组件添加动效；通过替换导入即可保留现有组件、样式与 API，并覆盖 Radix UI、Base UI、React Aria 等生态。页面还展示了多种可交互动画组件，以及可用自然语言驱动的 AI 动效技能。

- 🎞️ 一条命令即可为 shadcn/ui 组件添加动画，强调“替换导入、保留组件/样式/API”。
- 🧩 提供适用于 Radix UI、Base UI 和 React Aria 的即插即用动画原语，页面标示支持 React、Vue。
- ⚡ 支持 npm、pnpm、yarn、bun，通过 `npx @animate-ui/cli@latest animate all` 等命令快速启用。
- 🎛️ 可交互示例覆盖 Switch、Tabs、Accordion、Checkbox、Sliding Number、Radio Group、Icons、Toast、Progress。
- ♿ 每个原语保留所属库的无障碍能力，并支持自定义样式与动画。
- 🤖 提供 Animate UI skill：用自然语言描述动效需求，AI 代理会识别组件底层、选择最短路径并应用弹簧动画、检查细节。
- 🛠️ 该技能适用于 Claude Code、Cursor、Codex 等可读取 skills 的代理，可用 `npx skills add imskyleen/animate-ui` 安装。
- 🔍 支持通过 CLI 进行审计，作者为 Skyleen，源码在 GitHub，页面提供文档与 v1 信息。

---

### [Astryx 设计系统](https://astryx.atmeta.com/?ref=tailwindweekly.com)

**原文标题**: [Astryx Design System](https://astryx.atmeta.com/?ref=tailwindweekly.com)

内容仅为一句询问订单去向的话，未提供更多背景或细节。

- 📦 表达用户想知道自己的订单在哪里
- ❓ 核心诉求是查询订单状态或配送进度
- ⏳ 缺少订单号、物流信息等可帮助查询的具体内容

---

### [Shadcn 安装指南 | Video.js](https://videojs.org/docs/guides/installation/shadcn?ref=tailwindweekly.com)

**原文标题**: [Shadcn Installation Guide | Video.js](https://videojs.org/docs/guides/installation/shadcn?ref=tailwindweekly.com)

本文是 Video.js 的 Shadcn 安装指南，讲解如何通过 Shadcn registry 将可编辑的 React 或 HTML 皮肤源码（组件、布局、样式和交互）复制到项目中，并按框架、用例、皮肤、媒体源和样式完成播放器配置与运行。

- 🎯 核心目标：让开发者像修改普通源码一样审查和定制 Video.js 皮肤，而不是只能使用打包好的成品皮肤。
- 🔁 支持迁移：可从 Video.js 8、Mux Player、Plyr、Media Chrome、Vidstack、Video-React 等迁移到 Video.js v10，并提供 React/HTML 迁移指南。
- 🤖 AI Quickstart：运行 `npx @videojs/cli agents skills` 安装技能；React 用 `--framework react`，HTML 用 `--framework html` 初始化。
- 🧭 决策顺序：先检查项目与包管理器，再选择新/现有项目、播放器用例、皮肤、媒体适配器、扩展、安装方式、样式，最后确认并传入全部参数。
- 🧩 框架与模板：React 支持 Next、Vite、TanStack Start、React Router、Astro、Laravel；HTML 支持 Vite、Astro、Laravel。
- 🎨 皮肤选项：Default 现代磨砂外观；Neutral 干净纯色表面；Compat 兼容性更广；Scaffold 用于自建皮肤线框。
- 📺 用例与媒体：Video 支持 HTML5、HLS、DASH、Mux、Vimeo、YouTube、Cloudflare、TikTok、Twitch；Audio 支持 HTML5 Audio、Mux Audio、Spotify；另有 Live Video/Audio。
- ⚙️ 重要参数：`framework`、`project`、`preset`、`skin`、`media`、`extensions`、`source-url`、`package-manager`、`template`、`styling`。
- 🧱 配置准备：安装前先提交工作；配置 `components.json` 及 `aliases.components`；React 可运行 Shadcn 初始化，HTML 需配置 `tsconfig.json`、`vite.config.ts` 和 `components.json`。
- 📥 添加源码：先注册 `@videojs` registry，再用 `shadcn add @videojs/video|audio|live-video|live-audio --overwrite --yes` 添加皮肤源码。
- 📁 文件位置：源码添加到 `<components alias>/videojs/<preset>`，React 同时安装 `@videojs/react`，HTML 同时安装 `@videojs/html`。
- ▶️ 接入播放器：React 导入 `VideoPlayer`、`Video` 和皮肤组件；HTML 修改 `skin.html`、创建 `src/player.ts` 并在 `index.html` 中使用 `<video-player>`。
- 🚀 运行验证：执行开发服务器命令，确认所选媒体可播放；之后从 `skin.tsx` 或 `skin.html` 开始定制布局、颜色、控件和交互。
- 🔧 扩展与注意：Mux 视频/音频默认启用 Mux Data；需要投屏时可选 Google Cast；无需扩展用 `none`；无媒体 URL 时用 `source-url=demo`。
- 📚 后续方向：可继续自定义皮肤与 UI 组件、构建自定义控件、部署、检查浏览器支持、TypeScript、打包器兼容性和 CSP。

---

### [发布 v4.10.0 · schoero/eslint-plugin-better-tailwindcss · GitHub](https://github.com/schoero/eslint-plugin-better-tailwindcss/releases/tag/v4.10.0?ref=tailwindweekly.com)

**原文标题**: [Release v4.10.0 · schoero/eslint-plugin-better-tailwindcss · GitHub](https://github.com/schoero/eslint-plugin-better-tailwindcss/releases/tag/v4.10.0?ref=tailwindweekly.com)

eslint-plugin-better-tailwindcss 发布 v4.10.0，汇总了 HTML 模板支持、canonical classes 修复、文档更新及维护性改动。

- 🚀 发布最新版本 v4.10.0，发布于 10 月 19 日 19:18，包含合入 main 的 7 个提交。
- ✨ 新增 HTML 模板支持（#429）。
- 🛠️ 修复 canonical classes 中的原型键处理问题（#423）。
- 📘 文档更新：展示绝对 cwd 配置示例（#424）。
- 🧹 维护更新：更新 issue 模板。
- ❤️ 贡献者包括 Langning Zhang（@Boulea7）。
- 📦 该版本包含 2 个资源附件。

---

### [](https://github.com/uni-stack/uniwind/releases/tag/v1.13.0?ref=tailwindweekly.com)

**原文标题**: [Release Release v1.13.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.13.0?ref=tailwindweekly.com)

uniwind 仓库发布 v1.13.0（最新版本，10 月 19 日），包含自 v1.12.2 以来的 4 次提交。本次更新主要新增原生样式匹配谓词生成和原生端 CSS 级联顺序支持，并修复导出、测试主题、字体变体及 Metro 热重载相关问题，同时完成样式元数据重构和 CI 发布流程改进。

- 🚀 新功能：生成原生样式匹配谓词（#725）
- 🎨 新功能：在原生端遵循 CSS 级联顺序（#722）
- 🐛 修复：从原生组件入口转发所有 React Native 导出（#740）
- 🧪 修复：避免测试主题进入已发布的 uniwind.css（#718）
- 🔤 修复：移除字体变体中的空值（#729）
- 🔥 修复：Metro 跟踪导入的 CSS 依赖以支持热重载（#676）
- 🔧 重构：将样式元数据与声明分离（#723）
- ⚙️ 其他：改进 CI 发布流程（#715）
- 🎉 新贡献者：@fendyk 首次贡献（#676）
- 👥 贡献者包括 dlebedynskyi、jpudysz 等 4 人
- 📦 完整变更对比：v1.12.2...v1.13.0

---

### [GitHub - 20](https://github.com/20lives/tailwindcss-rtl?ref=tailwindweekly.com)

**原文标题**: [GitHub - 20lives/tailwindcss-rtl at tailwindweekly.com · GitHub](https://github.com/20lives/tailwindcss-rtl?ref=tailwindweekly.com)

tailwindcss-rtl 是一个为 Tailwind CSS 提供双向布局支持的插件，通过方向感知的逻辑工具类，让同一套样式同时适配 RTL 与 LTR。它兼容 Tailwind CSS 3.0–3.4 和 4.x，只补充当前 Tailwind 版本缺失的类，不覆盖核心输出，并提供 TypeScript 类型、ESM 与 CJS 支持。

- 🎯 核心用途：用 `ps-6`、`ms-4`、`start-0` 等逻辑类替代 `pl-6`、`mr-4`、`left-0`，避免为 RTL 单独编写一套样式。
- 🧭 使用方式：在 RTL 页面给 `<html>` 添加 `dir="rtl"`；LTR 是默认方向，无需设置 `dir="ltr"`。
- 🧩 与 Tailwind 核心分工：Tailwind 3.1/3.3/3.4/4.0/4.2 已逐步内置部分逻辑类；插件仅在当前版本缺失时生成补充类，从不覆盖核心输出。
- ➕ 插件专属能力：包括 `rounded-ts/te/bs/be-*`、`space-s-*`、`divide-s-*`、`origin-start/end` 及角变体、`bg-start/end` 及角变体、`translate-s-*`/`translate-e-*`、`forms` 选项等。
- 📦 安装：可通过 pnpm、npm、yarn 或 bun 以开发依赖安装 `tailwindcss-rtl`。
- ⚙️ 配置：Tailwind v4 在 CSS 中使用 `@plugin "tailwindcss-rtl"`；Tailwind v3 在 `tailwind.config.js` 的 `plugins` 中注册；支持传入 `forms` 选项。
- 🔁 嵌套方向：方向读取最近的 `dir` 属性，因此可在 RTL 页面中用 `dir="ltr"` 保持代码示例、导航等局部 LTR。
- 🛠️ 工具类范围：涵盖文本对齐、margin/padding、inset、圆角、边框、float/clear、space/divide、transform origin、背景定位、translate 等；支持主题值、任意值和合理场景下的负值。
- 🧾 `forms` 选项：用于镜像 `@tailwindcss/forms` 的 select 箭头及内边距，支持 `true`、`"base"`、`"class"`，需在 forms 插件之后注册。
- 🌐 浏览器支持：`origin-*`、`bg-*`、`translate-s/e-*` 和 `forms` 使用 `:dir()`，需 Chrome 120+、Safari 16.4+、Firefox 49+；旧浏览器会回退到 LTR 值。
- 🚀 迁移到 1.0：保留 0.x 类名；不再支持 Tailwind 2 及更早版本（继续用 0.9）；移除 `[dir]` 选择器，每个工具类为单类选择器，响应式和状态变体可正常覆盖。
- 🧪 开发与发布：提供 `pnpm test/lint/typecheck/check/smoke` 等脚本；发布需更新版本与 CHANGELOG，推送 `vX.Y.Z` 标签，由 Release workflow 发布到 npm。
- 📄 许可证：MIT；仓库还提供官方 Workcation i18n/RTL 实时演示。

---

### [Todowing — 为 Todoist 提供嵌套子任务及更多功能](https://todowing.com/?ref=tailwindweekly.com)

**原文标题**: [Todowing — Nested Sub-tasks & More for Todoist](https://todowing.com/?ref=tailwindweekly.com)

Todowing 是一款 Chrome 扩展，为 Todoist 补回被日期与筛选视图扁平化隐藏的子任务层级，并提供专注计时、时间估计、笔记、主题字体和 Apple 日历等增强；采用一次性付费 19.99 美元解锁，同时提供免费层。

- 🧩 产品定位：在 Todoist 中恢复内联、最多四级的子任务树，覆盖 Today、Upcoming、Filters、Labels 和 Boards。
- 📥 解决痛点：Todoist 在部分视图只显示父任务，子任务被隐藏；Todowing 让子任务连同日期、优先级和标签直接显示在行内。
- ✅ 免费层：包含完整嵌套展示、子任务完成/重开、每行详情、七种配色和文字大小滑块，但每个顶级任务最多显示 5 个子任务行。
- 🔓 付费解锁：无限子任务行、行内添加/重命名/拖拽排序、隐藏已完成子任务，以及跨项目“一任务两处”。
- ⏱️ 专注功能：从 Today 选择任务启动计时器，计时卡在列表旁倒计时，并跨所有打开的标签页运行。
- 🕒 时间估计：可在任务行内输入预计时长，并在视图标题和专注会话中汇总。
- 📝 其他增强：Today 列表上方有三行 Markdown 笔记板；可选择 50 种 Google Fonts；可将 Apple Calendar 事件显示在 Today 旁，最多 5 个日历。
- 💳 定价：一次性支付 19.99 美元，无订阅、无续费；前 50 名中 27 个已认领，之后为 29.99 美元；14 天内无理由退款。
- 🔁 未来升级：新功能会加入同一扩展，已购买解锁覆盖未来付费升级。
- 🌐 平台限制：仅支持 Chrome 中的 Todoist Web；不支持 Todoist 下载版桌面应用，可通过 Chrome 将页面安装为应用窗口使用。
- 🔒 隐私：Todoist API token 仅存于浏览器并直连官方 Todoist API，任务不经过其服务器，扩展内无分析或追踪。
- 💬 用户反馈：用户尤其认可子任务重回 Today 视图，以及意外实用的专注计时器。
- ❓ FAQ 重点：无需 Todoist Pro；许可证服务器故障或离线时仍保持解锁。

---

### [Blue-500 中的 500 是什么意思 · hipuku](https://www.hipuku.dev/writing/what-the-500-in-blue-500-means?ref=tailwindweekly.com)

**原文标题**: [What the 500 in Blue-500 Means · hipuku](https://www.hipuku.dev/writing/what-the-500-in-blue-500-means?ref=tailwindweekly.com)

本文解释设计系统中颜色编号（如 blue-500）并非跨色系统一含义；不同调色板用编号表示色阶位置、对比度等级、感知亮度或用途角色，因此同一编号在不同色相或系统中可能对应不同亮度和 WCAG 对比度，进而影响按钮文字可读性与设计规范的可复用性。

- 🎨 大多数设计系统把每种色相做成从浅到深的色阶，并用数字标记；Tailwind 的 blue-50 到 blue-950 常被设计师、工程师和评审共同引用。
- ⚠️ 数字相同不代表亮度和对比度相同：Tailwind v3 中白字在 bg-blue-600 上对比度为 5.17:1，通过 AA；白字在 bg-green-600 上仅 3.30:1，不通过。
- 📐 编号至少有四种用法：表示色阶位置（Material 2014、Tailwind）、表示对比度等级（Carbon、USWDS、Stripe）、表示测量亮度（Material 3 的 tone）、表示用途角色（Radix 的 step）。
- 🧱 Material 2014 用 50–900 表示位置，并建议把 500 作为主色；Tailwind 借用该数字体系并扩展到 50 和 950，但编号仍主要表示色相内的位置。
- 🌈 由于 HSL 亮度不符合人眼感知，黄色和蓝色即使 HSL 亮度相同，感知亮度也差异很大；用 OKLCH 看 Tailwind v3 的 500 色阶，indigo 约为 0.585，yellow 约为 0.795。
- 🔍 在 Tailwind 中，“200 文字配 700 背景”并非所有色相都通过 AA；17 个色系里有 12 个失败，说明按编号写死的规则需要逐色检查。
- 🧮 Carbon 用 10–100 编号，并规定等级差 ≥50 即满足可访问性；USWDS 用“magic number”40/50/70 分别对应大字号 AA、正文 AA、AAA，并通过统一亮度让规则跨色系成立。
- 🟡 统一亮度有代价：USWDS yellow-50 和 Material 3 yellow tone 40 变成深橄榄色，而 Tailwind yellow-500 仍是亮黄色，因为前者按亮度定义等级，后者按位置编号。
- 🧩 Material 3 用 HCT/CIELAB tone 从 0 到 100 编号，tone 差 40 保证至少 3:1，差 50 保证至少 4.5:1；Radix 则按角色编号，step 11/12 为文本并保证 APCA Lc 60/90。
- ⚖️ WCAG 2 用相对亮度公式计算对比度；APCA 对同一灰色在白色和黑色背景上的评分差异很大，且 WCAG 3 尚未确定最终对比度算法。
- 🚀 Tailwind v4 改用 OKLCH，基本保持 v3 亮度不变、主要提高饱和度，因此多数对比度变化很小；blue-600 上白字从 5.17:1 变为 5.26:1。
- 🧠 结论：blue-500 的含义取决于调色板的设计决策；若编号只表示位置，就不能把“200 on 700”这类规范当成跨色相通用规则，只有明确编号衡量什么并让所有颜色适配，规则才可复用。

---

### [拖垮性能的两行 CSS（从 120fps 降至 40fps）](https://component-odyssey.com/articles/13-improving-performance-by-changing-two-lines-of-css?ref=tailwindweekly.com)

**原文标题**: [The Two Lines of CSS That Tanked Performance (120fps to 40fps)](https://component-odyssey.com/articles/13-improving-performance-by-changing-two-lines-of-css?ref=tailwindweekly.com)

仅从标题可概括：这篇文章讨论一个前端性能案例——两行 CSS 代码使页面帧率从 120fps 骤降到 40fps，凸显 CSS 对渲染性能的潜在影响。

- ⚠️ 核心事件：两行 CSS 引发明显性能退化。
- 📉 关键指标：帧率由 120fps 降至 40fps。
- 🧠 技术启示：看似简单的样式也可能触发高开销的渲染路径。
- 🔍 排查方向：应使用浏览器性能工具定位耗时样式与重绘/重排。
- 🛠️ 优化建议：精简或替换高成本 CSS，避免不必要的渲染负担。

---

### [停止使用 :invalid 和 :valid 伪类，改用这个！ - YouTube](https://www.youtube.com/watch?v=fST4hhWE6y8&ref=tailwindweekly.com)

**原文标题**: [Stop Using :invalid and :valid Pseudo-Classes. Use THIS Instead! - YouTube](https://www.youtube.com/watch?v=fST4hhWE6y8&ref=tailwindweekly.com)

该内容为 YouTube 页面底部的导航与版权信息，涵盖平台介绍、联系渠道、创作者与广告/开发者资源，以及条款、隐私、安全等法律链接，并标注 © 2026 Google LLC。

- 🏢 提供“关于”“新闻”“联系我们”等平台与公司信息入口。
- 🎬 面向创作者、广告主和开发者提供相关资源与入口。
- ⚖️ 包含版权、条款、隐私及政策与安全等法律与合规链接。
- ⚙️ 提供“YouTube 如何运作”和“测试新功能”等平台机制与功能入口。
- ©️ 页面底部标注版权归属为 © 2026 Google LLC。

---

### [SEO Gets | 强大得惊人的 GSC + GA4 分析](https://seogets.com/?ref=tailwindweekly.com)

**原文标题**: [SEO Gets | Shockingly Powerful GSC + GA4 Analytics](https://seogets.com/?ref=tailwindweekly.com)

SEO Gets 是一款面向 SEO 从业者的 GSC+GA4 分析工具，旨在消除使用 Google Search Console 时的挫败感，提供更高数据上限、一体化仪表盘和隐私保护，并覆盖分析、策略、跟踪与报告全流程。它已获得 4,000+ SEO 专业人士信任，可免费连接 GSC，核心站点按月收费。

- 🚀 解决 GSC 痛点：免费连接 GSC，支持最多 50,000 行数据，对比 GSC 的 1,000 行限制。
- 📊 一个仪表盘管理所有属性，集中查看关键 SEO 指标，减少在 GSC、GA4 和多个标签页间切换。
- 🔒 隐私优先：不售卖、不跟踪、不访问用户数据；FAQ 说明仅临时保存可撤销的 Google 密钥。
- 🧠 分析功能包括 Master Dashboard、可接入 Claude/ChatGPT 的 MCP Server，以及按意图、主题或漏斗阶段一键生成优先内容组。
- 🎯 策略功能包括发现接近顶部排名的关键词、识别页面蚕食问题、发现内容衰退并及时优化。
- 🛠️ 跟踪功能支持监测最多 5,000 个页面的索引状态，并通过 Chrome 扩展记录页面改动内容、时间和原因。
- 📈 报告功能提供每周分析摘要邮件、实时客户门户和变更前后 SEO 测试，减少截图与重复制作报告。
- 👥 适用于 SEO 机构、顾问和内部 SEO 团队，并展示多位行业人士的使用好评。
- 💳 定价为核心站点每月 49 美元，额外核心站点每个 4 美元，达到 35 个站点后不限量；免费站点永久免费且无需信用卡。
- ✅ 每个核心站点包含人工入门指导、人工客服、GA4 分析、机会与行动报告、内容组/主题集群、注释与 Google 更新、SEO 测试、白标客户门户和 MCP 访问等。

---

### [shadercn - 精美的着色器，化繁为简](https://www.shadercn.run/?ref=tailwindweekly.com)

**原文标题**: [shadercn - Beautiful shaders, made simple](https://www.shadercn.run/?ref=tailwindweekly.com)

面向 React 的 WebGPU/WGSL 着色器组件库，主打“漂亮着色器，简单实现”。它基于 vgpu 与 TypeGPU 构建，通过 shadcn 分发，并提供组件浏览、安装命令与 Playground 预览。

- 🎨 核心定位：为 React 提供易用的 WebGPU/WGSL 着色器组件，降低高质量视觉效果的使用门槛。
- ⚙️ 技术基础：构建于 vgpu 和 TypeGPU 之上，采用 WebGPU/WGSL 实现着色器效果。
- 📦 分发方式：通过 shadcn 分发，支持使用 bun、npm、pnpm、yarn 等包管理器。
- 🚀 快速安装：可使用 `pnpm dlx shadcn add @shadercn/orb`，单个组件示例为 `npx shadcn@latest add @shadercn/orb-01`。
- 🧩 组件内容：提供 ORB-01 至 ORB-33 共 33 个球体着色器组件，每个组件对应独立视觉效果。
- 🌈 视觉风格：涵盖切面玻璃球、彩虹光带、等离子球、体素球、ASCII 矩阵、Minecraft Earth、星系、热成像等多种效果。
- 🖥️ 页面功能：包含 Get Started、Browse Components、Choose orb、Add、Copy 等操作入口。
- 🎮 交互预览：提供 Playground，可打开并体验所选着色器组件。

---

### [tiiny.host - 在线分享作品的最简单方式](https://tiiny.host/?fpr=vivian32&ref=tailwindweekly.com)

**原文标题**: [tiiny.host - The simplest way to share your work online](https://tiiny.host/?fpr=vivian32&ref=tailwindweekly.com)

您尚未提供需要总结的文章正文，因此暂时无法生成要点摘要。
- 📄 请补充或粘贴文章内容，我才能进行总结。
- 🧭 收到内容后，我会提炼关键信息与核心结论。
- 📝 输出将采用简洁的中文要点列表。
- ✅ 每条要点会使用“-”符号并配上合适 emoji。

---

### [获取失败](https://hilium.app/?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://hilium.app/?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 403。

---

### [Aura - 免费在线矢量编辑器](https://deslove.com/online-vector-editor?ref=tailwindweekly.com)

**原文标题**: [Aura - Free Online Vector Editor](https://deslove.com/online-vector-editor?ref=tailwindweekly.com)

Aura 是 Deslove 推出的免费在线矢量编辑器，可直接在浏览器中创建和编辑 logo、SVG 与矢量图形，无需安装；同时提供 Windows 桌面版，内置形状、字体和配色库，并支持多种矢量格式的导入与导出。

- 🖥️ 免费在线使用：网页版无需安装、无需注册账号即可试用绘图工具，Windows 版可从微软商店获取。
- ✏️ 核心编辑能力：支持矢量路径、贝塞尔曲线、节点与手柄编辑，以及形状联合、相减、路径拆分和描边转形状。
- 🔤 文字处理：可调整字距与字偶距，让文字沿路径排列，也可将文字转为轮廓后逐字调整。
- 🗂️ 图层与画板：支持编组，以及命名、隐藏和锁定图层，并提供蒙版、渐变、参考线和多画板。
- 🧩 Shape Lab：内置 141 个现成的几何构图，可调整模块、间距、变形、旋转和圆角半径，生成可编辑的矢量形状。
- 🔡 字体库：包含 450 个字体家族，全部遵循 SIL OFL，可免费用于个人和商业设计。
- 🎨 调色板：包含 500 套现成配色，支持按色相和情绪查找、HEX 搜索、收藏与复制色值。
- 📥 导入格式：支持 AURA、SVG/SVGZ、FIG、PDF、AI、EPS、CDR 等，兼容性取决于源文件所用特性。
- 📤 导出格式：可保存 AURA 工程文件，并导出 SVG/SVGZ、PDF、EPS、PNG、JPEG、WebP 等成品。
- ⚠️ 格式限制：导入的文本可能转为轮廓，嵌入图片不会自动矢量化，不保证第三方格式无损往返。
- 🖼️ 模板示例：提供 logo、图标集、海报等示例，无需账号即可编辑，登录后可保存和导出作品。
- 💾 账号与存储：打开自有文件、保存项目和导出需免费 Deslove 账号；草稿存于本机设备，不属于云端备份。
- 🪟 Windows 版：首次使用需账号激活，之后可在本地离线编辑和转换文档。
- 📱 平台支持：目前仅有网页版和 Windows 桌面版，暂无 macOS、iOS、Android 专属应用。

---

### [动态视频灵感 | MotionVideo](https://motionvideo.xyz/?ref=tailwindweekly.com)

**原文标题**: [Motion video inspiration | MotionVideo](https://motionvideo.xyz/?ref=tailwindweekly.com)

这是一个展示 AI 生成动态视频及其背后提示词与技能的合集页面，鼓励用户浏览、寻找灵感并创作自己的版本。内容涵盖各类动态设计、产品宣传、解释视频与创意动画示例。

- 🎬 汇集大量 AI 制作的动态视频案例，覆盖展示片、产品发布、品牌广告与创意短片。
- ✨ 每个案例都附带可参考的 Prompt，方便用户学习并改造成自己的作品。
- 🧠 示例主题丰富，包括动态字体、UI 状态变形、角色循环动画、产品宣传、历史与科普解释等。
- 🛠️ 页面还突出“Skill”内容，例如 Cinetic skill launch film，展示技能型动态设计案例。
- 🚀 提供“Surprise me”和“Submit a video”等入口，鼓励探索与投稿。
- 🏷️ 列表中包含赞助内容，如 Shadcn Labs，体现商业合作或推广展示。

---
