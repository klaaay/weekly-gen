### [Node 周刊第 586 期：2025 年 7 月 15 日](https://nodeweekly.com/issues/586)

**原文标题**: [Node Weekly Issue 586: July 15, 2025](https://nodeweekly.com/issues/586)

Node.js 最新动态与技术生态更新速览  

- 🚀 **Node v24.4.0 发布**：新增 `--watch-kill-signal` 参数支持，改进 `spawn` 权限标志传递，并包含 V8 和依赖项更新。  
- 🔒 **安全更新预告**：Node 团队即将发布 v24.x、22.x 和 20.x 版本的安全补丁，建议关注。  
- 📅 **年度大版本提案**：社区讨论是否将 Node.js 改为每年发布主版本，并缩短偶数版本 LTS 支持周期至 24 个月。  
- 🐳 **Docker 部署指南**：深入教程涵盖容器构建、Node 应用优化及 Docker Compose/Kubernetes 实践。  
- 💡 **TypeScript 5.9 Beta**：引入 `import defer` 支持，新增 `node20` 模式，未来将推出 Go 原生端口（TypeScript 7）。  
- 📦 **生态简讯**：  
  - Ubuntu Pro 延长 Node.js v18 支持至 2032 年。  
  - React Native 新增 Node-API 支持，提升跨平台原生代码共享能力。  
  - 朝鲜黑客组织发布 67 个恶意 npm 包，安全分析公开。  
- ⚡ **性能对比**：Node 版本管理器选择可能影响 shell 启动速度高达 500 倍，但实际场景影响有限。  
- 🔧 **工具更新**：  
  - **Necord**：基于 Nest 和 Discord.js 的机器人框架。  
  - **Envalid 8.1**：环境变量验证库时隔两年更新。  
  - **cRonstrue 3.0**：支持 30 种语言的 Cron 表达式自然语言转换。  
- 🌐 **其他亮点**：  
  - JavaScript `Date` 解析陷阱测验引发热议。  
  - Bun 处理 10 亿行文件挑战成绩突破 10 秒。  
  - Nginx 的 JavaScript 模块 `njs` 升级至 ES2023 支持。  

（注：文末推广内容未纳入摘要）

---

### [Node.js — Node v24.4.0（当前版本）](https://nodejs.org/en/blog/release/v24.4.0)

**原文标题**: [Node.js — Node v24.4.0 (Current)](https://nodejs.org/en/blog/release/v24.4.0)

Node.js v24.4.0（Current）版本发布，包含多项功能更新、错误修复及依赖项升级。

- 🔄 **crypto 模块**：支持 XOF 函数的`outputLength`选项（Aditi 贡献）  
- 📜 **文档更新**：添加所有 watch 模式相关标志至 node.1 手册（Dario Piotrowicz）  
- 📂 **fs 模块**：新增一次性`mkdtempSync`方法（Kevin Gibbons）  
- 🔒 **权限模型**：在`spawn`时传播权限标志（Rafael Gonzaga）  
- 🗃️ **SQLite 支持**：连接级别新增`readBigInts`选项（Miguel Marcondes Filho）  
- 🛠️ **权限 API 扩展**：支持`permission.has(addon)`检查（Rafael Gonzaga）  
- 🚦 **watch 模式**：新增`--watch-kill-signal`终止信号标志（Dario Piotrowicz）  
- 🐞 **错误修复**：修复 DNS 解析内存泄漏、SHAKE 算法兼容性等问题  
- ⬆️ **依赖升级**：更新 SQLite 至 3.50.2、Undici 至 7.11.0 等  
- 📦 **多平台支持**：提供 Windows/macOS/Linux 等系统安装包及源码

---

### [命令行 API | Node.js v24.4.0 文档](https://nodejs.org/api/cli.html#--watch)

**原文标题**: [Command-line API | Node.js v24.4.0 Documentation](https://nodejs.org/api/cli.html#--watch)

Node.js 命令行选项和环境变量文档概述

- 📜 文档详细介绍了 Node.js 的命令行选项和环境变量配置。
- 🔧 命令行选项包括调试、性能分析、模块加载、权限控制等多种功能。
- 🌐 环境变量部分涵盖了如何通过环境变量配置 Node.js 的行为，如调试、模块路径、TLS 设置等。
- ⚙️ 提供了多种性能分析选项，如 CPU 和堆分析，帮助开发者优化应用性能。
- 🔒 安全相关选项包括 FIPS 模式、权限模型等，确保应用的安全性。
- 🛠️ 包含实验性功能的选项，如 WebAssembly、ShadowRealm 等，供开发者尝试新特性。
- 📊 测试相关选项支持测试覆盖率、测试隔离等，便于开发者进行测试和调试。
- 🔄 监视模式选项允许开发者在文件变化时自动重启应用，提升开发效率。

---

### [Node.js — 2025 年 7 月 15 日星期二安全发布](https://nodejs.org/en/blog/vulnerability/july-2025-security-releases)

**原文标题**: [Node.js — Tuesday, July 15, 2025 Security Releases](https://nodejs.org/en/blog/vulnerability/july-2025-security-releases)

Node.js 项目将于 2025 年 7 月 15 日或之后发布 24.x、22.x 和 20.x 版本的安全更新，以修复多个高严重性问题。

- 🔥 **高严重性问题**：24.x 版本存在 2 个高严重性问题，22.x 和 20.x 版本各存在 1 个。
- ⚠️ **影响范围**：生命周期结束的版本同样会受到影响。
- 🛡️ **安全建议**：建议用户更新至最新版本以确保系统安全。
- 📅 **发布时间**：安全更新将于 2025 年 7 月 15 日或之后发布。
- 📧 **联系方式**：可通过 Node.js 安全政策页面和 GitHub 流程报告漏洞。
- 📬 **订阅更新**：建议订阅 nodejs-sec 邮件列表以获取安全漏洞和发布的最新信息。

---

### [提案 - 将 Node.js 改为年度主版本发布并缩短 LTS 周期 · Issue #1113 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1113)

**原文标题**: [Proposal - Shift Node.js to Annual Major Releases and Shorten LTS Duration · Issue #1113 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1113)

Node.js 提议从双年度主版本发布周期改为年度主版本发布，并缩短长期支持（LTS）时长，以减轻维护压力并提升稳定性。  

- 🚀 **背景**：当前双年度发布导致维护负担重、版本管理复杂，社区反馈希望简化发布周期。  
- 📅 **提议变更**：改为每年一次主版本发布，LTS 时长从 30 个月缩短至 24 个月（12 个月活跃支持 + 12 个月维护支持）。  
- ✅ **优点**：降低维护复杂度，提供更清晰的版本支持路线，提升稳定性。  
- ❌ **缺点**：新功能发布频率可能降低，LTS 缩短可能引发部分社区不满。  
- 📢 **实施策略**：需 TSC 和发布工作组达成共识，更新文档并加强社区沟通。  
- 🔍 **下一步**：细化提案、收集反馈，制定过渡计划并同步生态。

---

### [TypeScript 5.9 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/#support-for---module-node20)

**原文标题**: [Announcing TypeScript 5.9 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/#support-for---module-node20)

TypeScript 5.9 Beta 发布，带来多项新功能和优化，包括更简洁的 `tsconfig.json` 初始化、支持 `import defer` 语法、新增 `--module node20` 选项、DOM API 摘要描述、可扩展的悬停预览以及性能优化。

- 🚀 **TypeScript 5.9 Beta 发布** - 可通过 `npm install -D typescript@beta` 安装体验新功能。
- 🛠️ **更简洁的 `tsconfig.json` 初始化** - `tsc --init` 生成的配置文件更精简，默认启用常用选项（如 `strict`、`jsx` 等），减少手动调整。
- ⏳ **支持 `import defer` 语法** - 延迟模块执行，直到首次访问模块成员，适用于条件加载或优化启动性能。
- 📦 **新增 `--module node20` 选项** - 稳定支持 Node.js v20 的模块行为，默认目标为 `es2023`。
- 📚 **DOM API 摘要描述** - 悬停提示中显示 API 的简要说明，提升开发体验。
- 🔍 **可扩展的悬停预览（预览功能）** - 在 VS Code 中支持展开/折叠类型详细信息，无需跳转到定义。
- 📏 **可配置悬停长度** - 通过 `js/ts.hover.maximumLength` 设置调整悬停提示的最大长度，默认值更大。
- ⚡ **性能优化** - 缓存类型实例化减少重复计算，优化文件存在检查逻辑，提升编译速度。
- 🌟 **后续计划** - 团队正专注于 TypeScript 原生版本（TypeScript 7）的开发，鼓励用户试用 Beta 或每日构建版本并提供反馈。

---

### [TypeScript 5.9 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/#support-for-import-defer)

**原文标题**: [Announcing TypeScript 5.9 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/#support-for-import-defer)

TypeScript 5.9 Beta 版本发布，带来多项新功能和优化，包括更简洁的 `tsconfig.json` 初始化、支持 `import defer` 语法、新增 `--module node20` 选项、DOM API 摘要描述、可扩展的悬停预览以及性能优化。

- 🚀 **TypeScript 5.9 Beta 发布**：可通过 `npm install -D typescript@beta` 安装体验新功能。  
- 🛠️ **简化的 `tsconfig.json` 初始化**：`tsc --init` 生成的配置文件更精简，默认启用常用选项（如 `strict`、`jsx` 等），减少手动调整。  
- ⏳ **支持 `import defer`**：延迟模块执行，仅在首次访问时触发，适用于条件加载或优化启动性能。仅支持命名空间导入（`import defer * as module`）。  
- 📦 **新增 `--module node20`**：稳定支持 Node.js v20 的模块行为，默认目标为 `es2023`，区别于动态更新的 `nodenext`。  
- 📚 **DOM API 摘要描述**：在悬停提示中直接显示 API 功能摘要，提升开发效率。  
- 🔍 **可扩展悬停预览（实验性）**：在 VS Code 中通过 `+/-` 按钮展开或折叠类型详细信息，无需跳转定义。  
- 📏 **可配置悬停长度**：通过 `js/ts.hover.maximumLength` 设置悬停提示的最大显示内容，默认值更大。  
- ⚡ **性能优化**：缓存类型实例化减少重复计算，优化文件存在检查逻辑，提升大型项目编译速度。  
- 🔜 **后续计划**：团队正专注于 TypeScript 原生版本（TypeScript 7）的开发，同时欢迎用户试用 5.9 Beta 并提供反馈。  

（注：部分功能如 `import defer` 需运行时或工具原生支持，仅适用于 `--module preserve` 或 `esnext` 模式。）

---

### [TypeScript 5.9 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/#support-for---module-node20)

**原文标题**: [Announcing TypeScript 5.9 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/#support-for---module-node20)

TypeScript 5.9 Beta 版本发布，包含多项新功能和优化，旨在提升开发体验和性能。

- 🚀 **TypeScript 5.9 Beta 发布**：可通过 `npm install -D typescript@beta` 安装测试版。  
- 🛠️ **精简的 `tsc --init` 配置**：生成的 `tsconfig.json` 更简洁，默认启用常用选项（如 `strict`、`jsx` 等），减少手动调整。  
- ⏳ **支持 `import defer`**：延迟模块执行，首次访问时再触发副作用，适用于条件加载或性能优化。  
- 📦 **新增 `--module node20`**：稳定支持 Node.js v20 的模块行为，默认目标为 `es2023`。  
- 📚 **DOM API 摘要描述**：在工具提示中直接显示 API 功能摘要，减少跳转文档频率。  
- 🔍 **可扩展悬停预览（实验性）**：在 VS Code 中展开悬停信息，查看深层类型定义。  
- 📏 **可配置悬停信息长度**：通过 `js/ts.hover.maximumLength` 调整显示内容的详细程度。  
- ⚡ **性能优化**：缓存类型实例化减少重复计算，优化文件存在检查逻辑（提速约 11%）。  
- 🌟 **后续计划**：继续开发 TypeScript 5.9 并收集反馈，同时推进原生版本（TypeScript 7）的预览。  

开发者可通过夜间构建版或 VS Code 插件提前体验新功能。

---

### [添加 `--module node20` by andrewbranch · Pull Request #61805 · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/pull/61805)

**原文标题**: [Add `--module node20` by andrewbranch · Pull Request #61805 · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/pull/61805)

Microsoft TypeScript 仓库中关于添加 `--module node20` 的 PR 讨论和合并记录。

- 🚀 新增 `--module node20` 作为 `nodenext` 的别名，区别在于 `node20` 默认使用 `--target es2023`，而 `nodenext` 使用 `--target esnext`。  
- 🔧 修复了 `require(esm)` 对 `module.exports` 的互操作支持问题。  
- 📦 `node20` 和 `nodenext` 现在默认启用 `resolveJsonModule`，后续会回溯到 `node16` 和 `node18`。  
- 📊 更新了 Node.js 模块选项表，详细说明了不同模块选项的配置和功能差异。  
- ✅ 通过了大量测试验证，确保与 `node18` 和 `nodenext` 的兼容性。  
- 🤖 Copilot AI 参与了代码审查，确认了 523 个文件的修改无误。  
- 🔄 PR 最终被合并到主分支，并关闭了相关 issue。

---

### [10 倍速的 TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

**原文标题**: [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScript 团队宣布将推出原生版本编译器，性能提升高达 10 倍，显著减少编辑器启动和构建时间，并降低内存占用。预计 2025 年中发布预览版，年底完成功能支持。

- 🚀 TypeScript 原生编译器性能提升 10 倍，大幅优化编辑器启动和构建时间  
- 💡 原生版本预计 2025 年中发布预览版，年底实现完整功能支持  
- ⚡ 测试显示多个流行代码库构建速度提升 9-13 倍  
- 📉 内存占用减少约一半，未来可能进一步优化  
- 🔧 将迁移至语言服务器协议 (LSP)，提升与其他语言的兼容性  
- 🛠️ TypeScript 6.x 将继续维护，原生版本将作为 TypeScript 7.0 发布  
- 🤖 性能提升为 AI 工具提供更强大的开发支持  
- 💻 编辑器加载速度提升 8 倍，操作响应更迅捷  
- 📅 团队将在 GitHub 定期更新进展，并举办 AMA 答疑

---

### [NodeJS 18 LTS 在 Ubuntu 上的支持终止期从 2025 年 4 月延长至 2032 年 5 月 | Ubuntu](https://ubuntu.com/blog/nodejs-18-lts-eol-extended-from-april-2025-to-may-2032-on-ubuntu)

**原文标题**: [NodeJS 18 LTS EOL extended from April 2025 to May 2032 on Ubuntu | Ubuntu](https://ubuntu.com/blog/nodejs-18-lts-eol-extended-from-april-2025-to-may-2032-on-ubuntu)

NodeJS 18 LTS 的 EOL 从 2025 年 4 月延长至 2032 年 5 月，适用于 Ubuntu Pro 用户。

- 🕒 Node.js 18 最初的上游 EOL 日期为 2025 年 4 月 30 日，现通过 Ubuntu Pro 延长至 2032 年 5 月。  
- 🛡️ Ubuntu Pro 提供长达 12 年的开源软件安全补丁，覆盖 Node.js 18 等版本，超越上游维护周期。  
- 🔒 包含 FIPS 兼容的 Node.js 二进制文件，满足高合规性需求（如金融、医疗行业）。  
- 💡 免费方案支持：个人或商业评估可免费绑定 5 个 Ubuntu LTS 实例，获取安全更新。  
- ⚙️ 多种安装方式（snap、deb、NVM 等），但仅 Canonical 提供的 deb 包享受 12 年安全承诺。  
- 🌍 适用于长期项目：解决技术债务问题，避免因政府法规禁止使用 EOL 软件的风险。  
- 📅 Node.js 22 LTS 未纳入 Ubuntu 24.04 LTS，因其发布时间晚于 Ubuntu 功能冻结日期。  
- 🎤 开发者可参与 2025 年 Ubuntu Summit 展示作品，活动支持远程互动。  
- 🔄 软件发布者与用户目标冲突：Ubuntu Pro 平衡双方需求，提供稳定与长期安全支持。

---

### [宣布 React Native 支持 Node-API](https://www.callstack.com/blog/announcing-node-api-support-for-react-native)

**原文标题**: [Announcing Node-API Support for React Native](https://www.callstack.com/blog/announcing-node-api-support-for-react-native)

React Native 宣布支持 Node-API，这是一个跨平台的本地模块系统，旨在简化开发流程并提升生态系统互操作性。

- 🚀 **Node-API 引入 React Native**：社区合作将 Node.js 的本地模块系统 Node-API 引入 React Native，提供运行时无关的稳定接口。  
- 🔧 **跨平台与多语言支持**：支持多种编程语言（如 C++、Rust、Swift 等），并兼容 Node.js、Deno、Bun 等运行时，便于代码复用。  
- ⏱️ **预构建优化构建时间**：通过预构建本地模块，显著减少应用构建时间（Android 可缩短至 7 秒），当前 React Native 正推进 JSI 的 ABI 稳定性（计划于 0.81 版本）。  
- 🌐 **生态系统共享**：利用 Node-API 现有生态（如 WebRTC、Web Audio 等），促进 Web 与 React Native 的代码共享，Hermes 团队也计划采用其实现 Temporal 和 Intl。  
- 🛠️ **适用场景**：适合跨平台共享代码（如数据库、同步引擎）、高性能计算（AI 推理、加密）或调用平台 API（Apple SDK/Android NDK）。  
- 📦 **工具链支持**：提供 `cmake-rn`、`gyp-to-cmake` 和 `ferric` 等工具，支持 C++、Rust 等语言的模块构建。  
- ⚠️ **当前限制**：需使用特定 React Native 版本（0.79.1/0.79.2）并手动构建 Hermes，待官方合并 Node-API 支持后解除。  
- 🤝 **社区协作**：感谢 Microsoft、NativeScript、MongoDB 等团队贡献，呼吁开发者参与测试、构建模块或解决 [Good First Issues](https://github.com/callstackincubator/react-native-node-api)。  
- 🔮 **未来展望**：扩展对更多平台（如 Windows/macOS）的支持，推动 React Native 模块开发的标准化与高效化。  

示例仓库：[node-api-example-lib](https://github.com/callstackincubator/node-api-example-lib)

---

### [2025 年 5 月 TC39 全体会议摘要](https://blogs.igalia.com/compilers/2025/07/03/summary-of-the-may-2025-tc39-plenary/)

**原文标题**: [Summary of the May 2025 TC39 plenary](https://blogs.igalia.com/compilers/2025/07/03/summary-of-the-may-2025-tc39-plenary/)

2025 年 5 月 TC39 全会总结：会议在 Igalia 总部举办，聚焦 JavaScript 新特性进展，包括多个提案进入 Stage 4 及以下阶段，并探讨了语言设计与国际化功能的未来方向。

- 🎉 **会议概况**：Igalia 在西班牙 A Coruña 主办本次会议，感谢各方参与并期待再次合作。
- 🚀 **Stage 4 提案**：
  - `Array.fromAsync`：异步迭代器转数组，满足开发者需求，进入 Stage 4。
  - `Explicit Resource Management`：通过`using`声明实现资源自动释放，Chrome 等已支持。
  - `Error.isError`：可靠检测 Error 实例，结束多年讨论。
  - `Intl.Locale#variants`：补充 Locale 对象中变体信息的访问支持。
- 🔍 **Stage 3 更新**：
  - `Intl.Locale Info`：查询本地化元数据，调整文本方向未知时的返回值为`undefined`。
  - `Temporal`：Firefox 已支持，调整 UTC 偏移秒数的解析逻辑。
  - `Immutable ArrayBuffer`：测试计划完善，待测试完成后推进。
- ⚙️ **Stage 2.7 及以下进展**：
  - `Iterator Sequencing`：`Iterator.concat`方法因对象复用问题暂缓。
  - `Iterator Chunking`：分块方法`chunks`和`windows`行为调整，拆分为两个方法。
  - `AsyncContext`：异步上下文传播讨论持续，需解决浏览器实现复杂性。
- 📊 **新提案推进**：
  - `Math.clamp`（现`Number.prototype.clamp`）：数值范围限制方法进入 Stage 2。
  - `Seeded PRNG`：支持种子的随机数生成器进入 Stage 2。
  - `More random functions`：扩展随机数工具函数集进入 Stage 1。
  - `Keep trailing zeros`：国际化 API 保留数字末尾零进入 Stage 1。
- 💡 **其他讨论**：
  - `Decimal`：十进制数与精度包装类的集成探讨。
  - `Comparisons`：标准化断言函数进入 Stage 1 调研。
  - `IDL for ECMAScript`：探索在 ECMAScript 规范中使用 IDL 降低维护成本。
- 🌍 **社区活动**：会后举办本地技术社区交流，促进开发者互动。

---

### [传染性面试活动升级，涉及 67 个恶意 np...](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)

**原文标题**: [Contagious Interview Campaign Escalates With 67 Malicious np...](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)

研究发现 8 个恶意 Firefox 扩展，伪装成热门游戏，窃取用户数据并滥用浏览器权限。  

- 🎮 伪装游戏：恶意扩展冒充热门游戏，诱导用户安装。  
- 🔒 窃取凭证：通过 OAuth 令牌窃取用户登录信息。  
- 🌐 会话劫持：攻击者利用扩展劫持用户浏览器会话。  
- 👁️ 监控行为：滥用浏览器权限，暗中监视用户活动。  
- ⚠️ 安全风险：这些扩展对用户隐私和数据安全构成严重威胁。

---

### [Node.js 版本管理器间的 500 倍性能差距（以及为何你可能无需在意）](https://nodevibe.substack.com/p/the-500x-performance-gap-between)

**原文标题**: [The 500x performance gap between Node.js version managers (and why you might not care)](https://nodevibe.substack.com/p/the-500x-performance-gap-between)

Node.js 版本管理器在性能上存在高达 500 倍的差距，但具体影响取决于使用场景。

- 🚀 **性能差距显著**：NVM 在冷启动时耗时 508ms，而 Volta 仅需 1ms，差距达 500 倍。  
- 🏎️ **工具架构决定速度**：NVM 基于 Shell 脚本，而 FNM 和 Volta 是 Rust 编译的二进制工具，启动更快。  
- 💻 **使用场景影响体验**：频繁启动新 Shell（如 CI/CD、IDE 终端）时 NVM 明显拖慢速度，长期运行的 Shell 则影响较小。  
- ⏱️ **实际工作流耗时**：模拟开发流程中，NVM 总耗时 4 秒，Volta 仅 200ms，频繁操作节省数分钟。  
- 🔧 **Shell 环境差异**：Zsh 下 NVM 性能下降更明显（比 Bash 慢 270 倍），因 Zsh 初始化更复杂。  
- 🔄 **版本切换速度**：NVM 需 200ms 以上，而 Volta/FNM 仅需个位数毫秒，体验接近“瞬时”。  
- 📊 **迁移建议**：若追求性能，可换用 Volta 或 FNM，安装简单且支持自动版本切换。  
- ⚖️ **权衡选择**：若现有工作流满意，性能差距可忽略；若频繁启动 Shell，切换工具提升显著。  
- 🔍 **测试详情公开**：提供完整测试套件（GitHub），鼓励用户自行验证不同平台结果。  

（总结：性能差距真实存在，但是否值得切换取决于个人工作习惯和场景需求。）

---

### [JavaScript 作用域提升存在问题](https://devongovett.me/blog/scope-hoisting.html)

**原文标题**: [JavaScript scope hoisting is broken](https://devongovett.me/blog/scope-hoisting.html)

现代 JavaScript 打包工具中的"作用域提升"优化存在根本性问题，尤其在代码分割场景下会导致模块执行顺序错误和`this`绑定异常等缺陷。

- 🌀 作用域提升原理：将模块代码直接内联到单一作用域，取代传统的函数包裹模块方式，由 Rollup 首创并被主流打包器采用  
- 📦 传统模块打包：每个模块被函数包裹，通过`require`和`exports`对象交互，增加体积和运行时开销  
- ⚡ 代码分割冲突：作用域提升与多入口/动态导入场景下的公共依赖提取存在根本性矛盾  
- 🔀 执行顺序错乱：共享模块中的副作用代码（如 console.log）在拆分后执行顺序可能改变程序行为  
- 🛠️ 现有解决方案：Parcel 将共享模块包裹为函数并按需调用，Webpack 采用模块串联进行部分作用域提升  
- 🚨 其他问题：作用域提升会破坏导出函数的`this`绑定，特别是涉及重新导出时  
- 📉 优化收益有限：实测显示仅不到 5% 的模块能真正受益，多数仍需函数包裹  
- ⚖️ 权衡考量：现代工具已能独立实现摇树优化，作用域提升对运行时性能的影响需重新评估  
- 🔮 未来方向：作者考虑在 Parcel v3 中默认采用函数包裹模块，放弃作用域提升以提升正确性

---

### [包裹](https://parceljs.org/)

**原文标题**: [Parcel](https://parceljs.org/)

Parcel 是一款零配置、高性能的现代前端构建工具，专注于提升开发体验与生产效率，支持多语言、多文件类型及自动化优化。

- 🚀 **零配置开箱即用**：无需复杂配置，直接支持 HTML、CSS、JavaScript、TypeScript、SASS 等文件类型，自动安装所需插件。  
- 🔥 **内置开发服务器**：一键启动本地服务（含 HTTPS 支持），集成热重载（React/Vue 友好）和 API 代理功能。  
- 🐞 **友好错误诊断**：高亮显示代码错误位置，提供修复建议及文档链接。  
- ⚡ **极致构建速度**：基于 Rust 的并行编译（10-100 倍提速），多核优化，智能缓存避免重复构建。  
- 🌳 **自动生产优化**：支持 Tree Shaking（跨语言）、代码压缩、图片优化（格式/尺寸转换）、代码拆分（CSS/JS 并行加载）等。  
- 🌐 **多环境适配**：自动根据 `browserslist` 转译代码，支持差分打包（现代/旧版浏览器），原生兼容 Web Workers。  
- 📦 **库与多包构建**：一键生成 ES/CommonJS/TS 类型声明，支持 monorepo 项目批量打包。  
- 🔧 **灵活扩展**：通过 `.parcelrc` 简单配置或插件体系（转换器/解析器等）定制构建流程，插件支持热重载调试。  
- 🤖 **API 集成**：提供编程接口嵌入现有工具链，统一诊断格式便于问题追踪。  
- ❤️ **开源驱动**：由社区赞助与贡献维护，提供多层级赞助方案。

---

### [作用域提升](https://parceljs.org/features/scope-hoisting/)

**原文标题**: [
      Scope hoisting
    ](https://parceljs.org/features/scope-hoisting/)

JavaScript 打包工具 Parcel 通过作用域提升（Scope Hoisting）技术优化模块打包，减少代码体积并提升运行时性能。

- 🚀 作用域提升：Parcel 将模块合并到单一作用域，减少函数包裹，优化代码压缩和运行效率。
- 🌳 摇树优化（Tree Shaking）：静态分析模块导入导出，移除未使用代码，支持 ES 模块、CommonJS 等。
- 🔍 静态分析：Parcel 独立并行分析模块，重命名变量确保唯一性，移除未使用导出。
- ⚠️ 避免跳出（Bail Outs）：遇到无法静态分析的代码时，Parcel 会包裹模块以保留副作用。
- 🔗 动态成员访问：静态解析已知属性访问，动态属性访问需保留所有导出。
- 🔄 动态导入：支持静态属性访问或解构的摇树优化，动态访问需保留所有导出。
- 📦 CommonJS 支持：静态赋值可优化，动态赋值需保留所有导出。
- 🚫 避免使用 eval：eval 会阻止变量重命名和最小化。
- ↩️ 避免顶层 return：CommonJS 中顶层 return 会禁用摇树优化。
- 🔄 避免 module 和 exports 重赋值：重赋值会禁用静态分析和摇树优化。
- ⏱️ 避免条件 require：条件 require 会导致模块包裹，影响性能。
- 💊 副作用：通过 package.json 的 sideEffects 字段标记无副作用文件，优化打包。
- ✨ PURE 注释：标记无副作用函数调用，优化未使用代码的移除。

---

### [JavaScript 中使用 Array.fromAsync() 实现现代异步迭代 - Matt Smith](https://allthingssmitty.com/2025/07/14/modern-async-iteration-in-javascript-with-array-fromasync/)

**原文标题**: [
    Modern async iteration in JavaScript with Array.fromAsync() - Matt Smith
  ](https://allthingssmitty.com/2025/07/14/modern-async-iteration-in-javascript-with-array-fromasync/)

JavaScript 中通过 Array.fromAsync() 实现现代异步迭代

- 🚀 `Array.fromAsync()` 是 ES2024 新增方法，用于将异步/同步可迭代对象转为数组  
- 🔧 语法：`Array.fromAsync(source[, mapFn[, thisArg]])`，返回`Promise<Array>`  
- 💡 核心优势：替代手动`for await...of`循环，支持异步映射函数  
- 🌟 典型应用场景：  
  - 📡 异步 API 数据转换（如分页数据聚合）  
  - 🌊 流数据处理（Web Streams API）  
  - 🔄 异步生成器转数组  
- ⚠️ 注意事项：输入必须是可迭代对象，单独 Promise 会抛出 TypeError  
- 🛠️ 错误处理：自动传播迭代/映射过程中的同步/异步错误  
- 📊 与传统方案对比：  
  - 比手动收集数组代码更简洁  
  - 比`Promise.all`更适合处理迭代器场景  
- 🌐 兼容性：现代浏览器（Chrome121+/Firefox115+）和 Node.js22+ 原生支持  
- 📦 备用方案：提供了简易 polyfill 实现  
- 🆚 与`Array.from()`关键区别：  
  - 支持异步可迭代对象  
  - 返回 Promise  
  - 允许异步映射函数

---

### [类型化查询构建器：Kysely 对比 Drizzle](https://marmelab.com/blog/2025/06/26/kysely-vs-drizzle.html)

**原文标题**: [Typed Query Builders: Kysely vs. Drizzle](https://marmelab.com/blog/2025/06/26/kysely-vs-drizzle.html)

概述：本文比较了两种 TypeScript 数据库查询构建工具 Kysely 和 Drizzle，重点从开发体验（DX）角度分析了它们的模式生成、查询和迁移功能。通过一个简化的电子商务模式示例，作者展示了两种工具在实际应用中的表现，并最终根据项目需求选择了 Kysely。

- 🏠 文章介绍了 Marmelab 团队为提高开发体验，对 Kysely 和 Drizzle 两种类型化查询构建工具进行比较的过程。
- 🛒 测试使用了一个简化的电子商务模式，包含 Categories、Products、Customers、Orders 和 OrderItems 等表。
- 🔍 比较的两个工具：Kysely（类似增强版 Knex.js，强类型支持）和 Drizzle（轻量级、SQL 优先的类型安全 ORM）。
- 📝 Kysely 使用社区工具 kysely-codegen 生成模式，而 Drizzle 使用自带的 drizzle-kit 工具生成更复杂的模式和相关文件。
- 🔎 查询方面，Kysely 提供流畅的 API 和强大的类型推断，支持嵌套结构；Drizzle 语法更 SQL-like，但在处理嵌套数组时需要更多手动操作。
- 🚀 迁移方面，Kysely 提供简单灵活的手动迁移方式；Drizzle 提供更全面的迁移工具集，支持多种工作流程。
- ⚖️ 结论：Kysely 在查询构建和类型支持上更优，适合已有 Knex.js 项目；Drizzle 在 ORM 功能和迁移工具上更强，适合新项目。
- 💡 建议根据项目现有架构、团队专长和具体技术需求选择工具，而非盲目追随潮流。

---

### [NECORD - 使用 NestJS 创建 Discord 机器人的最佳方式](https://necord.org/)

**原文标题**: [NECORD - The best way to create Discord bots with NestJS](https://necord.org/)

Necord 是一个结合了 Discord.js 和 NestJS 的模块，旨在快速、简便地创建 Discord 机器人，并深度集成到 NestJS 应用中。

- 🚀 **最佳工具结合**：利用 Discord.js 的强大功能和 NestJS 的渐进式框架，创建结构良好的 Discord 机器人应用。  
- 📦 **简单安装**：通过 npm 安装 necord 和 discord.js 即可开始使用。  
- 💡 **示例代码**：提供清晰的代码示例，展示如何监听 Discord 机器人的“ready”事件并记录日志。  
- 🌍 **多语言支持**：文档支持多种语言，包括英语、俄语和葡萄牙语（巴西）。  
- 🤝 **社区支持**：拥有活跃的社区，提供 Discord 频道、GitHub 组织和 NPM 组织等资源。  
- ❤️ **赞助与贡献**：鼓励用户通过捐赠、贡献代码或翻译文档来支持项目发展。

---

### [获取失败](https://nodeweekly.com/link/171748/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/171748/web)

无法总结：获取内容失败，状态码 429。

---

### [GitHub - necordjs/necord: 🤖 基于 Discord.js 的 NestJS 模块，用于创建 Discord 机器人](https://github.com/necordjs/necord)

**原文标题**: [GitHub - necordjs/necord: 🤖 A module for creating Discord bots using NestJS, based on Discord.js](https://github.com/necordjs/necord)

Necord 是一个基于 NestJS 和 Discord.js 的模块，用于快速创建功能强大的 Discord 机器人，支持 NestJS 的各种特性如守卫、拦截器等。

- 🤖 基于 Discord.js 和 NestJS，提供高效、易用的 Discord 机器人开发方案  
- 📚 支持自定义装饰器、Slash 命令、上下文菜单、消息组件等 Discord 交互功能  
- 🛠️ 完全兼容 NestJS 的守卫（Guards）、拦截器（Interceptors）、过滤器（Filters）和管道（Pipes）  
- 📦 安装简单，支持 npm、yarn 和 pnpm：`npm i necord discord.js`  
- 🚀 提供丰富的文档和社区支持，包括官方 Wiki 和示例代码  
- 🔧 使用示例：通过 `NecordModule.forRoot` 配置机器人令牌和意图，并通过装饰器处理事件  
- 📜 开源项目，采用 MIT 许可证，作者为 Alexey Filippov  
- 🌟 GitHub 上有 420 星和 17 个 fork，活跃维护中

---

### [优票](https://upyo.org/)

**原文标题**: [Upyo](https://upyo.org/)

跨运行时兼容，提供一致的 API 体验  

- 🌐 支持 Node.js、Deno、Bun 及边缘函数  
- 🔄 跨平台无缝运行  
- 🛠️ 保持 API 一致性

---

### [在真实 iOS 设备上运行 Playwright 测试 | BrowserStack 文档](https://www.browserstack.com/docs/automate/playwright/playwright-ios?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=new-launches-updates&utm_campaign=PR-12-Jun-2025-iOS-Playwright&utm_campaigncode=701OW00000NyIRcYAN&utm_term=nodeweekly2)

**原文标题**: [Run Playwright tests on real iOS devices | BrowserStack Docs](https://www.browserstack.com/docs/automate/playwright/playwright-ios?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=new-launches-updates&utm_campaign=PR-12-Jun-2025-iOS-Playwright&utm_campaigncode=701OW00000NyIRcYAN&utm_term=nodeweekly2)

BrowserStack 推出 Playwright 测试支持真实 iOS 设备的功能，帮助开发者更高效地进行移动端测试。

- 🚀 **Playwright 支持 iOS 测试**：现可在 BrowserStack 上运行 Playwright 测试，覆盖 100 多种 iPhone 和 iPad 设备及浏览器组合。
- 🔍 **真实设备测试**：避免移动模拟器可能遗漏的 Safari 特定问题，确保测试准确性。
- ⚙️ **简单集成**：支持现有 CI 流水线，并提供测试日志和调试工具。
- 📋 **快速开始指南**：提供详细的步骤说明，包括克隆示例仓库、安装依赖和配置设备参数。
- 📊 **测试结果查看**：可通过 BrowserStack Automate 仪表板查看测试结果，便于分析和优化。
- 📱 **设备配置灵活**：支持动态调整测试配置，适应不同设备和操作系统版本。
- ❌ **不支持的功能**：部分功能如 playwrightLogs、consoleLogs 等在 iOS 测试中暂不支持。
- 📞 **技术支持**：提供支持团队联系方式，帮助解决测试中的问题。

---

### [GitHub - jhnns/rewire: Node.js 单元测试的简便猴子补丁工具](https://github.com/jhnns/rewire)

**原文标题**: [GitHub - jhnns/rewire: Easy monkey-patching for node.js unit tests](https://github.com/jhnns/rewire)

rewire 是一个用于 Node.js 单元测试的工具，允许对模块进行猴子补丁（monkey-patching），便于注入模拟对象或修改私有变量。

- 🛠 **功能特点**：支持修改模块内的私有变量、注入其他模块或全局对象的模拟版本（如 `process`）。
- 📦 **安装**：通过 `npm install rewire` 安装。
- 🔧 **基本用法**：使用 `__set__` 和 `__get__` 方法修改和获取模块内的变量。
- 🔄 **还原修改**：`__set__` 返回一个函数，用于还原修改；`__with__` 方法在回调执行后自动还原。
- ⚠️ **限制**：不支持 Babel 的 ES 模块模拟、函数内部变量、导出原始值的模块，以及部分全局变量（如 `eval` 和全局对象本身）。
- 📜 **API**：提供 `rewire()`、`__set__`、`__get__` 和 `__with__` 等方法，用于模块的引入和变量操作。
- ⚠️ **注意事项**：每次调用 `rewire()` 会重新执行模块；全局变量在模块引入时被导入，后续修改无效。
- 📄 **许可证**：采用 MIT 许可证。

---

### [GitHub - af/envalid：适用于Node、Bun及其他兼容JS运行时的环境变量验证工具](https://github.com/af/envalid)

**原文标题**: [GitHub - af/envalid: Environment variable validation for Node, Bun, and other compatible JS runtimes](https://github.com/af/envalid)

Envalid 是一个用于验证和访问 Node.js 程序环境变量的小型库，旨在确保程序在满足所有环境依赖时运行，并提供环境变量的不可变 API。

- 🚀 **功能概述**：验证和清理环境变量，确保程序运行前环境依赖满足。
- 📜 **类型安全**：完全用 TypeScript 编写，支持类型推断。
- 🏗️ **模块化设计**：支持自定义验证器、中间件和报告器。
- 🔧 **API 核心**：`cleanEnv(environment, validators, options)` 返回清理后的不可变环境对象。
- 📌 **验证器类型**：包括 `str()`, `bool()`, `num()`, `email()`, `host()`, `port()`, `url()`, `json()` 等。
- 🛠️ **自定义验证器**：通过 `makeValidator()` 创建自定义验证逻辑。
- ⚠️ **错误报告**：默认在缺失或无效环境变量时退出，支持自定义报告器。
- 🔄 **中间件支持**：`customCleanEnv()` 允许自定义验证后处理逻辑。
- 🧪 **测试工具**：`testOnly` 助手用于测试环境下的默认值设置。
- 🔗 **相关项目**：可与 `dotenv`, `react-native-config`, `fastify-envalid` 等工具集成。
- 📖 **动机**：遵循 12-Factor 应用准则，管理环境配置。

---

### [发布 v8.1.0 · af/envalid · GitHub](https://github.com/af/envalid/releases/tag/v8.1.0)

**原文标题**: [Release v8.1.0 · af/envalid · GitHub](https://github.com/af/envalid/releases/tag/v8.1.0)

overview summary  
GitHub 仓库发布了 v8.1.0 稳定版本，包含新功能支持、问题修复及内部工具升级，感谢贡献者的努力。  

- 🆕 新增对"yes"和"no"作为布尔值的支持 (#224)  
- 🛠️ 新增条件必填字段功能，通过`requiredWhen`验证器选项实现 (#223)  
- 🐛 修复未提供默认值时开发环境下未捕获`EnvMissingError`的问题 (#225)  
- ⚙️ 内部改进：更新多个开发依赖包  
- 🚀 单元测试迁移至`vitest`，速度更快、配置更简单  
- ✨ 代码格式化和检查迁移至`biome`工具  
- 📅 版本发布时间：2022 年 7 月 12 日  
- 🔄 加载错误时提示用户重新刷新页面

---

### [GitHub - bradymholt/cRonstrue: 将 Cron 表达式转换为人类可读描述的 JavaScript 库](https://github.com/bradymholt/cRonstrue)

**原文标题**: [GitHub - bradymholt/cRonstrue: JavaScript library that translates Cron expressions into human readable descriptions](https://github.com/bradymholt/cRonstrue)

cRonstrue 是一个 JavaScript 库，用于将 Cron 表达式转换为人类可读的描述。它支持多种语言和复杂的 Cron 表达式，并提供了多种安装和使用方式。

- 🌟 **功能特点**：支持所有 Cron 表达式的特殊字符，包括 5、6 或 7 部分的表达式，支持 Quartz Job Scheduler 和多种语言。
- 🚀 **安装方式**：可以通过 npm、CDN 或直接引入脚本文件来安装和使用。
- 📖 **使用方法**：通过简单的 API 调用即可将 Cron 表达式转换为可读的描述，支持多种选项和国际化。
- 🌍 **国际化支持**：支持 30 多种语言，可以单独引入或一次性引入所有语言。
- ❓ **常见问题**：库不验证 Cron 表达式的有效性，建议先使用其他库进行验证。
- 📜 **许可证**：采用 MIT 许可证，可自由分发。

---

### [GitHub - bradymholt/cRonstrue: 将 Cron 表达式转换为人类可读描述的 JavaScript 库](https://github.com/bradymholt/cRonstrue#supported-locales)

**原文标题**: [GitHub - bradymholt/cRonstrue: JavaScript library that translates Cron expressions into human readable descriptions](https://github.com/bradymholt/cRonstrue#supported-locales)

cRonstrue 是一个 JavaScript 库，用于将 Cron 表达式转换为人类可读的描述。它支持多种语言和复杂的 Cron 表达式，适用于各种开发环境。

- 🌟 **功能特点**：支持所有 Cron 表达式的特殊字符，包括 5、6 或 7 部分的表达式，支持 Quartz Job Scheduler 和多种语言。
- 🚀 **安装方式**：可通过 npm 安装，支持 Node、CommonJS、ESM、浏览器和 CDN 使用。
- 📖 **使用方法**：通过 `cronstrue.toString()` 方法将 Cron 表达式转换为可读描述，支持多种选项配置。
- 🌍 **国际化支持**：支持 30 多种语言，可以导入所有语言或单独加载需要的语言模块。
- ❓ **常见问题**：库不验证 Cron 表达式的有效性，建议使用其他库如 `cron-parser` 进行验证。
- 📜 **许可证**：采用 MIT 许可证，可自由分发。
- 💖 **赞助与贡献**：项目有多个赞助者和贡献者，欢迎参与和支持。

---

### [cRonstrue - 将 Cron 表达式翻译为人类可读的描述](https://bradymholt.github.io/cRonstrue/)

**原文标题**: [cRonstrue - translate cron expressions to human readable descriptions](https://bradymholt.github.io/cRonstrue/)

cRonstrue 是一个将 cron 表达式翻译成人类可读描述的 JavaScript 库，支持多国语言，无依赖，并兼容多种 cron 表达式格式。

- ⏳ 将 cron 表达式（如 `*/5 * * * *`）翻译为易读描述（如 "每 5 分钟"）
- 🌍 支持 30+ 种语言，包括中文、英语、日语等
- 🛠️ 兼容 5/6/7 段式 cron 表达式，支持特殊字符（* / , - ? L W #）
- ⚙️ 支持 Quartz Job Scheduler 的 cron 表达式格式
- 📦 零依赖，轻量级库
- 👥 由 Brady Holt 创建维护，众多贡献者参与改进
- 🔗 GitHub 开源项目，可自由使用

---

### [ESLint v9.31.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/07/eslint-v9.31.0-released/)

**原文标题**: [ESLint v9.31.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/07/eslint-v9.31.0-released/)

ESLint v9.31.0 是一个小版本升级，引入了新功能并修复了之前版本中的多个错误。

- 🚀 **核心规则支持显式资源管理**：更新了四个核心规则以支持 ES2026 JavaScript 中的显式资源管理，包括 `using` 和 `await using` 语法。
- 🔧 **`init-declarations` 规则改进**：不再报告必须初始化的 `using` 和 `await using` 变量。
- 🛑 **`no-const-assign` 规则增强**：现在会报告修改 `using` 和 `await using` 变量的行为。
- 🔄 **`no-loop-func` 规则优化**：不再报告对 `using` 和 `await using` 变量的引用，因为这些变量是常量。
- 📌 **`no-undef-init` 规则调整**：不再报告初始化为 `undefined` 的 `using` 和 `await using` 变量。
- 📊 **`RuleTester` 输出改进**：增强 `run` 方法，显示多个不匹配的错误位置属性，而不仅仅是单个属性。
- ✨ **新特性**：包括对显式资源管理的支持以及 `RuleTester` 输出的改进。
- 🐛 **错误修复**：修复了写入自动修复结果时的 EMFILE 重试问题，并移除了不正确的 `RuleContext` 类型。
- 📚 **文档更新**：更新了 README 和其他文档，修复了代码与文本不匹配的问题。
- 🔄 **维护工作**：升级了 `@eslint/js` 和其他依赖项，并进行了其他维护任务。

---

### [GitHub - CodeGenieApp/serverless-express: 在 AWS 无服务器技术（如 Lambda、API Gateway、Lambda@Edge 等）上运行 Express 及其他 Node.js 框架](https://github.com/CodeGenieApp/serverless-express)

**原文标题**: [GitHub - CodeGenieApp/serverless-express: Run Express and other Node.js frameworks on AWS Serverless technologies such as Lambda, API Gateway, Lambda@Edge, and more.](https://github.com/CodeGenieApp/serverless-express)

Serverless Express 是一个允许在 AWS Serverless 技术（如 Lambda、API Gateway 等）上运行 Express 和其他 Node.js 框架的工具。

- 🚀 **功能概述**：支持在 AWS Lambda、API Gateway、Lambda@Edge 等 Serverless 技术上运行 Express、Koa、Hapi 等 Node.js 框架。
- 📦 **安装方式**：通过 npm 安装 `@codegenie/serverless-express`。
- ⚡ **快速开始**：提供基础示例，包括 Lambda 函数、Express 应用和 Serverless 应用模板。
- 🔧 **Lambda 处理程序**：只需简单包装 Express 应用即可在 Lambda 中运行。
- 🔄 **异步处理**：支持在请求转发前执行异步任务（如数据库连接）。
- ☁️ **多平台支持**：不仅支持 AWS，还支持 Azure Functions。
- 🔄 **事件源支持**：支持 API Gateway、ALB、Lambda@Edge、VPC Lattice 等多种事件源。
- 🛠 **高级配置**：提供二进制响应处理、错误调试、自定义日志等高级功能。
- 📊 **性能优势**：按使用付费、无需管理基础设施、自动扩展等 Serverless 优势。
- 🔄 **项目维护**：原 AWS Serverless Express 现已由 Vendia 维护，并更名为 `@codegenie/serverless-express`。

---

### [发布 v3.1.0 · nats-io/nats.js · GitHub](https://github.com/nats-io/nats.js/releases/tag/v3.1.0)

**原文标题**: [Release v3.1.0 · nats-io/nats.js · GitHub](https://github.com/nats-io/nats.js/releases/tag/v3.1.0)

nats.js 仓库的 v3.1.0 版本发布，包含核心功能增强、JetStream 和 KV 模块的改进，以及文档和 CI 的更新。

- 🚀 **核心功能**：新增消息追踪支持（`TraceOptions`），修复订阅关闭事件和类型注解问题。  
- ✈️ **JetStream 改进**：支持每条消息的 TTL、固定消费者、严格模式及基于主题的序列约束。  
- 🔑 **KV 存储**：新增每条消息的 TTL 和 put/update 操作超时支持。  
- 📚 **文档更新**：修复拼写错误、更新示例链接，并补充新 API 类型说明。  
- 🛠️ **CI/工具**：移除旧 GitHub Actions 工作流，新增模块版本管理工具。  
- 👋 **新贡献者**：欢迎 @williamstein 等 4 位新开发者加入。  
- 🔗 **其他**：优化 Node.js 的 TLS 配置类型，修复服务迭代器关闭逻辑。

---

### [GitHub - sindresorhus/open：跨平台打开URL、文件、可执行程序等](https://github.com/sindresorhus/open)

**原文标题**: [GitHub - sindresorhus/open: Open stuff like URLs, files, executables. Cross-platform.](https://github.com/sindresorhus/open)

一个名为 "open" 的开源项目，用于跨平台打开 URL、文件和可执行文件，主要适用于命令行工具和脚本。

- 🚀 **项目功能**：支持跨平台打开 URL、文件和可执行文件，适用于命令行工具和脚本。
- 🔧 **技术特点**：使用 `spawn` 而非 `exec`，更安全；支持应用参数；修复了原 `node-open` 的多数问题。
- 📦 **安装方式**：通过 `npm install open` 安装，仅支持 ESM 模块。
- 💻 **使用示例**：可以打开图片、URL，并支持指定浏览器或应用及其参数。
- 📜 **API 说明**：提供 `open` 和 `openApp` 方法，支持等待应用退出、后台运行等选项。
- 🌍 **跨平台支持**：在 macOS、Windows 和 Linux 上使用不同的命令（`open`、`start`、`xdg-open`）。
- 🔍 **相关资源**：提供 CLI 工具和编辑器插件等相关项目链接。
- 📄 **许可证**：采用 MIT 许可证，有行为准则和安全政策。

---

### [GitHub - openai/openai-node: OpenAI API 官方 JavaScript/TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

OpenAI 官方提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API，支持多种功能和高级配置。

- 🚀 **官方库**：OpenAI 提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API。
- 📦 **安装方式**：支持 npm 和 JSR 安装，适用于 Node.js、Deno 等环境。
- 📄 **功能丰富**：支持文本生成、文件上传、实时 API、错误处理等。
- 🔄 **流式响应**：支持 Server Sent Events (SSE) 实现流式响应。
- 📂 **文件上传**：支持多种文件上传方式，如 `fs.ReadStream`、`fetch Response` 等。
- 🔒 **Webhook 验证**：提供验证和解析 webhook 的方法，确保安全性。
- ⚠️ **错误处理**：支持多种错误类型和状态码，便于调试。
- 🔄 **自动重试**：默认对某些错误自动重试，可配置重试次数。
- ⏱️ **超时设置**：可配置请求超时时间，默认 10 分钟。
- 📊 **分页支持**：支持自动分页和手动分页，便于处理大量数据。
- 🌐 **Azure OpenAI**：支持 Azure OpenAI，提供特定于 Azure 的配置。
- 📝 **高级用法**：支持自定义请求、日志记录、代理配置等。
- ❓ **常见问题**：提供语义版本控制、运行时要求等常见问题解答。
- 🤝 **贡献指南**：欢迎贡献，提供详细的贡献文档。

---

### [GitHub - bendrucker/snakecase-keys：将对象键名转换为蛇形命名](https://github.com/bendrucker/snakecase-keys)

**原文标题**: [GitHub - bendrucker/snakecase-keys: Convert an object's keys to snake case](https://github.com/bendrucker/snakecase-keys)

这是一个名为 `snakecase-keys` 的开源项目，用于将对象的键转换为蛇形命名法（snake case）。

- 🐍 项目功能：将对象的键转换为蛇形命名法（例如 `fooBar` 转换为 `foo_bar`）。
- 📦 安装方式：通过 `npm install snakecase-keys` 安装。
- 🛠️ 使用方法：导入 `snakecaseKeys` 函数并传入对象即可转换。
- ⚙️ 支持选项：包括深度转换（`deep`）、排除特定键（`exclude`）、自定义递归条件（`shouldRecurse`）等。
- 🔄 相关项目：`camelcase-keys` 和 `kebabcase-keys`。
- 📜 许可证：MIT 许可证。
- 🌟 项目状态：188 星，36 个 fork，被 163k+ 项目使用。
- 👥 贡献者：27 位贡献者。
- 💻 主要语言：TypeScript (60.6%) 和 JavaScript (39.4%)。

---

### [GitHub - poolifier/poolifier: 快速轻量的 Node.js worker_threads 与集群工作线程池](https://github.com/poolifier/poolifier)

**原文标题**: [GitHub - poolifier/poolifier: Fast and small Node.js worker_threads and cluster worker pool](https://github.com/poolifier/poolifier)

poolifier 是一个快速且轻量的 Node.js 工作线程（worker_threads）和集群（cluster）工作池库，旨在优化 CPU 和 I/O 密集型任务的性能，解决事件循环相关问题。

- 🚀 **高性能**：通过工作池提升任务执行效率，支持动态和固定大小的线程池。
- 🔄 **多模块支持**：兼容 Node.js 的 `worker_threads` 和 `cluster` 模块。
- 📊 **任务分发策略**：支持多种任务分发策略，包括空闲任务窃取和压力下的任务重分配。
- ⏱️ **动态资源管理**：动态线程池可根据负载自动扩展或收缩工作线程。
- 🔧 **开发者友好**：简洁的 API 设计，支持同步/异步任务、可中止任务及运行时任务函数管理。
- 🛡️ **健壮性**：内置错误处理，与 Node.js `async_hooks` 深度集成，广泛测试确保稳定性。
- 📦 **无运行时依赖**：轻量级，不引入额外依赖。
- 🌍 **多环境支持**：支持 CommonJS、ESM 和 TypeScript，适配 Node.js 20.x.x 及以上版本。
- 🔄 **活跃维护**：拥有活跃的社区和持续的开发维护，提供丰富的示例和文档。
- 📜 **开源许可**：采用 MIT 许可证，可自由使用和修改。

---

### [JavaScript 日期小测验](https://jsdate.wtf/)

**原文标题**: [The JavaScript Date Quiz](https://jsdate.wtf/)

JavaScript 的 Date 类小测验  
- 🧠 测试你对 JavaScript Date 类的了解程度  
- 🖥 使用 NodeJS 24.4.0 在 MacBook Pro 上验证（时区设为 BST，UTC+1）  
- ❤️ 由 samwho 制作  
- 📝 包含 20 个问题  
- 🔄 可依次答题或直接查看结果  
- 📤 支持分享和复制功能

---

### [ANSI 转义码](https://ansi.tools/)

**原文标题**: [ANSI Escape Codes](https://ansi.tools/)

提供的文本内容较短且零散，看起来像是一些关键词或标签的集合，没有明确的主题或连贯的上下文。以下是可能的总结：

- 📝 示例列表（如 ls/eza、blocks、test run）  
- 🔗 技术相关术语（如 hyperlinks、8-bit、commands）  
- 🎨 格式与样式（如 styles、mixed、colors）  
- 📊 数据操作（如 invert、grid、sort）  
- 📌 其他零散关键词（如 code、mnemonic、plain text）  

由于内容过于零散，无法形成具体的文章概述。

---

### [ANSI 转义码 | 速查表](https://ansi.tools/lookup)

**原文标题**: [ANSI Escape Codes | Lookup Table](https://ansi.tools/lookup)

以下是文本的概述总结：

- 📜 文本详细列出了各种终端控制序列（如 ESC 序列、CSI 序列、OSC 序列等），用于控制终端行为和显示效果。  
- 🎨 包含 SGR（Select Graphic Rendition）代码，用于设置文本样式（如粗体、斜体、颜色等）。  
- 🖥️ 描述了终端功能（如光标移动、屏幕擦除、滚动区域设置等）。  
- 🖱️ 包含鼠标和键盘事件处理的相关控制序列。  
- 🔄 涉及终端模式切换（如启用/禁用自动换行、反向视频等）。  
- 🌈 支持 24 位真彩色和 256 色调色板设置。  
- 📌 包含 OSC（Operating System Command）指令，用于设置窗口标题、图标、颜色等。  
- 🔧 提供 DEC 私有模式和其他终端特定功能的控制序列。  
- ❓ 最后提示如有遗漏或错误可反馈或修复。

---

### [在 Bun/Typescript 中 10 秒内解析 10 亿行数据](https://www.taekim.dev/writing/parsing-1b-rows-in-bun)

**原文标题**: [Parsing 1 Billion Rows in Bun/Typescript Under 10 Seconds](https://www.taekim.dev/writing/parsing-1b-rows-in-bun)

Tae Kim 使用 Bun/Typescript 在 10 秒内解析了 10 亿行数据，以下是关键步骤和优化策略：

- 🚀 **挑战背景**：受 1BRC（10 亿行挑战）启发，作者尝试用 Bun/Typescript 处理 13.8GB 文件，目标是计算每个气象站的最低、最高和平均温度。
- 🏗️ **初始尝试**：尝试用 `readFileSync` 读取整个文件，但遇到内存限制（Buffer 最大 4GB）。
- 🔄 **分块处理**：改用 `openSync` 和 `readSync`，分块读取文件（128KB 缓冲区最优，耗时 <1 秒）。
- ⚙️ **多线程优化**：利用多核 CPU 创建 Worker 处理分块数据，避免单线程瓶颈。
- 📏 **分块边界处理**：确保每个分块以换行符结束，避免截断数据行。
- ⚡ **性能提升**：手动解析字节（避免 UTF-8 解码），最终耗时 **9.22 秒**（每秒处理 5364 万行）。
- 📌 **关键限制**：Bun 的单线程特性和内存管理（如 4GB Buffer 限制）是主要挑战。
- 🔍 **优化重点**：平衡 I/O 和 CPU 负载，减少不必要的解码和内存分配。

---

### [nginx](https://nginx.org/)

**原文标题**: [nginx](https://nginx.org/)

NGINX 团队邀请用户参与 2025 年 NGINX 用户调查，并提供了相关资源和最新动态。

- 📢 NGINX 团队邀请用户参与 2025 年 NGINX 用户调查。  
- 🌐 NGINX 是一个多功能服务器，支持 HTTP、反向代理、内容缓存、负载均衡等。  
- 📜 最初由 Igor Sysoev 开发，采用 2-clause BSD 许可证。  
- 🏢 F5, Inc.提供企业版、商业支持及培训服务。  
- 🚀 最新版本 njs-0.9.1 发布，新增共享字典状态文件支持。  
- 🚀 nginx-1.29.0 主线版本发布，支持 Early Hints 功能。  
- ⚡ njs-0.9.0 版本性能提升 30%。  
- 🛠️ nginx-1.28.0 稳定版发布，包含多项优化和新功能。  
- 📚 其他 NGINX 项目包括 njs、NGINX Unit、Ingress Controller 和 Gateway Fabric。

---

### [现代 JavaScript 在 NGINX 中的应用：njs 对 QuickJS 引擎的支持 – NGINX 社区博客](https://blog.nginx.org/blog/quickjs-engine-support-for-njs)

**原文标题**: [Modern JavaScript in NGINX: QuickJS Engine Support for njs – NGINX Community Blog](https://blog.nginx.org/blog/quickjs-engine-support-for-njs)

NGINX 的 njs 模块现在支持 QuickJS 引擎，提供 ES2023 兼容性，为开发者带来更现代的 JavaScript 功能。

- 🚀 **QuickJS 引擎支持**：njs 0.9.1 版本引入 QuickJS 引擎，支持完整的 ES2023 规范，包括模块、异步生成器等现代特性。
- ⚖️ **平衡开发与集成**：原本的 njs 引擎虽轻量快速，但维护成本高且功能有限，QuickJS 的集成解决了这一问题。
- 🔄 **无缝切换**：通过`js_engine`指令可轻松切换引擎，现有脚本无需修改即可兼容 QuickJS。
- 📊 **性能考量**：QuickJS 在复杂逻辑处理上表现优异，但上下文创建时间较长，可通过`js_context_reuse`优化。
- 🧩 **高级功能示例**：展示了使用类、生成器、BigInt 等 ES2023 特性的复杂脚本示例。
- ⏱️ **性能对比**：启用上下文重用时，QuickJS 性能与 njs 引擎相当；禁用时性能显著下降。
- 🔮 **未来展望**：计划逐步将 QuickJS 设为默认引擎，鼓励开发者迁移以利用现代 JavaScript 特性。
- 📢 **反馈征集**：鼓励用户试用并提供反馈，以进一步优化引擎功能和性能。

---

