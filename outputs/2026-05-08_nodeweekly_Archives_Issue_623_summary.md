### [Node Weekly 第623期：2026年5月7日](https://nodeweekly.com/issues/623)

**原文标题**: [Node Weekly Issue 623: May 7, 2026](https://nodeweekly.com/issues/623)

Node.js 26.0 已发布，包含 Temporal API 默认启用、V8 14.6 和 Undici 8 等新特性。Node 20 已进入生命周期终止阶段。Rolldown 1.0 作为高性能 JS 打包器发布。Node 26.1 新增实验性 FFI 支持。

- 🚀 Node.js 26.0 发布，默认启用 Temporal API，支持 Map 的 upsert 方法和迭代器拼接
- ⚠️ Node 20（Iron）已进入生命周期终止（EOL）
- 📦 Rolldown 1.0 发布，提供 esbuild 级别速度与 Rollup 插件兼容性
- 🧪 Node 26.1 新增实验性 `node:ffi` 模块，支持直接调用 C ABI 库
- 🛠 PM2 7.0 重构，减少外部依赖并扩展 Bun 运行时支持
- 🔄 Valibot 1.4.0 发布，轻量模块化 TypeScript 模式验证库替代 Zod
- 📰 html-to-text 10.0 升级至现代标准，高效转换 HTML 为纯文本
- 🎨 opentype.js 支持读写 OpenType 字体，可创建自定义字体
- 📬 sqs-consumer 15.0 简化 Amazon SQS 应用构建
- ⚡ fast-json-stringify 6.4 比 JSON.stringify() 快 2 倍

---

### [Node.js — Node.js 26.0.0（当前版本）](https://nodejs.org/en/blog/release/v26.0.0)

**原文标题**: [Node.js — Node.js 26.0.0 (Current)](https://nodejs.org/en/blog/release/v26.0.0)

Node.js 26.0.0 正式发布，带来多项重大更新，包括默认启用 Temporal API、V8 引擎升级至14.6、Undici 更新至8.0，以及多项弃用和移除。

- 🎉 **Temporal API 默认启用**：提供更现代、功能更丰富的日期/时间 API，取代旧的 Date 对象。
- ⚡ **V8 引擎升级至 14.6**：包含 Chromium 146 的改进，新增 `Map.getOrInsert()` 和 `Iterator.concat()` 等提案。
- 🌐 **Undici 更新至 8.0.2**：HTTP 客户端实现获得新功能和性能提升。
- 🗑️ **多项弃用与移除**：包括 `crypto`、`http`、`stream` 模块的旧 API 被移除，以及 `module.register()` 等运行时弃用。
- 🔧 **构建工具更新**：GCC 要求提升至 13.2，Python 3.9 支持被移除，并新增 Rust 工具链支持。
- 🛠️ **其他重要变更**：`assert` 支持 printf 风格消息，`crypto` 增加 Ed25519 上下文参数，`esm` 使用 wasm 版 cjs-module-lexer 等。
- 📅 **LTS 计划**：Node.js 26 将于 2026 年 10 月进入长期支持（LTS），目前为“Current”版本。

---

### [《时间：修复JavaScript中时间问题的九年之旅》| 彭博JS博客](https://bloomberg.github.io/js-blog/post/temporal/)

**原文标题**: [Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/temporal/)

Temporal 提案历经9年，终于成为ECMAScript标准，为JavaScript带来了现代化的日期时间API，解决了Date对象长期存在的问题。

- 📅 **Temporal 成为 ES2026 标准**：经过9年努力，Temporal 提案于2026年3月达到 Stage 4，将正式纳入 ECMAScript 2026 规范。

- 🕰️ **Date 对象的根本缺陷**：1995年设计的 Date 存在可变性、月份算术不一致、解析歧义等问题，在复杂应用中成为开发痛点。

- 📚 **第三方库的兴起与局限**：Moment.js 等库虽解决了部分问题，但带来了包体积膨胀、无法树摇等新问题，促使标准化需求。

- 👥 **多方协作的标准化过程**：Microsoft、Bloomberg、Igalia、Google 等公司的工程师组成 Champion 团队，共同推动提案从 Stage 1 到 Stage 4。

- 🔧 **Temporal 的核心类型设计**：提供 ZonedDateTime、Instant、PlainDate/Time/DateTime、Duration 等不可变类型，支持时区、日历和纳秒精度。

- 🌍 **日历与时区支持**：Temporal 支持多种日历系统（如希伯来历），并能正确处理夏令时转换，避免 Date 的常见错误。

- ⚡ **跨引擎实现挑战**：Temporal 是 ES2015 以来最大的语言特性，测试用例约4500个，远超 Date。多引擎通过共享 Rust 库 temporal_rs 实现协作。

- 🚀 **当前浏览器支持**：Firefox v139、Chrome v144、Edge v144、TypeScript 6.0 Beta 已支持，Safari 部分支持。

- 🔗 **未来生态整合**：需要与 Date Picker、DOMHighResTimeStamp 等 Web API 集成，进一步扩展 Temporal 的应用场景。

---

### [GitHub - tc39/proposal-upsert: Map.prototype.upsert 的 ECMAScript 提案、规范及参考实现](https://github.com/tc39/proposal-upsert)

**原文标题**: [GitHub - tc39/proposal-upsert: ECMAScript Proposal, specs, and reference implementation for Map.prototype.upsert · GitHub](https://github.com/tc39/proposal-upsert)

概述摘要
- 📊 该提案为 Map 和 WeakMap 添加了 getOrInsert 和 getOrInsertComputed 方法，简化键值操作。
- 🎯 核心动机：解决在不确定键是否存在时，需要多次查找 Map 的问题，提高开发效率和性能。
- 💡 getOrInsert 方法：若键存在则返回值，否则插入默认值并返回，避免覆盖已有值。
- 🔄 getOrInsertComputed 方法：类似但使用回调函数计算默认值，适合成本较高的默认值场景。
- 📋 常见用例：处理默认值、增量分组数据、维护计数器等，代码更简洁高效。
- 🌐 其他语言类似功能：Java 的 computeIfAbsent、Python 的 setdefault、Rust 的 or_insert_with 等。
- 🛠 该提案处于 Stage 4，已提供 polyfill 实现，易于集成。

---

### [GitHub - tc39/proposal-iterator-sequencing：一个TC39提案，通过序列化现有迭代器来创建迭代器 · GitHub](https://github.com/tc39/proposal-iterator-sequencing)

**原文标题**: [GitHub - tc39/proposal-iterator-sequencing: a TC39 proposal to create iterators by sequencing existing iterators · GitHub](https://github.com/tc39/proposal-iterator-sequencing)

此提案旨在为JavaScript提供一种更简洁的方式来串联多个迭代器，使其像一个单一迭代器一样按顺序输出值。

- 📜 **核心功能**：通过 `Iterator.concat(lows, [4,5], highs)` 方法，将多个迭代器或可迭代对象按顺序连接成一个新迭代器
- 🔄 **现有方案**：目前需使用生成器函数（`function*`）配合 `yield*` 手动实现，代码冗长
- 🌍 **跨语言参考**：类似Python的`chain`、Ruby的`chain`、Rust的`chain`/`flatten`等标准库功能
- 📊 **提案状态**：已进入TC39 Stage 4阶段，规范地址为tc39.es/proposal-iterator-sequencing
- ⚙️ **无限迭代器处理**：对于嵌套无限迭代器，建议使用 `Iterator.prototype.flatMap` 配合恒等函数
- 📚 **社区支持**：已有多个JS库（如lodash、ramda、immutable.js）提供类似功能，但缺乏原生支持

---

### [Node.js — Node.js 26.1.0（当前版本）](https://nodejs.org/en/blog/release/v26.1.0)

**原文标题**: [Node.js — Node.js 26.1.0 (Current)](https://nodejs.org/en/blog/release/v26.1.0)

Node.js 26.1.0 版本发布，包含实验性 FFI 模块和多项功能增强。

- 🧪 实验性 `node:ffi` 模块，支持从 JavaScript 加载动态库和调用原生符号，需 `--experimental-ffi` 标志
- 📦 `buffer` 模块新增 `end` 参数
- 🔐 `crypto` 模块：`diffieHellman()` 接受密钥数据，并实现 `randomUUIDv7()`
- 🐞 `debugger` 模块：在 `node inspect` 中添加编辑时运行时表达式探针
- 📁 `fs` 模块：`fs.stat()` 新增 `signal` 选项，`statfs` 暴露 `frsize` 字段
- 🌐 `http` 模块：强化 `ClientRequest` 选项合并，`IncomingMessage` 新增 `req.signal`
- ⚙️ `process` 模块：`execve(2)` 失败时抛出错误而非中止
- 🔧 `src` 模块：允许空 `--experimental-config-file`
- 🌊 `stream` 模块：`duplexPair` 中传播销毁事件
- 🧪 `test_runner` 模块：对齐 mock 超时 API，支持 `AbortSignal.timeout` 和测试顺序随机化
- 🎨 `util` 模块：支持使用十六进制颜色为文本着色

---

### [使用Memetria K/V构建 — Memetria](https://dashboard.memetria.com/nodeweekly/)

**原文标题**: [Build with Memetria K/V — Memetria](https://dashboard.memetria.com/nodeweekly/)

Memetria 提供基于 Valkey 和 Redis OSS 的托管服务，支持无缝扩展、加密监控，并提供多种开发、生产及高性能方案。

- 🗄️ 兼容 Valkey 和 Redis OSS，支持轻松导入导出
- 📈 无缝扩展：无需停机即可调整资源
- 🔒 双重加密：支持 TLS 连接选项
- 📊 详细监控：提供健康、内存和性能图表
- 💼 多种方案：开发版（$14/月起）、生产版（$89/月起）、高性能版（$779/月起）
- 🌍 全球区域：覆盖非洲、亚太、欧洲、美洲等 20 个 AWS 区域
- 💾 容量选择：从 160 MB 到 350 GB 多种规格
- 📧 注册流程：提供工作邮箱，需同意服务条款和隐私政策

---

### [Node.js — 参会报告：Node.js 协作峰会（2026 伦敦）](https://nodejs.org/en/blog/events/collab-summit-2026-london)

**原文标题**: [Node.js — Trip report: Node.js collaboration summit (2026 London)](https://nodejs.org/en/blog/events/collab-summit-2026-london)

以下是2026年伦敦Node.js协作峰会的总结摘要：

- 📅 峰会于2026年4月在伦敦由Bloomberg主办，吸引超过40名现场参与者及十余名远程参与者。
- 📊 Next-10会议回顾了2025-2026年协作者健康调查结果，并讨论了2026年调查问题，包括AI相关议题。
- 🚀 新发布计划：自Node.js v27起，版本号与日历年份对齐，减少并发发布线以应对安全漏洞管理挑战。
- 🌊 新Streams API提案利用异步迭代（async/await），旨在统一Node.js与Web流，已作为实验性功能在v25.9.0中发布。
- 🤝 协作者计划讨论降低贡献门槛，包括代码所有权强制执行、扩展审查权限至工作组成员等。
- 🔍 OpenTelemetry项目介绍：作为CNCF下的可观测性标准，涵盖追踪、指标和日志，并讨论原生支持。
- 🛠️ 可观测性基础设施改进：包括AsyncLocalStorage语法支持、新diagnostic_channel API及内置OTLP协议支持。
- 🤖 AI贡献争议：讨论AI生成代码的利弊，包括审查负担、伦理问题及治理策略，如要求设计文档和明确维护者批准。
- 🔄 用户空间迁移：Node.js 22.x至24.x的弃用迁移接近完成，v25.9.0发布codemod工具。
- 📦 模块钩子稳定化：module.register()被弃用，推荐使用module.registerHooks()，并讨论vm.Module API新设计。
- 🧩 Libuv v2：计划引入破坏性变更以清理代码库，可能从Node.js 27开始支持，同时维护v1安全补丁。
- 📁 虚拟文件系统（VFS）提案：通过node:vfs模块标准化文件系统虚拟化，支持单执行文件应用和测试。
- 🔒 安全生态现状：AI生成漏洞报告激增导致维护负担加重，团队探索公开安全流程以减少误报和加速修复。
- 🙏 感谢Bloomberg主办及所有组织者与参与者，峰会录像已上传至YouTube。

---

### [可迭代流 | Node.js v25.9.0 文档](https://nodejs.org/docs/latest-v25.x/api/stream_iter.html#iterable-streams)

**原文标题**: [Iterable Streams | Node.js v25.9.0 Documentation](https://nodejs.org/docs/latest-v25.x/api/stream_iter.html#iterable-streams)

Node.js v25.9.0 的 `node:stream/iter` 模块提供了一套基于可迭代对象的流式 API，它不同于传统的事件驱动流或 Web Streams，需要 `--experimental-stream-iter` 标志启用。数据以 `Uint8Array[]` 批次流动，支持拉取和推送两种模型，并内置了多种背压策略。

- 📜 **核心概念**：流表示为 `AsyncIterable<Uint8Array[]>` 或 `Iterable<Uint8Array[]>`，数据以批次形式流动以摊销异步开销。转换器可以是无状态函数或有状态对象。
- 🔄 **拉取 vs 推送**：`pull()` 创建惰性管道，消费者驱动数据读取；`push()` 创建写入/读取对，需要显式背压管理。
- 🗜️ **背压策略**：支持 `strict`（默认，限制槽位和待写入队列）、`block`（仅限制槽位）、`drop-oldest`（丢弃最旧数据）和 `drop-newest`（丢弃最新数据）。
- ✍️ **写入器接口**：提供 `write()`、`writev()`、`end()`、`fail()` 等方法，以及同步变体（如 `writeSync`）用于快速路径回退。
- 🔗 **管道操作**：`pipeTo()` 将源通过转换器连接到写入器，自动尝试同步方法；`pull()` 创建惰性管道；`pullSync()` 为同步版本。
- 📦 **消费者函数**：`text()`、`bytes()`、`array()`、`arrayBuffer()` 等用于消费流数据，支持 `limit` 和 `signal` 选项。
- 🌐 **多消费者**：`broadcast()` 用于推送模式的多消费者广播；`share()` 用于拉取模式的多消费者共享，消费者共享同一缓冲区。
- 🔧 **实用工具**：`merge()` 合并多个源，`tap()` 创建观察转换，`ondrain()` 等待背压清除。
- 🏷️ **协议符号**：`Stream.toAsyncStreamable`、`Stream.broadcastProtocol` 等允许第三方对象参与流协议，无需直接导入模块。
- ⚡ **压缩转换**：通过 `node:zlib/iter` 模块提供 Gzip 等压缩/解压转换，可与 `pull()` 和 `pipeTo()` 配合使用。

---

### [Node.js — 生命周期结束](https://nodejs.org/en/about/eol)

**原文标题**: [Node.js — End-Of-Life](https://nodejs.org/en/about/eol)

Node.js 版本生命周期终止（EOL）概述  
- 📅 **版本终止含义**：当 Node.js 主版本达到 EOL 后，将不再获得任何更新（包括安全补丁），继续使用会面临安全风险。  
- 🔒 **漏洞无修复**：即使新版本修复了漏洞，EOL 版本也不会获得补丁，用户易受攻击。  
- 🔧 **工具链中断**：EOL 版本可能无法链接新版共享库，导致系统更新受阻或崩溃。  
- 🌐 **生态脱节**：主流 npm 包逐渐放弃对 EOL 版本的支持，使用旧版会导致更多未修复漏洞。  
- ⚠️ **合规风险**：行业审计通常禁止使用未维护的运行时环境。  
- 📊 **历史版本状态**：v0 至 v23 等多个版本已标记 EOL，其中 v20 和 v18 等 LTS 版本仍处于维护期。  
- 💼 **商业支持方案**：通过 OpenJS 基金会，HeroDevs 和 NodeSource 提供 EOL 版本的安全补丁和合规支持，但仅为过渡方案，最终应升级至活跃版本。

---

### [发布 electron v42.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v42.0.0)

**原文标题**: [Release electron v42.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v42.0.0)

Electron v42.0.0 是一个重大版本更新，带来了 Chromium、Node.js 和 V8 的升级，以及多项新功能、破坏性变更和大量 Bug 修复。

- ⬆️ **核心升级**：Chromium 升级至 148.0.7778.96，Node.js 升级至 v24.15.0，V8 升级至 14.8。
- ⚠️ **破坏性变更**：macOS 通知改用 `UNNotification` API，要求应用必须代码签名；`electron` 包不再通过 `postinstall` 脚本下载二进制文件，改为首次运行时动态下载；离屏渲染默认设备缩放因子改为常量 `1.0`；移除了 `Session.clearStorageData()` 中的 `quotas` 参数和 `ELECTRON_SKIP_BINARY_DOWNLOAD` 环境变量。
- ✨ **新增功能**：新增 WebAuthn Touch ID 支持 (macOS)、`Notification.getHistory()` (macOS)、`Notification.handleActivation()` (Windows)、`app.isActive()` (macOS)、全局快捷键挂起/恢复、MSIX 自动更新支持、`--experimental-transform-types` 支持、堆分析、P010le 10-bit YUV 纹理导入、`urgency` 通知选项 (Windows) 等。
- 🐛 **大量 Bug 修复**：修复了包括崩溃、内存泄漏、渲染问题、窗口大小调整、通知行为、网络请求、ASAR 支持、DevTools、打印、无障碍、安全性等多个方面的大量问题。
- 🔒 **安全更新**：向后移植了多个 CVE 安全漏洞的修复。
- 🛠️ **其他改进**：使用 oxlint 和 oxfmt 替换 ESLint 用于 JS/TS 格式化；限制 npm tarball 内容为显式允许列表；启用了 V8 builtins 的配置文件引导优化。

---

### [GitHub - boa-dev/temporal：ECMAScript Temporal API 的 Rust 实现 · GitHub](https://github.com/boa-dev/temporal)

**原文标题**: [GitHub - boa-dev/temporal: A Rust implementation of ECMAScript's Temporal API · GitHub](https://github.com/boa-dev/temporal)

temporal_rs 是一个基于 Rust 的日期/时间库，遵循 ECMAScript Temporal 规范，支持日历和时区计算，旨在实现 100% 测试合规，并已用于 Boa、Kiesel 和 V8 等项目。

- 📅 **核心功能**：提供 8 种日期时间类型（如 PlainDate、ZonedDateTime、Instant 等），支持日历和时区感知。
- 🌐 **日历与时区支持**：轻松转换日历（如 ISO 到日本历）和时区（如 America/Chicago 到 Europe/Zurich）。
- 🛠️ **设计灵活性**：提供 HostHooks 和 TimeZoneProvider 特征，允许自定义主机系统和时区数据，适用于 ECMAScript 解释器或原生 Rust 程序。
- 📚 **项目组成**：包含多个 crate，如 temporal_rs（核心库）、temporal_capi（C/C++ FFI）、timezone_provider（时区数据提供者）等。
- ⚙️ **无需默认特性**：无默认特性时，不嵌入时区数据，可通过 _with_provider API 手动提供时区数据。
- ✅ **合规性**：严格遵循 Temporal 语法（RFC9557/IXDTF），并可通过 Boa 的 test262 页面查看测试结果。
- 🤝 **开源贡献**：欢迎参与，提供贡献指南（CONTRIBUTING.md），可通过 Matrix 沟通。
- 📄 **许可**：采用 Apache-2.0 或 MIT 许可证。

---

### [node/BUILDING.md 位于主分支 · nodejs/node · GitHub](https://github.com/nodejs/node/blob/main/BUILDING.md#building-nodejs-with-temporal-support)

**原文标题**: [node/BUILDING.md at main · nodejs/node · GitHub](https://github.com/nodejs/node/blob/main/BUILDING.md#building-nodejs-with-temporal-support)

本文档详细介绍了在不同平台上构建Node.js的方法、支持平台、工具链要求及测试流程。

- 📋 **支持平台分三级**：Tier 1（主流平台，如Linux x64/arm64、macOS arm64、Windows x64）、Tier 2（较小用户群，如ppc64le、s390x、AIX）和Experimental（实验性平台，如Alpine、FreeBSD、OpenHarmony）
- 🔧 **必备工具链**：Linux需GCC ≥13.2或Clang ≥19.1；Windows需Visual Studio 2022/2026及ClangCL；macOS需Xcode ≥16.4
- 🛠️ **构建步骤**：Unix/macOS使用`./configure && make -j4`；Windows使用`.\vcbuild`；可通过Ninja加速
- ✅ **测试方法**：`make test-only`运行基础测试；`make -j4 test`完整测试；`tools/test.py`可指定单文件或子系统测试
- 📊 **代码覆盖率**：`./configure --coverage && make coverage`生成JS和C++覆盖率报告
- 🚀 **开发加速技巧**：使用ccache缓存编译结果；mold加速链接；`--node-builtin-modules-path`从磁盘加载JS文件
- 🌐 **国际化支持**：默认full-icu；可选small-icu（仅英文）或system-icu；也可完全禁用Intl
- 🔒 **安全特性**：支持FIPS兼容OpenSSL 3；可自定义OpenSSL配置节名称
- 🕐 **Temporal API**：需Rust工具链（rustc ≥1.82）构建支持
- 📦 **外部模块集成**：通过`--link-module`将自定义JS文件作为内置模块打包
- ⚠️ **分发注意事项**：需保持ABI兼容性，使用自定义NODE_MODULE_VERSION时需注册至官方registry

---

### [宣布 Rolldown 1.0 | VoidZero](https://voidzero.dev/posts/announcing-rolldown-1-0)

**原文标题**: [Announcing Rolldown 1.0 | VoidZero](https://voidzero.dev/posts/announcing-rolldown-1-0)

Rolldown 1.0 稳定版发布，这是一款基于 Rust 的高性能 JavaScript 打包工具，现已达到生产就绪状态，并作为 Vite 8 的默认打包器。

- 🚀 Rolldown 1.0 稳定版发布，采用语义化版本控制，API 保持向后兼容。
- ⚡ 速度比 Rollup 快 10-30 倍，与 esbuild 相当，基于 Rust 和 Oxc 构建。
- 🔌 兼容 Rollup 插件 API，支持钩子过滤器以减少性能开销。
- 🧩 提供额外功能，如更激进的死代码消除和细粒度代码分割。
- 🏢 已被 Framer、PLAID 等公司用于生产环境，显著缩短构建时间。
- 📦 可通过独立安装或 Vite 8 使用，支持自定义分块规则。
- 🔧 从最新 RC 升级无需代码更改，新增原生 MagicString 和监视模式。
- 🎯 未来计划包括 Vite 全包模式（开发时打包）和惰性桶优化。
- 🙌 感谢约 200 名贡献者，欢迎新贡献者参与文档、插件测试和问题修复。

---

### [发布 v0.22.0 · rolldown/tsdown · GitHub](https://github.com/rolldown/tsdown/releases/tag/v0.22.0)

**原文标题**: [Release v0.22.0 · rolldown/tsdown · GitHub](https://github.com/rolldown/tsdown/releases/tag/v0.22.0)

tsdown v0.22.0 版本发布，包含多项破坏性变更、新功能和错误修复。

- 🚨 **破坏性变更**：最低 Node.js 版本提升至 22.18.0，`unrun` 不再捆绑，需手动安装；`dts` 在 tsconfig 中 declaration 为 true 时自动启用；`publint` 要求 v0.3.8+。
- 🚀 **新功能**：升级 rolldown 至 v1.0.0；`exports` 默认自动检测并启用 bin 字段。
- 🐞 **错误修复**：明确移除 Node 23 支持；增强打包调试日志；修复条件导出中 types 字段检测和重复配置警告逻辑。
- 📝 **迁移指南**：升级 Node.js 至 22.18.0+；如需 `unrun` 或 `tsx` 加载器，请手动安装；`dts` 可通过配置显式禁用；`exports.bin` 自动检测 shebang，支持自定义行为。

---

### [为什么迁移到Valibot？ | Valibot](https://valibot.dev/blog/why-migrate-to-valibot/)

**原文标题**: [Why migrate to Valibot? | Valibot](https://valibot.dev/blog/why-migrate-to-valibot/)

Valibot 是一个兼具启动性能、类型安全、清晰心智模型和模块化架构的 schema 库，适合现代 TypeScript 应用，迁移成本低且代码风格熟悉。

- 🚀 **更优的启动性能**：Valibot 仅需 1.91 kB gzipped，初始化速度比 Zod v4 快 16 倍，适合网站、Web 应用和无服务器运行时。
- 🧠 **清晰的心智模型**：API 简化为 schemas、methods 和 actions 三个构建块，易于理解和扩展，尤其适合大型代码库。
- 🛡️ **更精确的类型安全**：不仅推断输出类型，还提供 schema 可能产生的 issue 类型，减少错误并提升开发者体验。
- 🔗 **统一的管道设计**：验证、转换和元数据通过管道（pipeline）按步骤组合，简单易用且可扩展，如添加 LEGO 积木般灵活。
- 📦 **功能丰富但轻量**：内置 46 个 schemas 和 118 个 actions（如 email、url、trim 等），模块化设计确保只加载使用部分，不增加负担。
- 🧩 **易于扩展和推理**：schemas 和 actions 是普通对象，可自定义构建，适合应用、库和领域特定工具的开发。
- 🤖 **适配 AI 编码助手**：结构明确、可预测，便于 AI 工具检查、理解和修改，支持元数据（如 title、description）和 llms.txt 路由。
- ✅ **总结**：Valibot 不是简单的小型替代品，而是精心设计的系统，平衡了性能、类型安全和扩展性，推荐通过迁移指南或 playground 尝试。

---

### [Valibot：模块化且类型安全的模式库](https://valibot.dev/)

**原文标题**: [Valibot: The modular and type safe schema library](https://valibot.dev/)

Valibot 是一个专为 TypeScript 设计的开源 schema 库，注重包体积、类型安全和开发者体验。

- 🔒 完全类型安全：在 TypeScript 中享受类型安全和静态类型推断的好处
- 📦 小包体积：由于 API 的模块化设计，包体积从不到 700 字节起
- 🚧 验证一切：支持从原始值到复杂对象的几乎所有 TypeScript 类型
- 🛟 100% 测试覆盖率：Valibot 的源代码是开源的，并经过 100% 覆盖率的全面测试
- 🔋 包含辅助工具：重要的验证和转换辅助工具已内置
- 🧑‍💻 开发者体验优秀的 API：提供最小化、可读性强且经过深思熟虑的 API，带来出色的开发者体验
- 💰 免费且开源：基于 MIT 许可证，免费使用，依赖合作伙伴和赞助者支持
- ⚙️ 核心功能：创建 schema 描述结构化数据，可在运行时执行以确保未知数据的类型安全
- 🌳 模块化设计减少包体积：通过 tree shaking 和代码分割，仅将实际使用的代码包含在生产构建中
- 📊 与 Zod 对比：功能相似，但模块化设计可将包体积减少高达 95%，特别适合客户端表单验证和无服务器环境

---

### [发布 v1.4.0 · open-circle/valibot · GitHub](https://github.com/open-circle/valibot/releases/tag/v1.4.0)

**原文标题**: [Release v1.4.0 · open-circle/valibot · GitHub](https://github.com/open-circle/valibot/releases/tag/v1.4.0)

概述摘要  
- 🚀 发布 v1.4.0 版本，感谢 11 位贡献者。  
- 📅 新增 `isoDateTimeSecond` 验证动作，支持带秒的 ISO 日期时间。  
- 🔄 添加 `toCamelCase`、`toKebabCase`、`toPascalCase` 和 `toSnakeCase` 转换动作，用于字符串命名格式转换。  
- ⚡ 改进 `object` 和 `record` 模式的 TypeScript 类型性能。  
- 🛠️ 优化热路径，减少对象分配并提升运行时性能。  
- 🎯 将构建目标改为 ES2020，确保兼容性。  
- 🔒 内部 `_LruCache` 改用 TypeScript `private` 方法，避免运行时辅助函数。  
- 🧩 修复 `flatten` 方法，支持只读问题数组。  
- 🐛 修复 `creditCard` 验证，拒绝无效长度的 Mastercard 号码。  
- 🔧 修复 `intersect` 模式，不再修改输入值，支持冻结对象和数组合并。

---

### [node-html-to-text/packages/html-to-text/README.md 位于 master 分支 · html-to-text/node-html-to-text · GitHub](https://github.com/html-to-text/node-html-to-text/blob/master/packages/html-to-text/README.md)

**原文标题**: [node-html-to-text/packages/html-to-text/README.md at master · html-to-text/node-html-to-text · GitHub](https://github.com/html-to-text/node-html-to-text/blob/master/packages/html-to-text/README.md)

html-to-text 是一个高级 HTML 转换工具，能够将 HTML 内容解析为格式优美的纯文本，支持多种自定义选项和格式化功能。

- 📦 **核心功能**：支持内联和块级标签、表格（含跨行跨列）、链接（文本和 href）、自动换行、Unicode 以及丰富的自定义选项。
- ⚙️ **安装与使用**：通过 npm 安装，提供 `convert` 和 `compile` 两种方式，后者适合批量处理以提升性能。
- 🎯 **选择器系统**：支持 CSS 选择器（如标签、类、ID、属性、伪类），用于精确控制元素格式化，具有优先级和合并规则。
- 🛠️ **自定义格式化**：可通过 `formatters` 选项定义自己的格式化函数，访问元素、子节点、构建器和选项，实现灵活输出。
- 📊 **预定义格式**：内置多种格式（如 `anchor`、`heading`、`table`、`dataTable`），并支持 `skip`、`blockString` 等特殊格式。
- 🔧 **选项丰富**：包括基础元素选择、实体解码、字符编码、输出限制、长词换行、空白字符处理等，并支持元数据传递。
- 📜 **版本历史**：从 v6 到 v10 不断演进，移除了许多旧选项，增加了选择器支持、ESM 模块、Node.js 20+ 等新特性。
- 🤝 **社区与许可**：由 @mlegenhausen 创建，@KillyMXI 维护，采用 MIT 许可，欢迎通过 Issues 和 PR 贡献。

---

### [免费试用 Tiger Cloud：$1,000 信用额度 | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Try Tiger Cloud Free: $1,000 Credit | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

本内容介绍了Tiger Cloud的免费试用及核心功能，强调弹性扩展、成本优化和高可用性。

- 💰 注册即获$1,000信用额度，30天有效，无需信用卡，仅限新用户
- 🔄 通过最多10个节点的副本集分离读写，结合SSD/S3分层存储，实现无底容量与成本效益
- ⚡ 计算与存储分离，独立扩展，避免为闲置容量付费，优化性能与成本
- 🛡️ 多可用区集群，自动故障转移、时间点恢复及跨区域备份，确保高可用性
- 🔒 符合SOC 2、HIPAA、GDPR标准，支持始终加密、SSO、RBAC和审计日志
- 📊 提供查询钻取和仪表盘，集成CloudWatch、Datadog、Prometheus等监控工具
- 🚀 分钟级数据库部署，支持SQL、CLI、Terraform、Cursor或Claude Code管理
- 🤝 企业级信任：合同SLA、区域数据隔离、合规认证，以及24/7全球Postgres专家支持

---

### [发布 v7.0.0 · Unitech/pm2 · GitHub](https://github.com/Unitech/pm2/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · Unitech/pm2 · GitHub](https://github.com/Unitech/pm2/releases/tag/v7.0.0)

PM2 v7.0.0 版本发布，包含重大变更、核心重构、安全修复和多项改进。

- 🚨 重大变更：要求 Node.js >= 18.0.0，放弃对 Node.js 16 的支持
- 🔧 核心重构：将多个依赖模块内部化，减少供应链攻击面；新增 Bun 运行时支持
- 🔒 安全修复：修复 ReDoS 漏洞 (CVE-2025-5891)、命令注入漏洞和原型污染问题
- 🐛 错误修复：重写 TreeKill 消除竞态条件；修复 Windows 路径和 fork 模式环境变量泄漏
- ✨ 新功能：`pm2 serve` 新增 `--ftp` 选项，支持目录列表
- 📦 依赖更新：添加 OpenTelemetry 追踪支持；升级 pidusage、ws 等；移除多个旧依赖
- 🧪 测试改进：新增 Docker 并行测试、Windows 测试套件和 OpenTelemetry 测试

---

### [PM2 - 首页](https://pm2.keymetrics.io/)

**原文标题**: [PM2 - Home](https://pm2.keymetrics.io/)

概述摘要
- 📦 PM2 是一个 Node.js 的高级进程管理器，可让应用 24/7 在线运行，通过 `npm install pm2 -g` 安装。
- ⚙️ 提供完整的生产环境功能集，包括行为配置、源映射支持和容器集成。
- 🔄 支持文件变动时自动监视与重载，以及热重载功能。
- 📊 内置日志管理和监控工具，可通过 `pm2 monit` 查看所有进程状态。
- 🧠 具备最大内存重载和集群模式，优化应用性能。
- 🛠️ 提供模块系统、启动脚本和部署工作流，兼容 PaaS 平台。
- 🔗 集成 Keymetrics 监控，并支持 API 管理。
- 🚀 常用命令包括 `pm2 start app.js` 启动、`pm2 list` 列出进程、`pm2 stop/restart/delete` 管理进程。
- 💬 用户评价：安装简便、性能提升显著、优于其他工具如 forever。

---

### [GitHub - delvedor/find-my-way: 一个极速HTTP路由器](https://github.com/delvedor/find-my-way)

**原文标题**: [GitHub - delvedor/find-my-way: A crazy fast HTTP router · GitHub](https://github.com/delvedor/find-my-way)

find-my-way 是一个基于高性能 Radix Tree（紧凑前缀树）的极速 HTTP 路由库，支持路由参数、通配符，并且与框架无关。它被 Fastify 和 Restify 等框架使用，提供了丰富的 API 和灵活的约束功能。

- 🚀 **高性能路由**：内部使用 Radix Tree 实现，速度极快，支持路由参数、通配符和正则表达式。
- 📦 **安装简单**：通过 `npm i find-my-way --save` 即可安装。
- 🛠️ **丰富的 API**：包括 `on()`、`off()`、`find()`、`lookup()`、`reset()` 等方法，支持路由注册、注销、查找和重置。
- 🔄 **版本化路由**：支持基于 semver 的版本约束，通过 `Accept-Version` 头部实现多版本路由。
- 🌐 **自定义约束策略**：允许添加自定义约束（如主机名、Accept 头部），并支持同步和异步的 `deriveConstraint` 函数。
- 📝 **路径格式灵活**：支持静态路径、参数化路径（`:param`）、通配符（`*`）和正则表达式路径。
- 🔍 **匹配顺序明确**：静态节点优先，其次是参数化节点（带静态结尾、正则、多参数、普通参数），最后是通配符。
- 🔧 **配置选项丰富**：支持 `ignoreTrailingSlash`、`ignoreDuplicateSlashes`、`caseSensitive`、`maxParamLength` 等选项。
- 📊 **调试工具**：提供 `prettyPrint()` 方法打印路由树，`routes` 属性列出所有注册路由。
- ⚠️ **注意事项**：不能注册仅参数不同的重复路由，正则表达式可能影响性能，自定义约束需谨慎使用。

---

### [opentype.js – 用于OpenType和TrueType字体的JavaScript解析器/写入器](https://opentype.js.org/)

**原文标题**: [opentype.js – JavaScript parser/writer for OpenType and TrueType fonts.](https://opentype.js.org/)

无法总结：未找到主要内容。

---

### [GitHub - opentypejs/opentype.js：使用JavaScript读写OpenType字体。](https://github.com/opentypejs/opentype.js)

**原文标题**: [GitHub - opentypejs/opentype.js: Read and write OpenType fonts using JavaScript. · GitHub](https://github.com/opentypejs/opentype.js)

opentype.js 是一个用 JavaScript 编写的开源库，可在浏览器和 Node.js 中读取和写入 OpenType 字体，提供对文字字形的访问。

- 📖 **核心功能**：从文本创建贝塞尔路径，支持复合字形、WOFF/OTF/TTF 字体、字距调整、连字、TrueType 字体提示、阿拉伯语和表情符号渲染，并可选低内存模式。
- 🛠️ **安装方式**：支持通过 CDN 或 npm 包管理器安装，并提供了 TypeScript 使用示例。
- 🚀 **使用指南**：详细说明了加载字体（包括 WOFF2 的解压处理）、从零创建字体、保存字体文件的方法，以及 Font、Glyph、Path 等核心对象的属性和方法。
- 🎨 **高级特性**：包含调色板管理（PaletteManager）、颜色字形图层管理（LayerManager）和可变字体属性管理（VariationManager），用于处理 COLR/CPAL 表和字体变体。
- 📜 **版本与许可**：遵循 SemVer 版本控制，采用 MIT 许可证，并致谢了 pdf.js、FreeType 等项目。

---

### [GitHub - bbc/sqs-consumer: 无需样板代码即可构建基于亚马逊简单队列服务（SQS）的应用程序](https://github.com/bbc/sqs-consumer)

**原文标题**: [GitHub - bbc/sqs-consumer: Build Amazon Simple Queue Service (SQS) based applications without the boilerplate · GitHub](https://github.com/bbc/sqs-consumer)

sqs-consumer 是一个用于构建 Amazon SQS 应用的 Node.js 库，简化消息处理流程，无需样板代码。

- 📦 **安装与版本**：通过 `npm install sqs-consumer` 安装，支持 JSR，仅维护 Node 活跃或安全支持的版本。
- 🚀 **快速使用**：创建 Consumer 实例，定义 `handleMessage` 异步函数处理消息，监听 `error` 和 `processing_error` 事件，调用 `start()` 开始轮询。
- 🔄 **轮询与消息处理**：默认使用长轮询连续拉取消息，单条处理（需 await），通过 `batchSize` 选项实现并行处理。
- ✅ **消息确认行为**：`alwaysAcknowledge` 为 false 时，返回 undefined/{} 不删除消息，返回消息对象则删除；`strictReturn` 为 true 时返回 null 会报错；`alwaysAcknowledge` 为 true 时始终删除。
- ⚠️ **错误处理与重试**：处理函数抛出错误或返回拒绝的 Promise 时，消息保留在队列中，可配合 SQS 死信队列策略。
- 🔢 **FIFO 队列支持**：需设置 `suppressFifoWarning: true` 并始终使用 `handleMessageBatch` 方法以维护顺序。
- 🔑 **凭证配置**：默认从环境变量读取 AWS 凭证，也可手动传入 SQSClient 实例指定 region 和 credentials。
- 🛡️ **IAM 权限**：需授予 `sqs:ReceiveMessage`、`sqs:DeleteMessage`、`sqs:ChangeMessageVisibility` 等权限。
- ⏹️ **优雅关闭**：调用 `stop()` 停止轮询，设置 `pollingCompleteWaitTimeMs` 等待当前处理完成，支持 `abort` 选项中断请求。
- 📊 **状态与更新**：`consumer.status` 返回 `isRunning` 和 `isPolling` 状态；`updateOption()` 可动态更新配置（如 `pollingWaitTimeMs` 下次轮询生效）。
- 📡 **事件监听**：Consumer 是 EventEmitter，可监听多种事件（如 `error`、`processing_error`、`stopped` 等）。
- 🤝 **贡献与许可**：欢迎贡献，遵循贡献指南和行为准则；基于 Apache 2.0 许可证分发。

---

### [发布 pnpm 11.0.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.8)

**原文标题**: [Release pnpm 11.0.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.8)

pnpm v11.0.8 版本发布，主要修复了锁文件、生命周期脚本和 tarball 下载的相关问题。

- 🛠️ 修复了 `pnpm-lock.yaml` 中 tarball URL 的保留策略，确保在无法从名称+版本+注册表推导 URL 时仍能保留，避免 `pnpm install --frozen-lockfile` 从空存储安装时出现 `ERR_PNPM_FETCH_404` 错误
- 📜 为 `pnpm version` 命令添加了 `preversion`、`version` 和 `postversion` 生命周期脚本的执行支持
- 🔧 修复了 `ERR_PNPM_BAD_TARBALL_SIZE` 错误，当注册表提供带有端到端 `Content-Encoding`（如 gzip）的 tarball 时，现在请求时使用 `Accept-Encoding: identity`，并取消了对声明 `Content-Encoding` 的响应进行严格的 `Content-Length` 检查

---

### [发布 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases)

**原文标题**: [Releases · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases)

pnpm 发布了多个版本更新，包括 v11.0.8、v11.0.7、v10.33.4、v11.0.6、v11.0.5、v10.33.3、v11.0.4、v11.0.3、v11.0.2 和 v11.0.1，主要修复了各种 bug 并引入了一些新功能。

- 🐛 修复了 `pnpm install --frozen-lockfile` 在非标准路径（如 GitHub Packages）上因 tarball URL 丢失而失败的问题（v11.0.8）
- 🛠️ 恢复了 `node-gyp` 在 `@pnpm/exe` 中的可执行权限，修复了生命周期脚本中的权限错误（v11.0.7）
- 🔒 为 git 托管的 tarball 添加了完整性校验，防止后续安装中被篡改（v11.0.7, v10.33.4）
- 🚀 修复了 `pnpm dlx` 和 `pnpx` 在 Git Bash/Windows 上的别名问题（v11.0.7）
- 📦 改进了 `pnpm fetch` 后的 `node_modules` 重建逻辑，避免不必要的清除（v11.0.7）
- 🗂️ 允许在全局 `config.yaml` 中设置更多用户级偏好（v11.0.7）
- 🔑 使 OIDC 可信发布优先于静态 `_authToken`，并支持 `NPM_ID_TOKEN` 环境变量（v11.0.7）
- 🎯 修复了 `--filter '!<pkg>'` 排除工作区根目录的问题（v11.0.7, v10.33.4）
- 📄 恢复了 `pnpm publish --json` 的 npm 兼容输出（v11.0.7）
- 🧩 修复了 `pnpm config get @<scope>:registry` 返回错误 URL 的问题（v11.0.7）
- 🔧 修复了 `pnpm_config_npmrc_auth_file` 等环境变量未生效的问题（v11.0.6）
- ⬆️ 改进了 `pnpm self-update` 从 v10 到 v11 的迁移路径（v11.0.6）
- ⚠️ 对全局配置文件中不允许的设置添加了警告（v11.0.6）
- 🖥️ 修复了 `pnpm dlx` 在严格构建策略下的交互式批准提示（v11.0.5）
- 🍏 为 Intel Mac 用户提供了 `@pnpm/exe` 的替代安装方案（v11.0.5）
- 🔍 修复了 `pnpm -g ls --json` 和 `--parseable` 的输出格式（v11.0.5）
- 📝 修复了 `pnpm publish` 忽略 `publishConfig.registry` 的问题（v11.0.5）
- 🚫 修复了 `pnpm self-update` 意外降级的问题（v11.0.4, v10.33.3）
- 🧹 改进了 `pnpm clean` 和 `pnpm ci` 的行为（v11.0.4）
- 🐟 修复了 Windows 上创建命令 shim 时的“打开文件过多”错误（v11.0.3）
- 🔗 修复了 `file:` 和 git 依赖的 tarball URL 被错误丢弃的问题（v11.0.3）
- 🆕 修复了 `pnpm add -g` 触发批准构建提示时的符号链接错误（v11.0.2）
- 🔄 修复了 corepack 下 `packageManagerDependencies` 过时的问题（v11.0.2）
- 📊 修复了递归发布摘要中 `publishConfig.directory` 的报告问题（v11.0.2）
- ✅ 修复了 `os`/`cpu` 否定条目被错误拒绝的问题（v11.0.2）
- 📝 修复了 `pnpm self-update` 同步 `package.json` 中的 `packageManager` 字段（v11.0.1）
- 🗑️ 拒绝工作区清单中的 `null` 命名目录（v11.0.1）
- 📋 为 git 依赖的 SBOM 输出添加了下载位置信息（v11.0.1）

---

### [pnpm 11.0 | pnpm](https://pnpm.io/blog/releases/11.0)

**原文标题**: [pnpm 11.0 | pnpm](https://pnpm.io/blog/releases/11.0)

pnpm 11.0 版本发布，带来了多项重大更新，包括安全默认值收紧、原生发布流程、SQLite 存储索引和隔离的全局安装。

- 🔒 安全默认值收紧：`minimumReleaseAge` 默认设为 1 天，`blockExoticSubdeps` 默认启用，`allowBuilds` 取代旧的构建依赖设置。
- 🚫 不再支持 Node.js 18-21，要求 Node.js 22+，且 pnpm 本身转为纯 ESM。
- 🗄️ 新的 SQLite 存储索引（store v11）：用单一数据库替代数百万 JSON 文件，减少系统调用，提升安装速度。
- 🌐 原生发布流程：`publish`、`login`、`view` 等命令不再依赖 npm CLI，改为原生实现。
- 📦 隔离的全局安装：每个 `pnpm add -g` 拥有独立目录和锁文件，避免全局包相互干扰。
- ⚙️ 配置变更：`.npmrc` 仅用于认证和注册表设置，其他配置移至 `pnpm-workspace.yaml` 或全局 `config.yaml`。
- 🛠️ 新命令：新增 `pnpm ci`、`pnpm clean`、`pnpm sbom`、`pnpm peers check`、`pnpm runtime set` 等。
- 🐛 `pnpm audit` 改用批量建议端点，CVE 过滤替换为 GHSA 过滤。
- ⚡ 性能优化：使用 `undici` 替代 `node-fetch`，预分配内存下载，NDJSON 元数据缓存等。
- 📝 其他变化：脚本输出更简洁，`pnpm init` 默认 `type` 为 `"module"`，隐藏脚本支持，`-F` 作为 `--filter` 短别名。

---

### [GitHub - extractus/article-extractor: 使用Node.js从指定URL中提取主要文章](https://github.com/extractus/article-extractor)

**原文标题**: [GitHub - extractus/article-extractor: To extract main article from given URL with Node.js · GitHub](https://github.com/extractus/article-extractor)

这是一个用于从URL中提取文章主要内容的Node.js库。

- 📦 支持多种包管理器安装：bun、npm、pnpm、yarn
- 🚀 核心API包括`extract()`和`extractFromHtml()`，可提取标题、描述、图片、作者等元数据
- ⚙️ 提供丰富的配置选项：解析参数（如阅读速度、描述长度限制）和请求参数（如代理、超时控制）
- 🔧 支持自定义转换规则：通过`addTransformations()`和`removeTransformations()`对HTML进行预处理和后处理
- 🛡️ 集成sanitize-html进行内容净化，并提供`getSanitizeHtmlOptions()`和`setSanitizeHtmlOptions()`方法
- 🌐 支持代理转发和HTTPS代理代理，适用于浏览器和Node环境
- 📄 提供测试和快速评估命令，便于开发验证
- ⭐ 获得1.9k星标，基于MIT许可证开源

---

### [GitHub - nodeca/probe-image-size: 无需完整下载即可获取图片尺寸。支持的图片类型：JPG、GIF、PNG、WebP、BMP、TIFF、SVG、PSD、ICO。](https://github.com/nodeca/probe-image-size)

**原文标题**: [GitHub - nodeca/probe-image-size: Get image size without full download. Supported image types: JPG, GIF, PNG, WebP, BMP, TIFF, SVG, PSD, ICO. · GitHub](https://github.com/nodeca/probe-image-size)

probe-image-size 是一个轻量级工具，无需完整下载即可获取图片尺寸，支持多种格式，并可通过 HTTP 或本地流高效处理大图。

- 📦 支持 JPG、GIF、PNG、WebP、BMP、TIFF、SVG、PSD、ICO、AVIF、HEIC 等多种图片格式
- ⚡ 无需完整下载，通过最小数据量获取图片尺寸，节省带宽和内存
- 🌐 支持远程 URL 和本地流（Stream）两种数据源
- 🔄 可提取 Exif 方向信息，便于处理旋转后的图片
- 🛠️ 提供异步（probe）和同步（probe.sync）两种 API，同步版适用于 Buffer 或 TypedArray
- 📐 返回结果包含宽度、高度、类型、MIME、URL 等，ICO 和 AVIF 支持多尺寸变体
- ⚠️ 对于不可信来源，返回的尺寸需额外验证安全性
- 🚫 错误时返回 ECONTENT（解析失败）或 HTTP 状态码
- 🔧 模块化设计，可单独使用 stream.js、http.js、sync.js，便于浏览器化
- 💰 通过 Tidelift 订阅支持项目开发

---

### [GitHub - fastify/fast-json-stringify: 比JSON.stringify()快2倍 · GitHub](https://github.com/fastify/fast-json-stringify)

**原文标题**: [GitHub - fastify/fast-json-stringify: 2x faster than JSON.stringify() · GitHub](https://github.com/fastify/fast-json-stringify)

fast-json-stringify 是一个基于 JSON Schema Draft 7 生成快速字符串化函数的库，在处理小数据负载时性能显著优于 JSON.stringify()，但优势随负载增大而缩小。

- ⚡ 性能优势：对小数据负载比 JSON.stringify() 快约 2 倍，但负载增大后优势减弱
- 📋 基于 Schema：需输入 JSON Schema Draft 7 来生成优化的 stringify 函数
- 🔧 丰富选项：支持 rounding、largeArrayMechanism、ajv 实例等自定义配置
- 🗓️ 特殊类型处理：Date 自动转 ISO 字符串，RegExp 转字符串，BigInt 转整数
- ❌ 必填字段验证：可设置 required 字段，缺失时抛出错误
- 🎯 模式匹配：支持 patternProperties、additionalProperties、anyOf/oneOf、if/then/else 等高级 Schema 特性
- 🔄 复用定义：通过 $ref 支持内部和外部 Schema 定义复用
- 🚀 大数组优化：提供 default 和 json-stringify 两种机制，默认 20000 元素阈值
- ⚠️ 安全警告：Schema 定义应视为应用代码，用户提供的 Schema 可能带来安全风险
- 🐛 调试与独立模式：支持 debug 模式查看生成代码，standalone 模式编译可直接运行的 Node.js 代码
- 📜 许可证：MIT 许可证，由 nearForm 赞助

---

### [自动缩放洞察：近十年应用自动缩放经验揭示的真相](https://judoscale.com/blog/autoscaling-insights-what-nearly-a-decade-of-autoscaling-your-apps-has-revealed-to-us?utm_source=node-weekly&utm_medium=referral&utm_campaign=lessons-learned&utm_content=jon-from-judoscale)

**原文标题**: [Autoscaling Insights: What Nearly A Decade Of Autoscaling Your Apps Has Revealed To Us](https://judoscale.com/blog/autoscaling-insights-what-nearly-a-decade-of-autoscaling-your-apps-has-revealed-to-us?utm_source=node-weekly&utm_medium=referral&utm_campaign=lessons-learned&utm_content=jon-from-judoscale)

## 概述总结
近十年的自动扩缩容实践揭示了八个关键洞察，涵盖硬件噪音、队列管理、成本优化和调度策略，强调通过简单、可重复的决策实现系统稳定。

- 🔊 **共享硬件存在噪音问题**：多租户机器因过度配置导致邻居突发流量影响自身延迟，需学会识别单实例异常并利用自动检测工具（如Dyno Sniper）重启受影响服务
- 🎯 **预留容量扩缩容难度大**：多数团队难以正确配置"预留头部空间"策略，导致过度配置或容量不足，建议使用基于利用率的主动扩缩容方案（如Judoscale）
- ⏱️ **健康应用的队列时间阈值低于预期**：专用硬件可低至5ms，共享硬件通过控制"Dyno Load"也能实现类似稳定性，需谨慎管理资源分配
- 💰 **工作进程缩容至零是超能力**：无任务时关闭工作进程可节省成本，冷启动时间（30-45秒）通常满足SLA要求，建议为低优先级队列启用零缩容
- 🗂️ **任务队列过多是常见问题**：超过5个队列会导致监控复杂、Redis压力大、维护困难，建议按SLA命名仅保留3个队列
- ⚖️ **Web端每次只缩容一个实例**：批量缩容可能过度削减容量导致用户体验下降，边际收益远低于风险，未来可能移除该选项
- 🔄 **理解实例内并发机制**：随机路由下单个实例需处理多请求，建议每个实例运行多个进程实现真正并行，优于部署多个单进程实例
- 📅 **调度策略简单有效**：根据流量周规律设置扩缩容范围（如工作日提高最小值），结合自动扩缩容可平衡成本与响应速度，避免突发流量时服务降级

---

### [GitHub - paradedb/paradedb: 为Postgres提供简单、Elastic品质的搜索](https://github.com/paradedb/paradedb)

**原文标题**: [GitHub - paradedb/paradedb: Simple, Elastic-quality search for Postgres · GitHub](https://github.com/paradedb/paradedb)

ParadeDB 是一个将 Elasticsearch 级别全文搜索和分析功能直接集成到 PostgreSQL 中的开源扩展。

- 🔍 **全文搜索**：支持 BM25 评分、Top K 查询、高亮显示、分词器及过滤功能
- 📊 **分析能力**：提供列式存储、聚合、分面搜索和 JOIN 操作
- 🛠️ **技术核心**：基于 Rust 开发，整合 Tantivy（搜索）和 Apache DataFusion（OLAP）库
- 🔗 **集成广泛**：兼容 Django、SQLAlchemy、Rails 等 ORM，以及 Railway、Render 等云平台
- 👥 **社区支持**：通过 Slack、GitHub Discussions 和 Issues 提供交流渠道
- 📜 **开源许可**：采用 AGPL-3.0 许可证，并提供企业版商业许可选项
- 🚀 **项目状态**：拥有 8.7k 星标、378 个复刻，已发布 231 个版本，最新为 v0.23.4

---

### [外部函数接口 - 维基百科](https://en.wikipedia.org/wiki/Foreign_function_interface)

**原文标题**: [Foreign function interface - Wikipedia](https://en.wikipedia.org/wiki/Foreign_function_interface)

本页面介绍了“外部函数接口”（FFI）的概念，即一种允许一种编程语言调用另一种语言编写的函数或服务的机制。FFI常用于调用动态链接库中的二进制代码。

- 🔗 **定义与用途**：FFI是一种机制，使程序能调用其他语言编写的函数或服务，常用于访问动态链接库。
- 🏷️ **命名来源**：术语源自Common Lisp规范，其他语言如Haskell、Rust、PHP、Python和LuaJIT也使用该术语，而Java使用JNI或JNA。
- ⚙️ **操作方式**：FFI通过匹配不同语言的语义和调用约定实现，方式包括使用兼容库、自动生成胶水代码或包装库。
- ⚠️ **复杂性因素**：垃圾回收差异、数据类型映射、跨语言继承和虚拟机环境等可能增加FFI的复杂性。
- 🛠️ **自动生成**：许多FFI可自动生成，例如通过SWIG工具，但扩展语言可能反转主客关系。
- 🌐 **跨语言调用**：FFI通常允许高级语言调用低级语言（如C/C++）的服务，但也支持反向调用。
- 🚫 **非FFI情况**：多语言运行时（如CLR）和分布式架构（如CORBA）通常不被视为FFI。
- 💡 **特殊案例**：当语言编译到相同字节码VM（如Clojure和Java）时，严格来说不视为FFI，但提供类似功能。

---

### [GitHub - node-ffi/node-ffi：Node.js外部函数接口 · GitHub](https://github.com/node-ffi/node-ffi)

**原文标题**: [GitHub - node-ffi/node-ffi: Node.js Foreign Function Interface · GitHub](https://github.com/node-ffi/node-ffi)

node-ffi 是一个 Node.js 插件，用于通过纯 JavaScript 加载和调用动态库，无需编写 C++ 代码即可创建原生库绑定，但需注意其调用开销较高且可能引发段错误。

- 📦 **核心功能**：node-ffi 允许在 Node.js 中直接调用动态库函数，例如通过 `ffi.Library` 加载 `libm` 并调用 `ceil` 函数。
- ⚠️ **使用警告**：该工具假设用户了解底层操作，错误使用可能导致解释器段错误，需具备 C 调试技能。
- 🔧 **安装方式**：通过 `npm install ffi` 安装，或使用 `node-gyp` 从源码编译，依赖平台构建工具。
- 🖥️ **支持平台**：兼容 Linux、OS X、Windows 和 Solaris，内置 libffi 无需单独安装。
- 📊 **类型系统**：函数声明中的类型基于 ref 类型系统，64 位整数因 V8 存储限制需用字符串处理。
- ⏱️ **性能开销**：FFI 调用存在显著开销，硬编码绑定比 FFI 版本快数个数量级，建议谨慎使用。
- 📜 **许可协议**：采用 MIT 许可证，详见 LICENSE 文件。

---

### [科菲](https://koffi.dev/)

**原文标题**: [Koffi](https://koffi.dev/)

Koffi 是一款快速易用的 Node.js C FFI 模块，支持多种平台和架构。

- 🚀 低开销、高性能，支持基准测试验证
- 📦 支持原始类型和聚合数据类型（结构体、定长数组），可通过引用或值传递
- 🔄 JavaScript 函数可作为 C 回调函数使用
- ✅ 经过充分测试，支持主流操作系统和架构组合（Windows、Linux、macOS、FreeBSD、OpenBSD 等）
- 💻 需要 Node.js 16 或更高版本，推荐使用 NVM 安装
- 🔧 预构建二进制文件已包含在 NPM 包中，无需 C++ 编译器即可安装
- 📂 源代码托管在 monorepo 中，便于跨项目重构和依赖管理
- 📜 采用 MIT 许可证，可自由使用和修改
- 🔄 支持 cdecl、stdcall、MS fastcall、thiscall 等调用约定（仅 cdecl 和 stdcall 可用于 C 到 JS 回调）

---

### [Node-API | Node.js v26.1.0 文档](https://nodejs.org/api/n-api.html)

**原文标题**: [Node-API | Node.js v26.1.0 Documentation](https://nodejs.org/api/n-api.html)

Node-API 是一个用于构建原生插件的 C 语言 API，它独立于底层 JavaScript 运行时（如 V8），并作为 Node.js 的一部分进行维护。该 API 在 Node.js 的各个版本之间保持应用二进制接口（ABI）稳定，旨在隔离插件免受底层 JavaScript 引擎变化的影响，并允许为一个主版本编译的模块在后续主版本上运行而无需重新编译。

- 📝 **核心概念**：Node-API 是一个用于构建原生 Node.js 插件的 C 语言 API，它提供 ABI 稳定性，确保在不同 Node.js 版本间无需重新编译即可运行。
- 🧩 **数据抽象**：所有 JavaScript 值都通过不透明类型 `napi_value` 进行抽象，API 调用返回 `napi_status` 状态码以指示成功或失败。
- 🔧 **构建工具**：开发 Node-API 原生插件需要 C/C++ 工具链，常用的构建工具包括 `node-gyp` 和 `CMake.js`，并可通过 `node-pre-gyp`、`prebuild` 或 `prebuildify` 上传预编译的二进制文件。
- 🗺️ **版本矩阵**：Node-API 有独立的版本号，从版本 9 开始，插件可能需要代码更新才能在新版本上运行，但 ABI 稳定性通过支持所有从 8 到最高版本的 API 来维持。
- 🌍 **环境生命周期**：Node-API 提供了 `napi_set_instance_data` 和 `napi_get_instance_data` 来管理与 Node.js 环境生命周期相关的全局状态。
- 🛠️ **数据类型与回调**：定义了多种基础数据类型（如 `napi_env`、`napi_value`）和回调类型（如 `napi_callback`、`napi_finalize`），用于处理 JavaScript 值和异步操作。
- ❌ **错误处理**：通过返回状态码和 JavaScript 异常进行错误处理，提供了 `napi_throw_error`、`napi_create_error` 等函数来抛出或创建错误对象。
- ⏳ **对象生命周期管理**：通过句柄作用域（`napi_open_handle_scope`/`napi_close_handle_scope`）和引用（`napi_create_reference`/`napi_delete_reference`）来管理 JavaScript 对象的生命周期。
- 🔄 **异步操作**：支持简单异步工作（`napi_create_async_work`）和自定义异步操作（`napi_async_init`/`napi_async_destroy`），以及线程安全函数调用（`napi_create_threadsafe_function`）。
- 🎭 **对象包装**：`napi_wrap` 和 `napi_unwrap` 用于将 C++ 类实例包装到 JavaScript 对象中，并支持类型标签（`napi_type_tag_object`）进行类型验证。
- 💬 **Promise 支持**：通过 `napi_create_promise`、`napi_resolve_deferred` 和 `napi_reject_deferred` 创建和操作 JavaScript Promise。
- 📦 **模块注册**：使用 `NAPI_MODULE` 或 `NAPI_MODULE_INIT` 宏注册 Node-API 模块，其 `Init` 函数返回 `exports` 对象。

---

### [lib、src、test、doc：由cjihrig添加node:ffi模块 · 拉取请求 #62072 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62072)

**原文标题**: [lib,src,test,doc: add node:ffi module by cjihrig · Pull Request #62072 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62072)

Node.js 已合并 `node:ffi` 模块，这是一个实验性的外部函数接口（FFI）支持，允许 JavaScript 直接调用原生 C 库函数。

- 🎉 **新增 `node:ffi` 模块**：为 Node.js 添加了实验性的 FFI 支持，允许 JavaScript 调用原生 C 函数。
- 🔧 **简化的 API 设计**：经过多次重构，最终采用了更简洁的 API，并移除了大量冗余代码。
- 🛡️ **权限安全模型**：引入了 `--allow-ffi` 权限标志，并在所有实例方法中加强了权限检查，防止未授权调用。
- 📦 **依赖 libffi**：集成了 `libffi` 库作为底层实现，支持多种架构（x86、ARM、RISC-V 等）。
- 🧪 **丰富的测试套件**：包含 20+ 个测试文件，覆盖函数调用、回调、内存操作、权限审计等场景。
- 🐧 **多平台支持**：修复了 Windows 和 AIX 上的构建问题，确保跨平台兼容性。
- 📚 **文档与示例**：新增了完整的 API 文档和测试用例，帮助开发者快速上手。
- 🚀 **已合并至主分支**：该 PR 已于 2026 年 4 月 14 日合并，并随 Node.js 26.1.0 版本发布。

---

### [权限 | Node.js v26.1.0 文档](https://nodejs.org/api/permissions.html)

**原文标题**: [Permissions | Node.js v26.1.0 Documentation](https://nodejs.org/api/permissions.html)

Node.js 权限模型用于控制系统资源访问，通过 `--permission` 标志启用，默认限制文件系统、网络、子进程等操作，并提供了运行时 API 和配置支持。

- 🔒 **权限模型概述**：通过 `--permission` 标志启用，默认限制文件系统、网络、子进程、Worker 线程、原生插件、WASI、FFI 和 Inspector 等资源访问。
- 📜 **运行时 API**：`process.permission.has(scope[, reference])` 用于在运行时检查权限，例如 `process.permission.has('fs.write', '/path')`。
- 📁 **文件系统权限**：使用 `--allow-fs-read` 和 `--allow-fs-write` 标志控制读写，支持通配符（如 `/home/test*`）和相对/绝对路径。
- ⚙️ **配置支持**：可通过 `node.config.json` 文件（实验性）声明权限，如 `"permission": { "allow-fs-read": ["./foo"] }`。
- 🚀 **npx 使用**：通过 `--node-options="--permission"` 启用，需额外授予全局 `node_modules` 或 npm 缓存目录的读取权限。
- ⚠️ **约束与限制**：权限模型不继承到 Worker 线程；某些标志（如 `--env-file`）在环境初始化前读取，不受限制；符号链接可能绕过路径限制。
- 🔍 **跨进程 Inspector**：`process._debugProcess(pid)` 可强制其他 Node.js 进程打开 Inspector，不受权限模型限制，需通过 OS 级隔离防范。
- 🛑 **已知问题**：符号链接可被跟随到未授权路径，需确保授权路径不含相对符号链接。

---

### [ffi: 通过bengl添加V8快速调用路径 · 拉取请求 #63140 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63140)

**原文标题**: [ffi: add V8 fast-call path by bengl · Pull Request #63140 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63140)

Node.js FFI 新增 V8 快速调用路径，性能大幅提升。

- 🚀 新增 V8 快速调用路径：为符合条件的原生调用提供并行调度路径，替代 libffi，性能提升最高达 5098%。
- 🛠️ 动态生成 JIT 跳板：在 DynamicLibrary.getFunction 时，为每个函数生成 JIT 跳板，剥离 V8 接收者参数并尾调用目标函数。
- ⚙️ 自动回退机制：含回调、不支持参数类型或参数过多的签名，自动回退到 libffi。
- 💻 多平台支持：支持 Linux/macOS/FreeBSD 的 x86_64 和 AArch64、Windows 的 x86_64 和 AArch64、Linux 的 AArch32。
- 🔐 内存安全：JIT 内存通过 mmap 分配，macOS 使用 MAP_JIT，其他平台执行 W^X 策略。
- 🧪 实验性功能：通过 `--experimental-ffi` 启用，可在构建时通过 `--without-ffi-fastcall` 禁用。
- 🎯 极致优化：通过 V8 补丁实现无接收者模式，消除 JIT 跳板，进一步减少调用开销。
- 📊 基准测试：多个测试场景性能提升显著，如 many-args 提升 5098%，add-i32 提升 2696%，getpid 提升 1353%。
- 🏆 社区反馈：获得开发者积极评价，被认为接近性能极限，有望超越现有用户态 FFI 实现。

---

### [发布 raylib v6.0 · raysan5/raylib · GitHub](https://github.com/raysan5/raylib/releases/tag/6.0)

**原文标题**: [Release raylib v6.0 · raysan5/raylib · GitHub](https://github.com/raysan5/raylib/releases/tag/6.0)

raylib 6.0 版本发布，这是迄今为止最大的一次更新，带来了众多新功能和改进，包括全新的软件渲染器、平台后端、文件系统和文本管理API等。

- 🎉 **全新软件渲染器 (rlsw)**：无需GPU即可在CPU上运行raylib，支持多种平台后端，包括ESP32微控制器。
- 🖥️ **新增内存平台后端 (rcore_memory)**：支持无头渲染到内存帧缓冲区，可直接导出图像。
- 🪟 **新增Win32平台后端 (rcore_desktop_win32)**：直接实现Win32 API，支持OpenGL和GDI窗口，为未来替代现有平台库奠定基础。
- 🌐 **新增Emscripten平台后端 (rcore_web_emscripten)**：摆脱libglfw.js依赖，直接实现Emscripten/JS功能，支持软件渲染和WebGL。
- 🔄 **重新设计全屏和高DPI缩放**：优先采用无边框全屏模式，自动检测并缩放内容，支持多显示器。
- 🦴 **重新设计骨骼动画系统**：支持动画混合和过渡，简化API并优化GPU蒙皮性能。
- ⚙️ **重新设计构建配置系统 (config.h)**：支持通过命令行轻松禁用功能，简化构建流程。
- 📁 **新增文件系统API**：包含40多个文件管理函数，统一管理文件读写、目录操作等。
- ✏️ **新增文本管理API**：包含30多个文本处理函数，如替换、分割、大小写转换等。
- 🛠️ **新增示例管理器 (rexm)**：简化示例的添加、删除、重命名和自动测试。
- 📚 **新增70+示例**：社区贡献了大量新示例，并统一了示例结构和头部信息。
- 💖 **感谢贡献者和赞助商**：感谢850+贡献者和NLnet、puffer.ai等赞助商的支持。

---

