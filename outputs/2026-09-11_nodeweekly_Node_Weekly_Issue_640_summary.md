### [](https://blog.cloudflare.com/workers-module-registry-nodejs/)

**原文标题**: [How we rebuilt Cloudflare Workersâ module registry for Node.js compatibility | Cloudflare Blog](https://blog.cloudflare.com/workers-module-registry-nodejs/)

Cloudflare 重写了 Workers 运行时核心开源组件 workerd 的模块注册表，使其更快、更符合标准，并更接近 Node.js 的模块解析、加载与缓存行为。开发者现在可通过 new_module_registry 兼容标志启用，但该标志尚未默认开启。

- 🚀 目标：让 ESM、CommonJS、WebAssembly 等模块的解析、加载和缓存更标准、更接近 Node.js，并支持更大型的 Node.js 应用。
- ⚙️ 启用方式：在 Worker 配置中加入 `"compatibility_flags": ["new_module_registry"]`；目前没有默认启用日期，必须显式开启。
- 📦 Node.js 兼容进展：Workers 已支持服务器场景中所有稳定 Node.js API，并默认启用；所有计划支持最大 64 MiB 部署包，取消压缩包大小限制。
- 🔗 import.meta 支持：启用后 `import.meta.url`、`import.meta.main`、`import.meta.resolve()` 均可工作；`main` 仅入口模块为 `true`。
- 🌐 说明符按 URL 解析：相对导入等同于 `new URL(specifier, base)`，完整 URL、查询字符串和片段都被正确处理；不同查询或片段会生成不同模块实例。
- 🧩 node: 内置模块：无论通过哪种路径访问，`node:` 内置模块都解析到同一模块实例。
- 📥 导入属性校验：`with { type: 'json' }` 正确校验；`text`/`bytes` 被识别但暂不支持并抛出 `TypeError`；未知属性或类型不匹配会报错。
- 🔄 require(esm)：`require()` ES 模块遵循 Node.js 规则：优先返回名为 `'module.exports'` 的导出，否则返回命名空间对象；workerd 的 `node:` 内置模块例外，直接返回 default 导出。
- ⏳ require 限制：若被 `require` 的模块或依赖图含顶层 await，会抛出错误；应改用 `import()`。
- 🧾 错误一致性：静态 `import`、动态 `import()`、`require()` 的解析失败使用一致错误类别和消息；找不到模块是普通 `Error`，无效说明符是 `TypeError`。
- 🧱 Wasm 源阶段导入：支持 `import source wasmModule from './add.wasm'` 和 `import.source()`，直接获得 `WebAssembly.Module`；仅限 Wasm，其他类型抛 `SyntaxError`。
- ⚡ 新实现优势：旧注册表按文件系统路径处理说明符，缺少 `import.meta.url`，整包预编译且每个 V8 isolate 私有缓存；新实现以 URL 为基础，支持懒编译和缓存共享。
- 🛠️ 打包影响：Wrangler 默认用 esbuild 打包成单模块，Vite 8/Rolldown 可生成入口和代码分块；新注册表让打包器减少转换，更多交给运行时处理。
- ✅ 兼容与反馈：旧注册表仍保留，已部署 Worker 继续工作；遇到疑似回归可向 workerd 仓库反馈。

---

### [Node.js 兼容性现已默认启用 · 更新日志](https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/)

**原文标题**: [Node.js compatibility is now enabled by default Â· Changelog](https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/)

自 2026 年 8 月 4 日起，Cloudflare Workers 对兼容日期为 2026-08-04 或更晚的项目默认启用 Node.js 兼容性，旧项目不受影响且仍可手动选择启用。

- 🚀 Workers 现在默认启用 `nodejs_compat` 和 `nodejs_compat_v2` 兼容标志，适用于兼容日期为 2026-08-04 或更晚的项目。
- 📅 对这些兼容日期，无需再显式使用这些标志，因为兼容日期本身会启用相同行为。
- 🧩 所有 Workers 运行时支持的 Node.js 内置 API 默认可用，包括 `node:crypto`、`node:buffer`、`node:stream`、`node:net`、`node:dns`、`node:fs`、`node:http` 等。
- 📦 依赖这些 API 的 npm 包无需额外配置即可工作。
- 🕰️ 使用更早兼容日期的 Workers 不受影响，仍可通过在 `compatibility_flags` 中添加 `nodejs_compat` 来选择启用。
- 🆕 新项目无需添加任一标志；现有项目可更新兼容日期而无需移除它们。
- ⚙️ Wrangler、Miniflare、Cloudflare Vite 插件和 Vitest Pool Workers 在启动运行时会忽略这些冗余标志。
- 🚫 若要完全关闭 Node.js 兼容性，需移除 `nodejs_compat` 和 `nodejs_compat_v2`，并添加 `no_nodejs_compat` 和 `no_nodejs_compat_v2` 标志。
- 📚 更多信息请参阅 Node.js 兼容性文档。

---

### [部署与扩展容器](https://master.dev/courses/kubernetes/?utm_source=email&utm_medium=nodeweekly&utm_content=kubernetescooper)

**原文标题**: [Deploy & Scale Containerized Applications | Master.dev](https://master.dev/courses/kubernetes/?utm_source=email&utm_medium=nodeweekly&utm_content=kubernetescooper)

本课程由 Erik Reinert（TheAltF4Stream）主讲，时长约 7 小时 56 分钟，发布于 2026 年 9 月 2 日，评分 5，属于 Cloud & DevOps 学习路径，主题涵盖 DevOps、Docker 与 AWS。课程通过从本地 Kind 集群到 Amazon EKS 的实战，系统讲解生产级 Kubernetes：Pod、Deployment、Service、健康检查、自动扩缩容、GitOps、安全与可观测性。

- 🎯 学习目标：自信部署和管理容器化应用，建立 Pod、Deployment、Service 的核心心智模型，并搭建可持久演进的基础设施。
- 🧱 先修要求：熟悉 Docker、Git、命令行和 AWS。
- 🔁 Kubernetes 核心：通过“循环”持续协调期望状态与实际状态，实现自我修复、可调试与可扩展。
- 🌐 本地 vs 云集群：Kubernetes 提供通用标准 API，同一套资源声明可运行在笔记本、云和边缘环境，简化多云策略。
- 🧪 Kind 起步：在 Docker 容器中创建本地 Kubernetes 集群，学习用 kubectl 声明式创建、配置和删除集群。
- 📦 Pod 与应用运行：Pod 可包含一个或多个容器；用 `kubectl run` 和 `kubectl delete` 命令式创建与删除应用。
- ♻️ Deployment 与自愈：Deployment 维护期望副本数，Pod 崩溃或被删除后会被自动重建。
- 📈 扩缩容与 k9s：演示 Deployment 扩缩容及 Pod 状态变化，推荐使用 k9s 终端 UI 管理 Kubernetes。
- 🔌 Services：Deployment 管理生命周期，Service 暴露 Pod，解决 Pod IP 易变问题；对比 NodePort、端口转发和 Ingress/Gateway API。
- 💾 持久化：无卷的 Postgres Pod 删除后数据丢失；需 PersistentVolume/PVC 等持久存储。
- 🗳️ etcd/Raft：etcd 使用 Raft 共识算法，通过领导者选举和多数派 quorum 保证一致、容错的状态。
- 📝 声明式 Manifest：将期望状态写入 Git 中的 YAML，可 diff、重建、审查，作为集群外单一事实来源；标签和选择器用于分组与路由。
- 🩺 健康检查：Readiness、Liveness、Startup 探针让 Kubernetes 判断应用是否健康和可接流量，失败时安全替换容器。
- 🔐 配置与隔离：ConfigMap 存非敏感配置，Secret 存敏感数据（base64 编码但非加密），Namespace 提供逻辑隔离。
- 🚪 Gateway API：标准化路由定义，替代厂商绑定的 Ingress，允许不改路由 Manifest 就切换控制器。
- 🧩 Operator 与 CRD：用 Operator 管理复杂应用，CRD 扩展 API；CloudNativePG 实现持久、可恢复的 Postgres 生态。
- 🧰 Kustomize：合并 YAML、组织 base 与 overlay，为多环境管理提供模板层而不改变 Kubernetes schema。
- ⚖️ 自动扩缩容与发布：HPA 根据 CPU/内存动态调整副本；Metric Server 收集指标；安全 rollout/rollback、PDB 和节点排水降低停机风险。
- 🛡️ RBAC 与安全：Role/RoleBinding 定义权限，ServiceAccount 为 Pod 提供身份，遵循最小权限；Sealed Secrets 可安全提交加密 Secret 到 Git。
- 🚀 GitOps 与 Argo CD：Argo CD 持续同步 Git 与集群，支持自动修剪、自愈，多应用/多集群可按目录组织。
- ☁️ Amazon EKS：创建托管集群，使用 EBS CSI、PVC、StorageClass、AWS ALB/Gateway 暴露服务，并用 Kustomize overlay 区分环境。
- 📊 可观测性与成本：优先使用平台原生监控；EKS 按小时计费，完成后必须删除所有云资源避免扣费。
- 🎓 结业：完成课程可获得完成证书，用于 LinkedIn 展示 Kubernetes 生产实践能力。

---

### [](https://www.jasnell.me/posts/a-node-bench-module)

**原文标题**: [node:bench | James M Snell](https://www.jasnell.me/posts/a-node-bench-module)

2026 年 8 月 28 日文章介绍：Node.js 已有内置测试运行器，但一直没有内置基准测试运行器；PR #65606 和 #65631 为此新增实验性 `node:bench` 模块，API 仿照 `node:test`，并配套 CLI、可编程事件流、可扩展 runner 与 `perf_hooks` 统计增强。

- 🧪 新增实验性 `node:bench` 模块，填补 Node.js 内置基准测试运行器的空白；API 设计参考 `node:test`，提供 `bench()` 和 `suite()`。
- 🖥️ 通过 `node --bench` 运行，支持显式文件或 glob 模式，会自动排序并按顺序执行。
- ⚙️ 默认 `--bench-isolation=process` 为每个文件启动新子进程并汇总结果；`--bench-isolation=none` 单进程运行更快，但模块与堆状态会跨文件共享，用户输出也会与 reporter 共用目标。
- 🏷️ CLI 标志还包括 `--bench-name-pattern`、`--bench-samples`、`--bench-warmup`、`--bench-reporter`、`--bench-reporter-destination`；内置 reporter 有 `spec` 和 `json`。
- 📡 可通过 `run()` 编程运行，返回 `BenchmarksStream` 对象模式 Readable，以 `{ type, data }` 事件发出生命周期记录：`bench:plan`、`bench:start`、`bench:sample`、`bench:complete`、`bench:diagnostic`、`bench:summary`。
- 🧩 自定义 reporter 可为任何 `stream.compose()` 接受的流，用于处理这些记录；`json` reporter 输出 NDJSON，将 `bigint` 编码为十进制字符串，并把错误精简为 `name`、`message`、`stack`、`code`、`cause`、`errors`。
- 🛠️ 为高层基准工具提供三个 API：`createRunner()` 创建隔离 runner，拥有自己的声明、钩子、过滤和输出，声明不会立即调度，且每个 runner 只运行一次；`runFile()` 在全新子进程中运行单个基准模块并返回流，加载失败或异常退出会产生错误诊断和 `success: false` 的终止摘要；`context.diagnostic()` 发出绑定当前基准、阶段和样本索引的 `info` 或 `warning` 记录。
- 📊 `perf_hooks` 新增 `Histogram.meanCI()`，使用 Student's t 和样本标准误返回均值的双侧置信区间，也是 `spec` reporter 95% CI 列的基础。
- 🧪 该分支已将部分核心基准移植到 `node:bench`，并添加 `benchmark/compare-node-bench.js` 和 `benchmark/scatter-node-bench.js` 作为概念验证。
- 🚧 该模块标记为 Stability 1.0（Early Development），CLI 标志仍属实验性。

---

### [](https://github.com/nodejs/node/pull/65606)

**原文标题**: [bench: add experimental `node:bench` module by jasnell · Pull Request #65606 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65606)

Node.js 核心仓库 PR #65606 引入实验性 `node:bench` 模块，由 James M Snell 发起，采用类似 `node:test` 的 `bench/suite` API 与 CLI，目标是提供轻量、无新运行时依赖的内置基准测试原语，而不是替代 `bench-node` 等全功能工具；该功能已合并并进入 Node.js 26.9.0。

- 🧪 PR #65606 新增实验性 `node:bench`，可通过 `import { bench, suite } from 'node:bench'` 编写基准测试，并用 `node --bench benchmark.mjs` 运行。
- 🏗️ 架构仿照 `node:test`，提供 suite、samples、params、start/end 计数、报告器和 CLI 隔离等最小内核。
- 🎯 定位为最小化基准原语，不是 `bench-node` 的替代品，旨在为更完整工具提供基础，且不引入新运行时依赖。
- 🔧 后续改进见 #65631；作者强调优先实现最小功能，核心已可用但仍需优化。
- 💬 社区讨论关注与 #50768、mitata 的差异，以及为何不 vendor `bench-node`；作者认为两者可互补，类似 `node:test` 与 vitest。
- 📊 Codecov 显示补丁覆盖率 98.99920%，项目覆盖率 90.14%，少量文件存在未覆盖行。
- ✅ 审查者 panva、ronag、H4ad、gurgunday 批准；mcollina 曾被请求审查，PR 最终关闭/合并。
- 🏷️ 标签包括 semver-minor、experimental、performance、large-pr、notable-change 等。
- 🚀 相关实现随 Node.js 26.9.0 (Current) 发布，包含 `node:bench`、reporters、CLI、`createRunner`、Histogram meanCI API 等。
- 🧪 测试更新包括提高 `node:bench` 覆盖率、修复时序、兼容 no-crypto 环境。

---

### [Node.js — Node.js 26.8.2（当前版本）](https://nodejs.org/en/blog/release/v26.8.2)

**原文标题**: [Node.js — Node.js 26.8.2 (Current)](https://nodejs.org/en/blog/release/v26.8.2)

Node.js 26.8.2（Current）于 2026-09-09 发布，由 Antoine du Hamel（@aduh95）负责发布。本次更新涵盖重要变更、依赖升级、文档、测试、工具链与类型定义改进，并提供多平台下载文件、SHA256 校验和及 PGP 签名；下一版本为 Node.js 24.21.0（LTS）。

- 🚀 **版本发布**：Node.js 26.8.2 为 Current 版本，发布日期为 2026-09-09。
- ⚠️ **重要弃用**：弃用 `node:net` 中的 `Server.prototype._listen2`（#65593）。
- 🔐 **安全态势**：改进实验性功能的安全漏洞处理策略（#65438）。
- 📦 **核心依赖更新**：Undici 更新至 8.10.2，OpenSSL 更新至 3.5.8（#65788、#65542）。
- 📦 **其他依赖升级**：npm 升至 11.19.1，corepack 升至 0.36.0，并更新 googletest、simdjson 4.6.9、perfetto 58.2、zlib 等。
- 🛠️ **构建改进**：涉及 riscv64 默认标志与 dockit 跳过、GN 构建中从 `target_cpu` 推导 `NODE_ARCH`、Windows 移除 LTO 并行限制等。
- 📚 **文档更新**：替换 `node:modules` 文档头、澄清 `fs.mkdtemp*` 返回类型、补充 `crypto.setEngine` 稳定性状态、修复链接与过时说明、重构 AI 指南等。
- 🧪 **测试稳定性**：大量 deflake、跳过 AIX/riscv64 平台特定测试、修复 WASI 线程握手、代理、权限 UDP、runner coverage 等相关测试。
- 🤖 **工具与元数据**：升级 CodeQL、checkout、setup-node、cachix、harden-runner 等 CI 依赖，改进贡献者自动化、首次贡献者欢迎、cron 偏移与 eslint 并发。
- 🧩 **类型定义**：新增或修复 `fs_event_wrap`、`stream_pipe`、`profiler`、`ffi`、`zlib` 等内部绑定类型。
- 💻 **下载与安装**：提供 Windows、macOS、Linux、AIX、ARMv8、源码包及文档链接，覆盖 x64、ARM64、ppc64le、s390x 等平台。
- 🔑 **校验与签名**：发布 SHASUMS SHA256 校验和及 PGP 签名。
- ⏭️ **下一版本**：Node.js 24.21.0（LTS）。

---

### [Node.js — Node.js 24.21.0 (LTS)](https://nodejs.org/en/blog/release/v24.21.0)

**原文标题**: [Node.js — Node.js 24.21.0 (LTS)](https://nodejs.org/en/blog/release/v24.21.0)

Node.js 24.21.0（代号 Krypton）是 LTS 长期支持版本，发布于 2026-09-08，由 @aduh95 发布。本次更新覆盖 crypto、依赖升级、性能优化、网络/HTTP、流、SQLite、QUIC、测试、文档与工具链等大量改进，并提供各平台安装包、源码及校验文件。

- 🚀 版本信息：Node.js 24.21.0 'Krypton'（LTS），发布日期 2026-09-08，发布者 @aduh95。
- 🔐 crypto 重点：根证书更新至 NSS 3.126；支持通过 STORE loaders 加载私钥（SEMVER-MINOR）；并修复 ASN1、FIPS 模式等相关问题。
- 📦 依赖升级：OpenSSL 3.5.8、Undici 7.29.1、Corepack 0.36.0、zlib、simdjson、googletest、libuv、ICU 等均有更新。
- ⚡ 性能与 API：改进 histogram 实现；perf_hooks histogram 增加统计假设检验；提升 net.BlockList 性能；util 新增不抛错的 MIMEType.parse（均为 SEMVER-MINOR）。
- 🌐 网络与协议：修复 dgram bind 错误处理、DNS setServers 校验与崩溃、HTTP 性能与 keylog/drain 问题、HTTP/2 UAF，以及多项 QUIC/HTTP3 行为。
- 🧵 流处理：优化 Web Streams/Transform 背压、取消、BYOB、TextEncoderStream 编码、缓冲复用与 promise 开销。
- 🗄️ SQLite：修复 session.close 重入、prepare/SQLTagStore 无语句 SQL、Boolean/ArrayBuffer 绑定、backup 速率与 maxSize 校验等。
- 🛠️ 文件与模块：fs 修复 glob、realpath、mkdtemp 越界写入、cp 符号链接等；module 改进 package.json 读取/缓存与 --check。
- 🧪 测试与工具：test_runner 支持 dot reporter 覆盖率、JUnit classname 层级、条件导出 mock 等；大量测试去 flaky 和补充覆盖率。
- 📝 文档与元信息：大量文档修复/补充，涉及 SQLite、QUIC、WebCrypto、http2 常量、AI 指南、安全发布流程等。
- 🖥️ 下载渠道：提供 Windows、macOS、Linux、AIX、ARMv8 等平台安装包或二进制，以及源码 tar.gz。
- 🔑 校验信息：提供 SHASUMS 与 PGP 签名，覆盖各平台发布文件哈希。
- 📚 文档入口：Node.js v24.21.0 API 文档已同步发布。

---

### [](https://github.com/nodejs/undici/releases/tag/v8.10.2)

**原文标题**: [Release v8.10.2 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v8.10.2)

Undici v8.10.2 已发布，这是一次以安全修复为主的版本更新，修复多项高危、中危和低危漏洞，并包含依赖升级、测试、类型与 CI 改进。

- 🔐 v8.10.2 最新发布，重点修复缓存、去重、BalancedPool、WebSocket、解压、重试等安全与稳定性问题。
- 🚨 高危：缓存和去重拦截器曾可能使用调用方控制的请求元数据而非 dispatcher origin，导致跨源缓存污染与数据泄露；现基于 dispatcher origin 生成身份。
- 🔑 高危：BalancedPool 克隆配置时可能丢失函数型连接选项，包括自定义 TLS 证书验证回调；现保留 connect 与旧版 tls 选项。
- 🧷 高危：WebSocket 服务端在未请求子协议时选择子协议会触发未捕获 TypeError 并可能终止进程；现以 1002 协议错误拒绝握手。
- 💥 中危：畸形 permessage-deflate 载荷超过解压限制会触发未处理 zlib 错误；现达到限制后销毁 inflater。
- 🧯 中危：WebSocketStream 非正常关闭且可写流被锁定时可能产生未观察的 rejected promise；现通过保留的可写流控制器传播失败。
- 🍪 中危：共享缓存曾可能存储并重放含 Set-Cookie 的响应，泄露用户 Cookie；现将其排除在共享缓存之外，包括已有条目和重验证路径。
- 📦 中危：解压拦截器未限制解码输出，压缩响应可消耗过多内存；现每阶段默认限制 64 MiB，并支持 maxSize 配置。
- ⏳ 中危：重试最终失败且响应头已暴露时可能遗留原响应体，导致消费者无限挂起；现将最终错误传播到已暴露的响应体。
- 🚫 低危：缓存拦截器曾可存储或重放 POST、DELETE 等不安全方法响应；现仅对安全方法进行缓存读写，同时保留不安全请求成功后的失效机制。
- 🧱 低危：dump 拦截器在无 Content-Length 时可能将超大分块响应误判为已截断；现按接收字节执行 maxSize 并中止超大响应。
- ✂️ 低危：重试拦截器可能把帧格式不一致的续传响应拼接进下游输出，造成响应拆分或损坏；现续传前校验 Content-Range 与原始响应帧。
- 🛠️ 其他修复包括：避免 Set-Cookie 属性解析器无界递归、支持 SOCKS5 连接超时、重连时校验 Last-Event-ID、避免重复释放、304 新增 Vary 字段时重新获取。
- 🔌 还修复代理授权头保护、h2 扩展 CONNECT 非 200 响应关闭 WebSocket、重试 rawHeaders 转发、fetch 仅向可信 URL 发送 Sec-Fetch-Mode 等。
- 📚 类型与工程更新：在 MockAgent 命名空间暴露 PendingInterceptor 和 PendingInterceptorsFormatter；升级 undici、jest、CodeQL、@humanfs/node 等依赖与 CI 配置。
- 🎉 新增贡献者 @darkdi、@kjsik11、@official-burak；完整变更见 v8.10.1...v8.10.2。

---

### [广泛使用的 Node.js 沙箱库 vm2 中存在严重的远程代码执行漏洞](https://about.gitlab.com/blog/critical-remote-code-execution-in-vm2/)

**原文标题**: [Critical remote code execution in vm2, a widely used Node.js sandbox library](https://about.gitlab.com/blog/critical-remote-code-execution-in-vm2/)

GitLab 是覆盖软件生命周期的一体化平台，旨在兼顾速度与控制，帮助团队更高效地交付软件。
- 🚀 提供贯穿软件生命周期的一体化平台
- ⚡ 兼顾速度与控制，提升软件交付效率
- 🛡️ 在快速推进的同时保持必要管控
- 🔗 可进一步了解更多信息

---

### [](https://github.com/patriksimek/vm2#the-fundamental-challenge)

**原文标题**: [GitHub - patriksimek/vm2: Advanced vm/sandbox for Node.js · GitHub](https://github.com/patriksimek/vm2#the-fundamental-challenge)

vm2 是一个在 Node.js 进程内运行不可信 JavaScript 的沙箱库，通过内置 VM 模块与 Proxy 拦截来隔离代码，并可控制模块加载；但官方强调它并非绝对安全，绕过漏洞可能持续出现，必须及时更新并叠加其他防护，完全不可信代码应改用进程/容器级隔离。仓库采用 MIT 许可，约 4.1k stars、328 forks。

- 🧩 项目定位：vm2 是 Node.js 的沙箱，可在同一进程内运行不可信代码，并按白名单限制内置模块访问。
- 🔒 安全免责声明：它只是安全边界之一，不能作为唯一防线；新绕过可能被发现，需订阅安全通告并保持更新。
- 🛡️ 更强隔离替代：isolated-vm、child_process/Worker、Docker/gVisor/Firecracker、云托管执行等，提供进程级或硬件级隔离。
- ✅ 适用场景：需要与宿主机对象紧密集成、代码来源相对可信、并结合网络/文件系统/资源限制等纵深防御。
- 🖥️ 运行时支持：Node.js 受支持且沙箱是安全边界；Bun 为实验性，兼容性不完整，明确不是安全边界。
- ✨ 主要功能：单进程安全运行、控制 console、限制 process 访问、按需 require 模块、限制内置模块、跨沙箱调用与回调、转译器支持。
- ⚙️ 工作原理：使用内部 VM 模块创建安全上下文，用 Proxy 防止逃逸，并重写 require 控制模块访问。
- 🆚 与 node:vm 差异：Node 原生 vm 可被 `this.constructor.constructor("return process")().exit()` 等方式逃逸，vm2 会阻止此类访问。
- 🧪 VM 类：同步运行无 require 的代码，仅提供 JS 内置对象和 Buffer；支持 timeout、sandbox、compiler、eval、wasm、allowAsync、bufferAllocLimit 等选项。
- 🧱 NodeVM 类：允许像普通 Node 一样 require 模块；可配置 console、sandbox、require.external、require.builtin、require.root、require.mock、nesting、wrapper、argv、env 等。
- 🧩 Resolver：可通过 makeResolverFromLegacyOptions 创建，并被多个 NodeVM 共享，以复用已编译模块代码、加快加载。
- 📜 VMScript：支持预编译脚本，可多次运行；首次运行自动编译，也可手动调用 `script.compile()`。
- 🧾 编译器：支持 javascript、typescript、coffeescript 或自定义函数；内置 TypeScript 编译器要求 typescript@6 或更早，TS7 需自行传入转译器。
- 🚨 错误处理：编译和同步执行错误可用 try-catch；异步错误可通过 process 的 `uncaughtException` 事件处理。
- 🐞 调试：可像普通进程一样调试沙箱代码，支持断点、`debugger` 关键字和单步进入。
- ❄️ 只读/保护对象：实验性 freeze 可深度冻结对象；protect 允许修改属性但禁止附加函数；已代理到 VM 的对象无法再冻结/保护。
- 🔗 跨沙箱关系：对象、函数、Buffer 在跨沙箱时保持 instanceof 与 prototype 关系。
- 💻 CLI：全局安装后可直接用 `vm2 ./script.js` 运行脚本。
- 🧰 加固建议：设置 bufferAllocLimit、安装 unhandledRejection 处理器、使用进程内存上限、避免 `require.builtin: ['*']`、不要把 `nesting: true` 用于不可信代码。
- ⚠️ 已知问题：不能继承被代理类、直接 eval 不可用、日志打印数组可能重复、源代码转换可能改变函数源字符串、沙箱仍可能崩溃 Node 进程，且 TS7 兼容有问题。
- 📄 许可：MIT 许可。

---

### [](https://github.com/nodejs/node/pull/65796)

**原文标题**: [src: seed V8 from the OS CSPRNG instead of OpenSSL's DRBG by colinhacks · Pull Request #65796 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65796)

该 PR #65796 已合并到 nodejs/node:main，核心是让 V8 的熵源不再在启动时经过 OpenSSL 的 DRBG，而是通过 `uv_random()` 读取操作系统 CSPRNG（AIX 除外），从而减少启动开销并推迟 OpenSSL DRBG/default provider 表的构造。

- 🚀 状态：由 colinhacks 提交，panva、jasnell 批准，2026-09-10 合并为 `43d3fe9`，92/94 检查通过。
- 🔥 动机：启动时 `CSPRNG(nullptr, 0)` 会提前运行 `RAND_status()`，实例化 DRBG 并构建默认 provider 的算法/名称表，约占 `node -e 0` 样本的 3.7%，且都发生在 `v8Start` 之前。
- ⚙️ 改动：V8 熵改用 `uv_random()` 读取 OS CSPRNG；V8 熵用于哈希种子、地址空间随机化和 `Math.random()`，均非加密用途；所有加密消费者仍走 OpenSSL。
- 🧱 AIX 例外：AIX 上 `uv_random()` 会读取阻塞的 `/dev/random`，因此保留 OpenSSL DRBG 作为 V8 熵源；OpenSSL 先从 `/dev/urandom` 播种。
- 🔐 Provider 逻辑：仍会在启动时激活 default provider，因为 `--openssl-legacy-provider` 依赖它；只有 default provider 不可用或 FIPS 启用时才执行种子检查。
- 🧪 行为变化：配置了无法获取的 DRBG（如 `random=NO-SUCH-DRBG`）不再启动中止，而是首次加密调用失败；`--secure-heap` 下 Worker 不再因 V8 熵回调中止，而返回 `ERR_OSSL_CRYPTO_SECURE_MALLOC_FAILURE`。
- 📉 性能：Linux x64 上 `node -e 0` 从 29.18 ms 降至 27.82 ms，`nodeStart→v8Start` 从 2.91 ms 降至 2.11 ms；macOS arm64 从 2.63 ms 降至 2.13 ms；首次 `crypto.randomBytes()` 初始化 DRBG 约 0.19 ms。
- ✅ 测试与披露：`parallel`/`sequential`/`message`/`es-module`/`addons` 套件无新增失败；AIX 测试加 `common.isAIX` 门控并重写 Worker 测试；作者按 AI 使用政策披露该变更由 AI coding agent 协助完成。

---

### [](https://github.com/nodejs/TSC/issues/1883)

**原文标题**: [Elections · Issue #1883 · nodejs/TSC · GitHub](https://github.com/nodejs/TSC/issues/1883)

nodejs/TSC 的 #1883 议题讨论 TSC 选举安排，作者因错过原定 5 月选举而致歉，并提出今年选举与交接的拟议时间表；议题已关闭，标签为 tsc-agenda。
- 🧑💻 议题由 mcollina 于 2026 年 7 月 31 日创建，状态为已关闭。
- 🙏 作者说明：TSC 选举通常在 5 月进行，但去年 7 月从 Micheal 接手后忘记推进，因此道歉。
- 🗳️ 去年选出了主席和副主席，今年预计继续选举这两个职位。
- 📅 拟议日程：8 月 1 日征集提名，8 月 7 日开始投票，8 月 31 日公布结果，9 月 1 日至 11 日交接。
- 🏷️ 标签为 tsc-agenda；未分配负责人，无类型、项目、里程碑或关联分支/PR。
- 📊 仓库页面显示 Fork 141、Star 693、Issues 31、Pull requests 8。

---

### [](https://blog.gaborkoos.com/posts/2026-09-05-Fuzzing-the-State-Machines-Inside-My-HTTP-Client/)

**原文标题**: [Fuzzing the State Machines Inside My HTTP Client](https://blog.gaborkoos.com/posts/2026-09-05-Fuzzing-the-State-Machines-Inside-My-HTTP-Client/)

ffetch 作者在对自家 HTTP 客户端做属性测试（fuzzing）时，本只想验证一个关于 hedge 插件的怀疑，结果一周内额外发现 10 个完全没预料到的缺陷。原有的 206 个基于示例的测试全部通过，却漏掉了大量"时间线顺序"层面的漏洞——因为写测试的人和写代码的人是同一个人，盲区也一致。最终 55 条属性、27,450 个生成用例共找出 11 个缺陷，测试套件仍能在 9 秒内跑完。

- 🧪 **起点**：ffetch 已有 19 个文件、206 个测试块，覆盖重试、超时、对冲、取消、熔断、舱壁、去重及插件组合，全部通过——但这恰恰值得怀疑。
- ⚡ **hedge 竞态**：对冲插件在"后启动的尝试"返回 429 时，会误以为它是最后机会并立刻采用，同时中止仍在飞行、2ms 后就要返回 200 的原始请求；生成器在第 4 个用例就命中它。
- 🔬 **最小化到 3ms**：`original: 200 @3ms` / `hedge: 429 @1ms`，插件返回 429 并掐掉了即将到来的成功；根因是用"尝试的启动位置"推断"是否还有更好的结果在路上"。
- 🔁 **示例测试的局限**：每个测试只证明"我能想到的那条路径"，覆盖感来自用例数量而非空间形状；漏洞存在于用例之间的排序里。
- 🎲 **属性测试取代两半**：不再挑选输入/写出期望，而是用 arbitrary 描述"任意合法输入"，用规则描述"任何输入下都必须成立"的关系；由生成器负责搜索。
- 🔒 **两大机制**：可复现性（失败时报告种子）与 shrinking（自动收缩到最小反例，如把 17ms/503/4ms/200 缩到 1ms/429/3ms/200）。
- ⏱️ **假定时器 + fast-check**：在既有 Vitest 内运行，无独立 runner 和 CI 任务；虚拟时间让上千用例从 20 秒降到 1 秒以内。
- 🐛 **取消却返回响应**：在后退期间 abort/timeout，客户端却把已保存的 503 当作正常响应返回，而非拒绝 `AbortError`/`TimeoutError`；根因是保存响应兜底的优先级高于终态判定。
- 🪤 **因错误原因通过的测试**：`abortAll()` 测试名为"中止所有请求"，但实际是靠 1 秒客户端超时自然拒绝才通过；内部 controller 的信号从未并入传给 fetch 的信号。
- 💧 **被丢弃的 Promise**：异步 `onRetry` 钩子的 reject 逃逸到进程层，成为未处理的拒绝，任何关于请求/钩子/清理的断言都看不见它。
- 🧩 **组件接缝才是灾区**：重试与 hedge 组合产生 3 个缺陷——第二个 hedge 无法克隆已被消费的 body、`onComplete` 每个投机分支各触发一次、落败分支的清理伪装成应用级 abort 上报。
- 🛡️ **熔断器零缺陷**：6 条属性、2,200 个用例未发现问题，价值在于把既有行为固化为"可执行的文档"。
- 🚦 **舱壁队列超时失效**：排队请求的 1ms deadline 触发后仍留在队列里，直到前面的请求完成才被拒绝；根因是监听了 caller 的 signal 而非包含总体超时与 `abortAll()` 的组合 signal。
- 🔑 **去重两处缺陷**：body 身份只读 `init.body`，导致完整 `Request` 对象都被当成无 body，`""` 与 `" "` 被错误合并；等待者的取消信号也从未被监听。
- 📏 **把服务器值当不变量**：`Content-Length: garbage` 变成 `NaN`，声明 1 字节却传 2 字节时百分比变成 2；解析需限定为非负十进制安全整数，百分比需 clamp。
- 📊 **总账**：55 条属性、27,450 个生成用例、11 个缺陷；测试从 19 文件/206 块增至 27 文件/274 测试，随 `@fetchkit/ffetch` 5.6.0 发布。
- 🧠 **共同模式**：把"位置"当成"证据"、取消在层边界停止、内部机制对外可见、服务器值被当成不变量、测试因无关原因通过、Promise 创建后无人等待。
- ⚠️ **不能证明什么**：27,450 次抽样仍继承了我对"网络结果"的假设；假定时器牺牲真实传输行为；这是有界属性测试，而非持续 fuzzing 与语料积累。
- 💡 **实践建议**：选"对顺序做出反应"的组件；陈述你已相信的规则而非你已担心的反例；用假定时器；先读收缩后的反例；同时保留属性与最小用例；当失败暴露的是设计问题而非错误时，让文档来裁决。
- 🏁 **最终收获**：最初的怀疑被证实只是最没价值的部分，真正的收益是那 10 个毫无预期、藏在"已完成"组件里、甚至被同名测试守护着的缺陷。

---

### [](https://github.com/dubzzz/fast-check)

**原文标题**: [GitHub - dubzzz/fast-check: Property based testing framework for JavaScript (like QuickCheck) written in TypeScript · GitHub](https://github.com/dubzzz/fast-check)

overview summary
fast-check 是由 dubzzz 创建并用 TypeScript 编写的 JavaScript/TypeScript 基于属性测试框架，类似 QuickCheck。它通过随机生成输入来验证代码属性，并在失败时自动收缩到最小反例，适合单元测试、模糊测试、模型测试与竞态检测。

- 🧪 核心定位：用于 JavaScript/TypeScript 的属性测试框架，验证“对所有满足前置条件的输入，断言都应成立”。
- 📦 安装方式：支持 pnpm、yarn、npm，例如 `pnpm add -D fast-check`。
- 🔌 测试集成：可配合 AVA、Jasmine、Jest、Mocha、Tape 等测试框架使用，并附有 Mocha 示例。
- 🐞 失败诊断：属性失败时会报告种子、路径、收缩次数等信息，帮助快速定位实现问题。
- 🧠 核心优势：强类型、TypeScript 友好，提供 `map`、`chain`、`fc.pre(...)`、`fc.gen()` 等扩展能力。
- 🧩 智能生成与收缩：默认偏向同时生成小值和大值，支持 `fc.oneof` 收缩，更易找到反例。
- 🛠️ 调试能力：支持 verbose 模式、最小反例重放、自定义样例、`fc.context` 日志记录。
- 🏗️ 高级测试：支持模型测试，可用于测试 UI、API、状态机，并检测异步代码中的竞态条件。
- ✅ 广泛信任：被 Jest、Jasmine、fp-ts、io-ts、Ramda、js-yaml、query-string 等项目使用，并帮助发现过开源项目 bug。
- 📊 仓库数据：约 5.1k stars、212 forks、58 issues、14 PR、6,814 commits，采用 MIT 许可证。
- 🧾 兼容性：4.x 需要 Node ≥12.17.0、ES2020、TypeScript ≥5.0；旧版本支持更低环境。
- 🤝 社区贡献：拥有大量贡献者，遵循 all-contributors 规范，欢迎各种形式的贡献。
- 💸 赞助支持：可通过 GitHub Sponsors 或 OpenCollective 赞助项目。
- 📚 文档资源：提供入门教程、内置/自定义 arbitraries、属性运行器、API 参考和示例。

---

### [错误](https://github.com/fetch-kit/ffetch)

**原文标题**: [Error](https://github.com/fetch-kit/ffetch)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /fetch-kit/ffetch (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [](https://sentry.io/cookbook/monitor-mcp-server/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=mcp-fy27q3-cookbook&utm_content=newsletter-sponsored-link-sentry-mcp-trysentry)

**原文标题**: [Monitor Your MCP Server with Sentry: Tools & Errors | Sentry](https://sentry.io/cookbook/monitor-mcp-server/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=mcp-fy27q3-cookbook&utm_content=newsletter-sponsored-link-sentry-mcp-trysentry)

用 Sentry 监控 MCP 服务器：只需一次包装调用，即可完整查看客户端活动、传输分布、工具/资源/提示性能以及错误（包括 MCP 静默吞掉的错误）；适合初学者，约 10–15 分钟完成。

- 📊 监控目标：客户端活动、传输分布、工具与资源性能、错误（含静默错误）。
- 🧩 功能与适用：AI 可观测性、Tracing、错误监控、Issues；支持 Node.js 与 Python；共 8 个步骤。
- 📦 前置条件：Sentry 账号与项目、可部署 MCP 服务器；JS 用 `@sentry/node` v9.46.0+ 和 `@modelcontextprotocol/sdk`；Python 用 `sentry-sdk` v2.43.0+ 和 `mcp`；了解 MCP tools/resources/prompts。
- ⚙️ JS 接入：先 `Sentry.init()`，再用 `Sentry.wrapMcpServerWithSentry()` 包装 `McpServer`；设置 `recordInputs`/`recordOutputs` 可捕获工具参数与结果。
- 🐍 Python 接入：在 `sentry_sdk.init()` 中加入 `MCPIntegration()`，并设 `send_default_pii=True`；支持 FastMCP 与 low-level Server API。
- 🚀 部署验证：触发工具调用或资源读取后，在 Sentry MCP Dashboard 几秒内看到数据。
- 👥 客户端/传输：Traffic by Client 显示 Cursor、Claude Desktop 等来源；Transport Distribution 显示 Streamable HTTP、SSE、stdio 或自定义传输。
- 🧰 工具性能：Tools 标签提供最常用、最慢、最失败工具，以及请求数、错误率、平均耗时、P95 延迟。
- 📚 资源/提示：Resources 按 URI 展示访问量、错误率与延迟；Prompts 跟踪模板使用、响应时间和错误率。
- 🔍 调用追踪：单次 trace 展示 JSON-RPC 全生命周期、工具名、耗时、输入输出，以及客户端、传输、请求 ID、会话 ID 等。
- 🕵️ 静默错误：MCP SDK 常以 JSON-RPC 响应而非抛错返回失败；Sentry 仍会捕获并关联到具体工具/资源/提示，在 Issues 中显示堆栈与上下文。
- ⚠️ 关键坑：未启用 `sendDefaultPii` 或 `recordInputs`/`recordOutputs` 时看不到输入输出；`Sentry.init()` 必须先于创建 MCP server；`tracesSampleRate`/`traces_sample_rate` 必须 > 0；注意 SDK 版本。
- 💡 实践建议：开发时开启输入输出，生产敏感数据可关闭；用 session ID 分组请求；兼容 OpenTelemetry；定期检查传输来源防未授权。
- 💰 成本：工具调用、资源读取、提示检索作为 span 计入 Sentry tracing 配额；MCP 错误计入错误配额。
- ➡️ 下一步：可接入 Sentry MCP server、探索 AI Observability、配置错误率或延迟告警。

---

### [Prisma 8 是否已准备好用于长期运行的生产应用？](https://www.prisma.io/blog/is-prisma-8-ready-for-long-lived-production-apps)

**原文标题**: [Is Prisma 8 Ready for Long-Lived Production Apps?](https://www.prisma.io/blog/is-prisma-8-ready-for-long-lived-production-apps)

Will Madden 回应 Reddit 对 Prisma 8 的三大担忧：架构变化、商业激励、迁移模型。他强调 Prisma 8 是首个面向代理时代的 ORM，采用可扩展、可替换组件架构；ORM 将继续 Apache-2.0 且独立于商业产品；新迁移系统以透明 SQL、可编辑 TypeScript 和图结构迁移为核心，适合多分支与代理协作。他建议长期项目可考虑 Prisma 8，但迁移应增量进行。

- 🧩 Prisma 8 是全新架构，目标是首个“agent-native ORM”，为开发者与代理协作开发而设计。
- 🏗️ 它从 Prisma 7 单体 Rust 引擎改为可扩展框架：默认不内置数据库，Postgres、MongoDB、IndexedDB、查询构建器、ORM 客户端、契约格式等都可替换。
- 🔓 开源承诺不变：ORM 保持 Apache-2.0，不会闭源，不会为付费产品削弱功能；核心不包含 Prisma Cloud 逻辑，托管工具可选。
- ⚖️ 商业激励会偏向 Prisma Postgres/Compute，但社区可自行添加数据库支持、中间件、校验集成或契约格式，不再受核心团队瓶颈限制。
- 🧾 迁移系统以透明为原则：每个迁移目录有 ops.json，Postgres 操作就是实际 SQL，可用 migration show 单独查看。
- ✍️ migration.ts 让自定义迁移更安全简单，可扩展操作词汇；JSON 中的 pre/post checks 使操作幂等，契约哈希用于按图导航迁移。
- 🌿 迁移是操作列表而非黑盒 SQL，因此 squash/split 可机械转换；图结构可减少多分支乱序冲突，应对代理并行开发带来的冲突放大。
- 🧱 作者称不会再有类似重写：没有剩余单体可替换，未来大版本会改 API，但不会改范式。
- ⏳ Prisma 8 现为 RC，正式 8.0.0 预计 4–8 周；RC 可能有破坏性变更，但会附带升级配方且越来越少。
- ☁️ Prisma 云平台 API 已运行 Prisma 8；Prisma 7 用户可增量迁移，新旧版本可并行连接同一数据库，逐条切换验证。
- 🛡️ Prisma 7 将继续获得 12 个月缺陷修复和安全更新，担心风险者可以等待。
- 💬 有更多问题可在 Prisma 公共社区 Discord 提问。

---

### [使用 Paketo Buildpacks 容器化并优化 Node.js 应用程序 | Paketo Buildpacks | 博客](https://blog.paketo.io/posts/containerizing-nodejs-apps/)

**原文标题**: [Containerizing and Optimizing Node.js Applications with Paketo Buildpacks | Paketo Buildpacks | Blog](https://blog.paketo.io/posts/containerizing-nodejs-apps/)

本文介绍如何使用 Paketo Buildpacks 在 Ubuntu Noble、Jammy、Resolute 以及 Red Hat UBI 8/9/10 builders 上容器化并优化 Node.js 应用，重点包括使用 tiny run image 缩小镜像、用 tini 支持无 shell 启动，以及为原生模块构建启用 Python。

- 🛠️ 先决条件：安装 Pack CLI、Podman 或 Docker、git，并准备 Node.js 应用；可克隆 `https://github.com/paketo-buildpacks/samples` 获取示例。
- 📦 使用 Ubuntu Noble builder 构建：运行 `pack build noble-nodejs-container-image --path samples/nodejs/npm --builder paketobuildpacks/ubuntu-noble-builder`，再用 Docker/Podman 运行并访问 `http://localhost:8080` 验证。
- 🪶 优化镜像体积：通过 `--run-image paketobuildpacks/ubuntu-noble-run-tiny` 改用 tiny run image，示例镜像从 396MB 降至 304MB，减少约 92MB。
- 🐚 tiny 镜像没有 shell，直接运行会报 `exec: "sh": executable file not found`；需将 `scripts.start` 简化为 `node server.js`，并设置 `BP_LAUNCH_WITH_TINI=true` 使用 tini 启动。
- 🧱 Jammy builders 也适用相同模式：可用 base builder 搭配 tiny run image；但 `builder-jammy-tiny` 不包含 Node.js buildpacks，会检测失败。
- 📉 Jammy 示例中，full builder 配 full run 为 996MB，配 tiny run 为 304MB；base builder 配 base run 为 390MB，配 tiny run 为 304MB，两个 tiny-run 输出镜像相同。
- 🐍 构建含原生模块的 npm 包需要 Python：Jammy base 缺少 Python 会失败，full builder 可成功；Noble 及以后弃用 full builder，应设置 `BP_NPM_INCLUDE_BUILD_PYTHON=true` 在构建时提供 Python，Jammy base 也适用。
- 🧭 Ubuntu Resolute builders 同样支持该流程：使用 `paketobuildpacks/ubuntu-resolute-builder` 和 `ubuntu-resolute-run-tiny`，并按需设置 `BP_LAUNCH_WITH_TINI=true` 与 `BP_NPM_INCLUDE_BUILD_PYTHON=true`。
- 🧢 UBI builders 无需 `--run-image` 或 tini 设置：它们通过 extension 自动选择最终 run image，构建镜像默认提供 Python；可用 UBI 8、UBI 9、UBI 10 builder 构建。
- ⚠️ UBI 上 `--run-image` 不生效，可用 `BP_UBI_RUN_IMAGE_OVERRIDE` 强制覆盖，但仅用于测试，不应生产使用；例如 UBI 8 构建、UBI 10 运行可能不稳定。
- 🎯 结论：文章覆盖跨 Ubuntu 与 UBI 构建 Node.js 应用、用 tiny run image 优化体积、用 tini 管理进程、用 Python 支持原生模块，以及 UBI 自动处理 run image 选择。
- 🤝 想参与 Paketo CNCF buildpacks 贡献，可查看社区 get involved 指南或相关贡献博客。

---

### [](https://blog.gaborkoos.com/posts/2026-09-08-Half-Past-Fetch/)

**原文标题**: [Half Past Fetch](https://blog.gaborkoos.com/posts/2026-09-08-Half-Past-Fetch/)

`await fetch(url)` 只表示响应头已到达，响应体仍在连接中传输；真正的请求完成取决于之后如何读取 body。这个“头部已解析、主体未到达”的间隙，决定了连接复用、内存、clone、abort 和超时等行为。

- ⏳ `await fetch()` 解析的是响应头：promise settle 时拿到 `Response`，但 `body` 是仍在被网络层写入的 `ReadableStream`。
- 📥 通常需要二次 await：`await response.json()`、`arrayBuffer()` 或 `text()` 才等待主体结束。
- 🧾 规范中 `HTTP-network fetch` 等到最终状态行和最后一个头部字节，随后创建 body stream；`processResponse` 让 fetch promise 解析，此时 body 仍可能在入队。
- 🚫 `HEAD` 与 null body 状态（101、103、204、205、304）例外：`response.body` 为 null，没有仍在到达的主体。
- 🔌 未读取 body 会占用连接：HTTP/1.1 需读完响应才能复用连接；小响应可能已被缓冲，大响应会触发新连接。Node 约 16KB 以上差异明显，Chrome 阈值更高。
- 📉 `response.body.cancel()` 不会还回连接；只有把 body 读到末尾才会释放连接。大 body 因 backpressure 停止拉取，等待消费者出现。
- 🧬 `clone()` 不是复制内存，而是对尚未结束的 body stream 做 tee；两个分支共享同一源头。
- 🧠 只读一个 clone 分支会让另一分支的数据在内存中累积；60MB 响应下，放弃分支可多占约 55MB。
- ⚠️ 必须在使用 body 前 `clone()`；读取后再 clone 会报 `Body has already been consumed`，`bodyUsed` 按对象记录。
- 🧹 `copy.body.cancel()` 可释放保留数据，但若先 await 它、再读另一分支会死锁；cancel promise 通常要等另一分支读完才 settle。
- 🛑 promise resolve 后 `AbortSignal` 仍连接着 body：abort 会使下一次 body 读取 reject；已收到的 chunk、状态和头部仍可用；body 读完后 abort 不再生效。
- ⏱️ 用 `Promise.race` 包 fetch 的超时只覆盖 headers 阶段；`AbortSignal.timeout` 传入 fetch 后持续到 body 结束，因此能中断慢 body。
- 🧪 浏览器后台 tab 会 clamp `setTimeout`，测试超时时需保持前台；多个取消原因可用 `AbortSignal.any` 组合。
- 📊 因为 body 是流，可在读取前 `pipeThrough(TransformStream)` 统计进度、包装成新 `Response`，实现下载进度或插件拦截。
- 🎯 结论：`await fetch()` 是“头部完成、主体开始”的分界点；之后仍属于请求生命周期，连接、内存、取消和超时都由后续 body 读取方式决定。

---

### [](https://rslib.rs/blog/v1-0)

**原文标题**: [Announcing Rslib 1.0 - Rslib](https://rslib.rs/blog/v1-0)

Rslib 1.0 正式发布：一个基于 Rsbuild 的 JavaScript 库开发工具，面向工具库、UI 组件库、CLI 与 Agent 应用，提供多格式输出、灵活构建模式、快速声明生成、多框架支持和完整开发工作流；0.x 到 1.0 历经 16 个次版本，性能显著提升，公共 API 已稳定并遵循 SemVer。

- 🚀 Rslib 1.0 于 2026 年 9 月 3 日发布，目标是简单直接地构建不同类型 JS 库。
- 🧱 基于 Rsbuild、Rspack 和 webpack 生态，可复用插件、loader 与配置，减少重复维护。
- 🔗 支持构建 Module Federation 输出，让库作为远程模块被多个应用运行时加载。
- 🛠️ 提供统一库构建管线，一次构建完成 JS 编译、框架语法转换、声明生成和静态资源处理。
- ⚡ 相比 0.7.0，在 1 万个 React 组件基准中，无缓存构建时间降低约 24.3%，缓存构建降低约 56.7%，未压缩产物体积降低约 32.2%。
- 🏷️ 声明生成更快，支持 TypeScript 7 和 Isolated Declarations；示例中分别约提升 2.4 倍和 4.2 倍。
- 🧩 组件库支持增强，覆盖 React、Vue、Svelte、Solid，并改进样式、资源、`new URL()`、Web Worker 与 Wasm 处理。
- 🧰 使用更灵活，简单项目可零配置或 CLI 构建，复杂项目可用配置文件与 JavaScript API。
- 🤝 开发体验更顺滑，可与 Rstest、Rspress、Rsdoctor 配合，并通过 Agent Skills 服务编码智能体。
- 🔀 输出格式覆盖 ESM、CJS、UMD、IIFE 和 Module Federation，并可在一个配置中定义多种输出。
- 🧭 ESM 输出经过优化，更利于静态分析、代码分割和下游 tree shaking。
- 📦 提供实验性可执行文件生成能力，基于 Node.js SEA，适合分发 CLI 等 Node.js 程序。
- 🧱 支持 bundle 与 bundleless 两种构建模式，可分别适应 SDK/CLI 或组件库/monorepo 内部包。
- 📝 通过 `dts` 配置在构建 JS 时生成声明文件，bundleless 模式下会处理路径别名与导入扩展名。
- ⚛️ 多框架开箱即用，通过 Rsbuild 插件集成 React、Vue、Svelte、Solid 编译器，并可启用 React Compiler。
- 🎨 样式与资源支持全面，包括 CSS Modules、PostCSS、样式提取/内联/压缩、Sass/Less/Stylus/Tailwind CSS、JSON 模块、图片字体等静态资源。
- 🖥️ 支持 Web Worker、Wasm ESM Integration、Source Phase Imports，并可保留 Wasm 导入给下游处理。
- ⚙️ 配置结构简化：单默认 ESM 输出可省略 `lib`，多输出使用 `lib` 数组，顶层共享配置可被单项覆盖。
- 🧪 集成测试、文档和发布检查：Rstest、Rspress、publint、Are The Types Wrong、Rsdoctor 等。
- 🤖 提供 Agent Skills，包括 `rslib-best-practices`、`rslib-modern-package`、`migrate-to-rslib`，并支持 `llms.txt` 与 `AGENTS.md`。
- 🚀 新用户可通过 StackBlitz 或 Quick start 上手；0.x 用户需注意破坏性变更并参考迁移指南。
- 🔭 后续将继续优化 ESM/CJS 输出、Node.js 打包、模块结构保留、声明生成，并强化测试、文档、质量检查与发布流程。
- 🙏 项目借鉴了 esbuild、mini-css-extract-plugin、tsdown、tsup、webpack 等开源项目，并感谢社区贡献。

---

### [从 0.x 升级到 v1 - Rslib](https://rslib.rs/guide/upgrade/v0-to-v1#default-syntax-target-update)

**原文标题**: [Upgrading from 0.x to v1 - Rslib](https://rslib.rs/guide/upgrade/v0-to-v1#default-syntax-target-update)

Rslib 0.23 到 1.0 的迁移指南涵盖多项破坏性变更，包括依赖升级、默认语法与外部模块行为、环境变量、资源模块、TypeScript 声明、Node.js 模板和配置 API；建议按指南或 Agent 提示逐步升级。

- 🚀 升级 `@rslib/core` 到 `^1.0.0`；v1 基于 Rsbuild v2，建议用 Taze 升级相关 Rsbuild 插件并检查 `peerDependencies`。
- 🤖 Coding Agent 可复制提示词，按 `https://rslib.rs/guide/upgrade/v0-to-v1.md` 执行迁移。
- 🎯 默认语法目标：`output.target` 为 `node` 且未配置 `lib.syntax` 时，从 `package.json#engines.node` 推断；缺失则用 `esnext`，显式 `lib.syntax` 优先。
- 🧱 `es2023`、`es2024` 的 Browserslist 基准更新，并新增 `es2025`；只影响 JS/CSS 语法转换，不注入运行时 polyfill。保留旧行为可把 `es2023` 改为 `es2022`，`es2024` 改为 `esnext`。
- 🔗 ESM 输出默认 `externalsType` 从 `module-import` 改为 `modern-module`；主要影响外部 CommonJS 的 `require()`，静态/动态 ESM import 不变。
- 🛠️ 外部 CJS 在 `target: 'node'` 下使用 `createRequire()`，在 `target: 'web'` 下保留 `require()`；可用 `'module-import some-package'` 或 `tools.rspack` 恢复旧行为。
- 🌐 环境变量处理：v1 对 `esm`/`cjs` 不再构建时替换 `import.meta.env.*`、`process.env.BASE_URL`、`process.env.ASSET_PREFIX`；`cjs` 中 `import.meta.env` 变为 `undefined`，可用 `source.define` 恢复。
- 🖼️ ESM 资源处理：`new URL()` 静态资产会被 emit 并重写路径；需删除重复的 `output.copy`，bundleless 模式下排除匹配 `source.entry` 的资产。
- 🚫 可跳过 `new URL()` 处理：单条用 `/* rspackIgnore: true */`，全部用 `tools.bundlerChain` 设置 `rslib:new-url` 的 `url` parser 为 `false`；目录和仅构建输出文件不能作为静态资产处理。
- 👷 Web Workers：v1 会解析 `new Worker(new URL(...))`，构建 Worker 及其依赖，重写 URL 并添加 `type: 'module'`；应移除单独 worker entry，直接引用源文件。
- 🧩 Wasm：ESM 输出支持 `compile`（生成加载代码和 hash `.wasm`）与 `preserve`（保留 `.wasm` import 和原路径）；bundleless 默认 `preserve`，可设 `wasm.mode: 'compile'`。
- 📝 `@typescript/native-preview`：v1 不再默认加载，改为解析项目根 TypeScript，TS7+ 自动启用 `dts.tsgo`；继续使用需设置 `dts.typescriptPath`。
- 📁 临时声明目录从 `.rslib/declarations` 改为 `.rstack/declarations`，旧 `.rslib` 可安全删除。
- 📦 Node.js 模板：只提供纯 ESM 模板，`node-esm`→`node`、`node-esm-js`→`node-js`、`node-esm-ts`→`node-ts`，dual 模板不再支持；新模板默认 `engines.node` 为 `^20.19.0 || >=22.12.0`，并自动推断 `lib.syntax`。
- 🔁 若仍需 dual ESM/CJS 模板，使用 `npx -y [email protected] my-project --template node-dual`。
- ⚙️ 默认启用 `redirect.dts.extension`，bundleless 声明导入会加/替换为 `.js` 扩展；如需旧行为设 `redirect.dts.extension: false`。
- 🔄 `lib.autoExternal` 已弃用，建议迁移到 `output.autoExternal`；`experiments.advancedEsm` 已移除，ESM 高级行为默认开启。
- 🧾 JavaScript API：`RslibConfig.lib` 类型变为 `LibConfig[] | undefined`，省略 `lib` 等于 `lib: [{}]`；`inspectConfig()` 移除 `mode: 'none'`，省略时按 `NODE_ENV` 推断，`development` 下仅输出 `format: 'mf'` 的库配置。

---

### [](https://rslib.rs/blog/v1-0#declaration-generation)

**原文标题**: [Announcing Rslib 1.0 - Rslib](https://rslib.rs/blog/v1-0#declaration-generation)

Rslib 1.0 于 2026 年 9 月 3 日正式发布，这是基于 Rsbuild 的库开发工具，面向工具库、UI 组件库、CLI 与 Agent 应用等场景，依托 Rspack/webpack 生态，支持 Module Federation 和统一构建流水线，并开始遵循 SemVer 稳定演进。

- 🚀 Rslib 1.0 正式发布，基于 Rsbuild，帮助开发者以简单直接的方式构建不同类型的 JavaScript 库。
- 🧩 支持 Rsbuild 插件以及 Rspack/webpack 生态中的插件和 loader，应用若也使用 Rsbuild/Rspack 可共享配置与工程经验。
- 🌐 除 ESM、CJS 等常见格式外，还能生成 Module Federation 输出，让库作为远程模块被多个应用运行时加载。
- 🛠️ 提供统一库构建流水线，一次构建可完成 JS 编译、框架语法转换、声明生成和静态资源处理。
- 📈 自 0.7 公开发布后已推出 16 个次版本，1.0 起配置模型和 JavaScript API 稳定，并遵循 SemVer。
- ⚡ 性能显著提升：在 1 万个 React 组件基准中，相比 0.7.0，无缓存构建时间降约 24.3%，有缓存降约 56.7%，Gzip 前体积降约 32.2%，Gzip 后降约 4.1%。
- 🧾 声明生成更快：支持 TypeScript 7 的 tsgo 与 Isolated Declarations；在 Rsbuild 仓库测试中分别约快 2.4 倍和 4.2 倍。
- 📦 支持 ESM、CJS、UMD、IIFE、Module Federation 等输出格式，并重点优化 ESM 的静态分析、代码分割与外部依赖处理。
- 🖥️ 提供实验性可执行生成能力，基于 Node.js SEA，可打包单入口为无需目标系统安装 Node.js 的可执行文件。
- 🗂️ 支持 bundle 与 bundleless 两种构建模式：bundle 适合 SDK、CLI，bundleless 保留源码结构，适合组件库、工具库和 monorepo 内部包。
- ⚛️ 多框架支持 React、Vue、Svelte、Solid，可通过 create-rslib 选择模板；React 可启用 SWC 中的 React Compiler，bundleless 模式可保留 JSX。
- 🎨 样式支持开箱即用，包括 CSS Modules、PostCSS、样式抽取/内联/压缩，并可通过插件集成 Sass、Less、Stylus、Tailwind CSS。
- 🖼️ 支持图片、字体、音视频、JSON Import Attributes、new URL()、Web Worker 和 Wasm 等资源处理，并自动更新输出引用。
- ⚙️ 使用灵活：简单项目可用 CLI 无配置构建；复杂项目可用配置文件、顶层共享配置和 lib 数组；也提供 JavaScript API，支持 Node.js、Deno、Bun。
- 🧪 工作流集成完善：可与 Rstest 测试、Rspress 文档、组件预览、API 文档生成配合使用。
- ✅ 发布检查与分析：可用 publint、arethetypeswrong 检查包结构、导出和声明，用 Rsdoctor 分析构建时间、依赖关系和产物体积。
- 🤖 提供 Agent Skills，包括 rslib-best-practices、rslib-modern-package、migrate-to-rslib，以及 llms.txt、llms-full.txt、Markdown 文档和 AGENTS.md。
- 🚦 入门与迁移：可通过 StackBlitz 或 Quick start 开始；0.x 升级到 1.0 有破坏性变更，tsc/tsup 用户也有迁移指南。
- 🔭 后续方向：继续优化 ESM/CJS 输出、Node.js 打包、模块结构保留、声明生成，并加强测试、文档、质量检查和发布流程集成。
- 🙏 致谢 esbuild、mini-css-extract-plugin、tsdown、tsup、webpack 等开源项目及社区贡献者。

---

### [](https://rslib.rs/config/lib/experiments#experimentsexe)

**原文标题**: [lib.experiments - Rslib](https://rslib.rs/config/lib/experiments#experimentsexe)

Rslib 的 `lib.experiments.exe` 是一个实验性功能，可借助 Node.js SEA 将生成的 JavaScript 输出打包为可执行文件，支持布尔或对象配置，并可定制目标平台、文件名、输出路径和 SEA 选项。

- 🧪 `lib.experiments` 用于启用 Rslib 实验性功能；`experiments.exe` 通过 Node.js SEA 将 JS 输出打包为可执行文件，便于分发到未安装 Node.js 的系统。
- ⚙️ 相关类型包括 `SeaOptions` 与 `ExeOptions`，默认值为 `false`，且要求 Node.js 25.7.0 或更高版本。
- 🟢 Bun 和 Deno 可分别使用 `bun build --compile`、`deno compile`，对 Rslib 生成的 JavaScript 入口文件进行可执行文件打包。
- ✅ 启用条件：`format` 为 `'esm'` 或 `'cjs'`、`output.target` 为 `'node'`、`bundle` 为 `true`，且 `source.entry` 只能有一个入口。
- 🚫 启用后会禁用代码分割，并忽略 `output.autoExternal`、`output.externals`、`externalHelpers` 等相关选项，所有模块会直接打包进可执行文件。
- 🔘 布尔配置：设为 `true` 时，使用当前 `process.execPath` 作为模板，输出到当前 JS 输出目录，并使用当前平台、架构和 Node.js 版本；设为 `false` 或未指定则禁用。
- 📦 对象配置可自定义 `fileName`、`outputPath`、`targets`、`seaOptions`。
- 📝 `fileName` 默认使用入口 JavaScript 文件名；`win32` 会自动追加 `.exe`；多目标时会追加 `-<platform>-<arch>-<nodeVersion>` 以避免冲突。
- 📁 `outputPath` 默认输出到当前 JavaScript 输出目录，也可指定其他目录。
- 🎯 `targets` 支持字符串形式：自定义 Node.js 可执行路径，作为模板，并使用同版本、可在主机运行的 Node.js 二进制执行 `--build-sea`。
- 🧩 `targets` 也支持对象形式：声明 `platform`（`darwin`/`linux`/`win32`）、`arch`（`x64`/`arm64`）、`nodeVersion`；`nodeVersion` 接受 `25.9.0` 或 `v25.9.0`，缺省字段回退到当前主机环境。
- 🖥️ 未指定 `targets` 或传入空数组时，行为与布尔默认模式相同；也可一次构建多个平台的可执行文件。
- 🔐 macOS `darwin` 目标仅在 macOS 上构建时自动签名；若在 Linux 或 Windows 上生成 macOS 可执行文件，则输出未签名，通常需在 macOS 上签名后才能正常运行。
- 🌊 `seaOptions` 会直接传给 Node.js SEA；默认值为 `disableExperimentalSEAWarning: true`、`useSnapshot: false`、`useCodeCache: false`、`execArgvExtension: 'env'`。
- ⚠️ 若目标与当前主机平台或架构不同，Rslib 会自动禁用 `useSnapshot` 和 `useCodeCache`；且 `useSnapshot` 不能与 `format: 'esm'` 同时使用。
- ▶️ 运行示例：非 Windows 使用 `./hello world`，Windows 使用 `.\hello.exe world`，输出均为 `Hello, world!`。

---

### [虚拟 GPU](https://vgpu.sh/)

**原文标题**: [vgpu](https://vgpu.sh/)

一个着色器，处处渲染：同一 WGSL 可在浏览器与 headless Node.js 中复用，支持交互、任意分辨率、图片/视频导出，并能在 CI 中做无头快照测试。

- 🌐 同一着色器跨浏览器与 headless Node.js 运行，示例为 `effect(gpu, eveWgsl)` 后 `eve.draw({ target })`。
- 🖼️ 支持 Web 交互 canvas、PNG 8192×4608、MP4 60 fps 视频、CI headless artifact。
- ✅ CI 会编译 shader、渲染无头帧、比较快照；`pnpm test:render` 约 842ms 通过。
- 🧩 vgpu 像 TypeScript 一样导入/导出 WGSL：解析模块图、反射绑定、删除未用声明，构建时输出紧凑 shader（示例 397 B）。
- 💻 `render(canvas)` 示例演示 `init()`、`surface()`、`effect()`、设置 uniforms、`frame()` pass 与 `dispose()`。
- 🛠️ `npx vgpu` CLI 提供 docs、examples、check、doctor，用于读 API、拉参考、验证 WGSL、修复运行时。
- 🌌 示例包括 Transmission、Black Hole、FFT ocean surface、Radiance Cascades 等 WebGPU 演示。
- 📚 文档含 Getting Started、Core Concepts、API Reference、Examples；agent 工具可读 Examples API 与 OpenAPI 3.1。

---

### [](https://mikro-orm.io/blog/mikro-orm-7-2-released)

**原文标题**: [MikroORM 7.2: Trust Issues | MikroORM](https://mikro-orm.io/blog/mikro-orm-7-2-released)

MikroORM 7.2 发布，核心是将 PostgreSQL 行级安全（RLS）提升为一等实体元数据，由 schema generator 管理策略，并通过连接级会话上下文强制执行；同时新增 through to-one 关系、重做游标分页、推出 sql.js 驱动与文档内 playground，并加入命名参数、字符串规范化、原生客户端访问、await using 等改进。

- 🔐 RLS：策略可声明在实体上，支持 using/check、command、roles、permissive/restrictive，schema generator 负责创建、diff、内省并写入迁移快照。
- 🧭 会话上下文：EntityManager fork 可设置 session variables/role；默认 transaction 策略在事务内 set_config/set local role，connection 策略在连接获取时 reset all 后应用，适合 pgBouncer。
- 🛡️ Fail-closed：rowLevelSecurity: true 且无策略即拒绝所有；'force' 对表所有者生效；违规抛 RowLevelSecurityViolationException，上下文纳入结果缓存键。
- 🔗 过滤器桥接：现有 filter 标 rls: true 即可同时生成应用层 where 与数据库策略；无法静态编译的条件会在 schema 构建时报错。仅 PostgreSQL/pglite。
- 🧩 through 关系：只读 ManyToOne/OneToOne 可经中间实体解析，支持 where/orderBy，并用相关子查询取第一条匹配；无新列或 FK。
- 📄 游标分页：新增 Type.fromJSON() 控制自定义 datetime 类型 cursor 编码；可空排序键显式处理 nulls 位置，修复方向、$gt 与 null 块进入及嵌套 orderBy。
- 🧪 sql.js 驱动：@mikro-orm/sql-js 以 WASM 内存 SQLite 运行于浏览器/Node/Bun/Deno，无原生绑定，复用 SQLite 平台特性。
- 📚 文档 playground：getting-started 移除 StackBlitz，改为页面内 Monaco + sucrase + Web Worker 的真实数据库运行环境。
- 🧾 命名参数：em.execute()/connection.execute() 支持 :name 与 :name:，raw() 也支持并修复绑定顺序、重复 token、前缀冲突。
- 🧹 字符串规范化：StringType/TextType 支持 trim 和大小写转换，作用于写库与 ORM 查询参数，不改变内存属性值。
- 🔌 原生客户端：getNativeClient() 暴露各驱动底层客户端，如 pg Pool、better-sqlite3 Database、PGlite、MongoClient 等。
- ♻️ await using：MikroORM 实现异步释放协议，作用域结束自动 close；Node 22 运行时可用，语法需 Node 24+ 或转译。
- ⚙️ 其他：M:N 连接列索引、em.map() 绕过身份映射、RequestContext 回调选项、migrations.snapshotOnMigrate、nub TS loader、CLI -q、cache:generate --combined 指定路径。
- ⚠️ 升级注意：已有手写 RLS 策略可能被 schema diff 建议删除，需采纳或 ignorePolicies；可空排序在 MySQL/MSSQL 会新增 order by 项，MongoDB null 排序行为变化。

---

### [第 1 章：第一个实体 |](https://mikro-orm.io/docs/guide/first-entity#-checkpoint-1)

**原文标题**: [Chapter 1: First Entity | MikroORM](https://mikro-orm.io/docs/guide/first-entity#-checkpoint-1)

本文是 MikroORM 7.2 第一章“第一个实体”的入门教程，涵盖环境准备、项目创建、ESM/TypeScript/CLI 配置、定义 User 实体、初始化 ORM，以及通过 EntityManager 理解持久化、Unit of Work、Identity Map、事务和 CRUD 等核心概念。

- 🧰 先决条件：Node.js 22.11+，最好 24，并安装 npm 或其他包管理器。
- 📁 创建 `blog-api` 项目，在 `src/modules` 下划分 `user`、`article`、`common` 模块。
- 📦 运行时依赖包括 `@mikro-orm/core`、`@mikro-orm/sqlite`、`fastify`；开发依赖包括 `@mikro-orm/cli`、`typescript`、`tsx`、`@types/node`、`vitest`。
- 🧩 使用 ESM：在 `package.json` 添加 `"type": "module"`，使用 `import/export`，并在 TypeScript 导入中使用 `.js` 扩展名。
- ⚙️ TypeScript 配置：`module` 和 `moduleResolution` 设为 `NodeNext`，`target` 为 `ES2024`，启用 `strict`，输出到 `dist`。
- 🔧 MikroORM CLI 配置：使用 `defineConfig`，指定 SQLite 数据库 `sqlite.db`、`entities: [UserSchema]`，并开启 `debug`。
- 🚀 npm 脚本：`build` 用 `tsc`，`start` 用 `tsx src/server.ts`，`test` 用 `vitest`。
- 👤 第一个实体 `UserSchema` 用 `defineEntity` 定义，包含 `id`、`fullName`、`email`、`password`、`bio`，并用 `InferEntity` 推导类型。
- 🆔 主键可用 `p.integer().primary()` 自增，也可用 `p.bigint().primary()` 或 `p.uuid().primary().onCreate(...)`。
- 🧱 标量属性通过 `p.string()`、`p.text()`、`p.integer()`、`p.boolean()`、`p.datetime()`、`p.json<T>()` 映射，`bio` 使用 `text` 且默认 `''`。
- 🏗️ 初始化 ORM：可用 `MikroORM.init(config)`，也可用同步的 `new MikroORM(config)`，从而获得 `EntityManager` 和 `SchemaGenerator`。
- ✍️ 持久化：`em.create()` 创建并自动 `persist`，`em.flush()` 在事务中写入；已托管实体修改后直接 `flush` 即可更新。
- 🧠 Unit of Work 与 Identity Map：同一 EntityManager 中同 ID 返回同一实例，`flush` 时进行变更跟踪，仅更新变化字段。
- 🚫 不应使用全局 `orm.em` 执行上下文相关操作，应通过 `em.fork()` 获得隔离上下文，避免内存增长和 API 响应不一致。
- 🗄️ 用 `orm.schema.refresh()` 重建数据库 schema；用 `find`、`findOne`、`findOneOrFail` 查询，用 `em.refresh()` 强制重新加载。
- 🗑️ 删除可用 `em.remove(entity)` 或 `em.nativeDelete()`；`em.getReference()` 可创建仅含主键的实体引用。
- 🔍 `wrap(entity)` 可访问 `WrappedEntity` 状态，支持 `isInitialized()`、`init()`，以及 `toObject()`、`toPOJO()`、`toJSON()`。
- 🧭 替代实体定义方式：装饰器、文件夹扫描发现实体、EntityGenerator 从现有数据库生成实体；ESM 配合 Vitest 可配置 `dynamicImportProvider`。
- ⛳ 当前检查点：应用包含一个 `User` 实体和测试用 `server.ts`，可通过内存 SQLite 在 StackBlitz 中运行体验。

---

### [Javet 6.0.0 文档](https://www.caoccao.com/Javet/)

**原文标题**: [Javet 6.0.0 documentation](https://www.caoccao.com/Javet/)

Javet 是一个将 Node.js 和 V8 嵌入 Java 的优秀方案，名称来自 Java + V8（JAVa + V + EighT）。它提供跨平台支持、Node.js/V8 双模式、Java 与 JavaScript 互操作，并配套 Maven/Gradle 依赖与丰富文档。

- 🧩 Javet = Java + V8，用于在 Java 中嵌入 Node.js 和 V8。
- 🌟 官方鼓励 Star 项目、关注作者、加入 Discord，并可通过捐赠支持。
- 🖥️ 支持 Android、Linux、MacOS、Windows，覆盖 x86/x86_64/arm/arm64，但不同平台支持情况不同。
- ⚙️ 集成 Node.js v26.8.1 与 V8 v15.3.76.9，支持 i18n 和非 i18n。
- 🔄 支持 Node.js 与 V8 模式动态切换，并可用 Javenode 为 V8 模式提供 polyfill。
- 🔌 支持 JVM 中暴露 V8 API、JavaScript 与 Java 互操作、原生 BigInt 和 Date。
- 🧵 提供 Javet 引擎池、易用的 Spring 集成、Chrome DevTools 实时调试。
- 🧠 通过 swc4j 进行 AST 分析，并支持 JS、TS、JSX、TSX 转换与转译。
- 🛠️ 通过 JavetBuddy 增强 JVM 字节码，通过 JavetShell 进行实时交互。
- 📦 快速开始提供 Maven、Gradle Kotlin DSL、Gradle Groovy DSL 依赖，核心包加各平台 Node.js/V8 包，版本为 6.0.0。
- 👋 “Hello Javet”示例展示 Node.js 模式和 V8 模式下创建 V8Runtime 并执行字符串。
- 🤝 赞助商包括 HiveMQ、SheetJS、momen.app；许可证为 Apache License 2.0。
- 📚 博客涵盖 GraalJS/Javet/Nashorn 性能对比、V8 沙箱、TypeScript、SSR React + Spring Boot 等。
- 📖 文档包含教程、迁移指南、API 参考、V8 值、转换器、资源管理、故障排查、发布说明、FAQ 和开发指南等。

---

### [](https://github.com/caoccao/Javet)

**原文标题**: [GitHub - caoccao/Javet: Javet is Java + V8 (JAVa + V + EighT). It is an awesome way of embedding Node.js and V8 in Java. · GitHub](https://github.com/caoccao/Javet)

Javet 是 Java + V8（JAVa + V + EighT）项目，旨在让 Java 嵌入 Node.js 和 V8，仓库 caoccao/Javet 采用 Apache-2.0 许可，拥有约 961 Star、100 Fork，支持多平台、多架构，并提供引擎池、调试、互操作、TypeScript 工具链等能力。

- ⭐ 核心定位：在 Java/JVM 中嵌入 Node.js 与 V8，运行 JavaScript。
- 📜 开源信息：Apache-2.0 许可证，约 961 Star、100 Fork、18 Watcher。
- 🧩 平台支持：覆盖 Android、Linux、macOS、Windows，支持 x86、x86_64、arm、arm64 等架构。
- 🟢 引擎版本：集成 Node.js v26.8.1 与 V8 v15.3.76.9，提供 i18n 和非 i18n 版本。
- 🔁 模式切换：支持 Node.js 模式与 V8 模式动态切换，Javenode 可为 V8 模式提供 polyfill。
- 🔗 互操作能力：在 JVM 中暴露 V8 API，支持 JavaScript 与 Java 互操作，并原生支持 BigInt 和 Date。
- 🏊 引擎池：提供 Javet engine pool，便于管理运行时，且易于与 Spring 集成。
- 🐞 调试支持：可通过 Chrome DevTools 进行实时调试。
- 🔬 代码分析：借助 swc4j 做 AST 分析，并支持 JS、TS、JSX、TSX 转换与转译。
- ⚡ 增强工具：JavetBuddy 可通过字节码增强 JVM，JavetShell 支持实时交互。
- 📦 依赖配置：核心依赖为 com.caoccao.javet:javet:6.0.0，并按平台添加 Node.js 或 V8 artifact，支持 Maven、Gradle Kotlin DSL、Gradle Groovy DSL。
- 👋 快速示例：Node.js 模式使用 V8Host.getNodeInstance()，V8 模式使用 V8Host.getV8Instance()，再创建 V8Runtime 执行字符串。
- 💖 社区与支持：欢迎 Star、关注作者、捐赠，官方支持渠道为 Discord，赞助商包括 HiveMQ、SheetJS、momen.app。
- 📚 文档资源：提供安装页、Javet 介绍、Javadoc、文档门户及多篇博客，涉及性能对比、TypeScript、SSR 等主题。

---

### [](https://github.com/ota-meshi/eslint-plugin-regexp)

**原文标题**: [GitHub - ota-meshi/eslint-plugin-regexp: ESLint plugin for finding regex mistakes and style guide violations. · GitHub](https://github.com/ota-meshi/eslint-plugin-regexp)

eslint-plugin-regexp 是 ota-meshi 开发的开源 ESLint 插件，用于发现正则表达式错误与风格违规，并帮助编写更一致、更优化的正则表达式。仓库当前约 773 stars、17 forks、907 commits、15 issues、2 pull requests，采用 MIT 许可证。

- 📌 核心功能：查找 RegExp 错误与提示，强制一致的 RegExp 风格，并提供优化正则表达式的建议。
- 🧮 规则数量：提供 80 条插件规则，覆盖正则表达式语法和特性，可在在线 DEMO 中检查。
- 📖 文档与安装：文档位于 documents；安装命令为 `npm install --save-dev eslint eslint-plugin-regexp`。
- 🧾 环境要求：需要 ESLint v9.38.0 及以上；Node.js v20.19.0、v22.13.0、v24 及以上。
- ⚙️ 使用方式：在 `eslint.config.js` 的 plugins 中加入 `regexp`，可使用推荐配置、全部配置，或手动配置规则。
- ✅ 推荐配置：`plugin.configs.recommended` 启用对大多数用户最有用的规则子集；`plugin.configs.all` 主要用于测试，不建议生产使用。
- 🧩 规则分类：包括 Possible Errors、Best Practices、Stylistic Issues，并标注推荐、警告、可自动修复、可编辑器建议等状态。
- ⛔ 已移除规则：如 `no-assertion-capturing-group` 等已在 v2.0.0 移除，并给出替代规则。
- 🛠️ 贡献与版本：遵循 Semantic Versioning 和 ESLint 版本策略；欢迎通过 GitHub Issues/PRs 贡献，详见 `CONTRIBUTING.md`。
- 🧪 开发工具：`npm test` 运行测试与覆盖率；`npm run update` 更新 README 和推荐配置；`npm run new` 创建新规则文件；`npm run docs:watch` 本地预览文档。
- 🔒 许可证：MIT 许可证。
- 📊 仓库状态：907 次提交、15 个 issue、2 个 pull request、17 个 fork、773 个 star、4 个 watcher。

---

### [演练场 | eslint-plugin-regexp](https://ota-meshi.github.io/eslint-plugin-regexp/playground/)

**原文标题**: [Playground | eslint-plugin-regexp](https://ota-meshi.github.io/eslint-plugin-regexp/playground/)

该内容是一个 ESLint 规则与正则规则浏览页，汇总 eslint-plugin-regexp 与 ESLint 核心规则，并附有正则优化简化和问题检测示例。

- 🧭 页面顶部为 Playground、Star、Tweet、Filter，可按规则类别筛选查看。
- 🧩 eslint-plugin-regexp 规则分为 All Rules、Possible Errors、Best Practices、Stylistic Issues。
- ⚠️ 可能错误类关注无效正则、重复分支、控制字符、灾难性回溯等，如 no-invalid-regexp、no-super-linear-backtracking。
- ✅ 最佳实践类关注更安全、可读的正则写法，如 no-unused-capturing-group、prefer-regexp-exec、require-unicode-regexp。
- 🎨 风格类关注正则书写一致性，如 letter-case、sort-flags、prefer-named-capture-group、unicode-property。
- 🧱 ESLint 核心规则分为 Possible Errors、Suggestions、Layout & Formatting。
- 🚨 核心可能错误涵盖常见 JS 错误，如 no-unused-vars、no-undef、no-dupe-keys、valid-typeof。
- 💡 核心建议规则提供代码质量改进，如 prefer-const、eqeqeq、no-console、sort-imports。
- 📐 布局格式规则列出 unicode-bom，并出现 /eslint-plugin[-regexp]/u 等配置。
- 🛠️ Optimize and Simplify 示例展示可简化正则，如 [0-9][^\s]、^\w[_A-Z\d]*\e{1,}、(?<!\w)a+(?=$)。
- 🐛 Detect problems 示例展示检测问题，如 /\1(a)/ 反向引用位置错误、RegExp 字符串拼接。
- ⏳ 末尾“Now loading...”表示页面内容仍在加载。

---

### [@rgrove/parse-xml - v5.0.0](https://rgrove.github.io/parse-xml/)

**原文标题**: [@rgrove/parse-xml - v5.0.0](https://rgrove.github.io/parse-xml/)

overview summary
- 📌 @rgrove/parse-xml v5.0.0 是一个快速、安全、合规的 XML 解析器，适用于 Node.js 和浏览器。
- 📦 可通过 npm 安装 `@rgrove/parse-xml`，也可用 Unpkg 加载压缩包并在浏览器使用 `parseXml` 全局函数。
- 🌳 解析后返回便捷的 XML 对象树，所有对象都有 `toJSON()`，方便转换为 JSON。
- ⚠️ 文档格式不良时会抛出详细错误，包含错误信息、行、列、字符位置和上下文片段。
- 📜 基本符合 XML 1.0（第五版）非验证解析器，并通过 XML Conformance Test Suite 相关测试。
- ⚡ 使用 TypeScript 编写，Node.js 编译为 ES2020，浏览器为 ES2017，零依赖、速度快且体积小。
- 🚫 不加载外部 DTD、不根据 DTD 验证、不解析 DTD 内自定义实体引用，且仅支持 UTF-8。
- 🧭 目标是避免原生依赖、宽松解析、庞大 API、强制流式解析、错误处理差和浏览器不友好等问题。
- 🏁 基准测试中，小文档解析最快；中大型文档下 libxmljs2 更快，但依赖 C、无浏览器支持且有安全历史。
- 📄 项目使用 ISC 许可证。

---

### [](https://github.com/rgrove/parse-xml/releases/tag/v5.0.0)

**原文标题**: [Release v5.0.0 · rgrove/parse-xml · GitHub](https://github.com/rgrove/parse-xml/releases/tag/v5.0.0)

rgrove/parse-xml 发布 v5.0.0：API 完全不变，但包格式改为 ES 模块、最低 Node.js 版本提升，并包含若干破坏性变更。

- 🚀 v5.0.0 由 rgrove 于 8 月 30 日 03:21 发布，提交 b15e011，签名已验证。
- 📦 parse-xml 现已改为 ES 模块：包中设置 `"type": "module"`，发布 ESM 而非 CommonJS。
- ✅ 若已使用 `import { parseXml } from '@rgrove/parse-xml'`，无需修改；Node.js 22+ 中 `require()` 也可通过 `require(esm)` 继续使用。
- ⚠️ 无法解析 ESM 的打包器/运行时会失效；CommonJS + TypeScript 项目需 TypeScript 5.8+ 和 `"module": "nodenext"`，旧版 TS 或 `"module": "node16"` 会报错。
- 🟢 最低支持的 Node.js 版本从 14.0.0 提升至 22.12.0。
- 📤 新增 `exports` 映射，仅公开 API 可导入：根入口和 `Xml*` 节点类不受影响，但 `Parser`、`StringScanner`、`syntax`、`types` 不再可导入。
- 🌐 浏览器包 `dist/browser.js` 改为 ESM，打包器可透明处理，并缩小 1.1 KB；`dist/global.min.js` 不变，CDN `<script>` 与全局 `parseXml` 用法照旧。
- 📉 发布到 npm 的包体积约缩小 40%（打包后 48 KB，4.2.3 为 82 KB），因移除不必要的 sourcemap。
- 🔗 完整变更日志：v4.2.3...v5.0.0。

---

### [](https://github.com/rawify/dhcp.js)

**原文标题**: [GitHub - rawify/dhcp.js: Type-safe DHCPv4 client, server, relay-aware watcher, and packet tools for Node.js · GitHub](https://github.com/rawify/dhcp.js)

dhcp.js 是一个面向 Node.js 的无依赖、类型安全 DHCPv4 客户端、服务器与流量监视器，提供原生 ESM、CommonJS 和 TypeScript 声明，可用于在 Node 进程内实现或观察 DHCPv4，包括中继、PXE、多子网、静态分配和 RFC 3118 认证，但不会自动配置主机接口；页面顶部虽有加载错误提示，README 主体内容完整。

- 📦 安装与要求：`npm install dhcp`；需要 Node.js 20+，绑定 UDP 67/68 的权限，以及允许 IPv4 广播的接口和防火墙配置。
- 🖥️ 服务器功能：`createServer` 支持地址范围、服务器/路由器/DNS/netmask/租期配置；动态范围包含端点，静态地址和服务器地址不会从动态池分配，过期租约可回收，池耗尽触发 `poolExhausted`。
- 🧷 静态分配与策略：支持 `static` 对象、`static(request)` 包感知回调和 `staticReservations`；`allocationPolicy: 'static-only'` 仅服务已识别客户端，未知请求被忽略并触发 `clientIgnored`。
- 🛡️ 地址冲突检测：可选 `addressProbe` 通过系统 ARP/邻居缓存探测地址；不可判定时失败开放并触发 `addressProbeInconclusive`；冲突动态地址隔离，冲突静态地址标记为 declined，也可注入原生 raw-socket 探测器。
- 📨 报文与选项：`broadcast` 配置 DHCP option 28；无 option 57 时响应限制为 576 字节，支持 `maxMessageSize`；标准选项均可配置或回调，`forceOptions` 可强制发送，默认包含 netmask、server/router、DNS、一天租期和随机分配。
- 🧑💻 客户端功能：`createClient` 支持 `mac`、`clientId`、`vendorClassId` 和 `features`；自动处理 T1 续租、T2 重绑定和到期，可用 `autoRenew:false` 手动 `sendRenew()`、`sendRebind()`、`sendRelease()`；支持 `addressChanged` 事件，但不修改操作系统接口配置。
- 🔐 RFC 3118 认证：服务端边界支持 option 90，推荐 Delayed Authentication，使用 HMAC-MD5 和递增重放值；认证发生在消息处理、地址选择和租约变更之前，失败触发 `authenticationFailed`；token 模式仅兼容且不是密码认证；内置客户端尚不发起 RFC 3118。
- 🧩 自定义与 ACK 选项：未知选项保留为 `Uint8Array`；可注册 `optionDefinitions` 或使用 `createOptionRegistry()`；`ackOptions` 仅出现在 DHCPACK，显式选项可覆盖配置，但保护消息类型 53 和回显的 option 82。
- 🌐 多子网与中继：`subnets` 支持独立池，按 `match(packet)`、option 118、`giaddr`、请求地址或 `ciaddr` 匹配；中继支持 RFC 3046 option 82，按 `giaddr` 限定租约身份并逐字节回显；`relayBindings` 使用字节精确匹配并自动预留地址。
- 🚀 PXE 支持：内置 RFC 4578 选项 93/94/97 的二进制格式；PXE 请求的 128–135 若未配置则静默省略，已知 PXE 选项长度错误会作为报文错误拒绝。
- 📊 日志与事件：默认以 info 级别输出结构化 JSON 日志，可设 `logLevel` 或注入 logger；服务端和客户端提供 `message`、`state`、`stage`、`bound`、`released`、`declined`、`poolExhausted`、`addressConflict`、`authenticationFailed`、`listening`、`error` 等事件；`close()` 幂等。
- 👀 流量监视与 CLI：`createBroadcastHandler` 可被动监听 DHCP 报文，例如识别 `DHCPDISCOVER`；命令行提供 `sudo dhcpd` 和 `dhcp`，正常运行时静默，`-v`/`-vv` 可开启可读或调试日志。
- 🔁 兼容与许可：保留 CommonJS API 以及 `createServer`、`createClient`、`createBroadcastHandler` 等原名称，并提供子路径导出；项目使用 MIT 许可证，Copyright 2026 Robert Eisele，仓库约有 308 stars、70 forks、8 issues。

---

### [dhcp.js：Node.js 的 DHCP 客户端和服务器 • RAW](https://raw.org/software/libraries/dhcp-js/)

**原文标题**: [dhcp.js: A DHCP client and server for Node.js • RAW](https://raw.org/software/libraries/dhcp-js/)

dhcp.js 是适用于 Node.js 的无依赖 DHCPv4 客户端、服务器和广播流量监视器；1.0.0 版支持 ESM、CommonJS 和 TypeScript，覆盖 DORA、多子网中继、自定义选项、安全校验与 CLI 工具。

- 📦 dhcp.js 是无运行时依赖的 DHCPv4 客户端、服务器和流量监视器，包名为 `dhcp`，项目名为 `dhcp.js`。
- 🔁 DHCP 地址分配采用 DORA 四步交换：DHCPDISCOVER、DHCPOFFER、DHCPREQUEST、DHCPACK；服务器监听 UDP 67，客户端监听 UDP 68。
- ⚠️ DHCP 是无连接协议，租约是跨数据报维护的协议状态；实验应使用隔离网络，避免生产 LAN 上出现第二个 DHCP 服务器导致错误网关或 DNS 配置。
- 🛠️ 安装要求 Node.js 20+，使用 `npm install dhcp`；同一包支持 ESM、CommonJS 和 TypeScript 声明。
- 🖥️ 服务器通过 `createServer` 配置动态地址范围、固定静态分配、服务器地址、路由器、DNS、子网掩码和租约时间，并触发 `bound`、`poolExhausted`、`error` 等事件。
- ⚙️ 注册选项可设为固定值或回调，例如按 `clientId` 动态返回 `bootFile`；动态静态分配回调可能返回的地址需预先列入 `staticReservations`。
- 🔍 可选地址冲突检测支持 `addressProbe`、超时和保留时间，并触发 `addressConflict` 或 `addressProbeInconclusive`；Node.js 无原生 raw-ARP，严格场景需注入原生 `AddressProbe`。
- 💻 客户端通过 `createClient` 支持 `mac`、`clientId`、`vendorClassId` 和 `features`，负责发现、T1 续租、T2 重绑和过期报告。
- 🧩 客户端不会修改主机接口、路由表、DNS 解析器或主机名；`bound` 事件仅暴露协商状态，应用需自行应用配置，也可关闭自动续租并手动释放。
- 📡 `createBroadcastHandler` 可被动解码本地 DHCP 流量，适合诊断和库存；绑定 `0.0.0.0` 接收有限广播，但 MAC 可随机或伪造，不能作为认证或安全关键依据。
- 🌐 多子网依赖中继代理和 `giaddr`；`subnets` 支持独立地址池，并按匹配策略、option 118、`giaddr`、请求地址或 `ciaddr` 选择，option 82 会原样保留。
- 🧾 未知 DHCP 选项保留为 `Uint8Array`，可注册实例局部选项定义；支持 PXE 选项 93、94、97，option 43 可用导出的 TLV 辅助工具处理。
- 🔐 经典 DHCP 不验证服务器或客户端可信；1.0.0 可验证 RFC 3118 option 90，但算法为 HMAC-MD5，内置客户端尚不发起认证交换，应配合 DHCP snooping 等措施。
- 📜 还支持 RFC 3203 FORCERENEW、RFC 6842 客户端标识回显、ACK-only 选项、最大消息协商以及类型化或不透明私有选项。
- 🧰 全局安装提供 `dhcpd` 服务器和 `dhcp` 客户端命令；`-v` 输出可读状态，`-vv` 输出结构化调试日志，特权网络服务应以最小权限运行。
- 📚 相关文章包括 macOS 命令行互联网共享、macOS 网络速查表，以及 CodinGame 网络主机数解法。

---

### [发布 pnpm 12.4 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v12.4.0)

**原文标题**: [Release pnpm 12.4 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v12.4.0)

pnpm v12.4.0 发布，重点支持在同一工作区管理 npm、Python 与 Cargo 依赖，新增 `pnpm pipeline` 任务编排，并带来大量锁文件、注册表、Windows 和跨平台修复。

- 🐍 支持 Python 依赖：启用 `python.enabled`，用 `pnpm add pypi:<package>` 安装，支持 `pyproject.toml`、`pylock.toml`、托管 `.venv` 及冻结/离线安装。
- 🦀 支持 Cargo 依赖：启用 `cargo.enabled`，用 `pnpm add crate:<package>` 安装，支持 crates.io、自定义 sparse registry 和凭据认证。
- ⚙️ Python 与 Cargo 均可通过 `pnprServer` 加速解析，不支持时回退本地解析。
- 🧩 新增 `pnpm pipeline [name]`：安装冻结依赖并运行 `pipelines` 中声明的任务图，任务失败后仍继续执行。
- 👀 `pnpm pipeline --dry-run` 可预览任务图，不安装配置依赖或运行 workspace hooks。
- 💻 新增平台支持：Android arm64/x64、FreeBSD x64、Linux ppc64le、s390x、RISC-V。
- 🧹 新增 `trustPolicyExcludePrune`，可在 `add/update/remove` 时自动清理未使用的 `trustPolicyExclude`，默认关闭。
- ✅ 新增 `pnpm change check`，用于 CI 校验包版本是否符合 `versioning.epics` 和 `versioning.fixed` 分组。
- 🔐 注册表元数据按 URL 路径与协议隔离，避免混用不同 registry 的版本、tarball 或 HTTP/HTTPS 元数据。
- 🧾 `pnpm cache view` 现在显示完整 registry URL，相关解析脚本需要更新。
- 🛠️ 新增构建脚本或 `binding.gyp` 的补丁会触发构建审批；支持 `--allow-build=!<pkg>` 和 `approve-builds` 保存决定。
- 🌐 `.npmrc` 中的 registry 优先于 `pnpm login` 保存的全局配置，修复登录后使用错误 registry。
- ⏱️ `fetch-timeout` 改为限制无进展时间，慢速大文件下载不再超时。
- 🚀 提升大型工作区安装、`pnpm deploy`、warm global virtual store 等场景性能，并修复相关锁文件错误。
- 📦 修复 `pnpm add --workspace <pkg>`，支持 `workspace:` 协议；`add/install` 接受 `jsr:`、`npm:`、`workspace:` 等协议前缀。
- 🔁 布尔标志支持显式值，如 `--prod=false`；`pnpm install <pkg>` 支持 `--offline` 与 `--prefer-offline`。
- 🧷 修复 `frozen-lockfile`、符号链接锁文件、`lockfileDir` 版本固定、`pnpm import`、`patch-commit`、版本范围上界等问题。
- 🪟 修复 Windows 下 `pnpm setup`、命令 shim 重试、`shellEmulator` 参数转发、store 路径反斜杠等兼容问题。
- 🔍 其他改进：`audit` 汇总排除忽略项、`pack --json` 错误 JSON、`outdated -r` 表格换行、shell 补全支持 `pn` 别名、`pnpm version -m` 短别名。

---

### [发布 v10.](https://github.com/nodemailer/nodemailer/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · nodemailer/nodemailer · GitHub](https://github.com/nodemailer/nodemailer/releases/tag/v10.0.0)

Nodemailer 发布 v10.0.0，这是一次包含重大变更的版本更新：核心要求升级到 Node.js 20+，移除旧兼容检查与 .npmignore，并迁移到 TypeScript、支持 ES module 与 CommonJS 双构建；同时修复了配置、DKIM、URL 解析、SMTP 连接/连接池等多处问题。

- 🚀 v10.0.0 已发布，提交 2ee030c 由 GitHub Actions 创建，并带有 GitHub 已验证签名。
- ⚠️ 重大变更：Node.js 20 或更高版本成为必需；Node.js 6 语法兼容检查和 .npmignore 文件被移除。
- 🧩 新特性：保持 @types/nodemailer 类型布局可用；迁移到 TypeScript，并提供 ES module 与 CommonJS 构建。
- ⚙️ 配置修复：应用配置对象时，除 url 之外的其他键也会生效。
- ✉️ DKIM 修复：按验证器的方式规范化原始邮件。
- 🔌 类型修复：确保 transporter 仍可赋值给普通 Transporter 类型。
- 🌐 URL 解析修复：保留连接或代理 URL 用户名中的冒号；拒绝旧解析器会截断的 URL 主机；运行时无接口表时解析主机名。
- 📡 SMTP 连接修复：连接在问候前断开时清除定时器；避免不完整的服务器回复进入 lastServerResponse。
- 🏊 SMTP 连接池修复：代理 socket 无法打开时释放连接池槽位。
- 📦 well-known 修复：保持 nodemailer/lib/well-known/services.json 可用。
- 📈 仓库数据：约 17.7k Star、1.4k Fork；页面部分区域出现加载错误，需重新加载。
- 👍 社区反应：1 个 👍、4 个 ❤️，共 5 人反应。

---

### [发布 v5.12.2 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.12.2)

**原文标题**: [Release v5.12.2 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.12.2)

overview summary
- 🚀 Fastify 仓库发布 v5.12.2，标记为最新版本，由 mcollina 于 9 月 4 日 08:20 发布，提交 942a2be 且签名已验证。
- 🔐 这是一个安全版本，修复 GHSA-9q9j-q6p8-xq58、GHSA-hwr6-493r-vm6h、GHSA-p68q-wchp-6fh7、GHSA-667r-xxjv-c9mm 四个安全公告。
- 🛠️ 包含 5.x 回溯修复：callNotFound 现在无论注册顺序都会运行 not-found preHandler（#6973）。
- 📦 包含 5.x 回溯杂项：在 npm 中忽略剩余 agent 文件（#7003）。
- 🔗 完整变更日志对比为 v5.12.1...v5.12.2；该版本提供 2 个资产。
- 📊 仓库 fastify/fastify 为公共仓库，约有 37.1k stars、3k forks、56 issues、94 pull requests 和 14 项安全与质量信息；修改通知设置需登录。
- ⚠️ 页面多次出现加载错误并提示重新加载，可能影响部分内容显示。
- 🎉 该发布获得 2 个庆祝反应，来自 NetLancer 和 HamoBoker。

---

### [](https://github.com/tinylibs/tinybench)

**原文标题**: [GitHub - tinylibs/tinybench: 🔎 A simple, tiny and lightweight benchmarking library! · GitHub](https://github.com/tinylibs/tinybench)

Tinybench 是 tinylibs 下的简单、极小且轻量的 JavaScript 基准测试库，基于 Web API 实现精确计时，支持多运行时、统计分析、并发、计时器诊断与中止控制，适合微基准和性能测试。
- 🔎 无依赖且跨运行时：完全基于 Web API，可在多个 JavaScript 运行时中使用，适合轻量基准测试。
- ⏱️ 精确计时：根据环境使用 `process.hrtime` 或 `performance.now`，默认使用 `performance.now`。
- 📊 统计分析：提供延迟和吞吐量的标准差、误差范围、方差、百分位等指标，并用 `bench.table()` 输出表格。
- 🧩 基本用法：通过 `new Bench()` 创建实例，用 `add()` 添加任务，再 `await bench.run()`；任务名必须唯一，且默认不打印结果。
- 📦 安装方式：使用 `npm install -D tinybench` 安装为开发依赖。
- 🔁 异步与并发：自动检测异步任务或返回 Promise 的任务，也可显式设置 `async`；并发模式支持 `null`、`'task'`、`'bench'`，可用 `threshold` 限制并发迭代。
- 🧪 样本保留：通过 `retainSamples: true` 保留原始延迟和吞吐样本，便于绘图、自定义分析或导出。
- 🕒 时间戳提供者：支持 `performanceNow`、`hrtimeNow`、`bunNanoseconds`、`auto` 或自定义 `TimestampProvider`。
- 🧮 计时器开销校正：`subtractTimerOverhead` 可校准并扣除计时器调用成本，也可直接使用 `calibrateTimerOverhead`；与 `concurrency: 'task'` 不兼容。
- 📐 任务自报测量：任务可返回 `overriddenDuration` 和 `overriddenIterationCost`，用于外部计时或批量调用统计，但需注意预算与统计语义。
- 🚨 计时器诊断：运行后暴露 `detectedResolution`；当样本出现零主导、低区分度或零 MAD 时触发 `warning` 事件，并提供相关辅助函数。
- 🛑 中止支持：支持 bench 级和 task 级的 `AbortSignal` 中止，执行中也可中止并触发 `abort` 事件；`runSync()` 无法被外部计时器中断。
- 📡 事件系统：`Bench` 和 `Task` 继承 `EventTarget`，可监听 `cycle`、`warning`、`abort` 等事件。
- 📚 文档与生态：提供 FAQ、Bench、Task、TaskResult、Events 文档和 examples 目录；项目采用 MIT 许可证。
- ⭐ 仓库数据：约 2.4k stars、60 forks、10 个 issues、4 个 PR、924 次提交；欢迎贡献和赞助。

---

### [](https://github.com/mapbox/supercluster)

**原文标题**: [GitHub - mapbox/supercluster: A very fast geospatial point clustering library for browsers and Node. · GitHub](https://github.com/mapbox/supercluster)

supercluster 是 Mapbox 维护的高性能 JavaScript 地理空间点聚合库，可在浏览器和 Node 中对 GeoJSON 点进行快速聚类，常用于地图应用处理海量点位。

- 🚀 定位：用于浏览器和 Node 的超快地理空间点聚合库，旨在为 Mapbox GL JS 提供聚合能力。
- 🗺️ 能力：可在 Leaflet 中聚合 600 万个点，适合大规模地图点位展示。
- 📦 安装：支持 npm/yarn 安装，也可通过 ES module、CDN 或普通 script 标签引入。
- 🧩 核心方法：load 加载点数据；getClusters 按 bbox/zoom 查询；getTile/getTileRaw 获取瓦片；getChildren、getLeaves、getClusterExpansionZoom 处理聚类层级与展开。
- 📍 数据要求：load 接收 GeoJSON Feature 数组，geometry 必须是 Point 或 MultiPoint；MultiPoint 会按每个坐标独立聚合，并继承 properties 和 id。
- ⚙️ 主要选项：minZoom、maxZoom、minPoints、radius、extent、nodeSize、log、generateId；maxZoom 上限为 30。
- 📊 属性聚合：支持 map/reduce 自定义聚类属性，例如累加 myValue；map 必须返回新对象，reduce 不得修改第二个参数。
- 🧾 TypeScript：内置类型声明，可直接导入 Options、PointFeature、ClusterFeature、Tile、RawTile 等命名导出。
- 🛠️ 开发：使用 npm install 安装依赖，npm run build 构建，npm test 运行测试。
- 📈 仓库信息：约 2.4k stars、304 forks、23 issues、9 PRs、186 commits，采用 ISC 许可证。
- ⚠️ 页面加载时曾提示错误，可刷新页面重试。

---

### [iGaming 欺诈预防 | Fingerprint](https://fingerprint.com/igaming/?utm_source=NodeWeekly09102026)

**原文标题**: [iGaming Fraud Prevention | Fingerprint](https://fingerprint.com/igaming/?utm_source=NodeWeekly09102026)

Fingerprint 面向 iGaming 行业提供设备智能与反欺诈平台，核心是从注册到提现保护账户安全，减少账户接管、拒付和奖金滥用，并通过高精度设备指纹、多源信号和合规认证帮助平台降低损失、维护玩家信任。

- 🎯 定位：为 iGaming/博彩平台提供设备智能，阻止账户接管、拒付和奖金滥用。
- 🤝 信任背书：被全球游戏与博彩领导者使用，覆盖从注册到提现的安全防护。
- 🛡️ 账户安全：识别异常登录、阻止暴力破解，并防范机器人、虚假用户和欺诈交易。
- 🎁 促销风控：防止小号注册、多账户和匹配投注等奖金与促销滥用。
- 💳 支付保护：标记风险交易、阻止卡测试攻击，降低拒付并维护用户信任。
- 📚 教程支持：提供分步指南，快速识别访客并阻止游戏欺诈，如提现、登录、优惠码场景。
- 📡 多源信号：结合网络、AI/机器人、行为和设备信号，覆盖浏览器与移动设备。
- 👩‍💻 开发者友好：提供 API、SDK 和 Webhooks，几行代码即可快速接入。
- ✅ 合规认证：符合 SOC 2 Type II、GDPR、CCPA、ISO 27001 等企业级要求。
- 🔒 技术优势：原创指纹库，具备先进检测与隐私技术；VisitorID 准确稳定，可保持数月。
- 📞 销售联系：可咨询套餐、定价、企业合同或演示，表单收集工作邮箱、公司网站、API 调用量等项目信息。
- 🧭 资源导航：官网涵盖产品、用例、资源、文档、演示、定价、开发者社区与公司信息等。

---

### [适用于任意规模](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

Tiger Cloud 为任意规模的时序工作负载提供 PostgreSQL 服务。单个服务可达到每天 3 万亿指标、3 PB 数据和 1 千万亿数据点的真实规模；新账户注册可获 1000 美元信用额度，30 天有效，无需信用卡，并受到 IoT 等领域数千家公司信赖。

- 📊 超大规模：单个 Tiger Cloud 服务可处理每天 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 💳 新户优惠：注册即得 1000 美元信用额度，30 天有效，无需信用卡，仅限新账户。
- 🤝 客户信任：IoT 等领域数千家公司正在使用。
- ⚙️ 核心能力：读写分离，最多 10 节点副本集，配合 SSD/S3 分层存储，实现低成本海量存储。
- 💸 成本优化：计算与存储分离，可独立扩展，避免为闲置容量付费。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级合规：符合 SOC 2、HIPAA、GDPR，支持始终加密、SSO、RBAC 和审计日志。
- 🔎 深度可观测：查询下钻与仪表板，指标可发送至 CloudWatch、Datadog、Prometheus。
- 🚀 快速部署：几分钟内配置数据库，可通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 生态集成：兼容首选云厂商及更广泛的 Postgres 生态。
- 🏢 企业支持：合同化 SLA、区域数据隔离、企业合规认证，以及 24/7 全球 Postgres 专家支持。
- 📄 其他信息：包含隐私偏好、法律、隐私、站点地图，以及 2026 Timescale/Tiger Data 版权信息。

---

### [](https://react.dev/blog/2026/09/09/react-19-3)

**原文标题**: [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3)

React 19.3 正式发布，核心亮点是 View Transitions 与 Fragment Refs 转为稳定 API，并新增 `browser()`、Trusted Types 支持、Server Components 直接渲染 `<Context>`，同时包含多项性能改进与错误修复。

- 🚀 React 19.3 已发布到 npm，View Transitions 和 Fragment Refs 不再处于实验阶段。
- 🎬 `<ViewTransition>` 基于浏览器 View Transition API，可为元素进入、退出、更新、共享位置添加动画。
- 🎛️ `addTransitionType` 可标记 Transition 原因，例如前进/后退，从而为同一状态更新选择不同动画。
- ⏳ View Transitions 可与 Suspense 配合，动画化 fallback 到最终内容，也能让图片、字体加载触发 Suspense。
- 🧩 Fragment Refs 允许将 `ref` 传给 `<Fragment>` 获取 `FragmentInstance`，对子 DOM 组执行事件、焦点、观察、测量等操作。
- 🌐 React DOM 新增 `browser()`：组件可用 `use(browser())` 退出服务端渲染，服务端触发 Suspense，客户端不挂起。
- 🔐 集成 Trusted Types API，React 不再把值强制转成字符串，更好配合严格 CSP 防止 DOM XSS。
- 🖥️ Server Components 现在可直接渲染从 `'use client'` 模块导入的 `<Context>`，无需额外 Provider 包装。
- ⚙️ 其他改进包括 Render Transitions 独立执行、Strict Mode hydration 双调用 Effects、新增全屏事件、`maskType`、`fetchPriority` 等支持。
- 🐞 修复了 `useDeferredValue` 卡住、Suspense fallback 上下文传播、`useSyncExternalStore`、`<ViewTransition>` 崩溃、hydration mismatch 等问题。
- 📚 完整变更与修复列表见官方 Changelog。

---

### [](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)

**原文标题**: [Trusted Types API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)

overview summary
- 🛡️ Trusted Types API 让开发者在数据进入可能执行代码的注入汇前，先经过指定的转换/净化函数，以防御客户端 XSS。
- 📅 该特性自 2026 年 2 月起成为 Baseline 2026 新可用功能，适用于最新设备和浏览器版本；旧设备/浏览器可能不支持，并支持 Web Workers。
- 🧩 核心做法：开发者定义策略对象，为不同类型注入汇提供转换方法；API 本身不提供策略或净化函数。
- 🚰 三类注入汇：HTML 汇（如 innerHTML、document.write）、JavaScript 汇（如 eval、脚本文本）、JavaScript URL 汇（如脚本 src）。
- 🧱 三种可信类型：TrustedHTML 用于 HTML 汇；TrustedScript 用于 JS 汇；TrustedScriptURL 用于脚本 URL 汇。
- 🏭 入口是 Window 和 Worker 中的 trustedTypes 全局属性，用于创建策略并验证可信类型实例。
- 🧼 示例：用 trustedTypes.createPolicy 定义 createHTML，内部调用 DOMPurify.sanitize，再通过 policy.createHTML 生成 TrustedHTML 传给 innerHTML。
- 🔒 CSP 指令 require-trusted-types-for 强制注入汇只接受可信类型；直接传字符串会抛出 TypeError。
- 📋 CSP 指令 trusted-types 指定允许创建的策略名白名单，防止意外创建策略。
- 🧯 default 策略：当代码仍向注入汇传字符串时自动调用，帮助发现并迁移遗留代码；建议仅过渡期使用；若返回 null/undefined 会抛 TypeError。
- 📥 直接 HTML 注入汇包括 Document.write/writeln、Element.innerHTML/outerHTML、DOMParser.parseFromString、Range.createContextualFragment 等。
- ⚙️ 直接 JavaScript 注入汇包括 eval、Function/AsyncFunction 构造器、setTimeout/setInterval 的 code 参数、script.text/textContent 等。
- 🔗 直接 JavaScript URL 注入汇包括 HTMLScriptElement.src、importScripts、Worker/SharedWorker 的 url、ServiceWorkerContainer.register 等。
- 🕵️ 间接注入汇：字符串经中间机制进入 DOM，如 createTextNode 后 appendChild 到 script；浏览器在脚本可执行时检查是否可信，否则尝试 default 策略或抛异常。
- 🧩 Tinyfill 为不支持 Trusted Types 的浏览器提供最小兼容；createPolicy 直接返回规则对象，使同一净化代码路径可用于旧浏览器。
- 🛠️ 主要接口：TrustedHTML、TrustedScript、TrustedScriptURL、TrustedTypePolicy、TrustedTypePolicyFactory。
- 🌐 HTTP/CSP 扩展：require-trusted-types-for、trusted-types，以及关键词 trusted-types-eval。
- 📚 示例：创建 escapeHTMLPolicy 转义特殊字符，生成 TrustedHTML 后赋给 innerHTML，确保不注入新 HTML 元素。
- ✅ 在支持浏览器中通过 CSP 强制 Trusted Types，可推动代码统一净化；结合 tinyfill，可在不支持环境中获得同等代码路径保护。

---

### [VS Code 的故事 | 官方纪录片 - YouTube](https://www.youtube.com/watch?v=kHL3XzjpT5w)

**原文标题**: [The Story of VS Code | Official Documentary - YouTube](https://www.youtube.com/watch?v=kHL3XzjpT5w)

此內容為 YouTube 網站頁尾的導覽與法律資訊列表，涵蓋平台介紹、新聞、版權、聯絡方式、創作者、廣告、開發者、條款、私隱、政策安全、運作方式、測試功能，以及 2026 年 Google LLC 版權標示。

- ℹ️ 提供「簡介」連結，說明平台基本資訊。
- 📰 設有「新聞中心」，發布相關消息與更新。
- ©️ 包含「版權」相關資訊。
- 📞 提供「聯絡我們」管道。
- 🎬 面向「創作者」的專屬連結。
- 📢 可前往「刊登廣告」頁面。
- 👨‍💻 提供「開發人員」資源。
- 📜 列出「條款」內容。
- 🔒 包含「私隱」政策連結。
- 🛡️ 設有「政策及安全」資訊。
- ⚙️ 說明「YouTube 的運作方式」。
- 🧪 提供「測試新功能」入口。
- ©️ 標示「© 2026 Google LLC」版權所有。

---

### [NW.js](https://nwjs.io/)

**原文标题**: [NW.js](https://nwjs.io/)

NW.js（原名 node-webkit）是一个使用 HTML5、CSS3、WebGL 等 Web 技术编写原生应用的框架，可直接从 DOM 和 Web Workers 调用 Node.js 模块，完整支持浏览器功能与 Node.js API，并可跨平台运行。
- 🌐 使用 HTML5、CSS3 和 WebGL 等 Web 技术构建原生应用
- 🧩 完整支持浏览器功能
- 📦 完整支持 Node.js API 及所有第三方模块
- 🔗 可直接从 DOM 和 Web Workers 调用 Node.js 模块
- 🔒 支持 JavaScript 源代码保护
- 💻 支持 Linux、Mac OS X 和 Windows
- 📥 提供下载、博客和文档入口
- 📚 帮助资源包括文档、Wiki 和 Bug 反馈
- 💬 社区渠道包括邮件列表、Gitter 和 Discord
- 🐙 可通过 GitHub 和 Twitter 连接项目
- ©️ 版权归 NW.js community，2015-2026

---

### [Tailwind Labs 加入 Shopify - Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

**原文标题**: [Tailwind Labs is joining Shopify - Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

Tailwind CSS 创始人宣布 Tailwind 正式加入 Shopify，为这个每周安装量超 1.1 亿次、被多家大型公司采用的开源框架提供长期稳定的维护支持。Shopify 本身深度使用 Tailwind，作者希望借真实产品场景推动框架演进；开源项目和许可证保持不变，商业业务将停止扩张，团队将专注在 Shopify 继续维护 Tailwind CSS。

- 🚀 Tailwind 正式加入 Shopify，目标是为其提供长期稳定、持续维护的家园。
- 📈 从九年前的个人项目起步，如今 Tailwind 每周安装量超过 1.1 亿次，被 ChatGPT、X、Cloudflare、Reddit、Shopify 等使用。
- 🛍️ 选择 Shopify 的原因：希望在真实复杂产品中开发框架，解决真实用户问题，并反哺 Tailwind。
- 🧱 Shopify 提供丰富场景：商家定制店面、管理销售与库存，消费者购物结账、订单追踪和 Shop 应用体验，还探索智能体电商。
- 🤝 Shopify 是最早大规模采用 Tailwind 的公司之一，不仅自用，也为客户押注该技术；Tailwind 是其关键基础设施。
- 💡 作者个人认同 Shopify 支持创业者的使命，认为创业改变了自己的人生。
- 🔓 Tailwind CSS 及其他开源项目一切不变，继续采用 MIT 许可证，团队将在 Shopify 支持下领导并维护。
- 💼 商业方面不再围绕 Tailwind 扩张业务；现有 Tailwind Plus 和 ui.sh 客户保留访问权，但关闭新客户注册，以聚焦 Shopify 内的 Tailwind CSS。
- 🙏 感谢过去九年所有使用和支持 Tailwind 的人，作者相信 Shopify 是继续这项工作的最佳归宿。

---

### [](https://www.aikido.dev/blog/teampcp-arrested-supply-chain)

**原文标题**: [TeamPCP arrests don't fix the supply chain risk they exposed](https://www.aikido.dev/blog/teampcp-arrested-supply-chain)

2026 年 8 月 27 日，作者 Charlie Eriksen 在 Aikido 博客发文，对涉嫌 TeamPCP 的两名男子被捕表示宽慰，并反思供应链攻击、LLM 加速威胁，以及攻击者与机构之间日益扩大的响应时间差。

- 🚔 澳大利亚联邦警察、FBI 和西澳警方宣布逮捕两名 20 岁出头男子，指控其与 TeamPCP 有关。
- 🧬 作者澄清：TeamPCP 并非 2025 年夏最初 S1ngularity 和 Shai-Hulud 攻击的幕后黑手，而是克隆了蠕虫；原始攻击者仍未知。
- ⚠️ TeamPCP 攻击造成重大伤害；即使长期可能让生态更强，也不能把攻击本身视为好事。
- 😟 作者在 2026 年 3 月 21 日调查攻击时被该组织注意到；被犯罪团伙关注不是荣耀，而是危险、不可预测且令人不安。
- 🎭 TeamPCP 难以归类：不像国家行为体、不完全是有组织犯罪、也不纯属意识形态，混合了金钱、政治、破坏、自负和博眼球。
- 🧠 他们并不特别高端，危险在于能快速把公开漏洞、技术、研究和恶意软件想法武器化；LLM 帮助缩小了“看到技术”到“规模化部署”的差距。
- 🏛️ 技术防御能控制事件，但问责需要机构；作者赞赏澳大利亚当局等机构艰难、隐蔽却关键的工作。
- ⏳ 攻击者与机构时间线严重不对称：攻击者可在数小时或数天内发起行动，机构取证、跨境协调并形成持久结果却需数月或数年；LLM 可能加剧这一问题。
- 🌐 TeamPCP 不会是最后一个；门槛降低、工具变强，小团队能力快速提升，条件正在恶化，能力与响应之间的差距可能继续扩大。
- 😴 对作者而言，今天是一个章节的结束；TeamPCP 消耗了大量睡眠、周末和精力，但未来仍会有新事件、新组织和长夜，只希望不是这个周末。

---

### [](https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared)

**原文标题**: [A Mini Shai-Hulud Has Appeared: Obfuscated Bun Runtime Payloads Hit SAP-Related npm Packages - StepSecurity](https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared)

StepSecurity 于 2026 年 4 月 29 日披露新一轮 Shai-Hulud npm 供应链攻击：攻击者通过 preinstall 钩子下载 Bun 运行时并执行 11.6 MB 混淆载荷，至少污染 mbt 与 @cap-js 等 SAP 生态包；载荷会窃取云、npm、GitHub、SSH 等凭据，借助窃取的 npm token 和 IDE 钩子自我传播，并把加密数据外泄到受害者 GitHub 账号下以“A Mini Shai-Hulud has Appeared”为描述的公开仓库。

- 🚨 StepSecurity 在首次恶意发布后数分钟内检测到攻击，并已通过 GitHub issue 与通知 SAP 安全团队进行负责任披露。
- 🌊 这是 Shai-Hulud 第三波，前两波分别为 2025 年 9 月和 2025 年 11 月；新变种新增 AI 编码代理钩子持久化、俄语区豁免和加密外泄。
- 📦 确认受影响的四个包：mbt@1.2.48、@cap-js/sqlite@2.2.2、@cap-js/postgres@2.2.2、@cap-js/db-service@2.10.1。
- 🧬 四个包都包含相同 preinstall 钩子“node setup.mjs”；setup.mjs 的 SHA-256 完全一致，是蠕虫自动化传播的确凿指纹。
- 🐇 setup.mjs 下载 Bun v1.3.13 到临时目录，并用 Bun 执行 11.6 MB 的 execution.js；执行后删除 Bun 以规避监控和取证。
- 🕵️ 使用 Bun 是为绕过 EDR/npm 审计对 npm install 期间 node 子进程的监控；载荷还检测 Alpine/musl，表明针对 CI 容器。
- 🔐 execution.js 为单行 11.6 MB，采用 obfuscator.io 字符串表轮转和自定义 ctf-scramble-v2 加密，含 48,370 个字符串表项。
- 🧮 载荷嵌入 RSA-4096 公钥；外泄数据先用 gzip 压缩，再用 AES-256-GCM 加密，AES 密钥用 RSA-OAEP 包裹，防守方只能看到密文。
- 🧠 在 GitHub Actions Linux runner 上，载荷通过 Python 子进程扫描 /proc 并读取 Runner.Worker 内存，绕过 secret masking 提取明文 secrets。
- ☁️ 五个并行收集器窃取 npm token、AWS Secrets Manager、GCP Secret Manager、Azure 凭据、GitHub PAT/OAuth 等。
- 📂 文件收集覆盖 SSH 密钥、云凭据、Kubernetes/Docker、加密钱包、VPN、Signal/Slack/Telegram 等消息应用、.npmrc、.git-credentials、AI 工具配置和 .env 文件等 134 类路径。
- 🪱 蠕虫机制：验证窃取的 npm token 是否具备 org write 权限，枚举可写包，并绕过 npm CLI 直接向 registry 发送 PUT 发布感染版本。
- 🧩 mbt 的入侵路径：攻击者获得 cloudmtabot 服务账号的静态 npm automation token，发布 mbt@1.2.48；该包从未使用 OIDC trusted publishing。
- 🧩 @cap-js 的入侵路径：攻击者控制 SAP 开发者 GitHub 账号，向 update/releases 分支推送修改 release-please.yml，滥用 OIDC trusted publishing 将 npm token 双 base64 编码输出到 workflow 日志。
- 🧹 后续提交注入 IDE 持久化文件并清理 OIDC 交换代码；workflow 被取消、分支被回滚，但恶意包已进入 npm registry。
- 🧷 新持久化向量：向仓库注入 .vscode/tasks.json，设置 "runOn": "folderOpen"，打开项目即运行 node .claude/setup.mjs。
- 🧷 同时注入 .claude/settings.json，滥用 Claude Code 的 SessionStart 钩子，在每个 Claude Code 会话开始时静默执行 node .vscode/setup.mjs。
- 📁 还复制 .claude/execution.js、.claude/setup.mjs、.vscode/setup.mjs，使感染在克隆/打开仓库的开发者机器上自我复制。
- 🕶️ 持久化提交伪装成 claude <claude@users.noreply.github.com>，提交信息为 "chore: update dependencies"。
- 🇷🇺 若系统 locale 为 ru，载荷记录 "Exiting as russian language detected!" 并干净退出，符合俄罗斯/CIS 行为者常用的 CIS 豁免模式。
- 🏭 载荷检测 32 个 CI/CD 平台；在开发机后台 daemonize 静默运行，在 CI 中内联运行以免任务结束被杀。
- 🛰️ 外泄通过 api.github.com 提交到受害者自己账号下的公开 GitHub 仓库，描述硬编码为 "A Mini Shai-Hulud has Appeared"；公开搜索已可见受害仓库。
- 🏷️ 仓库名使用 Dune 主题：16 个形容词 × 16 个名词 × 0-999 数字，如 sardaukar-sietch-247，可用正则识别。
- ⚙️ 若 GitHub token 有 workflow 权限，载荷注入 .github/workflows/format-check.yml，把 toJSON(secrets) 写入 artifact 窃取仓库 secrets。
- 🪄 注入分支名为 dependabout/github_actions/format/setup-formatter，仿冒 Dependabot；提交者伪装为 dependabot[bot]@users.noreply.github.com，提交信息为 "Add formatter workflow"。
- 🧪 Harden-Runner 审计模式捕获执行链：node setup.mjs → 下载 Bun → bun execution.js → Python 读 Runner.Worker 内存，并将内存访问标记为可疑进程事件。
- 🧾 关键 IOC 包括 setup.mjs SHA-256 4066781f...、execution.js SHA-256 80a3d287...（mbt）和 6f933d00...（@cap-js/sqlite）、Bun 1.3.13、ctf-scramble-v2、描述字符串和 Dune 仓库名模式。
- 🛡️ 检查是否受影响：npm list 四个包对应版本，检查 node_modules/*/setup.mjs，搜索 .vscode/tasks.json、.claude/settings.json、.claude/execution.js 和 dependabout 分支。
- 🧹 恢复步骤：卸载恶意版本并降级到 mbt@1.2.47、@cap-js/sqlite@2.2.1、@cap-js/postgres@2.2.1、@cap-js/db-service@2.10.0，使用 --ignore-scripts。
- 🔁 必须轮换所有可能泄露的凭据：GitHub、npm、AWS、GCP、Azure、SSH、Kubernetes、CI/CD secrets 及各类 Secrets Manager 中的密钥。
- 🗑️ 删除 IDE 持久化文件、注入的 dependabout 分支和恶意 workflow，删除未授权 GitHub 仓库，审计并 unpublish 异常 npm 版本。
- 📌 固定精确依赖版本，避免自动升级到恶意 patch 版本。
- 🏢 StepSecurity 企业功能包括 Threat Center 告警、Harden-Runner 拦截 Runner.Worker 内存 dump、Dev Machine Guard、npm 冷却检查、受污染更新检查和 AI Package Analyst 分钟级发现。

---

### [怎样才能真正改变 JavaScript？ - YouTube](https://www.youtube.com/watch?v=OkuNJo9tTtg)

**原文标题**: [How can someone actually change JavaScript? - YouTube](https://www.youtube.com/watch?v=OkuNJo9tTtg)

這是 YouTube 網站頁尾的連結與版權資訊，主要列出平台相關資源、政策規範、聯絡與開發者入口，以及 Google LLC 的版權標示。

- 🏢 簡介與新聞中心：提供 YouTube 的基本介紹與官方最新消息。
- ⚖️ 版權、條款、私隱、政策及安全：涵蓋法律規範、使用者條款、隱私與平台安全政策。
- 📞 聯絡我們：提供與 YouTube 聯繫的管道。
- 🎬 創作者、刊登廣告、開發人員：分別面向內容創作者、廣告主與開發者的資源入口。
- ⚙️ YouTube 的運作方式與測試新功能：說明平台運作機制及新功能測試相關資訊。
- ©️ 2026 Google LLC：標示版權所有與年份。

---

