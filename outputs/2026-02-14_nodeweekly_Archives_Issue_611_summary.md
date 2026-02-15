### [Node 周刊第 611 期：2026 年 2 月 12 日](https://nodeweekly.com/issues/611)

**原文标题**: [Node Weekly Issue 611: February 12, 2026](https://nodeweekly.com/issues/611)

TypeScript 6.0 进入测试版，对 Node 开发者带来多项重要更新，包括默认启用严格模式、类型默认值变更等。同时，Node.js 发布新版本，带来性能提升和新功能，JavaScript 生态系统也涌现出多项新工具和库更新。

- 🚀 TypeScript 6.0 进入测试版，默认启用严格模式，并引入多项影响 Node 开发者的变更
- 📦 Node.js 发布 25.6.1 和 24.13.1 版本，带来更快的模块解析和 Unicode 17 支持
- 🔧 生态系统更新：ESLint 10.0 发布，Bun 1.3.9 新增功能，Transformers.js v4 预览版支持 WebGPU
- 🛠️ 新工具涌现：包括终端应用框架 Ink 6.7、验证库 VineJS 4.3 和全栈框架 Shovel.js
- 📄 分类广告部分列出多项库和工具更新，如 Prisma 7.4.0 和 pnpm v10.29.3

---

### [TypeScript 6.0 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)

**原文标题**: [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)

TypeScript 6.0 Beta 版本发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本引入了多项新特性、改进以及为适应现代 JavaScript 生态而做的重大默认值变更和弃用。

- 🚀 **减少无 `this` 使用函数的上下文敏感性**：现在，如果函数内部未实际使用 `this`，则在进行类型推断时不会被跳过，解决了之前方法语法中因隐含 `this` 参数导致的类型推断问题。
- 📁 **支持以 `#/` 开头的子路径导入**：TypeScript 现在支持 Node.js 中允许的 `#/` 前缀子路径导入，简化了项目内部的模块别名配置。
- 🔧 **允许 `--moduleResolution bundler` 与 `--module commonjs` 组合使用**：为从已弃用的 `--moduleResolution node` 迁移的项目提供了更合适的升级路径。
- 🔄 **新增 `--stableTypeOrdering` 标志**：此标志使 TypeScript 6.0 的类型排序行为与 7.0 保持一致，有助于减少两个版本间的差异，便于迁移诊断，但可能会带来性能开销。
- 🎯 **新增 `es2025` 作为 `target` 和 `lib` 选项**：虽然 ES2025 没有新的语言特性，但增加了新的内置 API 类型（如 `RegExp.escape`），并将一些声明从 `esnext` 移至 `es2025`。
- ⏳ **为 `Temporal` API 提供内置类型**：针对已进入 Stage 3 的 `Temporal` 提案，TypeScript 6.0 通过 `esnext` 库提供了其类型定义，开发者可以提前使用。
- 🗺️ **为 Map/WeakMap 新增 "upsert" 方法类型**：为 ECMAScript 新增的 `getOrInsert` 和 `getOrInsertComputed` 方法提供了类型支持，简化了常见的“检查 - 设置”模式。
- 🛡️ **新增 `RegExp.escape` 类型**：为进入 Stage 4 的 `RegExp.escape` 提案提供了类型支持，用于安全地转义正则表达式中的特殊字符。
- 🌐 **`dom` 库现在包含 `dom.iterable` 和 `dom.asynciterable`**：将迭代相关声明直接并入主 `dom` 库，简化了配置，提升了开发体验。
- ⚠️ **多项重大变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、`target` 默认改为最新 ES 版本、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等旧有选项和语法，旨在推动项目现代化并提升性能。

---

### [TypeScript 7 进展 - 2025 年 12 月 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

**原文标题**: [Progress on TypeScript 7 - December 2025 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

TypeScript 7.0（代号“Corsa”）的开发进展顺利，已进入稳定可用的阶段，提供了显著性能提升和更完整的编辑器支持，同时团队宣布 TypeScript 6.0 将是最后一个基于 JavaScript 代码库的版本，未来将全力推进 TypeScript 7.0 的完善和发布。

- 🚀 **性能大幅提升**：TypeScript 7.0 通过原生代码和共享内存并行技术，编译速度相比 6.0 版本提升约 8-10 倍，并支持多项目并行构建。
- 🛠️ **编辑器支持完善**：VS Code 扩展已提供稳定的原生预览版，支持代码补全（含自动导入）、跳转定义、重命名等核心语言服务功能，可随时切换回内置版本。
- ✅ **类型检查高度兼容**：TypeScript 7.0 的类型检查已接近完成，在测试用例中与 6.0 的错误检测一致性极高，可安全用于项目验证。
- 📦 **编译器功能就绪**：命令行工具`tsgo`已支持增量编译、项目引用和构建模式，可通过`@typescript/native-preview`包安装使用。
- ⚠️ **需注意的变更**：7.0 将默认启用`--strict`、移除`--target es5`等已弃用功能，JavaScript 类型检查规则更严格，部分 JSDoc 标签不再支持。
- 🔄 **版本过渡策略**：TypeScript 6.0 作为最终 JavaScript 版本，主要提供弃用警告和兼容性桥梁，后续将仅通过补丁修复安全或严重回归问题。
- 🐛 **问题反馈重置**：由于语言服务架构重构，旧版编辑器相关的问题报告需在新版扩展中重新验证和提交。
- 📢 **鼓励试用反馈**：团队邀请开发者尝试 VS Code 扩展和预览版编译器，并通过 GitHub 提交问题以帮助完善最终版本。

---

### [错误](https://nodeweekly.com/link/180674/web)

**原文标题**: [Error](https://nodeweekly.com/link/180674/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/180674/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [TypeScript 6.0 Beta 版本发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#types-now-defaults-to-%5B%5D)

**原文标题**: [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#types-now-defaults-to-%5B%5D)

TypeScript 6.0 Beta 版本已发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本引入了多项新特性、改进以及为适应现代 JavaScript 生态而进行的重大变更和弃用。

- 🚀 **发布与定位**：TypeScript 6.0 Beta 是通往原生版本 7.0 的桥梁，包含了对齐性改进和新功能。
- 🔍 **类型推断优化**：对于未使用 `this` 的函数，减少了其上下文敏感性，提升了方法语法中的类型推断能力。
- 📁 **子路径导入支持**：现在支持以 `#/` 开头的子路径导入，简化了项目内部的模块别名配置。
- ⚙️ **模块解析组合**：`--moduleResolution bundler` 现在可与 `--module commonjs` 组合使用，为项目升级提供了更合适的路径。
- 🔢 **稳定类型排序标志**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，便于迁移对比，但可能会降低性能。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的选项，并引入了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 3 的 Temporal API 提供了内置类型支持，可通过 `esnext` 目标或库使用。
- 🗺️ **新增 Map 方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法，简化了“检查并插入”模式。
- 🛡️ **正则表达式转义**：新增 `RegExp.escape` 函数，用于安全地转义正则表达式中的特殊字符。
- 🌐 **DOM 库整合**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：多项默认值被更新（如 `strict: true`），并弃用了 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等旧选项和语法，为 7.0 做准备。
- 🛠️ **配置调整**：`rootDir` 默认值改为 `.`，`types` 默认值改为空数组 `[]`，许多项目需要据此调整配置以提升性能。
- 🚫 **命令行为变更**：当存在 `tsconfig.json` 时，在命令行中指定文件将报错，需使用 `--ignoreConfig` 标志来忽略配置。

---

### [TypeScript 6.0 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#subpath-imports-starting-with-#/)

**原文标题**: [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#subpath-imports-starting-with-#/)

TypeScript 6.0 Beta 版本发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本引入了多项新特性、改进以及为适应现代 JavaScript 生态而做的重大默认值变更和弃用。

- 🚀 **发布与定位**：TypeScript 6.0 Beta 发布，是通往原生重写版本 7.0 的桥梁版本。
- 🧠 **推断优化**：对于未使用 `this` 的函数，减少了其上下文敏感性，改善了泛型函数中的类型推断。
- 🗺️ **路径导入**：支持 Node.js 中以 `#/` 开头的子路径导入，简化了项目内部的模块别名配置。
- ⚙️ **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用。
- 🔢 **稳定类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，便于迁移对比。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的新选项。
- ⏳ **Temporal API 类型**：为已达到 Stage 3 的 Temporal 日期时间提案提供了内置类型支持。
- 📝 **Map 新增方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法类型。
- 🛡️ **正则表达式转义**：新增 `RegExp.escape` 函数的类型支持。
- 🌐 **DOM 库整合**：`dom` 类型库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容。
- ⚠️ **重大变更与弃用**：多项默认值变更（如 `strict: true`、`module: esnext`）和功能弃用（如 `target: es5`、`--moduleResolution node`、`--baseUrl` 等），旨在提升性能并反映现代开发实践。
- 🧭 **迁移准备**：强调需处理 6.0 中的弃用警告，因为它们将在 7.0 中被完全移除。

---

### [错误](https://nodeweekly.com/link/180671/web)

**原文标题**: [Error](https://nodeweekly.com/link/180671/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='devblogs.microsoft.com', port=443): Max retries exceeded with url: /typescript/announcing-typescript-6-0-beta/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [TypeScript 6.0 Beta 版本发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#deprecated:---esmoduleinterop-false-and---allowsyntheticdefaultimports-false)

**原文标题**: [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#deprecated:---esmoduleinterop-false-and---allowsyntheticdefaultimports-false)

TypeScript 6.0 Beta 版本已发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本引入了多项新特性、改进以及为适应现代 JavaScript 生态而做的重大变更和弃用。

- 🚀 **版本定位**：作为 TypeScript 7.0 的前置版本，主要变化旨在为迁移到 7.0 做准备。
- 🔧 **上下文敏感性优化**：对于未使用 `this` 的函数，改进了泛型类型推断，解决了方法语法中的参数类型推断问题。
- 📁 **子路径导入支持**：现在支持以 `#/` 开头的子路径导入，简化了项目内部的模块别名配置。
- ⚙️ **模块解析组合**：允许 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为项目升级提供更合适的路径。
- 🔄 **稳定类型排序标志**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，便于迁移对比，但可能会降低性能。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的选项，并引入了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 3 的 Temporal 提案提供了内置类型支持。
- 🗺️ **Map 新增方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法，简化了“检查 - 设置”模式。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数，用于安全地转义正则表达式中的特殊字符。
- 🌐 **DOM 库整合**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等多项设置，以反映现代开发实践。
- 📝 **配置默认值更新**：`rootDir` 默认改为项目根目录，`types` 默认改为空数组以提高性能，需要时需显式声明。
- 🚫 **错误语法弃用**：弃用了 `module` 关键字定义命名空间、`asserts` 导入属性关键字等旧语法。
- 🛑 **命令行行为变更**：当存在 `tsconfig.json` 时，在命令行指定文件将报错，需使用 `--ignoreConfig` 标志来忽略配置。

---

### [TypeScript 6.0 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#breaking-changes-and-deprecations-in-typescript-6.0)

**原文标题**: [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#breaking-changes-and-deprecations-in-typescript-6.0)

TypeScript 6.0 Beta 版本发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本引入了多项新特性、改进以及为适应现代 JavaScript 生态而做的重大默认值变更和弃用。

- 🚀 **版本定位**：TypeScript 6.0 是当前代码库的最终版本，作为向原生重写的 7.0 版本过渡的桥梁。
- 🔧 **推断优化**：对于未使用 `this` 的函数，减少了其上下文敏感性，改善了泛型函数中参数类型的推断能力。
- 📁 **路径导入**：支持 Node.js 中以 `#/` 开头的子路径导入，简化了项目内部的模块别名配置。
- ⚙️ **解析器组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为项目升级提供了更合适的路径。
- 🔄 **类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，便于迁移对比，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的新选项，并引入了新的内置 API 类型。
- ⏳ **时间 API**：为已达到 Stage 3 的 Temporal API 提供了内置类型支持。
- 🗺️ **Map 新方法**：为 `Map` 和 `WeakMap` 新增了 `getOrInsert` 和 `getOrInsertComputed` 方法，简化了“检查 - 插入”模式。
- 🛡️ **正则表达式转义**：新增 `RegExp.escape` 函数，用于安全地转义正则表达式中的特殊字符。
- 🌐 **DOM 库整合**：将 `dom.iterable` 和 `dom.asynciterable` 的内容完全整合到 `dom` 库中，简化了配置。
- ⚠️ **重大变更与弃用**：多项默认值发生变更（如 `strict` 默认为 `true`，`module` 默认为 `esnext`），并弃用了 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等大量旧选项和语法，为 7.0 做准备。
- 🚫 **配置加载规则**：当存在 `tsconfig.json` 时，在命令行中指定文件将报错，需使用 `--ignoreConfig` 标志来忽略配置。

---

### [使用 Memetria K/V 构建 — Memetria](https://dashboard.memetria.com/nodeweekly/)

**原文标题**: [Build with Memetria K/V — Memetria](https://dashboard.memetria.com/nodeweekly/)

Memetria 提供兼容 Valkey 和 Redis OSS 的键值存储服务，支持无缝扩展、加密连接和详细监控，并提供从开发到高性能的多层级托管方案。

- 🚀 **兼容性强** – 支持 Valkey 和 Redis OSS，轻松导入导出数据  
- 📈 **无缝扩展** – 可在不停机的情况下调整资源规模  
- 🔐 **加密连接** – 提供双重加密和纯 TLS 连接选项  
- 📊 **详细监控** – 包含健康状态、内存及性能图表  
- 💼 **多层级方案** – 从开发版（共享资源）到性能版（专属资源、高 I/O）的托管计划  
- 🌍 **全球区域** – 支持多个 AWS 区域部署，如亚洲、欧洲、美洲等  
- 📋 **灵活定价** – 月费从 14 美元起，按内存和性能需求分级

---

### [npmx - npm 注册表的包浏览器](https://npmx.dev/)

**原文标题**: [npmx - Package Browser for the npm Registry](https://npmx.dev/)

npmx 是一个专为 npm 软件包注册表设计的快速现代浏览器，旨在提升用户体验。

- 🔍 **搜索功能**：提供便捷的 npm 软件包搜索工具
- 🛠️ **技术兼容**：支持 Nuxt、Vue、React、Svelte 等多种前端框架
- 🤝 **社区参与**：鼓励用户通过 GitHub 贡献代码，共同改进产品
- 💬 **交流平台**：设有 Discord 社区，方便用户聊天、提问和分享想法
- 📢 **信息更新**：通过 Bluesky 等渠道发布最新动态，保持用户及时获取信息

---

### [获取失败](https://nodeweekly.com/link/180635/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/180635/web)

无法总结：获取内容失败，状态码 403。

---

### [axios - npmx](https://npmx.dev/package/axios)

**原文标题**: [axios - npmx](https://npmx.dev/package/axios)

Axios 是一个基于 Promise 的 HTTP 客户端，适用于浏览器和 Node.js 环境，提供简洁的 API 进行网络请求。

- 🌐 **跨平台支持**：可在浏览器和 Node.js 中发起 HTTP 请求。
- 🔄 **Promise 基础**：完全支持 Promise API，便于异步操作。
- 🛡️ **拦截器功能**：允许在请求和响应前后添加自定义逻辑。
- 📦 **自动数据转换**：自动序列化 JSON 数据，支持 FormData 和 URL 编码格式。
- ⏱️ **请求取消**：提供 AbortController 和 CancelToken（已弃用）机制取消请求。
- 🚀 **高级特性**：包括进度追踪、速率限制、HTTP/2 支持和 Fetch 适配器。
- 📚 **丰富配置**：支持全局默认设置、自定义实例和详细的请求/响应配置。
- 🛠️ **易于安装**：可通过 npm、yarn 等包管理器或 CDN 快速引入。

---

### [比较软件包 - npmx](https://npmx.dev/compare)

**原文标题**: [Compare Packages - npmx](https://npmx.dev/compare)

该工具允许用户并排比较不同的 npm 软件包，通过关键指标帮助选择最合适的包。

- 🔍 搜索并添加至少两个 npm 包进行对比
- 📊 提供性能、包大小、依赖数量等多项指标比较
- 📦 显示安装大小、直接依赖和总依赖数
- ⚡ 包含每周下载量、受欢迎度和发布时间等信息
- 🔒 评估安全性，包括许可证和漏洞情况
- 📐 检查兼容性，如引擎支持和模块格式
- 📈 综合健康度评估，辅助决策

---

### [如何在 Node.js 中发起 HTTP 请求](https://nodejsdesignpatterns.com/blog/nodejs-http-request/)

**原文标题**: [How to make an HTTP request in Node.js](https://nodejsdesignpatterns.com/blog/nodejs-http-request/)

本文全面介绍了在 Node.js 中发起 HTTP 请求的现代方法，重点推荐使用 Node.js 18 及以上版本内置的 `fetch()` API。文章涵盖了从基础 GET/POST 请求、认证、超时设置、流式处理，到处理重试、文件上传、查询参数、性能优化和单元测试等高级主题，并对比了 `fetch()`、`http/https` 模块及外部库（如 axios）的适用场景。

- 🚀 **首选内置 `fetch()` API**：Node.js 18+ 内置了与浏览器标准一致的 `fetch()` 函数，无需安装额外依赖即可进行 HTTP 请求，是现代 Node.js 开发的首选方式。
- 🔍 **正确处理请求与响应**：使用 `fetch()` 时需注意网络错误与 HTTP 语义错误的区别，应检查 `response.ok` 或状态码，并使用 `.json()`、`.text()` 等方法解析响应体。
- 📤 **发送 POST 请求与认证**：通过设置 `method: 'POST'`、`headers`（如 `'Content-Type': 'application/json'`）和 `body`（需 `JSON.stringify()`）来发送 JSON 数据；常用 `Authorization: Bearer <token>` 进行认证。
- ⏱️ **设置超时与处理流**：使用 `AbortSignal.timeout()` 防止请求无限挂起；通过 `response.body` 获取 `ReadableStream` 或配合 `fs` 模块实现大文件流式上传/下载，以优化内存使用。
- 🔄 **实现重试与并发控制**：为应对临时故障，可实现指数退避的重试逻辑（注意非幂等操作的风险）；使用 `Promise.all()` 进行并发请求，或通过自定义逻辑控制并发量以防过载。
- 🛡️ **安全构建 URL 与测试**：使用 `URL` 和 `URLSearchParams` API 安全构建查询参数，避免注入攻击；通过安装 `undici` 包并使用其 `MockAgent` 来模拟 HTTP 请求，便于编写可靠的单元测试。
- ⚖️ **性能考量与模块选择**：`fetch()` 易用但有一定性能开销；在超高吞吐场景（如每秒数千请求）可考虑直接使用 `undici.request()` 或 `http/https` 模块以获得更佳性能。`http/https` 模块更底层，适用于 Node.js 18 以下版本或需要精细控制的情况。
- ❓ **常见问题解答**：Node.js 18+ 自带 `fetch()`，通常无需 axios 等外部库；`http/https` 模块主要用于兼容旧版本、集成遗留代码或极端性能优化场景。

---

### [错误](https://nodeweekly.com/link/180639/web)

**原文标题**: [Error](https://nodeweekly.com/link/180639/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/180639/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Node.js — Node.js 25.6.1（当前版本）](https://nodejs.org/en/blog/release/v25.6.1)

**原文标题**: [Node.js — Node.js 25.6.1 (Current)](https://nodejs.org/en/blog/release/v25.6.1)

Node.js 25.6.1（Current）版本发布，包含多项依赖更新、性能优化、错误修复及文档改进，并提供了各平台的安装包和二进制文件下载链接。

- 🛠️ **依赖更新**：将 cjs-module-lexer 替换为 merve，并升级了 npm、undici、minimatch 等多个依赖包版本。
- 🐛 **错误修复**：解决了 Windows 下 DNS SRV 查询的 ECONNREFUSED 问题，修复了模块加载、网络连接及测试中的多个缺陷。
- 📚 **文档完善**：更新了 EventEmitter 错误处理、测试运行器环境选项等文档，并修正了多处描述错误和链接。
- ⚡ **性能优化**：在 HTTP 头部解析中引入内存板分配，优化 SQLite 大文本绑定和结构化克隆实现，提升执行效率。
- 🔧 **工具与测试**：更新了构建工具链（如 Visual Studio 2026），统一了测试快照模式，并修复了多个测试中的竞态条件和稳定性问题。
- 📦 **发布文件**：提供了 Windows、macOS、Linux 等多平台的安装程序和二进制文件，均附带 PGP 签名校验。

---

### [GitHub - nodejs/merve：一款用于从CommonJS模块中提取命名导出的快速C++词法分析器。该库通过静态分析检测CommonJS导出模式，无需执行代码。](https://github.com/nodejs/merve)

**原文标题**: [GitHub - nodejs/merve: A fast C++ lexer for extracting named exports from CommonJS modules. This library performs static analysis to detect CommonJS export patterns without executing the code.](https://github.com/nodejs/merve)

Merve 是一个用 C++ 编写的高性能词法分析器，用于从 CommonJS 模块中静态提取命名导出信息，无需执行代码。

- 🚀 **快速高效**：采用零拷贝解析，支持 SIMD 加速，单次遍历无回溯
- 🎯 **准确识别**：支持复杂的 CommonJS 导出模式，包括重导出、Object.defineProperty 和转译器输出
- 📍 **源码定位**：每个导出都包含基于 1 的行号，便于工具集成
- 🌐 **Unicode 支持**：正确处理 JavaScript 字符串转义序列，包括 Unicode 码点和代理对
- 📦 **易于集成**：提供 CMake 和单头文件两种安装方式，无依赖或可选依赖 simdutf
- 🛡️ **错误处理**：能检测 ESM 语法并返回相应错误，帮助区分模块类型
- 📄 **开源许可**：采用 Apache-2.0 和 MIT 双重许可

---

### [build,deps: 由 anonrig 在 nodejs/node 仓库的 Pull Request #61456 中将 cjs-module-lexer 替换为 merve](https://github.com/nodejs/node/pull/61456)

**原文标题**: [build,deps: replace cjs-module-lexer with merve by anonrig · Pull Request #61456 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61456)

Node.js 项目将 cjs-module-lexer 依赖替换为 merve，以提升 CommonJS 模块的冷导入性能约 25%，并计划将 merve 仓库转移至 Node.js 组织进行维护。

- 🚀 性能提升：新的 cjs 模块词法分析器 merve 使冷导入 CJS 文件速度提升约 25%，热导入提升约 12%
- 🔄 依赖变更：移除旧的 cjs-module-lexer，引入新的 merve 依赖
- 📊 基准测试：提供了详细的性能基准测试结果，涵盖多种 ESM 相关场景
- 🏗️ 代码审查：经过多位核心贡献者审查，包括更新相关文档和构建脚本
- 📝 文档更新：需要更新多处对 cjs-module-lexer 的引用
- 🔧 组织迁移：计划将 merve 仓库从个人账户迁移至 Node.js 组织
- ✅ 合并状态：该更改已被合并，并标记为 notable-change 将在发布说明中突出显示

---

### [GitHub - nodejs/cjs-module-lexer: 通过分析 CommonJS 模块快速提取命名导出的词法分析器](https://github.com/nodejs/cjs-module-lexer)

**原文标题**: [GitHub - nodejs/cjs-module-lexer: Fast lexer to extract named exports via analysis from CommonJS modules](https://github.com/nodejs/cjs-module-lexer)

这是一个用于快速解析 CommonJS 模块并提取命名导出的 JavaScript 词法分析器，由 Node.js 官方维护，主要用于在 ES 模块中导入 CommonJS 模块时检测可用的命名导出。

- 🚀 **高性能解析**：冷启动约 90ms/MB，热启动约 15ms/MB，WASM 版本性能提升约 1.5 倍
- 🎯 **精确检测**：支持`exports.name`、`exports['name']`、`Object.defineProperty`等多种导出模式
- 🔄 **重导出识别**：能检测`module.exports = require()`和转译器生成的星号重导出模式
- 🧩 **语法兼容**：全面支持 JavaScript 语法，正确处理注释、字符串和正则表达式歧义
- 🛡️ **模式冻结**：检测模式已固定，确保不同 Node.js 版本间的向后兼容性
- 📦 **多环境支持**：支持 Node.js 10+ 和所有支持 WebAssembly 的浏览器
- 🔧 **使用简便**：提供 CommonJS 和 ESM 两种 API，WASM 版本需要异步初始化
- 📊 **基准测试**：包含详细的性能基准数据，WASM 版本在 3635KB 样本上平均耗时 27.76ms

---

### [Node.js — Node.js 24.13.1（长期支持版）](https://nodejs.org/en/blog/release/v24.13.1)

**原文标题**: [Node.js — Node.js 24.13.1 (LTS)](https://nodejs.org/en/blog/release/v24.13.1)

Node.js 24.13.1（LTS）版本发布，代号“Krypton”，包含多项稳定性改进、依赖项更新、性能优化和安全修复。

- 🐍 构建系统新增对 Python 3.14 的支持
- 🚀 将 `--heapsnapshot-near-heap-limit` CLI 选项标记为稳定
- 🔒 根证书更新至 NSS 3.119，提升安全性
- 📦 将 `--build-snapshot` 和 `--build-snapshot-config` 标记为稳定功能
- 👥 新增三位协作者：avivkeller、gurgunday 和 Renegade334
- 🌐 URL 解析器 ada 更新至 v3.4.2，支持 Unicode 17
- ⚙️ 将 `v8.queryObjects()` API 标记为稳定
- 🛠️ 包含多项错误修复、性能改进及测试更新

---

### [ESLint v10.0.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/02/eslint-v10.0.0-released/)

**原文标题**: [ESLint v10.0.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/02/eslint-v10.0.0-released/)

ESLint v10.0.0 是一个主要版本发布，引入了新功能、修复了错误，并包含多项重大变更，需要用户仔细阅读迁移指南以确保顺利升级。

- 🚀 **主要版本升级**：ESLint v10.0.0 是一个重大更新，包含新功能和破坏性变更，需手动安装 `npm i eslint@10.0.0 --save-dev`。
- ⚠️ **Node.js 支持变更**：不再支持 Node.js v20.19.0 之前版本、v21.x 和 v23.x，仅支持 v20.19.0、v22.13.0 及以上版本。
- 📄 **全新配置查找算法**：默认从每个被检测文件的目录查找 `eslint.config.*`，支持单次运行中使用多个配置文件，适用于 monorepo。
- 🗑️ **移除 eslintrc 功能**：完全移除了旧的 eslintrc 配置系统，包括环境变量、CLI 参数和相关文件（如 `.eslintrc.*` 和 `.eslintignore`）。
- 🔍 **JSX 引用追踪**：现在正确追踪 JSX 元素的引用，解决了 `no-unused-vars` 和 `no-undef` 规则中的误报和漏报问题。
- 📦 **内置类型定义**：Espree 和 ESLint Scope 包现在包含内置类型定义，取代了之前的 `@types/` 包，可能需要更新相关代码。
- 🧪 **RuleTester 增强**：新增断言选项（`requireMessage`、`requireLocation`、`requireData`）以强化测试，并改进了失败测试的位置报告。
- ⚙️ **规则更新与弃用**：`max-params` 规则新增 `countThis` 选项；移除了多个已弃用的 `context` 成员和 `SourceCode` 方法；更新了 `eslint:recommended` 配置。
- 🎨 **格式化器上下文颜色属性**：当使用 `--color` 或 `--no-color` 时，格式化器的上下文对象会包含 `color` 属性，便于自定义格式化器决定是否应用颜色。
- 🔧 **其他变更**：`Program` AST 节点的范围现在涵盖整个源代码；不再支持 jiti < v2.2.0；进行了多项错误修复、文档更新和构建优化。

---

### [Bun v1.3.9 | Bun 博客](https://bun.sh/blog/bun-v1.3.9)

**原文标题**: [Bun v1.3.9 | Bun Blog](https://bun.sh/blog/bun-v1.3.9)

本文介绍了 Bun 的最新更新，包括安装与升级方法、并行与顺序运行脚本功能、HTTP/2 连接升级、Symbol.dispose 支持、NO_PROXY 改进、性能优化及多项错误修复。

- 🚀 **安装 Bun**：支持多种安装方式，如 curl、npm、PowerShell、Scoop、Homebrew 和 Docker。
- 🔄 **升级 Bun**：使用`bun upgrade`命令轻松升级。
- ⚙️ **并行与顺序运行脚本**：新增`--parallel`和`--sequential`选项，支持并发或顺序执行 package.json 脚本，并带有前缀输出。
- 🌐 **HTTP/2连接升级**：修复了`net.Server`到`Http2SecureServer`的连接升级模式，适用于 HTTP/2 代理服务器。
- 🔧 **Symbol.dispose 支持**：`mock()`和`spyOn()`现在支持`Symbol.dispose`，使用`using`关键字可自动恢复模拟。
- 🛡️ **NO_PROXY 改进**：现在即使显式设置代理选项，`NO_PROXY`环境变量也会被正确检查。
- ⏱️ **CPU 性能分析**：新增`--cpu-prof-interval`标志，可配置 CPU 分析器的采样间隔。
- 📦 **ESM 字节码支持**：`--compile`现在支持 ESM 格式的字节码。
- 🐛 **ARMv8.0 修复**：解决了在旧版 ARM64 处理器上的崩溃问题。
- ⚡ **性能优化**：包括更快的 Markdown 渲染、`AbortSignal.abort()`优化、正则表达式 SIMD 加速等。
- 🔧 **JavaScriptCore 升级**：多项性能改进，如`String#startsWith`、`Set#size`、`Map#size`和`String#trim`的优化。
- 🐞 **错误修复**：包括 Node.js 兼容性改进、Bun API 修复、Web API 问题解决和 TypeScript 类型修正。

---

### [almostnode — 浏览器中的 Node.js](https://almostnode.dev/)

**原文标题**: [almostnode — Node.js in your browser](https://almostnode.dev/)

Next.js 应用在浏览器环境中通过文件路由系统实现客户端渲染。

- 📁 基于文件的路由系统
- 🌐 完全客户端运行
- ⚡ 应用路由器架构

---

### [JavaScript 自我清理即将变得更加轻松 - Piccalilli](https://piccalil.li/blog/its-about-to-get-a-lot-easier-for-your-javascript-to-clean-up-after-itself/)

**原文标题**: [
  It’s about to get a lot easier for your JavaScript to clean up after itself - Piccalilli
](https://piccalil.li/blog/its-about-to-get-a-lot-easier-for-your-javascript-to-clean-up-after-itself/)

JavaScript 即将通过“显式资源管理”提案，让开发者能更轻松地管理资源清理，提升代码的整洁性和可预测性。

- 🧹 提案引入`using`关键字，声明块作用域变量，在其离开作用域时自动调用`[Symbol.dispose]()`方法进行资源清理
- 🔗 标准化`[Symbol.dispose]()`方法，为各种资源（如文件、WebSocket 连接等）提供一致的清理接口
- 🗑️ 解释了“隐式资源管理”，如 WeakSet 和 WeakMap 的弱引用机制，允许垃圾回收自动清理不再使用的对象
- ⏳ 强调垃圾回收的时机不确定，而显式资源管理让开发者能主动控制清理过程
- 🔄 通过生成器对象示例，展示了资源生命周期的概念及`finally`块在清理中的作用
- 🚀 提案已进入标准第三阶段，并获得主流浏览器（除 Safari 外）的支持，鼓励开发者尝试使用
- ⚠️ 提醒语法可能仍有变动，不建议在生产环境中使用，但可通过实验性功能提前体验

---

### [TimescaleDB：PostgreSQL 时序数据库 | 虎数 | 虎数](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB: PostgreSQL Time-Series DB | Tiger Data | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是基于 PostgreSQL 构建的时序数据库，提供自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图、自动化数据管理和专用时序函数等核心功能，适用于物联网、加密货币与金融科技、实时分析等场景。其托管云服务 Tiger Cloud 提供生产就绪的弹性平台，支持数据分层、统一数据架构、按需扩展计算和高可用性，同时提供 24/7 专家支持。

- 🗂️ **自动分区**：通过超表将 PostgreSQL 表按时间或 ID 自动分区，实现快速数据摄取和大规模查询优化。
- 💾 **行列混合存储**：结合行存储和列存储，以低成本保留多年历史数据，并加速分析查询。
- 📉 **高压缩率**：采用列式编码和时序感知压缩，压缩率高达 95%，支持在压缩数据上直接过滤和聚合。
- 🔄 **增量物化视图**：通过连续聚合实现增量刷新的汇总数据，支持实时模式包含最新变更。
- 🤖 **自动化数据管理**：内置任务调度器，可配置列存储、保留和连续聚合策略，提供完整可审计性。
- ⏱️ **专用时序函数**：提供约 200 个原生 SQL 函数，简化高级时序分析，支持统计汇总、时间加权平均等操作。
- 🌐 **应用场景**：适用于物联网传感器监控、加密货币与金融科技数据分析、实时客户仪表板等。
- ☁️ **Tiger Cloud 优势**：提供一键超表创建、数据分层到低成本对象存储、按需计算扩展、多可用区高可用性和安全合规支持。
- 🛠️ **自托管选项**：支持在自有基础设施上安装 TimescaleDB，包含核心功能，但需自行管理云专属特性如水平读取扩展和托管备份。
- 📞 **专家支持**：提供 24/7 技术指导和快速 SLA 响应，涵盖从原型开发到大规模生产的全周期支持。

---

### [Node.js 是单线程的吗？](https://nodesource.com/blog/is-nodejs-single-threaded-or-not)

**原文标题**: [Is Node.js Single-Threaded… or Not?](https://nodesource.com/blog/is-nodejs-single-threaded-or-not)

Node.js 的 JavaScript 执行默认是单线程的，但其运行时通过 libuv 和操作系统利用多线程处理 I/O 和计算密集型任务，从而实现并发。真正的并行 JavaScript 执行需通过 Worker Threads 等机制显式启用。

- 🧵 **JavaScript 执行默认单线程**：V8 引擎只有一个主调用栈，一次仅执行一段 JavaScript 代码。
- 🔄 **运行时多线程架构**：Node.js 通过 libuv 的线程池和操作系统异步 I/O 处理后台任务，避免阻塞主线程。
- ⏱️ **异步操作示例**：如 `setTimeout` 由 libuv 管理定时器，回调仍在主线程执行，保持 JavaScript 执行单线程。
- ⚙️ **计算密集型任务分流**：如 `crypto.pbkdf2` 将耗时计算委托给线程池的工作线程，主线程继续运行其他代码。
- 🧠 **关键区分**：需明确代码执行位置——主调用栈、libuv 委托、操作系统异步处理或显式并行机制。
- 📚 **深入学习建议**：了解事件循环各阶段（定时器、轮询等）可参考 Node.js 官方文档，以全面掌握异步工作机制。

---

### [Transformers.js v4 预览版：现已在 NPM 上发布！](https://huggingface.co/blog/transformersjs-v4)

**原文标题**: [Transformers.js v4 Preview: Now Available on NPM!](https://huggingface.co/blog/transformersjs-v4)

Transformers.js v4 预览版现已发布，带来全新 WebGPU 运行时、性能优化、代码库重构、新模型支持及独立分词器库等重大更新。

- 🚀 **性能与运行时改进**：采用全新 C++ 编写的 WebGPU 运行时，支持浏览器、Node、Bun、Deno 等多环境，并利用 ONNX Runtime 专有算子实现高达 4 倍的速度提升。
- 🏗️ **代码库重构**：使用 PNPM 工作区转为 monorepo 结构，拆分模块化类结构提升可维护性，并将示例移至独立仓库。
- 🛠️ **新构建系统**：从 Webpack 迁移至 esbuild，构建时间缩短 10 倍，默认打包体积减少 53%。
- 🤖 **新模型与架构**：新增 GPT-OSS、Chatterbox、Mamba、MoE 等先进模型，均支持 WebGPU 硬件加速。
- 📦 **独立分词器库**：推出@huggingface/tokenizers，仅 8.8kB 且无依赖，提供完整类型安全的独立分词功能。
- ✨ **其他改进**：增强类型系统与日志控制，支持超过 8B 参数的大模型，并优化离线使用体验。

---

### [发布 v6.7.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v6.7.0)

**原文标题**: [Release v6.7.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v6.7.0)

这是一个关于 Ink 库 v6.7.0 版本发布的 GitHub 页面内容摘要，主要包含版本更新信息和错误提示。

- 🚀 **版本发布**：v6.7.0 版本于 2 月 10 日发布，包含 16 次提交至主分支。
- 🔧 **功能改进**：新增对 React 并发渲染（可选）、同步更新、kitty 键盘协议支持（可选）、IME 光标定位 API 的支持，并改进了终端尺寸检测。
- 🐛 **问题修复**：修复了初始渲染时的全屏尾随换行符、使用多个 `useInput` 钩子时的 `MaxListenersExceededWarning`、卸载时刷新待处理渲染和等待 stdout 耗尽、以及 macOS 上 Option+Return 键处理等问题。
- ⚠️ **页面错误**：页面加载过程中出现错误提示，需要重新加载。
- 📊 **项目状态**：该项目有 34.9k 星标、847 次复刻、44 个议题和 9 个拉取请求。
- 👥 **社区反应**：发布获得了 4 次 🎉 和 5 次 🚀 的反应。

---

### [引言（指南）| VineJS 文档](https://vinejs.dev/docs/introduction)

**原文标题**: [Introduction (Guides) | VineJS Documentation](https://vinejs.dev/docs/introduction)

VineJS 是一个专为 Node.js 设计的表单数据验证库，主要用于验证 HTTP 请求体，它性能优异，提供运行时和静态类型安全，并内置丰富的验证规则和模式类型。

- 🚀 **性能卓越**：VineJS 是 Node.js 生态中最快的验证库之一，性能比 Zod 快 5 到 10 倍。
- 🛡️ **类型安全**：同时提供运行时和静态类型安全，确保数据验证的可靠性。
- 📝 **表单与 JSON 验证**：专门用于验证表单数据和 JSON 载荷，能原生处理 HTML 表单序列化的各种特殊情况（如数字和布尔值被序列化为字符串）。
- 🧩 **功能丰富**：内置 50 多种验证规则和 12 种模式类型，支持数组、对象、联合类型和条件分组等复杂验证。
- 🔧 **高度可扩展**：允许添加自定义验证规则和模式类型，并提供了便捷的测试方式。
- ❌ **使用限制**：VineJS 并非通用验证库，不能用于验证函数、Map、Set 等 JavaScript 数据类型，且仅限在 Node.js 后端环境中使用，无法在浏览器前端直接运行。
- 👥 **维护与赞助**：由 AdonisJS 核心团队维护，最初由 Harminder Virk 创建，是一个独立的开源项目，可通过 GitHub Sponsors 进行赞助以支持其发展。

---

### [发布 JSON 模式支持 · vinejs/vine · GitHub](https://github.com/vinejs/vine/releases/tag/v4.3.0)

**原文标题**: [Release JSON Schema Support · vinejs/vine · GitHub](https://github.com/vinejs/vine/releases/tag/v4.3.0)

VineJS 4.3.0 版本引入了 JSON Schema 支持，允许将验证模式转换为 JSON Schema Draft 7 格式，从而与标准 JSON Schema 验证器和工具实现互操作性。该版本还修复了若干错误，并添加了新功能。

- 📄 **JSON Schema 支持**：VineJS 现在支持将验证模式转换为 JSON Schema Draft 7 格式，便于与其他验证工具集成。
- 🔧 **转换方法**：使用 `.toJSONSchema()` 方法可将任何 VineJS 验证器转换为 JSON Schema。
- 🔗 **与标准验证器兼容**：生成的 JSON Schema 可与 AJV 等标准验证器无缝配合使用。
- 📐 **标准规范遵循**：验证器实现了 `StandardJSONSchemaV1` 规范，增强了与 JavaScript 验证生态系统的集成。
- 🐛 **错误修复**：修复了 `convertEmptyStringsToNull` 标志应用于包含多个空格的字符串时的处理问题，以及可选属性的处理。
- ✨ **新功能**：添加了 `StandardJSONSchema` 支持，并实现了 JSON Schema 支持功能。
- 📈 **版本更新**：从 v4.2.0 升级到 v4.3.0，由贡献者 `@kerwanp` 主导实现。

---

### [铲子 | 介绍铲子](https://shovel.js.org/blog/introducing-shovel/)

**原文标题**: [Shovel | Introducing Shovel](https://shovel.js.org/blog/introducing-shovel/)

Shovel.js 是一个由 AI 辅助开发的开源全栈服务器框架与元框架，旨在让开发者能够像编写浏览器 Service Worker 一样构建和部署 Web 应用，并可在 Node、Bun 和 Cloudflare 等环境中运行。它通过实现浏览器标准 API（如 Cache、FileSystem）并提供配置化全局服务，结合创新的路由、中间件和资源处理机制，提供了一种简洁、标准化且高效的开发体验。

- 🚀 **项目起源**：作者因 Remix 框架放弃 React 而决定自行开发基于 Crank.js 的全栈框架，并借助 Claude Code 在三个月内完成了 Shovel.js。
- 🛠️ **核心理念**：将浏览器 Service Worker 的标准 API（如 Cache、FileSystem、CookieStore）通过垫片实现在服务器运行时，提供一致的开发体验。
- 🌐 **跨平台运行**：支持在 Node.js、Bun 和 Cloudflare Workers 等多种 JavaScript 环境中运行 Service Worker 风格的代码。
- 🧩 **路由与中间件**：内置高性能路由器（基于基数树）和灵活的中间件系统，支持生成器函数实现请求/响应生命周期的清晰控制。
- ⚙️ **配置化全局服务**：通过 `shovel.json` 配置文件统一管理缓存、数据库、文件系统等服务的后端实现（如 Redis、S3、SQLite），代码中通过 `self.caches`、`self.databases` 等标准接口调用。
- 📦 **静态资源处理**：利用 ESBuild 和 import attributes 简化资源引用与打包，无需复杂加载器或文件路由，即可生成带哈希的公共 URL。
- 🔄 **通用渲染模式**：统一处理 SSR、SSG 和 SPA 等渲染策略，例如通过 Service Worker 的 `install` 事件实现静态站点生成。
- 🤖 **AI 辅助开发**：项目全程借助 Claude Code 实现，包括性能优化、标准兼容性测试及新功能（如自定义 DSL、数据库库 ZenDB）的设计与编码。
- 🚧 **早期采用与路线图**：已开放给早期使用者，计划增加会话、认证、WebSocket 等功能，并最终集成类似 Django 的管理界面。

---

### [Service Worker API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)

**原文标题**: [Service Worker API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)

Service Worker API 是一种在 Web Workers 中可用的技术，它作为代理服务器位于 Web 应用、浏览器和网络之间，主要用于创建离线体验、拦截网络请求、更新服务器资源，并支持推送通知和后台同步 API。

- 🛠️ **核心功能**：Service Worker 充当代理服务器，支持离线体验、网络请求拦截和资源更新。
- 🔒 **安全要求**：仅在安全上下文（如 HTTPS 或本地开发环境）中运行，防止中间人攻击。
- 📜 **注册与生命周期**：通过 `ServiceWorkerContainer.register()` 注册，生命周期包括下载、安装和激活阶段。
- ⚡ **异步与事件驱动**：运行在独立线程，无 DOM 访问，完全异步设计，依赖 Promise 处理响应。
- 🗂️ **缓存控制**：使用 Cache 和 CacheStorage API 管理资源缓存，提升离线性能和网络响应。
- 🔄 **更新机制**：新版本在后台安装，待旧版本页面关闭后激活，支持跳过等待和主动声明客户端。
- 🌐 **扩展用例**：包括后台数据同步、跨源请求处理、集中数据更新（如地理位置），以及未来支持的推送消息和地理围栏。
- 📚 **相关接口**：涉及 Cache、ServiceWorker、FetchEvent 等关键 API，扩展了 Window 和 Navigator 对象的功能。

---

### [文员 MCP 服务器](https://clerk.com/changelog/2026-01-20-clerk-mcp-server?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=mcp&utm_content=02-12-26&dub_id=6YbaOYr0nwekZOpA)

**原文标题**: [Clerk MCP Server](https://clerk.com/changelog/2026-01-20-clerk-mcp-server?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=mcp&utm_content=02-12-26&dub_id=6YbaOYr0nwekZOpA)

Clerk 推出 MCP 服务器公开测试版，使 AI 编程助手能直接获取最新的 SDK 代码片段和实施模式，提升开发效率。

- 🚀 Clerk 发布 MCP 服务器公开测试版，为 AI 编程助手提供实时 SDK 支持
- 🤖 兼容 Claude、Cursor 和 GitHub Copilot 等 AI 助手，优化开发体验
- 💡 可查询 Next.js 身份验证钩子、B2B SaaS 权限设置等具体实施问题
- 📚 提供完整设置指南和文档，方便开发者快速接入
- 💬 鼓励用户通过反馈门户和 Discord 社区提供使用意见

---

### [发布 9.5.2 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/releases/tag/9.5.2)

**原文标题**: [Release 9.5.2 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/releases/tag/9.5.2)

该页面显示了一个 GitHub 仓库的发布页面，其中包含版本 9.5.2 的更新详情、错误修复、依赖项更新以及新贡献者的信息。

- 🐛 修复了文档中的 MS 文章 URL 和编号项目引用导出问题
- 📚 更新了编号功能的文档，并添加了完整示例
- 🖋️ 新增了对段落“之间”边框的支持
- 🔧 实现了内容控件功能
- ⬆️ 进行了多项开发依赖项的版本升级
- 👋 欢迎了四位新贡献者的首次贡献

---

### [发布 7.4.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.4.0)

**原文标题**: [Release 7.4.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.4.0)

Prisma 发布了 7.4.0 稳定版本，引入了查询缓存层以提升性能，并新增了对部分索引（筛选索引）的预览支持，同时修复了多项社区贡献的 bug。

- 🚀 新增查询缓存层，通过缓存查询计划减少高并发下的编译开销，提升应用吞吐量
- 📊 支持部分索引（筛选索引），可在 PostgreSQL、SQLite、SQL Server 和 CockroachDB 中创建条件索引以优化性能
- 🐛 修复了多项 bug，包括 PostgreSQL 迁移脚本中 `CREATE INDEX CONCURRENTLY` 的使用问题、MySQL 和 CockroachDB 中 BigInt 精度损失等
- 💼 提供企业支持计划，包括优先问题处理、性能调优和安全合规帮助
- 👥 鼓励社区参与，修复的问题大多来自社区贡献，并开放招聘职位

---

### [GitHub - moscajs/aedes：基于流的轻量级MQTT代理，适用于任何流服务器，采用Node.js方式实现](https://github.com/moscajs/aedes)

**原文标题**: [GitHub - moscajs/aedes: Barebone MQTT broker that can run on any stream server, the node way](https://github.com/moscajs/aedes)

Aedes 是一个轻量级的 MQTT 代理服务器，专为 Node.js 环境设计，可在任何流服务器上运行，支持集群、多种持久化方案和插件扩展，性能优于前身 Mosca。

- 🚀 **核心特性**：兼容 MQTT 3.1/3.1.1，支持 TCP、SSL/TLS、WebSocket，具备消息持久化、自动重连和集群能力。
- 🔌 **扩展灵活**：提供中间件插件系统，支持多种持久化后端（如 MongoDB、Redis）和消息队列发射器。
- 📊 **性能优势**：基准测试显示，在集群配置下，Aedes 的吞吐量显著高于 Mosca，尤其在搭配 MongoDB 持久化与 Redis 发射器时表现最佳。
- 🌉 **桥接支持**：允许 MQTT 桥接协议连接，保留消息的保留标志，适用于分布式部署。
- 🛠️ **生产就绪**：源于 Mosca 的用户反馈，注重稳定性和性能，适用于物联网等高并发场景。
- 📚 **丰富生态**：拥有 CLI 工具、日志模块、统计扩展等，并被多个项目（如 Node-RED、Kuzzle）集成使用。

---

### [GitHub - jeffijoe/awilix：专为Node.JS设计的极其强大的控制反转（IoC）容器](https://github.com/jeffijoe/awilix)

**原文标题**: [GitHub - jeffijoe/awilix: Extremely powerful Inversion of Control (IoC) container for Node.JS](https://github.com/jeffijoe/awilix)

Awilix 是一个为 Node.js 设计的强大、高性能且经过实战检验的依赖注入（DI）容器，使用 TypeScript 编写，旨在帮助开发者编写可组合、可测试的软件，同时无需特殊注解即可实现依赖注入的解耦。

- 🚀 **功能强大**：提供极高性能的依赖注入容器，支持多种注入模式和生命周期管理。
- 🛠️ **灵活使用**：支持通过工厂函数、构造函数和类进行依赖注入，无需依赖特定注解。
- ⚙️ **生命周期管理**：提供三种生命周期（TRANSIENT、SCOPED、SINGLETON），支持作用域缓存和单例模式。
- 🔄 **注入模式**：支持 PROXY（默认）和 CLASSIC 两种注入模式，适应不同开发需求。
- 📦 **自动加载模块**：通过 `loadModules` 自动注册模块，简化大量依赖的手动注册过程。
- 🌐 **浏览器支持**：提供适用于浏览器环境的 UMD 和 ES 模块版本，兼容现代浏览器。
- 🧪 **测试友好**：依赖注入机制使得代码更易于单元测试和模拟。
- 🔧 **严格模式**：提供严格模式以检测潜在的生命周期配置错误，提高代码健壮性。
- 🗑️ **资源清理**：支持通过 `dispose` 方法清理缓存和释放资源，适用于数据库连接池等场景。
- 📚 **丰富生态系统**：拥有多个与流行框架（如 Express、Koa、Fastify）集成的第三方库。

---

### [发布 pnpm 10.29.3 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.29.3)

**原文标题**: [Release pnpm 10.29.3 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.29.3)

pnpm 发布了 10.29.3 版本，主要修复了内存错误、配置选项失效及部署目录问题，并优化了依赖树显示。

- 🐛 修复了在大型依赖图中使用 `pnpm list` 或 `pnpm why` 时可能出现的内存溢出错误，改用两阶段方法构建依赖树，并去重显示重复子树。
- ⚙️ 解决了通过 `.pnpmfile.cjs` 设置的 `allowBuilds` 选项无效的问题。
- 🔗 修正了当启用 `enableGlobalVirtualStore` 时，`pnpm deploy` 错误创建符号链接的问题，现确保部署目录自包含。
- ⏱️ 修复了 `pnpm dlx` 未遵守 `minimumReleaseAgeExclude` 设置的问题。

---

### [错误](https://nodeweekly.com/link/180662/web)

**原文标题**: [Error](https://nodeweekly.com/link/180662/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/180662/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [GitHub - antfu/broz：一款用于截图的简易无边框浏览器](https://github.com/antfu/broz)

**原文标题**: [GitHub - antfu/broz: A simple, frameless browser for screenshots](https://github.com/antfu/broz)

Broz 是一个用于截图的极简无边框浏览器，基于 Electron 构建，提供简洁的界面和便捷的截图功能。

- 🌐 无边框设计，专注于网页截图
- 📸 通过命令行快速启动，例如 `npx broz antfu.me`
- 🖱️ 隐藏的左上角区域支持拖动窗口
- ⌨️ 支持快捷键操作，如关闭窗口和导航
- 🔧 基于 TypeScript 开发，开源且可扩展
- 📈 在 GitHub 上获得 1.1k 星标和 35 个分支

---

### [尸鬼](https://shiki.style/)

**原文标题**: [Shiki](https://shiki.style/)

准确美观的文本编辑器，采用与 VS Code 相同的引擎，并随 VS Code 同步优化提升。

- 🌈 采用与 VS Code 相同的文本语法引擎
- 🎨 提供准确且美观的代码高亮与编辑体验
- 🔄 功能与优化随 VS Code 同步更新提升

---

### [smnx/promethee：适用于JavaScript的UEFI绑定（概念验证）- Codeberg.org](https://codeberg.org/smnx/promethee)

**原文标题**: [smnx/promethee: UEFI Bindings for JavaScript (Proof of Concept) - Codeberg.org](https://codeberg.org/smnx/promethee)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 📊 基于患者数据的个性化治疗方案正成为慢性病管理的新趋势
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任界定等伦理监管问题

---

### [GitHub - svaarala/duktape: Duktape - 专注于可移植性与小巧体积的可嵌入 JavaScript 引擎](https://github.com/svaarala/duktape)

**原文标题**: [GitHub - svaarala/duktape: Duktape - embeddable Javascript engine with a focus on portability and compact footprint](https://github.com/svaarala/duktape)

Duktape 是一个专注于可移植性和紧凑体积的可嵌入 JavaScript 引擎，采用 MIT 许可证，适用于 C/C++ 项目集成。

- 🚀 **可嵌入且轻量**：易于集成到 C/C++ 项目中，只需添加少量文件即可调用 ECMAScript 功能。
- 📜 **符合 ECMAScript 标准**：支持 E5/E5.1，并部分兼容 ES2015+ 特性，包括 TypedArray 等。
- 🔧 **内置工具丰富**：包含调试器、正则表达式引擎、Unicode 支持和模块加载等功能。
- 🌍 **跨平台与开源**：依赖少，支持自定义配置，可通过 vcpkg 安装，社区活跃。
- 🛠️ **开发与维护规范**：提供详细的开发指南、版本管理策略（如语义化版本）和贡献流程。

---

### [路线图 2026 (2026-02-04) | webpack](https://webpack.js.org/blog/2026-04-02-roadmap-2026/)

**原文标题**: [Roadmap 2026 (2026-02-04) | webpack](https://webpack.js.org/blog/2026-04-02-roadmap-2026/)

webpack 团队公布了 2026 年路线图，重点在于提升开发体验、扩展跨运行时支持、简化配置并加强社区与项目可持续性。核心目标包括让 webpack 更易用、更高效，并为其长远发展奠定基础。

- 🎯 **增强开发体验**：计划整合 CSS 模块和 HTML 入口点支持到核心功能中，减少对插件的依赖，并简化资源压缩与 CLI 工具。
- 🌐 **实现跨运行时支持**：致力于新增“universal”目标，使代码能在 Node.js、Deno、Bun 及 Web 等不同环境中无缝运行。
- ⚡ **探索性能优化**：评估引入类似 Rspack 的“惰性 Barrel 优化”以提升构建速度，并设计多线程 API 来利用多核系统。
- 📚 **改进文档与工具**：推动基于类型和模式自动生成准确、最新的 API 与配置文档，确保文档与代码行为一致。
- 👥 **加强社区与可持续性**：通过博客、会议等方式扩大社区参与，并依托 Google Summer of Code 项目培养未来维护者；同时强调捐赠与赞助对项目长期维护的关键作用。
- 🚀 **为 webpack 6 做准备**：通过提升测试与类型覆盖率、增加基准测试以及清理内部代码，为下一代版本打下坚实基础。

---

