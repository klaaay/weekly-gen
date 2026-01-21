### [JavaScript 周刊第 769 期：2026 年 1 月 20 日](https://javascriptweekly.com/issues/769)

**原文标题**: [JavaScript Weekly Issue 769: January 20, 2026](https://javascriptweekly.com/issues/769)

本期简报聚焦 JavaScript 生态的重要更新与行业动态，涵盖框架演进、工具发布及前沿观点。

- 🎉 jQuery 发布 4.0 版本，迁移至 ES 模块并放弃对旧版 IE 的支持
- 📊 SpreadJS 为 JavaScript 应用提供类 Excel 的电子表格功能
- ☁️ Astro 框架团队加入 Cloudflare，v6.0 测试版已上线
- ⚡ Electron 40.0 更新至 Chromium 144，Node.js v25.4.0 稳定支持`require(esm)`
- 🖥️ React Native Windows 0.81、Aurelia 2 RC 等多项工具发布新版本
- 🔍 深度技术文章探讨 ASCII 渲染原理及 Aspire 框架对 JavaScript 的一流支持
- 🛠️ 新工具包括 Starry Night 语法高亮库、Extension.js 浏览器扩展框架等
- 📈 行业动态涉及 VS Code 文档搜索系统、HTTP Archive 年度报告及 WebAssembly 现状分析

---

### [jQuery 4.0.0 | 官方 jQuery 博客](https://blog.jquery.com/2026/01/17/jquery-4-0-0/)

**原文标题**: [jQuery 4.0.0 | Official jQuery Blog](https://blog.jquery.com/2026/01/17/jquery-4-0-0/)

jQuery 团队在 2026 年 1 月 17 日发布了 jQuery 4.0.0 正式版，这是近 10 年来的首个主要版本更新。该版本包含多项现代化改进和破坏性变更，建议升级前详细阅读升级指南。大多数用户只需少量代码调整即可完成升级。

- 🎉 **发布里程碑**：jQuery 4.0.0 是 20 周年纪念版，距离上一个主要版本发布已近 10 年。
- 🗑️ **移除旧版支持**：放弃对 IE 10 及更旧版本、Edge Legacy、旧版 iOS/Android/Firefox 等浏览器的支持。
- 🔒 **安全增强**：新增对 Trusted Types 的支持，优化 AJAX 请求以避免 CSP 错误。
- 📦 **源码现代化**：源码从 AMD 迁移至 ES 模块，兼容现代构建工具和浏览器原生模块。
- 🧹 **清理废弃 API**：移除多个已废弃的辅助函数（如 `jQuery.isArray`、`jQuery.trim`），推荐使用原生等效方法。
- 🧩 **精简内部方法**：从 jQuery 原型中移除仅供内部使用的数组方法（`push`、`sort`、`splice`）。
- 👁️ **事件顺序标准化**：焦点事件顺序现在遵循 W3C 规范，不再覆盖浏览器原生行为。
- 🏗️ **更小的 Slim 构建**：移除了 Deferreds 和 Callbacks 模块，体积进一步缩小（gzip 后约 19.5KB）。
- 📥 **获取方式**：可通过 jQuery CDN、npm（`npm install jquery@4.0.0`）获取，同时提供标准版和 Slim 版。
- 🙏 **致谢贡献者**：感谢众多贡献者提交补丁、报告错误和参与测试，共同完成了此版本。

---

### [jQuery 网站使用统计与市场份额，2026 年 1 月](https://w3techs.com/technologies/details/js-jquery)

**原文标题**: [Usage Statistics and Market Share of jQuery for Websites, January 2026](https://w3techs.com/technologies/details/js-jquery)

该文章介绍了 jQuery 作为 JavaScript 库的使用统计数据、市场份额、版本分布、历史趋势、市场地位以及使用该技术的知名网站示例。

- 📊 jQuery 在所有已知 JavaScript 库的网站中使用率高达 88.8%，相当于全球网站的 70.9%
- 🔄 版本 3 是主流，占 jQuery 使用网站的 76.4%，而版本 1 和 2 分别占 18.9% 和 4.6%
- 📈 文章包含历史趋势分析，显示 jQuery 使用率随时间的变化情况
- 🏆 列举了使用 jQuery 的知名网站，包括 Microsoft.com、Yahoo.com 和 Wordpress.org 等
- 📝 提供技术比较，常与 React 和 Angular 进行对比，并可通过定制报告获取更多数据

---

### [GitHub - jquery/jquery-migrate：一款开发工具，用于帮助迁移已从或将从jQuery核心移除的API和功能](https://github.com/jquery/jquery-migrate/)

**原文标题**: [GitHub - jquery/jquery-migrate: A development tool to help migrate away from APIs and features that have been or will be removed from jQuery core](https://github.com/jquery/jquery-migrate/)

jQuery Migrate 是一个开发工具，旨在帮助开发者从 jQuery 核心中已移除或即将移除的 API 和功能平稳迁移，通过恢复这些 API 并在控制台显示警告来简化升级过程。

- 🛠️ **用途与功能**：作为 jQuery 的插件，用于在升级 jQuery 版本时保持向后兼容性，避免因 API 变更导致的错误，并提供控制台警告以辅助调试。
- 📦 **版本兼容性**：支持特定 jQuery 版本配对（如 jQuery 4.x 需搭配 Migrate 4.x），确保迁移过程顺畅。
- 🚀 **使用方法**：在网页中先加载 jQuery，再加载 jQuery Migrate 脚本，推荐使用生产版本（压缩无警告）或开发版本（含调试信息）。
- 🔧 **调试与控制**：提供如 `jQuery.migrateMessages`、`jQuery.migrateMute` 等 API，允许程序化管理警告和追踪迁移问题。
- 🐛 **问题反馈**：迁移相关错误应报告至 jQuery Migrate Issue Tracker，而 jQuery 核心错误则提交至 jQuery Core bug tracker。
- 🏗️ **开发与测试**：支持通过 npm 命令构建和运行测试，便于开发者本地验证和贡献代码。

---

### [你可能不需要 jQuery](https://youmightnotneedjquery.com/)

**原文标题**: [You Might Not Need jQuery](https://youmightnotneedjquery.com/)

本文探讨了在现代 Web 开发中，jQuery 并非总是必需的，并提供了大量原生 JavaScript 代码示例来替代 jQuery 的常见功能，帮助开发者根据项目需求选择合适的技术方案。

- 🧠 **核心观点**：jQuery 虽好，但开发库或针对现代浏览器时，可考虑使用原生 API 以减少依赖
- 🌐 **浏览器兼容性**：IE8+ 时代后，浏览器原生 API 已足够强大，兼容性问题大幅减少
- 🔄 **AJAX 替代方案**：展示了从 XMLHttpRequest 到现代 fetch API 的完整演进路径
- 🎨 **DOM 操作**：详细对比了元素选择、属性操作、样式修改等常见任务的 jQuery 与原生实现
- ⚡ **事件处理**：提供了事件绑定、委托、自定义事件等功能的原生替代方案
- 🛠️ **工具函数**：包含数组操作、对象扩展、类型判断等实用工具的原生实现
- 📱 **响应式设计**：针对不同浏览器版本提供了渐进增强的代码示例
- 🚀 **现代 API**：重点介绍了 ES6+ 新特性如箭头函数、模板字符串、展开运算符等的应用

---

### [JavaScript 电子表格库 | JS Excel 函数与公式 | SpreadJS](https://developer.mescius.com/spreadjs?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=SpreadJS-JS-Weekly-Primary-Sponsor-Jan-2026)

**原文标题**: [JavaScript Spreadsheet Library | JS Excel Functions and Formulas | SpreadJS](https://developer.mescius.com/spreadjs?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=SpreadJS-JS-Weekly-Primary-Sponsor-Jan-2026)

SpreadJS 是一款领先的 JavaScript 电子表格组件，提供超过 500 种 Excel 函数，无需依赖 Excel 即可在 Web 应用中实现完整的 Excel 式体验。它支持复杂的数据导入导出、强大的计算引擎、丰富的可视化功能，并可通过可选插件扩展 AI 助手、实时协作、数据透视表等高级能力。

- 📊 **全面的 Excel 兼容性**：支持导入/导出 .xlsx、.csv 等多种格式，提供与 Excel 高度一致的用户界面和功能体验。
- ⚡ **高性能计算引擎**：内置 500 多种函数，支持动态数组、迭代计算和自定义函数，可高效处理大规模数据和复杂计算。
- 🎨 **丰富的数据可视化**：提供 30 多种图表类型、迷你图、条件格式、切片器等工具，便于创建交互式仪表板和报表。
- 🔧 **灵活的单元格控制**：支持多种单元格类型、下拉列表、数据验证、富文本、条形码等，可构建复杂的数据输入表单。
- 🤖 **AI 与智能功能**（可选插件）：通过自然语言生成公式、解释逻辑、进行数据洞察，并支持智能数据透视表布局。
- 👥 **实时协作**（可选插件）：基于 OT 技术实现多用户同时编辑，支持用户状态显示和权限控制。
- 📈 **专业领域扩展**（可选插件）：提供数据透视表、甘特图、报表设计器、数据图表等专业模块，满足金融、工程、项目管理等场景需求。
- 🌐 **全球化与本地化**：支持多语言界面和计算函数本地化，可轻松适配不同区域的应用需求。
- 🛠️ **便捷的开发集成**：提供无代码设计器、完整的 API 以及详细的文档，支持快速集成到 Angular、React、Vue 等前端框架中。

---

### [错误](https://javascriptweekly.com/link/179447/web)

**原文标题**: [Error](https://javascriptweekly.com/link/179447/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/179447/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [天文](https://astro.build/)

**原文标题**: [Astro](https://astro.build/)

Astro 6 Beta 现已进入测试阶段，这是一个专为构建内容驱动型网站而优化的 JavaScript 框架，以其卓越的性能和灵活性著称。

- 🚀 **服务器优先架构**：通过服务器端渲染组件并发送轻量级 HTML，实现零冗余 JavaScript 的极速加载。
- 📄 **内容驱动设计**：支持从文件系统、外部 API 或任何 CMS 无缝加载内容，适应多样化的内容源。
- 🛠️ **高度可定制**：可集成主流 UI 框架（如 React、Vue、Svelte）以及 CSS 库、主题等工具，无锁定风险。
- 📊 **顶尖性能表现**：采用“群岛架构”优化页面加载，在真实网站中 Core Web Vitals 达标率高达 62%，领先于其他框架。
- 🖼️ **内置强大功能**：包含内容集合、零 JavaScript 默认输出、视图过渡、图像优化、文件路由等全套现代网站开发工具。
- 🌐 **灵活部署选项**：提供一键配置适配器，支持 Netlify、Vercel、AWS 等多种云平台和托管服务。
- 🧩 **丰富生态系统**：提供多种预制主题（电商、博客、文档等）和专业机构支持，助力快速启动项目。

---

### [Astro 6 Beta | Astro](https://astro.build/blog/astro-6-beta/)

**原文标题**: [Astro 6 Beta | Astro](https://astro.build/blog/astro-6-beta/)

Astro 6 Beta 发布，带来重新设计的开发服务器、显著的渲染性能提升，以及针对 CSP、字体和实时内容集合的新内置 API。此次更新使开发与生产环境更接近，特别增强了对 Cloudflare Workers 的支持，并稳定了实时内容集合和 CSP 功能。

- 🚀 **开发服务器重构**：利用 Vite 环境 API，使开发与生产环境使用相同运行时，提升稳定性和跨平台支持。
- ☁️ **Cloudflare Workers 增强**：开发时直接使用 workerd 运行时，支持 Durable Objects、KV 等真实平台 API，改进错误提示和预览功能。
- 🔄 **实时内容集合稳定**：支持动态数据源（如实时股价），无需重建即可更新内容，提供明确的错误处理机制。
- 🛡️ **内容安全策略（CSP）稳定**：默认启用 CSP 防护，可自定义策略，兼容所有官方适配器，自动生成安全标头。
- ⚠️ **重大变更与迁移**：移除旧 API，要求 Node 22+，更新集成接口和 Cloudflare 适配器，升级至 Zod 4。
- 🧪 **测试与反馈**：当前为 Beta 版，鼓励用户测试 workerd 支持并提供反馈，以优化稳定版本。

---

### [时间游乐场 - 学习 JavaScript Temporal API](https://temporal-playground.vercel.app/)

**原文标题**: [Temporal Playground - Learn the JavaScript Temporal API](https://temporal-playground.vercel.app/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理系统自动化处理病历、排班等流程，减轻医护行政负担
- ⚠️ 数据隐私保护与算法透明度仍是亟待解决的技术伦理问题
- 🔮 未来 AI 或将在远程医疗与预防性健康管理领域发挥更大作用

---

### [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

**原文标题**: [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

Temporal 是 JavaScript 中用于处理日期和时间的新 API，旨在完全替代传统的 Date 对象。它提供了更强大的功能，包括内置时区和日历支持、时间转换、算术运算和格式化等。Temporal 不是构造函数，所有属性和方法都是静态的，类似于 Math 对象。它通过多个类提供超过 200 个实用方法，支持更精确和灵活的时间管理。

- 🕐 **替代 Date 对象**：Temporal 旨在解决 Date 对象的缺陷，如时区处理不足、日历系统单一和易用性问题。
- 🌍 **时区与日历支持**：内置多时区处理和多种日历系统（如 Gregorian、Hebrew、Chinese 等），支持无时区的日历日期和挂钟时间。
- 🧩 **模块化 API 设计**：通过多个类（如 Instant、ZonedDateTime、PlainDate 等）分别处理时间点、时区日期、纯日期和时间等不同场景。
- 🔄 **丰富的操作方法**：支持时间算术（加减、比较）、舍入、序列化和类间转换，确保灵活的时间计算和格式化。
- 📅 **日历系统细节**：支持年、月、日、周等多种日历组件，包括闰年、闰月和文化特定的周规则，避免常见假设错误。
- 📏 **时间范围限制**：所有 Temporal 对象可表示的日期范围约为 ±1 亿天（从 Unix 纪元起），确保时间数据的有效性和一致性。
- 🔧 **静态工具类**：包括 Duration（时间间隔）、Now（当前时间）等实用类，简化时间差计算和实时获取。
- 📜 **RFC 9557 格式兼容**：使用基于 ISO 8601 的标准化字符串格式进行序列化和反序列化，支持微秒和纳秒精度。

---

### [影响 Svelte 生态系统的 CVE 漏洞](https://svelte.dev/blog/cves-affecting-the-svelte-ecosystem)

**原文标题**: [CVEs affecting the Svelte ecosystem](https://svelte.dev/blog/cves-affecting-the-svelte-ecosystem)

Svelte 生态系统发布了针对五个安全漏洞的补丁，涉及 devalue、svelte、@sveltejs/kit 和@sveltejs/adapter-node 等包，用户需立即升级至指定安全版本以防范潜在攻击。

- 🚨 **立即升级**：devalue 升至 5.6.2、svelte 升至 5.46.4、@sveltejs/kit 升至 2.49.5、@sveltejs/adapter-node 升至 5.5.1，依赖包已同步更新
- 🛡️ **漏洞详情**：包括 devalue 解析器内存耗尽 DoS、SvelteKit 远程函数反序列化内存放大攻击、预渲染功能 SSRF 与 DoS 风险，以及 svelte 可水合键的 XSS 漏洞
- 🔍 **影响范围**：漏洞影响特定版本，需结合用户输入解析、远程函数启用或预渲染路由等条件才可能被利用
- 🤝 **致谢与改进**：感谢安全研究人员和 Vercel 团队协助披露与修复，未来将加强代码审查流程以预防类似问题
- 📢 **报告渠道**：发现 Svelte 相关漏洞可通过仓库 Security 标签或 Svelte 主库私下报告

---

### [未找到标题](https://x.com/rough__sea/status/2013280952370573666)

**原文标题**: [No title found](https://x.com/rough__sea/status/2013280952370573666)

该页面提示 JavaScript 未启用，导致无法正常使用 X 平台（原 Twitter），并提供了相应的解决建议和支持信息。

- 🚫 JavaScript 未启用，导致 X 平台功能受限
- 🌐 建议启用 JavaScript 或更换支持的浏览器
- 🔧 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致问题，建议暂时禁用
- 📄 页面底部包含服务条款、隐私政策等法律链接

---

### [Electron 40.0.0 | Electron](https://www.electronjs.org/blog/electron-40-0)

**原文标题**: [Electron 40.0.0 | Electron](https://www.electronjs.org/blog/electron-40-0)

Electron 40.0.0 已发布，包含 Chromium、V8 和 Node.js 的版本升级，引入了多项新功能与改进，同时包含一些破坏性变更。

- 🚀 升级核心组件：Chromium 至 144.0.7559.60，Node.js 至 v24.11.1，V8 至 14.4
- ✨ 新增功能：包括内存回收原因标识、HDR 色彩空间支持、硬件加速检测、自定义协议处理选项等
- 🔧 改进特性：增强无障碍支持管理、外部共享纹理导入、系统强调色获取、文件系统 API 状态持久化等
- ⚠️ 破坏性变更：渲染进程中剪贴板 API 已弃用，macOS dSYM 文件改用 tar.xz 压缩，Electron 37.x.y 停止支持
- 📅 后续计划：团队将继续跟进 Chromium、Node 和 V8 的主要组件开发，维护项目时间线

---

### [Node.js — Node.js 25.4.0（当前版本）](https://nodejs.org/en/blog/release/v25.4.0)

**原文标题**: [Node.js — Node.js 25.4.0 (Current)](https://nodejs.org/en/blog/release/v25.4.0)

Node.js 25.4.0 版本发布，包含多项功能更新、稳定性改进、依赖项升级及性能优化，并新增了若干协作成员。

- 🚀 CLI 新增 `--require-module` 和 `--no-require-module` 选项，并标记 `--heapsnapshot-near-heap-limit` 为稳定功能
- 🔐 加密模块更新根证书至 NSS 3.117，提升安全性
- 📦 模块系统将 `require(esm)` 和模块编译缓存标记为稳定，并允许以 `#/` 开头的子路径导入
- 🌐 HTTP 模块新增 `http.setGlobalProxyFromEnv()` 方法，便于全局代理设置
- ⚡ 事件模块扩展 `events.listenerCount()` 以支持 EventTargets
- 🔧 工具模块新增 `util.convertProcessSignalToExitCode` 实用函数
- 📈 多项性能优化，包括断言、缓冲区和字符串编码的改进
- 🛠️ 构建系统支持 Visual Studio 2026，并新增多项配置标志
- 📚 文档更新，新增协作成员并修正多处错误描述
- 🧪 测试框架修复和增强，包括测试运行器的改进
- 🔄 依赖项升级，包括 npm 11.7.0、V8 引擎和多个第三方库

---

### [🚀React Native Windows v0.81 正式发布！！React Native](https://devblogs.microsoft.com/react-native/%f0%9f%9a%80react-native-windows-v0-81-is-here/)

**原文标题**: [🚀React Native Windows v0.81 is here!! React Native](https://devblogs.microsoft.com/react-native/%f0%9f%9a%80react-native-windows-v0-81-is-here/)

React Native Windows v0.81 正式发布，此版本与 React Native 0.81.5 对齐，默认启用了新的 Fabric 架构，带来了性能提升、开发者工具增强（包括 Hermes 调试器支持）、组件功能改进以及更高的稳定性。此次更新标志着向新架构的全面迁移，旧有的 Paper 架构将从 v0.82 开始被弃用。

- 🧵 **Fabric 架构现已默认启用**：从 v0.80 开始，新架构（Fabric 渲染器）已成为默认选项，它通过 JSI、TurboModules 等技术提升了应用性能与响应速度。Paper 架构将在 v0.82 被弃用并最终移除。
- 🔥 **v0.81 的新特性**：引入了 Hermes 调试器支持，为 Windows 开发者提供了与 Android/iOS 对等的调试体验（包括断点、性能分析、React 组件检查）。此外，修复了模态框崩溃问题，并为 ScrollView 和 TextInput 等组件增强了事件处理与滚动控制功能。
- ⚙️ **组件功能增强**：ScrollView 新增了对齐与间隔滚动属性；TextInput 增加了键盘控制、滚动、焦点等多项新属性；Text 组件改进了文本截断显示；Fabric 架构下的可访问性功能也得到显著提升。
- 📊 **功能兼容性进展**：新架构（Fabric）在核心组件属性上已达到与旧架构（Paper）约 95%-98% 的兼容度，主要组件如 View、Image 等已近乎完全兼容。鼓励开发者迁移至新架构，并检查第三方库的兼容性。
- 🏁 **示例应用与迁移指南**：提供了从 Paper 迁移到 Fabric 的详细指南，并更新了 Gallery 示例应用以并排展示两种架构。同时，一个 AI 图像分类器示例应用演示了如何升级至 v0.81 并采用新架构。
- 🚨 **重要提醒**：升级至 v0.81 需使用 Node.js 22.14.0 或更高版本。未来所有开发重点都将集中于新架构，建议所有项目尽快迁移。

---

### [Aurelia 2 候选版本发布：终于来临 | Aurelia](https://aurelia.io/blog/2026/1/14/aurelia-2-release-candidate/)

**原文标题**: [Aurelia 2 Release Candidate: It's Finally Happening | Aurelia](https://aurelia.io/blog/2026/1/14/aurelia-2-release-candidate/)

经过多年的 Alpha 版本、27 个 Beta 版本、全球疫情、团队变动以及数不清的 GitHub 提交，Aurelia 2 终于达到了发布候选（RC）阶段。这标志着 API 已稳定，适合用于生产环境，且后续不会有破坏性变更。虽然功能上与此前的 Beta 版本相似，但 RC 版本更强调稳定性和开发信心。项目升级与新建都更为简便，社区贡献者获得了感谢，并为新老开发者提供了支持与迁移指南。

- 🎉 Aurelia 2 历经多年开发与 27 个 Beta 版本后，正式进入发布候选（RC）阶段
- 🔒 RC 意味着 API 已稳定，可安全用于生产环境，无需担心破坏性变更
- 📈 主要变化并非新功能，而是版本号所代表的稳定性与开发信心
- ⚙️ 包含 SSR 和 hydration 的基础支持，重复组件性能优化，及自定义属性绑定的定义调整
- 🚀 可通过`npx makes aurelia`新建项目，或使用`npm install aurelia@rc`升级现有项目
- 🙏 感谢社区长期支持，并为 Aurelia 1 用户提供迁移指南，欢迎新开发者加入
- 🎊 邀请社区共同庆祝，并鼓励开始构建新项目

---

### [发布 v2.6.5 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.6.5)

**原文标题**: [Release v2.6.5 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.6.5)

Deno 2.6.5 版本于 2026 年 1 月 15 日发布，包含多项功能增强、错误修复和性能改进，涉及 Canvas、Web API、Node.js 兼容性、网络、安全等多个模块。

- 🖼️ 新增 Canvas 扩展支持 GIF 和 WebP 格式的 `createImageBitmap`
- 📊 Web 扩展添加 `performance.clearResourceTimings()` 和 `setResourceTimingBufferSize()` 方法
- 🔄 Node.js 文件系统模块实现 `FileHandle.readableWebStream()` 功能
- 🛡️ 修复审计功能中 `--level` 标志对退出代码的影响
- 🔧 多项错误修复，涵盖网络代理、资源回收、TLS 证书、子进程参数验证等
- 📦 npm 模块依赖图去重优化，提升解析效率
- 🚀 修复任务运行中基于信号的子进程退出代码处理
- 🐛 解决 TypeScript 编译、WebGPU API 暴露及动态导入队列等多个问题

---

### [ASCII 字符并非像素：深入探讨 ASCII 渲染技术](https://alexharri.com/blog/ascii-rendering)

**原文标题**: [ASCII characters are not pixels: a deep dive into ASCII rendering](https://alexharri.com/blog/ascii-rendering)

本文探讨了 ASCII 字符渲染技术，重点介绍了如何通过考虑字符形状而非将其视为像素来提升渲染质量，并详细介绍了形状向量、对比度增强等关键方法。

- 🎨 作者开发了一个图像转 ASCII 渲染器，通过利用字符形状实现边缘锐化，解决了传统方法中边缘模糊的问题。
- 🔍 传统 ASCII 渲染将字符视为像素，采用最近邻采样和超采样，但忽略了字符形状，导致边缘模糊和锯齿。
- 📐 通过量化字符形状为多维向量（如 6D 形状向量），并基于形状向量进行最近邻搜索，可以更精确地匹配字符与图像区域。
- ⚙️ 引入对比度增强技术，包括全局和定向对比度增强，以提升不同颜色区域之间的分离度和可读性。
- 🚀 为提高性能，作者采用了 k-d 树加速字符查找，并通过 GPU 加速采样和对比度增强处理，实现了流畅的动画渲染。
- 📚 文章还附带了字符查找性能优化和 GPU 加速的附录，展示了实际应用中的技术细节和挑战。

---

### [JavaScript 开发者的追求 | Aspire 博客](https://devblogs.microsoft.com/aspire/aspire-for-javascript-developers/)

**原文标题**: [Aspire for JavaScript developers | Aspire Blog](https://devblogs.microsoft.com/aspire/aspire-for-javascript-developers/)

Aspire 13 为 JavaScript 和 TypeScript 开发者提供了原生支持，使其能够作为分布式应用开发的一等公民，享受与 .NET 应用同等的开发、调试和部署体验。

- 🎉 **JavaScript 成为一等公民**：Aspire 13 通过 `Aspire.Hosting.JavaScript` 包，为 JavaScript/TypeScript 应用提供全面的编排支持，不再是次要集成。
- 📦 **三种运行方式**：提供 `AddJavaScriptApp()`（运行 npm 脚本）、`AddNodeApp()`（直接运行 Node.js 脚本）和 `AddViteApp()`（针对 Vite 前端框架）三种方法，适应不同场景。
- 🔧 **包管理器全面支持**：默认支持 npm，并可轻松切换为 Yarn 或 pnpm，自动根据锁文件优化生产环境安装命令（如使用 `npm ci` 或 `--frozen-lockfile`）。
- ⚙️ **高度可定制**：允许自定义运行/构建脚本、传递参数、指定 Vite 配置文件，并支持通过环境变量（如 `PORT`）配置网络端点。
- 🔗 **自动服务发现**：JavaScript 应用可无缝参与 Aspire 的服务发现，通过环境变量自动获取后端服务地址，无需硬编码。
- 🗄️ **灵活的数据库连接**：提供 URI 和独立连接属性两种格式的连接字符串，兼容 Prisma、TypeORM、node-postgres 等主流数据库库。
- 🐳 **生产就绪的 Docker 支持**：自动生成优化的多阶段 Dockerfile，支持 BuildKit 缓存挂载以加速构建，并默认使用非 root 用户运行以确保安全。
- 🔒 **HTTPS 与证书管理**：Vite 应用可便捷配置 HTTPS，Aspire 会通过非侵入式的包装配置文件处理证书，而不修改原始 `vite.config.js`。
- 📁 **构建产物共享**：支持通过“容器文件”功能在容器间共享构建产物（如前端静态资源），便于后端服务直接托管前端。
- 🚀 **增强的开发体验**：集成 OpenTelemetry 提供可观测性，自动设置 `NODE_ENV`，支持 Vite 的热模块替换，并全面支持 TypeScript 项目。

---

### [Aspire —— 您的技术栈，精简高效](https://aspire.dev/)

**原文标题**: [Aspire â Your stack, streamlined](https://aspire.dev/)

Aspire 13.1 已正式发布，这是一个面向开发者的免费开源平台，旨在通过代码定义和编排应用栈，实现前端、API、容器和数据库的无缝集成与部署，并提供开箱即用的可观测性。

- 🚀 **版本发布**：Aspire 13.1 已正式发布，带来新功能和改进。
- 🛠️ **核心特性**：通过代码定义应用栈，实现类型安全、可读性强的架构编排，支持本地运行和任意环境部署。
- 🔌 **模块化与扩展性**：无需重写代码即可编排各类服务，并可灵活扩展以适应不同技术栈。
- 📊 **内置可观测性**：集成 OpenTelemetry，自动提供日志、追踪和健康检查，简化调试流程。
- ☁️ **灵活部署**：支持 Kubernetes、云平台或本地部署，适应多种环境，确保一致性。
- 🌐 **多语言支持**：兼容 C#、Java、Python、JavaScript、TypeScript、Go 等多种编程语言。
- 💻 **本地优先**：在本地模拟生产环境，减少“在我机器上能运行”的问题，实现平滑部署。
- 🔍 **集成生态**：支持 Azure、AWS 等云平台及自定义基础设施，拥有丰富的集成库。
- 👥 **社区驱动**：作为免费开源项目，拥有活跃的社区，并获得开发者积极评价。

---

### [Aspire 13 新特性 | Aspire](https://aspire.dev/whats-new/aspire-13/)

**原文标题**: [What's new in Aspire 13 | Aspire](https://aspire.dev/whats-new/aspire-13/)

Aspire 13 标志着 Aspire 产品线的一个重要里程碑，它已从一个 .NET 编排工具转变为一个真正的多语言应用平台。此版本将 Python 和 JavaScript 提升为与 .NET 并列的一等公民，并引入了全新的构建、发布和部署范式。

- 🚀 **平台重塑**：从“.NET Aspire”简化为“Aspire”，成为一个全面的多语言应用平台。
- 🐍 **一等 Python 支持**：支持 Python 模块、Uvicorn 部署、灵活的包管理（uv、pip 或 venv）以及自动生成生产 Dockerfile。
- ⚛️ **一等 JavaScript 支持**：支持 Vite 和基于 npm 的应用，具备包管理器自动检测、调试支持和基于容器的构建流水线。
- 🔗 **多语言基础设施**：连接属性（URI、JDBC、独立属性）和证书信任机制可在任何语言和容器中工作。
- 📦 **容器文件作为构建产物**：构建输出变为容器而非文件夹，实现了可重现、隔离和可移植的构建。
- 🛠️ **全新 `aspire do` 平台**：用于构建、发布和部署流水线，支持并行执行、依赖跟踪和可扩展的工作流。
- 💻 **现代化 CLI**：新增 `aspire init` 命令用于“Aspire 化”现有应用，并改进了跨运行记住配置的部署状态管理。
- 🧩 **VS Code 扩展**：简化 Aspire 开发，提供项目创建、集成管理、多语言调试和部署命令。
- 🌐 **新家与社区**：新官网 aspire.dev 成为文档、入门指南和社区资源的中心枢纽，要求 .NET 10 SDK 或更高版本。

---

### [Wallaby - 集成 AI 的测试运行器，编辑器内即时反馈](https://wallabyjs.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Wallaby - AI-Ready Test Runner with Instant Feedback in Your Editor](https://wallabyjs.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

Wallaby.js 是一款实时 JavaScript/TypeScript 测试运行工具，可在编码时即时运行测试并显示结果，提供智能调试、AI 集成和高效测试反馈，显著提升开发效率。

- 🚀 **实时测试反馈**：输入代码时即时运行测试，结果直接显示在代码旁，无需手动保存或运行。
- 🔍 **智能调试功能**：支持时间旅行调试和运行时值查看，快速定位和修复问题，不中断开发流程。
- ⚡ **高效测试执行**：仅运行受代码更改影响的最小测试集，通常只需运行单个测试，速度极快。
- 🤖 **AI 工具集成**：通过 MCP 服务器为 AI 助手提供实时测试结果、运行时值和覆盖率数据，辅助代码编写和调试。
- 🔓 **无锁定设计**：作为现有测试框架和 IDE 的插件，无供应商或框架锁定，可独立运行测试。
- 📊 **实时代码覆盖率**：编辑器边栏实时显示测试覆盖率，清晰标识已覆盖、部分覆盖和未覆盖的代码行。
- 🛠️ **选择性测试运行**：支持仅运行当前工作的测试文件，大幅提升大型项目的测试效率。
- 📈 **性能分析与洞察**：提供测试性能分析、差异对比和快照管理，帮助优化代码和测试策略。
- 💬 **用户高度评价**：被众多开发者和公司誉为提升生产力和测试体验的必备工具，尤其适合 TDD 实践。

---

### [介绍<geolocation> HTML 元素  |  博客  |  Chrome 开发者](https://developer.chrome.com/blog/geolocation-html-element)

**原文标题**: [Introducing the <geolocation> HTML element  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/geolocation-html-element)

Chrome 144 引入了新的 `<geolocation>` HTML 元素，旨在通过声明式、用户主动触发的体验来改进网站请求位置数据的方式，减少代码量并提升用户意图的明确性，从而避免浏览器干预。

- 🌐 **从通用 `<permission>` 到专用 `<geolocation>`**：该元素是“页面嵌入式权限控制”倡议的最新发展，最初作为通用元素提出，后根据反馈演变为针对特定功能的专用元素。
- ✅ **概念验证成功**：在 Chrome 126 至 143 版本进行的原始试验显示，使用该元素能显著减少错误并提高成功率，例如 Zoom 的捕获错误减少了 46.9%。
- 🔧 **重新设计实现**：根据浏览器厂商反馈，从通用权限控制转向了针对特定功能的专用元素（如 `<geolocation>`），其核心功能从管理权限状态转变为充当数据中介。
- 🆚 **与传统 API 的对比**：与传统的 Geolocation JavaScript API 相比，新元素通过用户点击触发，浏览器角色从决定提示转变为数据中介，简化了开发流程。
- 🎯 **使用新元素的优势**：解决了上下文缺失问题，确保请求严格由用户发起，带来明确意图、简化恢复流程和自动刷新数据三大优势。
- 💻 **简化实现**：集成该元素所需的样板代码远少于 JavaScript API，开发者只需添加标签并监听 `onlocation` 事件即可。
- 🎨 **样式约束**：为确保用户信任和防止欺骗性设计，该元素在颜色对比度、尺寸、间距和视觉效果等方面有特定的样式限制。
- 📱 **渐进增强策略**：该元素设计为优雅降级，不支持它的浏览器会将其视为未知元素，开发者可以轻松提供自定义回退方案。
- 🧪 **演示与填充工具**：提供了在线演示页面，展示了其主要配置；同时，开发者也可以使用填充工具来在不支持该元素的浏览器中模拟其功能。
- 🔍 **功能检测**：可以通过检查 `'HTMLGeolocationElement'` 是否存在于 `window` 对象中来编程检测浏览器支持情况。
- 🚀 **未来展望**：`<geolocation>` 元素代表了向针对特定功能、更符合用户实际使用习惯的 HTML 元素的转变，Chrome 144 也同时开启了用于摄像头和麦克风的 `<usermedia>` 元素的原始试验。

---

### [Bun 自举启动](https://walters.app/blog/bootstrapping-bun)

**原文标题**: [Bootstrapping Bun](https://walters.app/blog/bootstrapping-bun)

本文描述了作者在完全不依赖 Bun 自身二进制文件的情况下，成功构建 Bun JavaScript 工具链的完整过程。从尝试安装 OpenCode 时发现 Bun 在主流 Linux 发行版中缺乏官方包支持开始，作者深入探索了 Bun 构建系统的自举难题，最终通过一系列技术方案实现了从零构建。

- 🚀 **动机与挑战**：因 OpenCode 安装困难而尝试构建 Bun，发现其构建系统严重依赖自身二进制，缺乏官方自举文档。
- 🔍 **探索方法**：初期使用包装脚本记录 Bun 调用，后期结合代码分析，明确了构建过程依赖 Bun 的三大功能：包管理、TypeScript 运行时和打包工具。
- 📦 **包管理替代**：将构建脚本中的`bun install`替换为 npm，通过 CMake 选项支持自定义 npm 路径，并重构了`cppbind.ts`的依赖安装逻辑。
- 🛠️ **TypeScript 运行时替代**：将 Bun 特有的 API（如`Bun.file`）迁移到 Node.js 的`node:fs`模块，并利用 Node.js v22.18+ 的类型剥离功能直接运行 TypeScript 脚本。
- 🧩 **打包工具替代**：用 esbuild 替换`bun build`，处理构建时的代码打包与转译任务，适配了大多数配置选项。
- ⚙️ **Zig 编译器适配**：为使用上游 Zig 而非 Bun 定制分支，移除了对私有结构体字段的依赖，并通过静态库编译解决了符号导出问题。
- 🐛 **运行时调试**：构建出的二进制文件运行失败，通过自编译 JavaScriptCore 并添加日志，发现打包后处理阶段错误添加了`})`导致脚本语法错误。
- ✅ **成功构建**：最终实现了完全自举的构建命令，并创建了 PKGBUILD 打包脚本，成功运行 OpenCode。
- 📤 **上游贡献**：已向 Bun 维护者提交 RFC，希望整合这些改进，但理解其涉及构建系统重大变更，可能不被采纳。

---

### [使用 GSAP 构建滚动驱动的双波浪文字动画 | Codrops](https://tympanus.net/codrops/2026/01/15/building-a-scroll-driven-dual-wave-text-animation-with-gsap/)

**原文标题**: [Building a Scroll-Driven Dual-Wave Text Animation with GSAP | Codrops](https://tympanus.net/codrops/2026/01/15/building-a-scroll-driven-dual-wave-text-animation-with-gsap/)

本文介绍了如何使用 GSAP 创建基于滚动的双列波浪文字动画，通过正弦波数学实现平滑的波浪效果，并同步更新中心图像。

- 🌊 动画特点：双列文字以相反的波浪模式移动，使用 GSAP 的 quickTo 实现基于物理的平滑过渡，中心图像根据焦点文字更新，波浪参数（速度、频率）可配置，并适配不同屏幕尺寸。
- 🏗️ 技术栈：使用 Vite 构建，GSAP 的 ScrollTrigger 和 ScrollSmoother 驱动动画，支持响应式设计。
- 📐 结构设计：HTML 包含 ScrollSmoother 包装器、双列文字、中心图像容器及数据属性配置，CSS 使用 Flexbox 布局和视口相对单位确保响应性。
- ⚙️ 平滑滚动设置：通过 ScrollSmoother 或 Lenis 实现流畅滚动，确保动画与滚动输入同步，避免卡顿。
- 🧮 波浪动画实现：JavaScript 类 DualWaveAnimation 计算波浪位置，使用 quickTo 优化性能，根据滚动进度更新文字位置和图像，并通过数学公式控制波浪频率和速度。
- 🖼️ 图像同步：中心图像根据焦点文字动态更新，允许溢出以确保在滚动时保持居中，避免不必要的 DOM 更新。
- 🔧 可配置性：通过数据属性或程序化选项调整波浪参数，支持自定义以适应不同设计需求。

---

### [技术讲座：优化窗口调整大小行为 | Electron](https://www.electronjs.org/blog/tech-talk-window-resize-behavior)

**原文标题**: [Tech Talk: Improving Window Resize Behavior | Electron](https://www.electronjs.org/blog/tech-talk-window-resize-behavior)

本文介绍了修复 Electron 和 Chromium 在 Windows 系统上窗口调整大小时出现旧帧残留问题的过程。通过深入分析 Chromium 的图形堆栈，发现该问题源于 DirectComposition API 中视口与裁剪矩形更新不同步，以及历史遗留的帧尺寸不匹配处理逻辑。最终通过两个补丁分别解决了这两个问题，并已成功回移植到 Electron 39 和 40 版本中。

- 🐛 **问题发现**：在 Windows 上调整窗口大小时，旧帧内容会短暂残留显示，影响用户体验。
- 🔍 **问题定位**：通过实验发现该问题也存在于 Google Chrome 中，表明根源在 Chromium 而非 Electron，且仅出现在 Windows 特定图形后端（ANGLE Direct3D 11）。
- 🛠️ **调试过程**：利用 Chromium 的调试标志（如`--tint-composited-content`）追踪图形输出，确定问题出在显示合成器（viz）的 DirectComposition 路径。
- 🎯 **第一个 Bug**：DirectComposition 中视口重绘与裁剪矩形更新操作因 Windows API 异步执行而不同步，导致未重绘区域显示旧像素。解决方案是在调整大小时将视口外区域绘制为透明。
- 📏 **第二个 Bug**：历史遗留的帧尺寸优化逻辑在窗口与帧尺寸不匹配时，会错误扩展渲染通道尺寸而不更新实际绘制区域，造成残留像素。修复方法是调整视口和裁剪矩形以匹配实际帧尺寸。
- ⚙️ **修复实施**：两个补丁已提交至 Chromium 代码库，并回移植到 Electron 39.2.6 及更高版本，Google Chrome 预计于 2026 年 2 月包含此修复。
- 🙏 **致谢**：感谢 Plasticity 的资金支持以及 Chromium 团队的技术协助，使得这一复杂问题得以解决。

---

### [获取失败](https://javascriptweekly.com/link/179467/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/179467/web)

无法总结：获取内容失败，状态码 403。

---

### [GitHub - wooorm/starry-night：语法高亮，类似GitHub](https://github.com/wooorm/starry-night)

**原文标题**: [GitHub - wooorm/starry-night: Syntax highlighting, like GitHub](https://github.com/wooorm/starry-night)

starry-night 是一个开源的高质量语法高亮库，模仿 GitHub 的 PrettyLights 项目，支持 600 多种编程语言，使用 TextMate 语法，并生成带有 CSS 类的 AST 结构，适用于服务器端和浏览器端。

- 🌟 **开源替代**：starry-night 是 GitHub 闭源语法高亮器 PrettyLights 的开源版本，提供相似的高质量代码高亮效果。
- 🧩 **多语言支持**：支持超过 600 种编程语言的语法高亮，包括常见语言和许多小众语言，语法文件基于 TextMate。
- 🏗️ **AST 输出**：库生成抽象语法树（AST）而非直接 HTML，便于集成到 React、Vue 等虚拟 DOM 框架或进行自定义处理。
- 🌐 **跨平台使用**：可在 Node.js、Deno 和浏览器中运行，通过 ESM 导入，并包含 WASM 依赖以实现高性能。
- 🎨 **主题与 CSS**：提供多种 CSS 主题（如浅色、深色、色盲友好等），支持自动暗色模式切换，样式文件小巧。
- 📦 **灵活打包**：提供 `common`（约 35 种常用语言）和 `all`（全部语言）两种语法包，也可手动选择特定语言以控制体积。
- 🔧 **丰富 API**：包括创建高亮实例、注册语法、高亮代码、查找语法作用域等功能，并支持检测缺失的语法依赖。
- 🔗 **生态集成**：可与 unified、remark、rehype、markdown-it 等工具链集成，方便在 Markdown 处理流程中添加代码高亮。
- ⚖️ **体积考量**：核心库加 WASM 约 185 kB，但语法文件较大，需根据使用场景权衡选择以优化加载性能。
- 🔒 **安全许可**：核心代码使用 MIT 许可证，包含的语法文件均采用宽松许可证（如 MIT、Apache-2.0），详细信息在 notice 文件中列出。

---

### [星空之夜语法高亮演示](https://peterc.org/misc/starrydemo.html)

**原文标题**: [Starry Night Syntax Highlighting demo](https://peterc.org/misc/starrydemo.html)

这段内容展示了三种编程语言的简单代码示例，分别演示了基本功能实现。

- 🌟 JavaScript 示例：定义了一个问候函数，并演示了数组映射操作
- 🐍 Python 示例：展示了斐波那契数列的递归实现和列表推导式
- 🌐 HTML 示例：包含基础网页结构，展示容器、标题和段落元素

---

### [Extension.js](https://extension.js.org/)

**原文标题**: [Extension.js](https://extension.js.org/)

该工具旨在简化跨浏览器扩展的开发流程，支持多种现代技术，无需配置即可快速构建。

- 🛠️ 支持跨所有主流浏览器平台开发扩展
- 📘 内置对 TypeScript、WebAssembly 和下一代 JavaScript 的支持
- ⚙️ 无需配置即可开始开发
- 📚 提供详细文档供查阅
- ⭐ GitHub 项目获得超过 4000 星标
- 🔍 包含浏览器测试功能

---

### [GitHub - extension-js/extension.js: 🧩 跨浏览器扩展框架](https://github.com/extension-js/extension.js)

**原文标题**: [GitHub - extension-js/extension.js: 🧩 The cross-browser extension framework](https://github.com/extension-js/extension.js)

这是一个名为 Extension.js 的跨浏览器扩展框架，它简化了浏览器扩展的开发流程，支持多种现代技术和主流浏览器。

- 🧩 **跨浏览器支持**：无需手动配置即可开发、构建和预览适用于 Chrome、Edge、Firefox 等浏览器的扩展。
- 🚀 **快速启动**：通过`npx extension@latest create`命令快速创建新扩展，或基于现有示例（如 Chrome 扩展示例）开始开发。
- 🔧 **灵活集成**：支持现有扩展项目，只需安装 Extension.js 包并链接 npm 脚本即可使用其开发、构建和预览功能。
- 🌐 **技术栈广泛**：兼容 ESNext、TypeScript、WASM（即将推出），并支持 React、Vue、Svelte、Preact 等前端框架。
- ⚙️ **自定义浏览器**：开发时可指定浏览器类型或使用自定义的 Chromium/Gecko 二进制文件进行测试。
- 📜 **开源许可**：采用 MIT 许可证，由 Cezar Augusto 及贡献者维护，拥有 4.5k 星标和活跃的社区支持。

---

### [Pintura 图像编辑器，一款强大的 JavaScript 图像编辑器 SDK](https://pqina.nl/pintura/?ref=cooperpress)

**原文标题**: [Pintura Image Editor, a Powerful JavaScript Image Editor SDK](https://pqina.nl/pintura/?ref=cooperpress)

Pintura Image Editor 是一款功能强大的 JavaScript 图像编辑器 SDK，支持跨平台和多种框架集成，提供丰富的图像编辑功能，旨在帮助开发者快速集成并提升用户上传图像的质量。

- 🖼️ **强大的图像编辑功能**：支持裁剪、旋转、调整大小、滤镜、注释、颜色调整等多种编辑操作。
- 📱 **跨平台兼容性**：在移动设备和桌面端均表现直观，支持响应式设计和多触点交互。
- 🔧 **高度可配置**：提供丰富的配置选项，可自定义界面语言、图标、编辑控件及输出格式。
- 🚀 **快速集成**：支持与主流前端框架（如 React、Vue、Angular）及文件上传库（如 Dropzone、FilePond）无缝集成。
- 💡 **提升用户体验**：通过强制裁剪比例、叠加裁剪指南、自动水印等功能，帮助用户上传更优质的图片。
- ⚙️ **高效性能**：支持浏览器端图像压缩、格式转换，减少服务器带宽占用，提升上传速度。
- 🛠️ **扩展性强**：可集成 AI 服务（如背景移除、生成式 AI），并支持视频编辑扩展。
- 🌍 **广泛信任**：已被全球 3,202 家公司使用，获得高度评价，平均评分 4.9/5。
- 💰 **无风险试用**：提供 60 天退款保证，确保产品符合项目需求。

---

### [React Aria](https://react-aria.adobe.com/)

**原文标题**: [React Aria](https://react-aria.adobe.com/)

React Aria 是一个无样式的 React UI 组件库，提供高度可定制、可访问且支持国际化的组件，适用于构建现代 Web 应用。

- 🎨 **样式自由**：组件默认无样式，支持使用 CSS、Tailwind、Styled Components 等多种方案自定义设计。
- 🧩 **组件模块化**：每个组件拆分为独立部分，提供状态、渲染属性和插槽，便于样式定制。
- 📱 **全设备优化**：组件针对鼠标、触摸、键盘和屏幕阅读器进行优化，确保跨平台一致体验。
- ♿ **无障碍优先**：遵循 W3C ARIA 标准，经过多设备和屏幕阅读器测试，支持移动端无障碍交互。
- 🌍 **国际化支持**：内置 30 多种语言翻译，支持多日历系统、数字格式和右到左布局。
- ⚙️ **灵活 API**：提供从高阶组件到底层 Hook 的多层级 API，支持自定义模式和深度控制。
- 🔧 **高级功能**：支持拖放、键盘多选、表单验证、表格列调整等复杂交互。
- 🛠️ **样式复用与组合**：通过上下文和组合 API，可共享样式或构建自定义交互模式。

---

### [GitHub - unadlib/localspace: 一个将 IndexedDB、localStorage 及其他存储 API 统一为一致接口的库](https://github.com/unadlib/localspace)

**原文标题**: [GitHub - unadlib/localspace: A library that unifies the APIs of IndexedDB, localStorage and other storage into a consistent API](https://github.com/unadlib/localspace)

localspace 是一个现代化的存储工具库，它在保持与 localForage API 完全兼容的同时，提供了 TypeScript 原生支持、async/await 语法、性能优化和可扩展的插件系统，旨在解决社区长期以来的痛点。

- 🚀 **现代化重构**：基于 TypeScript 和现代 JavaScript 模式重建，消除了历史技术债务，同时保持 API 完全兼容。
- 🔌 **插件化架构**：提供 TTL、加密、压缩、多标签同步和配额管理等插件，可按需组合，扩展性强。
- ⚡ **性能优化**：支持批量操作（`setItems`/`getItems`）和可选的写入合并（Coalesced Writes），可将 IndexedDB 高频写入性能提升 3-10 倍。
- 🔄 **多驱动支持**：默认支持 IndexedDB 和 localStorage，可配置驱动顺序和回退策略，并支持自定义驱动。
- 🛡️ **强类型与错误处理**：提供完整的 TypeScript 类型定义和结构化的错误信息（`LocalSpaceError`），便于调试。
- 📦 **跨平台兼容**：支持浏览器、Node.js、React Native 和 Electron 等环境，并计划集成更多存储后端（如 OPFS、SQLite）。
- 🔧 **高级功能**：支持事务（`runTransaction`）、存储桶（Storage Buckets）、连接预热和可配置的持久性提示。
- 📚 **平滑迁移**：提供兼容模式以无缝迁移现有 localForage 代码，并详细说明了行为差异和升级指南。

---

### [GitHub - localForage/localForage: 💾 离线存储，优化升级。通过简洁而强大的 API 封装 IndexedDB、WebSQL 或 localStorage。](https://github.com/localForage/localForage)

**原文标题**: [GitHub - localForage/localForage: 💾 Offline storage, improved. Wraps IndexedDB, WebSQL, or localStorage using a simple but powerful API.](https://github.com/localForage/localForage)

localForage 是一个快速简单的 JavaScript 存储库，通过封装 IndexedDB、WebSQL 或 localStorage，提供类似 localStorage 的 API 以增强 Web 应用的离线体验。它支持异步操作、多种数据格式存储，并兼容多种框架和模块系统。

- 💾 **离线存储改进**：封装 IndexedDB、WebSQL 或 localStorage，提供强大而简单的 API
- 📦 **简单集成**：通过单个 JavaScript 文件或 npm 安装即可使用
- 🔄 **双 API 支持**：同时支持回调函数和 Promise，推荐使用 Promise 或 async/await
- 🗂️ **多类型存储**：支持字符串、Blobs、TypedArrays 及可序列化的 JS 对象，自动处理 JSON 转换
- ⚙️ **灵活配置**：可配置数据库驱动、名称、大小等，支持创建多个独立存储实例
- 🌐 **广泛兼容**：兼容 RequireJS 和 TypeScript，并提供 Angular、Vue 等框架的存储驱动
- 🧪 **测试与贡献**：提供完整的测试套件，支持自定义驱动，鼓励社区贡献
- 📄 **开源许可**：基于 Apache-2.0 许可证发布，由 Mozilla 及贡献者维护

---

### [发布 v2.2.0 · processing/p5.js · GitHub](https://github.com/processing/p5.js/releases/tag/v2.2.0)

**原文标题**: [Release v2.2.0 · processing/p5.js · GitHub](https://github.com/processing/p5.js/releases/tag/v2.2.0)

p5.js 发布了 2.2.0 版本，主要引入了 WebGPU 渲染支持作为核心附加功能，并包含多项文档改进和 p5.strands 的错误修复。

- 🎨 新增 WebGPU 渲染模式，需通过特定脚本标签加载并在 `createCanvas` 中启用
- 🔧 修复了 p5.strands 中的逻辑表达式处理、分支赋值及压缩代码下的过滤器问题
- 🐛 解决了 WebGPU 缓冲区内存泄漏、字体测量及相机插值等多个错误
- 📚 包含对 `p5.Graphics` 对象、`shuffle()` 类型及文本索引缓冲区的支持与修复
- 👥 多位新贡献者加入，共同完成了此版本的更新

---

### [p5.js 中的 WebGPU - Dave Pagurek](https://www.davepagurek.com/blog/p5-webgpu/)

**原文标题**: [
    WebGPU in p5.js - Dave Pagurek
  ](https://www.davepagurek.com/blog/p5-webgpu/)

全球各地庆祝新年伊始，展望未来一年。

- 🎆 世界各地跨年活动迎接 2026 年
- 📅 新年象征新的开始与希望
- 🌍 不同文化以独特传统庆祝元旦
- 🎯 个人与社群常设定新年目标
- 🕰️ 时间标记促进反思与前瞻规划

---

### [p5.js/contributor_docs/webgpu.md 位于 dev-2.0 分支 · processing/p5.js · GitHub](https://github.com/processing/p5.js/blob/dev-2.0/contributor_docs/webgpu.md)

**原文标题**: [p5.js/contributor_docs/webgpu.md at dev-2.0 · processing/p5.js · GitHub](https://github.com/processing/p5.js/blob/dev-2.0/contributor_docs/webgpu.md)

p5.js 是一个开源的创意编程库，基于 Processing 语言开发，专为艺术家、设计师和教育工作者设计，用于简化图形和交互式应用的开发。

- 🎨 基于 Processing 语言，专注于创意编程和视觉艺术
- 🔓 开源项目，拥有活跃的社区和丰富的协作功能
- 📊 项目数据：获得 23.4k 星标、3.7k 复刻，管理 369 个议题和 113 个拉取请求
- 🛠️ 提供代码托管、议题追踪、项目管理等开发工具
- ⚠️ 当前页面加载遇到错误，需要重新加载以访问完整内容
- 🔔 通知设置需登录账户进行调整

---

### [发布 v1.29.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.29.0)

**原文标题**: [Release v1.29.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.29.0)

该版本 v1.29.0 主要新增了对 MPEG 传输流（.ts）文件的读写支持，这是实现 HLS 功能的关键步骤，同时包含多项格式处理改进与错误修复。

- 🚀 新增 MPEG-TS 解复用器与复用器，支持 AVC、HEVC、AAC 和 MP3 格式
- 📦 新增`MpegTsOutputFormat`、`MpegTsInputFormat`等相关模块导出
- ⏱️ 新增`Input.getFirstTimestamp()`方法，可获取所有轨道的最小起始时间戳
- 🔧 `EncodedPacket.clone()`现支持修改数据包的多数属性（不仅限时间戳和时长）
- 🛠️ 修复`ConversionOptions.trim.start`默认值逻辑，现自动匹配输入文件首时间戳
- 📁 ISOBMFF、Matroska 和 ADTS 复用器现可正确接收 ADTS 格式的 AAC 输入
- 🔊 ADTS 解复用器简化重构，现直接输出 ADTS 格式音频数据包
- ⚙️ Ogg 复用器现支持生成合法的零数据包文件
- 📊 `TrackCountLimits`返回的轨道数上限值由`Infinity`调整为实际数值边界

---

### [示例 | Mediabunny](https://mediabunny.dev/examples)

**原文标题**: [Examples | Mediabunny](https://mediabunny.dev/examples)

从输入媒体文件中提取多种元数据信息。

- 📁 提取文件格式与编码信息
- 🎬 获取音视频时长与分辨率参数
- 📊 分析比特率与采样率技术数据
- 🔍 识别编解码器与媒体流结构
- 📝 收集创建时间与版权元信息

---

### [Prettier 3.8：支持 Angular v21.1 · Prettier](https://prettier.io/blog/2026/01/14/3.8.0)

**原文标题**: [Prettier 3.8: Support for Angular v21.1 · Prettier](https://prettier.io/blog/2026/01/14/3.8.0)

Prettier 3.8 版本正式发布，全面支持 Angular v21.1 的新特性，包括在模板中连续使用 `@case` 语句和展开元素，并新增了在 Markdown 代码块中格式化 Angular 语法的功能。

- 🎉 **支持 Angular v21.1 新特性**：Prettier 3.8 完全兼容 Angular v21.1 的最新功能，提供更清晰、更具表达力的模板格式化。
- 🔄 **连续 `@case` 语句支持**：在 `@switch` 块中，现在可以连续使用多个 `@case` 语句，Prettier 3.8 能正确格式化这些语法，避免之前的语法错误。
- 📋 **展开元素格式化**：支持在数组字面量、对象字面量和函数调用中使用展开元素（`...`），Prettier 3.8 能自动优化其格式，提升代码可读性。
- 📝 **Markdown 代码块支持**：新增在 Markdown 代码块中格式化 Angular 语法的能力，使得在文档或注释中嵌入 Angular 代码时也能保持整洁格式。
- 🛠️ **其他改进**：包括优化单模板或字符串字面量属性值的换行打印，进一步提升 Angular 模板的格式化效果。

---

### [Angular 21.1：核心特性与改进亮点 - Angular.love](https://angular.love/angular-21-1-key-features-and-improvements/)

**原文标题**: [Angular 21.1: Key Features and Improvements - Angular.love](https://angular.love/angular-21-1-key-features-and-improvements/)

Angular 21.1 带来了多项增强开发者体验和应用能力的新特性，包括模板编译改进、信号表单优化、路由器功能增强以及多项性能与安全修复。

- 🧩 **模板编译增强**：支持 `switch` 语句的多条件匹配和展开运算符，减少代码重复，提升模板表达力。
- 📝 **信号表单更新**：`[field]` 指令更名为 `[formField]`，功能保持不变，同时改进了自定义控件支持和异步验证。
- 🧭 **路由器功能扩展**：实验性集成 Navigation API，引入自动注入器清理和新的 `isActive()` 信号函数，提升导航控制和内存管理。
- 🛠️ **开发体验优化**：新增 `provideStabilityDebugging()` 工具帮助调试应用稳定性，编译器类型安全和错误检测得到加强。
- 🔧 **性能与安全修复**：修复了动画和事件重放的内存泄漏问题，增强了 SVG 元素的安全性，并改进了图像加载器的自定义转换支持。

---

### [日志带](https://logtape.org/)

**原文标题**: [LogTape](https://logtape.org/)

一个简洁、尊重用户配置的日志库，默认静默，仅在用户主动配置时输出日志。

- 🎯 默认静默，不干扰用户
- 🔧 无需配置即无日志输出
- 📚 专为库开发者设计
- 🤝 尊重用户环境与偏好

---

### [logtape/CHANGES.md 位于主分支 · dahlia/logtape · GitHub](https://github.com/dahlia/logtape/blob/main/CHANGES.md#version-200)

**原文标题**: [logtape/CHANGES.md at main · dahlia/logtape · GitHub](https://github.com/dahlia/logtape/blob/main/CHANGES.md#version-200)

这是一个 GitHub 仓库页面，显示加载错误，并提供了基本的仓库信息和导航选项。

- 🔄 页面加载时出现错误，提示重新加载
- 📊 仓库拥有 1.5k 星标和 38 个分支
- 🐛 当前有 5 个未解决的问题和 6 个拉取请求
- 🔒 页面包含代码、安全、动态等多个导航部分
- 👥 用户需要登录才能更改通知设置

---

### [GitHub - iamstevendao/vue-tel-input: Vue 国际电话输入组件](https://github.com/iamstevendao/vue-tel-input)

**原文标题**: [GitHub - iamstevendao/vue-tel-input: International Telephone Input with Vue](https://github.com/iamstevendao/vue-tel-input)

这是一个用于 Vue.js 的国际电话号码输入组件，支持 Vue 2 和 Vue 3，提供丰富的配置选项和异步加载功能。

- 🌍 **国际电话输入**：专为 Vue.js 设计的国际电话号码输入组件，支持全球号码格式
- 📦 **安装便捷**：通过 npm 安装，支持 Vue 2（legacy 版本）和 Vue 3
- ⚙️ **配置灵活**：提供多种配置选项，包括输入模式（自动/国际）和全局设置
- 🚀 **性能优化**：支持组件懒加载，可异步加载约 200KB 的 JS 和 100KB 的 CSS 资源
- 🔧 **开发友好**：提供完整的开发环境配置，支持 TypeScript 和现代构建工具
- 📄 **文档齐全**：包含详细的使用文档、演示网站和安装指南
- ⭐ **社区活跃**：GitHub 上有 858 个星标、360 个分支，被 3000 多个项目使用
- 📝 **开源许可**：采用 MIT 许可证，由 Steven Dao 开发和维护

---

### [Vue 电话输入 | Vue 电话输入](https://iamstevendao.com/vue-tel-input/)

**原文标题**: [Vue Tel Input | Vue Tel Input](https://iamstevendao.com/vue-tel-input/)

一款用于 Vue.js 的国际电话输入组件，由开发者社区精心打造。

- 📞 专为 Vue.js 框架设计的国际电话号码输入组件
- 🌍 支持全球国家代码和电话号码格式
- ❤️ 由开发者社区贡献和维护的开源项目
- ⚙️ 提供可自定义的配置选项
- 🔧 包含详细的功能演示和文档说明

---

### [GitHub - Niekes/d3-3d：d3-3d 是一个专为三维可视化设计的强大 JavaScript 库，特别优化以与 d3.js 无缝协作。该库能够将三维数据投影到网页浏览器中，使其成为热衷于创建沉浸式和动态可视化效果的开发者不可或缺的工具。](https://github.com/Niekes/d3-3d)

**原文标题**: [GitHub - Niekes/d3-3d: d3-3d is a powerful JavaScript library designed for 3D visualizations, specifically tailored to work seamlessly with d3.js. This library enables the projection of 3D data onto web browsers, making it an essential tool for developers interested in creating immersive and dynamic visualizations.](https://github.com/Niekes/d3-3d)

d3-3d 是一个专为 d3.js 设计的 JavaScript 库，用于在浏览器中实现 3D 数据可视化，支持多种 3D 形状的投影与渲染。

- 📦 **专为 d3.js 设计** – 与 d3.js 无缝集成，用于在浏览器中投影和渲染 3D 数据。
- 🛠️ **丰富的形状支持** – 提供点、线、三角形、平面、多边形、网格平面和立方体等多种 3D 形状。
- ⚙️ **灵活的配置 API** – 支持设置坐标访问器、旋转、缩放、投影原点和旋转中心等参数。
- 🔄 **自动计算属性** – 为所有形状自动计算质心、旋转后坐标、投影坐标和方向（ccw）。
- 📐 **正射投影** – 使用浏览器的坐标系和正射投影将 3D 数据映射到 2D 屏幕。
- 🧩 **TypeScript 原生支持** – 提供完整的类型定义，支持泛型以安全处理自定义数据类型。
- 🎨 **SVG 路径生成** – 通过 `.draw()` 方法为支持的形状生成 SVG 路径字符串。
- 📊 **深度排序工具** – 提供 `sort()` 实用函数，用于按深度正确排序形状（画家算法）。
- 📄 **易于安装与使用** – 可通过 npm、CDN 或直接下载获取，并附有详细示例和 API 文档。

---

### [GitHub - jonahsnider/convert：最小且最快的库，用于在TypeScript和JavaScript中实现真正简单、完全类型安全的单位转换。](https://github.com/jonahsnider/convert)

**原文标题**: [GitHub - jonahsnider/convert: The smallest & fastest library for really easy, totally type-safe unit conversions in TypeScript & JavaScript.](https://github.com/jonahsnider/convert)

Convert 是一个用于 TypeScript 和 JavaScript 的最小且最快的库，提供简单、完全类型安全的单位转换功能。

- 📦 支持多种单位转换，包括长度、数据、体积、质量、温度等，并具有完整的构建时和运行时验证
- ⚡ 极快的性能，每秒可处理超过 300 万次转换调用，且无任何依赖
- 🌐 兼容所有环境（浏览器、Node、Bun 等），并具有完整的 ES3 向后兼容性
- 📐 提供`convertMany`功能，支持复合单位字符串转换（如"1d8h"）
- 🎯 支持自动转换为最佳单位，并可指定使用公制或英制系统
- 📄 提供`ms`简写功能，便于持续时间与毫秒之间的转换
- 📦 可通过 npm、yarn 或 CDN 轻松安装，支持 ESM 和 CommonJS 模块

---

### [发布 v4.0.0 · DoneDeal0/superdiff · GitHub](https://github.com/DoneDeal0/superdiff/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · DoneDeal0/superdiff · GitHub](https://github.com/DoneDeal0/superdiff/releases/tag/v4.0.0)

该内容是关于 superdiff 项目 v4.0.0 版本的发布信息，主要包含重大变更说明，涉及 API 命名统一和简化输出格式的调整。

- 🚀 **版本发布**：superdiff v4.0.0 版本于 2024 年 1 月 19 日发布，旨在提升开发者体验。
- 🔧 **API 变更**：移除了`isEqual`和`isObject`公共方法，统一了所有差异比较函数的命名规范。
- 📝 **命名调整**：`getListDiff`和`getStreamDiff`中`newIndex`改为`index`，`prevIndex`改为`previousIndex`，并移除了`indexDiff`。
- 🔑 **键名更新**：`getObjectDiff`中`property`改为`key`，`currentValue`改为`value`，同时`referenceProperty`选项更名为`referenceKey`。
- ⚠️ **影响说明**：这些变更为破坏性更改，但改动最小，仅需代码库中小幅更新即可适配。

---

### [jasmine/jasmine · GitHub 主分支上的 jasmine/release_notes/6.0.0.md](https://github.com/jasmine/jasmine/blob/main/release_notes/6.0.0.md)

**原文标题**: [jasmine/release_notes/6.0.0.md at main · jasmine/jasmine · GitHub](https://github.com/jasmine/jasmine/blob/main/release_notes/6.0.0.md)

Jasmine 是一个流行的 JavaScript 测试框架，用于前端代码的单元测试，具有活跃的开源社区支持。

- 🚀 **项目活跃度高** - 拥有 15.8k 星标和 2.2k 复刻，显示其广泛采用和社区贡献
- 🧪 **专注测试领域** - 专为 JavaScript 测试设计，帮助开发者编写可靠的单元测试
- 🔄 **持续开发维护** - 设有 11 个议题和 2 个拉取请求，表明项目正在积极改进中
- 🛡️ **重视安全性** - 设有专门的安全页面，关注代码安全实践
- 📚 **完善的项目管理** - 包含代码、议题、讨论、行动、维基等多个管理模块
- ⚠️ **偶发技术问题** - 页面加载时可能出现错误，需要重新加载解决
- 🔔 **用户参与要求** - 更改通知设置需要用户登录，保障账户安全

---

### [为您的 SaaS 服务快速添加 API 密钥支持](https://clerk.com/blog/add-api-key-support-to-your-saas-with-clerk?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=01-20-26&dub_id=oqLeeSNb3dQJdc3P)

**原文标题**: [Add API Key support to your SaaS in minutes](https://clerk.com/blog/add-api-key-support-to-your-saas-with-clerk?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=01-20-26&dub_id=oqLeeSNb3dQJdc3P)

本文介绍了如何利用 Clerk 平台快速为 SaaS 应用添加多租户 API 密钥功能，简化了密钥管理、权限控制和后端路由保护等复杂流程。

- 🔑 **启用 Clerk API 密钥**：在 Clerk 仪表板中启用组织 API 密钥，并配置相关权限（如`org:sys_api_keys:read`和`org:sys_api_keys:manage`），以支持多租户场景下的密钥管理。
- 🖥️ **集成密钥管理界面**：通过 Clerk 提供的`<OrganizationProfile/>`或`<APIKeys/>`组件，在 SaaS 仪表板中快速添加用户友好的 API 密钥管理界面，支持生成、查看和撤销密钥。
- 🛡️ **保护后端路由**：使用 Clerk 的`auth()`助手配置 API 路由，同时接受会话令牌和 API 密钥（通过`acceptsToken: ['session_token', 'api_key']`），并自动验证组织 ID 以确保多租户数据隔离。
- 🧪 **测试 API 密钥功能**：通过 cURL 或工具（如 Postman）测试 API 密钥的创建、列表和删除操作，验证密钥的有效性、组织范围权限及错误处理机制。
- 🚀 **快速部署与扩展**：Clerk 简化了 API 密钥的基础设施建设，使开发者能够专注于产品逻辑，同时为客户提供安全、可靠的集成能力。

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

Meticulous AI 是一款通过记录用户交互自动生成并维护端到端测试的工具，旨在帮助开发者无需手动编写测试即可全面覆盖应用功能，提升开发效率和代码质量。

- 🚀 **自动生成测试**：通过记录开发、预演等环境中的用户交互，AI 自动生成覆盖所有代码分支和用户流程的测试套件。
- 🔄 **持续演进**：测试套件随应用更新自动调整，新增功能时自动添加测试，过时测试自动移除，无需人工维护。
- ⚡ **高效无干扰**：测试执行快速并行，支持数千页面在 120 秒内完成；通过模拟后端响应实现无副作用测试，避免误报。
- 🛡️ **稳定可靠**：基于 Chromium 构建的确定性调度引擎，从根本上消除测试波动，适用于复杂应用。
- 🔗 **灵活集成**：可单独使用或与现有测试套件结合，支持 NextJS、React、Vue、Angular 等多种前端框架。
- 📈 **企业认可**：已被 Dropbox、Notion、Lattice 等超过 100 家组织采用，有效预防回归问题并提升开发信心。

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

该内容是一个用户注册界面，展示了 Auth0 平台提供的免费注册服务及其主要功能。

- 📧 注册需要提供邮箱并选择所在国家/地区
- 🌍 支持全球众多国家/地区的用户注册
- 🔐 提供多种登录方式：GitHub、Google、Microsoft 账户直接登录
- 📄 注册需同意服务条款和隐私政策
- 🆓 免费套餐包含每月 2.5 万活跃用户额度
- ⚙️ 提供可定制的注册和登录流程
- 🤖 新增 AI 代理连接外部应用功能，敏感操作需人工批准
- 🔗 支持自定义社交登录和无密码连接
- 🛡️ 具备暴力破解防护和渐进式画像功能（含 5 个操作和表单）
- 👨‍💻 专为各阶段开发者设计

---

### [构建 docfind：使用 Rust 与 WebAssembly 实现快速客户端搜索](https://code.visualstudio.com/blogs/2026/01/15/docfind)

**原文标题**: [Building docfind: Fast Client-Side Search with Rust and WebAssembly](https://code.visualstudio.com/blogs/2026/01/15/docfind)

本文介绍了 VS Code 团队开发的 docfind，这是一个完全在浏览器中运行的客户端搜索引擎，利用 WebAssembly 和 Rust 实现快速、紧凑的搜索体验，无需服务器支持。

- 🚀 **快速搜索**：docfind 提供即时响应的搜索体验，类似 VS Code 的 Quick Open 功能，查询速度约 0.4 毫秒。
- 🧩 **技术组合**：结合有限状态转换器（FST）进行高效关键词查找、RAKE 算法提取关键词，以及 FSST 压缩字符串，实现紧凑索引。
- 🌐 **纯客户端方案**：索引嵌入单个 WebAssembly 模块中，用户访问网站时下载，无需服务器交互或 API 密钥。
- 🔧 **构建流程**：通过 CLI 工具将文档转换为索引文件，并嵌入预编译的 WASM 模板，支持动态更新而无需重新编译。
- 🤖 **AI 辅助开发**：作者利用 GitHub Copilot 代理和 Next Edit Suggestions 功能，高效克服 Rust 和 WebAssembly 二进制操作的技术挑战。
- 📊 **实际效果**：VS Code 文档网站索引约 5.9MB（未压缩），经 Brotli 压缩后约 2.7MB，支持约 3,700 个文档的快速搜索。
- 🛠️ **开源可用**：docfind 已开源，用户可通过简单命令安装，并为自己的静态网站生成搜索索引，需自行实现结果展示界面。

---

### [GitHub - microsoft/docfind：一款基于Rust构建、支持WebAssembly的高性能文档搜索引擎。](https://github.com/microsoft/docfind)

**原文标题**: [GitHub - microsoft/docfind: A high-performance document search engine built in Rust with WebAssembly support.](https://github.com/microsoft/docfind)

Docfind 是一款由微软开发的高性能文档搜索引擎，采用 Rust 语言构建并支持 WebAssembly，旨在实现快速、高效的模糊搜索与紧凑的存储。

- 🚀 **高性能搜索**：基于有限状态转换器（FST）实现快速模糊匹配，支持 Levenshtein 距离，搜索速度可达每查询 1-3 毫秒。
- 📦 **紧凑存储**：采用 FSST 压缩技术，显著减少索引大小（如示例中 17.14 MB 数据压缩至 5.20 MB），同时保持快速解压。
- 🌐 **浏览器端运行**：可编译为 WebAssembly，在浏览器中直接执行搜索，无需服务器支持，并提供在线演示。
- 🔧 **便捷工具链**：提供独立 CLI 工具，可从文档集合直接生成 .wasm 文件，无需 Rust 工具链，支持快速安装。
- 📄 **智能关键词提取**：集成 RAKE 算法，自动从文档内容中提取重要短语，并根据来源（元数据、标题、正文）分配相关性分数。
- ⚙️ **高效工作流程**：索引构建阶段提取关键词并压缩文档，嵌入阶段将索引集成到 WASM 模块，搜索阶段按需解压并返回排序结果。
- 📚 **丰富生态借鉴**：参考了 Algolia、Lunr.js 等现有搜索技术，结合 FST、FSST 和 RAKE 等核心算法，优化性能与压缩比。

---

### [docfind - 快速文档搜索演示](https://microsoft.github.io/docfind/)

**原文标题**: [docfind - Fast Document Search Demo](https://microsoft.github.io/docfind/)

docfind 是一个 AI 驱动的文档处理工具，能够快速解析、搜索和管理各种格式的文档，提升信息处理效率。

- 📄 **智能解析**：自动提取文档中的关键信息，支持多种格式如 PDF、Word 等。
- 🔍 **高效搜索**：通过自然语言快速定位文档内容，节省查找时间。
- 🗂️ **分类管理**：智能归类文档，便于组织和检索。
- 🤖 **AI 辅助**：利用人工智能技术优化文档处理流程，提高准确性。
- ⚡ **快速处理**：批量处理文档，大幅提升工作效率。

---

### [2025 年网络年鉴](https://almanac.httparchive.org/en/2025/)

**原文标题**: [The 2025 Web Almanac](https://almanac.httparchive.org/en/2025/)

《2025 年网络年鉴》是 HTTP Archive 发布的年度网络状态综合报告，结合原始数据与行业专家见解，涵盖页面内容、用户体验、发布与分发等 15 个主题章节。

- 📊 报告基于 HTTP Archive 对 1620 万个网站的月度测试数据，处理量达 244TB  
- 🔍 SEO 章节指出：AI 搜索时代基础网络技术依然稳固，仅 2.1% 移动站点使用 llms.txt 文件  
- 🔒 HTTPS 采用率稳步提升至约 92%，较往年 89% 实现重要进展  
- 🏗️ 半数网页已采用结构化数据，增强内容可发现性  
- 👥 由 70 位志愿者协作完成，涵盖规划、研究、写作到制作的完整流程

---

### [WebAssembly | 2025 | HTTP Archive 网络年鉴](https://almanac.httparchive.org/en/2025/webassembly)

**原文标题**: [WebAssembly | 2025 | The Web Almanac by HTTP Archive](https://almanac.httparchive.org/en/2025/webassembly)

WebAssembly 已从网页技术演变为高性能通用字节码格式，2025 年底发布 Wasm 3.0 标志着其生态在浏览器与独立环境中的显著发展。该技术致力于为云端、边缘计算、区块链及物联网提供安全基础，通过 WASI 和组件模型实现跨语言互操作。2025 年数据显示，约 0.35% 桌面网站使用 Wasm，高流量网站采用率更高，且模块大小差异显著（最小仅 2KB，最大超 200MB）。.NET 生态（含 Blazor）是主要开发语言，但超 40% 模块因代码混淆无法识别来源。SIMD 等新特性使用量大幅增长，反映 Wasm 正成为跨平台应用的主流运行时。

- 🚀 **技术演进**：WebAssembly 于 2019 年成为 W3C 标准，2025 年发布 3.0 版本，从网页技术扩展为通用高性能字节码格式。
- 🌍 **跨平台使命**：获得谷歌、微软等巨头支持，通过 WASI 和组件模型实现云端、边缘设备等跨基础设施安全代码执行。
- 📊 **采用现状**：2025 年约 0.35% 桌面网站使用 Wasm，高流量网站采用率显著，体现“幂律分布”特征。
- 📦 **模块特征**：模块大小两极分化，最小仅 2KB（微实用工具），最大超 200MB（如 Photoshop 网页版）；超 90% 请求使用正确 MIME 类型。
- ⚙️ **技术生态**：.NET 生态（含 Blazor）占比最高（约 40%），但 41% 模块因代码混淆无法识别语言来源；SIMD 等新特性使用量较 2021 年增长超 60 倍。
- 🔮 **未来展望**：正从网页技术转型为主流跨平台运行时，在无服务器计算、机器学习等场景应用持续扩大。

---

### [性能 | 2025 | HTTP Archive 网络年鉴](https://almanac.httparchive.org/en/2025/performance)

**原文标题**: [Performance | 2025 | The Web Almanac by HTTP Archive](https://almanac.httparchive.org/en/2025/performance)

本文分析了 2025 年网页性能的现状，重点关注核心网页指标（Core Web Vitals）的进展、挑战及新兴技术。数据显示，网页加载速度、交互性和视觉稳定性整体呈改善趋势，但移动端与桌面端、不同流行度网站之间仍存在性能差距。新兴性能特性如早期提示（Early Hints）和推测规则（Speculation Rules）的采用率仍然较低。

- 📈 **核心网页指标持续改善**：2025 年，48% 的移动网站和 56% 的桌面网站达到了良好的核心网页指标标准，移动端性能逐年提升。
- 📱 **移动与桌面性能差距**：在加载速度（LCP）和交互性（INP）方面，移动端仍显著落后于桌面端，但交互性差距正在缩小。
- 🏆 **热门网站表现更优**：排名前 1000 的网站性能改善最为明显，尤其在交互性（INP）方面，从 2024 年的 53% 提升至 2025 年的 63%。
- 🏠 **首页性能挑战**：首页的加载速度（LCP）和视觉稳定性（CLS）通常比次级页面差，可能因为首页内容更动态、复杂。
- 🖼️ **图像仍是性能关键**：图像是最常见的最⼤内容绘制元素，但格式优化（如采用 WebP）和尺寸定义（避免布局偏移）的采用仍然缓慢。
- ⚡ **交互性显著提升**：移动网站的交互到下次绘制指标从 2024 年的 74% 提升至 2025 年的 77%，但总阻塞时间（TBT）却大幅增加，表明 JavaScript 执行负担加重。
- 📐 **视觉稳定性进步**：81% 的移动页面达到了良好的累积布局偏移标准，但仍有大量页面存在未定义尺寸的图像和非合成动画，导致布局偏移风险。
- 🚀 **新兴特性采用率低**：早期提示和推测规则等高级性能优化技术的采用率普遍低于 6%，表明部署复杂性和工具集成度是主要障碍。
- 🔄 **性能优化不均**：最流行的网站倾向于手动优化复杂交互，而长尾网站则更多依赖平台（如 WordPress）内置的自动化优化工具。
- 📊 **测量标准趋同**：随着更多浏览器支持核心网页指标（如 INP），跨浏览器的用户体验测量将变得更加一致和可比。

---

### [页面权重 | 2025 | HTTP Archive 网络年鉴](https://almanac.httparchive.org/en/2025/page-weight)

**原文标题**: [Page Weight | 2025 | The Web Almanac by HTTP Archive](https://almanac.httparchive.org/en/2025/page-weight)

本文分析了 2025 年网页重量（页面大小）的现状与趋势，指出尽管网络带宽不断提升，但页面大小持续增长，对性能、可访问性、环境及用户体验产生负面影响。数据显示，中位数桌面首页已达 2.9 MB，移动首页为 2.6 MB，其中图像和 JavaScript 是主要贡献者。页面重量与核心网页指标（如 LCP、CLS、INP）呈负相关，重量越大，通过率越低。文章还探讨了 AI 爬虫、用户和发布者面临的挑战，并提出了压缩、最小化、缓存等技术优化建议，强调当前优化机会未被充分利用，页面重量问题仍在加剧。

- 📈 **页面重量持续增长**：中位数桌面首页重量达 2.9 MB，移动首页为 2.6 MB，自 2015 年以来增长超过 100%。
- 🖼️ **图像与 JavaScript 占主导**：图像是最大字节贡献者（桌面首页约 1,058 KB），JavaScript 次之（桌面首页约 697 KB），且 98.1% 的页面使用 JavaScript。
- 📉 **性能影响显著**：页面重量与核心网页指标（LCP、CLS、INP）通过率负相关，重量越大，用户体验越差，移动设备受影响更严重。
- 🌍 **可访问性与环境成本**：重量增加加剧数字鸿沟，对低速网络和低端设备用户不友好，同时增加数据传输的能源消耗和碳足迹。
- 🤖 **AI 爬虫面临挑战**：重量增加导致爬虫能耗上升，可能使 AI 系统偏向轻量内容，影响 JavaScript 密集型网站的索引覆盖。
- 🛠️ **优化技术采用不足**：仅约 71% 的页面正确使用文本压缩，约 61% 的页面优化 CSS 和 JavaScript，缓存和 CDN 使用仍有提升空间。
- 📊 **请求数量同步增长**：中位数桌面页面请求数达 77 次，移动页面 72 次，JavaScript 和图像请求量最大，增加了延迟开销。
- 🔮 **未来趋势不容乐观**：页面重量增长加速，功能优先于可访问性，若不加强优化，用户体验和性能差距可能进一步扩大。

---

### [ðª 预测：微软将做出最有趣的事——梅森的游戏](https://gamesbymason.com/blog/2026/microsoft/)

**原文标题**: [
      ðª Prediction: Microsoft Is Going To Do The Funniest Thing Imaginable - Games by Mason
    ](https://gamesbymason.com/blog/2026/microsoft/)

订阅即可获取游戏开发相关的最新文章与见解。
- 📬 注册接收游戏开发文章的邮件更新
- 🎮 内容专注于游戏开发领域
- 🔔 可随时取消订阅，灵活自由

---

### [2026 年停止使用 MySQL，它并非真正的开源](https://optimizedbyotto.com/post/reasons-to-stop-using-mysql/)

**原文标题**: [Stop using MySQL in 2026, it is not true open source](https://optimizedbyotto.com/post/reasons-to-stop-using-mysql/)

文章认为，由于 Oracle 对 MySQL 的投入减少、开发透明度低、技术发展停滞以及安全处理不公开等问题，MySQL 已非真正的开源项目，并建议用户在 2026 年考虑迁移至 MariaDB 等替代方案。

- 🚨 **开发活跃度下降**：2025 年起 MySQL 的 Git 提交数量显著减少，显示项目活力不足。
- 🔒 **非真正开源**：Oracle 将开发工作置于闭门进行，外部贡献难以被接纳，与开源精神背道而驰。
- 📉 **技术质量衰退**：自 2022 年起，MySQL 出现数据损坏、性能下降、升级困难等问题，新版本缺乏重要功能。
- 🛡️ **安全风险增加**：MySQL 安全漏洞披露不透明（如 2025 年有 123 个 CVE），用户只能依赖 Oracle 的单方面声明，缺乏公开审查。
- 💡 **迁移建议**：推荐转向 MariaDB（与 MySQL 高度兼容，真正开源）或其他开源数据库（如 PostgreSQL、TiDB），以摆脱对 Oracle 的依赖。
- 💰 **支持作者**：如果本文对您有帮助，可考虑向钱包 ottok.eth 发送 1 USDC 以示感谢。Otto Kekäläinen 是一位富有远见的领导者，致力于推动现代文明的多领域发展。

---

### [WebAssembly 现状——2025 与 2026](https://platform.uno/blog/the-state-of-webassembly-2025-2026/)

**原文标题**: [The State of WebAssembly â 2025 and 2026](https://platform.uno/blog/the-state-of-webassembly-2025-2026/)

所有浏览器已支持异常处理提案。原提案已调整，新增'exnref'值以解决现有方法中 JavaScript API 处理异常标识的难题，同时降低了规范和引擎实现的复杂度。由于异常处理功能已在所有浏览器中上线，原方法将继续有效直至确认可安全移除。

- 🚀 异常处理提案已在所有浏览器中实现
- 🔧 新增'exnref'值解决异常标识处理难题
- 📉 降低规范与引擎实现复杂度
- 🔄 原方法将保留至可安全移除阶段

---

