# [Issue #649: node:sqlite marked stable — Node Weekly](https://nodeweekly.com/issues/649)

### [你的工具正在向你隐瞒 npm Audits—zachleat.com](https://www.zachleat.com/web/npm-audit-report/)

Zach Leatherman 指出，`npm audit` 的结果可能被框架和脚手架隐藏：全新 Gatsby 项目报告 78 个漏洞，而全新 Next.js 项目显示 0 个漏洞，但这并不代表 Next.js 更安全，因为它把自身依赖打包进 `dist/compiled`，绕开了对 `node_modules` 的常规审计；文章还梳理了 `create-*` CLI 与包管理器隐藏审计输出的做法，并发布 Prototype Pollution Report 进行跨生态对比。

- 🛡️ **审计假象**：同一天用默认选项分别执行 `create-gatsby` 和 `create-next-app`，Gatsby 项目报告 78 个漏洞（7 low、23 moderate、46 high、2 critical），Next.js 项目报告 0 个；但 Gatsby 已不再维护，0 漏洞并不等于更安全。
- 🧩 **依赖打包**：`next` v16.4.6 为其自身依赖绕过 `node_modules`，`node_modules/next/dist/compiled` 中有 139 个独立依赖，审计可发现 11 low、2 moderate、19 high、3 critical，但这些漏洞不会被标准 `npm audit` 报告。
- ⚠️ **Vite 类似做法**：Vite 在 `node_modules/vite/dist` 中也有打包依赖的做法，不过它属于本地开发工具，且维护者保持打包依赖更新的记录很好；文章仍认为完全让依赖退出审计有些过度。
- 🛠️ **CLI 隐藏输出**：`create-gatsby` 使用 `npm install --no-audit`；`create-astro`、TanStack CLI、`create-preact` 不显示控制台输出；`create-nuxt` 和 `ng new` 仅在安装失败时打印；`sv create` 短暂显示后清空日志；独立运行 `npm audit` 仍能看到项目依赖，但透明度不足。
- 📦 **包管理器差异**：`npm` 会在 `npm install` 后显示审计报告，而 `pnpm` 和 `yarn` 不会，这也会影响开发者对安装阶段漏洞的可见性。
- 📊 **跨生态报告**：Prototype Pollution Report 约每天更新，用统一口径比较不同框架生态；Ecosystem Scoreboard 统计各项目发布的全部非弃用包，并要求维护者弃用不再维护的包，Core-only Scoreboard 只统计核心包，文末附完整包列表和审计计数。

### [原型污染报告](https://ppr.zachleat.dev/)

总结失败：模型未返回符合格式的摘要。

### [ClickHouse 托管 Postgres | ClickHouse](https://clickhouse.com/campaigns/clickhouse-managed-postgres?utm_source=nodeweekly&utm_medium=sponsored-content&utm_campaign=2026-11-26_Primary_Clickhouse)

ClickHouse 推出 ClickHouse Managed Postgres，以运行在本地 NVMe 上的企业级 Postgres 承载事务负载，并通过 ClickPipes Postgres CDC、`pg_clickhouse` 与 ClickHouse 分析能力组成统一数据栈；该服务已在 AWS 正式可用，在 GCP 处于 Private Preview，目标是用更少运维复杂度支撑实时和 AI 驱动应用。

- 🚀 **正式可用**：ClickHouse Managed Postgres 已在 AWS 正式可用（GA），在 GCP 处于 Private Preview；面向实时和 AI 驱动应用提供事务与分析统一的数据栈，并附 30 天试用和 $300 credits。
- ⚡ **NVMe 性能**：Postgres 运行于本地 NVMe 存储，提供微秒级延迟和数百万 IOPS，I/O 密集负载最高快 10×，且不受 EBS 限流或网络抖动影响；同时改善 `VACUUM`、checkpoint 和逻辑复制等操作。
- 🛡️ **企业级能力**：内置高可用，最多两个专用 standby 仅用于 HA，读副本单独提供；支持自动备份、基于 WAL 归档的 PITR、端到端加密、私有网络，基础设施由 Ubicloud 支撑。
- 🔄 **实时 CDC**：通过 ClickPipes Postgres CDC connector 将 Postgres 数据实时复制到 ClickHouse，复制延迟低至数秒，分析最高快 100×；支持初始快照和 CDC 增量更新，已在数百家企业、每月数百 TB 的生产场景验证。
- 🔗 **统一查询层**：使用 `pg_clickhouse` 扩展从 Postgres 直接查询 ClickHouse，无需代理或额外查询层；查询透明下推并支持 joins、filters、aggregations、functions，22 条 TPC-H 查询中 14 条完全下推，带来 60×+ 加速，后续将扩展到 CTE 和窗口函数。
- 🧩 **开源栈**：技术栈由 Postgres 事务、ClickHouse 分析、PeerDB CDC 和 `pg_clickhouse` 统一查询层组成，强调无 vendor lock-in、数据可控。
- 🏢 **客户验证**：客户已从 Aurora/RDS 迁移多个多 TB 工作负载，其中有约 8.5 TB 热数据运行在 Postgres，并获得 NVMe 低延迟；客户反馈集中在性能、可靠性、性价比及部署支持。
- 🔮 **后续路线**：后续将增加更多原生 CDC 能力，包括亚秒级复制延迟、通过持续事务复制实现可靠 slot flushing 等，这些增强仅面向 ClickHouse Managed Postgres。

### [sqlite：由 christianaurichzm 标记为稳定 · Pull Request #67654 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67654)

Node.js 的 PR #67654（sqlite: mark as stable）已合入 commit d3fdcc6，将内置 node:sqlite 模块从 release candidate 标记为 stable；该模块自 v25.7.0 和 v24.15.0 起处于 RC，稳定后应用可直接使用 SQLite 数据库而无需安装原生 addon，这一变化也出现在 27.0.0-alpha.0.2.0 的发布说明中。

- 🚀 **正式稳定**：Node.js 内置 `node:sqlite` 从 release candidate 转为 stable，结束自 v25.7.0 和 v24.15.0 起的 RC 状态；应用可直接操作 SQLite 数据库，无需安装原生 addon。
- 🧩 **改动范围**：经评审，PR 收敛为文档层面的稳定标记，没有在该 PR 中新增 `--no-sqlite` 或移除 `--no-experimental-sqlite`；作者确认相关 CLI 变更另开 semver-major PR。
- ⚠️ **兼容性限制**：将 `--experimental-sqlite` 变为 no-op、移除 `--no-experimental-sqlite` 属于 semver-major，因此不随本次稳定化一起合入；文章提到后续 PR #67698 处理移除 `--no-experimental-sqlite`。
- 📈 **版本落地**：该变更被列入 2026-11-25/26 的 `27.0.0-alpha.0.2.0` 发布说明，和后续 SQLite semver-minor 变更（无 SQLite 支持时抛 `ERR_NO_SQLITE`、`statement.columnCount` getter）一同出现。

### [SQLite | Node.js v27.0.0 文档](https://nodejs.org/download/release/v27.0.0-alpha.0.2.0/docs/api/sqlite.html)

Node.js v27.0.0 文档显示内置 `node:sqlite` 已标记为 Stable，结束此前的实验与候选状态：模块以同步 API 提供 SQLite 连接、预编译语句、参数绑定、会话变更集、备份和虚拟表等能力，并通过默认防御性设置、扩展加载开关和资源限制强化安全边界。

- 🚀 **稳定发布**：Node.js v27.0.0 文档将 `node:sqlite` 标记为 Stable，此前它从 v22.5.0 引入，v23.4.0/v22.13.0 不再需要 `--experimental-sqlite` 但仍属实验，v25.7.0/v24.15.0 进入候选；模块仅通过 `node:` 方案访问，SQL 跟踪事件走 `diagnostics_channel` 的 `'sqlite.db.query'`。
- 🧩 **同步连接与语句**：`Database` 表示单个 SQLite 连接且 API 全同步，支持 `exec()` 执行 SQL、`prepare()` 创建预编译语句；`Statement` 的 `all/get/iterate/run` 通过绑定参数执行并返回行或变更摘要，预编译参数化可降低 SQL 注入风险；`DatabaseSync` 和 `StatementSync` 是兼容旧名的已弃用别名。
- 🔄 **类型转换**：JavaScript `number` 始终写入为 REAL，`bigint` 才写入 INTEGER；布尔值写为 1/0，`undefined` 写为 NULL，BLOB 使用 TypedArray/DataView/ArrayBuffer/SharedArrayBuffer；读取 INTEGER 默认转 number，可用 `readBigInts` 改读 bigint，超出安全整数范围且未开启 BigInt 会抛 `ERR_OUT_OF_RANGE`，bigint 超出有符号 64 位会抛 `ERR_INVALID_ARG_VALUE`。
- 🛡️ **安全默认值**：安全默认值包括 `defensive` 默认 true 以禁用可故意损坏数据库文件的 SQL 特性、`enableForeignKeyConstraints` 默认 true、`allowExtension` 默认 false 且构造后不能从 false 改为允许；`setAuthorizer()` 可返回 `SQLITE_OK`、`SQLITE_DENY` 或 `SQLITE_IGNORE` 实施访问控制，回调中禁止重入同一连接；启用 Permission Model 时不支持 URL 或 `file:` URI 路径。
- ⚡ **标签缓存**：`createTagStore([maxSize])` 创建默认最多 1000 条预编译语句的 LRU 缓存，`sqlTagStore.get/run/all/iterate` 以模板标签形式执行；`${value}` 会作为参数绑定而非字符串插值，缓存按 SQL 字符串及占位符位置精确匹配且区分大小写。
- 📦 **序列化与备份**：`serialize()` 将数据库导出为 `Uint8Array`，`deserialize(buffer[, options])` 可替换当前数据库且会先终结已有预编译语句；`sqlite.backup(sourceDb, path[, options])` 返回 Promise，支持 `source`、`target`、`rate` 和 `progress`，同一连接的新变更会立即反映到备份，其他连接的变更会使备份重启。
- 🧪 **虚拟表**：`createModule(name, options)` 注册虚拟表模块，`columns` 支持 `INTEGER`、`TEXT`、`REAL`、`BLOB`、`ANY`，`hidden` 列可作为表值函数参数，`rows` 返回可迭代的列值数组；模块可作为同名表直接查询或用 `CREATE VIRTUAL TABLE ... USING` 建表，虚拟表不应用列亲和性，需 INTEGER 时应返回 bigint。
- 🔗 **变更集**：`createSession([options])` 可跟踪全部表或指定 `table`/`db` 的变更，`session.changeset()` 和 `patchset()` 生成可应用到其他数据库的 `Uint8Array`；`applyChangeset()` 支持 `filter` 和 `onConflict`，冲突处理可返回 `SQLITE_CHANGESET_OMIT`、`REPLACE` 或 `ABORT`，异常或未知返回值会中止并回滚。
- 📊 **限制与统计**：`database.limits` 可运行时读写 `length`、`sqlLength`、`column`、`exprDepth`、`vdbeOp`、`functionArg` 等限制，设为 `Infinity` 恢复编译期最大值；`statement.stat(counter)` 读取 `fullscanStep`、`sort`、`vmStep`、`run`、`memused` 等计数器，`filterMiss`/`filterHit` 需 SQLite 3.38.0 或更新版本。

### [Node.js — Node.js 27.0.0-alpha.0.2.0（Alpha 版）](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.2.0)

Node.js 27.0.0-alpha.0.2.0（Alpha，2026-11-26）发布，带来下一主版本的早期 API 与内部改动：node:sqlite 转为稳定并补齐错误处理与元数据能力，多个 http2 兼容层 API 进入 SEMVER-MINOR，--process-timeout 从实验选项毕业，同时文档弃用 util.TextDecoder/util.TextEncoder、弃用 TLS 重协商并新增 allowRenegotiation 显式选择加入，另更新 V8、npm、undici 等依赖并修复 stream、fs、http、quic 等问题。

- 🚀 **Alpha 发布**：Node.js 27.0.0-alpha.0.2.0 于 2026-11-26 发布，提供 Windows、macOS、Linux、AIX 等平台二进制与源码；macOS Intel 二进制仍显示 Coming soon。
- 🧩 **SQLite 稳定化**：node:sqlite 标记为 stable，新增 statement.columnCount getter；在没有 SQLite 支持时抛出 ERR_NO_SQLITE，并在 Database 中执行权限模型，修复语句 finalize/reset、查询 trace 等边界问题。
- 🧩 **http2 兼容 API**：http2 兼容响应新增 writeProcessing()，补齐 setHeaders()，信息性头方法支持 callback，均标记为 SEMVER-MINOR。
- ⚙️ **process-timeout 毕业**：lib 的 --process-timeout 选项从实验毕业为正式选项，src 侧输出扩展到 workers。
- ⚠️ **TextEncoder 弃用**：文档弃用 util.TextDecoder 和 util.TextEncoder，改用全局 TextDecoder/TextEncoder，相关文档和测试同步替换。
- 🛡️ **TLS 重协商**：文档弃用 TLS 重协商，新增 allowRenegotiation 作为显式 opt-in；同时修复 session 解析、OpenSSL 压缩泄漏及致命错误后 socket 销毁等问题。
- 🔍 **文件描述符探测**：os 模块新增 guessFileDescriptorType，用于猜测文件描述符类型，标记为 SEMVER-MINOR。
- 📦 **依赖更新**：依赖更新包括 V8 15.6.75.60、npm 12.2.3、undici 8.13.1、zstd 1.6.0、zlib 1.4-401d185、simdjson 5.2.0、libffi 3.8.1、ada 4.1.1 等。
- 🔑 **SLH-DSA 接入**：crypto 通过 BoringSSL 接入 SLH-DSA，并为 TLS ticket key 回调增加 TicketHmacCtx 别名；WebCrypto 的 SPKI/PKCS#8 导出和非对称密钥导入逻辑被复用。
- 🔄 **stream/iter 优化**：大规模重构 stream/iter：减少 async generator 和每次读取的 Promise，使用 RingBuffer、索引写入及复用等待列表优化 from()/share()/broadcast()/merge()/pipeTo() 等热路径。
- 🐛 **关键修复**：修复 fs recursive mkdir() 返回 EROFS、cpSync() 在 dereference 时跨符号链接 stat 源、ReadStream 对 highWaterMark 的处理；http 不再复用过期空闲 socket，并 forward-port CVE-2026-105481 的 pending-read 修复；quic 修复流 FIN 丢失和每会话 SSL 泄漏。

### [AWS Lambda 新增对 Node.js 26 的支持 - AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-nodejs-26/)

AWS Lambda 于 2026 年 11 月 20 日新增 Node.js 26 支持，覆盖 Lambda Web Functions 和 Lambda Event Functions，开发者可将该长期支持版本用作托管运行时，也可用作基础容器镜像（仅限 Event Functions）。Node.js 26 是 Node.js 最新的 LTS 版本，预计安全与缺陷修复支持持续至 2029 年 4 月；AWS 会自动为托管运行时和基础镜像应用后续更新。

- 🚀 **运行时上线**：Lambda 现已支持用 Node.js 26 创建无服务器应用，Web Functions 与 Event Functions 均可使用，该运行时在两者可用的所有区域提供。
- 📦 **两种使用形态**：Node.js 26 可作为托管运行时使用，也可作为基础容器镜像使用，但基础镜像方式仅支持 Event Functions；AWS 会在更新可用时自动应用到托管运行时和基础镜像。
- 🗓️ **LTS 支持周期**：Node.js 26 是 Node.js 最新的长期支持版本，预计安全与缺陷修复支持至 2029 年 4 月。
- 🧩 **可用新特性**：在 Lambda 中可使用 Node.js 26 的新能力，例如便于处理日期、时间和时区的 Temporal API，以及 Fetch API 的增强。
- 🛠️ **工具链兼容**：可配合 Powertools for AWS Lambda (TypeScript) 实践无服务器最佳实践，并可通过 Lambda 控制台、AWS CLI、AWS SAM、AWS CDK 和 AWS CloudFormation 部署与管理应用。

### [Fastify 插件：中间件绕过、请求走私与伪造上传 | Corgea](https://corgea.com/research/cve-2026-133120-133250-133212-124289-fastify-express-middie-reply-from-november-2026)

2026 年 11 月 16 日至 20 日，Fastify 项目在八个插件中发布 26 个安全公告，其中 6 个为严重级别；问题集中在 Express/middie 中间件与 Fastify 路由器对路径解析不一致导致认证中间件被跳过、reply-from 在核心 http 传输上可请求走私，以及 multipart 将 JSON 对象伪造成上传文件，另有 WebSocket、busboy、static 和 proxy-addr 的崩溃、目录列表、路径校验与 IP 欺骗修复。现有信息称尚无公开利用或在野利用报告，多数公告附带触发请求；受影响用户应升级到固定版本，并把路径作用域认证迁到基于 request.routeOptions.url 的 preHandler。

