### [JavaScript 周刊第 746 期：2025 年 7 月 25 日](https://javascriptweekly.com/issues/746)

**原文标题**: [JavaScript Weekly Issue 746: July 25, 2025](https://javascriptweekly.com/issues/746)

概述总结：本期内容涵盖了 JavaScript 工具库更新、React 和 Next.js 开发技巧、WebAssembly 进展、npm 安全事件、新版本发布、前端开发文章与工具推荐，以及一些有趣的开发者资源和调查。

- 🚀 **es-toolkit 发布**：一个现代 JavaScript 工具库，比 Lodash 更快且体积更小，现已 100% 兼容 Lodash。  
- ⚠️ **React 和 Next.js 常见错误避免**：避免冗余的 useState 和 useEffect，学习如何重构复杂应用。  
- 🔧 **WebAssembly 的 DOM 支持进展**：现代构建工具和 WASM 的演进正在简化 DOM 操作。  
- 🛡️ **npm 安全事件**：多个流行包被劫持传播恶意软件，npm 下架了存在安全问题的 stylus 包。  
- 🌍 **EsJS 实验**：一个用西班牙语编写 JavaScript 的在线实验项目。  
- 📦 **Bun 1.2.19 发布**：支持 pnpm 风格的 node_modules 隔离，新增交互式依赖更新功能。  
- 🎨 **前端开发文章**：包括代码高尔夫比赛回顾、15 年前 JavaScript 代码的反思、现代 CSS 替代 SPA 的讨论等。  
- 🛠️ **工具推荐**：Transformers.js 3.7 支持浏览器端运行预训练模型，npq 工具可安全安装 npm 包。  
- 📊 **图表库更新**：ApexCharts 5.3 新增数据解析能力，支持直接映射原始数据到图表。  
- 🎉 **开发者资源**：MDN 庆祝 20 周年，Google 推出 OSS Rebuild 以增强开源生态安全性。

---

### [ES 工具包](https://es-toolkit.dev/)

**原文标题**: [es-toolkit](https://es-toolkit.dev/)

最佳性能  
es-toolkit 在现代 JavaScript 运行时中的性能表现比其他库高出 2-3 倍。  

- 🚀 **性能优势** - es-toolkit 在现代 JavaScript 运行时中的性能优于其他库 2-3 倍。  
- ⚡ **高效运行** - 专为现代 JavaScript 环境优化，提供更快的执行速度。  
- 📊 **显著提升** - 性能提升显著，适合高性能要求的应用场景。

---

### [Lodash](https://lodash.com/)

**原文标题**: [Lodash](https://lodash.com/)

Lodash 是一个现代化的 JavaScript 实用工具库，提供模块化、高性能和额外功能。

- 📚 **功能概述**：简化 JavaScript 操作，支持数组、数字、对象、字符串等数据处理  
- 🛠 **核心特性**：模块化方法，适用于迭代、值操作/测试、创建复合函数等场景  
- 📦 **多种构建版本**：  
  - 核心版（~4kB）  
  - 完整版（~24kB）  
  - 支持按需加载（FP 构建、方法分类或单独方法）  
- 🌐 **安装方式**：  
  - 浏览器直接引入`<script>`标签  
  - npm 全局或局部安装  
  - Node.js 中按需加载不同构建包  
- 🔄 **模块格式**：支持 UMD、ES 模块、AMD 及 FP（函数式编程）风格  
- 📜 **许可证**：MIT 开源协议，兼容现代环境（浏览器及 Node.js 8-12）  
- 🛠️ **配套工具**：推荐搭配`futil-js`等函数式工具库使用  
- ❓ **为什么选择 Lodash**：解决 JavaScript 复杂操作痛点，提升开发效率  
- 📖 **扩展资源**：贡献指南、版本日志、Wiki（路线图等）  
- ✔️ **兼容性**：全面测试主流浏览器及 Node.js 环境

---

### [在 | ES 工具包](https://es-toolkit.dev/reference/array/at.html)

**原文标题**: [at | es-toolkit](https://es-toolkit.dev/reference/array/at.html)

概述：该函数用于从数组中检索指定索引位置的元素，支持负数索引，返回一个新数组包含这些元素。

- 🔍 从数组中检索指定索引的元素  
- 🔄 支持负数索引（从数组末尾开始计数）  
- 📜 函数签名：`function at<T>(arr: T[], indices: number[]): T[]`  
- 📌 参数：  
  - `arr` (T[]): 要检索的源数组  
  - `indices` (number[]): 包含目标索引的数组  
- 🎯 返回值：新数组（包含对应索引的元素）  
- 🌰 示例：  
  ```typescript
  at([10,20,30,40,50], [1,3,4]) // 返回 [20, 40, 50]  
  ```

---

### [GitHub - toss/es-toolkit: 一个现代的 JavaScript 实用工具库，速度提升 2-3 倍且体积缩小高达 97%——lodash 的重大升级版](https://github.com/toss/es-toolkit)

**原文标题**: [GitHub - toss/es-toolkit: A modern JavaScript utility library that's 2-3 times faster and up to 97% smaller—a major upgrade to lodash.](https://github.com/toss/es-toolkit)

es-toolkit 是一个高性能的现代 JavaScript 工具库，旨在替代 lodash，提供更快的速度和更小的体积，同时具备强大的类型支持和丰富的功能。

- 🚀 **高性能**：es-toolkit 在现代 JavaScript 环境中性能提升 2-3 倍。  
- 📦 **轻量级**：相比其他库，体积最多可减少 97%，支持 Tree Shaking。  
- 🔧 **功能丰富**：提供常用工具函数如 `debounce`、`delay`、`chunk`、`sum` 和 `pick` 等。  
- 🔄 **兼容 lodash**：通过 `es-toolkit/compat` 提供无缝替换 lodash 的兼容层。  
- 🛠 **TypeScript 支持**：内置类型注解和类型守卫（如 `isNotNil`）。  
- 🔍 **广泛使用**：被 Storybook、Recharts、ink 和 CKEditor 等知名开源项目采用。  
- ✅ **100% 测试覆盖率**：经过严格测试，确保稳定性和可靠性。  
- 🌍 **多语言文档**：支持英文、韩文、简体中文和日文。  
- 🤝 **开源贡献**：欢迎社区贡献，提供详细的贡献指南。  
- 📜 **MIT 许可证**：由 Viva Republica, Inc. 维护。

---

### [错误](https://javascriptweekly.com/link/172282/web)

**原文标题**: [Error](https://javascriptweekly.com/link/172282/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/172282/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [未找到标题](https://x.com/feross/status/1947762759011291460)

**原文标题**: [No title found](https://x.com/feross/status/1947762759011291460)

总结失败：Connection error.

---

### [npm 'is' 包在扩大的供应链攻击中被劫持 -...](https://socket.dev/blog/npm-is-package-hijacked-in-expanding-supply-chain-attack)

**原文标题**: [npm ‘is’ Package Hijacked in Expanding Supply Chain Attack -...](https://socket.dev/blog/npm-is-package-hijacked-in-expanding-supply-chain-attack)

Socket CEO Feross Aboukhadijeh 和 a16z 合伙人 Joel de la Garza 探讨了氛围编程、AI 驱动的软件开发，以及尽管存在风险，但 LLM 的兴起仍指向更安全和创新的未来。

- 🎙️ Socket CEO 和 a16z 合伙人讨论 AI 驱动的软件开发及其未来影响  
- 💡 提到“氛围编程”（vibe coding）概念，强调开发中的直觉与协作  
- 🤖 大型语言模型（LLM）的崛起带来安全风险，但潜力巨大  
- 🔒 尽管存在风险，AI 技术仍有望推动更安全和创新的软件开发  
- 🚀 讨论重点：如何在风险与进步之间找到平衡，实现技术发展的可持续性

---

### [npm '意外'删除 Stylus 包，导致构建和管道中断](https://www.bleepingcomputer.com/news/security/npm-accidentally-removes-stylus-package-breaks-builds-and-pipelines/)

**原文标题**: [npm 'accidentally' removes Stylus package, breaks builds and pipelines](https://www.bleepingcomputer.com/news/security/npm-accidentally-removes-stylus-package-breaks-builds-and-pipelines/)

npm 意外移除了 Stylus 包，导致全球依赖该包的构建和流水线中断。

- 🚨 npm 将所有版本的 Stylus 库替换为“安全占位”页面，导致依赖该包的构建和流水线中断。
- 📉 Stylus 是一个合法的 CSS 开发库，每周下载量达 300 万次。
- 🔍 Stylus 开发者 Lei Chen 表示该库被“意外封禁”，目前正在等待 npm 恢复访问权限。
- 🌐 多个大型项目（如 Angular 12）依赖 Stylus，导致构建失败。
- 🕵️‍♂️ 安全研究员 Tom Abai 发现，Stylus 的维护者之一“panya”发布了 3 个恶意包，导致其账户被封禁，连带 Stylus 被误删。
- 🔧 开发者提供了临时解决方案，如通过 GitHub 直接引用 Stylus 库或使用 npm 的 overrides 功能。
- 📢 GitHub 表示正在恢复 Stylus 的访问权限，称此次事件是由于关联维护者发布恶意包所致。
- ⚠️ 这是首次因管理错误导致合法项目被整体移除的案例。

---

### [EsJS | 基于 JavaScript 的西班牙语语法编程语言](https://es.js.org/)

**原文标题**: [EsJS | Lenguaje de programación con sintaxis en Español basado en JavaScript](https://es.js.org/)

概述：该内容展示了一个网页的主要导航栏，包含多个功能入口和外部链接。

- 🔍 搜索栏 - 提供搜索功能，可能用于查找内容或资源  
- 🏠 主导航 - 包括多个主要栏目如 Guía（指南）、Ecosistema（生态系统）等  
- 📚 示例 - 提供 Ejemplos（示例）供参考  
- 🎓 教程 - 包含 Tutorial（教程）学习资源  
- 💬 社区 - 链接至 Discord 社区平台  
- 💻 开发 - 提供 GitHub 代码仓库链接  
- 🎨 外观 - Appearance 选项可能用于界面个性化设置

---

### [编辑器 EsJS](https://editor.esjs.dev/)

**原文标题**: [Editor EsJS](https://editor.esjs.dev/)

好的，请提供您需要总结的文本内容，我会按照您要求的模板生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结  

- 📌 要点一  
- 🔍 要点二  
- 💡 要点三  

请提供具体文本，我会为您生成相应的总结！

---

### [更快的类型感知 Lint 规则：Biome 与 Oxlint 对比 - Jökull Sólberg](https://www.solberg.is/fast-type-aware-linting)

**原文标题**: [Faster Type-Aware Lint Rules: Biome vs. Oxlint - Jökull Sólberg](https://www.solberg.is/fast-type-aware-linting)

概述总结  
Biome 和 Oxlint 是新兴的基于 Rust 的快速 lint 工具，但它们在类型感知规则上采取了不同的策略。Biome 通过自定义类型合成器实现，而 Oxlint 则依赖 TypeScript 官方编译器的优化。社区还探索了利用编辑器语言服务器的第三种方案。长期来看，Oxlint 的策略更具优势，因为它能直接继承 TypeScript 团队的优化成果。

- 🚀 **ESLint 和 TypeScript-ESLint 的重要性**：类型感知规则（如`no-floating-promises`和`no-unsafe-*`）是生产级 TypeScript 代码库的核心，但速度较慢。  
- ⏳ **速度问题**：冷启动`typescript-eslint`在 TripToJapan.com 的 monorepo 中需要 7 分钟。  
- ⚡ **Rust-based linters 的崛起**：Biome 和 Oxlint 能在 1.5 秒内完成 lint，但缺乏类型信息支持。  
- 🔍 **Biome 的解决方案**：通过 Biotype 重新实现 TypeScript 的类型检查器，但规则覆盖有限且可能存在行为偏差。  
- 🎯 **Oxlint 的策略**：等待 TypeScript 官方编译器（tsgo）优化，未来通过`tsgolint`实现高效且准确的类型感知 lint。  
- 💡 **第三种方案**：社区项目（如`tsslint`和`tsl`）利用编辑器语言服务器，减少重复内存占用。  
- 📅 **未来展望**：Oxlint 计划在 2025 年 7 月 28 日推出类型感知规则，长期来看更可能成为推荐方案。  
- 📊 **里程碑**：包括 Biome 的规则扩展、Oxlint 的发布以及 tsgo 的优化进展。  
- 🔗 **相关链接**：提供了 Oxlint、Biome 和 typescript-eslint 的文档和博客文章。

---

### [Bun v1.2.19 | Bun 博客](https://bun.sh/blog/bun-v1.2.19)

**原文标题**: [Bun v1.2.19 | Bun Blog](https://bun.sh/blog/bun-v1.2.19)

Bun 是一个用于构建和测试全栈 JavaScript 和 TypeScript 应用程序的完整工具包。

- 🚀 **安装方式多样**：支持 curl、npm、PowerShell、scoop、brew 和 Docker 安装。
- 🔄 **升级 Bun**：使用 `bun upgrade` 或 `bun install --linker=isolated` 来提升性能。
- 📦 **包管理**：新增 `bun pm pkg` 命令，支持 `get`、`set`、`delete` 和 `fix` 操作。
- ⚡ **性能优化**：修复了工作区包重复评估的问题，提升了安装速度。
- 🔄 **依赖解析优先级**：调整为 `devDependencies` > `optionalDependencies` > `dependencies` > `peerDependencies`。
- 🔕 **静默打包**：`bun pm pack` 新增 `--quiet` 标志，简化脚本输出。
- 🔗 **工作区包链接**：支持从 `.npmrc` 读取 `link-workspace-packages` 和 `save-exact` 设置。
- ❓ **依赖追踪**：新增 `bun why` 命令，解释为何安装某个包。
- 📂 **顶层配置**：`bun install` 支持在 `package.json` 的顶层定义 `catalog` 和 `catalogs`。
- 🧪 **VS Code 测试集成**：Bun 的 VS Code 扩展现在支持原生 Test Explorer UI。
- 🤖 **AI 代理优化**：`bun test` 输出更紧凑，适合 AI 代理处理。
- 🔤 **变量替换**：`test.each` 标题支持变量替换，提升测试可读性。
- 🚫 **忽略测试覆盖文件**：新增 `test.coveragePathIgnorePatterns` 选项，支持 glob 模式。
- 🔗 **快照文件链接更新**：`.snap` 文件的头注释链接更新为官方文档。
- ⚡ **Bun.sql 性能提升**：自动管道化查询，性能提升高达 5 倍。
- ⏱️ **减少首次查询延迟**：新增 `--sql-preconnect` CLI 标志，预热数据库连接。
- 🔏 **Windows 代码签名**：`bun build --compile` 生成的独立可执行文件支持 Authenticode 签名。
- 🚀 **启动优化**：启动时间减少 1ms，内存使用减少 3MB。
- 🔍 **控制台日志深度**：新增 `--console-depth` 标志和 `bunfig.toml` 配置，控制 `console.log` 的深度。
- ⚡ **SIMD 加速注释解析**：使用 SIMD 指令加速大型多行注释的解析。
- 🌳 **改进树摇优化**：消除死代码路径中的 `try...catch...finally` 块。
- 🔄 **移除未使用的 Symbol.for()**：如果生成的符号未被使用，则移除调用。
- 🛠️ **Node.js 兼容性改进**：支持更多 V8 C++ API 和 `vm.constants.DONT_CONTEXTIFY`。
- 🌐 **网络接口修复**：`os.networkInterfaces()` 正确返回 `scopeid` 属性。
- 📜 **支持 process.features.typescript**：返回 `"transform"`，反映 Bun 默认转译 TypeScript。
- 🔍 **fs.glob 增强**：支持数组模式和 `exclude` 选项。
- 🗺️ **SourceMap 支持**：实现 `node:module` 的 `SourceMap` 类和 `findSourceMap()` 函数。
- 📦 **@types/bun 更智能**：根据 `tsconfig.json` 的 `lib` 配置自动扩展全局类型。
- 🐛 **多项错误修复**：包括 `NODE_NO_WARNINGS` 支持、`node:http2` 修复、`bun:test` 内存问题等。
- 🙏 **感谢贡献者**：共有 18 位贡献者参与了本次更新。

---

### [PythonMonkey - JavaScript 与 Python 的邂逅](https://pythonmonkey.io/)

**原文标题**: [PythonMonkey - JavaScript meets Python](https://pythonmonkey.io/)

Python 和 JavaScript 之间的无缝互操作性，通过 pythonmonkey 库实现。

- 🐍 安装 pythonmonkey 库：`$ pip install pythonmonkey`  
- 🔄 导入 pythonmonkey 模块：`>>> import pythonmonkey as pm`  
- 💻 执行 JavaScript 代码：`>>> hello = pm.eval(" 'Hello World'.toUpperCase(); ")`  
- 🖨️ 输出结果：`>>> print(hello)` 显示 `'HELLO WORLD'`

---

### [Reanimated 4 稳定版发布 —— React Native 动画的未来 | 作者：Krzysztof Magiera | 2025 年 7 月 | Software Mansion](https://blog.swmansion.com/reanimated-4-stable-release-the-future-of-react-native-animations-ba68210c3713?gi=7aa515bb3517)

**原文标题**: [Reanimated 4 Stable Release — the Future of React Native Animations | by Krzysztof Magiera | Jul, 2025 | Software Mansion](https://blog.swmansion.com/reanimated-4-stable-release-the-future-of-react-native-animations-ba68210c3713?gi=7aa515bb3517)

Reanimated 4 稳定版发布，这是自 Reanimated 2 引入 worklets 概念以来最重要的一次更新，带来了全新的声明式 CSS 兼容动画 API，同时优化了 worklets 的性能和可维护性。

- 🎬 **Reanimated 4 稳定版发布**：经过六个月的开发，Reanimated 4 首个稳定版本正式推出，这是自 Reanimated 2 以来最重要的更新。  
- 🎨 **CSS 动画与过渡 API**：新增声明式 CSS 兼容动画 API，简化状态驱动的动画代码，提升性能和可读性，特别适合从 Web 开发转向 React Native 的开发者。  
- ⚙️ **Worklets 的优化与独立**：复杂场景（如手势驱动动画）仍推荐使用 worklets，其代码已移至独立包 `react-native-worklets`，未来将获得更多性能优化。  
- 🔧 **兼容性与迁移**：API 与 Reanimated 3 兼容，但需应用 React Native 新架构（New Architecture）。旧版 Babel 配置仍可临时使用，但建议更新为 `react-native-worklets/plugin`。  
- 🚀 **弹簧动画改进**：默认弹簧动画实现更自然，不再依赖敏感阈值参数，推荐仅设置时长和阻尼比以获得更可预测的效果。  
- 📜 **废弃与变更**：移除了 Reanimated 3 中已弃用的方法，部分旧方法保留为无操作以兼容，详情可查阅迁移指南。  
- 🤝 **致谢与展望**：感谢 Shopify 和 Meta React Native 团队的支持，Reanimated 4 旨在帮助开发者打造更出色的动画体验。  
- 🔗 **相关资源**：发布说明、CSS 动画/过渡文档及联系方式详见文末链接。

---

### [发布 oxlint v1.8.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.8.0)

**原文标题**: [Release oxlint v1.8.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.8.0)

oxc-project/oxc 是一个公开的代码仓库，当前版本为 oxlint v1.8.0，发布于 2025-07-22。该版本包含新功能、错误修复、重构和其他改进。

- 🚀 **新特性**  
  - 通过缓冲区将 AST 传递给 JS (#12350)  
  - 在 `exhaustive-deps` 规则中添加自动修复功能 (#12354)  

- 🐛 **错误修复**  
  - 修复 `unicorn/prefer-number-properties` 中对 `Infinity` 的自动修复 (#12445)  
  - 修正 `unicorn/catch-error-name` 未使用 `ignore` 属性的问题 (#12446)  
  - 改进配置文件查找的错误处理 (#12391)  
  - 修复 `filename-case` 规则在无配置时的默认行为 (#12389)  

- 🚜 **重构**  
  - 简化 `prefer-number-properties` 的修复逻辑 (#12451)  
  - 在 `RawTransferMetadata` 中添加 `source_len` 字段 (#12383)  
  - 优化外部规则运行逻辑 (#12370)  

- 📚 **文档更新**  
  - 修正 `RawTransferMetadata2` 类型的注释 (#12428)  

- 💼 **其他**  
  - 发布 oxlint v1.8.0 (#12452)  

- 🎉 **社区反应**  
  - 10 个 👍、13 个 🎉、4 个 ❤️、8 个 🚀、3 个 👀 等共计 20 人参与互动

---

### [GitHub - jasmine/jasmine：适用于浏览器和Node.js的简易JavaScript测试框架](https://github.com/jasmine/jasmine)

**原文标题**: [GitHub - jasmine/jasmine: Simple JavaScript testing framework for browsers and node.js](https://github.com/jasmine/jasmine)

Jasmine 是一个行为驱动开发（BDD）的 JavaScript 测试框架，适用于浏览器和 Node.js 环境，不依赖任何浏览器、DOM 或其他 JavaScript 框架。

- 🌐 **多环境支持**：可在浏览器（如 Safari、Chrome、Firefox、Edge）和 Node.js（18.20.5+、20、22、24 版本）中运行。  
- 📜 **开源许可**：采用 MIT 许可证，允许自由使用和修改。  
- 🛠️ **简单易用**：提供清晰的文档和教程，如《你的第一个测试套件》指南，帮助快速上手。  
- 🔄 **持续维护**：由活跃团队维护，定期更新版本并支持主流环境。  
- 📊 **社区活跃**：拥有 15.8k GitHub Stars 和 2.2k Forks，贡献者超过 225 人。  
- 📦 **安装灵活**：支持多种安装方式，具体可参考官方《入门指南》。  
- ⚠️ **版本兼容**：从 Jasmine 4.x 升级需查看升级指南，部分旧环境（如特定浏览器版本）可能仅有限支持。  
- 👥 **贡献友好**：欢迎社区参与，提供详细的贡献者指南。

---

### [1KB JS 数字站——特伦斯·伊登的博客](https://shkspr.mobi/blog/2025/07/1kb-js-numbers-station/)

**原文标题**: [1KB JS Numbers Station – Terence Eden’s Blog](https://shkspr.mobi/blog/2025/07/1kb-js-numbers-station/)

概述：作者在 js1024 竞赛中创建了一个 1KB 大小的 JavaScript 数字电台模拟器，利用浏览器的文本转语音（TTS）API 生成随机数字和单词，营造出诡异的氛围。  

- 🎨 作者参加 js1024 竞赛，主题为“Creepy”，并决定模拟数字电台（Numbers Stations）。  
- 🔊 利用 JavaScript 的 TTS API，通过调整语速（rate）和音高（pitch）生成诡异的声音效果。  
- 🔢 随机生成数字，并通过筛选全局对象属性获取单一大写字母开头的单词（如“Event”“Atomics”）。  
- 🌍 支持多语言，随机选择语音库中的语言，使 TTS 以不同口音朗读英文单词。  
- 🖥️ 演示在部分浏览器（如 Chrome）效果良好，但在 Safari 等平台可能无法正常工作。  
- 📜 剩余字节用于生成 Unicode 字符组成的简单随机动画。  
- 🗳️ 作者邀请读者体验并投票支持他的作品。  
- 💬 用户反馈中提到不同设备的兼容性问题，部分人认为效果“诡异”或“自然”。

---

### [机器人验证](https://js1024.fun/)

**原文标题**: [Bot Verification](https://js1024.fun/)

验证中，请稍候...  

- 🔍 系统正在确认您是否为真人用户  
- ⏳ 此过程可能需要短暂等待  
- 🤖 旨在防止自动化程序滥用或恶意访问  
- ✅ 完成验证后即可正常使用服务

---

### [机器人验证](https://js1024.fun/demos/2025/24/bar)

**原文标题**: [Bot Verification](https://js1024.fun/demos/2025/24/bar)

验证中，请确认您不是机器人...

- 🔍 系统正在检测用户是否为真人操作  
- 🤖 防止自动化程序或机器人的安全验证步骤  
- ⏳ 短暂等待以确保验证过程完成  
- ✅ 验证通过后即可继续访问或操作

---

### [数字电台 - 维基百科](https://en.wikipedia.org/wiki/Numbers_station)

**原文标题**: [Numbers station - Wikipedia](https://en.wikipedia.org/wiki/Numbers_station)

数字电台是一种通过短波广播传送格式化数字信号的电台，通常被认为用于向外国情报人员传递加密信息。以下是关键点总结：

- 📻 **基本特征**：通过短波广播传送数字、字母或莫尔斯电码，使用语音合成或数字模式（如 PSK/FSK），多数有固定频率和时间表。
- 🕵️ **用途推测**：普遍认为用于间谍活动，消息可能通过一次性密码本加密，确保无法破解。
- 🌍 **历史背景**：最早可追溯至一战，冷战时期最为活跃，部分电台至今仍在运行。
- 🎵 **识别与分类**：爱好者为电台起绰号（如“林肯郡偷猎者”因其间隔信号使用同名民谣），并按语言/模式分类（如 E-英语、G-德语、X-其他信号）。
- 📡 **技术细节**：使用 10-100kW 功率的短波发射机，部分信号包含数据突发或子载波调制，适应复杂接收环境。
- 🏛️ **官方关联案例**：
  - 古巴“Atención”电台在 1998 年美国“古巴五人组”间谍案中被法庭证实用于传递指令。
  - 英国“林肯郡偷猎者”电台（疑似军情六处运营）于 2008 年停播。
  - 朝鲜 2016 年恢复数字广播，被疑为心理战。
- 🚨 **干扰与争议**：部分电台曾干扰民航通信或遭蓄意干扰（如中国“音乐电台”干扰以色列 E10 电台）。
- 🎭 **文化影响**：出现在影视（《数字电台》《边缘》）、音乐（Wilco 专辑《Yankee Hotel Foxtrot》）和游戏中（《使命召唤：黑色行动》）。
- 🔍 **监测与研究**：业余爱好者组织（如 ENIGMA 2000）记录分类电台，部分录音被收录于《The Conet Project》合集。

---

### [机器人验证](https://js1024.fun/demos/2025)

**原文标题**: [Bot Verification](https://js1024.fun/demos/2025)

验证中，请稍候...

- 🔍 系统正在确认您是否为真人用户  
- 🤖 防止自动化程序或机器人访问  
- ⏳ 短暂等待以确保安全验证  
- ✅ 完成后将正常跳转或继续操作

---

### [重温我的 2010 年 JavaScript 库](https://idiallo.com/blog/revisiting-my-old-javascript)

**原文标题**: [Revisiting My 2010 JavaScript Library](https://idiallo.com/blog/revisiting-my-old-javascript)

回顾作者 2010 年编写的 JavaScript 库，探索早期 Web 开发的挑战与解决方案，以及现代浏览器的进步。

- 🕰️ 作者回顾 2010 年编写的 JavaScript 库，展示了早期 Web 开发的挑战和解决方案。  
- 🌐 2010 年代浏览器兼容性问题严重，特别是 Internet Explorer 对 HTML5 的支持不足。  
- 🛠️ 作者通过 JavaScript 代码使 IE 识别 HTML5 标签，以便正确渲染样式。  
- 🔄 自定义数组循环方法，弥补早期浏览器缺乏`Array.map`和`Array.forEach`的不足。  
- 🤔 作者反思早期代码设计，如使用`this`而非参数传递，以及原型污染的副作用。  
- 🕵️♂️ 使用神秘代码`(!+"\v1")`检测 IE 浏览器，尽管原理不明但效果显著。  
- 📜 处理事件监听器的浏览器差异，统一`addEventListener`和`attachEvent`的使用。  
- ⏳ 异步脚本加载和依赖管理的解决方案，类似 Google Analytics 的`_gaq`方法。  
- 📱 早期移动设备检测的复杂正则表达式，应对多样化的用户代理字符串。  
- 🚀 现代浏览器已原生支持许多过去需要自定义代码的功能，减少了对外部库的依赖。  
- 🔮 作者期待未来 Web 开发的发展，并好奇今天的代码在未来会如何被看待。

---

### [Next.js：使用 Clerk 在 Next.js 应用中构建 MCP 服务器](https://clerk.com/docs/references/nextjs/build-mcp-server?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=MCP&utm_content=07-25-25&dub_id=fGtbQMlWaiYazyCz)

**原文标题**: [Next.js: Build an MCP server in your Next.js application with Clerk](https://clerk.com/docs/references/nextjs/build-mcp-server?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=MCP&utm_content=07-25-25&dub_id=fGtbQMlWaiYazyCz)

在 Next.js 应用中利用 Clerk 构建 MCP 服务器的分步指南

- 🔧 安装依赖：除了`@clerk/nextjs`外，还需安装`@vercel/mcp-adapter`和`@clerk/mcp-tools`工具包
- 🛠️ 项目结构：在 app 目录下创建动态路由`[transport]`，支持/mcp 和/sse 两种协议路径
- 🤖 工具定义：使用`createMcpHandler()`创建服务，通过`server.tool()`定义 LLM 可调用的工具（如示例工具 get_clerk_user_data）
- 🔒 安全验证：用`withMcpAuth()`包装处理器，集成 Clerk 的 OAuth 令牌验证机制
- 📡 元数据端点：必须暴露/.well-known/oauth-protected-resource 和/.well-known/oauth-authorization-server 元数据端点
- 🎯 工具实现：示例工具通过 Clerk 获取认证用户数据，返回 MCP 标准格式响应
- 🌐 CORS 处理：为元数据端点配置跨域请求处理
- ✅ 完成准备：替换示例工具后，客户端即可通过最新 MCP 规范安全调用服务

---

### [网络连载：《我承认 JavaScript 并非一无是处的唯一理由》](https://theexceptioncatcher.com/2025/07/webserial-the-javascript-feature-that-suprised-me/)

**原文标题**: [Web Serial: The Only Reason Iâll Admit JavaScript Isnât All Bad](https://theexceptioncatcher.com/2025/07/webserial-the-javascript-feature-that-suprised-me/)

作者与 JavaScript 的关系并不融洽，但认可其在特定场景下的价值，并对 Web Serial API 的实用性表示赞赏。

- 😠 作者对 JavaScript 的整体感受不佳，认为它被过度扩展（如 Electron、NodeJS），超出了其最初作为客户端脚本语言的定位。  
- 📦 批评了 JavaScript 的包管理（npm、yarn）缺乏结构，对比认为 Maven 等更合理。  
- 🐍 类似观点也适用于 Python，反对语言脱离其设计初衷的滥用（如长期运行的高负载服务）。  
- 👍 例外赞赏 Web Serial API，它通过浏览器安全地与串行设备交互（如刷写固件），简化了硬件操作流程。  
- 🔧 列举了实际应用案例：ESPHome、RATGDO、Sonoff Zigbee 路由器等设备的固件刷写均通过浏览器完成。  
- 🔒 强调 Web Serial 需加密站点（HTTPS）支持，兼顾便利与安全性。  
- 🤫 结尾调侃式承认对 JavaScript"不完全讨厌，但大部分时候依然反感"。

---

### [Web Serial API - Web API 接口 | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Serial_API)

**原文标题**: [Web Serial API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Serial_API)

Web Serial API 允许网站通过串行端口、USB 或蓝牙设备与串行设备进行读写交互，适用于 3D 打印机、微控制器等设备，但需在安全上下文（HTTPS）中使用，且目前为实验性技术，浏览器兼容性有限。

- 🌐 **Web Serial API 功能**：提供网站与串行设备（如 3D 打印机、BBC micro:bit）的通信能力，支持串行端口、USB 或蓝牙模拟设备。  
- ⚠️ **实验性技术**：需谨慎用于生产环境，浏览器兼容性有限，部分主流浏览器不支持。  
- 🔒 **安全限制**：仅限 HTTPS 安全上下文使用，且需通过权限策略（Permissions-Policy）控制访问。  
- 🔧 **核心接口**：  
  - `Serial`：查找和连接串行端口。  
  - `SerialPort`：访问主机设备的串行端口。  
  - `Navigator.serial` 和 `WorkerNavigator.serial`：作为 API 入口点。  
- 📡 **事件与方法**：  
  - 监听设备连接/断开事件（`connect`/`disconnect`）。  
  - 通过 `getPorts()` 获取已授权端口，`requestPort()` 请求用户授权新设备。  
- 📖 **代码示例**：  
  - 检查可用端口并处理用户授权（如点击按钮触发）。  
  - 循环读取端口数据，处理非致命错误直至 `SerialPort.readable` 为 `null`。  
- 🔗 **相关资源**：  
  - 与 WebUSB API、WebHID API 互补，用于不同外设通信场景。  
  - 规范文档和浏览器兼容性表需仔细查阅。

---

### [现代 CSS 是时候终结单页应用了——乔诺·奥尔德森](https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/)

**原文标题**: [It's time for modern CSS to kill the SPA - Jono Alderson](https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/)

现代 CSS 技术（如视图过渡 API 和推测规则）已使单页应用（SPA）的核心优势（如流畅导航）变得过时，但开发者仍过度依赖 SPA 框架，导致性能下降和复杂性问题。

- 🚀 **SPA 的虚假承诺**：SPA 本应提供流畅体验，但实际常导致加载延迟、布局错乱和性能问题，且依赖大量 JavaScript 模拟原生导航。  
- 🌐 **浏览器的进步**：现代 CSS 技术（如视图过渡 API）支持原生页面过渡动画，无需 JavaScript 即可实现跨页面平滑过渡和共享元素动画。  
- ⚡ **推测规则**：通过预加载或预渲染页面，实现即时导航，显著提升用户体验，但需注意性能优化。  
- 📉 **SPA 与 MPA 性能对比**：传统 SPA（如 Next.js）通常体积庞大且加载慢，而现代多页应用（MPA）结合 CSS 技术更轻量、快速且 SEO 友好。  
- 🛠️ **开发建议**：大多数网站无需 SPA 的复杂性，应优先使用 HTML、原生导航和 CSS 动画，仅在需要时添加轻量交互。  
- 🔄 **平台优势**：现代浏览器（如 Back/Forward 缓存）奖励简洁架构，而 SPA 的设计模式常破坏这些优化机会。  
- 💡 **总结**：利用原生 CSS 和浏览器功能构建网站，避免不必要的 JavaScript，以实现更快、更稳定且易维护的体验。

---

### [我们将网站迁移至 Eleventy，性能提升 24% | Etch 软件工作室](https://etch.co/blog/we-migrated-our-site-to-eleventy-and-increased-performance-by-24-percent)

**原文标题**: [We migrated our site to Eleventy and increased performance by 24% | Etch Software Studio](https://etch.co/blog/we-migrated-our-site-to-eleventy-and-increased-performance-by-24-percent)

将网站从 Next.js 迁移到 Eleventy 后，性能提升了 24%，减少了依赖并优化了用户体验。

- 🚀 性能提升：Lighthouse 性能评分从 76 升至 97，主页 JavaScript 体积从 2161KB 降至 11.3KB  
- 📦 依赖简化：NPM 依赖从 1115 个减少到 13 个，代码行数从 6877 降至 4307  
- 🏗️ 工具选择：Eleventy 提供轻量级构建工具，专注于 HTML 模板和静态资源，不增加浏览器负担  
- 🔧 稳定性：自 2018 年以来仅 3 次重大版本更新，减少维护负担  
- 🛠️ 开发挑战：需手动实现 Next.js 的现成功能（如服务工人、样式打包）  
- 📝 模板语言：选用 WebC（基于 HTML 的模板语言），但学习曲线较陡且社区支持较少  
- 💡 核心优势：明确区分构建与浏览器环境，构建后不额外注入代码  
- ⚡ 最终效果：构建更快、用户体验更流畅，工具链更简洁

---

### [Eleventy 是一个更简单的静态网站生成器](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

Eleventy 是一个简单易用的静态网站生成器，支持多种模板语言，具有快速构建和高度灵活性的特点。

- 🚀 **快速构建**：Eleventy 构建速度极快，处理 4000 个 Markdown 文件仅需 1.93 秒，远超其他工具如 Astro、Gatsby 和 Next.js。
- 🛠️ **多模板支持**：支持多种模板语言，包括 HTML、Markdown、WebC、JavaScript、Liquid 等，且可以混合使用。
- 📦 **零配置启动**：无需复杂配置即可开始使用，同时支持灵活的扩展选项。
- 🌍 **生产就绪**：被 NASA、Google、Microsoft 等知名机构使用，稳定且可靠。
- 🔄 **增量迁移**：允许逐步迁移现有项目，无需一次性重构。
- 📜 **独立模板语言**：使用标准模板语言，避免锁定，便于未来迁移。
- � **无客户端 JS 默认**：默认不依赖客户端 JavaScript，适合长期稳定的项目。
- 🏆 **社区支持**：拥有活跃且友好的开发者社区。
- 📊 **高性能**：生成速度快，输出优化，适合大型项目。
- 📂 **灵活目录结构**：不强制特定目录结构，适应现有项目布局。

---

### [处理带参数的 JavaScript 事件监听器——Smashing Magazine](https://www.smashingmagazine.com/2025/07/handling-javascript-event-listeners-parameters/)

**原文标题**: [Handling JavaScript Event Listeners With Parameters — Smashing Magazine](https://www.smashingmagazine.com/2025/07/handling-javascript-event-listeners-parameters/)

JavaScript 事件监听器带参数处理的实用指南

- 🚀 事件监听器在 JavaScript 中至关重要，但管理不当可能导致内存泄漏和性能问题  
- 🛠️ 常见错误：在 addEventListener 中直接调用带参数的函数，导致立即执行而非事件触发时执行  
- 🔄 解决方案 1：使用箭头/匿名函数包裹目标函数，通过 AbortController 移除监听器  
- 🧩 解决方案 2：利用闭包特性，外层函数接收参数，内层函数作为事件处理器  
- 🗑️ 最佳实践：始终移除不再需要的事件监听器，防止内存泄漏  
- 💡 关键技巧：存储函数引用便于传统 removeEventListener 方法操作  
- 🌐 适用场景：动态列表操作（如带 ID 参数的删除按钮）等需要参数传递的交互  
- ⚠️ 注意事项：箭头函数无法被常规 removeEventListener 移除  
- 📚 技术支撑：AbortController 适合批量移除，闭包保持参数访问性  

（通过两种主流方案和实用示例，详解了带参事件监听器的正确处理与内存管理）

---

### [吕的主页](https://lui.ie/guides/semantic-search-fonts)

**原文标题**: [Lui's Homepage](https://lui.ie/guides/semantic-search-fonts)

好的，请提供您需要总结的文本内容，我会按照您要求的模板进行整理，包括概述总结和带 emoji 的简明要点列表。  

示例模板：  

这里是文章的概述总结，简明扼要地概括全文核心内容。  

- 🌟 第一个关键点  
- 🔍 第二个关键点  
- 📊 第三个关键点  

请提供您的文本，我会立即为您处理！

---

### [交互式文本销毁效果：使用 Three.js、WebGPU 与 TSL 实现 | Codrops](https://tympanus.net/codrops/2025/07/22/interactive-text-destruction-with-three-js-webgpu-and-tsl/)

**原文标题**: [Interactive Text Destruction with Three.js, WebGPU, and TSL | Codrops](https://tympanus.net/codrops/2025/07/22/interactive-text-destruction-with-three-js-webgpu-and-tsl/)

本文介绍了如何使用 Three.js、WebGPU 和 Three Shader Language (TSL) 创建一个交互式 3D 文本效果，其中字母会爆炸成动态形状。

- 🎨 **创意背景**：作者回顾了从 Flash 到现代 Web 技术的演变，强调了 Three.js 等工具如何重新赋予网页丰富的交互体验。
- 🛠️ **项目结构**：项目分为预加载资源和构建场景两部分，使用 FontLoader 加载字体文件。
- 🌐 **场景设置**：使用 WebGPURenderer 和 TSL，设置基本场景、光照和环境。
- ✏️ **3D 文本创建**：使用 TextGeometry 生成 3D 文本，并通过计算边界框实现居中。
- 💥 **交互效果**：通过 TSL 实现顶点变形效果，根据指针位置动态改变几何形状。
- 🌀 **物理模拟**：引入弹簧物理和摩擦力，使变形效果更加自然和动态。
- 🌈 **视觉效果增强**：通过噪声和旋转增加动画的随机性，调整材质颜色和自发光效果。
- 🌫️ **后期处理**：添加环境光遮蔽、辉光和噪声等后期处理效果，提升整体视觉体验。
- 📚 **总结**：教程详细展示了从基础设置到高级效果的完整流程，适合对 3D Web 开发感兴趣的开发者。

---

### [React Router 与 React 服务器组件：前行之路 | Remix](https://remix.run/blog/react-router-and-react-server-components)

**原文标题**: [React Router and React Server Components: The Path Forward | Remix](https://remix.run/blog/react-router-and-react-server-components)

React Router 与 React Server Components（RSC）的结合将带来更强大的数据模式和简化的架构，同时保持对现有功能的兼容性。以下是关键点总结：

- 🚀 **RSC 支持**：React Router 将支持 RSC，提供更强大的数据模式，同时简化底层架构。
- 🔄 **数据内联**：Framework Mode 和 RSC 都支持数据内联，React Router RSC 将同时支持两种模式。
- ⏳ **流式 UI**：两种模式都支持流式 UI，React Router RSC 将保留这两种实现方式。
- 📦 **代码分割**：Framework Mode 通过路由配置文件实现，RSC 通过动态导入实现，React Router RSC 将支持两种方式。
- 🛠 **架构简化**：新的 RSC 架构不再依赖复杂的打包器插件，而是通过普通数据结构和函数调用来实现路由。
- 🔧 **兼容性**：现有 Framework Mode 用户无需迁移，Data/Declarative Mode 用户未来可选择 RSC 版本。
- 🆕 **新项目建议**：由于 RSC 仍不稳定，建议新项目使用现有 Framework Mode 或 Data/Declarative API。
- 🔮 **未来计划**：计划为 Vite 提供 RSC-enabled Framework Mode，进一步简化路由配置和打包器集成。
- 🌟 **前景展望**：React Router 将变得更强大和灵活，支持从 SPA 到复杂 SSR 应用的各种用例。

---

### [发布 3.7.0 版 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.7.0)

**原文标题**: [Release 3.7.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/3.7.0)

Transformers.js 发布了 3.7.0 版本，新增了对 Voxtral、LFM2 和 ModernBERT Decoder 三种新模型架构的支持，并包含其他改进。

- 🚀 **新模型支持**  
  - 新增 Voxtral、LFM2 和 ModernBERT Decoder 三种架构。  

- 🎙️ **Voxtral**  
  - 基于 Ministral 3B 增强，支持音频输入，擅长语音转录、翻译和音频理解。  
  - 提供 ONNX 权重和在线演示。  

- 🤖 **LFM2**  
  - 由 Liquid AI 开发，专为边缘 AI 和设备端部署设计，提供 350M、700M 和 1.2B 三种参数规模。  

- 📊 **ModernBERT Decoder**  
  - 属于 Ettin 套件的一部分，提供编码器和解码器架构的公平比较，支持多种规模模型。  

- 🛠️ **其他改进**  
  - 在文本生成管道中添加了特殊令牌支持。  
  - 完整更新日志可查看 3.6.3 到 3.7.0 的变更。

---

### [GitHub - lirantal/npq：在预安装阶段通过审计安全安装npm包](https://github.com/lirantal/npq)

**原文标题**: [GitHub - lirantal/npq: safely install npm packages by auditing them pre-install stage](https://github.com/lirantal/npq)

npq 是一个用于在安装 npm 包之前进行安全检查的工具，通过多种检查机制确保包的安全性。

- 🔍 **功能概述**：npq 在安装前审核 npm 包，检查漏洞、包年龄、下载量等，确保安全性。
- 🛡️ **安全检查**：查询 snyk.io 漏洞数据库，检查包是否有公开的安全漏洞。
- 📊 **包信息检查**：包括包年龄、下载量、README、LICENSE 文件以及预安装脚本。
- ⚠️ **免责声明**：npq 不能保证绝对安全，仍需谨慎。
- 📹 **演示**：提供演示视频展示 npq 的使用流程。
- 📥 **安装**：通过 `npm install -g npq` 全局安装，推荐使用 npm 而非 yarn。
- 🔧 **使用示例**：`npq install express` 安装包时进行安全检查。
- 🔄 **嵌入日常使用**：可以通过别名将 npq 嵌入日常 npm 使用中，无需显式运行。
- 📦 **支持多种包管理器**：通过环境变量 `NPQ_PKG_MGR` 指定 yarn、pnpm 等。
- 🛠️ **Marshalls 检查项**：包括包年龄、作者、下载量、README、仓库 URL、安装脚本、许可证等多项检查。
- 🚫 **禁用检查项**：通过环境变量禁用特定检查，如 `MARSHALL_DISABLE_SNYK=1` 禁用 Snyk 检查。
- 🧪 **干运行**：`npq install express --dry-run` 只检查不安装。
- 📜 **纯文本输出**：`npq install express --plain` 强制非富文本输出。
- ❓ **FAQ**：解答常见问题，如与 npm audit 的区别、是否需要 Snyk API 密钥等。
- 👥 **贡献**：欢迎贡献，请参考 CONTRIBUTING 指南。
- 👤 **作者**：Liran Tal，联系方式 liran.tal@gmail.com。

---

### [介绍 Embrace 全新 Web RUM 产品](https://embrace.io/blog/introducing-embrace-web-rum/?utm_source=newsletter&utm_medium=paid&utm_campaign=javascript-weekly-7-25-2025)

**原文标题**: [Introducing Embrace's new Web RUM Product](https://embrace.io/blog/introducing-embrace-web-rum/?utm_source=newsletter&utm_medium=paid&utm_campaign=javascript-weekly-7-25-2025)

理解网页性能需从用户视角出发，结合技术数据与行为分析，全面优化体验。

- 🔍 解决复杂网页问题需上下文：了解用户操作、网络状况及交互延迟等关键信息。  
- 🕒 时间轴功能提供完整会话记录：追踪技术事件与用户行为，还原问题发生场景。  
- 🌐 网络条件影响体验：实时监测网络波动对用户操作流畅度的具体影响。  
- 🔁 重复交互暴露痛点：识别用户多次尝试的异常操作，定位体验瓶颈。  
- 📊 技术 + 行为双维度分析：通过 RUM 工具整合数据，精准诊断性能问题根源。

---

### [无标题 UI React —— React UI 组件库](https://www.untitledui.com/react)

**原文标题**: [Untitled UI React â React UI Component Library](https://www.untitledui.com/react)

Untitled UI React 是一个开源的 React UI 组件库，基于 Tailwind CSS 和 React Aria 构建，提供丰富的组件和模板，帮助开发者快速构建现代、美观的界面。

- 🚀 **开源组件库**：Untitled UI React 是世界上最大的开源 React 组件库，支持直接复制、粘贴和构建。  
- 🛠️ **技术栈**：基于 React v19.1、Tailwind CSS v4.1、TypeScript v5.8 和 React Aria，确保高性能和可访问性。  
- 📦 **丰富组件**：包含 5000+ 组件和 250+ 页面示例，如按钮、表格、日历、图表等，满足各种开发需求。  
- 🎨 **设计同步**：与 Untitled UI Figma 完美同步，确保设计和代码一致性，支持免费更新。  
- ⚡ **快速启动**：提供 CLI 工具和预配置的 Starter Kits（如 Next.js、Vite），支持一键初始化项目。  
- 🌙 **暗黑模式**：内置 CSS 变量支持，轻松实现暗黑模式切换。  
- 💰 **灵活定价**：提供免费版和付费 PRO 版（个人/团队授权），支持终身更新和无限项目使用。  
- 🌍 **社区认可**：被 280,000+ 设计师和开发者使用，包括多家知名公司和独立开发者。  
- 📚 **详细文档**：提供完整的文档和示例，帮助开发者快速上手。

---

### [介绍 | 无标题用户界面](https://untitledui.com/react/docs/introduction)

**原文标题**: [Introduction | Untitled UI](https://untitledui.com/react/docs/introduction)

Untitled UI React 是一个基于全球最大 Figma UI 套件的开源 React 组件库，提供现成的高质量组件，帮助快速构建现代界面。

- 🚀 **简介**：Untitled UI React 是全球最大的开源 React 组件集合，基于 Tailwind CSS 和 React Aria 构建，可直接复制粘贴使用。  
- 🛠️ **技术栈**：使用 React v19.1、Tailwind CSS v4.1、TypeScript v5.8 和 React Aria v1.9，保持简洁高效。  
- ♿ **无障碍性**：所有组件均基于 React Aria 构建，确保符合无障碍标准。  
- 🔓 **开源优势**：直接提供源代码，无依赖管理，可自由修改和扩展组件。  
- 💡 **免费与付费**：基础组件免费（MIT 许可），PRO 版提供更多高级组件和示例页面。  
- 🔄 **持续更新**：所有产品终身免费更新，紧跟技术最新版本。  
- 🎨 **Figma 配套**：与 Untitled UI Figma 设计系统完美同步，保持设计与代码一致性。  
- 🤝 **贡献欢迎**：可通过 GitHub 提交问题或拉取请求参与改进。  
- 📥 **安装指南**：提供详细的安装指南，帮助快速上手。

---

### [GitHub - codpro2005/ts-regexp: 一个极简、静态类型的 JavaScript RegExp 替代方案](https://github.com/codpro2005/ts-regexp/tree/main)

**原文标题**: [GitHub - codpro2005/ts-regexp: A minimal, statically typed alternative to JavaScript's RegExp.](https://github.com/codpro2005/ts-regexp/tree/main)

一个最小化、静态类型的 JavaScript RegExp 替代方案。

- 🚀 **项目概述**：ts-regexp 是一个提供静态类型支持的正则表达式工具，旨在替代 JavaScript 的原生 RegExp。
- 📜 **许可证**：MIT 许可证。
- ⭐ **受欢迎程度**：50 颗星，1 个 fork。
- 🛠️ **功能特点**：
  - ✅ 严格类型的命名和未命名捕获组。
  - ✅ 支持上下文感知。
  - ✅ 解析嵌套组、不同组类型（非捕获、环视、命名捕获等）、交替、字符类和转义字符。
  - ✅ 从量词推断组的可选性（`?`、`*`、`{n,m}`）。
  - ✅ 验证标志。
  - ✅ 支持动态（非字面量）模式和标志输入。
- 📦 **安装**：
  - 使用 npm：`npm install ts-regexp`
  - 使用 yarn：`yarn add ts-regexp`
  - 使用 pnpm：`pnpm add ts-regexp`
- 🧩 **使用方法**：
  - 导入 `typedRegExp` 并像原生 `RegExp` 构造函数一样使用。
  - 提供标准 `RegExp` 方法，但具有等效或改进的类型。
  - 提供 `RegExp` 相关的 `string.prototype` 方法作为 `${MethodName}In`。
  - 当使用全局标志（`g`）时，提供额外的方法。
- 🔧 **高级用法**：如果需要访问底层的 `RegExp` 实例，可以使用 `pattern.regExp`。
- 📘 **API**：目前可以参考示例或使用说明。

---

### [GitHub - apexcharts/apexcharts.js: 📊 基于 SVG 构建的交互式 JavaScript 图表库](https://github.com/apexcharts/apexcharts.js)

**原文标题**: [GitHub - apexcharts/apexcharts.js: 📊 Interactive JavaScript Charts built on SVG](https://github.com/apexcharts/apexcharts.js)

ApexCharts.js 是一个基于 SVG 的交互式 JavaScript 图表库，提供丰富的图表类型和简单易用的 API，适用于各种数据可视化需求。

- 📊 **功能丰富**：支持多种图表类型（如柱状图、折线图、蜡烛图、热力图等），并提供交互功能（缩放、平移、动态更新数据等）。  
- 🛠️ **易于集成**：可通过 npm 安装或直接引入脚本，并提供 Vue/React/Angular 等框架的官方封装。  
- 🌟 **开源热门**：GitHub 上获得 14.8k 星标，1.4k 分叉，社区活跃。  
- 📂 **模块化结构**：源码结构清晰，包含示例、测试和类型定义，支持自定义开发与扩展。  
- 📜 **双许可证**：支持个人和商业使用，详情见官网许可协议。  
- 🔗 **生态完善**：提供第三方封装（如 Ruby、Laravel、Blazor 等），并推荐高级数据网格工具 Ignite UI Grids。  
- 📱 **响应式设计**：图表自动适配不同设备，支持动态数据更新和混合图表组合。  
- 📍 **开发友好**：内置 Webpack 调试和构建脚本，贡献指南详细。  
- 🌐 **文档齐全**：官网提供完整文档和 100+ 示例，便于快速上手。

---

### [解析数据 – ApexCharts.js](https://apexcharts.com/docs/parsing-data/)

**原文标题**: [Parsing Data – ApexCharts.js](https://apexcharts.com/docs/parsing-data/)

ApexCharts 是一个功能强大的图表库，支持多种图表类型和数据解析功能，适用于各种数据可视化需求。

- 📊 **图表类型**：支持 20 种图表类型，包括线图、柱状图、饼图、雷达图等。
- 🔧 **安装与使用**：提供详细的安装指南和创建第一个图表的教程。
- 📂 **数据解析**：支持直接解析和映射原始数据对象，无需手动转换（v5.3.0+）。
- 🌐 **多数据源支持**：每个系列可以使用不同的数据源和解析配置。
- 🔄 **全局与系列级配置**：支持全局解析配置，并可针对特定系列进行覆盖。
- 🏗 **嵌套数据支持**：通过点符号映射嵌套 JSON 对象的字段。
- 📈 **动态更新**：支持从 JSON API 和 AJAX 更新图表数据。
- 🎨 **设计与主题**：提供多种颜色、主题、渐变和阴影效果。
- ⚙ **集成**：支持 Angular、React 和 Vue 等前端框架。
- 📜 **参考文档**：详细的选项和方法参考，便于开发者快速查阅。
- 🚀 **高性能**：每周下载量超过 100 万次，包含 100 多个示例。

---

### [JavaScript 图表示例与演示 – ApexCharts.js](https://apexcharts.com/javascript-chart-demos/)

**原文标题**: [JavaScript Chart Examples & Samples Demo – ApexCharts.js](https://apexcharts.com/javascript-chart-demos/)

概述  
探索 ApexCharts 中丰富的 JavaScript 图表功能，所有示例均附带源代码，助您节省开发时间。  

- 📊 **JavaScript 图表演示** - 展示 ApexCharts 的多样化图表功能。  
- 💻 **多框架支持** - 包含 JS、Angular、Vue 和 React 等框架的示例。  
- 📈 **图表类型丰富** - 涵盖折线图、面积图、柱状图、条形图、混合图等。  
- 🕒 **时间轴/范围条** - 支持时间轴和范围条图表展示。  
- 📊 **特殊图表** - 包括漏斗图、K 线图、箱线图、气泡图等。  
- 🌡️ **热力图** - 提供热力图和树形图等数据可视化方式。  
- 🥧 **饼图与极坐标** - 支持饼图、雷达图、极坐标面积图等。  
- 📱 **仪表盘** - 包含多种仪表盘示例，满足不同场景需求。  
- 🔍 **源码提供** - 所有示例均附带源代码，便于快速集成和开发。

---

### [Vue-Multiselect | Vue 选择组件库](https://vue-multiselect.js.org/)

**原文标题**: [Vue-Multiselect | Vue Select Library](https://vue-multiselect.js.org/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

概述总结  
- 📌 要点 1  
- 🔍 要点 2  
- 💡 要点 3  

请提供具体文本，我会为您整理！

---

### [GitHub - sindresorhus/eslint-plugin-unicorn：100多条强大的ESLint规则](https://github.com/sindresorhus/eslint-plugin-unicorn)

**原文标题**: [GitHub - sindresorhus/eslint-plugin-unicorn: More than 100 powerful ESLint rules](https://github.com/sindresorhus/eslint-plugin-unicorn)

eslint-plugin-unicorn 是一个包含 100 多个强大 ESLint 规则的插件，旨在提升代码质量和开发体验。

- 🦄 提供 100 多个 ESLint 规则，涵盖代码风格、错误预防和最佳实践  
- 📦 支持 ESM 和 flat config，要求 ESLint >=9.20.0  
- ⚙️ 提供推荐配置（recommended）和全规则配置（all）  
- 🔧 许多规则支持自动修复（--fix）或编辑器建议手动修复  
- 📜 开源项目，采用 MIT 许可证  
- 🌟 GitHub 上获得 4.7k stars 和 412 forks  
- 🛠️ 维护团队包括 Sindre Sorhus 等知名开发者  
- 📌 适用于 Node.js 和 JavaScript 项目  
- 🔍 规则分类明确，包括代码风格、现代 API 偏好、错误预防等  
- 💡 提供详细的文档和规则说明

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=july25th2025%20)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=july25th2025%20)

Meticulous AI 提供了一种无需编写和维护测试的自动化测试解决方案，通过记录用户交互并生成持续演化的测试套件，帮助开发者高效覆盖应用的所有边缘情况。

- 🚀 **无需编写测试** - Meticulous AI 自动生成并维护测试套件，覆盖所有用户流程和边缘情况。  
- 🎯 **记录用户交互** - 通过在开发、预发布和生产环境中添加脚本标签，记录用户会话以生成测试用例。  
- 🤖 **智能测试生成** - AI 引擎根据代码分支和用户交互动态生成视觉端到端测试，确保全面覆盖。  
- ⚡ **快速反馈** - 在合并代码前查看 PR 对用户工作流的影响，避免回归问题。  
- 🛠️ **无缝集成** - 支持与现有测试套件结合使用或完全替代，兼容多种前端框架（如 React、Vue、Angular 等）。  
- 🚄 **高效并行测试** - 测试任务在计算集群上并行执行，可在 120 秒内完成数千次测试。  
- 💬 **用户见证** - Dropbox 和 Notion 等 100 多家组织认可其提升开发效率和代码质量的效果。  
- 🔒 **安全可靠** - 从底层消除测试波动，确保测试结果稳定且无干扰。  
- 📥 **快速上手** - 只需几分钟即可完成设置，立即为整个应用生成测试覆盖。

---

### [KeyLines - JavaScript 开发者的图形可视化 SDK](https://cambridge-intelligence.com/keylines/?utm_campaign=16812718-React%20Status%20newsletter%20ad&utm_source=NewsletterAd&utm_medium=SponsoredLink)

**原文标题**: [
		KeyLines - The Graph Visualization SDK for JavaScript Developers	](https://cambridge-intelligence.com/keylines/?utm_campaign=16812718-React%20Status%20newsletter%20ad&utm_source=NewsletterAd&utm_medium=SponsoredLink)

KeyLines 是一款专为 JavaScript 开发者设计的图可视化工具包，帮助用户快速构建高性能、可扩展且直观的图可视化应用。

- 🚀 **快速开发**：KeyLines 提供快速构建强大、美观且交互性强的图可视化工具，适应各种技术栈。  
- 🔍 **揭示隐藏洞察**：支持构建交互式图可视化工具，帮助用户发现威胁和隐藏的数据关联。  
- 🛠️ **灵活工具包**：KeyLines 是一个灵活的 JavaScript 工具包，可根据用户需求、数据特性和问题定制应用。  
- 🌐 **广泛兼容性**：支持所有浏览器、设备、服务器和数据库，并提供清晰的教程、演示和 API 文档。  
- ⚡ **高性能引擎**：利用 HTML5 和 WebGL 图形渲染技术，提供快速且直观的可视化体验。  
- 📈 **可扩展性**：基于现代网络技术，可轻松集成到其他工具中并部署到任何地方。  
- 🤝 **全面支持**：提供从入门指导到项目健康检查、深度研讨会和一线支持的全程专家支持。  
- 🕒 **高级功能**：包括时间序列分析、地理空间分析、社交网络分析和自动图布局等高级功能。  
- 🌍 **全球客户**：客户遍布六大洲，涵盖初创公司、财富 500 强企业和国家政府机构。  
- 📚 **资源丰富**：提供白皮书下载、博客文章和案例研究，帮助用户更好地理解和应用图可视化技术。

---

### [SVG 入门指南：友好教程 • 乔希·W·科莫](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/)

**原文标题**: [A Friendly Introduction to SVG • Josh W. Comeau](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/)

SVG（可缩放矢量图形）是一种基于 XML 的图像格式，可以在浏览器中实现丰富的动态效果和交互性。以下是文章的核心内容总结：

- 🎨 **SVG 简介**  
  - SVG 是一种矢量图像格式，不同于 JPEG 或 PNG，它使用 XML 语法描述图形。  
  - 可以直接内联到 HTML 中，并通过 CSS 和 JavaScript 动态修改。

- ✏️ **基本形状**  
  - SVG 提供多种基本形状元素，如`<line>`、`<rect>`、`<circle>`、`<ellipse>`和`<polygon>`。  
  - 每种形状通过属性（如`cx`、`cy`、`r`等）控制位置和大小。

- 🔍 **可缩放性**  
  - 使用`viewBox`属性定义内部坐标系，实现图形在不同尺寸下的自适应缩放。  
  - SVG 是矢量图形，无限放大仍保持清晰。

- 🖌️ **表现属性**  
  - `fill`和`stroke`属性控制填充和描边样式。  
  - `stroke-dasharray`和`stroke-linecap`等属性可以创建复杂的描边效果。

- 🎥 **动态效果**  
  - 通过 CSS 过渡或动画可以动态修改 SVG 属性（如`stroke-dashoffset`），实现绘制动画或加载效果。  
  - 使用 JavaScript 计算路径长度（`getTotalLength()`）实现精准动画控制。

- 🚀 **进阶应用**  
  - SVG 的`<path>`元素支持复杂路径绘制（如贝塞尔曲线），适合高级图形设计。  
  - 未来课程将深入探讨 SVG 动画和交互技巧。

---

### [HTML 2025 现状](https://survey.devographics.com/en-US/survey/state-of-html/2025)

**原文标题**: [State of HTML 2025](https://survey.devographics.com/en-US/survey/state-of-html/2025)

2023 年，在 State of JS 和 State of CSS 调查进行数年后，团队意识到缺少对 HTML 技术的关注，因此推出了首个 State of HTML 调查，由 Lea Verou 领导，创下 21,000 名受访者的记录，并引入新的 UI 范式。2025 年，调查新增 35 项功能，并增加了“图形与多媒体”和“性能”两个新部分。调查结果将影响浏览器厂商的路线图，参与者可以帮助塑造 Web 的未来。  

- 🌐 2023 年推出首个 State of HTML 调查，填补了 JS 和 CSS 之外的空白  
- 🚀 由 Lea Verou 领导，首年吸引 21,000 名受访者，创下新纪录  
- ✨ 2025 年新增 35 项功能，引入“图形与多媒体”和“性能”板块  
- 📊 调查结果将影响浏览器厂商的路线图，帮助塑造 Web 未来  
- ⏱ 填写调查约需 10-15 分钟，面向所有网站和 Web 应用开发者  
- 📅 调查时间为 2025 年 7 月 15 日至 8 月 15 日，结果于 9 月 15 日发布  
- 🌍 由 Devographics 团队运营，支持多语言翻译，开放设计过程  
- 🔍 目标：衡量新 HTML 功能和浏览器 API 的认知度，跟踪使用趋势  
- 📢 呼吁志愿者协助翻译，支持多种语言版本

---

### [谷歌在线安全博客：推出 OSS Rebuild 项目——开源重建，持久耐用](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html)

**原文标题**: [
Google Online Security Blog: Introducing OSS Rebuild: Open Source, Rebuilt to Last
](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html)

Google 宣布推出 OSS Rebuild 项目，旨在通过重建上游开源组件增强软件供应链安全，为安全团队提供可靠数据以防范攻击，同时不增加维护者负担。

- 🛠️ **项目组成**：包括自动化构建定义生成、SLSA 合规证明、构建可观测性工具及可自托管的基础设施定义。  
- 🌍 **开源现状**：开源软件占现代应用的 77%，价值超 12 万亿美元，但广泛使用也使其成为攻击目标。  
- 🎯 **项目目标**：通过透明化构建流程和生成安全元数据，提升供应链安全性，支持 PyPI、npm 和 Crates.io 等主流生态。  
- 🔍 **工作原理**：自动化重建包并与上游对比，发布 SLSA 证明，支持验证来源和自定义构建。  
- 🤖 **AI 辅助**：实验显示 AI 可帮助复现复杂构建流程，减少人工干预。  
- 🛡️ **安全检测**：识别未提交源码、构建环境篡改和隐蔽后门等攻击，如 solana/webjs 和 xz-utils 事件。  
- 🏢 **企业价值**：增强元数据、完善 SBOM、加速漏洞响应，无需迁移现有注册表。  
- 👩💻 **维护者价值**：独立验证构建完整性，支持历史包补证，降低 CI 环境安全负担。  
- 📥 **使用方式**：提供 Go 命令行工具，支持查询证明、列出重建包或自行重建。  
- 🤝 **社区参与**：邀请开发者、企业和安全研究者通过 GitHub 贡献代码或反馈，共同提升开源安全。  

（注：原文中非核心的标签、归档等辅助信息已省略，聚焦项目技术内容和价值。）

---

### [庆祝 MDN 二十周年 | MDN 博客](https://developer.mozilla.org/en-US/blog/mdn-turns-20/)

**原文标题**: [Celebrating 20 years of MDN | MDN Blog](https://developer.mozilla.org/en-US/blog/mdn-turns-20/)

MDN（Mozilla Developer Network）庆祝成立 20 周年，回顾其作为开发者社区重要资源的发展历程，并感谢全球贡献者的支持。

- 🎂 **MDN 成立 20 周年**：本月庆祝 MDN 作为开发者资源平台的 20 年历程，从社区驱动的 wiki 发展为全面、可信的开发者文档库。  
- 🌐 **开放网络生态**：MDN 伴随网络平台成熟，提供近 14,000 页文档、33,000 篇本地化文章及 18,000 项功能兼容性数据，支持开发者构建更好的网络体验。  
- 🍰 **浏览器界的蛋糕传统**：延续浏览器厂商互赠蛋糕庆祝里程碑的传统，MDN 收到 web.dev 团队赠送的生日蛋糕，象征开放协作精神。  
- 💌 **致谢全球社区**：超过 10 万贡献者通过 GitHub 参与 MDN 建设，团队特别感谢每一位成员的激情与直接贡献。  
- 📢 **邀请分享与参与**：鼓励开发者通过 X、Mastodon 或 Bluesky 分享与 MDN 的故事，并加入协作，共同书写 MDN 的未来篇章。  
- 📚 **MDN 历史回顾**：文章提及 MDN 过去 10 年及 15 周年的庆祝活动，凸显其长期影响力。

---

### [三种 HTTP 版本过后，表单仍是一团糟](https://yorickpeterse.com/articles/three-http-versions-later-forms-are-still-a-mess/)

**原文标题**: [Three HTTP versions later, forms are still a mess](https://yorickpeterse.com/articles/three-http-versions-later-forms-are-still-a-mess/)

HTTP 1.1 协议及其表单处理机制的混乱现状，作者在 Inko 标准库中实现 HTTP 1.1 时遇到的挑战和协议设计问题。

- 🧩 HTTP 1.1 协议设计混乱，RFC 文档更像是参考而非规范，导致实现困难。  
- 🤯 协议中存在奇怪的设计选择，如使用十六进制而非十进制表示块传输大小。  
- ⚠️ 响应行中状态码后必须包含空格，即使没有原因字符串，这种细节容易引发错误。  
- 📝 表单处理机制在 HTTP 1.1 中仍未改进，两种编码格式（application/x-www-form-urlencoded 和 multipart/form-data）缺乏明确规范。  
- 🔍 application/x-www-form-urlencoded格式基于URL查询字符串规则，但缺乏统一标准，导致不同实现可能编码方式不同。  
- 📦 multipart/form-data格式复杂，边界分隔符可能冲突，解析效率低，且不支持数组或对象等数据结构。  
- 🚫 两种表单格式均未在 HTTP 规范中强制要求支持，导致服务器实现不一致。  
- 😠 作者对 HTTP 协议多年未改进表单处理机制表示 frustration，建议使用 JSON 等现代格式替代。  
- 🔄 提到 W3C 曾提案使用 JSON 处理表单，但未获推进，现有替代方案（如 tus 协议）适用范围有限。

---

