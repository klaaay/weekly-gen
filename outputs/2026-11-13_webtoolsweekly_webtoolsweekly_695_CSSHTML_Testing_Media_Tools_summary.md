### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=clickrelay&utm_medium=paid_newsletter&utm_campaign=tiger-cloud-free-trial-1-000-credits&utm_content=web-tools-weekly)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=clickrelay&utm_medium=paid_newsletter&utm_campaign=tiger-cloud-free-trial-1-000-credits&utm_content=web-tools-weekly)

Tiger Data 的 Tiger Cloud 提供面向任意规模时序工作负载的 Postgres 服务，突出超大规模真实表现、弹性伸缩、高可用、企业级合规与可观测性，并提供快速开通和生态集成；新账户可获 1000 美元信用额度。

- 🚀 单个 Tiger Cloud 服务可达每天 3 万亿指标、3 PB 数据、1000 万亿数据点。
- 🎁 新账户注册可获 $1000 信用额度，30 天有效，无需信用卡，仅限新账户。
- 🏭 受数千家 IoT 公司信赖。
- 📈 通过最多 10 节点副本集分离读写，并用 SSD/S3 分层存储实现低成本、可扩展存储。
- 💰 计算与存储解耦，可独立扩展，避免为空闲容量付费。
- 🛡️ 多可用区集群支持自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级能力包括 SOC 2、HIPAA、GDPR 合规、始终加密、SSO、RBAC 和审计日志。
- 🔍 深度可观测性：查询下钻、仪表盘，并可将指标发送至 CloudWatch、Datadog、Prometheus。
- ⚡ 数分钟内开通数据库，可通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 可与首选云厂商及更广泛的 Postgres 生态集成。
- 🏢 企业版提供合同化 SLA、区域数据隔离、合规认证及 7×24 全球 Postgres 专家支持。
- ©️ 页面版权信息显示 2026 年 Timescale, Inc.（d/b/a Tiger Data）保留所有权利。

---

### [Gradient Studio — 免费程序化 CSS 渐变生成器 | Amit Gajare](https://gradientsaas.blogspot.com/)