- 🛡️ **风险总览**：公告由 OpenJS Foundation CNA 分配 CVE，6 个严重；受影响包包括 @fastify/express、@fastify/middie、@fastify/reply-from、@fastify/multipart、@fastify/http-proxy、@fastify/busboy、@fastify/static、@fastify/proxy-addr。部分包周下载量很高，且多数公告给出可触发请求，但未见公开利用代码或在野使用。
- 🚀 **固定版本**：升级到 @fastify/express 4.0.10、@fastify/middie 9.3.8、@fastify/reply-from 12.9.1、@fastify/http-proxy 11.6.10、@fastify/multipart 10.1.9、@fastify/static 10.1.12；@fastify/busboy 升到 3.2.6，@fastify/proxy-addr 升到 5.1.3。@fastify/busboy 和 @fastify/proxy-addr 常为传递依赖，caret 范围下刷新 lockfile 可能足够。
- 🧩 **中间件绕过**：@fastify/express 和 @fastify/middie 先由 Fastify 的 find-my-way 选处理器，再由插件用 Express 或 path-to-regexp 判断 app.use() 挂载是否命中；两者对同一请求路径读出不同结果时，处理器执行而认证中间件被跳过。@fastify/express 5 个公告中 4 个 CVSS 9.1，@fastify/middie 的 CVE-2026-133250 也是 CVSS 9.1。
- 🧩 **路径解析差异**：关键向量包括 GET *admin 被 find-my-way 路由为 /admin 但 Express/middie 不匹配；/tenant/x%5C%20/admin 因 url.parse 把反斜杠改为斜杠而错位；%25 被二次解码；/tenant//admin 和 /tenant/ 的空 :id 或 * 参数不匹配；前缀字符串拼接导致正常流量绕过；caseSensitive:false 下 Kelvin 符号 /api/%E2%84%AAeys 命中 /api/keys 但跳过中间件。修复分别调整 URL 构造、编码保留与 fallback 字符重编码。
- 🧩 **请求走私**：@fastify/reply-from 12.9.1 修复 CVE-2026-133212（CVSS 9.0）：在核心 Node.js http 传输（undici:false、http 选项或 5.0.0 前默认）下，GET/HEAD/TRACE 或假值 JSON body 未发送 body 却转发客户端 Content-Length；上游把同一 keep-alive 套接字上的下一个请求当作缺失 body，从而执行越过代理路由和认证的请求。修复改为 body !== undefined 并转发假值 JSON，同时在无 body 时把 Content-Length 置 0。
- 🔄 **路径穿越**：@fastify/reply-from 12.8.4 修复 buildURL() 路径穿越：http:%2e%2e%2fsecret.txt 的段先读成 http:.. 而 WHATWG URL 解析器丢掉 scheme 后转发编码点段；..; 或 ..;jsessionid=x 在 Tomcat、Jetty、WildFly、Spring Boot 中会被解析为 ..（CVE-2026-130886、CVE-2026-127064）。@fastify/http-proxy 11.6.10 另修 WebSocket 路径上的同一 ..; 问题（CVE-2026-127060）。
- 🧩 **伪造上传**：在 @fastify/multipart <10.1.9 且 attachFieldsToBody 为 true 或 keyValues 时，saveRequestFiles() 会把带真值 file 和 _buf 属性的任意对象当上传；JSON body 如包含 filename ../../../../package.json 可伪造文件，绕过 onFile、files 和 fileSize 限制（CVE-2026-124289）。临时路径本身安全，但应用若把 file.filename 当目标路径会受影响。10.1.9 用模块私有 Symbol 标记合法文件包装器，并只在 isMultipart() 为真时处理。
- 🐛 **WebSocket 崩溃**：@fastify/http-proxy 11.6.10 修复 websocket:true 下三条升级路径缺少 error 监听导致进程崩溃：异步路由期间 TCP reset（CVE-2026-129500）、带 #fragment 的升级在 upstream 失败前返回 101（CVE-2026-129502）、升级请求流水线化（CVE-2026-130647）；第一和第三仅影响明文 HTTP/1 监听器，TLS 套接字保留自身监听器。插件还在转发 cookie 时丢弃 Origin，破坏 gorilla/websocket CheckOrigin 等上游检查（CVE-2026-133111）。
- 🐛 **解析器缺陷**：@fastify/busboy 3.2.6 修复：请求达到 parts 上限（默认 1000）后中途结束会因被跳过 part 无 error 监听而崩溃（CVE-2026-124724）；约 106 字节且头部未终止的 part 可永久挂起解析器（CVE-2026-128835）；畸形 %G 转义可跳过 URL 编码字段大小检查（CVE-2026-128842）；80 KiB headerSize 边界处拆分头部终止符可把文件变成字段（CVE-2026-128846）。
- 🛡️ **静态与代理**：@fastify/static 10.1.12 修复 dotfiles:'deny' 且 list 启用时 /.git/ 返回目录列表，文件内容仍受保护（CVE-2026-130811）；allowedPath 在 index 和扩展名解析前检查，/private/ 可提供被拒绝的 /private/index.html（CVE-2026-115515，10.1.8 已修）。@fastify/proxy-addr 5.1.3 修复 trustProxy 对带 zone 的 IPv6 链路本地地址 fe80::1%proxy0 忽略 zone，导致另一接口同地址被信任并采信 X-Forwarded-For（CVE-2026-121192）。
- 🔍 **排查与缓解**：用 npm ls 检查八个包；直接升级到上述固定版本，传递依赖刷新 lockfile。若无法立即升级，把认证/授权移到 Fastify preHandler 并依据 request.routeOptions.url 判断；在 @fastify/express 前注册 onRequest 拒绝非 / 开头目标和含反斜杠路径；reply-from 用默认 undici 并拒绝带 body 的 GET/HEAD/TRACE；saveRequestFiles 前检查 isMultipart()，对 file.filename 使用 path.basename() 或白名单。
- ⚠️ **检测特征**：访问日志或 WAF 可关注：除 OPTIONS * 外不以 / 开头的请求目标如 GET *admin；含 %5C、%2525、%E2%84%AA（Kelvin 符号）或受保护路由前空段的路径；..; 或 %2e%2e; 段及 http:/https: 后接编码点段的代理请求；带非零 Content-Length 的 GET/HEAD/TRACE；发往 multipart 上传端点的 application/json 且 body 含 file 与 _buf 键。

### [perf\_hooks：由 jsumners-nr 添加 node:perf\_hooks/pprof 时间分析器 · 拉取请求 #67779 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67779)

Node.js 仓库的 PR #67779 提议新增实验性 `node:perf_hooks/pprof` 模块，将当前线程的 wall time 采样编码为 pprof 格式，目标是让 pprof 命令行和持续剖析服务无需原生 addon 即可使用；实现移植自 `@datadog/pprof`，原生部分基于 Node.js 内部接口重写，当前仅覆盖 wall time，heap、上下文标签和 source map 留待后续，PR 仍处于 Open 状态并收到 reviewer 对设计方向的质疑。

- 🚀 **实验模块**：PR #67779 为 Node.js 增加 `node:perf_hooks/pprof`，加载时发出 `ExperimentalWarning`，无需启动 flag；它采集当前线程的 wall time 剖析并编码为 pprof，当前仍是 Open PR，尚未合并。
- 🧩 **原生移植**：wall time profiler 从 `@datadog/pprof`（Apache-2.0）移植，原生代码位于 `src/node_pprof.cc` 和 `src/pprof/`，改用 Node.js 内部接口而不是 nan/node-gyp；上游约 2639 行、移植约 1660 行，按去重行统计约 10% 与上游逐字重合。
- 🛠️ **API 与选项**：提供 `time.start([options])`、`time.stop([restart])`、`time.isStarted()`、`time.profile([options])`、`time.v8ProfilerStuckEventLoopDetected()` 和 `time.constants`；`time.profile()` 按 `durationMillis` 采样并支持 `AbortSignal` 提前停止，若其启动的 profiler 在计时结束前被停止会以 `ERR_INVALID_STATE` 拒绝，`encode()`/`encodeSync()` 返回 gzip 压缩的 pprof `Buffer`。
- ⚙️ **兼容选项**：保留 `@datadog/pprof` 的 `intervalMicros`、`durationMillis`、`lineNumbers`、`collectCpuTime`、`workaroundV8Bug` 选项，方便迁移；POSIX 上 `collectCpuTime` 通过拦截 V8 sampler 的 `SIGPROF` 把线程 CPU 时间归因到样本，也用于绕过 V8 重启后可能卡住的 bug，该 CPU 时间归因不支持 Windows，也不能与 `lineNumbers` 同用。
- 🧠 **V8 协作**：profiler 拥有自己的 `v8::CpuProfiler`，可与 `v8.startCpuProfile()` 和 inspector 的 `Profiler` 域并行；启动快照构建期间拒绝启动。
- ⚠️ **功能边界**：首版不包含 heap profiler、sampling contexts/labels 和 source map 支持；这些能力留待后续 PR，也决定现有生态用户能否完全移除原生 addon。
- 📊 **生态背景**：PR 引用数据称 `@datadog/pprof` 每周约 1760 万次下载，其中 `dd-trace` 约 1520 万；Grafana Pyroscope、Polar Signals、Coralogix 等也依赖它，且不少包固定旧版本，导致修复和新 Node.js 版本支持分发不均。
- 🔍 **审查争议**：reviewer legendecas 认为 pprof 是格式而非 profiler，Node 内置支持应优先把现有 V8 CPU profile 转成 pprof，不必新增 CPU profiler API；还质疑 `workaroundV8Bug` 不应暴露为公共选项，并指出 V8 15.9 起每次 `SIGPROF` 都必须调用 V8，核心不应绕过。
- 🧪 **测试覆盖**：测试覆盖模块警告和选项校验、profile 内容与 CPU 时间/行号/重启、卡住 profiler 恢复、编码与合成 profile 归一化、worker（含采样中被终止）、与 `v8.startCpuProfile()`/inspector 并行、未停止即退出和快照期间拒绝；`cctest` 覆盖样本归因、线程 CPU 时钟和信号链，Codecov 显示补丁覆盖率 96.72%。

### [GitHub - DataDog/pprof-nodejs：为 Node.js 提供 pprof 支持 · GitHub](https://github.com/DataDog/pprof-nodejs)

DataDog 的 `pprof-nodejs` 为 Node.js 提供 pprof 性能分析支持：通过原生组件调用 V8 的 CPU 与堆分析器采集 profile，要求 Node.js 18 及以上，并为 Linux arm64/x64、Alpine Linux x64、macOS arm64/x64、Windows x64 的 Node 18/20/22/24/25 提供预编译二进制，其他环境使用 `node-gyp` 构建；采集结果可用 `pprof` CLI 查看。

- 🚀 **平台与版本支持**：要求 Node.js 18+；预编译二进制覆盖 Linux arm64/x64、Alpine Linux x64、macOS arm64/x64、Windows x64，支持 Node 18/20/22/24/25；其他环境通过 `node-gyp` 构建，可能需要额外依赖。
- 📦 **安装与查看**：通过 `npm install --save @datadog/pprof` 安装；采集的 profile 可用 `pprof` CLI 查看，例如 `pprof -http=: wall.pb.gz`。
- 🧩 **墙钟时间采样**：调用 `pprof.time.profile({durationMillis:10000})` 采集指定时长的 wall time profile，再经 `pprof.encode` 保存为 `wall.pb.gz`。
- ⚙️ **命令行自动采集**：使用 `node --require @datadog/pprof app.js` 启动应用，会生成 `pprof-profile-${process.pid}.pb.gz` 的墙钟时间 profile，并可用 `pprof -http=:` 查看。
- 🧠 **堆采样机制**：启动时调用 `heap.start(intervalBytes, stackDepth)` 开启堆分析；示例中 `intervalBytes` 为 `512*1024`（平均采样间隔字节数），`stackDepth` 为 `64`（最大采样栈深度）。
- 📊 **堆 profile 格式**：`pprof.heap.profile()` 返回 `profile.proto` 格式，可编码保存为 `heap.pb.gz`；`pprof.heap.v8Profile()` 可采集 V8 allocation profile 格式。

### [依赖：由 nodejs-github-bot 将 ada 更新至 4.1.1 · 拉取请求 #67624 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67624)

Node.js 主分支通过自动化 PR `#67624` 将 URL 解析依赖 `ada` 升级至 `4.1.1`，并同步把 URL 的 WPT 更新到 `2fa965b55c`。此次更新关联 `ada-url/ada#1360` 对 `url_pattern` 结果输入中 use-after-free 的修复；PR 获得 5 个批准后于 2026 年 11 月 21 日合入，涉及 URL 与 `URLPattern` 相关实现及测试。

- 📦 **依赖升级**：`nodejs/node` 的 `ada` 依赖更新至 `4.1.1`，PR 为 `#67624`，目标分支为 `main`。
- 🛡️ **安全修复**：更新关联 `ada-url/ada#1360` 的修复，避免 `url_pattern` 结果输入中的 use-after-free，降低 `URLPattern` 相关路径的内存安全风险。
- 🧪 **WPT 同步**：第二个提交将 URL 的 Web Platform Tests 更新到 `2fa965b55c`，使测试基线跟随新的 URL 实现。
- 📊 **覆盖率验证**：Codecov 报告所有修改且可覆盖的行均被测试覆盖，项目覆盖率维持在 `90.72%`。
- ✅ **合入状态**：PR 获得 5 个批准，于 2026 年 11 月 21 日关闭并合入，落地提交范围为 `08eff13...07b0481`。

### [发布 v4.1.0 · ada-url/ada · GitHub](https://github.com/ada-url/ada/releases/tag/v4.1.0)

ada-url 发布 v4.1.0，核心是围绕 URL 解析、百分号编解码和 setter 路径做 NEON/AVX-512/SIMD 与减少分配的性能优化，同时集中修复 URLPattern/URLPatternList、IDNA、C API 和搜索参数迭代器的正确性与内存安全问题。该版本还更新了 ada-idna 到 v0.7.0 和 Web Platform Tests，对依赖标准 URL 行为的 C++/C 用户及使用 URLPattern 的调用方影响较大。

- 🚀 **正式发布**：ada-url 发布 v4.1.0，汇总大量性能改进、正确性修复和测试更新，面向使用其 C++ URL 解析库及 C API 的用户。
- ⚡ **SIMD 解析加速**：新增和调整多项 SIMD 快路径，包括 NEON 基于 SHRN 的零值测试、AVX-512VL 点分十进制 IPv4 解析、AVX-512 IPv6 主机解析、SIMD 扫描器与 nibble-table 分类，并加速规范 HTTP(S) URL 的 `can_parse` 和绝对 URL 快路径。
- 🔄 **编解码与 setter 优化**：`percent_decode` 使用批量 run-copying，`percent_encode` 使用针对字符集位图的 SIMD；同时跳过干净输入的 tab/换行清理和聚合器 setter 的字符串分配，`set_href` 改为移动解析结果，报告称 `url` 路径指令数降低约 6%。
- 🧩 **URLPatternList**：包含 `url_pattern_list` 编译式路由集匹配（URLPatternList）相关 RFC 变更，并修复路由数量上限、截断 trie 编码、可选前导斜杠匹配、空 `match` 空指针解引用、长字面量 `uint16` 截断和花括号前缀处理等问题。
- 🐛 **URLPattern 修复**：修复相对字符串无 base 时的 `test`/`exec` 匹配、特殊 scheme 的 pathname 规范化、结果输入字符串所有权、移动构造函数成员初始化，以及 `fast_test` 的 `noexcept` 阻止正则异常传播等问题。
- 🛡️ **安全与内存修复**：修复 C API `ada_strings_get` 索引边界检查、`ada_owned_string` 的 NUL 终止、搜索参数迭代器与 reset 的内存安全问题，处理 setter 输入与 URL 缓冲区别名、`max_input_length` 早返回绕过及 `set_host` IDNA 扩超长度等问题。
- 🌐 **URL 与 IDNA 正确性**：修复 `ada::url` 的 `host_end` 比文档位置少一字节、AVX-512 快路径 IPv4 组结构校验、file URL pattern 默认端口 0、AArch64 flush-to-zero 下 tab/换行处理、SSSE3 解析器仅在 CPU 支持时调度，并将 `ada-idna` 更新到 v0.7.0，按 Bidi 域对每个 label 应用 IDNA `CheckBidi`。
- 🧪 **测试与 CI**：多次更新 Web Platform Tests（url），补充 IPv6 主机解析器 `::` 语法边界和额外 setter 测试；CI 方面适配 Clang 22、修复 Ubuntu 26.04 的 clang-tidy 安装并稳定 CodSpeed 基准迭代。
- 📦 **依赖更新**：发布说明包含多项 Dependabot 更新，如 CodeQL Action、actions/checkout、setup-python、setup-node、ossf/scorecard-action 等；同时移除 OpenSSF Scorecard workflow 和徽章。

### [eve – 智能体框架 - Vercel](https://vercel.com/eve)

eve 以 1.5.0 版本开源（Apache-2.0），定位为面向可持久运行、长周期执行的生产级 AI Agent 框架：用 TypeScript 与 Markdown 文件定义 Agent，支持按会话动态解析、多租户、多通道接入，并整合 Vercel 的 Agent Runs 观测以及 AI Gateway、Sandbox、Drives、Workflows、Connect 等运行时基础设施，降低从模板到企业部署的集成成本。

