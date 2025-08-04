### [《JavaScript 周刊》第 747 期：2025 年 8 月 1 日](https://javascriptweekly.com/issues/747)

**原文标题**: [JavaScript Weekly Issue 747: August 1, 2025](https://javascriptweekly.com/issues/747)

概述：本期内容涵盖了 JavaScript 生态的最新动态，包括 Observable Notebooks 2.0 技术预览、Node.js 新特性、JavaScript 运行时回顾、工具更新以及相关教程和资源推荐。

- 🚀 **Observable Notebooks 2.0 技术预览**：推出基于 HTML 的新笔记本文件格式，支持原生 JavaScript 和库导入功能。
- 📦 **Node.js v22.18 LTS 默认支持 TypeScript**：现在可以直接运行`node app.ts`，与 Bun 和 Deno 类似。
- 🔍 **JavaScript 运行时回顾**：深入探讨了过去十年中主流和边缘的 JavaScript 运行时和引擎。
- 🛠 **工具更新**：
  - pnpm 10.14 支持自动安装和固定 Node.js、Deno 或 Bun 版本。
  - Node-RED 4.1、Ionic 8.7、Storybook 9.1 等工具发布新版本。
- 📚 **文章与视频**：
  - Zod 与 Valibot 的比较视频获得 Zod 创建者的高度评价。
  - Svelte 5 的编译机制解析。
- 🎮 **趣味项目**：使用 GLM-4.5 Air 模型在 MacBook Pro 上实现 JavaScript 版“太空侵略者”游戏。
- 📊 **调查结果**：JavaScript 在 Stack Overflow 2025 调查中仍是最常用语言，React 领先前端库。
- 🛠 **代码与工具**：
  - TanStack DB 为 React 提供嵌入式客户端数据库。
  - Ghost 6.0 RC 即将发布，Node.js 驱动的博客平台。
- 🎁 **额外资源**：Google 推出开源代码字体 Google Sans Code，NPKILL 工具清理`node_modules`文件夹。

---

### [可观察笔记本 2.0 技术预览版 | Observable](https://observablehq.com/notebook-kit/)

**原文标题**: [Observable Notebooks 2.0 Technology Preview | Observable](https://observablehq.com/notebook-kit/)

Observable Notebooks 2.0 技术预览版发布，带来全新的笔记本文件格式、桌面应用及 AI 集成，支持本地优先工作流和现代 JavaScript。

- 📓 发布 Observable Notebook Kit：开源笔记本文件格式及工具，支持生成静态网站  
- 🖥️ 推出 Observable Desktop：macOS 桌面应用，支持本地文件编辑与创新 AI 功能  
- 🚀 技术预览目标：支持文件工作流、采用原生 JavaScript、现代化笔记本、快速静态渲染  
- 🔧 Notebook Kit 功能：CLI 工具和 Vite 插件，支持自托管、持续集成及深度定制  
- ✨ 下一代编辑器愿景：无缝 AI 集成提升创造力，简洁编码界面优化体验  
- 🌐 未来计划：将新编辑器与 AI 功能扩展至网页端，实现协作共享  
- 📄 开放笔记本文件格式：基于 HTML，易于编辑、版本控制及工具开发  
- 🧑‍💻 原生 JavaScript 支持：弃用 Observable 专属语法，提升代码复用性  
- 🎨 主题与自定义：支持样式表、全宽布局、动画背景及多主题切换  
- 📚 现代化标准库：升级 Markdown/HTML/TeX 处理引擎，拥抱 ES 模块  
- ⚡ 静态站点生成：通过 Notebook Kit 快速构建部署，优化 SEO 与加载性能  
- 💻 桌面编辑器演示：提供 macOS 预览版下载，需 Apple Silicon 芯片  
- 🌈 示例库：移植 D3 图表等经典案例，展示新功能可能性  
- 💬 反馈渠道：通过 GitHub Issues/Discussions提交建议，欢迎社区贡献

---

### [可观察框架](https://observablehq.com/framework/)

**原文标题**: [Observable Framework](https://observablehq.com/framework/)

最好的仪表板是通过代码构建的，Observable Framework 是一个开源静态站点生成器，支持快速创建数据应用、仪表板和报告，提供本地开发预览服务器和自动化构建部署的 CLI 工具。

- 🚀 **快速创建**：通过命令行快速构建美观的数据应用、仪表板和报告，支持多种编程语言（Markdown、JavaScript、SQL、Python、R 等）。  
- 🔓 **开源免费**：Observable Framework 是完全开源且免费的静态站点生成器，适合各种数据展示需求。  
- 📝 **灵活编写**：使用 Markdown 编写页面，结合响应式 JavaScript 和数据加载器（支持 SQL、Python、R 等），生成静态站点以实现即时加载。  
- 🛠️ **强大工具链**：包含本地预览服务器、CLI 工具，支持自动化构建和部署，兼容任何编辑器与版本控制系统。  
- 🎨 **丰富主题与库**：内置精心设计的主题、网格和库（如 Observable Plot、D3、Vega-Lite 等），适配多设备展示。  
- 📊 **数据处理支持**：客户端支持 DuckDB、Arquero、SQLite 等工具，便于数据操作与可视化。  
- ⚡ **即刻开始**：通过简单命令 `npx @observablehq/framework@latest create` 即可快速上手。

---

### [可观察笔记本套件 | Observable](https://observablehq.com/notebook-kit/kit)

**原文标题**: [Observable Notebook Kit | Observable](https://observablehq.com/notebook-kit/kit)

Observable Notebook Kit 是一个开源命令行工具，用于基于开放文件格式从 Observable Notebooks 构建静态网站。它包含 Vite 插件和低级 JavaScript 接口，支持深度集成自定义 Web 应用程序。该工具是 Notebooks 2.0 技术预览版的一部分，适用于 macOS 的 Observable Desktop 应用可用于编辑笔记本。

- 📦 **安装**：通过 npm 安装 `@observablehq/notebook-kit`，要求 Node.js 20.19+ 或 22.12+。
- 📄 **笔记本文件格式**：基于 HTML，简单易读且易于编辑，支持多种单元格类型（如 JavaScript、Markdown、HTML、SQL 等）。
- 🛠️ **单元格属性**：支持 `pinned` 属性控制源代码显示，`id` 属性为单元格提供稳定标识。
- 🎨 **主题支持**：提供多种内置主题（如 `air`、`coffee` 等），并支持通过标准样式表应用自定义主题。
- 📑 **页面模板**：支持自定义页面模板，可添加页眉和页脚等额外内容。
- 💻 **命令行接口**：提供 `preview`（实时预览）、`build`（构建静态网站）和 `download`（下载笔记本为 HTML）命令。
- 🔌 **Vite 插件**：推荐用于基于 Vite 的应用程序，支持静态渲染和动态内容替换。
- 📜 **JavaScript 接口**：提供低级 API 用于深度集成，包括解析、转换和运行笔记本单元格的功能。
- 🔧 **实用工具 API**：提供默认值设置和单元格状态管理功能。
- 🏃 **运行时 API**：在 Observable Runtime 基础上提供额外逻辑，支持单元格重定义和标准库功能。

---

### [学习 Observable：响应式数据流 / Observable | Observable](https://observablehq.com/@observablehq/learning-observable-reactive-dataflow)

**原文标题**: [Learning Observable: Reactive dataflow / Observable | Observable](https://observablehq.com/@observablehq/learning-observable-reactive-dataflow)

Observable 是一个端到端的数据应用构建与托管平台，专注于数据可视化和协作分析。

- 🚀 **核心功能**：提供反应式 JavaScript 笔记本和协作画布，支持数据探索、原型设计和仪表盘创建  
- 🎨 **数据可视化**：专为数据展示设计，支持丰富的可视化表达  
- 💻 **平台工具**：包含 Observable Canvases、Notebooks、Framework、Plot 及 D3 等工具  
- 📚 **学习资源**：提供文档、博客、网络研讨会、视频教程和社区支持（Slack/论坛）  
- 🆓 **免费试用**：支持用户免费体验平台功能  
- 🌐 **公司信息**：涵盖产品动态、招聘、联系方式及社交媒体入口（GitHub/LinkedIn 等）  
- 🔒 **政策条款**：明确隐私、安全、服务条款和漏洞披露规范

---

### [催眠轮廓 / Mike Bostock | Observable](https://observablehq.com/@mbostock/hypnocontours)

**原文标题**: [Hypnocontours / Mike Bostock | Observable](https://observablehq.com/@mbostock/hypnocontours)

Observable 平台推出 Notebooks 2.0，专注于数据探索和可视化，提供协作式工具和免费试用选项。

- 🚀 **Notebooks 2.0 发布** - Observable 平台推出新版本，专为数据展示设计。  
- 📊 **数据可视化工具** - 提供反应式 JavaScript 笔记本和协作画布，用于原型设计和仪表盘创建。  
- 🆓 **免费试用** - 用户可免费体验平台功能。  
- 🔧 **平台资源** - 包括 Observable Canvases、Notebooks、Plot、D3 等工具及文档支持。  
- 🌐 **社区与支持** - 提供博客、网络研讨会、Slack 社区和论坛等资源。  
- 💼 **公司信息** - 包含关于我们、招聘、联系方式和社交媒体链接。  
- © **版权声明** - 2025 Observable, Inc. 保留所有权利，提供隐私和安全政策。

---

### [迈克·博斯托克](https://bost.ocks.org/mike/)

**原文标题**: [Mike Bostock](https://bost.ocks.org/mike/)

无法总结：未找到主要内容。

---

### [动画树形图 | Observable](https://observablehq.com/notebook-kit/ex/d3/animated-treemap)

**原文标题**: [Animated treemap | Observable](https://observablehq.com/notebook-kit/ex/d3/animated-treemap)

该内容描述了一个使用 D3.js 创建的动态树状图（treemap），用于展示美国人口数据随时间的变化。以下是关键点总结：

- 🌳 使用 D3.js 的`d3.treemapResquarify`布局来创建稳定的树状图，节点值会随时间变化。
- 📊 数据来源于美国人口普查局（U.S. Census Bureau），展示了不同州的人口分布。
- 🎨 通过颜色方案区分不同州，并调整颜色亮度以提高文本标签的可读性。
- 📏 树状图的大小会根据人口数据进行动态调整，确保每个州的比例在整个动画过程中保持一致。
- ⏱️ 提供了更新方法（update function），允许通过索引和时间参数来触发过渡动画。
- 🔍 包含了文本标签和提示框（tooltip），用于显示州名和具体人口数值。
- 📈 动画效果通过过渡（transition）实现，支持中断和恢复，确保平滑的视觉体验。
- 📂 数据通过 CSV 和 TSV 文件加载，并按地区和州进行分组处理。

---

### [过去十年中众多、众多、众多的 JavaScript 运行时 • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

**原文标题**: [The many, many, many JavaScript runtimes of the last decade • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

过去十年中，JavaScript 运行时和引擎的多样性显著增加，使其能够运行于各种场景，包括云端、边缘计算、智能电视、移动设备和微控制器等。以下是关键点的总结：

- 🌐 **边缘计算的兴起**：从 2016 年的 Lambda@Edge 和 Cloudflare Workers 开始，JavaScript 在边缘计算中的应用迅速扩展，随后出现了 Deno、Bun、WinterJS 和 LLRT 等运行时，各自采用不同的引擎（如 V8、JavaScriptCore、SpiderMonkey 和 QuickJS）。
- 💡 **微控制器的适配**：为了在资源有限的微控制器上运行 JavaScript，出现了 Duktape、Espruino、JerryScript 等轻量级引擎，能够在极低的内存（如 64KB 甚至 100 字节）下运行。
- 🔄 **多语言引擎的多样性**：JavaScript 引擎不仅限于 C++，还出现了基于 JVM 的 Rhino、Nashorn 和 Graal.js，以及支持.NET、Python、Ruby、Go、Rust 等多种语言的引擎，甚至有用 JavaScript 编写的引擎（如 Porffor）。
- 📱 **原生应用的发展**：JavaScript 在移动和桌面应用中的应用广泛，从早期的 PhoneGap/Cordova 到现代的 React Native 和 Electron，React Native 在移动应用中占据重要地位，而 Electron 在桌面应用中占主导。
- 📺 **智能电视的生态**：智能电视平台如 webOS、Tizen 和 Android TV 使用 JavaScript 运行时（如 Cordova 和 React Native）来支持跨平台应用开发。
- ⚙️ **Node.js 的扩展**：Node.js 被移植到移动设备（如 iOS 和 Android）并支持无 JIT 模式，但其在图形用户界面开发中的应用仍不如 Electron 和 React Native 广泛。
- 🏆 **多样化的运行时生态**：不同运行时和引擎针对不同的优化目标（如启动性能、运行时性能、包大小等），使得没有单一的“最佳”运行时，而是根据具体需求选择最适合的工具。

JavaScript 的生态系统和语言特性使其成为多平台开发的强大工具，未来仍将继续扩展和创新。

---

### [Node.js — Node.js v22.18.0（长期支持版）](https://nodejs.org/en/blog/release/v22.18.0)

**原文标题**: [Node.js — Node.js v22.18.0 (LTS)](https://nodejs.org/en/blog/release/v22.18.0)

Node.js v22.18.0 (LTS) 版本发布，包含多项新功能和改进。

- 🚀 **默认启用类型剥离** - 现在无需额外配置即可直接执行 TypeScript 文件，但仍有一些语法限制。可通过 `--no-experimental-strip-types` 禁用。
- 🔄 **ESM 改进** - 实现了 `import.meta.main`，用于检测当前模块是否为入口文件。
- 📂 **文件系统增强** - 改进了 `fs-events` 的异步迭代器处理，支持突发事件的正确处理。
- 🔒 **权限模型扩展** - 新增 `permission.has(addon)` 支持，并改进了权限模型的调试功能。
- 🛠️ **新 API 和标志** - 增加了 `fileURLToPathBuffer` API 和 `--watch-kill-signal` 标志，用于监视模式。
- 🧩 **Worker 线程改进** - 使 `Worker` 支持异步销毁。
- 🐛 **多项错误修复** - 包括内存泄漏修复、权限模型标志传播改进等。
- 📦 **依赖更新** - 升级了 npm 到 10.9.3，更新了 SQLite、simdjson 等依赖。
- 📜 **文档更新** - 添加了新的协作成员，更新了多个文档部分以反映最新变化。
- ⚙️ **构建和工具改进** - 包括 Python 3.14 兼容性更新和代码质量改进。

---

### [Node.js — Node.js v24.5.0（当前版本）](https://nodejs.org/en/blog/release/v24.5.0)

**原文标题**: [Node.js — Node.js v24.5.0 (Current)](https://nodejs.org/en/blog/release/v24.5.0)

Node.js v24.5.0（Current）版本发布，包含多项重要更新与改进。

- 🔒 升级至 OpenSSL 3.5.1，支持至 2030 年 4 月，与 Node.js 24 的 LTS 周期（至 2028 年 4 月）匹配。
- 🚀 取消`--experimental-wasm-modules`标志，正式支持 WebAssembly 模块的源阶段和实例阶段导入，遵循 ESM 集成提案。
- 🌐 `node:http`和`node:https`新增内置代理支持，可通过环境变量或`proxyEnv`选项配置全局代理。
- 📜 `node:tls`新增`setDefaultCACertificates()` API，支持动态配置默认 CA 证书。
- ⚡ 其他显著变更包括：DNS 支持最大超时、Worker 线程添加 Web Locks API、`net.blocklist`支持文件管理等。
- 🔧 多项修复与优化：修复 REPL 变量声明崩溃、改进 TLS 默认 CA 证书处理、更新核心依赖（如 npm 11.5.1、OpenSSL 3.0.17 补丁）等。
- 📦 提供全平台安装包与二进制文件下载（Windows/macOS/Linux/AIX 等），文档与 SHASUMS 校验文件同步更新。

---

### [我 2.5 年旧的笔记本电脑现在能用 GLM-4.5 Air 和 MLX 以 JavaScript 编写《太空侵略者》了](https://simonwillison.net/2025/Jul/29/space-invaders/)

**原文标题**: [My 2.5 year old laptop can write Space Invaders in JavaScript now, using GLM-4.5 Air and MLX](https://simonwillison.net/2025/Jul/29/space-invaders/)

Simon Willison 使用 GLM-4.5 Air 和 MLX 在 2.5 年前的笔记本电脑上成功运行了一个能编写 JavaScript 版《太空侵略者》的 AI 模型，展示了本地运行大型语言模型在编程任务上的强大能力。

- 🚀 **GLM-4.5 Air 模型**：由 Z.ai 开发的开源模型（MIT 许可证），参数规模达 1060 亿，基准测试显示其编码能力媲美 Claude Sonnet 4。  
- 💾 **量化版本**：Ivan Fioravanti 提供了 44GB 的 3bit 量化版本，适配 64GB 内存设备，使旧硬件也能运行。  
- 💻 **本地运行效果**：在 M2 MacBook Pro（64GB）上成功生成可直接运行的《太空侵略者》HTML/JavaScript 代码，无需修改。  
- ⚙️ **技术细节**：使用 `mlx-lm` 库加载模型，通过 Hugging Face 下载权重，峰值内存占用 48GB，生成速度达 25.564 token/秒。  
- 🎨 **其他测试**：模型还能生成“骑自行车的鹈鹕”SVG 图像，进一步验证其多模态能力。  
- 📈 **行业趋势**：2025 年发布的模型普遍强化编码能力，GLM-4.5、Mistral 3.2 Small 等模型表现突出，远超两年前的预期。  
- 🔗 **资源链接**：完整代码和交互示例已发布在 GitHub，用户可自行尝试。

---

### [太空侵略者](https://tools.simonwillison.net/space-invaders-GLM-4.5-Air-3bit)

**原文标题**: [Space Invaders](https://tools.simonwillison.net/space-invaders-GLM-4.5-Air-3bit)

游戏初始界面，包含基本操作和状态显示。  

- 👾 游戏名称：SPACE INVADERS（太空侵略者）  
- 🎮 初始分数：0  
- ❤️ 初始生命值：3  
- 🕹️ 操作方式：使用← →或 A/D 键移动，按空格键射击  
- 💀 结束提示：GAME OVER（游戏结束）  
- 📊 结算显示：Final Score（最终分数）  
- 🔄 重新开始选项：PLAY AGAIN（再玩一次）

---

### [npm 使用 OIDC 的信任发布现已全面可用 - GitHub 更新日志](https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/)

**原文标题**: [npm trusted publishing with OIDC is generally available - GitHub Changelog](https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/)

npm 可信发布功能正式推出，通过 OIDC 实现 CI/CD 工作流的安全发布，减少长期令牌管理需求。

- 🔒 无需 npm 令牌发布包：支持 GitHub Actions 和 GitLab CI/CD工作流通过OIDC认证发布。  
- 🛡️ 消除令牌安全风险：避免在 CI/CD 环境中存储或暴露长期令牌。  
- 🔗 建立加密信任：每次发布使用短期、工作流特定的凭证，不可复用或泄露。  
- 📜 自动生成来源证明：默认发布来源证明，无需`--provenance`标志。  
- 🌐 支持范围：所有 npm 公共和私有包（包括作用域和非作用域包），GitHub Actions 和 GitLab CI/CD。  
- ⚙️ 设置步骤：在 npmjs.com 配置可信发布者，更新工作流文件权限，无需生成写入令牌。  
- 🔄 自动来源证明：发布时自动生成来源证明，用户可验证包来源和构建环境。  
- 📚 详细文档：提供 GitHub Actions 和 GitLab CI/CD的详细设置指南。  
- 🚀 未来计划：扩展支持更多 CI/CD 提供商和自托管运行器。

---

### [2025 年 Stack Overflow 开发者调查](https://survey.stackoverflow.co/2025)

**原文标题**: [2025 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025)

Stack Overflow 2025 年开发者调查报告概述：覆盖全球 177 个国家、49,000+ 开发者，聚焦 AI 工具、LLMs 及社区平台的使用趋势与技术偏好。

- 🏆 开发者拒绝技术的三大主因：隐私安全问题（第 1 位）、定价过高（第 2 位）、存在更好替代品（第 3 位）  
- 🤖 69% 的 AI 工具使用者认为 AI 代理提升了效率，但仅 17% 认为其改善了团队协作  
- 📊 OpenAI GPT 模型使用率高达 81.4%，Claude Sonnet 成为最受推崇的 AI 模型（61.2%）  
- 🎓 36% 开发者去年为职业需求学习 AI 工具，45% 开发者编码经验不足 10 年  
- 🌐 美国（20.4%）、德国（8.6%）、印度（7.2%）为受访者最多国家  
- 💻 VS Code 连续四年蝉联最受欢迎开发环境（75.9%），Python 使用率同比增长 7%  
- 🏠 32% 开发者远程工作，美国远程比例最高（45%）  
- ⚠️ 66% 开发者对 AI 工具"近似正确但不精准"的输出表示沮丧  
- 📉 AI 工具正面评价从往年 70% 降至 60%，46% 开发者不信任其准确性  
- 🛠️ Rust 的 Cargo 包管理器获评最受推崇云开发工具（70.8%）  
- 📌 GitHub 超越 Jira 成为最理想协作工具，Markdown 连续三年最受推崇  
- 😊 开发者工作满意度从 20% 提升至 24%

---

### [技术 | 2025 年 Stack Overflow 开发者调查](https://survey.stackoverflow.co/2025/technology#1-programming-scripting-and-markup-languages)

**原文标题**: [Technology | 2025 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025/technology#1-programming-scripting-and-markup-languages)

Stack Overflow 2025 年度开发者调查报告摘要，涵盖技术趋势、工具偏好及开发者行为分析。

- 🐍 **Python 加速增长**：Python 采用率显著提升（+7%），成为 AI、数据科学和后端开发的首选语言。  
- 🏆 **最受欢迎技术**：JavaScript（66%）、HTML/CSS（61.9%）、SQL（58.6%）和 Python（57.9%）占据编程语言前列。  
- 🚀 **Rust 最受推崇**：连续多年成为开发者最喜爱的语言（72% 满意度），其次是 Gleam（70%）和 Elixir（66%）。  
- 🐳 **Docker 近普及**：使用率年增 17%，成为云开发的必备工具，Kubernetes 紧随其后（28.5%）。  
- 🏗️ **FastAPI 崛起**：Web 框架中增长最快（+5%），反映 Python 生态在高效 API 构建中的优势。  
- 💻 **VS Code 主导 IDE**：76% 开发者使用，同时是最受欢迎的代码编辑器，AI 增强工具如 Cursor 吸引关注。  
- 🗃️ **PostgreSQL 双冠王**：数据库中最受青睐且满意度最高，Redis 使用率增长 8%。  
- 🤖 **AI 工具渗透开发**：82% 开发者使用 OpenAI GPT 模型，Claude Sonnet 在专业开发者中更受欢迎（45%）。  
- 📊 **协作工具趋势**：GitHub（81%）和 Markdown（75.8% 满意度）主导，Obsidian 成为知识管理新宠。  
- 📱 **操作系统偏好**：Windows（工作 56.7%）和 MacOS（个人 32.7%）领先，Android 首次超越 Ubuntu（个人 29.1%）。  
- 🌐 **社区平台**：Stack Overflow 最常用（84.2%），学习编码者更依赖 YouTube（70% vs 开发者 60%）。  

关键洞察：开发者正积极拥抱 AI 工具（如 LLM）、高性能语言（Rust/Go）和容器化技术，同时 Python 生态持续扩张，开源协作工具需求旺盛。

---

### [技术 | 2025 年 Stack Overflow 开发者调查](https://survey.stackoverflow.co/2025/technology#1-web-frameworks-and-technologies)

**原文标题**: [Technology | 2025 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025/technology#1-web-frameworks-and-technologies)

Stack Overflow 2025 年度开发者调查报告摘要，涵盖技术趋势、工具偏好及开发者行为数据。

- 🐍 **Python 加速增长**：Python 采用率同比增长 7%，成为 AI、数据科学和后端开发的首选语言。
- 🏆 **最受欢迎技术**：JavaScript（66%）、HTML/CSS（61.9%）、SQL（58.6%）和 Python（57.9%）占据编程语言前四。
- 🚀 **Rust 最受推崇**：连续多年成为开发者最欣赏的语言（72% 满意度），新语言 Gleam 以 70% 满意度首次上榜。
- 🛢️ **数据库趋势**：PostgreSQL（55.6%）最受欢迎，Redis 使用率增长 8%，成为现代技术栈关键组件。
- 🐳 **Docker 近普及**：使用率一年激增 17%，71.1% 的开发者使用，成为云开发的准标准工具。
- ⚡ **FastAPI 崛起**：使用率增长 5%，反映 Python 在高效 API 开发中的优势。
- 💻 **开发工具霸主**：VS Code 以 75.9% 使用率连续五年居首，AI 增强型编辑器 Cursor（17.9%）和 Claude Code（9.7%）兴起。
- 🤖 **AI 工具渗透**：82% 开发者使用 OpenAI GPT 模型，Claude Sonnet 以 67.5% 满意度成为最受推崇 LLM。
- 🌐 **社区平台**：Stack Overflow（84.2%）和 GitHub（66.9%）主导，学习编码者更依赖 YouTube（70.1%）。
- 🔄 **技术迁移趋势**：Python 开发者倾向转向 Rust/Go；MongoDB 用户希望掌握 PostgreSQL；云平台用户普遍想学习 Docker。
- 📊 **方法论创新**：新增嵌入式工具和社区验证技术选项调查，通过"期望 vs.现实"可视化分析技术热度。

（注：数据基于 49,000+ 开发者样本，部分图表响应率在 30%-65% 之间）

---

### [Tailwind Plus 的 Vanilla JavaScript 支持 - Tailwind CSS](https://tailwindcss.com/blog/vanilla-js-support-for-tailwind-plus)

**原文标题**: [Vanilla JavaScript support for Tailwind Plus - Tailwind CSS](https://tailwindcss.com/blog/vanilla-js-support-for-tailwind-plus)

Tailwind Plus 的 UI 组件现在无需 JavaScript 框架即可直接使用交互功能，通过新推出的 @tailwindplus/elements 库实现跨框架兼容，支持原生 HTML 和现代 Web 特性。

- 🎯 **功能升级**：Tailwind Plus 所有 UI 组件（如下拉菜单、命令面板等）现支持纯 HTML 实现交互，无需依赖 React/Vue。  
- 🧩 **核心工具**：推出 `@tailwindplus/elements` 库，提供无头自定义元素（如 `<el-dropdown>`），封装复杂行为且可自由定制样式。  
- 🌐 **跨框架兼容**：通过 `<script>` 标签即可使用，示例代码展示在 Svelte、Rails 和 React 中的集成方式。  
- 🛠️ **丰富组件**：首版包含自动补全、对话框、选项卡等 8 种基础组件，支持无障碍和键盘操作。  
- ⚡ **现代技术**：基于 Custom Elements、`popover` 属性、`<dialog>` 等原生特性开发，内置 Polyfill 确保广泛兼容性。  
- 📚 **文档完善**：提供详细文档和示例，Tailwind Plus 用户可立即体验更新后的交互式组件。

---

### [pnpm 10.14 | pnpm](https://pnpm.io/blog/releases/10.14)

**原文标题**: [pnpm 10.14 | pnpm](https://pnpm.io/blog/releases/10.14)

pnpm 10.14 版本引入了 JavaScript 运行时自动安装支持，允许通过`devEngines.runtime`声明 Node.js、Deno 或 Bun 版本并自动下载锁定，同时修复了多个 bug 并新增了 CLI 功能。

- 🚀 新增`devEngines.runtime`配置，支持自动下载并锁定 Node.js/Deno/Bun 运行时版本  
- 🔒 运行时精确版本及校验和会存入锁文件，确保环境一致性  
- 🌐 支持多运行时（Node/Deno/Bun）及版本范围（优于旧版仅 Node 固定版本）  
- 🧩 允许工作区内不同项目使用不同运行时（类似`executionEnv.nodeVersion`）  
- ⚙️ 当前版本本地安装运行时，未来计划改为共享计算机位置  
- 🛠️ 新增 CLI 参数`--cpu`/`--libc`/`--os`自定义`supportedArchitectures` (#7510)  
- 🐞 修复`pnpm add`忽略`libc`配置下载不兼容包的问题 (#9750)  
- 🔄 改进`dlx`解析命令行标志的逻辑 (#9719)  
- 🗑️ 修正`pnpm install --prod`未移除提升的 dev 依赖问题 (#9782)  
- 📦 修复本地 tarball 内容变更后重链接虚拟存储的边界问题  
- ⏱️ 解决本地 tarball 含 peer 依赖时锁文件更新判断错误

---

### [版本 4.1 发布：Node-RED](https://nodered.org/blog/2025/07/29/version-4-1-released)

**原文标题**: [Version 4.1 released : Node-RED](https://nodered.org/blog/2025/07/29/version-4-1-released)

Node-RED 4.1 版本已发布，包含多项新功能和改进，同时邀请用户参与社区调查以帮助规划未来路线图。

- 🚀 **版本发布** - Node-RED 4.1 现已可供安装，升级前请阅读升级指南。
- 📝 **社区调查** - 邀请用户参与调查，帮助塑造 Node-RED 的未来发展。
- 🔔 **更新通知** - 新增匿名使用情况反馈功能，通知用户新版本和节点更新。
- 📚 **节点文档图标** - 节点编辑对话框中添加了文档信息图标，方便快速查看节点描述。
- 🔗 **流程依赖管理** - 导出流程时包含模块依赖信息，导入时提示需安装的模块。
- 🛠️ **调色板管理器更新** - 支持显示已弃用模块、按下载量排序节点、添加节点文档链接等。
- ⏳ **事件日志小部件** - 安装节点时显示进度小部件，方便跟踪安装状态。
- 🛑 **其他改进** - 包括忽略禁用节点的部署确认、新增触发节点按钮操作等。
- 🔄 **节点更新** - 多个核心节点功能改进和错误修复。
- 🌍 **社区参与** - 鼓励用户通过论坛、Slack 等渠道参与社区贡献和反馈。

---

### [宣布 Ionic 8.7 发布 - Ionic 博客](https://ionic.io/blog/announcing-ionic-8-7)

**原文标题**: [Announcing Ionic 8.7 - Ionic Blog](https://ionic.io/blog/announcing-ionic-8-7)

Ionic Framework 8.7 发布，带来了一系列新功能和改进，包括新的 Reorder 事件、CSS 工具类、Ionicons 更新以及 Angular 模态注入优化等，旨在提升开发效率和用户体验。

- 🔄 **新的 Reorder 事件**  
  新增 `ionReorderStart`、`ionReorderMove` 和 `ionReorderEnd` 事件，提供更精细的拖拽控制，支持自定义动画和实时反馈。`ionItemReorder` 已被弃用。

- 📅 **Datetime 组件新属性**  
  新增 `highlightedDates` 的 `border` 属性，增强高亮日期的视觉样式控制。

- 🎨 **新增 CSS 工具类**  
  引入响应式 `display` 和 `flex` 工具类，简化布局开发。弃用 `ion-hide-*` 和部分旧的 flex 类，推荐使用新类名。

- 📦 **文件大小影响**  
  新增工具类增加了 CSS 文件大小，但可通过移除不需要的导入来优化。

- ✨ **Ionicons v8 更新**  
  新增图标，优化 Safari 渲染和主题支持，提升性能和文档组织。

- ⚙️ **Angular 模态注入优化**  
  新增 `IonModalToken`，简化模态元素的程序化访问和事件监听，提升类型安全和测试便利性。

- 🌟 **社区贡献**  
  感谢实习生和社区开发者的贡献，包括文档更新和问题修复。

- 🚀 **未来计划**  
  正在开发 React Router v6+ 支持和模块化架构，提供更灵活的主题和功能定制。

---

### [发布 v9.1.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v9.1.0)

**原文标题**: [Release v9.1.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v9.1.0)

Storybook 9.1 版本发布，带来多项新功能和改进，包括增强的可访问性、简化测试流程以及更流畅的开发体验。

- 🚀 改进的升级命令，支持 monorepo 无缝升级  
- 🅰 Angular 修复：支持 Tailwind 4、缓存清除和无 zone 兼容  
- 🧪 新增`sb.mock` API 和自动模拟功能，简化测试流程  
- 🧪 测试状态通过 favicon 显示，提供快速视觉反馈  
- ⚛️ 简化 React Native 项目配置  
- 🔥 热更新时自动中止 play 函数，避免副作用  
- 🏗️ 改进 CSF 工厂 API，支持类型安全的故事定义  
- ♿️ 全面优化 Storybook UI 的可访问性（工具栏、侧边栏、移动端等）  
- 💯 数十项基于社区反馈的修复和改进  

部分更新亮点：  
- 📦 Angular 构建优化（TSup 打包）  
- 🛠️ Vite 构建器修复 IP 地址相关逻辑  
- 📱 移动端导航可访问性改进  
- 🎨 高对比度模式下视觉焦点指示器优化  
- 📊 新增自动化迁移错误统计功能  

贡献者：ghengeveld、kasperpeulen 等 15 位开发者。

---

### [宣布 TypeScript 5.9 候选版本 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/)

**原文标题**: [Announcing TypeScript 5.9 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/)

TypeScript 5.9 RC 发布，带来多项新功能和优化  

- 🚀 **发布候选版本**：TypeScript 5.9 RC 已发布，可通过 `npm install -D typescript@rc` 安装。  
- 🛠️ **精简的 `tsconfig.json`**：`tsc --init` 现在生成更简洁的配置文件，减少冗余注释并默认启用常用选项（如 `strict`、`jsx` 等）。  
- ⏳ **延迟模块加载**：支持 `import defer` 语法，延迟模块执行至首次访问命名空间属性，优化启动性能。  
- 📦 **Node.js 20 模块支持**：新增 `--module node20` 选项，稳定模拟 Node.js v20 的模块行为。  
- 📚 **DOM API 文档增强**：为 DOM API 添加基于 MDN 的摘要描述，提升开发体验。  
- 🔍 **可扩展悬停提示（预览）**：编辑器悬停工具提示支持展开/折叠类型详情，便于快速查看复杂类型。  
- 📏 **可配置悬停长度**：通过 `js/ts.hover.maximumLength` 设置调整悬停信息的最大显示长度。  
- ⚡ **性能优化**：缓存类型实例化以减少重复计算，优化文件存在性检查的逻辑，提升编译速度。  
- ⚠️ **行为变更**：`lib.d.ts` 调整导致 `ArrayBuffer` 不再作为某些 `TypedArray` 的父类型，可能引发类型错误（需更新 `@types/node`）。  
- 🔜 **后续计划**：TypeScript 5.9 正式版预计一周内发布，团队正专注于原生版本 TypeScript 7 的开发。

---

### [ESLint v9.32.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/07/eslint-v9.32.0-released/)

**原文标题**: [ESLint v9.32.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/07/eslint-v9.32.0-released/)

ESLint v9.32.0 是一个小版本升级，引入了新功能并修复了之前版本中的多个错误。

- 🆕 核心规则更新以支持显式资源管理功能，包括 `using` 和 `await using` 声明。
- 🔄 `curly` 规则现在允许 `using` 和 `await using` 作为块中的唯一语句。
- 🚫 `no-unused-vars` 规则将 `using` 和 `await using` 声明的变量视为已使用。
- 🏗 `prefer-destructuring` 规则不再要求对 `using` 和 `await using` 声明进行解构。
- ⏳ `require-await` 和 `no-await-in-loop` 规则现在识别 `await using` 作为 `await` 表达式。
- 🔧 更新了 TypeScript 访问器支持，包括 `accessor-pairs` 和 `grouped-accessor-pairs` 规则。
- 🐛 修复了多个错误，包括升级 `@eslint/js` 和重构报告功能。
- 📚 更新了文档，包括 README 的更新。
- 🛠 进行了多项内部改进和测试配置的调整。

---

### [发布 10.27.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/10.27.0)

**原文标题**: [Release 10.27.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/10.27.0)

overview summary  
Preact 是一个轻量级的 JavaScript 库，最新版本 10.27.0 发布，包含新特性、修复和改进，由多位贡献者共同完成。  

- 🚀 **新特性**：更新了`refcallback`类型以支持返回清理函数，并添加了调试辅助导出（#4860）。  
- 🛠️ **修复**：确保在 Suspense 边界抛出错误后重新渲染（#4856）。  
- 🔧 **维护**：更新了`replaceNode`弃用注释，并减少重复逻辑（#4844、#4814、#4821）。  
- 👥 **贡献者**：感谢 JoviDeCroock 和 rschristian 的贡献。  
- 🔄 **错误提示**：页面加载时出现错误，需重新加载。  
- ⭐ **项目数据**：37.8k 星标、2k 分叉、65 个议题、86 个拉取请求。

---

### [发布 20.1.4 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/20.1.4)

**原文标题**: [Release 20.1.4 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/20.1.4)

Angular 项目的最新版本 20.1.4 发布，包含多项更新和修复。

- 🚀 **版本发布**：Angular 20.1.4 于 7 月 31 日发布，包含 296 次提交至主分支。  
- 🔧 **编译器更新**：修复了双向绑定中的安全读取表达式问题（#62852）。  
- ⚙️ **核心改进**：更新了新信号 API 的符号（#62284）。  
- 🌐 **HTTP 模块**：添加了 fetch API 中缺失的 HTTP 选项（#62881），并改进了错误解析（#62765）。  
- 👍 **社区反应**：获得 5 个点赞、2 个庆祝、2 个爱心、3 个火箭和 1 个眼睛表情反应。

---

### [发布 v2.4.3 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.4.3)

**原文标题**: [Release v2.4.3 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.4.3)

Deno 2.4.3 版本发布，包含多项功能改进和错误修复。

- 🚀 **功能更新**：添加了隧道元数据支持（不稳定功能）。  
- 🛠 **错误修复**：修复了打包、检查、编译、Node 兼容性等多个问题。  
- 📦 **Node 改进**：优化了`fs.read`、`fs.write`的 Promise 兼容性，修复了 TLS 和 Zlib 相关功能。  
- 🔧 **工具链优化**：改进了任务递归执行、配置解析和锁文件处理。  
- ⚡ **性能提升**：优化了 Buffer 的`subarray`和`utf8Slice`性能。  
- 📜 **脚本支持**：支持`package.json`导入和 Deno 工作区配置。  
- 🐞 **问题修复**：解决了控制台日志、信号处理、覆盖率目录等潜在问题。

---

### [发布 19.1.1 版本（2025 年 7 月 28 日）· facebook/react · GitHub](https://github.com/facebook/react/releases/tag/v19.1.1)

**原文标题**: [Release 19.1.1 (July 28, 2025) · facebook/react · GitHub](https://github.com/facebook/react/releases/tag/v19.1.1)

React 项目在 GitHub 上的动态概览  

- 🚀 **版本发布**：React v19.1.1 于 2025 年 7 月 28 日发布，包含 530 次提交至主分支。  
- 🔧 **修复内容**：修复了 Owner Stacks 以兼容 ES2015 的 function.name 语义（由@hoxyq 提交）。  
- 🌟 **社区互动**：获得大量用户反应，包括 51 个点赞、37 个欢呼、23 个爱心、17 个火箭和 18 个围观表情。  
- 📊 **项目活跃度**：代码库拥有 238k 星标、49k 分叉，当前开放 806 个 Issues 和 206 个 Pull Requests。  
- ⚠️ **加载问题**：页面显示加载错误提示，需重新刷新。

---

### [Zod 对决 Valibot：JS/TS 验证器之战！- YouTube](https://www.youtube.com/watch?v=6P-2urhScwk)

**原文标题**: [Zod VS Valibot: JS/TS Validator Battle! - YouTube](https://www.youtube.com/watch?v=6P-2urhScwk)

关于 YouTube 的相关信息与链接  

- 📢 关于 - 提供 YouTube 平台的背景与介绍  
- 🗞️ 媒体 - 新闻稿与媒体资源  
- ©️ 版权 - 版权政策与保护措施  
- 📩 联系我们 - 用户与平台的联系渠道  
- 🎨 创作者 - 创作者相关资源与支持  
- 💼 广告 - 广告合作与推广信息  
- 👩💻 开发者 - 开发者工具与 API  
- 📜 条款 - 使用条款与条件  
- 🔒 隐私 - 隐私政策与数据保护  
- ⚖️ 政策与安全 - 社区准则与安全措施  
- 🔧 YouTube 运作方式 - 平台功能与机制解析  
- 🧪 测试新功能 - 体验最新推出的实验性功能  
- © 2025 Google LLC - 版权归属与年份声明

---

### [简介 | Zod](https://zod.dev/)

**原文标题**: [Intro | Zod](https://zod.dev/)

Zod 4 是一个 TypeScript 优先的验证库，用于定义和验证数据模式，支持从简单字符串到复杂嵌套对象的数据结构。  

- 🚀 **Zod 4 稳定版发布** - 最新版本现已稳定，提供更强大的功能和改进。  
- 📜 **TypeScript 优先** - 支持静态类型推断，确保数据验证和类型安全。  
- 🛠️ **丰富的功能** - 无外部依赖、体积小巧（2kb）、不可变 API、内置 JSON Schema 转换等。  
- 📦 **多平台支持** - 适用于 Node.js 和现代浏览器，支持多种包管理器安装（npm、yarn、bun 等）。  
- 🔄 **生态系统丰富** - 提供大量集成和工具，如 tRPC、React Hook Form 等。  
- ⚙️ **严格模式要求** - 需在 `tsconfig.json` 中启用 `strict` 模式以确保最佳兼容性。  
- 💰 **赞助支持** - 提供多种赞助层级，鼓励企业和开发者支持项目发展。  
- 📚 **详细文档** - 包含基础用法、错误处理、元数据管理等全面指南。

---

### [在脑海中编译 Svelte 5 | Tan Li Hau](https://lihautan.com/compile-svelte-5-in-your-head)

**原文标题**: [Compile Svelte 5 in your head | Tan Li Hau](https://lihautan.com/compile-svelte-5-in-your-head)

这篇文章深入探讨了 Svelte 5 的编译机制，从基础 DOM 操作到高级特性如信号和事件委托，逐步解析了 Svelte 如何将组件代码转换为高效的 JavaScript 输出。

- 🚀 **背景与介绍**：文章是为 Svelte 5 重写的，介绍了新特性如 runes 和细粒度响应性。
- 🛠️ **基础 DOM 操作**：创建元素、更新文本节点、移除元素、添加样式和事件监听器。
- 📜 **模板元素**：使用`<template>`元素克隆 DOM 结构，提高效率。
- 🔍 **高级 DOM 概念**：`nextSibling`和`firstChild`用于获取克隆元素的引用。
- 🎯 **事件委托**：在父元素上监听事件，提高性能并简化清理。
- 📝 **Svelte 语法**：介绍了基础语法、样式、响应式状态和事件处理。
- ⚡ **编译过程**：Svelte 将组件编译为函数，使用`from_html`生成模板克隆。
- 🔄 **响应式状态**：`$state`标记响应式变量，`$.set`和`$.get`用于更新和读取。
- 📊 **信号与效果**：`$.template_effect`跟踪信号变化并更新 DOM。
- 🖱️ **事件监听优化**：使用`__click`和`$.delegate`实现事件委托，减少重复注册。
- 🔗 **完整流程**：从初始化到事件触发，详细解析了 Svelte 的响应式更新机制。
- 📢 **总结与资源**：提供了进一步学习的资源和作者的相关演讲。

---

### [Svelte • 为大众而生的网页开发](https://svelte.dev/)

**原文标题**: [Svelte • Web development for the rest of us](https://svelte.dev/)

Svelte 是一个通过编译器让你能用熟悉的 HTML、CSS 和 JavaScript 编写极其简洁组件的 UI 框架，在浏览器中运行效率极高。  

- 🎨 **优雅简洁**：Svelte 以轻量、优雅和时尚著称，让开发者能编写高效的组件。  
- 🚀 **开发体验**：开发者普遍认为 Svelte 是最令人兴奋的前端框架之一。  
- 🌍 **广泛应用**：被多家知名公司采用，如 Vercel、Datawrapper 等。  
- 📽️ **背景故事**：可通过纪录片《Svelte Origins》深入了解其发展历程。  
- 🤝 **社区支持**：Svelte Society 组织全球活动，欢迎加入 Discord 社区交流。  
- 💡 **开源生态**：由全职和兼职维护者共同开发，得到 Vercel 及众多赞助商支持。  
- 📜 **开源协议**：采用 MIT 许可证，完全免费且开源。

---

### [选择正确的 SaaS 架构：多租户与单租户对比](https://clerk.com/blog/multi-tenant-vs-single-tenant?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=mt-st&utm_content=08-01-25&dub_id=pVJA52ewrNoJbkwZ)

**原文标题**: [Choosing the right SaaS architecture: Multi-Tenant vs. Single-Tenant](https://clerk.com/blog/multi-tenant-vs-single-tenant?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=mt-st&utm_content=08-01-25&dub_id=pVJA52ewrNoJbkwZ)

概述  
本文详细比较了多租户（Multi-Tenant）和单租户（Single-Tenant）SaaS 架构的优缺点、适用场景及选择建议，并介绍了现代工具如何简化租户隔离的实现。

- 🏢 **多租户架构**：共享应用和数据库实例，通过逻辑隔离服务多个客户。优势包括成本低、扩展性强、维护简单，但定制化能力有限，需严格设计租户隔离。  
- 🏠 **单租户架构**：每个客户拥有独立的应用和数据库实例。优势包括数据隔离性强、支持深度定制，但成本高、维护复杂，适合高安全需求或大型企业。  
- ⚖️ **核心差异**：多租户注重资源共享与效率，单租户侧重隔离与灵活性。关键权衡点包括成本、安全性、定制化、扩展性和维护复杂度。  
- 🔍 **选择建议**：  
  - 目标客户为中小企业或需要快速迭代？多租户更合适。  
  - 客户需求高度定制或受严格监管？考虑单租户或混合模式。  
  - 早期创业公司可优先选择多租户以降低成本。  
- 🛠️ **工具推荐**：  
  - **Clerk**：简化多租户身份验证与用户管理。  
  - **Supabase**：利用 PostgreSQL 的行级安全（RLS）实现数据隔离。  
  - **Prisma**：支持多数据库或动态租户过滤的 ORM 工具。  
  - **Neon**：通过数据库分支实现低成本单租户隔离。  
- 🔄 **混合策略**：结合两者优势，例如多租户核心 + 单租户选项，以满足不同客户需求。  
- 🚀 **结论**：没有绝对最优方案，需根据产品阶段、客户需求和资源选择架构，现代工具可帮助平衡安全性与效率。

---

### [JavaScript 中的逻辑赋值运算符：小语法，大收获 - Matt Smith](https://allthingssmitty.com/2025/07/28/logical-assignment-operators-in-javascript-small-syntax-big-wins/)

**原文标题**: [
    Logical assignment operators in JavaScript: small syntax, big wins - Matt Smith
  ](https://allthingssmitty.com/2025/07/28/logical-assignment-operators-in-javascript-small-syntax-big-wins/)

JavaScript 中的逻辑赋值运算符：简洁语法带来高效编码

- 🚀 逻辑赋值运算符是 ES2021 特性，结合逻辑运算符（||、&&、??）和赋值（=），简化条件赋值操作  
- ⚠️ 注意：可选链（?.）不能用于逻辑赋值左侧，会引发语法错误  
- 🔄 `||=`：当左侧为假值时赋值（包括 0、''、false 等），适合设置默认值但会覆盖有效假值  
- 🔍 `&&=`：当左侧为真值时赋值并更新为右侧表达式结果，适合条件更新  
- 🛡️ `??=`：仅当左侧为 null/undefined 时赋值，保留有效假值（0、false 等）  
- ⚡ 优势：减少样板代码，提升可读性，适用于组件 props、全局配置和状态管理  
- 🧩 应用场景：默认 props (`props.showHelpText ??= true`)、避免全局配置覆盖 (`config.apiBase ||= '/api/v1'`)  
- ⚠️ 注意事项：直接修改原对象，在不可变工作流（如 Redux）中需先克隆对象  
- 🌐 浏览器支持：Chrome 85+、Firefox 79+、Safari 14+，Node.js 15+，不支持 IE  
- 🔧 旧环境兼容：使用 Babel 的`@babel/preset-env`并配置 ES2021

---

### [理解性能扩展性 API——CSS 魔法](https://csswizardry.com/2025/07/the-extensibility-api/)

**原文标题**: [Making Sense of the Performance Extensibility API – CSS Wizardry](https://csswizardry.com/2025/07/the-extensibility-api/)

Harry Roberts 是一位独立的网络性能工程师顾问，帮助各种规模的公司发现并解决网站速度问题。

- 👨💻 Harry Roberts 是一位独立的网络性能工程师顾问  
- 🏢 他为各种规模的公司提供服务  
- ⚡ 专注于发现和解决网站速度问题

---

### [错误](https://javascriptweekly.com/link/172605/web)

**原文标题**: [Error](https://javascriptweekly.com/link/172605/web)

无法总结：获取内容时出错 - Response ended prematurely

---

### [多仓库 TypeScript 问题](https://www.carrick.tools/blog/the-multi-repository-typescript-problem)

**原文标题**: [The Multi-Repository TypeScript Problem](https://www.carrick.tools/blog/the-multi-repository-typescript-problem)

大型 TypeScript 代码库在分布式团队中常采用 monorepo 或 polyrepo 架构，monorepo 在类型共享方面优势显著，而 polyrepo 则面临跨服务类型安全的挑战。以下是关键点总结：

- 🏗️ **架构选择**：monorepo 便于共享 TypeScript 包和类型，而 polyrepo 因独立仓库导致类型同步复杂  
- 🔍 **类型提取难题**：跨仓库类型比较需递归解析依赖（如 Express 的 Response 含 47+ 属性），遭遇命名冲突和循环引用  
- 🛠️ **工具链方案**：使用 ts-morph 库解析类型 AST，智能分离本地类型（递归提取）与外部依赖（保留 import）  
- 📦 **便携式类型包**：CI 流程生成含类型定义和依赖清单的 npm 包（如`user-service-types`），上传至共享存储  
- 🔗 **生产者 - 消费者关联**：通过 API 路由生成唯一类型别名（如`GetApiUsersResponseProducer`），避免命名冲突  
- ✅ **类型验证机制**：临时 TS 项目合并多仓库类型包，直接利用 TS 编译器检查类型兼容性，输出原生错误提示  
- ⚡ **工程实践洞见**：突破 TS 项目边界需深度处理符号解析，性能优化关键（如减少 CI 编译文件量）  
- 🤖 **未来方向**：通过 AI 分析部署代码保持微服务类型对齐，实现 polyrepo 下 monorepo 级类型安全  

（注：原文中的功能导航条目如"AI in CI"等未纳入技术摘要）

---

### [`vi.mock` 是把双刃剑：为何默认应选用 `vi.spyOn`](https://laconicwit.com/vi-mock-is-a-footgun-why-vi-spyon-should-be-your-default/)

**原文标题**: [`vi.mock` Is a Footgun: Why `vi.spyOn` Should Be Your Default](https://laconicwit.com/vi-mock-is-a-footgun-why-vi-spyon-should-be-your-default/)

文章讨论了在测试中使用 `vi.mock` 的潜在问题，并推荐使用 `vi.spyOn` 作为更优选择。

- 🚨 `vi.mock` 是一个全局性的操作，会影响整个测试文件中的所有测试，可能导致不可预测的行为和难以维护的代码。  
- 🏎️ `vi.spyOn` 在运行时执行，仅针对特定方法进行模拟，更加精确和可控。  
- 🔄 `vi.mock` 会替换整个模块，包括那些你可能希望保持原样的部分，而 `vi.spyOn` 仅覆盖指定的方法。  
- 🛠️ `vi.spyOn` 提供更好的类型安全性，TypeScript 能够正确推断类型，减少错误。  
- 🚩 使用 `vi.mock` 结合 `vi.requireActual` 是一种反模式，代码复杂且容易出错，而 `vi.spyOn` 更简洁安全。  
- 🧩 在闭包和高阶函数中，`vi.spyOn` 可能无法覆盖所有情况，但可以通过调整代码结构来解决。  
- ✅ 最佳实践包括在每个测试后恢复模拟、使用命名空间导入模块，并将模拟操作放在测试附近以提高可读性。  
- ⚠️ `vi.mock` 适用于需要完全禁用某些依赖（如日志库或分析工具）的场景，但不适合用于控制具体行为的情况。  
- 🎯 结论是 `vi.spyOn` 应作为默认选择，提供更好的类型安全、测试隔离和可维护性。

---

### [如何使用 Matter.js 和 React Native Skia 构建 2D 游戏风格物理效果](https://expo.dev/blog/build-2d-game-style-physics-with-matter-js-and-react-native-skia)

**原文标题**: [How to build 2D game-style physics with Matter.js and React Native Skia](https://expo.dev/blog/build-2d-game-style-physics-with-matter-js-and-react-native-skia)

Expo 相关资源与服务导航  

- 📝 **博客与文档** - 提供博客文章和详细文档资源  
- 🛠️ **产品与服务** - 包括 EAS（Expo 应用服务）、Expo Go、Snack 等开发工具  
- 💰 **定价信息** - 查看产品定价和客户案例  
- 🌟 **社区支持** - GitHub Star 支持、Discord 社区加入  
- 🔧 **开发资源** - Expo CLI、EAS CLI、Orbit 等工具链接  
- 📢 **更新与新闻** - 变更日志、新闻订阅和信任中心  
- 🏢 **公司信息** - 关于 Expo、招聘、品牌和法律条款  
- ⚖️ **法律与合规** - 服务条款、隐私政策、安全合规说明  
- ©️ **版权声明** - 650 Industries, Inc. 版权所有

---

### [GitHub - sverweij/dependency-cruiser: 依赖关系验证与可视化。自定义规则。支持 JavaScript、TypeScript、CoffeeScript，以及 ES6、CommonJS、AMD 模块。](https://github.com/sverweij/dependency-cruiser)

**原文标题**: [GitHub - sverweij/dependency-cruiser: Validate and visualize dependencies. Your rules. JavaScript, TypeScript, CoffeeScript. ES6, CommonJS, AMD.](https://github.com/sverweij/dependency-cruiser)

Dependency-cruiser 是一个用于验证和可视化 JavaScript、TypeScript、CoffeeScript 等项目中依赖关系的工具，支持 ES6、CommonJS 和 AMD 模块系统。

- 🛠️ **功能**：验证依赖关系、可视化依赖图、支持自定义规则检测循环依赖等问题。  
- 📦 **安装**：可通过 npm、yarn 或 pnpm 安装，支持生成配置文件。  
- 📊 **可视化**：支持生成多种格式的依赖图（如 SVG、mermaid、JSON 等）。  
- ⚙️ **规则配置**：提供默认规则（如检测循环依赖），并支持自定义规则。  
- 📝 **报告**：支持多种报告格式（文本、图形、HTML 等）。  
- 🌍 **多语言支持**：支持 TypeScript、CoffeeScript、JSX、TSX、Vue 等。  
- 📜 **许可证**：MIT 开源协议。  
- 🤝 **社区**：拥有活跃的开源社区支持，定期更新和维护。  
- 🔗 **资源**：提供详细文档、命令行参考和 API 说明。

---

### [dependency-cruiser/doc/real-world-samples.md 位于 main · sverweij/dependency-cruiser · GitHub](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples.md)

**原文标题**: [dependency-cruiser/doc/real-world-samples.md at main · sverweij/dependency-cruiser · GitHub](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples.md)

该项目是 sverweij/dependency-cruiser，一个用于分析和可视化项目依赖关系的工具。

- 🔍 **功能** - 用于分析和可视化项目中的依赖关系。  
- 🌟 **受欢迎程度** - 获得 5.9k 星标，显示出较高的社区关注度。  
- 🛠 **开发活跃度** - 有 32 个未解决的问题和 1 个拉取请求，表明项目仍在积极维护中。  
- 📂 **结构** - 包含代码、问题、拉取请求、操作、项目和模型等多个模块。  
- ⚠ **错误提示** - 页面加载时出现错误，可能需要重新加载。  
- 🔒 **安全性** - 提供安全相关的功能或检查。

---

### [停止重复渲染 — TanStack DB，专为 TanStack Query 设计的嵌入式客户端数据库 | TanStack 博客](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query)

**原文标题**: [Stop Re-Rendering — TanStack DB, the Embedded Client Database for TanStack Query | TanStack Blog](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query)

TanStack DB 是一个客户端数据库层，旨在解决 React 应用中因数据更新导致的性能问题。它通过差异数据流技术，仅更新发生变化的部分，从而显著提升应用性能。

- 🚀 **性能优化**：TanStack DB 使用差异数据流技术，仅更新变化的数据，例如在 M1 Pro 上更新 100k 条数据中的一行仅需 0.7 毫秒。
- 🔄 **实时查询**：支持实时查询，仅流式传输变化的行，响应时间小于 1 毫秒。
- ⚡ **简化架构**：TanStack DB 提供了一种简化的架构，无需重写后端代码，即可实现快速的数据更新和查询。
- 🔧 **增量采用**：可以逐步采用 TanStack DB，从一个集合开始，逐步扩展到整个应用。
- 🔄 **乐观更新**：支持自动乐观更新和错误回滚，无需复杂的自定义状态管理。
- 📊 **大规模查询性能**：即使数据集包含数千条记录，也能保持亚毫秒级的查询性能。
- 🔌 **后端灵活性**：支持多种数据源，包括 REST、GraphQL、WebSocket 等，并可自定义集合。
- 🤝 **与 TanStack Query 集成**：TanStack DB 与 TanStack Query 无缝集成，前者负责数据的一致性，后者负责数据的获取。
- 🛠 **简化代码**：相比传统的 TanStack Query，TanStack DB 减少了大量样板代码，提升了开发效率。
- 🌐 **同步引擎支持**：特别适合与同步引擎（如 Electric、Firebase 等）配合使用，实现实时数据同步和高效的数据加载策略。

TanStack DB 的目标是为团队提供一个更高效、更灵活的方式来处理客户端数据，同时保持与现有后端技术的兼容性。

---

### [Embrace 用户旅程平台功能详解](https://embrace.io/blog/user-journeys-walkthrough/?utm_source=newsletter&utm_medium=paid&utm_campaign=javascript-weekly-8-1-2025&utm_content=user-journeys)

**原文标题**: [A walk-through of Embrace's User Journeys platform capability](https://embrace.io/blog/user-journeys-walkthrough/?utm_source=newsletter&utm_medium=paid&utm_campaign=javascript-weekly-8-1-2025&utm_content=user-journeys)

用户旅程功能将产品分析与可观察性结合，帮助工程师通过自定义流程分析技术性能对用户参与的影响。

- 🌉 连接产品分析和可观察性，填补两者之间的鸿沟  
- 🔧 工程师可自定义用户流程，深入分析技术性能  
- 📊 利用强大且精细的工具，评估用户参与度  
- 🚀 提升对技术性能如何影响用户体验的理解  
- ⏱️ 发布于 2025 年 7 月 22 日，阅读时长约 4 分钟

---

### [AudioTee.js：Node.js 的 macOS 系统音频捕获工具](https://stronglytyped.uk/articles/audioteejs-macos-system-audio-capture-nodejs)

**原文标题**: [AudioTee.js: macOS system audio capture for Node.js](https://stronglytyped.uk/articles/audioteejs-macos-system-audio-capture-nodejs)

AudioTee.js 是一个用于在 Node.js 中捕获 macOS 系统音频的开源库，通过 EventEmitter 接口流式传输 PCM 编码的音频数据。

- 🎧 **AudioTee.js 简介**  
  - 开源 Node.js 库，基于 AudioTee Swift 二进制文件构建，适用于 macOS 系统音频捕获。  
  - 通过子进程调用 Swift 二进制文件，简化实现并保持轻量（<600KB）。  

- 📦 **设计特点**  
  - 提供 Node.js 友好的 API，支持 PCM 音频流分块（`chunkDuration` 控制时长）。  
  - 强制单声道输出（`channels=1`），16 位采样（`bytesPerSample=2`）。  

- ⚙️ **配置选项**  
  - `sampleRate`：目标采样率（如 16000Hz）。  
  - `chunkDuration`：音频块时长（秒）。  
  - `mute`：是否静音系统音频。  
  - `includeProcesses/excludeProcesses`：按进程 ID 过滤音频源。  

- ⚠️ **当前限制**  
  - 仅支持 macOS 14.2+，默认输出设备捕获。  
  - 强制单声道，API 处于 0.x.x 阶段可能变动。  

- 🔮 **未来计划**  
  - 根据开发者反馈优化 API，鼓励用户提交 Issue 或 PR。  
  - 关联项目：原版 [AudioTee](https://github.com/...) 及 [macOS 音频捕获文章](...)。  

- 🌟 **社区互动**  
  - 欢迎分享用例或反馈，支持通过 [Bluesky](...) 等平台传播。

---

### [GitHub - makeusabrew/audioteejs：基于 Audiotee 的 NodeJS 封装库](https://github.com/makeusabrew/audioteejs)

**原文标题**: [GitHub - makeusabrew/audioteejs: A NodeJS wrapper library around Audiotee](https://github.com/makeusabrew/audioteejs)

NodeJS 封装的 Audiotee 库，用于捕获 Mac 系统音频输出并转换为 PCM 数据流。

- 🎧 **功能概述**：基于 Swift 二进制文件`AudioTee`，通过 NodeJS 封装实现捕获 Mac 系统音频输出，并以 PCM 格式分块发射。  
- 📦 **安装方式**：通过`npm install audiotee`安装，自动下载预构建的通用 MacOS 二进制文件（小于 600KB）。  
- ⚙️ **配置选项**：支持设置采样率（如 16000Hz）、分块时长（默认 0.2 秒）、静音系统音频、包含/排除特定进程 ID 等。  
- 🔊 **事件监听**：提供`data`（音频数据）、`start/stop`（生命周期）、`error`（错误）及`log`（系统日志）事件。  
- 🐞 **当前限制**：0.0.2 版本前仅`data`事件有效，其他生命周期事件暂不可用。  
- 🖥️ **系统要求**：仅支持 MacOS 14.2 及以上版本。  
- 📜 **许可证**：采用 MIT 协议，版权归 Nick Payne 所有。  
- ⚠️ **API 稳定性**：0.x.x 版本期间 API 可能不兼容变更。  
- 💡 **最佳实践**：建议明确指定采样率以优化性能，并根据使用场景调整分块时长。

---

### [发布 6.0.0-rc.0 版 · TryGhost/Ghost · GitHub](https://github.com/TryGhost/Ghost/releases/tag/v6.0.0-rc.0)

**原文标题**: [Release 6.0.0-rc.0 · TryGhost/Ghost · GitHub](https://github.com/TryGhost/Ghost/releases/tag/v6.0.0-rc.0)

Ghost 项目发布了 v6.0.0-rc.0 版本，包含多项功能更新和问题修复。  

- ✨ 新增原生 Web Analytics 支持（Tinybird 集成）和 ActivityPub 联邦功能（社交网络互联）  
- 🔒 增强安全性：防止域名仿冒攻击（punycode 域名）  
- 🎨 优化所有者用户创建逻辑（使用 ObjectID）  
- 🐛 修复主题资源 404 渲染问题  
- 🔥 移除多项废弃功能：无扩展名的主题文件服务、mobiledoc 字段、AMP 支持、Node.js v18/v20兼容性等  
- 🔥 API 限制调整：强制{{#get}}辅助函数和 API 请求的 limit 上限为 100  
- 📜 完整更新日志可查看版本对比：v5.130.2...v6.0.0-rc.0  
- 🎉 社区反响热烈，7 位用户给予庆祝表情反馈

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的命令行应用开发工具，允许开发者使用 React 组件模型构建交互式 CLI 应用。

- 🌈 **React for CLIs**：Ink 提供了与浏览器中相同的基于组件的 UI 构建体验，但适用于命令行应用。
- 📦 **Flexbox 布局**：使用 Yoga 构建终端中的 Flexbox 布局，支持大多数类似 CSS 的 props。
- 🛠 **React 特性支持**：作为 React 渲染器，Ink 支持所有 React 特性。
- 🚀 **快速开始**：可以使用 `create-ink-app` 快速搭建新的 Ink 项目。
- 📝 **组件支持**：提供 `<Text>`, `<Box>`, `<Newline>`, `<Spacer>`, `<Static>`, `<Transform>` 等组件。
- 🎮 **钩子支持**：提供 `useInput`, `useApp`, `useStdin`, `useStdout`, `useStderr`, `useFocus`, `useFocusManager` 等钩子。
- 📊 **测试支持**：可以使用 `ink-testing-library` 进行组件测试。
- 🔧 **React Devtools 支持**：支持使用 React Devtools 进行调试。
- 📚 **丰富的示例**：包含计数器、表单验证、表格、焦点管理等示例。
- 🏆 **知名用户**：包括 Codex、Claude Code、Gemini CLI、GitHub Copilot for CLI、Gatsby 等。

---

### [GitHub - vadimdemedes/ink: 🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink?tab=readme-ov-file#whos-using-ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink?tab=readme-ov-file#whos-using-ink)

Ink 是一个基于 React 的命令行界面（CLI）应用开发框架，允许开发者使用 React 组件构建交互式命令行应用。它支持 Flexbox 布局，并提供了丰富的组件和钩子来管理用户输入、输出和焦点控制。

- 🌈 Ink 是一个用于构建交互式命令行应用的 React 渲染器。
- 📦 支持 Flexbox 布局，使用 Yoga 引擎实现类似 CSS 的布局属性。
- 🛠 提供多种内置组件，如 `<Text>`、`<Box>`、`<Newline>`、`<Spacer>` 等。
- 🎮 支持用户输入处理，通过 `useInput` 钩子监听键盘事件。
- 📊 提供静态输出组件 `<Static>`，用于渲染不会变化的输出内容。
- 🔍 支持测试，可以使用 `ink-testing-library` 进行组件测试。
- 🔧 提供多种实用组件和钩子，如 `ink-text-input`、`ink-spinner` 等。
- 📝 支持 React Devtools，方便调试和开发。
- 🚀 被多个知名项目使用，如 Gatsby、Prisma、Shopify CLI 等。

---

### [Cytoscape.js](https://js.cytoscape.org/)

**原文标题**: [Cytoscape.js](https://js.cytoscape.org/)

总结失败：Error code: 400 - {'error': {'message': "This model's maximum context length is 65536 tokens. However, you requested 81416 tokens (73416 in the messages, 8000 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

### [GitHub - vuejs/eslint-plugin-vue: Vue.js 官方 ESLint 插件](https://github.com/vuejs/eslint-plugin-vue)

**原文标题**: [GitHub - vuejs/eslint-plugin-vue: Official ESLint plugin for Vue.js](https://github.com/vuejs/eslint-plugin-vue)

Vue.js 官方 ESLint 插件，用于 Vue.js 项目的代码规范和静态分析。

- 🚀 **官方插件** - 由 Vue.js 团队维护的 ESLint 插件，专为 Vue.js 项目设计。  
- 📖 **文档完善** - 详细文档请参考[官方网站](eslint.vuejs.org/)。  
- ⚖️ **版本策略** - 遵循语义化版本控制（SemVer），但可能在小版本中更改默认规则行为以添加新功能。  
- 🔄 **更新建议** - 推荐在`package.json`中使用`~`锁定小版本以避免意外构建错误。  
- 🛠 **贡献指南** - 欢迎贡献，开发新规则前需阅读[ESLint 指南](https://eslint.org/docs/developer-guide/)和[Vue 插件开发指南](https://eslint.vuejs.org/developer-guide/)。  
- 🌳 **AST 支持** - 使用[vue-eslint-parser](https://github.com/vuejs/vue-eslint-parser)解析 Vue 单文件组件，提供增强的 AST 节点。  
- 🔍 **规则测试** - 测试时需根据代码样本设置`RuleTester`的解析器属性。  
- 📜 **许可证** - 采用 MIT 许可证，详情见[LICENSE 文件](https://github.com/vuejs/eslint-plugin-vue/blob/master/LICENSE)。  
- 🌟 **社区活跃** - 4.6k 星标、690 分叉，232 名贡献者，被 190 万 + 项目使用。  
- 📦 **技术栈** - 主要使用 JavaScript（98.5%），辅以 TypeScript（1.5%）。

---

### [介绍 | eslint-plugin-vue](https://eslint.vuejs.org/)

**原文标题**: [Introduction | eslint-plugin-vue](https://eslint.vuejs.org/)

Vue.js 的官方 ESLint 插件，用于检查.vue 文件中的模板和脚本部分，以及.js 文件中的 Vue 代码，帮助发现语法错误、指令使用错误及违反 Vue.js 风格指南的问题。

- 🛠️ 官方 ESLint 插件，支持检查.vue 文件的<template>和<script>部分以及.js 文件中的 Vue 代码  
- 🔍 检测语法错误和 Vue.js 指令的错误使用  
- 📖 检查代码是否符合 Vue.js 风格指南  
- 🚥 遵循语义化版本控制，但可能与 ESLint 的版本策略不同  
- ⚠️ 次要版本更新可能引入更多 linting 错误，建议在 package.json 中使用波浪号 (~) 锁定版本  
- 📰 更新日志通过 GitHub Releases 发布  
- 🔒 采用 MIT 许可证

---

### [发布版本 v1.11.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.11.0)

**原文标题**: [Release Release v1.11.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.11.0)

axios GitHub 仓库的 v1.11.0 版本发布，包含错误修复和类型改进，获得社区积极反馈。

- 🐛 **Bug 修复**：修复了 form-data npm 包的问题（#6970）和大型 Buffer 导致的 RangeError（#6961）。  
- 📦 **类型修正**：解决了 ESM 与 CJS TypeScript 声明文件的类型差异（#6956）。  
- 👥 **贡献者**：感谢 izzy goldman、Manish Sahani 等开发者的贡献。  
- 🎉 **社区反应**：获得 21 个👍、5 个🎉、4 个❤️等积极反馈。  
- 🚀 **发布信息**：版本 v1.11.0 于 7 月 23 日发布，包含 6 次提交。

---

### [发布 v7.7.0 · inversify/InversifyJS · GitHub](https://github.com/inversify/InversifyJS/releases/tag/v7.7.0)

**原文标题**: [Release v7.7.0 · inversify/InversifyJS · GitHub](https://github.com/inversify/InversifyJS/releases/tag/v7.7.0)

InversifyJS 是一个轻量且强大的控制反转（IoC）容器，适用于 JavaScript 和 Node.js 应用，最新版本 v7.7.0 带来多项功能更新和优化。

- 🆕 **新增类型**：添加了`Bind`、`IsBound`、`OnActivation`、`OnDeactivation`、`Rebind`、`RebindSync`、`Unbind`和`UnbindSync`等类型。  
- 🔄 **功能调整**：更新了`BindOnFluentSyntaxImplementation.onDeactivation`，使其在非单例作用域绑定时抛出错误。  
- 🛠 **修复优化**：改进了`ServiceResolutionManager`的`getChained`操作，确保在计算属性重置后正常工作；优化了`Container`以更好地管理子容器在父容器恢复快照后的绑定。  
- 🏷 **版本发布**：v7.7.0 由 notaphplover 于 7 月 31 日发布，包含 2 次提交至 master 分支。  
- 🔒 **安全验证**：发布提交使用 GPG 密钥签名（ID: `B5690EEEBB952194`），支持 GitHub 的验证模式。

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=august1st2025)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=august1st2025)

Meticulous AI 提供了一种无需编写和维护测试的全新解决方案，通过记录用户交互自动生成覆盖所有边缘情况的测试套件，帮助团队快速交付无回归的可靠代码。

- 🚀 **无需编写测试** - Meticulous AI 自动生成并维护测试套件，覆盖应用程序的所有边缘情况，无需手动编写或修复测试。  
- 🔍 **记录用户交互** - 通过在开发、预演和生产环境中添加脚本标签，记录用户会话以生成测试用例。  
- 🤖 **AI 驱动测试** - AI 引擎根据代码分支和用户交互生成视觉端到端测试，确保覆盖每一行代码和用户流程。  
- ⚡ **快速集成** - 轻松与现有 CI 集成，无需设置特殊测试账户或模拟数据，测试无副作用且无假阳性。  
- 🛠️ **持续演进** - 测试套件随应用程序的更新自动调整，新增功能或边缘情况会自动纳入测试范围，旧测试则自动淘汰。  
- 🚫 **无 flakes** - 基于 Chromium 的确定性调度引擎，彻底消除测试中的不稳定因素，执行速度极快。  
- 📈 **高效并行测试** - 支持大规模并行测试，可在 120 秒内完成数千个屏幕的测试。  
- 💡 **客户认可** - 已被 Dropbox、Notion、Lattice 等 100 多家组织采用，显著提升开发效率和代码质量。  
- 🔗 **多框架支持** - 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流前端框架，集成简单。  
- 🔒 **安全可靠** - 提供完善的文档和安全保障，适合复杂应用程序的测试需求。

---

### [KeyLines - JavaScript 开发者的图形可视化 SDK](https://cambridge-intelligence.com/keylines/?utm_campaign=16812718-React%20Status%20newsletter%20ad&utm_source=NewsletterAd&utm_medium=SponsoredLink)

**原文标题**: [
		KeyLines - The Graph Visualization SDK for JavaScript Developers	](https://cambridge-intelligence.com/keylines/?utm_campaign=16812718-React%20Status%20newsletter%20ad&utm_source=NewsletterAd&utm_medium=SponsoredLink)

KeyLines 是一款专为 JavaScript 开发者设计的图可视化工具包，帮助用户快速构建高性能、可扩展且交互性强的图可视化应用。

- 🚀 **快速开发**：KeyLines 提供快速构建强大、美观且交互性强的可视化工具的能力，适应各种技术栈。  
- 📊 **高性能引擎**：基于 HTML5 和 WebGL 渲染技术，确保流畅的可视化体验。  
- 🌍 **跨平台兼容**：支持任何浏览器、设备和服务器，轻松集成到现有工具中。  
- 🔍 **高级功能**：包括时间序列分析、地理空间分析、社交网络分析和自动布局等。  
- 🤝 **全面支持**：提供从入门指导到深度技术支持的全程服务，帮助开发者快速上手。  
- 📂 **丰富资源**：包含教程、演示和详细的 API 文档，便于开发者学习和使用。  
- 🌐 **广泛应用**：客户遍布全球，涵盖初创企业、财富 500 强公司和政府机构。  
- 📰 **持续更新**：博客提供最新功能更新和用户体验优化建议。  
- 🆓 **免费试用**：支持申请免费试用，体验其强大功能。

---

### [GitHub - googlefonts/googlesans-code: Google Sans Code 字体家族](https://github.com/googlefonts/googlesans-code)

**原文标题**: [GitHub - googlefonts/googlesans-code: The Google Sans Code font family](https://github.com/googlefonts/googlesans-code)

Google Sans Code 是一个专为代码设计的等宽字体家族，源自 Google 的品牌字体设计风格，旨在提升代码编辑器和终端中的可读性和清晰度。

- 🎨 **字体特点**：专为编程语言语法优化，支持拉丁语扩展，提供 300 至 800 的可变字重。
- 📥 **安装方式**：下载最新可变字体版本，包含常规体和斜体两种样式。
- 🛠 **构建步骤**：使用 `fontc` 编译器从源码编译生成 TTF 格式的可变字体文件。
- 🔄 **持续集成**：每次推送到 `main` 分支或拉取请求时，自动编译并测试字体质量。
- 🤝 **贡献指南**：通过 GitHub 问题跟踪器提交问题，遵循项目贡献指南。
- 📜 **许可证**：采用 SIL Open Font License 1.1 许可证，版权归 Google LLC 等作者所有。
- 💡 **纪念**：项目纪念 Chris Simpkins，他对项目的热情和努力为项目奠定了基础。

---

### [Google Sans Code - Google 字体](https://fonts.google.com/specimen/Google+Sans+Code)

**原文标题**: [Google Sans Code - Google Fonts](https://fonts.google.com/specimen/Google+Sans+Code)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结  

- 📌 要点一  
- 🔍 要点二  
- 💡 要点三  

请提供具体内容，我会为您整理！

---

### [NPKILL - 保持开发工作区整洁](https://npkill.js.org/)

**原文标题**: [NPKILL - Maintain your development workspace clean.](https://npkill.js.org/)

Npkill 是一个 CLI 工具，用于查找并删除计算机中分散的 node_modules 文件夹，帮助用户轻松释放磁盘空间。

- 🚀 **快速高效**：Npkill 以分布式方式深度扫描磁盘，充分利用 CPU 和磁盘性能，快速定位 node_modules 或其他指定目录。  
- 😎 **简单易用**：通过直观的命令行界面，用户可轻松导航并删除不需要的文件夹，操作仅需几个按键。  
- ⚠️ **安全提示**：自动标记系统关键目录（如 Spotify/Discord 的 node_modules），避免误删导致应用崩溃。  
- 🛠️ **灵活选项**：支持自定义扫描路径、排序方式、排除目录、显示单位（GB/MB）等，满足多样化需求。  
- 💾 **空间释放**：用户反馈显示，工具可一次性清理数百 GB 冗余空间，尤其适合长期未维护的旧项目。  
- 📜 **操作指南**：  
  - 运行 `npx npkill` 启动扫描；  
  - 使用方向键导航，按 `Del` 删除选中项；  
  - 快捷键支持翻页（PgUp/PgDown）、跳转首尾（Home/End）等。  
- ❤️ **社区支持**：开源项目，由团队及贡献者维护，接受财务赞助，用户评价极高。  

（示例反馈：用户 @Jess 通过工具清理 100GB+；@Mehdi 节省 200GB 空间。）

---

### [npkill 的未来：超越 node_modules](https://imzaldih.com/en/post/npkill-future-beyond-node-modules/)

**原文标题**: [The Future of npkill: Beyond node_modules](https://imzaldih.com/en/post/npkill-future-beyond-node-modules/)

npkill v1.0 即将发布，核心将作为公共 API 开放，可能带来重大变革，包括推出网页版工具。项目创始人考虑扩展其功能，使其不仅限于 Node 开发者，而是服务于所有开发者，通过预定义配置文件支持多种语言和平台。然而，这也引发了关于项目本质和核心价值的讨论。

- 🚀 **npkill v1.0 即将发布**：核心将作为公共 API 开放，可能推出网页版工具。  
- 💡 **扩展功能的想法**：通过预定义配置文件支持多种语言和平台，如 Python、Java、Rust 等。  
- 🧩 **预定义配置文件的示例**：例如 Python 的`__pycache__`、Java 的`build`等。  
- 🤔 **身份与进化的矛盾**：项目本质是处理`node_modules`，扩展功能是否会稀释其核心价值？  
- 📢 **征求反馈**：创始人希望听取社区意见，决定是否扩展功能或保持原样。  
- 🔗 **相关链接**：npkill 官网、代码仓库、项目介绍及财务支持方式。

---

### [用 6 行 HTML 代码让任何网站加载更快 | DocuSeal](https://www.docuseal.com/blog/make-any-website-load-faster-with-6-lines-html)

**原文标题**: [Make any website load faster with 6 lines of HTML | DocuSeal](https://www.docuseal.com/blog/make-any-website-load-faster-with-6-lines-html)

DocuSeal 提供多种文档签名解决方案和资源，包括 API、企业方案和开发者指南，旨在优化文档处理流程并确保合规性。最新博客介绍了通过 Chrome 推测规则 API 提升网页加载速度的技术。

- 📄 **文档签名 API** - 用于构建自动化和工作流程  
- 🔗 **嵌入功能** - 无缝集成文档签名  
- 🏢 **企业解决方案** - 定制化企业级文档处理  
- 🖥️ **本地部署** - 支持自行托管在私有服务器  
- ✍️ **HTML 转文档** - 创建可填写的独特文档  
- ⚛️ **React 文档签名** - 在 React 应用中嵌入签名功能  
- 🌐 **SaaS 集成** - 为 SaaS 平台提供文档签名支持  
- 📚 **资源与合规** - 符合 eSign 标准及 GDPR 要求  
- 🚀 **性能优化技术** - 使用 Chrome 推测规则 API 实现近乎即时的页面导航  
- ⏳ **预加载与预渲染** - 通过`prefetch`和`prerender`提升用户体验  
- ⚠️ **浏览器兼容性** - 目前仅支持 Chrome 121+，其他浏览器需备用脚本  
- 🔄 **备用方案** - 为 Firefox 和 Safari 提供基于悬停预加载的脚本  
- 📜 **缓存要求** - 需设置`Cache-Control`头部以支持跨浏览器缓存

---

### [推测规则 API - Web API 接口 | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)

**原文标题**: [Speculation Rules API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)

Speculation Rules API 是一种实验性技术，旨在通过预加载或预渲染未来可能导航到的页面来提升多页面应用（MPA）的性能。它通过 JSON 规则配置，支持内联脚本或 HTTP 头的方式定义规则，并提供了比传统预加载/预渲染更灵活的语法和功能。

- 🚀 **实验性技术**：目前处于实验阶段，需谨慎使用并检查浏览器兼容性。  
- 🔗 **目标场景**：适用于多页面应用（MPA），而非单页应用（SPA）。  
- ⚡ **功能对比**：替代 `<link rel="prefetch">` 和已废弃的 `<link rel="prerender">`，支持更复杂的规则配置。  
- 📜 **规则定义**：通过 `<script type="speculationrules">` 或 `Speculation-Rules` HTTP 头指定 JSON 规则，支持预取（prefetch）和预渲染（prerender）。  
- 🛠️ **预取（Prefetch）**：仅下载页面主体，不加载子资源，适用于跨站点导航（需无 Cookie）。  
- 🌟 **预渲染（Prerender）**：完全渲染页面（包括子资源和 JS），默认限制同源，跨源需目标页面通过 `Supports-Loading-Mode` 标头授权。  
- ⚠️ **安全限制**：需避免预取/预渲染可能触发副作用（如注销、购物车操作）或用户状态敏感的页面。  
- 🔍 **检测机制**：通过 `Sec-Purpose` 标头、`Document.prerendering` 属性或 `prerenderingchange` 事件判断页面状态。  
- 🔄 **状态同步**：动态内容需通过 `Broadcast Channel API` 或类似技术更新，避免预渲染内容过时。  
- 🚫 **平台限制**：预渲染期间部分 API（如地理位置、通知）会被延迟或禁止执行。  
- 📊 **兼容性检测**：通过 `HTMLScriptElement.supports("speculationrules")` 判断 API 支持。  

示例规则：  
```html
<script type="speculationrules">
  {
    "prerender": [{ "where": { "href_matches": "/*" } }],
    "prefetch": [{ "urls": ["next.html"] }]
  }
</script>
```  
注意：需在 CSP 中允许 `inline-speculation-rules`。

---

### [未找到标题](https://x.com/izs/status/1950986951227744564)

**原文标题**: [No title found](https://x.com/izs/status/1950986951227744564)

当前页面提示 JavaScript 未启用或浏览器不受支持，导致功能无法正常使用。

- 🚫 JavaScript 未启用：检测到浏览器中 JavaScript 被禁用，需启用以继续使用 x.com。  
- 🌐 切换浏览器：建议更换至受支持的浏览器，具体列表可查看帮助中心。  
- 🔧 扩展冲突：某些隐私相关扩展可能导致问题，尝试禁用后重新加载。  
- 📜 相关链接：提供帮助中心、服务条款、隐私政策等文档入口。  
- 🔄 操作提示：页面鼓励用户再次尝试操作，并标注版权信息（© 2025 X Corp.）。

---

### [编写文本编辑器 - Computerphile - YouTube](https://www.youtube.com/watch?v=g2hiVp6oPZc)

**原文标题**: [Writing a Text Editor - Computerphile - YouTube](https://www.youtube.com/watch?v=g2hiVp6oPZc)

关于 YouTube 的相关信息与链接  

- 📢 关于 - 提供 YouTube 平台的背景与介绍  
- 🗞️ 媒体 - 新闻稿与媒体资源  
- ©️ 版权 - 版权政策与声明  
- 📩 联系我们 - 用户反馈与支持渠道  
- 🎨 创作者 - 创作者相关资源与支持  
- 💼 广告 - 广告合作与商业推广  
- 👩💻 开发者 - 开发者工具与 API 信息  
- 📜 条款 - 平台使用条款与条件  
- 🔒 隐私 - 隐私政策与数据保护  
- ⚖️ 政策与安全 - 社区准则与安全措施  
- 🔧 YouTube 运作机制 - 平台功能与算法简介  
- � 测试新功能 - 参与实验性功能体验  
- ®️ 版权归属 - 2025 年 Google LLC 所有

---

### [wheybags 的博客：我用 C 预处理器宏搭建了我的博客](https://wheybags.com/blog/macroblog.html)

**原文标题**: [wheybags' blog: I built my blog with C preprocessor macros](https://wheybags.com/blog/macroblog.html)

博客作者 Tom Mason 使用 C 预处理器宏构建了自己的博客系统，以替代原本使用的 Jekyll，从而避免了 Ruby 环境的问题。

- 🛠️ 作者最初使用 Jekyll 构建博客，但因 Ruby 环境问题频繁出现而放弃。
- 🤔 作者决定使用 C 预处理器宏来替代 Jekyll，因为他对 C++ 和 C 预处理器非常熟悉。
- ⚙️ 使用 GNU C 预处理器（cpp）来处理 HTML 文件，并通过特殊参数避免不必要的宏替换。
- 📜 通过生成一个头文件来取消所有预定义的宏，防止它们干扰博客内容。
- 📝 博客文章通过宏定义标题、日期和描述，并通过包含模板文件来生成完整的 HTML 页面。
- 📡 使用相同的宏系统生成 RSS 订阅源，通过模板和宏定义动态生成内容。
- 🎨 作者还改进了代码片段的显示方式，使用 SVG 嵌入文本，确保在移动设备上也能良好显示。
- 🔍 通过 highlight.js 解析代码，并将其转换为 SVG 中的<tspan>元素，以保持代码的可读性和可复制性。
- 😊 作者对这种“不按常理出牌”的解决方案感到非常满意，尽管它可能看起来有些混乱。

---

