### [Node.js — Node.js 26.4.0（当前版本）](https://nodejs.org/en/blog/release/v26.4.0)

**原文标题**: [Node.js — Node.js 26.4.0 (Current)](https://nodejs.org/en/blog/release/v26.4.0)

Node.js 26.4.0 版本发布，包含多项新功能和改进。

- 📦 新增 `node:vfs` 子系统，支持挂载虚拟文件系统实例
- 📁 `fs` 模块支持调用者提供 `readFile()` 缓冲区
- 🌐 `http` 模块的 `closeIdleConnections` 可关闭预请求套接字
- 🗺️ 加载器实现包映射（package maps）功能
- 🔗 `net` 模块的 `setKeepAlive` 支持 TCP_KEEPINTVL 和 TCP_KEEPCNT
- 🔒 `tls` 模块新增 certificateCompression 选项
- 🚀 FFI 增加对 AArch64 和 x86_64 的快速调用 API
- 📊 `blockList` 稳定性状态更新为候选发布版本
- 🛠️ 多项性能优化和错误修复，涵盖 stream、crypto、test_runner 等模块

---

### [模块：包 | Node.js v26.4.0 文档](https://nodejs.org/api/packages.html#package-maps)

**原文标题**: [Modules: Packages | Node.js v26.4.0 Documentation](https://nodejs.org/api/packages.html#package-maps)

Node.js v26.4.0 文档概述了 Node.js 中包管理的核心概念，特别是 `package.json` 文件的使用和模块系统。

- 📦 **包与模块系统**：包由 `package.json` 文件描述，Node.js 通过 `"type"` 字段（`"module"` 或 `"commonjs"`）决定 `.js` 文件的模块系统，`.mjs` 和 `.cjs` 扩展名可强制指定类型。
- 🚪 **包入口点**：`"exports"` 字段是现代替代 `"main"` 的方案，支持定义多个子路径导出和条件导出（如 `import` vs `require`），并封装内部模块；`"main"` 用于旧版兼容。
- 🔗 **子路径与模式**：通过 `"exports"` 或 `"imports"` 字段可定义精确的子路径导出（如 `"./submodule.js"`）或使用 `*` 模式匹配大量文件，避免 `package.json` 膨胀。
- 🧩 **条件导出**：支持按环境（如 `"node"`、`"import"`、`"require"`、`"default"`）映射不同路径，条件按对象键顺序从最具体到最通用匹配，可嵌套使用。
- 🏷️ **包映射（实验性）**：通过 `--experimental-package-map` 启用，使用 JSON 文件定义包 ID 和依赖关系，无需 `node_modules` 结构，适用于 monorepo 和依赖隔离。
- 🔄 **自引用**：包内模块可通过包名引用自身 `"exports"` 中定义的路径，需 `package.json` 包含 `"name"` 和 `"exports"` 字段。
- 📋 **`package.json` 字段定义**：关键字段包括 `"name"`（包名）、`"main"`（默认入口）、`"type"`（模块类型）、`"exports"`（导出定义）和 `"imports"`（内部导入映射）。

---

### [vfs: 由 mcollina 添加最小节点 vfs 子系统 · 拉取请求 #63115 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63115)

**原文标题**: [vfs: add minimal node:vfs subsystem by mcollina · Pull Request #63115 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63115)

Node.js 合併了一個實驗性的虛擬文件系統（VFS）子系統，在 `--experimental-vfs` 標誌後可用。

- 📦 新增 `node:vfs` 內建模組，包含 `VirtualFileSystem`、`VirtualProvider`、`MemoryProvider` 和 `RealFSProvider` 類別。
- 🔬 此功能為實驗性質，需透過 `--experimental-vfs` 命令列標誌啟用。
- 🚫 初始合併不包含與 `node:fs`、模組載入器或 SEA 的整合，這些功能將在後續 PR 中實現。
- 📊 總計約 10,000 行程式碼，其中測試佔最大部分（約 5,000 行），程式碼約 4,000 行，文件約 1,000 行。
- ✅ 經過多次程式碼審查和 CI 測試後，於 2026 年 5 月 23 日合併至 main 分支。
- 📝 後續 PR（#63537）實現了將 `fs/promises` 分派到已掛載的 VFS 實例。
- 🎉 此功能包含在 Node.js v26.4.0 版本中。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

概述：Tiger Cloud 提供可扩展的 PostgreSQL 时序数据库服务，具备高性能、企业级安全和深度可观测性，支持快速部署与弹性计费。

- 🚀 单服务可处理每日 3 万亿指标、3PB 数据及 1 千万亿数据点，提供 30 天$1000 免费额度
- 💰 计算与存储分离架构，独立扩展，避免为闲置容量付费，降低成本
- 🔄 支持最多 10 节点读写分离副本集，结合 SSD/S3 分层存储实现无限扩展
- 🛡️ 多可用区集群自动故障切换、时间点恢复与跨区域备份，保障高可用
- 🔐 符合 SOC 2、HIPAA、GDPR 标准，内置加密、SSO、RBAC 及审计日志
- 📊 深度可观测性：查询下钻、性能仪表盘，集成 CloudWatch、Datadog、Prometheus
- ⚡ 数分钟内完成数据库部署，支持 SQL、CLI、Terraform、Cursor、Claude Code 管理
- 🔌 无缝集成主流云提供商及 PostgreSQL 生态系统
- 👨‍💻 提供 24/7 全球 Postgres 专家支持，企业级 SLA 与区域数据隔离

---

### [阻止安装脚本并非万能良策](https://nodesource.com/blog/npm-v12-install-scripts-not-a-silver-bullet)

**原文标题**: [Blocking Install Scripts Is Not a Silver Bullet](https://nodesource.com/blog/npm-v12-install-scripts-not-a-silver-bullet)

npm v12 禁止了安装脚本，但这并非安全银弹，攻击者已将目标转向运行时。真正的防御需要结合权限模型和沙箱环境，层层设防。

- 🔒 **npm v12 的改进**：默认关闭 `allowScripts`、`--allow-git` 和 `--allow-remote`，阻止安装时自动执行脚本，减少供应链攻击面。
- ⚠️ **安装脚本的局限性**：攻击者已适应，如通过 `binding.gyp` 隐式触发 `node-gyp rebuild`（如 Miasma 恶意软件），或使用二进制文件（如 IronWorm）。
- 🚀 **攻击转向运行时**：恶意代码移至模块加载时执行，如顶层 IIFE（立即调用函数表达式），在 `require()` 或 `import` 时自动运行，无需安装钩子。
- 💻 **运行时攻击示例**：攻击者可在模块中注入代码，执行指纹识别、窃取环境变量、外传数据，甚至自我清理，所有操作均不依赖安装脚本。
- 🛡️ **Node.js 权限模型**：使用 `--permission` 标志限制运行时能力，如禁止子进程、网络访问和文件写入，缩小攻击半径，但需注意其非安全边界，且 `process.env` 访问不受限。
- 🏠 **沙箱环境**：结合 OS 级隔离（如容器、seccomp）、网络出口白名单和微虚拟机，提供更强保障，超越进程内限制。
- 🔧 **CI 中的安全**：在 CI 工作流中应用权限模型和出口监控（如 StepSecurity Harden-Runner），防止凭证泄露和恶意外传。
- 📋 **升级建议**：npm v12 预计 2026 年 7 月发布，需提前运行 `npm approve-scripts` 审核脚本，检查 Git 和远程依赖，启用权限模型，并添加 CI 出口控制。
- 🌟 **核心观点**：npm v12 是重要进步，但非终点；安全需分层防御，结合安装时阻断、运行时约束和环境隔离，才能有效应对供应链威胁。

---

### [npm v12 即将到来的破坏性变更 - GitHub 更新日志](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

**原文标题**: [Upcoming breaking changes for npm v12 - GitHub Changelog](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

npm v12 将于 2026 年 7 月发布，引入多项安全相关的默认变更，以提升安装过程的安全性。当前版本（11.16.0+）已提供警告，帮助用户提前准备。

- 🔒 `allowScripts` 默认关闭：`npm install` 不再自动执行依赖中的 `preinstall`、`install` 或 `postinstall` 脚本（包括 `node-gyp` 构建），需通过 `npm approve-scripts` 手动授权。
- 🚫 `--allow-git` 默认设为 `none`：`npm install` 不再解析 Git 依赖（直接或间接），以防止通过 `.npmrc` 覆盖 Git 可执行文件的代码执行风险。
- 🌐 `--allow-remote` 默认设为 `none`：`npm install` 不再解析远程 URL 依赖（如 HTTPS tarball），需显式允许。
- 🛠️ 准备步骤：升级到 npm 11.16.0+，运行 `npm approve-scripts --allow-scripts-pending` 查看待处理脚本，授权信任的包，提交更新后的 `package.json`。
- 📚 更多详情：参考文档 `npm approve-scripts`、`npm deny-scripts` 和 `allow-scripts` 配置，或在社区讨论中反馈问题。

---

### [权限 | Node.js v26.4.0 文档](https://nodejs.org/api/permissions.html)

**原文标题**: [Permissions | Node.js v26.4.0 Documentation](https://nodejs.org/api/permissions.html)

Node.js 权限模型概述  
- 🔒 权限模型通过 `--permission` 标志启用，限制文件系统、网络、子进程等资源访问  
- 🛡️ 采用"安全带"方法，防止可信代码意外修改文件或使用未授权资源，但无法防御恶意代码  
- ✅ 运行时 API 包括 `permission.has()` 检查权限和 `permission.drop()` 不可逆地撤销权限  
- 📂 文件系统权限通过 `--allow-fs-read` 和 `--allow-fs-write` 控制，支持通配符和路径  
- ⚙️ 支持配置文件（`node.config.json`）设置权限选项，自动启用 `--permission`  
- 🚀 使用 `npx` 时可通过 `--node-options` 传递权限标志，需注意文件系统读取错误  
- ⚠️ 权限模型不继承到工作线程，且对原生模块、网络、子进程等有约束  
- 🔓 `process._debugProcess()` 不受权限模型限制，可强制其他 Node.js 进程打开调试器  
- 🚧 已知限制包括符号链接绕过、文件描述符绕过、OpenSSL 引擎和运行时扩展加载限制

---

### [发布 v12.0.0-pre.1 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.1)

**原文标题**: [Release v12.0.0-pre.1 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.1)

npm v12.0.0-pre.1 预发布版本，包含多项重大变更、新功能和错误修复。

- ⚠️ **重大变更**：默认许可证从 "ISC" 改为空字符串；`allow-git` 和 `allow-remote` 默认设为 "none"；未知配置和标志现在会抛出错误。
- ✨ **新功能**：支持原生依赖修补（`npm patch add/commit/update/ls/rm`）；`npm init` 移除默认许可证；新增 `allowScripts` 安装脚本策略。
- 🐛 **错误修复**：修复 Git 操作中 HTTPS 协议保留问题；改进补丁命令的警告和锁文件同步；修复原型污染漏洞。
- 📚 **文档更新**：澄清 `approve-scripts` 仅在全局安装时抛出 `EGLOBAL`；更新 `package.json` 覆盖值规范。
- 📦 **依赖更新**：大量依赖升级，包括 `pacote@22.0.0`、`node-gyp@13.0.0`、`semver@7.8.4` 等。
- 🛠 **杂项**：更新问题模板；改进标志表输出；多个工作空间版本同步更新。

---

### [Deno，下一代 JavaScript 运行时](https://deno.com/)

**原文标题**: [Deno, the next-generation JavaScript runtime](https://deno.com/)

Deno 是一个现代化的 JavaScript/TypeScript 运行时，基于 Web 标准构建，提供零配置 TypeScript 支持、内置工具链和默认安全机制。

- ⭐ 拥有超过 10 万 GitHub Stars，40 万活跃用户和 200 万社区模块
- 🔒 默认安全：程序默认无文件、网络或环境访问权限，需显式授权
- 🚀 高性能网络：支持 HTTPS、WebSocket、HTTP2，请求处理速度超 Node.js 两倍
- 🛠 内置完整工具链：包含代码检查器、测试运行器、代码格式化器和独立可执行文件生成
- 📦 无缝兼容 npm 和 Node，可自动读取 package.json 或直接导入 npm 包
- 🌐 基于 Web 标准，实现浏览器与后端代码一致，积极参与 TC39 和 WinterCG
- ☁️ 专为云环境设计，支持 Deno Deploy、Docker、Digital Ocean、Fly.io 等平台
- 🌿 Fresh 2.0 框架：基于 Preact 和 Vite，采用岛屿架构，默认服务器端渲染
- 💬 社区高度评价其安全性、速度和易用性

---

### [桌面应用 | Deno 文档](https://docs.deno.com/runtime/desktop/)

**原文标题**: [Desktop apps | Deno Docs](https://docs.deno.com/runtime/desktop/)

### 概述总结
deno desktop 可将 Deno 项目（从单文件到 Next.js 应用）打包为跨平台桌面应用，支持框架自动检测、进程内绑定、交叉编译和内置自动更新，默认使用系统 WebView 以保持体积小巧。

- 🖥️ **核心功能**：将 TypeScript/Next.js 等项目打包为自包含桌面应用，包含 Deno 运行时和 Web 渲染引擎
- 📦 **体积优化**：默认使用操作系统原生 WebView，可选 Chromium (CEF) 后端，支持全 Node 兼容性
- 🔍 **框架自动适配**：无需修改代码即可支持 Next.js、Astro、Fresh、Remix 等主流框架，自动运行生产或开发服务器
- ⚡ **进程内通信**：通过进程内通道而非 IPC 实现后端与 UI 通信，减少跨进程开销
- 🌍 **交叉编译**：单机可构建 macOS、Windows、Linux 三平台应用，按需下载后端
- 🔄 **自动更新**：内置 bsdiff 二进制差异更新，支持回滚机制，通过 `latest.json` 清单管理
- 🛠️ **完整生态**：提供配置、窗口管理、菜单、托盘、通知、热更新、DevTools 等全套桌面功能
- 🚀 **快速入门**：`deno desktop main.ts` 即可编译，自动绑定 HTTP 服务器到 WebView

---

### [WebSocket 支持现已进入公开测试阶段 - Vercel](https://vercel.com/changelog/websocket-support-is-now-in-public-beta)

**原文标题**: [WebSocket support is now in Public Beta - Vercel](https://vercel.com/changelog/websocket-support-is-now-in-public-beta)

Vercel Functions 现已支持 WebSocket 连接，实现客户端与服务器端的双向通信。

- 🌐 支持实时功能：WebSocket 可用于交互式 AI 流、聊天和协作应用等实时场景
- ⚡ 运行于 Fluid compute：WebSocket 连接遵循与普通函数调用相同的限制和定价规则
- 💰 仅按处理时间计费：采用活跃 CPU 定价，仅对消息处理时间收费，空闲连接不收费
- 📦 标准 Node.js 库支持：无需额外配置，可直接使用 Express 和 ws 库创建 WebSocket 服务器
- 🔌 高级库兼容：支持 Socket.IO 等更高级的库
- 📚 提供文档：可查阅官方文档快速上手

---

### [介绍 | pnpm](https://pnpm.io/pnpr/)

**原文标题**: [Introduction | pnpm](https://pnpm.io/pnpr/)

pnpr 是一个用 Rust 编写的、兼容 pnpm 的 npm 注册表服务器，目前处于实验阶段，主要用于私有包管理、缓存代理和安装加速。

- 🔬 **实验性项目**：pnpr 仍在积极开发中，其行为、配置和 API 可能随版本变化。
- 📦 **私有注册表**：可托管组织内部私有包，支持按包设置访问和发布规则。
- ⚡ **缓存代理**：镜像上游注册表（如 npmjs.org），加速安装并应对上游故障。
- 🚀 **安装加速器**：服务端解析项目依赖图，为 pnpm 提供现成的锁文件。
- 🔗 **与 pnpm 的关系**：pnpr 是独立于 pnpm CLI 的服务器产品，但两者可协同工作，提升安装效率。
- 📜 **许可证**：采用 PolyForm Shield 1.0.0 许可证，允许运行、修改和自托管，但禁止用于竞争性产品。

---

### [如果 npm 运行在 AT 协议上会怎样？| James M Snell](https://www.jasnell.me/posts/what-if-npm-ran-on-atproto)

**原文标题**: [What If npm Ran on AT Protocol? | James M Snell](https://www.jasnell.me/posts/what-if-npm-ran-on-atproto)

以下是对文章内容的总结：

本文探讨了将 npm 包注册表构建在 AT Protocol（AT 协议）上的可能性，这是一个思想实验，旨在分析其优势、挑战和潜在创新。

- 🧩 **核心映射**：AT 协议的原语（如 DID、PDS、MST 等）可以自然地映射到包注册表的需求（如身份、命名空间、元数据、存储等），实现“发布在自己的仓库中，注册表发现你”的范式转变。
- 🏷️ **命名无冲突**：包名不再全局唯一，而是基于 DID 作用域（如 `@jsnell.dev/lodash`），彻底消除命名冲突、抢注和打字错误攻击。
- 🏢 **组织发布机制**：组织可运行自己的 PDS，通过双重记录（组织版本记录 + 个人发布证明）实现安全发布，即使组织 PDS 被攻破，攻击者也无法伪造个人证明，增强了供应链安全。
- 🔐 **信任模型**：AT 协议提供加密完整性（MST 签名）和身份验证（DID + 域名验证），但无法保证代码安全。需结合 Sigstore 等构建来源证明，形成“谁发布 + 代码来源”的完整链条。
- 🔍 **名称解析与审计**：名称到 DID 的映射需双重记录（发布者声明 + App View 授权），且变更公开可审计。锁定文件固定 DID，防止名称劫持。
- 🏷️ **标签系统**：独立标签服务可发布安全建议、恶意软件标记等，用户自由选择信任的标签者，打破 npm 单一数据库的垄断，实现可组合信任。
- ⚡ **性能潜力**：App View 架构支持服务端解析（一次请求返回完整依赖树），利用火鹤流预缓存数据，可能显著减少客户端往返次数，但需实际验证。
- 🔒 **私有包**：私有包需独立网络（公司自建 PDS、中继和 App View），与公共网络隔离，但保持相同协议和工具链，便于开源过渡。
- 🚧 **真实挑战**：包括个人 PDS 密钥托管问题、撤销传播延迟、性能不确定性、小型项目运行 PDS 的负担等。
- 💡 **独特创新**：可组合信任、无单点攻破（双重证明）、结构依赖混淆抵抗、透明所有权、可移植身份、可审计名称解析、身份 - 来源绑定等特性，是中心化模型难以复制的。

---

### [选择你的战士：为 Node.js 基准测试 5 个 WebSocket 服务器——火星编年史，Evil Martians 团队博客](https://evilmartians.com/chronicles/choose-your-fighter-benchmarking-5-websocket-servers-for-nodejs)

**原文标题**: [Choose your fighter: benchmarking 5 WebSocket servers for Node.js—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/choose-your-fighter-benchmarking-5-websocket-servers-for-nodejs)

以下是对五款 Node.js WebSocket 服务器的基准测试总结：

- 📊 在 10K 订阅者下，各服务器延迟相近（约 2-11 毫秒），但压力下表现分化明显。
- 🔄 AnyCable 在模拟网络中断时实现 100% 消息投递，且部署重启风暴中无需重启，广播吞吐量领先。
- ❌ 默认 Socket.io 在相同中断下丢失约 15% 消息，单机连接上限约 120K。
- ⚡ uWebSockets.js 单连接内存最省（约 5KB），但重启风暴恢复需数秒。
- 🛠️ 测试发现：负载生成器本身可能成为瓶颈（如单进程处理 10K 客户端导致延迟虚高），需分离测量工具与目标系统。
- 🧪 通过分片（40×250 客户端）和独立追踪验证，AnyCable 真实服务器端延迟仅 11 毫秒，而非最初报告的 234 毫秒。
- 🔍 关键教训：每个意外结果需用独立方法验证，避免仅怀疑工具或仅接受数据。
- 📈 连接容量：Socket.io 约 120K，AnyCable OSS 约 822K（内存瓶颈），AnyCable Pro 约 822K（内存仅用一半）。
- 🏆 综合表现：AnyCable 在抗网络抖动、部署恢复、大规模吞吐和内存效率上平衡最佳，但无单一服务器全胜。

---

### [AppSignal — 错误追踪与性能监控 | AppSignal](https://www.appsignal.com/?utm_source=node-weekly&utm_medium=newsletter&utm_campaign=appsignal_q2_2026&utm_content=n-plus-1)

**原文标题**: [AppSignal — Error Tracking & Performance Monitoring | AppSignal](https://www.appsignal.com/?utm_source=node-weekly&utm_medium=newsletter&utm_campaign=appsignal_q2_2026&utm_content=n-plus-1)

AppSignal 是一个集错误追踪、性能监控和日志分析于一体的全栈监控工具，帮助开发者快速定位并修复应用问题。

- 🚀 **错误追踪**：捕获所有异常和堆栈信息，按模式分组，在用户发现前定位问题。
- ⏱️ **性能监控**：监控响应时间、吞吐量和慢查询，从首次部署即开始。
- 🔗 **分布式追踪**：端到端追踪请求，识别跨服务的瓶颈。
- 📊 **自定义指标与仪表盘**：支持发送任意指标，自动生成可定制的仪表盘。
- 🔍 **日志搜索与过滤**：全文搜索日志，支持属性过滤和保存查询，无需 SSH。
- 📡 **实时日志流**：实时查看所有服务的日志行，无需刷新或轮询。
- 🧩 **追踪链接日志**：点击错误即可看到相关的日志行，自动关联时间戳。
- 🚨 **基于日志的告警**：根据日志模式设置告警，提前发现问题。
- 🤖 **AI 集成**：通过 MCP 服务器连接 Claude、Cursor 等 AI 工具，自动生成修复代码。
- 🚢 **部署追踪**：标记每次部署，关联错误，快速定位导致问题的版本。
- 💻 **多语言支持**：支持 Ruby、Python、Elixir、Node.js、PHP、Go、Java、Rust 等语言。
- 💰 **透明定价**：起价$0，无隐藏费用，支持峰值宽恕，不丢数据。
- 🌍 **合规与支持**：ISO/GDPR 合规，欧盟数据存储，真人开发者支持。

---

### [JavaScript 仍然无法发布全栈模块 | Wasp](https://wasp.sh/blog/2026/06/22/javascript-still-cant-ship-a-full-stack-module)

**原文标题**: [JavaScript still can't ship a full-stack module | Wasp](https://wasp.sh/blog/2026/06/22/javascript-still-cant-ship-a-full-stack-module)

JavaScript 仍然无法提供全栈模块

- 📦 全栈模块（Full-Stack Modules）是一种可复用的垂直功能切片，包含前端、后端、数据库模型和 webhook，安装后即可直接使用，无需手动接线。
- 💳 以支付功能为例，传统方式需要手动整合 Stripe SDK、UI 库和数据库，而全栈模块能一次性提供完整实现，省去繁琐的集成工作。
- 🤖 LLM（如 GPT）和开发者都喜欢“乐高式”的预制模块，因为它们能加速开发、提高安全性，并减少自定义代码带来的风险。
- 🧩 全栈模块本质上是“深层模块”（deep modules），对外提供简洁接口，内部隐藏复杂实现，便于 AI 和人类使用。
- 🌐 在 Rails、Laravel 等框架中，全栈模块已成熟，而 JavaScript 生态因缺乏统一的全栈层（客户端、服务器、数据库），无法标准化“胶水代码”（glue code）。
- 🔧 Wasp 框架通过 TypeScript 规范文件（spec file）统一管理路由、查询、操作等“胶水代码”，并支持将 React/Node.js 代码与规范打包为 npm 包，实现全栈模块。
- 📋 示例：安装`@acme/stripe-payments/spec`后，只需几行配置即可自动获得支付页面、操作和 webhook 端点，无需手动编写集成代码。
- 🚀 全栈模块可灵活定制：支持 fork、重写或暴露底层接口，适合企业内部复用，也可用于构建可插拔的开源 SaaS 启动模板（如 Open SaaS）。
- 🎯 Wasp 的目标是建立全栈模块注册中心，让开发者像安装普通 npm 包一样安装完整功能，提升开发效率和 AI 协作体验。

---

### [2026 年 WebAssembly 运行时的性能表现 - Frank DENIS 的随想](https://00f.net/2026/06/23/webassembly-runtimes-2026/)

**原文标题**: [Performance of WebAssembly runtimes in 2026 - Frank DENIS random thoughts.](https://00f.net/2026/06/23/webassembly-runtimes-2026/)

以下是對 2026 年 WebAssembly 運行時性能測試文章的總結：

WebAssembly 運行時在 2026 年持續進步，但效能差異仍取決於運行時選擇與功能支援，特別是 `wide_arithmetic` 指令對加密工作負載有顯著提升。

- 🚀 **Wasmer 表現最佳**，尤其在支援 `wide_arithmetic` 後，效能可達原生 1.33 倍，為 2026 年完整測試中最快結果。
- ⚡ **WAVM、WAMR 和 Wasmtime 緊追在後**，其中 WAVM 的優化器最強，能從基本 WebAssembly 生成極快程式碼。
- 📈 **Wasmtime 穩定進步**，每年效能提升，2026 年基準測試為原生 2.41 倍，加入 `wide_arithmetic` 後降至 1.46 倍。
- 🔥 **Bun 大幅躍進**，2026 年效能比 2025 年快約三倍，但仍有進步空間（8.77 倍原生）。
- 🛠️ **`wide_arithmetic` 是關鍵功能**，僅 Wasmtime 和 Wasmer 支援，能將加密運算效能從「不錯」提升至「接近原生」。
- 📊 **各運行時表現不一**：Node 緩慢改善、Wazero 持平、WAMR 穩定在 1.4-1.6 倍原生、wasm2c 持續可靠。
- ⚠️ **WasmEdge 需強制 AOT 模式**，否則預設直譯模式會導致效能災難（2026 年 AOT 下為 1.74 倍原生）。
- ❌ **部分運行時有相容性問題**，如 WAMR 2.1.0 無法編譯模組，Node 22.3.0 需調整記憶體設定才能執行。
- 💡 **結論：WebAssembly 效能取決於運行時、版本、功能支援與部署方式**，建議針對實際工作負載進行基準測試。

---

### [介绍 eve - Vercel](https://vercel.com/blog/introducing-eve)

**原文标题**: [Introducing eve - Vercel](https://vercel.com/blog/introducing-eve)

eve 是一个开源代理框架，旨在简化代理的构建、运行和扩展过程，让开发者专注于定义代理行为，而无需处理生产环境中的基础设施问题。

- 🚀 **生产就绪**：内置持久执行、沙箱计算、人工审批、子代理和评估功能，无需额外配置。
- 📁 **目录即代理**：代理结构清晰，通过文件树定义模型、指令、工具、技能、子代理、渠道和计划，一目了然。
- ⚡ **快速创建**：只需定义 `agent.ts` 和 `instructions.md` 文件，即可在几分钟内启动一个代理。
- 🔧 **电池齐全**：提供持久会话、沙箱隔离、人工审批、安全连接（支持 MCP 和 OAuth）、多渠道适配（Slack、Discord 等）和内置追踪评估。
- 🧩 **按文件扩展**：工具和技能以独立文件添加，eve 自动集成，无需样板代码。
- 🛠️ **本地开发与测试**：通过 `eve dev` 启动本地服务器，提供终端 UI 实时查看代理行为，并支持评估测试。
- 🌐 **一键部署**：作为普通 Vercel 项目部署，无需额外基础设施，代理在部署期间不中断。
- 🤖 **实际应用**：Vercel 内部运行超过 100 个代理，涵盖数据分析、销售、支持、内容生成和路由等领域，显著提升效率。
- 🎯 **入门简单**：通过 `npx eve@latest init` 命令，一分钟内创建第一个代理，并支持编码代理自动搭建。

---

### [eve – 智能体框架 - Vercel](https://vercel.com/eve)

**原文标题**: [eve – The Agent Framework - Vercel](https://vercel.com/eve)

Eve 是一个用于构建 AI 代理的框架，类似于 Next.js 对 Web 应用的作用，它使用 Markdown、TypeScript 和 Vercel 基础设施来创建可持久运行、多渠道部署的生产级代理。

- 🤖 **代理即目录**：代理是一个包含`instructions.md`、`agent.ts`、`tools/`等文件的目录，框架会将其编译并连接渠道。
- 📝 **从指令开始**：在`instructions.md`中用 Markdown 描述代理角色，即可运行一个完整的代理。
- ⚙️ **选择模型**：通过`agent.ts`配置文件选择 AI 模型（如`openai/gpt-5.4-mini`），默认使用 Eve 内置模型。
- 🧠 **可复用技能**：`skills/`目录中的 Markdown 剧本可在相关时加载，提供针对性指导而不增加提示负担。
- 🛠️ **TypeScript 工具**：在`tools/`中添加 TypeScript 文件，文件名自动成为工具名，无需注册。
- 🏖️ **自定义沙箱**：`sandbox/`提供隔离的执行环境，可配置后端（如 Vercel Sandbox）。
- 🔗 **多渠道连接**：通过`channels/`文件，同一代理可部署到 Slack、Discord、Teams、Web 等渠道。
- 🔐 **集成认证**：`connections/`处理 GitHub、Stripe 等服务的认证，工具调用无需管理令牌。
- 👨‍👩‍👧 **子代理委托**：`subagents/`允许主代理将专业任务委托给子代理，并合并结果。
- ⏰ **定时运行**：`schedules/`支持按 Cron 表达式自动运行代理，如每日报告。
- 💪 **持久化执行**：工作流可抵御崩溃和重启，每一步都检查点保存，代理在等待时暂停，收到消息后恢复。
- 🖥️ **沙箱计算**：代理在隔离的 VM 中运行，支持文件系统、bash 执行和代码运行，完全隔离。
- 🌐 **多渠道交付**：同一代理代码库可部署到 Web 聊天、Slack、API、Cron、CLI 等多种渠道。
- 👤 **人工介入**：需要确认的工具会触发审批门，会话暂停直到解决，然后无缝恢复。
- 🧪 **评估测试**：可定义测试套件和评分标准，每次部署和定时运行评估。

---

### [TypeScript 7.0 RC 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

**原文标题**: [Announcing TypeScript 7.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

TypeScript 7.0 RC 发布，基于 Go 重写，速度提升约 10 倍，兼容 6.0 语法，带来全新并行化架构与编辑器体验。

- 🚀 核心性能飞跃：代码库从 TypeScript 移植到 Go，利用原生速度和共享内存并行，编译速度比 6.0 快约 10 倍。
- 🧪 高度兼容与稳定：类型检查逻辑与 6.0 结构一致，通过十年积累的测试套件，已在微软内外数百万行代码库中验证。
- 📦 安装与试用：可通过`npm install -D typescript@rc`安装，VS Code 用户可安装“TypeScript Native Preview”扩展体验。
- 🔄 并行化控制：新增`--checkers`（默认 4）和`--builders`标志，分别控制类型检查和项目构建的并行度，支持单线程模式`--singleThreaded`。
- 👁️ 改进的`--watch`模式：基于 Parcel 文件监听器移植到 Go，跨平台稳定高效，大幅降低资源消耗。
- 📋 6.0 新默认值：`strict`默认 true，`module`默认`esnext`，`target`默认当前稳定 ES 版本，`rootDir`默认`./`，`types`默认`[]`等，需注意配置调整。
- 🚫 废弃功能硬错误：`target: es5`、`downlevelIteration`、`moduleResolution: node`等不再支持，需迁移到`nodenext`或`bundler`。
- 🔤 模板字面量类型改进：Unicode 码点按字符而非 UTF-16 代理对拆分，更符合直觉。
- 🛠️ JavaScript 支持重构：与`.ts`文件分析更一致，废弃`@enum`、`@class`等非标准 JSDoc 模式。
- ⚡ 编辑器体验增强：基于 LSP，支持多线程请求，新增语义高亮、排序导入、移除未用导入等功能，命令失败率降低 20 倍以上。
- 🗓️ 发布计划：RC 已可用，预计一个月内发布正式版，7.1 将提供稳定程序化 API。

---

### [访问控制 | 访问控制](https://onury.io/accesscontrol/)

**原文标题**: [AccessControl | AccessControl](https://onury.io/accesscontrol/)

本工具是一个基于角色与属性的 Node.js 访问控制库，提供链式 API 和策略引擎，支持 RBAC+ABAC 混合模型，具备安全审计、条件判断和自定义操作等特性。

- 🔐 支持 RBAC+ABAC 混合模型：将层级角色继承与基于属性的规则结合，实现经典访问控制模型的统一。
- 🛡️ 强化所有权与组管理：通过`own`验证记录归属，支持角色组和资源类别实现批量访问控制。
- ⚡ 自定义操作与门控：使用`.action()`/`.do()`扩展 CRUD 操作，通过`require()`添加强制性访问限制。
- 🔍 条件判断与异步检查：利用`.where()`附加条件（比较、CIDR、时间窗口等），支持自定义/异步逻辑解析。
- 🚨 安全加固与故障闭合：`tryCan()`不抛出异常，防范原型污染，支持可选的 ReDoS 防护正则，错误信息脱敏。
- 📊 事件审计与监控：每次决策触发`access`事件（含授权/拒绝原因），提供`change`和`error`钩子用于完整审计追踪。
- 🧩 简洁的 API 示例：通过`grant()`、`readOwn()`、`where()`等链式调用快速实现复杂权限控制。

---

### [AccessControl v3 新特性 | 访问控制](https://onury.io/accesscontrol/whats-new/)

**原文标题**: [What's New in AccessControl v3 | AccessControl](https://onury.io/accesscontrol/whats-new/)

AccessControl v3 引入了强大的策略引擎，在保持友好链式 API 的同时，新增了条件判断、所有权强制、自定义操作、拒绝覆盖、强制限制门、角色组/资源分类、异步检查及审计事件流等核心功能。

- 🔐 **条件判断 (ABAC)** — 通过 `.where()` 方法为授权添加声明式条件，支持丰富的运算符（如 `==`、`in`、`matches`、`before/after/between` 等），并可结合 `{ and, or, not }` 逻辑组合，实现基于属性的访问控制。
- 👤 **强制所有权验证** — v3 自动验证资源所有权，通过配置 `ownerField` 或自定义 `owner` 解析器，确保 `own` 权限仅在记录真正属于请求者时生效，默认 `strict.checks` 开启，安全优先。
- 🎯 **自定义操作** — 不再局限于 CRUD，通过 `.action()` 或 `.do()` 可定义任意名称的操作（如 `publish`），并支持所有权和条件机制。
- 🚫 **拒绝覆盖解析** — `deny` 始终优先于 `grant`，包括继承的授权，且 `deny` 不会跨所有权传播（如 `deny create:any` 不影响 `create:own`）。
- 🛑 **强制限制门 (require)** — 通过 `.require()` 设置独立限制门，只有所有门通过且存在匹配授权时，检查才通过，且限制门不会扩大访问权限。
- 📂 **角色组与资源分类** — 通过 `setup()` 声明角色组和资源分类，可批量授权，并支持动态继承，避免命名冲突。
- ⚡ **异步检查与自定义函数** — 注册业务逻辑函数，通过 `{ fn, args }` 引用，支持异步检查，使用 `grantedAsync` / `checkAsync` 方法。
- 📊 **事件与审计钩子** — 内置无依赖的事件发射器，`access` 事件记录每次检查（含拒绝原因），`change` 跟踪策略变更，`error` 报告错误，监听器隔离，不影响检查流程。
- 🧩 **三桶模型与序列化** — 构造函数接受 `grants`、`engine`、`policy`、`context` 四个参数，分别管理库机制、领域模型和上下文数据。新增 `snapshot()` / `restore()` 方法一键序列化/反序列化完整策略。
- 🛡️ **生产环境强化** — 提供 `tryCan()` 方法实现故障关闭；防止原型污染；正则匹配默认关闭并防 ReDoS；错误代码稳定且消息可安全显示；字符集默认 ASCII 防同形字攻击。

---

### [GitHub - onury/accesscontrol：基于角色和属性的Node.js访问控制](https://github.com/onury/accesscontrol)

**原文标题**: [GitHub - onury/accesscontrol: Role and Attribute based Access Control for Node.js · GitHub](https://github.com/onury/accesscontrol)

这是一个基于 Node.js 的角色与属性混合访问控制库，融合了 RBAC 和 ABAC 的优点，提供链式 API、条件策略、所有权验证、自定义操作和审计事件。

- 🔐 **核心功能** — 支持角色层级继承（拒绝优先）、条件策略（`.where()`）、强制所有权验证（`own`）、自定义操作（`.action()`/`.do()`）和全局/分类/资源级别的 `require()` 门控。
- 📦 **安装与快速使用** — 通过 `npm i accesscontrol` 安装，使用 `grant()` 定义角色权限，`can()` 检查权限，支持 CRUD 快捷方法和属性过滤。
- 🧩 **角色与继承** — 使用 `extend()` 继承角色权限，`deny()` 始终覆盖继承的权限，但拒绝不跨所有权传播（如 `deny create:any` 不影响 `create:own`）。
- 🛠️ **资源与属性过滤** — 支持 glob 模式（含否定和嵌套路径），`filter()` 方法返回仅包含允许字段的数据副本。
- 📋 **条件与门控** — 使用 `.where()` 附加条件（支持比较、包含、正则等运算符），`.require()` 作为独立门控，条件缺失时默认拒绝（失败关闭）。
- 👥 **组与分类** — 通过 `setup()` 定义角色组和资源分类，支持批量授权和继承，避免命名冲突。
- 🔒 **安全与质量** — 100% 测试覆盖率、变异测试、防原型污染、正则拒绝服务防护、安全错误信息（默认隐藏敏感数据）、同形字攻击防护。
- ⚡ **异步与事件** — 支持自定义异步条件函数（`defineCondition`、`grantedAsync`），提供 `access`（审计）、`change` 和 `error` 事件流。
- 🗄️ **序列化与持久化** — 支持将权限模型导出为数据库友好的行格式或 JSON 快照，并通过构造函数或 `restore()` 恢复。

---

### [GitHub - tuananh/camaro: camaro 是一个 Node.js 库，可将 XML 转换为 JSON，使用 Node.js 绑定到原生 XML 解析器 pugixml，这是目前最快的 XML 解析器之一。](https://github.com/tuananh/camaro)

**原文标题**: [GitHub - tuananh/camaro: camaro is a Node.js library that transform XML to JSON, using Node.js binding to native XML parser pugixml, one of the fastest XML parser around. · GitHub](https://github.com/tuananh/camaro)

camaro 是一个基于 Node.js 的 XML 转 JSON 库，利用 WebAssembly 和原生解析器 pugixml 实现高性能转换，支持自定义模板和 XPath 语法。

- ⚡ **高性能**：比 txml 快 1.99 倍，比 xml2js 快 14.52 倍，适合处理大型 XML 数据。
- 🛠️ **自定义模板**：支持 XPath 和扩展函数（如 title-case、number、boolean），仅提取所需字段。
- 🌐 **跨平台兼容**：基于 WebAssembly 编译，无需重新编译，支持 Linux、macOS 和 Windows。
- 🔄 **多核扩展**：利用 worker_threads 池，在多核处理器上表现优异。
- 📦 **安装简单**：通过 `pnpm add camaro` 或 `npm install camaro` 即可使用。
- 📝 **使用示例**：提供直观的模板语法，如 `['players/player', { name: 'title-case(name)' }]`，输出 JSON 对象。
- 🏆 **基准测试**：针对实际 API 响应（如 Expedia XML）进行优化，但小 XML 性能可能不如纯 JS 实现。
- 📚 **文档丰富**：包含 API.md、示例文件夹和博客教程，便于上手。
- 🔗 **社区应用**：被多个项目（如 hexo-generator-sitemap、Academic Bloggers Toolkit）采用。
- 📜 **开源许可**：MIT 许可证，允许自由使用和修改。

---

### [pugixml.org - 首页](https://pugixml.org/)

**原文标题**: [pugixml.org - Home](https://pugixml.org/)

pugixml 是一个轻量、快速且易用的 C++ XML 解析库，支持 XPath，并提供丰富的文档和下载选项。

- 📦 提供 DOM 接口，支持遍历和修改 XML 树结构
- ⚡ 解析速度极快，可从文件或缓冲区构建 DOM 树
- 🔍 内置 XPath 1.0 实现，支持复杂数据查询
- 🌐 完整 Unicode 支持，包括多种接口变体和自动编码转换
- 🧩 高度可移植，易于集成，提供多种下载和安装方式（Windows/Unix 压缩包、Git/Subversion、Linux/BSD 包管理器、Homebrew、MacPorts、NuGet、Conda）
- 📜 基于 MIT 许可证，完全免费，适用于开源和商业项目
- 🗓️ 自 2006 年持续开发维护，拥有众多用户，最新版本为 1.16（2026 年发布）

---

### [GitHub - tediousjs/tedious: 用于连接 SQL Server 数据库的 Node TDS 模块。](https://github.com/tediousjs/tedious)

**原文标题**: [GitHub - tediousjs/tedious: Node TDS module for connecting to SQL Server databases. · GitHub](https://github.com/tediousjs/tedious)

Tedious 是一个纯 JavaScript 实现的 TDS 协议库，用于连接 Microsoft SQL Server 数据库。

- 📚 核心功能：纯 JavaScript 实现 TDS 协议，用于连接 SQL Server 数据库实例，支持 TDS 7.1 至 7.4 版本（覆盖 SQL Server 2000 至 2022）
- 🛠️ 安装简单：通过 `npm install tedious` 即可安装，需先安装 Node.js
- 📖 文档丰富：提供详细文档和代码示例，访问 tediousjs.github.io/tedious/ 获取更多信息
- 🆕 版本更新：自 1.11.0 版本起，新列默认可空；1.2 版本起默认登录行为有所调整
- 🤝 开源贡献：采用 MIT 许可证，欢迎社区贡献代码和提交 Pull Request
- 📊 项目概况：拥有 1.6k Star、443 Fork、226 个版本发布，主要使用 TypeScript（95.2%）和 JavaScript（4.8%）开发

---

### [GitHub - tediousjs/node-mssql: 适用于 Node.js 的 Microsoft SQL Server 客户端 · GitHub](https://github.com/tediousjs/node-mssql)

**原文标题**: [GitHub - tediousjs/node-mssql: Microsoft SQL Server client for Node.js · GitHub](https://github.com/tediousjs/node-mssql)

node-mssql 是 Node.js 的 Microsoft SQL Server 客户端，支持 Tedious（默认）和 MSNodeSQLv8 两种驱动，提供连接池、查询、事务、预处理语句等功能，并内置 SQL 注入防护。

- 📦 **安装与驱动**：默认安装 `npm install mssql` 使用 Tedious 驱动，可选安装 `msnodesqlv8` 支持 Windows 认证。
- 🔗 **连接方式**：支持连接字符串或配置对象，示例包括本地连接、Azure 加密连接及 Windows 认证。
- 🧩 **核心功能**：提供 `query`、`batch`、`execute`、`bulk` 等方法，支持流式处理大结果集。
- 🔄 **连接池管理**：全局连接池和自定义池管理，支持 `validateConnection` 选项（`true`、`'socket'`、`false`）确保连接健康。
- 📊 **数据操作**：支持输入/输出参数、预处理语句、事务（含隔离级别）、表值参数（TVP）和批量插入。
- 🛡️ **安全特性**：使用参数化查询或模板字面量防止 SQL 注入，自动将 `undefined`/`NaN` 转为 `null`。
- 📈 **高级功能**：支持 JSON 解析、地理空间数据、重复列名处理（`arrayRowMode`）、以及通过 `diagnostics_channel` 进行遥测。
- ❌ **错误处理**：定义 `ConnectionError`、`TransactionError`、`RequestError`、`PreparedStatementError` 类型，并提供详细 SQL 错误信息。
- 🛠️ **CLI 工具**：全局安装后可通过命令行执行查询，支持配置文件覆盖。
- 📋 **版本迁移**：提供从 3.x 到 12.x 的变更说明，如 `encrypt` 默认改为 `true`、移除旧驱动支持等。

---

### [GitHub - TimelordUK/node-sqlserver-v8：从node-sqlserver分支而来，兼容所有Node版本的SQL Server 驱动程序 · GitHub](https://github.com/TimelordUK/node-sqlserver-v8)

**原文标题**: [GitHub - TimelordUK/node-sqlserver-v8: branched from node-sqlserver, SQL server driver compatible with all versions of Node · GitHub](https://github.com/TimelordUK/node-sqlserver-v8)

msnodesqlv8 是一个用于 Node.js 和 Electron 的原生 ODBC 驱动，支持 SQL Server 和 Sybase ASE，提供高性能数据操作和丰富的功能集。

- 🚀 **高性能**：通过 BCP 和批量插入实现高达 131k 行/秒的吞吐量，经 SQL Server 2022 验证。
- 📦 **跨平台支持**：为 Linux、macOS 和 Windows 提供预编译二进制文件，支持 Node 20/22/24 和 Electron 32+。
- 🔧 **安装简便**：通过 `npm install msnodesqlv8` 安装，自动下载预编译二进制，需搭配 Microsoft ODBC 驱动 17 或 18。
- ⚡ **快速入门**：提供简洁的 API 进行连接、查询和参数化插入，支持 Promise 和回调模式。
- 📊 **丰富功能**：支持流式结果、存储过程、表值参数、批量插入、BCP、连接池、预编译语句和事务。
- 🛠️ **故障排除**：针对常见问题（如驱动程序未找到、SSL 错误、段错误）提供解决方案，并链接到 GitHub Issues。
- 📚 **完整资源**：包含 Wiki API 参考、示例代码、测试套件和独立应用示例（如 Next.js、Electron、React）。
- 📜 **许可**：基于 Apache 2.0 许可证开源，提供贡献指南。

---

### [GitHub - runk/node-chardet: NodeJS 字符编码检测工具](https://github.com/runk/node-chardet)

**原文标题**: [GitHub - runk/node-chardet: Character encoding detection tool for NodeJS · GitHub](https://github.com/runk/node-chardet)

chardet 是一个纯 JavaScript/TypeScript 编写的字符编码检测模块，体积小巧（仅 22KB），无依赖，跨平台运行，通过频率分析确定最可能的编码。

- 📦 轻量无依赖：打包后仅 22KB，无需原生代码或绑定，100% TypeScript 编写
- 🌐 全环境兼容：支持 Node.js、浏览器及原生环境，可在 Linux/Mac/Windows 上运行
- 🔍 核心功能：提供 `detect()` 返回最高置信度编码，`analyse()` 返回排序后的编码列表
- ⚡ 大文件优化：支持采样前 N 字节和偏移量读取，平衡性能与准确性
- ⚠️ 字符串限制：输入需为 Buffer 或 Uint8Array，不能直接使用字符串（JavaScript 字符串默认 UTF-16）
- 📋 编码支持：涵盖 ASCII、UTF-8/16/32、ISO-8859 系列、Big5、GB18030 等 30 余种编码
- 📚 待完善编码：计划支持 KOI8-U、IBM866、CP949 等更多编码
- 🛠 开发状态：GitHub 仓库 309 星，30 个复刻，已发布 23 个版本（最新 v2.2.0）

---

### [GitHub - runk/node-chardet: NodeJS 字符编码检测工具](https://github.com/runk/node-chardet#supported-encodings)

**原文标题**: [GitHub - runk/node-chardet: Character encoding detection tool for NodeJS · GitHub](https://github.com/runk/node-chardet#supported-encodings)

这是一个纯 JavaScript/TypeScript 编写的字符编码检测模块，通过出现频率分析确定最可能的编码，体积小巧且无依赖。

- 📦 包体积仅 22 KB，纯 JavaScript/TypeScript 编写，无任何外部依赖
- 🌐 支持 Node.js、浏览器及原生环境，兼容 Linux/Mac/Windows 平台
- 🔍 提供 `detect()` 返回最高置信度编码，`analyse()` 返回按置信度排序的编码列表
- ⚡ 支持大数据集优化：可通过 `sampleSize` 和 `offset` 参数采样分析，平衡性能与准确性
- ⚠️ 注意：输入需为 Buffer 或 Uint8Array 原始数据，不能直接使用已转换为 UTF-16 的字符串
- 📋 支持 30+ 种编码，包括 ASCII、UTF-8/16/32、ISO-8859 系列、GB18030、Shift_JIS 等
- ✅ 100% TypeScript 编写，类型定义已包含，测试覆盖率高
- 🔧 提供同步 (`detectFileSync`) 和异步 (`detectFile`) 文件检测接口
- 🚀 项目活跃：309 星、30 个复刻、23 个发布版本，支持 Hacktoberfest

---

### [发布 v2.0.0 · jshttp/cookie · GitHub](https://github.com/jshttp/cookie/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · jshttp/cookie · GitHub](https://github.com/jshttp/cookie/releases/tag/v2.0.0)

概述摘要  
- 📦 jshttp/cookie 库发布 v2.0.0 版本，主要迁移至 ESM 模块系统  
- ⚠️ 重要变更：仅支持 ESM（Node 22+ 可用 require(esm)），不再支持旧版 Node  
- 🔄 方法重命名：`parse` → `parseCookie`，`stringify` → `stringifySetCookie`  
- 🚫 弃用旧代码路径：`stringifySetCookie` 仅支持对象模式（如 `{ name: "", value: "" }`）  
- ⚡ 性能优化：更快的 cookie 序列化与编码处理  
- 🛠 修复问题：对空 cookie 值应用编码，省略跳过值时的前导分号  
- 🔐 发布签名：由 Blake Embrey 使用已验证的 SSH 密钥签署提交

---

### [终极 PaaS 定价对比计算器](https://judoscale.com/tools/paas-pricing-calculator?utm_source=node-weekly&utm_medium=newsletter&utm_campaign=calculator&utm_content=paas-alternatives-head-to-head)

**原文标题**: [The Ultimate PaaS Pricing Comparison Calculator](https://judoscale.com/tools/paas-pricing-calculator?utm_source=node-weekly&utm_medium=newsletter&utm_campaign=calculator&utm_content=paas-alternatives-head-to-head)

### 概览摘要
该内容为 PaaS 定价计算器指南，对比不同云平台（Heroku、Render、Railway、Fly、AWS ECS Fargate）的成本与特性，强调通过水平扩展和自动扩缩容节省开支。

- 📊 **核心计算维度**：基于 CPU 核心数、内存、实例数、月度出站流量及团队规模进行月度成本估算。
- 💡 **成本优化建议**：建议从单 CPU 核心和 1GB 内存起步，优先水平扩展（增加实例），并利用自动扩缩容（如 Judoscale）可节省 33% 以上费用。
- ⚙️ **各平台特性差异**：
  - Heroku：无出站费用，但共享 CPU 性能不稳定，团队超 25 人需企业合同。
  - Render：按团队成员收费，出站有免费额度，但超限后按 GB 计费。
  - Railway：纯按用量计费（无固定层级），闲置 CPU/内存不收费，无团队费用。
  - Fly：多区域定价不同（示例用芝加哥），共享 CPU 有时间切片，出站按区域收费。
  - AWS ECS Fargate：按 vCPU 秒和 GB 秒计费，提供 100GB/月免费出站，无团队费用。
- 🚀 **关键提醒**：出站流量易被低估，建议通过 RPS×页面大小×2.5 估算；选择平台时需综合计算成本、团队规模及扩展灵活性。

---

### [GitHub - Agent-Field/agentfield: 像 API 和微服务一样构建、运行和扩展 AI 智能体——从第一天起就具备可观察、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平面，能将 AI 智能体构建为可调用的 API，并提供生产级基础设施支持。

- 🤖 **核心概念**：将 AI 智能体像 API 一样构建、部署和扩展，支持 Python、Go、TypeScript 编写智能体逻辑，自动转为 REST 端点。
- ⚡ **一键部署**：通过 `/agentfield` 指令在编码助手（如 Claude Code）中描述系统，即可获得生产就绪的多智能体后端。
- 🧩 **开发体验**：提供最简抽象，无 DSL/YAML，使用 `@app.reasoner()`、`app.ai()`、`app.pause()`、`app.call()` 等原生模式。
- 🔄 **执行引擎**：支持同步/异步执行、Webhook、SSE 流式传输、无超时限制、自动重试和背压管理。
- 🧠 **内存系统**：提供全局、智能体、会话、运行四种作用域的 KV 存储和向量搜索，无需 Redis。
- 👤 **人机协作**：`app.pause()` 支持持久化暂停/恢复，用于人工审批，崩溃安全且可审计。
- 🚦 **灰度部署**：支持金丝雀发布、A/B 测试、蓝绿部署，按流量权重路由版本。
- 🔐 **身份与治理**：每个智能体拥有 W3C DID 加密身份，支持可验证凭证、标签策略和加密签名请求。
- 📊 **可观测性**：自动生成工作流 DAG 图、Prometheus 指标、结构化日志和执行时间线。
- 🏗️ **架构**：控制平面为无状态 Go 服务，智能体可从任何地方连接，支持 Docker、Kubernetes 部署。

---

### [面向 AI 代理的临时 Cloudflare 账户](https://blog.cloudflare.com/temporary-accounts/)

**原文标题**: [Temporary Cloudflare Accounts for AI agents](https://blog.cloudflare.com/temporary-accounts/)

Cloudflare 推出 AI 智能体临时账户，让智能体无需注册即可直接部署代码，部署内容在 60 分钟内有效，可随时认领为永久账户。

- 🤖 临时账户专为 AI 智能体设计，解决传统注册流程（如 OAuth、复制粘贴 API 令牌、多因素认证）对智能体的阻碍。
- ⚡ 智能体只需执行 `wrangler deploy --temporary`，即可快速部署 Worker，无需人工干预，部署后自动获得预览链接并验证结果。
- 🔄 智能体可在 60 分钟内多次迭代代码并重新部署，支持试错循环（写代码 → 部署 → 验证）。
- 🏠 用户可随时通过认领链接将临时账户转为永久账户，包括 Worker、数据库及其他绑定资源。
- 🧠 Wrangler 会自动提示智能体使用 `--temporary` 标志，无需人类明确告知，智能体即可发现并利用该功能。
- 🔗 Cloudflare 正通过多方合作（如 Stripe、WorkOS 的 auth.md）消除智能体注册障碍，推动无摩擦部署生态。

---

### [Node.js 兼容性 · Cloudflare Workers 文档](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)

**原文标题**: [Node.js compatibility Â· Cloudflare Workers docs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)

Cloudflare Workers 支援部分 Node.js API，透過內建實作與 polyfill 確保相容性。

- 🛠️ 啟用 `nodejs_compat` 相容性標誌與 2024-09-23 後的日期，即可使用內建 Node.js API 與 polyfill。
- ✅ 多數 API 如 Buffer、Crypto、HTTP、Stream、Path、URL 等已原生完整支援。
- ⚠️ 部分 API 如 Async Hooks、Child Processes、HTTP/2 僅部分支援或為非功能樁。
- ❌ SQLite 與 Test Runner 目前尚未支援。
- 📦 未支援的 API 透過 Wrangler 與 unenv 自動注入 polyfill，呼叫時會拋出錯誤訊息。
- 🔧 可僅啟用 `nodejs_als` 標誌來單獨啟用 AsyncLocalStorage。

---

### [Jarred-Sumner 提出的 JavaScriptCore 共享内存线程（实验性，尚未生效）· 拉取请求 #249 · oven-sh/WebKit · GitHub](https://github.com/oven-sh/WebKit/pull/249)

**原文标题**: [Shared-memory threads for JavaScriptCore (experimental, not working yet) by Jarred-Sumner · Pull Request #249 · oven-sh/WebKit · GitHub](https://github.com/oven-sh/WebKit/pull/249)

这是一个为 JavaScriptCore 添加共享内存线程支持的实验性 Pull Request，旨在让 JavaScript 实现真正的多线程并行，而无需依赖 Worker 的消息传递或 SharedArrayBuffer。

- 🧵 **真正的共享内存线程**：`new Thread(fn)` 在另一个核心上运行函数，共享同一个堆和对象，无需结构化克隆或消息传递。
- 🚀 **简洁的 API**：`new Thread(fn, args).join()` 直接返回结果或抛出异常，闭包可捕获变量，无需字符串化或 Blob URL。
- ⚡ **并行映射与共享缓存**：可直接在共享数组上并行操作，或使用共享的 `Map` 和 `Lock` 实现线程安全的缓存，无需手动序列化。
- 🛑 **取消与进度**：通过共享布尔值实现线程取消，或直接读取共享属性获取实时进度，无需事件协议。
- 🔒 **完整的同步原语**：提供 `Lock`、`Condition`、`ThreadLocal`，并将 `Atomics.*` 扩展到普通对象属性，支持 `wait`/`notify`。
- 🧠 **共享模块图**：线程共享同一个 realm 和已执行的模块图，避免了 Worker 重复加载和解析的开销。
- 📊 **性能与开销**：不共享对象的代码几乎零开销（最坏情况串行回归 0.45%），共享对象的写入会变慢，但设计目标是近线性扩展。
- 🛠️ **复杂性与状态**：这是一个大型改动（约 6 万行 diff），修改了对象模型、所有 JIT 层、GC 和 VM 生命周期。目前测试套件通过，但尚未完成模糊测试和长期稳定性验证，可能永远不会合并。

---

### [工作线程 | Node.js v26.4.0 文档](https://nodejs.org/api/worker_threads.html#worker-threads)

**原文标题**: [Worker threads | Node.js v26.4.0 Documentation](https://nodejs.org/api/worker_threads.html#worker-threads)

Node.js 的 `worker_threads` 模块支持在独立线程中并行执行 JavaScript，适用于 CPU 密集型任务，并能通过消息传递和共享内存（如 `ArrayBuffer`）实现线程间通信。

- 🧵 **Worker 线程**：通过 `Worker` 类创建，用于执行 CPU 密集型操作，不适用于 I/O 密集型任务；Node.js 内置异步 I/O 更高效。
- 🔄 **线程间通信**：使用 `MessagePort`、`MessageChannel` 和 `BroadcastChannel` 进行双向或一对多通信，支持结构化数据、内存区域和 `MessagePort` 的传输。
- 🧠 **内存共享**：支持通过 `ArrayBuffer` 或 `SharedArrayBuffer` 共享内存，但需谨慎处理 `TypedArray` 和 `Buffer` 的传输，避免导致其他视图不可用。
- 🔒 **锁机制**：`LockManager` 和 `Lock` 类提供跨线程资源协调，支持独占和共享锁模式，可设置超时和中断信号。
- 📦 **环境数据**：`setEnvironmentData()` 和 `getEnvironmentData()` 可在线程间传递克隆数据，`SHARE_ENV` 允许共享环境变量。
- 🛠️ **线程属性**：`isMainThread`、`threadId`、`threadName` 和 `workerData` 用于识别和传递初始化数据；`resourceLimits` 可设置 JS 引擎资源限制。
- 🚫 **不可传输/克隆标记**：`markAsUntransferable()` 和 `markAsUncloneable()` 防止对象被传输或克隆，适用于共享内存池等场景。
- 📊 **性能分析**：支持 `cpuUsage()`、`getHeapSnapshot()`、`getHeapStatistics()` 和 `eventLoopUtilization()` 方法，用于监控线程性能。
- ⚠️ **注意事项**：Worker 线程继承父进程的 CLI 标志（如 `-r` 预加载脚本），可能导致递归创建；`stdio` 输出可能被主线程同步代码阻塞。

---

### [更安全的 pull_request_target 默认设置用于 GitHub Actions 检出 - GitHub 更新日志](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)

**原文标题**: [Safer pull_request_target defaults for GitHub Actions checkout - GitHub Changelog](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)

overview summary
GitHub Actions 的 `actions/checkout` v7 版本现已发布，默认阻止常见的“pwn request”攻击模式，以增强 `pull_request_target` 事件的安全性。该变更旨在防止从 fork 拉取请求中执行恶意代码，并计划于 2026 年 7 月 16 日回溯至所有受支持的主要版本。

- 🛡️ **默认阻止不安全检出**：`actions/checkout` v7 在 `pull_request_target` 和 `workflow_run` 事件中，自动拒绝从 fork 拉取请求检出代码（如 `refs/pull/number/head` 或 `refs/pull/number/merge`）。
- 🔒 **聚焦常见漏洞**：此变更主要针对“pwn request”攻击，防止攻击者利用未审查的 fork 代码获取工作流完整权限。
- ⏳ **回溯计划**：2026 年 7 月 16 日，安全增强将回溯至 `actions/checkout@v4` 等主要版本标签，固定 SHA 或补丁版本需手动升级。
- ❌ **未覆盖范围**：不阻止其他事件类型（如 `issue_comment`）或检出第三方仓库的不安全操作，需额外审查。
- ✅ **选择退出机制**：若工作流需合法使用 fork 代码（如生成覆盖率报告），可通过添加 `allow-unsafe-pr-checkout` 输入选择退出，但需谨慎评估安全风险。

---

