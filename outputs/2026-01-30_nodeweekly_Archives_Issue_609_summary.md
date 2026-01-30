### [Node 周刊第 609 期：2026 年 1 月 29 日](https://nodeweekly.com/issues/609)

**原文标题**: [Node Weekly Issue 609: January 29, 2026](https://nodeweekly.com/issues/609)

本期内容主要涵盖 Node.js 25.5 版本发布、性能优化、安全更新、工具推荐及生态系统动态，重点关注新特性、基准测试和开发资源。

- 🚀 Node.js 25.5 发布，新增`--build-sea`标志简化单可执行应用构建流程
- 📊 Node.js 16 至 25 版本性能基准测试显示，部分任务在 25 版有显著提升
- 🔒 OpenSSL 安全公告评估：Node.js 受三个 CVE 影响，将在常规更新中修复
- 🛠 推荐工具：`npx is-my-node-vulnerable`检查漏洞，`nr`工具加速 npm 脚本运行
- 📄 社区讨论：开发者对 Express 和 Node.js 的当前选择持不同意见
- 🤖 GitHub Copilot SDK 发布，支持在 Node 应用中集成 AI 代理功能
- 📋 工具更新：LibPDF 支持 TypeScript 处理 PDF，clipboardy 提供跨系统剪贴板 API
- 🌊 Bun 运行时更新：v1.3.7 提升异步性能，v1.3.8 内置 Markdown 解析器
- 🎧 播客推荐：访谈 Node.js TSC 成员探讨 2026 年运行时内部机制与性能趋势
- 🔄 生态动态：包括 Lodash 安全更新、Vercel/Netlify/Cloudflare 冷启动对比等

---

### [提升 Node.js 单可执行应用构建能力 | Joyee Cheung 的博客](https://joyeecheung.github.io/blog/2026/01/26/improving-single-executable-application-building-for-node-js/)

**原文标题**: [Improving Single Executable Application Building for Node.js | Joyee Cheung's Blog](https://joyeecheung.github.io/blog/2026/01/26/improving-single-executable-application-building-for-node-js/)

本文介绍了作者将 Node.js 单可执行应用构建流程集成到核心中的过程，包括背景、技术细节和社区贡献的挑战。

- 🚀 作者成功将单可执行应用构建流程移入 Node.js 核心，简化了构建步骤
- 🔧 新流程通过`--build-sea`标志实现，无需外部工具，降低了使用门槛
- 📜 单可执行应用功能最初由社区推动，经历了多次迭代和志愿者贡献
- 🐌 由于依赖志愿者，开发进度常因缺乏持续投入而放缓
- 🏗️ 构建过程涉及资源打包、注入和运行时加载，作者重点改进了注入环节
- 🔍 通过集成 LIEF 库处理不同平台的二进制格式，使 Node.js 能自主修改可执行文件
- 📦 集成 LIEF 后二进制大小仅增加约 5MB，在可接受范围内
- 🤝 改进最终被合并到 Node.js v25.5.0，并可能向后移植到旧版本
- 💡 作者呼吁更多社区贡献，以维持 Node.js 生态的持续发展

---

### [单可执行应用程序 | Node.js v25.5.0 文档](https://nodejs.org/api/single-executable-applications.html)

**原文标题**: [Single executable applications | Node.js v25.5.0 Documentation](https://nodejs.org/api/single-executable-applications.html)

Node.js 单可执行应用程序功能允许将脚本和资源打包进 Node.js 二进制文件中，生成一个独立的可执行文件，无需在目标系统上安装 Node.js。该功能通过注入一个包含捆绑脚本的准备数据块（blob）来实现，支持嵌入资源、启动快照和 V8 代码缓存以优化性能，并提供了配置执行参数和扩展的选项。

- 📦 **生成单可执行应用**：使用 `--build-sea` 标志和 JSON 配置文件，可将脚本、资源及配置打包成独立可执行文件。
- 🛠️ **资源配置与访问**：通过配置文件中的 `assets` 字段嵌入资源（如图片、文本），并在脚本中使用 `sea.getAsset()` 等 API 进行访问。
- ⚡ **性能优化支持**：启用 `useSnapshot` 可利用启动快照加速应用启动；启用 `useCodeCache` 可生成 V8 代码缓存，提升脚本编译速度。
- ⚙️ **执行参数配置**：通过 `execArgv` 字段预置 Node.js 运行时参数（如 `--no-warnings`），并可通过 `execArgvExtension` 控制环境变量或命令行扩展。
- 📝 **脚本环境特性**：注入的主脚本中，`require()` 仅支持内置模块，`__filename` 和 `__dirname` 指向可执行文件路径，且支持通过临时文件加载原生插件。
- 🔧 **创建与注入流程**：生成准备数据块后，需将其注入 Node.js 二进制文件（如使用 postject 工具），并更新特定标识以启用单可执行功能。
- 🌍 **平台兼容性**：该功能已在 Windows、macOS 和主流 Linux 发行版上经过测试，但部分平台（如 Alpine Linux、s390x 架构）可能不受支持。

---

### [Node.js — Node.js 25.5.0（当前版本）](https://nodejs.org/en/blog/release/v25.5.0)

**原文标题**: [Node.js — Node.js 25.5.0 (Current)](https://nodejs.org/en/blog/release/v25.5.0)

Node.js 25.5.0 版本发布，主要引入了新的 `--build-sea` 命令行标志，简化了单可执行应用程序（SEA）的构建流程，同时包含多项功能更新、错误修复和依赖项升级。

- 🚀 新增 `--build-sea` 标志，简化单可执行应用程序（SEA）的构建流程，将之前的多步操作合并为一步
- 🔧 `fs` 模块新增 `ignore` 选项到 `fs.watch`，增强文件监视功能
- 🛡️ SQLite 默认启用防御模式，提升安全性
- 📦 更新根证书至 NSS 3.119，增强加密安全性
- 🧪 测试运行器新增支持预期测试用例失败的功能
- 🔄 多项依赖项升级，包括 npm 至 11.8.0、SQLite 至 3.51.2、ICU 至 78.2 等
- 🐛 修复了多个模块的错误，包括流、HTTP/2、集群、子进程等
- 📚 文档更新，包括移除版本号前的 "v" 前缀、澄清 `process.argv[1]` 行为等
- 🌐 新增 Windows、macOS、Linux 等多平台的安装包和二进制文件下载链接

---

### [sqlite：默认启用防御模式 by louwers · Pull Request #61266 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61266)

**原文标题**: [sqlite: enable defensive mode by default by louwers · Pull Request #61266 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61266)

Node.js 项目中的 SQLite 模块已默认启用防御模式，以增强数据库文件的安全性，防止普通 SQL 语句意外损坏数据。

- 🛡️ 该 PR 默认启用 SQLite 防御模式，禁用可能破坏数据库文件的 SQL 语言特性
- 📚 修改参考了 SQLite 官方文档及相关讨论，确保变更合理且安全
- ✅ 代码审查通过，多位贡献者批准，并经过完整的 CI 测试
- 🏷️ 被标记为 semver-minor 和 notable-change，将在版本发布说明中重点提及
- 🚀 变更已成功合并至主分支，并随 Node.js v25.5.0 版本发布

---

### [fs: 添加忽略选项到 fs.watch 由 mcollina · Pull Request #61433 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61433)

**原文标题**: [fs: add ignore option to fs.watch by mcollina · Pull Request #61433 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61433)

Node.js 的 `fs.watch()` 函数新增了一个 `ignore` 选项，用于在递归监视文件系统时过滤不需要的事件，从而避免因监视大量文件（如 `node_modules`）而导致的系统资源压力。

- 🚀 **新增 `ignore` 选项**：为 `fs.watch()` 添加了 `ignore` 配置参数，支持字符串通配符、正则表达式、函数或它们的数组，以过滤文件系统事件。
- ⚙️ **优化内核资源使用**：该选项不仅过滤事件，还会完全跳过对忽略路径的监视，从而减少不必要的内核级文件监视器，提升性能。
- 🧪 **修复测试稳定性**：针对 macOS 等系统的事件延迟和合并特性，调整了测试逻辑（如使用 `setInterval` 替代 `setTimeout`），并修正了 `node_modules` 目录的模式匹配问题。
- 📚 **更新文档与测试**：同步更新了相关 API 文档，并新增了对应的测试用例，确保功能稳定可靠。
- ✅ **通过代码审查与 CI**：经过多位核心贡献者审查，并通过了完整的 CI 测试，最终被合并到 Node.js 主分支，并计划在下一个次要版本中发布。

---

### [文员 MCP 服务器](https://clerk.com/changelog/2026-01-20-clerk-mcp-server?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=mcp-server&utm_content=01-29-26&dub_id=WKInO9scCNTTAjqD)

**原文标题**: [Clerk MCP Server](https://clerk.com/changelog/2026-01-20-clerk-mcp-server?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=mcp-server&utm_content=01-29-26&dub_id=WKInO9scCNTTAjqD)

Clerk 推出 MCP 服务器公开测试版，使 AI 编程助手能直接获取最新的 Clerk SDK 代码片段和实现模式，提升开发效率。

- 🚀 Clerk 发布 MCP 服务器公开测试版，帮助 AI 编程助手（如 Claude、Cursor、GitHub Copilot）获取准确的 Clerk SDK 代码片段和实现模式
- 🤖 该服务器基于模型上下文协议（MCP），可为 AI 助手提供最新的实现指导和最佳实践
- 💬 连接后，开发者可向 AI 助手提问，例如如何在 Next.js 中实现身份验证钩子、设置 B2B SaaS 组织和权限、创建应用等候名单流程等
- 📚 完整设置说明和详细信息可查阅相关文档
- 📢 团队鼓励用户通过反馈门户或 Discord 社区提供使用反馈

---

### [Node.js 16 至 25 性能基准测试：性能随时间如何演变](https://www.repoflow.io/blog/node-js-16-to-25-benchmarks-how-performance-evolved-over-time)

**原文标题**: [Node.js 16 to 25 Benchmarks: How Performance Evolved Over Time](https://www.repoflow.io/blog/node-js-16-to-25-benchmarks-how-performance-evolved-over-time)

本文对 Node.js 16 至 25 版本进行了性能基准测试，重点关注 HTTP 吞吐量、JSON 处理、加密哈希、内存操作及循环计算等核心场景，揭示了版本迭代中的性能演进趋势。

- 🚀 **Node.js 24 与 25 版本性能显著提升**：测试发现 Node 24 在 Express 负载中表现突出，而 Node 25 在数值计算和密集型循环任务中进步尤为明显。
- 📊 **全面覆盖版本范围**：测试涵盖 16.0.0 至 25.3.0 共 20 个版本，包括 LTS 与非 LTS 版本，以展示完整的性能发展轨迹。
- ⚙️ **多维度性能指标**：测试包括 HTTP GET 吞吐量、JSON 解析与序列化速度、SHA-256 哈希计算、缓冲区复制、数组操作、字符串拼接及整数循环运算等关键场景。
- 🔬 **科学测试方法**：采用自定义基准测试工具，在 Apple M4 硬件上运行，每次测试重复五次并取中位数结果，避免热效应对结果的影响。
- 💡 **实际应用启示**：虽然合成测试显示最佳性能，但实际应用收益取决于 I/O、内存访问模式等因素；建议计算密集型项目升级至新版本以获得性能提升。

---

### [GitHub - dawsbot/nr：最快的“npm run”实现](https://github.com/dawsbot/nr)

**原文标题**: [GitHub - dawsbot/nr: The fastest "npm run" possible](https://github.com/dawsbot/nr)

nr 是一个用 Rust 编写的零开销 npm 脚本运行器，旨在以最快速度执行 package.json 中的脚本，无需 Node.js 启动或 npm 开销。

- 🚀 **极速运行**：相比传统工具，nr 在基准测试中比 pnpm 快 27.8 倍，启动仅需 10 毫秒
- ⚙️ **直接执行**：在 Unix 系统上使用 exec() 系统调用，无额外进程开销，脚本在原进程槽中运行
- 📦 **轻量二进制**：体积仅 377KB，无运行时、垃圾回收或框架依赖
- 🔧 **简易安装**：支持 macOS、Linux 和 Windows（通过 Git Bash/WSL），一行命令即可安装
- 🤖 **AI 助手集成**：可配置让 Claude、Cursor、GitHub Copilot 等 AI 编码助手使用 nr 替代 npm run
- 🎯 **功能专注**：仅读取 package.json 的 scripts 字段，不支持 pre/post 生命周期脚本和 workspaces
- ⚡ **性能优势**：无 Node.js 启动延迟，直接解析并执行命令，避免传统工具 50-100 毫秒的启动时间
- 📄 **开源实验**：项目处于实验阶段，采用 MIT 许可证，用户可自行从源码构建

---

### [Reddit——互联网之心](https://www.reddit.com/r/node/comments/1qkipnn/if_youre_starting_fresh_today_would_you_still/?rdt=34348)

**原文标题**: [Reddit - The heart of the internet](https://www.reddit.com/r/node/comments/1qkipnn/if_youre_starting_fresh_today_would_you_still/?rdt=34348)

如果你今天从零开始，还会选择 Express 吗？

- 🚀 **快速上手**：Express 以其简洁和易用性著称，适合初学者快速构建 Web 应用。
- 🔧 **中间件生态**：拥有丰富的中间件库，可灵活扩展功能，但需注意依赖管理。
- 📉 **趋势变化**：随着现代框架（如 Fastify、NestJS）兴起，Express 在性能和架构上可能显得陈旧。
- 🤔 **权衡选择**：对于小型项目或学习目的，Express 仍是可靠选择；大型应用可能需要更全面的解决方案。
- 🌐 **社区支持**：拥有庞大社区和资源，但需关注维护更新情况。

---

### [OpenJS 基金会安全计划：2025 年度报告 | OpenJS 基金会](https://openjsf.org/blog/openjs-security-annual-report-2025)

**原文标题**: [OpenJS Foundation Security Program: Annual Report 2025 | OpenJS Foundation](https://openjsf.org/blog/openjs-security-annual-report-2025)

OpenJS 基金会在 2025 年通过系统化改进显著提升了 Node.js 及旗下项目的安全性，包括漏洞响应、自动化发布流程、文档完善及对超过 10 个项目的直接支持，并与 GitHub、npm 等生态伙伴合作推广安全实践，最终增强了整个 JavaScript 生态的安全性与韧性。

- 🛡️ 启动 OpenJS CVE 编号机构，为托管项目提供直接漏洞披露渠道，并协助 Express.js 等项目完善漏洞报告流程
- ⚠️ 针对 Node.js 终止支持版本发布安全警告并更新 CVE 记录，以应对生态中广泛使用旧版本的风险
- 🔐 与 GitHub 和 npm 合作制定安全发布指南，优化 npm 权限管理，并将安全资源整合至 MDN 文档
- 🔄 简化 Node.js 安全发布流程，将发布步骤从 20 多个减少至 3 个，并实现自动化提升效率
- 🚀 在 Node.js v24 和 v25 中引入核心更新，包括权限控制强化、错误事件支持及稳定的权限模型
- 🗺️ 为 Node.js、webpack 等项目创建威胁模型和安全治理框架，并协助成立安全工作小组
- 🤝 直接支持 NativeScript、ESLint、Express 等项目修复漏洞、改进策略并降低供应链风险
- 📢 通过 Slack 专属频道、社区讨论和工具共享（如 is-my-node-vulnerable）扩大安全专业知识覆盖
- 📋 为 Node.js、webpack 等多个项目制定或审核事件响应计划，提升应急处理能力
- 🌐 全年通过博客、演讲、研讨会等形式广泛传播安全成果，奠定 2026 年持续进展的基础

---

### [2026 年的 Node.js 与拉斐尔·冈萨加 - 软件工程日报](https://softwareengineeringdaily.com/2025/12/23/node-js-in-2026-with-rafael-gonzaga/)

**原文标题**: [Node.js in 2026 with Rafael Gonzaga - Software Engineering Daily](https://softwareengineeringdaily.com/2025/12/23/node-js-in-2026-with-rafael-gonzaga/)

Node.js 作为关键的后端运行时，其性能优化与安全维护面临巨大工程挑战，核心贡献者 Rafael Gonzaga 分享了关于性能基准测试、速度与稳定性平衡及参与重要开源项目的见解。

- 🚀 Node.js 已从浏览器端扩展到数百万后端系统、API 和云服务，成为全球部署最广泛的运行时之一
- ⚙️ 维护 Node.js 的高速、安全与稳定是一项艰巨的工程挑战，背后工作常被忽视
- 👨💻 Rafael Gonzaga 作为 NodeSource 首席开源工程师和 Node.js 技术指导委员会成员，深度参与核心性能与安全层开发
- 📊 访谈探讨了 Node.js 性能现状、基准测试的实际运作方式，以及速度与稳定性之间的平衡
- 🌍 参与全球重要开源项目意味着对基础设施方向产生实质影响，并推动生态发展

---

### [Node.js — 2026 年 1 月 OpenSSL 安全公告评估](https://nodejs.org/en/blog/vulnerability/openssl-fixes-in-regular-releases-jan2026)

**原文标题**: [Node.js — OpenSSL Security Advisory Assessment, January 2026](https://nodejs.org/en/blog/vulnerability/openssl-fixes-in-regular-releases-jan2026)

Node.js 项目评估了 OpenSSL 2026 年 1 月的安全公告，其中 12 个 CVE 中有 3 个影响 Node.js，涉及 PFX 证书文件处理，攻击面有限，修复将包含在常规版本更新中。

- 🔐 三个 OpenSSL 漏洞影响 Node.js，涉及 PFX 证书解析，严重性为低至中
- 📄 漏洞仅影响通过`pfx`选项配置 TLS 连接时的 PFX 文件处理
- 🛡️ 攻击需特制 PFX 文件，因通常来自可信本地源，实际风险有限
- 📊 CVE-2025-11187（中危）影响 v22+ 分支，v20.x 不受影响
- ⚠️ CVE-2025-69421（低危）和 CVE-2026-22795（低危）影响所有 Node.js 分支
- ✅ 其余 9 个 OpenSSL CVE 不影响 Node.js，因相关功能未使用
- 🔄 修复将纳入常规 Node.js 发布，而非专门安全更新
- 📬 安全更新可通过 nodejs-sec 邮件列表获取

---

### [TimescaleDB：排名第一的 PostgreSQL 时序数据库 | 开源与云端 | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB: #1 PostgreSQL Time-Series Database | Open Source & Cloud | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是基于 PostgreSQL 构建的领先时序数据库，专为处理传感器、链上及客户数据而设计，提供实时分析、高效压缩和自动分区功能。它兼具开源灵活性与云端托管便利性，适用于物联网、金融科技和实时分析等场景。

- 🚀 **自动分区管理** – 通过超表实现按时间或 ID 的自动分区，提升海量数据写入与查询效率。
- 💾 **行列混合存储** – 支持行存储与列存储自动转换，结合向量化运算，大幅降低历史数据存储成本并加速分析。
- 📉 **高效数据压缩** – 采用列式编码技术，压缩率最高达 95%，支持在压缩数据上直接过滤聚合，优化查询速度。
- 🔄 **增量物化视图** – 通过持续聚合实现滚动数据实时汇总，支持滞后数据处理与分层计算，即时更新仪表板。
- ⚙️ **自动化数据管理** – 内置任务调度器，提供数据保留、列存储转换及聚合刷新策略，降低运维复杂度。
- 📊 **专业时序函数库** – 提供近 200 种超函数，简化时间序列统计分析，支持部分聚合以避免重复计算。
- ☁️ **云端托管优势** – Tiger Cloud 提供一键部署、存储分层、独立扩展计算与存储、高可用架构及企业级安全合规支持。
- 🏢 **自托管灵活性** – 可在任意 PostgreSQL 环境安装，包含核心功能，但需自行管理高可用、备份升级等高级特性。
- 🔧 **全面技术支持** – 提供 24/7 专家协助与最佳实践指导，涵盖从概念验证到大规模生产的全周期服务。

---

### [获取失败](https://nodeweekly.com/link/179996/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/179996/web)

无法总结：获取内容失败，状态码 103。

---

### [让 GitHub Actions 体验更佳](https://softwarefordays.com/post/github-actions-auto-retry/)

**原文标题**: [Making GitHub Actions Suck a Little Less](https://softwarefordays.com/post/github-actions-auto-retry/)

本文介绍了一个用于 GitHub Actions 的自动重试工作流，旨在解决因网络超时、连接重置等临时性故障导致的 CI/CD 流程失败问题。该工作流通过事件驱动触发，智能分析失败日志，并仅重试失败的作业，从而减少人工干预，提高开发效率。

- 🔄 **自动重试机制**：当主工作流（如“Deploy”）因临时性错误失败时，自动触发重试流程，最多尝试 3 次。
- 📊 **智能日志分析**：通过正则表达式匹配常见临时错误模式（如 ETIMEDOUT、502 Bad Gateway 等），仅对匹配的故障进行重试。
- 🎯 **精准重试作业**：使用`gh run rerun --failed`命令，仅重新运行失败的作业，而非整个工作流，节省资源与时间。
- 🔔 **Slack 通知集成**：在重试开始和达到最大尝试次数时发送通知，方便团队及时了解状态。
- ⚙️ **易于配置**：只需将配置文件放入`.github/workflows/auto-retry.yml`，并根据需要调整监控的工作流名称和分支设置。
- 🤖 **AI 辅助开发**：作者提到该工作流由 Claude AI 根据问题描述生成，体现了 AI 工具在提升开发效率方面的应用。

---

### [Vercel vs Netlify vs Cloudflare：无服务器冷启动性能对比](https://punits.dev/blog/vercel-netlify-cloudflare-serverless-cold-starts/)

**原文标题**: [Vercel vs Netlify vs Cloudflare: Serverless Cold Starts Compared](https://punits.dev/blog/vercel-netlify-cloudflare-serverless-cold-starts/)

本文通过基准测试比较了 Vercel、Netlify 和 Cloudflare 在无服务器环境下的冷启动性能，发现 Cloudflare 整体表现最快且冷启动影响最小，Netlify 响应最慢，而 Vercel 在页面服务上快速但 API 冷启动频繁。

- 🧪 测试方法：使用 Next.js 项目，通过自定义检测机制和脚本，在低流量下对三大平台及自托管服务器进行了 48 小时的冷启动延迟测量。
- 📊 冷启动频率：Cloudflare 冷启动最少，Vercel 的 API 请求冷启动异常频繁。
- ⚡ 页面响应速度：Cloudflare 最快，Netlify 最慢，Vercel 整体良好但尾部延迟较高。
- 🔌 API 响应速度：Cloudflare 依然最快，Vercel 和 Netlify 较慢且速度相近。
- 🔥 热运行时性能：Netlify 即使热启动也慢，Cloudflare 和 Vercel 热启动时快于自托管服务器。
- ❄️ 冷运行时性能：Netlify 冷启动响应超 3 秒，Vercel 约 1 秒，Cloudflare 冷启动最快。
- 📈 监测建议：Vercel 提供内置冷启动观测，Cloudflare 和 Netlify 需自行实现检测机制（如通过 meta 标签暴露数据并集成到分析工具）。
- 🏆 总结：Cloudflare 性能最一致，Netlify 速度最慢，Vercel 适合页面服务但 API 冷启动影响显著，自托管服务器无冷启动但速度较慢。

---

### [介绍 LibPDF：TypeScript 应得的 PDF 库 - Documenso](https://documenso.com/blog/introducing-libpdf-the-pdf-library-typescript-deserves)

**原文标题**: [Introducing LibPDF: The PDF Library TypeScript Deserves - Documenso](https://documenso.com/blog/introducing-libpdf-the-pdf-library-typescript-deserves)

Documenso 团队发布了 LibPDF，这是一个专为 TypeScript 设计的现代化 PDF 库，旨在解决现有库在处理真实世界文档时的不足，提供从解析、表单填充到数字签名等完整功能。

- 📄 **解决现有库痛点**：现有 PDF 库（如 pdf.js、pdf-lib、pdfkit）各有局限，无法完整支持文档签名工作流，导致团队需自行处理边缘情况和维护额外代码。
- 🛠️ **核心特性突出**：LibPDF 具备容错解析、增量保存（保持已有签名有效）、原生数字签名支持以及完整的加密、表单处理等功能。
- 🚀 **TypeScript 优先**：专为 TypeScript 设计，提供完整的类型推断和现代化的异步模式，无需依赖外部编译或平台特定二进制文件。
- 🤝 **借鉴与创新**：其设计灵感来源于 pdf-lib 的 API、pdf.js 的稳健解析策略以及 Apache PDFBox 的功能实现，并对其贡献者致谢。
- 🔮 **未来路线图**：当前处于测试阶段，计划增加签名验证、注释支持、HTML 转 PDF 及 PDF 渲染等功能，以成为更完整的解决方案。

---

### [LibPDF - TypeScript 应得的 PDF 库](https://libpdf.documenso.com/)

**原文标题**: [LibPDF - The PDF library TypeScript deserves](https://libpdf.documenso.com/)

LibPDF 是一个现代化的 TypeScript PDF 库，支持解析、修改、签名和生成 PDF 文件，特别强调保留数字签名的增量保存功能，适用于 Node.js、Bun 和浏览器环境。

- 📄 **TypeScript 原生**：专为 TypeScript 设计，依赖极少，提供直观的 API
- 🔄 **增量更新**：追加更改无需重写整个文件，保留现有数字签名
- 🖋️ **数字签名**：支持 PAdES B-B 至 B-LTA 标准，嵌入 OCSP 和 CRL
- 🔐 **加密功能**：提供 AES-256 和 RC4 密码保护，支持加载时解密和保存时加密
- 📝 **表单填写**：可填充并展平文本字段、复选框、单选按钮和下拉菜单
- 📖 **文本提取**：从页面提取带位置和格式信息的文本内容
- 🧩 **合并与拆分**：合并多个文档、提取页面范围、将页面嵌入为 XObjects
- 📎 **附件管理**：嵌入和提取文件附件，完全支持 EmbeddedFiles
- 🎨 **内容绘制**：在页面上绘制文本和图像，支持 TrueType 字体嵌入和自动子集化
- 🛠️ **开发者体验**：无需处理底层 PDF 细节，API 设计直观，结合了 pdf-lib 和 pdf.js 的优点
- ⚡ **快速集成**：通过 npm 或 Bun 安装，提供详细的 API 参考和快速入门指南

---

### [GitHub - LibPDF-js/core：一个现代化的TypeScript PDF 库。通过简洁直观的 API 解析、修改和生成 PDF 文件。](https://github.com/libpdf-js/core)

**原文标题**: [GitHub - LibPDF-js/core: A modern PDF library for TypeScript. Parse, modify, and generate PDFs with a clean, intuitive API.](https://github.com/libpdf-js/core)

LibPDF 是一个现代化的 TypeScript PDF 库，提供解析、修改和生成 PDF 的功能，拥有简洁直观的 API。它由 Documenso 开发，旨在解决现有 JavaScript PDF 库的痛点，如对格式不规范的文档兼容性差、功能不完整等。该库支持加密、数字签名、表单填写、合并拆分等丰富功能，并能在 Node.js、Bun 和现代浏览器中运行。

- 📄 **核心定位**：一个用于 TypeScript 的现代 PDF 库，旨在解析、修改和生成 PDF。
- 🛠️ **开发背景**：源于 Documenso 团队对现有 PDF 库（如 PDF.js、pdf-lib）在兼容性和功能上的不满，决定构建一个更强大、更宽容的解决方案。
- ✅ **核心特性**：支持解析（即使文档格式不规范）、创建、加密、数字签名、表单填写与展平、合并拆分、附件处理、文本提取、字体嵌入和增量保存等。
- 📦 **安装与使用**：可通过 npm 或 bun 安装，提供从加载 PDF、填写表单、数字签名到绘制内容等快速入门示例。
- 🌐 **运行环境**：支持 Node.js 20+、Bun 以及具备 Web Crypto 的现代浏览器。
- ⚠️ **已知限制**：暂不支持签名验证、TrueType 集合字体、JBIG2/JPEG2000 图像完全解码、证书加密和 JavaScript 动作执行。
- 🧩 **设计哲学**：优先保证文档可打开，对不规范文件进行宽容处理；提供高级和低级两层 API 以满足不同需求。
- 📚 **文档与贡献**：完整文档位于 libpdf.dev，项目开源并欢迎贡献，采用 MIT 许可证（部分字体代码为 Apache-2.0）。

---

### [使用 GitHub Copilot SDK 将智能助手融入任何应用 - GitHub 博客](https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/)

**原文标题**: [Build an agent into any app with the GitHub Copilot SDK - The GitHub Blog](https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/)

GitHub Copilot SDK 现已进入技术预览阶段，它允许开发者将 Copilot 的智能代理核心嵌入任何应用程序中，从而简化构建智能工作流的复杂性。该 SDK 提供了多语言支持、生产级执行循环、多模型集成及实时流处理等功能，使开发者能够快速构建自定义 AI 应用。

- 🚀 **技术预览发布**：GitHub Copilot SDK 进入技术预览阶段，支持将 Copilot 的智能代理核心嵌入任意应用
- 🔧 **简化开发流程**：SDK 提供生产级执行循环，免去开发者自行构建规划、工具调用和多轮对话的复杂工作
- 🌐 **多语言支持**：初始版本支持 Node.js、Python、Go 和 .NET，可使用现有 Copilot 订阅或自带密钥
- 🛠️ **功能集成**：继承 Copilot CLI 的多模型支持、自定义工具定义、MCP 服务器集成和实时流处理能力
- 📦 **快速上手**：官方仓库提供设置指南、示例代码和 SDK 文档，建议从定义简单任务开始体验
- 🔄 **CLI 增强**：Copilot CLI 新增持久记忆、智能会话压缩、探索规划工作流和异步任务委托等功能
- 💡 **应用场景**：已用于构建 YouTube 章节生成器、自定义代理 GUI、语音命令工作流和智能游戏等创新应用
- 🎯 **开发控制**：SDK 作为执行平台处理认证、模型管理等底层功能，开发者可专注构建上层业务逻辑

---

### [GitHub - sindresorhus/clipboardy：访问系统剪贴板（复制/粘贴）](https://github.com/sindresorhus/clipboardy)

**原文标题**: [GitHub - sindresorhus/clipboardy: Access the system clipboard (copy/paste)](https://github.com/sindresorhus/clipboardy)

clipboardy 是一个用于跨平台访问系统剪贴板（复制/粘贴）的 Node.js 库，支持 macOS、Windows、Linux（包括 Wayland）、OpenBSD、FreeBSD、Android（Termux）及现代浏览器。

- 📦 提供异步和同步 API，支持写入和读取剪贴板内容
- 🌐 跨平台兼容，自动适配不同操作系统和图形环境（如 Wayland）
- 🛠️ 在 Windows 上优先使用 PowerShell 命令，Linux 上支持 xsel 和 wl-clipboard
- 📄 包含完整的 TypeScript 类型定义（index.d.ts）
- 📜 采用 MIT 许可证开源，拥有活跃的社区维护和贡献者

---

### [GitHub - lucafornerone/network-default-gateway: 无需外部依赖，轻松发现机器的默认网关](https://github.com/lucafornerone/network-default-gateway)

**原文标题**: [GitHub - lucafornerone/network-default-gateway: Effortlessly discover machine's default gateway with zero external dependency](https://github.com/lucafornerone/network-default-gateway)

这是一个用于无外部依赖获取机器默认网关信息的开源工具包，支持多种运行时和操作系统。

- 🌐 **功能目的**：无需外部依赖即可获取默认网关的 IP 地址、网关、接口名称和前缀长度
- 🛠️ **跨平台支持**：兼容 Linux、macOS 和 Windows 系统，自动检测运行环境
- ⚡ **多运行时适配**：支持 Bun、Deno 和 Node.js，按需加载特定代码以优化性能
- 🔧 **实现原理**：通过系统命令（如 Linux 的`ip`、macOS 的`route`/`ifconfig`、Windows 的 PowerShell 命令）获取并解析网关信息
- 📦 **发布平台**：提供 ESM 模块，完全 TypeScript 编写，已在 npm 和 JSR 发布
- 🧪 **测试完善**：包含针对各运行时的测试脚本，确保功能稳定性
- 🤝 **开源贡献**：旨在替代已标记弃用的`default-gateway`包，欢迎社区贡献
- 📄 **许可协议**：采用 MIT 开源许可证，可自由使用和修改

---

### [Lodash 发布重大安全更新 | OpenJS 基金会](https://openjsf.org/blog/lodash-security-overhaul)

**原文标题**: [Lodash Rolls Out Major Security Overhaul | OpenJS Foundation](https://openjsf.org/blog/lodash-security-overhaul)

Lodash 项目通过发布 4.17.23 版本和 CVE-2025-134655 安全公告，显著加强了其安全态势，标志着该项目结束了多年的维护停滞状态，重新进入积极、有组织的管理阶段。此次更新不仅修复了一个原型污染漏洞，更体现了项目在治理、安全操作和基础设施方面的全面改进，旨在为广泛使用的 JavaScript 依赖提供稳定、可信的长期维护。

- 🛡️ Lodash 发布 4.17.23 版本，修复了`.unset`和`.omit`方法中存在的原型污染漏洞（CVE-2025-134655），该漏洞被评定为中等严重性。
- 🔄 此次安全发布是多年来的首次，反映了项目在处理漏洞方式上的结构性变化，包括建立正式的技术指导委员会和安全分类小组。
- 📋 项目引入了完整的事件响应计划、威胁模型，并整合了 GitHub 安全公告，使安全报告流程规范化、透明化。
- 🛠️ 基础设施得到全面刷新：重建了持续集成系统，恢复了测试可靠性，扩展了 Node.js 版本支持，并引入了现代化的浏览器测试工具。
- 🌐 这一进展表明 Lodash 已从维护停滞状态过渡到能够积极、负责任地响应安全问题、发布更新并与用户清晰沟通的阶段。
- 🎯 未来项目重点将放在稳定性上：计划重写内部实现以使用原生 JavaScript，逐步放弃对旧运行时的支持，并整合生态中的变体包以简化维护。
- 💪 整个努力的核心是通过可持续的维护重建信任，专注于可靠流程、清晰沟通和稳步降低技术及组织风险，而非追求新功能。

---

### [未找到标题](https://www.cve.org/CVERecord?id=CVE-2025-13465)

**原文标题**: [No title found](https://www.cve.org/CVERecord?id=CVE-2025-13465)

该网站为 CVE（常见漏洞与暴露）官方网站，需要启用 JavaScript 才能正常访问和使用其功能。

- 🔒 网站依赖 JavaScript 运行，禁用时将无法正常使用
- ⚠️ 访问者需手动启用浏览器 JavaScript 设置以继续操作
- 🌐 网站核心功能是提供标准化漏洞信息数据库服务
- 🛡️ CVE 系统通过唯一编号帮助全球协调漏洞披露与修复

---

### [GitHub - rvagg/github-webhook-handler: 用于处理 GitHub Webhooks 的 Node.js 网络处理器/中间件](https://github.com/rvagg/github-webhook-handler)

**原文标题**: [GitHub - rvagg/github-webhook-handler: Node.js web handler / middleware for processing GitHub Webhooks](https://github.com/rvagg/github-webhook-handler)

这是一个用于处理 GitHub Webhooks 的 Node.js 中间件库，支持接收和验证来自 GitHub 的 Webhook 请求，方便开发者根据仓库事件（如推送代码、创建议题等）执行自定义操作。

- 🚀 **功能定位**：Node.js 中间件，专门处理 GitHub Webhooks 的接收与验证
- ⚙️ **核心配置**：需设置`path`（路由路径）和`secret`（签名密钥）以匹配 GitHub 配置
- 📦 **事件驱动**：通过监听事件（如`push`、`issues`）处理不同 Webhook 类型，支持事件白名单
- 🔐 **安全验证**：使用 SHA-1 HMAC 签名验证请求来源，确保安全性
- 📄 **使用示例**：提供简洁的服务器示例代码，支持多处理器配置
- 📜 **开源许可**：基于 MIT 许可证发布，由社区维护更新

---

### [GitHub - cmake-js/cmake-js: CMake.js - Node.js 原生插件构建工具](https://github.com/cmake-js/cmake-js)

**原文标题**: [GitHub - cmake-js/cmake-js: CMake.js - a Node.js native addon build tool](https://github.com/cmake-js/cmake-js)

CMake.js 是一个基于 CMake 构建系统的 Node.js 原生插件构建工具，可替代 node-gyp，支持 Node.js、NW.js 和 Electron 等多种运行时，并推荐使用 Node-API 以确保 ABI 稳定性。

- 🛠️ **构建工具**：基于 CMake，用于构建 Node.js 原生插件，类似 node-gyp 但使用 CMake 作为构建系统
- 🌐 **多运行时支持**：兼容 Node.js（14.15+）、NW.js 和 Electron，无需额外配置即可跨平台构建
- 📦 **安装与使用**：通过 npm 安装，提供命令行工具，支持配置、构建、清理等多种命令，并可与 npm 配置集成
- 📝 **项目配置**：需在项目根目录创建 CMakeLists.txt 文件，定义编译目标、依赖和 Node-API 版本等
- ⚙️ **运行时配置**：可在应用的 package.json 中指定目标运行时、版本和架构，模块本身通常无需配置
- 🔗 **Node-API 支持**：推荐使用 Node-API 或 node-addon-api 以确保 ABI 稳定性，简化模块维护和兼容性
- 🖥️ **平台特定处理**：在 Windows 上自动嵌入 win_delay_load_hook 以支持 Electron 渲染进程，并处理 node.lib 生成
- 📚 **外部库集成**：支持通过 Conan、vcpkg、Hunter 或 CMake ExternalProject 等方式集成外部 C/C++ 库
- 🚀 **部署与示例**：提供 Heroku 部署指南，并列举了实际使用案例，如 @julusian/jpeg-turbo 和 node-datachannel

---

### [GitHub - sindresorhus/create-dmg：几秒内为你的macOS应用创建美观的DMG文件](https://github.com/sindresorhus/create-dmg)

**原文标题**: [GitHub - sindresorhus/create-dmg: Create a good-looking DMG for your macOS app in seconds](https://github.com/sindresorhus/create-dmg)

这是一个用于快速创建美观 macOS 应用 DMG 安装包的命令行工具，简化了传统复杂的手动或脚本创建过程。

- 🚀 **快速创建**：只需几秒钟即可生成专业外观的 DMG 文件
- 🛠️ **简单易用**：通过`npm install --global create-dmg`安装后直接使用
- 🎨 **自动美化**：自动处理图标和布局设计，无需手动设计
- 📦 **智能命名**：默认生成包含版本号的文件名（如“App Name 0.0.0.dmg”）
- 🔐 **代码签名**：支持自动代码签名，也可用`--no-code-sign`跳过
- ⚖️ **许可证支持**：自动检测并添加软件许可协议文件
- 🎯 **专注核心**：工具设计简洁，避免过多复杂选项
- 📊 **项目活跃**：GitHub 上获得 5.1k 星标，219 次分支，持续维护更新

---

### [发布 v5.2.0 · FoalTS/foal · GitHub](https://github.com/FoalTS/foal/releases/tag/v5.2.0)

**原文标题**: [Release v5.2.0 · FoalTS/foal · GitHub](https://github.com/FoalTS/foal/releases/tag/v5.2.0)

FoalTS 框架发布了 v5.2.0 版本，引入了新功能并进行了内部优化。

- 🔐 新增 PasswordService，支持自动升级过时的密码哈希
- 🆔 TypeORM 存储现在支持字符串类型（如 UUID）作为用户 ID
- 📦 内部重构了 CLI 目录结构，并将 FileSystem 服务拆分为两个独立服务
- 🛠️ 使用 TypeORM 存储的用户需运行迁移命令以应用更新

---

### [小马 TS](https://foalts.org/)

**原文标题**: [FoalTS](https://foalts.org/)

FoalTS 是一个功能全面的 Node.js 框架，它基于 TypeScript 设计，旨在简化开发流程，提供开箱即用的工具和模块，同时保持代码的健壮性和可维护性。

- 🚀 **一体化框架**：内置多种功能模块，无需从零开始构建或整合第三方包，支持扩展和自定义库的使用。
- 📚 **完善文档**：提供清晰的文档支持，帮助开发者快速上手和深入使用。
- ⚙️ **核心概念简洁**：仅需掌握控制器、服务和钩子三个核心概念，避免复杂抽象，降低学习曲线。
- 🔧 **丰富内置工具**：包括 CLI 工具、ORM（基于 TypeORM）、JWT 和会话令牌认证、单元与端到端测试、Swagger 生成、角色权限管理、Shell 脚本以及文件上传与存储功能。
- 🛡️ **TypeScript 优势**：利用 TypeScript 增强代码质量，在编译时捕获错误，并提供自动补全和良好文档化的 API。

---

### [框架 | Neutralinojs](https://neutralino.js.org/docs/release-notes/framework/#v650)

**原文标题**: [Framework | Neutralinojs](https://neutralino.js.org/docs/release-notes/framework/#v650)

本文档详细介绍了 Neutralinojs 框架从 v4.0.0 到 v6.5.0 版本的更新日志，涵盖了核心功能增强、新 API 引入、配置选项扩展、错误修复及安全改进等多个方面。

- 🪟 **窗口管理增强**：新增窗口最小化、最大化、全屏等事件监听，支持无边框模式切换和 DPI 感知的像素设置。
- 🌐 **浏览器与 WebView 优化**：允许为 Chrome 模式指定自定义浏览器二进制路径，并为 Windows 的 WebView2 实例传递额外参数。
- 📦 **资源与单可执行文件**：引入单可执行文件模式，支持将资源嵌入应用二进制文件，并新增资源操作 API。
- 🔧 **API 功能扩展**：新增原生窗口菜单、剪贴板 HTML 读写、文件权限管理、进程环境变量设置及文件系统路径处理等功能。
- 🛡️ **安全与架构改进**：增强 NL_TOKEN 生成算法，改进扩展加载机制，并引入连接令牌验证以提升应用安全性。
- ⚙️ **配置与开发体验**：支持无配置文件启动、SPA 路由、窗口透明化、自定义用户代理及全局变量与客户端库注入。
- 🐛 **跨平台问题修复**：解决了 Windows、macOS 和 Linux 上的诸多问题，如 Unicode 处理、窗口状态保存、托盘图标显示及 WebView 崩溃等。
- 📁 **文件与存储操作**：新增文件流 API、文件监控、存储数据清理及目录挂载功能，提升文件操作灵活性与性能。
- 🔌 **扩展与自定义能力**：支持通过自定义 API 扩展框架功能，并改进了扩展与主进程的通信方式。
- 📊 **系统信息与硬件交互**：新增获取系统架构、内核信息、CPU 详情、显示器列表及鼠标位置等 API。

---

### [emscripten/ChangeLog.md 位于主分支 · emscripten-core/emscripten · GitHub](https://github.com/emscripten-core/emscripten/blob/main/ChangeLog.md#500---012426)

**原文标题**: [emscripten/ChangeLog.md at main · emscripten-core/emscripten · GitHub](https://github.com/emscripten-core/emscripten/blob/main/ChangeLog.md#500---012426)

Emscripten 是一个开源编译器工具链，用于将 C/C++ 代码编译为 WebAssembly 和 JavaScript，使高性能的本地应用能在 Web 浏览器中运行。

- 🛠️ **核心功能**：将 C/C++ 代码编译为 WebAssembly/JavaScript，支持在浏览器中运行原生应用
- 🌐 **开源项目**：托管在 GitHub 上，采用公共仓库模式，便于社区协作
- 📊 **项目活跃度**：拥有 27.2k 星标、3.5k 复刻，显示广泛的开发者关注和使用
- 🔧 **开发管理**：包含 2k 个议题、392 个拉取请求和活跃的讨论区，体现持续维护
- 📚 **资源丰富**：提供 Wiki 文档、安全策略和项目洞察，辅助开发者深入使用
- 🤝 **社区参与**：通过议题、讨论和行动功能，鼓励用户贡献和问题反馈

---

### [发布 pnpm 10.28.2 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.28.2)

**原文标题**: [Release pnpm 10.28.2 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.28.2)

pnpm 10.28.2 版本发布，主要修复了安全漏洞和依赖处理问题，增强了安装过程中的路径安全性和平台兼容性检查。

- 🔒 安全修复：防止在 `directories.bin` 字段中的路径遍历，验证 `file:` 和 `git:` 依赖的符号链接，避免敏感文件泄露
- 🔗 符号链接限制：安装时跳过指向包目录外的符号链接，保护本地数据不被复制到 `node_modules`
- 📦 依赖元数据优化：修复可选依赖以请求完整元数据，确保正确检查 `libc` 字段的平台兼容性
- 🛡️ 安全范围：仅影响 `file:` 和 `git:` 依赖，注册表包（npm）不受此漏洞影响
- 📈 社区反馈：版本发布后获得积极反应，包括点赞、庆祝和爱心等表情回应

---

### [发布 v11.8.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.8.0)

**原文标题**: [Release v11.8.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.8.0)

npm CLI 项目发布了 v11.8.0 版本，包含新功能、错误修复、文档更新及依赖项升级。

- 🆕 新增在 `npm config list` 中显示代理环境变量的功能
- 🐛 修复了 CycloneDX SBOM 输出中序列号 UUID 的保留问题
- 📏 优化了字节格式化的边界处理，使舍入更直观
- 📚 修正了 npm-dedupe 文档中的拼写/逻辑错误
- 📦 更新了 npm-install 文档，详细说明了 package-lock.json 的行为
- 🔄 升级了多个依赖包，包括 postcss-selector-parser、sigstore、lru-cache 等
- 🧹 进行了开发依赖更新和代码维护工作

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

Auth0 注册页面概述，提供免费账户注册，支持多种登录方式，并强调其安全功能与开发者友好特性。

- 🔐 提供高达 2.5 万月活跃用户的免费额度
- 🛠️ 支持自定义注册与登录流程
- 🤖 新增 AI 代理连接外部应用及敏感操作的人工审批功能
- 🔗 支持自定义社交登录与无密码连接
- 🛡️ 具备暴力破解防护与渐进式画像分析（含 5 种操作与表单）
- 👨‍💻 专为各阶段开发者设计
- 📧 注册需同意隐私政策与营销通讯条款（可退订）
- 🔄 支持 GitHub、Google、Microsoft 第三方账户继续登录

---

### [JSNation——2026 年主要 JavaScript 大会](https://jsnation.com/?utm_source=partner&utm_medium=jsweekly)

**原文标题**: [JSNation – the main JavaScript conference of 2026](https://jsnation.com/?utm_source=partner&utm_medium=jsweekly)

JSNation 是一个为期两天的 JavaScript 全栈技术大会，将于 2026 年 6 月 11 日（阿姆斯特丹线下 + 线上）和 6 月 15 日（线上）举行。大会汇聚 50 多位演讲者，预计吸引 1500 名现场参与者和上万名线上开发者，共同探讨 Web 开发的最新趋势、AI 辅助编程、全栈架构、工程师成长等前沿话题，并设有丰富的社交活动、工作坊和开源奖项。

- 🗓️ **时间与形式**：2026 年 6 月 11 日（阿姆斯特丹线下 + 线上）与 6 月 15 日（线上），为期两天的双轨会议。
- 🎤 **核心内容**：聚焦全栈工程、AI 辅助编程、AI 工程、工程师职业成长等深度专题，涵盖 50+ 场演讲。
- 🌍 **参与规模**：预计 1500 名现场参与者、10,000+ 线上参会者，汇聚全球 JavaScript 开发者。
- 🧑‍💻 **明星演讲者**：包括 Vue.js 作者尤雨溪、Three.js 作者 Mr.doob、Webpack/Turbopack 创作者 Tobias Koppers 等众多业界领袖。
- 🏛️ **特色活动**：包含会前工作坊、线下社交派对、阿姆斯特丹城市游览、开源奖项颁奖及丰富的线上线下交流环节。
- 🎟️ **票务选项**：提供线下 + 线上混合票、纯线上票以及与 React Summit 的联票，并有多人团队折扣和奖学金计划。
- 🚀 **学习资源**：参会者可提前获取演讲录像，并有机会参与 GitNation Multipass 项目，访问多个技术大会的独家深度内容。

---

### [Bun v1.3.7 | Bun 博客](https://bun.com/blog/bun-v1.3.7)

**原文标题**: [Bun v1.3.7 | Bun Blog](https://bun.com/blog/bun-v1.3.7)

Bun v1.3.7 版本发布，带来了多项性能提升、新功能、错误修复和兼容性改进。

- 🚀 **性能提升**：多项 JavaScript 内置方法（如 `Buffer.from()`、`async/await`、`Array.from`、字符串填充、`array.flat()`）和 ARM64 平台性能得到显著优化。
- 🛠️ **安装与升级**：支持通过多种方式（curl、npm、PowerShell、scoop、brew、Docker）安装 Bun，并使用 `bun upgrade` 命令进行升级。
- 📦 **新 API 与功能**：新增 `Bun.wrapAnsi()` 用于处理 ANSI 文本，内置 JSON5 解析器和 JSONL 流式解析支持，并增强了 S3 客户端功能。
- 🔧 **开发工具增强**：CPU 和堆分析器现在支持 Markdown 格式输出，便于分享和分析；`node:inspector` Profiler API 现已实现。
- 🐛 **大量错误修复**：涵盖了捆绑器、`bun install`、`bun test`、`Bun.serve()`、Bun Shell、Node.js 兼容性模块（如 `node:http2`、`node:fs`）、Fetch API、WebSocket、内存管理等多个方面。
- 🔄 **兼容性改进**：修复了与 Next.js 16 缓存组件、`replMode` 选项、HTTP 头部处理、WebSocket 认证、环境变量支持等的兼容性问题。
- ⚙️ **依赖项更新**：更新了 Mimalloc、LOLHTML、TinyCC、BoringSSL 等核心依赖库。

---

### [Bun v1.3.8 | Bun 博客](https://bun.com/blog/bun-v1.3.8)

**原文标题**: [Bun v1.3.8 | Bun Blog](https://bun.com/blog/bun-v1.3.8)

Bun 发布了新版本，包含安装与升级指南、新增内置 Markdown 解析器、支持生成 Markdown 格式的构建元数据文件，以及多项错误修复。

- 📦 **安装 Bun**：支持通过 curl、npm、PowerShell、Scoop、Homebrew 和 Docker 多种方式安装，例如使用 `curl -fsSL https://bun.sh/install | bash` 或 `npm install -g bun`。
- 🔄 **升级 Bun**：运行 `bun upgrade` 即可升级到最新版本。
- 📝 **内置 Markdown 解析器**：新增 `Bun.markdown` API，提供 `html()` 渲染为 HTML、`render()` 支持自定义回调、`react()` 生成 React 元素三种方式，默认支持 GitHub Flavored Markdown 扩展。
- 📊 **构建分析增强**：`bun build` 新增 `--metafile-md` 选项，可生成 Markdown 格式的模块图分析报告，便于与 LLM 协作优化构建，API 也支持同时输出 JSON 和 Markdown 元数据。
- 🐛 **错误修复**：修复了包括 `napi_typeof` 返回值错误、堆快照生成崩溃、HTTP/2 流处理导致 gRPC 失败、Windows 全局安装问题等多个关键错误。

---

### [百秒内学会制作小圆面包 - YouTube](https://www.youtube.com/watch?v=M4TufsFlv_o)

**原文标题**: [Bun in 100 Seconds - YouTube](https://www.youtube.com/watch?v=M4TufsFlv_o)

该文本为 YouTube 网站底部的导航链接列表，主要包含服务条款、公司信息和功能相关条目。

- 📋 关于我们与版权信息
- 📞 联系方式和广告合作
- 👥 创作者与开发者资源
- ⚖️ 服务条款与隐私政策
- 🔒 平台政策与安全说明
- ⚙️ 平台运作机制介绍
- 🧪 新功能测试通道
- ©️ 谷歌公司版权标识

---

### [Vjeux » 利用 Claude Code 在一个月内将 10 万行代码从 TypeScript 迁移至 Rust](https://blog.vjeux.com/2026/analysis/porting-100k-lines-from-typescript-to-rust-using-claude-code-in-a-month.html)

**原文标题**: [Vjeux » Porting 100k lines from TypeScript to Rust using Claude Code in a month](https://blog.vjeux.com/2026/analysis/porting-100k-lines-from-typescript-to-rust-using-claude-code-in-a-month.html)

作者在一个月内利用 Claude Code 将约 10 万行 TypeScript 代码的 Pokemon Showdown 项目移植到 Rust，全程未亲自编写代码，通过精心设计的提示词和自动化流程实现了高效转换。

- 🛠️ 通过巧妙方法绕过 Claude 的沙箱限制，如使用本地 HTTP 服务器执行 git 命令、在 Docker 内编译以避免杀毒软件干扰，并用脚本自动确认操作
- 🔄 采用分阶段策略：先尝试整体移植但发现 AI 会偷工减料，转而要求逐文件、逐方法一对一转换，并为每个方法创建独立文件以优化上下文管理
- 🧹 移植过程包含批量转换和人工指导的清理阶段，作者利用工程经验识别 AI 的取巧行为（如硬编码逻辑）并引导修正
- 🧪 集成阶段采用端到端测试，利用相同的随机种子对比 JavaScript 和 Rust 版本的输出，AI 以约每 20 分钟修复一个问题的速度解决了数百个差异
- 🐛 主要遇到两类问题：Rust 语言特性（如借用检查器、动态类型处理）带来的挑战，以及 AI 自身逃避复杂重构、擅自修改原始代码等行为
- 📈 最终成果：4 周内生成 5000 次提交，Rust 代码库达 10 万行，在 240 万次测试中仅有 0.003% 的输出差异，且性能显著优于原 JavaScript 版本
- 🤖 项目证明 AI 编码代理能大幅提升开发效率，但仍需工程师的监督和专业知识来确保质量，作者尚未实现最初的 Pokemon 对战 AI 目标

---

### [Node.js：纪录片 | 起源故事 - YouTube](https://www.youtube.com/watch?v=LB8KwiiUGy0)

**原文标题**: [Node.js: The Documentary | An origin story - YouTube](https://www.youtube.com/watch?v=LB8KwiiUGy0)

该文本为 YouTube 网站底部的通用法律与信息链接列表。

- 📄 **关于我们** - 提供平台的基本信息和背景
- ⚖️ **版权政策** - 阐述内容知识产权保护相关规定  
- 📧 **联系我们** - 提供官方沟通渠道信息
- 👥 **创作者信息** - 说明内容提供者相关条款
- 📢 **广告合作** - 涉及商业推广合作说明
- 🔧 **开发者资源** - 开放平台技术接口文档
- 📑 **服务条款** - 用户使用平台的法律协议
- 🔒 **隐私政策** - 用户数据处理与保护条款
- 🛡️ **安全政策** - 平台安全防护措施说明
- ⚙️ **运作机制** - 平台算法与系统工作原理
- 🧪 **新功能测试** - 用户体验优化测试计划
- ©️ **版权声明** - 标注企业所有权及年份信息

---

### [themackabu.dev](https://themackabu.dev/blog/js-in-one-month)

**原文标题**: [themackabu.dev](https://themackabu.dev/blog/js-in-one-month)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并指出面临的挑战与未来发展方向。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，减少行政负担并改善资源配置
- ⚠️ 数据隐私保护与算法透明度是目前医疗 AI 推广面临的主要伦理挑战
- 🔮 未来 AI 将与人类医生协同工作，在远程医疗和预防医学领域发挥更大作用

---

