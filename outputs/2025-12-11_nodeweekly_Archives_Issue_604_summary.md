### [Node Weekly Issue 604: December 9, 2025](https://nodeweekly.com/issues/604)

**原文标题**: [Node Weekly Issue 604: December 9, 2025](https://nodeweekly.com/issues/604)

总结失败：Expecting value: line 10 column 1 (char 9)

---

### [Publications](https://cooperpress.com/publications/)

**原文标题**: [Publications](https://cooperpress.com/publications/)

我们通过一系列电子邮件摘要帮助开发者及其所在公司保持技术前沿，总订阅量超过 46 万，邮件打开率高达 30% 至 60%。

- 📧 **JavaScript 周刊**：最受欢迎的简报，面向 17 万 + JavaScript 与全栈开发者，涵盖 React、Node.js 等生态
- 🎨 **前端聚焦**：专注网页设计与浏览器技术，涵盖 HTML/CSS/WebGL 等现代 Web 平台 API
- 💎 **Ruby 周刊**：Ruby 社区首选读物，自 2010 年起汇集 Rails 生态最新动态
- ⚙️ **Node 周刊**：原为 JavaScript 周刊分支，现已成为独立的 Node.js 技术权威简报
- 🚀 **Golang 周刊**：Go 语言领域领先刊物，服务快速增长的后端开发社区
- ⚛️ **React 动态**：专注 React 与 React Native 的垂直简报，订阅量已达 4 万
- 🗄️ **Postgres 周刊**：聚焦全球最受欢迎的开源关系数据库 PostgreSQL

---

### [我们如何保护新闻编辑室免受 npm 供应链攻击 | pnpm](https://pnpm.io/blog/2025/12/05/newsroom-npm-supply-chain-security)

**原文标题**: [How We're Protecting Our Newsroom from npm Supply Chain Attacks | pnpm](https://pnpm.io/blog/2025/12/05/newsroom-npm-supply-chain-security)

《西雅图时报》新闻编辑室通过采用 pnpm 的三层客户端安全控制来防御 npm 供应链攻击，包括默认阻止生命周期脚本、设置发布冷却期和实施信任策略，构建了深度防御体系，确保在必须例外处理时仍有多重保护。

- 🛡️ **采用 pnpm 的客户端安全控制**：作为 npm 的补充防御，通过生命周期脚本管理、发布冷却期和信任策略三层控制，防止安装恶意包。
- ⚠️ **默认阻止生命周期脚本**：使用`strictDepBuilds: true`使安装遇到脚本时立即失败，强制团队审查并决定是否允许，避免自动执行恶意代码。
- ⏳ **设置发布冷却期**：通过`minimumReleaseAge`延迟安装新发布包，给予社区检测恶意软件的时间，降低供应链攻击风险。
- 🔒 **实施信任策略**：利用`trustPolicy`阻止认证强度降低的包安装，防止攻击者利用被盗凭证发布恶意版本。
- 🧩 **深度防御实践**：三层控制协同工作，允许在必要时为合法原因（如关键安全补丁）例外处理，同时其他层仍提供保护。
- 🚀 **试点经验与推广**：在单个后端服务中成功实施，耗时仅数小时，计划逐步扩展至其他代码库，强调从警告转向严格控制的必要性。

---

### [快速、节省磁盘空间的包管理器 | pnpm](https://pnpm.io/)

**原文标题**: [Fast, disk space efficient package manager | pnpm](https://pnpm.io/)

pnpm 是一个快速、高效且严格的包管理器，支持单体仓库，并拥有独特的依赖管理方式。

- 🚀 速度比 npm 快两倍
- 💾 通过硬链接或克隆共享存储，节省磁盘空间
- 📦 内置支持单体仓库管理
- 🔒 默认创建非扁平化 node_modules，提升依赖安全性

---

### [Node.js — 2025 年 12 月 15 日星期一安全更新发布](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

**原文标题**: [Node.js — Monday, December 15, 2025 Security Releases](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

Node.js 项目将于 2025 年 12 月 15 日或之后发布多个版本的安全更新，以修复高、中、低严重性漏洞，影响包括 25.x、24.x、22.x 和 20.x 等多个发布线，建议用户及时更新至最新版本以确保系统安全。

- 🚨 **安全更新发布**：Node.js 计划于 2025 年 12 月 15 日或之后发布安全更新，涵盖 25.x、24.x、22.x 和 20.x 版本线。
- ⚠️ **漏洞严重性**：涉及 3 个高严重性、1 个中严重性和 1 个低严重性安全问题，所有受影响的版本线均需修复。
- 📅 **发布计划**：更新将在指定日期或稍后时间提供，用户需关注发布进度并及时应用补丁。
- 🔗 **支持与政策**：生命周期结束的版本仍会收到安全修复，建议参考发布计划保持系统更新，安全策略和漏洞报告流程详见官方文档。
- 📧 **信息订阅**：可通过 nodejs-sec 邮件列表获取安全公告和更新信息，确保及时了解漏洞动态。

---

### [使用 Memetria K/V 构建 — Memetria](https://dashboard.memetria.com/nodeweekly/)

**原文标题**: [Build with Memetria K/V — Memetria](https://dashboard.memetria.com/nodeweekly/)

Memetria 提供兼容 Valkey 和 Redis OSS 的键值存储服务，支持无缝扩展、加密连接和详细监控，并提供从开发到高性能的多层级托管方案。

- 🛠️ 兼容 Valkey 和 Redis OSS，支持轻松导入导出
- 📈 无缝扩展，调整规模无需停机
- 🔐 提供双重加密和 TLS 专属连接选项
- 📊 详细监控，包含健康、内存和性能图表
- 💼 提供三种方案：开发版（共享资源，最高 250 MB）、生产版（专属资源，最高 3.5 GB）和性能版（专属资源、高 I/O、高速 CPU，包含高可用性）
- 🌍 支持多个 AWS 区域，包括非洲、亚太、欧洲、北美和南美等地
- 📋 注册需同意服务条款、隐私政策和最终用户许可协议

---

### [不再有令牌！锁定 npm 发布工作流程—zachleat.com](https://www.zachleat.com/web/npm-security/)

**原文标题**: [No more tokens! Locking down npm Publish Workflows—zachleat.com](https://www.zachleat.com/web/npm-security/)

近期一系列 npm 安全事件暴露了发布工作流的风险，作者通过审查自身项目（特别是 11ty）的安全措施，总结出一份强化 npm 发布安全性的清单。

- 🔐 **强制双因素认证**：为 GitHub 和 npm 的所有发布者启用 2FA，并使用密码管理器避免钓鱼攻击。
- 🗑️ **清理现有令牌**：删除 GitHub 和 npm 中所有遗留的访问令牌，实现“无令牌”环境。
- 🔗 **启用可信发布者**：在 npm 包设置中切换至 OIDC（Trusted Publishers），将凭证范围限定到特定 GitHub Action 工作流。
- 🚫 **限制发布权限**：在 npm 包设置中要求 2FA 并禁用令牌，减少未授权发布风险。
- 📦 **锁定依赖版本**：提交 lock 文件（如 package-lock.json），在发布脚本中使用`npm ci`而非`npm install`。
- 📌 **固定 GitHub Action 依赖**：在工作流配置中为`uses`操作指定完整 SHA 值，避免依赖劫持。
- 🛡️ **其他建议措施**：启用 GitHub 不可变发布、设置依赖更新冷却期、减少第三方依赖数量，并考虑使用虚拟机或权限模型隔离环境。

---

### [Eleventy 是一款更简洁的静态网站生成器](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

Eleventy 是一款简单、快速且灵活的静态网站生成器，支持多种模板语言，无需客户端 JavaScript，适合构建高性能网站。

- 🚀 **快速构建**：Eleventy 的构建速度远超其他主流静态网站生成器，处理大量文件时效率显著。
- 🛠️ **灵活配置**：支持零配置启动，也可通过配置文件深度定制，兼容多种模板语言（如 Markdown、Liquid、JavaScript 等）。
- 🌐 **无框架依赖**：默认不注入客户端 JavaScript，强调渐进增强，确保网站长期可维护性。
- 📂 **结构自由**：不强制特定目录结构，允许增量式迁移，仅处理指定文件，保留项目原有组织方式。
- 🔒 **稳定可靠**：自 2017 年发布以来更新稳定，被 NASA、Google 等知名机构使用，且不收集用户数据。
- 🌍 **活跃社区**：拥有热情的开发者社区，提供丰富的插件、文档和教程，支持快速上手和进阶使用。

---

### [TypeScript 7 进展 - 2025 年 12 月 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

**原文标题**: [Progress on TypeScript 7 - December 2025 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

TypeScript 7.0（代号“Corsa”）的开发进展顺利，其原生编译器与语言服务已进入预览阶段，性能显著提升，并计划作为 TypeScript 6.0 之后的下一个主要版本发布。

- 🚀 **性能大幅提升**：原生编译器（tsgo）在完整构建中相比 TypeScript 6.0 有近 10 倍速度提升，并支持多线程并行构建。
- 🔧 **编辑器支持完善**：VS Code 扩展预览版已提供代码补全（含自动导入）、跳转定义、重命名等核心语言服务功能，日常使用稳定。
- ✅ **类型检查高度兼容**：TypeScript 7.0 的类型检查已接近完成，在数千个测试用例中与 6.0 的错误检测结果基本一致。
- 📦 **编译器功能就绪**：支持增量编译（--incremental）、项目引用和构建模式（--build），大多数项目可无缝尝试。
- ⚠️ **注意变更与限制**：将移除部分已弃用功能（如--target es5），JavaScript/JSDoc 类型检查更严格，且暂不完全支持旧版 API 与低版本 ES 目标编译。
- 🛑 **版本过渡明确**：TypeScript 6.0 将是最后一个基于 JavaScript 代码库的版本，后续主要开发将集中在 7.0 上，以加速原生生态成熟。
- 📢 **鼓励开发者试用**：团队邀请用户通过 VS Code 扩展和 npm 包（@typescript/native-preview）体验预览版，并反馈问题以帮助完善。

---

### [TypeScript 6.0 将成为最后一个基于 JavaScript 的重大版本...](https://socket.dev/blog/typescript-6-0-will-be-the-last-javascript-based-major-release)

**原文标题**: [TypeScript 6.0 Will Be the Last JavaScript-Based Major Relea...](https://socket.dev/blog/typescript-6-0-will-be-the-last-javascript-based-major-release)

npm 已撤销经典令牌，要求维护者迁移至 OIDC，但 OpenJS 警告新方案仍存在安全风险，关键项目需谨慎评估。

- 🔐 GitHub 撤销 npm 经典发布令牌，强制维护者迁移至 OIDC 可信发布方案
- ⚠️ OpenJS 基金会指出 OIDC 方案存在权限管理漏洞，可能影响高敏感项目安全
- 🔄 维护者需重新配置发布流程，但需结合项目风险评估是否完全依赖 OIDC
- 📅 截至 2025 年 12 月，npm 生态正处安全过渡期，部分关键环节仍需加固

---

### [10 倍速 TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

**原文标题**: [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScript 团队宣布正在开发原生版本编译器，旨在大幅提升性能，预计将使构建速度提升 10 倍、编辑器启动速度提升 8 倍，并显著降低内存占用。该版本计划于 2025 年中发布命令行检查工具，年底提供完整的项目构建和语言服务支持。

- 🚀 原生版本 TypeScript 编译器将带来 10 倍构建速度提升和 8 倍编辑器加载加速
- ⏱️ 已在 VS Code、Playwright 等大型代码库测试中实现约 10 倍性能改进
- 💻 编辑器语言服务操作（如代码补全、跳转定义）响应速度将显著提高
- 📅 预计 2025 年中发布命令行版本，年底提供完整功能支持
- 🔧 采用 Go 语言重写，代码库已在 GitHub 开源
- 🧠 更低延迟将为 AI 编程工具提供更强大的语义信息支持
- 📊 内存使用量预计减少约 50%
- 🔄 将迁移至语言服务器协议（LSP）以更好兼容多语言环境
- 🗺️ 当前 JavaScript 代码库将继续维护为 TypeScript 6.x 系列
- 🎯 原生版本将作为 TypeScript 7.0 发布，两个版本将并行维护

---

### [我们如何让@platformatic/kafka 提速 223%（以及沿途的收获）](https://blog.platformatic.dev/how-we-made-platformatickafka-223-faster-and-what-we-learned-along-the-way)

**原文标题**: [How We Made @platformatic/kafka 223% Faster (And What We Learned Along the Way)](https://blog.platformatic.dev/how-we-made-platformatickafka-223-faster-and-what-we-learned-along-the-way)

本文介绍了 Platformatic 团队如何通过修正基准测试方法，发现并优化了@platformatic/kafka 客户端的性能瓶颈，最终使其单消息生产者吞吐量提升了 223%，并在多个场景下超越了其他主流 Kafka 客户端。

- 🔍 **基准测试方法修正**：团队发现原有测试方法存在缺陷，通过改为逐操作计时、确保消息送达确认及扩大样本量，获得了更准确可靠的性能数据。
- 🚀 **性能显著提升**：优化后，@platformatic/kafka v1.21.0 的单消息生产者吞吐量达到 92,441 次/秒，比 v1.16.0 版本提升 223%，批量处理和消费者性能也分别提升 18% 和 9%。
- ⚙️ **关键优化措施**：包括采用 Rust 原生 CRC32C 校验库、重构异步错误处理、修复元数据请求中的回调错误，以及改进背压处理机制。
- 📊 **方差大幅降低**：单消息生产者的性能方差从±34.18% 降至±1.05，显著提升了生产环境中的性能可预测性和稳定性。
- 🏗️ **架构优势**：纯 JavaScript 实现通过最小化缓冲区复制、直接协议实现、非阻塞事件循环和热路径优化等设计，避免了原生绑定的跨语言调用开销。
- 🤝 **社区贡献价值**：多个关键性能优化和错误修复来自社区贡献，体现了开源协作的重要性。
- 📈 **综合性能领先**：在单消息、批量处理和消费者场景中，@platformatic/kafka 均表现优异，尤其在性能一致性方面优于其他基于 C 语言实现的客户端。

---

### [GitHub - platformatic/kafka](https://github.com/platformatic/kafka)

**原文标题**: [GitHub - platformatic/kafka](https://github.com/platformatic/kafka)

这是一个用于 Apache Kafka 的现代、高性能、纯 TypeScript/JavaScript 类型安全客户端库。

- 🚀 **高性能**：针对速度进行了优化。
- 🧩 **纯现代 JavaScript**：使用最新的 ECMAScript 功能构建，无需原生插件。
- 🔒 **类型安全**：提供完整的 TypeScript 支持和强类型。
- 🔄 **灵活的 API**：所有 API 都支持 Promise 或回调函数。
- 🌊 **流式或事件驱动消费者**：借助 Node.js 流，可以选择首选的消费方式。
- 🛠️ **灵活的序列化**：支持可插拔的序列化和反序列化器。
- 🔗 **连接管理**：自动连接池和恢复机制。
- 📦 **低依赖**：外部依赖极少。
- 📚 **全面功能**：提供生产者、消费者和管理员客户端 API。
- 🛡️ **错误处理**：定义了清晰的错误层次结构，便于调试。
- 📈 **性能调优**：内部优化以减少事件循环开销，支持高水位线配置。
- 📄 **丰富文档**：包含详细的 API 参考和示例代码。

---

### [在 Node.js 中使用 fs.promises.glob 替换 glob-all – SiteLint](https://www.sitelint.com/blog/replacing-glob-all-with-fs-promises-glob-in-node-js)

**原文标题**: [Replacing glob-all with fs.promises.glob in Node.js – SiteLint](https://www.sitelint.com/blog/replacing-glob-all-with-fs-promises-glob-in-node-js)

本文介绍了在 Node.js 22.2 及以上版本中，如何用内置的`fs.promises.glob`替代第三方`glob-all`包来简化代码、减少依赖并优化打包体积。

- 🚀 **替代优势**：使用 Node.js 内置功能，无需额外安装`glob-all`包，减少依赖并简化代码。
- 🔄 **语法转换**：将`glob-all`的`ignore`选项替换为`fs.promises.glob`的`exclude`，注意排除路径需使用通配符模式（如`some/dir/**`）。
- ⚠️ **注意事项**：`fs.promises.glob`不支持否定模式（如`!foo.js`），且对非法模式或权限错误会抛出异常，建议在生产代码中使用`try…catch`包装。
- 📦 **使用示例**：通过`fs.promises.glob`匹配文件路径，并可结合`Array.fromAsync`在迭代时转换路径。
- ✅ **核心收益**：利用原生功能提升代码效率与可维护性，同时减小项目打包体积。

---

### [使用 JSDoc 探索 JavaScript 类型化的细微差别 | That HTML 博客](https://thathtml.blog/2025/12/nuances-of-typing-with-jsdoc/)

**原文标题**: [The Nuances of JavaScript Typing using JSDoc | That HTML Blog](https://thathtml.blog/2025/12/nuances-of-typing-with-jsdoc/)

作者偏好使用 JavaScript 而非 TypeScript，认为代码应专注于行为本身，而类型信息应作为文档注释存在。通过 JSDoc 注释结合 TypeScript 工具，可以在纯 JavaScript 项目中实现类型检查和编辑器提示，无需编写.ts 文件。

- 📝 类型信息应作为代码注释而非代码本身，JSDoc 是实现这一理念的理想工具  
- 🔧 在.js 文件顶部添加`// @ts-check`，配合 JSDoc 注释即可获得 TypeScript 的类型检查能力  
- ⚙️ 通过`jsconfig.json`和`tsconfig.json`配置类型检查行为，可生成声明文件并集成到 CI 流程  
- 📚 JSDoc 支持类构造函数参数、对象类型、循环变量和内联函数参数等多种类型标注场景  
- 🛡️ 特殊情况下可使用`// @ts-ignore`临时跳过类型检查，保持代码灵活性  
- 🌐 建议将“JavaScript + JSDoc + tsc”作为行业标准，在保持原生 JS 兼容性的同时获得类型安全优势

---

### [如何利用 GitHub Copilot Spaces 更快地调试问题 - GitHub 博客](https://github.blog/ai-and-ml/github-copilot/how-to-use-github-copilot-spaces-to-debug-issues-faster/)

**原文标题**: [How to use GitHub Copilot Spaces to debug issues faster - The GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-use-github-copilot-spaces-to-debug-issues-faster/)

GitHub Copilot Spaces 通过整合项目文件、文档和问题，为 Copilot 提供上下文，从而加速调试过程，生成基于实际代码的精准解决方案。

- 🚀 **创建知识空间**：将仓库、文件、问题和设计文档打包成空间，为 Copilot 提供项目背景
- 🎯 **添加自定义指令**：指导 Copilot 基于空间内容生成计划，并引用相关文件确保准确性
- 🔍 **智能调试问题**：Copilot 分析空间中的问题与文档，提出具体修复目标和步骤
- 📝 **自动生成拉取请求**：通过 Copilot 编码代理直接创建包含更改说明和参考来源的 PR
- 🔄 **灵活迭代与分享**：可在 PR 中与 Copilot 交互优化，或共享空间给团队以促进协作
- 💡 **多场景应用**：适用于代码调试、功能规划以及团队知识共享与新人培训

---

### [GitHub - poppinss/ts-exec：使用SWC在Node上执行TypeScript](https://github.com/poppinss/ts-exec)

**原文标题**: [GitHub - poppinss/ts-exec: Execute TypeScript on Node using SWC](https://github.com/poppinss/ts-exec)

ts-exec 是一个基于 SWC 构建的 TypeScript 即时编译器，允许在 Node.js 中直接运行 TypeScript 和 JavaScript 代码，无需预编译步骤，并完全支持 Node.js 24 及更高版本的 ESM 模块。

- 🚀 **基于 SWC 的 TypeScript 即时编译器**：无需构建步骤即可在 Node.js 中直接运行 `.ts` 和 `.tsx` 文件。
- 🛡️ **生产安全的导入规则**：严格遵循 Node.js 模块解析规则，确保开发与生产环境行为一致。
- ⚡ **现代化轻量设计**：代码少于 200 行，性能高效且零配置依赖。
- 🎨 **完整 TypeScript 支持**：支持枚举、旧版装饰器、命名空间导入和 JSX 语法。
- 📦 **原生 ESM 优先**：为 ECMAScript 模块提供一流支持，自动解析 `tsconfig.json`。
- 🔄 **智能导入扩展处理**：支持 `rewriteRelativeImportExtensions` 配置，自动转换 `.ts` 扩展名。
- 📍 **子路径导入别名兼容**：支持 `package.json` 中定义的导入别名，确保开发与编译后路径一致。
- ⚖️ **与 tsx/ts-node 对比优势**：解决 tsx 的扩展名省略和目录导入兼容性问题，同时支持旧版装饰器。

---

### [AdonisJS - 一款功能齐全的 Node.js 网络框架](https://adonisjs.com/)

**原文标题**: [AdonisJS - A fully featured web framework for Node.js](https://adonisjs.com/)

AdonisJS 是一个功能丰富的现代 Node.js 框架，提供类型安全、高性能和出色的开发体验。它内置了众多核心功能与官方维护的包，并拥有强大的测试工具和活跃的社区支持。

- 🛡️ **类型安全与智能提示**：框架 API 设计注重类型安全，提供无缝的智能感知和自动导入支持。
- 📦 **ESM 原生支持**：充分利用现代 JavaScript 特性，包括 ES 模块和 Node.js 子路径导入。
- ⚡ **高性能核心**：内置最快的验证库之一，HTTP 服务器性能与 Fastify 相当。
- 🧩 **功能丰富的单一核心包**：一个 npm 包即提供创建 Web 应用所需的所有基础功能（如路由、中间件、加密、文件上传等），无需组装大量第三方包，开箱即用。
- 🧪 **世界级的测试体验**：测试不是事后考虑，提供管理测试数据库、模拟依赖、生成假数据、进行浏览器和 Open API 测试等强大工具。
- 📚 **大量官方维护的包**：提供一系列官方维护、文档完善的包，涵盖 ORM (Lucid)、认证 (Auth)、授权 (Bouncer)、文件存储 (FlyDrive)、模板引擎 (Edge)、验证 (VineJS) 等众多领域。
- 🏗️ **架构与工具**：包含零配置的 IoC 容器、功能强大的 CLI、安全原语（CORS、CSRF 防护等），并支持 Vite 和 Inertia 等现代前端集成。
- 🌍 **积极的社区反馈**：开发者称赞其优秀的文档、类似 Laravel 的舒适体验、高生产力和合理的认知负荷，被认为是 Node.js 生态中极具价值的全栈框架。
- ❤️ **开源与赞助**：项目在 MIT 许可下独立运营，依靠 GitHub 赞助商的支持维持发展。

---

### [Node.js — 原生运行 TypeScript](https://nodejs.org/en/learn/typescript/run-natively)

**原文标题**: [Node.js — Running TypeScript Natively](https://nodejs.org/en/learn/typescript/run-natively)

Node.js 现已支持直接运行 TypeScript 代码，无需预先转译，简化了开发流程。

- 🚀 **无需转译**：在 Node.js v22.18.0 及以上版本中，可直接运行仅包含可擦除 TypeScript 语法的代码，无需任何标志。
- ⚙️ **版本兼容**：低于 v22.18.0 的版本需使用 `--experimental-strip-types` 标志来直接运行 TypeScript 文件。
- 🔧 **高级功能**：v22.7.0 引入了 `--experimental-transform-types` 标志，支持需转换的 TypeScript 语法（如 `enum` 和 `namespace`），并自动启用类型剥离。
- ⚠️ **使用注意**：`--experimental-transform-types` 为可选标志，仅当代码需要时使用；可通过 `--no-experimental-strip-types` 禁用类型剥离。
- 📋 **配置建议**：Node.js 的 TypeScript 加载器（Amaro）不依赖 `tsconfig.json`，但建议配置编辑器和 `tsc` 以匹配 Node.js 行为，使用 TypeScript 5.7 或更高版本。
- 🔗 **了解更多**：详细约束和 API 信息可参考官方文档。

---

### [GitHub - poppinss/ts-exec：使用SWC在Node上执行TypeScript](https://github.com/poppinss/ts-exec?tab=readme-ov-file#-why-ts-exec-exists)

**原文标题**: [GitHub - poppinss/ts-exec: Execute TypeScript on Node using SWC](https://github.com/poppinss/ts-exec?tab=readme-ov-file#-why-ts-exec-exists)

ts-exec 是一个基于 SWC 构建的 TypeScript 即时编译器，允许在 Node.js 中直接运行 TypeScript 和 JavaScript 文件，无需预先编译步骤。它严格遵循 Node.js 模块解析规则，确保开发与生产环境行为一致，提供完整的 TypeScript 功能支持，并优先兼容 ECMAScript 模块。

- 🚀 **基于 SWC 的 TypeScript 即时编译器**：无需构建步骤，直接在 Node.js 中运行 .ts 和 .tsx 文件。
- 🛡️ **生产安全的导入规则**：强制使用 Node.js 模块解析，避免开发与生产环境的不一致问题。
- ⚡ **完整的 TypeScript 支持**：包括枚举、旧版装饰器、命名空间导入和 JSX 语法。
- 📦 **ESM 优先设计**：为 Node.js 24 及以上版本提供原生 ECMAScript 模块支持。
- 🪶 **轻量级实现**：代码库少于 200 行，受 Amaro 启发，零配置需求。
- 🔄 **自动解析配置**：自动读取 tsconfig.json，支持 rewriteRelativeImportExtensions 选项。
- 📝 **导入路径处理**：推荐在导入中使用 .js 扩展名，或通过配置启用 .ts 扩展名重写。
- 🏷️ **子路径导入别名**：支持在 package.json 中定义别名，始终指向编译后的 .js 文件。
- ⚖️ **与 tsx 和 ts-node 对比**：相比 tsx，更严格遵循 Node.js 规则；相比 ts-node，更轻量且维护活跃。
- 📦 **安装与使用简单**：通过 npm 安装，支持命令行和编程式使用方式。

---

### [获取失败](https://nodeweekly.com/link/178158/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/178158/web)

无法总结：获取内容失败，状态码 520。

---

### [介绍 iceberg-js：Apache Iceberg 的 JavaScript 客户端](https://supabase.com/blog/introducing-iceberg-js)

**原文标题**: [Introducing iceberg-js: A JavaScript Client for Apache Iceberg](https://supabase.com/blog/introducing-iceberg-js)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 💊 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 🧬 基于患者基因组数据的 AI 模型可为个体提供定制化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任界定等伦理监管问题

---

### [Vercel 发布新 npm 包：自动修复流式 Markdown 中断问题](https://vercel.com/changelog/new-npm-package-for-automatic-recovery-of-broken-streaming-markdown)

**原文标题**: [New npm package for automatic recovery of broken streaming markdown - Vercel](https://vercel.com/changelog/new-npm-package-for-automatic-recovery-of-broken-streaming-markdown)

Remend 是一个独立的 JavaScript 包，专门用于智能处理 AI 流式输出中常见的未完成 Markdown 语法，确保其在任何应用程序中都能被正确渲染。

- 📦 **独立发布**：Remend 原本是 Streamdown 的一部分，现已作为独立库（`npm i remend`）发布，可集成到任何应用中。
- 🤖 **解决核心问题**：AI 模型逐令牌流式输出 Markdown 时，常产生未闭合的代码块、粗体标记、链接或列表，导致渲染失败或布局混乱。
- 🛠️ **自动补全**：它能自动检测并补全未终止的 Markdown 块，在流式传输中提供稳定、干净的输出。
- 🔌 **即插即用**：可作为任何 Markdown 渲染器的预处理步骤，与 unified 等工具链无缝配合。
- 🧪 **经过实战检验**：已在 Streamdown 及生产级 AI 应用中经过测试，能智能处理数学表达式、产品代码、嵌套链接等复杂边缘情况。
- 🚀 **快速上手**：可通过 Streamdown 使用，或直接通过 `npm i remend` 安装独立库。

---

### [GitHub - vercel/streamdown：专为AI驱动流式处理设计的react-markdown直接替代方案。](https://github.com/vercel/streamdown)

**原文标题**: [GitHub - vercel/streamdown: A drop-in replacement for react-markdown, designed for AI-powered streaming.](https://github.com/vercel/streamdown)

Streamdown 是一个专为 AI 驱动的流式传输设计的 Markdown 渲染库，可作为 react-markdown 的直接替代品，旨在优雅处理流式传输中不完整或未终止的 Markdown 内容。

- 🚀 **直接替代**：作为 react-markdown 的即插即用替代方案
- 🔄 **流式优化**：专门处理流式传输，能优雅应对不完整的 Markdown 内容
- 🎨 **未终止块解析**：使用 remend 构建，提升流式传输质量
- 📊 **GitHub 风格 Markdown**：支持表格、任务列表和删除线
- 🔢 **数学公式渲染**：通过 KaTeX 支持 LaTeX 方程
- 📈 **Mermaid 图表**：可将代码块渲染为图表并提供渲染按钮
- 🎯 **代码语法高亮**：使用 Shiki 实现美观的代码块
- 🛡️ **安全优先**：内置 rehype-harden 确保安全渲染
- ⚡ **性能优化**：采用记忆化渲染以实现高效更新

---

### [发布 v6.1.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v6.1.0)

**原文标题**: [Release v6.1.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v6.1.0)

该页面展示了 GitHub Actions 中 setup-node 项目的发布页面，详细介绍了 v6.1.0 版本的更新内容与社区互动情况。

- 🚀 **版本发布**：v6.1.0 版本于 12 月 3 日由维护者正式发布，包含多项功能优化与依赖更新  
- 🔧 **功能增强**：移除了 always-auth 配置处理逻辑，简化了身份验证流程  
- 📦 **依赖升级**：全面更新了@actions/cache、actions/checkout 和 js-yaml 等核心依赖包版本  
- 📚 **文档完善**：新增了仅恢复缓存功能的操作示例说明文档  
- 👥 **社区贡献**：本次更新汇集了三位贡献者的代码提交与问题修复  
- 💝 **用户反馈**：版本发布后获得社区用户的表情符号积极互动与认可

---

### [GitHub - openai/openai-node：OpenAI API 官方 JavaScript / TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

OpenAI 官方提供的 JavaScript/TypeScript 库，用于便捷访问 OpenAI REST API，支持多种运行时环境和高级功能。

- 📦 **官方库与安装**：提供 npm 和 JSR 两种安装方式，支持 Node.js、Deno、Bun 等多种运行时环境。
- 🔌 **核心 API 使用**：支持 Responses API 和 Chat Completions API 生成文本，包含流式响应和文件上传功能。
- 🔐 **Webhook 验证**：提供签名验证方法，支持解析和验证 OpenAI 发送的 Webhook 请求。
- 🛡️ **错误处理**：包含详细的 API 错误类型分类（如 BadRequestError、RateLimitError）和请求 ID 追踪。
- ⚡ **实时 API**：通过 WebSocket 支持低延迟、多模态对话体验，包括文本和音频输入输出。
- ☁️ **Azure 集成**：提供 AzureOpenAI 类专门用于 Microsoft Azure OpenAI 服务。
- 🔁 **自动重试与分页**：默认自动重试特定错误，支持列表接口的自动分页迭代。
- ⏱️ **超时配置**：可自定义请求超时时间，默认 10 分钟。
- 📊 **日志记录**：支持多级别日志（debug、info、warn 等），可配置自定义日志记录器。
- 🛠️ **高级定制**：允许自定义 fetch 客户端、代理配置、访问未文档化接口和参数。
- ❓ **常见问题**：遵循语义化版本，明确列出支持的运行时环境和浏览器使用的安全注意事项。

---

### [GitHub - jsdom/jsdom: 一个用于 Node.js 的多种 Web 标准的 JavaScript 实现](https://github.com/jsdom/jsdom)

**原文标题**: [GitHub - jsdom/jsdom: A JavaScript implementation of various web standards, for use with Node.js](https://github.com/jsdom/jsdom)

jsdom 是一个用于 Node.js 的纯 JavaScript Web 标准实现库，主要用于模拟浏览器环境以支持 Web 应用测试和爬虫开发。

- 🚀 **核心功能**：实现了 WHATWG DOM 和 HTML 标准，可在 Node.js 中模拟浏览器环境。
- ⚙️ **基础用法**：通过 `JSDOM` 构造函数解析 HTML 字符串，生成包含 `window` 等属性的虚拟 DOM 对象。
- 🔧 **自定义配置**：支持通过选项设置 URL、引用来源、内容类型等，以调整文档解析和资源加载行为。
- ⚠️ **脚本执行**：默认禁用内联脚本执行，需通过 `runScripts: "dangerously"` 显式启用（存在安全风险）。
- 🖥️ **视觉模拟**：通过 `pretendToBeVisual` 选项可模拟浏览器渲染状态，启用 `requestAnimationFrame` 等 API。
- 📦 **资源加载**：默认不加载子资源（如脚本、样式），可通过 `resources: "usable"` 启用，并支持自定义 `ResourceLoader`。
- 📟 **虚拟控制台**：提供 `VirtualConsole` 自定义日志输出，可转发或处理 jsdom 内部错误及页面控制台调用。
- 🍪 **Cookie 管理**：支持 `CookieJar` 管理 HTTP Cookie，影响文档 API 和子资源请求。
- 🔗 **高级 API**：提供 `fromURL()`、`fromFile()` 和 `fragment()` 等便捷方法，用于从 URL、文件或 HTML 片段创建 DOM。
- 🛠️ **扩展支持**：集成 `canvas` 包可为 `<canvas>` 元素提供 Canvas API 支持，并支持通过二进制数据自动检测编码。
- ⏳ **异步挑战**：异步脚本加载无内置完成检测，需通过页面回调或轮询等外部方式处理。
- ❌ **未实现功能**：暂不支持页面导航和 CSS 布局计算，相关 API 可能返回模拟值或触发错误。

---

### [发布版本 34.0.0 · photostructure/exiftool-vendored.js · GitHub](https://github.com/photostructure/exiftool-vendored.js/releases/tag/34.0.0)

**原文标题**: [Release Release 34.0.0 · photostructure/exiftool-vendored.js · GitHub](https://github.com/photostructure/exiftool-vendored.js/releases/tag/34.0.0)

这是一个关于 exiftool-vendored.js 项目发布 34.0.0 版本的页面，其中包含版本更新内容、提交记录和错误提示信息。

- 📦 项目发布了 34.0.0 版本，主要包含 API 变更、错误修复和依赖升级。
- 🔧 由于 batch-cluster v16.0.0 的更新，移除了 `maxReasonableProcessFailuresPerMinute` 选项和 `fatalError` 事件。
- 🐛 修复了 `stdin.write()` 错误导致进程残留的问题，现在会正确结束进程。
- ⏱️ 默认任务超时时间从 20 秒调整为 30 秒。
- 🔄 升级了 ExifTool 至版本 13.43。
- 📝 更新了相关文档和配置，修复了拼写和链接问题。
- 🧪 添加了针对任务超时处理的回归测试。

---

### [发布 9.0.1 版本 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.0.1)

**原文标题**: [Release 9.0.1 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.0.1)

该页面显示 Mongoose 库 9.0.1 版本的 GitHub 发布页面，其中包含错误提示、版本更新详情及社区互动信息。

- 🐛 页面加载时出现多个错误提示，需重新加载
- 🏷️ 最新版本为 9.0.1，发布于 2025 年 12 月 5 日
- ⚡ 性能优化：使用原生 Buffer.equals() 进行缓冲区比较
- 🔧 修复了 overwriteImmutable 选项与时间戳功能冲突的问题
- 🧩 改进了批量写入和枚举值的一致性处理
- 📚 更新了迁移指南、深色模式支持等文档
- 👥 社区有 4 次点赞和 1 次爱心表情互动

---

### [GitHub - bdeitte/hot-shots: Node.js 客户端，适用于 statsd、DogStatsD 和 Telegraf](https://github.com/bdeitte/hot-shots)

**原文标题**: [GitHub - bdeitte/hot-shots: Node.js client for statsd, DogStatsD, and Telegraf](https://github.com/bdeitte/hot-shots)

hot-shots 是一个 Node.js 客户端，支持 StatsD、DogStatsD 和 Telegraf 的 StatsD 服务器，提供丰富的配置选项和多种协议支持，适用于性能监控和数据收集。

- 📦 **多协议支持** – 支持 UDP、TCP、Unix Domain Socket（UDS）和原始流协议，适应不同部署环境。
- 🏷️ **标签与全局标签** – 支持为指标添加标签，可配置全局标签，并自动集成 Datadog 环境变量标签。
- 🔧 **丰富配置选项** – 提供主机、端口、前缀、采样率、错误处理等灵活参数，支持环境变量配置。
- 📊 **多种指标方法** – 支持增量、减量、直方图、分布、测量、集合、计时等多种指标类型，以及事件和服务检查。
- ⏱️ **计时与异步计时** – 提供同步和异步计时器，方便测量代码执行时间并自动发送指标。
- 🧩 **子客户端与嵌套** – 支持创建子客户端，为特定指标组添加额外前缀、后缀和标签。
- 🛡️ **错误处理与调试** – 可配置错误处理回调，支持通过 `NODE_DEBUG` 环境变量启用详细调试日志。
- 📈 **缓冲与重试机制** – 支持指标缓冲发送，提供 UDS 协议下的自动重试和退避策略，增强可靠性。
- 🧪 **模拟模式** – 提供模拟客户端，用于测试而不实际发送数据，方便开发和验证。
- 🔄 **活跃维护与社区** – 项目持续更新，遵循语义化版本，支持 TypeScript 类型，并有详细的变更记录和贡献指南。

---

### [pnpm 10.25 | pnpm](https://pnpm.io/blog/releases/10.25)

**原文标题**: [pnpm 10.25 | pnpm](https://pnpm.io/blog/releases/10.25)

pnpm 10.25 版本改进了证书处理，新增了基础初始化功能，并提供了多项体验优化。

- 🔐 支持为特定注册表 URL 配置内联证书，与 npm 行为保持一致
- 📄 新增 `pnpm init --bare` 标志，可创建仅含必需字段的 package.json 文件
- 📊 改进了被忽略依赖脚本的报告机制
- 🔧 安装时自动构建已添加至 onlyBuiltDependencies 但尚未构建的依赖
- 🚀 发布命令支持强制发布已存在版本
- ⚠️ 避免因缺少时间字段导致的信任策略检查错误

---

### [发布 7.1.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.1.0)

**原文标题**: [Release 7.1.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.1.0)

Prisma ORM 发布了 7.1.0 稳定版本，带来了多项质量改进和错误修复，包括对 pnpm 单仓库的支持、SQL 注释功能增强、错误消息优化以及社区贡献的更新。同时，读副本扩展已支持 Prisma v7，并引入了 SQL 注释功能，允许用户为查询添加元数据以提升可观测性。此外，还提供了企业支持信息和招聘机会。

- 🐛 修复了 pnpm 单仓库中与 Prisma 客户端运行时工具相关的 TypeScript 问题
- 🏷️ 实现了 SQL 注释器插件支持，允许为查询添加元数据（如跟踪标签和上下文）
- 🛠️ 新增了无参数创建 PrismaClient 实例时的错误提示，由社区贡献
- 📦 将 @opentelemetry/api 标记为外部依赖，避免重复打包
- 🔧 允许 env() 辅助函数接受基于接口的泛型，移除类型限制
- 🔄 读副本扩展现在支持 Prisma v7，用户可通过更新安装使用
- 💬 引入了 SQL 注释功能，支持通过插件添加查询标签、跟踪上下文和自定义元数据
- 🧩 提供了与 Hono、Express、Koa 等流行框架的集成示例
- 💼 提供了企业支持计划，包括优先问题处理和性能调优
- 👥 感谢社区贡献者 xio84 和 SaubhagyaAnubhav 的参与

---

### [Prettier 3.7：提升格式化一致性并新增插件功能！· Prettier](https://prettier.io/blog/2025/11/27/3.7.0)

**原文标题**: [Prettier 3.7: Improved formatting consistency and new plugin features! · Prettier](https://prettier.io/blog/2025/11/27/3.7.0)

Prettier 3.7 版本发布，重点提升了 TypeScript 和 Flow 的格式化一致性，特别是类和接口的格式对齐，同时修复了大量错误，新增了对 Angular 21 和 GraphQL 16.12 的支持，并为插件开发者提供了更多控制评论附加和忽略节点的 API。

- 🛠️ **提升 TypeScript/Flow 一致性**：对齐类和接口的格式化规则，移除类中类型参数的额外缩进，使输出更统一。
- 🐛 **修复大量错误**：包括 JavaScript 中的注释处理、CSS 选择器格式化、HTML 事件处理器等多项问题。
- 🔌 **新增语言支持**：支持 Angular 21 的新赋值操作符和正则表达式，以及 GraphQL 16.12 的可执行描述。
- 📝 **插件 API 增强**：允许插件更精细地控制评论附加、处理忽略节点，并支持异步预处理和自定义忽略节点打印。
- 🚀 **其他改进**：包括 CLI 缓存优化、YAML 文档标记保留、Markdown 表格对齐修复等。

---

### [发布 0.45.0 版本 · drizzle-team/drizzle-orm · GitHub](https://github.com/drizzle-team/drizzle-orm/releases/tag/0.45.0)

**原文标题**: [Release 0.45.0 · drizzle-team/drizzle-orm · GitHub](https://github.com/drizzle-team/drizzle-orm/releases/tag/0.45.0)

该页面为 Drizzle ORM 在 GitHub 上的项目仓库，显示版本 0.45.0 的发布信息，但页面加载时出现错误提示。

- 🔧 修复了 node-postgres 事务中 pg-native 连接池的检测问题
- 📊 允许在查询字段中使用子查询功能
- ✏️ 修正了拼写错误：将"algorythm"改为"algorithm"
- ⚙️ 修复了$onUpdate 未处理 SQL 值的问题（解决 issue #2388）
- 🗓️ 修正了 pg 映射器在 bun-sql:postgresql 驱动中处理 Date 类型数据的问题
- 📈 该版本获得了 29 个社区反应（6 个庆祝表情和 23 个爱心表情）

---

### [Bun 加入 Anthropic | Bun 博客](https://bun.com/blog/bun-joins-anthropic)

**原文标题**: [Bun is joining Anthropic | Bun Blog](https://bun.com/blog/bun-joins-anthropic)

Bun 已被 Anthropic 收购，将作为 Claude Code、Claude Agent SDK 及未来 AI 编程产品的核心基础设施。Bun 保持开源、公开开发，团队与路线不变，但将获得更多资源以加速发展，并更紧密地融入 AI 编程工具生态。

- 🚀 **Bun 被 Anthropic 收购**：将作为 Claude Code 等 AI 编程工具的基础设施，获得长期资源支持。
- 🔓 **开源承诺不变**：保持 MIT 许可证，代码公开开发，团队继续专注高性能 JavaScript 工具链。
- ⚡ **性能与兼容性持续优化**：重点提升 Node.js 兼容性、替代 Node.js 作为默认服务端运行时。
- 🤖 **深度集成 AI 编程生态**：通过单文件可执行文件支持 Claude Code 等工具，加速 AI 代理开发。
- 📈 **发展历程回顾**：从个人项目到月下载量超 720 万，经历多版本迭代，逐步成为生产级工具。
- 🧠 **收购逻辑**：AI 编程工具崛起使运行时和工具链更为关键，Bun 与 Anthropic 合作可跳过商业化探索阶段。
- 🔮 **未来方向**：聚焦 AI 驱动软件的开发、运行与测试，同时保持通用 JavaScript 工具的卓越性。

---

### [Bun v1.3.4 | Bun 博客](https://bun.sh/blog/bun-v1.3.4)

**原文标题**: [Bun v1.3.4 | Bun Blog](https://bun.sh/blog/bun-v1.3.4)

Bun 发布了新版本，包含安装与升级指南、新增功能如 URLPattern API 和测试假定时器、fetch() 代理头支持，以及多项错误修复与性能改进。

- 🚀 支持多种安装方式：通过 curl、npm、PowerShell、Scoop、Homebrew 或 Docker 安装 Bun，升级只需运行 `bun upgrade`
- 🔗 新增 URLPattern Web API：用于 URL 模式匹配，支持路由和参数提取，适用于 Web 服务器和框架
- ⏱️ 测试假定时器：`bun:test` 支持假定时器，可控制时间以测试 `setTimeout` 等定时器相关代码
- 🌐 fetch() 代理头自定义：代理选项现支持对象格式，可添加自定义头部如代理认证令牌
- 🔧 http.Agent 连接池修复：修复了 `keepAlive: true` 时连接未正确复用的错误
- 📦 独立可执行文件优化：默认不加载运行时配置文件，提升启动性能，可通过标志重新启用
- 📝 console.log 支持 %j 格式：现可输出 JSON 字符串化值，匹配 Node.js 行为
- 🗃️ SQLite 更新：`bun:sqlite` 升级至 v3.51.1，包含查询优化器修复
- 🐛 多项错误修复：涵盖测试、打包器、安装、Windows 兼容性、Node.js API 和 Bun 内部功能，提升稳定性和安全性

---

### [欢迎收听 VS Code 内幕播客](https://code.visualstudio.com/blogs/2025/12/03/introducing-vs-code-insiders-podcast)

**原文标题**: [Introducing the VS Code Insiders Podcast](https://code.visualstudio.com/blogs/2025/12/03/introducing-vs-code-insiders-podcast)

VS Code 团队推出官方播客“VS Code Insiders Podcast”，深入探讨编辑器幕后开发故事、新功能设计及 AI 编程未来趋势，并提供最新内测版本体验渠道。

- 🎙️ 官方播客揭秘 VS Code 幕后开发故事，涵盖功能设计、AI 编程等前沿话题
- 👥 每期邀请开发者、产品经理及社区贡献者分享实验性工具与扩展深度解析
- ♿ 近期节目聚焦无障碍设计、AI 规划代理及开源社区建设等多元主题
- 🚀 推荐听众订阅播客并安装内测版，实时体验最新功能与更新日志

---

### [Cypress 测试技巧与窍门 | Gleb Bahmutov | Substack](https://cypresstips.substack.com/)

**原文标题**: [Cypress Testing Tips & Tricks | Gleb Bahmutov | Substack](https://cypresstips.substack.com/)

本文介绍了使用 Cypress 进行网页测试的实用技巧与策略，旨在帮助开发者提升测试效率与覆盖范围。

- 🧪 掌握 Cypress 核心功能，优化测试流程与稳定性  
- 🔧 学习高级调试技巧，快速定位并解决测试中的问题  
- 📚 获取实战经验分享，涵盖常见场景与最佳实践  
- 🚀 提升测试自动化水平，确保 Web 应用质量与可靠性

---

### [类型感知 Linting Alpha | JavaScript 氧化编译器](https://oxc.rs/blog/2025-12-08-type-aware-alpha)

**原文标题**: [Type-Aware Linting Alpha | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2025-12-08-type-aware-alpha)

Oxlint 宣布其类型感知 linting 功能进入 Alpha 阶段，该功能利用 TypeScript 类型系统实现强大的代码检查规则，显著提升了稳定性、可配置性和规则覆盖范围，性能相比 ESLint 有大幅提升。

- 🚀 **快速开始**：通过安装 `oxlint` 和 `oxlint-tsgolint` 并使用 `--type-aware` 标志，即可在几分钟内启用类型感知 linting。
- ⚡ **性能卓越**：基准测试显示，Oxlint 的类型感知 linting 速度比 ESLint 结合 typescript-eslint 快约 10 倍。
- 🆕 **新增功能**：自技术预览版以来，增加了在 linting 同时进行类型检查、规则配置支持、内联禁用注释支持以及更多规则（如 `no-deprecated`）等功能。
- 🔧 **技术架构**：采用独特的双二进制架构，由 Rust 编写的 `oxlint` CLI 处理前端任务，Go 编写的 `tsgolint` 处理后端类型分析，确保高效运行。
- 📈 **未来计划**：团队正致力于为 Beta 版增加更多规则、优化性能与内存使用，并解决大型代码库可能遇到的内存问题。
- 🐛 **已知问题**：在极大代码库中可能遇到内存不足的情况，团队正在优化，鼓励用户反馈以帮助改进。
- 🤝 **致谢**：感谢 TypeScript 团队、typescript-eslint 团队及贡献者 `@auvred` 和 `@camchenry` 的支持与工作。

---

### [新闻稿](https://web.archive.org/web/20070916144913/http://wp.netscape.com/newsref/pr/newsrelease67.html)

**原文标题**: [Press Release](https://web.archive.org/web/20070916144913/http://wp.netscape.com/newsref/pr/newsrelease67.html)

Netscape 与 Sun 公司联合推出 JavaScript，这是一种开放的跨平台对象脚本语言，旨在为企业网络和互联网创建在线应用程序，并得到 28 家行业领先公司的支持。

- 🌐 **开放跨平台语言**：JavaScript 是一种开放的跨平台对象脚本语言，专为企业网络和互联网的应用程序开发而设计。
- 🤝 **与 Java 互补**：JavaScript 作为 Java 的补充，适用于 HTML 页面作者和企业应用开发者，用于动态控制客户端或服务器端对象的行为。
- 📈 **行业广泛支持**：包括美国在线、苹果、甲骨文等 28 家行业领先公司已认可 JavaScript，并计划在未来产品中集成该语言。
- 🛠️ **易于使用**：类似 Visual Basic，JavaScript 适合编程经验有限的用户快速构建复杂应用，尤其适用于创建实时在线应用。
- 🔗 **客户端与服务器端运行**：JavaScript 脚本可在客户端和服务器端运行，用于连接和定制 Java 对象，扩展在线应用功能。
- 🌍 **推动开放标准**：Netscape 和 Sun 计划将 JavaScript 提交给 W3C 和 IETF，作为开放的互联网脚本语言标准，促进广泛采用。
- 💼 **企业应用场景**：可用于智能表单计算、多媒体交互、数据库动态内容生成等，提升企业网络和互联网应用的交互性。
- 🚀 **开发工具支持**：Netscape 提供 Navigator Gold、LiveWire 等工具，支持 JavaScript 应用的快速开发、部署和管理。

---

