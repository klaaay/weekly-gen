### [JavaScript 周刊第 743 期：2025 年 7 月 4 日](https://javascriptweekly.com/issues/743)

**原文标题**: [JavaScript Weekly Issue 743: July 4, 2025](https://javascriptweekly.com/issues/743)

本期《JavaScript Weekly》主要涵盖技术动态、工具更新及实用教程，适合开发者关注前沿趋势与提升技能。

- 🌞 **Deno 2.4 发布**：重新引入`deno bundle`命令，支持 npm/JSR 依赖和自动 Tree-Shaking，内置 OpenTelemetry 稳定化。  
- 🐇 **CodeRabbit 免费 AI 代码审查**：集成 VS Code 等 IDE，提供逐行评审与一键修复功能。  
- 📜 **ECMAScript 2025 新特性**：Pawel Grzybek 对比 Dr. Axel 的观点，提供示例解析。  
- ⚡ **技术简讯**：Ryan Dahl 更新 JavaScript™商标争议；JS1024 代码竞赛主题“Creepy”；Angular 投票截止日。  
- 🛠️ **工具更新**：Rspack 1.4 支持 WebAssembly；Electron 37.0；ESLint 9.30 等版本发布。  
- 🎨 **教程与案例**：  
  - 构建 AI 驱动的颜色搜索引擎（Lúí Smyth）  
  - 使用 JS Proxy 实现轻量响应式状态管理（Loren Stewart）  
  - Next.js 15 全栈开发指南（Robin Wieruch 赞助）  
- 🤔 **趣味挑战**：Hillel Wayne 的 14 字符 JS 解析谜题引发热议。  
- 📦 **新工具推荐**：  
  - Milkdown 插件化 Markdown 编辑器  
  - Repomix 将代码库转为 AI 友好格式  
  - Spectral.js 基于绘画理论的色彩混合库  
- 🔍 **生态动态**：Patreon 国际化重构案例、Cloudflare Containers 上线、GitHub 提交漏洞赏金故事。

---

### [Deno 2.4：deno bundle 回归 | Deno](https://deno.com/blog/v2.4)

**原文标题**: [Deno 2.4: deno bundle is back | Deno](https://deno.com/blog/v2.4)

Deno 2.4 版本发布，重新引入了 `deno bundle` 命令，并新增多项功能改进，包括导入文本和字节、内置 OpenTelemetry 稳定化、环境变量管理优化等。

- 🚀 **Deno 2.4 发布**：支持通过 `deno upgrade` 升级，新增多项功能改进。
- 🔄 **`deno bundle` 回归**：支持将 JavaScript 或 TypeScript 打包为单文件，支持 npm 和 JSR 依赖，自动树摇和压缩。
- 📝 **导入文本和字节**：通过 `--unstable-raw-imports` 标志，可直接导入文本、字节等非 JavaScript 文件。
- 📊 **内置 OpenTelemetry 稳定化**：无需 `--unstable-otel` 标志，简化项目可观测性。
- 🛠 **新 `--preload` 标志**：允许在主脚本执行前运行代码，适用于修改全局变量或预加载数据。
- 🔄 **依赖管理优化**：新增 `deno update` 命令，简化依赖更新流程。
- 📈 **覆盖率收集改进**：`deno run --coverage` 支持子进程覆盖率收集，提升测试覆盖率报告的完整性。
- 🔧 **环境变量 `DENO_COMPAT=1`**：简化兼容性标志管理，提升与 Node.js 项目的兼容性。
- 🔒 **权限管理增强**：`--allow-net` 支持子域名通配符和 CIDR 范围，新增 `--deny-import` 标志限制导入来源。
- 📦 **`package.json` 条件导出支持**：提升与 npm 生态的兼容性，支持 React Server Components 等场景。
- 🖥 **`deno run` 裸说明符支持**：简化 `deno.json` 中配置的模块直接运行。
- ✨ **`deno fmt` 支持 XML 和 SVG**：自动格式化 XML 和 SVG 文件，提升开发体验。
- 🔧 **`tsconfig.json` 支持改进**：更好地支持前端框架如 Vue、Svelte 等。
- 🌐 **Node.js 全局变量简化**：`Buffer`、`global` 等全局变量对所有代码可用，减少兼容性问题。
- 📂 **本地 npm 包支持**：`deno.json` 中的 `patch` 选项更名为 `links`，提升本地开发体验。
- 🛠 **Node.js API 支持增强**：新增 `glob` API 支持，多个模块兼容性超过 95%。
- 🛠 **LSP 改进**：提升自动导入、配置处理等功能的用户体验。
- 🎨 **其他有趣功能**：`fetch` 支持 Unix 和 Vsock 套接字，`deno serve` 新增 `onListen` 回调，Jupyter 内核管理优化等。
- 🙏 **致谢**：感谢社区贡献者的支持和反馈。

---

### [Deno 2.4：deno bundle 功能回归 | Deno](https://deno.com/blog/v2.4#importing-text-and-bytes)

**原文标题**: [Deno 2.4: deno bundle is back | Deno](https://deno.com/blog/v2.4#importing-text-and-bytes)

Deno 2.4 版本发布，重新引入了 `deno bundle` 命令，并新增多项功能改进，包括导入文本和字节、内置 OpenTelemetry 稳定化、环境变量管理优化等。

- 🎉 **Deno 2.4 发布**：支持升级或安装，提供 Shell 和 PowerShell 安装命令。  
- 🔄 **`deno bundle` 回归**：支持单文件打包，自动树摇和压缩，适用于服务器和浏览器。  
- 📄 **导入文本和字节**：通过 `--unstable-raw-imports` 标志直接导入文本、二进制文件等资源。  
- 📊 **内置 OpenTelemetry 稳定化**：无需 `--unstable-otel` 标志，简化项目可观测性。  
- ⚙️ **新 `--preload` 标志**：允许在运行主脚本前执行代码，适合自定义运行时环境。  
- 🔄 **依赖管理优化**：新增 `deno update` 命令，简化依赖更新流程。  
- 📊 **覆盖率收集改进**：`deno run --coverage` 支持子进程覆盖率收集。  
- 🌐 **`DENO_COMPAT=1` 环境变量**：简化 Node.js 兼容性标志管理。  
- 🔒 **权限控制增强**：`--allow-net` 支持子域名通配符和 CIDR 范围，新增 `--deny-import` 标志。  
- 📦 **`package.json` 条件导出**：支持 npm 包的条件导出，如 React Server Components。  
- 🏃 **裸说明符支持**：`deno run` 可直接运行 `deno.json` 中定义的导入别名。  
- ✨ **格式化支持扩展**：`deno fmt` 新增对 XML、SVG 和 Mustache 文件的支持。  
- 🔧 **TypeScript 配置改进**：更好地支持 `tsconfig.json` 的 `references`、`extends` 等选项。  
- 🌍 **Node.js 全局变量简化**：`Buffer`、`global` 等全局变量默认可用，减少兼容性配置。  
- 📂 **本地 npm 包支持**：`deno.json` 中的 `links` 选项替代 `patch`，支持本地包链接。  
- 🛠️ **Node.js API 增强**：新增 `glob` API，提升多个模块兼容性至 95% 以上。  
- 🚀 **LSP 改进**：优化自动导入、配置处理和大型文件格式化性能。  
- 🎉 **其他有趣功能**：`fetch` 支持 Unix 和 Vsock 套接字，`deno serve` 新增 `onListen` 回调，Jupyter 内核管理增强等。  
- 🙏 **致谢**：感谢社区贡献者的支持和反馈。  

Deno 2.4 带来了更多功能和改进，提升开发体验和性能。

---

### [Bun v1.2.18 | Bun 博客](https://bun.sh/blog/bun-v1.2.18)

**原文标题**: [Bun v1.2.18 | Bun Blog](https://bun.sh/blog/bun-v1.2.18)

Bun 是一个用于构建和测试全栈 JavaScript 和 TypeScript 应用程序的完整工具包。本次更新修复了 52 个问题，并带来了多项新功能和改进。

- 🚀 **Bun 1.0 发布**：Bun 是一个完整的 JavaScript 和 TypeScript 工具包，适合全栈开发。
- 🛠️ **ReadableStream 新方法**：支持直接调用 `.text()`, `.json()`, `.bytes()`, `.blob()`，无需包装为 `Response` 对象。
- 📡 **WebSocket 客户端压缩**：支持 `permessage-deflate` 扩展，减少网络带宽使用。
- 📉 **减少内存使用**：优化 `fetch()` 和 `S3` 上传时的内存占用，实现更好的背压处理。
- 📦 **支持 `$NODE_PATH`**：Bun 的打包工具现在支持 `NODE_PATH` 环境变量，用于模块解析。
- 🧪 **测试改进**：`bun test` 现在会在没有匹配测试时失败，避免日志中显示大量跳过的测试。
- 🔄 **版本管理**：`bun pm version` 可以方便地更新 `package.json` 中的版本号。
- ⚡ **安装速度提升**：对于使用 `node-gyp` 的包，`bun install` 速度提升高达 2.5 倍。
- ➕ **新增 `Math.sumPrecise`**：提供高精度数字求和，适用于财务计算等场景。
- 🔄 **Node.js 兼容性改进**：Bun 现在报告为 Node.js v24.3.0，提升与原生模块的兼容性。
- 🚄 **性能优化**：`napi_create_buffer` 和字符串处理速度提升，减少内存使用。
- 📂 **`fs.glob` 默认匹配目录**：与 Node.js 行为一致，不再需要设置 `onlyFiles: false`。
- 🛑 **错误处理改进**：`net.createConnection()` 现在会验证 `options.host`，`http.ClientRequest#flushHeaders` 正确发送请求体。
- 🔧 **Bug 修复**：包括 `fs.watchFile` 忽略访问时间、`bun:sqlite` 升级到 SQLite 3.50.2 等多项修复。
- 📥 **安装与升级**：支持多种安装方式（curl、npm、PowerShell、scoop、brew、docker），升级命令为 `bun upgrade`。

---

### [ECMAScript 2025 新特性 | pawelgrzybek.com](https://pawelgrzybek.com/whats-new-in-ecmascript-2025/)

**原文标题**: [What's new in ECMAScript 2025 | pawelgrzybek.com](https://pawelgrzybek.com/whats-new-in-ecmascript-2025/)

ECMAScript 2025 引入了多项新特性，包括正则表达式命名捕获组的重复使用、Set 新增方法、正则表达式子模式修饰符、导入属性、迭代器辅助方法、Promise.try()、Float16Array 以及正则表达式转义功能等。

- 🆕 ECMAScript 2025 新特性发布，TC39 已批准  
- 🔄 允许正则表达式中重复使用命名捕获组，如 `/(?<version>[0-9]{4})|(?<version>[0-9]{2})/`  
- 🛠 Set 新增方法：`intersection`、`union`、`difference`、`symmetricDifference` 等  
- 🎛 正则表达式支持子模式修饰符，如 `/(?i:bearer) abc/` 可局部忽略大小写  
- 📥 导入属性支持 JSON 模块，如 `import data from "./data.json" with { type: "json" }`  
- 🔄 迭代器辅助方法新增 `map`、`filter`、`take`、`drop` 等，类似数组方法  
- 🤝 `Promise.try()` 简化同步/异步操作的 Promise 封装  
- � 新增 `Float16Array`，适用于内存受限的图形计算场景  
- 🛡 `RegExp.escape()` 提供正则表达式字符串转义功能，避免特殊字符误匹配  
- ™ JavaScript 商标归 Oracle 所有，Deno 发起请愿争取自由使用

---

### [Ecma 国际批准 ECMAScript 2025：有哪些新变化？](https://2ality.com/2025/06/ecmascript-2025.html)

**原文标题**: [Ecma International approves ECMAScript 2025: What’s new?](https://2ality.com/2025/06/ecmascript-2025.html)

ECMA 国际已批准 ECMAScript 2025 语言规范，正式成为标准。以下是新特性的概述：

- 🎉 **ECMAScript 2025 获批**：2025 年 6 月 25 日，第 129 届 Ecma 大会批准了新规范。  
- 📥 **导入属性和 JSON 模块**：支持通过`import with`语法导入非 JavaScript 资源（如 JSON）。  
- 🔄 **迭代器辅助方法**：新增`filter`、`map`、`drop`等方法，支持惰性计算和跨数据结构操作。  
- 🔍 **新 Set 方法**：包括集合运算（`union`、`intersection`）和关系检查（`isSubsetOf`）。  
- 🛡️ **RegExp.escape()**：转义文本以安全用于正则表达式。  
- 🏷️ **正则表达式内联标志**：局部应用标志（如`i`）到部分模式。  
- 📛 **重复命名捕获组**：允许在不同分支使用相同组名。  
- ⏳ **Promise.try()**：以同步或异步代码启动 Promise 链。  
- 🔢 **16 位浮点数支持**：新增`Float16Array`和`Math.f16round()`等 API。  
- 📚 **免费电子书**：作者提供在线书籍《Exploring JavaScript (ES2025 Edition)》详解新特性。  

编辑团队包括 Shu-yu Guo、Michael Ficarra 和 Kevin Gibbons。

---

### [JavaScript™ 商标更新 | Deno](https://deno.com/blog/deno-v-oracle4)

**原文标题**: [JavaScript™ Trademark Update | Deno](https://deno.com/blog/deno-v-oracle4)

JavaScript 商标争议更新：Ryan Dahl 对 TTAB 驳回针对 Oracle 的欺诈指控表示不满，案件将聚焦于“通用性”和“弃用”核心诉求，预计 8 月进入关键阶段。

- 🚨 TTAB 驳回了对 Oracle 的欺诈指控，Ryan Dahl 表示反对  
- 🤬 Oracle 在 2019 年商标续展中使用了 Node.js 网站截图作为证据，引发争议  
- ⚖️ 案件核心转向“JavaScript”是否为通用术语及商标是否被弃用  
- 📅 8 月 7 日前 Oracle 需回应撤销商标请愿，9 月 6 日进入证据开示阶段  
- 🌍 19,550 人联署 javascript.tm 支持“JavaScript”应归属公众  
- ✨ 胜诉或 Oracle 主动放弃商标将使 JavaScript 彻底自由化

---

### [机器人验证](https://js1024.fun/)

**原文标题**: [Bot Verification](https://js1024.fun/)

验证中，请确认您不是机器人...  

- 🔍 系统正在验证用户身份  
- 🤖 检测是否为自动化程序或机器人  
- ✅ 通过后即可继续访问或操作  
- ⏳ 可能需要短暂等待验证完成

---

### [RFC - Angular 官方吉祥物 · angular/angular · 讨论 #61733 · GitHub](https://github.com/angular/angular/discussions/61733)

**原文标题**: [RFC - Angular official mascot · angular/angular · Discussion #61733 · GitHub](https://github.com/angular/angular/discussions/61733)

Angular 社区正在讨论为其选择一个官方吉祥物，目前有三个候选方案，并鼓励社区成员参与投票和提出建议。

- 🛡️ **提案 1 - 角形角色**：灵感来自 Angular 的 logo，形象抽象、锐利且友好，头盔设计让人联想到超级英雄。  
- 🐠 **提案 2 - 鮟鱇鱼**：象征智慧与适应力，设计虽源自深海恐怖鱼类，但造型可爱化。  
- 🎨 **提案 3 - 鮟鱇鱼变体**：提案 2 的衍生版本，细节略有调整。  

- 🎯 **目标**：选择代表 Angular 价值观的吉祥物，提升社区凝聚力，并制定使用规范。  
- ❌ **非目标**：替代现有 Angular 盾牌 Logo，或仓促决定设计。  

- 💬 **社区互动**：成员可通过表情符号投票（1️⃣/2️⃣/3️⃣），或提出命名建议（如"Angie"）。  
- ⚠️ **注意事项**：讨论需遵守社区行为准则，确保包容性。  

- 📅 **后续步骤**：收集反馈后，设计团队将迭代最终方案并于数月内公布结果。  

- 😆 **趣味讨论**：部分用户调侃鮟鱇鱼的真实照片"吓人"，而提案 1 因关联 AngularJS 的"超级英雄"主题获高票支持。

---

### [Angular 自定义性能分析工具现已发布 | Angular | 2025 年 7 月 | Angular 博客](https://blog.angular.dev/the-angular-custom-profiling-track-is-now-available-0f9d8d36218a?gi=3e03dcb142c0)

**原文标题**: [The Angular Custom Profiling Track is now available | by Angular | Jul, 2025 | Angular Blog](https://blog.angular.dev/the-angular-custom-profiling-track-is-now-available-0f9d8d36218a?gi=3e03dcb142c0)

Angular 与 Chrome 团队合作，在 Chrome DevTools 性能面板中新增了 Angular 自定义性能分析轨道，为开发者提供了统一的性能分析体验，结合了 Angular 框架概念和 Chrome 详细函数调用分析的优势。

- 🚀 **新功能发布**：Angular 自定义性能分析轨道现已可用，集成于 Chrome DevTools 性能面板中。  
- 🔧 **解决痛点**：传统工具（Chrome 性能面板和 Angular DevTools）数据割裂，新功能提供统一视图。  
- 📊 **核心特性**：火焰图按 Angular 概念（如组件、生命周期钩子）分组代码执行，支持颜色标注和交互式钻取。  
  - 🟢 **绿色**：开发者编写的代码（如 DI 服务实例化）。  
  - 🟣 **紫色**：Angular 编译后的模板代码。  
  - 🔵 **蓝色**：入口点（如用户交互触发的组件更新）。  
- 🛠️ **启用步骤**：  
  1. 使用 Angular v20+ 和最新 Chrome 浏览器。  
  2. 开发模式下运行应用，在控制台输入`ng.enableProfiling()`。  
  3. 录制性能分析时即可看到“Angular”专属轨道。  
- 🌟 **目标**：通过更直观的性能洞察，帮助开发者构建更高效的 Angular 应用。

---

### [开源 AI 编辑器：首个里程碑](https://code.visualstudio.com/blogs/2025/06/30/openSourceAIEditorFirstMilestone)

**原文标题**: [Open Source AI Editor: First Milestone](https://code.visualstudio.com/blogs/2025/06/30/openSourceAIEditorFirstMilestone)

VS Code 团队宣布 GitHub Copilot Chat 扩展已开源，这是实现开源 AI 编辑器计划的首个里程碑，旨在促进社区创新和数据透明度。未来计划将该扩展功能整合至 VS Code 核心代码库，并与开源 AI 社区合作优化体验。

- 🎯 **首个里程碑达成**：GitHub Copilot Chat 扩展现已在 GitHub 上以 MIT 许可证开源。  
- 💡 **开源动机**：推动社区创新、增强数据透明度，延续 VS Code 开源成功模式。  
- 🔍 **探索与贡献**：开发者可查看代码实现细节（如代理模式、LLM 上下文处理等），并提交 PR 或反馈问题。  
- 🛠 **未来计划**：逐步将扩展功能重构至 VS Code 核心，后续或开源原 Copilot 扩展的补全功能。  
- 🤝 **社区合作**：携手开源 AI 社区，优化性能、扩展性和用户体验。  
- ❓ **更多信息**：可通过 FAQ 或 vscode 代码库提交问题获取详情。

---

### [宣布 Rspack 1.4 - Rspack](https://rspack.rs/blog/announcing-1-4)

**原文标题**: [Announcing Rspack 1.4 - Rspack](https://rspack.rs/blog/announcing-1-4)

Rspack 1.4 版本发布，带来多项新功能和性能优化，包括浏览器运行支持、更快的 SWC、更小的打包体积、默认增量构建等，同时介绍了 Rstack 生态系统的进展和升级指南。

- 🚀 **Rspack 1.4 发布**：新增多项功能，包括浏览器运行支持、更快的 SWC、更小的打包体积等。
- 🌐 **浏览器运行支持**：新增 Wasm 目标支持，可在浏览器环境中运行，支持在线平台如 StackBlitz。
- ⚡ **更快的 SWC**：JavaScript 解析器速度提升 30%-35%，压缩器速度提升 10%。
- 📦 **更小的打包体积**：SWC 增强死代码消除能力，结合 Rspack 的 tree shaking 功能，生成更小的打包文件。
- 🔄 **默认增量构建**：显著提升重建速度，HMR 性能提升 30%-40%。
- 🎨 **新的 CssChunkingPlugin**：实验性插件，专门处理 CSS 代码分割，确保样式加载顺序正确。
- 🏗 **增强的懒编译**：支持在 MultiCompiler 中独立配置懒编译选项。
- 📂 **自定义输入文件系统**：允许自定义 compiler.inputFileSystem，支持虚拟模块等场景。
- ⏱ **性能分析工具**：引入基于 perfetto 的精确追踪功能，快速识别构建性能瓶颈。
- 🔄 **依赖升级**：升级了 Zod v4 和 Biome v2 等主要依赖。
- 🛠 **Rstack 进展**：包括 Rsbuild 1.4、Rslib 0.10、Rspress 2.0 beta 等工具的更新和新功能。
- 🔍 **生态系统**：next-rspack 测试覆盖率提升，Kmi 框架集成 Rspack 带来性能提升。
- 📘 **升级指南**：包括升级 SWC 插件和懒编译中间件的变更说明。

---

### [Electron 37.0.0 | Electron](https://www.electronjs.org/blog/electron-37-0)

**原文标题**: [Electron 37.0.0 | Electron](https://www.electronjs.org/blog/electron-37-0)

Electron 37.0.0 发布，包含 Chromium 138、V8 13.8 和 Node 22.16.0 的升级，并引入多项新功能和改进。

- 🚀 **发布信息**：Electron 37.0.0 已发布，可通过 npm 或官网下载安装。  
- 🎨 **平滑圆角**：新增 `-electron-corner-smoothing` CSS 属性，支持创建类似 macOS 的平滑圆角（Squircle）。  
- 🔄 **堆栈升级**：Chromium 升级至 138.0.7204.35，V8 升级至 13.8，Node 升级至 22.16.0。  
- 🌟 **Google Summer of Code**：两位贡献者分别开发新的窗口状态 API 和现代化 Devtron 扩展工具。  
- ✨ **新功能**：  
  - 新增 `window.open` 的 `innerWidth` 和 `innerHeight` 选项。  
  - 支持拦截鼠标事件的 `before-mouse-event`。  
  - 新增 macOS 菜单项的 `sublabel` 功能。  
  - 支持 `HIDDevice.collections` 和 `screen` 坐标转换（Linux X11）。  
- ⚠️ **重大变更**：  
  - Utility Process 未处理 rejection 行为改为警告而非崩溃。  
  - `process.exit()` 在 Utility Process 中改为同步终止。  
  - WebUSB 和 WebSerial 默认启用 Chromium 阻止列表。  
  - 移除 `ProtocolResponse.session` 的 `null` 值支持。  
- 📅 **支持终止**：Electron 34.x.y 已停止支持，建议升级至新版。  
- 🔮 **未来计划**：团队将继续跟进 Chromium、Node 和 V8 的更新，更多信息见公开时间表。

---

### [ESLint v9.30.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/06/eslint-v9.30.0-released/)

**原文标题**: [ESLint v9.30.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/06/eslint-v9.30.0-released/)

ESLint v9.30.0 是一个小版本升级，引入了新功能并修复了之前版本中的多个错误。

- 🚀 **新增 `basePath` 配置属性**：配置对象现在支持 `basePath` 属性，用于指定子目录路径，使配置更易于管理。
- 🔧 **稳定功能标志 `v10_config_lookup_from_file`**：实验性配置文件解析功能已稳定，旧标志名仍兼容。
- 🔄 **`no-duplicate-imports` 新选项**：新增 `allowSeparateTypeImports` 选项，允许区分 `import` 和 `import type`。
- 🐛 **错误修复**：包括修复 `getIndexFromLoc` 方法中的负列值错误，更新 `no-restricted-properties` 的错误消息等。
- 📚 **文档更新**：修正拼写错误，澄清规则元数据的使用，更新子包相关变更。
- 🔄 **依赖升级**：升级到 `@eslint/js@9.30.0`，并进行其他内部维护。

---

### [ESLint v9.30.1 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/07/eslint-v9.30.1-released/)

**原文标题**: [ESLint v9.30.1 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/07/eslint-v9.30.1-released/)

ESLint v9.30.1 是一个补丁版本，修复了之前版本中的多个错误，并进行了文档更新和依赖升级。

- 🐞 **错误修复**：`no-duplicate-imports` 规则现在允许在单独的声明中使用默认类型导入和命名类型导入，以解决 TypeScript 的限制。  
- 📚 **文档更新**：更新了 README 和 JSDoc 的链接。  
- 🔧 **维护工作**：升级了 `@eslint/js@9.30.1` 并更新了 package.json。  
- 👥 **贡献者**：Francesco Trotta 和 Jenkins 等贡献者参与了本次发布。  
- 📅 **发布日期**：2025 年 7 月 1 日。

---

### [Astro 5.11 | Astro](https://astro.build/blog/astro-5110/)

**原文标题**: [Astro 5.11 | Astro](https://astro.build/blog/astro-5110/)

Astro 5.11 发布，引入实验性 CSP 适配器支持和禁用 HTML 流式传输功能，同时修复了多项问题。

- 🚀 **CSP 适配器支持**：Astro 5.11 允许通过官方适配器（如 Node.js、Netlify 和 Vercel）为预渲染页面设置自定义 CSP 头部，支持所有指令。  
- ⚙️ **实验性功能**：需在配置中启用`experimentalStaticHeaders`选项，Cloudflare 支持即将推出。  
- 📜 **禁用 HTML 流式传输**：Node.js 适配器新增`experimentalDisableStreaming`选项，可禁用 HTML 流式传输以适配特定主机需求。  
- 🔧 **升级指南**：推荐使用`@astrojs/upgrade`工具或手动运行包管理器的升级命令。  
- 🐞 **问题修复**：修复了自 5.10 版本以来的多项问题，详情参见更新日志。  
- 👏 **社区贡献**：感谢核心团队及众多社区成员的代码和文档贡献。

---

### [7.28.0 版本发布：`babel.config.ts`、显式资源管理及废弃绑定提案 · Babel](https://babeljs.io/blog/2025/06/30/7.28.0)

**原文标题**: [7.28.0 Released: `babel.config.ts`, explicit resource management, and discard binding proposal · Babel](https://babeljs.io/blog/2025/06/30/7.28.0)

Babel 7.28.0 版本发布，新增了对`babel.config.ts`和`babel.config.mts`的原生支持，默认启用了显式资源管理功能，并引入了丢弃绑定提案的支持。此外，还新增了`sourceType: "commonjs"`选项。

- 🚀 **Babel 7.28.0 发布**：支持`babel.config.ts`和`babel.config.mts`，推荐使用 Node.js 24 以获得最佳效果。
- 🔄 **显式资源管理默认启用**：ES2026 显式资源管理功能现已默认启用，无需额外插件。
- 🗑️ **丢弃绑定提案支持**：通过`@babel/plugin-proposal-discard-binding`插件支持`void`绑定，表示未使用的变量或参数。
- 📜 **新增`sourceType: "commonjs"`选项**：适用于 CommonJS 环境，允许在顶层使用`return`、`new.target`等语法。
- 💡 **Babel 8 Beta 兼容**：所有 7.28.0 的新功能已包含在`v8.0.0-beta.1`中。
- 💰 **支持 Babel 发展**：欢迎通过 Open Collective 捐赠或直接参与新 ECMAScript 提案的实现。

---

### [发布 r178 · mrdoob/three.js · GitHub](https://github.com/mrdoob/three.js/releases/tag/r178)

**原文标题**: [Release r178 · mrdoob/three.js · GitHub](https://github.com/mrdoob/three.js/releases/tag/r178)

three.js 的 r178 版本发布，包含多项功能更新、错误修复和性能优化。

- 🛠️ 移除已弃用代码，并修复所有渲染器中的混合公式问题。
- 🔄 升级 monaco-editor，并初步支持 Float16Array。
- ⏱️ 优化 Clock 模块，内联 performance.now()。
- 🎨 修复 Frustum 模块中 intersectsSprite() 的精灵偏移问题。
- 📊 为 GLBufferAttribute 添加 normalized 属性。
- 🖼️ 优化 ImageLoader 的缓存机制。
- 🔑 Loader 模块现在为每种加载器类型使用唯一的缓存键。
- 🧩 修复 NodeBuilder 中的插值指定问题。
- 🌈 NodeMaterial 现在支持 material.premultipliedAlpha。
- 🔄 更新 Quaternion 模块中 setFromUnitVectors() 的 epsilon 值。
- 📏 RenderObject 现在检查几何体的属性版本。
- 🧪 移除 SampleNode 中的 PURE 注解。
- 🔧 修复 TSL 模块中的 Fn 参数问题，并引入 sample() 和 textureBicubicLevel() 功能。
- 🚀 引入 Chromatic Aberration 效果，并修复 step() 的不一致链式调用。
- 🔄 重命名 premult 为 premultiplyAlpha，并引入 tangentViewFrame 和 bitangentViewFrame。
- 💻 WebGLPrograms 现在在启用线框时不使用平面着色。
- 🎮 WebGLRenderer 修复了传输过程中的渲染目标恢复问题。
- 🌐 WebGPUConstants 添加了缺失的功能。
- 🖥️ WebGPURenderer 修复了 WebGL 后端中的无效数组问题。
- 📚 文档改进，包括 JSDoc 和法语翻译。
- 🎨 示例部分进行了清理和改进，包括水演示和新的路径演示。
- 🔌 插件部分更新，包括 ArcballControls 和 FBXLoader 的改进。
- 🚀 贡献者包括 mrdoob 和其他 17 位开发者。

---

### [吕的主页](https://lui.ie/guides/semantic-search-colors)

**原文标题**: [Lui's Homepage](https://lui.ie/guides/semantic-search-colors)

好的，请提供需要总结的文本内容，我会按照您要求的模板进行整理：  

- 📌 概述总结（无标题）  
- 🌟 要点 1  
- 🔍 要点 2  
- 📊 要点 3  

（以此类推，根据具体内容调整）  

请将文本粘贴给我，我会立即为您生成结构化摘要！

---

### [brandmint.ai](https://brandmint.ai/color-genie)

**原文标题**: [brandmint.ai](https://brandmint.ai/color-genie)

好的，请提供您需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

概述总结  
- 🌟 要点一  
- 📌 要点二  
- 🔍 要点三  

请提供具体文本，我会为您生成相应的总结。

---

### [使用 JavaScript 代理构建轻量级响应式状态管理器 | Loren Stewart](https://www.lorenstew.art/blog/reactive-state-manager-with-proxies)

**原文标题**: [Building a Lightweight Reactive State Manager with JavaScript Proxies | Loren Stewart](https://www.lorenstew.art/blog/reactive-state-manager-with-proxies)

概述：本文介绍了如何使用 JavaScript 的 Proxy 对象构建一个轻量级响应式状态管理器，以自动同步 UI 与应用程序状态，避免使用复杂的状态管理库。

- 🛠️ 使用 JavaScript 的 Proxy 对象可以创建一个轻量级响应式状态管理器，自动同步 UI 与应用程序状态。
- 🎯 核心思想是通过 Proxy 拦截状态对象的 set 操作，在状态变化时自动触发 UI 更新函数。
- 📝 示例展示了一个媒体提交表单的状态管理，通过 Proxy 自动更新多个 UI 部分。
- 🔧 通过公共 API 函数和状态查询函数，保持代码的整洁和组织性。
- 🔄 支持复杂交互（如拖拽重新排序照片），状态变化自动触发 UI 更新。
- ✅ 优点包括简单性、无依赖、清晰的代码分离和低样板代码。
- 🚀 适用于需要轻量级状态管理的应用场景，避免引入大型状态管理库。

---

### [全栈 Next.js 15 课程 - Next 之路](https://www.road-to-next.com/?utm_source=javascript_weekly&utm_medium=referral&utm_campaign=next_course_launch)

**原文标题**: [Full-Stack Next.js 15 Course - The Road to Next](https://www.road-to-next.com/?utm_source=javascript_weekly&utm_medium=referral&utm_campaign=next_course_launch)

《The Road to Next》课程概览  
这是一门专注于 Next.js 15 和 React 19 的全栈开发课程，旨在帮助开发者从初级进阶到高级水平，掌握现代 Web 应用开发的核心技能。课程结合视频教学与实践项目，涵盖从基础到高级的全栈技术栈，适合不同背景的学习者。

- 🚀 **课程目标**：培养全栈开发能力，涵盖前端（React/Next.js）与后端（数据库、API、身份验证等），并教授高级软件工程思维。  
- 🎥 **课程形式**：视频课程 + 实战项目（构建 SaaS 启动套件），包含 14 天退款保证和终身访问权限。  
- 👨‍🏫 **讲师**：Robin Wieruch，资深软件工程师，拥有十年开发经验，曾为多家知名企业和政府项目提供技术支持。  
- 💻 **技术栈**：  
  - Next.js 15（全栈框架）  
  - React 19（前端框架）  
  - Prisma（ORM 工具）  
  - Supabase（Postgres 数据库）  
  - Stripe（支付集成）  
  - Tailwind CSS（样式设计）  
- 📚 **学习路径**：  
  - **开发者旅程**（$249）：基础到高级 Next.js 与 React 内容。  
  - **工程师旅程**（$349）：扩展至 SaaS 开发、消息队列、高级认证等。  
- 🌍 **适合人群**：  
  - 想进阶高级 React 或全栈开发的开发者  
  - 转行全栈的前端工程师  
  - 无 JavaScript 背景但有编程经验者  
  - 自由职业者或技术创业者  
- ✨ **学生评价**：  
  - 对 Server Components 和 Server Actions 的清晰讲解获高度好评。  
  - 项目结构（如功能文件夹）和认证实现被赞实用性强。  
  - Tailwind 和 Shadcn/UI 的教学帮助快速提升开发效率。  
- ❓ **常见问题**：  
  - 支持分期付款、学生折扣（20%）、团队许可。  
  - 提供英文字幕，推荐大屏学习以保持代码上下文。  
- 🔗 **附加福利**：Discord 社区支持、完成证书、可赠课或开发票。  

课程强调“学以致用”，通过真实项目演练帮助学员掌握行业级开发流程，最终具备独立构建复杂应用的能力。

---

### [一个令人困惑的 JavaScript 解析难题](https://www.hillelwayne.com/post/javascript-puzzle/)

**原文标题**: [A Perplexing Javascript Parsing Puzzle](https://www.hillelwayne.com/post/javascript-puzzle/)

概述：这篇文章探讨了 JavaScript 中一个令人困惑的解析问题，解释了为什么代码`x = 1; x --> 0`会输出`1`，并深入探讨了其历史背景和标准化原因。

- 🧩 代码`x = 1; x --> 0`输出`1`，因为`-->`在行首时被视为注释起始符。  
- 📜 这一行为源于 Netscape Navigator 2 时代的遗留问题，当时为了兼容旧浏览器，JavaScript 代码被包裹在 HTML 注释中。  
- 🤔 `<!--`和`-->`被现代 JavaScript 引擎保留为合法的注释符号，以避免破坏旧网站的功能。  
- 📌 `-->`仅在行首有效，以避免与递减操作符和大于操作符的歧义。  
- 🌐 现代浏览器和部分引擎（如 Node 和 Electron）支持此语法，但并非所有 JavaScript 引擎都必需支持。  
- 📧 作者邀请读者订阅其新闻通讯，并提到他为企业提供形式化方法培训的服务。  
- 🏷️ 文章分类为“编程”，标签包括“历史”、“JavaScript”和“罪行”。

---

### [2025 年现代 Node.js 模式](https://kashw1n.com/blog/nodejs-2025/)

**原文标题**: [Modern Node.js Patterns for 2025](https://kashw1n.com/blog/nodejs-2025/)

Node.js 在 2025 年的现代模式演进，从 CommonJS 到 ESM 模块化、内置 Web API、测试工具到异步模式优化，全面提升开发体验与性能。

- 📦 **模块系统：ESM 成为新标准**  
  从 CommonJS 过渡到 ES Modules (ESM)，支持静态分析和`node:`前缀明确核心模块依赖。

- 🌐 **内置 Web API 减少依赖**  
  原生集成 Fetch API、AbortController 等，替代`axios`等第三方库，支持超时和取消操作。

- 🧪 **内置测试工具**  
  无需 Jest/Mocha，Node.js 自带测试运行器，支持异步测试、覆盖率统计和监听模式。

- 🔄 **高级异步模式**  
  Top-level await 简化初始化，结合`Promise.all`并行处理，AsyncIterators 优化事件流处理。

- 🌊 **现代流处理**  
  增强的 Streams API 与 Web Streams 互通，`pipeline`函数简化错误处理和资源清理。

- 🧵 **Worker Threads 实现并行**  
  通过工作线程处理 CPU 密集型任务（如斐波那契计算），避免阻塞主线程。

- ⚡ **开发体验升级**  
  内置`--watch`监听文件变化，`--env-file`加载环境变量，减少`nodemon`和`dotenv`依赖。

- 🔒 **安全与性能监控**  
  实验性权限模型限制文件/网络访问，内置`perf_hooks`实现基础性能监控。

- 📦 **应用分发优化**  
  支持单可执行文件 (SEA) 打包，简化 CLI 工具和桌面应用部署。

- 🛠 **结构化错误处理**  
  扩展`Error`类增强上下文信息，结合诊断通道 (`diagnostics_channel`) 实现精细化监控。

- 🗂 **现代包管理**  
  Import Maps 优化内部模块引用，动态导入 (`dynamic import`) 实现按需加载。  

关键趋势：拥抱 Web 标准、减少外部依赖、强化异步模式与开发者体验，同时兼顾安全与部署效率。

---

### [halcy 日志](https://halcy.de/blog/2025/06/27/transmitting-data-via-ultrasound-without-any-special-equipment/)

**原文标题**: [halcy log](https://halcy.de/blog/2025/06/27/transmitting-data-via-ultrasound-without-any-special-equipment/)

2025 年 6 月 27 日，关于利用超声波传输数据的技术探索。  
- 🔊 超声波可用于设备间数据传输，无需特殊硬件，普通电脑扬声器和麦克风即可实现。  
- 🎵 人耳可听声音频率范围为 10-20000Hz，超过 20000Hz 的称为超声波，多数人听不见。  
- 💻 通过 WebAudio 技术，将数据编码为高频音频信号（如 RTZ FSK 调制），实现静默传输。  
- 📱 实验网站演示了手机与电脑间超声波传输消息，但存在速度慢、抗干扰差等局限性。  
- 🔧 代码开源，鼓励改进（如纠错算法），潜在应用包括会议软件的邻近设备检测。  
- 😠 类似技术被用于“驱散青少年”的高频噪音装置，原理相同但目的不同。

---

### [每位 React 开发者都应了解的 Signals 知识 - YouTube](https://www.youtube.com/watch?v=VgGl9i-OBBI)

**原文标题**: [What Every React Developer Should Know About Signals - YouTube](https://www.youtube.com/watch?v=VgGl9i-OBBI)

这是一个关于 YouTube 网站相关链接和信息的概览。

- 🏢 プレスルーム - 媒体和新闻相关信息的官方发布渠道  
- ©️ 著作権 - 版权信息和相关法律声明  
- 📧 お問い合わせ - 联系 YouTube 的途径  
- 🎨 クリエイター向け - 为内容创作者提供的资源和支持  
- 📢 広告掲載 - 广告投放和商业合作信息  
- 💻 開発者向け - 开发者资源和 API 相关支持  
- 📜 利用規約 - 平台使用条款和条件  
- 🔒 プライバシー - 用户隐私保护政策  
- 🛡️ ポリシーとセキュリティ - 平台政策和安全措施  
- ⚙️ YouTube の仕組み - YouTube 平台运作机制介绍  
- 🆕 新機能を試してみる - 尝试 YouTube 最新功能  
- ®️ © 2025 Google LLC - 版权归属和年份声明

---

### [Mapbox 自定义 3D 模型：逐步集成指南 - Bleech](https://bleech.de/en/blog/custom-3d-models-in-mapbox/)

**原文标题**: [Custom 3D models in Mapbox: a step-by-step integration guide - Bleech](https://bleech.de/en/blog/custom-3d-models-in-mapbox/)

本文详细介绍了如何在 Mapbox 地图中集成自定义 3D 模型的全过程，从建模到最终渲染，提供了技术实现的具体步骤和优化建议。

- 🏗️ 作者通过 Blender 创建了一个低多边形风格的 3D 建筑模型，以补充 Mapbox 标准 3D 数据集中缺失的特定地标建筑。
- 📏 建模前使用 Google Maps 测量工具和自定义标尺方法精确获取建筑尺寸，确保模型准确性。
- 💻 模型导出为.glb 格式后，通过 Mapbox GL JS 和 Three.js 进行集成，涉及移除默认建筑、设置模型位置和添加光照等步骤。
- 🌞 光照配置包括环境光和方向光，并详细调整了阴影参数（如阴影贴图分辨率和偏移值）以解决常见渲染问题。
- 🎨 通过 ShaderMaterial 实现了入口发光效果，使自定义模型与 Mapbox 原生建筑的视觉风格保持一致。
- 🔄 处理了窗口大小调整时的模型失真问题，通过重新初始化渲染器确保阴影计算正确更新。
- 🛠️ 文章提供了完整的技术实现代码片段，包括模型加载、场景设置和渲染循环等关键部分。
- 📚 推荐了 Three.js Journey 等学习资源，帮助读者深入掌握 3D 建模和 WebGL 集成技术。

---

### [获取失败](https://javascriptweekly.com/link/171373/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/171373/web)

无法总结：获取内容失败，状态码 403。

---

### [Milkdown](https://milkdown.dev/)

**原文标题**: [Milkdown](https://milkdown.dev/)

Milkdown 是一个插件驱动的框架，用于构建所见即所得的 Markdown 编辑器，支持高度定制和实时协作。

- 🔩 **插件驱动**：Milkdown 的所有功能都基于插件，可通过语法、主题、UI 等插件扩展编辑器功能。  
- 🤝 **实时协作**：借助 Y.js 支持，多用户可实时协作编辑同一文档。  
- 🤯 **无头设计**：Milkdown 不预设 CSS，可轻松自定义编辑器样式以适配应用风格。  
- 💡 **可靠生态**：基于 ProseMirror、Y.js 和 Remark 等成熟库构建，可直接利用其社区和生态系统获取支持。

---

### [入门指南 | Milkdown](https://milkdown.dev/docs/guide/getting-started)

**原文标题**: [Getting Started | Milkdown](https://milkdown.dev/docs/guide/getting-started)

GitHub 页面编辑功能概述  
- ✏️ 提供在 GitHub 上直接编辑页面的选项  
- 🔄 方便用户快速修改和更新内容  
- 🌐 支持协作和版本控制

---

### [游乐场 | Milkdown](https://milkdown.dev/playground)

**原文标题**: [Playground | Milkdown](https://milkdown.dev/playground)

好的，请提供需要总结的文本内容，我会按照您要求的模板生成概述和带表情符号的要点列表。  

示例模板：  

概述内容  

- 🌟 要点 1  
- 📌 要点 2  
- 🔍 要点 3  

请提供具体文本以便我为您生成总结！

---

### [GitHub - Milkdown/milkdown: 🍼 插件驱动的所见即所得 Markdown 编辑器框架](https://github.com/Milkdown/milkdown)

**原文标题**: [GitHub - Milkdown/milkdown: 🍼 Plugin driven WYSIWYG  markdown editor framework.](https://github.com/Milkdown/milkdown)

Milkdown 是一个插件驱动的所见即所得（WYSIWYG）Markdown 编辑器框架，灵感来源于 Typora，基于 prosemirror 和 remark 构建。

- 🍼 插件驱动的 WYSIWYG Markdown 编辑器框架  
- 🌐 官方网站：[milkdown.dev](https://milkdown.dev)  
- ⭐ 10.1k 星，462 个 Fork  
- 📜 采用 MIT 许可证  
- 🔧 基于 prosemirror 和 remark 构建  
- 🎨 设计由 Meo 和 Mirone 完成  
- 📚 详细文档请查看[官方文档网站](https://milkdown.dev/docs)  
- 🚀 开发计划可查看 [Milkdown TODO](https://github.com/orgs/Milkdown/projects/1) 和里程碑  
- 💬 欢迎加入 [Discord 社区](https://discord.gg/SdMnrSMyBX)  
- 🤝 遵循[贡献指南](https://github.com/Milkdown/milkdown/blob/main/CONTRIBUTING.md)参与贡献  
- 🙏 特别感谢 @Meo 的设计工作  
- 💖 支持维护可考虑[赞助项目](https://github.com/sponsors/Saul-Mirone)  
- 📄 代码语言主要为 TypeScript (90.9%) 和 CSS (7.5%)

---

### [Repomix | 将代码库打包为 AI 友好格式](https://repomix.com/)

**原文标题**: [Repomix | Pack your codebase into AI-friendly formats](https://repomix.com/)

AI 优化了代码库的格式，使其更易于 AI 理解和处理。

- 🤖 AI 优化 - 代码库经过特殊格式化，便于 AI 高效理解与处理。

---

### [GitHub - yamadashy/repomix: 📦 Repomix 是一款强大工具，能将整个代码库打包成单一且对 AI 友好的文件。非常适合需要将代码库输入大型语言模型（LLM）或其他 AI 工具（如 Claude、ChatGPT、DeepSeek、Perplexity、Gemini、Gemma、Llama、Grok 等）的场景。](https://github.com/yamadashy/repomix)

**原文标题**: [GitHub - yamadashy/repomix: 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.](https://github.com/yamadashy/repomix)

Repomix 是一个强大的工具，能够将整个代码仓库打包成单个 AI 友好的文件，适用于与大型语言模型（LLMs）和其他 AI 工具（如 Claude、ChatGPT、DeepSeek、Perplexity、Gemini、Gemma、Llama、Grok 等）交互的场景。

- 📦 **功能概述**：将代码仓库打包为 AI 友好的单一文件，支持多种输出格式（XML、Markdown、纯文本）。
- 🚀 **快速开始**：通过 CLI 工具、网站、浏览器扩展或 VSCode 插件使用，支持一键打包。
- 🛠️ **核心特性**：AI 优化、令牌计数、代码压缩、安全检查（Secretlint）、Git 感知（自动忽略 .gitignore 文件）。
- 🌐 **远程仓库支持**：无需克隆即可处理远程 Git 仓库，支持分支、标签和提交哈希。
- ⚙️ **配置灵活**：通过配置文件或命令行选项自定义包含/排除规则、输出格式和安全检查。
- 🔒 **隐私与安全**：CLI 工具完全离线运行，不收集用户数据；网站处理文件后自动删除。
- 📜 **开源与社区**：MIT 许可证，欢迎贡献，提供 Discord 社区支持。
- 🐳 **多平台支持**：支持 Docker、GitHub Actions，可作为库集成到 Node.js 应用中。

---

### [在真实 iOS 设备上运行 Playwright 测试 | BrowserStack 文档](https://www.browserstack.com/docs/automate/playwright/playwright-ios?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=new-launches-updates&utm_campaign=PR-12-Jun-2025-iOS-Playwright&utm_campaigncode=701OW00000NyIRcYAN&utm_term=javascriptweekly)

**原文标题**: [Run Playwright tests on real iOS devices | BrowserStack Docs](https://www.browserstack.com/docs/automate/playwright/playwright-ios?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=new-launches-updates&utm_campaign=PR-12-Jun-2025-iOS-Playwright&utm_campaigncode=701OW00000NyIRcYAN&utm_term=javascriptweekly)

BrowserStack 推出支持在真实 iOS 设备上运行 Playwright 测试的功能，提供 100 多种 iPhone 和 iPad 设备 - 浏览器组合测试，帮助开发者发现 Safari 特有的问题。

- 🚀 **Playwright 测试支持**：现在可以在 BrowserStack Automate 上运行 Playwright 测试，支持真实 iOS 设备。  
- 📱 **设备多样性**：覆盖 100 多种 iPhone 和 iPad 设备 - 浏览器组合，确保全面测试。  
- 🔍 **精准调试**：集成现有 CI 流程，提供测试日志和调试工具。  
- 📹 **视频教程**：提供视频介绍 iOS 浏览器测试的挑战及如何在 BrowserStack 上使用 Playwright。  
- ⚙️ **环境要求**：需要 BrowserStack 账户、NodeJS 14+ 及最新 Playwright iOS 兼容版本。  
- 🛠️ **快速开始**：通过克隆示例仓库、安装依赖、配置设备参数，即可运行测试。  
- 📊 **结果查看**：测试结果可在 BrowserStack Automate 仪表板查看。  
- ⚠️ **不支持功能**：部分功能如 playwrightLogs、consoleLogs 等在 iOS 设备上暂不支持。  
- ❓ **技术支持**：提供支持团队联系方式以解决疑问。

---

### [snapDOM – 高精度与极速的 HTML 转图像捕捉工具](https://zumerlab.github.io/snapdom/)

**原文标题**: [
    snapDOM – HTML to Image capture with superior accuracy and speed
  ](https://zumerlab.github.io/snapdom/)

概述总结  
- 🏁 基准测试：比较 snapDOM 和 html2canvas 库的性能  
- 📊 每个库将捕获相同的 DOM 元素 5 次，计算平均速度并显示胜者  
- 🎯 测试元素包括基础文本、动态效果、CSS 框架、Google 字体等  

- 🏁 **基准测试**  
  - 📊 每个库对同一 DOM 元素进行 5 次捕获，比较平均速度  

- 📦 **基础测试**  
  - ✨ 示例文本："Hello SnapDOM!"  

- 🚀 **动态效果**  
  - 🕺💃 动态变色文字："I'm dancing and changing color!"  

- 📦 **Orbit CSS 框架**  
  - 🪐 包含轨道路径和行星系统的演示  

- 🔤 **Google 字体**  
  - ✍️ 使用 `embedFonts: true` 嵌入独特字体  

- 🧱 **Shadow DOM**  
  - ⚡ 测试 Shadow DOM 的捕获能力  

- 🎨 **Canvas**  
  - 🖌️ 测试 Canvas 元素的捕获  

- 📁 **导出格式**  
  - 📤 支持 PNG、JPG 和 WebP 导出  

- ✨ **伪元素**  
  - ⚡ 测试包含伪元素的 DOM 捕获  

- ✂️ **Clip-Path 演示**  
  - 🔷 使用 `clip-path` 的图形捕获  

- 🌀 **混合模式**  
  - 🌈 测试混合模式内容的捕获  

- 🧾 **全页面捕获**  
  - 📄 测试完整页面的捕获功能

---

### [时间选择器 | OpenStatus](https://time.openstatus.dev/)

**原文标题**: [TimePicker | OpenStatus](https://time.openstatus.dev/)

这是一个关于基于 React 和 Shadcn UI 构建的时间选择器组件的介绍和快速入门指南。

- ⏰ 组件名称：`<TimePickerInput />`，支持时间选择功能  
- 📅 支持日期时间选择，包含小时、分钟、秒和时段（如 AM/PM）的选项  
- 🎯 功能特点：监听键盘事件、支持箭头导航、优化移动端键盘输入、格式化日期值  
- 📱 无需额外库依赖，原生支持 React 和 Shadcn UI  
- ⚙️ 快速开始：需安装`shadcn/ui`及其`Input`组件（12 小时制还需`Select`组件）  
- 📋 使用步骤：复制工具和输入组件文件，定义自己的时间选择器组件  
- 💻 提供多个代码片段示例，包括 12 小时制、日期时间选择器、表单集成等  
- 🌐 由 OpenStatus 提供技术支持

---

### [GitHub - rvanwijnen/spectral.js: Spectral.js 是一个基于 Kubelka-Munk 理论的类绘画调色库。](https://github.com/rvanwijnen/spectral.js)

**原文标题**: [GitHub - rvanwijnen/spectral.js: Spectral.js is a paint like color mixing library utilizing the Kubelka-Munk theory.](https://github.com/rvanwijnen/spectral.js)

Spectral.js 是一个基于 Kubelka-Munk 理论的轻量级 JavaScript 库，用于实现逼真的颜料混合效果。它通过模拟光线与颜料的相互作用，提供比传统 RGB 混合更真实的色彩混合效果。

- 🎨 **物理基础**：基于 Kubelka-Munk 理论，模拟颜料的光吸收和散射特性。
- ⚖️ **感知均匀**：使用 OKLab 和 OKLCh 色彩空间，确保色彩混合的感知均匀性。
- 🧠 **智能混合**：结合亮度、着色强度和用户定义的混合因子计算有效浓度。
- 🚀 **高性能**：采用惰性记忆化和快速数学计算，确保在浏览器环境中高效运行。
- 🛠️ **简单 API**：支持常见的颜色格式（如 hex、RGB 和 CSS 字符串），易于使用。
- 📐 **高精度计算**：使用 64 位浮点数学，确保色彩计算的准确性。
- 🌈 **光谱混合模型**：通过七种基本光谱反射曲线生成混合颜色，模拟真实颜料混合效果。
- 📦 **安装简便**：支持 npm 安装或直接下载脚本文件。
- 🚀 **功能丰富**：提供颜色混合、调色板生成、渐变生成等功能。
- 🧵 **GLSL 集成**：支持在着色器中实时进行光谱颜色混合，适用于 WebGL 项目。
- 🔧 **API 文档完善**：提供详细的 Color 类方法和属性说明，支持懒加载和缓存优化。
- 🚨 **版本升级**：3.0 版本引入重大变更，需使用 Color 类进行颜色操作。
- 🤝 **开源贡献**：欢迎开发者提交问题和拉取请求，共同改进项目。
- 📜 **MIT 许可证**：项目采用 MIT 许可证，可自由使用和修改。

---

### [库贝尔卡 - 芒克理论 - 维基百科](https://en.wikipedia.org/wiki/Kubelka%E2%80%93Munk_theory)

**原文标题**: [Kubelka–Munk theory - Wikipedia](https://en.wikipedia.org/wiki/Kubelka%E2%80%93Munk_theory)

Kubelka-Munk 理论是光学中用于模拟涂料薄膜外观的基础理论，由 Paul Kubelka 和 Franz Munk 于 1931 年提出。该理论通过两个与涂料相关的常数，描述了涂层如何改变基材颜色以及所需涂层的厚度。其数学模型基于双通量近似，适用于多种应用领域，包括涂料、纸张、半导体和光谱学。尽管该理论在工业中广泛应用，但在强吸收材料等情况下存在局限性，并已发展出多种改进方法。

- 🌈 Kubelka-Munk 理论由 Paul Kubelka 和 Franz Munk 于 1931 年提出，用于模拟涂料薄膜的光学外观。  
- 📐 理论基于双通量近似，仅使用两个涂料相关常数来描述涂层的吸收和反向散射特性。  
- 🎨 在涂料工业中，该理论用于预测涂层的遮盖力和颜色变化，尤其适用于无限厚涂层的特殊情况。  
- 📜 理论在纸张工业中用于预测纸张的光学性质，如反射率和不透明度，帮助优化纸张配方。  
- 🔬 在半导体领域，Kubelka-Munk 理论用于通过 Tauc 图确定材料的带隙能量。  
- 🖌️ 该理论还被应用于颜色混合和匹配，通过计算吸收与散射比来预测混合颜料的颜色。  
- 🔍 在光谱学中，Kubelka-Munk 函数用于分析漫反射光谱，尤其在近红外光谱中广泛应用。  
- ⚠️ 尽管理论简单且应用广泛，但在强吸收材料或非均匀层等情况下存在局限性，促使研究者提出多种改进方法。  
- 💻 近年来，该理论还被应用于计算机艺术中的 RGB 颜色模型，实现更真实的颜料混合效果。

---

### [GitHub - bufbuild/protobuf-es：ECMAScript 的 Protocol Buffers 实现。唯一完全通过 Protobuf 一致性测试的 JavaScript 库。](https://github.com/bufbuild/protobuf-es)

**原文标题**: [GitHub - bufbuild/protobuf-es: Protocol Buffers for ECMAScript. The only JavaScript Protobuf library that is fully-compliant with Protobuf conformance tests.](https://github.com/bufbuild/protobuf-es)

Protobuf-ES 是一个完整的 Protocol Buffers 实现，适用于 TypeScript 和 JavaScript，可在浏览器和 Node.js 中使用，由 Buf 创建。它是唯一完全符合 Protobuf 一致性测试的 JavaScript 库，支持生成类型安全的代码，并可与 Connect-ES 等 RPC 库配合使用。

- 🚀 **完全兼容** - Protobuf-ES 是唯一通过 Protobuf 一致性测试的 JavaScript 库。
- 📜 **协议定义** - 支持编写数据模式（schema）并定义二进制序列化格式。
- 🔄 **跨语言支持** - 生成的代码可跨语言使用，确保数据定义一致。
- ⚡ **快速上手** - 安装 `@bufbuild/protobuf` 和 `@bufbuild/protoc-gen-es` 即可开始使用。
- 📂 **代码生成** - 通过 `buf` 或 `protoc` 工具生成 TypeScript 代码。
- 📚 **文档丰富** - 提供详细手册、代码示例和插件开发指南。
- 📦 **生态系统** - 支持 Connect-ES 和 Buf Studio 等工具，适用于多种框架。
- ⚖️ **开源许可** - 主要代码采用 Apache-2.0 许可证，部分代码基于 BSD-3-Clause。
- 🌟 **社区活跃** - 拥有 1.3k+ Stars 和 81 Forks，被 88k+ 项目使用。

---

### [GitHub - Clariity/react-chessboard: ChessOpenings.co.uk 使用的 React 国际象棋棋盘库。灵感来自并改编自已停止维护的 Chessboard.jsx。](https://github.com/Clariity/react-chessboard)

**原文标题**: [GitHub - Clariity/react-chessboard: The React Chessboard Library used at ChessOpenings.co.uk. Inspired and adapted from the unmaintained Chessboard.jsx.](https://github.com/Clariity/react-chessboard)

一个 React 象棋棋盘组件库，用于构建现代响应式象棋应用。

- ♟️ **功能丰富**：支持拖放、自定义棋子、动画、事件处理等  
- 📦 **安装简单**：支持 pnpm/yarn/npm 安装  
- 🚀 **快速上手**：提供基础使用代码示例  
- 📚 **详细文档**：包含 API 参考和示例  
- 🤝 **欢迎贡献**：提供贡献指南和待实现功能列表  
- 📄 **MIT 许可**：开源且允许自由使用  
- 🌐 **社区支持**：提供 Discord 交流群组  
- 🔄 **持续维护**：基于 Chessboard.jsx 改进而来  
- 🛠️ **技术栈**：TypeScript 开发，支持多种框架集成

---

### [@storybook/core - Storybook](https://react-chessboard.vercel.app/?path=/docs/how-to-use-basic-examples--docs)

**原文标题**: [@storybook/core - Storybook](https://react-chessboard.vercel.app/?path=/docs/how-to-use-basic-examples--docs)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结。  

- 📌 要点一：关键信息  
- 🔍 要点二：核心内容  
- 📊 要点三：数据或结论  

请提供具体文本，我会为您生成相应的总结。

---

### [Faker](https://fakerjs.dev/)

**原文标题**: [Faker](https://fakerjs.dev/)

人物信息生成  
- 🧑‍💼 **姓名**：随机生成多样化姓名  
- ♀️♂️ **性别**：包含男、女及非二元选项  
- 📝 **简介**：自动生成简短个人背景描述  
- 👔 **职位**：提供常见职业或自定义职称  
- 🌍 **其他**：可扩展添加年龄、兴趣等字段  

概述：该工具用于快速创建虚拟人物完整档案，适用于写作、游戏或测试数据场景。

---

### [GitHub - jcubic/jquery.terminal: jQuery 终端模拟器 - 用于创建带自定义命令的基于网页的终端的 JavaScript 库](https://github.com/jcubic/jquery.terminal)

**原文标题**: [GitHub - jcubic/jquery.terminal: jQuery Terminal Emulator - JavaScript library for creating web-based terminals with custom commands](https://github.com/jcubic/jquery.terminal)

jQuery Terminal Emulator 是一个用于创建基于网页的终端模拟器的 JavaScript 库，支持自定义命令和丰富的功能。

- 🖥️ 主要功能：创建网页终端模拟器，支持自定义命令、JSON-RPC 服务调用和用户命令解析。
- 🔒 认证支持：提供登录和密码验证功能，支持 JSON-RPC 自动调用登录功能。
- 🌳 命令树结构：支持嵌套对象和命令，可以创建多层级的命令结构。
- 🔄 历史记录：支持命令行历史记录，使用本地存储保存历史命令。
- 🔍 自动补全：支持 Tab 键自动补全命令。
- ⌨️ 快捷键：支持类似 Bash 的快捷键，如 CTRL+A、CTRL+D 等。
- 📱 移动支持：实验性支持移动设备。
- 🎨 样式定制：可以轻松修改终端样式，包括颜色和光标动画。
- 🚀 安装方式：支持通过 CDN、npm 或 bower 安装。
- 📚 文档丰富：提供详细文档和示例，适合初学者和高级用户。
- 🔧 安全设置：默认禁用潜在的不安全功能，如非标准协议链接和终端方法调用。
- 🌟 开源项目：MIT 许可证，活跃的社区支持和贡献者。

---

### [jQuery 终端：基于 JavaScript 的网页终端模拟器](https://terminal.jcubic.pl/#demo)

**原文标题**: [jQuery Terminal: JavaScript Web Based Terminal Emulator](https://terminal.jcubic.pl/#demo)

jQuery Terminal 是一个免费开源的 JavaScript 库，用于在应用程序中创建命令行解释器，支持自定义命令、JSON-RPC 服务调用，并能实现嵌套解释器或交互式菜单等功能。

- 🖥️ 用于创建基于网页的交互式终端应用  
- 🔧 支持自定义命令（可通过服务器或浏览器 JavaScript 定义）  
- 🔄 自动调用 JSON-RPC 服务或对象方法（如创建 Python 解释器）  
- 🌳 支持嵌套对象实现多级交互（如游戏菜单）  
- 🛠️ 提供手动解析用户命令的函数（完全控制输入逻辑）  
- ⚡ 适合为高级用户扩展功能或作为调试工具  
- 🎨 可打造炫酷的交互式作品集网站（模仿 Linux/MacOS/WSL 终端风格）  
- 🐞 快速调试 REST API 或后端应用（支持实时 eval 调试）  
- 📱 兼容浏览器和移动设备，体验接近原生终端

---

### [发布 v2.2.0 · kewisch/ical.js · GitHub](https://github.com/kewisch/ical.js/releases/tag/v2.2.0)

**原文标题**: [Release v2.2.0 · kewisch/ical.js · GitHub](https://github.com/kewisch/ical.js/releases/tag/v2.2.0)

ical.js 项目 v2.2.0 版本发布  

- 🚀 **版本更新**：v2.2.0 于 2020 年 6 月 28 日发布，包含多项功能改进和 Bug 修复。  
- 🔧 **问题修复**：修复了参数多值处理、UTC 日期解析、Duration RFC 兼容性等问题。  
- ✨ **新功能**：支持`BYYEARDAY`和`BYDAY`规则，增加周期比较函数，优化 Time 类类型定义。  
- 📦 **依赖更新**：多项依赖库升级，提升稳定性和性能。  
- 👏 **新贡献者**：欢迎@onny、@st3iny 等 6 位新开发者加入并提交首次代码。  
- 📜 **完整日志**：详细变更记录可查看 v2.1.0 到 v2.2.0 的提交历史。

---

### [GitHub - ng-matero/ng-matero: Angular Material 后台管理模板](https://github.com/ng-matero/ng-matero)

**原文标题**: [GitHub - ng-matero/ng-matero: Angular Material admin template.](https://github.com/ng-matero/ng-matero)

Ng-Matero 是一个基于 Angular 和 Material 组件构建的后台管理模板，具有丰富的功能和灵活的配置选项。

- 🚀 **项目简介**: Ng-Matero 是一个 Angular 后台管理模板，使用 Material 组件构建，提供现代化的设计风格和多种布局选项。
- ✨ **主要特性**: 包括 Material 扩展、Schematics 支持、暗黑模式、RTL 支持、国际化、权限管理等。
- 📖 **文档支持**: 提供英文和简体中文文档，方便开发者查阅。
- 🔧 **安装方式**: 支持通过 `ng add` 命令快速安装，也可以通过 Git 克隆项目仓库。
- ⚙️ **Schematics 支持**: 提供模块和页面的快速生成功能，支持懒加载模块和入口组件生成。
- 💻 **开发环境**: 克隆项目后，运行 `npm install` 和 `npm run start` 即可启动开发服务器。
- 🤝 **贡献者**: 项目欢迎代码和财务贡献，支持社区发展。
- 📃 **许可证**: 采用 MIT 许可证，允许自由使用和修改。
- 🌍 **兼容性**: 支持多个 Angular 和 Material 版本，详细版本兼容性可查阅文档。

---

### [GitHub - PrismarineJS/mineflayer: 使用强大、稳定且高级的 JavaScript API 创建 Minecraft 机器人](https://github.com/PrismarineJS/mineflayer)

**原文标题**: [GitHub - PrismarineJS/mineflayer: Create Minecraft bots with a powerful, stable, and high level JavaScript API.](https://github.com/PrismarineJS/mineflayer)

PrismarineJS 的 Mineflayer 是一个用于创建 Minecraft 机器人的强大、稳定且高级的 JavaScript API，支持从 Python 使用。

- 🚀 **功能强大**：支持 Minecraft 1.8 至 1.21 版本，提供实体追踪、方块查询、物理运动、攻击实体、物品管理等功能。
- 📚 **文档丰富**：提供教程、API 参考、常见问题解答和变更日志，适合初学者和高级用户。
- 🔧 **易于使用**：通过简单的 npm 安装即可开始使用，支持自动版本检测和多种认证方式。
- 🌐 **多语言支持**：支持多种语言，包括中文，方便全球开发者使用。
- 🛠️ **模块化设计**：依赖多个模块如 minecraft-protocol、prismarine-physics 等，提供高度可定制性。
- 🔌 **插件支持**：支持第三方插件，如 pathfinder、prismarine-viewer 等，扩展机器人功能。
- 📹 **可视化工具**：通过 prismarine-viewer 可以在浏览器中实时查看机器人的行为。
- 📦 **丰富的示例**：提供多种示例代码，如路径查找、使用箱子、自动挖掘等，帮助快速上手。
- 🔄 **活跃社区**：有大量第三方项目和插件，社区活跃，持续更新和维护。
- 📜 **开源许可**：采用 MIT 许可证，允许自由使用和修改。

---

### [css-select | CSS 选择器编译器与引擎](https://feedic.com/css-select/)

**原文标题**: [css-select | a CSS selector compiler & engine](https://feedic.com/css-select/)

css-select 是一个 CSS 选择器编译器和引擎，能够将 CSS 选择器转换为可测试元素匹配的函数，并支持高效查询 DOM 树。

- 🛠️ **功能**：作为编译器，将 CSS 选择器转换为匹配函数；作为引擎，支持从顶部遍历 DOM 树。
- 🏗️ **默认配置**：基于 `domhandler` 模块的 DOM 结构，但支持通过选项查询其他 DOM 结构。
- 🌟 **特性**：完整支持 CSS3 和大部分 CSS4 选择器，部分支持 jQuery/Sizzle 扩展，高测试覆盖率，性能优异。
- 🔄 **执行方式**：采用从右到左的高效查询方式，避免重复检查，时间复杂度优化为 O(n)。
- 📚 **工作原理**：通过解析选择器生成函数堆栈，每个函数测试元素是否匹配选择器的某部分。
- 📜 **API**：提供 `selectAll`、`compile`、`is` 和 `selectOne` 等方法，支持查询、编译和测试元素。
- ⚙️ **选项**：包括 `xmlMode`、`rootFunc`、`adapter` 等，允许自定义查询行为和 DOM 交互方式。
- 🔌 **自定义适配器**：支持通过适配器接口与不同的 DOM 结构交互。
- 📌 **支持的选择器**：包括类型、后代、子代、属性、伪类等，以及部分 jQuery 扩展。
- 📜 **许可证**：采用 BSD-2-Clause 许可证。
- 🔒 **安全支持**：通过 Tidelift 报告漏洞，提供企业级支持选项。
- 👥 **维护**：由 `fb55` 维护，项目托管在 GitHub Pages。

---

### [GitHub - pixijs/pixijs: HTML5 创作引擎：用最快、最灵活的 2D WebGL 渲染器打造精美数字内容。](https://github.com/pixijs/pixijs)

**原文标题**: [GitHub - pixijs/pixijs: The HTML5 Creation Engine: Create beautiful digital content with the fastest, most flexible 2D WebGL renderer.](https://github.com/pixijs/pixijs)

PixiJS 是一个基于 WebGL 和 WebGPU 的下一代 HTML5 创作引擎，专注于创建精美的数字内容，提供最快的 2D 渲染能力。

- 🚀 **高性能渲染**：支持 WebGL 和 WebGPU，提供无与伦比的性能和速度。  
- 🎨 **易用且强大**：API 简单易用，同时功能强大。  
- 📦 **资源加载器**：内置资源加载功能，方便管理素材。  
- ✋ **交互支持**：完整的鼠标和多点触控支持。  
- ✍️ **灵活文本渲染**：支持多种文本渲染需求。  
- 📐 **多样化绘图**：支持基本图形和 SVG 绘制。  
- 🖼️ **动态纹理**：可创建和操作动态纹理。  
- 🎭 **遮罩与滤镜**：提供强大的遮罩和滤镜功能。  
- 🌈 **高级混合模式**：支持多种混合模式，增强视觉效果。  
- 📜 **开源与社区驱动**：采用 MIT 许可证，欢迎社区贡献。  
- 🔧 **快速上手**：通过 CLI 工具或 npm 安装，轻松集成到项目中。  
- 💡 **丰富文档**：提供指南、教程、示例和 API 文档，方便学习和使用。  
- 🤝 **活跃社区**：支持 Discord、Bluesky 等社区交流平台。

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=july4th2025)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=july4th2025)

Meticulous AI 提供了一种无需编写或维护测试的自动化测试解决方案，通过记录用户交互并利用 AI 生成覆盖所有边缘情况的测试套件，帮助开发团队快速、可靠地发布代码。

- 🚀 **无需编写测试** - Meticulous AI 自动生成并维护测试套件，覆盖应用程序的所有边缘情况。  
- 🔍 **记录用户交互** - 通过在开发、预演环境中添加脚本标签，记录用户会话以生成测试用例。  
- 🤖 **AI 驱动测试** - AI 引擎持续生成和更新测试套件，确保覆盖每一行代码和每个用户流程。  
- ⚡ **快速反馈** - 在合并代码前查看 PR 对用户工作流的影响，避免回归问题。  
- 🛠️ **无干扰测试** - 默认模拟后端响应，消除因数据变化导致的误报，无需设置测试账户或模拟数据。  
- 🔄 **自动更新** - 测试套件随应用程序的演进而自动更新，无需手动干预。  
- 🚫 **消除测试波动** - 基于 Chromium 的确定性调度引擎，彻底消除测试波动，执行速度极快。  
- 💡 **客户认可** - 受到 Dropbox、Notion、Lattice 等 100 多家组织的信任，显著提升代码质量和开发效率。  
- 🔗 **灵活集成** - 支持与现有测试套件结合使用或完全替代，兼容 NextJS、React、Vue 等多种框架。  
- ⏱️ **高效并行测试** - 在计算集群上并行运行数千次测试，120 秒内返回结果。  
- 📥 **快速上手** - 只需几分钟设置，即可开始为整个应用程序生成测试。

---

### [定价 | ConfigCat 功能开关](https://configcat.com/pricing/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_js_202506)

**原文标题**: [Pricing | ConfigCat Feature Flags](https://configcat.com/pricing/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_js_202506)

概述  
ConfigCat 提供功能开关和远程配置服务，支持多环境、多产品管理，并提供免费和付费计划。其核心功能包括审计日志、百分比目标、团队协作和安全合规支持。定价灵活，按需选择，适合从个人开发者到企业级用户的不同需求。

- 🔍 **产品介绍** - ConfigCat 是一个功能开关（Feature Flag）和远程配置管理平台，支持多环境和多产品管理。  
- ⚙️ **工作原理** - 通过 CDN 存储和分发配置 JSON 文件，SDK 本地缓存并定期更新，实现快速功能切换。  
- 💡 **核心优势** - 提供审计日志、强制修改理由、企业级代码托管服务（Escrow），确保安全与透明。  
- 💰 **定价计划** - 提供免费、Pro、Smart、Enterprise 和 Dedicated 计划，支持按月或按年付费，欧元和美元两种货币。  
- 📊 **免费计划** - 永久免费，包含 10 个功能开关、2 个环境和 2 个产品。  
- 🚀 **付费计划** - 从 Pro 到 Dedicated，资源逐级提升，支持无限功能开关、环境和定制协议。  
- 🌐 **网络流量** - 不同计划包含 20GB 到 24TB 不等的月度流量，满足不同规模需求。  
- 🔒 **安全合规** - 支持 2FA、SSO、SAML、SCIM，符合 GDPR 和 ISO 27001:2013 标准。  
- 👥 **团队协作** - 无限团队成员、服务连接和月度活跃用户（MAUs），支持权限分组管理。  
- 📚 **开发支持** - 提供多种 SDK、API、Webhooks 和技术债务工具，集成主流开发平台。  
- 🌳 **环保承诺** - 每笔订阅都会植树，减少碳足迹。  
- 🎓 **教育优惠** - 为学生和教师提供定制计划，支持教育项目。  
- 📞 **客户支持** - 从社区支持到专属 SLA，满足不同客户需求。  
- 📜 **合规与法律** - 提供软件托管服务（Escrow）、Cookie 政策和隐私条款，确保用户数据安全。

---

### [获取失败](https://javascriptweekly.com/link/171412/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/171412/web)

无法总结：获取内容失败，状态码 403。

---

### [容器现已公开测试，提供简单、全球可编程的计算服务](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/)

**原文标题**: [Containers are available in public beta for simple, global, and programmable compute](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/)

Cloudflare Containers 现已面向付费用户开放公测，支持与 Workers 无缝集成，提供全球化、可编程的容器化计算能力。

- 🚀 **公测上线**：Cloudflare Containers 进入公测阶段，付费用户均可使用。  
- 🌍 **全球化部署**：容器与 Workers 深度集成，支持一键部署至全球边缘节点（Region:Earth）。  
- 🔧 **灵活开发**：支持多种应用场景（如边缘数据处理、后端服务、CLI 工具），可通过 `wrangler deploy` 快速部署。  
- 🛠️ **编程控制**：容器实例由 Workers 代码动态调度，无需手动管理区域配置或 Kubernetes 算子。  
- 📦 **示例应用**：演示代码沙箱场景，通过路径路由（如 `/sandbox/ID`）自动隔离用户容器实例。  
- 🔄 **开发流程**：`wrangler dev` 支持本地镜像实时构建与调试，按需重启容器。  
- 📊 **内置监控**：控制台提供资源使用指标和日志（保留 7 天），支持外推至第三方日志服务。  
- 💰 **透明计费**：按实际使用量计费（CPU/内存/磁盘），包含免费额度，流量分级定价。  
- 🔮 **未来计划**：包括更大实例规格、全局自动扩缩容、容器-Workers 通信增强及开发者平台深度集成。  
- 🎯 **快速体验**：提供模板和文档，支持一键部署示例项目（如 FFmpeg 转码、定时任务等）。

---

### [单进程运行百万棋盘国际象棋大型多人在线游戏 · eieio.games](https://eieio.games/blog/a-million-realtime-chess-boards-in-a-single-process/)

**原文标题**: [Running a million-board chess MMO in a single process · eieio.games](https://eieio.games/blog/a-million-realtime-chess-boards-in-a-single-process/)

overview summary  
《One Million Chessboards》是一款由 Nolen Royalty 开发的实时多人国际象棋 MMO 游戏，支持 1000x1000 棋盘网格，玩家可跨棋盘移动棋子且无需回合制。游戏采用单进程架构，通过优化协议和分布式设计处理高并发，实现了低延迟和高效带宽利用。尽管游戏在规则和用户体验上存在争议，但其技术实现和规模表现获得了广泛关注。

- 🎮 游戏规则：实时跨棋盘移动棋子，无回合限制，但禁止跨棋盘捕获，形成独特玩法（如“Rooklyn”）。  
- 🚀 技术架构：单进程 Golang 实现，使用全局读写锁保护 8000x8000 棋盘数组，通过分区（Zones）和批量更新降低带宽消耗。  
- 📊 性能优化：采用 Protobuf 和 Zstd 压缩数据，实测带宽节省超 90%；快照和移动批次分发策略避免加载延迟。  
- 🔄 回滚机制：客户端乐观预测移动，依赖服务端验证和冲突解决（如图依赖分析），实现零延迟操作。  
- 💡 经验教训：初始设计过于追求规模而牺牲易用性；玩家分布策略未能营造“万人同屏”的震撼感。  
- 💰 成本控制：优化后服务器月成本约 80 美元，依赖 Cloudflare 缓存和数字海洋实例。  
- ❤️ 玩家反馈：隐藏成就等细节体现开发诚意，但部分国际象棋玩家对规则改动不满。  
- 📅 开发历程：耗时远超以往项目，克服技术挑战（如原子操作误区）并验证 Go 语言的并发优势。  

（注：Emoji 根据内容关联性添加，如技术类用🚀、优化用📊、情感反馈用❤️等）

---

### [客座文章：我是如何扫描 GitHub 所有“意外提交”以查找泄露的机密 ✦ Truffle Security 公司](https://trufflesecurity.com/blog/guest-post-how-i-scanned-all-of-github-s-oops-commits-for-leaked-secrets)

**原文标题**: [Guest Post: How I Scanned all of GitHubâs âOops Commitsâ for Leaked Secrets â Truffle Security Co.](https://trufflesecurity.com/blog/guest-post-how-i-scanned-all-of-github-s-oops-commits-for-leaked-secrets)

概述：本文介绍了 AI 编码助手可能带来的安全风险，并详细描述了一项研究，通过扫描 GitHub 上被强制推送删除的提交（“Oops Commits”）来发现泄露的敏感信息。研究发现了大量活跃的密钥，包括高价值的 GitHub 个人访问令牌和 AWS 凭证，并开发了一个开源工具来帮助组织扫描这些隐藏的提交。

- 🔍 GitHub 存档记录了所有公开提交，包括开发者尝试删除的提交，这些提交可能包含泄露的敏感信息。
- 💰 扫描自 2020 年以来的所有零提交强制推送事件，发现了价值 25,000 美元的漏洞赏金。
- 🛠️ 开源工具 Force Push Scanner 可以帮助组织扫描这些隐藏的提交，发现潜在的敏感信息泄露。
- 🔄 强制推送（force push）会覆盖 Git 历史，但 GitHub 仍然保留这些被删除的提交，使其仍可访问。
- 📅 通过 GitHub 事件 API 和 GH Archive 项目，可以大规模扫描所有被删除的提交。
- 🚨 案例研究：发现了一个具有 Istio 所有仓库管理员权限的 GitHub 个人访问令牌，可能引发大规模供应链攻击。
- 📊 数据分析显示，.env 文件是最常泄露敏感信息的文件类型，其次是 index.js 和 application.properties。
- 🤖 尝试利用 AI 自动分析泄露的敏感信息，以识别具有高价值的密钥。
- 🔑 研究发现，即使提交被删除，敏感信息仍可能被访问，因此一旦泄露应立即撤销相关密钥。
- 📢 呼吁改变“删除提交即安全”的常见假设，强调任何在线提交的敏感信息都应视为已泄露。

---

### [发布 PlanetScale for Postgres —— PlanetScale](https://planetscale.com/blog/planetscale-for-postgres)

**原文标题**: [Announcing PlanetScale for Postgres â PlanetScale](https://planetscale.com/blog/planetscale-for-postgres)

PlanetScale 宣布推出 Postgres 私有预览版，这是全球最快的 Postgres 托管平台，已开始支持客户的生产工作负载，并展现出卓越性能。

- 🚀 发布 PlanetScale for Postgres 私有预览版，客户可通过链接申请访问。  
- 🔍 客户需求驱动：因大量企业要求支持 Postgres，PlanetScale 决定扩展服务。  
- ⚡ 性能与可靠性：经过 50 多家客户调研，PlanetScale 旨在提供卓越工程解决方案，基准测试显示其性能超越所有现有 Postgres 产品。  
- 💾 技术优势：采用真实 Postgres 运行于专有操作器，支持高可用性、自动故障转移、查询缓冲和连接池，运行 Postgres v17 并支持在线导入。  
- 💡 创新存储：PlanetScale Metal 的本地 NVMe SSD 显著提升云中关系数据库的性能成本比。  
- 🔄 Vitess 未来支持：虽 Vitess 以 MySQL 为核心，但 PlanetScale 正从零构建新系统为 Postgres 提供类似扩展能力。  
- 🤝 社区参与：欢迎大规模使用 Postgres 的公司联系合作，共同验证产品成熟度。  
- 📅 提供私有预览等待列表注册，期待加入 Postgres 社区。

---

### [Postgres 基准测试 —— PlanetScale](https://planetscale.com/blog/benchmarking-postgres)

**原文标题**: [Benchmarking Postgres â PlanetScale](https://planetscale.com/blog/benchmarking-postgres)

PlanetScale 发布了 Postgres 服务，并通过内部工具“Telescope”进行性能基准测试，确保其数据库性能达到高标准。测试结果与其他主流 Postgres 供应商进行了对比，并公开了测试方法和结果。

- 🔍 PlanetScale 推出 Postgres 服务，致力于打造最佳性能体验。  
- 🛠️ 使用内部工具“Telescope”进行标准化、可重复的基准测试。  
- 📊 公开测试结果，包括与 Amazon Aurora、Google AlloyDB 等主流供应商的对比。  
- ⚖️ 测试力求公平，匹配或超过竞争对手的资源配置。  
- 💡 基准测试关注延迟、OLTP 负载、读写压力及性价比等关键问题。  
- 📈 测试结果显示 PlanetScale 在性能上显著优于其他供应商。  
- 📝 提供详细的测试方法和配置，确保透明度和可重复性。  
- 📧 邀请其他供应商提供反馈，确保测试方法的准确性。

---

### [入门指南 🌟 Strudel](https://strudel.cc/workshop/getting-started/)

**原文标题**: [
      Getting Started ð Strudel
    ](https://strudel.cc/workshop/getting-started/)

Strudel 是一个基于 JavaScript 的音乐编程工具，灵感来自 Tidal Cycles 模式语言，适合实时编码音乐、算法作曲和教学。

- 🎵 **什么是 Strudel**：Strudel 是一个动态音乐编程工具，无需 JavaScript 或 Tidal Cycles 基础即可使用。  
- 🎹 **功能亮点**：支持实时编码、算法作曲、教学集成，并可通过 MIDI/OSC 与现有音乐设备连接。  
- 🎧 **示例展示**：提供丰富的音乐示例，如《coastline》，展示其多样化的音乐生成能力。  
- 🚀 **快速入门**：推荐通过互动教程和 Strudel REPL 开始学习，适合新手快速上手。  
- 📚 **学习资源**：包含工作坊、文档和社区支持（如 Mastodon 上的 @strudel）。  
- 🔧 **技术扩展**：支持音频采样、合成器、效果器、MIDI/OSC 等高级功能，并兼容 Hydra 和 CSound。  
- 🌍 **社区互动**：鼓励用户编辑文档、参与社区交流，探索更多创意可能。

---

