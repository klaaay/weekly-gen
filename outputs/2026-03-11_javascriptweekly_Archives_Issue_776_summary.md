### [JavaScript 周刊第 776 期：2026 年 3 月 10 日](https://javascriptweekly.com/issues/776)

**原文标题**: [JavaScript Weekly Issue 776: March 10, 2026](https://javascriptweekly.com/issues/776)

本期 JavaScript 周刊涵盖了 Solid 2.0 测试版发布、TypeScript 6.0 候选版动态、多项工具更新及技术文章分享，聚焦前端生态进展与实用开发资源。

- 🚀 Solid 2.0 测试版发布，引入原生异步支持与优化 API，提供迁移指南
- 📚 TypeScript 6.0 候选版推出，为未来版本升级铺垫配置基础
- 🔧 多项工具更新：Node.js 25.8.0 新增权限审计选项，Astro 6.0 改进开发环境
- 🛡️ 安全警示：GitHub 问题触发 npm 令牌窃取事件与维基百科 JavaScript 蠕虫分析
- 📖 技术实践：Patreon 万行代码 TypeScript 迁移经验与实时待办应用开发教程
- 🧩 新工具推荐：高性能数据网格 RevoGrid、类型验证库 ArkType 2.2 及轻量游戏引擎 melonJS
- 🌐 生态趣闻：浏览器端 Linux 虚拟机 JSLinux 更新支持 x86_64 架构

---

### [发布 v2.0.0 Beta 版 - 悬念终结 · solidjs/solid · GitHub](https://github.com/solidjs/solid/releases/tag/v2.0.0-beta.0)

**原文标题**: [Release v2.0.0 Beta - The `<Suspense>` is Over · solidjs/solid · GitHub](https://github.com/solidjs/solid/releases/tag/v2.0.0-beta.0)

Solid 2.0 已进入 Beta 阶段，标志着该框架在异步处理、状态管理和开发体验方面的重大更新，旨在提供更稳定、可预测的 UI 构建方式。

- 🚀 **异步处理成为核心**：计算可返回 Promise 或异步可迭代对象，框架支持自动挂起与恢复工作流。
- ⏳ **加载状态优化**：`<Loading>` 组件用于初始渲染时的等待，而 `isPending` 则用于指示后台刷新状态，避免 UI 撕裂。
- 🔄 **突变与乐观更新**：引入 `action` 与乐观原语（如 `createOptimisticStore`），简化“乐观更新 → 等待 → 刷新”的数据流。
- 📊 **派生状态原生支持**：通过 `createSignal(fn)` 和 `createStore(fn)` 等函数形式，使派生但可写的状态模式更明确且可组合。
- ⚙️ **更可预测的调度器**：更新采用微任务批处理，读取操作在批处理刷新前不会更新，需手动调用 `flush()` 以立即生效。
- 🛡️ **开发环境防护**：新增开发警告，防止在组件顶层意外读取或在响应式作用域内写入，避免异步错误。
- 🧹 **DOM 模型清理**：移除 `use:` 指令，改用 `ref` 指令工厂函数；`classList` 功能并入 `class` 属性。
- 📝 **迁移与文档重点**：提供详细的迁移指南和 7 个 RFC 文档，涵盖响应式、控制流、存储等核心主题，帮助开发者平滑过渡。
- 🔧 **生态系统更新**：Vite 插件等工具已同步更新，后续将陆续推出更多官方支持。
- 🙏 **社区贡献致谢**：感谢多位贡献者在代码、测试和创意方面的支持，推动此版本发布。

---

### [获取失败](https://javascriptweekly.com/link/181871/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181871/web)

无法总结：获取内容失败，状态码 429。

---

### [时间确定性的架构 - HackMD](https://hackmd.io/@0u1u3zEAQAO0iYWVAStEvw/rJM9ws3Kbg)

**原文标题**: [The Architecture of Temporal Determinism - HackMD](https://hackmd.io/@0u1u3zEAQAO0iYWVAStEvw/rJM9ws3Kbg)

SolidJS 2.0 通过结构性确定性应对 AI 生成代码时代的复杂性，将异步作为值的固有部分，确保代码随时间推移保持正确性，为前端架构提供稳定、可预测的运行时保证。

- 🕒 终结“加载布尔值”时代：引入时间元组，将异步作为值的身份部分，消除 UI 与数据不同步的问题
- 🏗️ 通过构造实现确定性：将“未来”作为信号的一等公民，构建时间线投影架构，从结构上杜绝竞态条件等错误
- 🤖 运行时吸收 AI 生成代码：细粒度响应式将杂乱代码约束为透明可观察图，使糟糕代码也变得可预测
- 🛡️ 稳定性作为战略资产：投资永久原语（如信号、时间线），提供状态随时间流动的数学保证
- 🚀 未来属于确定性系统：在代码指数增长下，依靠运行时不变量的框架将持久存在，Solid 2.0 是为此现实构建的首个框架

---

### [Breaking SolidJS 2.0 Beta - YouTube](https://www.youtube.com/watch?v=-VzCdz7zfPc)

**原文标题**: [Breaking SolidJS 2.0 Beta - YouTube](https://www.youtube.com/watch?v=-VzCdz7zfPc)

该页面为 YouTube 网站底部的通用信息与链接区域，主要包含平台政策、功能说明及公司信息。

- 📄 **关于我们** - 介绍 YouTube 平台的基本信息
- 📢 **媒体联系** - 提供新闻媒体联系渠道
- ©️ **版权声明** - 说明平台版权保护相关内容
- 📧 **联系我们** - 提供用户联系反馈途径
- 🧑‍🎨 **创作者服务** - 面向内容创作者的相关资源
- 📈 **广告合作** - 广告商合作与营销解决方案
- 👨‍💻 **开发者资源** - 开放接口与技术文档
- ⚖️ **使用条款** - 平台服务条款与用户协议
- 🔒 **隐私政策** - 用户数据保护与隐私条款
- 🛡️ **安全政策** - 社区准则与安全措施说明
- ⚙️ **平台运作** - 解释 YouTube 的核心工作机制
- 🧪 **功能测试** - 新功能体验与测试计划说明
- 🏢 **公司信息** - 标注版权所有方及年份信息

---

### [闭包、异步与面向对象：JavaScript 的难点解析 | Frontend Masters](https://frontendmasters.com/courses/javascript-hard-parts-v3/?utm_source=email&utm_medium=javascriptweekly&utm_content=jshardpartsv3)

**原文标题**: [Closure, Async, and OOP: The Hard Parts of JavaScript | Frontend Masters](https://frontendmasters.com/courses/javascript-hard-parts-v3/?utm_source=email&utm_medium=javascriptweekly&utm_content=jshardpartsv3)

本课程深入讲解 JavaScript 中的高阶函数、闭包、异步编程、面向对象编程及元编程等核心难点，帮助开发者构建扎实的底层心智模型，提升代码复用与逻辑表达能力，并培养高级工程师必备的技术沟通能力。

- 🧠 掌握高阶函数与闭包，编写可复用、声明式代码，遵循 DRY 原则
- ⏳ 深入异步机制，理解事件循环、回调队列与微任务队列的运行原理
- 🏗️ 学习面向对象编程，掌握原型继承、类语法及`new`关键字背后的自动化过程
- 🔧 探索类型转换与元编程，使用 Symbol 等工具操控 JavaScript 类型系统
- 📚 课程含 54 节课、9.7 小时内容，评分 4.9，提供结业证书与灵活学习工具
- 👨🏫 由 Codesmith 创始人 Will Sentance 授课，融合十年教育经验与牛津大学研究背景
- 🛠️ 配套学习平台支持进度跟踪、笔记、测验与闪卡，强化知识掌握
- 🌟 受 50 万 + 开发者好评，被誉为理解 JavaScript 底层机制的顶尖课程

---

### [TypeScript 6.0 RC 版本发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

**原文标题**: [Announcing TypeScript 6.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

TypeScript 6.0 RC 已发布，这是基于当前 JavaScript 代码库的最后一次主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本包含多项新特性、改进以及为适应现代开发生态而引入的重大变更和弃用。

- 🚀 **发布候选版本**：TypeScript 6.0 RC 已推出，可通过 `npm install -D typescript@rc` 安装。
- 🔗 **过渡性版本**：作为 TypeScript 7.0 的前置版本，主要变化旨在为迁移到新代码库做准备。
- 🧠 **改进类型推断**：对未使用 `this` 的函数减少了上下文敏感性，提升了方法语法中的类型推断能力。
- 📁 **支持 `#/` 子路径导入**：现在支持以 `#/` 开头的子路径导入，简化了模块别名配置。
- ⚙️ **模块解析组合**：`--moduleResolution bundler` 现在可与 `--module commonjs` 组合使用，为项目升级提供更佳路径。
- 🔧 **稳定类型排序标志**：新增 `--stableTypeOrdering` 标志，使类型排序行为与 7.0 一致，便于版本间对比，但可能降低性能。
- 🎯 **新增 `es2025` 目标**：支持 `target` 和 `lib` 的 `es2025` 选项，包含新的内置 API 类型。
- ⏳ **内置 Temporal API 类型**：为处于 Stage 3 的 Temporal API 提供了内置类型支持。
- 🗺️ **新增 Map 的“upsert”方法类型**：为 `Map` 和 `WeakMap` 新增 `getOrInsert` 和 `getOrInsertComputed` 方法类型。
- 🛡️ **新增 `RegExp.escape`**：提供了 `RegExp.escape` 函数，用于转义正则表达式中的特殊字符。
- 🌐 **DOM 库包含可迭代类型**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容。
- ⚠️ **多项重大变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等，旨在简化编译器并适应现代开发实践。
- 📝 **配置默认值更新**：`rootDir` 默认改为 `.`，`types` 默认改为空数组 `[]`，需根据项目需求显式配置。
- 🚫 **弃用旧语法和选项**：弃用了 `module` 关键字定义命名空间、`asserts` 导入断言语法、`no-default-lib` 指令等。
- ❌ **命令行行为变更**：在存在 `tsconfig.json` 的目录中指定命令行文件将报错，可使用 `--ignoreConfig` 跳过。
- 🔮 **为 7.0 做准备**：建议在升级到 6.0 后尽快解决所有弃用警告，以便顺利过渡到即将发布的 TypeScript 7.0 原生版本。

---

### [TypeScript 6.0 RC 版本发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/#what%E2%80%99s-new-since-the-beta)

**原文标题**: [Announcing TypeScript 6.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/#what%E2%80%99s-new-since-the-beta)

TypeScript 6.0 RC 已发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本包含多项新特性、改进以及为未来版本对齐所做的调整，同时引入了许多破坏性变更和弃用项，以反映现代 JavaScript 生态并提升性能。

- 🚀 **发布候选版本**：TypeScript 6.0 RC 现已可用，可通过 `npm install -D typescript@rc` 安装。
- 🔗 **过渡性版本**：作为 TypeScript 7.0 的前置版本，主要变化旨在为迁移到未来的原生版本做准备。
- 🧠 **改进类型推断**：对于未使用 `this` 的函数，减少了上下文敏感性，提升了泛型函数中方法语法的类型推断能力。
- 📁 **支持 `#/` 子路径导入**：现在支持以 `#/` 开头的 Node.js 子路径导入，简化了项目内部的模块别名配置。
- ⚙️ **模块解析组合**：`--moduleResolution bundler` 现在可与 `--module commonjs` 组合使用，为项目升级提供更合适的路径。
- 🏷️ **稳定类型排序标志**：新增 `--stableTypeOrdering` 标志，使 TypeScript 6.0 的类型排序行为与 7.0 一致，便于版本间对比，但可能会带来性能开销。
- 📅 **支持 ES2025**：新增 `es2025` 作为 `target` 和 `lib` 的选项，更新了内置 API 的类型。
- ⏳ **内置 Temporal API 类型**：为处于 Stage 3 的 Temporal 提案提供了内置类型支持，可通过 `esnext` 或 `temporal.esnext` 使用。
- 🗺️ **新增 Map 的“upsert”方法类型**：为 `Map` 和 `WeakMap` 新增了 `getOrInsert` 和 `getOrInsertComputed` 方法的类型定义。
- 🛡️ **新增 RegExp.escape 类型**：为 `RegExp.escape` 函数提供了类型支持，用于安全地转义正则表达式中的特殊字符。
- 🌐 **DOM 库包含可迭代类型**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **多项破坏性变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等，旨在优化性能并适应现代开发实践。
- 🛠️ **为 7.0 做准备**：TypeScript 6.0 中的弃用项在设置 `"ignoreDeprecations": "6.0"` 后仍可工作，但将在 TypeScript 7.0 中被完全移除，建议用户提前处理。

---

### [获取失败](https://javascriptweekly.com/link/181805/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181805/web)

无法总结：获取内容失败，状态码 429。

---

### [⌚ **第四阶段时间安排** :tada:](https://ptomato.name/talks/tc39-2026-03/)

**原文标题**: [⌚ **Temporal for Stage 4** :tada:](https://ptomato.name/talks/tc39-2026-03/)

Temporal API 提案已满足 TC39 第四阶段的所有准入标准，包括两个兼容实现通过测试、实际部署经验、规范文本整合及编辑组批准，即将进入最终标准化阶段。

- 🎯 **实现与测试**：两个独立实现（SpiderMonkey 和 V8）已通过所有 Test262 测试，达到约 100% 的符合率。
- 🚀 **实际部署经验**：多个浏览器和非浏览器引擎已正式发布 Temporal 支持，社区还开发了多个 polyfill，累计每周下载量超百万。
- 🐛 **反馈与改进**：五年第三阶段中，通过实际使用发现了大量错误和优化机会，并借助快照测试自动识别了 19 个以上实现差异。
- 📜 **规范整合**：已向 ECMA-262 和 ECMA-402 提交合并请求，编辑组正在讨论发布形式，倾向于为 Temporal 设立独立的标准和维护组。
- 🔮 **未来规划**：现有“Temporal V2”收集了 36 项增量改进想法，但暂无成立新工作组计划；现有维护者将继续支持后续提案和问题修复。
- 📊 **项目统计**：规范文本约 1.36 万行，合并 PR 达 1800 个，举行近 200 次 champion 会议，讨论记录相当于 2-3 本小说字数。

---

### [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS 压缩性能基准测试：babel-minify、esbuild、terser、uglify-js、swc、google closure compiler、tdewolff/minify、oxc-minify · GitHub](https://github.com/privatenumber/minification-benchmarks)

**原文标题**: [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS minification benchmarks: babel-minify, esbuild, terser, uglify-js, swc, google closure compiler, tdewolff/minify, oxc-minify · GitHub](https://github.com/privatenumber/minification-benchmarks)

该项目对多个 JavaScript 代码压缩工具进行了性能基准测试，旨在帮助开发者根据压缩效果和速度选择适合的工具。

- 🏆 **最佳压缩工具**：@swc/core 在大型文件上表现最佳，压缩后体积小且速度快，综合性能最优。
- ⚡ **速度冠军**：@cminify/cminify-linux-x64 在几乎所有测试中速度最快，但压缩率相对较低。
- 🥈 **优秀竞争者**：oxc-minify 在速度和压缩率上表现均衡，尤其在大型文件上表现出色。
- 🛠️ **传统强者**：uglify-js 在压缩率上多次领先，但速度较慢；terser 在压缩率和速度间取得了良好平衡。
- ❌ **淘汰工具**：babel-minify 和 tedivm/jshrink 在处理某些文件时出现错误，未能完成所有测试。
- 📊 **测试方法**：使用多种流行 JavaScript 库作为测试样本，比较压缩后大小、Gzip 压缩后大小和压缩时间。
- 🎯 **项目目标**：促进压缩工具间的良性竞争，为开发者提供客观的性能参考数据。

---

### [GitHub - swc-project/swc：基于 Rust 的 Web 平台 · GitHub](https://github.com/swc-project/swc)

**原文标题**: [GitHub - swc-project/swc: Rust-based platform for the Web · GitHub](https://github.com/swc-project/swc)

SWC 是一个基于 Rust 开发的超快速 TypeScript/JavaScript 编译器，旨在提升 Web 开发效率，同时支持 Rust 和 JavaScript 使用。

- 🚀 **高性能编译器**：采用 Rust 编写，编译速度极快，专注于 TypeScript 和 JavaScript 的转换与优化。
- 🔧 **双平台支持**：既可作为 Rust 库使用（通过 parser 等模块），也提供 JavaScript 接口，方便不同开发者集成。
- 📦 **版本管理便捷**：提供脚本帮助 Rust 用户一键更新所有相关依赖至最新兼容版本。
- 🌐 **广泛兼容性**：支持 Node.js v10+ 运行环境，开发则需要 Node.js v20+，确保现代开发流程的顺畅。
- 📖 **完善文档与社区**：提供详细的在线文档、性能对比（如与 Babel）及架构说明，依托活跃社区和志愿者维护。
- 🤝 **开源与贡献友好**：遵循 Apache 2.0 许可证，鼓励开发者通过代码贡献、讨论或资金赞助参与项目发展。

---

### [GitHub - tdewolff/minify: 适用于网页格式的 Go 压缩工具 · GitHub](https://github.com/tdewolff/minify)

**原文标题**: [GitHub - tdewolff/minify: Go minifiers for web formats · GitHub](https://github.com/tdewolff/minify)

Minify 是一个用 Go 语言编写的高性能压缩工具库，支持 HTML5、CSS3、JS、JSON、SVG 和 XML 等多种格式的压缩，通过移除不必要的空白字符和注释来减小文件大小，同时保持功能不变，提升网络传输效率。

- 🚀 **高性能压缩**：在多种基准测试中表现优异，压缩速度通常比其他工具快几个数量级。
- 🌐 **多格式支持**：内置 HTML、CSS、JS、JSON、SVG 和 XML 的压缩器，并可扩展支持其他格式。
- 🔧 **灵活配置**：提供丰富的选项来自定义压缩行为，如保留特定注释、属性值或空白字符。
- 📦 **易于集成**：提供 CLI 工具、Docker 镜像及多种语言绑定（Python、JavaScript、.NET 等），方便不同场景使用。
- 🛡️ **安全可靠**：采用 100% 测试覆盖率及模糊测试，确保代码稳定性和处理各种输入时的安全性。
- 📈 **显著压缩效果**：HTML 压缩约减少 10%，CSS 约 10%-15%，JS 约 35%-65%，有效提升加载速度。
- 🔗 **智能内联资源处理**：可自动压缩 HTML 中内嵌的 CSS、JS 等资源，实现整体优化。
- 🧩 **模块化设计**：允许用户自定义压缩器或调用外部工具（如 Closure Compiler、UglifyJS），增强灵活性。

---

### [GitHub - oxc-project/oxc: ⚓ 一系列高性能 JavaScript 工具集 · GitHub](https://github.com/oxc-project/oxc)

**原文标题**: [GitHub - oxc-project/oxc: ⚓ A collection of high-performance JavaScript tools. · GitHub](https://github.com/oxc-project/oxc)

Oxc 是一个用 Rust 编写的高性能 JavaScript 和 TypeScript 工具集合，旨在提供统一、高效的开发工具链，支持解析、转换、格式化、代码检查和压缩等功能。

- 🚀 **高性能工具链**：Oxc 提供一系列基于 Rust 的高性能工具，包括解析器、转换器、格式化器、代码检查器和压缩器。
- 🛠️ **模块化设计**：各个组件可独立使用，也可组合成完整的工具链，支持灵活的集成和定制。
- 📦 **广泛的应用**：被 Rolldown、Nuxt、Nova、Preact、Shopify 等多个知名项目采用，用于解析、代码检查等场景。
- ⚡ **快速上手**：提供简单的命令行工具，如 `npx oxlint` 进行代码检查，`npx oxfmt` 进行代码格式化，支持快速集成到现有项目。
- 🌐 **社区与贡献**：项目开源并积极欢迎贡献，提供新手任务、Discord 社区支持，并可通过 GitHub Star、社交媒体分享等方式参与。
- 📄 **许可与致谢**：采用 MIT 许可证，感谢 Biome、Ruff 等项目的启发和支持，特别鸣谢项目贡献者和赞助者。

---

### [Eleventy 是一款更简洁的静态网站生成器。](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

Eleventy 是一个简单、快速且灵活的静态网站生成器，支持多种模板语言，无需客户端 JavaScript，提供零配置启动和高度可定制性，拥有活跃的社区和稳定的开发历史。

- 🚀 **快速构建**：Eleventy 在构建速度上表现卓越，处理大量 Markdown 文件时远超其他流行静态站点生成器。
- 🛠️ **灵活多语言支持**：支持 HTML、Markdown、WebC、JavaScript、Liquid、Nunjucks 等众多模板语言，并可混合使用。
- ⚙️ **零配置与高度可定制**：开箱即用，同时允许通过配置文件深度定制项目结构和输出。
- 🌐 **无客户端 JavaScript**：默认不注入任何客户端 JavaScript，注重长期可维护性和渐进增强。
- 📁 **适配现有项目结构**：不强制特定的目录布局，支持增量式迁移，可逐步将现有项目转换为使用 Eleventy。
- 🤝 **活跃与信任的社区**：拥有庞大的用户群和贡献者，被 NASA、Google、Mozilla 等知名机构使用。
- 🔒 **稳定与隐私友好**：版本更新稳定，极少破坏性变更，且不收集用户遥测数据。
- 📚 **全面文档与入门指南**：提供详细的文档、快速入门教程和丰富的学习资源，帮助开发者轻松上手。

---

### [Eleventy 现已更名为 Build Awesome — Eleventy](https://www.11ty.dev/blog/build-awesome/)

**原文标题**: [Eleventy is now Build Awesome — Eleventy](https://www.11ty.dev/blog/build-awesome/)

Eleventy 宣布更名为 Build Awesome，这是其加入 Font Awesome 后的品牌升级，旨在通过 Kickstarter 众筹确保项目的可持续发展。更名后，现有 Eleventy 项目将保持完全兼容，包括插件和构建命令，且 Zach 将继续领导开发。Build Awesome Pro 版本将为开源项目提供更多资源，但免费版功能依旧完整。项目原有的 Open Collective 账户仍用于报销社区开支，但未来支持建议转向 Kickstarter。

- 🚀 Eleventy 更名为 Build Awesome，作为 Font Awesome 旗下项目，通过 Kickstarter 众筹推动可持续发展
- 🔄 更名不影响现有项目，保持与 Eleventy 插件和构建命令的完全兼容，Zach 继续领导开发
- 💡 Build Awesome Pro 将增强开源项目功能，但免费版仍可独立使用，遵循 Awesome 系列商业模式
- 💸 Open Collective 账户继续报销项目开支，但未来支持建议通过 Kickstarter 进行
- 📢 鼓励社区通过 Kickstarter 订阅支持，并可通过 Mastodon 和 Bluesky 向 Zach 提问

---

### [Font Awesome](https://fontawesome.com/)

**原文标题**: [Font Awesome](https://fontawesome.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- ⚙️ 智能医疗管理平台自动化处理行政流程，减轻医护人员行政负担
- 🔬 基因组学与 AI 结合助力精准医疗发展，推动靶向治疗研究
- ⚖️ 数据隐私与算法透明度成为 AI 医疗应用亟待解决的伦理议题

---

### [dotJS | 全球最顶尖的 JavaScript 大会](https://www.dotjs.io/)

**原文标题**: [dotJS | the world's sharpest JavaScript conference](https://www.dotjs.io/)

dotJS 是世界上最顶尖的 JavaScript 会议，将于 2026 年 9 月 18 日在巴黎的 Folies Bergère 剧院举行，为期一天。同期在 9 月 17 日举办 dotAI 会议。会议提供技术演讲和闪电演讲，涵盖 AI、前端、Node.js 等多个领域，并设有合作伙伴展区和社交空间。

- 🗓️ **会议信息**：dotJS 将于 2026 年 9 月 18 日在巴黎 Folies Bergère 剧院举行，dotAI 会议在前一天（9 月 17 日）举行。
- 🎤 **演讲嘉宾**：包括 Node.js 和 Deno 的创建者 Ryan Dahl、全栈开发者 Wes Bos、知名作者 Kyle Simpson 等众多行业专家。
- 💡 **演讲主题**：涵盖在 JavaScript 中运行 AI 模型、前端路由、Web 性能、AI 代理、Node.js 内存管理等前沿技术话题。
- ⚡ **闪电演讲**：多位演讲者将分享关于 Web 性能、物理世界编程、持久化执行、ADHD 与编程等多样主题。
- 🏛️ **会议场地**：位于巴黎市中心的历史剧院 Folies Bergère，提供经典的剧院风格和大型社交空间。
- 📝 **参与方式**：目前开放注册和演讲提案征集（Call for Papers），可单独或同时参加 dotJS 和 dotAI 会议。
- 🤝 **往届反馈**：往届参会者高度评价会议的组织、演讲内容和社交氛围，会议在 2024 年回归后计划于 2025 年 4 月再次举办。

---

### [dotJS | 演讲](https://www.dotjs.io/speak)

**原文标题**: [dotJS | Speak](https://www.dotjs.io/speak)

DOTJS 2026 现正征集演讲提案，这是一个面向全球开发者的高端技术会议，提供专业支持与独特体验，旨在帮助演讲者提升个人品牌与影响力。

- 🎤 在 DOTJS 演讲可获得全球曝光，面向来自欧洲及其他地区的高水平开发者展示专业能力
- 🌟 享受优质演讲环境与专业团队支持，包括 TED 级别的演讲辅导，确保呈现最佳表现
- 📸 获得视频、照片等品牌宣传素材，并得到会议团队的推广支持，有效提升个人品牌
- 🤝 与演讲者、合作伙伴及技术社区建立联系，拓展专业网络
- 📅 演讲提案征集截止时间为 2026 年 4 月 28 日欧洲中部时间下午 6 点，需通过官方表格提交个人信息

---

### [Node.js — Node.js 25.8.0（当前版本）](https://nodejs.org/en/blog/release/v25.8.0)

**原文标题**: [Node.js — Node.js 25.8.0 (Current)](https://nodejs.org/en/blog/release/v25.8.0)

Node.js 25.8.0（Current）版本发布，包含多项功能增强、安全修复和依赖项更新，同时提供了各平台的安装包和二进制文件下载。

- 📄 **文档与构建工具更新**：采用新的 API 文档工具，并修复了构建过程中的 GN 配置问题。
- 🔧 **SQLite 功能增强**：为 DatabaseSync 新增了 limits 属性，扩展了数据库操作能力。
- 🛠️ **诊断与权限审计**：新增 C++ 层面对诊断通道的支持，并引入了`--permission-audit`标志以增强权限审计功能。
- 🧪 **测试框架改进**：在并发测试执行中暴露工作线程 ID，优化了测试运行器的功能。
- 🚀 **性能与安全修复**：优化了 buffer.concat 的性能，修复了 crypto 模块中的多个潜在空指针解引用问题。
- 📦 **依赖项升级**：更新了 undici 至 7.22.0、npm 至 11.11.0、simdjson 至 4.3.1 等多个核心依赖库。
- 🐛 **问题修复与优化**：涵盖了 http、stream、module、repl 等多个模块的错误修复和功能优化。
- 🔗 **多平台支持**：提供了 Windows、macOS、Linux、AIX 等系统的安装程序和二进制文件下载链接。

---

### [src,permission: 从 C++ 发送 dc 消息并使用--permission-audit 由 RafaelGSS · 拉取请求 #61869 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61869)

**原文标题**: [src,permission: emit dc messages from C++ and use --permission-audit  by RafaelGSS · Pull Request #61869 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61869)

该 PR 为 Node.js 添加了 C++ 层级的诊断通道支持，并引入了`--permission-audit`标志，使权限模型在警告模式下运行，通过诊断通道发布权限检查结果而非直接拒绝操作。

- 🔧 **新增 C++ 诊断通道 API**：允许原生代码直接检查订阅者并发布消息，无需跨 JS 边界，提升性能。
- 🚨 **引入`--permission-audit`标志**：启用权限模型的警告模式，权限拒绝时通过诊断通道发送消息并允许操作继续。
- 📡 **权限检查结果发布**：将权限决策发布到按作用域划分的诊断通道（如`node:permission-model:fs`），方便运行时监控。
- 🔄 **替换并扩展先前 PR**：此 PR 取代了#60578，进一步优化了实现方式。
- ✅ **代码审查与合并**：经过团队审查后已成功合并，并包含在 Node.js v25.8.0 版本中。

---

### [权限 | Node.js v25.8.0 文档](https://nodejs.org/api/permissions.html)

**原文标题**: [Permissions | Node.js v25.8.0 Documentation](https://nodejs.org/api/permissions.html)

Node.js 权限模型是一种在运行时限制对特定资源访问的机制，通过 `--permission` 标志启用，可限制文件系统、网络、子进程等操作的访问权限。

- 🛡️ **权限模型概述**：Node.js 权限模型采用“安全带”方法，防止受信任代码无意中更改文件或使用未明确授予访问权限的资源，但不提供针对恶意代码的安全保证。
- 🚫 **启用限制**：启用 `--permission` 后，默认限制对文件系统（`fs` 模块）、网络、子进程、Worker 线程等的访问，需通过特定标志（如 `--allow-fs-read`）显式允许。
- 📁 **文件系统权限**：通过 `--allow-fs-read` 和 `--allow-fs-write` 标志控制文件读写访问，支持使用通配符（`*`）或指定路径来定义允许范围。
- ⚙️ **运行时 API**：启用权限模型后，`process.permission.has()` 方法可用于在运行时检查特定权限（如 `'fs.write'`）。
- 📄 **配置文件支持**：权限设置可通过 Node.js 配置文件（如 `node.config.json`）声明，使用 `permission` 顶级对象配置各项权限，需配合 `--experimental-config-file` 标志使用。
- 🔧 **与 npx 集成**：使用 `npx` 执行脚本时，可通过 `--node-options` 标志传递权限参数（如 `--permission`），但需注意处理可能出现的文件系统读取错误。
- ⚠️ **约束与限制**：权限模型不继承到 Worker 线程，且启用后会限制原生模块、网络等功能；符号链接可能绕过路径限制，需确保授权路径中不包含相对符号链接。

---

### [Astro 6.0 | Astro](https://astro.build/blog/astro-6/)

**原文标题**: [Astro 6.0 | Astro](https://astro.build/blog/astro-6/)

Astro 6.0 正式发布，带来了一系列新功能和改进，包括内置字体 API、内容安全策略 API 以及支持实时内容集合，同时重构了开发服务器和构建管道，提升了开发与生产环境的一致性。

- 🚀 **开发服务器重构**：利用 Vite 新环境 API，开发时可直接运行生产环境，减少“开发正常、生产出错”的问题，尤其优化了对 Cloudflare Workers、Bun 和 Deno 等非 Node.js 运行时的支持。
- 🌐 **增强 Cloudflare 适配**：开发、预渲染和生产阶段均运行 `workerd` 运行时，本地即可使用 Cloudflare 平台 API 和绑定，无需模拟层。
- 🔤 **内置字体 API**：简化自定义字体配置，支持本地文件或 Google 等提供商，自动处理下载、缓存、优化回退字体和预加载链接，提升性能与隐私。
- 📄 **实时内容集合**：稳定功能，支持请求时获取外部托管内容，内容更新即时生效，无需重新构建，可与构建时集合共存。
- 🛡️ **内容安全策略（CSP）**：稳定 API，为静态和动态页面提供内置 CSP 配置，自动哈希脚本和样式，支持自定义指令和算法。
- 📦 **依赖包升级**：包括 Vite 7、Shiki 4、Zod 4，并需 Node.js 22 或更高版本，提升性能和安全性。
- ⚙️ **实验性 Rust 编译器**：替代原有 Go 编译器，速度更快、诊断更强，可通过标志启用，未来计划设为默认。
- ⚡ **实验性队列渲染**：新渲染策略，采用两阶段处理，早期测试显示渲染速度提升高达 2 倍，更高效内存使用。
- 💾 **实验性路由缓存**：平台无关的服务器渲染响应缓存 API，支持设置缓存时长、重新验证窗口和标签，与实时内容集合集成自动失效。
- 👥 **社区贡献**：感谢核心团队及众多贡献者的代码、文档、审查和测试工作，推动 Astro 6 的完善。

---

### [发布版本 3.5.2 · knockout/knockout · GitHub](https://github.com/knockout/knockout/releases/tag/v3.5.2)

**原文标题**: [Release Version 3.5.2 · knockout/knockout · GitHub](https://github.com/knockout/knockout/releases/tag/v3.5.2)

Knockout 3.5.2 版本发布，修复了多个 bug 并新增了 Trusted Types 支持等特性。

- 🐛 修复了 foreach 在某些情况下重复最后条目、bindingEvent.subscribe 在 applyBindings 前调用报错等多个 bug
- 🛡️ 新增 Trusted Types 支持，提升应用安全性
- 🔧 改进了 ko.toJS，保留 bigint 和 symbol 类型
- 📘 优化 TypeScript 类型定义，分离只读与可写计算类型
- 🎯 解决了 IE11 兼容性问题及事件处理相关缺陷

---

### [ESLint v10.0.3 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/03/eslint-v10.0.3-released/)

**原文标题**: [ESLint v10.0.3 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/03/eslint-v10.0.3-released/)

ESLint v10.0.3 是一个补丁版本，主要修复了之前版本中的若干错误，并更新了依赖项和文档。

- 🔧 修复了 minimatch 依赖版本至 ^10.2.4，避免因旧版本 bug 导致 ESLint 无法识别某些文件的问题
- 🐛 修复了 `no-useless-assignment` 规则中未包含变量名的错误消息问题
- 📚 更新了文档，包括添加 v10 迁移指南链接、移除已弃用的 eslintrc 文档文件，并修正了 `no-await-in-loop` 文档中的拼写错误
- 🛠️ 进行了多项维护工作，如简化代码辅助函数、更新配置依赖项，并调整了 Node.js 版本支持要求

---

### [ESLint v9.39.4 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/03/eslint-v9.39.4-released/)

**原文标题**: [ESLint v9.39.4 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/03/eslint-v9.39.4-released/)

ESLint v9.39.4 是一个补丁版本，主要修复了先前版本中的若干错误，并更新了关键依赖以解决安全漏洞和文件识别问题。

- 🔧 修复了 minimatch 依赖版本，设置为 ^3.1.5，避免因旧版本 bug 导致 ESLint 无法识别某些文件的问题
- 🛡️ 更新了 transitive dependency 中的 minimatch 至 ^3.1.5，以修复最近发布的安全漏洞
- 🐛 修复了多个 bug，包括更新 @eslint/eslintrc 至 ^3.3.4 和 ajv 至 6.14.0 以解决安全漏洞
- 📚 文档更新，添加了部分弃用通知
- 🔄 执行了维护任务，如更新依赖和固定 CI 中的 Node.js 版本至 25.6.1

---

### [Ember 6.11 版本发布](https://blog.emberjs.com/ember-released-6-11/)

**原文标题**: [Ember 6.11 Released](https://blog.emberjs.com/ember-released-6-11/)

Ember 6.11 版本发布，这是一个标准的小版本更新，主要包含针对经典构建系统的 bug 修复和开发者体验的细微改进，无新功能引入。

- 🐛 修复了经典构建系统中使用`@ember/reactive`命名空间的 bug，确保其被正确包含在 AMD 包中
- 🎯 优化了 TypeScript 自动补全体验，将`@glimmer/component`的默认导出重命名为 Component，便于编辑器提示
- 🔧 修复了 Ember CLI 中 babel 配置的路径问题，确保装饰器转换运行时模块在 ESM 环境下正确解析

---

### [Ionic Framework 8.8 发布公告 - Ionic 博客](https://ionic.io/blog/announcing-ionic-framework-8-8)

**原文标题**: [Announcing Ionic Framework 8.8 - Ionic Blog](https://ionic.io/blog/announcing-ionic-framework-8-8)

Ionic Framework 8.8 发布，重点增强了组件的可定制性和灵活性，新增了 CSS 类、CSS Shadow Parts 以及模态框和下拉刷新组件的事件，同时为社区驱动的项目提供了更好的支持，以适应最新的 iOS 设计系统和 Material Design 3 主题。

- 🎉 **发布更新**：Ionic Framework 8.8 正式发布，专注于提升组件定制能力。
- 🫳 **模态框拖拽事件**：新增 `ionDragStart`、`ionDragMove`、`ionDragEnd` 事件，支持实时响应拖拽位置、速度和断点变化。
- 🎢 **范围组件双滑块增强**：改进了双滑块行为，新增主机类和 Shadow Parts，支持按身份或位置进行样式定制。
- 🔄 **下拉刷新事件**：新增 `ionPullStart` 和 `ionPullEnd` 事件，提供更详细的拉取生命周期可见性，并弃用旧事件 `ionStart`。
- 🎨 **新增 CSS Shadow Parts 和类**：为 Content、Datetime、Item、List、Range、Select 和 Toast 等组件添加了更多定制选项。
- ✨ **新增和更新属性**：Segment View 新增 `swipeGesture` 属性，Select 新增 `cancelText` 属性，Textarea 的 `disabled` 和 `readonly` 属性现在会反映到主机元素。
- 🅰️ **Angular 注入器支持**：ModalController 和 PopoverController 现在支持传递自定义注入器，便于访问作用域内的依赖。
- 🧩 **Stencil 更新**：Stencil 从 v4.38 升级到 v4.43，包含编译器改进和错误修复。
- 🔮 **展望 Ionic Framework 9**：将引入模块化架构，支持自定义主题和 React Router 6，为更灵活的设计系统奠定基础。

---

### [发布 0.85.0-rc.0 · facebook/react-native · GitHub](https://github.com/facebook/react-native/releases/tag/v0.85.0-rc.0)

**原文标题**: [Release 0.85.0-rc.0 · facebook/react-native · GitHub](https://github.com/facebook/react-native/releases/tag/v0.85.0-rc.0)

React Native 发布了 v0.85.0-rc.0 预发布版本，包含多项重大变更、功能增强、问题修复及底层改进，涵盖 Android 和 iOS 平台。

- 🚨 **重大变更**：移除了已弃用的类型别名、`StyleSheet.absoluteFill` API，并停止支持旧版 Node.js。
- ✨ **新增功能**：为 `Pressable` 组件添加了 `onPressMove` 属性，支持多 CDP 连接，并引入了动画后端示例和文档。
- 🔧 **Android 改进**：重新添加了 `receiveTouches` 方法以兼容生态库，增加了自定义字体查询和开发服务器 IP 配置等功能。
- 🍎 **iOS 改进**：支持 Clang 虚拟文件系统，改进了文本渲染和阴影树同步机制。
- 📝 **更新与重构**：更新了 Metro 版本，重构了部分核心逻辑，并优化了开发工具体验。
- 🗑️ **废弃与移除**：废弃了 `AccessibilityInfo.setAccessibilityFocus` 等方法，并移除了旧架构中的多个类。
- 🐛 **问题修复**：修复了内存泄漏、动画崩溃、图像显示异常、可访问性及构建配置等多个问题。
- 🔒 **安全更新**：更新了 `chromium-edge-launcher` 依赖以移除 `rimraf`。
- 🔄 **底层与工具**：迁移了部分代码到 Kotlin，更新了 Flow 类型，并改进了构建和发布流程。

---

### [发布 pnpm 10.32 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.32.0)

**原文标题**: [Release pnpm 10.32 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.32.0)

pnpm 发布了 10.32.0 版本，包含新增的批准构建功能标志和针对之前问题的修复。

- 🆕 新增 `--all` 标志至 `pnpm approve-builds` 命令，允许无需交互提示即可批准所有待处理构建
- 🔧 撤销了与显式设置 npm 配置文件路径相关的更改，解决了由此引起的回归问题
- 🔧 撤销了与 `lockfile-include-tarball-url` 相关的修复，解决了特定问题
- 📅 版本于 2025 年 3 月 9 日发布，由维护者 zkochan 签名验证

---

### [发布 v3.8.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.8.0)

**原文标题**: [Release v3.8.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.8.0)

Recharts 发布了 v3.8.0 版本，主要引入了 TypeScript 泛型支持以增强图表类型验证，并新增了一系列用于坐标转换和鼠标交互的辅助函数与钩子，同时包含多项功能增强、错误修复及文档更新。

- 🚀 **TypeScript 泛型支持**：为 `data` 和 `dataKey` 属性添加泛型，使图表能通过 TypeScript 进行类型验证。
- 🎯 **坐标系统工具**：新增 `getRelativeCoordinate` 函数及多个钩子（如 `useXAxisScale`、`useYAxisInverseScale`），用于精确处理鼠标交互和坐标转换。
- ✨ **功能增强**：包括图例标签样式支持、X/Y 轴刻度优化（`niceTicks` 属性）、图表事件节流控制等。
- 🐛 **错误修复**：修复了饼图工具提示同步、条形图高亮、动画闪烁及事件处理等问题。
- 📚 **类型定义改进**：为多个组件（如 Bar、Pie、Tooltip）更新了类型定义，提升开发体验。
- 📖 **文档与示例更新**：新增 Treemap 嵌套、瀑布图工具等文档，并优化了暗模式示例。
- 👏 **社区贡献**：版本由 PavelVanecek 等 13 位贡献者共同完成，其中包含 10 位新贡献者的首次提交。

---

### [发布 v30.3.0 · jestjs/jest · GitHub](https://github.com/jestjs/jest/releases/tag/v30.3.0)

**原文标题**: [Release v30.3.0 · jestjs/jest · GitHub](https://github.com/jestjs/jest/releases/tag/v30.3.0)

Jest 发布了 v30.3.0 版本，包含新功能、错误修复及维护更新。

- 🆕 新增 `defineConfig` 和 `mergeConfig` 助手函数，用于类型安全的 Jest 配置
- ⏱️ 添加 `setTimerTickMode` 以配置计时器推进方式
- 🧠 优化通过大型语言模型运行时的令牌使用量
- 🐛 修复了使用 `--json` 和 `--outputFile` 时 CLI 覆盖率输出的问题
- 🔧 解决了控制台输出在特定条件下不显示的问题
- 📦 修复了动态导入和失败测试重新执行的相关问题
- 🛠️ 将剩余 micromatch 替换为 picomatch，并更新了依赖项
- 📚 更新了迁移指南和文档，以反映最新变更

---

### [获取失败](https://javascriptweekly.com/link/181829/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181829/web)

无法总结：获取内容失败，状态码 403。

---

### [使用 Jazz 与 Vue 3 构建实时待办事项应用 | alexop.dev](https://alexop.dev/posts/building-real-time-todo-app-jazz-vue/)

**原文标题**: [Building a Real-Time Todo App with Jazz and Vue 3 | alexop.dev](https://alexop.dev/posts/building-real-time-todo-app-jazz-vue/)

本文介绍了如何使用 Jazz 和 Vue 3 构建一个实时、离线可用的待办事项应用。Jazz 通过其协作数据结构 CoValues 替代了传统后端，实现了跨设备、跨用户的实时同步，无需服务器支持。应用支持拖拽排序、共享链接，并集成了 Jazz Inspector 用于调试。

- 🚀 **Jazz 替代后端**：使用 CoValues 实现实时协作、离线支持和共享链接，无需构建同步服务器或 API。
- 🔧 **核心工具**：结合`community-jazz-vue`库，提供如`useCoState`的组合式函数，直接集成到 Vue 的响应式系统中。
- 🔐 **权限管理**：通过 Jazz Groups 控制数据访问权限，支持角色层级和端到端加密，确保数据安全。
- 📱 **应用功能**：构建的待办应用支持实时同步、离线操作、拖拽排序（基于分数索引）、动态页面标题和可共享 URL。
- 🛠️ **开发步骤**：从项目初始化、定义 CoValue 模式、设置 Jazz 提供者，到实现 CRUD 操作和拖拽排序，详细展示了构建流程。
- 🌐 **同步机制**：数据变更通过 Jazz Cloud 同步，支持多标签页和设备间的实时更新，且在网络断开时仍可本地操作。
- 📖 **扩展资源**：提供了 Jazz 官方文档、社区 Vue 绑定库的链接，以及完整示例项目的 GitHub 仓库。

---

### [爵士——同步数据库。](https://jazz.tools/)

**原文标题**: [Jazz - The database that syncs.](https://jazz.tools/)

Jazz 是一个分布式数据库，能够在前端、容器、函数和全球自动扩展的云存储之间同步数据、文件和 LLM 流，使用方式类似于响应式本地 JSON 状态。它开源且支持自托管，旨在简化现代应用的开发，提供离线优先、实时同步和内置权限管理等核心功能。

- 🗄️ **分布式数据库**：Jazz 是一个分布式数据库，可在前端、容器、函数和云存储之间运行，实现数据、文件和 LLM 流的即时同步。
- 🔄 **即时同步与离线支持**：提供离线优先体验，数据在重新连接后自动同步，UI 更新无需 API 调用，实现实时协作。
- 🔒 **隐私与安全**：数据在设备端加密和签名，服务器不可见，支持用户权限管理，确保隐私安全。
- 🛠️ **开发友好**：开源（MIT 协议）且支持自托管，与 JavaScript、React、Svelte 等框架兼容，简化共享状态管理。
- 📁 **文件与媒体处理**：支持文件上传、渐进式图像加载，并可轻松转换为浏览器 Blob，提升媒体处理效率。
- ☁️ **云服务与定价**：提供 Jazz Cloud 云服务，包括免费 Starter 套餐及付费 Indie、Pro 和企业级方案，支持弹性扩展。
- 🤝 **团队与支持**：拥有活跃的开发团队和社区支持，提供文档、Discord 交流及企业级定制服务。

---

### [设置 Next.js 源映射 - 可读堆栈跟踪 | Sentry](https://blog.sentry.io/setting-up-next-js-source-maps-sentry/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjs&utm_content=newsletter-sponsored-link-sourcemaps-blog-learnmore)

**原文标题**: [Setting up Next.js source maps - Readable stack traces | Sentry](https://blog.sentry.io/setting-up-next-js-source-maps-sentry/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjs&utm_content=newsletter-sponsored-link-sourcemaps-blog-learnmore)

Next.js 应用在构建过程中会将源代码编译、压缩并分割成多个代码块，这虽然提升了性能，但导致错误堆栈难以阅读。通过配置 Sentry 上传源映射（source maps）和调试 ID（debug IDs），可以将生产环境中的错误堆栈映射回原始代码，从而在 Sentry 中显示可读的文件名和行号。

- 🛠️ Next.js 构建流程将 React 和 TypeScript 代码编译、压缩并分割成多个代码块，优化性能但增加调试难度。
- 🗺️ 源映射和调试 ID 帮助 Sentry 将压缩后的错误堆栈映射回原始代码，显示真实的文件名和行号。
- 🔍 开发环境中浏览器可直接访问源映射，但 Sentry 需要上传源映射才能正确解析错误堆栈。
- 🚀 本地开发建议使用 Spotlight 工具，避免调试噪音占用 Sentry 配额，保留 Sentry 用于生产环境问题。
- 🏗️ 通过运行`npm run build`和`npm run start`模拟生产构建，触发 Sentry 自动上传源映射。
- 📤 Sentry 在构建过程中收集代码块和源映射并上传，完成后删除源映射以避免泄露源代码。
- ✅ 验证源映射配置：在生产构建后触发错误，检查 Sentry 中的堆栈是否指向原始代码文件。
- ⚙️ 若源映射未生效，检查 Sentry 配置、环境变量，并尝试删除旧源映射后重新构建上传。
- ❓ 常见问题包括代码块名称变化导致重复错误、Turbopack 和 Webpack 的自动支持，以及本地开发使用 Spotlight 的建议。
- 📚 如遇问题，可参考 Next.js 源映射文档、故障排除指南，或通过 Discord 和 Sentry 沙箱获取帮助。

---

### [如何通过开启 GitHub 议题窃取 npm 发布令牌 — Neciu Dan](https://neciudan.dev/cline-ci-got-compromised-here-is-how)

**原文标题**: [How to steal npm publish tokens by opening GitHub issues — Neciu Dan](https://neciudan.dev/cline-ci-got-compromised-here-is-how)

2026 年 3 月 4 日，Cline CLI 工具因一系列漏洞和巧妙的攻击策略遭到入侵，攻击者通过 GitHub 问题窃取了 npm 发布令牌，并发布了包含恶意代码的 cline@2.3.0 版本。该版本在 npm 上存活了 8 小时，约有 4000 次安装。攻击利用了 Cline 仓库中 AI 问题分类机器人的提示注入漏洞，结合 GitHub Actions 缓存污染技术，最终窃取了高权限工作流中的 npm 令牌。文章详细分析了攻击链，并提供了防护建议。

- 🐛 攻击者通过 GitHub 问题标题的提示注入，在 Cline 的 AI 分类机器人工作流中执行任意命令
- 🔓 利用 GitHub Actions 缓存共享机制，攻击者污染了缓存，导致夜间发布工作流加载了恶意 node_modules
- 🛡️ 恶意代码从高权限工作流中窃取了 npm 发布令牌，并发布了包含 OpenClaw 安装脚本的 cline@2.3.0
- ⚠️ 被植入的 OpenClaw 虽非恶意软件，但其网关服务存在身份验证绕过漏洞，可能威胁 CI 环境安全
- 🔧 建议禁用 npm 生命周期脚本、在 CI 中使用 npm ci 而非 npm install，并运行 npm audit signatures 检查来源
- 📚 作者提供了免费安全课程，涵盖攻击原理、防御层、安全工具及事件响应等内容

---

### [维基百科遭自称可自我传播的 JavaScript 蠕虫攻击，页面遭恶意篡改](https://www.bleepingcomputer.com/news/security/wikipedia-hit-by-self-propagating-javascript-worm-that-vandalized-pages/)

**原文标题**: [Wikipedia hit by self-propagating JavaScript worm that vandalized pages](https://www.bleepingcomputer.com/news/security/wikipedia-hit-by-self-propagating-javascript-worm-that-vandalized-pages/)

维基媒体基金会遭遇一起自我传播的 JavaScript 蠕虫攻击，导致用户脚本被篡改和 Meta-Wiki 页面遭破坏。该事件源于一个潜伏两年的恶意脚本被意外激活，在 23 分钟内篡改了约 3,996 个页面并感染了 85 名用户的脚本。基金会已紧急修复并恢复编辑功能，确认无用户数据泄露。

- 🐛 自我传播的 JavaScript 蠕虫通过篡改全局和用户脚本扩散，在维基媒体平台引发连锁感染
- ⏰ 恶意脚本潜伏两年后，在安全审查中被意外激活，仅活跃 23 分钟即被控制
- 🔧 攻击同时针对用户级脚本和全站脚本，实现双重持久化感染机制
- 📄 蠕虫自动编辑随机页面，插入隐藏的 JavaScript 加载器和干扰性图片
- 🛡️ 维基媒体工程师紧急限制全平台编辑功能，逐项清除恶意代码并恢复用户脚本
- 📊 事后统计显示约 3,996 个页面被修改，85 名用户脚本遭替换，仅 Meta-Wiki 受影响
- 🔍 基金会强调此次为内部安全审查引发的意外事件，并非外部攻击，无数据泄露风险
- 📝 正在制定额外安全措施防止类似事件，完整事件报告尚未发布

---

### [如何使用 JavaScript 解码车辆识别码](https://cardog.app/blog/vin-decoder-javascript)

**原文标题**: [How to Decode a VIN in JavaScript](https://cardog.app/blog/vin-decoder-javascript)

本文介绍了在 JavaScript 中解码车辆识别号码（VIN）的三种方法，分别适用于不同场景，并提供了代码示例和性能对比，帮助开发者根据需求选择合适方案。

- 🚗 **VIN 解码应用场景**：用于库存管理、估值工具、合规检查、零件匹配、车队管理和移动应用等，可自动提取车辆品牌、型号、年份和规格信息。
- 📦 **离线解码方案**：使用@cardog/corgi 包，提供亚 15 毫秒的查询速度，无需网络依赖，适合高流量、低延迟或隐私敏感的应用，但需下载约 20MB 数据库。
- 🌐 **在线解码方案**：通过 Cardog API 获取丰富数据，包括市场情报、召回状态和估值信息，适合需要实时数据或快速原型开发的项目，但存在网络延迟。
- ⚙️ **原始 NHTSA API**：免费但响应慢（2-3 秒），字段名称不一致，适合调试或一次性脚本，不建议用于生产环境或高流量场景。
- ⚡ **性能对比**：Corgi 比原始 NHTSA API 快约 100 倍，Cardog API 居中，推荐大多数项目从 Corgi 开始，需要增强数据时再结合 Cardog API。
- 🔧 **实践示例**：展示了结合 Corgi 和 Cardog API 构建 VIN 扫描器的代码，支持离线快速解码和在线数据增强，提高应用鲁棒性。

---

### [车辆识别号码 - 维基百科](https://en.wikipedia.org/wiki/Vehicle_identification_number)

**原文标题**: [Vehicle identification number - Wikipedia](https://en.wikipedia.org/wiki/Vehicle_identification_number)

车辆识别码（VIN）是国际标准化组织（ISO）制定的一套全球统一的车辆身份识别系统，用于唯一标识汽车、摩托车等机动车辆。它由 17 位字符组成，包含世界制造商标识、车辆描述信息和车辆标识信息，能够提供车辆的生产地区、制造商、车型年份、装配厂及生产序列号等关键数据。

- 🌍 **全球标准**：VIN 遵循 ISO 3779 和 ISO 3780 国际标准，确保全球车辆身份识别的统一性和唯一性。
- 📅 **历史演变**：VIN 于 1954 年在美国首次使用，1981 年美国国家公路交通安全管理局（NHTSA）将其标准化为 17 位字符格式，并沿用至今。
- 🔢 **结构解析**：17 位 VIN 分为三部分：前 3 位是世界制造商标识（WMI），中间 6 位是车辆描述信息（VDS），最后 8 位是车辆标识信息（VIS）。
- 🌐 **地区编码**：VIN 的首位字符代表生产地区，如 1-5 为北美，J 为日本，W 为德国，L 为中国等。
- 🏭 **制造商识别**：前三位 WMI 代码由 SAE 分配，可识别车辆制造商及生产国家，例如“1G1”代表美国雪佛兰轿车。
- 📅 **车型年份**：北美地区 VIN 的第 10 位字符表示车型年份，采用字母和数字循环编码（如 2001 年为 1，2010 年为 A）。
- 🔍 **校验机制**：北美和中国地区的 VIN 包含第 9 位校验码，用于验证 VIN 的准确性，防止伪造或错误。
- 📍 **生产信息**：第 11 位字符表示装配厂代码，最后 6 位是车辆的生产序列号，确保每辆车具有唯一标识。
- 🛠️ **实际应用**：VIN 通常标注在挡风玻璃左下角、发动机舱内、车门柱等位置，可用于车辆历史查询、防盗及保险评估。

---

### [使用原生 JavaScript 构建异步页面过渡效果 | Codrops](https://tympanus.net/codrops/2026/02/26/building-async-page-transitions-in-vanilla-javascript/)

**原文标题**: [Building Async Page Transitions in Vanilla JavaScript | Codrops](https://tympanus.net/codrops/2026/02/26/building-async-page-transitions-in-vanilla-javascript/)

本文介绍了如何使用原生 JavaScript、GSAP 和 Vite 构建一个轻量级单页面应用（SPA）路由系统，实现异步交叉淡入淡出页面过渡效果，无需依赖任何前端框架。

- 🛠️ **项目概述**：通过克隆页面容器、同时动画化新旧页面并最终移除旧容器，实现真正的交叉淡入淡出过渡效果。
- 📁 **项目结构**：使用 Vite 初始化项目，创建页面模块（HTML 和 JS 文件）和路由定义，每个路由映射到对应的命名空间和动态导入函数。
- 🧭 **路由管理**：创建 Router 类拦截链接点击，使用 History API 管理导航，并通过事件委托处理全局点击事件。
- 🎬 **过渡引擎**：利用 GSAP 创建动画时间线，实现当前页面向上淡出、新页面从底部剪切入场的同步动画效果。
- 🔄 **异步过渡流程**：在过渡期间，新旧页面容器同时在 DOM 中共存，动画完成后清理旧容器并重置样式。
- 🚀 **页面进入动画**：为增强用户体验，添加标题元素的进入动画，并在页面初始化时调用。
- 📈 **扩展可能性**：系统支持进一步扩展，如页面生命周期钩子、中止过渡、预加载和元标签更新等功能。

---

### [适用于 Vue、React、Angular、Svelte 和 JavaScript 的高性能数据网格 | RevoGrid](https://rv-grid.com/)

**原文标题**: [High-Performance Data Grid for Vue, React, Angular, Svelte, and JavaScript | RevoGrid](https://rv-grid.com/)

快速构建优雅高效的数据表格。轻量而强大的架构让您能轻松应对需求增长。

- 🚀 快速构建优雅高效的数据表格
- 🏗️ 轻量而强大的架构设计
- 📈 轻松扩展以满足增长需求

---

### [数据网格演示 - Vue、Angular、React 与 Svelte | RevoGrid](https://rv-grid.com/demo/)

**原文标题**: [Data Grid Demo - Vue, Angular, React, and Svelte | RevoGrid](https://rv-grid.com/demo/)

该页面介绍了 RevoGrid 数据表格组件的核心特性、兼容性及框架支持信息。

- 🚀 **性能卓越**：支持海量数据平滑滚动，性能强劲。
- 🛠️ **简单易用**：提供丰富示例，完美支持 TypeScript，上手门槛低。
- ⚡ **功能强大**：内置拖拽、公式计算、主行操作和 CRUD 功能，支持深色模式与数据导入导出。
- 🔄 **框架通用**：API 设计保持跨框架一致性，便于知识迁移与复用。
- 📚 **多框架支持**：提供 Angular、React、Svelte、Vue 2/3 等主流框架的集成指南。

---

### [GitHub - revolist/revogrid：功能强大的虚拟数据表格，具备高级自定义功能。集Excel最佳特性与卓越性能于一身 🔋 · GitHub](https://github.com/revolist/revogrid)

**原文标题**: [GitHub - revolist/revogrid: Powerful virtual data table smartsheet with advanced customization. Best features from excel plus incredible  performance 🔋 · GitHub](https://github.com/revolist/revogrid)

RevoGrid 是一个基于 StencilJS 构建的高性能数据表格组件，支持处理数百万单元格和数千列，提供类似 Excel 的功能和丰富的自定义选项，适用于多种前端框架。

- 🚀 **高性能核心**：能处理视口中数百万单元格，内置智能虚拟 DOM 和虚拟滚动以优化渲染。
- ♿ **无障碍支持**：遵循 WAI-ARIA 最佳实践，提供全面的键盘导航和 RTL 语言支持。
- 🧩 **丰富功能**：包括排序、筛选、分组、单元格合并、公式计算、数据透视表及插件系统等。
- 📦 **轻量且跨框架**：初始包体积小，支持 React、Angular、Vue 2/3、Svelte 及纯 JavaScript 项目。
- 🛠️ **高度可定制**：允许自定义单元格模板、编辑器、主题，并提供行/列拖放、固定元素等高级操作。
- 🔄 **持续更新**：通过 GitHub Actions 实现多框架持续交付，并计划转向 monorepo 开发模式。
- 📄 **开源与赞助**：采用 MIT 许可证，提供专业版选项，欢迎社区贡献和赞助以支持项目发展。

---

### [核心 3](https://clerk.com/changelog/2026-03-03-core-3?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=core-3&utm_content=03-10-26&dub_id=FF6WjIn8CnxdHCRK)

**原文标题**: [Core 3](https://clerk.com/changelog/2026-03-03-core-3?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=core-3&utm_content=03-10-26&dub_id=FF6WjIn8CnxdHCRK)

Clerk 发布了其 SDK 的最新主要版本 Core 3，重点改进了自定义 API、主题编辑器、无密钥模式支持、现代 React 兼容性和性能优化。

- 🛠️ **改进的自定义 API**：重新设计了`useSignIn`、`useSignUp`和`useCheckout`钩子，并新增`useWaitlist`钩子，简化了自定义身份验证界面的构建。
- 🎨 **主题编辑器与交互式文档**：新增可视化主题编辑器，可实时调整预构建组件的样式，并支持在文档中直接预览和复制代码。
- 🔑 **扩展的无密钥模式支持**：无密钥模式现已支持 TanStack Start、Astro 和 React Router 框架，方便快速尝试和集成。
- ⚛️ **现代 React 兼容性**：优化了与 React 并发功能（如过渡、Suspense 和流式 SSR）的兼容性，避免了状态同步冲突。
- 🚀 **性能提升**：包括更小的捆绑包体积、更快的卫星域名处理、优化的离线处理以及后台令牌自动刷新。
- 📦 **简化与更新**：统一了包名（如`@clerk/react`），引入了`<Show>`组件替代多个旧组件，并增加了自动主题切换、Vite 环境变量检测等新功能。
- 📄 **其他改进**：包括前端 API 代理支持、类型子路径导出、Next.js 缓存组件支持，以及新的组件更新日志。
- ⚠️ **弃用说明**：弃用了 Clerk Elements 和`@clerk/types`包，建议使用新的钩子和集成类型。

---

### [ArkType 2.2 正式发布](https://arktype.io/docs/blog/2.2)

**原文标题**: [Announcing ArkType 2.2](https://arktype.io/docs/blog/2.2)

ArkType 2.2 版本发布，引入了类型安全的运行时验证函数、正则表达式、双向 JSON Schema 支持以及通用模式互操作性，显著增强了类型安全性和开发体验。

- 🎯 **类型安全函数验证** – 新增 `type.fn` 支持运行时验证参数和返回类型，适用于纯 JavaScript 文件，无需 TypeScript 注解。
- 🔍 **类型安全正则表达式** – 集成 `arkregex`，正则字面量支持完整类型推断，包括捕获组，通过 `x` 前缀启用运行时解析。
- 🔄 **双向 JSON Schema 转换** – 新包 `@ark/json-schema` 支持 JSON Schema 与 ArkType 类型间的双向转换，增强互操作性。
- 🧩 **通用模式互操作** – 可直接在定义中嵌入任何符合 Standard Schema 的验证器（如 Zod、Valibot），实现跨生态组合。
- 🧠 **深层类型内省** – 新增 `select` 方法用于查询类型内部结构，支持按节点类型和谓词进行精细配置。
- 📝 **改进的类型声明** – `type.declare` 支持形态感知声明和可选性表达，提供更清晰的错误提示。
- 📊 **可序列化错误** – `ArkErrors` 现在可 JSON 序列化，便于 API 响应和日志记录，新增结构化访问属性。
- ⚙️ **多元操作符** – `type.or`、`type.and` 等支持可变参数，避免链式调用，简化联合、交叉等类型操作。
- 🔗 **字符串内嵌管道操作符** – `|>` 操作符可直接在字符串定义中使用，简化类型转换链。
- 🆕 **新增内置关键字** – 引入 `string.hex` 和 `string.regex` 关键字，分别用于验证十六进制字符串和正则表达式语法。
- ⚡ **性能与兼容性优化** – 包括 ES2020/Hermes 兼容性、更快的自动补全、循环联合类型改进等多项增强。

---

### [微基](https://tinybase.org/)

**原文标题**: [TinyBase](https://tinybase.org/)

TinyBase 是一个轻量级、响应式的本地优先数据存储与同步引擎，最新版本 v8.0 支持对象、数组和中间件。它提供键值对和表格化数据存储，具备模式约束、索引、关系、查询和聚合功能，并内置 CRDT 实现多端同步。TinyBase 体积小巧（6.2–13.2 kB），无依赖，完全支持 TypeScript，可轻松与 React 集成，提供持久化、撤销重做和开发者工具，适用于快速构建离线可用的本地优先应用。

- 🚀 **响应式数据监听** – 监听数据变化，实现高效渲染，支持 React 绑定和预置组件，内置撤销栈和开发者工具。
- 🗃️ **数据库式数据建模** – 支持键值对和表格化数据，提供模式约束、索引、关系、聚合和类 SQL 查询引擎（TinyQL）。
- 🔄 **多端同步与持久化** – 内置 CRDT 支持跨客户端、服务器同步，可持久化到浏览器存储、IndexedDB、SQLite、PostgreSQL 等。
- 📱 **本地优先设计** – 专为离线应用优化，体积小（6.2–13.2 kB）、无依赖、100% 测试覆盖，完全开源且文档齐全。
- ⚛️ **React 深度集成** – 提供 useCell 等 Hooks 和预置 UI 组件，简化响应式界面开发，支持数据检查器实时编辑。
- 🛠️ **丰富扩展功能** – 包含指标聚合、索引、关系、检查点（撤销重做）、模式验证（支持 Zod 等库），以及多种持久化方案。
- 📦 **轻量与高性能** – 核心模块仅 6.2 kB，可选功能渐进增加，所有模块均经过全面测试，适用于各类 JavaScript 环境。

---

### [架构选项 | TinyBase](https://tinybase.org/guides/the-basics/architectural-options/)

**原文标题**: [Architectural Options | TinyBase](https://tinybase.org/guides/the-basics/architectural-options/)

TinyBase 提供了多种架构选项，用于在应用中集成数据存储、持久化和同步功能，可根据应用需求灵活选择。

- 🚀 **独立使用**：数据仅存在于内存中，适合原型开发，但刷新或关闭后数据丢失。
- ☁️ **只读云端数据**：启动时从服务器加载数据到内存，适合数据参考类应用，但数据不可交互保存。
- 💾 **浏览器存储**：将数据持久化到浏览器本地存储或会话存储，支持页面重载和会话恢复，但仅限于单一设备。
- 🗄️ **客户端数据库存储**：使用 SQLite 等客户端数据库进行结构化持久化，减少数据被清除的风险，但需加载 WASM 增加资源体积。
- 🔄 **仅客户端同步**：通过 MergeableStore 和 Synchronizer 在客户端间同步数据，支持多设备共享，但缺乏中心化数据源。
- 🌐 **客户端 - 服务器同步**：服务器作为数据源协调客户端同步，提供更可靠的数据持久化和完整性保障。
- 🔗 **第三方同步**：集成如 ElectricSQL、PowerSync 等第三方同步平台，可避免供应商锁定，但增加复杂性和潜在费用。

---

### [发布 | TinyBase](https://tinybase.org/guides/releases/#v8-0)

**原文标题**: [Releases | TinyBase](https://tinybase.org/guides/releases/#v8-0)

TinyBase 发布了多个版本更新，引入了新功能并改进了现有功能，包括支持对象和数组类型、中间件系统、状态钩子、参数化查询、模式转换器、空值支持、持久化与同步增强、React 集成优化以及工具模块的引入。

- 📦 **v8.0**：新增对象和数组类型支持，引入中间件系统用于数据验证和转换。
- ⚛️ **v7.3**：引入状态钩子，简化 React 组件中的数据读写操作。
- 🔍 **v7.2**：新增参数化查询功能，提升查询灵活性和效率。
- 🔧 **v7.1**：引入模式转换器，支持从外部验证库转换模式。
- 🆕 **v7.0**：支持空值类型，优化数据库持久化处理。
- 💾 **v6.7**：新增 OPFS 持久化支持，适用于浏览器环境。
- 🛠️ **v6.6**：改进检查工具，支持直接编辑和操作数据。
- 📱 **v6.5**：新增 React Native MMKV 持久化模块。
- 🗄️ **v6.4**：新增 React Native SQLite 持久化模块。
- ☁️ **v6.3**：新增 Cloudflare Durable Object SQL 存储持久化模块。
- 📦 **v6.2**：引入 omni 模块，优化打包和导出结构。
- 🐰 **v6.1**：新增 Bun SQLite 持久化，支持子集持久化和对象参数解构。
- 🔄 **v6.0**：更新依赖和基础设施，移除 CJS 和 UMD 包，支持 React 19。
- 🤝 **v5.4**：新增 Durable Objects 同步和持久化支持。
- ⚙️ **v5.3**：改进 API，支持 React SSR，新增状态监听器。
- 🐘 **v5.2**：新增 PostgreSQL 持久化模块。
- 🖥️ **v5.1**：新增服务器端持久化支持，改进同步器回调。
- 🔀 **v5.0**：引入可合并存储和同步器框架，优化模块结构。
- ⚡ **v4.8**：新增 PowerSync 持久化模块。
- 🌐 **v4.7**：新增 LibSQL 持久化模块。
- 🔌 **v4.6**：新增 ElectricSQL 持久化模块。
- 📱 **v4.5**：新增 Expo SQLite 现代版本持久化模块。
- 👁️ **v4.4**：新增存在性监听器，优化数据监听功能。
- 🎉 **v4.3**：新增 PartyKit 集成，支持云端协作。
- 💾 **v4.2**：新增 IndexedDB 持久化支持。
- 🖥️ **v4.1**：新增 DOM 组件和检查工具，优化 UI 开发。
- 🗃️ **v4.0**：新增 SQLite 和 CRDT 持久化模块，改进事务处理。
- 📊 **v3.3**：新增表级单元格 ID 跟踪功能。
- 🔄 **v3.2**：新增事务开始监听器，支持数据变更前处理。
- 📝 **v3.1**：引入基于模式的类型系统，优化 TypeScript 支持。
- 🔑 **v3.0**：新增键值存储功能，支持值类型数据操作。
- 🛠️ **v2.2**：引入工具模块，支持 API 和模式生成。
- 🔍 **v2.1**：支持多切片索引，适用于关键词搜索等场景。
- 🚀 **v2.0**：引入查询引擎，支持关系型数据查询、排序和分页。
- 🔄 **v1.3**：新增显式事务控制方法，支持事务完成监听。
- ↩️ **v1.2**：新增事务回滚功能，支持条件性撤销变更。
- ⚠️ **v1.1**：新增无效数据监听器，支持错误处理。

---

### [GitHub - cosmiciron/vmprint：一个纯JS、小巧的排版引擎，能在从Cloudflare Workers 到浏览器的所有环境中实现位级精确的 PDF 输出。无需 Headless Chrome 即可打印文本。并且——请访问下方主页尝试静态演示，亲自体验。· GitHub](https://github.com/cosmiciron/vmprint)

**原文标题**: [GitHub - cosmiciron/vmprint: A pure-JS, tiny typesetting engine with bit-perfect PDF output on everything—from Cloudflare Workers to the browser. No more Headless Chrome to just print text. AND -- try the static demos on the home page below and see for yourself. · GitHub](https://github.com/cosmiciron/vmprint)

VMPrint 是一个纯 TypeScript 编写的确定性、零 DOM 依赖的排版引擎/虚拟机，旨在为构建自定义文档生成器、边缘渲染管道或全新文字处理器提供底层数学基础设施。它绕过浏览器的 HTML/CSS 盒模型，通过区间算术和可变形盒架构，直接从语义化 JSON AST 计算复杂的打印布局，输出绝对坐标的平面数组。该引擎无环境依赖，可在浏览器、Node.js、Cloudflare Workers 等环境中一致运行，并支持多栏文本、浮动元素、基线网格、多语言断行等高级排版功能。

- 🚀 **确定性布局引擎** – 在不同操作系统和运行时中生成完全一致的布局，无布局漂移。
- 🌐 **零环境依赖** – 核心引擎无需无头浏览器、DOM 或 Node.js 内置模块，可在浏览器、Node.js 及边缘环境中无缝运行。
- 📏 **真实字形测量** – 从字体文件读取 OpenType 字宽和字距对，基于绝对排版数学进行布局，而非浏览器估算。
- ⚡ **高性能** – 在毫秒级内渲染复杂的多页布局，全局缓存字形指标和文本分段确保高吞吐量。
- 📄 **多栏与混合布局** – 原生支持 DTP 风格的多栏故事区域，可在同一页面无缝混合单栏标题、三栏文章和引文。
- 🧩 **高级分页与功能** – 支持浮动元素、首字下沉、孤行控制、跨页延续标记、页眉页脚区域及复杂表格（跨页、合并单元格等）。
- 🌍 **多语言排版** – 使用 Intl.Segmenter 进行字形级断行，支持语言感知连字符、混合脚本文本运行和基线对齐。
- 🔧 **可插拔架构** – 可更换字体管理器和渲染后端（如 PDF），易于扩展至 SVG、Canvas 或自定义上下文。
- 📦 **轻量级与便携** – 完整依赖树约 2 MiB（压缩），远小于 Chromium 的 ~170 MB，适合边缘环境部署。
- 🛠️ **模块化包结构** – 提供核心引擎、PDF 上下文、字体管理器、Markdown 转换器等多个独立包，支持从 JSON 或 Markdown 源生成 PDF 或 AST。

---

### [获取失败](https://javascriptweekly.com/link/181847/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181847/web)

无法总结：获取内容失败，状态码 429。

---

### [GitHub - sqliteai/sqlite-js：用JavaScript创建自定义SQLite函数。直接在JavaScript中扩展数据库，支持标量、聚合、窗口函数和排序规则。· GitHub](https://github.com/sqliteai/sqlite-js)

**原文标题**: [GitHub - sqliteai/sqlite-js: Create custom SQLite functions in JavaScript. Extend your database with scalars, aggregates, window functions, and collations directly in JavaScript. · GitHub](https://github.com/sqliteai/sqlite-js)

SQLite-JS 是一个为 SQLite 数据库添加 JavaScript 功能的扩展，允许用户使用 JavaScript 代码创建自定义函数、聚合函数、窗口函数和排序规则，从而在数据库内实现灵活的数据操作。

- 🚀 **功能扩展**：支持创建标量函数、聚合函数、窗口函数和自定义排序规则，直接在 SQLite 中使用 JavaScript 处理数据。
- 📦 **多平台安装**：提供预编译二进制文件，支持 Linux、macOS、Windows、Android、iOS，并可通过 Swift、Android、Node.js、Flutter 等包管理器集成。
- 🔧 **使用示例**：包含创建各类函数的详细 SQL 语句和 JavaScript 代码示例，如计算年龄、中位数、移动平均值等。
- 🔄 **同步与持久化**：与 sqlite-sync 结合使用时，用户定义的函数可在 SQLite Cloud 集群中自动复制和同步，支持离线操作。
- 📚 **实用工具**：提供直接评估 JavaScript 代码、加载文件内容、设置引擎堆栈大小等辅助功能。
- ⚖️ **命名与更新规则**：函数命名需遵循 SQLite 标识符规则，且由于 SQLite 限制，更新函数需通过新的数据库连接进行。
- 🛠️ **开源与许可**：项目基于 Elastic License 2.0 开源，属于 SQLite AI 生态系统的一部分，旨在为边缘 AI 应用提供数据与推理引擎。

---

### [GitHub - luciopaiva/heapify：最快的JavaScript优先队列。零依赖。· GitHub](https://github.com/luciopaiva/heapify)

**原文标题**: [GitHub - luciopaiva/heapify: The fastest JavaScript priority queue out there. Zero dependencies. · GitHub](https://github.com/luciopaiva/heapify)

Heapify 是一个极快的 JavaScript 优先队列库，基于二进制堆实现，使用两个并行的类型化数组存储数据，无任何依赖，代码简洁高效，适用于浏览器和 Node.js 环境。

- 🚀 **高性能优先队列** – 在多项基准测试中速度领先于其他流行库，如 Closure、FastPQ 等。
- 📦 **零依赖与轻量** – 代码库不足 200 行，无运行时依赖，支持 ES5/ES6。
- 🔧 **灵活 API** – 提供 `push`、`pop`、`peek`、`clear` 等操作，支持自定义容量与数组类型。
- 🌐 **多环境支持** – 可通过 npm、yarn 安装，支持 Node.js、浏览器及 CDN 引入。
- 🧪 **可靠性与可读性** – 强调测试覆盖率和代码清晰度，易于理解与集成。
- 📊 **功能全面** – 支持批量构建、按键优先级管理，但堆实现不稳定（相同优先级顺序无保证）。

---

### [GitHub - openplayerjs/openplayerjs: 轻量级 HTML5 视频/音频播放器，具备流畅控制功能，支持播放 VAST/VMAP 广告 · GitHub](https://github.com/openplayerjs/openplayerjs)

**原文标题**: [GitHub - openplayerjs/openplayerjs: Lightweight HTML5 video/audio player with smooth controls and ability to play VAST/VMAP ads · GitHub](https://github.com/openplayerjs/openplayerjs)

OpenPlayerJS 是一个轻量级、模块化的 HTML5 音视频播放器，支持 MP4/MP3、HLS 等格式，并具备播放 VAST/VMAP 广告的能力。其 v3 版本进行了彻底重构，采用插件优先架构，更易于扩展和维护，同时移除了对 M(PEG)-DASH 和 FLV 的原生支持，广告功能也不再依赖 Google IMA SDK。

- 🎬 **播放器核心**：基于 HTML5 video/audio 元素，支持 MP4/MP3、HLS 等主流媒体格式。
- 🔌 **插件化架构**：UI、广告、引擎等均以插件形式存在，支持按需安装和扩展。
- 🛠️ **v3 新特性**：模块化包管理、插件优先设计、更清晰的代码分离，并内置了不依赖 Google IMA 的广告引擎。
- ❌ **移除功能**：不再原生支持 M(PEG)-DASH 和 FLV 格式，画质切换功能改为由各引擎自行实现。
- 🌐 **使用方式**：支持 ESM 模块化引入和 UMD 脚本直接加载，兼容原有使用方式。
- ⚙️ **配置简单**：只需在 HTML 中添加 video/audio 标签，并通过 JavaScript 初始化即可。
- 📦 **核心包**：包括 @openplayer/core（生命周期与插件系统）、@openplayer/player（默认 UI）、@openplayer/hls（HLS 引擎）和 @openplayer/ads（广告插件）。
- 🔧 **注意事项**：使用跨域资源时需配置 CORS；可通过 preload="none" 优化带宽，但需手动提供视频时长。
- 📚 **文档与许可**：提供详细的迁移指南和贡献说明，项目基于 MIT 许可证开源。

---

### [GitHub - sindresorhus/emittery：简洁现代的异步事件发射器 · GitHub](https://github.com/sindresorhus/emittery)

**原文标题**: [GitHub - sindresorhus/emittery: Simple and modern async event emitter · GitHub](https://github.com/sindresorhus/emittery)

Emittery 是一个简单现代的异步事件发射器，支持 Node.js 和浏览器环境，强调异步优先和类型安全，提供丰富的生命周期管理和调试功能。

- 🚀 **异步优先设计** – 监听器被推迟到下一个微任务执行，确保代码非阻塞，适合高并发场景。
- 🦾 **TypeScript 强类型支持** – 提供完整的事件类型定义，增强代码可靠性和开发体验。
- 🔄 **异步迭代支持** – 内置 `for await...of` 和异步迭代器助手，方便处理事件流。
- 🧩 **生命周期钩子** – 提供 `init`/`deinit` 钩子，用于懒加载资源的初始化和清理。
- 🛡️ **取消与清理机制** – 支持 `AbortSignal` 取消订阅和 `Symbol.dispose` 自动清理。
- 🔍 **可调式调试模式** – 可通过环境变量或实例设置启用调试日志，支持自定义日志记录器。
- 📦 **零依赖与轻量** – 项目无外部依赖，适用于各种 JavaScript 环境。
- ⚙️ **丰富的 API 功能** – 包括批量监听、单次订阅、监听器计数、方法绑定和装饰器混入等。
- 🌐 **跨平台兼容** – 在 Node.js 和浏览器（通过打包工具）中均可使用。
- 📖 **详细文档与示例** – 提供完整的 README、代码示例和常见问题解答，便于上手使用。

---

### [GitHub - wobsoriano/svelte-sonner: 专为 Svelte 设计的个性化 Toast 组件，源自@emilkowalski 的 sonner 项目移植版。· GitHub](https://github.com/wobsoriano/svelte-sonner)

**原文标题**: [GitHub - wobsoriano/svelte-sonner: An opinionated toast component for Svelte. A port of @emilkowalski's sonner. · GitHub](https://github.com/wobsoriano/svelte-sonner)

svelte-sonner 是一个为 Svelte 框架设计的通知提示组件，基于 Emil Kowalski 的 Sonner 项目移植而来，提供多种提示类型、自定义样式和丰富的配置选项。

- 🚀 **快速开始**：通过 npm、yarn 或 pnpm 安装，添加 `<Toaster />` 组件后即可使用 `toast()` 函数触发提示。
- 🎨 **提示类型**：支持默认、成功、信息、警告、错误、操作按钮、异步 Promise 和自定义组件等多种提示样式。
- 🔧 **自定义配置**：可调整主题（浅色/深色）、位置、展开模式、可见数量、样式（包括 Tailwind CSS 支持）和图标。
- ⚙️ **高级功能**：支持更新或手动关闭提示、设置持续时长、添加关闭回调，以及通过 `useSonner` 钩子获取当前提示列表。
- 📜 **开源许可**：项目基于 MIT 许可证开源，托管于 GitHub，拥有活跃的社区贡献和版本发布。

---

### [GitHub - embedpdf/embed-pdf-viewer: 一款能与任何 JavaScript 项目无缝集成的 PDF 查看器 · GitHub](https://github.com/embedpdf/embed-pdf-viewer)

**原文标题**: [GitHub - embedpdf/embed-pdf-viewer: A PDF viewer that seamlessly integrates with any JavaScript project · GitHub](https://github.com/embedpdf/embed-pdf-viewer)

EmbedPDF 是一个开源、框架无关的 JavaScript PDF 查看器，可轻松集成到任何 JavaScript 项目中，提供流畅的阅读体验和清晰的开发者 API。

- 📄 开源 PDF 查看器，采用 MIT 许可证，支持 React、Vue、Svelte、Preact 或原生 JavaScript 项目
- 🛠️ 功能丰富，支持标注、真实擦除、搜索、文本选择、缩放、旋转及平滑虚拟化滚动
- 📚 提供完整文档、安装指南、API 参考和示例，官网为 https://www.embedpdf.com
- 🚀 可在线体验演示，支持上传自有 PDF 或使用示例文件
- 🤝 欢迎社区贡献，提供贡献指南和 GitHub 讨论区
- ⚖️ 项目基于 MIT 许可证，并包含采用 Apache 2.0 许可证的 PDFium 组件

---

### [Tabulator | JavaScript 表格与数据网格](https://tabulator.info/)

**原文标题**: [Tabulator | JavaScript Tables & Data Grids](https://tabulator.info/)

Tabulator 是一个功能丰富、易于使用的 JavaScript 表格库，支持交互式数据展示与操作，兼容多种浏览器和前端框架。

- 📊 **简单易用**：通过简洁的代码即可创建交互式表格，支持自动列生成。
- ⚙️ **功能全面**：提供丰富的配置选项，包括布局、分页、排序、过滤、编辑、历史记录等。
- 🌐 **广泛兼容**：支持所有主流浏览器和 JavaScript 框架，提供框架设置指南。
- 🎨 **高度可定制**：支持主题、格式化、分组、CSS 样式、本地化等，满足个性化需求。
- 🔄 **数据交互**：支持 Ajax 加载、数据编辑、验证、下载及文件导入导出功能。
- 📱 **响应式与移动友好**：适配不同屏幕尺寸，支持触摸设备，提供冻结行列、键盘导航等增强体验。
- 🛠️ **高级特性**：包含虚拟 DOM 加速渲染、树形结构、单元格范围选择、右键菜单等专业功能。

---

### [melonJS](https://melonjs.org/)

**原文标题**: [melonJS](https://melonjs.org/)

melonJS 是一款现代轻量的开源 HTML5 游戏引擎，专为使用 JavaScript 和 TypeScript 构建 2D 游戏而设计。它无需依赖、支持摇树优化，并采用宽松的 MIT 许可证永久免费。

- 🚀 **快速高效**：基于 ES6 类和摇树优化，提供 WebGL 渲染器（带 Canvas 回退）和 Web Audio 3D 空间音效。
- 🆓 **完全免费**：采用 MIT 许可证，无任何费用，可永久使用。
- 📦 **独立轻量**：零依赖，兼容所有主流浏览器和移动设备，压缩后体积小于 100KB。
- 🗺️ **强大关卡设计**：原生支持 Tiled 地图编辑器，可创建正交、等距和六边形地图，支持多层、视差滚动等功能。
- 🎮 **丰富功能**：包括精灵动画、2D 光照、内置物理碰撞检测、多输入支持（鼠标、触摸、键盘等）、相机特效、UI 工具包以及粒子效果等。
- 🌐 **广泛兼容**：支持 Chrome、Firefox、Safari、Opera 等主流浏览器及移动端版本。
- 🔧 **第三方工具集成**：提供与多种第三方工具的原生集成和支持。

---

### [GitHub - WebReflection/flatted：一款快速且极简的循环JSON解析器。· GitHub](https://github.com/WebReflection/flatted)

**原文标题**: [GitHub - WebReflection/flatted: A fast and minimal circular JSON parser. · GitHub](https://github.com/WebReflection/flatted)

Flatted 是一个轻量、快速的循环 JSON 解析库，由 CircularJSON 的创建者开发，支持多语言并兼容标准 JSON API。

- 📦 超轻量且快速，仅 0.5KB，专门处理循环引用对象的序列化与反序列化
- 🌐 支持多语言版本，包括 PHP、Python 和 Go
- 🔄 提供与标准 JSON 相同的 API，包括`parse`、`stringify`、`reviver`和`replacer`参数
- 🛠️ 包含`toJSON`和`fromJSON`辅助方法，便于自定义类的隐式序列化
- ⚠️ 仅支持 JSON 兼容的数据类型，不适用于特殊内部类（如 Socket）
- 🔧 兼容所有支持 Map、Set 和基本数组方法的 ECMAScript 引擎
- 📊 工作原理：序列化时将对象扁平化为索引，反序列化时按索引还原结构

---

### [Poku - 让测试变得简单](https://poku.io/)

**原文标题**: [Poku - Making Testing Easy](https://poku.io/)

Poku 是一款免费开源的跨平台测试运行器，旨在为 JavaScript 测试带来简洁高效的体验，支持 Node.js、Bun 和 Deno 等多种平台。

- 🐷 **Poku 是什么？** – 一款跨平台测试运行器，回归 JavaScript 测试的本质，免费且开源。
- ⚡️ **快速教程** – 提供从初级到高级的教程，涵盖断言、测试组织、TDD/BDD 实践，以及处理 API、服务、容器等复杂场景。
- 🌐 **跨平台测试** – 支持在 Node.js、Bun 和 Deno 上运行相同的测试套件，确保库或包的兼容性。
- 👥 **用户案例** – 已被 MySQL2 等开源项目采用，用于测试多平台兼容性，同时 Poku 自身也使用自己进行测试。
- ⬇️ **安装与支持** – 可通过 npm、Bun 或 Deno 安装，支持 TypeScript 无需编译，欢迎在 GitHub 上为其点赞支持。

---

### [精密 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的交互行为，自动生成并维护全面的端到端测试套件，无需人工编写或维护测试代码，从而帮助开发团队高效、无缺陷地交付代码。

- 🚀 **无需编写测试**：通过记录开发、预演和生产环境中的用户交互，自动生成覆盖所有代码分支和用户流程的测试套件。
- 🔄 **测试自动演进**：随着应用更新，测试套件自动添加新功能测试并淘汰过时用例，保持测试始终最新且完整。
- ⚡ **消除测试波动**：基于 Chromium 构建的确定性调度引擎，从根本上消除测试波动，实现闪电般快速的测试执行。
- 🛡️ **无副作用测试**：通过模拟后端响应，实现无副作用的测试，避免因数据变化导致的误报，无需设置测试账户或模拟数据。
- 🌐 **广泛集成支持**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等多种前端框架，轻松集成到现有开发流程。
- 📈 **提升开发效率**：被 Dropbox、Notion 等超过 100 家组织信任，帮助团队大幅提升代码交付速度和可靠性，减少调试和维护时间。

---

### [Trigger.dev | 构建和部署全托管 AI 智能体与工作流。](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=march&utm_term=js-weekly&utm_content=homepage)

**原文标题**: [Trigger.dev | Build and deploy fully-managed AI agents and workflows.](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=march&utm_term=js-weekly&utm_content=homepage)

Trigger.dev 宣布完成 1600 万美元 A 轮融资，这是一个用于构建和部署全托管 AI 代理与工作流的 TypeScript 平台，支持长时间运行任务、重试、队列、可观测性和弹性扩展。

- 🚀 **平台核心**：Trigger.dev 是一个基于 TypeScript 构建 AI 工作流的平台，提供长时间运行任务、自动重试、队列管理、可观测性和弹性扩展功能。
- 🤖 **AI 代理能力**：支持构建具备工具调用、自动重试和完整可观测性的生产级 AI 代理，可集成现有 Node.js SDK 和代码库。
- 🔄 **工作流类型**：包括自主代理、提示链、智能路由、并行处理、协调器、评估优化器等多种 AI 工作流模式。
- ⚙️ **部署与扩展**：无需管理服务器，按实际执行付费，无超时限制，支持弹性基础设施和多区域工作器。
- 🐛 **调试与监控**：提供错误警报、高级运行过滤、版本控制、批量操作和实时运行状态显示，便于快速发现和修复问题。
- 🌐 **实时功能**：通过 Trigger.dev Realtime 可在应用中实时显示任务状态和元数据，并支持将 LLM 响应流式传输到前端。
- 🛠️ **开发自由**：支持高度自定义构建过程，可集成 Python、Prisma、Puppeteer、esbuild、FFmpeg 等多种工具和系统包。
- 📊 **功能全面**：涵盖开发、生产、可观测性等全流程工具，包括任务重试、结构化输入输出、多环境支持、优先级和幂等性等。
- 🔓 **开源与集成**：采用 Apache 2.0 开源许可，可自托管，与现有技术栈无缝集成，已在 GitHub 上获得超过 1.4 万星标。
- 💬 **用户认可**：受到多家公司开发者好评，被认为能显著提升开发效率、可靠性和迭代速度，适用于 AI 驱动解决方案、自动化工作流等场景。

---

### [JSLinux](https://bellard.org/jslinux/)

**原文标题**: [JSLinux](https://bellard.org/jslinux/)

JSLinux 是一个在浏览器中运行 Linux 或其他操作系统的仿真平台，提供多种 CPU 架构和操作系统的选择，支持从简单控制台到图形界面的不同用户体验。

- 🌐 提供 x86_64、x86 和 riscv64 等多种 CPU 架构的仿真系统
- 🐧 可运行 Alpine Linux、Windows 2000、FreeDOS 和 Fedora 等操作系统
- 🖥️ 用户界面选项包括控制台、X Window 和图形界面，适应不同需求
- ⚙️ 部分系统支持 VFsync 功能，提升性能与体验
- ⚠️ 注意某些系统有免责声明、警告或较长启动时间
- 🔗 通过点击链接直接访问和启动仿真系统
- 📜 平台包含新闻、虚拟机列表、FAQ 和技术说明等资源

---

### [法布里斯·贝拉的个人主页](https://bellard.org/)

**原文标题**: [Fabrice Bellard's Home Page](https://bellard.org/)

该网站展示了 Fabrice Bellard 的一系列创新技术项目，涵盖从模拟器、编译器到数据压缩和大型语言模型应用等多个领域。

- 🖥️ **JSLinux** 支持 x86_64、AVX-512 和 APX 架构，可在浏览器中运行 X Window 或 Windows 2000
- 🔧 **QuickJS** 是一个小型但完整的 JavaScript 引擎，另有 **Micro QuickJS** 适用于微控制器
- 📊 **TextSynth Server** 提供大型语言模型的 REST API，支持文本补全、问答、分类、聊天和翻译
- 🗜️ **NNCP** 无损数据压缩器在大型文本压缩基准测试中领先，另有 **ts_zip** 和 **ts_sms** 基于大模型的文本/短信压缩工具
- 🎵 **TSAC** 是一种极低比特率音频压缩技术
- 🖼️ **BPG** 是基于 HEVC 的新图像格式，支持大多数浏览器，另有小型混淆图像解码器
- 💾 **TinyEMU** 是模拟 128 位 RISC-V 和 x86 机器的小型模拟器
- 🔢 **LibBF** 是处理任意精度浮点数的小型库，**TinyPI** 可计算数百万位圆周率
- 📡 **4G LTE/5G NR/NB-IoT 基站** 完全在标准 PC 上以软件运行
- 📺 **模拟和数字电视信号** 可通过在 PC 显示器上显示图像生成
- ⚙️ **QEMU** 是通用机器模拟器和虚拟器，**FFMPEG** 是开源多媒体系统
- 📝 **TCC** 是完整且微小的 ISOC99 C 编译器，支持将 C 用作脚本语言
- ✍️ **QEmacs** 是用于学习 Unicode 渲染和文本处理的 emacs 克隆
- 🎯 **OTCC** 是极小的自编译 C 子集编译器，曾赢得国际混淆代码大赛
- 🎨 **TinyGL** 是 OpenGL 的小型、免费且快速的子集
- 🧮 **在线科学计算器** 和 **圆周率公式算法** 项目，包括用桌面计算机计算 2700 亿位圆周率
- 🔗 网站最后更新于 2026 年 3 月 9 日，可通过 fabrice at bellard 联系作者

---

### [JSLinux](https://bellard.org/jslinux/vm.html?cpu=x86_64&url=alpine-x86_64.cfg&mem=256)

**原文标题**: [JSLinux](https://bellard.org/jslinux/vm.html?cpu=x86_64&url=alpine-x86_64.cfg&mem=256)

Fabrice Bellard 的个人网站，提供新闻、虚拟机列表、常见问题解答和技术笔记等资源。

- 📰 新闻动态
- 🖥️ 虚拟机列表
- ❓ 常见问题解答
- 📝 技术笔记

---

### [我一直对此着迷，却从未知晓其用途... | 黑客新闻](https://news.ycombinator.com/item?id=47312829)

**原文标题**: [I've always been fascinated by this, but I have never known what it would be use... | Hacker News](https://news.ycombinator.com/item?id=47312829)

JSLinux 是一个在浏览器中运行的 x86_64 模拟器，用户讨论了其多种实际应用场景，从教育、测试到创意项目，并探讨了其背后的价值与意义。

- 🧪 用于测试和编译代码，尤其是在本地环境与模拟器中的编译器版本不同时，提供了便捷的替代方案。
- 🎮 作为分享和展示个人爱好项目（如自制操作系统）的平台，降低了他人体验的门槛。
- 🏫 在教育场景中，无需安装即可提供完整的 Linux 命令行或编程环境，适合课堂教学或技术面试。
- 🔧 充当临时的、隔离的测试环境，可用于网络工具测试或学习 Shell，且通常具备网络访问能力。
- 🗃️ 支持创建基于浏览器的应用程序或旧系统档案，用户可以直接启动并体验，如旧版 Mac OS。
- 🛡️ 在运行不受信任或自动生成的代码时，提供一种额外的隔离层，尽管其安全性存在讨论。
- 🎨 体现了技术探索和创造本身的乐趣与价值，类似于艺术创作，不一定需要直接的“实用”目的。
- 🔗 通过配置文件或特定工具（如 VFsync）可以定制化虚拟机并预装文件，适合特定用例的部署。

---

### [JSLinux - 技术笔记](https://bellard.org/jslinux/tech.html)

**原文标题**: [JSLinux - Technical Notes](https://bellard.org/jslinux/tech.html)

JSLinux 是一个基于 TinyEMU 的 PC/x86 和 RISC-V 模拟器，通过 emscripten 编译为 JavaScript 或 WASM，可在浏览器中运行 Linux 和 Windows NT 等操作系统，支持多种虚拟设备和网络功能，主要用于技术演示、学习和浏览器内安全文件访问。

- 🕰️ 项目始于 2011 年，最初为 JavaScript 编写的 PC/x86 模拟器，后基于 TinyEMU 重构，并利用 emscripten 提升性能
- 🔧 模拟 64 位 x86 CPU，支持 x87、AVX-512、APX 等高级特性，并具备 AMD SVM 虚拟化扩展
- 🖥️ 提供多种虚拟设备，包括 VirtIO 文件系统、网络、控制台，以及 PS/2 键盘、IDE 磁盘等可选外设
- 🌐 支持 RISC-V 32/64位CPU模拟，主要维护64位Buildroot和Fedora系统镜像
- ⚡ 在 2017 年典型桌面 Firefox 上性能约 100 MIPS，内置 vmtime 工具可进行详细基准测试
- 🐧 默认使用 Alpine Linux 和 Buildroot 发行版，可选 X Window 和 Fluxbox 窗口管理器
- 🔗 通过 WebSocket VPN 提供受限网络访问（带宽 40 kB/s，每IP限两个连接）
- 🎯 开发初衷为技术探索，实际用途包括 JavaScript 引擎基准测试、命令行学习、安全文件处理和旧软件运行
- 📂 源代码基于 TinyEMU 项目开源，提供预编译演示版本

---

### [获取失败](https://javascriptweekly.com/link/181865/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181865/web)

无法总结：获取内容失败，状态码 202。

---

### [在 Jetson Nano 上使用 Node 22 升级 OpenClaw 至最新版本 · brtkwr.com](https://brtkwr.com/posts/2026-03-02-upgrading-openclaw-to-latest-node22-on-jetson-nano/)

**原文标题**: [Upgrading OpenClaw to Latest on Jetson Nano with Node 22 · brtkwr.com
](https://brtkwr.com/posts/2026-03-02-upgrading-openclaw-to-latest-node22-on-jetson-nano/)

本文记录了在 Jetson Nano 上将 OpenClaw 升级至最新版本并迁移到 Node 22 的完整过程，包括因 Bun 安装路径问题导致的升级失败、尝试 Docker 方案后放弃、耗时 27 小时从源码编译 Node 22、解决 MTE 编译错误、以及最终通过彻底清理和重新安装成功部署 OpenClaw 的详细步骤与关键教训。

- 🚀 升级动机是获取新功能，如改进的 Telegram 处理、cron 修复、更好的模型回退链和 Claude 的自适应思考默认设置。
- 🛑 Bun 因插件清单路径验证失败而停止工作，导致服务崩溃循环 408 次，需迁移至 Node 环境。
- 🐳 尝试 Docker 方案虽简单但失去了主机直接访问能力，无法实现自我升级和系统包管理，故放弃。
- ⏳ 在 Jetson Nano 上从源码编译 Node 22 耗时约 27 小时，期间需处理 MTE 编译错误并应对内存压力。
- 🤖 设置 OpenClaw 定时任务监控编译进度，但完成后未及时停止，导致持续报告并耗尽 API 配额。
- 🧹 彻底移除 Bun 依赖，清理安装目录，并通过 npm 全新安装 OpenClaw，确保路径明确。
- 🔧 使用 systemd 服务明确指定 Node 和 OpenClaw 路径，避免环境混淆，验证服务状态和 HTTP 访问。
- 💾 用户数据（配置、记忆、会话）保存在`~/.openclaw`中，升级过程中得以保留，建议升级前备份。
- 📦 新版本 2026.3.1 引入自适应思考、cron 循环防护、Telegram 改进及安全增强等特性。
- 🧠 关键教训：优先全新安装而非就地升级；使用 npm+Node 路径；长时任务需用 tmux；监控任务应设停止条件；重要数据定期备份。

---

### [NoJS 3 - Flappy Bird 的黎明。使用纯 HTML 和 CSS 制作 Flappy Bird 克隆版，无需 JavaScript](https://blog.scottlogic.com/2026/03/09/noJS-3-flappy-bird.html)

**原文标题**: [NoJS 3 - The dawn of Flappy Bird. Making a Flappy Bird clone using pure HTML and CSS, no JavaScript](https://blog.scottlogic.com/2026/03/09/noJS-3-flappy-bird.html)

一款仅使用 HTML 和 CSS（无需 JavaScript）制作的 Flappy Bird 克隆游戏，展示了现代 CSS 的强大功能，通过纯前端技术实现完整的游戏逻辑与交互。

- 🐦 完全使用 HTML 和 CSS 构建，无需 JavaScript 即可实现游戏核心功能
- 🎮 利用 CSS 动画和过渡效果控制小鸟飞行、管道移动及碰撞检测
- 🖱️ 通过:active 和:hover 等伪类实现点击与悬停交互，模拟游戏操作
- 📱 响应式设计确保在不同设备上流畅运行，保持游戏体验一致
- 🚀 展示现代 CSS 技术的潜力，证明复杂交互项目可不依赖 JavaScript 完成
- 🔧 采用纯前端方案，无需后端或复杂框架，简化开发与部署流程

---

