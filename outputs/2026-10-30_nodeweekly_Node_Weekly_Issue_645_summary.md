### [](https://nodejs.org/en/blog/release/v26.13.0)

**原文标题**: [Node.js — Node.js 26.13.0 (LTS)](https://nodejs.org/en/blog/release/v26.13.0)

Node.js 26.13.0 于 2026-10-28 发布，代号“Lithium”，标志着 Node.js 26.x 正式进入长期支持（LTS）阶段；本次发布主要更新 LTS 元数据，未包含相对 26.12.1 的进一步代码变更。

- 🏷️ 版本：Node.js 26.13.0（LTS），代号“Lithium”，由 Richard Lau 发布。
- 📅 支持周期：该 LTS 版本将持续获得更新至 2029 年 4 月底。
- 🔄 变更内容：除更新 `process.release` 等元数据以表明 LTS 状态外，与 Node.js 26.12.1 相比无其他变更。
- ⚠️ 升级提示：从 Node.js 24、22 或更早 LTS 升级时需注意，自 Node.js 25 起，Linux 官方二进制链接了 `libatomic`，部分 Linux 发行版可能需要单独安装。
- 💻 下载平台：提供 Windows 64 位/ARM64、macOS Intel/Apple Silicon、Linux x64/ppc64le/s390x/ARM64、AIX 64 位等安装包或二进制。
- 📦 其他资源：同时提供源代码包、文档、发布文件列表以及 SHA256 校验和与 PGP 签名。

---

### [Node.js — Node.js 版本发布](https://nodejs.org/en/about/previous-releases)

**原文标题**: [Node.js — Node.js Releases](https://nodejs.org/en/about/previous-releases)

Node.js 采用 Current 与 LTS 双阶段发布策略，生产环境应使用 Active LTS 或 Maintenance LTS；历史上奇数版本约 6 个月后停止支持，偶数版本进入 Active LTS。自 Node.js 27 起改为年度发布，每个主版本在 6 个月 Current 阶段（以及额外 6 个月 Alpha 阶段）后进入 LTS。LTS 通常保证关键缺陷修复总计 30 个月。下载页提供 CLI、系统包管理器、版本管理器等方式，并将安装方式分为“推荐”和“社区”。

- 📅 Current 发布状态持续六个月，便于库作者添加支持。
- ✅ 历史上（截至 Node.js 26）奇数版本（9、11 等）六个月后不再支持；偶数版本（10、12 等）进入 Active LTS。
- 🔁 从 Node.js 27 开始改为年度发布，每个主版本在六个月 Current 阶段（以及额外六个月 Alpha 阶段）后进入 LTS。
- 🛡️ LTS 即“长期支持”，通常保证关键缺陷修复总计 30 个月；生产应用仅应使用 Active LTS 或 Maintenance LTS。
- 💼 超过 Maintenance LTS 阶段的版本可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获得商业支持。
- 📊 发布表列出各版本代号、首次发布、最后更新和状态；当前 v27 为 Alpha，v26、v24 Krypton、v22 Jod 为 LTS，v25、v23、v20 等为 EOL。
- 🧰 下载页提供 CLI、操作系统包管理器（如 brew）和版本管理器（如 nvm）等非交互安装方式。
- 🏷️ 下载页将安装方式分为“推荐”和“社区”，兼顾灵活选择与精选入门列表。
- ⭐ “推荐”方式需与官方发布同步、使用未修改的官方二进制（无预编译时才从源码构建）、支持多版本并存，并与 Node.js 项目保持紧密沟通。
- 🌐 “社区”方式需支持所有受支持的非 EOL 版本、至少在一个官方支持 OS 上运行且不限于少数发行版、免费开源且非商业付费产品。
- 📝 任何人都可提议新的安装方式，但最终由 Node.js 项目决定是否收录。

---

### [构建持久耐用的后台 AI 智能体 | Master.dev](https://master.dev/courses/background-ai-agents/?utm_source=email&utm_medium=nodeweekly&utm_content=aiagentscooper)

**原文标题**: [Build Durable Background AI Agents | Master.dev](https://master.dev/courses/background-ai-agents/?utm_source=email&utm_medium=nodeweekly&utm_content=aiagentscooper)

本课程由 Netflix 的 Scott Moss 主讲，时长约 5 小时，教你在 TypeScript/Node.js 环境中构建可持续运行的后台代理：以结账服务故障分流为项目，结合 OpenAI 与 Inngest，把“观察—决策—行动”循环落地为可靠工作流，并通过确定性目标检查、持久化步骤、等待与恢复、人工审批和安全重试，让代理在无人值守时仍保持可控。

- 🧠 区分后台代理与聊天代理：后台代理更持久、更高效，适合持续监控并自动处理任务。
- 🔁 核心循环是“观察状态 → LLM 选择动作 → 执行 → 记录结果 → 继续循环”，服务状态就是代理所处的“世界”。
- 🛡️ 审批与安全检查应由 harness 执行，而不是交给 LLM；LLM 只通过结构化输出选择下一步动作。
- 🧪 课程项目是 checkout-service triage agent：接收告警、检查日志与变更，并执行如禁用功能等操作。
- 🧱 单步循环不够持久，需用 Inngest 拆成可记忆、幂等的步骤；工作流代码必须保持确定性。
- 💾 Inngest 保存步骤检查点，Postgres 保存业务状态；恢复时重放缓存步骤结果，而不是恢复 JavaScript 调用栈。
- 🧩 多步循环会在每轮校验运行状态，并把观察、生成报告、完成运行等异步操作分别放入独立步骤。
- ⚠️ 安全重试依赖稳定的 action ID：由 run、cycle、action 派生，避免重复执行；步骤应幂等且不混装多个破坏性操作。
- ⏳ 等待与恢复使用 waitForEvent 处理 incident-updated、审批或帮助事件，并支持超时；代理可主动选择等待或请求帮助。
- 🧑‍💼 人在回路以收件箱为接口：代理提出需审批动作，harness 保存状态快照；审批后重读提案并检查状态是否过期。
- ✅ 测试覆盖功能故障、依赖故障恢复、发布回滚审批与请求帮助；活动流可追踪每轮的观察、决策和结果。
- 🚀 收尾包含 HITL、不确定知识与评估等练习，并介绍 DBOS、Temporal、Vercel Workflows、Upstash 等替代方案。

---

### [Node.js — 2026年10月21日星期三安全版本发布](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

**原文标题**: [Node.js — Wednesday, October 21, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

2026年10月21日，Node.js 针对 26.x、24.x、22.x 发布安全更新，修复多个安全漏洞，最高严重性为 HIGH，并同步更新 c-ares、ca-cert、OpenSSL、SQLite、Undici 等依赖。建议受影响用户尽快升级到 v26.12.1、v24.22.1、v22.23.4。

- 📅 发布信息：安全版本于 2026 年 10 月 21 日发布，覆盖 26.x、24.x、22.x 发布线，三个版本线的最高严重性均为 HIGH。
- ⬆️ 升级版本：Node.js v26.12.1、v24.22.1、v22.23.4；End-of-Life 版本在安全发布时始终受影响，应使用受支持的最新版本。
- 📦 依赖更新：包括 c-ares、ca-cert（应对 eMudhra Intermediate CA 泄露）、OpenSSL、SQLite、Undici。
- 🌐 高危 DNS 漏洞：`dns.resolve*()` 和 `dns.reverse()` 会截断含 NUL 字节的主机名，可能绕过域名白名单并解析攻击者控制的域名（CVE-2026-105482）。
- 🔒 高危 TLS 漏洞：使用全角数字写法的 IPv4 地址（如 `１２７.0.0.1`）可绕过证书主机名/IP SAN 校验（CVE-2026-105483，影响 26.x、24.x）。
- 🔒 高危 TLS 漏洞：带前导零的非规范 IPv4（如 `0127.0.0.1`）在不同解析规则下可能被验证为另一个 IP 地址（CVE-2026-106069）。
- 💥 高危 Brotli 漏洞：畸形 Brotli 压缩数据可导致越界写，可能引发崩溃、内存泄露或远程代码执行（CVE-2026-111497）。
- 🧩 中危 HTTP 漏洞：keep-alive 连接复用可能接受在请求发送前已到达的响应，造成响应混淆（CVE-2026-105481）。
- 🧩 中危 TLS 漏洞：非规范 IPv4 写法（如 `0177.0.0.1`、`0x7f.0.0.1`、`2130706433`、`127.1`）可让仅含 DNS SAN 的证书认证 IP 端点（CVE-2026-106072）。
- 🎲 中危 crypto 漏洞：`randomUUID()`、`randomUUIDv7()`、`randomInt()` 的熵缓存可能被写入启动快照或 SEA，导致多个进程产生重复且可预测的值（CVE-2026-106074）。
- 🗜️ 低危 ZipFile 漏洞：ZIP 头校验失败后可能返回攻击者控制的前缀字节，影响基于 Node.js 的扫描器判断（CVE-2026-106070，影响 26.x）。
- 🛡️ 低危权限模型漏洞：通配符 radix 查找可能越权授予路径访问（CVE-2026-106071，影响 26.x）；`fs.realpathSync()` 缺少读权限检查可绕过 Permission Model（CVE-2026-106073）。
- 📣 后续建议：遵循 Node.js 安全策略，按 `SECURITY.md` 报告漏洞，并订阅 nodejs-sec 获取安全公告。

---

### [Node.js — 2026年10月21日（星期三）安全版本发布](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases#nodejs-brotli-decoder-out-of-bounds-write-permits-remote-code-execution-cve-2026-111497---high)

**原文标题**: [Node.js — Wednesday, October 21, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases#nodejs-brotli-decoder-out-of-bounds-write-permits-remote-code-execution-cve-2026-111497---high)

Node.js 项目于 2026 年 10 月 21 日发布 26.x、24.x、22.x 安全更新，修复多个高危漏洞，最高严重性为 HIGH，建议尽快升级。

- 🚨 本次安全发布覆盖 Node.js 26.x、24.x、22.x，最高严重性为 HIGH，三个发布线均受影响。
- 📦 同步更新 c-ares、ca-cert（eMudhra 中间 CA 泄露）、OpenSSL、SQLite、Undici 等依赖，以修复公开漏洞。
- 🌐 CVE-2026-105482（高危）：`dns.resolve*()` 和 `dns.reverse()` 会静默截断含 NUL 字符的主机名，可能绕过域名允许列表；影响 26.x、24.x、22.x。
- 🔐 CVE-2026-105483（高危）：TLS 主机名校验未将全角数字 IPv4（如 `１２７.0.0.1`）识别为 IP，证书 DNS SAN 可能错误认证 IP 端点；影响 26.x、24.x。
- 🔢 CVE-2026-106069（高危）：带前导零的非规范 IPv4（如 `0127.0.0.1`）在 WHATWG 规则与系统解析器间解释不一致，可能用另一 IP 的证书完成认证；影响 26.x、24.x、22.x。
- 💥 CVE-2026-111497（高危）：内置 Brotli 解码器存在越界写入，恶意压缩数据可导致内存损坏、崩溃、信息泄露或远程代码执行；影响 26.x、24.x、22.x。
- 🔁 CVE-2026-105481（中危）：HTTP Agent 复用 keep-alive 套接字时，可能把请求发送前已到达的响应当作新请求的响应；影响 26.x、24.x、22.x。
- 🧾 CVE-2026-106072（中危）：非规范 IPv4 拼写（如 `0177.0.0.1`、`0x7f.0.0.1`、`2130706433`、`127.1`）可能让仅含 DNS SAN 的证书认证 IP 端点；影响 26.x、24.x、22.x。
- 🎲 CVE-2026-106074（中危）：`crypto.randomUUID()`、`randomUUIDv7()`、`randomInt()` 的熵缓存可能被写入启动快照和 SEA，导致多个进程重复或可预测的值；影响 26.x、24.x、22.x。
- 🗜️ CVE-2026-106070（低危）：`zlib.ZipFile` 在 ZIP 头校验失败后可能返回攻击者控制的前缀字节；影响 26.x。
- 📁 CVE-2026-106071（低危）：Permission Model 通配符 radix 查找可能过度授权，例如 `--allow-fs-read=/etc/passwd.*` 也可能允许读取 `/etc/passwd`；影响 26.x。
- 🔎 CVE-2026-106073（低危）：Permission Model 下 `fs.realpathSync()` 缺少读权限检查，可检查文件存在性、解析符号链接并枚举受限目录外路径；影响 26.x、24.x、22.x。
- ⬇️ 新版本为 Node.js v26.12.1、v24.22.1、v22.23.4，建议按发布计划升级。
- ⚠️ End-of-Life 版本在安全发布时始终受影响；应使用受支持的最新版本以确保安全。
- 🛠️ Maintenance LTS 之后的商业支持可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获取。

---

### [Node2Shell：从 Brotli 数据到远程代码执行 | Imperva](https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/)

**原文标题**: [Node2Shell: From Brotli Data to Remote Code Execution | Imperva](https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/)

overview summary
- 🛡️ Imperva 红队将 CVE-2026-111497 命名为 Node2Shell，这是 Node.js 内置 Brotli 解码器中的高危越界写入漏洞，可导致远程代码执行。
- 🎯 官方受影响版本涉及 Node.js 22.x、24.x、26.x；修复版本为 22.23.4、24.22.1 和 26.12.1。
- 🧪 在官方 Node.js 24.22.0 Linux arm64 镜像中，PoC 可通过 Brotli 响应或请求体执行攻击者代码，无需调试器或插桩；相同输入在 24.22.1 上被拒绝。
- 🔁 攻击路径包括 Node.js 内置 fetch() 消费外部 Brotli 响应，以及 Express 5.0.0–5.3.0 和 body-parser 2.0.0–2.3.0 解码传入请求体。
- ⚠️ Express 和 body-parser 只是触发路径，漏洞根源在 Node.js 原生解码器；普通 Node.js HTTP 服务器不会仅因收到 Brotli 请求体就自动解码。
- 🧬 技术原因是解码器在无效流状态下继续处理，可能造成越界写入；上游修复使解码器对非法转换返回格式错误。
- ✅ 防御优先事项是更新受影响 Node.js 运行时，包括容器镜像和其他捆绑 Node 二进制的制品，并排查不可信 Brotli 数据进入运行时的路径。
- 🚧 更新期间可临时限制受影响路径上的不可信 Brotli 流量；Imperva 已添加并验证针对该 CVE 的 WAF 规则，可用于虚拟补丁争取修复时间。
- 🤖 文章指出 AI 正加速漏洞发现与利用开发，防守方从披露到修复的窗口更短，补丁速度需跟上攻击工具演进。
- 📌 该 PoC 并非每次尝试都成功，测试范围限于特定 Linux arm64 构建和应用配置；完整修复仍依赖更新 Node.js 运行时。

---

### [CVE-2026-111181：body-parser 中的拒绝服务漏洞 · Express.js](https://expressjs.com/en/blog/2026-10-28-cve-2026-111181/)

**原文标题**: [CVE-2026-111181: Denial of service in body-parser · Express.js](https://expressjs.com/en/blog/2026-10-28-cve-2026-111181/)

该文章披露了 Express `body-parser` 中间件中的拒绝服务漏洞 CVE-2026-111181：攻击者可通过单个请求触发未捕获异常并使服务器进程崩溃。问题源于解压缩流在请求解析完成后仍保持打开，且 `body-parser` 未附加 `error` 监听器；当请求体包含有效 gzip 数据、零字节及后续填充数据时，解码器报错无人处理，最终导致进程崩溃。

- 🚨 **漏洞编号**：CVE-2026-111181，属于 Express `body-parser` 的拒绝服务漏洞。
- 💥 **核心影响**：恶意客户端可用单个请求使服务器崩溃；若解析器全局挂载在认证之前，无需匹配有效路由或通过认证即可触发。
- ⚙️ **根本原因**：解压缩流在请求解析结束后仍存活，继续接收数据；`body-parser` 未给该流添加 `error` 监听器。
- 🧨 **触发机制**：请求体包含有效 gzip 成员、零字节和额外数据，解码完成后后续字节继续流入解码器并触发错误，最终变成未捕获异常。
- 🌐 **受影响范围**：`body-parser` 2.0.0 至 2.3.0，以及 1.20.8 及更早版本；标准 Express 4 或 5 应用同样可能受影响。
- 🛡️ **修复版本**：升级至 `body-parser` 2.4.0 或更高版本，或 1.20.9 或更高版本。
- ⚠️ **临时缓解**：若不需要压缩请求体，可设置 `inflate: false` 拒绝编码请求；但该做法会拒绝压缩请求体，需要支持时应升级。

---

### [](https://github.com/nodejs/TSC/pull/1900)

**原文标题**: [Should nodejs/node#63869 (`--experimental-strip-private-modules`) land? by github-actions[bot] · Pull Request #1900 · nodejs/TSC · GitHub](https://github.com/nodejs/TSC/pull/1900)

overview summary
Node.js TSC 已投票通过并合并 nodejs/node#63869，新增 `--experimental-strip-private-modules`，仅在 `node_modules` 链上所有包裹包均为私有包时，允许对 TypeScript 文件进行类型剥离。

- 🧱 当前 Node.js 拒绝从 `node_modules` 下的 TypeScript 文件剥离类型，并抛出 `ERR_UNSUPPORTED_NODE_MODULES_TYPE_STRIPPING`，以防未编译 TS 成为注册表发布包的入口。
- 🚩 PR #63869 提案增加 `--experimental-strip-private-modules` 实验性标志，使特定 `node_modules` 场景可进行类型剥离。
- 🔒 启用条件：从目标文件向上，`node_modules` 链中每个包的根 `package.json` 都必须含 `"private": true`；嵌套 `package.json` 被忽略。
- ⛔ 链中任意位置出现非私有包（例如已发布包捆绑私有包）即拒绝剥离；npm 兼容客户端也不会发布 `"private": true` 的包。
- 🎯 预期用途是被复制而非符号链接进 `node_modules` 的工作区包，如 `pnpm deploy` 输出、Docker 构建上下文和 vendored 代码。
- 🧩 “Do not land”选项主张 `node_modules` 中的类型剥离仍只通过 loaders 支持；该选项未获胜。
- 🗳️ TSC 投票于 2026-10-15 结束，最终参与率 94.44%；“Land”以 1 胜 0 负击败“Do not land”。
- ✅ 该提案获批准并合并到 `main`（2026-10-25），随后删除投票分支；扩展至非私有包仍为文档明确的非目标。
- ⚠️ 部分提交因删除文件、触碰多个文件或同一作者已有更新投票提交而被排除计票。

---

### [模块：新增 --experimental-strip-private-modules，作者 marco-ippolito · 拉取请求 #63869 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63869)

**原文标题**: [module: add --experimental-strip-private-modules  by marco-ippolito · Pull Request #63869 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63869)

overview summary
Node.js 已合并 PR #63869，新增实验性参数 `--experimental-strip-private-modules`，允许仅对 `node_modules` 中标记为 `private: true` 的包进行 TypeScript 类型剥离，目标是支持 monorepo/私有包开发，同时明确不推动公共 registry 直接发布未编译 `.ts` 入口。

- 🚀 新增 `--experimental-strip-private-modules` 标志，限制类型剥离只发生在私有 `node_modules` 包内。
- 📦 该 PR 是 #63853 的后续，作者为 marco-ippolito，最终合入 `nodejs:main`，合并提交为 `2052d0d`。
- 🔒 TypeScript 团队表示可接受，并强调公共 registry 包不应以未编译 `.ts` 作为入口；`private: true` 限制被视为折中方案。
- 🧪 讨论中要求补充文档说明 `private` 字段，并增加测试覆盖私有包内相对导入 TypeScript 文件的情况。
- ⚠️ 有审查者担忧 `private` 不能可靠判断包是否来自 registry，且增加复杂度；作者回应称该设计依赖 registry 拒绝发布 `private: true` 根包，对大多数用户足够。
- 🗳️ TSC 就该项目发起投票并最终通过，PR 带有 `semver-minor`、`strip-types` 等标签。
- ✅ 合并时 CI 共 79 项检查通过；Codecov 显示补丁覆盖率约 89.86%，主要缺失覆盖集中在 `src/node_modules.cc`。

---

### [Electron 45 | Electron](https://www.electronjs.org/blog/electron-45-0)

**原文标题**: [Electron 45 | Electron](https://www.electronjs.org/blog/electron-45-0)

Electron 45 已发布，核心升级至 Chromium 156.0.8078.48、V8 15.6 和 Node v24.22.0；重点提升启动、菜单与原生 API 性能，并新增本地 AI Prompt API、macOS 系统通行密钥、Windows 崩溃报告增强、ASAR 直读和 Perfetto 原生堆分析等能力，同时包含多项需要迁移适配的破坏性变更。

- 📦 可通过 `npm install electron@latest` 安装，或从 Electron releases 网站下载。
- ⚡ 性能优化：沙盒渲染器启动时避免加载 Electron JS bootstrap（除非启用 `webviewTag`）；macOS 冷启动预取框架文件；菜单构建与显示更快；窗口、视图、WebContents 的原生方法与属性调用开销降低。
- 🧩 沙盒 preload 破坏性变更：不再内置 `Buffer`、`setImmediate`、`clearImmediate` 以及 `events`、`timers`、`url` 模块 shim；`require()` 仅支持 `electron`、`electron/renderer`、`electron/common`，需改用 Web API 或自行打包 polyfill。
- 🖥️ 屏幕共享权限变更：截屏、窗口或标签页捕获现在以 `display-capture` 权限传给 `session.setPermissionRequestHandler()`；只允许 `media` 的处理器需同时允许 `display-capture`，否则屏幕共享会失效。
- 🤖 实验性 Prompt API：新增 `session.registerLocalAIHandler()`、`localAIHandler` 模块和 `LanguageModelUtility` 类，应用可在 utility process 中提供自己的本地模型实现；Electron 不内置模型或推理引擎。
- 🔐 macOS 系统通行密钥：`app.configureWebAuthn()` 支持 `platformPasskeys: true`，可调用 Apple 原生通行密钥面板；新增 `select-webauthn-authenticator` 事件用于在 Touch ID 与系统通行密钥间选择。
- 🧨 Windows 崩溃报告增强：新增 WER helper，使 `crashReporter` 可捕获 `__fastfail` 等绕过进程内处理器的崩溃；需将 `electron_wer.dll` 与可执行文件一同打包，并在重命名 exe 时同步重命名 DLL。
- 📁 ASAR 直读：`fs.open()`、`fs.createReadStream()`、`fs.copyFile()`、`fs.cp()` 等直接读取 ASAR 内文件，不再解压临时副本；大型打包文件冷读最高快 100 倍，但返回的文件描述符仅适用于 Node `fs`，写入类操作会失败。
- 🌐 网络、认证与下载事件增强：`webRequest` 和 `protocol` 请求新增 `initiatorOrigin`；`DownloadItem` 新增 `getInitiatorOrigin()`；`will-download` 和 `preconnect` 事件新增请求 `frame` 参数，便于按 frame 制定权限与网络策略。
- 📊 Perfetto 原生堆分析：`contentTracing.startRecording()` 支持 `nativeHeapProfiling`，可采样 C/C++ 原生内存分配；替代 `contentTracing.enableHeapProfiling()`，且所有 `contentTracing` 录制改用 Perfetto protobuf 格式。
- 🪟 其他改进：macOS app shims、Linux `Notification` 操作按钮、实验性 `protocol.registerSource()`、`disableWakeLocks`、`webFrame.getIsolatedWorlds()`、`ELECTRON_DEBUG_DRAGGABLE_REGIONS` 调试变量、macOS `autoUpdater` 流式下载/断点续传/二进制增量更新等。
- ⚠️ 其他破坏性变更：沙盒 preload 事件发射器改用原生 `EventEmitter`；iframe 创建的 Worker 需同时启用 `nodeIntegrationInSubFrames` 才获得 Node 集成；扩展 preload 遵循嵌入 frame；WebContents 捕获需使用 `chromeMediaSource: 'tab'`；非沙盒窗口的 `window.open()` 子窗口默认进入独立沙盒进程；`document.requestStorageAccessFor` 默认禁用；同步 `safeStorage` 方法已弃用并将在 Electron 46 移除。
- 🛑 Electron 42.x.y 已结束支持，建议升级到受支持版本；升级前应阅读迁移指南和破坏性变更文档。

---

### [GitHub Actions 工作流锁定文件现已正式可用 - GitHub 更新日志](https://github.blog/changelog/2026-10-28-github-actions-workflow-lockfiles-are-generally-available/)

**原文标题**: [GitHub Actions workflow lockfiles are generally available - GitHub Changelog](https://github.blog/changelog/2026-10-28-github-actions-workflow-lockfiles-are-generally-available/)

GitHub Actions 工作流依赖锁文件已正式可用，覆盖 GitHub Enterprise Cloud、带数据驻留的 Enterprise Cloud、Team 和 Free 计划；它允许工作流保留可读的标签/分支引用，同时实际运行已锁定的确切提交，即使这些引用后续发生移动。

- 📅 该功能于 2026 年 10 月 28 日发布，从公开预览转为正式可用。
- 🔒 可使用 GitHub CLI 的 `gh actions-lock` 扩展生成 `.github/workflows/actions.lock`，锁定 Actions 及其传递依赖。
- 🧩 支持逐步采用：可逐个接入工作流；已接入工作流的每个依赖都必须存在于锁文件中，并运行其记录的提交。
- 🔄 当 Dependabot 为已接入工作流中的 Action 发起版本更新时，会在同一 PR 中自动重新生成对应的锁文件条目，无需额外配置。
- 🛡️ 企业、组织和仓库管理员可通过“Require lockfile”策略强制要求使用锁文件。
- ✅ 可检查锁文件是否过期且不修改文件，适合用于 CI 检查。
- ⚠️ 锁文件有助于防止依赖发生意外变更，但并不能判断依赖是否安全，锁定前仍需审查依赖。
- 🚀 入门方式是安装 `gh-actions-lock` 扩展，审查并提交生成的锁文件与工作流变更，并参考 GitHub Docs 的工作流依赖锁文件文档。

---

### [Web 承受不起 JavaScript 运行时的单一文化——console.log()](https://redmonk.com/kholterhoff/2026/10/27/js-runtime-monoculture/)

**原文标题**: [The Web Can’t Afford a JavaScript Runtime Monoculture – console.log()](https://redmonk.com/kholterhoff/2026/10/27/js-runtime-monoculture/)

文章担忧 JavaScript 运行时正在重演浏览器时代的“单一文化”：Deno 团队加入 Cloudflare、Deno 运行时将在一年后停止开发，使 Node.js、Bun、Cloudflare workerd 成为少数主要选择，独立实现减少可能削弱 Web 的竞争、标准和抗风险能力。

- 🧭 Deno 团队加入 Cloudflare，Ryan Dahl 宣布 Deno 运行时将在一年后停止开发，Web 由此剩下更少的主流通用运行时。
- 🪟 文章以 IE6 为警示：缺乏竞争导致开发者迁就单一浏览器怪癖，直到 Firefox、Safari、Chrome 等替代品恢复竞争。
- 🌐 浏览器引擎也在整合：Blink 从 WebKit 分叉后，Opera 与 Edge 相继转向 Chromium，如今多数用户使用的浏览器集中在少数引擎上。
- 🔁 服务端曾有类似经历：Node.js 停滞促使 io.js 分叉，竞争压力最终推动 Node.js 回归中立基金会治理。
- 🚀 Deno 虽未超越 Node，却推动了 TypeScript、权限安全、Web API、测试工具等特性进入 Node 生态，体现竞争对创新的价值。
- ⚠️ 服务器运行时多依赖浏览器引擎：Node、Deno、Cloudflare 使用 V8，Bun 使用 JavaScriptCore，独立实现减少会让最流行实现的行为默认成为标准。
- 🧩 标准通常需要两个独立实现；若 WinterTC 等标准场合的独立声音减少，标准化可能更受单一实现支配。
- 💥 单一文化会“共同失败”：文章以 OpenSSL 的 Heartbleed 和 V8 漏洞为例，说明多样性不能消除 bug，但能限制影响范围。
- 🛠️ Deno 退出可能削弱竞争压力；Bun 对速度、Deno 对安全与工具链的推动，都会因挑战者减少而受损。
- 🌱 已出现 Ende、Dodo 等 Deno 分支，显示独立实现仍有活力，但也暴露治理、资源和可持续性的风险。
- 🗣️ Cloudflare 的 James Snell 强调“没有选择绝非好事”，Node、Bun、Deno 及 JSR、npmx 等多样尝试才能推动生态前进。
- ✅ 结论：Web 曾因人们持续建设并资助替代方案而走出 IE6 时代；如今 JavaScript 运行时需要刻意维护多样性，避免创新与韧性被整合削弱。

---

### [Reylo — 将 .sql 文件导入 TypeScript，完全类型化](https://reylo.dev/)

**原文标题**: [Reylo — Import .sql files into TypeScript, fully typed](https://reylo.dev/)

overview summary
Reylo 是一个基于 TypeScript 7.1 content mappers 的工具，让 TypeScript 直接导入 `.sql` 文件，并从实时开发数据库推断参数、列、可空性、行数和 JSON 类型。它支持 Postgres、MySQL 和 SQLite，无代码生成，需连接开发数据库，并可通过运行时/构建插件与现有数据库驱动集成。

- 🧩 核心机制：TypeScript 7.1 将 `.sql` 文件交给 Reylo，Reylo 让数据库 prepare 查询但不执行，再读取 catalog 返回精确类型。
- 💪 完整 SQL 能力：支持数据库原生 SQL 语法、函数和操作符，避免手写重复类型，schema 变更后类型随数据库同步。
- 🎯 类型推断覆盖广：参数类型、列类型、可空性、基数、枚举、聚合、窗口函数、左连接、子查询、`returning`、嵌套 JSON 等均可推断。
- 🗄️ 数据库支持：Postgres 14–18（含 Neon、PGlite）、MySQL 8.0.22+（含 PlanetScale）、SQLite（含 D1、Durable Objects、Turso、libSQL）。
- 🔌 自带驱动：通过 `.run(db, params)` 使用 `pg`、`postgres.js`、`mysql2`、`better-sqlite3`、Drizzle 等；支持事务、`.try()`、`.runSync()`、`.with()`。
- ⚙️ 安装要求：TypeScript 7.1 beta、Node 24+、运行中的开发数据库；安装 `reylo`、对应 `@reylosql/*` 包和 TypeScript beta。
- 🛠️ 配置方式：在 `tsconfig.json` 配置 content mapper，typecheck 使用 `tsc --noEmit --runExternalCode`；运行时用 `--import reylo/register` 或 Vite、Next.js、esbuild、webpack、Rspack、Jest、Cloudflare 插件。
- 🧭 数据库连接：通过 `DATABASE_URL` 或 `.reylo.yaml` 的 `direct_url` 指向开发库；支持 env 文件、变量插值和命令替换，建议直连而非事务池。
- 🧠 参数与类型控制：`:name` 自动推断，必要时用 `:q::text` 强制转换；`nullable(...)` 支持可空参数；无法推断时报错，或用 `strict_params: false` 设为 `unknown`。
- 🧱 高级查询能力：动态排序/过滤、JSON Schema 参数校验、列表过滤、批量插入、嵌套插入、`oneOf` 判别联合、嵌套 JSON 聚合都可类型化。
- 🚨 错误检查：SQL 错误在 `.sql` 文件行列显示；重复列名、`order by` 参数、错误参数类型等会报错；查询改动会导致调用方类型错误。
- 🖥️ 编辑器支持：需 TypeScript 7 扩展并指向项目 TypeScript；VS Code/Cursor/Zed 可配置 content mapper；Zed 中 `.sql` 内部错误仅在 `tsc` 显示。
- 🧪 缓存与 CI：`.reylo/` 按 schema 指纹缓存分析结果，自带 `.gitignore`，不应提交；CI 需启动数据库、应用迁移并设置 `DATABASE_URL`。
- 📈 可观测性：通过 Node tracing channel `reylo:query` 发布查询、参数、客户端、结果或错误，便于接入 span 和监控。
- ⚠️ 限制：类型检查和构建需要 live DB；Reylo 不负责迁移；日期为 ISO 字符串、64 位整数为 `bigint`、decimal 为精确字符串；MIT 许可。

---

### [宣布 TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/#content-mappers)

**原文标题**: [Announcing TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/#content-mappers)

TypeScript 7.1 Beta 已发布，重点新增环境模块导入属性、Source Phase Imports、`es2026` 目标、全新 API、内容映射器（Content Mappers），并带来显著性能与内存优化；同时包含更严格的分布式类型参数检查等行为变更。

- 🚀 **发布与安装**：TypeScript 7.1 Beta 于 2026 年 10 月 20 日发布，可通过 `npm install -D typescript@beta` 安装体验。
- 📦 **环境模块支持导入属性**：新增 `declare module "*" with { type: "css" | "text" | "bytes" }` 等写法，可根据导入属性提供正确类型，并在缺少必需属性时报错。
- ⚠️ **导入属性限制**：匹配环境模块声明的导入不会校验磁盘文件；这些声明也不会内置到 TypeScript 库中，建议由终端项目自行声明。
- 🧩 **Source Phase Imports**：支持 `import source` 与动态 `import.source()`，返回 `AbstractModuleSource`；WebAssembly 导入可得到 `WebAssembly.Module`，并可用于 `WebAssembly.instantiate`。
- 🔁 **Source Import 特性**：Source Imports 保持身份一致性，可用于 `Map`、`Set` 和可靠比较；需要合适的 `--module`、`--lib` 或 `--target` 配置。
- 🎯 **新增 `es2026` 目标**：`--target es2026` 和 `--lib es2026` 成为稳定选项，包含 `Math.sumPrecise()`、`Iterator.concat()`、`JSON.rawJSON()`、`Error.isError()`、`Map/WeakMap.getOrInsert()`、`Uint8Array` Base64/Hex 方法、`Array.fromAsync()` 等。
- 📚 **新增库方法**：`--lib esnext` 增加 `Promise.allKeyed`、`Promise.allSettledKeyed`，以及 `Iterator.zip`、`Iterator.zipKeyed`、`chunks`、`join`、`includes` 等提案方法。
- 🛠️ **全新 TypeScript 7.1 API**：拆分为 `typescript/sync`、`typescript/async`、`typescript/fs`、`typescript/ast`、`typescript/ast/is`、`typescript/ast/factory` 等入口，支持同步/异步编译客户端、AST 操作和文件系统抽象。
- ♻️ **快照与增量更新**：API 以 Snapshot 为核心，可通过 `api.createSnapshot` 创建、`snapshot.update()` 派生新快照，复用 Program ID 并保留旧快照信息；相关对象需用 `using` 或手动释放。
- 🗂️ **文件系统 API**：提供 `createFileSystem`、`createFileSystemWithLib`、`createFileSystemLayer`，支持虚拟文件系统、分层覆盖、内存中编译及 `emitToString()`。
- 🧑‍💻 **Content Mappers**：Volar 核心模型成为一等公民，可为 `.vue`、`.svelte`、`.astro`、MDX、CSS Modules 等嵌入式格式提供虚拟表示和映射；通过 `tsconfig.json` 的 `contentMappers` 注册，命令行需 `--runExternalCode`。
- ⚡ **性能与内存优化**：加入大量编译、类型检查、AST、缓存和内存布局优化；示例项目中速度提升约 1.2x–1.9x，耗时降低约 13%–47%，内存降低约 16%–50%。
- 🧠 **行为变更**：对分布式类型参数启用更严格检查，部分现有代码可能报错；DOM 相关 `lib.d.ts` 更新也可能影响类型检查。
- 🔭 **后续计划**：团队将继续改进速度与稳定性，预计约一个月后发布 Release Candidate，随后推出正式版。

---

### [ClickHouse 托管 Postgres | ClickHouse](https://clickhouse.com/campaigns/clickhouse-managed-postgres?utm_source=nodeweekly&utm_medium=sponsored-content&utm_campaign=2026-10-29_SponsoredLink_Clickhouse)

**原文标题**: [ClickHouse Managed Postgres | ClickHouse](https://clickhouse.com/campaigns/clickhouse-managed-postgres?utm_source=nodeweekly&utm_medium=sponsored-content&utm_campaign=2026-10-29_SponsoredLink_Clickhouse)

ClickHouse Managed Postgres 提供企业级、可扩展的 Postgres，并与 ClickHouse 原生集成，面向实时与 AI 驱动应用；它用 Postgres 处理事务、ClickHouse 处理分析，构成统一数据栈并降低复杂度。目前已登陆 AWS，GCP 处于私有预览，并提供 30 天免费试用和 300 美元额度。

- 🚀 产品定位：高性能、可扩展、企业级 Postgres，原生集成 ClickHouse，适合实时和 AI 应用。
- 🧩 统一数据栈：Postgres 负责事务，ClickHouse 负责分析，减少额外复杂性。
- ☁️ 可用与试用：AWS 已可用，GCP 私有预览；提供 30 天免费试用和 300 美元信用额度。
- ⚡ NVMe 性能：本地 NVMe 存储带来超低磁盘延迟，I/O 密集负载最高快 10 倍，避免 EBS 限流和网络抖动。
- 🔄 ClickHouse 集成：支持 Postgres 到 ClickHouse 的原生 CDC、快速复制，并通过 pg_clickhouse 统一查询。
- 🛡️ 企业级能力：高可用、自动备份、时间点恢复、端到端加密、私有网络，基础设施由 Ubicloud 支持。
- 🔓 开源优先：基于 Postgres、ClickHouse、PeerDB 和 pg_clickhouse，无厂商锁定，数据可控。
- 🏎️ OLTP 表现：微秒级延迟、数百万 IOPS，优于传统 SSD，降低尾延迟并加速 VACUUM、检查点和逻辑复制。
- ♻️ 高可用设计：最多两个专用备用实例用于 HA，读副本单独提供；WAL 归档支持备份和 PITR。
- 📈 实时复制：Postgres 数据实时复制到 ClickHouse，分析最高快 100 倍，复制延迟低至数秒，支持初始快照与 CDC 增量更新；ClickPipes 已在数百家企业生产验证，未来将增强亚秒级复制等能力。
- 🔍 统一查询层：pg_clickhouse 可从 Postgres 直接查询 ClickHouse，支持下推连接、过滤、聚合和函数；22 个 TPC-H 查询中 14 个完全下推，带来 60 倍以上加速，并持续扩展 CTE、窗口函数等。
- 💬 客户反馈：有客户从 Aurora 迁移后运行约 8.5 TB 热数据，NVMe 低延迟表现突出；也有客户看重性能、兼容性和可靠性，称其简化 CDP 架构并完成多 TB 工作负载迁移。

---

### [一个（大致）一致的 npm 依赖图 | vlt /](https://www.vlt.io/blog/consistent-ish-graph)

**原文标题**: [A consistent(-ish) npm dependency graph | vlt /vōlt/](https://www.vlt.io/blog/consistent-ish-graph)

近年来，大型开源项目常以 monorepo 方式批量发布大量相互依赖的 npm 包，导致依赖图在发布初期并不一致。文章指出，很多包在依赖尚未可用时就已上架；npm 发布时不校验依赖，扫描与分阶段发布又拉长了不可用窗口。为此，文章所述 registry 调整了复制系统：若传递依赖尚未发布，会暂时保留发布，提升依赖图可靠性；大多数发布可在几分钟内协调完成，少数会等待至多一小时。

- 📦 大型项目常在一个 monorepo 中维护大量互相依赖的包，并批量发布变更。
- ⚠️ 发布者往往并行发布所有包，而不是先发布依赖、等待可用后再发布依赖方。
- 🧾 npm 在发布时不会验证依赖是否存在，因此包可能引用尚未发布、甚至永远不会存在的依赖。
- 📉 最近 24 小时有 175,891 个新版本发布，其中 22%（38,995 个）存在无法解析的依赖。
- ⏳ npm 的扫描和分阶段发布流程增加了新版本不可用的时间窗口，使“最终一致性”问题更明显。
- 🐞 Effect-TS 和 Cloudflare Wrangler 等案例显示，依赖图只部分可用会直接阻碍用户安装。
- 🛠️ 所述 registry 会暂时保留发布，等待传递依赖也发布后再放出，以提供更一致的依赖图。
- ⏱️ 96% 的发布事件可在几分钟内完成协调发布；剩余 4% 最多等待一小时，超时后仍会释放。
- 🔄 该系统会处理生态中常见的循环依赖，但忽略 git 仓库等可变、非 registry 依赖。
- 🔍 剩余问题多来自依赖、peer 依赖或可选依赖根本不存在，可能涉及公司内部私有包。
- 📈 团队将继续观察生态发布与消费习惯，并可能调整策略和超时时间。

---

### [node:vfs：Node.js 中的虚拟文件系统](https://blog.platformatic.dev/article-slug-node-vfs-nodejs-virtual-filesystem)

**原文标题**: [node:vfs: Virtual Filesystems in Node.js](https://blog.platformatic.dev/article-slug-node-vfs-nodejs-virtual-filesystem)

Node.js 的 `node:vfs` 已从提案走向核心实现，目标是让应用无需改动依赖，就能从内存、ZIP、单可执行文件等非磁盘存储中读取文件并解析模块。核心变化包括：挂载点由 Node.js 统一分配、不再支持覆盖真实路径；模块解析仍沿用 Node.js 原有算法；并新增 ZIP、SEA、原生插件、`node:ffi` 与启动参数支持。该功能仍属实验性，需要 `--experimental-vfs`。

- 🚀 `node:vfs` 首个版本随 Node.js 26.4.0 发布，26.9.0 增加模块加载器集成、ZIP Provider、原生插件加载和 SEA 支持，26.10.0 增加 VFS 支持的 FFI 与启动挂载参数。
- 🧩 VFS 将存储 Provider 与类似 `fs` 的 API 结合，可用于内存测试夹具、打包配置读取、生成代码导入相邻模块等场景。
- 📌 `mount()` 不再接收自定义挂载点，而是返回 Node.js 分配的隔离命名空间；POSIX 下形如 `/dev/null/vfs/0`，但这是实现细节，应使用 `mount()`、`mountPoint` 或 `mountPointURL`。
- 🚫 新模型不支持覆盖真实路径或回退到磁盘；挂载路径下缺失的文件就是缺失，不会静默落到真实文件系统。
- 🧭 模块解析仍由 Node.js 原有解析器负责；挂载点作为解析根，包作用域和 `node_modules` 向上查找会在此停止。
- 🔗 虚拟模块与真实模块可以互相导入，因此这是解析边界，不是执行边界；卸载挂载会清理相关加载缓存，但不会停止已运行代码。
- 🗂️ 内置公开 Provider 包括 `MemoryProvider`、`RealFSProvider`、`ZipProvider`，`VirtualProvider` 用于自定义实现；不同 Provider 能力不同，例如 ZIP 在 26.10.0 不支持递归 `readdir`、符号链接和监听。
- 📦 可使用 `node:zlib` 的实验性 ZIP API 创建压缩归档，再通过 `ZipProvider` 直接挂载并导入入口模块，无需先解压到目录。
- ⚠️ ZIP 默认只读，可写归档通过文件句柄关闭时提交新条目；同步压缩和解压可能阻塞事件循环，打包为 ZIP 不保证启动更快。
- 🛡️ 文章明确纠正：VFS 和 `RealFSProvider` 不是沙箱、权限系统或访问控制机制；不可信代码仍需操作系统级隔离或独立进程。
- 🔐 启用 Node.js Permission Model 时，挂载需显式 `--allow-fs-vfs`；这只是允许使用挂载机制，不代表多租户隔离。
- 🧱 SEA 可通过 `"useVfs": true` 将资产挂载为只读 VFS 并从其中运行主脚本，支持 CommonJS 和 ESM；但目前不能与 `useSnapshot` 或 `useCodeCache` 组合。
- 🧬 可从 VFS `require()` `.node` 原生插件；Node.js 会读取字节并创建私有自清理映像，Linux 使用匿名内存文件描述符，其他平台可能用临时文件。
- 🛠️ `node:ffi` 的 `dlopen()` 和 `DynamicLibrary` 可从挂载路径加载共享库，使用与原生插件类似的私有映像机制；仍需匹配目标平台、ABI 和函数签名。
- 🧹 已打开的 FFI 库有独立生命周期，卸载 VFS 不会自动卸载库；在 Permission Model 下原生调用还需 `--allow-ffi`。
- ⚙️ 26.10.0 新增 `--vfs-load=app.zip` 和 `--vfs-mount` 启动参数，可直接挂载并运行入口；目录使用 `RealFSProvider`，ZIP 根据内容选择 `ZipProvider`。
- 🔌 新增 `registerProvider({ name, canHandle, create })`，允许预加载模块注册自定义格式，注册 Provider 会优先于内置 Provider 检查。
- 🔄 原先“从 `@platformatic/vfs` 一行迁移到 `node:vfs`”的说法过于宽泛；`@platformatic/vfs` v0.5.0 已适配新挂载 API，但用户态兼容层仍无法提供核心的 ZIP、SEA 和原生插件加载能力。
- ✅ 核心价值仍然成立：普通应用代码可通过常规 `fs` 和模块解析 API 访问不同存储 Provider 中的文件；但依赖自定义挂载点、覆盖层或核心未导出 Provider 的代码需要重构。

---

### [GitHub - sverweij/dependency-cruiser：验证并可视化依赖关系。你的规则。JavaScript、TypeScript、CoffeeScript。ES6、CommonJS、AMD。 · GitHub](https://github.com/sverweij/dependency-cruiser)

**原文标题**: [GitHub - sverweij/dependency-cruiser: Validate and visualize dependencies. Your rules. JavaScript, TypeScript, CoffeeScript. ES6, CommonJS, AMD. · GitHub](https://github.com/sverweij/dependency-cruiser)

dependency-cruiser 是一个用于校验和可视化 JavaScript、TypeScript、CoffeeScript 等项目依赖关系的开源工具，支持自定义规则、生成依赖图，并以文本、图形、HTML 等多种格式报告违规。项目采用 MIT 许可证，在 GitHub 上约有 7.3k stars、307 forks，累计 2,482 次提交。

- 🧭 核心功能：遍历项目依赖，按自定义规则进行校验，并报告被违反的规则。
- 🛠️ 支持语言与模块：JavaScript、TypeScript、CoffeeScript、LiveScript，以及 ES6、CommonJS、AMD、JSX、TSX、Vue、Svelte 等。
- 📦 安装方式：可通过 npm、yarn 或 pnpm 安装为开发依赖。
- ⚙️ 初始化配置：运行 `npx dependency-cruiser --init` 可生成适配项目的 `.dependency-cruiser.js` 配置文件。
- 🖼️ 依赖图生成：结合 GraphViz 的 `dot` 命令，可输出 SVG 等依赖关系图。
- ✅ 规则校验：运行 `npx dependency-cruiser src` 可按规则检查依赖，并以类似 ESLint 的格式显示违规。
- 📝 示例规则：可禁止测试目录外的代码依赖测试目录，规则包含名称、说明、严重级别和路径条件。
- 📊 多种输出：支持文本、dot、CSV、HTML、Mermaid、JSON 等报告和可视化格式。
- 🔍 内置常见规则：初始化配置会包含循环依赖、package.json 缺失依赖、孤立模块、生产代码依赖 dev/optionalDependencies 等检查。
- 🧩 扩展能力：支持 Webpack alias/modules、其他 alt-js 语言及自定义输出格式。
- 🤘 项目自检：dependency-cruiser 在自身构建流程中也使用自身进行依赖检查。

---

### [](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples.md)

**原文标题**: [dependency-cruiser/doc/real-world-samples.md at main · sverweij/dependency-cruiser · GitHub](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples.md)

本文介绍 dependency-cruiser 在真实开源项目中的依赖分析示例，展示如何生成高层、目录级和模块级依赖图，并提供复现命令与配置方法。

- 🧩 文档列举多个 npm 流行项目：Commander、Chalk、Yarn Berry、React、safe-regex、resolve、Yargs 等。
- 🗺️ dependency-cruiser 可把大项目的模块及其依赖合并并着色，生成更易理解的高层依赖图，且支持自定义配置。
- 🧶 Yarn 2（Berry）示例需通过 Yarn 本地脚本运行 dependency-cruiser，以适应 PnP 解析。
- ⚛️ React 示例提供基线检查和架构图脚本，可生成高层依赖 SVG/HTML 图。
- 🔷 支持直接分析 TypeScript 项目，无需单独转译；tslint 示例中橙色线标出围绕 barrel `index.ts` 的循环依赖警告。
- ☕ 同样直接支持 CoffeeScript；示例中一个不可解析模块来自构建脚本生成的解析器代码。
- 🛠️ dependency-cruiser 也用自身做示例，展示高层、文件夹和模块三种抽象层级，并通过自定义主题区分主要部分。
- 🚫 dependency-cruiser 自身仓库是唯一不能直接使用 `depcruise` 等命令的场景，需要直接运行 `bin` 下的 JavaScript 文件。
- 🎨 state-machine-cat 示例使用 `flat` 报告器，仅用颜色表示分组，并在节点中标注文件夹名，而不是聚类模块。
- 📈 mscgen.js 等项目也作为真实案例，用于展示将文本 DSL 转换为序列图的依赖关系图。

---

### [获取失败](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/3.x/migration-guide.md)

**原文标题**: [Failed to retrieve](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/3.x/migration-guide.md)

无法总结：获取内容失败，状态码 429。

---

### [打包：你的 Node 应用，一个已签名文件](https://bundle.pipobscure.com/)

**原文标题**: [bundle: your Node app, one signed file](https://bundle.pipobscure.com/)

bundle 是一个实验性工具，旨在把 Node.js 应用及其依赖冻结为单个可签名、可校验、可复现的归档文件，让分发和安装更透明，减少对 npm 安装流程和安装脚本的依赖。

- 📦 将 Node 应用打包为单一签名文件，接收方无需执行 `npm install`，Node 可直接从文件中运行应用。
- 🧊 发布时一次性冻结完整依赖树，生成标准 ZIP；相同文件生成相同归档，便于任何人重建并比对。
- 🔐 一个签名覆盖整个文件，任意字节被修改都会导致校验失败；默认使用 Sigstore，也支持自有 CA。
- ⚠️ 签名只证明“是谁构建的、字节未被改动”，并不证明应用安全；账号被劫持后仍可能签出恶意包，因此仍需审计与证明。
- 🛠️ 发布流程分为四步：运行并记录实际读取的文件、创建归档、审计（可与上一版本基线对比）、签名。
- 🚀 可通过 `bundle run` 或 `bundle sea` 独立可执行文件在运行前校验；但通过 `#!` 按名称启动不会自动校验。
- 🧾 `bundle install` 会先展示签名者、审计证明和警告，再按用户策略决定是否安装；安装过程不运行安装脚本。
- 🌐 证明、列表和套件是 Atmosphere/atproto 账户中的记录，发布者、审计者和用户各自控制自己的数据与信任策略。
- 🧩 套件可一次安装一组应用或插件，但每个成员仍需单独审查；插件也是签名 bundle，按应用安装并通过普通 `import` 加载。
- 📊 相比 npm、Docker 和编译二进制，bundle 无需安装时访问注册表、通常不运行安装代码、字节一致，并可用 `unzip` 查看内容。
- 🧪 目前仍是实验性方案，需要 Node 26.11.1 或更高版本及 `--experimental-vfs`；它不是沙箱，也不保证安全。
- 📥 可从最新 release 下载 `bundle.nzip`，用 Node 运行其 `install` 将签名后的 `bundle` 放入 PATH；也可通过 `npm install @pipobscure/bundle` 使用库和插件加载器。

---

### [gpuix-svelte · 使用 Svelte 构建原生桌面应用](https://gpuix-svelte.stanislav.garden/)

**原文标题**: [gpuix-svelte · Build native desktop apps with Svelte](https://gpuix-svelte.stanislav.garden/)

gpuix-svelte 可将 Svelte 5 组件直接渲染为 macOS、Windows 和 Linux 上 GPU 加速的原生桌面应用，无需浏览器或 WebView，并可通过 Node 或 Bun API 访问用户计算机上的能力。它基于 GPUI 和 Svelte 的实验性自定义渲染器，提供热重载、样式、测试、打包和 AI 友好文档等完整开发体验。

- 🖥️ **跨平台原生应用**：支持 macOS、Windows、Linux，使用 Metal、DirectX、Vulkan 进行 GPU 加速渲染。
- ⚡ **快速开始**：需要 Node.js 24+ 或 Bun 1.4+；通过 `npm create gpuix-svelte@latest my-app` 或 `bun create gpuix-svelte my-app` 创建项目，安装后运行启动。
- 🔧 **工作原理**：利用 Svelte 自定义渲染器将组件编译为原生 GPUI 节点，经 `@gpuix/native` Rust 插件和 `applyBatch` 每帧提交，无 DOM 或 WebView。
- 🔥 **热重载**：保存 `App.svelte` 后窗口就地更新，并支持状态在重载后保留。
- 🎨 **样式支持**：支持 scoped `<style>`、类规则、`:hover` 和 flexbox；HTML 标签映射到固定原生标签集，不支持标签回退为 `div` 并警告。
- 🖱️ **交互差异**：鼠标事件不冒泡，使用 `hitbox="self"` 让子元素点击到达父元素；无 `bind:`，输入通过事件值或 `{@attach}` 处理；键盘可用 `on_window_key`。
- 🧪 **内置测试**：可无头挂载组件并进行真实命中测试点击，无需窗口；也可从其他进程驱动运行中的应用。
- 🤖 **AI 友好**：starter 包含 `AGENTS.md`，文档以 `llms.txt` 形式发布，便于 AI 代理使用。
- 📦 **打包发布**：`npm run build` 将应用、运行时和 GPUI 打包为单个可执行文件；支持 Windows、macOS、Linux，macOS 可签名和公证，也可通过 GPUI WebAssembly 在浏览器运行。
- 📚 **丰富示例**：提供计数器、井字棋、样式游乐场、控制中心、Hacker News、桌面 API 和 12 步交互教程等示例。
- ❤️ **社区支持**：可在 GitHub 赞助项目发展，也可提交 issue 或 PR 展示作品。

---

### [](https://gpui.rs/)

**原文标题**: [GPUI](https://gpui.rs/)

GPUI 是一个面向 Rust 的快速、混合即时模式与保留模式、GPU 加速的 UI 框架，由 Zed 和 Delta 的创作者开发，并提供文档、示例与开源贡献入口。

- 🚀 **核心定位**：高性能 Rust UI 框架，结合即时模式与保留模式，并利用 GPU 加速渲染。
- 🧑‍💻 **背景来源**：由 Zed 与 Delta 的创作者打造，与 Zed 生态紧密相关。
- 🪟 **示例能力**：示例展示如何创建 500×500 居中窗口，并使用 flex 布局、间距、背景色、边框、阴影、文字样式及子元素色块构建界面。
- 📚 **文档资源**：提供 Docs、README、GPUI API 文档、示例、上下文说明、按键事件分发说明，以及 Zed crates 和 UI crate 中的更多内容。
- 🤝 **开源贡献**：GPUI 是开源项目，欢迎参与改进；近期贡献需提交到 Zed 仓库并与其保持同步。

---

### [GitHub - khromov/gpuix-svelte：使用 Svelte 和 GPUI 为 Mac、Windows 和 Linux 构建原生桌面应用 · GitHub](https://github.com/khromov/gpuix-svelte)

**原文标题**: [GitHub - khromov/gpuix-svelte: Build native desktop apps for Mac, Windows and Linux with Svelte and GPUI · GitHub](https://github.com/khromov/gpuix-svelte)

gpuix-svelte 是一个基于 Svelte 自定义渲染器和 GPUI 构建原生桌面应用的实验性项目，可把 Svelte 组件直接渲染到 GPU 加速的原生窗口中，支持 macOS、Windows 和 Linux。

- 🧱 项目定位：用 Svelte 编写 Mac、Windows、Linux 原生桌面应用，底层通过 `@gpuix/native` 与 GPUI（Zed 编辑器的 UI 框架）通信。
- ⚠️ 实验性质：依赖 Svelte 尚未发布的 custom renderer API，每个版本绑定特定 Svelte 构建，次版本升级可能有破坏性变更。
- 🚀 快速开始：运行 `npm create gpuix-svelte@latest my-app`，进入目录后执行 `npm install` 和 `npm start`，即可打开计数器窗口并支持热重载。
- 🖥️ 环境要求：需要 Node.js 24+ 或 Bun 1.4+；支持 macOS Apple Silicon、Windows x64、Linux x64；GPUI 二进制随 npm 预构建提供。
- 🐧 Linux 依赖：需 `libxcb`、`libxkbcommon`、`libxkbcommon-x11`；Wayland 和 X11 均可用，GNOME Wayland 下可能需要自绘标题栏。
- 🧩 Svelte 能力：支持 runes、snippets、`{#each}`、`{#if}`、`{#await}`、`<svelte:boundary>`、`.svelte.ts` 状态模块和 scoped `<style>` 类规则。
- 🎨 渲染与样式：元素映射为 GPUI 元素，如 `div`、`text`、`img`、`svg`、`input`、`textarea`、`markdown`、`virtual-list` 等；样式使用 CSS 和 flexbox，长度支持 `px`、`rem`、部分 `%` 和 `auto`。
- 🖱️ 交互差异：点击事件基于指针下元素，可用 `hitbox="self"` 让图标/徽章点击冒泡到父元素；输入通过事件报告值，没有 `bind:`；键盘快捷键通过 `on_window_key` 处理。
- 🧰 内置组件：提供 `Scroller`（含虚拟列表）、`Portal`、`Tooltip`、`Popover`，以及原生 `<anchored>`。
- 🪟 桌面能力：覆盖窗口标题、全屏、文件选择器、文件拖放、原始像素图像、焦点和无障碍属性等 API。
- 📦 现有项目接入：安装 `gpuix-svelte` 即可，它自带 Svelte；通过包内 bin 启动入口文件，例如 `gpuix-svelte app.ts`，Bun 下可加 `--bun`。
- 🛠️ TypeScript 配置：需要 `paths` 指向包内嵌套的 Svelte 构建，并配置 `gpuixHTML` namespace、`customConditions` 和 `types`；`starter/` 提供可复制配置。
- 🧪 示例丰富：仓库包含计数器、井字棋、Hacker News 阅读器、毛玻璃控制中心、样式演示、桌面 API 演示、WebGPU 浏览器版和 12 步交互教程。
- 🔄 Svelte 版本管理：每个 gpuix-svelte 版本捆绑并锁定其测试过的 Svelte 构建，用户不应在 `package.json` 中单独添加 `svelte`，升级前应阅读 changelog。
- ⚙️ 工作原理：维护 JavaScript 影子树并投影到 GPUI 扁平树，仅元素和非空文本创建原生节点；每帧变更批量发送给 Rust，在下次绘制前应用。
- 📚 文档与贡献：提供样式、组件、指南、测试、发布等文档；测试支持无头点击、截图和驱动运行窗口；项目采用 MIT 许可证。

---

### [sqlite-js-stream：为 Node.js 重写的 Litestream](https://blog.platformatic.dev/sqlite-js-stream-litestream-nodejs)

**原文标题**: [sqlite-js-stream: Litestream Rewritten for Node.js](https://blog.platformatic.dev/sqlite-js-stream-litestream-nodejs)

sqlite-js-stream 是 Litestream 的 TypeScript/Node 移植版，使用内置 `node:sqlite` 与 Node 原生类型剥离，可直接运行 `.ts`，无需构建步骤。它把 SQLite 的 WAL 持续备份为兼容 Litestream 的 LTX 文件，核心价值是让 SQLite 灾备以 npm 包形式融入现有 Node 部署流程。整个移植由本地 AI 编码代理完成，但架构、评审和关键范围决策由人类负责。

- 🎯 **核心定位**：sqlite-js-stream 是 Litestream 的 TypeScript 版，用于 Node，利用 `node:sqlite` 与原生类型剥离，无需构建步骤。
- 📦 **分发优势**：作为 npm 包运行在应用进程内，无需 sidecar 二进制、配置文件或额外版本管理，可跑在主事件循环、worker thread 或 serverless 中，显著降低 SQLite 生产使用门槛。
- 🧩 **存在原因**：SQLite 是单机文件数据库，直接 `cp` 正在写入的数据库会得到损坏快照；WAL 中已提交数据还可能被 checkpoint/truncate，因此需要理解 WAL 并暂停 checkpoint 才能做一致性备份。
- 🔄 **工作原理**：把 WAL 流式转为 LTX 文件，每个文件包含单事务变更页面，恢复时按顺序重放；LTX 格式与 Litestream 兼容，双方生成的文件可互读。
- 🧱 **主要能力**：提供驱动无关的 Replica API；支持端到端流式 `sync()/snapshot()`、`restore()`、LTX v0.5.2/CRC-64、与 Litestream 匹配的分层压缩与保留策略，以及基于 `lock.json` 的分布式租约，S3 上用条件写避免双主。
- 📊 **基准数据**：本地文件后端、小库测试中，sync 约 180–250 ms、15–21 MB/s WAL、400–480k rows/s、峰值 RSS 约 106 MB；restore 约 330–360 ms、7–8 MB/s、280–300k rows/s、峰值 RSS 约 114 MB。
- 🧠 **内存结论**：WAL 从 1.87 MB 增至 7.72 MB（4.1x）时，峰值 RSS 仅从 99.8 MB 增至 121.2 MB（1.22x），说明内存受页缓冲约束而非数据库大小；但这不是与 Go 版 Litestream 的直接性能对比。
- 🚧 **关键限制**：它是灾难恢复工具，不是分布式数据库；租约只选单一写入者，不合并/比较/协调多主机数据，多主机共享前缀仅适用于逻辑数据相同的灾备场景；故障切换会丢失主库最后几秒未备份数据。
- 🧪 **AI 参与**：整个移植由 pi 代理驱动 DeepSeek V4 Flash Vision 本地模型完成，运行在两台 NVIDIA DGX Spark 上；采用 TDD，121 个测试（103 核心 + 18 S3）在 Node 24 下全绿，机械性移植表现好。
- ⚠️ **AI 边界**：代理曾误解需求，去实现旧版 v0.3.x 恢复路径和另一套 LZ4 帧编解码，被人评审后叫停；架构与范围判断仍由人类负责，本地模型约束反而强化了规格与测试。
- 📌 **项目状态**：仍处早期，GCS/Azure/SFTP/NATS、VFS 镜像、IPC server 未实现，核心包尚未发布；格式兼容仍是难点，作者致谢 Ben Johnson 的 Litestream 与 `superfly/ltx`。

---

### [Litestream - 流式 SQLite 复制](https://litestream.io/)

**原文标题**: [Litestream - Streaming SQLite Replication](https://litestream.io/)

告别缓慢、复杂且脆弱的软件系统，改为在单台服务器上安全运行应用，并获得低成本、无痛的全复制数据库体验。

- 🚀 停止构建缓慢、复杂、脆弱的软件系统
- 🖥️ 在单台服务器上安全运行应用程序
- 🗄️ 提供全复制数据库，省心且成本低
- ✅ 立即开始使用

---

### [如何检测自动化电子商务结账机器人](https://fingerprint.com/blog/how-to-detect-checkout-bots/?utm_source=NodeWeekly102926&utm_medium=newsletter)

**原文标题**: [How to Detect Automated E-Commerce Checkout Bots](https://fingerprint.com/blog/how-to-detect-checkout-bots/?utm_source=NodeWeekly102926&utm_medium=newsletter)

文章说明智能体商务正在改变结账请求的形态：`complete_checkout` 往往不再来自浏览器，而是平台后端或 AI agent 通过 REST/MCP 直接调用 API，因此传统基于页面和 JavaScript 的机器人检测会失效。Fingerprint 的 Automation Intelligence API 可仅凭 HTTP 请求元数据检测自动化，并建议同时检查“调用方”和 UCP signals 中提供的“买家”。

- 🤖 Agentic commerce 让结账请求从浏览器页面转向平台后端或 AI agent 的直接 API 调用，没有页面加载、JavaScript 执行或可供浏览器检测脚本运行的上下文。
- 🧩 UCP Checkout 的 REST 绑定包含五个操作：创建、获取、更新、完成、取消结账会话，均位于 `/checkout-sessions` 下。
- 🔐 每个 UCP 请求必须携带 `UCP-Agent`、`Idempotency-Key` 和 `Request-Id` 头；平台还可使用 RFC 9421 HTTP Message Signatures 认证。
- 🔁 MCP 是另一种绑定：同样五个操作以 `tools/call` 到达单一 MCP 端点，操作名在 `params.name`，载荷在 `params.arguments`，但检测所需的 headers、method、URL、IP 不变。
- 🛡️ Automation Intelligence API 通过 headers、method、URL、IP 检测自动化，无需 JavaScript agent，适合 AI agent、MCP 服务器和后端到后端流量。
- 👥 UCP 集成应区分两个检测对象：caller 是实际打开 HTTP 连接的一方，信息始终来自原始请求；buyer 是平台声称正在完成购买的人，信息来自可选的 UCP `signals`。
- 📡 Caller 检测调用 `POST /edge`，请求体需包含 `headers`、`method`、`url`，以及 `ipv4_address` 或 `ipv6_address` 至少一项；可用 `linked_id` 关联 checkout session。
- 🪪 支持 Web Bot Auth：转发 `Signature-Agent`、`Signature-Input`、`Signature` 头后，Fingerprint 会服务端验签，`bot_info.identity` 可返回 `signed`。
- 📊 响应中 `bot_info` 只在检测到机器人时出现；`identity` 可为 `verified`（身份已确认）、`signed`（WBA 验签通过）、`unknown`（识别为自动化但无可验证身份）、`spoofed`（声称身份无法验证）。
- 🧾 Buyer 检测使用 UCP `signals` 中的 `dev.ucp.buyer_ip` 和 `dev.ucp.user_agent`，可做代理、VPN、数据中心、地理等 IP 情报；仅传 User-Agent 输入较弱，但仍有用，且可在流程早期运行。
- ⚖️ 组合判断建议：caller 为 `signed`/`verified` 且无 buyer 信号时通常无需复查；caller 为 `spoofed` 应优先审查；caller 干净但 buyer IP 指向数据中心或 VPN 时，可作为更广风险模型的输入；无 buyer 信号在 agent 发起的购买中很常见。
- 🗂️ 建议将 caller 和 buyer 两个事件或至少两个 `event_id` 与 checkout 关联存储，交由风控逻辑综合决策。
- 🚧 Automation Intelligence API 目前处于 Public Preview，响应 schema 可能变化；UCP 仍在活跃开发并按日期版本化，本文基于 `2026-04-08` 版本。

---

### [发票解析：将PDF数据转换为结构化JSON](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/invoice-parsing-pdf-to-structured-json/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=nodeweekly_20261029)

**原文标题**: [Invoice Parsing: Turn PDF Data into Structured JSON](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/invoice-parsing-pdf-to-structured-json/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=nodeweekly_20261029)

本指南比较 2026 年面向 AI 智能体的 10 款 PDF MCP 服务器，帮助读者根据具体任务，从免费本地阅读器到可转换、编辑和保护文件的云 API 中做出选择，并提前评估文档去向、完整工作流成本与安全缺口。

- 📄 并非所有 PDF MCP 服务器都能满足 AI 智能体的实际需求，选型需匹配具体任务。
- 🔟 指南对比了 10 种方案，覆盖免费本地阅读器与云端 API。
- 🛠️ 功能范围包括 PDF 转换、编辑和文件安全保护。
- 📍 需关注每款服务器将文档发送到哪里，以及数据流向是否合规。
- 💰 应评估完整工作流的真实成本，而不只是单项功能价格。
- 🔐 连接前要识别并补齐安全缺口，降低文档泄露或滥用风险。

---

### [](https://github.com/paulmillr/chokidar/releases/tag/6.0.0)

**原文标题**: [Release 6.0.0 · paulmillr/chokidar · GitHub](https://github.com/paulmillr/chokidar/releases/tag/6.0.0)

Chokidar 发布 6.0.0 最新版本，核心是围绕单一观察管线重写 watcher，并通过 lstat、stat、readdir 确认后端回调后再发出事件，确保突发变更后的最终状态与文件系统一致。该版本引入原生递归监听、共享原生句柄和自有 stat 轮询，同时带来多项 API 变更、错误修复与兼容性调整，并要求 Node.js 22.22 或更高版本。

- 🚀 **重大重构**：watcher 改为单一观察管线，后端回调仅视为失效信号，经文件系统确认后才发出事件。
- 📁 **原生递归监听**：新增 `fs.watch({ recursive: true })` 支持；默认 `auto` 后端在 macOS/Windows 使用原生递归，其他平台按目录监听。
- 🔗 **句柄与轮询优化**：跨 watcher 共享原生句柄并按目录打开，修复 macOS 监听大量文件时的 `EBADF`；用 Chokidar 自有 stat 轮询替代 `fs.watchFile`，并共享轮询循环。
- ⚙️ **API 变更**：新增 `backend` 选项（`auto`、`native`、`native-recursive`、`polling`）；`interval`/`binaryInterval` 更名为 `pollingInterval`/`pollingBinaryInterval`，旧名保留为弃用别名。
- 🛑 **行为调整**：轮询模式下 `atomic` 默认改为 `false`；`close()` 变为终态，关闭后 `add()` 会抛错；构造函数会校验无效选项并抛出 `TypeError`。
- 🧩 **接口与兼容性**：`add()` 错误改为 `error` 事件；`getWatched()` 返回 null-prototype 对象以支持 `__proto__` 目录；调整 `ignored` 对父目录的过滤逻辑。
- 🐛 **关键修复**：修复工作目录被删除导致 100% CPU 循环、监听文件系统根目录产生大量 `unlink`/`unlinkDir`、macOS socket 的 `UNKNOWN` 错误、符号链接 `ENOTDIR` 阻断监听等问题。
- 🪟 **平台与竞态修复**：修复 Windows 多文件写入误报 `change`、重复 `add` 事件、目录被同名文件替换时挂起、重命名含子目录的监听目录等问题；并修复新增目录扫描与注册之间漏文件等竞态。
- 🔄 **监听恢复与节流**：被删除后重建的监听路径会从最近存在的父目录继续等待；事件节流不再丢弃更新，窗口关闭时会重放最新差异变更。
- 📦 **其他维护**：`Stats` 改为仅类型导入，固定开发依赖并限制工作流权限；完整变更见 `5.0.0...6.0.0` 变更日志。

---

### [GitHub - verdaccio/verdaccio：一个轻量级的 Node.js 私有代理注册表 · GitHub](https://github.com/verdaccio/verdaccio)

**原文标题**: [GitHub - verdaccio/verdaccio: A lightweight Node.js private proxy registry · GitHub](https://github.com/verdaccio/verdaccio)

Verdaccio 是一个面向 Node.js 的轻量级私有 npm 代理 registry，强调零配置、内置小型数据库、公共 registry 缓存与插件化存储扩展，适合企业私有包管理和 CI/E2E 测试。

- 🧱 Verdaccio 是轻量级 Node.js 私有代理 registry，无需完整数据库即可启动。
- 🔁 可代理 npmjs.org 等公共 registry，并缓存下载模块；支持 uplinks 串联多个 registry。
- 🔌 支持社区插件扩展存储能力，如 Amazon S3、Google Cloud Storage，也可自研插件。
- 🧾 版本要求：v6 需 Node.js 22+；master/next 分支需 Node.js 24+。
- 📦 支持 npm、yarn、pnpm 全局安装，也支持 Docker 和官方 Helm chart。
- 🚀 快速使用：运行 `verdaccio`，默认地址为 `http://localhost:4873`，设置 registry 后可用 `npm adduser` 和 `npm publish`。
- ✅ 兼容标准 npm 功能：install/update、publish/unpublish、dist-tag、deprecate、用户管理、token、search、ping、audit 等。
- 🧪 广泛用于 E2E 测试，CI 覆盖 npm 10/11/12、Yarn 3/4、pnpm 10/11、bun 和 deno 最新版。
- ⚠️ 当前不支持 PM2 cluster 模式，使用可能导致未知行为。
- 🏢 被 n8n、create-react-app、Grafana、Docusaurus、Gatsby、Babel.js、pnpm 等项目使用。
- 📄 项目采用 MIT 许可；文档和 logo 采用 Creative Commons 许可。
- 💰 由志愿者维护，接受捐赠与赞助，暂无专门资助贡献或安全研究的资金。

---

### [Verdaccio 7 有哪些新功能 | Verdaccio](https://www.verdaccio.org/blog/2026/10/25/verdaccio-7-release/)

**原文标题**: [What's new in Verdaccio 7 | Verdaccio](https://www.verdaccio.org/blog/2026/10/25/verdaccio-7-release/)

Verdaccio 7 是自托管 npm 兼容 registry 的重大版本，核心是让发布更可控、插件体系更现代、运行时升级到 Node.js 24 与 Express 5，并带来 Web UI、包过滤、通知、搜索与下载可靠性改进；日常安装和发布命令不变，但升级前需重点检查配置、认证与插件兼容性。

- 🧪 分阶段发布（实验性）：通过 `stage` 标志启用，需 npm 11.17+，版本先上传待审核，批准后才可安装，并提供版本状态端点供流水线等待。
- 🔐 双因素认证（实验性）：通过 `tfa` 标志启用，使用 TOTP 保护账户操作、登录和发布；启用前需检查客户端与存储要求。
- 🛡️ 所有权与撤回更严格：`publish.check_owners` 扩展到 `deprecate`、版本撤回和 dist-tag 变更；撤回版本需要单独的撤回权限。
- 📦 发布完整性增强：拒绝非法附件名，tarball 完整写入后才记录上传，失败发布不会留下阻塞同版本重新发布的残留。
- 🔌 插件新基础：支持纯 ESM 插件，存储插件改用 Promise/async API，旧回调插件可通过兼容适配器迁移。
- ⚙️ 运行时升级：要求 Node.js 24+ 与 Express 5；中间件路由语法和嵌入式服务器 API 有变化，推荐使用命名导出 `runServer`。
- 🖥️ Web UI 改进：新增深色模式、按更新时间排序、作用域包搜索优化、登录/注册/密码页面刷新，以及首页筛选/作用域/排序工具栏和分步首次发布欢迎卡，并支持 bun。
- 🚦 包过滤与通知：包过滤支持 allow/block、glob 模式和排除弃用版本；通知覆盖 publish 与 unpublish 事件。
- 🔎 搜索与下载修复：改进作用域包搜索、旧存储插件搜索和多 uplink 下载；搜索增加限流、分页限制和批量权限检查。
- ⚠️ 升级前检查：仅接受 YAML 配置；包 API 请求需 Bearer token，旧 `_auth` 需迁移到 `_authToken`；服务器密钥需 32 字符；旧 `/-/all` 搜索和 star/unstar 已移除。
- 🐳 试用方式：Node.js 24+ 下可运行 `pnpm dlx verdaccio` 或 `npx --yes verdaccio`；Docker 镜像 `verdaccio/verdaccio:7` 已发布为 `latest`，留在 6.x 需固定 `:6`。
- 🙌 社区与支持：感谢贡献者、赞助商和 Open Collective 捐赠者，建议在 GitHub Discussions 或 Discord 反馈插件与发布流程体验。

---

### [GitHub - avajs/ava：让你自信开发的 Node.js 测试运行器 🚀 · GitHub](https://github.com/avajs/ava)

**原文标题**: [GitHub - avajs/ava: Node.js test runner that lets you develop with confidence 🚀 · GitHub](https://github.com/avajs/ava)

AVA 是一个面向 Node.js 的测试运行器，主打简洁 API、详细错误输出、对新语言特性的支持以及线程隔离，帮助开发者更自信地开发；项目在 GitHub 上约有 2.08 万 Star、1500 Fork，采用 MIT 许可证，并提供多语言 README 翻译。

- 🚀 定位：Node.js 测试运行器，强调速度、简洁和可靠性。
- ⭐ 社区数据：约 20.8k Stars、1.5k Forks、216 Watchers、51 Issues、15 PRs、2109 次提交。
- ⚡ 核心特性：最小化且快速、简单测试语法、并发运行测试、原子化测试、无隐式全局变量。
- 🧩 开发支持：内置 TypeScript 定义，支持 Promise、async 函数和 Observable。
- 🔍 调试体验：Magic assert 提供代码片段、清晰 diff、语法高亮和增强断言信息，并自动清理无关堆栈。
- 🧪 隔离与并行：每个测试文件拥有隔离环境；CI 中可自动并行运行并检测支持并行构建的环境。
- 📦 安装使用：运行 npm init ava，或 npm install --save-dev ava / yarn add ava --dev；需本地安装，不能全局运行。
- 📝 配置示例：package.json 中设置 "type": "module" 和 "test": "ava"；测试文件使用 import test from 'ava'。
- ▶️ 执行方式：npm test、npx ava，或 npx ava --watch 开启监听模式。
- 🧭 支持范围：支持 Node.js 官方仍支持的各主版本的最新版本；提供 TAP reporter。
- 📚 文档与生态：包含测试编写、断言、快照、CLI、配置、超时、常见陷阱、TypeScript、覆盖率等文档与食谱；相关包有 eslint-plugin-ava、@ava/typescript、@ava/cooperate、@ava/get-port。
- 🗣️ 名称与社区：名称写作 AVA，发音 /ˈeɪvə/；通过 GitHub Discussions 获取支持，并欢迎贡献。

---

### [发布 v8.1.0 · avajs/ava · GitHub](https://github.com/avajs/ava/releases/tag/v8.1.0)

**原文标题**: [Release v8.1.0 · avajs/ava · GitHub](https://github.com/avajs/ava/releases/tag/v8.1.0)

AVA 发布 v8.1.0，新增字符串快照的代码块格式化支持，并带来显著的性能提升；包含代码块的快照需使用 AVA 8.1 或更新版本读取，而不含代码块的快照仍保持向后兼容。

- 🚀 版本 v8.1.0 已发布，包含 10 个提交。
- 🧩 新增 `t.snapshot(expected, {formatAsCodeBlock}, message?)` 重载，仅当 `expected` 为字符串时可用。
- 💾 字符串会按原样存储，并在 `.snap.md` 文件中渲染为围栏代码块；`formatAsCodeBlock` 可设为 `true`，或设为非空语言标识符（如 `'js'`）以启用语法高亮。
- ⚠️ 含代码块的快照只能由 AVA 8.1 或更新版本读取；不含代码块的快照及已有快照仍向后兼容。
- ⚡ 性能提升：大量小型测试文件的启动速度约提升 40%，单文件包含数千个测试时约提升 30%，多文件并发运行时约提升 50%。
- 🔧 主要变更包括改进启动与测试运行性能（#3460），以及支持字符串快照的代码块格式化（#3449）。
- 👥 贡献者：novemberborn 和 sindresorhus。

---

### [GitHub - pillarjs/path-to-regexp：将诸如 `/user/:name` 的路径字符串转换为正则表达式 · GitHub](https://github.com/pillarjs/path-to-regexp)

**原文标题**: [GitHub - pillarjs/path-to-regexp: Turn a path string such as `/user/:name` into a regular expression · GitHub](https://github.com/pillarjs/path-to-regexp)

path-to-regexp 是一个用于将 `/user/:name` 这类路径字符串转换为正则表达式的 JavaScript 库，常用于 Express/Node.js 路由匹配，支持解析、匹配、编译和字符串化路径，并提供参数、通配符与可选片段等语法。

- 📦 安装方式：使用 `npm install path-to-regexp --save`，主要导出 `match`、`pathToRegexp`、`compile`、`parse`、`stringify`。
- 🔤 参数匹配：使用 `:foo` 定义参数，可匹配单个路径段，例如 `/:foo/:bar` 可匹配 `/test/route` 并返回参数对象。
- 🌟 通配符：使用 `*splat` 定义跨多个路径段的通配参数，匹配结果以数组形式返回。
- 🧩 可选片段：使用花括号定义可选部分，例如 `/users{/:id}/delete` 可匹配带或不带 `id` 的路径。
- 🎯 `match`：返回用于匹配字符串的函数，支持字符串、`TokenData` 对象或数组，并可配置 `decode`。
- 🧮 `pathToRegexp`：返回正则表达式和 `keys`，支持 `sensitive`、`end`、`delimiter`、`trailing` 等选项。
- 🔄 `compile`：执行反向转换，将参数对象编译为路径，支持 `encode` 配置和通配符数组输入。
- 🧷 `stringify`：将 `TokenData` 对象转换回 Path-to-RegExp 路径字符串。
- 🛠️ `parse`：将路径字符串解析为 `TokenData`，供 `match` 和 `compile` 使用，支持 `encodePath`。
- ⚠️ 使用限制：该库适用于有序数据（如路径、主机名），不适合查询字符串、URL 片段、JSON 等任意顺序数据。
- 🚫 错误与兼容性：不再支持旧版 `?`、`+`、正则字符等写法；通配符必须有名称；与 Express <= 4.x 存在兼容性变化。
- 📈 项目信息：MIT 许可证，约 8.6k stars、491 forks、65 watchers，面向 expressjs、nodejs、router 等场景。

---

### [发布 v9.0.0 · pillarjs/path-to-regexp · GitHub](https://github.com/pillarjs/path-to-regexp/releases/tag/v9.0.0)

**原文标题**: [Release v9.0.0 · pillarjs/path-to-regexp · GitHub](https://github.com/pillarjs/path-to-regexp/releases/tag/v9.0.0)

path-to-regexp 发布 v9.0.0（最新版），由 blakeembrey 发布。该版本转为仅支持 ESM，并要求 Node.js >=22；主要不兼容变更是同一路径段中两个及以上参数的模糊匹配从“首个参数贪婪”改为“最后一个参数贪婪”。例如 `/:file.:ext` 匹配 `/foo.json.html` 现在得到 `["foo","json.html"]`，v8 则为 `["foo.json","html"]`；此改动可提升正则性能，并便于构建非正则匹配器。

- 📦 v9.0.0 为最新发布版本，于 10 月 22 日发布，发布者为 blakeembrey。
- ⚠️ 重大不兼容变更：包改为仅 ESM，并要求 Node.js >=22。
- 🔄 模糊匹配规则改为最后参数和通配符贪婪，示例输出由 v8 的 `["foo.json","html"]` 变为 `["foo","json.html"]`。
- ⚡ 最后参数贪婪可改善正则表达式性能，并简化非正则匹配器实现。
- 🧹 避免重复尾部分隔符匹配：显式提供 `/foo/` 时不再追加额外可选分隔符（#443）。
- 🔧 匹配逻辑重构为非贪婪（#450），项目以 ESM 构建（#458），移除 `TokenData` 类和 `Keys` 类型（#461）。
- 🛠️ 修复 compile：拒绝空字符串参数（#444），拒绝编译为空路径的通配符数组（#448）。
- 🐛 修复 stringify：处理参数名中的控制字符（#445），引用后跟 astral `ID_Continue` 文本的参数名（#451），修复跨空文本 token 的 lookahead（#456）。
- 📜 完整变更日志为 `v8.4.2...v9.0.0`，贡献者包括 chatman-media、blakeembrey 等 6 人。

---

### [](https://github.com/directus/directus)

**原文标题**: [GitHub - directus/directus: The flexible backend for all your projects 🐰 Turn your DB into a headless CMS, admin panels, or apps with a custom UI, instant APIs, auth & more. · GitHub](https://github.com/directus/directus)

Directus 是一个可连接任意 SQL 数据库的灵活后端，可快速生成 REST/GraphQL API、可视化 Studio，并集成 AI 助手与原生 MCP 服务器，面向开发者、非技术团队和 AI 代理协作使用。

- 🐰 核心定位：把现有数据库变成 headless CMS、管理面板或应用后端，减少票据流程和样板代码。
- ⚡ 即时 API：根据数据库 schema 自动生成 REST 和 GraphQL API，基本无需配置。
- 🖥️ 可视化 Studio：为非技术成员提供完整管理界面，可直接操作实时数据。
- 🤖 AI 与 MCP：内置 AI Assistant，支持内容创建、翻译和工作流触发；原生 MCP Server 可连接 Claude、Cursor、ChatGPT 等兼容工具。
- 🔐 权限治理：基于策略的字段级访问控制，人类用户和 AI 代理遵循相同角色权限。
- 🗄️ 数据库支持：Postgres、MySQL、MariaDB、MS SQL、SQLite、OracleDB、CockroachDB 等。
- 🧩 可扩展与部署：支持自定义端点、hooks、界面和模块；可自托管、上云或使用 Directus Cloud。
- ☁️ 快速上线：Directus Cloud 可在约 90 秒内创建托管项目；Railway 一键部署包含 PostgreSQL、Redis 和 S3 兼容存储。
- 📊 项目与仓库数据：38.7k stars、5.0k forks、340 watchers、13,986 commits；已有 45M+ 下载和 500K+ 项目部署。
- 📄 许可证：采用 MSCL 1.0 源码可用许可；年收入低于 500 万美元且员工少于 50 人的组织可通过 Open Innovation Grant 免费使用，另有免费 Core Tier 和商业许可。
- 💬 社区支持：提供文档、论坛、Discord、GitHub Issues、路线图和 YouTube 教程；贡献前需阅读贡献指南，安全漏洞按安全政策报告。

---

### [](https://github.com/Hexagon/croner)

**原文标题**: [GitHub - Hexagon/croner: Trigger functions or evaluate cron expressions in JavaScript or TypeScript. No dependencies. Most features. Node. Deno. Bun. Browser. · GitHub](https://github.com/Hexagon/croner)

Croner 是一个面向 JavaScript/TypeScript 的零依赖 cron 调度库，可在 Node.js、Deno、Bun 和浏览器中触发函数、评估 cron 表达式并预测运行时间，主打功能完整、体积小和跨平台。
- 📦 零依赖，支持 Node.js >=18（require/import）、Deno >=2、Bun >=1 及浏览器（standalone、UMD、ESM）。
- ⏱️ 支持 5/6/7 段 cron 表达式，可选秒和年份字段，可计算下一次或未来多次运行时间。
- 🧮 支持高级语法：`L`（最后一天/最后一个星期几）、`W`（最近工作日）、`#`（第 n 个星期几）、`+`（AND 逻辑）、`?`（通配别名）。
- 🌍 支持时区与 `utcOffset`，也可用 Date 或 ISO 8601 字符串设置一次性触发时间。
- 🛡️ 内置防重入保护、错误捕获、TypeScript 类型声明和异步函数支持。
- ⏯️ 任务可暂停、恢复、停止、立即触发；完全内存运行，无需数据库或配置文件。
- 🔎 提供 `nextRun()`、`nextRuns()`、`previousRuns()`、`msToNext()`、`match()`、`isRunning()` 等状态与预测 API。
- ⚙️ 常用选项包括 `maxRuns`、`timezone`、`startAt`、`stopAt`、`interval`、`paused`、`context`、`domAndDow`、`unref`、`protect`、`allowPast`、`dayOffset`、`mode` 等。
- 📅 支持 `@yearly`、`@monthly`、`@weekly`、`@daily`、`@hourly` 等预设；`@reboot` 会被识别但会报错。
- 🕰️ DST 处理遵循 Vixie cron：固定时间任务在重复时段只跑第一次，间隔任务在重复时段会跑两次。
- 📊 项目约 2.6k stars、76 forks、839 commits；官方对比显示其零依赖、体积小、覆盖率高、性能较好。
- 🪪 采用 MIT 许可证，由 Hexagon 维护，提供 master 稳定版与 dev 开发版，完整文档位于 croner.56k.guru。

---

