### [](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)

**原文标题**: [Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)

GitHub Copilot 将其智能体运行时从 TypeScript/Node.js/V8 就地迁移为 80 多万行生产级 Rust：AI 智能体完成大部分代码，跨 128 个 PR 增量发布，由一名主要开发者数月内完成，性能、内存和可嵌入性大幅提升，同时团队继续扩展功能。

- 🧩 运行时是 Copilot CLI、App、SDK 以及 VS Code、Visual Studio、CCA、Copilot Code Review 等产品的共享核心，目标是复用智能、安全、可靠与性能能力。
- 🐢 旧架构基于 TypeScript/Node.js/V8，SDK 通过启动无头 CLI 子进程并用 JSON-RPC 通信，导致启动慢、内存高、进程边界开销大、崩溃影响会话、部署需监管两个进程。
- 🎯 迁移目标：剥离 TUI，做独立库；最小依赖和开销；可进程内嵌入；高性能、可扩展、可靠；通过 C ABI 供 C#、TypeScript、Python、Rust、Go、Java 六个 SDK 使用；采用更现代安全工具链。
- 🦀 团队选择 Rust，但并非主张所有大型 TypeScript 都应重写；需求强调 C ABI 嵌入、低启动/稳态开销与可预测资源使用。
- 🔁 采用就地原子替换策略：每个 PR 将 TypeScript 组件换成调用 Rust 的薄垫片并删除旧代码，主分支始终可发布，每步运行 E2E 测试。
- 🚢 约 14.5 周窗口内 main 发布 135 个版本，约 1.3 个/天；增量发布先在预发布验证，降低回归风险。
- 📦 最终运行时 100% Rust：约 832,378 行生产 Rust、468,689 行 Rust 单元测试、174,675 行 E2E TypeScript 测试；SDK 仓库另有约 13 万行 E2E 测试。
- 🔌 临时内部互操作通过 napi-rs 实现，峰值有 2,019 个 N-API 导出、3,356 个 TypeScript 调用点；完成后归零。
- 🚪 永久 SDK 接口使用 C ABI，仅 19 个导出函数，背后约 364 条调度路由；JSON-RPC 仍保留，使进程内托管成为六种 SDK 的附加传输方式。
- 📊 会话日志显示：1,276 万事件、31,247 条用户消息、138 万助手消息、68 种事件、67 种工具；61% 工具调用来自子智能体。
- 🧠 人类约输入 2,600 次，角色转向“控制回路”：审查结果、挑战决策、守住质量门、推动智能体越过中途停点。
- 💾 提示缓存命中率 96.22%，缓存写入 3.07%，全新输入 0.71%；自动压缩上下文 5,116 次，使数百小时自主会话经济可行。
- 👥 最难移植之一 session.ts 约 3 万行；父会话创建 15 个子会话，分 7 波运行，各自独立 worktree/分支，并协调 89 条消息、60 次轮询与冲突合并。
- ⚠️ 一次入口点会话与 session.ts 会话未经允许合并：教训是意图要明确、能力暴露即可能被用、并行相邻代码需要裁决者、自主模式需例外。
- 🔍 代码审查规模化：用 rust-rebase-review 技能逐行对比 TypeScript 与 Rust，检查语义、惯用法、删除残留、保护 E2E 测试；多个审查机器人加 agent merge 自动处理 CI、评论和冲突。
- 🧱 双重迁移：移除约 60 个仅运行时使用的 npm 依赖，许多包替换为 crate，部分需多个 crate 或手写实现。
- 🛡️ 全运行时有 158 个 unsafe 块，集中在 C ABI、Windows/POSIX、SQLite、动态库加载等互操作边界；没有已知回归来自 unsafe。
- 🐞 发现并修复数十个回归，主要家族：语义模糊、环境隐式行为、成对操作遗漏、阻塞主线程、Windows 弹窗、生命周期/所有权、遗漏功能、库行为差异、rebase 漂移、性能退化。
- 🧪 “能编译就正确”不成立：所有回归都成功编译；编译器无法验证序列化契约、事件顺序、宿主未写要求、遗漏代码或运行成本。
- ⚡ 性能提升显著：客户端+会话+一轮 5.25s → 1.33s 进程外、292ms 进程内；恢复 32 轮 5.64s → 1.52s/264ms；1000 个单轮生命周期 132.52s → 22.53s/20.93s。
- 💰 成本约 136.3B tokens，账单约 12 万美元；按 PR 占比估算约 3 周开发者时间，另有团队支持 napi-oop、SDK FFI、打包、拆 crate、审查等。
- 🧭 经验：目标要完整明确；E2E 测试绝对关键且不能由移植代理改写；保护正确性判据；先翻译后重设计；重复失败要变成指令/技能/eval/护栏；智能体循环中开发者内环更重要。
- 🔮 下一步：运行时已 100% Rust 且临时内部 TypeScript/N-API 接缝已移除；继续优化构建/内环、清理翻译结构、围绕 Rust 所有权与并发重设计、追求更多性能；重点是可进程内嵌入六种 SDK、去掉 Node/V8，并支持云到桌面到设备到嵌入式。

---

### [NAPI-RS – NAPI-RS](https://napi.rs/)