- 🚀 **开源发布**：eve 1.5.0 以 Apache-2.0 许可开源，面向构建、治理和演进企业级 Agent；提供 `npx eve@latest init my-agent` 初始化命令，并给出 Company brain、Software factory、Agentic apps 三类可运行模板，官方称可在 60 秒内于 Vercel 部署首个 Agent。
- 🧩 **文件即 Agent**：Agent 被定义为由 TypeScript 和 Markdown 文件组成的目录，文件路径决定加载方式：`instructions.md` 即可构成完整 Agent，`skills/` 按需加载 Markdown 操作手册，`tools/` 中的 TS 文件名自动成为工具名，另有 `channels/`、`connections/`、`subagents/`、`schedules/`。
- 🔄 **动态与多租户**：通过 `defineDynamic`，指令、技能、工具、子 Agent、连接和模型都可按会话解析；示例中 Enterprise 客户获得一小时 SLA、更大模型、值班呼叫和二级支持，Hobby 客户仅指向文档与社区，从而以一次部署服务多租户。
- 🌐 **多通道覆盖**：通道是框架原语，同一 Agent 可接入 Slack、Teams、Discord、Web、iMessage、WhatsApp 等，支持多人及单人聊天；模板还覆盖 Web 聊天、语音和 iMessage，并为每个用户保留长期记忆。
- 🛠️ **持久化执行**：运行时支持持久化执行：每一步设置检查点，可承受崩溃、重启和长达数天的等待，支持 cron 调度、消息间暂停并在投递后恢复；任务可选择完全自主循环、确定性工作流，或在同一运行中混用两者。
- 📊 **Agent Runs 观测**：Vercel 的 Agent Runs 会自动展示每个 eve 会话的轮次、工具调用、推理、耗时和 token 用量，无需埋点；可通过 `vercel agent-runs` 或 Vercel MCP 中的 Agent Runs 工具查看，并按 Slack、HTTP 等触发方式统计运行和 token。
- ⚙️ **模型与运行时**：模型调用经 AI Gateway，支持一行切换模型、提供商回退和按任务路由不同模型；运行时组合 Vercel Workflows、Sandbox、Drives 和 Connect，提供隔离执行、跨 Sandbox 持久工作区及 MCP/HTTP 端点。
- 🎨 **可定制栈**：框架允许自定义 harness，例如在 `defineAgent` 中设置 `defaultTools: false` 关闭默认工具；数据层可选择自有的工作流存储、沙箱提供商和模型路由，UI 可在 Next.js、Nuxt、SvelteKit 和 TanStack 中原生构建。
- 🛡️ **身份与隔离**：身份方面可接入任意 OIDC 提供商，以 Agent 或已登录用户身份行动，凭证保留在运行时，代码在每会话隔离沙箱中执行；Connections 负责 Linear、GitHub、Stripe 等服务的认证，子 Agent 可承担专门任务。
- 🧪 **生产保障**：生产保障包括 human in the loop 的暂停审批与持久恢复、变更前后运行的 Evals；Software factory 示例用 classifier、analyst、implementer、reviewer 四个子 Agent 将 issue 转为经审查的草稿 PR。

### [推出 eve 1.0 - Vercel](https://vercel.com/blog/eve-is-now-generally-available)

eve 1.0 正式发布，从公开预览转为生产可用的开源 agent 框架。该版本围绕自有 harness、Workflow SDK 持久执行、多人协作、多租户、跨会话记忆、OpenTelemetry 可观测性、扩展与编码代理等能力进行了完善，并大幅降低轮次延迟和长会话的 Workflow 成本。

- 🚀 **正式发布**：eve 1.0 从 6 月公开预览转为正式可用，定位为构建生产级 agent 的开源框架；预览以来发布 230+ 版本并合并数千个 PR，提供 1.0 升级指南并遵循语义化版本。
- 🧩 **核心机制**：eve 的 harness 负责调用模型、运行工具和把任务委派给子 agent；可选择模型、增删工具、编辑指令并设置哪些动作需要审批。Workflow SDK 持久化执行进度，崩溃后可从最后完成步骤恢复；多人会话和 agent 间调用内置。托管到 Vercel 时由 Vercel Workflows 做持久执行，Vercel Sandbox 隔离运行 agent 生成的代码。
- 💬 **多人协作**：多人会话允许多人在同一共享会话中与 agent 协作，eve 记录谁说了什么，并把审批和登录导向正确的人，可按用户或团队设置记忆。Slack 原生频道中每个 thread 是一个共享会话，审批按钮只允许对应人员回答，实时任务卡显示进度和耗时；可在 thread 内继续追问、取消当前轮次或从 Slack 重置会话。Ambient mode 可让 agent 在选定频道未被 @ 时监听，按频道目标决定何时发言或保持安静；为控制模型成本，先用小决策模型筛选消息，只有可能相关的消息才启动一轮。
- 🌐 **框架集成**：eve 1.0 扩展对 Next.js、Nuxt、SvelteKit、TanStack Start 和 Vite 的原生集成，框架集成会随应用一起构建 agent 并配置路由；在 Vercel 上可把 agent 与站点部署为一个项目或分开托管。客户端库统一处理工具调用、审批请求和问题，便于用会话数据构建自定义 UI；可用 eve add channel/web 脚手架生成带 AI Elements 的聊天应用，或在现有 UI 中加入 React、Vue、Svelte 绑定。
- 🏢 **多租户**：一套支持 agent 部署可为每个客户连接其工单系统并使用客户自己的凭据和审批规则；应用负责认证用户并识别租户，再为该租户和用户设置记忆、连接凭据和审批策略。主 agent 循环每次调用模型前，动态定义会从会话和外部数据加载能力；1.0 中覆盖模型、连接、子 agent 以及工具、技能和指令。
- 🧠 **跨会话记忆**：原生记忆支持跨会话携带上下文，可选记忆范围，并使用内置文件记忆、记忆 provider 或自建实现。内置 fileMemory 在 eve dev 中保存在内存，在 Vercel 上保存到配置的私有 Vercel Blob；其他 provider 包括 claude-mem、Hindsight、Kybernesis Arcana、Memanto、memco、Supermemory、Upstash AgentKit。
- 🔍 **可观测性**：追踪基于 OpenTelemetry 重建，eve dev 默认本地记录 trace，自托管可导出到 OpenTelemetry 后端；集成包括 Raindrop，可用 eve add instrumentation/<name> 添加或通过 instrumentation APIs 自建。Trace 显示 agent 等待人工的审批、问题、预算提示和登录，记录模型选择、审批决策、模型用量与成本，并跟踪到 MCP server 和远程 agent 的调用。可过滤 span、按目的地脱敏输入输出；生产中的私密对话默认只发送元数据，不含 prompt 和工具结果。Vercel Agent Runs 用同一批 trace 在仪表盘展示会话、模型调用、工具执行、子 agent 活动和审批决策，eve deploy 创建新项目时自动设置 trace 采样。
- ⚡ **延迟优化**：9 月初在 Vercel Workflows 的托管压力测试中，每轮中位延迟为 3.036s；1.0 同样 100 轮工作负载降至 414ms，p95 从 3.692s 降至 633ms。测试逐条发送消息、每次立即返回 mock 模型响应且每轮无工具调用，只衡量 eve 与 Workflow 开销。Workflow spec 9 让每次运行只有一个 orchestrator，后台步骤不再重放 workflow；事件和流写入改用 WebSocket，减少冗余历史读取。eve 还缓存会话路由信息、可在轮次间把空闲会话迁移到新部署，Web UI 可预热会话。
- 📊 **成本优化**：50 轮 Evo Docs 会话的 Vercel Workflows 估算成本从 5.4¢ 降至 1.3¢，约降低 76%，假设每轮约两个模型步骤、保留 30 天。eve 使用 Workflow SDK 5.5，仅保存轮次间变化的会话数据；workflow step 保存变更并引用已存数据，不需要历史的步骤不再接收历史，checkpoint 存工具返回图片的引用而非字节，prepared snapshot 跳过重复 sandbox 设置，停止 sandbox 后保留文件复用，会话结束时清理。存储改动位于开源 Workflow SDK，自托管在其他 Workflow 后端也减少重复会话数据；Vercel 上 workflow step 运行于 Fluid compute，超过 payload 大小限制的输入仍需额外存储写入，图片和文件仍可能触发写入。模型调用方面，工具和技能列表可按需加载，连接工具经 eve__search 和 eve__tool 运行，减少工具列表扩展，并调整 provider 缓存标记以复用更多内容。
- 🛠️ **扩展机制**：扩展机制让团队共享工具、技能、指令、连接、频道、计划、hooks 和子 agent，无需在 agent 间复制文件；可使用 extensions directory 或 npx eve@latest extension init <name> 创建。示例包括 agent-browser 浏览器自动化、Mux Video 视频资产与剪辑工具、Link 钱包与购买工具。eve 从源码构建 workspace 扩展并在开发时重载变更，便于在一个包中更新共享能力并在 agent 中试验。
- 💻 **编码代理**：1.0 的 code extension 建立在默认文件工具上，增加遵循仓库 AGENTS.md 的编码指令和技能，已包含在 eve 包中无需额外安装；将仓库放入其 sandbox 后，agent 可调查代码、编辑文件并运行项目检查。它使用与其他 agent 相同的 harness 和扩展系统，可替换或禁用工具、覆盖技能并添加指令。配套 eve/extensions/git 增加 GitHub 和 PR 工作流并使用配置的凭据与授权；在 Vercel 上可选远程自修改扩展让 agent 在草稿 PR 中提议修改自身源码，由人审查、合并和部署。
- 🔗 **公共 API**：子 agent、sleep 和 question 工具构建在可通过 defineWorkflowTool 使用的同一 workflow 系统上；工具可返回结果、启动后台任务或作为可恢复任务继续接收消息，可等待人、webhook 或定时器而不持续占用计算资源，运行可在重启后存活，无需单独后台任务系统。示例中定义 reviewer 子 agent 后，工具立即返回 receipt，task 主体等待 reviewer 结果并在后续消息中交给模型。
- 🔄 **升级路径**：1.0 升级指南覆盖扩展构建、agent API、会话事件、客户端和保存历史的变更，部署前应按指南升级；eve 遵循语义化版本，稳定 API 的破坏性变更只在大版本发生，实验性和内部 API（包括实验字段）可能在大版本之间变化。可用 coding agent 按指南顺序升级，并运行类型检查、eve build 和相关测试。
- 📦 **上手方式**：可从终端用 Node.js 24 或更新版本执行 npx eve@latest init my-agent 创建 agent，在交互式终端中安装依赖并打开 eve 终端 UI；若团队有 AI Gateway 访问权限，可复用现有 Vercel CLI 凭据本地调用模型。也可在 Vercel dashboard 用 agent builder 脚手架、建 Git 仓库并部署，或从 coding、知识数据、应用界面、消息、记忆、内容营销等模板开始。

### [CascadiaJS 2027 | 6 月 7 日 -8 日 | 华盛顿州西雅图](https://cascadiajs.com/)

CascadiaJS 2027 是一场面向太平洋西北地区 Web 与 AI 开发者的两天会议，定于 2027 年 6 月 7-8 日在西雅图会议中心举行；页面同时开放售票、演讲征集和赞助合作，并以开发者社区氛围和面对面交流作为核心卖点。

- 🗓️ **会议定档**：CascadiaJS 2027 将于 2027 年 6 月 7-8 日在 Seattle Convention Center 举行，定位为面向太平洋西北地区开发者的 Web + AI 会议。
- 📊 **规模数据**：官方页面列出 600+ 开发者、2 天、20+ 讲者、4 场工作坊和 2 场派对。
- 🧠 **讲者阵容**：已公布 Josh Goldberg、Andrea Griffiths、Shruti Kapoor、Laurie Voss、Kevin Whinnery 等讲者，并注明更多讲者即将公布。
- 📝 **演讲征集**：演讲征集面向 Web + AI 主题，提交截止日期为 2027 年 1 月 10 日，鼓励开发者分享自己的故事。
- 🏢 **赞助合作**：赞助商可接触 600+ 开发者，这些开发者会评估工具、分享推荐并影响组织技术决策；页面提供赞助手册。
- 💬 **社区口碑**：多条推荐语强调会议社区氛围、开发者主导组织、长期传统和卡拉 OK 等非正式交流，适合作为会议差异化卖点。

### [CascadiaJS | 2027 演讲嘉宾征集](https://cfp.cascadiajs.com/)

CascadiaJS 2027 公布演讲征集（CFP），会议定于 2027 年 6 月 7 日至 8 日在西雅图举行，聚焦 Web 与 AI 的前沿实践。提案需提交 2 分钟视频，正式演讲为 25 分钟，截止日期为 2027 年 1 月 10 日，采用滚动录取并最迟于 1 月 18 日通知结果；此次 CFP 同时提供基于 MCP 服务器的 AI agent 提交路径和传统网站表单。

- 🗓️ **会议与截止**：CascadiaJS 2027 将于 2027 年 6 月 7 日至 8 日在西雅图举行，入选演讲时长为 25 分钟；CFP 于 2027 年 1 月 10 日截止，滚动录取，最迟 2027 年 1 月 18 日通知所有提交者。
- 🎯 **征稿方向**：面向 Web + AI 前沿，包括端侧与浏览器内 AI、本地优先与同步引擎、Server Components 与流式渲染、生成式 UI 与 agent 界面、MCP 与 agent 互操作、沙箱代码执行、持久化 agent 工作流、prompt injection 与工具投毒、类型安全 API、边缘数据库等。
- 💡 **提案标准**：演讲应教授 Web + AI 新知识、讲述问题如何解决、帮助开发者或其团队，或分享独特创作经验；不应做产品/公司推介、重复入门信息或集中吐槽，提案可不限于所列类别并允许提交多个想法。
- 🧩 **MCP 提交流程**：MCP 服务地址为 `https://cfp.cascadiajs.com/mcp`，使用 Streamable HTTP；用户用邮箱和一次性验证码登录，agent 调用 `create-profile`、`submit-cfp`、`list-submissions` 完成建档、提交和查询，一次提交一个演讲但可提交多个。
- 🎨 **两分钟视频**：CFP 以 2 分钟视频介绍演讲想法，需说明姓名、公司、角色、主题和为何有趣；视频不会公开，通过 agent 或网站提交且未附链接时可直接录制最多 2 分钟并自动附加，也可上传到 YouTube 不公开链接、Dropbox、S3 或自有主机后用无痕模式检查可访问性，无法访问的视频不予考虑。
- 🛠️ **Agent 接入**：Claude Code 可用 `claude mcp add --transport http cascadiajs-cfp https://cfp.cascadiajs.com/mcp`；Claude 网页/桌面在 Settings → Connectors 添加自定义连接器；Cursor 写入 `~/.cursor/mcp.json`，VS Code 写入 `.vscode/mcp.json`，其他支持远程 Streamable HTTP 的 MCP 客户端也可接入。
- ✅ **网站与账号**：不使用 agent 可通过网站提交，表单与 agent 展示的相同；网站和 agent 使用同一邮箱会看到同一份 profile 和 talks，若两种方式都不可用可邮件联系协助提交，MCP agent 并非必需。
- 🏢 **演讲者福利**：入选演讲者可获 CascadiaJS 全额 VIP 票、停车或拼车报销、Friends of Cascadia 晚宴邀请、最高 500 美元美国国内或 1000 美元国际航班交通费，以及 3 晚住宿。
- ♿ **ASL 支持**：如用美国手语演讲，提案阶段需录制 2 分钟 ASL 视频并附文字稿，Talk Review Committee 将结合两者评估；提案入选后再协作安排现场面向不懂 ASL 观众的表达方式。
- 🧪 **新手与练习**：CFP 对首次大会演讲者开放，评审标准与有经验者一致且不因过往经历加分；文章建议先不录制，站立大声描述想法并重复十次，以约 20 分钟建立表达信心。

### [我如何通过让 monorepo 对 agent 更友好，在一周内修复了 55 个 bug](https://www.devas.life/how-i-fixed-55-bugs-in-a-week-by-making-my-monorepo-more-agent-friendly/)

Takuya Matsuyama 在把 39 个仓库迁入 monorepo 后，继续重构应用代码，让编码代理复制正确模式而非坏模式：按功能重组目录、用 lint 强制模块边界，并在为严格 lint 修复补测试的过程中发现并修复约 55 个由他手工编写的 bug。文章的核心结论是代码库本身就是代理的记忆，纠正代理应落成确定性检查，而不是不断追加规则。

