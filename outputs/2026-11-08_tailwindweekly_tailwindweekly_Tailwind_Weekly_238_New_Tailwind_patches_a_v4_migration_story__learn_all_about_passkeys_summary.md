### [Releases · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/?ref=tailwindweekly.com)

**原文标题**: [Releases · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/?ref=tailwindweekly.com)

该页面汇总了 Tailwind CSS 从 v4.2.1 到 v4.3.5 的发布记录（2 月至 11 月），重点涵盖新工具类与 `@variant`/`@utility` 能力扩展，以及 canonicalization、CLI/Vite/PostCSS/Webpack/Turbopack 集成和跨平台稳定性的持续修复。

- 🆕 v4.3.0 引入 `@container-size`、`scrollbar-*`、`zoom-*`、`tab-*` 等实用类，并支持 `@variant` 堆叠/组合与 functional `@utility` 的 `--default(...)`。
- 🧩 v4.3.4 新增 `@tailwindcss/turbopack`，加强 Next.js/Turbopack 支持，同时修复 `@scope`、watch 模式与自动源检测问题。
- 🩹 v4.3.5 作为最新版本，重点修复 canonicalization 性能、`color-mix(...)` 回退颜色、oxide WASM 加载和类型声明错误。
- ⚡ 多个版本持续优化 canonicalization：合并/迁移工具类、保留任意值单位与空格、避免错误 `calc(...)` 折叠及性能退化。
- 🛠️ CLI 与构建工具稳定性是主线：改进 `--watch`/`--poll`、Vite/PostCSS/Webpack 重建、Vite 8 支持、Vite alias 解析与 HMR 崩溃修复。
- 🌐 跨模板/语言支持增强：覆盖 Ruby `%w`/`%W`、Slim/Haml、Pug、Twig、Maud、MDX 等文件中的类名提取与识别修复。
- 🎨 样式细节修复包括 `placeholder-*` 颜色变量、CJK 字体语言适配、间距输出优化及滚动条/缩放等新增能力。
- 🔐 发布页显示各版本由 GitHub Actions 发布并使用 GitHub 验证签名，社区反应以点赞、庆祝、爱心和火箭为主。

---

### [发布 v4.3.4 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.4?ref=tailwindweekly.com)

**原文标题**: [Release v4.3.4 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.4?ref=tailwindweekly.com)

Tailwind CSS v4.3.4 是一次以稳定性和兼容性修复为主的补丁版本，唯一明确新增的是面向 Next.js 的 Turbopack loader；同时集中修复了 watch/源检测、@scope 与变体、canonicalization、Vite/Turbopack/Webpack 集成、CSS 解析与类名提取、平台兼容性等问题。

- 🚀 发布 v4.3.4，自上一版本包含 18 个提交，重点提升开发与构建稳定性。
- ➕ 新增 `@tailwindcss/turbopack`，用于在 Next.js 中使用 Tailwind CSS 的 Turbopack loader。
- 👀 修复 watch 模式对符号链接 `@source` 文件、忽略目录及 `.gitignore` 否定规则的处理，减少无效扫描。
- 🧩 修复 `@scope` 相关生成与扁平化语义，确保变体包裹、直接声明和嵌套规则行为正确。
- 🧠 改进 canonicalization：任意断点/容器查询转命名变体、主题透明度迁移、避免错误合并或折叠工具类，并修复性能与 polyfill 问题。
- ⚡ 修复 Vite 实验性 `bundledDev` 模式崩溃、扫描文件触发整页刷新，以及 `@tailwindcss/postcss` 相对 `url()` 重写。
- 🧱 增强 `@tailwindcss/oxide` 在无原生绑定平台回退 WASM，并修复 macOS 独立二进制签名。
- 🧪 提升类名提取：支持 Ruby `%w`/`%W` 自定义分隔符、Pug 多行与不平衡括号场景，并丢弃无效 UTF-8 候选。
- 🛡️ 修复多类 CSS 解析边界：空 `var()` fallback 空格、`\*/` 注释闭合、字符串中的 `!important`、末尾无分号声明/自定义属性、未平衡括号。
- 🔤 修正长度单位识别（如 `dvmin`、`svi`、`cap`、`rex`）、数值排序，以及空 modifier 或被忽略 modifier 不应生成 CSS。
- 🔁 修复 Turbopack/Webpack 在输入 CSS 变化时重建，避免 `next dev` 提供旧 CSS。
- 🧹 其他修复包括改进 `group-*`/`peer-*` 失效性能、插件日志写入 stderr、Angular 选择器警告、缓存编译器回调释放等。

---

### [发布 v4.3.5 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.5?ref=tailwindweekly.com)

**原文标题**: [Release v4.3.5 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.5?ref=tailwindweekly.com)

Tailwind CSS 发布了 v4.3.5 修复版本，重点提升性能并修复多个稳定性问题，涉及功能性变体值、`color-mix()`、WASI 加载、Turbopack 配置、CSS 注释解析和类型声明等。

