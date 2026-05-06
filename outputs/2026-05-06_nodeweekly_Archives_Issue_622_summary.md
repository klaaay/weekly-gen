### [Node 周刊第 622 期：2026 年 4 月 30 日](https://nodeweekly.com/issues/622)

**原文标题**: [Node Weekly Issue 622: April 30, 2026](https://nodeweekly.com/issues/622)

以下是您提供的Node Weekly内容的总结：

Node.js 26.0因macOS问题推迟至5月5日发布，Temporal API默认启用；pnpm 11.0引入SQLite包索引；Fresh 2.3支持WebSocket；以及其他工具更新和生态动态。

- 📅 **Node 26.0推迟至5月5日**：因Rosetta 2兼容性问题，Temporal API默认启用，RC 2已发布。
- 🚀 **pnpm 11.0发布**：新增SQLite包索引、原生发布工具、全局安装隔离和供应链保护。
- 🍋 **Fresh 2.3更新**：Deno全栈框架新增WebSocket支持，优化JavaScript加载，简化View Transitions API。
- 🛠 **工具与库更新**：portless提供稳定本地URL；AVA 8.0完全支持ESM；Hono Node.js适配器2.0性能提升；BWIP-JS 4.10支持100+条码标准。
- 📊 **数据可视化新方式**：Datatype可变字体可用纯文本渲染图表，无需JS或图片。
- 🔧 **Postgres与SQLite扩展**：Honker为SQLite添加NOTIFY/LISTEN事件；TimescaleDB提升Postgres分析性能。
- 📰 **生态动态**：GitHub可靠性争议持续，Ghostty项目离开GitHub；Ubuntu 26.04 LTS发布，支持至2031年。
- 🤖 **Cloudflare代理技能**：支持代理开发工具，代理可自主创建Cloudflare账户。

---

### [JavaScript 中真正的新特性（以及即将到来的更新）— Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

以下是您提供的文章摘要：

本文章详细介绍了JavaScript语言的最新发展，包括已发布的ES2025新特性、即将到来的ES2026新功能，以及一些仍在开发中的重要提案。文章还提供了如何让AI编程助手使用这些新特性的实用建议。

- 📜 **ES2025 已发布**：ECMAScript 2025 已于2025年6月正式批准，带来了多项实用新特性。
- 🔄 **迭代器辅助方法**：为迭代器添加了 `.map()`, `.filter()`, `.take()`, `.toArray()` 等方法，支持惰性求值，无需先转换为数组。
- 🧮 **Set 新方法**：Set 类型新增了 `.union()`, `.intersection()`, `.difference()` 等标准集合操作，且不会修改原 Set。
- 📦 **JSON 模块**：现在可以使用 `import config from './config.json' with { type: 'json' }` 原生导入JSON文件。
- 🎯 **Promise.try**：提供了一种更简洁的方式来处理可能同步或异步且可能抛出错误的函数，统一了错误处理路径。
- 🔒 **RegExp.escape**：用于安全地转义用户输入中的正则表达式特殊字符，避免手动编写易出错的转义函数。
- 📊 **Float16Array**：新增16位浮点数类型数组，主要用于WebGPU和机器学习等场景，内存占用减半。
- 🌍 **国际化增强**：新增 `Intl.DurationFormat` 和 `Intl.Locale` 信息访问器，简化了本地化日期、时长等信息的处理。
- 🚀 **ES2026 即将到来**：TC39已批准ES2026候选草案，预计2026年6月正式批准。
- ➕ **Math.sumPrecise**：使用Shewchuk算法精确计算浮点数数组的和，避免了 `reduce` 累加带来的精度误差。
- 🔢 **Uint8Array base64/hex**：为 `Uint8Array` 添加了原生 `toBase64()`, `toHex()`, `fromBase64()`, `fromHex()` 方法，告别手写工具函数。
- ❌ **Error.isError**：提供了一个跨realm（如iframe、Worker）可靠的错误对象检测方法，解决了 `instanceof` 的局限性。
- 🔗 **Iterator.concat**：允许将多个迭代器连接成一个，无需手动编写生成器函数。
- 📝 **Map.getOrInsert**：为Map和WeakMap添加了 `getOrInsert` 和 `getOrInsertComputed` 方法，简化了“获取或插入默认值”的常见模式。
- 📥 **Array.fromAsync**：`Array.from` 的异步版本，用于将异步可迭代对象收集到一个数组中。
- 📄 **JSON.parse 保留源文本**：`JSON.parse` 的reviver函数现在可以访问原始JSON文本，便于精确处理大数字等场景。
- 🕰️ **Temporal (ES2027)**：用于替代 `Date` 的新日期时间API已到Stage 4，计划在ES2027中发布，浏览器实现已趋成熟。
- 🔑 **using 关键字 (Stage 3)**：用于资源管理，可自动在作用域结束时释放资源（如文件句柄、数据库连接），类似Python的 `with` 语句。
- ⏳ **import defer (Stage 3)**：允许延迟执行模块的顶层代码，仅在首次访问其导出时执行，有助于减少应用启动时间。
- 🤖 **AI 编程助手适配**：文章指出当前AI模型训练数据滞后，并提供了一个可直接用于 `.cursorrules` 等配置的现代JavaScript偏好指令集，帮助AI生成ES2025/2026风格的代码。

---

### [JavaScript 中真正的新特性（以及即将到来的更新）—— Neciu Dan](https://neciudan.dev/whats-new-in-javascript#mathsumprecise)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript#mathsumprecise)

以下是您提供的文章的中文摘要，包含概述和要点列表。

概述总结
本文详细介绍了JavaScript语言的最新发展，包括已正式发布的ES2025新特性、即将在ES2026中落地的功能，以及仍在推进中的提案。文章还提供了如何让AI编程助手使用这些新特性的实用指南。

- 🔧 **迭代器辅助方法**：ES2025新增了 `Iterator.prototype` 上的 `.map()`、`.filter()`、`.take()` 等方法，支持惰性求值，无需先将迭代器转为数组，尤其适合处理无限序列或大型数据流。
- 🔗 **集合方法**：ES2025为 `Set` 新增了 `union()`、`intersection()`、`difference()` 等非破坏性方法，参数支持“类集合”对象，简化了集合运算。
- 📦 **JSON模块**：ES2025允许使用 `import config from './config.json' with { type: 'json' }` 原生导入JSON文件，需配合导入属性以确保安全。
- 🎯 **Promise.try**：ES2025引入 `Promise.try()`，统一处理同步或异步、可能抛出异常的函数，所有结果都通过 `.then()` / `.catch()` 链处理，避免了额外微任务延迟。
- 🔒 **RegExp.escape**：ES2025提供 `RegExp.escape()` 方法，安全转义用户输入中的正则特殊字符，防止注入攻击，并采用十六进制转义首个字符以增强安全性。
- 🧮 **Float16Array**：ES2025新增16位浮点数类型数组，内存占用为 `Float32Array` 的一半，主要用于WebGPU、TensorFlow.js等场景。
- 🌐 **Intl 增强**：ES2025新增 `Intl.DurationFormat` 和 `Intl.Locale` 信息访问器，提升国际化能力。
- ➕ **Math.sumPrecise**：ES2026将引入 `Math.sumPrecise()`，使用Shewchuk算法高精度求和，避免浮点数累加误差。
- 🔢 **Uint8Array base64和hex**：ES2026将为 `Uint8Array` 添加原生的 `toBase64()`、`toHex()` 等方法，告别手动编码。
- ❌ **Error.isError**：ES2026引入 `Error.isError()`，可靠地跨领域（如iframe、Worker）检测错误对象，避免 `instanceof` 的局限性。
- 🔗 **Iterator.concat**：ES2026提供 `Iterator.concat()`，无需生成器包装即可直接串联多个迭代器。
- 📝 **Map.getOrInsert**：ES2026为 `Map` 和 `WeakMap` 新增 `getOrInsert()` 和 `getOrInsertComputed()` 方法，简化“获取或插入”模式。
- 📥 **Array.fromAsync**：ES2026引入 `Array.fromAsync()`，将异步可迭代对象收集为数组，替代手动 `for await...of` 循环。
- 📄 **JSON.parse 源文本**：ES2026为 `JSON.parse` 的reviver函数新增 `context` 参数，提供原始源文本，便于精确处理大数字。
- ⏳ **Temporal**：已进入Stage 4，预计ES2027发布，是 `Date` 的现代化替代方案，支持时区、ISO 8601字符串解析，并提供 `PlainDate`、`ZonedDateTime` 等类型。
- 🔑 **using关键字**：仍为Stage 3，用于资源管理，自动在作用域结束时执行清理（如关闭文件、数据库连接），支持同步和异步。
- 📦 **import defer**：仍为Stage 3，允许延迟模块评估，仅在首次访问命名空间属性时执行模块代码，优化启动性能。
- 🤖 **AI助手建议**：文章提供了让AI编程助手（如Claude Code）优先使用ES2025/ES2026新特性的配置方法，包括安装插件或设置 `.cursorrules`，确保生成代码符合最新标准。

---

### [JavaScript 中真正的新特性（以及接下来会发生什么）—— Neciu Dan](https://neciudan.dev/whats-new-in-javascript#mapgetorinsert-upsert)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript#mapgetorinsert-upsert)

以下是您提供的文章内容的摘要：

概述总结
ES2025 已正式发布，ES2026 即将到来。本文详细介绍了 JavaScript 中已可用的新特性、即将推出的功能，以及如何让 AI 工具使用这些现代语法。

- 📜 **规范制定流程**：TC39 委员会负责 ECMAScript 规范，提案需经过从 Stage 0（构思）到 Stage 4（完成）的五个阶段，最终被纳入年度语言快照。
- 🚀 **ES2025 核心特性：迭代器助手**：为迭代器原生添加了 `.map()`、`.filter()`、`.take()` 等方法，支持惰性求值，无需先转换为数组即可处理无限或大型数据流。
- 🔧 **ES2025 核心特性：Set 方法**：Set 类型新增了 `union`、`intersection`、`difference` 等标准集合操作，且不修改原 Set。
- 📦 **ES2025 其他特性**：包括原生 JSON 模块导入（需 `with { type: 'json' }`）、处理同步/异步函数的 `Promise.try()`、安全的 `RegExp.escape()`、节省内存的 `Float16Array` 以及 `Intl.DurationFormat` 等国际化功能。
- ⏳ **ES2026 即将到来：Math.sumPrecise**：使用 Shewchuk 算法精确计算浮点数之和，避免了 `reduce` 累加时的精度损失。
- 🔄 **ES2026 即将到来：其他实用更新**：包括 `Uint8Array` 的原生 Base64/Hex 转换、跨 realm 可靠的 `Error.isError()`、用于连接迭代器的 `Iterator.concat()`、简化 Map 操作的 `getOrInsert`、异步收集的 `Array.fromAsync()` 以及可获取原始 JSON 文本的 `JSON.parse` 增强。
- 🌐 **即将到来但未纳入 ES2026**：`Temporal`（日期时间替代方案，预计 ES2027）、`using` 关键字（资源自动清理，仍为 Stage 3）和 `import defer`（延迟模块执行，仍为 Stage 3）虽已可部分使用，但未进入 ES2026 规范。
- 🤖 **AI 编码助手指南**：当前 AI 模型训练数据过时，建议通过配置 `.cursorrules` 或安装插件等方式，引导 AI 优先使用 `Map.getOrInsert`、`Temporal`、`Error.isError` 等现代 API，而非旧模式。

---

### [TimescaleDB — 排名第一的时间序列数据库 | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是一个基于 PostgreSQL 构建的时序数据库，提供高性能、实时分析和压缩功能，适用于传感器、链上数据和客户数据等场景。

- 🐯 **核心产品**：Tiger Cloud 弹性云平台、TimescaleDB Enterprise 自管理版、以及开源 TimescaleDB，支持时序、实时分析和向量搜索。
- 📊 **自动分区**：Hypertables 自动按时间或 ID 分区，实现快速写入和可预测查询，支持分区跳过和高效索引扫描。
- 💾 **混合存储**：行存储用于快速写入，列存储用于快速查询，自动转换并支持 SIMD 向量化操作，压缩率高达 95%。
- 🔄 **增量物化视图**：Continuous Aggregates 实现增量刷新，支持实时模式包含最新数据，适合即时仪表盘。
- ⚙️ **自动化管理**：内置作业调度器，支持列存储、保留策略和聚合刷新的自动化，具备完整审计能力。
- 🧮 **时序函数**：Hyperfunctions 提供约 200 个原生 SQL 函数，简化时间加权平均、插值等高级分析。
- 🌟 **客户成果**：Cloudflare、Replicated、orca.so 等客户验证了其平衡简单性与高性能的优势。
- 🤝 **社区驱动**：22K+ GitHub Stars、12K+ Slack 成员，支持 Helm 部署，强调开源和 PostgreSQL 兼容性。
- 🚀 **快速入门**：提供免费试用、开源下载和 Helm 安装命令，可查询数十亿行数据，响应时间毫秒级。

---

### [2026-05-05，版本26.0.0（当前版）由RafaelGSS提交 · 拉取请求 #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526)

**原文标题**: [2026-05-05, Version 26.0.0 (Current) by RafaelGSS · Pull Request #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526)

Node.js 26.0.0 正式发布，带来多项重大更新，包括 Temporal API 默认启用、V8 引擎升级、Undici 更新以及多项弃用和移除。

- 🎉 **Temporal API 默认启用**：现代日期/时间 API 替代传统 Date 对象，提供更强大和丰富的功能。
- ⚡ **V8 引擎升级至 14.6**：包含 `Map.prototype.getOrInsert()` 和 `Iterator.concat()` 等新特性。
- 🌐 **Undici 更新至 8.0.2**：Node.js HTTP 客户端实现获得新功能和改进。
- 🗑️ **多项弃用和移除**：包括 `http.writeHeader()`、`_stream_*` 模块的完全移除，以及 `module.register()` 的运行时弃用。
- 🔧 **构建系统更新**：GCC 要求提升至 13.2，放弃 Python 3.9 支持，目标 Power 9 架构。
- 🔒 **安全修复**：修复了数组索引哈希碰撞漏洞 (CVE-2026-21717)。
- 🚀 **性能优化**：流处理改进、代理对象检查优化等。

---

### [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

**原文标题**: [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

Temporal 是 JavaScript 中全新的日期时间管理API，旨在全面替代存在缺陷的 Date 对象，提供更强大、更清晰的日期时间处理能力。

- 🕐 Temporal 不是构造函数，而是像 Math 一样的静态命名空间，包含多个专门处理日期时间不同方面的类
- 📅 Date 对象存在根本性设计缺陷：同时承担时间戳和日期组件双重角色，导致开发者容易混淆和误用
- 🌍 Temporal 解决了 Date 缺乏时区支持的问题，提供 ZonedDateTime 处理任意时区，以及 Plain 系列处理无时区日期时间
- 🗓️ Temporal 支持多种日历系统（如希伯来历、中国农历等），而 Date 只支持公历
- 🔧 API 设计遵循"每个类做更少事"原则，通过 Instant、ZonedDateTime、PlainDateTime、PlainDate、PlainTime、PlainYearMonth、PlainMonthDay、Duration 等类清晰分离职责
- 📊 所有类共享统一的方法接口：构造、更新、算术、比较、序列化等，便于学习和使用
- 🔄 类之间提供丰富的转换方法，支持在不同时间表示形式间灵活切换
- 📝 使用 RFC 9557 格式进行序列化，支持纳秒级精度和时区/日历系统指定
- ⏳ 支持日期范围约为 ±10⁸ 天（从 -271821 年到 +275760 年），与 Date 兼容
- 🚫 避免常见误区：不假设年份天数、月份数量、星期长度，使用 daysInYear/monthsInYear/daysInWeek 等属性
- 🔒 所有 setter 方法返回新实例而非修改原对象，避免副作用

---

### [为Temporal启用Rust支持 · Issue #58730 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/58730#issuecomment-4336293111)

**原文标题**: [Enabling Rust support for Temporal · Issue #58730 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/58730#issuecomment-4336293111)

Node.js 正在考虑为 Temporal 功能添加 Rust 支持，但目前面临一些构建和依赖管理方面的挑战。

- 🕐 Temporal 功能基于 Rust 库 (temporal_rs 和 icu4x) 实现，V8 已支持但 Node.js 尚未启用
- 🔧 V8 新增了 v8_enable_temporal_support 选项，默认开启但在 Node 构建中被禁用
- 📦 Node.js 需要解决 Rust 依赖和工具链的 vendoring 问题，避免引入 Chrome 的全部 Rust 依赖
- 🚀 该功能仍在开发中，距离正式发布还有一段时间，但需要提前规划集成方案
- 🤝 贡献者表示愿意帮助上游推进相关工作

---

### [为Temporal启用Rust支持 · Issue #58730 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/58730#issuecomment-4351809373)

**原文标题**: [Enabling Rust support for Temporal · Issue #58730 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/58730#issuecomment-4351809373)

Node.js 正考虑引入对 Temporal 的支持，该功能依赖于 Rust 库，需要解决依赖管理和构建系统问题。

- 🕐 概述：V8 中已实现基于 Rust 的 Temporal 支持，Node.js 需跟进但面临依赖管理挑战
- 🔧 技术背景：Temporal 功能基于 temporal_rs 和 icu4x 两个 Rust 库实现，需要 Rust 工具链支持
- ⚙️ 当前状态：V8 已添加 v8_enable_temporal_support 选项，默认启用但在 Node 构建中禁用
- 📦 依赖问题：Node 需要处理 V8 的 third_party/rust 依赖，可能包含大量 Chrome 所需的额外 Rust 依赖
- 🛠️ 解决方案探讨：Node 可能需要构建系统层面的处理，选择性下载所需依赖而非全部纳入代码仓库
- 🤝 协作需求：开发者 Manishearth 已发起讨论，表示愿意协助上游整合工作

---

### [/download/rc/v26.0.0-rc.2/ 的索引](https://nodejs.org/download/rc/v26.0.0-rc.2/)

**原文标题**: [Index of /download/rc/v26.0.0-rc.2/](https://nodejs.org/download/rc/v26.0.0-rc.2/)

这是 Node.js v26.0.0 第二个候选发布版的下载目录，包含适用于多种操作系统的安装包和源码。

- 📁 包含 docs/、win-arm64/、win-x64/ 等子目录
- 🔐 提供 SHASUMS256.txt 校验文件（3.0 KB，2026-04-28）
- 🐧 Linux 版本：支持 x64、arm64、ppc64le、s390x 架构，提供 .tar.gz 和 .tar.xz 格式
- 🍎 macOS 版本：支持 arm64 和 x64 架构，提供 .tar.gz 和 .tar.xz 格式
- 🪟 Windows 版本：支持 x64 和 arm64 架构，提供 .msi、.7z、.zip 格式
- 📦 提供 headers 头文件包（.tar.gz 和 .tar.xz）
- 📜 提供完整源码包 node-v26.0.0-rc.2.tar.gz（118 MB）和 .tar.xz（57 MB）

---

### [pnpm 11.0 | pnpm](https://pnpm.io/blog/releases/11.0)

**原文标题**: [pnpm 11.0 | pnpm](https://pnpm.io/blog/releases/11.0)

以下是 pnpm 11.0 版本的总结：

pnpm 11.0 版本带来了多项重大改进，包括增强安全默认设置、原生发布流程、SQLite 存储索引以及隔离的全局安装，同时要求 Node.js 22 或更高版本。

- 🔒 安全默认设置增强：`minimumReleaseAge` 默认设为 1440 分钟（1天），`blockExoticSubdeps` 默认启用，新增 `allowBuilds` 配置替代旧版构建依赖设置。
- 🗄️ 全新 SQLite 存储索引：使用单一 SQLite 数据库替代数百万 JSON 文件，支持十六进制摘要和捆绑清单，减少系统调用并加快安装速度。
- 🌐 原生发布流程：`pnpm publish`、`login`、`logout` 等命令不再依赖 npm CLI，支持交互式 OTP 和二维码认证。
- 🧩 隔离全局安装：每个 `pnpm add -g` 使用独立目录和虚拟存储，避免全局包之间的冲突，二进制文件移至 `PNPM_HOME/bin` 子目录。
- ⚡ 性能优化：使用 `undici` 替代 `node-fetch`，预分配内存下载，NDJSON 元数据缓存，直接写入 CAS 文件，减少重命名系统调用。
- 🚀 新增命令：`pnpm ci`、`pnpm clean`、`pnpm sbom`、`pnpm peers check`、`pnpm runtime set`、`pnpm pack-app` 等。
- 🔄 审计修复：`pnpm audit --fix=update` 支持交互式修复，并自动将安全补丁版本添加到 `minimumReleaseAgeExclude`。
- 📦 ESM 支持：pnpmfiles 支持 `.mjs` 扩展名，优先于 `.cjs`；pnpm 本身现在为纯 ESM。
- 🛠️ 配置变更：`.npmrc` 仅用于认证和注册表设置，pnpm 特定设置移至 `pnpm-workspace.yaml` 或 `config.yaml`，环境变量使用 `pnpm_config_*` 前缀。
- 🔄 兼容性：放弃 Node.js 18-21 支持，要求 glibc 2.27+，提供从 v10 迁移的指南和 codemod 工具。

---

### [pnpm pack-app | pnpm](https://pnpm.io/11.x/cli/pack-app)

**原文标题**: [pnpm pack-app | pnpm](https://pnpm.io/11.x/cli/pack-app)

以下是 pnpm `pack-app` 命令的概述摘要：

该命令用于将 CommonJS 入口文件打包成独立的可执行文件，支持多平台构建，基于 Node.js 单可执行应用 API。

- 📦 **功能概述**：将 CJS 入口文件打包为独立可执行文件，支持多平台（如 linux-x64、darwin-arm64、win32-x64 等）。
- ⚠️ **实验性状态**：该功能在 v11.0.0 中引入，仍处于实验阶段，其标志、配置模式和输出布局可能在未来版本中更改。
- 🖥️ **系统要求**：主机需运行 Node.js v25.5+ 以执行 SEA 注入；跨平台编译 macOS 目标需 `ldid` 工具。
- 🐞 **已知限制**：`darwin-x64` 目标在 Intel Mac 上因上游 Node.js 错误而崩溃，建议使用非 SEA 工具（如 `@yao-pkg/pkg`）替代。
- ⚙️ **配置选项**：可通过 `--entry`、`--target`、`--runtime`、`--output-dir` 和 `--output-name` 等标志自定义构建，或在 `package.json` 的 `pnpm.app` 字段中设置默认值。
- 📝 **示例**：`pnpm pack-app --entry dist/index.cjs --target linux-x64 --target win32-x64` 可同时为 Linux 和 Windows 构建。

---

### [错误](https://nodeweekly.com/link/184540/web)

**原文标题**: [Error](https://nodeweekly.com/link/184540/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184540/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184541/web)

**原文标题**: [Error](https://nodeweekly.com/link/184541/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184541/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184542/web)

**原文标题**: [Error](https://nodeweekly.com/link/184542/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184542/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184543/web)

**原文标题**: [Error](https://nodeweekly.com/link/184543/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184543/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184544/web)

**原文标题**: [Error](https://nodeweekly.com/link/184544/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184544/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184545/web)

**原文标题**: [Error](https://nodeweekly.com/link/184545/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184545/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184546/web)

**原文标题**: [Error](https://nodeweekly.com/link/184546/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184546/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184547/web)

**原文标题**: [Error](https://nodeweekly.com/link/184547/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184547/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184548/web)

**原文标题**: [Error](https://nodeweekly.com/link/184548/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184548/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184549/web)

**原文标题**: [Error](https://nodeweekly.com/link/184549/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184549/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184550/web)

**原文标题**: [Error](https://nodeweekly.com/link/184550/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184550/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184551/web)

**原文标题**: [Error](https://nodeweekly.com/link/184551/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184551/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184552/web)

**原文标题**: [Error](https://nodeweekly.com/link/184552/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184552/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184553/web)

**原文标题**: [Error](https://nodeweekly.com/link/184553/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184553/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184554/web)

**原文标题**: [Error](https://nodeweekly.com/link/184554/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184554/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184555/web)

**原文标题**: [Error](https://nodeweekly.com/link/184555/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184555/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184556/web)

**原文标题**: [Error](https://nodeweekly.com/link/184556/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184556/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184557/web)

**原文标题**: [Error](https://nodeweekly.com/link/184557/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184557/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184558/web)

**原文标题**: [Error](https://nodeweekly.com/link/184558/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184558/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184559/web)

**原文标题**: [Error](https://nodeweekly.com/link/184559/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184559/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184560/web)

**原文标题**: [Error](https://nodeweekly.com/link/184560/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184560/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184561/web)

**原文标题**: [Error](https://nodeweekly.com/link/184561/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184561/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184562/web)

**原文标题**: [Error](https://nodeweekly.com/link/184562/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184562/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184563/web)

**原文标题**: [Error](https://nodeweekly.com/link/184563/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184563/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184564/web)

**原文标题**: [Error](https://nodeweekly.com/link/184564/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184564/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184565/web)

**原文标题**: [Error](https://nodeweekly.com/link/184565/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184565/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184566/web)

**原文标题**: [Error](https://nodeweekly.com/link/184566/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184566/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184567/web)

**原文标题**: [Error](https://nodeweekly.com/link/184567/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184567/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184568/web)

**原文标题**: [Error](https://nodeweekly.com/link/184568/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184568/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184569/web)

**原文标题**: [Error](https://nodeweekly.com/link/184569/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184569/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184570/web)

**原文标题**: [Error](https://nodeweekly.com/link/184570/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184570/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://nodeweekly.com/link/184571/web)

**原文标题**: [Error](https://nodeweekly.com/link/184571/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/184571/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

