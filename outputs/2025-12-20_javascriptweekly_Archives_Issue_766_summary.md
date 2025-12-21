### [JavaScript 周刊第 766 期：2025 年 12 月 19 日](https://javascriptweekly.com/issues/766)

**原文标题**: [JavaScript Weekly Issue 766: December 19, 2025](https://javascriptweekly.com/issues/766)

这是 2025 年最后一期《JavaScript 周刊》，包含年度回顾、重要新闻和未来展望。

- 🗓️ 本期是 2025 年最后一刊，明年起将于每周二发布，下一期将于 2026 年 1 月 6 日回归。
- 📦 文章探讨了 JavaScript 打包工具领域的现状，指出竞争焦点已从速度转向代码包体积优化。
- 🤖 介绍了如何将 AI 实际应用于 JavaScript 开发工作流，包括提示工程和构建生产级应用。
- ⚡ Simon Willison 分享了他使用 AI 工具在 4.5 小时内将 HTML5 解析器从 Python 移植到 JavaScript 的经历。
- 🛠️ 简讯部分包含 Dan Abramov 的新工具、Cloudflare Wrangler 的更新、新的拖放库以及 OpenAI GPT 5.2 Codex 的发布。
- 🚀 发布了多个重要库和框架的新版本，如 Tesseract.js 7.0、Base UI 1.0、Wasp 0.20 等。
- 🏆 列出了 2025 年最受欢迎的 10 篇文章，涵盖 JavaScript 谜题、ES2025 新特性、生成器函数实用指南、Web JavaScript 使用现状等主题。
- 📅 按月回顾了 2025 年 JavaScript 生态的重大事件，包括 Bun、Deno、TypeScript、React、Node.js 等关键项目的更新和行业动态。
- 🎄 在分类广告和结语中，推广了开发者工具，并感谢读者一年的支持，预告了 2026 年的回归。

---

### [JavaScript 打包器大赛——console.log()](https://redmonk.com/kholterhoff/2025/12/16/javascript-bundler-grand-prix/)

**原文标题**: [The JavaScript Bundler Grand Prix – console.log()](https://redmonk.com/kholterhoff/2025/12/16/javascript-bundler-grand-prix/)

JavaScript 打包工具领域正经历一场速度竞赛，各大公司投入巨资优化构建性能，但真正的挑战可能已从开发体验转向用户体验，即如何减少代码体积、提升运行时效率。

- 🚀 **速度竞赛白热化**：Vercel、VoidZero、字节跳动等公司竞相推出高性能打包工具（如 Turbopack、Rolldown、Rspack），通过 Rust/Go 等语言重写实现构建速度的大幅提升。
- ⚖️ **性能基准模糊化**：厂商频繁发布提速数据（如“构建快 5-10 倍”），但实际效果因项目差异巨大，且工具迭代迅速，难以判定绝对赢家。
- 🧩 **生态格局多元化**：从老牌工具 Webpack、Rollup 到现代方案 Vite、Bun，打包工具呈现社区项目与商业产品并存的局面，共同应对 JavaScript 依赖膨胀的挑战。
- 🔍 **核心矛盾转移**：专家指出，当构建时间缩短至“1 分钟 vs30 秒”时，速度优化已触及收益递减点，真正的战场应转向产物体积优化和消除未使用代码。
- 🤝 **工具协作深化**：未来打包工具需与编译器（如 SWC）深度集成，实现跨模块分析，从根本上解决“半数代码未使用”的行业痛点。
- 🏁 **竞赛本质演变**：行业正从单纯追求构建速度，转向关注开发者体验的可持续性、产物精简度，以及最终用户的页面加载性能。

---

### [捆绑器 - Bun](https://bun.com/docs/bundler)

**原文标题**: [Bundler - Bun](https://bun.com/docs/bundler)

Bun 是一个快速的本地打包工具，支持 JavaScript、TypeScript、JSX 等多种文件类型，可通过 CLI 命令或 JavaScript API 使用。它旨在减少 HTTP 请求、转换代码（如 TypeScript 和 JSX）、支持框架特性，并处理全栈应用程序的打包需求。Bun 打包器默认生成 ES 模块格式，支持代码分割、插件系统、环境变量注入、源映射生成和多种优化选项，同时提供监视模式和独立可执行文件生成功能。

- 🚀 **快速打包**：Bun 打包器性能优异，在 esbuild 的 three.js 基准测试中表现突出。
- 📦 **减少 HTTP 请求**：通过将多个文件合并为少量自包含的包，优化网络加载性能。
- 🔧 **代码转换**：内置支持 TypeScript、JSX、CSS 模块等，自动转换为纯 JavaScript 和 CSS。
- 🏗️ **框架支持**：通过插件和代码转换实现文件系统路由、客户端 - 服务器代码共置等框架特性。
- 🌐 **全栈应用**：可同时处理服务器和客户端代码，支持生产构建优化和单文件可执行文件生成。
- ⚙️ **灵活配置**：支持多种目标环境（浏览器、Bun、Node.js）、模块格式（ESM、CJS、IIFE）和代码分割选项。
- 🔌 **插件系统**：允许通过插件扩展或覆盖默认行为，增强打包灵活性。
- 🔍 **监视模式**：原生支持监视文件变化并增量重建，提升开发效率。
- 📄 **多文件类型**：支持 .js、.ts、.json、.css、.html 等多种扩展名，并可将未知文件类型作为外部资源处理。
- 🛠️ **高级功能**：包括环境变量注入、源映射生成、代码压缩、外部依赖排除和自定义文件命名等。

---

### [AI 编程学习路径 - 掌握软件开发的未来 | Frontend Masters](https://frontendmasters.com/learn/ai/?utm_source=email&utm_medium=javascriptweekly&utm_content=learnai)

**原文标题**: [Coding with AI Learning Path - Master the Future of Software Development | Frontend Masters](https://frontendmasters.com/learn/ai/?utm_source=email&utm_medium=javascriptweekly&utm_content=learnai)

掌握 AI 辅助软件开发的未来，通过实践学习将生成式内容集成到应用程序中。

- 🚀 掌握 AI 辅助工程工作流程
- ⏱️ 总学习时长 23 小时 47 分钟
- 🎯 获得生成式内容集成实践经验
- 📊 当前学习进度 0%

---

### [我用 Codex CLI 和 GPT-5.2 在 4.5 小时内将 JustHTML 从 Python 移植到 JavaScript。](https://simonwillison.net/2025/Dec/15/porting-justhtml/)

**原文标题**: [I ported JustHTML from Python to JavaScript with Codex CLI and GPT-5.2 in 4.5 hours](https://simonwillison.net/2025/Dec/15/porting-justhtml/)

作者使用 Codex CLI 和 GPT-5.2，在 4.5 小时内将 JustHTML 从 Python 移植到 JavaScript，创建了一个通过 9200 项测试、无依赖的 JavaScript HTML5 解析库，整个过程仅需少量提示，并在处理期间兼顾了家庭活动，引发了关于 AI 辅助开发在伦理、法律及开源生态方面影响的思考。

- 🚀 作者利用 Codex CLI 和 GPT-5.2，仅通过两个初始提示和少量跟进，在约 4.5 小时内成功将 Python 的 JustHTML 库移植到 JavaScript，创建了 simonw/justjshtml。
- 📊 新库通过了 html5lib-tests 测试套件中的 9200 项测试，实现了无依赖的 HTML5 解析功能，并模仿了原 Python 库的 API 设计。
- ⏱️ 整个移植过程基本自动化，GPT-5.2 消耗了约 160 万输入 token 和 62.5 万输出 token，生成了 9000 行 JavaScript 代码，期间作者还进行了购买圣诞树等家庭活动。
- 🔧 作者通过设置里程碑（如 Milestone 0.5）和持续集成（GitHub Actions），引导 AI 逐步完成库的构建、测试和文档编写。
- 🌐 项目最终包括了一个浏览器可用的交互式 playground 界面，并部署在 GitHub Pages 上，方便用户直接体验。
- 💡 实验展示了前沿 LLM 能够执行复杂、长时间的任务，并在拥有健全测试套件的问题上高效工作，突显了“设计智能体循环”的重要性。
- ⚖️ 作者提出了关于 AI 生成代码的伦理、法律（如版权问题）及对开源生态影响的开放性问题，反思了这种开发方式的合理性与责任。

---

### [GitHub - html5lib/html5lib-tests：html5lib的测试套件数据，包含事实上的标准HTML解析测试。](https://github.com/html5lib/html5lib-tests)

**原文标题**: [GitHub - html5lib/html5lib-tests: Testsuite data for html5lib, including the de-facto standard HTML parsing tests.](https://github.com/html5lib/html5lib-tests)

这是一个用于 html5lib 的测试套件数据仓库，包含事实标准的 HTML 解析测试。

- 📚 **测试套件**：为 html5lib 提供测试数据，包含事实标准的 HTML 解析测试。
- ⭐ **项目热度**：获得 237 个星标和 63 个分支，显示社区关注度。
- 🛠️ **代码管理**：包含多个测试模块，如编码、序列化、分词器和树构建等。
- 📄 **许可证**：采用 MIT 许可证，允许自由使用、修改和分发。
- 🔄 **活跃维护**：有 29 个未解决的问题和 9 个拉取请求，显示项目仍在积极开发中。
- 👥 **贡献者**：由 36 位主要贡献者和 22 位其他贡献者共同维护。

---

### [JustJSHTML 游乐场 - HTML5 解析器](https://simonw.github.io/justjshtml/playground.html)

**原文标题**: [JustJSHTML Playground - HTML5 Parser](https://simonw.github.io/justjshtml/playground.html)

JustJSHTML 是一个无需依赖的 HTML5 解析器，旨在通过完整的官方 html5lib 测试套件，提供 CSS 选择器、树遍历和美化打印功能。

- 🌐 无需依赖的 HTML5 解析器
- ✅ 通过完整的 html5lib 官方测试套件
- 🎯 支持 CSS 选择器功能
- 🌳 提供树遍历能力
- 🖨️ 包含美化打印功能

---

### [GitHub - simonw/justjshtml: EmilStenstrom/justhtml 的 JavaScript 移植版](https://github.com/simonw/justjshtml)

**原文标题**: [GitHub - simonw/justjshtml: JavaScript port of EmilStenstrom/justhtml](https://github.com/simonw/justjshtml)

这是一个名为 justjshtml 的 JavaScript 库，它是 Python 项目 JustHTML 的无依赖 JavaScript 移植版本，用于在浏览器和 Node.js 环境中解析 HTML5。

- 🚀 **项目目标**：通过完整的 html5lib-tests 套件（包括分词器、树构建、编码和序列化测试），仅使用纯 JavaScript 实现。
- ⚙️ **技术特性**：无运行时依赖，支持现代浏览器（ES 模块）和 Node.js（ESM），测试通过率高。
- 📦 **快速开始**：提供 Node.js 和浏览器的简单使用示例，支持字符串或字节输入，并包含丰富的配置选项。
- 🔧 **API 功能**：提供节点操作、CSS 选择器查询、流式解析和独立辅助函数，节点对象具有类 DOM 的 API。
- 🛠️ **开发过程**：基于测试驱动开发，使用 OpenAI Codex CLI 和 GPT-5.2 在 4.5 小时内完成移植，并包含完整的测试工作流。
- 🌐 **互动工具**：提供在线和本地的交互式 playground，方便用户实时测试 HTML 解析功能。
- 📚 **致谢与资源**：项目基于 Emil Stenström 的 JustHTML 和 html5lib-tests，架构受 html5ever 影响，UI 改编自 Simon Willison 的 playground。

---

### [介绍 RSC Explorer — 过度解读](https://overreacted.io/introducing-rsc-explorer/)

**原文标题**: [Introducing RSC Explorer — overreacted](https://overreacted.io/introducing-rsc-explorer/)

React Server Components（RSC）协议是 React 用于序列化和反序列化组件树的内部格式，通常未公开文档。近期因安全漏洞披露，社区对其兴趣增加。作者为此开发了 RSC Explorer 工具，这是一个在浏览器中模拟 RSC 协议交互的单页应用，帮助开发者直观理解 RSC 的工作原理，包括流式渲染、客户端与服务器代码交互、状态保持等机制，并提供了多个示例和开源代码。

- 🔍 RSC 协议是 React 内部用于序列化组件树的格式，缺乏公开文档，但近期因安全漏洞受到关注
- 🛠️ 作者开发了 RSC Explorer 工具，在浏览器中模拟 RSC 交互，无需网络请求即可演示协议流程
- 🌐 工具展示了 JSX 如何通过网络传输并在客户端重建，以及流式渲染中 Suspense 处理异步组件的机制
- ⚙️ 示例包括计数器组件传输虚拟 DOM 而非 HTML、服务器动作与客户端表单交互，以及无框架路由刷新实现
- 🔄 通过 Router 示例说明服务器如何向客户端传递新属性并保持组件状态，类似虚拟 DOM 更新
- 📚 工具提供分页、错误处理、客户端引用等更多示例，并支持嵌入代码片段和社区共享
- 🔓 包含安全漏洞 CVE-2025-55182 的演示，需切换至受影响版本才能运行
- 💡 RSC Explorer 完全开源，旨在通过可视化方式降低理解 RSC 底层机制的门槛

---

### [自动为 Cloudflare 配置您的框架·更新日志](https://developers.cloudflare.com/changelog/2025-12-16-wrangler-autoconfig/)

**原文标题**: [Configure your framework for Cloudflare automatically Â· Changelog](https://developers.cloudflare.com/changelog/2025-12-16-wrangler-autoconfig/)

Cloudflare Workers 的 Wrangler 工具现已推出实验性自动配置功能，支持多种流行 Web 框架，简化部署流程。

- 🚀 Wrangler 4.55 新增 `npx wrangler deploy --x-autoconfig` 命令，可自动为支持的框架配置并部署应用到 Cloudflare Workers
- ⚙️ 新增 `npx wrangler setup` 命令，允许仅配置应用而不部署，方便用户预览更改内容
- 📦 首批支持的框架包括 Next.js、Astro、Nuxt、TanStack Start、SolidStart、React Router、SvelteKit、Docusaurus、Qwik 和 Analog
- 🌐 自动配置功能同样支持静态站点，可自动检测资源目录和构建命令，从单个 HTML 文件到 Jekyll 或 Hugo 生成的站点均可一键部署
- 💬 用户可通过 GitHub 讨论区提供实验性功能的反馈

---

### [picknplace.js，拖放操作的替代方案](https://jgthms.com/picknplace.js/)

**原文标题**: [picknplace.js, an alternative to drag and drop](https://jgthms.com/picknplace.js/)

picknplace.js 是一种替代拖放操作的交互方案，通过“选取 - 滚动 - 放置”三步简化操作流程，尤其优化了移动端体验。

- 🖱️ **操作步骤简化**：采用“选取 → 滚动 → 放置”三步流程，支持用 Enter 键确认放置、Esc 键取消操作
- 📱 **移动端优化**：针对触屏设备改进交互，避免传统拖放中同时进行点击、长按、拖动和滚动的繁琐操作
- 🔄 **动态视觉反馈**：选取项目时会生成动画化副本列表，随滚动位置实时更新，提供直观的视觉引导
- 🎯 **操作可控性**：用户可在最终步骤确认或取消所有更改，降低误操作风险
- 💡 **概念验证性质**：当前版本为交互设计的概念演示，开发者可参考源码获取灵感
- 👨💻 **创作者背景**：由前端设计师 @jgthms 开发，可通过 Twitter 和 Github 关注其动态

---

### [介绍 GPT-5.2-Codex | OpenAI](https://openai.com/index/introducing-gpt-5-2-codex/)

**原文标题**: [Introducing GPT-5.2-Codex | OpenAI](https://openai.com/index/introducing-gpt-5-2-codex/)

OpenAI 发布了 GPT-5.2-Codex，这是目前最先进的代理式编码模型，专为复杂现实世界的软件工程和防御性网络安全设计。该模型在长上下文理解、工具调用可靠性和事实准确性方面有显著提升，同时增强了在 Windows 环境下的性能与网络安全能力。发布采取分阶段策略，结合安全措施，并针对网络安全专业人员推出受信任访问试点计划。

- 🚀 GPT-5.2-Codex 针对代理式编码优化，提升长时任务处理、大型代码重构与迁移能力，并在 Windows 环境中表现更佳
- 🔐 网络安全能力显著增强，可加速漏洞研究与防御工作，但需谨慎部署以应对双重用途风险
- 📊 在 SWE-Bench Pro 和 Terminal-Bench 2.0 基准测试中达到最先进水平，能有效处理大型代码库与复杂工程任务
- 🛡️ 新增安全防护措施，并基于预备框架评估，为未来可能达到“高”级别网络能力做准备
- 👥 已向付费 ChatGPT 用户开放，即将逐步开放 API 访问，并推出针对网络安全专业人士的受信任访问试点计划
- 💡 实际案例显示，前代模型曾协助安全研究人员发现 React 漏洞，体现 AI 在防御性安全工作中的加速作用
- 🌐 通过渐进式部署、安全措施与行业合作，旨在最大化防御效益，同时降低技术滥用风险

---

### [Tesseract.js | 纯 JavaScript OCR 支持 100 种语言！](https://tesseract.projectnaptha.com/)

**原文标题**: [Tesseract.js | Pure Javascript OCR for 100 Languages!](https://tesseract.projectnaptha.com/)

Tesseract.js 是一个纯 JavaScript 的多语言 OCR 库，支持超过 100 种语言，可在浏览器和 Node.js 环境中运行，提供文本方向检测和边界框识别功能。

- 🌐 纯 JavaScript OCR 引擎，支持 100 多种语言
- 🔄 自动检测文本方向和脚本
- 📦 提供段落、单词和字符边界框的简单接口
- 🌍 可在浏览器和 Node.js 服务器端运行
- 📚 示例代码和 API 文档可在 GitHub 查看
- 🖼️ 提供英文、中文和俄文演示页面
- 📄 支持上传图像文件进行文本识别

---

### [基础 UI](https://base-ui.com/)

**原文标题**: [Base UI](https://base-ui.com/)

Base UI 是一个由 Radix、Floating UI 和 Material UI 的创建者开发的 React UI 组件库，专注于构建可访问、灵活且持久的用户界面，其设计强调可组合性、一致性和细节工艺，不强制视觉风格，旨在为专业界面设计提供未来可靠的基础。

- 🧩 由知名 UI 库创作者打造，专注于 React 的可访问组件库
- 🛠️ 组件设计强调可组合性、一致性和工艺细节，提供高度灵活性
- 🎨 不强制视觉风格，支持团队打造独特且可访问的界面
- ⏳ 基于多年经验构建，旨在提供持久、未来可靠的界面设计基础
- 👥 专为创作者设计，由经验丰富的设计和工程团队支持
- ❓ 提供常见问题解答，涵盖兼容性、可访问性、商业使用等细节

---

### [黄蜂圣诞发射 - React 19、Claude 代码插件、Polar！🎄🎁 | Wasp](https://wasp.sh/blog/2025/12/17/wasp-xmas-launch)

**原文标题**: [Wasp Xmas Launch - React 19, Claude Code Plugin, Polar! 🎄🎁 | Wasp](https://wasp.sh/blog/2025/12/17/wasp-xmas-launch)

Wasp 将于 12 月 23 日提前发布四项新功能作为圣诞礼物，并举办线上庆祝活动。

- 🎁 支持 React 19，提供新 Actions、表单 API 和钩子等功能
- 🤖 推出官方 Claude Code 插件，让 AI 辅助开发更懂 Wasp
- 🐻‍❄️ 在 Open SaaS 中集成开源支付平台 Polar，简化 SaaS 计费
- 📰 新增 `wasp news` CLI 命令，直接在终端获取更新和提示

---

### [发布 7.4.0 版本 · graffle-js/graffle · GitHub](https://github.com/graffle-js/graffle/releases/tag/7.4.0)

**原文标题**: [Release 7.4.0 · graffle-js/graffle · GitHub](https://github.com/graffle-js/graffle/releases/tag/7.4.0)

这是一个关于 GraphQL 客户端库 Graffle 的 GitHub 仓库页面，主要展示了其最新版本 7.4.0 的发布信息。

- 🚀 **版本 7.4.0 发布**：于 12 月 15 日由 jasonkuhrt 发布，最新提交为 9b8714c。
- ✨ **新增功能**：在`GraphQLResponse`和`GraphQLClientResponse`类型中公开了响应头（`headers`）和响应体（`body`）属性，便于访问非 GraphQL 响应数据（例如返回纯 JSON 的 401/403/503 错误）。
- 👥 **贡献者**：此功能由@adambrgmn 贡献（PR #1476）。
- 📊 **项目概况**：该仓库拥有 6.1k 星标、310 个分支和 43 个议题，是一个活跃的开源项目。

---

### [Next.js 16.1 | Next.js](https://nextjs.org/blog/next-16-1)

**原文标题**: [Next.js 16.1 | Next.js](https://nextjs.org/blog/next-16-1)

Next.js 16.1 专注于提升开发工作流速度和稳定性，主要更新包括 Turbopack 文件系统缓存稳定化、新的实验性打包分析工具、更便捷的调试支持，以及对传递性外部依赖的改进。

- 🚀 **Turbopack 文件系统缓存已稳定**：`next dev` 默认启用磁盘缓存，大幅提升大型项目重启开发服务器时的编译速度，实测可达 5 倍至 14 倍加速。
- 🔍 **实验性打包分析器**：集成交互式工具，帮助开发者分析生产包大小、优化核心 Web 指标、减少依赖体积，并支持按路由过滤和查看完整导入链。
- 🐛 **更便捷的调试支持**：通过 `next dev --inspect` 可直接启用 Node.js 调试器，无需再设置 `NODE_OPTIONS` 环境变量。
- 📦 **改进的传递性外部依赖处理**：Turbopack 现可自动处理 `serverExternalPackages` 中的传递性依赖，无需手动配置，避免版本冲突和维护负担。
- 📉 **安装包体积减小**：得益于 Turbopack 缓存层简化，Next.js 安装体积减少约 20MB。
- ⬆️ **新增升级命令**：引入 `next upgrade` 命令，简化版本升级流程。
- 🛠️ **其他工具与优化**：包括 MCP 路由获取工具、开发日志增强、异步导入打包优化，以及改进的源映射路径兼容性。

---

### [Bun v1.3.5 | Bun 博客](https://bun.com/blog/bun-v1.3.5)

**原文标题**: [Bun v1.3.5 | Bun Blog](https://bun.com/blog/bun-v1.3.5)

Bun 发布了新版本，包含伪终端 API 支持、编译时特性标志、字符串宽度计算改进、V8 类型检查 API 增强、S3 客户端 Content-Disposition 支持、.npmrc 环境变量扩展修复，以及多项网络、Windows、Node.js 兼容性、TypeScript、Web API、打包器、YAML、安全和 Linux 相关的错误修复。

- 🚀 新增 Bun.Terminal API，支持在 POSIX 系统上创建和管理伪终端，用于运行交互式终端应用
- 🏗️ 打包器引入编译时特性标志，支持通过 `bun:bundle` 进行静态死代码消除
- 📏 改进 `Bun.stringWidth`，准确计算 Unicode 字符、ANSI 转义序列和表情符号的终端显示宽度
- 🔧 实现额外的 V8 C++ API 类型检查方法，提升与原生 Node.js 模块的兼容性
- 📎 S3 客户端新增 `contentDisposition` 选项，控制浏览器下载文件的行为
- ⚙️ 修复 `.npmrc` 中带引号值的环境变量扩展，支持 `?` 可选修饰符
- 🐛 修复多项错误，包括 macOS kqueue 事件循环 CPU 占用、Windows WebSocket 崩溃、Node.js API 兼容性问题等
- 🔒 修复安全漏洞，防止非 npm 包通过特定依赖源欺骗可信依赖列表
- 🙏 感谢 10 位贡献者的代码提交

---

### [发布 MathJax v4.1.0 · mathjax/MathJax-src · GitHub](https://github.com/mathjax/MathJax-src/releases/tag/4.1.0)

**原文标题**: [Release MathJax v4.1.0 · mathjax/MathJax-src · GitHub](https://github.com/mathjax/MathJax-src/releases/tag/4.1.0)

MathJax v4.1.0 版本发布，该版本在 v4.0.0 基础上新增多项功能并修复了多个问题，主要涵盖兼容性改进、用户界面优化、语音生成增强、TeX 输入处理更新、CHTML 和 SVG 输出调整，以及新增配置选项等方面。

- 🆕 **兼容性改进**：针对旧版浏览器优化了 CSS 使用，并添加了 `Object.hasOwn()` 的 polyfill 支持，同时修复了 Windows 环境下的构建工具问题。
- 🎨 **用户界面更新**：新增深色模式支持，改进了对话框的显示与交互，优化了表达式探索器的帮助图标位置，并允许通过 `enableExplorerHelp` 配置禁用该图标。
- 🔊 **语音生成增强**：改进了标签和括号的语音朗读规则，全面应用 SSML 标记以提升高亮同步，并优化了包含超链接的公式语音提示。
- 📝 **TeX 输入处理修复**：修正了 `mhchem` 扩展中箭头方向错误、`\operatorname{}` 内数字间距问题，以及 `data-latex` 属性标记不准确等多个问题。
- 🖥️ **输出格式优化**：调整了 CHTML 和 SVG 输出中的 CSS 规则以提升旧浏览器兼容性，修复了向量箭头位置偏差和表格布局计算错误。
- ⚙️ **新增配置选项**：引入了 `fontExtensions`、`fonts` 加载路径、`polyfillHasOwn` 和 `enableExplorerHelp` 等配置选项，提供更灵活的定制能力。
- 🐛 **问题修复列表**：详细列出了在 TeX 输入、输出渲染、用户界面、API 及构建工具等方面的多项错误修复。

---

### [发布 7.2.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.2.0)

**原文标题**: [Release 7.2.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.2.0)

Prisma 发布了 7.2.0 稳定版本，包含多项 ORM 功能增强、错误修复及 VS Code 扩展改进，并介绍了企业支持与招聘信息。

- 🎉 新增 SQL 注释插件，支持查询洞察元数据
- 🔧 为 `db pull`、`db push` 和 `migrate dev` 命令添加 `-url` 参数，提升连接配置灵活性
- ⚙️ 允许在 `prisma generate` 等场景中使用未定义的 URL，优化工作流
- 🐰 根据 JavaScript 运行时（Bun 或其他）自定义 `prisma init` 的初始化设置
- 🐛 修复多项错误，包括 Postgres 适配器错误处理、字节更新问题及 UTF-8 字符处理
- 📊 确保 `prisma version --json` 仅向标准输出发送 JSON 格式内容
- 🔌 修复 VS Code 扩展中的 Studio 连接问题，提升集成可靠性
- 💼 提供企业支持计划，涵盖性能调优、安全合规及优先问题处理
- 🌐 开放多个职位招聘，邀请开发者加入 Prisma 团队

---

### [一个令人困惑的 JavaScript 解析谜题](https://www.hillelwayne.com/post/javascript-puzzle/)

**原文标题**: [A Perplexing Javascript Parsing Puzzle](https://www.hillelwayne.com/post/javascript-puzzle/)

这篇文章探讨了 JavaScript 中一个令人困惑的解析现象：代码`x = 1 x --> 0`在控制台中输出`1`，并解释了其历史原因和技术细节。

- 🧩 代码`x = 1 x --> 0`在 JavaScript 控制台中输出`1`，因为`-->`在行首时被解析为注释起始符
- 📜 这一行为源于早期 Web 的兼容性需求，当时为兼容不支持`<script>`标签的旧浏览器，开发者使用 HTML 注释包裹脚本代码
- 🏛️ 为确保向后兼容，`<!--`和`-->`作为合法注释标记被纳入 ECMAScript 2015 标准，其中`-->`仅在行首有效
- 🌐 现代浏览器均支持此语法，Node.js 和 Electron 等基于 V8 引擎的环境也继承这一特性
- 🔧 这一设计体现了 Web 标准“永不破坏现有网站”的原则，即使它现在看起来像是一种历史遗留的“黑客”行为

---

### [Ecma 国际批准 ECMAScript 2025：有哪些新特性？](https://2ality.com/2025/06/ecmascript-2025.html)

**原文标题**: [Ecma International approves ECMAScript 2025: What’s new?](https://2ality.com/2025/06/ecmascript-2025.html)

ECMAScript 2025 语言规范已获 Ecma International 批准，正式成为标准，引入了多项新特性以增强 JavaScript 的功能和性能。

- 📥 **导入属性和 JSON 模块**：支持通过 `import` 语句导入非 JavaScript 资源（如 JSON 文件），使用 `with` 属性指定类型。
- 🔄 **迭代器辅助方法**：新增 `filter()`、`map()`、`drop()`、`take()` 等方法，支持对任意可迭代数据结构进行链式操作，无需创建中间数组。
- 🔗 **新的 Set 方法**：包括 `intersection()`、`union()`、`difference()` 等集合操作，以及 `isSubsetOf()`、`isSupersetOf()` 等关系检查方法。
- 🛡️ **RegExp.escape()**：提供转义文本功能，便于在正则表达式中安全使用字符串。
- 🏷️ **正则表达式模式修饰符（内联标志）**：允许在正则表达式的部分模式中应用标志（如 `i` 忽略大小写），而非整个表达式。
- 🔁 **重复命名捕获组**：允许在正则表达式的不同分支中使用相同的组名，增强模式匹配的灵活性。
- ⚡ **Promise.try()**：简化异步链的启动，支持同步和异步代码的混合处理，避免错误处理冗余。
- 🧮 **16 位浮点数（float16）支持**：新增 `Math.f16round()`、`Float16Array` 类型数组及相关 `DataView` 方法，优化数值计算性能。
- 📚 **免费 ECMAScript 2025 书籍**：作者提供在线免费书籍《Exploring JavaScript (ES2025 Edition)》，涵盖 JavaScript 历史、新特性详解等内容。

---

### [ECMAScript® 2025 语言规范](https://tc39.es/ecma262/2025/)

**原文标题**: [ECMAScript® 2025 Language Specification](https://tc39.es/ecma262/2025/)

总结失败：Error code: 400 - {'error': {'message': "This model's maximum context length is 131072 tokens. However, you requested 611051 tokens (603051 in the messages, 8000 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

### [宏观镜 - 开源免费](https://macroscope.com/open-source?utm_medium=newsletter&utm_source=jsweekly&utm_content=sponsoredlink&utm_campaign=dec25)

**原文标题**: [Macroscope - Free for Open Source](https://macroscope.com/open-source?utm_medium=newsletter&utm_source=jsweekly&utm_content=sponsoredlink&utm_campaign=dec25)

Macroscope 现为符合条件的非商业开源项目提供免费 AI 代码审查服务，旨在帮助开源社区减少错误、提升代码审查效率并增强项目可见性。

- 🆓 **免费开放**：符合资格的非商业开源项目可免费使用 Macroscope 的 AI 代码审查功能。
- 🐛 **高效查错**：在代码审查基准测试中，Macroscope 对 100 多个真实生产环境错误的检出率最高。
- ⚙️ **解决痛点**：针对开源社区常见问题，如减少代码错误、降低管理负担、跟踪项目贡献状态等提供解决方案。
- 📋 **资格要求**：项目需使用开源许可证、非商业用途、并在 GitHub 上公开。
- 🤝 **赞助机会**：Macroscope 寻求赞助优秀的开源项目，可通过指定渠道推荐。
- 🚀 **快速启动**：符合条件者可申请免费使用，其他用户可享受两周免费试用。

---

### [我想发电机的工效学设计正逐渐吸引我。 | 亚历克斯·麦克阿瑟](https://macarthur.me/posts/generators/)

**原文标题**: [I think the ergonomics of generators is growing on me. | Alex MacArthur](https://macarthur.me/posts/generators/)

作者分享了对 JavaScript 生成器（generators）从陌生到逐渐欣赏的心路历程，探讨了生成器在迭代协议、惰性求值、解耦代码、异步处理及分页优化等方面的实用价值。

- 🔄 生成器基于迭代器和可迭代协议，通过`function*`和`yield`简化了序列生成，支持无限序列和惰性求值
- ⚡ 惰性求值能提升性能，避免不必要的计算，尤其适用于大数据集或高成本操作场景
- 🧩 生成器有助于减少代码耦合，封装状态逻辑，使组件职责更清晰，提升可维护性和复用性
- ⏳ 异步生成器（async generators）结合`for await...of`可优雅处理轮询任务，避免回调地狱和递归陷阱
- 📄 生成器能优化分页数据获取，实现即时的流式处理，减少内存占用和等待时间
- 🛠️ 生成器可动态生成元素等序列，支持解构赋值，提供灵活的实用工具

---

### [function* - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)

**原文标题**: [function* - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)

`function*` 声明用于创建一个生成器函数，该函数可以暂停和恢复执行，并保存其上下文。它返回一个符合迭代器协议的生成器对象，支持通过 `yield` 表达式和 `next()` 等方法进行双向控制流。虽然曾用于异步编程，但现在更常用 `async/await` 和 Promise。生成器函数不能作为构造函数使用，且没有箭头函数形式。

- 🚀 **创建生成器**：`function*` 声明将新的生成器函数绑定到指定名称，返回可暂停执行的 `Generator` 对象。
- 🔄 **控制流机制**：通过 `yield` 暂停执行并返回值，使用 `next()` 恢复；`throw()` 和 `return()` 可向生成器内部抛出错误或提前返回。
- 📅 **兼容性广泛**：自 2016 年 9 月起，该功能已在主流浏览器中稳定支持，适用于大多数设备和版本。
- ⚠️ **使用限制**：生成器函数没有箭头函数变体，且不可用作构造函数（如 `new f()` 会报错）。
- 🔧 **多样定义方式**：除声明外，还可通过表达式、对象方法、计算属性（如 `*[Symbol.iterator]()`）或类方法定义生成器。
- 📊 **迭代协议应用**：生成器天然实现迭代器协议，便于创建自定义迭代逻辑（例如无限序列生成）。
- 🆚 **与异步对比**：过去用于解决回调地狱，现多由 `async` 函数和 Promise 替代，但仍适用于简化迭代器定义等场景。

---

### [JavaScript | 2024 | HTTP Archive 网络年鉴](https://almanac.httparchive.org/en/2024/javascript)

**原文标题**: [JavaScript | 2024 | The Web Almanac by HTTP Archive](https://almanac.httparchive.org/en/2024/javascript)

本文分析了 2024 年 JavaScript 在网页中的使用现状、趋势及其对性能的影响，并提供了优化建议。

- 📈 **JavaScript 体积持续增长**：2024 年移动端中位 JavaScript 负载达 558KB，桌面端达 613KB，较去年增长 14%，对设备资源造成更大压力。
- 📊 **请求数量稳步上升**：移动端中位 JavaScript 请求达 22 个，90 分位数达 68 个，增加请求可能引发主线程资源竞争，影响性能。
- 🗑️ **未使用代码问题显著**：约 44% 的下载 JavaScript 字节在页面加载时未被使用，移动端中位未使用字节达 206KB。
- 🛠️ **打包与转译工具使用稳定**：webpack 使用率保持在 5%，但顶级网站使用率下降；Babel 在顶级移动网站中使用率达 12%，TypeScript 使用率约 6%。
- ⚡ **异步加载成为主流**：`async`属性使用率从 2022 年的 76% 增至 87%，`defer`使用率从 42% 微增至 47%，`module`使用率仍较低（4%）。
- 🔗 **资源提示使用变化**：`preload`使用率从 16.4% 降至 7.5%，`prefetch`从约 1% 增至 4.8%，`modulepreload`使用率极低（约 0.7%）。
- 🌐 **第三方脚本占比增加**：90 分位数下第三方 JavaScript 请求从 34 个增至 36 个，可能带来性能、安全与隐私风险。
- 🔄 **动态导入与 Web Workers 使用增长**：动态导入使用率从 0.34% 增至 3.70%；Web Workers 使用率从 12% 增至 30%，有助于提升性能。
- 🗜️ **Brotli 压缩成为主流**：Brotli 使用率达 45%，首次超过 gzip（41%），但第三方脚本中 gzip 仍占主导（60%）。
- ✂️ **代码压缩仍有优化空间**：38% 的移动页面存在未压缩 JavaScript，中位页面可压缩约 12KB，主要问题来自第一方代码（占浪费字节的 82.7%）。
- 🐌 **响应性能问题突出**：移动端 90 分位数 INP 达 275ms，超出“良好”阈值；TBT 在移动端 90 分位数达 5.95 秒，长任务时间中位值达 2.37 秒。
- 🏗️ **jQuery 仍占主导地位**：使用率达 74%，核心库组合中 jQuery 相关占多数；React 使用率微增至 10%，Web Components 使用率有所增长。
- 📉 **遗留问题依然存在**：2.15% 的移动页面仍使用同步 XHR，12% 使用`document.write`，67% 的页面仍包含不必要的老旧 JavaScript 转换。

---

### [每位 JavaScript 开发者 2025 年都应了解的一些特性 | WaspDev 博客](https://waspdev.com/articles/2025-04-06/features-that-every-js-developer-must-know-in-2025)

**原文标题**: [Some features that every JavaScript developer should know in 2025 | WaspDev Blog](https://waspdev.com/articles/2025-04-06/features-that-every-js-developer-must-know-in-2025)

JavaScript 持续演进，2025 年开发者应掌握一些关键特性以提升代码效率和现代性，包括迭代器助手、数组 at() 方法、Promise.withResolvers() 等新功能，以及一些可能被忽视的实用技巧如变量交换和结构化克隆。

- 🔄 **迭代器助手**：提供类似数组方法的高效迭代器操作（如 drop、take、filter），避免链式转换中的临时数组分配，提升大数组处理性能。
- 🔢 **数组 at() 方法**：支持正负索引访问数组元素，简化如`arr[arr.length - 1]`的代码，更直观获取末尾元素。
- 🤝 **Promise.withResolvers()**：简化 Promise 解析器的创建，替代冗长的`new Promise`模式，使代码更简洁。
- 🔧 **字符串替换回调**：`replace()`和`replaceAll()`支持回调函数，允许单次遍历进行复杂替换，提升性能和灵活性。
- 🔄 **变量交换**：使用解构赋值`[a, b] = [b, a]`交换变量，避免临时变量，代码更优雅。
- 🧬 **structuredClone()**：提供深拷贝对象的标准 API，正确处理循环引用和特殊值（如 NaN、undefined），优于`JSON.stringify/parse`。
- 🏷️ **标签模板**：允许函数解析模板字面量，用于自动转义或处理插值，增强字符串处理能力。
- 🗑️ **WeakMap/WeakSet**：弱引用集合，允许对象作为键且不影响垃圾回收，适用于无副作用的对象关联场景。
- ⚙️ **集合操作**：Set 新增方法（如 difference、intersection、union），支持布尔运算，简化集合处理逻辑。

---

### [如何有效管理 package.json | Val Town 博客](https://blog.val.town/gardening-dependencies)

**原文标题**: [How to keep package.json under control | Val Town Blog](https://blog.val.town/gardening-dependencies)

Val Town 作为一个复杂的 React 应用，依赖管理至关重要。尽管 node_modules 体积庞大，但许多依赖是构建功能所必需的。作者分享了一套依赖管理的最佳实践，旨在保持项目的简洁与高效。

- 📖 **仔细阅读新依赖的源码和文档**：除了 React 等大型依赖外，建议亲自阅读代码，避免引入不必要的复杂性和安全风险。
- 🔍 **利用包管理器工具分析依赖树**：通过`npm ls`或`pnpm why`等命令了解直接和传递性依赖，发现可复用的模块以减少冗余。
- 📊 **评估包的实际大小影响**：使用磁盘空间分析工具（如 Grand Perspective）和打包分析工具（如 rollup-plugin-visualizer）分别监控开发和生产环境的体积。
- ✅ **选择高质量模块的标准**：关注维护历史、TypeScript 支持、测试覆盖和文档完整性，避免使用已废弃或与问题不匹配的模块。
- 🧹 **定期清理未使用的依赖**：借助 Renovate 保持依赖更新，使用 Knip 快速识别并移除 package.json 中的无用模块。
- 👥 **关注优秀模块作者**：建立常用可靠开发者的清单（如 Sindre Sorhus、Rich Harris 等），以便快速找到高质量解决方案。
- 🌱 **接受依赖管理的必然性**：依赖生态快速迭代是常态，主动维护依赖是开发工作的重要组成部分，需以积极态度应对。

---

### [JavaScript 简史 | Deno](https://deno.com/blog/history-of-javascript)

**原文标题**: [A brief history of JavaScript | Deno](https://deno.com/blog/history-of-javascript)

JavaScript 诞生 30 周年，从最初为网页添加交互性的脚本语言，发展成为当今最流行的编程语言，支撑着从浏览器到服务器、桌面应用乃至太空探索的广泛领域。其发展历程见证了开源社区的力量、技术标准的演进以及生态系统的持续创新。

- 🚀 **1995 年诞生**：Brendan Eich 在 10 天内为 Netscape 创造了 JavaScript，旨在为静态网页添加动态功能，并因 Java 的热度而得名。
- 🌐 **1996-1997 年标准化**：为避免浏览器生态分裂，JavaScript 被提交给 ECMA International，形成了 ECMAScript 标准，并由 TC39 委员会维护其发展。
- ⚔️ **浏览器战争**：微软推出 JScript 与 Netscape 竞争，而 Netscape 开源其浏览器代码催生了 Mozilla 项目及后来的 Firefox。
- 🔄 **2000 年代技术革新**：AJAX（2004 年）的普及带来了 Web 2.0 时代，jQuery（2006 年）简化了跨浏览器开发，Node.js（2009 年）让 JavaScript 走向服务器端。
- 📦 **模块化与工具生态**：CommonJS、npm（2010 年）和 Babel（2014 年）等工具推动了代码共享和现代开发流程，ES6（2015 年）引入了类、模块等关键特性。
- ⚛️ **框架崛起**：AngularJS、React（2013 年）、Vue.js（2014 年）等框架重塑了前端开发模式，促进了单页应用（SPA）的流行。
- 🛠️ **全栈与跨平台**：Express.js、MongoDB 等形成了 MEAN 栈，Electron（2013 年）使得用 Web 技术构建桌面应用成为可能。
- 🚀 **性能与运行时演进**：V8 引擎（2008 年）提升了执行速度，WebAssembly（2015 年）为高性能计算铺路，Deno（2020 年）和 Bun（2023 年）等新兴运行时不断涌现。
- 🔧 **开发体验提升**：TypeScript（2012 年）提供了静态类型，ESLint、Prettier 等工具优化了代码质量与格式，VS Code（2016 年）成为主流编辑器。
- ☁️ **云与边缘计算**：AWS Lambda（2014 年）、Cloudflare Workers（2017 年）推动了无服务器和边缘计算的发展。
- 📜 **持续标准化**：ECMAScript 每年更新，加入如 async/await、ES 模块等特性，TC39 通过开放流程推动语言演进。
- ⚖️ **生态治理与挑战**：OpenJS Foundation 成立（2019 年）整合了 JavaScript 与 Node.js 生态，npm leftpad 事件（2016 年）暴露了供应链安全问题，Oracle 对 JavaScript 商标的争议仍在持续。
- 🚀 **未来展望**：JavaScript 在太空（SpaceX Dragon，2020 年）、AI 工具链和更快的运行时（如 tsgo）中继续拓展边界，社区致力于更开放、高性能的下一代 Web 开发。

---

### [战争故事：我调试过的最棘手的漏洞](https://www.clientserver.dev/p/war-story-the-hardest-bug-i-ever)

**原文标题**: [War story: the hardest bug I ever debugged](https://www.clientserver.dev/p/war-story-the-hardest-bug-i-ever)

作者在 Google Docs 团队工作时，遇到一个难以复现的 Chrome 专属致命错误，通过两天艰苦调试，最终发现是 V8 引擎优化层级的 Math.abs() 函数错误返回负值导致的罕见 Bug。

- 🐛 **突发错误**：Google Docs 突然出现大量致命错误，仅影响特定 Chrome 版本，但用户投诉未激增
- 🔍 **艰难复现**：通过自动化脚本反复加粗/取消加粗 50 页文档，在第 10-40 次操作间随机触发这个非确定性 Bug
- 🖥️ **复杂架构**：当时 Google Docs 使用自定义布局引擎，所有屏幕元素绝对定位，依赖大量缓存保证性能
- 🧩 **错误传播**：问题根源在于视图层的记账代码错误，但实际崩溃发生在错误值被缓存并传递到下游后
- 👥 **协作调试**：作者与精通视图层的同事合作，花两天时间逐步回溯断点，定位问题区域
- 🤯 **惊人发现**：Math.abs() 函数在特定条件下对负输入返回负值，经技术主管确认后确认为 V8 引擎 Bug
- 🔗 **内部协调**：通过 Google 内部渠道联系 V8 团队，发现该问题已在修复状态但尚未部署
- ⚙️ **根源分析**：V8 引擎重构优化层时，有人误将 Math.abs() 在超级优化层级实现为恒等函数
- 🩹 **临时方案**：添加特定 Chrome 版本检查，手动实现绝对值计算，并添加详细注释说明原因
- 🎯 **无奈结局**：花费两天调试的问题其实已被修复，除了展示调试的艰辛外没有明确的教学意义

---

### [人们对 Electron 的常见误解](https://felixrieseberg.com/things-people-get-wrong-about-electron/)

**原文标题**: [Things people get wrong about Electron](https://felixrieseberg.com/things-people-get-wrong-about-electron/)

Electron 框架的核心理念在于利用 Web 技术构建跨平台桌面应用，并通过捆绑 Chromium 渲染引擎确保应用性能、稳定性和安全性，同时支持与原生代码灵活结合。

- 🛠️ **技术融合**：Electron 允许开发者混合使用 Web 技术（如 HTML/JavaScript）与原生代码（C++、Rust 等），打破“仅限 JavaScript”的误解，兼顾开发效率与原生性能。
- 🌐 **Web 技术优势**：Web 技术已成为广泛验证的 UI 方案，支撑着 NASA 任务控制、彭博终端等高要求应用，其跨平台能力和生态成熟度是核心优势。
- ⚡ **性能与可控性**：捆绑 Chromium 而非依赖系统 WebView，确保应用使用最新渲染引擎，避免系统版本碎片化，同时自主控制安全更新与性能优化。
- 💾 **安装包大小**：虽然 Electron 应用体积较大（约 100-300MB），但用户更关注功能体验，存储成本在当今环境中已非首要考量。
- 🎯 **解决实际需求**：Electron 旨在填补跨平台桌面应用开发工具的空缺，其成功源于帮助开发者高效构建用户喜爱的应用，而非与其他框架竞争。

---

### [转向仅支持 ESM](https://antfu.me/posts/move-on-to-esm-only)

**原文标题**: [Move on to ESM-only](https://antfu.me/posts/move-on-to-esm-only)

本文探讨了 JavaScript 生态系统中从 CommonJS（CJS）向 ES 模块（ESM）过渡的趋势，认为当前工具和生态已成熟，是时候推动 ESM-only 包的发展。作者回顾了双格式包的问题，并分析了适合迁移到 ESM-only 的场景，如新包、浏览器包和 CLI 工具。最后介绍了用于分析依赖 ESM 采用情况的工具 Node Modules Inspector，并展望了未来生态的优化方向。

- 🛠️ **工具就绪**：现代工具如 Vite、Vitest、tsx 等已全面支持 ESM，ESLint v9 也引入了原生 ESM 配置，降低了开发门槛。
- 📈 **生态趋势**：ESM 在 npm 包中的占比从 2021 年的 7.8% 增长到 2024 年的 25.8%，显示生态正稳步向 ESM 迁移。
- 🔄 **互操作改进**：Node.js v22 支持`require()`加载 ESM 模块，并引入新语法实现 CJS 兼容导出，缓解了迁移中的互操作难题。
- ⚠️ **双格式问题**：同时维护 CJS 和 ESM 会导致互操作复杂性、依赖解析混乱和包体积膨胀，增加维护负担。
- 🚀 **迁移场景**：新包、浏览器包、独立 CLI 工具以及针对高版本 Node.js 的包更适合优先采用 ESM-only。
- 🔍 **用户考量**：包作者需评估现有用户生态，例如 ESLint 插件可借助 v9 的 ESM 原生支持顺利过渡。
- 📊 **进展可视化**：作者开发的 Node Modules Inspector 工具可分析依赖的 ESM 采用状态，帮助开发者制定迁移策略。
- 🌱 **未来展望**：作者计划逐步将维护的包过渡到 ESM-only，并持续优化工具，以推动更轻量、高效的 JavaScript 生态。

---

### [Bun 1.2 | Bun 博客](https://bun.sh/blog/bun-v1.2)

**原文标题**: [Bun 1.2 | Bun Blog](https://bun.sh/blog/bun-v1.2)

Bun 1.2 是一个重大更新，专注于提升 Node.js 兼容性、引入内置的 S3 和 PostgreSQL 支持、改进包管理器、测试运行器和打包工具，并带来大量性能优化和新 JavaScript 特性。

- 🚀 **Node.js 兼容性大幅提升**：通过运行 Node.js 测试套件，修复了数千个错误，多个核心模块的测试通过率超过 90%。
- ☁️ **内置 S3 对象存储 API**：新增 `Bun.s3`，提供高性能的原生 S3 客户端，支持读写、预签名 URL 和 `fetch()` 集成，速度比 Node.js SDK 快 5 倍。
- 🗄️ **内置 PostgreSQL 客户端**：新增 `Bun.sql`，提供高性能的原生 PostgreSQL 支持（MySQL 即将推出），速度比其他客户端快 50%。
- 📝 **文本化锁文件**：`bun install` 默认生成 JSONC 格式的 `bun.lock` 文件，提升可读性和协作便利性，同时安装速度还提升了 30%。
- ⚡ **Express 性能提升**：通过优化 `node:http` 和 Bun 的 HTTP 服务器，使 Express 框架在 Bun 中的处理速度比在 Node.js 中快 3 倍。
- 🧪 **测试运行器增强**：`bun test` 新增 JUnit 和 LCOV 报告支持、内联快照、`test.only()`、更多 `expect()` 匹配器以及自定义错误消息。
- 📦 **打包工具功能扩展**：`bun build` 支持 HTML 导入、独立可执行文件跨平台编译、字节码缓存、CommonJS 输出格式以及内置 CSS 解析和打包。
- 🛠️ **新增内置 API**：包括 `Bun.udpSocket()`、`Bun.file()` 增强（支持 `delete()` 和 `stat()`）、`Bun.color()`、`dns.prefetch()` 以及 `Bun.inspect.table()` 等实用工具。
- 🔧 **包管理器改进**：支持 `package.json` 中的注释和尾随逗号、`.npmrc` 文件、`bun run --filter`、`bun outdated`、`bun publish` 以及依赖补丁功能 (`bun patch`)。
- ⚙️ **行为调整与优化**：`bun run` 的工作目录行为与其他包管理器对齐，`bun test` 会捕获未处理的错误，`Bun.build()` 在失败时拒绝 Promise，多项操作获得显著性能提升。
- ✨ **支持最新 JavaScript/Web 特性**：包括导入属性、`using` 声明、`Promise.withResolvers()`、`Promise.try()`、`Error.isError()`、`Uint8Array` 的 `toBase64`/`toHex`、迭代器辅助方法、`Float16Array` 以及 `TextDecoderStream` 等 Web API。

---

### [Express.js 新篇章：2024 年的辉煌成就与 2025 年的宏伟蓝图](https://expressjs.com/2025/01/09/rewind-2024-triumphs-and-2025-vision.html)

**原文标题**: [A New Chapter for Express.js: Triumphs of 2024 and an ambitious 2025](https://expressjs.com/2025/01/09/rewind-2024-triumphs-and-2025-vision.html)

Express.js 在 2024 年完成了治理革新、技术升级与安全强化，并发布了 Express 5.0，为 2025 年的自动化发布、性能优化和现代化改造奠定了坚实基础。

- 🏛️ **治理与社区里程碑**：推出《Express Forward Plan》并重组技术委员会，增强社区协作与发布流程透明度。
- 🛡️ **安全强化**：成立安全工作组，实施威胁模型，完成安全审计，并快速响应多个 CVE 漏洞。
- 🚀 **技术进展**：正式发布 Express 5.0，启动 Express 6.0 规划，并重新整合至 Node.js CITGM 项目。
- 🌟 **生态认可**：获得 OpenJS 基金会“Impact Project”认证，彰显其在 JavaScript 生态中的重要性。
- 🔄 **2025 年路线图**：依托 Sovereign Tech Fund，计划实现 npm 发布自动化、引入作用域包、强化安全流程与性能监控。
- 📚 **现代化与文档**：逐步淘汰过时技术（如猴子补丁），并加强安全文档，提升开发者体验。
- 🤝 **持续协作**：鼓励社区通过 GitHub Discussions 和开放会议参与，共同推动框架发展。

---

### [- YouTube](https://www.youtube.com/watch?v=cRC9DlH45lA)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=cRC9DlH45lA)

该内容为 YouTube 平台页脚导航链接，列出了网站的主要政策、功能说明及公司信息。

- 📄 关于平台与公司信息
- 📰 新闻与媒体相关
- ©️ 版权声明与保护
- 📞 联系与反馈渠道
- 🎨 内容创作者相关
- 📢 广告合作说明
- 💻 开发者资源与工具
- 📜 服务条款与协议
- 🔒 隐私政策与安全
- ⚙️ 平台运作机制
- 🧪 新功能测试公告
- ™️ 2025 年谷歌所有权声明

---

### [甲骨文曾以 Node.js 为其 JavaScript 商标辩护——如今却希望人们对此视而不见 | Deno](https://deno.com/blog/deno-v-oracle2)

**原文标题**: [Oracle justified its JavaScript trademark with Node.js—now it wants that ignored | Deno](https://deno.com/blog/deno-v-oracle2)

Oracle 试图通过法律手段维持其对“JavaScript”商标的控制，尽管该商标涉及一个由社区主导的开放标准语言，引发了对其商标合法性的广泛质疑。

- 🚨 Oracle 在商标续展中使用 Node.js 网站截图作为证据，尽管与该项目无关
- 📜 Deno 公司以通用性、废弃和欺诈为由，正式申请撤销该商标
- ⏳ Oracle 仅回应欺诈指控，并试图通过程序性动议拖延案件核心审理
- 🔍 质疑 Oracle 提交的 Oracle JET 证据是否仅为维持商标而存在，缺乏实际使用
- 🌐 JavaScript 由 ECMA-262 规范定义，由多方维护，Oracle 并无实际贡献或控制权
- ⚖️ 此案引发对商标系统滥用的担忧，即企业是否可无限期持有无关商标
- 📢 呼吁社区通过签署公开信和传播信息，共同反对 Oracle 的商标主张

---

### [TypeScript 5.8 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-5-8/)

**原文标题**: [Announcing TypeScript 5.8 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-8/)

TypeScript 5.8 正式发布，引入了多项新特性与优化，包括对条件返回表达式的更精细类型检查、支持在 CommonJS 中 require() ECMAScript 模块、新增 --module node18 和 --erasableSyntaxOnly 等编译选项，以及性能改进和部分行为调整。

- 🐛 **更精细的条件返回类型检查**：现在能直接检测 return 语句中条件表达式各分支的类型错误，避免因 any 类型导致的漏洞。
- 🔗 **支持 CommonJS 调用 ESM 模块**：在 --module nodenext 下，允许 CommonJS 文件通过 require() 加载 ECMAScript 模块，简化库作者的模块发布。
- 🏷️ **新增 --module node18 稳定选项**：为 Node.js 18 用户提供固定模块行为，区别于 nodenext 的某些特性（如禁止 require() ESM）。
- 🧹 **--erasableSyntaxOnly 编译选项**：确保 TypeScript 代码可被安全擦除为纯 JavaScript，适用于 Node.js 的 --experimental-strip-types 等场景。
- ⚙️ **--libReplacement 标志控制库替换**：允许禁用或启用 @typescript/lib-* 包替换默认 lib 文件的行为，提升性能。
- 📄 **声明文件中保留计算属性名**：在生成 .d.ts 文件时，保持计算属性名的原始书写形式，提升可预测性。
- ⚡ **程序加载与更新优化**：减少路径规范化时的数组分配，避免重复验证编译选项，提升大型项目的响应速度。
- 🚫 **限制 import assertions 语法**：在 --module nodenext 下，强制使用 import attributes（with 关键字）替代已弃用的 assert 语法。
- 📦 **DOM 类型更新与行为调整**：lib.d.ts 更新可能影响现有代码，部分错误修复可能引入新的类型检查错误。

---

### [密歇根 TypeScript 创始人成功在 Ty...内运行《毁灭战士》](https://socket.dev/blog/typescript-types-running-doom)

**原文标题**: [Michigan TypeScript Founder Successfully Runs Doom Inside Ty...](https://socket.dev/blog/typescript-types-running-doom)

Socket Firewall Free 现已集成至 Docker 加固镜像中，为 Node.js、Python 和 Rust 的加固基础镜像提供构建时和依赖安装阶段的供应链保护。

- 🔒 Socket Firewall Free 已内置在 Docker 加固镜像中
- 🛡️ 为 Node.js、Python 和 Rust 提供供应链安全保护
- ⚙️ 覆盖构建时和依赖安装阶段的安全防护
- 🐳 基于加固基础镜像进一步增强安全性

---

### [获取失败](https://javascriptweekly.com/link/178735/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/178735/web)

无法总结：获取内容失败，状态码 403。

---

### [Express@5.1.0：现为 npm 默认版本，附带长期支持时间表](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

**原文标题**: [Express@5.1.0: Now the Default on npm with LTS Timeline](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Express v5.0.0 已于去年发布，但直到现在才被设为 npm 的默认版本。项目团队在过去一年中致力于完善文档、提供迁移支持、确保生态系统兼容性，并制定了长期支持策略。v5.1.0 的发布标志着 v5 进入活跃支持阶段，同时 v4 进入维护阶段，并公布了版本支持时间表。

- 📄 **文档与迁移指南更新**：全面更新了 v5 文档，提供了详细的迁移指南，帮助开发者顺利升级。
- 🔧 **自动化迁移工具**：推出了 codemod 包，自动化处理从 v4 到 v5 的代码迁移，减少手动工作量。
- 🌍 **生态系统兼容性**：确保中间件和资源兼容 v5，特别关注初学者体验，避免因版本不匹配导致的问题。
- 🛡️ **长期支持策略**：引入了三个支持阶段（CURRENT、ACTIVE、MAINTENANCE），并公布了 v4 和 v5 的支持时间表。
- 🚀 **v5.1.0 更新内容**：包括性能优化、依赖更新、新功能支持（如 Uint8Array 和 ETag），并清理了技术债务。
- 🤝 **社区与未来计划**：感谢贡献者，启动性能工作组，改进 TypeScript 体验，并已开始 v6 的初步讨论。

---

### [Koa - Node.js 的下一代 Web 框架](https://koajs.com/)

**原文标题**: [Koa - next generation web framework for node.js](https://koajs.com/)

Koa 是一个由 Express 团队设计的现代化 Web 框架，专注于提供更精简、更具表现力和更健壮的基础，适用于 Web 应用和 API 开发。

- 🚀 基于 Express 团队设计，旨在成为更轻量、更强大的 Web 框架
- ⚡ 利用异步函数，避免回调函数，显著提升错误处理能力
- 🧩 核心不捆绑任何中间件，保持高度模块化
- ✨ 提供优雅的方法集，使服务器开发快速而愉快

---

### [Node.js — 行程报告：Node.js 协作峰会（2025 年巴黎）](https://nodejs.org/en/blog/events/collab-summit-2025-paris)

**原文标题**: [Node.js — Trip report: Node.js collaboration summit (2025 Paris)](https://nodejs.org/en/blog/events/collab-summit-2025-paris)

2025 年巴黎 Node.js 协作峰会汇集了近 40 名现场参与者和十余名远程参与者，围绕 CI 可靠性、WASM 模块、内存管理、导师计划、贡献者体验、AsyncLocalStorage 标准化、单可执行应用、Undici 集成、Chrome DevTools 支持、Next-10 调查及模块定制等关键议题展开讨论与规划。

- 🛡️ CI 可靠性与安全：针对近期安全事件，探讨了 CI 基础设施管理和测试稳定性改进方案，包括自动化流程优化和故障检测机制。
- ⚡ 技术进展分享：介绍了实验性 WASM 模块的启用计划、V8 内存管理集成（Cppgc）以提升性能与安全性，以及模块化工具链的优化方向。
- 👥 社区与协作：回顾了导师计划的成效，讨论了如何改善贡献者体验，包括减少 CI 不稳定、优化决策流程（如引入表情符号投票和 AI 总结），并计划更新 Next-10 倡议。
- 🌐 AsyncLocalStorage 标准化：探讨将 Node.js 的 AsyncLocalStorage 引入 Web 标准（AsyncContext 提案），重点解决跨平台上下文传播的安全性与 API 设计挑战。
- 📦 单可执行应用（SEA）：讨论了 ESM 支持、工具链简化和虚拟文件系统等需求，但进展受限于志愿者和资金不足，计划组建团队推动。
- 🔗 Undici 集成：规划通过暴露调度器配置来增强内置 HTTP 功能，支持 HTTP/2 自动升级，并探索通过 WASM 集成 Milo 项目。
- 🔧 开发工具集成：与 Chrome DevTools 团队合作，完善网络流量检查、Worker 线程自动发现等功能，提升 Node.js 调试体验。
- 📊 生态调研：优化了 Next-10 年度调查问题，以更准确收集社区对 Node.js 未来发展的意见。
- 🧩 模块定制与性能：更新了模块加载钩子的同步化改进方案，并介绍了基于 AST 重写的 ESM 插桩工具，以提升可观测性支持。

---

### [p5.js](https://p5js.org/)

**原文标题**: [p5.js](https://p5js.org/)

p5.js 是一个创意编程库，提供丰富的学习资源、社区作品展示及支持途径。

- 📚 提供 p5.js 库参考与示例学习资源
- 🎨 展示社区创意作品，如地理数据编织、黏菌模拟等
- 👥 活跃的创作者社区呈现多样视觉艺术作品
- 💝 支持通过捐赠和下载库文件参与发展

---

### [醒来吧，混音！ | 混音](https://remix.run/blog/wake-up-remix)

**原文标题**: [Wake up, Remix! | Remix](https://remix.run/blog/wake-up-remix)

Remix 框架宣布结束休眠，将推出全新的 Remix 3 版本，该版本将不再依赖 React，而是基于 Preact 构建，并致力于打造更轻量、更贴近 Web 标准的开发体验。

- 🛌 **Remix 结束休眠**：在 React Router v7 稳定并整合了 Remix 的核心功能后，Remix 团队决定重启项目，探索新的发展方向。
- 🚀 **React Router v7 表现卓越**：通过支持 RSC（React Server Components）和服务器端路由，React Router v7 已能提供类似 Remix 的完整全栈体验，并被 Shopify、GitHub 等大型项目广泛采用。
- 🧩 **Remix 3 的全新定位**：新版本将作为一个模块化工具包，注重简洁性、清晰度和性能，减少对外部依赖（包括 React），并基于 Preact 构建更贴近 Web 的组件模型。
- 🧭 **核心开发原则**：包括以模型优先开发适应 AI 时代、基于 Web API 构建、避免过度依赖静态分析和第三方依赖、强调组件的可组合性，以及提供统一分发包。
- 🎉 **社区参与邀请**：团队将在 Remix Jam 活动中分享进展，并邀请开发者订阅更新以获取最新动态。

---

### [3.13 版本发布 | GSAP | 文档与学习](https://gsap.com/blog/3-13/)

**原文标题**: [3.13 release | GSAP | Docs & Learning](https://gsap.com/blog/3-13/)

GSAP 3.13 版本发布，核心更新包括 GSAP 及其所有插件（如 SplitText、MorphSVG）现已完全免费，包括商业用途；SplitText 插件全面重写，体积减小 50% 并新增 14 项功能，如屏幕阅读器无障碍支持、响应式重新分割和嵌套元素处理；新增动画至 CSS 变量的功能；优化了 Webflow 集成安装流程；Club GSAP 会员将过渡至公共仓库，私人仓库访问将于 2025 年 6 月 1 日停止。

- 🎉 GSAP 及其所有插件（包括 SplitText、MorphSVG）现已完全免费，适用于商业用途
- 🔧 SplitText 插件全面重写，体积减小 50%，新增 14 项功能，如无障碍支持和响应式重新分割
- 🆕 新增动画至 CSS 变量的功能，可直接将 CSS 属性动画到变量值
- 🌐 优化 Webflow 集成，可直接在设置中启用 GSAP 核心库和插件
- 🔄 Club GSAP 会员将过渡至公共 NPM 仓库，私人仓库访问将于 2025 年 6 月 1 日停止
- 📚 提供完整文档、学习资源和社区论坛支持

---

### [Glitch 即将迎来重要更新](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

**原文标题**: [Important changes are coming to Glitch](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

Glitch 平台宣布将终止应用托管服务，这是基于当前生态变化和资源挑战所做的战略调整，旨在更有效地服务开发者社区。

- 🗓️ **服务终止时间**：2025 年 7 月 8 日将关闭项目托管和用户资料功能，仪表板会保留至 2025 年底供代码下载。
- 🔄 **过渡支持**：平台将提供项目子域名重定向功能（有效期至少至 2026 年底），并发布项目迁移指南。
- 💰 **付费方案调整**：立即停止新 Glitch Pro 订阅，现有订阅将服务至 7 月 8 日并退还未使用费用。
- 🌍 **生态演变**：因维护成本上升及新兴平台（如 Fly.io、Deno 等）提供更优方案，Glitch 决定重新聚焦核心价值。
- 🤝 **社区参与**：鼓励用户通过社区论坛或直接邮件反馈，共同探索 Glitch 未来的发展方向。

---

### [TypeScript 原生预览版发布 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)

**原文标题**: [Announcing TypeScript Native Previews - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)

TypeScript 团队宣布推出 TypeScript 原生预览版，该版本通过使用 Go 语言重写编译器并利用共享内存并行与并发技术，实现了高达 10 倍的性能提升。目前，用户可通过 npm 安装预览版编译器，并在 VS Code 中安装对应的扩展来体验。虽然该版本仍处于开发阶段，缺少部分稳定版功能，但已支持大多数类型检查，包括 JSX 和 JavaScript+JSDoc，并计划在未来逐步完善。

- 🚀 **性能大幅提升**：通过 Go 语言重写编译器，结合并行与并发技术，在多数项目中实现 10 倍速度提升。
- 📦 **预览版发布**：可通过 npm 安装 `@typescript/native-preview` 包，使用 `tsgo` 命令进行类型检查和构建。
- 🔌 **编辑器扩展**：VS Code 用户可安装“TypeScript (Native Preview)”扩展，需手动启用实验性功能以体验新语言服务。
- ⚙️ **功能进展**：已支持大部分类型检查，包括 JSX 和 JavaScript+JSDoc，但 `--build`、声明文件生成等高级功能尚待实现。
- 🛠️ **API 与兼容性**：提供了基于 IPC 的 API 层，支持跨语言调用；部分配置（如模块解析）需调整以适配新版本。
- 📅 **未来规划**：预览版将每日更新，目标在今年内完善编译器与编辑器功能，并最终成为 TypeScript 7。

---

### [宣布 Oxlint 1.0 | 零虚空](https://voidzero.dev/posts/announcing-oxlint-1-stable)

**原文标题**: [Announcing Oxlint 1.0 | VoidZero](https://voidzero.dev/posts/announcing-oxlint-1-stable)

Oxlint 1.0 稳定版正式发布，这是一款基于 Rust 构建的 JavaScript 和 TypeScript 代码检查工具，以其卓越的性能和易用性著称，已在 Shopify、Airbnb 等大型公司中得到应用。

- 🚀 **性能卓越**：比 ESLint 快 50~100 倍，在大型代码库中可显著降低 CI 成本，实测处理速度可达每秒约 10,000 个文件。
- 🏢 **业界认可**：已被 Shopify、Airbnb、梅赛德斯 - 奔驰等公司以及 Bun、Preact 等大型开源项目采用，在实际应用中验证了其效能。
- ⚙️ **易于上手**：无需配置即可运行，支持通过 `.oxlintrc.json` 文件进行灵活配置，并兼容 ESLint 扁平配置，便于迁移和团队协作。
- 📚 **规则全面**：内置超过 500 条规则，覆盖完整的 ESLint 规则集及多个流行插件，同时提供独有的 Oxlint 规则。
- 🔧 **集成友好**：提供 VS Code、IntelliJ 等主流编辑器的扩展支持，以及语言服务器协议，并配备清晰、可操作的错误诊断信息。
- 🗺️ **持续发展**：未来规划包括支持自定义规则、进一步的性能优化以及更精细的配置功能，项目由超过 200 名贡献者共同推动。

---

### [Vite 7.0 正式发布！ | Vite](https://vite.dev/blog/announcing-vite7.html)

**原文标题**: [Vite 7.0 is out! | Vite](https://vite.dev/blog/announcing-vite7.html)

Vite 7.0 正式发布，标志着该前端构建工具在诞生五年后迎来重要更新。本次版本聚焦性能提升、开发者体验优化及生态扩展，引入了 Rolldown 作为未来默认打包工具，并强化了环境 API 等核心功能。

- 🎉 **Vite 7.0 发布**：庆祝工具诞生五周年，周下载量达 3100 万次，生态影响力持续扩大
- 🌍 **线下 ViteConf**：将于 10 月在阿姆斯特丹举办首次线下会议，促进社区交流
- ⚡ **Rolldown 集成**：推出基于 Rust 的新一代打包工具，可显著提升大型项目构建速度
- 🔧 **Vite DevTools 开发**：与 NuxtLabs 合作打造深度调试工具，增强项目诊断能力
- 📚 **多语言文档**：新增波斯语翻译，并完善简体中文等多国语言支持
- 🚀 **Node.js 版本升级**：要求 Node.js 20.19+ 或 22.12+，全面转向 ESM 模块
- 🌐 **默认浏览器目标更新**：调整为 "baseline-widely-available"，提升跨浏览器兼容性
- 🧪 **环境 API 增强**：新增 buildApp 钩子，支持插件协同构建环境
- 🔗 **Vitest 兼容**：Vite 7.0 需搭配 Vitest 3.2+ 版本使用
- 📋 **平滑迁移建议**：移除已弃用功能，提供详细迁移指南和完整更新日志

---

### [探索 JavaScript（ES2025 版）](https://exploringjs.com/js/)

**原文标题**: [Exploring JavaScript (ES2025 Edition)](https://exploringjs.com/js/)

《探索 JavaScript》是一本面向初学者的现代 JavaScript 指南，涵盖至 ES2025 版本，旨在通过清晰的结构和丰富的辅助材料降低学习难度。

- 📚 本书原名《JavaScript for impatient programmers》，现更新为 ES2025 版，适合有编程基础但无需 JavaScript 经验的读者
- 🚀 采用现代特性优先的教学思路，包含可选高级章节和测试驱动练习、闪卡等辅助材料
- 🌐 提供免费在线阅读版本，数字离线套餐包含无 DRM 的 HTML/EPUB/PDF 格式电子书
- 💰 数字套餐分 39 美元“电子书”与 59 美元“电子书 + 附加资源”两档，旧版用户可享 25%-50% 升级折扣
- 🛒 另提供 ES2019 版纸质书在全球各大亚马逊平台销售，纸质书持有者可优惠获取数字套餐
- 👨🏫 作者 Axel Rauschmayer 博士专注 JavaScript 领域十余年，通过博客、书籍和培训课程分享专业知识

---

### [生物群落 v2—代号：生物型 | 生物群落](https://biomejs.dev/blog/biome-v2/)

**原文标题**: [Biome v2—codename: Biotype | Biome](https://biomejs.dev/blog/biome-v2/)

Biome v2（代号 Biotype）正式发布，这是首个不依赖 TypeScript 编译器即可提供类型感知 lint 规则的 JavaScript 和 TypeScript linter，标志着项目迈向下一代 Web 工具链的重要里程碑。

- 🚀 **首个独立类型感知 linter**：无需安装 TypeScript 包即可进行类型感知的代码检查，例如 noFloatingPromises 规则可检测约 75% 的浮动 Promise 案例。
- ⚙️ **多文件分析与类型推断**：新增文件扫描器支持跨文件类型查询，通过项目规则（project rules）启用，兼顾性能与功能扩展。
- 📦 **增强的 Monorepo 支持**：改进嵌套配置文件支持，新增`root: false`和`extends: "//"`配置方式，优化多包项目管理。
- 🔌 **Linter 插件初版发布**：支持匹配代码片段并报告诊断信息，为未来功能扩展奠定基础。
- 📑 **导入组织器全面升级**：解决空白行分组、同模块导入合并等问题，新增自定义排序和导出语句支持。
- 🛠️ **新增辅助功能（Assists）**：提供无诊断信息的代码操作，如对象键排序和 JSX 属性排序。
- 🔕 **改进的代码抑制功能**：新增`// biome-ignore-all`全文件抑制及`// biome-ignore-start/end`范围抑制。
- 🌐 **实验性 HTML 格式化器**：支持.html 文件格式化，为 Vue、Svelte 等框架集成铺路，需手动启用。
- 👏 **致谢与赞助方**：特别感谢 Vercel 赞助类型推断工作，Depot 提供 CI 支持，以及多位核心贡献者的技术贡献。
- 🛣️ **未来路线图**：重点包括稳定 HTML 支持、扩展框架集成、Markdown 解析器开发及类型推断优化。
- 🤝 **社区参与方式**：鼓励通过翻译、Discord 交流、代码贡献（如 lint 规则开发、解析器改进）或财务赞助支持项目发展。

---

### [数据库迎来新用户——大语言模型，它们需要不同的数据库 | 虎数据](https://www.tigerdata.com/blog/the-database-new-user-llms-need-a-different-database)

**原文标题**: [The Database Has a New User—LLMs—and They Need a Different Database | Tiger Data](https://www.tigerdata.com/blog/the-database-new-user-llms-need-a-different-database)

本文介绍了 TigerData 正在实验的“自描述数据库”概念，旨在通过为 PostgreSQL 添加自然语言描述的语义目录，帮助 LLM 更准确地理解和查询数据库。实验显示，使用语义目录可将 SQL 生成准确率提升高达 27%。

- 🧠 **数据库缺乏结构上下文**：传统数据库模式无法自我解释，导致 LLM 在缺乏额外上下文时难以准确生成查询，实验中 42% 的无上下文 LLM 生成 SQL 查询存在关键错误。
- 📚 **通过语义目录添加上下文**：允许开发者用自然语言描述数据库模式和业务逻辑，为 LLM 提供必要的语义信息，从而显著提升查询准确性。
- 🛠️ **构建自描述数据库的四个核心思想**：将语义嵌入模式、版本化描述、自我纠正查询机制（利用 EXPLAIN）以及透明度量和迭代。
- 🔬 **当前实验组件**：包括存储模式元素自然语言描述的语义目录，以及用于衡量查询准确性的评估工具，重点解决检索中因名称含义模糊导致的问题。
- 📈 **语义上下文提升性能**：在早期测试中，使用 LLM 生成的语义目录将某些模式的 SQL 生成准确率从 58% 提高到 86%，检索召回率也有所改善。
- 🔄 **查询工作流程**：分为四个步骤——使用 LLM 描述数据库、人工审核并添加上下文、导入到目录中、根据自然语言生成 SQL。
- 💡 **关键经验教训**：丰富的语义信息（而不仅是模式名称）对生成正确 SQL 至关重要；建议从严格限制的接口（如函数）开始，再逐步扩大访问范围。
- 🔍 **利用 EXPLAIN 自我纠正**：通过 PostgreSQL 的 EXPLAIN 命令预先捕获查询错误，使代理能够自我纠正，进一步提高准确性。
- 🗄️ **语义目录的灵活存储**：支持集成到现有数据库或独立部署，提供部署灵活性，特别是在仅具有只读访问权限时。
- 🚀 **未来展望：从自描述到自学习**：计划实现目录的自学习能力，通过分析生产环境查询自动丰富元数据，并支持用自然语言表达复杂的访问策略。

---

### [获取失败](https://javascriptweekly.com/link/178749/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/178749/web)

无法总结：获取内容失败，状态码 403。

---

### [Deno 2.4：deno bundle 功能回归 | Deno](https://deno.com/blog/v2.4)

**原文标题**: [Deno 2.4: deno bundle is back | Deno](https://deno.com/blog/v2.4)

Deno 2.4 版本重新引入了 `deno bundle` 命令，并新增了文本与二进制文件导入、稳定的内置 OpenTelemetry 支持、依赖管理优化、权限控制增强、Node.js API 兼容性改进等多项功能，旨在提升开发体验与运行时性能。

- 📦 **`deno bundle` 回归**：恢复单文件打包功能，支持 JavaScript/TypeScript、npm/JSR 依赖，集成 esbuild 实现摇树优化与压缩。
- 📄 **导入文本与字节文件**：通过 `--unstable-raw-imports` 标志，可直接将文本、二进制等文件作为模块导入，简化资源嵌入流程。
- 📊 **内置 OpenTelemetry 稳定化**：移除 `--unstable-otel` 标志，默认提供日志、指标与链路追踪的自动插桩，提升可观测性。
- ⚙️ **新增 `--preload` 标志**：允许在主脚本执行前运行预设代码，便于全局环境修改或依赖预加载。
- 🔄 **依赖管理命令 `deno update`**：新增子命令，支持一键更新 `deno.json` 或 `package.json` 中的依赖至最新兼容版本。
- 📈 **覆盖率收集扩展至 `deno run`**：除 `deno test` 外，`deno run` 也可通过 `--coverage` 标志收集代码覆盖率数据。
- 🔧 **环境变量 `DENO_COMPAT=1`**：简化 Node.js 兼容性配置，自动启用多项不稳定标志以提升与 `package.json` 项目的协作体验。
- 🛡️ **权限控制增强**：`--allow-net` 支持子域名通配符与 CIDR 范围；新增 `--deny-import` 标志以显式阻止特定主机导入。
- 📦 **Node.js 兼容性提升**：全面支持 `package.json` 条件导出、裸说明符运行、`Buffer` 等全局变量，并改进 `tsconfig.json` 与本地 npm 包支持。
- 🛠️ **工具链优化**：`deno fmt` 新增 XML/SVG 格式化；LSP 增强自动导入与诊断能力；`fetch` 支持 Unix/Vsock 套接字；`deno serve` 添加 `onListen` 回调。

---

### [NuxtLabs 加入 Vercel](https://nuxtlabs.com/)

**原文标题**: [NuxtLabs is joining Vercel](https://nuxtlabs.com/)

NuxtLabs 宣布加入 Vercel，旨在通过整合资源强化开源框架 Nuxt 的持续发展，确保项目在 MIT 许可下保持透明化运营，并将社区贡献置于核心位置。未来团队将聚焦 AI 集成与工具开源化，为开发者提供更高效的建设体验。

- 🚀 NuxtLabs 加入 Vercel 以专注开源发展，无需分散精力处理资金与维护问题
- 🌍 项目保持 MIT 许可，路线图公开透明，社区仍为核心
- 💡 赞助资金将转入 Open Collective 平台，确保直接支持核心开发与贡献者
- 🆓 即将免费开放 Nuxt UI v4 所有专业组件及 Figma 工具包
- 🛠️ 开源自托管版 Nuxt Studio，支持直接集成 Nuxt Content 站点管理
- 🔄 NuxtHub 将适配多平台，无缝对接 Vercel 市场的 Postgres 等服务
- 🤖 重点探索 AI 与 Nuxt 开发体验融合，与 Vercel AI 团队深度协作
- 🙏 感谢社区长期支持，创始人特别致谢团队成员、投资者及家人

---

### [TypeScript 5.9 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9/)

**原文标题**: [Announcing TypeScript 5.9 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9/)

TypeScript 5.9 正式发布，带来了多项新特性和改进，包括更精简的 `tsc --init` 配置生成、支持 `import defer` 语法、新增 `--module node20` 选项、DOM API 的摘要描述、可扩展的悬停预览、可配置的悬停长度限制，以及多项性能优化和需要注意的行为变更。

- 🛠️ `tsc --init` 现在生成更精简且预设了推荐选项的 `tsconfig.json` 文件，减少了初始配置的复杂性。
- ⏳ 新增对 ECMAScript `import defer` 语法的支持，允许延迟执行模块及其依赖，直到首次访问其导出，有助于优化启动性能。
- 🖥️ 引入了稳定的 `--module node20` 编译器选项，用于模拟 Node.js v20 的行为，并默认设置 `--target es2023`。
- 📚 许多 DOM API 现在提供了基于 MDN 文档的摘要描述，增强了编辑器内的代码提示体验。
- 🔍 预览了“可扩展悬停”功能，允许在编辑器中展开或折叠悬停提示以查看更详细的类型信息。
- 📏 支持通过 `js/ts.hover.maximumLength` 设置配置悬停提示的最大长度，且默认长度已显著增加。
- ⚡ 包含多项性能优化，例如缓存类型实例化以减少重复工作，以及优化文件存在性检查以减少闭包创建。
- ⚠️ 包含一些需要注意的行为变更，例如 `lib.d.ts` 的更新可能导致与 `ArrayBuffer` 和 `TypedArray` 相关的类型错误，以及类型参数推断的调整可能引入新的类型错误。

---

### [ECharts 6 新特性 - 基础入门 - 使用手册 - Apache ECharts](https://echarts.apache.org/handbook/en/basics/release-note/v6-feature/)

**原文标题**: [ECharts 6 Features - What's New - Basics - Handbook - Apache ECharts](https://echarts.apache.org/handbook/en/basics/release-note/v6-feature/)

Apache ECharts 6.0 正式发布，带来 12 项重大升级，围绕更专业的视觉呈现、拓展数据表达边界和释放组合自由三大核心维度，旨在让复杂数据呈现既强大又优雅，为开发者提供更灵活、便捷的图表创作体验。

- 🎨 全新默认主题：采用现代设计语言，通过设计令牌重构色彩与间距，确保图表在不同业务场景下和谐一致，并提供 v5.js 主题文件便于迁移。
- 🔄 动态主题切换：支持运行时无缝切换主题，无需重新初始化图表实例，显著提升多主题场景下的用户体验。
- 🌙 暗黑模式支持：自动适配系统暗黑/亮色模式，通过监听系统主题动态调整图表主题，增强应用界面一致性。
- 🕸️ 新增弦图：直观展示复杂关系网络中的流向与权重，支持使用源节点和目标节点的渐变颜色绘制边，创造独特视觉效果。
- 🐝 新增蜂群图：在分类轴上智能分布重叠数据点，保持数值轴准确性，避免传统散点图的拥挤问题。
- 📊 新增散点抖动：为密集数据点添加随机偏移，清晰展示数据分布，提升可读性且性能优于蜂群图。
- 📈 新增断裂轴：采用撕纸效果可视化展示数值差异巨大的数据，支持点击展开还原真实比例。
- 💹 增强股票交易图：优化标签相对于坐标系的位置，提供分时图、MACD、成交量、订单簿和深度图等专业交易分析工具。
- 🧩 新增矩阵坐标系：自由组合图表类型和组件，支持创建协方差矩阵图、周期表等灵活复杂的可视化布局。
- 🔧 增强自定义系列：支持动态注册和 npm 发布，提供官方自定义系列项目，便于代码复用和共享。
- 📉 新增自定义图表：包括小提琴图、等高线图、睡眠阶段图、分段环形图、条形范围图和线形范围图，丰富数据表达形式。
- 📏 坐标轴标签优化：智能调整默认标签布局，防止文本溢出和重叠，适应动态数据变化。

---

### [jQuery 4.0.0 候选版本 1 发布 | 官方 jQuery 博客](https://blog.jquery.com/2025/08/11/jquery-4-0-0-release-candidate-1/)

**原文标题**: [jQuery 4.0.0 Release Candidate 1 | Official jQuery Blog](https://blog.jquery.com/2025/08/11/jquery-4-0-0-release-candidate-1/)

jQuery 4.0.0 的第一个候选版本（rc.1）已发布，标志着该重大版本更新进入最终测试阶段。此版本包含多项期待已久的破坏性变更，如移除旧版 IE 支持、废弃 API 及简化内部行为，并首次引入了更轻量的“slim”构建版本。团队鼓励开发者积极测试并提供反馈，若无重大问题，最终版将随后发布。

- 🚀 **发布候选版本**：jQuery 4.0.0-rc.1 已推出，进入最终测试阶段，呼吁社区协助测试并反馈问题。
- ⚠️ **破坏性变更**：移除了对 IE11 以下版本的支持、已废弃的 API、未公开的内部参数及一些过于复杂的“魔法”行为。
- 📦 **新增 Slim 构建**：提供了排除 Ajax、动画和 Deferreds 模块的轻量版本，gzip 后体积比常规版本小约 8KB。
- 🔗 **获取方式**：可通过 jQuery CDN 直接获取文件或通过 npm 安装，第三方 CDN 将暂不托管此候选版本。
- 📄 **升级辅助**：同步发布了 4.0 升级指南和 jQuery Migrate 工具，但两者在最终版前仍可能调整。
- 🙏 **致谢贡献者**：感谢所有提交补丁、报告错误或参与测试的贡献者及 jQuery 团队。

---

### [媒体兔](https://mediabunny.dev/)

**原文标题**: [Mediabunny](https://mediabunny.dev/)

本文档是一个开源项目的导航页面，提供了核心资源与访问入口。

- 🧭 **主要导航** - 包含搜索功能与核心栏目（指南、API、大语言模型等）的访问路径
- 📘 **指南** - 提供项目使用教程与操作指引
- 🔌 **API** - 包含应用程序接口文档与开发资源
- 🧠 **大语言模型** - 展示与大语言模型相关的功能或集成内容
- 💡 **示例** - 呈现实际应用案例与代码范例
- 🤝 **赞助者** - 列出项目赞助方或支持者信息
- 📜 **许可证** - 说明项目的开源协议与使用条款
- 🎨 **外观** - 提供界面显示或主题的自定义选项

---

### [AddyOsmani.com - 谷歌 Chrome 浏览器 17 年历程 - 我们的浏览器历史回顾](https://addyosmani.com/blog/chrome-17th/)

**原文标题**: [AddyOsmani.com - Google Chrome at 17 - A history of our browser](https://addyosmani.com/blog/chrome-17th/)

本文回顾了 Google Chrome 浏览器 17 年的发展历程，从 2008 年作为一款以漫画形式发布的新浏览器，成长为如今被数十亿用户使用的核心产品。文章重点阐述了 Chrome 始终遵循的四大核心理念——速度、安全、稳定、简洁，并详细介绍了其在多进程架构、V8 引擎、AI 集成等方面的关键技术创新与演变。

- 🚀 **速度为先**：Chrome 自诞生起就将性能作为核心，其 V8 JavaScript 引擎大幅提升了网页应用运行速度。通过持续优化渲染管道、网络协议（如推动 HTTP/2 和 HTTP/3）以及专注于核心网页指标，Chrome 在 Speedometer 等基准测试中不断刷新纪录，为用户节省了大量加载时间。
- 🛡️ **深度防御安全**：Chrome 采用沙盒和多进程架构来隔离标签页，有效遏制恶意代码。通过自动更新、漏洞奖励计划、Site Isolation（站点隔离）以及集成安全浏览等服务，层层加固浏览器安全。近年来还利用本地机器学习模型实时检测网络钓鱼和恶意通知。
- 🧱 **稳固可靠**：多进程架构不仅提升了安全性，也极大地增强了稳定性——单个标签页的崩溃不会导致整个浏览器关闭。团队通过优化内存管理、淘汰问题插件（如 Flash）以及积极参与 Web 平台互操作性项目，确保浏览器和网络平台都能平稳运行。
- ✨ **简约哲学**：Chrome 以简洁、最小化的用户界面设计著称，突出网页内容本身。其 Omnibox（多功能地址栏）、智能建议和轻量级 UI 都旨在减少用户摩擦。扩展生态系统在提供强大定制能力的同时，也努力维持核心产品的简洁与安全。
- 🌐 **无处不在**：Chrome 从桌面迅速扩展到移动端（Android/iOS）和 ChromeOS，并通过同步功能实现跨设备无缝体验。它积极推动渐进式 Web 应用的发展，让 Web 应用能具备类似原生应用的能力，从而将 Web 打造为一个强大的应用平台。
- ⚙️ **推动平台进化**：通过“Project Fugu”等项目，Chrome 为 Web 引入了大量新 API（如文件系统访问、Web 蓝牙等），显著缩小了 Web 应用与原生应用的能力差距。同时，它通过开发者工具和丰富的文档积极支持开发者生态。
- 🤖 **AI 赋能新时代**：Chrome 正深度集成 AI 能力，例如通过 Gemini 模型提供智能标签页整理、AI 生成主题、写作辅助以及页面摘要等功能。它还向开发者提供了本地 AI API，让 Web 应用能利用设备端的模型能力，在增强功能的同时注重用户隐私。

---

### [npm 作者 Qix 因钓鱼邮件在重大供应链攻击中受侵](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

**原文标题**: [npm Author Qix Compromised via Phishing Email in Major Suppl...](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

恶意 NuGet 包通过仿冒流行的.NET 追踪库 Tracer.Fody，利用字形混淆技术窃取 Stratis 钱包的 JSON 文件与密码，并将数据外泄至俄罗斯 IP 地址。

- 🕵️ 恶意包“Tracer.Fody.NLog”通过仿冒合法库“Tracer.Fody”及其作者进行投毒攻击
- 🔠 使用同形异义字（homoglyph）技巧伪装包名，诱骗开发者下载
- 💰 专门针对 Stratis 钱包，窃取其 JSON 配置文件与密码信息
- 🌐 将窃取的数据外泄至位于俄罗斯的 IP 地址
- ⚠️ 突显软件供应链安全风险及依赖库验证的重要性

---

### [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

**原文标题**: [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

pnpm 10.16 版本引入了两项主要新功能以增强安全性及依赖管理灵活性，并包含多项问题修复。

- 🛡️ 新增 `minimumReleaseAge` 设置，可延迟安装新发布的依赖包（例如设为 1440 分钟即一天），以降低安装到被攻击的恶意包版本的风险，并可通过 `minimumReleaseAgeExclude` 排除特定包。
- 🔍 支持在 `.pnpmfile.cjs` 中定义“查找器函数”，使 `pnpm list` 和 `pnpm why` 命令能依据依赖包属性（如特定 peerDependencies）进行高级筛选，并支持在输出中返回自定义信息（如许可证）。
- 🐛 修复了在 Node.js 24 下执行时的弃用警告、`nodeVersion` 需为精确语义版本号的校验、`pnpm publish` 发布 `.tar.gz` 文件的能力，以及使用 Ctrl-C 取消进程后 `pnpm run` 应返回非零退出码的问题。

---

### [基于 Electron 的应用程序在 macOS 26 上引发全系统严重卡顿问题 · Issue #48311 · electron/electron · GitHub](https://github.com/electron/electron/issues/48311)

**原文标题**: [Electron-based apps cause a huge system-wide lag on macOS 26 · Issue #48311 · electron/electron · GitHub](https://github.com/electron/electron/issues/48311)

Electron 应用在 macOS 26 上引发系统级严重卡顿问题，用户报告在开启 Discord、VS Code 等基于 Electron 的应用时，即使 CPU 和 GPU 使用率低，窗口移动和滚动仍出现明显卡顿，且该问题在 macOS 15 中未出现。

- 🐛 **问题描述**：macOS 26 上 Electron 应用（如 Discord、VS Code）未最小化时，系统界面出现严重卡顿，影响窗口移动和滚动流畅度
- 🖥️ **系统环境**：macOS 26 Tahoe RC 系统，M1 Max 芯片设备，Electron 版本 37.3.1
- 🔍 **重现条件**：同时打开多个 Electron 应用时卡顿加剧，最小化应用后卡顿消失
- 🆚 **对比情况**：Chrome 浏览器未出现类似问题，macOS 15 系统无此现象
- 🐞 **问题状态**：已确认为 bug，维护者建议用户通过 Feedback Assistant 向苹果提交报告
- 📋 **处理进展**：问题已关闭，标签显示涉及 37-x-y 和 38-x-y 版本，归类为 macOS 平台性能问题

---

### [助我们筹集 20 万美元，让 JavaScript 摆脱 Oracle 的束缚 | Deno](https://deno.com/blog/javascript-tm-gofundme)

**原文标题**: [Help Us Raise $200k to Free JavaScript from Oracle | Deno](https://deno.com/blog/javascript-tm-gofundme)

Deno 公司发起法律行动，旨在通过美国专利商标局撤销 Oracle 对“JavaScript”商标的所有权，以使其成为公共领域术语，供开发者自由使用。目前案件进入关键证据收集阶段，需筹集 20 万美元用于法律费用，包括专业调查、专家证词及法律文件等。若胜诉，将确立商标法对通用名称的保护原则。

- 🏛️ Deno 向美国专利商标局提交撤销“JavaScript”商标的申请，案件进入证据收集阶段
- 💰 发起 20 万美元众筹，用于支付法律调查、专家证词及诉讼费用
- 📜 若胜诉，“JavaScript”将变为公共领域术语，开发者可自由使用
- ⚖️ Oracle 否认“JavaScript”为通用术语，案件结果将影响商标法对通用名称的保护原则
- 🌐 剩余资金将捐赠给 OpenJS 基金会，用于维护数字空间公民自由

---

### [React 编译器 v1.0 – React](https://react.dev/blog/2025/10/07/react-compiler-1)

**原文标题**: [React Compiler v1.0 – React](https://react.dev/blog/2025/10/07/react-compiler-1)

React Compiler 1.0 正式发布，这是一个构建时工具，通过自动记忆化优化 React 应用，无需重写代码即可提升性能。它兼容 React 17 及以上版本，并已集成到 Expo、Vite 和 Next.js 的新应用模板中。

- 🚀 **React Compiler 1.0 稳定版发布**：作为构建时优化工具，自动对组件和钩子进行记忆化，提升应用性能，无需手动重写代码。
- 🔧 **集成主流框架**：与 Expo、Vite 和 Next.js 合作，新应用默认启用编译器，支持渐进式采用。
- 📈 **生产环境验证**：在 Meta 等大型应用中测试，性能提升显著，如初始加载速度提升达 12%，交互响应提升 2.5 倍以上。
- 🛠️ **编译器工作原理**：通过高级中间表示（HIR）分析数据流和可变性，实现精细记忆化，甚至支持条件返回后的记忆化。
- 📚 **ESLint 规则增强**：通过 `eslint-plugin-react-hooks` 提供编译器驱动的 lint 规则，帮助检测违反 React 规则的问题。
- 🔄 **向后兼容性**：支持 React 17+，旧版本可通过配置和添加 `react-compiler-runtime` 使用。
- ⚡ **构建工具支持**：支持 Babel、Vite、Rsbuild，并与 swc 合作实验性集成，提升 Next.js 构建性能。
- 🧪 **记忆化控制**：编译器自动处理记忆化，但 `useMemo`/`useCallback` 仍可作为逃生舱口，用于精确控制效果依赖。
- 🚦 **升级建议**：建议遵循 React 规则并进行端到端测试，可固定编译器版本以确保升级稳定性。

---

### [Node.js — Node.js v25.0.0（当前版本）](https://nodejs.org/en/blog/release/v25.0.0)

**原文标题**: [Node.js — Node.js v25.0.0 (Current)](https://nodejs.org/en/blog/release/v25.0.0)

Node.js v25.0.0 正式发布，带来 V8 引擎升级、安全增强、多项 API 更新与废弃，以及性能优化。

- 🚀 V8 引擎升级至 14.1 版本，显著提升 JSON.stringify 性能，内置 Uint8Array 的 base64/hex 转换，并持续优化 WebAssembly 和 JIT 流水线
- 🔒 强化默认安全策略，权限模型新增 --allow-net 标志，默认启用 Web Storage，并将 ErrorEvent 设为全局对象
- 🗑️ 移除或终结多项长期弃用的 API，如 SlowBuffer、assert.fail 多参数调用、CallTracker 等
- ⚙️ 新增便携式编译缓存选项，支持 WebAssembly 的 JSPI（JavaScript Promise Integration），提升开发体验
- 📦 更新 npm 至 11.6.2 版本，并包含多项错误修复、测试更新和文档改进

---

### [Node.js 24 成为长期支持版本：你需要了解的关键信息](https://nodesource.com/blog/nodejs-24-becomes-lts)

**原文标题**: [Node.js 24 Becomes LTS: What You Need to Know](https://nodesource.com/blog/nodejs-24-becomes-lts)

Node.js 24 已进入长期支持（LTS）阶段，代号“Krypton”，将提供维护和安全更新至 2028 年 4 月。此版本增强了安全性、运行时验证和 Web API 支持，同时 N|Solid 6.0.2 已全面兼容该版本，为企业用户提供先进的监控和性能分析功能。

- 🔒 **安全性提升**：采用 OpenSSL 3.5，默认安全级别为 2，禁止使用弱密钥和 RC4 密码套件。
- 🛡️ **运行时验证加强**：多个 API（如 Buffer、fs.symlink）增加了严格的参数验证，帮助更早捕获错误。
- 🌐 **Web API 增强**：新增 CloseEvent、Float16Array 等全局对象，fetch() 实现更严格，提升与浏览器环境的互操作性。
- 📦 **模块系统优化**：ESM CommonJS 包装器默认导出 module.exports，改善 ESM 与 CommonJS 的互操作性。
- 🚀 **流和 Readline 改进**：增强 stream 错误传播和 readline 的 Unicode 支持，提升 I/O 稳定性和性能。
- 🔧 **编译要求更新**：构建 Node.js 需使用更新版本的编译器（如 GCC 12.2+、Xcode 16.1+），反映对现代 C++ 标准的支持。
- 🗑️ **API 清理**：移除了多个已弃用的 API 和内部绑定（如 util.is*()、tls.createSecurePair()），保持核心轻量安全。
- 💻 **平台支持调整**：停止提供 32 位 Windows 和 armv7 Linux 的预构建二进制文件，macOS 需 13.5 或更高版本。
- 🛠️ **N|Solid 全面兼容**：N|Solid 6.0.2 支持 Node.js 24 LTS，提供 gRPC 通信改进、OpenTelemetry 集成增强和持续性能分析。
- 📅 **长期支持策略**：NodeSource 继续支持所有活跃的 Node.js LTS 版本（包括 24、22、20），方便企业按需迁移。

---

### [介绍 React 基金会——React](https://react.dev/blog/2025/10/07/introducing-the-react-foundation)

**原文标题**: [Introducing the React Foundation – React](https://react.dev/blog/2025/10/07/introducing-the-react-foundation)

Meta 宣布将 React 和 React Native 从公司内部项目转移至新成立的 React 基金会，并建立独立的技术治理结构，以更好地服务社区和生态系统。

- 🏛️ React 基金会将成为 React、React Native 及 JSX 等项目的归属，负责基础设施维护、组织 React Conf 会议及资助生态项目
- 🤝 创始企业成员包括亚马逊、Callstack、Expo、Meta、微软、Software Mansion 和 Vercel，未来将吸纳更多成员
- 🧭 将建立独立于基金会的新技术治理结构，确保技术方向由贡献者共同决定，避免单一公司过度主导
- 🌱 此举旨在为 React 生态项目提供更多资源，巩固社区驱动的可持续发展模式

---

### [Bun 1.3 | Bun 博客](https://bun.sh/blog/bun-v1.3)

**原文标题**: [Bun 1.3 | Bun Blog](https://bun.sh/blog/bun-v1.3)

Bun 1.3 是迄今为止最大的版本更新，将 Bun 转变为一个功能全面的全栈 JavaScript 运行时。此版本引入了对前端开发的一流支持，包括内置的全栈开发服务器（支持热重载和浏览器到终端的控制台日志）、内置的 MySQL、PostgreSQL、SQLite 和 Redis 客户端，以及更好的路由、Cookie 和 WebSocket 支持。此外，还增强了包管理功能，如隔离安装、依赖目录和安全扫描，并改进了测试、调试、Node.js 兼容性和性能。

- 🚀 **全栈 JavaScript 运行时**：Bun 1.3 成为功能全面的全栈运行时，内置开发服务器、数据库客户端和 Redis 支持，支持前后端统一开发。
- 🌐 **前端开发增强**：可直接运行 HTML 文件，内置热模块替换（HMR）和 React Fast Refresh，生产构建通过 `bun build --production` 实现。
- 🔗 **全栈开发简化**：支持在同一服务器进程中运行前后端，简化 CORS 处理，新增参数化和通配符路由，并可编译为独立可执行文件。
- 🗄️ **数据库支持扩展**：Bun.SQL 统一支持 MySQL/MariaDB、PostgreSQL 和 SQLite，新增 `sql.array` 助手处理数组类型，PostgreSQL 客户端增强。
- 🔴 **内置 Redis 客户端**：提供高性能的 Redis（及 Valkey）客户端，支持标准操作、发布/订阅和自动重连，速度优于 ioredis。
- 🔧 **打包与构建改进**：支持通过 `Bun.build()` API 编程式创建可执行文件，新增代码签名、跨平台编译和更智能的代码压缩功能。
- 📦 **包管理功能升级**：引入依赖目录统一版本管理，默认启用隔离安装，支持从 yarn/pnpm 锁文件迁移，新增安全扫描 API 和最小发布时间要求。
- 🧪 **测试与调试优化**：VS Code Test Explorer 集成，支持并发测试和随机化测试顺序，新增 `expectTypeOf()` 类型测试和更丰富的匹配器。
- 📜 **API 与标准支持**：新增 YAML 解析、内置 Cookie API、`ReadableStream` 消费方法、WebSocket 压缩和 Zstandard 压缩支持。
- 🔒 **安全性增强**：引入 `Bun.secrets` API 用于加密凭证存储，提供 CSRF 保护工具，并大幅提升 Node.js crypto 模块性能。
- ⚙️ **Node.js 兼容性提升**：通过 800 多项 Node.js 测试，新增 `node:test`、`node:vm` 和 `require.extensions` 支持，改进 Worker 和核心模块。
- 🛠️ **开发者体验改善**：优化 TypeScript 默认配置，新增控制台深度控制、自定义 User-Agent 和预加载脚本支持，提升调试便利性。
- ⚡ **性能全面提升**：降低空闲 CPU 使用和内存占用，加速 `Bun.build`、Express/Fastify、`postMessage`、`Array.prototype.includes` 等操作。
- 🐛 **大量错误修复**：修复包管理器、运行时、打包器、测试运行器、内存泄漏、SQL、HTTP/TLS、CSS 解析器和 Windows 兼容性等方面的数百个问题。
- ⚠️ **重大变更说明**：`Bun.serve()` TypeScript 类型重构，默认 TypeScript 模块设置改为 `"Preserve"`，GC 信号在 Linux 上改为 SIGPWR，部分 API 行为调整。

---

### [Vite+ | VoidZero 发布公告](https://voidzero.dev/posts/announcing-vite-plus)

**原文标题**: [Announcing Vite+ | VoidZero](https://voidzero.dev/posts/announcing-vite-plus)

Vite+ 是一个基于 Vite 构建的统一 JavaScript 工具链，通过命令行提供项目脚手架、测试、代码检查、格式化、库打包、任务运行和图形化开发工具等一体化功能，旨在解决 JavaScript 工具生态的碎片化和性能瓶颈问题，尤其适合大型团队和复杂项目。它建立在 Rust 编写的共享基础设施上，性能优异，并兼容主流框架。Vite+ 将采用商业许可模式，但对个人、开源项目和小型企业免费，其底层开源项目（如 Vite、Vitest）将保持 MIT 许可不变。目前产品仍在开发中，计划于 2026 年初推出公开预览版。

- 🛠️ **一体化工具链**：Vite+ 是 Vite 的增强版，提供 `vite new`（项目脚手架）、`vite test`（单元测试）、`vite lint`（代码检查）、`vite fmt`（格式化）、`vite lib`（库打包）、`vite run`（任务运行器）和 `vite ui`（图形化工具）等命令，无需复杂配置即可协同工作。
- ⚡ **高性能基础**：整套工具链基于 Rust 构建，涵盖解析器、解析器、转换器、压缩器和打包器等环节，经过深度性能优化，已被 Framer、Linear 等公司广泛采用。
- 🧩 **生态兼容性**：继承 Vite 生态，兼容 React、Vue 等主流框架及全栈元框架（如 Tanstack Start、SvelteKit），并可与其他工具链配合使用。
- 🎯 **解决工具碎片化**：针对 JavaScript 工具生态长期存在的碎片化、配置复杂和性能瓶颈问题，为大型团队提供统一解决方案，减少工具选型和维护成本。
- 📜 **许可与可持续性**：Vite+ 采用商业许可，但对个人、开源项目和小型企业免费；底层开源项目（Vite、Vitest、Rolldown、Oxc）永久保持 MIT 许可，商业收入将反哺开源生态。
- 🚀 **开发与参与**：目前处于开发阶段，目标 2026 年初发布公开预览版，正在招募早期采用者进行生产环境测试，可通过官网联系参与。

---

### [Octoverse：每秒都有新开发者加入 GitHub，AI 引领 TypeScript 登顶榜首 - GitHub 博客](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

**原文标题**: [Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1 - The GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

GitHub 在 2025 年经历了创纪录的增长，AI 的普及推动了 TypeScript 首次成为平台最常用语言，开发者活动、开源贡献和全球开发者分布均呈现显著变化。

- 🚀 GitHub 开发者总数超过 1.8 亿，平均每秒新增一位开发者，年增长超 3600 万
- 🤖 AI 工具成为开发标配，80% 新用户首周使用 Copilot，AI 相关仓库数量翻倍
- 📈 TypeScript 超越 Python 和 JavaScript，首次成为 GitHub 最常用语言
- 🌍 印度成为最大开发者增长源，年增超 500 万，预计 2030 年占全球新开发者三分之一
- 🔧 开发者生产力大幅提升，代码推送、PR 合并和问题关闭数量均创历史新高
- 🛡️ 安全自动化加速，关键漏洞修复时间缩短 30%，Dependabot 使用量增长 137%
- 📊 开源贡献达 11.2 亿次，AI 基础设施项目成为增长最快领域
- 🌐 全球开发者分布更加多元化，巴西、印尼等新兴市场增长迅猛

---

### [GitLab 发现大规模 npm 供应链攻击](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

**原文标题**: [GitLab discovers widespread npm supply chain attack](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

最全面的 AI 驱动 DevSecOps 平台，提供一体化解决方案，助力开发与安全团队高效协作。

- 🛠️ 一体化平台：集成开发、安全与运维流程，实现全生命周期管理
- 🤖 AI 驱动：利用人工智能技术自动优化安全检测与漏洞修复
- 🔒 安全优先：将安全实践深度融入开发流程，提升应用防护能力
- ⚡ 高效协作：打破团队壁垒，促进开发与安全团队无缝配合
- 🌐 全面覆盖：支持从代码编写到部署运维的完整 DevSecOps 链条

---

### [JavaScript 引擎动物园](https://zoo.js.org/)

**原文标题**: [JavaScript engines zoo](https://zoo.js.org/)

该内容为一份开源 JavaScript 引擎的技术规格与项目元数据摘要。

- 🏗️ **引擎** - 核心执行环境名称
- 📊 **得分** - 性能或合规性量化指标
- 🔢 **二进制** - 编译产物格式
- 📏 **代码行数** - 项目规模统计
- 💬 **语言** - 实现所用编程语言
- ⚡ **即时编译** - 是否支持 JIT 优化
- 📅 **年限** - 项目维护时长
- 🎯 **目标平台** - 支持运行的环境
- 📜 **ES1-5** - ECMAScript 传统标准支持
- ✨ **ES6** - ECMAScript 2015 标准支持
- 🚀 **ES2016+** - 现代 ECMAScript 标准支持
- ⭐ **星标数** - 社区关注度指标
- 👥 **贡献者** - 项目协作人员数量
- 🏢 **组织** - 所属开发团队或机构
- 📄 **许可证** - 开源协议类型
- 📝 **描述** - 项目功能与定位说明

---

### [获取失败](https://javascriptweekly.com/link/178770/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/178770/web)

无法总结：获取内容失败，状态码 403。

---

### [JavaScript 周刊第 764 期：2025 年 12 月 5 日](https://javascriptweekly.com/issues/764)

**原文标题**: [JavaScript Weekly Issue 764: December 5, 2025](https://javascriptweekly.com/issues/764)

本期内容主要围绕 JavaScript 诞生 30 周年及相关技术动态展开，涵盖语言发展、企业工具、框架更新、安全实践及开发资源等多个方面。

- 🎉 JavaScript 迎来 30 周年纪念，回顾其诞生历程及当前在 Web、桌面、移动等多平台的核心地位
- 🔐 WorkOS 提供企业级身份验证与安全功能 API，帮助开发者快速集成 SSO、SCIM 等合规需求
- ⚡ TypeScript 7.0 进展中，将转向 Go 语言重写，预计性能提升 10 倍
- 🤖 Anthropic 收购 Bun 运行时，计划用于 Claude Code 智能开发工具，并承诺保持开源
- ⚠️ React 团队披露服务器组件安全漏洞，影响部分 Next.js 应用
- 🎄 多项编程挑战活动同步进行，包括 Advent of Code、AdventJS 与 Advent of Svelte
- 🛠️ 重要发布：Vite 8 Beta、Oxfmt 代码格式化工具、ESLint v10.0.0 Alpha 1
- 📖 安全实践：文章探讨 npm 发布流程加固与 JSDoc 替代 TypeScript 的类型方案
- 🐛 Wallaby 推出 AI 驱动调试工具，宣称比断点调试快 15 倍
- 📊 技术分析：对比 AWS Lambda 中 Arm 与 x86 架构性能、浏览器 Base64 处理速度
- 🎵 创意项目：利用 Web Audio API 实现无人机环境音合成器
- 📚 开发资源：涵盖 Angular 管道优化、Vue 组合函数测试、范畴论 JS 指南等深度文章
- 🔧 新工具：TanStack AI 统一 LLM 接口、Ruby2JS 转译器、Chokidar 文件监听库更新
- 📢 生态动态：包括 Spec Kit 驱动开发、Web 性能年度回顾、密码学图解指南等周边资讯

---

### [TypeScript 7 进展 - 2025 年 12 月 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

**原文标题**: [Progress on TypeScript 7 - December 2025 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

TypeScript 7.0（代号“Corsa”）的开发进展顺利，已进入预览阶段，其原生代码编译器与语言服务在性能和稳定性上均有显著提升，旨在为开发者带来更快的编译速度、更低的内存占用以及更流畅的编辑器体验。

- 🚀 **性能大幅提升**：原生编译器在完整构建中相比 TypeScript 6.0 有接近 10 倍的加速，并支持多线程并行构建项目。
- 🔧 **编辑器支持完善**：VS Code 扩展预览版已支持代码补全、自动导入、重命名等核心语言服务功能，日常使用稳定。
- 📦 **编译器功能就绪**：通过`@typescript/native-preview`包可体验新编译器，类型检查兼容性高，支持增量编译与项目引用。
- ⚠️ **需注意的变更**：TypeScript 7.0 将默认启用严格模式，移除部分已弃用配置（如`--target es5`），JavaScript 类型检查规则更严格。
- 🔄 **过渡与规划**：TypeScript 6.0 将是最后一个基于 JavaScript 的版本，作为向 7.0 过渡的桥梁，后续开发将聚焦于原生代码库。
- 🐛 **反馈与测试**：团队鼓励开发者尝试预览版并报告问题，以帮助完善最终版本。

---

### [Deno 2.6：dx 是新的 npx | Deno](https://deno.com/blog/v2.6)

**原文标题**: [Deno 2.6: dx is the new npx | Deno](https://deno.com/blog/v2.6)

Deno 2.6 版本引入了多项重要更新，包括新的 `dx` 工具用于便捷运行 npm 和 JSR 包二进制文件，更细粒度的权限控制，以及性能优化和 Node.js 兼容性改进。

- 🚀 新增 `dx` 工具，类似 `npx`，用于运行 npm 和 JSR 包的二进制文件，默认使用 `--allow-all` 权限并支持自动下载提示
- 🔒 引入更细粒度的权限控制，新增 `--ignore-read` 和 `--ignore-env` 标志，允许选择性忽略文件读取或环境变量访问
- ⚡ 集成实验性 TypeScript 类型检查器 `tsgo`，显著提升类型检查速度，并改进语言服务器功能
- 📦 支持 WebAssembly 源阶段导入，允许在构建时直接导入 Wasm 模块，提升效率
- 🔧 新增 `--require` 标志，支持运行 CommonJS 模块，增强 Node.js 兼容性
- 🛡️ 引入 `deno audit` 子命令，用于检查依赖中的安全漏洞，支持 GitHub CVE 数据库和 socket.dev 集成
- 📋 改进依赖管理，新增 `deno approve-scripts` 命令控制生命周期脚本，支持设置依赖最小年龄
- 🧩 增强打包器功能，支持 Web Workers 和外部依赖处理，改进 Node.js 兼容性
- 🔄 默认包含 `@types/node` 类型声明，提升 TypeScript 开发体验，并修复大量 Node.js API 问题
- 📈 性能优化，修复 `fetch` API 内存泄漏，优化 V8 引擎集成，提升 Node.js 兼容性操作速度
- 🛠️ 生活质量改进，包括动态任务补全、改进的堆栈跟踪、覆盖率报告增强等
- 🔧 升级至 V8 14.2 引擎，带来最新 JavaScript 功能和性能改进

---

### [Node.js — Node.js v24.12.0（长期支持版）](https://nodejs.org/en/blog/release/v24.12.0)

**原文标题**: [Node.js — Node.js v24.12.0 (LTS)](https://nodejs.org/en/blog/release/v24.12.0)

Node.js v24.12.0（代号“Krypton”）作为长期支持版本发布，包含多项新功能、性能优化、错误修复及依赖项更新，提升了模块系统、HTTP 处理、SQLite 集成、调试工具等方面的稳定性和效率。

- 🚀 **新增 HTTP 服务器选项**：添加`optimizeEmptyRequests`选项以优化空请求处理，提升服务器性能。
- 📦 **模块类型剥离功能稳定化**：将模块类型剥离标记为稳定功能，增强 ES 模块兼容性。
- 🔧 **Node-API 功能扩展**：新增`napi_create_object_with_properties`方法，简化对象创建流程。
- 🛡️ **SQLite 防御标志支持**：允许设置 SQLite 的防御标志，增强数据库操作安全性。
- ⚙️ **新增配置命名空间**：添加`watch`配置命名空间，改进文件监视功能。
- 📂 **编译缓存可移植性**：新增选项使编译缓存可跨环境移植，提升构建效率。
- 🔍 **调试器权限控制**：添加`--allow-inspector`选项，允许在权限模式下启用调试器。
- 📊 **V8 CPU 性能分析**：新增 CPU 性能分析功能，便于性能调优。
- 🐛 **多项错误修复与优化**：涵盖加密、控制台、调试器、流处理等模块，提升稳定性和性能。
- 🔄 **依赖项更新**：升级 V8 引擎、nghttp2、corepack 等依赖至新版本，引入功能改进和安全补丁。
- 📖 **文档完善与修正**：更新多个文档部分，修复链接错误并澄清功能描述。
- 🧪 **测试套件增强**：改进测试覆盖率，修复异步测试和断言问题，确保代码可靠性。

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=q4)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=q4)

Meticulous AI 是一款通过记录用户交互自动生成并维护端到端测试的工具，旨在帮助开发团队无需编写或维护测试代码即可实现全面覆盖，提升开发效率和代码质量。

- 🚀 **无需编写测试** – 通过记录开发、预演和生产环境中的用户交互，自动生成覆盖所有代码分支和用户流程的测试套件。
- 🔄 **自动维护与更新** – 测试套件随应用演进自动更新，新增功能或边缘案例会自动纳入测试，过时测试则被移除。
- ⚡ **快速无抖动测试** – 基于 Chromium 构建的确定性调度引擎，消除测试抖动，支持大规模并行测试，结果通常在 120 秒内返回。
- 🛡️ **安全无副作用** – 通过模拟后端响应进行测试，避免因数据变化导致的误报，无需设置测试账户或模拟数据。
- 🌐 **广泛集成支持** – 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流前端框架，可轻松集成到现有开发流程。
- 📈 **提升开发信心** – 已被 Dropbox、Notion、Lattice 等超过 100 家组织采用，帮助团队预防回归问题，加速可靠代码的交付。

---

### [Trigger.dev | 构建和部署全托管 AI 代理与工作流。](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=trigger.dev-december&utm_term=jsweekly&utm_content=homepage)

**原文标题**: [Trigger.dev | Build and deploy fully-managed AI agents and workflows.](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=trigger.dev-december&utm_term=jsweekly&utm_content=homepage)

Trigger.dev 宣布完成 1600 万美元 A 轮融资，这是一个用于在 TypeScript 中构建 AI 工作流和代理的平台，提供全托管、可扩展的解决方案，支持长时间运行的任务、重试、队列和实时监控。

- 🚀 Trigger.dev 完成 1600 万美元 A 轮融资，专注于构建全托管 AI 代理与工作流平台
- ⚙️ 提供基于 TypeScript 的 AI 工作流开发，支持长时间运行任务、自动重试、队列管理和弹性扩展
- 🔧 集成多样化功能：AI 任务、视频处理、定时任务、等待机制、并行处理、语义搜索等
- 🤖 支持复杂 AI 代理构建：包括自主代理、提示链、路由、并行化、协调器与评估优化器
- 🌐 无需管理服务器：提供无超时执行、按使用付费、多区域部署和自动扩展
- 🐛 内置高级调试：错误警报、运行过滤、版本控制、实时状态显示与流式响应传输
- 🔌 兼容现有技术栈：支持 Python、Prisma、Puppeteer、FFmpeg 等自定义扩展与集成
- 📈 受全球开发者信赖：已被多家公司用于关键业务场景，提升开发效率与系统可靠性
- 💰 提供灵活定价：按需付费、免费起步选项，并支持开源自托管部署

---