- 🧠 **代码库即记忆**：Lauren Tan 的演讲指出代码库是代理最大的输入之一，已有坏模式会被下一个代理当成惯例复制；因此每次纠正代理时，应优先转成 lint 等确定性检查，而不是继续往规则文件或 `AGENTS.md` 里加说明。
- 🧩 **按功能分组**：目录结构被视为上下文，代码从按类型分组改为按功能和层分组，避免 `utils`、`modules` 这类模糊分类；桌面端形成 `renderer/features` 下 15 个功能目录，每个功能只通过 `index.ts` 对外暴露，组件、hooks、actions、reducer、命令处理器和测试放在一起。
- 🛡️ **强制模块边界**：主进程和渲染进程不能再互相导入，否则 lint 报错；每个 IPC channel 都基于共享契约做类型约束，配置文件只允许主进程写入；移动端和 Web 编辑器也采用同一结构，减少跨边界导入和审查时到处查找。
- ⚙️ **严格 lint 拦截**：采用 Christoph Nakazawa 的 `@nkzw/oxlint-config`，其规则面向 anti-slop 且关注性能；初始在 2,422 个文件中报告 11,589 个问题，尚未全部完成，但仅 `rules-of-hooks` 就发现 18 个真实 bug，例如在提前 return 后或循环中调用 hooks。
- 🧪 **补测试找 bug**：为满足 `react-hooks/exhaustive-deps` 等规则，代理先在旧代码上补组件测试再修改；新增测试 uikit 385 个、mobile web editor 625 个、desktop 764 个、mobile 852 个，最终发现约 55 个 bug 且每个都有先失败的测试，例如编辑器搜索栏每次 effect 都订阅却从不取消订阅，导致“查找下一个”跳过多个匹配；移动端还有 13 个 bug 已被测试固定、等待修复。
- 🐛 **自动修复风险**：自动 fixer 并不总是安全：`catch-error-name` 把 `{ cause }` 改名为 `{ error }`，`prefer-node-protocol` 会破坏 React Native 的 `crypto` alias，`no-var` 会改写 `.d.ts` 文件里的 `declare var`。
- 🔄 **大规模迁移冲突**：目录移动后把 `main` 合并进 lint 分支产生了 145 个冲突；移动端还因从功能 `index.ts` 导出 Redux state 而让 Redux roots 反向加载组件，启动时新增 10 个 require cycle，后来通过每个功能增加第二个公共文件 `state.ts` 解决。
- ⚠️ **验证仍滞后**：迁移后尚未生成打包的桌面构建，CI 还没运行移动后的测试，Windows、Linux 和账号流程也仍未检查；作者下一步希望增加更多运行时验证。
- 💡 **工程方式转变**：作者意识到自己过去也像代理一样盲目沿用 Atom 的目录和编码模式，直到应用变大后旧模式不再适用；新的工程工作是从手工改代码转向通过工具和设计建立与代理的高信任，并在给代理加规则前先怀疑代码库和 lint 规则本身。

### [Inkdrop – 你的上下文，井然有序。](https://www.inkdrop.app/)

Inkdrop 是面向开发者的 AI 原生 Markdown 笔记应用，2016 年起持续运营。本次页面重点介绍它与 AI agent 的衔接：通过 MCP server 让 Claude Code 等客户端检索、读取笔记，提供内嵌 AI 指令的现成笔记模板，并在编辑器内加入行内 AI 助手和 Next Edit Suggestions；同时保留端到端加密同步、全平台客户端、结构化组织与插件化扩展能力。它的定位是让人负责记录「为什么」，把「怎么做」交给 agent，并用单一订阅套餐（30 天免费试用）覆盖个人开发者的知识管理需求。

- 🔗 **MCP 接入**：提供 MCP server，Claude Code 或任意 MCP 客户端可以搜索并读取你的笔记，让过往的决策与经验进入 agent 的工作流。
- 📝 **AI 就绪模板**：针对日报、bug 修复记录、功能计划等常见任务提供现成笔记模板，模板本身携带给 AI 的指令，agent 能按你的方式填写并归档。
- 💡 **编辑器内 AI**：行内 AI 助手支持选中文本后用自然语言描述修改；Next Edit Suggestions 由 AI 预测接下来的输入并在光标处补全整行。
- 🛡️ **加密同步与全平台**：端到端加密同步开箱即用，覆盖 macOS、Windows、Linux、iOS、Android，离线也能随时记录与查看。
- ⚙️ **Markdown 编辑体验**：空行按 `/` 唤出斜杠命令插入标题、警告块、代码块；选中文本弹出浮动工具栏；代码块内提供语言建议与自动补全，输入 `:` 加两个字符触发 GitHub 风格 emoji 补全；粘贴 URL 可就地选择链接格式，页面标题在后台抓取。
- 🎨 **渲染能力**：代码块支持语言图标、行号、文件名，围栏 `markdown` 块内也能高亮；Mermaid 图可平移、缩放、全屏查看并跟随明暗主题；KaTeX 渲染行内与块级公式。
- 📦 **组织与规模**：支持 notebook 嵌套与独立图标、workspace 视图聚焦单棵 notebook 树、active/on hold/completed/dropped 四种笔记状态及筛选、标签切片与笔记置顶，用于在数千条笔记下保持可扫读。
- 💻 **键盘与命令面板**：Telescope 命令面板以模糊查找运行命令、跳转 notebook 或切换标签，插件 `telescope-toc` 与 `telescope-themes` 可扩展；基于 selector 的自定义 keymap 按上下文绑定按键，支持多键序列与全局快捷键；vim 插件提供完整模态编辑。
- 🔧 **可扩展性**：Mermaid、数学、emoji 等内置功能本身即为插件，与社区插件共用同一套 TypeScript 插件 API；可通过 `init.js` 调用 API 脚本化应用、用 `styles.css` 重写任意界面样式；本地 HTTP server 让脚本、自动化与 agent 自定义工具访问笔记。
- 📈 **定价**：单一 Basic 套餐包含全部功能：月付 $9.98/月，年付 $8.31/月（$99.80/年），含云同步、无限笔记数与 30GB 存储，无安装费或隐藏费用，试用期结束后开始计费。

### [类型错误只占用我们编码智能体不到 1% 的时间——Martian Chronicles，Evil Martians 团队博客](https://evilmartians.com/chronicles/type-errors-cost-our-coding-agents-under-one-percent-of-their-time)

Evil Martians 在 2026 年 11 月用公开基准和自建运行检验「静态类型提升编码代理」的流行判断：在十种语言、TypeScript 与 JavaScript、Ruby 与 Rust、以及 Rails 上 plain Ruby、RBS、Sorbet 的对比中，截至当时没有数据表明类型系统能提高代理的任务解决率；类型错误耗时低于 1%，代理主要时间花在读代码和验证上，真正影响效率的是代码阅读量、测试速度、框架预制能力与工具链集成。

- 🧪 **验证方法**：研究汇总 SWE-bench Multilingual 的 300 个真实 issue，覆盖 41 个仓库、9 种语言、13 个模型和统一 `mini-SWE-agent`，并补充 SWE-bench Verified 的 500 个 Python 任务；另自建 24 次 Rails/Rust 运行与 104 次 Fizzy 的 plain Ruby、RBS、Sorbet 试验。
- 📊 **同难度持平**：按任务难度调整后，静态类型语言和动态语言均约解决 65%，Python 约 67%；原始差距主要来自任务构成，类型语言承担了 36% 的大修复任务而动态语言为 23%，类型组内部 Rust 72% 与 Go 53% 的差距也不能归因于类型。
- 🔍 **标签失真**：按参考修复实际编辑的文件重标 823 个 JS/TS 任务，472 个任务的修复编辑了与标签不同的代码；Preact、Svelte 的 JavaScript 本身做类型检查，Material UI 标为 TypeScript 但 174 个 Multi-SWE-bench 修复中 78 个只改普通 JavaScript。
- 📈 **TS 未胜 JS**：同难度比较中，仅改 TypeScript 文件的修复在 SWE-bench Multilingual 落后 2 个百分点、Multi-SWE-bench 落后 4 个百分点、SWE-PolyBench 落后 6 个百分点；两个最新 Opus 5.5 与 GLM-5.2 运行分别落后 10 和 8 个百分点，唯一两类任务都足够的 Material UI 内部打平。
- ⚙️ **代理少用类型检查**：在 TypeScript 运行中 `tsc` 仅约十分之一被调用；SWE-bench Multilingual 的 195 次 TypeScript 运行中仅 19 次运行 `tsc`，而测试套件运行率为 68%，说明代理主要靠测试而非类型检查反馈。
- 🛠️ **LSP 与 hook**：Claude Code 的 `typescript-lsp` 插件只接收 Edit/Write 工具的修改，而 Opus 5.5 在 75 次运行中有 70 次用 `sed -i` 或内联 Python 改文件，因此未报告类型错误；加 `PreToolUse` hook 后 39 次 TypeScript 运行中 23 次看到共 184 个错误，但解决率未提升，插件条件下解决率反而下降。
- 🧩 **类型化 Ruby**：Fizzy 四个任务、四个模型、104 次试验中，plain Ruby 解决 58%，RBS/Steep 61%，Sorbet/Tapioca 57%；68 次类型化试验都在 `AGENTS.md` 要求下以干净检查结束，但类型工具占用 20% 至 28% 的代理时间，且未抓到测试漏掉的 bug。
- ⚠️ **错误耗时极低**：24 次 Rails/Rust 运行中，101 个匹配 Ruby 类型错误模式的步骤仅 16 个是真实类型错误，修复耗时不到 1%；Rust 编译器错误耗时在 greenfield 低于 1%、Campfire 为 3%，没有任何运行因类型错误失败，失败均来自行为、需求或授权问题。
- 🧭 **时间去向**：自建运行中验证与读代码占大头：验证占 30% 至 55%，读代码占 14% 至 44%，类型或编译器错误低于 4%；Campfire 在 Rails 上读代码 15 分钟/次、Rust 41 分钟/次，单个浏览器检查曾耗时 13 分钟，超过 12 次 Rails 运行的全部 Ruby 类型错误时间。
- 🎯 **实践建议**：截至 2026 年 11 月，没有数据支持为代理迁移到静态类型；已用 TypeScript 或 Sorbet 无需放弃，但不应期待迁移提升代理表现。若要让 TS 类型生效，应通过语言服务器插件和 hook 让错误进入代理上下文，保持增量检查为秒级，禁止 `any`、类型断言、非空断言和 `@ts-ignore`，开启 `strict`，并以快速测试作为最终门禁。
- 📦 **开源复现**：所有 24 次 Ruby/Rust 运行记录、类型化 Ruby 实验、Claude Code 会话与基准分析脚本均以 MIT 许可发布在 `coding-agents-myths`，输入按固定 revision 下载并校验 SHA-256，可复现文中表格与图表。

### [获取失败](https://lemire.me/blog/2026/11/20/decoding-base64-email-attachments/)

无法总结：获取内容失败，状态码 520。

### [GitHub - simdutf/simdutf：Unicode 处理例程（UTF8、UTF16、UTF32）与 Base64：使用 SSE2、AVX2、NEON、AVX-512、RISC-V Vector Extension、LoongArch64、POWER 每秒处理数十亿字符。属于 Node.js、WebKit/Safari、Ladybird、Chromium、Cloudflare Workers、Ghostty 和 Bun。· GitHub](https://github.com/simdutf/simdutf)

simdutf 是面向 UTF-8、UTF-16、UTF-32 与 Base64 的 SIMD 加速库，目标是以数十亿字符每秒处理文本，已被 Node.js、WebKit/Safari、Chromium、Bun 等采用；其文档集中说明验证与转码 API、错误定位和安全/替换变体、WHATWG forgiving-base64、C++20 span 与实验性 C++23 constexpr、单头文件裁剪、命令行工具、实验性 C API 与无标准库构建，以及 ABI、静态初始化和线程安全等使用边界。

- 🚀 **项目定位**：simdutf 提供 UTF-8、UTF-16、UTF-32 与 Base64 的 SIMD 加速例程，覆盖 SSE2、AVX2、NEON、AVX-512、RISC-V Vector、LoongArch64、POWER；已用于 Node.js 19.4.0/20.0/18.15 或更好、WebKit/Safari、Ladybird、Chromium、Cloudflare Workers、Ghostty 和 Bun 等生产系统。
- ⚡ **性能与硬件门槛**：数百字符的字符串常可超过十亿字符每秒，非 ASCII 文本可比 ICU 快 3 至 10 倍，ASCII 文本可达 20 倍；AVX-512 需 AVX512-VBMI2（Ice Lake 或更好、AMD Zen 4 或更好）及 GCC 8+、Visual Studio 2022+、LLVM clang 6+，并需 gas 2.30+ 或 nasm 2.14+；RISC-V 需用 -march=rv64gcv 编译。
- 🛡️ **验证与错误定位**：validate_* 提供布尔快速路径，validate_*_with_errors 返回 simdutf::result，含 error_code 与错误位置或已处理数量；错误码包括 HEADER_BITS、TOO_SHORT、TOO_LONG、OVERLONG、TOO_LARGE、SURROGATE 等；validate_utf8_with_counts 额外统计 continuation 与四字节序列，可直接推导 UTF-16 长度和码点数而无需二次遍历。
- 🔄 **转码与流式边界**：convert_* 支持 Latin1、UTF-8、UTF-16LE/BE、UTF-32 间带验证转换，失败返回 0，另有 _with_errors、_safe、_safe_with_details；trim_partial_utf8/utf16/utf16le/be 可去除截断的尾部字符，适合分块流式处理；_safe 有输出上限，但短输入上可能比普通转换慢至多 3 至 4 倍。
- 🛠️ **替换与修复**：to_well_formed_utf16/utf16le/utf16be 用 U+FFFD 替换不匹配代理项，支持复制或原地修复；UTF-16 到 UTF-8 的 _with_replacement 系列始终成功并用 U+FFFD 替换未配对代理项；UTF-8 到 UTF-16 的替换按最大子部分处理，UTF-16 输出不会长于输入，长度结果记录最多 16 个非法子序列的字节偏移并可在转换时复用。
- 🧩 **Base64 解码**：支持 WHATWG forgiving-base64：忽略 ASCII 空白、允许省略填充、拒绝长度模 4 余 1；提供 base64_default/base64_url、无填充或有填充、accept_garbage 和 URL/默认混合模式；last_chunk 支持 loose、strict、stop_before_partial、only_full_chunks；base64_to_binary、_safe、_details 与 binary_to_base64、base64_valid 覆盖流式和并发场景，atomic_base64_to_binary_safe 会写两遍输出，1KB 以上输入比 base64_to_binary 慢 1.5 至 1.8 倍。
- 💻 **C++20/23 接口**：C++20 提供 std::span 重载，可直接传容器；C++23 实验性 constexpr 支持公开 API 的 span 重载，但 atomic_binary_to_base64、atomic_base64_to_binary_safe 不支持，autodetect_encoding、detect_encodings 尚未 constexpr；_base64 字面量在编译期解码为 std::array<char,N>，空白被忽略，非法输入导致编译错误。
- 📦 **集成与工具**：需要 C++17 编译器和 CMake 3.18+；可发布或生成 simdutf.h 与 simdutf.cpp 单头文件，amalgamate.py 支持 --with-utf8、--with-utf16、--with-utf32、--with-ascii、--with-latin1、--with-base64、--with-detect-enc 裁剪功能并设置 SIMDUTF_FEATURE_* 宏；可通过 vcpkg、conan、FreeBSD port、brew 获取，生产应使用 vX.Y.Z 发布而非主分支；sutf 类似 iconv 转码 UTF-8/UTF-16LE/BE/UTF-32，fastbase64 与 fastbase64.coreutils 提供 BSD/GNU 兼容 Base64 工具，benchmark、benchmark_base64、shortbench 覆盖转码、Base64 和短输入基准。
- 🧪 **实验性构建**：C API 以 simdutf_c.h 提供 C11 薄封装，覆盖验证、转码、长度估算、find 和 Base64，目前实验性且不支持有限功能单头文件；无 C++ 标准库构建也是实验性，仅在 GCC/LLVM/clang 支持，需定义 SIMDUTF_NO_LIBCXX=1 并使用 -nostdlib++ -fno-rtti -fno-exceptions，会自动启用静态初始化。
- ⚠️ **ABI、初始化与线程安全**：SIMDUTF_USE_STATIC_INITIALIZATION 实验性选项可去掉函数局部静态的同步开销，但可能触发静态初始化顺序问题；ABI 要求代码与预编译库使用相同 C++ 标准、标准库和 SIMDUTF_FEATURE_* 宏，Windows DLL 需定义 SIMDUTF_USING_WINDOWS_DYNAMIC_LIBRARY=1；库本身单线程，CPU 检测和运行时分发线程安全，但主线程清理运行时分发对象时其他线程继续使用可能有问题，可考虑 std::quick_exit。

### [在生产环境中发现 NestJS 应用的内存泄漏 - DEV Community](https://dev.to/nestjs/finding-a-memory-leak-in-a-nestjs-app-in-production-48km)

这篇文章以线上 NestJS 应用内存缓慢上涨、最终被 OOMKilled 或抛出 Reached heap limit 为起点，说明重启只能重置时钟而不能修复泄漏：先用 process.memoryUsage()、v8.getHeapSpaceStatistics() 区分真实泄漏与流量锯齿，把 --max-old-space-size 设在容器限制之下，再逐条排查 Nest 中最常见的泄漏来源，即默认单例 provider 的无界缓存、被单例长期持有的请求作用域实例、按请求注册却不移除的监听器与订阅、无 TTL 的缓存和未清理的定时器；随后用堆快照对比定位 retainers，用 NestJS Observe 的运行时指标和趋势判定把泄漏归到具体端点、实例和发布，并用自定义 gauge 验证修复。

