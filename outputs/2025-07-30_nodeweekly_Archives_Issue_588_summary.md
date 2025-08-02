### [Node 周刊第 588 期：2025 年 7 月 29 日](https://nodeweekly.com/issues/588)

**原文标题**: [Node Weekly Issue 588: July 29, 2025](https://nodeweekly.com/issues/588)

overview summary  
本期内容涵盖了 JavaScript 生态的最新动态，包括多个 JavaScript 运行时的深度解析、TypeScript 5.9 RC 的发布、npm 安全事件、Node.js 性能优化工具，以及一系列开发者工具和库的更新。此外，还介绍了机器学习在 Web 端的应用、博客平台 Ghost 的即将发布版本，以及其他开发者社区的趣闻和资源。  

- 🚀 **JavaScript 运行时大全** — 一篇耗时一年完成的文章，详细介绍了过去十年中出现的各种 JavaScript 运行时和引擎，包括 Node.js、云平台及其他小众选择。  
- 🔒 **npm 安全事件** — `is`包被劫持，攻击者通过仿冒 npm 域名钓鱼获取登录信息，再次引发对开源生态安全的关注。  
- 📦 **TypeScript 5.9 RC 发布** — 支持`import defer`和`--module node20`等新特性，正式版将于本周发布。  
- ⚡ **Node.js 性能优化** — Unix 域套接字比 TCP 回环降低 50% 延迟，适合 Node.js 进程间通信。  
- 🤖 **Bun 与 Node.js 兼容性** — Bun 创始人 Jarred Sumner 表示，Bun 的目标是成为 Node.js 生态的无缝替代品，主要精力投入在兼容性上。  
- 🛠 **开发者工具更新**  
  - **AudioTee.js** — 通过 Swift 二进制工具捕获 Mac 系统音频输出。  
  - **Transformers.js 3.7** — 支持在浏览器或 Node.js 中运行预训练机器学习模型（如 Voxtral、LFM2）。  
  - **match-sorter 8.1** — 提供确定性数组排序算法，附在线演示。  
- 📢 **其他新闻**  
  - **Ghost 6.0 RC** — 热门博客平台即将发布新版本。  
  - **State of HTML 2025 调查** — 开发者可参与并了解 HTML 技术趋势。  
  - **空格 vs 制表符之争** — 开发者称多数语言已倾向于使用空格。

---

### [过去十年中众多、众多、众多的 JavaScript 运行时 • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

**原文标题**: [The many, many, many JavaScript runtimes of the last decade • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

过去十年见证了 JavaScript 运行时的爆炸式增长，使其能够适应云端、边缘计算、智能电视、移动设备甚至微控制器等多种场景。以下是关键点总结：

- 🌐 **边缘计算**：从 Node.js 在 AWS Lambda 的应用到 Cloudflare Workers 的崛起，JavaScript 逐渐成为边缘计算的重要语言，各公司纷纷推出定制化运行时以优化性能。
- 💡 **微控制器**：为适应极低资源环境，出现了如 Duktape、JerryScript 等轻量级引擎，支持在 RAM 不足 64KB 的设备上运行 JavaScript。
- 🔄 **多语言引擎**：通过 Graal.js 等工具，JavaScript 实现了与 Java、.NET 等语言的无缝互操作，扩展了其应用场景。
- 📱 **原生应用**：React Native 和 NativeScript 等框架使 JavaScript 成为移动开发的主流选择，而 Electron 则主导了桌面应用开发。
- 📺 **智能电视**：JavaScript 通过 Cordova 和 React Native 等框架，成为智能电视应用开发的重要工具。
- 🛠 **多样化引擎**：不同运行时采用 V8、JavaScriptCore、SpiderMonkey 等多种引擎，根据场景需求优化性能与资源占用。

JavaScript 的灵活性和广泛的生态系统使其成为跨平台开发的优选语言，未来仍将持续扩展其应用边界。

---

### [宣布 TypeScript 5.9 RC 版本 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/)

**原文标题**: [Announcing TypeScript 5.9 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/)

TypeScript 5.9 RC 发布，包含多项新功能和优化，旨在提升开发体验和性能。

- 🚀 **TypeScript 5.9 RC 发布**：可通过 `npm install -D typescript@rc` 安装。
- 🛠️ **简化的 `tsc --init`**：生成的 `tsconfig.json` 更简洁，默认启用常用配置（如 `strict`、`jsx` 等）。
- ⏳ **支持 `import defer`**：延迟模块执行，首次访问时触发，适用于条件加载和高开销初始化。
- 📦 **新增 `--module node20`**：稳定支持 Node.js v20 的模块行为，默认目标为 `es2023`。
- 📚 **DOM API 摘要描述**：新增基于 MDN 的 API 功能摘要，提升文档可读性。
- 🔍 **可扩展悬停预览**：在 VS Code 中支持展开/折叠类型详细信息，便于快速查看复杂类型。
- 📏 **可配置悬停长度**：通过 `js/ts.hover.maximumLength` 设置悬停信息的最大显示长度。
- ⚡ **性能优化**：缓存类型实例化、减少闭包创建，提升大型项目编译速度。
- ⚠️ **行为变更**：`ArrayBuffer` 不再作为 `TypedArray` 的父类型，可能影响相关代码。
- 🔜 **后续计划**：聚焦 TypeScript 7 原生版本，5.9 正式版预计一周内发布。

---

### [谷歌在线安全博客：推出 OSS Rebuild 计划——开源重建，历久弥新](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html)

**原文标题**: [
Google Online Security Blog: Introducing OSS Rebuild: Open Source, Rebuilt to Last
](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html)

Google 宣布推出 OSS Rebuild 项目，旨在通过重建上游开源软件包来增强对开源生态系统的信任，应对供应链攻击的威胁。该项目为安全团队提供自动化工具和 SLSA 认证，以验证软件包的来源和构建过程，同时不增加维护者的负担。

- 🛡️ **项目目标**：通过重建开源软件包增强供应链安全，提供透明度和可验证的构建过程。  
- 🤖 **自动化工具**：支持 PyPI、npm 和 Crates.io 等流行包管理器的自动化构建定义生成。  
- 📜 **SLSA 认证**：为数千个软件包提供符合 SLSA Build Level 3 要求的来源证明，无需发布者干预。  
- 🔍 **检测能力**：识别未提交的源代码、构建环境被篡改和隐蔽后门等供应链攻击。  
- 🏗️ **基础设施**：提供组织自行运行 OSS Rebuild 实例的定义，支持重建、签名和分发软件包。  
- 🌍 **广泛支持**：初期支持 Python、JavaScript/TypeScript 和 Rust 生态系统，未来计划扩展至更多语言。  
- 🔧 **开发者友好**：提供命令行工具，方便获取和验证软件包的 SLSA 认证。  
- 🤝 **社区参与**：鼓励开发者、企业和安全研究人员参与项目，共同提升开源软件的安全性。

---

### [npm 'is' 包在扩大化的供应链攻击中被劫持 -...](https://socket.dev/blog/npm-is-package-hijacked-in-expanding-supply-chain-attack)

**原文标题**: [npm ‘is’ Package Hijacked in Expanding Supply Chain Attack -...](https://socket.dev/blog/npm-is-package-hijacked-in-expanding-supply-chain-attack)

Socket CEO Feross Aboukhadijeh 和 a16z 合伙人 Joel de la Garza 探讨了氛围编码、AI 驱动的软件开发，以及尽管存在风险，但 LLM 的兴起仍指向更安全和创新的未来。

- 🎙️ Socket CEO 和 a16z 合伙人讨论 AI 驱动的软件开发及其未来影响  
- 💡 提到“氛围编码”（vibe coding）概念及其在开发中的角色  
- 🤖 大型语言模型（LLM）的兴起带来安全风险，但也推动创新  
- 🔒 尽管存在风险，AI 技术仍有望促进更安全的软件开发  
- 🚀 讨论认为 AI 和 LLM 是未来技术进步的关键驱动力

---

### [npm 钓鱼邮件通过误植域名瞄准开发者...](https://socket.dev/blog/npm-phishing-email-targets-developers-with-typosquatted-domain)

**原文标题**: [npm Phishing Email Targets Developers with Typosquatted Doma...](https://socket.dev/blog/npm-phishing-email-targets-developers-with-typosquatted-domain)

Socket CEO Feross Aboukhadijeh 和 a16z 合伙人 Joel de la Garza 探讨了氛围编程、AI 驱动的软件开发，以及尽管存在风险，但 LLM 的兴起仍指向更安全和创新的未来。

- 💡 **氛围编程讨论**：探讨了开发者通过直觉和协作（而非严格规范）推动项目的“氛围编码”文化。  
- 🤖 **AI 驱动开发**：AI 工具正在改变软件构建方式，但需平衡自动化与代码质量/安全性。  
- ⚠️ **LLM 的风险**：大型语言模型可能引入安全漏洞（如生成易受攻击代码），需谨慎监管。  
- 🛡️ **安全未来**：尽管风险存在，AI 技术的进步最终将推动更高效的漏洞检测与修复。  
- 🔮 **创新前景**：LLM 的普及或加速开发周期，促成更具创造力的解决方案。

---

### [Node.js 开发者指南：Unix 域套接字比 TCP 回环降低 50% 延迟](https://nodevibe.substack.com/p/the-nodejs-developers-guide-to-unix)

**原文标题**: [The Node.js Developer's Guide to Unix Domain Sockets: 50% Lower Latency Than TCP loopback](https://nodevibe.substack.com/p/the-nodejs-developers-guide-to-unix)

概述  
本文介绍了 Unix 域套接字在 Node.js 中的优势，相比 TCP 回环可降低 50% 的延迟，并提供了实现方法和实际案例。

- 🚀 **性能优势**：Unix 域套接字延迟仅为 130µs，而 TCP 回环为 334µs，性能提升显著。  
- 📁 **工作原理**：Unix 套接字通过文件系统直接通信，避免了 TCP 的网络协议栈开销，减少内核切换和 CPU 占用。  
- 🔧 **实际应用**：PM2 和 PostgreSQL 等工具已广泛使用 Unix 套接字，实现高效进程管理和数据库连接。  
- 💡 **实现示例**：通过构建双模式聊天服务器（支持 TCP 和 Unix 套接字切换），验证了性能差异。  
- ⚙️ **测试结果**：基准测试显示，Unix 套接字在并发场景下延迟更低（平均 130µs vs TCP 的 334µs）。  
- 🛠️ **开发建议**：推荐在需要低延迟或避免端口冲突的 IPC 场景中使用 Unix 套接字。  
- 📂 **代码资源**：文章提供了完整代码仓库，供开发者进一步测试和实现。

---

### [Bun 创始人 Jarred Sumner 谈构建 Bun、Node.js 兼容性及开发流程中的 AI - YouTube](https://www.youtube.com/watch?v=VGjJWXFYyQo)

**原文标题**: [Creator of Bun Jarred Sumner on Building Bun, Node.js Compatibility & AI in Dev Workflows - YouTube](https://www.youtube.com/watch?v=VGjJWXFYyQo)

关于 YouTube 的相关信息与链接  

- 📢 **关于** - 提供 YouTube 平台的背景与介绍  
- 🗞️ **媒体** - 新闻稿与媒体资源  
- ©️ **版权** - 版权政策与保护措施  
- 📩 **联系我们** - 用户与平台的联系方式  
- 🎨 **创作者** - 创作者相关资源与支持  
- 💰 **广告** - 广告合作与推广信息  
- 👩💻 **开发者** - 开发者工具与 API 资源  
- 📜 **条款** - 使用条款与条件  
- 🔒 **隐私** - 隐私政策与数据保护  
- ⚖️ **政策与安全** - 平台规范与安全指南  
- ▶️ **YouTube 如何运作** - 平台功能与机制解析  
- 🧪 **测试新功能** - 新功能的试用与反馈  
- ®️ **版权声明** - © 2025 Google LLC

---

### [Bun — 一款全功能快速 JavaScript 运行时](https://bun.sh/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.sh/)

Bun v1.2.19 是一个快速、全能的 JavaScript 工具包，集成了开发、测试、运行和打包功能，旨在提供极速体验并兼容 Node.js。

- 🚀 **全能工具包**：Bun 是一个集运行时、打包工具、测试运行器和包管理器于一体的 JavaScript/TypeScript 工具。  
- ⚡ **极致性能**：在 HTTP 请求、WebSocket 消息和数据库查询等基准测试中，Bun 速度远超 Deno 和 Node.js。  
- 📥 **安装简便**：支持 Linux、macOS 和 Windows，可通过命令行一键安装（`curl` 或 PowerShell 脚本）。  
- 🔄 **Node.js 兼容**：目标是实现 100% 的 Node.js 兼容性，方便现有项目迁移。  
- 📊 **性能对比**：  
  - HTTP 请求：Bun（59,026/秒）vs Deno（25,335/秒）vs Node.js（19,039/秒）。  
  - WebSocket 消息：Bun（2,536,227/秒）vs Deno（1,320,525/秒）vs Node.js（435,099/秒）。  
  - 数据库查询：Bun（50,251/秒）vs Node.js（14,398/秒）vs Deno（11,821/秒）。  
- 🌐 **广泛使用**：被 Express、Postgres 和 WebSocket 等流行库采用。

---

### [如何构建向 LLM 公开数据资源的 Node.js MCP 服务器 | Snyk](https://snyk.io/articles/how-to-build-node-js-mcp-servers-that-expose-data-resources-to-llms/)

**原文标题**: [How to build Node.js MCP Servers that Expose Data Resources to LLMs | Snyk](https://snyk.io/articles/how-to-build-node-js-mcp-servers-that-expose-data-resources-to-llms/)

概述  
本文介绍了如何构建 Node.js MCP 服务器，以向大型语言模型（LLMs）暴露数据资源，包括资源定义、实现步骤及实际应用示例。

- 🧩 MCP 服务器资源允许 LLMs 访问只读数据，如数据库记录、应用状态或文本/二进制数据。  
- 📊 实际资源示例包括公司组织架构图、API 文档服务器和产品 FAQ 指南。  
- 🔗 资源通过唯一 URI 定义，例如`org-chart://company-wide`或`nodejs://releases-schedule-chart.svg`。  
- 🛠️ 使用 Node.js 构建 MCP 服务器时，需通过`server.setRequestHandler`API 处理资源请求。  
- 📂 示例代码展示了如何获取 Node.js 版本发布计划的 SVG 图表，并将其定义为资源。  
- 🔄 资源定义包含 URI、名称、描述、MIME 类型及处理函数，动态解析请求并返回数据。  
- 📜 服务器通过`server.js`和`index.js`文件配置，使用 STDIO 传输与客户端通信。  
- 📚 推荐阅读 MCP 架构初学者指南和 MCP 基础文章，以深入理解其工作原理。  
- 🔒 建议在 AI 编码工具中使用 Snyk CLI MCP 服务器，自动检测代码安全漏洞。  
- 🚀 提供免费 Snyk 账户注册和专家演示预约链接，帮助开发者集成安全方案。

---

### [多仓库 TypeScript 问题](https://www.carrick.tools/blog/the-multi-repository-typescript-problem)

**原文标题**: [The Multi-Repository TypeScript Problem](https://www.carrick.tools/blog/the-multi-repository-typescript-problem)

大型 TypeScript 代码库在分布式团队中常面临单仓库（monorepo）或多仓库（polyrepo）架构选择问题，本文探讨了多仓库环境下跨服务类型安全的挑战与解决方案。

- 🏗️ **架构选择**：单仓库便于共享 TypeScript 类型包，而多仓库因独立部署和团队自治更灵活，但类型管理复杂。
- 🔄 **多仓库类型同步难题**：需通过数据库模式生成类型、发布私有 NPM 包或契约优先（Contract-first）策略，但存在版本更新和契约维护问题。
- 🧩 **类型递归发现**：使用`ts-morph`库提取类型及其依赖，区分本地类型（递归收集）和外部依赖（保留导入）。
- 📦 **便携式类型包**：为每个服务生成包含类型定义和依赖清单的包，上传至共享存储供其他仓库 CI 下载。
- ✅ **类型验证机制**：临时构建 TypeScript 项目，合并依赖后直接利用编译器 API 检查类型兼容性，输出原生错误信息。
- ⚙️ **工程实践洞察**：突破 TypeScript 项目边界需深入编译器内部，平衡性能与准确性，最终实现多仓库类型安全。

---

### [JavaScript 中的逻辑赋值运算符：小语法，大收获 - Matt Smith](https://allthingssmitty.com/2025/07/28/logical-assignment-operators-in-javascript-small-syntax-big-wins/)

**原文标题**: [
    Logical assignment operators in JavaScript: small syntax, big wins - Matt Smith
  ](https://allthingssmitty.com/2025/07/28/logical-assignment-operators-in-javascript-small-syntax-big-wins/)

JavaScript 中的逻辑赋值运算符：简洁语法，高效编码

- 🚀 逻辑赋值运算符是 ES2021 特性，结合逻辑运算符（||、&&、??）和赋值（=），简化条件赋值  
- ⚠️ 注意：可选链（?.）不能用于逻辑赋值左侧，会抛出语法错误  
- 🔄 `||=` 在左侧为假值时赋值，适用于设置默认值，但会覆盖 0、''、false 等有意设置的值  
- 🔄 `&&=` 在左侧为真值时赋值并更新为右侧表达式的结果，即使结果为假值  
- 🔄 `??=` 仅在左侧为 null 或 undefined 时赋值，保留其他假值（如 0、false）  
- 💡 这些运算符直接修改原对象或变量，在不可变工作流中需先克隆对象  
- 🌟 适用场景：组件 props 默认值、全局状态/配置避免覆盖、防止 null/undefined 赋值  
- 🚫 `||=` 会覆盖假值，需注意；`??=` 更安全，仅针对 null/undefined  
- ⚡ 右侧表达式仅在需要时求值，提升性能并避免副作用  
- 🌍 浏览器支持：Chrome 85+、Firefox 79+、Safari 14+、Edge 85+，Node.js 15+，不支持 IE  
- 🔧 旧环境需使用 Babel 等转译器  
- 🛠️ 适用场景：prop/状态管理、API 默认值、表单清理等前端工作流

---

### [AudioTee.js：Node.js 的 macOS 系统音频捕获工具](https://stronglytyped.uk/articles/audioteejs-macos-system-audio-capture-nodejs)

**原文标题**: [AudioTee.js: macOS system audio capture for Node.js](https://stronglytyped.uk/articles/audioteejs-macos-system-audio-capture-nodejs)

AudioTee.js 是一个用于在 Node.js 中捕获 macOS 系统音频的开源库，通过 EventEmitter 接口流式传输 PCM 编码的音频数据。

- 🎧 **简介**：AudioTee.js 是一个 Node.js 库，基于 AudioTee Swift 二进制文件构建，用于捕获 macOS 系统音频并输出 PCM 格式的音频块。  
- 🛠️ **设计方法**：通过子进程调用 Swift 二进制文件，提供符合 Node.js 开发者习惯的 EventEmitter 接口。  
- ⚙️ **配置选项**：支持设置采样率（`sampleRate`）、音频块时长（`chunkDuration`）、静音（`mute`）以及包含/排除特定进程（`includeProcesses`/`excludeProcesses`）。  
- 📌 **当前限制**：仅支持 macOS 14.2+，仅捕获默认输出设备的音频，强制单声道输出，且 API 仍处于 0.x.x 阶段，可能变动。  
- 🔮 **未来计划**：期待用户反馈以改进功能，并鼓励开发者分享使用案例。  
- 📢 **反馈与支持**：欢迎通过 GitHub 提交问题或拉取请求，也支持在 Bluesky 等平台分享文章。

---

### [GitHub - makeusabrew/audioteejs: 一个围绕 Audiotee 的 NodeJS 封装库](https://github.com/makeusabrew/audioteejs)

**原文标题**: [GitHub - makeusabrew/audioteejs: A NodeJS wrapper library around Audiotee](https://github.com/makeusabrew/audioteejs)

概述：  
audioteejs 是一个围绕 Audiotee 的 NodeJS 封装库，用于捕获 Mac 系统音频输出并以 PCM 编码块形式定期发送。支持多种配置选项和事件监听，适用于音频处理场景。

- 🎧 **功能描述**：NodeJS 封装库，捕获 Mac 系统音频输出并生成 PCM 编码块。  
- 📦 **安装方式**：通过 `npm install audiotee` 安装，自动下载预构建的 macOS 二进制文件。  
- ⚙️ **配置选项**：支持采样率、块时长、静音模式、进程过滤等参数。  
- 🔊 **事件监听**：提供 `data`、`start`、`stop`、`error` 和 `log` 等事件，用于处理音频数据和系统消息。  
- 🐞 **已知问题**：0.0.2 及以下版本仅支持 `data` 事件。  
- 🖥️ **系统要求**：需 macOS 14.2 或更高版本。  
- 📜 **许可证**：采用 MIT 许可证，版权归 Nick Payne 所有。  
- 🌟 **项目状态**：0.x.x 版本期间 API 可能不稳定，后续可能变更。

---

### [发布 3.7.0 版 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.7.0)

**原文标题**: [Release 3.7.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.7.0)

Transformers.js 发布了 3.7.0 版本，新增了对 Voxtral、LFM2 和 ModernBERT Decoder 三种新模型架构的支持，并包含其他改进。

- 🚀 **新模型支持**  
  - 新增 Voxtral、LFM2 和 ModernBERT Decoder 三种架构。  

- 🎙️ **Voxtral 模型**  
  - 基于 Ministral 3B 增强，具备先进的音频输入能力，擅长语音转录、翻译和音频理解。  
  - 提供 ONNX 权重和在线演示示例。  

- ⚡ **LFM2 模型**  
  - 由 Liquid AI 开发，专为边缘 AI 和本地部署设计，提供 350M、700M 和 1.2B 三种参数规模。  
  - 支持文本生成任务。  

- 🔍 **ModernBERT Decoder 模型**  
  - 属于 Ettin 套件的一部分，提供编码器和解码器架构的公平比较，支持多种规模。  

- 🛠️ **其他改进**  
  - 在文本生成管道中添加了特殊令牌支持。  
  - 完整更新日志可查看 3.6.3 到 3.7.0 的变更。

---

### [Node.js 中的服务器端推理](https://huggingface.co/docs/transformers.js/tutorials/node)

**原文标题**: [Server-side Inference in Node.js](https://huggingface.co/docs/transformers.js/tutorials/node)

Transformers.js 文档介绍了如何在 Node.js 环境中进行服务器端推理，使用 JavaScript 实现情感分析等功能。

- 🏠 **Transformers.js 概述**：支持浏览器和服务器端推理，适用于 Node.js 项目。
- 🔧 **安装与设置**：通过 npm 安装 Transformers.js，创建 Node.js 项目并配置入口文件。
- 📦 **模块系统支持**：支持 ECMAScript 模块 (ESM) 和 CommonJS，分别使用 `import/export` 和 `require/module.exports`。
- 🚀 **示例应用**：构建一个简单的 HTTP 服务器，通过 `/classify` 端点进行文本情感分析。
- 🛠️ **自定义管道**：使用 `MyClassificationPipeline` 类实现单例模式，延迟加载模型。
- ⚙️ **服务器配置**：监听本地端口，处理请求并返回 JSON 格式的推理结果。
- 💾 **模型缓存**：默认缓存模型文件，支持自定义缓存路径和本地模型加载。
- 🔒 **远程模型控制**：可禁用从 Hugging Face Hub 加载远程模型，仅使用本地模型。
- 📌 **前提条件**：需要 Node.js 18+ 和 npm 9+ 版本。

---

### [Ruby on Rails、Elixir、Node.js 和 Python 应用监控](https://www.appsignal.com/?utm_source=cooperpress&utm_medium=cooperpress&utm_term=node_nl)

**原文标题**: [Application Monitoring for Ruby on Rails, Elixir, Node.js & Python](https://www.appsignal.com/?utm_source=cooperpress&utm_medium=cooperpress&utm_term=node_nl)

应用性能监控工具 AppSignal 提供全面的监控解决方案，帮助开发者快速定位并解决问题，确保应用稳定运行。

- 🚀 **轻松监控**：安装简单，使用便捷，设计强大，从警报到修复一气呵成。  
- 🐞 **错误追踪**：实时警报、详细报告、自定义标签，轻松调试并修复错误。  
- ⏱ **性能监控**：精确到纳秒级的性能分析，定位并优化慢查询。  
- 🖥 **主机监控**：全面监控服务器 CPU、磁盘、网络等关键指标。  
- 🔍 **异常检测**：自定义指标警报，智能降噪，支持多渠道通知。  
- 🌐 **可用性监控**：全球节点监测，30 秒间隔检测，实时宕机通知。  
- 📊 **指标仪表盘**：自动生成或自定义仪表盘，支持数据导出与对比。  
- 📝 **日志管理**：集中管理日志，快速搜索并关联错误与性能问题。  
- ⏳ **签到监控**：监控后台任务与进程，提供详细的性能分析。  
- 💡 **多语言支持**：支持 Ruby、Elixir、Node.js、JavaScript、Python 等多种语言及框架。  
- 🛠 **一体化界面**：九大功能集成，界面简洁易用，快速定位问题。  
- ⚡ **快速安装**：5 分钟内完成安装，自动配置，低学习成本。  
- 🔒 **合规与稳定**：GDPR 合规，99.999% 高可用性，轻量级 Rust 代理。  
- 👨‍💻 **开发者支持**：专业的技术支持团队，确保用户体验。  
- 🆓 **免费试用**：提供 30 天免费试用，无需信用卡，全功能开放。

---

### [Ruby on Rails、Elixir、Node.js 和 Python 的应用监控](https://www.appsignal.com/?utm_source=cooperpress&utm_medium=cooperpress&utm_term=node_nl)

**原文标题**: [Application Monitoring for Ruby on Rails, Elixir, Node.js & Python](https://www.appsignal.com/?utm_source=cooperpress&utm_medium=cooperpress&utm_term=node_nl)

应用性能监控（APM）工具，提供错误追踪、性能监控、主机监控等九大功能，支持多种编程语言和框架，安装简便，界面友好，适合开发团队快速定位和解决问题。

- 🚀 **轻松监控，自信编程**：快速从警报到修复，客户无感知。  
- 🔍 **错误追踪**：实时警报、详细报告、自定义标签和筛选功能。  
- ⏱ **性能监控**：精确到纳秒的性能分析，慢查询定位与修复。  
- 🖥 **主机监控**：全面监控 CPU、磁盘、网络等服务器指标。  
- 🚨 **异常检测**：自定义指标警报，智能降噪，多渠道通知。  
- 🌐 **可用性监控**：全球节点监测，30 秒间隔检测，实时宕机通知。  
- 📊 **指标仪表盘**：自动生成与自定义仪表盘，支持数据导出与对比。  
- 📝 **日志管理**：集中化日志，简单搜索，关联错误与性能问题。  
- ⏳ **后台任务监控**：定时任务与持续进程监控，遗漏警报与性能分析。  
- 💡 **多语言支持**：覆盖 Ruby、Elixir、Node.js、Python 等主流语言及框架。  
- 🛠 **五分钟快速接入**：简洁安装指南，低学习曲线，自动配置。  
- 🔒 **合规与稳定**：GDPR 合规，99.999% 可用性，轻量级 Rust 代理。  
- ❤️ **用户口碑**：1500+ 开发团队信赖，提供客户案例参考。  
- 🆓 **免费试用**：30 天全功能试用，无需信用卡，一键开启监控。

---

### [GitHub - kentcdodds/match-sorter: JavaScript 数组的简单、可预期且确定性最佳匹配排序](https://github.com/kentcdodds/match-sorter)

**原文标题**: [GitHub - kentcdodds/match-sorter: Simple, expected, and deterministic best-match sorting of an array in JavaScript](https://github.com/kentcdodds/match-sorter)

match-sorter 是一个简单、直观且确定性最佳匹配排序的 JavaScript 数组工具库，适用于智能过滤和排序场景。

- 🚀 **项目概况**: 由 kentcdodds 开发，4k stars，135 forks，MIT 许可证
- 🎯 **核心功能**: 提供用户友好的多级匹配算法（如精确匹配、开头匹配、模糊匹配等）
- 🔧 **高级选项**: 支持多键排序、嵌套对象、自定义阈值、保留变音符号等
- 📦 **安装使用**: npm 包 `match-sorter`，支持数组和对象列表的智能排序
- 🌍 **应用场景**: 国家列表匹配示例展示多级排序逻辑（如"ua"优先匹配"Uruguay"而非"United States"）
- ⚙️ **自定义配置**: 可设置最小/最大排名、自定义排序函数、多字段联合搜索等
- 🔍 **特色方案**: 支持 PascalCase/camelCase 等格式匹配，提供多字段表格过滤方案
- 🤝 **社区贡献**: 41 位贡献者，提供完善的 issue 模板和代码规范
- 🔗 **资源**: 包含演示案例、问题追踪和贡献指南

---

### [无标题](https://codesandbox.io/p/sandbox/wyk856yo48?file=%2Findex.js)

**原文标题**: [No title found](https://codesandbox.io/p/sandbox/wyk856yo48?file=%2Findex.js)

好的，请提供需要总结的文本内容，我会按照您要求的模板生成概述和带表情符号的要点列表。  

示例模板：  

概述总结放在这里  

- 📌 要点 1  
- 🔍 要点 2  
- 💡 要点 3  

请提供具体文本，我会为您生成符合要求的总结。

---

### [GitHub - SBoudrias/Inquirer.js：一系列常见的交互式命令行用户界面](https://github.com/SBoudrias/Inquirer.js)

**原文标题**: [GitHub - SBoudrias/Inquirer.js: A collection of common interactive command line user interfaces.](https://github.com/SBoudrias/Inquirer.js)

Inquirer.js 是一个用于创建交互式命令行用户界面的工具集合，支持多种常见提示类型，如输入、选择、确认等，适用于 Node.js 环境。

- 🚀 **项目概述**：Inquirer.js 提供了一系列常见的交互式命令行用户界面工具，适用于 Node.js 环境。
- 📦 **安装方式**：可以通过 npm 或 yarn 安装，命令分别为 `npm install @inquirer/prompts` 和 `yarn add @inquirer/prompts`。
- 🔄 **版本更新**：项目最近进行了重写，以减少包大小并提高性能，旧版本仍维护但不活跃开发。
- 💡 **使用示例**：支持多种提示类型，如输入、选择、确认等，每种提示都有详细的文档和示例。
- 🛠 **高级功能**：支持自定义提示、取消提示、处理 `ctrl+c` 退出等高级功能。
- 📜 **许可证**：项目采用 MIT 许可证，由 Simon Boudrias 维护。
- 🌟 **社区贡献**：鼓励社区贡献新的提示类型，已有多种社区开发的提示可供使用。
- 📊 **项目活跃度**：项目拥有 21k 星标、1.3k 分叉，被超过 1000 万项目使用。

---

### [GitHub - vercel/nft: Node.js 依赖追踪工具](https://github.com/vercel/nft)

**原文标题**: [GitHub - vercel/nft: Node.js dependency tracing utility](https://github.com/vercel/nft)

Vercel 的 NFT（Node File Trace）是一个用于确定应用程序运行时所需文件的 Node.js 依赖追踪工具，类似于 @vercel/ncc，但不进行打包，不依赖 webpack。

- 🚀 **功能**：用于确定应用程序运行时所需的文件（包括 node_modules），实现树摇效果而不移动资源或二进制文件。  
- 📦 **安装**：通过 `npm i @vercel/nft` 安装，提供源文件列表作为输入。  
- ⚙️ **选项**：支持自定义基础路径、处理当前工作目录、导出和导入条件、路径解析等。  
- 🔍 **分析**：默认进行尽可能多的分析以确保不遗漏任何可能需要的文件，支持自定义分析选项。  
- 🚫 **忽略**：支持自定义忽略文件或函数，跳过文件包含和分析。  
- 💾 **缓存**：支持通过缓存对象在构建之间持久化文件缓存。  
- 📊 **原因**：提供文件包含的底层原因，包括文件类型、是否被忽略和父文件列表。  
- 🔧 **高级功能**：支持 TypeScript 文件解析、文件 IO 并发控制、自定义解析钩子等。  
- 📜 **许可证**：MIT 许可证，开源且免费使用。

---

### [发布 v6.18.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.18.0)

**原文标题**: [Release v6.18.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.18.0)

MongoDB Node.js 驱动版本 6.18.0 发布，包含新功能、改进和错误修复，同时弃用了一些内部使用的 API。

- 🆕 新增 `appendMetadata` API，允许客户端在构建后添加握手元数据  
- ⏳ 游标现在延迟实例化会话，避免不必要的会话创建  
- 🔧 修复了 `minPoolSize=0` 时闲置连接未清理的问题  
- 🕒 `ChangeStream` 事件接口新增 `wallTime` 属性  
- 📊 `CommandSucceededEvent` 和 `CommandFailedEvent` 新增 `databaseName` 属性  
- ⚠️ 弃用仅供内部使用的 `Transaction` 状态获取器和 `ClientMetadata` 等类型  
- 🚫 弃用意外公开的 `CommandOptions.noResponse` 选项  
- 🐛 修复了多个错误，包括游标会话管理和闲置连接清理  
- 📚 更新了文档和参考 API，鼓励用户试用并反馈问题

---

### [GitHub - animir/node-rate-limiter-flexible: 原子计数器和速率限制工具。支持任意规模的资源访问限制。](https://github.com/animir/node-rate-limiter-flexible)

**原文标题**: [GitHub - animir/node-rate-limiter-flexible: Atomic counters and rate limiting tools. Limit resource access at any scale.](https://github.com/animir/node-rate-limiter-flexible)

node-rate-limiter-flexible 是一个灵活的限流工具，支持多种存储后端，用于防止 DDoS 和暴力攻击。

- 🚀 **多存储支持**：支持 Valkey、Redis、Memcached、MongoDB、MySQL、PostgreSQL 等多种存储后端。
- ⚡ **高性能**：分布式环境下平均请求耗时仅 0.7ms（集群）和 2.5ms（分布式应用）。
- 🔧 **灵活配置**：支持组合限流器、延迟操作、智能内存阻塞等功能。
- 🛡️ **防竞争条件**：所有操作使用原子增量，避免竞争条件。
- 🌐 **浏览器兼容**：内存限流器可在浏览器中使用。
- 📊 **固定窗口算法**：相比滚动窗口更快，性能更优。
- 📦 **易用性**：提供统一 API，支持多种 Node 驱动（如 redis、ioredis、mongoose 等）。
- 🛠️ **扩展性**：支持动态阻塞、保险策略、集群限流等功能。
- 📚 **丰富文档**：提供中间件（Express、Koa、Hapi）、插件和示例代码。
- 🔄 **无生产依赖**：轻量级，无额外依赖。

示例代码：
```javascript
const rateLimiter = new RateLimiterMemory({ points: 6, duration: 1 });
rateLimiter.consume(remoteAddress, 2)
  .then(() => { /* 成功 */ })
  .catch(() => { /* 限流 */ });
```

---

### [细雨 · animir/node-rate-limiter-flexible Wiki · GitHub](https://github.com/animir/node-rate-limiter-flexible/wiki/Drizzle)

**原文标题**: [Drizzle · animir/node-rate-limiter-flexible Wiki · GitHub](https://github.com/animir/node-rate-limiter-flexible/wiki/Drizzle)

该内容介绍了如何使用 `rate-limiter-flexible` 库的 `RateLimiterDrizzle` 模块与 PostgreSQL 数据库结合实现请求速率限制。

- 🚀 **项目概览**: `node-rate-limiter-flexible` 是一个灵活的限流库，支持多种存储后端，包括 PostgreSQL。
- 📊 **项目数据**: 该项目有 3.3k 星标，175 个 fork，16 个 issues 和 4 个 pull requests。
- 🛠 **Drizzle 集成**: 使用 `RateLimiterDrizzle` 需要配置 Drizzle ORM 和 PostgreSQL 数据库。
- 📝 **配置步骤**:
  - 创建 `schema.js` 定义限流表结构。
  - 创建 `drizzle.config.js` 配置数据库连接。
  - 运行 `npx drizzle-kit push` 推送表结构到数据库。
- ⚙ **使用示例**: 通过 `rateLimiter.consume(userId, 1)` 消费限流点数，处理请求过多时返回 429 状态码。
- 🔄 **灵活性**: 可以使用任何标识符（如用户 ID、邮箱或 IP 地址）进行限流。
- 📚 **扩展内容**: 该库还支持多种其他存储后端和限流策略，如 Redis、MongoDB、内存等。

---

### [发布 6.0.0-rc.0 版 · TryGhost/Ghost · GitHub](https://github.com/TryGhost/Ghost/releases/tag/v6.0.0-rc.0)

**原文标题**: [Release 6.0.0-rc.0 · TryGhost/Ghost · GitHub](https://github.com/TryGhost/Ghost/releases/tag/v6.0.0-rc.0)

Ghost 项目发布了 v6.0.0-rc.0 预发布版本，包含多项功能更新、安全修复和移除的旧功能。

- ✨ 新增原生 Web Analytics 支持（Tinybird 集成）和 ActivityPub 联邦功能（社交网络支持）  
- 🔒 通过 Punycode 域名防止同形异义字攻击，增强会员登录安全  
- 🎨 确保所有者用户创建时使用 ObjectID，提升数据一致性  
- 🐛 修复主题资源 404 渲染问题  
- 🔥 移除多项功能：无扩展名的主题文件服务、mobiledoc 字段、AMP 核心支持、Node.js v18/v20 支持等  
- ⚠️ 新增 API 限制：{{#get}} 助手和 API 请求的 ?limit 参数最大值设为 100  
- 📅 版本包含 39 次提交，基于 v5.130.2 的变更日志可查看完整详情

---

### [GitHub - googleapis/nodejs-bigtable: Google Cloud Bigtable 的 Node.js 客户端：谷歌的 NoSQL 大数据数据库服务](https://github.com/googleapis/nodejs-bigtable)

**原文标题**: [GitHub - googleapis/nodejs-bigtable: Node.js client for Google Cloud Bigtable: Google's NoSQL Big Data database service.](https://github.com/googleapis/nodejs-bigtable)

Node.js 的 Google Cloud Bigtable 客户端库，用于访问 Google 的 NoSQL 大数据数据库服务。

- 🚀 **项目简介**: Node.js 客户端库，用于 Google Cloud Bigtable，支持 NoSQL 大数据服务。  
- 📜 **许可证**: 采用 Apache-2.0 许可证。  
- ⭐ **关注度**: 105 个 star，63 个 fork。  
- 🔄 **版本控制**: 遵循语义化版本控制 (Semantic Versioning)，当前为稳定版本。  
- 📚 **文档**: 提供详细的 API 参考文档和示例代码。  
- 🔧 **安装**: 通过 npm 安装`@google-cloud/bigtable`即可使用。  
- 📝 **示例代码**: 包含快速入门、实例操作、读写片段等多种示例。  
- 🔗 **资源**: 提供 GitHub 仓库、官方文档和贡献指南链接。  
- 🌍 **多语言支持**: 主要使用 TypeScript(98.1%)，少量 JavaScript(1.8%) 和 Python(0.1%)。  
- 🤝 **贡献**: 欢迎贡献，需遵循贡献指南。

---

### [发布版本 v1.11.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.11.0)

**原文标题**: [Release Release v1.11.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.11.0)

axios 项目 GitHub 页面加载异常，部分功能需刷新访问。最新版本 v1.11.0 修复了多项问题，包括 form-data 包错误和大 Buffer 导致的 RangeError 等，并有 4 位贡献者参与。社区反应热烈，共收到 28 次表情互动。

- 🚨 页面加载错误提示需刷新访问  
- 🔄 项目动态含代码、议题、安全等导航选项  
- 🛠️ 版本 v1.11.0 修复 form-data 包及 Buffer 类型问题  
- 📜 发布说明包含 3 项关键修复提交  
- 👥 4 位贡献者参与本次版本更新  
- 👍 社区互动积极，获 20 次点赞等共 28 次表情反馈

---

### [GitHub - image-js/tiff：完全用JavaScript编写的TIFF图像解码器](https://github.com/image-js/tiff)

**原文标题**: [GitHub - image-js/tiff: TIFF image decoder written entirely in JavaScript](https://github.com/image-js/tiff)

这是一个基于 JavaScript 的 TIFF 图像解码器库，支持多种图像格式和压缩算法。

- 📜 **项目名称**: image-js/tiff  
- 🌟 **Stars**: 215  
- 🍴 **Forks**: 19  
- 📜 **许可证**: MIT  
- 🛠️ **功能**: 完全用 JavaScript 编写的 TIFF 图像解码器，支持灰度、RGB 图像（8/16/32 位）、LZW 压缩和带 Alpha 通道的图像  
- 📦 **安装**: `npm install tiff`  
- 📄 **API**: 提供`tiff.decode()`解码文件并返回 TIFF IFDs，`tiff.pageCount()`返回文件中的 IFD 数量  
- 🔧 **兼容性**: 支持 Zlib/deflate 压缩算法的图像  
- 📊 **IFD 对象**: 包含图像数据（如`data`属性为 Typed Array）、尺寸、分辨率等信息  
- 🌐 **资源**: 官网链接 [image-js.github.io/tiff/](https://image-js.github.io/tiff/)  
- 👥 **维护者**: Zakodium  
- 📌 **主题**: nodejs, javascript, image, tiff, image-decoder

---

### [ESLint v9.32.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/07/eslint-v9.32.0-released/)

**原文标题**: [ESLint v9.32.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/07/eslint-v9.32.0-released/)

ESLint v9.32.0 是一个小版本升级，新增了功能并修复了之前版本中的多个错误。主要更新包括对显式资源管理语法的规则支持以及对 TypeScript 访问器的增强支持。

- 🚀 **核心规则更新**：支持显式资源管理语法（`using` 和 `await using`），避免解析错误并优化未使用变量的处理。
- 🔧 **TypeScript 访问器支持**：增强 `accessor-pairs` 和 `grouped-accessor-pairs` 规则，支持 TypeScript 接口和类型字面量中的访问器检查。
- 🐞 **错误修复**：包括升级依赖、重构报告逻辑、修复 `no-implied-eval` 规则中的全局引用问题等。
- 📚 **文档更新**：更新 README 和其他相关文档。
- 🔄 **维护与测试**：包括切换到扁平配置模式、更新性能测试工具等。

---

### [Platformatic AI-Warp 1.0.0](https://blog.platformatic.dev/ai-warp-1-0-0)

**原文标题**: [Platformatic AI-Warp 1.0.0](https://blog.platformatic.dev/ai-warp-1-0-0)

Platformatic AI-Warp 1.0.0 是一款专为现代应用设计的终极 AI 网关解决方案，旨在简化开发者集成多 AI 提供商的过程，提供统一、可扩展的智能平台。

- 🚀 **AI 网关解决方案**：Platformatic AI-Warp 1.0.0 正式发布，为开发者提供全面的 AI 操作平台，解决生产级 AI 应用开发中的复杂问题。  
- 🔄 **无缝会话恢复**：支持跨服务重启、负载均衡切换和分布式部署的会话连续性，确保对话上下文不丢失。  
- 🌐 **统一 API 接口**：通过单一接口连接 OpenAI、DeepSeek 和 Google Gemini 等 AI 提供商，无需更改应用代码即可切换模型。  
- 🔄 **智能自动回退**：当主模型遇到速率限制或故障时，自动切换到备用模型，确保服务可靠性。  
- 💾 **企业级会话管理**：支持内存存储或分布式 Valkey/Redis 存储，适用于多实例部署，轻松维护会话上下文。  
- 🌊 **实时流式传输**：支持服务器发送事件（SSE）流式传输，具备自动恢复功能，确保故障容忍和带宽效率。  
- 🛡️ **生产级可靠性**：优化的 HTTP 客户端、连接池、优雅降级和错误恢复机制，确保服务稳定运行。  
- 📈 **灵活部署与扩展**：支持自托管、Kubernetes、Docker 等多种部署方式，具备分布式架构和速率限制管理功能。  
- ⚡ **快速入门**：通过简单的命令行工具或安装客户端库，几分钟内即可启动生产级 AI 服务。  
- 🚧 **未来计划**：支持更多 AI 提供商（如 Anthropic Claude、Cohere）、高级路由、分析仪表板和插件生态系统。  
- 📖 **社区与支持**：提供详细文档、社区交流和问题反馈渠道，助力开发者快速上手。  

Platformatic AI-Warp 1.0.0 现已可用，帮助开发者构建聊天机器人、内容生成器等创新 AI 应用。

---

### [GitHub - glitternetwork/pinme：一键部署你的前端应用](https://github.com/glitternetwork/pinme)

**原文标题**: [GitHub - glitternetwork/pinme: Deploy Your Frontend in a Single Command](https://github.com/glitternetwork/pinme)

PinMe 是一个简单易用的命令行工具，用于将文件和目录上传到 IPFS 网络。

- 🌐 **项目网站**：[https://pinme.eth.limo/](https://pinme.eth.limo/)  
- 🚀 **功能特点**：快速上传文件到 IPFS、支持多种文件类型、查看上传历史、自动生成 IPFS 链接、预览内容  
- 📦 **安装方式**：  
  - `npm install -g pinme`  
  - `yarn global add pinme`  
- 📂 **使用命令**：  
  - `pinme upload`（交互式上传）  
  - `pinme rm`（移除文件）  
  - `pinme list`（查看上传历史）  
  - `pinme help`（获取帮助）  
- ⚠️ **上传限制**：单文件 ≤20MB，目录 ≤500MB  
- 📍 **日志存储**：  
  - Linux/macOS：`~/.pinme/`  
  - Windows：`%USERPROFILE%\.pinme\`  
- 📜 **许可证**：MIT License  
- 💡 **使用技巧**：上传 Vite 项目时需配置 `base: "./"`  
- 📧 **联系方式**：  
  - GitHub Issues  
  - Email: pinme@glitterprotocol.io  
- ⭐ **项目数据**：274 Stars · 17 Forks · 2 Contributors

---

### [开发者如何利用 Postmark 打造一款通过电子邮件控制的 Game Boy 模拟器 | Postmark](https://postmarkapp.com/blog/how-a-developer-built-an-email-controlled-game-boy-emulator-with-postmark-because-why-not)

**原文标题**: [
      How a dev built an email-controlled Game Boy Emulator with Postmark. | Postmark  ](https://postmarkapp.com/blog/how-a-developer-built-an-email-controlled-game-boy-emulator-with-postmark-because-why-not)

一名开发者 Rens Wolters 利用 Postmark 的 Inbound 功能，打造了一款通过电子邮件控制的 Game Boy Advance 模拟器 PostmarkGBA，将传统游戏与现代通讯方式结合，意外成为社交体验。

- 🎮 项目灵感源于将邮件作为游戏引擎，最终选择支持现有游戏如《宝可梦》，因其已有“Twitch Plays”社区基础，模拟器兼容所有 GBA 游戏。
- 🖥️ 开发过程中，Windows 上快速实现，但在 Raspberry Pi 部署时遇到 Node 版本过时和截图库问题，最终通过键盘输入和 RetroArch 配置解决截图功能。
- 📧 利用 Postmark 的 Inbound 处理功能，设计上接受所有邮件输入，宽松处理错误，确保用户总能得到反馈，提升交互体验。
- 💡 开发建议：享受过程，不必过分追求效率或盈利，保持乐趣是关键，失败也是学习的一部分。
- 👥 项目意外成为社交平台，朋友们通过邮件协作、分享攻略，提供反馈，增强了项目的互动性和趣味性。
- 🌟 展示了 Postmark Inbound 处理的强大灵活性，能够支持创意项目，鼓励开发者探索非常规想法。

---

### [错误](https://nodeweekly.com/link/172365/web)

**原文标题**: [Error](https://nodeweekly.com/link/172365/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/172365/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [ES 工具包](https://es-toolkit.dev/)

**原文标题**: [es-toolkit](https://es-toolkit.dev/)

最佳性能  
es-toolkit 在现代 JavaScript 运行时中的性能比其他库高出 2-3 倍。  

- 🚀 es-toolkit 性能卓越，比同类库快 2-3 倍  
- ⚡ 专为现代 JavaScript 运行时优化

---

### [HTML 2025 现状](https://survey.devographics.com/en-US/survey/state-of-html/2025)

**原文标题**: [State of HTML 2025](https://survey.devographics.com/en-US/survey/state-of-html/2025)

2023 年，在 State of JS 和 State of CSS 调查进行数年后，团队意识到缺少对 HTML 技术的关注，因此推出了首个 State of HTML 调查，由 Lea Verou 领导，创下新调查记录并引入新 UI 范式。2025 年，调查新增 35 项功能及两个新板块，结果将影响浏览器厂商的未来规划。  

- 🌐 2023 年推出首个 State of HTML 调查，填补技术空白  
- 🚀 由 Lea Verou 领导，首年吸引 21,000 名受访者  
- ✨ 2025 年新增 35 项功能及“图形与多媒体”“性能”板块  
- 📊 调查结果将影响浏览器厂商的路线图  
- ⏳ 填写时间约 10-15 分钟，面向所有网页开发者  
- 📅 调查时间：2025 年 7 月 15 日至 8 月 15 日，9 月发布结果  
- 🔍 目标：衡量新 HTML 功能认知度，追踪使用趋势  
- 🌍 数据公开，供开发者及厂商使用  
- 👥 由 Devographics 及志愿者团队运营，社区参与设计  
- 💬 提供多语言翻译支持，欢迎协助翻译

---

### [马里乌斯 . 制表符与空格之争：战争已结束](https://xn--gckvb8fzb.com/tabs-vs-spaces-the-war-is-over/)

**原文标题**: [ããªã¦ã¹ . Tabs vs. Spaces: The War Is Over
](https://xn--gckvb8fzb.com/tabs-vs-spaces-the-war-is-over/)

编程语言中关于缩进使用制表符（Tabs）还是空格（Spaces）的长期争论似乎已经有了明确的结果，大多数主流语言和标记格式倾向于使用空格。

- 🔍 编程语言中关于缩进使用制表符还是空格的争论由来已久，但数据显示空格已成为主流选择。  
- 📊 调查显示约 90% 的主流编程语言和标记格式默认使用空格进行缩进，如 Python、JavaScript、Ruby 等。  
- ⚙️ 少数语言如 Go、Odin、Hare 和汇编语言明确推荐使用制表符，而 C/C++ 则视项目而定。  
- 🏆 Go 语言通过工具强制使用制表符，而非仅依赖风格指南，成为少数例外之一。  
- 🌍 空格缩进的普及类似于全球采用公制单位或右侧交通的趋势，反映了标准化的重要性。  
- ❓ 尽管空格明显占优，但这场争论是否真的结束仍存疑问，技术文化中的选择往往难以完全统一。  
- 📅 文章发布于 2025-07-24，并于 2025-07-25 更新，归类于“journal”并标记为“command-line”、“society”、“text”、“zig”。

---

