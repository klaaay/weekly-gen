### [](https://www.latticegrid.dev/?utm_source=NEWSLETTER&utm_medium=newsletter&utm_campaign=top-ad-combo)

**原文标题**: [One Data Grid, Every Live View: Board, Gantt, Charts, KPIs | Lattice Grid JS](https://www.latticegrid.dev/?utm_source=NEWSLETTER&utm_medium=newsletter&utm_campaign=top-ad-combo)

Lattice Grid 是一个零依赖、可编辑的实时数据网格：一个实时数据流可同时驱动网格、看板、甘特图、图表和 KPI 面板，并内置受治理编辑、AI 辅助与按域名授权模式。

- 🔄 一个实时数据源可驱动多种联动视图，任一处编辑，其他视图同步更新。
- ⚙️ 零依赖、受治理编辑、内置可信 AI；一个 Data Router 按记录类型分区，各面板只接收自己的数据切片。
- 🧩 支持 JavaScript、React、Vue、Svelte、Angular、htmx、Web Component、Python，可直接复制示例或跟 Python 教程。
- 🚀 快速开始：CDN 引入一个 CSS 和一个 JS，指向有高度的 div 并声明列即可；npm 包为 `@toclocoinc/lattice-grid`，无构建步骤和配置文件。
- 📊 默认包含排序、列筛选、拖拽调整/重排/隐藏、键盘导航；localhost 开发无需许可证。
- ✏️ 可编辑而非只读：内联编辑、拖拽填充、Excel 复制粘贴、批量编辑、提交前校验、统一撤销/重做、整行编辑和 22 种编辑器。
- 🛡️ 编辑受控：每个变更可经过自定义关口，可否决编辑或删除，可把写入限制在检查之后，并一键撤销。
- 🤖 AI 内置：可用自然语言重塑视图或生成基于网格数据的摘要；使用你自己的模型和密钥，网格本身不发起 AI 调用。
- 🗂️ 大数据支持：可覆盖 DuckDB、Parquet 或数据仓库，过滤、排序、分页下推为查询，仅返回屏幕上的行。
- 📈 统计能力：中位数、百分位、分布和预测基于当前查看的行重算，筛选后所有数字跟随更新。
- 🧪 工程数据类型：每列可声明 number、duration、bytes、ipv4、date、boolean、json 等类型，按解析后的值排序、筛选、汇总和导出。
- 👥 面向操作团队：支持演示模式、保存视图、单元格评论/线程、四种主题、Excel 导出和全程键盘操作。
- 🔍 诊断清晰：错误设置会命名配置、说明预期、显示实际值，并保留安全默认值继续渲染。
- 📊 图表与洞察：35 种图表直接来自网格行，筛选联动；阴影列可追踪增量、移动次数、排名和上升名次。
- 💰 授权按域名而非开发者：开发免费但带水印；部署 $1,000/域名，含一年支持；通配符 $10,000 覆盖一个域名的所有子域。
- ✅ 只有一个完整版本，无功能保留；评估版与部署版功能一致，许可证只决定可运行位置。
- 🌐 域名定义：网格所服务的 hostname；`example.com` 与 `www.example.com` 算两个，端口和路径不影响，localhost、CI、预发和预览分支免费带水印。

---

### [](https://github.com/daviddarnes/mastodon-post)

**原文标题**: [GitHub - daviddarnes/mastodon-post: A Web Component to display Mastodon posts and their metadata · GitHub](https://github.com/daviddarnes/mastodon-post)

这是一个由 daviddarnes 开发的 Web Component，用于将普通 Mastodon 帖子链接渲染为引用式帖子，并展示帖子元数据。它支持默认模板、自定义模板和数据绑定，可通过 `data-key` 读取 Mastodon 公共状态 API 字段，甚至支持嵌套数据。项目公开、采用 MIT 许可证，适合在网页中嵌入 Mastodon 内容。
- 📦 仓库信息：`daviddarnes/mastodon-post`，公开项目，main 分支，29 次提交，39 Stars，2 Forks，0 Issues，0 Pull Requests。
- 🧩 核心功能：把普通 Mastodon 帖子链接转换成带样式的引用式 Mastodon 帖子。
- 📊 元数据展示：可显示回复数、转发数、收藏数等帖子互动数据。
- 🎨 模板定制：支持全局模板 `<template id="mastodon-post-template">`，也可用 `template` 属性为单个实例指定自定义模板。
- 🔑 数据绑定：通过 `data-key` 属性绑定 Mastodon 公共状态 API 响应中的字段。
- 🌳 嵌套数据：支持 JavaScript 点号和索引语法，如 `account.display_name`、`media_attachments[0].preview_url`。
- 🔗 特殊处理：`<a>` 和 `<img>` 的 `data-key` 返回值若以 `http` 开头，会分别写入 `href` 和 `src` 属性。
- ⚙️ 安装方式：支持 `npm install @daviddarnes/mastodon-post`、从 GitHub 下载，或通过第三方 CDN 引入，但 CDN 不推荐用于生产。
- 📄 主要文件：包含 `mastodon-post.js`、`demo.html`、`demo-custom-template.html`、`package.json`、`README.md`、`LICENSE` 等。
- 🙏 致谢：项目受 Zach Leatherman 的 Web Component 仓库模板启发。

---

### [GitHub - codepen/slideVars：用于更新 CSS 自定义属性的 UI · GitHub](https://github.com/codepen/slideVars)

**原文标题**: [GitHub - codepen/slideVars: UI for Updating CSS Custom Properties · GitHub](https://github.com/codepen/slideVars)

@codepen/slidevars 是一个 TypeScript 库，用于为 CSS 自定义属性创建交互式 UI 控件，通过 Shadow DOM Web 组件提供滑块和颜色选择器，支持自动检测、手动配置与混合模式，并内置 Lit 响应式模板。

- 🎛️ 自动在页面右上角注入 `<slide-vars>` 切换按钮（🎛️），点击可打开/关闭控制面板。
- 🔍 自动检测 `:root` 中的 CSS 变量，识别数值单位生成滑块，识别颜色生成颜色选择器。
- ⚙️ 支持手动配置变量，可指定类型（slider/color）、范围、默认值、单位、作用域，并能按标签分组。
- 🧩 混合模式下手动配置优先于自动检测，灵活覆盖默认行为。
- 🎨 颜色检测支持 Hex、rgb、hsl、命名颜色及现代色彩空间（oklch、oklab、lch、lab、hwb、color()），现代色彩空间使用高级 `<color-input>` 组件。
- 📦 安装简单：`npm install @codepen/slidevars`，调用 `slideVars.init()` 即可。
- 🛠️ 提供 API：`init`、`destroy`、`open`、`close`、`toggle`、`getElement`，完整 TypeScript 类型定义。
- 📐 自动滑块默认范围基于 MDN 单位类型，若当前值超出范围会自动扩展。
- 🚀 开发命令：`npm run example` 本地演示，`npm run build` 构建库，`npm run build:demo` 构建文档站并自动部署到 GitHub Pages。
- 🖼️ 包含自定义 `<slidevars-logo>` 组件，面板开合时三个滑块动画变化。
- 📄 MIT 许可证，由 CodePen 维护，GitHub 上获得 84 星、3 次 fork。

---

### [GitHub - argyleink/prop-for-that：JS 知道的，现在 CSS 也知道了 · GitHub](https://github.com/argyleink/prop-for-that)

**原文标题**: [GitHub - argyleink/prop-for-that: what JS knows, now CSS knows · GitHub](https://github.com/argyleink/prop-for-that)

prop-for-that 是一个将 JavaScript 可读取、但 CSS 无法直接感知的运行时状态，写入 `--live-*` 与 `--const-*` CSS 自定义属性的库，让 CSS 通过 `calc()` 和 `var()` 直接组合、响应这些状态。它零依赖、TypeScript 编写、支持 ESM + CJS，并且 SSR 安全。

- 🎯 核心目标：把滑块值、指针位置、元素可见性、视口尺寸、电池、网络、传感器等状态暴露给 CSS。
- 📦 安装使用：`npm i prop-for-that`；最简单方式是 `<script type="module">import 'prop-for-that/auto'</script>`。
- 🏷️ 声明式绑定：元素添加 `data-props-for="key …"`，CSS 中读取对应 `--live-*` 属性。
- 🎨 示例：`<input type="range">` 可通过 `--live-value-pct` 自绘，无需事件监听或手动渲染循环。
- 🔗 提升与样式查询：自定义属性只向下继承，`@container style()` 匹配祖先；可用 `data-props-to="<selector>"` 或 `{ to }` 把值写到最近匹配祖先，供自身或兄弟元素响应。
- ⚡ 性能设计：每帧一次 `requestAnimationFrame` 刷新，无变化时空闲，标签页隐藏时冻结；写入变更 diff，并全页共享 `ResizeObserver` / `IntersectionObserver`。
- 🧠 采样策略：持续采样元素源在离屏时暂停；事件驱动源（表单、range、select 等）不受限制。
- 🧩 按需加载：内置 4 个核心源：viewport、元素尺寸、可见性、`<input type="range">` 值；其他均为可选、可 tree-shake 插件，`auto` 下按 `data-props-for` 需求懒加载。
- 📡 插件能力：20+ 插件，包括指针、电池、网络/在线、页面焦点/可见性、导航类型、meta 标签、低熵 UA、FPS、时钟、滚动速度、设备方向/运动、定位、CPU 压力、软键盘几何、媒体播放、表单/字段状态、select/color-picker、文本截断、图像/视频主色与强调色、可种子随机数等。
- 🧱 平台整合：可选启用 typed `@property` 以支持插值，或使用 FOUC 安全常量在首绘前写入；体积小、无依赖、支持多种 bundle 格式。
- 🚪 入口点：`prop-for-that/auto` 零配置声明式；`prop-for-that` 提供命令式 API `propsFor()`、`register()`、`configure()`；`prop-for-that/head` 提供同步 FOUC 安全常量；`prop-for-that/plugins` 是插件目录。
- ⚠️ 注意事项：`auto` 只观察 light DOM，不处理 shadow roots，需用 `propsFor(el, …)`；`auto` 懒加载插件 chunk，CDN 应使用原样提供 `dist` 的 unpkg / jsDelivr。
- 📚 文档与 AI 参考：文档在 `prop-for-that.netlify.app/docsite`；`llms.txt` 提供单文件参考，并随 npm 包发布。
- 📈 仓库信息：MIT © Adam Argyle；约 904 stars、19 forks、6 watchers、3 issues、1 PR、41 commits。

---

### [](https://www.fontself.app/)

**原文标题**: [FontSelf](https://www.fontself.app/)

该页面是 FontSelf 的字体自托管提示与操作界面，核心提醒是：从 Google 服务器加载字体可能违反 GDPR；建议在几分钟内改为自托管，以兼顾加载速度与用户隐私。页面还提供字体预览、字重配置、下载子集等操作入口，以及版权和政策链接。

- ⚠️ 合规警告：网站若从 Google 服务器加载字体，可能违反 GDPR。
- 🔒 隐私建议：自托管字体有助于保护用户数据隐私。
- ⚡ 性能目标：自托管后仍可保持网站加载快速。
- 🖥️ 工具名称：FontSelf，提供渲染预览与字体加载界面。
- 1️⃣ 配置字重：选择字体以配置不同变体。
- 2️⃣ 下载选项：选择字体以查看其子集。
- ©️ 版权信息：© 2026 FontSelf。
- 📄 政策链接：包含隐私政策与条款。

---

### [CSS Type Studio：使用 CSS 进行高级排版](https://www.csstypestudio.com/)

**原文标题**: [CSS Type Studio: Advanced Typography with CSS](https://www.csstypestudio.com/)

该页面是 CSS Type Studio 的交互式排版工具，围绕“Advanced Typography with CSS”提供示例文本、颜色模式、全局与元素级 CSS 排版控制，并支持布局保存、分享及账户订阅管理。

- 📝 提供多种示例文本：Basic、Kitchen Sink、Winnie the Pooh、Moby Dick、UN Charter、Python Code、Pumpkin Pie Recipe。
- 🌗 支持 Light、Dim、Dark、Cool、Warm 五种颜色模式。
- ⚙️ 全局属性：可设置字体大小单位（rem/px）和最大宽度。
- 🏷️ 元素属性：可针对 H1-H4、P、ol > li、ul > li、div.byline、div.dateline 等元素调整样式。
- 🔤 字体控制：字体系列、字号、字体样式、字重 100-950，以及字体变体配置。
- 🔠 字体变体：涵盖大写、连字、数字形式等高级排版选项。
- 📐 文本排版：对齐、缩进、字母间距、行高、词间距和文本换行。
- 📦 text-wrap：支持 wrap、nowrap、balance、pretty、stable，用于平衡标题换行或关闭换行。
- 🔍 font-kerning：可选 auto、normal、none，控制字体字距信息的使用。
- 🖥️ 文本渲染与光学尺寸：包括 text-rendering、font-optical-sizing 等设置。
- 🧬 合成控制：字重、样式、小型大写字母合成，可选 auto 或 none。
- 📏 间距与边距：可设置上/下边距和左内边距。
- 📋 列表样式：支持 none、disc、circle、square、decimal、罗马数字、拉丁/字母编号等。
- 💾 布局管理：可保存、加载、删除布局，并生成分享链接。
- 👤 账户功能：免费用户可管理账单，使用 Stripe 支付，升级 Pro，登出或删除账户。
- 🔐 登录后可保存/分享排版布局并获取 CSS 代码；也可免费创建账户。
- 🔗 页脚包含排版指南、字体库、联系我们、隐私政策、服务条款和版权信息。

---

### [](https://charcuterie.elastiq.ch/)

**原文标题**: [Charcuterie — A Visual Unicode Explorer](https://charcuterie.elastiq.ch/)

这段内容主要提及 SigLIP 2 模型，并标注了图形/绘画、声音、动画以及所有角色/字符等相关信息。
- ✎ 模型：SigLIP 2
- 🎨 涉及图形、绘画或视觉相关标识
- 🔊 涉及声音或音频相关标识
- ✓ 动画功能已启用或勾选
- 👥 面向所有角色或字符
- ❌ “×”可能表示排除、不支持或某种组合关系，需结合上下文理解

---

### [](https://github.com/NickHodges/tshtmlwriter)

**原文标题**: [GitHub - NickHodges/tshtmlwriter: TypeScript HTML Writer · GitHub](https://github.com/NickHodges/tshtmlwriter)

tshtmlwriter 是 NickHodges 发布的公开 TypeScript 库，用链式、类型安全的方式构建 HTML，避免字符串拼接、模板字面量和 JSX；它是 DelphiHTMLWriter 的 TypeScript 移植版，采用 MIT 许可证，零依赖，并通过大量测试保证 HTML 结构。

- 📦 仓库：NickHodges/tshtmlwriter，公开，MIT 许可，2 次提交，0 Star、1 Fork、0 Issue/PR。
- ✨ 目标：面向 TypeScript 的流畅、类型安全 HTML 构建器，通过链式调用生成格式良好的 HTML。
- 🔁 来源：移植自 DelphiHTMLWriter，保留流畅构建器设计并利用 TypeScript 类型系统。
- 🧩 特性：流畅 API、严格 TypeScript 字面量联合类型、编译期上下文错误检查、完整 HTML5 支持、零依赖、347 个测试/21 个测试文件。
- 📥 安装：npm install tshtmlwriter 或 bun add tshtmlwriter。
- 🏭 工厂函数：createDocument(docType?)、create(tagName)、createFragment()。
- 🏗️ 内容与结构：addText、addRawText、addTag、closeTag、toHTML 等。
- 🏷️ 属性支持：addId、addClass、addStyle、data/aria/role，以及 required、disabled、autofocus、hidden、readonly、multiple、novalidate 等布尔属性。
- 🅰️ 文本格式：bold、italic、underline、emphasis、strong、code、mark、ruby 等多种格式方法。
- 🔢 标题与列表：addHeadingText(1-6)；支持无序、有序和定义列表。
- 📊 表格与表单：表格（caption/tr/th/td）及表单（form/fieldset/legend/label/input/button）构建方法。
- 🌐 语义与媒体：header、nav、main、article、aside、footer、section、figure、details、dialog、video、audio、img、iframe、embed 等。
- 🧰 便捷方法：addFigure、addDetailsSummary、addAnchor、addComment。
- ⚠️ 错误处理：运行时检测无效结构，如 NotInListError、ClosingClosedTagError、DocumentHasOpenTagsError，可用 setErrorLevels() 配置。
- 🧬 类型导出：IHTMLWriter、HeadingLevel、FormatType、InputType、DocType、BulletShape、NumberType、TableOptions、FormOptions。
- 📄 许可证：MIT。

---

### [](https://github.com/tinylibs/picospinner)

**原文标题**: [GitHub - tinylibs/picospinner: A lightweight, no dependency, pluggable CLI spinner library. · GitHub](https://github.com/tinylibs/picospinner)

picospinner 是 tinylibs 组织下的一个轻量级、零依赖、可插拔的 CLI spinner（命令行加载指示器）库，提供简单 API、ESM 支持、自定义符号/帧/颜色/速度等能力，仓库采用 MIT 许可证，约有 93 stars、3 forks。

- 📦 轻量零依赖：picospinner 是一个无依赖、可插拔的命令行 spinner 库。
- 🛠️ 安装方式：使用 `npm i picospinner`；v3 仅发布为 ES module，CommonJS 可安装 `picospinner@2`。
- 🚀 基本用法：`new Spinner('Loading...')` 后调用 `start()`，可用 `succeed`、`fail`、`warn`、`info` 或 `stop` 结束。
- 🎨 自定义符号：可通过 `symbols` 选项覆盖符号，例如设置 `warn: '⚠'`。
- 🔄 自定义帧：可通过 `frames` 选项设置旋转动画帧，例如 `['-', '\\', '|', '/']`。
- 🧹 停止与移除：调用 `spinner.stop()` 会停止 spinner 并将其从输出中移除。
- 🖥️ 输出流：默认写入 `process.stdout`，也可传入 `stream: process.stderr` 避免干扰机器可读输出。
- 🌈 颜色支持：v3.0.0 起默认启用颜色，基于 `node:util` 的 `styleText`；可用 `colors: false` 关闭或传入对象自定义。
- 🧩 第三方格式化：可使用 picocolors、chalk 等格式化文本，也支持 `symbolFormatter` 自定义符号样式。
- ⏱️ 旋转速度：可向 `spinner.start(10)` 传入毫秒值，自定义 tick 速度。
- 📊 仓库概况：MIT 许可证，约 93 stars、3 forks、2 watchers、30 commits，当前 0 issues 和 0 pull requests。

---

### [](https://github.com/HexmosTech/git-lrc)

**原文标题**: [GitHub - HexmosTech/git-lrc: Free, Micro AI Code Reviews That Run on Git Commit · GitHub](https://github.com/HexmosTech/git-lrc)

git-lrc 是 HexmosTech 推出的免费、轻量 AI 代码审查工具，挂接到 git commit，在提交前自动审查暂存 diff，为 AI 生成代码加上“刹车”，在停机、泄露和技术债进入生产前拦截风险。它结合 10 类风险、100+ 失败模式、内联评论、风险评分、摘要卡、Git 日志追踪、BYOK 与 Agent 模式，把代码审查变成每个团队都有的提交习惯，并提供免费个人层和团队版 LiveReview。

- 🚦 定位：AI 编码像没有刹车的赛车，git-lrc 在每次 git commit 时审查每个 diff，防止 AI 静默破坏逻辑、放宽约束、泄露凭证或引入昂贵云调用。
- ⚡ 快速安装：Linux/macOS 用 `curl ... | bash && ipm i HexmosTech/git-lrc`，Windows 用 PowerShell 安装；安装后全局设置 hook。
- 🧭 Issue Navigator：把审查结果按严重程度、类别、子类别、类型和区域结构化过滤，支持复制问题或发送到 Claude，并通过点赞/点踩优化后续审查。
- 🧾 Summary Deck：每次审查生成 60 秒摘要卡，用通俗语言说明改了什么、为什么、风险和技术亮点，适合新人入职、事故复盘和长期记忆。
- 🖥️ 审查 UI：提供 GitHub 风格 diff、行内 AI 评论、严重级别徽章、审查摘要、暂存文件列表、问题复制、逐条导航和事件日志。
- ✅ 提交决策：审查后可选择 Commit、Commit & Push 或 Skip；Skip 会中止提交，先修复问题。
- 🔁 审查循环：生成代码 → `git lrc review` → 复制问题给 AI 修复 → 再审查，直到满意；工具记录迭代次数和 AI 审查覆盖率。
- 🙋 Vouch / ⏭️ Skip：`--vouch` 表示人工担责并跳过 AI；`--skip` 表示不审查、不担责；git log 会记录 `ran`、`vouched` 或 `skipped`。
- 🤖 Agent 模式：`git lrc review --agent-mode` 非交互运行 AI 审查并输出 JSON，适合 Claude Code、Cursor、CI；完成后记录 `agent-reviewed`，失败时安全回退。
- 📊 风险评分视图：按“爆炸半径”和“客户影响潜力”对每个 hunk 排序，高风险改动优先；本地知识图谱引擎自动安装到 `~/.lrc/bin`。
- 🧠 评分机制：Blast Radius 与 Review Priority 两个 0-100 分独立计算后按 60/40 合并，考虑调用链、HTTP 路由、重复实现、测试缺失、架构层和历史耦合等信号。
- 📝 Git Log Tracking：提交信息追加 LiveReview 状态行，如 `ran (iter:3, coverage:85%)`，团队能直接看到哪些提交被审查、担责或跳过。
- 🔌 BYOK：默认使用 Gemini，也支持 OpenAI、Claude、DeepSeek、OpenRouter、Atlas Cloud 和 Anthropic 兼容 API；用 `lrc ui` 管理连接器与优先级。
- 📚 仓库规则：`.lrc/rules/*.md` 和 `ignore` 让审查器理解团队偏好、禁用依赖和忽略文件；规则上限 3000 字符，可离线校验和预览发送给模型的内容。
- 🛡️ 安全检查：每次审查覆盖 10 个风险类别、100+ 失败模式，分为停机、泄露、技术债三大支柱，涵盖可靠性、正确性、性能、可扩展性、安全、合规、可维护性、架构、开发者体验和成本。
- 💰 定价：免费个人层每月 30k LOC；Premium 从 $32 起 100k LOC；Enterprise 支持自托管、SSO、自定义域和更强数据控制。
- 📦 许可证：采用修改版 Sustainable Use License，源码可用，允许内部业务使用和修改，禁止转售或商业再分发。
- 👥 团队版：LiveReview 提供团队级 AI 代码审查，包含仪表盘、组织策略和审查分析。
- ⭐ 免费推广：无信用卡、无试用陷阱；鼓励分享给开发者朋友并 Star 仓库，让更多 AI 生成代码先审查再进入生产。

---

### [wterm | 面向 Web 的终端模拟器](https://wterm.dev/)

**原文标题**: [wterm | Terminal Emulator for the Web](https://wterm.dev/)

wterm（读作“dub-term”）是一个面向 Web 的终端模拟器，核心用 Zig 编写并编译为 WASM，通过渲染到 DOM 获得原生文本选择、复制/粘贴、查找和无障碍支持，同时实现接近原生的性能。

- 🖥️ 直接渲染到 DOM：自带原生文本选择、剪贴板、浏览器查找与屏幕阅读器支持。
- ⚙️ Zig + WASM 核心：解析 VT100/VT220/xterm 转义序列，`.wasm` 二进制约 12 KB。
- 🔗 原生超链接：OSC 8 链接在视口与回滚历史中精确附着到单元格，并限制为安全 HTTP(S) 锚点。
- 🧹 脏行跟踪：通过 `requestAnimationFrame` 仅重新渲染被触碰的行。
- 🖌️ 同步输出：模式 2026 可原子化阻塞绘制，并带有有界恢复截止时间。
- 🎨 主题：基于 CSS 自定义属性，内置 Default、Solarized Dark、Monokai、Light。
- 📜 终端兼容性：支持备用屏幕缓冲，`vim`、`less`、`htop` 可正常工作；提供可配置环形缓冲的回滚历史。
- 🌍 Unicode 与颜色：CJK、全角、emoji 宽单元格保持对齐，支持 24 位 RGB SGR 颜色。
- 🧩 框架与自适应：提供 React、Vue 3、Svelte 组件，基于 `ResizeObserver` 自动调整大小。
- 🔌 连接方式：通过 WebSocket 连接 PTY 后端并支持重连；示例使用 just-bash，也可参考 SSH、local。
- 🚀 下一步：可从 Get Started 开始使用。

---

### [错误](https://sendercircle.com/r.php?id=3641)

**原文标题**: [Error](https://sendercircle.com/r.php?id=3641)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='sendercircle.com', port=443): Max retries exceeded with url: /r.php?id=3641 (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [](https://github.com/below43/git-uncommit)

**原文标题**: [GitHub - below43/git-uncommit · GitHub](https://github.com/below43/git-uncommit)

git-uncommit 是一个用于撤销最近一次或多次 git 提交的开源命令行工具，同时会保留更改在暂存区。它等价于 `git reset --soft HEAD~N`，并支持通过 Homebrew 安装，适合记不住原生命令的用户。

- 🧰 `git-uncommit` 可撤销最近一次提交，并保持更改已暂存。
- ⚙️ 用法简单：`git uncommit` 撤销最后一次；`git uncommit 3` 撤销最近 3 次。
- 🔄 功能等价于 `git reset --soft HEAD~N`，作者因记不住该命令而创建。
- 🍺 可通过 Homebrew 安装：`brew tap below43/git-tools`，再执行 `brew install git-uncommit`。
- 📁 仓库包含 `release`、`.gitignore`、`LICENSE`、`README.md` 和 `git-uncommit` 等文件。
- 📜 项目采用 MIT 许可证，README 中说明了用途、安装方式和使用示例。
- ⭐ 当前仓库有 4 个 star、0 个 fork、0 个 issue、0 个 pull request。

---

### [](https://ante.run/)

**原文标题**: [Ante — A ghost in your shell](https://ante.run/)

未提供需要总结的文本，因此暂时无法生成文章摘要；请在下一条消息中粘贴内容，我会按要求输出中文要点总结。

- 📄 当前消息中的“以下内容”为空，暂无可总结信息。
- ✍️ 请补充文章或文本，我会提取关键点并生成简洁摘要。
- ✅ 输出将采用“概述摘要 + - 表情符号要点”的中文格式。
- 🔍 每条要点会尽量保留核心信息，省略次要细节。

---

### [hunk — 审查优先的终端差异查看器](https://www.hunk.dev/)

**原文标题**: [hunk — review-first terminal diff viewer](https://www.hunk.dev/)

Hunk 是一款面向人类和 AI 代理的“审查优先”终端 diff 查看器，主打快速、美观、跨平台，适合代码审查与代理协作；v0.22.0 带来历史浏览、范围审查和精确评论。

- ⚡ 定位：Hunk 是 review-first 的 diff 查看器，与代理配合良好，快速、好看且处处可用。
- 📦 安装：支持 curl 一键脚本、Homebrew、npm（`hunkdiff`）、mise 和 Nix。
- 🧭 v0.22.0：新增历史浏览、范围审查、精确评论；支持 split view。
- 📄 单流浏览：按侧栏顺序从上到下阅读整个变更集，无需切换单文件视图；可查看文件计数，用 `[` 和 `]` 跳转 hunk。
- 🤖 代理注释：代理在 sidecar 留下摘要、理由和作者，Hunk 将注释渲染在对应 hunk 上方，跳转 hunk 时注释跟随。
- ⌨️ 交互：支持键盘快速操作和鼠标浏览；点击侧栏跳转、滚轮滚动、悬停评论，也可作为 pager 接收 patch。
- 🖥️ 布局：自动选择并排或统一视图，也可用 `1`、`2`、`0` 切换；支持换行和行号实时开关。
- 🎨 主题与高亮：真实语法高亮，内置 Catppuccin、Dracula、Gruvbox、GitHub 等经典主题，并有 59+ 社区主题，支持自定义。
- 🧩 扩展性：可用 TypeScript 编写扩展，添加主题、命令、文件预览、停靠面板或版本控制后端，并可从任意 git 仓库安装。
- 🛠️ 其他能力：watch 模式、live sessions、Jujutsu & Sapling 支持、pager & difftool、macOS/Linux/Windows、自定义主题。
- ⭐ 口碑：Mitchell Hashimoto 称其已替代其他本地 diff 查看器，DHH 也表达喜爱；另有视频演示可供观看。
- 🚀 行动：可在下一个 changeset 中安装并试用 Hunk。

---

### [](https://github.com/coder/ghostty-web)

**原文标题**: [GitHub - coder/ghostty-web: Ghostty for the web with xterm.js API compatibility · GitHub](https://github.com/coder/ghostty-web)

ghostty-web 是 Coder 推出的开源项目，旨在把 Ghostty 的终端模拟能力带到浏览器，并提供与 xterm.js 兼容的 API。它使用 Ghostty 的 WASM 解析器，让 Web 终端获得更正确的 VT100 与 Unicode 处理能力。

- 🖥️ 核心定位：为 Web 提供 Ghostty 终端模拟，兼容 xterm.js API，迁移时只需把 `@xterm/xterm` 改为 `ghostty-web`
- ⚙️ 技术实现：使用从 Ghostty 编译而来的 WASM 解析器，与原生应用共享同一套代码，零运行时依赖，WASM 包约 400KB
- 🌐 项目起源：最初为 Mux（隔离式并行智能体开发桌面应用）创建，但设计上可用于任何场景
- 🚀 体验方式：可访问 Live Demo，或运行 `npx @ghostty-web/demo@next`，在 `http://127.0.0.1:8080` 启动带真实 shell 的环回 HTTP 服务器，`/ws` 有同源 token 保护
- 🔍 对比 xterm.js：改善复杂文字（如天城文、阿拉伯文）渲染问题，并完整支持 `XTPUSHSGR/XTPOPSGR`；xterm.js 用 JavaScript 手写终端仿真，Ghostty 使用久经考验的模拟器代码
- 📦 安装使用：`npm install ghostty-web`；需先 `await init()`，再创建 `Terminal`、调用 `open`，并处理 `onData` 与 `write`
- 🛠️ 开发与未来：从 Ghostty 源码构建，依赖 Zig 和 Bun，目前只需少量补丁；未来将消费原生 Ghostty WASM 发行版，并继续提供 xterm.js 兼容 API
- 📄 许可与社区：MIT 许可证；GitHub 约 2.8k stars、172 forks、119 commits、26 issues、33 PR

---

### [Meco：排名第一的简报阅读器 | 整理你的收件箱](https://meco.app?utm_campaign=3nux)

**原文标题**: [Meco: The #1 newsletter reader | Declutter your inbox](https://meco.app?utm_campaign=3nux)

Meco 是一个专为阅读、发现和整理新闻邮件而生的 newsletter 聚合器，旨在把订阅内容移出混乱的收件箱，并提供 AI 摘要、音频简报、智能筛选、标注与跨平台阅读等功能。

- 📥 将新闻邮件从收件箱迁移到专为阅读打造的空间，减少干扰与订阅混乱。
- 🔗 支持连接现有 Gmail 或 Outlook 快速导入 newsletter，也可使用专属 Meco 邮箱订阅新内容。
- 🧹 已导入的 newsletter 可自动跳过收件箱，并能随时恢复回原邮箱。
- 🎯 提供智能筛选与分组，帮助优先查看最相关、最感兴趣的内容。
- 🤖 基于 AI 生成每日 5–10 分钟个性化音频简报，并支持即时文本摘要与每周精选。
- 🔍 根据阅读兴趣和趋势推荐个性化 newsletter，让用户更放心地订阅。
- 📝 支持书签、标注、分类、标签、笔记与高亮，帮助留存和整理知识。
- 📴 支持离线阅读，可在 iOS、Android 和网页端使用。
- ✂️ 提供一键退订，方便清理不再需要的订阅。
- 🔐 不出售数据、不投放广告；邮件数据本地存储于个人设备，靠付费订阅盈利。
- ⚙️ 若不适合，可断开 Gmail/Outlook 并将 newsletter 恢复到收件箱；FAQ 提供更多支持。

---

### [GitHub - frappe/builder：使用直观的可视化构建器轻松打造](https://github.com/frappe/builder)

**原文标题**: [GitHub - frappe/builder: Craft beautiful websites effortlessly with an intuitive visual builder and publish them instantly · GitHub](https://github.com/frappe/builder)

Frappe Builder 是一个面向 Frappe 生态的低代码可视化网站构建器，主打直观设计、响应式、高性能与一键发布，适合设计师和开发者快速创建并上线网站。仓库 frappe/builder 为公开项目，采用 MIT 许可证，拥有约 2.4k stars、538 forks、40 个 issues、11 个 PR 和 4,454 次提交。

- 📦 仓库概况：frappe/builder 公开可用，MIT 许可，社区关注度高，持续活跃开发。
- 🧱 可视化建站：提供类似 Figma 的直观编辑器，简化网页设计流程。
- 🤖 AI 建站：可与代理 Bob 对话来构建和编辑页面，它会基于现有站点内容、设计语言、组件和主题 token 工作，并支持权限控制、审批与回滚。
- 📱 响应式视图：确保网站在不同设备上都能良好显示。
- 🌙 暗色模式：内置暗色模式，支持系统偏好自动检测和手动切换。
- 🗂️ 内置 CMS：借助 Frappe Framework 的 CMS 管理结构化内容，获取动态数据并驱动数据型页面。
- ⚙️ 高级脚本能力：支持全局脚本、客户端脚本、按区块数据脚本和类型化区块属性，并可绑定动态值。
- 🚀 一键发布：单击即可将网站发布到线上。
- ⚡ 性能优秀：避免加载冗余脚本，在 Google Lighthouse 测试中持续获得高分。
- 📊 页面分析：内置分析仪表盘，提供页面浏览量、独立访客和主要来源等洞察。
- 🏭 生产可用：Frappe.io 基于 Frappe Builder 构建，验证其生产环境可靠性。
- 🧰 技术栈：基于 Frappe Framework 全栈框架和 Frappe UI（Vue UI 库）。
- ☁️ 生产部署：支持 Frappe Cloud 托管，也可通过 easy-install 脚本自托管，约 5 分钟完成配置。
- 🐳 开发方式：支持 Docker 和 Bench 本地设置，前端开发可使用 Vite 开发服务器。
- 🔗 相关资源：提供官网、文档、Telegram 群、论坛、Figma 插件（Beta）、Frappe Script Editor 和翻译等链接。

---

### [](https://github.com/ruvnet/drupaljs)

**原文标题**: [GitHub - ruvnet/drupaljs · GitHub](https://github.com/ruvnet/drupaljs)

Drupal.js 是 ruvnet 的公开项目，一个基于 Node.js、Vite.js、Tailwind CSS 和 Supabase 的 Drupal CMS 克隆；它提供完整代码、配置、示例插件、环境变量、Dockerfile、API 与目录结构，并强调与 Drupal 的分类/数据结构兼容以及现代全栈开发优势。仓库当前约 40 星、5 叉、179 次提交，含 2 个 issue 和 1 个 PR。

- 📦 项目定位：Drupal.js 用 Node.js + Vite.js + Tailwind CSS + Supabase 构建 Drupal 风格 CMS，附带可直接运行的脚本与配置。
- 🧬 兼容 Drupal：使用实体类型、字段、分类法、实体关系和权限矩阵，贴近 Drupal 的内容建模方式。
- ⚡ Node.js 优势：比 PHP 更高性能、可扩展、前后端同用 JavaScript、NPM 生态丰富、支持现代实践与活跃社区。
- 🗄️ Supabase 作用：托管 PostgreSQL、内置认证授权、实时能力、自动生成 REST API，并支持扩展。
- 🏗️ 项目结构：backend 用 Strapi + Supabase，frontend 用 React/Vite/Tailwind，含 Docker、docs、docker-compose 与环境变量。
- 🚀 安装启动：准备 Node.js、Docker、Git、Supabase 账号；配置 .env；运行 docker-compose up --build；后台 localhost:1337/admin，前端 localhost:3000。
- 🔐 Supabase 配置：创建项目，获取 API URL、anon key 与数据库凭据，Strapi 启动后自动建表。
- 🌐 API：提供 REST（/api）与 GraphQL（/graphql），支持注册/登录，并对文章、分类、页面等做 CRUD。
- 📈 扩展性：后端可用 Docker/负载均衡/水平扩展；前端可静态托管+CDN；数据库可升级 Supabase 计划、读副本与缓存。
- 🧰 功能规格：文章、页面、分类、菜单等内容类型；Admin/Editor/Author/Public 角色；认证、CRUD、媒体、分类、国际化、插件。
- 🛠️ 技术栈：后端 JavaScript/Node.js/Strapi/PostgreSQL/JWT/Docker；前端 React/Vite/Tailwind/React Router/Axios。
- 🎨 UI：导航栏、页脚、首页、文章列表/详情、登录注册、后台仪表盘、内容管理表单、WYSIWYG 与媒体上传。
- 🔒 安全与测试：保护环境变量、生产用 HTTPS、更新依赖；用 Jest 单元/集成测试，Cypress/Selenium E2E。
- 🚢 部署与许可：建议 CI/CD 自动化部署至 AWS/DigitalOcean/Heroku 等；项目采用 MIT 许可证。

---

### [获取失败](https://recs.page/web-tools-weekly?ref_code=a082baf699&lc=link_campaign_0286c16e2f8b&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recs.page/web-tools-weekly?ref_code=a082baf699&lc=link_campaign_0286c16e2f8b&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [](https://github.com/mearashadowfax/ScrewFast)

**原文标题**: [GitHub - mearashadowfax/ScrewFast: Open-source Astro website template with sleek, customizable TailwindCSS components · GitHub](https://github.com/mearashadowfax/ScrewFast)

ScrewFast 是一个基于 Astro、Tailwind CSS 和 Preline UI 的开源网站模板，将落地页、博客、产品目录和 Starlight 文档站整合在同一仓库中，内置 SEO、国际化、安全头与 CI，适合通过修改内容和 props 快速上线完整网站。

- 🧩 一个仓库包含四种站点类型：落地页、博客、产品目录和 Starlight 文档，共享布局、导航栏与页脚。
- 🧱 提供 79 个现成组件：19 个页面区块（Hero、功能、定价、评价、FAQ、巨型菜单等）和 57 个 UI 元素。
- 🌍 开箱即用多语言：营销页支持英语和法语；文档支持 7 种语言（en、de、es、fa、fr、ja、zh-CN），并支持 RTL。
- 🔍 内置 SEO：集中配置标题、描述、Open Graph、JSON-LD 结构化数据，自动生成 sitemap 和 robots.txt。
- 🔒 生产环境加固：通过 vercel.json 设置 CSP 等安全头，构建后 HTML 压缩，CI 在每次推送时执行类型检查、构建和冒烟测试。
- ⚙️ 当前技术栈：Astro 7、Tailwind CSS 4、Preline 5、TypeScript 6，Dependabot 维护依赖。
- 🤖 对 AI 助手友好：AI_GUIDE.md 指导 Cursor、Copilot、Claude 了解项目结构与约定。
- 🚀 快速开始：需要 Node.js 22 和 pnpm 9+；可用 GitHub 模板或克隆仓库，执行 pnpm install、pnpm dev、pnpm build、pnpm preview。
- ✏️ 易定制：站点信息、SEO、OG 在 src/data_files/constants.ts；导航和页脚在 src/utils/navigation.ts；页面由 src/components/sections/ 的区块通过 props 组合。
- 📝 内容管理：博客、产品、洞察使用 Markdown/MDX，存放于 src/content/{blog,products,insights}/{en,fr}/，schema 定义于 src/content.config.ts。
- 📚 文档：Starlight 托管于 /welcome-to-docs/，支持搜索、暗色模式、代码高亮和响应式导航；若侧边栏无法滚动需移除 Lenis 脚本。
- 📦 部署：pnpm build 生成 dist/ 静态站点，可部署到 Vercel 或 Netlify；vercel.json 已包含安全与缓存规则。
- 🧭 项目结构：src/ 包含 components、content、data_files、images、layouts、pages、utils；public/、process-html.mjs、scripts/smoke.mjs、vercel.json 等辅助文件。
- 🛠️ 底层特性：Lenis 平滑滚动、GSAP 动画、隐藏滚动条、图片粘贴、HTML 压缩、Prettier 格式化等。
- ✅ 开源与社区：MIT 许可，GitHub 上约 1.4k stars、384 forks；欢迎 issue、讨论和 PR，提交前运行 pnpm format:fix 和 pnpm build；示例公司、产品与 Logo 为虚构，需替换。

---

### [](https://datenstrom.se/yellow/)

**原文标题**: [For people who make small websites - Datenstrom Yellow](https://datenstrom.se/yellow/)

Datenstrom Yellow 是一个有趣、轻量且开源的内容管理系统，无需数据库或后台管理面板，主要通过文件和文件夹管理，适合小型网站、维基和博客，并可在浏览器中即时编辑。

- 🎈 使用有趣：在浏览器中登录用户账户即可编辑网站，使用导航、修改内容并立即查看结果。
- 🚫 没有数据库、没有管理面板、没有杂物，不会妨碍你的操作。
- 🧪 可以先试用演示。
- ⏱️ 几分钟即可安装：下载一个文件、解压，然后复制到 Web 服务器。
- 🧩 核心功能已包含，还可安装扩展来添加功能、语言和主题；项目开源。
- 🚀 可以快速开始，并获取扩展。
- 📁 仅由文件和文件夹组成：适合制作小型网站、维基和博客。
- ✍️ 可使用喜欢的文本编辑器，在电脑上修改一切，方便开发者、设计师和译者。
- 🔄 适应你的工作流程，让你按最适合自己的方式工作。
- 🆘 可以获取帮助。

---

### [](https://github.com/freshjuice-dev/astro-webmcp)

**原文标题**: [GitHub - freshjuice-dev/astro-webmcp: Astro integration that exposes your site content via WebMCP for AI agents · GitHub](https://github.com/freshjuice-dev/astro-webmcp)

overview summary
@freshjuice/astro-webmcp 是一个 Astro 集成，可通过 WebMCP 将站点内容暴露给 AI 智能体，让 Astro 网站用一行代码变得“AI-agent ready”。它支持内置工具、自定义工具、声明式表单扫描、多种搜索后端与安全控制，并基于 fabricioctelles/astro-webmcp 由 FreshJuice 维护增强。

- 🚀 项目定位：Astro 集成，通过 WebMCP 向 AI agents 暴露站点内容，使其能调用结构化工具。
- 🌐 WebMCP 概念：Chrome 提出的 Web 标准，让网站声明 AI 可执行工具，例如搜索文章、导航分区、获取页面元数据。
- 📦 安装方式：运行 `npm install @freshjuice/astro-webmcp`，并在 `astro.config.mjs` 的 `integrations` 中加入 `webmcp()`。
- ⚙️ 主要配置：`collections`、`customTools`、`formScanning`、`search`、`security`，可过滤集合、注册自定义工具、启用表单扫描和设置安全策略。
- 🧩 自定义工具：每个工具有 `name`、`description`、`inputSchema`、`executeBody`、`annotations`；`executeBody` 在浏览器运行，接收 `params`、`safeOutput`、`signal`。
- 🔎 搜索后端：`search_content` 支持 `manifest`、`pagefind`、`orama` 三种后端，并会自动回退到 manifest 搜索。
- 📝 表单扫描：当 `formScanning: true` 时，带 `toolname` / `tooldescription` 的 `<form>` 会自动注册为 WebMCP 工具，也兼容旧版属性。
- 🧰 内置工具：包括 `search_content`、`list_sections`、`go_to`、`get_page_info`，以及声明式表单和用户自定义工具。
- 🏗️ 架构流程：构建时生成 `/_webmcp/manifest.json`；运行时注入脚本，获取 manifest 并调用 `document.modelContext.registerTool()` 注册工具。
- 🌍 浏览器支持：WebMCP 正在 Chrome 149–156 进行 Origin Trial，开发可用 Chrome Flag，生产需注册 Origin Trial token，H2 2026 目标原生支持。
- 🔐 安全设计：遵循 Chrome Agent Security Guidelines，包含只读提示、不可信内容提示、用户交互确认、输出截断、防提示注入和跨域控制。
- 🍹 FreshJuice 改进：修复脚本注入、增加自定义工具 API、Pagefind/Orama 搜索、声明式表单扫描、增强元数据，并转为英文文档与注释。
- 📚 附加信息：项目提供 Usage Guide、Architecture、Changelog，采用 MIT 许可证。

---

### [](https://github.com/raulcanodev/zenex-cms)

**原文标题**: [GitHub - raulcanodev/zenex-cms: Minimal CMS for indie blogging · GitHub](https://github.com/raulcanodev/zenex-cms)

Zenex CMS 是一个面向独立博客的多语言无头 CMS，基于 Next.js 16、React 19、Prisma 6、PostgreSQL 与 Editor.js 构建；灵感来自 Zenblog，但为独立代码库，提供多博客协作、内容编辑、公共/私有 API、MCP 与 OAuth 接入能力。

- 🧩 核心功能：支持多博客、所有者/成员协作、作者、分类、标签、Editor.js 内容、草稿/发布、SEO 字段和关联翻译。
- ☁️ 可选集成：支持 OpenAI 翻译和 Cloudflare R2/S3 兼容图片存储；公共媒体 URL 无需认证即可访问上传图片，包括草稿中的图片。
- 🖥️ 本地运行：需 Node.js 24.x 与 PostgreSQL；执行 npm ci、配置 .env、运行 Prisma generate/migrate dev、npm run dev，访问 localhost:4444。
- 🌐 公共 API：无需认证，仅返回已发布内容；支持文章、分类、标签、分页、语言过滤与 includeContent，请求草稿或全部状态会返回 400。
- 🔒 私有编辑 API：基路径为 /api/v1/blogs/{blogId}，使用 Bearer API key；支持文章、分类、标签、作者、媒体等 CRUD，私有路径使用记录 ID。
- 📦 请求限制：私有 JSON 请求体限制 1 MiB；base64 图片解码上限 700 KiB；仪表盘 multipart 上传保留 10 MiB 图片限制。
- 🔑 API 密钥：仅所有者可创建/列出/撤销；默认 content:read + content:write，可增加 publish、delete、blog:write、media:write；密钥为 256 位随机、仅存 SHA-256 哈希、默认 90 天过期、每博客最多 25 个。
- 🚦 权限与限流：发布或编辑已发布文章需 write+publish，删除已发布需 delete+publish；每密钥每分钟 120 次认证请求，429 返回 Retry-After: 60。
- 🤖 MCP 接入：支持 Streamable HTTP 远程端点和本地 stdio 桥，共享私有 API 的操作与权限，并提供 mcp-server/ 独立网关。
- 🔗 OAuth：支持 ChatGPT、Claude 等连接器通过动态客户端注册、授权码/刷新令牌、撤销端点接入；每次授权限定一个博客及相应 scopes。
- 🧪 开发命令：npm run typecheck、npm test、npm run lint、npm run build。
- 🏗️ 架构：lib/integrations 管理作用域、模式、操作目录、鉴权、HTTP 护栏、MCP 与 OpenAPI；服务层共享内容、密钥、媒体逻辑；REST、MCP 与 OpenAPI 共用操作目录。
- 🚀 部署迁移：先备份并审查迁移，再运行 npx prisma migrate deploy；不要在生产使用 migrate dev 或 db push，也不要在每个副本启动时自动迁移。
- 🗃️ 迁移说明：首个迁移添加 ApiKey 表；后续迁移加入 neverExpires 并使 expiresAt 可选；旧 365 天密钥可变为不过期，但保留原过期时间以兼容。
- ✅ 上线验证：以所有者创建最小权限密钥，验证草稿 CRUD、无 publish 时拒绝发布、MCP initialize/list/call 与 stdio、撤销后 401、跨博客拒绝、公共 GET 不返回草稿。
- ⚠️ 安全注意：状态 published 会立即公开，publishedAt 不是调度器；代理应默认草稿并获批准后再发布/删除；媒体公开且非恶意软件扫描；编辑内容应视为不可信，包括提示注入风险。
- 📚 文档与社区：运行中应用提供 /docs/api/management、/docs/mcp、/api/v1/openapi；仓库为 Public，约 18 stars、3 forks、33 commits，主题为 indie blogging/CMS。

---

### [](https://github.com/arnarg/nixtml)

**原文标题**: [GitHub - arnarg/nixtml: Static website and blog generator written in nix · GitHub](https://github.com/arnarg/nixtml)

nixtml 是一个用 Nix 编写的静态网站/博客生成器，灵感来自 Hugo，采用 MIT 许可证，在 GitHub 上约有 195 个 Star。它通过 Nix flake 和模块化配置，支持 Markdown 内容、静态资源、集合分页、RSS 与分类法，并提供 Nix 函数式 HTML 或字符串模板来构建页面。

- 🛠️ 项目定位：`arnarg/nixtml` 是一个受 Hugo 启发的静态网站生成器，主要使用 Nix 实现。
- ⭐ 仓库概况：公开仓库，MIT 许可证，约 195 Star、1 Fork、1 Issue，23 次提交。
- 🚀 快速开始：通过 `flake.nix` 引入 `nixtml`，使用 `nixtml.lib.mkWebsite` 构建网站，可配置名称、`baseURL`、元数据和内容目录。
- 📁 内容与静态资源：`content.dir` 会遍历 Markdown 文件并生成对应 HTML，例如 `about.md` 变为 `about/index.html`；`static.dir` 可复制整个静态目录并符号链接到最终网站。
- 🧩 模板系统：模板定义在 `website.layouts` 下，模板是返回字符串或字符串列表的函数；支持 Nix 函数式 HTML 标签，也支持普通字符串模板。
- 🏗️ 标准模板：包括 `base`、`home`、`page`、`collection`、`taxonomy` 和 `partials`，分别用于网站骨架、首页、普通页面、集合分页、分类分页和可复用片段。
- 📚 集合功能：`website.collections.<name>` 可对相关内容分组、分页和列出，例如博客文章，并支持 `pagination.perPage` 与 `rss.enable`。
- 🏷️ 分类法：可在集合中启用 `taxonomies`，如 `tags`、`series`，并在 Markdown YAML frontmatter 中填写对应术语，自动生成分类页面。
- 📡 RSS 与分页：集合可生成 `index.xml`，并自动创建如 `blog/index.html`、`blog/page/2/index.html` 等分页页面。
- 🧾 集合/分类上下文：模板可获取 `pageNumber`、`totalPages`、`items`、`hasNext`、`hasPrev`、`nextPageURL`、`prevPageURL`；分类模板还包含 `title`。
- 🧪 示例：仓库提供 `examples` 目录，可用 `nix build .#examples.simple` 和 `nix build .#examples.blog` 构建查看。

---

### [联系 Web Tools](https://webtoolsweekly.com/contact?opt=classifieds)

**原文标题**: [Contact Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

本页介绍如何就 Web Tools Weekly 的广告投放进行咨询与预订，并列出广告方案及联系表单字段。

- 📢 想了解 Web Tools Weekly 广告，可先查看“Advertising Plans”页面中的选项。
- ✉️ 发送消息可询问当前广告位是否可用。
- 📝 若需讨论方案或预订位置，请填写下方表单。
- ⚠️ 该表单仅用于广告咨询。
- 💬 一般咨询或提交工具，可通过 X 私信、Bluesky 聊天，或回复订阅邮件联系。
- 📋 表单必填项包括：姓名、邮箱、广告 URL、期望广告方案。
- 🧾 可选广告方案：顶部广告+顶部文字链接、付费产品评测、中部图片广告、文字链接组合、分类广告、广告互换。
- 🗒️ 还可填写评论/说明。

---

### [](https://merget.ai/)

**原文标题**: [Merget â Coming soon](https://merget.ai/)

Merget 是一个即将上线的“语义合并队列”工具或服务，目前提供电子邮件和 LinkedIn 作为联系或关注渠道。

- 🧩 Merget：产品/项目名称。
- 🔀 The Semantic Merge Queue：核心定位是语义化合并队列。
- ⏳ Coming soon：即将推出，尚未正式发布。
- 📧 Email：提供电子邮件联系或订阅入口。
- 💼 LinkedIn：提供 LinkedIn 关注或联系渠道。

---

### [学习 Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

**原文标题**: [Learn Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

尚未提供需要总结的文本，因此无法生成内容摘要。请补充文章内容后，我将按要点进行总结。

- 📄 当前未检测到任何可供总结的文章或文本内容。
- ✍️ 请提供原文，我会提取关键信息并生成简洁的中文要点。
- 🧭 输出格式将包括概述摘要，以及每条以“-”开头并配有合适表情符号的要点。

---

### [AEO 上帝模式 | 面向 WordPress 的答案引擎优化](https://aeogodmode.io/)

**原文标题**: [AEO God Mode | Answer Engine Optimization for WordPress](https://aeogodmode.io/)

AEO God Mode 是 Metronyx AI 推出的 WordPress 答案引擎优化插件，帮助网站在 ChatGPT、Perplexity、Gemini 和 Google AI Overviews 中被发现、理解并引用；提供结构化数据、llms.txt、AI 爬虫管理、引用追踪、内容优化与竞品分析，含免费、Pro、Growth 和 Agency 方案。

- 🚀 定位：不只优化 Google，而是让 AI 搜索引擎发现、理解并引用站点内容。
- 🧩 免费核心版：不限站点、10 AI credits/月，含 Schema 引擎、llms.txt、内容差距扫描、爬虫允许列表/日志、内容健康、Schema 验证、冲突检测等。
- ⚙️ Pro 版：$19/月（年付 $228），1 站点、500 AI credits/月，增加引用追踪、E-E-A-T、GSC、主题地图、答案密度、AI 元数据、智能内链、内容再利用等。
- 📈 Growth 版：$49/月（年付 $588），最多 5 站点、1500 AI credits/月，含全市场主题地图、竞品引用间谍、索引 AI 提及搜索、Will AI Quote Me 等。
- 🤖 AI 爬虫允许列表：一键管理 18+ AI 爬虫，写入 robots.txt，并监控 GPTBot、PerplexityBot、ClaudeBot、Google-Extended 等访问。
- 🧠 Schema 引擎：自动注入 Article、FAQ、HowTo、Product、LocalBusiness 等 JSON-LD，并验证 Google Rich Results。
- 📄 llms.txt 生成器：从站点自动生成 LLM 上下文文件，支持自定义指令，示例规范合规 6/6。
- 🔍 引用追踪：查询 Perplexity、ChatGPT、Gemini、Claude，判断域名是否被引用，示例命中率 73%。
- 🧮 可引用性评分：用 10 项信号给出 A+ 到 F 评分，预测 AI 引用可能性并给出修复建议。
- 🧑💼 E-E-A-T 作者资料：输出 Person schema、作者卡片、资历、专业标签和社交链接，强化可信度信号。
- 🔗 Google Search Console：一键连接索引、点击与爬取数据，含 AI Query Explorer 和关键词聚类。
- 🧰 兼容与设置：与 Yoast、Rank Math、Elementor、WooCommerce 等共存，5 分钟内完成设置。
- 📊 市场依据：ChatGPT 每周 9 亿用户；63% 网站已获 AI 搜索访客；AI 搜索访客转化率高 23 倍。
- 🎯 适用对象：博主/出版者、本地商家、SaaS/产品站和代理商。
- 💰 联盟计划：最高 40% 佣金，起始 25%。

---

### [Git2](https://git2docs.com/)

**原文标题**: [Git2Docs — AI-generated documentation that stays in sync with your code](https://git2docs.com/)

Git2Docs 是一个面向智能体时代的 AI 原生文档平台，可从 Git 仓库自动生成并维护与代码同步的文档，并通过运行时验证和 RAG 支持聊天机器人确保准确性与可用性。

- 🚀 **核心价值**：连接 Git 仓库即可自动生成完整、一致、始终最新的文档；AI 写文档，你来审核。
- 📏 **可度量文档**：对照代码验证每一条文档声明，追踪准确率与覆盖率，确保达到目标。
- 🔄 **五步流程**：摄取 → 分析 → 生成 → 优化与验证 → 同步；代码推送后文档自动更新。
- 🧠 **代码理解**：使用 tree-sitter 按语言解析 API、模型、配置和业务逻辑，构建完整语义地图。
- 💻 **语言支持**：TypeScript、JavaScript、Python、Go、Rust、Java、C、C++、Ruby；更多语言可申请。
- 🧪 **运行时验证**：接入编程智能体（推荐 Claude Code，也支持 Codex / Antigravity），对实时部署执行文档中的 CLI/API 调用，发现不一致并批量修复。
- 💬 **L1 支持聊天机器人**：Team 和 Enterprise 自带基于已发布文档的 RAG 聊天机器人，答案有引用、不编造、零配置。
- 📈 **自我改进**：机器人无法回答的问题会进入维护者仪表盘，一键加入文档简报，下次再生成时补齐。
- 🧩 **平台功能**：分区编辑与反馈、AI 批量修复、仓库健康仪表盘、品牌与自定义域名、富文本编辑、多文档空间、每次推送自动同步。
- 💰 **商业价值**：相比雇佣 1–2 名技术写作者（年薪 $90K–$140K）和 L1 支持团队，可 10 倍更快创建文档、100% 代码准确、$0 技术写作者成本，并始终与代码同步。
- 🎯 **适用对象**：初创与成长期公司、客户支持、产品经理、工程团队、企业 DevOps。
- 💵 **定价**：Builder $69/月（最多 5 个仓库，约 30K LOC）；Team $99/月（最多 10 个仓库，约 80K LOC，含 1,000 次/月聊天，超量 $2/1K LOC）；Enterprise 定制（不限仓库/LOC，10,000 次/月聊天，SLA、SSO/SAML、私有云）；年付省 15%。
- 🎁 **行动号召**：提供 30 天免费试用，停止从零写文档，开始生成文档。

---

### [获取失败](https://recs.page/web-tools-weekly?ref_code=fde5b5c207&lc=link_campaign_d8b9780aafe8&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recs.page/web-tools-weekly?ref_code=fde5b5c207&lc=link_campaign_d8b9780aafe8&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [](https://sourcetodesign.com/)

**原文标题**: [Source to Design - Frontend projects to editable Figma layers](https://sourcetodesign.com/)

目前没有收到可总结的文章内容，因此无法生成摘要。

- 📭 当前输入为空，缺少需要总结的正文。
- 📝 请提供或粘贴文章内容。
- ✅ 收到文本后，我会用中文输出概览摘要和 emoji 要点列表。

---

### [Respectify — AI 评论审核 | Perspective API 替代方案](https://respectify.org/)

**原文标题**: [Respectify — AI Comment Moderation | Perspective API Alternative](https://respectify.org/)

Respectify 是一款帮助在线社区在评论发布前进行审核与引导的工具，可识别不当、无关、低质量或编码性言论，并教育用户修改。它支持 API、WordPress、JSON 等方式集成，可作为 Perspective API 的近乎无缝替代，目标是维护尊重、相关且有建设性的讨论。

- 🛡️ 在评论发布前拦截不当内容，并解释原因，让用户编辑后重试。
- 🎓 不只是审核，还“教化”用户，帮助改善评论质量。
- 🎯 可配置保持评论与页面或博客主题相关。
- 🚫 可禁止不想要的内容，如 troll、伪善意评论及特定表达。
- 🐕 识别“狗哨”式编码语言，并按站点、话题和受众定制。
- 📧 用 AI 理解上下文和意图来防垃圾评论，不依赖黑名单或验证码。
- ✍️ 帮助用户更好表达，检测措辞不当与潜在误解并建议改写。
- 👍 识别并突出积极评论，鼓励更尊重、更投入的社区互动。
- 🌍 过滤不尊重评论、推广正面互动，营造安全欢迎的环境。
- 🔌 可作为 Perspective API 的近乎即插即用替代，提供 API、演示、仪表盘、定价和文档。
- 🐻 以熊的评论为例，展示逻辑谬误、冒犯短语、负面语气和低投入评论。
- 📊 API 返回 logical_fallacies、objectionable_phrases、negative_tone_phrases、appears_low_effort、overall_score 等字段。

---

### [](https://x.com/EthanDriskill/status/2095713237513728445)

**原文标题**: [Ethan Driskill on X: "Show me a sick high-converting, well designed, intentionally branded website created by Claude or Codex." / X](https://x.com/EthanDriskill/status/2095713237513728445)

这条帖子是 Ethan Driskill 在 X 上公开征集案例：希望看到由 Claude 或 Codex 生成的、高转化、设计精良且品牌表达明确的网站，并附带了该帖的浏览与互动数据。

- 🧑‍💻 发帖人：Ethan Driskill（@EthanDriskill）
- 📣 核心请求：展示由 Claude 或 Codex 创建的“极佳、高转化、设计好、品牌感强”的网站
- 🤖 涉及工具：Claude、Codex
- 🎯 关注重点：转化效果、设计质量、有意图的品牌塑造
- 🕒 发布时间：2026年9月4日 3:19 AM
- 📈 互动数据：178.4K 浏览，120 回复，16 转发，554 点赞，1K 书签/收藏

---

### [路易斯·拉扎里斯 (@LouisLazaris) / X](https://x.com/LouisLazaris)

**原文标题**: [Louis Lazaris (@LouisLazaris) / X](https://x.com/LouisLazaris)

Louis Lazaris 是一位来自加拿大的科技内容创作者，X/Twitter 账号为 @LouisLazaris，个人简介自称“Chairman of the Bored.”，并创办了两份科技通讯，拥有超过 5,400 名关注者。

- 👤 姓名与账号：Louis Lazaris（@LouisLazaris）
- 📝 个人简介：Chairman of the Bored.
- 📰 创办两份科技通讯：webtoolsweekly.com 和 techproductivity.co
- 🔗 相关链接：bio.link/louislazaris、impressivewebs.com
- 📍 地点信息：个人资料写作“Torontocisco, Canadafornia.”，写法较戏谑
- 📅 加入时间：2009 年 5 月
- 📊 账号数据：5,254 篇帖子、717 个关注、5,454 名关注者
- 🧭 页面栏目：Posts、Replies、Reposts、Media、Mention、Follow 等
- 🔐 页面顶部：包含 Log in / Sign up 登录注册入口

---

### [](https://bsky.app/profile/louislazaris.com)

**原文标题**: [@louislazaris.com on Bluesky](https://bsky.app/profile/louislazaris.com)

该内容是 Bluesky 的个人资料页面提示与用户简介，说明页面依赖 JavaScript 运行，并列出 Louis Lazaris 的身份、项目链接和社交信息。

- ⚠️ 页面要求启用 JavaScript，因为这是高度交互的 Web 应用，简单 HTML 界面无法呈现。
- 🧩 可前往 bsky.social 和 atproto.com 了解更多关于 Bluesky 的信息。
- 👤 个人资料属于 Louis Lazaris，个人网站为 louislazaris.com。
- 🆔 其去中心化标识符为 did:plc:6if43vohxmohxuooa7bkkw5q。
- 💻 他是前端开发者和 newsletter 策划人。
- 🔗 相关项目包括 Web Tools Weekly、Tech Productivity、VS Code Email 和个人网站。
- 🎸 还运营面向吉他爱好者的 YouTube 频道 @tunejotter。

---

### [向 Web Tools Weekly 提交工具](https://webtoolsweekly.com/submit)

**原文标题**: [Submit a Tool to Web Tools Weekly](https://webtoolsweekly.com/submit)

如果你开发了或知道对前端开发者可能有用的工具，可通过 X 或 Bluesky 提交；可提交多种开发工具，但不接受文章/教程，生产力工具需提交至 Tech Productivity。

- 📩 通过 X 私信 @LouisLazaris 提交
- 💬 通过 Bluesky 聊天 @LouisLazaris.com 提交
- 📚 可提交库、框架、插件、脚本
- 🌐 可提交 Web 应用、桌面应用、移动应用
- 🔌 可提交 API/服务、编辑器/IDE
- 🛠️ 也可提交任何其他对 Web 开发者、程序员或设计师有用的工具
- 🚫 不要提交文章或教程，它们不会被收录
- 📈 生产力相关工具已移至 Tech Productivity，也可按上述方式提交

---

### [免费在线帆船模拟器与游戏 | VibeSail](https://vibesail.com/)

**原文标题**: [Free Online Sailing Simulator & Game | VibeSail](https://vibesail.com/)

VibeSail 是一个免费在线 3D 帆船模拟器与航行游戏，无需下载，打开浏览器即可游玩；它提供真实航行物理、互动教学、每日比赛、多人航行和世界地图等内容，并支持桌面与移动端。

- ⛵ 免费在线 3D 帆船模拟器/航行游戏，浏览器直接玩，无需下载或安装。
- 🌬️ 真实航行物理：风向角、帆面调整、船体倾斜与船只响应都会影响操作。
- 🏁 多种玩法：自由航行、每日竞赛、实时多人帆船以及 High Sea 远航挑战。
- 🎓 互动教程：新手可学习转向、调帆和起步，然后再参加比赛。
- 🗺️ 包含世界地图、城市、排行榜等探索与竞技内容。
- 💻 支持桌面和移动浏览器，可用键盘、触屏或手柄操作。
- ❓ FAQ 说明：免费游玩、无需下载、支持移动端；控制可从教程学起，再到自由航行练习调帆和换舷。
- 📧 可订阅罕见游戏更新邮件，无垃圾邮件，并提供隐私与联系方式。

---

### [](https://webtoolsweekly.com/)

**原文标题**: [Web Tools Weekly | A Weekly Newsletter for Front-end Developers](https://webtoolsweekly.com/)

Web Tools Weekly 是面向 Web 开发者的每周邮件通讯，已有 15,615 名订阅者，承诺每周一封、无垃圾邮件，并展示大量读者自发好评。读者普遍称赞它能帮助发现新工具、JavaScript 技巧和前端资源，是值得长期订阅的高价值精选通讯。

- 📬 定位：面向 Web 开发者的每周通讯，目前有 15,615 名订阅者。
- 📧 订阅说明：每周发送一封邮件，无垃圾邮件；页面提供隐私政策、条款及 reCAPTCHA 相关信息。
- 🧰 主要内容：聚焦新 Web 工具、库和前端开发资源，帮助开发者保持更新。
- 💡 特色亮点：每期包含 JavaScript 技巧，读者认为实用且富有启发性。
- 🌟 读者评价：被称为“很棒”“最有用”“必订”的科技与 Web 开发通讯之一。
- ⏳ 长期价值：不少读者订阅多年，表示每周期待、从未错过，并持续获得价值。
- 🛠️ 实际效果：读者通过它发现许多常用新工具，并感谢作者的精选与整理。
- 🙌 口碑来源：页面汇总了来自邮件和社交媒体的读者自发好评样本。

---