- 🐛 **先判断是否真泄漏**：健康服务的内存呈锯齿状：V8 不断分配和回收；泄漏的标志是锯齿底部持续抬升，即每次 major GC 后存活的对象在流量平稳时仍在增长。跟随流量并在夜间回落的是负载；部署后出现阶跃上升是回归，需要 bisect，无论之后是否继续增长。重启只是隐藏趋势，不是修复。
- 📊 **三个内存数字**：process.memoryUsage() 的 heapUsed 是存活 JS 对象占用，代码泄漏体现在这里；heapTotal 是 V8 为堆预留的量，跟随 heapUsed 缓慢回落；rss 是进程全部内存，若 RSS 上涨而堆持平，要看 Buffers（同一次调用中的 external 与 arrayBuffers）、没有人消费的流和原生模块。v8.getHeapSpaceStatistics() 可进一步区分：长期存活对象泄漏在 old_space，大字符串或数组泄漏在 large_object_space，new_space 活跃但持平只是分配波动；v8.getHeapStatistics().heap_size_limit 是 V8 实际使用的上限。
- ⚙️ **先设置堆上限**：显式设置 --max-old-space-size，并明显低于容器内存限制，为堆外内存留出空间。否则内核会从外部杀掉进程（OOMKilled，退出码 137），既没有错误也没有调用栈，更没有机会写快照；设置后由 V8 先触及自身上限，这样崩溃才可分析。
- 🧩 **单例 provider 生命周期**：Nest 中 provider 默认是单例，生命周期与整个应用相同，因此它持有的任何东西也会存活同样久。典型例子是 RatesService 中以 `${currency}:${day}` 为 key 的 Map，只写入从不删除，key 空间随日期无限增长；应对方式是加大小上限（LRU）、加 TTL，或迁移到 Redis。
- 🔄 **DataLoader 不可共享**：DataLoader 会为实例生命周期内加载过的每个 key 保留缓存，官方 README 建议每个请求新建一个：长期存活的 loader 会占用过多内存，跨用户共享缓存更有风险。放进单例 provider 会同时中招，应改为在 GraphQL context 工厂中创建，或用 @Injectable({ scope: Scope.REQUEST })；请求作用域会向上冒泡，注入该 loader 的 resolver 也会变成请求作用域。
- 🔗 **请求作用域被单例钉住**：Nest 用 WeakMap 以请求的 ContextId 为 key 保存请求作用域实例，请求结束且无其他引用时会一并回收。泄漏来自长生命周期对象持有这些实例，常见于构造函数：单例 EventEmitter2 上 events.on('order.created', ...) 的闭包持有 this，this 又持有 request 的 headers、body、user。请求作用域 provider 没有按请求执行的销毁钩子，onModuleDestroy 等只在单例上、且仅在应用关闭时调用。修复原则是引用只朝一个方向：请求作用域可以用单例，单例不能持有请求作用域实例；必要时在 Express 上用 request.res?.once('close', () => events.off('order.created', handler)) 释放。快照中该类与 IncomingMessage 的实例数应接近正在处理的请求数，若按两次快照间隔内服务过的请求数增长，retainers 会终结于 emitter 的 _events、Subject 的 observers 或单例数组。
- 🧭 **其他常见模式与例外**：Durable providers 是“随请求回收”的有意例外：ContextIdStrategy 每租户返回一个持久上下文，就为每个租户保留一套实例，前提是租户数量有界；若用 user id 或客户端可控的 header 作 key，就等于用 DI 重建了第一个例子里的 Map。ModuleRef.create() 创建的实例完全在容器管理之外，只要你还持有它，它就一直存在。此外还有：在请求处理器里对长生命周期 emitter 调用 this.events.on('order.paid', handler)，会累积监听器和闭包，超过 10 个监听器时 Node 会抛 MaxListenersExceededWarning，应把它当作泄漏报告，而不是用 setMaxListeners 消音；对长生命周期 Subject 或 interval 订阅却不用 take、takeUntil 或取消订阅；把 req 直接 push 进单例数组；无 TTL 无上限的内存缓存；以及 provider 中启动却不在 onModuleDestroy 清理的 setInterval。
- 🔍 **用堆快照取证**：以 node --heapsnapshot-signal=SIGUSR2 --max-old-space-size=1536 dist/main.js 启动，内存高时执行 kill -USR2 <pid>，快照写入进程工作目录，文件名形如 Heap.20261020.143012.4213.0.001.heapsnapshot，Kubernetes 中用 kubectl cp 取出。--heapsnapshot-near-heap-limit=2 可在堆接近上限时最多写两份，自 Node.js 22.22.1、24.13.1、25.4.0 起不再是实验特性。代价要提前规划：生成快照会阻塞事件循环，阻塞时长取决于堆大小，并需要约两倍堆内存的内存，已经逼近上限的进程可能因此被杀；应在有余量的副本上、最好先摘掉流量再操作。
- 🧪 **采样分析与快照对比**：--heap-prof 在整个进程生命周期运行 V8 采样堆分析器，退出时写出 .heapprofile，DevTools 可按函数查看分配情况；它采样而非遍历整个堆，开销小，但只在干净退出时写入，适合主动排空并停止的副本，不适合抓崩溃。需要即时应答时可用 v8.writeHeapSnapshot()，但要放在仅管理员可访问的端点后面，因为快照包含内存中的全部内容，包括密钥。对比方法：预热后取一份快照，堆增长一段时间后再取一份（第三份更晚的快照能让模式更明显），在 Chrome DevTools 的 Memory 标签打开，选中较晚的快照并切换到对较早快照的 Comparison 视图，按 size delta 排序，取增长最多的 constructor 查看 Retainers，链通常终结于 RatesService.cache、AuthorsLoader.byId 这类 provider 字段。
- 📈 **Observe 定位端点与实例**：NestJS Observe 默认每 60 秒（runtimeMetricsInterval）采样各进程的 RSS、heap total、heap used、垃圾回收和事件循环，并 traces 请求与任务；所有计划含免费版，runtime metrics 不计为事件。页面按四个 gauge 给出 Coping、Strained 或 Under pressure 的判定；排查泄漏不要依赖内存 gauge（它是 RSS 对操作系统报告的总内存，容器内常是整机内存，即将被 OOMKilled 的 pod 也可能只显示几个百分点），要看堆图表和趋势。窗口后三分之一的平均堆比前三分之一高 30% 以上时会出现 Heap usage keeps climbing 提示，按三分段比较可避免正常锯齿误触发；若爬升与某个请求或任务同步起落，Memory 区顶部会点名该操作。再往下可按实例卡片查看（一个 pod 上涨而其他平稳，说明与它收到的流量有关，如某租户、粘性会话或独占全部分区的消费者）、对比发布页面的 What changed in the code 缩小 diff、点击内存阶跃点查看当时异常运行的请求与任务（按偏离自身基线的程度排序），并用 GC 图表佐证：泄漏的堆越满，major GC 越频繁、GC 占总时间比例越大。
- 🎯 **用自定义 gauge 验证**：对疑似增长的字段直接埋点，而不是从堆推断：在 provider 中用 @Interval(60_000) 定时执行 this.tracer.gauge('rates.cache.size').setValue(this.cache.size)，如果这条线与堆同步上升就确认了，若持平则一下午就排除掉。自定义指标不绑定 trace，需由定时器上报，可像内置指标一样设置告警；修复后继续观察，Pro 及以上可用 runtime alert rules 按应用监控内存，anomaly 模式（偏离自身近期基线）往往比固定阈值更合适。
- ✅ **下一次泄漏前的清单**：把 --max-old-space-size 设在容器限制之下，让 V8 先于内核失败；至少保留一个带 --heapsnapshot-near-heap-limit 且有可写目录的副本；看堆的趋势而不只是水位，阈值只提前几分钟，趋势能提前几天；先查单例上的字段，多数泄漏是只增不减的 provider 属性；确认没有单例持有请求作用域实例，若快照中请求作用域类的实例数远高于正在处理的请求数，就有长生命周期对象在留住它们；不要把重启当成修复。

### [为测试与增长重构 Fastify 应用的 5 个步骤——Liran Tal](https://lirantal.com/blog/refactor-fastify-app-testing-growth)

文章以一个小型 users API 为例，说明如何把单文件 Fastify 应用按职责边界重构为可测试、可增长的结构：用异步工厂分离应用构建与网络监听，把 Prisma 放入插件管理连接与关闭，以两阶段 autoload 组织基础设施插件和按功能划分的路由，在处理器旁声明请求与响应 JSON Schema，并用 tap 的 inject 在没有监听器的情况下测试路由和启动失败；示例基于 Fastify 5、Node.js 24、Prisma 6.19（SQLite）和 tap 21，并提醒 Prisma 7 的客户端配置不同。

- 🧩 **构建与启动分离**：将 `buildApp()` 做成异步工厂，内部注册插件并 `await app.ready()`，但不调用 `listen()`；`server.js` 作为进程入口负责监听和 `SIGINT`/`SIGTERM` 关闭，使测试可为每个用例创建独立实例。
- 🔑 **Prisma 生命周期**：用 `fastify-plugin` 包装 Prisma 插件，在启动时 `$connect()` 并 `decorate('prisma')` 供同作用域路由使用；`onClose` 只 `$disconnect()` 插件自己创建的客户端，调用方注入的客户端由调用方清理。
- 📦 **两阶段 autoload**：先 autoload `plugins` 再 autoload `routes`；路由模块用 `autoPrefix` 提供 `/users`，加载器提供 `/api`，设置 `dirNameRoutePrefix: false` 避免目录名改变公开 URL。小项目仍可显式 `register`，autoload 不保证文件间的依赖顺序。
- ✅ **Schema 契约**：为 `/:id` 声明 `params` 为大于等于 1 的整数，并用响应 schema 约束 200 和 404；Fastify 默认 Ajv 会把合法数字路径参数强制为整数，非法值在查询前返回 400，响应 schema 控制序列化但不负责授权或数据库完整性，Prisma `select` 只取 `id` 和 `name`。
- 🧪 **无监听测试**：用 `tap` 与 `app.inject()` 测试状态码、响应体和启动失败，无需占用端口；示例用假 Prisma 客户端验证查询参数、200 序列化、400 时不访问数据库、404、错误前缀 404，以及 `buildApp()` 在数据库连接失败时拒绝。假客户端不能验证 SQL、迁移和真实连接清理，需另设临时数据库集成测试。
- ⚠️ **重复路由**：两个插件注册相同方法和 URL 且路由约束相同时，Fastify 在启动阶段以 `FST_ERR_DUPLICATED_ROUTE` 拒绝；封装不会自动隔离 URL 命名空间，前缀和路由约束才决定是否冲突，这与 Express 按注册顺序执行处理器的行为不同。
- 🛠️ **方案取舍**：重构增加入口、工厂、数据库插件和功能路由等机制；显式注册适合插件少或需严格排序，autoload 适合模块增长但让文件布局成为配置的一部分；假客户端测试快但无法覆盖持久化，真实临时库更可信但隔离成本高。
- 🛡️ **运维边界**：启动时连接成功只是一次依赖检查，运行中数据库仍可能不可用；应区分 liveness 与 readiness、定义数据库不可用是否摘除实例并设置超时。Pino 日志需配置脱敏（如授权头和 cookie），认证基础设施应放在可继承作用域，但授权钩子仍需覆盖受保护路由且不能误伤健康检查。
- 📈 **性能声明**：把处理器拆到不同文件不会自动提升吞吐；复用 Prisma 客户端可避免每请求创建客户端，编译后的响应 schema 可能影响序列化，但数据库延迟常占主导。应固定端点、数据集、并发和日志配置对比，并记录延迟分位数与错误率。

### [Jimp | Jimp](https://jimp-dev.github.io/jimp/)

Jimp 是一个完全用 JavaScript 编写的图像处理库，可在 Node.js 和浏览器中读取、编辑和写入图像，无需安装或编译原生依赖；站点集中展示其 API、格式支持、可扩展插件机制以及 v1/v2 迁移文档，并用浏览器内可运行示例降低试用门槛。

- 🚀 **纯 JS 跨平台**：Jimp 用纯 JavaScript 实现，可在 Node.js、浏览器、Web Worker、worker thread 和 Cloudflare Workers 中运行，不需要原生依赖。
- 📦 **内置多格式**：内置支持 PNG、JPEG、GIF、BMP、TIFF 和 ICO；WEBP、AVIF、JPEG XL、JPEG 2000 与 SVG 需通过 WASM 插件添加。
- 🧩 **链式图像方法**：提供 resize、crop、rotate、flip、blur、sharpen、pixelate、dither、颜色调整、合成与绘图等 102 个方法及辅助函数，方法可链式调用并原地修改图像。
- ⚙️ **三步工作流**：典型程序为 load、manipulate、save：从文件、URL 或 buffer 读取，调用方法处理，再写出文件或获取 buffer/data URL。
- 🛠️ **可扩展与裁剪**：可为新格式或图像处理方法编写插件，也可构建仅包含所需插件和格式的自定义 Jimp，减小体积。
- 💻 **浏览器实机示例**：网站示例在浏览器中运行真实 Jimp，可上传图片、选择区域并执行 pixelate 等方法，同时显示对应代码和完整 playground。
- 📚 **文档与迁移**：文档覆盖浏览器使用、大图解码限制、EXIF、色彩空间、插件、自定义构建、Worker、图像服务器、Open Graph 图片，以及 v1 和 v2 迁移说明。

### [发布 v2.0.0 · jimp-dev/jimp · GitHub](https://github.com/jimp-dev/jimp/releases/tag/v2.0.0)

Jimp 发布 v2.0.0 大版本，带来 Node.js 22+ 运行要求、多项破坏性 API 与像素运算修正，以及 TrueType/OpenType/WOFF 字体打印、绘图插件、动画 GIF/多页 TIFF、JPEG XL/JPEG 2000/SVG/ICO 等格式支持和新滤镜/变换能力，并集中修复颜色合成、重采样、编解码与跨运行时兼容问题。

- 🚀 **正式发布**：Jimp v2.0.0 发布，由 hipstersmoothie 于 11 月 24 日发布，包含大量破坏性变更、增强、修复和文档更新，并感谢 17 位贡献者。
- ⚙️ **运行环境**：要求 Node.js 22 或更高版本，CI 已切到 Node 22，同时让仓库在 Windows 上完成构建和测试。
- ⚠️ **破坏性变更**：移除无效选项，修正颜色/阈值/量化像素数学，越界区域改为裁剪到图像，`setPixelColor` 不再绘制边缘外像素，`composite` 可跨 Jimp 类，`write()` 选项按扩展名类型化，并支持读取 `Uint8Array`/`Blob`。
- 📚 **字体与文字**：`@jimp/plugin-print` 支持 TrueType、OpenType 和 WOFF 字体，按码点打印，保留空行并测量换行，修复 `loadFont` HTTP 错误、缺失字形按 `?` 度量及非 PNG BMFont 页面报错。
- 🎨 **绘图与边框**：新增 `@jimp/plugin-draw`，可绘制线条、形状、路径、渐变和洪水填充；新增 `@jimp/plugin-border`，提供 `roundCorners`、`border` 和 `boxShadow`。
- 🔄 **动画与多页**：支持读写动画 GIF 和多页 TIFF，并修复 GIF 编码内存耗尽问题。
- 📦 **格式扩展**：新增 `@jimp/wasm-jxl`、`@jimp/wasm-jpeg2000` 和 `@jimp/wasm-svg` 读取，支持 ICO 读写、1/4/8 位 BMP 写入，以及通过预编译 wasm 模块在 Cloudflare Workers 中使用各 wasm 编解码器。
- 🧩 **色彩与元数据**：新增 Display P3 与 ICC 色彩配置支持，JPEG 写入可选保留 EXIF，新增 `exifRotate` 选项跳过自动旋转，并为 PNG 默认选择最小无损颜色类型。
- ⚡ **变换与滤镜**：新增 `skew()`、`affine()`，颜色动作 `multiply`、`sepia(amount)`、`exposure()`、`vibrance()`，Floyd–Steinberg/Atkinson/Bayer 抖动、Otsu 自动阈值、`sharpen()` 及卷积 `divisor`/`bias`。
- 🔍 **重采样与图像操作**：新增 LANCZOS、LANCZOS2、MITCHELL 重采样模式，优化 BILINEAR/BICUBIC/HERMITE/BEZIER 并加入 `premultiplyAlpha`，新增 `autocropRect`、分数 `{ x, y }` 对齐、`displace` 的 y 偏移，以及形态学 `erode()`、`dilate()`、`open()`、`close()`。
- 🛠️ **修复与兼容**：修复模糊按 alpha 加权和真正可分离高斯、pHash 排除 DC 项、旋转中心偏移、蒙版亮度、JPEG/TIFF/PNG/BMP 解码边界，以及 Deno、Workers、浏览器无 Buffer polyfill 的兼容问题。
- 📝 **文档与迁移**：文档站升级到 Astro 7 和 Starlight 0.43 并重新设计，补充 Jimp 2.0、迁移指南、绘图、动画 GIF/多页 TIFF、Vite/wasm 配置及 v0/v1 残留清理。

### [发布 v2.1.0 · jimp-dev/jimp · GitHub](https://github.com/jimp-dev/jimp/releases/tag/v2.1.0)

Jimp 发布 v2.1.0，核心变化是引入 @jimp/jpeg-js 与 @jimp/pngjs 两个维护分支、让 GIF 解码改用 Jimp 自有 reader 并移除 omggif，同时更新 CI、测试资产与文档站体验和品牌；这些改动覆盖核心包、编解码包以及多个插件和 WASM 包，重点提升图像编解码依赖的可维护性。