- ⚡ 优化规范化性能，改善包含大量功能性变体值的项目表现，例如带有数千个值的 `matchVariant` 插件。
- 🎨 修复缺少颜色插值方法的 `color-mix(…)` 导致崩溃或生成错误回退颜色的问题。
- 🧩 确保 `@tailwindcss/oxide-wasm32-wasi` 正常加载，避免在 WebContainers 等环境中无限挂起。
- 📝 从 `@tailwindcss/turbopack` 的 README 设置中移除 `as: '*.css'`，避免破坏 CSS Modules。
- 💬 忽略顶层规则之间的 `<!--` 和 `-->`，不再抛错或吞掉下一条规则。
- 🔍 确保 `@tailwindcss/oxide-wasm32-wasi` 在首次扫描后能检测到变更和新增的源文件。
- 🛠️ 修复 `@tailwindcss/node` 类型声明中未发布模块导入在 `skipLibCheck: false` 下引发的类型错误。

---

### [Aceternity UI — React 和 Tailwind CSS 组件库](https://ui.aceternity.com/?ref=tailwindweekly.com)

**原文标题**: [Aceternity UI â React & Tailwind CSS Component Library](https://ui.aceternity.com/?ref=tailwindweekly.com)

这是 Cited 的 AI 可见性落地页：以明暗两种主题呈现，用于推广让品牌在 ChatGPT、Claude 和 Google 中被提及的工具，并包含实时仪表盘首屏、定价与 FAQ 等核心模块。

- 🎯 **产品定位**：Cited 帮助品牌在 ChatGPT、Claude 和 Google 的 AI 回答中获得提及。
- 🌗 **视觉设计**：落地页采用明暗双主题，风格轻量现代。
- 📊 **首屏亮点**：Hero 区域展示实时仪表盘，突出产品可视化能力。
- 🧭 **页面结构**：包含导航栏、Hero、AI 回答展示弧线、功能、工作原理、可见性阶梯与数据统计、用户评价。
- 💰 **转化模块**：设置定价、FAQ、行动号召和页脚，形成完整落地页链路。
- 🛠️ **附加入口**：提供实时预览和获取代码入口，便于查看与使用。

---

### [免费 Shadcn UI 组件、区块、图标、模板和 MCP -](https://reui.io/?ref=tailwindweekly.com)

**原文标题**: [Free Shadcn UI Components, Blocks, Icons, Templates & MCP - ReUI](https://reui.io/?ref=tailwindweekly.com)

ReUI 是面向 shadcn/ui 的设计优先、Agent 就绪组件平台，结合 MCP、Agent Skills 与精选注册表，帮助开发者从提示词快速走到生产环境，构建 React + Tailwind 应用。

- 🚀 平台定位：为 shadcn/ui 提供“Agent-ready”层，让 AI 编码代理直接获取真实组件、区块、图标及其 API，减少“AI 生成垃圾 UI”。
- 📦 资源规模：包含 1,264 个免费 shadcn/ui 组件、27 个 ReUI 自定义原语、678 个 Pro 区块、667 个高级图标（4 种风格、2,668 个变体）及多套整站模板。
- 🧱 Pro 区块覆盖：678 个区块分布于 7 大组、79 个类别，覆盖应用外壳、数据网格、图表、解决方案、AI & Agents、电商、营销等场景。
- 🆓 免费组件：1,264 个 shadcn 组件与 27 个自定义原语永久免费，MIT 许可，支持商用与开源，可通过 shadcn CLI 安装。
- 🎨 图标与模板：提供手绘动画图标；模板覆盖 Next.js、Vite、TanStack Start、Astro、Laravel + Inertia，包含仪表盘、SaaS、AI 聊天、白板、工单等整站应用。
- 🤖 AI 工具链：免费 ReUI MCP 可连接 Claude、Codex、Cursor、v0、Lovable、Replit、Bolt、VS Code、GitHub Copilot 等；Agent Skills 教会代理按 ReUI 模式构建。
- ⚡ 开发体验：支持 CLI 安装（如 `@reui/auth-1`）、复制源码到仓库、自由修改、无运行时锁定；每个区块可复制 AI prompt 给编码代理。
- ✅ 质量保障：由资深设计工程师手工打造并经过真实产品验证；基于 Radix UI，内置无障碍、键盘导航与 ARIA；支持暗色模式与主题变量定制。
- 💳 定价模式：Pro 一次性 $249，终身更新、无限项目、源码归你；免费组件永久免费，高级区块、图标和部分模板需授权。
- ⭐ 社区与背书：获 shadcn/ui 创作者认可，称其为可信注册表之一；社区已有 6,000+ 开发者与团队使用。
- 🆕 本轮最大更新：新增 66 个免费组件、7 个 Pro 区块和 29 个图标。

---

### [适用于 React、Next.js 和 React Native 的动画组件 · beUI](https://beui.dev/?ref=tailwindweekly.com)

**原文标题**: [Animated Components for React, Next.js and React Native · beUI](https://beui.dev/?ref=tailwindweekly.com)

overview summary
beUI 是一个面向 React、Next.js 和 React Native 的动画组件库，提供可复制粘贴的源代码组件，基于 Framer Motion 与 Tailwind CSS 构建，可通过 shadcn CLI 一键安装，并以 MIT 许可证免费用于商业项目。

- 🧩 拥有 156 个 React 组件和 73 个 React Native 组件，涵盖 Components、Blocks、AI Agents、Charts、Casino 等 5 个分类
- ⚡ 组件基于 Framer Motion 和 Tailwind CSS，动画流畅，而且可以直接修改源代码和动效
- 💻 通过一条命令即可安装，例如 `bunx --bun shadcn add @beui/button`，安装后源码完全归你所有
- 📱 beUI Native 为 React Native 提供同等体验，基于 Reanimated、Gesture Handler 和 Uniwind，适配触控操作
- 🆓 公共组件库采用 MIT 许可证，可免费商用和修改，只需保留版权与许可声明
- 💎 Pro 版包含 350+ 高级组件和动画块、60+ React Native 屏幕、完整模板以及动画插画等增值内容
- ⚙️ 技术要求为 React 19、Tailwind CSS 4 和 Motion，需要参考主题设置指南来配置共享的 CSS 变量
- 🌟 在 X 平台上获得了众多开发者的好评，他们称赞其动画精致、交互设计用心、组件持续更新

---

### [assistant-ui · 面向 AI 智能体的前端库](https://www.assistant-ui.com/?ref=tailwindweekly.com)

**原文标题**: [assistant-ui · The frontend library for AI agents](https://www.assistant-ui.com/?ref=tailwindweekly.com)

assistant-ui 是面向 AI 智能体的前端库，提供生产级聊天原语与运行时，可通过适配器连接任意后端，并支持高度可组合、可定制的聊天界面。

- 🚀 定位为 AI Agent 的前端库，提供生产聊天所需的 primitives 与 runtime。
- 🔌 通过适配器支持任意后端，兼容 AI SDK、LangGraph、LangChain、Mastra 和自定义运行时。
- 📈 项目数据亮眼：13k GitHub stars、310 万周下载量，并获得 Y Combinator 支持。
- 🧠 运行时统一管理线程、流式输出和工具调用；使用 provider、hook 和组件即可接入。
- 🧩 支持流式响应、推理、工具、审批、来源、附件、分支、建议、语音和生成式 UI 等能力。
- 🎨 每个部分都是可组合组件，CLI 可将 UI 源码复制到你的仓库，便于深度定制。
- 🖥️ 覆盖 React、Vue、React Native 和 Ink；示例展示路由运行模型、transport 流式返回。
- ☁️ Assistant UI Cloud 可托管线程与持久化，让会话跨刷新保留并持续积累上下文。
- 🛠️ 提供 `npx assistant-ui@latest create` 新建项目和 `init` 初始化现有项目。
- 📜 当前版本为 `@assistant-ui/react@0.15.32`，采用 MIT License。

---

### [一个精美的 SVG 标志库 - SVGL](https://svgl.app/?ref=tailwindweekly.com)

**原文标题**: [A beautiful library with SVG logos - SVGL](https://svgl.app/?ref=tailwindweekly.com)

该内容是一个按 A-Z 排序的 Logo 目录，共收录 676 个品牌或产品标识，涵盖 AI、软件、数据库、设计、开发工具等多个类别。

- 📚 **目录规模**：共 676 个 Logo，按字母顺序排列，并以品牌或产品名称和所属类别展示。
- 🛠️ **开发工具**：包括 LogBrew、Depot 等。
- 🗄️ **数据库**：包括 Cockroach Labs、Xata 等。
- 🤖 **AI 类别**：包括 TypeSafe AI、Mastra、Cerebras、Leedlime、Conductor、Codex、OpenClaw、OpenCode、Glide 等。
- 📊 **分析与平台**：包括 Retain、Orshot 等。
- 🧩 **软件类别**：包括 TanStack、Postqued、ClickUp、Trello、Runframe、Interfere、Stripe、Render、vlt 等。
- 🎨 **设计类别**：包括 Grida、Photopea 等。
- ₿ **加密与主题**：包括 Nano 和 Dracula。
- 📄 **重复项**：Acrobat Reader 和 Adobe 的标识在列表中重复出现。

---

### [Kokonut UI：免费开源的 React 与 Tailwind 组件](https://kokonutui.com/?ref=tailwindweekly.com)

**原文标题**: [Kokonut UI: Free Open-Source React & Tailwind Components](https://kokonutui.com/?ref=tailwindweekly.com)

Kokonut UI 是一个免费开源的 React 组件目录，基于 React、Tailwind CSS、Motion 与 shadcn/ui 构建，主打可即时体验、可单文件安装、代码归开发者所有的动画与交互组件。

- 🧩 共提供 102 个组件，覆盖背景、卡片、导航、输入、AI、媒体、文本、按钮等类别。
- 🎛️ 每个组件均有实时演示，用户可先试用，再通过一条命令或一段 AI 提示词安装。
- 🆕 最新更新标注为 2026 年 10 月 22 日，新增 8 个组件，包括 Card Field、Stay Picker、Slot Picker 等。
- 🤖 支持 AI Agent 安装：描述需求后，编辑器中的 Agent 会从 registry 查找并安装组件及其依赖。
- 💻 支持 shadcn CLI 安装，例如 `npx shadcn@latest add @kokonutui/particle-button`。
- 🔗 也可在 `components.json` 中添加 `@kokonutui` 命名空间，之后用短名称引用组件。
- 🧠 采用 shadcn/ui registry 模式，组件以源码形式进入项目仓库，并自动处理依赖。
- ✨ 示例组件包括 Apple Activity Card、Slide to Confirm、Detent Dial、AI State Loading、Tear Button、Drape Background、Wheel Picker、Plucked Text、Pull Cord、Activity Terrain、Liquid Gauge、Bell Button 等。
- 💬 获得 shadcn/ui 创作者及多位开发者推荐，被认为是值得了解的 React/shadcn UI 组件库。
- 💎 提供付费版 Kokonut UI Pro：120+ 组件、20+ 类别、6 个模板，覆盖 Heroes、应用界面、定价、AI 部件和完整网站模板。
- 🖼️ Pro 模板包括 Marlow 作品集、Fleet AI Agent 发布站、Agenta 创业公司站点等，单售 59 美元或包含在 Pro 中。
- 💰 Pro 为一次性付费，现价 119 美元；原价 159 美元，使用 PRO25 可享 25% 折扣、省 40 美元，包含现有与未来组件/模板及后续版本。

---

### [Shadcnblocks shadcn/ui 区块与组件](https://www.shadcnblocks.com/?ref=tailwindweekly.com)

**原文标题**: [Shadcnblocks shadcn/ui blocks & components](https://www.shadcnblocks.com/?ref=tailwindweekly.com)

Shadcnblocks 于 2026 年 10 月 30 日更新 406 个新区块，定位为面向 Shadcn UI、Tailwind 与 React 的完整区块库，提供 2866 个区块、2241 个组件和 22 个模板，覆盖营销页、仪表盘、电商、主题、设计套件、页面构建器、IDE 扩展及多种安装方式，并采用一次性终身定价。

- 🧱 本次更新新增 **406 个区块**，持续扩充 Shadcn UI 与 Tailwind 生态资源。
- 📦 资源规模包括 **2866 个区块、2241 个组件、22 个模板**，可直接复制粘贴或通过 Shadcn CLI 安装。
- 🖥️ 区块类别涵盖 Dashboard、Hero、Feature、Pricing、Contact、Product List、Product Detail、Bento、Testimonial、Data Table、Chart Group 等。
- 🧩 所有区块和组件均为 React 组件，支持 Next.js、Vite、Astro、Remix，并提供 **Radix UI、Base UI、React Aria** 三种 primitive 构建。
- 🎨 提供 **39 个 Shadcn 主题**，支持明暗模式、自定义字体及一行 CLI 安装。
- 🛠️ 另有 **Shadcn Figma Kit**、**Shadcn Admin Kit**、**Shadcn Page Builder** 和 **Shadcn IDE Extension** 等设计与开发工具。
- ⚙️ 支持通过 **Shadcn CLI、Shadcn MCP、IDE 扩展、Shadcnblocks App** 四种方式安装或使用区块。
- 💳 定价为终身买断：**Standard $149、Pro $299、Elite $399**；高阶方案包含模板、Figma Kit、Admin Kit、97+ 预构建页面和 Page Builder。
- 📈 平台数据显示：**22,162 名免费用户、5,420 名 Pro 客户、约每日 10,000 次安装**，成立于 2023 年，并保持每月新增组件、区块、页面和模板。

---

### [HextaUI — 用于 shadcn/ui 的 React 组件与区块](https://hextaui.com/?ref=tailwindweekly.com)

**原文标题**: [HextaUI — React components and blocks for shadcn/ui](https://hextaui.com/?ref=tailwindweekly.com)

HextaUI 提供基于 shadcn/ui 和 Base UI 的 React 组件库及 Pro AI 聊天 UI 区块，帮助开发者在周末而非数周内上线 AI 应用聊天界面，覆盖流式输出、工具调用、语音和智能体状态等复杂交互。

- 🚀 **快速上线 AI 聊天 UI**：Pro 区块可直接嵌入，省去处理流式传输、工具调用、语音和智能体状态的数周开发时间。
- 💬 **完整聊天体验**：支持聊天线程、流式文本、中途停止与重试、消息版本切换，以及模型输出时线程不跳动。
- 🛠️ **高级交互状态**：包含工具调用审批、智能体待办、思考过程、代码块与差异对比、语音模式等。
- 🎙️ **Prompt Input 能力强**：支持模型与推理强度选择、听写、提及、命令和文件上传。
- 👀 **实时预览与安装**：所有 Pro 区块都可在线试用，并通过 shadcn CLI 从私有注册表安装。
- 💰 **Pro 定价**：2026 年 11 月 30 日前，单人 $49、10 人团队 $149；之后 Solo $79、Team $249。
- 🔁 **买断与退款**：一次付款覆盖全部 55 个 Pro 区块及未来新增区块，支持 30 天无理由退款。
- 🧩 **免费开源基础**：包含 65 个组件、9 个 Hooks、5 个工具函数，采用 MIT 许可证，可免费用于个人和商业项目。
- ♿ **重视边缘状态与可访问性**：组件内置加载、错误、空状态，支持键盘操作、屏幕阅读器、可中断动画、320px 布局和从右到左语言。
- 🧱 **技术栈明确**：基于 React 19、Tailwind CSS v4、Base UI 和 Tabler 图标，兼容 shadcn/ui 项目。
- 📚 **面向人和 AI 的文档**：文档提供 Markdown 版本和 llms.txt，并提供只读 MCP 服务器，方便 Claude Code、Cursor 等助手查询组件与示例。
- 🔓 **代码归你所有**：CLI 将源码复制到项目中，可阅读、修改和保留，不依赖包更新。

---

### [Glance。原生 macOS Markdown 查看器](https://glance.md/?ref=tailwindweekly.com)

**原文标题**: [Glance. Native macOS markdown viewer](https://glance.md/?ref=tailwindweekly.com)

Glance 是一款面向 macOS 的原生 Markdown 编辑器与查看器，体积约 15.0 MB，主打快速查看和轻量编辑；它可即时打开 .md 文件，原生渲染 Mermaid、LaTeX、表格和代码，采用“免费阅读、Pro 解锁编辑”的模式。

- 📄 原生 Markdown 支持：可即时查看 .md、.markdown、.mdown、.mkd、.mkdn 文件，也支持代码、JSON、YAML、CSV、日志等带语法高亮和行号的视图。
- ⚡ 轻量快速：仅 15.0 MB，采用原生引擎，不依赖 WebView；支持在 Finder 中按空格键 Quick Look 预览，也支持用 ⌘F 在文件内查找。
- 📊 数学与图表：LaTeX 和 Mermaid 均可原生渲染，代码与配置文件有语法颜色和行号。
- 🖱️ 智能缩放：围绕鼠标指针捏合缩放，可放大页面任意内容。
- 📁 文件夹与自动保存：用 ⌘O 打开文件夹后，Markdown 文件会显示在侧边栏，输入即保存，并且不会向文件夹添加索引或配置文件。
- ✍️ Pro 编辑功能：可在页面上直接输入，或按 ⌘\ 并排查看 Markdown 源码；支持内联格式、表格编辑、Mermaid 源编辑，并可 ⌘↩ 更新。
- 💰 价格与试用：阅读永久免费；Pro 编辑提供 14 天试用，无需信用卡和注册；一次性 $9.99，最多覆盖 3 台 Mac，含 1 年更新。
- 🔒 隐私与联网：仅检查更新和验证 Polar 许可证；远程图片会下载；无分析、无追踪，可关闭更新检查。
- 💻 系统要求：支持 macOS 14 Sonoma 及以上，仅限 Apple Silicon；无 Intel 构建，也没有 iPad/iOS 版本且暂无计划。

---

### [设计系统迁移的视觉回归测试 · UI Verify](https://uiverify.ai/blog/design-system-migration-visual-regression?ref=tailwindweekly.com)

**原文标题**: [Visual regression testing for a design system migration · UI Verify](https://uiverify.ai/blog/design-system-migration-visual-regression?ref=tailwindweekly.com)

overview summary
本文说明设计系统迁移中的视觉回归测试方法：先在旧系统上为所有页面和状态建立基线，再按切片迁移，并把截图差异归类为预期 token 变化、布局重排或真实破坏；自研前后对比与宽松阈值容易漏报，Tailwind 升级工具也可能漏改已移除的类，需结合 grep、按分支基线和审查工具完成规模化复核。

- 🧭 **定义与价值**：迁移改变的是 UI 底层 token 或组件层，代码审查无法判断 200 个屏幕最终长什么样，视觉回归测试用于在合并前发现真实破坏。
- 🧪 **实测设置**：文章用 12 页 Tailwind v3 商店站，Playwright 以 1280px 截图，运行官方升级工具后用 pixelmatch 对比。
- ⚠️ **自研检查盲区**：为忽略预期噪声而放宽阈值，会连真实变化一起忽略；默认阈值 0.1 下仅 5/12 页被标记，评级标签 8px 重排被标出，产品图标透明度破坏却未标出。
- 🧱 **升级工具漏改**：Tailwind v4 移除了 `bg-opacity-*`、`text-opacity-*`、`border-opacity-*`，升级工具未改这三类，导致元素退回完全不透明。
- 💥 **真实破坏示例**：删除店铺弹窗背景由半透明变实心，89% 像素变化；幽灵按钮边框变实、产品图标失去半透明，后两者容易混在大量预期调色变化中发布。
- 🗂️ **执行顺序**：迁移分支开始前先在 main 上基线所有页面；覆盖弹窗、空态、错误态和窄视口，而不只覆盖路由。
- 🍰 **切片迁移**：先单独跑 codemod，再换 token，再换组件；每个 PR 只引入一种原因，使每个 diff 的审查问题更简单。
- 🔍 **差异分类**：把每张截图差异分为预期 token 变化、布局重排、真实破坏；批量接受预期变化，重点看无人能解释的差异。
- 🧹 **搜索移除项**：升级指南列出的移除工具类和重命名 props 要逐个 grep，弥补 codemod 无法重写的情况。
- 🛠️ **审查工具帮助**：按分支维护基线，AI 结合 PR 描述标记“可能预期”或“可能回归”，支持批量接受、自动忽略 flake，并用“本 PR vs base”查看整体 UI 变更。
- 🚦 **核心规则**：不要靠放宽比较阈值让测试变绿；让每个页面变化都出现，按原因解释，并把注意力放在无法解释的变化上。

---

### [用数学平衡你的标题样式——克雷格·阿博特](https://www.craigabbott.co.uk/blog/2026/using-maths-to-balance-your-heading-styles/?ref=tailwindweekly.com)

**原文标题**: [Using maths to balance your heading styles - Craig Abbott](https://www.craigabbott.co.uk/blog/2026/using-maths-to-balance-your-heading-styles/?ref=tailwindweekly.com)

文章介绍一种基于模块化比例的六级标题样式系统：以正文基准字号和统一比例为起点，按字号、间距、字重的优先顺序建立可访问的视觉层级，并用数学半步解决 h4 字号断层。
- 📐 以模块化比例统一计算标题字号与间距，默认比例 1.5、基准 1.2rem，避免随意像素值。
- 🔍 标题区分不能只靠颜色，还需考虑强制颜色模式；同时避免斜体、全大写等对阅读障碍者不友好的方式。
- 🥇 视觉线索优先级：字号最强，其次间距，最后字重；强线索用完再用弱线索并适当重叠。
- 🔠 h1–h3 分别使用 s3、s2、s1，h4–h6 初始落到正文字号 s0；标题不应小于其引导的正文。
- ↔️ 用 flow-space 控制正文流间距，标题上方加大间距，标题下方缩小间距以关联后续内容。
- ⚖️ h6 字重降至 500，使其与 h5 和 strong 区分；需使用具备相应字重的优质字体。
- 🧮 h4 使用几何平均数/半步：s0 × sqrt(ratio)（或 pow(ratio, 0.5)）得到约 23.5px，填补 19–28px 断层且仍受比例约束。
- 🧩 也可用 pow() 直接从基准计算每一步，变量名与计算一致，结果与链式计算相同。
- ♿ 最终系统不依赖颜色，仍可通过可选颜色增强；在 forced-colors 模式下层级仍成立。
- 🛠️ 作者主张用系统化比例替代“像素完美”微调，保证标题与间距始终协调且易维护。

---

### [通行密钥的工作原理——Mystic Coders](https://howdopasskeyswork.com/?ref=tailwindweekly.com)

**原文标题**: [How do passkeys work — Mystic Coders](https://howdopasskeyswork.com/?ref=tailwindweekly.com)

overview summary
通行密钥以本地私钥签名、网站用公钥验证的方式替代“发送密码”：注册时保存公钥，登录时提交与本次挑战绑定的证明，生物识别/PIN 不上传。
- 🔑 核心区别：密码把秘密发给网站；通行密钥只发送证明，网站用事先保存的公钥核验。
- 🛠️ 创建与授权：新账户可首设通行密钥；现有账户添加通常需先用现有方式登录或恢复流程授权。
- 💾 保存选择：可存于密码管理器（如 Apple Passwords、Google Password Manager、1Password）、本设备（如 Windows Hello）或物理安全密钥。
- 📱 本地批准：用面部、指纹或设备 PIN 授权；检查只在本机进行，网站不会收到生物识别或 PIN。
- 🧾 注册细节：服务器发随机挑战与网站身份等信息，认证器生成密钥对；私钥留在认证器/提供商，公钥随注册响应交服务器保存。
- 🔏 登录细节：服务器发新挑战；认证器用私钥对认证器数据和客户端数据哈希签名，响应绑定本次挑战与来源。
- ✅ 服务器校验：检查签名、挑战、来源、RP ID 与必要标志，全部通过后才建立会话；旧响应不能复用。
- 🚫 仿冒防护：浏览器按真实来源/RP ID 限制凭证，假网站不能直接使用真实网站的通行密钥；复制响应也受原挑战和上下文限制。
- 💾 丢失与同步：部分通行密钥可跨设备同步，部分绑定单设备或安全密钥；应提前设置备份或账户恢复方式。
- ⚠️ 边界：不能修复被攻破设备、被盗会话或弱恢复流程；是否保留密码取决于网站。
- 🧪 演示与实现：文中动画为模拟，不创建真实通行密钥；服务端通常需注册/登录的 options 与 verify 端点，并自行管理账户授权、挑战生命周期、凭证存储、会话和恢复。

---

### [免费订阅追踪与管理器 | Subfaro](https://subfaro.com/en/?ref=tailwindweekly.com)

**原文标题**: [Free Subscription Tracker & Manager | Subfaro](https://subfaro.com/en/?ref=tailwindweekly.com)

Subfaro 是一款订阅追踪与管理工具，帮助用户集中查看所有订阅、在免费试用结束和续费前收到提醒、发现涨价，并计算月度与年度总支出；无需登录银行账户，支持免费套餐和 Pro 付费套餐，覆盖网页、Android、Chrome 扩展及 AI 助手等使用方式。

- 📊 将所有订阅集中在一个地方，清晰查看每项服务的费用与续费情况。
- ⏰ 提供免费试用结束提醒和续费前提醒，避免意外扣费。
- 📈 自动监测官方价格变化，发现涨价并提醒用户更新账单金额。
- 💰 内置订阅费用计算器，可按月/年统计总支出，并显示分类占比。
- 👥 共享订阅只计算用户自己的分摊部分，家庭计划更准确。
- 🔎 覆盖 Netflix、Spotify、ChatGPT Plus、Hulu、HBO Max、YouTube Premium 等热门服务，价格每周检查。
- 🚫 无需连接银行账户或银行卡，不获取银行密码，强调数据隐私。
- 🧾 为目录内服务提供直接取消链接和步骤指南，但不能替用户直接取消。
- 🆓 免费版最多追踪 10 个订阅，包含自动价格、涨价提醒、扣费/试用提醒、分类统计、CSV 导出和 Claude 连接器。
- ⭐ Pro 版为 $2.99/月或 $24.99/年，提供无限订阅、完整省钱建议、详细月报、日历同步、价格历史、自定义分类、WhatsApp 提醒等。
- 📱 支持 Android App、网页版、iPhone 添加到主屏幕、Chrome 扩展一键添加订阅。
- 🤖 可连接 Claude 等 MCP 兼容 AI 助手，通过聊天添加订阅，并可选择只读或可编辑权限。
- 💬 Pro 用户可通过 WhatsApp 接收提醒和管理订阅，每月最多 100 条消息。
- 🔐 用户可导出数据、随时删除账户，Pro 可随时取消且保留数据。

---

### [GitHub - unlayer/react-image-editor 位于 tailwindweekly.com · GitHub](https://github.com/unlayer/react-image-editor?ref=tailwindweekly.com)

**原文标题**: [GitHub - unlayer/react-image-editor at tailwindweekly.com · GitHub](https://github.com/unlayer/react-image-editor?ref=tailwindweekly.com)

这是一个将 Unlayer Image Editor 封装为 React 组件的开源项目，支持图片裁剪、缩放、滤镜、绘制、文字、形状、贴纸、边框以及可选的 AI 助手；要求 React >= 18，采用 MIT 许可证。

- 🖼️ 核心功能：提供 crop、resize、filter、draw、text、shapes、stickers、frame 八种编辑工具，默认全部启用。
- 📦 安装使用：通过 `npm install @unlayer/react-image-editor` 安装，使用 `<ImageEditor />` 组件并传入图片 URL 或 base64。
- ⚙️ 主要 Props：包括必填的 `image`，以及 `options`、`minHeight`、`style`、`wrapperStyle`、`ariaLabel` 和各类回调。
- 🔄 回调事件：支持 `onLoad`、`onSave`、`onCancel`、`onLoadError`、`onError`，分别处理加载、保存、取消和错误。
- 🧩 Ref API：暴露 `editor` 实例，可调用 `getImage()`、`hasChanges()`、`reset()`、`updateOptions()`、`destroy()`。
- 🧠 属性更新行为：`image` 变化会重置并清空撤销/重做和 AI 聊天；`theme`、`locale`、`translations` 热更新；其他 `options` 会触发重挂载。
- ⚠️ 错误处理：`onLoadError` 针对图片加载失败；`onError` 针对嵌入脚本、编辑器创建或图片重置等包装层失败。
- 🛠️ 工具配置：可通过 `features.imageEditor.tools` 启用/禁用工具、自定义图标或设置工具栏位置，但该配置变更会重建编辑器。
- 🤖 AI 助手：可选聊天式编辑功能，需要 Unlayer `projectId`，并启用 `features.ai.enabled` 与 `assistant`。
- 🌍 本地化与演示：内置 en、es、fr、de、it、pt、nl、ja、ko、zh 等语言，支持自定义翻译；提供在线 Demo 和本地 Vite 示例。
- ⭐ 项目信息：仓库约 265 stars、29 forks，兼容 React Server Components，带 `'use client'` 指令。

---

### [RenderPixels · 像素级精准的图像，直接来自 Claude](https://renderpixels.com/?ref=tailwindweekly.com)

**原文标题**: [RenderPixels · Pixel-exact images, straight from Claude](https://renderpixels.com/?ref=tailwindweekly.com)

RenderPixels 是一款通过 MCP 连接 AI 助手的图像渲染工具：用户用自然语言提出需求，Claude、ChatGPT、Muse、GrokBot 或 Cursor 负责设计，RenderPixels 按平台所需尺寸生成可直接使用的图片，并能在聊天中直接查看、下载或复制链接。

- 🖼️ 图片可直接显示在 Claude 聊天中，支持下载和复制 URL，无需离开对话。
- 🤖 支持 Claude、ChatGPT、Muse、GrokBot、Cursor 等 AI 助手，通过 MCP 连接器接入。
- 💬 用自然语言描述文字、颜色和风格，AI 负责版式设计，RenderPixels 负责精确尺寸渲染。
- 📐 覆盖 Open Graph、X、LinkedIn、Instagram、Stories、YouTube 缩略图和完整 favicon 套件等尺寸。
- 🎨 可保存品牌套件（颜色、字体、Logo），按名称调用，确保每次渲染符合品牌。
- 🔗 每个文件都有永久 URL，可直接用于网页、meta 标签或消息分享。
- 🆓 每月 50 次免费渲染，无需信用卡，每月 1 日 UTC 重置。
- 💳 超出免费额度后可购买一次性 credit 包，1 credit = 1 次渲染，完整 favicon 套件也算 1 次。
- ⏳ Credits 永不过期：2,000 个/$10、6,000 个/$25、15,000 个/$50、40,000 个/$100。
- ⚙️ 设置简单：注册并验证邮箱后，将 MCP 服务器 URL 添加到 AI 助手；Claude、Claude Code、ChatGPT、GrokBot 等均有对应接入方式。
- 🔐 使用邮箱和密码进行 OAuth 登录，无 API key；不支持 OAuth 的助手无法连接。
- 📌 示例包括单次提示生成 Open Graph 图、favicon 套件、Logo、横幅和 Instagram 帖子。

---

### [Jog · 用于智能体规模开发的 GitHub 运行器](https://usejog.com/?ref=tailwindweekly.com)

**原文标题**: [Jog Â· GitHub runners for agent-scale development](https://usejog.com/?ref=tailwindweekly.com)

Jog 是面向 agent 规模开发的 GitHub Actions runner 替代方案，核心卖点是只需修改一行 `runs-on` 配置即可迁移，并显著降低 CI 成本，支持按秒计费、自动缓存和多种 agent 工具集成。

- 🚀 迁移简单：将 workflow 中的 `runs-on: ubuntu-latest` 改为 `runs-on: jog`，除 runner 外基本无需改动其他工作流。
- 💰 成本优势明显：比 GitHub 便宜约 80%，比 Blacksmith 和 WarpBuild 便宜约 70%；1,000 分钟在 GitHub 为 $6，在 Jog 为 $1.20。
- 🎁 免费与计费：每月提供 5,000 免费分钟，按秒计费，无订阅、无最低消费。
- ⚙️ 零配置缓存：Actions cache 可自动工作，无需额外配置。
- 🧩 Agent 集成：可粘贴到 Claude Code、Codex、Pi、OpenCode 等 agent 中开始使用。
- 📊 价格档位：Jog 为 2 vCPU $0.0012/分钟；Jog Max 为 2 vCPU $0.0024/分钟，使用双倍免费分钟，比 Blacksmith 低 40%。
- 🏷️ 同级价格对比：2 vCPU 下 Jog $0.0012、Jog Max $0.0024、Namespace $0.003、Blacksmith/WarpBuild $0.004、GitHub/Depot $0.006/分钟。
- ⏱️ 短任务更省：按秒计费避免按分钟取整；百万个 25 秒任务可节省 $1,750–$3,500（Jog）或 $2,950–$5,900（Jog Max）。
- 🖥️ 规格与环境：提供 2–32 vCPU 多档规格，每个任务运行在全新 VM 上；基于 Ubuntu 24.04 和 GitHub runner 工具，少数大型工具需自行安装。
- 👤 账户与额度：支持个人 GitHub 账户私有仓库；预付费额度未使用可退，免费分钟及赠送额度不可退。

---

### [Handy](https://handy.computer/?ref=tailwindweekly.com)

**原文标题**: [Handy](https://handy.computer/?ref=tailwindweekly.com)

Handy 是一款开源、本地运行的语音转文字应用，用户可通过快捷键录音并自动将转写内容粘贴到当前文本输入框；它强调免费、开源、隐私和简单易用，并提供 Apple Silicon 版 v0.10.0 下载。

- 🎙️ Handy 是开源语音转文字工具，可在自己的电脑上运行，按下快捷键说话并松开后，内容会自动粘贴到正在输入的文本框中。
- ⚙️ 设置简单：默认启用“按住说话”模式，也可关闭为按一次开始、再按一次停止转写。
- ⌨️ 支持自定义快捷键，示例中映射为 Ctrl-Z；录制时 Mac 顶部会出现转写图标提示。
- 🆓 免费提供无障碍工具，不应被付费墙限制。
- 🧩 开源可扩展，用户可自行扩展并为项目做贡献。
- 🔒 隐私友好，语音保留在本地电脑，无需上传音频到云端即可获得转写。
- 🧰 功能专注：只做一件事，把用户说的话转写并放入文本框。
- 💎 项目有赞助商支持，包括 Wordcab、Epicenter、Bolt AI、Canty Digital，也接受捐赠、GitHub Sponsors 或直接联系赞助。
- 💻 页面提供 Handy 下载信息：Apple Silicon 版 v0.10.0；若浏览器不支持 HTML 视频，可选择直接下载视频。

---

### [交付代码——构建真实系统，而非教程](https://shipthatcode.com/?ref=tailwindweekly.com)

**原文标题**: [Ship That Code — Build Real Systems, Not Tutorials](https://shipthatcode.com/?ref=tailwindweekly.com)

该平台主打“从零构建真实系统并用真实执行器证明其可用”：学习者重建 Redis、Git、数据库、操作系统内核等，从空文件开始，直到在统一评分器上通过测试。平台免费，提供 179 门课程、37 条语言轨道和 8 条职业路径，首个测试约 2 分钟即可开始。

- 🛠️ 核心理念是“构建真实产物，再证明它能运行”：要么通过测试，要么不通过。
- 🧪 每道练习都在真实执行器上评分，并配有隐藏测试，避免“看起来正确”就算通过。
- 🎯 项目产物是真实系统：Redis 能被真实 redis-cli 连接，Git 能被 git log 读取，内核能启动。
- 💻 可使用平台编辑器，也可关联 GitHub 仓库；每次 push 都会评分，README 徽章实时更新进度。
- 🏅 证书只在所有评分练习通过后颁发，包含公开验证页、凭证 ID，且无需付费购买。
- 📚 课程覆盖 Build Redis（29 课）、数据库（34 课）、Git（18 课）、编程语言（38 课）、容器运行时（19 课）、Shell（16 课）、OS 内核（24 课）、神经网络（25 课）、HTTP 服务器（16 课）、Transformer（14 课）、文本编辑器（14 课）、TLS 1.3（14 课）等。
- 🧭 提供 8 条职业路径，例如 Backend Engineer 约 80 小时、8 门课程，覆盖 Go、SQL、Redis、HTTP、OAuth 等。
- 🎓 教育者和研究者可申请课程同行评审，姓名会展示在课程页，并获得可验证的同行评审证书。
- 🔍 同行评审采用版本化审查流程，确保课程修改可追踪，不会静默重写。
- ⏱️ 第一个可完成的测试约需两分钟，平台强调免费永久使用、无需信用卡。

---

