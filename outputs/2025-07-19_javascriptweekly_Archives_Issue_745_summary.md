### [JavaScript 周刊第 745 期：2025 年 7 月 18 日](https://javascriptweekly.com/issues/745)

**原文标题**: [JavaScript Weekly Issue 745: July 18, 2025](https://javascriptweekly.com/issues/745)

- 📧 订阅服务，随时可取消，邮箱安全有保障（附隐私政策链接）。  
- 🧩 JavaScript 周报#745（2025 年 7 月 18 日）包含技术动态与工具更新。  
- ⏳ **JavaScript 日期测验**：挑战对原生日期解析的认知，等待 Temporal API 普及前的趣味测试。  
- 🔄 **Next.js 15.4 发布**：性能优化、稳定性提升及 Turbopack 兼容性改进，并预告 Next.js 16 新特性。  
- 🔐 **WorkOS 赞助**：简化 SSO/SCIM 集成，助力开发者专注核心功能（客户包括 Vercel 等）。  
- 🌐 **WebAssembly 应用场景**：深入探讨其在浏览器与服务器端的多样化应用趋势。  
- 🚀 **技术简讯**：  
  - Vue 3.6 Alpha 预览版发布，新增 Vapor Mode 高效编译。  
  - React Native 支持 Node-API，促进代码共享与生态扩展。  
  - Node.js 考虑改为年度大版本更新。  
  - Laravel（PHP）现可在 Node.js 环境中运行。  
- 📦 **版本发布**：  
  - Nuxt v4.0（全栈 Vue 框架重大更新）。  
  - Node.js 多版本安全补丁（v24.4.1 等）。  
  - ESLint v9.31.0 支持显式资源管理规则。  
- 📚 **文章与视频**：  
  - 2025 年创建 NPM 包全指南（Matt Pocock）。  
  - React 发展史与核心设计哲学（Corbin Crutchley）。  
  - 8 分钟速览 JavaScript 历史（Deno 团队视频）。  
- 🛠️ **工具推荐**：  
  - Tiptap v3 无头富文本编辑器框架（支持 SSR 等新特性）。  
  - Hyper Fetch 强化版 Fetch 库（类型安全、实时通信）。  
  - Wallaby AI 调试工具（比断点快 15 倍）。  
- 🎁 **附加内容**：  
  - Git 仓库统计脚本（`git-quick-stats.sh`）。  
  - 24 小时爬取 10 亿网页经验分享。  
  - GitHub Copilot Coding Agent 预览。  
  - 亚马逊 S3 新增向量存储查询功能。

---

### [JavaScript 日期小测验](https://jsdate.wtf/)

**原文标题**: [The JavaScript Date Quiz](https://jsdate.wtf/)

JavaScript 的 Date 类小测验，包含 20 个问题，使用 NodeJS 24.4.0 在 BST 时区（UTC+1）的 MacBook Pro 上验证。

- 📅 测验主题：JavaScript 的 Date 类  
- 🖥️ 测试环境：NodeJS 24.4.0，MacBook Pro，BST 时区（UTC+1）  
- ❤️ 制作者：samwho  
- 🔢 题目数量：20 个问题  
- 🎯 测验进度：从“第 1 题”开始，可逐步完成  
- 📊 结果展示：最终显示正确率（0/0 初始状态）  
- 🔗 分享功能：支持分享或复制测验链接

---

### [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

**原文标题**: [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

Temporal 是一个用于处理日期和时间的新 API，旨在替代现有的 `Date` 对象，提供更强大和灵活的功能。

- ⏳ **实验性技术**：Temporal 目前是实验性功能，尚未在所有主流浏览器中广泛支持。
- 🔄 **替代 Date 对象**：Temporal 旨在解决 `Date` 对象的诸多设计缺陷，提供更完善的日期和时间管理功能。
- 🌍 **时区和日历支持**：Temporal 内置支持多种时区和日历系统，解决了 `Date` 对象在时区和日历处理上的不足。
- ⚙️ **静态方法**：与 `Math` 类似，Temporal 的所有属性和方法都是静态的，不能通过构造函数调用。
- 📅 **丰富的类结构**：Temporal 包含多个类，如 `Temporal.Instant`、`Temporal.ZonedDateTime` 等，分别用于处理不同的日期和时间场景。
- 📊 **API 复杂性**：Temporal 提供了超过 200 个实用方法，通过多个类组织，功能强大但可能显得复杂。
- ⚠️ **日期处理的复杂性**：Temporal 强调了日期处理的复杂性，并提供了更安全和易用的 API 设计。
- 📜 **RFC 9557 格式**：Temporal 支持 RFC 9557 格式的日期时间字符串，扩展了 ISO 8601 的功能。
- 🚫 **有限的日期范围**：Temporal 对象支持的日期范围有限，超出范围的日期将无法构造或操作。
- 📚 **更多资源**：可以参考 `Intl.DateTimeFormat` 等相关 API 来进一步了解日期和时间的处理。

---

### [Next.js 15.4 | Next.js](https://nextjs.org/blog/next-15-4)

**原文标题**: [Next.js 15.4 | Next.js](https://nextjs.org/blog/next-15-4)

Next.js 15.4 版本带来了性能、稳定性和 Turbopack 兼容性的更新，同时预览了 Next.js 16 的新功能。

- 🚀 **Turbopack 构建**：`next build --turbopack` 已通过所有 8298 项集成测试，并在 vercel.com 上验证。
- 🔧 **稳定性改进**：Next.js 和 Turbopack 进行了多项稳定性和性能优化。
- ⏳ **Next.js 16 预览**：包括缓存组件、优化客户端路由、开发工具调试等新功能。
- 📦 **部署适配器**：新增自定义部署适配器支持，提供更灵活的构建和部署选项。
- 🛠️ **升级指南**：提供了自动升级 CLI 和手动升级的详细步骤。
- 🐞 **问题修复**：修复了多个已知问题，包括缓存、路由和性能优化等方面。
- 🙏 **贡献者致谢**：感谢超过 3000 名开发者的贡献，特别提到了 Next.js、Turbopack 和文档团队的成员。

---

### [WebAssembly：是的，但用来做什么？- ACM Queue](https://queue.acm.org/detail.cfm?id=3746171)

**原文标题**: [WebAssembly: Yes, but for What? - ACM Queue](https://queue.acm.org/detail.cfm?id=3746171)

WebAssembly（Wasm）已发展十年，尽管在部分领域取得成功，但尚未完全发挥潜力。文章探讨了 Wasm 的成功与失败案例，并预测了未来可能的应用方向。

- 🌐 **Web 上的 Wasm**：Wasm 在网页端表现参差不齐，成功案例包括 Adobe Photoshop 的网页版和 SQLite 的 Wasm 编译版本，但在游戏行业未成为主流。
- 🛠️ **工具链与语言支持**：Wasm 主要适用于 C++ 和 Rust 等低级语言，但新的 WasmGC 扩展为更多语言（如 Java、Kotlin）提供了支持。
- 🔌 **非网页应用**：Wasm 在插件系统、轻量级虚拟化和组件模型中表现出色，如 Firefox 使用 RLBox 工具隔离不安全代码。
- ☁️ **云计算潜力**：Wasm 的快速冷启动特性使其在边缘计算和云服务中具有优势，多家公司正在探索相关应用。
- 🔍 **成功模式**：Wasm 在需要隔离和安全性的场景中表现最佳，如插件系统和虚拟化。
- 🚀 **未来方向**：可能的应用包括操作系统内核驱动、轻量级操作系统和 AI 领域的机密计算。

---

### [发布 v3.6.0-alpha.1 · vuejs/core · GitHub](https://github.com/vuejs/core/releases/tag/v3.6.0-alpha.1)

**原文标题**: [Release v3.6.0-alpha.1 · vuejs/core · GitHub](https://github.com/vuejs/core/releases/tag/v3.6.0-alpha.1)

Vue.js 3.6.0-alpha.1 版本发布，引入 Vapor Mode 新编译模式，旨在减少基础包大小并提升性能。该版本包含多项功能改进、性能优化和错误修复，同时提供部分功能的稳定性测试。

- 🚀 **Vapor Mode 新特性**：新的 SFC 编译模式，支持部分 Vue API，性能对标 Solid 和 Svelte 5。  
- 🔧 **性能优化**：重构响应式核心代码，提升反应性系统效率。  
- 🐞 **错误修复**：修复 CSS 变量继承、响应式作用域管理等问题。  
- ⚠️ **稳定性说明**：Vapor Mode 仍处于 Alpha 阶段，不建议用于生产环境迁移。  
- 📌 **待实现功能**：SSR 水合、异步组件、过渡动画等暂不支持。  
- 🔌 **启用方式**：在 `<script setup>` 中添加 `vapor` 属性，或通过 `vaporInteropPlugin` 实现与 VDOM 的互操作。  
- ⚠️ **兼容性限制**：不支持 Options API、全局属性等特性，自定义指令接口也有变化。  
- 🔄 **行为一致性**：Vapor Mode 尽量匹配 VDOM 行为，但可能存在边缘情况差异。  
- 📊 **社区反响**：发布后获得大量积极反馈（👍 240、🎉 189 等）。

---

### [宣布 React Native 支持 Node-API](https://www.callstack.com/blog/announcing-node-api-support-for-react-native)

**原文标题**: [Announcing Node-API Support for React Native](https://www.callstack.com/blog/announcing-node-api-support-for-react-native)

React Native 宣布支持 Node-API，这是一个跨平台的本地模块系统，旨在简化开发并提升性能。

- 🚀 **Node-API 引入 React Native**：将 Node.js 中广泛使用的本地模块系统 Node-API 引入 React Native，实现跨运行时和稳定的 JavaScript 与本地代码交互。  
- 🔧 **跨平台与多语言支持**：Node-API 支持多种编程语言（如 C++、Rust、Swift 等），并具有 ABI 稳定性，便于模块共享和维护。  
- ⏱️ **提升构建效率**：通过预构建本地模块，显著减少应用构建时间，Android 上可能缩短至 7 秒。  
- 🌐 **生态系统兼容性**：Node-API 已在 Node.js、Deno、Bun 等运行时中广泛应用，React Native 的加入将进一步促进代码共享。  
- 📦 **现有生态利用**：支持直接使用现有的 Node-API 模块（如 WebRTC、Web Audio），加速功能开发。  
- 🛠️ **适用场景**：适合跨平台共享代码、高性能计算（如 AI、加密）或调用平台 API 的场景。  
- 🚧 **进展与限制**：目前需使用特定版本的 React Native 和 Hermes，iOS 和 Android 已支持，其他平台正在扩展中。  
- 🤝 **社区协作**：由 Microsoft、Callstack 等团队共同推动，欢迎开发者参与贡献。  
- 🔗 **示例与资源**：提供示例仓库（[node-api-example-lib](https://github.com/callstackincubator/node-api-example-lib)）和文档（[react-native-node-api](https://github.com/callstackincubator/react-native-node-api)）供参考。

---

### [提案 - 将 Node.js 改为年度主版本发布并缩短 LTS 支持周期 · Issue #1113 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1113)

**原文标题**: [Proposal - Shift Node.js to Annual Major Releases and Shorten LTS Duration · Issue #1113 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1113)

Node.js 提议将主要版本发布周期从半年一次改为一年一次，并缩短长期支持（LTS）期限，以减轻维护负担并提高稳定性。

- 🚀 **背景**：当前半年一次的主要版本发布导致维护压力大，社区和生态系统对版本选择感到困惑。  
- 📅 **提议变更**：改为每年一次主要版本发布，LTS 期限从 30 个月缩短至 24 个月（12 个月活跃支持 + 12 个月维护支持）。  
- ✅ **优点**：减轻维护负担、提高发布质量、提供更清晰的长期支持承诺。  
- ❌ **缺点**：可能减缓新功能发布速度，部分社区成员可能不适应较短的 LTS 期限。  
- 🛠️ **实施策略**：需获得技术指导委员会（TSC）和发布工作组的共识，更新文档并加强沟通。  
- 📢 **下一步**：在发布工作组内展开详细讨论，准备过渡文档和时间表，并收集社区反馈。  
- 👍 **社区反应**：60 人支持，6 人反对，2 人点赞，1 人关注。

---

### [Laravel 与 Node.js：Watt 运行时中的 PHP](https://blog.platformatic.dev/laravel-nodejs-php-in-watt-runtime)

**原文标题**: [Laravel and Node.js: PHP in Watt Runtime](https://blog.platformatic.dev/laravel-nodejs-php-in-watt-runtime)

Laravel 应用现可通过 Platformatic PHP stackable 在 Node.js 的 Watt 运行时中运行，实现了 PHP 与 Node.js 生态的融合，为全栈开发者提供了新的可能性。

- 🚀 Laravel 应用现可在 Node.js 中运行，通过 Platformatic PHP stackable 实现 PHP 与 Node.js 的集成。
- 🔗 使用@platformatic/php-node 这一 Rust 原生模块，实现高性能的 PHP 与 JavaScript 桥接。
- 📦 配置简单，只需在 package.json 中添加必要依赖和配置 platformatic.json 文件。
- 🛠️ 支持 Laravel 的路由规则和热重载，提升开发效率。
- 🌐 允许 PHP 和 JavaScript 微服务在统一运行时中部署，减少基础设施复杂度。
- 🔄 提供逐步迁移的可能性，可在保持现有功能的同时向 JavaScript 过渡。
- 📚 支持自定义 PHP 扩展、环境变量管理和性能调优等高级功能。
- 📈 为现代 Web 开发开辟新途径，结合 Laravel 和 Node.js 生态的优势。

---

### [发布 Nuxt 4.0 · Nuxt 博客](https://nuxt.com/blog/v4)

**原文标题**: [Announcing Nuxt 4.0 · Nuxt Blog](https://nuxt.com/blog/v4)

Nuxt 4.0 正式发布，专注于提升开发者体验，带来更清晰的项目结构、更智能的数据获取和更好的类型安全支持。

- 🎉 **Nuxt 4.0 发布**：经过一年的实际测试，Nuxt 4.0 正式发布，这是一个以稳定性为重点的主要版本，引入了一些深思熟虑的重大变化以改善开发体验。  
- 🗂️ **新的项目结构**：默认将应用代码放在`app/`目录下，使项目组织更清晰，提升文件监视速度和 IDE 上下文感知。  
- 🔄 **更智能的数据获取**：优化了`useAsyncData`和`useFetch`，支持自动数据共享、自动清理和响应式键重新获取数据。  
- 🔧 **更好的 TypeScript 支持**：为应用代码、服务器代码和共享文件夹创建独立的 TypeScript 项目，提升自动补全和类型推断。  
- ⚡ **更快的 CLI 和开发体验**：冷启动更快，使用 Node.js 编译缓存和原生文件监视，减少系统资源占用。  
- 🚀 **升级指南**：大多数项目可以平滑升级，建议使用`npx nuxt upgrade --dedupe`命令，并配合 Codemod 工具自动化迁移步骤。  
- 🗺️ **未来计划**：Nuxt 5 将带来 Nitro v3 和 h3 v2，进一步提升性能，并支持 SSR 流式传输、内置无障碍模块等新功能。  
- ❤️ **感谢社区**：特别感谢过去一年中测试 v4 兼容模式的开发者们，他们的反馈帮助完善了这一版本。  
- 📑 **完整发布说明**：详细内容可查看 Nuxt v4.0.0 的完整发布说明。

---

### [Node.js — 2025 年 7 月 15 日星期二安全发布](https://nodejs.org/en/blog/vulnerability/july-2025-security-releases)

**原文标题**: [Node.js — Tuesday, July 15, 2025 Security Releases](https://nodejs.org/en/blog/vulnerability/july-2025-security-releases)

Node.js 项目于 2025 年 7 月 15 日发布安全更新，修复了多个高严重性漏洞，影响 20.x、22.x 和 24.x 版本。

- 🚨 **Windows 设备名称路径遍历漏洞 (CVE-2025-27210)**  
  - 影响所有活跃版本（20.x、22.x、24.x），尤其是 Windows 用户使用 `path.join` API 的情况。  
  - 感谢报告者 oblivionsage 和修复者 RafaelGSS。  

- ⚠️ **V8 引擎 HashDoS 漏洞 (CVE-2025-27209)**  
  - 仅影响 Node.js v24.x，攻击者可通过控制字符串生成哈希碰撞。  
  - 感谢报告者 sharp_edged 和修复者 targos。  

- 📥 **更新版本**  
  - 修复版本：v20.19.4、v22.17.1、v24.4.1。  

- ⏰ **发布时间**  
  - 计划于 2025 年 7 月 15 日或之后发布。  

- 🔍 **后续关注**  
  - 安全政策与漏洞报告流程详见 [Node.js 安全页面](https://nodejs.org/en/security/)。  
  - 建议订阅 [nodejs-sec 邮件列表](https://groups.google.com/forum/#!forum/nodejs-sec) 获取更新。

---

### [ESLint v9.31.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/07/eslint-v9.31.0-released/)

**原文标题**: [ESLint v9.31.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/07/eslint-v9.31.0-released/)

ESLint v9.31.0 是一个小版本升级，引入了新功能并修复了之前版本中的多个错误。

- 🆕 **核心规则支持显式资源管理**：更新了四个核心规则以支持 ES2026 JavaScript 中的显式资源管理，包括 `using` 和 `await using` 语法。
- 🛠️ **`init-declarations` 规则改进**：不再报告必须初始化的 `using` 和 `await using` 变量。
- 🚫 **`no-const-assign` 规则增强**：现在会报告修改 `using` 和 `await using` 变量的行为。
- 🔄 **`no-loop-func` 规则优化**：不再报告对 `using` 和 `await using` 变量的引用，因为这些变量是常量。
- 📍 **`RuleTester` 输出改进**：在测试用例中，错误位置的多个属性不匹配时会显示完整信息，而不仅是一个属性。
- 🐛 **错误修复**：包括修复 EMFILE 写入自动修复结果时的重试机制和移除不正确的 `RuleContext` 类型。
- 📚 **文档更新**：修复了 `globalIgnores()` 代码与文本不匹配的问题，并更新了 README 和工作问题信息。
- 🔧 **维护工作**：升级到 `@eslint/js@9.31.0`，更新依赖项，并进行了其他维护任务。

---

### [Astro 5.12 | Astro](https://astro.build/blog/astro-5120/)

**原文标题**: [Astro 5.12 | Astro](https://astro.build/blog/astro-5120/)

Astro 5.12 发布，带来 Netlify 开发体验升级、内容加载器支持 TOML 文件等新功能。

- 🚀 **Astro 5.12 发布**：包含 Netlify 开发体验升级、TOML 支持及实验性环境变量原始值功能。  
- ⚙️ **TOML 支持**：内容加载器现支持 TOML 文件，无需额外配置，可直接在内容集合中使用。  
- 🌐 **Netlify 开发体验**：新版适配器集成 Netlify 平台功能，本地开发时支持图片 CDN、Blobs 服务器、重定向等。  
- 🔧 **实验性功能**：新增 `rawEnvValues` 选项，禁用环境变量自动类型转换，与 Vite 行为对齐。  
- 🔄 **升级指南**：推荐使用 `@astrojs/upgrade` CLI 工具或手动运行包管理器命令升级。  
- 🐞 **错误修复**：修复了自 5.11 版本以来的多个问题，详情参见更新日志。  
- 👏 **社区贡献**：感谢核心团队及众多社区成员的代码与文档贡献。

---

### [发布 Neutralinojs v6.2.0！· neutralinojs/neutralinojs · GitHub](https://github.com/neutralinojs/neutralinojs/releases/tag/v6.2.0)

**原文标题**: [Release Neutralinojs v6.2.0 released! · neutralinojs/neutralinojs · GitHub](https://github.com/neutralinojs/neutralinojs/releases/tag/v6.2.0)

Neutralinojs 项目发布了 v6.2.0 版本，新增了窗口和文件系统 API 功能，改进了配置选项，并修复了一些问题。

- 🖨️ 新增`Neutralino.window.print()`功能，支持在所有平台显示原生打印对话框。  
- 🖱️ 引入`window.beginDrag()`函数，用于触发原生窗口拖动。  
- 📁 添加`filesystem.getJoinedPath`、`getNormalizedPath`和`getUnnormalizedPath`函数，优化路径处理。  
- ⚙️ 新增`window.webviewArgs`配置选项，支持为 Windows 平台的 WebView2 实例传递额外参数。  
- 🐞 改进了 WebView 初始化失败时的 GUI 错误提示，并更新了`cli.binaryVersion`至 6.2.0。  
- 📚 提供快速入门文档链接：[Neutralino.js 文档](https://neutralino.js.org/docs)。  
- 🤖 此版本由 ReleaseZri 自动生成。

---

### [发布 v6.2.0 · openpgpjs/openpgpjs · GitHub](https://github.com/openpgpjs/openpgpjs/releases/tag/v6.2.0)

**原文标题**: [Release v6.2.0 · openpgpjs/openpgpjs · GitHub](https://github.com/openpgpjs/openpgpjs/releases/tag/v6.2.0)

OpenPGP.js 发布了 v6.2.0 版本，包含多项功能改进和错误修复。

- 🔒 默认启用 OpenPGP 消息语法验证（新增 `config.enforceGrammar` 配置项）
- ⚡ 支持在可用时使用 WebCrypto 进行 X25519 加密
- 🔄 在创建时间相同的情况下，优先选择算法 ID 更高的子密钥（假设其更现代/安全）
- 🛠 改进数据包流和错误处理：
  - 未认证流中的解析错误会延迟到解密数据流认证后才抛出
  - 非关键未知数据包转为 `UnparseablePacket` 对象而非被忽略
- 📝 使 Issuer Key ID 签名子数据包变为非关键项
- 🧩 改进 `User` 类的类型定义
- 👋 新增两位贡献者：@caarlos0 和 @kkredit
- 📦 完整更新日志：v6.1.0...v6.2.0

---

### [如何创建 NPM 包 | 完全掌握 TypeScript](https://www.totaltypescript.com/how-to-create-an-npm-package)

**原文标题**: [How To Create An NPM Package | Total TypeScript](https://www.totaltypescript.com/how-to-create-an-npm-package)

本指南详细介绍了如何从零开始创建一个生产就绪的 npm 包，涵盖版本控制、代码编写、格式化、测试、CI 流程、版本管理和发布等全流程步骤。

- 🛠️ 初始化 Git 仓库，设置.gitignore，并推送到 GitHub  
- 📦 创建 package.json，配置基本信息、许可证和 README  
- 🖥️ 安装 TypeScript，配置 tsconfig.json，设置构建脚本  
- ✨ 使用 Prettier 格式化代码，并集成到 CI 流程  
- 🧪 使用 Vitest 进行测试，支持开发模式和 CI 运行  
- 🔄 配置 GitHub Actions 实现自动化 CI 流程  
- 🚀 使用 Changesets 管理版本和发布，支持自动生成变更日志  
- 📌 最终实现一个包含完整工具链的生产级 TypeScript npm 包

---

### [React 代码演变史 | 趣味编程](https://playfulprogramming.com/posts/react-history-through-code)

**原文标题**: [
	The History of React Through Code | Playful Programming
](https://playfulprogramming.com/posts/react-history-through-code)

React 的发展历程及其核心设计理念的演变，展示了其从诞生至今的持续一致性和对未来功能的深远规划。

- 🚀 **React 的起源**：2011 年由 Jordan Walke 创建，最初为 Facebook 内部解决 BoltJS 的问题，后发展为 React 并开源。
- 🔄 **虚拟 DOM (VDOM)**：React 引入 VDOM 以提高性能，通过差异比较仅更新必要的 DOM 节点。
- 🏗️ **组件化开发**：React 强调组件化，通过组合和复用组件构建复杂 UI。
- ⚡ **Hooks 的引入**：2019 年推出的 Hooks 解决了类组件的逻辑复用问题，使函数组件更强大。
- 🔄 **并发特性**：React 18 引入并发模式，优化渲染优先级，提升用户体验。
- 📡 **数据获取**：React 19 的 `use` API 和 Suspense 简化数据获取，避免瀑布式加载。
- 🌐 **服务器组件**：React 服务器组件 (RSC) 优化了服务器端渲染，减少客户端重新渲染。
- 🔮 **未来展望**：React 正在开发 `<Activity>` API 和编译器优化，进一步提升性能和开发体验。
- 🧩 **一致性设计**：React 的设计理念始终保持一致，从 VDOM 到 Hooks 再到服务器组件，每个新功能都基于现有架构。

---

### [如何使用 Clerk、Lovable 和 Supabase 构建 AI 编码规则应用](https://clerk.com/blog/build-app-with-lovable-supabase-clerk?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=ai-coding-rules&utm_content=07-18-25-jsw&dub_id=BHzEOYO6hGurGVqs)

**原文标题**: [How to build an AI coding rules app with Clerk, Lovable, and Supabase](https://clerk.com/blog/build-app-with-lovable-supabase-clerk?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=ai-coding-rules&utm_content=07-18-25-jsw&dub_id=BHzEOYO6hGurGVqs)

本文介绍了如何利用 Clerk、Lovable 和 Supabase 构建一个安全的 AI 编码规则应用的全过程。

- 🛠️ **工具组合**：使用 Lovable 的 AI 生成平台、Clerk 的身份验证和 Supabase 的数据存储，快速构建全栈应用。
- 🤖 **Lovable 简介**：Lovable 是一个通过聊天与 AI 代理交互即可构建全栈应用的平台，支持 React 和 Supabase 等流行框架。
- 🔐 **Clerk 的作用**：Clerk 提供用户管理和身份验证功能，通过简单的代码即可实现复杂的身份验证流程。
- 📦 **Supabase 集成**：Supabase 作为后端服务，支持 Row-Level Security (RLS) 来确保数据安全，并与 Clerk 无缝集成。
- 🚀 **应用构建步骤**：
  - 在 Lovable 中输入提示，生成应用框架。
  - 配置 Clerk 应用并获取 API 密钥。
  - 集成 Supabase 并设置 RLS 策略，确保用户只能访问自己的数据。
- ⚠️ **注意事项**：AI 生成代码可能存在错误或漏洞，需人工审核和修正。
- 🔧 **常见问题解决**：
  - 修正类型不匹配问题。
  - 确保 Supabase 客户端正确配置 Clerk 会话令牌。
- 🎯 **结论**：结合 AI 工具和现代开发工具，可以快速构建安全、可扩展的应用，但仍需人工监督以确保质量。

---

### [JavaScript 不为人知的故事 - YouTube](https://www.youtube.com/watch?v=TYsPrXWgNS8)

**原文标题**: [The untold story of JavaScript - YouTube](https://www.youtube.com/watch?v=TYsPrXWgNS8)

这是一个关于 Google LLC 旗下平台（可能是 YouTube）的相关信息和链接的简要列表。  

- 📢 簡介  
- 🗞️ 新聞中心  
- ©️ 版權  
- 📩 聯絡我們  
- 🎨 創作者  
- 📢 刊登廣告  
- 💻 開發人員  
- 📜 條款  
- 🔒 私隱  
- ⚖️ 政策及安全  
- ▶️ YouTube 的運作方式  
- 🧪 測試新功能  
- © 2025 Google LLC

---

### [JavaScript 简史 | Deno](https://deno.com/blog/history-of-javascript)

**原文标题**: [A brief history of JavaScript | Deno](https://deno.com/blog/history-of-javascript)

JavaScript 诞生 30 周年，从 10 天开发的脚本语言成长为全球最流行的编程语言，塑造了现代 Web 生态。以下是其发展历程的关键节点：

- 🚀 **1994 年 12 月**：Netscape 发布首款图形化浏览器 Netscape Navigator 1.0，为 JavaScript 诞生奠定基础  
- ⏱️ **1995 年 5 月**：Brendan Eich 用 10 天设计出 JavaScript，命名借 Java 热度营销  
- ⚔️ **1996 年 3 月**：微软推出 JScript 对抗 Netscape，开启浏览器脚本语言之争  
- 📜 **1997 年 6 月**：JavaScript 提交 ECMA 标准化，形成 ECMAScript 规范与 TC39 委员会  
- 🔥 **1998 年 1 月**：Netscape 开源浏览器代码，催生 Mozilla 项目与未来 Firefox  
- 📡 **1999 年 3 月**：IE5 引入 XMLHttpRequest，为 AJAX 技术埋下伏笔  
- 🛠️ **2004 年 4 月**：Gmail 应用 AJAX 技术，开启 Web 2.0 时代  
- 🧩 **2006 年 3 月**：jQuery 发布，解决跨浏览器兼容性问题  
- 🚀 **2008 年 9 月**：Chrome 携 V8 引擎横空出世，JS 执行速度革命性提升  
- 💻 **2009 年 3 月**：Ryan Dahl 创建 Node.js，JavaScript 进军服务端开发  
- 🔄 **2015 年 6 月**：ES6 发布，带来 let/const、箭头函数、Promise 等现代语法  
- ⚛️ **2015 年 5 月**：React 开源，引领组件化前端开发浪潮  
- 📦 **2016 年 3 月**：npm left-pad 事件暴露供应链安全问题  
- 🦕 **2018 年 6 月**：Ryan Dahl 预告 Deno 项目，反思 Node.js 设计缺陷  
- 🛰️ **2020 年 5 月**：JavaScript 随 SpaceX 龙飞船进入太空  
- 🧬 **2022 年**：Deno 加入 TC39，IE11 退役，ES2022 支持顶层 await  
- 🚀 **2024 年**：Deno 2 发布，JSR 新注册表上线，与 Oracle 展开商标法律战  
- 🤖 **2025 年 3 月**：TypeScript 宣布 Go 语言移植计划，性能提升 10 倍  

JavaScript 已从简单的网页脚本发展为全栈开发的核心语言，涵盖前端、服务端、移动端甚至 AI 领域，其生态系统仍在持续创新演进。

---

### [获取失败](https://javascriptweekly.com/link/171980/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/171980/web)

无法总结：获取内容失败，状态码 403。

---

### [让你的网站开口说话：JavaScript Web Speech API - Andrew Magill, 网络工程师](https://magill.dev/post/make-your-website-talk-with-the-javascript-web-speech-api)

**原文标题**: [Make Your Website Talk with The JavaScript Web Speech API - Andrew Magill, Web Engineer](https://magill.dev/post/make-your-website-talk-with-the-javascript-web-speech-api)

网站通过 JavaScript Web Speech API 实现语音朗读功能，提升可访问性和用户体验。

- 🎙️ 利用 Web Speech API 为网站添加“朗读”按钮，让用户能听内容  
- 🛠️ 提供可复用的代码函数，检测浏览器支持并实现语音合成  
- 🌍 根据网页语言自动选择匹配的语音，增强多语言适配性  
- ♿ 兼顾无障碍需求，帮助视觉障碍用户或偏好听觉阅读的人群  
- 🤖 作者分享 React 组件实现代码，并附 MDN 文档等学习资源  
- 🚀 预测语音合成技术将随 AI 发展更普及，成为未来网页基础功能  
- 📢 文末鼓励社交分享，提供多平台快捷分享链接

---

### [我是如何绕过谷歌大规模反广告屏蔽更新的](https://0x44.xyz/blog/web-request-blocking/)

**原文标题**: [
        How I found a bypass in Google's big anti-adblock update
    ](https://0x44.xyz/blog/web-request-blocking/)

概述总结  
Google Chrome 从 MV2 升级到 MV3，移除了对广告拦截器至关重要的`webRequestBlocking`权限，但作者发现了一个漏洞，使得广告拦截器在 MV3 中仍可运行。  

- 🕵️‍♂️ Google Chrome 正在从 MV2 转向 MV3，移除了`webRequestBlocking`权限，这对广告拦截器造成重大影响。  
- 🐛 作者发现了一个漏洞，允许在 MV3 中继续使用`webRequestBlocking`功能，绕过了 Google 的限制。  
- 💻 漏洞源于 Chrome 扩展 API 的 JavaScript 绑定遗留问题，特别是`chrome.webRequest`事件的处理方式。  
- 🔧 通过伪造 WebView ID，作者成功绕过了权限检查，实现了请求拦截功能。  
- 📅 该漏洞在 2023 年被报告，并在 Chrome 118 中被修复，但作者未获得奖金，因为 Google 认为这不是安全问题。  
- 😆 作者认为这是自己发现过的最有趣的漏洞之一，展示了少量代码如何绕过大型公司的重大更新。  
- 🔗 文章还提到了作者发现的另一个 Chrome 扩展漏洞，该漏洞获得了 CVE 编号和 1 万美元的奖励。

---

### [获取失败](https://javascriptweekly.com/link/171982/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/171982/web)

无法总结：获取内容失败，状态码 403。

---

### [JavaScript 中使用 Array.fromAsync() 实现现代异步迭代 - Matt Smith](https://allthingssmitty.com/2025/07/14/modern-async-iteration-in-javascript-with-array-fromasync/)

**原文标题**: [
    Modern async iteration in JavaScript with Array.fromAsync() - Matt Smith
  ](https://allthingssmitty.com/2025/07/14/modern-async-iteration-in-javascript-with-array-fromasync/)

JavaScript 中通过 Array.fromAsync() 实现现代异步迭代  
2025 年 7 月 14 日 · 2 分钟阅读 · 1021 次浏览  

- 🆕 `Array.fromAsync()` 是 ES2024 新增方法，用于将异步或同步可迭代对象转为数组，返回`Promise<Array>`  
- 🔧 语法：`Array.fromAsync(source[, mapFn[, thisArg]])`，支持异步映射函数  
- ⚠️ 注意：输入必须是可迭代对象，单独 Promise 会抛出`TypeError`  
- 🚀 典型场景：异步生成器转数组、分页 API 数据整合、流数据处理替换`for await...of`循环  
- 💡 优势：相比手动循环收集或`Promise.all`，提供更简洁的异步数据聚合方案  
- 🔄 示例：异步翻倍数值 `await Array.fromAsync(generator, async x => x*10)`  
- 🛡️ 错误处理：迭代或映射中的错误会自动传递，可用`try...catch`捕获  
- 🌐 实际应用：  
  - 📑 分页数据加载：自动合并多页结果到单一数组  
  - 🌊 流处理：将 Web Streams API 的块数据转为数组存储  
- 📌 兼容性：Chrome 121+、Firefox 115+、Safari 16.4+、Edge 121+ 及 Node.js 22+ 原生支持  
- 🧩 备用方案：提供了简易 polyfill 实现（未完全符合 ECMAScript 规范）  
- 🔍 对比`Array.from()`：专为异步设计，支持 Promise 返回和异步映射

---

### [最新动态 | Tiptap 资源](https://tiptap.dev/docs/resources/whats-new)

**原文标题**: [What's new | Tiptap Resources](https://tiptap.dev/docs/resources/whats-new)

总结失败：Connection error.

---

### [GitHub - ueberdosis/tiptap：专为网页工匠打造的无头富文本编辑器框架](https://github.com/ueberdosis/tiptap)

**原文标题**: [GitHub - ueberdosis/tiptap: The headless rich text editor framework for web artisans.](https://github.com/ueberdosis/tiptap)

Tiptap 是一个无头（headless）、框架无关的富文本编辑器框架，基于 ProseMirror 构建，提供高度可定制和可扩展的编辑体验。它支持协作编辑、丰富的扩展功能，并适用于多种前端框架。

- 🚀 **无头框架**：Tiptap 不提供预设的用户界面，允许开发者完全自由地设计 UI。
- 🔧 **框架无关**：兼容 Vue、React 和原生 JavaScript，无兼容性问题。
- 🧩 **扩展驱动**：提供 100 多种扩展，支持从基础文本编辑到高级拖放功能。
- 💡 **协作编辑**：通过开源后端 Hocuspocus 和 Yjs 实现多人实时协作。
- 📚 **丰富文档**：详细文档和社区支持，帮助开发者快速上手。
- 🌟 **Pro 扩展**：提供高级功能如协作编辑、文件管理等，免费注册 Tiptap 账户即可使用。
- 🏗️ **开源与商业结合**：核心开源，同时提供付费高级功能如 Content AI 和 Tiptap Cloud。
- 💖 **活跃社区**：GitHub 讨论区、赞助商支持和贡献者社区推动项目发展。
- 📜 **MIT 许可**：自由使用和修改，适合商业和开源项目。

---

### [优票](https://upyo.org/)

**原文标题**: [Upyo](https://upyo.org/)

跨运行时兼容，在 Node.js、Deno、Bun 及边缘函数上提供一致的 API 体验。

- 🌐 跨平台支持：无缝运行于 Node.js、Deno、Bun 等环境  
- 🔄 API 一致性：在不同运行时中保持统一的接口设计  
- ⚡ 边缘计算友好：适配边缘函数场景，高效执行

---

### [Copilot 代理工具与 MCP 支持](https://wallabyjs.com/blog/wallaby-mcp.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Copilot Agent tools and MCP support](https://wallabyjs.com/blog/wallaby-mcp.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

Wallaby 推出 MCP 支持与 AI 工具，为开发者提供实时运行时数据，显著提升 AI 代理在代码调试、测试创建和代码分析中的能力。

- 🚀 **Agentic AI 工作流**：高质量上下文（如运行时值、执行路径、覆盖率数据）是 AI 代理理解、调试和增强代码的关键。  
- 🛠️ **支持多款 AI 代理**：包括 Copilot Agent、Cursor、Windsurf 等，可访问 Wallaby 和 Console Ninja 的运行时洞察。  
- 🔄 **新旧对比**：传统方式依赖表面级上下文（如 CLI 输出），新方式通过 MCP 服务器提供深度实时代码模型（如运行时值、依赖图）。  
- ⚙️ **两种集成方式**：VS Code 内置 AI 工具或独立 MCP 服务器，支持跨编辑器和代理使用。  
- 📝 **应用场景示例**：修复失败测试、创建新测试、分析代码覆盖率、优化代码等，支持分步处理复杂任务。  
- 🔧 **自定义配置**：通过 Copilot 指令或代理规则（如 Cursor/Windsurf）优化代理与 Wallaby 工具的交互。  
- 🌟 **新功能**：可视化运行时值为交互式图表，增强调试体验。  
- 📢 **反馈邀请**：鼓励用户探索并分享使用体验，以持续改进功能。

---

### [无缝请求与实时连接 | HyperFetch](https://hyperfetch.bettertyped.com/)

**原文标题**: [Seamless Requests and Real-Time Connectivity | HyperFetch](https://hyperfetch.bettertyped.com/)

Hyper Fetch 是一个现代化的数据交换框架，旨在简化与任何远程 API 的连接，提供类型安全、开发者友好和架构灵活性的解决方案。

- 🚀 **统一数据获取层** - Hyper Fetch 是一个适用于现代开发需求的数据交换框架，提供一流的类型安全和卓越的开发者体验。  
- 🤖 **AI/LLM 就绪** - 标准化架构支持 AI 驱动的适配器和 SDK 生成，内置 LLM 支持。  
- 📜 **标准化获取** - 通过 Swagger/OpenAPI 的代码生成，提升开发体验，减少错误并加速开发。  
- 🔍 **专用开发者工具** - 提供深度洞察，监控统计数据，分析性能，全面控制数据和缓存。  
- ⚡ **HyperFlow 开发者工具** - 实时请求跟踪、详细错误分析和全面的性能指标，提升调试体验。  
- 🔄 **实时通信** - 通过 WebSockets 模块实现应用程序中的实时数据交换。  
- ⚛️ **React 集成** - 使用自定义钩子轻松将 Hyper Fetch 集成到 React 应用中，简化数据获取和状态管理。  
- 🛠️ **框架无关** - 适用于 React、Next.js、Remix、Astro、Node.js 等任何 JavaScript 框架。  
- 📂 **SDK 生成** - 通过 CLI 从 OpenAPI/Swagger 模式生成类型安全的 SDK，提供类似 tRPC 的语法和自动完成功能。  
- 🌐 **开源与灵活** - 框架无关，几乎零依赖，可无缝集成到任何项目中并参与其发展。  
- 💡 **类型安全设计** - 充分利用 TypeScript 的潜力，自动生成类型，增强开发者信心。  
- 🤝 **社区支持** - 通过 GitHub Sponsors 计划或其他方式支持项目发展。

---

### [GitHub - BetterTyped/hyper-fetch：⚡ 数据获取与实时交换框架](https://github.com/BetterTyped/hyper-fetch)

**原文标题**: [GitHub - BetterTyped/hyper-fetch: ⚡ Fetching and realtime data exchange framework.](https://github.com/BetterTyped/hyper-fetch)

Hyper Fetch 是一个专注于简单性和高效性的数据获取和实时数据交换框架，具有类型安全和用户友好的设计，支持浏览器和服务器端使用。

- ⚡ **框架特点**：提供简单设置、请求取消、请求去重、队列管理、响应缓存、离线优先等功能。
- 🔗 **实时数据交换**：支持实时数据交换和类型安全设计。
- 📦 **安装方式**：可通过 npm 或 yarn 安装核心包、Sockets 包或 React 包。
- 🛠 **简单示例**：展示了如何创建客户端、定义请求以及发送请求。
- ⚛ **React 支持**：提供了 `useFetch` 和 `useSubmit` 等钩子，方便在 React 中使用。
- 🔄 **动态数据传递**：支持在发送请求时动态传递参数、数据和查询参数。
- 📡 **多适配器支持**：包括 Firebase、GraphQL 和 Axios 等适配器。
- 📜 **开源协议**：采用 Apache-2.0 许可证。
- 🌟 **社区支持**：拥有 1.2k 星标和 29 个分支，持续更新和维护。

---

### [GrowField — 一个轻量、无依赖的 JavaScript 模块，用于使 textarea 元素随内容自动扩展](https://growfield.js.org/)

**原文标题**: [GrowField — A tiny, dependency-free JavaScript module for making textarea elements grow with their content](https://growfield.js.org/)

GitHub 上的 GrowField 是一个轻量级、无依赖的 JavaScript 模块，用于使 textarea 元素随内容自动调整高度。

- 🌱 **项目名称**: GrowField  
- 📦 **特点**: 无依赖、轻量级的 JavaScript 模块  
- ✏️ **功能**: 让 textarea 元素随内容自动增长  
- 🏷️ **项目归属**: Five Fifteen 项目  
- ⬇️ **下载方式**: 可通过 GitHub 或 npm 安装  
- 📄 **文档**: GitHub 上提供详细文档  
- 🔧 **安装命令**: `npm install growfield --save`  
- ©️ **版权**: 归属于 Five Fifteen

---

### [GitHub - eslint/markdown: 检查 Markdown 文档中的 JavaScript 代码块](https://github.com/eslint/markdown)

**原文标题**: [GitHub - eslint/markdown: Lint JavaScript code blocks in Markdown documents](https://github.com/eslint/markdown)

ESLint Markdown 语言插件，用于在 Markdown 文档中检查 JavaScript 代码块，支持 JS、JSX、TypeScript 等多种语言。

- 📦 **安装方式**：支持 npm、yarn、pnpm、bun 和 Deno 等多种包管理器安装。
- ⚙️ **配置选项**：提供 `recommended` 和 `processor` 两种配置，支持 CommonMark 和 GitHub Flavored Markdown 格式。
- 📜 **规则列表**：包含多种规则，如 `no-html`、`require-alt-text` 等，部分规则默认启用。
- 🌐 **语言支持**：支持 CommonMark 和 GitHub-Flavored Markdown 两种解析格式。
- 🛠️ **处理器功能**：可从 Markdown 中提取代码块进行单独检查，支持通过文件名元数据指定文件路径。
- 📝 **编辑器集成**：VSCode 的 `vscode-eslint` 插件已内置支持 Markdown 处理器。
- 🔧 **贡献指南**：提供详细的贡献步骤，遵循 ESLint 的贡献规范。
- 💖 **赞助支持**：项目由多个公司和组织赞助，支持持续维护和开发。

---

### [GitHub - jakubfiala/atrament: 一个小巧的 JS 库，用于在 HTML Canvas 上实现精美的绘图与手写功能。](https://github.com/jakubfiala/atrament)

**原文标题**: [GitHub - jakubfiala/atrament: A small JS library for beautiful drawing and handwriting on the HTML Canvas.](https://github.com/jakubfiala/atrament)

Atrament 是一个用于在 HTML Canvas 上进行美观绘图和手写的轻量级 JavaScript 库。它旨在提供自然流畅的绘图体验，并直接绘制到画布上，类似于墨水笔在纸上作画。

- 🎨 **功能特点**：支持绘图、填充和擦除模式，可调节的平滑度和线条粗细，以及颜色设置。
- 📦 **安装方式**：通过 npm 安装，适用于 rollup 或 webpack 等打包工具。
- 🖌️ **使用方法**：创建 canvas 元素并通过 Atrament 实例进行初始化，支持多种配置选项。
- 🔄 **事件跟踪**：提供多种事件监听，如笔画开始/结束、填充开始/结束等，支持笔画记录和程序化绘图。
- 📝 **数据模型**：将输出建模为独立的笔画，每个笔画包含多个段，记录位置、时间和压力数据。
- 🔧 **开发与演示**：提供本地开发指南和演示应用，可通过简单的 HTTP 服务器运行。
- ⚠️ **注意事项**：从版本 4 开始，仅支持现代浏览器，旧版浏览器需使用版本 3。
- 📜 **许可证**：采用 MIT 许可证，代码开源且免费使用。

---

### [GitHub - xojs/xo: ❤️ 提供优秀默认配置的 JavaScript/TypeScript 代码检查工具（基于 ESLint）](https://github.com/xojs/xo)

**原文标题**: [GitHub - xojs/xo: ❤️ JavaScript/TypeScript linter (ESLint wrapper) with great defaults](https://github.com/xojs/xo)

XO 是一个基于 ESLint 的 JavaScript/TypeScript 代码检查工具，提供开箱即用的优秀默认配置，旨在简化代码风格的统一和优化。

- 🚀 **特点**：零配置但可定制，支持 TypeScript，包含多种 ESLint 插件，如 unicorn、import 等。
- 🔧 **功能**：自动修复问题 (`--fix`)、缓存提升性能、支持编辑器插件和 Prettier 集成。
- 📝 **默认代码风格**：Tab 缩进、分号、单引号、多行尾随逗号、严格相等 (`===`) 等。
- ⚙️ **配置**：通过 `xo.config.js` 或 `package.json` 配置，支持覆盖默认规则。
- 🔄 **工作流**：推荐本地安装并通过 `npm init xo` 快速集成到项目。
- ❓ **常见问题**：解释了与 Standard 和 ESLint 的区别，强调 XO 的灵活性和易用性。
- 🌟 **相关资源**：提供了编辑器插件、构建系统插件和各种配置的链接。
- 📌 **团队与支持**：由社区维护，支持通过 Twitter 和 GitHub 获取帮助。

---

### [发布 v0.17.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.17.0)

**原文标题**: [Release v0.17.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.17.0)

Wasp 语言项目 v0.17.0 版本发布，包含重大变更、新功能、错误修复和小改进。

- ⚠️ **重大变更**：`usernameAndPassword`认证方法中的`login()`函数现在接受包含`username`和`password`的对象，而非单独参数；TypeScript 配置需更新；不再自动生成`favicon.ico`；Express 升级至 v5。  
- 🎉 **新功能**：支持 Railway 一键部署；新增`onAfterEmailVerified`认证钩子；支持 Slack 作为认证提供商；支持 Prisma `Decimal`类型返回；新增客户端环境变量验证和`prismaSetupFn`数据库钩子。  
- 🐞 **错误修复**：修复 OAuth 逻辑竞争条件、未登录时`useAuth()`请求失败、Prisma 文件无模型导致应用无法渲染、Wasp Studio 在 Firefox 中无法使用等问题。  
- 🔧 **小改进**：优化无路由定义的错误提示；TypeScript 支持现代化；支持 Wasp 符号跳转定义；改进`userSignupFields`类型传播；生成服务器代码前进行类型检查；`package.json`应用名称改为 kebab case；改进`npm`版本错误处理。  
- 🙏 **社区贡献者**：感谢@0xTaneja、@Scorpil、@Reikon95 的贡献。

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

概述总结  
Wasp 是一个类似 Rails 的全栈 Web 应用开发框架，支持 React、Node.js 和 Prisma，旨在快速构建和部署应用。它通过简单的配置文件和高阶功能（如全栈身份验证、类型安全、RPC 等）显著减少样板代码，同时保持开发者在熟悉技术栈中的灵活性。  

- 🚀 **快速开发** - 类似 Rails 的框架，支持 React、Node.js 和 Prisma，一天内完成应用并一键部署。  
- 🔐 **全栈身份验证** - 几行代码即可集成 Google、GitHub 或邮箱登录，无第三方锁定。  
- 🔄 **类型安全 RPC** - 自动生成跨客户端和服务器的类型安全代码，简化数据交互。  
- ☁️ **简单部署** - 提供 CLI 工具支持主流平台，轻松部署应用。  
- ⏳ **后台任务** - 支持定义、调度和重试持久化任务，如延迟任务。  
- 📧 **邮件发送** - 集成邮件服务提供商即可发送邮件。  
- 🛡️ **全栈类型安全** - 全面支持 TypeScript，自动生成类型定义。  
- 🧩 **更多功能** - 自定义 API 路由、数据库填充、乐观更新等。  
- 🛠️ **工作原理** - 通过`.wasp`配置文件和现有代码生成完整应用源码，减少样板代码。  
- ❤️ **开源社区** - 完全开源，欢迎贡献，用户反馈积极。  
- 🏗️ **案例展示** - 提供 Todo 应用、CoverLetterGPT 等示例，展示实际应用场景。  
- 🏆 **用户评价** - 开发者称赞其高效和易用性，适合快速构建全栈应用。  
- 📅 **持续更新** - 公开路线图，功能不断迭代。  
- ❓ **常见问题** - 解答与其他框架的差异、学习难度和技术栈支持等问题。

---

### [发布 v6.4.0 · tinyplex/tinybase · GitHub](https://github.com/tinyplex/tinybase/releases/tag/v6.4.0)

**原文标题**: [Release v6.4.0 · tinyplex/tinybase · GitHub](https://github.com/tinyplex/tinybase/releases/tag/v6.4.0)

tinybase 发布了 v6.4.0 版本，新增了对 React Native SQLite 数据库的支持模块。

- 🆕 新增了 `persister-react-native-sqlite` 模块，支持通过 `react-native-sqlite-storage` 库在 React Native 中使用 SQLite 数据库持久化数据。  
- 📱 使用示例展示了如何启用 Promise、打开数据库、创建存储并保存到数据库。  
- 🔄 开发者可以通过简单的 API 调用实现数据存储功能，并提供了反馈渠道。  
- 🚀 版本由 jamesgpearce 于 7 月 10 日发布，包含其他未详细说明的更新。

---

### [更新日志 - express-rate-limit](https://express-rate-limit.mintlify.app/reference/changelog)

**原文标题**: [Changelog - express-rate-limit](https://express-rate-limit.mintlify.app/reference/changelog)

express-rate-limit 是一个用于 Express 应用的限流中间件，记录所有用户可见的变更，遵循语义化版本控制。

- 🛠️ **8.0.1 修复**：修复了 CommonJS 构建中的 `ipKeyGenerator` 导出问题，并修正了 Express 类型引用。
- 🔄 **8.0.0 重大变更**：默认将 IPv6 地址掩码为 /56 子网，防止用户通过迭代 ISP 分配的子网绕过限流。
- 📝 **7.5.0 新增**：实现了 IETF RateLimit 标头规范的第八草案，新增 `identifier` 选项和 `headersDraftVersion` 验证检查。
- 🚀 **7.4.0 新增**：添加 `passOnStoreError` 选项，允许在后端错误时“开放失败”。
- 🔧 **7.3.0 新增**：新增 `unsharedStore` 验证检查，防止多个限流器共享单个存储实例。
- 📊 **7.2.0 新增**：新增 `creationStack` 验证检查，识别在请求处理程序中创建的实例。
- 🔄 **7.0.0 重大变更**：`max: 0` 现在会阻止所有请求，重命名 `req.rateLimit.current` 为 `req.rateLimit.used`，最低 Node 版本要求提升至 v16。
- 📉 **6.11.0 新增**：支持从存储中检索给定键的当前命中计数和重置时间。
- 📜 **6.10.0 新增**：支持 IETF 标准的 RateLimit 标头，新增 `standardHeaders: 'draft-7'` 选项。
- 🛑 **6.0.0 重大变更**：重命名 `draft_polli_ratelimit_headers` 为 `standardHeaders`，移除 `delayMs` 和 `delayAfter` 选项，最低 Node 版本要求提升至 12.9.0。
- 📦 **5.x 变更**：移除 TypeScript 类型定义，简化默认处理函数。
- 🔄 **4.x 变更**：不再修改传入的选项对象，而是创建其克隆。
- 🗑️ **3.x 移除**：移除 `delayAfter` 和 `delayMs` 选项，这些功能已移至 `express-slow-down` 包。
- 📌 **2.x 新增**：支持外部存储，新增 `limiter.resetKey()` 方法重置特定客户端的命中计数器。

---

### [twgl.js/变更列表.md 位于 main · greggman/twgl.js · GitHub](https://github.com/greggman/twgl.js/blob/main/CHANGELIST.md#change-list)

**原文标题**: [twgl.js/CHANGELIST.md at main · greggman/twgl.js · GitHub](https://github.com/greggman/twgl.js/blob/main/CHANGELIST.md#change-list)

概述：这是一个 GitHub 仓库页面，展示了 twgl.js 项目的相关信息，包括代码、问题、讨论等部分，但页面加载时出现了错误提示。

- 🚀 项目名称：twgl.js  
- 🌟 星标数：2.9k  
- 🍴 复刻数：264  
- 🐛 问题数：52  
- 🔄 拉取请求：1  
- ⚠️ 错误提示：页面加载时出现错误，建议重新加载  
- 📂 导航选项：代码、问题、拉取请求、讨论、操作、项目、Wiki、安全、洞察等

---

### [TWGL.js，一个轻量级 WebGL 辅助库](http://twgljs.org/)

**原文标题**: [TWGL.js, a tiny WebGL helper library](http://twgljs.org/)

TWGL 是一个简化 WebGL API 使用的轻量级库，旨在减少代码冗余，提供核心功能封装，同时保持底层灵活性。

- 🎯 **核心目标**：减少 WebGL 的冗余代码，提供简洁的封装，但不替代 three.js 等高级库。  
- 🛠️ **核心功能**：  
  - `twgl.createProgramInfo`：编译着色器并创建属性和 uniform 的设置器。  
  - `twgl.createBufferInfoFromArrays`：创建缓冲区和属性配置。  
  - `twgl.setBuffersAndAttributes`：绑定缓冲区并设置属性。  
  - `twgl.setUniforms`：设置 uniform 变量。  
  - `twgl.createTextures`：创建多种纹理。  
  - `twgl.createFramebufferInfo`：创建帧缓冲和附件。  
- 📊 **代码对比**：TWGL 大幅简化 WebGL 操作（如着色器编译、缓冲设置、纹理加载等），示例中代码量减少 50% 以上。  
- 🌐 **支持环境**：  
  - ES6 模块、AMD、CommonJS/Browserify。  
  - 提供完整版（含数学函数和基本图元生成）和最小版。  
- 📥 **下载方式**：GitHub、Bower、npm（`twgl.js` 或 `twgl-base.js`）。  
- 🔍 **设计理念**：  
  - 不封装 WebGL 底层，允许与原生 API 混用。  
  - 类似 TDL 的“无类”设计，手动构建数据结构。  
- 📚 **文档与学习**：  
  - API 文档独立提供。  
  - 推荐 [webglfundamentals.org](https://webglfundamentals.org) 学习 WebGL。  
- 🚀 **示例应用**：包括立方体渲染、纹理、动态缓冲、GPGPU 粒子等。

---

### [BladewindUI：基于 Laravel Blade 的超简洁优雅 UI 组件库，采用 TailwindCSS 与原生 Javascript](https://bladewindui.com/)

**原文标题**: [BladewindUI: Super simple but elegant Laravel blade-based UI component library using TailwindCSS and vanilla Javascript](https://bladewindui.com/)

BladewindUI 是一个为 Laravel 应用设计的 UI 组件库，提供丰富的组件和功能，支持暗黑模式，完全免费且开源。

- 🚀 **安装简单**：通过 `composer require mkocansey/bladewind` 即可快速安装使用。
- 🎨 **多样化组件**：包含 Accordion、Alert、Avatar、Button、Card 等众多 UI 组件。
- 🌙 **暗黑模式支持**：轻松自定义暗黑模式配色方案。
- 🔄 **版本更新**：当前版本为 v3.1.0，提供持续的功能更新和改进。
- 💡 **功能丰富**：支持表单控件（Input、Checkbox、Select）、图表（Chart、Progress Bar）、通知（Notification、Bell）等。
- 📊 **数据展示**：提供 Table、Statistic、Timeline 等组件，方便数据可视化。
- 🛠 **自定义工具**：包含 Theme Switcher、Colorpicker、Filepicker 等工具，满足个性化需求。
- 📱 **响应式布局**：适配不同设备，支持 App Layouts 和 Helper Functions。
- 📜 **文档完善**：提供详细的安装、定制和组件使用文档，支持 Light/Dark/System 主题切换。
- 🤝 **社区支持**：鼓励贡献，提供 Roadmap 和 Contribution Guide，开源在 GitHub。
- 🆓 **完全免费**：所有组件及未来更新均免费，无付费计划。

---

### [GitHub - mapbox/concaveman: 一个非常快速的 JavaScript 二维凹壳算法](https://github.com/mapbox/concaveman)

**原文标题**: [GitHub - mapbox/concaveman: A very fast 2D concave hull algorithm in JavaScript](https://github.com/mapbox/concaveman)

这是一个关于 JavaScript 库`concaveman`的概述，该库用于快速计算 2D 点集的凹包（凹壳）。

- 🚀 **快速算法**：`concaveman`是一个非常快速的 2D 凹包算法，基于 JavaScript 实现。
- 📜 **许可证**：采用 ISC 许可证发布。
- ⭐ **受欢迎程度**：拥有 686 颗星和 84 个分支。
- 📦 **依赖项**：依赖`rbush`、`tinyqueue`、`point-in-polygon`和`robust-predicates`等库。
- 📐 **参数可调**：支持调整凹度（concavity）和长度阈值（lengthThreshold）以控制输出形状的复杂度。
- 📚 **算法来源**：基于 2012 年 Jin-Seo Park 和 Se-Jong Oh 的论文，但性能显著提升至 O(n log n)。
- 🛠 **多语言支持**：2019 年推出了 C++ 端口，支持从 C/C++、Python 等语言调用。
- 📖 **TypeScript 支持**：通过`@types/concaveman`提供类型定义。
- 🔍 **使用场景**：适用于需要生成点集大致轮廓的场景。

---

### [发布 v8.8.0 · mui/mui-x · GitHub](https://github.com/mui/mui-x/releases/tag/v8.8.0)

**原文标题**: [Release v8.8.0 · mui/mui-x · GitHub](https://github.com/mui/mui-x/releases/tag/v8.8.0)

MUI-X 发布了 v8.8.0 版本，包含多项功能更新、问题修复和本地化支持，特别感谢 13 位贡献者的努力。

- 🚀 **版本发布**：MUI-X v8.8.0 正式发布，包含 50 次提交至 master 分支。  
- 🌍 **本地化支持**：新增印尼语（id-ID）本地化支持。  
- 📊 **图表功能增强**：  
  - 新增图表缩放预览功能。  
  - 优化轴高亮控制和默认域限制。  
  - 新增漏斗方向控制和导出前回调。  
- 🛠 **数据网格修复**：  
  - 修复了`useGridSelector`在严格模式下的订阅问题。  
  - 修正滚动条填充的`z-index`问题。  
  - 优化分页禁用时的数据源缓存块大小。  
- 🌳 **树视图改进**：修复了懒加载和复选框启用时的滚动问题。  
- 📚 **文档更新**：  
  - 新增独立金字塔图表页面。  
  - 优化移动端条形图示例。  
  - 改进图表概览页面。  
- 🤝 **社区贡献**：特别感谢@kennarddh 等社区成员的贡献。  
- 🔧 **基础设施**：修复 CI 问题并优化 Prettier 配置解析。

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=july18th2025)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=july18th2025)

Meticulous AI 提供了一种无需编写或维护测试的自动化测试解决方案，通过记录用户交互并生成持续演化的测试套件，覆盖应用程序的所有边缘情况，帮助团队快速、可靠地发布代码。

- 🚀 **无需编写测试** - Meticulous AI 自动生成并维护测试套件，覆盖所有用户流程和边缘情况。  
- 🔍 **记录用户交互** - 通过在开发、预发布和生产环境中添加脚本标签，记录用户会话以生成测试用例。  
- 🤖 **AI 驱动测试** - AI 引擎分析代码分支，生成可视化端到端测试，确保每一行代码都被覆盖。  
- ⚡ **快速反馈** - 在合并代码前查看 PR 对用户流程的影响，避免回归问题。  
- 🛠️ **无副作用测试** - 通过模拟后端响应，避免因数据变化导致的误报，无需设置测试账户或模拟数据。  
- 🔄 **自动演化** - 测试套件随应用程序的更新自动调整，无需人工干预。  
- 🚀 **高效并行测试** - 支持大规模并行测试，数千个测试可在 120 秒内完成。  
- 💡 **广泛集成** - 支持多种前端框架（如 NextJS、React、Vue、Angular 等），几分钟即可完成设置。  
- 📢 **用户证言** - Dropbox、Notion 和 Lattice 等 100 多家组织已采用，显著提升开发效率和代码质量。  
- 🔒 **安全可靠** - 从底层消除测试中的不稳定因素，确保测试结果准确无误。

---

### [Node 周刊](https://nodeweekly.com/)

**原文标题**: [Node Weekly](https://nodeweekly.com/)

Node Weekly 是一份免费的每周电子邮件简报，专注于 Node.js 的新闻和文章。  

- 📧 免费订阅：每周通过电子邮件发送 Node.js 相关资讯和文章  
- � 订阅人数：62,555 位订阅者  
- 📜 期刊数量：已发布 586 期  
- 📡 支持 RSS 订阅  
- 🔍 提供最新一期样本供参考  
- 🏢 由 Cooperpress 发布  
- 🔒 严格的隐私政策：包括反垃圾邮件和 GDPR 合规  
- ® Node.js 是 Joyent, Inc 的注册商标，经授权使用

---

### [Git 快速统计：一种简单高效获取 Git 仓库各类统计信息的方法](https://git-quick-stats.sh/)

**原文标题**: [Git quick statistics is a simple and efficient way to access various statistics in git repository.](https://git-quick-stats.sh/)

概述总结  
git-quick-stats 是一个多功能工具，用于快速访问 Git 仓库的统计数据，支持跨平台使用，并提供交互式和非交互式操作模式。  

- 🚀 **快速开始**：提供简单的安装方式和直接安装命令。  
- 💻 **跨平台支持**：兼容 Windows、Linux、macOS 和 Docker。  
- 📊 **贡献统计**：展示仓库贡献者列表和代码审查推荐人选。  
- 📜 **变更日志**：轻松获取 Git 变更日志和按作者分类的日志。  
- ⚙️ **非交互式使用**：支持命令行参数直接执行特定功能。  
- 📅 **时间统计**：按日、月、星期、小时等维度查看提交记录。  
- 🌳 **分支信息**：显示分支树状图和按日期排序的分支列表。  
- 📂 **路径排除**：支持通过路径规范排除特定目录或文件。  
- 🎨 **主题切换**：提供默认和传统两种颜色主题可选。  
- 📄 **文档支持**：支持设置时间范围、输出限制和合并提交查看策略。  
- 📜 **开源许可**：基于 MIT 许可证，完全免费和开源。

---

### [2025 年：仅用 24 小时多一点爬取十亿网页](https://andrewkchan.dev/posts/crawler.html)

**原文标题**: [Crawling a billion web pages in just over 24 hours, in 2025](https://andrewkchan.dev/posts/crawler.html)

概述总结  
作者在 2025 年用 24 小时爬取了 10 亿个网页，探讨了现代网络爬虫的技术挑战与优化方案，并与 2012 年的基准数据对比，分析了硬件、软件及网络环境的变化对爬虫效率的影响。  

- 🚀 **目标与约束**：24 小时内爬取 10 亿网页，预算约 500 美元，仅抓取 HTML 内容，遵守 robots.txt 等礼貌原则。  
- 💻 **硬件优化**：使用 12 台 i7i.4xlarge 实例（16 核/128GB 内存/10Gbps 带宽），单机集成 Redis、抓取和解析功能，避免分布式系统复杂性。  
- 🔍 **技术瓶颈**：解析（CPU 密集型）和 SSL 握手（占 CPU 时间 25%）成为主要瓶颈，而非传统认为的网络带宽或 DNS。  
- 📉 **网页变化**：平均网页体积从 2012 年的 51KB 增至 242KB，动态内容增多，但大部分仍可通过静态抓取获取。  
- 💡 **关键优化**：替换解析库（lxml→selectolax）、截断大页面（250KB）、异步高并发设计（单机 6000+ 抓取协程）。  
- ⚠️ **意外挑战**：热门域名（如 Yahoo、Wikipedia）的待爬队列内存爆炸，需手动干预和排除。  
- 📊 **成本对比**：最终花费 462 美元，远低于使用 S3 存储的方案（约 5000 美元），实例存储更经济。  
- 🤖 **未来方向**：动态渲染（如 JS 执行）的爬取成本、样本数据分析（死链/多媒体比例）、对抗云服务反爬措施（如 Cloudflare 按次付费）。  
- 🙏 **致谢**：感谢 Michael Nielsen 等前辈的启发和反馈。

---

### [在 VS Code 中命令 GitHub 的编码助手](https://code.visualstudio.com/blogs/2025/07/17/copilot-coding-agent)

**原文标题**: [Command GitHub's Coding Agent from VS Code](https://code.visualstudio.com/blogs/2025/07/17/copilot-coding-agent)

GitHub Copilot Coding Agent 现已在 VS Code 中集成，支持多代理同时运行，可分配任务给 AI 团队完成代码开发、PR 提交和代码审查等复杂工作。

- 🚀 **多代理并行工作**：VS Code 现支持多个 Copilot Coding Agent 同时运行，提升开发效率。  
- 🤖 **自主 AI 开发者**：代理可处理 GitHub 问题、提交 PR、代码审查，并使用 MCP 工具操作数据库或云服务。  
- ⚙️ **集成工作流**：通过 GitHub Pull Requests 扩展直接在 VS Code 中分配任务，无需切换浏览器。  
- 📊 **进度跟踪**：新增“Copilot on My Behalf”查询，实时查看代理操作记录并可终止任务。  
- 🔄 **交互式审查**：代理提交 PR 后，开发者可直接在 VS Code 中评论并要求迭代修改。  
- 💬 **聊天面板启动**：通过 Copilot Chat 直接委托任务给代理，跳过问题步骤，自动生成详细 PR 描述。  
- 🔧 **未来计划**：包括 PR 性能优化、集成聊天视图、共享自定义指令等，详情可见开源迭代计划。  
- 📥 **立即体验**：安装 GitHub Pull Requests 扩展并启用设置即可使用预览版功能。

---

### [介绍 Amazon S3 Vectors：首个原生支持大规模向量处理的云存储（预览版） | AWS 新闻博客](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-vectors-first-cloud-storage-with-native-vector-support-at-scale/)

**原文标题**: [Introducing Amazon S3 Vectors: First cloud storage with native vector support at scale (preview) | AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-vectors-first-cloud-storage-with-native-vector-support-at-scale/)

AWS 宣布推出 Amazon S3 Vectors 预览版，这是首个支持大规模原生向量存储的云对象存储服务，可将向量数据的上传、存储和查询总成本降低高达 90%。

- 🚀 **成本效益**：Amazon S3 Vectors 通过原生向量支持，显著降低存储和查询成本，降幅可达 90%。  
- 🔍 **向量搜索**：支持生成式 AI 应用中的语义搜索，通过向量表示比较数据相似性。  
- 🗂️ **向量存储结构**：引入向量桶和向量索引，每个桶可容纳 10,000 个索引，每个索引可存储数千万向量。  
- 🔄 **自动优化**：S3 Vectors 自动优化向量数据，确保价格与性能的最佳平衡，适应数据集的扩展和变化。  
- 🤖 **集成服务**：与 Amazon Bedrock Knowledge Bases、Amazon SageMaker Unified Studio 和 Amazon OpenSearch Service 深度集成，支持 RAG 应用和实时低延迟搜索。  
- 🛠️ **操作简便**：通过 AWS CLI、SDK 或 REST API 插入、查询向量，支持元数据过滤和多种距离度量（如余弦或欧几里得）。  
- 🌍 **多区域可用**：预览版已在美东、美西、欧洲和亚太部分区域推出。  
- 📊 **行业应用**：适用于个性化推荐、内容分析和智能文档处理等多种场景。  
- 📚 **学习资源**：提供详细的用户指南和 GitHub 仓库，帮助用户快速上手。  

S3 Vectors 的推出为大规模 AI 应用提供了经济高效的向量存储解决方案，简化了向量数据的管理和查询流程。

---

