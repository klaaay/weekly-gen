### [Node周刊第615期：2026年3月12日](https://nodeweekly.com/issues/615)

**原文标题**: [Node Weekly Issue 615: March 12, 2026](https://nodeweekly.com/issues/615)

Node Weekly 第615期（2026年3月12日）聚焦Node.js生态的最新动态，涵盖版本更新、工具发布、安全警示及技术深度解析。

- 📅 **Node.js发布周期调整**：官方确认每年发布一个主版本，从Node 27开始，LTS用户基本不受影响。
- 🕒 **Temporal提案进入Stage 4**：JavaScript时间处理库Temporal已获TC39批准，需等待Node 26默认启用。
- ⚠️ **阻塞I/O普遍存在**：对250个Node仓库的扫描显示，76%存在阻塞I/O调用，研究量化了其性能成本。
- 📦 **Node内置Zstd字典压缩**：Node v24.6+和v22.19+的zlib模块新增高效压缩功能。
- 🛠️ **重要工具更新**：MikroORM 7放弃Knex改用Kysely，node-sqlite3 6.0发布后停止维护，推荐转向better-sqlite3或node:sqlite。
- 🔧 **新工具与库**：ArkType 2.2实现TypeScript类型运行时验证，Systeminformation支持查询系统环境信息，Emittery 2.0提供简洁异步事件发射器。
- 💡 **AI辅助开发技巧**：Matteo Collina分享个人AI技能集，优化Node与Fastify开发中的AI代码生成。
- 🚨 **安全漏洞警示**：攻击者通过GitHub问题注入劫持npm发布令牌，提醒维护者加强仓库安全。
- 📊 **性能与生态**：JavaScript压缩工具基准测试显示SWC领先，JSLinux现支持x86_64并在浏览器中运行Node。

---

### [我的人工智能辅助Node.js开发个人技能](https://adventures.nodeland.dev/archive/my-personal-skills-for-ai-assisted-nodejs/)

**原文标题**: [My Personal Skills for AI-assisted Node.js Development](https://adventures.nodeland.dev/archive/my-personal-skills-for-ai-assisted-nodejs/)

作者分享了一个专为AI助手设计的个人技能库，旨在提升Node.js开发的效率与代码质量。该库整合了作者在Fastify、TypeScript等领域的多年实践经验，帮助AI生成更符合最佳实践的代码。

- 🚀 **快速集成**：通过`npx skills add mcollina/skills`即可使用该技能库，编码个人偏好与最佳实践
- 🛠️ **全面覆盖**：包含Fastify开发、Node.js核心、TypeScript高级类型、Git工作流等八大技能模块
- 📚 **标准格式**：遵循开放的Agent Skills标准，兼容主流AI开发工具如GitHub Copilot、Claude Code等
- 🎯 **实践导向**：每个技能提供Markdown说明、代码片段和配置示例，基于真实项目经验总结
- 🔮 **持续演进**：作者计划持续添加性能优化、安全部署等新技能，社区可参与完善

---

### [快速且低开销的Node.js Web框架 | Fastify](https://fastify.dev/)

**原文标题**: [Fast and low overhead web framework, for Node.js | Fastify](https://fastify.dev/)

Fastify 是一个高性能的 Node.js Web 框架，专注于提供最佳开发者体验、低开销和强大的插件架构，旨在高效处理服务器资源，同时确保安全性和开发便利性。

- 🚀 **高性能**：据称是目前最快的 Web 框架之一，每秒可处理高达 3 万次请求。
- 🔌 **可扩展性**：通过钩子、插件和装饰器实现完全可扩展。
- 📝 **基于模式**：推荐使用 JSON Schema 验证路由和序列化输出，内部将模式编译为高性能函数。
- 📊 **日志记录**：集成 Pino 日志库，几乎零成本实现高效日志记录。
- 👨‍💻 **开发者友好**：设计注重表达性，兼顾性能与安全，提升开发效率。
- ⚙️ **TypeScript 支持**：提供类型声明文件，全面支持 TypeScript 开发。
- 🌍 **广泛采用**：每月下载量超过 1000 万次，被众多组织和产品使用。
- 🛠️ **快速入门**：通过 npm 安装，简单几行代码即可创建并运行服务器。
- 📚 **丰富生态**：拥有超过 291 个插件，覆盖数据库、模板语言等常见需求。
- 👥 **活跃团队**：由核心维护者和贡献者组成的团队持续推动项目发展。

---

### [获取失败](https://nodeweekly.com/link/181960/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/181960/web)

无法总结：获取内容失败，状态码 429。

---

### [获取失败](https://nodeweekly.com/link/181961/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/181961/web)

无法总结：获取内容失败，状态码 429。

---

### [获取失败](https://nodeweekly.com/link/181962/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/181962/web)

无法总结：获取内容失败，状态码 429。

---

### [你的技能在opus上有效。它会让俳句变差吗？跨Claude模型的人工智能技能基准测试](https://tessl.io/blog/your-skill-works-on-opus-does-it-make-haiku-worse-benchmarking-ai-skills-across-claude-models/)

**原文标题**: [Your skill works on opus. Does it make haiku worse? Benchmarking AI skills across Claude models](https://tessl.io/blog/your-skill-works-on-opus-does-it-make-haiku-worse-benchmarking-ai-skills-across-claude-models/)

本文介绍了Tessl新推出的review-model-performance技能，该技能可自动评估AI技能在不同Claude模型上的表现，通过生成测试场景、对比有无技能时的模型表现，帮助开发者发现技能的有效性、模型兼容性问题及潜在的性能退化。

- 🧪 **自动生成评估场景**：技能能根据技能内容自动创建测试场景和可验证的评估标准，无需手动编写。
- 📊 **跨模型性能对比**：在haiku、sonnet、opus三个模型上运行测试，对比有无技能时的表现，量化技能提升效果。
- 🔍 **识别技能价值**：低基线分配合高技能分表明技能有效；高基线分则提示技能可能冗余。
- 🛠️ **逐项分析优化**：通过查看每项评估标准的通过率，定位技能内容的不足，例如发现某些模式在所有模型中均失败。
- ⚠️ **检测性能退化**：技能可能在某些场景导致模型表现变差，评估能及时发现此类回归问题。
- 🚀 **快速开始指南**：提供安装Tessl、导入技能、运行评估的步骤，帮助用户自行进行技能基准测试。

---

### [TimescaleDB — 排名第一的时序数据库 | 泰格数据](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB是一个基于Postgres构建的时序数据库，提供高性能时序数据处理、实时分析和事件管理，兼具开源灵活性与企业级可扩展性。

- 🚀 核心功能：自动分区（Hypertables）、行列混合存储、高达95%的数据压缩、增量物化视图和自动化管理
- ⏱️ 时序分析：内置约200种超函数，支持时间加权平均、插值和部分聚合，简化高级时序计算
- ☁️ 云原生兼容：100% PostgreSQL兼容，支持Helm快速部署，适合初创公司和企业弹性扩展
- 🛠️ 行业应用：已服务于加密货币、能源科技等领域，客户包括Cloudflare、Replicated等企业
- 🌍 开源生态：拥有2.2万+ GitHub星标和1.2万+ Slack社区成员，支持开发者共同推进产品发展
- 📊 性能优势：支持毫秒级查询数十亿行数据，兼顾实时分析需求与历史数据低成本存储

---

### [Node.js — 演进中的Node.js发布日程安排](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule)

**原文标题**: [Node.js — Evolving the Node.js Release Schedule](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule)

Node.js 将从 27.x 版本开始，将每年两次的主要版本发布改为每年一次，以简化版本管理、减轻维护者负担，并为用户提供更可预测的发布周期。新计划包括引入 Alpha 通道进行早期测试，所有版本都将成为长期支持版本，取消奇偶版本区分，版本号将与发布年份对齐。

- 📅 **发布周期调整**：从每年两个主要版本改为每年一个，自 2027 年的 27.x 版本开始实施。
- 🔄 **版本统一**：所有版本都将成为长期支持版本，取消奇偶版本区分，减少用户混淆。
- 🧪 **新增 Alpha 通道**：提供 6 个月的早期测试期，允许语义化版本的重大变更，供库作者和 CI 管道提前适配。
- 📊 **版本号对齐年份**：版本号将反映发布的日历年份，例如 27.0.0 对应 2027 年。
- ⏳ **支持周期不变**：长期支持期仍为 30 个月，总支持时间从首次发布到终止支持共 36 个月。
- 👥 **减轻维护负担**：减少并发发布线，缓解志愿者在安全更新和后移植方面的压力。
- 🗓️ **时间表示例**：Node.js 27 将于 2026 年 10 月进入 Alpha 阶段，2027 年 4 月发布正式版，2027 年 10 月进入长期支持，2030 年 4 月终止支持。

---

### [TypeScript 6.0 RC 版本发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

**原文标题**: [Announcing TypeScript 6.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

TypeScript 6.0 RC 已发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本包含多项新特性、改进以及为未来版本对齐所做的调整，同时引入了多项重大变更和弃用以反映现代 JavaScript 生态。

- 🚀 **发布候选版**：TypeScript 6.0 RC 现已可用，可通过 `npm install -D typescript@rc` 安装。
- 🌉 **过渡版本**：作为 TypeScript 7.0 的前身，6.0 主要专注于为未来的原生版本做好对齐和准备。
- 🧠 **改进的类型推断**：对于未使用 `this` 的函数，减少了其上下文敏感性，从而在方法语法等场景中实现了更好的类型推断。
- 📁 **子路径导入支持 `#/`**：现在支持以 `#/` 开头的 Node.js 子路径导入，与常见的打包器路径映射习惯保持一致。
- ⚙️ **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **稳定的类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，有助于减少版本间差异，但可能带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的新选项，并引入了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 3 的 Temporal API 提供了内置类型支持。
- 🗺️ **新增 Map 方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法类型。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数类型，用于转义正则表达式中的特殊字符。
- 🌐 **DOM 库整合**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容。
- ⚠️ **多项重大变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、`types` 默认改为空数组、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等。建议使用 `"ignoreDeprecations": "6.0"` 暂时忽略警告，但这些选项将在 7.0 中彻底移除。
- 🚫 **配置加载行为变更**：当存在 `tsconfig.json` 时，在命令行中指定文件将报错，需使用 `--ignoreConfig` 标志来忽略配置。
- 🔜 **为 7.0 做准备**：强烈建议在升级到 TypeScript 7.0 之前，解决所有在 6.0 中出现的弃用警告。

---

### [TypeScript 6.0 RC 版本发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/#what%E2%80%99s-new-since-the-beta)

**原文标题**: [Announcing TypeScript 6.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/#what%E2%80%99s-new-since-the-beta)

TypeScript 6.0 RC 已发布，这是基于当前 JavaScript 代码库的最后一个版本，旨在为使用 Go 重写的 TypeScript 7.0 原生版本铺平道路。此版本包含多项新特性、改进以及为未来版本对齐所做的变更，同时引入了多项破坏性更改和弃用项。

- 🚀 **发布候选版本**：TypeScript 6.0 RC 现已可用，可通过 `npm install -D typescript@rc` 安装。
- 🌉 **过渡性版本**：作为 TypeScript 7.0 的前置版本，主要变更旨在为迁移到新代码库做准备。
- 🔧 **推断改进**：对无显式 `this` 使用的方法减少了上下文敏感性，提升了泛型函数中参数类型的推断能力。
- 📁 **子路径导入支持**：现在支持以 `#/` 开头的子路径导入，简化了项目内的模块映射。
- ⚙️ **模块解析组合**：`--moduleResolution bundler` 现在可与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🏷️ **稳定类型排序标志**：新增 `--stableTypeOrdering` 标志，使 TypeScript 6.0 的类型排序行为与 7.0 保持一致，便于迁移对比。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的选项，包含了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为处于 Stage 3 的 Temporal API 提供了内置类型支持。
- 🗺️ **新增 Map 方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法类型。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数类型，用于正则表达式字符转义。
- 🌐 **DOM 库更新**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容。
- ⚠️ **多项破坏性变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等。`types` 字段现在默认为空数组，需要显式声明。
- 🚫 **配置加载行为变更**：在存在 `tsconfig.json` 的目录中通过命令行指定文件进行编译现在会报错，需使用 `--ignoreConfig` 标志。
- 📅 **为 7.0 做准备**：强烈建议在 TypeScript 6.0 中解决所有弃用警告，以便顺利过渡到即将发布的 TypeScript 7.0 原生版本。

---

### [错误](https://nodeweekly.com/link/181967/web)

**原文标题**: [Error](https://nodeweekly.com/link/181967/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/181967/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [《时间之旅：修复JavaScript中时间问题的九年征程》| 彭博JS博客](https://bloomberg.github.io/js-blog/post/temporal/)

**原文标题**: [Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/temporal/)

本文概述了JavaScript中新的日期时间API——Temporal的九年发展历程，从旧Date对象的缺陷出发，通过TC39标准化流程，最终成为ECMAScript 2026标准的一部分。Temporal提供了不可变、时区感知、高精度且支持多种日历的现代化日期时间处理方案，解决了长期困扰开发者的痛点。

- 🕰️ JavaScript的Date对象源于1995年对Java Date的直接移植，设计上存在诸多历史遗留问题，如可变性、时区处理不一致和解析歧义等。
- 📚 为解决Date的不足，社区涌现了如Moment.js等库，但它们带来了包体积膨胀和维护负担，促使标准化新API的需求。
- 🏗️ Temporal提案于2017年由Maggie Johnson-Pint提出，得到Bloomberg、Microsoft、Google、Igalia等多方支持，历经TC39各阶段成熟度审核。
- 👥 核心贡献者包括来自Bloomberg、Igalia、Google等公司的工程师，他们共同推动规范设计、实现及测试，确保提案的实用性与鲁棒性。
- 🔧 Temporal提供多种不可变类型，如ZonedDateTime（精确时刻带时区）、Instant（纳秒级时间戳）、PlainDate系列（无时区日期时间）及Duration（时间间隔）。
- 🌍 支持多日历系统（如希伯来历），允许按特定日历规则进行日期运算，避免Gregorian历法下的偏差。
- ⚙️ 实现挑战巨大，Temporal是自ES2015以来最大的语言新增特性，最终通过跨引擎协作的Rust库temporal_rs高效实现，并已集成到主流浏览器和Node.js中。
- 🚀 Temporal已于2026年初达到TC39 Stage 4，纳入ES2026标准，目前可在Firefox、Chrome、Edge等环境中使用，未来将逐步与Web API（如日期选择器、Cookie设置）深度集成。
- 🤝 项目成功体现了JavaScript社区通过开放协作解决长期问题的能力，为生态提供了统一、可靠的日期时间处理基础。

---

### [默认启用Temporal功能 · Issue #57127 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/57127)

**原文标题**: [Let's enable Temporal by default · Issue #57127 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/57127)

Node.js GitHub仓库中关于启用Temporal API的提案讨论。

- 🚀 **提议默认启用Temporal API**：该API在TC39标准中接近完成且基本稳定，建议在Node.js主分支中默认启用。
- ⚠️ **仍标记为实验性功能**：尽管默认启用，但会保留实验性标识，以反映其尚未达到TC39最终阶段的状态。
- 🔄 **平台趋势与兼容性**：其他平台已开始默认启用此功能，Node.js应考虑跟进以保持技术一致性。
- 📋 **问题跟踪与标签**：该提案在GitHub上被标记为“功能请求”，目前处于待处理状态，尚未分配负责人或设定里程碑。

---

### [Node.js — Node.js 25.8.1（当前版本）](https://nodejs.org/en/blog/release/v25.8.1)

**原文标题**: [Node.js — Node.js 25.8.1 (Current)](https://nodejs.org/en/blog/release/v25.8.1)

Node.js 25.8.1（Current）版本发布，主要修复了模块、加密、流处理等多个核心模块的问题，并更新了依赖项和文档。

- 🐛 修复了在 `"type": "module"` 包中无扩展名的 CJS 文件处理问题
- 🔐 加密模块更新，包括修复 AES 字典缺失和参数检查，并调整了系统 CA 证书的加载方式
- 📦 更新了多个依赖项，如 amaro、sqlite、merve 和 V8 引擎
- 📚 文档进行了多处修正和补充，包括新增维护者
- 🌊 流处理模块优化，修复了压缩流错误处理和 UTF-8 字符损坏等问题
- 🛠️ 构建和工具链改进，包括修复测试运行器和更新 GitHub Actions
- 🔗 提供了 Windows、macOS、Linux 等多平台的安装包和二进制文件下载

---

### [Node.js — Node.js 22.22.1（长期支持版）](https://nodejs.org/en/blog/release/v22.22.1)

**原文标题**: [Node.js — Node.js 22.22.1 (LTS)](https://nodejs.org/en/blog/release/v22.22.1)

Node.js 22.22.1（LTS）版本发布，包含多项重要更新，涵盖构建系统、CLI工具、加密证书、文档改进、性能优化及错误修复，同时更新了多个依赖库并新增了三位协作者。

- 🛠️ **构建系统**：支持在 Python 3.14 上进行测试，并修复了多个构建相关的问题。
- 📊 **CLI 工具**：将 `--heapsnapshot-near-heap-limit` 选项标记为稳定功能。
- 🔐 **加密证书**：根证书更新至 NSS 3.119 版本，提升安全性。
- 📚 **文档与协作者**：新增三位协作者，并进行了大量文档修正与更新。
- ⚡ **性能优化**：改进了 Buffer 拼接、断言比较、控制台日志等多项性能。
- 🐛 **错误修复**：修复了集群端口重用、HTTP/2 初始窗口大小验证等多个问题。
- 📦 **依赖更新**：更新了 OpenSSL、SQLite、ICU、zlib 等多个核心依赖库。
- 🧪 **测试与工具**：增强了测试框架，优化了基准测试，并改进了开发工具链。

---

### [Node.js — Node.js 20.20.1（长期支持版）](https://nodejs.org/en/blog/release/v20.20.1)

**原文标题**: [Node.js — Node.js 20.20.1 (LTS)](https://nodejs.org/en/blog/release/v20.20.1)

Node.js 20.20.1（LTS）版本发布，代号“Iron”，包含多项更新与修复，涵盖构建系统、加密模块、依赖库升级及文档修正等方面。

- 🐍 构建系统现在支持在 Python 3.14 上进行测试
- 🔒 加密模块的根证书已更新至 NSS 3.119 和 3.117 版本
- 🛠️ 多个依赖库得到升级，包括 V8、ICU、zlib、minimatch 等
- 📝 修复了文档中的多处拼写错误和语法问题
- 🌐 解决了 HTTP 和 HTTP2 模块中的若干问题，如保持连接超时和窗口大小验证
- 🧪 标记了多个在特定平台（如 AIX、LinuxONE）上不稳定的测试用例
- 🔧 改进了工具链和持续集成流程，包括使用 ARM 运行器和优化构建步骤
- 📦 提供了适用于 Windows、macOS、Linux 等多个平台的安装包和二进制文件

---

### [我们扫描了250个Node.js仓库的阻塞I/O问题，76%存在此状况——基准测试揭示其重要性。](https://stackinsight.dev/blog/blocking-io-empirical-study/)

**原文标题**: [We Scanned 250 Node.js Repos for Blocking I/O. 76% Had It — and the Benchmarks Explain Why That Matters.](https://stackinsight.dev/blog/blocking-io-empirical-study/)

一项针对250个Node.js开源项目的静态分析显示，76%的代码库中存在阻塞I/O调用，其中约7%位于请求处理路径中，可能严重影响服务器性能。基准测试揭示了不同阻塞操作的性能影响：execSync在请求处理器中会导致吞吐量下降280倍，pbkdf2Sync虽不影响吞吐量但会引发大量错误和超时，而常见的文件操作（如readFileSync）也会造成3倍以上的性能损失。

- 🔍 **高普遍性** – 扫描发现76.4%的Node.js项目包含阻塞I/O调用，文件系统操作占90.6%，其中existsSync是最常见的阻塞方法。
- ⚠️ **风险分布** – 约6.8%的阻塞调用位于请求处理路径中，属于高风险；另有60.3%因静态分析限制无法明确分类，实际风险可能更高。
- 📉 **性能影响显著** – 基准测试显示：execSync使吞吐量从10,000请求/秒降至36，延迟飙升841倍；pbkdf2Sync导致91次错误和26次超时；文件读写操作普遍造成3倍性能下降。
- 🛡️ **安全与风险** – pbkdf2Sync在认证端点可能放大DoS攻击；execSync在并发下会使服务器近乎瘫痪，属于最危险的阻塞操作。
- 🛠️ **检测与修复** – 可通过grep搜索Sync(、使用AST分析工具或监控生产环境事件循环延迟（P99>50ms即需排查）来定位问题；修复通常只需替换为异步版本并添加await。
- ✅ **安全场景** – 约31.5%的阻塞调用位于启动脚本、构建工具或测试文件中，这些场景通常可接受同步操作。
- 📊 **数据公开** – 所有扫描代码、基准测试实现和结果数据均已开源，可供复现和进一步研究。

---

### [词典压缩终于到来，效果惊人地出色](https://httptoolkit.com/blog/dictionary-compression-performance-zstd-brotli/)

**原文标题**: [Dictionary Compression is finally here, and it's ridiculously good](https://httptoolkit.com/blog/dictionary-compression-performance-zstd-brotli/)

字典压缩技术现已广泛支持，可显著减少网络数据传输量，例如使YouTube的JS包缩小90%，Google搜索结果HTML缩小近50%。该技术通过预共享字典实现高效压缩，适用于JS、WASM及API响应等场景。

- 🚀 **高效压缩**：利用预共享字典，仅传输差异数据，大幅降低带宽使用
- 🌐 **广泛适用**：支持Zstandard和Brotli算法，适用于JS包、WASM文件及结构化API响应
- 🔧 **简单部署**：通过HTTP头协商字典，Chrome等现代浏览器已支持，可逐步实施
- 📦 **字典类型**：可使用历史响应作为字典，或构建自定义字典以覆盖常见数据模式
- ⚠️ **注意事项**：仅限同源使用，需注意缓存策略及字典管理复杂性
- 📊 **实测效果**：Google搜索流量减少23-50%，部分场景压缩比高达95%
- 🔮 **未来展望**：有望显著减少重复数据传输，推动网络性能优化

---

### [源映射：通过标准发布功能 | 彭博JS博客](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

**原文标题**: [Source Maps: Shipping Features Through Standards | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

Source Maps 是连接开发者源代码与浏览器运行代码的关键技术，经历了从非正式协作到正式标准化的历程，如今在 ECMA-426 标准下持续演进，以支持更复杂的调试需求。

- 🗺️ **源映射的作用**：在代码经过编译、压缩后，源映射能将生成代码的位置映射回原始源代码，使调试成为可能。
- 📜 **历史背景**：源映射最初没有正式标准，依赖共享文档协作了十年，直到 2023 年成立 TC39-TG4 任务组，并于 2024 年正式标准化为 ECMA-426。
- 🔍 **文件结构**：源映射是一个 JSON 文件，包含版本、源文件列表、映射数据等字段，其中 `mappings` 字段使用 Base64 VLQ 编码以提高效率。
- 📉 **版本演进**：Revision 3（2011 年）通过改用分段映射和相对编码，大幅减小了文件大小，成为现代源映射的基础。
- 🚀 **新特性发展**：在没有标准时期，通过 `x_` 前缀添加了如 `ignoreList` 等特性；标准化后，正在推进 **Scopes**（提供作用域和变量信息）和 **Range Mappings**（提高映射精度）等新功能。
- 🤝 **社区协作**：标准化过程汇集了 Bloomberg、Google、Mozilla 等多方力量，体现了开源生态的合作精神，未来将继续开放征集反馈。

---

### [AdonisJS 7 转换器深度解析 | Mezie 实验室](https://mezielabs.com/articles/adonisjs-7-transformers-a-deep-dive)

**原文标题**: [AdonisJS 7 Transformers: A Deep Dive | Mezie Labs](https://mezielabs.com/articles/adonisjs-7-transformers-a-deep-dive)

AdonisJS 7 引入了转换器（Transformers）作为其核心特性之一，旨在解决序列化过程中的类型安全、关注点分离和关系处理等问题。转换器通过独立的类来明确定义数据输出格式，支持变体、关系处理、分页响应和依赖注入，并与前端类型生成无缝集成，实现了端到端的类型安全。

- 🎯 **解决序列化痛点**：转换器解决了 AdonisJS 6 中模型序列化混合关注点、缺乏类型安全和关系处理不便的问题。
- 🏗️ **独立序列化层**：转换器作为独立的类，通过 `toObject()` 方法定义数据输出格式，实现序列化与持久化层的分离。
- 🛠️ **便捷创建与使用**：通过 `make:transformer` 命令快速生成转换器，并在控制器中使用 `serialize()` 方法进行序列化。
- 🔧 **辅助方法增强灵活性**：提供 `pick` 和 `omit` 方法进行类型安全的属性选择，支持变体（variants）以适应不同上下文的数据输出。
- 🔗 **关系处理与深度控制**：通过组合转换器处理关联数据，使用 `whenLoaded` 和 `whenCounted` 方法避免未加载关系导致的错误，并支持显式的序列化深度控制。
- 📊 **分页响应支持**：转换器提供 `paginate` 方法，与 Lucid 的分页查询无缝集成，自动生成包含元数据的分页响应。
- 🧩 **依赖注入与自定义数据**：支持通过 `@inject()` 装饰器注入服务，并允许传递自定义上下文数据，增强转换逻辑的灵活性。
- 🔗 **前端类型生成**：AdonisJS 7 自动生成基于转换器的 TypeScript 类型，实现后端与前端之间的端到端类型安全。
- 🚀 **Inertia 集成**：转换器与 Inertia.js 深度集成，支持延迟加载属性和共享数据，提升全栈应用开发体验。

---

### [ArkType 2.2 正式发布](https://arktype.io/docs/blog/2.2)

**原文标题**: [Announcing ArkType 2.2](https://arktype.io/docs/blog/2.2)

ArkType 2.2 版本正式发布，引入了运行时验证函数、类型安全正则表达式、双向 JSON Schema 支持以及通用模式互操作性等多项新功能，显著增强了类型定义和验证能力。

- 🎯 **运行时验证函数**：通过 `type.fn` 定义具有运行时验证参数和返回类型的函数，支持默认值、可选参数和可变参数，无需 TypeScript 即可获得完整类型安全。
- 🔍 **类型安全正则表达式**：集成 `arkregex`，正则表达式字面量现在支持完整的类型推断，包括捕获组，可通过 `x` 前缀在运行时解析捕获组。
- 🔄 **双向 JSON Schema 支持**：新增 `@ark/json-schema` 包，支持将 JSON Schema 解析为 ArkType 类型，并提供可配置的 `toJsonSchema` 方法，实现双向转换。
- 🧩 **通用模式互操作性**：任何符合 Standard Schema 的验证器都可以直接嵌入 ArkType 定义中，实现跨生态系统的验证器混合使用。
- 🛠️ **深度引用内省**：新增 `select` 方法，允许查询类型的内部结构，并可针对特定引用进行配置，无需转换整个类型。
- 📝 **改进的类型声明**：`type.declare` 现在支持形态感知声明，可通过属性值表达可选性，并提供清晰的错误信息。
- 📊 **可序列化错误**：`ArkErrors` 现在可 JSON 序列化，便于作为 API 响应或日志存储，新增结构化访问属性。
- 🔗 **N 元操作符**：`type.or`、`type.and`、`type.merge` 和 `type.pipe` 现在支持可变参数定义，避免链式或组合二元表达式。
- 🧵 **字符串嵌入管道操作符**：`|>` 管道操作符现在可直接在字符串定义中使用，简化类型转换链。
- 🆕 **新关键字和配置**：新增 `string.hex` 和 `string.regex` 关键字，支持 `exactOptionalPropertyTypes` 全局配置，提升兼容性和性能。
- ⚙️ **其他改进**：包括类型分发、ES2020/Hermes 兼容性、文档内 playground、循环联合类型优化、更快的自动完成、更好的 JSDoc 支持等。

---

### [MikroORM 7：解放束缚 | MikroORM](https://mikro-orm.io/blog/mikro-orm-7-released)

**原文标题**: [MikroORM 7: Unchained | MikroORM](https://mikro-orm.io/blog/mikro-orm-7-released)

MikroORM 7 是迄今为止最大的版本更新，核心包实现零运行时依赖，并引入多项重大改进和新功能。

- 🚀 **核心零依赖**：`@mikro-orm/core` 包移除所有运行时依赖，显著减少打包体积和冷启动时间，提升可维护性。
- 🔄 **Knex 替换为 Kysely**：内部查询构建完全重写，使用 Kysely 作为查询执行器，提供更优的 SQL 控制和自动类型推断。
- 📦 **原生 ESM 支持**：MikroORM 现在是一个原生 ESM 包，同时保持对 CJS 项目的兼容性。
- 🌐 **脱离 Node.js 依赖**：核心运行时不再直接依赖 Node.js 内置模块，为 Deno 等运行时支持奠定基础。
- 📚 **发布至 JSR**：所有包同时发布到 JSR，为 Deno 用户提供一流的 TypeScript 支持。
- 🛡️ **类型安全的 QueryBuilder**：查询构建器现在通过泛型参数跟踪连接别名，提供完整的自动补全和类型检查。
- 🏷️ **字段别名支持**：QueryBuilder 的 `select()` 方法支持字段别名，包括 `@Formula` 属性，且别名在类型系统中被跟踪。
- 🔍 **类型安全的部分加载**：`fields` 参数现在在 QueryBuilder 中也是类型安全的，返回的实体或 DTO 类型会根据所选字段自动缩小。
- 🧩 **公共表表达式（CTE）**：QueryBuilder 新增 `with()` 和 `withRecursive()` 方法，支持跨所有 SQL 驱动器的 CTE。
- 🔗 **UNION 条件查询**：新增 `unionWhere` 选项，通过 `UNION ALL` 创建索引友好的替代方案，优化复杂 `$or` 查询。
- ♻️ **可重用的原始片段**：`raw()` 创建的查询片段现在使用符号和 `WeakMap` 进行缓存，支持跨多个查询重用。
- 📏 **集合大小操作符**：新增 `$size` 操作符，用于查询 `to-many` 关系的集合大小，支持精确匹配和比较操作符。
- 🔍 **透明查询嵌入式数组**：现在可以直接查询嵌入式数组元素的属性，ORM 会自动生成正确的 `EXISTS` 子查询。
- 🏷️ **JSON 数组的 $elemMatch 操作符**：为纯 JSON 数组属性引入 `$elemMatch` 操作符，支持元素级条件匹配。
- 🌍 **排序规则支持和 MongoDB 查询选项**：新增 `collation` 选项，支持 SQL 驱动器的排序规则应用和 MongoDB 的原生排序规则选项。
- 🌊 **原生流式支持**：新增 `em.stream()` 和 `qb.stream()` 方法，支持逐行或批量流式处理大型数据集。
- ⚖️ **平衡加载策略为默认**：v6.5 引入的平衡加载策略现为默认，它连接 `to-one` 关系，但对 `to-many` 关系使用单独查询。
- 🎯 **按关系覆盖填充提示**：新增 `populateHints` 选项，允许为单个关系覆盖加载策略或连接类型。
- 🏗️ **使用自定义类的 defineEntity**：现在可以扩展 `defineEntity` 自动生成的类，添加自定义域方法，无需重复属性定义。
- 📊 **实体级默认排序**：现在可以在实体本身上定义默认的 `orderBy`，该排序在直接查询实体或作为关系填充时自动应用。
- 🏷️ **ES 装饰器**：所有装饰器已移至专门的 `@mikro-orm/decorators` 包，并提供两种风格：传统（TypeScript 实验性）和 ES 规范。
- 👁️ **视图实体**：新增视图实体支持，可创建由模式生成器管理的实际数据库视图，PostgreSQL 还支持物化视图。
- 🔗 **多态关系**：新增多态关系支持，允许单个属性引用多个不同类型的实体，每个类型位于自己的表中。
- 🧬 **表按类型继承（TPT）**：新增表按类型继承支持，每个实体都有自己的专用表，子表通过外键链接到父表。
- 🔑 **非主键外键目标**：现在原生支持 `to-one` 关系以任何唯一列为目标，通过 `targetKey` 选项配置。
- 📈 **高级索引功能**：新增对高级索引功能的原生支持，包括列排序顺序、NULLS 排序、覆盖索引、填充因子等。
- 🔌 **可插拔的 SQLite 方言**：SQLite 驱动程序重构以支持可插拔方言，现支持 Node.js 22 内置的 `node:sqlite` 模块，实现零原生依赖。
- 🗄️ **SQLite ATTACH DATABASE**：SQLite 现在支持 `ATTACH DATABASE`，用于在单个连接上处理多个数据库文件。
- ⚡ **边缘运行时的预编译函数**：新增 `compile` CLI 命令，可预生成所有优化函数到纯 `.js` 文件中，兼容禁止动态代码评估的边缘运行时。
- 📦 **打包友好的迁移和种子**：`@mikro-orm/migrations` 包不再依赖 `umzug`，迁移编排完全内联，通过 `migrationsList` 和 `seedersList` 选项避免文件系统访问。
- 🔧 **更多 TypeScript 加载器支持 CLI**：现支持多种 TypeScript 加载器（如 swc、tsx、jiti、tsimp），无需自定义加载器或脚本。
- 🛠️ **改进的压缩支持**：内部改用类引用而非类名，提高对重复或混淆类名的抵抗力。
- ⏱️ **慢查询日志**：新增内置慢查询检测功能，可设置阈值记录超过指定时间的查询。
- 🔄 **自动刷新模式改进**：自动刷新模式重新设计，仅在必要时使用属性描述符，减少性能开销。
- 🏭 **实体生成器默认值更新**：实体生成器现在使用反映现代 MikroORM 使用方式的默认值。
- ⚡ **类型级性能优化**：对关键类型进行重构，减少 TypeScript 编译器需要评估的类型实例化次数，提升 IDE 反馈和编译速度。
- 📖 **文档全面改进**：文档进行了大规模改进，包括刷新的主页、新的架构概述页面、重新组织的侧边栏、重写的入门指南以及扩展的参考部分。
- 🛠️ **开发者工具更新**：代码库从 ESLint 切换到 oxlint，并采用 oxfmt 进行格式化，提升开发效率。
- ⚠️ **重要的破坏性变更**：包括默认启用 `forceUtcTimezone`、外键规则与 `cascade` 选项解耦、`ReflectMetadataProvider` 不再默认、更严格的 `em.create()` 和 `em.assign()` 类型检查等。
- 🗃️ **新增 Oracle 数据库支持**：通过新的 `@mikro-orm/oracledb` 包支持 Oracle 数据库，使支持的数据库总数达到八个。
- 🖇️ **NestJS 适配器更新**：`@mikro-orm/nestjs` 适配器已更新以支持 v7 的所有新功能。

---

### [从 v6 升级到 v7 | MikroORM](https://mikro-orm.io/docs/upgrading-v6-to-v7)

**原文标题**: [Upgrading from v6 to v7 | MikroORM](https://mikro-orm.io/docs/upgrading-v6-to-v7)

MikroORM v7 是一个重大版本更新，引入了多项破坏性变更，主要转向原生 ESM 模块、更新核心依赖、重构 API 并增强类型安全性，同时移除了部分旧功能。

- 🚀 **原生 ESM 支持**：MikroORM v7 现在是一个原生的 ESM 包，要求 Node.js 22.17+ 和 TypeScript 5.8+。
- 📦 **装饰器包分离**：装饰器已移至独立的 `@mikro-orm/decorators` 包，并提供了传统和 ES 规范两种版本。
- 🔄 **查询运行器更换**：底层查询运行器从 `knex` 替换为 `kysely`，相关包名和 API 随之调整。
- 🛠️ **TypeScript CLI 支持改进**：CLI 的 TypeScript 加载机制更新，默认支持 `swc`、`tsx` 等多种加载器，`ts-node` 相关配置被移除或重命名。
- 🧪 **QueryBuilder 类型安全增强**：QueryBuilder 不再可直接 await，需使用 `.execute()` 或 `.getResult()`，并且在连接后能更好地跟踪别名以提供类型检查和自动补全。
- ⚙️ **配置与行为变更**：环境变量不再总是覆盖显式配置；默认加载策略改为 `balanced`；`forceUtcTimezone` 和 `processOnCreateHooksEarly` 选项现在默认启用。
- 🗑️ **API 移除与重命名**：移除了 `persistAndFlush`、`removeAndFlush`、`MikroORM.initSync` 等方法；`ArrayCollection` 类被合并到 `Collection`；多个 SchemaGenerator 和 Migrator 方法被重命名。
- 🔧 **内部重构与私有化**：大量内部类属性改用原生的 `#private` 字段，提高了封装性，可能影响依赖内部属性的自定义代码。
- 📝 **公式与回调签名更新**：公式、索引、检查约束等回调函数的签名改变，参数顺序调整，并引入了 `quote` 辅助函数来正确处理标识符引用。
- 🧹 **清理与依赖调整**：移除了对 `dotenv`、`umzug` 等包的内置支持，改为可选或需用户自行安装；`dataloader` 变为可选的 peer dependency。

---

### [使用 TypeScript 学习 Temporal 101 | 掌握 Temporal](https://learn.temporal.io/courses/temporal_101/typescript/?utm_source=newsletter&utm_medium=sponsorship&utm_campaign=newsletter-2026-03-12-node&utm_content=temporal101-typescript-node)

**原文标题**: [Temporal 101 with TypeScript | Learn Temporal](https://learn.temporal.io/courses/temporal_101/typescript/?utm_source=newsletter&utm_medium=sponsorship&utm_campaign=newsletter-2026-03-12-node&utm_content=temporal101-typescript-node)

本课程介绍Temporal平台的基础知识，通过TypeScript SDK构建应用，涵盖工作流、活动、故障恢复等核心概念，并提供实践工具。

- 🚀 学习Temporal平台基础：使用TypeScript SDK构建应用，掌握工作流与活动等核心模块
- 🛠️ 实践开发技能：配置开发环境，实现业务流程，并与外部服务通信
- 🔄 理解执行模型：探索Temporal的事件历史与故障恢复机制，提升应用可靠性
- 📊 使用管理工具：通过Web UI和命令行工具监控与管理工作流生命周期
- 🆓 免费自学课程：约2小时自主学习，适合有后端开发经验者，TypeScript基础非必需

---

### [GitHub - TryGhost/node-sqlite3: Node.js 的 SQLite3 绑定库 · GitHub](https://github.com/TryGhost/node-sqlite3)

**原文标题**: [GitHub - TryGhost/node-sqlite3: SQLite3 bindings for Node.js · GitHub](https://github.com/TryGhost/node-sqlite3)

这是一个已弃用的Node.js SQLite3绑定库，提供异步非阻塞的数据库操作功能。

- 🚫 项目已停止维护，不再更新问题或合并请求
- 🔌 支持异步查询、参数绑定及完整的Buffer/Blob处理
- 🧪 包含完整的测试套件，采用现代C++编写并检测内存泄漏
- 📦 默认捆绑SQLite v3.52.0，也可使用本地SQLite构建
- ⚡ 通过Node-API实现，预编译二进制支持Node v20.17.0+多个平台
- 🔧 支持从源码构建、自定义SQLite路径和SQLCipher加密扩展
- 📚 提供详细的API文档和多种安装方式（npm/yarn/源码）
- 🛡️ 采用BSD-3-Clause许可证，原由Mapbox创建，现由Ghost维护

---

### [GitHub - WiseLibs/better-sqlite3：Node.js 中最快且最简单的 SQLite3 库。· GitHub](https://github.com/WiseLibs/better-sqlite3)

**原文标题**: [GitHub - WiseLibs/better-sqlite3: The fastest and simplest library for SQLite3 in Node.js. · GitHub](https://github.com/WiseLibs/better-sqlite3)

better-sqlite3 是 Node.js 中最快、最简单的 SQLite 库，提供同步 API、完整事务支持、高性能与安全性，适合大多数 SQLite 使用场景，但在极高并发读写或超大数据库情况下可能不适用。

- 🚀 性能卓越：相比其他库，在多数操作中速度显著领先，支持完整的 SQLite 功能
- 🔧 同步易用：提供简单直观的同步 API，并支持 WAL 模式以优化性能
- 🛡️ 安全可靠：采用 JavaScript 内存管理，避免底层风险，保障稳定性
- 📊 适用场景广：适用于大多数应用，但极高并发或 TB 级数据库建议使用 PostgreSQL 等专业 RDBMS
- 💰 社区支持：鼓励企业赞助以维持项目长期发展，提供多种捐助方式
- 📦 安装简便：通过 npm 安装，支持当前 Node.js 版本，提供预编译二进制文件
- 🔄 升级需谨慎：升级前需查阅版本说明，可能涉及 API 变更或 SQLite 兼容性变化

---

### [SQLite | Node.js v25.8.1 文档](https://nodejs.org/api/sqlite.html)

**原文标题**: [SQLite | Node.js v25.8.1 Documentation](https://nodejs.org/api/sqlite.html)

Node.js v25.8.1 文档中的 `node:sqlite` 模块提供了同步操作 SQLite 数据库的功能，支持数据库连接管理、SQL 语句执行、预编译语句、用户自定义函数、数据备份以及变更集应用等核心操作。

- 🗄️ **模块概述**：`node:sqlite` 模块允许在 Node.js 中同步操作 SQLite 数据库，需通过 `node:` 前缀导入，目前处于发布候选阶段。
- 🔗 **数据库连接**：通过 `DatabaseSync` 类建立连接，支持文件或内存数据库，可配置只读模式、外键约束、超时等选项。
- 📝 **SQL 执行**：提供 `exec()` 方法执行无返回结果的 SQL 语句，以及 `prepare()` 方法创建预编译语句以提高效率与安全性。
- 🔧 **高级功能**：支持注册聚合函数与标量函数、设置授权回调进行访问控制、创建会话跟踪变更并生成变更集/修补集。
- 💾 **数据操作**：`StatementSync` 类提供 `run()`、`get()`、`all()`、`iterate()` 等方法执行预编译语句并处理结果。
- 🏷️ **语句缓存**：`SQLTagStore` 类作为 LRU 缓存，通过模板字面量标签复用预编译语句，提升性能并防止 SQL 注入。
- 🔄 **类型转换**：定义了 JavaScript 与 SQLite 数据类型（NULL、INTEGER、REAL、TEXT、BLOB）之间的自动转换规则。
- ⚙️ **实用工具**：包含 `backup()` 函数进行数据库备份，以及 `constants` 对象提供冲突解决与授权操作所需的常量。

---

### [发布 v12.7.0 · WiseLibs/better-sqlite3 · GitHub](https://github.com/WiseLibs/better-sqlite3/releases/tag/v12.7.0)

**原文标题**: [Release v12.7.0 · WiseLibs/better-sqlite3 · GitHub](https://github.com/WiseLibs/better-sqlite3/releases/tag/v12.7.0)

该页面显示了一个名为better-sqlite3的GitHub仓库的发布页面，其中v12.7.0版本被标记为预发布并存在两个主要问题：Electron v41的兼容性问题导致预构建文件缺失，以及SQLite 3.52.0版本存在严重问题需回退至3.51.3。页面还列出了相关的代码更改和贡献者信息。

- ⚠️ v12.7.0版本为预发布版本，存在两个关键问题使其无法正常使用。
- 🔌 Electron v41移除了某些函数，导致多个预构建文件缺失。
- 🐛 SQLite团队发现3.52.0版本存在严重问题，计划撤回并替换为修复后的3.51.3版本。
- 📝 本次更新包含了针对Electron v41的适配修复和Node v25的测试错误修复。
- 👥 该版本由mceachen和m4heshd两位贡献者共同完成。

---

### [GitHub - sebhildebrandt/systeminformation: Node.JS 系统信息库 · GitHub](https://github.com/sebhildebrandt/systeminformation)

**原文标题**: [GitHub - sebhildebrandt/systeminformation: System Information Library for Node.JS · GitHub](https://github.com/sebhildebrandt/systeminformation)

这是一个用于Node.js的系统和操作系统信息库，提供超过50个函数来获取详细的硬件、系统和OS信息，支持Linux、macOS、Windows、FreeBSD、OpenBSD、NetBSD、SunOS和Android平台。

- 📦 **项目概况**：Systeminformation是一个轻量级Node.js库，用于收集系统和硬件信息，无npm依赖，已发布超过700个版本，每月下载量高达2000万次。
- 🚀 **版本动态**：当前版本为5.x，包含音频、蓝牙、USB、打印机等新功能；即将发布的版本6将完全用TypeScript重写，带来API改进和新特性。
- ⚙️ **功能范围**：提供CPU、内存、磁盘、网络、电池、进程、Docker、虚拟化等50多个信息查询函数，覆盖系统监控的各个方面。
- 🖥️ **跨平台支持**：兼容Node.js、Bun和Deno运行时，支持多种操作系统，但明确不适用于浏览器环境。
- 📚 **使用方式**：支持回调、Promise和async/await三种调用方式，可通过npm安装或直接使用npx命令行工具快速体验。
- ⚠️ **注意事项**：某些功能如温度检测在macOS和Windows上可能需要额外权限或软件包支持，Linux的S.M.A.R.T.状态需要安装smartmontools。
- 🔄 **活跃开发**：项目持续维护，近期版本增加了USB序列号、WiFi信号质量、内存可回收空间等新特性，保持定期更新。

---

### [系统() 更新Mac 2026型号编号（macOS）· sebhildebrandt/systeminformation@6466144 · GitHub](https://github.com/sebhildebrandt/systeminformation/commit/64661445dbe0ddbe1ee33156748fcb26e4b961cc)

**原文标题**: [system() updated Mac 2026 mopdel numbers (mac OS) · sebhildebrandt/systeminformation@6466144 · GitHub](https://github.com/sebhildebrandt/systeminformation/commit/64661445dbe0ddbe1ee33156748fcb26e4b961cc)

systeminformation 库更新至版本 5.31.3，主要针对 macOS 系统信息识别功能进行了增强，新增了对 2026 年 Mac 型号的支持。

- 📝 版本 5.31.3 发布于 2026 年 3 月 4 日，主要更新了 `system()` 函数以支持 macOS 2026 年新款 Mac 的型号识别。
- 🔧 更新内容涉及多个文件，包括 CHANGELOG.md、docs/history.html、docs/index.html 和 lib/util.js，共计 58 行新增和 3 行修改。
- 🖥️ 在 lib/util.js 中新增了多个 2026 年 Mac 型号的识别数据，例如 MacBook Pro（14 英寸和 16 英寸，搭载 M5、M5 Pro 或 M5 Max 处理器）以及 MacBook Neo（14 英寸，搭载 A18 Pro 处理器）。
- 📈 文档页面（docs/index.html）的版本号已从 5.31.2 更新至 5.31.3，以反映此次发布。

---

### [发布 v2.0.0 · sindresorhus/emittery · GitHub](https://github.com/sindresorhus/emittery/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · sindresorhus/emittery · GitHub](https://github.com/sindresorhus/emittery/releases/tag/v2.0.0)

Emittery 2.0.0 版本发布，引入了重大变更、新功能及错误修复，主要更新包括监听器参数格式统一为对象、错误处理改进、Node.js 版本要求提升至 22，并新增生命周期钩子与 Disposable 支持等。

- 🚨 **重大变更**：监听器现在接收统一的 `{name, data}` 对象，而非原始数据，影响 `.on()`、`.onAny()`、`.once()` 及异步迭代器。
- ⚠️ **错误处理改进**：`emit()` 在多个监听器抛出错误时，现在抛出 `AggregateError` 收集所有错误，而非静默丢弃后续错误。
- 📦 **环境要求**：最低 Node.js 版本从 14.16 提升至 22。
- 🔧 **新功能**：新增 `init`/`deinit` 生命周期钩子，用于在监听器订阅/取消订阅时执行设置与清理逻辑。
- 🧹 **自动清理支持**：`.on()` 和 `.onAny()` 返回的取消订阅函数现在支持 `Disposable`，可与 `using` 语句配合实现自动资源管理。
- 🔄 **异步迭代器增强**：`.events()` 和 `.anyEvent()` 返回的异步迭代器现在支持 `AsyncDisposable`，适用于 `await using`。
- 🎛️ **外部控制支持**：为 `.events()`、`.anyEvent()` 和 `.once()` 添加 `AbortSignal` 支持，允许通过信号外部取消订阅。
- ⚙️ **配置扩展**：`.once()` 现在接受选项对象 `{predicate, signal}`，而不仅是谓词函数。
- 🏗️ **装饰器兼容**：`Emittery.mixin()` 现在同时支持旧版和 TC39 标准装饰器语法。
- 🐛 **错误修复**：解决了 `emit()` 静默丢弃多个监听器错误、调试日志器内部元事件噪音、子类中异步 `emit()` 覆盖被破坏、Proxy 包装失效及混合装饰器语法兼容性问题。

---

### [GitHub - verdaccio/verdaccio: 一个轻量级的Node.js私有代理注册表 · GitHub](https://github.com/verdaccio/verdaccio#readme)

**原文标题**: [GitHub - verdaccio/verdaccio: A lightweight Node.js private proxy registry · GitHub](https://github.com/verdaccio/verdaccio#readme)

Verdaccio 是一个轻量级、零配置的私有 npm 注册表，支持缓存公共包、代理其他注册表，并可通过插件扩展存储功能，适用于企业私有包管理、CI/CD 集成和依赖混淆防护等场景。

- 🏠 **私有包管理**：支持在企业内部使用私有 npm 包，无需公开代码，使用方式与公共包一样简便。
- 🔄 **缓存与代理**：可代理并缓存 npmjs.org 等公共注册表，减少延迟、提供故障转移，并避免公共包消失或 404 问题。
- 🔗 **多注册表链接**：通过 uplinks 功能链式连接多个注册表，实现从单一端点获取多个来源的包。
- ✏️ **包覆盖功能**：允许在本地发布修改后的第三方包版本，便于临时修复或测试。
- 🧪 **端到端测试**：轻量快速，适合 CI/CD 环境，被 create-react-app、Babel、Angular CLI 等多个知名项目用于集成测试。
- 🐳 **多方式部署**：支持通过 npm、yarn、pnpm 全局安装，或使用 Docker、Helm 进行容器化与云原生部署。
- 🔌 **插件生态**：提供插件生成器，支持扩展存储到 AWS S3、Google Cloud Storage 等服务，并可自定义插件。
- 🛡️ **安全与兼容**：支持 npm 主要功能（发布、安装、审计等），提供漏洞报告流程，并兼容 npm、pnpm、yarn 的常用命令。
- 🌍 **社区与支持**：由志愿者维护，接受捐赠，并提供详细的文档、视频教程和社区讨论渠道。

---

### [GitHub - sindresorhus/get-windows：获取活动窗口及已打开窗口的元数据（标题、ID、边界、所有者等）· GitHub](https://github.com/sindresorhus/get-windows)

**原文标题**: [GitHub - sindresorhus/get-windows: Get metadata about the active window and open windows (title, id, bounds, owner, etc) · GitHub](https://github.com/sindresorhus/get-windows)

这是一个用于获取活动窗口和打开窗口元数据的Node.js包，支持macOS、Linux和Windows系统。

- 🖥️ 支持跨平台：兼容macOS 10.14+、Linux（不支持Wayland）和Windows 7+
- 📦 功能丰富：可获取窗口标题、ID、位置尺寸、所属应用、浏览器URL等元数据
- 🔧 两种调用方式：提供异步（activeWindow()）和同步（activeWindowSync()）API
- 🌐 浏览器支持：macOS上可获取Chrome、Safari、Edge等主流浏览器的活动标签页URL
- ⚠️ 权限要求：macOS需要辅助功能和屏幕录制权限才能获取完整信息
- 📊 额外功能：支持获取所有打开窗口列表（openWindows()）和进程内存使用情况
- 🛠️ 开发友好：包含TypeScript类型定义，支持调试日志和Electron集成

---

### [Poku - 让测试变得简单](https://poku.io/)

**原文标题**: [Poku - Making Testing Easy](https://poku.io/)

Poku是一款免费开源的跨平台测试运行器，旨在为JavaScript测试带来简洁高效的体验，支持Node.js、Bun和Deno等多平台。

- 🐷 **核心定位**：免费开源的跨平台测试运行器，回归JavaScript测试的本质  
- ⚡️ **学习路径**：提供从初级断言测试到高级API、容器管理的渐进式教程  
- 🔧 **平台兼容**：支持同时为Node.js、Bun、Deno运行相同测试套件，包括多版本验证  
- 🏆 **应用实例**：已被MySQL2等开源项目采用，支持CommonJS/ES模块双模式测试  
- 🔄 **自举测试**：工具自身使用TypeScript编写并通过Poku进行无编译测试  
- 📦 **安装方式**：支持npm/bun/deno多种包管理器一键安装  
- 🌟 **开源生态**：采用MIT许可证，鼓励开发者通过GitHub星标支持项目发展

---

### [GitHub - mercurius-js/mercurius：使用Fastify实现GraphQL服务器和网关 · GitHub](https://github.com/mercurius-js/mercurius)

**原文标题**: [GitHub - mercurius-js/mercurius: Implement GraphQL servers and gateways with Fastify · GitHub](https://github.com/mercurius-js/mercurius)

Mercurius 是一个为 Fastify 框架设计的 GraphQL 适配器，提供高性能的 GraphQL 服务器和网关功能，支持订阅、联合和查询优化。

- 🚀 **高性能特性**：内置查询解析与验证缓存、自动加载器集成以避免 N+1 查询，并利用 graphql-jit 实现即时编译。
- 🔌 **扩展支持**：通过插件支持 GraphQL 联合（Federation）和网关（Gateway）功能，均包含订阅能力。
- 📦 **灵活查询**：支持批量查询和可自定义的持久化查询，提升数据处理效率。
- 📚 **完善文档**：提供详细的安装指南、快速入门、API 文档、示例代码及 TypeScript 使用说明。
- 🌐 **集成与安全**：兼容 HTTP 和 WebSocket 协议，包含相关插件集成和 CSRF 防护等安全特性。
- ⭐ **社区活跃**：项目在 GitHub 上获得大量关注，采用 MIT 许可证，由 NearForm 和 Platformatic 赞助维护。

---

### [GitHub - sqliteai/sqlite-js：用JavaScript创建自定义SQLite函数。直接在JavaScript中扩展数据库，支持标量、聚合、窗口函数和排序规则。· GitHub](https://github.com/sqliteai/sqlite-js)

**原文标题**: [GitHub - sqliteai/sqlite-js: Create custom SQLite functions in JavaScript. Extend your database with scalars, aggregates, window functions, and collations directly in JavaScript. · GitHub](https://github.com/sqliteai/sqlite-js)

SQLite-JS 是一个强大的扩展，允许在 SQLite 中使用 JavaScript 创建自定义函数、聚合函数、窗口函数和排序规则，从而直接在数据库内实现灵活的数据处理。

- 🚀 **功能扩展** – 支持创建标量函数、聚合函数、窗口函数和自定义排序规则，通过 JavaScript 代码增强 SQLite 的数据处理能力。
- 📦 **多平台安装** – 提供预编译二进制文件，支持 Linux、macOS、Windows、Android 和 iOS，并可通过 Swift、Android、Node.js 和 Flutter 等包管理器集成。
- 🔧 **函数创建示例** – 包括计算年龄、中位数、移动平均值等实用示例，展示如何通过 SQL 语句注册和使用 JavaScript 函数。
- 🔄 **同步与持久化** – 结合 sqlite-sync 可实现用户定义函数在 SQLite Cloud 集群中的自动同步和持久化，确保多设备间逻辑一致。
- 📚 **实用工具函数** – 提供 `js_eval` 直接执行 JavaScript 代码，以及 `js_version`、`js_load_text` 等辅助函数，便于版本查询和文件加载。
- ⚙️ **构建与许可** – 支持从源码构建，项目采用 Elastic License 2.0 许可，属于 SQLite AI 生态系统的一部分，旨在为边缘 AI 应用提供数据与推理引擎。

---

### [错误](https://nodeweekly.com/link/181993/web)

**原文标题**: [Error](https://nodeweekly.com/link/181993/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /sindresorhus/wallpaper (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [GitHub - Schniz/fnm: 🚀 快速简洁的 Node.js 版本管理器，基于 Rust 构建 · GitHub](https://github.com/Schniz/fnm)

**原文标题**: [GitHub - Schniz/fnm: 🚀 Fast and simple Node.js version manager, built in Rust · GitHub](https://github.com/Schniz/fnm)

fnm 是一个用 Rust 编写的快速、跨平台的 Node.js 版本管理器，支持自动版本切换和多种安装方式。

- 🚀 快速且跨平台支持（macOS、Windows、Linux），基于 Rust 构建
- 📦 提供多种安装方式，包括脚本、Homebrew、Winget、Scoop、Cargo 和二进制文件
- ⚙️ 支持通过 `.node-version` 和 `.nvmrc` 文件自动切换 Node.js 版本
- 🐚 兼容多种 Shell（Bash、Zsh、Fish、PowerShell、Windows CMD），并提供自动补全功能
- 🔧 可通过配置启用高级功能，如使用 `--use-on-cd` 参数实现目录自动版本切换
- 🛠️ 项目开源，鼓励贡献，提供完整的开发、测试和运行指南

---

### [ESLint v10.0.3 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/03/eslint-v10.0.3-released/)

**原文标题**: [ESLint v10.0.3 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/03/eslint-v10.0.3-released/)

ESLint v10.0.3 是一个补丁版本，主要修复了之前版本中的多个错误，并更新了依赖项和文档。

- 🔧 修复了 minimatch 依赖版本，避免因旧版本 bug 导致 ESLint 无法识别某些文件的问题
- 🐛 修复了 `no-useless-assignment` 规则中未包含变量名的错误提示信息
- 📚 更新了 README 和迁移指南，移除了已弃用的 eslintrc 文档文件
- 🛠️ 简化了 `isCombiningCharacter` 辅助函数，并更新了 TypeScript 最低支持版本至 5.3
- ⚙️ 调整了 Node.js 版本要求，并更新了相关配置和 CI 设置

---

### [ESLint v9.39.4 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/03/eslint-v9.39.4-released/)

**原文标题**: [ESLint v9.39.4 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/03/eslint-v9.39.4-released/)

ESLint v9.39.4 是一个补丁版本，主要修复了先前版本中的多个错误，包括更新依赖项以解决安全漏洞和文件识别问题。

- 🔧 修复了 minimatch 依赖版本，避免因旧版本 bug 导致 ESLint 无法识别某些文件的问题
- 🛡️ 更新了 transitive dependency 以修补最近发布的安全漏洞
- 🐛 修复了与 @eslint/eslintrc 和 ajv 相关的安全漏洞
- 📄 文档部分添加了弃用通知
- 🔄 完成了针对 ESLint v9.39.4 的依赖更新和 CI 配置调整

---

### [pnpm 10.32 | pnpm](https://pnpm.io/blog/releases/10.32)

**原文标题**: [pnpm 10.32 | pnpm](https://pnpm.io/blog/releases/10.32)

pnpm 10.32版本引入了`--all`标志以简化构建批准流程，并包含了一些修复性调整。

- 🚀 新增`--all`标志，允许通过`pnpm approve-builds --all`一键批准所有待处理构建，无需交互提示
- 🔧 撤销了先前与npm配置文件路径设置相关的更改，以解决回归问题
- 🔧 回退了`lockfile-include-tarball-url`相关修复，以处理特定问题

---

### [发布 7.5.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.5.0)

**原文标题**: [Release 7.5.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.5.0)

Prisma ORM 发布了 7.5.0 稳定版本，主要增强了嵌套事务回滚支持，修复了多项客户端与引擎的 bug，并大幅优化了 Prisma Studio 的用户体验，新增了多单元格选择、全表搜索、命令面板和原始 SQL 查询等功能。

- 🎉 Prisma ORM 7.5.0 稳定版发布，包含多项功能增强与错误修复
- 🔄 ORM 新增对嵌套事务通过保存点进行回滚的支持，提升事务处理可靠性
- 🐛 修复了 Prisma Client 中 DbNull 序列化、DateTime 字段返回无效日期及游标分页等问题
- 🛠️ Schema Engine 优化了部分索引的处理逻辑，避免不必要的迁移与重建
- 🖥️ Prisma Studio 引入多单元格选择、全表搜索、更直观的过滤界面和 Cmd+K 命令面板
- 📊 Studio 新增原始 SQL 查询功能，支持直接对数据库执行自定义查询
- 💼 提供企业级支持计划，涵盖优先问题处理、性能调优与定制化培训
- 🧑💻 Prisma 正在招聘，鼓励开发者加入团队共同成长

---

### [如何通过开启GitHub议题窃取npm发布令牌 — Neciu Dan](https://neciudan.dev/cline-ci-got-compromised-here-is-how)

**原文标题**: [How to steal npm publish tokens by opening GitHub issues — Neciu Dan](https://neciudan.dev/cline-ci-got-compromised-here-is-how)

本文详细分析了Cline CLI被攻击的事件，攻击者通过一系列漏洞和巧妙策略窃取了npm发布令牌，并利用其在npm上发布了恶意版本。文章解释了攻击链条，包括GitHub问题中的提示注入、GitHub Actions缓存污染，以及最终如何窃取令牌发布恶意包。同时提供了防护建议，如禁用npm生命周期脚本、使用npm ci、检查npm审计签名等。

- 🛡️ **攻击概述**：攻击者通过GitHub问题的提示注入漏洞，在Cline仓库的AI工单分类机器人中执行任意命令，进而污染GitHub Actions缓存，窃取npm发布令牌，最终发布了包含恶意postinstall脚本的Cline@2.3.0版本。
- 🤖 **漏洞源头**：Cline仓库配置的AI工单分类机器人存在权限问题，允许任何GitHub用户通过问题标题触发提示注入，使Claude AI在Actions运行器上执行具有Bash、读写权限的命令。
- 💾 **缓存污染**：攻击者利用低权限运行器向共享缓存写入大量数据，触发LRU清理机制，清除合法缓存后，使用相同键值注入恶意node_modules目录，从而在夜间发布工作流中恢复恶意环境。
- 🔑 **令牌窃取**：夜间发布工作流在恢复被污染的缓存后，运行在受控环境中，攻击者嵌入的代码成功读取并外泄NPM_RELEASE_TOKEN，用于发布恶意包。
- 📦 **恶意发布**：被盗令牌发布的Cline@2.3.0版本在package.json中添加了postinstall脚本，全局安装OpenClaw（一个合法的AI助手工具），但其本地服务存在未授权访问漏洞（CVE-2026-25253），可能危及CI环境中的敏感信息。
- ✅ **防护措施**：建议在.npmrc中设置ignore-scripts=true禁用脚本，使用npm ci替代npm install确保依赖一致性，在CI中运行npm audit signatures检查来源证明，并审查依赖项的构建和发布流程。
- 📚 **延伸资源**：文章提供了事件完整报告、npm安全最佳实践指南的链接，以及作者为前端开发者制作的免费安全课程，涵盖攻击原理、防御策略和工具使用。

---

### [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS 压缩性能基准测试：babel-minify、esbuild、terser、uglify-js、swc、google closure compiler、tdewolff/minify、oxc-minify · GitHub](https://github.com/privatenumber/minification-benchmarks)

**原文标题**: [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS minification benchmarks: babel-minify, esbuild, terser, uglify-js, swc, google closure compiler, tdewolff/minify, oxc-minify · GitHub](https://github.com/privatenumber/minification-benchmarks)

该项目对多个JavaScript代码压缩工具进行了性能基准测试，旨在帮助开发者根据压缩效果和速度选择适合的工具。

- 🏆 **最佳综合表现**：@swc/core在压缩率和速度之间取得了最佳平衡，多次在测试中名列前茅
- ⚡ **最快压缩工具**：@cminify/cminify-linux-x64在速度方面表现突出，但压缩效果相对较弱
- 📦 **最佳压缩效果**：uglify-js在多个测试中实现了最小的Gzip压缩体积，但速度较慢
- 🚀 **新兴竞争者**：oxc-minify在大型文件压缩中表现出色，兼具良好的压缩效果和速度
- ⏱️ **测试方法**：采用独立进程执行，验证压缩前后代码完整性，综合评估压缩体积和耗时
- 📊 **评估指标**：重点关注Gzip压缩后体积（影响网络传输）和压缩时间，采用加权评分进行排名
- ❌ **淘汰工具**：babel-minify和tedivm/jshrink在某些测试用例中出现压缩失败
- 🔄 **持续更新**：通过自动化PR和GitHub Actions保持基准测试数据的最新性

---

### [GitHub - swc-project/swc：基于Rust的Web平台 · GitHub](https://github.com/swc-project/swc)

**原文标题**: [GitHub - swc-project/swc: Rust-based platform for the Web · GitHub](https://github.com/swc-project/swc)

SWC是一个用Rust编写的超快速TypeScript/JavaScript编译器，旨在提升Web开发效率。它同时为Rust和JavaScript提供库支持，并注重版本兼容性与开发体验。

- 🚀 **高性能编译器**：采用Rust编写，编译速度极快，支持TypeScript和JavaScript
- 🔧 **多语言支持**：同时提供Rust库（通过parser入口）和JavaScript接口
- 📦 **版本稳定性**：确保所有crate最新版本兼容，MSRV（最低支持Rust版本）为1.73
- 🌐 **广泛兼容**：支持Node v10+运行环境，Node v20+开发环境
- 📊 **功能完善**：提供与Babel的详细对比和性能基准测试结果
- 🤝 **社区驱动**：由志愿者维护，通过OpenCollective接受赞助，提供Discord和GitHub讨论区
- 📄 **开源协议**：基于Apache License 2.0分发，文档和架构说明齐全
- 📈 **项目活跃**：拥有33.3k星标、1.4k分支，持续发布新版本（最新为2026年3月）

---

### [GitHub - tdewolff/minify: 适用于网页格式的Go压缩工具 · GitHub](https://github.com/tdewolff/minify)

**原文标题**: [GitHub - tdewolff/minify: Go minifiers for web formats · GitHub](https://github.com/tdewolff/minify)

Minify 是一个用 Go 语言编写的高性能压缩工具库，支持 HTML5、CSS3、JS、JSON、SVG 和 XML 等多种格式的压缩，通过移除不必要的空白字符和注释来减小文件大小，提升网络传输效率。该库设计注重性能，在各类基准测试中表现优异，并提供了丰富的 API 和自定义扩展能力。

- 📦 **支持多种格式**：提供 HTML、CSS、JS、JSON、SVG 和 XML 的压缩功能，并能处理嵌入式资源。
- ⚡ **高性能设计**：在压缩速度和效率上表现突出，通常比其他工具快几个数量级。
- 🔧 **灵活可扩展**：允许用户基于 MIME 类型或正则表达式添加自定义压缩器或调用外部命令。
- 🌐 **跨平台绑定**：提供 CLI 工具及 Python、JavaScript、.NET 等语言绑定，便于集成。
- 📊 **全面测试覆盖**：追求 100% 测试覆盖率，并进行模糊测试以确保稳定性和安全性。
- 🛠️ **丰富的配置选项**：各压缩器提供多种选项（如保留注释、空格、精度控制等）以适应不同需求。
- 🔄 **中间件支持**：提供 HTTP 中间件，可实时压缩响应内容，并建议配合缓存使用。
- 📈 **持续发展路线**：计划通过 SIMD 优化、变量缩短、源映射生成等功能进一步改进性能与功能。

---

### [获取失败](https://nodeweekly.com/link/182003/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/182003/web)

无法总结：获取内容失败，状态码 502。

---

### [JSLinux](https://bellard.org/jslinux/)

**原文标题**: [JSLinux](https://bellard.org/jslinux/)

JSLinux 是一个在浏览器中运行 Linux 或其他操作系统的在线模拟器平台，提供多种 CPU 架构和操作系统的即时访问。

- 🌐 支持 x86_64、x86 和 riscv64 等多种 CPU 架构的模拟系统
- 🐧 提供 Alpine Linux、Windows 2000、FreeDOS 和 Fedora 等多种操作系统选项
- 🖥️ 包含控制台、X Window 和图形界面等多种用户界面选择
- ⚙️ 部分系统支持 VFsync 功能，提升显示性能
- 🚀 通过点击链接即可快速启动对应模拟环境
- 📝 提供技术说明和特殊提示（如右键菜单、启动时间警告等）

---

### [JSLinux](https://bellard.org/jslinux/vm.html?cpu=x86_64&url=alpine-x86_64.cfg&mem=256)

**原文标题**: [JSLinux](https://bellard.org/jslinux/vm.html?cpu=x86_64&url=alpine-x86_64.cfg&mem=256)

Fabrice Bellard的个人网站，包含新闻、虚拟机列表、常见问题解答和技术笔记等资源。

- 📰 新闻动态
- 🖥️ 虚拟机列表
- ❓ 常见问题
- 📝 技术笔记

---

### [应对GitHub近期可用性问题 - GitHub博客](https://github.blog/news-insights/company-news/addressing-githubs-recent-availability-issues-2/)

**原文标题**: [Addressing GitHub’s recent availability issues - The GitHub Blog](https://github.blog/news-insights/company-news/addressing-githubs-recent-availability-issues-2/)

GitHub近期遭遇多次服务可用性问题，承认未达到自身可靠性标准，并正采取措施提升系统韧性。

- 🚨 **近期多次服务中断**：2月2日、2月9日和3月5日发生重大可用性与性能事故，影响多项服务。
- 📈 **根本原因分析**：快速增长的用户负载暴露架构扩展限制，包括架构耦合导致问题蔓延、系统无法有效隔离异常客户端负载。
- 🗓️ **2月9日事故详情**：核心数据库集群过载，起因包括热门客户端应用更新导致API读取流量激增、缓存刷新时间调整，以及工作日高峰负载叠加。
- ⚙️ **GitHub Actions事故**：2月2日因配置问题导致托管运行器中断；3月5日Redis集群故障转移后出现写入故障，暴露潜在配置缺陷。
- 🛠️ **短期改进措施**：重新设计用户缓存系统、加速容量规划、隔离关键依赖项以降低级联风险、实施流量优先级保护。
- 🌐 **长期架构投资**：迁移至Azure基础设施以支持弹性扩展，目标7月前50%流量由Azure处理；推进服务解耦，实现独立扩展与故障隔离。
- 📢 **透明度承诺**：通过状态页面和月度可用性报告公开事故详情，将持续向社区通报进展。

---

