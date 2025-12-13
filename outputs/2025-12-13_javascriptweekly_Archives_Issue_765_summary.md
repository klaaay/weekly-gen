### [JavaScript 周刊第 765 期：2025 年 12 月 12 日](https://javascriptweekly.com/issues/765)

**原文标题**: [JavaScript Weekly Issue 765: December 12, 2025](https://javascriptweekly.com/issues/765)

本期内容涵盖了 JavaScript 和 Web 开发领域的最新动态，包括工具发布、安全更新、技术文章和实用资源。重点介绍了 Deno 2.6 的新功能、React 安全漏洞、Node.js LTS 版本发布，以及多个开源工具和库的更新。同时，分享了一些关于构建 HTML 工具、优化 Web 应用性能和前端工程实践的文章。

- 🛠️ **Deno 2.6 发布**：引入了类似 npx 的 dx 工具、deno 审计功能、更细粒度的运行时权限控制和源阶段导入等新特性。
- ⚠️ **React 安全漏洞**：新增两个与 React 服务器组件相关的安全漏洞，独立于上周的 React2Shell 事件。
- 🔒 **npm 令牌策略更新**：GitHub 撤销所有经典 npm 令牌，推出新的两小时会话令牌和细粒度访问令牌流程。
- 🕒 **Chrome 144 Beta 发布**：支持用于处理日期和时间的 Temporal API。
- 📦 **Node.js v24.12.0 (LTS)**：首个将类型剥离标记为稳定的 LTS 版本。
- 🐰 **Bun v1.3.4 更新**：新增 URLPattern 支持、测试运行器中的可控计时器，以及类似 Node 的 console.log %j说明符。
- 📖 **技术文章精选**：包括《西雅图时报》如何防范 npm 供应链攻击、微软提出的延迟消息计时 API 提案，以及用 JavaScript 构建微型 2D 物理引擎等。
- 🛠️ **开源工具与库**：Remix 商店开源、GitHub 的 relative-time 5.0 Web 组件、ts-exec TypeScript 执行工具、Toastflow Vue 3 通知库等。
- 🔍 **生态系统动态**：TypeSlayer 工具展示、CSS Wrapped 2025 总结、GitHub Actions 平台更新，以及 OpenAI 发布 GPT 5.2 模型。

---

### [构建 HTML 工具的有用模式](https://simonwillison.net/2025/Dec/10/html-tools/)

**原文标题**: [Useful patterns for building HTML tools](https://simonwillison.net/2025/Dec/10/html-tools/)

本文介绍了作者 Simon Willison 在过去两年中构建超过 150 个“HTML 工具”的经验总结，这些工具是结合 HTML、JavaScript 和 CSS 的单文件应用，旨在提供实用功能。文章分享了一系列高效构建此类工具的模式和技巧。

- 🛠️ **HTML 工具定义**：指结合 HTML、JavaScript 和 CSS 的单文件应用，提供特定功能，作者已构建超过 150 个，大多由 LLM 生成。
- 📁 **单文件结构**：工具采用单 HTML 文件，内联 JS 和 CSS，避免使用 React 等需要构建步骤的框架，便于复制粘贴和托管。
- 🚀 **原型开发**：可直接在 ChatGPT、Claude 或 Gemini 的“Canvas”或“Artifacts”功能中快速原型开发，并强调添加“No React”提示。
- 🔗 **依赖加载**：通过 CDN 加载外部库（如 cdnjs、jsDelivr），避免 npm 构建步骤，提升开发效率和便携性。
- 🌐 **自主托管**：推荐将工具部署到 GitHub Pages 等静态托管服务，避免 LLM 平台沙箱限制，提升可靠性和用户体验。
- 📋 **利用剪贴板**：许多工具基于复制粘贴交互，支持富文本粘贴和“复制到剪贴板”按钮，增强移动端友好性。
- 🐛 **构建调试工具**：创建如 clipboard-viewer 等调试工具，探索浏览器 API 能力，为开发更复杂工具奠定基础。
- 🔗 **状态持久化**：使用 URL 参数存储工具状态便于分享，或利用 localStorage 保存较大数据或敏感信息（如 API 密钥）。
- 🌉 **利用 CORS API**：收集支持 CORS 的开放 API（如 iNaturalist、PyPI、GitHub），实现跨域数据获取，丰富工具功能。
- 🤖 **直接调用 LLM API**：通过 CORS 直接调用 OpenAI、Anthropic、Gemini 的 API，结合 localStorage 存储用户 API 密钥。
- 📂 **本地文件处理**：使用`<input type="file">`在浏览器中直接处理用户文件，无需上传服务器，实现 OCR、图像裁剪等功能。
- ⬇️ **生成可下载文件**：借助 JavaScript 库在浏览器中生成并下载文件（如图片、ICS 日历文件），无需服务器参与。
- 🐍 **使用 Pyodide**：通过 Pyodide 在浏览器中运行 Python 及 PyPI 包，实现数据分析和可视化等复杂功能。
- ⚙️ **WebAssembly 扩展能力**：利用 WebAssembly 在浏览器中运行其他语言编写的工具（如图像压缩、OCR），扩展功能边界。
- 🔄 **复用与重组工具**：通过参考现有工具代码，快速组合新功能，LLM 能基于已有示例更准确地生成代码。
- 📝 **记录提示与对话**：保存并公开 LLM 交互记录，有助于技能提升和工具维护，可通过分享链接或提交记录到代码库实现。

---

### [tools.simonwillison.net](https://tools.simonwillison.net/)

**原文标题**: [tools.simonwillison.net](https://tools.simonwillison.net/)

这是一个由 Simon Willison 创建的实验性 HTML+JavaScript 工具集合网站，主要用于探索提示驱动的低风险开发，所有工具代码开源，并附有开发过程的详细记录。

- 🛠️ **工具集合**：网站包含大量基于 HTML 和 JavaScript 构建的实用工具，涵盖图像处理、文本转换、数据工具、开发辅助等多个类别。
- 🤖 **LLM 驱动开发**：大多数工具是在大型语言模型的帮助下创建的，体现了提示驱动开发的实验性质。
- 📂 **开源与透明**：所有工具代码开源在 GitHub，且每个工具都附有开发过程的提交信息和对话记录。
- 🔄 **持续更新**：网站会定期添加和更新工具，例如近期新增了 PDF 查看、Bugzilla 问题查看等功能。
- 🗂️ **分类清晰**：工具按功能分为图像与媒体、文本与文档、数据与时间、GitHub 与开发、LLM 调试等多个板块，方便查找。
- 🔗 **相关资源**：网站还提供了使用 Python 编写的工具链接，以及关于 Claude 自定义指令的说明文档。

---

### [JavaScript 电子表格库 | JS Excel 函数与公式 | SpreadJS](https://developer.mescius.com/spreadjs?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=SPJS-JS-Weekly-Primary-Sponsor-December-2025)

**原文标题**: [JavaScript Spreadsheet Library | JS Excel Functions and Formulas | SpreadJS](https://developer.mescius.com/spreadjs?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=SPJS-JS-Weekly-Primary-Sponsor-December-2025)

SpreadJS 是一款领先的 JavaScript 电子表格组件，提供与 Excel 高度相似的体验，支持超过 500 种函数，无需依赖 Excel 即可实现复杂的数据处理、导入导出及可视化。

- 📊 **强大的计算引擎**：内置超过 500 种函数，支持动态数组、自定义函数和复杂计算模型。
- 🔄 **无缝 Excel 兼容**：支持导入和导出 .xlsx、.xlsm、.xltm 等多种 Excel 文件格式，实现数据无损交换。
- 🎨 **丰富的可视化功能**：提供 30 多种图表类型、条件格式、迷你图（Sparklines）和数据切片器（Slicers）。
- 🛠️ **灵活的单元格控制**：支持多种单元格类型、下拉列表、数据验证、富文本及条形码等高级格式设置。
- 📈 **交互式仪表板与表单**：可创建交互式数据输入表单、财务报表、预算分析仪表板和高级数据透视表。
- 🌐 **全球化与本地化**：支持多语言界面和计算引擎本地化，包括中文、日文等 18 种语言包。
- ⚡ **高性能处理**：专为大数据集优化，可快速加载和处理数百万单元格，性能卓越。
- 🤖 **AI 智能助手（预览版）**：通过自然语言生成公式、解释逻辑并创建数据透视表，提升工作效率。
- 🧩 **可选的扩展组件**：包括设计器功能区、数据透视表、甘特图、报表设计器和高级图表等附加模块。
- 📱 **无代码设计工具**：提供桌面设计器和设计器功能区组件，允许用户无需编码即可创建和定制电子表格。

---

### [Deno 2.6：dx 是新的 npx | Deno](https://deno.com/blog/v2.6)

**原文标题**: [Deno 2.6: dx is the new npx | Deno](https://deno.com/blog/v2.6)

Deno 2.6 版本引入了多项重要更新，包括新的 `dx` 工具用于便捷运行 npm 和 JSR 包二进制文件，更细粒度的权限控制，以及通过 `tsgo` 实现更快的类型检查。此外，还新增了 Wasm 源阶段导入、CommonJS 模块的 `--require` 支持、安全审计命令 `deno audit`，以及依赖管理和 Node.js 兼容性的多项改进。

- 🚀 引入 `dx` 工具，类似 `npx`，方便运行 npm 和 JSR 包的二进制文件，默认使用 `--allow-all` 权限并支持生命周期脚本
- 🔒 新增 `--ignore-read` 和 `--ignore-env` 权限标志，提供更细粒度的文件读取和环境变量访问控制
- ⚡ 集成 `tsgo` 实验性类型检查器，显著提升 TypeScript 类型检查速度，并改进语言服务器功能
- 📦 支持 Wasm 源阶段导入，允许在构建时直接导入 WebAssembly 模块源码，提升效率
- 🔧 新增 `--require` 标志，支持运行 CommonJS 模块，增强 Node.js 兼容性
- 🛡️ 引入 `deno audit` 命令，用于扫描依赖中的安全漏洞，支持 GitHub CVE 数据库和 socket.dev 集成
- 📋 提供 `deno approve-scripts` 命令，允许更精细地控制 npm 包生命周期脚本的执行
- 🧩 默认包含 `@types/node` 类型声明，无需手动安装即可获得 Node.js API 的完整类型提示
- 🧪 稳定 `BroadcastChannel` API，改进 Web 流的可转移性，并支持 `ImageData` 中的 `Float16Array`
- 🚄 优化性能，修复 `fetch` API 内存泄漏，改进 V8 引擎集成，并提升 Node.js 兼容性操作的执行速度

---

### [GitHub - tc39/proposal-source-phase-imports：关于在源码阶段导入模块的提案](https://github.com/tc39/proposal-source-phase-imports)

**原文标题**: [GitHub - tc39/proposal-source-phase-imports: Proposal to enable importing modules at the source phase](https://github.com/tc39/proposal-source-phase-imports)

该提案旨在为 ECMAScript 模块系统引入源阶段导入功能，允许在模块加载过程中获取模块的编译后源表示，以支持 JavaScript 和 WebAssembly 等模块类型的自定义加载、链接与执行需求。

- 🚀 **提案状态**：目前处于 Stage 3 阶段，由 Luca Casonato 和 Guy Bedford 担任 Champion，主要目标是为模块加载提供更灵活的底层控制。
- 🔧 **核心语法**：支持静态导入（`import source x from "<specifier>"`）和动态导入（`await import.source("<specifier>")`），允许获取模块的源对象而不触发依赖处理。
- 🧩 **模块源对象**：定义`AbstractModuleSource`作为基础原型，JavaScript 模块返回`ModuleSource`对象，WebAssembly 模块则复用`WebAssembly.Module`并扩展其原型链。
- 🛡️ **安全优势**：继承宿主加载器的安全策略（如内容安全策略 CSP），避免动态加载时需使用`unsafe-eval`等宽松策略，增强模块加载的安全性。
- 🔗 **应用场景**：适用于自定义加载器、WASI 等 WebAssembly 运行时集成、静态分析工具和打包器优化，提升模块依赖的可追踪性与缓存效率。
- ❓ **常见问答**：澄清与导入属性、模块表达式等特性的关系，强调其作为模块请求阶段补充的定位，并对比与传统动态加载方式在安全性和工具链支持上的差异。

---

### [React Server Components 中的拒绝服务与源代码暴露问题 – React](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components)

**原文标题**: [Denial of Service and Source Code Exposure in React Server Components – React](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components)

React 团队披露了 React Server Components 中的两个新安全漏洞，需立即升级相关包至修复版本。

- 🚨 **高危漏洞：拒绝服务攻击**  
  恶意 HTTP 请求可导致服务器陷入无限循环，消耗 CPU 资源，使服务不可用。涉及 CVE-2025-55184 和 CVE-2025-67779（CVSS 7.5）。

- 🔓 **中危漏洞：源代码泄露**  
  攻击者可能通过特制请求获取 Server Function 的源代码，暴露硬编码的密钥等敏感信息。涉及 CVE-2025-55183（CVSS 5.3）。

- ⚠️ **需重复更新**  
  若已针对上周关键漏洞升级至 19.0.2、19.1.3 或 19.2.2 版本，因修复不完整，必须再次升级至 19.0.3、19.1.4 或 19.2.3。

- 📦 **受影响范围**  
  漏洞存在于 react-server-dom-webpack、react-server-dom-parcel、react-server-dom-turbopack 的 19.0.0 至 19.2.2 版本。使用 Next.js、React Router 等框架的项目需检查更新。

- 🛡️ **缓解措施**  
  未使用服务器或 React Server Components 的应用不受影响。部分托管服务商已部署临时防护，但建议直接升级依赖包。

- 📅 **时间线**  
  漏洞于 12 月初陆续报告，React 团队在 12 月 11 日发布完整补丁并分配 CVE 编号。

---

### [React2Shell（CVE-2025-55182）](https://react2shell.com/)

**原文标题**: [React2Shell (CVE-2025-55182)](https://react2shell.com/)

React2Shell（CVE-2025-55182）是一个影响 React.js 服务端使用的 10.0 级严重漏洞，Next.js 框架中对应编号为 CVE-2025-66478。该漏洞由研究者于 2025 年 11 月 29 日向 Meta 团队披露，官方于 12 月 3 日发布补丁。目前存在部分无效概念验证报告混淆视听，建议用户及时根据官方公告修补系统。

- 🔥 漏洞编号 CVE-2025-55182（React.js）与 CVE-2025-66478（Next.js），危险等级 10.0
- 📅 2025 年 11 月 29 日由研究者向 Meta 团队披露，12 月 3 日官方发布补丁
- ⚠️ 已出现无效概念验证报告，需警惕错误漏洞判断
- 🔧 建议用户立即参照 React 与 Next.js 官方公告更新修补
- 🤝 感谢 Meta、Vercel 团队及合作研究者的协调与贡献
- 📌 Next.js 因特殊打包机制单独分配 CVE 编号便于识别

---

### [npm 经典令牌已撤销，现提供基于会话的身份验证和 CLI 令牌管理 - GitHub 更新日志](https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available/)

**原文标题**: [npm classic tokens revoked, session-based auth and CLI token management now available - GitHub Changelog](https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available/)

npm 已完成经典令牌的全面淘汰，转向更安全的会话式认证与令牌管理机制，以强化生态系统安全。

- 🔐 所有 npm 经典令牌已被永久撤销，无法再用于认证或恢复
- ⏳ 新登录将生成两小时会话令牌，到期需重新认证，且会话期间发布操作强制启用双重认证
- 🛠️ 新增命令行工具支持直接在终端创建、查看和撤销细粒度访问令牌
- 🏗️ 新发布的包将默认启用双重认证保护，现有包设置保持不变
- 🔄 为兼容性临时恢复旧版 API 端点支持，但将在未来数月内移除
- 🔧 本地开发需定期运行`npm login`重新认证；CI/CD 流程应改用细粒度令牌或 OIDC 可信发布方案

---

### [Chrome 144 测试版  |  博客  |  面向开发者的 Chrome](https://developer.chrome.com/blog/chrome-144-beta?hl=en)

**原文标题**: [Chrome 144 beta  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-144-beta?hl=en)

Chrome 144 Beta 版本引入了多项 CSS、Web API 及功能更新，同时宣布了多项 API 的弃用计划，主要围绕增强开发者体验、改进性能与隐私保护。

- 🎨 **CSS 与界面增强**：包括 CSS 锚点定位支持变换、查找高亮样式自定义、滚动状态样式控制等，提升页面交互与视觉效果。
- 🔧 **Web API 扩展**：新增 `<geolocation>` 元素简化地理位置获取、View Transitions 支持高级动画控制、WebGPU 功能优化等，丰富开发者工具集。
- 📱 **跨平台与性能改进**：Android 支持 Pointer Lock API、事件计时 API 新增交互计数、优化滚动行为与 RTL 数学渲染等，提升跨平台一致性与用户体验。
- 🛡️ **隐私与安全调整**：弃用 Topics API、Protected Audience API 等多个隐私沙盒相关 API，并移除 XML 外部实体加载功能，以强化隐私保护。
- 🧪 **新功能实验**：启动增强 Canvas 文本测量等源试用，为开发者提供前沿功能测试机会。
- ⚠️ **弃用与移除通知**：详细列出多项 API 的弃用计划，包括共享存储、归因报告等，开发者需关注并调整代码适配。

---

### [时间性](https://tc39.es/proposal-temporal/)

**原文标题**: [Temporal](https://tc39.es/proposal-temporal/)

总结失败：Error code: 400 - {'error': {'message': "This model's maximum context length is 131072 tokens. However, you requested 183953 tokens (175953 in the messages, 8000 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

### [宣布适用于 VS Code 的 JavaScript/TypeScript 现代化工具 - Microsoft 开发者平台](https://developer.microsoft.com/blog/jsts-modernizer-preview)

**原文标题**: [Announcing the JavaScript/TypeScript Modernizer for VS Code - Microsoft for Developers](https://developer.microsoft.com/blog/jsts-modernizer-preview)

微软宣布推出适用于 VS Code 的 JavaScript/TypeScript 现代化工具，这是一款 AI 辅助工具，旨在帮助开发者自动化升级 npm 包和更新代码，以简化项目现代化过程。

- 🚀 **工具发布**：推出 VS Code 扩展“JavaScript/TypeScript Modernizer”，利用 GitHub Copilot 自动化升级 JS/TS 项目依赖和代码。
- 🤖 **AI 驱动**：通过 Copilot Chat 交互式指导，自动分析项目、升级 npm 包至最新版本，并适配代码变更。
- ⚙️ **使用条件**：需预先安装 Node.js/npm、启用 GitHub Copilot，并安装预览版扩展后手动开启实验性设置。
- 📦 **操作流程**：在 VS Code 中打开项目，通过扩展面板启动升级，跟随 Copilot 提示完成包更新和代码调整。
- ⚠️ **预览限制**：目前仅支持单项目升级，且为预览功能，可能遇到复杂场景兼容性问题。
- 📢 **反馈收集**：鼓励用户通过邮件提交使用反馈，以帮助改进工具功能。

---

### [类型感知 Linting Alpha | JavaScript 氧化编译器](https://oxc.rs/blog/2025-12-08-type-aware-alpha)

**原文标题**: [Type-Aware Linting Alpha | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2025-12-08-type-aware-alpha)

Oxlint 宣布其类型感知 linting 功能进入 Alpha 阶段，该功能利用 TypeScript 类型系统实现更强大的代码检查，现已支持 43 条规则，性能相比 ESLint 有显著提升，并引入了实验性的类型检查等新特性。

- 🚀 **快速开始**：通过安装 `oxlint` 和 `oxlint-tsgolint` 并使用 `--type-aware` 标志，即可在几分钟内启用类型感知 linting。
- ⚡ **性能优势**：基准测试显示，Oxlint 的类型感知 linting 速度比 ESLint 配合 `typescript-eslint` 快约 10 倍。
- 🆕 **新增功能**：自技术预览版以来，增加了在 linting 同时进行类型检查、规则配置支持、内联禁用注释支持以及更多规则（如 `no-deprecated`）等功能。
- 🔧 **技术架构**：采用独特的双二进制架构，`oxlint`（Rust）处理前端逻辑，`tsgolint`（Go）基于 `typescript-go` 进行类型分析和规则执行。
- 📝 **类型检查集成**：实验性支持通过 `--type-check` 标志在 linting 过程中输出 TypeScript 类型错误，有望减少 CI 中单独类型检查的时间。
- ⚠️ **已知问题**：在处理超大型代码库时可能遇到内存不足的情况，团队正在优化内存使用。
- 🔮 **未来计划**：Beta 版本将专注于支持更多规则、优化性能与内存使用，并持续跟进 TypeScript 7.0 的稳定发布。
- 🤝 **致谢与反馈**：感谢 TypeScript、`typescript-eslint` 团队及贡献者，鼓励用户通过 Discord、GitHub 等渠道提供反馈。

---

### [Node.js — Node.js v24.12.0（长期支持版）](https://nodejs.org/en/blog/release/v24.12.0)

**原文标题**: [Node.js — Node.js v24.12.0 (LTS)](https://nodejs.org/en/blog/release/v24.12.0)

Node.js v24.12.0（LTS）版本“Krypton”发布，包含多项新功能、性能优化、错误修复及依赖项更新，同时提供了各平台的安装包和二进制文件下载。

- 🆕 **新增 HTTP 服务器选项**：添加`optimizeEmptyRequests`选项以优化空请求处理。
- ⚙️ **工具函数增强**：`util.deprecate`新增配置选项，提升废弃 API 管理灵活性。
- 📦 **模块功能稳定化**：模块类型剥离（type stripping）标记为稳定功能。
- 🔧 **Node-API 扩展**：新增`napi_create_object_with_properties`方法，简化对象创建。
- 🛡️ **SQLite 安全增强**：允许设置防御性标志（defensive flag），提升数据库安全性。
- 👀 **监视配置支持**：新增监视配置命名空间，便于文件变更监控。
- 💾 **编译缓存可移植性**：添加选项使编译缓存可在不同环境间移植。
- 🔍 **调试权限控制**：新增`--allow-inspector`选项，精细化控制调试器访问权限。
- 📊 **性能分析工具**：V8 引擎新增 CPU 性能分析功能，便于性能调优。
- 🚀 **性能与稳定性优化**：涵盖缓冲区处理、控制台输出、加密验证等多个核心模块的改进。
- 🔄 **依赖项更新**：升级 V8 引擎至 13.6.233.17，并更新 nghttp2、corepack 等关键依赖。
- 📚 **文档完善与修正**：修复多处文档错误，新增术语解释和代码示例，提升使用体验。
- 🐛 **错误修复与测试强化**：修复调试器、TLS、流处理等多个模块的问题，并增强测试覆盖率。

---

### [Python-Node：现已支持流式传输与 WebSocket](https://blog.platformatic.dev/streaming-and-websocket-support-now-available-in-platformaticpython-node)

**原文标题**: [Python-Node: Streaming and WebSocket Now Supported](https://blog.platformatic.dev/streaming-and-websocket-support-now-available-in-platformaticpython-node)

@platformatic/python-node v2.0.0 版本现已发布，引入了对 HTTP 响应流式传输和双向 WebSocket 通信的完整支持。该版本使全栈团队能够通过桥接 Python 的异步生态系统与 Node.js，构建实时、高性能的应用程序。

- 🚀 **支持 HTTP 响应流式传输**：新的 `handleStream()` 方法允许以增量方式处理响应块，减少大响应的内存占用，并可在正文完成前立即访问响应头。
- 📤 **支持 HTTP 请求流式传输**：现在可以将请求正文流式传输到 Python，这对于处理大文件上传、渐进式数据处理或实现自定义流式协议至关重要。
- 🔄 **支持双向 WebSocket 通信**：Python ASGI 应用程序现在可以处理持久、双向的连接，适用于构建聊天应用、实时仪表板或多人游戏等场景。
- 🏗️ **实现 ASGI 3.0 协议**：底层实现了 ASGI 3.0 协议规范，确保与整个 Python 异步生态系统的兼容性，包括 FastAPI 的 `StreamingResponse` 和 Starlette 的 WebSocket 端点。
- 💾 **降低内存占用**：流式传输大响应而无需将所有内容缓冲在内存中。
- ⚡ **更快的首字节时间**：在正文开始写入之前即可立即访问响应头。
- 🔧 **更好的资源利用率**：响应块到达时即进行处理，无需等待完成。
- ⏪ **向后兼容**：现有使用 `handleRequest()` 的代码几乎完全无需更改即可继续工作。
- 📊 **实际应用示例**：包括使用 FastAPI 构建服务器发送事件（SSE）的实时监控仪表板，以及构建具有双向通信的对话式 AI 助手。
- 🛠️ **集成场景**：支持多种集成模式，如在 Python 中运行机器学习模型进行实时推理、渐进式数据处理、混合 API 网关以及为现有 Python 工具添加 WebSocket 接口。
- 📦 **入门与迁移**：提供了安装指南，并解释了何时使用 `handleRequest()` 与 `handleStream()`，以及迁移现有应用程序的检查清单。

---

### [Bun v1.3.4 | Bun 博客](https://bun.sh/blog/bun-v1.3.4)

**原文标题**: [Bun v1.3.4 | Bun Blog](https://bun.sh/blog/bun-v1.3.4)

本文介绍了 Bun 的最新更新，包括安装与升级方法、新增功能如 URLPattern API 和测试假定时器、fetch() 代理头自定义、连接池优化、独立可执行文件配置加载改进、console.log 格式支持、SQLite 版本升级，以及多项错误修复和兼容性改进。

- 🚀 **安装与升级**：支持多种方式安装 Bun（如 curl、npm、PowerShell 等），升级命令为`bun upgrade`
- 🔗 **URLPattern API**：新增 URLPattern Web API，用于 URL 模式匹配，支持路由和参数提取
- ⏱️ **测试假定时器**：`bun:test`支持假定时器，可控制时间测试定时相关代码
- 🌐 **fetch() 代理头**：`fetch()`代理选项现支持对象格式，可自定义发送给代理服务器的头部
- 🔄 **连接池优化**：修复`http.Agent`连接复用问题，提升 HTTP 请求效率
- ⚡ **独立可执行文件**：编译后的可执行文件默认不加载运行时配置文件，提升启动性能
- 📝 **console.log 格式**：支持`%j`格式符输出 JSON 字符串化内容
- 🗃️ **SQLite 更新**：`bun:sqlite`升级至 v3.51.1，优化查询规划
- 🐛 **多项修复**：涵盖测试、打包、安装、Windows 兼容性、Node.js API 及安全等方面

---

### [发布 19.2.3 版本（2025 年 12 月 11 日）· facebook/react · GitHub](https://github.com/facebook/react/releases/tag/v19.2.3)

**原文标题**: [Release 19.2.3 (December 11th, 2025) · facebook/react · GitHub](https://github.com/facebook/react/releases/tag/v19.2.3)

这是一个关于 React 在 GitHub 上的仓库页面摘要，主要展示了其最新版本 v19.2.3 的发布信息。

- 📦 React 最新版本 v19.2.3 于 2025 年 12 月 11 日发布
- 🔧 该版本主要针对 React Server Functions 增加了额外的循环保护功能
- 👥 由贡献者 sebmarkbage 提交，eps1lon 负责发布
- ⭐ 项目目前拥有 242k 星标和 50.1k 次复刻，显示出很高的社区关注度
- 🐛 页面显示存在一些加载错误和技术问题需要重新加载解决
- 💬 发布后获得了社区成员的多种表情反应，包括 5 个点赞、3 个大笑等

---

### [发布 19.1.4 版本（2025 年 12 月 11 日）· facebook/react · GitHub](https://github.com/facebook/react/releases/tag/v19.1.4)

**原文标题**: [Release 19.1.4 (December 11th, 2025) · facebook/react · GitHub](https://github.com/facebook/react/releases/tag/v19.1.4)

React 项目在 GitHub 上的最新动态，包括版本发布、社区互动和错误提示。

- 🚀 **版本更新** – React v19.1.4 于 2025 年 12 月 11 日发布，包含对服务器组件的额外循环保护。
- ⭐ **项目热度** – 项目获得 242k 星标和 50.1k 分支，显示出广泛的社区关注和使用。
- ⚠️ **加载问题** – 页面多次提示加载错误，建议用户重新加载以获取最新内容。
- 👥 **社区参与** – 最新版本由贡献者 sebmarkbage 提交，获得 9 位用户的积极反应（8 个赞和 1 个火箭表情）。
- 🔍 **功能导航** – 页面提供代码、问题、拉取请求等导航选项，方便开发者深入参与项目。

---

### [发布 19.0.3 版本（2025 年 12 月 11 日）· facebook/react · GitHub](https://github.com/facebook/react/releases/tag/v19.0.3)

**原文标题**: [Release 19.0.3 (December 11th, 2025) · facebook/react · GitHub](https://github.com/facebook/react/releases/tag/v19.0.3)

React 19.0.3 版本于 2025 年 12 月 11 日发布，主要针对 React 服务器组件进行了安全性和稳定性的更新。

- 🔧 为 React 服务器函数添加了额外的循环保护机制
- 👥 由开发者 sebmarkbage 贡献此修复
- 🚀 社区反应积极，获得多个点赞、爱心和火箭表情回应
- 📅 版本由维护者 eps1lon 于 12 月 12 日正式发布

---

### [我们如何保护新闻编辑室免受 npm 供应链攻击 | pnpm](https://pnpm.io/blog/2025/12/05/newsroom-npm-supply-chain-security)

**原文标题**: [How We're Protecting Our Newsroom from npm Supply Chain Attacks | pnpm](https://pnpm.io/blog/2025/12/05/newsroom-npm-supply-chain-security)

《西雅图时报》技术团队通过采用 pnpm 的三层客户端安全控制，防范 npm 供应链攻击。这些措施与 npm 的发布端安全改进形成互补，构建深度防御体系，确保在依赖包管理过程中即使需要例外处理，其他防护层仍能提供保护。

- 🛡️ **生命周期脚本管理**：pnpm 默认阻止包安装时的预装/后装脚本执行，通过严格模式强制团队审查并记录例外，防止恶意代码自动运行。
- ⏳ **发布冷却期**：设置包版本安装的最小发布时间间隔，降低使用刚发布即被社区发现问题的恶意包风险，同时允许紧急安全更新例外。
- 🔐 **信任策略**：检测包版本的认证强度降级（如从可信发布者变为基础认证），阻止可能因维护者凭证泄露而发布的恶意版本。
- 🧩 **深度防御实践**：三层控制协同工作，例如紧急 React 安全补丁可豁免冷却期，但其他两层仍会检查脚本与信任降级，避免单点失效。
- ⚙️ **试点经验**：在单个后端服务实施仅需数小时，发现并阻断了 esbuild 等包的非必要脚本，团队需适应“安全优先”的决策流程，但控制措施对中型团队切实可行。
- 📝 **实施建议**：从单一项目试点、预期并记录例外、启用严格脚本模式、信任多层防护，逐步构建可应对实际复杂场景的供应链安全体系。

---

### [快速、节省磁盘空间的包管理器 | pnpm](https://pnpm.io/)

**原文标题**: [Fast, disk space efficient package manager | pnpm](https://pnpm.io/)

pnpm 是一个快速高效的包管理器，支持单仓库多包管理，并通过非扁平的 node_modules 结构确保严格依赖。

- 🚀 pnpm 比 npm 快两倍
- 💾 通过单一存储克隆或硬链接 node_modules 文件，节省空间
- 📦 内置支持单仓库多包（monorepo）
- 🔒 默认创建非扁平 node_modules，防止代码访问未声明的包

---

### [获取失败](https://javascriptweekly.com/link/178426/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/178426/web)

无法总结：获取内容失败，状态码 403。

---

### [delayed-message-timing/README.md 位于 main · WICG/delayed-message-timing · GitHub](https://github.com/WICG/delayed-message-timing/blob/main/README.md)

**原文标题**: [delayed-message-timing/README.md at main · WICG/delayed-message-timing · GitHub](https://github.com/WICG/delayed-message-timing/blob/main/README.md)

该页面是 WICG（Web 平台孵化器社区组）中关于“delayed-message-timing”提案的 GitHub 仓库界面，展示了项目的基本信息和导航结构。

- 📂 仓库位于 WICG 组织下，主题为“delayed-message-timing”，状态为公开
- 🔔 页面提示用户需登录以更改通知设置，并提供分支、星标等交互选项
- ⚠️ 当前加载遇到错误，显示“Uh oh!”提示并建议重新加载页面
- 🧭 导航栏包含代码、议题、拉取请求等标准 GitHub 仓库管理选项

---

### [CERN 如何利用 TimescaleDB 推动突破性物理研究 | 虎数据](https://www.tigerdata.com/blog/how-cern-powers-ground-breaking-physics-with-timescaledb)

**原文标题**: [How CERN Powers Ground-Breaking Physics with TimescaleDB | Tiger Data](https://www.tigerdata.com/blog/how-cern-powers-ground-breaking-physics-with-timescaledb)

欧洲核子研究中心（CERN）利用 TimescaleDB 替代传统 Oracle 数据库，构建下一代数据归档系统（NGA），以应对大型强子对撞机等实验产生的海量时序数据管理挑战，实现更高的写入吞吐、存储压缩和查询性能。

- 🚀 **应对数据挑战**：CERN 拥有 800 多个 SCADA 系统，每日产生数百 GB 时序数据，原有 Oracle 方案存在架构耦合与技术债务问题。
- 🔄 **战略升级**：2017 年启动 NGA 项目，采用可插拔后端架构，支持 PostgreSQL 和 TimescaleDB，已部署约 500 个系统。
- 📊 **选型依据**：TimescaleDB 凭借时序数据优化、压缩能力、持续聚合功能及与 PostgreSQL 生态兼容性被选中。
- ⚡ **性能表现**：写入吞吐达每秒 4 万行，满足最大系统需求；压缩减少 78-95% 存储空间，查询速度提升 10-40 倍。
- 🔮 **未来规划**：2027 年前全面部署 TimescaleDB 生产环境，通过持续聚合和压缩技术支撑物理实验数据分析与可视化。

---

### [马克西姆·欧齐埃](https://xem.github.io/articles/2D-physics.html)

**原文标题**: [Maxime Euzière](https://xem.github.io/articles/2D-physics.html)

作者基于对 JavaScript 中 2D 物理引擎的长期探索，通过跟随一个 YouTube 教程系列，逐步构建并优化了一个功能完整的 2D 物理引擎。该引擎支持圆形和矩形的碰撞检测与响应、刚体动力学、多种关节（如弹簧、铰链和固定关节），并最终通过代码压缩将体积大幅减小至约 1.4KB（gzip 压缩）。尽管在堆叠稳定性方面仍存在挑战，但作者通过参考其他轻量级引擎的解决方案，为未来的改进指明了方向。

- 🎯 作者长期探索 JS 中的 2D 物理，最终通过一个 YouTube 教程系列实现了功能完整的引擎构建。
- 📚 教程涵盖了从基础设置到高级功能（如碰撞检测、刚体集成、关节系统）的完整实现过程。
- 🔧 引擎支持圆形与矩形的碰撞检测、刚体动力学（质量、速度、摩擦力、恢复系数）及多种关节类型。
- ⚙️ 通过代码压缩和优化，最终引擎体积大幅减小至约 1.4KB（gzip 压缩），适合轻量级应用。
- 🧩 实现了弹簧、铰链、固定关节等高级功能，满足了作者对“高级物理”的初始需求。
- 🐛 在矩形堆叠稳定性上遇到挑战，发现需要多接触点支持才能实现稳定堆叠。
- 🔍 参考了其他轻量级引擎（如 Cirobb、Box2D-lite 的 Phaser 适配）来探索堆叠稳定性的解决方案。
- 🚀 项目最终以开源形式发布，并提供了完整的演示和代码库，供社区使用和进一步开发。

---

### [二维物理](https://xem.github.io/2Dphysics/)

**原文标题**: [2Dphysics](https://xem.github.io/2Dphysics/)

这是一个用 JavaScript 编写的超轻量级 2D 物理引擎，包含弹簧和关节等物理交互功能，体积极小且高度优化。

- 🌐 提供完整版（20KB 注释源码/1.5KB 压缩）和微缩版（无关节，1.2KB 压缩）两种版本
- 🔧 支持矩形和圆形两种基本形状，并可设置质量、摩擦、弹性等物理属性
- 🧩 内置四种关节类型：弹簧关节、排斥关节、铰链关节和固定关节
- ⚙️ 提供形状创建、锚点设置、关节连接和物理模拟运行等核心 API 函数
- 🎮 包含完整的演示代码，展示如何创建物理对象、实现游戏循环和简单渲染
- 📖 代码完全公开并属于公共领域，附带详细的使用示例和参数说明

---

### [跨浏览器非阻塞画布图像渲染 - 网页性能日历](https://calendar.perfplanet.com/2025/non-blocking-image-canvas/)

**原文标题**: [  Non-blocking cross-browser image rendering on the canvas - Web Performance Calendar](https://calendar.perfplanet.com/2025/non-blocking-image-canvas/)

本文探讨了在 Canvas 中实现跨浏览器非阻塞图像渲染的技术挑战与解决方案，旨在解决大图像解码时主线程阻塞的问题，以提升 Web 应用的用户体验。

- 🎯 **核心挑战**：不同浏览器对 Canvas 的`drawImage()`图像解码实现不一致，导致难以找到一种通用方法避免主线程阻塞。
- 🖼️ **应用场景**：以 Iconik 视频预览功能为例，Canvas 渲染可实现实时图像变换，支持用户快速浏览视频缩略图，优化媒体处理工作流。
- 🔍 **实验方法**：测试了六种图像加载与解码方案，包括标准加载、`decode()`方法、`OffscreenCanvas`、`createImageBitmap`等，并记录了各浏览器兼容性。
- 🛠️ **最终方案**：结合两种方法——针对 Chrome 使用`fetch`+`Blob`+`createImageBitmap`，针对 Firefox 和 Safari 使用`Image.decode()`+`createImageBitmap`，实现了全浏览器非阻塞解码。
- 📊 **效果验证**：优化后显著减少了 UI 卡顿，提升了大型图像（如 7MB 精灵图）渲染时的界面响应速度。
- 💡 **未来展望**：希望 Chrome 和 Safari 能遵循规范统一实现，目前仅 Firefox 完全符合标准。

---

### [《重生密室序曲：用 TypeScript 重写经典》](https://angelo-lima.fr/en/prelude-of-the-chambered-reborn-typescript-web-port/)

**原文标题**: [Prelude of the Chambered Reborn: Rewriting a Classic in TypeScript](https://angelo-lima.fr/en/prelude-of-the-chambered-reborn-typescript-web-port/)

《Prelude of the Chambered Reborn》是一款基于 TypeScript 的浏览器游戏，完整复刻了 Markus Persson 在 2011 年 Ludum Dare 游戏开发大赛中创作的 Java 版复古地牢爬行游戏。该项目旨在通过现代 Web 技术（如 Vite 和 Canvas 2D API）实现软件渲染，让玩家无需安装 Java 环境即可直接在浏览器中体验原作的像素风格、解谜和战斗内容，同时保留了原游戏的核心架构和关卡设计系统。

- 🎮 **游戏起源**：复刻自 Notch 在 2011 年 Ludum Dare 大赛中开发的 Java 游戏《Prelude of the Chambered》
- 🌐 **技术移植**：将 Java 代码完整重写为 TypeScript，使用 Vite 构建，支持浏览器直接运行
- 🧩 **核心特性**：采用纯软件渲染（Canvas 2D API），保留原版光线投射引擎和像素风格
- 🗺️ **关卡设计**：沿用基于 PNG 图像的关卡系统，像素颜色对应不同游戏元素（如墙壁、机关）
- 🏗️ **模块化架构**：代码分为渲染、实体、关卡、菜单等独立模块，便于维护和扩展
- ⚔️ **游戏内容**：包含 6 个关卡、多种敌人和 Boss、道具收集系统及解谜机制
- 🔧 **开发挑战**：解决 Java 到 TypeScript 的类型转换、游戏循环重构和输入处理适配
- 📂 **开源贡献**：项目开放源代码，支持漏洞修复、素材优化和移动端适配等协作
- 🚀 **现代部署**：通过 GitHub Actions 实现自动部署，强调 Web 游戏的便捷性和可访问性

---

### [入门指南 | Angular 技巧](https://ngtips.com/)

**原文标题**: [Getting started | Angular Tips](https://ngtips.com/)

Angular Tips 是一份面向开发者的文档，旨在指导构建复杂、大规模且需长期维护的工业级 Web 应用，可能不适用于简单应用。它汇集了 Angular 专家的最佳实践，帮助开发者避免常见陷阱，理解框架特性的使用原因与方式。文档基于 Angular v21 编写，遵循与 Angular 相同的主版本号，并采用特定词汇区分建议强度。

- 📘 **文档目标**：指导构建复杂、可长期维护的大型 Angular 应用，可能不适用于简单项目。
- 🎯 **核心动机**：分享 Angular 专家经验，帮助开发者理解最佳实践、避免常见错误，明确技术选型的原因。
- 🔢 **版本对应**：基于 Angular v21 编写，与 Angular 主版本号同步（从 v19 开始），旧版本用户可参考对应历史文档。
- 📖 **指南分类**：通过“Do”（应遵循）、“Consider”（建议遵循）、“Avoid”（应避免）等词汇区分建议强度，并配有 ✅ 和 ❌ 图标示例。

---

### [开源 Remix 商店 | Remix](https://remix.run/blog/oss-remix-store)

**原文标题**: [Open Sourcing the Remix Store | Remix](https://remix.run/blog/oss-remix-store)

Remix 团队开源了其官方商店的源代码，旨在为 React Router 和 Shopify 开发者提供学习参考，并分享构建过程中的经验与挑战。

- 🛒 **开源商店代码**：Remix 团队宣布开源其官方商店的源代码，以帮助 React Router 和 Shopify 开发者学习实际项目。
- 🎯 **目标受众明确**：商店主要面向 Remix 用户、Hydrogen 用户和 Shopify 开发者，用于宣传、教育及内部协作。
- 🛠️ **构建历程分享**：文章详细介绍了从设计、开发到最终上线的全过程，包括团队协作、资源申请及多次迭代。
- 🎨 **独特设计功能**：商店包含多个创新交互功能，如滚动同步的 3D 连帽衫、集合页面标题的“爆炸”效果、产品图片模糊加载等。
- 🔄 **技术实践与优化**：利用 Hydrogen 和 React Router 实现乐观购物车、错误页面的故障文本效果等，以提升用户体验。
- 📈 **持续改进计划**：团队计划推出新产品、更新主页、优化国际运费，并最终将商店迁移至 Remix 3。
- 🤝 **鼓励社区贡献**：邀请开发者查看代码、提交问题或拉取请求，并提供 15% 的折扣码以表感谢。

---

### [首页 | 混音商店](https://shop.remix.run/)

**原文标题**: [Home | The Remix Store](https://shop.remix.run/)

Remix 品牌提供一系列面向工程师和网站开发者的服饰及周边商品，涵盖不同款式与价格。

- 👕 连帽衫选择多样，如 Remix Engineering Hoodie 黑色与深灰色款，售价均为 $62.00
- 🏃 跑步主题服饰包括 Run Club L/S Shirt 蓝色与白色款，价格各为 $31.00
- 👔 T 恤款式丰富，例如 Remix Engineering T-shirt 和 Load in Parallel T-shirt，单价 $29.00
- 🧢 配件类有 Remix Engineering Hat 和 Remix Better Web Hat，每顶售价 $29.00
- 📓 其他周边含 Remix Sticker Pack 贴纸包 $6.00 与 Remix Notebook 笔记本 $14.00

---

### [混音 - 构建更优网站](https://remix.run/)

**原文标题**: [Remix - Build Better Websites](https://remix.run/)

Remix 是一个全栈 Web 框架，专注于通过 Web 标准和现代用户体验来构建更优秀的网站。它强调从用户界面出发，利用嵌套路由、并行数据加载和内置表单处理等特性，提供快速、流畅且具有弹性的用户体验。框架支持渐进增强、内置错误处理，并能运行在各种服务器环境中。

- 🚀 **专注于现代 Web 体验**：Remix 通过 Web 标准和现代 UX 设计，帮助开发者构建更快、更顺滑的网站。
- 🔗 **嵌套路由优化**：通过嵌套路由实现数据与视图的并行加载，减少加载状态和界面卡顿。
- ⚡ **并行数据预取**：支持预取数据、模块和 CSS，实现近乎即时的页面切换，避免加载等待。
- 📝 **内置表单处理**：提供渐进增强的数据变更支持，简化表单提交、状态管理和乐观 UI 实现。
- 🛡️ **错误边界处理**：内置错误处理机制，通过路由级错误边界保持应用部分功能可用，提升稳定性。
- 🌍 **多环境部署**：基于 Web Fetch API，可原生运行于 Cloudflare Workers、无服务器及传统 Node.js 环境。

---

### [氢：Shopify 的无头商务框架](https://hydrogen.shopify.dev/)

**原文标题**: [Hydrogen: Shopifyâs headless commerce framework](https://hydrogen.shopify.dev/)

Shopify Hydrogen 是一个专为电商优化的无头前端框架，基于 Remix 构建，旨在提升开发效率和网站性能，支持快速构建高性能的电商网站。

- 🚀 **快速启动**：通过命令行工具快速创建项目，几分钟内即可从零搭建到运行。
- ⚡️ **性能优化**：采用服务器端渲染和边缘计算，减少客户端 JavaScript，提升页面加载速度和稳定性。
- 🛒 **电商功能集成**：内置购物车、多市场支持、Shop Pay 支付、客户账户等核心电商功能。
- 🔧 **灵活开发**：提供可定制的 UI 组件和样式库支持（如 Tailwind、CSS Modules），适配多种开发需求。
- 🌍 **全球部署**：通过 Oxygen 全球托管服务，实现低延迟访问，覆盖 300+ 节点。
- 🔌 **可扩展性**：支持与任何 API 集成，兼容 Shopify 生态系统及第三方应用。
- 📊 **分析与营销**：内置数据分析、像素跟踪和折扣链接等功能，优化营销效果。
- 🆓 **免费使用**：Oxygen 托管在多数 Shopify 套餐中免费提供，降低开发成本。

---

### [获取失败](https://javascriptweekly.com/link/178465/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/178465/web)

无法总结：获取内容失败，状态码 429。

---

### [获取失败](https://javascriptweekly.com/link/178438/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/178438/web)

无法总结：获取内容失败，状态码 404。

---

### [GitHub - github/relative-time-element：标准<time>元素的Web组件扩展。](https://github.com/github/relative-time-element)

**原文标题**: [GitHub - github/relative-time-element: Web component extensions to the standard <time> element.](https://github.com/github/relative-time-element)

这是一个用于扩展标准 `<time>` 元素的 Web 组件，能够将时间戳格式化为本地化字符串或自动更新的相对时间文本。

- 🕐 **核心功能**：提供 `<relative-time>` 自定义元素，根据用户浏览器设置和偏好，将 ISO 8601 时间戳自动本地化并动态显示为相对时间（如“2 天前”）或绝对日期。
- 📦 **安装与兼容**：可通过 npm 安装 `@github/relative-time-element`。依赖现代浏览器的 `Intl.DateTimeFormat` 和 `Intl.RelativeTimeFormat` API，旧版浏览器可能需要相应 polyfill。
- ⚙️ **多种显示格式**：支持 `datetime`（本地化绝对日期）、`relative`（默认，显示相对时间，超过阈值如 30 天则显示绝对日期）、`duration`（显示精确的时长分解）等格式，并包含一些已弃用的格式选项。
- 🌍 **本地化与时区**：利用 `lang` 属性确定语言，支持通过 `time-zone` 属性指定 IANA 时区名称，元素会沿 DOM 树向上查找最近的设置或使用浏览器默认值。
- 🔧 **丰富属性配置**：提供 `tense`（控制时态）、`precision`（控制显示精度）、`threshold`（控制相对时间转为绝对日期的阈值）、`prefix`（绝对日期前缀）等多种属性进行细粒度控制。
- ⚛️ **框架集成**：文档说明了如何在 React 项目中通过类型声明来使用该自定义元素。
- 📄 **许可证与资源**：项目采用 MIT 许可证，在 GitHub 上开源，拥有大量星标和分支，并提供了详细的使用文档、示例和贡献指南。

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=q4)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=q4)

Meticulous AI 是一款通过记录用户交互自动生成并维护端到端测试的 AI 工具，旨在帮助开发团队无需编写或维护测试代码即可实现全面的应用测试覆盖，从而提升开发效率和代码质量。

- 🚀 **自动生成测试**：通过记录开发、预演等环境中的用户交互，AI 自动生成覆盖所有代码分支和用户流程的测试套件。
- 🛡️ **零维护与无抖动**：测试随应用自动更新，从底层消除测试抖动，确保结果稳定可靠。
- ⚡ **快速集成与执行**：支持主流前端框架，添加脚本即可快速集成；测试高度并行化，可在 120 秒内完成数千次测试。
- 🔄 **实时影响预览**：在合并代码前，通过拉取请求预览改动对现有用户流程的影响，避免回归问题。
- 🌟 **企业级认可**：已被 Dropbox、Notion 等超过 100 家组织采用，帮助团队防止回归并提升开发信心。

---

### [GitHub - poppinss/ts-exec：使用SWC在Node上执行TypeScript](https://github.com/poppinss/ts-exec)

**原文标题**: [GitHub - poppinss/ts-exec: Execute TypeScript on Node using SWC](https://github.com/poppinss/ts-exec)

ts-exec 是一个基于 SWC 构建的 TypeScript 即时编译器，允许在 Node.js 中直接运行 TypeScript 和 JavaScript 文件，无需预先编译步骤。它严格遵循 Node.js 模块解析规则，确保开发与生产环境行为一致，并全面支持 ESM、TypeScript 特性及零配置使用。

- 🚀 **基于 SWC 的 TypeScript 即时编译器** – 直接在 Node.js 中运行 `.ts` 和 `.tsx` 文件，无需构建步骤。
- 🛡️ **生产安全的导入规则** – 强制遵循 Node.js 模块解析，避免开发与生产环境的不一致问题。
- ⚡ **现代轻量基础** – 基于 SWC 构建，代码少于 200 行，启动快速且资源占用低。
- 📦 **完整的 ESM 支持** – 为 Node.js 24 及以上版本提供一流的 ECMAScript 模块支持。
- 🎨 **全面 TypeScript 功能** – 支持枚举、旧版装饰器、命名空间导入和 JSX 语法。
- ⚙️ **零配置体验** – 自动解析 `tsconfig.json`，无需额外配置文件。
- 🔄 **导入扩展名处理** – 支持通过 `rewriteRelativeImportExtensions` 选项在导入中使用 `.ts` 扩展名。
- 📍 **子路径导入别名兼容** – 支持 `package.json` 中定义的导入别名，确保开发与编译后路径一致。
- 🤔 **与其他工具对比** – 相比 `tsx` 和 `ts-node`，更注重 Node.js 兼容性和旧版装饰器支持。
- 📜 **开源与社区驱动** – 采用 MIT 许可证，鼓励社区贡献并遵循行为准则。

---

### [AdonisJS - 一款功能齐全的 Node.js 网络框架](https://adonisjs.com/)

**原文标题**: [AdonisJS - A fully featured web framework for Node.js](https://adonisjs.com/)

AdonisJS 是一个现代化的 Node.js 全栈框架，提供类型安全、高性能、丰富的核心功能以及出色的开发体验，包括一流的测试支持和大量官方维护的包，深受全球开发者喜爱。

- 🛡️ **类型安全**：框架 API 设计注重类型安全、智能提示和自动导入支持。
- 📦 **ESM 就绪**：利用现代 JavaScript 特性，包括 ES 模块和 Node.js 子路径导入。
- ⚡ **高性能**：内置最快的验证库之一，HTTP 服务器性能与 Fastify 相当。
- 🧩 **功能丰富的核心**：单一 npm 包提供创建 Web 应用所需的所有基础功能，无需组装多个包。
- 🔧 **配置管理**：包括类型安全的环境变量、合理的文件夹结构、路由、控制器、中间件、文件上传等。
- 🧪 **一流的测试体验**：提供管理测试数据库、模拟依赖、生成假数据等原语，支持浏览器测试、Open API 测试等。
- 📚 **官方维护的包集合**：包括 Lucid ORM、Auth 认证、Bouncer 授权、FlyDrive 文件管理、VineJS 验证等。
- 💬 **开发者好评**：全球开发者称赞其文档完善、易于上手，类似 Laravel 但用于 Node.js，提升开发效率。
- 💖 **开源支持**：项目依赖 GitHub 赞助商支持，保持独立和开源。

---

### [Node.js — 原生运行 TypeScript](https://nodejs.org/en/learn/typescript/run-natively)

**原文标题**: [Node.js — Running TypeScript Natively](https://nodejs.org/en/learn/typescript/run-natively)

Node.js 现已支持直接运行 TypeScript 代码，无需预先转译，简化了开发流程。

- 🚀 **无需转译**：在 Node.js v22.18.0 及以上版本中，若源代码仅包含可擦除的 TypeScript 语法，可直接执行 TypeScript 文件。
- ⚙️ **版本兼容**：低于 v22.18.0 的版本需使用 `--experimental-strip-types` 标志来运行 TypeScript 文件。
- 🔧 **高级功能**：v22.7.0 引入 `--experimental-transform-types` 标志，支持需转换的语法（如 `enum` 和 `namespace`），并自动启用类型剥离。
- 🛑 **灵活控制**：可通过 `--no-experimental-strip-types` 标志禁用类型剥离功能。
- 📋 **配置建议**：Node.js 的 TypeScript 加载器（Amaro）不依赖 `tsconfig.json`，但建议配置编辑器和 `tsc` 以匹配 Node.js 行为，使用 TypeScript 5.7 或更高版本。
- ⚠️ **注意事项**：需注意 TypeScript 支持的约束条件，详细信息可参考 API 文档。

---

### [GitHub - poppinss/ts-exec：使用SWC在Node上执行TypeScript](https://github.com/poppinss/ts-exec?tab=readme-ov-file#-why-ts-exec-exists)

**原文标题**: [GitHub - poppinss/ts-exec: Execute TypeScript on Node using SWC](https://github.com/poppinss/ts-exec?tab=readme-ov-file#-why-ts-exec-exists)

ts-exec 是一个基于 SWC 构建的 TypeScript 即时编译器，允许在 Node.js 中直接运行 TypeScript 和 JavaScript 代码，无需预先编译，并完全支持 Node.js 24 及更高版本的 ESM。

- 🚀 **直接执行 TypeScript**：无需构建步骤，可直接运行 `.ts` 和 `.tsx` 文件。
- 🛡️ **生产安全的导入**：严格遵循 Node.js 模块解析规则，确保开发与生产环境行为一致。
- ⚡ **现代轻量基础**：基于 SWC 构建，少于 200 行代码，性能高效。
- 📦 **ESM 优先支持**：为 ECMAScript 模块提供一流支持。
- ⚙️ **零配置体验**：无需额外配置文件，自动解析 `tsconfig.json`。
- ✅ **完整 TypeScript 功能**：支持枚举、旧版装饰器、命名空间导入和 JSX 语法。
- 🔄 **导入扩展处理**：支持在 `tsconfig.json` 中启用 `rewriteRelativeImportExtensions`，自动重写 `.ts` 扩展为 `.js`。
- 📍 **子路径导入别名**：通过 `package.json` 定义别名，始终指向编译后的 `.js` 文件路径。
- 🤔 **与 tsx 对比优势**：强制使用显式文件扩展名，避免开发与生产环境的不一致问题，并支持旧版装饰器。
- 📊 **功能全面对比**：在维护活跃度、SWC 基础、装饰器支持、导入合规性等方面优于 ts-node 和 tsx。
- 📥 **安装与使用**：通过 npm 安装，可通过 `node --import` 直接运行或编程方式导入。
- 🤝 **社区与贡献**：鼓励社区贡献，提供行为准则和贡献指南。
- 📜 **开源许可**：基于 MIT 许可证开源。

---

### [Vue Toast 通知演示场 | Toastflow](https://toastflow.adrianjanocko.sk/)

**原文标题**: [Vue Toast Notifications Playground | Toastflow](https://toastflow.adrianjanocko.sk/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能整合临床数据，减少医护人员行政负担
- ⚖️ 数据隐私与算法透明度仍是医疗 AI 推广过程中需要应对的关键伦理问题

---

### [GitHub - adrianjanocko/toastflow：框架无关的提示引擎，附带Vue 3 渲染器。类型化核心、流畅的堆叠动画、CSS 优先主题定制，以及对布局和行为的完全控制。](https://github.com/adrianjanocko/toastflow)

**原文标题**: [GitHub - adrianjanocko/toastflow: Framework-agnostic toast engine with a Vue 3 renderer. Typed core, smooth stack animations, CSS-first theming, and full control over layout and behavior.](https://github.com/adrianjanocko/toastflow)

Toastflow 是一个与框架无关的轻量级消息通知引擎，提供 Vue 3 渲染器，支持类型化核心、流畅的堆叠动画、CSS 优先的主题定制，以及对布局和行为的完全控制。

- 🚀 **框架无关** – 核心引擎独立于框架，可通过 Vue 3 渲染器或自定义方式使用
- 🎨 **CSS 优先主题** – 通过 CSS 变量轻松定制外观，支持动画覆盖
- ⚙️ **全面控制** – 可配置位置、持续时间、重复项处理、悬停暂停等行为
- 🔌 **灵活集成** – 支持在组件、TS/JS 模块或服务中调用，提供无头渲染插槽
- 📦 **类型安全** – 基于 TypeScript 构建，提供完整的类型支持
- 🛠️ **丰富功能** – 支持异步流程、HTML 内容、事件订阅与状态访问
- 🌐 **开源许可** – 采用 MIT 许可证，欢迎社区贡献

---

### [GitHub - sveltejs/devalue：当JSON.stringify力不从心时的得力助手](https://github.com/sveltejs/devalue)

**原文标题**: [GitHub - sveltejs/devalue: Gets the job done when JSON.stringify can't](https://github.com/sveltejs/devalue)

devalue 是一个用于序列化 JavaScript 值的库，类似于 JSON.stringify，但能处理循环引用、重复引用、特殊值（如 undefined、NaN）以及多种内置类型（如 Map、Set、Date 等），同时支持自定义类型序列化，并提供 XSS 防护功能。

- 🛠️ **功能丰富**：支持序列化循环引用、重复引用、undefined、NaN、正则表达式、Date、Map、Set、BigInt 等 JSON.stringify 无法处理的值。
- 🔄 **两种使用方式**：提供 `uneval` 生成紧凑的 JavaScript 代码，以及 `stringify`/`parse` 用于类似 JSON 的序列化与反序列化。
- 🛡️ **安全防护**：自动转义 HTML 特殊字符，有效防止 XSS 攻击，确保服务器到客户端的数据传输安全。
- 🧩 **自定义类型支持**：允许通过 reducers 和 revivers 序列化和反序列化自定义类或对象。
- ⚠️ **错误处理**：在遇到无法序列化的值（如函数）时抛出错误，并提供 `error.path` 帮助定位问题来源。
- 📦 **轻量与高效**：注重性能、安全性和输出紧凑性，适用于状态序列化和数据传输场景。
- 🔗 **生态集成**：属于 Svelte 项目生态系统，广泛应用于前端开发，被超过 62.6 万个项目使用。

---

### [贬值演示 • 游乐场 • Svelte](https://svelte.dev/playground/138d70def7a748ce9eda736ef1c71239)

**原文标题**: [devalue demo â¢ Playground â¢ Svelte](https://svelte.dev/playground/138d70def7a748ce9eda736ef1c71239)

Svelte 框架核心概念与功能概览，涵盖从基础语法到高级特性的完整开发指南。

- 🚀 **动态属性**：允许组件属性根据数据变化动态更新。
- 🎨 **样式系统**：支持组件作用域的 CSS 与动态样式绑定。
- 🧩 **嵌套组件**：通过组合简单组件构建复杂界面结构。
- 🔗 **HTML 标签集成**：可直接在组件中使用原生 HTML 元素。
- ⚡ **响应式系统**：基于赋值自动更新 UI，无需手动 DOM 操作。
- 📝 **响应式声明**：使用`$:`语法创建衍生状态与副作用。
- 🎯 **属性传递**：通过 props 实现父子组件数据通信，支持默认值与展开语法。
- 🧠 **逻辑控制**：提供`{#if}`、`{#each}`、`{#await}`等模板逻辑块。
- 🎪 **事件处理**：支持 DOM 事件、组件事件传递与事件修饰符。
- 🔗 **数据绑定**：实现表单输入、媒体元素等双向数据绑定。
- ⏳ **生命周期**：包含`onMount`、`onDestroy`等钩子函数与`tick`API。
- 🏪 **状态管理**：提供可写/只读/衍生存储及自定义存储方案。
- ✨ **动画特效**：内置补间/弹簧动画、CSS/JS 过渡及 SVG 动画支持。
- 🛠️ **指令系统**：包含`use`动作指令、`class`类绑定等扩展功能。
- 🧱 **组件架构**：支持渲染属性、条件渲染及上下文 API 通信。
- 🧩 **特殊元素**：提供`<svelte:element>`等编译时特殊标签。
- 🐛 **调试工具**：通过`@debug`标签实现状态跟踪与问题定位。
- 📱 **实战案例**：包含 7GUIs 经典案例及 HackerNews 等完整项目示例。

---

### [介绍 iceberg-js：Apache Iceberg 的 JavaScript 客户端](https://supabase.com/blog/introducing-iceberg-js)

**原文标题**: [Introducing iceberg-js: A JavaScript Client for Apache Iceberg](https://supabase.com/blog/introducing-iceberg-js)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时提及了相关的伦理挑战和未来发展趋势。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 🔬 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 🧬 基于基因数据的个性化治疗方案正成为精准医疗的核心发展方向
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任界定等伦理监管挑战
- 🌐 远程医疗与可穿戴设备结合，推动慢性病管理的智能化转型

---

### [Inertia.js - 现代单体架构](https://inertiajs.com/)

**原文标题**: [Inertia.js - The Modern Monolith](https://inertiajs.com/)

Inertia 是一个现代全栈框架，允许开发者使用 React、Vue 或 Svelte 构建单页应用体验，同时保留传统的服务器端路由和逻辑，无需编写 API 接口，并能与多种后端框架无缝集成。

- 🚀 支持使用 React、Vue 或 Svelte 开发单页应用，并享受服务器端路由的优势
- 🔌 可与 Laravel、Rails、Django 等多种后端框架即插即用，无需额外 API
- 🛠️ 提供生产就绪功能，如表单处理、SEO 优化、部分重载和实时轮询
- 🔄 实现服务器状态同步、资源版本控制和身份验证，后端作为单一数据源
- ⚡ 支持预取、延迟属性和无限滚动，以优化性能和用户体验
- 📚 提供详细文档和 Laravel 入门套件，便于快速上手和部署

---

### [发布 v6.3.0 · openpgpjs/openpgpjs · GitHub](https://github.com/openpgpjs/openpgpjs/releases/tag/v6.3.0)

**原文标题**: [Release v6.3.0 · openpgpjs/openpgpjs · GitHub](https://github.com/openpgpjs/openpgpjs/releases/tag/v6.3.0)

OpenPGP.js 发布了 v6.3.0 版本，主要更新包括对 Node.js v24 的支持、新增配置选项以限制解压消息大小、优化压缩/解压性能、降低内存使用，并改进了文档和持续集成流程。

- 🆕 支持 Node.js v24
- ⚙️ 新增配置选项限制解压消息大小，防止内存过度使用
- 🔄 切换压缩库至 unbzip2-stream，提升解压效率
- 🚀 非流式处理时使用原生压缩 API，提高性能
- 💾 采用无缓冲转换，降低流式处理内存占用
- 📚 优化 JSDoc 文档，仅包含用户相关接口并添加 TypeScript 支持
- 🔧 更新依赖版本并改进持续集成流程

---

### [HackerOne 打造的 React 日期选择器](https://reactdatepicker.com/)

**原文标题**: [React Datepicker crafted by HackerOne](https://reactdatepicker.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🏥 AI 辅助诊断系统能通过分析医学影像提升疾病检测的准确性与效率
- 💊 机器学习可帮助制定个性化治疗方案并预测药物反应
- 📊 智能管理系统优化医院资源分配，减少患者等待时间
- ⚠️ 数据隐私、算法偏见和临床验证仍是需要克服的主要挑战
- 🔮 未来 AI 有望与人类医生协同工作，实现更精准高效的医疗服务

---

### [GitHub - omnibrain/svguitar：创建精美的SVG吉他弦图](https://github.com/omnibrain/svguitar)

**原文标题**: [GitHub - omnibrain/svguitar: Create beautiful SVG guitar chord charts](https://github.com/omnibrain/svguitar)

SVGuitar 是一个用于在浏览器中直接创建美观的 SVG 吉他指法图的 JavaScript（TypeScript）库，它高度可定制，并支持多种配置选项。

- 🎸 **功能核心**：直接在浏览器中生成 SVG 格式的吉他指法图。
- ⚙️ **高度可定制**：提供丰富的配置选项，可调整指法样式、标题、调弦、指板标记等。
- 📦 **易于集成**：可通过 UMD 脚本直接引入，或通过 npm、yarn、pnpm 安装为项目依赖。
- 🎨 **应用示例**：被 ChordPic、muted.io 等多个在线音乐工具和项目所使用。
- 🔧 **技术支持**：拥有详细的 TypeScript API 文档和在线演示。
- 🌐 **开源项目**：采用 MIT 许可证，鼓励贡献和协作开发。

---

### [发布 pnpm 10.25 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.25.0)

**原文标题**: [Release pnpm 10.25 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.25.0)

pnpm 10.25.0 版本发布，引入了对特定注册表 URL 证书加载的支持，新增了用于创建最小化 package.json 的 `--bare` 标志，并包含多项错误修复与功能改进。

- 🔧 允许为特定注册表 URL 从 `cert`、`ca` 和 `key` 加载证书，扩展了安全配置选项
- 📄 新增 `pnpm init --bare` 标志，可创建仅含必需字段的最小化 package.json 文件
- 🐛 改进了被忽略依赖脚本的报告显示，提升调试体验
- 🔨 确保 `pnpm install` 会构建已添加到 `onlyBuiltDependencies` 但尚未构建的依赖
- 📤 允许 `pnpm publish -r --force` 覆盖注册表中已存在的版本
- ⚠️ 修复了当被排除在信任策略检查外的包缺少元数据时间字段时的错误处理

---

### [GitHub - lydell/js-tokens：微型JavaScript词法分析器。](https://github.com/lydell/js-tokens)

**原文标题**: [GitHub - lydell/js-tokens: Tiny JavaScript tokenizer.](https://github.com/lydell/js-tokens)

js-tokens 是一个基于正则表达式的轻量级 JavaScript 词法分析器，能够稳定处理几乎所有 JavaScript 代码，包括无效语法，并支持 JSX 和最新 ECMAScript 标准。

- 🧩 轻量且稳定：基于正则表达式实现，体积小巧，处理代码时几乎不会失败
- 🔄 生成器函数：将 JavaScript 字符串转换为可迭代的词法单元对象序列
- 🧱 词法单元丰富：支持字符串、模板、正则表达式、注释、标识符、数字、标点等类型
- ⚛️ JSX 支持：通过选项启用 JSX 词法分析，支持 JSX 字符串、文本、标识符等特有词法单元
- 📜 规范兼容：高度遵循 ECMAScript 词法规范，仅存在少量已知边界情况
- ⚡ 性能优异：相比 Babel 解析器，在处理大型文件时速度显著更快
- 🔧 宽松处理：即使面对无效语法也能返回词法单元，不会抛出异常
- 🧪 测试全面：通过绝大多数 test262 解析器测试，确保可靠性

---

### [Trigger.dev | 构建并部署全托管 AI 智能体与工作流。](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=trigger.dev-december&utm_term=jsweekly&utm_content=homepage)

**原文标题**: [Trigger.dev | Build and deploy fully-managed AI agents and workflows.](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=trigger.dev-december&utm_term=jsweekly&utm_content=homepage)

Trigger.dev 是一个用于构建和部署全托管 AI 代理与工作流的 TypeScript 平台，专注于处理长时间运行的任务，并提供重试、队列、可观测性和弹性扩展等功能。

- 🚀 **构建 AI 工作流**：使用 TypeScript 构建 AI 代理和工作流，支持长时间运行的任务，具备自动重试、队列管理、可观测性和弹性扩展。
- 🔄 **可靠执行**：无超时限制，自动重试和追踪，支持现有 Node.js SDK 和代码库，确保 AI API 调用的可靠性。
- 🤖 **AI 代理功能**：支持自主代理、提示链、路由、并行化、协调器和评估优化器，用于处理复杂任务和多阶段流程。
- 📈 **部署与扩展**：无需管理服务器，按实际执行付费，支持多区域工作器、静态 IP、并发队列和弹性基础设施。
- 🐛 **调试与监控**：提供错误警报、高级筛选、版本控制、日志追踪和实时运行状态显示，便于快速发现和修复问题。
- 🌐 **实时功能**：通过 Trigger.dev Realtime 在应用中实时显示任务状态，并支持将 LLM 响应流式传输到前端。
- 🔧 **开发灵活性**：支持自定义构建过程，集成 Python、Prisma、Puppeteer、esbuild、FFmpeg 等工具，满足多样化开发需求。
- 💬 **社区与开源**：Apache 2.0 开源许可，拥有活跃的 GitHub 社区和 Discord 成员，深受开发者喜爱。
- 🏆 **用户认可**：被多家公司用于关键业务功能，如视频处理、邮件活动、AI 工作流等，提高了开发效率和系统可靠性。
- 💰 **简单定价**：按使用量付费，支持自托管，提供免费起步选项，适合不同规模的团队和项目。

---

### [开发者套餐：每月 5 美元的 PostgreSQL 与 MySQL 服务 | Aiven](https://aiven.io/developer-tier?utm_source=freeman-forrest&utm_medium=referral&utm_campaign=aiven-december&utm_term=jsweekly&utm_content=developertier)

**原文标题**: [Developer Tier: PostgreSQL & MySQL for $5/Mo | Aiven](https://aiven.io/developer-tier?utm_source=freeman-forrest&utm_medium=referral&utm_campaign=aiven-december&utm_term=jsweekly&utm_content=developertier)

该服务提供每月 5 美元的 PostgreSQL 和 MySQL 数据库方案，具备企业级功能与高可用性，适合应用与代理开发。

- 💰 每月仅需 5 美元，无隐藏费用
- 🛡️ 提供企业级 PostgreSQL 和 MySQL 数据库服务
- 📊 具备 99.99% 的高可用性保证
- 🔄 包含备份与技术支持
- 🚀 支持快速开始应用与代理开发
- 📚 提供详细文档查阅

---

### [密歇根 TypeScript 创始人成功在 Ty...内运行《毁灭战士》](https://socket.dev/blog/typescript-types-running-doom)

**原文标题**: [Michigan TypeScript Founder Successfully Runs Doom Inside Ty...](https://socket.dev/blog/typescript-types-running-doom)

Deno 2.6 版本引入了 deno audit 命令及新的--socket 标志，可直接集成 Socket，为 Deno 命令行工具带来供应链安全检查功能。

- 🛡️ Deno 2.6 新增 deno audit 命令，强化安全审计
- 🔌 通过--socket 标志直接集成 Socket 供应链安全检测
- ⚙️ 将供应链安全检查融入 Deno CLI 工作流
- 📅 功能于 2025 年 12 月 12 日由 Sarah Gooding 发布

---

### [- YouTube](https://www.youtube.com/watch?v=IP6EZXzXBzY)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=IP6EZXzXBzY)

该页面为 YouTube 平台的政策与信息索引，列出了其核心功能、法律条款及用户指南。

- 📄 关于平台的基本介绍与背景信息
- 📰 官方新闻发布与媒体资源
- ©️ 版权保护政策与内容所有权说明
- 📞 用户联系与客服支持渠道
- 🎬 内容创作者专属资源与工具
- 📢 广告合作与商业推广服务
- 💻 开发者接口与技术文档
- ⚖️ 平台使用条款与协议
- 🔒 隐私保护政策与数据安全措施
- 🛡️ 平台安全政策与社区准则
- ⚙️ YouTube 功能运作机制说明
- 🧪 新功能测试与体验计划
- 📅 2025 年谷歌公司版权所有声明

---

### [CSS 2025 年度回顾](https://chrome.dev/css-wrapped-2025/)

**原文标题**: [CSS Wrapped 2025](https://chrome.dev/css-wrapped-2025/)

本文介绍了 2024 年 CSS 和 Web 平台的一系列新特性与改进，涵盖交互组件、滚动体验、动画优化及样式增强等方面，旨在提升开发者构建现代 Web 应用的能力与效率。

- 🎛️ **调用器命令**：通过`commandfor`和`command`属性，无需 JavaScript 即可声明式控制对话框和弹出层的显示与隐藏，支持自定义命令。
- 🖱️ **对话框轻量关闭**：为`<dialog>`元素新增`closedby`属性，支持点击外部或按 ESC 键关闭对话框，提升用户体验。
- 💡 **提示弹出层**：新增`popover="hint"`类型，用于创建临时性 UI（如工具提示），可与其他弹出层共存，并支持通过`interestfor`属性触发。
- 🎨 **可自定义选择框**：通过`appearance: base-select`完全用 CSS 样式化`<select>`元素，支持 HTML 内容嵌入和下拉列表顶层渲染。
- 🚗 **滚动按钮与标记**：引入`::scroll-button()`和`::scroll-marker()`伪元素，无需 JavaScript 即可创建可访问的轮播导航和标记指示。
- 🔗 **滚动目标组**：使用`scroll-target-group`属性将锚点链接列表转换为滚动标记，实现滚动监听导航。
- 🎯 **锚点容器查询**：通过`container-type: anchored`和`anchored()`函数，根据锚点定位的备用位置动态样式化元素（如工具提示箭头方向）。
- ⏳ **兴趣调用器**：新增`interestfor`属性，基于悬停或聚焦事件声明式触发 UI，支持延迟设置，便于创建工具提示等交互。
- 📜 **滚动状态查询**：使用`container-type: scroll-state`查询元素是否处于滚动、吸附或固定状态，并相应应用样式。
- 🔢 **树计数函数**：引入`sibling-index()`和`sibling-count()`函数，简化基于元素位置的动画和布局计算。
- 🎞️ **嵌套视图过渡组**：扩展视图过渡 API，支持嵌套`::view-transition-group`以保留 3D 和裁剪效果。
- 🧩 **DOM 状态保留移动**：使用`moveBefore`方法移动元素（如 iframe、视频）时保持其状态（如播放进度），避免重新加载。
- 🛠️ **增强 attr() 函数**：扩展`attr()`函数支持更多 CSS 属性和数据类型（如颜色、长度），实现动态样式绑定。
- 🎭 **ToggleEvent.source**：通过`ToggleEvent.source`属性识别触发弹出层、对话框等切换事件的元素，便于处理用户操作。
- 📏 **文本框特性**：新增`text-box-trim`和`text-box-edge`属性，优化文本垂直对齐，实现视觉居中。
- ✂️ **shape() 函数**：提供`shape()`函数用于创建复杂、响应式的裁剪形状，支持动画和自定义属性控制。
- ⚖️ **if() 语句**：在 CSS 中引入`if()`条件函数，基于媒体查询、特性支持或样式查询动态设置属性值。
- 🔧 **自定义函数**：通过`@function`定义可重用的 CSS 函数，提升样式代码的模块化和维护性。
- 📊 **扩展范围语法**：在样式查询和`if()`语句中支持范围比较运算符（如`>`、`<`），实现更灵活的样式逻辑。
- 📐 **拉伸尺寸关键字**：新增`stretch`关键字用于尺寸属性，使元素填充包含块空间并保留外边距。
- 🔶 **角落形状**：引入`corner-shape`属性，支持多种角落形状（如斜角、凹槽、圆形等），增强边框样式设计。

---

### [聊聊 GitHub Actions - GitHub 博客](https://github.blog/news-insights/product-news/lets-talk-about-github-actions/)

**原文标题**: [Let’s talk about GitHub Actions - The GitHub Blog](https://github.blog/news-insights/product-news/lets-talk-about-github-actions/)

GitHub Actions 在 2025 年经历了核心架构的重大重构，以应对快速增长的使用量（每日处理任务从 2300 万增至 7100 万），并在此基础上推出了多项社区期待已久的改进，包括 YAML 锚点、非公开工作流模板、更深的可重用工作流嵌套、更大的缓存空间以及更多工作流调度输入选项。团队计划在 2026 年继续优化，引入时区支持、并行步骤等功能，并邀请用户通过社区反馈共同规划未来路线图。

- 🚀 **核心架构重构**：为应对快速增长，GitHub Actions 彻底重建了后端服务，使每日处理任务能力提升至 7100 万，为性能和可靠性打下基础。
- 📈 **使用量大幅增长**：2025 年公开和开源项目中的 GitHub Actions 使用分钟数达 115 亿，同比增长 35%。
- 🔧 **YAML 锚点支持**：通过锚点和别名减少工作流配置重复，提升复杂工作流的维护效率。
- 🏢 **非公开工作流模板**：允许组织在内部仓库中创建私有模板，确保团队 CI/CD 流程的一致性。
- 🔄 **可重用工作流深度增加**：支持 10 层嵌套和 50 个工作流调用，助力模块化、大规模流水线构建。
- 💾 **缓存空间扩大**：突破 10GB 限制，满足依赖复杂或大型项目的构建需求，减少重复下载。
- 🎛️ **工作流调度输入扩展**：手动触发工作流的输入参数从 10 个增至 25 个，支持更丰富的自动化场景。
- 📅 **2026 年规划**：将推出时区支持、并行步骤、页面加载优化等功能，持续提升开发者体验。
- 💬 **社区参与**：鼓励用户通过社区讨论投票和反馈，共同塑造 2026 年的产品路线图。

---

### [为您心仪的网页功能投票  |  博客  |  web.dev](https://web.dev/blog/upvote-features)

**原文标题**: [Vote for the web features you want to see  |  Blog  |  web.dev](https://web.dev/blog/upvote-features)

WebDX 社区推出新功能，让开发者能直接为希望跨浏览器实现互操作的网页功能投票，以此向浏览器厂商传达需求。

- 🗳️ **投票表达需求**：在 web.dev、caniuse.com 等平台点击“Upvote”按钮，即可对特定功能表示支持。
- 📝 **评论补充背景**：除了点赞，开发者可在 GitHub 对应 issue 中留言说明具体使用场景，帮助浏览器工程师理解实际痛点。
- ⏳ **常年开放持续累积**：投票渠道全年无休，且票数会持续累积，不会像年度调查那样定期重置。
- ⚖️ **影响开发优先级**：虽然票数不是唯一标准，但开发者需求是浏览器厂商制定路线图的重要参考因素。
- 🔗 **参与方式便捷**：无需撰写正式提案，只需通过现有 issue 进行点赞或评论即可参与。
- 🤝 **共建网络生态**：鼓励开发者在遵守行为准则的前提下积极反馈，共同构建更符合需求的网络平台。

---

### [介绍 GPT-5.2 | OpenAI](https://openai.com/index/introducing-gpt-5-2/)

**原文标题**: [Introducing GPT-5.2 | OpenAI](https://openai.com/index/introducing-gpt-5-2/)

OpenAI 发布了 GPT-5.2 系列模型，这是目前最先进的前沿模型，专为专业工作和长期运行的智能体设计。该系列在多项基准测试中刷新了记录，尤其在知识工作、编程、长上下文理解、视觉识别和工具调用等方面表现卓越，旨在为用户提供更高的经济价值和效率提升。

- 🚀 **性能突破**：GPT-5.2 在 GDPval 知识工作任务中击败或追平了 70.9% 的行业专家，处理速度提升 11 倍以上，成本不足 1%。
- 💻 **编程增强**：在 SWE-Bench Pro 测试中达到 55.6% 的新高度，能更可靠地调试代码、实现功能请求和重构大型代码库。
- 📊 **事实准确性提升**：在 ChatGPT 查询中，错误响应减少了 30%，提高了研究和分析工作的可靠性。
- 📜 **长上下文理解**：在 OpenAI MRCRv2 测试中表现领先，能准确处理长达 256K 令牌的文档，适合深度分析和多源工作流。
- 👁️ **视觉能力进步**：在图表推理和软件界面理解任务中错误率减半，能更精准解读仪表盘、图表和技术图。
- 🔧 **工具调用优化**：在 Tau2-bench Telecom 测试中达到 98.7% 的准确率，能有效处理多步骤客户支持等复杂工作流。
- 🔬 **科学与数学能力**：在 GPQA Diamond 和 FrontierMath 测试中分别达到 92.4% 和 40.3%，加速科研和数学研究。
- 🧠 **抽象推理提升**：在 ARC-AGI-2 测试中达到 52.9%，展现出更强的多步骤推理和问题解决能力。
- 🛡️ **安全与心理健康**：通过安全完成技术改进，在心理健康、情感依赖和自我伤害提示中的不良响应显著减少。
- 💰 **定价与可用性**：API 中 GPT-5.2 定价为每百万输入令牌 1.75 美元，输出令牌 14 美元；已在 ChatGPT 付费计划中逐步推出。

---

