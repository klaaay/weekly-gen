### [JavaScript 周刊第 778 期：2026 年 3 月 24 日](https://javascriptweekly.com/issues/778)

**原文标题**: [JavaScript Weekly Issue 778: March 24, 2026](https://javascriptweekly.com/issues/778)

JavaScript Weekly 第 778 期（2026 年 3 月 24 日）概述了 JavaScript 生态系统的最新动态，包括 TypeScript 6.0 的发布、Node.js 社区对 AI 生成代码的讨论、多个框架和工具的更新，以及性能优化和开发实践的相关文章。

- 🚀 TypeScript 6.0 发布，为 7.0 版本做准备，引入严格模式默认开启等多项变更和弃用。
- 🤖 Node.js 社区就 AI 生成代码的贡献展开辩论，部分开发者发起请愿反对。
- 📉 Deno 公司多名员工离职，但项目仍将继续运营。
- ⚡ Next.js 16.2 提升开发启动速度和渲染性能约 50%。
- 📦 pnpm 11 Beta 0 预览版发布，改用 SQLite 存储并增强构建安全性。
- 🛠️ 文章探讨 JavaScript 臃肿的三大原因及解决方案。
- 🔄 案例显示 TypeScript 重写 Rust/WASM 解析器后性能提升 2-4 倍。
- 📊 React SSR 框架性能对比测试推动 TanStack 和 React 的优化补丁。
- 🐛 Wallaby 团队推出比断点调试快 15 倍的时间旅行 JavaScript 调试工具。
- 📰 其他新闻包括 VS Code 团队利用 AI 加速发布、Secretlint 检查代码秘密泄露等。

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

TypeScript 6.0 正式发布，这是一个重要的过渡版本，旨在为基于 Go 重写的原生编译器 TypeScript 7.0 铺平道路。此版本包含多项新特性、改进以及为迎接 7.0 而做的对齐调整，同时也引入了一些重大的默认值变更和弃用项。

- 🚀 **发布与定位**：TypeScript 6.0 现已可用，它是基于当前代码库的最后一个主要版本，充当 5.9 和未来的原生版本 7.0 之间的桥梁。
- 🧠 **类型推断优化**：对于未使用 `this` 的函数，减少了其上下文敏感性，从而在方法语法等场景中改善了泛型参数的类型推断。
- 📁 **子路径导入支持**：现在支持 Node.js 中以前导 `#/` 开头的子路径导入（如 `#/*`），需在 `--moduleResolution` 设为 `nodenext` 或 `bundler` 时使用。
- ⚙️ **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **稳定的类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，有助于减少版本间差异的噪音，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的选项，包含了新的内置 API 类型（如 `RegExp.escape`）并将一些声明从 `esnext` 移入。
- ⏳ **Temporal API 类型**：为已达到 Stage 4 的 Temporal API 提供了内置类型支持，可通过 `--target esnext` 或 `"lib": ["esnext"]` 使用。
- 🗺️ **新增 Map 方法类型**：为 `Map` 和 `WeakMap` 新增了 `getOrInsert` 和 `getOrInsertComputed` 方法的类型定义，它们源自已进入 Stage 4 的提案。
- 🛡️ **RegExp.escape**：增加了 `RegExp.escape` 函数的类型，用于转义正则表达式中的特殊字符。
- 🌐 **DOM 库更新**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：此版本包含多项旨在反映现代 JS 生态的默认值变更和弃用，例如 `strict` 默认为 `true`、`module` 默认为 `esnext`、`target` 默认为 `es2025`，并弃用了 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等。建议使用 `"ignoreDeprecations": "6.0"` 暂时忽略警告，但这些选项将在 7.0 中彻底移除。
- 📝 **为 7.0 做准备**：团队鼓励开发者在升级到 6.0 后，着手解决所有弃用警告，并尝试 TypeScript 7.0 的原生预览版，以便顺利过渡。

---

### [TypeScript/src/compiler at main · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/tree/main/src/compiler)

**原文标题**: [TypeScript/src/compiler at main · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/tree/main/src/compiler)

TypeScript 是一个由 Microsoft 开发的开源编程语言，它在 GitHub 上拥有活跃的社区和丰富的编译器源代码结构。

- 🏢 **项目归属** – 由 Microsoft 维护，是一个公开的开源项目
- ⭐ **社区热度** – 在 GitHub 上获得 108k 星标和 13.3k 分支，显示出广泛的关注和使用
- 🔧 **代码结构** – 编译器核心代码位于 `src/compiler/` 目录，包含绑定、检查、解析、发射等多个模块
- 📁 **文件组织** – 目录中包含 `binder.ts`、`checker.ts`、`parser.ts`、`emitter.ts` 等关键文件，覆盖编译流程各阶段
- 🔄 **协作活跃** – 项目有 5k 个议题和 13 个拉取请求，表明持续的开发和社区参与
- 🛡️ **安全状态** – 当前安全警报显示为 0，反映项目在安全方面的稳定性
- 📚 **附加资源** – 提供 Wiki、项目、模型等导航选项，支持开发者深入学习和贡献

---

### [10 倍速 TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

**原文标题**: [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScript 团队宣布正在开发原生版本编译器，旨在大幅提升性能，预计将使构建速度提升 10 倍、编辑器启动更快并降低内存占用，计划于 2025 年中发布预览版，年底实现功能完整的语言服务。

- 🚀 TypeScript 正在开发原生版本，目标是将构建速度提升 10 倍，并显著改善编辑器启动时间和内存使用
- 📅 预计 2025 年中发布支持命令行类型检查的预览版，年底提供完整的项目构建和语言服务
- ⚡ 实测显示，在 VS Code、Playwright 等大型代码库上，类型检查速度提升达 9-13 倍
- 💻 编辑器加载项目时间可缩短 8 倍，语言服务操作（如代码补全、跳转定义）响应速度也将大幅提升
- 🔄 将迁移至语言服务器协议（LSP），更好地与其他语言工具集成
- 🏗️ 当前 JavaScript 代码库将继续开发至 6.x 系列，原生版本将作为 TypeScript 7.0 发布
- 📚 团队将在 GitHub 提供进展更新，并邀请社区参与讨论和测试

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#simple-default-changes)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#simple-default-changes)

TypeScript 6.0 作为 TypeScript 5.9 与即将到来的基于 Go 原生重写的 TypeScript 7.0 之间的桥梁版本正式发布。此版本主要旨在为 7.0 的采用进行对齐和准备，同时也引入了一些新特性和改进，包括对无 `this` 使用函数的上下文敏感性优化、支持以 `#/` 开头的子路径导入、新增 `--stableTypeOrdering` 标志以匹配 7.0 的类型排序行为，以及为 `es2025`、`Temporal` API、`Map` 的 `getOrInsert` 方法和 `RegExp.escape` 等新增类型支持。此外，6.0 也包含多项重大的默认值变更和功能弃用，例如默认启用严格模式、`module` 默认改为 `esnext`、`types` 默认改为空数组，并弃用了 `target: es5`、`--moduleResolution node`、`--baseUrl` 等选项，以更好地反映现代 JavaScript 生态。

- 🚀 **发布与定位**：TypeScript 6.0 正式发布，它是当前基于 JavaScript 的代码库的最后一个主要版本，旨在为基于 Go 重写的 TypeScript 7.0 铺平道路。
- 🔧 **上下文敏感性优化**：对于未使用 `this` 的函数，TypeScript 6.0 在类型推断时不再将其视为上下文敏感函数，从而解决了某些方法语法中参数类型推断失败的问题。
- 📁 **子路径导入支持**：现在支持 Node.js 中以 `#/` 开头的子路径导入（例如 `#/*`），需在 `--moduleResolution` 设置为 `nodenext` 或 `bundler` 时使用。
- ⚙️ **新的编译器标志**：新增 `--stableTypeOrdering` 标志，使 TypeScript 6.0 的类型排序行为与 7.0 保持一致，有助于减少版本间差异，但可能会带来性能开销。
- 🎯 **新的编译目标与库**：新增 `es2025` 作为 `target` 和 `lib` 的选项，并引入了对 `Temporal` API、`Map` 的 `getOrInsert`/`getOrInsertComputed` 方法以及 `RegExp.escape` 的静态类型支持。
- 🌐 **DOM 库更新**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：多项默认值发生变更（如 `strict` 默认为 `true`，`types` 默认为 `[]`），并弃用了 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等大量旧选项和语法，以推动生态现代化。
- 🛠️ **为 7.0 做准备**：TypeScript 6.0 是一个过渡版本，团队鼓励开发者在解决 6.0 中的弃用警告后，尝试 TypeScript 7.0 的原生预览版。

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#deprecated:-amd-umd-and-systemjs-values-of-module)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#deprecated:-amd-umd-and-systemjs-values-of-module)

TypeScript 6.0 作为连接 5.9 与未来 7.0 的过渡版本正式发布，它主要旨在为基于 Go 重写的原生编译器 TypeScript 7.0 做准备。此版本引入了多项新特性、改进以及重要的破坏性变更和弃用，以更好地适应现代 JavaScript 开发环境。

- 🚀 **版本定位**：TypeScript 6.0 是当前 JavaScript 代码库的最后一个主要版本，作为迈向基于 Go 的原生编译器 TypeScript 7.0 的桥梁。
- 🛠️ **安装与尝试**：可通过 `npm install -D typescript` 安装，并鼓励开发者尝试 TypeScript 7.0 的原生预览版。
- 🔧 **类型推断改进**：对于未使用 `this` 的函数，减少了其上下文敏感性，从而在方法语法中实现了更好的类型推断。
- 📁 **子路径导入支持**：现在支持以 `#/` 开头的子路径导入（Subpath Imports），与 Node.js 20+ 及 bundler 行为对齐。
- ⚙️ **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **稳定的类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，便于迁移对比，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的新选项，并引入了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 4 的 Temporal API 提供了内置类型支持。
- 🗺️ **新的 Map 方法**：为 `Map` 和 `WeakMap` 新增了 `getOrInsert` 和 `getOrInsertComputed` 方法类型。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数类型，用于正则表达式字符转义。
- 🌐 **DOM 库更新**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **破坏性变更与弃用**：包含多项默认值变更（如 `strict: true`、`module: esnext`）和功能弃用（如 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等），旨在优化性能并反映现代开发实践。建议使用 `"ignoreDeprecations": "6.0"` 暂时忽略警告，但这些选项将在 7.0 中彻底移除。
- 📝 **配置调整**：许多项目需要显式设置 `"types"` 数组（如 `["node"]`）和 `"rootDir"` 来适应新的默认行为。
- 🚫 **命令行行为变更**：在存在 `tsconfig.json` 的目录中通过命令行指定文件进行编译现在会报错，可使用 `--ignoreConfig` 标志跳过。
- 🔮 **未来展望**：团队将专注于 TypeScript 7.0 的稳定发布，鼓励用户提供反馈。TypeScript 6.0 本身也包含可直接使用的改进和新功能。

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#deprecated:---baseurl)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#deprecated:---baseurl)

TypeScript 6.0 正式发布，这是一个独特的过渡版本，旨在为基于 Go 重写的原生 TypeScript 7.0 铺平道路。此版本包含多项新特性、改进以及为迎接 7.0 而做的重大变更和弃用。

- 🚀 **发布与定位**：TypeScript 6.0 现已可用，它是基于当前 JavaScript 代码库的最后一个主要版本，作为 5.9 与未来原生版本 7.0 之间的桥梁。
- 🧠 **类型推断优化**：对于未使用 `this` 的函数，减少了其上下文敏感性，从而在泛型调用中实现了更佳的类型推断。
- 📁 **子路径导入支持**：现在支持以 `#/` 开头的子路径导入（如 `#/*`），与 Node.js 20+ 及 bundler 行为对齐。
- ⚙️ **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **稳定的类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，便于迁移对比，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 选项作为 `target` 和 `lib` 的新值，并引入了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 4 的 Temporal API 提供了内置类型支持，可通过 `esnext` 或 `esnext.temporal` 使用。
- 🗺️ **新增 Map 方法类型**：为 `Map` 和 `WeakMap` 新增了 `getOrInsert` 和 `getOrInsertComputed` 方法类型，简化了“检查 - 插入”模式。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数类型，用于安全地转义正则表达式中的特殊字符。
- 🌐 **DOM 库整合**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：多项默认值更改（如 `strict: true`、`module: esnext`）和功能被弃用（如 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等），旨在反映现代开发生态并提升性能，为 7.0 做准备。
- 🚫 **配置加载行为变更**：当目录中存在 `tsconfig.json` 时，在命令行中指定文件进行编译现在会报错，需使用 `--ignoreConfig` 标志来忽略配置。

---

### [JavaScript 电子表格库 | JS Excel 函数与公式 | SpreadJS](https://developer.mescius.com/spreadjs?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=SpreadJS-JS-Weekly-Primary-Sponsor-March-2026)

**原文标题**: [JavaScript Spreadsheet Library | JS Excel Functions and Formulas | SpreadJS](https://developer.mescius.com/spreadjs?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=SpreadJS-JS-Weekly-Primary-Sponsor-March-2026)

SpreadJS 是一款领先的 JavaScript 电子表格组件，提供类似 Excel 的完整功能体验，支持超过 500 种函数，无需依赖 Excel 即可实现高性能计算、数据导入导出及丰富的可视化功能，适用于金融、工程、医疗等多种业务应用场景。

- 📊 **类似 Excel 的完整体验** – 提供工作表、行列标题、状态栏、图表、表格、形状、条件格式等全面功能，支持无缝导入导出 Excel 文件。
- 🚀 **高性能计算引擎** – 内置 500 多种函数，支持动态数组、自定义函数和大数据计算，可快速处理复杂计算模型。
- 🔒 **全面的文档控制** – 通过 API 精确控制单元格、行列、公式的访问和编辑权限，确保数据安全与合规性。
- 🎨 **无代码设计工具** – 提供桌面设计器和设计器功能区组件，支持用户无需编码即可创建和自定义电子表格模板。
- 📈 **丰富的数据可视化** – 支持 30 多种图表类型、迷你图、条件格式、切片器等，帮助用户直观分析数据。
- 🔄 **灵活的导入导出** – 支持 Excel（.xlsx、.xlsm、.xltm）、CSV、PDF、HTML 及专有.sjs 格式，保持数据与格式完整。
- 🤖 **智能 AI 助手** – 通过自然语言生成公式、解释逻辑、分析数据，并支持智能数据透视表布局生成。
- 👥 **实时协作服务器** – 支持多用户同时编辑，基于 OT 框架同步更改，提供用户状态跟踪和权限管理。
- 📂 **高级数据管理** – 集成 Data Manager 和 TableSheet，支持连接远程数据源（如 REST、OData）和本地数据，实现高效数据绑定与分析。
- 🛠️ **可扩展的附加组件** – 提供数据透视表、甘特图、报表设计、数据图表等可选模块，满足多样化业务需求。

---

### [GitHub - indutny/no-ai-in-nodejs-core: 关于禁止在 Node.js 核心中接受 LLM 生成的 Pull Requests 的请愿 · GitHub](https://github.com/indutny/no-ai-in-nodejs-core)

**原文标题**: [GitHub - indutny/no-ai-in-nodejs-core: A petition to disallow acceptance of LLM generated Pull Requests in Node.js core · GitHub](https://github.com/indutny/no-ai-in-nodejs-core)

该请愿书呼吁 Node.js 技术指导委员会（TSC）拒绝在 Node.js 核心代码中接受 AI 生成的代码，强调此举可能损害项目的可靠性、伦理基础和教育价值。

- 🚫 **反对 AI 代码**：请愿者要求 Node.js TSC 投票反对“是否允许 AI 辅助开发”，并拒绝接受 LLM 生成的核心代码重写。
- ⚠️ **核心风险**：Node.js 作为关键基础设施，其核心代码经过多年精心编写，引入 AI 生成代码可能破坏项目声誉和贡献者信任。
- 📜 **法律与伦理争议**：尽管 OpenJS 基金会认为 LLM 辅助代码不违反开发者来源证书（DCO），但请愿指出 AI 训练数据可能涉及版权和伦理问题。
- 🎓 **教育影响**：使用 LLM 可能阻碍学习过程，降低代码审查的教育意义，影响新贡献者的成长和项目长期健康。
- 💰 **特权门槛**：LLM 工具通常需要付费订阅或昂贵硬件，这可能造成贡献和审查过程中的不平等。
- ✍️ **社区签名**：请愿通过 GitHub 提交、Issue 或 change.org 收集签名，已获得包括 Node.js 前 TSC 成员在内的数十位开发者支持。

---

### [Deno，下一代 JavaScript 运行时](https://deno.com/)

**原文标题**: [Deno, the next-generation JavaScript runtime](https://deno.com/)

Deno 是一个开源的现代 JavaScript 运行时，基于 Web 标准构建，内置 TypeScript 支持、强大的安全性和完整的工具链，旨在简化 JavaScript 开发。

- 🚀 **现代 JavaScript 运行时**：Deno 基于 Web 标准构建，提供零配置的 TypeScript 支持、内置工具链和无与伦比的安全性。
- 🔧 **内置完整工具链**：包含代码检查器、测试运行器、代码格式化器和独立可执行文件生成器，无需额外配置。
- 🛡️ **默认安全**：默认情况下，Deno 程序无法访问文件系统、网络或环境变量，需显式授权，有效防止供应链攻击。
- 🌐 **兼容 Node.js 和 npm**：支持直接导入 npm 包或使用 package.json，无缝迁移现有项目。
- ⚡ **高性能网络**：原生支持 HTTPS、WebSocket、HTTP/2 和自动响应压缩，性能优于 Node.js。
- ☁️ **云端部署优化**：提供官方 Docker 镜像，支持 Deno Deploy 等云平台，简化部署流程。
- 🏝️ **Fresh 框架集成**：内置 Fresh 2.0 框架，采用岛屿架构，实现最小化 JavaScript 运行时开销。
- 👥 **活跃社区生态**：拥有超过 40 万活跃用户和 200 万社区模块，获得广泛开发者好评。

---

### [@marvinh.dev 在 Bluesky](https://bsky.app/profile/marvinh.dev/post/3mhbtbl2ptk23)

**原文标题**: [@marvinh.dev on Bluesky](https://bsky.app/profile/marvinh.dev/post/3mhbtbl2ptk23)

Marvin Hagemeister 宣布从 Deno 离职，目前正在寻找新工作机会。

- 🚀 昨天是他在 Deno 的最后一天，他称赞团队中聚集了许多高技能同事
- 👋 虽然离开，但他会继续为 Deno 团队加油助威
- 🔍 目前尚未确定下一步计划，正在正式寻找新工作

---

### [@collinsworth.dev 在 Bluesky](https://bsky.app/profile/collinsworth.dev/post/3mhdpgmoao22j)

**原文标题**: [@collinsworth.dev on Bluesky](https://bsky.app/profile/collinsworth.dev/post/3mhdpgmoao22j)

Deno 公司因商业现实困难进行裁员，但 Deno 项目本身将继续运营和发展。

- 🚀 Deno 是一个高度交互的 Web 应用，需要 JavaScript 支持
- 🔗 了解更多信息可访问 bsky.social 和 atproto.com
- 📝 作者 Josh Collinsworth 澄清裁员源于严峻的商业现实，而非项目问题
- 💪 强调 Deno 项目不会消失，目前只是面临困难时期
- 🗓️ 相关信息发布于 2026 年 3 月 18 日

---

### [《chibivue 入门指南》](https://book.chibivue.land/)

**原文标题**: [The chibivue Book](https://book.chibivue.land/)

从响应式系统的基本原理出发，涵盖从 EffectScope 到 CustomRef 等高级 API 的广泛实现。

- 🧠 讲解响应式系统的基本原理
- 🔄 涵盖 EffectScope 等核心实现
- ⚙️ 深入高级 API 如 CustomRef
- 📚 系统化学习从基础到进阶的内容

---

### [Next.js 16.2 | Next.js](https://nextjs.org/blog/next-16-2)

**原文标题**: [Next.js 16.2 | Next.js](https://nextjs.org/blog/next-16-2)

Next.js 16.2 版本带来了显著的性能提升、调试优化、对 AI 代理的改进以及超过 200 项 Turbopack 修复与增强。

- 🚀 开发启动速度提升约 400%，渲染性能提高约 50%
- 🐛 新增默认错误页面设计，优化开发终端中的服务器函数执行日志
- 🔍 增强水合差异指示器，支持生产服务器调试（--inspect）
- ⚙️ 引入 transitionTypes 属性优化链接导航，提升 ImageResponse 生成速度
- 🛠️ 适配器功能稳定化，支持多格式图标自动处理
- 🧪 新增实验性功能：unstable_catchError 错误边界、unstable_retry 重试机制、预取内联优化等
- 📈 包含 Turbopack 构建加速和 AI 开发工具链改进专项优化

---

### [发布 v10.3.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v10.3.0)

**原文标题**: [Release v10.3.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v10.3.0)

Storybook 10.3 版本发布，带来数百项修复与改进，重点提升开发者体验、AI 辅助工具及生态系统支持。

- 🤖 推出 Storybook MCP 预览版，支持 React 的智能组件开发、文档与测试
- ⚡ 新增 Vite 8 支持，优化构建性能
- ▲ 兼容 Next.js 16.2，提升框架集成度
- 📝 支持 ESLint 10，增强代码规范检查
- 〰️ Addon Pseudo-States 插件现支持 Tailwind v4
- 🔧 Addon-Vitest 配置简化，无需额外设置文件
- ♿ 全面优化 UI 可访问性，包括滚动区域、弹窗标签等多项改进
- 🛠️ 修复多项核心问题，如热更新竞争条件、CORS 中间件注册等
- 📦 更新多项目依赖，包括 Angular 模块解析优化、Vite 插件集中管理等
- 👥 由 remino、ghengeveld 等 28 位贡献者共同完成

---

### [Node.js — 2026 年 3 月 24 日星期二安全更新发布](https://nodejs.org/en/blog/vulnerability/march-2026-security-releases)

**原文标题**: [Node.js — Tuesday, March 24, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/march-2026-security-releases)

Node.js 项目于 2026 年 3 月 24 日发布了针对多个版本的安全更新，修复了包括高、中、低严重性在内的多个安全漏洞，涉及 TLS、HTTP、权限模型、URL 处理、加密等多个核心模块。

- 🛡️ **TLS 漏洞修复**：修复了`SNICallback`中未受保护的同步异常问题，该问题可导致远程拒绝服务（CVE-2026-21637，高危）。
- 🚨 **HTTP 头部处理漏洞**：修复了当请求头名为`__proto__`时，访问`req.headersDistinct`会导致未捕获的`TypeError`并崩溃的问题（CVE-2026-21710，高危）。
- 🔓 **权限模型绕过**：修复了 Unix 域套接字服务器在未启用`--allow-net`时仍可绑定/监听的问题（CVE-2026-21711，中危）。
- 💥 **URL 解析崩溃**：修复了`url.format()`处理畸形国际化域名时导致断言失败并崩溃的问题（CVE-2026-21712，中危）。
- ⏱️ **加密时序侧信道**：修复了 HMAC 验证中使用非恒定时间比较，可能导致签名伪造的问题（CVE-2026-21713，中危）。
- 🧠 **HTTP/2内存泄漏**：修复了客户端在流 0 上发送`WINDOW_UPDATE`帧导致流控制窗口溢出时，`Http2Session`对象未被清理的内存泄漏问题（CVE-2026-21714，中危）。
- 🐌 **V8 哈希碰撞攻击**：修复了 V8 中字符串哈希机制导致整数类字符串哈希值可预测，可能引发哈希碰撞拒绝服务攻击的问题（CVE-2026-21717，中危）。
- 📁 **文件系统权限绕过**：修复了`fs.realpathSync.native()`未执行读取权限检查，可能泄露文件存在信息的问题（CVE-2026-21715，低危）。
- ⚠️ **权限补丁不完整**：修复了`FileHandle.chmod()`和`FileHandle.chown()`的 Promise API 版本未正确应用权限检查的问题（CVE-2026-21716，低危）。

---

### [发布 v2.7.6 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.7.6)

**原文标题**: [Release v2.7.6 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.7.6)

Deno 2.7.6 版本发布，包含多项新功能、错误修复和性能优化，旨在提升运行时稳定性、Node.js 兼容性及开发体验。

- 🆕 **新增功能**：引入可克隆资源注册表、支持 Windows 额外信号、自动检测 CJS/ESM 模块，并新增生成交互式 CPU 性能火焰图选项。
- 🐛 **错误修复**：解决了核心崩溃、模块加载、Node.js 兼容性、网络连接、加密及进程管理等方面的多个问题，增强了系统稳定性。
- ⚡ **性能优化**：优化了字符串转换、文件操作、缓冲区处理及生命周期脚本执行等关键路径，提升了整体运行效率。
- 🔧 **工具改进**：完善了 LSP、测试覆盖、环境文件处理及事件循环唤醒机制，改善了开发者工具链的体验。
- 📦 **生态系统**：增强了 npm 包管理、Telemetry 集成及 Web API 支持，进一步巩固了 Deno 的现代 JavaScript/TypeScript 运行时地位。

---

### [Bun v1.3.11 | Bun 博客](https://bun.com/blog/bun-v1.3.11)

**原文标题**: [Bun v1.3.11 | Bun Blog](https://bun.com/blog/bun-v1.3.11)

本文介绍了 Bun 的最新更新，包括安装与升级方法、新增的 `Bun.cron` API、`Bun.sliceAnsi` 工具、Markdown 渲染增强、测试路径忽略功能、多项错误修复及性能改进。

- 🚀 **安装与升级**：支持多种安装方式（curl、npm、PowerShell、scoop、brew、Docker），并通过 `bun upgrade` 轻松升级。
- 📅 **内置 Cron 作业**：新增 `Bun.cron` API，支持跨平台注册、解析和移除系统级定时任务，兼容 Cloudflare Workers API。
- ✂️ **ANSI 字符串切片**：`Bun.sliceAnsi` 提供终端列宽切片，保留 ANSI 转义码并正确处理字形簇（如表情符号）。
- 📝 **Markdown 渲染增强**：`Bun.markdown.render()` 为列表项回调提供更多元数据（如索引、深度、有序性），便于自定义列表标记。
- 🚫 **测试路径忽略**：`bun test` 新增 `--path-ignore-patterns` 标志，支持通过 glob 模式排除文件或目录。
- 🐛 **错误修复**：修复了 macOS 上的 UDP 套接字问题、Windows ARM64 原生 shim、Node.js 兼容性问题、Bun API 及 Web API 中的多项缺陷。
- 🔧 **性能与优化**：Bun 在 Linux x64 上体积减小 4MB，改进了 `Bun.Transpiler` 的内存管理，并修复了打包器和 CSS 解析器的相关问题。
- 🙏 **致谢贡献者**：感谢 15 位贡献者的代码提交与问题报告。

---

### [Valibot v1.3：更智能的管道、结果缓存与新验证器 | Valibot](https://valibot.dev/blog/valibot-v1.3-release-notes/)

**原文标题**: [Valibot v1.3: Smarter pipelines, result caching, and new validators | Valibot](https://valibot.dev/blog/valibot-v1.3-release-notes/)

Valibot v1.3 版本引入了更智能的管道工具、结果缓存机制和新的验证器，提升了数据验证和处理的效率与灵活性。

- 🛠️ 新增 `guard` 和 `parseBoolean` 管道工具，支持类型细化和布尔值解析，简化数据转换流程
- 💾 引入 `cache` 和 `cacheAsync` API，通过缓存验证结果减少重复计算，优化性能
- 🔍 添加 `domain`、`jwsCompact` 和 `isrc` 验证器，扩展了对域名、JWS 令牌和音乐编码的验证支持
- 🔧 修复了 `creditCard`、`isoTimestamp` 的兼容性问题，并改进了对深层只读默认值的处理
- 🤝 感谢社区贡献者的支持，版本持续优化集成体验和开发者工作流

---

### [ESLint v10.1.0 版本发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/03/eslint-v10.1.0-released/)

**原文标题**: [ESLint v10.1.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/03/eslint-v10.1.0-released/)

ESLint v10.1.0 是一个次要版本更新，引入了 API 对批量抑制功能的支持，并包含多项功能增强、错误修复、文档更新及维护任务。

- 🚀 新增 API 支持批量抑制功能，允许通过 `applySuppressions: true` 选项在 Node.js API 中自动应用抑制规则
- 🔧 功能改进：修复了 `no-var` 规则在 `TSModuleBlock` 中的自动修复问题
- 🐛 错误修复：防止 `no-var` 在变量声明前使用时进行自动修复，并更新了 ESLint 内部依赖
- 📚 文档更新：修正了 `require-jsdoc` 的 JSDoc 链接，添加了弃用通知，更新了迁移指南和 AI 使用政策
- 🛠️ 维护与测试：更新了多个依赖包版本，修复了 CLI 和 `RuleTester` 的测试问题，并调整了 CI 配置

---

### [JavaScript 臃肿的三大支柱](https://43081j.com/2026/03/three-pillars-of-javascript-bloat)

**原文标题**: [The Three Pillars of JavaScript Bloat](https://43081j.com/2026/03/three-pillars-of-javascript-bloat)

JavaScript 依赖臃肿的三大根源：对旧运行环境的兼容、原子化架构设计以及过时的 Ponyfill 使用，导致大多数开发者被迫承担不必要的性能与安全成本。社区正通过清理冗余包、推广原生替代方案等举措逐步优化。

- 🧩 **对旧运行环境的兼容**：为支持 ES3 等老旧引擎、防止全局命名空间污染及跨 Realm 值传递，许多工具包被引入，但绝大多数现代项目已无需这些兼容层。
- 🧱 **原子化架构**：将代码拆分为极细粒度的包（如 `arrify`、`is-wsl`），本意是提高复用性，却导致大量单用途包和版本重复，增加了依赖树的复杂性和供应链风险。
- 🦄 **过时的 Ponyfill**：这些原本为库函数提供的非污染性填充方案，在功能已被原生广泛支持后仍被保留（如 `object.entries`），造成不必要的依赖累积。
- 🛠️ **解决方案**：开发者可通过工具（如 `knip`、`e18e CLI`、`npmgraph`）检测并移除无用依赖，查阅 `module-replacements` 项目寻找原生替代，并向维护者反馈以推动清理。

---

### [GitHub - sindresorhus/ponyfill：🦄 如同 polyfill，但具备 pony 的纯粹性 · GitHub](https://github.com/sindresorhus/ponyfill)

**原文标题**: [GitHub - sindresorhus/ponyfill: 🦄 Like polyfill but with pony pureness · GitHub](https://github.com/sindresorhus/ponyfill)

Ponyfill 是一种不修改全局环境的标准化功能实现方式，与 polyfill 不同，它通过显式导入提供功能，避免副作用和全局污染。

- 🦄 Ponyfill 通过模块导出功能，不修改全局 API，保持代码纯净和可预测性。
- 🐒 Polyfill 通过猴子补丁修改全局环境，可能导致兼容性问题和不一致行为。
- ⚖️ Ponyfill 适用于可控代码，而 polyfill 可能在依赖链不支持某功能时成为唯一选择。
- 📦 创建 Ponyfill 需遵循规范实现，避免依赖原生 API，并发布为独立模块。
- 🔍 可通过 npm 搜索 Ponyfill 资源，相关讨论和定义可在技术社区中找到。

---

### [e18e | 生态系统性能](https://e18e.dev/)

**原文标题**: [e18e | Ecosystem Performance](https://e18e.dev/)

代码库优化与依赖项精简，提升项目维护性与性能。

- 🧹 清理冗余依赖项，移除不再使用的库
- 🔄 替换过时组件，采用现代技术方案
- ⚡ 优化项目结构，提升运行效率
- 📦 精简依赖关系，降低维护复杂度
- 🛠️ 确保兼容性，保持系统稳定运行

---

### [用 TypeScript 重写我们的 Rust WASM 解析器 | OpenUI](https://www.openui.com/blog/rust-wasm-parser)

**原文标题**: [Rewriting our Rust WASM Parser in TypeScript | OpenUI](https://www.openui.com/blog/rust-wasm-parser)

本文介绍了将 Rust WASM 解析器重写为 TypeScript 后性能提升 3 倍的经历，核心在于发现 WASM 边界开销和算法复杂度是性能瓶颈，而非解析计算本身。

- 🚀 将 Rust WASM 解析器移植到 TypeScript 后，单次解析速度提升 2.2-4.6 倍，流式解析总开销降低 2.6-3.3 倍
- 🧱 WASM 边界开销是主要瓶颈：每次调用需复制字符串、序列化为 JSON、再反序列化，解析计算本身反而很快
- ⚠️ 尝试用 serde-wasm-bindgen 直接返回 JS 对象反而更慢：因为需要大量细粒度的运行时边界转换
- 🔄 流式解析存在 O(N²) 算法问题：每次收到新块都重新解析整个累积字符串
- 💡 解决方案：语句级增量缓存——只重新解析未完成的语句，已完成语句的 AST 被缓存复用
- 📊 性能对比：TypeScript 增量解析在 contact-form 上单次 13.4µs，流式总开销 122µs；而 WASM 单次 61.4µs
- ✅ WASM 适用场景：计算密集型且交互少（如图像处理、加密）、移植原生库
- ❌ WASM 不适用场景：解析结构化文本为 JS 对象、小输入高频调用的函数
- 🎯 关键启示：性能分析应先于语言选择；算法优化比语言级优化影响更大；WASM 与 JS 堆不共享，转换总有成本

---

### [Chrome 扩展 JavaScript SDK 支持](https://clerk.com/changelog/2026-03-04-chrome-extension-js-quickstart?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=chrome-ext&utm_content=03-24-26)

**原文标题**: [Chrome Extension JavaScript SDK support](https://clerk.com/changelog/2026-03-04-chrome-extension-js-quickstart?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=chrome-ext&utm_content=03-24-26)

Chrome Extension SDK 现已通过 createClerkClient() 支持原生 JavaScript，并弃用了 /background 导入路径，为 React 和非 React 项目提供了统一的初始化方式。

- 🚀 Chrome Extension SDK 新增对原生 JavaScript 的支持，可通过 createClerkClient() 函数实现
- 📚 发布了新的 Chrome Extension JS 快速入门指南，帮助开发者快速上手
- 🔧 使用 createClerkClient() 从 @clerk/chrome-extension/client 导入，可在弹出窗口或侧面板中初始化 Clerk
- ⚙️ createClerkClient() 新增 background: true 选项，用于后台服务工作线程，替代原有的独立导入路径
- ⚠️ 已弃用 @clerk/chrome-extension/background 导入路径，建议统一使用 @clerk/chrome-extension/client

---

### [获取失败](https://javascriptweekly.com/link/182678/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/182678/web)

无法总结：获取内容失败，状态码 429。

---

### [开发者不喜却无法回避的两个 React 设计选择 - DEV 社区](https://dev.to/playfulprogramming/two-react-design-choices-developers-dont-like-but-cant-avoid-d6g)

**原文标题**: [Two React Design Choices Developers Don’t Like—But Can’t Avoid - DEV Community](https://dev.to/playfulprogramming/two-react-design-choices-developers-dont-like-but-cant-avoid-d6g)

React 早期备受争议的两个设计选择——状态提交的延迟与 Effect 依赖数组——并非随意决定，而是反映了异步环境下 UI 框架必须面对的根本约束。作者通过开发 Solid 2.0 的经验指出，异步操作迫使任何系统都必须隔离状态提交、预先知晓 Effect 的依赖关系，并保持一致性快照。这些并非 React 独有的问题，而是所有处理异步的 UI 框架都无法回避的“物理定律”。接纳这些约束并不意味着放弃 Signals 的细粒度更新优势，而是让框架在异步世界中既保持高效又确保正确性。

- 🕐 **异步操作要求状态提交必须被隔离**：在异步值未就绪时，如果立即提交状态更新，会导致 UI 显示与底层数据不一致，用户可能与非实时的界面进行交互。因此，框架必须延迟提交，直到所有相关异步派生值都已确定。
- 📋 **Effect 的依赖必须在执行前就已知**：在异步可中断的渲染过程中，如果副作用在依赖未完全确定前执行，可能会基于部分或推测状态运行，导致不可预测的结果。React 的依赖数组虽显笨拙，却确保了依赖的预先收集，这是异步环境下保持确定性的必要条件。
- 🔄 **Signals 并未真正解决异步问题，只是推迟了它**：Signals 在同步更新中通过细粒度响应提供了即时一致性，但一旦异步进入依赖图，这种同步假设就会崩溃。框架必须正面处理异步，而非将其视为特殊情况。
- 🛠 **编译器无法完全解决异步带来的语义问题**：依赖的静态提取无法覆盖运行时动态行为，尤其是当异步源通过函数调用隐藏时。异步是运行时现象，必须在运行时层面保证一致性。
- 🌐 **这些约束不是 React 的独创，而是 UI 框架的通用定律**：Vue 的观察者机制也体现了类似的副作用分离。接纳这些约束是框架成熟的标志，让异步成为架构中的一等公民，而非边缘情况。

---

### [JavaScript 视万物皆为日期](https://futuresearch.ai/blog/javascript-thinks-everythings-a-date/)

**原文标题**: [JavaScript Thinks Everything's a Date](https://futuresearch.ai/blog/javascript-thinks-everythings-a-date/)

JavaScript 的 Date 构造函数在解析字符串时过于宽松，常将非日期文本错误转换为日期对象，导致难以察觉的代码错误。

- 🧐 JavaScript 的`new Date(string)`会尝试从任意字符串中提取日期，甚至将“Route 66”解析为 1966 年 1 月 1 日
- 📜 根据 ECMAScript 规范，除 ISO 8601 格式外，其他字符串的解析行为由实现定义，V8 和 SpiderMonkey 引擎使用遗留解析器
- ⚠️ 遗留解析器会忽略数字前的非识别单词，将大于 31 的数字视为年份，导致“Beverly Hills, 90210”被解析为公元 90210 年
- 🌍 ISO 解析器使用 UTC 时间，而遗留解析器默认使用本地时间，同一日期字符串可能因格式差异返回不同结果
- 🍎 Safari 的 JavaScriptCore 引擎更严格，会拒绝这些异常解析，而 Chrome 和 Firefox 仍保留宽松行为
- 🐛 这种宽松解析曾导致实际错误，如将街道名称和标识符错误显示为日期格式
- 🐍 Python 采用严格策略，只接受明确格式的日期字符串，遵循“面对歧义时拒绝猜测”的原则
- 🔧 建议仅对可控输入格式使用`new Date(string)`，对用户数据应先验证格式或使用严格解析库如 date-fns

---

### [书签小工具完全指南 | CSS-Tricks](https://css-tricks.com/a-complete-guide-to-bookmarklets/)

**原文标题**: [A Complete Guide to Bookmarklets | CSS-Tricks](https://css-tricks.com/a-complete-guide-to-bookmarklets/)

书签小工具（Bookmarklets）是一种将 JavaScript 代码保存为浏览器书签的技术，允许用户通过点击书签执行脚本，从而增强浏览器的功能。它简单易用，无需安装额外软件，适合快速执行小型任务，如修改页面样式或调试网页。

- 🔧 书签小工具是将 JavaScript 代码保存为书签的工具，通过点击执行脚本，扩展浏览器功能
- 📜 创建书签小工具需将代码封装为 IIFE，使用`javascript:`前缀，并进行 URL 编码以确保兼容性
- 🌐 安装方法因浏览器而异，通常通过编辑书签或拖放链接到书签栏完成
- 🎨 书签小工具可应用 CSS 样式，例如通过创建`<style>`元素或使用`CSSStyleSheet`接口修改页面外观
- ⚠️ 使用书签小工具时需注意内容安全策略（CSP）的限制，且代码应尽量自包含以避免跨域问题
- 🔒 在线获取书签小工具需谨慎，避免恶意代码，浏览器会默认剥离`javascript:`前缀以防误触发
- 📚 社区提供了丰富的书签小工具资源，如测试 CSS、辅助功能审计等，适合开发者探索使用

---

### [如何在 JavaScript 框架上烧掉 3000 万美元... - YouTube](https://www.youtube.com/watch?v=ReAnFFqvCeA)

**原文标题**: [How to burn $30m on a JavaScript framework... - YouTube](https://www.youtube.com/watch?v=ReAnFFqvCeA)

该文本为 YouTube 网站底部的通用信息与链接列表，概述了平台的政策、功能及法律信息。

- 📄 关于平台的基本信息与介绍
- 📢 新闻与媒体相关资源
- ©️ 版权说明与保护
- 📞 联系与合作方式
- 🧑‍🎨 内容创作者相关资源
- 💼 广告与商业合作
- 👨‍💻 开发者工具与资源
- 📜 服务条款与使用协议
- 🔒 隐私政策与数据保护
- ⚙️ 平台政策与安全指南
- 🔧 YouTube 功能运作说明
- 🧪 新功能测试与更新
- 🏢 公司信息与版权年份

---

### [Node.js 工作线程虽存争议，却为我们带来卓越成效 - Inngest 博客](https://www.inngest.com/blog/node-worker-threads)

**原文标题**: [Node.js worker threads are problematic, but they work great for us - Inngest Blog](https://www.inngest.com/blog/node-worker-threads)

Node.js 的 worker 线程虽然存在一些限制，但通过将 Inngest Connect 的核心功能移至 worker 线程，有效解决了主线程因 CPU 密集型任务阻塞导致的心跳中断问题，从而避免了服务器误判 worker 失效的情况。

- 🧵 **单线程限制**：Node.js 的单线程事件循环在 CPU 密集型任务下会阻塞所有其他操作，包括定时器和网络回调，导致关键功能如心跳无法执行。
- ⚙️ **worker 线程隔离**：通过`worker_threads`模块创建独立的 JavaScript 执行环境，每个 worker 拥有自己的 V8 实例和事件循环，防止 CPU 任务影响其他线程。
- 📜 **文件入口限制**：worker 线程必须通过文件路径启动，无法直接传递函数，这要求设计独立的通信协议和消息传递机制。
- 📨 **消息传递通信**：线程间通过`postMessage`进行数据交换，使用结构化克隆算法序列化数据，适用于小型消息，但大型负载会有性能开销。
- 🛠️ **构建工具挑战**：打包工具如 webpack 难以自动检测 worker 文件路径，需要特定语法或显式配置来确保文件被正确包含在构建输出中。
- 💾 **资源开销较高**：每个 worker 线程占用约 10MB 内存，启动成本较高，因此适合长时间运行的任务，而非频繁创建和销毁的短期任务。
- 🔄 **实际应用架构**：Inngest Connect 将 WebSocket 连接和心跳等关键功能移至 worker 线程，主线程处理用户代码，通过消息传递协调，确保连接稳定。
- 🛡️ **容错与恢复**：worker 线程崩溃时，主线程会监控并采用指数退避策略重新启动，避免无限循环重启，提高系统韧性。
- ⚖️ **权衡与收益**：尽管 worker 线程在设计和构建上带来复杂性，但提供了强隔离性，彻底解决了事件循环阻塞导致的服务中断问题。

---

### [发布 pnpm 11 Beta 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-beta.0)

**原文标题**: [Release pnpm 11 Beta 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-beta.0)

pnpm 11 Beta 0 版本发布，带来多项重大变更，包括存储优化、全局包隔离、配置格式调整、移除旧功能及新增命令等。

- 🗃️ 存储系统升级：采用 SQLite 数据库存储包元数据，减少文件系统调用，提升安装速度。
- 🌍 全局包隔离：全局安装的包现在各自独立，避免依赖冲突，并默认使用全局虚拟存储。
- ⚙️ 配置格式变更：配置管理转向 YAML 文件（如 pnpm-workspace.yaml），不再支持 package.json 中的 pnpm 字段。
- 🧹 移除旧功能：弃用 pnpm server 命令、部分构建依赖设置及非标准配置加载方式。
- 🛠️ 新增命令：引入 pnpm sbom（生成软件物料清单）、pnpm clean（清理 node_modules）等实用命令。
- 🔗 链接命令调整：pnpm link 现在仅接受路径参数，不再支持全局链接简化操作。
- 🔒 安全与审计增强：默认启用严格依赖构建检查，新增 pnpm audit --fix=update 以更新锁文件修复漏洞。
- 📦 发布流程独立：pnpm publish 不再依赖 npm CLI，支持直接发布并改进 OTP 认证体验。

---

### [快速、节省磁盘空间的包管理器 | pnpm](https://pnpm.io/)

**原文标题**: [Fast, disk space efficient package manager | pnpm](https://pnpm.io/)

pnpm 是一款高效、安全的 Node.js 包管理器，专注于提升安装速度、节省磁盘空间，并优化 monorepo 管理体验。

- 🚀 安装速度极快，显著减少依赖安装等待时间
- 💾 智能节省磁盘空间，避免重复存储依赖包
- 🏗️ 内置 monorepo 支持，简化多包项目管理
- 🔒 增强安全性，通过最小发布延迟等机制防范供应链攻击
- ⏱️ 用户反馈显示能大幅提升开发与构建效率，部分 CI 流程从 12 分钟缩短至 2 分钟
- 🌟 受到众多知名开源项目如 Next.js、Vue、Vite、Nuxt 等广泛采用
- 🤝 由 Bit Cloud、Sanity、Vitejs 等多家企业赞助支持

---

### [Edge.js：在 WebAssembly 沙箱中运行 Node 应用 · 博客 · Wasmer](https://wasmer.io/posts/edgejs-safe-nodejs-using-wasm-sandbox)

**原文标题**: [Edge.js: Running Node apps inside a WebAssembly Sandbox · Blog · Wasmer](https://wasmer.io/posts/edgejs-safe-nodejs-using-wasm-sandbox)

Edge.js 是一个专为 AI 和边缘计算设计的 JavaScript 运行时，它通过 WebAssembly 沙箱安全地运行 Node.js 应用，实现了与 Node.js 的完全兼容，同时提供了更高的安全性和更快的启动速度。

- 🚀 **完全兼容 Node.js**：Edge.js 保持了与 Node.js v24 的完全兼容，现有应用和原生模块无需修改即可运行。
- 🛡️ **安全沙箱执行**：通过 WebAssembly 和 WASIX 隔离系统调用和原生代码，确保不安全部分被安全沙箱化。
- ⚡ **高性能与高密度**：相比容器，Edge.js 提供了更快的启动时间和更高的应用部署密度，适合边缘计算场景。
- 🔧 **灵活的 JS 引擎支持**：支持 V8、JavascriptCore 或 QuickJS 等多种 JavaScript 引擎，并可插拔使用。
- 📊 **广泛的模块兼容性**：在测试中，Edge.js 在大多数 Node.js 核心模块上表现出比 Bun 和 Deno 更高的测试通过率。
- 🛠️ **基于 NAPI 与 WASIX 的架构**：利用 Node.js 的 NAPI 抽象层和 WASIX 系统调用沙箱，平衡了兼容性、安全性与性能。
- 🚫 **无需 Docker 容器**：Edge.js 允许在无需 Docker 容器的情况下安全运行 JS 应用、MCP 和代理，简化了部署流程。
- 📈 **持续性能优化**：目前性能接近原生 Node.js，团队正致力于进一步缩小性能差距并改善启动时间。
- 🤖 **AI 加速开发**：项目依赖 AI（如 GPT-5.4）大幅缩短开发周期，使小型团队能在几周内完成原本需数年的工作。

---

### [Edge.js - 在任何地方，使用任何 JS 引擎安全运行 Node.js](https://edgejs.org/)

**原文标题**: [Edge.js - Run Node.js safely, anywhere, with any JS engine](https://edgejs.org/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战与伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台通过自动化流程减少行政负担，提升医疗机构运营效率
- ⚠️ 数据隐私保护与算法透明度仍是当前技术落地需要解决的关键问题
- 🔮 未来 AI 或将在预防医学与远程医疗领域发挥更重要的支撑作用

---

### [Wallaby - 集成即时反馈的 AI 就绪测试运行器](https://wallabyjs.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Wallaby - AI-Ready Test Runner with Instant Feedback in Your Editor](https://wallabyjs.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

Wallaby.js 是一款实时 JavaScript/TypeScript 测试运行工具，可在编码时即时显示测试结果和覆盖率，并提供时间旅行调试、AI 集成等功能，显著提升开发效率和测试体验。

- 🚀 **实时测试反馈**：在编辑器中即时显示测试结果和代码覆盖率，无需手动运行测试。
- ⚡ **智能测试执行**：仅运行受代码更改影响的最小测试集，执行速度极快。
- 🤖 **AI 深度集成**：通过 MCP 服务器为 AI 工具提供实时运行时数据，辅助调试和代码生成。
- 🔧 **强大调试功能**：支持时间旅行调试、实时值查看和交互式数据探索，快速定位问题。
- 🛠️ **无锁定设计**：作为现有测试框架和 IDE 的插件，无需担心供应商或框架锁定。
- 📊 **详细测试洞察**：提供测试性能分析、差异对比、快照管理和覆盖率报告等高级功能。
- 💬 **用户高度评价**：被众多开发者和公司誉为提升生产力和测试体验的必备工具。

---

### [ArrowJS —— 面向智能体时代的首个 UI 框架](https://arrow-js.com/)

**原文标题**: [ArrowJS â The first UI framework for the agentic era](https://arrow-js.com/)

ArrowJS 是一个专为智能体时代设计的轻量、快速、零依赖、类型安全的 UI 框架，无需构建步骤，并支持在 WebAssembly 沙箱中安全运行组件逻辑。

- 🚀 **轻量快速**：框架体积小（<5kb），无需构建步骤、JSX 编译或复杂工具链，性能优异。
- 🛡️ **安全沙箱**：通过 WebAssembly 沙箱隔离组件逻辑，支持安全执行 AI 生成的代码，无需 iframe。
- ⚡ **反应式数据**：使用 `reactive()` 创建可观察状态，`html` 模板字面量渲染 DOM，支持动态更新。
- 🧩 **组件化**：通过 `component()` 创建组件，支持本地状态、生命周期管理和异步组件。
- 🔍 **数据监听**：`watch()` 自动追踪依赖，实现模板外的副作用响应。
- 🌐 **路由支持**：提供简单的路由函数，支持 SSR 和 hydration，确保前后端渲染一致。
- 🧪 **丰富示例**：包含待办列表、计时器、颜色调色板等多种交互示例，可直接在 Playground 中编辑运行。
- 🤖 **智能体友好**：提供专门的提示词和 JSON 模式，方便 AI 智能体生成沙箱代码。

---

### [FormKit ⚡️ Vue 的开源表单框架](https://formkit.com/)

**原文标题**: [FormKit ⚡️ The open-source form framework for Vue](https://formkit.com/)

FormKit 是一个开源的表单框架，通过创新的架构设计，极大地简化了表单开发流程，使开发者能够高效构建复杂表单而无需手动处理状态管理。

- 🚀 **简化开发流程**：减少样板代码，提升可访问性，无需手动进行属性传递、事件发射或复杂数据存储
- 🧩 **智能数据建模**：自动创建无限深度的输入连接，支持组件化表单元素，无需手动数据建模
- 📦 **统一组件接口**：使用单一 FormKit 组件处理验证、提交等所有功能，支持通过插槽和属性完全自定义
- 🔗 **无缝数据集成**：自动构建结构化表单数据，支持分组输入和重复器，轻松处理嵌套数据结构
- ⚡ **提升开发体验**：被多个知名团队采用，显著提高表单开发效率，获得开发者社区广泛好评
- 🎯 **专注业务逻辑**：架构设计简洁直观，让开发者专注于表单构建而非状态管理

---

### [糖分飙升](https://sugar-high.vercel.app/)

**原文标题**: [Sugar High](https://sugar-high.vercel.app/)

Sugar High 是一个超轻量级的语法高亮库，提供简洁的 API 和预设支持多种编程语言，包括 JavaScript、CSS、Python 和 Rust，并可通过插件集成到 remark.js 中。

- 🚀 **超轻量级**：体积小巧，专注于提供高效的语法高亮功能。
- 🎨 **多语言支持**：内置预设支持 JavaScript、CSS、Python、Rust 等语言，并可根据文件扩展名自动选择预设。
- 🌗 **主题适配**：提供浅色和深色主题的 CSS 变量，支持根据系统主题或手动切换。
- 🔌 **插件集成**：可与 remark.js 等工具集成，方便在 Markdown 中高亮代码块。
- 📦 **简单易用**：通过 `highlight` 函数快速将代码转换为高亮的 HTML，支持自定义预设。

---

### [GitHub - huozhi/sugar-high: ✏️ 超轻量级代码语法高亮器，压缩并 gzip 后约 1KB · GitHub](https://github.com/huozhi/sugar-high)

**原文标题**: [GitHub - huozhi/sugar-high: ✏️ Super lightweight code syntax highlighter, around 1KB after minified and gzipped · GitHub](https://github.com/huozhi/sugar-high)

Sugar High 是一个超轻量级的 JavaScript 和 JSX 语法高亮库，压缩后仅约 1KB，支持浏览器及任何可设置 HTML 字符串的 JS 运行时。

- 📦 **安装与使用**：通过 npm 安装，导入 `highlight` 函数即可将代码转换为高亮 HTML。
- 🌐 **多语言支持**：核心支持 JavaScript 和 JSX，通过预设（presets）可扩展至 CSS、Rust、Python 等语言。
- 🎨 **自定义样式**：通过 CSS 自定义属性（如 `--sh-class`、`--sh-string`）灵活设置高亮颜色，支持主题定制。
- 🔢 **行号与高亮行**：可利用 CSS 计数器添加行号，并通过 `nth-child` 选择器高亮特定行。
- 📝 **集成工具**：提供 remark 插件，便于在 Markdown 处理中自动高亮代码块。
- 📄 **开源信息**：项目采用 MIT 许可证，在 GitHub 上拥有 843 个星标和 24 个分支，主要使用 TypeScript 开发。

---

### [发布 v12.0.0 · fb55/htmlparser2 · GitHub](https://github.com/fb55/htmlparser2/releases/tag/v12.0.0)

**原文标题**: [Release v12.0.0 · fb55/htmlparser2 · GitHub](https://github.com/fb55/htmlparser2/releases/tag/v12.0.0)

htmlparser2 发布了 v12.0.0 版本，主要更新包括将 HTML 解析与 WHATWG 规范对齐，涉及原始文本标签处理、SVG/MathML 支持、注释与声明解析改进，以及其他错误修复。

- 🚀 **版本发布**：v12.0.0 于 2025 年 3 月 20 日发布，包含 3 次提交至主分支。
- 📜 **规范对齐**：HTML 解析模式已与 WHATWG 规范对齐，XML 模式基本不受影响。
- 🔤 **原始文本标签**：`<iframe>`、`<noembed>`、`<noframes>` 和 `<plaintext>` 现为原始文本标签，内容不再解析为 HTML；`<textarea>` 现在解码实体。
- 🖼️ **SVG 与 MathML**：`<svg>` 内的标签名按规范进行大小写调整；外来内容中的 CDATA 部分被视为文本。
- 💬 **注释与声明**：改进了 `<!-->`、`<!DOCTYPEhtml>` 等特殊结构的解析，确保符合规范。
- 🔧 **隐式开闭与修复**：修复了 `reset()` 未清除属性状态的问题，并处理了 `<a>`、`<form>` 等标签的隐式行为。
- 📄 **完整日志**：详细更改记录可从 v11.0.0 到 v12.0.0 查看。

---

### [GitHub - staskobzar/vue-audio-visual: VueJS 音频可视化组件 · GitHub](https://github.com/staskobzar/vue-audio-visual)

**原文标题**: [GitHub - staskobzar/vue-audio-visual: VueJS audio visualization components · GitHub](https://github.com/staskobzar/vue-audio-visual)

这是一个用于 Vue.js 框架的音频频谱可视化插件，基于 HTML5 Web Audio API 构建，提供多种可视化组件，支持 Vue 3，并可通过组合式函数灵活使用。

- 🎵 **音频可视化组件**：提供 AvLine、AvBars、AvCircle、AvWaveform 和 AvMedia 等多种可视化组件，支持线条、柱状、圆形、波形等不同样式。
- 🔌 **Vue 3 兼容**：当前版本仅兼容 Vue 3，Vue 2 需使用 2.5.1 版本。
- 📦 **安装简便**：通过 npm 安装，支持全局插件注册或单个组件导入。
- 🛠️ **组合式函数**：每个组件都提供对应的 use 函数（如 useAVBars），允许直接操作 audio 和 canvas 元素引用。
- ⚙️ **丰富配置**：各组件支持多种自定义属性，如颜色、尺寸、动画效果等，满足不同可视化需求。
- 🎨 **媒体流支持**：AvMedia 组件可直接处理 MediaStream 对象，适用于实时音频输入可视化。
- 📄 **详细文档**：提供完整的 API 说明、属性列表和示例代码，便于开发者快速上手。
- 🔗 **开源项目**：采用 MIT 许可证，拥有活跃的社区支持和持续更新。

---

### [Vue 音视频插件演示](https://staskobzar.github.io/vue-audio-visual/)

**原文标题**: [Vue audio visual plugin demo](https://staskobzar.github.io/vue-audio-visual/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 📊 基于患者基因数据的人工智能模型可为慢性病患者提供动态个性化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题需要完善

---

### [GitHub - artiebits/svelte-seo：通过元标签、开放图谱和JSON-LD优化您的网站，提升搜索引擎和社交媒体表现。· GitHub](https://github.com/artiebits/svelte-seo)

**原文标题**: [GitHub - artiebits/svelte-seo: Optimize your website for search engines and social media with meta tags, Open Graph, and JSON-LD. · GitHub](https://github.com/artiebits/svelte-seo)

Svelte SEO 是一个用于优化 Svelte 应用搜索引擎和社交媒体可见性的开源工具，通过添加元标签、Open Graph、Twitter Card 和 JSON-LD 来提升网站在搜索结果中的排名。

- 📦 **安装便捷**：支持 npm、yarn 和 pnpm 安装，轻松集成到 Svelte 项目中。
- 🏷️ **基础功能**：可快速设置页面标题、描述和关键词等基础元标签。
- ⚙️ **高级配置**：支持 Open Graph、Twitter Card、Facebook 应用 ID 和 JSON-LD 等高级 SEO 属性。
- 🔧 **灵活定制**：提供丰富的属性选项，如语言变体、规范链接、AMP 版本等，满足多样化需求。
- 📄 **默认设置**：可通过布局文件统一设置默认 SEO 属性，减少重复配置。
- 📚 **文档齐全**：详细说明各属性用法，并参考了 Next SEO 等开源项目。
- 🌐 **社区活跃**：项目在 GitHub 上获得大量关注，有持续更新和维护。
- 📄 **开源许可**：采用 MIT 许可证，可自由使用和修改。

---

### [GitHub - pnpm/action-setup：安装 pnpm 包管理器 · GitHub](https://github.com/pnpm/action-setup)

**原文标题**: [GitHub - pnpm/action-setup: Install pnpm package manager · GitHub](https://github.com/pnpm/action-setup)

这是一个用于在 GitHub Actions 中安装 pnpm 包管理器的官方 Action，支持版本管理、依赖安装和缓存等功能。

- 🚀 **安装 pnpm**：通过指定版本号或使用 package.json 中的 packageManager 字段自动安装 pnpm。
- ⚙️ **配置灵活**：支持设置安装路径、是否运行 pnpm install 以及安装时的递归、工作目录和额外参数。
- 💾 **缓存支持**：可启用缓存以加速后续工作流，默认基于 pnpm-lock.yaml 文件生成缓存键。
- 📦 **独立模式**：提供 standalone 选项，允许在不安装 Node.js 的情况下使用 pnpm。
- 🔄 **使用示例丰富**：文档提供了多种常见使用场景的示例，包括仅安装 pnpm、结合 packageManager 安装、安装依赖包以及启用缓存。
- 📄 **开源许可**：项目基于 MIT 许可证开源，由社区维护。

---

### [GitHub - iamstevendao/vue-tel-input: Vue 国际电话输入组件 · GitHub](https://github.com/iamstevendao/vue-tel-input)

**原文标题**: [GitHub - iamstevendao/vue-tel-input: International Telephone Input with Vue · GitHub](https://github.com/iamstevendao/vue-tel-input)

这是一个用于 Vue.js 的国际电话号码输入组件库，支持 Vue 3，提供便捷的安装和多种使用方式。

- 📦 **组件功能**：国际电话号码输入组件，支持 Vue 3
- 🛠️ **安装方式**：可通过 npm 安装，也支持浏览器直接引入
- ⚙️ **使用灵活**：支持全局注册或局部组件引入，可配置全局选项
- 📄 **文档齐全**：提供详细文档和演示网站
- 🔄 **Vue 2 支持**：通过 legacy 版本兼容 Vue 2
- 🚀 **性能优化**：支持懒加载，减少初始包体积
- 🔧 **开发友好**：提供完整的开发环境和构建脚本
- 📜 **开源许可**：采用 MIT 许可证，可自由使用和修改
- 🌍 **国际化**：专门处理国际电话号码格式
- 📊 **项目活跃**：拥有 874 个星标，362 个分支，持续维护更新

---

### [Vue 电话输入 | Vue 电话输入](https://iamstevendao.com/vue-tel-input/)

**原文标题**: [Vue Tel Input | Vue Tel Input](https://iamstevendao.com/vue-tel-input/)

一款用于 Vue.js 的国际电话输入组件，由开发者社区精心打造。

- 📞 专为 Vue.js 框架设计的国际电话输入组件
- 👥 由开发者社区合作开发与维护
- ⚙️ 提供多种可配置选项和功能
- 💝 开源项目，体现开发者热情与奉献

---

### [发布 v1.40.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.40.0)

**原文标题**: [Release v1.40.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.40.0)

该页面显示了一个 GitHub 仓库的发布页面，其中包含版本 v1.40.0 的更新详情和错误信息提示。

- 🐛 页面加载时出现错误，提示需要重新加载
- 🏷️ 发布版本为 v1.40.0，于 2021 年 3 月 19 日由 Vanilagy 创建
- 🔧 新增了 FlacOutputFormatOptions.appendOnly 功能，支持 FLAC 文件的仅追加写入
- 🛠️ 修复了视频旋转元数据错误写入的问题
- 📐 修正了 ISOBMFF 3D 变换矩阵旋转提取和 MPEG-TS PAT 读取的错误
- 📊 优化了 VideoDecoderConfig 中 displayAspectWidth/Height 的包含逻辑
- 👥 有 3 位用户对该发布做出了积极反应

---

### [GitHub - vkurko/calendar: 全尺寸拖放式 JavaScript 事件日历，支持资源与时间线视图 · GitHub](https://github.com/vkurko/calendar)

**原文标题**: [GitHub - vkurko/calendar: Full-sized drag & drop JavaScript event calendar with resource & timeline views · GitHub](https://github.com/vkurko/calendar)

EventCalendar 是一个功能全面的 JavaScript 事件日历库，支持资源视图和时间线视图，提供拖放操作，轻量且无依赖。

- 📦 **轻量且独立**：压缩后仅约 35KB，采用 CSS Grid 构建，DOM 结构简洁，无需外部依赖。
- 🌐 **广泛使用**：已被超过 70,000 个网站使用，灵感来源于 FullCalendar，并实现了类似的选项。
- 🛠️ **多种集成方式**：支持作为 JavaScript 模块、Svelte 5 组件或独立捆绑包使用，可通过 CDN 快速引入。
- 🔌 **插件化视图**：提供 DayGrid、List、ResourceTimeline、ResourceTimeGrid、TimeGrid 及 Interaction 等插件，需至少选择一个视图插件。
- ⚙️ **丰富的配置选项**：包含事件管理、资源绑定、视图切换、本地化、主题定制等大量可配置项，支持动态修改选项。
- 🖱️ **交互功能**：内置事件拖放、调整大小、日期选择等交互功能，需配合 Interaction 插件使用。
- 📅 **事件与资源管理**：支持通过数组、URL 或自定义函数获取事件和资源数据，提供完整的 CRUD API 方法。
- 🎨 **主题与样式**：内置浅色/深色主题，支持通过 CSS 变量自定义颜色，适配现代浏览器（Chrome、Firefox、Safari、Edge）。

---

### [GitHub - LouisMazel/maz-ui: 用于构建界面的独立组件与工具的 Vue 和 Nuxt 库 · GitHub](https://github.com/LouisMazel/maz-ui)

**原文标题**: [GitHub - LouisMazel/maz-ui: Vue & Nuxt library of standalone components & tools to build interfaces · GitHub](https://github.com/LouisMazel/maz-ui)

Maz UI 是一个专为 Vue 和 Nuxt 设计的轻量高效 UI 组件库，提供丰富的组件、插件和工具，支持按需导入、主题定制和暗黑模式。

- 🎯 **按需导入组件** - 支持仅导入所需组件，避免代码冗余
- 🌙 **内置暗黑模式** - 提供开箱即用的深色主题支持
- 🎨 **可定制主题** - 通过 CSS 变量轻松自定义样式
- 📱 **响应式设计** - 采用移动优先的设计理念
- 🔧 **TypeScript 支持** - 提供完整的类型定义
- ⚡️ **轻量高效** - 支持 Tree-shaking，保持库的精简
- 🔍 **SSR 就绪** - 完美支持服务器端渲染
- 🧰 **功能全面** - 包含组件、插件、组合式函数、指令和工具包
- 📦 **多包管理** - 提供主题、图标、翻译、Nuxt 模块等独立包
- 🤝 **社区驱动** - 开放贡献指南，鼓励开发者参与共建

---

### [发布 3.0.0 版本 · gilbarbara/react-joyride · GitHub](https://github.com/gilbarbara/react-joyride/releases/tag/v3.0.0)

**原文标题**: [Release 3.0.0 · gilbarbara/react-joyride · GitHub](https://github.com/gilbarbara/react-joyride/releases/tag/v3.0.0)

react-joyride 3.0.0 版本是一次全面的重写，专注于采用现代 React 模式、减小包体积并提供更直观的 API。此次更新引入了新的钩子、事件系统和组件，同时进行了多项重大变更以优化性能和开发体验。

- 🎣 引入 `useJoyride` 钩子，替代 `getHelpers`，提供控制、状态、当前步骤等
- 🎭 采用新的区分类型事件系统，支持 `onEvent` 和选择性订阅
- ⚡ 新增步骤级异步 `before`/`after` 回调钩子
- 🎯 集成 Floating UI 替代 Popper.js，提升定位灵活性
- 🎨 使用 SVG 覆盖层精确渲染聚光灯效果，替代 CSS 阴影
- 🧩 支持通过 React Portal 渲染，允许自定义容器
- 📦 包体积减少约 30%，依赖项优化
- ⚠️ 包含多项重大变更，如 API 重构和属性重命名
- 📚 提供完整的迁移指南和新功能文档

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户在开发、预演环境中的交互行为，利用 AI 生成并持续更新全面的端到端测试套件，旨在彻底消除传统测试的维护负担和不可靠性，帮助开发团队以更快速度交付无回归的高质量代码。

- 🎯 **自动化测试生成**：通过记录用户交互，AI 自动生成覆盖所有代码分支和用户流程的测试套件
- 🔄 **持续演进**：测试套件随应用功能变化自动更新，无需人工编写、修复或维护测试
- ⚡ **极致速度**：基于 Chromium 构建的确定性调度引擎，实现闪电般快速且零波动的测试执行
- 🛡️ **无副作用测试**：通过记录和回放后端响应，实现无副作用、无虚假警报的测试环境
- 🌐 **广泛兼容**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流前端框架
- 🏢 **企业级验证**：已被 Dropbox、Notion 等 100 多家组织采用，特别适合复杂代码库
- 🚀 **快速集成**：只需添加脚本标签即可在几分钟内完成设置，支持与现有测试套件结合或完全替代

---

### [VS Code 如何利用 AI 进行构建](https://code.visualstudio.com/blogs/2026/03/13/how-VS-Code-Builds-with-AI)

**原文标题**: [How VS Code Builds with AI](https://code.visualstudio.com/blogs/2026/03/13/how-VS-Code-Builds-with-AI)

VS Code 团队通过 AI 代理将发布周期从每月缩短至每周，显著提升了开发效率与反馈速度。团队利用 AI 自动化日常任务，如问题分类、代码审查和发布说明，同时保持高质量标准。AI 代理使产品经理和工程师能够并行工作并快速原型设计，而人工审查则专注于代码质量和用户体验的“品味”评估。

- 🤖 **AI 代理驱动工作流**：VS Code 团队利用 AI 代理自动化问题分类、提交总结和发布说明，实现每周发布周期。
- 🚀 **并行工作与效率提升**：通过同时运行多个 AI 会话，团队能在会议期间并行处理任务，打破“制造者”与“管理者”日程的冲突。
- 📈 **自动化处理规模化开销**：AI 代理自动处理提交总结、问题分类和代码审查，帮助团队在提速的同时维持工作质量。
- 👥 **全员参与代码提交**：产品经理等非工程师角色也能通过 AI 代理创建原型和 PR，加速功能验证与迭代。
- 🛡️ **质量保障与人工审查**：尽管 AI 代理提升效率，团队仍依赖人工审查确保代码架构合理、用户体验愉悦，并通过自动化测试和“黄金场景”验证防止回归。
- 🔮 **未来展望与社区协作**：团队致力于构建“AI 就绪”的代码库，并鼓励社区分享自动化工作流经验，共同推进开发流程的演进。

---

### [GitHub - secretlint/secretlint: 可插拔的凭证防泄露代码检查工具。 · GitHub](https://github.com/secretlint/secretlint)

**原文标题**: [GitHub - secretlint/secretlint: Pluggable linting tool to prevent committing credential. · GitHub](https://github.com/secretlint/secretlint)

Secretlint 是一个可插拔的代码检查工具，旨在防止在代码库中意外提交敏感凭证信息。

- 🔍 **扫描功能**：能够检测项目中的敏感凭证并生成报告
- 🛠️ **项目友好**：易于在项目中设置，并可集成到持续集成服务中
- 🔒 **预提交钩子**：支持在提交前检查，防止提交包含凭证的文件
- 🔌 **可插拔架构**：允许创建自定义规则和灵活配置
- 📚 **文档完善**：每条规则都提供详细的检测原因说明
- 🐳 **多平台支持**：提供 Docker、Node.js 和独立二进制文件三种安装方式
- ⚙️ **配置灵活**：支持通过配置文件、注释忽略和消息 ID 过滤等多种方式定制检查规则
- 🔗 **丰富集成**：支持 Husky、pre-commit、GitHub Actions 等多种开发工具和工作流
- 🌐 **浏览器扩展**：提供 Chrome 和 Firefox 浏览器扩展，可在开发者工具中检测请求/响应中的凭证
- 📦 **规则丰富**：包含 AWS、GCP、GitHub、OpenAI 等多个平台的专用检测规则

---

### [无](https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html)

**原文标题**: [None](https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html)

罗布·派克的编程五法则强调避免过度优化和保持简单性，主张通过测量定位性能瓶颈，并优先选择简单可靠的数据结构与算法。

- 🔍 无法预知程序性能瓶颈，避免未经证实的优化
- 📏 优化前必须测量，仅处理关键瓶颈部分
- 🐌 复杂算法在小数据量时效率低，慎用花哨方案
- 🐛 简洁算法更少错误且易于实现
- 🗃️ 数据结构决定算法设计，是编程核心

---

### [AddyOsmani.com - 理解债务：AI 生成代码的隐性成本。](https://addyosmani.com/blog/comprehension-debt/)

**原文标题**: [AddyOsmani.com - Comprehension Debt - the hidden cost of AI generated code.](https://addyosmani.com/blog/comprehension-debt/)

理解债是过度依赖 AI 和自动化对人类智力和记忆造成的隐性成本，尤其影响工程师的代理式工程。它表现为代码量与人类真正理解之间的差距，虽不体现在速度指标中，但会悄然累积，最终需连本带利偿还。

- 🧠 **理解债是代码量与人类理解间的隐形差距**：不同于技术债，它滋生虚假信心，在系统理论“蒸发”后导致意外崩溃。
- 📉 **AI 辅助削弱技能形成**：研究显示，使用 AI 的工程师在理解测试中得分更低，被动委托尤其损害调试和概念理解能力。
- ⚡ **速度不对称破坏审查循环**：AI 生成代码的速度远超人类评估能力，使代码审查从质量关卡变为吞吐量问题。
- 🧪 **测试无法完全替代理解**：自动化验证有硬性上限，无法覆盖未预料的行为，且 AI 可能同时更改代码和测试，掩盖问题。
- 📝 **详细规格并非万能解决方案**：规格无法完全捕捉隐式决策，且编写成本可能超过 AI 带来的生产力收益。
- 🏛️ **系统理解者价值不降反升**：随着 AI 代码量增加，深刻理解系统的工程师成为稀缺资源，负责维护代码库的连贯性。
- 📊 **现有度量体系无法捕捉理解债**：速度指标看似完美，但无法反映理解缺陷，导致组织在无意识中分散责任。
- ⚖️ **监管迫在眉睫**：当 AI 代码应用于关键领域时，缺乏充分审查将无法在事故报告中站住脚，理解纪律成为必需。
- 🔍 **核心在于理解而非生成更多代码**：必须明确变更意图，将验证视为结构性约束，并区分“测试通过”与“真正理解”。

---

### [史蒂夫·特劳顿 - 史密斯："这是给 macOS 上讨厌菜单图标的人准备的…" - Mastodon](https://mastodon.social/@stroughtonsmith/116262411548746327)

**原文标题**: [Steve Troughton-Smith: "Here's one for the icons-in-menus haters on macOS…" - Mastodon](https://mastodon.social/@stroughtonsmith/116262411548746327)

要使用 Mastodon 网页应用，需启用 JavaScript，或根据您的平台选择原生应用。

- 🌐 启用 JavaScript 以访问网页版
- 📱 可下载平台对应的原生应用替代

---

