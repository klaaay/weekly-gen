### [](https://nodejs.org/en/blog/release/v26.7.0)

**原文标题**: [Node.js — Node.js 26.7.0 (Current)](https://nodejs.org/en/blog/release/v26.7.0)

Node.js 26.7.0（Current 版本）于 2026 年 8 月 5 日正式发布，本次更新聚焦于加密模块增强、性能追踪支持、模块系统改进和测试工具拓展，并同步升级了多个核心依赖，同时修复了大量跨模块的稳定性与安全性问题。

- 🔐 crypto：支持通过 STORE 加载私钥，并更新根证书至 NSS 3.125
- 📊 lib/src：新增 perfetto 支持，提供性能追踪与 trace agent
- ♻️ module：在 ModuleHooks 中实现 Symbol.dispose 以优化资源管理
- 🧪 test_runner：新增 --test-coverage-include-all 选项，扩展覆盖率统计范围
- 📦 依赖升级：npm 升至 11.19.0，ngtcp2、nghttp3、simdjson、sqlite、zlib 等均有更新
- 🛠️ 构建与工具：perfetto 集成至 GHA、调整 rustc 要求并修复跨平台编译问题
- 🐛 修复多个关键问题：涵盖 http、http2、stream、sqlite、ffi、quic 等模块的崩溃与错误处理
- 🗂️ 其他改进：优化 stream 性能、增强 permission 审计模式、完善类型定义与文档
- 📥 提供多平台安装包与二进制文件：覆盖 Windows、macOS、Linux、AIX 及 ARM 架构

---

### [](https://nodejs.org/en/blog/release/v26.6.0)

**原文标题**: [Node.js — Node.js 26.6.0 (Current)](https://nodejs.org/en/blog/release/v26.6.0)

Node.js 26.6.0（Current）版本发布，主要包含新功能、依赖更新、文档改进及大量 bug 修复，并提供了各平台安装包与校验和。

- 🔧 新增 `ffi.getCurrentEventLoop()` 方法，用于获取当前事件循环信息。
- 🧪 测试运行器新增 `context.log()` 及 `test:log` 事件，并在 TestStream 事件中报告 `entryFile`。
- 📄 将 MikeMcC399 添加为 collaborator。
- 🔒 多项 crypto 修复：处理不完整 RSA 私钥、保留 RSA-PSS 旧版公钥 DER、清理 provider 私钥副本、限制 KangarooTwelveParams 自定义长度为 512 字节等。
- 📦 依赖升级：npm 升至 11.18.0，更新 libffi、c-ares、zlib、ngtcp2、V8 补丁、timezone、googletest 等。
- 🚀 流（stream）性能优化：使用环形缓冲区、改进背压处理、加速异步迭代、修复 share() 的 drop-newest 行为等。
- 🖧 网络：支持 BoundSocket 同步连接，TCP Server/Socket 可在 worker 线程间转移。
- 💾 fs 改进：添加 matchGlobPattern() 模式缓存，修复 Windows 上 cp 的符号链接与 EEXIST 处理。
- ⚡ events 优化：避免保留已移除的事件名，优化 once() 和 removeListener()。
- 📜 文档大量完善：修正 TLS、DNS、vm 等说明，更新发布指南和协作指南。
- 🛠 工具与构建：新增 Nix 对比工作流、benchmark 评论选项，禁用 GHA 上的 tarball 压缩。
- 🧩 其他修复：vfs 递归操作改进、sqlite 读取列计数、timers 不保留异步存储引用、zlib 拒绝截断的 zstd 输入。

---

### [](https://github.com/nodejs/node/pull/64830)

**原文标题**: [test_runner: add support for --test-coverage-include-all by avivkeller · Pull Request #64830 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/64830)

该 PR 为 Node.js 测试运行器新增了 `--test-coverage-include-all` 选项，可将未被测试加载的源文件纳入覆盖率报告并标记为零覆盖。该功能修复了相应 issue，并已合并至 Node.js 26.7.0 版本。

- 🆕 新增 CLI 选项 `--test-coverage-include-all`，支持在覆盖率报告中包含从未被测试加载的源文件（零覆盖）。
- 🔍 候选文件从当前工作目录中自动搜索，并遵循现有的 `--test-coverage-include` / `--test-coverage-exclude` 过滤规则。
- 🎯 旨在解决 issue #58887：项目中的未测试文件无法在覆盖率报告中显示 0% 覆盖的问题。
- 👥 由 avivkeller 提交，并获得 MoLow 和 atlowChemi 两位维护者的批准。
- ⚠️ Codecov 报告显示补丁覆盖率较低（23.21%），但项目整体覆盖率保持 90.12%。
- 🚀 该功能被标记为 semver-minor，最终随 Node.js v26.7.0（Current）版本正式发布。

---

### [Etsy 的工程师如何在流量激增时保持应用不崩溃 | Sentry](https://sentry.io/resources/etsy-workshop/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=ecommerce-fy27q3-etsyworkshop&utm_content=newsletter-primary-register)

**原文标题**: [How Etsy's Engineers Keep Their App Crash-Free During Traffic Spikes | Sentry](https://sentry.io/resources/etsy-workshop/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=ecommerce-fy27q3-etsyworkshop&utm_content=newsletter-primary-register)

overview summary  
Etsy 工程团队在高流量期间如何确保应用无崩溃的实战经验分享，强调崩溃对营收的直接影响，并介绍应对峰值流量的准备、实时调试与业务影响衡量方法，同时附上相关监控与调试资源。

- 📈 假期购物季的崩溃不仅是技术问题，更是直接的收入损失问题  
- 🛠️ Etsy 工程师 Jay Henry 与 Sentry 的 Sergiy Dybskiy 联合分享高峰流量应对经验  
- ⚡ 团队如何提前准备峰值流量、进行实时调试并衡量崩溃的业务影响  
- 🎯 包含 Etsy 高流量事件的真实案例与实用技巧  
- 📋 提供电商关键体验监控开发者清单，助力系统性排查  
- 🔍 通过 Session Replay 调试电商性能问题，定位用户实际体验瓶颈  
- 📊 学习如何监控并修复关键用户流程，保障核心转化路径稳定

---

### [](https://research.jfrog.com/post/shai-hulud-is-back-august/)

**原文标题**: [Major Shai Hulud campaign strikes npm again, affecting keyv and 400+ packages - JFrog Security Research](https://research.jfrog.com/post/shai-hulud-is-back-august/)

JFrog 安全团队发现新一轮 Shai-Hulud 供应链攻击，通过 keyv、cacheable 等 npm 包感染 400+ 包、1700+ 版本。该恶意软件集凭据窃取、npm 蠕虫传播、GitHub 仓库感染于一体，利用 npm preinstall 钩子和开发者工具执行链（VS Code、Claude）扩散。文章详细分析了其技术原理、C2 机制、受影响的包列表、入侵指标（IOC）以及应急响应建议，强调一旦受影响必须彻底轮换凭据并重建环境。

- 🔍 攻击概述：Shai-Hulud 恶意软件再度袭击 npm，波及 400+ 包、1700+ 版本，起点是 keyv 和 cacheable 等广泛使用的缓存库。
- 🧬 恶意载荷：710KB JavaScript 混淆样本（SHA-256 已公开），核心目标包括窃取本地/CI/云/K8s/Vault 密钥、加密外传、用 npm 凭据发布恶意包、用 GitHub 凭据感染更多仓库。
- 📦 感染路径：恶意包通过 preinstall 钩子运行 setup.mjs，使用 Bun 执行真实 payload；npm 12+ 默认禁用 preinstall 可降低安装时风险。
- 🔐 npm 蠕虫逻辑：验证 npm token（需 bypass_2fa 且具写权限），自动下载最新包、植入恶意代码、递增补丁版本并发布至所有可写包，实现自传播。
- 🖥️ GitHub 仓库钩子：向分支提交 .vscode/tasks.json、.claude/settings.json 等 5 个文件，开发者打开 VS Code 或启动 Claude 会话即可触发执行。
- 🤖 GitHub Actions 窃密：盗取带 workflow 权限的 token 后，注入恶意 workflow，通过 `${{ toJSON(secrets) }}` 将全部 secrets 写入 artifact 并下载外传，随后删除运行痕迹。
- 📁 凭据收集范围：扫描数百个路径，涵盖 npm/Yarn/PyPI 令牌、AWS/Azure/GCP 等云配置、K8s/Vault、.env、SSH 密钥、浏览器凭据、AI 工具凭据等，还能读取 GitHub Actions runner 进程内存。
- 🌐 C2 机制：动态通过以太坊合约（0xE1f2395ee43e45A1556EC6438a88c31B83493103）解析 C2 域名，备用方案利用 GitHub 提交消息中特定标记（如 thebeautifulmarchoftime）验证后获取地址，并支持远程代码执行。
- 🎯 定向攻击：针对 @opensearch-project/opensearch 仓库，滥用 GitHub Actions OIDC trusted publishing 流程，生成带有合法 Sigstore 来源的恶意包。
- 🛡️ 规避与对抗：字符串自研替换密码、AES-256-GCM 加密载荷，使用 PID 锁、空信号处理器、退出码伪装，并包含假“俄语检测”字符串（实际不生效）。
- ⚠️ 应急响应：一旦安装受影响版本，应隔离系统并保留证据、撤销并轮换所有 npm/GitHub/云/数据库等凭据、审计所有分支和 Actions 运行记录、移除恶意包并重建 CI 和开发环境。
- 🕵️ 入侵指标（IOC）：关键文件包括 setup.mjs、math_init.js、.claude/、.vscode/ 中的钩子文件；GitHub 提交特征为“chore: update config”和分支“dependabot/github_actions/format/setup-formatter”；C2 路径 /router。
- 📋 受影响包列表持续更新：已涉及 @keyv/*、@cacheable/*、@qlik/*、@onnereach/*、@ornikar/*、@servicetitan/*、@or-sdk/* 等多个系列，部分 Go 模块也被标记为恶意。

---

### [](https://github.com/jaredwray/keyv)

**原文标题**: [GitHub - jaredwray/keyv: Simple key-value storage with support for multiple backends · GitHub](https://github.com/jaredwray/keyv)

Keyv 是一个支持多后端存储的简单键值存储库，通过存储适配器提供统一接口，支持 TTL 过期，适合作为缓存或持久化存储。项目采用 monorepo 结构，涵盖核心库、存储/压缩/序列化适配器及文档网站，同时欢迎社区贡献；目前 v6 正在开发中，v5 仅保留维护与安全更新。

- 🔑 核心功能：简单键值存储，支持多种后端，默认内存存储，可扩展持久化适配器
- 📦 快速开始：使用`npm install keyv`安装，提供`set`、`get`等简洁 API
- 🗂️ 项目结构：monorepo 分为 core、serialization、compression、storage、website 等目录
- 🧩 核心包：包含 keyv 主库、API 合规测试套件 test-suite、可扩展内存 Map（bigmap）
- 💾 存储适配器：支持 Redis、Postgres、MySQL、Mongo、SQLite、Memcache、Etcd、Valkey、Dynamo、Cloudflare KV 等
- 🗜️ 压缩适配器：提供 Brotli、Gzip、LZ4 压缩方案
- 🔄 序列化：默认内置 JSON 序列化，可选 SuperJSON（支持 Date/Map/Set/BigInt）和 MessagePack 高性能序列化器
- 🌍 第三方适配器：支持社区构建更多存储后端，完整列表见 keyv.org
- 🤝 贡献方式：Fork 仓库并提交 PR、开 issue 报告问题或请求功能，需遵守行为准则
- 🛡️ 安全与规范：设有安全政策，存储适配器请求需在 30-60 天内获得社区关注
- 🚀 版本状态：v6 开发中，将改进 TypeScript 支持、hooks 系统和适配器接口；v5 仅做维护与安全修复
- 📄 开源许可：基于 MIT License

---

### [](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

**原文标题**: [Upcoming breaking changes for npm v12 - GitHub Changelog](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

npm v12 預計於 2026 年 7 月發布，針對 `npm install` 導入多項安全相關的預設變更，將原本自動執行的行為改為需明確允許；目前可在 npm 11.16.0 以上版本查看警告並提前準備。

- 🔒 npm v12 預設關閉 `allowScripts`：不再自動執行依賴的 `preinstall`、`install`、`postinstall` 指令碼（包含 node-gyp 建置），除非專案明確允許。
- 🚫 來自 git、file 與 link 依賴的 `prepare` 指令碼也同樣被封鎖；可用 `npm approve-scripts --allow-scripts-pending` 查看，再用 `npm approve-scripts` / `npm deny-scripts` 管理白名單，並提交更新後的 `package.json`。
- ⛔ `--allow-git` 預設為 `none`：不再自動解析 Git 依賴（直接或間接），以避免依賴的 `.npmrc` 覆寫 Git 執行程式所造成的程式碼執行風險。
- 📦 `--allow-remote` 預設為 `none`：不再自動解析遠端 URL（如 HTTPS tarball）依賴；`--allow-file` 與 `--allow-directory` 的預設值則維持不變。
- ✅ 建議先升級至 npm 11.16.0 以上，執行例行安裝並檢查警告，核准信任的套件；升級後未核准的指令碼將停止執行，以確保供應鏈安全。

---

### [快速](https://pnpm.io/)

**原文标题**: [Fast, disk space efficient package manager | pnpm](https://pnpm.io/)

pnpm 是一个注重速度与磁盘空间优化的 JavaScript 包管理器，特别适合 monorepo 工作流，获得了众多开发者与知名开源项目的认可。

- ⚡ 安装速度极快：pnpm 专为提升依赖安装效率而设计，大幅减少等待时间。
- 💾 节省磁盘空间：通过内容可寻址存储与硬链接，避免重复下载，多个项目共享依赖。
- 🏗️ 强大的工作区支持：原生支持 monorepo，可并行管理多个子包，简化 CI 构建流程。
- 🧰 运行时管理：提供便捷的 Node.js 版本与运行时管理能力。
- 🛡️ 安全与体验俱佳：可禁用 postinstall 脚本、支持 minimumReleaseAge 延迟更新，降低供应链攻击风险，并简化依赖覆盖操作。
- 🚀 性能提升案例：有用户将 CI 构建从 12 分钟缩短至 2 分钟，另有团队观察到部分流程耗时降低 40%。
- 💖 获广泛赞助：包括 Bit Cloud、OpenAI、Sanity、Discord、Vite、StackBlitz、Nx、Replit 等多家公司支持。
- 📦 被众多知名项目采用：next.js、n8n、Material UI、Vite、Nuxt、Vue、Astro、Prisma、SvelteKit、Vercel 等均在使用 pnpm。

---

### [](https://www.vlt.io/blog/1-0)

**原文标题**: [vlt 1.0 & Hosted Package Registries | vlt /vōlt/](https://www.vlt.io/blog/1-0)

vlt 1.0 稳定版正式发布，同时托管 JavaScript 注册表及生态镜像全面上线（GA），标志着 vlt 从包管理器发展为覆盖开发全流程的端到端平台。客户端可作为 npm 的即插即用替代品，具备安全优先的查询选择器、分阶段安装、目录管理等特性；托管服务则提供兼容 API、免费层、边缘性能优化、隐私保护和主动恶意软件拦截。

- 🎉 vlt 1.0 与托管 JavaScript 注册表/生态镜像正式发布，形成端到端开发平台。
- 🔍 客户端拥有 60+ 图原生伪选择器（约 30 个专注安全），如 :malware、:cve、:unmaintained、:eval 等，并支持 :host(local) 跨本机项目查询依赖。
- 🏷️ --scope 标志让选择器适用于所有命令；Graph Modifiers 可覆盖依赖；分阶段安装（install 不执行脚本，build 选择性运行）默认阻止恶意软件；Catalogs 集中管理版本。
- 🔑 支持 OIDC 可信发布，CI 中无需长期令牌即可发布到 npm 公共注册表，GitHub Actions 开箱即用。
- 🔄 vlt 客户端是 npm 的即插即用替代品，可运行 init、install、build、publish 等完整软件生命周期。
- 🌐 托管注册表与 npm API 向后兼容，npm/pnpm/yarn/bun/deno 均可安装和发布；提供慷慨的免费层。
- ⚡ 包从靠近开发者和 CI 的边缘基础设施分发，基准测试显示干净安装比 npm 快 38%。
- 🔒 支持无限私有包，发布时强制作用域并验证清单；主动摄取 OSV 等恶意软件源，已标记超 27.5 万包版本（超 25% 在 npm 公共注册表仍可下载）。

---

### [2026 年 7 月安全发布 · Express.js](https://expressjs.com/en/blog/2026-07-31-security-releases/)

**原文标题**: [July 2026 Security Releases · Express.js](https://expressjs.com/en/blog/2026-07-31-security-releases/)

概述：Express 团队发布了 body-parser 的安全更新，修复了一个因无效 limit 值导致的拒绝服务漏洞，建议用户升级到最新版本。

- 🔒 发布 body-parser 1.20.6 和 2.3.0，修复拒绝服务漏洞（CVE-2026-12590，低危）。
- ⚠️ 受影响版本：< 1.20.6 以及 >= 2.0.0 且 < 2.3.0。
- 🛑 漏洞成因：无效 limit 值（如不可解析字符串或 NaN）导致 bytes.parse() 返回 null，请求体大小检查被静默跳过。
- 📈 风险影响：依赖 limit 限制请求体大小的应用会接受超大载荷，导致内存和 CPU 过度消耗，引发拒绝服务。
- ✅ 修复方式：无效 limit 值现在会在解析器创建时抛出明确错误，而非静默禁用限制。
- 📦 升级建议：运行 `npm update body-parser` 更新依赖，确保应用安全。

---

### [网络 | Node.js v26.7.0 文档](https://nodejs.org/api/net.html#class-netblocklist)

**原文标题**: [Net | Node.js v26.7.0 Documentation](https://nodejs.org/api/net.html#class-netblocklist)

Node.js v26.7.0 文档中的 `node:net` 模块提供了基于流（stream）的异步网络 API，用于创建 TCP 服务器和客户端，以及支持 IPC（Windows 命名管道和 Unix 域套接字）。该模块包含 `BlockList` 用于 IP 地址封禁、`SocketAddress` 表示地址、`Server` 与 `Socket` 管理连接，并新增了同步预绑定套接字的 `BoundSocket`。文档还涵盖了常用的 `createServer`、`createConnection`、`connect` 等工厂函数，以及地址过滤、自动选择 IPv4/IPv6 家族、TCP 句柄跨线程转移等功能。

- 📡 `node:net` 模块是异步网络库，用于创建基于流的 TCP 或 IPC 服务器（`net.createServer()`）和客户端（`net.createConnection()`）。
- 🔌 支持 IPC：Windows 上使用命名管道，其他系统使用 Unix 域套接字；Unix 路径受 `sockaddr_un.sun_path` 长度限制（Linux 约 107 字节，macOS 约 103 字节），且管道/套接字在关闭或进程退出后自动消失。
- 🚫 `net.BlockList` 类用于禁用对特定 IP、IP 范围或子网的访问，支持 `addAddress`、`addRange`、`addSubnet`、`check` 和 `rules` 属性，并可通过 `fromJSON`/`toJSON` 导入导出。
- 📍 `net.SocketAddress` 类表示 IP 地址和端口，支持构造、属性读取（`address`、`family`、`port` 等）以及静态 `SocketAddress.parse()` 解析字符串。
- 🖥️ `net.Server` 类创建 TCP/IPC 服务器，具有 `close`、`connection`、`error`、`listening`、`drop` 等事件，以及 `listen()` 的多种重载、`address()`、`getConnections()` 等方法。
- 🔗 `net.Socket` 类是 TCP 或 IPC 端点的抽象，包含 `connect`、`data`、`end`、`error`、`timeout` 等事件，以及 `write()`、`end()`、`destroy()`、`setKeepAlive()`、`setNoDelay()` 等常用方法。
- 🧵 支持将已连接的 TCP `net.Socket` 或正在监听的 `net.Server` 通过 `worker_threads` 的 `transferList` 转移到其他线程，实现跨线程连接分发。
- 🆕 `net.BoundSocket`（v26.4.0 新增）可同步创建预绑定套接字，支持 TCP 端点或 Unix/命名管道路径绑定，可传给 `server.listen()` 或 `new net.Socket()` 实现所有权转移。
- ⚙️ `net.createServer()` 可配置 `allowHalfOpen`、`highWaterMark`、`keepAlive`、`noDelay`、`pauseOnConnect`、`blockList` 等选项。
- 🏭 `net.createConnection()` 和 `net.connect()` 用于快速建立连接，支持传入 `port`/`host` 或 `path`，并可通过 `onread` 选项使用固定缓冲区高效读取数据。
- 🌐 IPv4/IPv6 自动选择（`autoSelectFamily`）功能可依次尝试多个地址，默认开启（初始超时 500ms），可通过 `net.setDefaultAutoSelectFamily()` 和 `net.setDefaultAutoSelectFamilyAttemptTimeout()` 调整。
- 🔍 `net.isIP()`、`net.isIPv4()`、`net.isIPv6()` 用于检测 IP 地址格式，严格匹配点分十进制且不允许前导零。

---

### [](https://github.com/nodejs/node/pull/64974)

**原文标题**: [net: make multiple improvements to net.BlockList by jasnell · Pull Request #64974 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/64974)

overview summary  
该 Pull Request 针对 Node.js 的 net.BlockList 进行多项改进：新增了丰富的管理 API，并通过基数树、常量时间查找和 V8 快速 API 等优化，使查找性能从 O(n) 大幅提升至接近 O(1)；同时补充了基准测试与更多测试，最终通过评审并合并到主分支。

- 🆕 新增 API：addCIDR、addCIDRs、addAddresses、removeAddress、removeRange、removeSubnet、removeCIDR、clear()，以及 size 属性和 BlockList.PRIVATE_RANGES 预设。
- ⚡ 性能优化：采用常数时间地址查找、基数树子网查找、V8 快速 API、批量插入和读写锁等机制。
- 📈 性能提升：地址规则性能提升约 9x–1186x，子网规则提升约 5x–418x，规则越多效果越显著。
- 🧪 测试与覆盖率：新增基准测试和测试用例，补丁覆盖率约 90%，项目覆盖率为 90.30%。
- 🛠️ 代码修复：修复了重复地址插入、规则列出顺序、边界检查等问题，并简化了内部实现。
- ✅ 评审合并：获得多位维护者批准，CI 通过，最终合入 Node.js 主分支（提交 27d6cfa）。

---

### [](https://github.com/nodejs/node/pull/64894)

**原文标题**: [worker: add support for Web Workers by avivkeller · Pull Request #64894 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/64894)

该 PR 为 Node.js 添加 Web Worker API 支持，依据 HTML 标准实现，并针对 Node.js 运行环境列出多项差异与适配。实现附带大量 WPT 测试，经过评审与多轮修改，目前已获得部分批准，仍在等待其他维护者审核。

- 🔧 为 Node.js 添加 Web Worker API 支持，修复 issue #43583，核心实现位于`lib/internal/webworker.js`
- 🚫 未实现`SharedWorker`，因其依赖 origin 与 browsing context 等 Node.js 不存在的概念
- 📂 Worker 脚本仅从本地文件系统同步加载，只接受`file:`、`data:`、`blob:` URL；其他 scheme 抛`NotSupportedError`，不可读脚本抛`NetworkError`；仅对`data:`与`blob:`执行 MIME 类型校验
- 🌐 Node.js 无 origin 模型，`location.origin`为`null`；主线程相对 URL 基于当前工作目录解析，worker 内则基于自身 URL
- ⏹ `close()`会立即终止 worker，不执行后续代码，与规范的“closing flag”算法不同
- 🔗 worker 全局对象基于 Node.js 全局对象，将`DedicatedWorkerGlobalScope`插入原型链；`file:` worker 通过 CommonJS/ESM loader 执行，顶层声明不成为全局属性，而`data:`/`blob:` worker 仍按 classic script 运行
- 📡 不触发`languagechange`、`online`、`offline`、`rejectionhandled`、`unhandledrejection`等事件；`ErrorEvent`缺少`filename`、`lineno`、`colno`字段
- 🧪 包含大量 WPT（Web Platform Tests），造成 1300+ 文件、54k+ 行变更；作者使用 AI 辅助解决 WPT 测试中的问题
- 📝 评审中建议拆分 WPT 测试，最终整理为 5 个提交，并加入多全局 WPT runner 与相关优化
- ✅ 已获 panva 批准，CI 整体通过，但存在 macOS flaky 测试待观察；等待 jasnell、mcollina 等进一步审查

---

### [](https://github.com/nodejs/node/commit/5ba72ae7bc42fb3f884c860e7a4f7800794984f8)

**原文标题**: [zlib: add ZipEntry, ZipFile, and ZipBuffer · nodejs/node@5ba72ae · GitHub](https://github.com/nodejs/node/commit/5ba72ae7bc42fb3f884c860e7a4f7800794984f8)

此提交为 Node.js 的 `node:zlib` 模块新增了完整的 ZIP 归档支持，引入了三个核心类及配套辅助函数，并同步更新了文档、错误码与大量测试。

- 📦 新增 `ZipEntry` 类，支持单个归档成员的缓冲读取（`content()`）、有界内存流式读取（`contentIterator()`）以及通过 `create()`/`createStream()` 构建成员。
- 🗂️ 新增 `ZipFile` 类，提供基于文件描述符的随机访问，可惰性读取成员且不保留其内容，并支持原地写入新成员，通过 `open()`/`openSync()` 打开。
- 💾 新增 `ZipBuffer` 类，提供对已存在于 `Buffer` 中的归档的零拷贝、纯内存视图。
- 🛠️ 添加辅助函数 `createZipArchive()` 用于将条目序列化为归档字节流，`setMaxZipContentSize()` 用于限制默认内存解压大小。
- ⚠️ 新增 7 个相关错误码：`ERR_ZIP_ARCHIVE_TOO_LARGE`、`ERR_ZIP_ENTRY_CORRUPT`、`ERR_ZIP_ENTRY_NOT_FOUND`、`ERR_ZIP_ENTRY_TOO_LARGE`、`ERR_ZIP_INVALID_ARCHIVE`、`ERR_ZIP_NOT_WRITABLE`、`ERR_ZIP_UNSUPPORTED_FEATURE`。
- 📚 更新了 `doc/api/errors.md`、`zlib.md` 与 `type-map.json` 文档，补充了类与错误说明的链接引用。
- 🧪 新增了 17 个测试文件，覆盖覆盖度、边界情况、编码、模糊测试、加固、互操作性、元数据、安全性、同步操作、可写性、ZIP64 等场景。
- 🔢 本次变更共涉及 36 个文件，新增 9,679 行代码，由 pipobscure 提交，并经过 4 位维护者审核。

---

### [Mongoose 9.9 的新特性：重大性能](https://thecodebarbarian.com/mongoose-99-perf.html)

**原文标题**: [What's New in Mongoose 9.9: Major Performance Improvements | www.thecodebarbarian.com](https://thecodebarbarian.com/mongoose-99-perf.html)

overview summary
- 🚀 Mongoose 9.9.0 于 2026 年 7 月 30 日发布，主要聚焦性能提升，在不绕过任何核心功能的前提下减少多个热路径的开销。
- ⚡ `insertMany()` 性能提升 35%，通过改用空对象替代`Map`、采用快速路径`toObjectShallow()`、优化`versionKey`设置以及重写`parallelLimit()`（用计数器替代`Set`和`Promise.race()`）实现。
- 🔄 变更跟踪优化：引入`clearAllExcept()`方法，避免在`clear()`循环中使用`delete`导致的 JIT 去优化，使保存含 10 个属性的新文档时速度提升约 10%。
- 🗂️ `toObject()`和`toJSON()`效率提升：缓存带转换器（transforms）和 getter 的路径，避免每次扫描全部 schema，尤其在无变换或复杂投影时显著加快序列化。
- 🕒 时间戳更新优化：仅在设置`upsert: true`时才向`$setOnInsert`添加`createdAt`，普通更新不再生成无用字段。
- 📊 基准测试显示：`insertMany()`从 13.58ms 降至 8.75ms（驱动为 5.31ms），`save()`从 2.61ms 降至 2.35ms（驱动为 2ms）。
- 🧪 建议生产环境用户运行测试套件验证升级；当前基准较简单，嵌套文档、自定义验证器、中间件等场景会有不同表现。
- 📦 可通过`npm install mongoose@9.9`立即体验新版本。

---

### [](https://github.com/Automattic/mongoose)

**原文标题**: [GitHub - Automattic/mongoose: MongoDB object modeling designed to work in an asynchronous environment. · GitHub](https://github.com/Automattic/mongoose)

overview summary  
Mongoose 是一个专为异步环境设计的 MongoDB 对象建模工具，支持 Node.js 与 Deno（alpha），提供 Schema 定义、模型创建、中间件、嵌入式文档等丰富功能，并有详细的官方文档和社区插件生态。

- 📖 官方文档位于 mongoosejs.com，Mongoose 9.0.0 已于 2025 年 11 月 21 日发布，文档有 9.0.0 破坏性变更说明。
- 📦 可通过 npm、pnpm、yarn、bun 安装，Mongoose 6.8.0 起包含 Deno 的 alpha 支持。
- 🔌 支持 CommonJS `require`、ES6 `import`，以及 Deno 的 `createRequire` 方式导入。
- 🔗 使用 `mongoose.connect` 或 `mongoose.createConnection` 连接 MongoDB，二者均接受 `mongodb://` URI 或参数；连接前所有命令会被缓冲。
- 📐 通过 `Schema` 接口定义模型，支持校验器、默认值、getter、setter、索引、中间件、方法、静态方法、插件及伪 JOIN 等功能。
- 🧩 支持嵌入式文档（如 `comments: [Comment]`），可像普通模型一样使用默认值、校验和中间件。
- ⚙️ 中间件可拦截并修改方法参数，通过 `pre` 钩子实现，并支持链式声明。
- ⚠️ Schema 中 `type` 作为字段名时需使用对象嵌套写法，否则会被误解为类型声明。
- 🛠️ 可通过 `YourModel.collection` 访问底层 MongoDB 驱动集合，但会绕过 Mongoose 的钩子与校验等特性。
- 📚 API 文档由 dox 和 acquit 生成，另有 MongoDB 测试工具、CLI、数据填充、Express 会话存储等相关项目。
- 📜 使用 MIT 许可证，版权归 LearnBoost 所有。

---

### [调试卡住的 Node](https://engineering.myhoai.com/posts/debugging-stuck-node-js-processes/)

**原文标题**: [Debugging stuck Node.js processes | HOAi](https://engineering.myhoai.com/posts/debugging-stuck-node-js-processes/)

在生产环境出现间歇性健康检查失败，传统排查手段无效后，通过深入 Node.js 内部机制，最终用崩溃时 CPU 采样定位到隐藏极深的缺陷，并沉淀为可复用的排查工具。

- 🔍 问题现象：关键应用间歇性健康检查失败并自动重启，日志、指标和本地复现均无法解释根因。
- 💡 初步误判：工程师与 AI 代理推测是资源密集型活动，但多次性能优化后故障依旧。
- 🧵 事件循环线索：故障容器显示单核 CPU 100%、无网络流量、无日志输出，判定事件循环被长时间阻塞。
- 📊 追踪方案失效：基于 tracing 的阻塞检测器只发现少量低效函数，平均阻塞 <5 秒，不足以触发重启。
- 🚨 关键洞察：若代码片段永不交还事件循环，追踪器无法上报；需从外部强制采样。
- 🛠️ 新策略：利用 Node 内置调试器，在容器收到终止信号时对卡死进程生成 CPU profile。
- 📦 实现方式：entrypoint 脚本捕获 SIGTERM/SIGINT，调用基于 expect 的 profiler 脚本，采样 5 秒后上传 S3。
- 🐛 最终根因：对空字符串调用 `indexOf(str, N)` 导致事件循环死循环，修复后不再复发。
- ✅ 长期收益：该崩溃报告机制无性能损耗，已额外发现两个类似疑难 bug，每次仅需约一小时定位。
- 🌍 开源分享：已发布演示版工具，支持 Docker 和 curl 快速试用。

---

### [](https://firecrawl.github.io/anydoc/)

**原文标题**: [anydoc by Firecrawl](https://firecrawl.github.io/anydoc/)

overview summary  
anydoc 是一个开源的 Rust 库，可将 Word、PowerPoint、Excel、PDF 等格式转换为 GitHub 风格的 Markdown，并提供 Node、Python、浏览器及 CLI 绑定；它支持在浏览器中本地运行，文件不会离开设备。

- 📄 支持多种文档格式（Word、PPT、Excel、PDF、RTF、CSV 等）统一转换为 GitHub 风格 Markdown。
- 🧩 所有格式先解析为同一文档模型，再经相同序列化器输出，保证标题、嵌套列表、合并单元格、脚注等表现一致。
- 🔍 格式识别基于文件字节内容而非扩展名，因此误标扩展名的文件也能正确转换。
- ⚡ 纯 Rust 实现，无 ML 模型、无外部服务；中位转换时间低于 5 毫秒，在 100 份文档基准测试中唯一能处理全部 14 种格式。
- 📑 文本型 PDF 通过 pdf-inspector 本地转换；扫描件需 OCR，可由 Firecrawl Parse 叠加支持。
- 🌐 本页在线转换器是 anydoc 编译为 WebAssembly 的版本（@firecrawl/anydoc-wasm），可集成到自有应用中。
- 📦 安装方式覆盖多语言与场景：Rust `cargo add anydoc`、Node `npm install @firecrawl/anydoc`、Python `pip install firecrawl-anydoc`、浏览器 `npm install @firecrawl/anydoc-wasm`、CLI `npx @firecrawl/anydoc report.docx`、Agent skill `npx skills add firecrawl/anydoc`。
- 🔧 API 在所有环境中保持一致：支持从路径或字节转换，也可仅输出文档模型并保留嵌入资源；详见 README。

---

### [](https://github.com/firecrawl/anydoc)

**原文标题**: [GitHub - firecrawl/anydoc: Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean Markdown. Built in Rust, with Node.js and Python bindings. · GitHub](https://github.com/firecrawl/anydoc)

anydoc 是一个由 Firecrawl 开发的 Rust 库，能够将 Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV 和 PDF 等多种办公文档快速转换为干净的 GitHub 风格 Markdown，并提供 Node.js、Python、Rust 及浏览器（WebAssembly）绑定，同时支持作为 Agent Skill 使用，让 AI 代理直接读取文档。

- 📄 支持 14 种文档格式（Word、PPT、Excel、OpenDocument、RTF、EPUB、CSV、PDF），统一输出为 GitHub 风格 Markdown
- ⚡ 纯 Rust 实现，中位转换时间低于 5 毫秒，比最快的竞品快一个数量级
- 🔗 提供 Node.js、Python、Rust 和浏览器（WebAssembly）四种绑定，TypeScript 类型和 Python stubs 随包发布
- 🤖 以 Agent Skill 形式分发，执行 `npx skills add firecrawl/anydoc` 即可让 Claude Code、Codex 等代理读取文档
- 🖼️ 保留完整文档结构：标题锚点、表格、嵌套列表、脚注、区块引用等，图片以替代文本呈现并保留原始字节
- 🔍 基于文件内容而非扩展名进行格式检测，可正确处理错误标记的文件
- 📊 基准测试覆盖 14 种格式、100 个真实文档，anydoc 在所有格式上得分最高，且速度远超 LibreOffice、Pandoc 等工具
- 🧩 架构上所有格式先解析为共享文档模型，再通过统一序列化器输出，修复一个格式的问题会自动惠及其他格式
- 🛡️ 提供清晰的错误分类：Unsupported、Malformed、Encrypted、ResourceLimit、MissingPart、Io，便于管道处理异常文件
- 🖥️ 支持 CLI 使用，如 `npx @firecrawl/anydoc report.docx`，也可从 stdin 读取数据
- 📦 PDF 转换基于内置的 pdf-inspector，纯本地处理文本型 PDF，无需 OCR 服务；扫描页可选用 Firecrawl Parse 的 OCR 能力
- 🛠️ 开发测试完善：包含 fixture 快照测试、变异测试、模糊测试和性能基准测试
- 📜 项目采用 MIT 许可证，并已发布到 crates.io、npm 和 PyPI

---

### [适用于任意规模时间序列工作负载的 Postgres | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

overview summary  
Tiger Data 提供专为时序工作负载设计的托管 Postgres 服务，以极致规模、弹性架构和企业级安全为特色，并支持快速部署与深度可观测性。

- 📈 可处理每天 3 万亿指标、3 PB 数据及 1 千万亿数据点，支撑真实世界大规模时序场景。  
- 🎁 新账户赠 30 天有效期的 1000 美元额度，无需信用卡，受到数千家 IoT 公司信赖。  
- ⚙️ 通过最多 10 节点的副本集分离读写，并结合分层 SSD/S3 实现无上限的廉价存储。  
- 💸 计算与存储分离，可独立伸缩，避免空闲容量浪费，优化成本与性能。  
- 🛡️ 多可用区集群具备自动故障转移、时间点恢复与跨区域备份，保障高可用。  
- 🔐 符合 SOC 2、HIPAA、GDPR，具备全程加密、SSO、RBAC 与审计日志，企业级安全默认开启。  
- 📊 查询钻取与仪表盘提供深度可观测性，可向 CloudWatch、Datadog、Prometheus 发送指标。  
- ⚡ 数分钟内即可完成数据库部署，并支持通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。  
- 🔌 可与首选云提供商及更广泛的 Postgres 生态无缝集成。  
- 🤝 企业版提供合同化 uptime SLA、区域数据隔离、合规认证，以及 24/7 全球专家支持。

---

### [](https://github.com/redis/ioredis)

**原文标题**: [GitHub - redis/ioredis: 🚀 A robust, performance-focused, and full-featured Redis client for Node.js. · GitHub](https://github.com/redis/ioredis)

ioredis 是一个为 Node.js 打造的健壮、高性能且功能全面的 Redis 客户端，支持集群、哨兵、流、管道、Lua 脚本、发布/订阅等丰富特性，并完整提供 TypeScript 类型声明。它兼容 Redis 2.6.12 至最新版本，API 友好，支持回调与 Promise，但官方建议新项目优先考虑 node-redis。

- 🚀 高性能：支持自动管道（enableAutoPipelining），可避免 Head-of-Line 阻塞，吞吐量提升 35%~50%。
- 📦 全功能：覆盖 Cluster、Sentinel、Streams、Pipelining、Lua 脚本、Redis Functions、Pub/Sub、二进制数据、TLS、离线队列等。
- 💻 类型安全：100% 使用 TypeScript 编写，提供官方声明，支持 Node.js >= 20 与 Redis 6.2 以上版本。
- 🔧 简单易用：安装后即可 `new Redis()` 连接 localhost:6379，命令调用与 Redis 原生命令一一对应。
- 🔌 连接灵活：支持端口、主机、Unix socket、`redis://` 和 `rediss://` 连接字符串，可配置 db、username、password。
- 📡 Pub/Sub：支持 `subscribe`/`publish` 及模式订阅，注意同一连接不能同时充当订阅者和发布者。
- 🗄️ Streams：支持 `xadd`、`xread` 等流命令，方便构建流式架构与日志持久化。
- ⏱️ 过期控制：直接传参 `"EX" 60` 即可设置键过期，与 Redis 命令完全一致。
- 🔢 二进制数据：默认支持 Buffer，提供 `getBuffer`、`setBuffer` 等变体命令处理二进制内容。
- 🧩 管道与事务：`pipeline()` 批量发送命令，性能提升 50%~300%；`multi()` 实现事务，可配合管道使用。
- 📜 Lua 脚本：通过 `defineCommand` 自定义命令，自动优化 `EVAL`/`EVALSHA` 调用。
- 🏷️ 键前缀：`keyPrefix` 选项为所有键自动添加前缀，便于管理命名空间。
- 🔄 转换器：支持参数与回复转换，例如将 `hgetall` 结果转为对象。
- 📶 RESP3 协议：默认启用 RESP3，自动降级到 RESP2，可配置 `replyMapping` 控制回复格式。
- 📊 扫描与监控：支持流式 `scanStream`、`hscanStream` 等，以及 MONITOR 命令实时观察命令。
- 🔁 自动重连：可自定义 `retryStrategy` 实现指数退避重连，并自动重新订阅和重发未完成命令。
- ⏰ 阻塞超时：`blockingTimeout` 选项防止阻塞命令因 TCP 僵尸连接而无限等待。
- 📈 诊断通道：基于 Node.js `diagnostics_channel` 发布遥测数据，支持命令、批处理和连接追踪。
- 🔐 TLS 支持：支持 `rediss://` URL、自定义 TLS 选项及预配置 TLS 配置文件。
- 🧭 Sentinel 模式：开箱即用，故障转移时自动切换到新主节点，支持 `preferredSlaves` 选择从节点。
- 🗺️ Cluster 模式：支持分片、读写分离、NAT 映射、事务管道、Pub/Sub 及分片 Pub/Sub。
- ⚡ 自动管道：事件循环内命令自动合并成管道，极大提升网络利用率。
- ❗ 错误处理：提供 `ReplyError` 类型与 `showFriendlyErrorStack` 选项，便于定位代码错误。
- 🧪 测试与调试：支持 `DEBUG=ioredis:*` 日志，并提供 `ioredis-mock` 用于测试环境。

---

### [Redis 序列化协议规范 | 文档](https://redis.io/docs/latest/develop/reference/protocol-spec/)

**原文标题**: [Redis serialization protocol specification | Docs](https://redis.io/docs/latest/develop/reference/protocol-spec/)

Redis 序列化協議（RESP）是用於 Redis 客戶端與伺服器之間通訊的線協議，設計上追求簡單、快速解析且人類可讀。它支援多種資料類型，包括整數、字串、陣列及錯誤類型，並具備二進位安全特性。協議有 RESP2 與 RESP3 版本，RESP3 為超集，透過 HELLO 指令進行版本協商。用戶端以字串陣列形式傳送指令，伺服器回傳對應的 RESP 類型，並支援流水線、發布/訂閱等例外模式。

- 📡 RESP 是 Redis 客戶端與伺服器之間的通訊協議，也適用於其他客戶端 - 伺服器專案，特點是簡單、快速、可讀。
- 🔄 RESP 有 RESP2 與 RESP3 版本；RESP3 是超集，Redis 6.0 起可選用，透過 HELLO 指令協商版本。
- 🌐 網路層使用 TCP 連接（預設連接埠 6379），並採用請求 - 響應模型，但支援流水線、Pub/Sub、MONITOR、RESP3 Push 等例外。
- 📦 客戶端發送指令時，以由批量字串組成的陣列表示；伺服器回覆的類型由指令決定。
- ➕ 簡單字串以「+」開頭，例如 +OK\r\n，適合短的非二進位字串。
- ❌ 簡單錯誤以「-」開頭，例如 -ERR unknown command 'asdf'，客戶端應將其視為例外。
- 🔢 整數以「:」開頭，例如 :1000\r\n，表示有號 64 位元整數。
- 💾 批量字串以「$」開頭，包含長度與資料，例如 $5\r\nhello\r\n，最大預設 512MB。
- 🚫 空批量字串以 $-1\r\n 表示，空陣列以 *-1\r\n 表示；RESP3 新增專用 null 類型「_」。
- 📋 陣列以「*」開頭，可巢狀、混合型別，例如 *2\r\n$5\r\nhello\r\n$5\r\nworld\r\n。
- ✅ 布林值（RESP3）以「#t」或「#f」表示；雙精度浮點數以「,」開頭；大數字以「(」開頭。
- 📝 批量錯誤（RESP3）以「!」開頭；逐字字串以「=」開頭，包含編碼提示（如 txt）。
- 🗺️ 地圖（RESP3）以「%」表示鍵值對；屬性以「|」表示附屬資料；集合以「~」表示；推送以「>」表示。
- 🤝 新連接建議先呼叫 HELLO 指令，可傳回伺服器資訊、協議版本，並支援 AUTH 認證。
- ⚡ 支援流水線：客戶端可一次發送多個指令，之後統一讀取回應；也支援 telnet 的 inline 指令格式。
- 🚀 RESP 使用前置長度傳輸資料，解析時無需掃描特殊字元，效能接近二進位協議。
- 💡 客戶端作者可參考 Lua 型別轉換技巧，測試時讓 Redis 回傳所需的 RESP2/RESP3 型別。

---

### [Redis 开源版 8.10 发布说明 |](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.10-release-notes/)

**原文标题**: [Redis Open Source 8.10 release notes | Docs](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.10-release-notes/)

Redis 8.10 是 Redis 开源版的重要版本更新，引入多项新功能、性能优化与命令增强，同时修复大量内核、模块及集群相关问题，并扩展了多平台支持。

- 🗜️ 新增「紧凑哈希（Compact hashes）」编码，将共享 schema 的字段名仅存一次，大幅降低内存占用
- ⚡ 新命令 `HIMPORT` 支持高吞吐紧凑哈希批量插入，提升数据导入效率
- 🔄 新增 `LMOVEM`、`BLMOVEM` 命令，可在列表间一次移动多个元素
- 📊 新增 `SUNIONCARD` 与 `SDIFFCARD` 命令，分别返回集合并集与差集的基数
- 💾 新增 `BACKUP` 命令，基于多部分 AOF（MP-AOF）实现节点侧备份与恢复
- 🔍 `XREAD`、`XREADGROUP` 新增 `MAXCOUNT` 与 `MAXSIZE` 参数，限制累计回复条目与大小
- 🏷️ 新增 `FT.ALIASLIST` 命令，获取索引的所有别名；同时为马来语和塔加拉语添加词干分析支持
- 📐 JSONPath 扩展大量语法：支持投影表达式、过滤取反、数值运算、字符串函数、数组聚合及关系函数等
- ⏱️ 时间序列模块新增 `TS.NRANGE`、`TS.NREVRANGE`、`TS.READ`、`TS.QUERYLABELS` 等命令，并支持 `EXCLUDEEMPTY` 参数
- 🔒 引入基于 TLS 对端证书的服务器间认证，增强通信安全
- 🐛 修复多项关键 Bug：包括 ACL 权限绕过、I/O 线程忙循环、内存统计不准确、崩溃及 RDB/AOF 加载健壮性问题
- 🚀 性能与资源优化：改进 `lpSeek()`、优化宽 `HSET`、减少内存碎片计算、降低 HNSW 索引内存占用等
- 🧩 模块 API 增强：新增集群拓扑变更、fork 子事件、槽迁移结束事件及键通知后绑定任务等回调
- ⚙️ 新增多个配置参数与指标，涵盖紧凑哈希模板、内存统计、`INFO` 与 `MEMORY STATS` 输出
- 🛠️ CLI 工具增强：`--latency` 支持指定百分位数，`redis-cli --cluster reshard/rebalance` 使用原子槽迁移
- 📦 提供 Alpine、Debian、snap、brew、RPM 及 APT 等多种安装方式，并支持主流 Linux 发行版与 macOS（Intel/ARM）

---

### [](https://github.com/AsyncBanana/microdiff)

**原文标题**: [GitHub - AsyncBanana/microdiff: A fast, zero dependency object and array comparison library. Significantly faster than most other deep comparison libraries and has full TypeScript support. · GitHub](https://github.com/AsyncBanana/microdiff)

Microdiff 是一个快速、微小的对象与数组比较库，零依赖、体积小于 1kb，并有完整 TypeScript 支持。它提供简单的 diff() 函数，支持多运行环境和循环引用，性能显著优于同类库。

- ⚡ 速度极快：比大多数对象差异库快两倍以上，基准测试远优于 deep-diff、deep-object-diff 和 jsDiff
- 📦 超轻量：压缩后小于 1kb，零依赖，体积开销极小
- 🌎 多环境支持：可用于 Deno、Node、Bun、Web 及 Service Workers，内置 TypeScript 类型
- 🔰 易用性：只需调用单个 `diff(obj1, obj2)` 函数即可完成比较
- 📅 特殊对象支持：完整支持 `Date`、`RegExp` 等复杂类型的比较
- 🔄 变更类型明确：返回 `CREATE`、`REMOVE`、`CHANGE` 三种操作，并带有 `path`、`value`、`oldValue` 字段
- ♻️ 循环引用：默认支持循环引用，可通过 `cyclesFix: false` 关闭以提升性能
- 📊 基准测试（Node 22 / Ryzen 7950x）：microdiff 无循环模式为 100%，开启循环为 149%，而 deep-diff 为 197%、deep-object-diff 为 288%、jsDiff 高达 1565%
- 🤝 易于贡献：可用 `npm run build` 构建、`npm run bench` 跑基准、`npm run test` 跑测试，并遵守行为准则

---

### [](https://github.com/sveltejs/devalue)

**原文标题**: [GitHub - sveltejs/devalue: Gets the job done when JSON.stringify can't · GitHub](https://github.com/sveltejs/devalue)

devalue 是一个 JavaScript 序列化库，能处理 JSON.stringify 无法完成的场景（如循环引用、特殊值和内置类型），同时强调性能、XSS 安全与紧凑输出。

- 🔄 支持循环引用（`obj.self = obj`）与重复引用（`[value, value]`）
- 🔢 能序列化 `undefined`、`Infinity`、`NaN`、`-0`、`BigInt`
- 🧩 内置支持正则、日期、`Map`/`Set`、`ArrayBuffer`/Typed Arrays、`URL`/`URLSearchParams`、`Temporal`
- 🎨 通过 reducers/revivers 或 replacer 实现自定义类型序列化
- ⏳ `stringifyAsync` 可等待并序列化 Promise 的解析结果
- 🎯 设计目标：高性能、安全、输出紧凑；非目标：人类可读、序列化函数、跨版本稳定
- ✍️ `uneval` 生成可执行 JS 代码，`stringify`/`parse` 则类似 JSON 方法，适用于不能执行 eval 的场景
- 🧩 `unflatten` 可从更大的 JSON 字符串中只还原 devalue 部分数据
- 🛠 可自定义 `StringifyOperations`/`ParseOperations`，支持无副作用序列化和跨运行时（如 `node:vm`、WASM）
- ⚠️ 遇到未处理的函数或非 POJO 会抛出错误，并可通过 `error.path` 定位问题位置
- 🛡️ XSS 缓解：自动转义 `</script>` 等危险字符，且拒绝函数/非 POJO，阻止恶意代码执行
- 🔒 安全提醒：不要用 `uneval` 将客户端用户数据发回服务器；`eval` 应使用间接调用 `(0, eval)` 避免作用域泄漏
- 📦 项目采用 MIT 许可证，受 `lave`、`arson`、`oson` 等启发

---

### [](https://svelte.dev/playground/138d70def7a748ce9eda736ef1c71239)

**原文标题**: [devalue demo â¢ Playground â¢ Svelte](https://svelte.dev/playground/138d70def7a748ce9eda736ef1c71239)

概述：这份内容是 Svelte 官方教程的完整目录，涵盖了从入门基础到高级模式的系统学习路径，包括响应式、组件通信、事件、绑定、生命周期、状态管理、动效、SVG 以及实际示例等核心主题。

- 📘 基础介绍：包括动态属性、样式、嵌套组件、HTML 标签等入门概念
- ⚡ 响应式核心：响应式赋值、声明与语句的用法
- 🎁 Props 机制：声明、默认值及展开传递
- 🔀 逻辑控制块：if、else、each、await 等模板逻辑
- 🖱️ 事件处理：DOM 事件、组件事件及事件转发
- 📝 表单绑定：输入框、复选框、选择框、文件、媒体元素、canvas 等绑定
- ⏳ 生命周期管理：onMount、onDestroy、tick 的运用
- 🌐 Stores 状态管理：可写、可读、派生、自定义及自动订阅
- 🎭 动效与缓动：tweened 和 spring 实现平滑动画
- 🔄 过渡效果：指令、参数、自定义 CSS/JS 过渡及延迟过渡
- 🌀 动画指令：animate 指令与缓动可视化
- 📊 SVG 实例：时钟、柱状图、面积图、散点图及 SVG 过渡
- 🛠️ Actions 指令：use 指令、参数及复杂动作封装
- 🎨 类绑定指令：class 指令与简写形式
- 🧩 组件组合技巧：渲染 props、回退、命名与条件渲染
- 🔗 Context API：setContext 与 getContext 实现跨组件通信
- 🧬 特殊元素：svelte:element、window、document、body、head 的高级用法
- 📦 模块上下文：命名导出的应用
- 🐛 调试工具：@debug 标签的使用
- 🏗️ 7GUIs 实战：计数器、温度转换器、航班订票器、计时器、CRUD 及圆绘制器
- 🧩 杂项扩展：递归组件、动态组件和 Hacker News 示例

---

### [首页 | node-x11](https://sidorares.github.io/node-x11/)

**原文标题**: [Home | node-x11](https://sidorares.github.io/node-x11/)

overview summary  
- 🚀 纯 JavaScript 实现，零依赖，无需原生代码或 node-gyp，直接在 unix socket 或 TCP 上通信 X11 协议  
- 📦 完整支持核心协议与扩展：120 个核心请求、34 个事件，以及 RENDER、RANDR、XFIXES、Composite、Damage、SHAPE、XTEST、XKB、XInput、MIT-SHM 等  
- 🎮 完整 GLX 1.4 支持（含厂商扩展），可直接在 Node.js 中创建 GL 上下文并渲染 OpenGL 内容  
- 🌐 可插拔传输层，可在浏览器中运行（支持任意双工流），Playground 即将提供在线演示  
- 🖥️ 直接与 X server 对话，安装命令 `npm install x11`，单次调用即可连接，所有请求都作为客户端方法使用  
- 📖 提供入门指南和 API 参考，示例代码展示创建窗口、绘制文本并响应 Expose 事件

---

### [](https://sidorares.github.io/node-x11/playground)

**原文标题**: [Playground | node-x11](https://sidorares.github.io/node-x11/playground)

该页面展示了一个完全在浏览器中运行的 X 服务器模拟环境，右侧面板通过纯 JavaScript X 服务器将真实 X 会话渲染到画布上；编辑器中的代码与真实 node-x11 客户端相同，通过自定义 DISPLAY 传输连接，且所有代码片段都保存在链接中，无需服务器存储。

- 🖥️ 页面右侧是真实的 X 会话，由纯 JavaScript X 服务器合成到 canvas 上。
- 📝 编辑器运行标准 node-x11 客户端代码，通过自定义 DISPLAY 传输（demo/local:0）连接。
- 🔗 点击 Share 可将整个代码片段放入链接查询字符串，无需服务器存储。
- ⚠️ 这是运行 X 服务器的“慢速”方式：所有内容均为模拟，服务器用 JavaScript 在主线程中栅格化。
- 📡 输入通过 postMessage 跨 iframe 边界传输；而桌面环境通常通过 Unix socket 连接 GPU 加速的 C X 服务器。
- 🧪 该环境用于评估协议行为，性能则需在真实服务器上测试。
- 🎨 演示示例涵盖窗口、渐变、文本、图形绘制、裁剪、位图、指针绘画、光栅操作、事件日志、动画、键盘、RENDER 扩展（Porter-Duff 算子、渐变、变换/滤镜）、窗口管理器以及 OpenGL（GLX）三角形和旋转立方体。
- 👋 示例包括“Hello window”，展示创建和映射窗口并绘制问候语。

---

### [pnpm 11.20 | pnpm](https://pnpm.io/blog/releases/11.20)

**原文标题**: [pnpm 11.20 | pnpm](https://pnpm.io/blog/releases/11.20)

overview summary
- 🔒 修复多注册表安装时的包替换风险，按注册表限定键记录包来源。
- 🏷️ 新增内置 `npmjs:` 别名，可直接锁定公共注册表。
- 🛠️ 修复空代理设置导致安装失败的问题，并支持 `proxy=false` 关闭代理。
- 🛡️ 增强 `pnpm rebuild` 对恶意锁文件的防护，拒绝路径穿越包名。
- ⚡ 优化依赖解析性能，减少元数据过滤和 semver 重复解析。

- 🔐 **安全修复**：包现在以 `<name>@<registryName>:<version>` 格式记录在锁文件中，区分不同注册表的同名包，避免意外替换。
- 📦 锁文件格式版本不变，仅影响使用命名注册表的项目，旧版 pnpm 仍可读取。
- ⚠️ 使用命名注册表的用户需提交锁文件变更，且团队需统一使用新版本，避免锁文件在旧版与新版间反复切换。
- 🚫 若锁文件引用的注册表别名被删除，会报 `ERR_PNPM_MISSING_NAMED_REGISTRY`，不再静默回退到默认注册表。
- 🧩 禁止使用保留前缀（如 `file`、`link`、`npm` 等）作为注册表别名，否则报 `ERR_PNPM_RESERVED_NAMED_REGISTRY_NAME`。
- 📌 新增内置 `npmjs:` 别名，无需配置即可指向 `registry.npmjs.org`，可覆盖代理或镜像设置。
- 🖥️ 支持通过 `pnpm-workspace.yaml` 覆盖 `npmjs:` 别名，指向内部镜像，并影响锁文件验证逻辑。
- 🧹 空代理环境变量（如 `HTTP_PROXY=`）视为未设置，不再报错；`proxy=false` 可明确关闭代理。
- 🛡️ `pnpm rebuild` 拒绝包含路径遍历包名的锁文件（如 `../../../escaped@1.0.0`），防止脚本在虚拟存储外执行。
- ⏩ 当目标 pnpm 版本 ≥12 时，环境锁文件不再固定 `@pnpm/exe`（因为 v12 起 `pnpm` 本身即原生可执行文件）。
- 🔄 修复锁文件 tarball URL 与注册表 URL 匹配顺序不确定的问题，确保一致性。
- ⚡ 性能优化：`minimumReleaseAge` 激活时按文档而不是依赖边过滤元数据，并复用已解析的 semver 版本。

---

### [](https://github.com/pnpm/pnpm/releases/tag/v12.0.0-rc.0)

**原文标题**: [Release pnpm 12 RC 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v12.0.0-rc.0)

pnpm v12.0.0-rc.0 发布，主要包含安全性提升、依赖链接修复、并发安装优化及多种边界情况处理。

- 🚫 通过 sudo 运行 pnpm setup、self-update 或全局安装命令会报错 ERR_PNPM_SUDO_NOT_SUPPORTED，只读全局命令不受影响。
- 📁 修复以反斜杠作为分隔符的压缩包路径：嵌套路径正确解析，路径遍历被拒绝。
- 🔄 修复 file: 依赖源目录变化后未重新复制的问题，现在编辑本地包并运行 pnpm install 会更新 store 中的副本。
- 📝 使用每项目锁文件时，将受阻止构建的批准脚手架写入发现的工作区清单。
- 🤝 并发安装共享全局虚拟存储不再报“Directory not empty”错误，也不会短暂移除其他进程正在读取的包目录。
- 🔗 修复 enableGlobalVirtualStore 下的 link: 依赖，使链式子项实体化并按解析目标隔离槽位。
- 🧩 无头安装（--frozen-lockfile）现在会为公开提升的工作区包的 bin 创建命令 shim，与普通安装一致。
- ❌ pnpm fetch 及 virtualStoreOnly 安装不再在 nodeLinker: pnp 下写入 .pnp.cjs 加载器。
- 🛡️ 防止当 modulesDir 解析到项目根目录时 pnpm 删除项目文件。
- 📄 修复 pnpm-lock.yaml 带有前导环境锁文件文档、且文件为 CRLF 行尾或含 UTF-8 BOM（Windows core.autocrlf 产生）时被误判为多个 YAML 文档并忽略的问题。
- 📂 当项目上方的目录不支持硬链接（如 AI agent 沙箱或只挂载项目可写）时，默认 store 创建在 <project>/node_modules/.pnpm-store 而不是 pnpm 主目录。
- 🧹 node_modules 中的非目录杂项条目不再导致安装失败，而是被跳过。

---

### [](https://github.com/honojs/hono/releases/tag/v4.13.0)

**原文标题**: [Release v4.13.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.13.0)

Hono v4.13.0 正式发布，本次更新亮点包括性能大幅优化、对 HTTP QUERY 方法的一等支持、新增 Method Not Allowed 中间件，以及多项开发体验改进。核心请求/响应路径经低层优化后，在常见路由上性能最高提升 1.25 倍；QUERY 方法现已在核心及内置中间件（Cache、ETag、CORS）中获得完整支持。

- 🚀 性能优化：核心请求/响应路径提速最高 1.25 倍（如 json 路由从 528.99ns 降至 422.44ns），通过跳过不必要的 Headers 分配、用 indexOf 替代正则测试、惰性分配内部状态等实现
- 📨 新增 QUERY 方法一等支持：依据 RFC 10008 标准，可使用 `app.query()` 定义安全的、可携带请求体的幂等请求处理
- 🗃️ Cache 中间件支持 QUERY：缓存键现包含请求内容的 SHA-256 摘要，不同查询体分别缓存；注意内部缓存键格式已变更（/.hono/cache?__hono_cache_key=...），需更新外部清理逻辑
- 🏷️ ETag 与 CORS 中间件适配：ETag 支持 QUERY 条件请求（返回 304）；CORS 默认 Allow-Methods 现包含 QUERY（GET, HEAD, PUT, POST, DELETE, PATCH, QUERY）
- 🚫 新增 Method Not Allowed 中间件：路径匹配但方法不允许时返回 405 响应及正确的 Allow 头，并支持通过 `onMethodNotAllowed` 选项自定义响应
- ⚡ RegExpRouter 改进：不支持的路径组合在注册时即抛出 `UnsupportedPathError`，实现启动时快速失败，注册加首次匹配提速约 20%
- 🔧 其他改进：`hono/utils/headers` 同步 IANA 注册表新增字段（如 Accept-Query）；JWT/JWK 中间件新增 `realm` 选项且正确转义质询值；JSX 的 `useRef`/`RefObject` 对齐 React 19 类型；函数组件可返回子元素数组；Compress 中间件在协商响应中设置 `Vary: Accept-Encoding` 头

---

### [](https://github.com/jaydenseric/graphql-upload)

**原文标题**: [GitHub - jaydenseric/graphql-upload: Middleware and a scalar Upload to add support for GraphQL multipart requests (file uploads via queries and mutations) to various Node.js GraphQL servers. · GitHub](https://github.com/jaydenseric/graphql-upload)

graphql-upload 是一个为 Node.js GraphQL 服务器提供文件上传能力的库，通过中间件和 `Upload` 标量实现 GraphQL multipart 请求规范。它支持 Koa、Express 等主流框架，允许文件作为查询或变更变量上传，并能流式处理文件内容。

- 📦 提供 `Upload` 标量及 `graphqlUploadKoa`、`graphqlUploadExpress` 中间件，可快速集成文件上传。
- 🔧 支持 `processRequest` 函数用于自定义中间件，灵活适配不同服务器环境。
- 🚀 文件通过 `Upload` 变量传递，解析器获得包含 `createReadStream` 的 Promise，便于流式处理或存储。
- ⚙️ 使用 `busboy` 解析 multipart 请求，`fs-capacitor` 将上传缓冲到文件系统，支持并发读写。
- ⚠️ 注意：需要确保临时目录可读写、磁盘空间充足，并妥善处理上传流错误。
- 🔄 建议用 `Promise.all` 或 `Promise.allSettled` 并发处理多个上传，避免响应提前发送。
- 🛠️ 运行环境要求 Node.js `^22.13.0 || ^24.0.0 || >=26.0.0`，并需配置 TypeScript 以支持 ECMAScript 模块。
- 📁 npm 包无主入口，需从 `GraphQLUpload.mjs`、`graphqlUploadExpress.mjs` 等模块深导入。
- 🔗 可参考 Apollo 上传示例及 GraphQL multipart 请求规范进行扩展。

---

### [](https://github.com/harrisiirak/cron-parser)

**原文标题**: [GitHub - harrisiirak/cron-parser: Typescript library for parsing crontab instructions · GitHub](https://github.com/harrisiirak/cron-parser)

这是一个用于解析和操作 cron 表达式的 JavaScript/TypeScript 库，支持时区处理、夏令时转换、迭代器、严格模式、日期范围自动调整、crontab 文件解析、字段编程式修改以及可种子化的随机抖动（H 字符）等高级功能。

- 📦 支持 Node.js >= 18 和 TypeScript >= 5，通过 `npm install cron-parser` 安装。
- ⏱ 标准 cron 格式包含秒、分、时、日、月、周 6 个字段，支持 `*`、`?`、`,`、`-`、`/`、`L`、`#`、`H` 等特殊字符。
- 📅 提供 `@yearly`、`@monthly`、`@daily`、`@hourly`、`@weekdays` 等预定义表达式快捷方式。
- ⚙️ 可配置选项包括 `currentDate`、`startDate`、`endDate`、`tz`（时区）、`hashSeed`（随机种子）和 `strict`（严格模式）。
- 🔄 基本用法：通过 `CronExpressionParser.parse()` 解析表达式，使用 `next()`、`prev()`、`take(n)` 获取日期。
- 📆 日期范围自动处理：若未提供 `currentDate` 则回退到 `startDate`，超出 `startDate`/`endDate` 边界时自动钳制，迭代时仍会校验范围并抛出“Out of the time span range”错误。
- 📂 支持解析 crontab 文件，提供异步 `parseFile()` 和同步 `parseFileSync()` 方法，返回变量、表达式和错误信息。
- 🚨 严格模式：禁止同时设置“日”和“周”字段，要求必须包含全部 6 个字段，并拒绝空表达式，避免歧义。
- 📌 支持 `L`（月中最后一天/周中最后一天）以及 `1L`、`3L` 这样的“本月最后一个指定星期几”语法，还可与其他星期几组合。
- ♻️ 表达式结果可直接迭代（`for...of`），也可用 `take()` 批量获取多个未来日期。
- 🌍 基于 Luxon 提供稳健的时区支持，能正确处理夏令时（DST）切换。
- 🛠 通过 `CronFieldCollection.from()` 可编程化修改小时、分钟、星期等字段，支持传入原始值或 CronField 实例。
- 🎲 支持 `H` 字符生成随机抖动值（如 `H/5`、`H(0-10)`），可用 `hashSeed` 使结果可复现，灵感来自 Jenkins cron 语法。
- 🤝 欢迎贡献，提供贡献指南、行为准则和安全策略；项目采用 MIT 许可证。

---

### [API、AI 和 MCP 的统一网关 - Zuplo](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

**原文标题**: [The Unified Gateway for APIs, AI, and MCP - Zuplo](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

Zuplo 是一个面向 API 和 AI 的统一网关，通过单一可编程策略引擎，管理每一次 API、LLM 和 MCP 调用，同时覆盖出站（应用调用模型）与入站（AI 代理调用你的 API）流量，提供安全、治理、可观测性和成本控制。

- 🔀 统一网关处理双向流量：应用调用 LLM（出站）和 AI 代理调用你的 API（入站），均通过同一网关，策略一次编写、双向生效。
- 🛡️ 四大核心能力：Agents（MCP 访问）、Users（API keys/JWT/OAuth）、APIs & MCPs（REST/GraphQL/MCP）、LLMs（路由、预算、缓存、护栏）共用一套政策引擎。
- 💰 成本控制：动态速率限制吸收流量尖峰，按团队/密钥设置硬性预算和上限，阻止失控代理超支；示例显示 14 天节省 $42.9k，总成本下降 41%。
- 📊 完整可见性：每次调用记录代理、用户、工具、状态、延迟和策略，支持实时仪表盘并导出 Datadog/SIEM，满足审计需求。
- 🔒 安全与治理：认证失败、速率超限、无效 schema、提示注入等恶意流量在网关处被拦截，12.4k 次请求被阻止，0 次到达源站。
- 💵 变现与计量：内置计划、配额、计量和 Stripe 计费，可按请求、token 或任意单位向客户收费，无需自建计费系统。
- 🔌 代码集成简单：出站仅需替换 OpenAI SDK 的 baseURL；入站通过 OpenAPI 扩展标记 MCP 工具，即可暴露为 MCP 端点。
- 🚀 生产验证：客户案例显示 2 个月迁移、成本节省超 70%、数小时上线 MCP 服务器、支持 1B+ 终端用户，SLA 99.99%，SOC 2 Type II。
- ⚡ 快速上线：免费层包含 100K 请求/月，无需信用卡，几分钟内即可部署到 300+ 边缘位置，约 20 秒完成部署。

---

### [](https://www.youtube.com/watch?v=o98XmRVjxWs)

**原文标题**: [The secret third option for JavaScript comments - YouTube](https://www.youtube.com/watch?v=o98XmRVjxWs)

overview summary
- 📄 涵蓋網站基本資訊：簡介、媒體、著作權與聯絡方式
- 👤 提供創作者與廣告相關的支援說明
- 🛠️ 包含開發人員資源及條款、隱私權政策
- 🔍 說明 YouTube 運作方式與新功能測試
- ⚖️ 標示版權所有：© 2026 Google LLC

---

### [](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html#sec-hashbang)

**原文标题**: [ECMAScript® 2027 Language Specification](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html#sec-hashbang)

该文档是 ECMAScript 语言规范的整体目录，并重点摘录了“第 12 章：词法语法”的详细内容，涵盖从源码文本到语法记号的定义与规则。

- 📘 规范覆盖完整语言体系：从简介、一致性、术语、表示约定，到数据类型、抽象操作、对象行为、执行上下文和内置对象。
- 🧱 词法语法负责把源码转为输入元素，包括记号、行终止符、注释和空白，并按语法上下文选择多种词法目标（如 InputElementDiv、RegExp 等）。
- ⬜ 空白字符与行终止符有明确的 Unicode 范围；行终止符还影响自动分号插入及语法解析行为。
- 💬 注释支持单行与多行形式，多行注释不能嵌套，且含行终止符的多行注释会被视为行终止符；另有 Hashbang 注释。
- 🔑 标识符基于 Unicode ID_Start / ID_Continue，并允许 `$`、`_` 及 Unicode 转义；关键字与保留字区分上下文用法（如 `async`、`await`、`yield`）。
- 🔣 标点符号、数字字面量、字符串字面量、正则表达式字面量和模板字面量都有精确定义，包括转义序列、分隔符及数值计算规则。
- ⚙️ 自动分号插入（ASI）规则详细说明了在哪些情况下分号会被自动插入，并列出受限产生式（如 `return`、`break`、`continue`、箭头函数等）。
- 📚 文档还包含大量附录，如 Web 浏览器的额外特性、严格模式、宿主分层点，以及语法汇总和参考书目。

---

### [](https://astro.build/)

**原文标题**: [Astro](https://astro.build/)

Astro 7.2 是一款专为内容驱动型网站设计的 JavaScript 网页框架，主打服务器优先渲染、零默认 JavaScript、极致性能与灵活集成，现已正式发布，并被全球大型企业广泛采用。

- 🚀 **Astro 7.2 正式发布**：专为内容驱动型网站打造，支持营销页、博客、电商等场景，快速上手命令为 `npm create astro@latest`。

- 🖥️ **服务器优先渲染**：组件在服务器端渲染，向浏览器发送轻量 HTML，极大减少不必要的 JavaScript 开销，提升网站性能。

- 📝 **内容驱动设计**：可从文件系统、外部 API 或任意 CMS 加载数据，天然适配各类内容工作流。

- 🧩 **高度可定制**：支持接入任意 JavaScript UI 组件、CSS 库、主题与集成，灵活扩展。

- ⚡ **行业领先性能**：Astro 的 Core Web Vitals 达标率达 66%，远超 WordPress（48%）、Gatsby（47%）、Next.js（30%）和 Nuxt（28%）。

- 🏝️ **Astro Islands 架构**：独特的页面加载优化机制，可显著提升转化率、核心体验指标与 SEO。

- 🔗 **零锁定自由集成**：支持 React、Vue、Preact、Svelte、Solid 等主流框架，可复用现有组件并享受优化后的客户端构建性能。

- 📦 **功能全面内置**：包含内容集合（TypeScript 类型安全）、零默认 JavaScript、视图过渡、图片优化、UI 集成、文件路由、中间件、Actions 后端函数、部署适配器等。

- 🧭 **简单模板语法**：只要懂 HTML 就能编写 Astro 组件，团队协作门槛低。

- 🔮 **AI 就绪与开发者体验**：官方 MCP 服务器、环境变量管理、内置开发工具栏等，提升开发效率。

- 🎨 **丰富生态与主题**：提供电商、博客、文档、作品集、落地页等大量主题，并可快速浏览使用。

- 🤝 **专业伙伴机构支持**：如 Bejamas、Lucky Media、Seibert Group 等，提供从落地页到电商的专业 Astro 服务。

- 💖 **免费开源**：Astro 完全免费开放源代码，并感谢 Netlify、Webflow、Cloudflare 等赞助商支持。

---

### [](https://flueframework.com/blog/flue-2/)

**原文标题**: [Flue 2.0 | Flue](https://flueframework.com/blog/flue-2/)

Flue 2.0 正式发布，这是一个基于全新 hooks API 的智能体框架，支持构建可动态演化能力的智能体，并带来多项基础设施升级。

- 🎉 发布 Flue 2.0：从静态智能体定义重构为 hooks 驱动，解决复杂工作流与能力扩展难题。
- 🔗 核心机制 Agent Hooks：支持持久化状态、生命周期事件、按需动态挂载模型/工具/技能，类似“React for Agents”。
- 📦 内置 16 个 hooks：涵盖 useTool、useSkill、useSubagent、useSandbox、usePersistentState 等，并支持自定义可组合 hooks。
- 🖥️ 全新 CLI 与 Vite 架构：本地与 CI 用 `flue run`，托管智能体直接基于 Vite 构建，Hono 负责路由。
- 🔌 内置无状态 MCP：通过 useMcpConnection 挂载远程 MCP 工具，可条件启用并优雅降级。
- 💾 简化工作流与 Actions：移除 defineWorkflow，借助持久化消息实现确切的“一次处理”，支持 durable 工具与 step.do()。
- 📡 新会话级 SDK：`@flue/sdk` 提供 send/read/observe/abort 方法，前端可用 `@flue/react` 流式接入同一会话。
- 🌐 Cloudflare 零配置追踪：部署后启用 Workers Traces 即可获取对话内容、成本等指标，无需额外代码。
- 🧭 迁移支持：提供从 Flue 1.0 Beta 的迁移指南，并可通过提示词让编码助手快速搭建首个项目。

---

### [](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=26)

**原文标题**: [USPTO TTABVUE. Proceeding Number 92086835](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=26)

无法总结：未找到主要内容。

---

### [](https://www.youtube.com/watch?v=V_qzqY1bb7I)

**原文标题**: [Reliability Lessons From SQLite - Richard Hipp | SSW 2026 - YouTube](https://www.youtube.com/watch?v=V_qzqY1bb7I)

概述：此內容為 YouTube 頁面底部的標準資訊與連結，涵蓋公司介紹、法律條款、創作者資源及平台運作說明。

- 📄 提供簡介、媒體資訊與著作權相關連結
- 📮 包含與我們聯絡的管道
- 🎬 設有創作者與廣告專區
- 🛠️ 列出開發人員資源
- ⚖️ 涵蓋條款、隱私權及政策與安全性
- 🔍 說明 YouTube 運作方式及測試新功能
- ©️ 顯示 2026 Google LLC 版權聲明

---

### [CSS 现状 2026](https://2026.stateofcss.com/en-US/)

**原文标题**: [State of CSS 2026](https://2026.stateofcss.com/en-US/)

2026 年 CSS 状态调查显示，CSS 生态持续演进，涌现出锚点定位等新特性，但浏览器支持仍是主要瓶颈；同时 CSS 开发仍以手工编码为主，AI 参与度较低。

- 🧭 锚点定位（Anchor Positioning）成为最受欢迎的新 CSS 特性，但同时也因浏览器支持不足而被开发者回避。
- 🌐 浏览器兼容性问题（如 View Transitions、if() 等）仍是 CSS 特性落地的最大阻碍，Interop 等倡议有望改善。
- 🤖 相比其他 Web 技术，CSS 的 AI 生成比例较低（平均 28%），开发者普遍认为 AI 尚不能很好编写 CSS。
- 🧩 CSS 被视为一门独特语言，其长期演化和现代形态令人关注。
- 📊 调查样本为 4,902 人，覆盖新特性偏好、浏览器兼容性痛点及 AI 使用情况等多个维度。

---

