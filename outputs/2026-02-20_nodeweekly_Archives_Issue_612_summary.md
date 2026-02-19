### [Node 周刊第 612 期：2026 年 2 月 19 日](https://nodeweekly.com/issues/612)

**原文标题**: [Node Weekly Issue 612: February 19, 2026](https://nodeweekly.com/issues/612)

本期内容涵盖了 Node.js 生态的最新动态，包括性能优化、新工具发布、安全增强及社区更新。

- 🐳 **Node.js 内存优化**：Cloudflare 等合作推出 node-caged Docker 镜像，通过 V8 指针压缩技术可降低 Node 25 约 50% 的内存使用，但需权衡性能影响。
- 🤖 **AI 代理开发课程**：Frontend Masters 推出详细视频课程，指导从零构建 AI 代理，涵盖工具调用、代理循环、评估及框架选择等内容。
- 📦 **npm v11.10.0 发布**：新增`--allow-git`标志（当前默认允许，未来版本可能限制），支持多包信任发布配置批量管理，并引入`--min-release-age`选项。
- ⚡ **Node.js 更新速览**：Node.js 25.6.1 和 24.13.1（LTS）版本发布；Temporal API 即将默认启用；单可执行应用（SEA）现支持 ESM 入口点。
- 🔒 **npm 安全增强**：npm 包页面新增 Socket 安全分析直链（如 express 包），帮助开发者快速评估依赖安全性。
- 📊 **运行时性能对比**：RepoFlow 团队发布 Node.js、Deno 与 Bun 的微基准测试结果，建议谨慎解读数据。
- 🛠️ **新工具与库**：包括嵌入式 SQL 数据库绑定@stoolap/node、网络模拟工具 fetch-network-simulator、DNS over HTTPS 工具 Tangerine，以及 pnpm、jsdom 等多项更新。
- 🌐 **生态动态**：Vercel 发布像素风格字体 Geist Pixel；Electrobun v1 支持基于 Bun 构建轻量桌面应用；Three.js 创作者尝试将《Descent》移植至浏览器；Deno 2.6.10 新增脚本编译安装功能。

---

### [获取失败](https://nodeweekly.com/link/180908/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/180908/web)

无法总结：获取内容失败，状态码 429。

---

### [AI 智能体 | 大型语言模型、工具调用与人机协同 | Frontend Masters](https://frontendmasters.com/courses/ai-agents-v2/?utm_source=email&utm_medium=nodeweekly&utm_content=aiagentsv2)

**原文标题**: [AI Agents | LLMs, Tool Calling, and Human-in-the-Loop | Frontend Masters](https://frontendmasters.com/courses/ai-agents-v2/?utm_source=email&utm_medium=nodeweekly&utm_content=aiagentsv2)

本课程由 Netflix 的 Scott Moss 主讲，系统性地教授如何从零开始构建 CLI 智能体，涵盖工具调用、智能体循环、评估等核心概念，并包含人工审批、上下文管理等高级主题。

- 🤖 课程从智能体基础讲起，包括工具调用和循环机制，并演示如何构建能执行 API 调用、文件操作等任务的智能体
- 📊 重点讲解评估方法，包括单轮与多轮评估，以及如何使用 Laminar 进行性能指标追踪和结果分析
- 🛠️ 详细展示文件系统工具、网络搜索工具的实现，并探讨上下文窗口管理与令牌使用监控策略
- ⚙️ 介绍代码执行与 Shell 工具的安全实践，强调沙箱环境的重要性以保障操作安全
- 👥 深入探讨人工介入与审批流程，包括同步与异步审批架构，以增强高风险操作的可靠性
- 🧠 课程最后总结了主流智能体开发框架，并推荐了进一步学习与部署的相关工具和平台

---

### [npm 批量可信发布配置与脚本安全性现已全面推出 - GitHub 更新日志](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/)

**原文标题**: [npm bulk trusted publishing config and script security now generally available - GitHub Changelog](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/)

npm CLI v11.10.0+ 发布两项新功能，旨在增强软件供应链安全性和配置管理效率。

- 🔄 **批量配置 OIDC 可信发布**：维护者现可通过 `npm trust` 命令一次性为多个软件包添加或更新可信发布配置，无需逐个操作。
- 🛡️ **新增 `--allow-git` 安装标志**：Git 依赖可能包含覆盖 git 执行路径的 `.npmrc` 文件，存在任意代码执行风险。该标志允许用户明确控制是否允许 Git 依赖，默认值为 `all` 以保持向后兼容，但建议立即使用 `--allow-git=none` 以提高安全性，并仅在必要时启用。
- ⏳ **未来默认值变更**：`--allow-git=none` 预计将在 npm CLI v12 中成为默认设置，进一步强化安装过程的安全基线。

---

### [feat: 由 wraithgar 添加 min-release-age · 拉取请求 #8965 · npm/cli · GitHub](https://github.com/npm/cli/pull/8965)

**原文标题**: [feat: add min-release-age by wraithgar · Pull Request #8965 · npm/cli · GitHub](https://github.com/npm/cli/pull/8965)

该内容描述了 npm CLI 仓库中一个关于新增 `min-release-age` 配置的合并请求（PR #8965），该功能允许用户通过相对天数来设置 `before` 配置，以限制安装包的发布日期。

- 🆕 新增 `min-release-age` 配置，可通过相对天数（如 `--min-release-age=30`）自动计算并设置 `before` 日期，限制安装包的发布日期范围
- 🤝 功能基于社区贡献（@kaezone 的 #8802 和 @PR3C14D0 的 #8825），经过多次代码推送和团队审核后合并
- ⚙️ 配置会确保 `--before` 和 `--min-release-age` 参数互斥，并将相对天数转换为 npm 可用的日期值
- 🚫 当前版本未包含包排除功能，开发者表示未来可能单独处理该需求
- 📅 与 pnpm 的类似功能（使用分钟为单位）不同，此功能以天为单位，与 Dependabot 的设计保持一致
- 🎉 该功能已随 npm 版本 11.10.0 发布，后续讨论中提出了添加包排除支持的议题（#8994）

---

### [Node.js — Node.js 25.6.1（当前版本）](https://nodejs.org/en/blog/release/v25.6.1)

**原文标题**: [Node.js — Node.js 25.6.1 (Current)](https://nodejs.org/en/blog/release/v25.6.1)

Node.js 25.6.1（Current）版本发布，包含多项依赖更新、性能优化、错误修复及文档改进，并提供了各平台的安装包和二进制文件下载链接。

- 🔄 依赖更新：将 cjs-module-lexer 替换为 merve，并升级了 npm、undici、minimatch 等多个核心依赖版本。
- 🐛 错误修复：解决了 Windows DNS SRV 查询的 ECONNREFUSED 问题，修复了模块解析钩子重复调用等 bug。
- ⚡ 性能优化：在 HTTP 头部解析中引入 slab 分配，优化 SQLite 大文本绑定和结构化克隆实现的内存使用。
- 📚 文档完善：更新了 EventEmitter 错误处理、测试运行器环境默认选项等说明，并修正了多处文档错误。
- 🛠️ 工具与测试：更新了构建工具链（如 Visual Studio 2026），修复了多个测试中的竞态条件和跨平台路径匹配问题。
- 🔗 发布文件：提供了 Windows、macOS、Linux 等多平台的安装程序和二进制文件，并附带了完整的 SHASUMS 校验和 PGP 签名。

---

### [Node.js — Node.js 24.13.1（长期支持版）](https://nodejs.org/en/blog/release/v24.13.1)

**原文标题**: [Node.js — Node.js 24.13.1 (LTS)](https://nodejs.org/en/blog/release/v24.13.1)

Node.js 24.13.1（LTS）版本发布，代号“Krypton”，包含多项功能更新、依赖升级、错误修复及性能改进。

- 🐍 **构建支持**：新增对 Python 3.14 的支持。
- 🚀 **功能稳定化**：将 `--heapsnapshot-near-heap-limit`、`--build-snapshot`、`--build-snapshot-config` 及 `v8.queryObjects()` 标记为稳定功能。
- 🔒 **安全更新**：根证书更新至 NSS 3.119，并修复了 TLS 相关安全问题（CVE-2025-59465、CVE-2026-21637）。
- 📦 **依赖升级**：升级了 OpenSSL、npm、SQLite、ICU、ADA 等多个核心依赖至新版本。
- 🛠️ **错误修复**：修复了断言、缓冲区、子进程、集群、HTTP/2、流等多个模块的问题。
- ⚡ **性能优化**：改进了断言、缓冲区、字符串编码等操作的性能。
- 📚 **文档完善**：更新了多项功能的文档，并新增了三位协作者（avivkeller、gurgunday、Renegade334）。
- 🔧 **工具与测试**：更新了构建工具，改进了测试框架，并修复了多个测试用例。

---

### [构建：默认启用 Temporal by richardlau · Pull Request #61806 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61806)

**原文标题**: [build: enable Temporal by default by richardlau · Pull Request #61806 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61806)

该内容是关于 Node.js 项目中一个名为“build: enable Temporal by default”的拉取请求（PR #61806），旨在默认启用 Temporal 支持，但需要 Rust 工具链（cargo 和 rustc）。PR 引入了自动检测机制，并讨论了相关构建配置和发布流程的潜在影响。

- 🛠️ 默认启用 Temporal 支持需依赖 Rust 工具链（cargo 和 rustc），这是新的构建要求。
- ⚙️ 新增`--v8-disable-temporal-support`选项以显式禁用 Temporal 支持（无需 Rust）。
- 🔍 若未显式传递`--v8-enable-temporal-support`，configure.py 会尝试自动检测 cargo 和 rustc：检测到则启用，未检测到则警告并禁用。
- ❌ 若显式传递`--v8-enable-temporal-support`但未检测到 Rust 工具链，构建将报错停止。
- 🚫 同时使用启用和禁用选项会导致 configure.py 报错停止，以避免歧义。
- 🤔 讨论中关注自动检测可能因系统更新意外影响 Temporal 的启用状态，建议在发布机器上显式指定选项以确保稳定性。
- 🏷️ PR 被标记为 semver-major（重大变更），计划在 Node.js 26 版本中推出，且暂不应用于 v20.x 至 v25.x 版本线。

---

### [单可执行应用程序 | Node.js v25.6.1 文档](https://nodejs.org/api/single-executable-applications.html)

**原文标题**: [Single executable applications | Node.js v25.6.1 Documentation](https://nodejs.org/api/single-executable-applications.html)

Node.js 单可执行应用程序功能允许将脚本和资源打包进 Node.js 二进制文件，生成独立的可执行文件，无需在目标系统安装 Node.js。该功能支持嵌入脚本、资源文件，并可配置启动参数、V8 代码缓存和启动快照以优化性能。

- 🚀 **生成单可执行应用**：使用 `--build-sea` 标志和配置文件，可将 JavaScript 脚本及相关资源打包成独立可执行文件。
- 📦 **资源嵌入与管理**：通过配置文件的 `assets` 字段嵌入资源（如图片、文本），并在运行时通过 `node:sea` API（如 `getAsset`）访问。
- ⚡ **性能优化选项**：支持 V8 代码缓存（`useCodeCache`）加速脚本编译，以及启动快照（`useSnapshot`）实现快速启动。
- ⚙️ **执行参数配置**：可通过 `execArgv` 预设 Node.js 运行时参数，并通过 `execArgvExtension` 控制环境变量或命令行扩展参数。
- 🔧 **手动注入流程**：除 `--build-sea` 外，也可使用 `postject` 等工具手动将准备块注入 Node.js 二进制文件，支持 Windows、macOS 和 Linux。
- 📝 **脚本环境特性**：嵌入的主脚本中，`require()` 仅支持内置模块，`__filename` 和 `__dirname` 指向可执行文件路径，原生插件需作为资源嵌入并临时加载。
- 🖥️ **平台支持**：CI 定期测试 Windows、macOS 和 Linux（除 Alpine 和 s390x 架构），其他平台可通过社区工具链探索支持。

---

### [sea: 通过 joyeecheung 在 SEA 中支持 ESM 入口点 · Pull Request #61813 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61813)

**原文标题**: [sea: support ESM entry point in SEA by joyeecheung · Pull Request #61813 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61813)

Node.js 项目合并了一个支持在单可执行应用（SEA）中使用 ESM 模块作为入口点的功能。

- 🚀 通过新增 `"mainFormat": "module"` 配置字段，SEA 现在支持将 ESM 模块作为入口点。
- 🔧 该功能基于新的 `StartExecutionCallbackWithModule` 嵌入器 API 实现，行为与 CommonJS 入口点基本保持一致。
- ⚠️ 代码缓存和快照支持将作为后续工作，目前暂未实现。
- 📦 此特性允许用户在打包应用以构建 SEA 时，将输出目标从 CommonJS 改为 ESM。
- 🔒 目前仅支持内置模块的访问，对非内置模块的访问需等待虚拟文件系统（VFS）功能的实现。
- 📝 文档已相应更新，并修复了 `node:sea` 内置模块中 `sea.isSea()` API 的表述，以保持与其他 API 的一致性。

---

### [Node.js 虚拟文件系统 by mcollina · Pull Request #61478 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61478)

**原文标题**: [Virtual File System for Node.js by mcollina · Pull Request #61478 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61478)

Node.js 核心仓库中一个关于新增虚拟文件系统（VFS）模块的拉取请求，该模块具有可插拔的提供者架构，并与 `fs` 模块和模块加载器集成。

- 📦 **核心功能**：引入 `node:vfs` 模块，提供基于提供者架构的虚拟文件系统，支持内存、SEA（单可执行应用）资产和自定义提供者。
- 🔌 **架构设计**：采用可扩展的提供者架构，包括 `MemoryProvider`（内存读写）、`SEAProvider`（只读访问 SEA 资产）和 `VirtualProvider`（自定义提供者基类）。
- 🛠️ **API 兼容**：使用标准的 `fs` API（如 `writeFileSync`, `readFileSync`），无需学习新方法，并可挂载到特定路径前缀（如 `/virtual`）。
- 🔗 **模块集成**：支持通过 `require()` 和 `import` 无缝加载虚拟文件，并与单可执行应用（SEA）集成，资产自动挂载在 `/sea`。
- 📝 **代码示例**：展示了如何创建 VFS、写入文件、挂载并使用标准 `fs` API 和 `require` 访问虚拟文件，以及 SEA 中的自动资产访问。
- 🔍 **开发进展**：PR 经历了多次代码审查、反馈和修改，包括路径规范化、API 调整、文档完善和安全性改进（如确保缓冲区副本安全）。
- 🧪 **测试与覆盖**：添加了测试用例以提高代码覆盖率，并解决了 Windows 兼容性等问题。
- 📄 **文档更新**：更新了相关文档，说明了 VFS 的局限性（如不支持原生插件、子进程等）和 SEA 集成细节。
- 👥 **社区互动**：多位贡献者参与讨论，提出了关于 API 设计、性能、与现有规范（如 WHATWG FS）对齐以及未来扩展性的反馈。

---

### [Socket 安全分析现已在 npm 上一键完成 - Sock...](https://socket.dev/blog/socket-security-analysis-is-now-one-click-away-on-npm)

**原文标题**: [Socket Security Analysis Is Now One Click Away on npm - Sock...](https://socket.dev/blog/socket-security-analysis-is-now-one-click-away-on-npm)

Cline CLI npm 包因疑似缓存投毒攻击而遭到入侵，攻击者利用被泄露的 npm 发布令牌推送了包含恶意后安装脚本的 cline@2.3.0 版本，该工具作为流行的 AI 编程助手 CLI 每周下载量达 9 万次。

- 🔐 攻击者通过泄露的 npm 发布令牌推送了恶意版本 cline@2.3.0
- ⚠️ 恶意代码隐藏在 postinstall 脚本中，可能自动执行有害操作
- 📦 该包作为 AI 编程助手 CLI 工具，每周下载量高达 9 万次
- 🕵️ 攻击方式疑似为缓存投毒，通过劫持合法发布流程实施
- 🚨 事件凸显 npm 生态系统对发布令牌安全性的依赖风险

---

### [express - npm 包安全分析 - Socket](https://socket.dev/npm/package/express)

**原文标题**: [express - npm Package Security Analysis - Socket](https://socket.dev/npm/package/express)

npm 现已将 Socket 的安全分析功能集成至每个软件包页面，用户可一键查看详细安全评估报告。

- 🔍 **一键安全分析**：npm 每个软件包页面新增 Socket 安全分析入口，实现快速漏洞检测
- 📊 **多维评估报告**：涵盖依赖风险、代码变更监控、恶意软件扫描等核心安全维度
- 🛡️ **主动防护升级**：通过实时监控供应链攻击和可疑代码行为，提升开源生态安全性
- ⚡ **无缝集成体验**：开发者无需切换平台即可获取专业安全洞察，优化开发工作流程
- 📈 **行业标准演进**：此次合作标志着开源软件供应链安全验证流程向标准化迈出关键一步

---

### [zlib：通过 rokob 添加对 Brotli 压缩字典的支持 · Pull Request #61763 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61763)

**原文标题**: [zlib: add support for brotli compression dictionary by rokob · Pull Request #61763 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61763)

Node.js 的 zlib 模块新增了对 Brotli 压缩字典的 JavaScript API 支持，该功能已合并至主分支。

- 🆕 **新增功能**：为 Brotli 压缩添加了自定义字典支持，类似于已有的 zstd 实现。
- 🔧 **技术实现**：底层 Brotli 依赖已支持此功能，本次更新主要是在 JavaScript API 层面进行封装。
- 🐛 **问题修复**：解决了 GitHub 议题 #52250 中关于添加 Brotli 1.1.0 绑定与字典支持的需求。
- ✅ **代码审查**：经过多位核心贡献者（Anna Henningsen、Colin Ihrig 等）的审查与批准。
- 🧪 **测试与验证**：添加了相关测试，并经历了完整的 CI（持续集成）流程验证。
- 📝 **提交记录**：最终将三个提交合并为一个，并成功并入 `main` 分支。

---

### [Node.js vs Deno vs Bun 性能基准测试对比](https://www.repoflow.io/blog/node-js-vs-deno-vs-bun-performance-benchmarks)

**原文标题**: [Node.js vs Deno vs Bun Performance Benchmarks](https://www.repoflow.io/blog/node-js-vs-deno-vs-bun-performance-benchmarks)

本文对 Node.js、Deno 和 Bun 三个 JavaScript 运行时进行了 14 项性能基准测试，结果显示 Bun 在多数项目中领先，尤其在 HTTP 吞吐和大型 JSON 解析方面表现突出；Deno 在异步调度和算术循环测试中占优；Node.js 整体表现稳定，并在 SHA-256 哈希测试中领先。

- 🚀 **HTTP 吞吐测试**：Bun 在本地服务器高并发场景中表现最佳
- 📊 **JSON 解析性能**：Bun 处理大型 JSON 数据时速度最快，Deno 在小数据解析中也有优势
- 🔄 **JSON 序列化测试**：Bun 在中小型对象序列化中保持领先地位
- 🔐 **加密哈希性能**：Node.js 在小缓冲区 SHA-256 哈希测试中夺冠，Bun 在大数据哈希中更优
- 💾 **内存操作测试**：Bun 在 64KB 缓冲区复制测试中展现卓越的内存带宽性能
- 🧮 **数据处理效率**：Bun 在数组映射归约操作中速度最快
- 🔗 **字符串处理**：Bun 在字符串拼接测试中表现最优
- ⚡ **循环计算性能**：Deno 在随机化整数循环测试中领先
- ⏱️ **异步任务调度**：Deno 在 Promise 微任务链和 async/await 吞吐测试中表现最佳
- 🧪 **测试方法论**：所有测试在 M4 芯片设备上重复 15 次，采用自定义基准测试工具
- 📈 **综合结果**：Bun 在 8 项测试领先，Deno 在 5 项领先，Node.js 在 1 项领先
- 🔍 **测试局限性**：属于微基准测试，未反映完整应用场景性能
- 💡 **版本信息**：测试使用 Node 25.6.1、Deno 2.6.9、Bun 1.3.9 最新版本

---

### [Node.js 16 至 25 性能基准测试：性能随时间如何演变](https://www.repoflow.io/blog/node-js-16-to-25-benchmarks-how-performance-evolved-over-time)

**原文标题**: [Node.js 16 to 25 Benchmarks: How Performance Evolved Over Time](https://www.repoflow.io/blog/node-js-16-to-25-benchmarks-how-performance-evolved-over-time)

本文对 Node.js 16 至 25 版本进行了性能基准测试，重点关注 HTTP 吞吐量、JSON 处理、加密哈希、内存操作及循环计算等核心场景，揭示了版本迭代中的性能演进趋势，特别是 Node 25 在数值计算密集型任务中的显著提升。

- 🚀 **HTTP 吞吐量测试**：测量本地 HTTP 服务器在保持连接和并发请求下的每秒处理能力，展现版本间网络性能优化  
- 📊 **JSON 解析与序列化**：对比各版本解析和序列化小型 JSON 数据的速度，反映数据处理效率改进  
- 🔐 **SHA-256 哈希计算**：通过 crypto 模块测试哈希生成吞吐量，体现加密运算性能变化  
- 🧠 **内存与缓冲区操作**：使用 Buffer.copy 评估 64KB 数据复制效率，揭示内存管理优化  
- 🔁 **数组与字符串处理**：通过 map/reduce 操作和字符串拼接测试，展示常用编程模式性能演进  
- ⚡ **整数循环计算**：针对密集算术循环的专项测试，Node 25 在此类计算密集型任务中表现突出  
- 🎲 **随机化循环验证**：引入 Math.random() 防止过度优化，确认性能提升的真实性  
- 📈 **测试方法论**：基于 Apple M4 硬件，采用五次运行取中位数的严谨测试方式，避免热偏差影响结果  
- 💡 **核心结论**：Node.js 性能持续稳步提升，Node 25 在循环和数值计算场景提升显著，实际应用收益取决于具体工作负载特性

---

### [介绍@stoolap/node：一款速度惊人的原生 Node.js 驱动——Stoolap](https://stoolap.io/blog/2026/02/19/introducing-stoolap-node/)

**原文标题**: [Introducing @stoolap/node: A Native Node.js Driver That's Surprisingly Fast - Stoolap](https://stoolap.io/blog/2026/02/19/introducing-stoolap-node/)

本文介绍了作者为嵌入式 SQL 数据库 Stoolap 开发的 Node.js 原生驱动@stoolap/node，通过 NAPI-RS 实现高性能访问，并对比了其与 SQLite 在多种查询场景下的性能表现。

- 🚀 Stoolap Node.js 驱动通过 NAPI-RS 实现原生绑定，无需 HTTP 中间层，直接访问 Rust 编写的数据库引擎
- 📊 基准测试显示，在 53 项查询中 Stoolap 在 47 项领先，尤其在复杂查询（如 COUNT DISTINCT）中快达 138 倍
- ⚙️ 性能优势源于 MVCC 无锁并发、基于成本的查询优化器和并行执行机制
- 🐢 SQLite 在简单单行操作（如按 ID 查询）仍保持约 1.1-1.6 倍微弱优势
- 💾 提供完整的持久化支持，支持 WAL 日志和可配置的同步级别
- 📦 提供预编译二进制包，支持 macOS/Linux/Windows，无需 Rust 工具链即可安装使用

---

### [Stoolap - Rust 语言编写的高性能嵌入式 SQL 数据库 - Stoolap](https://stoolap.io/)

**原文标题**: [Stoolap - High-performance embedded SQL database in Rust - Stoolap](https://stoolap.io/)

Stoolap 是一个纯 Rust 编写、无 C 语言依赖的嵌入式 SQL 数据库，支持 ACID 事务、成本优化器、并行执行和 110 多种内置函数，并能编译为 WebAssembly。

- 🚀 **纯 Rust 实现**：零 C 语言依赖，内存安全，可编译为 WebAssembly，支持在浏览器中直接运行。
- 🔄 **MVCC 事务**：支持多版本并发控制与快照隔离，读写互不阻塞，提供时间旅行查询（`AS OF`）功能。
- ⚡ **成本优化器**：采用 PostgreSQL 风格的查询规划，支持自适应执行、布隆过滤传播和语义查询缓存，提升查询效率。
- 🧵 **并行执行**：基于 Rayon 工作窃取调度器，自动并行化过滤、连接、排序等操作，支持多核扩展。
- 🛠️ **企业级功能**：内置 B 树、哈希、位图等多种索引类型，支持窗口函数、递归 CTE、WAL 日志与崩溃恢复。
- 📊 **完整 SQL 支持**：涵盖 JOIN、子查询、ROLLUP/CUBE/GROUPING SETS、UNION 等标准 SQL 语法。
- 📦 **易于集成**：提供 Rust API 和独立 CLI，可快速嵌入应用，无需外部依赖或服务器部署。
- 🌐 **开源友好**：采用 Apache 2.0 许可证，包含明确的专利授权，适合企业和社区使用。

---

### [Stoolap 游乐场 - 在浏览器中试用 Stoolap - Stoolap](https://stoolap.io/playground/)

**原文标题**: [Stoolap Playground - Try Stoolap in Your Browser - Stoolap](https://stoolap.io/playground/)

Stoolap Playground 是一个基于浏览器的 SQL 查询工具，它通过 WebAssembly 在本地运行，确保数据安全且无需网络传输。

- 🚀 在浏览器中直接运行真实的 SQL 查询，无需安装额外软件
- 🔒 基于 WebAssembly 技术，所有操作均在本地执行，数据不会离开用户设备
- 🧪 提供交互式命令行界面，支持即时输入和执行 SQL 命令
- 📊 内置多种 SQL 功能示例，包括窗口函数、连接、聚合和递归 CTE 等
- 🛠️ 包含数据表查看、查询分析和执行计划解释等实用工具

---

### [GitHub - thisiskps/fetch-network-simulator: 获取网络模拟器](https://github.com/thisiskps/fetch-network-simulator)

**原文标题**: [GitHub - thisiskps/fetch-network-simulator: fetch-network-simulator](https://github.com/thisiskps/fetch-network-simulator)

fetch-network-simulator 是一个用于前端开发的网络行为模拟工具，它通过拦截全局 fetch 函数，在浏览器中模拟真实世界的不稳定网络条件，帮助开发者在开发阶段测试 UI 的健壮性。

- 🌐 **拦截全局 fetch**：在 JavaScript 层修改真实的 API 请求和响应行为，而非模拟 API。
- 🧪 **模拟多种网络状况**：包括延迟、随机请求失败、自动重试、响应乱序、并发限制和带宽限制。
- 🛠️ **提升 UI 韧性测试**：旨在暴露在生产环境中才可能出现的 UI 错误，如竞态条件和状态覆盖问题。
- 📦 **易于集成**：通过 npm 安装，需在应用入口点（如 main.js）初始化，建议仅在开发环境启用。
- 🔍 **支持调试模式**：提供结构化的请求生命周期日志，帮助开发者观察规则应用、重试和失败等情况。
- 🏗️ **可扩展架构**：采用确定性的规则执行管道，内置多种规则，并允许高级开发者实现自定义规则。
- 🚧 **持续开发中**：计划增加请求取消模拟、响应乱序等高级功能，并正在开发可视化控制层（UI）。
- ⚠️ **适用范围与限制**：仅限浏览器环境，作用于 HTTP 请求/响应层，不模拟传输层问题，也不能替代 API 模拟框架或后端模拟器。

---

### [定价 — 免费支持高达 5 万用户 | 月费从 0 美元起](https://clerk.com/pricing?utm_medium=newsletter&utm_campaign=pricing-rollout&utm_content=02-19-26&utm_source=cooper_press&dub_id=tWxC4SavLgiEUFux)

**原文标题**: [Pricing — Free Up to 50K Users | Plans from $0/mo](https://clerk.com/pricing?utm_medium=newsletter&utm_campaign=pricing-rollout&utm_content=02-19-26&utm_source=cooper_press&dub_id=tWxC4SavLgiEUFux)

Clerk 提供四个主要定价方案（Hobby、Pro、Business、Enterprise）和三个附加功能（B2B 认证、管理、计费），支持无限应用，按月度留存用户（MRU）和月度留存组织（MRO）计费，并提供免费起步层和初创公司折扣。

- 🆓 **Hobby 方案免费**：包含 5 万 MRU/应用、3 个仪表板席位、基础认证功能，无需信用卡即可开始构建。
- 💼 **Pro 方案增强功能**：年付$20/月起，增加移除品牌、多因素认证、企业连接等高级特性，适合规模扩展。
- 🏢 **Business 方案合规支持**：年付$250/月起，提供 SOC2/HIPAA 合规、优先支持、审计日志等，满足团队与合规需求。
- 🏭 **Enterprise 定制方案**：提供定制解决方案、高可用性 SLA、专属支持与迁移协助，按年计费。
- 🔧 **附加功能灵活扩展**：B2B 认证（免费基础版）、管理工具（免费 5 次模拟）和计费系统（0.7% 费用）可独立添加。
- 📊 **清晰按量计费**：超出免费额度后按 MRU/MRO 阶梯计价，提供首日免费和批量折扣，数据可随时导出。

---

### [BrowserPod：基于 Wasm 的通用浏览器沙箱（从 Node.js 起步）](https://labs.leaningtech.com/blog/browserpod-10)

**原文标题**: [BrowserPod: universal in-browser sandbox powered by Wasm (starting with Node.js)](https://labs.leaningtech.com/blog/browserpod-10)

BrowserPod 1.0 是一款基于浏览器的代码沙盒，利用 WebAssembly 技术，在用户端安全、高效地运行不受信任的代码，提供接近原生的速度、极低延迟、强数据本地化和低成本，同时保持与本地/云端执行的高保真度。首版支持 Node.js，未来将扩展至 Python、Ruby、Go、Rust 等语言，并计划在 2026 年底引入基于 CheerpX 的 Linux 级沙盒。

- 🌐 **浏览器内安全执行**：利用 WebAssembly 和浏览器安全模型，在浏览器中直接运行代码，避免云端沙盒的延迟、成本和数据暴露问题。
- 🚀 **多语言运行时支持**：首版搭载 Node.js 引擎，后续将陆续支持 Python、Ruby、Go、Rust 等语言，构建通用的浏览器计算平台。
- 🔧 **实际应用场景**：适用于浏览器内智能编码、Web IDE、交互式文档、教育平台等，实现高性能、高保真的开发与演示环境。
- 🌐 **门户网络功能**：通过 Portals 功能，将沙盒内服务暴露为可共享 URL，支持实时预览、协作调试，无需后端基础设施。
- 🏗️ **技术架构基础**：基于 WebVM 的系统调用层，提供虚拟文件系统、进程隔离和真正并发，适用于复杂工具和工作负载。
- 📅 **明确发展路线**：2026 年将逐步推出命令行工具及各语言引擎，并于年底实现 Linux 容器在浏览器中的运行，迈向通用浏览器执行层愿景。

---

### [CheerpX － 您网页应用中的虚拟机](https://cheerpx.io/)

**原文标题**: [CheerpX － Virtual machines in your web app](https://cheerpx.io/)

CheerpX 是一个 JavaScript 库，允许在浏览器中安全地客户端执行 x86 二进制文件，由 Leaning Technologies 开发，目前处于测试阶段。它支持在 Web 应用中运行虚拟机，并推出了 WebVM 演示和 CheerpX Games Runner 扩展。该技术基于 WebAssembly 实现浏览器内的 x86 虚拟化，提供商业支持、文档和社区资源。

- 🚀 CheerpX 1.0 现已发布，支持高性能浏览器内 x86 虚拟化
- 🌐 可通过 WebVM 演示体验图形化支持，无需本地安装
- 🎮 CheerpX Games Runner 扩展允许在浏览器中直接运行游戏
- 🔧 提供商业技术支持、定制化开发和咨询
- 📚 开放文档、GitHub 仓库和 Discord 社区资源
- 📅 持续更新博客分享技术进展和案例

---

### [GitHub - raineorshine/npm-check-updates: 查找比 package.json 允许更新的包依赖版本](https://github.com/raineorshine/npm-check-updates)

**原文标题**: [GitHub - raineorshine/npm-check-updates: Find newer versions of package dependencies than what your package.json allows](https://github.com/raineorshine/npm-check-updates)

npm-check-updates 是一个用于检查和升级 package.json 中依赖包版本的工具，支持 npm、yarn、pnpm、deno 和 bun，提供丰富的自定义选项和配置方式。

- 🔍 **检查依赖更新**：自动检测项目中 package.json 允许的依赖包是否有新版本，并保持现有的语义版本控制策略。
- ⬆️ **升级依赖版本**：通过命令 `ncu -u` 升级 package.json 中的依赖版本，需随后运行 `npm install` 更新安装包和 lock 文件。
- 🎯 **多种升级目标**：支持按最新版本、次要版本、补丁版本或遵循 semver 范围等多种方式升级，并可针对特定标签（如 beta）进行升级。
- 🛠️ **高度可定制**：提供过滤、排除、交互模式、医生模式等高级选项，可通过配置文件或命令行参数灵活控制升级行为。
- 📁 **配置文件支持**：支持通过 `.ncurc` 文件进行配置，并可定义函数实现更复杂的过滤和升级逻辑。
- 🔧 **模块化使用**：除了 CLI，还可作为模块导入到项目中以编程方式使用，方便集成到自动化流程中。
- 🛡️ **安全与稳定**：提供冷却期选项以减少供应链攻击风险，医生模式可测试升级后项目的稳定性，确保兼容性。

---

### [GitHub - forwardemail/tangerine: Node.js DNS over HTTPS - Tangerine 是 dns.promises.Resolver 的最佳直接替代方案，它通过 undici 使用 DNS over HTTPS（"DoH"），内置重试、超时、智能服务器轮换、AbortControllers 以及支持多后端缓存（含 TTL 和清除功能）。专为 @forwardemail 打造。](https://github.com/forwardemail/tangerine)

**原文标题**: [GitHub - forwardemail/tangerine: Node.js DNS over HTTPS - Tangerine is the best drop-in replacement for dns.promises.Resolver using DNS over HTTPS ("DoH") via undici with built-in retries, timeouts, smart server rotation, AbortControllers, and caching support for multiple backends (with TTL and purge support).  Made for @forwardemail.](https://github.com/forwardemail/tangerine)

Tangerine 是一个 Node.js 库，作为 `dns.promises.Resolver` 的直接替代品，通过 DNS over HTTPS (DoH) 提供 DNS 解析功能。它内置了重试、超时、智能服务器轮换、AbortController 支持以及多后端缓存（支持 TTL 和清除），旨在为隐私优先的电子邮件服务 Forward Email 提供增强的 DNS 解决方案。

- 🍊 **直接替代**：完全兼容 Node.js 原生的 `dns.promises.Resolver` API，支持 ESM 和 CJS 模块。
- 🔒 **隐私与安全**：默认使用 Cloudflare 的 DoH 服务器（1.1.1.1, 1.0.0.1），通过 HTTPS 加密 DNS 查询，防止中间人攻击。
- ⚡ **高性能**：基准测试显示其性能接近原生 DNS 模块，并支持自定义缓存后端（如 Redis）以提升速度。
- 🔧 **丰富功能**：包括智能服务器轮换、请求超时与重试、AbortController 支持、ECS 客户端子网查询及调试日志。
- 🧩 **灵活缓存**：支持多种缓存后端，可配置 TTL，并提供缓存清除功能，便于处理 DNS 记录变更。
- 📚 **完整文档**：提供详细的 API 说明、使用示例、配置选项和性能基准测试结果。

---

### [DNS over HTTPS - 维基百科](https://en.wikipedia.org/wiki/DNS_over_HTTPS)

**原文标题**: [DNS over HTTPS - Wikipedia](https://en.wikipedia.org/wiki/DNS_over_HTTPS)

DNS over HTTPS（DoH）是一种通过 HTTPS 协议进行远程域名系统（DNS）解析的技术，旨在通过加密 DNS 查询数据来提升用户隐私和安全性，防止中间人攻击窃听或篡改。该协议由 IETF 于 2018 年 10 月发布为 RFC 8484，并得到主流浏览器和操作系统的逐步支持。

- 🔒 **加密 DNS 查询**：通过 HTTPS 协议加密 DNS 数据，防止窃听和中间人攻击。
- 🌐 **主流应用支持**：自 2020 年起，Firefox、Chrome 等浏览器默认启用 DoH，iOS、Android、Windows 等系统也逐步集成。
- ⚖️ **与 DoT 的对比**：DoH 使用 HTTPS 加密，而 DNS over TLS（DoT）使用 TLS 协议，两者在隐私与安全上各有优势，取决于具体使用场景。
- 🛡️ **增强隐私保护**：Oblivious DNS over HTTPS（ODoH）通过代理和加密技术，进一步防止 DNS 服务器同时获取用户 IP 和查询内容。
- 🖥️ **多种部署方式**：可通过应用程序内置、本地网络代理或系统本地代理实现，适应不同网络环境。
- ⚠️ **争议与挑战**：DoH 可能影响企业网络安全监控、绕过家长控制或内容过滤，并引发关于网络审查与隐私平衡的讨论。
- 🔧 **技术持续发展**：IETF 和相关组织仍在完善 DoH 标准，以平衡性能、安全与网络管理需求。

---

### [GitHub - pnpm/pnpm：快速、节省磁盘空间的包管理器](https://github.com/pnpm/pnpm)

**原文标题**: [GitHub - pnpm/pnpm: Fast, disk space efficient package manager](https://github.com/pnpm/pnpm)

pnpm 是一个快速且节省磁盘空间的包管理器，适用于 Node.js 项目，通过内容寻址存储和硬链接技术优化依赖安装效率与存储。

- 🚀 **速度快**：比 npm 和 Yarn 快达 2 倍，适用于大型项目和单仓库
- 💾 **高效存储**：使用单一内容寻址存储，通过硬链接减少重复文件，节省磁盘空间
- 🔒 **严格依赖**：每个包只能访问其 package.json 中明确声明的依赖，避免隐式依赖问题
- 📦 **确定性安装**：使用 pnpm-lock.yaml 锁文件确保依赖版本一致性
- 🌍 **跨平台支持**：兼容 Windows、Linux 和 macOS 系统
- 🛠️ **多功能集成**：内置 Node.js 版本管理功能（pnpm env use），并支持单仓库架构
- 🏢 **生产验证**：自 2016 年起被各种规模团队广泛使用，包括微软的 Rush 项目
- 📜 **开源许可**：采用 MIT 许可证，社区活跃，拥有大量贡献者和用户

---

### [pnpm why | pnpm](https://pnpm.io/cli/why)

**原文标题**: [pnpm why | pnpm](https://pnpm.io/cli/why)

pnpm why 命令用于显示依赖指定包的所有包，输出以反向依赖树的形式呈现，从被查询的包开始回溯至工作区根目录，并自动去重重复子树。

- 🔍 **显示依赖关系**：列出所有依赖指定包的包，形成反向依赖树。
- 🌳 **树状结构输出**：从查询包开始回溯，重复子树标记为“deduped”。
- ⚙️ **多种选项**：支持递归查询、JSON 格式、详细输出、可解析格式等。
- 📦 **过滤与限定**：可针对生产依赖、开发依赖、全局包或指定深度进行筛选。
- 🛠️ **高级功能**：支持通过选择器过滤或使用自定义查找函数匹配依赖。

---

### [发布版本 28.1.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/28.1.0)

**原文标题**: [Release Version 28.1.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/28.1.0)

jsdom 28.1.0 版本发布，主要新增了 blob 相关方法，改进了计算样式和性能，并修复了多项问题。

- 🆕 新增 blob.text()、blob.arrayBuffer() 和 blob.bytes() 方法
- 🎨 改进 getComputedStyle()，考虑 CSS 特异性及正确处理 !important 优先级
- ⚡ 提升同步 XMLHttpRequest 性能，减少重复请求的初始开销
- 🔗 优化 node.getRootNode()、node.isConnected 和 event.dispatchEvent() 性能，通过缓存根节点
- 🆔 修复 document.getElementById() 在多个元素 ID 相同时返回首个树顺序元素
- 🖼️ 修正 <svg> 元素不再错误地将事件处理程序代理到 Window
- 📄 调整 FileReader 事件时序和结果状态以更符合规范
- 🛠️ 修复同步 XMLHttpRequest 遇到分发错误时的潜在挂起问题
- 🔄 提升与已使用 Node.js 内置 fetch() 的环境的兼容性，解决 undici 版本不兼容问题

---

### [GitHub - theoephraim/node-google-spreadsheet: JavaScript / TypeScript 的 Google Sheets API 封装库](https://github.com/theoephraim/node-google-spreadsheet)

**原文标题**: [GitHub - theoephraim/node-google-spreadsheet: Google Sheets API wrapper for Javascript / Typescript](https://github.com/theoephraim/node-google-spreadsheet)

这是一个用于 JavaScript/TypeScript 的 Google Sheets API 封装库，提供多种认证方式和丰富的表格操作功能。

- 📦 **项目概况** - 这是一个开源的 Node.js 库，拥有 2.5k 星标和 393 个分支，采用 MIT 许可证
- 🔐 **认证方式** - 支持服务账户、OAuth、API 密钥等多种 Google 认证方式
- 📊 **核心功能** - 提供单元格级和行级的读写操作，支持批量更新和格式设置
- 📑 **工作表管理** - 可添加、删除、调整大小、复制和更新工作表属性
- 📁 **文档管理** - 支持创建新文档、删除文档和基本的共享权限设置
- 📤 **导出功能** - 可将表格/文档以多种格式下载
- 🔄 **自动重试** - 内置指数退避算法的失败/限流请求自动重试机制
- 🛠️ **开发支持** - 提供完整的 TypeScript 类型支持，包含详细文档网站
- 👥 **社区贡献** - 项目由 Theo Ephraim 维护，欢迎社区贡献和支持

---

### [mineflayer - 使用稳定、高级 API 创建 Minecraft 机器人](https://prismarinejs.github.io/mineflayer/)

**原文标题**: [mineflayer - create minecraft bots with a stable, high level API](https://prismarinejs.github.io/mineflayer/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统通过分析医学影像提升疾病识别准确率
- 💊 基于算法的个性化治疗方案推荐助力精准医疗发展
- ⚡ 智能流程管理工具优化医院资源分配与患者就诊体验
- 🔬 基因组学与 AI 结合加速新药研发和病理机制研究
- ⚖️ 数据隐私保护与算法透明度成为实际应用中的关键议题

---

### [GitHub - ljharb/qs：支持嵌套的查询字符串解析器和序列化器](https://github.com/ljharb/qs)

**原文标题**: [GitHub - ljharb/qs: A querystring parser and serializer with nesting support](https://github.com/ljharb/qs)

qs 是一个用于解析和序列化查询字符串的 JavaScript 库，支持嵌套对象和数组，提供丰富的配置选项以处理不同编码、限制和安全需求。

- 📦 支持嵌套对象和数组的查询字符串解析与序列化
- ⚙️ 提供多种配置选项，如深度限制、数组格式、字符编码等
- 🛡️ 内置安全防护，包括参数数量限制和深度限制，防止滥用
- 🔄 支持多种数组格式（索引、括号、重复、逗号）和对象表示法（点号、括号）
- 🌐 兼容 UTF-8 和 ISO-8859-1 编码，支持字符集检测
- 📄 可自定义编码/解码函数，适应特殊需求
- 🏢 企业级支持可通过 Tidelift 订阅获得

---

### [发布 v8.56.0 · typescript-eslint/typescript-eslint · GitHub](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v8.56.0)

**原文标题**: [Release v8.56.0 · typescript-eslint/typescript-eslint · GitHub](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v8.56.0)

typescript-eslint 发布了 v8.56.0 版本，主要新增了对 ESLint v10 的支持，并修复了从 context.languageOptions 获取解析器选项的问题。

- 🚀 新增对 ESLint v10 的支持
- 🩹 修复了从 context.languageOptions 获取解析器选项的问题
- ❤️ 感谢贡献者 Brad Zacher、DMartens 和 Joshua Chen

---

### [Node Weekly 读者专享优惠 · EuroPDF - 快速安全地将 HTML 转换为 PDF！](https://www.europdf.eu/node-weekly/)

**原文标题**: [Special offer for Node Weekly readers Â· EuroPDF - create PDFs from HTML, fast and secure!](https://www.europdf.eu/node-weekly/)

EuroPDF 是一项基于 PrinceXML 引擎的 PDF 生成服务，通过 API 将 HTML、CSS 和 JavaScript 转换为 PDF，完全在欧盟境内运营，注重数据隐私与安全。

- 📄 **核心功能**：通过 API 调用将 HTML/CSS/JavaScript 快速生成 PDF，支持回调 URL 和异步处理  
- 🌍 **数据合规**：服务器位于德国，数据处理全程在欧盟境内，满足 GDPR 高标准要求  
- 🛠️ **技术优势**：基于 PrinceXML 引擎，完整支持现代 CSS、JavaScript、SVG、网页字体等标准  
- ♿ **可访问性**：通过结构化 HTML 可生成符合无障碍标准的 PDF 文档  
- 📊 **灵活计费**：提供免费方案（每月 5 份常规 PDF）及阶梯式付费方案（起价 12 欧元/月），支持按量超额计费  
- ⚡ **高扩展性**：自动处理大规模或复杂文档生成，支持高并发请求（最高 32 并发）  
- 🔧 **开发友好**：提供 Fetch/Axios/Got 等多种代码示例，支持即时测试（测试 PDF 带水印）  
- ⏱️ **时效保障**：同步 API 限时 60 秒，异步生成限时 5 分钟，适合数百页大型文档  
- 📦 **数据留存**：生成完成后立即删除输入/输出数据，可手动延长保留期用于调试  
- 🔄 **版本更新**：持续支持最新 Prince 引擎版本（当前支持 Prince 16 及 15.4）

---

### [JSNation——2026 年主要 JavaScript 大会](https://jsnation.com/?utm_source=partner&utm_medium=nodeweekly)

**原文标题**: [JSNation – the main JavaScript conference of 2026](https://jsnation.com/?utm_source=partner&utm_medium=nodeweekly)

JSNation 2026 是一场为期两天的 JavaScript 国际会议，将于 6 月 11 日（阿姆斯特丹线下 + 线上）和 6 月 15 日（线上）举行。会议聚焦全栈工程与前沿 Web 开发，设有 50 多位演讲者、深度专题研讨、免费与付费工作坊，并提供线上线下混合参与方式，旨在连接全球开发者社区。

- 🗓️ **会议时间与形式**：2026 年 6 月 11 日（阿姆斯特丹线下 + 线上）与 6 月 15 日（纯线上），为期两天双轨道。
- 🎤 **核心内容**：涵盖 50+ 场演讲，主题包括全栈开发与架构、AI 辅助编程、AI 工程、晋升高级工程师与 Tech Lead 所需技能等深度专题。
- 🌍 **参与规模**：预计 1500 名线下参会者，超过 1 万名远程参与者，汇聚全球 JavaScript 开发者。
- 🛠️ **特色活动**：会前工作坊、线下社交派对、阿姆斯特丹城市游览、全球最大的 JS 派对以及 JS 开源奖项评选。
- 🧑‍🏫 **知名讲者**：包括来自 Google、Meta、Netflix、Vercel 等公司的技术专家，如 Addy Osmani、Evan You、Matteo Collina 等。
- 🎟️ **票务选项**：提供线下 + 线上混合票、纯远程票、与 React Summit 的联票，以及包含酒店住宿的套餐，并有多人团队折扣。
- 📚 **增值服务**：GitNation Multipass 可通行 10 场会议，并提供独家深度内容；会议提供奖学金支持技术领域的多元群体。

---

### [介绍 Geist Pixel - Vercel](https://vercel.com/blog/introducing-geist-pixel)

**原文标题**: [Introducing Geist Pixel - Vercel](https://vercel.com/blog/introducing-geist-pixel)

Geist 字体家族新增 Geist Pixel 系列，这是一款基于像素网格设计的位图风格字体，延续了 Geist Sans 和 Geist Mono 的系统化设计理念，注重功能性、可扩展性和现代产品适配性。

- 🎨 **系统化扩展**：Geist Pixel 并非装饰字体，而是作为 Geist 字体系统的功能延伸，包含五种独立变体（方形、网格、圆形、三角形、线条），适用于实际产品场景。
- 🔢 **严格像素网格**：所有字形基于统一像素网格构建，兼顾节奏感、间距与可读性，既保留早期屏幕字体的复古感，又适合现代数字产品。
- ⚙️ **生产环境优化**：解决了传统像素字体在跨视口缩放、排版指标冲突等问题，保持视觉纹理的同时确保排版严谨性，与 Geist 家族共享清晰结构、可预测指标和跨平台适配性。
- 📦 **便捷集成**：提供 npm 安装包和 CSS 变量，支持在 Web 项目中快速调用，示例代码展示如何在布局文件中嵌入字体变体。
- 🖥️ **现代产品导向**：专为真实 UI 场景设计（如横幅、仪表盘、实验性布局），垂直指标与 Geist 家族对齐，支持多语言（32 种语言）并包含 7 种风格集。
- ✍️ **手工精修设计**：虽基于网格，但每个字形均经手动优化，避免视觉噪点与权重不均，采用半等宽水平指标，兼顾小尺寸清晰度与大尺寸表现力。
- 🚀 **内部先行应用**：发布前已在 Vercel 内部用于探索性设计与产品重塑，逐步融入品牌视觉语言。
- 🌱 **家族持续扩展**：Geist 家族已覆盖功能型 UI 文本至表达型显示场景，未来将继续推出 Geist Serif 等新成员。

---

### [盖斯特字体](https://vercel.com/font)

**原文标题**: [Geist Font](https://vercel.com/font)

Vercel 推出专为开发者和设计师设计的 Geist 字体家族，包含 Geist Sans、Geist Mono 和最新发布的 Geist Pixel 版本，强调简洁、清晰与功能性，并支持多种安装方式。

- 🎨 Geist 字体家族包含 Sans、Mono 及新推出的 Pixel 版本，专为开发与设计场景打造
- 📐 设计灵感源自瑞士设计运动，注重简约、极简与速度，提升视觉体验
- 🔤 提供完整字形支持与字体特性设置，可通过 NPM、Google Fonts 或手动下载安装
- ⚙️ 推荐使用 NPM 安装，以获取最佳 Next.js 集成、全字形支持及自动更新功能
- 🌐 Google Fonts 提供快速网页集成，但暂不支持 Geist Pixel 及部分高级特性
- 📦 支持手动下载 .zip 文件，包含 OTF、WOFF2 及可变字体文件，适用于自定义项目

---

### [Electrobun v1 - 黑板博客](https://blackboard.sh/blog/electrobun-v1/)

**原文标题**: [Electrobun v1 - Blackboard Blog](https://blackboard.sh/blog/electrobun-v1/)

Electrobun v1 是一个用于构建快速、轻量、跨平台桌面应用的 TypeScript 框架，由开发者 Yoav 历时两年开发而成，现已稳定发布。

- 🚀 开发动机源于对现有桌面开发工具链的不满，特别是 Electron 在代码签名、分发和更新方面的复杂体验，以及 Tauri 对 Rust 语言的依赖
- 🌍 从仅支持 macOS 扩展到全面支持 macOS、Windows 和 Ubuntu，提供自动生成的安装程序、自动更新和差分补丁
- 🔧 采用 Bun 作为底层运行时，利用其 FFI 和共享内存特性优化性能，并集成 zig-bsdiff 实现高效的差分更新
- 🖥️ 提供完整的桌面应用功能套件，包括跨平台窗口控制、菜单、快捷键、剪贴板、对话框、Webview 分区等
- 🧩 创新实现 `<electrobun-webview>` 标签，解决了 Electron 中 Webview 的遗留问题，支持真正的进程隔离和跨平台兼容
- 📈 目前框架已稳定，作者将其用于重写 co(lab) 项目，并鼓励社区在 Discord 中共同构建应用

---

### [Electrobun 文档 - 构建超快速、轻量级、跨平台桌面应用](https://blackboard.sh/electrobun/docs/)

**原文标题**: [Electrobun Documentation - Build ultra fast, tiny, cross-platform desktop apps](https://blackboard.sh/electrobun/docs/)

Electrobun 是一个基于 TypeScript 的超快、超小、跨平台桌面应用开发框架，它结合了原生绑定与 Bun 运行时，提供极致的性能和原生体验。

- 🚀 使用 Bun 作为后端运行时和打包工具，结合 C++、ObjC 和 Zig 编写的原生绑定，实现超高性能
- 📦 应用体积极小（约 14MB），更新包仅 14KB，启动时间低于 50 毫秒
- 🌐 默认使用系统原生 Webview 渲染（可选 CEF），确保 100% 原生操作感受
- 🔄 内置基于 bsdiff 的自定义增量更新机制，支持跨平台（macOS、Windows、Linux）
- 🛠️ 提供完整的开发工具链，包括窗口管理、上下文菜单、系统托盘、事件处理等浏览器与原生 API
- 📚 涵盖从快速入门、UI 构建、打包分发到高级主题（如跨平台开发、代码签名）的详细文档
- 👥 拥有活跃的社区支持，提供 GitHub 仓库和 Discord 频道供开发者交流与获取帮助

---

### [Three.js 地震模拟](https://mrdoob.github.io/three-quake/)

**原文标题**: [Three.js Quake](https://mrdoob.github.io/three-quake/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统通过分析医学影像提升疾病识别准确率
- 💊 基于算法的个性化治疗方案推荐助力精准医疗发展
- ⚡ 智能流程管理工具优化医院资源分配与患者就诊体验
- 🧠 自然语言处理技术加速医疗文献分析与临床决策支持
- ⚖️ 数据隐私保护与算法透明度成为行业关注焦点

---

### [Three.js 下降](https://mrdoob.github.io/three-descent/)

**原文标题**: [Three.js Descent](https://mrdoob.github.io/three-descent/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 🧬 基于患者基因组数据的 AI 模型可为慢性病和肿瘤提供个性化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [GitHub - mrdoob/three-descent: 将《Descent》移植到 Three.js 的工作进行中版本。](https://github.com/mrdoob/three-descent)

**原文标题**: [GitHub - mrdoob/three-descent: A WIP port of Descent to Three.js.](https://github.com/mrdoob/three-descent)

这是一个使用 Three.js 对经典游戏《Descent》进行移植的未完成项目。

- 🎮 项目是一个基于 Three.js 的《Descent》游戏移植版本
- 🚧 当前状态为“进行中”（WIP），尚未完成
- 🌐 提供在线试玩链接，使用分享版游戏资源（仅包含第一章节）
- 📄 完整游戏需要用户自行替换为正版游戏文件
- ⚖️ 项目代码采用 MIT 开源许可证
- 👥 由 mrdoob 主导开发，并得到 Claude 的协助
- ⭐ 在 GitHub 上获得 63 个星标和 3 个分支

---

### [发布 v2.6.10 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.6.10)

**原文标题**: [Release v2.6.10 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.6.10)

Deno 2.6.10 版本发布，主要包含多项功能增强、错误修复及 Node.js 兼容性改进。

- 🚀 **新增功能**：支持 TLS 密钥日志、更多许可证文件类型发布，以及 `deno install --compile` 命令。
- 🔧 **编译与部署修复**：优化编译检查、部署依赖年龄限制，并清理安装时的 `node_modules` 文件夹。
- 📦 **Node.js 兼容性提升**：修复 `assert.ok`、`fs.rmdir`、`worker_threads` 等多处模块行为，确保与 Node.js 一致。
- 🌐 **Web 与网络修复**：防止 AbortSignal 被垃圾回收，优化可写流的中断信号处理。
- 🛠️ **工具与测试改进**：更新 LSP 依赖、修复 zlib 回调异步性，并禁止在测试执行中调用 `Deno.test()`。

---

### [功能：通过 littledivy 添加 `deno install --compile` · 拉取请求 #32046 · denoland/deno · GitHub](https://github.com/denoland/deno/pull/32046)

**原文标题**: [feat: add `deno install --compile` by littledivy · Pull Request #32046 · denoland/deno · GitHub](https://github.com/denoland/deno/pull/32046)

该内容是关于 Deno 项目的一个 GitHub Pull Request，主要介绍了为 `deno install` 命令新增 `--compile` 选项的功能，允许将 npm 包编译为独立的可执行文件。

- 🚀 新增 `deno install --compile` 功能，支持将 npm 包编译为独立可执行文件
- ⚡ 编译后的可执行文件运行更快，且不依赖 Deno 环境
- 📦 示例中编译了 `npm:@anthropic-ai/claude-code` 包，生成 83.17MB 的可执行文件
- 🔧 该功能解决了 issue #19156，允许通过 `deno install -g --compile` 标志进行全局安装
- ✅ Pull Request 已合并，经过代码审查和测试，53/59 项检查通过
- 👥 由 littledivy 提交，dsherret 审核并批准合并

---