**原文标题**: [Gradient Studio — Free Procedural CSS Gradient Generator | Amit Gajare](https://gradientsaas.blogspot.com/)

这是一个免费的编辑风格 CSS 渐变生成器“Gradient Studio”，由 Amit Gajare 打造，可用于创建带光影效果的高级背景，并导出为 CSS、Tailwind 或 SCSS。

- 🔒 项目编号为 No. 001，当前状态为锁定。
- 🎨 主题为“编辑渐变研究”（Editorial gradient study）。
- 🛠️ 工具名为 Gradient Studio。
- 🆓 这是一款免费的、程序化生成的编辑风格 CSS 渐变生成器，作者是 Amit Gajare。
- ✨ 支持创建带光影处理的高级背景。
- 📤 可导出为 CSS、Tailwind 或 SCSS。

---

### [GitHub - aarongustafson/form-saver：一个 Web 组件，用于存储（并恢复）其所包裹表单中的值 · GitHub](https://github.com/aarongustafson/form-saver)

**原文标题**: [GitHub - aarongustafson/form-saver: A web component that stores (and restores) values within the form it wraps · GitHub](https://github.com/aarongustafson/form-saver)

form-saver 是 Aaron Gustafson 开发的 Web Component，用于保存并恢复其包裹的第一个表单中的值，主要面向崩溃恢复和中断会话场景。

- 🧩 包裹表单后自动保存输入值，页面重新加载时可恢复；成功提交流程后清除已保存数据。
- 💾 用户输入时以防抖方式写入 `localStorage`，减少频繁序列化和写入；页面隐藏时会刷新待处理更改。
- 🔐 永不保存或恢复密码字段，文件字段也会被排除；即使字段名出现在 `retain` 中也不会保存密码。
- 📝 支持 `input`、`textarea`、`select`（单选和多选），但排除 `password`、`file`、`submit`、`button`、`reset`、`image` 等类型。
- 📦 安装方式为 `npm install @aarongustafson/form-saver`，可自动定义 `<form-saver>`，也可导入 `FormSaverElement` 手动注册自定义标签。
- 🏷️ 主要属性包括 `retain`、`retain-choice`、`retain-choice-label`、`retain-choice-container`、`storage-key`；默认存储键格式为 `form-saver:{method}:{resolvedActionUrl}`。
- ✅ `retain` 可指定提交后保留的字段；`retain-choice` 可注入用户选择是否保留信息的复选框，并支持通过 CSS 选择器控制插入位置。
- 🛠️ 提供 `saveFormState()`、`restoreFormState()`、`clearSavedData()` 方法；手动保存立即执行，事件触发保存使用短防抖。
- ⚠️ 数据以明文存储在 `localStorage` 中，同源 JavaScript 可读取；存储失败时会派发冒泡且 composed 的 `form-saver-error` 事件，`detail` 包含 `operation` 和 `error`。
- 🌐 基于 Custom Elements v1、Light DOM 和 ES Modules，旧浏览器可能需要 polyfill；项目采用 MIT 许可证。

---

### [网站规范](https://specification.website/)

**原文标题**: [The Website Specification](https://specification.website/)

概述：这份指南说明“一个好网站”需要做什么，覆盖从页面 `<title>` 到 HTTP 响应头的技术细节，面向人类与 AI 代理，适用于任意技术栈；共包含 185 个主题、10 个领域，并提供可执行清单与审计流程。

- 🧭 网站职责涵盖四类：文档基础、用户体验、信任保护、发现与理解；一个网站需同时承担这些责任。
- 🗂️ 10 大领域包括：基础（23）、SEO（14）、无障碍（31）、安全（25）、Well-Known URI（13）、AI 代理就绪（23）、性能（27）、隐私（7）、韧性（9）、国际化（13）。
- ✅ 清单按状态分级：必需 36 项、推荐 92 项、可选 51 项、应避免 6 项；每项均为“是/否”判断。
- 📖 每个主题解释“是什么、为何重要、如何实现”，并强调每项细节都有标准依据，且平台无关。
- 🛠️ 使用方式是阅读规范、检查站点、审计缺失、修复后复检，以持续改进网站。
- 🤖 除面向人的 HTML 外，还提供面向代理的 Markdown、llms.txt、Agent Skill 和开放只读 MCP 服务器，参考工具无需认证。
- 🔄 规范持续更新，例如 2026-11-11 新增自动填充令牌、内置 AI API、可定制 select 页面；项目开源并欢迎 PR。

---

### [订阅 | 代码](https://codenewsletter.ai/subscribe?utm_source=clickrelay&utm_medium=paid_newsletter&utm_campaign=the-code-subscriber-growth&utm_content=web-tools-weekly)

**原文标题**: [Subscribe | The Code](https://codenewsletter.ai/subscribe?utm_source=clickrelay&utm_medium=paid_newsletter&utm_campaign=the-code-subscriber-growth&utm_content=web-tools-weekly)

每天只需5分钟，即可学习如何借助AI更快编写代码；内容面向35万+ CTO、工程师和技术领导者，提供高价值的AI软件开发新闻、趋势资源与工具，并邀请免费订阅及注册领取200+免费工程资源。

- ⏱️ 每天用5分钟学习如何借助AI提升编码速度。
- 👥 面向35万+ CTO、工程师和技术领导者。
- 📰 提供高价值的AI软件开发新闻、趋势资源和工具。
- 🎁 可免费订阅，并注册获取200+免费工程资源。
- 🔐 页面包含隐私政策和使用条款说明。

---

### [dom-docx — 浏览器中的 HTML 转 Word 转换器](https://dom-docx.com/)

**原文标题**: [dom-docx — HTML to Word converter in the browser](https://dom-docx.com/)

dom-docx 是一个将语义化 HTML 片段转换为原生 Word 文档（OOXML）的开源工具，支持浏览器、Node.js 和 CLI，并可将段落、列表、表格和链接转换为 Word 中可编辑的内容。

- 🧩 将 HTML 映射为真实 OOXML，保留段落、列表、表格、链接等可编辑结构。
- 🌐 支持浏览器与 Node 环境，提供 npm 包和浏览器 IIFE 包，方便在应用中实现“导出到 Word”。
- 🚀 无需上传文件、无需 API Key，在线转换器直接在浏览器本地运行。
- 🎨 默认支持内联样式，也可处理样式表或类名 HTML，但计算样式需使用实时 DOM，不依赖 Playwright。
- 💻 提供 CLI 用法：可转换 HTML 文件、从 stdin 管道输入，或全局安装后直接在 PATH 中使用。
- 🖥️ 附带在线演示、Showcase 画廊和 hmr-serve，可预览实时 HTML 后再交给 dom-docx 生成 Word 文件。
- 📈 项目源于提升 HTML→DOCX 转换保真度的实验，经过 40+ 真实测试用例和机器评分循环，布局保真度达到中 90% 以上，高于传统库的中 60% 左右。
- 🗺️ 路线图包括托管 DOCX 转换 API，目前可加入 waitlist 获取早期访问。

---

### [GitHub](https://github.com/bramus/rich-input)

**原文标题**: [GitHub - bramus/rich-input: A rich input field with keyword-based autocomplete and in-input highlighting powered by <datalist>, OpaqueRange, and the Custom Highlight API · GitHub](https://github.com/bramus/rich-input)

`rich-input` 是一个采用 MIT 许可证的 Web Component，由 Bramus 开发。它像原生 `<input type="text">` 一样易用，同时支持 `keyword:value` 查询语法、基于 `<datalist>` 的关键词自动补全、输入内高亮、表单集成，以及面向不支持浏览器的渐进增强回退。它基于 OpaqueRange API 与 CSS Custom Highlight API 实现原生体验。

- 📥 支持 npm 安装、ESM 导入或 CDN 使用，仓库包含源码、测试、演示和构建脚本。
- 🧩 组件行为接近标准文本输入框，支持 `value`、选择范围、标准事件和表单提交。
- 🔍 自动补全覆盖关键词、布尔组合词和值建议，例如输入 `a` 可提示 `artist:`，输入 `AND` 可提示组合词。
- ⚙️ 可通过 HTML 属性或 JavaScript 按实例配置 `operators`、`combinators`、`delimiters`，也可在 `RichInput` 类上设置全局默认值。
- 🗂️ 使用嵌套 `<datalist>` 和 `<option>` 声明关键词与选项，支持运行时动态更新，并会自动为含空格的值加引号。
- 🖼️ 选项内可嵌入 `<img>`，在建议列表中展示 logo、头像或封面等富媒体内容。
- 🎨 使用 CSS Custom Highlight API 高亮关键词、值、操作符、组合词、分隔符和无效标记。
- 📍 使用 OpaqueRange 定位自动补全浮层与高亮范围；不支持时回退到隐藏镜像 `div` 进行测量定位。
- 🧭 在支持 CSS Custom Highlight API 但无 OpaqueRange 的浏览器中，使用 `[contenteditable]` 回退实现输入内高亮。
- 🧱 暴露 `::part(control/input/icon/clear-button/popover/suggestion-item...)` 等 Shadow Parts，便于完整主题化。
- ♿ 遵循 W3C ARIA 1.2 Combobox 模式，支持方向键、Enter、Tab、Escape 等键盘交互。
- 🧠 JavaScript API 提供 `value`、`getParsedQuery()`、`getKeywords()`、选择范围、聚焦/失焦等方法。
- 🔔 事件包括 `input`、`change`、`search` 和 `rich-input-select`，选择建议时可获取类型、关键词、值等信息。
- 📝 支持 `name` 与 `ElementInternals`，可参与 `<form>` 提交、`FormData` 和表单重置流程。
- 🛠️ 构建使用 `npm run build`，本地演示使用 `npm start`，项目采用 MIT 许可证。

---

### [GitHub - viliket/pure-web-bottom-sheet: A performant, lightweight, and accessible bottom sheet web component powered by CSS scroll snap and CSS scroll-driven animations. Works with any framework, supports SSR, multiple snap points, and nested scrolling mode. · GitHub](https://github.com/viliket/pure-web-bottom-sheet)

**原文标题**: [GitHub - viliket/pure-web-bottom-sheet: A performant, lightweight, and accessible bottom sheet web component powered by CSS scroll snap and CSS scroll-driven animations. Works with any framework, supports SSR, multiple snap points, and nested scrolling mode. · GitHub](https://github.com/viliket/pure-web-bottom-sheet)

pure-web-bottom-sheet 是一个轻量、框架无关、可访问的底部面板 Web Component，核心基于 CSS scroll snap 与 CSS scroll-driven animations，以浏览器原生滚动实现接近原生的交互，并支持 SSR、多个吸附点和嵌套滚动。

- 🧩 以 Web Component 形式实现，兼容任意框架或原生 HTML，支持 SSR 与 Declarative Shadow DOM，可减少首屏 FOUC。
- ⚡ 核心功能近乎零 JavaScript，依赖浏览器原生滚动机制，性能好且接近原生手感。
- 📐 支持多个吸附点，通过 `slot="snap"` 与 `--snap` 设置位置，`initial` 指定初始吸附点，`top` 标记完全展开位置。
- 🔽 支持 `swipe-to-dismiss`、`nested-scroll`、`content-height`、`expand-to-scroll` 等模式，并可与 Dialog/Popover API 配合实现模态或非模态底部面板。
- 🧱 提供 `<bottom-sheet>` 与 `<bottom-sheet-dialog-manager>`；后者封装原生 `<dialog>`，处理背景点击关闭和下滑关闭。
- 🛠 API 包括 CSS 变量 `--sheet-max-height`、`--sheet-background`、`--sheet-border-radius`，事件 `snap-position-change`，方法 `snapToPoint(index, options)`。
- 🎨 可通过 `::part(sheet/handle/content/header/footer)` 自定义样式，并提供 default、snap、header、footer slots。
- 📦 安装方式为 `npm install pure-web-bottom-sheet`，提供 Vanilla HTML、Astro、React、Vue 示例及 React/Vue 包装组件和 `BottomSheetElement` 类型。
- 🌍 已在 Chrome、Safari、Firefox 的桌面和移动端测试；Safari 需 18.2+，因其依赖离散滚动吸附动画特性。
- 🪪 采用 MIT 许可证，仓库约 225 stars、6 forks，附演示、API 参考和贡献指南，欢迎社区贡献。

---

### [Markuplint - 面向所有标记开发者的 HTML 代码检查工具。 | Markuplint](https://markuplint.dev/)

**原文标题**: [Markuplint - An HTML linter for all markup developers. | Markuplint](https://markuplint.dev/)

Markuplint 提供规范校验、项目规则、组件结构检查、按选择器应用规则、多语法支持和 VS Code 实时反馈等核心能力，帮助团队提升标记语言的可靠性与一致性。

- 🚨 **一致性检查**：依据 HTML Standard、WAI-ARIA 等规范校验 HTML，捕获浏览器可能忽略、但辅助技术和搜索引擎会受影响的错误。
- 🛡 **项目自定义规则**：支持配置无障碍、安全、性能和命名规范等规则，把团队约定变成可自动检查的标准。
- 📐 **设计系统结构校验**：检查元素的属性、特性及父子关系，确保组件按设计系统正确使用，维护组件契约。
- 🆔 **按选择器应用规则**：可通过 CSS 选择器、扩展伪类或正则表达式定位元素，精细控制规则适用范围与严格程度。
- 📝 **支持多种语法**：除 HTML 外，还可通过官方解析器插件检查 JSX（React）、Vue、Svelte、Astro、Alpine.js、HTMX、Pug、PHP、Smarty、eRuby、EJS、Mustache/Handlebars、Nunjucks、Liquid、Markdown、MDX 及 lit-html 标签模板字面量。
- 🧩 **VS Code 扩展**：安装后无需项目配置，打开 HTML 文件即可在输入时获得实时检查反馈。

---

### [ascii.rest：用于网页的动态 ASCII 艺术，作者 @bas3line](https://ascii.rest/)

**原文标题**: [ascii.rest: animated ascii art for web pages, by @bas3line](https://ascii.rest/)

ascii.rest 是一个面向网页的动画 ASCII 艺术资源库与组件集合，提供可复制使用的场景、加载动画、图表、文字、Logo 及物理/生成艺术等内容，强调零依赖、TypeScript 类型支持、多框架集成与 MIT 免费使用。

- 🎨 包含 241 件动画 ASCII 作品：34 个全彩场景、加载器、图表、文字、29 个语言 Logo、23 个公司 Logo、23 个 Linux 发行版 Logo，以及 3D 形状、物理模拟和生物等。
- 🧩 每件作品都是小型、带类型的 TypeScript 模块，无第三方依赖，可用于 React、Next.js、Astro 或普通 HTML 页面。
- 🖥️ 支持在终端播放，如 `npx ascii.rest donut`；也可制作 README 横幅，或将任意图片/Logo/照片转换成动画 ASCII。
- 🔌 提供多种接入方式：HTML 标签、React 客户端组件、Astro 服务端首帧渲染、TypeScript `mount` 函数、终端 CLI，以及面向 Claude Code、Cursor、Codex 等编码代理的 skill。
- 🏞️ 场景示例包括土星升起、琥珀堡、皮丘拉湖、雪夜列车、黑色棱镜、云海、冰岛极光、城市夜景、沙漠星空、地球升起等。
- 📊 还包含 UI 组件、数据可视化、字体与 Logo、自然、生物、特效、生成艺术等分类，适合网页装饰与动态展示。
- 📜 项目采用 MIT 许可证，免费使用和修改；源码位于 GitHub，并提供文档、赞助与字体支持信息。

---

### [文档截图自动化 | Heroshot](https://heroshot.dev/)

**原文标题**: [Screenshot Automation for Documentation | Heroshot](https://heroshot.dev/)

该内容介绍一种让文档截图随界面变化自动更新、并通过 CI 保持文档与产品实时一致的方案。

- 🔄 UI 变化时截图会自动重新生成
- 📄 文档能始终与产品实际情况保持一致
- ⚙️ 可通过 CI 自动完成配置与集成
- ✅ 避免文档过时，保持内容长期有效

---

### [GitHub - ajinabraham/njsscan：njsscan 是一款](https://github.com/ajinabraham/njsscan)

**原文标题**: [GitHub - ajinabraham/njsscan: njsscan is a semantic aware SAST tool that can find insecure code patterns in your Node.js applications. · GitHub](https://github.com/ajinabraham/njsscan)

njsscan 是一款面向 Node.js 应用的语义感知静态应用安全测试（SAST）工具，结合 libsast 的模式匹配能力与 semgrep 的语法感知语义搜索，用于发现不安全代码模式。

- 🛡️ 核心定位：面向 Node.js/Express 等应用的 SAST 扫描工具，可发现 XSS、SQL 注入等安全问题。
- ⚙️ 技术组合：使用 libsast 模式匹配器和 semgrep 语义代码搜索，兼具规则匹配与语义分析。
- 📦 安装要求：通过 `pip install njsscan` 安装，要求 Python 3.10+，仅支持 macOS 和 Linux。
- 🖥️ 命令行能力：支持扫描文件或目录，输出 JSON、SARIF 2.1.0、SonarQube、DefectDojo、GitLab SAST、HTML 等格式。
- 🔍 示例发现：可检测 `express_xss`，对应 OWASP A1 Injection、CWE-79，严重级别为 ERROR，并给出文件、行号和匹配代码。
- 🧩 配置方式：可在源码根目录放置 `.njsscan` 文件，或用 `--config` 指定；支持配置扩展名、忽略文件/路径/规则、严重级别过滤与覆盖。
- 🚫 抑制告警：可在触发行添加 `// njsscan-ignore: rule_id1, rule_id2` 来忽略特定规则。
- 🐍 Python API：可通过 `NJSScan` 类调用扫描，返回包含模板、Node.js 发现和错误信息的字典结果。
- 🔄 CI/CD 集成：支持 GitHub Actions、GitHub Code Scanning（SARIF）、GitLab CI/CD 原生 SAST 报告、Travis CI、CircleCI 等。
- 🐳 Docker 支持：可拉取 `opensecurity/njsscan` 镜像或本地构建，挂载源码目录进行扫描。
- 🌐 生态扩展：nodejsscan 基于 njsscan 构建，提供完整的漏洞管理界面及集成能力。
- 📈 项目信息：采用 LGPL-3.0 许可证，仓库约有 459 stars、110 forks，并持续维护。

---

### [网络工具周刊 - 推荐中心](https://recommendations.page/web-tools-weekly/offer_recommendations/offer_recommendation_19e077609f25)

**原文标题**: [Web Tools Weekly - Recommendations Hub](https://recommendations.page/web-tools-weekly/offer_recommendations/offer_recommendation_19e077609f25)

该内容是一个订阅专属优惠页面，主要推广 AI Chief 的免费 AI 洞察与工具资源，但当前优惠在用户所在国家/地区不可用。

- 🌍 订阅专属优惠在用户所在国家/地区无法使用。
- 🆓 提供 100% 免费的 AI 洞察内容，来源为 AI Chief。
- 🚀 强调要“先掌握 AI”，以免被 AI 掌控。
- 🛠️ AIChief 汇集热门工具与突破性进展，帮助节省时间并提升工作流效率。
- 🧠 倡导更聪明地工作，保持竞争力。
- 📩 页面包含“领取优惠”的行动号召。
- 🔎 提示用户可继续发现所有专属优惠。

---

### [找出你的表单永远无法显示的问题 — FormPath](https://form-path.com/)

**原文标题**: [Find questions your form can never show — FormPath](https://form-path.com/)

FormPath 是一款在浏览器内运行的表单逻辑检查工具，可在条件表单出现缺失数据之前，发现 SurveyJS JSON、REDCap 数据字典和 FHIR Questionnaire 中永远无法显示的问题、失效字段引用，以及仍会影响后续问题的隐藏答案。

- 🔍 支持检查 SurveyJS、REDCap 和 FHIR Questionnaire，重点识别不可达问题、断开的引用、陈旧答案风险和修订影响。
- 🧾 对可支持规则尽量给出精确规则、可工作的答案示例或证明，并明确列出无法安全检查的部分。
- 🖥️ 所有分析在浏览器中完成，表单定义无需上传，也不需要参与者数据。
- 🧨 案例 FP–SJS–001 展示了规则把文本“property-use”当作答案字段并拼错“residential”，导致抵押状态问题被证明不可达。
- 📊 2026 年 7 月的便利性审查覆盖 64 个公开工件，发现 7 个受影响文件和 4 种缺陷形态；这些数字用于验证检查器，并非流行率估计。
- 🧪 SurveyJS 的工作答案组合会在 SurveyJS 中回放，支持的不可达规则会用有限证明；REDCap 和 FHIR 结论则明确标注为翻译模型证据。
- 🚩 工具会区分已确认回归、有意行为变化和分析覆盖变化，并诚实标注远程选项、自定义函数、动态行等未知项。
- 🔁 工作流程包括导入定义、运行分析、下载可复用回归测试套件；这些是测试输入，不是完整受访者旅程。
- 🧭 针对 SurveyJS 问题不显示、REDCap 分支逻辑失效、FHIR enableWhen 答案代码不匹配提供故障排查指南。
- ✅ 无需注册或上传即可打开分析器，报告可导出为 JSON 或 Markdown，便于在下一修订版到达受访者前检查。

---

### [OpenAPI 规范审计与就绪度评分 | Octri](https://octri.dev/openapi-audit)

**原文标题**: [OpenAPI spec audit and readiness score | Octri](https://octri.dev/openapi-audit)

Octri 提供 OpenAPI 规范评分工具，用同一套 14 条规则为规范打出 0–10 分，用来预测代码生成器能生成多好的 SDK，而不是评价 API 本身。用户可粘贴 URL 或上传 JSON/YAML，无需账号，规范不会被保存，也可选择发布公开评分页。

- 🎯 评分关注“SDK 生成可用性”：缺少响应 schema 会让方法返回 `any`/`unknown`，内联模型会生成大量重复类型，公开名称冲突会迫使生成器静默重命名方法。
- 🧮 14 条规则按影响范围扣分，规则一旦触发至少损失其权重的五分之一；最重的三条各占 2 分：成功响应声明 schema、共享模型放入 `components` 并用 `$ref`、生成公开名称不冲突。
- 📉 其他重点规则包括：路径占位符必须有参数、必须声明 `operationId` 且命名像方法名、操作需有摘要或描述、请求体需文档化、声明错误响应、操作需打标签、避免重复路径、描述认证方案、参数需说明、声明 server URL。
- 🏅 分数解读：8.0 及以上为 Strong，可生成类型化方法、命名模型和文档注释；6.0–7.9 为 Mixed，客户端可用但存在未类型化返回、裸参数或路径段命名空间；低于 6.0 为 Weak，应先修复重权重规则再发布 SDK。
- 🛠️ 在 Octri 内，14 条规则中有 8 条可一键写入修复并重新评分；规范每次变更都会重新审计，同一文档可驱动参考页、十种语言 SDK 和 MCP server。
- 🔍 示例审计得到 6.8/10、覆盖 24 个操作；公开已评分规范包括 Box 9.1、Petstore 8.7、Adyen 8.7、Asana 8.3、Plaid 7.8、OpenAI 7.6、GitHub 6.9、Stripe 6.6 等。
- 📦 超过约 300 个操作或 400 个模型不会扣分，而会建议按 tag 拆分客户端，避免用户为少量端点安装全部 SDK。
- 🔒 隐私与限制：只保留 `info` 块和扣分规则记录，不保存文档本身；支持 OpenAPI 3.0/3.1/3.2 的 JSON/YAML，不支持 Swagger 2.0；最大 5 MB，每个地址每分钟 10 次审计。
- ✅ 它不是验证器：规范可以完全合法却仅得 4 分，因为“合法”并不代表响应声明了 schema，也不代表能生成好用的 SDK。

---

### [Drydock 软件包审查：查看用户将要安装的软件包中有哪些变化](https://drydock.org/)

**原文标题**: [Drydock Package Review: See what changed in the package your users will install](https://drydock.org/)

Drydock 提供发布前包差异审查：在用户安装前检查变更文件与供应链风险，无需账号或安装即可试用公共包 diff，并可将审查加入构建发布流程。它通过 Workflow Gate 强制暂停 GitHub 发布任务，或用 Stage Watchtower 对 npm 私有暂存包做建议性审查；发布凭据仍保留在 npm/GitHub Actions，由人工最终批准。

- 🔍 发布前检查：对比候选包与已发布基线，查看新增安装脚本、凭据读取等风险，且不执行包内容。
- 🚪 发布门禁：Workflow Gate 在 CI 构建上传后暂停 GitHub 发布任务，批准才继续、拒绝则阻止；覆盖 npm、PyPI、VS Code。
- 📦 npm 暂存审查：Stage Watchtower 审查 `npm stage publish` 的私有候选包并记录决定，最终在 npm 用 2FA 独立批准或拒绝。
- 🔐 安全边界：使用受限令牌获取发布证据，发布凭据留在 npm 或 GitHub Actions；报告保留脱敏证据而非原始归档。
- 🧩 集成方式：可通过 Renovate 预设或 PR 评论工作流，把 npm/PyPI 依赖更新链接到包 diff。
- 🧾 真实案例：node-ipc、semversyphus、es5-ext 展示 runtime 依赖、postinstall 钩子等变更；event-stream、ua-parser-js、node-ipc、chalk & debug 说明恶意代码可能只存在于发布 tarball。
- 🛡️ 来源与人工决策：结合 provenance 证据与包内容审查；维护者通过 CI 门禁或 npm 2FA 做最终批准。
- 🚀 上手：为下一次发布设置 GitHub workflow gate 或连接 npm staging，即可审查候选发布。

---

### [pour · 免费无障碍检查器与 WCAG 2.2 审计工具](https://pour.dev/)

**原文标题**: [pour · Free Accessibility Checker & WCAG 2.2 Audit Tool](https://pour.dev/)

Pour 是一款免费、开源、非营利的网页无障碍审计工具，通过浏览器扩展、书签小工具、命令行、VS Code 扩展与 Meta Quest 应用，帮助发现并修复网站可访问性问题；它强调自动检测与人工审查结合，并推动符合 WCAG 标准。

- 🌍 每六人中约有一人体验网页的方式不同；pour 展示障碍所在并给出具体修复方法。
- 🧩 提供 Chrome、Edge、Firefox 扩展、书签小工具、iOS 快捷指令、CLI 和 Meta Quest 应用，全部免费，无账户、无订阅、无付费层级。
- 🚀 四步上手：安装扩展 → 打开并审计 → 阅读发现 → 修复后重新审计，并可用模拟和键盘检查。
- 👁️ 内置 55+ 视觉、感知与运动模拟及透镜，如隧道视野、白内障、色觉异常、手抖、键盘 Tab 顺序等。
- 📐 以 WCAG 四原则 POUR 命名：可感知、可操作、可理解、健壮。
- 🛠️ 浏览器扩展本地运行审计，按严重性分组、定位元素，支持 DevTools/侧边栏、选择 WCAG 版本级别、导出 Markdown/CSV/JSON。
- 🔖 书签小工具无需安装，可在页面内运行同款审计；但严格 CSP 站点和跨源 iframe 可能受限。
- 💻 命令行工具 `npm install -g pour-cli`：使用 headless Chrome 审计、CI 退出码、模拟截图、爬取站点生成独立 HTML 报告，并支持 MCP 供 AI agent 使用。
- 🧑‍💻 VS Code 扩展可检查 HTML、React、Vue、Svelte、Angular、Liquid、Nunjucks 源码；对比度、点击目标、焦点、动效等仍需浏览器工具。
- 🎨 引擎含 99 条自动规则，协助覆盖 WCAG 2.2 的 86 条成功标准中的 51 条，另 35 条需人工清单，不宣称完全自动判定。
- ⚡ 2026 年 9 月基准：典型页面比 axe-core 快约 3 倍；194,000 元素最大测试页快 24 倍（7 秒 vs 2 分 43 秒）。
- 🎯 Beta Block 测试中检出全部 38 个植入故障并标出 8 个人工判断项，且报告无误报。
- 📊 2026 年 11 月数据：前 10 万网站中 93.9% 存在已证实无障碍失败。
- 🥽 Meta Quest 3/3S 应用将模拟实时叠加到真实房间；无网络/麦克风权限，摄像头帧用后丢弃，非医疗设备。
- ⚖️ 法规趋势：欧盟 EAA 自 2025-06-28 生效并指向 WCAG 2.2 AA；美国 ADA Title II 要求 2027/2028 落实 WCAG 2.1 AA；WCAG 2.2 为当前 W3C 推荐标准。
- ❤️ 非营利设计：所有工具永久免费，欢迎捐赠但不收费。

---

### [GitHub - denodell/playwright-soak-test：使用 Playwright 在几分钟而非几小时内发现单页 Web 应用中的内存泄漏。· GitHub](https://github.com/denodell/playwright-soak-test)

**原文标题**: [GitHub - denodell/playwright-soak-test: Find memory leaks in your single-page web app in minutes rather than hours, with Playwright. · GitHub](https://github.com/denodell/playwright-soak-test)

项目 playwright-soak-test 是一个基于 Playwright 的浸泡测试工具，可在几分钟内发现单页 Web 应用中的内存泄漏。它通过重复执行可回到初始状态的用户流程数百次，持续统计 DOM 节点和事件监听器数量；若计数持续增长，则判定存在泄漏，并借助虚拟时钟和请求模拟覆盖长时间使用场景。

- 🧪 核心原理：重复打开或关闭抽屉、筛选或清除筛选等闭环流程，比较每轮后的 DOM 节点与监听器计数，异常增长即失败。
- ⏱️ 虚拟时钟默认每轮推进 18 秒，200 轮约覆盖 1 小时应用时间；配合 `page.route` 用 fixture 响应请求，避免等待真实服务器。
- 📦 安装：`npm install --save-dev playwright-soak-test`；依赖 `@playwright/test` 1.45+，仅支持 Chromium，Firefox/WebKit 会跳过。
- 🚀 快速使用：从 `playwright-soak-test` 导入 `test`，调用 `soak.run()` 包装待测流程；`soak.measure()` 只返回数据不失败，适合无限滚动等会主动增长的流程。
- ⚙️ 建议配置独立 soak 项目，匹配 `*.soak.spec.ts`，使用 `soakLaunchOptions`，关闭 trace 和 video，并保留 `list` reporter；运行 `npx playwright test --project=soak`。
- 📊 失败报告会显示监听器、DOM 节点、堆内存趋势图与每轮增长斜率、R²，并通过堆快照对比指出泄漏引用链，例如 `window` 上未移除的 `onResize` 监听器。
- 🕒 可配置 `advanceMs` 匹配应用轮询周期；用 `waitForResponse` 等待每轮请求完成；支持 `page.routeWebSocket()`（Playwright 1.48+）和 `page.clock.runFor()` 处理计时器。
- 🔧 关键默认值：`passes=200`、`warmup=5`、`nodeThreshold=100`、`listenerThreshold=0`、时钟每轮 18 秒、`gcPasses=2`、`diagnose='on-failure'` 等；可通过 `soakOptions` 或 `run`/`measure` 第二参数覆盖。
- ⚠️ 限制：计数存在波动，建议夜间运行；使用 `workers: 1`、`retries: 0`；非 DOM 泄漏需设置 `heapThresholdPercent`；`contenteditable` 撤销历史和 `console.log` 对象可能干扰计数。
- 🧭 与 fuite、memlab 等外部工具相比，它直接嵌入现有 Playwright 测试，流程重复次数更多，并可利用虚拟时钟覆盖更长应用时间；仓库含示例应用、测试和覆盖率要求，采用 MIT 许可证。

---

### [GitHub - Lexington-Themes/astro-image-inspector · GitHub](https://github.com/Lexington-Themes/astro-image-inspector)

**原文标题**: [GitHub - Lexington-Themes/astro-image-inspector · GitHub](https://github.com/Lexington-Themes/astro-image-inspector)

`@lexingtonthemes/astro-image-inspector` 是一个 Astro 开发工具栏应用，用于在本地开发时悬停检查页面图片，显示图片实际尺寸、渲染尺寸、加载模式及常见警告；仅在运行 `astro dev` 时生效，不会出现在生产构建中。

- 🔍 主要功能：悬停任意 `<img>` 即可查看 natural（原始宽高）、rendered（显示宽高）、loading（lazy/eager/auto）和 warnings（警告信息）。
- 🛠️ 安装方式：使用 `npm install @lexingtonthemes/astro-image-inspector --save-dev` 安装为开发依赖。
- ⚙️ 配置方式：在 `astro.config.mjs` 的 `integrations` 中加入 `imageInspector()`。
- 🖱️ 使用流程：运行 `astro dev`，悬停页面底部显示 Dev Toolbar，点击 Image Inspector 图标开启检查，再悬停图片查看信息。
- 🖼️ 视觉反馈：检查器会高亮当前悬停图片，并默认在左下角显示小型信息面板。
- ⚠️ 常见警告：Upscaled（渲染尺寸大于原图）、Possibly oversized source（原图尺寸超过渲染尺寸 2 倍）、No width/height（缺少宽高属性）。
- 🧩 配置项：支持 `enabled`、`appName`；`showWarningsOnly`、`warnOnUpscale`、`warnOnOversized` 为预留选项。
- 📦 发布维护：维护者需在 `@lexingtonthemes` npm 组织下执行 `npm run build` 和 `npm publish`。
- 📄 许可证：MIT © Lexington Themes。
- ⭐ 仓库信息：14 stars、2 forks、6 commits。

---

### [订阅 Superhuman AI – 获取顶级 AI 新闻与工具 | Superhuman AI](https://www.superhuman.ai/subscribe?utm_source=wp_ads&utm_medium=Web+Tools+Weekly&utm_content=v2-r1047379-p1364312-c45336&transaction_id=102648b7706d42b6e2b70c1a7b2a28)

**原文标题**: [Subscribe to Superhuman AI – Get Top AI News & Tools | Superhuman AI](https://www.superhuman.ai/subscribe?utm_source=wp_ads&utm_medium=Web+Tools+Weekly&utm_content=v2-r1047379-p1364312-c45336&transaction_id=102648b7706d42b6e2b70c1a7b2a28)

这是 Superhuman AI 的订阅推广页面，主打“每天 3 分钟掌握 AI 工具、教程与资讯”，面向希望提升生产力和职业发展的读者，并提供免费订阅及资源入口。

- 🚀 定位：帮助用户每天仅用 3 分钟掌握 AI 工具、教程和新闻。
- 👥 规模：宣称已有超过 200 万读者加入。
- 📈 价值：学习如何利用 AI 提升工作效率、加速职业发展。
- 🆓 订阅：提供免费订阅入口。
- 🎁 资源：注册可获取 1,000+ 提示词、AI 课程和速查表。
- 📄 其他：页面包含隐私政策和使用条款链接。
- 🔁 说明：所给内容重复出现，核心信息为订阅推广，无更多实质文章内容。

---

### [Logos — 15,017 个免费 SVG 标志，适用于应用、开发工具和技术品牌](https://logos.lndev.me/)

**原文标题**: [Logos — 15,017 free SVG logos for apps, dev tools & tech brands](https://logos.lndev.me/)

该页面提供 15,017 个免费 SVG 标志，面向应用、开发工具和科技品牌，支持搜索、分类筛选、下载或一键复制，方便直接使用。

- 🎨 收录 15,017 个免费 SVG 标志，适用于应用、开发工具和科技品牌。
- 🔍 支持搜索和按 20 个类别筛选，并可清除筛选条件。
- ⬇️ 每个标志均可一键下载或复制，便于快速使用。
- 🧩 包含 13,072 个图标和 1,945 个文字标志。
- 🖼️ 图库需要启用 JavaScript 才能正常浏览。
- 📦 可在 GitHub 浏览全部 15,017 个标志，或下载完整资源包。
- 📄 每页可设置显示 50、100、250 或 500 个标志。

---

### [一键下载适用于 Windows、macOS 和 Linux 的 FFmpeg](https://ffmpegdownload.com/)

**原文标题**: [Download FFmpeg for Windows, macOS & Linux in one click](https://ffmpegdownload.com/)

该页面是一个 FFmpeg 预编译下载与安装指南，通过分步选择操作系统、架构、链接方式、许可证、版本和提供方来获取合适构建，并附带许可证、链接方式、版本说明、下载校验、构建检查和常用命令等参考信息。

- 🖥️ 支持 Windows、Linux、macOS，架构可选 x86_64、arm64、x86，下载器会自动匹配最佳构建。
- 🔗 链接方式分为 Static、Shared、Fully static：Static 将 libav* 打包进单个二进制；Shared 保留独立库文件；Fully static 还静态链接 glibc，适合嵌入式或精简系统。
- 📜 许可证有 GPL、LGPL、Non-free：GPL 要求源码开源；LGPL 可用于闭源项目；Non-free 分发通常需要付费商业许可。
- 🏷️ 版本遵循 MAJOR.MINOR.PATCH；MAJOR 有破坏性变更，MINOR 增加兼容功能，PATCH 仅修复缺陷，生产环境建议固定 MAJOR.MINOR 并让 PATCH 浮动。
- 🌿 Main 分支构建是未版本化快照，不同提供方构建时间和提交可能不同；需要可复现流水线时应固定版本化 URL。
- 📦 提供方包括 ffmpeg.org、BtbN-FFmpeg-Builds 和 Gyan Doshi；BtbN 流行于 Windows/Linux，Gyan 流行于 Windows，即使 FFmpeg 版本相同，编解码器和硬件加速支持也可能不同。
- ⬇️ 下载链接可能始终指向最新 Main 构建；页面还提供版本化下载、CI/CD 一行命令、`.sha256` 校验和 `.info` 版本与提交信息。
- ✅ 下载后可校验 SHA-256，并用 `ffmpeg -buildconf`、`-codecs`、`-encoders`、`-decoders`、`-hwaccels`、`-filters`、`-formats`、`-protocols` 检查构建能力。
- 🎞️ 页面给出首个示例命令：从样例视频前 60 秒生成 GIF 预览。
- 📚 还提供 FFmpeg 常用命令速查表，覆盖格式转换、裁剪、音频混合、跳剪、GIF、缩略图、Ken Burns 效果和 GPU 编码等。
- ⚖️ 页面强调许可证说明不构成法律建议，分发前应结合具体使用场景核实 GPL、LGPL 或 Non-free 合规性。

---

### [Mitos ASCII 工具](https://mitos.shared.oxide.computer/)

**原文标题**: [Mitos ASCII Tool](https://mitos.shared.oxide.computer/)

未收到可总结的文章内容，因此暂时无法提取要点；请粘贴需要总结的原文。

- 📄 当前输入为空，无法生成文章摘要。
- ✍️ 请提供原文内容，我将按“概述 + 要点列表”的格式输出中文总结。
- 🧾 要点将使用“-”符号，并为每条搭配合适的表情符号。

---

### [让你的标志比白色更亮](https://www.soverybright.com/)

**原文标题**: [Make your logo brighter than white](https://www.soverybright.com/)

该在线工具可将 Logo 转换为 HDR JPEG，让指定颜色在 HDR 屏幕上比纯白更亮；上传、选色、下载即可，文件在普通设备上仍是正常 JPEG，且免费、不存储。

- 🖼️ 支持 PNG、JPEG、WebP，拖拽或点击上传；图像仅在内存中处理，不会存储。
- ✨ 选定颜色在 HDR 屏幕上最高可达 #FFFFFF 的 7.5 倍亮度，普通屏幕上则显示为正常 JPEG。
- 📦 Web 端使用 ISO 21496-1 gain-map JPEG：附加一张微型灰度图，告诉 HDR 软件每个像素可增亮多少，基础像素不变。
- 💼 LinkedIn 版本使用 BT.2100 PQ 像素和匹配 ICC 配置，LinkedIn 会保留该 HDR 信息。
- 🎨 示例包括白色字标、白色圆环加品牌蓝、深色背景上的奶油色贴纸文字；浅色、近白元素最适合发光。
- 🔆 最佳效果是深色背景上的浅色元素，约 +2.9 档、约 1500 尼特；深色本身很难发光，强行提亮会像霓虹发白。
- ⚠️ HDR 效果仅在支持 gain map/PQ 的 HDR 显示器和软件中显示，如 Chrome、Safari 26、Apple Photos、LinkedIn 应用；其他平台可能剥离或归一化，但文件仍正常。
- 🔤 文字也能“比白更亮”：CSS 暂不能直接写超过 #FFFFFF 的颜色，可用 background-clip: text 让文字透出 HDR 图像。
- 📱 通过 @media (dynamic-range: high) 仅在 HDR 屏幕启用图像文字方案，SDR、Firefox 和打印环境回退为真实白色，避免裁剪和兼容问题。
- 🧩 适合标题和强调文字，不适合整段正文；1500 尼特长段落会刺眼，并建议为 ::selection 设置可见颜色。
- 🚫 filter: brightness() 无法让 CSS 颜色超过白色；只有 HDR 内容才能获得额外亮度空间。
- 👤 工具由 Chris Bennett 制作，并提供 64×64 白色 JPEG 光斑示例及 1.3 KB 的 white-7.5x.jpg 下载。

---

### [在浏览器中转换图片、视频、音频、PDF — ConvertYard](https://convertyard.com/)

**原文标题**: [Convert Images, Video, Audio, PDF in Browser — ConvertYard](https://convertyard.com/)

ConvertYard 是一个免费的浏览器本地文件转换工具，强调文件永不离开电脑：无需上传、无需账号、无水印，支持图片、PDF、视频和音频等批量处理，依靠 WebAssembly 在设备上完成转换。

- 🔒 **隐私优先**：所有处理都在浏览器本地运行，文件不会上传到服务器，也不会被存储。
- ⚙️ **本地技术**：通过 WebAssembly 在浏览器中运行类似桌面端的 libvips、ffmpeg、pdf-lib 等代码。
- 📦 **批量处理**：每批最多支持 1,000+ 个文件，可单独下载或打包为 ZIP。
- 🖼️ **工具丰富**：提供 152 个工具，涵盖图片转换、压缩、缩放、背景移除、PDF 合并/压缩/转 JPG、MP4 转 MP3、JSON 格式化、Alt 文本生成等。
- 🚀 **使用简单**：拖入文件 → 浏览器内转换 → 下载结果，无需注册、无转换限制、无输出水印。
- 🆚 **对比优势**：相比 Smallpdf、iLovePDF、CloudConvert，不上传文件、批量更大、通常无需账号、首次加载后可离线使用、无广告打断转换流程。
- 💻 **适用人群**：适合摄影师批量处理照片、开发者提升工作流效率，以及处理合同、医疗记录、财务文件等敏感资料。
- ⚠️ **使用限制**：文件大小主要取决于设备内存，多数浏览器约可处理 2GB；实际批量速度取决于 CPU 和显卡性能。
- 💰 **免费模式**：网站使用 Google Analytics 并可能展示广告，但广告和统计不会接触用户文件；工具本身免费、无需登录。

---

### [免费 SVG 图标 - 搜索](https://svgicons.com/)

**原文标题**: [Free SVG Icons - Search 312K+ Open-Source Icons - Svg/icons](https://svgicons.com/)

您尚未提供需要总结的文本，因此目前无法生成摘要。请发送文章内容，我会按要求整理成中文要点列表。

- 📄 请提供需要总结的文章或文本内容。
- ✨ 收到内容后，我将生成简洁的中文要点，并为每条要点配上合适的表情符号。

---

### [GitHub - yossdotpro/removerized：完全在浏览器中运行的 AI 图像工具包——免费、私密、离线优先。 · GitHub](https://github.com/yossdotpro/removerized)

**原文标题**: [GitHub - yossdotpro/removerized: AI Image Toolkit that runs fully in your browser — free, private, and offline-first. · GitHub](https://github.com/yossdotpro/removerized)

Removerized 是一个开源、本地优先的 AI 图像工具包，完全在浏览器中运行，基于 ONNX Runtime Web，实现免上传、无服务器、无限制的图像处理，强调隐私、免费与离线优先。

- 🖼️ 项目定位：AI 图像工具包，所有处理均在用户设备本地完成，不上传数据。
- ⭐ 仓库热度：GitHub 公共仓库，约 1.6k stars、164 forks、8 watchers、232 次提交。
- 🧠 核心功能：支持多 AI 模型选择、背景移除、图像放大、批量处理、模型缓存和高级输出控制。
- ⚡ 技术机制：模型直接在浏览器加载，使用 WebAssembly 推理，并通过 IndexedDB 缓存资源。
- 🔌 隐私与离线：首次加载后可离线使用，零后端、零数据收集，数据不离开设备。
- 🎯 项目理念：AI 工具应快速、私密且人人可用，注重隐私优先、本地性能和开发者友好实验。
- 🛠️ 快速开始：使用 `yarn install` 安装依赖，`yarn dev` 启动开发环境。
- 📌 路线图：计划加入图像上色、照片修复、图像转 Alt 文本、高级蒙版编辑、PWA 和浏览器扩展。
- 🤝 贡献规则：欢迎 issue 和 PR；提交 PR 即同意原创声明、GPLv3 许可及向维护者授予额外再许可权利。
- ⚖️ 许可证：项目采用 GPL-3.0 许可证，由 Yoannis Sánchez Soto（@yossdotpro）维护。

---

### [GitHub - CristianOlivera1/openvid: Create professional demos and 3D mockups in seconds, directly in your browser · GitHub](https://github.com/CristianOlivera1/openvid)

**原文标题**: [GitHub - CristianOlivera1/openvid: Create professional demos and 3D mockups in seconds, directly in your browser · GitHub](https://github.com/CristianOlivera1/openvid)

OpenVid 是一个开源、基于浏览器的视频演示与 3D 样机制作工具；用户可录制或上传视频，添加缩放、设备样机和 3D 效果，并导出电影级演示。仓库当前约有 2.9k stars 和 421 forks。

- 🎬 定位：直接在浏览器中快速创建专业演示和 3D 样机，无需安装。
- 📥 视频输入：支持浏览器屏幕录制，以及上传 MP4、WebM、QuickTime、MKV。
- 🧩 样机与 3D：可将样机应用到图片，并进行 3D 变换。
- 🎨 视觉定制：提供 100+ 预设背景，支持自定义图片、Unsplash、纯色与渐变。
- ✍️ 画布元素：支持矩形、圆形、三角形、文字、SVG，以及 PNG/JPG/WebP 图片叠加。
- 🔍 动态效果：可按时间线缩放，控制速度与缓动，并基于兴趣点实现 3D 相机倾斜和旋转。
- 🎵 音频：支持多轨音频，并按视频时长自动裁剪。
- 📤 导出：支持 4K、2K、1080p、720p、480p；格式包括 MP4（H.264）、WebM（VP9，支持透明背景）、GIF、PNG、WEBP、JPG、AVIF。
- ⚙️ 技术栈：使用 FFmpeg.wasm、Canvas API、MediaBunny、Three.js、HTML to Image；本地采用 IndexedDB、LocalStorage，Supabase 云备份即将推出。
- 🚀 快速开始：运行 pnpm install，复制 .env.example 并配置 Supabase，再运行 pnpm dev，访问 localhost:3000。
- 🤝 社区：欢迎贡献，可通过 Discord 协作；仓库已有约 2.9k stars、421 forks。

---

### [联系网络工具周刊](https://webtoolsweekly.com/contact?opt=classifieds)

**原文标题**: [Contact Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

本页面向希望在 Web Tools Weekly 投放广告的用户，提供广告方案查看、可用性咨询和预订联系渠道；广告咨询表单仅用于广告相关事宜，一般咨询或工具投稿需通过其他方式联系。

- 📢 想了解 Web Tools Weekly 的广告投放选项，可先查看“Advertising Plans”页面。
- ✉️ 如需询问当前广告位是否可用，请发送消息联系。
- 📝 若要讨论具体广告选项或预订广告位，请填写页面底部表单。
- ⚠️ 该表单仅用于广告咨询，不处理一般咨询或工具投稿。
- 💬 一般咨询、工具投稿可通过 X 私信、Bluesky 聊天，或回复订阅邮件联系。
- 📋 广告表单需填写姓名、邮箱、广告链接、期望广告方案及备注/说明。
- 📌 广告方案选项包括：顶部广告+顶部文字链接、付费产品评测、中部图片广告、文字链接组合、分类广告、广告互换。

---

### [面向游戏资产的 AI 像素艺术生成器与编辑器 | Sprite Fusion](https://www.spritefusion.com/pixel-art-generator)

**原文标题**: [AI Pixel Art Generator & Editor for Game Assets | Sprite Fusion](https://www.spritefusion.com/pixel-art-generator)

Sprite Fusion 是一款面向游戏开发的 AI 像素艺术生成器，主打通过文本提示快速产出可商用的精灵、图标、精灵表和动画，并以精确尺寸、固定色板、风格参考、8 方向生成、内置编辑器及 Unity/Godot 集成服务独立开发者与工作室。它还提供 API 与 AI Agent 接入、免费法线贴图生成，以及 Tilemap Editor、Pixel Snapper 等配套工具，定价从每月 $9 起。

- 🎯 定位：AI 像素艺术生成器，可在几分钟内创建游戏用 sprites、icons 和 animations，覆盖独立项目到工作室管线。
- ⏱️ 解决痛点：传统像素艺术学习周期长、每个资产耗时数小时，免费素材包还容易让游戏外观同质化。
- 🧭 三步流程：描述创意 → 生成独特资产 → 一键导出到 Unity、Godot、GameMaker 或其他游戏引擎。
- 📏 精确控制：支持 16×16 至 128×128 的原生尺寸输出，可使用 PICO-8、Game Boy 或自定义色板。
- 🎨 风格一致：可用一张 sprite 作为风格参考生成新资产；也能用提示词编辑现有像素画并保留原有风格。
- 🔄 资产生成：覆盖角色、道具、敌人、UI 图标等，并支持皮肤/姿态变体、8 方向精灵、行走/攻击/待机动画及 sprite sheets。
- 🧩 编辑器与导入：内置浏览器像素编辑器，可手绘、修正、导入外部或素材包 sprite 后继续编辑、动画化和导出；支持透明背景。
- 🔌 集成能力：提供原生 Unity/Godot 插件；API 支持生成、编辑、风格匹配、8 方向、动画和法线贴图；可接入 Claude Code、Codex 等 AI agents。
- 🧱 附加工具：Tilemap Editor 支持导入任意 tileset、自动铺砖与碰撞层、多引擎导出；Pixel Snapper 可清理模糊或离网格像素并批量处理。
- 💡 技术亮点：使用自研 in-house 模型生成“真像素艺术”而非普通图片滤镜；法线贴图可免费生成，生成器已在 GitHub 开源。
- 💰 定价：Starter $9/月含 450 credits；Creator $19/月含 1,050 credits（最受欢迎）；Pro $49/月含 3,000 credits；支持商业使用及月/年付费。
- 🌐 社区与资源：提供社区作品画廊、Discord、GitHub、文档和教程；FAQ 涵盖标签管理、API、AI agents、导入导出与法线贴图等。
- ⚖️ 使用边界：核心聚焦 text-to-pixel-art 资产工作流，不是主要的照片转像素画工具；背景/场景可生成，但主要优化单个游戏资产。

---

### [内置分析功能的 JavaScript 数据网格 | Lattice Grid](https://www.latticegrid.dev/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=lg_launch_2026q3&utm_content=text_ad_w35)

**原文标题**: [JavaScript Data Grid With Built-In Analysis | Lattice Grid](https://www.latticegrid.dev/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=lg_launch_2026q3&utm_content=text_ad_w35)

该产品以高性能数据网格为核心，可在同一份实时数据上构建数据驱动应用，并内置统计分析、仪表盘、Gantt、Kanban、日历、调度器和表单等视图，由数据路由引擎统一驱动。单一许可证覆盖全部组件，localhost 免费，商业使用按域名收费。

- 🧱 以高性能数据网格为基础，用于构建数据驱动应用。
- 📊 内置仪表盘、Gantt、Kanban、日历、调度器和表单，并共享同一份实时数据。
- 🧮 Grid 支持分组比较、解释数值、聚类行和派生网格，筛选后结果会实时重算。
- 📈 Dashboards 提供 KPI 卡片、图表和地图；Gantt 支持依赖、关键路径和资源负载。
- 🗂️ Kanban 与数据行联动，拖动卡片即更新行；Calendar 支持按日期列拖拽改期。
- 👥 Scheduler 分配人员和机器，并标记过度分配；Forms 提供表单、记录编辑器和应用外壳。
- 🚦 Data Router 可将一个实时数据流分区，驱动多个联动视图，无需为每个面板单独连接。
- 🧪 演示包含 5000 条云端成本数据，全部在浏览器运行，筛选后派生、比较、解释和聚类实时更新。
- 💻 支持 JavaScript、React、Vue、Svelte、Angular、Web Component、htmx 和 Python。
- 💳 一个许可证覆盖全部组件：每域名 $1,000，无限开发者，一年支持；localhost 免费。
- 🏷️ 测试、预览和 CI 可用带小水印的完整版；个人、教学或开源项目可申请非商业密钥；商业发布需按域名购买许可证。

---

### [视频转视频 AI | 用提示词变换视频风格](https://videotovideoai.online/)

**原文标题**: [Video to Video AI | Transform Video Style with Prompts](https://videotovideoai.online/)

视频到视频 AI 可让用户上传短片并描述改造方向，生成私密的 720p/1080p 变体；源片提供运动、时序与构图引导，适合风格迁移、场景/氛围替换、角色引导和社交短片创作，但结果并非逐帧完全复制。

- 🎥 上传源视频：支持 MP4/MOV，时长 3–15 秒，短边 480–720p，文件 ≤50 MB；清晰主体、稳定构图和可读动作更易获得好评。
- ✍️ 在工作台选择任务并编辑提示词，说明“要改变什么”和“要保留什么”；可选参考图引导角色外观。
- 🖼️ 参考图支持 JPG/PNG/WebP，≤10 MB；运动迁移通常需要动作视频加角色图。
- 🎨 支持整场景风格迁移，如动漫、3D、水彩、漫画、像素、电影感等，也可调整地点、季节、时间、光线与氛围。
- 🧑 可通过一张角色图指导新角色外观，源片负责表演和动作；适合角色研究与角色替换。
- ⚙️ 可设置输出 720p/1080p、5/10/15 秒时长、画幅比例（Auto、16:9、9:16、1:1、4:3、3:4、21:9）及创意程度。
- 🔊 新音频为生成音频且默认关闭，不保留原始音轨；Kling Motion 不提供该选项。
- 👀 结果为私密变体，可预览、与源片对比、下载 MP4，或从历史记录重新打开；历史变体保留。
- 🧭 三步流程：上传短片 → 描述改造并设置参数 → 预览、对比并下载。
- 💡 建议一次只做一个聚焦改动；提示词先写风格，再写主体、场景、色彩和需保留内容，便于评估。
- ⚠️ 不保证动作、身份、面部、细节、时序和构图完全一致；“Continue shot”生成独立续接片段，不会自动拼接原文件。
- 💳 生成成本最高 225 credits，按具体设置而定；示例模型 Kling 3.0 标称最快、最低成本。
- 📱 适用场景包括社交短片、场景概念、角色研究、电影与氛围测试。

---

### [Insight Cat - 全栈监控](https://insightcat.com/)

**原文标题**: [Insight Cat - Full-stack monitoring](https://insightcat.com/)

InsightCat 提供全栈监控解决方案，可深度观察各类基础设施，通过简单集成快速接入，并借助智能告警与实时洞察帮助企业预防宕机、提升可观测性。

- 🔍 提供全栈监控，深入查看每个细节，体验简单顺畅。
- 🔌 通过数百种简单集成监控负载均衡器、数据库、云、无服务器等。
- ⚙️ 支持自带基础设施，无需重大变更，几分钟内即可部署 InsightCat。
- 📈 Prometheus：将 InsightCat 服务器添加为 remote_write 目标，零配置获得强大可视化。
- 📝 Telegraf：在 telegraf.conf 中添加一行，即可获得实时洞察和智能告警。
- 🧩 InsightCat 客户端：开源，支持动态清单、更快指标传输、日志、APM 等。
- 🚨 智能告警与升级：及时通知团队，避免错过事件。
- ⏱️ 实时洞察：通过预防避免停机。
- 🌍 全球企业采用全栈监控以预防停机并获得更好的可观测性。
- 🚀 几分钟内即可开始全栈监控，并提供免费试用。

---

### [问卷与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=web-tools&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=web-tools&utm_medium=email)

SurveyJS 是一套用于在 Web 应用中构建调查问卷与表单管理的 JavaScript 组件库，强调数据自主可控、可自托管、无使用限制，并提供从表单渲染、拖拽创建、数据看板到 PDF 导出的完整能力，适合需要隐私合规与深度定制的企业应用。

- 🧩 四大组件：Form Library 渲染动态交互表单；Survey Creator 拖拽生成 JSON 表单结构；Dashboard 用图表和表格分析响应；PDF Generator 导出可编辑或预填 PDF。
- 🔐 数据自主：表单与响应存入自有数据库，支持自托管，避免第三方 SaaS 锁定，便于满足 HIPAA、FERPA、GDPR 等合规与隐私要求。
- ♾️ 无使用限制：不限表单数量、受访者、提交量、文件上传、管理员数量与功能使用。
- 🧱 高可定制：支持自定义及复合题型，可集成 Angular、React、Vue 3 组件，并可通过主题适配 Bootstrap、Material UI、shadcn/ui。
- ♿ 可访问性：Form Library 与 Survey Creator 符合 WCAG、Section 508、ARIA 标准，支持键盘导航与屏幕阅读器，并经 Axe 验证。
- 📴 离线收集：问卷、主题和响应可本地存储，联网后自动同步，适合离线优先场景。
- ✅ 数据验证：除内置客户端验证外，支持自定义客户端规则与服务端校验、事件处理。
- 🎨 白标与一致设计：各组件共享设计令牌和主题系统，便于匹配现有产品设计。
- 🤖 AI 辅助：可通过 API 集成自然语言生成表单、翻译和智能内容建议。
- 🏢 行业适用：保险、医疗、市场研究、教育、HR、电商、客户体验、非营利、银行等可自托管收集敏感数据。
- 💳 许可模式：Survey Creator、PDF Generator、Dashboard 采用一次性开发者许可，可永久使用；含 12 个月维护与支持，后续可续订。
- 🖥️ 前后端边界：SurveyJS 只负责前端 UI，不存储、访问或跟踪数据；后端、数据库、用户管理与审批流程需自行实现或对接。
- ⭐ 用户反馈：评价集中在灵活易用、支持多种 JS 框架、复杂条件逻辑、开源以及支持响应快。

---

### [Kobbe：尊重访客的网站分析](https://kobbe.io/)

**原文标题**: [Kobbe: Web analytics that respect your visitors](https://kobbe.io/)

Kobbe 是面向创始人和小团队的隐私优先、收入导向型网站分析工具，可查看访问者、阅读内容与页面收益，并将销售归因到来源页面；它强调无 Cookie、无横幅、过滤机器人，且所有套餐功能一致，仅按事件量收费。

- 👀 **核心定位**：帮助小团队看清谁在访问、读了什么、带来了多少收入，并把 Stripe、Polar、Paddle 等平台的销售追溯到具体页面和来源。
- 🤖 **机器人过滤**：每次访问经过七项检查，过滤无头浏览器、数据中心流量和引荐垃圾；VPN 用户仍会计入。
- 💰 **收入归因**：按页面、来源和活动查看毛收入、净收入与归因收入，支持 Stripe、Polar、Paddle、Shopify 等。
- 🍪 **无 Cookie 分析**：默认不跟踪个人、不存个人数据，尊重 Global Privacy Control 和 Do Not Track，通常无需 Cookie 横幅，并提供 DPA。
- ⚙️ **快速安装**：一个约 2.5 KB 的脚本标签即可开始，使用 defer 加载；完整版约 5 KB，支持 22 个平台安装指南。
- 📥 **历史数据导入**：可从 Google Analytics、Plausible、PostHog、Fathom、Umami、Matomo 等 13 个工具导入历史流量，默认不覆盖已有 Kobbe 数据。
- 📊 **完整功能**：实时访客、漏斗、Core Web Vitals、Search Console、错误跟踪、流量提醒、共享仪表板、数据导出、AI 代理与 CLI 等。
- 🧠 **AI 代理接入**：通过 Kobbe CLI 的 MCP 服务器连接 Cursor、Claude 等 MCP 兼容代理，可读取流量、收入、漏斗和活动，或设置目标与漏斗；令牌有权限范围，危险操作需输入确认。
- 💵 **统一定价**：所有套餐功能相同，仅按月事件量收费，无企业版或功能分级；价格从 100K 事件 $9/月到 10M 事件 $169/月不等。
- 🎁 **免费试用**：15 天免费试用，无需信用卡；试用后按所选套餐计费，可随时升级、降级或取消。
- 📈 **超限规则**：达到月度事件上限后，Kobbe 会停止接收新分析事件，直到下月重置或升级套餐。
- 🔐 **GDPR 友好**：默认无 Cookie、应用数据库不存原始 IP、不建立持久访客画像，并提供托管服务 DPA；网站方仍需负责隐私声明、合法性基础及必要同意。
- 🚀 **适用性**：只要能添加脚本标签即可使用，支持 WordPress、Shopify、Webflow、Framer、Next.js、Astro、Google Tag Manager 等；官方强调不会明显拖慢网站。

---

### [面向开发者的电子邮件 API · Pigeon](https://pigeonfs.com/)

**原文标题**: [Email API for developers · Pigeon](https://pigeonfs.com/)

Pigeon 是面向开发者的邮件 API 与通讯订阅平台，用于让应用自动发送欢迎、密码重置、收据、邀请等邮件，并提供域名验证、发送日志、新闻通讯和收件功能。

- 📧 定位为开发者邮件 API，发送应用“欠用户”的自动邮件，如注册欢迎、密码重置、付款收据和邀请。
- ⚡ 迁移成本低，约 5 分钟即可切换；保留 from、to、subject、html 字段，支持 Node、Python、Go、Java、Rust、Elixir 和 SMTP。
- 💳 免费起步每月 3,500 封且无需信用卡；每月 50,000 封对应 20 美元套餐；Postmark 付费方案含 10,000 封后按千封计费。
- 🛠️ 三步接入：添加域名 DNS 记录并验证、在应用中配置发送密钥、从产品发送邮件，仪表盘会记录每次调用。
- 📰 新闻通讯：创建通讯并设置已验证域名的发件地址，分享订阅页，仅确认订阅者收到下一期，可在仪表盘撰写或通过 API 发布。
- 📥 收件功能：验证域名后创建地址，将 MX 记录指向 pigeonfs.com，仅接受已创建地址，主题和正文加密存储并在 Incoming 中读取。
- 🤖 支持 Grok MCP：配置 Pigeon MCP server 后，可让 Grok 验证域名、创建新闻通讯并返回订阅页链接。
- 🔌 API 示例：POST /api/newsletters 传入 name 和 from，返回的 url 即订阅页；发布 issue 需要第二次调用。
- 🔐 核心保障：从已验证域名发信、一个 API 或 SMTP 登录、提供日志与套餐限额，让退信或发送限制在用户反馈前可见。
- 🚀 建议先在自己的域名上发送第一封欢迎邮件，再邀请其他人使用。

---

### [Matt Pocock 在 X 上：“这个平台上的 AI 回复糟糕得惊人

我不再像以前那样查看通知——不再为有趣的讨论而兴奋，](https://x.com/mattpocockuk/status/2116925366669312413)

**原文标题**: [Matt Pocock on X: "AI replies on this platform are astonishingly bad

I don't check my notifications how I used to - excited by interesting discussions, like a conference hallway track

Instead, I search for profile pictures of people I know aren't bots

They are getting harder and harder to spot" / X](https://x.com/mattpocockuk/status/2116925366669312413)

概览：Matt Pocock 批评该平台上的 AI 回复质量极差，并表示机器人内容正在改变他查看通知和参与讨论的方式。

- 🤖 Matt Pocock 认为该平台上的 AI 回复“差得惊人”。
- 🔔 他不再像以前那样频繁查看通知，也不再期待通过通知参与有趣的讨论，并把过去的感觉比作会议走廊里的交流。
- 🔍 现在，他会主动寻找自己认识且确定不是机器人的人的头像，以此筛选互动对象。
- 😕 他指出，这些机器人账号越来越难以辨认。
- 📊 该帖子获得约 5.61 万次浏览，以及 146 条回复、12 次转发、619 次点赞和 38 次收藏。

---

### [路易斯·拉扎里斯 (@LouisLazaris) / X](https://x.com/LouisLazaris)

**原文标题**: [Louis Lazaris (@LouisLazaris) / X](https://x.com/LouisLazaris)

这是 Louis Lazaris 的社交媒体个人资料页概览，主要展示其身份、简介、账号数据和内容分区。
- 👤 姓名为 Louis Lazaris，账号为 @LouisLazarris，自我简介是“Chairman of the Bored.”
- 📰 创始人身份：创办了两份科技类通讯，分别是 webtoolsweekly.com 和 techproductivity.co。
- 💼 职业标签包括 Entrepreneur，个人链接为 bio.link/louislazaris。
- 🌍 所在地显示为“Torontocisco, Canadafornia”，个人网站为 impressivewebs.com。
- 📊 账号数据：5,307 条帖子、717 个关注、5,479 个粉丝。
- 📅 加入时间为 2009 年 5 月。
- 🗂️ 页面内容分区包括 Posts、Replies、Reposts 和 Media，当前展示的是其帖子内容。

---

### [Bluesky 上的 @louislazaris.com](https://bsky.app/profile/louislazaris.com)

**原文标题**: [@louislazaris.com on Bluesky](https://bsky.app/profile/louislazaris.com)

这是 Louis Lazaris 的 Bluesky 个人资料简介，介绍其前端开发者与 newsletter 策划者身份，并列出个人网站及多个项目链接。

- 👤 姓名：Louis Lazaris；个人网站：louislazaris.com；Bluesky DID：did:plc:6if43vohxmohxuooa7bkkw5q
- 💼 身份：前端开发者、newsletter 策划/编辑者
- ⚙️ Web Tools Weekly：https://webtoolsweekly.com
- 📈 Tech Productivity：https://techproductivity.co
- 💻 VS Code newsletter：https://vscode.email
- 👨‍💻 个人主页：https://louislazaris.com
- 🎸 吉他相关 YouTube 频道：youtube.com/@tunejotter
- 🌐 使用 Bluesky 需启用 JavaScript；了解更多可访问 bsky.social 和 atproto.com

---

### [向 Web Tools Weekly 提交工具](https://webtoolsweekly.com/submit)

**原文标题**: [Submit a Tool to Web Tools Weekly](https://webtoolsweekly.com/submit)

本文介绍了推荐前端开发相关工具的提交渠道与范围：可通过 X 或 Bluesky 提交实用工具，但不接收文章或教程，生产力相关工具则归入另一份简报。

- 📥 如果你开发或发现了对前端开发者有用的工具，可通过 X 或 Bluesky 提交。
- 🗓️ X 私信每周一、周二开放：@LouisLazaris；Bluesky 聊天开放：@LouisLazaris.com。
- 🛠️ 可提交内容包括：库、框架、插件、脚本、Web 应用、桌面应用、移动应用、API/服务、编辑器/IDE，以及其他对 Web 开发者、程序员或设计师有用的工具。
- 🚫 请勿提交文章或教程，此类内容不会被收录。
- 📈 生产力相关工具已移至另一份简报 Tech Productivity，也可通过上述方式提交。

---

### [HaxxorWPM](https://haxxorwpm.0s.is/)

**原文标题**: [HaxxorWPM](https://haxxorwpm.0s.is/)

HaxxorWPM 是一个用于测试终端命令输入速度的新工具，提供限时打字测试、运行统计与排行榜等功能。

- ⌨️ 核心功能：测试终端命令输入速度（terminal-fu）
- ⏱️ 计时模式：默认 60 秒，可选 30s、60s、120s
- 📊 实时指标：显示 WPM、准确率、命令数和错误数
- 🚀 开始方式：开始输入后即启动测试
- 💻 示例命令：grep -R "error" logs、systemctl status nginx、git pull --rebase、docker compose up -d
- 📈 运行结果：展示 WPM、准确率、Raw WPM、命令数，并支持保存运行
- 🏆 附加功能：排行榜、刷新、布局与键盘设置
- 🕘 最近运行：显示“Last run”和“Balanced run”等统计信息

---

### [Web 工具周刊 | 面向前端开发者的每周通讯](https://webtoolsweekly.com/)

**原文标题**: [Web Tools Weekly | A Weekly Newsletter for Front-end Developers](https://webtoolsweekly.com/)

Web Tools Weekly 是一份面向 Web/前端开发者的每周邮件通讯，拥有约 15,910 名订阅者，主要分享新工具、前端库和 JavaScript 技巧；订阅需同意相关条款与隐私政策，页面还展示了大量读者的积极评价。

- 📧 每周发送一封邮件，承诺无垃圾邮件，订阅即表示同意接收 Web Tools Weekly 邮件。
- 🛠️ 内容聚焦 Web 开发工具、前端库和 JS 技巧，帮助开发者及时了解新资源。
- 👥 页面显示已有 15,910 名订阅者。
- 🔐 订阅涉及 EmailOctopus 的数据存储与追踪，并使用 reCAPTCHA，需遵守相应隐私政策与条款。
- ⭐ 读者评价普遍正面，称其为优秀甚至最佳技术通讯之一，实用性强。
- 🔍 多位读者表示通过该通讯发现新工具、长期订阅并获得实际价值，且期待每期内容。

---