- 🚀 **版本发布**：jimp v2.1.0 发布，涉及 @jimp/core、@jimp/docs、jimp 以及 JPEG/GIF/PNG 编解码和多个 plugin、wasm 包，主要变化集中在编解码依赖与 GIF 解码路径。
- 🧩 **JPEG 依赖**：新增 @jimp/jpeg-js，作为 jpeg-js 的维护分支，并由 @jimp/js-jpeg 使用（#1554）。
- 🧩 **GIF 解码**：GIF 改用 Jimp 自己的 reader 解码，移除 omggif 依赖（#1553）。
- 🧩 **PNG 依赖**：新增 @jimp/pngjs，作为 pngjs 的维护分支，并用于 @jimp/js-png（#1552）。
- ⚙️ **CI 发布**：CI 支持在发布后手动部署文档（#1546）。
- 🧪 **测试资产**：将 jpeg-js 测试语料和编解码一致性测试图片移入 Git LFS（#1556、#1555），并为 @jimp/pngjs 的 6000x4000 往返测试设置 60s 超时（#1557）。
- 🎨 **文档品牌**：多个 README 使用 Jimpy 与 JIMP wordmark 品牌，favicon 和分享横幅中的铅笔吉祥物替换为 Jimpy（#1547、#1548）。
- 🛠️ **文档体验**：修复文档站加载时布局偏移和页头跳动，保持左侧栏滚动可见，修复 Safari 裁切 feature stamps，并让页面切换交叉淡入（#1544、#1545、#1550、#1551）；README logo 字母轮廓闭合（#1549）。

### [jimp-dev/jimp 发布 v2.2.0 · GitHub](https://github.com/jimp-dev/jimp/releases/tag/v2.2.0)

Jimp 发布 v2.2.0，集中加入颗粒与渐变抖动、3D LUT 调色、BlurHash 占位图、中值/双边降噪、渐变映射、完整 W3C 混合模式、智能裁剪和主色提取等图像处理能力，同时引入 @jimp/layout、@jimp/worker、@jimp/server 以及 core 的 apply()，让 OG 图布局、主线程外处理和边缘运行时图像转换更易落地。

- 🚀 **正式发布**：Jimp v2.2.0 由 @hipstersmoothie 于 11 月 25 日发布，覆盖 jimp 及 docs、server、worker、layout、utils 和多个插件包。
- 🎨 **颗粒与抖动**：新增 grain() 和渐变抖动，用于修复渐变中的条带（banding），涉及 color、draw 等包。
- 🎨 **3D LUT 调色**：@jimp/plugin-lut 新增 colorGrade()，支持从 .cube 文件和 Hald 图像进行 3D LUT 色彩分级。
- 🔗 **BlurHash 占位**：@jimp/plugin-hash 新增 BlurHash 占位图支持，提供 image.blurhash、decodeBlurhash 和 fm=blurhash。
- 🧪 **降噪滤波**：@jimp/plugin-blur 新增 median() 和 bilateral() 降噪能力。
- 🎨 **渐变映射**：新增 gradientMap()，用于生成双色调（duotones）和渐变映射效果。
- 🎨 **混合模式**：补全 W3C 混合模式，并在 @jimp/layout 中提供 blendMode。
- 🎯 **智能裁剪**：@jimp/plugin-cover 的 cover 支持“entropy”和“attention”两种智能裁剪模式。
- 📊 **主色提取**：@jimp/plugin-quantize 新增 palette() 和 dominantColor()，用于提取图像主色。
- 🧩 **布局渲染**：新增 @jimp/layout，这是面向 OG 图片的 flexbox 风格布局渲染器。
- ⚙️ **主线程外运行**：@jimp/worker 可让 Jimp 在主线程之外运行。
- 🌐 **边缘运行时**：新增 @jimp/server，为边缘运行时提供图像转换 handler，并涉及 js-ico、js-png 及 wasm-avif、wasm-png、wasm-webp。
- 🛠️ **数据化编辑**：core 新增 apply()，可执行以数据形式存储的一组编辑操作。
- 📝 **文档修复**：文档 OG 卡片现在展示每个页面的方法结果或图标，并适配长标题。

### [绘制 | Jimp](https://jimp-dev.github.io/jimp/concepts/drawing/)

Jimp v2.2.0 文档介绍了 @jimp/plugin-draw 的矢量绘图能力：可以在图像上以类似小型画布的方式绘制抗锯齿的直线、矩形、椭圆、多边形和 SVG 路径，支持纯色或渐变填充与描边，以及油漆桶式 floodFill；同时导出底层光栅化 API，供自定义插件复用同一套抗锯齿、Paint 与合成逻辑。

- 🎨 **绘制方法**：drawLine、drawRect、drawEllipse、drawPolygon、drawPath、floodFill 和 render 都接收一个 options 对象，并直接在图像上绘制，因此调用可以链式串联。
- 🧩 **抗锯齿原理**：渲染时不采样像素；它为每个像素精确计算形状覆盖该像素的面积比例，并把该比例作为该像素的绘制强度，方法与 FreeType、font-rs 相同；曲线和弧会先按 0.1 像素误差拆成线段，再进行测量。
- 🎯 **填充与描边**：drawRect、drawEllipse、drawPolygon、drawPath 支持 fill、stroke 或两者；渲染时先填充再描边。strokeWidth 默认 1，并以边缘为中心；drawRect 还支持 strokeAlign 取 inside 或 outside；drawLine 只描边，使用 color 和 width。
- ⚙️ **颜色与渐变**：fill、stroke、color 接受 Paint，可为十六进制数、CSS 颜色（含 color(display-p3)）或 {r,g,b,a} 对象；渐变支持 linear 与 radial，坐标为图像像素，stops 至少一个，裸色均匀分布；CSS 颜色会转换到图像色彩空间，十六进制数与对象不转换。
- 📊 **渐变抖动**：dither: true 会在量化前加入小于半级的确定性噪声以消除色带，默认关闭，因为 1200×630 的渐变卡片 PNG 会从 75 KB 涨到 512 KB，且 JPEG/WebP 压缩会自行抹平噪声并引入自己的色带。
- 🔄 **填充规则**：drawPolygon 和 drawPath 支持 fillRule：nonzero（默认，按绕行方向计数）和 evenodd（嵌套轮廓即成为孔）；描边始终按 nonzero 填充。
- 🛡️ **裁剪与校验**：形状可部分或完全位于图像外，越界坐标会被裁剪且不会抛错，从图像外开始的 floodFill 不会填充；非法输入由 zod 校验并抛出 ZodError，例如 NaN、Infinity、负尺寸或 miterLimit 小于 1。
- 💻 **合成方式**：采用 source-over 与直通 alpha 混合，绘制 alpha 会乘以覆盖率；半透明红画在透明图上得到 0xff000080，而不是更暗的红；单次调用中形状的重叠部分只混合一次。
- ⚡ **性能**：纯 JavaScript 实现，使用类型数组且逐像素无分配；1920×1080 上 1000 条 1/3/10 像素宽的随机线耗时 50/65/130 ms，1080p 满幅线性渐变矩形 43 ms（开 dither 约多 45 ms），整幅 floodFill 26 ms，浏览器包增约 7 KB gzip。
- 🛠️ **插件 API**：@jimp/plugin-draw 导出 parseSvgPath、flattenPath（默认 0.1 像素容差）、strokePolylines、rasterize、fillPolylines、fillPath、strokePath、drawShape 和 PaintSchema，可在自定义插件中复用同样的抗锯齿、Paint 与合成；图像只需提供 bitmap 与 iccProfile。
- 📖 **路径与字体**：路径命令与 opentype.js 一致（M/L/Q/C/Z，H/V/S/T/A 会转换），transform 为 [a,b,c,d,e,f] 矩阵；通过 loadTTF 绘制的 TrueType/OpenType 文本使用同一光栅化器，因此同样支持颜色与渐变。

### [演练场 | Jimp](https://jimp-dev.github.io/jimp/playground/)

Jimp v2.2.0 的 Playground 把整套 Jimp 图像处理方法搬进浏览器：用户可选择方法、调整参数并实时查看效果，同时自动生成与操作等价的 Node 或浏览器代码，还可上传自有图片进行试验。

- 🚀 **浏览器演练场**：在浏览器中直接对图片试用每个 Jimp 方法，调整选项即可看到图像变化，并可复制生成结果对应的代码。
- 🧩 **真实执行与代码生成**：每个按钮运行真实的 Jimp；代码面板构建等价程序，Node 版以 `write()` 保存结果，Browser 版通过 `getBase64()` 显示到 `<img>`。
- 🛠️ **方法与分类**：覆盖加载保存、尺寸形状、模糊效果、颜色、合成、绘制、文本、像素、比较和工具等方法，包括 `getBuffer`、`resize`、`crop`、`blur`、`composite`、`print`、`diff` 等。
- 🎨 **交互操作**：更改选项会重跑最后一步，点 `Apply again` 可叠加调用；`crop`、`pixelate` 等区域工具支持在图上拖选区域；按住 Compare 查看原图，Undo 回退。
- ⚡ **性能限制**：宽于 360 px 的图片会先缩放以保证 Playground 流畅，但用户复制的代码仍作用于全尺寸图片。
- 📦 **版本与参考**：页面标注 Jimp v2.2.0；每个方法有独立页面，包含全部选项、示例和说明，可在 method reference 中浏览。

### [如何检测 Claude Duet](https://fingerprint.com/blog/how-to-detect-claude-duet/?utm_source=NodeWeekly112626&utm_medium=newsletter)

Fingerprint 在其 Bot Detection Smart Signal 中新增对 Anthropic 个人 AI 代理 Claude Duet 的识别，将其作为独立的 AI agent 流量标注出来，并与已有的 Claude 助手流量区分。Claude Duet 目前以研究预览形式面向美国 Claude Pro、Max 和 Ultra 订阅用户分批开放，能通过自己的云端浏览器和真实凭据替用户登录、操作网站并完成购买；Fingerprint 的更新让站点可以识别这类自动化流量，再按规则决定放行、增加摩擦或拦截。

- 🚀 **新增识别**：Fingerprint 的 Bot Detection Smart Signal 现在可直接标注推断为 Claude Duet 的流量，使用 `bot_type` 为 `claude_duet`，并与已验证的 Claude 助手流量分开。
- 🧠 **代理定位**：Claude Duet 是 Anthropic 的个人 AI 代理，用户可通过文本或语音下达任务；它在云端拥有自己的计算机和浏览器，可读取收件箱、登录网站并用 Link 或 Shop Pay 的一次性卡完成购买，关闭应用后仍继续运行。
- 🔍 **检测难点**：Claude Duet 会通过独立 User-Agent 和 Anthropic 公布的 IP 地址声明代理身份，但这不是 Web Bot Auth 那样的加密签名；User-Agent 可被复制，真实云浏览器不会暴露常见自动化标记，真实凭据和一次性支付卡也让账户与支付检查看起来像普通客户。
- 🧩 **响应字段**：检测命中时返回 `bot` 为 `good`、`bot_type` 为 `claude_duet`、`category` 为 `ai_agent`、`provider` 为 `Anthropic`，`identity` 为 `unknown`，表示已识别代理但未提供可验证身份；`confidence` 可为 `high`、`medium` 或 `low`。
- ⚙️ **使用方式**：安装 Fingerprint 后，可通过 Server API、MCP server 或仪表盘筛选 Claude Duet 事件，并用规则引擎或自有系统决定放行、在登录和结账等敏感流程增加摩擦，或直接拦截。
- ⚠️ **上线说明**：已有 Bot Detection 的 Fingerprint 客户无需额外付费即可使用 Claude Duet 检测，但该能力正分批上线；此前被标为通用浏览器自动化或 `chromium_automation` 的会话现在会按名称识别，依赖 `bot` 为 `bad` 等规则的匹配结果可能出现小幅变化。

### [重新介绍 Stricli | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/reintroducing-stricli/)

Bloomberg 重新介绍其于 2024 年开源的 Stricli CLI 框架，强调其面向 TypeScript 的类型安全设计和基于动态 import() 的按需加载能力，可在 Node.js、Bun 等任意 JavaScript 兼容运行时中使用；文章还提到面向 AI 编码代理的 llms.txt 文档和交互式文档体验。

- 🚀 **框架定位**：Stricli 是 Bloomberg 于 2024 年开源的 CLI 框架，已用于其内部命令行工具，并可在 Node.js、Bun 等任何 JavaScript 兼容运行时中使用。
- 🧩 **类型安全**：Stricli 以 TypeScript 为核心设计，提供编译期保证，使参数解析器产生的类型与各命令实现期望的类型一致，并支持字符串枚举、可变参数数组等类型。
- 🛡️ **运行时校验**：框架内置运行时断言，可与编译期类型一起配置；当用户为参数提供无效值（如本应为 number）时，能检测并给出帮助信息，这些配置还会同步影响自动生成的帮助和错误消息。
- ⚡ **按需加载**：通过 async loader 支持和动态 import()，Stricli 只懒加载当前参数需要的命令代码；实现代码可组织为 ES modules，且动态加载的代码仍受 TypeScript 类型检查，无需在运行时性能与类型安全之间取舍。
- 🧠 **AI 与文档**：文章认为类型安全保证有利于 AI 编码代理，并已发布 token 友好的 llms.txt 版本文档；文档还提供 Quick Start 和可在浏览器中试验 API 的 Live Playground。

### [Stricli](https://bloomberg.github.io/stricli/)

Stricli 展示了其命令行解析器的核心设计：用一次定义的 TypeScript 类型贯通命令的命名标志和位置参数，并以零运行时依赖、ESM/CJS 双发布、可代码分割、可选依赖注入和动态 shell 补全来兼顾类型安全、启动性能与可测试性。

- 🧩 **TypeScript 类型贯通**：命令的命名标志和位置参数只需定义一次 TypeScript 类型，类型信息会贯穿整个应用。
- 📦 **零运行时依赖**：Stricli 是自包含的命令行解析器，没有运行时依赖，这来自其对支持特性范围的严格限制。
- 🔄 **ESM 与 CJS 双支持**：包同时面向 ESM 和 CommonJS 消费者发布，但推荐使用 ESM。
- ⚡ **面向代码分割**：命令实现与参数定义分离，便于在 ESM 构建工具中做异步导入和代码分割；运行 `--help` 时无需导入任何运行时依赖。
- 🧪 **可选依赖注入**：所有系统访问都封装在单个 context 对象中，因而更便于依赖注入，也便于在单元测试中 mock。
- 💬 **动态自动补全**：一等支持 shell 自动补全，并可在运行时加入自定义的动态建议。

### [GitHub - keichi/binary-parser：用于二进制数据的极速声明式解析器构建器 · GitHub](https://github.com/keichi/binary-parser)

binary-parser 是 keichi 维护的 JavaScript 声明式二进制解析器构建器，通过链式 API 描述整数、位域、字符串、数组、choice、pointer 和自定义嵌套结构，并在首次 parse 时动态生成并缓存解析代码，以获得接近手写解析器的性能；npm 包以 ES module 分发，支持 Node.js（22.12 及以上可用 require 加载 CommonJS）、Bun、Deno 和浏览器。

- 🚀 **声明式构建**：通过 `new Parser()` 或 `Parser.start()` 链式组合字段，调用 `parse` 传入 `Buffer` 或 `Uint8Array` 并返回对象，解析失败抛异常。
- ⚡ **动态编译缓存**：首次 `parse` 时即时生成并编译解析代码，内部缓存；提供 `compile()`、`getCode()`、`sizeOf()`，静态尺寸无法确定时 `sizeOf()` 返回 `NaN`。
- 📦 **整数与浮点**：支持 8/16/24/32/48/64 位有符号和无符号整数及 32/64 位浮点；可用 `le`/`be` 显式指定字节序，64 位整数返回 `bigint`，其余整数返回 `number`。
- 🎯 **位域与字符串**：提供 `bit1` 至 `bit32` 位域，`skipBits(length)` 跳过 1 至 32 个保留位；字符串支持固定/可变长度、零终止和多种编码，`length` 可为数字、字段名或函数，并可用 `greedy`、`stripNull` 等选项。
- 🔄 **数组与映射**：`array` 的元素类型可为内置类型、别名或 `Parser`，必须指定 `length`、`lengthInBytes` 或 `readUntil`；`readUntil` 可接收已解析元素和缓冲区，指定 `key` 时结果按该字段值存为对象。
- 🌐 **分支与嵌套**：`choice` 按 `tag` 字段或函数值从整数键 `choices` 中选择解析器，可设 `defaultChoice`，常与 `array` 组合处理 TLV；`nest` 嵌入内部解析器，`pointer` 跳到绝对 `offset` 解析后回退。
- 🛠️ **递归引用**：`namely(alias)` 为解析器注册别名，使 `array`、`nest`、`choice` 可按名称引用自身或其他解析器，适合递归树；但可能造成循环引用、无限递归，且递归未做尾优化，过深时可能内存泄漏。
- 🧪 **包装转换**：`wrapped` 先按 `length` 或 `readUntil` 读取数据，经 `wrapper` 函数转换为新的 `Buffer`/`Uint8Array`，再交给 `type` 解析器处理，示例用于 `zlib.inflateRawSync` 解压后继续解析。
- ✅ **格式化与断言**：通用选项 `formatter` 可转换解析值；`assert` 为字符串或数字时按 `===` 比较，为函数时以解析值为参数且返回 `false` 抛异常，适合校验魔数。
- 💡 **上下文变量**：顶层调用 `useContextVars()` 后可在解析中访问 `$parent`、`$root` 和 `$index`，解析结束移除；该功能默认关闭以提升性能，`$index` 仅在数组的 `length` 模式可用。
- 🔍 **字节序细节**：`endianness` 可取 `little` 或 `big`，默认大端；该设置也影响 `bit1` 至 `bit32` 的提取顺序，大端从 MSB 到 LSB，小端从 LSB 到 MSB，必要时可将位域放入独立的 `.endianness('big')` 解析器再 `nest`。

