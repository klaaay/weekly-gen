### [Node 周刊第 579 期：2025 年 5 月 27 日](https://nodeweekly.com/issues/579)

**原文标题**: [Node Weekly Issue 579: May 27, 2025](https://nodeweekly.com/issues/579)

概述：本期 Node.js 周报涵盖了 Google I/O 回顾、Node.js 协作峰会动态、TypeScript 原生预览版发布、Node.js 技术委员会否决功能悬赏计划等关键内容，同时包含工具更新、性能优化指南及 JavaScript 生态的其他新闻。

- 🎤 编辑 Peter Cooper 从 Google I/O 归来，虽无 Node 相关重磅消息，但整理了两周新闻动态。  
- 🤝 Node.js 协作峰会讨论了 CI 安全事件、Async Context、应用编译为可执行文件等议题。  
- 🚫 Node.js 技术委员会暂不批准功能悬赏计划，认为当前不适合建立正式奖励机制。  
- ⚡ 微软发布 TypeScript 原生预览版，性能提升 10 倍，支持 Go 编译和并发优化。  
- 🛠️ Glitch 平台将关闭应用托管功能，Astro 5.8 和 Angular 20 放弃 Node 18 以下版本支持。  
- 📢 Node v24.1 和 v22.16.0（LTS）发布，后者新增 node.config.json 支持。  
- 📊 开发者指南：Slack 等应用优化 Electron 性能的六种方法，以及 API 密钥迁移至 OAuth 2.1 的要点。  
- 📚 技术文章涵盖 Node.js 控制台文本样式、内存管理及数组 at() 方法解析。  
- 🔧 工具更新包括 Google Gen AI SDK、JavaScript 转 EXE 编译器 Astra、Express+TypeScript 生成器等。  
- 🌐 JavaScript 生态动态：Deno 澄清运营谣言，ESLint 9.0 过渡回顾，npm 恶意包警告及多语言压力测试结果。

---

### [Node.js — 行程报告：Node.js 合作峰会（2025 巴黎）](https://nodejs.org/en/blog/events/collab-summit-2025-paris)

**原文标题**: [Node.js — Trip report: Node.js collaboration summit (2025 Paris)](https://nodejs.org/en/blog/events/collab-summit-2025-paris)

2025 年巴黎 Node.js 协作峰会汇集了近 40 名现场参与者和十几名远程参与者，讨论了 CI 可靠性、WASM 模块、内存安全改进、贡献者体验优化、AsyncLocalStorage 的 Web 标准化、单可执行应用（SEA）进展、Undici 嵌入、Chrome DevTools 集成等议题，并探讨了模块定制与性能优化的未来方向。

- 🔒 **CI 可靠性与安全**：针对近期 CI 安全事件，讨论了基础设施管理和 flake 检测的改进措施。  
- 🚀 **WASM 模块实验**：介绍了实验性 WASM 模块的进展及与浏览器协调的解封计划。  
- 🧠 **内存安全改进**：展示了 V8 Oilpan 库的集成，以提升垃圾回收效率和内存安全性。  
- 👥 **导师计划**：回顾了现有导师项目，探讨如何优化知识共享和新人引导。  
- 😓 **贡献者体验**：通过回顾板收集反馈，重点关注 CI 不稳定和决策流程冗长的问题，提出 AI 摘要和表情投票等改进方案。  
- 🌐 **AsyncLocalStorage 标准化**：探讨如何将 Node.js 的异步上下文特性引入 Web（TC39 提案 Stage 2），并解决跨平台安全性和 API 设计挑战。  
- 📦 **单可执行应用（SEA）**：讨论了 ESM 支持、工具链简化等需求，但缺乏志愿者和资金仍是主要障碍。  
- 🔗 **Undici 嵌入**：计划通过稳定调度器 API 和文档改进提升 HTTP 客户端定制体验，并探索 QUIC 支持。  
- 🛠️ **Chrome DevTools 集成**：推进网络流量检查和 Worker 线程调试功能，增强开发者工具支持。  
- 📊 **Next-10 调查**：现场修订 2025 年生态调查问题，聚焦未来技术优先级。  
- 📦 **模块定制与性能**：同步化模块加载路径以提升性能，并探索 AST 重写技术实现 ESM 插桩。

---

### [Node.js — Node.js 测试 CI 安全事件](https://nodejs.org/en/blog/vulnerability/march-2025-ci-incident)

**原文标题**: [Node.js — Node.js Test CI Security Incident](https://nodejs.org/en/blog/vulnerability/march-2025-ci-incident)

Node.js 测试 CI 安全事件概述：2025 年 3 月 21 日，Node.js 项目通过 HackerOne 收到安全报告，发现测试 CI 主机被攻破。攻击者通过提交拉取请求并利用时间差漏洞在 Jenkins 代理上执行代码。项目团队迅速采取行动，修复漏洞并加强安全措施，确保未来操作的安全性。

- 🚨 **安全事件报告**：2025 年 3 月 21 日，Node.js 通过 HackerOne 收到测试 CI 主机被攻破的报告。
- 🔍 **攻击方式**：攻击者提交拉取请求，利用时间差漏洞在 Jenkins 代理上执行代码。
- 🛠️ **修复措施**：限制 Jenkins CI 访问，重建 24 台受感染主机，验证提交 SHA，更新标签逻辑。
- 📅 **时间线**：3 月 21 日报告，24 日确认并限制访问，28 日修复并重新启用部分功能。
- ⚖️ **安全与开发体验**：项目团队在安全与开发便利性之间寻求平衡，依赖志愿者进行安全加固。
- 📢 **用户影响**：事件不影响 Node.js 运行时，用户无需采取行动。
- 📧 **联系方式**：安全政策与漏洞报告流程详见 Node.js 官网和 GitHub。

---

### [GitHub - tc39/proposal-async-context: JavaScript 的异步上下文提案](https://github.com/tc39/proposal-async-context)

**原文标题**: [GitHub - tc39/proposal-async-context: Async Context for JavaScript](https://github.com/tc39/proposal-async-context)

Async Context for JavaScript 提案旨在解决异步代码中隐式调用栈信息丢失的问题，提供一种机制来跨事件循环传播上下文信息。

- 🚀 **提案状态**: 目前处于 Stage 2，由 @andreubotella、@legendecas 和 @jridgewell 担任 Champion。
- 🔗 **讨论渠道**: 通过 #tc39-async-context Matrix 房间进行讨论。
- 🎯 **动机**: 解决异步代码中因调用栈替换导致的隐式信息丢失问题，尤其是在 async/await 语法中。
- 📦 **核心 API**: 提供 `AsyncContext.Variable` 和 `AsyncContext.Snapshot` 来传播和捕获上下文。
  - `Variable`: 用于存储和传播上下文值，通过 `run` 和 `get` 方法管理。
  - `Snapshot`: 高级 API，用于捕获当前所有 `Variable` 的值并在后续执行中恢复。
- 🌐 **用例示例**:
  - **应用监控**: 如 OpenTelemetry 使用 `Variable` 跟踪跨异步操作的调用链。
  - **任务调度**: 通过 `Variable` 传递任务优先级，确保子任务继承相同优先级。
  - **用户队列**: 使用 `Snapshot` 实现与 `Variable` 解耦的用户队列。
- ❓ **FAQ**:
  - **为何 `run` 需要函数参数？**: 确保异步上下文的值在执行流中保持一致。
  - **与内置调度器的交互**: 内置调度器默认使用注册时的快照执行回调。
- 📚 **资源**: 包含详细文档（如 `SCOPING.md`、`USE-CASES.md`）和示例代码。
- 🔒 **许可**: 采用 CC0-1.0 许可证。

---

### [单可执行文件应用 | Node.js v24.1.0 文档](https://nodejs.org/api/single-executable-applications.html)

**原文标题**: [Single executable applications | Node.js v24.1.0 Documentation](https://nodejs.org/api/single-executable-applications.html)

Node.js 单可执行应用程序（SEA）功能允许将脚本和资源打包进二进制文件，实现在无 Node.js 环境的系统中运行应用。

- 📦 **功能概述**：将 Node.js 脚本注入二进制文件，无需安装 Node.js 即可运行（仅支持 CommonJS 模块）。
- 🔧 **创建步骤**：
  - 1️⃣ 编写脚本和配置文件。
  - 2️⃣ 生成注入用的 Blob 文件（`node --experimental-sea-config`）。
  - 3️⃣ 复制 Node 二进制并注入 Blob（使用工具如`postject`）。
  - 4️⃣ 移除/重新签名（macOS/Windows 需处理签名）。
- 🖼️ **资源嵌入**：通过配置`assets`字段打包图片/文本等资源，运行时通过`sea.getAsset()`获取。
- ⚡ **性能优化**：
  - **快照支持**（`useSnapshot`）：预初始化堆状态，加速启动。
  - **代码缓存**（`useCodeCache`）：预编译脚本减少运行时编译开销。
- 📂 **路径变量**：注入脚本中的`__filename`、`__dirname`指向二进制路径。
- ⚠️ **限制**：
  - 注入脚本的`require()`仅支持内置模块，文件模块需通过`createRequire`实现。
  - 跨平台生成时需禁用快照和代码缓存（平台兼容性问题）。
- 🖥️ **平台支持**：官方测试覆盖 Windows、macOS 和主流 Linux 发行版（除 Alpine 和 s390x 架构）。

---

### [Node.js 技术指导委员会拒绝支持功能悬赏计划 - Soc...](https://socket.dev/blog/node-js-tsc-declines-to-endorse-feature-bounty-program)

**原文标题**: [Node.js TSC Declines to Endorse Feature Bounty Program - Soc...](https://socket.dev/blog/node-js-tsc-declines-to-endorse-feature-bounty-program)

美国国家标准与技术研究院（NIST）因国家漏洞数据库（NVD）处理积压和延迟问题正接受联邦审计，漏洞数据处理瓶颈日益严重。  

- 🔍 NIST 因 NVD 处理积压和延迟问题被联邦政府正式调查  
- ⏳ 漏洞数据处理瓶颈问题持续加剧  
- 📅 事件报道时间：2025 年 5 月 27 日  
- ✍️ 作者：Sarah Gooding

---

### [宣布 TypeScript 原生预览版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)

**原文标题**: [Announcing TypeScript Native Previews - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)

TypeScript 团队宣布推出 TypeScript Native Previews，这是将 TypeScript 编译器及工具集移植到原生代码的成果，性能提升高达 10 倍。  

- 🚀 **性能提升**：通过使用 Go 语言和共享内存并行性，TypeScript Native Previews 在大多数项目中实现了 10 倍的速度提升。  
- 📦 **安装方式**：用户可通过 npm 安装预览版编译器，命令为 `npm install -D @typescript/native-preview`，并使用 `tsgo` 替代 `tsc` 进行编译。  
- 🔧 **编辑器支持**：VS Code 用户可安装“TypeScript (Native Preview)”扩展，需手动启用实验性功能。  
- ⚠️ **功能限制**：目前缺少部分功能，如 `--build` 模式、声明文件生成、自动导入等，但团队正在积极开发中。  
- 🔍 **类型检查改进**：已支持 JSX 和 JavaScript + JSDoc 的类型检查，大幅提升大型项目的编译速度。  
- 📅 **未来计划**：团队计划在今年晚些时候完善编译器功能，并持续发布夜间构建版本供用户测试。  
- 📢 **反馈渠道**：鼓励开发者试用并提供反馈，以便团队进一步优化。

---

### [10 倍速的 TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

**原文标题**: [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScript 团队宣布将推出原生版本的 TypeScript 编译器，预计性能提升 10 倍，大幅减少构建时间和内存使用，并优化编辑器体验。

- 🚀 TypeScript 将推出原生版本，性能提升 10 倍，大幅减少构建时间和内存使用。
- ⏱️ 原生版本预计在 2025 年中发布预览版，支持命令行类型检查，年底前完成功能完整的语言服务。
- 📉 测试显示，原生版本在多个流行代码库中性能显著提升，如 VS Code 构建时间从 77.8 秒降至 7.5 秒。
- 💻 编辑器加载时间提升 8 倍，内存使用减少约一半，语言服务操作响应速度大幅提高。
- 🔄 未来将迁移至语言服务器协议（LSP），更好地与其他语言工具集成。
- 📅 TypeScript 6.x 系列将继续开发，原生版本将作为 TypeScript 7.0 发布，两者将并行维护一段时间。
- ❓ 团队在 GitHub 上提供了常见问题解答，并计划在社区 Discord 举行问答活动。
- 🌟 这一改进将为开发者带来更快的开发体验，并支持更先进的 AI 工具和功能。

---

### [重要变更即将登陆 Glitch](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

**原文标题**: [Important changes are coming to Glitch](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

Glitch 社区即将停止应用托管服务，但保留代码下载和子域名重定向功能，以帮助用户平稳过渡。团队将专注于为开发者社区提供更有价值的服务，并协助用户迁移至其他现代平台。

- 📅 **重要日期**：2025 年 7 月 8 日停止项目托管和用户资料服务，仪表盘功能保留至 2025 年底。  
- 💾 **数据迁移**：提供项目代码下载和子域名重定向功能（需在 2025 年 12 月 31 日前设置）。  
- 🔍 **原因**：运营成本上升、平台老化及滥用问题，同时现代开发平台（如 Fly.io、Deno 等）已提供更优解决方案。  
- 🛠 **支持措施**：发布迁移指南、社区论坛答疑，并停止 Glitch Pro 新订阅（现有用户退款将处理）。  
- ❤️ **社区反馈**：鼓励用户通过论坛或邮件（[email protected]）分享意见，团队将持续更新进展。  
- 🌟 **未来方向**：探索 Glitch 社区的新角色，例如整合外部应用展示功能。

---

### [故障的终结（尽管他们说并非如此）](https://keith.is/blog/the-end-of-glitch-even-though-they-say-it-isnt/)

**原文标题**: [The End of Glitch (Even Though They Say It Isn't)](https://keith.is/blog/the-end-of-glitch-even-though-they-say-it-isnt/)

Glitch 将于 2025 年 7 月 8 日关闭项目托管和用户资料功能，这实质上意味着该平台的终结。尽管官方避免称之为“关闭”，但移除核心功能后，Glitch 仅剩重定向服务和部分链接。

- 🚨 **核心功能关闭**：Glitch 将停止项目托管和用户资料，标志着平台的终结。  
- 🌟 **Glitch 的独特之处**：以快速部署、协作编码和创意社区著称，帮助用户轻松从想法到上线应用。  
- 🎨 **创意与社区**：拥有活跃的创作者和开发者社区，支持“混音”文化，鼓励学习和分享。  
- 🌐 **Glitch in Bio**：简化个人网站创建，推动网络民主化，让用户拥有自己的互联网空间。  
- 🔧 **技术挑战**：早期架构问题导致技术债务累积，维护日益困难。  
- 🏢 **Fastly 收购**：本希望解决基础设施问题，但文化与优先级差异导致整合困难。  
- ✊ **首个科技工会**：Glitch Workers Union 成为科技行业工会化的先驱，虽解散但影响深远。  
- 📌 **迁移建议**：推荐 Val Town、Netlify、GitHub Pages 和 Fly.io 作为替代平台。  
- 💔 **失去的价值观**：Glitch 代表了互联网早期的实验精神，强调创造而非消费，但难以在当今互联网经济中持续。  
- 🛠 **帮助与资源**：社区论坛和代码导出工具仍可用，帮助用户平滑过渡。

---

### [Astro 5.8 | Astro](https://astro.build/blog/astro-580/)

**原文标题**: [Astro 5.8 | Astro](https://astro.build/blog/astro-580/)

Astro 5.8 是一个重要的更新，主要涉及 Node.js 版本要求的变更，并提供了升级指南和社区贡献者名单。

- 🔄 **Node.js 版本更新**：最低要求提升至 18.20.8，并建议升级至 Node.js 22 以获取长期支持。  
- ⚠️ **终止支持**：Node.js 18 已停止维护，未来版本将完全放弃对其的支持。  
- 🛠️ **升级指南**：推荐使用 `@astrojs/upgrade` 工具或手动运行包管理器的升级命令。  
- 🌐 **部署调整**：需在本地和 CI/CD 环境中更新 Node.js 版本，支持通过 `.nvmrc` 或环境变量配置。  
- ☁️ **Cloudflare Pages 用户**：需手动覆盖默认的 Node.js 18.17.1 至 22 版本。  
- 🐞 **问题修复**：包含自 5.7 版本以来的多项错误修复，详情参见更新日志。  
- 👏 **社区贡献**：感谢核心团队及众多社区成员的代码与文档贡献。  
- 💬 **交流渠道**：欢迎通过 Astro Discord 进行反馈或交流。

---

### [Node.js 未来十年调查 - 2025](https://linuxfoundation.research.net/r/2025nodenext10)

**原文标题**: [Node.js Next 10 Survey - 2025](https://linuxfoundation.research.net/r/2025nodenext10)

Node.js Next 10 调查问卷（2025 年）概述  
- 🌍 **居住地**：问卷包含全球所有国家/地区的选项，要求参与者选择当前居住地。  
- 🗣️ **主要语言**：提供多种常见语言选项，包括英语、中文、西班牙语等，并支持填写其他语言。  
- ⏳ **Node.js 使用时长**：以滑动条形式询问使用经验，范围从 0 到 10 年以上。  
- 🏢 **组织类型**：涵盖学术、企业、政府、自由职业、非营利等类别，支持填写其他类型。  
- 🏭 **公司行业**（若适用）：列出农业技术、金融、IT 等多个领域，支持填写其他行业。  
- 👥 **组织规模**：通过滑动条选择员工/成员数量，范围从 0 到 1000+。  
- 📄 **问卷进度**：当前为第 1 页（共 4 页），完成度 25%。

---

### [Node.js — Node v24.1.0（当前版本）](https://nodejs.org/en/blog/release/v24.1.0)

**原文标题**: [Node.js — Node v24.1.0 (Current)](https://nodejs.org/en/blog/release/v24.1.0)

Node v24.1.0 (Current) 版本发布，包含多项功能更新、错误修复和文档改进。

- 🚀 **重要变更**：新增对 `Dir` 显式资源管理的支持（SEMVER-MINOR）。
- 📜 **文档更新**：新增 JonasBa 和 puskin 为协作者，更新多个文档内容。
- 🔧 **依赖更新**：V8 更新至 13.6.233.10，llhttp 更新至 9.3.0。
- 🛠️ **修复与改进**：修复多个模块的问题，包括 `fs`、`http2`、`crypto` 等。
- 🧪 **测试优化**：减少测试迭代次数，修复测试中的问题。
- 📦 **构建改进**：修复构建过程中的多个问题，包括 32 位架构支持。
- 🔄 **功能新增**：`fs.glob` 支持 `URL` 作为 `cwd` 选项，新增诊断通道。
- 🖥️ **平台支持**：提供 Windows、macOS、Linux 等多个平台的安装包和二进制文件。
- 📄 **源码与文档**：提供源码下载和详细文档链接。

---

### [Node.js — Node v22.16.0（长期支持版）](https://nodejs.org/en/blog/release/v22.16.0)

**原文标题**: [Node.js — Node v22.16.0 (LTS)](https://nodejs.org/en/blog/release/v22.16.0)

Node.js v22.16.0 (LTS) 版本发布，包含多项功能更新、性能优化和错误修复。

- 🚀 **重要更新**：时区数据更新至 2025b 版本，确保日期和时间处理的准确性。
- 📚 **文档改进**：新增 Dario Piotrowicz 为协作者，并修复多处文档错误和格式问题。
- ⚡ **ESM 增强**：支持`import.meta`属性的正式毕业，提升模块系统的稳定性。
- 🛠 **SQLite 功能扩展**：新增`StatementSync.prototype.columns()`方法，增强数据库操作能力。
- 🔧 **配置支持**：引入`node.config.json`作为默认配置文件，简化应用配置管理。
- 🧩 **新 API**：新增`worker.getHeapStatistics()`方法，提供工作线程堆内存统计信息。
- 🐞 **错误修复**：修复跨领域`SharedArrayBuffer`验证和`ArrayBuffer`检查问题，提升安全性。
- ⚙️ **性能优化**：改进断言和工具模块的深层对象比较性能，提升执行效率。
- 📦 **依赖更新**：升级 zstd 至 1.5.7，zlib 至 1.3.0.1，确保依赖库的最新功能和安全性。
- 🔄 **流处理改进**：在`finished()`中保留 AsyncLocalStorage 上下文，确保异步操作的连续性。
- 📊 **测试增强**：新增多个测试用例，覆盖 SQLite、REPL 和 HTTP/2 等模块，提升代码质量。

---

### [成为 V8 提交者 | Seokho 的博客](https://blog.seokho.dev/development/2025/05/10/Became-V8-Committer.html)

**原文标题**: [Became a V8 committer | Seokho’s blog](https://blog.seokho.dev/development/2025/05/10/Became-V8-Committer.html)

Seokho Song 在 2025 年 5 月 10 日宣布成为 V8 项目的提交者（committer），并回顾了过去两年的贡献历程。

- 🎉 今早正式获得 V8 提交者身份  
- ⏳ 过去两年利用业余时间持续贡献 V8 项目  
- 🛠️ 主导实现 Float16Array 新特性  
  - 撰写开发日志《Float16Array Turbofan Pipeline DevLog》  
  - 与 V8 负责人每周同步进展  
- ⚡ 优化多项操作（包括 JIT 编译器）  
  - 发表《Optimize V8 Math.hypot - Hidden cost of the loop》  
- 🐞 修复长期存在的 bug（含 7 年历史规范偏差）  
- 🌍 全球仅 75 名提交者（含本人）  
- ✨ 项目经历带来技术成长与珍贵人脉  
- 🚀 希望贡献能使世界更高效安全  
- 🔥 承诺持续投入开发  
- 📜 贡献清单可通过链接查看  

（注：原文末段关于 Disqus 评论及前文链接等非核心内容未纳入摘要）

---

### [6 种方式：Slack、Notion 和 VSCode 如何提升 Electron 应用性能 | Palette 文档](https://palette.dev/blog/improving-performance-of-electron-apps)

**原文标题**: [6 Ways Slack, Notion, and VSCode Improved Electron App Performance | Palette Docs](https://palette.dev/blog/improving-performance-of-electron-apps)

Electron 应用性能优化的六个关键策略，通过 Slack、Notion 和 VSCode 等案例展示了如何解决启动慢和交互卡顿问题。

- 🚀 **使用打包工具替代 require()**  
  避免同步阻塞的`require()`，采用 Webpack/Vite 等打包工具，显著提升启动速度（如 Atom 案例中减少模块加载时间）。

- ⏳ **延迟非关键代码加载**  
  通过路由级代码拆分（如 React 的`lazy+Suspense`）和异步导入，将启动时间从 10 秒缩短至 3 秒。

- 🏗️ **迁移计算密集型任务到 WebAssembly/Native 模块**  
  Notion、Figma 等应用通过 WASM 或原生模块（如 1Password 加密）优化性能，实现确定性高性能。

- 📸 **利用 V8 快照加速初始化**  
  使用`electron-link`生成快照（如 Atom 启动提速 50%），避免动态值且适用于框架初始化阶段。

- 📊 **监控生产环境用户体验指标**  
  收集点击/滚动延迟等感知性能数据（如 Slack 内置监控工具），VSCode 通过输入延迟追踪版本回归。

- 🔥 **端到端 JavaScript 性能分析**  
  Notion 借助 Palette 平台分析生产环境代码瓶颈，定位 15% 输入延迟问题，缩短故障排查周期 3-4 周。

---

### [从 API 密钥迁移至 OAuth 2.1：为 AI 代理实现安全的机器间认证](https://www.scalekit.com/blog/migrating-from-api-keys-to-oauth-mcp-servers?utm_source=node-weekly&utm_medium=developers-guide&utm_campaign=paid-inclusion)

**原文标题**: [Migrate from API keys to OAuth 2.1: Secure M2M authentication for AI agents](https://www.scalekit.com/blog/migrating-from-api-keys-to-oauth-mcp-servers?utm_source=node-weekly&utm_medium=developers-guide&utm_campaign=paid-inclusion)

本文介绍了如何将 MCP 服务器的身份验证从 API 密钥迁移到 OAuth 2.1，强调了 OAuth 2.1 的安全性和可扩展性，并提供了使用 Scalekit 简化迁移过程的步骤和最佳实践。

- 🔐 **OAuth 2.1 的必要性**：2025 年起，OAuth 2.1 成为 MCP 服务器的强制标准，取代静态 API 密钥，提供更安全的机器间通信。
- ⚠️ **API 密钥的局限性**：静态密钥无法限制访问范围、缺乏追踪能力，一旦泄露风险极高。
- 🔄 **OAuth 2.1 的优势**：短期有效的令牌、细粒度权限控制（scopes）、审计日志支持，并符合企业级标准。
- 🛠️ **迁移步骤**：
  - 1️⃣ 在 Scalekit 注册客户端，获取`client_id`和`client_secret`。
  - 2️⃣ 客户端通过凭证交换短期访问令牌。
  - 3️⃣ API 调用时携带 Bearer 令牌。
  - 4️⃣ 服务端验证令牌签名、元数据及自定义声明（如`org_id`）。
- 📊 **渐进式迁移建议**：
  - 清点现有 API 密钥使用情况。
  - 定义细粒度 scopes 和租户隔离策略。
  - API 同时支持密钥和 OAuth 2.1 令牌。
  - 监控迁移进度并设定密钥淘汰截止日期。
- 💡 **Scalekit 的作用**：托管授权服务器，简化令牌颁发、验证及多租户管理，无需自建基础设施。
- ⚡ **常见问题**：
  - 避免过度宽泛的 scopes。
  - 安全存储`client_secret`。
  - 令牌缓存以减少频繁请求。
  - 注意 Client Credentials 流程不包含刷新令牌。
- 🚀 **未来价值**：OAuth 2.1 提升 API 安全性，适应现代架构和合规要求，支持企业级客户集成。

---

### [从 API 密钥迁移至 OAuth 2.1：为 AI 代理提供安全的机器间认证](https://www.scalekit.com/blog/migrating-from-api-keys-to-oauth-mcp-servers?utm_source=node-weekly&utm_medium=developers-guide&utm_campaign=paid-inclusion)

**原文标题**: [Migrate from API keys to OAuth 2.1: Secure M2M authentication for AI agents](https://www.scalekit.com/blog/migrating-from-api-keys-to-oauth-mcp-servers?utm_source=node-weekly&utm_medium=developers-guide&utm_campaign=paid-inclusion)

本文介绍了如何从使用静态 API 密钥迁移到 OAuth 2.1 来增强 MCP 服务器的安全性和可扩展性，并详细说明了使用 Scalekit 简化这一过程的步骤和优势。

- 🔐 **OAuth 2.1 的必要性**：2025 年起，OAuth 2.1 将成为 MCP 服务器的强制标准，取代静态 API 密钥，提供更高的安全性和可追溯性。
- ⚠️ **API 密钥的局限性**：静态 API 密钥缺乏灵活性、无法限制访问范围、难以追踪请求来源，且在泄露时无法自动失效。
- 🔄 **OAuth 2.1 的优势**：通过短生命周期、范围限定的令牌，减少泄露风险，支持客户端唯一标识和审计日志，符合企业标准。
- 🛠️ **迁移步骤**：
  - 1️⃣ 在 Scalekit 中注册客户端，获取`client_id`和`client_secret`。
  - 2️⃣ 使用客户端凭证交换访问令牌。
  - 3️⃣ 在 API 请求中使用 Bearer 令牌。
  - 4️⃣ 在 API 服务器上验证令牌的签名、元数据和自定义声明。
- 📊 **逐步迁移计划**：
  - 清点现有 API 密钥使用情况。
  - 定义细粒度的访问范围和租户隔离。
  - 在 API 中同时支持 API 密钥和 OAuth 2.1 令牌。
  - 逐步迁移客户端并监控使用情况。
  - 设定明确的 API 密钥淘汰日期。
- 🚀 **Scalekit 的作用**：简化 OAuth 2.1 的实现，提供令牌颁发和验证功能，无需自建授权服务器。
- ⚡ **内部服务通信示例**：展示了如何通过 OAuth 2.1 和 Scalekit 保护订单服务与库存服务之间的通信。
- ❓ **常见问题**：
  - OAuth 2.1 令牌是动态的、短生命周期的，而 API 密钥是静态的。
  - 不需要手动轮换 OAuth 2.1 令牌。
  - Scalekit 支持多租户令牌声明和完整的 OAuth 2.1 合规性。
  - 开发环境可通过测试组织和模拟器进行测试。
  - 迁移期间可同时支持 API 密钥和 OAuth 2.1 令牌。

---

### [在 Node.js 中设置控制台文本样式](https://2ality.com/2025/05/ansi-escape-sequences-nodejs.html)

**原文标题**: [Styling console text in Node.js](https://2ality.com/2025/05/ansi-escape-sequences-nodejs.html)

本文介绍了如何在 Node.js 中通过 ANSI 转义序列和内置工具对控制台输出的文本进行样式设置。

- 🎨 **ANSI 转义序列**：用于控制终端文本颜色、字体样式等，以 ASCII 转义字符和方括号开头。  
- 📜 **SGR 控制序列**：通过`\x1B[`和属性代码设置显示属性，如`1`表示加粗，`22`表示恢复正常。  
- 🛠️ **Node.js 工具**：`util.styleText()`函数可生成带样式的文本字符串，支持多种修饰符如`bold`、`red`等。  
- 🏷️ **模板标签**：可创建自定义模板标签（如加粗标签`b`），简化样式文本的生成。  
- ⚠️ **终端检测**：`process.stdout.isTTY`判断输出是否为终端，非终端环境可能忽略样式。  
- 🔧 **强制样式**：通过`validateStream: false`或环境变量`FORCE_COLOR`强制保留样式。  
- 📖 **less 命令**：默认不解析 ANSI 序列，需添加`-R`选项显示样式文本。

---

### [解析 Node.js 内存 - 从原始字节到可用数据 | banjocode](https://www.banjocode.com/post/node/memory-management)

**原文标题**: [Unpacking Node.js Memory - From Raw Bytes to Usable Data | banjocode](https://www.banjocode.com/post/node/memory-management)

概述  
本文深入探讨了 Node.js 中的内存管理机制，从最基础的二进制数据到高级的 Buffer 操作，逐步解析了 ArrayBuffer、TypedArray 和 Buffer 的作用及其相互关系。  

- 🔍 作者出于对 Node.js 底层机制的好奇，探索了文件管理、流、缓冲区和内存管理等高级特性。  
- 🧠 ArrayBuffer 是固定大小的二进制数据块，无法直接读写，需通过 TypedArray 或 DataView 操作。  
- 🔢 TypedArray（如 Int8Array、Uint32Array）为 ArrayBuffer 提供特定类型的数据视图，同一内存可被不同视图解析为不同结果。  
- 📊 不同整数类型（8/16/32/64 位）占用内存不同，影响数值范围和精度（如 Int8 范围：-128~127）。  
- 🔄 TypedArray 不拥有数据，仅作为视图，修改数据会直接影响底层的 ArrayBuffer。  
- 🛠️ Buffer 是 Node.js 全局对象，基于 Uint8Array，提供更便捷的二进制数据操作方法（如字符串编码转换）。  
- 📂 Node.js 中文件读取默认返回 Buffer，适合处理大文件（流式读取避免内存溢出）。  
- 📚 抽象层级：ArrayBuffer（原始内存）→ TypedArray（类型化视图）→ Buffer（高级封装）。  
- 💡 理解这些概念有助于优化文件操作和内存管理，尽管日常开发中可能不常直接使用。

---

### [JavaScript 的 at() 方法如何简化数组索引 - Matt Smith](https://allthingssmitty.com/2025/05/19/how-javascript-at-method-makes-array-indexing-easier/)

**原文标题**: [
    How JavaScript’s at() method makes array indexing easier - Matt Smith
  ](https://allthingssmitty.com/2025/05/19/how-javascript-at-method-makes-array-indexing-easier/)

JavaScript 的`at()`方法为数组索引提供了更简洁的方式，特别适合从数组末尾访问元素。

- 🍎 `at()`方法是 ECMAScript 2022 新增的，支持负索引，如`fruits.at(-1)`直接获取末尾元素  
- 📏 相比传统方式`fruits[fruits.length - 1]`，代码更简洁且减少越界错误  
- 🔄 不仅适用于数组，还可用于字符串和类型化数组（如`Int8Array`）  
- ⚖️ 与方括号 notation 行为一致，越界时返回`undefined`，索引值会被截断而非四舍五入  
- 🚀 性能接近方括号 notation，现代浏览器（Chrome 92+ 等）均已支持  
- 📝 提供 polyfill 代码以兼容旧环境（如 IE）  
- 🛠️ 适用场景：获取最后消息、轮播图导航、历史栈查看等  
- 🐍 类似 Python/Ruby 的负索引语法，提升代码可读性

---

### [GitHub - googleapis/js-genai：适用于Gemini和Vertex AI 的 TypeScript/JavaScript SDK](https://github.com/googleapis/js-genai)

**原文标题**: [GitHub - googleapis/js-genai: TypeScript/JavaScript SDK for Gemini and Vertex AI.](https://github.com/googleapis/js-genai)

Google GenAI JavaScript SDK 是一个为 TypeScript 和 JavaScript 开发者设计的工具包，用于构建基于 Gemini 的应用程序，支持 Gemini Developer API 和 Vertex AI。  

- 🚀 **功能概述**：支持 Gemini 2.0 功能，包括内容生成、函数调用、流式传输等。  
- 🔒 **安全提示**：避免在客户端代码中暴露 API 密钥，建议在生产环境中使用服务器端实现。  
- ⚙️ **安装与初始化**：通过 `npm install @google/genai` 安装，支持 API 密钥或 Vertex AI 配置初始化。  
- 🌐 **API 版本选择**：可设置 `apiVersion` 选择稳定版（v1）或预览版（v1alpha）API 端点。  
- 📂 **模块功能**：  
  - `ai.models`：模型查询与元数据检查。  
  - `ai.caches`：管理缓存以降低重复提示成本。  
  - `ai.chats`：创建多轮交互的本地聊天对象。  
  - `ai.files`：上传文件并在提示中引用。  
  - `ai.live`：支持实时交互（文本/音频/视频输入，文本/音频输出）。  
- 📜 **示例代码**：提供快速入门、流式生成、函数调用等代码示例。  
- 🔄 **流式传输**：使用 `generateContentStream` 实现逐块响应。  
- 🔧 **函数调用**：通过声明函数、启用工具配置实现外部系统交互。  
- 📝 **内容结构**：支持多种 `contents` 参数类型（如 `Content`、`Part` 等），需注意 `FunctionCall` 的显式处理。  
- 🔄 **与其他 SDK 区别**：此为 Google Deepmind 官方 SDK，专注新功能；旧版 SDK（如 `@google/generative_language`）不再支持 Gemini 2.0+。  
- 📊 **项目状态**：开源（Apache-2.0 协议），563 星，67 分支，22 贡献者，TypeScript 编写。

---

### [Gemini API | Google 开发者人工智能平台](https://ai.google.dev/gemini-api/docs#javascript)

**原文标题**: [Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs#javascript)

Gemini API 提供了多种编程语言的调用示例，包括 Python、JavaScript、Go、Java 和 REST，并介绍了 Gemini 的不同模型及其特点。

- 🚀 **获取 API 密钥** - 快速获取 Gemini API 密钥并开始使用。  
- 🐍 **Python 示例** - 使用 Python 调用 Gemini API 生成内容。  
- 🌐 **JavaScript 示例** - 通过 JavaScript 调用 Gemini API 生成内容。  
- 🏃 **Go 示例** - 使用 Go 语言调用 Gemini API 生成内容。  
- ☕ **Java 示例** - 通过 Java 调用 Gemini API 生成内容。  
- 🔗 **REST 示例** - 使用 curl 命令通过 REST API 调用 Gemini 生成内容。  
- 🤖 **模型介绍** - Gemini 提供了多种模型，包括 2.5 Pro（复杂推理）、2.5 Flash（多模态）、2.0 Flash-Lite（高效任务处理）。  
- 🖼️ **原生图像生成** - Gemini 2.0 Flash 支持原生图像生成和编辑。  
- 📜 **长文本处理** - Gemini 模型支持处理数百万 token 的输入，包括非结构化图像、视频和文档。  
- 📊 **结构化输出** - Gemini 可以生成 JSON 格式的响应，便于自动化处理。  
- 📜 **许可证信息** - 内容遵循 Creative Commons Attribution 4.0 License，代码示例遵循 Apache 2.0 License。

---

### [GitHub - astracompiler/cli: 🚀 快速、可靠且易于使用的 JavaScript 转可执行文件编译器](https://github.com/astracompiler/cli)

**原文标题**: [GitHub - astracompiler/cli: 🚀 Fast, reliable and easy-to-use js-to-exe compiler.](https://github.com/astracompiler/cli)

Astra 是一个快速、可靠且易于使用的 JavaScript 到可执行文件的编译器，支持最新的 Node.js 版本，并致力于提供卓越的开发者体验。它通过 esbuild 实现快速编译，支持 ESM 应用，并生成独立的可执行文件。Astra 目前仅支持 Windows 应用，但正在开发 macOS 和 Linux 版本。该项目采用 MIT 许可证，欢迎贡献。

- 🚀 **快速编译** - 使用 esbuild 实现最快的编译速度。  
- 📦 **轻量级输出** - 生成约 70-80MB 的可执行文件，使用 upx 可压缩至约 30MB。  
- 🔄 **支持最新 Node.js** - 兼容最新的 Node.js 版本。  
- 📝 **改进的 ECMAScript 支持** - 支持编译基于 ESM 的应用。  
- 🛠️ **开发者友好** - 使用 signale、inquirer 和 chalk 提供出色的开发者体验。  
- 🏷️ **可定制元数据** - 可修改生成的 exe 文件的图标、名称、版本等。  
- 🤝 **欢迎贡献** - 接受并审核所有贡献，即使是小修复。  
- 📜 **MIT 许可证** - 项目采用 MIT 许可证。  
- ❤️ **由 QwertyCodeQC 开发** - 用爱心打造的工具。

---

### [GitHub - kepano/defuddle: 从网页中提取主要内容](https://github.com/kepano/defuddle)

**原文标题**: [GitHub - kepano/defuddle: Extract the main content from web pages.](https://github.com/kepano/defuddle)

Defuddle 是一个用于从网页中提取主要内容的工具，通过移除非必要元素（如评论、侧边栏、页眉页脚等）来生成简洁易读的 HTML 文档。

- 🛠️ **功能特点**  
  - 清理网页内容，保留核心信息（正文、标题、作者等）。  
  - 优化输出一致性，支持脚注、数学公式、代码块等标准化格式。  
  - 提取元数据（如 schema.org 数据、网站图标、发布日期等）。  
  - 可作为 Mozilla Readability 的替代方案，容错性更强。  

- 📦 **安装与使用**  
  - 浏览器端：通过 `npm install defuddle` 安装，直接解析当前文档。  
  - Node.js 端：需额外安装 JSDOM，支持从 HTML 字符串或 URL 解析内容。  
  - 提供调试模式（`debug: true`）和 Markdown 转换选项（`markdown: true`）。  

- 📄 **输出内容**  
  - 返回对象包含 `content`（清理后的内容）、`title`、`author`、`description`、`wordCount` 等属性。  

- 🔧 **标准化处理**  
  - 标题优化（H1 转 H2，移除重复标题）。  
  - 代码块保留语言标识，移除行号和语法高亮。  
  - 脚注和数学公式（MathML/LaTeX）转换为统一格式。  

- 🧩 **多版本支持**  
  - **核心版**（`defuddle`）：基础功能，无依赖。  
  - **完整版**（`defuddle/full`）：支持数学公式解析。  
  - **Node.js 版**（`defuddle/node`）：集成 JSDOM，支持 Markdown 转换。  

- 🚀 **开发与构建**  
  - 通过 `npm run build` 编译项目，依赖 TypeScript 和 HTML。  
  - 开源协议：MIT License。  

- 🌟 **项目状态**  
  - GitHub 星标 1.8k，分支 41 个，持续维护中。  
  - 主要用于 Obsidian Web Clipper 等场景。

---

### [GitHub - mozilla/readability: 可读性库的独立版本](https://github.com/mozilla/readability)

**原文标题**: [GitHub - mozilla/readability: A standalone version of the readability lib](https://github.com/mozilla/readability)

Mozilla 的 Readability.js 是一个独立的库，用于 Firefox 阅读模式，能够解析网页并提取主要内容。

- 📦 **安装**：可通过 npm 安装`@mozilla/readability`，支持 Node.js 和浏览器环境。
- 🛠️ **基本用法**：通过`new Readability(document).parse()`解析 DOM 文档，返回文章标题、内容等元数据。
- ⚙️ **配置选项**：支持调试模式、元素解析上限、保留特定 HTML 类等参数定制。
- 🔄 **DOM 处理**：默认会修改原始 DOM，建议传入文档克隆对象以避免影响原页面。
- 🚦 **预检测接口**：`isProbablyReaderable()`快速判断文档是否适合解析，可配置内容长度和可见性检查。
- 🖥️ **Node.js 支持**：需配合`jsdom`等 DOM 库使用，需指定 URL 以处理相对路径。
- 🔒 **安全建议**：强烈建议对不可信输入使用 DOMPurify sanitizer 库，并启用 CSP 防止脚本注入。
- 🤝 **贡献与许可**：接受社区贡献，采用 Apache 2.0 开源协议，版权归 Arc90 Inc 所有。

---

### [解谜游乐场](https://kepano.github.io/defuddle/)

**原文标题**: [Defuddle Playground](https://kepano.github.io/defuddle/)

解析 HTML 工具界面概览  

- 🎮 输入 HTML 区域：提供原始 HTML 代码输入功能  
- 🧹 清除按钮：一键清空输入/输出内容  
- 🔍 解析按钮：触发 HTML 解析与处理操作  
- 📝 输出显示区：展示解析后的内容/元数据/调试信息  
- 📊 多标签页：支持切换查看内容/元数据/调试详情  
- 🐞 调试功能：提供 HTML 处理过程中的诊断信息  

（注：此为功能界面描述，未涉及具体操作逻辑或技术实现细节）

---

### [GitHub - seanpmaxwell/express-generator-typescript：创建一个类似express-generator但使用TypeScript的新express应用](https://github.com/seanpmaxwell/express-generator-typescript)

**原文标题**: [GitHub - seanpmaxwell/express-generator-typescript: Create a new express app similar to express-generator but with TypeScript](https://github.com/seanpmaxwell/express-generator-typescript)

这是一个名为`express-generator-typescript`的 GitHub 仓库，用于生成基于 TypeScript 的 Express 应用程序框架。

- 🚀 **项目目的**: 类似于`express-generator`，但生成的是使用 TypeScript 而非 JavaScript 的 Express 应用。
- 🛠️ **功能特点**: 配置了 TypeScript 最佳实践，支持相对路径，无需额外配置`tsconfig-paths`和`module-alias`。
- 📦 **安装方式**: 可以通过`npx`或全局安装`npm install -g express-generator-typescript`来使用。
- ⚡ **快速开始**: 使用`npx express-generator-typescript`创建项目，支持`--use-yarn`选项使用 yarn。
- 🔥 **开发命令**: 提供多种 npm 脚本，如开发模式`npm run dev`、单元测试`npm run test`、生产构建`npm run build`等。
- 🐛 **调试支持**: 使用`nodemon`开发时支持调试，需修改`package.json`中的`nodemonConfig`。
- 📝 **VSCode 用户注意**: 需要配置`.vscode/settings.json`以支持 eslint。
- 📜 **许可证**: MIT 许可证。
- 🌟 **项目状态**: 879 stars，83 forks，14 位贡献者。

---

### [GitHub - express-rate-limit/express-slow-down: 减缓重复请求；可作为 express-rate-limit 的替代（或补充）方案](https://github.com/express-rate-limit/express-slow-down)

**原文标题**: [GitHub - express-rate-limit/express-slow-down: Slow down repeated requests; use as an alternative (or addition) to express-rate-limit](https://github.com/express-rate-limit/express-slow-down)

express-slow-down 是一个基于 Express 的中间件，用于减缓重复请求的响应速度，而非直接阻止请求。它适用于公共 API 或密码重置等端点，可与 express-rate-limit 配合使用。

- 🚦 **功能**：减缓重复请求的响应速度，而非直接阻止请求。
- 🔧 **兼容性**：与 express-rate-limit 兼容，并基于其构建。
- 🏪 **存储**：默认使用内存存储，也支持外部存储（需不同前缀避免重复计数）。
- 📦 **安装**：可通过 npm、yarn 或 pnpm 安装，也支持从 GitHub Releases 下载。
- ⏳ **使用示例**：可全局应用或针对特定路由，支持自定义延迟逻辑（如指数级延迟）。
- ⚙️ **配置选项**：包括窗口时间（windowMs）、初始延迟请求数（delayAfter）、延迟时间（delayMs）和最大延迟（maxDelayMs）。
- 📡 **请求 API**：在请求对象中添加 req.slowDown 属性，包含当前请求的延迟信息。
- 🐛 **问题与贡献**：欢迎提交问题和贡献代码，需先阅读贡献指南。
- 📜 **许可证**：MIT 许可证，由 Nathan Friedly 和 Vedant K 维护。

---

### [发布版本 30.0.0 · photostructure/exiftool-vendored.js · GitHub](https://github.com/photostructure/exiftool-vendored.js/releases/tag/30.0.0)

**原文标题**: [Release Release 30.0.0 · photostructure/exiftool-vendored.js · GitHub](https://github.com/photostructure/exiftool-vendored.js/releases/tag/30.0.0)

概述：  
PhotoStructure 的 exiftool-vendored.js 项目发布了 30.0.0 版本，主要更新包括放弃对 Node v18 的支持、升级 ExifTool 至 13.29 版本、新增 TagNames 枚举以及自动化发布流程等。

- 💔 放弃对 Node v18 的支持，因其生命周期已结束。  
- 🌱 将 ExifTool 升级至 13.29 版本。  
- ✨ 新增 TagNames 字符串枚举，包含约 2500 个常用标签字段名，并支持用户反馈补充缺失字段。  
- 📦 将 Tags 接口中的.tz 字段更名为.zone，未来版本将弃用.tz。  
- 🤖 通过 GitHub Actions 实现 ExifTool 版本更新的全自动化。  
- 🔧 更新了 CI 工作流中的 Node.js 版本，新增 v24 并移除 v18。  
- 📄 添加了 CLAUDE.md 文件，包含项目指导和关键命令。  
- 🔄 重构了多个功能模块，包括时区处理、字符串枚举等。  
- 🛠️ 修复了多个问题并优化了代码结构。

---

### [GitHub - axa-group/oauth2-mock-server: 面向开发与测试的 OAuth2 模拟服务器](https://github.com/axa-group/oauth2-mock-server)

**原文标题**: [GitHub - axa-group/oauth2-mock-server: A development and test oriented OAuth2 mock server](https://github.com/axa-group/oauth2-mock-server)

AXA Group 的 OAuth2-mock-server 是一个专为开发和测试设计的模拟 OAuth2 服务器，支持多种授权类型和自定义配置。

- 🚀 **项目概述**: 一个易于配置的 OAuth2 模拟服务器，用于开发和自动化测试，不支持生产环境使用。
- ⚠️ **警告**: 该工具缺乏生产级 OAuth2 服务器所需的许多功能。
- 🔧 **开发前提**: 需要 Node.js 20.19+ 环境。
- 📦 **安装**: 通过 npm 安装为开发依赖项：`npm install --save-dev oauth2-mock-server`。
- � **快速开始**: 支持生成 RSA 密钥、启动和停止服务器，以及构建 JWT 令牌。
- 🔑 **支持的授权类型**: 包括客户端凭证、资源所有者密码凭证、授权码（带 PKCE 支持）和刷新令牌。
- 🔐 **支持的 JWK 格式**: 包括 RSA、ECDSA 和 EdDSA 等多种算法。
- 🎣 **自定义钩子**: 提供事件发射器，允许自定义令牌签名、响应体等。
- 🔗 **HTTPS 支持**: 可配置 SSL/TLS，推荐使用 `mkcert` 生成本地信任证书。
- 🌐 **支持的端点**: 包括 OpenID 配置、JWKS、令牌颁发、用户信息、令牌吊销等。
- 💻 **命令行界面**: 支持全局安装或通过 npx 直接运行。
- 📜 **许可证**: MIT 许可证。
- 👥 **贡献**: 欢迎贡献，遵循项目行为准则。

---

### [发布 slonik@48.0.0 · gajus/slonik · GitHub](https://github.com/gajus/slonik/releases/tag/slonik%4048.0.0)

**原文标题**: [Release slonik@48.0.0 · gajus/slonik · GitHub](https://github.com/gajus/slonik/releases/tag/slonik%4048.0.0)

Slonik 项目的最新动态及错误提示。

- 🚨 页面加载错误，需重新加载。  
- 🔔 需登录以更改通知设置。  
- 🌟 项目获得 4.8k 星标，144 次分叉。  
- 🛠️ 26 个未解决问题，无拉取请求。  
- 🔒 安全及其他导航选项可用。  
- 🏷️ 最新版本 slonik@48.0.0 于 5 月 19 日发布。  
- 🔍 包含 4 次提交至主分支。  
- 📜 主要变更：支持 ESM、兼容 zod v4 的@standard-schema/spec、原生 OpenTelemetry 工具（中间件和查询日志）。  
- ⚠️ 资产加载错误，需重新加载页面。

---

### [GitHub - salsita/node-pg-migrate: PostgreSQL 的 Node.js 数据库迁移管理工具](https://github.com/salsita/node-pg-migrate)

**原文标题**: [GitHub - salsita/node-pg-migrate: Node.js database migration management for PostgreSQL](https://github.com/salsita/node-pg-migrate)

node-pg-migrate 是一个专为 PostgreSQL 设计的 Node.js 数据库迁移管理工具，支持其他符合 SQL 标准的数据库如 CockroachDB。该项目由 Theo Ephraim 发起，现由 Salsita Software 维护，当前维护者是 @Shinigami92。

- 🚀 **功能特点**：专为 PostgreSQL 设计，提供全功能支持，简化使用和维护。
- ⚙️ **前置条件**：需要 Node.js 20.11+ 和 PostgreSQL 13+，需安装 `pg` 库。
- 📦 **安装**：通过 `npm add --save-dev node-pg-migrate` 安装，提供可执行文件。
- 📝 **快速示例**：创建迁移文件，定义 `up` 函数执行数据库操作，如创建表、添加列等。
- 🔗 **文档**：完整文档可在 [salsita.github.io/node-pg-migrate](https://salsita.github.io/node-pg-migrate) 查看。
- 🤝 **贡献**：欢迎开发者贡献，项目开源且社区友好。
- 📜 **许可证**：MIT 许可证，允许自由使用和修改。
- 🌟 **项目状态**：1.4k stars，182 forks，82 位贡献者，11.5k+ 项目使用。

---

### [GitHub - octokit/octokit.js：全功能GitHub SDK，适用于浏览器、Node.js 和 Deno。](https://github.com/octokit/octokit.js)

**原文标题**: [GitHub - octokit/octokit.js: The all-batteries-included GitHub SDK for Browsers, Node.js, and Deno.](https://github.com/octokit/octokit.js)

octokit.js 是一个功能全面的 GitHub SDK，支持浏览器、Node.js 和 Deno 环境，提供 REST API、GraphQL API、身份验证等功能。

- 🚀 **功能全面** - 覆盖 GitHub 平台 API 的所有功能，并遵循最佳实践。
- 🌍 **跨平台支持** - 兼容现代浏览器、Node.js 和 Deno。
- 🧪 **高测试覆盖率** - 所有库均达到 100% 测试覆盖率。
- 📦 **模块化设计** - 可按需使用部分功能或构建自定义 Octokit 实例。
- 🔌 **可扩展性** - 支持插件和钩子机制，可扩展功能或自定义身份验证策略。
- 🔒 **身份验证支持** - 支持静态令牌、GitHub App、OAuth 等多种身份验证方式。
- 📊 **REST 和 GraphQL API** - 提供便捷的 REST 端点方法和 GraphQL 查询支持。
- 🔄 **分页处理** - 内置分页 API，支持遍历大量数据。
- 🛡️ **错误处理** - 提供详细的请求错误信息，便于调试和处理。
- 🤖 **GitHub App 和 Webhooks** - 支持 GitHub App 的安装管理和 Webhook 事件处理。
- 🔄 **OAuth 支持** - 提供 OAuth 登录流程和令牌管理功能。
- 📜 **MIT 许可证** - 开源且允许自由使用和修改。

---

### [GitHub - sindresorhus/image-type：检测Buffer/Uint8Array的图像类型](https://github.com/sindresorhus/image-type)

**原文标题**: [GitHub - sindresorhus/image-type: Detect the image type of a Buffer/Uint8Array](https://github.com/sindresorhus/image-type)

这是一个名为 `image-type` 的开源项目，用于检测 `Buffer/Uint8Array` 中的图像类型。

- 🏷️ **项目名称**: image-type  
- 🌟 **Star 数**: 389  
- 🍴 **Fork 数**: 16  
- 📜 **许可证**: MIT  
- 📦 **安装方式**: `npm install image-type`  
- 🖼️ **功能**: 检测 `ArrayBuffer/Uint8Array` 中的图像类型，返回扩展名和 MIME 类型  
- 📏 **最小字节数**: 需要至少 4100 字节来检测文件类型  
- 🌐 **支持环境**: Node.js 和浏览器  
- 📄 **支持的文件类型**: 包括 `jpg`、`png`、`gif`、`webp`、`bmp`、`ico` 等  
- 🔗 **相关项目**: `file-type`（检测更多文件类型）、`image-dimensions`（获取图像尺寸）  
- 📂 **代码托管**: GitHub  
- 👥 **贡献者**: 7 人  
- 💻 **主要语言**: JavaScript (64.7%) 和 TypeScript (35.3%)

---

### [GitHub - expressjs/multer: 用于处理 `multipart/form-data` 的 Node.js 中间件](https://github.com/expressjs/multer)

**原文标题**: [GitHub - expressjs/multer: Node.js middleware for handling `multipart/form-data`.](https://github.com/expressjs/multer)

Multer 是一个 Node.js 中间件，用于处理 `multipart/form-data` 类型的数据，主要用于文件上传。它基于 busboy 实现，效率极高。Multer 不会处理非 multipart 类型的表单数据。

- 🚀 **功能概述**  
  - Multer 是 Node.js 中间件，专为处理文件上传设计。  
  - 仅支持 `multipart/form-data` 类型的表单。  

- 📦 **安装与基础用法**  
  - 安装命令：`npm install multer`。  
  - 通过 `upload.single()`、`upload.array()` 或 `upload.fields()` 处理单个或多个文件上传。  

- 📂 **存储选项**  
  - **DiskStorage**：自定义文件存储路径和文件名（需手动创建目录）。  
  - **MemoryStorage**：文件以 Buffer 形式暂存内存，适用于小文件。  

- ⚠️ **注意事项**  
  - 内存存储（MemoryStorage）需警惕大文件或高并发导致的内存溢出。  
  - 全局使用 Multer 存在安全风险，建议仅在特定路由启用。  

- 🔧 **配置选项**  
  - `dest`：指定文件存储目录（自动创建）。  
  - `limits`：限制上传文件大小、数量等，防止 DoS 攻击。  
  - `fileFilter`：通过函数控制文件类型过滤。  

- ❌ **错误处理**  
  - Multer 错误可通过 `err instanceof multer.MulterError` 捕获，其他错误由 Express 处理。  

- 🌍 **多语言支持**  
  - README 提供阿拉伯语、中文、韩文等翻译版本。  

- 📜 **开源协议**  
  - 采用 MIT 许可证，代码托管于 GitHub（11.8k stars，1.1k forks）。

---

### [GitHub - faker-js/faker: 在浏览器和 Node.js 中生成大量虚假数据](https://github.com/faker-js/faker)

**原文标题**: [GitHub - faker-js/faker: Generate massive amounts of fake data in the browser and node.js](https://github.com/faker-js/faker)

Faker 是一个用于在浏览器和 Node.js 中生成大量假数据的开源库，支持多种语言和模块，适用于测试和开发场景。

- 🚀 **功能丰富** - 支持生成人物、地点、日期、金融、商业、黑客等多种类型的假数据。
- 🌏 **多语言支持** - 提供超过 70 种语言的本地化数据生成。
- 📦 **安装简单** - 通过 npm 安装 `@faker-js/faker` 即可使用。
- 🪄 **使用示例** - 提供 ESM 和 CJS 两种导入方式，并包含生成随机用户的代码示例。
- 💎 **模块化设计** - 提供详细的 API 文档，支持模板生成和自定义数据组合。
- 🌏 **本地化实例** - 可以导入不同语言的实例，支持自定义回退语言。
- ⚙️ **随机种子设置** - 通过设置种子确保生成的数据具有一致性。
- 🤝 **赞助支持** - 项目由社区赞助支持，MIT 许可证开源。
- ✨ **贡献指南** - 提供贡献指南，欢迎社区参与开发。
- 📜 **历史背景** - 解释了原始 faker.js 的变更和团队更新。
- 🔑 **许可证** - 采用 MIT 许可证，代码和文档托管在 fakerjs.dev。

---

### [发布 v21.0.0 · sindresorhus/file-type · GitHub](https://github.com/sindresorhus/file-type/releases/tag/v21.0.0)

**原文标题**: [Release v21.0.0 · sindresorhus/file-type · GitHub](https://github.com/sindresorhus/file-type/releases/tag/v21.0.0)

该内容是关于 GitHub 仓库"sindresorhus/file-type"的发布版本 v21.0.0 的更新日志，包含重大变更、改进和修复。

- 🚨 **重大变更**：要求 Node.js 20 版本，并移除了 Adobe Illustrator (.ai) 文件检测支持。  
- 📌 **MIME 类型修正**：对 Matroska 视频、FLAC、Apache Parquet 和 Apache Arrow 的 MIME 类型进行了正式 IANA 注册修正。  
- 🔧 **改进**：允许直接向导出函数传递选项，并新增了`mpegOffsetTolerance`选项。  
- 🛠 **修复**：解决了部分 PAX TAR 格式的检测问题。  
- 🔄 **错误提示**：页面加载错误时提示重新加载。  
- 🔔 **通知设置**：用户需登录以更改通知设置。  
- 📊 **仓库数据**：拥有 4k 星标、382 次分叉，当前有 5 个议题和 1 个拉取请求。

---

### [GitHub - PrismarineJS/mineflayer: 使用强大、稳定且高级的 JavaScript API 创建 Minecraft 机器人](https://github.com/PrismarineJS/mineflayer)

**原文标题**: [GitHub - PrismarineJS/mineflayer: Create Minecraft bots with a powerful, stable, and high level JavaScript API.](https://github.com/PrismarineJS/mineflayer)

PrismarineJS 的 Mineflayer 是一个用于创建 Minecraft 机器人的强大、稳定且高级的 JavaScript API，支持 Python 使用。支持 Minecraft 1.8 至 1.21 版本，提供多种功能如实体追踪、方块查询、物理运动、攻击实体、物品管理等。项目拥有丰富的文档、示例和第三方插件，社区活跃，持续更新。

- 🚀 **功能强大** - 支持 Minecraft 1.8 到 1.21 版本，提供实体追踪、方块查询、物理运动等功能。
- 📚 **文档丰富** - 提供教程、API 参考、常见问题解答等详细文档。
- 🛠️ **模块化设计** - 使用多个独立 npm 包实现功能，如 minecraft-protocol、prismarine-physics 等。
- 🔌 **第三方插件** - 支持多种插件扩展功能，如 pathfinder、prismarine-viewer 等。
- 🌍 **多语言支持** - 提供中文等多种语言的文档。
- 📈 **活跃社区** - 拥有 5.7k 星和 1k fork，持续更新和维护。
- 🎥 **视频教程** - 提供多个视频教程帮助用户快速上手。
- 🧪 **测试完善** - 支持针对不同版本和功能的测试。
- 📜 **MIT 许可** - 开源免费使用。

---

### [发布 v7.10.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.10.0)

**原文标题**: [Release v7.10.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.10.0)

Undici 是一个 Node.js 的 HTTP/1.1 客户端，最新版本 v7.10.0 发布，包含多项功能改进和问题修复。

- 🚀 新增 "clientLifetime" 选项，支持设置连接池中连接的关闭和移除时间 (#4175)  
- 🐛 修复了代理内存泄漏问题 (#4223)  
- 📊 新增检测 MemoryCacheStore 达到最大容量的能力 (#4224)  
- 🔄 更新了 ProxyAgent 行为，使其在 HTTP->HTTP 代理连接中匹配 Curl 的行为 (#4180)  
- 📝 修正了 FormData 请求示例文档 (#4226)  
- 🔧 其他更新包括移除冗余测试、添加 Node v24 工作流、更新 WPT 等 (#4207, #4206, #4172)  
- 👋 欢迎新贡献者 @dhalbrook, @caitp, @inyourtime 的首次贡献  
- 📦 完整更新日志可查看 v7.9.0...v7.10.0

---

### [发布 v14.0.0 · tj/commander.js · GitHub](https://github.com/tj/commander.js/releases/tag/v14.0.0)

**原文标题**: [Release v14.0.0 · tj/commander.js · GitHub](https://github.com/tj/commander.js/releases/tag/v14.0.0)

commander.js 发布了 v14.0.0 版本，要求 Node.js v20 或更高版本，新增了功能组支持和未转义负数参数解析，修复了一些问题，并进行了内部重构。

- 🚀 新增了对选项和命令组支持，通过 `.helpGroup()`、`.optionsGroup()` 和 `.commandsGroup()` 方法 (#2328)  
- 🔢 支持未转义的负数作为选项参数和命令参数 (#2339)  
- 🛠 TypeScript 中为 `Argument` 类添加了 `parseArg` 属性 (#2359)  
- 🐛 修复了帮助信息中默认值无描述时的多余空格问题 (#2348)  
- 🔄 `.configureOutput()` 现在复制设置而非原地修改，避免副作用 (#2350)  
- ⚠️ 重大变更：Commander 14 需要 Node.js v20 或更高版本  
- 🔧 内部重构了 `Help` 类，新增 `formatItemList()` 和 `groupItems()` 方法 (#2328)  
- 🎉 发布版本 v14.0.0，包含上述更新和修复

---

### [幼驹 TS](https://foalts.org/)

**原文标题**: [FoalTS](https://foalts.org/)

FoalTS 是一个全功能的 Node.js 框架，基于 TypeScript，简单易用且文档完善。它提供了丰富的内置功能，同时保持高度可扩展性，适合快速开发和高质量代码编写。

- 🚀 **一体化框架**：无需从头构建或整合第三方包，所有功能均已内置，但仍支持使用其他库。  
- 🛠️ **CLI 工具**：支持开发和生产环境的构建与运行，可生成文件。  
- 🗃️ **ORM 支持**：集成 TypeORM，可从模型生成迁移文件。  
- 🔐 **认证机制**：支持 JWT 和会话令牌，实现有状态或无状态认证。  
- � **自动化测试**：提供单元测试和端到端测试环境，含简易依赖注入系统。  
- 📄 **Swagger 生成**：直接从代码生成 OpenAPI 规范和 Swagger 文档。  
- 🛡️ **权限控制**：通过静态角色或动态权限管理路由访问。  
- 📜 **Shell 脚本**：创建命令行脚本并支持参数验证。  
- ☁️ **文件存储**：支持文件上传验证及本地或 AWS S3 存储。  
- ✨ **简洁设计**：仅需掌握控制器、服务和钩子三个核心概念，降低学习成本。  
- 💻 **TypeScript 优势**：利用强类型检测减少错误，提供自动补全和清晰的 API 文档。  
- 🔧 **快速开始**：提供完善的入门指南和社区支持。

---

### [ESLint v9.27.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/05/eslint-v9.27.0-released/)

**原文标题**: [ESLint v9.27.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/05/eslint-v9.27.0-released/)

ESLint v9.27.0 是一个小版本升级，引入了新功能并修复了之前版本中的多个错误。主要更新包括将 MCP 服务器分离为独立包、新增环境变量设置功能标志、规则改进及 TypeScript 语法支持增强等。

- 🚀 **MCP 服务器独立包**：ESLint MCP 服务器从核心中分离为 `@eslint/mcp` 包，减少依赖数量和大小，CLI 标志 `--mcp` 仍保留原有行为。
- 🔧 **环境变量设置功能标志**：新增 `ESLINT_FLAGS` 环境变量，便于在 CI/CD 或跨命令中统一启用功能标志。
- 📝 **排序抑制文件键名**：`eslint-suppressions.json` 中的对象键名现在会自动排序，减少不必要的差异。
- 🆕 **新增规则 `no-unassigned-vars`**：检测声明但未赋值的变量使用，避免潜在的编程错误。
- 🔍 **`no-useless-escape` 新增选项**：允许通过 `allowRegexCharacters` 指定正则表达式中无需转义的字符。
- 🔄 **`no-array-constructor` 支持自动修复**：大多数问题可通过 `--fix` 自动修复，不安全情况仍提供建议。
- 💻 **增强 TypeScript 语法支持**：核心规则 `max-params` 和 `no-unassigned-vars` 新增对 TypeScript 语法的支持。
- 🐛 **多项错误修复**：包括类型定义修正、规则匹配问题及文档更新等。
- 📚 **文档改进**：更新配置文件和编辑器集成文档，澄清未使用抑制规则会导致非零退出码。

---

### [比特。可组合软件。](https://bit.dev/?utm_source=NodeWeekly&utm_id=125%20)

**原文标题**: [Bit. Composable software.](https://bit.dev/?utm_source=NodeWeekly&utm_id=125%20)

概述总结  
Bit 平台庆祝其可组合性理念 10 周年，推出 Harmony，提供 AI 驱动的开发工作空间，支持可组合组件和零开销架构。Bit 通过组织源代码为可组合组件，帮助开发者构建可靠、可扩展的应用程序，并支持原子化部署和统一开发标准。  

- 🎉 庆祝可组合性 10 周年，推出 Harmony，AI 驱动开发工作空间  
- 🏗️ Bit 将代码组织为可组合组件，支持可靠、可扩展的应用程序开发  
- 🚀 支持原子化部署，确保简单、安全的测试和生产环境  
- 🔄 可组合架构，支持 Shell 应用、可复用组件和标准构建块  
- ⚡ 提供 SSR 和 SPA 性能优化，避免全页面刷新  
- � 提升 UX 一致性，简化组件集成和复用  
- 📦 减少依赖，简化架构，降低学习曲线  
- 🌐 技术栈无关，支持遗留系统和现代框架集成  
- 🛠️ 支持全栈功能开发，组合 UI 组件和后端服务  
- 🔍 通过本地 HMR 和 CI 测试，早期发现问题  
- 🔄 逐步采用可组合性，利用现有代码库  
- 🤖 内置 MCP 服务器，支持 AI 工具创建和复用组件  
- 📊 Bit 平台提供包管理、变更请求、图表和分析工具  
- 👥 拥有 10 万开发者、250+ 社区插件和 1.6 万 + GitHub 星标  
- 🌍 加入全球最大的开源组件社区，拥有 6 万 + 组件

---

### [为什么我们要为 Node.js 再创建一个 Kafka 客户端](https://blog.platformatic.dev/why-we-created-another-kafka-client-for-nodejs?showSharer=true)

**原文标题**: [Why we created another Kafka client for Node.js](https://blog.platformatic.dev/why-we-created-another-kafka-client-for-nodejs?showSharer=true)

Apache Kafka 已成为构建实时数据管道和流应用程序的基石，特别是在金融科技和媒体行业。Node.js 开发者传统上需要在 KafkaJS 和 Node-rdkafka 之间选择，但两者都存在维护和兼容性问题。因此，Platformatic 推出了新的 Kafka 库 @platformatic/kafka，旨在提供更好的性能、开发者体验和 TypeScript 支持。

- 🚀 **Kafka 在 Node.js 中的重要性**：Apache Kafka 是金融科技和媒体行业实时数据处理的核心工具。
- 🔧 **现有库的问题**：KafkaJS 已不再维护，Node-rdkafka 存在兼容性和性能问题。
- 🛠️ **新库的诞生**：@platformatic/kafka 旨在解决现有问题，提供更好的性能和开发者体验。
- 📈 **性能对比**：@platformatic/kafka 在生产者和消费者基准测试中均优于 KafkaJS 和 Node-rdkafka。
- 🔄 **开发者体验**：新库简化了 API，支持序列化和反序列化，并提供了更好的 TypeScript 集成。
- 🎯 **设计目标**：平衡性能、开发者体验和易用性，适用于现代 Node.js 开发。
- 📊 **基准测试结果**：@platformatic/kafka 在生产者和消费者测试中分别比 KafkaJS 快 25% 和 10.41%。
- 💡 **结论**：@platformatic/kafka 是一个高性能、易用的 Kafka 客户端，适合 Node.js 开发者。

---

### [JavaScript 简史 | Deno](https://deno.com/blog/history-of-javascript)

**原文标题**: [A brief history of JavaScript | Deno](https://deno.com/blog/history-of-javascript)

JavaScript 诞生 30 周年，从 1995 年诞生至今，已发展成为全球最流行的编程语言，深刻影响了互联网的发展。

- 🚀 **1994 年 12 月**：Netscape 发布 Netscape Navigator 1.0，为 JavaScript 的诞生奠定基础。
- ⚡ **1995 年 5 月**：Brendan Eich 用 10 天时间创造了 JavaScript，旨在为网页添加交互性。
- 📜 **1995 年 12 月**：Netscape 和 Sun 宣布 JavaScript，定位为轻量级脚本语言。
- 💻 **1996 年 3 月**：微软推出 JScript，与 Netscape 竞争，支持 ActiveX。
- 🌐 **1997 年 6 月**：JavaScript 提交给 ECMA 国际，标准化为 ECMAScript。
- 🔓 **1998 年 1 月**：Netscape 开源 Navigator，催生 Mozilla 项目。
- 📦 **1999 年 12 月**：ECMAScript 3 发布，引入正则表达式、异常处理等关键功能。
- 📡 **2004 年 4 月**：Gmail 推出，使用 AJAX 技术，开启 Web 2.0 时代。
- 🛠️ **2006 年 3 月**：jQuery 诞生，简化跨浏览器开发。
- 📱 **2007 年 1 月**：iPhone 发布，不支持 Flash，推动 JavaScript 在移动端的发展。
- 🚀 **2008 年 9 月**：Google 发布 Chrome 和 V8 引擎，大幅提升 JavaScript 性能。
- 🖥️ **2009 年 3 月**：Ryan Dahl 创建 Node.js，使 JavaScript 可用于服务器端开发。
- 🔄 **2015 年 6 月**：ECMAScript 6（ES2015）发布，引入模块化、Promise 等现代特性。
- ⚛️ **2015 年 5 月**：React 发布，推动组件化前端开发。
- 📦 **2016 年 3 月**：npm 的 leftpad 事件暴露供应链安全问题。
- 🛠️ **2017 年 9 月**：Yarn 发布，改进 npm 的依赖管理。
- 🌍 **2018 年 6 月**：Ryan Dahl 宣布 Deno 项目，反思 Node.js 的不足。
- 🤖 **2020 年 5 月**：JavaScript 随 SpaceX 龙飞船进入太空。
- 🚀 **2020 年 5 月**：Deno 1.0 发布，支持 TypeScript 和权限模型。
- 📜 **2022 年 6 月**：IE11 退役，推动 Web 标准化。
- 🐢 **2024 年 2 月**：Node.js 选择 Rocket Turtle 作为吉祥物。
- 📦 **2024 年 3 月**：JSR 发布，改进 JavaScript 包管理体验。
- ⚖️ **2024 年 9 月**：Deno 发起#FreeJavaScript 运动，挑战 Oracle 的商标权。
- 🚀 **2025 年 3 月**：TypeScript 计划移植到 Go，提升性能。

JavaScript 从简单的脚本语言发展为全栈开发的基石，未来将继续推动 Web 技术的创新。

---

### [关于 Deno 消亡的报道被严重夸大了 | Deno](https://deno.com/blog/greatly-exaggerated)

**原文标题**: [Reports of Deno's Demise Have Been Greatly Exaggerated | Deno](https://deno.com/blog/greatly-exaggerated)

Deno 近期虽面临质疑，但实际发展势头强劲，用户增长显著，平台功能持续优化。团队承认沟通不足导致误解，并澄清产品调整是基于实际需求而非退缩，同时预告多项新功能与改进即将推出。

- 🚀 Deno 2 发布后用户增长翻倍，Node 兼容性消除主要使用障碍  
- 🌍 Deno Deploy 区域缩减为 6 个，优化性能与合规性，转向应用托管平台  
- 🔄 即将支持子进程、后台任务、OpenTelemetry 及自托管区域  
- 💾 Deno KV 保持 beta 版，专注特定场景，未来将深化计算与状态绑定  
- 🌱 Fresh 2 注重质量打磨，稳定版将于年内发布  
- 🛠️ Deno 平台集成 TypeScript、权限控制、LSP、OpenTelemetry 等全栈工具链  
- 🌐 通过 JSR 推进开放治理，参与 TC39 标准制定，挑战 Oracle 商标争议  
- 🔜 基于 Deploy/KV 经验开发新产品，简化分布式应用构建  
- 🤝 承认沟通不足，承诺加强透明度并持续推动 JavaScript 生态进步

---

### [ESLint v9.0.0：回顾与展望 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/05/eslint-v9.0.0-retrospective/)

**原文标题**: [ESLint v9.0.0: A retrospective - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/05/eslint-v9.0.0-retrospective/)

ESLint v9.0.0 是近三年来的首个重大版本，重点引入了新的配置系统，但发布后遭遇了用户负面反馈和升级挑战。团队通过文档、工具支持和版本策略应对问题，并从中总结了改进经验。

- 🚀 **发布概况**：ESLint v9.0.0 于 2024 年 4 月发布，是三年来的首个重大版本，主打新配置系统，但初期用户反馈负面。  
- 📅 **开发时间线**：从 2019 年 RFC 提出到 2024 年正式发布，历时五年，中间经历了多次测试和预览版本。  
- ✅ **成功之处**：  
  - 📜 制定了明确的版本支持政策，并与 HeroDevs 合作维护旧版本。  
  - 🔧 提供了六个月对 v8.x 的兼容性支持，并改进了发布基础设施。  
  - 📚 发布了详尽的文档和迁移指南，帮助用户过渡。  
  - 🛠️ 快速响应问题，推出了兼容性工具和配置迁移器。  
- ❌ **不足之处**：  
  - ⚠️ 一次引入了过多破坏性变更，导致用户混淆和升级困难。  
  - 📖 文档过于冗长，用户更倾向于直接求助而非阅读指南。  
  - 🐢 生态系统适配缓慢，部分插件作者未及时更新支持。  
  - 🔄 未预见到插件作者对双配置支持的需求。  
- 📌 **经验教训**：  
  - 🔄 未来将采用更小、更频繁的重大更新，减少破坏性变更的集中引入。  
  - 🛠️ 优先开发工具（如自动化迁移工具），而非依赖文档。  
  - 💡 改进错误提示，直接引导用户解决问题。  
  - 🤝 加强生态系统的沟通和协作。  
- 🔮 **未来展望**：团队将持续优化发布流程和用户体验，吸取 v9.0.0 的教训，推动 ESLint 的进一步发展。

---

### [60 个恶意 npm 包泄露网络与主机数据于 Acti...](https://socket.dev/blog/60-malicious-npm-packages-leak-network-and-host-data)

**原文标题**: [60 Malicious npm Packages Leak Network and Host Data in Acti...](https://socket.dev/blog/60-malicious-npm-packages-leak-network-and-host-data)

美国国家标准与技术研究院（NIST）因国家漏洞数据库（NVD）处理积压和延迟问题正接受联邦审计，漏洞数据处理瓶颈日益严重，引发政府正式调查。  

- 🔍 NIST 因 NVD 处理积压和延迟问题接受联邦审计  
- ⚠️ 漏洞数据处理瓶颈问题日益严重  
- 📅 调查于 2025 年 5 月 27 日由 Sarah Gooding 报道  
- 🏛️ 联邦政府正式介入调查 NIST 的管理情况

---

### [我们测试了 7 种语言在极端负载下的表现，只有一种没有崩溃（结果出乎意料） | CodeStories - Freedium](https://freedium.cfd/https://medium.com/@codeperfect/we-tested-7-languages-under-extreme-load-and-only-one-didnt-crash-it-wasn-t-what-we-expected-67f84c79dc34)

**原文标题**: [We Tested 7 Languages Under Extreme Load and Only One Didn't Crash (It Wasn't What We Expected) | by CodeStories - Freedium](https://freedium.cfd/https://medium.com/@codeperfect/we-tested-7-languages-under-extreme-load-and-only-one-didnt-crash-it-wasn-t-what-we-expected-67f84c79dc34)

概述总结  
Freedium 更新了捐赠选项，新增多个平台支持其使命；同时，一篇关于编程语言在极端负载下表现的测试文章显示，Erlang 在七种语言中展现出惊人的稳定性。  

- 💌 Freedium 新增 Patreon、Ko-fi 和 Liberapay 捐赠渠道，支持用户以更灵活的方式贡献  
- 🏆 在极端负载测试中，Erlang 是唯一未崩溃的语言，其架构设计（如“let it crash”哲学和监管树）是关键  
- ⚙️ 测试环境：16 台高性能服务器，五种极端工作负载（并发连接、内存压力、CPU 饱和、I/O 轰炸、错误模拟）  
- 🚀 各语言表现：  
  - **Go**：高并发优秀，但内存压力下 GC 延迟导致不稳定  
  - **Rust**：内存安全高效，但错误级联引发死锁  
  - **C++**：性能最强，但内存管理问题导致崩溃  
  - **Java**：JVM 成熟，但 GC 停顿时间过长  
  - **Python**：异步改进显著，但 GIL 和内存问题成瓶颈  
  - **Node.js**：I/O 处理优异，但内存压力阻塞事件循环  
- 📌 关键结论：  
  - 架构（如隔离和自动恢复）比单纯性能更重要  
  - 内存管理是极限负载下的主要瓶颈  
  - 并发模型和容错能力对系统可靠性至关重要  
- 🔧 实践建议：设计需考虑故障隔离、监管层级和资源管理，而非仅依赖语言性能

---

