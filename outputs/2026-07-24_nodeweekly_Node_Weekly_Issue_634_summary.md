### [不，我们无法强化 Node.js 以防止原型污染](https://adventures.nodeland.dev/archive/no-we-cant-harden-nodejs-against-prototype/)

**原文标题**: [No, We Can't Harden Node.js Against Prototype Pollution](https://adventures.nodeland.dev/archive/no-we-cant-harden-nodejs-against-prototype/)

### 概述总结
文章指出，Node.js 无法通过加固核心来防御原型污染，因为一旦攻击者能写入 `Object.prototype`，所有依赖原型链的代码都可能成为漏洞入口。真正的解决方案是在应用边界处阻止污染发生。

- 🛡️ 原型污染不是 Node.js 或库的问题，而是应用本身需要防范的代码漏洞
- 🔍 每次安全报告都假设攻击者已能写入 `Object.prototype`，这实际上意味着攻击者已经获胜
- 🎯 加固单个函数（如 `execSync`）只是打地鼠，因为整个生态系统的每个选项对象都可能成为攻击目标
- ⚙️ JavaScript 通过语法（解构、展开、`for...of` 等）访问原型链，使得全面加固几乎不可能
- 🧱 Primordials 机制只能保证 Node.js 自身不崩溃，无法阻止原型污染带来的安全风险
- 🚫 Node.js 安全计划不将需要原型污染前提的漏洞视为核心漏洞，这是对威胁模型的诚实界定
- 🔒 修复的关键在于边界：在不可信数据转化为对象时（如 `JSON.parse`）拦截 `__proto__` 和 `constructor` 操作
- 🛠️ 使用 `secure-json-parse`、冻结对象、优先使用 `Map` 和空原型对象等防御措施
- ⚠️ 如果攻击者能写入原型，游戏已经结束；你的任务是确保他们永远无法获得这种写入能力

---

### [GitHub - paradedb/drizzle-paradedb：用于ParadeDB的Drizzle官方扩展 · GitHub](https://github.com/paradedb/drizzle-paradedb)

**原文标题**: [GitHub - paradedb/drizzle-paradedb: Official extension to Drizzle for use with ParadeDB · GitHub](https://github.com/paradedb/drizzle-paradedb)

该仓库是 ParadeDB 官方为 Drizzle ORM 提供的集成扩展，支持 BM25 索引管理及完整 ParadeDB API 查询，适用于 Node.js 和 TypeScript 项目。

- 📦 官方 Drizzle 集成：专为 ParadeDB 设计的 ORM 扩展，基于 pg_search Postgres 扩展
- 🚀 核心功能：支持 BM25 全文搜索、向量检索、聚合查询及分面搜索
- 🛠️ 环境要求：Node 22.12+、Drizzle 1.0+、ParadeDB 0.22.0+、PostgreSQL 15+
- 📚 示例丰富：提供快速入门、分面搜索、自动补全、相似查询、混合 RRF 及 RAG 等示例
- 🤝 社区支持：通过 Slack、GitHub Discussions 获取帮助，商业支持可联系团队
- 📄 开源协议：采用 MIT 许可证，包含贡献指南和行为准则

---

### [我的智能编码设置，2026 年 7 月 | Domenic Denicola](https://domenic.me/agentic-coding-setup/)

**原文标题**: [My Agentic Coding Setup, July 2026 | Domenic Denicola](https://domenic.me/agentic-coding-setup/)

该文章介绍了作者在 2026 年 7 月使用的 AI 辅助开发设置，重点是通过 Tailscale、Linux 虚拟机、ChatGPT 桌面应用等工具实现高效、灵活的远程编码工作流。

- 💻 核心要求：代理需在 Linux 上运行，支持无缝切换设备、并行工作流、最小化审批中断，并允许通过手机修复生产错误。
- 🔗 Tailscale：将桌面、笔记本和 Linux 虚拟机连接成私有网络，支持 SSH 和 HTTPS 访问，实现远程开发和服务器暴露。
- 🖥️ 虚拟机设置：使用 Ubuntu Server ISO 创建可丢弃的 Linux 虚拟机，安装 Tailscale 和代理工具（Claude Code、Codex CLI），并配置零审批权限。
- 🛠️ 代理工具：ChatGPT 桌面应用提供流畅的 SSH 支持和会话同步，而 Claude 应用在远程工作流和会话管理上表现较差。
- 🔒 安全策略：启用`--dangerously-skip-permissions`和 sudo 权限，允许代理自主操作，但风险可控，建议频繁推送到 GitHub 备份。
- 📂 Git 工作树：支持多个代理在同一个项目中并行工作，ChatGPT 和 Claude 应用内置工作树功能，但 Claude 的默认位置可能引发冲突。
- 🖥️ VS Code 集成：通过 Remote-SSH 扩展远程查看和编辑代理代码，ChatGPT 应用提供直接打开工作树的按钮。
- 🌐 开发服务器：使用 Portless 工具暴露代理的预览服务器，通过 Tailscale URL 提供安全上下文，避免端口冲突。
- 🔄 配置同步：使用 chezmoi 管理 dotfiles，包括`AGENTS.md`和技能文件，跨设备同步并备份到私有 GitHub 仓库。
- 📱 手机开发：通过 ChatGPT 移动应用和 Tailscale VPN，实现从手机远程启动代理、修复 bug 并部署，提升移动工作流效率。
- ⏳ 剩余挑战：建议使用开发容器提升安全性，改进会话模型以支持文件夹重命名，并备份会话历史以保留设计决策记录。

---

### [你误解了承诺的意义 | Domenic Denicola](https://domenic.me/youre-missing-the-point-of-promises/)

**原文标题**: [You're Missing the Point of Promises | Domenic Denicola](https://domenic.me/youre-missing-the-point-of-promises/)

这篇关于 Promise 的文章指出，许多 JavaScript 库错误地将 Promise 理解为简单的回调聚合器，而忽略了其真正的价值：实现异步操作的函数式组合和错误冒泡，使其行为与同步代码平行。

- 🎯 **Promise 的真正目的**：不是简单的回调聚合，而是为异步操作提供与同步函数相同的返回值和异常抛出能力，从而实现函数组合和错误冒泡。
- 🔗 **关键机制 `then` 函数**：`then` 必须返回一个新的 Promise，并支持四种场景（成功/失败处理器的返回值或异常），从而允许链式调用和错误传递。
- ⚠️ **常见误区**：jQuery 等库的 Promise 实现仅支持成功处理器的返回值，忽略了异常处理和错误冒泡，导致无法正确模拟同步行为。
- 🚫 **兼容性问题**：不符合 Promises/A 规范的库（如 jQuery）会破坏库之间的互操作性，迫使开发者使用丑陋的 hack 来检测和处理伪 Promise 对象。
- ✅ **推荐方案**：使用符合 Promises/A+ 规范的库（如 Q、RSVP.js、when.js），它们提供完整的函数组合和错误处理能力，并支持跨库互操作。
- 🔧 **实用建议**：如果被迫使用不规范的 Promise（如 jQuery 的），应尽快用 `Q.when()` 等工具将其转换为真正的 Promise。

---

### [GitHub - jsdom/jsdom: 多种 Web 标准的 JavaScript 实现，适用于 Node.js · GitHub](https://github.com/jsdom/jsdom)

**原文标题**: [GitHub - jsdom/jsdom: A JavaScript implementation of various web standards, for use with Node.js · GitHub](https://github.com/jsdom/jsdom)

jsdom 是一个纯 JavaScript 实现的 Web 标准库，用于 Node.js，模拟浏览器环境以支持测试和网页抓取。

- 🎯 **核心用途**：模拟浏览器子集，用于测试和抓取真实 Web 应用，支持 DOM 和 HTML 标准。
- ⚙️ **基本用法**：通过 `JSDOM` 构造函数解析 HTML 字符串，返回包含 `window` 对象的实例，可操作 DOM。
- 🔧 **自定义选项**：支持设置 URL、referrer、内容类型、节点位置、存储配额等参数，以定制 jsdom 行为。
- 🚨 **脚本执行**：默认禁用脚本执行，可通过 `runScripts: "dangerously"` 启用，但需注意安全风险；`runScripts: "outside-only"` 允许外部脚本运行。
- 🎨 **视觉模拟**：`pretendToBeVisual: true` 可模拟视觉浏览器行为，如启用 `requestAnimationFrame`，但仍无实际渲染。
- 📦 **资源加载**：通过 `resources: "usable"` 加载子资源（如脚本、样式、图片），支持自定义 userAgent、代理和拦截器。
- 🖥️ **虚拟控制台**：可自定义虚拟控制台，转发或过滤日志，支持 `jsdomError` 事件处理。
- 🍪 **Cookie 管理**：支持自定义 Cookie 罐，共享或预置 Cookie，基于 `tough-cookie` 库。
- 🛠️ **高级功能**：提供 `serialize()`、`nodeLocation()`、`getInternalVMContext()`、`reconfigure()` 等方法，以及 `fromURL()`、`fromFile()`、`fragment()` 便捷 API。
- 🖼️ **Canvas 支持**：需安装 `canvas` 包以扩展 `<canvas>` 元素功能。
- 🔍 **编码嗅探**：支持二进制数据输入，自动嗅探编码，并遵循 BOM 和 `Content-Type` 优先级。
- ⏰ **定时器管理**：`window.close()` 可终止所有定时器，避免进程持续运行。
- 🐞 **调试工具**：可使用 Chrome DevTools 调试，并借助 `jsdom-devtools-formatter` 优化 DOM 元素显示。
- ⚠️ **限制与未实现功能**：不支持异步脚本加载的自动检测、导航（如点击链接）和 CSS 布局计算，需通过变通方法解决。

---

### [多梅尼克·德尼科拉](https://domenic.me/)

**原文标题**: [Domenic Denicola](https://domenic.me/)

概述总结
一位最近退休的浏览器软件工程师分享了他的职业生涯、当前生活以及精选作品集。

- 🌐 专注于浏览器开发与网络标准，曾参与 JavaScript Promise、模块、流、自定义元素等标准制定
- 🚀 近期工作涉及投机加载优化性能及内置 AI API，使浏览器/OS 的 AI 模型对开发者可用
- 🗼 2022 年移居东京，探索 AI 能力与安全研究，同时维护 jsdom 开源项目并学习日语
- 📝 最新文章涵盖 AI 编码设置、Windows 原生应用开发困境及流标准反思
- ⭐ 精选作品包括机器学习改进的间隔重复系统、数学意识哲学探讨及“解释网络魔法”的扩展网络宣言
- 🔧 网络标准领域涉及内置 AI API 设计、套接字与文件流读取的 JavaScript API 设计
- 💻 JavaScript 与 Node.js 内容涵盖 ES6 迭代器、严格模式作用域及 npm 对等依赖功能
- 📚 其他作品包括代理开源维护反思、退休感言及 AI 生产力研究参与报告

---

### [Node.js — 2026 年 7 月 27 日，星期一，安全发布](https://nodejs.org/en/blog/vulnerability/july-2026-security-releases)

**原文标题**: [Node.js — Monday, July 27, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/july-2026-security-releases)

Node.js 项目将于 2026 年 7 月 27 日发布安全更新，修复 26.x、24.x 和 22.x 版本中的高危漏洞，建议用户及时升级至受支持版本。

- 🔒 修复 26.x、24.x 和 22.x 版本中的高危安全漏洞
- 📅 安全版本将于 2026 年 7 月 27 日（周一）或之后发布
- ⚠️ 已停止维护的版本始终受安全漏洞影响，需更新至受支持版本
- 🔗 安全政策详见：https://nodejs.org/en/security/
- 📧 可通过 nodejs-sec 邮件列表获取安全公告更新
- 🛡️ 漏洞报告流程请参考：https://github.com/nodejs/node/blob/master/SECURITY.md

---

### [收藏贡献者洞察](https://insights.linuxfoundation.org/collection/details/ojsf/contributors?timeRange=past365days&start=2025-07-23&end=2026-07-23)

**原文标题**: [Collection Contributors Insights](https://insights.linuxfoundation.org/collection/details/ojsf/contributors?timeRange=past365days&start=2025-07-23&end=2026-07-23)

OpenJS Foundation 是一个由 Linux 基金会主办的项目集合，旨在支持 JavaScript 生态系统，促进协作与创新。该集合包含 43 个项目和 115K 贡献者，但平均健康状况为“令人担忧”（30 分）。以下是对该集合的总结：

- 🏢 **托管项目**：包含 43 个支持 JavaScript 生态系统的项目/仓库。
- 👥 **贡献者规模**：拥有 115,000 名贡献者，但活跃度数据仍在加载中。
- ⚠️ **健康状况**：平均健康状况为“令人担忧”（30 分），需要关注。
- 📊 **分析工具**：LFX Insights 提供贡献者、组织、地理分布等数据，帮助决策。
- 🔄 **数据加载**：多个关键指标（如贡献者排行榜、活跃组织、季度留存率）仍在加载中。
- 🌍 **地理分布**：支持按组织和贡献者查看地理分布，但数据尚未完全加载。
- 🔗 **协作功能**：包括协作活动、依赖关系分析等，但部分数据待更新。
- 🛠️ **其他工具**：提供 AI 代码追踪、产品更新、个人/组织仪表板等功能。

---

### [项目 | OpenJS 基金会](https://openjsf.org/projects)

**原文标题**: [Projects | OpenJS Foundation](https://openjsf.org/projects)

OpenJS 基金会是一个中立的非营利组织，为 JavaScript 生态系统中的关键项目提供家园，并通过跨项目委员会（CPC）协调治理、促进项目生命周期管理。

- 🏠 **中立家园**：为 Appium、Node.js、jQuery 等核心 JavaScript 项目提供可持续的社区支持。
- ⚙️ **生命周期管理**：通过 CPC 监督项目从孵化到归档的六个阶段（影响、孵化、归档等）。
- 🌟 **影响项目**：托管 Electron、Express、webpack 等 7 个顶级项目，涵盖桌面应用、Web 框架和打包工具。
- 📦 **孵化与成长**：支持 Lit、kepler.gl 等孵化项目，以及 ESLint、Jest 等 20+ 成熟项目。
- 💰 **定向资助**：允许会员（白金无上限，金银按比例）向特定项目或倡议提供额外资金。
- 🤝 **社区参与**：鼓励企业雇佣贡献者、举办活动，个人可通过 GitHub Sponsors 等平台直接支持。

---

### [Bun 在 X 上表示：“Bun v1.4 将是自 Bun v1.0 以来在 Node.js 兼容性上最大的一次飞跃 https://t.co/fk9WHd8Zzf” / X](https://x.com/bunjavascript/status/2079863261630267773)

**原文标题**: [Bun on X: "Bun v1.4 will be our biggest jump in Node.js compatibility since Bun v1.0 https://t.co/fk9WHd8Zzf" / X](https://x.com/bunjavascript/status/2079863261630267773)

Bun v1.4 将带来自 v1.0 以来最大的 Node.js 兼容性提升
- 📈 超过 505 项测试和修复等待合并，兼容性大幅提升
- 🔍 通过差分模糊测试与 Node.js 对比，覆盖运行时 API 和系统调用
- 🛡️ 扫描安全漏洞，修复内存使用和边缘案例问题
- 🗓️ 用户询问发布日期，但尚未公布具体时间

---

### [Bun — 一个快速的全能 JavaScript 运行时](https://bun.com/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.com/)

Bun v1.3.14 发布，这是一个快速、增量可用的全栈 JavaScript/TypeScript/JSX 工具包，包含运行时、打包器、测试运行器和包管理器，兼容 Node.js。

- 🚀 Bun v1.3.14 版本发布，作为快速的全栈 JavaScript 工具包
- ⚡ 支持 Linux、macOS 和 Windows 系统，安装命令简单
- 🛠️ 包含运行时、打包器、测试运行器和包管理器，可增量采用
- 🔄 目标实现 100% Node.js 兼容性
- 📊 打包性能领先：Bun 在打包 10,000 个 React 组件时仅需 269.1ms，远快于 Rolldown、esbuild、Farm 和 Rspack

---

### [pnpm 11.11-11.14 | pnpm](https://pnpm.io/blog/releases/11.11-11.14)

**原文标题**: [pnpm 11.11-11.14 | pnpm](https://pnpm.io/blog/releases/11.11-11.14)

pnpm 11.11 到 11.14 版本新增了原生工作区发布管理、诊断命令、包和团队管理命令、聚合覆盖、带协议的 peerDependencies 说明符，并修复了路径遍历漏洞、降低了内存使用、解决了 peer 依赖死锁等问题。

- 📦 **原生工作区发布管理**：新增 `pnpm change`、`pnpm lane` 和 `pnpm version -r` 命令，支持在工作区内直接进行版本管理和发布，无需额外工具。
- 🩺 **pnpm doctor 诊断命令**：提供全面的安装和环境诊断，包括版本、存储、网络连接等，并支持 `--offline`、`--json` 和 `--benchmark` 选项。
- 🔑 **pnpm access 和 pnpm team 命令**：用于管理注册表上的包访问权限、可见性以及组织团队和成员。
- 🔄 **聚合覆盖（Convergence overrides）**：新增空范围覆盖选择器，使兼容的依赖项收敛到同一版本，同时保持不兼容依赖项的独立解析。
- 🔗 **peerDependencies 支持带协议说明符**：允许使用命名注册表、`npm:` 别名、`file:` 等协议的说明符，并基于其语义版本范围进行匹配。
- 🚀 **性能优化与安全修复**：冷缓存解析内存峰值降低约 30%，修复了路径遍历漏洞、死锁问题以及多个 `pnpm install`、`pnpm update` 等命令的错误。

---

### [使用 Codemod 自动化 ESLint 迁移 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/07/eslint-codemod-migrations/)

**原文标题**: [Automating ESLint migrations with Codemod - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/07/eslint-codemod-migrations/)

ESLint 与 Codemod 合作推出官方自动化迁移工具，支持 v8 到 v9 及 v9 到 v10 的升级，并提供开源代码和社区贡献渠道。

- 🚀 **合作发布**：ESLint 与 Codemod 联合推出官方 codemod，简化 v8→v9 和 v9→v10 的迁移流程，代码托管于 eslint/codemods 和 Codemod Registry。
- 🛠️ **Codemod 平台**：开源工具，支持多步骤转换、跨文件重构、多语言和 AI 辅助，已被 React、Node.js 等主流项目采用。
- 📦 **v8→v9 配置迁移**：`@eslint/v8-to-v9-config`可自动提取`eslintConfig`、清理注释、转换规则选项，并处理`env`到`globals`的映射。
- 📝 **v8→v9 规则迁移**：`@eslint/v8-to-v9-custom-rules`支持 CommonJS/ESM 规则，自动替换已弃用的`context`方法，并添加`meta`和`create`对象格式。
- ⚠️ **手动检查要点**：迁移后需审查 TODO 注释、`getComments`方法参数、高阶包装器，并运行测试套件验证规则。
- 🔄 **v9→v10 迁移**：`@eslint/v9-to-v10`包含配置、规则、RuleTester 和 Linter API 四个独立 codemod，可单独运行。
- 🎯 **社区参与**：鼓励用户提交 issue 或 PR 贡献新 codemod，合并后自动发布至 Codemod Registry。
- 📚 **资源链接**：详见 v9 和 v10 升级指南、Codemod 文档及 Discord 社区。

---

### [发布 v13.0.0 · WiseLibs/better-sqlite3 · GitHub](https://github.com/WiseLibs/better-sqlite3/releases/tag/v13.0.0)

**原文标题**: [Release v13.0.0 · WiseLibs/better-sqlite3 · GitHub](https://github.com/WiseLibs/better-sqlite3/releases/tag/v13.0.0)

better-sqlite3 v13.0.0 版本发布，这是首个基于 N-API 的重大更新，支持跨 Node.js、Electron 及 Bun 等运行时的预编译二进制文件。

- 🎉 首个基于 N-API 的版本，预编译二进制文件可跨 Node.js、Electron 和 Bun 等运行时使用
- 🔧 移除了已弃用的 prebuild-install 依赖，预编译二进制文件直接随代码发布
- 🆕 新增 db.explain() 方法，用于运行 EXPLAIN 查询时无需提供绑定参数
- 📝 新增 preparedStatement.toString() 方法，可获取预处理语句的扩展 SQL
- 🛠️ 修复了 SqliteError 跨 realm 兼容性和 Error.isError 问题
- 👥 感谢新贡献者 dennismutuku2005 的首次贡献

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

Tiger Cloud 提供可扩展的 PostgreSQL 时序数据库服务，支持从 IoT 到企业级的大规模工作负载，并附赠 $1000 试用额度。

- 📊 支持每日 3 万亿指标、3 PB 数据及 1 千万亿数据点的超大规模实时处理
- 💰 新用户注册即获 $1000 额度（30 天有效），无需信用卡
- 🚀 通过最多 10 节点副本集实现读写分离，结合 SSD/S3 分层存储实现弹性扩展
- 💡 计算与存储独立扩展，避免为闲置容量付费，优化成本与性能
- 🔒 多可用区集群支持自动故障转移、时间点恢复与跨区域备份，保障高可用
- 🛡️ 符合 SOC 2、HIPAA、GDPR 标准，提供加密、SSO、RBAC 及审计日志
- 📈 深度可观测性：查询钻取与仪表盘，集成 CloudWatch、Datadog、Prometheus
- ⚡ 数分钟内完成数据库部署，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 与主流云提供商及 PostgreSQL 生态无缝集成
- 🏢 企业级功能：合同化 SLA、区域数据隔离、24/7 全球专家支持

---

### [解析 AsyncAPI npm 供应链妥协与导入时载荷投递 | 微软安全博客](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)

**原文标题**: [Unpacking the AsyncAPI npm supply chain compromise and import-time payload delivery | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)

2026 年 7 月 14 日，AsyncAPI npm 组织遭受供应链攻击，五个恶意包版本通过 GitHub Actions OIDC 发布，利用 import 时执行载荷，绕过常见缓解措施，最终部署 Miasma 模块化后门。

- 🎯 攻击概述：攻击者通过恶意 PR 利用`pull_request_target`工作流窃取 bot 令牌，随后通过 GitHub Actions OIDC 发布五个恶意 npm 包，影响开发者工作站、CI/CD 管道和容器构建。
- 🚨 执行机制：恶意载荷在`require()`或`import`时立即执行，而非通过`postinstall`钩子，因此`npm install --ignore-scripts`无法防御。载荷生成隐藏子进程，从 IPFS 下载第二阶段载荷。
- 🔑 第二阶段载荷：`sync.js`通过三层加密解密 Miasma 模块化运行时，包含 C2 通信、持久化（Windows 注册表、Linux systemd、macOS shell RC）和去中心化回退通道（Nostr、以太坊、BitTorrent DHT 等）。
- 🔍 受影响版本：`@asyncapi/specs@6.11.2-alpha.1`和`6.11.2`、`@asyncapi/generator@3.3.1`、`@asyncapi/generator-components@0.7.1`、`@asyncapi/generator-helpers@1.1.1`。
- 🛡️ 缓解措施：立即移除所有受影响版本，清除 npm 和 Yarn 缓存，查找`sync.js`和`NodeJS`伪装目录，阻止对`85.137.53[.]71`的出站连接，轮换所有可能暴露的凭据。
- 🔬 检测指标：Microsoft Defender 将恶意文件检测为`Trojan:JS/MiasmStealer.SC`和`Trojan:Script/Supychain.A`，并提供高级狩猎查询以发现相关活动。
- ⚠️ 攻击根源：攻击源于`asyncapi/generator`仓库中配置错误的`pull_request_target`工作流，该工作流执行了攻击者控制的 PR 代码，暴露了`asyncapi-bot` PAT。

---

### [新研究识别出 5 个前沿领域的 53 个 Slopsquatting 目标](https://socket.dev/blog/slopsquatting-targets-across-frontier-llms)

**原文标题**: [New Study Identifies 53 Slopsquatting Targets Across 5 Front...](https://socket.dev/blog/slopsquatting-targets-across-frontier-llms)

概述：一项大规模攻击活动利用被入侵的 GitHub 仓库中的 GitHub Actions，针对 cPanel 和 WHM 的 CVE-2026-41940 漏洞进行利用，并窃取服务器凭证。

- 🔍 攻击活动大规模滥用 GitHub Actions，在已攻破的仓库中执行恶意操作
- 🚨 利用 cPanel 和 WHM 中的 CVE-2026-41940 漏洞进行分布式攻击
- 🔑 攻击目标为窃取服务器凭证，威胁系统安全
- 🕵️ 由研究员 Kirill Boychenko 于 2026 年 7 月 22 日报告此事件

---

### [使用 BullMQ 在 Node.js 中处理后台任务](https://flaviocopes.com/nodejs-background-jobs-bullmq/)

**原文标题**: [Background jobs in Node.js with BullMQ](https://flaviocopes.com/nodejs-background-jobs-bullmq/)

本教程介绍了如何使用 BullMQ 和 Redis 在 Node.js 中构建可靠的背景任务队列，包括生产者、工作者、重试、退避、进度、并发和幂等性等关键概念。

- 📋 **系统架构**：由 HTTP 应用（生产者）、Redis 队列和工作者三部分组成，应用快速添加任务，工作者异步处理
- 🐳 **启动 Redis**：使用 Docker 运行 Redis 容器，并创建 Node.js 项目安装 bullmq 和 express 依赖
- ⚙️ **创建队列**：定义队列名称和连接配置，设置默认任务选项（最多 5 次重试、指数退避、完成/失败任务清理规则）
- 🚀 **添加任务 API**：通过 Express POST 端点接收请求，使用 jobId 确保同一用户的任务唯一性，返回 202 Accepted 状态
- 👷 **工作者实现**：监听队列处理任务，支持进度更新、完成/失败事件监听，以及优雅关闭
- ⏱️ **重试与退避**：指数退避（1 秒、2 秒、4 秒等）避免立即重试造成压力，可添加随机抖动防止同时重试
- 🔒 **幂等性设计**：使用数据库记录操作键（如`welcome-{userId}`）确保任务安全重复执行，不依赖"恰好一次"假设
- 📊 **进度与状态**：提供 GET 端点查询任务状态、进度、结果和失败原因，注意保护敏感数据
- 🔔 **队列事件**：使用 QueueEvents 监听跨进程的完成/失败事件，基于 Redis 流实现
- ⚡ **并发控制**：设置 concurrency:5 实现 I/O 密集型任务并行处理，CPU 密集型任务需多进程/线程
- 🎯 **优先级与延迟**：支持任务延迟执行（如 60 分钟后）和优先级设置（数值越低优先级越高）
- 🏭 **独立部署**：Web 应用和工作者分离运行，可独立扩展，生产环境需持久化 Redis、启用认证和 TLS
- 💡 **关键设计原则**：队列不消除失败，而是提供重试、检查和恢复的场所；可靠任务需包含验证输入、稳定名称、有界重试、幂等策略、进度数据、日志和清理策略

---

### [GitHub - sindresorhus/execa：面向人类的进程执行 · GitHub](https://github.com/sindresorhus/execa)

**原文标题**: [GitHub - sindresorhus/execa: Process execution for humans · GitHub](https://github.com/sindresorhus/execa)

Execa 是一个面向程序员的进程执行库，基于 child_process 构建，提供简洁、安全且功能丰富的接口。

- 🚀 **简洁语法**：支持 Promise 和模板字符串，类似 zx，无需转义或引用，避免 shell 注入。
- 🖥️ **脚本接口**：提供 `$` 函数，可直接执行命令并支持管道、变量插值等。
- 🏠 **本地二进制**：无需 npx 即可直接执行本地安装的二进制文件。
- 🪟 **Windows 优化**：改进对 shebang、PATHEXT、优雅终止等 Windows 特性的支持。
- 🔍 **调试友好**：提供详细错误信息、详细模式及自定义日志功能。
- 🔗 **管道增强**：支持多进程管道，可获取中间结果、多源/目标、取消管道。
- 📄 **输出处理**：自动分割文本行、去除多余换行，支持渐进式迭代。
- 🎯 **灵活输入/输出**：支持文件、字符串、Uint8Array、迭代器、对象等多种输入/输出类型。
- 📡 **流式支持**：兼容 Node.js 流和 Web 流，可转换为双工流。
- 💬 **进程间通信**：支持与子进程交换消息，可传递任意类型数据。
- 🛡️ **可靠终止**：确保子进程在拦截终止信号或主进程意外结束时正常退出。

---

### [发布 v10.0.0 · sindresorhus/execa · GitHub](https://github.com/sindresorhus/execa/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · sindresorhus/execa · GitHub](https://github.com/sindresorhus/execa/releases/tag/v10.0.0)

Execa v10.0.0 发布，主要包含破坏性变更、新功能和修复。

- 🚨 **重大变更**：要求 Node.js 22 或更高版本，子进程现为标准 Promise，需通过 `subprocess.nodeChildProcess` 访问原生 API
- ❌ **移除功能**：删除了 `execaCommand()` 和 `execaCommandSync()`，改用模板字符串语法；移除了旧的 `stdio: [..., 'ipc']` 语法，改用 `ipc: true` 选项
- 🔧 **行为变更**：当 `input` 或 `inputFile` 与继承的 `stdin` 结合时，现在优先使用显式输入而非忽略
- 🎯 **新选项**：新增 `killDescendants` 选项，可终止子进程的后代进程（如 shell 模式下的子进程）
- 🌊 **Web 流支持**：子进程可通过 `readableStream()`、`writableStream()` 或 `transformStream()` 转换为 Web 流
- 🔗 **管道增强**：`subprocess.pipe()` 现在返回目标子进程的方法，可直接迭代输出行、转换为流或交换 IPC 消息
- 📁 **额外文件描述符**：支持通过 `{value, input: true}` 对象将额外文件描述符作为输入
- 🛠️ **类型改进**：`transform` 生成器函数的 `chunk` 参数现在根据转换模式进行类型化（字符串、Uint8Array 或 unknown）
- 🐛 **修复**：修复了 `ipc` 选项为 `true` 时，文件描述符特定选项（如 `verbose`、`maxBuffer`）与 `ipc` 冲突的问题

---

### [GitHub - sindresorhus/eslint-package-json: 针对 package.json 的强大 ESLint 规则 · GitHub](https://github.com/sindresorhus/eslint-package-json)

**原文标题**: [GitHub - sindresorhus/eslint-package-json: Powerful ESLint rules for package.json · GitHub](https://github.com/sindresorhus/eslint-package-json)

eslint-package-json 是一个强大的 ESLint 插件，用于检查和自动修复 `package.json` 文件中的常见错误，支持超过 50 条规则，并深度集成 ESLint 的 flat config 和 `@eslint/json`。

- 🎯 **核心功能**：提供 50+ 条规则，涵盖字段验证、依赖规范、路径检查、导出配置等，多数规则支持自动修复。
- ⚙️ **配置方式**：支持 `recommended` 和 `all` 预设配置，也可手动启用规则，需 ESLint >=10.4 及 flat config。
- 🔧 **自动修复**：多数规则可通过 `--fix` 自动修复，部分规则提供编辑器建议（💡）。
- 📦 **安装与使用**：通过 `npm install eslint-package-json` 安装，在 `eslint.config.js` 中引入并配置插件。
- 🚫 **规则禁用**：由于 `package.json` 不能包含注释，需在 `eslint.config.js` 中通过 `rules` 对象禁用特定规则。
- 🔄 **与其他工具对比**：相比 `eslint-plugin-package-json` 规则更精简强大；相比 `npm-package-json-lint` 支持自动修复和 ESLint 生态集成。

---

### [TypeScript 中的独立 ActivityPub 机器人](https://botkit.fedify.dev/)

**原文标题**: [Standalone ActivityPub bots in TypeScript](https://botkit.fedify.dev/)

以下是您提供的 BotKit 文档导航内容的概述摘要：

BotKit 是一个用于构建联邦宇宙机器人的工具包，提供了从入门到部署的完整指南。

- 🤖 BotKit 概述：一个用于构建联邦宇宙（ActivityPub）机器人的工具包
- 📚 学习资源：包含入门指南、构建 RSS 机器人教程、食谱和示例
- 🧠 核心概念：涵盖 Bot、Instance、Session、Events、Message、Text、Repository 等关键概念
- 🚀 部署选项：支持 Deno Deploy、Cloudflare Workers、Docker 和自托管
- 🗄️ 存储与消息队列：提供 PostgreSQL、Redis、SQLite 等集成
- 📖 参考文档：包括 @fedify/botkit 及其扩展包（Postgres、Redis、SQLite）的详细参考
- 🎨 外观定制：支持 Matrix 主题和外观配置

---

### [发布 v0.5.0 · nubjs/nub · GitHub](https://github.com/nubjs/nub/releases/tag/v0.5.0)

**原文标题**: [Release v0.5.0 · nubjs/nub · GitHub](https://github.com/nubjs/nub/releases/tag/v0.5.0)

Nub v0.5.0 发布，主要新增 `nub init` 脚手架、改进包管理器兼容性并优化 Node 安装速度。

- 🚀 **新增 `nub init` 命令**：一键生成 TypeScript 项目，默认使用 TypeScript 7，零运行时依赖，严格类型检查，并自动初始化 git。
- 🎯 **增强 `nub create` 命令**：支持 `create-*` 生态模板（如 Vue、Vite、Nuxt），并能自动检测 Nub 环境，输出相应命令。
- 🔧 **包管理器修复**：修复 `packageExtensions`、`dlx/create` 子进程环境变量、`nub update` 支持 dist-tag、`hoisted` 链接器、`approve-builds`、`dedupe` 等多项问题。
- ⚡ **性能优化**：缓存 dist-tag 解析、精简元数据请求、流式下载 Node 安装包并重叠校验和获取，提升安装速度。
- 🛠️ **进程管理改进**：修复 macOS 下进程组孤儿问题、`nub watch` 支持 `--env-file`、`node-gyp` 兼容性增强。
- 🌍 **平台支持**：`nub upgrade` 支持 Windows 自拥有通道，Android/Termux 无需 JVM 即可源码构建。
- 📦 **内部更新**：同步上游 aube 引擎至 v1.32.0，清理死代码并收紧可见性。

---

### [介绍 Nub：Node.js 的一体化工具包 — Nub](https://nubjs.com/blog/introducing-nub)

**原文标题**: [Introducing Nub: an all-in-one toolkit for Node.js — Nub](https://nubjs.com/blog/introducing-nub)

Nub 是一个基于 Node.js 的全能工具包，旨在通过 Rust CLI 增强 Node.js 开发体验，而非替代它。它集成了文件运行、脚本运行、包管理、版本管理等功能，并兼容 TypeScript、JSX 等现代特性。

- 🚀 **快速脚本运行**：`nub run` 比 `pnpm run` 快 24 倍，通过 Rust 实现，避免 Node.js 启动开销。
- ⚡ **高效二进制运行**：`nubx` 比 `npx` 快 19 倍，直接执行 `node_modules/.bin` 中的 CLI，无需 Node 引导。
- 🛠️ **TypeScript 原生支持**：`nub index.ts` 直接运行 TypeScript 文件，支持枚举、命名空间、参数属性等，比 `tsx` 快 2.9 倍。
- 🔄 **内置文件监听**：`nub watch` 基于依赖图自动重启，无需配置，支持 TypeScript 文件变化。
- 📦 **全面包管理**：`nub install` 兼容 pnpm、npm、Yarn 和 Bun 的锁文件，性能优越，安全默认（如禁止生命周期脚本）。
- 🌐 **版本管理**：`nub node install` 自动从 `.node-version` 或 `.nvmrc` 解析并安装 Node.js 版本。
- 🧩 **现代 API 支持**：提供 Worker、Temporal、WebSocket 等 API，兼容旧版 Node，无需迁移。
- 🔒 **零锁定**：无 Nub 特定 API，移除后代码仍可正常运行，完全兼容现有 Node.js 生态。

---

### [GitHub - dmtrKovalenko/odiff: 一个极速的 SIMD 优先图像比较库（含 Node.js API）](https://github.com/dmtrKovalenko/odiff)

**原文标题**: [GitHub - dmtrKovalenko/odiff: A very fast SIMD-first image comparison library (with nodejs API) · GitHub](https://github.com/dmtrKovalenko/odiff)

ODiff 是一款全球最快的单线程像素级图像差异比较工具，采用 Zig 语言编写并支持 SIMD 优化，提供 CLI、Node.js 和服务器模式，适用于视觉回归测试等场景。

- 🚀 性能卓越：比 ImageMagick 和 pixelmatch 快 6 倍以上，8K 图像比较仅需约 2 秒
- 🖼️ 多格式支持：可比较 PNG、JPEG、WebP、TIFF 等不同格式图像，支持不同布局
- ⚙️ 丰富功能：支持抗锯齿检测、区域忽略、YIQ NTSC 视觉差异算法，内存占用可控
- 🔧 多种使用方式：提供 CLI、Node.js 绑定、服务器模式（减少进程开销），以及 Playwright/Cypress 插件
- 📊 详细差异报告：返回像素差异数量、百分比，可选行/列差异位置，支持缓冲区比较
- 🛠️ 高度可配置：支持差异颜色、阈值、输出遮罩、忽略区域等参数，100% 测试覆盖
- 📦 跨平台安装：通过 npm 包（odiff-bin）或直接下载预编译二进制文件，支持主流平台

---

### [GitHub - frinyvonnick/node-html-to-image: 一个从 HTML 生成图片的 Node.js 模块](https://github.com/frinyvonnick/node-html-to-image)

**原文标题**: [GitHub - frinyvonnick/node-html-to-image: A Node.js module that generates images from HTML · GitHub](https://github.com/frinyvonnick/node-html-to-image)

这是一个基于 Node.js 的 HTML 转图片库，利用 Puppeteer 和 Handlebars 实现从 HTML 生成 PNG/JPEG 图像。

- 🌄 核心功能：将 HTML 内容转换为 PNG 或 JPEG 图像，支持自定义输出路径和图像质量
- 🛠️ 安装简单：通过 `npm install node-html-to-image` 或 `yarn add node-html-to-image` 即可使用
- 📝 模板支持：内置 Handlebars 模板引擎，支持变量、条件、循环等逻辑，并可自定义辅助函数
- 🖼️ 图像处理：支持本地图像通过 Base64 嵌入，远程图像直接引用，可生成透明背景 PNG
- ⚙️ 丰富选项：提供输出分辨率、等待策略、编码格式、选择器、超时时间等配置项
- 💾 灵活输出：支持保存到磁盘或返回 Buffer 对象，便于直接用于 Web 响应或进一步处理
- 🔄 批量生成：通过数组形式的内容可一次生成多张图片，每张可独立指定输出路径
- 🎭 多 Puppeteer 支持：可替换为 puppeteer-core 或 puppeteer-extra 等不同库
- 📦 类型安全：使用 TypeScript 编写，提供完整的类型定义支持
- ⭐ 社区活跃：拥有 879 颗星、123 个分支，提供 CLI 工具和相关文章资源

---

### [GitHub - delvedor/find-my-way: 一个极快的 HTTP 路由器 · GitHub](https://github.com/delvedor/find-my-way)

**原文标题**: [GitHub - delvedor/find-my-way: A crazy fast HTTP router · GitHub](https://github.com/delvedor/find-my-way)

find-my-way 是一个基于 Radix Tree 的高性能 HTTP 路由器，支持路由参数、通配符，并独立于框架。

- ⚡ **极致性能**：内部使用高度优化的 Radix Tree（紧凑前缀树），速度极快，可与常用路由器进行基准对比。
- 📦 **安装简便**：通过 `npm i find-my-way --save` 即可安装使用。
- 🔧 **灵活配置**：支持自定义默认路由、错误处理（如畸形 URL）、忽略尾部斜杠或重复斜杠、设置参数最大长度、关闭大小写敏感等选项。
- 🧩 **路由注册**：使用 `on(method, path, handler, store)` 注册路由，支持单方法、多方法数组、版本化路由及自定义约束策略。
- 🗺️ **路径格式丰富**：支持静态路径、参数化路径（`:param`）、正则参数、通配符（`*`）及可选参数（`?`），并明确匹配优先级。
- 🔍 **路由查找与匹配**：提供 `lookup`（自动处理请求/响应）、`find`（直接查找路由对象）、`findRoute`（按模式查找）等方法。
- 🛠️ **路由管理**：支持 `off` 注销路由、`reset` 清空路由表、`prettyPrint` 打印路由树（含元数据）、`routes` 列出所有注册路由。
- 🔒 **约束支持**：内置基于 semver 的版本约束和基于正则的主机名约束，并可自定义约束策略（如 Accept 头）。
- ⚠️ **注意事项**：不能注册仅参数不同的重复路由；正则路由可能影响性能；自定义约束策略需谨慎使用。

---

### [GitHub - gitify-app/gitify: 菜单栏上的 Git 通知。支持 macOS、Windows 和 Linux。](https://github.com/gitify-app/gitify)

**原文标题**: [GitHub - gitify-app/gitify: Git notifications on your menu bar. Available on macOS, Windows & Linux. · GitHub](https://github.com/gitify-app/gitify)

Gitify 是一个在菜单栏显示 Git 通知的开源应用，支持多平台和多 Git 平台。

- 🔔 统一来自 GitHub、Gitea、Bitbucket 等 Git 平台的通知
- ⚒️ 支持多平台：GitHub Cloud、GitHub Enterprise、Gitea、Forgejo、Codeberg、Bitbucket Cloud
- 💻 跨平台兼容：macOS、Windows 和 Linux
- 🎨 可自定义设置、过滤器和主题
- 🖥️ 托盘/菜单栏集成，提供原生体验
- ⚡ 快速、原生体验
- 📥 免费下载自 gitify.io，支持 Homebrew 安装
- 🛠️ 开源 MIT 许可，接受社区贡献

---

### [发布 v6.8.0 · verdaccio/verdaccio · GitHub](https://github.com/verdaccio/verdaccio/releases/tag/v6.8.0)

**原文标题**: [Release v6.8.0 · verdaccio/verdaccio · GitHub](https://github.com/verdaccio/verdaccio/releases/tag/v6.8.0)

Verdaccio v6.8.0 发布，包含多项功能增强与错误修复。

- 📢 新增取消发布通知钩子：当包被完全删除或单个版本被移除时，webhook 会触发通知，并通过 `{{ publishType }}` 和 `{{ publishedPackage }}` 变量区分事件类型。
- 🔒 修复上游 403 错误传递：当上游注册表返回 403 时，现在会正确传递给客户端，而非返回通用 500 错误，帮助区分授权失败。
- ⚡ 优化 npm 搜索 v1 端点：添加速率限制，限制 `size`（最大 250）和 `from`（最大 10000）参数，并提前停止权限检查，防止无限制的全量扫描。
- 🛠️ 修复 tarball 上游选择：现在根据 tarball URL 匹配上游，而非依赖包模式，解决多上游配置下的下载失败问题。
- 🗂️ 修复缺失的 distfile 记录：当缓存版本缺少 `_distfiles` 记录时，从 `dist.tarball` 元数据恢复位置，避免永久返回 404。
- 🎨 更新 UI 主题：`@verdaccio/ui-theme` 升级至 `9.0.0-next-9.21`，提升界面体验。
- 🧹 重构 ESLint 配置：优化代码质量工具链。

---

### [GitHub - piscinajs/piscina: 一个快速、高效的 Node.js 工作线程池实现 · GitHub](https://github.com/piscinajs/piscina)

**原文标题**: [GitHub - piscinajs/piscina: A fast, efficient Node.js Worker Thread Pool implementation · GitHub](https://github.com/piscinajs/piscina)

Piscina 是一个高性能的 Node.js 工作线程池库，支持多种任务调度、灵活的线程管理和丰富的功能特性。

- ⚡ 支持线程间快速通信，适用于固定任务和可变任务场景
- 🔧 提供灵活的线程池大小配置，支持最小/最大线程数限制
- 📊 内置运行时间和等待时间统计，包含平均值、百分位数等详细指标
- 🛑 支持任务取消，可通过 AbortController 或 EventEmitter 实现
- 🧩 兼容 CommonJS、ESM 和 TypeScript，支持多函数导出
- 🗂️ 提供自定义任务队列接口，内置高性能 FixedQueue 实现
- 🖥️ 支持 Linux 线程优先级设置（需安装 @napi-rs/nice 模块）
- 🔄 支持背压控制，通过 maxQueue 和 drain 事件管理任务流
- 📡 支持 BroadcastChannel 实现主线程与工作线程的广播通信
- 🛡️ 提供资源限制功能，可设置内存、栈大小等限制
- 🧹 支持优雅关闭（close）和强制销毁（destroy）两种停止方式
- 📈 提供利用率计算，帮助评估线程池的负载情况

---

### [发布 7.9.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.9.0)

**原文标题**: [Release 7.9.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.9.0)

Prisma 7.9.0 稳定版发布，带来多项新功能、改进和错误修复。

- 🎉 **CLI 标签补全**：支持 bash、zsh、fish 和 PowerShell 的 shell 标签补全，通过 `@bomb.sh/tab` 集成，简化命令输入。
- 🤖 **AI 代理支持**：`prisma init` 自动安装技能目录，增强 AI 代理（如 Claude Code、Cursor）的兼容性，并添加安全检查防止破坏性操作。
- 🛡️ **安全改进**：扩展 AI 代理检测范围，为 `db push --accept-data-loss` 添加防护，从 `prisma mcp` 服务器移除 `migrate-reset` 工具。
- 🐛 **Prisma Client 修复**：修复 TypeScript 性能回归、`XOR` 类型验证、`Date` 序列化错误、文档注释转义问题，以及交互式事务超时导致的连接泄漏。
- 🔧 **CLI 修复**：修复 `prisma validate` 在符号链接循环中的挂起问题，以及 Windows 上引擎二进制缓存路径的稳定性。
- 🗄️ **驱动适配器修复**：修复 `Bytes` 列读取的弃用警告、PostgreSQL 列名解析、SQL Server 空值错误等。
- 📋 **Schema 引擎修复**：修复 `prisma migrate status` 对回滚迁移的报告错误，以及 PostgreSQL 主键约束重命名问题。
- 🖥️ **Prisma Studio 更新**：从 0.27.3 升级到 0.33.0，新增迁移历史视图、Prisma Streams 浏览器、SQL 模式感知功能。
- ☁️ **Prisma Compute 公测**：推出托管服务，支持 TypeScript 应用部署在数据库旁，提供无冷启动、分支环境和自定义域名。
- 🤝 **企业支持**：提供企业支持计划，包括优先问题处理、性能优化和定制培训。
- 🙏 **社区贡献**：感谢多位贡献者（如 @AmirSa12、@kyungseopk1m 等）的修复和功能。

---

### [API、AI 和 MCP 的统一网关 - Zuplo](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

**原文标题**: [The Unified Gateway for APIs, AI, and MCP - Zuplo](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

Zuplo 是一个统一的 API、LLM 和 MCP 网关，提供安全、治理和变现功能，可在几分钟内上线。

- 🔒 **统一网关**：为出站（应用调用 LLM）和入站（AI 代理调用你的 API）流量提供单一可编程策略引擎，支持认证、速率限制、预算和审计。
- 💰 **成本控制**：动态速率限制和按团队预算上限可防止成本激增，例如在 14 天内节省了 42,900 美元，总支出降低 41%。
- 🛡️ **安全与治理**：在网关层阻止恶意流量，包括认证失败、速率限制、无效模式和提示注入攻击，本周已阻止 12,400 次请求。
- 📊 **可见性**：每次 API、LLM 和 MCP 调用都记录并归因于消费者，支持实时仪表盘和导出到 Datadog 或 SIEM。
- 💳 **变现**：内置计费功能，支持按请求、令牌或单位计量，并与 Stripe 集成，例如 6 月产生 30,000 美元收入，环比增长 12%。
- 🚀 **快速部署**：通过简单的配置（如 OpenAI SDK 的 base URL 替换或 OpenAPI 扩展）即可在几分钟内上线，支持 Claude、Cursor、Codex 和 ChatGPT 等代理。
- 📈 **实际成果**：客户报告硬件占用减少 90%，成本节省超过 70%，并在几小时内启动 MCP 服务器。
- ❓ **常见问题**：提供关于统一网关、AI 网关、MCP 网关以及是否需要替换现有网关的直接答案，免费套餐包括每月 100,000 次请求。

---

