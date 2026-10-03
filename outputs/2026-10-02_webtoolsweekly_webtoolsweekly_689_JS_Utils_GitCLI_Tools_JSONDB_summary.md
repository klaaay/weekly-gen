### [STRICH | 面向 Web 应用的条形码扫描](https://strich.io/?ref=wtw)

**原文标题**: [STRICH | Barcode scanning for web apps](https://strich.io/?ref=wtw)

overview summary
STRICH 是一款面向 Web 应用的 JavaScript SDK，可在浏览器中通过摄像头实时扫描 1D/2D 条码。它完全在客户端处理、无需后端，内置扫描 UI，零依赖，兼容主流框架，并以透明订阅制定价和企业级支持面向开发者与业务。

- 📦 通过 `npm i @pixelverse/strichjs-sdk` 安装，可从 NPM 或 CDN 使用，TypeScript 绑定，零依赖。
- 🌐 完全浏览器端处理，无需后端，支持 Android/iOS 主流浏览器和高端/低端设备。
- 🔍 支持广泛 1D/2D 码：Code 128、EAN、UPC、Code 39、ITF、QR、MicroQR、Data Matrix、Aztec、PDF417 等。
- 🖥️ 内置扫描 UI：Popup Scanner、瞄准覆盖、相机选择、闪光灯、点击对焦；一行代码可调用。
- ⚡ 使用 WebAssembly 和 WebGL，实时解码，快速可靠，可读取褪色/损坏、光照不均、反色条码。
- 🧩 兼容 Angular/Vue/React/SvelteKit 等框架，提供示例代码，集成通常不到一天。
- 🆚 对比 ZXing-JS、QuaggaJS 等开源方案：STRICH 有维护、商业支持、内置 UI，困难条件下读取率更高。
- 📱 Web 应用优势：无需应用商店、通过链接/QR 分发、始终最新、降低 iOS/Android 开发成本、减少应用疲劳。
- 🏢 企业级能力：定期更新、安全合规、可选离线操作、零网络流量、可信/分阶段 NPM 发布、创始人直接支持。
- 💰 定价：Basic €99/月（1 万次扫描）、Professional €249/月（10 万次扫描）、Business €4,000/年起（无限扫描/设备，按应用数）、Enterprise 定制。
- 🆓 提供 14 天免费试用，无限设备、无限应用、可随时取消；超额不阻断扫描，连续两月超额需 7 天内升级。
- 🤝 客户评价强调：性能和价值好、准确、易集成、跨设备可靠、户外条件可用，并有从 Scandit/Dynamsoft 迁移案例。
- 🛒 采购友好：Paddle 作为 Merchant of Record，支持采购订单、银行转账、供应商注册、经销商和 OEM 许可。
- 🇨🇭 Pixelverse GmbH 位于瑞士，是瑞士 GS1 解决方案合作伙伴，支持 GS1 条码标准。

---

### [](https://github.com/SacDeNoeuds/yawn)

**原文标题**: [GitHub - SacDeNoeuds/yawn: The forever v1 JSX library (embryo) mirroring Web Standards & APIs · GitHub](https://github.com/SacDeNoeuds/yawn)

Yawn 是一个主张“永久 v1”的极简 JSX 前端库胚胎，核心理念是镜像 Web 标准与 API，并用原生 AsyncIterable 实现响应式，从而减少 JavaScript 疲劳。目前仍属概念验证，仓库约 24 stars；若达到 5,000 stars，作者将推进生产可用并寻求贡献者。

- 🧠 作者顿悟：前端自 2018 年起已拥有响应式能力，即 Async Iterables；首个值是初始状态，后续 `yield` 是状态更新。
- ⚛️ 主流框架各自造响应式系统：React `useState`、Vue `ref`、Angular RxJS/Signals、Svelte stores/runes、Solid Signals，导致 API 不断变化。
- 🌐 Yawn 的目标是让“懂 Web 标准与 API ⇔ 懂库 API”，API 按设计保持不变，告别 JavaScript 疲劳。
- 🧩 JSX 直接返回 HTML 元素；事件小写如 `onclick`；属性沿用 `class`、`for`；只额外增加 `ref`。
- 🔁 响应式由 AsyncIterable 驱动；可写状态用 `State` 类，提供 `set(nextValue)` 与 `update(prev => next)`。
- 🪝 生命周期用 `onConnected` / `onDisconnected`，替代 `useEffect`、`onMount` 等概念。
- 📦 体积很小：渲染部分约 2.6kB，JSX runtime 约 1.5kB gzipped。
- 🧪 已有 demo 与示例：Counter、Todo 派生状态、connected/disconnected 生命周期等。
- ✅ 优点包括：纯标准 JS、复用生态、惰性求值、细粒度拉取式响应式，并可接入 WebSocket、SSE、ReadableStream。
- ⚠️ 待探索与缺点：数组状态渲染、SSE 组合 JSX、内存泄漏、Async Iterator 学习曲线，以及相比 Signals 缺少自动依赖追踪。
- ⭐ 项目当前约 24 stars；若达 5,000 stars，作者将开始生产化并寻找贡献者。
- 🤝 可通过 GitHub issue 参与讨论，贡献前可参考 `VALUES.md` 了解作者对前端库/框架的价值观。

---

### [](https://paraglidejs.com/)

**原文标题**: [Paraglide JS](https://paraglidejs.com/)

Paraglide JS 是一个编译器优先的国际化（i18n）方案，适用于 React、TanStack Start、SvelteKit 及任何 Vite 应用，通过将消息编译为类型安全的 ESM 函数，实现更小的打包体积、完整的类型安全和一流的 SSR 支持，是 SvelteKit 官方及 TanStack Router 端到端测试采用的 i18n 集成方案。

- 🚀 **核心定位**：编译器优先的 i18n，将消息编译为类型安全的 ESM 函数，适用于 React、TanStack Start、SvelteKit 及任何 Vite 应用
- 📦 **打包体积优势**：通过消息级 tree-shaking，i18n 打包体积最多可减少 70%（47 KB 对比 i18next 的 205 KB，5 个语言环境、200 条消息场景）
- 🎯 **完全类型安全**：消息键和参数支持自动补全，拼写错误会变成编译错误
- 🌐 **内置 i18n 路由**：开箱即用的基于 URL 的语言检测和本地化路径
- 🧩 **开放本地化格式**：基于 inlang，通过 `project.inlang/settings.json` 配置，翻译文件保留在版本控制中（如 `messages/en.json`）
- 🛠️ **广泛框架支持**：React、Vue、TanStack Start、SvelteKit、React Router、Astro、Vanilla JS/TS
- ⚡ **SSR 就绪**：通过服务端中间件和 AsyncLocalStorage 实现请求作用域的语言环境处理，并发请求中也能正确解析
- 🔗 **路由协同**：应用保留 `/about` 等规范路由，Paraglide 负责将 `/en/about`、`/de/ueber` 等本地化 URL 映射到规范路由
- 🚀 **快速上手**：一条命令 `npx @inlang/paraglide-js init` 自动创建消息文件、配置打包器并生成类型安全函数
- ✍️ **富文本支持**：通过 `@inlang/paraglide-js-react` 等类型化标记适配器，让翻译者控制链接和强调位置
- 🔢 **多语言格式化**：基于声明式格式化器支持复数、数字、日期时间和相对时间，兼容 ICU、i18next、JSON 等格式
- 🧠 **编译器优先原理**：构建时编译而非运行时字典查找，使 tree-shaking 和类型检查成为可能，且消息库增长时体积保持稳定
- 📊 **对比优势**：相比 Lingui 和 i18next，Paraglide 在 tree-shaking、类型安全、路由与 SSR 方面具有独特优势
- 🔄 **迁移友好**：可通过 i18next 插件编译现有 i18next 翻译文件，逐步从 `i18next.t("key")` 迁移到类型化消息函数
- 🌱 **生态工具**：Sherlock VS Code 扩展、CLI 自动化机器翻译、Fink 网页翻译编辑器、Parrot Figma 管理工具
- 💬 **开发者好评**：被评价为"市面上最好的 i18n 方案"，有开发者从 i18next 迁移后 i18n 包体积从 40KB 降至约 2KB
- 📜 **开源许可**：MIT 许可，`@inlang/paraglide-js` 已发布 v2 生产就绪版本

---

### [2D物理](https://xem.github.io/2Dphysics/)

**原文标题**: [2Dphysics](https://xem.github.io/2Dphysics/)

2Dphysics v1.1 是一个号称“世界最小”的 JavaScript 2D 物理引擎，支持弹簧和关节，提供注释源码、压缩版和 Micro 版，并附带 API 说明、示例代码与演示。

- 🧩 体积小巧：注释源码约 20kb，压缩版约 1.5kb zip，Micro 版无关节约 1.2kb zip。
- ⚙️ 全局参数：G=[0,.1] 为重力，O=.4 为重叠修正，E=.01 为固定关节弹性，R=20 为每帧求解次数；H/J/M 分别保存形状、关节和流形。
- 🔵 形状与关节类型：RECTANGLE=0、CIRCLE=1；SPRING=0、REPULSIVE=1、HINGE=2、FIXED=3。
- 🛠️ 核心 API：shape、anchor、joint、transform、run，分别用于创建形状、锚点、关节、变换形状和运行模拟。
- 📐 数据格式：中心、锚点、偏移等均为 [x,y] 数组；形状选项包括摩擦 f、恢复系数 r、角度 a、速度 v、角速度 A、重力 g、自定义数据 d 等，mass=0 表示固定形状。
- 🎮 渲染器不包含在发布中，但提供示例；示例涵盖简单渲染与游戏循环、矩形/圆形创建、弹簧/排斥/固定/铰链关节和运动学形状。
- 🧪 Demo 可点击重启；Micro 版功能有限，只能支持部分示例；更多代码片段位于 demo 下方。
- 📜 许可为公共领域，作者 Xem，2025；源码与 making-of 在 GitHub 提供。

---

### [Templatical — 开源电子邮件编辑器 SDK](https://templatical.com/)

**原文标题**: [Templatical — Open-Source Email Editor SDK](https://templatical.com/)

Templatical 是一款开源、拖拽式邮件编辑器 SDK，可通过一次 init() 调用嵌入任意应用，内置自定义区块、主题、合并标签和显示条件，支持 MJML 输出、多框架、零运行时依赖且无许可证密钥；同时提供编码代理 Agent Skill 和可选的 Templatical Cloud。

- 🧩 开源拖拽式邮件编辑器 SDK，一次 init() 即可嵌入应用。
- ⚛️ 框架中立：支持 React、Svelte、Angular、Vue 和原生 JS，零运行时依赖。
- 🛠️ 内置自定义区块、完整主题、合并标签和显示条件。
- 📝 TypeScript 优先，基于 MJML，采用 FSL-1.1-MIT（自动转 MIT）。
- 🛡️ Shadow DOM 样式隔离，内置 WCAG 无障碍检查与自动修复。
- 🔓 无许可证密钥、无激活调用、无遥测，功能不会被远程禁用。
- 📦 体积小：初始 172 kB，懒加载 418 kB。
- 🤖 开源 Agent Skill 可在现有编码代理中编写、导入、验证和预览模板，并辅助集成。
- ⚡ 一条命令添加：npx skills add templatical/sdk，无需后端或 API Key。
- ☁️ Templatical Cloud 可选托管 AI 聊天、MCP、实时协作、多租户和 API 访问。
- 🆚 对比自建：省去拖拽、嵌套、分栏、撤销/重做、合并标签作用域、显示条件、媒体库、保存区块、版本历史、测试发送、预览解析、暗色预览、MJML、兼容性、无障碍和样式隔离等大量工程。
- 🆚 对比 SaaS 构建器：核心功能不按席位/套餐收费，避免自定义区块、显示条件、主题、白标、媒体库、保存区块等被付费墙限制。
- 🆚 相比 Easy Email Pro：运行时独立，无许可证密钥/client ID、无远程功能开关、无遥测，模板留在自有应用内。
- 💾 模板可存自有后端，支持自动保存、版本历史、评论、测试发送和自有 ESP 发送。
- 🔄 提供 8 个免费 MIT 许可导入器，可导入现有模板。
- 🚀 快速开始：npm install @templatical/editor @templatical/renderer，JSON 输入，MJML 输出，可任意渲染。

---

### [](https://github.com/Oaxoa/fp-filters)

**原文标题**: [GitHub - Oaxoa/fp-filters: A curated list of ready-to-use (functional programming) array filters (TS / ESM / CJS) · GitHub](https://github.com/Oaxoa/fp-filters)

fp-filters 是由 Oaxoa 维护的 npm 包，提供 130+ 个常用过滤函数，采用函数式编程风格，旨在减少重复编写 filter 代码并提升可读性；函数均为谓词，返回布尔值，适合用于数组 filter、find 等场景。

- 📦 项目信息：GitHub 仓库为 Oaxoa/fp-filters，npm 包名为 fp-filters，文档地址为 oaxoa.github.io/fp-filters。
- 🎯 核心价值：停止重复编写相同过滤逻辑，大幅提高可读性，让开发者可能不再需要自己写过滤函数。
- 🧩 导入方式：所有函数按语义分组并单独导出，例如 `fp-filters/number/isEven.js`，没有 barrel 文件或统一入口。
- 🌳 按需打包：只导入和打包实际使用的函数，天然 tree-shakeable，成本以字节计算。
- 🧠 覆盖类别：包含布尔、日期、长度、杂项、数字、对象、位置、字符串、类型、数组等过滤函数。
- ✨ 函数特性：纯函数、多数为一行、可组合、大多零依赖，部分仅依赖零依赖的 fp-booleans。
- 🧪 测试保障：100% 按设计测试，覆盖每个分支和每一行，130+ 个稳定单元测试运行时间少于 1 秒。
- 🟦 类型支持：全部使用 TypeScript 类型化，无 any 类型，少量 unknown，仍在改进中。
- 🔁 否定与组合：多数函数提供否定别名，如 isNot、isNotEmpty；也可用 fp-booleans 的 not、and、or 自行组合。
- 🗂️ 语义分组：按数字、字符串等类别组织，便于直观查找所需函数。
- 🚀 安装方式：`npm install --save fp-filters` 或 `yarn add fp-filters`。
- 🤝 贡献与许可：提供贡献指南和行为准则；采用 MIT 许可证，Copyright 2023-present Pierluigi Pesenti (Oaxoa)。
- 📈 仓库状态：162 次提交，91 个 star，0 个 issue，0 个 pull request，1 个 watcher，0 个 fork。

---

### [](https://tanstack.com/pacer/latest)

**原文标题**: [TanStack Pacer](https://tanstack.com/pacer/latest)

Pacer beta 为噪声事件与异步工作提供统一的时序模型，涵盖防抖、节流、限流、队列和批处理，并让状态可观测，帮助决定什么运行、何时运行以及压力下如何表现。

- ⏱️ 核心定位：为事件与异步任务建立共享计时模型，应对抖动、并发与背压。
- 🔀 五种策略：Debounce、Throttle、Rate limit、Queue、Batch，分别解决不同产品问题。
- 🧭 选择原则：按可承受的丢失、延迟、采样或分组来选择策略，而不是凭记忆挑定时器。
- 🔍 Debounce：保留最新值并等待静默，适合搜索输入；代价是等待安静。
- 🎛️ Throttle：保留规律采样并丢弃中间项，适合指针更新。
- 🚧 Rate limit：只保留额度内调用并拒绝超额请求，适合 API 请求。
- 📥 Queue：保留每个任务并控制并发，适合文件上传；示例为并发/2、最多重试 2 次。
- 📦 Batch：保留每个项目并分组执行，适合分析写入。
- 🚦 异步流量控制：队列把大量 Promise 变成显式流量，支持顺序、优先级、并发、过期、重试与取消。
- 📈 可观测状态：可查看 status、executions、pending、last run，并通过订阅状态渲染进度。
- 🧩 可观测设计：定时器不再是黑箱，可订阅执行计数、待处理工作、错误与状态，并在 devtools 检查同一模型。
- 🛠️ 架构：包含 core、框架适配器与 devtools，可按需单独采用 core。
- 📊 采用数据：总下载 69.9M，周下载 6,282,968，GitHub 776 stars。
- 🤝 赞助与合作伙伴：Gold、Silver、Bronze 与 OSS Sponsors；赞助者可获私有 Discord、优先 issue 请求与直接支持。

---

### [](https://github.com/jespervos/blossom-carousel)

**原文标题**: [GitHub - jespervos/blossom-carousel: Native-first carousel enhanced with drag support for pointer devices. · GitHub](https://github.com/jespervos/blossom-carousel)

Blossom Carousel 是一个基于原生浏览器滚动的轮播库，通过为指针设备提供拖拽增强，同时保留真实滚动容器的性能、可访问性与核心交互模型，并支持 React、Vue、Svelte、Web Components 等框架。

- 🥇 原生滚动：完整保留浏览器滚动的性能与可访问性。
- 🚀 拖拽支持：为所有指针类型提供基于物理的自定义拖拽体验。
- ➡️ 导航控件：内置上一张、下一张和圆点导航，圆点渲染可自定义。
- ✨ 无抽象：兼容所有原生 Web API。
- 💡 CSS 配置：支持 CSS scroll-snap、position: sticky、滚动驱动动画等。
- 🪶 触屏设备 0kb：仅在检测到精细指针设备时加载。
- 🧱 框架就绪：提供 React、Vue、Svelte 和 Web Components 组件。
- 🚧 实验性循环滚动：支持轮播无限循环。
- 📦 安装方式：Vue、React、Svelte、Web Component、Core 均可通过 npm 安装对应包。
- 🤖 Agent Skills：帮助 AI 编码助手提供包专属指导，可通过 npx skills add https://www.blossom-carousel.com 安装。
- 🧩 示例：提供按复杂度分组的可直接复制轮播模式。
- 🔁 迁移指南：支持从 Embla、Swiper、Splide、Slick、Flickity 迁移。
- 📊 项目状态：Apache-2.0 许可，约 1k stars、38 forks、6 watchers、165 commits、2 issues。

---

### [](https://github.com/dlvhdr/diffnav)

**原文标题**: [GitHub - dlvhdr/diffnav: A git diff pager based on delta but with a file tree, à la GitHub. · GitHub](https://github.com/dlvhdr/diffnav)

diffnav 是一个基于 delta 的 git diff 分页器，带 GitHub 风格文件树，使用 Bubble Tea 构建 TUI，支持安装、管道输入、全局 pager、watch 模式、丰富配置、图标主题和快捷键操作。

- 📦 仓库为 dlvhdr/diffnav，公开项目，MIT 许可证，约 1.6k stars、49 forks、159 commits，并包含 Issues、PR、Discussions、Actions、Security 等板块。
- 🧭 核心定位：基于 delta 查看 diff，但提供类似 GitHub 的文件树界面。
- 💖 项目支持赞助，设有 TUI Innovator、TUI Visionary、TUI Power User、TUI Backer 等赞助等级。
- 🍺 Homebrew 安装：`brew install diffnav`，也可用 `brew install dlvhdr/formulae/diffnav`。
- 🐹 Go 安装：克隆仓库后进入目录执行 `go install .`。
- 🔤 图标需安装 Nerd Font 并在终端中选择该字体，也可通过 brew cask 安装。
- 🔀 直接管道使用：`git diff | diffnav`，或 `gh pr diff <URL> | diffnav`。
- ⚙️ 可设为全局 Git diff pager：`git config --global pager.diff diffnav`。
- 🚩 主要 Flags：`--side-by-side/-s`、`--unified/-u`、`--watch/-w`、`--watch-cmd`、`--watch-interval`。
- 👀 Watch 模式可周期性重跑 diff 命令并自动刷新，适合监控未暂存、已暂存或指定分支差异；默认命令为 `git diff`，默认间隔 2s。
- 📁 配置文件搜索顺序：`$DIFFNAV_CONFIG_DIR/config.yml`、`$XDG_CONFIG_HOME/diffnav/config.yml`、`~/.config/diffnav/config.yml`、系统特定配置目录。
- 🎛️ 配置项包括：隐藏页眉/页脚、显示文件树、文件树宽度、搜索面板宽度、图标风格、按 Git 状态着色、显示 diff 统计、并排视图、文件夹展开深度、主题等。
- 🎨 图标风格支持 `nerd-fonts-status`、`nerd-fonts-simple`、`nerd-fonts-filetype`、`nerd-fonts-full`、`unicode`、`ascii`；默认主题为 `tokyo_night`，可按 `T` 选择主题。
- ⌨️ 常用快捷键：`j/k` 上下导航，`n/p` 切换文件，`Ctrl-d/u` 滚动 diff，`e` 切换文件树，`t` 搜索文件，`y` 复制路径，`i` 切换图标，`o` 用 `$EDITOR` 打开，`s` 切换并排/统一视图，`Tab` 切换窗格，`T` 打开主题选择，`q` 退出。
- 🛠️ 技术栈：Bubble Tea 构建 TUI，Bubbletint 负责主题，delta 负责查看 diff；截图使用 kitty、tokyonight 和 CommitMono。
- 💬 社区支持：有 Discord 社区，贡献指南位于 `https://www.gh-dash.dev/contributing`。

---

### [](https://github.com/Fast-Editor/Lynkr)

**原文标题**: [GitHub - Fast-Editor/Lynkr: Streamline your workflow with Lynkr, a CLI tool that acts as an HTTP proxy for efficient code interactions using Claude Code CLI. · GitHub](https://github.com/Fast-Editor/Lynkr)

Lynkr 是面向 Claude Code、Cursor、Codex 等 AI 编程工具的 LLM 网关/HTTP 代理，通过 token 压缩、语义缓存、分层路由与成本可观测性，在不改代码的情况下降低 token 消耗与模型费用，并连接本地与 14+ 云提供商。  
- 🚀 核心数据：JSON 工具结果减少 84% token，工具密集型请求减少 53%，语义缓存命中低于 300ms，支持 14+ LLM 提供商，0 代码改动。  
- 🧩 工作方式：剥离未用工具、压缩 JSON、语义缓存、按复杂度路由、从结果学习；下游可接 Ollama、Bedrock、Azure、OpenRouter、OpenAI 等。  
- 🛠️ Wrap 模式：`lynkr wrap claude` 可为 Claude Code Pro/Max 提供分层路由、粘性会话、TOON/RTK 压缩、语义缓存，并支持 OAuth 与 API key。  
- ⚡ 快速开始：`lynkr init` 交互配置，或复制 `.env.example`；本地测试可先装 Ollama 并拉取 `qwen2.5-coder`，然后 `lynkr start`；Cursor/Codex 将 Base URL 指向 `http://localhost:8081/v1`。  
- 🧭 分层路由：按 SIMPLE、MEDIUM、COMPLEX、REASONING 自动路由；结合锚嵌入、LLM 难度分类、风险关键词、自主代理检测，会话指纹粘性，任务变大时自动升级。  
- 📉 路由效果：70-90% 请求走更便宜/更快模型；相比仅锚点基线，昂贵层过度路由减少 15 倍（0.6% vs ~15%）。  
- 💾 Token 优化：RTK 工具结果压缩、MCP 工具去重、请求绕过始终开启；可开 `PROMPT_CACHE`、`SEMANTIC_CACHE`、`CAVEMAN` 简明输出模式。  
- 🏁 基准 vs LiteLLM：TOON 压缩 60 项 grep JSON 从 3458 降至 427 token（少 87.6%，便宜 50%）；语义缓存二次调用 171ms（11 倍快），0 token 计费。  
- 🧪 路由头对头：同一后端与提示下，Lynkr 11/11 正确；LiteLLM Auto Router v2 启发式 4/11、LLM 分类器 6-8/11 且非确定，常见系统性地把复杂任务下路由到 7B 本地模型。  
- 📊 RouterArena：ICLR 2026、8400 查询中，Lynkr 路由得分 67.65 arena / 68.41% 准确率，$0.29/1K 查询，92.38 鲁棒性，高于 GPT-5 内置路由器和 NotDiamond。  
- 📈 成本影响：10 万请求/月 TOON 工具密集场景，LiteLLM ~$818 vs Lynkr ~$409；日常编码 8 小时用 Lynkr+Ollama 免费，云方案每月约 $60-240，而非 Anthropic 直连 $300-900。  
- 🖥️ 内置仪表盘：`http://localhost:8081/dashboard` 展示花费/节省、层级混合、路由准确性、请求日志、提供商健康、洞察、探索透视、会话下钻、缓存收据，并提供 JSON API。  
- 📌 Claude Code 状态行：配置 `lynkr-statusline` 可在每轮后显示路由层级、服务模型、今日花费、缓存重读占比，且不消耗 token。  
- 🧠 高级功能：实时 SSE 流式（原生透传/跨格式转换）、成本与模型定价追踪、Titans 风格记忆、负载削减、管理热重载、可选 Graphify AST 代码智能。  
- 📦 安装方式：NPM 推荐 `npm install -g lynkr`，也支持一行安装脚本、Homebrew、Docker Compose、从源码构建。  
- ⚠️ 常见问题：`pino-pretty` 旧版报错升级到 9.3.0+；缺 tier 配置只是警告；Ollama 需 `ollama serve`；连接拒绝检查 8081 端口；慢首请求可设 `OLLAMA_KEEP_ALIVE=30m`。  
- 🆚 对比替代品：比 LiteLLM/OpenRouter/PortKey 更强调 Claude Code/Cursor/Codex 原生接入、本地模型、TOON 压缩、语义缓存、路由准确性、仪表盘与成本建议。  
- 📜 项目信息：Apache 2.0 许可，作者 Vishal Veera Reddy；社区含 GitHub Discussions、Issues、NPM、DeepWiki。

---

### [TermDOM | 使用 HTML、CSS 和 DOM 构建终端应用](https://termdom.org/)

**原文标题**: [TermDOM | Build terminal apps with HTML, CSS, and DOM](https://termdom.org/)

TermDOM 是一个 JavaScript/TypeScript 库，让你用 HTML、CSS 和 DOM API 构建终端应用；它渲染真实 DOM 节点并在变更时自动重绘，使 TUI 和交互式 CLI 能用原生 JavaScript 或任意前端框架编写。

- 🧱 实现符合规范的 DOM 与 CSSOM API：创建 div、设置样式、append 到 body，无需手动 render，变更自动绘制。
- 🎨 使用真实 CSS 级联：运行样式表和行内样式，将计算样式输出为 ANSI 转义序列，并映射终端调色板与粗体、斜体、下划线、删除线。
- 📐 采用浏览器布局算法：用 flexbox、grid、表格和盒模型在字符单元格网格上排版，1px 与 1ch 都表示一个单元格。
- 🔄 支持文本换行与终端缩放重排，内容会随终端尺寸变化重新布局。
- ⌨️ 将 stdin 转义序列解码为 DOM 事件：keydown 派发到焦点元素，click 派发到指针下元素，paste 携带粘贴文本。
- 🧭 Tab 可移动焦点，:focus 样式会跟随焦点变化，适合构建表单和交互式界面。
- 🧩 可复用浏览器生态：Prism 等浏览器库无需修改即可运行，多数前端框架只需少量设置。
- 🃏 示例涵盖 Klondike 纸牌、Hello World、flexbox 布局、表单交互和 Prism 语法高亮。
- 📊 尽量遵循 Web 规范，仅在终端中无意义的概念上做例外，并提供兼容性表。
- 📦 入门方式：npm install @b9g/termdom，可查看 getting started、examples 页面和 GitHub 源码。

---

### [](https://meco.app?utm_campaign=3nux)

**原文标题**: [Meco: The #1 newsletter reader | Declutter your inbox](https://meco.app?utm_campaign=3nux)

Meco 是一款专为阅读 newsletter 打造的聚合阅读器，可将邮件简报从拥挤的收件箱转移到专门阅读空间，减少干扰并整理订阅。支持连接 Gmail/Outlook 或使用专属 Meco 邮箱，并提供 AI 摘要、音频简报、筛选分组、发现推荐、书签笔记、高亮、一键退订、离线阅读及多平台支持。

- 📥 将 newsletter 移出收件箱，集中到专为阅读设计的空间，快速清理邮箱。
- 🔗 可连接现有 Gmail 或 Outlook 快速导入订阅，也可申请专属 Meco 邮箱来订阅。
- ⚙️ 使用流程：连接邮箱/创建 Meco 邮箱 → 添加或订阅 newsletter → 在 Meco 中阅读并保持收件箱清爽。
- 🧠 智能筛选与分组，帮助聚焦最相关、最有趣的内容。
- 🎧 AI 每日音频摘要：用 5–10 分钟个性化播客汇总订阅中的关键新闻。
- 📝 提供 AI 文本摘要和每周摘要，快速获取重点，避免错过重要洞察。
- 🔍 个性化发现：根据阅读内容、兴趣和热门趋势推荐 newsletter。
- 🔖 书签、标签、笔记与高亮：保存、标注、分类文章，构建第二大脑。
- 🚫 一键退订，轻松移除不再需要的订阅。
- 📱 支持 iOS、Android 和网页端，可离线阅读。
- 💳 通过付费订阅盈利，不投放广告、不出售数据；可随时断开 Gmail/Outlook 并恢复简报回收件箱。
- 🔒 强调隐私安全：不存储或处理邮件数据，邮件仅保存在本地设备。
- 🌐 面向创作者提供合作计划与提交 newsletter，页面还包含 FAQ、联系与法律信息，可免费开始使用。

---

### [](https://github.com/Arindam200/gitpack)

**原文标题**: [GitHub - Arindam200/gitpack: AI-powered Git packaging CLI for planning commits, drafting PRs, and tracking reviews from the terminal. · GitHub](https://github.com/Arindam200/gitpack)

gitpack 是一款 AI 驱动的 Git 命令行工具，旨在帮助开发者将零散的工作整理成可审查的提交，并在终端内追踪代码审查进度，无需切换至 GitHub。它默认启用 AI（Nebius Token Factory），用于优化提交信息、分组理由和 PR 摘要，同时保持核心逻辑的确定性，AI 不可用时自动回退到启发式建议。

- 🛠️ **核心功能**：`plan`（规划提交）、`apply`（交互式应用提交）、`pr`（生成 PR 草稿）已实现，视图层和交接命令在路线图中
- 📦 **安装方式**：支持全局安装 `npm install -g @arindam1729/gitpack` 或通过 `npx` 直接运行
- 🤖 **AI 默认启用**：默认使用 Nebius Token Factory，模型为 `moonshotai/Kimi-K2.5`，可通过环境变量切换至任意 OpenAI 兼容服务
- ✂️ **智能提交分组**：自动将相关文件（如 `foo.ts` 与 `foo.test.ts`）归入同一提交，并解释分组理由
- ⚠️ **风险预警**：标记认证、数据库 schema、环境变量、CI 等高风险路径的变更
- 🔁 **交互式提交**：逐个审阅建议的提交信息，支持接受、编辑、AI 重新生成或跳过
- 📊 **终端仪表盘**：`gitpack status` 单屏展示分支状态、提交记录、PR 审查和 CI 检查结果
- 👀 **视图命令**：`view diff/comments/checks/log` 无需打开 GitHub 即可查看差异、评论和 CI 失败详情
- 🚀 **发布辅助**：`gitpack release` 按类型分组提交生成发布说明，支持 `--draft` 和 `--publish`
- 🔒 **安全与回退**：`gitpack undo` 可撤销上一次 `apply`，默认安全、透明、可脚本化
- 🧭 **设计原则**：默认安全、零配置可用、核心确定性、AI 增强但不依赖 AI、对操作透明
- 📜 **开源许可**：MIT 许可证，当前 7 颗星，仓库包含 `docs`、`src` 等目录

---

### [](https://worktrunk.dev/)

**原文标题**: [Worktrunk — Git worktree management for parallel AI agent workflows](https://worktrunk.dev/)

Worktrunk 是一个面向并行 AI 代理工作流的 Git worktree 管理 CLI，用简洁的核心命令把 worktree 操作变得像分支一样容易，并提供 hooks、缓存共享、LLM 提交与交互选择器等增强功能。

- 🤖 面向并行 AI 代理：支持同时管理 5-10+ 个 Claude Code、Codex 等代理，让每个代理拥有独立工作目录。
- 🌳 简化 Git worktree：以分支名寻址，路径由可配置模板计算，命令也可接受 worktree 路径。
- ⚙️ 核心命令：`wt switch`、`wt list`、`wt remove` 覆盖切换、查看和清理等日常操作。
- 🚀 创建并启动：`wt switch -x claude -c feature-a -- '任务'` 可创建 worktree、切换并运行命令。
- 🪝 自动化 hooks：支持 create、pre-merge、post-merge、post-start 等阶段自动执行命令。
- 📝 LLM 提交信息：可根据 diff 生成提交信息，`wt merge` 可自动完成 squash、rebase、合并与清理。
- 🔍 交互式选择器：浏览 worktree，并预览 CI 状态、diff、日志、PR 和评论；`wt list --full` 显示 CI 与 AI 摘要。
- 💾 共享构建缓存：在 APFS、btrfs、XFS 上让多个 worktree 复用 `target/`、`node_modules/` 等，无需重复构建或复制。
- 🌐 PR 与开发服务器：`wt switch pr:123` 可直接检出 PR 分支；`hash_port` 可为每个 worktree 分配唯一端口。
- 🧩 扩展能力：支持别名、按分支变量、自定义 `wt <name>` 命令，以及更多工作流模式。
- 📦 安装方式：支持 Homebrew、Cargo、Windows Winget、Arch Linux、Conda/Pixi；安装后运行 `wt config shell install` 启用 shell 集成。
- 📚 后续步骤：学习核心命令、配置 hooks、探索 LLM 提交、交互选择器、Claude Code 集成、CI/PR 链接与 tips/patterns；当前版本 v0.80.0，许可证为 MIT OR Apache-2.0。

---

### [](https://github.com/tesserato/CodeWeaver/)

**原文标题**: [GitHub - tesserato/CodeWeaver: Weave your codebase into a single, navigable Markdown document · GitHub](https://github.com/tesserato/CodeWeaver/)

CodeWeaver 是一个用 Go 编写的命令行工具，可将代码库递归扫描并生成单个可导航的 Markdown 文档，嵌入目录树与文件内容，便于代码分享、文档化以及集成到 AI/ML 工具中。

- 📦 项目信息：tesserato/CodeWeaver，公开仓库，741 stars，58 forks，采用 MIT 许可证。
- 🧩 核心功能：递归扫描目录，生成树状文件结构，并把每个文件内容放入基于扩展名的 Markdown 代码块。
- 🎯 路径过滤：支持 `-include` 白名单和 `-ignore` 黑名单正则表达式，精确控制包含或排除哪些文件。
- 📝 路径记录：可选将包含或排除的文件路径保存到单独文件中，便于追踪。
- 📋 剪贴板支持：使用 `-clipboard` 可将生成的 Markdown 复制到系统剪贴板。
- ⚙️ CLI 选项：包括 `-input`、`-output`、`-ignore`、`-include`、`-included-paths-file`、`-excluded-paths-file`、`-clipboard`、`-version`、`-help`。
- 📥 安装方式：推荐 `go install github.com/tesserato/CodeWeaver@latest`，需 Go 1.18 及以上；也可从 releases 下载预编译可执行文件。
- 🚀 基本用法：运行 `codeweaver` 默认扫描当前目录，生成 `codebase.md`，默认忽略 `\.git.*`。
- 🔎 include/ignore 规则：只用 `-include` 时仅包含匹配项；二者同时使用时，包含匹配 `-include` 且不匹配 `-ignore` 的路径。
- 🧪 使用示例：可指定输入输出、忽略 `.log/temp/build`、只包含 `.go/.md`、组合过滤、保存路径列表、复制到剪贴板等。
- 🔤 正则说明：列出 `.`、`*`、`+`、`?`、`[abc]`、`^`、`$`、`\.`、`\|` 等常用元字符及示例。
- 🧾 完整示例：`codeweaver -input=. -output=codebase.md -ignore="..." -include="..." -excluded-paths-file="excluded_paths.txt" -clipboard`。
- 🤝 贡献与许可：欢迎提交 issue 或 pull request，项目使用 MIT License。
- 🧭 替代工具：提到 ai-context、code2prompt、RepoMix、gitingest、onefilellm 等，以及 r2md、repo2txt、repoprompt 和 VSCode 扩展等类似方案。

---

### [](https://github.com/metaory/glitcher-cli)

**原文标题**: [GitHub - metaory/glitcher-cli: CLI to generate animated pseudo-random glitch SVG effects from unicode characters · GitHub](https://github.com/metaory/glitcher-cli)

metaory/glitcher-cli 是一个公开 GitHub 仓库，提供从 ASCII/Unicode 字符生成动态伪随机故障 SVG 的 CLI 工具，并已有在线 Web 应用。
- 🎨 功能：从 ASCII 字符生成带伪随机故障动画的 SVG。
- 🌐 Web 应用：Glitcher Web App 已上线，地址为 metaory.github.io/glitcher-app。
- 🎲 随机属性：切片数量、切片高度、颜色通道偏移、动画时长、关键帧时间和帧值均随机。
- ⭐ 仓库数据：99 个 Star、2 个 Fork、4 个关注者、19 次提交；Issues 和 PR 均为 0。
- 📁 主要文件：.github、LICENSE、README.md、glitcher。
- ⚙️ 安装：克隆仓库，赋予执行权限，并链接到 $PATH，例如 /usr/bin/glitcher。
- 🚀 使用：`bash glitcher out.svg hello world` 可创建内容为 hello world 的 out.svg。
- 📜 命令格式：`glitcher FILE TEXT...`
- 🧰 依赖：GNU Bash v5+、GNU bc、GNU coreutils（sort、uniq）。
- 🛠️ TODO：增加 noise、density、color、font 参数及 help。
- ⚠️ 注意：目前仅在 Linux 上测试。
- 📄 许可：MIT License；并包含行为准则、贡献指南与安全政策。
- 🏷️ 主题：cli、glitch、glitch-art、pin、svg、svg-animations、svg-filters、svg-generator。

---

### [](https://github.com/uhop/stream-json)

**原文标题**: [GitHub - uhop/stream-json: A micro-library of stream components for building custom JSON and JSONC processing pipelines with a minimal memory footprint — parse, filter, and transform JSON far larger than available memory with a SAX-inspired token API, on Node.js or Web Streams. · GitHub](https://github.com/uhop/stream-json)

stream-json 是一个用于流式处理 JSON/JSONC 的微库，能以极低内存解析远超可用内存的大文件，通过 SAX 风格令牌/事件 API 和可组合管道按需提取、过滤、转换数据。

- 🧩 基于 stream-chain 构建，各组件是管道阶段，可与普通函数、生成器、Node/Web 流组合，并内置 TypeScript 类型。
- 🧠 最小内存占用：无需用 JSON.parse 全量加载，可流式解析超大文档，甚至逐段处理键、字符串和数字。
- 🎯 精准提取：pick、ignore、replace、filter 只保留目标子对象，跳过的字节不会组装进内存。
- ⚙️ 核心流程：parser 把文本转为 token 流，filters 实时裁剪/重塑流，streamers 把保留下来的 token 组装成 JavaScript 对象。
- 🛡️ 适用数据：适合数据库转储、导出、日志和自有系统文件；不适合开放互联网或不可信用户的 JSON/JSONC。
- 💡 典型用法：从大于内存的 JSON 中提取数组并逐条统计；pick 匹配多个子对象时，可配合 streamValues 分别组装。
- 📦 安装方式：npm install --save stream-json；仅支持 ESM，运行于维护中的 Node、Bun、Deno 和浏览器。
- 🧰 内置组件：JSON、JSONL、JSONC 解析器，流式对象处理辅助工具，以及 parseFile、stringerToFile 等文件读写能力。
- 🚀 近期版本：3.7.0 为 FlexAssembler 规则新增 maxDepth，并优化字符串和 RegExp 过滤器性能；更早版本包含安全修复和 JSONC 注释流支持。
- 🔗 相关项目：stream-chain 是底层管道组合基础；stream-csv-as-json 可将大型 CSV 转为兼容 stream-json 的 token 格式。
- 📜 仓库概览：BSD-3-Clause 许可证，GitHub 约 1.2k stars、55 forks、536 commits。

---

### [GitHub -](https://github.com/columnar-tech/databow)

**原文标题**: [GitHub - columnar-tech/databow: A command-line tool for querying databases · GitHub](https://github.com/columnar-tech/databow)

databow 是 columnar-tech 开发的公开命令行数据库查询工具，基于 ADBC 和 Rust 构建，支持多数据库连接、交互式 SQL Shell、格式化输出与结果导出，仓库采用 Apache-2.0 许可证。

- 🛠️ 核心用途：通过 ADBC 从命令行查询数据库。
- 🗄️ 多数据库支持：可连接任何兼容 ADBC 的驱动。
- 💻 交互式 SQL Shell：支持命令历史和直观导航。
- 🎨 语法高亮：SQL 查询高亮显示，提升可读性。
- 📊 格式化输出：结果以整洁对齐的表格展示，列宽动态调整。
- 📁 文件导出：查询结果可导出为 JSON、CSV 或 Arrow IPC。
- ⚡ 快速轻量：使用 Rust 构建，高性能且资源占用低。
- 📦 安装方式：支持 uv、Cargo、Homebrew 安装。
- 🚀 快速开始：先用 dbc 安装 DuckDB ADBC 驱动，再运行 databow --driver duckdb。
- 🧪 非交互模式：支持 --query、stdin、--file 执行查询，并可用 --output 输出到文件。
- ⚙️ 主要参数：包括 --profile、--driver、--uri、--username、--password、--option、--mode、--query、--file、--output 等。
- 📈 仓库状态：约 269 stars、17 forks、8 issues、3 pull requests、115 commits。
- 📜 许可证：Apache-2.0。
- 🔖 相关主题：ADBC、Apache Arrow、CLI、database、SQL。

---

### [](https://mongogui.com/)

**原文标题**: [Mongo GUI | Native MongoDB workflow for macOS](https://mongogui.com/)

Mongo GUI 是 ILO APPLICATIONS SL 发布的独立第三方 macOS MongoDB 客户端，不是官方 Compass；它主打原生 Mac 工作流、行优先响应、重连恢复、本地密钥管理与隐私优先 AI。

- 🧭 原生 macOS 体验：Swift/SwiftUI 构建，三栏工作区、暗黑模式、Cmd+K 快速访问和系统级控件。
- 🔐 连接管理：支持 Direct、SRV、手动 URI、TLS、SSH，连接信息保存，凭据存入 Keychain。
- ⚡ 行优先性能：文档行、选择、查询编辑和分页优先保持响应，精确计数和元数据后台更新。
- 🔁 重连恢复：重连后返回活动数据库、集合、查询草稿、选择和可见工作区。
- 🗂️ 最近页面缓存：按连接、集合、查询、分页等缓存，提升重复访问速度。
- 🧰 文档操作：密集表格浏览、查询补全与过滤审查、结构化编辑、Extended JSON、预设与查询重放。
- 📤 导出与片段：支持 CSV/JSON 导出、聚合结果导出，可粘贴 AI 生成的 mongosh 片段并本地验证。
- 🧱 结构与运维：Schema 抽样、索引创建与批量删除、集合统计、聚合管道、Live Watch。
- 📊 仪表板与监控：Smart Create 仪表板、性能监控、Slow Query Advisor、慢查询和长运行操作洞察。
- 🤖 隐私优先 AI：可选侧栏、用户自有 OpenAI Key、评审优先、只读分析审查、更新前预览确认。
- 🛡️ 安全与分发：密钥本地保存、加密设置导出/导入、匿名分析、签名公证 DMG、Sparkle 更新。
- 💸 定价状态：Beta 期间免费，生产环境可用，暂无付费计划，正式定价未定。
- 🆚 推荐规则：需要官方免费默认工具可选 Compass；需要原生 Mac、响应式浏览、重连恢复、仪表板和 AI 片段验证则选 Mongo GUI。

---

### [](https://recommendations.page/web-tools-weekly/offer_recommendations/offer_recommendation_fe8b4765ca0d)

**原文标题**: [Web Tools Weekly - Recommendations Hub](https://recommendations.page/web-tools-weekly/offer_recommendations/offer_recommendation_fe8b4765ca0d)

此内容是一个订阅者专属优惠，但提示当前国家/地区不可用；它宣传以199美元获得价值14,000+美元的AI工具与权益，折扣高达98%，包含AI工具、额度、模板、福利和合作伙伴权益，面向希望更快应用AI的运营者、创始人和领导者。

- 🔒 订阅者专属优惠，但当前国家/地区无法使用
- 🏷️ 折扣高达98%，优惠来自 The AI Report
- 💳 一张卡即可解锁价值 $14,000+ 的AI工具
- 💰 价格为 $199，对应 AI Executive’s Pass
- 🧰 包含AI工具、额度、模板、福利和合作伙伴权益
- 🚀 面向运营者、创始人和领导者，帮助更快推进AI应用
- 🎯 行动号召：领取优惠（Claim Offer）

---

### [](https://slimsnap.ai/)

**原文标题**: [SlimSnap. Paste a screenshot into your terminal](https://slimsnap.ai/)

SlimSnap 是一款把截图转换为结构化 JSON 的工具，让无法读取图片的终端编程代理获得“视觉”。它通过本地 OCR、元素边界框和可导出标注，把 UI 截图变成可粘贴到任意文本环境的 JSON，使 Claude Code、Aider、Codex CLI 等代理能更准确地理解界面并定位要修改的元素。

- 📸 终端代理能读文件、跑测试、写代码，但不能接收图片；SlimSnap 用 JSON 填补 UI 沟通缺口。
- ✍️ 一张截图可替代约 200 字你本来要手写的界面描述。
- ⌨️ Mac 按 ⌘⇧S、Windows 按 Ctrl+Shift+S 选区截图；⌘⇧L / Ctrl+Shift+L 可捕获整页或滚动页面。
- 🖍️ 支持箭头、标注和高亮，标注导出为结构化“意图”，指向具体元素，减少代理猜测。
- 📋 一键复制 JSON，可粘贴到 Claude Code、Aider、Codex CLI、Cursor、Continue.dev，以及终端、SSH、CI 日志、git 提交等只接受文本的地方。
- 🧩 JSON 包含每个元素的文本、类型、颜色和归一化 0–1 边界框，布局确定，代理不必猜位置。
- 🔎 内建 OCR 读取标签、按钮和错误信息；暗色模式同样适用，极低对比度主题需注意。
- 🖥️ 全页捕获会拆分为可读帧，并提供覆盖整个页面的按序 JSON，避免超长图被 AI 下采样到不可读。
- 🔒 捕获与 OCR 本地运行，不上传、无账户、无服务器；连接器可让 Claude 直接读取本机最新捕获。
- 🧑💻 Claude Code skill 通过 ~/.slimsnap/config.json 查找保存目录和文件名模式，无硬编码路径；也可用于任何有效 SlimSnap JSON。
- 📜 JSON schema 在 GitHub 以 MIT 开源，可校验、手写或自建导出器；Claude Code skill 开源，但应用本体闭源。
- 🖥️ 支持 Mac Apple Silicon 与 Windows 10/11，功能一致；Linux 用户可发邮件请求。
- ⚖️ 对“修复特定元素”任务，JSON 比原图更可靠；对视觉风格探索，可贴原图，也可两者同时发送。
- 🆓 免费、无需注册，让终端代理“看得见”。

---

### [](https://www.doltgres.com/)

**原文标题**: [DoltgreSQL](https://www.doltgres.com/)

未提供任何可总结的文章内容，因此暂时无法生成摘要。请补充需要总结的文本，我会按指定格式输出中文要点。

- 📄 当前消息中只有总结指令，没有正文内容。
- 📝 无法提取关键信息或撰写概要。
- 📌 请提供文章或文本，我将按“- 表情符号 要点”的格式整理。
- ✅ 收到内容后，我会生成简洁、准确的中文摘要。

---

### [](https://github.com/discoveryjs/discovery)

**原文标题**: [GitHub - discoveryjs/discovery: A framework for ad hoc JSON data analysis, shareable server-less reports and dashboards · GitHub](https://github.com/discoveryjs/discovery)

overview summary
Discovery 是 discoveryjs 的开源框架，用于临时 JSON 数据分析、可共享的无服务器报告和仪表盘，并可作为高级 JSON 查看器或浏览器扩展使用。

- 📊 核心定位：面向 JSON 的即席数据分析、可共享无服务器报告与仪表盘。
- 🌐 使用方式：可在 GitHub 上作为高级 JSON 查看器，或以 Chrome、Edge、Firefox 扩展 JsonDiscovery 使用。
- 🧩 生态项目：JsonDiscovery、Statoscope（webpack 包分析）、CPUpro（CPU 分析）、CSS syntax reference、Jora Docs、CSSWG spec drafts index、react-native-bundle-discovery。
- 📝 文章教程：包括 Discovery.js 快速入门教程，以及 JsonDiscovery 改变浏览器查看 JSON 的方式。
- 🔗 相关项目：Discovery CLI 提供 CLI 服务/构建，Jora 是数据查询语言，Jora CLI 用于命令行处理 JSON。
- 📁 仓库结构：包含 .github、cypress、dist、docs、models、scripts、src 等目录，master 分支有 1,495 次提交。
- 📈 社区数据：423 stars、10 forks、22 issues、4 pull requests、12 watching。
- ⚖️ 许可证：MIT。
- 🏷 主题：data-analysis、data-visualization、json。

---

### [](https://json-structure.org/)

**原文标题**: [JSON Structure | JSON Structure is a data structure definition language that enforces strict typing, modularity, and determinism.](https://json-structure.org/)

JSON Structure 是一种数据定义语言，强调严格类型、模块化和确定性，旨在让数据结构定义能清晰地映射到编程语言类型、数据库结构以及 JSON 编码，并支持语义注解以供开发者和大型语言模型理解。

- 📋 **核心定位**：JSON Structure 是一种强数据定义语言，与 JSON Schema 不同，后者侧重点在文档验证，而前者侧重类型定义并兼顾验证
- 🧩 **语言特性**：提供清晰映射编程语言类型、精确数值与日期时间类型、模块化扩展、简化跨文档引用、类型复用、多语言描述与别名支持
- 📦 **扩展规范**：包含 Import、别名与描述、符号与单位与货币、验证、条件组合、关系、语义与参考系统注解等多个配套扩展
- 🛠️ **SDK 支持**：官方提供 TypeScript/JavaScript、Python、.NET、Java、Go、Rust、Ruby、R、Perl、PHP、Swift、C 等多语言 SDK，支持模式与实例验证
- 🔍 **VS Code 扩展**：提供内联诊断验证、关键字 IntelliSense、悬停文档和常见问题快速修复
- 📝 **示例展示**：通过 Product 模式演示了 uuid、string、decimal、double、datetime、set、map 等类型及别名、单位、货币等注解
- 📚 **配套文档**：包含 Primer 高层概览和 Core Specification 详细规范，面向不同层次的开发者
- 📰 **文章资源**：涵盖身份与关系、命名、单位、枚举翻译、联合类型、集合与映射、二进制数据、日期类型、小数与整数等丰富主题

---

### [](https://webtoolsweekly.com/contact?opt=classifieds)

**原文标题**: [Contact Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

本页面是 Web Tools Weekly 的广告联系页，用于查看广告方案、咨询广告位、讨论方案或预订广告，并说明该表单仅限广告咨询；一般咨询或工具投稿请通过其他渠道联系。

- 📢 广告咨询可先查看“Advertising Plans”页面上的方案。
- ✉️ 想了解当前广告位可用情况，请发送消息询问。
- 📝 若要讨论某个方案或预订广告位，请填写下方表单。
- ⚠️ 此表单仅用于广告咨询。
- 💬 一般咨询或提交工具，可通过 X 私信、Bluesky 聊天，或回复订阅的新闻邮件联系。
- 🧾 表单必填项包括：姓名、邮箱、广告链接、期望广告方案。
- 📌 广告方案选项：顶部广告+顶部文字链接、付费产品评测、中部图片广告、文字链接组合、分类广告、广告交换。
- 🗒️ 另有“评论/说明”栏可填写补充信息。

---

### [sheetscope · 将文档转变为可用 SQL 查询的](https://sheetscope.com/)

**原文标题**: [sheetscope · Turn documents into a database you can query with SQL](https://sheetscope.com/)

sheetscope 可将 PDF、电子表格、幻灯片或扫描件转换为可用 SQL 查询的数据库，让会 SQL 的分析师无需手动录入或写脚本，即可提取字段、跨文档查询并导出结果。

- 📄 支持上传 PDF、XLSX、PNG 等文件，自动读取文档内容。
- 🧩 可选择所需字段，如发票号、金额和日期，无需编写代码即可定义数据结构。
- 🗃️ 将文档提取为可查询数据表，示例中 3 个文件生成 3 行 4 列：vendor、invoice_no、amount、due_date。
- 🔎 用纯 SQL 跨所有文档一次查询，例如 `SELECT * FROM "invoices" WHERE amount > 1000;`。
- 🚀 三步完成：上传文档、描述字段、用 SQL 查询并导出为 CSV 或 JSON。
- 📂 能处理扫描发票、导出的电子表格、幻灯片、对账单等杂乱文件。
- 📊 字段可统一定义，每份文档都按相同结构返回，方便查询。
- 🌐 可对数百份文档运行同一条 SQL，如同它们是一个单一表。
- 📤 结果可复制到剪贴板，或下载 CSV/JSON 用于表格或 BI 工具。
- 🗂️ 可将文档分组到文件夹，并保存分析为可返回的 notebook。
- 👥 为团队设计，工作区对组织私有，成员基于同一份数据协作。
- ✅ 引导用户上传首批文件并立即运行查询。

---

### [学习 Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

**原文标题**: [Learn Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

您尚未提供需要总结的文本内容，因此暂时无法生成有效摘要。请补充文章内容，我会按要点提炼并保持简洁。

- ⚠️ 当前缺少待总结的文章或文本
- 📥 请直接粘贴或发送需要处理的内容
- 🧾 收到后将按“概述 + 要点”格式用中文总结
- ✅ 每个要点会使用“-”符号并搭配合适 emoji
- 🎯 重点提取关键信息、核心观点和必要细节

---

### [](https://www.onset.io/)

**原文标题**: [Onset - Keep customers in the loop on every release.](https://www.onset.io/)

Onset 是面向产品团队的发布说明与 changelog 平台，可借助 AI 快速起草、发布和通知更新，支持公共/内部发布说明、定时发布、多渠道提醒，以及编辑器和应用内集成。

- 🚀 快速生成：几分钟内写好发布说明，或让 AI 代理自动起草。
- 📣 客户触达：通过公开 changelog 展示最新更新和改进，让客户持续了解进展。
- 🧭 团队对齐：内部发布说明提供上下文、细节和洞察，保持团队同步。
- ✍️ 清晰沟通：AI 辅助将技术更新转化为用户愿意阅读的清晰公告。
- ⏰ 精准定时：可草稿、预览并设定发布上线时间，便于跨团队和时区协调。
- 🔔 一键通知：将发布提醒发送到 Slack、Discord 或电子邮件，无需切换工具。
- 🤖 AI 写作：把 pull request 和已完成任务转成精炼的客户可用发布说明。
- 🧩 编辑器发布：连接 Claude、Cursor 或任意 MCP 客户端，在现有工具中起草并发布到 changelog。
- 📱 应用内 Widget：将发布说明嵌入应用，用户无需离开即可获知更新。
- 💳 免费试用：可免费开始使用，无需信用卡。
- 📚 开发者资源：提供文档、MCP Server、REST API、Webhooks、Widget API 和 JavaScript SDK。
- 🔍 竞品对比：可与 AnnounceKit、Beamer、Changelogfy、Noticeable、Olvy、ReleaseNotes.io 比较。
- 📬 支持与合规：提供支持邮箱、GitHub、Twitter/X，以及隐私政策、条款、DPA、系统状态和 Cookie 说明。

---

### [FluentDB - 适用于 macOS 的 AI 数据库客户端](https://www.fluentdb.ai/)

**原文标题**: [FluentDB - The AI Database Client for macOS](https://www.fluentdb.ai/)

FluentDB 是一款面向 Mac 的 AI 原生数据库客户端，支持 PostgreSQL、MySQL、SQLite、SQL Server 等，主打快速、安全、AI-first 与 Apple Silicon 原生体验。它提供带安全护栏的 AI 辅助 SQL 编辑、数据浏览、自定义看板、MCP 控制和自带模型方案，并可一次性买断。

- 🧠 定位：Mac 上的 AI 数据库客户端，可连接 PostgreSQL、MySQL、SQLite、SQL Server 等。
- ⚡ 特点：快速、安全、AI-first，原生支持 Apple Silicon。
- 🛡️ AI 护栏：提供强安全保护，避免昂贵错误和数据泄漏。
- 💻 SQL 编辑器：面向 2026 重新设计，支持 schema 感知自动补全、格式化、即时结果、AI 模式和保存查询。
- 🔎 浏览体验：按 ⌘P 搜索并打开任意表或视图，操作顺畅。
- 📊 性能：即使超过 10 万行，数据网格仍可快速流畅滚动。
- 🗂️ 自定义看板：可将查询以图表和表格形式布局，随时回访。
- 🔌 MCP 与模型：可用 MCP 连接自己的 AI 代理；支持 Anthropic、OpenAI、Ollama，无自有模型，提示直连服务商或本地。
- 🗄️ 数据库支持：PostgreSQL、MySQL、SQLite、SQL Server 已可用；MongoDB、Redis、ClickHouse、MariaDB、Snowflake、BigQuery、DuckDB、Cassandra 即将推出。
- 🔐 隐私：默认 AI 只读 schema，不读行数据；连接和凭证存于 Mac Keychain，无需账户。
- 💰 价格：非订阅，一次性购买 54 美元起，许可证不过期，含一年更新，可选终身更新。
- ✅ 退款保障：无免费试用，但 14 天内未替代现有客户端可无理由退款。
- 🖥️ 平台：目前仅支持 macOS，原生适配 Apple Silicon，暂不支持 Windows/Linux。
- 🚀 口号：停止与数据库纠缠，一个客户端、一次付费、永久拥有，可下载 Mac 版。

---

### [获取失败](https://recs.page/web-tools-weekly?ref_code=fde5b5c207&lc=link_campaign_d8b9780aafe8&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recs.page/web-tools-weekly?ref_code=fde5b5c207&lc=link_campaign_d8b9780aafe8&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [获取失败](https://nitropack.io/)

**原文标题**: [Failed to retrieve](https://nitropack.io/)

无法总结：获取内容失败，状态码 403。

---

### [](https://www.paintbyjson.com/)

**原文标题**: [Paint By JSON â Design Figma against real API data](https://www.paintbyjson.com/)

Paint By JSON 是一款早期访问的 Figma 插件，可用真实、实时的 API 数据填充设计，像 Lorem ipsum 一样简单：一次保存映射，一键应用，帮助设计验证真实姓名、长度和边界情况，并统一设计与工程规格。

- 🔌 连接任意 API endpoint，可在插件内预览 JSON，支持 headers 和认证。
- 🗺️ 将 JSON 路径绑定到图层名称，按名称定位图层，让 Palette 跨文件、团队库和重构保持可移植。
- 💾 将 endpoint、headers 和映射保存为可复用 Palette，一键应用到任意 frame，支持跨文件共享。
- 🧱 支持单帧填充或集合模式，可将数组迭代到重复组件实例。
- 🛠️ 支持入站转换：截断文本、格式化货币、解析日期、if/then/else 分支和链式转换。
- 🔒 默认沙箱运行，API 响应和认证值留在本机，不上传数据库。
- 📤 Pro 支持导出 JSON、Markdown 或 Spec Frame，将数据随设计一起交接。
- 🆓 Guest 免费无账号：1 个 Palette、基础文本转换、单帧+集合模式。
- 💰 Free 永久 $0：2 个 Palette、云同步；Pro $12/月：50 个 Palette、全部转换、导出、优先支持。
- 🚀 安装 Paint By JSON，连接首个 API，用真实数据替代 Lorem ipsum，避免反复 mock。

---

### [](https://x.com/benjitaylor/status/2096656821591413161)

**原文标题**: [Benji Taylor on X: "A personal website should feel like you’ve briefly left the rest of the internet" / X](https://x.com/benjitaylor/status/2096656821591413161)

Benji Taylor 在 X 上表示，个人网站应让访问者感觉像是短暂离开了互联网的其他部分；该帖发布于 2026 年 9 月 6 日，并获得约 570 万次浏览和大量互动。

- 💡 核心观点：个人网站应营造一种“暂时离开整个互联网”的独特体验。
- 🌐 这意味着个人网站应区别于社交媒体和主流平台，带来更独立、安静的空间感。
- 🕒 发布时间：2026 年 9 月 6 日下午 5:48。
- 👀 浏览量：约 570 万次。
- 💬 互动数据：827 条回复、598 次转发、1.2 万次点赞、7000 次收藏。

---

### [](https://x.com/LouisLazaris)

**原文标题**: [Louis Lazaris (@LouisLazaris) / X](https://x.com/LouisLazaris)

这是 Louis Lazaris（@LouisLazaris）的社交个人资料摘要，简介自称“Chairman of the Bored”，是两份科技通讯的创始人，常驻加拿大，自2009年5月加入，拥有约5,462名关注者。

- 👤 账号：Louis Lazaris，用户名 @LouisLazaris
- 🏷️ 个人简介：Chairman of the Bored
- 📰 创办两份科技通讯：webtoolsweekly.com 与 techproductivity.co
- 🔗 链接汇总：bio.link/louislazaris
- 🌐 个人网站：impressivewebs.com
- 📍 位置：加拿大多伦多（原文写作 Torontocisco, Canadafornia）
- 📅 加入时间：2009年5月
- 📝 发帖数：5,258
- 👥 社交数据：关注 717 人，关注者 5,462 人
- 🗂️ 内容分类：Posts、Replies、Reposts、Media

---

### [](https://bsky.app/profile/louislazaris.com)

**原文标题**: [@louislazaris.com on Bluesky](https://bsky.app/profile/louislazaris.com)

Louis Lazaris 是前端开发者兼电子报策展人，其 Bluesky 资料页列出了个人介绍、多个项目链接，以及使用 Bluesky 的相关说明。

- 👤 姓名：Louis Lazaris
- 🌐 个人网站：louislazaris.com
- 🆔 Bluesky 标识：did:plc:6if43vohxmohxuooa7bkkw5q
- 🛠️ 职业：前端开发者与 newsletter curator（电子报策展人）
- ⚙️ Webtools Weekly：https://webtoolsweekly.com
- 💼 Tech Productivity：https://techproductivity.co
- 💻 VS Code Email：https://vscode.email
- 👨‍💻 个人主页：https://louislazaris.com
- 🎸 YouTube 频道：@tunejotter，面向吉他爱好者
- ℹ️ Bluesky 提示：需启用 JavaScript 才能使用；详情可访问 bsky.social 和 atproto.com

---

### [向 Web Tools Weekly 提交工具](https://webtoolsweekly.com/submit)

**原文标题**: [Submit a Tool to Web Tools Weekly](https://webtoolsweekly.com/submit)

如果你开发或知道对前端开发者有用的工具，可通过 X 或 Bluesky 私信推荐；可提交库、框架、插件、脚本、应用、API、编辑器等，但不接受文章或教程，生产力工具请投另一份简报 Tech Productivity。

- 📩 可通过 X 私信 @LouisLazaris 提交工具推荐
- 💬 可通过 Bluesky 私信 @LouisLazaris.com 提交工具推荐
- 🧰 可提交库、框架、插件、脚本
- 🌐 可提交 Web 应用、桌面应用、移动应用
- 🔌 可提交 API / 服务、编辑器 / IDE
- 🛠️ 也可提交其他对 Web 开发者、程序员或设计师有用的工具
- 🚫 请勿提交文章或教程，它们不会被收录
- 📰 生产力相关工具已移至另一份简报 Tech Productivity，也可按上述方式提交

---

### [](https://stowaway.live/)

**原文标题**: [Stowaway â Live 3D flight tracking from the window seat](https://stowaway.live/)

Stowaway 是一个把航班追踪变成沉浸式 3D 天空体验的网站：用户可从飞行器视角看到实时天空、飞机、卫星与星空，并“坐进”靠窗座位。它免费、无需安装或账号，数据来自公开 ADS-B 与天文目录；支持者可获得更清晰地面和 AI 助手 Roger 等增强功能，同时强调隐私与无广告。

- ✈️ 不只显示地图上的飞机图标，而是呈现飞机正在穿越的真实天空、地平线、时间和当晚星空。
- 🛰️ 所有内容均为渲染但并非虚构：飞机在真实位置，卫星在真实轨道，星空按用户所在地计算。
- 🧭 称为“超越航班追踪”的 3D 航班追踪，实时位置来自公开信号，用户可选择搭上某架航班。
- 💎 支持者可看到更清晰的真实建筑与街道；这也是免费版能保持无广告的原因。
- 🔒 无账户、不向广告商或数据经纪商出售信息，也不保留用户查看位置的历史。
- 📈 通过口碑传播，每天有大量跟随飞行和全球航班分享；用户称其有旧互联网氛围与新技术。
- 🆓 免费使用，天空、飞机和卫星无需账户；支持者额外功能非必需。
- 📡 航班数据来自 ADS-B 公开无线电信号，由全球志愿者接收分享；不可作为导航工具。
- 🖥️ 无需安装，现代浏览器、桌面、平板或手机均可运行。
- 🌐 天空功能全球适用；飞机覆盖欧洲和北美较密，海洋和偏远地区较稀疏。
- 🛰️ 可查看国际空间站、Starlink、气象卫星和碎片，轨道来自公开天文目录。
- 🤖 支持者可用 AI 助手 Roger 以自然语言找航班和视角，如“把我放在阿尔卑斯山上空”。
- 📍 位置仅用于绘制对应天空，之后不再使用；隐私政策有详细说明。
- 🎫 无需机票、机场或安检，约十秒即可体验飞行魔法。

---

### [](https://webtoolsweekly.com/)

**原文标题**: [Web Tools Weekly | A Weekly Newsletter for Front-end Developers](https://webtoolsweekly.com/)

Web Tools Weekly 是一份面向 Web 开发者的每周邮件通讯，已有 15,555 名订阅者；它承诺每周只发一封邮件、无垃圾邮件，并分享新工具、库和 JavaScript 技巧。订阅涉及 Web Tools Weekly、EmailOctopus、reCAPTCHA/Google 的相关条款与隐私政策；大量读者长期订阅并给予高度评价。

- 📬 面向 Web 开发者的每周通讯，订阅人数达 15,555。
- 🚫 每周仅一封邮件，并承诺无垃圾邮件。
- 🔍 可查看隐私政策，了解数据收集与使用方式。
- ✅ 订阅即表示同意接收 Web Tools Weekly 邮件，并接受相关条款。
- 🔐 数据会按 EmailOctopus 的隐私政策与条款进行存储和追踪。
- 🤖 网站受 reCAPTCHA 保护，并适用 Google 隐私政策与服务条款。
- 💬 多年来收到大量来自邮件和社交媒体的自发好评。
- 🏆 读者称其通过“ awesome 测试”，是最棒的科技通讯之一。
- 🧰 许多读者通过它发现并长期使用新的 Web 工具和库。
- 💡 每期附带的 JS 技巧尤其受欢迎，常带来意想不到的启发。
- 📈 读者表示订阅多年、每周期待阅读，并从中获得很大价值。
- 🙌 读者认为该通讯为前端开发工作带来了巨大帮助。

---

