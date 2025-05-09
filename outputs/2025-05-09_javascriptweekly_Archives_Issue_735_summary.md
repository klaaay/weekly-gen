### [JavaScript 周刊第 735 期：2025 年 5 月 9 日](https://javascriptweekly.com/issues/735)

**原文标题**: [JavaScript Weekly Issue 735: May 9, 2025](https://javascriptweekly.com/issues/735)

- 📧 订阅服务随时可取消，邮箱安全有保障（附隐私政策链接）。  
- 🚀 **k6 1.0 发布**：基于 Go 的 JavaScript 负载测试工具，支持 TypeScript，提升扩展性。  
- 📝 **SurveyJS**：JSON 驱动的白标表单构建工具，兼容 React/Angular/Vue 3。  
- 🔄 **Node 24 发布**：含 npm 11、V8 13.6 新特性（如`RegExp.escape`），默认启用`URLPattern` API。  
- 💻 **VS Code 1.100 更新**：增强 JavaScript 开发支持，包括缺失导入建议、Node 网络调试优化及 GPT 4.1 默认模型。  
- 📊 **Node.js 未来调查**：邀请用户参与 Next 10 调查以指导发展方向。  
- 🛠️ **工具更新**：  
  - 🤖 ESLint v9.26 支持 MCP（AI 模型直接使用）；  
  - 🗾 Mapbox GL JS 3.12 发布；  
  - 📦 Relay v19、Material UI 7.1（兼容 Tailwind CSS 4）等。  
- 📖 **文章推荐**：  
  - `...`语法妙用；  
  - Astro 与 React Server Components 对比；  
  - Prettier/ESLint迁移至Biome指南。  
- 🛠 **新工具**：  
  - HelloCSV：前端 CSV 导入工作流；  
  - PptxGenJS 4.0：JavaScript 生成 PPT；  
  - Mantine 8.0：新增图表和 20+ 组件。  
- 🌐 **生态动态**：  
  - CSS Overflow 5 实现纯 CSS 轮播；  
  - 团队从 Next.js 迁移至 Ruby on Rails 案例；  
  - Postgres 18 Beta 1 发布，优化 Linux IO 性能。  
- 🤖 **Gemini 2.5 Pro 升级**：谷歌称其前端开发能力显著提升。  

（注：分类广告及赞助内容未列入核心摘要）

---

### [GitHub - grafana/k6: 一款采用 Go 和 JavaScript 的现代负载测试工具 - https://k6.io](https://github.com/grafana/k6)

**原文标题**: [GitHub - grafana/k6: A modern load testing tool, using Go and JavaScript - https://k6.io](https://github.com/grafana/k6)

k6 是一个基于 Go 和 JavaScript 的现代负载测试工具，专为开发者和测试人员设计，强调开发者体验和性能测试的现代化方法。

- 🚀 **现代负载测试工具**：k6 是一个专为 DevOps 时代设计的性能测试工具，结合了 Go 的高性能和 JavaScript 的易用性。
- 📜 **测试即代码**：支持脚本化测试，可复用、模块化，并可与 CI 集成。
- 🌐 **多协议支持**：包括 HTTP、WebSockets、gRPC 和浏览器等。
- 🔧 **可扩展性**：拥有丰富的扩展生态系统，支持自定义需求。
- 📊 **灵活的指标存储和可视化**：支持多种数据输出和可视化选项，包括与 Grafana Cloud 的原生集成。
- 📉 **配置灵活的负载生成**：即使是低配机器也能模拟大量流量。
- 📚 **全面的文档**：涵盖从入门到高级使用的各个方面，包括 HTTP 请求、阈值设置、场景配置等。
- 🛠 **示例脚本**：提供示例脚本展示如何配置测试和模拟用户行为。
- 🗺 **公开路线图**：团队持续改进工具，公开未来开发计划，欢迎社区反馈。
- 🤝 **社区支持**：提供论坛、GitHub 讨论等多种支持渠道。
- ⚖ **AGPL-3.0 许可证**：k6 采用 AGPL-3.0 许可证分发。

---

### [GitHub - grafana/sobek](https://github.com/grafana/sobek)

**原文标题**: [GitHub - grafana/sobek](https://github.com/grafana/sobek)

Sobek 是一个用 Go 语言实现的 ECMAScript 5.1+ 解释器，强调标准兼容性和性能。该项目是 goja 的一个分支，并受到 otto 的启发。

- 🚀 **功能特性**：完整支持 ECMAScript 5.1（包括正则表达式和严格模式），并通过了大部分 tc39 测试。支持运行 Babel、TypeScript 编译器等 ES5 代码。
- 📦 **模块支持**：实验性支持 ECMAScript Modules (ESM)，但目前 API 可能会在未来有破坏性变更。
- ⚠️ **已知问题**：WeakMap 实现因 Go 运行时限制，可能导致内存使用高于预期；JSON.parse() 无法正确处理损坏的 UTF-16 代理对；Date 转换存在整数溢出问题。
- ❓ **FAQ**：解释了性能、并发安全性、缺失功能（如 setTimeout）的原因，以及如何贡献代码。
- 📝 **基础示例**：展示了如何运行 JavaScript 代码、传递和导出值、调用 JS 函数以及处理异常。
- 🔧 **高级用法**：包括结构体字段和方法名称映射、原生构造函数实现、正则表达式支持和中断执行机制。
- 📜 **许可证**：采用 MIT 许可证，无额外发布包，但有 229 个项目使用。

---

### [发布 v1.0.0 · grafana/k6 · GitHub](https://github.com/grafana/k6/releases/tag/v1.0.0)

**原文标题**: [Release v1.0.0 · grafana/k6 · GitHub](https://github.com/grafana/k6/releases/tag/v1.0.0)

Grafana k6 v1.0 正式发布，标志着该项目经过 9 年迭代和社区贡献后进入稳定阶段，提供更可靠的支持和透明度。

- 🎉 **v1.0 里程碑**：Grafana k6 v1.0 发布，承诺稳定性、正式支持保障和项目发展的透明度。  
- 🌍 **社区贡献**：27000+ GitHub 星标，9000+ 提交，200+ 贡献者，全球团队使用。  
- 🔒 **稳定性保障**：遵循语义化版本 2.0，提供 2 年支持保证，明确 API 表面。  
- 📜 **TypeScript 支持**：直接运行.ts 文件，无需转译，支持类型安全测试。  
- 🛠️ **扩展简化**：扩展现支持 k6 cloud run，无需手动构建或 xk6 工具链。  
- 📊 **测试摘要改进**：分层输出，更清晰的阈值和检查布局，多种摘要模式。  
- 🚀 **生活质量提升**：稳定模块（k6/browser 等），改进的 Grafana Cloud 集成。

---

### [Node.js — Node v24.0.0（当前版本）](https://nodejs.org/en/blog/release/v24.0.0)

**原文标题**: [Node.js — Node v24.0.0 (Current)](https://nodejs.org/en/blog/release/v24.0.0)

Node.js v24.0.0 是一个重要的版本更新，带来了多项新特性和改进，包括 V8 引擎升级、npm 更新、权限模型改进等。该版本将在 10 月进入长期支持（LTS）阶段。

- 🚀 V8 引擎升级至 13.6 版本，新增多种 JavaScript 特性，如`Float16Array`和`Error.isError`。
- 📦 npm 更新至 11.0.0，提升了性能和安全性。
- 🔄 `AsyncLocalStorage`默认使用`AsyncContextFrame`，提高了异步上下文跟踪的效率。
- 🌐 `URLPattern`现在作为全局对象提供，无需显式导入即可使用。
- 🔒 权限模型改进，标志从`--experimental-permission`简化为`--permission`，表明其稳定性增强。
- 🧪 测试运行器增强，自动等待子测试完成，简化了测试编写。
- ⚠️ 多项 API 被弃用或移除，如`url.parse()`和`tls.createSecurePair`。
- 🛠️ Windows 平台编译要求变更，不再支持 MSVC，需使用 ClangCL。
- 📅 Node.js 24 将在 10 月进入长期支持（LTS）阶段，目前为“Current”版本。

---

### [错误](https://javascriptweekly.com/link/169095/web)

**原文标题**: [Error](https://javascriptweekly.com/link/169095/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/169095/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [URLPattern - Web API 接口 | MDN](https://developer.mozilla.org/en-US/docs/Web/API/URLPattern)

**原文标题**: [URLPattern - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/URLPattern)

URLPattern 是 URL Pattern API 提供的接口，用于匹配 URL 或其部分内容，支持通过捕获组提取匹配部分。该功能目前为实验性技术，兼容性有限，需谨慎在生产环境中使用。

- 🌐 **实验性技术**：URLPattern 目前为实验性功能，浏览器兼容性有限，使用前需仔细检查兼容性表。  
- 🔍 **匹配功能**：可匹配 URL 的各个部分（如协议、主机名、路径等），并支持通过捕获组提取内容。  
- 🛠️ **构造函数**：`URLPattern()` 用于创建新的 URLPattern 对象，基于给定的模式和基础 URL。  
- 📌 **实例属性**：包括 `hash`、`hostname`、`password` 等，分别用于匹配 URL 的对应部分。  
- ⚙️ **实例方法**：  
  - `exec()`：返回匹配的 URL 部分对象，不匹配时返回 `null`。  
  - `test()`：返回布尔值，表示 URL 是否匹配给定模式。  
- 📚 **相关资源**：  
  - 语法详情参考 [URL Pattern API](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API)。  
  - GitHub 提供 [polyfill](https://github.com/kenchris/urlpattern-polyfill) 支持。  
- ❗ **注意事项**：该功能可在 Web Workers 中使用，但未纳入 Baseline 标准（因主流浏览器支持不全）。  
- 🔄 **反馈与更新**：MDN 文档最后更新于 2024 年 3 月，鼓励用户反馈以改进内容。

---

### [Node.js — Node v24.0.1（当前版本）](https://nodejs.org/en/blog/release/v24.0.1)

**原文标题**: [Node.js — Node v24.0.1 (Current)](https://nodejs.org/en/blog/release/v24.0.1)

Node.js v24.0.1（当前版本）发布，包含多项修复和更新。

- 🔄 回退 "buffer: move SlowBuffer to EOL" 的更改 (Filip Skokan) #58211  
- 📊 修复 benchmark 中方法名的拼写错误 (Miguel Marcondes Filho) #58128  
- 🛠️ 默认在 GN 中使用 //third_party/simdutf (Shelley Vohr) #58115  
- 📝 新增 HBSPS 为 triager (Wiyeong Seo) #57980  
- 📄 为 --input-type 部分添加历史记录 (Antoine du Hamel) #58175  
- ✉️ 添加 ambassador 消息 (Brian Muenzenmeyer) #57600  
- 📖 修复 vm.compileFunction() 中的选项对齐问题 (Jimmy Leung) #58145  
- 🐛 修复 benchmark 脚本路径的拼写错误 (Miguel Marcondes Filho) #58129  
- 📚 为 readlinePromises.createInterface() 添加缺失的 options.signal (Jimmy Leung) #55456  
- 📄 修复 zlib.md 中的拼写错误 (yusheng chen) #58093  
- ℹ️ 澄清 v25+ 中 Corepack 的移除计划 (Trivikram Kamat) #57825  
- 🔄 更新 actions/setup-node 到 4.4.0 (dependabot[bot]) #58111  
- 🔄 更新 actions/setup-python 到 5.6.0 (dependabot[bot]) #58107  
- 🛠️ 从 CodeQL 扫描中排除 deps/v8/tools (Rich Trott) #58132  
- 🔧 更新 eslint 工具组 (dependabot[bot]) #58105  
- 💾 提供多平台安装包和二进制文件下载链接（Windows、macOS、Linux、AIX 等）  
- 🔒 包含 SHASUMS 和 PGP 签名以确保下载文件的完整性

---

### [2025 年 4 月（版本 1.100）](https://code.visualstudio.com/updates/v1_100)

**原文标题**: [April 2025 (version 1.100)](https://code.visualstudio.com/updates/v1_100)

Visual Studio Code 2025 年 4 月版本（1.100）更新概览，发布于 2025 年 5 月 8 日，支持 Windows、Mac 和 Linux 多平台下载。

- 🚀 **Chat 功能增强**：支持自定义指令和可重用提示，提供更智能的 GitHub、扩展和笔记本工具结果。
- ⚡ **性能优化**：重复聊天请求响应更快，代理模式下的编辑速度提升。
- 🖥️ **编辑器体验改进**：多窗口支持优化，更易识别暂存更改。
- 📝 **指令与提示文件**：通过 Markdown 文件定制 AI 体验，支持自动同步和手动附加指令。
- 🔍 **GitHub 仓库代码搜索**：新增`#githubRepo`工具，可直接搜索仓库代码片段。
- 🌐 **网页抓取工具升级**：支持整页内容作为上下文，并转换为 Markdown 格式。
- 🛠️ **代理模式编辑**：支持 OpenAI 和 Anthropic 的编辑格式，大幅提升大文件编辑速度。
- 📊 **Notebooks 功能**：支持拖放单元格输出到聊天，新增代理模式工具如运行单元格、获取内核状态。
- 🔧 **调试与语言支持**：Node.js 调试器网络视图默认启用，CSS 和 HTML 显示浏览器支持情况。
- 🔌 **扩展开发**：支持 ESM 模块扩展，新增文本编码 API，工具调用支持图像结果。
- 🛡️ **安全增强**：所有平台强制扩展签名验证，防止恶意扩展安装。
- ♿ **无障碍改进**：合并编辑器更易访问，新增编辑建议提示音。
- 🌈 **主题与 UI**：新增预览主题 Codesong，浮动窗口支持紧凑和置顶模式。

感谢所有贡献者的努力，VS Code 持续优化开发体验。

---

### [2025 年 4 月（版本 1.100）](https://code.visualstudio.com/updates/v1_100#_javascript-debugger-network-view)

**原文标题**: [April 2025 (version 1.100)](https://code.visualstudio.com/updates/v1_100#_javascript-debugger-network-view)

2025 年 4 月发布的 Visual Studio Code 1.100 版本带来了多项功能更新和优化，主要包括：

- 🚀 **Chat 功能增强**：支持自定义指令和可重用提示文件，提升与 GitHub、扩展和笔记本的交互效率。
- ⚡ **性能优化**：聊天响应速度加快，特别是在重复请求和代理模式下的编辑操作。
- 🖥️ **编辑器体验改进**：多窗口支持优化，更易识别暂存更改。
- 📂 **文件类型支持**：新增`.instructions.md`和`.prompt.md`文件类型，用于定制 AI 体验和创建可重用聊天请求。
- 🛠️ **代理模式编辑**：支持 OpenAI 和 Anthropic 的编辑格式，大幅提升大文件编辑速度。
- 🔍 **GitHub 仓库代码搜索**：通过`#githubRepo`工具直接搜索 GitHub 仓库中的代码片段。
- 📊 **扩展工具集成**：使用`#extensions`工具在聊天中查找和安装 Marketplace 扩展。
- 🌐 **网页抓取工具改进**：支持完整页面抓取并转换为 Markdown 格式，提升内容相关性检测。
- ⌨️ **聊天输入优化**：改进附件显示和上下文选择器，移除“完成”按钮以减少混淆。
- 🔧 **辅助功能提升**：合并编辑器更易访问，新增设置通知预测建议和差异行导航音频提示。
- 🖱️ **UI 元素拖放支持**：实验性功能允许将 Simple Browser 中的 UI 元素拖放至聊天作为上下文。
- 📝 **任务创建与运行**：代理模式下支持创建和运行任务，简化项目启动流程。
- 🔐 **安全性增强**：所有平台强制扩展签名验证，防止恶意扩展安装。
- 📚 **语言支持**：CSS 和 HTML 的浏览器支持提示，`.env`文件默认语法高亮，JavaScript 和 TypeScript 支持可展开悬停信息。
- 🐍 **Python 环境优化**：支持分支覆盖率测试，新增快速创建环境命令，集成聊天工具获取环境信息和安装包。
- 🔄 **远程开发**：Dev Container 功能现在包含指令文件，提升聊天建议的相关性。
- 📦 **扩展开发支持**：新增 ESM 模块支持，允许扩展使用`import`和`export`语句。

此外，还包括多项错误修复和社区贡献的改进，进一步提升了 VS Code 的稳定性和用户体验。

---

### [Node.js 未来十年调查 - 2025](https://linuxfoundation.research.net/r/2025nodenext10)

**原文标题**: [Node.js Next 10 Survey - 2025](https://linuxfoundation.research.net/r/2025nodenext10)

以下是您提供的文本的总结：

overview summary  
该内容是 Node.js Next 10 Survey - 2025 的调查问卷，包含多个问题，涉及居住地、主要语言、Node.js 使用年限、工作组织类型、公司所属行业以及组织规模等。

- 🌍 居住地：问卷列出了全球多个国家和地区供选择。  
- 🗣️ 主要语言：包括英语、西班牙语、法语、德语、阿拉伯语、中文等多种语言选项。  
- ⏳ Node.js 使用年限：选项包括 0-5 年、10 年以上等。  
- 🏢 工作组织类型：涵盖学术界、公司、政府、个体/自由职业者、非营利组织等。  
- 🏭 公司所属行业：包括农业技术、通信服务、能源、金融、医疗保健等多个领域。  
- 👥 组织规模：通过滑块选择员工数量，范围从 0 到 1000+。  
- 📄 问卷进度：当前为第 1 页，共 4 页，完成度为 25%。

---

### [GitHub - EvanZhouDev/polycompiler：将Python和JS代码合并为可在两种语言中运行的单一文件](https://github.com/EvanZhouDev/polycompiler)

**原文标题**: [GitHub - EvanZhouDev/polycompiler: Merge Python and JS code into one file that can be run in both languages.](https://github.com/EvanZhouDev/polycompiler)

Polycompiler 是一个实验性项目，旨在将 Python 和 JavaScript 代码合并到一个源文件中，使其可以在两种语言环境中运行。

- 🚀 **项目功能**：将 Python 和 JS 代码合并为一个文件，支持在 Node.js 和 Python 3 中分别运行对应的代码段。
- 📦 **安装方法**：通过 npm 安装 `polycompiler`：`npm i polycompiler`。
- 🛠 **使用步骤**：运行 `polycompiler` 命令，提供 JS 文件、Python 文件路径及可选的输出文件路径。
- 📝 **文件命名**：输出文件扩展名为 `.py.js`，以确保 Node.js 能够解析。
- 🐍 **Python 运行**：执行 Python 代码时，忽略 JS 部分。
- 🌐 **JS 运行**：执行 JS 代码时，忽略 Python 部分。
- ❓ **项目动机**：主要为趣味性，但也可能适用于需要同时面向 Python 和 JS 用户的场景。
- 🎥 **工作原理**：通过巧妙利用 Python 的 `exec` 和 JS 的 `eval` 及标签语句，实现在不同环境中运行对应代码。
- 📌 **示例代码**：展示如何在同一文件中分别输出 "Hello Python" 和 "Hello JS"。
- 🔍 **技术细节**：详细解释了代码在 Python 和 JS 中的执行逻辑。
- ⚠ **注意事项**：项目仍在进行中（WIP），当前文件命名规则为 `.py.js`。

---

### [认识我们的 2025 年 OpenJS 基金会董事会 | OpenJS 基金会](https://openjsf.org/blog/openjs-board-directors-2025)

**原文标题**: [Meet Our 2025 OpenJS Foundation Board of Directors | OpenJS Foundation](https://openjsf.org/blog/openjs-board-directors-2025)

OpenJS 基金会宣布了 2025 年董事会成员名单，包括新加入和连任的董事，他们将在不同层级（Gold、Silver 和社区）担任职务，共同推动基金会的技术政策和发展方向。

- 🎉 欢迎新董事 Stephen Husak（Capital One）加入董事会，作为 Silver 董事，他在企业级 Node.js 和开源技术应用方面有丰富经验。  
- 🔄 六名董事连任，包括 Jordan Harband（Gold）、Abby Cabunoc Mayes（Silver）等，继续为基金会贡献力量。  
- 🏛️ 董事会成员由 Platinum 会员任命、Gold/Silver 会员选举及社区代表（CPC）推选产生，确保多方参与治理。  
- 🌟 Platinum 董事包括 IBM、Microsoft 等企业的代表，主导基金会的战略方向。  
- 💡 Stephen Husak 作为新董事，曾主导 Capital One 的云平台迁移，并在开源社区积极分享经验。  
- 🤝 基金会感谢所有董事的服务，期待他们在新一年推动 JavaScript 生态发展。

---

### [ESLint v9.26.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/05/eslint-v9.26.0-released/)

**原文标题**: [ESLint v9.26.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/05/eslint-v9.26.0-released/)

ESLint v9.26.0 是一个小版本升级，引入了新功能并修复了之前版本中的多个错误。

- 🚀 **MCP 服务器集成**：新增支持 Model Context Protocol (MCP) 服务器，使 ESLint 能够通过统一接口与 AI 模型和工具交互，适用于 AI 辅助开发工具如 GitHub Copilot。  
- 🔍 **`no-shadow-restricted-names` 支持 `globalThis`**：新增检测 `globalThis` 遮蔽的功能，需通过 `reportGlobalThis: true` 启用。  
- ⚙️ **`no-unused-expressions` 新增 `ignoreDirectives` 选项**：允许在 ES3 代码库中忽略指令（如 `"use strict"`），避免误报未使用代码。  
- 🛠 **新特性**：包括为 `eqeqeq` 规则添加建议、MCP 服务器支持等。  
- 🐞 **错误修复**：修复缓存文件删除检查、`RuleTester` 循环引用崩溃等问题。  
- 📚 **文档更新**：修复 Markdown 格式、命令空格等细节。  
- 🔧 **维护工作**：依赖升级、内部类型优化等。  

贡献者包括 Francesco Trotta 等团队成员。

---

### [引言 - 模型上下文协议](https://modelcontextprotocol.io/introduction)

**原文标题**: [Introduction - Model Context Protocol](https://modelcontextprotocol.io/introduction)

Model Context Protocol (MCP) 是一个开放协议，用于标准化应用程序如何为大型语言模型 (LLM) 提供上下文。类似于 USB-C 接口的统一连接功能，MCP 为 AI 模型提供了连接不同数据源和工具的标准方式。

- 🔌 **MCP 的作用**：帮助构建基于 LLM 的代理和复杂工作流，提供预构建集成、灵活的 LLM 供应商切换和数据安全最佳实践。
- 🏗️ **核心架构**：采用客户端 - 服务器架构，包括 MCP 主机、客户端、服务器以及本地和远程数据源。
- 🚀 **快速入门**：提供针对服务器开发者、客户端开发者和 Claude 桌面用户的不同入门路径。
- 📚 **示例与教程**：包含官方服务器和客户端示例，以及利用 LLM 加速开发的教程和调试指南。
- 🧠 **深入探索**：涵盖核心架构、资源管理、提示模板、工具集成、采样机制和传输方式等高级概念。
- 🤝 **贡献与支持**：鼓励通过 GitHub 参与贡献，并提供多种反馈渠道包括问题报告和讨论区。

---

### [发布 v3.12.0 · mapbox/mapbox-gl-js · GitHub](https://github.com/mapbox/mapbox-gl-js/releases/tag/v3.12.0)

**原文标题**: [Release v3.12.0 · mapbox/mapbox-gl-js · GitHub](https://github.com/mapbox/mapbox-gl-js/releases/tag/v3.12.0)

Mapbox GL JS 最新版本 v3.12.0 发布，包含多项功能改进与错误修复。

- 🚀 新增实验性功能：支持渲染 3D 道路交叉口和阴影效果的高架线  
- 🎨 添加图案过渡属性（如 line-pattern-cross-fade），实现图案图像平滑切换  
- 🌐 引入 TileJSON 的 extra_bounds 支持，优化稀疏数据区域的瓦片请求控制  
- ⚡ 性能提升：延迟加载 3D 模型，略微减小 JS 包体积  
- 📦 多项 TypeScript 类型改进  
- 🐛 修复符号图层调用 setData 时的闪烁问题  
- 🔍 修正低缩放级别下 Globe 模式的 queryRenderedFeatures 查询问题  
- 🖥️ 修复 styleimagemissing 事件未触发等边缘场景问题  
- 🔄 放宽 line-gradient 验证条件，支持预计算属性的矢量瓦片源

---

### [发布 v19.0.0 · facebook/relay · GitHub](https://github.com/facebook/relay/releases/tag/v19.0.0)

**原文标题**: [Release v19.0.0 · facebook/relay · GitHub](https://github.com/facebook/relay/releases/tag/v19.0.0)

Relay 19.0.0 发布，包含文档改进、错误修复和功能增强。

- 🚀 **版本更新**：Relay 19.0.0 发布，支持 React 19 作为有效对等依赖。
- 📝 **文档改进**：新增多个文档页面，包括快速入门、生产设置、Relay Babel 插件等，并优化现有文档。
- ⚠️ **重大变更**：默认生成 ES 模块导入，可通过配置恢复旧行为；不再包含预捆绑模块。
- 🛠️ **功能改进**：包括代码导航优化、环境构造参数可选、订阅功能增强等。
- 🐛 **错误修复**：修复了多个问题，如片段引用、网络错误处理、缓存问题等。
- 📚 **文档优化**：更新教程和指南，修复代码示例和错误链接，移除过时内容。
- 🔬 **实验性变更**：支持客户端 3D、执行时解析器等新功能。
- 👥 **贡献者**：多位开发者参与，修复问题并添加新功能。

---

### [发布 v7.1.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v7.1.0)

**原文标题**: [Release v7.1.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v7.1.0)

Material UI 发布了 v7.1.0 版本，包含多项功能更新、问题修复和文档改进，由 21 位贡献者共同完成。

- 🎉 Material UI 现在支持 Tailwind CSS v4，并提供了设置指南。  
- 🛠️ 修复了多个组件的问题，如 InputBase、OutlinedInput、Snackbar 等。  
- 📚 文档方面新增了多个指南，包括 Tailwind CSS v4 集成指南和 Next.js App Router 指南。  
- 🔧 核心代码基础设施进行了多项改进，包括类型定义修正和依赖版本对齐。  
- 👏 感谢所有贡献者，包括@alexfauquette、@andreachiera 等 21 位开发者。

---

### [发布 v1.3.9 · web-infra-dev/rspack · GitHub](https://github.com/web-infra-dev/rspack/releases/tag/v1.3.9)

**原文标题**: [Release v1.3.9 · web-infra-dev/rspack · GitHub](https://github.com/web-infra-dev/rspack/releases/tag/v1.3.9)

Rspack 发布了 v1.3.9 版本，包含性能优化、错误修复、文档更新和其他改进。

- ⚡ **性能优化**：通过优化 JS 统计提升了性能。  
- 🐞 **错误修复**：修复了多个问题，包括循环依赖关系、插件错误堆栈信息缺失等。  
- 📖 **文档更新**：改进了 JavaScript 压缩与转换示例、SWC API 示例、数据 URI 模块规则等文档。  
- 🔧 **其他改进**：包括依赖项更新、CI 优化、SWC 升级等。  
- 👏 **贡献者**：感谢 stormslowly、renovate 等 8 位贡献者的努力。  
- 🚀 **社区反应**：获得了 4 个点赞、2 个火箭和 1 个关注表情的积极反馈。

---

### [发布 8.7.0 版 · BabylonJS/Babylon.js · GitHub](https://github.com/BabylonJS/Babylon.js/releases/tag/8.7.0)

**原文标题**: [Release 8.7.0 · BabylonJS/Babylon.js · GitHub](https://github.com/BabylonJS/Babylon.js/releases/tag/8.7.0)

Babylon.js 是一个开源的 3D 游戏引擎和图形库，最新版本 8.7.0 于 5 月 8 日发布。

- 🚀 **版本更新**：最新版本为 8.7.0，发布于 5 月 8 日。  
- 🔧 **问题修复**：修复了 NME 中的区域灯光问题（#16577）。  
- ⚙️ **功能优化**：对流程图中的 waitAll 功能进行了小幅修复（#16576）。  
- 📦 **开源项目**：拥有 24.1k 星标和 3.5k 的分支，显示其受欢迎程度。  
- 🔄 **持续更新**：版本更新包含 4 次提交，显示活跃的开发状态。

---

### [Electron 36.0.0 | Electron](https://www.electronjs.org/blog/electron-36-0)

**原文标题**: [Electron 36.0.0 | Electron](https://www.electronjs.org/blog/electron-36-0)

Electron 36.0.0 版本发布，包含 Chromium 136、V8 13.6 和 Node 22.14.0 的升级，新增多项功能改进和修复。

- 🚀 **发布信息**：Electron 36.0.0 已发布，支持通过 `npm install electron@latest` 安装或从官网下载。  
- 🛠️ **主要更新**：  
  - ✍️ **写作工具支持**：macOS 系统级功能（如拼写检查、自动填充）可通过 `menu.popup()` 的 `frame` 参数启用。  
  - 📦 **依赖升级**：Chromium 升级至 136.0.7103.48，V8 至 13.6，Node 至 22.14.0。  
- 🌟 **新功能**：  
  - 🪟 新增 `BrowserWindow.isSnapped()` 检测窗口是否被 Windows Snap 排列。  
  - 🔍 新增 `WebContents.focusedFrame` 获取聚焦的框架。  
  - 🎨 新增 `nativeTheme.shouldUseDarkColorsForSystemIntegratedUI` 区分系统和应用主题。  
  - 🖥️ 支持 Linux 的 `system-context-menu`。  
- ⚠️ **破坏性变更**：  
  - ❌ 弃用 `NativeImage.getBitmap()`，改用 `toBitmap()`。  
  - 🔄 扩展方法从 `session` 移至 `session.extensions`。  
  - 🗑️ 移除 `session.clearStorageData` 的 `syncable` 配额类型。  
  - 🐧 GNOME 默认使用 GTK 4，可通过命令行回退到 GTK 3/2。  
- 📅 **支持终止**：Electron 33.x.y 已停止支持，建议升级至新版本。  
- 🔮 **未来计划**：团队将继续跟进 Chromium、Node 和 V8 的更新，详细路线图可参考官方文档。  
- 📢 **反馈渠道**：用户可通过 Bluesky、Mastodon、Discord 或 GitHub 提交反馈和问题。

---

### [JavaScript 中展开与剩余语法的力量 - Matt Smith](https://allthingssmitty.com/2025/05/05/the-power-of-spread-and-rest-patterns-in-javascript.md/)

**原文标题**: [
    The power of the spread and rest syntax in JavaScript - Matt Smith
  ](https://allthingssmitty.com/2025/05/05/the-power-of-spread-and-rest-patterns-in-javascript.md/)

JavaScript 中的展开（spread）和剩余（rest）语法是强大且常用的特性，它们通过简洁的`...`语法实现不同的功能，使代码更清晰、表达力更强。

- 🔄 **展开语法（Spread）**：用于解构数组、对象等可迭代结构，常见于数组复制、合并、函数参数传递等场景。
- 📦 **剩余参数（Rest）**：用于收集多个元素，常见于函数参数、数组或对象解构中，替代传统的`arguments`对象。
- 🛠 **实际应用**：在 React 中用于不可变状态更新、表单处理、工具函数等，提升代码的可维护性和简洁性。
- ⚠️ **注意事项**：展开语法仅进行浅拷贝，对象展开时顺序会影响属性覆盖，需谨慎处理嵌套结构。
- 🌟 **总结**：掌握展开和剩余语法是现代 JavaScript 开发的必备技能，能显著提升代码质量和开发效率。

---

### [RSC 面向天文开发者的应用 — 过度解读](https://overreacted.io/rsc-for-astro-developers/)

**原文标题**: [RSC for Astro Developers — overreacted](https://overreacted.io/rsc-for-astro-developers/)

Astro 和 React Server Components（RSC）在架构设计上有相似之处，但也存在显著差异。两者都区分了服务端和客户端组件，但实现方式和灵活性不同。

- 🚀 **Astro 组件**：使用`.astro`扩展名，仅在服务端或构建时执行，无法在客户端运行。适合处理文件系统、数据库等服务器端任务，但不支持交互性。
- 🏝️ **客户端岛屿**：使用 React、Vue 等框架编写的组件，负责处理交互性。可以嵌套同框架组件，但不能渲染 Astro 组件。
- 🔄 **数据流**：数据只能从 Astro 组件流向客户端岛屿，形成单向数据流。
- 🔧 **RSC 组件**：React Server Components 也分为服务端组件和客户端组件，通过`'use client'`指令标记客户端组件。
- 🚪 **世界分隔**：Astro 通过文件扩展名分隔服务端和客户端，RSC 通过`'use client'`指令实现。
- 🔄 **灵活性**：RSC 中，组件可以根据导入的上下文决定运行在服务端还是客户端，更具灵活性。
- 🌳 **单一树结构**：RSC 的 UI 是一个单一的 React 树，支持服务端和客户端组件的深度嵌套和交互。
- 📜 **输出格式**：Astro 输出 HTML，RSC 输出 React 树（可转为 HTML 或 JSON）。
- 🛠️ **开发体验**：Astro 更易上手，RSC 更灵活但学习曲线较陡。
- 🔄 **刷新机制**：RSC 支持服务端组件的就地刷新，Astro 则需要整页刷新或移至客户端岛屿。
- 🌐 **框架支持**：RSC 是底层标准，Next.js 和 Parcel 等框架提供实现。

总的来说，Astro 适合简单、静态的场景，RSC 适合需要深度交互和灵活性的项目。两者各有优劣，选择取决于项目需求。

---

### [天文](https://astro.build/)

**原文标题**: [Astro](https://astro.build/)

Astro 5.7 现已发布，这是一个专为内容驱动型网站设计的 JavaScript 框架，以其卓越的性能和灵活性受到全球大型企业的青睐。

- 🚀 **高性能框架**：Astro 通过服务器优先渲染和轻量级 HTML 输出，优化网站性能，减少不必要的 JavaScript 负担。
- 🌍 **内容驱动**：支持从文件系统、外部 API 或 CMS 加载内容，适应多样化的内容来源。
- 🛠️ **高度可定制**：允许使用喜爱的工具和库，包括 JavaScript UI 组件、CSS 库和主题等。
- 📊 **卓越性能表现**：Astro Islands 技术显著提升页面加载速度，改善转化率、Core Web Vitals 和 SEO，实际数据表现优于 Gatsby、WordPress 等框架。
- 🔄 **无锁定设计**：支持所有主流 UI 框架（如 React、Vue、Svelte 等），现有组件可无缝集成。
- 🧩 **丰富功能**：包括内容集合、零 JavaScript 默认设置、视图过渡 API、中间件支持、类型安全的后端操作等。
- 🏗️ **生态系统支持**：提供多种主题模板（电商、博客、文档等）和专业机构合作，便于快速开发和获取专业支持。
- 💻 **开发者友好**：内置开发工具栏、环境变量管理和部署适配器，简化开发和部署流程。
- 📦 **免费开源**：由 Netlify、Sentry 等赞助支持，社区驱动持续发展。

---

### [Copilot 代理工具与 MCP 支持](https://wallabyjs.com/blog/wallaby-mcp.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Copilot Agent tools and MCP support](https://wallabyjs.com/blog/wallaby-mcp.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

AI 代理工具和 MCP 支持正在改变开发者与代码的交互方式，通过提供高质量的上下文信息，显著提升 AI 代理在代码创建、修复和维护方面的能力。

- 🚀 **上下文关键性**：高质量的上下文（如运行时值、代码执行路径等）能大幅提升 AI 代理对代码的理解和调试能力。  
- 🛠️ **工具支持**：Wallaby 和 Console Ninja 的新 AI 工具及 MCP 服务器支持 Copilot Agent、Cursor 等多种 AI 代理，提供实时运行时洞察。  
- 🔄 **新旧对比**：传统方式依赖有限的上下文（如 CLI 输出），而新方式通过 MCP 服务器提供深度代码行为和执行环境模型。  
- 📊 **深度访问**：代理可访问运行时值、执行路径、分支级代码覆盖率等，无需修改代码。  
- ⚙️ **集成方式**：通过 VS Code 的 AI 工具或独立 MCP 服务器实现，支持多种编辑器和代理。  
- 💡 **应用示例**：修复失败测试、创建新测试、分析代码覆盖率等，支持复杂任务分解和定制化工作流。  
- 🌟 **未来展望**：Wallaby 的 MCP 支持为开发者生产力开辟新维度，结合 AI 代理实现更智能、高效的代码辅助。  
- 📢 **反馈邀请**：鼓励用户探索新功能并分享反馈，以持续优化工具。  
- 🆕 **新功能**：新增交互式图表可视化复杂运行时值功能。

---

### [将 JavaScript 项目从 Prettier 和 ESLint 迁移至 BiomeJS | AppSignal 博客](https://blog.appsignal.com/2025/05/07/migrating-a-javascript-project-from-prettier-and-eslint-to-biomejs.html)

**原文标题**: [Migrating A JavaScript Project from Prettier and ESLint to BiomeJS | AppSignal Blog](https://blog.appsignal.com/2025/05/07/migrating-a-javascript-project-from-prettier-and-eslint-to-biomejs.html)

BiomeJS 是一个新兴的 JavaScript 工具链，旨在整合代码格式化和 linting 功能，以简化开发流程并提升性能。它基于 Rust 构建，支持多线程，性能远超 Prettier 和 ESLint。尽管 BiomeJS 在某些语言和框架支持上仍有不足，但其简洁的配置和高效的执行使其成为现代 JavaScript 开发的强力候选工具。

- 🚀 **BiomeJS 简介**：BiomeJS 是一个高性能的代码格式化和 linting 工具，整合了 Prettier 和 ESLint 的功能，简化了开发流程。
- ⚡ **性能优势**：基于 Rust 和多线程架构，BiomeJS 的格式化速度比 Prettier 快 25 倍，linting 速度比 ESLint 快 15 倍。
- 🔧 **功能对比**：BiomeJS 的格式化输出与 Prettier 基本兼容，但支持的语言和框架较少；linting 规则与 ESLint 类似，但更易配置。
- 📦 **安装与使用**：通过 npm 安装 BiomeJS，无需配置文件即可立即使用，支持格式化、linting 及自动修复功能。
- 🛠️ **编辑器集成**：提供 VS Code、IntelliJ 等编辑器的官方扩展，支持实时 linting 和保存时自动格式化。
- ⚙️ **配置灵活**：通过 `biome.json` 文件自定义规则，支持从 Prettier 和 ESLint 迁移配置。
- 🚫 **忽略规则**：使用 `biome-ignore` 注释或配置文件忽略特定文件或代码行的格式化和 linting。
- 🔄 **项目集成**：支持仅处理变更文件，可设置预提交钩子和持续集成工作流，确保代码质量。
- 🤔 **是否切换**：BiomeJS 适合追求性能和简化的团队，但在某些文件类型支持上可能不足，可结合现有工具使用。
- 📚 **总结**：BiomeJS 是 Prettier 和 ESLint 的有力替代品，尤其适合性能敏感项目，但需根据项目需求权衡支持范围。

---

### [错误](https://javascriptweekly.com/link/169118/web)

**原文标题**: [Error](https://javascriptweekly.com/link/169118/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/169118/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [非 HTML 内容](https://blog.vaxry.net/articles/2025-electronAintBad)

**原文标题**: [Non-HTML content](https://blog.vaxry.net/articles/2025-electronAintBad)

无法总结：非 HTML 内容。

---

### [React 编译器三分钟解析（告别重复渲染） - YouTube](https://www.youtube.com/watch?v=40osg7LoShc)

**原文标题**: [React Compiler Explained in 3 Minutes (Goodbye, re-renders) - YouTube](https://www.youtube.com/watch?v=40osg7LoShc)

YouTube 平台的主要功能和政策概览  

- 📜 **簡介** - YouTube 的基本介紹和平台概述  
- 📺 **媒體** - 媒體內容相關資訊和資源  
- ©️ **著作權** - 版權保護政策和相關規定  
- 📩 **與我們聯絡** - 聯繫 YouTube 的方式和渠道  
- 🎨 **創作者** - 創作者相關資源和支持  
- 📢 **廣告** - 廣告政策和投放資訊  
- 💻 **開發人員** - 開發者工具和 API 資源  
- 📑 **條款** - 使用條款和服務協議  
- 🔒 **隱私權** - 隱私保護政策和數據使用說明  
- ⚖️ **政策與安全性** - 平台政策和安全措施  
- ⚙️ **YouTube 運作方式** - 平台運作機制和功能解釋  
- 🧪 **測試新功能** - 新功能的測試和反饋渠道  
- � **© 2025 Google LLC** - 版權所有者和年份標註

---

### [你对 Angular（及前端）中的 DDD 理解有误](https://www.angularspace.com/youre-misunderstanding-ddd-in-angular-and-frontend/)

**原文标题**: [You're misunderstanding DDD in Angular (and Frontend)](https://www.angularspace.com/youre-misunderstanding-ddd-in-angular-and-frontend/)

概述总结  
本文探讨了前端开发（特别是 Angular 社区）中对领域驱动设计（DDD）的普遍误解，强调 DDD 的核心是业务驱动而非技术实现，并澄清了 DDD 在前端应用中的误区和正确实践。

- 🚨 **误解普遍性**：前端开发者常将 DDD 与代码结构或工具（如模块化、Monorepo）混淆，偏离了 DDD 的业务本质。  
- 🏥 **业务场景示例**：以医疗预约系统为例，说明 DDD 应围绕业务问题（如资源竞争、支付流程）而非技术分层。  
- 🔍 **DDD 的本质**：DDD 是跨产品全栈的方法论，需通过战略设计（业务划分）和战术设计（技术实现）协作，前端不能独立作为“限界上下文”。  
- 🧩 **核心概念澄清**：  
  - **限界上下文**：业务模块的语义边界（如预约、支付），需包含前后端整体，而非仅前端。  
  - **统一语言**：术语需在特定上下文中精确一致，避免跨模块混淆（如“患者”在不同场景含义不同）。  
- ⚠️ **战术 DDD 的局限性**：聚合根、仓储等模式在前端无意义，因前端不处理持久化或并发控制。  
- 📦 **Monorepo 的误区**：代码组织工具与 DDD 无直接关联，过度共享代码反而会破坏模块自治性。  
- 💡 **正确实践**：DDD 成功依赖于深度业务理解、专家协作及全栈视角，而非技术标签化。  
- 🔥 **社区反思**：滥用 DDD 术语会导致“语义扩散”，呼吁用简单语言传递核心价值，避免盲目跟风。  

作者最终强调：DDD 是复杂业务场景的工具，需谨慎评估必要性，并推荐从业务对齐而非框架角度切入学习。

---

### [Fastify 与 Vue 的故事](https://hire.jonasgalvez.com.br/2025/apr/30/fastify-vue/)

**原文标题**: [The Story of Fastify + Vue](https://hire.jonasgalvez.com.br/2025/apr/30/fastify-vue/)

Rich Hickey 的演讲"Simple Made Easy"强调了简单与容易的区别，指出开发者常因追求便利而忽视复杂性，导致长期效率低下。文章通过 Fastify/Vite 栈的实践，探讨了如何通过模块化和透明性实现真正的简单系统。

- 🎯 Rich Hickey 指出开发者过于追求便利性，而忽视了简单性，长期来看会降低开发速度。
- 🔍 真正的简单系统需要深入理解内部机制，而非依赖黑箱工具。
- 🧩 模块化的关键在于组件间的低耦合和高独立性。
- 🛠️ 现代工具常标榜"容易"和"快速"，但缺乏真正的简单性。
- 🔄 作者在 Nuxt 项目中经历了便利性的诱惑，但最终意识到透明性和控制权的重要性。
- 🚀 Fastify 提供了干净透明的 Node.js HTTP 服务器构建方式，强调从基础生长而非框架约束。
- 💎 @fastify/vue 通过最小化设计和可替换性，实现了高度模块化和可组合性。
- 🔄 用户可以轻松覆盖默认行为，保持对系统各个层面的控制。
- 📦 采用"包含电池但可更换"的设计哲学，平衡开箱即用和定制需求。
- 🌱 项目持续进化，如加入 TypeScript 支持，同时保持对原始组件和交互的专注。
- 🔗 通过真实案例展示如何将复杂转化为简单而不牺牲模块独立性。
- 💡 最终目标是让开发者拥抱并掌控复杂性，从而设计出真正简单的抽象。

---

### [你好 CSV](https://hellocsv.github.io/HelloCSV/)

**原文标题**: [HelloCSV](https://hellocsv.github.io/HelloCSV/)

好的，请提供需要总结的文本内容，我会按照您要求的模板进行整理，包括概述总结和带 emoji 的简洁要点列表。  

示例模板：  

[这里是概述总结，无标题]  

- 🌟 要点 1  
- 📌 要点 2  
- 🔍 要点 3  

请提供具体文本内容以便我为您生成总结。

---

### [简介 - HelloCSV](https://hellocsv.mintlify.app/common/get-started/introduction)

**原文标题**: [Introduction - HelloCSV](https://hellocsv.mintlify.app/common/get-started/introduction)

HelloCSV 是一个用于处理 CSV 文件的工具，提供导入、验证和转换功能，支持 React 环境，并允许高度自定义。

- 🏠 **主页** - 提供基本信息和搜索功能  
- 🔍 **搜索支持** - 快速查找所需内容  
- 🚀 **试用功能** - 可直接体验工具  
- 📚 **导航菜单** - 包含入门指南、介绍、演示和源码  
- ❓ **为什么选择** - 解释工具的优势和用途  
- 🛠️ **API 参考** - 详细说明导入属性、表格定义、列类型等  
- ⚙️ **配置选项** - 支持 Peer 和 Bundled 模式  
- ⚛️ **React 支持** - 提供 React 环境下的使用方法  
- 🎨 **自定义样式** - 可调整高度、宽度和主题  
- 🛠️ **开发指南** - 包含设置、无构建示例和部署文档  
- 📖 **文档资源** - 提供详细的开发和使用说明  
- 🌟 **欢迎使用** - 工具简介和 GitHub 支持

---

### [GitHub - gitbrent/PptxGenJS: 使用 JavaScript 创建 PowerPoint 演示文稿。支持 Node、React、网页浏览器等环境。](https://github.com/gitbrent/PptxGenJS)

**原文标题**: [GitHub - gitbrent/PptxGenJS: Build PowerPoint presentations with JavaScript. Works with Node, React, web browsers, and more.](https://github.com/gitbrent/PptxGenJS)

PptxGenJS 是一个用于生成 PowerPoint 演示文稿的 JavaScript 库，支持 Node.js、React、浏览器等多种环境，无需安装 PowerPoint 即可创建专业演示文稿。

- 🚀 **功能丰富**：支持创建文本、表格、形状、图像、图表等多种幻灯片对象，并支持 SVG、GIF、YouTube 嵌入等。
- 🌍 **广泛兼容**：兼容 PowerPoint、Keynote、LibreOffice 等 OOXML 应用，支持现代浏览器和 Node.js 环境。
- 📦 **简单易用**：仅需 4 行代码即可创建演示文稿，提供完整的 TypeScript 定义和 75+ 示例幻灯片。
- 💾 **多种导出方式**：支持下载为 .pptx 文件，或导出为 base64、Blob、Buffer 等格式。
- � **HTML 转 PowerPoint**：轻松将 HTML 表格转换为幻灯片，适合动态数据报告和 Web 应用导出。
- 📖 **详细文档**：提供快速入门指南、完整 API 参考和集成教程，帮助开发者快速上手。
- 🛠️ **社区支持**：欢迎提交问题和建议，提供预配置的 jsFiddle 和 StackOverflow 支持。
- 🙏 **开源贡献**：感谢众多贡献者的支持，特别提及 Dzmitry Dulko、Michal Kacerovský 等关键贡献者。
- 📜 **MIT 许可证**：项目完全开源，鼓励社区参与和支持。

---

### [PptxGenJS 功能演示](https://gitbrent.github.io/PptxGenJS/demo/browser/index.html)

**原文标题**: [PptxGenJS Feature Demos](https://gitbrent.github.io/PptxGenJS/demo/browser/index.html)

概述总结  
该内容主要介绍了 PptxGenJS 库的功能和使用方法，包括图表类型、形状、颜色方案、演示文稿基础操作、HTML 转 PPT 功能、动态表格选项、图像、媒体、形状、文本、表格以及幻灯片母版等。  

- 📚 **库信息** - 包含库版本、图表类型、形状类型和颜色方案。  
- 🏗️ **基础演示** - 提供可编辑代码和沙箱执行功能，方便用户尝试库的各种特性。  
- 🖥️ **HTML 转 PPT** - 支持将 HTML 表格转换为 PPT 幻灯片，包括自动分页和样式设置。  
- 📊 **动态表格选项** - 可设置行数、单元格边距、重复标题行等参数。  
- 🎨 **样式演示** - 展示无样式和带样式的表格，支持单元格样式和边框设置。  
- 🔀 **跨行跨列** - 演示表格中的跨行（rowspan）和跨列（colspan）功能。  
- 📈 **图表功能** - 支持多种图表类型，如条形图、折线图、饼图、雷达图等。  
- 🖼️ **图像处理** - 支持多种图像类型（GIF、JPG、PNG 等）和操作（旋转、阴影、裁剪等）。  
- 📹 **媒体支持** - 支持视频（avi、mp4 等）和音频（mp3、wav 等）嵌入，包括 YouTube 链接。  
- 🔷 **形状与文本** - 提供多种形状（矩形、圆形等）和文本格式（对齐、超链接、项目符号等）。  
- 📑 **表格功能** - 支持表格布局、单元格格式、自动分页和复杂文本处理。  
- 🏛️ **幻灯片母版** - 演示如何使用母版幻灯片和模板布局。

---

### [店员开单](https://clerk.com/billing?dub_id=5XtVJqg7EIC4lDh1)

**原文标题**: [Clerk Billing](https://clerk.com/billing?dub_id=5XtVJqg7EIC4lDh1)

Clerk Billing 是为 B2C 和 B2B 应用实现订阅功能的最简单方式，无需编写支付集成代码、设计 UI 或处理 Webhooks。

- 🚀 **快速开始**：直接在 Clerk 中定义和管理订阅计划，无需编码。  
- 🛠️ **仪表盘配置**：通过 Clerk 仪表盘设置计划，使用 `<PricingTable />` 组件创建定价页面。  
- 👥 **用户管理**：客户可通过 Clerk 的个人资料组件管理订阅。  
- 💳 **支付集成**：支持 100+ 支付方式，与 Stripe 连接处理定期账单。  
- 🔒 **数据同步**：自动更新并存储用户订阅状态，无需复杂同步代码。  
- 🔑 **权限控制**：使用 `has()` 助手和 `<Protect />` 组件基于订阅计划控制访问权限。  
- 🌍 **多语言支持**：提供 30+ 种语言的本地化选项，支持自定义翻译。  
- ⚙️ **灵活集成**：支持 Next.js、React、React Router 和 React Native（通过 Expo SDK）。  
- 📈 **扩展功能**：未来支持按量计费、按席位计费、税费管理、优惠券、付费附加功能和试用期。  
- 🔐 **高安全性**：符合 SOC 2 TYPE II、HIPAA、CCPA 等标准，不存储信用卡信息。  
- 💡 **开发者友好**：提供预构建组件和钩子，支持深度定制。

---

### [版本 v8.0.0 | Mantine](https://mantine.dev/changelog/8-0-0/)

**原文标题**: [Version v8.0.0 | Mantine](https://mantine.dev/changelog/8-0-0/)

Mantine v8.0.0 于 2025 年 5 月 5 日发布，包含多项新功能和改进，同时提供迁移指南帮助用户从 7.x 版本升级。主要更新包括全局样式分割、菜单子菜单支持、日期组件使用字符串格式、新增时间选择器和热图组件，以及代码高亮和轮播组件的重大变更。

- 🚀 **版本发布** - Mantine v8.0.0 于 2025 年 5 月 5 日发布，源代码已在 GitHub 上公开。
- 💖 **支持开发** - 用户可通过 OpenCollective 赞助 Mantine 的开发，资金将用于改进和新增功能。
- 📚 **迁移指南** - 提供详细的 7.x 到 8.x 迁移指南，帮助用户顺利升级。
- 🎨 **全局样式分割** - 全局样式现在分为三个文件：`baseline.css`、`default-css-variables.css` 和 `global.css`。
- 🍔 **菜单子菜单** - `Menu` 组件新增子菜单支持，提升导航体验。
- 🎯 **Popover 改进** - `Popover` 组件新增 `hideDetached` 属性，控制下拉框在目标元素隐藏时的行为。
- 📅 **日期字符串格式** - `@mantine/dates` 组件现在使用 `YYYY-MM-DD` 或 `YYYY-MM-DD HH:mm:ss` 格式的字符串，避免时区问题。
- ⏰ **新增 TimePicker** - 提供更多功能的时间选择器，支持 24 小时和 12 小时格式。
- 📊 **新增 Heatmap 组件** - 新增热图组件，支持日历形式的数据展示。
- ✨ **代码高亮改进** - `@mantine/code-highlight` 不再依赖 `highlight.js`，支持通过适配器使用任意语法高亮库。
- 🚗 **轮播组件更新** - `@mantine/carousel` 更新至最新版 `embla-carousel-react`，移除部分属性并调整 API。
- 🎚️ **Switch 组件改进** - `Switch` 组件新增 `withThumbIndicator` 属性，调整样式。
- 🛠️ **其他改进** - 包括主题类型扩展、`Kbd` 组件支持 `size` 属性、`ScrollArea` 组件样式调整等。

---

### [曼蒂恩](https://mantine.dev/)

**原文标题**: [Mantine](https://mantine.dev/)

一个功能全面的 React 组件库 Mantine，提供 120+ 可定制组件和 70+ 钩子，支持快速构建功能完善且易访问的 Web 应用。

- 🚀 **快速开发** - 包含 120+ 高质量组件（如输入框、日期选择器等）和 70+ 实用钩子，加速应用开发  
- 🎨 **灵活样式** - 支持 CSS、Styles API 等多种样式方案，轻松覆盖默认样式  
- 🌙 **暗色主题** - 一行代码切换暗色模式，所有组件原生支持  
- 🔧 **组合式组件** - Combobox 提供高度定制能力，可构建选择框、标签输入等复杂功能  
- 📊 **扩展功能** - 富文本编辑器、通知系统、轮播图等扩展包满足多样化需求  
- 📝 **表单库** - 轻量级高性能表单库`@mantine/form`，支持复杂验证和嵌套数据结构  
- 🌍 **社区支持** - 28k+ GitHub 星标，活跃的 Discord 社区和优质文档  
- ⚡ **多框架适配** - 支持 Next.js、Vite、React Router 等现代工具链

---

### [热力图 | Mantine](https://mantine.dev/charts/heatmap/)

**原文标题**: [Heatmap | Mantine](https://mantine.dev/charts/heatmap/)

概述：本文详细介绍了 Mantine 图表库中的 Heatmap 组件，包括其基本用法、数据格式、自定义样式、工具提示、颜色调整、标签设置等功能。

- 📅 **基本用法**：Heatmap 组件用于以表格形式展示数据，每列代表一周。必须提供`data`属性，格式为`YYYY-MM-DD`日期键和数值值的对象。
- 🎨 **自定义颜色**：通过`colors`属性可以调整热力图的颜色，支持 CSS 颜色值。默认使用 4 种颜色表示热度级别。
- 🔍 **工具提示**：设置`withTooltip`和`getTooltipLabel`属性可以在悬停时显示工具提示，自定义提示内容。
- 📊 **数据范围**：使用`domain`属性手动指定数值范围，适用于数据未覆盖全部可能值的情况。
- 🏷️ **标签设置**：通过`withMonthLabels`和`withWeekdayLabels`显示月份和星期标签，并可自定义标签文本。
- 📏 **矩形样式**：调整`rectSize`、`rectRadius`和`gap`属性可以改变矩形的大小、圆角和间隙。
- 🖱️ **交互功能**：使用`getRectProps`属性可以为每个矩形添加点击事件等交互功能。
- 🚫 **隐藏外部日期**：设置`withOutsideDates`为`false`可以隐藏指定范围之外的日期。
- 🌍 **首日设置**：通过`firstDayOfWeek`属性可以更改每周的第一天，默认为周一。

---

### [树 | Mantine](https://mantine.dev/core/tree/)

**原文标题**: [Tree | Mantine](https://mantine.dev/core/tree/)

概述：本文详细介绍了 Mantine 库中的 Tree 组件，包括其基本用法、数据格式要求、自定义渲染、状态控制（展开/选中/勾选）以及实际应用示例（如文件树展示）。

- 🌳 **Tree 组件功能**：用于展示层级数据，默认样式简洁，可通过 Styles API 自定义  
- 📝 **数据格式要求**：  
  - 必须为数组结构，每个节点需包含`value`和`label`字段  
  - 子节点通过`children`数组嵌套，`value`值必须唯一  
- 🎨 **自定义渲染**：通过`renderNode`属性可完全控制节点渲染（含图标、交互逻辑等）  
- ⚙️ **状态控制**：  
  - 使用`useTree`钩子管理展开/选中/勾选状态  
  - 支持批量操作（如`expandAllNodes`/`checkAllNodes`）  
- 📂 **文件树示例**：演示如何结合图标库实现可视化文件目录（区分文件夹/文件类型）  
- 🔍 **初始状态设置**：通过`getTreeExpandedState`可快速生成默认展开的节点配置  
- ✅ **复选框功能**：支持节点勾选状态，提供`isNodeChecked`等状态判断方法

---

### [半圆进度条 | Mantine](https://mantine.dev/core/semi-circle-progress/)

**原文标题**: [SemiCircleProgress | Mantine](https://mantine.dev/core/semi-circle-progress/)

概述  
SemiCircleProgress 是一个用于展示半圆形进度条的组件，支持多种自定义配置，包括填充方向、颜色、大小、标签位置等。  

- 📊 **功能** - 用半圆形图表展示进度，支持多种自定义配置。  
- 📂 **源码与文档** - 提供源码查看、文档说明及属性（Props）和样式 API。  
- 🎨 **样式定制** - 可调整填充颜色（`filledSegmentColor`）、空白段颜色（`emptySegmentColor`）、大小（`size`）和厚度（`thickness`）。  
- 🔄 **填充方向** - 支持从左到右（`left-to-right`）或从右到左（`right-to-left`）填充。  
- ⬆️ **方向控制** - 可设置半圆朝上（`up`）或朝下（`down`）。  
- 🏷️ **标签位置** - 默认标签在底部，可通过 `labelPosition` 设置为居中（`center`）。  
- ⏱️ **过渡动画** - 默认无过渡效果，可通过 `transitionDuration` 设置过渡时间（毫秒）。  
- 🎲 **动态值** - 支持动态更新进度值，示例中展示了随机值设置功能。  
- 🔗 **相关组件** - 提及了 `RingProgress` 和 `Skeleton` 等其他组件。  
- 🌐 **社区支持** - 提供 Discord、X（Twitter）、GitHub 等社区交流渠道。

---

### [GitHub - hyparam/hyparquet: JavaScript 的 Parquet 文件解析器](https://github.com/hyparam/hyparquet)

**原文标题**: [GitHub - hyparam/hyparquet: parquet file parser for javascript](https://github.com/hyparam/hyparquet)

hyparquet 是一个轻量级、无依赖的纯 JavaScript 库，用于解析 Apache Parquet 文件，适用于浏览器和 Node.js 环境，支持高效处理大型数据集。

- 🚀 **轻量无依赖**：纯 JavaScript 实现，无外部依赖，体积小巧（仅 9.7kb min.gz）。  
- 🌐 **浏览器原生支持**：可直接在浏览器中运行，支持在线查看 Parquet 文件（如通过 hyperparam.app）。  
- ⚡ **高性能**：按需加载数据，适合大数据和机器学习场景。  
- 📜 **高度兼容**：支持所有 Parquet 编码和压缩格式（需配合 hyparquet-compressors 包）。  
- 🔧 **功能丰富**：支持读取元数据、流式分块处理、自定义异步缓冲等。  
- 📦 **TypeScript 支持**：内置类型定义。  
- 🛠 **扩展性**：可通过插件支持更多压缩格式（如 gzip、zstd）。  
- 📊 **演示与示例**：提供 React 集成示例和在线演示，便于快速上手。  
- 🔄 **活跃维护**：由 Hugging Face 开源资助，社区贡献欢迎。  

**核心功能**：  
- 读取 Parquet 文件内容（`parquetReadObjects`）。  
- 异步获取远程文件（`asyncBufferFromUrl`）。  
- 支持行/列过滤以优化性能。  

**适用场景**：数据科学、Web 应用数据可视化及无需后端的 Parquet 文件处理。

---

### [超参数 - 看看你的数据 👀](https://hyperparam.app/)

**原文标题**: [Hyperparam - Look At Your Data 👀](https://hyperparam.app/)

Hyperparam 是一款专注于机器学习数据探索和分析的浏览器工具，支持大规模文本数据集的高效处理，采用现代数据格式（如 parquet）实现本地化操作，并倡导开源理念。

- 👁️ **数据质量至关重要**：机器学习成功的关键在于数据质量，Hyperparam 帮助用户在浏览器中直接探索和分析海量文本数据集。  
- � **快速开始**：支持拖放数据集（如 parquet 格式），无需复杂配置即可启动分析。  
- 🌐 **大规模数据演示**：示例展示了如何通过浏览器直接读取 S3 中的英文 Wikipedia 全量 parquet 文件，实现按需检索。  
- 🛠️ **LLM 数据集工具**：解决传统工具无法交互式处理现代数据规模的问题，支持数十亿行数据的即时加载与探索。  
- 🔍 **模型辅助数据探索**：利用模型反哺训练数据，帮助用户筛选高质量数据以优化模型性能。  
- 💻 **本地优先设计**：完全在浏览器中运行，提供 CLI 工具（如`npx hyperparam`）便捷访问本地文件。  
- 🔓 **开源核心**：坚持开源优先，代码公开于 GitHub，推动开放数据标准和社区共享。  
- 📅 **最新动态**：2025 年 4 月宣布推出 Hyperparam 开源生态，持续更新博客与资源。

---

### [react-sounds - React 音效库](https://www.reactsounds.com/)

**原文标题**: [react-sounds - Sound Effects for React](https://www.reactsounds.com/)

好的，请提供您需要总结的文本内容，我会按照以下模板为您生成简洁的要点列表：  

overview summary  

- 🌟 Emoji 要点 1  
- 📌 Emoji 要点 2  
- 🔍 Emoji 要点 3  

请将需要总结的文本粘贴进来，我会立即为您处理！

---

### [GitHub - ije/mono-jsx: 将`<html>`作为`Response`返回](https://github.com/ije/mono-jsx)

**原文标题**: [GitHub - ije/mono-jsx: `<html>` as a `Response`.](https://github.com/ije/mono-jsx)

mono-jsx 是一个轻量级的 JSX 运行时，用于在 JavaScript 运行时（如 Node.js、Deno、Bun、Cloudflare Workers 等）中将 `<html>` 元素渲染为 `Response` 对象。

- 🚀 无需构建步骤，直接使用 JSX 语法
- 🦋 轻量级（8KB gzipped），零依赖
- 🔫 支持响应式状态管理
- 🛟 完整的 Web API TypeScript 定义
- ⏳ 支持流式渲染
- 🥷 集成 htmx
- 🌎 跨平台支持（Node.js、Deno、Bun、Cloudflare Workers 等）
- 📦 提供 `html`、`css` 和 `js` 标签函数
- 🔄 支持异步组件和生成器
- 🎨 支持标准 HTML 属性名（如 `class` 代替 `className`）
- 🧩 使用 `<slot>` 元素进行内容分发
- ⚠️ 注意：事件处理程序仅在客户端执行

---

### [发布 6.7.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.7.0)

**原文标题**: [Release 6.7.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.7.0)

Prisma 发布了 6.7.0 稳定版本，引入了多项新功能和改进，包括无 Rust 引擎的 Prisma ORM 早期访问、对 better-sqlite3 JavaScript 驱动的支持、多文件 Prisma 模式的生产就绪以及生成的输出分割等。

- 🎉 Prisma ORM 6.7.0 稳定版发布，包含多项新功能和改进。
- 🚀 提供无 Rust 引擎的 Prisma ORM 早期访问，改用 TypeScript 编写的查询编译器，提升性能和架构效率。
- 📚 支持 PostgreSQL 和 SQLite 数据库，未来将支持更多数据库。
- 🔧 使用新的查询编译器需添加 queryCompiler 和 driverAdapters 特性标志。
- 🛠️ 引入对 better-sqlite3 JavaScript 驱动的支持，可通过 driverAdapters 预览功能使用。
- 📂 多文件 Prisma 模式现已生产就绪，支持将模式文件分割为多个文件。
- ✂️ 新的 prisma-client 生成器将生成的输出分割为多个文件，避免单个大文件导致的性能问题。
- 🎯 生成的文件不再引发 ESLint 和 TypeScript 错误，提升开发体验。
- 📢 公司新闻包括 Prisma Postgres 与 Vercel Marketplace 的集成等新动态。

---

### [发布 Slack Send v2.1.0 · slackapi/slack-github-action · GitHub](https://github.com/slackapi/slack-github-action/releases/tag/v2.1.0)

**原文标题**: [Release Slack Send v2.1.0 · slackapi/slack-github-action · GitHub](https://github.com/slackapi/slack-github-action/releases/tag/v2.1.0)

Slack GitHub Action 发布了 v2.1.0 版本，主要改进了错误消息解析并新增了 API 选项以自定义 Slack API 方法 URL。此外，还包括了多个错误修复、文档更新、依赖项升级和维护工作。

- 👾 **功能增强**  
  - 新增 'api' 选项以自定义 Slack API 方法 URL (#409)  

- 🐛 **错误修复**  
  - 修复环境变量冲突导致的错误 (#374)  
  - 修复自定义 'api' URL 发送问题 (#420)  
  - 在日志中显示解析错误原因 (#431)  

- 📚 **文档更新**  
  - 修复参数名称错误 (#371)  
  - 更新用例示例 (#376)  
  - 添加版本迁移指南 (#410)  
  - 文档结构调整 (#422, #424, #425)  

- 🤖 **依赖项升级**  
  - 升级 axios、codecov-action、slack/web-api 等多个依赖项 (#369, #365, #392 等)  
  - 修复安全漏洞 CVE-2025-27152 (#407)  

- 🧰 **维护工作**  
  - 减少 GitHub Actions 权限 (#375)  
  - 重构日志配置 (#408)  
  - 发布 v2.1.0 (#438)  

- 💌 **新贡献者**  
  - 欢迎 @topkim993、@slackapi、@lukegalbraithrussell 首次贡献 (#371, #422, #424)

---

### [GitHub - panva/openid-client: 适用于 JavaScript 运行时的 OAuth 2 / OpenID Connect 客户端 API](https://github.com/panva/openid-client)

**原文标题**: [GitHub - panva/openid-client: OAuth 2 / OpenID Connect Client API for JavaScript Runtimes](https://github.com/panva/openid-client)

openid-client 是一个用于 JavaScript 运行时的 OAuth 2 / OpenID Connect 客户端 API，简化了与授权服务器的集成，支持多种认证和授权流程。

- 🔍 **功能概述**：支持 OpenID Connect 1.0、OAuth 2.0/2.1、FAPI 1.0/2.0 等协议，提供授权码流、刷新令牌、设备授权等多种授权方式。
- 🌐 **多运行时支持**：适用于 Node.js、浏览器、Deno、Cloudflare Workers 等多种 JavaScript 运行时。
- 📜 **认证与合规**：通过 OpenID Connect™ 基础、FAPI 1.0 和 FAPI 2.0 认证。
- 💡 **快速开始**：提供简单的 API 发现和授权码流示例，便于快速集成。
- 🔄 **扩展功能**：支持 DPoP、JWT 安全请求、PAR 等高级特性。
- 🛠 **开发支持**：提供详细的 API 文档、示例代码和社区支持，鼓励通过赞助支持项目发展。
- 📦 **分发渠道**：通过 npmjs.com、jsr.io 和 github.com 分发，支持 ESM 和 CJS 模块。
- 🔒 **安全与维护**：强调安全修复和持续维护，支持多种现代 JavaScript 运行时和版本。

---

### [docx - 使用 JavaScript 生成.docx 文档](https://docx.js.org/#/)

**原文标题**: [docx - Generate .docx documents with JavaScript](https://docx.js.org/#/)

好的，请提供您需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结。  
- 📌 关键点一  
- 🔍 关键点二  
- 💡 关键点三  

请提供具体内容，我会为您整理！

---

### [GitHub - prettier/eslint-plugin-prettier: 用于 Prettier 格式化的 ESLint 插件](https://github.com/prettier/eslint-plugin-prettier)

**原文标题**: [GitHub - prettier/eslint-plugin-prettier: ESLint plugin for Prettier formatting](https://github.com/prettier/eslint-plugin-prettier)

这是一个关于 `eslint-plugin-prettier` 插件的介绍和配置指南，该插件用于将 Prettier 作为 ESLint 规则运行，并报告格式化差异。

- 🛠️ **功能概述**: 将 Prettier 作为 ESLint 规则运行，报告格式化差异。
- 📦 **安装**: 需要单独安装 Prettier 和 ESLint，推荐禁用其他格式化相关的 ESLint 规则。
- ⚙️ **配置**: 提供了传统 `.eslintrc*` 和新的 `eslint.config.js` 两种配置方式。
- ⚠️ **注意事项**: 使用 `arrow-body-style` 和 `prefer-arrow-callback` 规则时可能出现问题，推荐关闭这些规则。
- 🔧 **选项**: 支持传递 Prettier 选项，但不推荐通过 ESLint 配置传递。
- 🤝 **贡献**: 提供了贡献指南和变更日志。
- 📜 **许可证**: 使用 MIT 许可证。

---

### [一丝不苟](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=may9th2025)

**原文标题**: [Meticulous](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=may9th2025)

Meticulous AI 提供了一种无需编写和维护测试的自动化测试解决方案，通过记录用户交互并生成持续演化的测试套件，覆盖所有边缘情况，提升开发效率和代码质量。

- 🚀 **无需编写测试** - Meticulous AI 通过记录用户交互自动生成测试套件，无需手动编写或维护测试。
- 🔍 **全面覆盖** - 监控代码分支和用户流程，确保覆盖所有边缘情况和每行代码。
- ⚡ **快速反馈** - 在合并前查看代码变更对用户流程的影响，避免回归问题。
- 🛠️ **无缝集成** - 轻松集成到现有开发环境，支持多种框架（如 React、Vue、Angular 等）。
- 📈 **持续演化** - 测试套件随应用功能更新自动调整，保持测试的时效性和完整性。
- 🏆 **客户认可** - 被 Dropbox、WithPower 和 Lattice 等 100 多家组织信任，显著提升开发效率和代码信心。
- ⚙️ **技术优势** - 基于 Chromium 的确定性调度引擎，消除测试波动，执行速度快且稳定。
- 📚 **灵活使用** - 可作为现有测试套件的补充或完全替代方案，支持大规模并行测试。

---

### [职业发展 | Brilliant](https://brilliant.org/careers/)

**原文标题**: [Careers | Brilliant](https://brilliant.org/careers/)

Brilliant 致力于培养全球问题解决者，专注于为成人提供数学、数据科学及 AI 等领域的互动学习体验，拥有健康商业模式和多元化团队文化。  

- 🎯 **使命与愿景**：打造问题解决者的世界，通过互动学习改变教育方式，专注实用技能而非抽象理论。  
- 🌍 **团队分布**：约 100 人，以旧金山和纽约为核心，半数成员就近办公，支持远程协作与季度线下聚会。  
- � **文化特质**：高执行力、低自我，倡导卓越、冒险、坦诚与终身学习，工作自主性强且项目迭代快。  
- 📊 **业务现状**：付费用户达数十万，盈利稳健，估值务实，正加速扩展至百万用户规模。  
- 👥 **团队多样性**：成员背景多元，涵盖科学家、艺术家、工程师等，鼓励 underrepresented 群体加入。  
- 🛠 **招聘开放**：提供远程工程、内容制作等职位，接受非公开岗位咨询，重视创意与协作能力。  
- ✨ **成员故事**：团队经历丰富，包括密码学冠军、直升机飞行员、高中创办者等，凸显“非常规”人才。  
- 📅 **工作模式**：核心协作时段（太平洋 10am-3pm），强调实时合作，兼顾高强度工作与充足休假。

---

### [CSS 旋转木马效果  |  Chrome 开发者博客](https://developer.chrome.com/blog/carousels-with-css)

**原文标题**: [Carousels with CSS  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/carousels-with-css)

Chrome 135 版本引入了 CSS Overflow 5 规范的新功能，无需 JavaScript 即可创建滚动和轮播效果。这些功能包括滚动按钮、滚动标记、滚动驱动动画等，且浏览器自动处理了轮播的最佳实践和可访问性问题。

- 🚀 **新功能发布**：Chrome 135 支持 CSS Overflow 5 规范，提供无需 JavaScript 的滚动和轮播体验。
- 🎥 **视频展示**：展示了滚动按钮、滚动标记、滚动驱动动画等多种新功能的和谐应用。
- ♿ **可访问性优化**：浏览器自动处理轮播的可访问性，确保最佳用户体验。
- 🛠️ **滚动按钮**：通过`::scroll-button()`添加，支持左右滚动，内容可自定义。
- 🔖 **滚动标记**：通过`::scroll-marker()`添加，支持快速导航到指定内容，可自定义标记样式。
- 📏 **基本滚动区域**：使用 CSS 创建滚动区域，支持水平和垂直滚动。
- 🖱️ **滚动按钮添加**：通过 CSS 伪元素添加滚动按钮，支持自定义内容和样式。
- 📌 **滚动标记添加**：通过 CSS 伪元素添加滚动标记，支持自定义内容和样式，增强导航体验。
- 🔄 **组合使用**：滚动按钮和标记可同时使用，提升用户体验，无需 JavaScript。
- 📚 **资源推荐**：提供了轮播配置器和轮播画廊，展示更多高级功能和用例。
- 🔮 **未来改进**：计划支持自定义元素和循环滚动功能，进一步提升用户体验。
- 📜 **许可证信息**：内容遵循 Creative Commons Attribution 4.0 License，代码遵循 Apache 2.0 License。

---

### [“CSS 轮播”是否具有可访问性？](https://www.sarasoueidan.com/blog/css-carousels-accessibility/)

**原文标题**: [Are 'CSS Carousels' accessible?](https://www.sarasoueidan.com/blog/css-carousels-accessibility/)

CSS Carousels 的可访问性分析

- 🚨 **实验性功能**：CSS Carousels 目前是高度实验性的，尚未准备好投入生产环境，主要因为浏览器支持不足和严重的可访问性问题。
  
- 🔍 **可访问性问题**：所有示例中的滚动标记（scroll markers）都被浏览器暴露为 `tab` 角色，但缺乏对应的 `tabpanel`，违反了 ARIA 规范中对 Tabs 组件的要求。

- 📌 **命名问题**：滚动标记的 accessible name 通过 CSS `content` 属性提供，但所有标记共享相同的名称，无法区分不同项，导致用户无法理解每个标记的具体作用。

- 🎭 **语义不匹配**：尽管组件被暴露为 Tabs，但实际行为并不符合 Tabs 的交互模式（如多项目同时可见、键盘导航混乱等），导致屏幕阅读器用户和键盘用户的操作体验极差。

- 🛠 **开发者责任**：开发者需要手动补充缺失的 ARIA 角色（如 `tabpanel`），但即使如此，组件的底层行为（如滚动容器特性）仍会破坏 Tabs 的预期交互。

- ⚠️ **浏览器实现缺陷**：`::scroll-marker` 和 `::scroll-button` 的交互伪元素缺乏完整的可访问性支持（如禁用状态未正确暴露、焦点管理异常等）。

- 📚 **规范与现实的差距**：CSS 规范未明确说明这些功能如何影响可访问性树，导致开发者误以为浏览器会“自动处理可访问性”，而实际上需要大量手动修复。

- 💡 **替代方案建议**：呼吁优先开发原生 HTML 组件（如 `<tabs>`、`<carousel>`），而非依赖 CSS 抽象层，以从根本上解决语义和交互问题。

- 🔧 **测试与改进**：强调开发者必须通过屏幕阅读器和键盘测试组件，并理解 ARIA 角色与用户期望的匹配程度。

- 🌟 **核心结论**：CSS Carousels 目前不可访问，不推荐使用；更重要的是培养对新技术特性的批判性思维，始终以用户体验为中心评估功能可行性。  

（注：以上总结基于原文对四个示例的详细分析，涵盖键盘导航、屏幕阅读器兼容性、ARIA 规范匹配等关键问题。）

---

### [水库抽样](https://samwho.dev/reservoir-sampling/)

**原文标题**: [Reservoir Sampling](https://samwho.dev/reservoir-sampling/)

蓄水池抽样是一种在不知道总体大小的情况下进行公平随机抽样的技术。  

- 🎯 **应用场景**：适用于需要从未知大小的数据流中公平选取样本的情况，例如日志收集服务中的流量控制。  
- 🔢 **数学原理**：通过动态调整新元素的选中概率（1/n 或 k/n），确保每个元素被选中的概率均等。  
- 💡 **实现方法**：维护一个大小为 k 的“蓄水池”，对于第 n 个元素，以 k/n 的概率替换蓄水池中的随机一个元素。  
- ⚖️ **公平性验证**：通过数学推导证明，无论数据流多长，每个元素被选中的概率均为 k/n。  
- 📊 **日志收集示例**：用蓄水池抽样限制每秒最多发送 5 条日志，既避免峰值过载，又保留低流量时期的全部数据。  
- 📚 **扩展阅读**：加权蓄水池抽样可处理优先级不同的数据（如错误日志优先保留），但实现更复杂。  
- ✨ **优势**：内存高效（仅存储 k 个样本）、无需预知数据规模、实现简单且严格公平。

---

### [可视化/蓄水池抽样 at main · samwho/可视化 · GitHub](https://github.com/samwho/visualisations/tree/main/reservoir-sampling)

**原文标题**: [visualisations/reservoir-sampling at main · samwho/visualisations · GitHub](https://github.com/samwho/visualisations/tree/main/reservoir-sampling)

这是一个名为“samwho/visualisations”的 GitHub 仓库页面概览。

- 👀 仓库名称：visualisations  
- 🌟 星标数：241  
- 🍴 复刻数：6  
- 📜 代码、问题、拉取请求等功能标签可见  
- 🔒 需要登录才能更改通知设置  
- 📂 其他导航选项包括代码、问题、拉取请求等

---

### [第一部分：我们如何对 Next.js 失去热情，重新爱上 Ruby on Rails 和 Inertia.js](https://hardcover.app/blog/part-1-how-we-fell-out-of-love-with-next-js-and-back-in-love-with-ruby-on-rails-inertia-js)

**原文标题**: [Part 1: How We Fell Out of Love with Next.js and Back in Love with Ruby on Rails & Inertia.js](https://hardcover.app/blog/part-1-how-we-fell-out-of-love-with-next-js-and-back-in-love-with-ruby-on-rails-inertia-js)

overview summary  
Hardcover 是一个图书相关的平台，最初使用 Next.js 构建，后来迁移到 Ruby on Rails 和 Inertia.js。迁移的主要原因是 Next.js 的缓存不清晰、成本不可控以及开发速度慢。新的架构显著提升了性能，降低了成本，并改善了开发体验。  

- 🚀 **迁移原因**：Next.js 的缓存机制不透明，服务器成本飙升，开发速度缓慢。  
- 💡 **新架构**：采用 Ruby on Rails 和 Inertia.js，结合 React 前端，实现了服务器端渲染（SSR）和直接数据库连接。  
- 🔍 **技术选型**：评估了 Remix 和 Rails，最终选择 Rails 并搭配 Inertia.js，因其性能和对 React 的良好支持。  
- ⚙️ **实现细节**：使用 Rails 控制器生成数据，Inertia.js 传递数据到 React 组件，Vite 处理前端构建。  
- 📉 **成本优化**：从 Vercel 和 Google Cloud Run 迁移到 Digital Ocean，显著降低了运营成本。  
- 🚀 **性能提升**：Google Pagespeed 分数大幅提高，页面加载时间减少，用户体验改善。  
- 📈 **效果验证**：迁移后，用户停留时间翻倍，SEO 表现提升，新用户注册保持稳定。  
- 🔜 **未来计划**：修复剩余问题，优化慢速页面，加大市场推广力度。

---

### [PostgreSQL：PostgreSQL 18 Beta 1 发布！](https://www.postgresql.org/about/news/postgresql-18-beta-1-released-3070/)

**原文标题**: [PostgreSQL: PostgreSQL 18 Beta 1 Released!](https://www.postgresql.org/about/news/postgresql-18-beta-1-released-3070/)

PostgreSQL 18 Beta 1 已发布，这是 PostgreSQL 18 的第一个测试版本，包含所有计划功能的预览。社区鼓励用户测试新功能以帮助发现和修复问题，尽管不建议在生产环境中使用此测试版。  

- 🚀 **性能提升**：PostgreSQL 18 引入了异步 I/O（AIO）子系统，支持 Linux 的 io_uring，可提高 I/O 吞吐量并减少延迟，部分测试显示性能提升 2-3 倍。  
- 🔍 **查询优化**：新增多列 B 树索引的“跳过扫描”功能，优化了包含 `OR` 和 `IN` 的 `WHERE` 子句，并改进了表连接性能。  
- 📊 **统计信息保留**：支持在主要版本升级时保留优化器统计信息，减少升级后运行 `ANALYZE` 的时间。  
- ⚡ **并行处理**：`pg_upgrade` 现在支持并行检查，并新增 `--swap` 选项以加速升级过程。  
- 💡 **开发者体验**：新增虚拟生成列（实时计算而非存储）、UUIDv7 生成函数，并支持在 `RETURNING` 子句中访问旧值和新值。  
- 🔒 **安全性增强**：引入 OAuth 2.0 认证，弃用 `md5` 密码认证，推荐使用 SCRAM，并支持 FIPS 模式验证。  
- 📈 **监控改进**：`EXPLAIN ANALYZE` 新增缓冲区访问统计，`pg_stat_all_tables` 显示真空和分析时间，并增强逻辑复制的冲突监控。  
- ✅ **默认数据校验**：新集群默认启用数据校验，可通过 `initdb --no-data-checksums` 禁用。  
- 🔄 **协议更新**：新增 PostgreSQL 有线协议 3.2 版本，但 libpq 默认仍使用 3.0。  
- 🐞 **测试与反馈**：社区呼吁用户测试并反馈问题，以确保最终版本的稳定性。正式版预计于 2025 年 9/10 月发布。

---

### [Gemini 2.5 Pro 预览版：更卓越的编程性能

- Google 开发者博客](https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/)

**原文标题**: [
            
            Gemini 2.5 Pro Preview: even better coding performance
            
            
            - Google Developers Blog
            
        ](https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/)

Google 发布了 Gemini 2.5 Pro 预览版（I/O 版），重点提升编码能力，尤其在前端和 UI 开发方面表现卓越。

- 🚀 **提前发布**：Gemini 2.5 Pro 预览版提前几周推出，为开发者提供更强的编码工具。  
- 💻 **编码能力提升**：在代码转换、编辑及复杂工作流创建方面有显著改进。  
- 🌟 **前端开发领先**：在 WebDev Arena 排行榜上排名第一，支持 Cursor 等创新代码代理。  
- 🎥 **视频理解与应用**：结合视频理解能力（VideoMME 基准得分 84.8%），实现从视频生成交互式学习应用。  
- 🛠️ **简化开发流程**：帮助开发者快速实现功能，如自动生成 CSS 代码和 UI 设计。  
- 📱 **快速原型开发**：支持从概念到功能完备的 Web 应用，如听写启动应用。  
- 🔧 **开发者工具**：可通过 Google AI Studio 和 Vertex AI 使用 Gemini 2.5 Pro，企业客户尤其受益。  
- 🔄 **无缝升级**：现有用户无需操作即可使用改进版，价格不变。  

期待开发者利用 Gemini 2.5 Pro 构建更多创新应用！

---

### [React 状态](https://react.statuscode.com/)

**原文标题**: [React Status](https://react.statuscode.com/)

每周汇总最新的 React 和 React Native 相关链接和教程，提供订阅服务，拥有大量订阅者和定期发布的刊物。

- 📬 57698 位订阅者 — 展示广泛的读者群体  
- 📰 428 期内容 — 长期稳定的更新历史  
- 🔗 提供 RSS 订阅方式 — 方便读者获取最新内容  
- 📢 鼓励查看最新一期 — 作为内容样本预览  
- 🏢 由 Cooperpress 出版 — 专业的发布背景  
- 🔒 严格的隐私、反垃圾邮件和 GDPR 政策 — 重视用户数据保护

---

### [Node 周刊](https://nodeweekly.com/)

**原文标题**: [Node Weekly](https://nodeweekly.com/)

Node Weekly 是一份免费的每周电子邮件简报，专注于 Node.js 的新闻和文章。  

- 📧 免费订阅，每周发送一次  
- 📰 包含 Node.js 新闻和文章摘要  
- ✉️ 拥有 62,762 名订阅者  
- 📂 已发布 577 期  
- 📡 提供 RSS 订阅方式  
- 🔍 可查看最新一期作为样例  
- 🏢 由 Cooperpress 发布  
- 🔒 严格遵守隐私、反垃圾邮件和 GDPR 政策  
- ®️ Node.js 是 Joyent, Inc 的注册商标，经许可使用

---

