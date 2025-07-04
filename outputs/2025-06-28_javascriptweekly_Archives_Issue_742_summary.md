### [JavaScript 周刊第 742 期：2025 年 6 月 27 日](https://javascriptweekly.com/issues/742)

**原文标题**: [JavaScript Weekly Issue 742: June 27, 2025](https://javascriptweekly.com/issues/742)

- 🌐 Ecma 国际批准了 ECMAScript 2025 规范，详细内容可查阅官方文档或 Dr. Axel 的简明解析。  
- 🚀 Deno 团队分享了 9 个正在 TC39 流程中的 JavaScript 新提案，包含代码示例。  
- 🛠 Maximiliano Firtman 推出视频课程，教你用原生 JavaScript 和 Go 构建高性能全栈应用。  
- ⚡ Vite 7.0 发布，作为前端构建工具的重要升级，从 v6 迁移更轻松。  
- 📅 JSConf 2025 演讲阵容公布，10 月在美国马里兰州举行。  
- 🔧 V8 团队优化 WebAssembly 性能，Shopify 探讨 React Native 高级图形技术。  
- 🎮 Construct 游戏开发环境新增 TypeScript 支持。  
- 🤖 Angular 团队发布 LLM 提示词和 AI IDE 规则文件，帮助开发者生成更优代码。  
- 🌟 Vercel 年度活动发布多项公告，涵盖新产品和更新。  
- ⏳ Temporal API 提案进入 Stage 3 草案阶段。  
- 📦 发布更新：Transformers.js 3.6、zx 8.6、Node.js 多版本、Prettier 3.6 等。  
- 📖 文章推荐：正则表达式技巧、OAuth 指南、RSS 服务器端阅读器实现等。  
- 🛠️ 工具推荐：Hono 4.8 框架、LogTape 1.0 日志库、Google 开源 Gemini CLI AI 代理。  
- 📊 图表库更新：Billboard.js 3.16、AG Charts 12.0、Recharts 3.0。  
- 🎁 其他亮点：Google 发布 Gemma 3n 轻量级 LLM、John Carmack 谈 AI 研究、zsh 历史记录禁用技巧等。

---

### [Ecma 国际批准 ECMAScript 2025：有哪些新变化？](https://2ality.com/2025/06/ecmascript-2025.html)

**原文标题**: [Ecma International approves ECMAScript 2025: What’s new?](https://2ality.com/2025/06/ecmascript-2025.html)

ECMA 国际批准了 ECMAScript 2025 语言规范，新增多项功能，包括导入属性、迭代器辅助方法、新 Set 方法等。

- 🎉 ECMAScript 2025 于 2025 年 6 月 25 日正式成为标准。
- 📥 新增导入属性和 JSON 模块，支持非 JavaScript 资源的导入。
- 🔄 迭代器辅助方法（如 filter、map、drop 等）增强了对可迭代数据结构的操作能力。
- 🔍 新增 Set 方法（如 intersection、union、difference 等），方便集合操作。
- 🛡️ 引入 RegExp.escape()，用于正则表达式文本转义。
- 🏷️ 正则表达式模式修饰符（内联标志）允许对部分正则应用标志。
- 🔄 支持重复命名捕获组，可在不同备选方案中使用相同组名。
- ⏳ 新增 Promise.try()，便于启动可能抛出异常的 Promise 链。
- 🔢 支持 16 位浮点数（float16），新增 Math.f16round() 和 Float16Array 等。
- 📚 提供免费在线书籍《Exploring JavaScript (ES2025 Edition)》，涵盖 JavaScript 历史和新增功能。

---

### [ECMAScript® 2025 语言规范](https://tc39.es/ecma262/2025/)

**原文标题**: [ECMAScript® 2025 Language Specification](https://tc39.es/ecma262/2025/)

总结失败：Error code: 400 - {'error': {'message': "This model's maximum context length is 65536 tokens. However, you requested 611050 tokens (603050 in the messages, 8000 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

### [JavaScript 新动态 | Deno](https://deno.com/blog/updates-from-tc39)

**原文标题**: [What's coming to JavaScript | Deno](https://deno.com/blog/updates-from-tc39)

Deno 致力于推动 JavaScript 生态发展，参与 TC39 标准制定，近期有 9 项提案进入不同阶段，涵盖资源管理、异步迭代、错误检测等功能优化，旨在提升开发效率和代码安全性。

- 🚀 **TC39 提案进展**：9 项提案分属 4 个阶段（Stage 0 至 Stage 4），涉及资源管理、数组操作、错误检测等。  
- 🔧 **Stage 4 特性**  
  - `using`声明：自动资源清理（如文件句柄），支持同步/异步释放（`Symbol.dispose`/`Symbol.asyncDispose`）。  
  - `Array.fromAsync`：异步迭代转数组，简化异步数据收集。  
  - `Error.isError`：可靠检测 Error 对象（包括跨域或子类）。  
- 🛡️ **Stage 3 特性**  
  - `Immutable ArrayBuffer`：不可变二进制数据，提升多线程安全性（`transferToImmutable`/`sliceToImmutable`）。  
- 🎲 **Stage 2 特性**  
  - `Random.Seeded`：可复现的伪随机数生成器（指定种子）。  
  - `Number.prototype.clamp`：数值范围限制（替代`Math.min/max`链式调用）。  
- 📊 **Stage 1 特性**  
  - `Keep Trailing Zeros`：精细化数字格式化（如货币显示）。  
  - `Comparisons`：标准化值比较输出（用于测试框架等）。  
  - `Random Functions`：安全的随机数生成工具（如加权抽样、数组乱序）。  
- 🌐 **Deno 实践**：已集成部分提案（如`using`管理资源、`async context`追踪），并计划优化二进制 API 性能。  
- ⏭️ **下一步**：TC39 将于 9 月下旬继续讨论提案，Deno 同步推进标准兼容性（如 OpenTelemetry 集成）。

---

### [Vite 7.0 正式发布！ | Vite](https://vite.dev/blog/announcing-vite7.html)

**原文标题**: [Vite 7.0 is out! | Vite](https://vite.dev/blog/announcing-vite7.html)

Vite 7.0 正式发布！这是自 Evan You 提交首个 Vite 代码库以来的第五年，前端生态系统已发生巨大变化。Vite 现已成为现代前端框架和工具的共享基础设施，每周下载量达 3100 万次，比上次大版本发布后七个月内增长了 1400 万次。

- 🎉 **ViteConf 线下活动**：10 月 9-10 日将在阿姆斯特丹举办，由 JSWorld、Bolt、VoidZero 和 Vite 核心团队联合组织。
- 🚀 **Rolldown 集成**：VoidZero 开发的 Rust 打包工具 Rolldown 现可作为 `rolldown-vite` 包使用，未来将成为 Vite 默认打包工具，显著提升大型项目构建速度。
- 🔧 **Vite DevTools**：Anthony Fu 与 NuxtLabs 合作开发，为基于 Vite 的项目提供更深入的调试和分析功能。
- 🌍 **多语言支持**：新增波斯语文档，其他语言包括简体中文、日语、西班牙语等。
- ⚡ **Node.js 支持**：Vite 7.0 要求 Node.js 20.19+ 或 22.12+，不再支持已终止维护的 Node.js 18。
- 🎯 **默认浏览器目标更新**：从 `'modules'` 改为 `'baseline-widely-available'`，提升未来版本的兼容性预测。
- 🧪 **Vitest 支持**：Vite 7.0 需搭配 Vitest 3.2 使用，进一步优化测试体验。
- 🔌 **环境 API 改进**：新增 `buildApp` 钩子，插件可协调环境构建，API 仍处于实验阶段，欢迎反馈。
- 📦 **迁移指南**：Vite 7.0 从 Vite 6 升级平滑，移除了已弃用的功能，建议查看详细迁移指南。
- 🙏 **致谢**：感谢 Vite 团队、贡献者及赞助商，特别鸣谢 sapphi-red 在 Rolldown 和本次发布中的卓越工作。

---

### [Vite | 下一代前端构建工具](https://vite.dev/)

**原文标题**: [Vite | Next Generation Frontend Tooling](https://vite.dev/)

Vite 是一个现代化的前端构建工具，提供快速、高效的开发体验。

- 🚀 **主要导航**：包括指南、配置、插件、资源等核心功能入口  
- 🔗 **社区链接**：提供 Bluesky、Mastodon、X（推特）、Discord 等社交平台连接  
- 📚 **文档版本**：支持 Vite 2 至 Vite 6 多个版本的文档查阅  
- 🌍 **多语言**：支持简体中文、英文、日语、西班牙语等 8 种语言  
- 🎨 **外观设置**：可自定义界面显示样式

---

### [从 v6 迁移 | Vite](https://vite.dev/guide/migration)

**原文标题**: [Migration from v6 | Vite](https://vite.dev/guide/migration)

Vite 6 版本更新内容概述，包括 Node.js 支持变更、默认浏览器目标调整、移除旧 API 及废弃功能等。

- 🚨 **Node.js 支持变更**  
  Vite 6 不再支持已终止维护的 Node.js 18，最低要求变更为 Node.js 20.19+ 或 22.12+。

- 🌐 **默认浏览器目标升级**  
  构建目标`build.target`默认值更新为 2025 年广泛支持的浏览器版本（如 Chrome 107、Safari 16.0），旧选项`'modules'`被替换为`'baseline-widely-available'`。

- 🔧 **移除 Sass 旧版 API 支持**  
  不再兼容 Sass 遗留 API，需删除配置中的`css.preprocessorOptions.sass.api`相关选项。

- 🗑️ **废弃功能移除**  
  - 移除`splitVendorChunkPlugin`插件（v5.2.7 已废弃），推荐使用`build.rollupOptions.output.manualChunks`控制代码分割。  
  - 废弃`transformIndexHtml`钩子的`enforce/transform`参数（v4.0.0 已废弃），改用`order`和`handler`。

- ⚙️ **高级变更**  
  - 清理无用的遗留属性（如`legacy.proxySsrExternalModules`、`ModuleRunnerOptions.root`等）。  
  - SSR 相关：`__vite_ssr_exportName__`现为必填项，`optimizeDeps.entries`仅接受 glob 模式路径。  
  - 中间件执行顺序调整：部分中间件现会在`configureServer`/`configurePreviewServer`钩子前应用。

- 📚 **迁移建议**  
  若从 Vite 5 升级，需先查阅 Vite 6 官方迁移指南，再处理本页列出的变更。

---

### [JSConf 2025 演讲嘉宾公布 | OpenJS 基金会](https://openjsf.org/blog/jsconf-25-speakers-announced)

**原文标题**: [JSConf 2025 Speakers Announced | OpenJS Foundation](https://openjsf.org/blog/jsconf-25-speakers-announced)

OpenJS 基金会宣布了 JSConf 2025 的演讲者阵容，会议将于 10 月 14 日至 16 日在马里兰州切萨皮克湾举行，涵盖前端性能、AI、编译器等多个主题。

- 🎤 **主题演讲嘉宾**：包括 VoidZero 创始人 Evan You、Bun 创始人 Jarred Sumner 等业界领袖。
- 🚀 **专题演讲**：涵盖性能优化、JavaScript 框架、安全隐私、AI 与新兴技术等热门话题。
- 🛠 **开发者工具与实践**：探讨模块化、CSS/HTML 替代方案等实用技巧。
- 🌍 **开源与社区**：分享开源协作、技术决策和文化建设的经验。
- ♿ **UI/UX与无障碍**：案例研究如何构建无障碍界面及优化用户体验。
- 📅 **注册提醒**：鼓励尽早注册以锁定参会名额。

---

### [基于去优化与内联的 WebAssembly 推测性优化 · V8 引擎](https://v8.dev/blog/wasm-speculative-optimizations)

**原文标题**: [Speculative Optimizations for WebAssembly using Deopts and Inlining · V8](https://v8.dev/blog/wasm-speculative-optimizations)

概述  
V8 引擎在 Google Chrome M137 中实现了两项针对 WebAssembly 的优化：推测性间接调用内联和去优化支持。这些优化通过基于运行时反馈的假设生成更高效的机器代码，显著提升了 WebAssembly 的执行速度，尤其是对 WasmGC 程序的优化效果更为明显。结合两项优化后，Dart 微基准测试平均提速超过 50%，实际应用和基准测试的提速范围在 1% 至 8% 之间。去优化还为未来更多优化奠定了基础。

- 🚀 **优化概述**  
  V8 引擎新增两项 WebAssembly 优化：推测性间接调用内联和去优化支持，显著提升执行速度。

- 📊 **性能提升**  
  结合两项优化后，Dart 微基准测试平均提速超 50%，实际应用提速 1%-8%。

- 🔍 **背景与动机**  
  WebAssembly 的静态类型特性使其易于优化，但 WasmGC 的引入使得推测性优化更为重要，尤其是针对高层次的类型和操作。

- 🛠️ **推测性内联**  
  通过运行时反馈记录间接调用的目标函数，优化时内联高频目标，提升执行效率并启用后续优化。

- 🔄 **去优化机制**  
  当运行时行为与优化假设不符时，回退到未优化代码，确保正确性同时避免生成复杂的慢路径代码。

- 📈 **技术细节**  
  反馈向量记录调用目标信息，优化编译器根据反馈决定内联策略，去优化时保存并转换程序状态以继续执行。

- ⚡ **实际效果**  
  在 Dart 微基准测试中，单独启用间接调用内联提速 1.19 倍，结合去优化后提速 1.59 倍；实际应用如 SQLite 和 Google Sheets 也有显著提升。

- 🔮 **未来展望**  
  计划扩展推测性优化范围，如边界检查消除和 WasmGC 对象的负载消除，并探索跨语言内联（如 JavaScript 到 Wasm 调用）。

---

### [React Native 图形技术的未来：WebGPU、Skia 及其他（2025 年） - Shopify](https://shopify.engineering/webgpu-skia-web-graphics)

**原文标题**: [The Future of React Native Graphics: WebGPU, Skia, and Beyond (2025) - Shopify](https://shopify.engineering/webgpu-skia-web-graphics)

React Native 图形技术的未来因 WebGPU 和 Skia 的引入而迎来重大革新，包括性能提升、跨平台支持扩展以及 2D/3D 图形无缝结合等突破性进展。

- 🚀 **WebGPU 的变革性影响**：通过统一后端架构（如 Dawn 实现），减少平台差异（OpenGL/Metal），并支持通用 GPU 计算（如机器学习）。  
- 🌐 **与 Web 生态对齐**：借助 Three.js 和 TensorFlow.js 等工具，实现 Web 与原生应用的无缝兼容。  
- 🎨 **Three.js 与 React Three Fiber 原生支持**：通过 WebGPU 和 TSL 着色语言，同一套 3D 代码可跨 Web 和移动端运行（如 Shopify 黑五地球仪案例）。  
- ⚡ **性能优化**：React Native Skia 架构改进（如不可变场景图）使动画性能提升 50%-200%，并减少 13% 代码量。  
- 📱 **多平台扩展**：新增 macOS、tvOS 和 Node.js 支持，实现“一次编写，多端渲染”（如动态生成 Open Graph 预览）。  
- 🔮 **Skia Graphite 前瞻**：实验性支持自动线程管理和 2D/3D 混合渲染，为创意场景打开新可能。  
- 🤖 **机器学习集成**：WebGPU 支持 TensorFlow.js 在移动端运行，赋能实时图像处理等 ML 任务。  
- 🛠️ **开发者工具丰富**：ComputeToys 等工具推动计算着色器艺术和 GPU 计算应用。  
- ❤️ **社区致谢**：强调 React Native 社区的贡献是技术演进的核心动力。

---

### [游戏制作软件 - Construct 3](https://www.construct.net/en)

**原文标题**: [
	Game Making Software - Construct 3 
](https://www.construct.net/en)

每月有超过 25 万用户使用 Construct 3 制作游戏，它是一款基于浏览器的尖端游戏开发工具，无需编码即可轻松创建游戏。

- 🎮 **无需编程**：通过可视化脚本和事件表快速制作游戏  
- 💡 **支持 JavaScript**：可结合 JavaScript 扩展功能，提升游戏控制力  
- 🌍 **广泛使用**：全球开发者使用，每年 195 万创作者，每月新增 20 万项目  
- 🚀 **高性能**：运行速度快，支持复杂游戏开发  
- 🔄 **持续更新**：定期推出新功能和改进  
- 🛠️ **功能全面**：内置图像编辑、物理引擎、路径寻找等工具  
- 📱 **多平台发布**：支持 Android、iOS、Windows 等 10+ 平台  
- 🆓 **免费试用**：提供初学者指南和交互式教程帮助入门

---

### [Construct 现已内置支持 TypeScript](https://www.construct.net/en/blogs/construct-official-blog-1/construct-built-in-support-1894)

**原文标题**: [
	Construct now has built-in support for TypeScript
](https://www.construct.net/en/blogs/construct-official-blog-1/construct-built-in-support-1894)

Construct 现已内置支持 TypeScript，用户可直接在编辑器中使用.ts 文件，享受类型检查和项目特定细节支持。

- 🎉 Construct 编辑器现支持 TypeScript，无需外部工具即可编写.ts 文件  
- 📝 TypeScript 是 JavaScript 的扩展，添加静态类型以提升代码正确性和工具支持  
- 🔧 类型注解帮助捕获错误，如参数类型不匹配，提升开发效率  
- ⚡ TypeScript 编译为 JavaScript，保持相同的高性能  
- 🛠️ 在 Construct 中，TypeScript 文件可直接添加到事件表和项目栏，自动编译为.js  
- 🔍 类型系统提供精确的自动完成，避免无关建议，提升编码体验  
- 🚨 TypeScript 能捕获潜在错误，如实例方法误用，适合初学者和大型项目  
- 🔄 支持在 JavaScript 和 TypeScript 之间切换，包括批量重命名文件  
- 📚 新增大量 TypeScript 文档、示例和教程，与 JavaScript 支持并重  
- 🌟 内置 Monaco 编辑器支持高级功能如“转到定义”，TypeScript 下更精准  
- 🔗 支持.d.ts 类型定义文件和 JavaScript/TypeScript 代码互操作  
- 🎥 正在制作 TypeScript 视频教程，未来将发布更多资源  
- 🏆 此次更新是 Construct 自 2019 年引入 JavaScript 后最大的编码能力升级  
- 💼 使用行业标准语言（如 TypeScript）学习真实技能，助力职业发展  
- ⏭️ 未来开发重点将回归 Construct 其他功能，如游戏服务和资源管理器

---

### [LLM 提示词与 AI 集成开发环境搭建 • Angular 框架](https://angular.dev/ai/develop-with-ai)

**原文标题**: [LLM prompts and AI IDE setup • Angular](https://angular.dev/ai/develop-with-ai)

Angular 官方文档提供了关于使用大型语言模型（LLM）生成 Angular 代码的指南和资源，旨在帮助开发者更准确地生成符合 Angular 最佳实践的代码。

- 🚀 **Angular 与 LLM 结合**：介绍了如何利用 LLM 生成符合 Angular 最佳实践的代码，并提供了定制提示和系统指令。  
- 📝 **最佳实践文件**：提供`best-practices.md`文件，包含 TypeScript 和 Angular 的编码规范，如使用严格类型检查、独立组件和信号管理等。  
- ⚙️ **规则文件**：针对不同开发环境（如 Firebase Studio、VS Code 等）提供了特定的规则文件，以优化 LLM 生成的代码。  
- 📂 **上下文文件**：通过`llms.txt`和`llms-full.txt`文件，帮助 LLM 更好地理解和处理 Angular 相关内容。  
- 🔧 **开发工具支持**：列出了支持 LLM 集成的开发工具和 IDE，并提供了相应的配置指南。  
- 🌐 **社区与资源**：提供了 Angular 社区、社交媒体和相关资源的链接，方便开发者获取更多支持。

---

### [Vercel Ship 2025 精彩回顾 - Vercel](https://vercel.com/blog/vercel-ship-2025-recap)

**原文标题**: [Vercel Ship 2025 recap - Vercel](https://vercel.com/blog/vercel-ship-2025-recap)

Vercel Ship 2025 展示了面向未来的应用开发工具和平台增强功能，重点聚焦 AI、计算、安全和团队协作。

- 🚀 **Vercel Ship 2025 活动**：超过 1200 人参与，探讨 AI、计算和安全等领域的最新进展。
- 🤖 **AI Gateway**：提供统一端点访问多 AI 模型，支持快速切换供应商和智能路由请求。
- 💡 **Fluid 和 Active CPU 定价**：优化 AI 推理和代理工作负载，显著降低成本并提升效率。
- 🛡️ **Vercel Sandbox**：安全运行不受信任代码的隔离环境，支持 Node.js 和 Python。
- 🔄 **Rolling Releases**：支持增量部署和实时监控，确保安全高效的版本发布。
- � **Microfrontends**：允许团队独立开发和部署应用模块，提升开发速度和灵活性。
- 🤖 **BotID**：通过隐形 CAPTCHA 技术防御自动化攻击，保护关键路由。
- 🔍 **Vercel Agent**：内置 AI 助手，分析应用性能和安全性，提供优化建议。
- 📊 **Vercel Queue**：支持后台任务处理，确保长时间运行作业的完成。
- 🌐 **AI Cloud 愿景**：从 Frontend Cloud 向 AI Cloud 演进，构建适应 AI 原生时代的平台。

---

### [时间性](https://tc39.es/proposal-temporal/)

**原文标题**: [Temporal](https://tc39.es/proposal-temporal/)

总结失败：Error code: 400 - {'error': {'message': "This model's maximum context length is 65536 tokens. However, you requested 180237 tokens (172237 in the messages, 8000 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

### [发布 3.6.0 版 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.6.0)

**原文标题**: [Release 3.6.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.6.0)

Hugging Face 发布了 Transformers.js v3.6 版本，新增支持 Gemma 3n、Qwen3-Embedding 和 Llava-Qwen2 等模型，并包含多项改进。

- 🚀 **Gemma 3n 模型发布**：支持多模态输入（图像、文本、音频、视频），采用 MatFormer 架构，提供 ONNX 权重，目前仅支持 Node.js、Deno 和 Bun 运行。
- 🤖 **Qwen3-Embedding 模型**：专为文本嵌入和排序任务设计，支持多语言和长文本理解，提供多种尺寸（0.6B、4B、8B）。
- 🛠️ **Llava-Qwen2 支持**：新增对 Llava 模型的支持，基于 Qwen2 文本骨干。
- 📈 **其他改进**：优化了 Deno/Bun 的检测和使用，增加了 eos/last_token 池化功能。
- ⚠️ **注意事项**：Gemma 3n 模型因体积较大，暂不支持浏览器 WebGPU 运行，相关支持正在开发中。

---

### [发布 8.6.0 版本 — Valve Vanguard · google/zx · GitHub](https://github.com/google/zx/releases/tag/8.6.0)

**原文标题**: [Release 8.6.0 — Valve Vanguard · google/zx · GitHub](https://github.com/google/zx/releases/tag/8.6.0)

页面加载错误，请重新加载。  

- ⚠️ 页面加载时出现错误，需重新加载。  
- 🔔 必须登录才能更改通知设置。  
- 📊 项目数据：1.1k Fork，44.3k Star，13 Issues，3 Pull requests。  
- 🚀 最新版本 8.6.0 发布，包含多项内部重构和功能改进。  
- 🔧 新增`thenable`参数处理功能，示例代码展示其用法。  
- 📦 依赖更新，文档改进，体积优化。  
- ❤️ 7 人点赞，🚀1 人点赞，👀3 人关注。

---

### [Node.js — Node v22.17.0（长期支持版）](https://nodejs.org/en/blog/release/v22.17.0)

**原文标题**: [Node.js — Node v22.17.0 (LTS)](https://nodejs.org/en/blog/release/v22.17.0)

Node v22.17.0 (LTS) 版本发布，包含多项功能改进、弃用警告和错误修复。

- 🚨 **弃用警告**  
  - 不推荐使用 `new` 关键字实例化 `node:http` 类（如 `IncomingMessage` 或 `ServerResponse`）。  
  - 在 `node:child_process` 中使用空字符串 `options.shell` 的行为不再支持。  
  - HTTP/2 优先级信号 API（如 `stream.priority`）已弃用。  

- ✅ **稳定功能**  
  - `assert.partialDeepStrictEqual()` 方法正式稳定，支持部分属性深度比较。  
  - 新增多项稳定 API，如 `fs.glob()`、`fs.openAsBlob()` 和 `URL.createObjectURL()`。  

- 🔧 **新功能与改进**  
  - `fs.FileHandle.readableWebStream` 新增 `autoClose` 选项，避免资源泄漏。  
  - `fs.Dir` 支持显式资源管理（如 `Symbol.asyncDispose`）。  
  - HTTP/2 新增诊断通道 `http2.server.stream.finish`，便于监控。  
  - 权限模型默认允许对入口文件的读取访问。  
  - `util.styleText()` 新增 `'none'` 样式，用于清除终端样式。  

- 🛠️ **其他更新**  
  - 社区新增多位贡献者和 TSC 成员。  
  - 多项错误修复和性能优化，包括文件系统操作、HTTP/2 和缓冲区处理。  

- 📥 **下载支持**  
  - 提供 Windows、macOS、Linux 等多平台安装包和二进制文件。  

- 📜 **文档与安全**  
  - 更新文档和错误提示，修复已知安全问题。

---

### [Node.js — Node v24.3.0（当前版本）](https://nodejs.org/en/blog/release/v24.3.0)

**原文标题**: [Node.js — Node v24.3.0 (Current)](https://nodejs.org/en/blog/release/v24.3.0)

Node.js v24.3.0（Current）版本发布，包含多项功能改进、错误修复和依赖项更新。

- 🚀 **重要变更**：添加了 Shima Ryuhei 为协作者，并移除了模块类型剥离的实验性警告。
- 🔄 **文件系统**：改进了 fs-events 的 AsyncIterator 处理，允许正确处理突发情况。
- 🛠 **测试运行器**：支持对象属性模拟，并修复了子测试自动等待的问题。
- 📦 **依赖更新**：升级了 nghttp2、acorn、npm 等多个依赖项的版本。
- 🐛 **错误修复**：修复了 HTTP/2 的 DEP0194 消息、REPL 标签补全等问题。
- 📜 **文档改进**：修复了多个文档链接和描述错误，并添加了新的协作者。
- 🔗 **URL 模块**：新增了 fileURLToPathBuffer API。
- 🔧 **工具链**：改进了工具链配置，包括 Python 兼容性和 ESLint 插件更新。
- 📥 **下载链接**：提供了 Windows、macOS、Linux 等多个平台的安装包和二进制文件下载链接。

---

### [Node.js — Node v20.19.3（长期支持版）](https://nodejs.org/en/blog/release/v20.19.3)

**原文标题**: [Node.js — Node v20.19.3 (LTS)](https://nodejs.org/en/blog/release/v20.19.3)

Node.js v20.19.3 (LTS) 版本发布，包含多项更新和修复。

- 🚀 **重要变更**：WebCryptoAPI 的 Ed25519 和 X25519 算法已升级为稳定版 (Filip Skokan)。
- 🔒 **安全更新**：根证书更新至 NSS 3.108 (Node.js GitHub Bot)。
- ⏰ **依赖更新**：时区数据更新至 2025b (Node.js GitHub Bot)。
- 📜 **文档改进**：新增协作者 Dario Piotrowicz，并修复多处文档问题。
- 🛠️ **构建与测试**：修复了多个构建和测试问题，包括 Windows 32 位架构支持 (RafaelGSS)。
- 🌐 **HTTP/2 修复**：修复了会话优雅关闭问题 (Kushagra Pandey)。
- 📦 **依赖升级**：更新了多个依赖，包括 V8、ICU、Corepack 和 SIMDUTF。
- 🐞 **Bug 修复**：修复了多个模块的问题，包括 crypto、http、os 和 worker。
- 💾 **下载链接**：提供了多个平台的安装包和二进制文件下载链接。
- 🔏 **安全签名**：包含所有发布文件的 SHASUMS 和 PGP 签名，确保下载安全。

---

### [Prettier 3.6：实验性快速 CLI 及全新 OXC 与 Hermes 插件！ · Prettier](https://prettier.io/blog/2025/06/23/3.6.0)

**原文标题**: [Prettier 3.6: Experimental fast CLI and new OXC and Hermes plugins! · Prettier](https://prettier.io/blog/2025/06/23/3.6.0)

Prettier 3.6 版本发布，引入了实验性高性能 CLI 和两个新插件，同时包含多项改进和修复。

- 🚀 新增实验性高性能 CLI，可通过 `--experimental-cli` 标志启用  
- 🔌 发布两个新官方插件：`@prettier/plugin-oxc`（基于 Rust 的快速 JS/TS 解析器）和 `@prettier/plugin-hermes`（基于 Hermes 引擎的 Flow 语法解析器）  
- 🛠️ JavaScript 多项语法一致性改进：序列表达式括号、类属性键赋值表达式括号、可选链数字括号等  
- ⚠️ 移除对已废弃的 Records & Tuples 提案支持  
- 📦 TypeScript 支持导入类型属性，修复逻辑表达式注释和映射类型换行检测  
- 🎨 CSS 新增 Tailwind V4 的 `@utility` 指令支持，修复 `:has` 伪类缩进  
- 📝 Markdown 修复块引用相邻语法和列表意外换行问题  
- 🔄 API 增强：支持 URL 作为插件和配置文件路径，新增 `isSupported` 函数支持  
- 🐛 多项错误修复：Flow 条件类型括号、Angular 控制流冒号、MJML 标签解析等  
- ⚡ CLI 改进：禁止配置冲突标志、缓存策略优化、错误退出码修正  

（注：由于原文过长，此为高度精简的核心内容摘要，实际更新细节请参考官方发布说明）

---

### [Bun v1.2.17 | Bun 博客](https://bun.sh/blog/bun-v1.2.17)

**原文标题**: [Bun v1.2.17 | Bun Blog](https://bun.sh/blog/bun-v1.2.17)

本次 Bun 版本更新修复了 50 个问题，新增 24 项 Node.js 测试通过，主要改进包括：

- 🚀 修复 50 个问题（处理 80 个👍），新增 24 项 Node.js 测试通过
- 📦 HTML 导入支持预编译打包，提升全栈应用开发效率
- 🐚 Bun Shell 可靠性提升，解决复杂脚本栈溢出问题
- 💾 setTimeout/setImmediate内存占用减少8-15%
- 🗃 bun:sqlite 新增 columnTypes 和 declaredTypes 支持
- 🔍 bun pm view 重命名为更直观的 bun info
- 🛠 Node.js 兼容性改进：child_process.fork 支持 execArgv
- 🌐 fs.glob 选项参数变为可选
- 🔒 实现 tls.getCACertificates()
- 🤖 bun init 自动生成 CLAUDE.md（检测到 claude 时）
- ⚡ JavaScriptCore 引擎升级带来多项性能优化
- 🛡 安全加固：修复 WebAssembly 解释器漏洞
- 🐛 修复包管理器、解析器、打包器和运行时多个问题
- 👏 感谢 15 位贡献者的付出

安装与升级：
- curl: `curl -fsSL https://bun.sh/install | bash`
- npm: `npm install -g bun`
- PowerShell: `powershell -c "irm bun.sh/install.ps1|iex"`
- scoop: `scoop install bun`
- brew: `brew tap oven-sh/bun && brew install bun`
- docker: `docker pull oven/bun`
- 升级：`bun upgrade`

---

### [SVGO](https://svgo.dev/)

**原文标题**: [SVGO](https://svgo.dev/)

SVGO 是一个多功能工具，支持命令行和 JavaScript API，拥有丰富的集成和开源社区支持。

- 🛠️ SVGO 提供命令行和 JavaScript API 两种使用方式，并附有详细的帮助文档  
- 🔌 已与多种工具集成，如 Docusaurus、PostCSS 和 webpack 等  
- 💡 开源项目，欢迎提交错误报告、功能请求或拉取请求

---

### [让 JavaScript 中的正则表达式更易用的小技巧](https://2ality.com/2025/06/javascript-regexp-tips.html)

**原文标题**: [Tips for making regular expressions easier to use in JavaScript](https://2ality.com/2025/06/javascript-regexp-tips.html)

概述：本文介绍了在 JavaScript 中使正则表达式更易用的多种技巧，包括使用/v 标志、命名捕获组、添加注释和空格以提高可读性，以及通过库或原生方法实现模式复用等。

- 🚀 使用/v 标志：减少正则表达式的怪异行为并增加功能，如支持多码位字符和字符类集合操作。
- 🔤 按字母顺序排列标志：使标志顺序一致，便于管理和阅读。
- 🏷️ 命名捕获组：通过命名捕获组提高可读性，减少外部文档需求。
- 📝 添加注释和空格：使用 Regex+ 库的 regex 模板标签，支持忽略空格和行内注释，大幅提升正则表达式的可读性。
- 🧪 编写测试：通过测试用例确保正则表达式按预期工作，验证其功能。
- 📖 文档示例：在文档中提供匹配示例，帮助理解正则表达式的用途。
- 🔄 模式复用：利用 Regex+ 库的插值功能，复用正则表达式片段，减少冗余。
- ✂️ 无库实现忽略空格：通过 String.raw 和.replaceAll() 方法，无需库即可实现忽略空格的正则表达式编写。
- 🎯 结论：通过合理使用空格、注释和现代特性，正则表达式可以变得易读且易于维护。

---

### [RSS 服务器端阅读器](https://matklad.github.io/2025/06/26/rssssr.html)

**原文标题**: [RSS Server Side Reader](https://matklad.github.io/2025/06/26/rssssr.html)

作者对 RSS 的理解及自建 RSS 阅读器的经验分享，特别介绍了其服务器端实现的个人化 RSS 阅读方案。

- 📰 RSS 的核心功能是通知机制，让读者能及时获知博客更新，而非依赖社交媒体或算法推荐。  
- ⚙️ 推荐使用 Atom 标准而非原始的 RSS，因其更清晰简单，但 JSON Feed 虽理想却缺乏维护。  
- 🖥️ 现有 RSS 阅读器功能冗余，作者仅需通知功能，偏好直接在原网站阅读。  
- ❌ 最初尝试客户端方案因 CORS 限制失败，无法跨域获取订阅源。  
- ✅ 成功方案：通过服务器端生成静态页面（SSR），集成到个人博客构建流程中，公开可访问。  
- 📝 使用纯文本文件`blogroll.txt`管理订阅源，简单易维护，替代复杂的 OPML 格式。  
- ⏰ 通过 GitHub Actions 每日自动重建订阅列表，确保内容更新。  
- 🔗 方案代码公开，利用现有库解析 Feed，展示最新 3 篇文章并排序。  
- 🌐 附带个人常用链接页，扩展内容分享形式。

---

### [OAuth 工作原理](https://clerk.com/blog/how-oauth-works?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-27-25&dub_id=JwXEM4p4DH9clhTY)

**原文标题**: [How OAuth Works](https://clerk.com/blog/how-oauth-works?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-27-25&dub_id=JwXEM4p4DH9clhTY)

OAuth 是一种复杂的开放授权标准，但通过核心概念解析和实际示例可以简化理解。本文重点介绍了 OAuth 的作用机制、授权代码流程及安全实践，帮助开发者实现安全的第三方应用集成。

- 🔐 OAuth 的核心目标是允许第三方应用在无需用户共享密码的情况下，安全访问用户数据。
- 🔄 授权代码流程是 OAuth 中最常见的流程，涉及用户同意、授权码交换令牌等步骤。
- 🛠️ 实际代码示例展示了如何实现 OAuth 流程，包括请求授权和处理回调。
- 🚫 安全措施包括使用 PKCE（Proof Key for Code Exchange）防止攻击，特别是在公开客户端（如移动应用和单页应用）中。
- 🔄 动态客户端注册允许通过 API 注册 OAuth 客户端，但需注意其安全风险。
- 🔗 OAuth 与 OIDC（OpenID Connect）结合使用，可提供用户身份信息，简化用户认证流程。
- 🏗️ 使用 Clerk 可以简化 OAuth 实现，内置授权服务器支持安全令牌管理和动态客户端注册。

---

### [mlacast](https://mlacast.com/projects/undo-redo)

**原文标题**: [mlacast](https://mlacast.com/projects/undo-redo)

在复杂的视觉应用中实现撤销/重做系统是一项具有挑战性但极具价值的任务，尤其在多上下文环境中需要确保操作的直观性和安全性。

- 🎨 **复杂性与挑战**：在 Alkemion Studio 这样的多上下文应用中，用户可能同时在多个界面（如画布、编辑器、节点表）操作，传统的单堆栈撤销/重做系统无法满足需求，可能导致不可见的意外修改或数据丢失。  
- 🧩 **上下文感知设计**：核心原则是“用户不能撤销他们看不到的操作”。通过配置文件和全局上下文管理，系统仅允许在当前可见的上下文中执行撤销/重做，避免混淆和破坏性错误。  
- � **动作类与封装**：每个可撤销操作封装为`Action`类（含`undo`/`redo`方法），并分为`ActionSingle`（单动作）和`ActionGroup`（关联动作组）。动作实例由中央单例`ActionStore`管理，存储于按类名分组的“动作卷”中。  
- 🗂 **容器化隔离**：借鉴 Docker 思想，通过“容器”隔离不同 UI 状态（如弹窗）的动作环境。每个容器拥有独立的动作堆栈，退出时可选择丢弃或合并动作到主容器，确保局部操作的原子性。  
- 🔢 **多堆栈排序与索引**：通过动态调整`globalIndex`解决跨上下文动作的时序问题。新动作插入时重排索引，确保撤销/重做的顺序符合用户预期，即使切换上下文也能保持操作连贯性。  
- ⚠ **依赖与未来改进**：当前系统依赖严格的动作顺序规范，未来计划引入依赖图（DAG）处理动作间的隐式关联，以应对更复杂的边缘场景。  
- 💻 **代码实现亮点**：包括动作实例化、上下文感知的堆栈生成、容器生命周期管理等方法，均以 TypeScript 示例展示，强调语言无关的架构普适性。  

这一系统通过分层设计（动作→容器→全局）和动态索引机制，平衡了灵活性与安全性，成为 Alkemion Studio 中“隐形却关键”的基础设施。

---

### [没时间学（网页）框架 X | 大脑烘焙](https://brainbaking.com/post/2025/06/no-time-to-learn-web-framework-x/)

**原文标题**: [No Time To Learn (Web) Framework X | Brain Baking](https://brainbaking.com/post/2025/06/no-time-to-learn-web-framework-x/)

overview summary  
Keith Cirkel 质疑是否值得花时间学习像 React 这样可能在未来几年内过时或发生巨大变化的 Web 框架，并建议开发者应专注于可迁移的基础技能。文章探讨了 Web 框架的演变、生命周期以及如何判断学习某项技术是否值得投入时间。

- 🤔 **质疑学习 React 的价值**：Keith Cirkel 认为 React 的 Hooks 等特性是独特的，缺乏可迁移性，质疑是否值得投入时间学习。  
- ⏳ **时间有限，选择重要**：开发者时间有限，应优先学习可迁移的基础技能，如纯 JavaScript、HTTP 协议或开源贡献。  
- 📊 **框架生命周期分析**：通过 Stack Overflow 标签流行度图表显示，大型框架（如 React、Angular）生命周期较长，而小型框架（如 Backbone、Knockout）易被淘汰。  
- 🔄 **框架的破坏性变更**：React 等框架每 2-3 年发布重大版本，可能导致开发者需要重新学习，增加学习成本。  
- 🛠️ **基础技能更持久**：与框架相比，编程语言（如 JavaScript、Java）的基础知识更稳定且长期有用。  
- 🚀 **早期采用者的风险**：依赖早期版本（如 0.x）的框架或技术可能面临频繁变更，增加学习负担。  
- 📉 **技术淘汰的普遍性**：作者列举了 AngularJS、Gulp 等已过时的技术，强调技术迭代的不可避免性。  
- 💡 **React 的优势**：尽管有争议，React 因其生态、社区和稳定性仍被视为默认选择。  
- 📚 **学术研究的局限性**：关于框架演变的研究可能因技术迭代过快而过时，难以提供实用指导。  
- 📧 **作者信息**：Wouter Groeneveld 分享个人观点并鼓励读者支持其创作，同时提供联系方式。

---

### [比较 Rust、JavaScript 和 Go 编写 WASM 组件的优劣](https://obeli.sk/blog/comparing-rust-javascript-and-go-for-authoring-wasm-components/)

**原文标题**: [



Comparing Rust, JavaScript and Go for authoring WASM Components
- Blog
](https://obeli.sk/blog/comparing-rust-javascript-and-go-for-authoring-wasm-components/)

概述：本文比较了 Rust、JavaScript 和 Go 在编写 WASM 组件方面的表现，通过具体示例展示了各语言在工具链、代码复杂度、文件大小等方面的差异，并给出了语言选择的建议。

- 🛠️ WASM 组件模型对 JavaScript 和 Go 的支持需要额外调整和工具链修复。
- 📦 JavaScript 工具链包括 ComponentizeJS、jco CLI 等，步骤较为复杂但社区活跃。
- 🐹 Go 的工具链相对简单，主要依赖 TinyGo 和 wit-bindgen-go，但代码更冗长。
- 🔍 通过 HTTP 客户端活动的示例，比较了 Rust、JavaScript 和 Go 的实现差异。
- 📊 WASM 文件大小比较：JavaScript 最大（12MB），Go 中等（1-2.6MB），Rust 最小（417KB-4.2MB）。
- 🔄 工作流示例展示了各语言在确定性执行和错误处理上的不同实现方式。
- 🌐 Webhook 端点示例显示 JavaScript 和 Go 在 HTTP 处理上的便利性差异。
- 🏆 结论：Rust 工具链最成熟，JavaScript 在社区和工具集成上占优，Go 在类型检查上有优势但代码不够简洁。
- 🚀 2025 年推荐选择 JavaScript 编写 WASM 组件，平衡了开发体验和社区支持。

---

### [如何撰写引人注目的软件发布公告 · 重构英语](https://refactoringenglish.com/chapters/release-announcements/)

**原文标题**: [How to Write Compelling Software Release Announcements · Refactoring English](https://refactoringenglish.com/chapters/release-announcements/)

这篇文章探讨了如何撰写引人注目的软件发布公告，强调从用户角度出发，突出改进而非技术细节，并提供实用建议。

- 📢 发布公告应聚焦用户体验的改进，而非简单罗列新功能。  
- 🚫 避免“变更日志”式公告，需说明功能如何直接惠及用户。  
- 📝 区分发布公告（精选重要改进）与发布说明（详尽变更记录）。  
- ⚡ 用“提速 100 倍”等积极表述替代“修复了卡顿问题”等消极描述。  
- 🌟 简短介绍产品功能，兼顾新老用户需求。  
- 🗑️ 删除“多项改进和错误修复”等模糊表述。  
- 🖼️ 截图需突出关键改动，搭配箭头/高亮等引导注意力。  
- 🎬 动画演示控制在 15 秒内，优先选用 WebP/AVIF 等高效格式。  
- 📅 开发阶段即规划公告内容，确保版本更新对用户有价值。  
- 📚 书摘来自《重构英语：开发者的高效写作指南》，支持预购获取章节更新。

---

### [用 AI 生成 Playwright 测试：试试新的 Playwright MCP 服务器！ - YouTube](https://www.youtube.com/watch?v=MIlcVo1x3Is)

**原文标题**: [Generating Playwright Tests With AI: Let's Try the New Playwright MCP Server! - YouTube](https://www.youtube.com/watch?v=MIlcVo1x3Is)

YouTube 平台相关信息概览  

- 📢 关于我们 - 介绍 YouTube 的基本信息和背景  
- 🗞️ 新闻动态 - 提供 YouTube 相关的新闻和公告  
- ©️ 版权信息 - 说明 YouTube 的版权政策和内容  
- 📩 联系我们 - 提供与 YouTube 联系的方式  
- 🎨 创作者 - 介绍 YouTube 创作者相关的内容和支持  
- 💼 广告合作 - 提供广告投放和商业合作的信息  
- 🛠️ 开发者 - 面向开发者的资源和支持  
- 📜 服务条款 - 列出 YouTube 的使用条款和条件  
- 🔒 隐私政策 - 说明 YouTube 如何处理用户数据和隐私  
- ⚖️ 政策与安全 - 介绍平台的安全政策和社区准则  
- 🔧 工作原理 - 解释 YouTube 的功能和运作方式  
- 🧪 测试新功能 - 介绍新功能的测试和更新  
- © 2025 Google LLC - 版权归属和年份声明

---

### [发布 v4.8.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.8.0)

**原文标题**: [Release v4.8.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.8.0)

Hono v4.8.0 版本发布，带来多项功能增强和新特性，包括路由助手、JWT 自定义头支持、JSX 流式非 ce 值支持等，同时代码体积进一步减小。

- 🚀 **代码体积减小** - `hono/tiny` 包减少约 800 字节，现仅约 11 KB（gzip 后 4.5 KB）。
- 🛠️ **路由助手** - 新增 `matchedRoutes`、`routePath` 等函数，简化路由信息获取。
- 🔐 **JWT 自定义头支持** - 支持从非标准头（如 `X-Auth-Token`）获取 JWT 令牌。
- 🛡️ **JSX 流式非 ce 值支持** - 为 CSP 兼容性，JSX 流式渲染支持添加 `scriptNonce`。
- 🌐 **CORS 动态方法控制** - 根据请求来源动态返回允许的 HTTP 方法。
- 🔓 **JWK 匿名访问支持** - 新增 `allow_anon` 选项，允许未认证请求继续处理。
- 💾 **缓存状态码选项** - 可指定缓存特定状态码（如 200 和 404）。
- 🔥 **Service Worker `fire()` 函数** - 替代 `app.fire()`，提供更简洁的调用方式。
- 🧩 **SSG 插件系统** - 支持自定义插件扩展静态站点生成过程（如生成站点地图）。
- 📦 **第三方中间件更新** - 新增 MCP 中间件、UA 拦截器中间件和 Zod Validator v4 支持。

---

### [Hono - 基于 Web 标准的 Web 框架](https://hono.dev/)

**原文标题**: [Hono - Web framework built on Web Standards](https://hono.dev/)

超快速且轻量化的路由器解决方案  

- 🚀 RegExpRouter 性能极快，提供高效路由处理  
- 📦 hono/tiny 预设体积小于 14kB，极致轻量化  
- 🌐 基于 Web Standard APIs，确保兼容性和标准化

---

### [宣布 LogTape 1.0.0 发布](https://hackers.pub/@hongminhee/2025/announcing-logtape-1-0)

**原文标题**: [Announcing LogTape 1.0.0](https://hackers.pub/@hongminhee/2025/announcing-logtape-1-0)

LogTape 1.0.0 是一个专为现代 JavaScript 生态系统设计的日志库，具有零依赖架构、跨运行时支持和库优先设计理念。此次发布标志着其核心 API 的稳定性和长期支持承诺。

- 🎉 **LogTape 简介**：专为 JavaScript 设计的日志库，支持 Node.js、Deno、Bun、浏览器和边缘函数，零依赖且对性能影响极小。
- 🚀 **里程碑成就**：1.0.0 版本发布，核心 API 稳定，适合生产环境使用，遵循语义化版本控制。
- ⚡ **高性能日志基础设施**：新增非阻塞选项和异步日志操作支持，优化文件操作性能。
- 🔗 **新接收器集成**：新增 AWS CloudWatch Logs 和 Windows Event Log 的集成支持。
- 🌈 **开发体验优化**：引入 `@logtape/pretty` 包，提供美观的本地开发日志输出。
- 🔌 **生态系统集成**：新增 `winston` 和 `pino` 适配器，便于现有应用无缝集成。
- 🛠️ **开发者体验增强**：改进浏览器兼容性，新增 `getLogLevels()` 函数和更好的类型推断。
- ⚠️ **重大变更与迁移指南**：移除 `LoggerConfig.level` 属性，推荐使用 `LoggerConfig.lowestLevel`。
- 📦 **完整包生态系统**：包含 11 个专用包，涵盖日志基础设施的各个方面。
- 🏁 **快速入门**：简单配置即可开始使用，现有应用可通过适配器轻松集成。

---

### [什么是 LogTape？ | LogTape](https://logtape.org/intro)

**原文标题**: [What is LogTape? | LogTape](https://logtape.org/intro)

LogTape 是一个适用于 JavaScript 和 TypeScript 的日志记录库，设计简洁灵活，易于使用和扩展。

- 📦 **零依赖**：LogTape 无任何依赖，使用时不需担心额外依赖问题。  
- 📚 **库支持**：适用于库和应用，可为库用户提供日志功能。  
- 🌐 **多运行时支持**：兼容 Deno、Node.js、Bun、边缘函数及浏览器，代码无需改动。  
- 🏷️ **结构化日志**：支持记录带结构化数据的日志消息。  
- 🌳 **层级分类系统**：通过层级分类管理日志记录器，可灵活控制不同层级的日志详细程度。  
- ✏️ **模板字面量**：支持使用模板字面量记录含占位符和值的日志消息。  
- 🔒 **内置数据脱敏**：提供基于模式或字段的敏感信息脱敏功能。  
- � **简单接收器**：轻松自定义日志输出目标（sinks）。

---

### [如果你正在构建一个 JavaScript 库并需要日志功能，你可能会爱上 LogTape](https://hackers.pub/@hongminhee/2025/logtape-for-libraries)

**原文标题**: [If you're building a JavaScript library and need logging, you'll probably love LogTape](https://hackers.pub/@hongminhee/2025/logtape-for-libraries)

JavaScript 库日志记录工具 LogTape 的设计理念与优势  
- 🛠️ **库优先设计**：LogTape 专为库作者设计，未配置时完全透明（无输出/副作用），用户可自主启用日志。  
- 🔄 **统一配置**：支持集中管理所有使用 LogTape 的库日志，提供一致的 API 和格式，解决生态碎片化问题。  
- 📦 **零依赖**：无第三方依赖，减少用户负担（仅 5.3KB 体积），兼容 ESM/CommonJS 及多运行时（Node.js、Deno、浏览器等）。  
- ⚡ **高性能**：未启用时接近零开销；启用后控制台输出性能优于同类方案。  
- 🏷️ **命名空间隔离**：层级分类系统（如`["my-lib", "database"]`）避免日志冲突，支持细粒度级别控制。  
- 🔌 **适配器支持**：提供 winston/Pino 等适配器，兼容现有日志系统，降低迁移成本。  
- 🛡️ **TypeScript 原生**：内置类型安全，支持模板字面量和结构化日志，提升开发体验。  
- 🌍 **多语言支持**：文档含韩文、中文、日文等多语言版本，便于国际化使用。  

核心价值：为库作者提供灵活、轻量的日志方案，平衡功能性与用户自主权，推动生态日志标准化。

---

### [谷歌宣布推出 Gemini CLI：你的开源 AI 助手](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)

**原文标题**: [Google announces Gemini CLI: your open-source AI agent](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)

Gemini CLI 是一款开源 AI 代理工具，旨在为开发者提供终端内的 Gemini 模型直接访问，提升工作效率和体验。

- 🚀 **开源与免费**：Gemini CLI 是 Apache 2.0 开源项目，开发者可自由使用、审查代码并参与贡献。  
- 💻 **终端集成**：直接在命令行中使用 Gemini 进行代码编写、调试、任务管理等，支持自然语言交互。  
- 🔍 **多功能支持**：包括代码理解、文件操作、动态故障排除，甚至内容生成（如视频脚本创作）。  
- ⚡ **高性能模型**：免费用户可访问 Gemini 2.5 Pro，享受百万 token 上下文窗口和超高请求限额（60 次/分钟，1000 次/天）。  
- 🔧 **扩展性强**：支持 Google 搜索集成、Model Context Protocol (MCP) 扩展，以及自定义提示和工作流自动化。  
- 🔗 **与 Gemini Code Assist 联动**：与 VS Code 的 Gemini Code Assist 共享技术，提供多步骤协作式 AI 编程支持。  
- 🌍 **社区驱动**：鼓励开发者通过 GitHub 提交问题、建议或代码改进，共同推动项目发展。  
- 📥 **快速入门**：仅需邮箱即可安装，免费计划拥有行业领先的使用额度。

---

### [GitHub - google-gemini/gemini-cli：一款开源AI代理，将Gemini的强大功能直接带入您的终端。](https://github.com/google-gemini/gemini-cli)

**原文标题**: [GitHub - google-gemini/gemini-cli: An open-source AI agent that brings the power of Gemini directly into your terminal.](https://github.com/google-gemini/gemini-cli)

Gemini CLI 是一个开源命令行工具，将 Gemini AI 集成到终端中，支持代码查询、自动化任务及多模态应用开发。

- 🚀 **功能概述**：Gemini CLI 支持代码库查询与编辑、多模态应用生成（如从 PDF 或草图创建应用）、自动化操作任务（如处理 PR 或复杂 rebase）。  
- 🔧 **快速开始**：需 Node.js 18+，通过 `npx` 或全局安装即可使用，提供 60 次/分钟、1000 次/天的免费请求额度。  
- 🔑 **认证方式**：支持个人 Google 账号登录或 API 密钥（需从 Google AI Studio 获取），企业用户可参考高级认证指南。  
- 📂 **使用示例**：包括创建新项目（如生成 Discord 机器人）或分析现有项目（如总结代码变更）。  
- 🔗 **扩展能力**：集成工具链（如 Imagen、Veo）和 Google 搜索工具，支持本地系统与企业协作工具对接。  
- 📚 **文档支持**：提供贡献指南、CLI 命令文档、故障排查及完整文档链接。  
- ⚠️ **注意事项**：需遵守服务条款和隐私政策，开源协议为 Apache-2.0。

---

### [一丝不苟](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=june27th2025)

**原文标题**: [Meticulous](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=june27th2025)

Meticulous AI 是一款无需编写和维护测试的自动化测试工具，通过记录用户交互并利用 AI 生成动态测试套件，覆盖所有边缘案例，提升开发效率和代码质量。

- 🚀 **无需编写测试** - Meticulous AI 自动生成并维护测试套件，无需手动编写或修复测试。  
- 🔍 **全面覆盖** - 通过记录用户交互，覆盖所有代码分支、用户流程和边缘案例。  
- ⚡ **快速集成** - 只需添加脚本标签，即可在本地、预发布和生产环境中记录会话。  
- 🛠️ **无干扰测试** - 默认模拟后端响应，避免因数据变化导致的误报，无需设置测试账户或模拟数据。  
- 📈 **持续进化** - 测试套件随应用功能更新自动调整，保持最新且完整。  
- 🚫 **无 flakes** - 基于 Chromium 的确定性调度引擎，消除测试不稳定性，执行速度极快。  
- 💡 **客户认可** - 被 Dropbox、WithPower、Lattice 等 100 多家组织信任，显著减少回归问题。  
- 🔗 **灵活使用** - 可单独使用或与现有测试套件结合，支持 NextJS、React、Vue、Angular 等框架。  
- ⏱️ **高效并行** - 测试在计算集群上高度并行化，数千次测试可在 120 秒内完成。  
- 📚 **简单上手** - 提供详细文档和快速入门指南，几分钟即可集成并开始生成测试。

---

### [获取失败](https://javascriptweekly.com/link/171079/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/171079/web)

无法总结：获取内容失败，状态码 415。

---

### [JSNation —— 美国主要的 JavaScript 大会](https://jsnation.us/?utm_source=Newsletter&utm_medium=JSWeekly%20)

**原文标题**: [JSNation – The main JS conference in the US](https://jsnation.us/?utm_source=Newsletter&utm_medium=JSWeekly%20)

美国 JSNation 大会 2025 年 11 月 17 日（纽约线下 + 线上）和 20 日（纯线上）举行，汇聚 50+ 顶尖专家、700+ 开发者及全球万名程序员，共同探索 JavaScript 未来趋势。活动包含深度研讨会、AI 编程专题、星球剧院演讲及全美最大 JS 派对，提供混合参与模式与独家 Multipass 福利。

- 🌟 **活动概况**：2025 年 11 月 17 日（纽约线下 + 线上）和 20 日（纯线上），覆盖全球 10 万+JS 开发者  
- 🎤 **核心嘉宾**：Google Chrome、Vue.js、Node.js、Svelte 等核心团队及行业领袖  
- 🚀 **亮点内容**：  
  - AI 辅助编程、工程师成长路径等深度研讨  
  - 西半球最大天文馆技术演讲（React 专题）  
  - 曼哈顿景观渡轮社交派对  
- 💻 **参与方式**：  
  - 线下票（含实体福利包）$640 起  
  - 远程票（高清直播 + 数字礼包）$190 起  
  - Multipass 通票（10 场会议 + 独家课程）$19/月  
- 🎉 **特色活动**：  
  - 11 月 18 日线下狂欢夜（19:00-23:00 ET）  
  - 免费/付费工作坊（React 架构、MCP 协议等）  
- 📅 **日程亮点**：  
  - 11 月 17 日：主会议日（混合模式）  
  - 11 月 20 日：远程专题日（双轨道直播+Q&A）  
- ✨ **额外福利**：分享邀请码可赢免费门票，企业赞助机会开放

---

### [GitHub - plv8/pljs: PLJS - PostgreSQL 的 JavaScript 语言插件](https://github.com/plv8/pljs)

**原文标题**: [GitHub - plv8/pljs: PLJS - Javascript Language Plugin for PostreSQL](https://github.com/plv8/pljs)

PLJS 是一个为 PostgreSQL 设计的轻量级、快速的 JavaScript 语言扩展插件，支持通过 JavaScript 编写 PostgreSQL 函数。

- 🚀 **项目状态**：当前版本为 1.0.0，支持 PostgreSQL 14+  
- 🔧 **技术栈**：基于 QuickJS 实现 JavaScript 运行时  
- 📚 **文档**：包含类型转换、函数配置、开发指南等详细内容  
- 💡 **使用示例**：安装后执行 `CREATE EXTENSION pljs` 并调用 JS 函数  
- 📊 **社区数据**：163 Stars，4 Forks，提供 Discord 支持频道  
- 📜 **许可证**：开源（LICENSE 文件可查看详情）  
- 🛠 **开发相关**：提供构建指南、版本策略和性能基准（对比 PLV8）  
- ⚠ **已知问题**：页面加载错误时需手动刷新

---

### [GitHub - plv8/plv8: PostgreSQL 的 V8 引擎 JavaScript 过程语言插件](https://github.com/plv8/plv8)

**原文标题**: [GitHub - plv8/plv8: V8 Engine Javascript Procedural Language add-on for PostgreSQL](https://github.com/plv8/plv8)

PLV8 是一个基于 V8 JavaScript 引擎的 PostgreSQL 过程语言扩展，允许用户在 SQL 中调用 JavaScript 编写的函数。

- 🚀 **项目简介**: PLV8 是一个共享库，为 PostgreSQL 提供了基于 V8 JavaScript 引擎的过程语言支持。  
- 🔧 **构建要求**: 在 Linux 和 MacOS 上需要安装特定的开发工具和依赖项，如 `cmake`、`git` 和 `libstdc++-dev`。  
- 🛠️ **安装步骤**: 通过 `make` 和 `make install` 命令可以构建并安装 PLV8 扩展。  
- 🧪 **测试方法**: 使用 `make installcheck` 运行测试，或在 PostgreSQL 中执行简单的 JavaScript 代码片段进行验证。  
- 📚 **文档支持**: 完整文档可在 [plv8.github.io](https://plv8.github.io/) 查看。  
- 🐳 **Docker 支持**: 提供 Docker 支持，具体信息参见 `./platforms/Docker/README.md`。  
- 🌟 **项目状态**: 项目拥有 2k stars 和 145 forks，由 41 位贡献者维护。  
- 📊 **技术栈**: 主要使用 C++ (77.3%) 和 PLpgSQL (15.9%) 开发。

---

### [QuickJS JavaScript 引擎](https://bellard.org/quickjs/quickjs.html)

**原文标题**: [QuickJS Javascript Engine](https://bellard.org/quickjs/quickjs.html)

QuickJS 是一个轻量且可嵌入的 JavaScript 引擎，支持 ES2023 规范，具有快速解释器和低启动时间，适用于多种应用场景。

- 🚀 **轻量且可嵌入**：仅需少量 C 文件，无外部依赖，代码体积小（210 KiB）。
- ⚡ **快速解释器**：低启动时间，可在单核桌面 PC 上 2 分钟内完成 77000 个 ECMAScript 测试。
- 📜 **ES2023 支持**：支持模块、异步生成器、代理和 BigInt 等特性，兼容 Annex B。
- ✅ **高测试通过率**：在 ES2023 特性测试中通过率接近 100%。
- 🔄 **引用计数垃圾回收**：减少内存使用，行为确定，支持循环移除。
- 💻 **命令行工具**：提供交互式解释器（`qjs`）和编译器（`qjsc`），支持脚本和模块。
- 📦 **内置标准库**：包含 `std` 和 `os` 模块，提供基础功能。
- 🛠 **C API**：简单高效的 C API，支持运行时、上下文、异常处理和自定义模块。
- 📊 **内部优化**：字节码直接生成、字符串和对象优化、快速函数调用等。
- 📜 **MIT 许可证**：开源且允许自由使用。

---

### [标记文档](https://marked.js.org/)

**原文标题**: [Marked Documentation](https://marked.js.org/)

Marked 是一个高性能的 Markdown 解析器，支持多种 Markdown 规范，提供 CLI 和 JavaScript 使用方式，强调安全性和扩展性。

- 🚀 **高性能**：Marked 为速度而设计，解析 Markdown 时不缓存或长时间阻塞。
- 📚 **多功能支持**：支持 Markdown 1.0、CommonMark 0.31 和 GitHub Flavored Markdown 0.29 等多种规范。
- 🛠️ **多种使用方式**：提供 CLI、浏览器和 Node.js 等多种使用方式。
- ⚠️ **安全警告**：Marked 不自动过滤输出的 HTML，需使用 DOMPurify 等工具防止 XSS 攻击。
- 📖 **CLI 使用**：支持通过命令行快速转换 Markdown 文件为 HTML。
- 🏗️ **扩展性**：支持通过 marked.use() 等方法进行自定义扩展。
- 🔍 **测试覆盖**：严格测试确保规范兼容性，部分功能如链接和自动链接支持度较高但非 100%。
- 🛡️ **安全性**：项目重视安全性，发现漏洞可通过邮件报告，承诺 48 小时内初步评估，两周内修复。
- 🌍 **社区工具**：多个工具如 zero-md 和 Homebrewery 使用 Marked 进行快速 Markdown 转换。

---

### [标记演示](https://marked.js.org/demo/)

**原文标题**: [Marked Demo](https://marked.js.org/demo/)

该内容介绍了 Markdown 的演示工具及其相关功能选项。

- 🔄 提供多种 Markdown 演示模式（CommonMark、Daring Fireball 等）  
- ⚙️ 包含输入、永久链接、版本切换等操作选项  
- 📝 支持 Markdown 预览与 HTML 源码切换查看  
- 🚀 提供快速参考指南和响应时间显示  
- ⚠️ 需启用 JavaScript 才能使用该工具

---

### [GitHub - markedjs/marked: 一个 Markdown 解析器和编译器。为速度而生。](https://github.com/markedjs/marked)

**原文标题**: [GitHub - markedjs/marked: A markdown parser and compiler. Built for speed.](https://github.com/markedjs/marked)

marked 是一个高效的 Markdown 解析器和编译器，专为速度而设计，支持多种 Markdown 语法规范，适用于浏览器、服务器和命令行环境。

- ⚡ **高效性能**：低层编译器，解析 Markdown 时不缓存或长时间阻塞  
- ⚖️ **轻量全面**：体积小但支持所有主流 Markdown 特性和规范  
- 🌐 **多端兼容**：可在浏览器、服务器或 CLI 中运行  
- 🚨 **安全提示**：输出 HTML 需额外消毒（推荐使用 DOMPurify 等库）  
- 📥 **安装灵活**：支持全局 CLI (`npm install -g marked`) 或浏览器端 (`npm install marked`)  
- 📚 **丰富文档**：提供演示页面和详细配置选项说明  
- 🔒 **版本要求**：仅支持 Node.js 当前和 LTS 版本，不兼容 IE11 浏览器  
- 📜 **开源许可**：基于 MIT 许可证，由 Christopher Jeffrey 等 190+ 贡献者维护  
- 🌟 **生态数据**：35k+ Stars | 3.5k+ Forks | 被 150 万 + 项目使用

---

### [未找到标题](https://tewolde.co/vueInfinity/)

**原文标题**: [No title found](https://tewolde.co/vueInfinity/)

Vue-Infinity 是一个模块化工具包，旨在帮助开发者使用 Vue 构建高性能、内存高效且媒体丰富的应用程序。通过智能数据获取和虚拟化渲染，确保即使处理大型数据集也能提供流畅的用户体验。

- 🚀 **关键特性**：Vue-Infinity 提供多种功能模块，包括 InfiniteList、InfiniteCarousel、AutoObserver 和 Ghost Component，优化性能和用户体验。
- 🔄 **InfiniteList**：支持分页数据访问、缓存管理、自动预加载和取消网络请求，适用于快速滚动场景。
- 🪂 **InfiniteCarousel**：集成 InfiniteList，支持自定义行列、滚动方向、模板和动态项目大小。
- 🔎 **AutoObserver**：自动观察新增元素，停止观察已移除元素，并在组件卸载时自动清理。
- 👻 **Ghost Component**：通过条件渲染优化性能，卸载不可见内容以节省内存，并提供可见性变化钩子。
- 📹 **示例演示**：包含视频和图片的动态加载与卸载，展示工具包的实际应用效果。

---

### [GitHub - isaact/vue-infinity: Vue Infinity 是一个模块化工具包，旨在帮助开发者使用 Vue 构建高性能、内存高效且富含媒体的应用程序。通过智能数据获取和虚拟化渲染技术，即使在处理大型数据集时也能确保流畅的用户体验。](https://github.com/isaact/vue-infinity)

**原文标题**: [GitHub - isaact/vue-infinity: Vue Infinity is a modular toolkit designed to help developers build high-performance, memory-efficient, and media-rich applications with Vue. By leveraging smart data fetching and virtualized rendering, it ensures smooth user experiences even with large datasets.](https://github.com/isaact/vue-infinity)

Vue Infinity 是一个模块化工具包，旨在帮助开发者使用 Vue 构建高性能、内存高效且媒体丰富的应用程序。通过智能数据获取和虚拟化渲染，确保即使处理大型数据集也能提供流畅的用户体验。

- 🚀 **关键特性**：Vue Infinity 通过仅渲染可见内容，显著提升 UI 效率，适用于无限滚动、轮播、媒体库等场景。
- 👻 **幽灵组件**：优化性能，用占位符替换非可见内容，保持布局稳定，并触发可见性相关事件。
- 🪂 **无限轮播组件**：支持网格或轮播布局，可自定义行列数、滚动方向及动态项目大小。
- 🔄 **无限列表**：提供分页数据访问、缓存管理及项目索引访问，支持请求取消。
- 🔎 **自动观察器**：增强 IntersectionObserver，自动处理新增和移除的元素。
- 📦 **安装**：通过 npm 安装，提供本地运行演示应用的指南。
- 📄 **许可证**：采用 Apache 2.0 许可证，支持开源使用。
- 🌐 **资源**：包含实时演示链接和详细文档，便于开发者快速上手。

---

### [首页 - Spark](https://sparkjs.dev/)

**原文标题**: [Home - Spark](https://sparkjs.dev/)

Spark 是一个专为 THREE.js 设计的高级 3D 高斯泼溅渲染器，支持与其他网格和泼溅效果集成，提供快速渲染和动态可编程效果，兼容多种格式。

- 🏠 **主页** - 提供 Spark 渲染器的基本信息和使用入口。  
- � **入门指南** - 帮助用户快速开始使用 Spark 渲染器。  
- 👀 **概述** - 简要介绍 Spark 的核心功能和优势。  
- 🖥️ **系统设计** - 解释 Spark 的架构和技术实现。  
- 🎨 **SparkRenderer** - 核心渲染器组件，负责处理 3D 高斯泼溅渲染。  
- 👁️ **SparkViewpoint** - 视角管理工具，优化渲染视角设置。  
- 🔳 **SplatMesh** - 泼溅网格处理模块，支持高效渲染。  
- 📦 **PackedSplats** - 提供紧凑的泼溅数据存储和渲染优化。  
- 📂 **加载 Gsplats** - 支持加载高斯泼溅数据文件。  
- 🌀 **程序化泼溅** - 动态生成和控制泼溅效果。  
- ✏️ **泼溅 RGBA-XYZ SDF 编辑** - 编辑泼溅的颜色、位置和形状。  
- 🌪️ **Dyno 概述** - 动态效果系统的简介。  
- 📚 **Dyno 标准库** - 提供预定义的动态效果和工具。  
- � **控制** - 用户交互和控制选项。  
- ⚡ **性能调优** - 优化渲染性能的技巧和建议。  
- 👥 **社区资源** - 提供额外的学习材料和社区支持链接。

---

### [火花 • 示例](https://sparkjs.dev/examples/)

**原文标题**: [Spark • Examples](https://sparkjs.dev/examples/)

好的，请提供您需要总结的文本内容，我会按照您要求的模板进行整理，包括概述总结和带表情符号的要点列表。  

示例格式：  

概述总结  
- 📌 要点一  
- 📌 要点二  
- 📌 要点三  

请提供具体文本，我会为您生成相应的总结。

---

### [billboard.js 3.16.0 版本发布：✨ 新增柱状趋势线 & 优化调整大小性能！ | 作者 Jae Sung Park | 2025 年 6 月 | Medium](https://netil.medium.com/billboard-js-3-16-0-release-bar-trending-line-improved-resizing-performance-168e36a8b099)

**原文标题**: [billboard.js 3.16.0 release: ✨ bar trending line & improved resizing performance! | by Jae Sung Park | Jun, 2025 | Medium](https://netil.medium.com/billboard-js-3-16-0-release-bar-trending-line-improved-resizing-performance-168e36a8b099)

billboard.js 3.16.0 版本发布，新增条形趋势线功能并优化了调整大小的性能表现。

- 🆕 **新增条形趋势线功能**  
  支持四种不同类型的连接方式，可自定义样式，通过 CSS 选择器 `.bb-bar-connectLine` 实现。

- 🔄 **反向轴刻度裁剪选项**  
  新增 `axis.tick.culling.reverse` 选项，控制刻度文本的显示顺序，从末尾开始显示。

- 📏 **指定绝对轴文本尺寸**  
  新增 `axis.evalTextSize` 功能，可手动设置轴文本的尺寸，解决样式和渲染问题。

- ⚡ **性能提升**  
  优化了调整大小时的性能，平均减少了 54.87% 的处理时间。

- 🚀 **未来展望**  
  持续改进响应式行为和视觉清晰度，打造更灵活、开发者友好的图表核心。欢迎通过 GitHub 和社区渠道反馈！

---

### [GitHub - andrewmd5/hako：一款可嵌入、轻量级、安全且高性能的JavaScript引擎](https://github.com/andrewmd5/hako)

**原文标题**: [GitHub - andrewmd5/hako: An embeddable, lightweight, secure, high-performance JavaScript engine.](https://github.com/andrewmd5/hako)

Hako 是一个可嵌入、轻量级、安全且高性能的 JavaScript 引擎，基于 PrimJS 分支开发，支持 ES2019 及更高版本的 ESNext 特性。

- 🚀 **高性能**：Hako 在性能上优于 QuickJS 和 QuickJS-NG，例如在字符串拼接基准测试中表现更优。
- 🔒 **安全性**：通过编译为 WebAssembly 实现内存安全，内置沙盒机制（VMContext）限制代码能力，并提供 API 限制内存和资源消耗。
- 📦 **可嵌入性**：无需 Emscripten，支持任何有 WebAssembly 运行时的语言嵌入，体积小巧（约 800KB）。
- 🌐 **多语言支持**：提供 TypeScript 参考实现，并计划逐步完善文档和 API 稳定性。
- ⚠️ **早期阶段**：项目处于早期访问阶段，API/ABI 可能不稳定，欢迎通过 Issue 或 PR 贡献反馈。

---

### [发布 5.9.0 版本 · marmelab/react-admin · GitHub](https://github.com/marmelab/react-admin/releases/tag/v5.9.0)

**原文标题**: [Release 5.9.0 · marmelab/react-admin · GitHub](https://github.com/marmelab/react-admin/releases/tag/v5.9.0)

react-admin 项目发布了 v5.9.0 版本，包含多项功能更新、问题修复和文档改进。

- 🚀 新增对 MUI 主题的自定义支持，涵盖输入框、主视图组件、按钮、字段和删除按钮 (#10772, #10771, #10770)  
- 🆕 引入 `<RecordField>` 组件 (#10749)  
- 🔄 为 `useUpdateMany` 添加中间件支持 (#10795)  
- 🌍 允许资源特定的页面和按钮翻译 (#10686)  
- 🐛 修复 `<AutocompleteInput>` 覆盖输入插槽属性时的问题 (#10793)  
- 🎨 修复批量操作按钮的悬停样式 (#10788)  
- 📷 修复就绪页面中图片对齐问题 (#10780)  
- 🔒 修复 `useLogoutAccessDenied` 未提供 `redirectTo` 时的错误 (#10763)  
- 📚 文档更新：添加 Appwrite 到 AuthProvider 列表 (#10798)、更新 DataProvider 列表中的 Appwrite 信息 (#10787)、新增迁移指南 (#10786) 等  
- 🧹 清理演示代码中的重复文件 (#10792)  
- 🧪 测试环境优化，确保在英语环境下运行 (#10781)

---

### [AG Charts 12 的新变化](https://blog.ag-grid.com/whats-new-in-ag-charts-12/)

**原文标题**: [What's New in AG Charts 12](https://blog.ag-grid.com/whats-new-in-ag-charts-12/)

AG Charts 12 是 2025 年的首个主要版本，引入了多项新功能和开发者体验优化，旨在提升图表可读性和开发效率。

- 🌟 **轴带高亮** - 悬停时高亮整个类别或日期轴带，增强数据关联性。  
- 📏 **轴标签自动换行** - 自动处理长标签避免重叠，默认支持含空格的类别轴标签。  
- � **全局格式化器** - 集中配置图表格式化逻辑，减少重复代码。  
- 🛠 **TypeScript 泛型支持** - 为数据和上下文对象提供自动补全和编译时验证。  
- 🎨 **增强的高亮选项** - 自定义悬停/非悬停项及系列的样式，提升视觉区分度。  
- 📌 **上下文对象** - 为所有回调和事件处理器附加自定义信息，支持图表级、系列级和轴级上下文传递。  

💡 版本亮点包括更清晰的视觉效果、开发者控制强化及 TypeScript 支持优化。详见[发布说明](链接)或[更新日志](链接)。  

👉 新用户可[免费快速入门](链接)，企业用户可申请[两周试用许可](链接)。  

作者：David Glickman（AG Charts 技术产品分析师）与 James Swinton-Bland（AG Grid 开发者关系负责人）。

---

### [发布 v3.0.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.0.0)

Recharts 3.0 版本发布，包含重大更新、新功能及改进，旨在提升社区贡献体验。

- 🚀 Recharts 3 正式发布，由 PavelVanecek 主导开发，重写了状态管理并新增 3500 个单元测试。  
- ⚠️ 包含重大变更：移除 `CategoricalChartState` 和 `<Customized />` 的内部状态传递，清理内部属性。  
- 🆕 新功能：支持自定义 SVG 组件、Tooltip 和 Legend 的 Portal 渲染、默认无障碍支持及极坐标图多轴功能。  
- 🔧 改进与修复：动画优化、TypeScript 增强、无障碍改进及长期存在的 Bug 修复。  
- 📚 提供 3.0 迁移指南和更新版 Storybook 示例。  
- 👏 社区反响热烈，获得大量点赞和庆祝表情回应。

---

### [Gemma 3n 开发者指南发布 - Google Developers 博客](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/)

**原文标题**: [
            
            Introducing Gemma 3n: The developer guide
            
            
            - Google Developers Blog
            
        ](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/)

Google 发布了 Gemma 3n 模型，这是一款专为移动设备设计的先进多模态 AI 模型，具有高效性和强大的性能。

- 🚀 **Gemma 3n 发布**：Gemma 3n 是一款专为开发者设计的移动优先 AI 模型，支持多模态输入（图像、音频、视频、文本）和文本输出。  
- 📱 **高效移动架构**：提供两种尺寸（E2B 和 E4B），内存占用低至 2GB 和 3GB，性能媲美去年的云端前沿模型。  
- 🧩 **MatFormer 架构**：采用嵌套 Transformer 设计，支持弹性推理，开发者可自定义模型大小以适应硬件限制。  
- 💾 **内存优化**：通过 Per-Layer Embeddings (PLE) 技术，显著减少加速器内存占用，提升设备端运行效率。  
- 🔊 **音频处理**：集成 Universal Speech Model (USM) 编码器，支持语音识别和翻译，尤其擅长英语与西班牙语等语言的互译。  
- 👁️ **视觉编码器**：搭载 MobileNet-V5，支持多种分辨率输入，在边缘设备上实现实时视频分析和图像理解。  
- 🌍 **多语言支持**：支持 140 种语言的文本理解和 35 种语言的多模态理解。  
- 🛠️ **开发者工具**：兼容 Hugging Face、llama.cpp、Ollama 等流行工具，并提供详细的文档和部署指南。  
- 🏆 **Gemma 3n Impact Challenge**：发起挑战赛，鼓励开发者利用 Gemma 3n 构建具有现实影响力的应用，奖金总额 15 万美元。  
- 🔧 **快速开始**：开发者可通过 Google AI Studio 体验模型，或从 Hugging Face 和 Kaggle 下载权重，支持多种部署方式。

---

### [gemma3n](https://ollama.com/library/gemma3n)

**原文标题**: [gemma3n](https://ollama.com/library/gemma3n)

Gemma 3n 模型专为高效运行于日常设备（如笔记本、平板或手机）设计，支持 140 多种语言，采用选择性参数激活技术降低资源需求，提供 2B 和 4B 两种参数规模版本，并在多领域基准测试中表现优异，同时注重伦理与安全性评估。

- 💻 **设备兼容性**：专为笔记本、平板、手机等日常设备优化设计  
- 🌍 **多语言支持**：训练数据涵盖 140 多种语言  
- ⚙️ **高效技术**：选择性参数激活技术降低资源占用，实际运行参数为 2B/4B  
- 📊 **性能表现**：在推理、多语言、STEM 等多项基准测试中优于前代模型  
- 🔍 **伦理安全**：通过儿童安全、内容安全、表征公平性等严格评估  
- 🛠️ **应用场景**：支持文本生成、对话 AI、研究教育等多领域应用  
- ⚠️ **使用限制**：当前评估主要基于英语提示，存在一定局限性  

（注：由于原始文本包含大量表格数据，摘要已提炼核心信息，具体基准分数未逐一罗列）

---

### [奥林匹斯之战 ※ 破解 VG 密码 S3e1 - YouTube](https://www.youtube.com/watch?v=2xzWmTfapuM)

**原文标题**: [The Battle of Olympus ※ Cracking VG Passwords S3e1 - YouTube](https://www.youtube.com/watch?v=2xzWmTfapuM)

关于 YouTube 的相关信息与链接  
- 📢 关于 - 了解 YouTube 的更多背景信息  
- 🗞️ 媒体 - 查看 YouTube 的新闻与公告  
- ©️ 版权 - 版权相关政策和信息  
- 📩 联系我们 - 提供联系方式以便沟通  
- 🎨 创作者 - 为内容创作者提供的资源和支持  
- 💼 广告 - 广告合作与推广信息  
- 👩💻 开发者 - 开发者工具和资源  
- 📜 条款 - 使用条款和条件  
- 🔒 隐私 - 隐私政策和数据保护  
- ⚖️ 政策与安全 - 平台政策与安全措施  
- 🔧 YouTube 工作原理 - 平台运作机制解析  
- � 测试新功能 - 尝试 YouTube 的最新功能  
- © 2025 Google LLC - 版权归属声明

---

### [Omarchy：DHH 打造的固执己见的 Arch/Hyprland 配置](https://omarchy.org/)

**原文标题**: [Omarchy: Opinionated Arch/Hyprland Setup By DHH](https://omarchy.org/)

该内容似乎是一段混合了 ASCII 艺术、软件安装命令和公司信息的文本。

- 🖥️ 包含一个 ASCII 艺术图形，可能代表某种徽标或装饰性元素  
- ⚙️ 提供了一个命令行安装指令 `wget -qO- https://omarchy.org/install | bash`  
- 📚 提到"手动"和"代码"两个选项（The Manual | The Code）  
- 🏢 由 37signals 公司提供，该公司开发了 Basecamp、HEY 和 ONCE 等产品

---

### [约翰·卡马克（Keen Technologies）：2025 年上限研究方向的探讨 - YouTube](https://www.youtube.com/watch?v=3pdlTMdo7pY)

**原文标题**: [John Carmack (Keen Technologies): Research Directions @ Upper Bound 2025 - YouTube](https://www.youtube.com/watch?v=3pdlTMdo7pY)

关于 YouTube 平台的相关信息与资源  
- 📢 关于：平台的基本介绍与背景  
- 🗞️ 媒体：新闻与公告  
- ©️ 版权：版权政策与保护  
- 📩 联系我们：用户沟通渠道  
- 🎨 创作者：内容创作者相关资源  
- 💼 广告：广告合作与推广  
- 👩💻 开发者：开发者工具与 API  
- 📜 条款：服务使用条款  
- 🔒 隐私：隐私政策与数据保护  
- ⚖️ 政策与安全：社区准则与安全措施  
- 🔧 YouTube 运作机制：平台功能解析  
- 🧪 测试新功能：体验最新推出的特性  
- ®️ 版权归属：2025 年 Google LLC 所有

---

### [禁用当前 zsh shell 会话的历史记录 · Jamie Tanna | 软件工程师](https://www.jvt.me/posts/2025/06/26/zsh-no-history/)

**原文标题**: [Disabling zsh history for a given shell session · Jamie Tanna | Software Engineer](https://www.jvt.me/posts/2025/06/26/zsh-no-history/)

文章概述了如何在 zsh 会话中临时禁用历史记录功能，以避免敏感信息被保存到历史文件中。

- 🔍 作者在处理敏感信息时，需要临时禁用 zsh 历史记录功能。  
- 🛠️ 通过运行`unset HISTFILE`、`export HISTSIZE=0`和`export SAVEHIST=0`命令，可以临时禁用历史记录。  
- 📜 这些命令确保当前 zsh 会话不会保存任何历史记录，直到启动新的 shell 会话。  
- ⚠️ 注意：禁用历史记录后，只有禁用命令本身会被记录，其他命令不会被保存。  
- 📅 文章发布于 2025 年 6 月 26 日，遵循 CC-BY-NC-SA-4.0 和 Apache-2.0 许可协议。  
- 💡 作者还提到内容部分来源于 LLM（如 GPT-4.1），并鼓励读者支持其创作。

---

