### [Node 周刊第 584 期：2025 年 7 月 1 日](https://nodeweekly.com/issues/584)

**原文标题**: [Node Weekly Issue 584: July 1, 2025](https://nodeweekly.com/issues/584)

Node.js 和 JavaScript 生态的最新动态，包括版本更新、工具发布、技术文章和行业新闻。

- 🚀 **Node.js 2025 年现代模式** — Ashwin 探讨了 Node.js 的 ES 模块、内置 Web API、测试运行器等新特性。  
- 🔧 **Node v22.17.0 (LTS) 发布** — 包含 `assert.partialDeepStrictEqual()` 稳定化及实验性 API 的改进。  
- 📜 **ECMAScript 2025 获批** — 新语言规范发布，Dr. Axel 提供了简明解读。  
- 🛡️ **Express.js 快速授权** — Cedar 语言为 Express.js 应用提供权限管理支持。  
- 🤖 **AI 代码审查工具** — CodeRabbit 在 VS Code 等 IDE 中提供免费 AI 代码审查。  
- ⚡ **V8 引擎优化** — WebAssembly 通过去优化和内联实现性能提升。  
- 📦 **工具更新** — Marked 16.0（Markdown 解析器）、Transformers.js 3.6（支持 Gemma 3n 模型）、Electron v37.0.0 等发布。  
- 📰 **行业动态** — Deno 展望 JavaScript 新特性、JSConf 2025 演讲阵容公布、Cloudflare Containers 推出。  
- 📢 **其他新闻** — Temporal API 进入 Stage 3、Postgres 支持 JavaScript 函数（PLJS）。

---

### [2025 年现代 Node.js 模式](https://kashw1n.com/blog/nodejs-2025/)

**原文标题**: [Modern Node.js Patterns for 2025](https://kashw1n.com/blog/nodejs-2025/)

Node.js 在 2025 年的现代模式演进，从 CommonJS 到 ESM 模块化、内置 Web API、测试工具到异步模式优化，全面提升开发体验与性能。

- 📦 **模块系统**：ESM 成为新标准，支持`node:`前缀明确核心模块，替代传统 CommonJS 的`require`语法  
- 🌐 **内置 Web API**：原生集成 Fetch API 和 AbortController，减少对`axios`等第三方库的依赖  
- 🧪 **内置测试工具**：无需 Jest/Mocha，直接使用`node:test`实现完整测试套件  
- ⚡ **异步模式升级**：顶层 await 简化初始化，AsyncIterators 优化事件流处理  
- 🌊 **现代流处理**：兼容 Web Streams 标准，`pipeline`函数提供更健壮的流式错误处理  
- 🧵 **Worker Threads**：通过独立线程处理 CPU 密集型任务，避免阻塞主线程  
- 🔍 **开发体验优化**：内置`--watch`模式和环境变量加载，替代 nodemon 和 dotenv  
- 🔒 **安全增强**：实验性权限模型可限制文件/网络访问，遵循最小权限原则  
- 📊 **性能监控**：原生 Performance Hooks 实现 APM 基础功能，无需额外工具  
- 📦 **应用分发**：实验性单可执行文件 (SEA) 功能简化部署  
- 🛠 **错误诊断**：结构化错误类和 Diagnostics Channel 提供更丰富的调试信息  
- 🗂 **包管理革新**：Import Maps 支持别名路径，动态导入实现按需加载

---

### [Node.js — Node v22.17.0（长期支持版）](https://nodejs.org/en/blog/release/v22.17.0)

**原文标题**: [Node.js — Node v22.17.0 (LTS)](https://nodejs.org/en/blog/release/v22.17.0)

Node.js v22.17.0 (LTS) 版本发布，包含多项功能改进、弃用警告和社区更新。

- ⚠️ **弃用警告**  
  - 不推荐使用 `new` 关键字实例化 `node:http` 类（如 `IncomingMessage` 或 `ServerResponse`）。  
  - 避免在 `node:child_process` 中使用 `options.shell = ""`，建议明确指定 `shell: true` 或路径。  
  - HTTP/2 优先级信号 API（如 `stream.priority`）已弃用，未来可能移除。  

- ✅ **稳定功能**  
  - `assert.partialDeepStrictEqual()` 方法支持部分属性深度比较，适用于灵活测试断言。  

- 🔧 **新功能与改进**  
  - `fs.FileHandle.readableWebStream` 新增 `autoClose` 选项，控制文件描述符自动关闭。  
  - `fs.Dir` 支持显式资源管理（如 `.close()` 或 `Symbol.asyncDispose`）。  
  - HTTP/2 新增诊断通道 `http2.server.stream.finish`，便于监控流完成事件。  
  - 权限模型默认允许对入口文件的读取访问（`allow-fs-read`）。  
  - `util.styleText()` 新增 `'none'` 样式，用于清除终端样式。  

- 🧑‍💻 **社区更新**  
  - 新增多位贡献者加入 TSC 和协作者列表。  

- 📦 **其他改进**  
  - 多项 API 和工具优化，包括文件系统性能提升、错误处理改进和依赖库更新。  

- 📥 **下载支持**  
  - 提供多平台安装包和二进制文件（Windows、macOS、Linux 等）。  

完整变更和下载链接详见 [Node.js 官方文档](https://nodejs.org/docs/v22.17.0/api/)。

---

### [Node.js — Node v24.3.0（当前版本）](https://nodejs.org/en/blog/release/v24.3.0)

**原文标题**: [Node.js — Node v24.3.0 (Current)](https://nodejs.org/en/blog/release/v24.3.0)

Node.js v24.3.0 (Current) 版本发布，包含多项功能改进、错误修复和依赖项更新。

- 🚀 **重要变更**：添加了 Shima Ryuhei 作为协作者。
- 🔄 **SEMVER-MINOR**：fs 模块现在支持 AsyncIterator 正确处理 fs-events 中的突发情况。
- 📦 **模块改进**：移除了类型剥离的实验性警告。
- 🛠️ **测试修复**：修复了测试超时标志的问题，并恢复了自动子测试等待的功能。
- 🔧 **对象模拟**：test_runner 现在支持对象属性模拟。
- 📂 **新 API**：url 模块新增了 fileURLToPathBuffer API。
- 🔄 **依赖更新**：更新了多个依赖项，包括 nghttp2、acorn、npm、sqlite 等。
- 📚 **文档修正**：修复了多个文档问题，包括错误的 RFC 编号和稳定性链接。
- 🖥️ **平台支持**：提供了多种平台的安装包和二进制文件，包括 Windows、macOS、Linux 等。
- 🔒 **安全**：更新了 SHASUMS 和 PGP 签名以确保下载的安全性。

---

### [错误](https://nodeweekly.com/link/171108/web)

**原文标题**: [Error](https://nodeweekly.com/link/171108/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='2ality.com', port=443): Max retries exceeded with url: /2025/06/ecmascript-2025.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [ECMAScript® 2025 语言规范](https://tc39.es/ecma262/2025/)

**原文标题**: [ECMAScript® 2025 Language Specification](https://tc39.es/ecma262/2025/)

总结失败：Error code: 400 - {'error': {'message': "This model's maximum context length is 65536 tokens. However, you requested 611050 tokens (603050 in the messages, 8000 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

### [使用 Cedar 在 5 分钟内保护您的 Express 应用 API | AWS 开源博客](https://aws.amazon.com/blogs/opensource/secure-your-application-apis-in-5-minutes-with-cedar/)

**原文标题**: [Secure your Express application APIs in 5 minutes with Cedar | AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/secure-your-application-apis-in-5-minutes-with-cedar/)

AWS 开源博客宣布发布`authorization-for-expressjs`包，帮助开发者快速为 Express 应用 API 添加基于 Cedar 策略语言的授权功能。

- 🚀 Cedar 发布新包`authorization-for-expressjs`，支持 Express 框架快速集成策略授权  
- ⏱️ 仅需 5 分钟即可完成 API 授权部署，无需远程服务调用  
- 💻 相比自定义集成代码减少 90% 工作量，提升安全性和开发效率  
- 🐾 示例宠物商店应用展示如何限制不同用户组（顾客/员工）的 API 访问权限  
- 🔗 通过 OpenAPI 规范自动生成 Cedar 策略架构，简化策略定义流程  
- 📝 提供策略模板生成工具，支持细粒度权限控制（如`POST /pets`仅限员工访问）  
- 🔄 将授权逻辑与业务代码解耦，解决传统嵌入式授权难以维护的问题  
- 🛠️ 配套提供 Cedar 分析 CLI 工具，支持复杂策略的审计验证  
- 📦 开源 NPM 包支持中间件集成，仅需添加数十行代码即可完成改造  
- 🔐 演示包含 JWT 验证、用户组映射等完整实现方案

---

### [雪松语言游乐场](https://www.cedarpolicy.com/en)

**原文标题**: [Cedar Language Playground](https://www.cedarpolicy.com/en)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

概述内容  

- 📌 要点 1  
- 🔍 要点 2  
- 📊 要点 3  

请提供具体文本，我会为您整理成清晰的结构化摘要。

---

### [GitHub - cedar-policy/expressjs 授权模块](https://github.com/cedar-policy/authorization-for-expressjs)

**原文标题**: [GitHub - cedar-policy/authorization-for-expressjs](https://github.com/cedar-policy/authorization-for-expressjs)

这是一个为 Express.js 应用提供基于 Cedar 策略的授权中间件的开源项目，支持细粒度访问控制并与认证系统无缝集成。

- 🔍 **项目概述**：Cedar Authorization for ExpressJS 是一个中间件包，用于在 Express.js 应用中实现基于 Cedar 策略的授权控制。
- 🛠️ **主要功能**：
  - 🔒 提供 Cedar 策略的授权中间件
  - 🎯 支持细粒度访问控制
  - 🔑 与 OIDC/JWT 认证无缝集成
  - ⚡ 优化的授权检查
  - 🚫 支持端点排除
- 📦 **安装方式**：通过 npm 安装`@cedar-policy/authorization-for-expressjs`。
- 🚀 **快速开始**：
  - 创建 Cedar 策略和架构
  - 设置授权中间件
  - 定义路由
- ⚙️ **配置选项**：
  - 支持自定义主体映射
  - 可配置的日志记录
  - 支持跳过特定端点的授权检查
- 📝 **示例**：项目提供了完整的示例实现。
- 🔧 **工具支持**：提供从 OpenAPI 规范生成架构和示例策略的工具。
- 🔐 **安全**：遵循 CONTRIBUTING 指南中的安全建议。
- 📜 **许可证**：项目采用 Apache-2.0 许可证。

---

### [Bluesky 上的@nodejs.org](https://bsky.app/profile/nodejs.org)

**原文标题**: [@nodejs.org on Bluesky](https://bsky.app/profile/nodejs.org)

这是一个高度交互的网络应用，需要 JavaScript 支持。虽然简单的 HTML 界面可行，但此应用并非如此。

- 🌐 这是一个高度交互的网络应用，需要 JavaScript 支持  
- 📜 简单的 HTML 界面无法满足此应用的需求  
- 🔍 了解更多关于 Bluesky 的信息，请访问 [bsky.social](bsky.social) 和 [atproto.com](atproto.com)  
- 👤 配置文件相关技术：Node.js  
- 🖥️ Node.js 官网：[nodejs.org](nodejs.org)  
- 🔗 DID 标识：did:plc:abbt45q3u3bttqfs7nepehhu

---

### [Node.js Bluesky 关注者调查讨论帖 · nodejs/bluesky · 讨论 #140 · GitHub](https://github.com/nodejs/bluesky/discussions/140)

**原文标题**: [Node.js Bluesky Follower Survey Discussion Thread · nodejs/bluesky · Discussion #140 · GitHub](https://github.com/nodejs/bluesky/discussions/140)

Node.js Bluesky 官方账号发起了一项调查和讨论，旨在优化内容管理并更好地满足关注者需求。

- 📊 **调查目的**：通过收集反馈优化 Node.js Bluesky 账号的内容管理，确保发布内容符合关注者期望。  
- 🗂 **调查内容**：包含 7 类固定内容的投票（如版本发布、技术文章等），每类单独线程讨论。  
- 💡 **新增建议**：考虑定期发布招聘线程（如月度），便于社区分享 Node.js 相关职位信息。  
- 🔧 **实现方式**：内容审核及自动化工具由该仓库维护，调查结果将指导志愿者管理发布内容。  
- 📢 **参与方式**：用户可在对应线程投票或提出新内容建议，支持点赞认同的想法。  
- ⚙️ **技术背景**：当前内容请求和审核均通过该仓库的自动化流程处理。  

（注：原文含部分页面加载错误提示及 GitHub 交互选项，已过滤非核心信息。）

---

### [JavaScript™ 商标更新 | Deno](https://deno.com/blog/deno-v-oracle4)

**原文标题**: [JavaScript™ Trademark Update | Deno](https://deno.com/blog/deno-v-oracle4)

JavaScript 商标争议更新：Ryan Dahl 对 TTAB 驳回针对 Oracle 的欺诈指控表示不满，案件将聚焦于“通用性”和“弃权”核心主张，预计 8 月进入快速审理阶段。

- 🚨 TTAB 驳回了针对 Oracle 的欺诈指控，Ryan Dahl 对此表示反对  
- 🤨 Oracle 在 2019 年商标续展中使用 Node.js 网站截图作为证据，被指误导 USPTO  
- 💡 案件核心将转向“通用性”和“弃权”主张，强调“JavaScript”是通用语言名称而非品牌  
- ⏳ 8 月 7 日前 Oracle 需回应撤销商标请愿，9 月 6 日进入证据开示阶段  
- 🌍 19,550 人联署 javascript.tm 支持“JavaScript 应属于公众”  
- ✨ 胜诉或 Oracle 主动放弃商标后，JavaScript 将不再受™限制，成为完全自由的名称

---

### [Node.js — 开源身份](https://nodejs.org/en/blog/community/2025-pride)

**原文标题**: [Node.js — Open sourced identity](https://nodejs.org/en/blog/community/2025-pride)

开源身份认同  

- 🌈 文章以 Pride Month 为背景，探讨身份认同与编程学习的相似性，强调标签的演变与自我认知的成长。  
- 💻 作者回顾编程历程，从初学时的固定模式（如 MERN、Rails）到后期打破框架、融合多元技术，类比身份标签（如 LGBTQ+）的拓展与更新。  
- 🔄 技术领域的变革（如 Docker、React 的兴起）与性别/性向认同的演进平行，均体现“唯一不变的是变化”这一真理。  
- 🏷️ 酷儿群体通过历史沉淀的标签（如 LGBT）描述自我，但新世代不断重构语言（如非二元、泛性恋），类似开源社区的协作创新。  
- 💡 自我发现可能瞬间觉醒（如梦境、他人反应），也可能长期压抑；社会环境可能支持探索，也可能强迫伪装，但“面具终会不适”。  
- 🌟 Pride Month 的意义在于让未确定自我或隐藏身份的人知道“被看见”和“不孤独”，Node.js 项目借此邀请 LGBTQ+ 技术者分享故事。  
- ✨ 文末引用 Laurie Voss 的推文，强调 Pride 的包容性——即使未准备好出柜，社群依然用色彩与音乐传递爱与等待。  
- 📢 作者 Carl Vitullo（Node.js Discord 志愿者）呼吁 LGBTQ+ 技术者提交开源贡献与身份历程的 PR，延续对话。

---

### [Node.js — Node.js LGBTQIA+ 故事：艾米莉亚·史密斯](https://nodejs.org/en/blog/community/2025-06-28-Emelia-Smith)

**原文标题**: [Node.js — Node.js LGBTQIA+ Stories: Emelia Smith](https://nodejs.org/en/blog/community/2025-06-28-Emelia-Smith)

概述总结  
Emelia Smith 分享了她在澳大利亚乡村长大的经历，如何通过在线社区和 Node.js 找到自我认同和职业方向，以及她作为 LGBTQIA+ 成员的出柜历程和对开源社区的贡献。  

- 🌏 在澳大利亚乡村长大，社会对 LGBTQIA+ 的接受度较低，Emelia 感到自己与周围环境格格不入。  
- 💻 通过 DeviantART 和在线聊天室接触到技术，开始学习编程和网络开发。  
- 🚀 2008 年因博客文章被招聘人员注意到，意识到编程可以成为职业。  
- 🛠️ 早期贡献 Node.js，包括添加`fs.readdirSync`方法和实现`'upgrade'`事件，支持 WebSocket 开发。  
- 📚 将 Node.js 文档拆分为多文件，成为项目前十贡献者，并因此获得旧金山的工作机会。  
- 🎙️ 与 Mikeal Rogers 合作推出早期 Node.js 播客 The Noded，采访项目核心成员。  
- 🏳️‍🌈 20 多岁时意识到自己是酷儿，2014 年底出柜为性别酷儿，后确认为跨性别女性和女同性恋者。  
- 🌈 在柏林生活，继续从事 Node.js 和创业工作，积极参与开源项目如 Mastodon 和 Adonis.js。  
- ❤️ Node.js 和 DeviantART 社区为她提供了安全感和归属感，帮助她找到自我和幸福。  
- 📢 现在在 Mastodon 上活跃（@[email protected]），并接受对其开源工作的经济支持。

---

### [基于去优化与内联的 WebAssembly 推测性优化 · V8 引擎](https://v8.dev/blog/wasm-speculative-optimizations)

**原文标题**: [Speculative Optimizations for WebAssembly using Deopts and Inlining · V8](https://v8.dev/blog/wasm-speculative-optimizations)

V8 引擎为 WebAssembly 实现的两项新优化：基于运行时反馈的间接调用内联和去优化支持，显著提升了执行效率（特别是 WasmGC 程序），在 Dart 微基准测试中平均加速超 50%，实际应用场景提升 1%-8%。

- 🚀 V8 引擎在 Chrome M137 中引入 WebAssembly 间接调用内联和去优化支持，通过运行时反馈生成更优机器码  
- 🔍 去优化机制：当假设不成立时回退到基线代码，保留中间状态并重构栈帧，避免慢路径拖累性能  
- 🧩 间接调用内联：利用单态/多态反馈记录，将高频目标函数内联至调用处，消除调用开销并启用后续优化  
- ⚡ 性能提升：Dart 微基准测试平均加速 1.59 倍，SQLite 提速 1%，Flutter 类 UI 基准最高提升 8%  
- 🌐 技术背景：WasmGC 支持 Java/Kotlin 等托管语言，其丰富的类型系统和子类型特性更需要推测优化  
- 📊 反馈向量：四级状态转换（未初始化→单态→多态→超多态），通过 Torque 内置函数动态更新调用目标统计  
- 🛠️ 实现细节：TurboFan 基于启发式决定内联策略，结合实例检查和目标校验确保安全内联  
- 🔮 未来方向：扩展跨语言内联（JS→Wasm）、边界检查消除等基于去优化的推测优化

---

### [如何使用 NestJS 作为 WebRTC 视频聊天的信令服务器](https://www.telerik.com/blogs/how-to-use-nestjs-signaling-server-webrtc-video-chat)

**原文标题**: [
	How to Use NestJS as Signaling Server for WebRTC Video Chat
](https://www.telerik.com/blogs/how-to-use-nestjs-signaling-server-webrtc-video-chat)

本文介绍了如何使用 NestJS 作为信令服务器来构建一个基于 WebRTC 的点对点视频聊天应用。

- 🚀 WebRTC 简介：WebRTC 是一个开源项目，支持浏览器之间直接通信，无需中介服务器，适用于视频、音频等实时数据传输。
- 🔗 信令服务器的作用：NestJS 作为信令服务器，帮助浏览器发现彼此并建立连接，但不传输视频数据。
- 📌 项目特点：直接浏览器连接、无插件或外部 API、仅用于初始连接建立。
- 🔄 连接流程：分为四个阶段：呼叫发起、呼叫接受、网络准备和直接连接。
- 🛠️ 项目设置：包括后端（NestJS）和前端（HTML/JavaScript）的配置，使用 HTTPS 和 WebSocket 确保安全通信。
- 📂 文件结构：详细说明了后端和前端所需的文件及其功能。
- 🔧 核心功能：包括处理 WebRTC 的 offer/answer 交换、ICE 候选者管理以及媒体流的处理。
- 🧪 测试步骤：指导如何在本地网络中测试视频聊天功能。
- ⚠️ 常见问题：如摄像头权限、HTTPS 要求和网络限制等问题的解决方法。
- 📚 结论：总结了如何利用 NestJS 和 WebRTC 构建高效、隐私保护的点对点视频聊天应用，并提出了进一步改进的建议。

---

### [如何撰写引人注目的软件发布公告 · 重构英语](https://refactoringenglish.com/chapters/release-announcements/)

**原文标题**: [How to Write Compelling Software Release Announcements · Refactoring English](https://refactoringenglish.com/chapters/release-announcements/)

概述  
本文介绍了如何撰写引人入胜的软件发布公告，强调从用户角度出发，突出改进而非技术细节，并提供实用建议和示例。

- 📢 发布公告应聚焦用户体验，而非简单罗列功能更新。  
- ✍️ 避免“变更日志”式写法，用用户语言描述功能价值（如“自动创建重复事件”而非“新增重复按钮”）。  
- 📝 区分发布公告（精选重要改进）与发布说明（详尽技术列表）。  
- ⚡ 强调改进效果（如“提速 100 倍”），而非修复的问题（如“修复 UI 卡顿”）。  
- 🌟 为新用户简短介绍产品功能，避免冗长背景。  
- 🖼️ 截图需突出关键改动，使用箭头/高亮引导注意力。  
- 🎬 动画演示控制在 15 秒内，优先用 WebP/AVIF 等高效格式。  
- 📊 用图表替代原始数据，直观展示性能提升等改进。  
- 🚫 删除模糊表述（如“多项改进和修复”），明确用户收益。  
- 📅 开发阶段提前规划公告内容，确保版本有用户可见价值。  
- 🔍 推荐学习 Gleam 和 Figma 的公告范例，注重用户视角与可视化表达。  

（注：文末书籍推广及修订记录未纳入摘要）

---

### [使用 Claude 代码构建 GitHub Actions 工作流程 - YouTube](https://www.youtube.com/watch?v=VC6dmPcin2E)

**原文标题**: [Using Claude Code to build a GitHub Actions workflow - YouTube](https://www.youtube.com/watch?v=VC6dmPcin2E)

关于 YouTube 平台的相关信息与链接  
- 📢 关于 - 平台的基本介绍  
- 🗞️ 媒体 - 新闻与公告  
- ©️ 版权 - 版权政策与保护  
- 📩 联系我们 - 用户沟通渠道  
- 🎨 创作者 - 内容创作者资源  
- 💼 广告 - 广告合作与投放  
- 💻 开发者 - 开发者工具与 API  
- 📜 条款 - 使用条款与协议  
- 🔒 隐私 - 隐私政策说明  
- ⚖️ 政策与安全 - 社区准则与安全措施  
- 🔧 YouTube 运作 - 平台功能解析  
- � 测试新功能 - 体验最新产品特性  
- ®️ 版权归属 - 谷歌公司版权所有（2025 年）

---

### [问 HN：为什么我的 Node.js 多人游戏在 500 玩家时 CPU 占用低却出现延迟？ | Hacker News](https://news.ycombinator.com/item?id=44389408)

**原文标题**: [Ask HN: Why does my Node.js multiplayer game lag at 500 players with low CPU? | Hacker News](https://news.ycombinator.com/item?id=44389408)

overview summary  
开发者使用 Node.js 和 Socket.IO 搭建的回合制多人浏览器游戏在单台 Hetzner 服务器（4 核/16GB 内存）上遇到性能瓶颈：500 名玩家同时在线时出现高事件循环延迟，但 CPU 利用率仅 25%。核心问题与实时打字广播功能相关，移除后性能可提升至 1000+ 玩家。最终发现容器数量过多导致 NIC/OS 层性能下降，减少容器数量后性能提升 6 倍至 3000+ 玩家。

- 🎮 游戏架构：Node.js + Socket.IO，Docker Swarm 部署，Traefik 负载均衡，基于内存的回合制房间分片设计  
- 🐢 性能瓶颈：500 玩家时事件循环延迟显著，但 CPU/带宽占用低（25%/6Mbps）  
- ⌨️ 关键因素：实时打字广播功能（200ms 间隔）是主要性能消耗点  
- 🐳 容器陷阱：意外发现 2 个 Node 容器性能反而不如 1 个，NIC/OS 层处理多进程流量时效率下降  
- 🔍 调试历程：排除 Redis、Socket.IO 广播锁、内核参数等可能性，最终通过减少容器数量解决  
- 🤖 测试方法：本地模拟 500+ 机器人连接进行压测，但未考虑单源连接的影响  
- 💡 经验总结：过早优化反成性能杀手，垂直扩展不一定优于水平扩展

---

### [发布 3.6.0 版 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.6.0)

**原文标题**: [Release 3.6.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.6.0)

Transformers.js 发布了 v3.6 版本，新增支持多种模型并进行了多项改进。

- 🚀 **新模型支持**  
  - Gemma 3n：本地运行的多模态模型，支持图像、文本、音频和视频输入。  
  - Qwen3-Embedding：专为文本嵌入和排序任务设计的模型系列。  
  - Llava-Qwen2：支持 Llava 模型与 Qwen2 文本骨干结合。  

- 🛠️ **其他改进**  
  - 优化了 Deno/Bun 的检测和使用。  
  - 新增了 eos/last_token 池化功能。  

- ⚠️ **注意事项**  
  - Gemma 3n 目前仅支持 Node.js、Deno 和 Bun，WebGPU 支持正在开发中。  

- 📦 **发布信息**  
  - 版本号：3.6.0  
  - 发布日期：2024 年 6 月 26 日

---

### [Gemma 3n 开发者指南发布 - Google Developers 博客](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/)

**原文标题**: [
            
            Introducing Gemma 3n: The developer guide
            
            
            - Google Developers Blog
            
        ](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/)

Google 发布了 Gemma 3n 模型，这是一款专为移动设备设计的先进多模态 AI 模型，具有高效性和强大的性能。

- 🚀 **Gemma 3n 发布**：Gemma 3n 是一款移动优先的多模态 AI 模型，支持文本、图像、音频和视频输入，并优化了边缘设备性能。  
- 📱 **高效设计**：提供两种尺寸（E2B 和 E4B），内存占用低至 2GB 和 3GB，性能媲美去年的云端前沿模型。  
- � **创新架构**：采用 MatFormer 嵌套 Transformer 架构，支持弹性推理，允许开发者根据需要选择模型大小或自定义中间版本。  
- 🎤 **音频理解**：集成 Universal Speech Model (USM) 编码器，支持语音识别和翻译，尤其擅长英语与西班牙语等语言的互译。  
- 👁 **视觉处理**：配备 MobileNet-V5 视觉编码器，支持多种分辨率，在移动设备上实现实时视频分析（60 FPS）。  
- � **社区合作**：与 Hugging Face、llama.cpp 等开源工具合作，提供广泛支持，并推出 Gemma 3n Impact Challenge，鼓励开发者利用其离线多模态能力创新。  
- 🛠 **快速上手**：可通过 Google AI Studio 体验，或从 Hugging Face、Kaggle 下载模型，支持多种部署工具（如 Ollama、MLX）。  
- 🌍 **多语言支持**：文本支持 140 种语言，多模态理解覆盖 35 种语言，显著提升数学、编程和推理能力。

---

### [GitHub - Meridius-Labs/apple-on-device-ai: 适用于 NodeJS 的 Apple 基础模型绑定（支持 Vercel AI SDK）](https://github.com/Meridius-Labs/apple-on-device-ai)

**原文标题**: [GitHub - Meridius-Labs/apple-on-device-ai: Apple foundation model bindings for NodeJS (supports Vercel AI SDK)](https://github.com/Meridius-Labs/apple-on-device-ai)

Meridius-Labs 提供的 Apple 设备端 AI 绑定库，支持 NodeJS 和 Vercel AI SDK，具备丰富的功能和跨平台兼容性。

- 🍎 **Apple 智能集成**：直接访问苹果设备端模型  
- 🧠 **双 API 支持**：支持原生 Apple AI 接口和 Vercel AI SDK  
- 🌊 **流式响应**：实时流式传输，兼容 OpenAI 格式  
- 🎯 **结构化生成**：支持 Zod 或 JSON Schema 生成结构化数据  
- 💬 **聊天接口**：提供类似 OpenAI 的聊天补全功能  
- 🔧 **工具调用**：支持通过 Zod 或 JSON Schema 调用函数/工具  
- 🔄 **跨平台兼容**：支持 React、Next.js、Vue、Svelte 和 Node.js（Apple Silicon）  
- 📝 **TypeScript 支持**：完整的类型安全和开发体验优化  

**安装与使用**  
- 🔧 推荐使用 Bun 安装：`bun add @meridius-labs/apple-on-device-ai`  
- 🚀 提供原生接口和 Vercel AI SDK 集成的快速示例  

**功能亮点**  
- ⚡ 支持流式文本生成、结构化对象生成和工具调用  
- 📊 提供丰富的错误处理和 API 参考  

**系统要求**  
- 💻 macOS 26+ 并启用 Apple Intelligence  
- 🖥️ Apple Silicon 芯片（M1/M2/M3/M4）  
- 🌍 设备语言设置为支持的语言（如英语、西班牙语等）  
- 💾 至少 4GB 存储空间用于模型文件  

**开源与贡献**  
- 🤝 欢迎贡献，遵循 MIT 许可证  
- 🔗 项目地址和更多资源见 npm 包和 GitHub 仓库

---

### [在真实 iOS 设备上运行 Playwright 测试 | BrowserStack 文档](https://www.browserstack.com/docs/automate/playwright/playwright-ios?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=new-launches-updates&utm_campaign=PR-12-Jun-2025-iOS-Playwright&utm_campaigncode=701OW00000NyIRcYAN&utm_term=nodeweekly)

**原文标题**: [Run Playwright tests on real iOS devices | BrowserStack Docs](https://www.browserstack.com/docs/automate/playwright/playwright-ios?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=new-launches-updates&utm_campaign=PR-12-Jun-2025-iOS-Playwright&utm_campaigncode=701OW00000NyIRcYAN&utm_term=nodeweekly)

BrowserStack 推出 Playwright 测试支持真实 iOS 设备的功能，帮助开发者更高效地进行移动端测试。

- 🚀 **Playwright 支持 iOS 设备**：现可在 BrowserStack 上运行 Playwright 测试，覆盖 100 多种 iPhone 和 iPad 设备与浏览器组合，解决 Safari 特有的问题。  
- 📱 **真实设备测试**：避免移动模拟器的局限性，直接在真实 iOS 设备上进行测试，确保准确性。  
- 🔧 **快速开始指南**：提供详细的步骤，包括克隆示例仓库、安装依赖、配置设备参数等，帮助用户快速上手。  
- ⚙️ **配置灵活**：支持动态调整测试配置，如设备名称、操作系统版本等，满足不同测试需求。  
- 📊 **结果查看**：测试结果可在 BrowserStack Automate 仪表板中查看，方便调试和分析。  
- ❌ **不支持的功能**：部分功能如`playwrightLogs`、`consoleLogs`等在 iOS 设备测试中暂不支持。  
- 📞 **技术支持**：提供支持团队联系方式，帮助用户解决测试过程中的问题。

---

### [Repomix | 将代码库打包为 AI 友好格式](https://repomix.com/)

**原文标题**: [Repomix | Pack your codebase into AI-friendly formats](https://repomix.com/)

AI 优化了代码库的格式，使其更易于 AI 理解和处理。

- 🤖 AI 优化：调整代码库格式，提升 AI 处理效率  
- 🧠 易理解：简化结构，便于 AI 快速解析  
- ⚡ 高效处理：优化后的代码加速 AI 运算与分析

---

### [发布 v1.0.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.0.0)

**原文标题**: [Release v1.0.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.0.0)

Repomix 发布了 v1.0 版本，核心功能稳定且无重大变更计划，感谢贡献者和用户的支持。

- 🎉 发布 v1.0 版本，核心功能稳定且无破坏性变更计划  
- 🚀 新增 `--stdin` 标志，支持从命令行处理文件列表，提升脚本集成灵活性  
- ⚡ 改进远程仓库处理（`--remote`），优先使用归档下载并优化 GitHub 仓库可靠性  
- 📊 新增条件性摘要显示功能，根据文件选择动态控制输出  
- 🔒 安全增强：停止在终端输出 secretlint 结果，防止敏感信息泄漏  
- 🐛 修复远程仓库处理中的文件复制效率问题  
- ⚠️ 停止支持 Node.js 18，需升级至 Node.js 20 或更高版本  
- 🔧 内部改进：GitHub Actions 安全加固、依赖项优化及性能提升  
- 📥 更新方式：通过 `npm update -g repomix` 或 `npx repomix@latest` 获取最新版本  
- ❤️ 特别致谢贡献者 @yoshi-taka、@eriknygren 等社区成员

---

### [GitHub - yamadashy/repomix: 📦 Repomix 是一款强大工具，能将整个代码库打包成单一且适合 AI 处理的文件。特别适合需要将代码库输入大型语言模型（LLM）或其他 AI 工具（如 Claude、ChatGPT、DeepSeek、Perplexity、Gemini、Gemma、Llama、Grok 等）的场景。](https://github.com/yamadashy/repomix)

**原文标题**: [GitHub - yamadashy/repomix: 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.](https://github.com/yamadashy/repomix)

Repomix 是一个强大的工具，能够将整个代码仓库打包成单一、AI 友好的文件，特别适合与大型语言模型（LLM）或其他 AI 工具（如 Claude、ChatGPT、DeepSeek 等）配合使用。

- 📦 **功能概述**：将代码仓库打包为 AI 友好的单一文件，支持多种输出格式（XML、Markdown、纯文本）。
- 🚀 **快速开始**：通过命令行工具、网站或浏览器扩展快速使用，支持本地和远程仓库处理。
- 🔧 **配置灵活**：可通过配置文件或命令行选项自定义包含/排除文件、输出格式等。
- 🔒 **安全特性**：内置安全检查，防止敏感信息泄露。
- 🛠️ **高级功能**：代码压缩、令牌计数、Git 集成等。
- 🌐 **社区支持**：提供 Discord 社区和网站支持，用户可分享使用经验和技巧。
- 📜 **开源许可**：采用 MIT 许可证，欢迎社区贡献。
- 🤖 **AI 集成**：优化输出以适配多种 AI 工具，提升代码分析和生成的效率。

---

### [标记文档](https://marked.js.org/)

**原文标题**: [Marked Documentation](https://marked.js.org/)

Marked 是一个高性能的 Markdown 解析器，支持多种 Markdown 规范，提供 CLI 和 JavaScript 使用方式，强调安全性和扩展性。

- 🚀 **高性能**：Marked 为速度而设计，解析 Markdown 时不缓存或长时间阻塞。
- 📚 **多功能支持**：支持多种 Markdown 规范，包括 CommonMark 和 GitHub Flavored Markdown。
- 💻 **多平台可用**：提供 CLI 工具，并可在浏览器和 Node.js 中使用。
- ⚠️ **安全警告**：Marked 不自动过滤输出的 HTML，需使用如 DOMPurify 等工具防止 XSS 攻击。
- 🔧 **扩展性强**：支持自定义渲染器、分词器和钩子，满足高级需求。
- 📊 **规范支持**：详细列出了对各种 Markdown 功能的支持百分比。
- 🛠️ **工具集成**：多个工具如 zero-md 和 Homebrewery 使用 Marked 进行 Markdown 转换。
- 🔒 **安全措施**：鼓励通过邮件报告安全问题，承诺快速响应和修复。
- 📖 **文档丰富**：提供详细的安装、使用和扩展文档，适合从入门到高级用户。

---

### [标记演示](https://marked.js.org/demo/)

**原文标题**: [Marked Demo](https://marked.js.org/demo/)

该内容介绍了 Markdown 的演示工具及其相关功能选项。

- 🚀 提供多种 Markdown 演示模式：Marked Demo、CommonMark Demo、Daring Fireball (pedantic) Demo  
- ⚙️ 包含实用功能选项：输入、永久链接、版本切换（master）、清除  
- 📄 支持预览 HTML 源码及 Lexer 数据  
- 🔍 提供 Markdown 快速参考指南  
- ⏱️ 显示响应时间  
- 💡 需启用 JavaScript 才能使用该工具

---

### [GitHub - markedjs/marked: 一款 Markdown 解析器和编译器。为速度而生。](https://github.com/markedjs/marked)

**原文标题**: [GitHub - markedjs/marked: A markdown parser and compiler. Built for speed.](https://github.com/markedjs/marked)

marked 是一个高效的 Markdown 解析器和编译器，专为速度而设计，支持多种 Markdown 风格和规范，适用于浏览器、服务器和命令行环境。

- ⚡ **高效性能**：低层编译器，解析 Markdown 时不缓存或长时间阻塞  
- ⚖️ **轻量全面**：体积小但支持所有主流 Markdown 功能和规范  
- 🌐 **多端兼容**：可在浏览器、服务器或 CLI 中运行  
- 🚨 **安全提示**：输出 HTML 需额外消毒（推荐使用 DOMPurify）  
- 📚 **丰富文档**：官网和示例均用 marked 渲染  
- 📦 **灵活安装**：支持 npm 全局/本地安装或 CDN 直接引入  
- 🔧 **多种用法**：提供 CLI、浏览器脚本和 ES 模块导入示例  
- 📜 **开源许可**：采用 MIT 许可证，贡献者超 190 人  
- 🌟 **社区活跃**：35k+ Stars，3.5k+ Forks，每月 150 万 + 项目使用

---

### [GitHub - Secreto31126/whatsapp-api-js：一个与服务器无关的TypeScript版WhatsApp官方API框架](https://github.com/Secreto31126/whatsapp-api-js)

**原文标题**: [GitHub - Secreto31126/whatsapp-api-js: A TypeScript server agnostic Whatsapp's Official API framework](https://github.com/Secreto31126/whatsapp-api-js)

一个基于 TypeScript 的、服务器无关的 WhatsApp 官方 API 框架，支持多种消息类型和事件处理。

- 🚀 **项目概述**：whatsapp-api-js 是一个 TypeScript 框架，用于与 WhatsApp 官方 API 交互，支持多种服务器环境。
- 📜 **许可证**：采用 MIT 许可证，开源免费使用。
- ⭐ **受欢迎程度**：获得 206 颗星和 39 次分叉，显示其受欢迎程度。
- 🔧 **设置要求**：需要 Meta Business App 和 WhatsApp API 激活，获取 API 令牌和应用密钥。
- 📦 **安装方式**：通过 npm 安装，命令为`npm install whatsapp-api-js`。
- 📝 **功能示例**：支持发送文本、图片、文档等多种消息类型，并处理接收消息和发送状态。
- 🌐 **Webhook 设置**：需配置 Webhook URL 并订阅消息事件，支持 GET 和 POST 请求处理。
- 📚 **文档与示例**：提供详细文档和示例代码，帮助开发者快速上手。
- 🔄 **更新与维护**：定期更新，提供变更日志和版本发布信息。
- 🤝 **贡献指南**：欢迎开发者贡献代码，提供贡献指南和安全策略。
- 🛠️ **多语言支持**：主要使用 TypeScript 和 JavaScript 开发，支持多种开发环境。

---

### [GitHub - motdotla/dotenv: 为 Node.js 项目从.env 文件加载环境变量](https://github.com/motdotla/dotenv)

**原文标题**: [GitHub - motdotla/dotenv: Loads environment variables from .env for nodejs projects.](https://github.com/motdotla/dotenv)

dotenv 是一个零依赖模块，用于从 `.env` 文件加载环境变量到 `process.env`，遵循十二要素应用方法论。

- 🌱 **安装** - 通过 npm、yarn、bun 或 pnpm 安装 dotenv。
- 🏗️ **使用** - 在项目根目录创建 `.env` 文件，并通过 `require('dotenv').config()` 加载。
- 📝 **多行值与注释** - 支持多行变量（如私钥）和行内注释。
- 🔧 **解析与配置** - 提供 `parse` 和 `config` 方法，支持自定义路径、编码、调试等选项。
- 🔄 **变量扩展** - 使用 `dotenv-expand` 支持变量扩展。
- 🌴 **多环境管理** - 通过 `dotenvx` 支持多环境（如 `.env.production`）。
- 🔒 **加密与部署** - 使用 `dotenvx` 加密 `.env` 文件，安全部署。
- ❓ **常见问题** - 解决 `.env` 文件未加载、多环境配置、变量解析规则等问题。
- 🛠️ **自定义与插件** - 支持通过返回对象自定义环境变量，或结合 `dotenv-expand` 扩展功能。
- ⚠️ **前端注意事项** - 在 React 等前端项目中需通过 Webpack 配置注入环境变量。
- 📜 **贡献与更新** - 提供贡献指南和更新日志，社区活跃，被众多项目依赖。

---

### [错误](https://nodeweekly.com/link/171135/web)

**原文标题**: [Error](https://nodeweekly.com/link/171135/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/171135/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [Electron 37.0.0 | Electron](https://www.electronjs.org/blog/electron-37-0)

**原文标题**: [Electron 37.0.0 | Electron](https://www.electronjs.org/blog/electron-37-0)

Electron 37.0.0 发布，包含 Chromium 138、V8 13.8 和 Node 22.16.0 的升级，新增平滑圆角 CSS 属性，支持 Google Summer of Code 项目，并引入多项新功能和改进。

- 🚀 **发布信息**：Electron 37.0.0 发布，升级至 Chromium 138、V8 13.8 和 Node 22.16.0。  
- 🎨 **平滑圆角**：新增 `-electron-corner-smoothing` CSS 属性，支持创建类似 macOS 的平滑圆角（squircle）。  
- 🔧 **堆栈更新**：Chromium 升级至 138.0.7204.35，V8 升级至 13.8，Node 升级至 22.16.0。  
- 🌟 **Google Summer of Code**：两位贡献者分别开发新的窗口状态 API 和现代化 Devtron 扩展工具。  
- ✨ **新功能**：  
  - 新增 `innerWidth` 和 `innerHeight` 选项支持 `window.open`。  
  - 添加 `before-mouse-event` 拦截鼠标事件。  
  - 支持 `HIDDevice.collections` 和 `screen.dipToScreenPoint` 等功能。  
- ⚠️ **重大变更**：  
  - Utility Process 未处理 rejection 行为变更，不再崩溃而是警告。  
  - `process.exit()` 在 Utility Process 中同步终止进程。  
  - WebUSB 和 WebSerial 支持 Chromium 的阻止列表。  
- 📅 **支持终止**：Electron 34.x.y 已停止支持，建议升级至新版本。  
- 🔮 **未来计划**：团队将继续跟进 Chromium、Node 和 V8 的主要组件更新。

---

### [GitHub - tclindner/npm-package-json-lint: 可配置的 package.json 文件检查工具](https://github.com/tclindner/npm-package-json-lint)

**原文标题**: [GitHub - tclindner/npm-package-json-lint: Configurable linter for package.json files](https://github.com/tclindner/npm-package-json-lint)

一个用于检查 package.json 文件的 Node.js 项目工具，支持命令行和程序化使用，可自定义配置规则。

- 🔍 **功能概述**：npm-package-json-lint 用于检查 package.json 文件的规范性和质量，支持多种规则检查，如数据类型、版本号、依赖项等。
- ⚙️ **安装与使用**：支持全局安装或在项目中安装，通过命令行或程序调用使用。
- 📜 **自定义配置**：通过修改 .npmpackagejsonlintrc 文件来配置规则，满足项目需求。
- 🛠️ **本地开发**：提供详细的本地开发设置步骤，方便贡献代码。
- 📚 **文档与迁移**：提供详细的文档和多个版本的迁移指南，帮助用户升级。
- 🤝 **社区与许可**：鼓励社区贡献，采用 MIT 许可证，有多个贡献者和丰富的发布历史。
- 🌐 **相关资源**：提供默认配置模块和项目网站链接，方便用户获取更多信息。

---

### [GitHub - openai/openai-node: OpenAI API 官方 JavaScript/TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

OpenAI 官方提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API，支持多种功能和高级用法。

- 🚀 **官方库**：OpenAI 提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API。
- 📦 **安装方式**：支持 npm 和 JSR 安装，适用于 Node.js、Deno 等环境。
- 💡 **主要功能**：包括生成文本、流式响应、文件上传、Webhook 验证等。
- 🔄 **流式响应**：支持 Server Sent Events (SSE) 实现流式响应。
- 📂 **文件上传**：支持多种文件上传方式，如`fs.ReadStream`、`fetch Response`等。
- 🔒 **Webhook 验证**：提供验证和解析 Webhook 请求的方法，确保安全性。
- ⚠️ **错误处理**：支持多种错误类型处理，如`APIError`及其子类。
- 🔄 **自动分页**：支持自动分页，方便处理大量数据。
- ⏱️ **超时和重试**：可配置请求超时和自动重试机制。
- 🌐 **Azure 支持**：提供`AzureOpenAI`类支持 Microsoft Azure OpenAI。
- 📊 **高级用法**：包括访问原始响应数据、自定义日志、自定义请求等。
- ❓ **常见问题**：涵盖语义版本、运行时要求等。
- 🤝 **贡献**：欢迎贡献，提供相关文档和指南。

---

### [OpenAI 平台](https://platform.openai.com/docs/guides/webhooks)

**原文标题**: [OpenAI Platform](https://platform.openai.com/docs/guides/webhooks)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结  

- 📌 要点一：关键信息 1  
- 🔍 要点二：关键信息 2  
- 💡 要点三：关键信息 3  

请提供具体文本，我会为您生成相应的总结。

---

### [GitHub - WiseLibs/better-sqlite3: Node.js 中最快且最简单的 SQLite3 库](https://github.com/WiseLibs/better-sqlite3)

**原文标题**: [GitHub - WiseLibs/better-sqlite3: The fastest and simplest library for SQLite3 in Node.js.](https://github.com/WiseLibs/better-sqlite3)

better-sqlite3 是 Node.js 中最快且最简单的 SQLite3 库，支持完整的事务处理、高性能和易用的同步 API。

- 🚀 **高性能**：比 node-sqlite3 更快，尤其在事务处理和查询中表现优异。
- 🔄 **同步 API**：提供简单易用的同步 API，支持高并发。
- 🛠️ **功能丰富**：支持用户自定义函数、聚合、虚拟表和扩展。
- 💾 **64 位整数支持**：无缝处理大整数。
- 🧵 **工作线程支持**：适用于大型或慢查询。
- 📜 **MIT 许可证**：开源且免费使用。
- ⚠️ **不适用场景**：高并发读写或超大型数据库（如 TB 级）建议使用 PostgreSQL。
- 📈 **性能对比**：在多数操作中比 node-sqlite3 快数倍。
- 📥 **安装简单**：通过 npm 安装，支持 Node.js v14.21.1 及以上版本。
- 💡 **推荐设置**：启用 WAL 模式以提高性能。
- 🔄 **升级注意**：升级时需查看版本变更和 SQLite 版本兼容性。
- 📚 **详细文档**：提供 API 文档、性能优化指南和贡献规则。

---

### [GitHub - XeroAPI/xero-node: 基于 XeroAPI/Xero-OpenAPI 生成的 OAuth 2.0 版 Xero Node SDK](https://github.com/XeroAPI/xero-node)

**原文标题**: [GitHub - XeroAPI/xero-node: Xero Node SDK for OAuth 2.0 generated from XeroAPI/Xero-OpenAPI](https://github.com/XeroAPI/xero-node)

Xero Node SDK 是一个基于 Xero OpenAPI 规范的 JavaScript SDK，用于访问 Xero 的 API，支持 OAuth 2.0 认证，适用于会计、资产、银行数据等多种业务场景。

- 🚀 **功能覆盖**：支持 Xero 的多组 API，包括会计、资产、银行数据、文件、项目及各国工资单等。
- 📚 **文档与示例**：提供详细的 API 文档和示例应用程序，帮助开发者快速上手。
- 🔐 **认证机制**：使用 OAuth 2.0 进行认证，支持访问令牌和刷新令牌的管理。
- ⚙️ **配置灵活**：支持自定义连接（Custom Connections）和客户端凭证授权（client_credentials grant）。
- 🛠️ **辅助方法**：提供多种辅助方法，如令牌刷新、租户更新等，简化开发流程。
- 🔧 **安全措施**：利用 openid-client 库进行 JWT 验证和 CSRF 防护。
- 🤝 **社区贡献**：鼓励开发者通过 PR 和问题讨论参与项目改进，遵循 MIT 许可证和贡献者公约。
- 📦 **安装简便**：通过 npm 即可安装，集成到现有项目中。

---

### [GitHub - PrismarineJS/mineflayer: 使用强大、稳定且高级的 JavaScript API 创建 Minecraft 机器人](https://github.com/PrismarineJS/mineflayer)

**原文标题**: [GitHub - PrismarineJS/mineflayer: Create Minecraft bots with a powerful, stable, and high level JavaScript API.](https://github.com/PrismarineJS/mineflayer)

PrismarineJS 的 Mineflayer 是一个用于创建 Minecraft 机器人的强大、稳定且高级的 JavaScript API，支持 Python 使用。

- 🚀 **功能强大**：支持 Minecraft 1.8 至 1.21 版本，提供实体追踪、方块查询、物理运动、攻击实体、物品管理等功能。
- 📚 **文档丰富**：包含教程、API 参考、常见问题解答和示例代码，适合初学者和高级用户。
- 🔌 **模块化设计**：依赖多个模块如 minecraft-protocol、prismarine-physics 等，提供高度可扩展性。
- 🛠️ **第三方插件**：支持多种插件如 pathfinder、prismarine-viewer 等，增强机器人功能。
- 🌍 **多语言支持**：提供多种语言的文档，包括中文、英文、俄文等。
- 📈 **活跃开发**：社区活跃，有详细的开发路线图和贡献指南。
- 📺 **可视化工具**：通过 prismarine-viewer 可以在浏览器中实时查看机器人行为。
- 🔄 **持续更新**：定期发布新版本，支持最新 Minecraft 版本和功能。

---

### [发布 v7.11.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.11.0)

**原文标题**: [Release v7.11.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.11.0)

Undici 项目发布了 v7.11.0 版本，包含多项功能更新、问题修复和依赖项升级，并有新贡献者加入。

- 🚀 **版本发布**: v7.11.0 于 2024 年 6 月 26 日发布，包含 9 次提交至主分支。  
- ✨ **新功能**:  
  - 新增 zstandard 解压缩支持 (#4238)  
  - 添加全局 WHATWG fetch 类的 install() 函数 (#4286)  
  - 新增请求体诊断通道 (#4289)  
- 🐛 **问题修复**:  
  - 修复 EventSource 在网络错误时不重连的问题 (#4247)  
  - 修复类型定义和拦截器缓存问题 (#4240, #4272)  
  - 优化调试日志和 Mock 工具 (#4236, #4176)  
- ⬆️ **依赖升级**:  
  - 多项 GitHub Actions 和开发依赖更新 (#4252-#4255等)  
- 📚 **文档改进**:  
  - 修正拦截器顺序描述 (#4251)  
  - 添加 Undici 与 Fetch 的对比文档 (#4245)  
- 👋 **新贡献者**: 8 位开发者首次提交代码 (#4236, #4272 等)  
- 🔄 **其他变更**:  
  - 移除 FinalizationRegistry 的 workaround (#4250)  
  - 更新内存缓存默认限制 (#4292)  
- ❤️ **社区互动**: 获得 4 个❤️反应

---

### [定价 | ConfigCat 功能开关](https://configcat.com/pricing/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202506)

**原文标题**: [Pricing | ConfigCat Feature Flags](https://configcat.com/pricing/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202506)

ConfigCat 是一个功能管理和远程配置服务，提供多种定价方案和功能，适用于不同规模的企业和开发团队。

- 🚀 **功能概述**：提供功能开关、远程配置、多环境支持、团队协作及安全合规功能。  
- 💰 **定价方案**：  
  - **免费版**：永久免费，支持 10 个功能开关、2 个环境。  
  - **专业版**（€110/月）：100 个功能开关、3 个环境。  
  - **智能版**（€325/月）：无限功能开关和环境。  
  - **企业版**（€900/月）：定制协议和高级支持。  
  - **专属版**（€4000/月）：私有云部署。  
- 🌍 **全球支持**：支持欧元（EUR）和美元（USD）计价，年付优惠。  
- 🔒 **安全与合规**：提供 2FA、SSO、SAML、GDPR 和 ISO 27001 合规。  
- 📊 **资源限制**：  
  - **配置 JSON 下载**：从 500 万/月（免费版）到 60 亿+/月（专属版）。  
  - **网络流量**：从 20GB/月（免费版）到 24TB/月（专属版）。  
- 👥 **团队协作**：无限团队成员、服务连接和月度活跃用户（MAUs）。  
- 🔧 **开发工具**：支持多种 SDK（JavaScript、.NET、Java 等）和集成（GitHub、Jira、Slack 等）。  
- 📜 **审计与透明度**：审计日志保留（7 天至 2 年），支持强制修改理由记录。  
- 🌱 **环保承诺**：每笔订阅捐赠树木，减少碳足迹。  
- 🎓 **教育优惠**：为学生和教师提供定制方案。  
- 📞 **支持服务**：免费版提供社区支持，企业版提供 SLA 保障和专属技术支持。  

（注：部分功能如软件托管需额外付费。）

---

### [不支持的浏览器](https://open.spotify.com/show/0cjrbI217FlGr0oopolcON)

**原文标题**: [Unsupported browser](https://open.spotify.com/show/0cjrbI217FlGr0oopolcON)

当前浏览器不支持 Spotify 播放，建议更新浏览器或下载应用以获得最佳体验。  

- 🚫 当前浏览器不支持使用 Spotify  
- 🔄 建议更新浏览器以获得最佳聆听体验  
- 📲 或下载 Spotify 应用  
- ℹ️ 提供“了解更多”选项获取详细信息

---

### [JavaScript 新动态 | Deno](https://deno.com/blog/updates-from-tc39)

**原文标题**: [What's coming to JavaScript | Deno](https://deno.com/blog/updates-from-tc39)

Deno 致力于推动 JavaScript 生态发展，参与 TC39 标准制定，近期有 9 项提案进入不同阶段，涵盖资源管理、异步迭代、错误检测等功能优化，旨在提升开发效率和代码安全性。

- 🚀 **Explicit Resource Management (Stage 4)**  
  新增`using`声明实现资源自动清理（如文件句柄、网络连接），确保异常时也能释放资源，支持 Chrome、Firefox 和 Deno。

- 🔄 **Array.fromAsync (Stage 4)**  
  异步迭代转数组，简化异步数据收集，兼容所有主流运行时（Deno v1.38+、Node v22+）。

- ❗ **Error.isError (Stage 4)**  
  内置方法可靠检测 Error 对象，适用于跨域或子类错误判断，浏览器和 Deno v2.2+ 已支持。

- 🔒 **Immutable ArrayBuffer (Stage 3)**  
  新增不可变二进制数据操作（`transferToImmutable`/`sliceToImmutable`），提升多线程数据共享安全性。

- 🎲 **Random.Seeded (Stage 2)**  
  可种子化的伪随机数生成器（`Random.Seeded`），支持游戏/仿真场景的确定性随机序列。

- 🔢 **Number.prototype.clamp (Stage 2)**  
  数值范围限制方法，替代`Math.min(max, Math.max(min, x))`的冗余写法。

- 💰 **Keep Trailing Zeros (Stage 1)**  
  `Intl.NumberFormat`新增尾零保留选项，优化货币等格式化场景。

- 🔍 **Comparisons (Stage 1)**  
  标准化值比较输出格式，统一测试框架和调试工具的差异显示。

- 🎯 **Random Functions (Stage 1)**  
  `Random`命名空间提供安全随机数生成、数组抽样/洗牌等方法，减少常见错误。

- 🌐 **后续计划**  
  TC39 将持续推进提案，Deno 将整合新特性（如异步上下文传播），9 月召开下一次会议。  
  *附：Deno Deploy 近期更新了实时日志、Next.js 模板等功能。*

---

### [GitHub - plv8/pljs: PLJS - PostgreSQL 的 JavaScript 语言插件](https://github.com/plv8/pljs)

**原文标题**: [GitHub - plv8/pljs: PLJS - Javascript Language Plugin for PostgreSQL](https://github.com/plv8/pljs)

PLJS 是一个轻量、快速的 PostgreSQL JavaScript 语言扩展插件，基于 QuickJS 引擎，支持 PostgreSQL 14+ 版本，提供类型转换、函数集成等功能，并拥有活跃的社区支持。

- 🚀 **项目简介** - PLJS 是 PostgreSQL 的 JavaScript 语言插件，轻量且高效。  
- 🔧 **技术栈** - 基于 QuickJS 引擎，兼容 PostgreSQL 14+。  
- 📌 **当前状态** - 最新版本为 1.0.1，支持基础功能如 `CREATE EXTENSION pljs`。  
- 📚 **文档资源** - 提供类型转换、函数集成、配置选项等详细文档。  
- 💬 **社区支持** - 拥有 Discord 社区供讨论和问题解答。  
- 📊 **项目数据** - 185 星标，5 个分支，3 位主要贡献者。  
- 📜 **许可证** - 开源项目，具体许可证需查看 LICENSE 文件。  
- 🔍 **开发信息** - 代码以 C 语言为主（84.1%），含开发指南和版本规划。

---

### [JSConf 2025 演讲嘉宾公布 | OpenJS 基金会](https://openjsf.org/blog/jsconf-25-speakers-announced)

**原文标题**: [JSConf 2025 Speakers Announced | OpenJS Foundation](https://openjsf.org/blog/jsconf-25-speakers-announced)

OpenJS 基金会宣布了 JSConf 2025 的演讲者阵容，会议将于 10 月 14 日至 16 日在马里兰州切萨皮克湾举行，涵盖前端性能、AI、编译器等多个主题。

- 🎤 **主题演讲嘉宾**：包括 VoidZero 创始人 Evan You、Bun 创始人 Jarred Sumner 等业界领袖。
- 🔍 **专题演讲**：涵盖性能优化、JavaScript 框架、安全隐私、AI 新兴技术等热门话题。
- 🛠 **性能与优化**：探讨 WASM、Rust 及大规模客户端性能优化。
- 🖥 **JavaScript 框架**：讨论 Node.js 依赖管理、RPC 复兴及编译器优化。
- 🔒 **安全与隐私**：分享前端安全架构及统一配置文件管理。
- 🤖 **AI 与新兴技术**：展示 WebGPU、个人 AI 代理及 LLM 优先的 Web 框架。
- 🌍 **开源与社区**：探讨技术决策、旧代码维护及开源协作。
- ♿ **UI/UX与无障碍**：研究 Web 动画、微前端及 Copilot 构建无障碍 UI。
- 🛠 **开发者工具与实践**：分享模块定制钩子、JS 替代方案及开放 Web 挑战。
- 📅 **注册提醒**：鼓励参与者尽快注册以预留席位。

---

### [容器现已公开测试，提供简单、全球可编程的计算服务](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/)

**原文标题**: [Containers are available in public beta for simple, global, and programmable compute](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/)

Cloudflare Containers 现已面向付费用户开放公测，支持与 Workers 无缝集成，提供全球化、可编程的容器化计算能力。

- 🚀 **公测发布**：Cloudflare Containers 进入公测阶段，付费用户可立即使用。  
- 🌍 **全球化部署**：一键部署至全球边缘节点（Region:Earth），无需多区域配置。  
- 🔧 **开发便捷性**：通过 `wrangler deploy` 快速部署容器，流程与 Workers 一致。  
- ⚖️ **灵活路由**：支持 Workers（轻量级）与 Containers（高性能）混合使用，按需选择。  
- 💻 **代码沙箱示例**：演示如何通过容器隔离运行用户/AI 生成代码，实现秒级启动和全局分发。  
- 🛠️ **配置简化**：通过 `Container` 类定义端口、超时等参数，Worker 自动路由请求至容器实例。  
- 🔄 **开发体验**：`wrangler dev` 支持本地镜像实时重建，按“R”键快速重启。  
- 📊 **内置监控**：控制台提供资源使用指标和 7 天日志，支持外接日志服务。  
- 💰 **透明计费**：按实际使用时长（10ms 精度）收费，包含免费额度，流量分级计价。  
- 🔮 **未来规划**：包括更大实例规格、全局自动扩缩容、容器-Workers 深度通信等增强功能。  
- 🎯 **应用场景**：涵盖媒体处理、定时任务、前后端混合部署等，集成 R2、KV 等开发者工具。  
- 📚 **快速开始**：提供模板和文档，支持 CLI 或一键部署体验。

---

### [RSS 服务器端阅读器](https://matklad.github.io/2025/06/26/rssssr.html)

**原文标题**: [RSS Server Side Reader](https://matklad.github.io/2025/06/26/rssssr.html)

作者对 RSS 的理解及个人 RSS 阅读器的实现方法。

- 📌 RSS 的核心功能是通知机制，让读者知道博客有新文章发布。
- 🔄 RSS 是 Twitter 和 HackerNews 的替代品，让用户自主选择关注的内容来源。
- ⚠️ 原始的 RSS 标准复杂且不清晰，推荐使用 Atom 或 JSON Feed。
- ❓ 作者对现有 RSS 阅读器不满，因为它们功能过多，而作者只需要简单的通知功能。
- 🚫 作者最初尝试客户端阅读器，但因 CORS 限制而失败。
- ✅ 最终解决方案是服务器端渲染 (SSR)，将 RSS 阅读器集成到个人博客的构建过程中。
- 📝 使用简单的 blogroll.txt 文件作为数据源，公开显示最新三篇文章。
- ⏰ 通过 GitHub Actions 每天自动更新博客列表。
- 🔗 作者还维护了一个常用链接列表，方便分享和访问。

---

### [时间性](https://tc39.es/proposal-temporal/)

**原文标题**: [Temporal](https://tc39.es/proposal-temporal/)

总结失败：Error code: 400 - {'error': {'message': "This model's maximum context length is 65536 tokens. However, you requested 180237 tokens (172237 in the messages, 8000 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

