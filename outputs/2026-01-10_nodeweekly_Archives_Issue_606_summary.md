### [Node周刊第606期：2026年1月8日](https://nodeweekly.com/issues/606)

**原文标题**: [Node Weekly Issue 606: January 8, 2026](https://nodeweekly.com/issues/606)

Node Weekly 第606期（2026年1月8日）概述了Node.js和JavaScript生态系统的最新动态，包括npm发布流程的重大变更、Node.js中ES模块加载的稳定性进展、性能优化案例，以及一系列新工具和库的发布。

- 🎉 Node Weekly 现已调整为每周四发送，作为通讯重组的一部分。
- 🔐 npm 将在2026年引入“分阶段发布”模式，为包发布增加审查期。
- 🧠 Agentic Postgres 数据库推出，旨在让AI代理能安全、直接地与PostgreSQL协同工作。
- ⚙️ Node.js 核心贡献者详细阐述了 `require(esm)` 功能从实验到稳定的实现过程。
- 🚀 文章分享了解决大型TypeScript项目性能问题的案例研究。
- 📊 新工具 npmgraph 可用于可视化npm模块的依赖关系图。
- 🎨 Fabric.js 7 发布，这是一个适用于浏览器和Node.js的HTML5 Canvas库。
- 🛡️ pnpm 10.27 版本更新，增强了包管理的安全性和配置选项。
- 🌐 生态圈动态包括新的微型JavaScript引擎、用JavaScript构建的Linux用户空间实验，以及HTML 2025年度调查报告结果公布。

---

### [出版物](https://cooperpress.com/publications/)

**原文标题**: [Publications](https://cooperpress.com/publications/)

我们通过一系列电子邮件摘要帮助开发者及其所在公司保持技术前沿，总订阅量超过46万，邮件打开率高达30%至60%。

- 📧 **JavaScript周刊**：最受欢迎的简报，面向17万以上JavaScript与全栈开发者，涵盖React、Node.js等生态
- 🎨 **前端聚焦**：专注网页设计与浏览器技术，涵盖HTML、CSS及WebGL等现代Web API
- 💎 **Ruby周刊**：Ruby社区首屈一指的刊物，自2010年起持续服务分散而多元的Ruby开发者群体
- 🟢 **Node周刊**：从JavaScript周刊独立发展的Node.js专项简报，已成为重要技术媒体
- 🐹 **Golang周刊**：Go语言领域领先的电子邮件刊物，服务近3万快速增长的开发生态
- ⚛️ **React动态**：专注React与React Native的技术简报，每周触达近4万订阅者
- 🐘 **Postgres周刊**：专攻PostgreSQL关系型数据库，覆盖全球最受欢迎的开源数据库生态

---

### [npm在动荡迁移后实施分阶段发布...](https://socket.dev/blog/npm-to-implement-staged-publishing)

**原文标题**: [npm to Implement Staged Publishing After Turbulent Shift Off...](https://socket.dev/blog/npm-to-implement-staged-publishing)

Socket CEO Feross Aboukhadijeh 在 Insecure Agents 播客中探讨了 CVE 修复、供应链安全及 AI 代理的挑战，强调应对供应链攻击需采用与传统漏洞管理不同的安全策略。

- 🛡️ 讨论 CVE 修复和供应链安全的重要性  
- 🔗 强调供应链攻击需要独特的安全应对方法  
- 🤖 涉及 AI 代理在安全领域的应用与挑战  
- 🎙️ 由 Socket CEO Feross Aboukhadijeh 参与播客分享见解

---

### [沙虫2.0：供应链攻击的检测、调查与防御指南 | 微软安全博客](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)

**原文标题**: [Shai-Hulud 2.0: Guidance for detecting, investigating, and defending against the supply chain attack | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)

Shai-Hulud 2.0是一次针对云原生生态系统的重大供应链攻击，通过恶意篡改数百个公开npm软件包，攻击开发者环境、CI/CD流水线及云工作负载，以窃取凭证和配置信息。攻击利用预安装脚本自动传播，并盗用知名项目维护者账户，凸显了现代软件供应链的深层风险。

- 🚨 **攻击机制**：恶意npm包通过预安装脚本`setup_bun.js`植入Bun运行时，下载GitHub Actions Runner并部署恶意代理`SHA1Hulud`，窃取云端凭证。
- 🔍 **检测与响应**：Microsoft Defender通过容器警报、无代理代码扫描及攻击路径分析，帮助识别威胁；建议客户检查密钥库、轮换凭证并隔离受影响环境。
- 🛡️ **防护建议**：启用云交付保护、攻击面缩减规则；npm维护者应启用可信发布与双因素认证，优先使用WebAuthn而非TOTP。
- 📊 **威胁狩猎**：提供多平台查询语句，用于监测恶意Node.js进程、GitHub外泄行为及密钥管理服务访问路径，支持快速调查。
- 🔗 **情报整合**：Microsoft Defender XDR与Sentinel提供检测分析、威胁情报报告及安全Copilot提示簿，协助自动化事件响应与影响评估。

---

### [npm安全更新：经典令牌创建已禁用及令牌粒度变更 - GitHub更新日志](https://github.blog/changelog/2025-11-05-npm-security-update-classic-token-creation-disabled-and-granular-token-changes/)

**原文标题**: [npm security update: Classic token creation disabled and granular token changes - GitHub Changelog](https://github.blog/changelog/2025-11-05-npm-security-update-classic-token-creation-disabled-and-granular-token-changes/)

npm 安全更新：自 2025 年 11 月 5 日起，禁用经典令牌创建并实施更精细的令牌管理变更，以增强 npm 注册表的安全性。

- 🔐 **经典令牌停用**：无法再创建新的 npm 经典令牌，现有令牌将在 11 月 19 日后失效。
- ⚙️ **精细令牌强化**：新创建的具有写入权限的令牌默认强制启用双因素认证（2FA），并为 CI/CD 工作流提供“绕过 2FA”选项。
- ⏳ **令牌有效期调整**：所有现有具有写入权限的精细令牌最长有效期调整为 90 天，部分令牌到期日统一调整为 2026 年 2 月 3 日。
- 🔄 **用户需采取行动**：使用经典令牌的用户需在 11 月 19 日前迁移至精细令牌；所有用户应检查令牌到期日并计划轮换。
- 🚫 **不影响的范围**：GitHub 个人访问令牌、精细令牌及 GitHub Actions 密钥不受此次变更影响。
- 📅 **未来计划**：11 月 19 日将永久撤销所有经典令牌，并将长期本地发布令牌替换为 2 小时会话令牌。

---

### [加强供应链安全：为下一次恶意软件攻击做好准备 - GitHub博客](https://github.blog/security/supply-chain-security/strengthening-supply-chain-security-preparing-for-the-next-malware-campaign/)

**原文标题**: [Strengthening supply chain security: Preparing for the next malware campaign - The GitHub Blog](https://github.blog/security/supply-chain-security/strengthening-supply-chain-security-preparing-for-the-next-malware-campaign/)

开源生态系统持续面临有组织、适应性的供应链威胁，这些威胁通过泄露的凭证和恶意包生命周期脚本传播。本文总结了持久的教训和行动，帮助维护者和组织强化系统，为未来的攻击做好准备，而不仅仅是应对上一次事件。文章还介绍了npm安全路线图的近期计划。

- 🐛 **Shai-Hulud攻击活动**：这是一个针对JavaScript供应链的协调性多波次攻击，从机会性入侵演变为有针对性、精心设计的攻击，利用维护者工作流程和CI发布管道中的信任边界。
- 🔐 **凭证相关入侵**：攻击者通过泄露的凭证或OAuth令牌获得初始立足点，然后收集更多秘密（如npm令牌、CI令牌、云凭证）以扩大影响范围，实现跨组织重用。
- ⚙️ **安装时执行与混淆**：恶意代码通过后安装或生命周期脚本注入包中，仅在运行时激活，并根据环境条件（如环境检查、组织范围）调整行为，以逃避检测。
- 🎯 **针对可信命名空间和内部包名**：攻击影响流行和受信任的包，并发布与现有包同名的受感染包，甚至通过修补版本号伪装成合法更新。
- 🔄 **快速迭代与绕过防御**：攻击变种间隔短，且故意改变以规避先前的缓解措施，表明攻击者具有组织性和持久访问的目标。
- 🛡️ **npm安全路线图更新**：包括批量OIDC集成、扩展OIDC提供商支持，以及引入分阶段发布功能，让维护者在包上线前有审查期，以MFA验证批准。
- 🔧 **通用安全建议**：为所有账户启用防钓鱼MFA，为令牌设置过期日期，审计并撤销未使用的GitHub/OAuth应用访问权限，使用沙箱（如GitHub Codespaces）进行开发工作。
- 🛠️ **维护者专项建议**：启用分支保护，使用npm可信发布替代令牌，固定CI依赖项，启用代码扫描并解决警报，监控包工件并验证发布文件与源代码的一致性。

---

### [代理专用Postgres | 虎数据](https://www.tigerdata.com/blog/postgres-for-agents?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for Agents | Tiger Data](https://www.tigerdata.com/blog/postgres-for-agents?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

Tiger Data 宣布推出专为 AI 代理设计的 Agentic Postgres 数据库，旨在帮助开发者更高效地构建 AI 应用，将重复性工作交给代理处理，从而专注于更高层次的架构与创新。

- 🚀 **推出 Agentic Postgres**：专为 AI 代理设计的数据库，内置 MCP 服务器，提供安全、结构化的数据库访问和高阶工具支持。
- 🔍 **集成搜索与检索功能**：支持原生全文搜索（pg_textsearch）和语义搜索（pgvectorscale），优化混合 AI 应用的查询性能。
- ⚡ **快速零拷贝分支**：基于 Fluid Storage 存储层，支持秒级创建轻量级数据分支，便于实验、测试和并行迁移，且仅按变更数据计费。
- 🛠️ **新 CLI 与免费层级**：提供全新命令行工具和免费服务，方便开发者与代理快速上手和体验。
- 🧠 **代理行为优化**：针对代理“调用而非点击”“检索而非记忆”等工作特点设计，提升开发效率与系统安全性。
- 📈 **高效存储架构**：采用 Fluid Storage 分布式存储，支持即时快照、自动扩缩容和高吞吐性能（单卷超 11 万 IOPS）。
- 🎯 **开发者赋能**：旨在让开发者与 AI 代理协同工作，将重心转向架构设计与创新，提升工程化能力而非仅停留在实验阶段。

---

### [Node.js中的require(esm)：从实验到稳定 | Joyee Cheung的博客](https://joyeecheung.github.io/blog/2025/12/30/require-esm-in-node-js-from-experiment-to-stability/)

**原文标题**: [require(esm) in Node.js: from experiment to stability | Joyee Cheung's Blog](https://joyeecheung.github.io/blog/2025/12/30/require-esm-in-node-js-from-experiment-to-stability/)

Node.js 中的 `require(esm)` 功能经过一年多的实验与迭代，现已作为稳定特性在所有支持的 LTS 版本中提供，显著降低了 ESM 的采用门槛，并有望加速生态系统的现代化迁移。

- 🚀 **实验到稳定**：`require(esm)` 经过多次测试与反馈，已在 Node.js v20.19.0+ 和 v22.12.0+ 中取消实验标志并标记为稳定。
- 🤝 **社区驱动**：该功能的实现得益于社区贡献者的协作、维护者的支持以及 Bloomberg 的赞助，体现了“众人拾柴火焰高”的力量。
- 🔄 **打破迁移僵局**：缺乏 `require(esm)` 曾导致 ESM 成为次优的发布格式，迫使许多包通过转译或双包模式兼容，增加了复杂性与风险。
- 📦 **简化发布流程**：支持 `require(esm)` 后，包作者可直接发布 ESM 格式，无需转译为 CommonJS，减少了构建开销和双包隐患。
- ⚡ **提升兼容性**：该功能允许 CommonJS 代码直接加载 ESM 模块，支持渐进式升级，降低了大规模代码库的迁移阻力。
- ⏳ **异步限制**：`require(esm)` 不支持顶层 `await`，但实际影响极小，仅极少数包受影响，且可通过动态 `import()` 替代。
- 🛠️ **设计原则**：实现遵循了向后兼容、渐进迁移、兼容打包工具、减少内部泄漏影响和保持合理性能的核心准则。
- 🔙 **向后移植**：该功能被向后移植到 v20 和 v22 LTS 版本，使更多项目能提前受益，并简化了包配置。

---

### [Node.js 中的 require(esm)：实现者的故事 | Joyee Cheung 的博客](https://joyeecheung.github.io/blog/2025/12/30/require-esm-in-node-js-implementers-tales/)

**原文标题**: [require(esm) in Node.js: implementer's tales | Joyee Cheung's Blog](https://joyeecheung.github.io/blog/2025/12/30/require-esm-in-node-js-implementers-tales/)

本文探讨了在 Node.js 中实现 `require(esm)` 功能时遇到的技术挑战与解决方案，重点在于确保与现有生态系统的兼容性。

- 🧩 **处理“伪ESM”包**：为保持与广泛使用的转译代码（通过 `__esModule` 标志识别ESM）的兼容性，Node.js 通过创建包含额外 `__esModule` 导出的ESM门面模块来返回命名空间对象。
- ⚙️ **CommonJS 的特殊导出**：引入了特殊的 `"module.exports"` 字符串命名导出，允许ESM模块自定义被 `require()` 加载时的返回值，以平滑迁移并保持对CommonJS消费者的兼容。
- 📦 **双包策略与条件导出**：为避免破坏已使用 `"module"` 条件的包，引入了新的 `"module-sync"` 导出条件，使包能同时支持支持 `require(esm)` 的新版Node.js和仅支持CommonJS的旧版。
- 🔧 **同步内置模块检测**：新增 `process.getBuiltinModule()` API，使ESM代码能同步检测和使用内置模块，减少了对顶层 `await` 和动态 `import()` 的依赖。
- 🏃 **防止竞态条件**：通过将ESM的获取和链接过程完全同步化，解决了与异步 `import()` 共享缓存时可能出现的罕见竞态问题。
- 🔄 **防范评估重入**：当前实现会检测并阻止在模块评估期间出现的ESM/CommonJS循环依赖导致的重新进入评估，未来可能通过“延迟模块评估”提案支持此类循环。

---

### [北欧.js 2025 • Joyee Cheung - 2025年Node.js包发布策略 - YouTube](https://www.youtube.com/watch?v=I0jvOJW7NaI)

**原文标题**: [Nordic.js 2025 • Joyee Cheung - Shipping Node.js packages in 2025 - YouTube](https://www.youtube.com/watch?v=I0jvOJW7NaI)

该页面为YouTube网站的页脚导航部分，列出了平台的关键政策、功能说明及法律信息。

- 📄 关于平台的基本信息与介绍
- 📢 媒体与新闻相关资源
- ©️ 版权政策与保护说明
- 📞 联系与反馈渠道
- 🧑‍🎨 创作者相关资源与服务
- 💼 广告与商业合作信息
- 👩‍💻 开发者工具与API资源
- ⚖️ 服务条款与使用协议
- 🔒 隐私政策与数据保护
- 🛡️ 平台安全与内容政策
- ⚙️ YouTube功能运作机制说明
- 🧪 新功能测试与更新信息
- 📅 版权年份及公司归属声明

---

### [Reddit - 互联网之心](https://www.reddit.com/r/node/comments/1plnmqb/why_nodejs_is_not_considered_enterprise_like_c/?rdt=62450)

**原文标题**: [Reddit - The heart of the internet](https://www.reddit.com/r/node/comments/1plnmqb/why_nodejs_is_not_considered_enterprise_like_c/?rdt=62450)

Node.js 虽被许多知名公司采用，但在企业级开发中仍被认为不如 C#/ASP.NET 成熟，未来可能随着生态发展而改变。

- 🏢 **企业传统偏好**：C#/ASP.NET 长期与微软生态绑定，在企业级工具、安全支持和合规性方面更受信赖。
- 🚀 **高性能应用场景**：Node.js 适合高并发I/O场景，但复杂计算或大型单体应用可能更倾向.NET的强类型和稳定性。
- 🔧 **开发与维护**：C# 静态类型和成熟框架利于大型团队协作与长期维护，Node.js 动态特性可能增加企业级项目的管理复杂度。
- 🌱 **生态发展**：Node.js 生态活跃但碎片化，.NET 提供更统一的企业级解决方案，如官方数据库工具和云服务集成。
- 📈 **未来潜力**：随着TypeScript普及和云原生趋势，Node.js 可能通过工具链完善逐渐缩小企业级差距。

---

### [快速、节省磁盘空间的包管理器 | pnpm](https://pnpm.io/)

**原文标题**: [Fast, disk space efficient package manager | pnpm](https://pnpm.io/)

pnpm 是一款高效、安全的 Node.js 包管理工具，特别适合单仓库项目，能显著提升安装速度并节省磁盘空间。

- 🚀 安装速度极快，优化依赖安装流程，节省开发时间
- 💾 采用智能存储机制，大幅减少磁盘空间占用
- 🏗️ 内置工作区支持，高效管理单仓库项目
- 🔒 增强安全性，通过最小发布延迟等机制防范供应链攻击
- ⚙️ 内置运行时管理及并行任务处理，优化构建流程
- 🌟 受到众多知名开源项目及企业赞助商采用
- 💬 用户反馈积极，认可其在开发体验和性能上的显著提升

---

### [🚀 pnpm 在 2025 年 | pnpm](https://pnpm.io/blog/2025/12/29/pnpm-in-2025)

**原文标题**: [🚀 pnpm in 2025 | pnpm](https://pnpm.io/blog/2025/12/29/pnpm-in-2025)

2025年是pnpm变革性的一年，主要聚焦于重新定义包管理的安全模型，同时在性能与开发者体验方面也取得了显著进展。

- 🛡️ **默认安全增强**：v10.0起默认阻止生命周期脚本执行，大幅减少供应链攻击风险，后续引入`allowBuilds`等配置实现更精细的构建控制。
- 🛡️ **深度防御机制**：新增`minimumReleaseAge`、`trustPolicy`等策略，在安装前拦截恶意包，并阻止可信依赖引入不可信子依赖。
- 💾 **全局虚拟存储**：v10.12引入全局虚拟存储功能，通过中央化链接依赖显著节省磁盘空间并加速安装过程。
- 📦 **原生JSR支持**：v10.9起支持JSR注册表，可直接通过`jsr:`协议安装包，并与npm依赖无缝集成。
- ⚙️ **配置依赖管理**：v10.0推出配置依赖功能，允许跨项目集中管理pnpm配置（如钩子、补丁和构建权限），确保版本一致性。
- 🔧 **自动运行时管理**：扩展至支持Node.js、Deno、Bun等多运行时，通过`devEngines.runtime`配置自动下载并使用指定版本。
- 🌐 **主页重新设计**：与赞助商Bit.cloud合作重构官网，采用Bit组件构建并引入AI辅助设计系统。
- 🎤 **社区影响力提升**：维护者在JSNation大会首次进行现场演讲，分享配置依赖主题，证实pnpm在开发者中的广泛采用。

---

### [修复TypeScript性能问题：案例研究 | Viget](https://www.viget.com/articles/fixing-typescript-performance-problems)

**原文标题**: [Fixing TypeScript Performance Problems: A Case Study | Viget](https://www.viget.com/articles/fixing-typescript-performance-problems)

本文分享了作者在大型TypeScript单体仓库中诊断和解决性能问题的经验，通过一系列工具和方法显著提升了编译速度和开发体验。

- 🛠️ **诊断步骤**：从更新工具、检查依赖等常规排查开始，使用`tsc --listFiles`和`tsc --explainFiles`验证文件包含，并通过`tsc --extendedDiagnostics`获取性能基线数据。
- 🔍 **深入分析**：利用`tsc --generateTrace`生成编译器跟踪文件，结合`@typescript/analyze-trace`分析热点，定位到特定文件类型检查耗时长达80秒。
- 🐌 **根本原因**：性能瓶颈源于使用`kysely`库的复杂泛型助手函数，其类型推断在大型数据库接口下导致指数级计算复杂度。
- ⚡ **优化措施**：删除问题助手函数并内联查询，同时修复循环依赖、清理未使用类型和依赖项、升级包版本等，大幅减少编译资源消耗。
- 📊 **显著成果**：构建时间从6.2分钟降至1.3分钟（提升79%），内存使用减少50%，类型检查时间下降83%，语言服务器响应速度和智能提示得到根本改善。

---

### [在Node.js脚本中自动加载.env文件 | Stefan Judis Web开发](https://www.stefanjudis.com/today-i-learned/load-env-files-in-node-js-scripts/)

**原文标题**: [Automatically load .env files in Node.js scripts | Stefan Judis Web Development](https://www.stefanjudis.com/today-i-learned/load-env-files-in-node-js-scripts/)

Node.js 现已原生支持加载.env文件，无需依赖第三方库如dotenv，提供了命令行标志和脚本内方法两种方式。

- 🚀 Node.js 新增原生支持加载.env文件，减少对dotenv等第三方库的依赖
- ⚙️ 可通过命令行标志`--env-file`和`--env-file-if-exists`或脚本内`loadEnvFile()`方法加载环境变量
- 📁 `loadEnvFile()`方法默认加载当前目录的.env文件，也支持自定义文件路径
- ⚠️ 需注意`loadEnvFile()`在.env文件不存在时会抛出错误，生产环境中建议使用错误处理包装
- 💡 作者分享了一个安全加载工具函数，可忽略文件不存在的错误，适用于生产环境
- 📅 该功能自Node.js v24起标记为稳定，体现了Node.js持续集成用户常用特性的发展趋势

---

### [Express 4与Express 5性能基准对比](https://www.repoflow.io/blog/express-4-vs-express-5-benchmark-node-18-24)

**原文标题**: [Benchmarking Express 4 vs Express 5](https://www.repoflow.io/blog/express-4-vs-express-5-benchmark-node-18-24)

本文对 Express 4 与 Express 5 在不同 Node 版本和场景下的性能进行了基准测试，结果显示 Express 5 在原始吞吐量上普遍略慢于 Express 4，尤其在轻量路由和中间件密集的场景中较为明显，但在处理大负载时差距缩小。

- 🚀 **测试范围**：涵盖 Node 18、20、22、24 版本及 Express 4.18.2、4.22.1、5.0.0、5.1.0、5.2.1 版本，通过四种场景（ping、50个中间件、JSON解析、100KB响应）对比请求每秒处理能力。
- 📊 **性能趋势**：在所有测试中，Express 5 的吞吐量均低于 Express 4，差异在轻量路由和中间件链较深时更为显著。
- ⚖️ **场景差异**：对于大负载或 JSON 密集型端点，两者性能差距减小甚至接近；若应用以小型响应或深层中间件为主，Express 4 仍能提供更高的每秒请求数。
- 🔄 **升级权衡**：升级至 Express 5 可获得新特性和长期维护支持，但需以牺牲部分峰值吞吐量为代价。

---

### [V8引擎中的预任期机制 — wingolog](https://wingolog.org/archives/2026/01/05/pre-tenuring-in-v8)

**原文标题**: [pre-tenuring in v8 — wingolog](https://wingolog.org/archives/2026/01/05/pre-tenuring-in-v8)

V8 中的预晋升机制通过动态监测分配点对象的存活率，将高存活率的对象直接分配到老生代空间，以减少垃圾回收开销和无效复制。该机制主要适用于对象字面量、数组字面量和 `new Array` 等特定分配场景。

- 🧠 **分配点与备忘录**：V8 使用 `AllocationSite` 对象记录程序中的分配点，并在分配对象后附加 `AllocationMemento` 指向对应分配点，用于追踪对象创建和存活情况。
- 📊 **动态决策机制**：当分配点累计创建 100 个对象后，系统会根据其存活率（默认阈值 85%）决定是否启用预晋升，并通过去优化和重新优化代码实现直接分配到老生代。
- 🔄 **条件重置**：如果主垃圾回收清理了超过 90% 的老生代对象，系统会重置所有预晋升标记，避免因过早晋升导致性能下降。
- ⚙️ **适用范围限制**：预晋升机制目前主要适用于对象字面量、数组字面量和 `new Array`，可能受历史实现和对象初始化方式的影响，其他分配场景（如类实例化）尚未全面支持。
- 🛠️ **特殊处理场景**：部分对象（如 WebAssembly 内存）和特定分配源（如引导程序、解析器字面量）会默认直接分配到老生代，无需动态决策。

---

### [如何使用静态Hermes将JavaScript编译为C](https://devongovett.me/blog/static-hermes.html)

**原文标题**: [How to compile JavaScript to C with Static Hermes](https://devongovett.me/blog/static-hermes.html)

本文介绍了如何使用静态Hermes将JavaScript编译为C代码，以便在Rust工具中嵌入JavaScript插件，从而提升性能并避免运行时解释器的开销。

- 🛠️ 作者在将Parcel移植到Rust时面临插件支持挑战，部分工具（如React Compiler、Less、Sass）仍基于JavaScript，需在Rust中运行。
- 🔄 现有方法包括通过napi嵌入Rust核心或跨进程通信，但均存在性能开销（如Lightning CSS中JS插件慢7倍）。
- ⚡ 静态Hermes是Facebook的JavaScript引擎，通过提前将JS编译为C代码（再经LLVM转为机器码），生成独立二进制文件，无需JS虚拟机，提升性能并易于嵌入其他语言（如Rust）。
- 📦 作者以Less.js为例，先用Parcel打包为无依赖的单一JS文件，暴露全局`compile`函数，再使用静态Hermes编译为C库（生成`less.o`对象文件）。
- 🔗 编写C包装器（`compile.c`）调用JS函数，编译为`compile.o`，最后在Rust中通过FFI调用C函数，链接所有对象文件和Hermes库，实现从Rust编译Less代码。
- 🚀 该方法展示了原生工具集成预编译JS插件的潜力，无需嵌入解释器，未来可能应用于React Compiler等JS工具，尽管目前存在一些未解决的问题。

---

### [仅用200行JavaScript实现JSON流式处理](https://krasimirtsonev.com/blog/article/streaming-json-in-just-200-lines-of-javascript)

**原文标题**: [Streaming JSON in just 200 lines of JavaScript](https://krasimirtsonev.com/blog/article/streaming-json-in-just-200-lines-of-javascript)

本文介绍了作者在探索渐进式JSON流技术时，开发了一个名为Streamson的小型库（约200行代码），用于在服务器和客户端之间分块传输JSON数据，以提升大型数据集的渲染性能。

- 🚀 **渐进式JSON流的核心思想**：服务器将JSON数据分块发送，客户端可提前渲染已接收部分，未就绪数据用占位符替代，从而改善用户体验。
- 🔧 **服务器实现**：使用NDJSON格式和分块传输编码，通过递归遍历数据对象，将Promise替换为占位符，待Promise解析后发送实际数据。
- 🌐 **客户端处理**：利用Fetch API读取流式响应，将占位符转换为Promise，并在数据到达时解析，实现动态数据替换。
- 📦 **Streamson库**：作者将代码封装为NPM包，提供简洁的服务器和客户端API，支持在Express等框架中快速集成流式JSON传输。
- ⚡ **性能优势**：该技术特别适用于大数据集或实时生成数据的场景，能显著减少用户等待时间，提升应用响应速度。

---

### [npmgraph - NPM 依赖关系图](https://npmgraph.js.org/)

**原文标题**: [npmgraph - NPM Dependency Diagrams](https://npmgraph.js.org/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🏥 AI辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能整合临床数据，减少行政负荷，提升医院运营效率
- ⚖️ 数据隐私与算法透明度等伦理问题仍需在技术发展中同步解决

---

### [Fabric.js JavaScript库](https://fabricjs.com/)

**原文标题**: [Fabric.js Javascript Library](https://fabricjs.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能整合病历信息，减少行政负担并降低人为错误
- 🔬 自然语言处理技术助力科研人员从海量文献中提取关键医学发现
- ⚖️ 数据隐私保护与算法透明度是目前AI医疗应用面临的主要伦理挑战

---

### [GitHub - Automattic/node-canvas: Node canvas 是一个基于Cairo的Canvas实现，适用于NodeJS。](https://github.com/Automattic/node-canvas)

**原文标题**: [GitHub - Automattic/node-canvas: Node canvas is a Cairo backed Canvas implementation for NodeJS.](https://github.com/Automattic/node-canvas)

node-canvas 是一个基于 Cairo 的 Node.js 画布实现，支持图像生成、PDF 和 SVG 输出，并提供了丰富的 API 和跨平台安装选项。

- 🎨 基于 Cairo 的 Node.js 画布实现，支持 Web Canvas API
- 📦 支持 PNG、JPEG、PDF 和 SVG 输出格式
- 🔧 提供跨平台安装，包括预编译二进制和源码编译选项
- 📚 包含实用方法如 `createCanvas`、`loadImage` 和 `registerFont`
- 🖼️ 支持图像处理、字体注册和多种像素格式
- 🧪 提供测试套件和示例代码，便于开发和调试
- 📄 支持多页 PDF 生成和超链接添加
- 🔄 兼容 Node.js 18.12.0 及以上版本

---

### [Fabric.js 演示示例](https://fabricjs.com/demos/)

**原文标题**: [Fabric.js Demos](https://fabricjs.com/demos/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发过程，大幅缩短化合物筛选与临床试验设计周期
- 📊 基于患者数据的个性化治疗方案正成为现实，AI可预测药物反应并优化治疗路径
- ⚖️ 数据隐私与算法透明度等伦理问题仍需建立完善的监管框架来解决

---

### [介绍客户信任：Clerk的免费凭证填充防护工具](https://clerk.com/changelog/2025-11-14-client-trust-credential-stuffing-killer?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=client-trust&utm_content=01-08-26&dub_id=zxgyHMpc7nXIPnjE)

**原文标题**: [Introducing Client Trust: Clerk’s free credential stuffing killer](https://clerk.com/changelog/2025-11-14-client-trust-credential-stuffing-killer?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=client-trust&utm_content=01-08-26&dub_id=zxgyHMpc7nXIPnjE)

Clerk推出名为Client Trust的免费功能，旨在通过自动要求新设备登录时进行二次验证，从根本上防止凭据填充攻击，且该功能全平台免费并自动启用。

- 🛡️ 针对近期大规模密码泄露引发的凭据填充攻击，Clerk推出了Client Trust防御机制
- 🔐 当用户在新设备使用正确密码登录且未开启双因素认证时，系统将自动要求二次验证
- ⚙️ 该功能无需额外配置，可自动平衡安全性与用户体验，默认对新应用启用
- 🆓 所有Clerk套餐均免费包含此功能，现有应用可通过控制台一键更新启用

---

### [pnpm 10.27 | pnpm](https://pnpm.io/blog/releases/10.27)

**原文标题**: [pnpm 10.27 | pnpm](https://pnpm.io/blog/releases/10.27)

pnpm 10.27版本引入了信任策略忽略设置、全局虚拟存储库的项目注册机制以支持垃圾回收，并包含多项错误修复。

- 🔐 新增`trustPolicyIgnoreAfter`设置，允许忽略对指定发布时间之前的包进行信任策略检查
- 📁 为全局虚拟存储库添加项目注册功能，支持通过`pnpm store prune`追踪并安全移除未使用的包
- 🗂️ 调整无作用域包在全局虚拟存储库中的存储位置，统一目录深度为四级
- 🧹 引入标记-清除垃圾回收算法，自动清理全局虚拟存储库中未使用的包
- ⚠️ 当`tokenHelper`设置包含环境变量时抛出错误
- 🔧 修复Git依赖构建脚本未遵循`dangerouslyAllowAllBuilds`设置的问题
- ⏭️ 使用`--global`参数时跳过包管理器检查并发出警告
- 🐛 修复`pnpm store prune`在dlx缓存目录包含文件时失败的问题
- 📝 修正`pnpm add`错误修改`pnpm-workspace.yaml`中目录条目的问题

---

### [GitHub - sindresorhus/file-type：检测文件、流或数据的文件类型](https://github.com/sindresorhus/file-type)

**原文标题**: [GitHub - sindresorhus/file-type: Detect the file type of a file, stream, or data](https://github.com/sindresorhus/file-type)

这是一个用于检测文件类型的Node.js库，通过检查文件的魔数（magic number）来识别二进制文件格式，支持从文件、缓冲区、流等多种来源进行检测。

- 📦 **功能概述**：通过魔数检测文件类型，支持多种输入源（文件、缓冲区、流等），返回扩展名和MIME类型
- 🛠️ **安装与使用**：通过npm安装，支持ESM模块，提供多种API如`fileTypeFromFile`、`fileTypeFromBuffer`等
- 🌐 **跨平台支持**：适用于Node.js和浏览器环境，支持Web流和Node.js流
- 🔧 **自定义检测**：允许添加自定义检测器，支持第三方检测器扩展功能
- 📄 **支持格式**：广泛支持常见二进制文件格式，如图像、音频、视频、文档等，但不支持纯文本格式（如.txt、.csv）
- ⚙️ **高级选项**：提供配置选项如自定义检测器、中止信号等，增强检测灵活性和控制
- 🔗 **相关资源**：包含CLI工具和与其他库的集成，社区活跃，有持续的维护和更新

---

### [GitHub - taoqf/node-html-parser: 一款极速HTML解析器，生成简化DOM，支持基础元素查询。](https://github.com/taoqf/node-html-parser)

**原文标题**: [GitHub - taoqf/node-html-parser: A very fast HTML parser, generating a simplified DOM, with basic element query support.](https://github.com/taoqf/node-html-parser)

这是一个名为node-html-parser的快速HTML解析器，它生成简化的DOM树并支持基本元素查询，性能优异，适用于处理大量HTML文件。

- 🚀 **性能卓越**：在多个HTML解析器基准测试中表现突出，解析速度极快。
- 🔧 **功能全面**：支持CSS选择器查询、DOM操作（如增删改元素）、属性管理等。
- 📦 **易于使用**：提供简洁的API，如`parse()`解析HTML，`querySelector()`查询元素。
- ⚙️ **高度可配置**：解析选项丰富，包括标签大小写转换、注释保留、修复嵌套标签等。
- 🛡️ **稳定可靠**：覆盖常见HTML格式错误，但可能无法处理所有畸形HTML。
- 📄 **类型支持**：完全兼容TypeScript（最低支持版本^4.1.2）。
- 🌐 **广泛应用**：被超过88万个项目使用，社区活跃（1.2k星，116个分支）。

---

### [升级 6.x 至 7.x | Middy.js](https://middy.js.org/docs/upgrade/6-7/)

**原文标题**: [Upgrade 6.x -> 7.x | Middy.js](https://middy.js.org/docs/upgrade/6-7/)

Middy 7.x 版本引入了对 Durable Functions 的支持，并带来了一些重大变更，包括执行模式的调整、部分中间件的更新以及不再支持 Node.js 20.x。以下是主要变更的概述：

- 🚀 新增对 Durable Functions 的支持，但暂不支持超时中止信号
- ⚠️ 不再支持 Node.js 20.x，建议升级至 Node.js 24.x
- 🔄 `streamifyResponse` 选项已弃用，改为使用 `executionModeStreamifyResponse`
- 🌐 新增 `executionModeStandard` 和 `executionModeDurableContext` 执行模式，支持 LLRT
- 🏢 兼容新的租户隔离模式和 Lambda 托管实例的多并发功能
- 📝 `input-output-logger` 中间件新增对 DurableContext 的支持，并将 `awsContext` 选项重命名为 `lambdaContext`
- 🔧 `http-content-encoding` 中间件新增 `zstd` 支持
- 🛡️ `http-security-headers` 中间件更新了 `poweredBy` 和 `xssProtection` 的默认行为
- 🧭 `http-router` 中间件优化了动态/静态路由的优先级处理

---

### [GitHub - vercel/nft: Node.js 依赖追踪工具](https://github.com/vercel/nft)

**原文标题**: [GitHub - vercel/nft: Node.js dependency tracing utility](https://github.com/vercel/nft)

Vercel 的 Node File Trace（NFT）是一个用于分析 Node.js 应用依赖关系的工具，能够精确追踪运行时所需的文件，包括 node_modules 和静态资源，实现依赖树摇优化而无需打包。

- 📦 **依赖追踪工具**：用于确定 Node.js 应用运行时所需的文件，包括 node_modules 和资源文件。
- 🔍 **无打包树摇**：类似 @vercel/ncc，但不进行打包，不依赖 webpack，实现相同的树摇效果。
- ⚙️ **灵活配置选项**：支持设置基础路径、进程工作目录、导出条件、自定义路径解析和钩子函数等。
- 📁 **高级功能**：支持 TypeScript 文件解析、文件 IO 并发控制、自定义分析选项和缓存机制。
- 📊 **输出详细信息**：提供文件列表和包含原因的对象，说明每个文件被包含的依据和父级引用关系。

---

### [Node与TypeScript的终极ORM](https://orange-orm.io/)

**原文标题**: [The ultimate ORM for Node and Typescript](https://orange-orm.io/)

Orange ORM 是一个面向 Node.js、Bun 和 Deno 的现代对象关系映射器，支持 TypeScript 和 JavaScript，提供丰富的查询模型、Active Record 模式，无需代码生成即可获得完整的智能感知。它支持多种数据库（如 PostgreSQL、MySQL、SQLite 等）和运行时环境，并可在浏览器中安全使用。此外，Orange ORM 还提供了灵活的数据操作功能，包括插入、更新、删除、事务处理以及高级查询和过滤能力。

- 🚀 **跨平台支持**：兼容 Node.js、Bun、Deno 和 Cloudflare 等多个运行时环境。
- 🗄️ **多数据库适配**：支持 PostgreSQL、MySQL、SQLite、MS SQL、Oracle 等多种数据库。
- 🌐 **浏览器端安全使用**：通过 Express.js 插件在浏览器中安全操作，避免暴露敏感数据库信息。
- 🔧 **无需代码生成**：提供完整的 TypeScript 智能感知，无需额外生成代码。
- 📊 **丰富的查询模型**：支持复杂的查询、过滤、聚合和关系加载。
- 🔄 **Active Record 模式**：使用简洁的语法进行数据库交互，支持关联数据的插入、更新和删除。
- 🛡️ **并发控制**：提供乐观、覆盖和跳过冲突等多种并发策略，确保数据一致性。
- 🔗 **灵活的关系映射**：支持一对一、一对多和多对多关系，并可定义级联操作。
- 📈 **数据聚合与统计**：支持计数、求和、平均值等聚合函数，可进行跨行或逐行计算。
- 🧪 **数据验证**：内置非空验证、自定义验证和 JSON 模式验证，确保数据完整性。
- 🔐 **安全性增强**：支持序列化排除敏感字段，防止数据泄露；提供原始 SQL 查询的安全限制。
- 📝 **日志记录**：可监听查询事件，方便调试和监控数据库操作。
- ⚙️ **高级功能**：支持复合主键、列鉴别器、公式鉴别器、默认值和事务处理。

---

### [发布 v1.11.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.11.0)

**原文标题**: [Release v1.11.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.11.0)

Repomix v1.11.0 版本发布，新增了 `--split-output` 选项，可将大型代码库的打包输出自动分割为多个文件，便于在具有文件大小限制的 AI 工具中使用。

- 🚀 新增 `--split-output` 选项，支持按指定大小（如 1MB、20MB）将输出分割成多个编号文件
- 📁 文件按顶级目录分组，确保单个文件或目录的完整性，避免跨文件分割
- 🔧 支持使用单位（如 kb、mb）和十进制数值指定分割大小
- 👏 此功能由贡献者 @Dango233 开发
- 📦 可通过 `npm update -g repomix` 命令更新工具

---

### [GitHub - bdeitte/hot-shots: Node.js 客户端，适用于 statsd、DogStatsD 和 Telegraf](https://github.com/bdeitte/hot-shots)

**原文标题**: [GitHub - bdeitte/hot-shots: Node.js client for statsd, DogStatsD, and Telegraf](https://github.com/bdeitte/hot-shots)

hot-shots 是一个 Node.js 客户端库，支持向 StatsD、DogStatsD 和 Telegraf 服务器发送指标数据，提供多种协议支持、丰富的配置选项和客户端功能。

- 📦 **支持多种服务器**：兼容 StatsD、Datadog 的 DogStatsD 和 InfluxDB 的 Telegraf 服务器。
- 🔧 **灵活的配置**：支持 UDP、TCP、UDS（Unix Domain Socket）和原始流协议，可配置主机、端口、标签、采样率等。
- 🏷️ **标签与采样**：支持为指标添加全局和自定义标签，并可通过采样率控制数据发送频率。
- 📊 **丰富的指标类型**：提供增量（increment）、计量（gauge）、直方图（histogram）、分布（distribution）、计时（timing）等多种方法。
- 🐕 **Datadog 专属功能**：支持事件（event）和服务检查（check），并可启用客户端遥测以监控客户端自身指标。
- 🔄 **高级特性**：包含子客户端、模拟模式、异步计时器、错误处理和连接优雅重启等功能。
- 📈 **调试与监控**：可通过环境变量启用调试日志，支持配置错误处理器来捕获各类错误。
- 📄 **社区维护**：项目遵循 MIT 许可，由社区驱动，接受贡献并注重版本管理与发布安全。

---

### [mquickjs/README.md 位于主分支 · bellard/mquickjs · GitHub](https://github.com/bellard/mquickjs/blob/main/README.md)

**原文标题**: [mquickjs/README.md at main · bellard/mquickjs · GitHub](https://github.com/bellard/mquickjs/blob/main/README.md)

QuickJS是一个由Fabrice Bellard开发的小型且可嵌入的JavaScript引擎，具有轻量级、高效和符合ECMAScript规范的特点。

- 🚀 高性能：QuickJS设计注重执行速度，支持即时编译（JIT）技术，提供快速的JavaScript代码运行性能。
- 📦 轻量嵌入：引擎体积小巧，适合嵌入到各种应用程序中，如物联网设备、桌面应用或服务器端工具。
- 🔧 标准兼容：全面支持ECMAScript 2020规范，包括现代JavaScript特性如模块、异步编程和类。
- 🛠️ 易于集成：提供简单的C API，方便开发者将JavaScript功能集成到现有C/C++项目中。
- 🌐 多用途：可用于脚本扩展、插件系统或作为独立的JavaScript解释器，适用于多种开发场景。

---

### [GitHub - popovicu/ultimate-linux：用JavaScript编写的终极Linux微发行版！一个功能强大的最小化Linux用户空间，完全由...纯JavaScript编写！虽不完全如此，但也差不多了。我保证，它真的很棒！](https://github.com/popovicu/ultimate-linux)

**原文标题**: [GitHub - popovicu/ultimate-linux: The Ultimate Linux micro distribution written in JavaScript! A very functional minimal userspace for Linux written in... pure JavaScript! Not quite, but almost. It's good, I promise!](https://github.com/popovicu/ultimate-linux)

这是一个用JavaScript编写的微型Linux发行版项目，旨在通过JavaScript（配合少量C代码）构建一个极简的Linux用户空间，探索Linux内核与用户软件的交互原理。

- 🐧 **项目目标**：创建一个不依赖libc的微型Linux发行版，主要使用JavaScript实现，用于演示Linux内核的系统调用接口
- 🔧 **技术实现**：基于QuickJS将JavaScript代码转译为C，并静态链接musl libc生成独立的可执行文件
- 🚀 **构建流程**：包含下载QuickJS、安装musl libc、编译转译、生成initramfs镜像并在QEMU虚拟机中运行
- 💻 **功能特性**：实现了一个简易Shell，支持ls、cd、cat、mkdir、mount、exit等基本命令
- 📖 **项目背景**：作者通过该项目回应关于Linux内核与操作系统关系的讨论，并探索Go、Rust等语言直接调用系统调用的可能性
- 🌐 **相关资源**：项目提供详细构建说明和演示，并推荐阅读作者关于微型Linux发行版的原理文章

---

### [QuickJS JavaScript引擎](https://bellard.org/quickjs/)

**原文标题**: [QuickJS Javascript Engine](https://bellard.org/quickjs/)

QuickJS是一个小型且可嵌入的JavaScript引擎，支持ES2023规范，包括模块、异步生成器、代理和BigInt等特性，适用于资源受限的环境。

- 🚀 **2025-09-13发布新版本**：包含更新日志，持续优化引擎性能与兼容性。
- 🔧 **2025-04-26版本简化代码**：移除大数扩展和qjscalc应用，推荐使用BFCalc计算器作为替代。
- 📦 **轻量嵌入式设计**：仅需少量C文件，无外部依赖，简单程序代码体积约367 KiB。
- ⚡ **快速解释器与低启动延迟**：单核桌面PC可在约2分钟内运行78000项ECMAScript测试套件，运行时实例完整生命周期低于300微秒。
- ✅ **近乎完整ES2023支持**：涵盖模块、异步生成器等特性，并通过接近100%的ECMAScript测试套件验证。
- 🔄 **引用计数垃圾回收**：结合循环移除技术，降低内存占用并确保确定性行为。
- 🌐 **在线演示与多平台支持**：可通过JSLinux运行，提供跨Linux、Mac、Windows等系统的Cosmopolitan二进制文件。
- 📚 **丰富资源与子项目**：包含文档、源码下载、TypeScript和Babel编译器集成，以及独立的libregexp、libunicode等可复用C库。
- ⚖️ **MIT许可开源**：由Fabrice Bellard和Charlie Gordon主导开发，遵循宽松的开源协议。

---

### [AddyOsmani.com - 在谷歌14年的21条经验分享](https://addyosmani.com/blog/21-lessons/)

**原文标题**: [AddyOsmani.com - 21 Lessons From 14 Years at Google](https://addyosmani.com/blog/21-lessons/)

在谷歌14年的工作经历让我明白，工程师的成功不仅取决于编程能力，更在于如何应对代码之外的人事、协作与不确定性。这些经验教训无关具体技术，而是关于在长期项目中反复出现的核心模式。

- 👥 **关注用户问题**：优秀工程师从深入理解用户需求出发，而非执着于特定技术方案。
- 🤝 **协作胜于正确**：推动团队达成共识比单纯证明自己正确更重要，避免因固执引发隐性阻力。
- 🚀 **行动导向**：先交付再完善，实际反馈比完美空想更有价值。
- 📝 **清晰优于巧妙**：代码的可读性比炫技更重要，能降低团队维护成本。
- ⚖️ **谨慎创新**：只在必要领域创新，其他场景优先选择成熟稳定的方案。
- 🗣️ **主动展示价值**：在大型组织中，让他人理解你的贡献与实际能力同等重要。
- 🗑️ **减少代码量**：最好的代码往往是不需要编写的代码，删除冗余能提升系统健壮性。
- 🔄 **兼容性即产品**：大规模系统中，所有行为都可能被依赖，需谨慎对待变更。
- 🧭 **对齐消除拖延**：团队进度缓慢常源于目标不一致，而非执行不力。
- 🎯 **专注可控因素**：将精力投入可影响的范围，避免为不可控变量焦虑。
- 🏗️ **理解底层逻辑**：抽象层终有失效之时，保持对底层原理的认知至关重要。
- ✍️ **写作促进思考**：通过输出检验认知盲区，教学相长是高效的学习方式。
- 🔗 **重视隐性工作**：文档、协调等支撑性工作需有意识规划，避免无偿消耗。
- 🕊️ **警惕表面认同**：轻易赢得的辩论可能埋下执行阻力，真正共识需要耐心磨合。
- 📊 **警惕指标异化**：任何度量标准被过度强调后都会失真，需配合质量维度综合评估。
- ❓ **坦然承认无知**：公开表达不确定性反而能营造安全的学习型团队氛围。
- 🌐 **建设人际网络**：职业关系比单一岗位更持久，用心经营会带来长期回报。
- ⚡ **优化始于删减**：提升性能最有效的方式往往是减少不必要的工作量。
- 🛠️ **流程服务效率**：好的流程应降低协作成本，而非制造文书负担。
- ⏳ **时间重于金钱**：职业生涯后期需清醒权衡时间投入与回报的关系。
- 📈 **坚持复利成长**：通过持续实践与反思积累专业资本，避免追逐捷径。

---

### [HTML 2025 现状](https://2025.stateofhtml.com/en-US/)

**原文标题**: [State of HTML 2025](https://2025.stateofhtml.com/en-US/)

2025年HTML现状调查概述：该调查由Lea Verou设计更新，得到谷歌Chrome团队等合作伙伴支持，涵盖表单、图形、性能、设备API交互、可访问性等广泛类别。今年重点分析了大量自由回答中的痛点，新增分类数据深度挖掘和原始回答检索功能，旨在帮助开发者共同面对挑战与期望。

- 📊 调查覆盖表单、图形、性能、设备API、可访问性等多领域，展现Web平台快速发展
- 🔍 今年新增痛点自由回答分析功能，支持分类数据挖掘和原始回答检索
- 👥 由Lea Verou主导设计更新，谷歌Chrome团队等提供合作伙伴支持
- 🌍 提供多语言翻译支持，包括中文、日语、韩语等十余种语言版本
- 📧 开放邮件订阅，及时通知下一次调查活动信息

---

### [@cassidoo.co 在 Bluesky 上](https://bsky.app/profile/cassidoo.co/post/3mbs2sqipuc25)

**原文标题**: [@cassidoo.co on Bluesky](https://bsky.app/profile/cassidoo.co/post/3mbs2sqipuc25)

这是一个高度交互的网络应用，需要JavaScript支持。文章介绍了Bluesky平台的相关信息，并分享了一个关于GitHub头像的小技巧。

- 🌐 Bluesky是一个基于atproto协议的高度交互式网络应用，需要JavaScript运行
- 🔗 官方资源可通过bsky.social和atproto.com获取
- 👤 用户Cassidy（cassidoo.co）在平台上分享实用技巧
- 🖼️ GitHub用户可通过在个人主页地址后添加“.png”直接获取头像图片
- ⏰ 该贴文发布于2026年1月6日

---

