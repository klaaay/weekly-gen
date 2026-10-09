### [获取失败](https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002)

**原文标题**: [Failed to retrieve](https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002)

无法总结：获取内容失败，状态码 403。

---

### [Watt 快速入门 | Platformatic 开源软件](https://docs.platformatic.dev/docs/getting-started/quick-start)

**原文标题**: [Watt Quick Start | Platformatic Open Source Software](https://docs.platformatic.dev/docs/getting-started/quick-start)

Platformatic Watt 3.72.0 快速入门介绍如何用 Node.js 应用服务器组合并运行多应用：使用 Next.js 作为前端、node:http 创建现有 Node.js 应用，并通过 Platformatic Gateway 统一协调和暴露；同时涵盖创建项目、开发运行、生产构建和调试流程。

- 🚀 Watt 是 Node.js 应用服务器，可组合运行多个应用和框架，支持 Next.js、Astro、Remix、Vite、NestJS 等，并提供 AI 编码代理官方技能。
- ✅ 前置条件：Node.js v22.19.0+、npm 和代码编辑器。
- 🛠️ 使用 `npx wattpm create` 初始化项目；选择 `@platformatic/node`、npm、应用名 `node`、端口 `3042`、不使用 TypeScript，项目位于 `web/node`。
- 📄 自动生成 `watt.json` 和 `package.json`，并加入 `@platformatic/node` 依赖。
- 🧩 默认 Node 示例使用 `node:http` 和 `@platformatic/globals` 的 `getLogger()`，导出 `create()` 创建服务器，由 Watt 在独立 worker 线程中运行；也可使用 Express、Fastify、Koa 等。
- ▶️ 根目录 `npm start` 运行 `wattpm start`；`npm run dev` 运行 `wattpm dev` 启用监听模式；可用 `curl http://localhost:3042` 测试。
- 🌐 再次运行 `npx wattpm create` 可添加 `@platformatic/gateway`，命名为 `gateway`；默认将 `node` 应用代理到 `/node`，可访问 `http://localhost:3042/node`，并通过 `web/gateway/watt.json` 自定义暴露方式。
- ⚛️ 使用 `npx create-next-app web/next` 添加 Next.js 前端。
- ⚠️ npm workspaces 下需将 `web/next/package.json` 的 `name` 改为非 `next`（如 `frontend`），避免遮蔽 Next.js 包；并在 `next.config.mjs` 设置 `turbopack.root` 为 Watt 项目根目录，解决 Turbopack 工作区根目录解析问题。
- 📦 运行 `npx wattpm-utils import` 导入 Next.js 应用并安装 `@platformatic/next`；在 `web/next/watt.json` 设置 `basePath` 为 `/next`，然后 `npm run dev` 后访问 `http://localhost:3042/next`。
- 🔄 Next.js 可通过内部域名 `http://node.plt.local` 调用 Node 应用数据；该域名仅在 Watt/Platformatic 环境内可用，示例用 `cache: 'no-store'` 关闭 Next.js fetch 缓存。
- 🏗️ 生产构建运行 `npm run build`（即 `wattpm build`），生产启动运行 `npm run start`（即 `wattpm start`）。
- 🐞 调试：`npm run start -- --inspect` 后可用 Chrome DevTools 的 `chrome://inspect`；VS Code 可开启 `Debug: Toggle Auto Attach > Always`，再用 `npm run dev` 并触发断点。
- ✏️ 若自定义路径，需同步修改 `web/next/watt.json` 的 `basePath` 和 `web/gateway/watt.json` 的 `prefix`。

---

### [SerpApi：Google 搜索 API](https://serpapi.com/?utm_source=cooperpress-newsletter)

**原文标题**: [SerpApi: Google Search API](https://serpapi.com/?utm_source=cooperpress-newsletter)

请提供需要总结的文本内容，目前未收到可摘要的文章。
- 📭 当前输入中“Use the following content:”后为空，无法提取关键信息。
- ✍️ 请粘贴文章或段落，我将据此生成中文要点摘要。
- 🧾 收到内容后，我会按“概述 + emoji 要点列表”的格式输出。

---

### [Node.js — Node.js 26.11.0（当前版本）](https://nodejs.org/en/blog/release/v26.11.0)

**原文标题**: [Node.js — Node.js 26.11.0 (Current)](https://nodejs.org/en/blog/release/v26.11.0)

Node.js 26.11.0（Current）于 2026-10-07 发布，由 @aduh95（Antoine du Hamel）维护，属于当前版本线。本次更新包含多项 SEMVER-MINOR 新特性、性能优化、稳定性修复、依赖升级，并提供各平台安装包、源码及 SHA256/PGP 校验信息。

- 🚀 版本信息：Node.js 26.11.0（Current）发布，日期为 2026-10-07，发布者 @aduh95。
- 🧩 buffer 更新：新增 `isLatin1` 与 `Buffer.stringLength()`，并修复大缓冲区负索引、UTF-16LE `indexOf` 起点等问题。
- 🌐 HTTP/HTTP2：新增 `isValidHeaderName()` / `isValidHeaderValue()`，HTTP/2 新增 `connectionWindowSize` 选项；同时优化响应对象、解析器回调和请求分配。
- 📊 perf_hooks：修复 `monitorEventLoopDelay()` 分辨率截断，允许 `RecordableHistogram` 记录 0，新增 `histogram.diff()` / `snapshot()`，增强 CBOR 导入校验和内存报告。
- ⚙️ 进程与运行时：`process.ref` / `unref` 转为稳定；新增 `--process-timeout=N`；堆分析输出增加 size/count；嵌入方可豁免链接绑定的 addon 权限。
- 🗄️ SQLite：重命名 `DatabaseSync` / `StatementSync`，新增虚拟表 `createModule()`，修复重开连接状态、过大字符串、虚拟表参数等问题。
- 🔐 加密与 TLS：大量 WebCrypto 健壮性修复，涉及 AES-GCM/KW、KMAC、Argon2、PBKDF2、RSA/EC/JWK 等；根证书升级至 NSS 3.129，TLS 修复会话/SNI 与 CN 名称约束。
- 🧵 stream/worker：优化 webstreams 快速路径、背压与取消；worker 终止时丢弃/序列化消息，修复 `postMessage` 重载、`BroadcastChannel` 标签等。
- 📦 依赖升级：V8、OpenSSL 3.5.9、npm 11.20.0、undici 8.11.2、zlib、LIEF 1.0.0、时区 2026e、histogram 0.12.0 等。
- 🧰 FFI/FS/网络修复：FFI 增加安全整数、指针范围、释放后使用等校验；fs 修复 `cpSync` 时间戳、`mkdir` ENOENT 重试、fd 0 关闭等；net 加速 BlockList 与 IPv6 检查。
- 🧪 测试与工具：大量测试去 flake、WPT 更新、CI/基准构建配置共享、lint/format 工具改进及依赖 bump。
- 📚 文档与模块：Alpine Linux 提升为 tier 2 支持；文档修复和补充；模块缓存键、包映射路径、内置暴露策略优化。
- 📥 下载与校验：提供 Windows x64/ARM64、macOS Intel/Apple Silicon、Linux x64/ARM64/PPC LE/s390x、AIX 安装包或二进制；源码 tar.gz/xz；附 SHA256 与 PGP 签名。
- 🔗 相关版本：页面显示上一版为 Node.js 26.11.1（Current），下一版为 Node.js 22.23.3（LTS）。

---

### [](https://github.com/nodejs/node/pull/66138)

**原文标题**: [src: add --process-timeout=N by jasnell · Pull Request #66138 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/66138)

Node.js 核心仓库合并了 PR #66138，新增 `--process-timeout=N` 命令行选项，为进程提供跨平台一致且可诊断的超时机制，并已包含在 v26.11.0 版本中。

- ✨ 新增 `--process-timeout=N` 选项，可为 Node.js 进程设置统一超时。
- ⚠️ 现有方案有缺陷：OS/CI 超时不一致且无诊断，`setTimeout` 在事件循环忙时失效，信号诊断同样受限。
- 🛠️ 实现方式：原生看门狗线程中断主线程，即使代码运行中也能打印 JS 堆栈和事件循环资源，可选完整诊断报告，退出码 124。
- 📝 示例：`node --process-timeout=10s -e "while(true) {}"` 会输出超时信息和调用栈，而标准 `timeout` 命令无诊断输出。
- 🔍 即使主线程卡在原生代码中，进程仍会退出，并给出明确超时原因。
- 🧪 测试风险：2 秒宽限期固定、微小时间窗口、Windows pid 重用、慢机器可能导致测试不稳定。
- ✅ 已获 mcollina 和 trivikr 批准，合并提交 823d229，标签 semver-minor 和 notable-change。
- 📦 该功能作为 semver-minor 变更包含在 Node.js v26.11.0 (Current) 发布中。

---

### [](https://github.com/nodejs/node/pull/65787)

**原文标题**: [sqlite: add virtual table support via createModule() by TrevorBurnham · Pull Request #65787 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65787)

overview summary
Node.js 的 SQLite 模块新增 `database.createModule(name, options)`，通过封装 `sqlite3_create_module_v2()` 暴露虚拟表 API，让 JavaScript 数据源可提供只读虚拟表；PR #65787 已合并到 `nodejs:main`，提交为 `dd9f4da`，后续进入 Node.js 26.11.0。

- 🧩 核心能力：注册模块可用于同名表（`SELECT * FROM module_name`）或命名虚拟表（`CREATE VIRTUAL TABLE t USING module_name`）。
- 🔌 参数传递：隐藏列通过表值函数语法传参，如 `SELECT * FROM module_name(param1, param2)`。
- ⚙️ 配置项：`options` 支持 `columns`、`rows`、`directOnly`、`useBigIntArguments`。
- 🛡️ 类型校验：列类型仅允许 `INTEGER`、`TEXT`、`REAL`、`BLOB`、`ANY`，构建 `sqlite3_declare_vtab()` schema 时会引用列名。
- ⚠️ 亲和性说明：虚拟表不对 `xColumn` 返回值应用列亲和性；`number` 按 `REAL`、`bigint` 按 `INTEGER` 存储，即使列声明为 `INTEGER`。
- 🧪 关键修复：`xColumn` 返回隐藏列被约束的值而非 NULL；`xBestIndex` 随约束消耗降低 `estimatedCost`；迭代协议违规返回 SQLite 错误。
- 🧯 稳定性修复：用 `idxStr` 传递隐藏列索引，避免 int 位掩码别名；`xFilter/xNext/xColumn` 使用 `CallbackDepthGuard`，防止内部 `close()` 导致进程崩溃。
- 🧹 清理语义：`xClose` 调用迭代器 `return()` 以运行 generator `finally`，但在 GC 拆卸或已有错误挂起时跳过。
- 🔐 生命周期：`VirtualTableModule` 使用 `BaseObjectWeakPtr<DatabaseSync>`；`createModule()` 拒绝在 authorizer 回调中调用，并重新检查数据库是否仍打开。
- 🐞 审查修正：处理选项 getter 重入 `close()` 的空指针风险；`xClose` 不再错误调用 `PropagateJSError`，并固定清理抛错时的错误优先级。
- 📈 质量与合并：Patch 覆盖率约 81.97%，项目覆盖率 90.17%；获 trivikr 与 jasnell 批准，CI 81/82 通过后于 2026-09-22 合并。
- 🔗 关联：延续 #61544，修复 #61539，参考 #63826；后续在 2026-10-07 的 Node.js 26.11.0 中被提及。

---

### [](https://github.com/nodejs/node/pull/66064)

**原文标题**: [buffer: add Buffer.stringLength() by mcollina · Pull Request #66064 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/66064)

该 PR 由 Matteo Collina 提交并已合并到 Node.js main，新增 `Buffer.stringLength(input[, encoding])`，作为 `Buffer.byteLength()` 的对应方法，用于在不解码的情况下预估字符串长度，并帮助流式输入场景提前进行内存预算与限制检查。

- 🧩 新增 `Buffer.stringLength(input[, encoding])`，返回 `buf.toString(encoding)` 将产生的 UTF-16 代码单元数量，且无需实际解码。
- ⚙️ UTF-8 编码使用 simdutf 计算；无效输入按解码器同样的最大子部分替换规则计数，因此结果始终与 `toString().length` 匹配。
- 📐 其他编码仅基于 `byteLength` 进行计算。
- 🎯 主要用途是让累积流式输入的代码在解码前，对照 `buffer.constants.MAX_STRING_LENGTH` 检查结果并规划内存预算，关联 issue #66062。
- 🚀 x64 基准测试中，UTF-8 下 4 KiB ascii 约 3.5M ops/s、约 17 GB/s；1 MiB 有效多字节输入约 7.5 GB/s，末尾无效输入也约 7.5 GB/s。
- 🛠️ 最初命名为 `buffer.stringLength()`，经反馈后改为静态方法 `Buffer.stringLength()`，并同步更新文档、测试和基准。
- ✅ 已获 ShogunPanda、gurgunday 批准，CI 检查通过，并于 2026-09-19 合并到 `nodejs:main`，提交为 `22ab7d7`。
- 🏷️ 该功能被标记为 `semver-minor`，并已出现在 Node.js 26.11.0 的发布说明中。

---

### [](https://voidzero.dev/posts/announcing-vite-plus-1-0)

**原文标题**: [Announcing Vite+ 1.0 | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-1-0)

overview summary
Vite+ 1.0 正式发布：这是由 Vite、Vitest、Rolldown、Oxc 团队打造的统一 Web 开发工具链，以单命令 `vp` 整合 Node.js 运行时、包管理器与前端工具。它 MIT 开源、框架无关，不替代 Vite，也不要求项目使用 Vite；用一个 `vite.config.ts` 和九条命令覆盖创建、安装、开发、检查、测试、构建、打包、任务运行与环境管理，目标是减少工具链维护、加快本地反馈和 CI。Beta 后还增强了迁移、CI、Docker/Homebrew、Git hooks 等能力，已有近 200 万周下载和 2600+ 公共仓库采用。

- 🚀 Vite+ 1.0 已发布，稳定、MIT 许可，接近每周 200 万下载。
- 🧰 单命令 `vp` 管理 Node.js 运行时、包管理器和前端工具链；安装方式为 `curl -fsSL https://vite.plus | bash`。
- 🏗️ 提供 `vp create` 新建项目，`vp migrate` 迁移现有项目。
- 🧩 由 Vite、Vitest、Rolldown、Oxc 团队打造，但不是框架、不是包管理器，也不替代 Vite。
- 🌐 免费开源、框架无关，React、Vue、Node CLI、400 包 monorepo 都可使用，项目甚至不必使用 Vite。
- 📦 解决自组工具链痛点：运行时、包管理器、开发服务器、linter、formatter、测试器、打包器各自配置与升级容易漂移。
- ⚙️ 九条命令覆盖开发周期：`vp create/install/dev/check/test/build/pack/run/env`。
- 🛠️ 单个根目录 `vite.config.ts` 配置全部工具；无参数运行 `vp` 会进入交互提示。
- 🔄 单一 `vite-plus` 依赖可替代 `vite`、`vitest`、`eslint`、`prettier`、`tsup`、`turbo` 等及插件配置，升级只需一次版本提升。
- 🧭 各仓库内置 `vp` 命令含义一致，项目自定义脚本可通过 `vpr <script>` 运行，便于新同事和 agents 上手。
- ⚡ Rust 工具带来加速：Oxlint 比 ESLint 快 50 至 100 倍，Oxfmt 比 Prettier 快至多 30 倍，Vite 8 因 Rolldown 构建更快。
- ✅ CI 更快：`vp run` 记录文件、参数、环境变量，未变化任务可即时缓存重放；`setup-vp` 合并 Node 设置、包管理器设置和依赖缓存步骤。
- 🔓 无锁定：可继续使用喜欢的 Vite 插件和包管理器，`vp run` 也能缓存任意脚本。
- 🆕 Beta 后新增：GitLab CI/CD 的 `setup-vp`、`tsup` 迁移、Homebrew 与 Docker 镜像、`vp toolchain`、`vp env doctor`、`vp hooks`、`vp staged` 及生态兼容增强。
- 📈 底层工具升级：Vitest 5 稳定、Vite 8.1 实验性 Bundled Dev Mode、Oxc 原生 React Compiler 支持，比 Babel 插件快 10 倍。
- 👥 使用者包括 Tiptap、Dify、vinext、BlockNote、Inkline、npmx、hono 等；2600+ 公共仓库依赖 `vite-plus`。
- 🚦 上手方式：macOS/Linux 用 curl，Windows 用 PowerShell；随后 `vp create` 或 `vp migrate`，迁移会先展示计划，生产项目应先读迁移指南。
- 🗺️ 后续计划包括远程缓存、更深入的 monorepo 诊断、`vp release`、`vp docs` 等。
- 🙏 项目由国际核心团队与社区共同建设，感谢 alpha/beta 测试者、问题报告者和贡献者。

---

### [Node.js —](https://nodejs.org/en/download)

**原文标题**: [Node.js — Download Node.js®](https://nodejs.org/en/download)

Node.js 官方下载页面，提供各版本 Node.js 的下载选项、版本状态说明及相关资源链接。

- 📦 页面提供 Node.js 多个版本的下载，当前 LTS 版本为 v24.21.0，Current 版本为 v26.11.1
- ⚠️ 大量旧版本（从 v0.12.18 到 v25.9.0）已标记为 EOL（生命周期结束），不再维护
- 🖥️ 页面需要 JavaScript 才能正常使用，若禁用可访问下载归档页面直接下载
- 🚀 官方建议希望更快获得新功能的用户使用最新 Node.js 版本
- 📥 提供预构建的 Node.js 二进制文件下载，包括独立二进制（.gz）和安装程序（.gz）等形式
- 🔗 可查看版本更新日志、博客文章以及 Node.js 发布计划与 LTS 状态说明
- 🔐 提供验证签名 SHASUMS 的方法，以及签名源码 tarball 下载
- 🌙 可获取每日构建（nightly）二进制、历史版本及非官方第三方平台二进制
- 🤝 下载服务与基础设施由合作伙伴支持维护

---

### [模块：同步加载大多数 ES 模块 · nodejs/node@c89ec29 · GitHub](https://github.com/nodejs/node/commit/c89ec290f0f82f544e39e6e5f2eab3b6de2c1cca)

**原文标题**: [module: synchronously load most ES modules · nodejs/node@c89ec29 · GitHub](https://github.com/nodejs/node/commit/c89ec290f0f82f544e39e6e5f2eab3b6de2c1cca)

本次提交（c89ec29，作者 Geoffrey Booth）改进了 Node.js 的 ES 模块加载机制，使入口模块在大多数情况下可以同步加载、链接和求值。核心思路是默认在主线程使用 `ModuleJobSync`，只有当模块图包含顶层 await 时才回退到异步求值路径。该改动新增了针对大型 ESM 依赖图启动性能的基准测试，并调整了加载器的解析与构造逻辑，从而在启动阶段避免创建不必要的 Promise，提升性能。

- 🚀 **同步化入口加载**：新增 `importForEntryPoint()` 方法，入口点模块的依赖图始终同步加载和链接；若图中不含顶层 await，则连求值也同步完成，整个过程不产生任何 Promise。
- 🔄 **顶层 await 回退机制**：当模块图包含顶层 await 时，方法会返回已构建的 `ModuleJob`，让调用方沿用异步入口流程求值，避免重新解析和链接同一模块。
- 🧩 **新增私有符号**：通过 `internalBinding('util')` 引入 `entry_point_module_private_symbol`，将已同步求值的入口模块挂载到 `globalThis` 上。
- ⚙️ **加载器构造逻辑调整**：`getOrCreateModuleJob` 中默认选用 `ModuleJobSync`，仅当处于异步加载钩子 worker 或 `kRequireInImportedCJS` 场景时才使用 `ModuleJob`。
- 🪄 **统一同步解析**：主线程上始终使用 `resolveSync` 进行解析，并会与异步加载钩子 worker 协调；只有钩子 worker 内部才走异步解析路径。
- 📊 **新增性能基准测试**：添加 `benchmark/esm/startup-esm-graph.js`，构建分支因子为 10 的模块树（250/500/1000/2000 个模块），测量 ESM 依赖图启动加载性能。
- 📁 **影响范围**：共修改 9 个文件，新增 373 行、删除 84 行，涉及 loader、module_job、run_main 及相关测试用例。
- ✅ **审查通过**：由 Matteo Collina、Jacob Smith、Filip Skokan、Marco Ippolito、Joyee Cheung、Gürgün Dayıoğlu 等多位维护者审核。

---

### [错误](https://github.com/nodejs/node/pull/62530)

**原文标题**: [Error](https://github.com/nodejs/node/pull/62530)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /nodejs/node/pull/62530 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [](https://github.com/nodejs/node/pull/66537)

**原文标题**: [deps: update V8 to 15.5 by joyeecheung · Pull Request #66537 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/66537)

Node.js PR #66537 由 Joyee Cheung 发起并最终合并，核心是将内置 V8 引擎更新到 15.5.35.20；该 PR 包含 20 多个提交，涉及依赖升级、ABI 调整、多平台兼容修复与构建系统适配，属于 semver-major 的 V8 引擎变更。

- ⬆️ 核心升级：将 Node.js 的 V8 更新至 15.5.35.20，并同步更新相关 Rust crates。
- 🔧 ABI 变更：更新 NODE_MODULE_VERSION 为 152，并将嵌入器字符串重置为 `-node.0`；V8 主版本升级通常带来 API/ABI 不兼容。
- 🍒 补丁合入：cherry-pick 多项 V8 修复，覆盖 MSVC STL、Solaris、illumos、Windows、GCC 与旧版 ClangCL 等问题。
- 🧵 栈追踪修复：修复 `Error.stackTraceLimit` 在超大值下的整数溢出，避免 `error.stack` 静默丢失帧。
- 🌍 平台兼容：适配 illumos 指针范围、`madvise(3C)` 签名变化、Solaris 线程栈保留限制等。
- 🧩 构建与源码调整：迁移 `GetPrototypeV2()` 到 `GetPrototype()`，迁移到 cppgc-owned `v8::MicrotaskQueue`，禁用 `V8_USE_METAGEN_INSTANCE_TYPES`。
- 🧪 CI 与审查：PR 经过完整 CI，带有 `build`、`dependencies`、`semver-major`、`v8 engine`、`commit-queue-rebase` 等标签，并获得多位审查者批准。
- 📝 发布说明提示：讨论中提到“外部分配现在默认参与 V8 的全局分配限制”，可能需要在发布说明中说明。
- ✅ 最终状态：该 PR 已关闭/合并，后续还引出 QUIC CI 与替换 `SetPrototypeV2` 调用等相关工作。

---

### [优化具有 null 原型的对象](https://adventures.nodeland.dev/archive/optimizing-objects-with-null-prototypes/)

**原文标题**: [Optimizing objects with null prototypes](https://adventures.nodeland.dev/archive/optimizing-objects-with-null-prototypes/)

文章揭示 V8 中 `{ __proto__: null }` 会让对象进入并长期停留在字典模式，拖慢热路径；Node WebStreams 通过改用类实例或 `Object.setPrototypeOf`，把吞吐量提升了一倍以上，并强调只需优化高频路径上的空原型对象。

- 🐌 `{ __proto__: null }` 和 `Object.create(null)` 在 V8 中创建后即进入字典模式，属性存于哈希表而非隐藏类。
- ⏱️ 空原型字面量创建成本约 500–1500 ns，普通字面量约 30 ns；后续属性访问始终是字典查找，读取再多也不会变快。
- 🧪 唯一例外：空原型对象若被用作其他对象的原型，V8 会将其优化为快速模式；已在 Node `main` 与 v24.18.0 验证。
- 📊 表格结论：`__proto__: null` 字面量和 `Object.create(null)` 为 DICT；`Object.setPrototypeOf({...}, null)`、空原型的类实例、普通字面量、`Object.freeze` 均为 FAST。
- ✅ 三种快速替代方案：空原型作为类原型、对普通字面量调用 `Object.setPrototypeOf(..., null)`、只读取自有属性的普通字面量。
- 🚀 Node WebStreams 第 16 轮：四个每流状态记录改为类实例后，pipe-to 吞吐约 +105–112%，WritableStream 创建 +204%，ReadableStream +138%，TransformStream +134%。
- 🔧 第 19 轮：`kNilRequest` 和 `kNilPendingAbortRequest` 哨兵改为普通字面量后再置空原型，pipe-to +12.3–14.9%，带转换 pipe-through +6.8%，writer 写入 +6.5–17.6%。
- 🔍 实时 `WritableStream` 中这些哨兵在 `main` 为 DICT，打补丁后变为 FAST。
- 🎯 核心结论：只有热路径上创建或读取的空原型对象才值得优化，包括长期共享常量；一次性使用的描述符无需改动。
- 🧰 可用 `node --allow-natives-syntax nullproto.js` 复现完整表格，并用脚本检查 WritableStream 哨兵的属性模式。

---

### [我测试了11个HTTP弹性库](https://blog.gaborkoos.com/posts/2026-10-04-I-Tested-11-Http-Resilience-Libraries/)

**原文标题**: [I Tested 11 HTTP Resilience Libraries](https://blog.gaborkoos.com/posts/2026-10-04-I-Tested-11-Http-Resilience-Libraries/)

overview summary
- 🧪 作者为开发 ffetch 而构建 21 个 HTTP 韧性测试场景，对比 11 个固定版本的库，代码和报告开源。
- 🎯 核心发现：基础重试和超时大多可靠，但组合重试、超时、熔断、舱壁、对冲、去重后，取消、截止时间和状态竞态会暴露大量问题。
- 📊 共 147 个已实现测试单元格，25 个失败；11 个库全通过的只有 5 个场景，集中在基础重试、真实 HTTP 重试和请求体重放。
- 🧰 方法：脚本化 fetch 加 Vitest 假计时器，固定随机抖动；两个原生 fetch + node:http 集成；每个库用薄适配器保留各自结果和错误。
- 🧩 参与库：ffetch、ky、fetch-retry、ofetch、wretch、resilient-fetch-client、fetch-smartly、@resili/fetch、fetch-resilience、flowshield、ts-retry-circuit。
- ✅ 全通过场景：重试恢复、重试耗尽、零重试、真实 HTTP 重试、重试加请求体重放；单策略隔离场景也大多稳定。
- ❌ 失败聚类：当策略正在等待时发生取消、超时、队列离开、迟到成功或探测完成等“第二事件”，库容易出错。
- ⏳ 重试加退避中取消：6 个库结算过晚，5 个取消后仍派发；fetch-retry 和 fetch-resilience 甚至继续耗尽重试预算。
- 🚧 舱壁加排队取消：有队列的 5 个库中 4 个失败，取消的等待者不释放容量，替换请求被拒；ffetch 是唯一通过。
- ⏰ 重试加总超时：wretch、resilient-fetch-client、fetch-resilience、flowshield 在截止后仍派发；多数库只有单次尝试超时。
- 📅 Retry-After 加取消：resilient-fetch-client 的等待不可中断，@resili/fetch 不按头部控制时序；6 个库完全不读该头部。
- 🪝 重试加抛错钩子：8 个库通过，wretch 因回调拒绝导致调用者 Promise 永不结算。
- 🦔 对冲最不完整：84 个 N/A 中 32 个来自对冲；仅 ffetch、@resili/fetch、flowshield 支持可配置延迟，flowshield 在期限场景失败。
- 🔁 去重加重试：@resili/fetch 共享了重试序列但把同一响应体给所有调用者，导致 3/4 调用者拿到不可用结果。
- ⚡ 熔断加半开并发：ffetch 迟到成功污染新冷却状态；fetch-smartly、ts-retry-circuit 更严重，会提前放行并消耗恢复响应。
- 🧯 熔断加本地取消：resilient-fetch-client、fetch-resilience、@resili/fetch 在退避取消结算或派发上失败；熔断健康计数整体尚可。
- ⚖️ 作者承认确认偏差：场景源于 ffetch 修复过的 bug，规则偏严，部分库即使符合文档也可能判失败；每格可查配置与预期。
- 🚫 范围限制：不做基准、吞吐、API、文档或维护者响应评估；只测 11 个固定发布版在 21 场景下的行为。
- 🛠️ 保持更新：Dependabot 固定版本，每周重建页面；npm test && npm run report 可本地复现，报告在 fetchkit.org/http-resilience。
- 🧭 未覆盖：流式请求体中途失败重试、缓存校验加重试、POST 对冲、去重组内超时、跨进程熔断状态、限流等。
- 💡 结论：基础重试已是商品化能力，但组合策略才是风险所在；应针对应用实际用法测试，文档有功能不等于契约正确。

---

### [](https://github.com/fetch-kit/ffetch)

**原文标题**: [GitHub - fetch-kit/ffetch: TypeScript-first fetch wrapper with configurable timeouts, retries, and circuit-breaker baked in. · GitHub](https://github.com/fetch-kit/ffetch)

@fetchkit/ffetch 是 fetch-kit 生态中面向生产环境的 TypeScript 优先 fetch 封装库/原生 fetch 替代品，保留 fetch 用法并内置超时、重试、断路器，同时通过可选插件提供更多弹性能力。

- 🧩 可包装任意 fetch 兼容实现：原生 fetch、node-fetch、undici、框架 fetch，适用于 SSR、边缘、Node.js、浏览器、Cloudflare Workers、React Native 等环境。
- ⏱️ 核心功能包括可配置超时、指数退避 + 抖动重试、Abort 感知重试，并支持全局或按请求覆盖配置。
- 🔌 采用树摇插件架构，核心约 3KB minified，零运行时依赖，提供 ESM/CJS 双格式。
- 🛡️ 可选预置插件：去重、bulkhead 并发限制、断路器、请求对冲、上下文 ID、请求/响应快捷方法、下载进度。
- 🚨 内置错误类：TimeoutError、RetryLimitError、CircuitOpenError、BulkheadFullError、HttpError、NetworkError、AbortError。
- ⚙️ 支持 `throwOnHttpError`，可在 HTTP 错误响应时抛出 HttpError，使错误处理更明确。
- 🧭 提供生命周期 hooks，可用于日志、认证、指标、请求/响应转换，并可实时查看 pendingRequests。
- 🚀 基本用法是 `createClient({ timeout, retries, plugins })`，插件从 `@fetchkit/ffetch/plugins/*` 导入。
- 🧪 生产配置可组合 dedupePlugin、circuitPlugin、contextIdPlugin、requestShortcutsPlugin、responseShortcutsPlugin 等。
- 🌐 支持自定义 `fetchHandler`，可传入 node-fetch、undici、框架作用域 fetch 或 polyfill，且所有功能行为一致。
- 🧷 推荐环境支持 `AbortSignal.any`：Node.js 20.6+、Chrome/Firefox/Edge 117+、Safari 17+；旧环境需安装 polyfill。
- ⚠️ 去重默认关闭；流、FormData、Blob 请求体不参与去重，非幂等请求需谨慎使用；可配置 TTL 与清理间隔。
- 📊 相比原生 fetch、Axios、ky，ffetch 强调智能重试、插件管道、断路器、去重、bulkhead、hedging、请求监控、强类型和自定义 fetch 支持。
- 🔐 安全实践包括 OpenSSF Scorecard、固定 GitHub Actions、CodeQL、Dependabot、OIDC provenance、SBOM、安全策略与分支保护。
- 📄 文档覆盖 API、插件架构、错误处理、高级功能、生产运维、hooks、示例和兼容性；项目采用 MIT 许可证，欢迎贡献并加入 Discord 社区。

---

### [](https://github.com/sindresorhus/ky)

**原文标题**: [GitHub - sindresorhus/ky: 🌳 Tiny & elegant JavaScript HTTP client based on the Fetch API · GitHub](https://github.com/sindresorhus/ky)

Ky 是一个基于 Fetch API 的轻量、优雅 JavaScript HTTP 客户端，目标平台包括现代浏览器、Node.js、Bun 和 Deno；它无依赖，仓库约 17.1k stars、500 forks、64 watchers，并在 fetch 之上提供更简洁的 API、错误处理、重试、超时、进度、hooks、Schema 校验和 TypeScript 支持。

- 🌳 项目定位：`ky` 是 tiny & elegant 的 Fetch API 封装，适合现代 JavaScript 运行时。
- 📦 安装与导入：`npm install ky`；Deno/浏览器可用 CDN，如 `https://esm.sh/ky`。
- 🚀 相比原生 fetch：提供方法快捷、非 2xx 抛错、自动重试、`json` 选项、超时、上传/下载进度、`baseUrl`、自定义实例、hooks、Schema 校验和 TS 泛型。
- 🧩 基本用法：`await ky.post(url, {json: {foo: true}}).json()`；返回带 `.json()`、`.text()`、`.formData()`、`.arrayBuffer()`、`.blob()`、`.bytes()` 的便利响应。
- 🛠️ 方法快捷：`ky.get/post/put/patch/head/delete/query(input, options?)`，会自动设置对应 HTTP 方法。
- 🔧 核心选项：`method`、`json`、`searchParams`、`baseUrl`、`prefix`、`retry`、`timeout`、`totalTimeout`、`maxResponseSize`、`hooks`、`throwHttpErrors`、`context`、`dispatcher`、`next` 等。
- 🔗 `baseUrl` 按标准 URL 解析规则工作；`prefix` 只是字符串拼接。多数场景推荐 `baseUrl`，除非希望 `/users` 被当作页面相对路径。
- 🔁 重试：默认 `limit: 2`，对 GET/PUT/HEAD/DELETE/OPTIONS/TRACE/QUERY 等可重试方法，在 408/413/429/500/502/503/504 等状态和网络错误时重试；支持 `shouldRetry`、`retryOnTimeout`、`jitter`、`backoffLimit`、`maxRetryAfter`。
- ⏱️ 超时：`timeout` 默认每次尝试 10000ms，`false` 可关闭；`totalTimeout` 控制包含重试和延迟的总时长；`maxResponseSize` 限制响应体大小并抛 `ResponseSizeError`。
- 🪝 Hooks 生命周期：`init` 同步修改选项；`beforeRequest` 请求前修改/替换请求或 mock；`beforeRetry` 重试前修改请求；`beforeError` 抛错前修改错误；`afterResponse` 读取/修改响应，可用 `ky.retry()` 强制重试。
- 🏭 实例：`ky.create()` 创建全新默认实例；`ky.extend()` 继承父默认并深合并 hooks/headers/searchParams；`replaceOption()` 可改为替换而非合并。
- ⛔ 控制重试：`ky.stop` 可静默停止重试，但响应为 `undefined` 且不能用 body 方法；更推荐从 hook 抛错。
- 🔄 强制重试：`ky.retry({delay, code, cause, request})` 可在 `afterResponse` 中基于响应体或状态强制重试，受 `retry.limit` 约束。
- 🧾 错误类型：`KyError` 为基类，包含 `HTTPError`、`NetworkError`、`TimeoutError`、`ResponseSizeError`、`ForceRetryError`；`SchemaValidationError` 不继承 `KyError`。提供 `isKyError()` 等类型守卫。
- ✅ 校验：`.json(schema)` 支持 Standard Schema 兼容校验器，如 Zod 3.24+；失败抛 `SchemaValidationError`，包含 `issues`。
- 📤 进度与流：`onDownloadProgress` / `onUploadProgress` 提供 percent、bytes、chunk；流式上传需 request stream support，且默认重试会缓冲整个流。
- 📝 数据处理：`parseJson` 可自定义 JSON 解析，如 Bourne、reviver、错误日志；`stringifyJson` 可自定义序列化；`fetch` 选项可包装或注入自定义 fetch。
- 🧪 表单与取消：`FormData` 自动 multipart；`URLSearchParams` 为 x-www-form-urlencoded；可手动覆盖 `Content-Type`；用 `AbortController` 取消请求。
- 🌐 代理与 HTTP/2：Node.js 可用 `NODE_USE_ENV_PROXY` 或 undici 的 `ProxyAgent`/`EnvHttpProxyAgent`；HTTP/2 需自定义 `Agent/Pool` 并启用 `allowH2`。
- 📡 生态：SSE 可配合 `parse-sse`，分页可配合 `fetch-extras`，测试可用 Vitest/Playwright/MSW 或自定义 `fetch`。
- 🧷 TS 与支持：JSON 泛型默认 `unknown`；类型设计避免全局模块扩充，建议本地包装类型；支持最新 Chrome/Firefox/Safari、Node.js 22+。
- ❓ FAQ 要点：Node 原生 fetch 可直接使用；SSR 注意绝对 URL；认证用 `beforeRequest`，401 刷新令牌用 `beforeRetry`；相比 `got` 更小且跨浏览器，相比 `axios` 更现代、标准化。
- 🌸 名称含义：`ky` 是随机短包名，但在日语中可指“空気読めない”（kuuki yomenai，不会读空气）。

---

### [](https://github.com/unjs/ofetch)

**原文标题**: [GitHub - unjs/ofetch: 😱 A better fetch API. Works everywhere. · GitHub](https://github.com/unjs/ofetch)

ofetch 是 unjs 推出的增强版 fetch API，可在 Node、浏览器和 Workers 中运行；当前 README 面向 v2 alpha 开发分支，v1 文档需查看 v1。它重点解决响应解析、错误处理、重试、超时、拦截器、类型支持、baseURL/query、代理、SSE 等常见请求需求，仓库约 5.4k stars、198 forks，MIT 许可。

- 😱 定位：更好的 fetch API，跨 Node、浏览器、Workers 使用。
- 🚀 快速开始：`npx nypm i ofetch`，然后 `import { ofetch } from "ofetch"`。
- ✔️ 响应解析：自动解析 JSON；二进制内容返回 `Blob`；可用 `parseResponse` 或 `responseType`（`blob`、`arrayBuffer`、`text`、`stream`）自定义解析。
- 🧾 JSON 请求体：对象或带 `.toJSON()` 的类会自动 `JSON.stringify`；`PUT`、`PATCH`、`POST` 的字符串/对象体会默认加 `content-type` 和 `accept: application/json`，可覆盖。
- 🧩 二进制流支持：支持 `Buffer`、`ReadableStream`、`Stream` 等，流式请求自动设置 `duplex: "half"`。
- ⚠️ 错误处理：`response.ok` 为 `false` 时抛出 `FetchError`，含友好错误信息和精简堆栈；`error.data` 可取解析后的错误体；`ignoreResponseError` 可跳过状态错误。
- 🔁 自动重试：默认可重试状态码包括 408、409、425、429、500、502、503、504；可配 `retry`、`retryDelay`、`retryStatusCodes`；默认 `retry=1`，但 `POST`、`PUT`、`PATCH`、`DELETE` 默认不重试，自定义后则总是重试。
- ⏱️ 超时：通过 `timeout` 毫秒数自动中止请求，默认禁用。
- 🧠 类型友好：支持 `ofetch<Article>(...)`，获得返回值类型提示。
- 🔗 URL 处理：`baseURL` 自动拼接；`query` 或 `params` 通过 `ufo` 添加查询参数并保留原查询。
- 🪝 拦截器：支持 `onRequest`、`onRequestError`、`onResponse`、`onResponseError`，可传数组；可用 `ofetch.create` 共享拦截器。
- 🏭 默认实例：`ofetch.create({ baseURL: "/api" })` 可创建带默认选项的 fetch 实例；注意嵌套选项如 `headers` 的克隆与继承。
- 📨 自定义请求头：通过 `headers` 选项追加额外请求头。
- 🍣 原始响应：`ofetch.raw` 可访问原始响应，如 `headers` 等。
- 🌿 原生 fetch：`ofetch.native` 直接提供原生 `fetch` API。
- 📡 SSE：可处理 SSE 响应，读取 stream 并解码文本块。
- 🕵️ 代理支持：Node 可用 `undici` 的 `ProxyAgent`/`dispatcher`，支持全局 `setGlobalDispatcher` 和自签名证书（有 MITM 风险）；Bun 支持 `proxy`；Deno 可用 undici；Bun/Deno 遵循 `HTTP_PROXY`、`HTTPS_PROXY`，Node 需 `NODE_USE_ENV_PROXY=1`。
- 💪 类型扩展：可通过 `declare module "ofetch"` 扩展 `FetchOptions`，添加自定义属性并获得类型安全。
- 📊 仓库信息：unjs/ofetch，约 5.4k stars、198 forks、14 watchers、52 issues、78 pull requests、415 commits；MIT 许可。

---

### [](https://elbywan.github.io/wretch/)

**原文标题**: [Wretch - The Tiny Fetch Wrapper](https://elbywan.github.io/wretch/)

Wretch 是一个约 1.8KB（gzip）的轻量 fetch 封装，提供直观、可链式、同构且模块化的 HTTP 请求方式，并可通过 Addons 与 Middlewares 扩展能力。

- 📦 体积小巧：约 1.8KB gzipped，围绕原生 fetch 构建。
- 🔗 链式语法：所有方法 100% 可链式调用，代码简洁易读。
- 🧊 不可变设计：不修改内部状态，每次函数调用返回原对象副本。
- 🌐 同构兼容：支持浏览器和 Node.js，可使用任意 polyfill。
- 🧩 模块化扩展：Addons 添加新方法，Middlewares 拦截请求并自定义行为。
- ⌨️ 开发友好：语法直观，包含 TypeScript 定义文件，支持自动补全。
- 📥 安装方式：支持 npm、yarn、pnpm、bun 以及 CDN 引入。
- 🚀 快速开始：导入 wretch、创建实例、配置 URL、添加请求体、执行方法、处理错误、解析响应。
- 🛠️ 请求与响应：支持 .json、.formData、.formUrl 等请求体；响应可解析为 .json、.text、.blob、.arrayBuffer。
- 🚨 错误处理：支持 .notFound、.unauthorized、.forbidden、.error(500, ...) 等链式处理。
- 🧪 完整示例：通过 `await wretch(...).json(...).post().notFound(...).error(...).json()` 获取用户数据。
- 🔌 扩展能力：Addons 可处理查询字符串、表单数据等；Middlewares 可实现重试、缓存、节流和自定义拦截器。
- 📜 项目信息：作者 Julien Elbaz，MIT 许可证，2017-2025，图标来自 Lucide（ISC 许可证）。

---

### [](https://www.sonarsource.com/products/sonarqube/hunter-agent/?utm_source=fnf&utm_medium=paid&utm_campaign=ss-hunteragents26&utm_term=newsletter-node&utm_content=v1&s_category=Paid&s_source=Paid+Other&s_origin=influencer)

**原文标题**: [SonarQube Hunter Agent | AI Logic Flaw Detection Tools | Sonar](https://www.sonarsource.com/products/sonarqube/hunter-agent/?utm_source=fnf&utm_medium=paid&utm_campaign=ss-hunteragents26&utm_term=newsletter-node&utm_content=v1&s_category=Paid&s_source=Paid+Other&s_origin=influencer)

SonarQube Hunter Agent 是 Sonar 推出的 AI 驱动安全代理，专门搜寻传统分析工具无法捕捉的逻辑漏洞，包括越权访问、业务逻辑缺陷和身份认证问题。它能发现代码本身看似正常但意图被滥用的漏洞，在开源应用中已揭露超过 200 个 0day 漏洞，精确度达 90%，且结果可重复。该代理通过 playbook 进行全代码库深度推理，与 SAST、SCA 结合形成分层安全防护，并直接集成到 SonarQube 现有工作流中。

- 🎯 专为搜寻逻辑漏洞设计，发现访问控制、业务逻辑和身份认证三类传统分析无法捕捉的缺陷
- 🔍 检测范围涵盖越权访问（IDOR、权限提升、敏感数据暴露）、业务逻辑缺陷（跳过流程步骤、缺少速率限制）及身份认证问题（会话固定、弱密码恢复、缺少 MFA、暴力破解缺口）
- 📊 战绩亮眼：在开源应用中揭露超过 200 个 0day 漏洞，精确度高达 90%
- 🔁 扫描结果高度可重复，避免普通 AI 提示每次运行结果从 2-3 个到 60 个不等的波动问题
- 🧠 通过 playbook（多步骤专业安全提示序列）进行全代码库深度推理，像安全研究员一样跟踪数据与身份流，构建假设并验证
- 🔄 四步工作流程：搜寻（探索代码库、跟踪流）、确认（验证每个可疑漏洞）、解释（提供严重级别、原因与精确位置）、集成（发现结果进入 SonarQube 问题列表）
- 🛡️ 与 SAST 和 SCA 形成分层防护，各司其职：SAST 捕捉已知模式与注入漏洞，Hunter Agent 捕捉意图型漏洞
- 🔒 独立零信任设计：审查代码的代理并非编写代码的代理，方法不同、职责分离、发现可审计且可重复
- ⚙️ 无缝集成现有工作流，发现结果自动标记进入 SonarQube 问题列表，无需安装新工具
- 📅 SonarQube World Tour NYC 将于 10 月 15 日举行，聚焦代理式软件工厂构建

---

### [繁忙机器上的 Node.js 线程池](https://blog.platformatic.dev/more-threads-on-an-already-busy-machine)

**原文标题**: [Node.js Thread Pools on Busy Machines](https://blog.platformatic.dev/more-threads-on-an-already-busy-machine)

本文讨论了 Node.js 线程池自动扩容的问题：作者 Matteo Collina 反对根据 CPU 数量自动设置线程池大小，认为 `os.availableParallelism()` 只反映进程可用的并行能力，并不代表 CPU 真的空闲；在繁忙主机上盲目增加 worker 反而会拖慢事件循环、增加请求延迟。文章建议按实际测量结果手动调优，并在繁忙主机上同时关注吞吐量与慢请求，尤其对 bcrypt 这类 CPU 密集型任务更需谨慎。

- 🧠 **核心异议**：反对"按 CPU 数自动决定线程池大小"，因为系统不清楚机器上还有谁在占用 CPU
- 📊 **"可用"不等于"空闲"**：`os.availableParallelism()` 只估算进程可用的并行度，并不检查 CPU 是否真的空闲
- ⚔️ **多进程竞争**：多个进程都读到 16 就各起 worker，会一起抢占同一批 CPU 时间，没有预留机制
- 🐌 **nice 值不等于空闲**：降低到 nice 10 只是减少份额，仍会占用 CPU、内存与缓存带宽，还可能拉长请求完成延迟
- 🖥️ **一 vCPU 的例外**：Nub 检测到 ≤1 vCPU 时仍保留 4 个 worker（10 是 nice 值，不是线程数），对容器配额而言仍可能过多
- 📉 **gzip 实测反例**：2 MiB 输入、8:1 压缩下，1 worker + 1 job 达 49.3 MiB/s，4 worker + 4 job 只有 37.3 MiB/s，增加并发反而更慢
- 💾 **等待存储与计算不同**：I/O worker 等待存储时几乎不耗 CPU，多起 worker 可能有收益；bcrypt 是计算密集型，无法享受这种好处
- 🧪 **基准测试的矛盾**：Node.js PR 中更大线程池提升了 crypto 基准，却让某个文件系统基准变慢，不能据此一刀切定默认值
- ✅ **结论与建议**：应针对具体应用在繁忙主机上测试，兼顾吞吐与慢请求；nice 值解决不了这个问题，且队列的 job/字节预算满时必须停止接收工作

---

### [](https://www.kevinold.com/blog/a-week-maintaining-wait-on)

**原文标题**: [Maintaining wait-on at agent speed: AI, npm supply-chain risk, and a Rust engine](https://www.kevinold.com/blog/a-week-maintaining-wait-on)

Kevin Old 加入 wait-on 维护者后，借助 AI 编码代理、Compound Engineering 工作流与严格护栏，在约一周内推进大量 PR、发布新版本，并并行启动 Rust 引擎移植以降低 npm 供应链风险；核心教训是：在广泛依赖的包上，agent 速度只有在护栏能同样快速被机器检查时才可信。

- ⏳ wait-on 由 Jeff Barczewski 于 2015 年创建，用于等待文件、端口、socket 或 URL 就绪，常见于“先启动 dev server，再跑 e2e 测试”。
- 📈 影响面很大：npm 周下载 12,791,721；start-server-and-test 固定 9.1.0；jest-dev-server 等依赖它；Grafana、WordPress、Storybook、React Router、undici、Cloudflare、Elastic、Shopify、Angular、Microsoft、Meta、Spotify、IBM、Automattic 等项目也在使用。
- 🤖 作者用 AI agents 一夜并行完成 Rust 实现；Rust engine 与 JS 同 API，并通过同一测试套件：496 passing、0 failing、0 pending。
- 🗓️ 9 月 22 日至 10 月 1 日：合并 27 个 PR（26 个来自作者），关闭 17 个 issue（最老可追溯到 2017 年），发布 9.2.0 到 9.5.1 等版本。
- 🚧 10.0.0-rc.1 进入 next tag：移除 axios/lodash，HTTP 检查转向 fetch + undici，要求 Node 22.19；Rust engine 不在该 RC，计划进入未来 major。
- 🦀 Rust port 以 parent issue #35 为 spine，拆成 14 个 lanes，每个 lane 对应一个 issue、plan 和 PR；在 fork 上合并，实验分支有 243 个 commits（PR #51）。
- 🧩 许多工作是把积压社区 PR 用今日代码重建：parseArgs、TypeScript 定义、command 资源、string options、axios→fetch 等；10.0 release notes 致谢 @arthurzam 与 @rogervila。
- 🧠 工作流基于 Compound Engineering：brainstorm、plan、work、review、compound；计划写入 docs/plans/（已有 47 个），经验写入 docs/solutions/。
- 🛠️ overdrive 整合工具；ko-multi-worker-pm 让一个 agent 会话充当 PM，按 gate 管理 lanes，最多三个 workers 并行，并在 herdr 中为每个 worker 提供独立 pane。
- 🧪 速度带来更严规则：AGENTS.md 强制 test-first；每个 bug 先有失败复现；计划中风险要变成失败测试；两个输入交互时，组合逐项测试。
- 🔐 护栏包括：人类合并；agents 可开 PR 但不能改 CI；Rust lanes 不得碰 .github/workflows/；提交信息检查；semantic-release + OIDC trusted publishing，不从笔记本发布。
- ⚠️ 供应链防御是 Rust 的核心动机：Shai-Hulud 蠕虫后 npm 建议 ignore-scripts=true；wait-on 被装进大量 e2e 流水线，其依赖也是别人的攻击面。
- 📉 依赖树已开始削减：9.5.1 依赖 joi/rxjs/axios/lodash；10.0.0-rc.1 依赖 joi/rxjs/undici；Rust 默认后目标只剩 joi，且 Rust 路径不加载 rxjs/undici。
- 📦 Rust 打包策略：WAIT_ON_ENGINE=rust 可选；无安装脚本、安装时不下载；八个平台二进制同一 tarball；用 ignore-scripts=true、--read-only --network none 容器测试。
- ✅ Rust 依赖审计：cargo-deny 与 cargo-vet 把关；npm provenance 只证明谁构建 binary，不证明内部 crates 安全。
- 🔁 双引擎同 repo：crates/ 与 lib/ 并存；npm test 跑 JS，WAIT_ON_ENGINE=rust-strict 跑同一 mocha 套件；Rust 核心保持 100% 行/区域覆盖。
- 💰 成本：JS-only 约 70 KB unpacked；带八二进制的预发布约 15,035,917 bytes packed、约 36 MB unpacked；目标约 8 MB packed；Rust 仍启动 Node，依赖削减未完全落地。
- 🧭 建议：试用 Compound Engineering/overdrive，安装 herdr 和 skills，测试 wait-on@next，并复制护栏：test-first、一 PR 一关注点、人类合并、agents 不改 CI、不从笔记本发布。
- 💡 结论：在如此广泛安装的包上，agent 速度只有在护栏能以同样速度被检查时才可信；作者主要读计划与测试，让测试严格到足以信任未逐行阅读的代码。

---

### [](https://github.com/jeffbski/wait-on)

**原文标题**: [GitHub - jeffbski/wait-on: wait-on is a cross-platform command line utility and Node.js API which will wait for files, ports, sockets, and http(s) resources to become available · GitHub](https://github.com/jeffbski/wait-on)

wait-on 是一个跨平台的命令行工具与 Node.js API,用于等待文件、端口、套接字及 http(s) 资源变为可用(或通过反向模式等待其不可用),让构建或启动流程可以按依赖顺序可靠衔接。

- 🌐 跨平台运行,凡 Node.js 支持的环境(Linux、Unix、macOS、Windows)均可使用
- 📦 支持多种资源类型:文件(默认)、http、https、tcp 端口、Unix 域套接字,以及执行任意命令等待其退出码为 0
- 🔁 提供反向模式(--reverse),等待资源变为不可用,适合确认服务已关闭再继续后续操作
- ⏱️ 文件监测带稳定性窗口(window,默认 750ms),等待文件大小停止增长后才判定就绪
- 🔍 http/https 前缀发送 HEAD 请求,http-get/https-get 前缀发送 GET 请求,适用于不支持 HEAD 或需依据响应体判断的场景
- ✅ 默认只接受 2XX 状态码,可用 --status-codes 指定单码、范围或逗号列表(如 200-499)
- 🛠️ 常用选项包括初始延迟 delay、轮询间隔 interval、超时 timeout、tcpTimeout、并发数 simultaneous、日志 log 与详细输出 verbose
- 🔐 支持 TLS 相关配置(ca、cert、key、passphrase、strictSSL)、代理 proxy、认证 auth、自定义 headers 与 validateStatus 函数
- 💻 命令行用法简洁:wait-on 资源 && NEXT_CMD,资源就绪后以退出码 0 触发下一条命令,被中断或超时则返回非零码
- 🧩 同时提供 Node.js API,支持回调、Promise 与 async/await 三种调用方式,并可通过 js/json 配置文件传参
- 📝 在 Node.js 20+ 上 localhost 会同时解析 IPv4 与 IPv6,旧版本可能只解析 ::1 导致 IPv4 服务看似不可用
- ⭐ 项目采用 MIT 许可,目前在 GitHub 上有约 2k Star、89 个 Fork

---

### [如何将 JavaScript 编译成单个可执行文件](https://flaviocopes.com/javascript-single-executable/)

**原文标题**: [How to compile JavaScript into a single executable](https://flaviocopes.com/javascript-single-executable/)

overview summary
本文介绍如何用 Deno、Bun 和 Node.js 将 JavaScript 程序打包成单个可执行文件，并以 readtime CLI 为例，比较三种工具的命令、跨平台构建、文件嵌入、体积与启动速度、发布注意事项和选型建议。

- 🧩 JavaScript 可编译成单文件可执行程序：通过 `deno compile`、`bun build --compile`、`node --build-sea`，用户无需安装运行时或复制 `node_modules`。
- ⚙️ 与 Go/Rust 不同：它不是生成机器码，而是把运行时和 JS 代码打包在一起，所以体积很大，示例程序会变成 60–150 MB。
- 🧪 示例程序 readtime：统计 Markdown 字数并估算阅读时间，使用 `node:fs`、`node:util` 和 `picocolors`。
- 🦕 Deno：命令为 `deno compile --allow-read --output readtime readtime.js`；npm 项目需 `--no-check` 或安装 `@types/node`；权限在编译时固化到可执行文件。
- 🌍 Deno 跨平台：用 `--target` 构建 Linux、macOS、Windows，首次会下载 `denort` 并缓存。
- 📦 Deno 嵌入文件：用 `--include`，读取时基于 `import.meta.dirname`；`--bundle` 可减小体积，`--engine quickjs` 可降到 37 MB 但可能更慢。
- 🥟 Bun：命令为 `bun build --compile readtime.js --outfile readtime`；自动打包依赖，无需权限或类型检查。
- 🐧 Bun 跨平台：支持 `bun-linux-x64`、`bun-darwin-arm64`、`bun-windows-x64` 等，也支持 Alpine Linux 的 musl。
- 🚀 Bun 生产标志：`--minify`、`--sourcemap`、`--bytecode`；嵌入文件用 `import './help.txt'` 或 `with { type: 'file' }`。
- 🟢 Node.js：称为 SEA，需先用 esbuild 等打包，再运行 `node --build-sea sea-config.json`；Node 25.5+ 简化了流程。
- 🍎 Node macOS：写入 node 二进制会破坏签名，需要 `codesign --sign - readtime`；Linux 不需要，Windows 可选。
- 🧷 Node 嵌入文件：在 `sea-config.json` 的 `assets` 中列出，用 `node:sea` 的 `getAsset()` 读取，并用 `isSea()` 判断。
- 💻 Node 跨平台：没有 `--target`，需下载对应平台的 node 二进制并通过 `executable` 字段指定；旧版 Node 24/22 用 blob + postject。
- 📊 体积与速度：Rust 446 KB/1.3 ms；Bun 62 MB/7 ms；Deno 68 MB/20 ms；Node 146 MB/24 ms；Linux 构建更大，Bun 81 MB、Deno 105 MB、Node 150 MB。
- 📁 发布注意：每个平台一个文件；代码没有隐藏，`strings` 可读源码，不要放密钥。
- 🔐 签名：macOS 需 Developer ID 并公证，Windows SmartScreen 会警告未签名 exe。
- 🧠 动态加载：计算路径的 `import()`、worker、运行时读取文件不会被自动包含，需 Deno `--include`、Bun 文件导入、Node `assets`；原生 `.node` 插件最难处理。
- 🧭 Bun 和 Deno 编译出的程序运行在各自运行时上，不依赖 Node；使用不常见 Node API 时需测试。
- 🗑️ pkg 已归档，nexe 老旧；新项目应使用三大内置方案。
- ✅ 选型建议：优先 Bun；已有 Deno 或想固化权限用 `deno compile`；需要 Node 本身、原生模块或团队偏好时用 Node SEA。

---

### [](https://github.com/dolanmiu/docx/releases/tag/9.9.0)

**原文标题**: [Release 9.9.0 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/releases/tag/9.9.0)

overview summary
dolanmiu/docx 发布最新版 9.9.0，最大亮点是新增 docx/layout 排版引擎，按 Word 的方式计算页面布局，并让目录页码、页面引用、PAGE/SECTION 域和 SEQ 题注编号保持“干净”；同时带来大量修复、表格/补丁增强和依赖更新。

- 🚀 9.9.0 为最新版本，于 10 月 7 日发布，包含自 9.8.1 以来的大量变更。
- 🧩 新增 docx/layout 入口点，可像 Word 一样计算文档中元素的页面位置。
- 🔢 可写入目录页码、页面引用（含 \p 及自定义格式）、PAGE/SECTION 字段和 SEQ 题注编号，减少 Word 打开时更新域提示。
- 📄 支持读取现有 .docx，用于填充模板页码、核对 Word 页面，并返回每页内容。
- ⚠️ 遇到尚未支持的布局会停止并说明，或按需给出最佳猜测。
- 🔤 文本测量支持 Pretext、Word 宽度表、给定/嵌入/Office 字体，并处理斜体、伪粗体、字距、连字、缺字、多语言及 RTL/东亚字体提示。
- 📝 行与段落覆盖升降部高度、图片基线、对齐空格压缩、边框、自动/上下文间距、缩进、制表符、软连字符、隐藏文字、修订、上标、小型大写、着重号、拼音指南和首字下沉等。
- 🔢 列表按 Word 方式编号和定位，支持带边框列表、Word 6 列表编号及列表样式。
- 📊 表格支持自动适配、长单词列加宽、合并/嵌套单元格、跨页断行、重复表头、行高、边框、单元格间距、浮动表格和按页宽比例等。
- 📑 节、栏与页码支持不同宽度分栏、连续分节前均栏、下一栏节、跨栏保留段落、装订线/小册子、多种页码格式、章节号和重排。
- 🧷 脚注/尾注支持编号定位、跨页延续、分栏/表格行/保留段落布局、分隔符、续分隔符和尾注页。
- 🖼️ 图形与框架支持图片、形状、浮动表格的文字环绕（含重叠）、文本框、VML 文本框、对象、图片和页眉图片。
- 🧮 公式支持线性/堆叠公式、数学设置、重音、上下限、括号、上下标、幻影、框和公式数组。
- 🌏 东亚版式与兼容支持文档网格、竖排、日文线规则、压缩标点、网格缩进，以及兼容模式 11/12/14、suppressTopSpacing、useFELayout、HTML divisions 和 w:altChunk。
- ✅ 通过与 Word 输出对比验证布局，含 scripts/layout-probes 探测与 Word PDF，并合入大量布局 PR。
- 🛠️ 其他修复/功能包括 PageReference、Turbopack 下 ImageRun、patchDocument 书签/脚注尾注、外部样式保留、重新打包一致性、RTL 保留、嵌入字体、目录条目、表格列宽、PatchType.TABLE_ROWS 和链接格式等。
- 📦 依赖更新包括 prettier、@types/node、cspell、markdown-it、eslint、typescript-eslint、api-extractor、vite、vitest、globals 等。
- 👥 贡献者包括 dolanmiu、alexvcasillas 等，新贡献者 @vhinayindia；完整变更见 9.8.1...9.9.0。

---

### [docx - 使用 JavaScript 生成 .docx 文档](https://docx.js.org/)

**原文标题**: [docx - Generate .docx documents with JavaScript](https://docx.js.org/)

未提供任何可总结的文本内容，因此无法生成有效摘要。

- 📄 当前消息中“Use the following content:”之后没有附带正文。
- ❓ 缺少原文会导致无法提取关键点、核心信息或结论。
- 📝 请补充需要总结的文章或文本，我将按要求输出中文摘要。

---

### [](https://h3.dev/blog/v2)

**原文标题**: [H3 v2 - H3](https://h3.dev/blog/v2)

H3 v2 已正式发布稳定版，这是一个基于 Web 标准的全面重写版本，兼容大部分 v1 工具，并且比 v1 更快、更小。它带来了 Web 标准优先的设计、跨平台运行能力、类 URLPattern 路由、中间件与插件支持、类型安全、路由规则引擎以及丰富的内置工具，同时升级门槛较低。

- 🎉 H3 v2 现已稳定发布，基于 Web 标准全面重写，兼容大多数 v1 工具，速度更快、体积更小
- 🌐 以 Web 标准为核心，基于 Request、Response、URL 和 Headers 构建；处理器接收标准 Request，返回任意值都会自动转换为 Response
- 🚀 跨平台运行，同一应用可在 Node.js、Bun、Deno、Cloudflare Workers、Service Workers 和浏览器中运行，srvx 提供通用服务层
- 🌳 采用 rou3 v1 实现类 URLPattern 路由，支持命名参数、正则约束、可选与重复参数、分组和通配符，查找依然快速
- 🧩 支持 (event, next) 中间件、内置辅助函数（onRequest、onResponse、onError、basicAuth、bodyLimit 等）以及可复用插件
- 🔒 类型安全，处理器、响应和错误均有类型；验证处理器与 body/query/params 验证兼容任意 Standard Schema 库
- 📏 新增 h3/rules 路由规则引擎，可通过一个配置对象为路由组添加请求头、重定向、CORS、缓存和代理
- 🧰 内置丰富工具，涵盖 cookies（含分块 cookies）、会话、CORS、代理、静态文件、缓存头、SSE、WebSocket、JSON-RPC/MCP 等
- ⬆️ 升级便捷，大部分 v1 工具仍可使用，已弃用的 v1 名称仍会导出；在 Node.js 上运行需 >= 20.19
- ❤️ 特别感谢所有贡献者、测试者、社区、Nitro 社区以及赞助商的支持

---

### [入门 - H3](https://h3.dev/guide)

**原文标题**: [Getting Started - H3](https://h3.dev/guide)

H3 v2 是一个轻量、快速且可组合的现代 JavaScript 服务端框架，基于 Request、Response、URL、Headers 等 Web 标准原语，可与兼容运行时集成，也能低延迟挂载其他 Web 兼容处理器；它从轻量 H3 实例出发，按需引入可摇树工具或自定义功能，并共享 H3Event 上下文。

- ⚡ 核心定位：H3 是面向现代 JavaScript 运行时的轻量、快速、可组合服务器框架。
- 🌐 Web 标准：基于 Request、Response、URL、Headers 等标准原语，兼容多种运行时。
- 🧩 可组合设计：不提供庞大核心，而是从轻量 H3 实例开始，按需导入内置可摇树工具或自带功能。
- 📦 打包优势：只包含实际使用代码，应用体积更易扩展，工具使用显式清晰、全局影响更小。
- 🎯 少预设：H3 尽量不限制开发者选择，所有工具共享 H3Event 上下文。
- 🚀 快速开始：安装 h3 后创建 server.mjs，使用 new H3().get("/", ...) 和 serve(app, { port: 3000 }) 启动。
- 🔄 跨运行时：可用 Node、Deno、Bun 等运行；serve 基于 srvx，符合 Web 标准且跨运行时。
- 🧪 测试与部署：app.fetch 可用于 Web 兼容运行时或直接测试；也可通过 CDN 导入，如 Cloudflare Workers。
- 🧠 工作机制：H3 类负责匹配路由、生成响应、调用中间件与全局钩子；返回值会自动转换为 Web 响应。
- 📌 文档版本：当前为 H3 v2 文档，旧版文档见 v1.h3.dev。
- 📚 文档范围：涵盖基础、请求生命周期、路由、中间件、事件处理、响应、错误处理、嵌套应用、路由规则、API、插件、WebSocket 等。

---

### [](https://crashunited.itch.io/klattsch/devlog/1580425/klattsch-engine-is-free-software-put-it-in-your-game)

**原文标题**: [klattsch engine is free software - put it in your game! - klattsch by Crash United](https://crashunited.itch.io/klattsch/devlog/1580425/klattsch-engine-is-free-software-put-it-in-your-game)

klattsch 是一个 MIT 许可的免费语音合成引擎，其 npm 包可直接嵌入游戏；支持 CLI 烘焙 WAV、浏览器实时合成、Godot/Unity 集成和 Rust 移植，并允许商业免版税使用，只需保留许可证声明。

- 🎛️ klattsch app 底层是免费 MIT 语音合成引擎，`klattsch` npm 包就是核心，可直接用于自己的游戏。
- 🗣️ 输入 ARPABET 音素与音高、速度、颤音、呼吸等指令即可发声；音高支持音符（如 `bC4`）或频率。
- 💻 最简方式无需代码：`npx klattsch "..." guard_halt.wav` 生成 WAV；可在 app 或 `klatts.ch/play` 测试。
- 📦 构建时烘焙：`klattsch/dialog-bake` 读取 CSV，输出 `out/<id>.wav`，适合 Unity、Unreal、GameMaker、Ren'Py 等，无需运行时 Node。
- 🌐 Web 实时合成：通过 AudioWorklet 和 `compileString` 生成 schedule，连接 `formant-processor`，适合 Phaser、PixiJS、Vite、webpack。
- 🎮 Godot 支持：`klattsch/godot` 是编辑器插件与示例，保留 `voice_lines.csv` 后一键烘焙/导入，并支持 JavaScriptBridge。
- 🎭 它是合成器/乐器：可程序化生成角色声线，例如 `b95 r180` 守卫、`b160 r240 s1.2` 店主，还可加呼吸、颤音、缩放声道。
- 🧬 运行时生成：可合成程序化名字、动态输入或 Animalese 式音节乱语，不必预先烘焙所有句子。
- 👄 口型同步：`compileString` 返回带时间戳的 schedule，`dialog-bake --schedules` 可导出 JSON 驱动嘴型动画。
- ⏱️ 示例 countdown-choir：倒计时合唱，运行时修改字符串、压缩时间并提高音高，营造恐慌感。
- 🖥️ app 可当编辑器：GUI 中试听/作曲，文本模式复制音素串到代码，也能直接导出 WAV。
- 🧩 原生嵌入：在 QuickJS/Jint 等嵌入式 JS 解释器运行 `compileString`/`renderToBuffer`，把 PCM 交给引擎音频 API。
- 🦀 Rust 移植：`klattsch-rs` 在 crates.io，`FormantSynth::process` 实时安全（无分配/锁/I/O），适合 Bevy、godot-rust、cpal；目前基于较旧引擎，即将更新。
- ⚙️ 引擎结构简单：声门脉冲 + 噪声源经三个带通滤波器；曾用定点 C 重写到 386 DOS。
- ⚖️ MIT 许可：声音归你、可商业免版税；捆绑代码需保留版权与许可证文本；非 copyleft，可闭源，只需保留版权声明。
- 🙏 作者请求：若使用，可在鸣谢中写 “Speech synthesis by klattsch (https://klatts.ch) / Tony Gies”，并展示作品；klattsch 工具售价 $9.99 或更多，支持多语言与盲友好。

---

### [](https://feedsmith.dev/)

**原文标题**: [Feedsmith: Fast JavaScript Feed Parser and Generator](https://feedsmith.dev/)

Feedsmith 是一个快速、全能的 JavaScript feed 解析与生成库，支持 RSS、Atom、RDF、JSON Feed，并兼容主流命名空间与 OPML。其通用及格式专用解析器会把 feed 转为镜像原始结构的对象，并将旧元素映射到现代等价项，让新旧 feed 读取方式一致。Feedsmith 3.0 已发布，带来多项改进与破坏性变更，并提供迁移指南。

- 🚀 核心定位：一个包同时完成 feed 解析与生成，覆盖主要 feed 格式和命名空间。
- 🧩 结构保留：解析后的对象保持原始 feed 结构，便于访问数据。
- 🏷️ 命名空间智能处理：将自定义前缀规范化为标准前缀，如 `<custom:creator>` 变为 `dc.creator`。
- 🧬 旧格式兼容：自动将旧元素规范化为现代等价项，减少旧 feed 读取负担。
- 🔤 大小写不敏感：字段和属性可任意大小写组合。
- 🌐 命名空间 URI 宽容：接受非官方 URI、HTTPS 变体、大小写差异、尾随斜杠和空白。
- 🛠️ 容错性强：优雅处理畸形或不完整 feed，并提取有效数据，适合真实世界 feed。
- ⚡ 性能：号称最快的 JavaScript feed 解析器之一，并提供基准测试。
- 🧾 类型安全：用 TypeScript 从底层构建，为每种格式和命名空间提供完整类型定义。
- 🌳 Tree-shakable：可按需引入，减少打包体积。
- ✅ 测试充分：超过 4000 个测试，代码覆盖率 99%。
- 💻 兼容性：支持 Node.js 和现代浏览器，也可用纯 JavaScript，无需 TypeScript。
- 📡 支持格式：RSS 0.9x/2.0 可解析/生成；Atom 0.3/1.0 可解析/生成；RDF 0.9/1.0 可解析，生成计划中；JSON Feed 1.0/1.1 可解析/生成；OPML 1.0/2.0 可解析/生成。
- 🧩 命名空间：支持 Atom、Dublin Core、Syndication、Content、Slash、iTunes、Podcast Index、Media RSS、Spotify、YouTube、GeoRSS、OpenSearch 等大量命名空间的解析与生成。
- 🎯 与替代方案差异：Feedsmith 的关键优势是精确保留各 feed 格式定义的原始结构，避免把 `author`、`dc:creator`、`creator` 合并，混同 `dc:date`、`pubDate`，或不一致处理多个 `<atom:link>` 等归一化造成的信息丢失。

---

### [快速开始](https://feedsmith.dev/quick-start)

**原文标题**: [Quick Start](https://feedsmith.dev/quick-start)

本指南帮助你快速上手 Feedsmith：它支持解析和生成 RSS、Atom、RDF、JSON Feed 及 OPML，可在 Node.js 14.0.0+ 和现代浏览器中使用，并兼容 CommonJS 与 ES 模块。

- 📦 安装：可通过 npm、yarn、pnpm、bun 安装，也可通过 CDN（如 esm.sh）在浏览器中使用。
- 🔄 通用解析：使用 `parseFeed` 可自动识别并解析 RSS、Atom、RDF 和 JSON Feed，返回格式与 feed 数据。
- 🎯 指定格式解析：提供 `parseRssFeed`、`parseAtomFeed`、`parseRdfFeed`、`parseJsonFeed` 等专用解析器，便于访问类型化数据。
- 📂 OPML 解析：使用 `parseOpml` 解析 OPML 文件，可访问 `head`、`body`、`outlines` 等信息。
- 🏗️ 生成 Feed：使用 `generateRssFeed`、`generateAtomFeed`、`generateJsonFeed`、`generateOpml` 生成对应格式内容。
- ⚠️ 错误处理：抛出 `DetectError`、`MalformedError`、`ParseError`、`GenerateError`，分别对应格式不匹配、内容畸形、解析结果无效、生成失败。
- 🧩 TypeScript 类型：为所有 Feed 格式提供完整类型，包括 `AnyFeed`、`AtomFeed`、`JsonFeed`、`Opml`、`RssFeed` 及嵌套类型。
- 📚 后续学习：可继续查看解析 Feed、命名空间、生成 Feed、API 参考和基准测试等文档。

---

### [从 2.x 迁移到 3.x](https://feedsmith.dev/migration/v2-to-v3)

**原文标题**: [Migrate from 2.x to 3.x](https://feedsmith.dev/migration/v2-to-v3)

本指南详细说明 Feedsmith 从 2.x 升级到 3.x 的破坏性变更与迁移步骤：3.x 将默认行为改为宽松模式，严格模式需显式启用，并调整 Atom、RSS、Media、Podcast、Dublin Core 等字段结构、类型导出、错误处理及新增功能。

- ⚠️ 3.x 反转默认行为：feed 默认宽松，所有字段可选；严格模式通过 `{ strict: true }` 启用。
- 📦 安装最新版：`npm install feedsmith@latest`。
- ✅ 迁移清单：移除所有生成函数调用中的 `{ lenient: true }`。
- ✅ 如需编译时校验必填字段，添加 `{ strict: true }`。
- ✅ 使用严格类型时，在类型参数最后添加 `true`。
- ✅ 移除 `DeepPartial` 导入，并改用基础类型直接访问。
- ✅ 将 `feedsmith/types` 导入改为 `feedsmith`。
- ✅ Atom 文本字段：`title`、`subtitle`、`rights`、`summary` 改为读取 `.value`，生成时用 `{ value: '...' }`。
- ✅ Atom `entry.content`：读取 `content?.value`，生成时用 `{ value: '...' }`。
- ✅ RSS 人物字段：`managingEditor`、`webMaster`、`authors` 改为读取 `.email`/`.name`，生成时用 `{ email, name }`。
- ✅ Media 弃用字段替换：`group` → `groups`。
- ✅ Podcast 弃用字段替换：`location` → `locations`，`value` → `values`，`chats` → `chat`。
- ✅ Dublin Core 单数字段改为复数数组，如 `title` → `titles`。
- ✅ Dublin Core Terms 单数字段改为复数数组，如 `title` → `titles`。
- ✅ 重命名类型导入：`Rss` → `RssFeed`，`Atom` → `AtomFeed`，`Json` → `JsonFeed`，`Rdf` → `RdfFeed`。
- ✅ 更新错误处理：使用 `DetectError`、`MalformedError`、`ParseError`、`GenerateError`，而非泛型 `Error`。
- ✅ 测试 feed 生成输出，确保迁移后结果正确。
- 🧭 严格模式现在为可选加入：2.x 默认严格且需 `{ lenient: true }` 才宽松；3.x 默认宽松，`{ strict: true }` 才严格。
- 🧩 所有类型字段默认可选：之前必填字段现在可省略；需要编译时强制时传入 `true` 作为严格类型参数。
- 🗑️ `DeepPartial` 已移除：因所有字段默认可选，不再需要；直接使用 `RssFeed.Feed`、`AtomFeed.Feed` 等基础类型。
- 🚪 `feedsmith/types` 入口已移除：所有类型从主入口 `feedsmith` 导出；旧泛型别名移除，`RssFeed` 等现在是格式类型命名空间。
- 📝 Atom 文本字段从字符串改为对象：保留 `type` 等属性；解析读 `.value`，生成传 `{ value, type? }`。
- 📦 Atom `content` 从字符串改为对象：保留 `type`、`src`、XML 命名空间；解析读 `content?.value`，生成传 `{ value, type?, src? }`。
- 🌐 Atom `type="xhtml"` 值现在为纯 HTML：移除包装 `<div>` 和 `xhtml:` 前缀，`xml:base`/`xml:lang` 折叠到 `xml` 对象，转义字符不解码；生成时传内部标记并保持良构 XML。
- 👤 RSS 人物字段从字符串改为对象：`managingEditor`、`webMaster`、`authors` 使用 `RssFeed.Person`；解析读 `email`/`name`，生成传 `{ email, name }`；`link` 仅解析不生成。
- 🎞️ Media 命名空间：弃用 `group` 移除，改用 `groups`，访问 `media.groups?.[0]`。
- 🎙️ Podcast 命名空间：`location` → `locations`，`value` → `values`，`chats` → `chat`，对齐 Podcasting 2.0。
- 📚 Dublin Core：单数字段移除，改为复数数组，如 `dc.title` → `dc.titles?.[0]`；`coverage`、`rights` 保留名称但变为数组。
- 📚 Dublin Core Terms：大量单数字段改复数数组，如 `dcterms.title` → `dcterms.titles?.[0]`；`created` 等保留名称但变为数组。
- 🏷️ 格式类型命名空间重命名：`Rss` → `RssFeed`，`Atom` → `AtomFeed`，`Json` → `JsonFeed`，`Rdf` → `RdfFeed`；旧名作为弃用别名保留至 4.x。
- 📤 `parseFeed` 返回类型公开为 `AnyFeed`：可直接标注 `const result: AnyFeed = parseFeed(content)`，函数行为不变。
- 🆕 新增错误类型：`DetectError`、`MalformedError`、`ParseError`、`GenerateError`，用于不同失败场景。
- 🆕 命名空间类型导出：`ItunesNs`、`DcNs`、`MediaNs`、`PodcastNs` 等可直接从 `feedsmith` 导入。
- 🆕 工具类型导出：`DateLike`、`XmlStylesheet` 等从主包导出。
- 🆕 自定义日期解析：解析函数支持 `parseDateFn` 选项，将所有日期字段转换为任意格式。
- 🆕 XML 命名空间支持：RSS、Atom、RDF feed 支持 `xml:*` 属性；feed 与 item 层均有 `xml` 属性，含 `xml:lang`、`xml:base`、`xml:space`、`xml:id`。

---

### [pnpm 12.10.0 | pnpm](https://pnpm.io/blog/releases/12.10.0)

**原文标题**: [pnpm 12.10.0 | pnpm](https://pnpm.io/blog/releases/12.10.0)

pnpm 12.10.0 发布，新增实验性 loaded node linker、锁文件记录解析设置，并加快缓存 registry 元数据读取；同时包含多项安全修复，例如阻止依赖版本通过路径穿越在全局虚拟存储之外写文件，并修复安装、脚本、配置、更新/审计/发布与输出等问题。

- 🧪 新增实验性 `nodeLinker: { type: loaded }`：兼容依赖通过自动注册的 Node.js loader 直接从内容寻址存储加载。
- 📦 `nodeLinker.excluded` 可选择包及其依赖树安装到全局虚拟存储。
- 🔒 `lockfile.includeResolutionSettings: true` 让 `pnpm-lock.yaml` 记录 `autoDedupe`、`dedupeInjectedDeps`、`dedupePeerDependents`、`linkWorkspacePackages`；记录其他值的锁文件视为过期。记录 `autoDedupe` 的锁文件可在不同机器复用，`pnpm run` 在 `pnpm install --frozen-lockfile` 后不再触发另一次安装。
- 🛡️ 安全：`pnpm install` 阻止带路径穿越的依赖版本写出全局虚拟存储；锁定配置依赖安装前会校验 registry，配置依赖必须来自 npm registry，锁文件不能替换 `version+integrity` 的完整性。
- 🔐 锁文件校验会检查 `variations` resolution 中的 tarball；空的 `variations` resolution 的 `name@version` 条目被拒绝；`pnpm audit signatures` 按锁文件记录的完整性验证签名，无完整性记录的包无法通过。
- 📏 `pnpm install` 和 `pnpm publish` 在读取前拒绝大于 64 MiB 的归档元数据；发布预构建 tarball 也拒绝大于 64 MiB 的 manifest 和 README。
- 🧷 两个 URL/本地路径依赖在字符 `+ # : ?` 与 `/` 不匹配时不再共用虚拟存储目录；包括用 `#` 固定的 git 依赖，目录名会加哈希后缀。
- 🙈 关于忽略项目 `.npmrc` registry 设置的警告不再打印 URL 作用域键中的用户名和密码。
- 🚫 `pnpm install` 遇到不支持协议（如 Yarn `patch:`）会以 `ERR_PNPM_UNSUPPORTED_PROTOCOL` 失败；读取无效 `package.json` 会指出文件名。
- ❗ 依赖 specifier 非字符串（如 `"is-positive": 42`）会以 `ERR_PNPM_PACKAGE_MANIFEST_INVALID_ATTRIBUTE` 失败；此前会被静默漏出锁文件，`readPackage` 钩子仍可修正。
- 🔧 修复可执行文件父目录含悬空符号链接时的 `ERR_PNPM_CMD_SHIM_RESOLVE_PATH`；`--frozen-lockfile` 不再因自定义 fetcher 的 resolution 形状不匹配失败。
- 🩹 `pnpm install --fix-lockfile` 可修复 importer 引用无 snapshot 条目的锁文件；当依赖把自身精确依赖移到旧版时，自动安装的 peer 依赖会随之移动，避免重复版本（如两份 `vue`）。
- 🔍 `pnpm dedupe` 像 `pnpm install` 一样读取精确版本依赖的 registry 元数据，避免因 `minimumReleaseAge` 导致锁文件写入不一致。
- ⚡ 依赖解析更快读取缓存 registry 元数据；元数据缓存移至 `<cache-dir>/v12/`，升级后首次安装会重新下载；损坏缓存会重下，`--offline` 时报错。
- 🧹 `pnpm cache prune` 也会清理旧版 pnpm 写在 `<cache-dir>/v11/` 的元数据缓存。
- 🌐 当 `maxSockets` 或代理限制 registry 连接时，包元数据请求不再排在 tarball 下载队列后；大型安装解析更快，`Request took` 警告更少。
- 🍎 大型 macOS workspace 中，依赖链接已存在时安装加速：保留已指向正确包的链接，不再先尝试创建。重新链接 1,000 个 workspace 项目的直接依赖从 116 ms 降至 45 ms。
- 🏃 固定不同 pnpm 版本的项目在 macOS 上启动命令约快 13 ms；直接运行固定版本二进制，不再经过 shell 脚本。
- 📉 pnpm 二进制约缩小 0.9 MB，arm64 Linux 二进制再缩小约 1 MB。
- ⌨️ `pnpm run` 在 Ctrl+C 后不再打印 `[ELIFECYCLE] Command failed ...`；退出行为遵循脚本 shell：Windows 下 cmd 报告 `-1073741510`、PowerShell 报告 `1`，Unix 下重新抛出 SIGINT。
- 🔎 `pnpm run "/<regex>/"` 支持 JavaScript 正则语法，如 lookahead/lookbehind；`/^hello:(?!b).*$/` 不再报 `ERR_PNPM_NO_SCRIPT`。
- ⚙️ `pnpm run` 和 `pnpm exec` 会把 `--config.*` 标志转发给 `verifyDepsBeforeRun` 启动的安装；Windows 子进程可再次用 `CREATE_BREAKAWAY_FROM_JOB`，pnpm 退出后继续运行。
- 🧩 空的 `nodeOptions` 会覆盖低优先级设置；脚本在 `nodeOptions` 为空时保留父环境或 `extraEnv` 的 `NODE_OPTIONS`。
- 🚦 pnpm 读取 `pnpm-workspace.yaml` 的 `failIfNoMatch`；无匹配项目时退出码 1，`--no-fail-if-no-match` 可临时关闭。
- 🧰 `pnpm config get --global` / `list --global` 及 `--location=global` 只显示全局配置；加载配置失败时会打印配置警告，如 `.npmrc` 中未设置的环境变量。
- 🔄 旧于 11.28.4 的 pnpm 11 在 `packageManager` 固定时可再次运行 pnpm 12；Windows `pnpm self-update` 替换旧 `pnpm.cmd` 时不再运行两次更新。
- 🧭 `pnpm setup` 在继承较后位置的登录 shell（如 macOS VS Code 终端）中把 `$PNPM_HOME/bin` 放到 `PATH` 最前；再次运行可更新 shell 配置块。
- 📤 `pnpm update --latest` 重写无自身操作符的范围（如 `<2.0.0`）时应用 `savePrefix`；`pnpm audit --fix` 交互选择器按 override 的 `saveExact`/`savePrefix` 风格显示补丁版本。
- 🗑️ `pnpm unpublish <pkg>@<version>` 在 registry 位于子路径（如 Gitea npm registry）时删除正确路径下的 tarball，不再把 `/npm-mirror/` 误认为 `/npm/`。
- 🧾 `devEngines` 或 `packageManager` pin 警告输出到 stderr，`pnpm cache path`、`pnpm list --json` 的 stdout 保持纯净；`nodeLinker: hoisted` 时 `pnpm list` 报告正确包路径。
- 🧭 解析错误会指出失败依赖及父包；`--reporter=ndjson` 下致命错误以带错误码的结构化记录输出；无效 git 仓库错误码为 `ERR_PNPM_INVALID_GIT_REPOSITORY`。
- 📚 `pnpm runtime --help` 和 `pnpm help runtime` 会列出 `set` 子命令及其接受的 runtime。

---

### [](https://github.com/honojs/hono/blob/v5.0.0-rc.0/docs/MIGRATION.md)

**原文标题**: [hono/docs/MIGRATION.md at v5.0.0-rc.0 · honojs/hono · GitHub](https://github.com/honojs/hono/blob/v5.0.0-rc.0/docs/MIGRATION.md)

overview summary
Hono 迁移指南汇总从 v1.6.4 到 v5.0.0-rc.0 的破坏性变更，核心包括 ESM only、运行时适配器拆分、废弃 API 清理、类型收紧，以及 Deno 改用 JSR。

- 🚀 v4.13.x→v5.0.0：hono 仅发布 ESM，移除 CommonJS；Node.js 需 22.12+，但 require('hono') 仍可用。
- 🧱 v5.0.0：非 Error 抛出会进入 onError（默认 500）并包装为 Error，原值在 err.cause，不再从 app.fetch() 外泄。
- 🎨 v5.0.0：移除 getColorEnabledAsync()，改用 getColorEnabled()；Cloudflare Workers 需传入 c.env。
- 🔍 v5.0.0：c.req.query()/queries() 可能返回 undefined；c.req.json() 返回 unknown；c.json() 对不可 JSON 序列化值抛 TypeError。
- 📦 v5.0.0：运行时适配器移至 @hono/* 包；hono/cloudflare-pages 移除；hono/adapter 保留。
- 🗑️ v5.0.0：移除多项废弃功能，如 app.fire/mount、req.matchedRoutes/routePath、Bearer Auth 消息选项、serveStatic pathResolve、SSG hooks/常量、timingSafeEqual、getQueryStrings、UnOfficalStatusCode。
- 🌐 v4.3.11→v4.4.0：Deno 不再从 deno.land/x 发布，改用 JSR：import { Hono } from 'jsr:@hono/hono'。
- 🧹 v3.12.x→v4.0.0：大量废弃清理，如 hono/nextjs→hono/vercel、c.jsonT→c.json、c.stream/streamText→hono/streaming、c.env→getRuntimeKey、app.handleEvent→app.fetch、req.cookie→hono/cookie。
- ☁️ v3.12.x→v4.0.0：Cloudflare Workers serveStatic 需 manifest；JSX docType 默认 true；FC 不传 children，用 PropsWithChildren；部分 MIME 移除。
- 🧭 v2.7.8→v3.0.0：c.req 变为 HonoRequest，访问原始 Request 用 c.req.raw；StaticRouter 废弃；Validator 变更；serveStatic 由适配器提供；new Hono 泛型必须用 type。
- ✅ v2.7.1→v2.x.x：当前 Validator Middleware 弃用，建议改用 Zod、TypeBox 等第三方验证库。
- 🔐 v2.2.5→v2.3.0：Basic/Bearer Auth 嵌套使用时改为 return auth(c, next)，不再使用 await auth(c, next)。
- 📥 v2.0.9→v2.1.0：c.req.parseBody 不再解析 JSON/text/ArrayBuffer，仅解析 multipart/form 或 urlencoded；new Hono 泛型改为 Variables/Bindings。
- 🍪 v1.6.4→v2.0.0：Deno 中间件改从 hono/middleware.ts 导入；cookie、body-parse、graphql-server、mustache 中间件废弃，cookie 与 c.req.parseBody() 成为默认能力。

---

### [发布 v10.1.0 · sindresorhus/execa · GitHub](https://github.com/sindresorhus/execa/releases/tag/v10.1.0)

**原文标题**: [Release v10.1.0 · sindresorhus/execa · GitHub](https://github.com/sindresorhus/execa/releases/tag/v10.1.0)

execa v10.1.0 由 sindresorhus 于 10 月 6 日发布，为最新版本；本次更新以行为变更和多项修复为主，行为变更本质是 bug 修复，但可能影响依赖旧错误行为的代码。

- 🚀 v10.1.0 是最新版本，提交号为 `63ddae6`，对比 `v10.0.1...v10.1.0`，包含 2 个资源。
- ⚠️ 行为变更可能影响代码：`extendEnv: false` 且未提供 `env` 时，不再继承 `process.env`。
- 🪟 Windows 上 `.cmd` 和 `.bat` 文件参数改为类似 Rust 的转义方式，修复批处理读取 `%~1`。
- 🚫 非法 `stdio` 值（如负文件描述符）现在会抛错；输入和输出为同一文件也会抛错，即使路径写法不同。
- 📏 同步方法现在强制按文件描述符执行 `maxBuffer`，并在 `signal` 选项下抛错，同时像异步方法一样写入原始输出字节。
- 🛠️ 修复 `subprocess.kill()` 在子进程启动失败时误向当前进程组发信号，以及 spawn 失败或文件目标无法打开时的崩溃。
- 🧯 修复同步方法启动失败时 `error.stdout` 和 `error.stderr` 为 `undefined`。
- ⏳ 修复子进程 Promise 因输出流未读取而挂起，以及 `subprocess.pipe()` 与 `stdio` 选项、目标子进程残留运行的问题。
- 📊 修复 `result.all` 在仅部分文件描述符被缓冲或按行拆分时的问题，以及 transforms 中的 `encoding` 和行拆分。
- 🔄 修复同步方法的输入/输出 transforms，以及含 emoji 和续行的模板字符串。
- 🌐 修复 Windows 上 `killDescendants` 误伤无关进程；修复 IPC 在 `serialization: 'json'`、`strict: true` 和 `verbose` 选项下的问题。
- 📂 修复当前目录被删除时子进程错误被隐藏，以及 Windows 上小型文件的 shebang 脚本问题。

---

### [Effect 4.0 | Effect 博客](https://effect.website/blog/releases/effect/40)

**原文标题**: [Effect 4.0 | Effect Blog](https://effect.website/blog/releases/effect/40)

Effect 4.0 正式发布，这是该项目迄今最雄心勃勃的版本，从底层完全重建，带来显著的性能提升、零依赖核心、更小的打包体积以及长期支持承诺，标志着 Effect 从单一函数工具演进为覆盖分布式系统的完整编程模型。

- 🚀 **性能飞跃**：Effect 4.0 相比 3.x 实现 5 倍更小的打包体积（最小程序从 35.6 kB 降至 7.1 kB）、6.4 倍并发任务吞吐量（每秒 4.57M 任务）、每个 fiber 内存占用减少 86%（5 万个 fiber 从 157.5 MB 降至 21.8 MB）。

- 📦 **零依赖核心**：`effect` 核心包不再有任何运行时依赖，许多原本独立的包现已整合其中，共享统一版本同步发布，有效降低供应链攻击风险。

- 🏗️ **全栈覆盖**：Effect 从最初的单一函数作用域，扩展至涵盖类型化错误、依赖注入、资源管理、结构化并发和可观测性，并进一步提供持久化工作流和集群等分布式系统高级原语，所有层级共享同一编程模型和保证。

- 📈 **主流采用**：Effect 已在各类规模企业生产环境中运行，每周 npm 下载量达 4390 万次，自 3.x 以来增长 179 倍，4.x 采用率已达 56%，超过 3.x 的 44%；围绕其生态还涌现出 Alchemy（云基础设施）和 Foldkit（前端）等社区项目。

- 🛡️ **长期支持**：从本版本起，每个 Effect 主版本均享有 LTS 政策。4.x 的 bug 修复支持至 2029 年 9 月或 5.0 发布后一年（取较晚者），安全修复支持至 2029 年 9 月或 5.0 发布后两年（取较晚者），最短支持周期为三年。

- 🔧 **后续计划**：首要任务是稳定生态系统中仍标记为 unstable 或 experimental 的新模块，通过生产反馈将其提升为稳定状态；同时继续扩展 Effect 成为整个应用统一的编程模型，提供更广泛的原生平台支持和更多高级原语。

- 🤝 **迁移与社区**：迁移可参考迁移指南，交由编码代理即可完成大部分工作；官方感谢所有贡献者、测试者和社区成员，并邀请大家在 X、Bluesky 和 Discord 上共同庆祝。

---

### [发布 v4.7.10 · handlebars-lang/handlebars.js · GitHub](https://github.com/handlebars-lang/handlebars.js/releases/tag/v4.7.10)

**原文标题**: [Release v4.7.10 · handlebars-lang/handlebars.js · GitHub](https://github.com/handlebars-lang/handlebars.js/releases/tag/v4.7.10)

v4.7.10 是 Handlebars.js 的最新发布版本，由 jaylinski 于 05 Oct 23:07 发布；自该版本以来 master 已有 251 次提交。仓库当前有 75 个 Issue、38 个 PR、11 个安全与质量项。本次发布以安全修复为主，并包含兼容性、文档和依赖更新。

- 🚀 v4.7.10 为最新版本，发布于 10 月 5 日 23:07，包含 251 次 master 提交。
- 🔐 安全：压缩时清理 source map URL。
- ⚡ 安全：在 {{#each}} 中惰性迭代，并以线性时间去除空白。
- 🛡️ 安全：预编译输出中转义 <!-- 和 <script（GHSA-xw65-4hp5-5hc7）。
- 🧷 安全：不信任上下文数据上的特殊属性（GHSA-p8wg-vrv2-v86f）。
- 📦 安全：仅编译模板字符串形式的 partial。
- 🧭 安全：编译器和访问器仅分发已知节点类型。
- ✅ 安全：在编译器中验证 AST 值，而非解析器中（GHSA-8r5x-fm3f-whwj）。
- 📝 文档：澄清 --root 不限制文件系统访问。
- ⬆️ 依赖：将 minimist 升级到 ^1.2.8。
- 📚 文档：修复 Ruby 组件发布文档；修复 Composer 组件定义。
- ⚠️ 兼容性：{{#each}} 会像 for...of 一样惰性遍历 Map、Set、生成器等可迭代对象，不再先复制为数组；渲染期间新增的值也会被访问。
- 📦 发布资产：2 个 Assets；获得 1 个 🚀 反应。

---

### [](https://github.com/mathiasbynens/he)

**原文标题**: [GitHub - mathiasbynens/he: A robust HTML entity encoder/decoder written in JavaScript. · GitHub](https://github.com/mathiasbynens/he)

he 是一个用 JavaScript 编写的健壮 HTML 实体编码/解码库，支持所有标准化命名字符引用，能像浏览器一样处理歧义与边缘情况，并良好支持星体 Unicode 符号。
- 📦 可通过 npm 安装：`npm install he`，以 ECMAScript 模块提供 `decode`、`encode`、`escape`、`unescape` 等命名导出。
- 🔤 `he.encode(text, options)` 默认编码非可打印 ASCII 及 `&`、`<`、`>`、`"`、`'`、`` ` `` 等符号，默认使用十六进制字符引用。
- ⚙️ `encode` 支持 `useNamedReferences`、`decimal`、`encodeEverything`、`strict`、`allowUnsafeSymbols` 等选项，并可通过 `he.encode.options` 全局覆盖默认值。
- 🔁 `he.decode(html, options)` 按 HTML 规范算法解码命名和数字字符引用，支持 `isAttributeValue`、`strict` 选项，并可通过 `he.decode.options` 全局覆盖。
- 🛡️ `he.escape(text)` 仅转义 XML/HTML 文本上下文中的 `&`、`<`、`>`、`"`、`'`、`` ` ``；`he.unescape` 是 `he.decode` 的别名。
- 🖥️ 提供 CLI：全局安装后可用 `he --encode`、`he --decode`、`--use-named-refs` 等，支持文件与管道输入输出。
- ✅ 拥有广泛测试套件，支持现代浏览器和 Node.js v22+，属于 ES2022 模块；CLI 也要求 Node.js v22+。
- 🛠️ 开发命令包括 `npm test`、`npm run coverage`、`npm run build`、`npm run fetch`、`npm run format`。
- 📜 项目由 Mathias Bynens 创作，采用 MIT 许可证；仓库约有 3.6k stars、264 forks、57 watchers。

---

### [GitHub - Agent-Field/CodeAF：面向开放模型的开源软件工厂 · GitHub](https://github.com/Agent-Field/CodeAF)

**原文标题**: [GitHub - Agent-Field/CodeAF: Open-Source Software factory for Open Models · GitHub](https://github.com/Agent-Field/CodeAF)

CodeAF 是 AgentField AI 推出的开源软件工厂与编码 harness，面向开放模型，目标是用更低成本获得前沿级编码能力。它采用 Go 单二进制、Apache 2.0 许可，当前为早期预览版；核心是用一个窗口管理所有项目、任务、子 harness、模型分工、无头运行与远程开发。

- 📦 安装简单：`curl -fsSL https://agentfield.ai/get/codeaf | bash` 后运行 `codeaf`；可固定版本或源码构建；支持 OpenRouter、Codex ChatGPT 计划、DeepSeek、GLM、Kimi、MiniMax、Qwen、Ollama 及 OpenAI 兼容端点。
- 🏆 基准领先：在 DeepSWE 同一模型上，十款编码 harness 中排名第一，领先 Claude Code、Codex、OpenCode、Kilo 和 DeepSeek 自家 harness，且每个已解决 issue 成本最低。
- 🏭 工厂定位：自动完成调度、拆分、检查与合并，只在必要时询问；问题统一进入 `needs you`，其他事项自行决策、记录并继续。
- 🪟 一个窗口：`home` 列出机器上所有项目与对话；`enter` 打开标签，`tab` 切换，`alt+k` 跳转；每个项目可独立设置审批规则、模型与消费限额。
- 🗣️ 对话转任务：一条消息可拆成多个任务，分别在独立仓库副本和分支运行；通过检查的工作自动落到你的分支，不碰 `main`、`dev` 或发布分支；未通过/未检查项进入 `unread`。
- 🛠️ 子 harness：为 PR 审查、修 issue、依赖审计等固定任务打造专家；PR-AF 即将原生推出，`/senior-dev` 已可用；也可用自然语言生成自定义 harness。
- 📊 `/senior-dev` 基准：在 DeepSeek V4 Flash 上与九款 harness 对比，使用 DeepSWE 的 113 个真实 GitHub issue 和官方验证器，解决最多且单题成本最低。
- 👥 多模型班组：一次会话多模型；座位包括 worker、planner、checker；默认 `auto`，按 Pareto Crewing 评分选型；`/crew` 可查看、固定、限制开放模型，`/task --best/--cheap` 可调整单任务。
- 💸 成本控制：每任务默认 $5 限额，可设日限额；`/redo stronger` 可升级重跑；模型池默认开启，仅发送去文本化、匿名、按安装 nonce 的计算指标，不发送代码、提示、路径或身份。
- 📌 常设指令：规则、提醒、监控可用自然语言设定，如禁止直推 `main`、每周草稿、CI 变红通知；按项目或全局生效，并共享日消费限额。
- 🤖 无头模式：面向 CI、cron、脚本和基准；`codeaf do "简报" --timeout 30m --json` 输出 JSON 与退出码；`exec` 运行无规划 worker，`run` 执行编辑过的计划。
- 🖥️ 远程开发：屏幕在本地，对话在工作机器；`codeaf chat --host devbox` 走自有 ssh，输入不等待网络，断线重连 5 分钟，文件双向传输，手机终端可加入同一会话。
- ⚖️ 与 copilot 区别：copilot 管一个窗口/一个仓库、你盯它输入；CodeAF 管整机所有项目、你描述工作并决定什么落地，任务和常设指令可跨窗口持续，且可无头/手机运行。
- ⚡ 性能突出：单个 Go 二进制仅 53 MB，最高比对手小 21 倍；每新增会话 RAM 27 MB，16 个空闲会话 507 MB，单轮峰值 122 MB，恢复 50 轮会话 145 ms。
- 📚 文档与许可：内置 `codeaf manual`，涵盖指南、架构、无头、远程、限制；Apache-2.0；仓库约 355 stars、46 forks、254 issues、15 PRs、3166 commits。
- 🔐 遥测透明：默认发送匿名使用计数；不发送提示、代码、文件名、路径、仓库名、密钥、邮箱、IP、机器名或模型名；可用 `/settings`、`CODEAF_TELEMETRY=off` 或 `DO_NOT_TRACK=1` 关闭。

---

### [](https://fingerprint.com/use-cases/new-account-fraud-prevention/?utm_source=NodeWeekly09242026)

**原文标题**: [New Account Fraud Detection and Prevention | Fingerprint Device Intelligence](https://fingerprint.com/use-cases/new-account-fraud-prevention/?utm_source=NodeWeekly09242026)

打击激励滥用，识别并制止那些利用推荐奖励、欢迎优惠和营销活动牟利的欺诈者。

- 🛑 阻止激励滥用行为
- 🕵️ 识别刷取推荐奖金的欺诈者
- 🎁 防范欢迎优惠被恶意套取
- 📣 警惕营销促销被滥用牟利

---

### [](https://newgtldprogram.icann.org/en/application-rounds/round2)

**原文标题**: [New gTLD Program: 2026 Round | New gTLD Program](https://newgtldprogram.icann.org/en/application-rounds/round2)

2026轮新通用顶级域（New gTLD）项目是应ICANN全球多利益相关方社区请求而制定，依据社区多年形成的政策建议，其实施催生了申请指南中的流程、规则与要求，并决定项目关键里程碑的时间安排；2012轮的历史信息可供参考。
- 📘 申请指南（AGB）：与实施审查团队协作制定，最终版于2025年12月发布。
- 🛤️ 申请人之旅：展示申请从准备到可能授权的各阶段，并解释每个阶段的事件与评估。
- 📜 2026轮基础注册协议：成功申请人在新gTLD授权前与ICANN签订的预期注册协议形式。
- 🎓 2026轮资源：为申请人及社区成员提供培训和资源，帮助其完成申请与评估流程。
- ❓ 2026轮常见问题：列出常见问题及ICANN的回应。
- 📊 申请发布与统计（APS）：提供2026轮申请信息，包括项目统计、申请公开部分、争议集、异议与上诉。
- 🌐 2012轮历史信息：可查阅上一轮新gTLD项目的参考资料。

---

### [](https://gtlds.fyi/)

**原文标题**: [gtlds.fyi — New gTLD applications](https://gtlds.fyi/)

当前未收到需要总结的文本，因此无法生成文章摘要。请提供具体内容后，我将按模板输出中文要点总结。

- 📄 未检测到可总结的文章或文本内容。
- ✍️ 请粘贴需要总结的内容。
- 🧭 收到后我会提炼关键信息并保留核心细节。
- 🗂️ 输出格式：概览摘要 + emoji 项目符号。
- 🌐 全部使用中文。

---

### [](https://bsky.app/profile/sindresorhus.com/post/3mwtgzhv7uk2t)

**原文标题**: [@sindresorhus.com on Bluesky](https://bsky.app/profile/sindresorhus.com/post/3mwtgzhv7uk2t)

Sindre Sorhus 宣布，由于 AI 的影响，他已禁用所有代码仓库的外部拉取请求；他感叹传统开源时代已经结束，但仍会继续维护项目和处理问题。

- 🤖 因 AI，Sindre Sorhus 关闭了所有仓库的外部 PR。
- 🕰️ 他认为人们熟悉的开源模式已走到尽头，对他而言已持续 15 年。
- 🛠️ 他仍会继续维护项目并处理 issue。
- 📅 该声明发布于 2026-10-01 的 Bluesky 帖子。

---

### [获取失败](https://lemire.me/blog/2026/10/06/linking-node-js-with-mold/)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/10/06/linking-node-js-with-mold/)

无法总结：获取内容失败，状态码 202。

---

### [](https://github.com/pingdotgg/ts-rust)

**原文标题**: [GitHub - pingdotgg/ts-rust: An experimental Rust port of the TypeScript 7 compiler (tsc) · GitHub](https://github.com/pingdotgg/ts-rust)

pingdotgg/ts-rust（tsc-rs）是一个由 LLM 生成代码、用 Rust 重写 TypeScript 7 编译器的实验项目，目标是做快速类型检查器并支持高性能 WASM。它移植 Microsoft 原生 Go 版 TypeScript 编译器，保持相同 CLI、语言服务器和 API，当前为早期版本，已有 698 stars、43 forks、6038 commits，采用 MIT 许可。

- 📌 仓库概况：公开仓库 pingdotgg/ts-rust，698 stars，43 forks，6 issues，3 PR，6,038 commits，MIT。
- 🦀 项目性质：Microsoft 原生 TypeScript 编译器（Go 编写，原 typescript-go）的直接 Rust 移植，保留 Go 算法与行为，提供相同 tsc CLI、语言服务器和 API。
- 🎯 动机：测试 LLM 能力、做快速 TS 类型检查器、做可高性能运行在 WASM 的检查器，以及 Memes。
- ⚠️ 警告：早期版本；在测试过的真实项目中 100% 兼容，可作为大多数应用 drop-in 替代，但存在已知问题；作者称自己从未读过一行代码。
- 📦 安装与平台：`npm install -D tsc-rs`，`npx tsc-rs -p tsconfig.json`；npm 包名为 tsc-rs 以避免与 typescript 冲突。支持 Linux x64 静态版和 macOS arm64；Windows 与 Linux arm64 尚未支持。
- 🧪 Effect 诊断：内置 Effect 语言服务诊断（377xxx），tsconfig 配 `@effect/language-service` 插件时运行；规则、选项和 `@effect-diagnostics` 注释移植自 Effect-TS/tsgo 0.46.1；编辑器功能未移植。
- 💰 LLM 成本：OpenAI 模型花费超 40 万美元 token，写 130 万+ 行 Rust，未过 84% 兼容；Claude Opus 5.5 从零开始 10 小时出 v0，后期两周 API 约 2.4 万美元，达 $200 周计划限额的 925%–983%。总 token 成本超 42 万美元，但可能约 2 万美元即可完成。
- 🔖 上游版本：固定在 microsoft/TypeScript 673a5f17d713（2026-09-29，TypeScript 7.1.0-dev）；比较应使用 `typescript@7.1.0-dev.20260929.1`。
- ✅ 正确性：TanStack Query core 和 Hono 诊断与 Go 相同；181,711 个移植的 Go 测试全部通过；语言服务器和 API 在 oracle 测试集上与 Go 一致。
- ⚡ 性能：60 个开源项目上类型检查时间约为 Go 版一半（几何平均）；CI 预览包无 PGO/BOLT，因此比实测构建更慢。
- 📊 T3 Code 基准：无 Effect 诊断时 bun check 4.07s、tsc-rs 7.25s、tsc 7 16.10s、tsc 6 62.63s；带 Effect 诊断时 tsc-rs 内置 11.13s，tsc 7+@effect/tsgo 21.07s，bun check+effect 37.60s，tsc 6+@effect/language-service 138.63s；三者报告相同 221 条 Effect 诊断。
- 📊 真实应用基准：六个开源应用几何平均相对 tsc 6 加速：tsc 7 7.1×，tsc-rs 11.4×，bun check 20.9×；相对 tsc 7，tsc-rs 快 1.61×，bun check 快 2.95×。bun check 除 tRPC 外最快，但会报告其他检查器没有的错误（Sentry 3、tRPC 2）。tsc-rs 在 VS Code 报 10 错、Sentry 报 2 错，与 TypeScript 7.1.0-dev 一致。
- 🧪 测量与适配：Apple M4 Pro（12 核/48GB）、macOS 26.5.1、hyperfine 5 次中位数、`--noEmit --incremental false`、默认线程数；tsc 6 用 Node 24.19 与 16GB 堆。四个应用需小改才能在 tsc 7 下 0 错误：Excalidraw 去 baseUrl，TypeORM 改 nodenext，VS Code 加 electron 类型，Playwright 用生成源码。rxjs、date-fns 未列入。
- 🐛 已知问题：monorepo 中同一源文件可经 node_modules 和直接导入到达时，tsc-rs 可能写更多文件并报 TS6059；结果稳定，而 tsc 因计时会变。`tsc -b` 中若项目导入另一项目输出但无 project reference，可能读到旧/缺失输出（TS2305/TS2307），加 reference 可修复。
- 🧠 编辑器内存：长时间编辑会话内存缓慢增长（约 20 MiB/1000 次编辑），起始比 tsc 高 12–24%，约 20 次编辑后在测量会话中低于 tsc（最多 2,190 次）。
- 🏷️ 版本：`tsc-rs --version` 打印所移植的 TypeScript 版本 7.1.0-dev，而非 npm 版本；编译器据此匹配 typesVersions。
- 🛠️ 开发结构：`crates/ts_goport` 是编译器，含 `goport_util`、`goport_lsproto` 于 `crates/ts_goport/parts`，lib 文件在 `crates/ts_goport/libs`；`tools/ts_ast_codegen` 生成 astdata，`tools/ts_diagnostics_codegen` 生成 diagnostics/catalog.rs 与 diag.rs；`crates/ts_wasm` 是 WASM 构建（npm/wasm）。
- 🔨 构建/测试：`./scripts/run-cargo-capped.sh build --release -p ts_goport --bins`；`./scripts/verify.sh`；二进制为 goport（类型检查）与 tsgo（Go tsgo 命令行）；Go 基线测试用 `TS_GO_REPO=/path/to/typescript-go ./scripts/run-cargo-capped.sh test -p ts_goport --test go_baselines`。规则见 PORTING.md、AGENTS.md、docs/history.md 等。
- 🚀 发布与许可：推送 `v<version>` 标签触发 release workflow，构建、打包、测试、发布 npm 和 GitHub release；稳定版到 latest，预发布版到 next。MIT 许可，保留 TypeScript Apache-2.0 与 Go 标准库部分 BSD-3-Clause，见 NOTICE.md。

---

### [](https://survey.stackoverflow.co/2026)

**原文标题**: [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026)

第16届 Stack Overflow 年度开发者调查覆盖169个国家/地区的30,903名技术人员，围绕工作、AI、技术、社区与知识五大类展开，核心问题是“你最近怎么样？”
- 🌍 调查涵盖103个问题、467项技术，汇集了全球开发者与技术人员的广泛反馈。
- 😟 工作满意度下降：45%对工作平淡/自满，33%不开心，仅22%开心。
- 🚀 自由职业/自雇比例从3.9%跃升至10.5%，越来越多人转向独立工作。
- 🤖 AI使用激增：80%每天至少使用AI一小时，62%对AI工具持好感。
- 🔐 对AI输出的信任从31%升至87%，但48%只在可验证时才信任。
- 📚 93%认为AI回答需引用来源；AI采用关键因素包括准确结果、安全隐私、价格与合规。
- 🐍 AI用途中Python领先（39%），随后是JavaScript（38%）、HTML/CSS（33%）、SQL（30%）。
- 🧑‍💻 16年以上经验者中，SQL（63%）和JavaScript（62%）最常用。
- 🛠️ 仅19%自建工具替代供应商，但其中超过一半使用AI工具辅助。
- 🔎 社区找答案：82.7%用在线搜索，69.9%问AI代理，43.7%查已知仓库，28.8%问信任的人。
- 💼 工作问题来源仍偏人类：同事/队友72%，代码与注释63%，内部文档/维基60%。
- 📉 64%因AI少访问Stack Overflow简单问题，29%整体少提问，27%少贡献。
- 🧠 上下文挑战突出：63%遇信息不完整，61%关键信息只在人脑，56%信息过时，53%分散在太多工具。
- ⏳ 约79%开发者常在做完任务后才发现重要上下文，75%花5小时以上寻找答案。
- 🎯 AI代理最需要的上下文：项目目标/需求85%、代码/文档73%、过往决策44%、相关工单37%。

---

