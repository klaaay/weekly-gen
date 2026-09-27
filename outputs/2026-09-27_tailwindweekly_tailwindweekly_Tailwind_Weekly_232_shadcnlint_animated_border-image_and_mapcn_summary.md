### [](https://github.com/shadcn-ui/lint?ref=tailwindweekly.com)

**原文标题**: [GitHub - shadcn-ui/lint at tailwindweekly.com · GitHub](https://github.com/shadcn-ui/lint?ref=tailwindweekly.com)

@shadcn/lint 是一个面向 Tailwind 设计系统的 agent-first linter，让代理按你定义的规则验证 UI 写法；它支持 Tailwind v4、ESLint/Oxlint、React/Vue/Svelte，且不要求使用 shadcn/ui，错误会基于组件、变体和主题给出修复建议。

- 🎯 @shadcn/lint 让团队用规则定义设计系统允许的写法，代理可运行 lint 检查自己的改动。
- 🧩 适配现有 Tailwind 设计系统，无需重写；支持 ESLint 与 Oxlint，以及 React、Vue、Svelte。
- ✍️ 当代理违规时，错误不仅指出问题，还会结合你的组件、变体、主题建议如何修复。
- 🧠 相比 TypeScript 类型限制只告诉代理“不允许”，该工具会进一步告诉代理“应该用什么”。
- ⚙️ 可配置组件契约，例如 Button 允许 margin 和全宽，但不允许 padding、圆角、固定高宽。
- 🧱 支持按组件名分别设置规则，如 CardTitle 可改排版但不能改字体，CardContent 可改间距但不能改排版。
- 🎨 可结合 no-arbitrary-values 要求间距使用主题比例，禁止 md:p-[13px] 这类任意值。
- 🤖 为写 UI 的代理设计：错误说明哪里坏了、该用什么、去哪里找可用的尺寸、变体或主题值。
- 📊 在 150+ 任务运行中测试，几乎每个任务一轮纠正后达到零违规；示例中多个模型完成 8/8 任务且错误归零。
- 💰 Claude 对照运行显示，使用 lint 反馈修复违规比仅靠规则便宜 10%–48%。
- 🔧 linter 可编程：不改组件即可写规则，同一组件可在不同项目使用不同契约，也可覆盖第三方组件。
- 💬 支持自定义错误消息，例如提示“使用 size prop 而不是 padding”。
- 🏷️ 支持消息占位符，如 {{sizes}}、{{component}}、{{file}}，可引用可用尺寸、组件名和主题文件路径。
- 📏 内置规则包括 no-restyle、no-raw-colors、no-arbitrary-values、no-inline-styles、no-unknown-classes、require-static-classes。
- 🚀 快速开始：让代理读取 SETUP.md 并安装，或自行配置；要求 Node.js 20.19+，ESLint 9.30+ 或 Oxlint 1.80+。
- 🛠️ 安装后在 ESLint/Oxlint 配置中加入插件和规则，将 eslint . 或 oxlint 设为 lint 脚本，并在 AGENTS.md 中要求代理改动后运行修复。
- 🧭 React、Vue、Svelte 共用规则、选项、契约和消息；动态元素应用 token 规则但不应用 no-restyle。
- ⚙️ 通过 settings.shadcn 配置 ui、componentImports、ignoreImports、mergeFunctions、variantFunctions、note；无 shadcn/ui 也可用。
- 🏢 Monorepo 可使用 workspace 包导入前缀，并对 packages/ui/src/components/** 覆盖或关闭规则。
- 📚 提供文档、贡献指南与 MIT 许可证；仓库约有 2.8k stars、53 forks、24 commits。

---

### [](https://www.youtube.com/watch?v=tPQgw_DPIoM&ref=tailwindweekly.com)

**原文标题**: [Shadcn Just Fixed Tailwind's Biggest Problem - YouTube](https://www.youtube.com/watch?v=tPQgw_DPIoM&ref=tailwindweekly.com)

本内容为 YouTube 页脚导航与版权信息，主要列出平台介绍、联系与合作入口、法律政策、功能说明及版权归属。

- ℹ️ About / Press：了解 YouTube 介绍与新闻动态。
- 📞 Copyright / Contact us：提供版权事务与联系方式入口。
- 🎬 Creators / Advertise / Developers：面向创作者、广告主和开发者的资源入口。
- 📜 Terms / Privacy / Policy & Safety：展示使用条款、隐私政策与安全政策。
- ⚙️ How YouTube works / Test new features：说明 YouTube 运作方式并测试新功能。
- ©️ © 2026 Google LLC：版权归 Google LLC 所有。

---

### [发布 cn@0.4.0 · shadcn-ui/cn · GitHub](https://github.com/shadcn-ui/cn/releases/tag/cn%400.4.0?ref=tailwindweekly.com)

**原文标题**: [Release cn@0.4.0 · shadcn-ui/cn · GitHub](https://github.com/shadcn-ui/cn/releases/tag/cn%400.4.0?ref=tailwindweekly.com)

shadcn-ui/cn 是一个公开 GitHub 仓库，最新发布版本为 cn@0.4.0；此次小版本更新由 github-actions 于 9 月 22 日发布，核心变化是让 cn build 和插件注册 Tailwind CSS 中声明的主题尺度。

- 📦 仓库：shadcn-ui/cn，公开。
- ⭐ 社区数据：Star 1.6k，Fork 17。
- 🧾 待处理：Issues 3，Pull requests 2。
- 🚀 最新版本：cn@0.4.0。
- 📅 发布时间：9 月 22 日 10:41，发布者 github-actions。
- 🔀 自该版本以来，main 分支有 1 个提交。
- 🔐 提交 84db832 已通过 GitHub 验证签名，GPG key ID：B5690EEEBB952194。
- 🛠️ 小版本变更：#153（2691a38），感谢 @shadcn。
- ✨ cn build 和插件现在会注册 Tailwind CSS 中声明的 theme scales。
- 📎 发布附带 2 个 Assets。
- ⚠️ 页面部分发布/标签筛选内容加载出错，提示需刷新。

---

### [](https://github.com/JJBeta-Dev/tailwind-strict-colors?ref=tailwindweekly.com)

**原文标题**: [GitHub - JJBeta-Dev/tailwind-strict-colors at tailwindweekly.com · GitHub](https://github.com/JJBeta-Dev/tailwind-strict-colors?ref=tailwindweekly.com)

Tailwind Strict Colors 是 JJBeta-Dev 开发的 VS Code/Antigravity 扩展，用于检测 Tailwind CSS v4 中使用默认调色板的“硬编码”颜色类，并依据项目 @theme 中的 --color-* token 给出替换建议；它直接解析 CSS，不依赖 ESLint 或根配置文件。  
- 🎯 核心目标：将 bg-red-500、text-gray-200、border-white 等默认色类替换为自定义设计 token。  
- 📦 安装方式：从 Releases 下载 .vsix，在 VS Code/Antigravity 中通过 Extensions → ... → Install from VSIX 安装。  
- 🔍 工作方式：按 themeFileGlob（默认 **/index.css）查找 CSS，提取 @theme 内所有 --color-* 声明。  
- 🗂 扫描范围：默认检查 jsx/tsx/html/vue/svelte/astro 等语言，覆盖 bg-、text-、border-、ring-、fill- 等工具类。  
- ⚠️ 诊断提示：违规类会在 Problems 面板和编辑器中显示黄色波浪线警告。  
- 💡 修复入口：提供 Quick Fix，最多显示 maxSuggestions（默认 5）个建议。  
- 🖱 Hover 提示：悬停显示颜色 swatch、建议 token 和快速替换链接。  
- 🪄 Fix All：支持一次替换当前文件或整个工作区中的违规颜色。  
- 🧭 侧边栏面板：扫描整个项目，按文件分组展示结果，支持搜索与点击跳转。  
- 🎨 排序逻辑：可解析 hex/rgb/var 时按真实颜色距离排序；oklch/color-mix 等则按 danger、warning、success 等语义匹配。  
- 🛠 开发命令：npm run build/watch/typecheck/test/lint/format/format:check/verify。  
- 🤖 CI：GitHub Actions 在每次 push/PR 运行 verify，并打包 .vsix。  
- ⚙️ 配置项：enable、themeFileGlob、languages、utilities、ignoredColorNames、maxSuggestions。  
- 🧱 代码结构：src/ 包含配置、调色板、CSS 解析、扫描、诊断、Quick Fix、Hover、Fix All、Webview 等模块；example/ 用于 F5 调试。  
- 🚧 已知限制：v1 只能解析 hex、rgb/rgba 和 var 链；oklch/hsl/color-mix 仅按语义排序；使用正则而非完整 JSX/Vue/Svelte 解析器，但可覆盖 className、class、clsx()、cva() 等。  
- 📄 许可：MIT，CLAUDE.md 提供架构、数据流与设计决策说明。

---

### [](https://reactbits.dev/?ref=tailwindweekly.com)

**原文标题**: [React Bits - Animated UI Components For React](https://reactbits.dev/?ref=tailwindweekly.com)

未检测到需要总结的文本内容，因此暂时无法生成有效摘要。

- 📭 请补充或粘贴需要总结的文章内容。
- 🧾 收到内容后，我会提取关键信息并精简为要点。
- ✨ 每条要点将使用“-”符号和合适的表情符号。
- 🀄 最终输出将使用中文。

---

### [Vue Bits - 适用于 Vue 的动画 UI 组件](https://vue-bits.dev/?ref=tailwindweekly.com)

**原文标题**: [Vue Bits - Animated UI Components For Vue](https://vue-bits.dev/?ref=tailwindweekly.com)

未收到可总结的正文内容，因此暂时无法生成摘要。请粘贴需要总结的文章文本，我会按中文输出概览与要点列表。

- 📄 当前缺少待总结的文本，无法提取关键信息。
- ✍️ 请提供原文后，我将生成简洁的中文摘要。
- ✅ 输出会使用“-”要点列表，并为每条要点搭配合适的 emoji。
- 📌 摘要将包含概览总结和核心信息，确保有效捕捉文章重点。

---

### [任务卡片 | 元素 · assistant-ui](https://www.assistant-ui.com/elements/task-card?ref=tailwindweekly.com)

**原文标题**: [Task card | Elements · assistant-ui](https://www.assistant-ui.com/elements/task-card?ref=tailwindweekly.com)

Task Card 是 assistant-ui 的一个元素组件，用于在对话中把委托任务的状态、计时、结果和转录内容整合为一张可展开的卡片。它支持 React 与 React Native，可通过 CLI 或 shadcn 方式安装，既可搭配 runtime 在 Thread 中自动识别嵌套工具调用并渲染成任务泳道，也可作为纯 props 组件独立使用。

- 🃏 **核心作用**：将委托任务的状态、计时、结果和转录内容整合为一张卡片，让任务进度在对话中清晰可读
- 📱 **跨平台支持**：同时支持 React 和 React Native，CLI 会读取 package.json 自动从对应注册表安装
- 🛠️ **两种安装方式**：可用 `npx assistant-ui@latest add elements-task-card` 或 shadcn 的 `npx shadcn@latest add "@assistant-ui/task-card"`
- 🔌 **运行方式灵活**：搭配 assistant-ui runtime 使用时，Thread 能自动识别嵌套工具调用；独立使用时则需自行提供任务状态、计时、结果与转录内容
- 🧵 **Thread 中启用任务泳道**：通过设置 `components.TaskGroup` 插槽开启，携带嵌套 messages 数组且无注册工具 UI 的工具调用会渲染为卡片
- 📊 **泳道分组**：同级委托以四张卡片为一组，超出显示 "Show N more" 按钮，并附如 "5 tasks · 1 running · 1 failed" 的摘要
- 🎨 **状态可视化**：每个泳道显示状态图标、标签（从 description、task、title 等字段取值）、可选元标签（如 subagent_type、model）以及已用时间
- ⏳ **等待用户时不停滞**：等待用户输入的任务卡片保留审批与恢复控制，并持续计时；失败显示错误文本，取消则标记为已取消
- 📂 **按需挂载转录**：打开卡片时才通过 ReadonlyThreadProvider 挂载嵌套对话，只读线程中不显示审批控制
- 📌 **可手动放置**：注册的工具 UI 优先级高于插槽，可在 toolkit 的 render 中返回绑定的 TaskCard
- 🧩 **独立使用简单**：TaskCard 为纯 props 组件，提供 label、meta、state、elapsed、actions、result、open 及转录子元素即可
- 🏷️ **五种状态**：state 可选 "working"、"waiting"、"done"、"failed"、"cancelled"，决定状态图标与辅助技术暴露的状态

---

### [](https://nuqs.dev/registry?ref=tailwindweekly.com)

**原文标题**: [Shadcn Registry | nuqs](https://nuqs.dev/registry?ref=tailwindweekly.com)

Shadcn Registry 提供通过 shadcn CLI 安装社区自定义解析器、适配器和工具的方式，也支持直接复制代码片段；同时可通过 RSS 跟踪更新。

- 🧩 使用 shadcn CLI 安装社区提供的自定义解析器、适配器与工具。
- 📋 每个条目可按 CLI 说明添加到项目，或直接复制粘贴代码片段。
- ⚙️ 社区适配器 Inertia.js：现代单体方案，常搭配 Laravel、Phoenix、Django、Rails 等非 JS 后端。
- ⚛️ One.js：旨在用 React 和 React Native 更简单、更快速地构建 Web 与原生应用。
- 🏮 Waku：极简 React 框架。
- 🚧 Expo Router：即将加入 registry，已在 GitHub 上讨论。
- 🔤 社区解析器 UUID：用于在查询字符串中验证 UUID 字符串（版本 1-8）。
- 📡 订阅 registry 的 RSS 源，及时了解最新变更与新增内容。
- 🧭 Inertia.js 相关：介绍如何在 Inertia.js 应用（例如 Laravel 后端）中使用 nuqs。

---

### [useLayouts | 免费动画 React 组件](https://uselayouts.com/?ref=tailwindweekly.com)

**原文标题**: [useLayouts | Free animated React components](https://uselayouts.com/?ref=tailwindweekly.com)

useLayouts 是一个面向 React 开发者的交互式组件库，旨在用现成、可定制、带动效的组件帮助开发者快速构建既美观又好用的界面，而无需从零实现每个交互，并已获 100+ 开发者信任。

- 🧩 提供丰富组件分类：12+ 布局、14+ 导航、18+ 交互、20+ UI 组件。
- 🧱 布局涵盖 Grid、Bento、Hero、Sections 等。
- 🧭 导航涵盖 Navbar、Tabs、Menu、Sidebar 等。
- 🎛️ 交互涵盖 Hover、Drag、Press、Reveal 等。
- 🪟 UI 涵盖 Cards、Forms、Gallery、Pricing 等。
- ✨ 核心理念是“复制、定制、发布”，使用生产级组件快速落地。
- 🎞️ 动效有意义，服务于反馈、聚焦和流程，而非单纯装饰。
- 🛠️ 源码干净可编辑，可自由替换 token、重设样式，不被抽象层锁死。
- 🚀 从可用模式开始，减少脚手架工作，把精力放在产品本身。
- 🔌 兼容 React、Next.js、TypeScript、Tailwind CSS、Motion、Shadcn、Radix、Lucide 等工具。
- 💬 获得多位开发者、创始人和创作者好评，称其组件精致、动画流畅、开源友好。
- 🧾 示例组件包括 Theme Toggle、Get In Touch、Confidential Folder、Accessible Action、3D Book、Polaroid Stack、Status Button、Bucket、Photo Albums、AccordionOS、Analog Stick、Shake Testimonial 等。
- 📌 页面底部显示版权 © 2026 useLayouts，作者为 0xUrvish。

---

### [](https://www.cozywatch.com/?ref=tailwindweekly.com&aff=lVeE1)

**原文标题**: [Cozy Watch - Clear GitHub Notifications for macOS](https://www.cozywatch.com/?ref=tailwindweekly.com&aff=lVeE1)

Cozy Watch 是一款开源、MIT 许可的 macOS 应用，支持 macOS 12 Monterey 及以上，旨在减少 GitHub 动态和邮件噪音，只在 PR、审查、提及或 CI 更新真正需要你时提醒，帮助你保持专注。个人使用免费，商业使用需付费。

- 📥 下载与平台：提供 macOS 应用下载，开源且采用 MIT 许可。
- 🔔 智能通知：当 pull request、review、mention 或 CI 结果需要你时及时通知。
- 🎯 明确下一步：跳过收件箱分类，直接进入发生变化的 pull request。
- 📊 PR 一览：可从菜单栏和 Cozy Watch 应用查看当前 pull request 状态。
- 🧘 专注设计：不需要你时保持安静，不打扰工作流。
- 🆓 个人免费：所有功能对个人项目和非商业用途永久免费，支持无限仓库和全部通知类型。
- 💼 商业授权：工作、客户项目、企业或非营利组织使用需 $29/年，含 30 天商业试用和许可管理。
- 🔐 开源私密：隐私优先，可随时查看源代码；商业许可通过 Lemon Squeezy 安全销售。
- 🔄 持续更新：更新日志如 0.8.6 修复 PR 缓存、大量仓库 DNS 错误，迁移 GitHub App，并优化仓库选择性能。
- 📨 社区与订阅：被 Uneed 推荐，提供 newsletter 更新，无 GitHub 噪音和垃圾邮件。

---

### [](https://www.cozywatch.com/download/?ref=tailwindweekly.com&aff=lVeE1)

**原文标题**: [Download | Cozy Watch](https://www.cozywatch.com/download/?ref=tailwindweekly.com&aff=lVeE1)

Cozy Watch 是一款面向 macOS 的桌面应用，让你无需一直泡在 GitHub 收件箱里，也能随时掌握拉取请求、评审、提及和 CI 更新。它提供功能、定价、更新日志、GitHub App 与下载等入口，并按年销售商业许可证。
- 🖥️ 为 macOS 打造的 Cozy Watch，旨在以更愉悦的方式管理 GitHub pull requests。
- 🔔 集中掌握 pull requests、reviews、mentions 与 CI updates，减少对 GitHub 收件箱的依赖。
- ⬇️ 提供最新版下载，支持 Apple Universal。
- 💰 商业许可证按年收费，价格为 29 美元。
- 🍎 要求 macOS 12 Monterey 或更高版本。
- 🗂️ 可浏览所有发布版本，并在 GitHub 查看源代码。
- 📧 可通过加入邮件列表跟进 Cozy Watch 动态。
- 🧭 站点导航包括首页、关于、下载、源代码、GitHub App、路线图、EULA、条款、隐私政策、更新日志、博客、联盟计划与招聘。
- 🐦 社交账号为 @cozy_watch。
- 📜 开源项目，采用 MIT 许可证；标语称“Made in a cozy armchair”。

---

### [请稍等……](https://css-tricks.com/animating-css-border-image/?ref=tailwindweekly.com)

**原文标题**: [One moment, please...](https://css-tricks.com/animating-css-border-image/?ref=tailwindweekly.com)

该文本仅为网页加载与验证提示，表示请求正在被验证，请用户稍候，未包含具体文章内容。

- ⏳ 当前状态为加载器（Loader）显示中
- 🛡️ 系统正在验证用户请求
- ⏸️ 用户需要等待验证完成
- 📄 没有可供进一步总结的正文或主题信息

---

### [](https://dbushell.com/2026/07/03/fixing-full-bleed-css/?ref=tailwindweekly.com)

**原文标题**: [Fixing full-bleed CSS â David Bushell â Web Dev (UK)](https://dbushell.com/2026/07/03/fixing-full-bleed-css/?ref=tailwindweekly.com)

本文讨论 full-bleed 全宽 CSS 布局的实现、缺陷与更现代的修复方案：从 `100vw` 工具类出发，指出经典滚动条会导致宽度计算与裁切问题，再逐步引入 `overflow-x`、`scrollbar-gutter`、CSS 容器单位 `cqi`、`@property` 继承，以及对未来容器单位引用语法的期待。

- 🧑‍💻 作者强调自己是前端开发者，不是医生；full-bleed 布局可用 CSS Grid/subgrid 实现，但并非总能将整页网格化。
- 🧩 Andy Bell 的工具类用 `width: 100vw; margin-left: calc(50% - 50vw);` 实现全宽突破。
- ⚠️ 问题在于 `100vw` 可能比实际视口更宽，经典滚动条会占空间，导致两侧轻微裁切、边框或阴影被截断、对齐出现微妙偏移。
- 🪟 在 Windows 或 macOS“始终显示滚动条”设置下更容易复现；作者建议在这些环境测试。
- 🩹 部分修复：`body { overflow-x: hidden; }`，或 `html { scrollbar-gutter: stable; }`；后者在无需垂直滚动时可能显得奇怪。
- 📦 现代方案：用 CSS containment 把 `body` 设为容器：`container: body / inline-size; overflow-x: clip;`，再用容器单位替换视口单位。
- 📐 `.full-bleed` 可改为 `inline-size: 100cqi; margin-inline-start: calc(50% - 50cqi);`；隐藏溢出不再严格必需，作者偏好 `clip`。
- 🌍 作者也使用逻辑属性和值，以支持从右到左（RTL）文本方向。
- 🪆 嵌套容器问题：`cqi` 假设 `body` 是父容器；若中间有非全视口宽度的 `.inside` 容器，新的 full-bleed 会失效。
- 🧪 解决方案：用 `@property` 定义 `--body-size`，设置 `inherits: true`、`initial-value: 100%`；让 `.inside` 设置 `--body-size: 100cqi` 并成为容器，`.full-bleed` 继承该值后用 `var()` 计算宽度和负 margin。
- 🧠 `@property` 的作用：让值在 `.inside` 设置时相对父级 `body` 计算，而不是在 `.full-bleed` 使用时相对 `inside` 计算；更多容器时可在 `body` 的直接子元素如 `main` 上设置 `--body-size`。
- 🚀 下一代期望：CSS 应支持引用指定容器，如 `100cqi(body)`、`calc(100 * cqi(body))` 或 `calc(100 * container(cqi, body))`；希望 Interop 2026 推进。
- 📝 文末还包含订阅、Mastodon/Bluesky、作者人类写作声明与 Valley Fold 合作信息。

---

### [请稍等……](https://css-tricks.com/orbital-mechanics-or-how-i-optimized-a-css-keyframes-animation/?ref=tailwindweekly.com)

**原文标题**: [One moment, please...](https://css-tricks.com/orbital-mechanics-or-how-i-optimized-a-css-keyframes-animation/?ref=tailwindweekly.com)

当前内容仅为加载与验证提示，用户需等待系统完成请求验证后才能继续访问。

- ⏳ 页面显示加载状态，提示“Loader”。
- 🔍 系统正在验证你的请求。
- 🕒 请耐心等待验证完成。
- 🚫 验证结束前可能无法继续操作或访问内容。

---

### [](https://www.socialfetch.dev/?ref=tailwindweekly.com)

**原文标题**: [Social Media Scraping API — 233 Endpoints | Social Fetch](https://www.socialfetch.dev/?ref=tailwindweekly.com)

overview summary
- 🚀 Social Fetch 是面向生产管道的社媒数据 API，每日处理 800 万+ API 请求，主打“数据，而非维护”。
- 🌐 一个 API 覆盖 23 个平台、233 个端点，统一 JSON schema，返回资料、帖子、转录文本和指标等数据。
- 🔄 每次请求实时抓取公开数据，不是共享缓存；代理、平台变化和浏览器变动由服务方维护。
- 🧪 示例端点包括 YouTube 频道、TikTok/Instagram/X/LinkedIn 资料，使用 x-api-key 认证，响应含 followers、subscribers、bio、verified 等字段。
- ⚙️ 返回统一结果状态 found、not_found 或可重试错误；版本化 JSON，并提供 requestId 追踪每次请求。
- 📈 可靠性数据：99.8% uptime、平均响应约 3.2 秒、Operational 状态；无公开 RPS 上限，建议并发低于约 500 并重试 503。
- 🧑💻 三步接入：创建免费账号获得 100 请求额度，选择端点并传入用户名/URL/关键词/帖子 ID，获取干净 JSON。
- 🔌 集成 TypeScript SDK、n8n、Make、Apify、MCP 和 AI 客户端，适合代码、自动化和 AI 工作流。
- 🧰 主要用例：品牌/竞品监控、创作者筛选、视频/音频转写检索、Reddit/Facebook 群组等社区追踪。
- 💰 定价按请求计费，1 请求=1 信用；Starter $14/1k、Growth $47/25k、Scale $379/230k，月付/年付有折扣，按量信用永不过期。
- 🆓 提供 100 免费信用，无需信用卡；免费试用使用真实实时端点，与付费响应结构一致。
- 📊 平台覆盖：TikTok 30、Instagram 20、X 29、YouTube 13、LinkedIn 41、Reddit 7、Facebook 21 等，共 23 个平台。
- 🎯 TikTok 示例端点包括资料、视频、关注者、关注列表、地区、受众、互动和直播等。
- 🏭 面向生产环境：支持并发工作负载、明确状态和请求 ID，客户反馈强调摆脱频繁损坏的自建爬虫。
- 🛡️ 合规说明：仅返回公开数据，使用者需遵守合同、平台条款和适用法律；提供隐私、安全、DPA、子处理者页面。
- 🏆 社会证明：Product Hunt 当日第 3 名、3,200+ 开发者、DevHunt/Product Hunt/Uneed 五星评价，并与 Talkwalker、Brandwatch、Hootsuite 等比较。
- 📝 博客主题包括面向 LLM 的抓取 API、社媒 API 应“无聊”、Talkwalker 替代方案等。

---

### [](https://www.mapcn.dev/?ref=tailwindweekly.com)

**原文标题**: [mapcn - Beautiful maps made simple](https://www.mapcn.dev/?ref=tailwindweekly.com)

mapcn 是一个免费、开源、即用且可定制的 React 地图组件库，基于 MapLibre 构建，并使用 Tailwind 进行样式设计，目标是让精美地图的开发更简单。

- 🗺️ 核心卖点：精美地图，简单实现
- ⚛️ 面向 React：提供即用、可定制的地图组件
- 🧱 技术基础：基于 MapLibre，使用 Tailwind 样式
- 🚀 主要入口：开始使用、查看组件、为智能体复制提示词
- 📊 数据示例：活跃用户 3,544，较上一小时增长 12.5%
- 🏞️ 路线示例：Central Park Loop，6.2 英里、32 分钟、285 卡路里
- 🌍 城市示例：纽约、伦敦、东京、悉尼
- 🔗 产品导航：文档、组件、区块
- 👥 社区与资源：GitHub、赞助、MapLibre GL、shadcn/ui、Tailwind CSS
- ©️ 版权信息：2026 mapcn，保留所有权利

---

### [tiiny.host - 在线分享作品的最简单方式](https://tiiny.host/?fpr=vivian32&ref=tailwindweekly.com)

**原文标题**: [tiiny.host - The simplest way to share your work online](https://tiiny.host/?fpr=vivian32&ref=tailwindweekly.com)

当前未收到可总结的文本，因此无法提取文章要点并生成摘要。

- 📭 您尚未粘贴需要总结的内容
- ✍️ 请提供文章或文本后，我会按中文输出摘要
- 📌 摘要将包含顶部概述和带表情符号的“-”要点
- ✅ 我会尽量保留关键信息并做到简洁清晰

---

### [](http://tinycast.dev/?ref=tailwindweekly.com)

**原文标题**: [Tinycast â everything on your Mac, one keystroke away](http://tinycast.dev/?ref=tailwindweekly.com)

Tinycast 是一款专为 macOS 打造的原生启动器，以极简、轻量和隐私至上为核心理念，用一个快捷键就能访问一切功能，拒绝 Electron、账号与遥测。

- 🚀 **定位**：原生 macOS 启动器（v0.11.3），支持 macOS 26+ 及 Apple silicon/Intel，一个快捷键调用全部功能
- 🪶 **轻量**：内存占用低于 100 MB，零第三方依赖，启动速度远超 Electron 应用
- 💰 **免费开源**：AGPL-3.0 协议，无 Pro 付费墙，仅接受可选打赏，代码可自行审阅与构建
- 🧰 **核心功能**：应用模糊搜索启动、内联计算器（数学/单位/货币/时区）、剪贴板历史、AI 聊天、快速操作（改写/翻译/总结）
- 🪟 **进阶功能**：窗口管理（34 条命令）、JavaScriptCore 扩展、代码片段、浮动笔记、文件搜索、日历、自定义命令等
- 🔒 **隐私优先**：0 账号、0 遥测、0 依赖，绝大多数功能默认关闭，按需开启，数据永不离开本地
- ⌨️ **键盘驱动**：可自定义唤起快捷键，支持 Cmd+数字 打开收藏、Tab 切换模式等，按键跟随物理位置适配任意布局
- 🔄 **平滑迁移**：可直接读取 Raycast v2.0+ 的 `.rayconfig` 导出文件，迁移快捷键、收藏、剪贴板、代码片段等设置
- 🏢 **用户群体**：被 Apple、Google、Microsoft、OpenAI、字节跳动、Cloudflare 等公司员工日常使用
- 🎨 **外观与备份**：支持浅色/深色/玻璃主题，整套设置可一键导出为单文件并恢复到任意设备

---

### [使用 HTTP 拦截、调试和构建](https://httptoolkit.com/?ref=tailwindweekly.com)

**原文标题**: [Intercept, debug & build with HTTP](https://httptoolkit.com/?ref=tailwindweekly.com)

HTTP Toolkit 是一款开源、跨平台的 HTTP 调试、测试与构建工具，支持在 Windows、Linux 和 macOS 上一键拦截、查看和编辑任意 HTTP(S) 流量，并能精准覆盖移动应用、设备、容器、浏览器和后端进程等多种客户端。

- 🚀 一键拦截：零配置捕获 HTTP(S)，可只针对单个客户端抓包，避免干扰整台电脑。
- 🎯 精准目标：支持拦截 Android/iOS 单个应用、整台设备、Docker 容器、浏览器窗口、Node.js/Java/Python/Ruby 后端进程、终端会话等，也可手动将任意客户端配置为 HTTP 代理。
- 🔎 查看与搜索：按内容类型和来源分类，支持强大过滤，快速定位关键消息。
- 📄 消息检查：查看 URL、状态、请求头、正文，解析参数，并内置 MDN 标准头文档说明。
- 🧩 正文解析：基于 Monaco（VS Code 编辑器）支持 JSON、Protobuf、Base64、HTML、XML、JS、hex 等高亮与自动格式化。
- ⏸️ 断点编辑：暂停传输中的 HTTP 流量，精细化匹配，重定向请求，修改方法、头、状态或正文；也可直接模拟响应或强制关闭连接。
- ✉️ 自定义请求：内置完整 HTTP 客户端，可发送请求探索 API，自动处理正文压缩和消息分帧，并复用调试工具查看响应。
- 🛠️ 自动化改写（Pro）：注入模拟响应、映射本地文件、覆盖真实响应，或模拟尚不存在的端点/服务器。
- 📚 规则集管理：从拦截流量一键创建规则，分组和别名组织，导出分享给团队或保存为私有库。
- 🔄 转换与错误注入：将生产站点重定向到本地测试服务器，用连接重置、超时、失败状态码阻止请求；动态转换请求/响应，注入头、匹配替换正文、修补 JSON。
- 💻 下载平台：提供 Windows（安装器/Winget/Zip）、macOS（Apple Silicon/Intel/Homebrew）、Linux（DEB/RPM/Arch/AppImage/Zip x64/arm64）版本。
- 📱 移动端支持：可发送下载链接到电脑，在电脑下载 HTTP Toolkit 后连接移动设备进行调试。

---

### [](https://promptwatch.com/?ref=tailwindweekly.com)

**原文标题**: [Promptwatch | #1 AI Search Visibility & GEO Platform](https://promptwatch.com/?ref=tailwindweekly.com)

Promptwatch 是一个面向 AI 搜索时代的品牌可见性监测与优化平台，帮助企业在 ChatGPT、Gemini、Claude、Perplexity 等生成式搜索中追踪、分析并提升品牌曝光，并将 AI 搜索转化为可带来转化流量的收入渠道。

- 🔍 核心功能是追踪真实用户提示词，查看 AI 回答中何时提及品牌，并跨多个 AI 平台监控可见性。
- 📊 提供引用分析、AI 爬虫与代理分析、实时提及跟踪、情感分析和声量份额等数据洞察。
- 🤖 内容代理可基于真实引用数据生成更易被 AI 引用的内容，包括内容缺口分析、内容简报、内容日历和发布到引用时间线。
- 🛒 支持电商与购物洞察，查看 ChatGPT 等平台的实际推荐、购物数据和品牌/产品/竞品实体追踪。
- 🌐 覆盖 ChatGPT、Gemini、AI Overviews、Claude、Perplexity、Grok、Copilot、DeepSeek、Mistral、Meta 等 AI 平台。
- 🌍 支持英语、荷兰语、德语、葡萄牙语、日语等多语言，以及任意地区追踪。
- 🔗 站外引用功能可跟踪 Reddit、YouTube 等外部来源，理解哪些引用和内容类型驱动 AI 可见性。
- ⚡ 可连接网站，并与 Cloudflare、Fastly、Vercel 等集成，实时追踪 AI 爬虫与代理流量。
- 🧠 通过 GEO 洞察、内容差距和优先级建议，帮助团队决定优化什么以提升 LLM 推荐。
- 📈 商业价值在于揭示 AI 偏好内容、追踪 AI 代理访问，并生成优化内容以提升高意向流量和收入。
- 🏢 适合品牌、SEO 团队和代理机构，可管理多个客户并对比竞品在 AI 搜索中的可见性。
- ⭐ 已有 1,780+ 品牌和代理机构使用，G2 评分 4.7/5，并拥有约 265 亿条引用、点击和提示数据。
- 🗣️ 用户评价称赞其站外提及追踪、Actions 功能、API 集成、仪表盘、客户成功团队和可执行洞察。
- ❓ 常见问题说明：从输入品牌 URL 和 5 个相关提示词开始，平台会收集品牌与竞品在 AI 回答中的提及。
- 🚀 提供预约演示和免费试用，目标是让品牌成为 AI 推荐的首选。

---

