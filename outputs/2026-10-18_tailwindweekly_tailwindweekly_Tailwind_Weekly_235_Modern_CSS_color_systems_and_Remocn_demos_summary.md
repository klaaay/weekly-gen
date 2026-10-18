### [发布 v4.12.0 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases/tag/v4.12.0?ref=tailwindweekly.com)

**原文标题**: [Release v4.12.0 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases/tag/v4.12.0?ref=tailwindweekly.com)

Nuxt UI v4.12.0 发布，重点包括全新 Chart 组件、与 @nuxtjs/i18n 的自动 locale 集成，以及页面体积和交互性能的显著优化，同时带来多项组件增强、可访问性修复与问题修复。

- 📊 新增 Chart 组件：基于 TanStack Charts，支持折线图、面积图、柱状图和环形图，并在服务端渲染为 SVG；通过 `--ui-chart-*` CSS 变量跟随主题与色彩模式。
- 🌐 自动 locale：安装 @nuxtjs/i18n 后，App 组件会自动跟随当前 i18n locale，仅打包与 `i18n.locales` 匹配的 Nuxt UI 语言包，可移除手动 `import * as locales`。
- ⚡ 页面更轻更快：页面 JavaScript 最多减少 27%，JS 从 871.6 kB 降至 549.6 kB，gzip 从 251.9 kB 降至 183.9 kB。
- 🚀 性能优化：Header、Sidebar、DashboardSidebar 菜单、DashboardSearch/ContentSearch 命令面板及 Toaster 改为懒加载；UButton 挂载约快 38%，DropdownMenu 项约快 30%。
- 🧩 新功能与属性：Calendar 增加 `yearsPerPage`，CheckboxGroup 增加 `max`，ContextMenu 增加 `open`/`pressOpenDelay`，FileUpload 增加 `reject` 事件及自定义文件项，InputNumber 增加 `startingValue`/`allowInvalid`，NavigationMenu 增加 `viewport`，Sidebar 增加 `breakpoint`，Toast 操作支持 `closeOnClick` 等。
- 🛠️ 组件改进：支持 `loop`、`as`、`prompt`、`autoOpen` 等属性；导出 prose 组件；InputMenu 增加默认插槽；优化 FileUpload dropzone 响应性、Form 空值类型、Kbd 水合、SelectMenu 焦点及 Table 虚拟化行高等。
- ♿ 修复与可访问性：本地化硬编码无障碍标签，补齐 ChatMessages/ChatPromptSubmit、Listbox、Pagination 等可访问名称，并修复 Drawer 动画事件、ColorModeButton 标签、Link 预取等问题。
- 💚 贡献者：由 @benjamincanac 等 14 位贡献者参与，完整变更见 `v4.11.3...v4.12.0`。

---

### [一个基于 Base UI 构建的全新现代化 UI 组件库 - coss ui](https://coss.com/ui?ref=tailwindweekly.com)

