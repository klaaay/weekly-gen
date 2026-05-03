### [Node Weekly 第 622 期：2026 年 4 月 30 日](https://nodeweekly.com/issues/622)

**原文标题**: [Node Weekly Issue 622: April 30, 2026](https://nodeweekly.com/issues/622)

Node Weekly 第 622 期主要涵盖了 Node.js 生态的最新动态，包括新特性、工具更新和社区新闻。

- 📰 **Node 26.0 延期至 5 月 5 日**：因 Rosetta 2 兼容问题导致 macOS 构建失败，但 Temporal API 默认启用，RC 2 版本已可用。
- 🆕 **JavaScript 新特性总结**：Promise.try、Set 集合操作、Array.fromAsync 和 using 已支持，Math.sumPrecise 和 Map.getOrInsert 将在 Node 26 中实现。
- 🛠 **pnpm 11.0 发布**：新增 SQLite 包索引、原生发布工具、全局安装隔离及供应链保护功能。
- 🍋 **Fresh 2.3 框架更新**：Deno 全栈框架支持 WebSocket、零 JS 页面加载，并简化 View Transitions API 使用。
- 📊 **TimescaleDB 赞助内容**：通过 Hypertables 和连续聚合，在 Postgres 上实现快速分析，避免额外数据库延迟。
- 🖥 **portless 工具**：用稳定命名 URL（如 myapp.localhost）替代端口号，新增 Tailscale 支持。
- 🔧 **AVA 8.0 测试框架**：完全支持 ESM，新增 test.skipIf() 和 test.runIf() 修饰符。
- 🎨 **其他工具更新**：Hono 适配器 2.0、BWIP-JS 4.10、basic-ftp 6.0、Ora 9.4、Mongoose 9.6 等。
- 📢 **社区动态**：GitHub 可靠性争议持续，Ghostty 项目退出 GitHub；Ubuntu 26.04 LTS 发布；Datatype 字体支持纯文本图表渲染。

---

### [JavaScript 中真正的新特性（以及接下来会有什么）—— Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

以下是根据您提供的内容生成的摘要：

ES2025 已正式发布，ES2026 即将到来。本文详细介绍了 JavaScript 的新特性、未来趋势，以及如何让 AI 助手使用这些新功能。

- 🚀 **Iterator helpers**：ES2025 新增，支持对迭代器进行 `.map()`、`.filter()`、`.take()` 等惰性操作，无需先转为数组，适合处理无限或大型数据流。
- 🔗 **Set methods**：ES2025 新增，提供 `.union()`、`.intersection()`、`.difference()` 等非变异集合操作，返回新 Set，参数支持类 Set 对象。
- 📦 **JSON modules**：ES2025 新增，原生支持通过 `import config from './config.json' with { type: 'json' }` 导入 JSON，需指定导入属性确保安全。
- 🛡️ **Promise.try**：ES2025 新增，统一处理同步/异步函数和异常，避免双重错误处理，且不会引入额外微任务延迟。
- 🔒 **RegExp.escape**：ES2025 新增，安全转义用户输入中的正则特殊字符，防止注入攻击，自动处理边界情况。
- 📐 **Float16Array**：ES2025 新增，16 位浮点类型数组，内存减半，适用于 WebGPU、TensorFlow.js 等场景。
- 🌐 **Intl.DurationFormat 和 Locale info**：ES2025 新增，实现语言感知的时长格式化和本地化元数据获取，如周起始日。
- ➕ **Math.sumPrecise**：ES2026 即将推出，使用 Shewchuk 算法高精度求和，避免浮点误差累积。
- 🔢 **Uint8Array base64 和 hex**：ES2026 即将推出，原生支持字节数组与 base64/hex 字符串互转，替代手动实现。
- ❌ **Error.isError**：ES2026 即将推出，跨 realm 可靠检测 Error 对象，解决 `instanceof` 在不同执行环境中的失效问题。
- 🔗 **Iterator.concat**：ES2026 即将推出，将多个迭代器串联为一个，无需手动编写生成器包装。
- 📝 **Map.getOrInsert (Upsert)**：ES2026 即将推出，提供 `getOrInsert` 和 `getOrInsertComputed` 方法，简化 Map 的“获取或插入”模式。
- 📚 **Array.fromAsync**：ES2026 即将推出，异步版本的 `Array.from`，将异步可迭代对象收集为数组。
- 📖 **JSON.parse with source text**：ES2026 即将推出，reviver 函数可访问原始 JSON 文本，用于精确处理大数字等场景。
- ⏳ **Temporal**：已到 Stage 4，预计 ES2027 发布。全面替代 Date，提供 `PlainDate`、`ZonedDateTime` 等类型，支持时区、日期计算，已有成熟 polyfill。
- 🔑 **The using keyword**：仍为 Stage 3，实现资源自动清理（如文件句柄、数据库连接），支持同步和异步，已在 Chrome 和 Node 中可用。
- ⏸️ **Import defer**：仍为 Stage 3，延迟模块执行直到首次访问，优化启动性能，仅支持命名空间导入。
- ⏳ **未进入 ES2026 的特性**：Decorators（Stage 3）、Records and Tuples（已撤回，由 Composites 替代）、Pipeline operator（接近 Stage 2）、Pattern matching（Stage 1）、Async iterator helpers（Stage 2）、Iterator.range（Stage 2）、AsyncContext（Stage 2）。
- 🤖 **AI 助手使用建议**：AI 模型训练数据可能过时，建议使用包含现代 API 查找表的技能或提示文件，引导 AI 优先使用 ES2025/ES2026 新特性。

---

### [JavaScript 中真正的新特性（以及即将到来的更新）— Neciu Dan](https://neciudan.dev/whats-new-in-javascript#mathsumprecise)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript#mathsumprecise)

以下是您提供的文章内容的摘要：

JavaScript 在 ES2025 和 ES2026 中引入了多项实用新特性，包括迭代器辅助方法、Set 新方法、更精确的数学计算和日期处理等，同时指出了 AI 编码助手可能因训练数据过时而无法使用这些新特性的问题，并提供了应对方案。

- 📜 **ES2025 新特性概览**：包括迭代器辅助方法（如 `.map()`, `.filter()`, `.take()`）、Set 方法（如 `.intersection()`, `.union()`）、JSON 模块导入、`Promise.try()`、`RegExp.escape()` 和 `Float16Array` 等，均已可在现代浏览器和 Node.js 中使用。
- 🚀 **ES2026 即将推出的特性**：包括 `Math.sumPrecise()`（精确浮点数求和）、`Uint8Array` 的 base64 和十六进制方法、`Error.isError()`（跨 realm 错误检测）、`Iterator.concat()`、`Map.getOrInsert()`、`Array.fromAsync()` 和 `JSON.parse` 的源文本上下文支持。
- ⏳ **尚未进入 ES2026 但值得关注的新功能**：`Temporal`（日期时间处理）、`using` 关键字（资源自动清理）和 `import defer`（延迟模块执行）虽未包含在 ES2026 中，但已在浏览器和 Node.js 中实现或可通过 polyfill 使用。
- 🤖 **AI 编码助手需更新**：由于 AI 模型训练数据过时，常会推荐旧版 JavaScript 写法。文章提供了针对 Claude Code 的插件和通用提示词模板，帮助 AI 优先使用 ES2025/ES2026 的新 API。
- 🛠️ **实用开发者提示**：文章详细列出了新旧 API 的对比和替换建议，涵盖迭代器、集合、日期、Promise、资源清理、错误处理、数字计算、正则表达式和模块导入等方面，帮助开发者编写更现代、高效的代码。

---

### [JavaScript 中真正的新特性（以及即将到来的更新）—— Neciu Dan](https://neciudan.dev/whats-new-in-javascript#mapgetorinsert-upsert)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript#mapgetorinsert-upsert)

以下是您提供的文章摘要，包含概述和要点列表：

ES2025 已正式发布，ES2026 也即将到来。本文详细介绍了 JavaScript 中已可用和即将推出的新特性，包括迭代器辅助方法、Set 方法、JSON 模块、Promise.try、RegExp.escape、Float16Array 等。文章还涵盖了 ES2026 中即将推出的功能，如 Math.sumPrecise、Uint8Array 的 base64 和 hex 方法、Error.isError、Iterator.concat、Map.getOrInsert、Array.fromAsync 和 JSON.parse with source text。此外，文章还讨论了 Temporal、using 关键字和 import defer 等尚未进入 ES2026 但已可用的特性，并提供了如何让 AI 编码助手使用这些新特性的建议。

- 📅 **ES2025 已正式发布**：ECMAScript 2025（第 16 版）于 2025 年 6 月 25 日获批，包含多项实用新特性。
- 🔄 **迭代器辅助方法**：为迭代器添加了`.map()`、`.filter()`、`.take()`、`.toArray()`等方法，支持惰性求值，避免中间数组分配。
- 🧩 **Set 方法**：新增`union`、`intersection`、`difference`、`symmetricDifference`、`isSubsetOf`、`isSupersetOf`、`isDisjointFrom`等非变异方法。
- 📦 **JSON 模块**：原生支持通过`import config from './config.json' with { type: 'json' }`导入 JSON 文件。
- ⚡ **Promise.try**：统一处理同步/异步函数及其异常，避免双重错误处理。
- 🔒 **RegExp.escape**：安全转义用户输入中的正则特殊字符，防止注入。
- 🔢 **Float16Array**：新增 16 位浮点数类型数组，节省内存，适用于 WebGPU 和机器学习场景。
- 🌍 **Intl 增强**：`Intl.DurationFormat`和`Intl.Locale`信息访问器，提升国际化能力。
- 🚀 **ES2026 即将推出**：包括`Math.sumPrecise`（高精度浮点求和）、`Uint8Array`的 base64/hex 方法、`Error.isError`（跨 realm 错误检测）、`Iterator.concat`、`Map.getOrInsert`、`Array.fromAsync`和`JSON.parse with source text`。
- ⏳ **未进入 ES2026 但已可用的特性**：`Temporal`（日期时间库）、`using`关键字（资源自动清理）、`import defer`（延迟模块执行），浏览器和 Node 实现已成熟。
- 🤖 **AI 编码助手建议**：提供了一份“现代 JavaScript 偏好”指令，可引导 AI 使用 ES2025/ES2026 新特性，避免生成过时代码。

---

### [TimescaleDB — 排名第一的时间序列数据库 | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是一个基于 PostgreSQL 构建的顶级时序数据库，提供高性能、实时分析和开源解决方案，适用于传感器、链上和客户数据场景。

- 🐯 **核心产品**：Tiger Cloud 提供弹性云平台，TimescaleDB Enterprise 支持本地/边缘/私有云部署，开源版兼容 PostgreSQL 100%
- ⏱️ **自动分区**：Hypertables 按时间或 ID 自动分区，实现快速数据摄取和可预测查询，支持分区跳过和高效索引扫描
- 💾 **混合存储**：行存储用于写入，列存储用于查询，自动转换并支持 SIMD 向量化操作，压缩率高达 95%
- 📊 **增量物化视图**：Continuous Aggregates 实现增量刷新，支持实时仪表盘和并行批量更新
- ⚙️ **自动化管理**：内置作业调度器，可配置保留策略和列存储/聚合刷新，完全可审计
- 🔧 **时序函数**：约 200 个原生 SQL 函数（如时间加权平均、插值），简化高级时序分析
- 🌟 **客户成果**：Cloudflare、Replicated 和 orca.so 等企业验证其平衡简单性与高性能，支持 Postgres 原生体验
- 🤝 **开源社区**：22K+ GitHub Stars、12K+ Slack 成员，支持 Helm 部署，鼓励贡献和协作
- 🚀 **快速上手**：提供免费试用和开源下载，可毫秒级查询数十亿行数据

---

### [RafaelGSS 提交的 2026-04-28，版本 26.0.0（当前版本）· 拉取请求 #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526)

**原文标题**: [2026-04-28, Version 26.0.0 (Current) by RafaelGSS · Pull Request #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526)

Node.js 26.0.0 版本发布，带来多项重大更新，包括默认启用 Temporal API、V8 引擎升级至 14.6、Undici 升级至 8.0，以及多项弃用和移除。该版本将于 2026 年 10 月进入长期支持 (LTS) 阶段。

- 🚀 **默认启用 Temporal API**：提供更现代、功能更丰富的日期/时间 API，作为传统 `Date` 对象的替代方案。
- ⚙️ **V8 引擎升级至 14.6**：带来 `[Weak]Map.prototype.getOrInsert()`、`[Weak]Map.prototype.getOrInsertComputed()` 和 `Iterator.concat()` 等新功能。
- 🌐 **Undici 升级至 8.0.2**：改进了 Node.js 的 HTTP 客户端实现。
- 🗑️ **多项弃用和移除**：包括移除 `http.Server.prototype.writeHeader()`、`_stream_*` 模块，以及运行时弃用 `module.register()` 和移除 `--experimental-transform-types` 标志。
- 🔧 **构建系统变更**：GCC 要求提升至 13.2，放弃对 Python 3.9 和 Power 8/z13 架构的支持。
- 🛡️ **安全修复**：修复了数组索引哈希碰撞漏洞 (CVE-2026-21717)。
- 🐧 **平台支持更新**：将 AIX/IBM i 的目标架构提升至 Power 9，并更新了 Windows SDK 版本要求。
- 🗓️ **发布推迟**：由于 macOS 构建问题，原定于 4 月 28 日的发布被推迟至 5 月 5 日。

---

### [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

**原文标题**: [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

以下是您提供的关于 JavaScript `Temporal` API 内容的摘要：

Temporal 是一个全新的日期和时间管理 API，旨在全面替代存在设计缺陷的 `Date` 对象，提供更强大、更清晰且不易误用的时间处理能力。

- 🆕 **设计初衷**：`Temporal` 旨在解决 `Date` 对象的根本问题，如时间处理复杂、易混淆、缺乏时区和日历支持等，提供更安全、更明确的 API。
- 🧩 **非构造函数**：`Temporal` 是一个命名空间（类似 `Math`），所有属性和方法都是静态的，不能使用 `new` 或直接调用。
- 📦 **核心类与分组**：API 包含多个类，按功能分为：时间点（`Instant`、`ZonedDateTime`）、无时区日期时间（`PlainDate`、`PlainTime`、`PlainDateTime` 等）、时长（`Duration`）以及实用工具（`Temporal.Now`）。
- ⏰ **时区与日历**：`Temporal` 原生支持任意时区和多种日历系统（如农历、希伯来历），解决了 `Date` 仅支持 UTC 和本地时区、仅支持公历的局限。
- 🔄 **丰富的类接口**：每个类共享相似的方法，如构造（`from()`）、更新（`with()`）、算术（`add()`、`subtract()`）、比较（`equals()`、`compare()`）、舍入（`round()`）和序列化（`toString()`、`toJSON()` 等）。
- 🔗 **类间转换**：提供了清晰的转换方法表，例如 `Instant` 可转换为 `ZonedDateTime`，`PlainDate` 可结合时间转换为 `PlainDateTime`，确保不同类之间数据互操作。
- 📅 **日历系统详解**：详细解释了太阳历、太阴历、阴阳历的区别，以及 `year`、`month`、`day`、`era`、`monthCode` 等属性的使用注意事项，避免常见误解。
- 🗓️ **日期范围限制**：所有表示具体日期的对象有统一的有效范围（约 ±10⁸ 天），从 -271821 年到 +275760 年，超出此范围会拒绝构造。
- 📝 **序列化格式**：所有类支持 RFC 9557 格式（基于 ISO 8601），可指定微秒、纳秒、时区和日历系统，比 `Date` 的格式更强大。
- 🌐 **浏览器兼容性**：该功能目前不是基线标准，因为部分主流浏览器不支持，但已有 polyfill 可供使用。

---

### [为 Temporal 启用 Rust 支持 · 问题 #58730 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/58730#issuecomment-4336293111)

**原文标题**: [Enabling Rust support for Temporal · Issue #58730 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/58730#issuecomment-4336293111)

概述摘要
Node.js 仓库中提出了一项新议题，讨论如何为 V8 引擎中的 Temporal 功能启用 Rust 支持，以便未来 Node.js 能够集成该功能。

- 🚀 议题提出者为 Manishearth，正在 V8 中实现 ECMAScript Temporal，基于 Rust 库 temporal_rs 和 icu4x
- 🔧 V8 已添加 v8_enable_temporal_support 构建标志，默认启用，但在 Node.js 构建中禁用
- ⏳ 尽管 Temporal 尚未准备就绪，但需提前规划 Node.js 的集成方案
- 📦 Node.js 需处理 V8 的 Rust 依赖（third_party/rust），可能需避免引入 Chrome 的全部 Rust 依赖
- 🛠️ 建议通过构建系统下载依赖但不检入仓库，以保持代码树简洁

---

### [为 Temporal 启用 Rust 支持 · Issue #58730 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/58730#issuecomment-4351809373)

**原文标题**: [Enabling Rust support for Temporal · Issue #58730 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/58730#issuecomment-4351809373)

概述摘要
Node.js 正在考虑为 Temporal（ECMAScript 时间处理库）添加 Rust 支持，这需要解决 V8 引擎中 Rust 依赖的集成问题。

- 🕐 开发者 Manishearth 正在为 V8 实现 ECMAScript Temporal 功能，基于 Rust 库 temporal_rs 和 icu4x
- 🔧 Temporal 支持需要 Rust 依赖，V8 已添加 v8_enable_temporal_support 选项（默认启用，但 Node 构建中禁用）
- 🚧 Node.js 最终可能需要支持 Temporal，但仍有充足时间准备正式发布
- 📦 挑战在于 Node.js 需要处理 V8 的 Rust 第三方依赖（third_party/rust），包括工具链和大量额外依赖
- 🧩 如果 Node 不想引入所有 Chrome 的 Rust 依赖，可能需要构建系统层面的解决方案（下载但不检入仓库）
- ⏸️ Temporal 在运行时默认仍处于禁用状态，因为实现尚未完成

---

### [/download/rc/v26.0.0-rc.2/ 的索引](https://nodejs.org/download/rc/v26.0.0-rc.2/)

**原文标题**: [Index of /download/rc/v26.0.0-rc.2/](https://nodejs.org/download/rc/v26.0.0-rc.2/)

Node.js v26.0.0 候选版本 2 的下载目录，包含适用于多平台和架构的安装包及校验文件。

- 📂 包含 `docs/`、`win-arm64/`、`win-x64/` 等子目录
- 🔐 提供 `SHASUMS256.txt` 校验文件（3.0 KB，2026-04-28）
- 🐧 Linux 版本：支持 x64、arm64、ppc64le、s390x 架构，提供 `.tar.gz`（约 60-67 MB）和 `.tar.xz`（约 32-35 MB）格式
- 🍎 macOS 版本：支持 arm64 和 x64，提供 `.tar.gz`（约 56-57 MB）和 `.tar.xz`（约 29-31 MB）
- 🪟 Windows 版本：支持 arm64 和 x64，提供 `.7z`（约 22-24 MB）、`.zip`（约 34-38 MB）及 `.msi` 安装包（约 30-34 MB）
- 📦 通用源码包：`node-v26.0.0-rc.2.tar.gz`（118 MB）和 `.tar.xz`（57 MB）
- 🧩 头文件包：`node-v26.0.0-rc.2-headers.tar.gz`（10 MB）和 `.tar.xz`（579 KB）
- 🕒 所有文件更新日期为 2026-04-28，时间从 21:30 到 23:30

---

### [pnpm 11.0 | pnpm](https://pnpm.io/blog/releases/11.0)

**原文标题**: [pnpm 11.0 | pnpm](https://pnpm.io/blog/releases/11.0)

pnpm 11.0 版本发布，带来了多项重大更新和性能改进，包括更严格的安全默认设置、原生发布流程、SQLite 存储索引以及隔离的全局安装。

- 🔒 **安全默认设置加强**：`minimumReleaseAge` 默认设为 1440 分钟（1 天），`blockExoticSubdeps` 默认启用，新增 `allowBuilds` 取代旧的构建依赖设置。
- 🚀 **原生发布流程**：`pnpm publish`、`login`、`logout` 等命令不再依赖 npm CLI，改用原生实现，支持二维码认证和交互式 OTP 提示。
- 🗄️ **SQLite 存储索引**：存储索引从 JSON 文件改为 SQLite 数据库，减少系统调用，提升安装速度，支持十六进制摘要和捆绑清单。
- 🌍 **隔离的全局安装**：每个 `pnpm add -g` 创建独立目录，拥有自己的 `package.json`、`node_modules` 和锁文件，避免全局包相互干扰。
- 🛠️ **配置重构**：`.npmrc` 仅用于认证和注册表设置，其他配置移至 `pnpm-workspace.yaml` 或新的全局 `config.yaml`，环境变量改用 `pnpm_config_*` 前缀。
- 📦 **Node.js 22+ 要求**：放弃对 Node.js 18-21 的支持，pnpm 本身改为纯 ESM 分发，独立可执行文件需要 glibc 2.27+。
- ⚡ **性能优化**：使用 `undici` 替代 `node-fetch`，支持 Happy Eyeballs 和预分配内存下载，CAS 文件直接写入内容寻址路径，减少重命名系统调用。
- 🔍 **审计功能更新**：`pnpm audit` 改用批量建议端点，CVE 过滤替换为 GHSA 过滤，新增 `--fix=update` 和 `--interactive` 标志。
- 🆕 **新命令**：添加 `pnpm ci`、`pnpm clean`、`pnpm sbom`、`pnpm peers check`、`pnpm runtime set`、`pnpm with`、`pnpm pack-app` 等命令。
- 📝 **其他变化**：pnpmfile 支持 ESM 格式，脚本输出更简洁，`pnpm init` 默认 `type` 为 `"module"`，新增 `dedupePeers` 设置等。

---

### [pnpm pack-app | pnpm](https://pnpm.io/11.x/cli/pack-app)

**原文标题**: [pnpm pack-app | pnpm](https://pnpm.io/11.x/cli/pack-app)

以下是 pnpm `pack-app` 命令的摘要：

该命令用于将 CommonJS 入口文件打包成独立可执行文件，基于 Node.js 单可执行应用 API，支持多平台构建。

- 🚀 **功能概述**：将 CJS 入口文件打包为独立可执行文件，支持多目标平台（如 Linux、macOS、Windows），输出到 `dist-app/<target>/` 目录。
- ⚙️ **要求**：主机需运行 Node.js v25.5+ 以执行 SEA 注入；跨平台构建可能需要额外工具（如 Linux 上构建 macOS 目标需 `ldid`）。
- 🎯 **支持的目标**：格式为 `<os>-<arch>[-<libc>]`，包括 `linux-x64`、`darwin-arm64`、`win32-x64` 等，`-musl` 仅适用于 Linux。
- 📝 **配置方式**：可通过 CLI 参数（如 `--entry`、`--target`、`--runtime`）或 `package.json` 中的 `pnpm.app` 字段设置默认值，CLI 参数会覆盖配置。
- 💡 **示例**：`pnpm pack-app --entry dist/index.cjs --target linux-x64 --target win32-x64` 同时构建 Linux 和 Windows 版本；可指定运行时版本如 `--runtime node@25.5.0`。
- 🛠️ **选项**：包括 `--entry`（入口路径）、`--target`（目标平台，可多次指定）、`--runtime`（嵌入的 Node.js 版本）、`--output-dir`（输出目录，默认 `dist-app`）、`--output-name`（输出文件名，默认包名）。
- 📂 **配置示例**：在 `package.json` 中设置 `pnpm.app` 对象（包含 `entry`、`targets`、`runtime` 等），可简化命令调用。

---

### [单文件可执行应用 | Node.js v25.9.0 文档](https://nodejs.org/api/single-executable-applications.html)

**原文标题**: [Single executable applications | Node.js v25.9.0 Documentation](https://nodejs.org/api/single-executable-applications.html)

Node.js 25.9.0 支持创建单可执行应用程序（SEA），允许将 Node.js 应用打包成独立可执行文件，无需系统安装 Node.js。

- 📦 **核心功能**：将应用脚本和资源打包到 `node` 二进制文件中，启动时自动执行注入的脚本。
- ⚙️ **生成方式**：使用 `--build-sea` 标志和 JSON 配置文件，指定主脚本、输出路径、资源等。
- 🗂️ **资源嵌入**：通过 `assets` 字段嵌入文件，运行时使用 `sea.getAsset()` 等 API 访问。
- 🚀 **启动优化**：支持启动快照（`useSnapshot`）和 V8 代码缓存（`useCodeCache`）以加速启动。
- 🧩 **模块支持**：注入脚本支持 CommonJS 和 ES 模块，但模块加载仅限内置模块，需自行打包依赖。
- 🔧 **执行参数**：通过 `execArgv` 预设 Node.js 参数，并通过 `execArgvExtension` 控制扩展方式（无、环境变量或命令行）。
- 🛠️ **API 交互**：提供 `sea.isSea()`、`sea.getAsset()`、`sea.getAssetAsBlob()` 等内置 API 与 SEA 交互。
- 📝 **注入脚本特性**：`__filename` 和 `__dirname` 指向可执行文件路径，`require()` 功能受限。
- 🔗 **原生插件**：可将 `.node` 插件作为资源嵌入，运行时写入临时文件后通过 `process.dlopen()` 加载。
- 🖥️ **平台支持**：主要在 Windows、macOS 和 Linux（除 Alpine 和 s390x）上测试，其他平台需手动注入。

---

### [Perry — TypeScript → 原生](https://www.perryts.com/)

**原文标题**: [Perry â TypeScript â Native](https://www.perryts.com/)

### 概述总结
Perry 是一款将 TypeScript 直接编译为原生可执行文件的工具，无需运行时或 Electron，支持多平台，性能卓越，二进制文件小巧。

- 🚀 **原生性能**：TypeScript 直接编译为原生二进制，无需 Node.js 或 V8，启动时间仅约 1ms，性能比 Node.js 快高达 18 倍。
- 📦 **小巧二进制**：输出文件通常仅 2-5 MB，即使包含 V8 运行时也仅 15-20 MB，部署更轻量。
- 🖥️ **多平台支持**：支持 macOS、iOS、Android、Linux、Windows 等 10+ 平台，使用原生 UI 组件（AppKit、GTK4 等）。
- 🧩 **丰富标准库**：内置 fs、path、crypto 等常见 Node.js API，以及 30+ 原生 npm 包（如 mysql2、bcrypt）。
- ⚙️ **编译时优化**：支持编译时插件系统、真正多线程、国际化（i18n），无运行时开销。
- 🛠️ **完整工作流**：从编译、签名到分发（App Store、Play Store）一站式解决，内置自动化测试工具 Geisterhand。
- 📊 **基准测试**：在 accumulate、object create 等场景中，Perry 比 Node.js 快 1.4x 至 18x，内存开销更低。
- 🔓 **开源免费**：对开源项目免费，团队计划通过 Perry Publish 提供更多功能。

---

### [Eleventy 是一个更简单的静态网站生成器](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

Eleventy 是一个更简单的静态网站生成器，强调性能、稳定性和开发者友好。

- 🚀 极快的构建速度：构建 4000 个 Markdown 文件仅需 1.93 秒，远快于 Astro、Gatsby 和 Next.js
- 🏢 生产就绪且值得信赖：被 NASA、CERN、Google、Microsoft 等大型组织使用，下载量超 1789 万次
- 🎯 零配置启动：只需 Node.js 18+ 和 npx 命令即可运行，支持多种模板语言（Markdown、Liquid、Nunjucks 等）
- 🔒 稳定可靠：自 2017 年以来发布 222 个版本，仅 3 个版本需要开发者更改代码
- 🕵️ 无追踪：不使用或收集遥测数据，无需选择退出数据收集
- 🧩 灵活可扩展：支持增量采用，可与现有项目目录结构配合，允许精确控制文件处理
- 🌐 零客户端 JavaScript：默认不注入客户端 JavaScript，支持渐进增强
- 💬 活跃社区：拥有 882 位作者和 1280 个网站，社区成员（如 Mat Marquis、Lea Verou）高度评价
- 📚 丰富文档：提供完整指南、教程、插件和社区资源

---

### [Eleventy 现已更名为 Build Awesome — Eleventy](https://www.11ty.dev/blog/build-awesome/)

**原文标题**: [Eleventy is now Build Awesome — Eleventy](https://www.11ty.dev/blog/build-awesome/)

### 概述总结
Eleventy 项目更名为 Build Awesome，并计划通过 Kickstarter 众筹支持其持续发展，同时保持与现有社区和插件的完全兼容性。

- 📢 **项目更名**：Eleventy 正式更名为 Build Awesome，纳入 Font Awesome 生态系统，但保持开源项目的延续性。
- 🚀 **众筹支持**：通过 Kickstarter 订阅 Build Awesome Pro，以获取更多功能和服务，同时免费版本仍可正常使用。
- 🔄 **兼容性承诺**：Build Awesome 完全兼容现有 Eleventy 插件和构建命令，确保平滑升级体验。
- 🌟 **开源增长**：类似 Font Awesome Pro 和 Web Awesome Pro 的成功案例，Pro 版本将推动免费版本的功能和稳定性提升。
- 💰 **Open Collective 账户**：仍用于支付项目相关费用（如网站、Meetup、会议等），但未来主要支持方式将转向 Kickstarter。
- 📝 **社区反馈**：项目负责人 Zach 承诺继续维护，并欢迎通过 Mastodon 或 Bluesky 提出疑问。

---

### [返回构建 Awesome Pro，让网页构建更轻松！— Eleventy](https://www.11ty.dev/blog/build-awesome-pro/)

**原文标题**: [Back Build Awesome Pro and make it easier to build for the web! — Eleventy](https://www.11ty.dev/blog/build-awesome-pro/)

### 概述总结
Eleventy 团队推出 Build Awesome Pro 项目，旨在简化网站构建、发布和维护流程，并通过 Kickstarter 众筹获取支持。

- 📢 宣布启动 Build Awesome Pro Kickstarter 众筹，目标是让网站构建更易上手
- 🧀 推荐观看 Kickstarter 宣传视频（搭配奶酪更佳）
- 📝 提供开发者友好型介绍：阅读《协作编辑作为渐进增强》博客
- 🎥 在 Kickstarter 页面可观看更多演示视频
- 🙏 感谢社区支持，并提醒 Open Collective 支持者查看邮件获取专属奖励
- ⏳ 众筹截止日期为 5 月 28 日
- 🔗 视频同步发布至 YouTube 平台

---

### [GitHub - vercel-labs/portless：用稳定、命名的本地URL替代端口号。适用于人类和智能体。](https://github.com/vercel-labs/portless)

**原文标题**: [GitHub - vercel-labs/portless: Replace port numbers with stable, named local URLs. For humans and agents. · GitHub](https://github.com/vercel-labs/portless)

Portless 是一个用稳定、命名的 .localhost URL 替代端口号的本地开发工具，同时适用于人类和 AI 代理。

- 🔗 将 `localhost:3000` 替换为 `https://myapp.localhost` 这样的命名 URL，告别记忆端口号
- 🚀 自动生成并信任本地 CA，默认启用 HTTPS 和 HTTP/2，提升开发体验
- 🧩 自动检测框架并注入正确的 `--port` 和 `--host` 参数，支持 Next.js、Vite、Expo 等
- 📦 支持单仓库（monorepo），通过 `portless.json` 或 `package.json` 配置，自动发现工作区包
- 🌐 支持子域名、自定义 TLD（如 `.test`）、Git 工作树（worktree）自动生成唯一 URL
- 🖥️ 提供 LAN 模式（mDNS），让局域网设备通过 `.local` 域名访问
- 🔄 与 TurboRepo 无缝集成，无需修改 `turbo.json`
- 🛡️ 支持 Tailscale 分享（`--tailscale`）和公网 Funnel 暴露（`--funnel`）
- 🧹 提供丰富的命令：`portless list`、`portless clean`、`portless trust`、`portless proxy` 等
- ⚙️ 环境变量和 CLI 选项灵活配置，支持 `PORTLESS_PORT`、`PORTLESS_LAN` 等

---

### [发布 v0.12.0 · vercel-labs/portless · GitHub](https://github.com/vercel-labs/portless/releases/tag/v0.12.0)

**原文标题**: [Release v0.12.0 · vercel-labs/portless · GitHub](https://github.com/vercel-labs/portless/releases/tag/v0.12.0)

概述摘要
- 🚀 **Tailscale 共享**：新增 `--tailscale` 标志，可通过 Tailscale 网络共享任意无端口应用，每个应用自动挂载到独立 HTTPS 端口，无需 `basePath` 配置。
- 🌐 **Tailscale Funnel**：新增 `--funnel` 标志，通过 Tailscale Funnel 将应用公开到互联网，隐含 `--tailscale` 功能。
- 🔗 **环境变量支持**：子进程可通过 `PORTLESS_TAILSCALE_URL` 环境变量获取 Tailscale HTTPS 地址。
- 📋 **列表命令增强**：`portless list` 命令在 Tailscale 共享激活时，同时显示本地和 Tailnet 网络 URL。
- 🧹 **清理功能优化**：`portless prune` 可清除失效的 Tailscale 注册记录；`portless clean` 可移除 Tailscale serve/funnel 相关状态。

---

### [调试 Next.JS 最佳实践：日志与追踪 | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-nextjsworkshop&utm_content=newsletter-sponsored-link-register)

**原文标题**: [Debugging Next.JS Best Practices: Logs and Tracing | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-nextjsworkshop&utm_content=newsletter-sponsored-link-register)

概述摘要
- 🔧 工作坊聚焦于调试 Next.js 应用的最佳实践，涵盖日志与追踪技术
- 📝 强调编写高上下文日志，记录失败原因、用户影响及具体细节（谁、什么、为什么）
- 🚨 学习如何查询和设置日志告警，捕获认证、支付、Webhook 及第三方 API 调用中的静默故障
- 🔍 深入讲解跨客户端和 Node 运行时的分布式追踪技术
- 🔗 将日志与追踪关联，无需切换工具即可获得完整上下文
- 📖 提供额外资源：Sentry 调试 Next.js 应用、AI 代理与 MCP 服务器构建、Next.js 日志简化指南

---

### [调试 Next.JS 最佳实践：日志与追踪 | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-nextjsworkshop&utm_content=newsletter-sponsored-link-register%20)

**原文标题**: [Debugging Next.JS Best Practices: Logs and Tracing | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-nextjsworkshop&utm_content=newsletter-sponsored-link-register%20)

### 概述摘要
本资源介绍了关于调试 Next.js 应用的最佳实践，重点涵盖日志记录、追踪和性能问题排查，并提供相关研讨会和文章链接。

- 🔧 研讨会涵盖：编写高上下文日志，记录失败原因、用户影响及上下文信息
- 📊 查询和告警日志，用于捕获身份验证、支付、Webhook 和第三方 API 调用中的静默故障
- 🔍 深入探讨跨客户端和 Node 运行时的分布式追踪
- 🔗 将日志与追踪连接，无需切换工具即可获取完整上下文
- 📚 提供额外资源：使用 Sentry 观察和调试 Next.js 应用、构建 AI 代理和 MCP 服务器、以及 Next.js 日志记录技巧

---

### [Fresh 2.3：默认零 JS、视图过渡与 Temporal 支持 | Deno](https://deno.com/blog/fresh-2.3)

**原文标题**: [Fresh 2.3: Zero JS by default, View Transitions, and Temporal support | Deno](https://deno.com/blog/fresh-2.3)

Fresh 2.3 版本发布，带来零 JavaScript 默认支持、视图过渡动画、WebSocket 原生支持等多项重大更新。

- 🚀 **零 JavaScript 默认**：页面不再自动注入 JavaScript，仅当使用岛屿或局部更新时才加载脚本，静态页面实现零 JS 加载
- ✨ **视图过渡动画**：通过 `f-view-transition` 属性集成 View Transitions API，支持自定义 CSS 动画和元素级过渡效果
- 🔗 **WebSocket 原生支持**：新增 `app.ws()` 方法和 `ctx.upgrade()` 接口，支持托管模式和裸模式，自动处理非 WebSocket 请求返回 400
- ⚡ **Vite 集成优化**：移除 Babel 转换，由 Vite 直接处理 CJS 转 ESM 和 `process.env` 替换，提升 Radix UI 等包兼容性
- 🔒 **安全增强**：新增 CSP nonce 注入中间件和 IP 过滤中间件，支持 CIDR 白名单/黑名单
- 📊 **OpenTelemetry 追踪**：自动注入 W3C traceparent 元标签，实现浏览器端到服务端的追踪连接
- 📅 **Temporal API 支持**：支持所有八种 Temporal 类型作为岛屿属性传递，包括日期、时间、持续时间等
- 📁 **多静态目录**：`staticDir` 选项支持数组，同名文件按优先级顺序加载
- 🔄 **表单加载指示器**：加载指示器现在支持表单提交，可针对不同提交按钮设置独立指示器
- 🌐 **反向代理支持**：新增 `trustProxy` 选项，自动读取 `X-Forwarded-Proto` 和 `X-Forwarded-Host` 头
- 🛠️ **预编译中间件**：中间件链在启动时一次性编译，减少每次请求的组装开销
- 🐛 **多项 Bug 修复**：包括路由参数、部分更新、活动链接、Windows 路径等问题的修复

---

### [Fresh - 简洁、易用、高效的 Web 框架。](https://fresh.deno.dev/)

**原文标题**: [Fresh - The simple, approachable, productive web framework.](https://fresh.deno.dev/)

概述摘要
- 🍳 点击食谱即可将 HTML 内容流式加载到此处。

---

### [GitHub - russellromney/honker：支持持久队列、流、发布/订阅和调度器的Postgres NOTIFY/LISTEN语义的SQLite扩展及绑定](https://github.com/russellromney/honker)

**原文标题**: [GitHub - russellromney/honker: SQLite extension + bindings for Postgres NOTIFY/LISTEN semantics with durable queues, streams, pub/sub, and scheduler · GitHub](https://github.com/russellromney/honker)

honker 是一个 SQLite 扩展，为 SQLite 添加了类似 Postgres NOTIFY/LISTEN 的语义，支持持久化发布/订阅、任务队列和事件流，无需客户端轮询或独立代理，所有功能都内置于单个 .db 文件中。

- 📦 **一体化解决方案**：将任务队列、发布/订阅和事件流直接嵌入 SQLite，避免引入 Redis 等第二数据存储，减少运维复杂度和双写问题。
- ⚡ **毫秒级跨进程通知**：通过每 1 毫秒轮询 `PRAGMA data_version` 实现推送式语义，跨进程反应时间仅 1-2 毫秒，无需应用层轮询。
- 🔒 **事务性原子操作**：业务写入和队列/通知操作可在同一事务中提交或回滚，确保数据一致性，支持“事务性发件箱”模式。
- 🛠️ **丰富功能集**：支持工作队列（重试、优先级、延迟任务、死信表）、持久化流（每个消费者独立偏移）、临时发布/订阅、定时任务、速率限制和命名锁。
- 🌐 **多语言绑定**：提供 Python、Node.js、Rust、Go、Ruby、Bun、Elixir 等语言绑定，以及 SQLite 可加载扩展，任何 SQLite 3.9+ 客户端均可使用。
- 🧩 **框架集成**：可轻松与 SQLAlchemy、Django、FastAPI 等 ORM 和 Web 框架集成，只需在连接上加载扩展并调用 SQL 函数。
- 🚀 **高性能**：在现代笔记本上每秒处理数千条消息，空闲时仅消耗少量 CPU（约 3.5 µs/查询），通过部分索引优化热路径。
- 🛡️ **崩溃恢复**：利用 SQLite 的 ACID 特性，SIGKILL 等崩溃不会留下脏状态，任务超时后自动重新分配。
- 📜 **Apache 2.0 许可**：开源项目，提供完整文档、基准测试和贡献指南。

---

### [获取失败](https://nodeweekly.com/link/184552/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/184552/web)

无法总结：获取内容失败，状态码 403。

---

### [GitHub - russellromney/honker：支持持久队列、流、发布/订阅和调度器的Postgres NOTIFY/LISTEN语义的SQLite扩展及绑定](https://github.com/russellromney/honker#nodejs)

**原文标题**: [GitHub - russellromney/honker: SQLite extension + bindings for Postgres NOTIFY/LISTEN semantics with durable queues, streams, pub/sub, and scheduler · GitHub](https://github.com/russellromney/honker#nodejs)

honker 是一個 SQLite 擴展，為 SQLite 添加了 Postgres 風格的 NOTIFY/LISTEN 語義，內建持久化發布/訂閱、任務隊列和事件流功能，無需客戶端輪詢或獨立代理程序。

- 📦 **核心功能**：支援跨進程通知/監聽、工作隊列（含重試、優先級、延遲任務、死信表）、持久化流與每消費者偏移量，以及定時任務排程器。
- ⚡ **高效能設計**：透過每 1 毫秒查詢 `PRAGMA data_version` 實現推送式語義，跨進程反應時間僅數毫秒，無需應用層輪詢。
- 🔗 **事務性耦合**：任務/事件/通知可與業務寫入在同一事務中提交或回滾，實現原子性操作，避免雙寫問題。
- 🌐 **多語言支援**：提供 SQLite 可載入擴展及 Python、Node.js、Rust、Go、Ruby、Bun、Elixir 等多種語言綁定，共享同一底層架構。
- 🗃️ **單檔案儲存**：所有資料（隊列、流、通知）儲存在單一 `.db` 檔案中，利用 SQLite 的嵌入式、持久化與快照優勢。
- 🛠️ **易於整合**：可與 SQLAlchemy、Django、Drizzle 等 ORM 配合使用，僅需載入擴展並在 ORM 事務中呼叫 SQL 函數。
- 🧪 **實驗性專案**：API 可能變更，但已提供完善測試與基準測試，支援崩潰恢復與 WAL 模式最佳化。

---

### [发布 v8.0.0 · avajs/ava · GitHub](https://github.com/avajs/ava/releases/tag/v8.0.0)

**原文标题**: [Release v8.0.0 · avajs/ava · GitHub](https://github.com/avajs/ava/releases/tag/v8.0.0)

AVA v8.0.0 版本发布，带来了重大变更和新功能。

- 🚀 **Node.js 版本要求提升**：现在需要 Node.js 22.20、24.12 或更新版本。
- 📦 **内部全面采用 ESM**：AVA 内部已完全转为 ES 模块，支持通过 `require()` 加载 ES 模块。
- 🔄 **CommonJS 项目需更新导入方式**：从 `require('ava')` 改为 `const {default: test} = require('ava')`。
- 📁 **默认文件扩展名变更**：现默认使用 `.js` 和 `.mjs`，如需 `.cjs` 扩展名需手动配置 `extensions: ['cjs', 'js', 'mjs']`。
- 🧪 **测试文件通过 `import()` 加载**：所有测试文件及 `require` 配置加载的文件均通过 `import()` 加载，建议使用自定义钩子进行转译。
- 🆕 **新增测试修饰符**：`test.skipIf()` 和 `test.runIf()` 可根据运行时条件跳过或运行测试，并支持与其他修饰符（如 `.serial`、`.failing`）组合使用。
- 👀 **监视模式改进**：忽略对 `*.tsbuildinfo` 文件的更改。
- 📝 **TAP 报告器优化**：在恢复原始错误名称时更加稳健。
- 🐛 **错误报告增强**：改进了 `throwsAsync`/`notThrowsAsync` 未等待时的错误报告。
- 🤝 **新贡献者**：感谢 @ninper00 的首次贡献。
- 🔗 **完整更新日志**：v7.0.0...v8.0.0

---

### [发布 v2.0.0 · honojs/node-server · GitHub](https://github.com/honojs/node-server/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · honojs/node-server · GitHub](https://github.com/honojs/node-server/releases/tag/v2.0.0)

Hono Node.js 适配器 v2.0.0 发布，性能大幅提升，最高可达 2.3 倍吞吐量，API 保持不变，并移除了对 Node.js v18 和 Vercel 适配器的支持。

- 🎉 **性能飞跃**：v2 版本在 body 解析场景下吞吐量提升 2.3 倍，其他场景也有显著提升，整体性能超越 Koa 和 Fastify。
- ⚡ **核心优化**：通过引入 `LightweightRequest`/`LightweightResponse` 和直接读取 `IncomingMessage` 的 body 解析优化，避免了不必要的对象转换，大幅提升效率。
- 🔧 **关键改进**：包括请求 body 读取优化、URL 构建快速路径、`buildOutgoingHttpHeaders` 优化、方法键缓存、信号快速路径等多项性能改进。
- 🚫 **破坏性变更**：放弃对 Node.js v18 的支持（需 v20+），并移除了 Vercel 适配器（可自行实现替代方案）。
- 🌐 **新功能**：新增对 WebSocket 的一流支持。
- 🛠 **构建与工具**：从 tsup 迁移至 tsdown，测试框架从 Jest 迁移至 Vitest，并添加 `type: module` 到 `package.json`。
- 📈 **基准测试**：在 `bun-http-framework-benchmark` 的 Body 场景中，Hono v2 取得第一名，击败 Koa 和 Fastify。
- ⚠️ **注意**：srvx 的 `FastResponse` 模式在特定基准测试中速度更快，但方法论不同，需注意对比。

---

### [Hono - 基于 Web 标准的 Web 框架](https://hono.dev/)

**原文标题**: [Hono - Web framework built on Web Standards](https://hono.dev/)

概述总结
Hono 框架的 RegExpRouter 路由器速度极快，hono/tiny 预设体积小于 14kB，且仅使用 Web 标准 API。

- 🚀 RegExpRouter 路由器性能超快，处理请求高效
- ⚖️ hono/tiny预设体积轻巧，仅14kB以下
- 🌐 完全基于 Web 标准 API 构建，无额外依赖

---

### [GitHub - metafloor/bwip-js: 纯 JavaScript 条码生成器 · GitHub](https://github.com/metafloor/bwip-js)

**原文标题**: [GitHub - metafloor/bwip-js: Barcode Writer in Pure JavaScript · GitHub](https://github.com/metafloor/bwip-js)

bwip-js 是一个将纯 PostScript 条形码编写器转换为原生 JavaScript 的库，支持在浏览器、Node.js 等多种平台上生成超过 100 种条形码类型，输出格式包括 PNG、Canvas 和 SVG。

- 📦 **多平台支持**：bwip-js 提供浏览器、Node.js、React Native、Electron 和命令行接口，并针对各平台提供独立包（如 `@bwip-js/node`、`@bwip-js/browser`）。
- 🎯 **核心功能**：通过 `toCanvas()`、`toBuffer()`、`toSVG()` 等方法生成条形码，支持自定义缩放、旋转、填充、背景色等选项，并兼容 BWIPP 的扩展参数。
- 📋 **丰富条形码类型**：涵盖 Code128、QR Code、Data Matrix、EAN、UPC、PDF417 等 100 多种标准，包括 GS1、HIBC 等复合类型。
- 🛠️ **灵活集成**：支持 ES6 模块树摇优化，可单独导入编码器（如 `gs1_128`），并提供在线生成器、API 服务和演示应用（`demo.html`）。
- 📄 **输出格式多样**：生成 PNG 图像（Node.js）、Canvas 渲染（浏览器）、SVG 矢量图（所有平台），以及 React Native 的 `toDataURL()` 方法。
- 🔧 **高级配置**：支持自定义字体、缩放因子（`scale`）、旋转方向（`rotate`）、填充区域（`padding`）和颜色（`backgroundcolor`），并处理低分辨率下的模块宽度约束。
- 🌐 **在线服务**：提供在线条形码生成器和 API，可通过 URL 参数直接生成条形码图像，适用于非 JavaScript 服务器。
- 📚 **文档与示例**：包含详细的 API 参考、示例代码（Node.js 服务器、React 组件、Electron 应用）和命令行工具使用说明。

---

### [bwip-js - JavaScript 条形码生成器](https://bwip-js.metafloor.com/demo/demo.html)

**原文标题**: [bwip-js - JavaScript Barcode Generator](https://bwip-js.metafloor.com/demo/demo.html)

这是一个纯 JavaScript 编写的条码生成工具，支持多种条码类型和输出格式，可自定义文本、缩放、旋转和反转等选项。

- 📊 支持多种条码类型（bwip-js）的纯 JavaScript 实现
- 🔤 可自定义条码文本和替代文本（Alt Text）
- ⚙️ 提供丰富的选项设置（Options）
- 💾 支持保存为 PNG 或 JPEG 格式
- 🔗 可生成跳转 URL 功能
- 🎨 支持 Canvas 和 SVG 两种渲染方式
- 📐 支持 X/Y 轴缩放调整（Scale X,Y）
- 🔄 支持图像旋转：正常、右转、左转
- 🔁 提供反转显示功能（Invert）

---

### [GitHub - patrickjuchli/basic-ftp：Node.js的FTP客户端，支持基于TLS的FTPS、IPv6下的被动模式、async/await以及TypeScript。](https://github.com/patrickjuchli/basic-ftp)

**原文标题**: [GitHub - patrickjuchli/basic-ftp: FTP client for Node.js, supports FTPS over TLS, passive mode over IPv6, async/await, and Typescript. · GitHub](https://github.com/patrickjuchli/basic-ftp)

basic-ftp 是一个基于 Node.js 的 FTP 客户端库，支持 FTPS、IPv6 被动模式、Promise 异步操作，并提供目录级操作方法。建议优先使用 HTTPS 或 SFTP，仅在必须使用 FTP 时采用此库，并尽量启用 FTPS 加密。

- 📦 **核心特性**：支持 FTPS over TLS、IPv6 被动模式、Promise 异步 API，以及目录批量操作（如上传/下载整个目录）。
- ⚠️ **安全建议**：FTP 协议存在可靠性问题，建议优先使用 HTTPS 或 SFTP；若必须使用，应启用 FTPS 加密。
- 🔧 **安装与依赖**：仅需 Node.js 10.0 或更高版本，通过 `npm install basic-ftp` 安装。
- 💻 **基础用法**：支持 TLS 连接、文件上传下载、目录创建与清空等操作，示例代码展示了完整流程。
- 🛠️ **客户端 API**：提供 `access()`、`list()`、`uploadFrom()`、`downloadTo()`、`ensureDir()` 等方法，支持超时配置和错误处理。
- 📊 **进度追踪**：通过 `trackProgress()` 可监控上传、下载或列表操作的实时进度，包括文件名、类型和传输字节数。
- 🔒 **错误处理**：FTP 服务器错误会抛出 `FTPError` 并保持连接；超时或连接错误会关闭连接，需重新调用 `access()` 恢复。
- 📝 **日志与扩展**：设置 `client.ftp.verbose = true` 可输出调试信息，支持自定义日志函数；库基于 TypeScript 开发，提供类型声明文件。
- 📂 **目录解析**：支持 MLSD、Unix 和 DOS 格式的目录列表解析，可通过 `client.parseList` 自定义解析函数。
- 🏆 **项目信息**：获得 721 颗星、102 个分支，采用 MIT 许可证，最新版本为 6.0.0（2026 年 4 月发布），主要语言为 TypeScript（62.6%）和 JavaScript（37.4%）。

---

### [GitHub - lovell/icc: 用于解析国际色彩联盟（ICC）配置文件的 JavaScript 模块](https://github.com/lovell/icc)

**原文标题**: [GitHub - lovell/icc: JavaScript module to parse International Color Consortium (ICC) profiles · GitHub](https://github.com/lovell/icc)

概述摘要
- 📦 **icc** 是一个用于解析国际色彩联盟（ICC）配置文件的 JavaScript 模块。
- 🛠️ 通过 `npm install icc` 安装，使用 `parse` 函数从 Buffer 中解析 ICC 配置文件。
- 📋 解析后返回包含版本、意图、设备类别、色彩空间等关键信息的对象。
- 📄 示例输出包括版本 `2.0`、意图 `Perceptual`、设备类别 `Monitor` 等。
- 📚 项目基于 Apache-2.0 许可证，由 Lovell Fuller 等人开发。
- ⭐ 在 GitHub 上获得 59 颗星，6 个复刻，主要使用 JavaScript 和 TypeScript。

---

### [GitHub - sindresorhus/ora: 优雅的终端旋转器 · GitHub](https://github.com/sindresorhus/ora)

**原文标题**: [GitHub - sindresorhus/ora: Elegant terminal spinner · GitHub](https://github.com/sindresorhus/ora)

Ora 是一个优雅的终端旋转加载动画库，支持丰富的自定义选项和多种状态提示。

- 🎯 核心功能：提供美观的终端旋转动画，支持自定义文本、颜色和动画样式
- ⚙️ 配置选项：可设置文本、前缀/后缀内容、旋转样式、颜色、缩进、隐藏光标等
- 🎨 状态方法：支持 start、stop、succeed、fail、warn、info 等状态切换，并自动显示对应符号
- 🔄 实例属性：可动态修改 text、color、spinner 等属性，并实时生效
- 🚀 oraPromise：直接为 Promise 添加旋转动画，自动根据结果显示成功或失败状态
- 📝 日志兼容：支持在旋转动画运行时使用 console.log 输出日志，不会破坏显示
- ⚡ 性能优化：建议使用异步操作避免阻塞动画，支持 Worker 线程通过消息通信控制
- 🖥️ 跨平台：自动适配 Windows 终端，支持 Unicode 和 ASCII 字符集

---

### [发布 9.6.0 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.6.0)

**原文标题**: [Release 9.6.0 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.6.0)

概述摘要
- 📦 升级 MongoDB Node.js 驱动至 7.2 版本
- 🚫 新增 `allowNull` 选项，允许在非必填字段中禁止 null 值
- 🔧 改进 QueryFilter 类型，支持字符串联合类型和枚举
- 📤 导出 Projector 和 ArrayProjectionOperators 类型
- 🐛 修复多项问题（#16245, #16237, #15905, #16242, #16240, #16243, #16235）

---

### [简介（指南）| VineJS 文档](https://vinejs.dev/docs/introduction)

**原文标题**: [Introduction (Guides) | VineJS Documentation](https://vinejs.dev/docs/introduction)

VineJS 是一个专为 Node.js 后端设计的表单数据验证库，提供高性能、类型安全及丰富的验证规则，并原生处理 HTML 表单序列化问题。

- 🚀 性能卓越：VineJS 是 Node.js 生态中最快的验证库之一，基准测试显示其性能比 Zod 快 5-10 倍。
- 🛡️ 类型安全：同时提供运行时验证和静态类型安全，确保代码健壮性。
- 📦 丰富规则：内置超过 50 条验证规则和 12 种 schema 类型，支持自定义扩展。
- 🌐 表单友好：原生处理 HTML 表单序列化 quirks（如数字/布尔值转字符串、空字段等），无需手动规范化。
- 📝 错误处理：支持自定义错误消息和格式化，提供更好的错误处理工作流。
- 🔧 可扩展性：易于添加自定义规则和 schema 类型，并支持测试自定义规则。
- ❓ 适用场景：专为后端 HTTP 请求体验证设计，不适用于浏览器或验证函数/Map/Set 等 JS 类型。
- 👥 社区支持：由 AdonisJS 核心团队维护，通过 GitHub Sponsors 赞助支持。

---

### [Clerk CLI](https://clerk.com/cli?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli&utm_content=04-30-26&dub_id=MVEK0ksA9raZGW5R)

**原文标题**: [Clerk CLI](https://clerk.com/cli?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli&utm_content=04-30-26&dub_id=MVEK0ksA9raZGW5R)

### 概述总结
Clerk CLI 提供了一种从终端直接设置身份验证的便捷方式，支持开发者和 AI 代理快速集成认证功能，无需手动复制 API 密钥。

- 🛠️ **三步完成认证设置**：通过 `clerk init`、`clerk config` 和 `clerk deploy`（即将推出）三个命令，即可在现有项目中添加认证功能。
- 🔗 **自动检测与集成**：`clerk init` 自动识别项目框架，链接应用并添加所需认证文件。
- ⚙️ **代码化管理配置**：`clerk config` 允许从代码中管理设置，提升配置效率。
- 🚀 **代理友好设计**：AI 代理可通过 CLI 自动处理认证设置、租户接入和生产部署，支持从提示到生产的全流程。
- 📦 **多平台安装支持**：提供 npm、bun、pnpm、yarn、Homebrew 和 curl 等多种安装方式，适配不同开发环境。
- 🔄 **生产环境部署**：`clerk deploy`（即将推出）可验证变更、同步实例状态，确保认证变更安全上线。

---

### [GitHub 可用性更新 - GitHub 博客](https://github.blog/news-insights/company-news/an-update-on-github-availability/)

**原文标题**: [An update on GitHub availability - The GitHub Blog](https://github.blog/news-insights/company-news/an-update-on-github-availability/)

GitHub 近期发生两次服务中断事件，团队正全力提升系统可靠性和扩展能力，以应对因 AI 开发工作流激增带来的 30 倍规模增长需求。

- 📉 两次中断事件概述：4 月 23 日合并队列故障导致 658 个仓库受影响，4 月 27 日搜索系统因机器人攻击过载，均未造成数据丢失但影响用户体验
- 🚀 容量扩展计划升级：从 2025 年 10 月启动 10 倍扩容，到 2026 年 2 月调整为 30 倍规模设计，主要驱动因素是 AI 代理开发工作流爆发式增长
- ⚙️ 短期优化措施：解决 Webhooks 迁移、用户会话缓存重设计、认证授权流程重构等瓶颈，利用 Azure 迁移增加计算资源
- 🛡️ 服务隔离与降级：隔离 Git 和 Actions 等关键服务，减少单点故障，将性能敏感代码从 Ruby 迁移至 Go，优化依赖分析与风险排序
- ☁️ 多云架构推进：加速从小型数据中心迁移至公有云，并启动多云战略以提升弹性、低延迟和灵活性
- 📂 大型单体仓库优化：针对仓库数量激增和大型单体仓库趋势，投资 Git 系统和 PR 体验，优化合并队列操作以支持每日数千次 PR
- 🔍 透明度提升：更新状态页面显示可用性数据，承诺报告所有大小事件，改进事件分类和用户报告机制
- 💡 核心承诺：优先保障可用性，其次容量，最后新功能，通过减少不必要工作、改善缓存、隔离服务等方式提升系统优雅降级能力

---

### [Ghostty 将离开 GitHub – Mitchell Hashimoto](https://mitchellh.com/writing/ghostty-leaving-github)

**原文标题**: [Ghostty Is Leaving GitHub – Mitchell Hashimoto](https://mitchellh.com/writing/ghostty-leaving-github)

概述摘要
- 😢 Mitchell Hashimoto 宣布其项目 Ghostty 将离开 GitHub，原因是频繁的故障严重影响工作效率。
- 💔 他从 2008 年起就是 GitHub 重度用户，曾将其视为最快乐的地方，甚至梦想在此工作。
- 😡 近年 GitHub 频繁宕机（几乎每天一次），导致无法进行 PR 审查、代码提交等核心工作。
- 🚀 Ghostty 将逐步迁移至其他平台，但会保留 GitHub 只读镜像。
- 🔍 具体迁移目标仍在与多个商业及开源提供商协商中。
- ⏳ 个人项目和其他工作暂时保留在 GitHub，但未来可能跟进。
- 📅 此决定与 2026 年 4 月 27 日的大规模故障无关，计划已酝酿数月。

---

### [Ubuntu 26.04（"坚毅浣熊"）LTS 发布 - 公告 - Ubuntu 社区中心](https://discourse.ubuntu.com/t/ubuntu-26-04-resolute-raccoon-lts-released/80833)

**原文标题**: [Ubuntu 26.04 ("Resolute Raccoon") LTS released - Announcements - Ubuntu Community Hub](https://discourse.ubuntu.com/t/ubuntu-26-04-resolute-raccoon-lts-released/80833)

Ubuntu 26.04 LTS（代號「Resolute Raccoon」）正式發布，帶來安全性、效能與可用性的全面提升，支援桌面、伺服器與雲端環境，並提供多種官方衍生版本。

- 🔒 引入 TPM-backed 全碟加密與記憶體安全元件，強化系統安全性與韌性
- 🖥️ 搭載 GNOME 50 on Wayland，提供精緻桌面體驗與無障礙功能
- 🛠️ 擴展 Livepatch 支援 Arm 系統，減少停機時間並提升穩定性
- 🤖 原生支援現代 AI 與高效能運算工具，優化從核心到雲端的效能
- 📦 統一軟體管理體驗，改進應用程式權限控制
- 🎨 同步發布 Edubuntu、Kubuntu、Lubuntu 等官方衍生版本
- ⏳ 桌面與伺服器版提供 5 年維護更新，衍生版本支援 3 年，ESM 提供額外安全支援
- 📥 可從官方網站下載，25.10 用戶自動升級，24.04 LTS 用戶將在 26.04.1 發布後升級

---

### [数据类型——将文本转化为图表的可变字体](https://franktisellano.github.io/datatype/)

**原文标题**: [Datatype — variable font that turns text into charts](https://franktisellano.github.io/datatype/)

概述摘要：Datatype 是一款将文本表达式转换为内嵌图表的可变字体，无需 JavaScript 或图像，通过连字替换实现柱状图、折线图和饼图的实时渲染，并支持字体宽度、粗细等轴调节。

- 📊 **柱状图**：使用 `{b:值}` 语法，支持 0-100 的逗号分隔值，最多 20 个柱，高度按百分比设置。
- 📈 **折线图**：使用 `{l:值}` 语法，支持 0-100 的逗号分隔值，最多 20 个点，高度按百分比设置。
- 🥧 **饼图**：使用 `{p:值}` 语法，单个 0-100 值表示填充百分比。
- 🔧 **可变轴控制**：通过宽度（Width）和重量（Weight）两个轴实时调整图表密度和粗细。
- 📏 **尺寸自适应**：图表在 14px 到 64px 范围内均可清晰渲染，匹配不同字号。
- 🌐 **上下文嵌入**：图表可自然融入表格、仪表盘或段落文本中，支持衬线、无衬线和等宽字体。
- 🛠️ **使用简单**：通过 CSS 加载字体后，在 HTML 中直接输入图表表达式即可，无需额外库。
- 📥 **开源免费**：基于 SIL Open Font License 开源，可在 GitHub 和 Google Fonts 获取。

---

### [数据类型 - Google 字体](https://fonts.google.com/specimen/Datatype)

**原文标题**: [Datatype - Google Fonts](https://fonts.google.com/specimen/Datatype)

概述：本文探讨了人工智能在医疗诊断中的应用，强调了其提高准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🩺 人工智能通过分析医学影像和病历数据，能辅助医生更快速、准确地诊断疾病。
- 📊 机器学习算法在处理大规模医疗数据时，可识别出人类医生可能忽略的细微模式。
- 🔒 数据隐私是主要挑战，患者信息的收集和使用需严格遵守伦理与法律规范。
- ⚖️ 算法偏见可能导致诊断结果不公平，需通过多样化训练数据来缓解这一问题。
- 🌐 人工智能在偏远地区医疗中具有巨大潜力，能弥补专业医生资源不足的短板。

---

### [GitHub - cloudflare/skills: 用于教授代理如何基于 Cloudflare 构建的技能。· GitHub](https://github.com/cloudflare/skills)

**原文标题**: [GitHub - cloudflare/skills: Skills for teaching agents how to build on Cloudflare. · GitHub](https://github.com/cloudflare/skills)

Cloudflare Skills 是一个为 AI 代理（如 Claude Code、Cursor 等）提供技能插件的开源项目，帮助开发者基于 Cloudflare 平台构建应用。

- ⚙️ 支持多种 AI 代理：兼容 Claude Code、Cursor、OpenCode、OpenAI Codex 和 Pi 等代理，可通过插件市场或手动安装。
- 📦 多种安装方式：提供插件市场、Cursor 市场、npx skills CLI 或直接克隆仓库等灵活安装选项。
- 🛠️ 包含命令和技能：提供可调用的斜杠命令（如 /cloudflare:build-agent）和自动加载的技能（如 cloudflare、agents-sdk、durable-objects）。
- 🌐 覆盖 Cloudflare 全平台：技能涵盖 Workers、Pages、存储（KV、D1、R2）、AI（Workers AI、Vectorize）、网络（Tunnel、Spectrum）和安全（WAF、DDoS）。
- 🤖 专注 AI 代理开发：agents-sdk 和 building-ai-agent-on-cloudflare 技能专为构建有状态 AI 代理设计，支持 RPC、WebSockets 和工具集成。
- 🔗 集成 MCP 服务器：包含 cloudflare-api、cloudflare-docs 等远程 MCP 服务器，增强账户管理、文档查询和可观测性功能。
- 📚 提供丰富资源：附带 Cloudflare Agents 文档、MCP 指南、SDK 仓库和入门模板，方便开发者上手。

---

### [代理现在可以创建 Cloudflare 账户、购买域名并进行部署](https://blog.cloudflare.com/agents-stripe-projects/)

**原文标题**: [Agents can now create Cloudflare accounts, buy domains, and deploy](https://blog.cloudflare.com/agents-stripe-projects/)

### 概述总结
AI 代理现在能自动完成 Cloudflare 账户注册、域名购买和代码部署，无需人工手动操作。

- 🤖 **代理自主操作**：AI 代理可代表用户创建 Cloudflare 账户、获取 API 令牌、购买域名并部署应用，全程无需人工干预。
- 🔗 **Stripe 集成协议**：通过与 Stripe 合作的新协议，代理能发现服务、完成身份验证和支付，无需用户提供信用卡信息。
- 🛠️ **零配置启动**：用户只需登录 Stripe 并初始化项目，代理即可自动完成从零到生产环境的部署。
- 💳 **安全支付机制**：Stripe 提供支付令牌，代理无法直接获取信用卡信息，且默认每月消费上限为 100 美元。
- 🌐 **开放平台支持**：任何拥有登录用户的平台都可按此协议与 Cloudflare 集成，实现类似 Stripe 的无缝体验。
- 📋 **发现与授权**：代理通过`stripe projects catalog`命令发现可用服务，并通过 OAuth 自动完成账户创建或授权。
- 🚀 **快速部署示例**：视频演示显示，代理能在两分钟内完成账户创建、域名注册和应用部署的全流程。

---