### [binary-parser/example 位于 master · keichi/binary-parser · GitHub](https://github.com/keichi/binary-parser/tree/master/example)

`binary-parser` 仓库的 `example` 目录页面展示了 `master` 分支下的示例与样本文件集合，覆盖 Java class、BMP/JPG 图像、ELF32、IP/TCP、MBR、TAR 等二进制格式解析样例，并包含 `Hello.java`、`Hello.class` 及多个测试样本文件。

- 📦 **示例目录**：页面路径为 `binary-parser/example`，当前分支为 `master`，文件列表包含 TypeScript 示例、Java 文件、镜像与测试样本。
- 🧩 **格式覆盖**：示例文件包括 `bmp.ts`、`jpg.ts`、`elf32.ts`、`ip.ts`、`tcp.ts`、`mbr.ts`、`tar.ts` 和 `classfile.ts`，对应多种二进制格式的解析示例。
- 💻 **Java 类文件示例**：目录中有 `Hello.java`、`Hello.class` 和 `hello`，与 `classfile.ts` 同处示例目录，构成 Java 类文件相关示例文件。
- 🧪 **测试样本**：目录列出 `test.bmp`、`test.jpg`、`test.tar` 和 `raspbian.img` 等样本文件，供示例目录配套使用。

### [GitHub - mourner/flatbush：一个用于 JavaScript 中二维点和矩形的极快静态空间索引 🌱 · GitHub](https://github.com/mourner/flatbush)

Flatbush 是一个面向 JavaScript 的极快静态二维点与矩形空间索引库，基于 packed Hilbert R-tree，可在数百万对象上执行快速空间查询，适用于地图、数据可视化和计算几何；相比 RBush 的静态设计带来更快索引与搜索、更低内存占用，并把索引存为单个 ArrayBuffer 以便线程间传输或保存为紧凑二进制文件。

- 🧩 **核心机制**：采用 packed Hilbert R-tree，初始化时指定容量并逐个调用 `add(minX,minY[,maxX,maxY])`，调用 `finish()` 完成索引；索引后不能增删条目。未提供 `maxX/maxY` 时按点处理，`finish()` 时矩形数量须与构造容量一致，否则先 `trim()`，坐标含 `NaN` 会抛错。
- 🛠️ **构造参数**：构造函数为 `new Flatbush(numItems[, nodeSize, ArrayType, ArrayBufferType])`；`nodeSize` 默认 `16`，影响查询性能且对索引速度影响很小；`ArrayType` 默认 `Float64Array`，整数数据可用 `Int32Array`；`ArrayBufferType` 默认 `ArrayBuffer`，需要在线程间共享时可用 `SharedArrayBuffer`。
- 🔍 **查询接口**：`search(minX,minY,maxX,maxY[,filterFn])` 返回与包围盒相交或接触的条目索引，可传入 `filterFn` 过滤，或在回调中直接处理命中项的索引与包围盒坐标；`collides(...)` 在首个匹配处停止，命中很多时比 `search(...).length > 0` 快得多。
- 🎯 **KNN 查询**：`neighbors(x,y[,maxResults,maxDistance,filterFn])` 按距离返回条目索引，即 K 最近邻；`maxResults` 和 `maxDistance` 默认均为 `Infinity`；`filterFn` 只用于筛选潜在结果，不应像 `search` 那样用于处理结果。
- 📦 **索引传输**：索引暴露为 `index.data` 的 `ArrayBuffer` 或 `SharedArrayBuffer`，可通过 `postMessage(index.data,[index.data])` 立即从 Worker 转移到主线程，再用 `Flatbush.from(data[,byteOffset])` 重建；也适合线程共享或保存为文件。
- ⚡ **性能基准**：在 MacBook Pro M1 Pro、Node v26 上运行 `node bench.js`：索引 1,000,000 个矩形 44ms；10,000 次 0.1% 面积查询 146ms；10,000 次 0.1% 面积 `collides` 21ms；10,000 次 1 邻居查询 19ms；10,000 次 100 邻居查询 129ms；1 次 1,000,000 邻居查询 88ms。
- 🌐 **生态扩展**：提供 `geoflatbush` 扩展以支持地理位置；同类点索引库为 KDBush；已有 C++、Rust、C#、Python、Dart 等移植，`geo-index` 提供 Rust 移植与 Python 绑定并保持 ABI 兼容，FlatGeobuf 是受 Flatbush 启发的地理空间格式。
- 📚 **获取与许可**：可通过 `npm install flatbush` 安装并作为模块导入，也可用 jsDelivr 的 ESM 版本或带 `Flatbush` 全局变量的浏览器包；仓库采用 ISC 许可，当前约 1.6k stars、70 forks。

### [发布 v4.8.0 · mourner/flatbush · GitHub](https://github.com/mourner/flatbush/releases/tag/v4.8.0)

flatbush 发布 v4.8.0，重点提升大规模索引与查询性能：对 8192+ 项输入改用 radix sort 使索引构建提速 1.7–2.7 倍，`neighbors(x, y, 1)` 查询约快 25%，并新增 `index.trim()`，同时修复大索引和 `neighbors()` 的若干边界问题。

- 🚀 **索引提速**：对 8192+ 项输入改用 radix sort，索引构建提速 1.7–2.7 倍；示例：1M 项从 105 ms 降至 44 ms，100k 项从 9.1 ms 降至 3.4 ms。
- ⚡ **查询提速**：`neighbors(x, y, 1)` 约快 25%；在 1M 项上执行 10k 次查询从 30.5 ms 降至 22.7 ms。
- 🧩 **新增 trim**：新增 `index.trim()`，将索引收缩到实际已添加的条目数，相关 issue #72。
- 🐛 **大索引修复**：修复 `neighbors()` 在条目数超过约 252M 的索引上崩溃的问题。
- 🐛 **异常后陈旧结果**：修复前一次调用的 `filterFn` 抛出异常后，`neighbors()` 可能返回陈旧条目的问题（#77，感谢 @fbirds5230）。
- ✅ **空结果修复**：修复 `neighbors()` 在 `maxResults = 0` 时仍返回结果的问题，现在返回空结果（#76，感谢 @RealBhupesh）。

### [GitHub - alexreardon/memoize-one：一个仅记住最近一次调用的记忆化库 · GitHub](https://github.com/alexreardon/memoize-one)

memoize-one 是一个只记住最近一次调用参数和结果的 memoization 库，通过放弃通用缓存淘汰策略来避免内存膨胀并保持极小体积。v7 进一步改为仅提供 ES module，更新参数比较为 Object.is，并强化 TypeScript 类型与导出能力。

- 🎯 **设计取舍**：仅缓存最近一次调用的参数和结果，避免 maxAge、maxSize 等通用缓存机制带来的内存膨胀；用新参数调用会覆盖旧缓存，再次使用更早参数会重新计算。适合与 useMemo、useCallback 类似的场景，不适合同时缓存多个结果和参数的通用 memoization。
- 🧩 **默认比较**：默认 areInputsEqual 要求参数数量相同且逐个通过 Object.is 相等；NaN 等于 NaN，+0 与 -0 不相等，和 React useMemo 的依赖比较一致。
- ⚙️ **自定义相等**：可传入 (newArgs,lastArgs)=>boolean 的 EqualityFn，返回 true 时跳过原函数。newArgs 每次都是新数组，不能靠引用相等判断；this 变化时不会调用相等函数。可复用导出的 areInputsEqual，例如忽略最后一个参数。
- 🛡️ **this 处理**：保留并尊重原函数和包装函数的 this 绑定；若 this 按 Object.is 与上次不同，会被视为参数变化并重新执行原函数。
- 🛠️ **清空缓存**：缓存函数带 .clear()，可释放内存或在参数不变时强制重新计算结果。
- ⚠️ **异常行为**：原函数抛出异常时异常会传播，且该次调用不会写入缓存；已有缓存不会被破坏，之后相同参数仍按原缓存命中。
- 📝 **函数属性**：不保留原函数对象上的自定义属性，也不保留 .length，包装后通常为 0；需要时可自行 Object.defineProperty 设置 length。
- 🧠 **类型签名**：MemoizedFn<TFunc> 保留 this、Parameters 和 ReturnType，并增加 clear()；但只保留重载函数的最后一个签名，泛型参数会变成 unknown，类型谓词和断言签名不再收窄。
- 📦 **v7 发布形态**：memoize-one@7+ 仅提供 ES module；浏览器需支持 ES2022，Node.js 中 import 可用，require() 需 Node.js 20.19+ 或 22.12+ 且返回模块对象，应写 const { memoizeOne } = require('memoize-one')；memoizeOne 现为命名导出，默认导出仍保留。
- 🌐 **环境适配**：TypeScript 编译到 CommonJS 时需用 module nodenext（TS 5.8+）或 node20（TS 5.9+），node16/node18 对 require() ES module 报 TS1479；Jest 需额外配置 transformIgnorePatterns 与 Babel，或使用 --experimental-vm-modules。
- 🔄 **升级变化**：v7 用 Object.is 比较参数和 this，+0 与 -0 视为不同；CommonJS 和 UMD 构建移除，禁止 memoize-one/dist/... 深导入，不再支持 IE11 和 Flow 类型，EqualityFn<any> 类型更严格，并新增 areInputsEqual 与 memoizeOne 命名导出。
- ⚡ **体积与性能**：压缩后约 400 B，brotli 后约 226 B，无依赖；基准显示仅缓存最近调用的场景性能接近 micro-memoize，在部分类别排名第二或第三，例如单原始参数约 66,542,477 ops/s。
- ✅ **质量保障**：使用 TypeScript 编写并覆盖 JavaScript 内建类型测试，类型通过 publint 和 arethetypeswrong 检查，采用 ES module 且无依赖。

### [GitHub - cure53/DOMPurify：DOMPurify——仅基于 DOM、超快、极其宽容的 HTML、MathML 和 SVG XSS 清理器。DOMPurify 默认安全，但提供大量可配置项和钩子。演示：· GitHub](https://github.com/cure53/DOMPurify)

DOMPurify 是 cure53 维护的纯 DOM XSS 消毒器，用于净化 HTML、MathML 与 SVG，项目始于 2014 年 2 月，当前版本为 v3.5.0。README 重点说明了 3.4.14 与 3.5.0 对非常规 DOM 输入（非 HTML 解析器构建的节点、声明式 shadow DOM）的安全加固、闭合 shadow root 无法净化的边界、服务端搭配 jsdom 的要求，以及 Trusted Types、hooks、IN_PLACE 失败关闭等配置能力。

- 🚀 **版本与支持范围**：项目始于 2014 年 2 月，已发布至 v3.5.0。v2.5.9 是最后一个支持 MSIE 的版本，MSIE 的安全更新走 `2.x` 分支；在旧浏览器上 DOMPurify 不报错也不做事，原样返回输入，并提供 `isSupported` 供调用方自行兜底。
- 🧩 **基本用法与返回类型**：默认可净化 HTML、SVG 和 MathML，`DOMPurify.sanitize(dirty)` 返回净化后的字符串；可用 `USE_PROFILES: {html: true}` 只保留 HTML。通过 `RETURN_DOM`、`RETURN_DOM_FRAGMENT`、`RETURN_TRUSTED_TYPE` 改变返回类型，`IN_PLACE` 则原地净化节点。
- 🛡️ **非解析器 DOM 输入加固**：自 3.4.14 起，对非 HTML 解析器产生的节点做加固：用 DOM API 或 XML/XHTML 解析（如 `DOMParser` 配合 `application/xhtml+xml` 与 `importNode()`）可构造保留大小写的 `ONERROR` 属性，或让 `<style>` 文本里含元素子节点/自身结束标签；DOMPurify 改为按精确 `Attr` 节点删除属性，并把这些字面文本树视为不安全。3.5.0 又将含元素子节点的 `<textarea>`、`<title>`，以及带子节点的 `<img>`、`<col>` 等 void 元素一并移除。输出侧的上下文混用仍需使用者自行避免。
- ⚠️ **闭合 shadow root 的盲区**：开放 shadow root 会被递归遍历，闭合 shadow root 对任何脚本不可见，DOMPurify 无法净化其内容。`<template shadowrootmode="closed">` 经 `setHTMLUnsafe()` 或 `parseHTMLUnsafe()` 解析后会生成闭合根，因此不要把这类不可信标记先解析成节点再交给 DOMPurify；这影响 `IN_PLACE`、`RETURN_DOM`、`RETURN_DOM_FRAGMENT`，字符串输入和字符串输出不受影响。
- 💻 **服务端运行要求**：服务端需要 DOM，官方推荐最新版 `jsdom`；旧版 jsdom 自身缺陷可导致 XSS，例如 v19.0.0 的已知攻击向量在 v20.0.0 修复。`happy-dom` 目前不被认为安全，与之组合很可能导致 XSS。Cloudflare Workers、Vercel Edge 等无法运行 jsdom 的环境可用第三方 `purify-edge`（基于 parse5 的 window），但官方不维护，测试通过也不构成背书或安全保证。
- 🔑 **Trusted Types 支持**：1.0.9 起支持 Trusted Types API，2.0.0 增加配置开关；启用 `RETURN_TRUSTED_TYPE: true` 时尝试返回 `TrustedHTML`。在 `trustedTypes.createPolicy` 的 `createHTML` 内调用 DOMPurify 需设 `RETURN_TRUSTED_TYPE: false`。未提供 `TRUSTED_TYPES_POLICY` 时 DOMPurify 会自建名为 `dompurify` 的策略，若 CSP 的 `trusted-types` 不允许该名字会触发告警和违规；传 `TRUSTED_TYPES_POLICY: null` 可关闭此回退策略。不要把自己的包装策略再传回 DOMPurify，否则形成递归并抛出 `TypeError`。
- 🔄 **嵌套调用与 hooks 行为变化**：3.5.0 起可在 hook 或 `CUSTOM_ELEMENT_HANDLING.tagNameCheck` 等配置回调中调用 `DOMPurify.sanitize()`，嵌套调用返回后外层会恢复其配置、允许列表和 `DOMPurify.removed`，但 hooks 也会对嵌套调用生效，需自行防递归；此前嵌套调用会覆盖外层配置。3.4.12 起经 `tagNameCheck` 放行的自定义元素也会走 `afterSanitizeElements`（GHSA-c2j3-45gr-mqc4）；3.4.13 起 `IN_PLACE` 下被 hook 摘除的子树仍会被中和。
- ⚙️ **IN_PLACE 失败关闭机制**：传入的根节点必须是允许的标签且未被 DOM clobbering（如子节点名为 `nodeName`、`ownerDocument` 的 `<form>`），否则 DOMPurify 会清空根、剥除其下所有非允许属性（含开放 shadow root）并抛出 `TypeError`。遍历中途抛错也会对根和已摘除子树执行同样的中和。hook 或自定义元素摘除、移动、回插的节点在 `sanitize()` 返回或抛错前都会剥除属性；如果树反复变动，DOMPurify 会清空根并抛错。
- 🛠️ **主要配置项**：支持 `ALLOWED_TAGS`/`ALLOWED_ATTR`、`FORBID_TAGS`/`FORBID_ATTR`、可用函数形式的 `ADD_TAGS`/`ADD_ATTR`、`CUSTOM_ELEMENT_HANDLING`（`tagNameCheck`、`attributeNameCheck`，后者可选接收 `tagName` 第二参数）、`NAMESPACE`、`ALLOW_ARIA_ATTR`、`ALLOW_DATA_ATTR`、`WHOLE_DOCUMENT`、`SANITIZE_NAMED_PROPS`（给 `id`/`name` 加 `user-content-` 前缀）、`KEEP_CONTENT`、`FORCE_BODY`、`PARSER_MEDIA_TYPE`。注意 `<tbody>` 始终被允许且无法禁止，因为浏览器会自行插入，禁止曾导致 `sanitize()` 循环（#365），要整表移除需同时禁止 `table`。
- ⚠️ **模板与 XML 开关风险**：`SAFE_FOR_TEMPLATES: true` 会从文本、注释和属性值中去掉 `{{ ... }}`、`${ ... }` 和 `<% ... %>`，不覆盖其他模板语法和框架指令，属性名不会被清理，hook 通过 `forceKeepAttr` 保留或自行写入的值也不处理；该模式不建议用于生产。字符串输入有保证，DOM 节点输入和 `IN_PLACE` 只是尽力而为。`SAFE_FOR_XML: false` 仅在确实只处理 HTML 时才可设，否则可能导致 XSS。
- 🔗 **URI 与协议白名单**：默认允许相对/协议相对 URL 及 http、https、ftp、ftps、tel、mailto、callto、sms、cid、xmpp、matrix；`ALLOW_UNKNOWN_PROTOCOLS: true` 放开未知协议，`ALLOWED_URI_REGEXP` 可自定义正则（默认模式可用 `sftp` 等方式扩展），官方提醒正则需保持线性时间，因为它会跑在攻击者可控的值上。`ADD_DATA_URI_TAGS` 和 `ADD_URI_SAFE_ATTR` 可扩展 Data URI 与 URI 类属性范围，均有 XSS 风险。
- 🏢 **生态与标准化**：DOMPurify 启发了 HTML Sanitizer API 的诞生，该 API 已在许多浏览器中发布，同样的能力正被纳入 WHATWG HTML 规范。面向整页 Trusted Types 强制执行的 DOMFortify 是独立项目，它安装一个由 DOMPurify 支撑的 `default` 策略并拒绝脚本类 sink，DOMPurify 本身保持专注消毒器的定位。
- 🧪 **测试与 CI 覆盖**：每次推送到发布分支会在 Chromium、Firefox、WebKit 上覆盖 Ubuntu、macOS、Windows 共 9 种浏览器/系统组合，PR 在 Linux 上跑三种引擎；另有矩阵在约三年前的旧引擎快照（约 Chromium 110、Firefox 108、WebKit 16.4）上重跑以捕获回归。还在 `jsdom` 上以 Node.js v20、v22、v24、v26 运行。提供 `npm run test`、`test:jsdom`、`test:browser`、`test:fuzz`、`bench` 等脚本，`/dist` 由 rolldown 构建。
- 📝 **已移除配置**：`SAFE_FOR_JQUERY` 自 2.1.0 起移除，无需替代配置。此外 `DOMPurify.removed` 仅用于观察被丢弃的元素和属性，不可用于任何安全关键决策。