**原文标题**: [A new, modern UI component library built on top of Base UI - coss ui](https://coss.com/ui?ref=tailwindweekly.com)

该页面介绍 coss.com 的现代化 UI 组件库：它基于 Base UI 构建，面向开发者和 AI，提供快速入门入口以及 522 个可浏览的 particles，并涵盖多种常用界面组件。

- 🧱 基于 Base UI 构建，定位为现代 UI 组件库，服务开发者与 AI 场景。
- 🚀 页面提供 “Get started” 和 “Browse 522 particles” 入口，便于快速开始和浏览组件。
- 🧩 组件覆盖表单、导航、弹窗、数据展示与反馈等常见场景，如 Accordion、Button、Calendar、Dialog、Form、Table、Toast。
- ✨ 新增 Composer，面向聊天和 AI 助手界面，支持输入框增长、持久操作，以及可选的提及或斜杠命令。
- ♿ 包含 Label、Separator、Tooltip、Preview Card 等注重可访问性与提示体验的组件。
- 🌱 页脚显示 © 2026 coss.com，并强调“open source, open heart, open mind”的开源理念。

---

### [更新日志 - ReUI](https://reui.io/docs/changelog?ref=tailwindweekly.com)

**原文标题**: [Changelog - ReUI](https://reui.io/docs/changelog?ref=tailwindweekly.com)

该文档汇总了 ReUI 从 v2.0.1 到 v2.8.1 的更新日志，核心集中在组件库扩展、Data Grid 与日历/Gantt 等复杂组件增强、React Compiler 兼容、Pro 区块与模板增长，以及 MCP、Agent Skills、图标体系和文档体验完善；同时包含多项破坏性变更与迁移提示。

- 🚀 v2.8.1（10/15）：新增 Shadcn Trace 与 22 个示例、12 个 Pro 区块；Data Grid、Event Calendar、Gantt、Date Selector 支持 React Compiler；File Type 支持 171 种格式。
- 🎨 v2.8.0（10/11）：新增 Color Picker、Emoji Picker、File Type 基础组件；Data Grid 支持分组表头；205 个图标重命名并重组分类，属破坏性变更。
- ✍️ v2.7.0（10/3）：新增 Signature Pad、Time Picker；Cascader 支持全局搜索；新增富文本编辑器、Whiteboard、DevOps 等 Pro 区块。
- 📈 v2.6.x（9 月）：新增 Deal Pipeline Workspace、App Shell、Pricing、CTA、Compare、How It Works 等区块；新增 Sidebar、Message、Bubble 等免费示例；MCP 支持缩略图与 `get_thumbnail`。
- 🧮 v2.5.x（8–9 月）：Data Grid 增强单元格选择、复制粘贴、拖拽填充、编辑 API 与本地化；新增 AI Agents、Data Grid Editing、Flow、Agent Activity 等区块；`cn` 包迁移为破坏性变更。
- 🧱 v2.4.0（8/25）：新增 Code Block 基础组件；Gantt 支持依赖箭头与里程碑；新增多个 Ultimate Templates。
- 🌲 v2.3.0（8/19）：新增 Cascader 基础组件；Filters 重建为布尔查询树并产生多项破坏性 API 变更；新增营销 Hero 与模板。
- ⚙️ v2.2.0（8/5）：Data Grid 升级到 TanStack Table v9；列固定从 `left/right` 改为 `start/end`；React Compiler 的 `"use no memo"` 不再默认。
- 📅 v2.1.x（7–8 月）：Data Grid 支持树形行；新增 Event Calendar、Gantt、Icon Tile 基础组件与示例；模板目录扩展；Pro 提供 485 个区块、562 个图标。
- 🧩 v2.0.1 / v1（3 月及更早）：新增 Input Group、Button Group、Card、Dropdown Menu、Data Grid 组件；加入虚拟化、行固定与移动端修复。
- 🛠️ 横向能力：MCP Server、Agent Skills、`llms.txt`、RTL、文档性能、图标搜索与无障碍持续改进。
- ⚠️ 迁移重点：图标重命名/分类、Filters API、Data Grid 列固定、`cn` 导入方式等变更需按文档迁移；旧图标名与部分旧 URL 仍提供兼容或重定向。

---

### [适用于 React、Next.js 和 React Native 的动画组件 · beUI](https://beui.dev/?ref=tailwindweekly.com)

**原文标题**: [Animated Components for React, Next.js and React Native · beUI](https://beui.dev/?ref=tailwindweekly.com)

beUI 是面向 React、Next.js 和 React Native 的动画组件库，提供基于 Motion 与 Tailwind CSS 的可复制源码或 CLI 安装组件；免费版开源且采用 MIT 许可，Pro 版提供 300+ 高级区块、模板与动画插画等扩展资源。

- 🧩 包含 143 个 React 组件与 45 个 React Native 组件，覆盖按钮、弹窗、Tabs、图表、AI 界面等。
- ⚙️ 基于 Motion/Framer Motion 与 Tailwind CSS，面向 React 19、Tailwind CSS 4，并通过 shadcn 注册表分发。
- 📦 支持 bun、npm、pnpm、yarn，可用 `bunx --bun shadcn add @beui/button` 等 CLI 命令安装，也可手动复制源码。
- 📱 beUI Native 使用 Reanimated、Gesture Handler 和 Uniwind 为触屏重建组件，支持 Expo 与裸 React Native，并提供 Expo Go 二维码试用。
- 🆓 公共组件库免费开源，MIT 许可，允许个人和商业项目使用与修改，但需保留版权和许可声明。
- 💎 Pro 版包含 300+ 高级区块、完整落地页模板、动画插画、Agent Skill、MCP 访问、私有注册表和可下载源码，含终身更新。
- 🛠️ 组件源码位于项目中，可自定义样式、动效和行为，并可使用自有主题 token。
- 💬 页面展示大量开发者好评，强调动效流畅、设计干净、易于使用和持续更新。
- ❓ FAQ 明确免费版可商用、Pro 为单独付费许可，且免费组件不依赖 Pro。

---

### [assistant-ui · 面向 AI 智能体的前端库](https://www.assistant-ui.com/?ref=tailwindweekly.com)

**原文标题**: [assistant-ui · The frontend library for AI agents](https://www.assistant-ui.com/?ref=tailwindweekly.com)

assistant-ui 是面向 AI 智能体的前端库，提供生产级聊天所需的基础组件与运行时，可通过适配器连接任意后端。

- 🧩 提供 primitives 与 runtime，覆盖生产聊天界面、线程、流式输出和工具调用。
- 🔌 支持 AI SDK、LangGraph、LangChain、Mastra 及自定义后端，通过适配器接入。
- 📈 项目热度为 12.6k GitHub stars、每周 120 万次下载，并获 Combinator 支持。
- ⚛️ React 端以 Provider、Hook 和单个组件快速搭建；示例通过 AssistantChatTransport 流式返回模型输出。
- 🛠️ Runtime 处理流式输出、推理、工具、审批、来源、附件、分支、建议、语音和生成式 UI。
- 🎨 UI 完全可组合定制，CLI 会将 UI 源码复制到你的仓库，便于按需改造。
- ☁️ 可选择 Assistant UI Cloud 托管线程与持久化，实现跨刷新会话和上下文积累。
- 🚀 支持 React、Native 和 Ink；MIT 许可，可通过 `npx assistant-ui init` 初始化项目并连接后端适配器。

---

### [React Bits —— 免费动画 React 组件](https://reactbits.dev/?ref=tailwindweekly.com)

**原文标题**: [React Bits â Free Animated React Components](https://reactbits.dev/?ref=tailwindweekly.com)

该内容介绍面向创意开发者的 React 动画组件与背景库，提供可完全掌控的源码，并支持按需安装与高度自定义。

- 🎨 提供动画组件与背景，安装后即以源码形式归开发者所有
- 🎛️ 支持调节每个参数值，包括当前页面背景效果
- 🧩 组件分类涵盖文字动画、动画、组件、背景和微交互
- 💻 可选择 JavaScript 或 TypeScript，并使用纯 CSS 或 Tailwind
- 📋 支持复制源码，或通过 CLI 安装所需组件
- 📘 提供安装指南，方便快速上手使用

---

### [AI 元素 - shadcn-svelte](https://shadcn-svelte.com/docs/ai-elements?ref=tailwindweekly.com)

**原文标题**: [AI Elements - shadcn-svelte](https://shadcn-svelte.com/docs/ai-elements?ref=tailwindweekly.com)

AI Elements 是一套用于构建“智能体界面（agentic interfaces）”的模式集合，基于 shadcn-svelte 组件组合而成，代码直接复制进项目，无需安装任何包。会话由 Message Scroller 中的多个 Message 轮次组成；智能体在每一轮中执行的操作，例如 Reasoning、Tool、Plan，都建立在 Trace 之上，因此结构统一。示例使用 @ai-sdk/svelte，但模式只读取消息片段，所以可配合任意消息来源使用。

- 📦 **无包安装**：每个模式都是 shadcn-svelte 组件的组合，代码归你所有，复制即可用。
- 💬 **Chat 结构**：会话是 Message Scroller 内的一系列 Message 轮次，流式回复时自动保持阅读位置。
- 🧱 **统一步骤形态**：推理、工具调用、计划等均基于 Trace 构建，保证每一步形状一致。
- 🔌 **消息源无关**：示例用 @ai-sdk/svelte，但只消费 message parts，兼容任意来源。
- 🛠️ **快速开始**：运行 `pnpm dlx shadcn-svelte@latest add trace code-block`，再复制对应模式代码，页面会列出额外所需组件。
- 🧠 **Chain of Thought**：默认折叠的摘要，展开后显示智能体所走的步骤。
- 📍 **Checkpoint**：对话中可回退到的节点。
- ✅ **Confirmation**：工具执行前的批准或拒绝提示。
- 📊 **Context**：显示对话已占用上下文窗口的比例。
- 🌲 **File Tree**：以文件夹树呈现智能体改动的文件。
- 🔗 **Inline Citation**：句内来源，悬停即展开。
- 🤖 **Model Selector**：两个菜单，分别选择运行模型与思考强度。
- 🗺️ **Plan / Queue / Task**：分别展示计划步骤与进度、待办与已完成事项、实时执行步骤。
- 💭 **Reasoning**：流式呈现智能体的思考过程。
- 📚 **Sources**：回复所引用的链接。
- 🧵 **Stack Trace / Test Results**：展示失败工具调用的栈帧，以及测试套件与失败详情。
- 🧩 **Subagent / Tool / Terminal**：展示子智能体运行结果、工具调用的输入输出、命令及其流式输出。
- ✍️ **Prompt Input / Suggestion**：带附件与发送按钮的输入框，以及一键发送的简短提示。
- 📁 **Context、File Tree 等其余模式**：涵盖上下文用量、文件变更、引用等常见智能体交互场景。

---

### [Remocn - 用你的 AI 智能体制作产品演示视频](https://remocn.dev?ref=tailwindweekly.com)

**原文标题**: [Remocn - Make a product demo video with your AI agent](https://remocn.dev?ref=tailwindweekly.com)

remocn 是一款开源产品演示视频生成工具：用户只需在空文件夹中向 AI 编程代理描述产品，它就会自动搭建项目、安装技能，并在浏览器中生成可实时预览、可通过对话修改的视频；无需剪辑软件、After Effects 或关键帧，代码本地保存且采用 MIT 许可。

- 🎬 核心体验：一个 AI Agent + 一个空文件夹，用户描述需求，代理构建视频，用户在浏览器中观看。
- 🛠️ 三步上手：打开 Claude Code、Cursor 或 ChatGPT；粘贴提示安装 remocn skill；在 localhost 预览视频。
- ⏱️ 首次配置约十分钟，第一支视频约一个下午，熟练后不到一小时。
- 💸 相比传统方式更省成本：省去约 600 美元、两周沟通的动效设计费用，也无需学习 After Effects 或制作关键帧。
- 🎞️ 区别于屏幕录制：使用预构建动画组件，效果更像正式发布的产品演示，而不是随意录屏。
- 🧩 构建块覆盖 Motion、Typography、Shaders、Transitions、Animated Icons、UI Primitives，代理按场景组合时间线。
- 🔁 修改方式直接：说出哪里不对，预览即时更新，无需修订轮次或等待他人排队。
- 📦 代码归属清晰：项目复制进仓库并保留，MIT 许可，无运行时、无账号、无锁定。
- 📊 资源与兼容性：包含 395 个组件，支持任意 coding agent，并与 shadcn 相关生态结合。
- 💬 社区反馈积极：开发者称赞其解决了产品动画演示需求，项目完成度高。
- ❓ FAQ 要点：不需要会写代码，但需使用 AI 编程代理；无需 After Effects 或视频编辑器；本地安装小项目，不依赖官方服务器。
- 🌐 免费开源：由赞助商支持组件注册表扩展与渲染速度，赞助从每月 10 美元起，并提供制作首个视频与 GitHub Star 入口。

---

### [Cozy Watch - 为 macOS 提供清晰的 GitHub 通知](https://www.cozywatch.com/?ref=tailwindweekly.com&aff=lVeE1)

**原文标题**: [Cozy Watch - Clear GitHub Notifications for macOS](https://www.cozywatch.com/?ref=tailwindweekly.com&aff=lVeE1)

Cozy Watch 是一款面向 macOS 的开源 GitHub 通知与 PR 管理工具，旨在过滤 GitHub 噪音，只在需要时提醒用户，并帮助用户直接进入相关 PR，从而保持专注。

- 🔔 核心功能：当拉取请求、代码审查、提及或 CI 结果需要你处理时，及时通知你。
- 🖥️ 支持从菜单栏和应用内查看当前 PR 状态，跳过收件箱筛选，直接进入发生变更的 PR。
- 🔒 开源、默认保护隐私，支持 macOS 12 Monterey 或更高版本，并可随时查看源码。
- 🆓 个人使用永久免费，包含全部功能、无限仓库、所有通知类型、免费更新及 MIT 开源许可。
- 💼 商业用途为 $29/年，包含正式商业使用、30 天商业试用、全部功能及应用内许可证管理，通过 Lemon Squeezy 安全售卖。
- 🚀 最新版本 0.8.6（2026 年 2 月 28 日）：更新时保留 PR 缓存；修复管理 2000 多个仓库时的 ENOTFOUND DNS 错误；迁移至 GitHub App；优化仓库选择速度。
- 📬 提供邮件订阅以获取更新、版本发布和改进信息，并可在 Uneed 查看社区评价；官网还提供下载、路线图、博客等入口。

---

### [我的 2026 年 HTML 样板 - Manuel Matuzović](https://matuzo.at/blog/2026/html-boilerplate?ref=tailwindweekly.com)

**原文标题**: [My HTML boilerplate in 2026 - Manuel Matuzović](https://matuzo.at/blog/2026/html-boilerplate?ref=tailwindweekly.com)

文章回顾作者五年前发布的 HTML 基础模板，并给出 2026 年更新版：通过完整代码示例逐行说明 HTML 文档的基础结构、必需/推荐/可选元素及其原因，重点涉及兼容性、可访问性、性能、移动端适配、社交分享和 LLM/去中心化平台支持。

- 🧱 提供一份可直接参考的完整 HTML boilerplate，覆盖 `doctype`、`html`、`head`、`body` 及常用 `meta`、`link`、`script`。
- ✅ `<!DOCTYPE html>` 仍属必需，用于兼容性；HTML 虽为 living standard，但不能省略 doctype。
- 🌍 `<html lang="en">` 很重要，应按 BCP47 语言标签声明页面自然语言。
- 🚫 `no-js` class 可选，用于无 JavaScript 或 JS 被禁用时的样式控制，也利于 Web Components 渲染前优化。
- 🔤 `<meta charset="UTF-8">` 必需且应放在 `<title>` 前，避免标题或字符显示错误。
- 📱 viewport 建议使用 `width=device-width`；`initial-scale=1` 已非必需，但为兼容旧设备可保留。
- 🔎 新增可选 `text-scale` meta，让移动浏览器尊重系统文字缩放，但作者提醒必须测试布局是否被破坏。
- 🏷️ 页面应有唯一且有信息量的 `<title>`，影响浏览器标签、搜索结果和书签。
- ⚡ 渲染阻塞 JS 应谨慎放在 head；普通非阻塞脚本优先用 `type="module"`，其隐式延迟执行利于性能。
- 🖨️ 建议提供打印样式表，作者认为这是良好 UX，也能节省纸张和墨水。
- 🎨 Favicon 建议同时考虑 `favicon.ico`、SVG favicon 和 `apple-touch-icon`；SVG 可缩放并支持深色模式。
- 📲 `manifest` 对 Android/PWA 很重要，应包含 192、512 及 maskable 图标。
- 🔗 `canonical` 可避免重复内容造成 SEO 问题；`og:url` 也应设置，防止带参数的分享链接被平台当作不同页面。
- 🤖 可选 Markdown alternate 链接，便于 LLM 读取并减少 token 消耗。
- 🐘 `rel="me"` 可用于 Mastodon 身份验证；`fediverse:creator` 可署名，但需在 Mastodon 设置中配置域名允许列表。
- 🌐 `site.standard.publication` 用于 Standard.site/atmosphere 发布；`theme-color` 支持有限，Safari 26 起行为也有变化。
- 📝 页面描述、`og:image`、`og:url` 属社交分享关键项；`og:title`、`og:description`、`og:image:alt`、`og:type`、`og:locale` 可选且各平台支持不一致。
- 🧩 其他可选增强包括 preload、RSS、作者 meta、`viewport-fit=cover` 适配刘海屏、`interactive-widget=resizes-content` 控制键盘弹出时的视口行为，以及 `color-scheme` 声明明暗配色支持。

---

### [我希望早点理解的颜色系统](https://theadminbar.com/semantics-and-primitives-color-system/?ref=tailwindweekly.com)

**原文标题**: [The Color System I Wish I Understood Sooner](https://theadminbar.com/semantics-and-primitives-color-system/?ref=tailwindweekly.com)

颜色管理是网站项目中容易被忽视但影响长期维护的关键环节；文章提出用“基础色 primitives + 语义色 semantics”两层体系，既统一定义调色板，又让颜色按用途被直观使用和灵活修改。

- 🎨 HEX 有超过 1600 万种可能值，直接选色会让决策困难；建立受控调色板是正确方向。
- 📚 真实项目调色板不只有品牌色，还包括中性色、功能色（成功/警告/错误）以及各种深浅状态。
- 🧱 第一层 primitives 按颜色本身命名，如 `--blue-600`、`--gray-200`，集中定义所有可用色值。
- ✅ primitives 的优点是结构化、一致、单一来源；Tailwind 的 22 个色系×11 个深浅就是典型例子。
- ⚠️ 但 primitives 只说明“有哪些颜色”，不说明“用在哪里”；半年后很难记住按钮、链接分别用了哪个蓝。
- 🏷️ 第二层 semantics 按用途命名，如 `--button-background`、`--link-color`、`--heading`，更直观。
- ✅ semantics 让修改目标明确，不用反推数字含义；需要改按钮颜色时可直接找到对应变量。
- ⚠️ 但仅用 semantics 时，多个语义变量可能重复同一个 HEX 值；全局改色要逐个更新，容易漏改并导致不同步。
- 🔗 两层结合后，primitives 负责“调色板源值”，semantics 负责“如何应用”，语义变量指向基础色变量。
- 🔄 全局改色只需更新一个 primitive，所有引用它的语义色自动同步；例如改 `--blue-600` 可统一更新按钮、链接和 CTA。
- 🎯 同时保留元素级独立控制：把 `--button-background` 改为 `var(--orange-600)`，只影响按钮，不影响链接和 CTA。
- ✅ 最终收益是：调色板有明确定义、命名有实际意义、全局控制与局部灵活兼得，项目更一致也更好维护。
- 💡 作者经验表明，单独使用任一层都会遇到瓶颈；真正把两层分开并配合使用后，颜色管理才变得清晰可靠。

---

### [今天就能使用的12个无需构建步骤的CSS特性](https://flaviocopes.com/modern-css-features/?ref=tailwindweekly.com)

**原文标题**: [12 CSS features you can use today with no build step](https://flaviocopes.com/modern-css-features/?ref=tailwindweekly.com)

文章介绍了 12 个在 2026 年 9 月已可直接使用的原生 CSS 特性，它们能替代 Sass、PostCSS 插件和大量 JavaScript 补丁；文中逐项说明用途、替代的旧方案、浏览器支持情况和主要注意点，并建议用 MDN Baseline 与 `@supports` 做兼容性检查。

- 🧩 **原生嵌套**：规则可写在父选择器内，支持媒体查询和容器查询嵌套；Baseline 广泛可用（2026 年 6 月），但 `&__title` 不会拼接类名，选择器列表会影响优先级。
- 🔍 **`:has()`**：让 CSS 能根据后代元素反向选择父级或兄弟元素；Baseline 广泛可用（2026 年 6 月），优先级取最具体参数，避免在 `body` 上做过大范围检查。
- 📐 **容器查询与 `cqi` 单位**：按组件容器宽度而非视口调整布局；Baseline 广泛可用（2025 年 8 月），但 `container-type: inline-size` 不适合宽度由内容决定的元素。
- 🧱 **Subgrid**：子网格可借用父网格行，让多张卡片的标题、正文和按钮对齐；Baseline 广泛可用（2026 年 3 月），需配合 `grid-row: span 3`。
- 🎨 **`oklch()` 与 `color-mix()`**：原生颜色计算与运行时混色，替代 Sass 的 `darken()`、`mix()`；Baseline 广泛可用（2025 年 11 月），注意广色域颜色在普通屏幕上可能变暗。
- 🖼️ **`aspect-ratio`**：一行代码固定宽高比，替代 padding hack；Baseline 广泛可用（2024 年 3 月），它是偏好值而非硬限制，图片仍应保留 `width`/`height` 属性。
- 🗂️ **级联层 `@layer`**：把样式顺序写进 CSS，减少对文件顺序和 `!important` 的依赖；Baseline 广泛可用（2024 年 9 月），未分层样式优先于所有层，`!important` 会反转顺序。
- 🎯 **`:is()` 与 `:where()`**：简化选择器分组；`:where()` 不增加优先级，适合基础样式；Baseline 广泛可用（2023 年 7 月），`:is()` 取最具体参数优先级且参数容错。
- 🎞️ **滚动驱动动画**：用 `animation-timeline: scroll()` 或 `view()` 实现阅读进度、进入视口淡入等效果；尚未 Baseline，Firefox 仅 Nightly 支持，需 `@supports` 和 `prefers-reduced-motion` 兜底。
- 📱 **`dvh`、`svh`、`lvh`**：解决移动端 `100vh` 被浏览器工具栏遮挡的问题；Baseline 广泛可用（2025 年 6 月），`dvh` 会随滚动变化，布局通常优先用 `svh`。
- 🌍 **逻辑属性**：用 `margin-inline-start`、`padding-inline` 等按书写方向描述布局，天然支持 RTL；Baseline 广泛可用（2024 年 3 月），不要在同一元素混用物理属性和逻辑属性。
- ✨ **`@starting-style`**：为从 `display: none` 出现的元素提供初始状态，实现淡入淡出；Baseline 新近可用（2024 年 8 月），Firefox 的退出过渡仍有差异，且只作用于首次渲染。
- 🧪 **其他未列入主榜的特性**：`text-wrap: balance`、`@scope`、`field-sizing` 值得关注；CSS 锚点定位仍属 Limited；`@property`、`light-dark()`、`linear()` 也可作为候选项。
- ✅ **实践建议**：用 MDN 的 Baseline 徽章确认支持情况，把风险特性包在 `@supports` 中，让降级版本仍然可读可用。

---

### [Zernio - 面向智能体的营销基础设施](https://zernio.com/?ref=tailwindweekly.com)

**原文标题**: [Zernio - Marketing Infrastructure for Agents](https://zernio.com/?ref=tailwindweekly.com)

Zernio 为开发者和 AI Agent 提供统一的营销基础设施：通过一次官方 API 集成，即可覆盖社交发布、广告投放、通信与博客内容管理，省去逐平台审核、令牌轮换和限流维护，支持快速上线并规模化运营。

- 🚀 **统一营销 API**：一个集成覆盖社交、博客、消息、语音和广告渠道，仅使用官方 API，平台审核与维护由 Zernio 承担。
- 📱 **社交发布与管理**：支持 16 个社交网络，可发布、排期、回复评论和私信并拉取分析数据；示例包括 Instagram、TikTok、X、LinkedIn、Facebook、YouTube、Reddit、Discord、Telegram、Slack 等。
- 📣 **广告投放 API**：统一管理 Meta、Google、LinkedIn、TikTok、Pinterest、X、OpenAI 和 Reddit Ads，可创建 campaign、调整预算、暂停/恢复并汇总花费与表现。
- 💬 **通信 API**：统一接入 WhatsApp、iMessage、SMS/MMS 和语音通话，提供统一收件箱与账单，并可在 55 个国家搜索、购买和验证电话号码。
- 📝 **博客与内容渠道**：通过 Blogs API 在 WordPress、Shopify 等平台发布和管理文章。
- 🧩 **多种接入方式**：提供 8 种 SDK、REST API、MCP 和 CLI；MCP 提供 496 个工具与单一 OAuth 连接，CLI 提供 371 条命令、47 个分组并默认输出 JSON。
- 🤖 **面向 AI Agent**：可与 Claude Code、Cursor、Codex、OpenClaw、Grok bot、Hermes 等配合，让 Agent 执行发帖、回复和调用等任务。
- ⚡ **快速上线**：从注册到完成首次发帖、消息、报告或广告可少于 5 分钟；无需逐平台开发者应用审核，免费开始且无需信用卡或销售电话。
- 🏢 **企业级能力**：支持管理 2,000+ 连接账户，提供 SSO、MFA、SCIM、RBAC、审计日志、SOC 2、GDPR 合规及 99.97% 正常运行时间。
- 👥 **开发者认可**：已有 200,000+ 开发者和构建者使用，用户评价集中在集成简单、SDK 清晰、多平台发布高效以及广告 API 稳定。

---

### [Remocn - 用你的 AI 智能体制作产品演示视频](https://remocn.dev/?ref=tailwindweekly.com)

**原文标题**: [Remocn - Make a product demo video with your AI agent](https://remocn.dev/?ref=tailwindweekly.com)

remocn 是一款借助 AI 智能体生成产品演示视频的工具：你只需用自然语言描述想做的视频，它就会在空文件夹中搭建项目、生成动画预览，并让你边看边改，无需学习剪辑软件或时间轴操作。

- 🎬 **核心体验**：在空文件夹中打开 Claude Code、Cursor 或 ChatGPT，粘贴一条提示词，即可自动安装项目与 remocn skill，并在浏览器中预览视频。
- 🛠️ **极简流程**：只需“智能体 + 空文件夹”，没有编辑器要学、没有时间轴要拖；你描述，它构建，你观看。
- ✍️ **即时修改**：对预览说出想改的地方，视频会立即更新，无需等待修改轮次或反复沟通。
- 💸 **替代传统方案**：无需动效设计师、After Effects、关键帧或粗糙录屏；传统演示视频可能花费约 600 美元和两周时间，这里只需一条提示词和一个下午。
- 🧩 **组件化构建**：视频由运动、字体、着色器、转场、动画图标、UI 基础件等构建模块组成，智能体按场景组合到时间轴上。
- 📦 **代码归你所有**：代码会复制到你的仓库中并保留，采用 MIT 许可，无运行时、无账户、无锁定。
- ⚡ **效率与门槛**：第一次制作约需一个下午熟悉，之后不到一小时；不需要会写代码，但需通过 AI 编程智能体操作。
- 🔒 **本地运行**：安装的是本地小型视频项目及所需组件，不运行在官方服务器上，也不会回传数据。
- 🆓 **免费开源**：完全免费且 MIT 开源，赞助商支持组件库扩展与渲染速度提升，赞助档位从每月 10 美元起。
- 🌟 **社区反馈**：已有 395 个组件，支持任意编程智能体与 shadcn；社区评价积极，认为其填补了动画演示视频制作的需求空白。

---

### [tiiny.host - 在线分享作品的最简单方式](https://tiiny.host/?fpr=vivian32&ref=tailwindweekly.com)

**原文标题**: [tiiny.host - The simplest way to share your work online](https://tiiny.host/?fpr=vivian32&ref=tailwindweekly.com)

尚未收到需要总结的文章内容，无法生成有效摘要。
- 📄 请提供文章正文，我将按要点提炼并附上合适的表情符号。
- 🧾 收到内容后，我会生成简洁的中文概览摘要与关键信息列表。

---

### [Droppy：为 Mac 打造的超级灵动岛](https://getdroppy.app/?ref=tailwindweekly.com)

**原文标题**: [Droppy. Supercharged Dynamic Island for Mac](https://getdroppy.app/?ref=tailwindweekly.com)

Droppy 是一款面向 macOS 的“超级动态岛”效率应用，可把刘海屏或无刘海屏变成集实时活动、文件托盘、剪贴板、悬浮播放器和 36 个免费扩展于一体的原生工具；它一次买断、无订阅、本地优先，并与 iPhone 免费同步。内容更新于 2026 年 7 月 6 日。

- 🍏 **核心定位**：Droppy 把多种 Mac 小工具整合进刘海/动态岛，定位为“Mac 的瑞士军刀”，减少在多个应用间切换。
- 🧩 **36 个免费 Droplets**：内置动作环、日历、编码代理、文件转换、元素截图、应用清理、系统监控、歌词、DropClip 等扩展，可按需开启或关闭。
- 🎵 **媒体与锁屏体验**：支持 Now Playing、动态专辑封面、歌词逐行/逐词显示、播放队列管理、悬浮播放器，以及锁屏动态艺术效果。
- 🗓️ **刘海周边信息**：日历、实时活动、下载进度、会议倒计时、AirPods 电量、屏幕录制、消息回复等可直接在刘海旁显示和操作。
- 📁 **文件托盘与剪贴板**：拖入文件即可暂存、压缩、转换或分享；剪贴板历史可通过快捷键快速调用。
- 🧑‍💻 **工作流增强**：可查看 Claude、Codex、Cursor、Antigravity 等编码代理状态与用量限制，并支持 Zoom、Teams、Google Meet、WhatsApp、Telegram 会议控制。
- 📱 **iPhone 同步**：Droppy for iPhone 免费提供给 Mac 许可证用户，可双向同步剪贴板、文件和笔记，并支持 Live Activities 与小组件。
- 🔐 **隐私与本地优先**：剪贴板和文件数据在设备端处理；iPhone 同步采用端到端加密，同步服务器无法读取内容。
- 🎨 **高度自定义**：可选择 Dynamic Glass、Liquid Glass 或黑色风格，自定义高亮色、刘海/岛形态、侧边小组件、命令中心布局、悬浮播放器尺寸和 App 图标。
- 💰 **价格模式**：一次性买断，页面标注 $9.99，结账页显示 €8.78 起；无订阅、无续费，包含终身更新，一个许可证可覆盖两台 Mac。
- 🖥️ **兼容性**：支持有刘海 MacBook，也支持 iMac、Mac mini 和外接显示器等无刘海设备；要求 macOS 14 Sonoma 或更高版本。
- 🛟 **试用与退款**：提供 3 天全功能免费试用，购买后 14 天内可申请全额退款；支持 15 种语言。

---

### [Feedsmith：快速的 JavaScript Feed 解析器与生成器](https://feedsmith.dev/?ref=tailwindweekly.com)

**原文标题**: [Feedsmith: Fast JavaScript Feed Parser and Generator](https://feedsmith.dev/?ref=tailwindweekly.com)

Feedsmith 是一个快速、一体化的 JavaScript Feed 解析与生成库，支持 RSS、Atom、RDF、JSON Feed 及多种命名空间和 OPML 文件。

- 🚀 提供通用解析器与各格式专用解析器，将 Feed 转为镜像原始结构的对象，并把旧元素映射到现代等价元素。
- 🎉 已发布 Feedsmith 3.0，包含多项改进和破坏性变更，并提供从 2.x 升级的迁移指南。
- 🧩 核心能力包括全面格式支持、保留原始结构、智能命名空间处理（如将自定义前缀规范为标准前缀）、解析与生成一体化。
- 🛡️ 具备较强容错性：规范化旧版元素、字段和属性大小写不敏感、容忍非官方命名空间 URI 变体，并能从畸形或不完整 Feed 中提取有效数据。
- ⚡ 性能突出：解析速度快，使用 TypeScript 构建，提供完整类型定义，支持 tree-shaking 以减小打包体积。
- 🧪 测试充分：拥有 4000 多个测试，代码覆盖率约 99%。
- 🌐 兼容 Node.js 和现代浏览器，可直接用于普通 JavaScript，无需 TypeScript。
- 📦 支持 RSS 0.9x/2.0、Atom 0.3/1.0、JSON Feed 1.0/1.1 的解析与生成；RDF 0.9/1.0 支持解析，生成功能计划中；OPML 1.0/2.0 支持解析与生成。
- 📚 支持大量 Feed 命名空间的解析与生成，如 Dublin Core、iTunes、Podcast Index、Media RSS、YouTube、GeoRSS、OpenSearch 等。
- 💡 相比一些将不同字段、日期和链接合并规范化的替代库，Feedsmith 的关键优势是精确保留原始 Feed 结构，避免信息丢失，更适合依赖特定命名空间数据的应用。

---

### [GitHub - heronapp/hostflip（位于 tailwindweekly.com）· GitHub](https://github.com/heronapp/hostflip?ref=tailwindweekly.com)

**原文标题**: [GitHub - heronapp/hostflip at tailwindweekly.com · GitHub](https://github.com/heronapp/hostflip?ref=tailwindweekly.com)

hostflip 是一款免费开源的 macOS 菜单栏 /etc/hosts 配置切换工具，强调保留用户原始 hosts、按分组管理配置、通过一次授权后的后台助手实现无密码切换，并提供 CLI、SwitchHosts 迁移和安全写入机制。

- 🍎 原生轻量：使用 Swift 与 SwiftUI 构建的菜单栏应用，要求 macOS 14 或更高版本，面向 Apple 芯片；采用 MIT 许可证。
- 🔐 核心理念：/etc/hosts 归用户所有；首次运行会将现有文件导入为只读 Base Hosts，并永久保留原文件备份。
- 🧱 只写自有区块：仅修改 hostflip 自己的围栏区块；若其他程序修改 hosts，会检测到 drift，并通过差异视图协助协调，避免覆盖外部改动。
- 👥 激活模型：配置文件按组管理，每组最多激活一个；跨组激活配置和独立配置会叠加生成最终 hosts。
- ⚡ 零中断切换：一次性批准内嵌 SMAppService 守护进程后，后续切换无需反复输入密码。
- ⏸️ 主开关：可暂停全部配置并恢复基线 hosts，同时记住每个配置的状态。
- 🔁 SwitchHosts 迁移：支持 v3/v4/v5 数据，文件夹转为组，远程规则转为可自动刷新的远程配置；导入后默认不激活，并显示导入摘要。
- 📦 安装方式：可通过 Homebrew tap/cask 安装，或从 Releases 下载公证 DMG；CLI 随应用捆绑，可符号链接到 PATH。
- 🛠️ 命令行工具：支持 status、list、activate、cat、write、refresh、doctor 等命令；支持 --json 与稳定错误码。
- 🚦 退出码语义：3 表示系统 hosts 发生 drift 且阻止写入；7 表示 doctor 诊断发现不一致，便于脚本和 CI 使用。
- 🧪 刷新与诊断：refresh 分别处理远程内容保存与必要时的系统 hosts 重写；doctor 只读地按“配置→合并→文件→解析器”链路排查主机名问题。
- ⚙️ 写入机制：原子重写 /etc/hosts，先写 Base Hosts 再写活动配置；通过最小 root daemon 和仅接受“替换 hosts”的 XPC 接口写入，双向代码签名验证，写后刷新 DNS 缓存。
- 🧹 卸载注意：应先使用“Deactivate and Remove Helper”再删除应用；卸载不会自动恢复 /etc/hosts，建议先关闭主开关恢复基线；hosts.orig 会保留在 Application Support。
- 🌐 常见问题：切换后浏览器仍解析旧地址，多因浏览器私有 DNS 缓存和长连接池；需清理 host cache/socket pools 或使用隐私窗口；启用 DoH 时可能绕过 /etc/hosts。
- 🧭 其他信息：支持 Homebrew 或应用内更新；源码构建需真实 Developer ID 才能通过 XPC 验证；hostflip 由 Heron 开发者制作，但独立且无依赖。

---

