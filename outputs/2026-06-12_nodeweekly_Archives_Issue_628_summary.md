### [Node 周刊第 628 期：2026 年 6 月 11 日](https://nodeweekly.com/issues/628)

**原文标题**: [Node Weekly Issue 628: June 11, 2026](https://nodeweekly.com/issues/628)

概述总结  
- 📬 **Node Weekly #628** 发布，涵盖 npm v12 安全更新、Node.js 新版本发布计划、ESM 采用率增长等关键内容。  
- 🔒 npm v12 默认禁止执行安装脚本，需通过 `npm approve-scripts` 工作流授权，以应对供应链攻击。  
- 🛡️ npm install 将默认不解析 git 或远程 URL，需使用 `--allow-git` 和 `--allow-remote` 启用。  
- 📅 Node.js 从第 27 版起改为每年一次主要版本发布，并新增“alpha”测试通道。  
- 🚨 Node.js v26.x、24.x、22.x 将于 6 月 17 日发布安全更新，最高严重级别为“高”。  
- 📊 流行 npm 包中 ESM 采用率从 33.4% 升至 38%，其中 16% 仅支持 ESM。  
- 🛠️ Node-RED 5.0 发布，带来编辑器界面重大更新，包括深色主题和可暂停调试输出。  
- 📦 Commander.js 15.0 改为仅支持 ESM，v14 维护至 2027 年 5 月。  
- 🎮 Andrew Nesbitt 创建交互式 3D 体验，让用户以 FPS 风格浏览 `node_modules` 文件夹。

---

### [npm v12 即将到来的重大变更 - GitHub 更新日志](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

**原文标题**: [Upcoming breaking changes for npm v12 - GitHub Changelog](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

npm v12 将于 2026 年 7 月发布，引入安全相关的默认变更，影响 `npm install` 行为。当前版本（11.16.0+）可预览警告并提前准备。

- 🔒 `allowScripts` 默认关闭：`npm install` 不再自动执行依赖的 `preinstall`、`install` 或 `postinstall` 脚本（包括 `node-gyp` 构建），需通过 `npm approve-scripts` 显式允许。
- 🚫 `--allow-git` 默认设为 `none`：`npm install` 不再解析 Git 依赖（直接或传递），防止通过 `.npmrc` 覆盖 Git 可执行文件的安全风险。
- 🌐 `--allow-remote` 默认设为 `none`：`npm install` 不再解析远程 URL 依赖（如 HTTPS tarball），需通过 `--allow-remote` 显式允许。
- ⚙️ 准备步骤：升级到 npm 11.16.0+，运行 `npm approve-scripts --allow-scripts-pending` 查看待处理脚本，批准信任的包并提交更新后的 `package.json`，未批准的脚本将在升级后停止运行。
- 📚 更多详情：参阅 `npm approve-scripts`、`npm deny-scripts` 和 `allow-scripts` 配置文档，或参与社区讨论。

---

### [发布 v11.16.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.16.0)

**原文标题**: [Release v11.16.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.16.0)

npm CLI v11.16.0 版本发布，包含新功能、错误修复、文档更新和依赖升级。

- 🚀 新增 `publish --access=private` 作为受限发布的别名功能
- 🔒 第一阶段引入 `allowScripts` 可选安装脚本策略
- 🐛 修复 `fullMetadata` 的拼写错误
- ⏸️ 修复交互式编辑器启动时进度旋转器的暂停问题
- 📝 记录 `npm_old_version` 和 `npm_new_version` 环境变量
- 📦 更新多个依赖，包括 undici、sigstore、lru-cache 等
- 🧹 清理开发依赖并改进标志表默认值中的换行处理
- 👥 感谢 claude、36degrees 等贡献者的参与

---

### [POSETTE：Postgres 2026 活动 - POSETTE](https://posetteconf.com/2026/)

**原文标题**: [POSETTE: An Event for Postgres 2026 - POSETTE](https://posetteconf.com/2026/)

POSETTE 是由微软 Postgres 团队组织的免费虚拟开发者活动，将于 2026 年 6 月 16 日至 18 日举行，涵盖 4 场直播，内容聚焦 PostgreSQL 开源生态系统、培训与教育。

- 🐘 活动名称 POSETTE 代表 Postgres 开源生态系统讲座、培训与教育，发音为/Pō-zet/
- 🎤 汇聚顶尖 Postgres 专家，分享最新功能、性能技巧和实际应用案例
- 💬 通过 Microsoft Open Source Discord 的#posetteconf 频道与演讲者实时互动
- 📅 4 场直播分别于 6 月 16-18 日举行，覆盖 PDT 和 CEST 时区，每场 6 小时
- 🎥 所有演讲将在活动后在线提供，方便回看
- 📧 订阅 POSETTE 新闻通讯，获取活动更新、CFP 开放和日程安排
- 🤝 在 Discord、LinkedIn、X、Bluesky 和 Mastodon 上关注#PosetteConf 参与讨论
- ❤️ 由微软 Postgres 团队主办，包括 Azure Database for PostgreSQL、Azure HorizonDB 和 Citus 开源数据库引擎的贡献者

---

### [Node.js 正在更改其发布计划和版本号](https://nodejsdesignpatterns.com/blog/nodejs-release-schedule-changes/)

**原文标题**: [Node.js is changing its release schedule and version numbers](https://nodejsdesignpatterns.com/blog/nodejs-release-schedule-changes/)

Node.js 将从 2026 年 10 月起调整发布周期和版本号，改为每年一次主要发布，版本号与年份对齐，所有版本均成为 LTS，并新增 Alpha 测试通道。

- 🔄 发布频率减半：从每年两次主要发布改为一次，4 月发布新版本，10 月升级为 LTS。
- 📅 版本号与年份对齐：例如 Node.js 27 对应 2027 年，28 对应 2028 年，直观反映版本年龄。
- ✅ 所有版本均成 LTS：取消奇偶版本区分，每个主要发布都会获得长期支持，支持周期约 30 个月。
- 🧪 新增 Alpha 通道：在版本成为 Current 前有 6 个月测试期（如 27.0.0-alpha.1），供库作者和 CI 提前测试破坏性变更。
- 📆 新生命周期：Alpha（6 个月）→ Current（6 个月）→ LTS（30 个月）→ 结束支持，总周期约 36 个月。
- 🚀 起始时间：Node.js 26 是旧模型最后版本，Node.js 27 从 2026 年 10 月启动 Alpha，2027 年 4 月正式发布。
- 🎯 实际影响：仅用 LTS 的用户变化不大；库作者需在 CI 中集成 Alpha 测试以提前发现兼容问题。
- 💡 项目动机：减少志愿者维护负担，避免低采用率的奇数版本浪费资源，并简化新用户学习曲线。

---

### [Node.js — 2026 年 6 月 17 日（星期三）安全发布](https://nodejs.org/en/blog/vulnerability/june-2026-security-releases)

**原文标题**: [Node.js — Wednesday, June 17, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/june-2026-security-releases)

Node.js 项目将于 2026 年 6 月 17 日发布安全更新，涉及 26.x、24.x 和 22.x 版本线，最高严重等级为“高”。

- 🔒 安全更新计划：2026 年 6 月 17 日（周三）或之后，Node.js 将发布 26.x、24.x 和 22.x 版本线的安全修复，最高严重等级为“高”。
- ⚠️ 影响范围：所有三个版本线（26.x、24.x、22.x）的最高严重等级均为“高”，且已终止支持（EOL）的版本也会受影响。
- 🛡️ 安全建议：请使用最新版本以确保系统安全，详见发布日程。
- 📅 发布时机：更新将在 2026 年 6 月 17 日或之后提供。
- 📧 联系与更新：当前安全政策见 https://nodejs.org/en/security/；报告漏洞请遵循 https://github.com/nodejs/node/blob/master/SECURITY.md；订阅 nodejs-sec 邮件列表（https://groups.google.com/forum/#!forum/nodejs-sec）以获取安全通知。
- 🔧 后续开发：正在为 V8 开发一种抗 HashDoS 且快速可逆的整数哈希算法。

---

### [新型 IronWorm 恶意软件攻击 npm 供应链，波及 36 个软件包](https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/)

**原文标题**: [New IronWorm malware hits 36 packages in npm supply-chain attack](https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/)

概述摘要  
- 🦠 新型 IronWorm 恶意软件攻击 npm 生态，感染 36 个软件包，属于供应链攻击。  
- 🔑 目标窃取 86 个环境变量和 20 个凭证文件，包括 OpenAI、AWS、Anthropic、npm 凭证、SSH 密钥及 Exodus 加密货币钱包。  
- 🛡️ 该恶意软件用 Rust 编写，通过 eBPF 内核 rootkit 隐藏，并通过 Tor 网络通信。  
- 🔄 自我传播机制：利用窃取的 npm 凭证（包括 Trusted Publishing 工作流）发布恶意包，感染更多开发者。  
- 🧬 与 Shai Hulud 攻击相似，使用相同提交名称，可能是其进化版本。  
- 📅 攻击始于被入侵的“asteroiddao”账户，通过伪造历史提交时间戳（长达 13 年）逃避检测。  
- 📤 秘密交付机制：将窃取数据伪装成 lint 或格式化输出文件，作为 GitHub Actions 构建工件上传，无需外部 C2。  
- 💰 攻击者硬编码自身加密货币钱包恢复短语，避免测试阶段被窃。  
- 🛑 安全公司 Ox Security 在早期阻止攻击，建议开发者升级包、轮换密钥并启用 2FA。  
- 🔍 同期发现类似 JavaScript 恶意软件“binding.gyp”，进行注册表投毒和 GitHub Actions 感染。

---

### [VU#319816 - npm 未能限制恶意 npm 包的行为](https://www.kb.cert.org/vuls/id/319816)

**原文标题**: [VU#319816 - npm fails to restrict the actions of malicious npm packages](https://www.kb.cert.org/vuls/id/319816)

npm 存在安全漏洞，允许恶意包作者创建可自我复制的蠕虫，并利用其设计特性在生态系统中扩散。

- 🐛 **核心问题**：npm 的语义版本控制、持久登录和集中注册表机制结合，使恶意包能通过依赖链自我复制和传播。
- 🔗 **蠕虫传播路径**：攻击者通过社交工程诱骗模块所有者安装恶意包，随后该包可创建新模块、设置生命周期钩子、发布到账户，并自动更新所有拥有模块的依赖。
- ⏰ **披露时间线**：2016 年 1 月 1 日发现漏洞，1 月 4 日向 npm 披露，1 月 8 日 npm 确认“按设计工作”且不计划修复。
- 🛡️ **官方回应**：npm 认为生命周期脚本是核心功能，不计划禁用；但提供注册表发布终止开关和事后识别/回滚机制。
- ⚠️ **影响范围**：攻击者可创建蠕虫，在用户安装包时自动传播，威胁整个 npm 生态系统。
- 🔧 **临时缓解措施**：用户应退出登录、使用 `npm shrinkwrap` 锁定依赖、或通过 `--ignore-scripts` 禁用脚本执行。
- 📊 **CVSS 评分**：基础分 6.0（中等），攻击复杂度中等，需用户交互，部分影响机密性、完整性和可用性。

---

### [Drizzle ORM - 下一代 TypeScript ORM](https://orm.drizzle.team/)

**原文标题**: [Drizzle ORM - next gen TypeScript ORM.](https://orm.drizzle.team/)

Drizzle ORM 是一个快速、支持 TypeScript 和 JavaScript 的 ORM，提供全面的数据库连接、模式管理、查询和迁移功能，并拥有活跃的社区和持续的版本更新。

- 🌧️ **核心定位**：Drizzle 是一个“无头”的 TypeScript ORM，强调快速交付和类型安全，支持 JavaScript 和 TypeScript。
- 🚀 **性能卓越**：基准测试显示，Drizzle 在处理查询和连接时延迟极低，CPU 负载小，性能优于 Prisma 等竞品。
- 🌐 **广泛兼容**：支持 PostgreSQL、MySQL、SQLite、MSSQL、CockroachDB、SingleStore 等多种数据库，以及 Cloudflare Workers、Vercel Functions 等主流 serverless 运行时。
- 🛠️ **功能全面**：提供模式定义、数据查询（Select/Insert/Update/Delete）、迁移（generate/migrate/push/pull）、数据填充（seed）和 Studio 可视化数据管理。
- 📦 **持续迭代**：从 v0.32 到 v1.0 Beta 版本，不断推出新功能（如行级安全 RLS、Gel 方言、缓存层）、修复大量 Bug，并重写了迁移引擎。
- 👨‍💻 **社区驱动**：拥有活跃的贡献者团队和 Discord/Twitter 社区，定期发布版本更新和教程，并接受赞助。
- 🎮 **趣味元素**：官网包含贪吃蛇游戏等趣味功能，团队氛围轻松，强调“快速交付”和“乐趣”。

---

### [Drizzle ORM 在 X 上表示：“我们无法发布新版本，因为已经达到了 npm 100MB 的发布限制，正在尝试与 npm 支持团队解决这个问题（至今已近两周）。

不过，一个大版本即将到来，我们肯定会在这次发布后立即触及新的限制。” / X](https://x.com/DrizzleORM/status/2062629339556921581)

**原文标题**: [Drizzle ORM on X: "we can't ship new releases because we've hit 100mb npm releases limit, trying to resolve this with npm support(almost 2 weeks so far)

big release is coming though, we'll definitely hit new limits right after this one too" / X](https://x.com/DrizzleORM/status/2062629339556921581)

Drizzle ORM 团队因 npm 发布包大小超过 100MB 限制，导致无法发布新版本，已与 npm 支持团队沟通近两周仍未解决。尽管面临限制，团队表示即将推出重大更新，并预计发布后会再次触及新限制。

- 📦 发布受阻：因 npm 包大小超过 100MB 限制，无法发布新版本
- ⏳ 沟通拖延：与 npm 支持团队沟通近两周，仍未解决限制问题
- 🚀 重大更新：即将推出重要版本，但预计会再次突破新限制
- 📈 增长挑战：随着项目发展，包大小可能持续超出 npm 限制

---

### [获取失败](https://nodeweekly.com/link/186414/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/186414/web)

无法总结：获取内容失败，状态码 403。

---

### [npm 工具错误地将单字符包标记为...](https://socket.dev/blog/npm-tooling-single-character-bug)

**原文标题**: [npm Tooling Bug Incorrectly Marks One-Character Packages as ...](https://socket.dev/blog/npm-tooling-single-character-bug)

概述：攻击者利用恶意 PyPI 包，通过原生扩展和.pth 加载器在生物信息学和 MCP 开发环境中执行 JavaScript 窃密程序，涉及 Mini Shai-Hulud、Miasma 和 Hades 蠕虫等变种。

- 🐛 Mini Shai-Hulud 蠕虫通过恶意 PyPI 包感染生物信息学开发环境
- ☁️ Miasma 变种利用原生扩展隐藏恶意代码
- 👾 Hades 蠕虫针对 MCP 开发者，使用.pth 加载器执行 JavaScript 窃密程序
- 🔒 攻击者通过伪装成合法库的 PyPI 包传播恶意负载
- 📉 这些恶意包专门窃取开发环境中的敏感数据

---

### [GitHub - wooorm/npm-esm-vs-cjs: 公共 npm 注册表中 ESM 与 CJS 占比数据 · GitHub](https://github.com/wooorm/npm-esm-vs-cjs#data)

**原文标题**: [GitHub - wooorm/npm-esm-vs-cjs: Data on the share of ESM vs CJS on the public npm registry · GitHub](https://github.com/wooorm/npm-esm-vs-cjs#data)

该仓库追踪了 npm 公共注册表中 ESM 与 CJS 模块格式的采用趋势数据。

- 📊 数据涵盖高影响力 npm 包，按 ESM、双格式、伪 ESM 和 CJS 分类统计
- 📈 从 2021 年 8 月到 2026 年 6 月，ESM 和双格式包的数量显著增长
- ⚠️ 2025 年 12 月的数据源切换导致收录包数量大幅增加
- 🔧 包含爬取和分析脚本，需 NPM_TOKEN 运行
- 🎯 数据可用于了解 ESM 迁移进展，但存在统计偏差
- 📁 提供 SVG 图表和 CSV 原始数据文件
- 🤝 欢迎贡献，需先参与 npm-high-impact 项目

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

Tiger Data 提供专为时序工作负载优化的 Postgres 云服务，具备超大规模处理能力与高性价比。

- 📊 单服务可处理 3 万亿指标/天、3PB 数据及 1 万亿数据点，展现真实世界规模
- 💰 新用户获$1000 额度（30 天有效），无需信用卡，支持免费试用
- 🔄 读写分离架构（最多 10 节点），搭配分层 SSD/S3 实现无限低成本存储
- ⚡ 计算与存储解耦，独立扩缩容，避免为闲置容量付费
- 🛡️ 多 AZ 集群自动故障切换、时间点恢复及跨区域备份，保障高可用
- 🔒 符合 SOC 2、HIPAA、GDPR 标准，支持加密、SSO、RBAC 及审计日志
- 📈 深度可观测性：查询下钻与仪表盘，集成 CloudWatch、Datadog、Prometheus
- ⏱️ 数分钟内完成数据库部署，支持 SQL、CLI、Terraform、Cursor 及 Claude Code 管理
- 🔌 与主流云提供商及 Postgres 生态系统无缝集成
- 🏢 企业级服务：合同化 SLA、区域数据隔离、24/7 专家支持及合规认证

---

### [揭秘 Playwright Fixtures API 背后的魔法](https://ivakin.dev/blog/how-playwright-fixtures-work)

**原文标题**: [Uncovering the Magic Behind Playwright's Fixtures API](https://ivakin.dev/blog/how-playwright-fixtures-work)

### 概述总结
Playwright 的 Fixtures API 通过解析函数参数实现惰性初始化，利用`Function.prototype.toString()`提取参数名，从而在测试运行前确定所需 fixtures 并仅初始化必要资源。

- 🧩 **惰性初始化机制**：Playwright 通过分析测试函数参数，仅初始化被实际使用的 fixtures（如`page`），避免不必要的资源开销。
- 🔍 **参数提取技术**：使用`Function.prototype.toString()`将函数转为字符串，配合正则表达式解析参数名，强制要求对象解构模式以简化提取。
- ⚙️ **Proxy 与异步处理**：早期尝试用 Proxy 实现惰性加载，但异步 fixtures 需`await`调用，影响 API 简洁性；最终方案通过预解析参数实现同步访问。
- 🛠️ **边界情况处理**：支持多种函数声明形式（箭头函数、async/await、生成器等），兼容 Terser/esbuild 等压缩工具对参数名的重命名。
- ⚠️ **局限性**：函数组合场景（如包装器）会导致解析失败，但 Playwright 测试场景中不常见；API 设计存在“魔法感”，可能违反最小惊讶原则。
- 🎯 **设计权衡**：通过牺牲部分透明性换取更直接的测试编写体验，该方案在测试框架中表现优秀，但其他场景适用性有限。

---

### [我希望 Deno 能继续做它最擅长的事](https://hackers.pub/@hongminhee/2026/i-wish-deno-would-keep-doing-what-it-does-best)

**原文标题**: [I wish Deno would keep doing what it does best](https://hackers.pub/@hongminhee/2026/i-wish-deno-would-keep-doing-what-it-does-best)

### 概述总结
作者回顾了自己从 Python 和 Haskell 转向 TypeScript 的经历，最初因配置复杂而却步，后被 Deno 的零配置、Web 标准集成和内置工具链所吸引。然而，作者观察到 Deno 近年逐渐偏离初心，转向兼容 Node.js，导致其独特性减弱。尽管作者仍优先使用 Deno，但对其发展方向感到担忧，认为 Deno 应在垂直整合和工具质量上持续领先，而非追赶竞争对手。

- 🚫 **配置壁垒**：JavaScript 生态的 tsconfig.json、ESLint 等配置文件让作者望而却步，Deno 的零配置体验（`deno run main.ts`）打破这一障碍。
- ✨ **核心吸引力**：Deno 的 Web 标准一致性（如`fetch()`）、内置工具链（`deno fmt`、`deno lint`等）和 URL 导入机制，让开发更简洁高效。
- 🔄 **方向偏移**：Deno 近年增加 npm 兼容性、`node_modules`支持和`deno add`默认 npm 包，逐渐向 Node.js 靠拢，削弱了其独特性。
- ⚖️ **竞争趋同**：Node.js 已引入 TypeScript 支持、权限模型和 Web API，而 Deno 的追赶策略可能让开发者无需专门适配 Deno。
- 🛠️ **防御性反思**：Deno 本可凭借内置工具（如`deno fmt`）成为“特洛伊木马”，但 Fresh 框架选择 Vite 而非深化垂直整合，错失领先机会。
- ⏳ **时间压力**：Deno Land Inc.作为 VC 支持的公司，面临投资回报压力，可能迫使其选择短期可见的兼容性策略，而非长期耐心推进。
- 💔 **忠实用户的退却**：作者虽仍优先使用 Deno，但已转向`node:test`和`node:sqlite`以跨运行时兼容，对 JSR 的停滞感到失望。
- 🤔 **未来隐忧**：作者担心 Deno 正偏离最初吸引自己的方向，若连核心用户都在退缩，其吸引力将更难维持。

---

### [创建 VS Code 代理钩子以响应文件更改 - 编程之人](https://humanwhocodes.com/blog/2026/05/vscode-agent-hooks/)

**原文标题**: [Creating a VS Code agent hook to respond to file changes - Human Who Codes](https://humanwhocodes.com/blog/2026/05/vscode-agent-hooks/)

### 概述总结
本文介绍了如何在 VS Code 中创建代理钩子（agent hook），以检测特定文件编辑并自动触发后续操作，提升开发工作流的可靠性。

- 🛠️ **代理钩子工作原理**：代理钩子是在代理会话特定事件点执行的 Shell 命令，支持 SessionStart、UserPromptSubmit、PreToolUse、PostToolUse 等事件，通过 JSON 配置文件（位于`.github/hooks`目录）定义。

- 📥 **钩子输入与输出**：钩子通过 stdin 接收 JSON 数据（含时间戳、工作目录、会话 ID 等），通过退出码（0 继续、2 停止）和 stdout（含 continue、systemMessage 等字段）与 VS Code 通信。

- 🔍 **检测特定文件编辑**：通过读取 stdin 获取钩子负载，过滤出编辑工具（如 editFiles、create_file 等），检查工具输入中是否包含目标文件名（如 wrangler.jsonc），并提取父目录以执行后续操作。

- ⚙️ **配置与集成**：在`.github/hooks`目录创建 JSON 文件，指定 PostToolUse 事件和命令（如`node ./scripts/detect-file-change.mjs`），即可实现文件编辑后自动触发脚本。

- 🎯 **实际应用案例**：作者通过代理钩子自动在编辑 wrangler.jsonc 文件后运行`wrangler types`命令生成 TypeScript 类型定义，解决了代理无法可靠执行后续任务的问题。

- 💡 **优势与价值**：代理钩子提供确定性行为，无需依赖模型记忆，确保工作流自动化和一致性，减少手动干预和错误。

---

### [版本 5.0 发布：Node-RED](https://nodered.org/blog/2026/06/09/version-5-0-released)

**原文标题**: [Version 5.0 released : Node-RED](https://nodered.org/blog/2026/06/09/version-5-0-released)

Node-RED 5.0 正式发布，这是编辑器体验史上最大的一次变革，重点改进了用户界面、节点外观、功能增强和项目基础设施，并引入了深色主题、侧边栏重新设计等多项新特性。

- 🎨 **编辑器现代化**：重新设计侧边栏布局，支持垂直拆分显示两个面板，并可通过拖拽自由排列面板位置。
- 🌙 **内置深色主题**：根据浏览器/系统偏好自动切换，也可手动设置，并支持主题插件提供多主题变体。
- ♿ **无障碍改进**：增加 ARIA 属性，优化下拉菜单触控和滚动，提升对比度和可访问性，选中的节点显示蓝色光晕。
- 🔍 **节点文档徽章**：带有额外文档的节点会显示徽章，点击即可弹出文档内容。
- 📝 **Markdown 支持 GitHub 风格警报**：支持 `[!IMPORTANT]` 等标记，渲染为高亮提示框。
- ⏸️ **调试输出暂停**：调试侧边栏新增暂停按钮，暂停后停止滚动并丢弃新消息。
- 🔗 **Function 节点调用 Link 节点**：新增 `node.linkcall` API，支持在 Function 节点中调用 Link 节点并等待响应。
- 📋 **节点选择列表排序**：Link、Complete 等节点的选择列表按标签字母顺序排序，便于查找。
- ⏱️ **Delay 节点突发模式**：新增突发模式，允许消息以到达速率通过，直到达到限制后阻塞。
- 🔒 **TLS 选项增强**：支持 PFX/P12 文件、环境变量加载证书，HTTP Request 节点可设置 SNI 服务器名。
- 🛡️ **认证加固**：OAuth 登录采用令牌交换模式，移除默认 CORS 规则。
- ⚙️ **底层更新**：最低要求 Node.js 22.9.0，推荐 Node.js 24；npm 成为显式依赖；开发者工具迁移至 npm 脚本和 ESLint。

---

### [盆景——规则、过滤器和模板的安全表达式](https://danfry1.github.io/bonsai-js/)

**原文标题**: [Bonsai — Safe Expressions for Rules, Filters, and Templates](https://danfry1.github.io/bonsai-js/)

- 🚀 零运行时依赖：不向依赖树中引入任何额外包
- 🖥️ 支持运行环境：Node 22+、Bun 以及浏览器

---

### [游乐场 — 盆景 | 盆景](https://danfry1.github.io/bonsai-js/playground)

**原文标题**: [Playground — Bonsai | Bonsai](https://danfry1.github.io/bonsai-js/playground)

概述总结  
- 🔍 提供搜索功能，方便用户快速查找内容  
- 📚 包含主要导航菜单，涵盖指南、游乐场、API 等核心板块  
- 🛠️ 设有“工作原理”页面，解释系统机制  
- 📦 支持 npm 包管理，便于集成  
- 🎨 提供外观设置选项，可自定义界面主题

---

### [DepsGuard - 供应链防御](https://depsguard.com/)

**原文标题**: [DepsGuard - Supply Chain Defense](https://depsguard.com/)

该工具 DepsGuard 用于防御软件供应链攻击，通过配置包管理器延迟新版本安装并禁用危险脚本，降低被恶意包影响的风险。

- 🛡️ **核心防御机制**：通过设置“最低发布年龄”（如 7 天）延迟新版本安装，并禁用危险安装脚本（如`ignore-scripts=true`），为社区发现恶意包争取时间。
- ⚙️ **支持的包管理器**：覆盖 npm、pnpm、Yarn、Bun、aube、uv、pip、Poetry，以及 Renovate 和 Dependabot 的配置检查与修复。
- 🖥️ **交互式使用**：提供 TUI 界面，支持扫描、选择修复、预览差异（`d`键）、应用更改（`Enter`键）和回滚（`depsguard restore`）。
- 📦 **安装方式**：支持 macOS（Homebrew）、Linux（APT）、Windows（WinGet/Scoop）及 Cargo 安装，零依赖。
- 🔄 **紧急绕过指南**：针对需要立即安装的安全修复，提供各包管理器的临时绕过方法（如`npm install --min-release-age=0`），并建议事后移除例外。
- ❓ **FAQ 关键点**：强调该工具不防所有攻击（如长期潜伏的恶意包），但能有效应对短时攻击（如 axios 3 小时事件）；与 SCA 工具互补；免费且 MIT 开源。
- 🔗 **补充资源**：推荐配合`cooldowns.dev`使用，并建议额外措施（如锁定 GitHub Actions SHA、CI 中使用冻结锁文件）。

---

### [发布 v15.0.0 · tj/commander.js · GitHub](https://github.com/tj/commander.js/releases/tag/v15.0.0)

**原文标题**: [Release v15.0.0 · tj/commander.js · GitHub](https://github.com/tj/commander.js/releases/tag/v15.0.0)

Commander.js 发布了 v15.0.0 版本，这是一个重大更新，主要将库从 CommonJS 迁移到 ESM 模块系统，并引入了多项破坏性变更和功能改进。

- 🎉 发布 Commander.js v15.0.0 版本，这是 ESM 专属版本，要求 Node.js v22.12.0 或更高版本
- 🚨 破坏性变更：只有单独的 `--no-*` 选项会将默认值设为 `true`，正反选项同时定义时不再隐式设置默认值
- 📦 从 CommonJS 迁移到 ESM 模块系统，移除了 `commander/esm.mjs` 的废弃导出
- 🛠️ 新增功能：在错误信息中显示多余的命令参数
- 🔄 开发工具从 Jest 切换到 `node:test` 测试运行器
- ⚠️ 迁移提示：ESM 可从 CommonJS 导入，但某些工具（如测试框架或打包器）可能不兼容，建议暂时停留在 v14 版本
- 🛡️ v14 版本将获得安全更新至 2027 年 5 月，为期 12 个月
- 🐛 修复了 MINGW64 的兼容性问题，更新了示例中的字符

---

### [NodeAV](https://seydx.github.io/node-av/)

**原文标题**: [NodeAV](https://seydx.github.io/node-av/)

NodeAV 是一个原生 Node.js 的 FFmpeg 绑定库，提供完整的 TypeScript 支持，包括类型安全的编解码器、格式、滤镜和比特流滤镜选项，并支持硬件加速和自动资源管理。

- 🎯 **核心特性**：提供低层和高层 API，支持硬件加速、流处理、设备捕获和 FFmpeg 二进制访问
- 📦 **安装与使用**：通过 npm 安装，支持多种导入方式（api/lib/constants/layouts）以实现最佳 tree shaking
- 🚀 **性能表现**：与 FFmpeg CLI 性能相当，在 H.264/H.265 转码中差异极小，内存使用更优
- 🛠️ **API 层级**：低层 API 提供直接 C 绑定，高层 API 简化常见任务，Pipeline API 支持链式处理
- 💻 **平台支持**：提供 Windows、Linux、macOS 的预编译二进制，支持 Electron 应用
- 📹 **高级功能**：支持 Whisper 语音识别、复杂滤镜链、浏览器流式传输、RTSP 双向通信和图像缩放
- 🔄 **资源管理**：使用 Disposable 模式自动清理资源，支持同步和异步操作
- 🎨 **类型安全**：所有 FFmpeg 选项都经过类型化，支持自动补全和编译时验证

---

### [框架 | Neutralinojs](https://neutralino.js.org/docs/release-notes/framework/#v680)

**原文标题**: [Framework | Neutralinojs](https://neutralino.js.org/docs/release-notes/framework/#v680)

Neutralinojs 框架的版本发布说明，涵盖了从 v4.0.0 到 v6.8.0 的多个版本更新，包括新功能、API 改进、配置选项和错误修复。

- 🪟 **v6.8.0**: 新增窗口策略 (`window.newWindowPolicy`)，支持系统、浏览器或自定义方式处理 `target="_blank"` 链接；实现原生文件拖放支持 (`window.emitDropEvents`)；新增 `computer` 和 `filesystem` API（如 `getHostname`、`chmod`、`chown`）；改进静态服务器支持 HTTP 206 部分内容；扩展支持 WebSocket 二进制模式；修复内存和托盘问题。
- 🖱️ **v6.7.0**: 新增输入设备模拟 API (`computer.setMousePosition`、`setMouseGrabbing`、`sendKey`)；添加 `os.setTray` 的 `useTemplateIcon` 选项；修复 macOS 窗口排序和焦点问题。
- 📐 **v6.5.0**: 新增窗口事件（最小化、恢复等）和 `window.setBorderless` 方法；配置支持自定义 Chrome 浏览器路径 (`browserBinary`) 和逻辑像素模式 (`useLogicalPixels`)；修复 Linux 文件对话框和 Windows 托盘图标问题。
- 🗂️ **v6.4.0**: 实现 `storage.clear()` 和 `storage.removeData()`；修复 Windows 可拖动区域和窗口状态保存问题。
- 📦 **v6.3.0**: 引入单可执行文件模式（通过 `--embed-resources`）；新增 `window.skipTaskbar` 和 `window.openInspectorOnStartup` 配置；修复 WebView2 在 Unicode 路径下的崩溃问题。
- 🖨️ **v6.2.0**: 添加 `window.print()` 和 `window.beginDrag()`；新增 `filesystem` 路径处理函数；实现 `window.webviewArgs` 配置。
- 🍔 **v6.1.0**: 实现原生窗口主菜单 (`window.setMainMenu`)；新增全局变量 `NL_LOCALE` 和 `NL_COMPDATA`。
- 📋 **v6.0.0**: 实现剪贴板 HTML 读写；`os.execCommand` 和 `os.spawnProcess` 支持环境变量；`filesystem` 新增权限和文件监控时间戳；改进 `NL_TOKEN` 生成安全性。
- 🌐 **v5.6.0**: 新增 `server` API（挂载/卸载目录）；实现 `window.snapshot` 截图功能；修复 Windows 窗口标题和资源提取问题。
- 💉 **v5.5.0**: 支持注入全局变量和客户端库到外部 Web 服务；实现预加载脚本 (`window.injectScript`)；新增 `dataLocation` 和 `storageLocation` 配置。
- 📁 **v5.4.0**: 实现 `resources` API（读取资源包文件）；添加窗口最小化/恢复功能；修复剪贴板和进程问题。
- 🔲 **v5.3.0**: 支持 Windows 窗口透明度；新增 `filesystem` 路径处理函数；修复 Unicode 和输出显示问题。
- ⚙️ **v5.2.0**: 支持无配置文件启动；实现 SPA 路由 (`singlePageServe`)；改进 `window.show()` 行为。
- 🎨 **v5.1.0**: 支持窗口透明度（除 Windows）；实现剪贴板图像读写。
- 🔒 **v5.0.0**: 实现标准流读写；`filesystem` 新增复制/移动/删除；增强 WebSocket 安全；移除旧版函数。
- 🌍 **v4.15.0**: 支持自定义用户代理字符串和配置文件。
- 🛠️ **v4.14.0**: 新增 `filesystem.getWatchers`；改进二进制文件读取和进程工作目录支持。
- 💾 **v4.13.0**: 实现持久化窗口状态。
- 🎯 **v4.12.0**: 添加 `window.center` 和窗口位置配置；静态链接 WebView2。
- 👀 **v4.11.0**: 实现文件监控 API。
- 🍏 **v4.10.0**: 支持 macOS arm64 二进制；添加 JSON Schema；支持 ESM/NPM 模块。
- 🧩 **v4.9.0**: 实现自定义方法 API；添加文件流 API。
- 🖥️ **v4.8.0**: 新增 `os.getEnvs`、`storage.getKeys`、`computer.getMousePosition`；改进文件读取选项。
- 📊 **v4.7.0**: 新增系统信息 API（CPU、OS、显示器等）；对话框支持默认路径。
- ⚡ **v4.6.0**: 实现进程生成 API；支持 Linux ARM 二进制；改进文件统计和资源 URL。
- 🔔 **v4.5.0**: 添加窗口焦点事件；使用 BuildZri 自动化；动态加载库。
- 📄 **v4.4.0**: 新增 `window.getPosition` 和文件追加功能。
- 🔑 **v4.3.0**: 添加 `tokenSecurity` 配置；实现 `window.setAlwaysOnTop` 和 `window.getSize`。
- 📋 **v4.2.0**: 实现剪贴板 API；支持 Chrome 模式 CLI 参数。
- 🌐 **v4.1.0**: 添加 `window.getTitle`；支持 Chrome 模式。
- 🚀 **v4.0.0**: 重写 `os.execCommand`；实现扩展 API；支持社区驱动进程；添加广播事件和更新器 API。

---

### [GitHub - Automattic/juice: Juice 将 CSS 样式表内联到您的 HTML 源代码中。](https://github.com/Automattic/juice)

**原文标题**: [GitHub - Automattic/juice: Juice inlines CSS stylesheets into your HTML source. · GitHub](https://github.com/Automattic/juice)

Juice 是一个将 CSS 样式内联到 HTML 元素 style 属性中的工具，特别适用于 HTML 邮件和第三方网站嵌入场景。

- 🎯 **核心功能**：将 CSS 规则内联到 HTML 的 `style` 属性中，支持 HTML 字符串、文件或 cheerio 文档处理。
- 🚀 **现代 CSS 支持**：自动处理嵌套规则、`@container`/`@layer` 规则，并正确计算 `:is()`/`:where()` 等选择器的特异性。
- ⚙️ **丰富选项**：提供 20+ 配置项，如控制样式标签保留、伪元素内联、`!important` 保留、CSS 变量解析等。
- 📋 **多种方法**：支持 `juice()`、`juiceResources()`、`juiceFile()`、`juiceDocument()` 等，满足不同场景需求。
- 🎨 **特殊标记**：通过 `data-embed`、`data-juice-duplicates`、`data-juice-important` 等属性，可精细控制内联行为。
- 💬 **CSS 注释控制**：使用 `/* juice ignore */` 等注释，可跳过整个文件、单个规则或声明的内联。
- 🖥️ **CLI 工具**：提供命令行接口，支持通过 `--css` 和 `--options-file` 加载外部配置。
- 🌐 **浏览器兼容**：通过 `juice/client` 入口支持浏览器环境，但仅提供部分方法（如 `inlineContent`）。
- 🛠️ **全局设置**：可配置 `codeBlocks`（如模板语法）、`ignoredPseudos`、`tableElements` 等，增强灵活性。
- 📜 **许可与依赖**：MIT 许可，依赖 cheerio、mensch 和 Slick 等库。

---

### [juice/PROJECTS.md 位于 master 分支 · Automattic/juice · GitHub](https://github.com/Automattic/juice/blob/master/PROJECTS.md)

**原文标题**: [juice/PROJECTS.md at master · Automattic/juice · GitHub](https://github.com/Automattic/juice/blob/master/PROJECTS.md)

概述摘要  
- 🚀 **juice** 是一个用于将 CSS 内联到 HTML 邮件中的开源工具，拥有 3.3k 星标和 233 个分支。  
- 📧 **node-email-templates** 使用 ejs 模板和 juice 内联 CSS 渲染美观的邮件。  
- 🛠️ **swig-email-templates** 支持模板继承，并能从模板生成虚拟上下文。  
- 🌐 **nodejs-api-starter** 是一个构建 Node.js 和 GraphQL Web API 的项目模板，包含邮件功能。  
- 🔔 **notifme-template** 用于处理邮件、短信、推送等通知模板，可配合 notifme-sdk 使用。  
- 🎨 **mosaico** 是首个开源邮件模板编辑器，可快速构建响应式邮件模板。  
- ✉️ **mjml** 是一种标记语言，用于轻松编写兼容所有邮件客户端的响应式 HTML 邮件。  
- 🖌️ **maizzle** 使用 Tailwind CSS 快速构建 HTML 邮件。  
- 🔧 **grunt-email-workflow** 是一个 Grunt 工作流，用于设计和测试响应式 HTML 邮件模板（支持 SCSS）。

---

### [发布 v13.0.0 · cucumber/cucumber-js · GitHub](https://github.com/cucumber/cucumber-js/releases/tag/v13.0.0)

**原文标题**: [Release v13.0.0 · cucumber/cucumber-js · GitHub](https://github.com/cucumber/cucumber-js/releases/tag/v13.0.0)

这是一个关于 cucumber-js v13.0.0 版本的发布说明。

- 📦 **主要版本发布**：cucumber-js v13.0.0 已发布，包含多项重大变更和破坏性更新。
- 🔧 **新增支持**：新增对 Node.js 26.x 的支持。
- 🔄 **并行运行时重构**：使用工作线程重新实现了并行运行时，这是一个破坏性变更。
- ⏳ **钩子执行变更**：所有 `BeforeAll` 和 `AfterAll` 钩子现在始终执行，属于破坏性变更。
- 🎨 **格式化输出改进**：重新设计了摘要、进度、进度条和美观格式化器的输出。
- 📉 **依赖减少**：减少了传递依赖。
- 🚫 **弃用旧类**：弃用了旧的 `SummaryFormatter` 和 `ProgressFormatter` 类，以及 `printAttachments` 选项。
- 🐛 **错误修复**：修复了状态颜色、错误链显示和未定义/模糊处理等问题。
- ❌ **移除旧支持**：移除了对 Node.js 20.x 和 25.x 的支持，以及已弃用的 Cli 导出和格式处理。

---

### [GitHub - kristiandupont/kanel: 从 Postgres 生成 TypeScript 类型](https://github.com/kristiandupont/kanel)

**原文标题**: [GitHub - kristiandupont/kanel: Generate Typescript types from Postgres · GitHub](https://github.com/kristiandupont/kanel)

Kanel 是一个从 Postgres 数据库生成 TypeScript 类型的工具，适合不喜欢 ORM 但需要类型检查和智能提示的开发者。

- 🗄️ 从 Postgres 数据库直接生成 TypeScript 类型，无需 ORM
- 📖 提供完整文档和示例，帮助快速上手
- ⚙️ 支持配置文件 `kanel.config.js` 和程序化调用
- 🚀 使用简单：安装后运行 `npx kanel` 即可生成类型
- 🎯 适用于需要数据库类型安全但偏好原生 SQL 的开发者
- 📂 示例基于 Postgres 示例数据库，便于参考
- 🤝 开源项目，MIT 许可证，支持社区贡献
- ⭐ 在 GitHub 上获得 1.2k 星标，拥有 79 个 fork
- 🏷️ 已发布 63 个版本，最新为 v3.5.1

---

### [GitHub - af/envalid: 适用于 Node、Bun 及其他兼容 JS 运行时的环境变量验证工具](https://github.com/af/envalid)

**原文标题**: [GitHub - af/envalid: Environment variable validation for Node, Bun, and other compatible JS runtimes · GitHub](https://github.com/af/envalid)

Envalid 是一个用于验证和访问 Node.js 程序中环境变量的小型库，确保程序仅在环境依赖满足时运行，并提供不可变的 API。

- 🔒 **类型安全**：完全用 TypeScript 编写，支持强大的类型推断，确保环境变量类型正确。
- ⚡ **轻量无依赖**：没有外部依赖，体积小巧，易于集成。
- 🛠️ **模块化设计**：支持自定义验证器、中间件和错误报告，灵活满足不同需求。
- 📋 **核心函数 `cleanEnv()`**：接受环境对象、验证器对象和可选选项（如自定义报告器），返回经过验证和清理的不可变环境对象。
- ✅ **内置验证器**：提供 `str()`、`bool()`、`num()`、`email()`、`host()`、`port()`、`url()` 和 `json()` 等常用验证器，支持 `choices`、`default`、`desc` 等配置选项。
- 🧩 **自定义验证器**：通过 `makeValidator()`、`makeExactValidator()` 和 `makeStructuredValidator()` 轻松创建自定义验证逻辑。
- 🚨 **错误处理**：默认在环境变量缺失或无效时记录错误并退出，可通过 `reporter` 选项自定义行为，并支持 `EnvError` 和 `EnvMissingError` 异常类型。
- 🔧 **高级中间件**：提供 `customCleanEnv()` 函数，允许完全替换验证后的处理逻辑，与内置中间件混合使用。
- 📚 **相关生态**：与 `dotenv`、`react-native-config`、`fastify-envalid` 等工具兼容，扩展使用场景。

---

### [Dyno 狙击手](https://judoscale.com/docs/sniper?utm_source=node-weekly&utm_medium=referral&utm_campaign=dyno-sniper&utm_content=solved-for-good)

**原文标题**: [Dyno Sniper](https://judoscale.com/docs/sniper?utm_source=node-weekly&utm_medium=referral&utm_campaign=dyno-sniper&utm_content=solved-for-good)

概述摘要  
Dyno Sniper 是 Judoscale 针对共享硬件上“吵闹邻居”问题的解决方案，通过重启异常 dyno 来补充自动扩缩容，而非替代它。目前仅适用于 Heroku 平台的 web dyno，需同时启用队列时间和利用率指标。

- 👀 **适用范围**：当前仅支持 Heroku 应用，且仅适用于使用队列时间或响应时间进行自动扩缩容的 web dyno（非 worker）。若仅使用利用率指标，则无法启用该功能。
- 🔍 **工作原理**：持续监控每个 dyno 的队列时间或响应时间，当某个 dyno 长时间显著高于集群中位数时，通过 Heroku API 重启它，通常会将新 dyno 分配到不同物理主机，避开吵闹邻居。
- ⚙️ **设计特点**：与集群中位数比较而非绝对数值；信号需持续异常才触发（过滤短期峰值）；每 10 秒检查一次（与自动扩缩容同步）；无需单独配置，自动继承扩缩容阈值灵敏度。
- 🚫 **不触发场景**：自动扩缩容未启用、应用处于维护模式、dyno 数量少于 3 个、刚完成扩缩容、多个 dyno 同时异常、dyno 刚被重启过。
- 🛠️ **使用方法**：在 web 进程的高级设置中启用，重启事件会以标记形式显示在扩缩容图表上。可随时取消勾选停止该功能。
- 📧 **反馈渠道**：如有改进建议或成功案例，可发送邮件至 [email protected]。

---

### [邮件日志公开测试版](https://clerk.com/changelog/2026-06-01-email-logs-public-beta?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=email-logs&utm_content=06-11-26&dub_id=dzZbpcWTHAWKQjc0)

**原文标题**: [Email Logs public beta](https://clerk.com/changelog/2026-06-01-email-logs-public-beta?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=email-logs&utm_content=06-11-26&dub_id=dzZbpcWTHAWKQjc0)

概述摘要
- 📧 邮件日志功能现已公开测试，可在 Clerk 仪表板中查看事务性邮件发送事件。
- 🔍 支持按收件人、IP 地址、消息 ID、时间范围和事件类型筛选日志，便于调试投递问题。
- 📋 点击日志条目可查看详细投递状态、响应原因、元数据及原始提供商负载。
- 🛠️ 通过 Clerk 仪表板的“日志”部分启用该功能，自定义角色需授予“邮件日志”读取权限。

---

### [node_modules/](https://nesbitt.io/heap)

**原文标题**: [node_modules/](https://nesbitt.io/heap)

概述总结：该内容展示了 Node.js 项目依赖安装后的状态，包括模块目录、操作提示、性能指标和安全警告。

- 📦 `node_modules` 目录已存在，包含所有已安装的依赖包
- 🎮 提供了 WASD 移动、鼠标视角、Shift 冲刺和空格飞行的交互控制说明
- 📊 显示当前有 0 个包加载和 0 个磁盘占用，可能表示未加载实际项目包
- 🌐 操作界面包含方向控制（▲/◀/▶/▼）和飞行模式切换（fly）
- 🔍 提示“点击进入堆内存”，可能指向调试或性能分析功能
- ⚠️ npm 安装完成，但存在 47 个安全漏洞（3 个低危、18 个中危、26 个高危）

---

### [获取失败](https://nodeweekly.com/link/186436/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/186436/web)

无法总结：获取内容失败，状态码 402。

---

