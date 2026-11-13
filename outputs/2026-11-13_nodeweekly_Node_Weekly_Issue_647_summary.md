### [src: experimental green threads implementation by jasnell · Pull Request #67288 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67288)

**原文标题**: [src: experimental green threads implementation by jasnell · Pull Request #67288 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67288)

该 PR（#67288，Draft）由 jasnell 发起，为 Node.js 引入实验性的 green threads：一种轻量级 worker，每个实例拥有独立 V8 isolate，但没有完整 Node.js 环境和 API；它们共享一个最多 8 个物理线程的池，通过消息、RPC 或模块导出接收任务，并支持 CPU 时间/内存限制、终止和预热池。其在内存占用、启动速度、多实例密度和沙箱隔离方面明显优于 worker threads，但单条消息速度略慢，且无法利用超过 8 个核心；更适合多租户、插件系统和运行不可信代码等场景。

- 🧵 核心定义：green thread 是轻量级 worker，每个有独立 V8 isolate，但不绑定单独 OS 线程，也不带完整 Node.js Environment。
- ⚙️ 调度模型：大量 green threads 共享最多 8 个池线程；每个任务在独立调用上下文中运行，避免一个实例长期占用物理线程。
- 📨 通信方式：宿主可通过 `postMessage()`、RPC、`env` 回调和 ES 模块 `exports` 与 green thread 交互。
- 🔒 资源与安全：支持 `maxTaskCpuTimeMs`、`maxCpuTimeMs`、`maxMemoryMb` 等限制，可强制终止失控代码；默认不暴露 `fs`、`net`、`child_process` 等 Node.js API。
- 🚀 预热池：`setWarmPoolSize(n)` 可预创建 isolate，使启动耗时约降至 20 微秒，适合大量短生命周期实例。
- 📉 内存优势：每实例内存比 worker 低约 1.5–6.5 倍；1000 个租户约用 1 GB，而 worker 方案约 6.7 GB。
- ⚡ 多实例性能：1000 个 green threads 共享 8 个 OS 线程，基准中每秒请求数比 worker 高约 15–20%。
- 🐢 单消息开销：顺序消息往返约 57,000 次/秒，worker 约 61,000 次/秒，worker 约快 5%。
- 🧮 CPU 密集任务：同等并行度下速度接近；但 green thread 池上限为 8 线程，重并行计算仍应使用 worker。
- 🧩 插件宿主：同一插件系统用 green threads 约 43 行，用 worker 约 155 行；后者需自行处理模块加载、双向 RPC、错误转发和资源限制。
- 🧭 适用场景：多租户/Serverless 小型处理器、插件扩展系统、用户脚本、需要 CPU/内存限制且大量短命或空闲的代码。
- 🛠️ worker 仍适用：需要 Node.js API 或依赖这些 API 的 npm 包、跨全部核心的重计算、阻塞式同步等待，以及少量长期实例。
- ⚠️ 注意事项：该实现仅为实验性，需 `--experimental-green-threads`；`Atomics.wait()` 等同步阻塞被禁用；部分 JIT 优化代码可能忽略终止，需依赖 watchdog 放弃 isolate。
- 💬 讨论要点：作者强调优势来自对 worker 模型的“减法”——不绑定单个物理线程、不创建完整 Node.js 环境；因此并非简单给现有 worker 增加功能即可获得同等收益。

---

### [更新日志直播 | Sentry](https://sentry.io/resources/changelog-live/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=brand-fy27q4-changeloglive&utm_content=newsletter-primary-register)

**原文标题**: [Changelog Live | Sentry](https://sentry.io/resources/changelog-live/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=brand-fy27q4-changeloglive&utm_content=newsletter-primary-register)

Sentry 将举办 Changelog Live 直播活动，展示最新版本及可能错过的更新，内容涵盖错误与性能问题的调试、AI 工作流、SDK 与集成更新，并提供录播和实时问答。

- 🎥 Sentry Changelog Live 将以直播形式展示最新发布内容，并回顾一些容易错过的更新。
- 🔍 更快排查问题：提供更丰富的错误上下文、更智能的问题分类、更强的搜索能力，以及可跨技术栈拉取数据的升级版 Seer Agent。
- 🤖 AI 工作流新动态：展示 Sentry 如何融入 AI 工作流，包括用 Seer 修复生产问题，以及追踪和调试你构建的智能体。
- ⚙️ 技术内幕速览：快速介绍 SDK 更新、新集成和告警改进。
- ❓ 活动将提供录播，并安排实时问答环节，可提前保存席位了解最新内容。
- 🎙️ Sentry 还赞助了开发者播客 Syntax，可在常用收听平台收听。

---

### [Node.js — 2026年11月11日星期三 安全版本发布](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases)

**原文标题**: [Node.js — Wednesday, November 11, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases)

overview summary
Node.js 项目于 2026 年 11 月 11 日发布 26.x、24.x、22.x 安全版本，修复依赖及多个 HTTP/2、TLS、权限模型等漏洞，最高严重性为 HIGH，建议尽快升级。

- 🗓️ 安全版本于 2026 年 11 月 11 日或稍后发布，覆盖 26.x、24.x、22.x 发布线。
- 📦 更新依赖以修复公开漏洞：llhttp（22.x/24.x/26.x）、undici（24.x/26.x）、sqlite（22.x/24.x）。
- 🚨 最高严重性为 HIGH；26.x、24.x、22.x 三条发布线的最高修复级别均为 HIGH。
- 🧨 CVE-2026-123863（高危）：HTTP/2 会话拆除可达断言，未认证客户端可中止服务器。
- 🧨 CVE-2026-123864（高危）：HTTPS 零长度 TLS 写重入 llhttp，可能泄露堆内存，包括 TLS 私钥等。
- 🧨 CVE-2026-123865（高危）：HTTP/2 关闭期间触发协议错误，导致会话和文件描述符永久泄漏。
- 🧨 CVE-2026-123866（高危）：HTTP/2 流拆除 UAF，可能向对端发送已释放的响应内存。
- 🧨 CVE-2026-126051（高危）：TLS 延迟握手回调导致远程可触发未捕获异常并终止进程。
- 🧨 CVE-2026-123872（高危）：TLS 1.2 重协商可单方面更改 servername，绕过客户端证书认证。
- 🧨 CVE-2026-123874（高危）：HTTP/2 respondWithFile()/respondWithFD() 流在待写时重置导致 UAF。
- ⚠️ CVE-2026-123828（中危）：session.altsvc() 长 origin 触发一字节堆溢出。
- ⚠️ CVE-2026-123867（中危）：仅 CA 的 SNI 客户端 CA 回退到默认 CA，绕过按主机 mTLS 授权。
- ⚠️ CVE-2026-123868（中危）：HTTP/2 未排空流入站数据不计入 maxSessionMemory，可耗尽服务器内存。
- ⚠️ CVE-2026-123871（中危）：ERR_PROXY_INVALID_CONFIG 错误信息泄露代理凭据。
- ⚠️ CVE-2026-123877（中危）：https.Agent 跨策略 TLS 会话复用导致证书验证绕过。
- ⚠️ CVE-2026-123875（中危）：取消 respondWithFile() 下载触发 StreamPipe NULL 解引用并崩溃。
- 🕵️ CVE-2026-123829（低危）：递归 fs.watch 的 Permission Model 绕过，泄露被拒绝后代的名称。
- 🧩 CVE-2026-123862（低危）：zlib params() 加 destroy() 抛出不可捕获 ERR_INTERNAL_ASSERTION。
- 🧩 CVE-2026-106071（低危）：Permission Model 通配符 radix 查找导致文件系统过度授权。
- ⬇️ 发布版本：Node.js v22.23.5、v24.22.3、v26.13.1。
- 🛡️ 所有活跃发布线受影响，EOL 版本也会受影响；应使用受支持的最新版本。
- 🤝 维护 LTS 之后的商业支持可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获得。
- 📚 可通过 Node.js 安全策略、漏洞报告流程和 nodejs-sec 邮件列表持续跟踪更新。

---

### [Node.js — Node.js 26.13.1（长期支持版）](https://nodejs.org/en/blog/release/v26.13.1)

**原文标题**: [Node.js — Node.js 26.13.1 (LTS)](https://nodejs.org/en/blog/release/v26.13.1)

Node.js 26.13.1（LTS，代号“Lithium”）于 2026-11-11 发布，由 Antoine du Hamel 发布，是一次安全更新，修复了多个高、中、低危漏洞，并更新了若干依赖。

- 🔐 高危修复集中在 http2 与 tls/http：释放已移除流的头部、防止空写入触发嵌套解析器执行、检测 nghttp2 放弃的流、在套接字写入完成前保留缓冲区，以及修复可远程触发的 TLS 服务端崩溃。
- 🛡️ TLS 安全加固：禁止无 session id 上下文的 mTLS 恢复、禁止重协商或 HRR 更改 SNI、禁止 TLS 恢复更改 SNI。
- ⚠️ 中危问题涉及 http2 的 ALTSVC 缓冲区溢出、SNI 上下文 CA 应用、入站 DATA 计入 maxSessionMemory、代理 URL 错误中凭据脱敏、取消流上的空写请求保护，以及 https Agent TLS 策略键隔离。
- 🧩 低危问题包括递归 fs.watch 权限泄漏、zlib 销毁后参数回调处理，以及权限检查堆快照目标。
- 📦 依赖更新：brotli 1.2.1、llhttp 9.4.4、sqlite 3.54.1、undici 8.12.4。
- 💻 提供 Windows、macOS、Linux、AIX、ARMv8 等多平台安装包和二进制文件，以及源码包、文档和 SHASUMS/PGP 签名校验信息。

---

### [Node.js — Node.js 24.22.3（长期支持版）](https://nodejs.org/en/blog/release/v24.22.3)

**原文标题**: [Node.js — Node.js 24.22.3 (LTS)](https://nodejs.org/en/blog/release/v24.22.3)

Node.js 24.22.3 'Krypton' (LTS) 于 2026-11-11 发布，由 @aduh95 发布，是一次安全更新，修复 HTTP/2、TLS/HTTP、权限与 zlib 等漏洞，并更新多项依赖，提供多平台下载及校验信息。

- 🛡️ 这是安全版本，建议使用 Node.js 24 LTS 的用户尽快升级。
- 🚨 高危修复包括 CVE-2026-123863/123864/123865/123866/123872/123874/126051，涉及 HTTP/2 头与流/缓冲区管理、空写入嵌套解析、mTLS 恢复、SNI 变更限制及远程 TLS 服务器崩溃。
- 🟠 中危修复包括 CVE-2026-123828/123867/123868/123871/123875/123877，涉及 ALTSVC 缓冲区溢出、SNI 上下文 CA、HTTP/2 内存计费、代理凭据脱敏、取消流写入防护、HTTPS Agent TLS 策略隔离。
- 🟢 低危修复包括 CVE-2026-123829/123862/123873，涉及递归 fs.watch 权限泄露、zlib 销毁后回调处理、堆快照目标检查。
- 📦 依赖更新：brotli 1.2.1、llhttp 9.4.4、SQLite 3.54.1、undici 7.30.2。
- 💻 提供 Windows、macOS、Linux、AIX、ARM 等多平台安装包、二进制及源码下载。
- 🔐 发布页附 SHA256 校验和与 PGP 签名，下载后应验证文件完整性。

---

### [Node.js — Node.js 22.23.5（长期支持版）](https://nodejs.org/en/blog/release/v22.23.5)

**原文标题**: [Node.js — Node.js 22.23.5 (LTS)](https://nodejs.org/en/blog/release/v22.23.5)

Node.js 22.23.5（LTS，代号 “Jod”）于 2026-11-11 发布，由 @aduh95 发布，是一次安全版本更新，主要修复 HTTP/2、TLS、HTTP 等模块中的多项安全漏洞，并更新相关依赖。

- 🔐 本次为安全发布，包含多个 High、Medium、Low 风险等级的安全修复。
- 🚨 高风险问题集中在 HTTP/2 与 TLS，涉及流和头部释放、缓冲区保留、nghttp2 废弃流检测、空写入导致的嵌套解析、mTLS 会话恢复及 SNI 变更限制等。
- 🛡️ 中风险修复包括 HTTP/2 ALTSVC 缓冲区溢出、SNI 上下文 CA 应用、入站 DATA 内存计费、无效代理 URL 凭据脱敏、取消流空写入保护及 HTTPS Agent TLS 策略键隔离等。
- 🧹 低风险修复涉及递归 `fs.watch` 权限信息泄露、`zlib` 销毁后的参数回调处理及堆快照目标路径检查。
- 📦 依赖更新包括 `llhttp` 升级至 9.4.4，`sqlite` 升级至 3.54.1。
- 💻 提供 Windows、macOS、Linux、AIX、ARM 等多平台安装包、二进制文件及源码下载。
- ✅ 发布页同时提供文档、SHASUMS 校验和及 PGP 签名信息。
- ⏮️ 相邻版本为 Node.js 24.22.3（LTS）与 Node.js 27.0.0-alpha.0.0.0（Alpha）。

---

### [发布 v8.12.4 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v8.12.4)

**原文标题**: [Release v8.12.4 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v8.12.4)

本次 Undici v8.12.4 发布重点是一次安全修复版本，共修复 6 个漏洞（1 个高危、5 个中危），主要涉及重定向与缓存交互导致的缓存污染/凭据泄露、缓存重放异常导致进程退出，以及 `fetch()` 的 SRI 校验绕过；同时包含文档、类型、HTTP/2、mock、fetch 与依赖更新。

- 🔒 高危：CVE-2026-116592 / GHSA-mqg3-3v4r-cm32，重定向链最终响应可能按原始请求键缓存，未逐跳应用源、缓存策略、新鲜度和 `Vary` 要求，可能导致缓存污染或跨用户响应暴露；修复为逐跳校验、合并 `Vary`、采用最严格的新鲜度/陈旧策略，并使旧版 SQLite 持久化条目失效。
- 🍪 中危：CVE-2026-120474 / GHSA-7xg3-fphp-28hg，`compose(redirect(), cache())` 可能将同源重定向中依赖凭据的响应存到原始 URL 下；带 `Authorization`、`Cookie`、`Proxy-Authorization` 的重定向请求不再存入原始别名键。
- 🔁 中危：CVE-2026-116630 / GHSA-5rm8-gv32-r954，跨源重定向再验证时，目标源的 `304 Not Modified` 可能验证原源缓存响应；现会校验再验证目标与缓存 URL、验证器与存储表示一致后再回放缓存体。
- 🧹 中危：CVE-2026-120415 / GHSA-9v6h-8rgp-m69f，重定向拦截器在请求头为 `[name, value]` 数组时未正确移除凭据，可能把凭据发往跨源重定向目标；现同时处理元组数组和扁平头数组。
- 💥 中危：CVE-2026-120222 / GHSA-3g9m-rv3r-w5w2，缓存回放期间下游处理器异常可能变成未捕获异常/未处理 Promise 拒绝并终止进程，包括 `dump` 大小限制、`decompress` 的 `Content-Encoding` 过多、异步缓存存储失败、`304` 后缓存体回放；现作为请求错误上报。
- 🛡️ 中危：CVE-2026-120423 / GHSA-r4pc-4jcp-7pqc，`fetch()` 在完整性元数据被空格以外 ASCII 空白（如制表符）分隔或包围时可能跳过 SRI 校验；现按所有 ASCII 空白拆分后再进行 SHA-256/384/512 校验。
- 🛠️ 其他变更包括：文档澄清与错别字修复、mock 忽略查询串前尾斜杠、`DecoratorHandler` 放行 1xx 临时响应、`FormData` 类型声明、SQLite 缓存忽略 `SQLITE_BUSY`、HTTP/2 释放流错误接收器与 GOAWAY 竞态重放、RISC-V 禁用 WASM SIMD、fetch 异步可迭代体惰性读取与 GC 后中止传播等。
- 📦 依赖与构建更新：升级 `eslint`、`neostandard`、`cronometro`、`@fastify/busboy`、`undici`、`node-forge`、`jsondiffpatch`、`upload-artifact`、`harden-runner` 等。
- 👥 版本由 `github-actions` 于 11 月 5 日发布；包含 8 位新贡献者，完整变更对比为 `v8.12.3...v8.12.4`，贡献者包括 `mcollina`、`hrw` 等 14 人。

---

### [Node.js 27 有哪些新特性](https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-27/)

**原文标题**: [What's new in Node.js 27](https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-27/)

Node.js 27 首个 Alpha 于 2026 年 10 月发布，采用新的年度发布节奏：10 月进入 Alpha，2027 年 4 月成为 Current，2027 年 10 月转为 LTS。该版本带来 V8 15.6 的迭代器与数学新 API，新增 `node:net/promises`、取消 `node:vfs` 实验标志，并调整 HTTP、内存与权限模型默认行为；同时包含多项需要注意的破坏性变化。生产环境在此之前仍应使用 LTS，库作者可尽早加入 CI 测试。

- 🗓️ 发布节奏变化：取消奇偶版本号规则，每年发布一个大版本且都会成为 LTS；Node.js 27 计划 2027 年 4 月进入 Current、2027 年 10 月成为 LTS，支持至 2030 年 4 月。
- 🧩 Iterator 新能力：新增 `Iterator.zip()`、`zipKeyed()`、`join()`、`includes()`，可惰性配对并行序列、按列组合对象、直接拼接或查找，避免创建中间数组。
- ➗ `Math.sumPrecise()`：使用高精度累加减少浮点求和误差，但不会把 JavaScript 数字变成十进制精确数；金额计算仍建议使用整数分或十进制库。
- 🌐 `node:net/promises`：新增 `listen()` 与 `connect()`，并让 `net.Server` 成为异步可迭代对象，便于用 `async/await` 构建 TCP 服务器和套接字逻辑。
- 📦 `node:vfs` 取消实验标志：可创建内存虚拟文件系统并挂载，供普通 `node:fs`、`import`、`require()` 使用；支持 `using` 自动卸载和 CLI 的 `--vfs-load`。
- 🧪 核心库升级：新增 `fs.mkstemp()` 原子创建临时文件，`fs.glob()` 改为原生 C++ 实现；Permission Model 增加 `--allow-env`；测试运行器 watch 模式稳定，并加入 Jest 风格 mock 简写。
- ⏱️ HTTP 默认值调整：`http.Server` 的 `keepAliveTimeout` 从 5 秒提高到 65 秒，降低代理场景下的 502 风险；HTTP/2 增大默认流控窗口。
- 🛡️ `req.headers` 与 `req.trailers` 改为 null 原型：避免继承属性与原型污染风险；调用 `hasOwnProperty()` 会抛错，应改用 `Object.hasOwn()`。
- ⚙️ 运行时依赖升级：V8 15.6、OpenSSL 4.1.0、Undici 8.12、SQLite 3.54、npm 12.1.0，`NODE_MODULE_VERSION` 更新为 153；排序、`await`、`JSON.parse()` 等有性能改进。
- 💾 默认堆上限提高：未指定 `--max-old-space-size` 时，老生代堆上限为物理内存一半并限制在 256MB–4GB；8GB 机器默认从 2GB 提升到 4GB，`Buffer`/`ArrayBuffer` 也纳入 V8 全局分配限制。
- ⚠️ 破坏性变化：`v8.serialize()` 新格式旧版 Node.js 无法反序列化；堆快照更大且包含完整脚本源码；`Math` 结果、`Math.random()` 序列、排序比较器调用次数可能变化；`node:domain`、`_http_*`、`_tls_*`、OpenSSL 1.x/engine 等被废弃或移除。
- ✅ 使用建议：2027 年 4 月前生产环境继续使用 LTS；库作者应尽早将 Node.js 27 加入 CI；本地可试验 `Iterator.zipKeyed()`、`Math.sumPrecise()`、`node:net/promises` 和 `node:vfs`。

---

### [Node.js 27 有哪些新特性](https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-27/#heads-up-nodejs-27-breaking-changes)

**原文标题**: [What's new in Node.js 27](https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-27/#heads-up-nodejs-27-breaking-changes)

overview summary  
Node.js 27 于 2026 年 10 月发布首个 Alpha，采用新的年度发布节奏：每年一个大版本，且所有大版本最终都会进入 LTS。首个 Alpha 带来 V8 15.6、迭代器新能力、`node:net/promises`、解禁的 `node:vfs`、核心模块与默认值更新，同时包含若干破坏性变更；生产环境在 2027 年 4 月进入 Current、10 月进入 LTS 前应继续使用 LTS。

- 📅 **发布节奏变化**：Node.js 27 是首个按新计划发布的版本，2026 年 10 月进入为期 6 个月的 Alpha，2027 年 4 月成为 Current，2027 年 10 月进入 LTS，并支持至 2030 年 4 月；奇数版本也可成为 LTS。
- 🔗 **迭代器新 API**：V8 15.6 新增 `Iterator.zip()`、`Iterator.zipKeyed()`、`Iterator.prototype.join()`、`Iterator.prototype.includes()`，可惰性配对、按键组合、拼接和查找同步迭代器，避免中间数组。
- 🧮 **更精确求和**：`Math.sumPrecise()` 使用高精度累加器，仅在最后舍入一次，可减少浮点累加误差；但它不会把 JavaScript 数字变成精确十进制数，金额计算仍建议用整数分或十进制库。
- 🌐 **TCP 异步化**：新增实验性 `node:net/promises`，提供 `listen()`、`connect()`，并让 `net.Server` 成为异步可迭代对象，便于用 `async/await` 构建 TCP 服务器和客户端。
- 🗂️ **虚拟文件系统解禁**：`node:vfs` 不再需要 `--experimental-vfs`，可创建内存文件系统并挂载到保留命名空间，让常规 `node:fs` 和模块加载直接读取；也支持 `--vfs-load` 加载目录或 ZIP。
- 🔐 **文件与权限增强**：新增原子临时文件 API `fs.mkstemp()`、`fs.mkstempSync()`、`fsPromises.mkstemp()`；`fs.glob()` 移植为原生 C++；Permission Model 新增 `--allow-env`，未授权环境变量会在启动时被清除。
- 🧪 **测试运行器更新**：`node --test --watch` 进入稳定状态；`--test-forbid-only` 可阻止误提交 `.only`；mock 增加 `mockReturnValue()`、`mockResolvedValue()`、`mockRejectedValue()`、`mockThrownValue()` 等简写。
- 🚀 **HTTP 默认值调整**：`http.Server` 的 `keepAliveTimeout` 从 5 秒提高到 65 秒，减少代理复用连接时出现 502 的概率；HTTP/2 默认流控窗口增大；`req.headers` 和 `req.trailers` 改为 null 原型对象。
- ⚙️ **运行时与依赖升级**：默认老生代堆上限改为物理内存的一半，并在 256 MB 到 4 GB 间钳制，8 GB 机器默认从 2 GB 提升到 4 GB；`Buffer`/`ArrayBuffer` 内存纳入 V8 全局分配限制；升级 OpenSSL 4.1、Undici 8.12、SQLite 3.54、npm 12.1，`NODE_MODULE_VERSION` 为 153。
- ⚠️ **主要破坏性变更**：`req.headers.hasOwnProperty()` 会抛错，应改用 `Object.hasOwn()`；多进程部署可能需显式设置 `--max-old-space-size`；Node.js 27 生成的 `v8.serialize()` 数据旧版本无法反序列化；堆快照更大且包含完整脚本源码。
- 🔄 **其他兼容性风险**：部分 `Math` 结果、`Math.random()` 固定种子序列、`Array.prototype.sort()` 比较器调用次数可能变化；`node:domain` 运行时弃用，私有 `_http_*` 弃用、`_tls_*` 移除，OpenSSL engines 和 OpenSSL 1.x 支持移除，Intel macOS 降为实验支持。
- 🛡️ **升级与使用建议**：2027 年 4 月前生产环境继续使用 LTS；库作者应尽快把 Node.js 27 Alpha 加入 CI 以提前发现破坏性变更；本地可试用 `Iterator.zipKeyed()`、`Math.sumPrecise()`、`node:net/promises` 和 `node:vfs`。

---

### [lib: enable web worker api by default by avivkeller · Pull Request #65323 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65323)

**原文标题**: [lib: enable web worker api by default by avivkeller · Pull Request #65323 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65323)

overview summary
- 🧩 Node.js 合并 PR #65323，默认启用 Web Worker API，这是 semver-major 破坏性变更，计划在下一个主版本发布。
- 👤 该 PR 由 avivkeller 提交，panva、aduh95、mcollina、gurgunday 等人参与评审，共有 7 名参与者。
- 🏷️ 该 PR 被添加 semver-major、c++、config、needs-ci、commit-queue-squash、experimental 等标签。
- 📝 评审要求补充 changes 条目，并更新 `doc/api/globals.md` 中 `Worker` 类的实验性说明和相关 CLI 参数链接。
- 🧪 评审中讨论了回归测试需求；后续确认现有测试已有较合理覆盖，未额外阻塞合并。
- ✅ Codecov 报告显示所有修改且可覆盖的代码行均被测试覆盖，项目覆盖率为 90.69%，较基线提升 0.01%。
- 🔁 PR 经历多次 force-push、CI 运行和重新批准，最终 68 项检查全部通过。
- 🚀 2026 年 11 月 11 日合并到 `nodejs:main`，合并提交为 `77e6379`。
- ⚠️ 合并时未默认在首次使用时发出实验性警告；如需要，可在后续 PR 中补充。

---

### [Val Town 正在逐步停止运营 | Val Town 博客](https://blog.val.town/winding-down)

**原文标题**: [Val Town is winding down | Val Town Blog](https://blog.val.town/winding-down)

Val Town 宣布将逐步停止运营，原因是无法在云计算领域继续竞争；团队将暂停计费、为现有订阅免费续服，并提供迁移指南与支持渠道，同时按时间表进入只读、全面停服及开源阶段。

- 🛑 Val Town 已做出逐步关停的艰难决定，并向社区致歉与致谢。
- 💳 即日起暂停计费，现有订阅继续免费服务；年付预付用户将获得部分退款。
- 🔁 官方提供迁移指南，支持迁往 Cloudflare、Vercel、Netlify 和 Render。
- 📅 2026 年 11 月 10 日起停止新注册和套餐升级。
- 📖 2026 年 12 月 10 日起进入只读模式，但不包括 SQLite 和 Blob 存储。
- ⏳ 2027 年 1 月 10 日起所有其他服务停止。
- 🧑‍💻 2027 年 2 月 1 日将开源 Val Town。
- 📬 用户可通过 support@val.town 或 Discord 寻求帮助。
- 🙏 创始人感谢团队、投资人、客户和用户过去四年的信任与支持。

---

### [我曾是 Deno 安全模型的粉丝 - macwright.com](https://macwright.com/2026/11/09/deno-security-model)

**原文标题**: [I was a fan of Deno's security model - macwright.com](https://macwright.com/2026/11/09/deno-security-model)

作者回顾了自己作为 Deno 安全模型支持者的经历：Deno 在 Val Town 的实际生产环境中经受住了考验，尽管其许多核心理念最终败给 Node 兼容性，但其权限沙箱在严格、非交互式使用下确实有效，并解决了真实的安全问题。

- 🛡️ 作者曾在 Val Town 使用 vm2 作为沙箱，但发现不够安全，随后推动迁移到 Deno，主要看重其更强的隔离能力。
- 📉 作者认为 Deno 的多数核心理念最终落败：Node 兼容性胜出，Bun 因兼容 Node 获得大量用户，Node 核心反而不断扩张。
- 🔁 Deno 的 HTTP imports 等创新被逐步回滚，模块系统最终与 Node 趋于一致，模块加载创新更偏向渐进演化而非激进变革。
- ✅ 但 Deno 的安全模型“确实有效”：Val Town 将公司押注在 Deno 运行时权限标志上，未出现因这些标志导致的安全事故。
- ⚙️ 作者从第一天就使用 `--no-prompt`，不启用 `--allow-run`，并让代码运行在人工环境中；权限提示更适合学习权限需求，而非核心生产用例。
- 🧱 理论上可用 bwrap、cgroups、Linux namespaces 做更强隔离，但在 Docker/PaaS 环境中难以实施，许多托管平台无法直接使用 cgroups 或命名空间。
- 🌍 Deno 的优势是跨平台、部署简单、可扩展，在 macOS 和 Windows 上行为一致，便于在开发者机器上可靠测试。
- 💡 作者认为语言级能力控制很有前景，例如 Starlark 的“封闭”执行、Lua 沙箱，以及 Koka 可能实现的效应系统，可对不可信代码做更细粒度隔离。
- ⚖️ OS 级能力控制强大可靠但粗粒度；语言级控制可为应用增加额外信任与 compartmentalization。
- 🙏 总结：Deno 安全模型并不完美，但在需要时确实存在、保证成立并解决了真实问题，因此作者仍然感激它。

---

### [Netlify 服务器：使用 WebSockets 实现长时间运行的后端](https://www.netlify.com/blog/introducing-netlify-server/)

**原文标题**: [Netlify Server: long-running backends with WebSockets](https://www.netlify.com/blog/introducing-netlify-server/)

Netlify 于 2026 年 11 月 10 日发布 Netlify Server（早期访问），将 Netlify 的零配置、预览环境和原子部署工作流扩展到后端。它提供无需自行运维的长运行服务器，支持 WebSocket、内存状态和自动扩缩容，定位为补充而非替代 Functions 与 Edge Functions。

- 🧩 背景：函数适合短请求，但长等待、WebSocket、持久状态以及现有 Express/Hono 应用适配等需求会受限。
- 🖥️ 核心：长期运行的 Node.js 进程可并发处理请求，空闲时缩到零，Netlify 负责部署、扩缩容和监控。
- 📁 开发：在 `netlify/server/index.ts` 编写请求处理器，或直接运行 Express、Hono、Fastify 服务，无需配置端口、健康检查或适配器。
- 🔌 集成：Netlify Database、Blobs、AI Gateway、Cache API 等开箱即用；分支部署和 Deploy Preview 各有独立后端与数据库分支。
- 🪝 控制：提供 `onStart`、`onHealthCheck`、`onShutdown` 生命周期钩子，并支持自定义队列、连接池等扩缩容信号。
- 🤖 场景：适用于实时协作、多人游戏与聊天、AI Agent 循环、长时间任务、定时抓取与实时推送等。
- 🧭 定位：不回归单体架构，也不替代函数；静态资源和 Edge 仍在边缘处理，后端可与前端同仓库、同流水线、同原子部署。
- 🧪 早期访问：支持信用制计划和启用信用的企业计划；需 CLI 27.17.0+；最多 3 个实例（Free/Personal 为 1 个），无请求 5 分钟后缩零。
- 💰 计费：早期访问免费；正式可用后按预留内存（GB RAM/小时）和活跃 CPU（vCPU 小时）计费，其他计量功能照常计费。
- 🚀 下一步：收集真实负载反馈，后续将支持保持最小实例数，并继续建设新的计算平台。

---

### [lib: add experimental node:yaml module by marcopiraccini · Pull Request #67157 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67157)

**原文标题**: [lib: add experimental node:yaml module by marcopiraccini · Pull Request #67157 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67157)

该 PR 提议为 Node.js 增加实验性的内置 YAML 解析器 `node:yaml`，目前处于开放评审阶段；实现为仅解析、无外部依赖，并遵循 Bun `Bun.YAML.parse()` 的调用方式，同时围绕 API 设计、版本策略和是否内置展开讨论。

- 🧩 PR #67157 提议新增实验性 `node:yaml` 模块，需通过 `--experimental-yaml` 启用，当前仅提供解析能力。
- ⚙️ `yaml.parse(input)` 支持字符串及二进制输入，返回单文档值、多文档数组或空流 `null`，无效输入抛出 `ERR_INVALID_YAML`。
- 📦 解析器从零实现，支持 YAML 1.2 core schema、锚点、别名、标签和多文档流，并与 Bun 的 `yaml.parse()` 行为保持一致。
- 🧪 官方 YAML Test Suite 402 个用例中 400 个通过；2 个失败用例涉及重复键，因解析器按规范强制键唯一而列为已知失败。
- 🚀 性能讨论显示 JS 实现已较优：332 KiB 输入约 6.49 ms，rapidyaml 约 3.54 ms，Wasm 方案约 7.81 ms；作者倾向首版保留 JS。
- 💬 评审关注点包括 YAML 版本演进、是否兼容 1.1、模块是否应做成完整 YAML API，以及内置 `node:yaml` 可能引发 `node:toml`、`node:xml` 等模块扩张。
- 🧭 版本策略上，解析器按 YAML 1.2 规则处理；接受 `%YAML 1.1` 指令但按 1.2 解析，拒绝 `%YAML 2.x`，未来可考虑增加 `version` 选项。
- 🛠️ 已根据反馈加入 `throwIfInvalid: false`、测试夹具生成工具、复用 `TextDecoder`，并优化映射对象构建，典型文档解析约快 60%。
- 🔜 后续计划包括 `yaml.stringify()`、`import ... with { type: 'yaml' }`、配置文件 YAML 支持、子系统标签及最终移除实验标志。
- 🏷️ PR 已添加 `experimental`、`semver-minor`、`notable-change` 等标签，并有部分维护者批准，但 API 与模块定位仍在讨论中。

---

### [2026 年 JavaScript 现状](https://survey.devographics.com/en-US/survey/state-of-js/2026)

**原文标题**: [State of JavaScript 2026](https://survey.devographics.com/en-US/survey/state-of-js/2026)

提供的正文仅为“Loading...”，没有可总结的实际文章内容。

- ⏳ 当前内容仍在加载中，无法获取有效信息。
- 📄 未提供可分析的文章正文或关键信息。
- ❓ 无法提取要点、主题或核心结论。
- 🔄 建议在内容加载完成后重新提供完整文本。

---

### [获取失败](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

**原文标题**: [Failed to retrieve](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

无法总结：获取内容失败，状态码 403。

---

### [开始使用 WarpBuild | 50 美元免费额度 | WarpBuild](https://www.warpbuild.com/start?utm_source=cooperpress&utm_medium=newsletter&utm_campaign=h2-2026&utm_content=nodeweekly-2026-11-12)

**原文标题**: [Get Started with WarpBuild | $50 in Free Credits | WarpBuild](https://www.warpbuild.com/start?utm_source=cooperpress&utm_medium=newsletter&utm_campaign=h2-2026&utm_content=nodeweekly-2026-11-12)

WarpBuild 提供可直接替换 GitHub Actions 的 CI runner 基础设施，主打“一行 YAML 改动即可让构建速度提升 2 倍、成本减半”，支持 Linux、macOS、Windows 以及 x86-64、ARM64，并提供 macOS 无限并发、BYOC 和企业级安全能力；新用户可领取 $50 免费额度，无需信用卡。

- ⚡ AI 代理带来更多代码和提交，GitHub Actions 流水线压力上升，CI 成为瓶颈。
- 🚀 WarpBuild runner 价格约为 GitHub 托管 runner 的一半，同时任务完成更快，降低费率与运行时长成本。
- 🧩 只需修改 workflow 中的 `runs-on` 一行即可迁移，无需重写工作流。
- 💻 支持 Linux、macOS、Windows，覆盖 x86-64 与 ARM64，包括 M4/M5 Pro Mac。
- 🍎 macOS runner 支持无限并发，Mac 任务无需排队等待自身任务。
- ☁️ 支持 WarpBuild 托管云，也可 BYOC 部署到自有 AWS、GCP 或 Azure。
- 🔐 企业就绪：SOC2 Type 2、临时隔离 VM、SSO、7x24 支持与 SLA。
- 🎁 注册后在 Settings > Billing 使用优惠码 START50 可获 $50 免费额度，无需信用卡，约 2 分钟设置。
- ✅ 兼容现有 GitHub Actions 工作流并预装标准工具；Braintrust、Raycast、OpenRouter、Comcast、Jane Street 等团队在使用。
- 📈 客户反馈构建时间从约 25 分钟降至约 9 分钟，macOS 构建从 30 分钟降至 8 分钟。

---

### [恶意 bee-js npm 发布版本和 Swarm Desktop 发布版本传播 SleepyDuck 以太坊 C2 后门 | Socket](https://socket.dev/blog/bee-js-compromise)

**原文标题**: [Malicious bee-js npm Release and Swarm Desktop Releases Deliver SleepyDuck Ethereum C2 Backdoor | Socket](https://socket.dev/blog/bee-js-compromise)

2026年11月9日，Ethersphere 的发布流水线遭入侵，攻击者利用合法 GitHub 自动化发布恶意 npm 包 `@ethersphere/bee-js@13.3.0` 和带木马的 Swarm Desktop 0.56.2。两者均含加载器，会从 `api[.]frameworkmetrics[.]xyz` 拉取 JavaScript 并以 Node.js 权限执行；其 C2 地址来自与 SleepyDuck/EtherDuck Open VSX 行动相同的以太坊合约。

- 🧨 攻击者控制了两个 GitHub 账号：维护者 `nugaon` 和发布自动化身份 `bee-worker`；11月6日曾尝试窃取 CI 密钥但失败，未发现成功外泄证据。
- 📦 `bee-js@13.3.0` 通过合法 trusted publishing 和有效 SLSA provenance 发布，`scripts/generate-version.cjs` 被改为 `postinstall` 远程代码加载器。
- ⏱️ npm 在发布约75分钟后移除该版本；但发布任务中加载器曾运行3次，且当时具备 OIDC 令牌能力。
- 🖥️ Swarm Desktop 0.56.2 由项目自身 CI 构建、签名和公证，Electron 主进程启动即执行加载器，并通过自动更新推送给 macOS Apple Silicon 和 Windows x64 用户。
- 🔗 加载器从以太坊合约 `0xf8a900Db50b3331be6B768bA460BB59f3E40C344` 读取 C2 地址；该合约及控制钱包与2026年10月披露的 SleepyDuck/EtherDuck 行动重合。
- 🕵️ 第二阶段载荷会窃取 Bee 节点 `config.yaml`、节点钱包密钥，并下载第三阶段植入物。
- 🐚 macOS/Linux 第三阶段为 Go 后门，存放于 `~/.solidity/`，通过 systemd 用户服务或 LaunchAgent 持久化，并连接 C2 获取远程 shell。
- 🪟 Windows 第三阶段使用 UAC 绕过、Defender 排除项和合法签名的 ScreenConnect 客户端，实现无人值守远程访问。
- 💥 受影响风险包括 Bee 节点钱包资金、chequebook、质押、安装用户或 CI 环境可访问的凭据，以及持久远程控制。
- 🧹 bee-js 用户应搜索锁文件、缓存和镜像中的 `@ethersphere/bee-js@13.3.0`，固定到 13.2.0，并轮换可能暴露的凭据。
- 🛠️ Swarm Desktop 用户应检查日志中是否出现 `Bee Desktop version: 0.56.2 (production)`，卸载并升级到 0.56.3，同时将节点资金迁移到新钱包。
- 🔍 安全团队应 Hunt `api[.]frameworkmetrics[.]xyz`、相关 IP/端口、以太坊合约 `eth_call` 请求，以及 `~/.solidity/`、`com.solidity.langsupport.runner`、`solidity-langsupport-runner.service`、ScreenConnect 服务等痕迹。
- 🧱 维护者应限制发布事件只能发布受保护分支或已合并发布 PR 的提交，为发布环境配置必需审核者和标签策略，并避免手动工作流接触签名证书。
- 📌 IOC 包括恶意包/版本、提交哈希、两个配置合约、两个操作钱包、多个 C2/IP、ScreenConnect 中继、webhook 收集器及文件哈希。

---

### [你的 JS 错误在骗你](https://blog.gaborkoos.com/posts/2026-11-12-Your-JS-Error-Is-Lying-to-You/)

**原文标题**: [Your JS Error Is Lying to You](https://blog.gaborkoos.com/posts/2026-11-12-Your-JS-Error-Is-Lying-to-You/)

本文追踪一个 JavaScript Error 从创建、包装、序列化、跨线程/进程/HTTP 边界到写入日志的全过程，说明错误对象在每一层都可能被丢字段、改含义或变成不可诊断的表示；核心不是“别用 JSON.stringify”，而是理解这些表示并主动保留失败上下文。

- 🧩 `JSON.stringify(err)` 常得到 `{}`：`message` 和 `cause` 是非枚举属性，`Object.keys`、展开、`Object.assign` 同样看不到；`catch` 捕获值也未必是 `Error`。
- 🧱 `stack` 不是 ECMAScript 标准：V8 在错误创建时采集，默认只留 10 帧，可被覆盖；异步栈是沿 Promise 链重建的，格式和深度因引擎而异。
- 🔗 包装错误若不传 `{ cause }` 会丢失原始失败；即使传了，也必须遍历 cause 链，且链可能有环、过长或包含非对象值。
- 🌳 失败结构可能是图而非单链：`AggregateError.errors`、`SuppressedError.error/suppressed`、`cause` 含义不同，诊断遍历要分别处理。
- 🌐 Node.js、Deno、Bun、Chrome、Firefox、WebKit 在语言保证上一致，但额外属性、栈格式/深度、消息文本、宿主错误形态不同。
- 📦 序列化各有损失：JSON 和对象复制只保留可枚举字段；`structuredClone` 可保留部分 message/cause，但常丢子类字段；`toJSON` 会替换契约。
- 🚚 跨边界传递不会保留原对象：Web Worker、`postMessage`、worker_threads、子进程 IPC、HTTP 各保留不同部分，接收方拿到的是重建/投影。
- 🪵 日志器可能隐藏失败：Pino/Winston 的结果取决于错误放在哪个 key、位置和配置；错误 key 不对会丢 message/stack，Winston 默认甚至可能只写 `{"level":"error"}`。
- 🔐 日志还有泄露风险：Pino 默认会复制自定义可枚举字段，URL token、Authorization、查询参数可能入库；应使用 redact 或 allowlist，只记录命名且必要的字段。
- 🧭 处理错误应分离关注点：重试/恢复基于稳定 `code`（沿 cause 链查找），日志保留诊断信息，HTTP 客户端只需小型 problem document。
- 🛠️ 推荐自建提取函数：遍历 `cause`、`errors`、`error`、`suppressed`，处理循环、深度/成员上限，只读数据属性，只复制调用方命名的字段。
- 📮 对外 HTTP 响应应使用 RFC 9457 `application/problem+json`，不返回 stack、文件路径、数据库地址；完整错误留在服务端日志并用 instance 关联。
- ✅ 最终结论：Error、栈、日志、序列化对象、API 错误响应只是同一失败的不同表示，不能互换；没有任何机制能无损携带完整诊断状态，必须在源头传 cause 并主动构造可控表示。

---

### [One TypeScript client, every forge - forges](https://forges.link/)

**原文标题**: [One TypeScript client, every forge - forges](https://forges.link/)

`forges` 是一个统一接口库，用于跨 14 个代码托管平台（forge）处理 issue、拉取请求、通知、检查和 webhook。它让开发者用一套代码适配不同平台，并自动处理各平台的端点、分页、认证和速率限制。

- 🧩 提供统一客户端：一个客户端即可连接 GitHub、GitLab、Codeberg 等 14 个 forge，覆盖问题、PR、通知、检查和 webhook。
- 📦 安装简单：使用 `pnpm add forges` 即可开始，通过 `createForges` 组合多个 provider。
- 🔐 支持认证配置：例如 GitHub 使用 token，GitLab 也支持 token；匿名模式仅能进行公开读取。
- 🧠 统一数据模型：issue、PR、评论、检查和事件在各平台保持相同结构，同时保留原始 `raw` 数据。
- ✅ 声明式能力检查：每个 provider 声明支持的能力，可在调用前用 `provider.can()` 检查，并通过测试验证。
- 🔔 Webhook 验证与类型化事件：自动验证 webhook 投递并转换为统一类型事件，跨平台保持相同事件类型和动作。
- 🪶 按需打包：只打包导入的 forge，GitHub provider 约 42 kB gzip；webhook 转换代码按需加载。
- 🧪 离线测试：支持内存 forge 或回放响应进行测试，无需访问网络。
- ⚠️ 类型化错误与重试：速率限制、token 失效、权限不足等有独立错误类，短期限流后可自动重试一次。
- 📊 能力矩阵：展示各 forge 对 `threads.merge`、`notifications.list`、`checks.list`、`ci.runs`、`releases.list`、`webhooks.create`、`search.threads` 等能力的支持状态（原生、实验、模拟、未验证等）。
- 🛠️ 适用场景：通知收件箱、标签机器人、发布摘要、统一 webhook 接收器等。
- 🚀 快速上手：安装包、读取一个 issue，再添加第二个 forge，即可体验统一接口。

---

### [GitHub - aws/aws-emulator：AWS Emulator 是 AWS API 的本地模拟器。 · GitHub](https://github.com/aws/aws-emulator)

**原文标题**: [GitHub - aws/aws-emulator: AWS Emulator is a local emulator of the AWS APIs. · GitHub](https://github.com/aws/aws-emulator)

AWS Emulator 是一个本地 AWS API 模拟器，用于在本机、开发服务器或 CI 中测试软件，无需调用真实 AWS 或拥有 AWS 账号；请求会发送到模拟器并操作模拟资源。它不收取额外服务费，只有实际部署 AWS 资源时才需付费；仅适用于构建和测试，不应用于生产或安全测试。

- 🌐 本地程序提供 AWS API 端点且无图形界面；启动后设置环境变量让 AWS CLI/SDK 指向该端点，嵌入式模式则把模拟器 HTTP 客户端传给 SDK。
- 🤖 可通过 AI 编码代理快速上手：安装 aws-emulator skill，需要 AWS CLI 2.35.0+，命令为 `aws agent-toolkit add-skill --skill-name aws-emulator --region us-east-1`。
- 🖥️ 服务器模式：Linux 安装 RPM 或 Debian 包并运行 `aws-emulator`；Windows/macOS 使用简短 Dockerfile 构建容器运行。
- 🧩 嵌入式模式：作为 Rust 测试的 dev-dependency 在进程内运行，每个测试一个隔离实例，无需端点 URL、证书或环境变量。
- 💰 嵌入式模式构建成本：首次 `cargo test` 会把模拟器服务 crate 编入测试二进制，首次构建和 `target/` 空间开销类似源码构建；建议复用 `CARGO_TARGET_DIR`、缓存 `target/` 或使用 sccache，并固定模拟器版本。
- ⚠️ 已知问题与兼容性：各版本发布页提供保真度分数；未实现和已修复行为分别记录在 `issues/things-that-do-not-work/` 与 `issues/things-that-now-work/`。
- 🛠️ 从源码构建需求：Rust/Cargo、C 编译器、至少 100GB 磁盘、多核机器；支持 Linux x86_64/aarch64，Windows/macOS 建议使用 Docker。
- 🚀 构建运行命令：`cargo build -p aws-emulator-router`、`cargo run -p aws-emulator-router`；服务 HTTPS 于 `127.0.0.1:9297`，使用自签名证书。
- 🧱 仓库布局：每个 AWS 服务一个 crate；`core/router` 挂载所有服务，`core/embedded` 提供进程内门面，`vendor/` 为框架代码勿编辑，`issues/` 跟踪保真度问题。
- 📊 仓库约 5.4k Star、184 Fork、15 Watcher、30,681 次提交；使用 CC0-1.0 许可证，`vendor/` 目录为 Apache 2.0。
- 📡 默认开启遥测，向 AWS 报告使用数据；严格最小化，不包含请求/响应内容、代码、凭证或个人数据，也不与第三方共享。
- 🔕 关闭遥测方式：`--telemetry off`；`EMULATOR_TELEMETRY=off`；配置文件 `config.toml` 中设置 `[telemetry] enabled=false`；嵌入式 API 使用 `Telemetry::Off`。
- 🧑‍💻 若工具内置模拟器，应告知用户遥测并提供关闭方式，也可默认关闭遥测。
- 🐞 问题反馈：在 GitHub Issues 报告 bug 和保真度缺口，最好包含服务、操作、SDK 版本、请求及与真实 AWS 的差异；仓库不接受 PR。
- 📜 许可证：除 `vendor/` 外采用 CC0-1.0。

---

### [为使用智能体构建提供更好的反馈 | AWS 洞察](https://aws.amazon.com/blogs/aws-insights/better-feedback-for-building-with-agents/)

**原文标题**: [Better feedback for building with agents | AWS Insights](https://aws.amazon.com/blogs/aws-insights/better-feedback-for-building-with-agents/)

AWS 发布本地环境 AWS Emulator，让开发者和 AI 编码代理无需预置云资源或支付模拟操作费用，即可使用熟悉的 AWS API、SDK 和工具构建并测试应用。它通过快速、准确的本地反馈帮助代理更早发现并纠正错误假设，减少在错误基础上继续构建的代码；同时也可用于代理评估与强化学习训练。但模拟器与真实 AWS 存在差异，团队需关注其服务覆盖范围和已验证结果。

- 🧪 **本地测试 AWS 应用**：AWS Emulator 提供本地环境，可使用常见 AWS API、SDK 和工具，无需预置云资源，也无需为模拟操作支付 AWS 服务费用。
- ⚡ **快速反馈决定代理效率**：代理承担更多任务时，需要知道什么成功、什么失败、哪里需要修改；反馈越快越准确，可委托的工作越多，结果也越可信。
- 🔁 **按当前状态评估请求**：与依赖预先编写响应的 mock 不同，模拟器根据当前状态评估请求，让开发者和代理测试不同操作序列。
- 🛒 **重复订单示例**：在 SQS 到 DynamoDB 的场景中，条件写入可暴露重复订单处理缺陷，代理能借模拟器遇到、调查并修正错误。
- 🧭 **尽早发现错误假设**：错误未被发现的时间越长，代理围绕它构建的代码越多；本地检查可让应用更早进入 AWS 测试阶段。
- 🧵 **支持并行试验方案**：独立本地环境可让代理实现两种方案、运行相同测试，并交由开发者比较结果。
- 🎯 **用于代理评估与训练**：团队可在多种应用和任务上测试代理，降低云资源预置与清理成本，并支持强化学习中的任务练习和结果评估。
- ⚠️ **注意模拟器与 AWS 的差异**：若模拟器接受 AWS 会拒绝的行为，训练可能强化错误；团队需要了解哪些行为与 AWS 一致、哪些不同。
- 📊 **公布覆盖与验证结果**：AWS Emulator 覆盖数百个服务接口，但各服务与操作的实现完整度不同；AWS 公布版本化测试、场景及单步成功率。
- 🐧 **现已免费提供**：支持 Linux，以 Docker 容器形式提供，GitHub 上有源代码，文档涵盖安装设置和服务覆盖范围。

---

### [AWS 模拟器：一个完全由自主 AI 智能体构建的本地模拟器](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator)

**原文标题**: [AWS Emulator: a local emulator built 100% by autonomous AI agents](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator)

本文介绍了 AWS Emulator：一个可在本地运行、用于构建和测试 AWS 应用的 AWS 服务模拟器。它完全由自主 AI 代理编写，团队未编写或审查代码；其核心在于通过明确规范、真实 AWS 参考实现和多层护栏，让代理在边界内独立工作，并以 CC0 许可在 GitHub 持续更新。

- 🧠 AWS Emulator 是本地 AWS 服务模拟器，100% 由自主 AI 代理编写，团队未编写或审查任何代码。
- 🧩 项目源于周末实验：作者用 Kiro 按“先写 CLI 测试、再对真实 AWS 验证、最后做内存实现”的提示，15 分钟得到可用的 Amazon SQS 初版，周末扩展到更多 AWS 服务。
- 🛡️ 关键护栏是保真测试：每个测试对应真实 AWS 场景，并在提交前对真实 AWS 验证；测试可重复运行且目标明确。
- 👥 系统由三类代理团队协作：一队维护测试套件，一队回放测试并发现差异/提交问题，一队负责修复单个问题。
- 🔍 修复代理需定位根因并修改代码，变更必须通过合入门禁：编译、编码标准审查、安全检查和保真度回归验证。
- ⚙️ 数百个代理可并发工作，每天修复数千个问题；合入门禁是保证速度与可靠性的关键。
- 🚀 代码合并后经 AWS Developer Tools 发布流水线处理，以 AWS CodeCommit 为主仓库，最终打包为可下载二进制并发布到 GitHub。
- 📂 GitHub 上可查看所有问题记录：已修复项在“issues/things-that-now-work”，待办项在“issues/things-that-do-not-work”。
- 🐍 早期代理曾自行构建 Python 解释器来支持 AWS Lambda，后来被指导优先复用现有库。
- 📜 源码和保真测试均已在 GitHub 以 CC0 许可公开；后续文章将深入多代理架构、保真度测量和质量安全措施。

---

### [GitHub - paulirish/chrome-capture：从 Chrome 捕获 60-120fps / 2160p 标签页视频/音频 · GitHub](https://github.com/paulirish/chrome-capture)

**原文标题**: [GitHub - paulirish/chrome-capture: 60-120fps / 2160p tab video/audio capture from Chrome · GitHub](https://github.com/paulirish/chrome-capture)

chrome-capture 是 Paul Irish 开发的开源工具，可直接将 Chrome 标签页录制成 60–120fps、最高 2160p 的 AV1 MP4，并支持标签页音频，无需 ffmpeg；底层基于 Chrome 153+ 新增的 `Page.startScreenRecording`。

- 🎥 **核心能力**：以 60–120fps 录制标签页视频，最高支持 2160p，并输出 AV1 编码的 `.mp4` 文件。
- 🔊 **音频支持**：可同时录制标签页音频，为 48kHz 立体声 Opus。
- ⚡ **技术升级**：帧从合成器经共享内存直达进程外编码器，Chrome 边录边写 AV1，不再依赖 JPEG + ffmpeg 管道。
- 🛑 **停止几乎即时**：编码在录制过程中完成，停止仅需约 17ms，而旧方案需约 3.8s。
- 🧰 **CLI 易用**：支持 `npx chrome-capture <url> <output.mp4> <duration>`，可配置 fps、分辨率、headful、DevTools 等。
- 🧩 **多环境 API**：`startRecording()` 支持 Playwright Page、Puppeteer Page 或原生 CDP session，默认 60fps。
- 🧪 **测试集成**：提供 `@playwright/test` fixture，可自动录制每个测试并将 mp4 附加到报告。
- 🎭 **可见光标**：Playwright 下可通过 `page.screencast.showActions()` 将光标、点击徽章、元素高亮绘制到 DOM 中并被录制。
- 📊 **性能对比**：同一 6.4s 回放，旧方案 25fps、总耗时 21s、停止 3.8s、WebSocket 10.5MB；新方案 60fps、11s、17ms、450KB。
- 🎚️ **码率与画质**：暂无数码率或 CRF 调节；libaom AV1 实时 1-pass VBR，码率随像素率线性增长，1080p60 约 9Mbps 是较佳平衡点。
- 🖥️ **性能上限**：Mac headless 可达 2160p60；120Hz ProMotion Mac headful 可达 1080p120 和 2160p120；Linux headless 常见 1080p60 或 1440p60。
- ⚠️ **macOS 注意**：GPU 加速的 Mac 上不要传 `--disable-frame-rate-limit --disable-gpu-vsync`，否则会拖垮 capture readback。
- 📦 **项目信息**：Apache-2.0 许可，约 393 stars、7 forks；可通过 npm 安装，也可直接参考精简的 `src/index.ts` 实现。

---

### [发布 v1.65.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.65.0)

**原文标题**: [Release v1.65.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.65.0)

overview summary
Playwright v1.65.0 发布，新增 Bun 测试运行支持、仅失败报告和测试锁等能力，并带来多项行为变更与运行环境要求调整。

- 🥟 新增 `--bun` 支持，在 Bun 下运行测试；但无 watch 模式，`tsconfig`/JSX 选项和自定义 ESM loader 不生效，堆栈与 trace 控制台输出也有差异。
- 🚨 新增 `failures` reporter，以及 HTML、JSON、JUnit reporter 的 `onlyFailures` 选项，仅保留失败、flaky 和中断测试。
- 🎯 测试运行器新增 `-exclusive-` 测试锁；`skip/fixme/fail/slow` 可只传描述并记录为注解；新增 `PLAYWRIGHT_TRANSFORM_CACHE_DIR`。
- 🔌 新 API/选项：`cdpSession.send()` 支持 `timeout` 和 `signal`，`testRun.mode()` 可用于 `reporter.preprocess()`。
- ⚠️ TypeScript 类字段遵循 `useDefineForClassFields`，在 ES2022+ 或未指定 target 时启用，可能导致读取构造参数属性的字段初始化失败。
- ⏳ 点击、勾选、填充等操作会等待元素非 `inert`；对 `inert` 元素执行操作会超时。
- 🧪 分片运行在所有分片均无匹配测试时报 “No tests found”；空分片在其他分片有测试时仍可通过。
- 🍪 Cookie 匹配遵循 RFC 6265；代理凭据仅用于代理挑战，网站认证需使用 `httpCredentials`。
- 🧭 不可渲染文本不再计入可访问名称和 aria 快照；`params` 会追加到已有查询；CSS 预处理器导入变为空模块且文件必须存在。
- 🐳 不再测试 Node.js 20，建议使用 Node 22/24/26；Docker 镜像升级至 Node 26；浏览器版本为 Chromium 158、Firefox 159、WebKit 27.2。

---

### [获取失败](https://vlt.io/blog/vlt-1-7)

**原文标题**: [Failed to retrieve](https://vlt.io/blog/vlt-1-7)

无法总结：获取内容失败，状态码 429。

---

### [发布 v4.1.0 · porsager/postgres · GitHub](https://github.com/porsager/postgres/releases/tag/v4.1.0)

**原文标题**: [Release v4.1.0 · porsager/postgres · GitHub](https://github.com/porsager/postgres/releases/tag/v4.1.0)

postgres.js v4.1.0 发布，重点增强查询超时、批处理、查询级解析器和标识符构造，并修复 TLS、取消、监听、事务错误及内存问题，同时带来多项性能优化。

- 🚀 发布 v4.1.0（13 个提交），新增 query_timeout（默认关闭，超时抛 QUERY_TIMEOUT）和 cancel_timeout（默认 5 秒），可处理服务端或网络静默。
- 📦 新增 sql.batch([queries])，单次往返发送；事务外整批提交或回滚，失败时 error.index 指出失败查询位置。
- 🔍 新增 sql.identifier(...parts)，正确引用带点标识符，如 "acme.inc"."users"；无参数抛 NO_PARTS。
- 🧩 新增查询级 .parsers() 自定义行解析器；transform 支持 json: false/true 控制 JSON 键重命名与发送。
- ⚡ 新增 eager_types: true，可在连接池启动时读取数组类型和域；Node.js 18 恢复支持（require 仍需 20.19 或 22.12）。
- 🔁 修复 sql.listen 在最后 unlisten 后保持连接并提升性能；首次重连失败会按 backoff 持续重试。
- 🔐 现在读取 PGSSLMODE；require 使用 TLS，verify-ca/verify-full 使用 Node CA；URL 中 sslrootcert、sslcert、sslkey 会正确转为 ca、cert、key。
- 🛑 取消查询不再无限等待：服务端不响应超过 cancel_timeout 会关闭连接并重连，相关查询以 CONNECTION_DESTROYED / CANCEL_UNANSWERED 拒绝。
- 🧾 修复 insert helper 在带引号 schema 加未引号表名下的构造错误；IP 主机证书验证、savepoint/嵌套 begin 连接丢失错误也修复。
- ⚠️ 服务器以 25P04、25P03、57P01 结束事务时，sql.begin 现在以服务器 FATAL 错误拒绝而非 CONNECTION_CLOSED；重试逻辑需考虑 57P01。
- 🧠 修复缓存 prepared statement 保留查询结果导致内存膨胀；copy ... to stdout 流 destroy 后连接可释放；每个查询获得独立错误。
- 🚀 性能优化：SSL ca 上下文复用、数字/null 无类型参数单次往返、数组/域惰性读取、时间戳直读字节、bytea/int 数组二进制解析，并改善大量连接就绪时的查询调度。

---

### [发布 v4.0.0 · porsager/postgres · GitHub](https://github.com/porsager/postgres/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · porsager/postgres · GitHub](https://github.com/porsager/postgres/releases/tag/v4.0.0)

Postgres.js v4.0.0 是一次底层大重写：连接池、连接、协议、启动流程和 socket 层均重写，但查询、辅助函数、事务、游标、COPY、LISTEN、订阅、大对象和选项等公共 API 基本保持与 3.4.9 一致，并带来安全修复、破坏性变更、新功能、错误修复、性能优化和更完整测试。

- 🔄 **底层重写**：v4 重写公共 API 以下的连接池、连接、协议、启动和 socket 层；多数上层用法与 v3.4.9 类似。
- 🔐 **安全修复**：连接参数中的 NUL 字符不能再注入额外启动参数，协议字符串含 NUL 会以 `NUL_CHARACTER` 拒绝；`__proto__` 列现在作为行自身属性处理，避免原型污染。两项修复也回补 v3。
- ⬆️ **升级注意**：README 提供升级指南；默认 `infer: false`，由服务器决定参数类型，`Date` 写入/比较 `timestamp`/`date` 时按 UTC 处理；`infer: true` 保留 v3 行为。
- 📦 **运行时变更**：仅提供 ES module；支持 Node.js 20+、Bun、Cloudflare Workers，Deno 通过 Node 兼容层；CommonJS/Deno 构建移除，Node 20.19/22.12+ 可用 `require('postgres').default`。
- 🚫 **移除 `sql.array()`**：改为直接传数组并按需加 cast，例如 `${ids}::int[]`；调用 `sql.array()` 会抛 `ARRAY_REMOVED`。
- ↩️ **事务语义更严格**：服务器对 COMMIT 返回 ROLLBACK 时，`sql.begin` 以 `TRANSACTION_ROLLED_BACK` 拒绝；已释放连接保持释放；不安全的手动 `begin` 会以 `UNSAFE_TRANSACTION` 拒绝并回滚；事务内无法构建/序列化的查询会使事务中止。
- 🧠 **新调度器**：连接全忙时根据语句耗时和进行中查询选择管线化连接，显著降低快查询 p99；`scheduler: false` 改用最少在途查询的连接，`max: 1` 时关闭调度。
- ⏱️ **超时与取消**：新增 `queue_timeout`，等待连接超时以 `QUEUE_TIMEOUT` 拒绝；查询支持 `.signal(abortSignal)`，等待中可拒绝、运行中可取消；游标在批次间取消会停止并关闭 portal。
- 🧰 **新功能与便利性**：支持 `sql.join`、事务内嵌套 `sql.begin` 使用 savepoint、`sql.rollback()`、事务内任意位置管线化、按名称自定义类型、`using`/`await using`、`unref_sockets`、`min`/`idle_timeout`、`user` 函数、`PGPASSFILE`、命名参数、COPY 行数、持久复制槽、`sql.stats`、`query.text`/`query.parameters`、诊断 tracing 通道等。
- 📡 **连接与协议增强**：支持 SCRAM-SHA-256-PLUS 通道绑定、Node.js 直连 TLS、Cloudflare Workers `workerd` 导出、命名游标、语句列类型变化后重新 prepare、`sql.close()` 可关闭连接后继续使用连接池。
- 🐞 **修复大量正确性问题**：包含 33 个回归测试覆盖的 bug，如冷池只开一个连接、`PostgresError` 字段/JSON 序列化、游标回调、大对象 `end`、Bun/Cloudflare Workers、语句名冲突 `42P05`、TypeScript 类型、helper 子句识别、连接 URL 解析、答案错配、事务连接丢失、查询顺序、`connect_timeout`、认证不完整、`DEALLOCATE ALL`、`search_path` 多租户等。
- ⚡ **性能优化**：参数类型已知的语句一次往返完成 prepare/describe/run；`int2`/`int4`/`oid`/`bool` 直接从字节解码；空闲连接直达；每连接单缓冲区；结果形状稳定后使用编译函数构建行对象，降低 CPU 开销。
- 🧪 **测试更完整**：新增协议/类型/查询构建/错误单元测试、真实客户端对假服务器的故障模拟、按领域拆分的集成测试；CI 覆盖 PostgreSQL 14–18、Node.js 20/22/24、Bun、Deno、Cloudflare Workers 和 TypeScript 类型测试，并用 V8 coverage 检查覆盖率。

---

### [Postgres 中的 JSON：100 万行 JSONB 仍然很快吗？ - 博客](https://exobench.ai/blog/jsonb-at-scale?utm_source=nodeweekly&utm_medium=newsletter&utm_campaign=nw-2026-11-12-classified)

**原文标题**: [JSON in Postgres: still fast at 1M rows of JSONB? - Blog](https://exobench.ai/blog/jsonb-at-scale?utm_source=nodeweekly&utm_medium=newsletter&utm_campaign=nw-2026-11-12-classified)

文章通过 ExoBench 在 Postgres 17.11 上对 1M 行 JSONB 订单表进行压测，结论是：JSONB 在开发环境的小数据量下看似很快，但在生产规模下，若过滤或排序字段仍留在 jsonb 中，GIN 或普通表达式索引往往无法避免全表扫描；把关键字段提升为普通列，可把读取量从 283 MB 降到 369 KB。

- 📉 1M 行执行 `(details->>'units_shipped')::int > 950` 时，GIN 索引仍走并行全表扫描：34,598 页、283 MB、76.19 ms。
- 🧩 在 `details->>'units_shipped'` 上建普通 btree 索引无效，Postgres 未使用，仍是同样全表扫描；只有索引表达式与查询强制转换一致时，类型化表达式索引才生效，读 25,595 页、210 MB、31.95 ms。
- 🚀 改为普通 `units_shipped int` 列并建索引后，使用 Index Only Scan：仅 45 页、369 KB、8.02 ms，同等结果下读取数据量少约 769 倍。
- 🧪 10K 行时各方案都低于 3 ms，开发库“很快”不能代表 1M 行；文章强调要用 10K、100K、1M 多规模基准测试。
- 🗺️ GIN 只擅长 `@>` 包含查询，例如 region 查询可从 34,598 页降到 14,003 页；但对数值范围 `>` 和排序帮助有限；类型化表达式索引对 Top 100 排序帮助明显。
- 🖥️ 管理后台三块查询刷新：GIN 方案约读 683 MB、190 ms；普通列方案约读 1.4 MB、10 ms；20 个桌面每 5 秒刷新时，GIN 方案约 2.7 GB/s，普通列约 5.4 MB。
- 🛠️ 建议：能迁移就把过滤或排序字段提升为普通列；暂不能迁移时，为字段建与查询相同 cast 或排序的表达式索引；用 `pg_stat_statements`、`pg_indexes` 和 Prisma/Drizzle SQL 日志排查。
- ⚠️ 局限：数据为合成且均匀、只测读取未测写入成本、行较小、缓存预热、毫秒值有最高约 36% 波动，页面数最多波动 6 页。

---

### [防范账户接管欺诈 | Fingerprint 设备智能平台](https://fingerprint.com/use-cases/account-takeover/?utm_source=NodeWeekly111026&utm_medium=newsletter)

**原文标题**: [Prevent Account Takeover Fraud | Fingerprint Device Intelligence Platform](https://fingerprint.com/use-cases/account-takeover/?utm_source=NodeWeekly111026&utm_medium=newsletter)

该内容强调全面防范账户接管（ATO），重点阻止凭据填充和暴力破解攻击，以提升账户安全性。

- 🛡️ 阻止所有类型的账户接管（ATO）
- 🔐 防范凭据填充攻击
- 🚫 阻止暴力破解攻击

---

### [我测试了每一个 JavaScript 运行时（令人惊讶）- YouTube](https://www.youtube.com/watch?v=zDw_DxM5GlI)

**原文标题**: [I tested EVERY Javascript runtime (surprising) - YouTube](https://www.youtube.com/watch?v=zDw_DxM5GlI)

该文本是 YouTube/Google 页面底部的导航与法律信息链接列表，涵盖平台介绍、联系与创作者资源、广告与开发者入口，以及条款、隐私、政策安全和版权声明等内容。

- 📌 提供“关于”“新闻”“版权”“联系我们”等基本信息入口。
- 👥 包含“创作者”“广告”“开发者”等合作与开发相关链接。
- 📜 列出“条款”“隐私”“政策与安全”等法律与政策说明。
- ⚙️ 包含“YouTube 运作方式”和“测试新功能”等平台说明与功能入口。
- ©️ 文末标注“© 2026 Google LLC”版权信息。

---

### [GitHub - arjaythedev/js-runtimes-benchmark: 22 ways to run a JavaScript API: Node, Bun and Deno with their popular frameworks, load tested on one 8-core server · GitHub](https://github.com/arjaythedev/js-runtimes-benchmark)

**原文标题**: [GitHub - arjaythedev/js-runtimes-benchmark: 22 ways to run a JavaScript API: Node, Bun and Deno with their popular frameworks, load tested on one 8-core server · GitHub](https://github.com/arjaythedev/js-runtimes-benchmark)

该项目对 Node、Bun、Deno 及 22 种流行框架组合进行了统一压测：同一套 RealWorld “Conduit” API（19 个端点、Postgres），按各自官方文档实现，在单台 8 vCPU 应用服务器上运行，并以 5 分钟内维持 p95<500ms、p99<1s、错误率<1% 的最大用户数作为评分。

- 🧪 测试设计：22 个“运行时 × 框架”栈，独立 Postgres 与 Go 压测机；用户为浏览器式闭模型访客，约 7 秒思考时间、单 keep-alive 连接、约 5% 写请求。
- 🥇 总排名：Bun 全面领先；Bun.serve 以 84,000 用户、21,469 req/s、p95 445ms 居首，Elysia 76,000，Bun+H3/Hono 68,000，Bun+Express 62,000 仍超过最快 Node 栈 uWebSockets.js 的 52,000。
- ⚙️ 运行时大于框架：所有 Bun 行都胜过 Node/Deno；Node 上框架差异较小，多数落在 39–42k，仅 uWS 52k、Fastify/ultimate-express 46k 突出；Deno 原生 44–48k，但 npm 兼容的 Express/Fastify 最差且过载不稳定。
- 🗄️ Node 的 pg 默认有隐藏成本：默认未命名语句导致 Postgres 每次解析/规划；改用命名预处理语句后 Node 中位数提升约 14%，每请求数据库 CPU 降低约 30–37%，但仍无法缩小与 Bun 的差距。
- 🌐 HTTP/2 反而更慢：h2c 下各栈用户数下降 5–36%，内存增至 1.5–3 倍；结论是 TLS/HTTP/2/HTTP/3 应终止在 CDN/代理，应用层继续用 HTTP/1.1。HTTP/3 因运行时支持不足未测。
- 🐛 关键坑点：H3 v2 会静默破坏 node:cluster；Bun 的 node:http 忽略 reusePort；Deno `--parallel` 共享 socket 且分配不均；Deno+Express 过载后会永久卡死；uWS 空闲连接 10 秒关闭；Node 默认 keep-alive 仅 5 秒；Fastify 默认 coerceTypes 会错误接受输入；JWT 帮助函数多只读 Bearer 而 RealWorld 用 Token。
- ⚠️ 注意事项：首轮测试有约 5% 背景负载和遗留监控进程，Bun/Deno 分数可能略低几个百分点，但排序不变；顶部 Bun 栈已把数据库打到 96–98%，应视为“至少”；每栈仅一次运行，约 10% 以内差异属噪声。
- 📁 仓库提供各栈代码与 README、完整 hold 结果、默认 pg 对照、异常/停止运行记录及评分工具，便于复现与核查。

---