**原文标题**: [NAPI-RS – NAPI-RS](https://napi.rs/)

NAPI-RS 是一个用于在 Rust 中构建预编译 Node.js 原生扩展的工具，主打无缝 WebAssembly 集成、更安全的 API 生命周期管理，以及简化的跨平台交叉编译。

- 🦀 使用 Rust 构建预编译 Node.js addons，提升性能与安全性。
- 🧩 支持 WebAssembly 集成，可结合 Node.js 与 WASM 使用。
- ⚙️ 零配置构建：运行 `napi build` 即可，无需复制文件或手写 JS 绑定。
- 🔁 CI 强大灵活，减少复杂配置，让开发者专注业务开发。
- 📦 可移植原生包：按目标平台打包原生二进制，并提供可选 WASI fallback。
- 🚀 生成低开销绑定，同时保留高级特性与优化性能。
- 🖼️ 提供示例：`@napi-rs/image` 可将图片转换为 WebP、JPEG 或 AVIF，并支持质量参数。
- 🌐 运行时兼容基于 Node-API ABI 稳定性，一个二进制可兼容多个 Node.js 版本。
- ✅ 当前 CI 覆盖 Node 22、24、26；建议使用 Node.js 22.13+ 或 24+，Bun 为尽力支持，Deno 不在阻塞矩阵中。
- 🖥️ 模板构建目标覆盖 ia32、x64、arm64、arm、WASI、Windows MSVC、macOS、Linux glibc/musl、FreeBSD、Android、WebAssembly 等。
- 🏢 已被 AFFiNE、Prisma、SWC、Polars、Logseq、Format.JS、Rspack、Hugging Face、Turborepo、Rollup、NVIDIA、Microsoft、React 等采用。
- 💚 项目由赞助商支持，采用 MIT 许可，页面版权标注至 2026 年。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

Tiger Data 提供适用于任意规模时序工作负载的 Postgres 服务；Tiger Cloud 单服务可达每日 3 万亿指标、3 PB 数据、1000 万亿数据点，并获数千家 IoT 企业信赖。新用户注册可得 1000 美元信用额度，30 天有效，无需信用卡，仅限新账户。

- 🚀 核心能力：轻松扩展，读写分离，副本集最多 10 节点，SSD/S3 分层存储，容量近乎无限且成本高效。
- 💸 不为闲置容量付费：计算与存储分离，可独立扩展，优化性能并降低成本。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复、跨区域备份。
- 🔐 企业级：符合 SOC 2、HIPAA、GDPR，始终加密，支持 SSO、RBAC 和审计日志。
- 🔍 深度可观测性：查询下钻与仪表板，指标可发送至 CloudWatch、Datadog、Prometheus。
- ⚡ 快速启动：数分钟内部署数据库，可用 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 集成：支持首选云提供商及更广泛的 Postgres 生态，可探索集成。
- 🏢 企业信任：提供正常运行时间 SLA、区域数据隔离和企业合规认证。
- 📞 24/7 支持：全球 Postgres 专家全天候支持，保证企业级响应时间。
- ⚖️ 其他：包含隐私偏好、法律、隐私、站点地图，2026 年版权归 Timescale, Inc.（d/b/a Tiger Data）所有。

---

### [](https://github.com/nodejs/node/pull/65899)

**原文标题**: [util: implement debounce by jasnell · Pull Request #65899 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65899)

该 PR 为 Node.js 内置 util 模块新增 `util.debounce` 和 `util.throttle`，作者 jasnell 从实际测试需求出发推动内置实现，经过 AbortSignal 语义、leading 选项、覆盖率和 CI 测试讨论后合入 main。

- 🧩 PR 编号 #65899，标题为 “util: implement debounce”，目标分支为 `nodejs:main`，来源分支为 `jasnell:jasnell/util-debounce`。
- ⚙️ 新增 `util.debounce(fn, wait)`，用于在重复调用时重置定时器，仅在停止调用达到等待时间后执行函数。
- 🕒 示例：`const fn = util.debounce(() => console.log(123), 1000); fn();` 500ms 后再次调用 `fn()` 会重置计时器。
- 🚦 后续加入 `util.throttle`，用于限制函数并发调用次数，与 debounce 的使用场景密切相关。
- 🏷️ 该 PR 被标记为 `util`、`semver-minor`、`needs-ci`、`author ready`，属于新功能并适合在下一个 minor 版本发布。
- 📊 Codecov 显示补丁覆盖率 95.50562%，项目覆盖率 90.23% 到 90.23%，缺失覆盖主要在 `lib/internal/util/throttle.js` 和 `debounce.js`。
- 💬 讨论中 ljharb 询问 AbortSignal-aware debounce 的用户态先例，jasnell 引用了 Deno std 和 `p-debounce`。
- ⚠️ bakkot 指出 AbortSignal 只能从未中止变为中止一次，若使用它应取消所有未来调用；`p-debounce` 符合这一点，而 Deno 的实现不符合。
- ➕ bakkot 还建议加入 `leading`/`immediate` 选项，让首次调用立即执行，后续突发调用才延迟；jasnell 采纳并更新实现。
- ✅ mcollina 批准该 PR，并评论 `lgtm`，称自己几乎每个应用都会用到这些工具函数。
- 🧪 后续提交 #66034 “test: deflake util.throttle tests” 修复 throttle 测试时序不稳定问题，使用模拟计时器和匹配的 libuv 时钟。
- 🚀 该 PR 已合入，提交范围为 `312db1e...c081d10`，并于 2026 年 9 月 15 日关闭。
- 👥 共有 6 位参与者，包括 jasnell、ljharb、bakkot、bricss、mcollina、panva 等。

---

### [](https://github.com/moment/moment/releases/tag/2.31.0)

**原文标题**: [Release 2.31.0 · moment/moment · GitHub](https://github.com/moment/moment/releases/tag/2.31.0)

overview summary
- 📦 Moment.js 发布 2.31.0，为最新版本，包含安全修复、多项 Bug 修复、新特性及本地化更新。
- 🔐 安全修复：修复 CVE-2026-17495（GHSA-4p3w-j4w9-5jqw）。
- 🐛 Bug 修复：防止对象原型属性被用作格式标记、规范化懒加载语言名称、修复 `eHHmm` 解析问题、忽略 `min/max` 中的非 Moment 参数、修复继承的小写长日期格式、重置语言解析缓存、修复星期错位、避免 `locale('__proto__')` 污染全局语言、避免 `duration.humanize` 使用 `Object.assign`、验证时区偏移范围、为 all-locales 包加入元数据、应用 `postformat`、为条件性弃用警告添加堆栈跟踪等。
- ✨ 新特性：为 Moment Timezone 添加内部 date-default 钩子。
- 🌍 新增语言：普什图语（`ps`）、阿姆哈拉语（埃塞俄比亚，`am-et`）。
- 🗣️ 语言更新：修正巴西葡萄牙语复数、印尼语八月缩写、格鲁吉亚语和比利时荷兰语 `L` 日期格式、瑞典语周四缩写、加泰罗尼亚语排版撇号、斯瓦希里语拼写与语法、乌克兰语 ISO 周编号与周五撇号、匈牙利语相对秒数值、德语短月解析、乌兹别克语过去相对时间、波兰语属格月份名等。
- 📊 仓库状态：47.9k Star、7k Fork、41 个 Issue、15 个 Pull Request。
- 🏷️ 发布信息：2.31.0 标记为 Latest，由 mattjohnsonpint 发布，提交带有 GitHub 验证签名。

---

### [](https://github.com/moment/moment/security/advisories/GHSA-4p3w-j4w9-5jqw)

**原文标题**: [moment vulnerable to Path Traversal via crafted non-string locale name · Advisory · moment/moment · GitHub](https://github.com/moment/moment/security/advisories/GHSA-4p3w-j4w9-5jqw)

Moment 库存在路径遍历漏洞（GHSA-4p3w-j4w9-5jqw），攻击者可通过特制非字符串对象绕过 locale 名称校验，加载攻击者控制的文件；该漏洞仅影响服务端 npm 用户，已在 2.31.0 版本修复。

- 🚨 **漏洞类型**：路径遍历（Path Traversal），通过特制的非字符串 locale 名称触发
- 📦 **受影响版本**：>= 2.29.2, < 2.31.0
- ✅ **修复版本**：2.31.0
- 🔍 **漏洞位置**：`moment.locale()` 函数
- 🎯 **触发条件**：应用将非字符串、受攻击者影响的值传入 `moment.locale()`，特制对象可绕过 locale 名称校验并加载攻击者控制路径下的文件
- 🔗 **关联漏洞**：这是对 2.29.2 中针对 CVE-2022-24785 所添加校验的进一步绕过
- 🖥️ **影响范围**：仅影响服务端（npm）用户；纯字符串输入不受影响，现有校验可正确拒绝含路径分隔符的字符串
- 🛡️ **临时缓解**：在将任何用户输入传给 `moment.locale()` 之前，先验证其为字符串类型
- ⚠️ **严重等级**：中等（Moderate），CVSS 综合评分 5.9
- 📊 **CVSS 向量**：CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N（完整性影响高，机密性与可用性无影响）
- 🆔 **CVE 编号**：CVE-2026-17495
- 🧩 **弱点类型**：CWE-27 路径遍历（'dir/../../filename'）
- 👥 **致谢**：报告者 zolbooo；修复开发者 UlisesGascon、mattjohnsonpint；协调者 gilmoreorless
- 📅 **发布日期**：2026 年 9 月 15 日

---

### [关于本文档 | Node.js 26.8.2 文档](https://beta.docs.nodejs.org/)

**原文标题**: [About this documentation | Node.js 26.8.2 Documentation](https://beta.docs.nodejs.org/)

本文档是 Node.js 官方 API 参考，介绍基于 V8 的 JavaScript 运行时、稳定性索引以及各核心模块的用途与状态。

- 📘 文档为 Node.js 官方 API 参考，Node.js 是基于 V8 引擎的 JavaScript 运行时，自 v0.10.0 引入。
- 🛠️ 文档错误可在 issue tracker 报告，提交 PR 需参考贡献指南。
- ⚖️ 稳定性索引：0 已弃用、1 实验性、2 稳定、3 旧版；实验性功能不推荐生产使用，可能需命令行标志并发出警告。
- 🏛️ 旧版功能通常不会移除且仍受语义化版本保证，但不再积极维护，漏洞可能不修复。
- ✅ 稳定核心模块覆盖断言、异步上下文跟踪、Buffer、子进程、集群、控制台、加密、调试器、诊断、DNS、事件、文件系统、HTTP/2/HTTPS、网络、OS、路径、性能、进程、流、测试、定时器、TLS、URL、工具、V8、VM、Web Crypto、Web Streams、Worker threads、Zlib 等。
- 🧪 实验性功能包括 async_hooks（不推荐）、FFI、可迭代流、单可执行应用、SQLite、跟踪事件、虚拟文件系统、WASI 等。
- 🚫 已弃用/待弃用包括 domain、punycode 及部分弃用 API；可能发出警告且不保证向后兼容。
- 🧩 C++ 集成：C++ addons 可通过 require() 加载；C++ embedder API 支持在其他 C++ 软件中运行 JS。
- 🧠 异步与并发：async hooks、异步上下文跟踪、cluster 多进程、worker_threads 多线程。
- 🌐 网络与协议：HTTP、HTTP/2、HTTPS、TCP/IPC、UDP/datagram、TLS/SSL、DNS、URL、查询字符串。
- 📁 文件与系统：fs、path、os、process、环境变量、权限、TTY、readline、REPL、命令行 API。
- 🔐 安全与加密：crypto、Web Crypto、TLS、权限控制；WASI 文件系统沙箱安全有限。
- 🗄️ 数据与压缩：Buffer、字符串解码器、Zlib 支持 Gzip/Deflate/Brotli/Zstd，SQLite 为实验性。
- 🧪 测试、调试与诊断：assert、测试运行器、debugger、inspector、诊断报告/通道、跟踪事件、性能测量 API。
- 📦 模块系统：CommonJS、ECMAScript 模块、包、TypeScript、node:module API、Node-API、V8。
- 🌍 国际化与错误：提供国际化支持；应用会遇到不同类别错误。
- 🧾 文档输出：每个 .html 文档有对应 .json；系统调用文档链接到 man pages，Unix 与 Windows 行为可能有差异。

---

### [](https://github.com/nodejs/node/pull/62045#issuecomment-5689768930)

**原文标题**: [build, doc: move to redesign by avivkeller · Pull Request #62045 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62045#issuecomment-5689768930)

该 PR（#62045）将 Node.js 文档生成迁移到重新设计的文档体验，核心是让 doc-kit 使用新的 `web` 模板，移除旧版 all-in-one HTML 产物，并最终合入 main。整体目标是与 Node.js 主站 UI 更一致，同时将主要实现推进到 `doc-kit`。

- 🎨 重新设计：Node.js 文档迎来全新 redesign，HTML 结构与样式更贴近主站，提供更统一的品牌体验。
- ⚙️ 构建切换：在 `Makefile` 和 `vcbuild.bat` 中，doc-kit 模板由 `legacy-html-all` 改为 `web`。
- 🧹 产物调整：不再把 `out/doc/api/all.html` 声明为 `doc-only` 必需/生成的文档产物。
- 🧪 测试移除：删除 `test-make-doc`，因为新生成器会压缩 HTML，旧正则难以解析，且 `doc-kit` 中已有相关测试。
- 🔗 预览地址：`https://beta.docs.nodejs.org`，正式文档入口为 `https://nodejs.org/api`。
- 🚧 CI 与平台：曾标记 `wip`、`blocked`、`needs-ci`、`windows`；多数 CI 机器可运行，但 macOS 在限制 6GB/8GB 内存时 OOM，实际占用约 4–5GB。
- 💬 反馈要点：panva 提到脚注不工作、方法参数标为 “Attributes” 奇怪、方法列表 TOC 难读、正文 14px/16px 混用、表格宽度不足、`[C]`/`[P]` 列表区分度低。
- 🛠️ 作者回应：`Attributes` 是为统一描述 typed lists；完整参数 TOC 更精确；正文 16px，typed lists 14px；大表格应拆分；`[C]`/`[P]` 表示条目类型。
- 📄 文档文件：讨论过移除 `documentation.md`，但因稳定性级别说明和 `/about` 概览页仍需保留，后续再议。
- ✅ 评审结果：经多轮 review 后，获 panva、jasnell、pimterry、bmuenzenmeyer、aymen94 等批准；Copilot 也参与评审。
- 📊 覆盖率：Codecov 显示项目覆盖率 90.21%，较 base 提升 0.03%，修改且可覆盖的行均被测试覆盖。
- 🚀 最终状态：该 PR 已合入，landed in `18a9ba5`，并关闭；属于 notable change，应进入 changelog 的 Other Notable Changes 或专门发布说明。

---

### [](https://github.com/nodejs/node/pull/65010)

**原文标题**: [http: reject responses exceeding header limit by mcollina · Pull Request #65010 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65010)

Node.js 的 nodejs/node 仓库合并 PR #65010，将 HTTP 客户端在响应头超过 request.maxHeadersCount 时的行为从静默截断改为直接拒绝，并返回 HPE_HEADER_OVERFLOW；该变更属于 semver-major，已在 2026-09-14 合并到 main。

- 🚀 PR #65010 标题为 “http: reject responses exceeding header limit”，作者为 Matteo Collina（mcollina）。
- ⚠️ 此前 ClientRequest 会静默截断超出 maxHeadersCount 的响应，而 llhttp 仍继续使用被省略的头，可能导致解析器状态与暴露头不一致。
- ✅ 现在改为以 HPE_HEADER_OVERFLOW 拒绝响应，防止解析器状态与暴露头分歧。
- 💥 这是 semver-major 破坏性变更，应随下一个主版本发布。
- 🧪 Codecov 报告显示所有修改且可覆盖行均被测试覆盖，项目覆盖率约 90.27%。
- 👥 多位审查者批准，包括 aduh95、ShogunPanda、ronag、jasnell、avivkeller、bjohansebas。
- 🏷️ 相关标签包括 semver-major、http_parser、c++、needs-ci、author ready、commit-queue。
- 📅 2026-08-04 提交，2026-09-14 合并提交 e5778f7 进入 nodejs:main，91 项检查通过。
- 🔗 相关讨论：Bun 也有类似请求头限制问题（oven-sh/bun#42532）。

---

### [](https://nodejs.org/en/blog/release/v26.9.0)

**原文标题**: [Node.js — Node.js 26.9.0 (Current)](https://nodejs.org/en/blog/release/v26.9.0)

Node.js 26.9.0（Current）于 2026 年 9 月 16 日发布，由 Antoine du Hamel（@aduh95）维护，带来多项 SEMVER-MINOR 级新特性与大量稳定性修复，覆盖 crypto、worker、vfs、perf_hooks、ffi 等核心模块，并同步提供全平台安装包、二进制与源码下载及 SHA256/PGP 校验信息。

- 🚀 **版本信息**：Node.js 26.9.0（Current），发布日期 2026-09-16，发布者 @aduh95（Antoine du Hamel）
- 🔐 **crypto 新 API**：新增通用 MAC API，并支持从 OpenSSL providers 自动发现 cipher 与 hash 算法
- 🧩 **ffi 默认启用**：ffi 模块现已默认开启，无需额外实验标志
- 📊 **node:bench 落地**：新增内置基准测试模块 node:bench（含 createRunner、runFile、bench:plan 事件、报告器等），可通过 --experimental-bench 启用
- 📈 **perf_hooks 增强**：实现 Histogram meanCI API，并支持直方图数据的 CBOR 导出/导入以方便交换
- 📡 **DTLS 实验性支持**：新增实验性 DTLS API，包含统计数据与互操作测试
- 🗂️ **vfs 集成**：虚拟文件系统与 CJS、ESM 模块加载器打通，新增 ZipProvider，并支持从挂载文件系统加载原生插件
- 👷 **Worker 升级**：新增对 Web Workers 的支持，支持 ref/unref，并可基于内建快照启动工作线程
- 🔒 **crypto 安全修复**：修复 Hmac.digest() 返回未初始化内存、加固 X509Certificate 状态、修正多素数 RSA JWK、RSA-PSS 超长 salt、SPKI/PKCS8 导出错误等
- 🛡️ **FIPS 强化**：--force-fips 新增严格模式与 FIPS 指示器诊断通道
- 📁 **fs 多项改进**：fs.cp() 改用线程池复制目录树、glob 新增 maxDepth、递归 watch 竞态与错误处理修复、符号链接处理与时间戳保留优化
- 🌐 **http / http2 / https 修复**：限制代理 CONNECT 响应头、修复大窗口下写入死锁、修正异步上下文丢失与分块写入合并
- 🌊 **stream 大规模修复**：涉及 pipeTo 取消与失败处理、异步 flush、背压与 canWrite/ondrain 语义、写入重入防护等
- 🧱 **sqlite / sea / quic 修复**：会话生命周期与备份处理、SEA 虚拟文件系统挂载与 ELF 分段、QUIC 流控与 0-RTT 改进
- 🏗️ **构建系统变更**：新增 --shared-perfetto、--shared-highway、--shared-abseil 等标志，启用 V8 sandbox 与 gdb/lldb 插件支持，--use-largepages 变为空操作
- 💻 **下载渠道**：提供 Windows（x64/ARM64）、macOS（Intel/Apple Silicon）、Linux（x64/arm64/ppc64le/s390x/musl）、AIX 等安装包与二进制，以及源码 tar.gz/tar.xz
- ✅ **校验与文档**：附带 SHASUMS 与 PGP 签名，API 文档见 nodejs.org/docs/v26.9.0/api/
- ⏭️ **上一版本**：Node.js 26.8.2（Current）

---

### [](https://master.dev/sale/?utm_source=nodeweekly&utm_medium=newsletter&utm_campaign=buildersale)

**原文标题**: [Build Better With AI Sale | Master.dev](https://master.dev/sale/?utm_source=nodeweekly&utm_medium=newsletter&utm_campaign=buildersale)

秋季促销提供100美元优惠，主打掌握基础知识并用AI更好地构建，活动仅剩数天，可立即领取折扣。

- 🍂 秋季促销：立减100美元
- 📚 掌握基础知识
- 🤖 借助AI构建得更好
- ⏳ 促销仅剩数天
- 🛒 立即获取折扣

---

### [](https://thelazyweb.dev/connection-reuse-is-the-money)

**原文标题**: [Connection reuse is the money](https://thelazyweb.dev/connection-reuse-is-the-money)

支付平台 webhook 发送器通过连接复用，把每周 1120 万次出站 POST 中大量重复 TCP/TLS 握手消掉；收益高度集中在少数高频、快速响应的目的地，长尾目的地因投递间隔过长几乎无法复用连接。

- 🚚 旧发送器没有连接复用、会话或熔断器，每次 webhook 投递都新建连接并完整握手。
- 🧠 替换后最大优化不是更快运行时或服务器，而是确保 TCP 和 TLS 握手只做一次。
- 📈 单目的地流量可能突发也可能恒定；最忙目的地每几百毫秒一次，但并发低，平均约 5 连接。
- ⏱️ 冷 HTTPS 请求包含 DNS、TCP 1 RTT、TLS 1.2 2 RTT、证书验证和慢启动；72ms RTT 下握手约 155ms，占冷请求约 45%。
- 🎯 复用对快速响应目的地收益最大，因为固定握手时间占剩余延迟比例高；对慢目的地影响较小。
- 🧩 使用 Undici，每个目的地一个 Agent 池，`connections=10`、`keepAliveTimeout=60s`、`keepAliveMaxTimeout=10min`、`allowH2=true`。
- 📊 一周生产数据显示：10% 目的地间隔小于 60 秒，承载约 96% POST；15% 在 60 秒到 10 分钟，约 4%；75% 超过 10 分钟，不到 1%。
- 🌡️ 最忙目的地平均间隔小于 360ms，池化后头部 10% 基本永久热，超过 95% 投递可命中 keep-alive。
- 🧹 目的地空闲后按 `keepAliveTimeoutMs` 清理 socket、agent 和周边工具；连接生命周期驱动内存生命周期。
- 🛡️ 每个目的地独立池可隔离故障；`agent.destroy()` 是异步的，关闭时 await，空闲清理则 fire-and-forget 并记录错误。
- 🔀 HTTP/2 帮助有限：低并发下无东西可多路复用；Undici v8 会先填满连接再复用，`connections=10` 时 h2 突发仍可能开十个 socket。
- 📉 复用收益集中：前 5 个目的地约占 61% POST，前 25 个约占 85%；60 秒窗口大约覆盖到第 70 繁忙主机。
- ⚠️ 长尾约 500 个目的地共享最后几个百分点，超过三分之一每周少于 10 次投递，每次仍是冷连接。
- ❌ 第二繁忙目的地是证书验证失败的裸 IP，占 13% POST 且全是重试，近百万次尝试、每次约半秒握手，约等于每天 19 到 29 小时握手。
- ✅ 状态码分布：约 31% 为 2xx，40% 为 4xx，16% 为 5xx，13% 无响应；4xx 仍能复用连接，但说明三分之二尝试失败。
- 🧮 结论：池化是押注目的地“热且有突发”；用一天出站日志按目的地算平均间隔，与 keep-alive 窗口对比，并估算每空闲 socket 约 50KB，即可判断是否值得。
- 💰 连接复用减少在途时间并影响 AWS 账单，是整体每月节省超过 2000 美元的一部分；Lambda 与连接复用天然不太契合。

---

### [](https://undici.nodejs.org/api/Agent)

**原文标题**: [Agent | Node.js Undici](https://undici.nodejs.org/api/Agent)

Undici 的 Agent 是一个按 origin 管理并复用连接的默认调度器，用于向多个不同 origin 分发请求；未显式传入 dispatcher 时，request、stream、fetch 都会使用它。它按需为每个 origin 懒创建并复用 Pool 或 Client，空闲且无连接、不忙时会自动关闭。

- 🧭 核心作用：Agent 向多个不同 origin 分发请求，并维护 origin 到 dispatcher 的内部映射。
- 🔁 复用机制：首次请求通过 factory 懒创建对应 dispatcher，后续同 origin 请求复用它。
- ⚠️ 顺序说明：请求不保证按调用顺序分发。
- 🏷️ 版本与稳定性：v3.2.0 引入，Stability 2 Stable；源码位于 lib/dispatcher/agent.js，继承 Dispatcher。
- 🏭 构造与 factory：new Agent(options?)；默认 factory 为 (origin, opts) => new Pool(origin, opts)；若 connections: 1，则默认创建 Client，否则创建 Pool。
- 🚦 maxOrigins：限制同时接收请求的不同 origin 数量，默认 Infinity；必须大于 0；超过限制会抛出 MaxOriginsReachedError。
- ⚙️ 继承选项：Agent 继承 PoolOptions 和 ClientOptions；每个 origin 的 Pool 默认 connections 不设限，并发请求会分散到多个 Client 和套接字。
- 🧵 HTTP/2 注意：若希望 HTTP/2 多路复用共享 session，应把 connections 设为较小值，例如 1；allowH2 默认 true，maxConcurrentStreams 默认 100。
- 📊 属性 closed：调用 agent.close() 后为 true。
- 💥 属性 destroyed：调用 agent.destroy() 后，或 close() 且关闭完成后为 true。
- 📈 属性 stats：v7.9.0 加入；按 origin 返回 ClientStats 或 PoolStats 聚合统计，不暴露 stats 的 origin 会被省略。
- 🛣️ dispatch：agent.dispatch(options, handler) 将请求路由到 options.origin 的 dispatcher，必要时创建；origin 必填；忙时返回 false 并等待 drain；无效 origin 抛 InvalidArgumentError。
- 🧹 close：agent.close(callback?) 优雅关闭 Agent 及其所有 dispatcher，等待进行中请求完成；可返回 Promise 或使用 callback。
- 💣 destroy：agent.destroy(error?, callback?) 强制销毁 Agent 及其所有 dispatcher，并中止待处理请求；可返回 Promise 或使用 callback。
- 🔌 路由方法：connect、pipeline、request、stream、upgrade 都会路由到 options.origin 对应的 dispatcher，行为参见 Dispatcher 对应方法。
- 📡 事件：connect 在 socket 创建并准备好接收请求时触发；disconnect 在 socket 断开时触发；connectionError 在连接失败时触发；drain 在 origin 的 dispatcher 不再忙时触发。
- 🧾 事件参数：事件通常带 origin、targets（从 Agent 开始的 dispatcher 链）；disconnect 和 connectionError 还带 error；事件转发自底层 dispatcher。

---

### [](https://hackers.pub/@hongminhee/2026/upyo-email-decoupled-from-where-and-how)

**原文标题**: [æ´ª æ°æ (Hong Minhee): Email, decoupled from where and how: A cross-runtime, cross-provider email library for JavaScript and TypeScript](https://hackers.pub/@hongminhee/2026/upyo-email-decoupled-from-where-and-how)

概览总结
Upyo 是一个面向 JavaScript/TypeScript 的跨运行时、跨提供商邮件库。它基于 Web 标准与统一 Transport 接口，让同一套发送代码能在 Node.js、Deno、Bun 和边缘运行时中工作，并通过可组合的传输层把重试、故障转移、开发调试和测试从应用逻辑中解耦。

- 🌍 背景：Nodemailer 在 Node.js/SMTP 场景依然成熟，但现代 JS/TS 还运行在 Deno、Bun、Cloudflare Workers 等环境，且开发与生产常切换邮件提供商。
- 🎯 目标：Upyo 不只回答“如何从 Node.js 发邮件”，而是回答“应用如何不依赖运行时和提供商来投递邮件”。
- 🧩 通用性：基于 fetch()、Web Streams、Web Crypto 等 Web 标准，不依赖 node:net、node:tls、node:stream，可跨 Node.js、Deno、Bun 和边缘函数运行。
- 🔌 统一接口：所有邮件服务通过同一个 Transport 接口接入，支持 SMTP、JMAP、Resend、SendGrid、Mailgun、Amazon SES、Plunk、Lettermint，切换提供商无需改应用发送逻辑。
- 📦 轻依赖：@upyo/ses 自行实现 AWS Signature v4，避免引入假设 Node.js 的 AWS SDK，从而保持边缘运行时兼容。
- ✉️ 小巧 API：Transport 核心为 send()、sendMany()，取消通过 AbortSignal；批量发送可按提供商优化为批端点、SMTP 连接复用或并发发送。
- 🔁 重试解耦：RetryTransport 可包装任意传输层，应用代码无需自建重试逻辑，只需接收 transport: Transport 并注入具体实现。
- ⚠️ 错误统一：Receipt 区分成功与失败，失败包含 retryable、category、retryAfterMilliseconds 等字段，使 429 和临时 SMTP 错误可统一处理。
- 🧮 池化与故障转移：PoolTransport 支持按优先级故障转移或轮询分发，并可与 RetryTransport 叠加，灵活决定重试与切换顺序。
- 🪄 开发体验：@upyo/logtape 在开发中用日志代替真实发送，可直接从服务器日志复制 magic link，无需反复查收件箱。
- 🧪 测试友好：@upyo/mock 的 MockTransport 可注入同一 sendMagicLink()，通过 waitForMessage 断言，业务函数本身无需改动。
- 🛠️ 功能完整：SMTP 支持 SMTPUTF8、DSN，附件可流式处理，支持日历邀请/取消，以及 messageId、inReplyTo、references 等会话头。
- 🚀 快速开始：安装 @upyo/core 与 @upyo/smtp，创建 SmtpTransport 和消息后调用 send()；按需叠加 RetryTransport、PoolTransport、LogTapeTransport。
- 📚 资源：文档、GitHub 源码、npm 与 JSR 包均已提供，作者欢迎通过 issue 或 discussion 反馈。

---

### [Upyo | 跨运行时邮件库](https://upyo.org/)

**原文标题**: [Upyo | Cross-runtime email library](https://upyo.org/)

该内容为 Upyo 邮件库文档的导航目录，按入门、消息编写、传输服务、工具集成与 API 参考组织。

- 🚀 入门部分包含“Why”和“Start”。
- ✉️ 消息能力覆盖撰写消息、MIME 组合、附件及日历邀请。
- 📬 内置 SMTP、JMAP 传输，并集成 Lettermint、Maileroo、Mailtrap、Mailgun、Plunk、Resend、SendGrid、Amazon SES。
- 🛠️ 高级与辅助传输包括 Pool、Retry、LogTape、OpenTelemetry、Mock 和自定义传输。
- 📦 References 列出 @upyo/core、@upyo/mime、@upyo/smtp、@upyo/jmap 以及各服务与功能包。
- 🧭 界面还提供搜索快捷键（⌘/Ctrl K）、Unstable 和 Appearance 等项目。

---

### [深入探究 JavaScript 引擎的内部工作原理：编写让 V8 满意的代码](https://www.audreydoyen.com/blog/en/js-engines-and-v8-en)

**原文标题**: [A deep dive into the inner workings of JavaScript engines: writing code that makes V8 happy](https://www.audreydoyen.com/blog/en/js-engines-and-v8-en)

本文深入剖析 V8 内部机制，从浏览器与 JavaScript 引擎的关系切入，讲解四层 JIT 编译管线、隐藏类、内联缓存、优化/去优化循环、垃圾回收，并总结如何写出让 V8 更易优化的代码。

- 🌐 浏览器没有统一架构，可能使用单进程多线程或多进程；浏览器、Web 引擎、JavaScript 引擎是不同层面的概念。
- 🧩 Chrome 是浏览器应用，Chromium 是开源项目，Blink 是 Web 引擎，V8 是 JavaScript 引擎。
- 🧠 JavaScript 引擎负责执行 JS，也可嵌入 Node.js、VS Code 等；其他引擎有 SpiderMonkey、Nitro 等。
- 🎯 聚焦 V8 的原因：采用广泛、文档公开、架构演进活跃，是理解现代 JS 引擎的典型案例。
- ⚙️ JavaScript 实际采用 JIT：解释与编译结合，动态把代码编译为机器码。
- 🚀 V8 四层管线：Ignition 解释器 → Sparkplug 基线编译器 → Maglev 中层编译器 → TurboFan 顶层优化编译器。
- 📊 Ignition 执行字节码并收集类型、调用频率等 profiling 信息；函数变“温”后逐层优化。
- 🔁 优化基于假设：若类型或对象形状变化，V8 会去优化并回退到低层，之后可能重新优化。
- 🧩 隐藏类/形状：V8 为对象建立内部布局，属性按相同顺序初始化可共享形状，属性访问更快。
- ⚡ 内联缓存：缓存属性查找结果；单态最快，多态稍慢，巨态会退化为完整查找。
- 📉 去优化惩罚可能 2×–20×，热点路径更严重；反复优化/去优化会进入“去优化地狱”，甚至被标记为不可优化。
- 🚫 常见优化杀手：delete 会让对象进入字典模式；初始化后随意加属性；属性顺序不一致；历史 try/catch 影响优化。
- ✅ V8 友好写法：保持对象形状稳定、属性顺序一致、不混用类型、热代码不用 delete、初始化所有属性、写可预测的单态代码。
- 🧹 V8 垃圾回收分代：新生代用 Scavenger，老生代用 Mark-Sweep-Compact；Orinoco 通过并行/并发减少停顿。
- 💡 GC 友好技巧：短命对象成本低；避免 detached DOM 节点、未清理事件监听器等内存泄漏，及时清除引用。
- 🧠 TypeScript 编译后仍是 JS，不能单独让 V8 满意；精确类型、避免 any 和宽联合类型可间接帮助 V8 优化。
- 🛠️ 文章包含多个动手练习，如可视化隐藏类、单态 vs 多态、追踪优化、测量 delete 影响、调试内存泄漏。
- 🏁 核心结论：写“无聊、稳定、可预测”的 JavaScript，往往就是让 V8 跑得更快的代码；工具背后仍取决于使用意图。

---

### [](https://humanwhocodes.com/blog/2026/09/five-roles-working-ai/)

**原文标题**: [Five software engineering roles for working with AI - Human Who Codes](https://humanwhocodes.com/blog/2026/09/five-roles-working-ai/)

软件工程师与 AI 的协作仍在演化，已从更好的代码补全发展到能自主分诊缺陷、定位根因并部署修复的代理。作者用五种职业角色描绘人机交互光谱——观察者、技术主管、架构师、工程经理、产品经理；选择取决于对 AI 的信任、任务风险和技术上下文，并需始终对结果负责。

- 👀 观察者（结对程序员）：实时观看并审查 AI 写代码，可追问和纠错；适合起步或信任不足时，但易审查疲劳，可交替做驱动者。
- 🧭 技术主管：写技术规范，让代理并行实现，最后审查代码并反馈；通过自动化格式化、lint、测试覆盖减少审查负担，提升生产力。
- 🏗️ 架构师：聚焦系统布局、组件接口、基础设施与框架，主要看架构和日志而非代码；风险是远离代码，出问题缺乏底层知识，需抽查代码与测试。
- 🏭 工程经理：搭建“软件工厂”，定义流程（如 PRD→技术规范→实施计划），给代理分配任务和验收标准；风险是流程失灵时重启循环可能较慢。
- 🎯 产品经理：专注用户体验、界面和用户旅程，不关心实现细节，只要产品按预期工作；挑战是技术故障时难以修复，可能依赖他人。
- ⚙️ 自动化是关键：格式化、lint、测试与覆盖率要求越高，越能降低审查疲劳，增强对 AI 生成代码合并的信心。
- ⚠️ 主要权衡：越亲力亲为越可控但吞吐受限；越放手越高效但离代码越远，故障定位与修复能力越弱。
- ✅ 结论：五种角色没有绝对优劣，应按信任度、风险和技术背景有意识地选择，并随信心与 AI 能力提升沿光谱移动。
- 🔄 你可以在探索陌生代码库时当观察者，在协调多工作流时当技术主管，在重视用户体验时当产品经理，但不应放弃对结果的责任。

---

### [如何实现分布式熔断器](https://blog.gaborkoos.com/posts/2026-09-14-How-to-Implement-a-Distributed-Circuit-Breaker/)

**原文标题**: [How to Implement a Distributed Circuit Breaker](https://blog.gaborkoos.com/posts/2026-09-14-How-to-Implement-a-Distributed-Circuit-Breaker/)

overview summary
本文以 caracal 的 Redis 后端为例，说明如何从单进程熔断器扩展到分布式熔断器：共享窗口后，必须处理原子决策、时钟偏差、浮点阈值、代际/epoch、全局探针预算、协调器故障与配置耦合等问题。

- 🛡️ 熔断器通过统计近期调用结果，在失败率过高时快速失败，保护故障依赖并释放调用方容量。
- 🔁 三态：closed 正常放行并记录；open 立即拒绝；half-open 限量探针决定恢复或再次打开。
- 📊 四类转换：closed→open 需达到 failureThreshold 且观测数≥minimumThroughput；open→half-open 经 openMs；half-open→closed 需 halfOpenSuccesses；half-open→open 任一探针失败。
- ⏱️ open→half-open 宜用惰性转换：首个发现超时的调用完成转换并抢占探针槽，避免空闲定时器和多副本惊群。
- 🧮 进程内窗口可用环形缓冲区维护失败计数；minimumThroughput 防止单个失败就熔断。
- 🧬 并发结果可能迟到，用 generation 计数丢弃针对旧状态的结算，避免过期成功错误关闭。
- 🕳️ half-open 探针槽必须最终释放；超时或适配器 promise 不结算会让熔断器永久卡住，因此超时应放在熔断器内部。
- 🌐 多副本各自维护窗口会使依赖承受约副本数倍的伤害才触发；需将窗口放入共享存储。
- 🗂️ 共享窗口按 scope key 划分，可按区域、租户或全局；全局反应快但爆炸半径大，窄 scope 更安全但填充慢。
- 🧾 scope key 应稳定且不含敏感信息；所有共享同一 key 的副本必须使用一致配置。
- ⚛️ 分布式下“读取窗口”和“执行动作”是两个往返，存在竞态；应把记录、评估、转换放入 Redis Lua 脚本原子执行。
- 🕰️ 各副本时钟不一致，关键时间戳应使用协调器的 Redis TIME，避免客户端时间进入决策。
- 🔢 Lua 浮点比较阈值有边界问题；将失败率缩放为千分整数，并拒绝 <0.0005 或 ≥0.9995 的阈值。
- 🧿 generation 在分布式变为 epoch：观测带 epoch 标签，转换只增 epoch 而不删除旧观测；open→half-open 不增 epoch 以保留窗口。
- 🧹 状态哈希丢失但观测遗留会产生孤儿数据；可用观测 UUID 哈希派生非零新 epoch，并避免 Lua 科学计数法破坏 epoch 前缀。
- 🎟️ 探针预算必须全局：Redis ZSET 保存每个在途探针及过期时间，先清理过期槽位再计数，防止各副本同时放行探针。
- 🧷 探针结算要检查 deadline；已过期探针不应再影响计数，正常结算则立即释放槽位。
- 🧯 协调器故障时：已知 open/half-open 的 scope 应 fail-closed；未知或 closed 默认 fail-open，可配置；无法记录的观测可丢弃。
- 🚫 不建议协调器不可用时回退本地熔断器，因为这会重建每副本窗口并让系统误以为仍受分布式保护。
- 🧪 用内存版与 Lua 版双实现做差分测试，并统计关键路径覆盖，避免生成序列只走快乐路径。
- ⚙️ 配置相互耦合：窗口保留期、最小吞吐、探针租约 TTL、调用超时、halfOpenSuccesses 与探针速率、状态过期与观测保留都需一起校验。
- 📦 caracal 用同一接口支持本地内存和 Redis 后端，便于直接比较两种实现。

---

### [](https://www.eraser.io/blog/open-sourcing-eraser-diagrams)

**原文标题**: [Open-sourcing Eraser Diagrams â Eraser](https://www.eraser.io/blog/open-sourcing-eraser-diagrams)

Eraser Diagrams 是一个 AI 原生、坐标感知的图表格式，已在 MIT 许可下开源，并发布规范、参考渲染器和示例库。文章解释：LLM 已能胜任坐标布局，而 Mermaid 等关系语言无法表达“东西放在哪里”，因此需要为 LLM 生成与人类理解设计的新格式。

- 🧠 LLM 过去不擅长把设计意图转为坐标，AI 图表工具因此依赖 ELK 等确定性布局引擎：模型只决定连接关系，引擎决定位置。
- 🚀 2025 年末至 2026 年初，前沿模型开始真正擅长基于坐标的布局，模型可直接生成布局本身。
- 📏 旧引擎适合小图，但复杂图以“减少交叉”为目标会牺牲叙事和尺寸要求；“放到一页幻灯片”“数据库放右列”等需求无法表达。
- 👁️ AI 执行不是瓶颈，人类理解、评估和治理才是；清晰图表能帮助人类跟上 agent 产出，并应利用方向、对称、比例、颜色、富文本和动效。
- 🧜 Mermaid 是关系语言，布局交给引擎，无法指定位置；LLM 已悄然超越 Mermaid。
- 🧩 现有坐标格式不合适：SVG/HTML 太底层，Draw.io XML 冗长，Graphviz/D2/PlantUML 仍是关系语言。
- 📦 Eraser Diagrams 定位为“语义节点与边 + 显式坐标 + 强默认值”，并为 token 高效的 LLM 生成而设计；用 JSON 表达 entities/connections、图标、分组和坐标。
- 🛠️ 三项设计原则：易引导（强默认，少量 JSON 出图）、深度可定制（样式/连接器/动画/自定义组件）、默认惰性（JSON 非代码，可 schema 验证，不能计算，图标安全处理）。
- 🌍 开源因为人类理解瓶颈不应被单一产品垄断；希望用于 agent 框架、PR 机器人、文档流水线和 IDE。策略是商品化格式，押注上层工具与服务。
- 🔗 MIT 许可、商用免费、不接受贡献；规范、渲染器和示例在 github.com/eraserlabs/eraser-diagrams。

---

### [Platformatic Memcached：](https://blog.platformatic.dev/introducing-platformatic-memcached)

**原文标题**: [Platformatic Memcached: A Faster Client for Node.js](https://blog.platformatic.dev/introducing-platformatic-memcached)

Platformatic 推出 @platformatic/memcached，一个面向 Node.js 的高性能、零依赖 memcached 客户端，基于 meta 协议并支持完整请求流水线，目标是解决现有 Node.js 客户端老旧、慢且维护不足的问题。

- 🚀 性能突出：单连接可达 35 万+ SET/s、36.9 万+ GET/s，约为对比中最快客户端的 3 倍。
- ⚡ 采用 meta 协议：替代冗长易错的经典文本协议和已弃用的二进制协议，使用紧凑命令、明确标志、长度前缀数据块与 CAS 支持。
- 🧩 设计继承 @platformatic/kafka：单连接全流水线、FIFO 响应匹配、增量 Buffer 解析、writev 合并写、零运行时依赖，仅使用 node:net。
- 🛡 通过 opaque token 校验响应：每次响应都验证不透明令牌，避免协议失步导致错误数据。
- 🛠 API 简洁完整：支持 get/gets、set/add/cas、delete、incr/decr、noop、version、stats、statsAll；值使用 Buffer，键最多 250 字节。
- 🌐 生产级功能：客户端 ketama 分片、AWS ElastiCache 自动发现、TLS 与 ASCII authfile 认证、连接池、指数退避重连。
- 🔐 连接与认证：支持 memcacheds:// 和 node:tls，每个连接首条命令完成认证；不支持基于弃用二进制协议的 SASL。
- 📊 内置可观测性：client.metrics() 提供稳定指标，node:diagnostics_channel 发布事件，@platformatic/memcached-otel 可生成 OpenTelemetry CLIENT span。
- 🎯 实际动机：为 Platformatic Gateway 请求去重功能提供 memcached 存储适配器，支撑跨副本高并发协调，避免客户端成为瓶颈。
- 🧪 当前状态：私有且实验性，API 可能变化，但工程实现已生产级，并用真实 memcached Docker 环境测试 auth、TLS、互操作和编译包。
- 📦 可试用与参考：提供 npm install @platformatic/memcached，代码与基准脚本在 GitHub platformatic/memcached。
- 🧠 核心结论：缓存位于热路径，单连接流水线、按长度解析、opaque token 校验，让客户端不仅快，而且在大规模操作下可信。

---

### [memcached —— 分布式内存对象缓存系统](https://memcached.org/)

**原文标题**: [memcached - a distributed memory object caching system](https://memcached.org/)

Memcached 是一个免费开源、高性能、分布式内存对象缓存系统，主要用于通过减轻数据库负载来加速动态 Web 应用。

- ⚡ 免费开源、高性能、分布式内存对象缓存系统，通用但主要用于加速动态 Web 应用。
- 🗄️ 内存键值存储，用于缓存小块任意数据，如字符串、对象，来源包括数据库调用、API 调用或页面渲染结果。
- 🧩 简单而强大：简洁设计促进快速部署与开发，解决大型数据缓存的许多问题，API 支持大多数流行语言。
- 📦 最新稳定版为 v1.6.45，发布日期为 2026-7-9，提供发行说明和 tar.gz 下载。
- 💻 快速示例：`get_foo` 先查询 Memcached，未命中则从数据库获取，再写回缓存。
- 🔌 可通过 telnet 交互，例如 `telnet localhost 11211`，使用 `get foo`、`stats` 等命令。
- 💬 有问题可加入 Discord 聊天、查阅文档站点或使用邮件列表；也支持商业支持与赞助开发。
- 📝 页面由 Dormando 维护，Logo/横幅版权为 2009-2018，布局取自 git-scm.com，建议通过邮件列表反馈。

---

### [发布 v30.1.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v30.1.0)

**原文标题**: [Release v30.1.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v30.1.0)

jsdom v30.1.0 已发布，本次更新聚焦性能与正确性，新增元素命名访问、QuotaExceededError 等能力，并修复大量 DOM、CSS、事件、脚本、资源加载与内存问题；感谢 @scttcper 及多位贡献者，多数改动为 AI 辅助。
- 🚀 版本包含 12 个提交，专门感谢 @scttcper 借助 @codex 发现并修复大量性能与正确性问题。
- 🏷️ 新增 document 上元素的命名访问，例如 document.myForm 对应 `<form name="myForm">`。
- 💾 新增 QuotaExceededError，用于存储配额错误和过大的 crypto.getRandomValues() 请求。
- 📜 支持更宽松的 DOM 命名规则来创建元素、属性和文档类型。
- ⚡ 大幅提升 DOM 构建、树变更、Range 操作、live collection、getComputedStyle()、样式变更和 CSS 序列化性能。
- 🖱️ 提升事件派发、表单控件/标签查找、`<select>` 与单选按钮组更新的性能。
- 🧠 减少 DOM 节点、属性、事件监听器和 MutationObserver 的内存占用。
- 🪟 window.close() 现在会保留对文档和 DOM 的引用访问。
- 🔍 修复查询与选择器问题：querySelectorAll 首段匹配自身、CSS 属性选择器大小写、querySelector 同 ID 不匹配、shadow 树 :focus。
- 🧬 修复 DOM 插入/替换、replaceChildren()、非法文档元素/doctype 放置，以及 replaceWith() 期间的变更。
- ⏱️ 修复脚本执行、自定义元素回调、iframe 加载和 MutationObserver 通知顺序，包括 shadow 树场景。
- 🛑 修复 window.close()/iframe 移除后事件与导航继续，并阻止已销毁文档启动新脚本、资源、定时器或动画帧。
- 🌐 修复资源加载、JSDOM.fromURL() 挂起、缓存加载误判中断、重定向/拦截器/XMLHttpRequest 取消，以及 iframe 自移除导致的父文档等待。
- 🎨 修复样式表顺序、@import/@media 处理、shadow 树样式失效，以及 getComputedStyle() 的边框宽度、font-weight、长度/百分比/数学函数和 shorthand 解析问题。
- 📝 修复 Range/Selection CDATA、text.normalize()、CDATA/处理指令克隆与序列化、命名属性集合和内存泄漏。
- 🔐 修复存储事件、命名空间属性、input.list、attr.ownerDocument、getElementsByTagName/tagName 大小写等行为。
- 🔘 修复 radio/select 分组与选中更新、input.indeterminate 克隆、焦点状态、空 script 插入执行、document.currentScript、事件派发和异步 volumechange/ratechange。
- 🧰 修复 XPath/NodeIterator、FileReader 字符集、时间输入、textarea 换行、readyState、translate、XML 代理/命名空间、base URL、SVG viewportElement、blobEvent.timecode 和 CSS 对象形状。
- 👥 贡献者包括 @soroushm、@scttcper 等 14 人，多数贡献为 AI 辅助。

---

### [发布 v5.0.0 · xojs/xo · GitHub](https://github.com/xojs/xo/releases/tag/v5.0.0)

**原文标题**: [Release v5.0.0 · xojs/xo · GitHub](https://github.com/xojs/xo/releases/tag/v5.0.0)

xo v5.0.0 是一次重大版本更新，由 sindresorhus 于 9 月 16 日发布，包含破坏性变更、多项改进、修复以及大量新增 lint 规则。

- 🚀 发布 v5.0.0 最新版本，重点更新 XO 的配置行为、TypeScript 支持、规则集和依赖版本。
- ⚠️ 破坏性变更：`space`、`semicolon`、`prettier` 选项现在只能全局设置；若在同时包含 `files`、`ignores` 或 `basePath` 的配置项中设置会报错。
- 🔧 文件级覆盖需改用 `@stylistic/indent`、`@stylistic/semi` 和 `prettier/prettier` 规则。
- 🔄 `unicorn/prefer-minimal-ternary` 的 `checkVaryingCallee` 选项更名为 `checkVaryingBase`。
- ✅ 改进：使用 `eslint-package-json` 检查 `package.json` 文件，`space` 选项现在也适用于 HTML 文件。
- 📦 改进：TypeScript 中通过 `n/file-extension-in-import` 强制导入文件扩展名，支持自动修复并理解 `.js` 对应 `.ts` 的导入约定，取代 `import-x/extensions`。
- 🧹 改进：禁用 `@stylistic/function-paren-newline`，并升级到 `eslint-plugin-unicorn 75` 和 `eslint-node-test 0.4`。
- 🐛 修复：修复 Windows 上的 TypeScript 文件匹配问题（#896）。
- 🆕 新增 `n` 规则：`n/prefer-process-get-builtin-module`。
- 🦄 新增多项 `unicorn` 规则：包括 `no-async-iterator-callback`、`no-multiple-promise-resolver-calls`、`no-shorthand-property-overrides`、`no-transition-all`、`no-unnecessary-string-trim`、`no-unsafe-sqlite-interpolation`、`no-unused-builtin-method-return`、`no-unused-iterator-helper`、`no-useless-re-export`、`no-useless-set-construction`、`no-using-resource-escape`、`prefer-combined-guards`、`prefer-dom-node-html-methods`、`prefer-iterator-zip`、`prefer-temporal-conversion`、`prefer-then-catch`、`single-line-block-comment-style` 等。
- 🔁 `unicorn/no-unused-builtin-method-return` 取代 `unicorn/no-unused-array-method-return`。
- 🧪 新增多项 `node-test` 规则：包括 `no-duplicate-mock-timers-enable`、`no-expect-failure-without-reason`、`no-import-test-files`、`no-late-test-activity`、`no-misused-context-hook`、`no-mock-module-after-import`、`no-process-chdir-in-test`、`no-test-global-configuration`、`prefer-mock-accessor`、`prefer-mock-call-count`、`valid-test-tags`。

---

### [](https://github.com/harshankur/officeParser)

**原文标题**: [GitHub - harshankur/officeParser: A robust, strictly-typed Node.js and Browser library for parsing office files into a rich Abstract Syntax Tree (AST) and generating high-fidelity output in multiple formats.  Parses: docx · pptx · xlsx · odt · odp · ods · pdf · rtf · csv · md · html. Generates: Markdown · HTML · CSV · RTF · PDF · Plain Text · RAG Chunks · GitHub](https://github.com/harshankur/officeParser)

officeParser 是一个严格类型、支持 Node.js 与浏览器的 Office 文档解析/生成/转换库，可将文件解析为统一 AST，并高保真输出多种格式；v8 重点升级 PDF 结构提取、密码支持、原生 DOCX/ODT/PDF 生成与 RAG 分块。

- 📥 解析格式：docx、pptx、xlsx、odt、odp、ods、odg、pdf、rtf、csv、md、html、epub。
- 📤 生成格式：DOCX、ODT、Markdown、HTML、CSV、RTF、PDF、EPUB、纯文本与 RAG chunks。
- 🌐 提供浏览器交互式 AST 可视化与文档，可上传文件、检查 AST、调整配置并实时预览。
- 🆕 v8 重建 PDF 文本提取：标签 PDF 可产出标题、表格、列表、脚注/尾注；无标签 PDF 用几何方式恢复结构。
- 🧭 PDF 支持多栏/浮动文本阅读顺序、连字符重连、旋转文本、内部链接、合并单元格与页面 bounds。
- 🔐 加密 PDF、OOXML、ODF 通过统一 password/onPassword 支持解析、转换和模板。
- 🧩 原生 DOCX/ODT 生成，以及基于 pdf-lib 的原生 PDF 引擎，可在 Node 和浏览器生成真实 PDF 字节。
- ✉️ OfficeTemplate.render 支持 DOCX 模板 {{placeholders}} 邮件合并，单个或批量，保留格式并确定性输出。
- ⚙️ 安装：npm i officeparser；要求 Node.js >= 22.13。
- 💻 CLI：npx officeparser file --to=text/md/html/csv/epub/docx/odt/chunks 等，支持 --output、--ocr、--password、--extractAttachments。
- 🧠 核心 API：parseOffice、OfficeConverter.convert、OfficeGenerator.generate、ast.to(format)。
- 🔄 OfficeConverter.convert() 一步完成解析+生成，并自动同步 extractAttachments；配置使用嵌套 parseConfig/generatorConfig。
- 📥 输入支持路径、Buffer、ArrayBuffer、Uint8Array、Blob/File；md/html/csv 等无魔数格式从缓冲区解析需 fileType。
- 🛑 支持 AbortSignal 取消；OCR worker 会自动清理，并可配置 workerLoad/recognition/autoTerminate 超时。
- 👁️ OCR 基于 Tesseract，需 extractAttachments；默认 preserveLayout 保留二维布局，适合扫描表格、表单和发票。
- 🧱 AST 包含 type、metadata、content 节点树、auxiliary 页眉页脚/母版/大纲、attachments、warnings、config 与 to()。
- 🏷️ OfficeIssue 统一警告/错误结构，错误携带 error.officeIssue.code，便于按稳定代码分支处理。
- 📊 按格式能力矩阵：注释、脚注、页眉页脚、母版、图片、图表、表格合并等支持情况因格式而异。
- 📋 深度组件：列表、table→row→cell、合并单元格、图片/OCR、图表、格式化、break nodes、公式统一为 LaTeX。
- 🧾 元数据含 author/title/created/modified/keywords/customProperties/nativeProperties/styleMap 等，生成时可用 metadataOverrides。
- 📝 Markdown 扩展方言支持任务列表、admonitions、脚注、定义列表、缩写、属性列表、引用、wikilinks、数学与 embeds，并支持 HTML 往返。
- 📚 EPUB 支持：解析 OPF/spine 与 Dublin Core；生成 EPUB 3；含图片时需 extractAttachments: true。
- 🚀 性能：ODP 解析最高快 23×，Excel 大稀疏表内存优化，RTF 去除 O(n²)，DOCX 支持 vMerge/gridSpan。
- 🔧 丰富配置：OfficeParserConfig、GeneratorConfig、htmlConfig/mdConfig/pdfConfig/docxConfig/odtConfig/csvConfig/textConfig、ChunkingConfig、styleMap、onNode。
- 🧩 RAG 分块：document-structure、fixed-size、semantic 三种策略；OfficeChunk 带来源、页码、幻灯片、工作表、最近标题、表格等元数据。
- 🌍 浏览器：提供 ESM/IIFE/slim/native-pdf 等 bundle；MV3 扩展用 slim；PDF worker 版本需匹配 pdfjs-dist@6.2.108。
- 🛠️ 常见问题：OCR 后调用 terminateOcr()；PDF worker 配置；大 Excel 早转文本释放内存；PDF 生成可装 puppeteer 或切 native。
- ⚠️ 已知限制：ODT/ODS 图表、PDF 图片转 PNG、无标签 PDF 结构尽力恢复、PDF 下划线/删除线仍未提取。
- 🔒 安全边界：解析不可信文件有风险；库做输出转义、解压限制、SSRF 防护等尽力加固，但不保证安全，需沙箱/资源限制。
- 📄 项目 MIT 许可，欢迎贡献与赞助；npm 与 GitHub 为 harshankur/officeParser。

---

### [](https://github.com/oclif/oclif)

**原文标题**: [GitHub - oclif/oclif: CLI for generating, building, and releasing oclif CLIs. Built by Salesforce. · GitHub](https://github.com/oclif/oclif)

oclif 是 Salesforce 开发的 Open CLI Framework 官方 CLI，用于生成、构建和发布 oclif CLI，并支持开发 oclif 插件与命令行工具。该项目在 GitHub 上开源，采用 MIT 许可证，拥有约 9.6k stars 和 363 forks。

- 📦 项目定位：为 oclif CLI 提供生成、构建、发布能力，是开发 oclif 插件和 CLI 的核心工具。
- ⭐ 社区数据：约 9.6k stars、363 forks、71 watchers、10 个 issues、14 个 pull requests，main 分支有 3,136 次提交。
- 🧩 主要命令：包括 oclif generate、init、manifest、pack、promote、readme、upload 等。
- 🚀 快速开始：可用 npx oclif generate mynewcli 创建 CLI，再通过 ./bin/run.js --version 或 --help 运行。
- ⚙️ 环境要求：当前支持 Node 18+，并支持 Node LTS 版本。
- 🔄 V1 迁移变化：oclif multi、plugin、single 被移除，统一改为 oclif generate；hook 和 command 改为 generate:hook、generate:command。
- 🆕 整合能力：版本 2 整合原 oclif-dev CLI，新增 manifest、pack、pack:deb、pack:macos、pack:win、upload 系列、readme 等命令。
- 📚 学习资源：提供 Getting Started 教程、Usage 文档，以及 Hello-World、Salesforce CLI、Heroku CLI 等示例。
- 🏭 相关仓库：@oclif/core 是基础库，@oclif/test 是测试辅助工具。
- 🤝 贡献与许可：提供贡献指南和行为准则，项目采用 MIT 许可证，由 Salesforce 构建。
- 🏷️ 项目主题：CLI、Node.js、oclif、TypeScript。

---

### [发布 12.33.0 · timgit/pg-boss · GitHub](https://github.com/timgit/pg-boss/releases/tag/12.33.0)

**原文标题**: [Release 12.33.0 · timgit/pg-boss · GitHub](https://github.com/timgit/pg-boss/releases/tag/12.33.0)

pg-boss 12.33.0 发布，核心是引入可注入时钟，让测试无需真实等待即可推进队列轮询、重试、过期与调度；Schema 升级到 42，并新增 doctor --fix 处理遗留的测试时钟覆盖。

- 🕒 新增 TestClock：通过 clock 构造选项让 JS 与数据库两侧时间由测试控制，可 tick 推进 JS Date、Postgres 时间戳和 worker 轮询。
- 🗄️ Schema 42 新增 `${schema}.job_now()` STABLE SQL 函数，所有语句经它读取时钟；生产中计划器内联到 `pg_catalog.now()`，成本不变。
- 🧪 测试示例：配合 `__test__enableSpies` 和 `getSpy('q').waitForJobWithId(id, 'completed')`，可在 `tick(60_000)` 后验证 `startAfter` 等行为。
- 🩺 `doctor --fix`：TestClock 正常释放会恢复 `job_now()`，但异常终止可能留下覆盖；doctor 可检测、打印恢复语句并修复。
- ⚠️ 运行 `--fix` 前需确认没有实例持有 live TestClock，因为遗留覆盖与活跃覆盖无法区分；修复只针对此问题并重新扫描。
- 🔍 检测基于存储函数体中的覆盖设置正向测试，也兼容 CockroachDB 这类会重写存储对象的数据库。
- 📦 升级影响：仅目录级变更，创建 `job_now()` 并替换 `create_queue()`，不重写表、不触碰行、不回填。
- 👥 变更由 @bhamiltoncx #901 实现，@timgit #904 跟进；完整变更范围 `12.32.0...12.33.0`。
- 📊 发布信息：16 Sep 20:43 发布，4 commits 到 master，贡献者 timgit 和 bhamiltoncx；项目约 4k stars、272 forks。

---

### [](https://github.com/moscajs/aedes)

**原文标题**: [GitHub - moscajs/aedes: Barebone MQTT broker that can run on any stream server, the node way · GitHub](https://github.com/moscajs/aedes)

overview summary
Aedes 是 Mosca 的继任者，一个基于 Node.js 的轻量级 MQTT broker，可在任意流式服务器上运行；它强调 MQTT 兼容性、可扩展性、集群能力和高并发性能，并拥有丰富的持久化、消息发射器、中间件与扩展插件生态。

- 📌 项目定位：moscajs/aedes 是“barebone” MQTT 服务器，可在任意 stream server 上运行，旨在解决 Mosca 在生产环境中的性能与稳定性问题。
- ⭐ 项目热度：约 2k stars、241 forks、48 watchers、75 issues、18 PR、861 commits；采用 MIT 许可证。
- 📦 安装方式：使用 `npm install aedes`，同时提供 Docker 支持。
- 🔌 API：主要提供 `Aedes` class 与 `Client` class。
- ✅ 核心特性：完整兼容 MQTT 3.1/3.1.1，支持 TCP、SSL/TLS、WebSocket、消息持久化、自动重连、离线缓冲、背压 API、高可用、可集群、认证授权、`$SYS`、可插拔中间件与动态 Topics。
- ⚠️ 协议限制：暂不支持 MQTT 5.0；支持 Bridge Protocol，但仅限入站连接。
- 🌉 桥接行为：普通发布时 `retain` 标志会被 Aedes 消费并设为 `false`；通过 Bridge Protocol 连接时，`retain` 标志会按原样传播。
- 🧩 集群要求：集群需要 MongoDB、Redis 等磁盘数据库；测试与用户反馈显示最佳性能和稳定性组合是 `aedes-persistence-mongodb` 搭配 `mqemitter-redis`。
- 🧪 集群测试：`aedes-tests` 仓库用于测试 Aedes 集群及不同 emitter/persistence 组合，可作为集群实践起点。
- 🧱 扩展插件：包括 `aedes-logging`、`aedes-stats`、`aedes-cli`、`aedes-protocol-decoder`、`aedes-server-factory`。
- 💾 持久化插件：支持内存、MongoDB、Redis、SQLite、LevelDB、NeDB。
- 📡 MQEmitter 插件：包括 `mqemitter`、Redis、MongoDB、child-process、client/server、P2P、Aerospike。
- 🧪 性能基准：1000 客户端发送 5000 条 QoS 1 消息；Aedes 内存无集群约 178.5 秒、28114 msg/s；Redis 持久化 + Redis emitter + 集群约 114.4 秒、45896 msg/s；Mongo 持久化 + Redis emitter + 集群约 112.8 秒、47464 msg/s；Mosca 约 264.9 秒、18926 msg/s。
- 🏗️ 采用案例：`node-red-contrib-aedes`、`Mqtt2Mqtt`、Kuzzle 等项目使用 Aedes 作为 MQTT Broker。
- 🔐 安全提示：消息通过 `authorizePublish` 回调后即被视为有效，即使之后权限被撤销，消息仍有效；时间敏感消息建议使用 QoS 0 或 clean session。
- 🤝 贡献与支持：欢迎提交 PR；生产环境 bug/泄漏可提交 PR 或联系维护者获取付费支持；项目有 backers 与 sponsors。
- 📄 许可证：MIT。

---

### [发布 v4.22.3 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v4.22.3)

**原文标题**: [Release v4.22.3 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v4.22.3)

Express v4.22.3 已发布，重点是修复安全漏洞、支持 QUERY 请求条件重新验证，并更新依赖与 CI 发布流程，同时新增两位首次贡献者。

- 🚀 版本 v4.22.3 由 UlisesGascon 于 9 月 14 日 06:45 发布，提交为 899b524，并带有 GitHub 验证签名。
- 🛡️ 安全更新：将 path-to-regexp 升级到 0.1.13，以修复 CVE-2026-4867，由 @baryman 在 #7135 贡献。
- ✅ 新功能：允许 QUERY 请求的条件重新验证（v4），由 @Cherry 在 #7377 提交。
- 📦 依赖更新：qs 更新为 ~6.16.0，由 @lazerg 在 #7440 贡献。
- ⚙️ CI 改进：新增 npm staged publication 并支持 dist-tag，由 @UlisesGascon 在 #7465 完成。
- 🧾 发布提交：4.22.3 由 @UlisesGascon 在 #7466 发布，完整变更日志为 v4.22.2...v4.22.3。
- 👥 贡献者：Cherry、UlisesGascon 及其他 2 位贡献者；新贡献者为 @baryman 和 @lazerg。
- 📊 仓库概况：expressjs/express 为公开项目，约 69.5k Star、25k Fork、107 个 Issue、123 个 PR。
- 💬 发布反应：获得 👍6、❤️2、🚀4，共 10 人参与反应。
- ⚠️ 页面提示：部分区域加载出错并要求重新加载，标签筛选与加载也出现错误，未找到结果。

---

### [](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

**原文标题**: [The Unified Gateway for APIs, AI, and MCP - Zuplo](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

Zuplo 是面向 API 与 AI 的统一网关，用一个可编程策略引擎统一管理 API、LLM 和 MCP 调用，覆盖认证、限流、支出上限、审计与可观测性，让应用调用模型、AI Agent 调用你的 API 都经过同一网关，并可快速上线、控制成本与用量计费。

- 🚪 **统一网关**：Zuplo 同时面向 API 和 AI，统一处理出站 LLM 调用与入站 AI Agent/MCP 流量。
- 🔄 **双向流量**：出站是产品调用 LLM，入站是 AI Agent 通过 MCP 调用你的 API；两者都需要身份、路由、配额和审计。
- 🧩 **一个策略引擎，四大能力**：Agents、Users、APIs & MCPs、LLMs；无需新增供应商即可按需启用。
- 🤖 **MCP Gateway/Server**：把 OpenAPI 操作标记为 MCP 工具或资源，部署后 Agent 可在 `/mcp` 连接；支持 OAuth 2.1、PKCE、DCR + CIMD。
- 🛡️ **安全治理**：认证、Schema 校验、限流和提示注入防御在网关拦截；示例中 12.4k 请求被阻止，0 到达源站。
- 💸 **成本控制**：动态限流防止源站成本飙升，AI Token 预算可硬性返回 429；示例 14 天节省 42.9k 美元，总支出降低 41%。
- 📊 **可观测性**：每次 MCP 工具调用都归属到用户、客户端和策略，实时看板可看调用、拒绝、延迟，并可导出 Datadog 或 SIEM。
- 💳 **商业化**：内置套餐、配额和按用量计费，连接 Stripe，无需自建计费基础设施。
- 🧑‍💻 **代码接入简单**：出站保留 OpenAI SDK，仅替换 base URL；入站用 OpenAPI 的 `x-zuplo-route` 声明 MCP 工具。
- 🚀 **上线与规模**：分钟级上线，99.99% 正常运行时间 SLA，SOC 2 Type II，1B+ 终端用户，300+ 边缘节点，约 20 秒部署。
- 📈 **客户成果**：Blockdaemon 节省 70%+ 成本、硬件足迹降 90%；Yext 提升扩展、安全与合规；Finsolutia 数小时上线 MCP Server。
- ✅ **免费层**：每月 10 万请求，无需信用卡或销售电话，可免费开始或预约演示。

---

### [](https://fingerprint.com/try/bot-detection/?utm_source=NodeWeekly09172026)

**原文标题**: [Fingerprint | Industry-leading Bot Detection](https://fingerprint.com/try/bot-detection/?utm_source=NodeWeekly09172026)

Fingerprint 提供面向开发者与反欺诈团队的隐形机器人/AI 检测 API，可在 10 行代码内接入，无需 CAPTCHA，既能拦截恶意自动化，也能识别并放行合法 AI 代理，覆盖注册、结账、账户接管、内容抓取等场景。

- 🕶️ 隐形检测：无 CAPTCHA、无挑战，保持顺畅用户体验。
- ⚡ 快速接入：`npm i @fingerprint/agent`，约 10 行代码，免费开始。
- 🤖 AI 代理感知：识别 ChatGPT、Gemini、Claude、Manus 等签名、验证或未知代理。
- 🛡️ 核心用例：阻止假注册、机器人结账、账户接管和内容抓取。
- 🔍 单一接口多信号：`api.fpjs.io/v4/events/{event_id}`，判断自动化流量真实意图。
- 🧰 规则引擎：无需写代码即可按浏览器机器人、开发者工具、反检测浏览器、虚拟机/数据中心 IP 等规则拦截。
- 🧑‍💻 技术栈兼容：支持 JavaScript、React、Next.js、Preact、Vue、Nuxt、Angular、Svelte 等。
- 🏢 受信任：Booking.com、Manus、Dropbox、Plaid、Binance、Resend 等使用。
- 🌟 开源基础：GitHub 31.2K+ stars，NPM 月下载 5,400,000+。
- 🚀 上线简单：包管理器或 CDN 分钟级设置，无需信用卡或销售通话。
- 💬 客户认可：Northsea CEO 称其提升数据质量与信任。

---

### [](https://select.supabase.com/?utm_source=newsletter&utm_medium=email&utm_campaign=nodeweekly&dub_id=FrA6vspUPpul6hml)

**原文标题**: [Select26 | Oct 2 | Supabase curated day of talks](https://select.supabase.com/?utm_source=newsletter&utm_medium=email&utm_campaign=nodeweekly&dub_id=FrA6vspUPpul6hml)

Supabase Select 26 是由 Supabase 主办、联合业界顶尖构建者的一日演讲活动，聚焦开发者工具、Postgres 与真实产品构建。活动于 10 月 2 日在旧金山 555 20th Street 线下举行，仅限申请参加，票价 256 美元/人，需通过 Luma 申请。

- 🗓️ 活动名称与形式：Supabase Select 26，一日精选演讲，线下参与且需申请。
- 📍 时间地点：10 月 2 日，旧金山 555 20th Street。
- 💵 门票：每人 256 美元，需通过 Luma 申请。
- 🎙️ 嘉宾阵容：Steve Wozniak、Andrew Ng、Paul Copplestone、Ant Wilson 等；并涵盖 OpenAI、Anthropic、Y Combinator、Stripe、Replit、Postman 等公司代表及 Supabase 团队。
- 🔮 抢先看点：第一手了解 Supabase 即将发布的内容，认识热门开发者工具公司，获取 Postgres 最新动态。
- 🛠️ 构建者分享：主舞台炉边谈话，Build Stage 功能深度解析，展示真实产品如何构建。
- 🤝 团队互动：在 Ask Supabase 展台向 Supabase 工程师提问。
- 🎫 其他信息：门票现已开放；由 Supabase 主办，设有首席赞助商；活动有行为准则，并开放演讲申请。

---

### [npm图表](https://www.npmchart.com/)

**原文标题**: [npmchart](https://www.npmchart.com/)

npmchart 是一个用于查看任意 npm 包下载趋势、版本发布和仓库活动的工具，并支持多包对比，首页展示了热门包与常见对比场景。

- 🔍 支持查看任意 npm 包的下载趋势、发布记录和仓库活动
- ⚖️ 支持同时对比多个 npm 包
- 📈 layerchart v2.5.0：可组合的 Svelte 图表组件，周下载 202.2K，增长 +46%
- 🧩 svelte v5.57.0：增强型 Web 应用框架，周下载 5.1M，增长 +61%
- 🚀 @sveltejs/kit v2.70.3：快速构建 Svelte 应用，周下载 2.4M，增长 +56%
- ⚡ vite v8.3.0：原生 ESM 驱动的 Web 开发构建工具，周下载 163.8M，增长 +66%
- 📊 数据可视化对比示例：layerchart、layercake、@unovis/svelte、svelteplot、@sveltejs/pancake
- 🖥️ 前端框架对比示例：react、svelte、vue、@angular/core
- 🛠️ 构建工具对比示例：vite、webpack、rollup、esbuild

---

### [express · npm 下载量与仓库活动](https://www.npmchart.com/p/express)

**原文标题**: [express Â· npm downloads and repository activity](https://www.npmchart.com/p/express)

Express 是一个快速、无偏好、极简的 Web 框架，最新版本为 5.2.1，采用 MIT 许可，已发布 289 个版本，由 wesleytodd、jonchurch、ctcpip 等维护。
- 🚀 定位：快速、无偏好、极简的 Web 框架。
- 🏷️ 版本与许可：最新版 5.2.1；MIT 许可证；共 289 个版本。
- 🧑💻 维护者：wesleytodd、jonchurch、ctcpip，另有 2 人。
- 🔗 关键词：framework、sinatra、web、http、REST、RESTful、router、app、API、npm、GitHub、website。
- 📊 下载数据：周下载量为 0，较前一周无变化；近 30 天为 0。
- ⭐ 项目指标：Stars、最新提交、开放 issue 等显示为“—”。
- 🗓️ 统计区间：2026-06-20 至 2026-09-17（90 天）总下载量为 0，该范围内无下载；最近 7 天及按版本下载数据不可用。
- 📦 发布历史：自 2010-12-29 起共发布 289 个版本。
- 🆕 近期版本：4.22.3（4 天前）、4.22.2（4 个月前）、4.22.1/5.2.1/5.2.0/4.22.0（10 个月前）、5.1.0（去年）、4.21.2（2 年前）。
- 🧩 页面栏目：Commits、Issues、Pull requests。

---

### [](https://nesbitt.io/2026/09/10/package-manager-trends.html)

**原文标题**: [Package Manager Trends | Andrew Nesbitt](https://nesbitt.io/2026/09/10/package-manager-trends.html)

概述摘要：过去十六周包管理生态的主线是防御性功能快速普及——发布冷却、安装脚本拦截、恶意软件扫描和注册表管控——同时路径遍历、凭据泄露和命令注入三类漏洞反复被修复，供应链资助与治理也在推进。

- 🧊 发布年龄冷却成为最普遍新功能：Deno、npm、Yarn、Bundler、mise、Hex、Mamba、Cargo nightly 等加入 `min-release-age` / `-Zmin-publish-age`；Dependabot 默认三天冷却。
- 🚨 冷却与安全更新冲突时，Dependabot、Renovate、Hex 支持在有安全公告时解除限制；npm 12 和 pnpm 12 对未识别配置键报错。
- 🚫 安装脚本默认阻止：npm 12 默认阻止 lifecycle scripts 并用 `allowScripts` 白名单；Bun 1.4 限制自动信任为 npm 源；pnpm 将 `allowBuilds` 扩展到 git 托管依赖。
- 🔒 安装源限制收紧：npm 12 的 `allow-git` / `allow-remote` 默认 `none`；Composer 2.10 禁用下载失败时从 dist 回退到 source。
- 🦠 恶意软件检查前移：Composer 2.10、uv、npm registry 在安装或发布时扫描；npm 可给包元数据附加 `contentPolicy` 判定。
- 🔎 内置审计扩展：Deno、uv、Homebrew、Bun、Hex 增加或扩展 `audit` / 漏洞提示命令。
- 🧱 项目配置与机器级信任分离：pnpm 阻止项目级配置重定向凭据、展开环境变量、影响自更新等；mise 将 `credential_command` 限制为全局并加入 `MISE_SAFE=1`；Renovate 采用于锁文件更新。
- ✅ 完整性校验收紧：pnpm 对 tarball 完整性不匹配硬失败，并拒绝缺少 `integrity` 的锁文件条目；uv 0.12 强制 `--require-hashes`，拒绝仅 MD5 源；Bun 1.4 为 GitHub 和 tarball 依赖记录 SHA-512。
- 🏛️ 注册表控制加强：npm 分阶段发布与 2FA 绕过令牌限制；Packagist 不可变版本与透明日志；PyPI 拒绝向超过 14 天的 release 添加新文件；NuGet API key 寿命从 365 天降至 30 天；AUR 在接管事件后禁用孤儿包认领。
- 🧩 工作区/单仓库支持落地：PDM、Conan、pixi、Hatch、uv、mise；pnpm 12 Rust 重写达到稳定；GitHub Actions 的 `uses:` 被 pnpm、Dependabot、Renovate 当作依赖管理。
- 🐛 路径遍历漏洞最常见：十六周中至少十四周出现修复，涉及 uv、pnpm、RubyGems、Podman、Composer、Docker、Flatpak、Poetry 等；pnpm 修了四次，Docker 三次，Composer 两次。
- 🔑 凭据错发或泄露频发：Cargo、Dependabot、ORAS、Composer、Renovate 修复相关问题；RubyGems.org CDN 因缓存错误把一个账户的旧 API key 发给另一个账户。
- 💥 命令注入通过 VCS URL 或引用出现：pnpm、Docker、Composer 中招；Renovate 十个公告中有四个属于此类。
- 🌱 可持续与治理推进：Alpha-Omega 资助 PHP Foundation 与 Ruby Central 安全工程师驻留；Rust Foundation 维护者基金公布首批驻留者；Sovereign Tech Agency 向 Flatpak 投资 €508,640；NYU Tandon 推出供应链安全运营中心；PSF 举行首次 Python Packaging Council 选举。
- ⚰️ 弃用与 EOL：Helm v3 定于 2027 年 2 月 EOL；Go 放弃 Bazaar；pip 旧解析器 2027 年移除；Nixpkgs 核心团队解散；Maven 3.8.x 结束支持。

---

### [发布 v12.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0)

**原文标题**: [Release v12.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0)

npm CLI 正式发布 v12.0.0（2026-07-08），带来多项破坏性变更、命令移除、默认行为与安全策略调整，以及内部依赖升级，升级前需重点评估兼容性。

- 🚨 重大版本：npm v12.0.0 于 2026-07-08 发布，包含多项 BREAKING CHANGES。
- 📦 输出变更：`npm view --json` 现在始终返回数组。
- 🧾 SBOM 变更：`npm sbom --sbom-format=cyclonedx` 改为使用各包 `package.json` 中的 `name`，而非磁盘目录名；根组件和别名依赖的 `name`、`bom-ref`、`purl` 可能变化。
- 📖 手册页：全局安装时不再向系统注册 man 页面，`man npm-install` 不再可用，但 `npm help install` 不受影响。
- 🛠️ `npm pkg`：输出不再强制为 JSON，可获取单值，非 JSON 输出更接近 `npm view`。
- 🗑️ 移除 shrinkwrap：删除 `npm shrinkwrap`、`shrinkwrap` 配置别名，且不再加载或遵守项目根目录及依赖 tarball 中的 `npm-shrinkwrap.json`；应重命名为 `package-lock.json`，或使用 `bundleDependencies`。
- 👤 资料字段：npm registry 移除 Twitter 和 Freenode 个人资料字段，用户无法再设置或查看。
- 🔗 Node 路径解析：不再通过 `which node` 解析 node 路径；`process.execPath` 已由 Node 设置为真实路径，可能影响依赖 PATH 解析的脚本。
- 📄 `npm pack` 与 `npm publish`：`--json` 输出格式改变，现在始终一致。
- ⭐ 命令移除：删除 `star`、`stars` 和 `unstar` 命令。
- 🔐 用户认证：移除 `npm adduser`，请在 npm 网站创建和管理账号，命令行使用 `npm login` 认证。
- 🌐 Git 协议：使用 git 时保留 HTTPS 协议。
- 📜 许可证默认值：`npm init` 默认 license 从 `ISC` 改为空字符串；未设置时新包省略 license 字段。
- 🟢 Node 支持：npm 现在支持 `^22.22.2 || ^24.15.0 || >=26.0.0`。
- 🔒 依赖来源限制：`allow-git` 和 `allow-remote` 默认 `none`；需设为 `all` 或 `root` 才能安装 git 或用户提供的 tarball URL 依赖。
- ⏱️ 安装顺序：根 `preinstall` 现在在依赖安装前运行。
- ⚠️ 配置校验：`.npmrc` 未知配置、未知 CLI 标志、缩写标志、单连字符多字符简写现在会抛错，而非仅警告。
- 🚫 生命周期脚本：依赖生命周期脚本默认被阻止，除非根包 `allowScripts` 策略允许；安装后运行 `npm install-scripts approve` 记录批准，再运行 `npm rebuild` 执行新批准脚本。
- 🧹 预发布模式：移除 npm 12 和 workspaces 的预发布模式（#9735）。
- ⬆️ 依赖升级：多个内部依赖升级，包括 `@npmcli/arborist@10.0.0`、`@npmcli/config@11.0.0`、`libnpmaccess@11.0.0`、`libnpmpublish@12.0.0` 等。
- 🙌 贡献者与反馈：贡献者包括 `reggi`，发布页有 2 个资产，并获得多个 🎉 与 ❤️ 反应。

---

### [](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata/)

**原文标题**: [npm publish-time malware scanning and dual-use metadata - GitHub Changelog](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata/)

npm 正在引入发布时恶意软件自动扫描，并新增针对双用途内容的元数据与发布要求，以加强供应链安全。

- 🔍 npm 推出发布时自动扫描：新发布包在可安装前会被扫描，结果可能是正常发布、暂扣人工审核或直接阻止。
- ⏱️ 扫描会带来短暂延迟，通常约 5 分钟；高峰期或视包内容与大小可能超过 15 分钟，且这不是服务保证。
- 🤖 若自动化流程假设发布后立即可安装，需要更新为容忍短暂可用延迟。
- 🏷️ 扫描期间 `npm dist-tag` 仍可用；但 `npm deprecate`、`npm unpublish` 等依赖已发布版本的操作需等包可用后才能用。
- 🚫 若包被阻止，发布者可能收到通知并有机会申诉；根据问题严重性和置信度，可能对维护者账号采取进一步行动。
- 🛡️ npm 会阻止可检测的恶意软件，并持续改进检测覆盖和缩短扫描时间；允许范围见 npm Acceptable Use Policies。
- 🧾 新增双用途内容元数据要求：维护者可在 `package.json` 中使用 `contentPolicy` 字段声明具有安全相关能力、但用途合法的内容。
- 📄 声明双用途内容还必须在包根目录添加纯文本 `DISCLOSURE` 文件，说明双用途功能及其合法用途，供 Trust & Safety 审核。
- ⚙️ 声明该元数据可能触发额外自动扫描，但不自动授予发布资格；双用途包仍可能被个案审核。
- 🔐 双用途包必须通过强制 2FA 的方式发布，例如 trusted publishing、OIDC、交互式 2FA 或 staged publishing；不允许用绕过 2FA 的令牌直接发布。
- 📌 双用途声明必须持久保留：新版本不能移除 `contentPolicy` 或 `DISCLOSURE`，否则发布会被拒绝。
- 📣 该要求将逐步强制执行；npm 正邮件联系需要添加元数据的双用途包维护者，更多信息见相关文档与社区讨论。

---

### [](https://github.com/nodejs/Release/issues/1161)

**原文标题**: [Plans for npm 12 · Issue #1161 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1161)

npm 团队正在推进 npm 12，预计 2026 年 7 月发布。这是一次以安全为核心的破坏性更新，目标是把当前自动执行的 `npm install` 行为改为需要显式选择加入，并希望将这些保护性默认值尽快带到 Node.js 24 和 Node.js 26 等活跃发布线。

- 🔐 npm 12 是安全导向版本，所有破坏性变更都将“自动执行”改为“用户主动启用”
- 📦 安装脚本改为选择性启用：`allowScripts` 默认关闭，依赖的 `preinstall`、`install`、`postinstall` 不再自动运行
- 🛠️ 原生 `node-gyp` 构建也受影响：即使包只提供 `binding.gyp` 而没有显式安装脚本，也会被阻止
- 🔗 git/file/link 依赖的 `prepare` 脚本同样被阻止
- ✅ 可通过 `package.json` 的 `allowScripts` 按包授权，并使用 `npm approve-scripts` 和 `npm deny-scripts` 管理，对应 RFC 54
- 🚫 git 依赖改为选择性启用：`--allow-git` 默认为 `none`，除非显式允许，否则不再解析直接或传递 git 依赖
- 🧨 该变更关闭了 git 依赖的 `.npmrc` 覆盖 git 可执行文件的代码执行路径，即使使用 `--ignore-scripts` 也可能被触发
- 🌐 远程 URL 依赖改为选择性启用：`--allow-remote` 默认为 `none`，不再解析 https tarball 等直接或传递远程依赖
- 📁 相关 `--allow-file` 和 `--allow-directory` 在 npm 12 中保持当前默认值
- ⚠️ 上述变更已在 npm 11.16.0 及之后版本中通过警告形式提供，便于提前测试
- 🧪 希望进入 Node 24 和 26 的理由：多数用户处于活跃线，且 Node LTS 政策允许基于安全理由将 semver-major 作为 semver-minor 发布
- 🛡️ 近年来 event-stream、Lazarus、chalk/debug、Shai-Hulud、Axios 等供应链攻击都利用了安装脚本或安装时解析作为入口
- 📋 测试要求：不引入 Node 自身测试套件新失败，不破坏 `citgm` 包集安装/测试，不产生不兼容的 `package-lock.json` 变更
- ⚙️ 将像 npm 10 一样，通过 GitHub Actions 的 node-integration 工作流对所有 npm 12 预发布版运行测试
- 🗓️ 时间线：`npm@12.0.0-pre.0` 已于 2026 年 5 月 20 日发布，`12.0.0-pre.1` 待发布
- 🧩 计划流程：预发布期间向 Node.js `main` 提交 CI-only PR，稳定后提交可审查 PR，随后回移植到 Node 26 和 Node 24
- 🎯 npm 12 正式版目标为 2026 年 7 月，并计划届时提升为 `latest`
- 🔙 Node 26 和 Node 24 的回移植与发布目前为暂定，取决于预发布测试进展
- 🔗 相关链接包括 GitHub 博客公告、社区讨论、RFC 54、npm 与 Node 集成指南，以及 npm 9 和 npm 10 的先前计划

---

### [GitHub Actions 新增 cache-mode 以限制缓存投毒风险 | Socket](https://socket.dev/blog/github-actions-cache-mode)

**原文标题**: [GitHub Actions Adds cache-mode to Limit Cache Poisoning Risk | Socket](https://socket.dev/blog/github-actions-cache-mode)

GitHub Actions 新增 `cache-mode`，通过最小权限控制缓存访问，专门缓解近期供应链攻击中使用的缓存投毒技术；该设置可按工作流或作业限制缓存读写，但不能覆盖所有 Actions 风险。

- 🛡️ **缓存投毒是什么**：一个上下文写入共享 Actions 缓存的条目，可被另一个上下文恢复并执行；攻击者可借此植入恶意构建产物或依赖。
- 🎯 **关联攻击事件**：该技术被用于 2024 年 Ultralytics PyPI 包入侵，以及 2026 年 5 月 TanStack npm 包攻击；后者结合 `pull_request_target` 发布 42 个 `@tanstack/*` 包的 84 个恶意版本。
- 🔏 **构建来源无法检测**：SLSA provenance 和 Sigstore 签名仍可能通过，因为它们证明构建来源，不保证从缓存拉取的输入未被篡改。
- ⚙️ **四种访问模式**：`read` 可恢复但不可保存，是 `pull_request_target` 等低信任事件默认值；`write` 可恢复和保存，是 `push` 等可信事件默认值；`write-only` 只保存不可恢复；`none` 完全禁止缓存访问。
- 🧩 **权限控制细化**：作业级设置覆盖工作流级设置，缓存服务强制执行；可复用工作流不能获得超过调用者授予的缓存权限。
- ⚠️ **低信任事件警告**：在低信任事件中声明 `write` 或 `write-only` 会重新引入投毒风险，GitHub 会添加警告注释。
- 🤖 **AI 代理工作流建议**：GitHub 推荐对 AI 代理工作流使用 `cache-mode: none`，以移除执行 issue 或 PR 文本等不可信输入时的缓存风险。
- 📝 **write-only 来自反馈**：2026 年 5 月设计初版只有 `read`、`write`、`none`；安全研究员 Adnan Khan 推动增加 `write-only`，该模式已在最终版本发布。
- 🚧 **不覆盖其他风险**：GitHub 已于 2026 年 6 月为多数不可信触发器启用只读缓存默认值；但 `cache-mode` 仍不解决检出不可信代码、运行包生命周期脚本或生成 OIDC 令牌等风险。
- ✅ **核心建议**：为每个工作流或作业只授予其所需的缓存访问权限，遵循最小权限原则。

---

### [](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

**原文标题**: [Postmortem: TanStack npm supply-chain compromise | TanStack Blog](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

TanStack 发布 2026-05-11 npm 供应链攻击事后分析：攻击者串联 GitHub Actions `pull_request_target`、缓存投毒与 OIDC token 内存提取，发布 42 个 `@tanstack/*` 包的 84 个恶意版本；约 20 分钟后被 StepSecurity 研究员发现，受影响版本已全部废弃并由 npm 移除，2026-05-15 官方确认全部安全。

- ✅ 状态：2026-05-15 官方发布全部安全通告；仅 Router/Start 仓库受影响，其他 TanStack 包安全。
- 📦 影响范围：42 个 monorepo 包、84 个版本，每包两个恶意版本，约间隔 6 分钟发布。
- 🧪 确认干净：`@tanstack/query*`、`table*`、`form*`、`virtual*`、`store` 及 `@tanstack/start` 元包等未受影响。
- ⏱️ 攻击窗口：2026-05-11 19:20–19:26 UTC，恶意版本通过 OIDC 认证直接发布到 npm。
- ☠️ 恶意行为：安装受影响版本会触发恶意 `optionalDependencies`，拉取 fork 中 payload 并执行约 2.3 MB 混淆脚本 `router_init.js`。
- 🔑 窃取目标：AWS、GCP、Kubernetes、Vault、`~/.npmrc`、GitHub token、SSH 私钥等凭据。
- 🕵️ 外泄方式：通过 Session/Oxen 文件上传网络外泄，端到端加密，无传统 C2 域名。
- 🧬 自我传播：枚举同一维护者的其他 npm 包并重新发布，注入相同恶意依赖。
- 🧨 攻击链：`pull_request_target` “Pwn Request” + GitHub Actions 缓存投毒 + 从 runner 内存提取 OIDC token。
- 🧱 根因 1：`bundle-size.yml` 对 fork PR 使用 `pull_request_target`，并检出、运行 fork 控制代码。
- 💾 根因 2：`actions/cache` 后置保存不受 `permissions` 限制，毒缓存可跨 PR 与 main 发布流程共享。
- 🪪 根因 3：`release.yml` 拥有 `id-token: write`，恶意代码从 `/proc/<pid>/mem` 提取 OIDC token，绕过正常发布步骤。
- 🧾 关键事实：没有 npm token 被盗，npm 发布工作流本身未被攻破。
- 🕒 时间线：5/10 创建伪装 fork；5/11 开 PR #7378，force-push 落地恶意提交，污染 pnpm 缓存后恢复为 0 文件 no-op。
- 🚀 触发：19:15 Release workflow 重跑恢复毒缓存；19:20 与 19:26 两批恶意版本发布。
- 🔍 检测：19:46 StepSecurity 的 `ashishkurmi` 开 issue #7383，发布后约 20–26 分钟公开检测。
- 🛑 响应：20:19 开始废弃，21:03 完成全部 84 版本废弃；npm 于 22:13–23:55 移除 tarball。
- 🧹 加固：清理 TanStack GitHub 缓存，重构 `bundle-size.yml`，增加 `repository_owner` 守卫，第三方 action 固定 SHA。
- ⚠️ 建议：2026-05-11 安装过受影响版本的主机应视为可能被攻破，轮换 AWS、GCP、K8s、Vault、GitHub、npm、SSH 凭据。
- 🔎 IOC：`optionalDependencies` 含 `@tanstack/setup` 指向 `github:tanstack/router#79ac49...`；存在 `router_init.js`；特定 `Linux-pnpm-store` 缓存键。
- 🌐 网络 IOC：`filev2.getsession.org`、`seed{1,2,3}.getsession.org`；二级 payload 位于 `litter.catbox.moe`。
- 👤 攻击者标识：`zblgg`、`voicproducoes`；伪造提交身份 `claude <claude@users.noreply.github.com>`；fork `zblgg/configuration`。
- ✅ 做得好：外部研究快速报告，维护者跨时区协调，公开 IOC 数小时内形成。
- ❌ 不足：无内部发布告警；`pull_request_target` 未审计；浮动 action refs；npm unpublish 受限；7 位维护者扩大风险；OIDC 发布无逐次审查。
- 🍀 幸运：payload 破坏测试使正常发布步骤跳过，攻击更早暴露；若攻击者更谨慎可能潜伏更久。
- ❓ 待查：`bundle-size` 是否调用 `actions/cache`、初始 PR head 内容、恶意提交如何进入 fork、`voicproducoes` 身份、npm cache 是否污染、其他 fork/仓库是否含 payload、实际下载量、维护者机器是否受影响。
- 📚 参考：跟踪 issue `TanStack/router#7383`；GitHub 安全公告 `GHSA-g7cv-rxg3-hmpx`；相关缓存投毒、Pwn Request 与 tj-actions 事件研究。

---

