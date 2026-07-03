### [node/doc/contributing/first-contributions.md 位于主分支 · nodejs/node · GitHub](https://github.com/nodejs/node/blob/main/doc/contributing/first-contributions.md)

**原文标题**: [node/doc/contributing/first-contributions.md at main · nodejs/node · GitHub](https://github.com/nodejs/node/blob/main/doc/contributing/first-contributions.md)

本指南為首次貢獻者提供 Node.js 專案的貢獻流程說明，涵蓋從問題處理到合併請求的完整步驟。

- 📋 **入門建議**：先閱讀行為準則，並從標記為"good first issue"的簡單問題開始，避免一開始就處理複雜或大型的貢獻。
- 💬 **有效溝通**：無需請求指派任務，透過留言更新進度即可；避免同時接手多個問題，並注意留言長度以維持討論可讀性。
- ⚠️ **新手應避免**：不要自動化貢獻、提交大型合併請求，或在第一個 PR 尚未核准前就開啟新的 PR。
- 🔄 **PR 審查流程**：提交 PR 前需簽署開發者來源認證（DCO），並熟悉審查過程中的更新與回饋處理方式。
- ❓ **常見問題解答**：若 PR 未獲關注，可適時提醒相關貢獻者或至 Slack 頻道求助；更新 PR 後需重新取得核准。
- 🛠️ **處理合併衝突**：需手動重新基底分支並解決衝突，避免使用 GitHub 網頁介面處理。
- ✅ **CI 檢查流程**：首次 PR 需由貢獻者核准工作流程；Jenkins CI 需由具權限者手動觸發，請耐心等待志願者協助。
- 📅 **版本發布時程**：非重大變更通常先進入 Current 版本，兩週後可納入 LTS 版本；重大變更需等待下一個主要版本發布。
- 🔙 **回溯處理**：若變更無法乾淨回溯至發布分支，需自行開啟回溯 PR 以確保納入版本發布。

---

### [GitHub - Agent-Field/SWE-AF: 自主软件工程 AI 智能体舰队，在 AgentField 上实现生产级 PR：规划、编码、测试与交付。](https://github.com/Agent-Field/SWE-AF)

**原文标题**: [GitHub - Agent-Field/SWE-AF: Autonomous software engineering fleet of AI agents for production-grade PRs on AgentField: plan, code, test, and ship. · GitHub](https://github.com/Agent-Field/SWE-AF)

SWE-AF 是一个基于 AgentField 构建的全自主软件工程团队运行时，只需一次 API 调用即可启动完整的工程团队，从规划到代码再到交付，端到端完成复杂软件项目。

- 🤖 **一次调用，全栈交付** — 只需一个 API 请求即可启动产品经理、架构师、程序员、审查员和测试员组成的完整团队，自动完成从目标到代码的整个流程。
- 🏭 **工厂式架构** — 采用三层嵌套控制循环（内层/中层/外层），根据任务难度实时调整策略，而非简单重试。
- 🔄 **多模式运行** — 支持单仓库和多仓库模式，可协调主应用与共享库、微服务等跨代码库的变更。
- 🎯 **卓越性能** — 在基准测试中以 Claude haiku 和 MiniMax M2.5 均获得 95/100 分，远超 Claude Code Sonnet (73) 和 Codex o3 (62)。
- 💰 **成本高效** — 使用 MiniMax M2.5 运行时仅需约 $6，即可完成高质量构建，成本仅为同类方案的 30%。
- 🧠 **持续学习** — 开启 `enable_learning` 后，早期发现的约定和失败模式会自动注入后续问题处理中。
- ⚡ **并行执行** — 依赖级别调度配合隔离的 git 工作树，支持大规模并行处理，单次构建可调度数百至数千个智能体。
- 🔧 **多模型支持** — 支持 Claude、OpenRouter、OpenAI 和 Google 等多种模型，可为不同角色分配不同模型。
- 🛡 **弹性恢复** — 检查点机制支持在崩溃或中断后恢复构建，确保长期运行的可靠性。
- 📊 **透明审计** — 提供完整的工件追踪（规划、执行、验证），并支持 PR 后的 CI 门控自动修复。

---

### [GitHub - lirantal/nodejs-cli-apps-best-practices: 最大的 Node.js CLI 应用最佳实践清单 ✨](https://github.com/lirantal/nodejs-cli-apps-best-practices)

**原文标题**: [GitHub - lirantal/nodejs-cli-apps-best-practices: The largest Node.js CLI Apps best practices list ✨ · GitHub](https://github.com/lirantal/nodejs-cli-apps-best-practices)

一个关于构建成功、人性化且用户友好的 Node.js 命令行应用程序的最佳实践集合。

- 🤖 该指南包含 37 个最佳实践，涵盖命令行体验、分发、互操作性、可访问性、测试、错误处理、开发、分析、版本控制和安全性等多个方面。
- 🎨 强调构建富有同理心的 CLI，包括尊重 POSIX 参数、提供彩色体验、丰富的交互（如进度条和下拉菜单）以及超链接。
- 📦 在分发方面，建议优先选择较小的依赖包、使用 shrinkwrap 锁定依赖版本，并在卸载时清理配置文件。
- 🔗 确保互操作性，包括接受 STDIN 输入、支持结构化输出（如 JSON）、遵循跨平台规范以及支持配置优先级。
- ♿ 提升可访问性，例如将 CLI 容器化、提供优雅降级（如支持 `--json` 参数）、兼容 Node.js 版本以及使用 `#!/usr/bin/env node` 自动检测运行时。
- 🧪 测试时不要信任本地化设置，以避免因系统语言不同导致的测试失败。
- 🚨 错误处理应提供可追踪的错误码、可操作的修复建议、调试模式、正确的退出码，并简化错误报告流程。
- 🛠️ 开发时使用 `bin` 对象解耦可执行文件名、使用相对路径（`process.cwd()` 和 `__dirname`）以及通过 `files` 字段精简发布包。
- 📊 分析功能必须严格采用用户主动选择加入（Opt-in）的方式，并明确告知数据收集范围。
- 🏷️ 版本管理需包含 `--version` 标志、遵循语义化版本控制、在 `package.json` 中记录版本信息、在错误消息中显示版本、保持向后兼容性、发布版本化 npm 包并提供更新日志。
- 🔒 安全方面需最小化参数注入风险，避免将敏感系统操作暴露给命令行参数。

---

### [GitHub - lirantal/nodejs-cli-apps-best-practices: 最大的 Node.js CLI 应用最佳实践清单 ✨](https://github.com/lirantal/nodejs-cli-apps-best-practices#111-cli-frameworks-table)

**原文标题**: [GitHub - lirantal/nodejs-cli-apps-best-practices: The largest Node.js CLI Apps best practices list ✨ · GitHub](https://github.com/lirantal/nodejs-cli-apps-best-practices#111-cli-frameworks-table)

该指南提供了构建成功、富有同理心且用户友好的 Node.js 命令行应用的最佳实践集合。

- 📚 **概述**：一个精心策划的最佳实践集合，旨在帮助开发者构建成功、富有同理心且用户友好的 Node.js 命令行应用，优化用户体验。
- 🤖 **AI 就绪**：包含 SKILL.md 文件，为 AI 代理提供支持。
- ✅ **37 项最佳实践**：涵盖命令行体验、分发、互操作性、可访问性、测试、错误处理、开发、分析、版本控制和安全性等关键领域。
- 🌍 **多语言支持**：提供中文、西班牙文等多语言版本，并欢迎社区贡献翻译。
- 👤 **作者背景**：由 Liran Tal 创建，他是一位热衷于构建命令行应用的开发者，并贡献了多个开源项目。
- ✨ **核心团队**：感谢多位贡献者，包括翻译、写作和开发支持。
- 📑 **详细目录**：指南结构清晰，包含 12 个主要章节，每个章节下细分具体实践，方便查阅。
- 🖥️ **命令行体验**：强调遵循 POSIX 标准、构建同理心 CLI、提供彩色输出、丰富交互和超链接，以及支持零配置。
- 📦 **分发与打包**：建议减少依赖体积、使用 shrinkwrap 锁定版本，并在卸载时清理配置文件。
- 🔗 **互操作性**：支持 STDIN 输入、结构化输出、跨平台兼容，并遵循配置优先级规则。
- ♿ **可访问性**：通过容器化、优雅降级、兼容 Node.js 版本和自动检测运行时，确保 CLI 的广泛可用性。
- 🧪 **测试与错误**：测试时不信任区域设置，提供可追踪、可操作的错误信息，支持调试模式，并合理使用退出码。
- 🛠️ **开发与维护**：使用 bin 对象、相对路径和 files 字段优化项目结构。
- 📊 **分析与版本控制**：严格采用选择加入的分析方式，并遵循语义化版本控制，提供清晰的版本信息。
- 🔒 **安全性**：最小化参数注入风险，避免敏感系统操作被利用。
- 📖 **附录资源**：提供 CLI 框架表格和教育资源链接，帮助开发者进一步学习。

---

### [获取失败](https://github.com/lirantal/nodejs-cli-apps-best-practices/blob/main/skills/nodejs-cli-best-practices/SKILL.md)

**原文标题**: [Failed to retrieve](https://github.com/lirantal/nodejs-cli-apps-best-practices/blob/main/skills/nodejs-cli-best-practices/SKILL.md)

无法总结：获取内容失败，状态码 429。

---

### [Nub — Node.js 的一体化工具包](https://nubjs.com/)

**原文标题**: [Nub — an all-in-one toolkit for Node.js](https://nubjs.com/)

Nub 是一个为 Node.js 设计的全合一 JavaScript 工具包，它通过增强而非替代 Node.js 来提升开发体验。它提供 TypeScript 优先的工具链，支持运行 TypeScript 文件、脚本和本地 CLI，且无需新的运行时或锁定。

- 🚀 **TypeScript 优先**：直接运行 `.ts`、`.tsx` 和 `.jsx` 文件，支持 `tsconfig.json`、`.env` 加载和现代语法，无需额外配置。
- ⚡ **高性能**：使用 Rust 和 oxc 进行内存转译，启动速度与原生 Node.js 相当，比 tsx 快 2.9 倍，脚本运行比 pnpm run 快 24 倍。
- 🔧 **全合一工具链**：一个 Rust 二进制文件即可运行文件、脚本、管理依赖和 Node 版本，替代 tsx、ts-node、nvm 等多个工具。
- 📦 **包管理器兼容**：支持 pnpm、npm 和 bun 的锁文件，安装速度比 pnpm 快 2.5 倍，且内置供应链攻击防护。
- 🛡️ **安全默认**：默认拒绝构建脚本，查询 OSV 恶意包建议，并防止信任降级，确保依赖安全。
- 🔄 **零锁定**：无 Nub 特定 API，代码在原生 Node.js 上运行，兼容所有 Node 标志和选项，可无缝替换 `node`。
- 👀 **依赖感知监视模式**：自动重启更改的文件，支持 TypeScript 源映射，并监视 `package.json`、tsconfig 和 `.env` 文件。
- 🌐 **现代 API 支持**：自动填充 Temporal、Worker 等 API，并解锁实验性 Node.js 功能，如 WebSocket 和 `using` 语法。

---

### [发布 v0.2.0 · nubjs/nub · GitHub](https://github.com/nubjs/nub/releases/tag/v0.2.0)

**原文标题**: [Release v0.2.0 · nubjs/nub · GitHub](https://github.com/nubjs/nub/releases/tag/v0.2.0)

nub 项目发布 v0.2.0 版本，主要新增了 Web Worker 支持并增强了包管理器兼容性。

- 🛠️ 新增 Web Worker 支持：在 Node 中实现浏览器标准的 `Worker` 构造函数，支持 TypeScript/JSX 直接运行、内联 Worker、`MessageEvent` 和 `Transferables` 等特性。
- 📦 包管理器兼容性改进：修复了 yarn-berry 目录解析、pnpm 工作空间版本锁定和凭证泄漏等问题。
- 🐳 工具与分发更新：推出官方 Docker 镜像（基于 Node 26 slim 和 Alpine）、Homebrew 自动更新，并优化了构建配置。
- 📚 文档完善：添加了 Node 版本/层级表、Homebrew 安装路径和 Docker 镜像链接。
- 🧪 测试与内部改进：新增 WPT Worker 一致性测试、Node 版本矩阵测试，并修复了多个 CI 和构建错误。

---

### [npm 为高影响力账户添加预防性账户保护 - GitHub 更新日志](https://github.blog/changelog/2026-06-25-npm-adds-preventive-account-protection-for-high-impact-accounts/)

**原文标题**: [npm adds preventive account protection for high-impact accounts - GitHub Changelog](https://github.blog/changelog/2026-06-25-npm-adds-preventive-account-protection-for-high-impact-accounts/)

npm 为高影响力账户新增预防性保护措施
- 🔒 当高影响力账户（管理最常用包的账户）发生敏感变更（如修改邮箱或使用 2FA 恢复码）时，自动进入 72 小时只读状态
- 📧 系统会向账户原邮箱发送警报，阻断攻击者通过篡改邮箱、生成令牌并发布恶意版本的攻击路径
- ✅ 只读期间仍可安装下载包、查看组织和团队、浏览账户及包设置
- 🚫 暂停发布、管理令牌、修改包可见性、变更组织/团队成员等可能影响注册表或账户安全的操作
- ⏳ 72 小时后自动恢复完全访问权限，无需手动确认，依赖包始终保持可用
- 🆘 如账户意外受影响或需协助，可联系 npm 支持

---

### [发布 v11.18.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.18.0)

**原文标题**: [Release v11.18.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.18.0)

npm CLI v11.18.0 版本发布，主要引入了链接安装策略的稳定化、多项功能增强和错误修复，并更新了多个依赖项。

- 🎉 **链接安装策略正式稳定**：将链接安装策略从实验性功能升级为稳定版，并扩展了替换注册表主机的 URL 前缀匹配功能。
- 🛠️ **安装脚本管理优化**：新增`install-scripts`命令命名空间，并自动清理未使用的`allowScripts`条目，提升脚本管理效率。
- 🔒 **审计与安全增强**：当最小发布年龄阻止审计修复时发出警告，并加强了`allowScripts`的执行漏洞修复。
- 🐛 **多项错误修复**：修复了 SBOM 生成中的 URL 编码问题、`npm token list`参数输出、链接策略下的工作区依赖标记等大量 bug。
- 📚 **文档更新**：建议使用`install-strategy=linked`来捕获幽灵依赖，提升项目依赖可见性。
- ⬆️ **依赖项升级**：更新了`undici`、`brace-expansion`、`tar`、`semver`和`npm-profile`等多个核心依赖库。
- 🔧 **工作区组件更新**：`@npmcli/arborist`、`@npmcli/config`、`libnpmexec`等子包均同步更新至对应新版本。

---

### [配置 | npm 文档](https://docs.npmjs.com/cli/v11/using-npm/config/#install-strategy)

**原文标题**: [Config | npm Docs](https://docs.npmjs.com/cli/v11/using-npm/config/#install-strategy)

npm 配置文件详细说明了 npm 获取配置值的来源、优先级、简写方式以及所有可用的配置项。

- 📋 **配置来源优先级**：命令行标志 > 环境变量 > npmrc 文件（项目级 > 用户级 > 全局级 > 内置）
- 🔧 **命令行标志**：使用 `--foo bar` 格式设置配置，`--flag` 无值则设为 `true`，`--` 停止解析标志
- 🌐 **环境变量**：以 `npm_config_` 开头的变量会被解析为配置参数，下划线代替短横线
- 📁 **npmrc 文件**：包括项目级 (`/path/to/project/.npmrc`)、用户级 (`~/.npmrc`)、全局级 (`$PREFIX/etc/npmrc`) 和内置配置文件
- ⚡ **常用简写**：`-g` 表示 `--global`，`-D` 表示 `--save-dev`，`-f` 表示 `--force`，`-y` 表示 `--yes`
- 🔐 **认证与安全**：支持 `_auth`、`auth-type`、`otp`、`ca`、`strict-ssl` 等安全配置
- 📦 **包管理**：`access` 控制作用域包可见性，`registry` 设置注册表 URL，`tag` 指定安装标签
- 🛠️ **安装策略**：`install-strategy` 支持 hoisted（默认）、nested、shallow、linked 四种模式
- ⏱️ **版本控制**：`before` 和 `min-release-age` 限制安装特定日期前的版本，`allow-same-version` 允许相同版本
- 🚫 **依赖限制**：`allow-directory`、`allow-file`、`allow-git`、`allow-remote` 控制不同类型依赖的安装
- 📊 **输出格式**：`json` 输出 JSON 数据，`parseable` 输出可解析格式，`long` 显示扩展信息
- 🔄 **已弃用配置**：`global-style` 改为 `--install-strategy=shallow`，`only` 改为 `--omit=dev` 等

---

### [为什么 Drizzle ORM 一个月无法在 NPM 上发布新版本 | vlt /vōlt/](https://www.vlt.io/blog/packument-size-limits)

**原文标题**: [Why Drizzle ORM couldn't publish new releases on NPM for a month | vlt /vōlt/](https://www.vlt.io/blog/packument-size-limits)

### 概述总结
Drizzle ORM 因 NPM 的 100 MB 包文档限制，一个月无法发布新版本，最终通过删除旧版本解决。该限制源于 NPM 的包文档机制，每次发布都会累积所有版本的元数据，导致体积膨胀。项目可通过避免发布开发版、监控包文档大小等方式预防此问题。

- 📦 **NPM 限制**：包文档（packument）上限为 100 MB（未压缩），包含所有版本的元数据，超过后无法发布新版本。
- 🚫 **触发原因**：Drizzle ORM 每个版本约 131 KB，发布 763 次即达上限；自动发布快照版本加速了问题出现。
- 🔧 **解决方案**：联系 NPM 支持团队手动删除旧版本（因 72 小时后无法自行删除），最终包文档降至 61 MB。
- ⚠️ **风险检查**：使用命令 `curl -s https://registry.npmjs.org/<包名> | wc -c` 可查看当前包文档大小。
- 💡 **预防措施**：避免发布开发版快照；使用替代注册表（如私有注册表）；监控包文档大小并提前清理。
- 🛠 **改进方向**：建议 NPM 支持按版本范围查询，减少客户端下载量；部分镜像（如私有注册表）通过白名单机制大幅压缩包文档（如 Drizzle 仅 1.7 MB）。

---

### [Drizzle ORM - 下一代 TypeScript ORM](https://orm.drizzle.team/)

**原文标题**: [Drizzle ORM - next gen TypeScript ORM.](https://orm.drizzle.team/)

Drizzle ORM 是一个快速、支持 TypeScript 和 JavaScript 的 ORM，支持多种数据库和运行时环境，并提供强大的查询构建、迁移管理和数据操作功能。

- 🚀 **高性能**：在基准测试中，Drizzle 的查询和连接延迟极低，CPU 负载小，请求处理能力远超 Prisma。
- 🗄️ **多数据库支持**：支持 PostgreSQL、MySQL、SQLite、SingleStore、MSSQL、CockroachDB 等主流数据库，以及 PlanetScale、Neon、Supabase 等云服务。
- 🌐 **多运行时兼容**：可在 Node.js、Bun、Deno、Cloudflare Workers、Vercel Functions、React Native 等环境中运行。
- 🛠️ **完整工具链**：提供 `drizzle-kit` 用于迁移管理（生成、推送、拉取、导出等），以及 `drizzle-seed` 用于数据填充。
- 🎨 **灵活查询**：支持关系查询（RQB v2）、动态查询、事务、批量操作、缓存层、行级安全（RLS）等高级特性。
- 🔌 **丰富集成**：内置 Zod、Valibot、TypeBox、ArkType 等验证库支持，并提供 ESLint 插件和 GraphQL 扩展。
- 🖥️ **Drizzle Studio**：可视化数据浏览器，支持表/视图创建、数据编辑、SQL 控制台、CSV 导入导出等。
- 🔄 **持续更新**：从 v0.23 到 v1.0 Beta，不断修复 Bug、添加新功能（如 Gel 方言、MSSQL 支持、性能优化等）。
- 💬 **社区活跃**：拥有活跃的 Discord、Twitter 社区，并获得众多开发者认可（尽管也有吐槽）。
- 🆓 **开源免费**：Drizzle 是免费且开源的，可通过 GitHub Star、赞助等方式支持。

---

### [使用 TypeScript 7 更快迭代](https://code.visualstudio.com/blogs/2026/06/26/iterating-faster-with-ts-7)

**原文标题**: [Iterating faster with TypeScript 7](https://code.visualstudio.com/blogs/2026/06/26/iterating-faster-with-ts-7)

### 概述总结
VS Code 团队通过渐进式迁移策略成功采用 TypeScript 7，将类型检查速度提升 7 倍，整体构建时间缩短 4 倍，同时为 TypeScript 团队提供了宝贵的真实世界反馈。

- 🚀 **性能飞跃**：TypeScript 7 在 Go 中重写，类型检查速度提升 7 倍（从 36 秒降至 5 秒），`npm run watch`从 80 秒降至 20 秒。
- 🧩 **渐进式迁移**：分 6 个阶段逐步引入，从低风险扩展开始，最终覆盖整个 VS Code 代码库，避免了大版本切换的风险。
- 🔄 **并行验证**：同时运行 TS 6 和 TS 7 的 CI 检查，确保类型检查一致性，并优先修复导致开发者回退的格式问题。
- 🛠️ **构建简化**：迁移后统一使用`tsgo`（TS 7）进行类型检查和开发构建，用 esbuild 替代 webpack，简化了工具链。
- 🎯 **早期反馈**：通过每日更新的`native-preview`包和内置报告机制，为 TypeScript 团队提供了持续的真实世界 bug 反馈。
- 📊 **显著收益**：编辑器语言工具加载时间从近 1 分钟降至 10 秒，大幅提升开发者日常迭代效率。
- 🤝 **协作共赢**：VS Code 的复杂代码库成为 TypeScript 7 的优质测试场，帮助打磨出更稳定的最终版本。

---

### [用不到 50 行代码实现你自己的文件路由 | Wasp](https://wasp.sh/blog/2026/07/01/roll-your-own-file-based-router)

**原文标题**: [Roll your own file-based router in under 50 lines of code | Wasp](https://wasp.sh/blog/2026/07/01/roll-your-own-file-based-router)

本文介绍了如何在 Wasp 框架中用不到 50 行代码实现自定义的基于文件的路由系统，强调显式与可编程性。

- 🧩 **核心思想**：Wasp 的 Spec 是可编程的 Node.js 程序，而非静态配置，允许用户通过代码动态生成路由。
- 📂 **文件路由实现**：通过`globSync`扫描`page.tsx`文件，将文件夹路径映射为 URL 路径，并用`pascalCase`生成路由名称。
- 🔧 **自定义约定**：支持路由分组（如`(marketing)`）、权限控制（`(auth)`）、预渲染（`(prerender)`）等自定义规则，仅需简单代码过滤。
- 🚀 **动态与可选段**：通过方括号语法（如`[productId]`）支持动态参数和可选参数，完全由用户定义。
- 🔗 **类型安全**：生成的路由自动获得 TypeScript 类型检查，`<Link>`组件支持自动补全和类型错误提示。
- 🛠️ **扩展性**：不仅限于路由，还可通过相同方式生成 API、查询、任务等 Spec 对象，实现全栈模块化。
- 💡 **哲学**：Wasp 拒绝隐式魔法，通过显式可编程 Spec 让用户掌控框架行为，同时保留框架的完整功能。

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

Wasp 是一个专为 AI 时代设计的全栈 TypeScript 框架，集成了 React、Node.js 和 Prisma，内置认证、任务和部署功能，让开发者一天内即可交付应用并完全掌控代码。

- 🚀 **一键启动全栈应用**：通过 `npm i -g @wasp.sh/wasp-cli@latest` 快速安装，使用 `wasp new` 创建新项目，`wasp start` 同时运行前后端开发服务器。
- 🔐 **内置完整认证系统**：支持邮箱、Google、GitHub 等多种登录方式，提供现成的登录/注册表单，并可自定义 UI。
- 🗄️ **集成 Prisma 数据模型**：在 `schema.prisma` 中声明模型，自动生成类型安全的前后端代码，支持数据库迁移和可视化。
- 📡 **类型安全的 RPC 通信**：在服务器定义函数，客户端直接调用，无需 REST 或 GraphQL，基于 TanStack Query 实现自动缓存和响应式更新。
- ⏰ **后台任务开箱即用**：支持定时任务（Cron）、一次性任务和重试机制，无需外部服务，通过 `PgBoss` 执行。
- 📧 **邮件发送集成**：支持 SendGrid、Mailgun、SMTP 等提供商，提供统一 API，自动用于认证流程。
- 🔌 **WebSocket 实时通信**：基于 Socket.IO 实现类型安全的双向通信，支持聊天、通知等实时功能。
- 📄 **静态渲染优化**：通过 `prerender: true` 开启 SSG，提升 SEO 和 LLM 兼容性，适合静态内容页面。
- 🌐 **一键部署到任意平台**：支持 Fly.io、Railway 等托管服务，也可生成 Dockerfile 自行部署，无供应商锁定。
- 🔗 **类型安全的路由链接**：自动生成类型化的 `Link` 组件和 `routes` 对象，编译时检查路径和参数错误。
- 🛠️ **自定义 HTTP API**：基于 ExpressJS 定义 REST 接口，自动集成认证和实体访问。
- 🤖 **AI 友好设计**：高抽象级别减少代码量，清晰结构降低错误率，节省 AI 上下文 token，提供官方 AI 工具（规则文件、技能、插件）。
- 🧅 **洋葱架构哲学**：提供从高层 API（覆盖 80% 用例）到底层控制的渐进式灵活性，让开发者按需选择复杂度。
- 📚 **丰富的示例应用**：包括 Todo App、CoverLetterGPT、Waspello 等参考实现，可学习、复刻或直接部署。

---

### [使用 AI 驱动的堆快照分析在几分钟内调试 Node.js 内存泄漏](https://nodesource.com/blog/debug-nodejs-memory-leak-ai-heap-snapshot-analysis)

**原文标题**: [Debug a Node.js Memory Leak in Minutes with AI-Powered Heap Snapshot Analysis](https://nodesource.com/blog/debug-nodejs-memory-leak-ai-heap-snapshot-analysis)

本文介绍了如何使用 N|Solid 扩展在 VS Code 等编辑器中，通过 AI 驱动的堆快照分析，快速定位并修复 Node.js 内存泄漏问题。

- 🧠 **问题描述**：内存泄漏是生产环境中最令人头疼的问题之一，表现为内存持续增长、GC 频繁、性能下降甚至进程崩溃。
- 🔍 **检测方法**：通过 N|Solid 扩展在编辑器中直接观察运行时内存指标，无需切换外部仪表盘，发现内存持续上升。
- 📸 **堆快照捕获**：直接捕获堆快照，AI 自动分析内存图，快速识别出模块级数组 `leak` 是泄漏根源。
- 🎯 **根因定位**：AI 报告指出 `leak.push(JSON.parse(resp))` 导致对象被永久保留，并重建了保留路径：GC 根 → http.Server → requestListener → 模块作用域 → leak。
- 🛠️ **修复方案**：移除不必要的数组保留，修正后的代码不再存储请求对象，让 GC 能正常回收内存。
- ✅ **验证修复**：部署修复后再次捕获堆快照，AI 分析确认无活动泄漏，无增长的对象集合，泄漏模式消失。
- 💡 **核心价值**：将生产调试工作流整合到编辑器中，减少上下文切换，缩短从发现问题到理解修复的时间。
- 🎬 **完整演示**：提供视频链接展示从泄漏检测到根因分析再到验证的完整流程。
- 🚀 **开始使用**：N|Solid 扩展支持 VS Code、Cursor、Windsurf 和 Antigravity，可直接从编辑器调试生产问题。

---

### [GitHub - romgrk/node-gtk: NodeJS 的 GTK 绑定 · GitHub](https://github.com/romgrk/node-gtk)

**原文标题**: [GitHub - romgrk/node-gtk: GTK bindings for NodeJS · GitHub](https://github.com/romgrk/node-gtk)

node-gtk 是一个为 Node.js 提供 GTK 绑定，支持在 Linux、macOS 和 Windows 上构建原生 GTK 应用的项目，拥有 562 颗星和 42 个复刻，支持 ESM、TypeScript 和 CSS 热重载。

- 🚀 **快速启动**：通过 `npx node-gtk create <your-app>` 命令即可生成完整项目，并支持 GTK4/Adwaita 应用开发。
- 📦 **安装简便**：Linux 用户需安装 GTK4 和 libadwaita；macOS 用户通过 Homebrew 安装；Windows 用户可直接使用预构建库。
- 🌐 **跨平台支持**：提供预构建二进制文件，适用于 Node.js 22、24 和 26 版本，覆盖三大操作系统。
- 📚 **丰富示例**：包含 hello world、网页浏览器和系统监视器等示例，帮助快速上手。
- 🛠️ **技术基础**：基于 gobject-introspection 库，类似于 GJS 或 PyGObject，支持任何内省的 C 库。
- 📜 **开源许可**：采用 MIT 许可证，拥有 1,377 次提交和 36 个发布标签，社区活跃。

---

### [GTK 项目 - 一个自由开源的跨平台控件工具包](https://www.gtk.org/)

**原文标题**: [The GTK Project - A free and open-source cross-platform widget toolkit](https://www.gtk.org/)

GTK 是一个功能全面、跨平台的开源 UI 工具包，旨在帮助开发者创建用户喜爱的应用程序，支持多种编程语言，并拥有活跃的社区。

- 🎨 提供完整的 UI 元素集合，适用于从小工具到完整应用套件的各种项目。
- 🌐 支持 Linux、Windows、MacOS 等多个操作系统，具备良好的可移植性。
- 🗣️ 通过语言绑定支持 C、JavaScript、Perl、Python、Rust、Vala 等多种编程语言。
- 📦 提供稳定版（4.22.4）和旧稳定版（3.24.52）下载，以及最新的不稳定版（4.23.2）。
- 🛠️ 拥有丰富的核心控件（如按钮、窗口、工具栏）和易于使用的 API，可缩短开发时间。
- 🔓 基于 LGPL 许可证的开源项目，由 GNOME 和社区维护。
- 🧩 构建在 GLib 之上，提供基础数据类型和系统集成点，避免代码重复。
- 🌟 支持原生外观、主题和面向对象方法，满足现代开发者需求。
- 🤝 社区活跃，可通过 Discourse、Matrix、博客和 Mastodon 获取帮助和更新。
- 🚀 鼓励开发者贡献代码，参与 bug 修复和功能开发，并定期举办会议和黑客松。

---

### [xyOps - 开放工作流自动化](https://xyops.io/)

**原文标题**: [xyOps - Open Workflow Automation](https://xyops.io/)

xyOps™ 是一款集作业调度、监控、告警和工单系统于一体的下一代工作流自动化平台，支持可视化构建、灵活扩展，并采用 BSD 开源许可。

- 🧩 **可视化工作流构建**：通过图形化编辑器连接事件、触发器、动作和监控，支持条件逻辑、文件传递和并行执行。
- ⏰ **灵活作业调度**：支持单次或重复作业、黑名单时段、crontab 导入，以及基于插件的调度扩展。
- 📊 **实时作业追踪**：并行运行作业，实时更新进度与剩余时间，可设置 CPU/内存限制，并基于结果执行自定义操作。
- 🖥️ **服务器监控**：提供服务器和组级仪表盘，支持自定义监控指标（CPU、内存、网络等），并生成历史性能图表。
- 🚨 **智能告警**：支持灵活触发规则，通过邮件、Webhook 或自定义通知发送告警，可自动创建工单或阻止新作业启动。
- 🎫 **集成工单系统**：内置工单管理，支持告警自动生成工单、附件上传及 CI/CD 集成，可通过 API 完全脚本化。
- 🌐 **多语言插件支持**：基于 JSON/STDIO 的简单 API，无需 SDK，支持所有编程语言，并可发布到插件市场。
- 📦 **插件市场**：提供官方及社区插件（如 Atlassian、AWS S3、Discord、GitHub 等），支持 MCP 服务器集成。
- 🔁 **高可用与扩展**：支持热备份故障转移，无作业中断，可扩展至数千台服务器，支持 macOS、Linux 和 Windows 代理。
- 🆓 **开源许可**：100% 免费开源，采用 BSD 3-Clause 许可，所有功能永久开源，专业和企业支持计划另售。
- 💰 **定价方案**：免费版（自托管，社区支持）、专业版（$167/月，含专业支持与工单系统）、企业版（$834/月，含 SSO、离线安装、1 小时响应），支持自定义发票付款。
- 🚀 **即将发布**：可注册邮件通知，获取上线提醒。

---

### [AI SDK 7 现已发布 - Vercel](https://vercel.com/blog/ai-sdk-7)

**原文标题**: [AI SDK 7 is now available - Vercel](https://vercel.com/blog/ai-sdk-7)

AI SDK 7 每周下载量超过 1600 万次，是构建 AI 应用的 TypeScript SDK，支持多种模型提供商。它也是 Vercel 开源代理框架的基础。AI SDK 7 在五个方面增强了代理的生产能力：

- 🧠 **开发代理**：提供推理控制、工具和运行时上下文、提供商文件与技能上传、MCP 应用以及终端 UI。
- ⚙️ **运行代理**：支持工具审批、持久化（WorkflowAgent）、超时和沙箱。
- 🔗 **集成代理框架**：可集成 Codex、Claude Code、Deep Agents、OpenCode 或 Pi 等。
- 👁️ **观察代理**：通过遥测、Node.js 追踪通道、生命周期事件和性能统计进行监控。
- 🎤 **超越文本代理**：支持提供商无关的实时语音和视频生成。

---

### [Electron 43 | Electron](https://www.electronjs.org/blog/electron-43-0)

**原文标题**: [Electron 43 | Electron](https://www.electronjs.org/blog/electron-43-0)

Electron 43 正式发布，带来多项性能改进和新功能，并升级了 Chromium、Node.js 和 V8 核心组件。

- 🚀 **启动性能提升**：主进程从嵌入式 Node.js 快照启动，框架包和预加载脚本缓存为 V8 字节码，沙盒渲染器启动数据提前推送，减少阻塞 IPC。
- 🖥️ **Linux 圆角窗口**：无框窗口在 Linux 上默认启用圆角，可通过 `roundedCorners: false` 禁用。
- 📂 **默认下载文件夹**：文件下载默认保存至用户“下载”文件夹（若无则使用主目录）。
- 🔔 **macOS 通知管理**：新增 `Notification.remove()`、`removeAll()`、`removeGroup()` 静态方法，支持完全管理通知生命周期。
- ⚙️ **核心升级**：Chromium 150.0.7871.46、Node v24.17.0、V8 15.0。
- ✨ **新功能与改进**：包括 WebContents 克隆、崩溃报告堆栈追踪、WebAuthn Touch ID 支持、全局快捷键暂停/恢复、Windows 通知分组、NV12 像素格式支持等。
- 🔄 **行为变更**：`nativeImage` 像素值标准化为 SRGB；Linux 无框窗口默认圆角；WCO 遵循原生标题栏布局；`chrome.scripting` CSS 注入支持更多回退框架。
- ❌ **移除与弃用**：Linux 上 `dialog` API 的 `showHiddenFiles` 选项被移除；Electron 40.x.y 停止支持；32 位平台（Windows x86、Linux ARM）将在 v43 生命周期结束后停止支持。

---

### [Deno 2.9 | Deno](https://deno.com/blog/v2.9)

**原文标题**: [Deno 2.9 | Deno](https://deno.com/blog/v2.9)

Deno 2.9 版本发布，带来桌面应用构建、性能大幅提升、Node.js 项目迁移简化等众多新特性。

- 🖥️ **deno desktop**：全新桌面应用构建工具，无需 Electron 样板代码，可将 Web 项目编译为单一原生桌面二进制文件，支持原生桌面 API、Webview 或 CEF 渲染引擎，以及跨平台交叉编译。
- 🚀 **性能大幅提升**：冷启动速度提升近 2 倍（34ms → 17ms），HTTP 吞吐量提升 11%-27%，内存占用在负载下降低 2.2-3.1 倍，保持约 62 MB 稳定。
- 📦 **无缝迁移 Node 项目**：`deno install` 可直接读取 npm、pnpm、yarn、Bun 的锁文件，保留精确依赖版本；自动处理 pnpm 工作区；`node` 命令被智能代理，无需额外配置。
- 🧪 **测试与覆盖率增强**：内置快照测试（`t.assertSnapshot()`）、变更感知测试选择（`--changed`）、失败重试（`--retry`）、重复运行（`--repeats`）、覆盖率阈值、分片测试（`--shard`）以及参数化测试（`Deno.test.each`）。
- 🎨 **CSS 模块导入**：支持通过 `import sheet from "./styles.css" with { type: "css" }` 导入可构造样式表，无需打包器。
- 🔧 **依赖管理工具**：新增 `deno link`/`deno unlink` 管理本地包链接、`deno list` 列出项目依赖、`preferPackageJson` 设置、`jsrDepsInNodeModules` 选项等。
- 🛡️ **供应链安全**：默认启用 24 小时最小发布年龄检查，新增 `no-downgrade` 信任策略防御维护者令牌被盗攻击。
- 🔒 **Web 加密 API 扩展**：实现后量子密码算法（ML-KEM、ML-DSA、SLH-DSA），新增 ChaCha20-Poly1305、SHA-3、Argon2 等算法，`crypto.subtle` 整体迁移至 Rust。
- 🌐 **Node.js 兼容性**：目标版本提升至 Node.js 26，裸 Node 内置模块无需配置即可解析，新增 `process.resourceUsage()` 等 API。
- ⚙️ **其他改进**：`deno compile` 新增 `--include-as-is`、`--bundle`、`--watch`；`deno fmt` 重构非 JS 格式化器并支持 `.editorconfig`；`deno task` 支持输入缓存、并发控制；Web Locks API、User-Agent Client Hints API、Happy Eyeballs v2 等。

---

### [Git 2.55 亮点 - GitHub 博客](https://github.blog/open-source/git/highlights-from-git-2-55/)

**原文标题**: [Highlights from Git 2.55 - The GitHub Blog](https://github.blog/open-source/git/highlights-from-git-2-55/)

Git 2.55 发布了多项新功能和改进，包括增量多包索引、修复历史提交、并行钩子等。

- 📦 **增量多包索引**：`git repack` 现在支持增量 MIDX 链，通过几何压缩保持层数对数增长，避免重写整个索引。
- 🔧 **修复历史提交**：`git history fixup` 命令可将暂存的更改直接应用到早期提交，并重放后续提交，无需手动变基。
- ⚡ **并行配置钩子**：兼容的配置钩子可并行运行，通过 `hook.jobs` 等选项控制并发数，提升效率。
- 🐧 **Linux 文件系统监控**：内置的 `fsmonitor` 现支持 Linux，使用 inotify 监控文件变化，加速 `git status`。
- 🚀 **位图生成优化**：通过避免树递归、重用位图等，生成时间从 612 秒降至 294 秒，伪合并位图也得到改进。
- 📉 **路径遍历打包**：`--path-walk` 模式现可与多种过滤器结合，如 `blob:none`，生成更小的包文件（如 16% 更小）。
- 📝 **新命令 `git format-rev`**：从标准输入格式化提交，替代 `git log` 处理单个提交，减少进程开销。
- 🔒 **侧带输出安全**：默认屏蔽终端控制序列，仅允许 ANSI 颜色，防止远程注入。
- 🛡️ **安全切换分支**：`git checkout -m` 使用自动 stash 保存冲突更改，避免丢失工作。
- 🌐 **远程组推送**：`git push` 现支持远程组，可同时推送到多个远程仓库（如主站和镜像）。
- 📊 **图形限制选项**：`git log --graph-lane-limit=<n>` 可限制图形列数，超出部分用 `~` 替代。
- ⏳ **最旧提交选择**：新增 `--max-count-oldest=<n>` 选项，直接获取范围内最旧的 n 个提交。
- 🤝 **协商引用控制**：新增 include/restrict 选项，控制哪些引用参与 fetch 协商，优化历史查找。

---

### [发布 12.7.0 · vitaly-t/pg-promise · GitHub](https://github.com/vitaly-t/pg-promise/releases/tag/12.7.0)

**原文标题**: [Release 12.7.0 · vitaly-t/pg-promise · GitHub](https://github.com/vitaly-t/pg-promise/releases/tag/12.7.0)

pg-promise 库发布了 12.7.0 版本，更新了依赖并扩展了官方支持的 Node.js 版本。

- 🔄 更新了所有依赖，包括 node-postgres 驱动至最新版本。
- 🆕 新增 NodeJS v26 为官方支持版本。
- ⚠️ 例外：仍使用 TypeScript v5.9.3 生成声明文件，未升级至 v6。

---

### [Middy.js](https://middy.js.org/)

**原文标题**: [Middy.js](https://middy.js.org/)

Middy 是一个专为 AWS Lambda 设计的 Node.js 中间件引擎，旨在简化代码组织、消除重复，并让开发者专注于业务逻辑。

- 📦 核心功能：中间件引擎将非功能性代码（如认证、验证、序列化）与业务逻辑分离，使代码更整洁、可维护。
- 🎯 专注业务：通过将非功能性代码移至中间件，开发者可专注于核心业务逻辑，提高生产力。
- ⚡ 轻量核心：Middy 拥有极小的核心和简洁 API，最大限度减少对 Lambda 性能的影响。
- 🔋 开箱即用：提供丰富的官方中间件和工具，覆盖常见非功能性需求（如日志、错误处理）。
- 🚀 高性能：优化设计保持 Lambda 冷启动快速，仅添加所需中间件以控制函数大小。
- 🔧 可扩展：支持自定义中间件，并通过钩子（hooks）扩展 Middy 自身功能。
- 📊 社区支持：拥有 3.9k GitHub Stars、300 万 + 月下载量、200+ 贡献者，社区活跃。
- 💻 代码示例：对比显示，使用 Middy 后，业务逻辑更纯净，非功能性代码被隔离为可复用的中间件链。
- 🔗 触发器支持：兼容多种 AWS Lambda 触发器，包括 API Gateway（HTTP/REST/WebSocket）、SQS、S3、DynamoDB、SNS 等。
- 🚀 快速上手：安装简单，文档清晰，可立即开始构建更整洁的 Lambda 函数。

---

### [错误](https://github.com/middyjs/middy/releases/tag/7.7.0)

**原文标题**: [Error](https://github.com/middyjs/middy/releases/tag/7.7.0)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /middyjs/middy/releases/tag/7.7.0 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [发布 v5.9.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.9.0)

**原文标题**: [Release v5.9.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.9.0)

Fastify v5.9.0 版本发布，包含多项新功能、错误修复、性能优化和文档改进。

- 🚀 **新增功能**: 新增 `request.mediaType` 属性和 `onMaxParamLength` 支持。
- 🐛 **错误修复**: 修复了多个问题，包括重复的 `res.end` 调用、重复的 `closeIdleConnections` 调用、路由错误时 `error.code` 缺失、无效路由 `logLevel` 验证、响应模式查找使用 ContentType 解析器、HTTP/2 大缓冲区回复分块、keep-alive 泄漏、嵌套前缀双斜杠、装饰器检查内置属性、异步错误处理程序诊断跟踪等。
- ⚡ **性能优化**: 延迟 ContentType 解析、缓存解析后的 ContentType 对象、在 `send` 和 `onSendEnd` 中添加类型守卫。
- 📚 **文档更新**: 更新了生态系统插件列表、贡献规则、错误页面、警告代码、类型定义、服务器指南 Dockerfile 等。
- 🔧 **CI/工程化**: 引入 TSTyche 进行类型测试、更新依赖、添加 Node.js 26 测试矩阵、更新赞助商列表。
- 👥 **新贡献者**: 欢迎 21 位新贡献者加入。

---

### [特性：由 climba03003 添加 request.mediaType · 拉取请求 #6653 · fastify/fastify · GitHub](https://github.com/fastify/fastify/pull/6653)

**原文标题**: [feat: add request.mediaType by climba03003 · Pull Request #6653 · fastify/fastify · GitHub](https://github.com/fastify/fastify/pull/6653)

Fastify 框架合併了 #6653 拉取請求，新增了 `request.mediaType` 唯讀屬性，並重構了內容類型處理方式。

- 🚀 新增 `request.mediaType` 唯讀屬性，供公開使用
- 🗃️ 新增 `kRequestContentType` 內部屬性，用於快取 `ContentType` 實例
- 🔄 重構程式碼，全面使用 `ContentType` 來解析標頭
- ✅ 通過所有檢查（37 項），並獲得多位審查者批准
- 📝 更新相關文件，並遵循開發者認證與行為準則

---

### [发布 3.3.0 · knex/knex · GitHub](https://github.com/knex/knex/releases/tag/3.3.0)

**原文标题**: [Release 3.3.0 · knex/knex · GitHub](https://github.com/knex/knex/releases/tag/3.3.0)

Knex 3.3.0 版本发布，新增多项功能、修复多个 Bug，并进行了代码优化和文档更新。

- 🚀 新增功能：支持 MariaDB 的 `returning` 子句和专用驱动
- 🔧 新增功能：允许通过 `connectionPool` 选项引入外部连接池
- 🗺️ 新增功能：添加 `knex.migrate.to` 和 `knex.migrate.before` 迁移方法
- 🐛 Bug 修复：修复带显式模式的 `FOR UPDATE OF` 查询
- 🐛 Bug 修复：修复 SQLite 多行插入时的条件插入/合并问题
- 🐛 Bug 修复：修复流式 `postProcessResponse` 错误无法被 `.on('error')` 捕获
- 🐛 Bug 修复：修复 PostgreSQL 中 `updateFrom` 绑定顺序
- 🐛 Bug 修复：修复 MSSQL 认证中的令牌凭据支持
- 🐛 Bug 修复：修复 `.where` 类型回归问题
- 🐛 Bug 修复：修复连接超时流时的未处理错误
- 🐛 Bug 修复：正确声明 MSSQL 所需的 `tedious` 依赖
- 🐛 Bug 修复：修复 PostgreSQL 和 MSSQL 中删除和更新查询的绑定顺序
- ⚡ 性能优化：优化 `wrappingFormatter` 的微性能
- 📚 文档更新：更新超时部分文档
- 🧹 杂项：升级 `tarn` 依赖至 3.1.0，清理测试，增强 CI 稳定性
- 👥 新贡献者：9 位新贡献者加入项目

---

### [GitHub - nodeca/js-yaml: JavaScript YAML 解析器和转储器。速度非常快。· GitHub](https://github.com/nodeca/js-yaml)

**原文标题**: [GitHub - nodeca/js-yaml: JavaScript YAML parser and dumper. Very fast. · GitHub](https://github.com/nodeca/js-yaml)

JS-YAML 是一个用于 JavaScript 的 YAML 1.2 解析器和写入器，支持 YAML 1.2 和 1.1 规范，并通过了完整的 YAML 测试套件。

- 📦 **安装与升级**：通过 `npm install js-yaml` 安装，从 v4 升级需参考 v5 迁移指南。
- 🔧 **核心 API**：提供 `load()` 解析单文档、`loadAll()` 解析多文档、`dump()` 序列化对象为 YAML，均支持多种选项配置。
- ⚙️ **选项丰富**：包括模式选择（如 `CORE_SCHEMA`、`YAML11_SCHEMA`）、缩进、引用样式、排序键、最大深度等，满足定制需求。
- 🛡️ **安全考虑**：处理不可信输入时需注意安全，默认 `CORE_SCHEMA` 不包含 `!!merge` 标签，可手动启用。
- 📚 **支持类型**：覆盖标准 YAML 类型（如 null、bool、int、float、str、seq、map）及 YAML 1.1 特有类型（如 binary、timestamp、set、omap、pairs）。
- 💻 **CLI 工具**：通过 `npx js-yaml -h` 快速检查 YAML 内容，但功能有限。
- 🌟 **项目状态**：拥有 6.6k 星标、820 个复刻，主要语言为 TypeScript（58.4%）和 JavaScript（40.5%），采用 MIT 许可证。

---

### [JavaScript 的 YAML 解析器 - JS-YAML](https://nodeca.github.io/js-yaml/)

**原文标题**: [YAML parser for JavaScript - JS-YAML](https://nodeca.github.io/js-yaml/)

YAML（YAML Ain't Markup Language）是一种人类可读的数据序列化格式，常用于配置文件和数据交换。js-yaml 是一个在 JavaScript 中解析和生成 YAML 的库，提供演示页面用于测试和转换。

- 🔧 **解析功能**：支持将 YAML 字符串转换为 JavaScript 对象，方便在代码中直接使用。
- 📝 **生成功能**：可将 JavaScript 对象序列化为 YAML 格式，便于数据存储或导出。
- 🖥️ **在线演示**：提供交互式界面，用户可输入 YAML 代码并实时查看转换后的 JS 对象。
- 🔗 **Permalink 功能**：支持生成当前编辑内容的永久链接，便于分享和版本保存。
- ⚙️ **Clear 按钮**：一键清空编辑区内容，快速重置演示环境。

---

### [远程站点可靠性工程师 | Crystallize 职业机会](https://crystallize.com/careers/senior-sre)

**原文标题**: [Remote Site Reliability Engineer | Crystallize Careers](https://crystallize.com/careers/senior-sre)

Crystallize 正在招聘远程高级 DevOps/后端工程师，负责保障其全球无头电商 GraphQL API 服务的高可用、可观测与可扩展性。

- 🌐 远程优先，可选择在挪威团队现场办公，加入产品工程团队，维护全球规模下的 GraphQL API 服务。
- 🎯 核心职责：定义并捍卫 SLO/SLA，管理错误预算，构建可观测性（指标、追踪、日志），主导事件响应与无指责事后分析。
- ⚙️ 技术栈：Node/TypeScript、GraphQL、AWS（ECS/EKS/Lambda）、MongoDB Atlas、Terraform、Cloudflare Workers。
- 📈 要求：分布式系统设计经验、AWS 管理能力、基础设施即代码（Terraform）熟练度、能跨层调试 TypeScript/GraphQL 代码库。
- 🚀 加分项：多租户 SaaS、电商流量模式或无头架构经验。
- 🌱 成长机会：多样化团队、挑战性工作、知识共享文化，助力推动互联网工艺边界。
- 📝 申请需提交：姓名、邮箱、LinkedIn、GitHub、动机信（最多 5000 字符）、简历（PDF，最大 5MB），并同意数据用于招聘流程。

---

