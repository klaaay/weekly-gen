### [Node 周刊第 603 期：2025 年 12 月 2 日](https://nodeweekly.com/issues/603)

**原文标题**: [Node Weekly Issue 603: December 2, 2025](https://nodeweekly.com/issues/603)

本期内容涵盖 Node.js 生态系统的最新动态，包括性能优化、工具更新、安全提醒及学习资源。

- 🚀 **Node.js 性能提升**：AWS Lambda 上 ARM64 架构比 x86 性能更优，Node 22 比 Node 20 快 8-11%，切换至 ARM64 是简单的性能优化方案。
- ⚠️ **安全更新提醒**：Express 发布 v5.2.1，紧急回退 v5.2.0 中可能导致应用崩溃的安全修复；v4.22 同步更新。
- 🛠️ **工具库新版本**：  
  - Tinybench 6.0：轻量级跨运行时基准测试库  
  - Chokidar 5.0：跨平台文件监听库（仅支持 ESM）  
  - Playwright 1.57：测试报告新增性能排序功能  
  - pnpm 10.24：自适应网络并发提升包下载速度
- 📦 **依赖管理可视化**：DepX 工具生成依赖数量徽章，可展示在项目文档中。
- 🔐 **证书有效期调整**：Let's Encrypt 将逐步把证书有效期从 90 天缩短至 45 天，需确保自动续签流程稳定。
- 🎓 **免费学习资源**：Piccalilli 团队开放《JavaScript 异步编程》章节免费阅读；Advent of Code 推出 12 天精简版编程挑战。
- 📄 **技术实践分享**：  
  - 使用 Claude Code 分析 Gmail 邮件的自动化方案  
  - HTTP 流式传输优化 TTFB 与用户体验  
  - OpenShift 4 中 cgroups v2 对 Node.js 的影响分析
- 🌐 **生态扩展**：Node.js 24 LTS 已在 Vercel 和 AWS Lambda 上线；Electron 项目进入维护者休整期；Prisma 7 发布完整功能解读。

---

### [GitHub - tinylibs/tinybench: 🔎 一个简单、小巧且轻量级的基准测试库！](https://github.com/tinylibs/tinybench)

**原文标题**: [GitHub - tinylibs/tinybench: 🔎 A simple, tiny and lightweight benchmarking library!](https://github.com/tinylibs/tinybench)

Tinybench 是一个简单、轻量级的 JavaScript 基准测试库，适用于多种运行时环境，提供精确的计时和统计分析功能。

- 🔎 **轻量级设计**：库体积小巧，仅约 10KB（压缩后约 2KB），无外部依赖。
- ⏱️ **精确计时**：基于 Web API（如 `performance.now` 或 `process.hrtime`）提供准确的时间测量。
- 📊 **统计分析**：支持延迟与吞吐量的统计分析，包括标准差、误差范围、方差和百分位数等。
- 🔄 **并发支持**：支持任务级别和基准测试级别的并发执行模式。
- 🎯 **事件驱动**：兼容 `Event` 和 `EventTarget`，可监听任务周期、中止等事件。
- 🤖 **自动异步检测**：能自动识别异步函数，也支持手动设置异步选项。
- 📈 **结果表格化**：提供 `bench.table()` 方法，可将结果转换为适合 `console.table()` 的格式。
- 💾 **样本保留**：可选择保留原始样本数据，便于进一步分析或可视化。
- ⏹️ **可中止测试**：支持通过 `AbortSignal` 在基准测试或任务级别中止执行。
- 🔧 **自定义时间戳**：允许使用不同的时间戳提供程序（如 `hrtime`、`performance.now` 或自定义实现）。

---

### [在 Kubernetes 中加速 Next.js](https://blog.platformatic.dev/93-faster-nextjs-in-your-kubernetes)

**原文标题**: [Accelerate Next.js in Kubernetes](https://blog.platformatic.dev/93-faster-nextjs-in-your-kubernetes)

本文探讨了在 Kubernetes 中运行 Next.js 应用时面临的性能挑战，并介绍了 Watt 解决方案如何通过利用 Linux 内核的 SO_REUSEPORT 特性，显著提升应用性能与可靠性。传统方法如 PM2 集群模块或单 CPU Pod 水平扩展存在协调开销与负载不均衡问题，而 Watt 通过零开销负载均衡、独立事件循环和外部健康监控，实现了 93.6% 的延迟降低与 99.8% 的成功率。

- 🚀 **性能大幅提升**：Watt 相比 PM2 和单 CPU Pod，在相同 CPU 资源下，中位延迟降低 93.6%，吞吐量提升 9.6%，成功率高达 99.8%。
- 🔧 **技术原理**：利用 Linux 内核的 SO_REUSEPORT 特性，实现零协调开销的连接分发，避免传统集群模块约 30% 的 IPC 性能损耗。
- ⚖️ **负载均衡优化**：通过内核级哈希分布连接，结合 Kubernetes 服务层，形成双层负载均衡，改善统计复用与容错特性。
- 🛡️ **健康监控与自愈**：Watt 从外部监控工作进程，能在事件循环阻塞前重启异常工作者，避免级联故障，提升系统可靠性。
- 📊 **生产级基准测试**：在 AWS EKS 上对 Next.js 进行实测，Watt 在持续 1000 请求/秒负载下，中位延迟仅 11.6 毫秒，P95 延迟 235 毫秒。
- 🔄 **部署简便**：Watt 开源且易于集成，支持从 PM2 或单 CPU Pod 架构平滑迁移，无需重大架构变更即可获得性能收益。
- 💡 **适用场景**：特别适用于 Next.js 等无法实现早期请求拒绝的 CPU 密集型框架，解决传统扩展方法在容器化环境中的根本缺陷。

---

### [GitHub - platformatic/platformatic: Platformatic 开源单体仓库！](https://github.com/platformatic/platformatic#readme)

**原文标题**: [GitHub - platformatic/platformatic: Platformatic Open Source monorepo!](https://github.com/platformatic/platformatic#readme)

Platformatic 是一个开源项目，提供名为 Watt 的 Node.js 应用服务器，旨在通过单一服务器统一处理数据库、API、前端框架和微服务，内置可观测性并支持零配置部署。

- 🚀 **快速启动**：通过简单命令可在 2 分钟内创建并运行首个 Watt 应用，自动生成 REST 和 GraphQL API。
- 🔧 **一体化服务**：在一个服务器中同时运行数据库 API、自定义服务、前端框架和 API 网关，架构可组合。
- 📊 **内置可观测性**：提供开箱即用的日志记录、指标、追踪和健康检查功能。
- ⚙️ **框架集成**：支持 Next.js、Astro、Remix、Vite、NestJS 及原生 Node.js。
- 🛡️ **生产就绪**：内置 Docker 部署、环境配置和扩展能力，适用于生产环境。
- 📘 **TypeScript 优先**：提供完整的类型安全，支持自动生成类型和 SDK。
- 📚 **学习路径灵活**：为 Node.js 新手、经验丰富的开发者和现有应用迁移者分别提供指导。
- 🌐 **支持与资源**：提供详细文档、社区 Discord、GitHub 问题反馈和企业级解决方案。

---

### [使用 Express 和 Node.js 构建 RESTful API、Postgres 数据库及 JWT 认证 | Frontend Masters](https://frontendmasters.com/courses/api-design-nodejs-v5/?utm_source=email&utm_medium=nodeweekly&utm_content=nodejsv5)

**原文标题**: [RESTful APIs, Postgres, and JWTs with Express and Node.js | Frontend Masters](https://frontendmasters.com/courses/api-design-nodejs-v5/?utm_source=email&utm_medium=nodeweekly&utm_content=nodejsv5)

这门课程由 Netflix 的 Scott Moss 主讲，专注于使用 Node.js 和 Express 构建可扩展的 API。课程涵盖 RESTful API 设计、Postgres 数据库迁移、JWT 身份验证、TypeScript 集成、Zod 运行时验证以及全面的集成测试策略。通过实际项目（习惯追踪 API），学员将学习从开发到生产部署的全流程。

- 🚀 使用 Node.js 和 Express 构建可扩展的 RESTful API
- 🔐 通过 JWT 实现安全的身份验证和授权
- 🗄️ 使用 Postgres 进行数据库设计、迁移和关系管理
- 📝 利用 TypeScript 和 Zod 确保类型安全和运行时验证
- 🧪 采用 Vitest 和 supertest 进行全面的集成测试
- 🌐 学习环境变量管理、中间件应用和错误处理最佳实践
- 🚢 完成从本地开发到 Render 平台的生产部署
- 📚 获得实际项目经验，涵盖路由设计、CRUD 操作和 API 安全

---

### [2025 年末多运行时环境下 AWS Lambda Arm64 与 x86_64 性能对比](https://chrisebert.net/comparing-aws-lambda-arm64-vs-x86_64-performance-across-multiple-runtimes-in-late-2025/)

**原文标题**: [Comparing AWS Lambda Arm64 vs x86_64 Performance Across Multiple Runtimes in Late 2025](https://chrisebert.net/comparing-aws-lambda-arm64-vs-x86_64-performance-across-multiple-runtimes-in-late-2025/)

2025 年末对 AWS Lambda 在 arm64 与 x86_64 架构上的性能进行了全面基准测试，涵盖 Node.js、Python 和 Rust 运行时，测试包括 CPU 密集型、内存密集型和轻量级工作负载。结果显示，arm64 架构在性能、成本和冷启动时间上普遍优于 x86_64，尤其是在启用平台特定优化后，优势更为显著。

- 🏆 **性能与成本优势**：arm64 在大多数场景下性能相当或更优，且计算成本低 20-40%，结合性能提升，整体效率更高。
- ⚡ **冷启动更快**：arm64 的初始化时间比 x86_64 快 13-24%，Rust 在 arm64 上的冷启动仅需 16 毫秒，适合延迟敏感应用。
- 🦀 **Rust 表现突出**：Rust 在 arm64 上综合性能最佳，尤其在 CPU 密集型任务中，通过启用汇编优化（如 SHA-256 的 NEON 指令），速度可达 x86 的 4-5 倍。
- 🐍 **Python 版本差异**：Python 3.11 在 arm64 上性能最优，比 3.12、3.13 和 3.14 快 9-15%，但内存密集型任务中 Python 表现波动较大。
- 🌐 **Node.js 升级收益**：Node.js 22 比 20 快 8-11%，结合切换到 arm64 架构，可带来约 18% 的免费性能提升。
- 💡 **工作负载建议**：CPU/内存密集型任务首选 Rust on arm64；I/O 密集型任务可任选运行时，重点优化成本；Python 和 Node.js 用户应优先使用 arm64 及最新稳定版本。
- 📊 **测试方法**：基准测试包括轻量（DynamoDB 操作）、CPU 密集型（SHA-256 哈希）和内存密集型（数组排序）工作负载，覆盖多种内存配置，通过大量调用收集热启动和冷启动数据。
- 🔧 **优化重要性**：性能受代码和库的硬件优化影响显著（如 arm 的 NEON 指令），建议确保关键依赖启用架构特定优化以最大化性能。

---

### [发布 v5.2.0 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v5.2.0)

**原文标题**: [Release v5.2.0 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v5.2.0)

Express.js 项目发布了 5.2.0 版本，主要包含安全修复、依赖更新、代码优化及多项改进，同时欢迎了多位新贡献者的加入。

- 🔒 修复了安全漏洞 CVE-2024-51999，并升级 body-parser 至 2.2.1 以应对 CVE-2025-13466
- 📦 更新了多项依赖，包括 GitHub Actions、CodeQL 及开发工具如 morgan 和 cookie-session
- 🛠️ 进行了代码重构和优化，如简化 acceptsLanguages 实现、使用 req.socket 替代已弃用的 req.connection
- 🧪 增加了测试覆盖范围，包括对 app.listen() 变体的测试，并更新了测试矩阵以支持 Node.js 24 和 25
- 📚 更新了文档和贡献指南，将部分文档移至讨论区，并修复了链接和示例
- 👥 新增了 11 位贡献者，并对项目管理和 CI/CD 流程进行了多项改进

---

### [发布：5.2.1 由 UlisesGascon 提交 · 拉取请求 #6933 · expressjs/express · GitHub](https://github.com/expressjs/express/pull/6933#issuecomment-3602268351)

**原文标题**: [Release: 5.2.1 by UlisesGascon · Pull Request #6933 · expressjs/express · GitHub](https://github.com/expressjs/express/pull/6933#issuecomment-3602268351)

Express.js 项目在 GitHub 上发布了 5.2.1 版本，该版本撤销了之前 5.2.0 版本中包含的一个安全补丁，原因是该补丁引入了不兼容的破坏性变更，且相关 CVE 已被认定为无效。

- 🔄 **版本回退**：5.2.1 版本撤销了 5.2.0 中针对 CVE-2024-51999 的安全补丁，因为该补丁实际上是一个破坏性变更，不符合语义化版本规范。
- ⚠️ **CVE 无效**：相关 CVE 已被提交拒绝，因为其描述的行为并非真正的安全漏洞，而是 JavaScript 对象原型属性的正常解析行为。
- 🛠️ **维护者解释**：维护者表示该补丁被错误地包含在次要版本发布中，可能破坏依赖特定边缘场景（如 `constructor` 属性）的用户代码。
- 🤔 **社区疑虑**：部分用户对撤销安全补丁表示担忧和不解，担心可能重新引入安全问题，但维护者澄清不存在实际漏洞。
- 📝 **后续计划**：项目团队计划发布事后分析，说明事件原因并改进发布流程，以防止类似问题再次发生。

---

### [发布 4.22.0 版本 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/4.22.0)

**原文标题**: [Release 4.22.0 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/4.22.0)

Express.js 4.22.0 版本发布，主要包含安全修复和多项改进。

- 🔒 修复了安全漏洞 CVE-2024-51999（GHSA-pj86-cfqh-vqx6）
- 📚 重构代码以提高可读性
- 🛠️ 添加对 Node.js 23.0 和 24.0 的支持
- 🐛 修复无路径方法函数的错误处理
- 🔄 更新 GitHub Actions CI 工作流程
- 📦 更新依赖项 qs 至 6.14.0 版本
- 👥 由多位贡献者共同完成发布

---

### [发布 v4.22.1 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v4.22.1)

**原文标题**: [Release v4.22.1 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v4.22.1)

Express.js 项目发布了 4.22.1 版本，主要修复了前一版本中引入的意外破坏性变更，并澄清了相关安全问题。

- 🔄 版本 4.22.1 已完全回滚了 4.22.0 中关于扩展查询解析器的错误变更
- ⚠️ 澄清此前变更并未导致实际的安全漏洞，相关 CVE 已被拒绝
- 📅 该版本于 2024 年 12 月 1 日由维护者发布
- 👥 发布过程获得了社区成员的积极反馈与互动

---

### [Node.js 24 LTS 现已全面支持构建与函数功能 - Vercel](https://vercel.com/changelog/node-js-24-lts-is-now-generally-available-for-builds-and-functions)

**原文标题**: [Node.js 24 LTS is now generally available for builds and functions - Vercel](https://vercel.com/changelog/node-js-24-lts-is-now-generally-available-for-builds-and-functions)

Node.js 24 现已作为运行时版本提供，用于构建和函数，新项目默认使用此版本，并带来多项核心更新。

- 🚀 **V8 引擎升级**：搭载 V8 13.6 引擎，性能提升，新增 Float16Array 和 Error.isError 等 JavaScript 功能
- 🌐 **全局 URLPattern API**：简化 URL 路由与匹配，无需依赖外部库或复杂正则表达式
- ⚡ **Undici v7**：内置 fetch API 性能更快，HTTP/2 与 HTTP/3 支持更佳，连接处理更高效
- 📦 **npm v11**：更新 npm 版本，提升与现代 JavaScript 包的兼容性
- 🔄 **自动更新**：当前版本为 24.11.0，将自动更新，仅保证主版本（24.x）稳定

---

### [沙虫 2.0 npm 蠕虫：深度分析与必备知识 | Datadog 安全实验室](https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/)

**原文标题**: [
  The Shai-Hulud 2.0 npm worm: analysis, and what you need to know | Datadog Security Labs
](https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/)

2025 年 9 月发现首个自复制 npm 蠕虫 Shai-Hulud，同年 11 月 24 日出现具有相似手法的升级版 Shai-Hulud 2.0。该蠕虫已感染 796 个合法 npm 包，累计周下载量超 2000 万次，主要功能为窃取凭证并通过 GitHub 仓库外泄。它利用自托管 GitHub 运行器建立 C2 通道，并能通过读取自身代码感染更多 npm 包进行自我传播。据估计，至少 500 名 GitHub 用户和 150 个组织的数据遭泄露。若蠕虫无法传播或外泄数据，会尝试删除用户主目录作为最后手段。

- 🐛 **蠕虫概述**：Shai-Hulud 2.0 通过注入恶意文件并添加预安装脚本感染 npm 包，使用 Bun 运行时执行混淆负载。
- 🔑 **凭证窃取**：广泛收集本地与云端（AWS、GCP、Azure）的凭证，包括调用元数据服务和访问密钥库。
- 📤 **数据外泄**：默认创建描述为“Sha1-Hulud: The Second Coming.”的公开 GitHub 仓库外泄凭证，若无凭证则搜索其他受害者的仓库复用令牌。
- 🤖 **C2 通道建立**：在受感染机器上安装自托管 GitHub 运行器，通过注入命令的 GitHub Action 实现远程代码执行。
- 🔄 **自我传播**：利用本地 npm 令牌自动感染用户拥有的其他 npm 包（最多 100 个），通过篡改版本和添加恶意文件实现。
- 💥 **破坏性行为**：若无法获取有效 GitHub 或 npm 凭证，则尝试彻底删除用户主目录中的所有文件。
- 📊 **影响评估**：通过 GHArchive 数据集分析，外泄活动在 2025 年 11 月 24 日达到高峰，创建了超 1.4 万个 GitHub 仓库。
- 🛡️ **检测与防护**：提供受影响包列表、文件哈希等 IOC，推荐使用 Datadog 的 SCFW 等工具进行主动拦截和运行时监控。

---

### [十二月静默月（2025 年 12 月）| 电子](https://www.electronjs.org/blog/dec-quiet-period-25)

**原文标题**: [December Quiet Month (Dec'25) | Electron](https://www.electronjs.org/blog/dec-quiet-period-25)

Electron 项目将于 12 月 1 日进入静默期，期间维护人员将暂停常规维护工作以休息或专注深度工作，并于 2026 年 1 月全面恢复运作。这一传统自 2020 年起实施，旨在让团队休整后以更佳状态迎接新一年。项目健康运行得益于所有维护者和贡献者的持续努力。

- 🎉 2025 年项目成果丰硕：发布了 6 个 Electron 主版本、迁移至 Siso 构建系统、更新发布页面设计、通过并实施多项 RFC、完成两个谷歌编程之夏项目、升级所有 npm 包为 ES 模块、采用无令牌发布系统，并新增四位维护者。
- ⏸️ 静默期政策调整：基本延续往年安排，但明确了对问题处理和代码审查可能延迟的说明，同时允许维护者按意愿参与项目。
- 🛡️ 安全与行为准则不变：重大安全漏洞将照常处理，行为准则报告与调解持续进行。
- 🚫 12 月变动事项：月初发布年度最后稳定版后暂停计划内发布；下旬停止夜间版及测试版发布；工作组会议暂停；问题分类与代码审查可能延迟。

---

### [Prisma 7 版本发布：无锈、更快、兼容性更强](https://www.prisma.io/blog/announcing-prisma-orm-7-0-0)

**原文标题**: [Prisma 7 Release: Rust-Free, Faster, and More Compatible](https://www.prisma.io/blog/announcing-prisma-orm-7-0-0)

Prisma 7 正式发布，标志着 Prisma ORM 和 Prisma Postgres 的重大更新，专注于提升开发体验、性能和易用性。此次版本移除了 Rust 依赖，采用 TypeScript 重构客户端，显著优化了打包大小和运行效率，同时引入了新的配置文件和更快的类型生成。Prisma Postgres 进一步扩展兼容性，支持标准 Postgres 协议，便于与各种工具集成。

- 🚀 **性能大幅提升**：移除 Rust 依赖后，打包体积减少 90%，查询速度提升 3 倍，CPU 和内存占用显著降低，部署更简单
- 🔧 **开发体验优化**：生成代码移至项目源码，新增 Prisma 配置文件，支持动态配置，提升工作流灵活性
- ⚡ **类型生成加速**：与 ArkType 合作优化，类型检查速度提高 70%，所需类型数量大幅减少，提供更高效的类型安全
- 🗄️ **Prisma Postgres 增强**：基于标准 Postgres 协议，兼容更多生态工具，提供一键创建数据库的便捷体验
- 📦 **功能更新与改进**：包括枚举映射支持、Node 和 TypeScript 最低版本更新，以及新版 Prisma Studio，详细更新可查看官方日志

---

### [Node.js 24 运行时现已在 AWS Lambda 中可用 | AWS 计算博客](https://aws.amazon.com/blogs/compute/node-js-24-runtime-now-available-in-aws-lambda/)

**原文标题**: [Node.js 24 runtime now available in AWS Lambda | AWS Compute Blog](https://aws.amazon.com/blogs/compute/node-js-24-runtime-now-available-in-aws-lambda/)

AWS Lambda 现已支持 Node.js 24 作为托管运行时和容器基础镜像，该版本处于活跃 LTS 状态，预计支持至 2028 年 4 月。新运行时包含重新编写的 TypeScript 运行时接口客户端，移除了对回调式处理程序等旧功能的支持，并引入了多项语言更新和性能改进。

- 🚀 **Node.js 24 正式上线**：AWS Lambda 现已提供 Node.js 24 托管运行时和容器基础镜像，该版本为活跃 LTS，适用于生产环境，支持将持续至 2028 年 4 月。
- 🔄 **运行时接口客户端更新**：新的 TypeScript 版运行时接口客户端简化了 Node.js 在 Lambda 中的集成，移除了回调式处理程序等旧功能，仅支持 async/await 和同步处理程序。
- 🛠️ **语言特性增强**：Node.js 24 引入了显式资源管理、Undici 7 HTTP 客户端性能提升以及 AsyncLocalStorage 的默认 AsyncContextFrame 实现，有助于优化资源清理和异步上下文传播。
- ⚠️ **回调处理程序不再支持**：Node.js 24 运行时移除了对回调式处理程序的支持，开发者需将现有函数迁移至 async/await 或同步处理程序签名。
- 🔧 **实验性功能默认禁用**：Lambda 默认禁用了 Node.js 中的实验性功能（如 require() 在 ES 模块中的支持），但可通过环境变量重新启用。
- 📦 **ES 模块支持扩展**：Node.js 24 允许在 CloudFormation 内联函数中使用 ES 模块，简化了小型工具和引导逻辑的编写，无需额外打包步骤。
- ⚡ **性能注意事项**：新运行时初期可能因缓存使用率较低导致冷启动时间延长，建议性能敏感型工作负载自行测试，而非依赖通用基准。
- 🔄 **迁移指南**：从 Node.js 16 或更早版本升级时，需将 AWS SDK 从 v2 升级至 v3，容器镜像需将包管理器从 yum 切换为 dnf。
- 🛠️ **多工具支持**：可通过 AWS 管理控制台、CLI、SDK、SAM、CDK 等多种工具配置和部署 Node.js 24 函数，也支持使用容器基础镜像进行构建。

---

### [AWS Lambda 托管实例发布：兼具无服务器简洁性与 EC2 灵活性 | AWS 官方博客](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/)

**原文标题**: [Introducing AWS Lambda Managed Instances: Serverless simplicity with EC2 flexibility | AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/)

AWS Lambda Managed Instances 是一项新功能，允许在用户自己的 Amazon EC2 计算资源上运行 Lambda 函数，同时保持无服务器操作的简便性。它旨在满足需要特定硬件或希望通过 EC2 预留定价优化成本的稳态工作负载，而无需用户自行管理基础设施。

- 🚀 **结合无服务器与 EC2 灵活性**：在自有 EC2 实例上运行 Lambda 函数，享受无服务器体验，同时获得 EC2 的专用计算选项和定价优势。
- 💰 **优化成本**：支持应用计算节省计划和预留实例等 EC2 承诺定价模型，相比按需定价最高可节省 72% 成本，尤其适合稳态工作负载。
- ⚙️ **简化运维**：AWS 负责实例生命周期管理、操作系统修补、负载均衡和自动扩展，用户无需管理底层 EC2 基础设施。
- 🔄 **支持多并发**：每个执行环境可同时处理多个请求，提高资源利用率，减少计算消耗，并有效避免冷启动影响。
- 🛠️ **易于配置**：通过控制台、CLI 或 IaC 工具创建“容量提供者”，定义实例类型、网络和扩展参数，并将其关联到 Lambda 函数。
- 🌍 **现已可用**：在多个 AWS 区域推出，支持 Node.js、Java、.NET 和 Python 运行时，可与现有 Lambda 工作流及监控工具集成。
- 📊 **定价透明**：费用包含 Lambda 请求费、EC2 实例费以及 15% 的计算管理费，无需为每次请求的执行时长单独付费。

---

### [用 Claude Code 管理我的电子邮件](https://jlongster.com/wrangling-email-claude-code)

**原文标题**: [Wrangling my email with Claude Code](https://jlongster.com/wrangling-email-claude-code)

作者因不擅长管理邮件而错过重要机会，在离职后利用 Claude Code 和 AI 工具构建了高效的邮件处理流程。通过创建自定义技能，让 AI 直接读取 Gmail 并智能分析邮件内容，实现了自动追踪待回复邮件、整理公司信息并生成结构化数据，极大提升了工作效率。

- 📧 作者因邮件管理混乱常错过重要机会，离职后决定用 AI 优化工作流程
- 🤖 放弃复杂自动化工具 n8n，转向熟悉的 Claude Code 扩展邮件处理能力
- 🔧 通过 Skills 功能创建 Gmail 技能，用脚本连接 Gmail API 实现邮件读取
- 🧠 AI 能智能分析邮件线程，自动识别未回复邮件并提取关键信息
- 📊 成功整理公司联系信息并生成含调研数据的 CSV 文件，辅助职业决策
- 💡 发现技能在非技能目录运行时存在指令识别问题，但整体效果出色
- ⚡ 强调上下文保持和渐进式交互让 AI 工具像增强版 REPL 般高效实用

---

### [介绍代理技能 | Claude](https://www.claude.com/blog/skills)

**原文标题**: [Introducing Agent Skills | Claude](https://www.claude.com/blog/skills)

Anthropic 推出了名为“技能”的新功能，使 Claude 能够通过加载包含指令、脚本和资源的文件夹来更专业地执行特定任务，该功能现已在 Claude 应用、API 和 Claude Code 中全面可用。

- 🧠 **核心功能**：技能是包含指令和资源的文件夹，Claude 仅在任务相关时按需加载，从而提升其在 Excel 操作、品牌指南遵循等专业任务中的表现。
- 🔄 **工作原理**：Claude 自动扫描可用技能并匹配任务，仅加载必要信息以保持高效；技能可组合、可移植且支持包含可执行代码。
- 📱 **产品覆盖**：技能适用于 Claude 应用（Pro、Max、Team 和 Enterprise 用户）、Claude 开发者平台 API（需代码执行工具）以及 Claude Code（可通过插件市场安装）。
- 🛠️ **创建与管理**：用户可通过“技能创建器”交互式创建自定义技能；开发者可通过 API 和 Claude 控制台管理技能版本，并利用官方示例进行定制。
- ⚠️ **安全提示**：由于技能允许 Claude 执行代码，用户需仅使用可信来源的技能以确保数据安全。
- 🚀 **未来规划**：团队正致力于简化技能创建流程和企业级部署能力，以便更轻松地在组织内部分发技能。

---

### [使用 Foxit API 将安全电子签名嵌入您的应用 - Foxit](https://developer-api.foxit.com/developer-blogs/compliance-security/audit-trails/embed-secure-esignatures-into-your-app-with-foxit-api/?utm_source=cooperpress&utm_medium=Display&utm_campaign=12-02-25)

**原文标题**: [Embed Secure eSignatures into Your App with Foxit API - Foxit](https://developer-api.foxit.com/developer-blogs/compliance-security/audit-trails/embed-secure-esignatures-into-your-app-with-foxit-api/?utm_source=cooperpress&utm_medium=Display&utm_campaign=12-02-25)

我们分享了在 API World 2025 上的精彩体验，展示了如何利用 Foxit API 构建一个可审计、AI 驱动的文档自动化系统。

- 🎉 在 API World 2025 上与开发者交流，展示 Foxit API 在 AI 简历生成器和互动涂鸦应用中的应用
- 🛠️ 通过实际案例演示，介绍如何使用 Foxit PDF 服务和文档生成 API
- 🤖 构建具备审计功能的 AI 驱动文档自动化工作流程
- 📄 结合 PDF 处理与智能文档生成技术，提升文档处理效率与透明度

---

### [网页性能日历 » 通过 HTTP 流提升 TTFB 与用户体验](https://calendar.perfplanet.com/2025/improve-ttfb-and-ux-with-http-streaming/)

**原文标题**: [Web Performance Calendar » Improve TTFB and UX with HTTP streaming](https://calendar.perfplanet.com/2025/improve-ttfb-and-ux-with-http-streaming/)

本文介绍了如何通过 HTTP 流式传输技术提升动态生成网页的加载速度和用户体验，特别针对依赖数据库查询的页面。

- 🚀 **提升感知速度**：HTTP 流式传输能显著改善动态页面的首字节时间（TTFB），让用户更早开始浏览内容。
- ⚡ **即时发送内容**：页面头部等不依赖数据库的部分可立即发送，无需等待整个查询完成。
- 🔄 **逐行流式输出**：数据库查询结果可逐行转换为 HTML 并发送，实现边查询边渲染。
- 🛠️ **技术实现关键**：需确保从数据库驱动到 CDN 的整个链路支持非阻塞流式传输，避免使用阻塞操作的`await`。
- 💻 **代码示例演示**：使用 Mastro 框架和 Kysely 数据库库，通过`db.stream()`替代`await db.execute()`实现异步迭代流式处理。

---

### [获取失败](https://nodeweekly.com/link/177827/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177827/web)

无法总结：获取内容失败，状态码 403。

---

### [面向 JavaScript/TypeScript 开发者的范畴论 —— Ibrahim Cesar](https://ibrahimcesar.cloud/blog/category-theory-for-javascript-typescript-developers/)

**原文标题**: [Category Theory for JavaScript/TypeScript Developers â Ibrahim Cesar](https://ibrahimcesar.cloud/blog/category-theory-for-javascript-typescript-developers/)

本文为 JavaScript/TypeScript 开发者介绍了范畴论的核心概念及其实际应用，旨在揭示日常编程中如 Promise.then 等操作背后的深层数学结构，并展示如何利用这些理论改进代码设计和组合方式。

- 🧩 范畴论将类型视为对象、函数视为态射，并强调组合与恒等律，为编程中的类型与函数关系提供了精确的数学框架。
- 🗺️ 函子（如 Array.map）是结构保持的映射，允许在不同范畴间转换并保持组合关系，是处理如数组、Promise 等容器的基础。
- 🔄 自然变换在不同函子间提供一致的转换方式（如从数组取首元素转为 Option 类型），确保操作与结构变换可交换。
- 🧠 单子（如 Promise）通过 flatMap（或 then）组合可能失败或具有副作用的操作，提供了一种可预测、可组合的处理模式。
- 🔗 伴随关系是单子的来源，描述了如同步与异步操作间“几乎可逆”的映射关系，解释了为什么某些 API（如 async/await）会“感染”代码结构。
- 💡 Yoneda 引理表明“从 Hom 函子到 F 的自然变换”等价于 F(A) 的元素，这为如 CPS（延续传递风格）等模式提供了理论基础，并允许免费获得映射操作。
- 🛠️ 通过显式表示态射、函子和自然变换，可以构建嵌入式 DSL，使范畴结构可操作、可测试，从而提升代码的可靠性和可组合性。
- ✅ 范畴论提供了可验证的定律（如单子定律），确保重构的安全性，并帮助识别设计模式，避免重复实现。
- 📚 实际应用中，开发者可利用现有库（如 fp-ts、Effect）实现这些模式，专注于识别问题而非重复造轮子，从而设计出更优雅、可组合的 API。

---

### [首页 | voici.js](https://voici.larswaechter.dev/)

**原文标题**: [Home | voici.js](https://voici.larswaechter.dev/)

voici.js 是一个用 TypeScript 编写的开源 Node.js 库，用于在终端中以表格形式美观地展示数据集，相比 `console.table()` 功能更丰富。

- 🎨 支持文本、列和行的样式设计
- 🔍 提供高亮和筛选功能
- 📊 支持动态列和列尺寸调整
- 📈 包含数据累加和排序功能
- 📤 支持表格导出和类型系统
- 👀 提供数据预览功能

---

### [排序 | voici.js](https://voici.larswaechter.dev/examples/sorting)

**原文标题**: [Sorting | voici.js](https://voici.larswaechter.dev/examples/sorting)

该文章介绍了如何使用 Voici.js 库中的 Table 组件对表格数据进行多列排序，包括升序和降序排列，并提供了具体的代码示例和排序结果。

- 📊 表格排序功能允许根据指定列和方向（升序或降序）对数据进行排序。
- 🔢 可通过`sort`选项配置排序，需提供`columns`和`directions`数组，且两者长度必须一致。
- 💻 代码示例展示了如何对包含姓名和年龄的数据按姓氏升序、年龄降序进行排序。
- 📋 排序结果以表格形式输出，清晰展示了排序后的数据排列。

---

### [色彩 | voici.js](https://voici.larswaechter.dev/examples/styling/colors)

**原文标题**: [Colors | voici.js](https://voici.larswaechter.dev/examples/styling/colors)

本文介绍了如何使用 Voici.js 库自定义表格的文本和背景颜色，包括整体设置、表头定制以及按列配置颜色的方法。

- 🎨 可更改表格的文本和背景颜色，颜色值需使用十六进制格式
- 📝 通过配置`body`对象设置表格主体内容的颜色，如示例 1 所示
- 🏷️ 通过配置`header`对象单独设置表头颜色，如示例 2 所示
- 📊 使用`bgColorColumns`数组为不同列设置背景颜色，如示例 3 所示

---

### [GitHub - larswaechter/voici.js：一个用于在终端上漂亮打印数据的Node.js库🎨](https://github.com/larswaechter/voici.js)

**原文标题**: [GitHub - larswaechter/voici.js: A Node.js library for pretty printing your data on the terminal🎨](https://github.com/larswaechter/voici.js)

voici.js 是一个用于在终端中美观打印数据的 Node.js 开源库，支持表格展示、样式定制、排序、筛选等多种功能。

- 🎨 一个 Node.js 库，用于在终端中以表格形式美观打印数据
- 📦 通过 npm 安装，支持 TypeScript 编写，提供丰富的 API 和功能
- 🛠️ 功能包括文本样式、列与行样式、高亮、筛选、动态列、列尺寸调整、数据汇总、表格导出和排序等
- 📚 提供 GitBook 文档、TypeDoc 及测试示例，便于学习和使用
- 🤝 欢迎贡献，遵循 MIT 开源协议，项目托管在 GitHub 上

---

### [GitHub - paulmillr/chokidar：轻量高效的跨平台文件监控库](https://github.com/paulmillr/chokidar)

**原文标题**: [GitHub - paulmillr/chokidar: Minimal and efficient cross-platform file watching library](https://github.com/paulmillr/chokidar)

Chokidar 是一个跨平台文件监控库，以其高效和轻量著称，适用于 Node.js 环境，支持递归监控、符号链接、文件过滤等功能，并优化了事件处理和资源使用。

- 📁 **跨平台文件监控库** – 提供高效、轻量的文件系统监控，支持 macOS、Windows 和 Linux。
- 🔄 **优于原生 fs.watch** – 解决了事件重复报告、文件名丢失等问题，提供更可靠的事件响应。
- ⚙️ **丰富配置选项** – 支持忽略特定文件、递归深度限制、原子写入检测和轮询模式等。
- 📦 **广泛使用与稳定** – 自 2012 年发布，被数千万仓库使用，经过生产环境验证。
- 🚀 **持续更新优化** – 最新版本 v5 仅支持 ESM，减少依赖并提升性能，要求 Node.js v20 以上。
- 🛠️ **易于集成使用** – 通过简单 API 监听文件变化，支持添加、删除、更改等多种事件。
- ⚠️ **故障处理与兼容** – 提供解决文件句柄耗尽等常见问题的方法，并说明版本升级变化。

---

### [GitHub - paulmillr/readdirp: 递归版 fs.readdir，内存与 CPU 占用极低。](https://github.com/paulmillr/readdirp)

**原文标题**: [GitHub - paulmillr/readdirp: Recursive version of fs.readdir with small RAM & CPU footprint.](https://github.com/paulmillr/readdirp)

readdirp 是一个递归读取目录的 Node.js 库，提供流式 API 和 Promise API，具有低内存和 CPU 占用。它支持文件/目录过滤、深度控制、符号链接处理等功能，适用于高效遍历文件系统。

- 📦 **递归读取目录**：提供 fs.readdir 的递归版本，支持流式与 Promise 两种 API。
- 🚀 **高性能设计**：通过流式处理实现低内存和 CPU 占用，适合处理大量文件。
- ⚙️ **灵活过滤选项**：支持通过 fileFilter 和 directoryFilter 自定义文件与目录的包含/排除规则。
- 📏 **深度与类型控制**：可设置递归深度（depth）和输出类型（文件、目录或全部）。
- 🔗 **符号链接支持**：可配置 lstat 选项以包含符号链接条目。
- 📄 **详细文件信息**：返回 EntryInfo 对象，包含路径、基础名、状态统计等数据。
- 🛠️ **多版本兼容**：支持 Node.js 8+ 版本，最新版本使用 TypeScript 重写，提供 CommonJS 和 ESM 模块。
- 📜 **开源许可**：基于 MIT 许可证发布，由社区维护并广泛使用。

---

### [GitHub - keichi/binary-parser：用于二进制数据的极速声明式解析器构建工具](https://github.com/keichi/binary-parser)

**原文标题**: [GitHub - keichi/binary-parser: A blazing-fast declarative parser builder for binary data](https://github.com/keichi/binary-parser)

binary-parser 是一个用于 JavaScript 的二进制解析器构建工具，允许以声明式方式编写高效的二进制解析器。它支持解析结构化二进制数据所需的所有常见数据类型，并通过即时动态生成和编译解析器代码来实现接近手写解析器的性能。

- 🚀 **高性能解析器构建工具** – 通过即时编译生成高效代码，性能接近手写解析器。
- 📦 **支持丰富数据类型** – 包括整数、浮点数、位字段、字符串、数组、选择结构和指针等。
- 🔧 **声明式 API 设计** – 提供链式方法调用，可直观构建复杂解析逻辑。
- 🧩 **灵活的数据处理** – 支持动态长度数组、条件解析、嵌套结构和自定义格式化。
- 🔄 **递归与自引用解析** – 通过 `namely()` 方法支持解析递归数据结构。
- 📏 **上下文变量支持** – 可选启用 `$parent`、`$root` 等上下文变量，便于跨层级数据访问。
- 🧪 **完善的错误处理与断言** – 提供 `assert` 选项进行数据验证，确保解析正确性。
- 🌐 **广泛的编码支持** – 字符串解析支持多种编码，包括 UTF-8 和十六进制等。
- 📄 **活跃的开源项目** – 采用 MIT 许可证，拥有活跃的社区维护和丰富的示例。

---

### [更好的认证](https://www.better-auth.com/)

**原文标题**: [Better Auth](https://www.better-auth.com/)

Better Auth 是一个面向 TypeScript 的全面身份验证框架，旨在让开发者能够快速、自信地构建自己的身份验证系统。它支持多种主流前端框架，提供电子邮件密码、社交登录、双因素认证、多租户组织等功能，并通过插件生态系统扩展能力，开发者反馈其设置简单、运行高效。

- 🚀 **快速集成**：只需几分钟即可完成身份验证系统的搭建，一次设置即可稳定运行。
- 🔧 **框架无关**：支持 React、Vue、Svelte、Next.js 等众多流行前端框架。
- 📧 **多种认证方式**：内置电子邮件密码认证、社交登录（如 GitHub、Google）及双因素认证。
- 🏢 **多租户支持**：提供组织、团队、成员管理和邀请功能，适合企业级应用。
- 🧩 **插件生态**：通过官方和社区插件轻松扩展更多功能，提升应用体验。
- ⚡ **高效易用**：开发者反馈其配置简单、性能出色，相比其他方案更快捷。
- 🌟 **社区认可**：获得众多开发者和行业领袖的高度评价，被视为身份验证领域的佳作。

---

### [更好的认证 1.4](https://www.better-auth.com/blog/1-4)

**原文标题**: [Better Auth 1.4](https://www.better-auth.com/blog/1-4)

Better Auth 1.4 版本发布，引入了无状态认证、SCIM 配置、数据库查询优化、OAuth 流程自定义状态、性能提升、SSO 域名验证等多项新功能与改进，并包含大量错误修复和细节优化。

- 🚀 **无状态认证**：现可无需数据库配置，启用无状态会话管理，并支持获取访问令牌、账户信息和刷新令牌。
- 🔗 **SCIM 配置支持**：通过标准化协议简化多域场景下的身份管理。
- 🛠️ **OAuth 流程自定义状态**：允许在 OAuth 流程中传递额外数据，并在钩子或中间件中访问。
- ⚡ **数据库连接优化（实验性）**：启用数据库连接功能，显著降低超过 50 个端点的延迟。
- 🔑 **API 密钥二级存储**：API 密钥插件现支持二级存储，以实现更快的密钥查找。
- 🖥️ **全新默认错误页面**：提供更美观、信息更丰富的错误页面，并支持自定义样式或路径。
- 🌐 **SSO 域名验证**：支持通过关联域名自动验证 SSO 提供商的所有权。
- 📊 **CLI 数据库索引支持**：Better-Auth CLI 现支持开箱即用的数据库索引，提升应用性能。
- 🔄 **JWT 密钥轮换支持**：JWT 插件现支持密钥轮换，无需停机即可更新密钥。
- 🔌 **改进的通用 OAuth 插件**：为尚未原生支持的 OAuth 提供商提供预配置选项。
- 📦 **包大小优化**：通过使用 `better-auth/minimal` 版本，可减少自定义适配器的包大小。
- 🆔 **UUID 支持**：现支持将 UUID 作为主 ID 字段类型。
- 📧 **改进的邮箱更改流程**：为提升安全性，要求用户在向新地址发送验证邮件前通过当前邮箱确认更改。
- 📱 **设备授权插件**：完整支持 OAuth 2.0 设备授权许可，适用于智能电视和游戏机等输入受限设备。
- 🍪 **基于 Cookie 的账户存储**：可将用户账户数据存储在签名 Cookie 中，适用于无状态应用或延迟数据库持久化的场景。
- ⚠️ **破坏性变更**：包括现有认证流程、插件选项、认证配置等方面的多项变更，升级时需注意调整。
- 🐛 **错误修复与改进**：包含超过 250 项错误修复，涵盖适配器、会话管理、OAuth、组织管理、双因素认证等多个方面。

---

### [发布 v1.57.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.57.0)

**原文标题**: [Release v1.57.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.57.0)

Playwright 1.57.0 版本发布，引入了新的性能分析工具 Speedboard，将浏览器引擎从 Chromium 切换为 Chrome for Testing，并新增了等待 Web 服务器输出的配置选项。同时，移除了已弃用三年的 Page#accessibility API，并添加了多项新 API 和改进。

- 🚀 **Speedboard 性能分析**：HTML 报告中新增 Speedboard 标签页，按执行速度排序显示测试，帮助识别耗时较长的测试。
- 🔄 **浏览器引擎切换**：从 Chromium 切换到 Chrome for Testing，预计无功能变化，但图标和标题更新；Arm64 Linux 仍使用 Chromium。
- ⏳ **Web 服务器等待功能**：testConfig.webServer 新增 wait 字段，支持通过正则表达式等待服务器日志匹配，并可捕获环境变量。
- 🗑️ **API 移除**：移除已弃用三年的 Page#accessibility API，建议使用 Axe 等库进行无障碍测试。
- 🏷️ **测试标签支持**：新增 testConfig.tag 属性，为所有测试添加标签，便于使用 merge-reports。
- 📝 **控制台事件监听**：worker.on('console') 事件可监听 Worker 内的 console 调用，worker.waitForEvent() 用于等待事件。
- 🔍 **定位器描述增强**：locator.description() 返回之前设置的描述，Locator.toString() 在可用时使用描述。
- 🖱️ **鼠标事件配置**：locator.click() 和 locator.dragTo() 新增 steps 选项，配置移动到目标元素时的 mousemove 事件数量。
- 🌐 **Service Worker 网络请求**：Chromium 中 Service Worker 发出的网络请求现可通过 BrowserContext 报告和路由，可通过环境变量禁用。
- 📢 **Service Worker 控制台消息**：Service Worker 的控制台消息通过 worker.on('console') 分发，可通过环境变量禁用。
- 🔧 **浏览器版本更新**：Chromium 143.0.7499.4、Firefox 144.0.2、WebKit 26.0。

---

### [Chrome for Testing：为浏览器自动化提供可靠下载 | 博客 | Chrome for Developers](https://developer.chrome.com/blog/chrome-for-testing/)

**原文标题**: [Chrome for Testing: reliable downloads for browser automation  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-for-testing/)

Chrome for Testing 是一个专为浏览器自动化和测试设计的新版本 Chrome，它解决了开发者在使用常规 Chrome 进行测试时遇到的自动更新和版本匹配问题，通过提供无自动更新、与 Chrome 发布流程同步的版本化二进制文件，简化了测试环境的搭建。

- 🚀 **发布目的**：专为网页应用测试和自动化设计，解决开发者测试环境搭建难题
- 🔄 **解决自动更新问题**：常规 Chrome 自动更新影响测试结果一致性，此版本禁用该功能
- 🔢 **版本化二进制文件**：提供特定版本 Chrome 下载，便于版本锁定和回溯测试
- 🔗 **与 ChromeDriver 集成**：确保 Chrome 与 ChromeDriver 版本兼容，简化自动化测试配置
- 📦 **获取方式**：可通过 `@puppeteer/browsers` 命令行工具或 JSON API 下载各版本
- ⚠️ **使用限制**：仅用于测试可信内容，不适用于日常浏览

---

### [pnpm 10.24 | pnpm](https://pnpm.io/blog/releases/10.24)

**原文标题**: [pnpm 10.24 | pnpm](https://pnpm.io/blog/releases/10.24)

pnpm 10.24 版本引入了自适应网络并发功能，根据机器核心数自动调整并发连接数以提升性能，同时包含多项可靠性修复，增强了在容器环境中的稳定性和包管理安全性。

- 🚀 自适应网络并发：根据 CPU 核心数自动调整网络并发连接数（16 至 64 之间），提升多核机器性能，同时保持资源使用可控。
- 🔒 信任策略优化：安装稳定版时忽略预发布版本的信任证据，防止受信任的预发布版本阻碍稳定版安装。
- 🐛 容器环境兼容性：在 OverlayFS 等容器环境中，优雅处理`ENOENT`错误，自动回退到文件复制操作。
- ↩️ 撤销自我更新功能：取消了从配置的 npm 仓库下载 pnpm 的自我更新行为。
- 📦 包导入优化：对于无`package.json`的包（如 Node.js），通过检查额外文件避免每次安装时重复从存储导入。
- 🔑 认证令牌读取修复：修正了包含下划线的 URL 中认证令牌的读取问题。

---

### [Sidequest.js](https://sidequestjs.com/)

**原文标题**: [Sidequest.js](https://sidequestjs.com/)

Sidequest.js 是一款专为 Node.js 设计的持久化、分布式且云无关的任务队列系统，旨在提供简单可靠的后台作业管理。

- 🌎 云无关：可在任何云平台或本地环境运行，避免供应商锁定，无需重写代码
- 🚀 高可扩展：支持分布式部署，能协调大规模作业并保持高吞吐下的持久性
- 🎨 现代管理界面：提供直观的监控界面，便于实时查看任务状态和调试问题
- 🧰 开发者友好：拥有简洁的 API 和完整文档，可轻松集成到现有 Node.js 应用中

---

### [GitHub - WiseLibs/better-sqlite3：Node.js中最快且最简单的SQLite3库。](https://github.com/WiseLibs/better-sqlite3)

**原文标题**: [GitHub - WiseLibs/better-sqlite3: The fastest and simplest library for SQLite3 in Node.js.](https://github.com/WiseLibs/better-sqlite3)

better-sqlite3 是 Node.js 中一个高性能、简单易用的 SQLite3 库，以其同步 API 设计、出色的性能表现和丰富的功能支持而著称，适用于大多数需要轻量级数据库的场景。

- 🚀 **高性能表现**：相比其他 Node.js SQLite 库（如 node-sqlite3），在多数操作中速度更快，尤其在事务处理和查询方面优势明显。
- 🔄 **同步 API 设计**：采用同步 API，简化了使用方式，并在并发场景下表现优于异步 API，避免了不必要的资源浪费。
- 🛠️ **功能全面**：支持完整的事务、用户自定义函数、聚合、虚拟表、扩展以及 64 位整数和 Worker 线程。
- 📦 **易于安装使用**：通过 npm 即可安装，提供清晰的文档和示例，支持 ES6 模块导入。
- ⚠️ **适用场景说明**：适用于大多数应用，但对于极高并发读写、超大数据库（接近 TB 级）或返回数据量极大的场景，建议使用如 PostgreSQL 等全功能 RDBMS。
- 🔧 **维护与支持**：项目活跃，鼓励企业赞助以持续发展，提供详细的升级指南和性能优化建议（如启用 WAL 模式）。

---

### [GitHub - animir/node-rate-limiter-flexible：原子与非原子计数器及速率限制工具。任意规模下的资源访问限制。](https://github.com/animir/node-rate-limiter-flexible)

**原文标题**: [GitHub - animir/node-rate-limiter-flexible: Atomic and non-atomic counters and rate limiting tools. Limit resource access at any scale.](https://github.com/animir/node-rate-limiter-flexible)

node-rate-limiter-flexible 是一个用于 Node.js 的灵活、高性能的限流库，支持多种存储后端，旨在防止 DoS 和暴力攻击，并能在分布式环境中原子性地操作。

- 🛡️ **支持多种存储**：可与 Valkey、Redis、Memcached、MongoDB、MySQL、PostgreSQL、SQLite、DynamoDB 等集成，也支持进程内存和集群。
- ⚡ **高性能**：平均请求耗时在集群中为 0.7ms，分布式应用中为 2.5ms，采用固定窗口算法。
- 🔒 **原子操作**：所有操作在内存或分布式环境中均使用原子递增，避免竞态条件。
- 🧩 **高度灵活**：提供组合限流器、延迟操作、故障转移保险、内存智能拦截等功能，API 统一且易于扩展。
- 🌐 **广泛兼容**：与各种 Node.js 驱动和框架（如 Express、Koa、Hapi、NestJS）友好集成，并支持 Deno。
- 📚 **丰富功能**：包含阻塞策略、保险策略、队列支持、黑白名单、动态拦截等，适用于登录保护、API 限流、WebSocket 防洪水等场景。
- 📦 **简单易用**：通过 `consume` 方法消耗点数，基于 IP、用户 ID、令牌等关键标识进行限流，并返回详细的限流响应对象。
- 🔧 **可定制配置**：可设置点数、持续时间、键前缀、拦截时长等选项，支持中间件和插件生态系统。
- 👥 **活跃社区**：拥有 3.4k 星标、180 分支，持续更新并接受贡献，要求新存储限流器扩展自 `RateLimiterStoreAbstract`。

---

### [框架 | Neutralinojs](https://neutralino.js.org/docs/release-notes/framework/#v640)

**原文标题**: [Framework | Neutralinojs](https://neutralino.js.org/docs/release-notes/framework/#v640)

Neutralinojs 框架版本更新摘要，涵盖从 v4.0.0 到 v6.4.0 的主要功能增强、API 新增、配置选项改进及错误修复。

- 🗑️ **v6.4.0**: 新增 `storage.clear()` 和 `storage.removeData(key)` API 以清除存储数据；修复 Windows 可拖动区域失效、窗口关闭时保存状态等问题，并替换 macOS 废弃 API。
- 📦 **v6.3.0**: 引入单可执行文件模式，通过 `--embed-resources` 将资源嵌入二进制文件；新增 `window.skipTaskbar` 和 `window.openInspectorOnStartup` 配置选项。
- 🖨️ **v6.2.0**: 新增 `window.print()` 支持原生打印对话框，`window.beginDrag()` 触发窗口拖动；文件系统 API 增加路径处理函数，并支持为 WebView2 传递额外参数。
- 🍎 **v6.1.0**: 新增 `window.setMainMenu()` 支持原生窗口菜单（Linux/Windows）和应用菜单（macOS）；新增全局变量 `NL_LOCALE` 和 `NL_COMPDATA`。
- 📋 **v6.0.0**: 剪贴板 API 新增 HTML 读写功能；`os` 模块的进程函数支持环境变量设置；文件系统 API 增强权限管理和文件监视事件。
- 🌐 **v5.6.0**: 新增 `server` 命名空间，支持挂载本地目录到静态服务器；资源 API 增加统计和提取功能；`window.snapshot()` 可捕获窗口为 PNG 图像。
- 💉 **v5.5.0**: 支持通过配置向外部网页注入全局变量和客户端库；新增预加载脚本功能；配置选项增加 `dataLocation` 和 `storageLocation`。
- 🪟 **v5.4.0**: 资源模块新增读取嵌入文件的功能；窗口 API 增加最小化、取消最小化及相关状态检查函数。
- 🪟 **v5.3.0**: Windows 支持窗口透明模式；文件系统 API 新增绝对路径、相对路径和路径解析函数。
- ⚙️ **v5.2.0**: 支持无配置文件启动框架；静态服务器新增单页应用（SPA）路由支持；改进 `window.show()` 在 Windows 上的行为。
- 🎨 **v5.1.0**: 支持窗口透明模式（macOS/Linux）；剪贴板 API 新增图像读写、清除和格式检查功能。
- 🔒 **v5.0.0**: 新增标准流读写 API；文件系统 API 支持递归操作和文件移动/复制/删除；增强安全机制，要求有效的连接令牌。
- 🌍 **v4.15.0**: 支持通过配置扩展用户代理字符串；允许使用 `--config-file` 指定自定义配置文件。
- 🛠️ **v4.14.0**: 文件系统 API 新增文件监视器管理功能；`os.execCommand` 支持设置工作目录；修复 Windows 托盘菜单的 Unicode 问题。
- 💾 **v4.13.0**: 核心功能支持持久化窗口状态（位置、大小、最大化状态），可通过配置启用或禁用。
- 🎯 **v4.12.0**: 新增 `window.center()` 以编程方式居中窗口；配置支持设置初始窗口位置和居中选项；Windows 版静态链接 WebView2 加载器。
- 👁️ **v4.11.0**: 新增原生文件监视器 API，支持创建跨平台的文件系统事件监视器。
- 📦 **v4.10.0**: 提供 ESM/NPM 支持，开发者可通过模块导入客户端库；生成 macOS arm64 和通用二进制文件。
- 🔧 **v4.9.0**: 引入自定义方法 API，允许开发者在不修改框架核心的情况下添加原生 API；新增基于事件的文件流 API。
- 🖱️ **v4.8.0**: 新增 `os.getEnvs()` 获取所有环境变量；文件系统 API 支持设置读取位置和大小；新增 `storage.getKeys()` 和 `computer.getMousePosition()`。
- 💻 **v4.7.0**: 系统信息 API 增强，新增获取 CPU、操作系统、内核和显示器详情的函数；系统对话框支持设置默认路径。
- 🚀 **v4.6.0**: 新增进程生成 API，支持异步处理长时间运行进程；支持 Linux ARM 架构的官方二进制构建。
- 🔔 **v4.5.0**: 新增 `windowFocus` 和 `windowBlur` 原生事件；使用 BuildZri 进行 C++ 构建自动化；新增全局变量 `NL_COMMIT`。
- 📝 **v4.4.0**: 新增 `window.getPosition()` 和文件追加函数；依赖项更新为 ayatana-appindicator3。
- 🔐 **v4.3.0**: 新增 `tokenSecurity` 配置以增强令牌安全性；新增 `window.setAlwaysOnTop()` 和 `window.getSize()`。
- 📋 **v4.2.0**: 新增剪贴板 API，支持读写系统剪贴板文本；配置支持 Chrome 模式参数和自定义 HTTP 头。
- 🌐 **v4.1.0**: 新增 Chrome 模式，可将应用作为 Chrome 应用运行；`window.getTitle()` 返回当前窗口标题。
- 🔌 **v4.0.0**: 引入扩展 API，支持加载外部进程；增强 `os.execCommand()` 返回多值；新增应用广播和更新器 API。

---

### [发布 v4.7.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.7.0)

**原文标题**: [Release v4.7.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.7.0)

NodeBB v4.7.0 版本发布，主要增强了联邦活动（ActivityPub）功能，包括话题移动、删除和上下文处理的改进，同时修复了多个错误并进行了代码重构。

- 🚀 **新功能**：新增联邦活动处理逻辑，支持话题移动、删除和上下文操作的联邦同步，并自动启用链接预览插件。
- 🛠️ **错误修复**：修复了附件属性检查、活动 ID 生成、主题事件逻辑及多个联邦同步中的逻辑错误。
- 🔄 **其他变更**：重构了部分内部方法，优化了帖子附件处理和联邦活动输出逻辑，并移除了`federatedDescription`字段。
- 📦 **依赖更新**：升级了 Markdown、Web-Push 和主题等依赖包版本。
- 🧪 **测试调整**：更新了测试用例以反映父帖子清除后`toPid`字段的保留逻辑。

---

### [ESLint v10.0.0-alpha.1 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/11/eslint-v10.0.0-alpha.1-released/)

**原文标题**: [ESLint v10.0.0-alpha.1 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/11/eslint-v10.0.0-alpha.1-released/)

ESLint v10.0.0-alpha.1 已发布，这是一个包含新功能、错误修复和重大变更的主要版本预发布，旨在收集社区反馈，暂不建议用于生产环境。

- 🚨 此版本为预发布版，主要用于测试和反馈，不适用于生产环境
- 🔧 移除了多个已弃用的 `SourceCode` 方法，如 `getTokenOrCommentBefore()`，需使用替代方案
- 📦 安装时需指定 `next` 标签或直接使用版本号 `10.0.0-alpha.1`
- 📘 提供了详细的迁移指南，帮助用户处理重大变更和升级问题
- ✨ 包含多项功能更新、文档改进及内部维护优化

---

### [ConfigCat - 团队功能标志服务](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

**原文标题**: [ConfigCat - Feature Flag Service for Teams](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

ConfigCat 是一个功能开关（Feature Flag）服务平台，允许开发团队安全地发布新功能，通过逐步推出和即时回滚来降低风险。

- 🚀 **快速启动**：10 分钟完成设置，无需信用卡，提供免费永久套餐
- 🛡️ **安全可控**：支持目标用户发布、即时功能开关，出现问题可立即关闭
- 💻 **技术实现**：通过客户端 SDK（如 ConfigCat.js）轻松集成功能标志
- 🔒 **隐私保护**：不收集用户数据，功能标志在客户端评估，符合安全合规要求
- 💰 **透明定价**：提供免费到企业级套餐，无隐藏费用，支持随时数据导出
- ⭐ **用户口碑**：获得行业好评，被评价为简单易用、性价比高的替代方案
- 📊 **套餐选择**：从免费版（10 个功能标志）到企业版（无限资源）多层级服务

---

### [获取失败](https://nodeweekly.com/link/177848/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177848/web)

无法总结：获取内容失败，状态码 520。

---

### [获取失败](https://nodeweekly.com/link/177849/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177849/web)

无法总结：获取内容失败，状态码 520。

---

### [全栈 Next.js 16 课程 - 通往 Next 之路](https://www.road-to-next.com/?utm_source=node_weekly&utm_medium=referral&utm_campaign=next_course)

**原文标题**: [Full-Stack Next.js 16 Course - The Road to Next](https://www.road-to-next.com/?utm_source=node_weekly&utm_medium=referral&utm_campaign=next_course)

《The Road to Next》是一门专注于使用 Next.js 16 和 React 19 的全栈 Web 开发视频课程，旨在帮助开发者从初级进阶到高级，掌握构建现代 SaaS 应用所需的技能。

- 🚀 **课程目标**：帮助学员成为全栈开发者，掌握高级 React 和 Next.js 概念，构建真实世界的 SaaS 产品。
- 🛠️ **技术栈**：涵盖 Next.js 16、React 19、Prisma、Supabase、TypeScript、Tailwind CSS、Stripe 等现代工具。
- 📚 **课程结构**：包含“Web 开发者之旅”和“软件工程师之旅”两个学习路径，从基础到高级，逐步深入。
- 🧑‍🏫 **讲师背景**：由经验丰富的软件工程师 Robin Wieruch 授课，拥有多年开发和咨询经验。
- 🎯 **适合人群**：适合前端开发者转型全栈、希望提升至高级水平、或想学习后端开发的学习者。
- 💡 **学习方式**：结合视频课程、实践项目和社区支持，提供自定进度的学习体验。
- 💰 **价格与优惠**：提供两个课程包，价格分别为 $249 和 $349，支持学生折扣、分期付款和 14 天退款保证。
- 🌍 **附加价值**：包含证书、Discord 社区访问权限和终身访问权，助力学员在技术领域取得成功。

---

### [Depx | 依赖关系分析](https://depx.co/badge)

**原文标题**: [Depx | Dependency analysis](https://depx.co/badge)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时也提及了相关的伦理挑战和未来发展趋势。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 💊 机器学习加速新药研发流程，大幅降低临床试验成本与周期
- 🧬 基于基因数据的个性化治疗方案正成为精准医疗的核心发展方向
- ⚖️ 医疗 AI 面临数据隐私、算法透明度与责任界定等伦理监管挑战
- 🌐 远程医疗与可穿戴设备结合 AI 技术，推动预防性医疗体系革新

---

### [代码降临 2025](https://adventofcode.com/)

**原文标题**: [Advent of Code 2025](https://adventofcode.com/)

从今年开始，每年十二月将有为期 12 天的谜题挑战。

- 🧩 谜题活动在十二月举行
- 📅 持续 12 天
- 🎯 每年固定举办
- 🗓️ 从今年开始实施

---

### [Let's Encrypt：将证书有效期缩短至 45 天](https://letsencrypt.org/2025/12/02/from-90-to-45.html)

**原文标题**: [
Decreasing Certificate Lifetimes to 45 Days -  Let's Encrypt
](https://letsencrypt.org/2025/12/02/from-90-to-45.html)

Let's Encrypt 将于 2028 年前将证书有效期从 90 天缩短至 45 天，并缩短授权重用期至 7 小时，以遵循行业安全标准并提升互联网安全性。这一变更将分阶段实施，用户可通过 ACME 配置文件控制生效时间。建议用户检查自动化工具兼容性，并启用 ACME Renewal Information（ARI）功能以确保及时续期。同时，Let's Encrypt 正在开发新的 DNS-PERSIST-01 验证方法，以简化域名控制验证流程。

- 🔐 证书有效期将从 90 天逐步缩短至 45 天，授权重用期从 30 天减至 7 小时，以提升安全性
- 📅 变更分三阶段实施：2026 年 5 月推出可选 45 天证书配置，2027 年 2 月默认证书改为 64 天，2028 年 2 月全面过渡至 45 天证书
- ⚙️ 多数自动化用户无需操作，但需确保系统兼容短有效期证书并启用 ARI 功能监控续期状态
- 🌐 将推出 DNS-PERSIST-01 新型验证方法，允许一次性设置 DNS 记录实现长期自动续期，无需频繁更新
- 📢 建议订阅技术更新邮件列表并查阅年度报告，以获取最新动态和详细指南

---

### [GitHub - trekhleb/javascript-algorithms: 📝 使用 JavaScript 实现的算法和数据结构，附带解释和进一步阅读链接](https://github.com/trekhleb/javascript-algorithms)

**原文标题**: [GitHub - trekhleb/javascript-algorithms: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings](https://github.com/trekhleb/javascript-algorithms)

这是一个用 JavaScript 实现算法和数据结构的开源项目，包含详细解释和进一步阅读链接，适合学习和面试准备。

- 📚 项目包含大量 JavaScript 实现的算法与数据结构，每个都有独立说明文档
- 🌍 支持多语言文档，包括中文、英文、日文等十几种语言版本
- 🏗️ 涵盖基础到高级的数据结构，如链表、树、图、堆、哈希表等
- ⚙️ 实现多种算法，包括排序、搜索、数学、字符串、加密、机器学习等类别
- 📊 提供算法范式分类，如分治法、动态规划、回溯、贪心算法等
- 🧪 包含测试环境与 playground，方便用户实践与测试代码
- 📈 附有 Big O 复杂度分析和数据结构操作对比表
- 🤝 采用 MIT 开源协议，欢迎社区贡献和赞助支持

---

### [异步 JavaScript 入门 - Piccalilli](https://piccalil.li/javascript-for-everyone/lessons/48)

**原文标题**: [
  Introduction to Asynchronous JavaScript - Piccalilli
](https://piccalil.li/javascript-for-everyone/lessons/48)

本文介绍了 JavaScript 的异步编程概念，重点解释了事件循环、回调函数和 Promise 机制，帮助理解单线程环境下如何处理非阻塞操作。

- 🧵 JavaScript 在单个执行域（如浏览器标签页）中是单线程的，但可通过 Web Workers 实现多线程
- 🔄 事件循环模型管理异步任务，包括回调队列和微任务队列，确保主线程不被阻塞
- ⏳ 异步操作（如`setTimeout`、`fetch`）通过回调函数在条件满足后执行，不中断主线程运行
- 🎯 Promise 提供更优雅的异步处理方式，代表未来可能完成的操作结果
- 🌐 前端性能优化需关注“长任务”，避免过多复杂 JavaScript 阻塞主线程影响用户体验

---

### [JavaScript 面向所有人 - 课程概览 - Piccalilli](https://piccalil.li/javascript-for-everyone/lessons)

**原文标题**: [
  JavaScript for Everyone - Course overview - Piccalilli
](https://piccalil.li/javascript-for-everyone/lessons)

这是一门名为“JavaScript for Everyone”的免费在线课程，由 Piccalilli 提供，旨在全面系统地教授 JavaScript 编程语言，涵盖从基础语法到高级概念的广泛内容。

- 📚 **课程介绍** – 包含欢迎模块、JavaScript 历史回顾及严格模式的重要性
- 🔤 **词法语法** – 讲解词法分析、空白字符、注释、大小写敏感性和表达式等基础概念
- 🧱 **原始类型** – 深入介绍数字、字符串、布尔值、null 与 undefined、BigInt 和 Symbol 等基本数据类型
- 📦 **变量** – 涵盖标识符、声明与作用域、解构赋值等变量相关主题
- 🗂️ **索引集合** – 专注于数组的创建、元素访问和扩展语法
- 🔑 **键控集合** – 介绍 Set、WeakSet、Map 和 WeakMap 等数据结构
- 🏗️ **对象** – 详细讲解对象属性创建与访问、原型继承和属性描述符
- 🔄 **可迭代对象与迭代器** – 包括迭代协议、迭代器和相关概念
- ⚙️ **函数** – 涵盖函数定义与调用、生成器函数、构造函数及 this 关键字
- 🏛️ **类** – 介绍类的定义与调用、方法属性、公共/私有/静态字段及类继承
- ⏳ **异步 JavaScript** – 深入讲解 Promise 创建与消费、异步函数等异步编程概念
- 🎯 **课程总结** – 包含结束语和致谢部分

---

### [GitHub - Hans-Halverson/brimstone: 用 Rust 编写的新 JavaScript 引擎](https://github.com/Hans-Halverson/brimstone)

**原文标题**: [GitHub - Hans-Halverson/brimstone: New JavaScript engine written in Rust](https://github.com/Hans-Halverson/brimstone)

Brimstone 是一个用 Rust 从头编写的 JavaScript 引擎，旨在完整支持 JavaScript 语言，目前仍在开发中，尚未准备好投入生产使用。

- 🚀 **项目概述**：Brimstone 是一个用 Rust 编写的新 JavaScript 引擎，目标是完全支持 JavaScript 语言。
- 📜 **规范遵循**：实现了 ECMAScript 规范，并大量借鉴了 V8 和 LibJS 的设计。
- 🛠️ **核心特性**：包含字节码虚拟机、紧凑型垃圾回收器、自定义正则表达式引擎和解析器，以及大多数内置对象和函数。
- 🧪 **测试与构建**：支持通过 Cargo 构建和运行，使用 test262 等测试套件进行集成测试，并提供模糊测试。
- ⚠️ **缺失功能**：已实现 ES2024 及大部分阶段 4 提案，但暂不支持 SharedArrayBuffer 和 Atomics。
- 📊 **项目状态**：在 GitHub 上获得 1.1k 星标和 27 个分支，采用 MIT 许可证，主要使用 Rust 开发。

---

### [JavaScript 引擎动物园](https://zoo.js.org/)

**原文标题**: [JavaScript engines zoo](https://zoo.js.org/)

该内容为 JavaScript 引擎的技术规格与项目元数据概览。

- 🚀 **引擎** - 核心执行环境
- 📊 **分数** - 性能或兼容性评分
- 🔢 **二进制** - 编译后的可执行格式
- 📏 **代码行数** - 项目规模指标
- 💬 **语言** - 实现所用的编程语言
- ⚡ **即时编译** - 运行时优化技术
- 📅 **年份** - 开发周期或版本历史
- 🎯 **目标** - 设计目的或运行平台
- 📜 **ES1-5** - 早期 ECMAScript 标准支持
- 🔷 **ES6** - ECMAScript 2015 标准支持
- 🆕 **ES2016+** - 最新 ECMAScript 特性支持
- ⭐ **星标** - 项目受欢迎程度
- 👥 **贡献者** - 开发团队规模
- 🏢 **组织** - 维护机构
- 📄 **许可证** - 开源授权协议
- 📝 **描述** - 项目功能简介

---

