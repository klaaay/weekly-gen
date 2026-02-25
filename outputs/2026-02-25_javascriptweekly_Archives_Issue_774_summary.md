### [JavaScript周刊第774期：2026年2月24日](https://javascriptweekly.com/issues/774)

**原文标题**: [JavaScript Weekly Issue 774: February 24, 2026](https://javascriptweekly.com/issues/774)

本期JavaScript周刊涵盖了多个重要更新和工具发布，包括Oxfmt代码格式化器的Beta版、Vuetify 4.0发布、Firefox支持Service Worker中的JS模块，以及内存优化和前端工具链的改进等内容。

- 🚀 **Oxfmt Beta发布**：基于Rust的JavaScript代码格式化器，兼容Prettier，速度提升显著，支持JSX、Tailwind CSS排序等功能。
- 📊 **FlexGrid数据网格更新**：Wijmo推出的高性能JavaScript DataGrid，支持虚拟化渲染，并可扩展至Angular、React和Vue框架。
- 🎨 **前端工具链优化**：Christoph推荐快速JavaScript工具栈，强调提升开发效率，并提供Markdown版本供LLM处理。
- 🔒 **增强XSS防护**：Firefox v148支持Sanitizer API，推荐使用`setHTML`替代`innerHTML`，提升默认安全性。
- 💾 **Node.js内存优化**：通过V8指针压缩技术，`node-caged`Docker镜像可减少高达50%的内存使用。
- 🛠️ **重要版本发布**：包括Vuetify 4.0、npm v11.10.0、Node.js v25.7.0/LTS v24.14.0、ESLint 10.0.2等。
- 📸 **OpenSeadragon 6.0发布**：高效的高分辨率图像Web查看器，新增异步和缓存管理管道，提升大规模处理性能。
- 📈 **SurveyJS动态表单库**：支持React/Angular/Vue的JSON驱动表单构建工具，保障数据所有权。
- ⏳ **Slowmo调试工具**：可调整浏览器中时间流速的库或扩展，用于调试CSS动画和JavaScript定时任务。
- 🩺 **React Doctor代码检查工具**：扫描React代码库并给出健康评分，Angular版本也已推出。

---

### [Oxfmt Beta | JavaScript 氧化编译器](https://oxc.rs/blog/2026-02-24-oxfmt-beta)

**原文标题**: [Oxfmt Beta | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2026-02-24-oxfmt-beta)

Oxfmt 已进入 Beta 阶段，这是一款基于 Rust 构建、兼容 Prettier 的代码格式化工具，专为 JavaScript 生态系统设计，在保持与现代工具链完全兼容的同时，显著提升了性能表现。

- 🚀 Oxfmt 在无缓存初始运行中比 Prettier 快 30 倍以上，比 Biome 快 3 倍
- 📁 支持 JavaScript、TypeScript、JSON、YAML、HTML、CSS、Markdown 等广泛文件格式
- 🔄 提供 100% 的 Prettier 兼容性，可通过迁移命令轻松从 Prettier 切换
- 🎨 内置 Tailwind CSS 类排序和导入排序功能
- ⚙️ 新增程序化 Node.js API 和增强的 CLI 选项
- 📈 已被 Vue.js、Turborepo、Hugging Face 等多个知名项目采用
- 🔧 支持所有主流编辑器，包括 VS Code、IntelliJ 和 Neovim
- 🗺️ 未来路线图包括 Prettier 插件支持和进一步性能优化

---

### [Prettier · 固执己见的代码格式化工具 · Prettier](https://prettier.io/)

**原文标题**: [Prettier · Opinionated Code Formatter · Prettier](https://prettier.io/)

Prettier 是一款流行的代码格式化工具，支持多种编程语言和编辑器集成，旨在通过自动格式化提升代码一致性和开发效率。

- 🛠️ 一个固执己见的代码格式化工具，支持 JavaScript、TypeScript、CSS、HTML 等多种语言
- 🔌 可与大多数主流编辑器（如 VS Code、WebStorm、Vim 等）无缝集成
- ⏱️ 保存时自动格式化代码，节省团队讨论代码风格的时间
- 🌐 被超过 83% 的 State of JS 2021 受访者使用，拥有广泛的社区和生态系统支持
- 📦 在 GitHub 上有超过 990 万个依赖仓库，npm 上有超过 1.94 万个依赖包

---

### [Oxlint v1.0 稳定版 | JavaScript 氧化编译器](https://oxc.rs/blog/2025-06-10-oxlint-stable.html)

**原文标题**: [Oxlint v1.0 Stable | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2025-06-10-oxlint-stable.html)

Oxlint 1.0 稳定版正式发布，这是一款基于 Rust 构建的 JavaScript 和 TypeScript 代码检查工具，以其卓越的性能和易用性著称，已获多家大型企业采用。

- 🚀 **性能大幅提升**：相比 ESLint 有 50~100 倍的性能提升，在大型代码库中显著减少 CI 时间与成本。
- 🏢 **企业级应用**：已被 Shopify、Airbnb、梅赛德斯-奔驰等公司以及 Bun、Preact 等大型开源项目采用。
- ⚡ **快速上手**：无需配置即可运行，支持 npm、pnpm、yarn、bun、deno 等多种包管理器。
- ⚙️ **灵活配置**：支持通过 `.oxlintrc.json` 文件进行配置，兼容 ESLint 扁平配置，便于迁移和团队协作。
- 📚 **规则覆盖全面**：包含超过 500 条规则，涵盖 ESLint 核心、TypeScript 及多个流行插件，并拥有独家规则。
- 🔧 **编辑器集成**：提供 VS Code、IntelliJ IDEA、WebStorm、Zed 等编辑器的官方扩展及语言服务器协议支持。
- 🛣️ **持续发展路线图**：未来计划支持自定义规则、进一步性能优化及更精细的配置功能。
- 👥 **活跃社区**：拥有超过 200 位贡献者，欢迎通过 Discord、GitHub 等渠道加入社区并提供反馈。

---

### [生物群落，网络工具链](https://biomejs.dev/)

**原文标题**: [Biome, toolchain of the web](https://biomejs.dev/)

Biome v2.4 是一款专为 Web 项目设计的快速、一体化工具链，集代码格式化、代码检查等功能于一身，旨在提升开发效率。

- 🚀 **快速格式化**：支持 JavaScript、TypeScript、JSX、TSX、JSON、HTML、CSS 和 GraphQL，与 Prettier 兼容性达 97%，格式化速度显著更快。
- 🛠️ **智能代码检查**：包含 451 条规则，源自 ESLint 等工具，提供详细诊断和可自动修复的建议，帮助优化代码质量。
- ⚡ **高效性能**：基于 Rust 构建，架构先进，处理大型代码库时速度极快，节省 CI 和开发时间。
- 🔧 **一体化工具链**：通过单一命令即可同时执行格式化和检查，无需复杂配置，开箱即用。
- 🌐 **广泛支持**：提供企业级商业支持，已被 AWS、Google、Microsoft 等众多领先组织采用，并拥有活跃的开源社区。

---

### [排序 | JavaScript 氧化编译器](https://oxc.rs/docs/guide/usage/formatter/sorting.html#sort-tailwind-css-classes)

**原文标题**: [Sorting | The JavaScript Oxidation Compiler](https://oxc.rs/docs/guide/usage/formatter/sorting.html#sort-tailwind-css-classes)

Oxfmt 提供了对导入语句、Tailwind CSS 类和 package.json 字段的排序功能，这些功能可通过配置文件进行自定义。

- 📦 **导入排序**：基于 `eslint-plugin-perfectionist/sort-imports`，默认禁用，支持自定义分组和换行设置。
- 🎨 **Tailwind CSS 类排序**：基于 `prettier-plugin-tailwindcss`，默认禁用，可配置样式表路径和函数。
- 📄 **package.json 字段排序**：默认启用，采用预设顺序，可调整脚本排序等选项。

---

### [排序 | JavaScript 氧化编译器](https://oxc.rs/docs/guide/usage/formatter/sorting.html#sort-imports)

**原文标题**: [Sorting | The JavaScript Oxidation Compiler](https://oxc.rs/docs/guide/usage/formatter/sorting.html#sort-imports)

Oxfmt 提供了针对导入语句、Tailwind CSS 类和 package.json 文件的排序功能，这些功能可通过配置文件进行自定义设置。

- 📦 **导入排序**：基于 `eslint-plugin-perfectionist/sort-imports`，默认关闭，支持通过分组、自定义组和换行设置来灵活配置导入语句的顺序。
- 🎨 **Tailwind CSS 类排序**：基于 `prettier-plugin-tailwindcss`，默认关闭，可指定样式表路径和函数名，并保留空白字符。
- 📄 **package.json 字段排序**：默认启用，采用预设顺序排列字段，支持额外按字母顺序排序 `scripts` 字段。

---

### [JavaScript 数据网格 | FlexGrid | Wijmo](https://developer.mescius.com/wijmo/flexgrid-javascript-data-grid?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=Wijmo-JS-Weekly-Primary-Sponsor-Feb-2026)

**原文标题**: [JavaScript DataGrid | FlexGrid | Wijmo](https://developer.mescius.com/wijmo/flexgrid-javascript-data-grid?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=Wijmo-JS-Weekly-Primary-Sponsor-Feb-2026)

Wijmo的FlexGrid是业界最灵活的JavaScript数据表格控件，提供类似Excel的丰富功能，支持高度自定义、高性能数据绑定及多种框架集成，适用于复杂的企业级应用开发。

- 📊 **类似Excel的体验** – 提供熟悉的操作界面，支持键盘快捷键、数据聚合、单元格合并和冻结等功能。
- 🎨 **高度可定制单元格** – 通过单元格模板和主题灵活定制外观与功能，支持条件样式和动态更新。
- 🌳 **树形表格支持** – 可绑定子项目创建TreeGrid，支持懒加载和XML数据导入，提升数据展示层次。
- 🔍 **动态数据筛选** – 提供全文搜索、分组、过滤等多种数据查询方式，并支持高亮匹配结果。
- ⚡ **高性能数据绑定** – 支持客户端与服务器端数据绑定，虚拟滚动技术实现流畅的大数据量浏览。
- 🛠️ **多框架兼容** – 完美支持Angular、React、Vue及PureJS，保持跨框架功能一致性。
- 📁 **数据导入导出** – 支持Excel、PDF格式的导入导出及打印功能，方便数据交换与存档。
- ♿ **无障碍访问** – 遵循WCAG 2.0 AA标准，提供ARIA支持和屏幕阅读器兼容性。
- 🔒 **安全合规** – 符合内容安全策略（CSP），确保企业级应用的安全性。
- 📦 **轻量高效** – 模块体积仅113kb，采用TypeScript开发，提供完整的类型提示和设计时错误检查。

---

### [创意代码高尔夫](https://tixy.land/)

**原文标题**: [(t,i,x,y) => "creative code golfing"](https://tixy.land/)

tixy是一个创意编程挑战平台，要求用户用32个字符以内的代码生成动态图形。

- 🎨 创意编程：通过极简代码创作动态视觉艺术
- ⛳ 代码高尔夫：限制在32字符内，挑战编程简洁性
- 🖱️ 交互设计：点击界面元素可获取更多信息
- 📐 函数参数：使用(t,i,x,y)四个参数定义图形行为
- 🎯 核心挑战：在严格限制下实现丰富的视觉效果

---

### [动画666字节位图自生成程序](https://aem1k.com/bitquine/)

**原文标题**: [Animated 666-Byte Bitmap Quine](https://aem1k.com/bitquine/)

这是一个仅666字节的动画位图程序，它既是可执行文件，又能输出自身的完整源代码，同时还能在屏幕上显示动态的旋转立方体图案。

- 🎨 程序是一个自包含的动画位图，尺寸极小，仅666字节
- 🔄 它同时是一个“奎因”（Quine），即能精确打印自身源代码的程序
- 🧊 运行时会在屏幕上显示一个不断旋转的3D立方体动画
- ⚙️ 通过巧妙的代码压缩和自引用技术实现多重功能
- 📁 文件格式为位图，但实际是可执行程序，展示编程艺术与极简主义

---

### [aemkei.github.io/bitquine/annotated.html 位于 master 分支 · aemkei/aemkei.github.io · GitHub](https://github.com/aemkei/aemkei.github.io/blob/master/bitquine/annotated.html)

**原文标题**: [aemkei.github.io/bitquine/annotated.html at master · aemkei/aemkei.github.io · GitHub](https://github.com/aemkei/aemkei.github.io/blob/master/bitquine/annotated.html)

这是一个名为“aemkei”的GitHub用户公开仓库页面，展示了其项目的基本信息和相关活动。

- 📂 仓库名称：aemkei.github.io，属于公开项目
- ⭐ 获得36个星标，被10个用户复刻
- 🔧 包含代码、议题、拉取请求等标准仓库功能
- 📋 目前有0个未解决议题和1个拉取请求
- 🛡️ 设有安全、洞察等高级管理选项
- 👁️ 需要登录才能更改通知设置

---

### [美国专利商标局商标审判与上诉委员会电子系统。案件编号92086835](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=22)

**原文标题**: [USPTO TTABVUE. Proceeding Number 92086835](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=22)

无法总结：未找到主要内容。

---

### [未找到标题](https://x.com/rough__sea/status/2026054678669414832)

**原文标题**: [No title found](https://x.com/rough__sea/status/2026054678669414832)

该页面提示用户浏览器中JavaScript功能未启用或受阻，导致无法正常使用X平台（原Twitter），并提供了相应的解决方案和支持信息。

- 🔐 检测到浏览器已禁用JavaScript，影响X平台正常使用
- 🌐 建议启用JavaScript或切换至受支持的浏览器版本
- 📖 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致加载异常，建议临时禁用后重试
- 🔄 页面提供“重试”功能供用户重新加载内容
- ⚖️ 页脚包含服务条款、隐私政策等法律文件链接

---

### [@patrickbrosset.com 在 Bluesky](https://bsky.app/profile/patrickbrosset.com/post/3mfloileyvs27)

**原文标题**: [@patrickbrosset.com on Bluesky](https://bsky.app/profile/patrickbrosset.com/post/3mfloileyvs27)

Bluesky是一个高度交互的Web应用，需要JavaScript支持，其核心功能现已支持在Service Workers中使用JavaScript模块。

- 🔧 现在可以在Service Workers中使用JavaScript模块（即通过`import`和`export`组织代码）
- 🌐 Firefox浏览器已加入支持，与其他浏览器引擎保持一致
- 📄 相关技术详情可参考官方文档链接
- 🗓️ 该更新发布于2026年2月24日

---

### [利用浏览器<canvas>进行数据压缩](https://jstrieb.github.io/posts/canvas-compress/)

**原文标题**: [Using the Browser’s <canvas> for Data Compression](https://jstrieb.github.io/posts/canvas-compress/)

本文介绍了一种利用浏览器Canvas API实现数据压缩的巧妙方法，尤其适用于旧版浏览器中缺乏直接压缩API的情况。

- 🎨 通过将数据编码为PNG图像像素，利用浏览器内置的PNG压缩算法间接实现数据压缩
- 🔧 提供完整的JavaScript压缩/解压缩函数示例，支持Uint8Array与base64字符串转换
- 🌐 主要应用场景包括SPA状态存储、URL哈希压缩等前端数据优化需求
- 📅 该方法在2023年5月前特别有用，当时Compression Streams API尚未广泛支持
- 🧪 包含演示页面和测试文件，确保代码可靠性
- ⚠️ 注意解压缩需异步处理，需等待图像加载完成
- 🔄 相比移植压缩库到WASM，此方法直接利用浏览器优化实现更高效

---

### [Vuetify —— Vue 组件框架](https://v4.vuetifyjs.com/en/)

**原文标题**: [Vuetify — A Vue Component Framework](https://v4.vuetifyjs.com/en/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- ⚡ 智能医疗管理平台自动化处理行政流程，减轻医护人员行政负担
- 🔬 自然语言处理技术助力临床研究，加速从海量文献中提取关键信息
- ⚖️ 数据隐私保护与算法透明度是目前医疗AI面临的主要伦理挑战

---

### [升级指南 — Vuetify](https://vuetifyjs.com/en/getting-started/upgrade-guide/#quick-start-with-vuetify-mcp)

**原文标题**: [Upgrade guide — Vuetify](https://vuetifyjs.com/en/getting-started/upgrade-guide/#quick-start-with-vuetify-mcp)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 💊 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 🧬 基于患者基因组数据的AI模型可为个体提供定制化治疗方案
- ⚖️ 医疗AI面临数据隐私、算法透明度及责任界定等伦理监管问题

---

### [npm 批量可信发布配置与脚本安全性现已全面推出 - GitHub 更新日志](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/)

**原文标题**: [npm bulk trusted publishing config and script security now generally available - GitHub Changelog](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/)

npm CLI v11.10.0+ 引入了两项新功能，以增强软件供应链安全性和配置效率。

- 🔄 **批量配置 OIDC 可信发布**：维护者现在可以使用 `npm trust` 命令一次性为多个软件包添加或更新可信发布配置，无需逐个配置。
- 🛡️ **新增 `--allow-git` 安装标志**：该标志允许用户明确控制 Git 依赖项的行为，默认值为 `all` 以保持向后兼容，但建议使用 `--allow-git=none` 来避免潜在的任意代码执行风险，预计在 npm CLI v12 中 `none` 将成为默认值。

---

### [Node.js — Node.js 25.7.0（当前版本）](https://nodejs.org/en/blog/release/v25.7.0)

**原文标题**: [Node.js — Node.js 25.7.0 (Current)](https://nodejs.org/en/blog/release/v25.7.0)

Node.js 25.7.0 版本发布，包含多项功能增强、错误修复和性能改进，涵盖 HTTP/2、SEA、SQLite、Stream 等模块，并更新了依赖项和文档。

- 🚀 **HTTP/2 新增 HTTP/1 回退配置选项**：允许自定义 HTTP/1 回退行为，提升兼容性。
- 📦 **SEA 支持 ESM 入口点**：单可执行应用现在可使用 ESM 模块作为入口，增强模块化支持。
- 🗃️ **SQLite 模块标记为发布候选**：SQLite 集成接近稳定，为正式发布做准备。
- 🔄 **Stream 模块重命名 Duplex.toWeb() 选项**：将 `type` 选项更名为 `readableType`，提高代码清晰度。
- 🧪 **测试运行器显示中断的测试**：在收到 SIGINT 信号时展示被中断的测试，便于调试。
- ⚙️ **多项依赖项更新**：包括 npm 升级至 11.10.1、llhttp 更新至 9.3.1 等，提升安全性和性能。
- 🛠️ **构建和工具链优化**：改进 Windows 构建配置、缓存策略和自动化测试流程。
- 📚 **文档修复与澄清**：修正多处文档错误，更新平台支持信息（如 RISC-V 64 位）。
- 🐛 **错误修复与内存泄漏处理**：解决 HTTP/2 文件句柄泄漏、Worker 进程竞争条件等问题。
- 🔗 **提供多平台安装包**：支持 Windows、macOS、Linux 等系统，包含安装程序和二进制文件。

---

### [Node.js — Node.js 24.14.0（长期支持版）](https://nodejs.org/en/blog/release/v24.14.0)

**原文标题**: [Node.js — Node.js 24.14.0 (LTS)](https://nodejs.org/en/blog/release/v24.14.0)

Node.js 24.14.0（LTS版本代号“Krypton”）发布，包含多项功能增强、性能优化和错误修复，涵盖异步钩子、文件系统、HTTP、模块系统、SQLite及测试运行器等核心模块的更新。

- 🚀 **异步钩子增强**：新增 `trackPromises` 选项至 `createHook()`，提升异步操作追踪能力。
- 🔧 **依赖项更新**：引入LIEF依赖并替换cjs-module-lexer为merve，优化模块解析与二进制分析。
- 📁 **文件系统改进**：为 `fs.watch` 添加 `ignore` 选项，增强文件监控的灵活性。
- 🌐 **HTTP功能扩展**：新增 `http.setGlobalProxyFromEnv()` 方法，支持从环境变量设置全局代理。
- 📦 **模块系统优化**：允许以 `#/` 开头的子路径导入，提升模块解析的兼容性。
- ⚡ **性能与内存优化**：改进 `AsyncLocalStorage` 在 `queueMicrotask` 中的保留机制，减少不必要的开销。
- 🗃️ **SQLite功能增强**：默认启用防御模式，并新增预处理选项参数，提升数据库操作安全性与灵活性。
- 🔌 **嵌入API支持**：为嵌入API添加初始ESM支持，扩展Node.js的嵌入应用场景。
- 📊 **流处理改进**：在 `stream/consumers` 中新增 `bytes()` 方法，优化流数据消费方式。
- 🧪 **测试运行器升级**：新增 `env` 选项和测试失败预期支持，提升测试配置与验证能力。

---

### [ESLint v10.0.2 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/02/eslint-v10.0.2-released/)

**原文标题**: [ESLint v10.0.2 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/02/eslint-v10.0.2-released/)

ESLint v10.0.2 是一个补丁版本，主要修复了先前版本中的多个错误，并更新了依赖项以解决安全漏洞。

- 🔧 更新了 ajv 依赖至 v6.14.0，修复了最近公开的安全问题
- 🐛 修复了与安全漏洞相关的错误（提交 2b72361）
- 📚 文档更新：链接规则类型说明至 CLI 选项 --fix-type（提交 13eeedb）
- 📝 更新迁移指南以反映 Program 范围变更（提交 98cbf6b）
- ✏️ 在 vars-on-top 规则示例中添加缺失的分号（提交 61a2405）
- 🔄 更新依赖项 @eslint/eslintrc 至 ^3.3.4（提交 951223b）
- 📦 更新依赖项 eslint-plugin-jsdoc 至 ^62.7.0（提交 6aa1afe）

---

### [发布 v4.12.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.12.0)

**原文标题**: [Release v4.12.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.12.0)

Hono v4.12.0 版本发布，引入了客户端新功能、中间件改进、适配器增强及显著的性能优化。

- 🛠️ Hono 客户端新增 `$path()` 方法，用于获取路径字符串，便于路由或缓存键操作。
- 🔧 新增 `ApplyGlobalResponse` 类型助手，为 RPC 客户端添加全局错误响应类型。
- 🔀 SSG 新增 `redirectPlugin`，为 HTTP 重定向响应生成静态 HTML 重定向页面。
- 🔐 Basic Auth 中间件新增 `onAuthSuccess` 回调，支持认证成功后设置上下文或记录日志。
- 🌐 `getConnInfo()` 现已支持 AWS Lambda、Cloudflare Pages 和 Netlify 适配器。
- 🔗 尾部斜杠中间件新增 `alwaysRedirect` 选项，确保重定向在通配符路由前执行。
- 🌍 语言中间件的 `normalizeLanguage` 函数支持 RFC 4647 渐进式区域代码截断。
- 📦 `ExecutionContext` 类型新增 `exports` 属性，便于 Cloudflare Workers 类型扩展。
- ⚡ TrieRouter 性能提升 1.5 至 2 倍，通过优化减少语法开销和冗余处理。
- 🚀 `c.json()` 新增快速路径优化，提升响应创建效率，减少内存分配。

---

### [发布 v2.6.10 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.6.10)

**原文标题**: [Release v2.6.10 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.6.10)

Deno 2.6.10 版本发布，主要包含多项新功能、错误修复及兼容性改进，重点增强了TLS密钥日志、许可证文件支持、编译安装功能，并修复了Node.js兼容性、Web API、安装及测试等方面的问题。

- 🔐 新增TLS密钥日志支持，便于网络调试
- 📄 扩展发布功能，支持更多许可证文件类型
- ⚙️ 新增 `deno install --compile` 命令，支持编译后安装
- 🐛 修复多项Node.js兼容性问题，包括 `assert.ok`、`fs.rmdir`、`worker_threads` 等模块
- 🌐 修复Web API中 `AbortSignal.any()` 的内存管理问题
- 📦 改进安装过程，自动清理 `node_modules` 文件夹
- 🔧 修复语言服务器协议依赖，提升开发工具稳定性
- 🧪 增强测试功能，禁止在测试执行期间调用 `Deno.test()`

---

### [发布 electron v40.6.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v40.6.0)

**原文标题**: [Release electron v40.6.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v40.6.0)

Electron v40.6.0 版本发布，新增导航时禁用自动聚焦功能，并修复了无边框窗口在 Mac App Store 构建中的调整大小问题。

- 🚀 **新增功能**：通过 `webPreferences.focusOnNavigation` 设置，支持在导航时禁用 WebContents 的自动聚焦。
- 🔧 **问题修复**：解决了在 Mac App Store 构建中无边框窗口调整大小异常的问题。
- 📅 **发布时间**：2025年2月19日，由 sudowoodo-release-bot 发布，包含16次提交。
- 🔗 **版本关联**：此功能也同步在 Electron 41 版本中提供。

---

### [发布 r183 · mrdoob/three.js · GitHub](https://github.com/mrdoob/three.js/releases/tag/r183)

**原文标题**: [Release r183 · mrdoob/three.js · GitHub](https://github.com/mrdoob/three.js/releases/tag/r183)

Three.js 发布了 r183 版本，包含多项核心功能更新、性能优化、错误修复及文档改进，涵盖渲染器、材质、节点系统、WebGPU 支持、加载器、示例和编辑器等方面。

- 🛠️ **移除废弃代码并更新工具链** – 清理了已弃用的 API，替换了 ESLint 插件，并更新了依赖包。
- 🚀 **WebGPU 渲染器增强** – 引入了反向深度缓冲支持、兼容性模式优化、MRT 混合改进及性能提升。
- 📦 **节点系统与 TSL 扩展** – 新增了 `clipSpace`、`retroPass` 等 TSL 功能，优化了节点构建和缓存机制。
- 🎨 **材质与渲染改进** – 为 `MeshLambertMaterial` 和 `MeshPhongMaterial` 添加了环境光照支持，改进了阴影映射和后期处理。
- 🔧 **加载器与资源处理** – 增强了 USD 格式支持，改进了 GLTF 加载器，并修复了多个加载器的错误。
- 📚 **文档与示例更新** – 完善了中文文档，新增了物理模拟页面，并优化了多个示例的视觉效果和性能。
- 🖥️ **编辑器功能升级** – 增加了 WebGPU 渲染器支持、动画面板、资源管理面板，并改进了用户界面。

---

### [面向人类与AI的最快前端工具 | Christoph Nakazawa](https://cpojer.net/posts/fastest-frontend-tooling)

**原文标题**: [Fastest Frontend Tooling for Humans & AI | Christoph Nakazawa](https://cpojer.net/posts/fastest-frontend-tooling)

本文介绍了2026年加速JavaScript前端工具链的现代方案，旨在为开发者和AI提供更快的反馈循环、严格的代码规范和本地推理能力。

- 🚀 **tsgo替代TypeScript**：采用Go重写的TypeScript实现，类型检查速度提升约10倍，且能捕获更多类型错误，迁移步骤简单。
- 🎨 **Oxfmt替代Prettier**：内置多种插件（如导入排序、Tailwind CSS类排序），支持多语言回退至Prettier，迁移方便。
- 🔍 **Oxlint替代ESLint**：支持直接运行ESLint插件，提供类型感知规则，可与tsgo结合进行类型检查。
- 📦 **@nkzw/oxlint-config配置包**：提供严格、一致的代码规范，禁止警告仅保留错误，优化LLM代码生成质量。
- ⚡ **开发体验优化工具**：推荐npm-run-all2并行运行脚本，ts-node结合nodemon和swc实现Node.js服务快速重启。
- 🛠️ **经典工具持续推荐**：pnpm作为高效包管理器，Vite作为快速稳定的构建工具，React配合编译器保持现代性。

---

### [非 HTML 内容](https://cpojer.net/posts/fastest-frontend-tooling.md)

**原文标题**: [Non-HTML content](https://cpojer.net/posts/fastest-frontend-tooling.md)

无法总结：非 HTML 内容。

---

### [获取失败](https://javascriptweekly.com/link/181115/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181115/web)

无法总结：获取内容失败，状态码 403。

---

### [Sanitizer API | 我能用... HTML5、CSS3等支持表格](https://caniuse.com/mdn-api_sanitizer)

**原文标题**: [Sanitizer API | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/mdn-api_sanitizer)

Sanitizer API 的浏览器支持情况目前非常有限，仅在新版本的 Firefox 和 Chrome 中得到支持，其他主流浏览器及移动端浏览器均未支持或支持状态未知。

- 🌐 **全球使用率**：当前支持率为 0%，表明该 API 尚未被广泛采用。
- 🔍 **浏览器支持**：仅 Firefox（148-150 版本）和 Chrome（146-148 版本）提供支持。
- 🚫 **普遍不支持**：IE、Edge、Safari、Opera 及其移动版本等均未支持此 API。
- 📱 **移动端情况**：iOS Safari、Android 浏览器及各大移动浏览器均未支持或支持未知。
- ❓ **未知支持**：部分浏览器如 Opera Mini 和 Baidu Browser 的支持状态尚不明确。

---

### [HTML 清理器 API](https://wicg.github.io/sanitizer-api/)

**原文标题**: [HTML Sanitizer API](https://wicg.github.io/sanitizer-api/)

本文档介绍了Sanitizer API，旨在为开发者提供一种在客户端安全处理HTML字符串的方法，以减轻DOM型跨站脚本攻击的风险。该API通过解析HTML字符串并根据用户配置过滤DOM树，确保插入的HTML不会执行脚本，同时允许开发者自定义允许的元素和属性列表。

- 🛡️ 提供安全的HTML处理机制，防止通过`innerHTML`插入字符串时意外执行JavaScript。
- 🔧 包含`setHTML()`和`setHTMLUnsafe()`等方法，支持安全与不安全两种模式，并可配置过滤规则。
- ⚙️ 通过`Sanitizer`配置对象定义允许或移除的元素、属性，支持全局和局部列表，确保配置有效性。
- 🚫 内置安全基线配置，默认移除如`<script>`、事件处理器等可能导致脚本执行的元素和属性。
- ⚠️ 注意API无法防护服务器端XSS、DOM篡改、脚本小工具攻击及变异XSS等安全威胁。

---

### [元素：setHTML() 方法 - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/setHTML)

**原文标题**: [Element: setHTML() method - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/setHTML)

Element接口的setHTML()方法提供了一种XSS安全的方式来解析和清理HTML字符串，并将其作为元素的子树插入DOM中。该方法会移除所有被视为XSS不安全的元素和属性，即使这些元素和属性在传入的清理器配置中被允许。建议在支持的情况下，将其作为设置用户提供的HTML字符串时Element.innerHTML的替代方法。

- 🛡️ **XSS安全**：setHTML()方法通过内置的清理机制，自动移除如`<script>`、`<iframe>`等XSS不安全元素和事件处理属性，确保插入的HTML内容安全。
- ⚙️ **灵活配置**：支持可选的`sanitizer`参数，允许自定义清理规则（通过`Sanitizer`对象或`SanitizerConfig`配置），但XSS不安全内容始终会被移除。
- 🔄 **替代innerHTML**：推荐用于替代`Element.innerHTML`处理不可信的HTML字符串，避免XSS攻击风险，同时保持高效解析和插入。
- 🚫 **始终移除不安全内容**：即使自定义清理器允许某些元素（如`<script>`），setHTML()仍会强制移除它们，确保最高级别的安全性。
- 📝 **使用示例**：方法支持基本用法和动态示例，可通过默认或自定义清理器处理HTML，并实时展示清理效果，便于开发者理解和调试。
- 🌐 **浏览器兼容性**：该功能尚未被广泛支持（非Baseline标准），部分主流浏览器可能无法使用，需注意兼容性并考虑备用方案。

---

### [GitHub - cure53/DOMPurify: DOMPurify - 一款仅针对DOM、超快速、高度容错的HTML、MathML及SVG跨站脚本攻击净化器。DOMPurify默认采用安全配置，同时提供丰富的可定制选项与钩子函数。演示：](https://github.com/cure53/DOMPurify)

**原文标题**: [GitHub - cure53/DOMPurify: DOMPurify - a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG. DOMPurify works with a secure default, but offers a lot of configurability and hooks. Demo:](https://github.com/cure53/DOMPurify)

DOMPurify 是一个专注于 DOM 的、速度极快、容忍度极高的 XSS 净化器，用于处理 HTML、MathML 和 SVG。它提供安全的默认配置，同时支持高度自定义和钩子函数，能有效防止跨站脚本攻击。

- 🛡️ **功能核心**：通过净化输入的脏 HTML 字符串，移除其中所有危险元素和属性，输出安全的 HTML，从而预防 XSS 攻击。
- 🌐 **广泛兼容**：支持所有现代浏览器（如 Chrome、Firefox、Safari 等）及 Node.js 环境（需配合 jsdom），对旧版浏览器（如 IE）则安全地返回原字符串。
- ⚙️ **高度可配置**：允许通过设置（如 `ALLOWED_TAGS`、`ALLOWED_ATTR`）精细控制允许的标签、属性，并支持自定义元素处理、URI 安全策略等。
- 🔗 **多种用途**：可在浏览器中直接使用，也支持服务器端运行；能与 Trusted Types API 集成，并可返回 DOM 节点或文档片段。
- 🧪 **安全可靠**：由安全专家开发，具备详细的安全目标和威胁模型，提供演示页面、净化示例，并设有安全邮件列表和漏洞赏金计划。
- 🛠️ **开发支持**：项目包含完整的测试套件、持续集成，提供钩子机制以扩展功能，并得到众多贡献者和赞助商（如 BrowserStack）的支持。

---

### [定价 — 免费支持高达5万用户 | 月费从0美元起](https://clerk.com/pricing?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=pricing-rollout&utm_content=02-24-26&dub_id=N1EB6KFQdJ8RsNy4)

**原文标题**: [Pricing — Free Up to 50K Users | Plans from $0/mo](https://clerk.com/pricing?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=pricing-rollout&utm_content=02-24-26&dub_id=N1EB6KFQdJ8RsNy4)

Clerk提供多层级身份验证服务定价方案，从免费到企业定制，支持无限应用，核心按月度留存用户（MRU）和组织（MRO）计费，并提供B2B认证、管理和计费等增强功能。

- 🆓 **免费Hobby计划**：适合起步项目，包含5万MRU/应用、3个仪表盘席位、基础认证功能，无需信用卡
- 💼 **专业Pro计划**：每月20美元起，增加无品牌展示、多因素认证、企业连接等高级功能，适合增长阶段
- 🏢 **商业Business计划**：每月250美元起，提供SOC2/HIPAA合规、优先支持、审计日志，满足团队扩展需求
- 🏭 **企业Enterprise计划**：定制方案，含高可用性SLA、专属支持、迁移协助，为大型机构提供保障
- 🔧 **B2B认证增强**：基础免费含100MRO/应用，增强版100美元/月起支持无限成员、自定义角色等高级功能
- 👥 **管理功能**：基础版含5次用户模拟，增强版提供无限模拟权限，便于团队协作管理
- 💳 **集成计费服务**：所有计划均含0.7%交易费率，无缝集成Stripe，提供订阅管理和预建组件
- 🎯 **清晰计价模式**：按实际留存用户/组织收费，首日免费，提供用量阶梯折扣，数据可随时导出

---

### [获取失败](https://javascriptweekly.com/link/181121/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181121/web)

无法总结：获取内容失败，状态码 429。

---

### [我的Angular技术栈在2026年 - YouTube](https://www.youtube.com/watch?v=tT5xMfHb4Gg)

**原文标题**: [My Angular Stack in 2026 - YouTube](https://www.youtube.com/watch?v=tT5xMfHb4Gg)

该文本为YouTube网站页脚的标准法律与信息链接列表，概述了平台的核心政策、功能及公司信息。

- 📄 **关于我们** - 介绍YouTube平台的基本信息。
- 📢 **新闻中心** - 提供官方新闻和公告。
- ©️ **版权** - 链接至版权政策与内容所有权信息。
- 📧 **联系我们** - 提供用户与平台沟通的渠道。
- 👥 **创作者** - 面向内容创作者的相关资源与信息。
- 💼 **广告** - 关于广告投放和广告商的信息。
- 👨‍💻 **开发者** - 面向技术开发者的API和工具资源。
- 📑 **条款** - 平台的使用条款与条件。
- 🔒 **隐私** - 隐私政策与数据保护措施。
- ⚖️ **政策与安全** - 社区准则、安全政策与执行措施。
- ⚙️ **YouTube工作原理** - 解释平台的算法、推荐系统等运作方式。
- 🧪 **测试新功能** - 关于新功能测试与用户体验更新的信息。
- ⓘ **版权声明** - 注明公司所有权及年份（© 2026 Google LLC）。

---

### [如何通过GitHub Actions发布到NPM | 以优质软件构建更美好世界](https://glebbahmutov.com/blog/npm-publish-from-github/)

**原文标题**: [How To Publish To NPM From GitHub Actions | Better world by better software](https://glebbahmutov.com/blog/npm-publish-from-github/)

本文介绍了如何利用NPM OIDC可信发布工作流，通过GitHub Actions自动化发布NPM包，以应对个人令牌失效带来的发布中断问题。

- 🔐 NPM在2025年底撤销了所有个人令牌，提升了安全性但中断了CI发布流程
- 🤖 作者拥有400多个NPM包，必须实现自动化发布，拒绝手动操作
- ⚙️ 可信发布功能允许NPM识别特定GitHub Actions工作流为合法发布者
- 🔧 配置步骤：进入NPM账户设置→选择GitHub Actions→填写用户名、仓库名和工作流文件名
- 📝 更新ci.yml工作流文件，移除旧NPM令牌，添加id-token: write权限
- 🚀 使用semantic-release-action实现语义化版本发布，配合GITHUB_TOKEN
- ✅ 成功案例：cypress-split和cypress-map已采用此方案，cypress-timestamps也将应用
- 🔍 关键配置：确保使用Node.js v24+版本，避免身份验证错误

---

### [使用Three.js与WebGL打造无限循环的贪吃蛇游戏 | Codrops](https://tympanus.net/codrops/2026/02/10/building-an-endless-procedural-snake-with-three-js-and-webgl/)

**原文标题**: [Building an Endless Procedural Snake with Three.js and WebGL | Codrops](https://tympanus.net/codrops/2026/02/10/building-an-endless-procedural-snake-with-three-js-and-webgl/)

本文深入探讨了如何利用Three.js和WebGL构建一个基于GPU增强的无限程序化蛇形曲线系统，通过简单的转向规则和连续的贝塞尔路径，实现有机的动态效果。

- 🐍 系统采用两段式曲线设计：CurveGenerator根据行为规则生成短贝塞尔段，EndlessCurve将其拼接成连续且内存受限的路径，最终渲染出程序化蛇形。
- 🧭 运动方向由多种转向力（如追踪、环绕、盘旋、随机游走）混合决定，并通过转向速率限制确保平滑过渡，避免突变。
- 📐 每个更新周期根据方向生成短立方贝塞尔段，通过自适应控制点保持曲线平滑，并确保相邻段之间的G1连续性。
- ♾️ 无限曲线系统采用滑动窗口机制，动态生成新段并移除旧段，同时通过全局距离计数器维持路径连续性。
- 🧩 使用并行传输框架计算稳定的法线方向，避免视觉扭曲，并通过缓存和插值优化随机访问性能。
- 🖥️ 蛇身通过实例化几何体构建，利用数据纹理将曲线位置和法线信息上传至GPU，在顶点着色器中完成定位和渲染。
- 🎨 通过半径变化、椭圆截面、腹部偏移、轻微扭转和噪声扰动等细节增强真实感，并结合光照效果（如边缘光、阴影压缩和各向异性高光）提升视觉表现。
- 🔮 未来可扩展方向包括：腹部约束运动、更精确的盘旋行为、解剖学头部建模、环境交互以及应用于其他动态物体（如触手、藤蔓）。

---

### [OpenSeadragon](http://openseadragon.github.io/)

**原文标题**: [OpenSeadragon](http://openseadragon.github.io/)

OpenSeadragon 是一个开源的、基于 Web 的高分辨率可缩放图像查看器，使用纯 JavaScript 实现，适用于桌面和移动设备。它支持多种图像服务协议，提供丰富的界面元素和 UI 定制选项，并拥有众多插件来扩展功能，如注释、滤镜、测量等。此外，它还提供浏览器扩展、详细的 API 文档、学习课程以及活跃的社区支持。

- 🌐 开源可缩放图像查看器，适用于桌面和移动设备
- 🧩 支持多种图像服务协议（如 DZI、IIIF、Zoomify 等）
- 🛠️ 提供丰富的界面元素和 UI 定制选项
- 🔌 拥有众多插件，扩展注释、滤镜、测量等功能
- 🌍 提供浏览器扩展，可在网页上直接使用
- 📥 支持多种安装方式（下载、npm、CDN 等）
- 📚 提供详细的 API 文档和学习课程
- 💬 拥有活跃的社区支持（GitHub、Twitter、Discord 等）
- 🔧 开源开发，基于 New BSD 许可证

---

### [发布 v6.0.0 · openseadragon/openseadragon · GitHub](https://github.com/openseadragon/openseadragon/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · openseadragon/openseadragon · GitHub](https://github.com/openseadragon/openseadragon/releases/tag/v6.0.0)

OpenSeadragon项目发布了v6.0.0版本，主要进行了数据管道的全面重构，引入了新的缓存系统、异步数据转换和失效处理机制，并新增了多项功能、优化和问题修复。

- 🚀 **数据管道重构**：彻底改革了数据管理，引入基于缓存的异步数据转换与失效处理系统。
- 🛠️ **新增功能**：支持IIP和Iris瓦片源、默认自动选择WebGL或Canvas渲染器、新增动画期间加载目标区域瓦片选项。
- 🔧 **API增强**：新增完全加载状态监测、键盘导航控制、坐标转换改进及TypeScript类型定义集成。
- ⚡ **性能优化**：提升移动端性能、改进WebGL支持与恢复机制、增加瓦片加载批处理选项。
- 🐛 **问题修复**：修复了透明度检测、鼠标跟踪、图像排列、瓦片更新等多个已知问题。
- 📚 **文档与测试**：改进了代码文档、命名规范，并增加了新的测试套件与演示示例。

---

### [未找到标题](https://cannoneyed.com/projects/isometric-nyc)

**原文标题**: [No title found](https://cannoneyed.com/projects/isometric-nyc)

作者利用最新的生成式AI模型和编码代理工具，创建了一个巨大的等距像素艺术纽约市地图项目，探索了AI在创意工作中的潜力和局限。

- 🏙️ 项目灵感源于对90年代末/00年代初世界建造游戏的怀旧，旨在用像素艺术风格重现纽约市景观。
- 🤖 作者几乎未手写代码，主要依赖Claude Code、Gemini CLI和Cursor等AI编码代理完成开发，显著提升了效率。
- 🗺️ 初始尝试使用CityGML数据渲染城市几何体，后转向Google Maps 3D tiles API以获得更精确的几何和纹理。
- 🎨 使用Nano Banana Pro生成像素艺术图块，但面临一致性和成本问题，转而微调Qwen/Image-Edit模型以优化效果和成本。
- 🔄 采用“填充”策略生成无缝图块，通过掩码逐步生成相邻内容，确保整体一致性。
- 🛠️ 开发了端到端的生成应用程序，包括数据库存储、Web界面和微工具（如边界编辑器、水体分类器），以支持大规模生成。
- 🌊 项目遇到水体和树木等边缘情况，模型难以可靠生成，需结合手动修正和定制工具处理。
- ⚙️ 为提升生成速度和降低成本，将模型部署到Lambda AI的GPU实例，实现并行处理和规模化生成。
- 🤔 发现图像模型与文本/代码模型存在显著差距，尤其在理解自身错误和编辑特定部分方面能力有限。
- ❄️ 项目后期添加了雪景图层，通过颜色归一化、水体掩码增强和服务器无GPU推理（使用modal.com）进一步优化了自动生成流程。
- 💡 核心收获：AI代理使软件构建变得廉价快速，但软件工程原则（如模块化、测试）仍然关键；图像模型尚未成熟，自动化质量评估仍具挑战；AI消除了创意工作中的繁琐任务，使艺术家能专注于决策和细节打磨。

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=jsweekly&utm_medium=referral&utm_campaign=feb2)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=jsweekly&utm_medium=referral&utm_campaign=feb2)

SurveyJS是一套开源JavaScript库，用于在应用中自主构建和管理调查表单，支持完全的数据所有权与自托管，无需依赖第三方SaaS平台。

- 📚 **表单库** – 免费MIT许可的UI组件，可解析JSON表单配置并在JavaScript应用中动态渲染交互式表单，用于收集用户响应并存储至自有数据库。
- 🛠️ **调查创建器** – 白标拖放式表单构建工具，自动生成描述表单结构、样式和行为的JSON模式，支持深度定制以匹配应用设计。
- 📊 **仪表板** – 通过JSON模式解析响应数据，生成交互式图表和表格，实现调查结果的实时可视化分析。
- 🖨️ **PDF生成器** – 将JSON表单模式转换为PDF格式，支持填充已收集的响应数据，导出可编辑或预填的PDF文件。
- ♿ **无障碍支持** – 表单库与调查创建器全面遵循WCAG、Section 508和ARIA标准，支持键盘导航与屏幕阅读器。
- ∞ **无使用限制** – 不限制表单数量、响应量、管理员或提交次数，所有数据存储于用户自有数据库。
- 🧩 **自定义输入字段** – 支持创建自定义问题类型，可扩展内置组件或集成Angular、React、Vue 3组件。
- 📡 **离线数据收集** – 支持完全离线工作，表单、主题和响应本地存储，恢复网络后自动同步。
- 💳 **一次性购买许可** – 开发者可永久使用调查创建器、PDF生成器和仪表板，包含12个月免费维护与期间所有版本永久使用权。
- ✅ **自定义数据验证** – 除内置客户端验证外，支持通过JavaScript函数和事件处理器创建自定义客户端规则与服务器端校验。
- 🔓 **开源与自托管** – 所有库在GitHub开源，支持React、Angular、Vue 3和原生JavaScript，允许修改扩展并保持数据自主托管。
- 🎨 **白标化定制** – 完全控制表单与调查创建器的外观，支持CSS变量主题、JSON导出及元素级样式定制。
- 🤖 **AI辅助功能** – 可通过API集成AI，实现自然语言表单生成、翻译与智能内容建议。
- 🏢 **多行业适用** – 服务于保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利组织及银行等领域，满足敏感数据的安全收集与合规需求。
- 🔒 **数据安全与合规** – 支持自托管以完全控制数据流，帮助满足HIPAA、FERPA、GDPR等法规要求，确保隐私与法律合规。
- 🔄 **前后端分离** – 仅提供前端UI库，需用户自行构建后端实现数据存储、用户管理与业务流程，保障系统灵活性。

---

### [bignumber.js API](https://mikemcl.github.io/bignumber.js/)

**原文标题**: [bignumber.js API](https://mikemcl.github.io/bignumber.js/)

BigNumber.js 是一个用于任意精度算术的 JavaScript 库，提供高精度数值计算功能，支持大数运算、多种舍入模式及格式化输出。

- 🔢 **构造函数与配置**：通过 `BigNumber` 构造函数创建实例，支持十进制、二进制、十六进制等多种进制输入，并可配置小数位数、舍入模式等参数。
- ⚙️ **静态方法**：包括最大值（`maximum`）、最小值（`minimum`）、随机数生成（`random`）和求和（`sum`）等工具函数。
- 🔄 **实例方法**：提供丰富的数学运算，如加减乘除（`plus`、`minus`、`times`、`div`）、取模（`modulo`）、幂运算（`exponentiatedBy`）和平方根（`squareRoot`）。
- 📏 **精度与格式化**：可设置和获取数值的精度（`decimalPlaces`、`precision`），并支持格式化输出（`toFormat`、`toExponential`、`toFixed`）。
- 🧮 **舍入模式**：内置多种舍入模式（如 `ROUND_UP`、`ROUND_HALF_EVEN`），适用于不同计算场景。
- 🛡️ **错误处理**：对无效输入或操作抛出详细错误，便于调试和验证。
- 🔧 **高级功能**：支持克隆独立构造函数（`clone`）、对象序列化（`toObject`）以及安全随机数生成（需配置 `CRYPTO`）。
- ❓ **常见问题**：解释了为何移除尾随零以保持计算清晰性，避免精度误导。

---

### [慢动作](https://slowmo.dev/)

**原文标题**: [slowmo](https://slowmo.dev/)

Slowmo 是一个用于控制网页内容时间速度的 JavaScript 库，支持减速、暂停或加速动画、视频及交互效果，便于调试、学习或调整游戏难度。

- 🐢 通过 npm 安装或 Chrome 扩展快速集成，使用 `slowmo(0.5)` 即可将时间速度减半
- 🎮 提供直观交互：拖动边缘调整速度，点击中心暂停，支持 CSS、JS 动画及 HTML5 视频
- ⚙️ 完整 API 包括设置速度、暂停/播放、重置及获取当前速度，如 `slowmo.pause()` 暂停所有动画
- 💡 灵感来源于 Benji Taylor 的 "agentation" 项目，开源在 GitHub 并遵循 MIT 许可证

---

### [GitHub - seflless/slowmo](https://github.com/seflless/slowmo?tab=readme-ov-file#what-it-works-with)

**原文标题**: [GitHub - seflless/slowmo](https://github.com/seflless/slowmo?tab=readme-ov-file#what-it-works-with)

slowmo 是一个用于控制网页内容时间流速的 JavaScript 库，允许开发者减速、暂停或加速动画、视频及各类基于时间的交互效果，便于调试、学习或调整游戏难度。

- 🎬 **核心功能**：通过简单 API 调整网页动画、视频、音频等内容的播放速度，支持从暂停到加速的多档调节。
- ⚙️ **易于集成**：通过 npm 安装，一行代码即可控制全局或特定元素的时间流速。
- 🎛️ **可视化控件**：提供可拖拽、旋转的拨盘 UI 组件，支持原生 JS 和 React，操作直观且状态持久化。
- 🛡️ **兼容广泛**：支持 CSS 动画、Web Animations API、视频音频、requestAnimationFrame、GSAP、Three.js 等主流动画技术。
- 🚫 **排除控制**：允许特定元素通过 `data-slowmo-exclude` 属性保持原速，不受全局速度影响。
- ⚠️ **存在限制**：无法平滑控制基于固定帧递增的动画；iframe、Service Workers 等独立线程内容需额外处理；视频音频有浏览器速度限制。
- 🔧 **开源贡献**：项目基于 MIT 许可证开放源码，提供 Chrome 扩展规划，欢迎开发者参与改进。

---

### [React 医生](https://www.react.doctor/)

**原文标题**: [React Doctor](https://www.react.doctor/)

本文介绍了人工智能在医疗领域的应用现状与未来前景，重点探讨了其在疾病诊断、药物研发、个性化治疗及医疗管理中的具体作用。

- 🩺 AI辅助诊断：通过深度学习分析医学影像，提升早期疾病检测准确率
- 💊 药物研发加速：利用算法预测分子结构，大幅缩短新药开发周期
- 🧬 个性化治疗方案：基于患者基因数据定制治疗策略，提高疗效
- 📊 医疗资源优化：智能调度系统改善医院运营效率，缓解资源不均问题
- 🔮 未来挑战：数据隐私保护、算法透明度及临床验证仍需突破

---

### [React 扫描](https://react-scan.com/)

**原文标题**: [React Scan](https://react-scan.com/)

React Scan 是一款无需代码改动即可自动检测 React 应用性能问题的工具，提供多种集成方式，帮助开发者快速定位需优化的组件。

- 🛠️ 无需代码改动即可检测 React 应用性能问题
- 🔍 精准高亮需优化的组件，提供直观视觉提示
- 📦 支持多种集成方式：通过脚本标签、npm 等灵活使用
- 🚀 提供便捷的启动命令和手动安装选项，适配不同项目框架
- 🤝 受多个工程团队信任，提供 GitHub 和 Discord 社区支持

---

### [React Grab](https://www.react-grab.com/)

**原文标题**: [React Grab](https://www.react-grab.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 🧬 基于基因数据的AI模型可为患者提供个性化治疗方案，实现精准医疗
- ⚖️ 医疗AI面临数据隐私、算法透明度及责任归属等伦理监管问题

---

### [GitHub - millionco/react-doctor：让编码代理诊断并修复你的React代码](https://github.com/millionco/react-doctor)

**原文标题**: [GitHub - millionco/react-doctor: Let coding agents diagnose and fix your React code](https://github.com/millionco/react-doctor)

React Doctor 是一个开源工具，通过 AI 代理自动诊断和修复 React 代码问题，提供健康评分和详细建议。

- 🩺 **功能概述**：自动扫描代码库，检测安全、性能、正确性和架构问题，输出 0-100 健康评分。
- ⚙️ **工作原理**：并行执行代码规范检查（60+规则）和死代码检测，根据项目配置自动适配规则。
- 📥 **安装使用**：通过 `npx -y react-doctor@latest` 快速安装，支持 `--verbose` 查看详细结果。
- 🤖 **AI 代理集成**：提供脚本让 Cursor、Claude 等编码代理学习 47+ React 最佳实践规则。
- 🔧 **GitHub Actions**：支持集成到 CI/CD，可设置差异扫描和自动生成 PR 评论。
- ⚡ **配置灵活**：通过配置文件或 `package.json` 自定义忽略规则、文件路径和检查选项。
- 📊 **API 支持**：提供 Node.js API 供程序化调用，返回诊断结果和结构化数据。
- 🌟 **社区应用**：已用于多个知名开源项目（如 tldraw、excalidraw），评分公开可查。
- 🔄 **开源贡献**：项目基于 MIT 许可，鼓励开发者参与改进和提交 PR。

---

### [GitHub - antonygiomarxdev/angular-doctor: 扫描你的Angular代码库，检测性能、架构和死代码问题——输出0-100健康评分并提供可操作的诊断建议](https://github.com/antonygiomarxdev/angular-doctor)

**原文标题**: [GitHub - antonygiomarxdev/angular-doctor: Scan your Angular codebase for performance, architecture, and dead code issues — outputs a 0–100 health score with actionable diagnostics](https://github.com/antonygiomarxdev/angular-doctor)

Angular Doctor 是一款用于扫描 Angular 代码库并生成健康评分的工具，可检测性能、架构和死代码问题，提供 0-100 分的健康评分及可操作的诊断建议。

- 🩺 **Angular 感知的代码检查**：支持对组件、指令、管道、性能、架构和 TypeScript 进行针对性检查。
- 💀 **死代码检测**：通过 knip 识别未使用的文件、导出和类型。
- 🏢 **工作区支持**：自动识别 Angular CLI 和 npm/pnpm 工作区，支持多项目扫描。
- 📊 **差异扫描模式**：仅扫描相对于基准分支发生更改的文件。
- 📄 **Markdown 报告生成**：可生成详细报告，便于分享和存档。
- ⚙️ **灵活的配置选项**：支持通过配置文件或 CLI 参数自定义检查规则和忽略项。
- 🔧 **Node.js API**：提供编程接口，便于集成到其他工具或自动化流程中。
- 🧪 **全面的检查范围**：涵盖组件规范、性能优化、架构最佳实践和 TypeScript 使用等多个方面。

---

### [未找到标题](https://vue-scrollama.pages.dev/)

**原文标题**: [No title found](https://vue-scrollama.pages.dev/)

Vue-Scrollama 是一个 Vue 组件库，用于创建滚动驱动的交互式叙事（scrollytelling）效果，支持组件和组合式 API 两种使用方式。

- 🎯 提供组件和组合式 API 两种实现滚动叙事的方式
- 📊 包含组件原语和实际滚动叙事模式示例
- 🔗 开源项目，可在 GitHub 上获取
- 📐 支持图形元素在滚动时固定定位（Sticky Graphic）

---

### [Scrollama.js入门指南](https://pudding.cool/process/introducing-scrollama/)

**原文标题**: [An Introduction to Scrollama.js](https://pudding.cool/process/introducing-scrollama/)

Scrollama.js 是一个轻量级的 JavaScript 库，用于实现滚动叙事效果，它利用 IntersectionObserver 替代传统的滚动事件监听，以提升性能和用户体验。该库提供了步骤触发、步骤进度跟踪和粘性图形模式等核心功能，适用于创建流畅的交互式滚动故事。

- 🚀 **轻量高效**：基于原生 JavaScript，无依赖项，通过 IntersectionObserver 优化滚动检测，减少页面卡顿。
- 🎯 **核心功能**：支持步骤触发、步骤进度（0-100%）和粘性图形模式，简化常见滚动叙事模式的实现。
- 📱 **兼容性强**：提供 Polyfill 确保在不支持 IntersectionObserver 的浏览器中正常运行。
- 🛠️ **易于使用**：通过 HTML、CSS 和 JS 的简单配置即可搭建滚动叙事结构，支持自定义图形和布局。
- 📖 **文档丰富**：提供详细文档、示例代码和最佳实践指南，帮助开发者快速上手并适配移动端。

---

### [GitHub - lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid#readme)

**原文标题**: [GitHub - lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid#readme)

这是一个用于将Mermaid图表渲染为美观SVG或ASCII艺术的开源库，专为AI编程时代设计，支持同步渲染、丰富主题和终端输出。

- 🚀 **超快同步渲染** – 无需异步等待，支持React的`useMemo`实现零闪烁图表生成
- 🎨 **强大主题系统** – 提供15种内置主题，支持CSS变量实时切换，兼容Shiki所有VS Code主题
- 📟 **双输出格式** – 可生成精美SVG图像或ASCII/Unicode终端艺术，满足不同场景需求
- 🧩 **多图表类型** – 支持流程图、状态图、时序图、类图和ER图五种Mermaid核心图表
- 🎯 **极简配置** – 仅需背景和前景两种颜色即可生成协调美观的图表（单色模式）
- 🔌 **零DOM依赖** – 纯TypeScript实现，可在任何JavaScript环境中运行
- ⚡ **性能优异** – 500毫秒内可渲染100+个图表，基于优化的ELK.js布局引擎
- 📦 **易于集成** – 提供React组件示例，支持同步和异步两种渲染方式

---

### [发布 v3.4.0 · plotly/plotly.js · GitHub](https://github.com/plotly/plotly.js/releases/tag/v3.4.0)

**原文标题**: [Release v3.4.0 · plotly/plotly.js · GitHub](https://github.com/plotly/plotly.js/releases/tag/v3.4.0)

这是一个关于Plotly.js版本3.4.0的发布说明页面，其中包含新增功能、改进和修复的更新内容。

- 🚀 **版本发布**：Plotly.js v3.4.0 于2024年2月20日由alexshoe发布。
- 🆕 **新增功能**：支持点击图例标题切换所有轨迹的可见性；支持形状引用多个坐标轴；支持散点图中使用虚线标记线。
- 🔧 **改进内容**：优化条形图外部文本标签的坐标轴自动范围，避免标签被裁剪。
- 🐛 **问题修复**：修复堆叠面积图中某些轨迹在隐藏/显示操作后填充渲染不正确的问题；修复scattergl动画轨迹类型中的越界索引问题。
- 👥 **贡献者**：感谢chrimaho和BJohnBraddock的代码贡献。

---

### [Plotly JavaScript 图形库](https://plotly.com/javascript/)

**原文标题**: [
     Plotly javascript graphing library in JavaScript
](https://plotly.com/javascript/)

Plotly.js 是一个基于 d3.js 和 stack.gl 构建的高级声明式图表库，提供超过 40 种图表类型，包括 3D 图表、统计图表和 SVG 地图。它免费开源，支持高度定制，并通过 WebGL 实现高性能渲染，同时其 JSON 结构使其能跨 Python、R、MATLAB 等平台使用。

- 📊 **丰富的图表类型**：内置超过 40 种图表，涵盖 3D、统计、地图等多样化需求。
- 🆓 **免费开源**：完全免费开放源代码，用户可查看、报告问题或贡献代码。
- 🛠️ **高度可定制**：通过 JSON 对象声明式配置图表，支持颜色、网格、图例等细节调整。
- ⚡ **高性能渲染**：利用 WebGL 和 stack.gl 技术，实现快速交互式 2D/3D 图表渲染。
- 🌐 **跨平台兼容**：基于 JSON 结构，可无缝集成到 Python、R、MATLAB 等编程环境中。
- 📈 **多样化应用场景**：支持基础图表、科学图表、金融图表、地图及动画等多种用途。

---

### [发布 pnpm 10.30 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.30.0)

**原文标题**: [Release pnpm 10.30 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.30.0)

pnpm 10.30.0版本发布，主要改进了`pnpm why`命令的功能和性能，并修复了相关问题。

- 🔄 `pnpm why`现在显示反向依赖树，使依赖关系更清晰易读
- 🛠️ 恢复了`pnpm why`的依赖修剪功能，优先保证正确性
- ⚡ 优化了`pnpm why`和`pnpm list`在大型工作区中的性能表现
- 🔒 版本标签和提交均经过GPG签名验证
- 📅 该版本于2024年2月17日发布，包含379次提交更新

---

### [pnpm why | pnpm](https://pnpm.io/cli/why)

**原文标题**: [pnpm why | pnpm](https://pnpm.io/cli/why)

pnpm why 命令用于显示依赖指定包的所有包，输出为反向依赖树，从指定包回溯到工作区根目录，并自动去重重复子树。

- 🔍 **显示依赖关系**：列出所有依赖指定包的包，形成反向依赖树。
- 🌳 **树状结构**：输出以指定包为根，依赖包为分支，回溯至工作区根。
- 🔄 **自动去重**：重复子树在输出中标记为“deduped”。
- 📁 **递归选项**：使用 `--recursive` 在子目录或工作区所有包中执行。
- 📊 **输出格式**：支持 JSON (`--json`)、详细 (`--long`)、可解析 (`--parseable`) 格式。
- 🌍 **全局包**：`--global` 选项查看全局安装目录中的包。
- 📦 **依赖类型过滤**：`--prod` 仅显示 dependencies，`--dev` 仅显示 devDependencies。
- 📏 **深度限制**：`--depth` 限制依赖树的显示深度。
- 🏢 **工作区项目**：`--only-projects` 仅显示工作区内也是项目的依赖。
- 🚫 **排除对等依赖**：`--exclude-peers` 排除对等依赖（但保留其子依赖）。
- 🔎 **包选择器过滤**：`--filter` 按选择器过滤依赖。
- 🔧 **自定义查找器**：`--find-by` 使用 .pnpmfile.cjs 中的查找器函数按非名称属性匹配依赖。

---

### [docx - 使用JavaScript生成.docx文档](https://docx.js.org/)

**原文标题**: [docx - Generate .docx documents with JavaScript](https://docx.js.org/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🤖 AI辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，助力医院资源调度与远程医疗服务
- ⚠️ 数据隐私保护与算法透明度仍是亟待解决的技术伦理挑战
- 🔮 未来AI或将成为医疗人员的协同工具，推动精准医疗发展

---

### [JSNation——2026年主要JavaScript大会](https://jsnation.com/?utm_source=partner&utm_medium=jsweekly)

**原文标题**: [JSNation – the main JavaScript conference of 2026](https://jsnation.com/?utm_source=partner&utm_medium=jsweekly)

JSNation 2026 是一场为期两天的 JavaScript 国际会议，将于 6 月 11 日（阿姆斯特丹线下+线上）和 6 月 15 日（线上）举行。会议聚焦全栈工程与 Web 开发前沿，设有 50 多位演讲者、深度专题研讨、免费及付费工作坊，并提供丰富的线上线下社交活动。参与者可了解 AI 辅助编程、Node.js 演进、前端架构等最新趋势，并与全球开发者社区建立联系。

- 🗓️ **会议时间与形式**：2026年6月11日（阿姆斯特丹线下+线上）与6月15日（线上），为期两天双轨制。
- 🎤 **核心内容**：50多位行业专家演讲，涵盖全栈开发、AI 工程、Node.js、TypeScript、Vite 等前沿技术。
- 👥 **参与规模**：预计1500名线下参会者，超1万名远程参与者，汇聚全球 JavaScript 开发者社区。
- 🧠 **深度专题**：设有“全栈开发与架构”、“AI 辅助编程”、“晋升高级工程师与 Tech Lead”等深度研讨主题。
- 🛠️ **实践工作坊**：会前会后提供免费与付费工作坊，主题包括 React Query、DevOps 实践、AI 应用开发等。
- 🏆 **开源奖项**：设立 JS 开源奖项，表彰对社区有突出贡献的开源项目与个人。
- 🤝 **社交活动**：包含线下派对、城市游览、演讲者见面会及线上交流室，促进社区连接。
- 🎫 **票务选择**：提供线下混合票、远程票及包含酒店的组合票，并有多人团队折扣与奖学金计划。

---

### [精密AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的日常交互，自动生成并维护覆盖所有代码分支和用户流程的测试套件，无需手动编写或维护测试，从而帮助开发团队高效、无差错地发布代码。

- 🚀 **无需编写测试**：通过记录开发、预演和生产环境中的用户交互，自动生成覆盖所有代码行和边缘情况的测试套件。
- 🔄 **测试自动演化**：随着应用更新，测试套件自动添加新测试并淘汰过时测试，保持测试的时效性和完整性。
- ⚡ **闪电般执行速度**：利用并行计算集群，可在120秒内完成数千个屏幕的测试，大幅提升测试效率。
- 🛡️ **消除测试波动**：基于Chromium构建的确定性调度引擎，从根本上消除测试中的不稳定因素，确保结果可靠。
- 🔗 **无缝集成**：支持与现有测试套件结合使用或完全替代，轻松集成到CI/CD流程中，无需额外配置测试账户或模拟数据。
- 📈 **提升开发速度**：帮助团队快速、可靠地发布无回归错误的代码，被Dropbox、Notion等超过100家组织信任使用。

---

### [Windows 3.11 模拟器 - Pieter™ 打造的拨号上网复古电脑](https://pieter.com/)

**原文标题**: [
        Windows 3.11 Emulator - retro computer with dial-up internet by Pieter™    ](https://pieter.com/)

这篇文章介绍了由@levelsio和@bai0共同创建的“Help Ideas + Bugs”平台，旨在收集用户反馈、创意和错误报告，以改进产品或服务。

- 💬 平台功能：用户可通过键盘快捷键提交帮助请求、分享创意或报告软件缺陷
- 👥 合作项目：由两位开发者@levelsio和@bai0联合打造，专注于用户反馈收集
- ⌨️ 交互设计：采用直观的键盘界面，支持快速输入和操作
- 📥 数据管理：提供加载和下载功能，便于处理反馈信息
- 🔧 实用工具：包含删除、大小写切换等编辑功能，优化用户体验

---

### [Git的魔法文件 | 安德鲁·内斯比特](https://nesbitt.io/2026/02/05/git-magic-files.html)

**原文标题**: [Git’s Magic Files | Andrew Nesbitt](https://nesbitt.io/2026/02/05/git-magic-files.html)

Git 仓库中包含一系列特殊的配置文件，它们随代码一同提交，用于控制 Git 的行为和工具的工作方式，如忽略文件、处理属性、配置子模块等。这些文件不仅影响 Git 本身，还被许多外部工具（如版本管理器、编辑器、CI/CD 平台）所使用，以实现自动化和标准化的工作流程。

- 📁 **.gitignore**：定义 Git 应忽略的文件模式，支持通配符、目录标记和否定规则，可从多个位置读取（如全局忽略文件）。
- ⚙️ **.gitattributes**：配置文件的处理方式，包括行尾标准化、二进制文件标记、自定义差异和合并驱动，以及覆盖 GitHub Linguist 的语言检测。
- 🔗 **.lfsconfig**：存储 Git LFS 的配置，如服务器端点和传输设置，确保所有开发者使用相同的 LFS 环境。
- 🧩 **.gitmodules**：记录子模块的路径、URL 和分支信息，用于管理嵌套的 Git 仓库作为依赖项。
- 📧 **.mailmap**：映射作者名称和邮箱地址到规范身份，用于聚合 `git log`、`git shortlog` 和 `git blame` 中的提交记录。
- 🚫 **.git-blame-ignore-revs**：列出 `git blame` 应跳过的提交（如格式化更改），以显示有意义的代码修改作者。
- 📝 **.gitmessage**：作为提交消息的模板，需手动配置 `commit.template` 来使用，指导开发者编写规范的提交信息。
- 🌐 **平台特定文件夹**：如 `.github/`、`.gitlab/` 等，包含 CI/CD 工作流、问题模板等配置，专用于对应的代码托管平台。
- 📂 **其他约定文件**：如 `.gitkeep`（保留空目录）、`.gitconfig`（建议配置）、`.gitsigners`（签名密钥）等，扩展 Git 工作流。
- 🛠️ **外部工具文件**：如 `.editorconfig`（编辑器设置）、`.ruby-version`（语言版本）、`.dockerignore`（Docker 忽略规则），被多种开发工具自动读取以标准化环境。

---

### [x86CSS](https://lyra.horse/x86css/)

**原文标题**: [x86CSS](https://lyra.horse/x86css/)

这是一个仅用CSS实现的x86 CPU模拟器项目，能够在浏览器中运行编译后的8086机器代码，无需JavaScript支持。

- 🖥️ 项目是一个完全用CSS编写的x86 CPU模拟器，可执行8086机器代码，无需JavaScript
- 🔧 兼容性有限，目前仅支持基于Chromium的浏览器，使用了CSS的if()语句、样式查询等高级功能
- ⚙️ 支持自定义程序运行，用户可通过编译8086汇编或C代码（使用gcc-ia16）生成程序文件
- 🎨 项目为纯手工编写CSS，部分重复代码使用Python脚本生成，强调艺术性与趣味性而非实用性
- 📚 实现了大部分x86指令集，通过实际程序需求逐步完善，但并非完全模拟所有硬件细节
- ⌨️ 提供自定义I/O接口，示例程序展示了字符输出与键盘输入交互功能
- 🚫 明确声明未使用AI工具开发，认为此类项目无法通过LLM实现
- 🔗 包含完整开发工具链说明，支持内存大小调整和跨平台编译（Linux/WSL）

---

### [全息图](https://hologram.page/)

**原文标题**: [Hologram](https://hologram.page/)

Web开发通过Hologram的声明性组件系统再次变得简单，允许开发者完全使用Elixir构建丰富交互的UI，无需依赖JavaScript框架。

- 🚀 使用Elixir构建交互式UI：通过Hologram的声明性组件系统，开发者能完全用Elixir创建前端界面，简化开发流程。
- 🔄 智能转译为JavaScript：客户端代码被智能转译为JavaScript，提供现代前端功能，无需额外JavaScript框架。
- 📚 资源与支持：提供入门指南、文档、课程、通讯和GitHub资源，由赞助支持，帮助开发者快速上手和深入使用。

---

### [从34%到96%：移植计划成果显著 - Hologram v0.7.0 - Hologram](https://hologram.page/blog/porting-initiative-delivers-hologram-v0-7-0)

**原文标题**: [From 34% to 96%: The Porting Initiative Delivers - Hologram v0.7.0 - Hologram](https://hologram.page/blog/porting-initiative-delivers-hologram-v0-7-0)

Hologram v0.7.0 版本标志着 Elixir 到 JavaScript 移植计划取得重大进展，通过新增 150 个 Erlang 函数移植，将 Erlang 运行时覆盖率从 34% 大幅提升至 96%，同时 Elixir 标准库就绪度从 74% 增长到 87%。此版本包含超过 700 次提交，历时近 3 个月的集中开发，显著增强了浏览器端 Elixir 的功能，为构建全栈 Web 和基础本地优先应用奠定了基础。此外，版本还带来了编译加速、跨平台支持等多项改进与错误修复，并感谢了 49 位贡献者与赞助商的支持。

- 🚀 **Erlang 覆盖率跃升**：新移植 150 个 Erlang 函数，覆盖率从 34% 提升至 96%，Elixir 标准库就绪度达 87%。
- 🌐 **浏览器端功能扩展**：字符串处理、集合操作、数学计算、Unicode 规范化等众多 Elixir 标准库函数现可在浏览器中使用。
- ⚡ **性能与体验优化**：引入异步编译加速、NixOS 兼容性改进、OPFS 混合存储策略，修复了配额超限等多项错误。
- 👥 **社区贡献突出**：49 位贡献者参与，特别感谢 Michael Ward 等多位开发者完成复杂模块的移植工作。
- 🛠️ **基础设施增强**：为客户端 ERTS、ETS 支持等未来功能奠定基础，并改进了页面快照存储策略。
- 💖 **赞助商支持关键**：感谢 Curiosum、Erlang 生态系统基金会等赞助商对项目开发的持续支持与指导。

---

### [发布 v4.2.0 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.2.0)

**原文标题**: [Release v4.2.0 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.2.0)

Tailwind CSS 发布了 v4.2.0 版本，新增了多个颜色主题、实用工具类及 Webpack 插件，同时修复了多项问题并优化了性能。

- 🎨 新增了淡紫、橄榄、薄雾和灰褐四种颜色主题到默认调色板
- 📦 添加了 `@tailwindcss/webpack` 包，支持作为 Webpack 插件运行
- 🧱 新增了 `pbs-*`、`pbe-*`、`mbs-*`、`mbe-*` 等块级内边距和外边距实用工具
- 📏 引入了 `inline-*`、`block-*` 等内联尺寸和块尺寸相关工具类
- 🔧 新增了 `inset-s-*`、`inset-e-*` 等定位工具，并弃用了旧的 `start-*` 和 `end-*` 工具
- 🛠️ 修复了包括无限循环、类名提取、源映射注释等在内的多个问题
- ⚡ 通过减少文件系统遍历优化了 Oxide 扫描器在大型项目中的性能
- 📝 添加了对 Astro v5 导入别名和 Biome 格式化器的更好支持

---

### [GitHub - angular/angular: 自信地交付Web应用 🚀](https://github.com/angular/angular)

**原文标题**: [GitHub - angular/angular: Deliver web apps with confidence 🚀](https://github.com/angular/angular)

Angular 是一个用于构建移动端和桌面端 Web 应用的开发平台，基于 TypeScript/JavaScript 等语言，以其跨平台、高性能、可扩展性和强大的工具链而受到开发者欢迎。

- 🚀 **平台特性**：用于构建现代 Web 应用的开发平台，支持移动端和桌面端
- ⚙️ **技术栈**：主要使用 TypeScript/JavaScript，提供完整的开发生态
- 📚 **丰富文档**：官方文档网站提供从入门到高级的全面指南
- 🛠️ **开发工具**：包含 Angular CLI 命令行工具，简化项目创建和管理
- 🌍 **活跃社区**：拥有庞大的开发者社区，提供多种交流渠道和支持
- 📈 **项目规模**：GitHub 上获得 10 万星标，2.7 万分支，显示出广泛采用
- 🔄 **持续更新**：保持活跃开发，有详细的更新日志和升级指南
- 🤝 **开源协作**：采用 MIT 许可证，欢迎社区贡献，有完善的贡献指南
- 🎯 **核心优势**：跨平台、快速、可扩展、工具链完善，被数百万人使用

---

