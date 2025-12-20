### [JavaScript周刊第766期：2025年12月19日](https://javascriptweekly.com/issues/766)

**原文标题**: [JavaScript Weekly Issue 766: December 19, 2025](https://javascriptweekly.com/issues/766)

这是2025年最后一期《JavaScript周刊》，包含年度回顾、重要新闻和未来展望。

- 🗓️ 本期是2025年最后一刊，明年起将于每周二发布，下一期将于2026年1月6日回归。
- 📦 文章探讨了JavaScript打包工具领域的现状，指出竞争焦点已从速度转向代码包体积优化。
- 🤖 介绍了如何将AI实际应用于JavaScript开发工作流，包括提示工程和构建生产级应用。
- ⚡ Simon Willison分享了他使用AI工具在4.5小时内将HTML5解析器从Python移植到JavaScript的经历。
- 🛠️ 简讯部分包含Dan Abramov的新工具、Cloudflare Wrangler的更新、新的拖放库以及OpenAI GPT 5.2 Codex的发布。
- 🚀 发布了多个重要库和框架的新版本，如Tesseract.js 7.0、Base UI 1.0、Wasp 0.20等。
- 🏆 列出了2025年最受欢迎的10篇文章，涵盖JavaScript谜题、ES2025新特性、生成器函数实用指南、Web JavaScript使用现状等主题。
- 📅 按月回顾了2025年JavaScript生态的重大事件，包括Bun、Deno、TypeScript、React、Node.js等关键项目的更新和行业动态。
- 🎄 在分类广告和结语中，推广了开发者工具，并感谢读者一年的支持，预告了2026年的回归。

---

### [JavaScript打包器大赛——console.log()](https://redmonk.com/kholterhoff/2025/12/16/javascript-bundler-grand-prix/)

**原文标题**: [The JavaScript Bundler Grand Prix – console.log()](https://redmonk.com/kholterhoff/2025/12/16/javascript-bundler-grand-prix/)

JavaScript打包工具领域正经历一场速度竞赛，各大公司投入巨资优化构建性能，但真正的挑战可能已从开发体验转向用户体验，即如何减少代码体积、提升运行时效率。

- 🚀 **速度竞赛白热化**：Vercel、VoidZero、字节跳动等公司竞相推出高性能打包工具（如Turbopack、Rolldown、Rspack），通过Rust/Go等语言重写实现构建速度的大幅提升。
- ⚖️ **性能基准模糊化**：厂商频繁发布提速数据（如“构建快5-10倍”），但实际效果因项目差异巨大，且工具迭代迅速，难以判定绝对赢家。
- 🧩 **生态格局多元化**：从老牌工具Webpack、Rollup到现代方案Vite、Bun，打包工具呈现社区项目与商业产品并存的局面，共同应对JavaScript依赖膨胀的挑战。
- 🔍 **核心矛盾转移**：专家指出，当构建时间缩短至“1分钟vs30秒”时，速度优化已触及收益递减点，真正的战场应转向产物体积优化和消除未使用代码。
- 🤝 **工具协作深化**：未来打包工具需与编译器（如SWC）深度集成，实现跨模块分析，从根本上解决“半数代码未使用”的行业痛点。
- 🏁 **竞赛本质演变**：行业正从单纯追求构建速度，转向关注开发者体验的可持续性、产物精简度，以及最终用户的页面加载性能。

---

### [捆绑器 - Bun](https://bun.com/docs/bundler)

**原文标题**: [Bundler - Bun](https://bun.com/docs/bundler)

Bun 是一个快速的本地打包工具，支持 JavaScript、TypeScript、JSX 等多种文件类型，可通过 CLI 命令或 JavaScript API 使用。它旨在减少 HTTP 请求、转换代码（如 TypeScript 和 JSX）、支持框架特性，并处理全栈应用程序的打包需求。Bun 打包器默认生成 ES 模块格式，支持代码分割、插件系统、环境变量注入、源映射生成和多种优化选项，同时提供监视模式和独立可执行文件生成功能。

- 🚀 **快速打包**：Bun 打包器性能优异，在 esbuild 的 three.js 基准测试中表现突出。
- 📦 **减少 HTTP 请求**：通过将多个文件合并为少量自包含的包，优化网络加载性能。
- 🔧 **代码转换**：内置支持 TypeScript、JSX、CSS 模块等，自动转换为纯 JavaScript 和 CSS。
- 🏗️ **框架支持**：通过插件和代码转换实现文件系统路由、客户端-服务器代码共置等框架特性。
- 🌐 **全栈应用**：可同时处理服务器和客户端代码，支持生产构建优化和单文件可执行文件生成。
- ⚙️ **灵活配置**：支持多种目标环境（浏览器、Bun、Node.js）、模块格式（ESM、CJS、IIFE）和代码分割选项。
- 🔌 **插件系统**：允许通过插件扩展或覆盖默认行为，增强打包灵活性。
- 🔍 **监视模式**：原生支持监视文件变化并增量重建，提升开发效率。
- 📄 **多文件类型**：支持 .js、.ts、.json、.css、.html 等多种扩展名，并可将未知文件类型作为外部资源处理。
- 🛠️ **高级功能**：包括环境变量注入、源映射生成、代码压缩、外部依赖排除和自定义文件命名等。

---

### [AI编程学习路径 - 掌握软件开发的未来 | Frontend Masters](https://frontendmasters.com/learn/ai/?utm_source=email&utm_medium=javascriptweekly&utm_content=learnai)

**原文标题**: [Coding with AI Learning Path - Master the Future of Software Development | Frontend Masters](https://frontendmasters.com/learn/ai/?utm_source=email&utm_medium=javascriptweekly&utm_content=learnai)

掌握AI辅助软件开发的未来，通过实践学习将生成式内容集成到应用程序中。

- 🚀 掌握AI辅助工程工作流程
- ⏱️ 总学习时长23小时47分钟
- 🎯 获得生成式内容集成实践经验
- 📊 当前学习进度0%

---

### [我用Codex CLI和GPT-5.2在4.5小时内将JustHTML从Python移植到JavaScript。](https://simonwillison.net/2025/Dec/15/porting-justhtml/)

**原文标题**: [I ported JustHTML from Python to JavaScript with Codex CLI and GPT-5.2 in 4.5 hours](https://simonwillison.net/2025/Dec/15/porting-justhtml/)

作者使用Codex CLI和GPT-5.2，在4.5小时内将JustHTML从Python移植到JavaScript，创建了一个通过9200项测试、无依赖的JavaScript HTML5解析库，整个过程仅需少量提示，并在处理期间兼顾了家庭活动，引发了关于AI辅助开发在伦理、法律及开源生态方面影响的思考。

- 🚀 作者利用Codex CLI和GPT-5.2，仅通过两个初始提示和少量跟进，在约4.5小时内成功将Python的JustHTML库移植到JavaScript，创建了simonw/justjshtml。
- 📊 新库通过了html5lib-tests测试套件中的9200项测试，实现了无依赖的HTML5解析功能，并模仿了原Python库的API设计。
- ⏱️ 整个移植过程基本自动化，GPT-5.2消耗了约160万输入token和62.5万输出token，生成了9000行JavaScript代码，期间作者还进行了购买圣诞树等家庭活动。
- 🔧 作者通过设置里程碑（如Milestone 0.5）和持续集成（GitHub Actions），引导AI逐步完成库的构建、测试和文档编写。
- 🌐 项目最终包括了一个浏览器可用的交互式playground界面，并部署在GitHub Pages上，方便用户直接体验。
- 💡 实验展示了前沿LLM能够执行复杂、长时间的任务，并在拥有健全测试套件的问题上高效工作，突显了“设计智能体循环”的重要性。
- ⚖️ 作者提出了关于AI生成代码的伦理、法律（如版权问题）及对开源生态影响的开放性问题，反思了这种开发方式的合理性与责任。

---

### [GitHub - html5lib/html5lib-tests：html5lib的测试套件数据，包含事实上的标准HTML解析测试。](https://github.com/html5lib/html5lib-tests)

**原文标题**: [GitHub - html5lib/html5lib-tests: Testsuite data for html5lib, including the de-facto standard HTML parsing tests.](https://github.com/html5lib/html5lib-tests)

这是一个用于html5lib的测试套件数据仓库，包含事实标准的HTML解析测试。

- 📚 **测试套件**：为html5lib提供测试数据，包含事实标准的HTML解析测试。
- ⭐ **项目热度**：获得237个星标和63个分支，显示社区关注度。
- 🛠️ **代码管理**：包含多个测试模块，如编码、序列化、分词器和树构建等。
- 📄 **许可证**：采用MIT许可证，允许自由使用、修改和分发。
- 🔄 **活跃维护**：有29个未解决的问题和9个拉取请求，显示项目仍在积极开发中。
- 👥 **贡献者**：由36位主要贡献者和22位其他贡献者共同维护。

---

### [JustJSHTML 游乐场 - HTML5 解析器](https://simonw.github.io/justjshtml/playground.html)

**原文标题**: [JustJSHTML Playground - HTML5 Parser](https://simonw.github.io/justjshtml/playground.html)

JustJSHTML是一个无需依赖的HTML5解析器，旨在通过完整的官方html5lib测试套件，提供CSS选择器、树遍历和美化打印功能。

- 🌐 无需依赖的HTML5解析器
- ✅ 通过完整的html5lib官方测试套件
- 🎯 支持CSS选择器功能
- 🌳 提供树遍历能力
- 🖨️ 包含美化打印功能

---

### [GitHub - simonw/justjshtml: EmilStenstrom/justhtml 的 JavaScript 移植版](https://github.com/simonw/justjshtml)

**原文标题**: [GitHub - simonw/justjshtml: JavaScript port of EmilStenstrom/justhtml](https://github.com/simonw/justjshtml)

这是一个名为justjshtml的JavaScript库，它是Python项目JustHTML的无依赖JavaScript移植版本，用于在浏览器和Node.js环境中解析HTML5。

- 🚀 **项目目标**：通过完整的html5lib-tests套件（包括分词器、树构建、编码和序列化测试），仅使用纯JavaScript实现。
- ⚙️ **技术特性**：无运行时依赖，支持现代浏览器（ES模块）和Node.js（ESM），测试通过率高。
- 📦 **快速开始**：提供Node.js和浏览器的简单使用示例，支持字符串或字节输入，并包含丰富的配置选项。
- 🔧 **API功能**：提供节点操作、CSS选择器查询、流式解析和独立辅助函数，节点对象具有类DOM的API。
- 🛠️ **开发过程**：基于测试驱动开发，使用OpenAI Codex CLI和GPT-5.2在4.5小时内完成移植，并包含完整的测试工作流。
- 🌐 **互动工具**：提供在线和本地的交互式playground，方便用户实时测试HTML解析功能。
- 📚 **致谢与资源**：项目基于Emil Stenström的JustHTML和html5lib-tests，架构受html5ever影响，UI改编自Simon Willison的playground。

---

### [介绍RSC Explorer — 过度解读](https://overreacted.io/introducing-rsc-explorer/)

**原文标题**: [Introducing RSC Explorer — overreacted](https://overreacted.io/introducing-rsc-explorer/)

React Server Components（RSC）协议是React用于序列化和反序列化组件树的内部格式，通常未公开文档。近期因安全漏洞披露，社区对其兴趣增加。作者为此开发了RSC Explorer工具，这是一个在浏览器中模拟RSC协议交互的单页应用，帮助开发者直观理解RSC的工作原理，包括流式渲染、客户端与服务器代码交互、状态保持等机制，并提供了多个示例和开源代码。

- 🔍 RSC协议是React内部用于序列化组件树的格式，缺乏公开文档，但近期因安全漏洞受到关注
- 🛠️ 作者开发了RSC Explorer工具，在浏览器中模拟RSC交互，无需网络请求即可演示协议流程
- 🌐 工具展示了JSX如何通过网络传输并在客户端重建，以及流式渲染中Suspense处理异步组件的机制
- ⚙️ 示例包括计数器组件传输虚拟DOM而非HTML、服务器动作与客户端表单交互，以及无框架路由刷新实现
- 🔄 通过Router示例说明服务器如何向客户端传递新属性并保持组件状态，类似虚拟DOM更新
- 📚 工具提供分页、错误处理、客户端引用等更多示例，并支持嵌入代码片段和社区共享
- 🔓 包含安全漏洞CVE-2025-55182的演示，需切换至受影响版本才能运行
- 💡 RSC Explorer完全开源，旨在通过可视化方式降低理解RSC底层机制的门槛

---

### [自动为Cloudflare配置您的框架·更新日志](https://developers.cloudflare.com/changelog/2025-12-16-wrangler-autoconfig/)

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

picknplace.js 是一种替代拖放操作的交互方案，通过“选取-滚动-放置”三步简化操作流程，尤其优化了移动端体验。

- 🖱️ **操作步骤简化**：采用“选取 → 滚动 → 放置”三步流程，支持用 Enter 键确认放置、Esc 键取消操作
- 📱 **移动端优化**：针对触屏设备改进交互，避免传统拖放中同时进行点击、长按、拖动和滚动的繁琐操作
- 🔄 **动态视觉反馈**：选取项目时会生成动画化副本列表，随滚动位置实时更新，提供直观的视觉引导
- 🎯 **操作可控性**：用户可在最终步骤确认或取消所有更改，降低误操作风险
- 💡 **概念验证性质**：当前版本为交互设计的概念演示，开发者可参考源码获取灵感
- 👨💻 **创作者背景**：由前端设计师 @jgthms 开发，可通过 Twitter 和 Github 关注其动态

---

### [介绍GPT-5.2-Codex | OpenAI](https://openai.com/index/introducing-gpt-5-2-codex/)

**原文标题**: [Introducing GPT-5.2-Codex | OpenAI](https://openai.com/index/introducing-gpt-5-2-codex/)

OpenAI发布了GPT-5.2-Codex，这是目前最先进的代理式编码模型，专为复杂现实世界的软件工程和防御性网络安全设计。该模型在长上下文理解、工具调用可靠性和事实准确性方面有显著提升，同时增强了在Windows环境下的性能与网络安全能力。发布采取分阶段策略，结合安全措施，并针对网络安全专业人员推出受信任访问试点计划。

- 🚀 GPT-5.2-Codex针对代理式编码优化，提升长时任务处理、大型代码重构与迁移能力，并在Windows环境中表现更佳
- 🔐 网络安全能力显著增强，可加速漏洞研究与防御工作，但需谨慎部署以应对双重用途风险
- 📊 在SWE-Bench Pro和Terminal-Bench 2.0基准测试中达到最先进水平，能有效处理大型代码库与复杂工程任务
- 🛡️ 新增安全防护措施，并基于预备框架评估，为未来可能达到“高”级别网络能力做准备
- 👥 已向付费ChatGPT用户开放，即将逐步开放API访问，并推出针对网络安全专业人士的受信任访问试点计划
- 💡 实际案例显示，前代模型曾协助安全研究人员发现React漏洞，体现AI在防御性安全工作中的加速作用
- 🌐 通过渐进式部署、安全措施与行业合作，旨在最大化防御效益，同时降低技术滥用风险

---

### [Tesseract.js | 纯JavaScript OCR支持100种语言！](https://tesseract.projectnaptha.com/)

**原文标题**: [Tesseract.js | Pure Javascript OCR for 100 Languages!](https://tesseract.projectnaptha.com/)

Tesseract.js 是一个纯JavaScript的多语言OCR库，支持超过100种语言，可在浏览器和Node.js环境中运行，提供文本方向检测和边界框识别功能。

- 🌐 纯JavaScript OCR引擎，支持100多种语言
- 🔄 自动检测文本方向和脚本
- 📦 提供段落、单词和字符边界框的简单接口
- 🌍 可在浏览器和Node.js服务器端运行
- 📚 示例代码和API文档可在GitHub查看
- 🖼️ 提供英文、中文和俄文演示页面
- 📄 支持上传图像文件进行文本识别

---

### [基础UI](https://base-ui.com/)

**原文标题**: [Base UI](https://base-ui.com/)

Base UI 是一个由 Radix、Floating UI 和 Material UI 的创建者开发的 React UI 组件库，专注于构建可访问、灵活且持久的用户界面，其设计强调可组合性、一致性和细节工艺，不强制视觉风格，旨在为专业界面设计提供未来可靠的基础。

- 🧩 由知名 UI 库创作者打造，专注于 React 的可访问组件库
- 🛠️ 组件设计强调可组合性、一致性和工艺细节，提供高度灵活性
- 🎨 不强制视觉风格，支持团队打造独特且可访问的界面
- ⏳ 基于多年经验构建，旨在提供持久、未来可靠的界面设计基础
- 👥 专为创作者设计，由经验丰富的设计和工程团队支持
- ❓ 提供常见问题解答，涵盖兼容性、可访问性、商业使用等细节

---

### [黄蜂圣诞发射 - React 19、Claude代码插件、Polar！🎄🎁 | Wasp](https://wasp.sh/blog/2025/12/17/wasp-xmas-launch)

**原文标题**: [Wasp Xmas Launch - React 19, Claude Code Plugin, Polar! 🎄🎁 | Wasp](https://wasp.sh/blog/2025/12/17/wasp-xmas-launch)

Wasp 将于12月23日提前发布四项新功能作为圣诞礼物，并举办线上庆祝活动。

- 🎁 支持 React 19，提供新 Actions、表单 API 和钩子等功能
- 🤖 推出官方 Claude Code 插件，让 AI 辅助开发更懂 Wasp
- 🐻‍❄️ 在 Open SaaS 中集成开源支付平台 Polar，简化 SaaS 计费
- 📰 新增 `wasp news` CLI 命令，直接在终端获取更新和提示

---

### [发布 7.4.0 版本 · graffle-js/graffle · GitHub](https://github.com/graffle-js/graffle/releases/tag/7.4.0)

**原文标题**: [Release 7.4.0 · graffle-js/graffle · GitHub](https://github.com/graffle-js/graffle/releases/tag/7.4.0)

这是一个关于GraphQL客户端库Graffle的GitHub仓库页面，主要展示了其最新版本7.4.0的发布信息。

- 🚀 **版本7.4.0发布**：于12月15日由jasonkuhrt发布，最新提交为9b8714c。
- ✨ **新增功能**：在`GraphQLResponse`和`GraphQLClientResponse`类型中公开了响应头（`headers`）和响应体（`body`）属性，便于访问非GraphQL响应数据（例如返回纯JSON的401/403/503错误）。
- 👥 **贡献者**：此功能由@adambrgmn贡献（PR #1476）。
- 📊 **项目概况**：该仓库拥有6.1k星标、310个分支和43个议题，是一个活跃的开源项目。

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

### [一个令人困惑的JavaScript解析谜题](https://www.hillelwayne.com/post/javascript-puzzle/)

**原文标题**: [A Perplexing Javascript Parsing Puzzle](https://www.hillelwayne.com/post/javascript-puzzle/)

这篇文章探讨了JavaScript中一个令人困惑的解析现象：代码`x = 1 x --> 0`在控制台中输出`1`，并解释了其历史原因和技术细节。

- 🧩 代码`x = 1 x --> 0`在JavaScript控制台中输出`1`，因为`-->`在行首时被解析为注释起始符
- 📜 这一行为源于早期Web的兼容性需求，当时为兼容不支持`<script>`标签的旧浏览器，开发者使用HTML注释包裹脚本代码
- 🏛️ 为确保向后兼容，`<!--`和`-->`作为合法注释标记被纳入ECMAScript 2015标准，其中`-->`仅在行首有效
- 🌐 现代浏览器均支持此语法，Node.js和Electron等基于V8引擎的环境也继承这一特性
- 🔧 这一设计体现了Web标准“永不破坏现有网站”的原则，即使它现在看起来像是一种历史遗留的“黑客”行为

---

### [Ecma国际批准ECMAScript 2025：有哪些新特性？](https://2ality.com/2025/06/ecmascript-2025.html)

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

Macroscope现为符合条件的非商业开源项目提供免费AI代码审查服务，旨在帮助开源社区减少错误、提升代码审查效率并增强项目可见性。

- 🆓 **免费开放**：符合资格的非商业开源项目可免费使用Macroscope的AI代码审查功能。
- 🐛 **高效查错**：在代码审查基准测试中，Macroscope对100多个真实生产环境错误的检出率最高。
- ⚙️ **解决痛点**：针对开源社区常见问题，如减少代码错误、降低管理负担、跟踪项目贡献状态等提供解决方案。
- 📋 **资格要求**：项目需使用开源许可证、非商业用途、并在GitHub上公开。
- 🤝 **赞助机会**：Macroscope寻求赞助优秀的开源项目，可通过指定渠道推荐。
- 🚀 **快速启动**：符合条件者可申请免费使用，其他用户可享受两周免费试用。

---

### [我想发电机的工效学设计正逐渐吸引我。 | 亚历克斯·麦克阿瑟](https://macarthur.me/posts/generators/)

**原文标题**: [I think the ergonomics of generators is growing on me. | Alex MacArthur](https://macarthur.me/posts/generators/)

作者分享了对JavaScript生成器（generators）从陌生到逐渐欣赏的心路历程，探讨了生成器在迭代协议、惰性求值、解耦代码、异步处理及分页优化等方面的实用价值。

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

本文分析了2024年JavaScript在网页中的使用现状、趋势及其对性能的影响，并提供了优化建议。

- 📈 **JavaScript体积持续增长**：2024年移动端中位JavaScript负载达558KB，桌面端达613KB，较去年增长14%，对设备资源造成更大压力。
- 📊 **请求数量稳步上升**：移动端中位JavaScript请求达22个，90分位数达68个，增加请求可能引发主线程资源竞争，影响性能。
- 🗑️ **未使用代码问题显著**：约44%的下载JavaScript字节在页面加载时未被使用，移动端中位未使用字节达206KB。
- 🛠️ **打包与转译工具使用稳定**：webpack使用率保持在5%，但顶级网站使用率下降；Babel在顶级移动网站中使用率达12%，TypeScript使用率约6%。
- ⚡ **异步加载成为主流**：`async`属性使用率从2022年的76%增至87%，`defer`使用率从42%微增至47%，`module`使用率仍较低（4%）。
- 🔗 **资源提示使用变化**：`preload`使用率从16.4%降至7.5%，`prefetch`从约1%增至4.8%，`modulepreload`使用率极低（约0.7%）。
- 🌐 **第三方脚本占比增加**：90分位数下第三方JavaScript请求从34个增至36个，可能带来性能、安全与隐私风险。
- 🔄 **动态导入与Web Workers使用增长**：动态导入使用率从0.34%增至3.70%；Web Workers使用率从12%增至30%，有助于提升性能。
- 🗜️ **Brotli压缩成为主流**：Brotli使用率达45%，首次超过gzip（41%），但第三方脚本中gzip仍占主导（60%）。
- ✂️ **代码压缩仍有优化空间**：38%的移动页面存在未压缩JavaScript，中位页面可压缩约12KB，主要问题来自第一方代码（占浪费字节的82.7%）。
- 🐌 **响应性能问题突出**：移动端90分位数INP达275ms，超出“良好”阈值；TBT在移动端90分位数达5.95秒，长任务时间中位值达2.37秒。
- 🏗️ **jQuery仍占主导地位**：使用率达74%，核心库组合中jQuery相关占多数；React使用率微增至10%，Web Components使用率有所增长。
- 📉 **遗留问题依然存在**：2.15%的移动页面仍使用同步XHR，12%使用`document.write`，67%的页面仍包含不必要的老旧JavaScript转换。

---

### [每位JavaScript开发者2025年都应了解的一些特性 | WaspDev博客](https://waspdev.com/articles/2025-04-06/features-that-every-js-developer-must-know-in-2025)

**原文标题**: [Some features that every JavaScript developer should know in 2025 | WaspDev Blog](https://waspdev.com/articles/2025-04-06/features-that-every-js-developer-must-know-in-2025)

JavaScript 持续演进，2025年开发者应掌握一些关键特性以提升代码效率和现代性，包括迭代器助手、数组at()方法、Promise.withResolvers()等新功能，以及一些可能被忽视的实用技巧如变量交换和结构化克隆。

- 🔄 **迭代器助手**：提供类似数组方法的高效迭代器操作（如drop、take、filter），避免链式转换中的临时数组分配，提升大数组处理性能。
- 🔢 **数组at()方法**：支持正负索引访问数组元素，简化如`arr[arr.length - 1]`的代码，更直观获取末尾元素。
- 🤝 **Promise.withResolvers()**：简化Promise解析器的创建，替代冗长的`new Promise`模式，使代码更简洁。
- 🔧 **字符串替换回调**：`replace()`和`replaceAll()`支持回调函数，允许单次遍历进行复杂替换，提升性能和灵活性。
- 🔄 **变量交换**：使用解构赋值`[a, b] = [b, a]`交换变量，避免临时变量，代码更优雅。
- 🧬 **structuredClone()**：提供深拷贝对象的标准API，正确处理循环引用和特殊值（如NaN、undefined），优于`JSON.stringify/parse`。
- 🏷️ **标签模板**：允许函数解析模板字面量，用于自动转义或处理插值，增强字符串处理能力。
- 🗑️ **WeakMap/WeakSet**：弱引用集合，允许对象作为键且不影响垃圾回收，适用于无副作用的对象关联场景。
- ⚙️ **集合操作**：Set新增方法（如difference、intersection、union），支持布尔运算，简化集合处理逻辑。

---

### [如何有效管理package.json | Val Town博客](https://blog.val.town/gardening-dependencies)

**原文标题**: [How to keep package.json under control | Val Town Blog](https://blog.val.town/gardening-dependencies)

Val Town作为一个复杂的React应用，依赖管理至关重要。尽管node_modules体积庞大，但许多依赖是构建功能所必需的。作者分享了一套依赖管理的最佳实践，旨在保持项目的简洁与高效。

- 📖 **仔细阅读新依赖的源码和文档**：除了React等大型依赖外，建议亲自阅读代码，避免引入不必要的复杂性和安全风险。
- 🔍 **利用包管理器工具分析依赖树**：通过`npm ls`或`pnpm why`等命令了解直接和传递性依赖，发现可复用的模块以减少冗余。
- 📊 **评估包的实际大小影响**：使用磁盘空间分析工具（如Grand Perspective）和打包分析工具（如rollup-plugin-visualizer）分别监控开发和生产环境的体积。
- ✅ **选择高质量模块的标准**：关注维护历史、TypeScript支持、测试覆盖和文档完整性，避免使用已废弃或与问题不匹配的模块。
- 🧹 **定期清理未使用的依赖**：借助Renovate保持依赖更新，使用Knip快速识别并移除package.json中的无用模块。
- 👥 **关注优秀模块作者**：建立常用可靠开发者的清单（如Sindre Sorhus、Rich Harris等），以便快速找到高质量解决方案。
- 🌱 **接受依赖管理的必然性**：依赖生态快速迭代是常态，主动维护依赖是开发工作的重要组成部分，需以积极态度应对。

---

### [JavaScript简史 | Deno](https://deno.com/blog/history-of-javascript)

**原文标题**: [A brief history of JavaScript | Deno](https://deno.com/blog/history-of-javascript)

JavaScript 诞生30周年，从最初为网页添加交互性的脚本语言，发展成为当今最流行的编程语言，支撑着从浏览器到服务器、桌面应用乃至太空探索的广泛领域。其发展历程见证了开源社区的力量、技术标准的演进以及生态系统的持续创新。

- 🚀 **1995年诞生**：Brendan Eich 在10天内为 Netscape 创造了 JavaScript，旨在为静态网页添加动态功能，并因 Java 的热度而得名。
- 🌐 **1996-1997年标准化**：为避免浏览器生态分裂，JavaScript 被提交给 ECMA International，形成了 ECMAScript 标准，并由 TC39 委员会维护其发展。
- ⚔️ **浏览器战争**：微软推出 JScript 与 Netscape 竞争，而 Netscape 开源其浏览器代码催生了 Mozilla 项目及后来的 Firefox。
- 🔄 **2000年代技术革新**：AJAX（2004年）的普及带来了 Web 2.0 时代，jQuery（2006年）简化了跨浏览器开发，Node.js（2009年）让 JavaScript 走向服务器端。
- 📦 **模块化与工具生态**：CommonJS、npm（2010年）和 Babel（2014年）等工具推动了代码共享和现代开发流程，ES6（2015年）引入了类、模块等关键特性。
- ⚛️ **框架崛起**：AngularJS、React（2013年）、Vue.js（2014年）等框架重塑了前端开发模式，促进了单页应用（SPA）的流行。
- 🛠️ **全栈与跨平台**：Express.js、MongoDB 等形成了 MEAN 栈，Electron（2013年）使得用 Web 技术构建桌面应用成为可能。
- 🚀 **性能与运行时演进**：V8 引擎（2008年）提升了执行速度，WebAssembly（2015年）为高性能计算铺路，Deno（2020年）和 Bun（2023年）等新兴运行时不断涌现。
- 🔧 **开发体验提升**：TypeScript（2012年）提供了静态类型，ESLint、Prettier 等工具优化了代码质量与格式，VS Code（2016年）成为主流编辑器。
- ☁️ **云与边缘计算**：AWS Lambda（2014年）、Cloudflare Workers（2017年）推动了无服务器和边缘计算的发展。
- 📜 **持续标准化**：ECMAScript 每年更新，加入如 async/await、ES 模块等特性，TC39 通过开放流程推动语言演进。
- ⚖️ **生态治理与挑战**：OpenJS Foundation 成立（2019年）整合了 JavaScript 与 Node.js 生态，npm leftpad 事件（2016年）暴露了供应链安全问题，Oracle 对 JavaScript 商标的争议仍在持续。
- 🚀 **未来展望**：JavaScript 在太空（SpaceX Dragon，2020年）、AI 工具链和更快的运行时（如 tsgo）中继续拓展边界，社区致力于更开放、高性能的下一代 Web 开发。

---

### [战争故事：我调试过的最棘手的漏洞](https://www.clientserver.dev/p/war-story-the-hardest-bug-i-ever)

**原文标题**: [War story: the hardest bug I ever debugged](https://www.clientserver.dev/p/war-story-the-hardest-bug-i-ever)

作者在Google Docs团队工作时，遇到一个难以复现的Chrome专属致命错误，通过两天艰苦调试，最终发现是V8引擎优化层级的Math.abs()函数错误返回负值导致的罕见Bug。

- 🐛 **突发错误**：Google Docs突然出现大量致命错误，仅影响特定Chrome版本，但用户投诉未激增
- 🔍 **艰难复现**：通过自动化脚本反复加粗/取消加粗50页文档，在第10-40次操作间随机触发这个非确定性Bug
- 🖥️ **复杂架构**：当时Google Docs使用自定义布局引擎，所有屏幕元素绝对定位，依赖大量缓存保证性能
- 🧩 **错误传播**：问题根源在于视图层的记账代码错误，但实际崩溃发生在错误值被缓存并传递到下游后
- 👥 **协作调试**：作者与精通视图层的同事合作，花两天时间逐步回溯断点，定位问题区域
- 🤯 **惊人发现**：Math.abs()函数在特定条件下对负输入返回负值，经技术主管确认后确认为V8引擎Bug
- 🔗 **内部协调**：通过Google内部渠道联系V8团队，发现该问题已在修复状态但尚未部署
- ⚙️ **根源分析**：V8引擎重构优化层时，有人误将Math.abs()在超级优化层级实现为恒等函数
- 🩹 **临时方案**：添加特定Chrome版本检查，手动实现绝对值计算，并添加详细注释说明原因
- 🎯 **无奈结局**：花费两天调试的问题其实已被修复，除了展示调试的艰辛外没有明确的教学意义

---

### [人们对Electron的常见误解](https://felixrieseberg.com/things-people-get-wrong-about-electron/)

**原文标题**: [Things people get wrong about Electron](https://felixrieseberg.com/things-people-get-wrong-about-electron/)

Electron框架的核心理念在于利用Web技术构建跨平台桌面应用，并通过捆绑Chromium渲染引擎确保应用性能、稳定性和安全性，同时支持与原生代码灵活结合。

- 🛠️ **技术融合**：Electron允许开发者混合使用Web技术（如HTML/JavaScript）与原生代码（C++、Rust等），打破“仅限JavaScript”的误解，兼顾开发效率与原生性能。
- 🌐 **Web技术优势**：Web技术已成为广泛验证的UI方案，支撑着NASA任务控制、彭博终端等高要求应用，其跨平台能力和生态成熟度是核心优势。
- ⚡ **性能与可控性**：捆绑Chromium而非依赖系统WebView，确保应用使用最新渲染引擎，避免系统版本碎片化，同时自主控制安全更新与性能优化。
- 💾 **安装包大小**：虽然Electron应用体积较大（约100-300MB），但用户更关注功能体验，存储成本在当今环境中已非首要考量。
- 🎯 **解决实际需求**：Electron旨在填补跨平台桌面应用开发工具的空缺，其成功源于帮助开发者高效构建用户喜爱的应用，而非与其他框架竞争。

---

### [转向仅支持ESM](https://antfu.me/posts/move-on-to-esm-only)

**原文标题**: [Move on to ESM-only](https://antfu.me/posts/move-on-to-esm-only)

本文探讨了JavaScript生态系统中从CommonJS（CJS）向ES模块（ESM）过渡的趋势，认为当前工具和生态已成熟，是时候推动ESM-only包的发展。作者回顾了双格式包的问题，并分析了适合迁移到ESM-only的场景，如新包、浏览器包和CLI工具。最后介绍了用于分析依赖ESM采用情况的工具Node Modules Inspector，并展望了未来生态的优化方向。

- 🛠️ **工具就绪**：现代工具如Vite、Vitest、tsx等已全面支持ESM，ESLint v9也引入了原生ESM配置，降低了开发门槛。
- 📈 **生态趋势**：ESM在npm包中的占比从2021年的7.8%增长到2024年的25.8%，显示生态正稳步向ESM迁移。
- 🔄 **互操作改进**：Node.js v22支持`require()`加载ESM模块，并引入新语法实现CJS兼容导出，缓解了迁移中的互操作难题。
- ⚠️ **双格式问题**：同时维护CJS和ESM会导致互操作复杂性、依赖解析混乱和包体积膨胀，增加维护负担。
- 🚀 **迁移场景**：新包、浏览器包、独立CLI工具以及针对高版本Node.js的包更适合优先采用ESM-only。
- 🔍 **用户考量**：包作者需评估现有用户生态，例如ESLint插件可借助v9的ESM原生支持顺利过渡。
- 📊 **进展可视化**：作者开发的Node Modules Inspector工具可分析依赖的ESM采用状态，帮助开发者制定迁移策略。
- 🌱 **未来展望**：作者计划逐步将维护的包过渡到ESM-only，并持续优化工具，以推动更轻量、高效的JavaScript生态。

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

### [Express.js新篇章：2024年的辉煌成就与2025年的宏伟蓝图](https://expressjs.com/2025/01/09/rewind-2024-triumphs-and-2025-vision.html)

**原文标题**: [A New Chapter for Express.js: Triumphs of 2024 and an ambitious 2025](https://expressjs.com/2025/01/09/rewind-2024-triumphs-and-2025-vision.html)

Express.js 在2024年完成了治理革新、技术升级与安全强化，并发布了Express 5.0，为2025年的自动化发布、性能优化和现代化改造奠定了坚实基础。

- 🏛️ **治理与社区里程碑**：推出《Express Forward Plan》并重组技术委员会，增强社区协作与发布流程透明度。
- 🛡️ **安全强化**：成立安全工作组，实施威胁模型，完成安全审计，并快速响应多个CVE漏洞。
- 🚀 **技术进展**：正式发布Express 5.0，启动Express 6.0规划，并重新整合至Node.js CITGM项目。
- 🌟 **生态认可**：获得OpenJS基金会“Impact Project”认证，彰显其在JavaScript生态中的重要性。
- 🔄 **2025年路线图**：依托Sovereign Tech Fund，计划实现npm发布自动化、引入作用域包、强化安全流程与性能监控。
- 📚 **现代化与文档**：逐步淘汰过时技术（如猴子补丁），并加强安全文档，提升开发者体验。
- 🤝 **持续协作**：鼓励社区通过GitHub Discussions和开放会议参与，共同推动框架发展。

---

### [- YouTube](https://www.youtube.com/watch?v=cRC9DlH45lA)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=cRC9DlH45lA)

该内容为YouTube平台页脚导航链接，列出了网站的主要政策、功能说明及公司信息。

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
- ™️ 2025年谷歌所有权声明

---

### [甲骨文曾以Node.js为其JavaScript商标辩护——如今却希望人们对此视而不见 | Deno](https://deno.com/blog/deno-v-oracle2)

**原文标题**: [Oracle justified its JavaScript trademark with Node.js—now it wants that ignored | Deno](https://deno.com/blog/deno-v-oracle2)

Oracle试图通过法律手段维持其对“JavaScript”商标的控制，尽管该商标涉及一个由社区主导的开放标准语言，引发了对其商标合法性的广泛质疑。

- 🚨 Oracle在商标续展中使用Node.js网站截图作为证据，尽管与该项目无关
- 📜 Deno公司以通用性、废弃和欺诈为由，正式申请撤销该商标
- ⏳ Oracle仅回应欺诈指控，并试图通过程序性动议拖延案件核心审理
- 🔍 质疑Oracle提交的Oracle JET证据是否仅为维持商标而存在，缺乏实际使用
- 🌐 JavaScript由ECMA-262规范定义，由多方维护，Oracle并无实际贡献或控制权
- ⚖️ 此案引发对商标系统滥用的担忧，即企业是否可无限期持有无关商标
- 📢 呼吁社区通过签署公开信和传播信息，共同反对Oracle的商标主张

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

### [密歇根TypeScript创始人成功在Ty...内运行《毁灭战士》](https://socket.dev/blog/typescript-types-running-doom)

**原文标题**: [Michigan TypeScript Founder Successfully Runs Doom Inside Ty...](https://socket.dev/blog/typescript-types-running-doom)

Socket Firewall Free现已集成至Docker加固镜像中，为Node.js、Python和Rust的加固基础镜像提供构建时和依赖安装阶段的供应链保护。

- 🔒 Socket Firewall Free已内置在Docker加固镜像中
- 🛡️ 为Node.js、Python和Rust提供供应链安全保护
- ⚙️ 覆盖构建时和依赖安装阶段的安全防护
- 🐳 基于加固基础镜像进一步增强安全性

---

### [获取失败](https://javascriptweekly.com/link/178735/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/178735/web)

无法总结：获取内容失败，状态码 403。

---

### [Express@5.1.0：现为npm默认版本，附带长期支持时间表](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

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

Koa是一个由Express团队设计的现代化Web框架，专注于提供更精简、更具表现力和更健壮的基础，适用于Web应用和API开发。

- 🚀 基于Express团队设计，旨在成为更轻量、更强大的Web框架
- ⚡ 利用异步函数，避免回调函数，显著提升错误处理能力
- 🧩 核心不捆绑任何中间件，保持高度模块化
- ✨ 提供优雅的方法集，使服务器开发快速而愉快

---

### [Node.js — 行程报告：Node.js协作峰会（2025年巴黎）](https://nodejs.org/en/blog/events/collab-summit-2025-paris)

**原文标题**: [Node.js — Trip report: Node.js collaboration summit (2025 Paris)](https://nodejs.org/en/blog/events/collab-summit-2025-paris)

2025年巴黎Node.js协作峰会汇集了近40名现场参与者和十余名远程参与者，围绕CI可靠性、WASM模块、内存管理、导师计划、贡献者体验、AsyncLocalStorage标准化、单可执行应用、Undici集成、Chrome DevTools支持、Next-10调查及模块定制等关键议题展开讨论与规划。

- 🛡️ CI可靠性与安全：针对近期安全事件，探讨了CI基础设施管理和测试稳定性改进方案，包括自动化流程优化和故障检测机制。
- ⚡ 技术进展分享：介绍了实验性WASM模块的启用计划、V8内存管理集成（Cppgc）以提升性能与安全性，以及模块化工具链的优化方向。
- 👥 社区与协作：回顾了导师计划的成效，讨论了如何改善贡献者体验，包括减少CI不稳定、优化决策流程（如引入表情符号投票和AI总结），并计划更新Next-10倡议。
- 🌐 AsyncLocalStorage标准化：探讨将Node.js的AsyncLocalStorage引入Web标准（AsyncContext提案），重点解决跨平台上下文传播的安全性与API设计挑战。
- 📦 单可执行应用（SEA）：讨论了ESM支持、工具链简化和虚拟文件系统等需求，但进展受限于志愿者和资金不足，计划组建团队推动。
- 🔗 Undici集成：规划通过暴露调度器配置来增强内置HTTP功能，支持HTTP/2自动升级，并探索通过WASM集成Milo项目。
- 🔧 开发工具集成：与Chrome DevTools团队合作，完善网络流量检查、Worker线程自动发现等功能，提升Node.js调试体验。
- 📊 生态调研：优化了Next-10年度调查问题，以更准确收集社区对Node.js未来发展的意见。
- 🧩 模块定制与性能：更新了模块加载钩子的同步化改进方案，并介绍了基于AST重写的ESM插桩工具，以提升可观测性支持。

---

### [p5.js](https://p5js.org/)

**原文标题**: [p5.js](https://p5js.org/)

p5.js是一个创意编程库，提供丰富的学习资源、社区作品展示及支持途径。

- 📚 提供p5.js库参考与示例学习资源
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

### [3.13版本发布 | GSAP | 文档与学习](https://gsap.com/blog/3-13/)

**原文标题**: [3.13 release | GSAP | Docs & Learning](https://gsap.com/blog/3-13/)

GSAP 3.13版本发布，核心更新包括GSAP及其所有插件（如SplitText、MorphSVG）现已完全免费，包括商业用途；SplitText插件全面重写，体积减小50%并新增14项功能，如屏幕阅读器无障碍支持、响应式重新分割和嵌套元素处理；新增动画至CSS变量的功能；优化了Webflow集成安装流程；Club GSAP会员将过渡至公共仓库，私人仓库访问将于2025年6月1日停止。

- 🎉 GSAP及其所有插件（包括SplitText、MorphSVG）现已完全免费，适用于商业用途
- 🔧 SplitText插件全面重写，体积减小50%，新增14项功能，如无障碍支持和响应式重新分割
- 🆕 新增动画至CSS变量的功能，可直接将CSS属性动画到变量值
- 🌐 优化Webflow集成，可直接在设置中启用GSAP核心库和插件
- 🔄 Club GSAP会员将过渡至公共NPM仓库，私人仓库访问将于2025年6月1日停止
- 📚 提供完整文档、学习资源和社区论坛支持

---

### [Glitch即将迎来重要更新](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

**原文标题**: [Important changes are coming to Glitch](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

Glitch平台宣布将终止应用托管服务，这是基于当前生态变化和资源挑战所做的战略调整，旨在更有效地服务开发者社区。

- 🗓️ **服务终止时间**：2025年7月8日将关闭项目托管和用户资料功能，仪表板会保留至2025年底供代码下载。
- 🔄 **过渡支持**：平台将提供项目子域名重定向功能（有效期至少至2026年底），并发布项目迁移指南。
- 💰 **付费方案调整**：立即停止新Glitch Pro订阅，现有订阅将服务至7月8日并退还未使用费用。
- 🌍 **生态演变**：因维护成本上升及新兴平台（如Fly.io、Deno等）提供更优方案，Glitch决定重新聚焦核心价值。
- 🤝 **社区参与**：鼓励用户通过社区论坛或直接邮件反馈，共同探索Glitch未来的发展方向。

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
- 🏢 **业界认可**：已被 Shopify、Airbnb、梅赛德斯-奔驰等公司以及 Bun、Preact 等大型开源项目采用，在实际应用中验证了其效能。
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

### [探索JavaScript（ES2025版）](https://exploringjs.com/js/)

**原文标题**: [Exploring JavaScript (ES2025 Edition)](https://exploringjs.com/js/)

《探索JavaScript》是一本面向初学者的现代JavaScript指南，涵盖至ES2025版本，旨在通过清晰的结构和丰富的辅助材料降低学习难度。

- 📚 本书原名《JavaScript for impatient programmers》，现更新为ES2025版，适合有编程基础但无需JavaScript经验的读者
- 🚀 采用现代特性优先的教学思路，包含可选高级章节和测试驱动练习、闪卡等辅助材料
- 🌐 提供免费在线阅读版本，数字离线套餐包含无DRM的HTML/EPUB/PDF格式电子书
- 💰 数字套餐分39美元“电子书”与59美元“电子书+附加资源”两档，旧版用户可享25%-50%升级折扣
- 🛒 另提供ES2019版纸质书在全球各大亚马逊平台销售，纸质书持有者可优惠获取数字套餐
- 👨🏫 作者Axel Rauschmayer博士专注JavaScript领域十余年，通过博客、书籍和培训课程分享专业知识

---

### [生物群落v2—代号：生物型 | 生物群落](https://biomejs.dev/blog/biome-v2/)

**原文标题**: [Biome v2—codename: Biotype | Biome](https://biomejs.dev/blog/biome-v2/)

Biome v2（代号Biotype）正式发布，这是首个不依赖TypeScript编译器即可提供类型感知lint规则的JavaScript和TypeScript linter，标志着项目迈向下一代Web工具链的重要里程碑。

- 🚀 **首个独立类型感知linter**：无需安装TypeScript包即可进行类型感知的代码检查，例如noFloatingPromises规则可检测约75%的浮动Promise案例。
- ⚙️ **多文件分析与类型推断**：新增文件扫描器支持跨文件类型查询，通过项目规则（project rules）启用，兼顾性能与功能扩展。
- 📦 **增强的Monorepo支持**：改进嵌套配置文件支持，新增`root: false`和`extends: "//"`配置方式，优化多包项目管理。
- 🔌 **Linter插件初版发布**：支持匹配代码片段并报告诊断信息，为未来功能扩展奠定基础。
- 📑 **导入组织器全面升级**：解决空白行分组、同模块导入合并等问题，新增自定义排序和导出语句支持。
- 🛠️ **新增辅助功能（Assists）**：提供无诊断信息的代码操作，如对象键排序和JSX属性排序。
- 🔕 **改进的代码抑制功能**：新增`// biome-ignore-all`全文件抑制及`// biome-ignore-start/end`范围抑制。
- 🌐 **实验性HTML格式化器**：支持.html文件格式化，为Vue、Svelte等框架集成铺路，需手动启用。
- 👏 **致谢与赞助方**：特别感谢Vercel赞助类型推断工作，Depot提供CI支持，以及多位核心贡献者的技术贡献。
- 🛣️ **未来路线图**：重点包括稳定HTML支持、扩展框架集成、Markdown解析器开发及类型推断优化。
- 🤝 **社区参与方式**：鼓励通过翻译、Discord交流、代码贡献（如lint规则开发、解析器改进）或财务赞助支持项目发展。

---

### [数据库迎来新用户——大语言模型，它们需要不同的数据库 | 虎数据](https://www.tigerdata.com/blog/the-database-new-user-llms-need-a-different-database)

**原文标题**: [The Database Has a New User—LLMs—and They Need a Different Database | Tiger Data](https://www.tigerdata.com/blog/the-database-new-user-llms-need-a-different-database)

本文介绍了TigerData正在实验的“自描述数据库”概念，旨在通过为PostgreSQL添加自然语言描述的语义目录，帮助LLM更准确地理解和查询数据库。实验显示，使用语义目录可将SQL生成准确率提升高达27%。

- 🧠 **数据库缺乏结构上下文**：传统数据库模式无法自我解释，导致LLM在缺乏额外上下文时难以准确生成查询，实验中42%的无上下文LLM生成SQL查询存在关键错误。
- 📚 **通过语义目录添加上下文**：允许开发者用自然语言描述数据库模式和业务逻辑，为LLM提供必要的语义信息，从而显著提升查询准确性。
- 🛠️ **构建自描述数据库的四个核心思想**：将语义嵌入模式、版本化描述、自我纠正查询机制（利用EXPLAIN）以及透明度量和迭代。
- 🔬 **当前实验组件**：包括存储模式元素自然语言描述的语义目录，以及用于衡量查询准确性的评估工具，重点解决检索中因名称含义模糊导致的问题。
- 📈 **语义上下文提升性能**：在早期测试中，使用LLM生成的语义目录将某些模式的SQL生成准确率从58%提高到86%，检索召回率也有所改善。
- 🔄 **查询工作流程**：分为四个步骤——使用LLM描述数据库、人工审核并添加上下文、导入到目录中、根据自然语言生成SQL。
- 💡 **关键经验教训**：丰富的语义信息（而不仅是模式名称）对生成正确SQL至关重要；建议从严格限制的接口（如函数）开始，再逐步扩大访问范围。
- 🔍 **利用EXPLAIN自我纠正**：通过PostgreSQL的EXPLAIN命令预先捕获查询错误，使代理能够自我纠正，进一步提高准确性。
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

NuxtLabs宣布加入Vercel，旨在通过整合资源强化开源框架Nuxt的持续发展，确保项目在MIT许可下保持透明化运营，并将社区贡献置于核心位置。未来团队将聚焦AI集成与工具开源化，为开发者提供更高效的建设体验。

- 🚀 NuxtLabs加入Vercel以专注开源发展，无需分散精力处理资金与维护问题
- 🌍 项目保持MIT许可，路线图公开透明，社区仍为核心
- 💡 赞助资金将转入Open Collective平台，确保直接支持核心开发与贡献者
- 🆓 即将免费开放Nuxt UI v4所有专业组件及Figma工具包
- 🛠️ 开源自托管版Nuxt Studio，支持直接集成Nuxt Content站点管理
- 🔄 NuxtHub将适配多平台，无缝对接Vercel市场的Postgres等服务
- 🤖 重点探索AI与Nuxt开发体验融合，与Vercel AI团队深度协作
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

Apache ECharts 6.0 正式发布，带来12项重大升级，围绕更专业的视觉呈现、拓展数据表达边界和释放组合自由三大核心维度，旨在让复杂数据呈现既强大又优雅，为开发者提供更灵活、便捷的图表创作体验。

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

jQuery 4.0.0 的第一个候选版本（rc.1）已发布，标志着该重大版本更新进入最终测试阶段。此版本包含多项期待已久的破坏性变更，如移除旧版IE支持、废弃API及简化内部行为，并首次引入了更轻量的“slim”构建版本。团队鼓励开发者积极测试并提供反馈，若无重大问题，最终版将随后发布。

- 🚀 **发布候选版本**：jQuery 4.0.0-rc.1 已推出，进入最终测试阶段，呼吁社区协助测试并反馈问题。
- ⚠️ **破坏性变更**：移除了对IE11以下版本的支持、已废弃的API、未公开的内部参数及一些过于复杂的“魔法”行为。
- 📦 **新增Slim构建**：提供了排除Ajax、动画和Deferreds模块的轻量版本，gzip后体积比常规版本小约8KB。
- 🔗 **获取方式**：可通过jQuery CDN直接获取文件或通过npm安装，第三方CDN将暂不托管此候选版本。
- 📄 **升级辅助**：同步发布了4.0升级指南和jQuery Migrate工具，但两者在最终版前仍可能调整。
- 🙏 **致谢贡献者**：感谢所有提交补丁、报告错误或参与测试的贡献者及jQuery团队。

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

### [AddyOsmani.com - 谷歌Chrome浏览器17年历程 - 我们的浏览器历史回顾](https://addyosmani.com/blog/chrome-17th/)

**原文标题**: [AddyOsmani.com - Google Chrome at 17 - A history of our browser](https://addyosmani.com/blog/chrome-17th/)

本文回顾了Google Chrome浏览器17年的发展历程，从2008年作为一款以漫画形式发布的新浏览器，成长为如今被数十亿用户使用的核心产品。文章重点阐述了Chrome始终遵循的四大核心理念——速度、安全、稳定、简洁，并详细介绍了其在多进程架构、V8引擎、AI集成等方面的关键技术创新与演变。

- 🚀 **速度为先**：Chrome自诞生起就将性能作为核心，其V8 JavaScript引擎大幅提升了网页应用运行速度。通过持续优化渲染管道、网络协议（如推动HTTP/2和HTTP/3）以及专注于核心网页指标，Chrome在Speedometer等基准测试中不断刷新纪录，为用户节省了大量加载时间。
- 🛡️ **深度防御安全**：Chrome采用沙盒和多进程架构来隔离标签页，有效遏制恶意代码。通过自动更新、漏洞奖励计划、Site Isolation（站点隔离）以及集成安全浏览等服务，层层加固浏览器安全。近年来还利用本地机器学习模型实时检测网络钓鱼和恶意通知。
- 🧱 **稳固可靠**：多进程架构不仅提升了安全性，也极大地增强了稳定性——单个标签页的崩溃不会导致整个浏览器关闭。团队通过优化内存管理、淘汰问题插件（如Flash）以及积极参与Web平台互操作性项目，确保浏览器和网络平台都能平稳运行。
- ✨ **简约哲学**：Chrome以简洁、最小化的用户界面设计著称，突出网页内容本身。其Omnibox（多功能地址栏）、智能建议和轻量级UI都旨在减少用户摩擦。扩展生态系统在提供强大定制能力的同时，也努力维持核心产品的简洁与安全。
- 🌐 **无处不在**：Chrome从桌面迅速扩展到移动端（Android/iOS）和ChromeOS，并通过同步功能实现跨设备无缝体验。它积极推动渐进式Web应用的发展，让Web应用能具备类似原生应用的能力，从而将Web打造为一个强大的应用平台。
- ⚙️ **推动平台进化**：通过“Project Fugu”等项目，Chrome为Web引入了大量新API（如文件系统访问、Web蓝牙等），显著缩小了Web应用与原生应用的能力差距。同时，它通过开发者工具和丰富的文档积极支持开发者生态。
- 🤖 **AI赋能新时代**：Chrome正深度集成AI能力，例如通过Gemini模型提供智能标签页整理、AI生成主题、写作辅助以及页面摘要等功能。它还向开发者提供了本地AI API，让Web应用能利用设备端的模型能力，在增强功能的同时注重用户隐私。

---

### [npm作者Qix因钓鱼邮件在重大供应链攻击中受侵](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

**原文标题**: [npm Author Qix Compromised via Phishing Email in Major Suppl...](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

恶意NuGet包通过仿冒流行的.NET追踪库Tracer.Fody，利用字形混淆技术窃取Stratis钱包的JSON文件与密码，并将数据外泄至俄罗斯IP地址。

- 🕵️ 恶意包“Tracer.Fody.NLog”通过仿冒合法库“Tracer.Fody”及其作者进行投毒攻击
- 🔠 使用同形异义字（homoglyph）技巧伪装包名，诱骗开发者下载
- 💰 专门针对Stratis钱包，窃取其JSON配置文件与密码信息
- 🌐 将窃取的数据外泄至位于俄罗斯的IP地址
- ⚠️ 突显软件供应链安全风险及依赖库验证的重要性

---

### [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

**原文标题**: [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

pnpm 10.16版本引入了两项主要新功能以增强安全性及依赖管理灵活性，并包含多项问题修复。

- 🛡️ 新增 `minimumReleaseAge` 设置，可延迟安装新发布的依赖包（例如设为1440分钟即一天），以降低安装到被攻击的恶意包版本的风险，并可通过 `minimumReleaseAgeExclude` 排除特定包。
- 🔍 支持在 `.pnpmfile.cjs` 中定义“查找器函数”，使 `pnpm list` 和 `pnpm why` 命令能依据依赖包属性（如特定peerDependencies）进行高级筛选，并支持在输出中返回自定义信息（如许可证）。
- 🐛 修复了在Node.js 24下执行时的弃用警告、`nodeVersion` 需为精确语义版本号的校验、`pnpm publish` 发布 `.tar.gz` 文件的能力，以及使用Ctrl-C取消进程后 `pnpm run` 应返回非零退出码的问题。

---

### [基于Electron的应用程序在macOS 26上引发全系统严重卡顿问题 · Issue #48311 · electron/electron · GitHub](https://github.com/electron/electron/issues/48311)

**原文标题**: [Electron-based apps cause a huge system-wide lag on macOS 26 · Issue #48311 · electron/electron · GitHub](https://github.com/electron/electron/issues/48311)

Electron应用在macOS 26上引发系统级严重卡顿问题，用户报告在开启Discord、VS Code等基于Electron的应用时，即使CPU和GPU使用率低，窗口移动和滚动仍出现明显卡顿，且该问题在macOS 15中未出现。

- 🐛 **问题描述**：macOS 26上Electron应用（如Discord、VS Code）未最小化时，系统界面出现严重卡顿，影响窗口移动和滚动流畅度
- 🖥️ **系统环境**：macOS 26 Tahoe RC系统，M1 Max芯片设备，Electron版本37.3.1
- 🔍 **重现条件**：同时打开多个Electron应用时卡顿加剧，最小化应用后卡顿消失
- 🆚 **对比情况**：Chrome浏览器未出现类似问题，macOS 15系统无此现象
- 🐞 **问题状态**：已确认为bug，维护者建议用户通过Feedback Assistant向苹果提交报告
- 📋 **处理进展**：问题已关闭，标签显示涉及37-x-y和38-x-y版本，归类为macOS平台性能问题

---

### [助我们筹集20万美元，让JavaScript摆脱Oracle的束缚 | Deno](https://deno.com/blog/javascript-tm-gofundme)

**原文标题**: [Help Us Raise $200k to Free JavaScript from Oracle | Deno](https://deno.com/blog/javascript-tm-gofundme)

Deno公司发起法律行动，旨在通过美国专利商标局撤销Oracle对“JavaScript”商标的所有权，以使其成为公共领域术语，供开发者自由使用。目前案件进入关键证据收集阶段，需筹集20万美元用于法律费用，包括专业调查、专家证词及法律文件等。若胜诉，将确立商标法对通用名称的保护原则。

- 🏛️ Deno向美国专利商标局提交撤销“JavaScript”商标的申请，案件进入证据收集阶段
- 💰 发起20万美元众筹，用于支付法律调查、专家证词及诉讼费用
- 📜 若胜诉，“JavaScript”将变为公共领域术语，开发者可自由使用
- ⚖️ Oracle否认“JavaScript”为通用术语，案件结果将影响商标法对通用名称的保护原则
- 🌐 剩余资金将捐赠给OpenJS基金会，用于维护数字空间公民自由

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

Node.js 24 已进入长期支持（LTS）阶段，代号“Krypton”，将提供维护和安全更新至2028年4月。此版本增强了安全性、运行时验证和Web API支持，同时N|Solid 6.0.2已全面兼容该版本，为企业用户提供先进的监控和性能分析功能。

- 🔒 **安全性提升**：采用OpenSSL 3.5，默认安全级别为2，禁止使用弱密钥和RC4密码套件。
- 🛡️ **运行时验证加强**：多个API（如Buffer、fs.symlink）增加了严格的参数验证，帮助更早捕获错误。
- 🌐 **Web API增强**：新增CloseEvent、Float16Array等全局对象，fetch()实现更严格，提升与浏览器环境的互操作性。
- 📦 **模块系统优化**：ESM CommonJS包装器默认导出module.exports，改善ESM与CommonJS的互操作性。
- 🚀 **流和Readline改进**：增强stream错误传播和readline的Unicode支持，提升I/O稳定性和性能。
- 🔧 **编译要求更新**：构建Node.js需使用更新版本的编译器（如GCC 12.2+、Xcode 16.1+），反映对现代C++标准的支持。
- 🗑️ **API清理**：移除了多个已弃用的API和内部绑定（如util.is*()、tls.createSecurePair()），保持核心轻量安全。
- 💻 **平台支持调整**：停止提供32位Windows和armv7 Linux的预构建二进制文件，macOS需13.5或更高版本。
- 🛠️ **N|Solid全面兼容**：N|Solid 6.0.2支持Node.js 24 LTS，提供gRPC通信改进、OpenTelemetry集成增强和持续性能分析。
- 📅 **长期支持策略**：NodeSource继续支持所有活跃的Node.js LTS版本（包括24、22、20），方便企业按需迁移。

---

### [介绍React基金会——React](https://react.dev/blog/2025/10/07/introducing-the-react-foundation)

**原文标题**: [Introducing the React Foundation – React](https://react.dev/blog/2025/10/07/introducing-the-react-foundation)

Meta宣布将React和React Native从公司内部项目转移至新成立的React基金会，并建立独立的技术治理结构，以更好地服务社区和生态系统。

- 🏛️ React基金会将成为React、React Native及JSX等项目的归属，负责基础设施维护、组织React Conf会议及资助生态项目
- 🤝 创始企业成员包括亚马逊、Callstack、Expo、Meta、微软、Software Mansion和Vercel，未来将吸纳更多成员
- 🧭 将建立独立于基金会的新技术治理结构，确保技术方向由贡献者共同决定，避免单一公司过度主导
- 🌱 此举旨在为React生态项目提供更多资源，巩固社区驱动的可持续发展模式

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

### [Octoverse：每秒都有新开发者加入GitHub，AI引领TypeScript登顶榜首 - GitHub博客](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

**原文标题**: [Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1 - The GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

GitHub在2025年经历了创纪录的增长，AI的普及推动了TypeScript首次成为平台最常用语言，开发者活动、开源贡献和全球开发者分布均呈现显著变化。

- 🚀 GitHub开发者总数超过1.8亿，平均每秒新增一位开发者，年增长超3600万
- 🤖 AI工具成为开发标配，80%新用户首周使用Copilot，AI相关仓库数量翻倍
- 📈 TypeScript超越Python和JavaScript，首次成为GitHub最常用语言
- 🌍 印度成为最大开发者增长源，年增超500万，预计2030年占全球新开发者三分之一
- 🔧 开发者生产力大幅提升，代码推送、PR合并和问题关闭数量均创历史新高
- 🛡️ 安全自动化加速，关键漏洞修复时间缩短30%，Dependabot使用量增长137%
- 📊 开源贡献达11.2亿次，AI基础设施项目成为增长最快领域
- 🌐 全球开发者分布更加多元化，巴西、印尼等新兴市场增长迅猛

---

### [GitLab发现大规模npm供应链攻击](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

**原文标题**: [GitLab discovers widespread npm supply chain attack](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

最全面的AI驱动DevSecOps平台，提供一体化解决方案，助力开发与安全团队高效协作。

- 🛠️ 一体化平台：集成开发、安全与运维流程，实现全生命周期管理
- 🤖 AI驱动：利用人工智能技术自动优化安全检测与漏洞修复
- 🔒 安全优先：将安全实践深度融入开发流程，提升应用防护能力
- ⚡ 高效协作：打破团队壁垒，促进开发与安全团队无缝配合
- 🌐 全面覆盖：支持从代码编写到部署运维的完整DevSecOps链条

---

### [JavaScript引擎动物园](https://zoo.js.org/)

**原文标题**: [JavaScript engines zoo](https://zoo.js.org/)

该内容为一份开源JavaScript引擎的技术规格与项目元数据摘要。

- 🏗️ **引擎** - 核心执行环境名称
- 📊 **得分** - 性能或合规性量化指标
- 🔢 **二进制** - 编译产物格式
- 📏 **代码行数** - 项目规模统计
- 💬 **语言** - 实现所用编程语言
- ⚡ **即时编译** - 是否支持JIT优化
- 📅 **年限** - 项目维护时长
- 🎯 **目标平台** - 支持运行的环境
- 📜 **ES1-5** - ECMAScript传统标准支持
- ✨ **ES6** - ECMAScript 2015标准支持
- 🚀 **ES2016+** - 现代ECMAScript标准支持
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

### [JavaScript周刊第764期：2025年12月5日](https://javascriptweekly.com/issues/764)

**原文标题**: [JavaScript Weekly Issue 764: December 5, 2025](https://javascriptweekly.com/issues/764)

本期内容主要围绕JavaScript诞生30周年及相关技术动态展开，涵盖语言发展、企业工具、框架更新、安全实践及开发资源等多个方面。

- 🎉 JavaScript迎来30周年纪念，回顾其诞生历程及当前在Web、桌面、移动等多平台的核心地位
- 🔐 WorkOS提供企业级身份验证与安全功能API，帮助开发者快速集成SSO、SCIM等合规需求
- ⚡ TypeScript 7.0进展中，将转向Go语言重写，预计性能提升10倍
- 🤖 Anthropic收购Bun运行时，计划用于Claude Code智能开发工具，并承诺保持开源
- ⚠️ React团队披露服务器组件安全漏洞，影响部分Next.js应用
- 🎄 多项编程挑战活动同步进行，包括Advent of Code、AdventJS与Advent of Svelte
- 🛠️ 重要发布：Vite 8 Beta、Oxfmt代码格式化工具、ESLint v10.0.0 Alpha 1
- 📖 安全实践：文章探讨npm发布流程加固与JSDoc替代TypeScript的类型方案
- 🐛 Wallaby推出AI驱动调试工具，宣称比断点调试快15倍
- 📊 技术分析：对比AWS Lambda中Arm与x86架构性能、浏览器Base64处理速度
- 🎵 创意项目：利用Web Audio API实现无人机环境音合成器
- 📚 开发资源：涵盖Angular管道优化、Vue组合函数测试、范畴论JS指南等深度文章
- 🔧 新工具：TanStack AI统一LLM接口、Ruby2JS转译器、Chokidar文件监听库更新
- 📢 生态动态：包括Spec Kit驱动开发、Web性能年度回顾、密码学图解指南等周边资讯

---

### [TypeScript 7 进展 - 2025年12月 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

**原文标题**: [Progress on TypeScript 7 - December 2025 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

TypeScript 7.0（代号“Corsa”）的开发进展顺利，已进入预览阶段，其原生代码编译器与语言服务在性能和稳定性上均有显著提升，旨在为开发者带来更快的编译速度、更低的内存占用以及更流畅的编辑器体验。

- 🚀 **性能大幅提升**：原生编译器在完整构建中相比TypeScript 6.0有接近10倍的加速，并支持多线程并行构建项目。
- 🔧 **编辑器支持完善**：VS Code扩展预览版已支持代码补全、自动导入、重命名等核心语言服务功能，日常使用稳定。
- 📦 **编译器功能就绪**：通过`@typescript/native-preview`包可体验新编译器，类型检查兼容性高，支持增量编译与项目引用。
- ⚠️ **需注意的变更**：TypeScript 7.0将默认启用严格模式，移除部分已弃用配置（如`--target es5`），JavaScript类型检查规则更严格。
- 🔄 **过渡与规划**：TypeScript 6.0将是最后一个基于JavaScript的版本，作为向7.0过渡的桥梁，后续开发将聚焦于原生代码库。
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

Node.js v24.12.0（代号“Krypton”）作为长期支持版本发布，包含多项新功能、性能优化、错误修复及依赖项更新，提升了模块系统、HTTP处理、SQLite集成、调试工具等方面的稳定性和效率。

- 🚀 **新增HTTP服务器选项**：添加`optimizeEmptyRequests`选项以优化空请求处理，提升服务器性能。
- 📦 **模块类型剥离功能稳定化**：将模块类型剥离标记为稳定功能，增强ES模块兼容性。
- 🔧 **Node-API功能扩展**：新增`napi_create_object_with_properties`方法，简化对象创建流程。
- 🛡️ **SQLite防御标志支持**：允许设置SQLite的防御标志，增强数据库操作安全性。
- ⚙️ **新增配置命名空间**：添加`watch`配置命名空间，改进文件监视功能。
- 📂 **编译缓存可移植性**：新增选项使编译缓存可跨环境移植，提升构建效率。
- 🔍 **调试器权限控制**：添加`--allow-inspector`选项，允许在权限模式下启用调试器。
- 📊 **V8 CPU性能分析**：新增CPU性能分析功能，便于性能调优。
- 🐛 **多项错误修复与优化**：涵盖加密、控制台、调试器、流处理等模块，提升稳定性和性能。
- 🔄 **依赖项更新**：升级V8引擎、nghttp2、corepack等依赖至新版本，引入功能改进和安全补丁。
- 📖 **文档完善与修正**：更新多个文档部分，修复链接错误并澄清功能描述。
- 🧪 **测试套件增强**：改进测试覆盖率，修复异步测试和断言问题，确保代码可靠性。

---

### [精密AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=q4)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=q4)

Meticulous AI 是一款通过记录用户交互自动生成并维护端到端测试的工具，旨在帮助开发团队无需编写或维护测试代码即可实现全面覆盖，提升开发效率和代码质量。

- 🚀 **无需编写测试** – 通过记录开发、预演和生产环境中的用户交互，自动生成覆盖所有代码分支和用户流程的测试套件。
- 🔄 **自动维护与更新** – 测试套件随应用演进自动更新，新增功能或边缘案例会自动纳入测试，过时测试则被移除。
- ⚡ **快速无抖动测试** – 基于 Chromium 构建的确定性调度引擎，消除测试抖动，支持大规模并行测试，结果通常在 120 秒内返回。
- 🛡️ **安全无副作用** – 通过模拟后端响应进行测试，避免因数据变化导致的误报，无需设置测试账户或模拟数据。
- 🌐 **广泛集成支持** – 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流前端框架，可轻松集成到现有开发流程。
- 📈 **提升开发信心** – 已被 Dropbox、Notion、Lattice 等超过 100 家组织采用，帮助团队预防回归问题，加速可靠代码的交付。

---

### [Trigger.dev | 构建和部署全托管AI代理与工作流。](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=trigger.dev-december&utm_term=jsweekly&utm_content=homepage)

**原文标题**: [Trigger.dev | Build and deploy fully-managed AI agents and workflows.](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=trigger.dev-december&utm_term=jsweekly&utm_content=homepage)

Trigger.dev 宣布完成1600万美元A轮融资，这是一个用于在TypeScript中构建AI工作流和代理的平台，提供全托管、可扩展的解决方案，支持长时间运行的任务、重试、队列和实时监控。

- 🚀 Trigger.dev 完成1600万美元A轮融资，专注于构建全托管AI代理与工作流平台
- ⚙️ 提供基于TypeScript的AI工作流开发，支持长时间运行任务、自动重试、队列管理和弹性扩展
- 🔧 集成多样化功能：AI任务、视频处理、定时任务、等待机制、并行处理、语义搜索等
- 🤖 支持复杂AI代理构建：包括自主代理、提示链、路由、并行化、协调器与评估优化器
- 🌐 无需管理服务器：提供无超时执行、按使用付费、多区域部署和自动扩展
- 🐛 内置高级调试：错误警报、运行过滤、版本控制、实时状态显示与流式响应传输
- 🔌 兼容现有技术栈：支持Python、Prisma、Puppeteer、FFmpeg等自定义扩展与集成
- 📈 受全球开发者信赖：已被多家公司用于关键业务场景，提升开发效率与系统可靠性
- 💰 提供灵活定价：按需付费、免费起步选项，并支持开源自托管部署

---