### [GitHub - jsdom/jsdom：用于 Node.js 的各种 Web 标准的 JavaScript 实现 · GitHub](https://github.com/jsdom/jsdom)

jsdom 是面向 Node.js 的纯 JavaScript Web 标准实现，重点模拟 WHATWG DOM 与 HTML 标准，以便在测试和抓取真实网页时提供足够的浏览器环境。当前 README 系统说明了 `JSDOM` 构造器、脚本执行与资源加载的安全配置、虚拟控制台、Cookie 与存储、文档序列化和源码定位等能力，并明确标注导航与布局尚未实现。文档还反映 canvas 可选后端已转向 `@napi-rs/canvas`，以及二进制编码嗅探、未处理异步脚本等使用限制。

- 🚀 **项目定位**：jsdom 用纯 JavaScript 实现多项 Web 标准，主要覆盖 WHATWG DOM 和 HTML，目标是在 Node.js 中模拟足够多的浏览器子集，用于测试和抓取真实 Web 应用；最新版本要求较新的 Node.js，具体见 `package.json` 的 `engines` 字段。
- 🧩 **JSDOM 构造器**：核心入口是 `JSDOM` 命名导出，传入 HTML 字符串后返回带 `window` 的实例，并按浏览器方式补全隐式的 `html`、`head`、`body` 标签；常见用法是解构出 `window` 或 `document` 后直接操作。
- 🛡️ **脚本执行安全**：内嵌脚本默认不执行，启用 `runScripts` 的 `dangerously` 模式才会运行页面内脚本和 `onclick` 等事件处理器属性；外部脚本还需配合 `resources` 设为 `usable`。`outside-only` 会安装独立的 `window.Array`、`window.Promise`、`window.eval` 等全局对象，适合从外部执行脚本。官方强调沙箱并非万无一失，运行不可信代码可能触及 Node.js 环境。
- ⚙️ **资源加载配置**：`resources` 设为 `usable` 可加载 frame、iframe、样式表、脚本和图片，其中脚本还要求 `runScripts` 为 `dangerously`，图片还要求安装 `@napi-rs/canvas`。高级配置支持 `userAgent`、undici 的 `dispatcher` 和 `interceptors`，并提供 `requestInterceptor()` 返回合成响应；jsdom 内同步 `XMLHttpRequest` 会忽略这些自定义。
- 🎨 **视觉模拟**：`pretendToBeVisual` 设为 `true` 后，`document.hidden` 返回 `false`，`document.visibilityState` 返回 `visible`，并启用 `window.requestAnimationFrame()` 与 `window.cancelAnimationFrame()`；jsdom 仍不执行布局或渲染，只是模拟可见状态。
- 💬 **虚拟控制台**：`VirtualConsole` 可接管页面内 `window.console` 输出和 jsdom 自身日志，支持 `forwardTo()` 转发到 Node.js 控制台；`jsdomError` 事件区分 `css-parsing`、`not-implemented`、`resource-loading`、`unhandled-exception`、`xml-parsing` 等错误类型，并可按类型过滤。
- 📦 **Cookie 与存储**：`CookieJar` 基于 tough-cookie，默认启用 `looseMode: true`，可在多个 jsdom 间共享或预先填充 Cookie。`localStorage` 和 `sessionStorage` 受 `storageQuota` 限制，默认每个源 5,000,000 代码单元，超限抛出 `DOMException`；`url`、`referrer`、`contentType` 等构造选项会影响文档 URL、来源和解析方式。
- 🛠️ **文档操作 API**：`serialize()` 返回包含 doctype 的 HTML 序列化结果；`nodeLocation()` 在 `includeNodeLocations` 开启时返回 parse5 的源码位置信息；`getInternalVMContext()` 可在设置 `runScripts` 后获取适合 Node.js `vm` 模块的上下文；`reconfigure()` 可从外部覆盖 `windowTop` 和 `url`，但不会触发实际导航。
- 🌐 **便捷构造 API**：`JSDOM.fromURL()` 会跟随重定向，并由响应决定 URL、内容类型和 referrer，同时处理 `Set-Cookie`；`JSDOM.fromFile()` 默认使用文件 URL，并对 `.xht`、`.xhtml`、`.xml` 默认采用 `application/xhtml+xml`；`JSDOM.fragment()` 通过共享模板文档创建 `DocumentFragment`，不走完整浏览上下文且不接受选项。
- ⚠️ **Canvas 迁移**：canvas 与图片解码的可选后端为 `@napi-rs/canvas` 1.x 的 1.0.13 或更高版本，单独安装 `canvas` 已不能启用支持；原生 `Image` 和 canvas 对象不可互换，字体注册应改用 `GlobalFonts.registerFromPath(path, family)`。Skia 替代 Cairo 后字体、抗锯齿和编码字节可能不同，支持 PNG、JPEG、WebP，其他 MIME 类型回退为 PNG。
- 🔍 **编码嗅探**：构造器可接收 `ArrayBuffer`、`Uint8Array`、`DataView` 等二进制数据，并像浏览器一样扫描 `meta charset` 嗅探编码；`contentType` 中的 charset 会覆盖嗅探结果，但 UTF-8 或 UTF-16 BOM 优先。`fromURL()` 的响应 `Content-Type` 优先，二进制解码还会剥离前导 BOM。
- ⚠️ **已知限制**：异步脚本加载没有可靠的完成信号，需要页面自身回调或轮询元素等变通方案；导航和布局不在 jsdom 范围内，相关 API 可能返回占位值或触发 `not-implemented`。未清理的定时器会保持 Node.js 进程存活并阻止 window 被回收，可用 `window.close()` 终止；调试时可借助 `jsdom-devtools-formatter` 以类似真实 DOM 的形式查看元素。

### [GitHub - redis/ioredis：🚀 一个健壮、注重性能且功能全面的 Node.js Redis 客户端。· GitHub](https://github.com/redis/ioredis)

ioredis 是面向 Node.js 的高性能 Redis 客户端，支持 Cluster、Sentinel、Streams、管道、Lua 脚本、Redis Functions 与二进制 Pub/Sub，并被阿里巴巴等大型公司使用。README 明确了项目的维护定位：项目稳定但按 best-effort 处理问题，新项目推荐改用 node-redis。当前 6.x 默认走 RESP3 并可透明降级到 RESP2，同时提供自动管道、Node.js 诊断通道遥测、阻塞命令客户端超时，以及仍处实验阶段的 Redis 8.10 HIMPORT 受管 fieldset 支持，另外预告了两项下一主版本的破坏性变更。

- 🏢 **项目定位**：ioredis 定位为稳定项目，只对相关问题做 best-effort 维护，贡献仍会被评估和合并；README 明确建议新项目使用 node-redis，后者为 MIT 开源、从头重写并持续维护，且支持 hash-field expiration、Redis Stack 与 Redis 8 的搜索、JSON、时序和概率数据结构能力。
- 📦 **版本支持**：支持 Redis >= 2.6.12 并完全兼容 Redis 7.x；6.x（main 分支）要求 Node.js >= 20 与 Redis 6.2 ~ latest，5.x 要求 Node.js >= 12、覆盖 Redis 2.6.12 ~ latest，4.x 要求 Node.js >= 8、覆盖 Redis 2.6.12 ~ 7。
- 🧩 **RESP3 默认**：默认 `protocol: 3`，连接时发送 `HELLO 3`，服务端不支持时（Redis < 6）透明降级为 RESP2；`replyMapping` 仅在 protocol 3 下有效，`legacy` 将 map 表示为扁平数组、double 为字符串，`resp3` 则返回普通对象和数字，`resp3` 搭配 `protocol: 2` 会在构造时抛错。Buffer 变体始终返回值 buffer，但 `resp3` 下 map 键固定按 UTF-8 字符串解码，`hgetallBuffer` 的字段名在两种映射下都是字符串。
- ⚡ **自动管道**：设置 `enableAutoPipelining: true` 后，一个事件循环内发出的命令会自动进入 ioredis 管理的管道并在循环结束时一次性发送，避免队头阻塞；基准测试中单节点从 174.62 op/sec 提升到 233.33 op/sec，3 主 3 从集群从 164.05 提升到 235.31 op/sec，官方称提升约 35%~50%。集群模式下按服务该 slot 的节点各建一条管道，显式 `pipeline()` 与 `multi()` 批次仍单独发送。
- 🔍 **诊断通道**：通过 Node.js `diagnostics_channel` 发布 `ioredis:command`、`ioredis:batch`、`ioredis:connect` 遥测，基于 `TracingChannel#tracePromise()` 发出 start、end、asyncStart、asyncEnd、error 子事件，订阅名为 `tracing:<name>:<event>`；需 Node.js >= 18.19.0，旧版本静默不可用且无开销。参数按 `@opentelemetry/redis-common` 规则脱敏，`SET` 值、`AUTH` 密码等替换为 `?`，`GET`、`DEL` 等只读命令保留参数，未列出或自定义命令默认全部脱敏。
- 🧪 **实验特性**：受管 HIMPORT fieldset 仍为实验特性，需 Redis 8.10 或更新版本，通过 `himportFieldsets` 配置 name 与 fields；Cluster 客户端需在顶层选项传入而非 `redisOptions` 下。集群上直接调用 `HIMPORT PREPARE`、`DISCARD`、`DISCARDALL` 会广播到所有当前 master 并等待全部回复，任一失败即拒绝；显式 pipeline 内这些命令仍绑定单连接。后台准备失败不阻止连接变为 ready，独立与 Sentinel 客户端通过 `error` 事件报告，Cluster 通过 `node error` 报告。
- 🛡️ **阻塞超时**：`blockingTimeout` 为 opt-in，默认关闭，仅当设为正数毫秒才为 `blpop`、`brpop`、`bzpopmin`、`bzmpop`、`blmpop`、`xread`、`xreadgroup` 等阻塞命令启用客户端超时，用于应对 TCP 假死；有限超时命令按命令超时加 `blockingTimeoutGrace`（默认 100ms）设截止时间，超时以 `null` 返回，永久阻塞（timeout 0 / `BLOCK 0`）则以 `blockingTimeout` 兜底。
- 🌐 **集群读写与订阅**：`scaleReads` 可取 `master`（默认）、`all`、`slave` 或自定义函数决定读命令落点；`subscriberNodeRole` 独立于 `scaleReads`，控制经典 Pub/Sub 专用订阅连接可选 `all`、`master`、`slave`，无合格节点时集群仍就绪但订阅命令被拒绝。分片 Pub/Sub 需先开启 `shardedSubscribers: true` 再使用 `ssubscribe`/`spublish`，单次 `ssubscribe` 的频道须落在同一 hash slot，订阅连接按 `shardedSubscriberHealthCheckInterval`（默认 10000ms，最小 1000，可设 `null` 关闭）发 `PING` 探活。
- ⚠️ **弃用预告**：`import Redis from "ioredis"` 写法虽仍支持，但将在下一主版本弃用，建议改用 `import { Redis } from "ioredis"`；README 中的 `RedisCloudFixed`、`RedisCloudFlexible` 等 TLS profiles 也将在下一主版本弃用，官方建议显式提供 TLS 选项。

### [GitHub - jeffijoe/awilix：极为强大的 Node.JS 控制反转（IoC）容器 · GitHub](https://github.com/jeffijoe/awilix)

Awilix 是一个用 TypeScript 编写、面向 JavaScript/Node 的 IoC/DI 容器，强调无需特殊注解即可编写可组合、可测试的代码，并通过注册、解析、作用域和生命周期管理将应用代码与 DI 机制解耦。README 说明了 PROXY/CLASSIC 注入模式、TRANSIENT/SCOPED/SINGLETON 生命周期、Awilix 10 严格模式、自动加载与 TypeScript 类型推断工具，以及 v3 起的 dispose 和浏览器构建等能力与限制。

- 🧩 **核心定位**：Awilix 是 JavaScript/Node 的依赖注入容器，用 TypeScript 编写，目标是无需特殊注解实现可组合、可测试的软件；核心 API 包括 `createContainer()`、`register()`、`resolve()` 和 `cradle` 代理。
- ⚙️ **基本用法**：容器通过 `register()` 注册模块，用 `asClass()`、`asFunction()`、`asValue()`、`aliasTo()` 指定解析方式；`container.cradle.foo` 等价于 `container.resolve('foo')`，默认注入模式为 `PROXY`，README 建议开启 `strict`。
- 🔄 **生命周期**：支持 `Lifetime.TRANSIENT`（默认，每次解析新实例）、`SCOPED`（同一作用域复用，适合请求级状态）和 `SINGLETON`（根容器缓存）；若长生命周期模块依赖短生命周期模块，可能保留过期依赖，严格模式会报 `AwilixResolutionError`。
- 🛡️ **严格模式**：Awilix 10 的严格模式启用正确性检查：单例或作用域注册依赖 transient 非值注册时报错；禁止在非根作用域注册单例；单例只使用根容器注册解析；可用 resolver 选项 `isLeakSafe: true` 排除特定解析器的生命周期泄漏检查。
- ⚡ **注入模式**：`InjectionMode.PROXY` 为默认，向函数/构造函数注入 cradle 代理，支持解构并便于测试；`InjectionMode.CLASSIC` 解析函数/构造函数参数名匹配注册，初始化成本略高但解析更快，代码压缩后会失效；可按容器、解析器或自动加载模块配置，最具体配置优先。
- 📦 **自动加载**：`loadModules()` 通过 glob 批量注册模块，默认读取默认导出，非默认导出需设置 `RESOLVER`；支持 `formatName: 'camelCase'` 或函数、统一或按 glob 指定 `resolverOptions`，`opts.esModules` 会让其异步返回 Promise；依赖 `fast-glob`，不适用于 Webpack、Rollup、esbuild、Browserify 等打包器，`listModules()` 同样依赖 glob。
- 🔑 **局部注入**：Awilix 2.5 引入按模块局部注入，可通过 `.inject(() => ({ timeout: 2000 }))` 或 `injector` 选项给单个注册提供额外值；实现上会包装 cradle 代理，因此拿到该 cradle 的对象也能访问这些局部值。
- 🧠 **内联选项**：Awilix 2.8 支持在模块上通过 `RESOLVER` Symbol 内联设置 `lifetime`、`injectionMode` 和 `name`；`name` 仅被 `loadModules()` 用于注册名，`RESOLVER` 也可让非默认导出被自动加载识别。
- 🛠️ **类型工具**：提供 TypeScript 工具类型 `InferCradleFromResolvers`、`InferCradleFromContainer` 和 `InferResolverType`，可从 resolvers、容器或单个 resolver 推断 cradle/解析类型；README 仍建议为服务定义独立的 options 类型，以避免应用代码耦合 DI 容器。
- 🔧 **资源释放**：v3.0 起 `container.dispose()` 返回 Promise，清理自身缓存并调用 scoped/singleton 的 disposer，默认 `DisposalMode.CONCURRENT` 并发执行，也可用 `SERIAL` 按缓存逆序等待；不会释放 scope，也不释放父容器缓存，清理中的错误汇总为 `AggregateError`，释放完成后容器不能再解析依赖。
- 🌐 **浏览器支持**：v3 起提供 CommonJS、Node ESM、浏览器 ESM 和 UMD 四种构建，`package.json` 字段供打包器自动选择；浏览器构建不支持 `loadModules` 和 `listModules`，最低要求 Chrome 85、Firefox 79、Edge 85、Opera 71、Safari 14、iOS Safari 14，不支持 IE。
- 🏢 **生态**：生态包含 `awilix-express`、`awilix-koa`、`awilix-router-core`、`fastify-awilix`、`awilix-vite`、`awilix-modular` 等绑定或扩展，以及提供 eager injection、异步初始化、按标签查找依赖的 `awilix-manager`。
