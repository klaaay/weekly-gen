### [Node 周刊第 614 期：2026 年 3 月 5 日](https://nodeweekly.com/issues/614)

**原文标题**: [Node Weekly Issue 614: March 5, 2026](https://nodeweekly.com/issues/614)

Node.js 团队正考虑将主要版本发布频率调整为每年一次，并取消奇数/偶数版本区分，使每个版本都成为长期支持版本。同时，Node.js 25.8.0 发布，新增权限审计功能；社区讨论了改进 JavaScript 流 API 的提案，并出现了多项工具更新。

- 🗓️ Node.js 团队计划调整发布计划，可能改为每年一个主要版本，每个版本均为 LTS 版本
- 🔧 Node.js 25.8.0 发布，新增`--permission-audit`标志，用于权限模型的审计和调试
- 💬 社区提出改进 JavaScript 流 API 的替代方案，以解决现有标准的可用性和性能问题
- 🛠️ 多个工具更新发布，包括 Bun v1.3.10、Fastify 5.8、AVA 7.0 等
- 🌐 Inquirer.js 新增 i18n 包，支持非英语命令行提示
- 📄 VMPrint 推出纯 JavaScript 排版引擎，用于生成精确的 PDF 输出
- 💰 Dinero.js 2.0 发布，为货币计算提供不可变库
- 🔍 出现新的 npm 注册表浏览工具 npmx.dev，目前处于 alpha 阶段

---

### [错误](https://nodeweekly.com/link/181550/web)

**原文标题**: [Error](https://nodeweekly.com/link/181550/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodejs-org-git-fork-ulisesgascon-release-announcement-openjs.vercel.app', port=443): Max retries exceeded with url: /en/blog/announcements/evolving-the-nodejs-release-schedule (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [提案 - 将 Node.js 改为年度主要版本发布并缩短 LTS 支持周期 · Issue #1113 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1113)

**原文标题**: [Proposal - Shift Node.js to Annual Major Releases and Shorten LTS Duration · Issue #1113 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1113)

Node.js 社区正在讨论一项提案，旨在将主要版本发布周期从半年一次改为一年一次，并缩短长期支持（LTS）的持续时间，以减轻维护负担并提高版本稳定性。

- 🗓️ **发布周期调整**：提议将 Node.js 的主要版本发布从每年两次改为每年一次，以简化维护工作并减少社区困惑。
- ⏳ **LTS 期限缩短**：建议将长期支持的总时长从 30 个月减少至 24 个月，包括 12 个月的活跃 LTS 和 12 个月的维护 LTS。
- 🛠️ **减轻维护压力**：当前频繁的发布节奏使维护者面临管理多个版本、修复回溯和确保兼容性的巨大压力，新模型旨在缓解这一问题。
- 🚀 **提升稳定性与可预测性**：年度发布和明确的 LTS 生命周期将为用户和生态伙伴提供更清晰、稳定的版本规划路线图。
- ⚖️ **权衡利弊**：好处包括降低维护负担、提高发布质量；潜在缺点则是重大新功能的推出速度可能放缓，以及部分社区可能对缩短的 LTS 期初有抵触。
- 📋 **实施策略**：提案需获得技术指导委员会和发布工作组的共识，随后更新官方文档并开展广泛的生态沟通，确保平稳过渡。
- 💬 **征求社区反馈**：鼓励社区参与讨论，以确保提案最终能更好地满足整个 Node.js 生态系统的需求。

---

### [Node.js 发布日程演进 · GitHub](https://gist.github.com/peterc/c67c356a802f37b0ea5528fcf8546cb7)

**原文标题**: [Evolving the Node.js Release Schedule · GitHub](https://gist.github.com/peterc/c67c356a802f37b0ea5528fcf8546cb7)

Node.js 将从 2027 年的 v27 版本开始，将每年两次的主要版本发布调整为一次，以简化发布流程、减轻维护负担，并更好地适应用户实际需求。

- 📅 **发布周期调整**：从每年两个主要版本改为一个，版本号与年份对齐（如 v27 于 2027 年发布）
- 🔄 **取消奇偶版本区分**：所有版本都将成为长期支持（LTS）版本，消除用户困惑
- 🧪 **新增 Alpha 测试通道**：替代原有的奇数版本，用于早期功能测试
- ⏳ **支持周期优化**：活跃版本线从最多 5 个减少到 3 个，总支持期为 35 个月
- 👥 **维护可持续性**：减轻志愿者维护负担，集中资源保障常用版本的稳定性
- 📊 **基于数据的决策**：根据十年使用数据，发现奇数版本采用率极低，多数用户直接使用 LTS 版本
- 🗓️ **时间安排明确**：每年 4 月发布新版本，10 月进入 LTS 阶段，保持可预测性
- 🔧 **质量标准不变**：LTS 支持时长、测试流程和安全标准均保持不变

---

### [使用 Memetria K/V 构建 — Memetria](https://dashboard.memetria.com/nodeweekly/)

**原文标题**: [Build with Memetria K/V — Memetria](https://dashboard.memetria.com/nodeweekly/)

Memetria 提供兼容 Valkey 和 Redis 的键值存储服务，支持无缝扩展、加密连接和详细监控，并提供从开发到高性能的多层级托管方案。

- 🛠️ **兼容性**：支持 Valkey 和 Redis OSS，轻松导入导出数据
- 📈 **无缝扩展**：可在无需停机的情况下调整资源规模
- 🔐 **加密连接**：提供双重和仅 TLS 的连接选项以确保安全
- 📊 **详细监控**：包含健康状态、内存及性能的详细图表
- 💼 **托管方案**：提供开发版（共享资源，最高 250MB）、生产版（专属资源，最高 3.5GB）和高性能版（专属资源、高 I/O、包含高可用性）等多种计划
- 🌍 **区域覆盖**：服务覆盖全球多个 AWS 区域，包括非洲、亚洲、欧洲、北美和南美等地
- 📝 **注册要求**：需使用工作邮箱注册，并同意服务条款、隐私政策及最终用户许可协议

---

### [Node.js — Node.js 25.8.0（当前版本）](https://nodejs.org/en/blog/release/v25.8.0)

**原文标题**: [Node.js — Node.js 25.8.0 (Current)](https://nodejs.org/en/blog/release/v25.8.0)

Node.js 25.8.0 版本发布，包含多项功能增强、安全修复和依赖项更新，提升了性能、稳定性和开发体验。

- 📚 采用新的 API 文档工具链，改进文档生成流程
- 🗄️ SQLite 模块新增 `limits` 属性至 `DatabaseSync`，增强数据库控制能力
- 🔧 新增 C++ 层面对诊断通道的支持，便于性能监控与调试
- 🔐 引入 `--permission-audit` 标志，强化权限审计功能
- 🧪 测试运行器支持暴露工作线程 ID，优化并发测试执行
- ⚡ 优化 `buffer.concat` 性能，提升数据处理效率
- 🛡️ 修复多项加密模块潜在的空指针解引用问题，增强安全性
- 📦 更新核心依赖项，包括 undici 至 7.22.0、npm 至 11.11.0
- 🌐 改进 HTTP 模块，验证客户端请求路径与早期提示头部
- 🔄 修复流模块中 `pipeTo` 方法的写入行为以符合 WHATWG 规范

---

### [src,permission: 从 C++ 发送 dc 消息并使用--permission-audit 由 RafaelGSS · Pull Request #61869 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61869)

**原文标题**: [src,permission: emit dc messages from C++ and use --permission-audit  by RafaelGSS · Pull Request #61869 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61869)

该拉取请求为 Node.js 添加了 C++ 端的诊断通道支持，并引入了`--permission-audit`标志，使权限模型以仅警告模式运行，通过诊断通道发布消息而非直接拒绝操作。

- 🔧 **新增 C++ 诊断通道 API**：允许原生代码高效检查订阅者并发布消息，减少 JS 边界开销。
- 📊 **共享缓冲区优化性能**：使用 AliasedUint32Array 在 C++ 和 JS 间共享数据，实现快速的`HasSubscribers`内联检查。
- 🚨 **引入权限审计模式**：通过`--permission-audit`标志，权限检查失败时发布诊断消息并允许操作继续。
- 📡 **按作用域发布权限结果**：将权限决策发布到特定诊断通道（如`node:permission-model:fs`），方便运行时监控。
- 🔄 **代码审查与优化**：经过讨论优化了发布回调机制，避免在热路径中频繁调用`dc.channel()`。
- ✅ **已合并并发布**：该功能已作为 semver-minor 变更并入 Node.js v25.8.0 版本。

---

### [权限 | Node.js v25.8.0 文档](https://nodejs.org/api/permissions.html)

**原文标题**: [Permissions | Node.js v25.8.0 Documentation](https://nodejs.org/api/permissions.html)

Node.js 权限模型是一种进程级的安全机制，通过限制对文件系统、网络、子进程等资源的访问，防止可信代码无意中执行危险操作，但无法防御恶意代码的绕过。

- 🔐 **权限模型概述**：Node.js 权限模型通过`--permission`标志启用，默认限制对文件系统、网络、子进程等核心模块的访问，采用“安全带”机制防止意外操作。
- 🚩 **启用与配置**：使用`--allow-fs-read`、`--allow-net`等标志细化权限；支持通配符路径和配置文件（需配合`--experimental-config-file`）进行权限设置。
- 📁 **文件系统权限**：通过`--allow-fs-read`和`--allow-fs-write`控制读写权限，支持相对路径、绝对路径和通配符；入口文件自动加入读取白名单。
- ⚙️ **运行时 API**：启用权限后，可通过`process.permission.has()`动态检查权限，例如验证是否具有特定文件的读写权限。
- 🔗 **npx 集成**：使用`npx`时需通过`--node-options`传递权限参数，并需额外授权全局`node_modules`或 npm 缓存目录的读取权限。
- ⚠️ **约束与限制**：权限不继承到 Worker 线程；启用后会限制原生模块、网络、子进程等功能；符号链接可能绕过路径限制；OpenSSL 引擎和运行时扩展加载受限。

---

### [宣布 Node.js LTS 升级与现代化计划 | OpenJS 基金会](https://openjsf.org/blog/nodejs-lts-upgrade-program)

**原文标题**: [Announcing the Node.js LTS Upgrade and Modernization Program | OpenJS Foundation](https://openjsf.org/blog/nodejs-lts-upgrade-program)

OpenJS 基金会推出 Node.js LTS 升级与现代化计划，旨在帮助企业安全地从过时或停止支持的 Node.js 版本迁移，降低安全与运营风险，并通过认证合作伙伴提供专业升级服务。

- 🚀 **计划启动**：OpenJS 基金会正式推出 Node.js 长期支持（LTS）升级与现代化计划，助力企业安全迁移旧版 Node.js
- 🤝 **合作模式**：基金会负责制定计划框架与标准，认证商业合作伙伴（首期为 NodeSource）直接为客户提供升级服务
- ⚠️ **问题背景**：约三分之二 Node.js 用户仍在使用过时或不受支持的版本，导致广泛的安全与运营风险
- 🛡️ **服务内容**：包括版本评估、依赖分析、分阶段升级方案、测试执行以及临时安全支持选项
- 💰 **收益分配**：采用生态系统可持续计划收入模式，合作伙伴保留 85% 收入，15% 用于支持 OpenJS 与 Node.js 项目
- 🌐 **访问渠道**：升级服务信息将直接展示在 Node.js 官网、文档及生命周期结束指南等用户触达场景
- 🎯 **核心目标**：为企业提供低风险升级路径，确保其在现代化过程中保持与 Node.js 上游项目的紧密联系

---

### [GitHub - SBoudrias/Inquirer.js：一系列常见的交互式命令行用户界面。· GitHub](https://github.com/SBoudrias/Inquirer.js)

**原文标题**: [GitHub - SBoudrias/Inquirer.js: A collection of common interactive command line user interfaces. · GitHub](https://github.com/SBoudrias/Inquirer.js)

Inquirer.js 是一个用于构建交互式命令行界面的 Node.js 库，提供了多种常见提示类型，支持国际化，并允许用户创建自定义提示。

- 📦 提供多种内置提示类型，如输入、选择、确认、密码、编辑器等
- 🌍 通过 @inquirer/i18n 包支持国际化，可自动检测或指定语言环境
- 🔧 允许开发者通过 API 创建自定义提示，并提供了测试工具
- ⚙️ 支持高级配置，如自定义输入/输出流、清除提示、使用 AbortSignal 取消操作
- 🛡️ 包含错误处理指南，如优雅处理 Ctrl+C 退出和超时默认值
- 🔄 提供实用技巧，如条件提问、答案收集为对象、在脚本或钩子中使用
- 🧩 社区贡献了多种扩展提示，如交互式列表、文件选择器、可排序复选框等
- 📄 采用 MIT 许可证，由 Simon Boudrias 维护，在 GitHub 上拥有大量星标和分支

---

### [GitHub - SBoudrias/Inquirer.js：一系列常见的交互式命令行用户界面。· GitHub](https://github.com/SBoudrias/Inquirer.js?tab=readme-ov-file#internationalization-i18n)

**原文标题**: [GitHub - SBoudrias/Inquirer.js: A collection of common interactive command line user interfaces. · GitHub](https://github.com/SBoudrias/Inquirer.js?tab=readme-ov-file#internationalization-i18n)

Inquirer.js 是一个用于构建交互式命令行界面的 Node.js 库，提供了一系列常见提示组件，支持国际化，并允许用户创建自定义提示。

- 📦 **核心功能**：提供输入、选择、确认、密码等多种交互式命令行提示组件。
- 🚀 **现代化重构**：近期进行了彻底重写，以减小包体积并提升性能。
- 🌍 **国际化支持**：通过 `@inquirer/i18n` 包支持多语言（如英语、法语、中文等），可自动检测环境语言。
- ⚙️ **高级配置**：支持自定义输入/输出流、清除提示、使用 AbortSignal 取消操作等。
- 🛠️ **自定义扩展**：提供了 API 和测试工具，方便开发者创建自己的提示组件。
- 🔧 **实用技巧**：文档包含优雅处理 Ctrl+C、条件提问、超时默认值、在脚本中使用等多种场景的示例。
- 🤝 **社区生态**：拥有丰富的社区贡献提示（如交互式列表、文件选择器、可排序复选框等）。
- 📄 **开源协议**：项目采用 MIT 许可证，由 Simon Boudrias 维护。

---

### [Drizzle ORM - 下一代 TypeScript ORM。](https://orm.drizzle.team/)

**原文标题**: [Drizzle ORM - next gen TypeScript ORM.](https://orm.drizzle.team/)

Drizzle ORM 是一个基于 TypeScript 的轻量级、高性能对象关系映射工具，专注于开发者体验和与多种数据库及运行时的兼容性。它提供类型安全的查询构建、灵活的迁移管理以及直观的数据操作接口，同时支持广泛的数据库驱动和云平台集成。

- 🚀 **高性能与轻量级** – 相比传统 ORM 具有更低的延迟和更高的请求处理能力，专为现代应用优化。
- 🔗 **多数据库支持** – 兼容 PostgreSQL、MySQL、SQLite、MSSQL、CockroachDB 等主流数据库，并提供多种驱动和云服务连接方案。
- 🛠️ **类型安全与开发体验** – 完全基于 TypeScript 设计，提供自动类型推断、查询构建和验证集成（如 Zod、Valibot）。
- 📦 **迁移与架构管理** – 通过 Drizzle Kit 提供生成、推送、拉取等迁移命令，支持团队协作和自定义迁移流程。
- 🌐 **全平台运行时兼容** – 可在 Cloudflare Workers、Vercel、Supabase、Deno、Bun 等服务器和边缘环境中运行。
- 🧩 **模块化与扩展性** – 支持关系定义、行级安全、缓存层、动态查询构建等高级功能，并持续集成新特性和修复。
- 📈 **活跃的社区与持续更新** – 拥有活跃的贡献者团队，定期发布版本更新、新增功能（如 RLS 支持、Gel 方言）并优化文档和工具。
- 🎮 **开发者工具丰富** – 提供 Drizzle Studio 用于数据浏览和架构管理，以及 CLI 工具、基准测试和教程资源。

---

### [Drizzle 加入 PlanetScale —— PlanetScale](https://planetscale.com/blog/drizzle-joins-planetscale)

**原文标题**: [Drizzle joins PlanetScale â PlanetScale](https://planetscale.com/blog/drizzle-joins-planetscale)

PlanetScale 宣布 Drizzle 团队加入，共同致力于提升 JavaScript 和 TypeScript 的数据库工具性能与开发者体验，同时保持 Drizzle 作为独立开源项目的地位。

- 🚀 Drizzle 团队加入 PlanetScale，专注于优化 JavaScript 和 TypeScript 的数据库工具性能与开发者体验  
- 🔧 Drizzle ORM 因高性能和开发者友好性成为默认选择，与 PlanetScale 理念高度契合  
- 🌍 Drizzle 将继续作为独立开源项目运营，保持自身路线图和目标不变  
- 💪 PlanetScale 将支持 Drizzle 团队专注于核心工作，强化开源社区贡献  
- 🤝 PlanetScale 团队感谢 Drizzle 对社区的积极影响，欢迎成为同事

---

### [我们值得为 JavaScript 拥有一个更好的流 API。](https://blog.cloudflare.com/a-better-web-streams-api/)

**原文标题**: [We deserve a better streams API for JavaScript](https://blog.cloudflare.com/a-better-web-streams-api/)

本文探讨了当前 Web Streams API 存在的根本性可用性和性能问题，并提出了一种基于 JavaScript 语言原语的替代方案。作者认为，尽管 Web Streams 标准在统一浏览器和服务器端流处理方面做出了重要贡献，但其设计决策导致了复杂的 API、性能开销以及常见的开发陷阱。新方案通过利用现代 JavaScript 特性（如异步迭代），采用拉取式转换、显式背压策略和批处理块等设计原则，在基准测试中实现了显著的性能提升（2 倍至 120 倍）。文章旨在引发关于未来流 API 设计的讨论，而非直接取代现有标准。

- 🚀 **性能瓶颈**：Web Streams API 因过度依赖 Promise 和复杂的状态管理，在高频场景下产生显著性能开销。
- 🔒 **锁机制问题**：手动锁管理（`getReader()`/`releaseLock()`）容易导致流被意外永久锁定，增加调试难度。
- 🧩 **BYOB 复杂性**：BYOB（自带缓冲区）读取 API 设计复杂且使用率低，增加了实现和使用的负担。
- ⚖️ **背压机制缺陷**：背压信号（如`desiredSize`）仅为建议性，无法有效防止内存无限增长，`tee()`等操作可能导致无界缓冲。
- 🔄 **转换流问题**：`TransformStream`采用推送模型，可能在没有消费者时仍执行转换，导致不必要的计算和缓冲。
- 🗑️ **GC 压力**：在服务器端渲染等场景中，大量小数据块处理会引发垃圾回收压力，降低吞吐量。
- 🛠️ **实现优化负担**：各运行时（如 Node.js、Deno、Bun）需自行开发非标准优化以提升性能，导致行为不一致和可移植性问题。
- 📜 **规范复杂性**：Web Streams 规范包含大量边缘情况测试（如原型污染防御、WebAssembly 内存处理），增加了实现和维护成本。
- 🔄 **新方案设计原则**：提出以异步迭代为核心、拉取式转换、显式背压策略和批处理块的新 API，强调简单性和性能。
- ⚡ **性能对比**：新方案在多项基准测试中表现优异，尤其在链式转换场景下，性能提升可达 80-90 倍。
- 🔗 **兼容性与迁移**：新方案可通过适配层与现有 Web Streams 互操作，并提供了同步/异步分离的 API 以优化不同场景。
- 💬 **呼吁讨论**：作者开源了参考实现，鼓励社区就流 API 的未来设计进行反馈和探讨。

---

### [[草案] 流：jasnell 提出的新流实现原型 · Pull Request #62066 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62066)

**原文标题**: [[DRAFT] stream: prototype for new stream implementation by jasnell · Pull Request #62066 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62066)

Node.js 社区正在讨论一个关于新流实现的原型提案，该提案旨在探索性能优化和与现有流实现的兼容性。

- 🚀 提案引入了一种新的流实现原型，性能测试显示在某些场景下比传统 Node.js 流快 15%，比 Web 流快两倍。
- 🔧 新设计强调严格的反压处理，与 Web 流忽略反压的模式不同，旨在提供更可控的数据流管理。
- 📊 内存基准测试表明，新流在管道和广播场景中显著减少了堆内存使用，例如在 `pipeTo` 转换中内存占用仅为 Web 流的约 1/7。
- ⚠️ 讨论中指出了异步生成器可能存在的资源泄漏风险，以及跨领域（cross-realm）类型检查的兼容性问题。
- 🔄 代码优化建议包括使用位图减少实例大小，以及考虑在 Node.js 环境中使用 `Buffer` 而非 `Uint8Array` 以提升性能。
- 🛠️ 提案目前处于草案阶段，主要用于评估可行性和性能，尚未计划立即合并到主分支。

---

### [在Jetson Nano上使用Node 22升级OpenClaw至最新版本 · brtkwr.com](https://brtkwr.com/posts/2026-03-02-upgrading-openclaw-to-latest-node22-on-jetson-nano/)

**原文标题**: [Upgrading OpenClaw to Latest on Jetson Nano with Node 22 · brtkwr.com
](https://brtkwr.com/posts/2026-03-02-upgrading-openclaw-to-latest-node22-on-jetson-nano/)

本文记录了在Jetson Nano上将OpenClaw升级至最新版本（Node 22环境）的完整过程，包括因Bun安装路径问题导致的升级失败、尝试Docker方案后放弃、耗时27小时从源码编译Node 22的详细经历，以及最终通过彻底清理和重新安装成功部署OpenClaw的步骤与关键注意事项。

- 🚀 **升级动机**：原Bun安装运行正常，但为获取新功能（如改进的Telegram处理、cron修复、模型回退链优化及Claude自适应思维默认设置）而进行升级。
- 🛑 **Bun停止工作**：OpenClaw自2026.2.26版本起加强插件清单验证，Bun全局安装路径被判定为不安全，导致服务崩溃循环，需切换至Node环境。
- 🐳 **Docker方案尝试与放弃**：容器化方案虽简单但失去主机直接访问能力（如tmux面板抓取、摄像头调用），不符合在Jetson Nano上运行OpenClaw的集成需求，故回归主机原生部署。
- ⏳ **编译Node 22的漫长过程**：因Jetson Nano系统老旧（Ubuntu 18.04），无预编译Node 22二进制文件，从源码编译耗时约27小时，期间经历内存不足中断、MTE指令集补丁修复等问题。
- 🤖 **自动化监控的教训**：设置OpenClaw cron任务每小时检查编译进度，但编译完成后未及时停止监控，导致持续报告“编译已完成”并耗尽免费API配额。
- 🧹 **彻底清理与重装**：移除Bun依赖、删除残留安装目录，使用npm全新安装OpenClaw，并在systemd服务中明确指定Node和OpenClaw路径以确保稳定性。
- 💾 **数据安全性**：用户数据（配置、记忆、会话）均存储在`~/.openclaw`目录，重装二进制包不会影响这些数据，但仍建议升级前备份。
- 📦 **新版本特性**：2026.3.1版本引入Claude自适应思维默认设置、cron定时任务热循环防护、Telegram功能修复及消息控制令牌清理等改进。
- 🧠 **关键建议**：在Jetson Nano上优先选择全新安装而非原地升级；长期任务务必使用tmux会话；监控任务需设置停止条件；升级前备份数据目录。

---

### [Jetson Nano | NVIDIA 开发者平台](https://developer.nvidia.com/embedded/jetson-nano)

**原文标题**: [Jetson Nano | NVIDIA Developer](https://developer.nvidia.com/embedded/jetson-nano)

Jetson Nano是一款专为嵌入式应用和AI物联网设计的紧凑型高性能计算机，以99美元的价格提供现代AI计算能力，并配备完整的JetPack SDK以加速开发。

- 💻 搭载NVIDIA Maxwell架构GPU和四核ARM Cortex-A57处理器，具备强大的AI运算能力
- 💾 配备4GB LPDDR4内存和16GB eMMC存储，支持高效数据处理
- 🎥 支持4K视频编解码，最高可处理1路4K@60帧或9路720p@30帧视频流
- 📡 提供丰富的连接选项，包括千兆以太网、4个USB 3.0接口和多种扩展接口
- 🔌 采用69.6×45毫米紧凑设计，通过260针边缘连接器实现模块化扩展
- 🛠️ 配套JetPack SDK包含深度学习、计算机视觉等加速库，简化开发流程
- 🤝 拥有合作伙伴生态系统，提供基于Jetson Nano的成熟产品解决方案

---

### [Temporal 驱动对持久执行的需求 | Temporal](https://temporal.io/blog/temporal-raises-usd300m-series-d-at-a-usd5b-valuation?utm_source=newsletter&utm_medium=sponsorship&utm_campaign=newsletter-2026-03-05-node&utm_content=series-d-node)

**原文标题**: [Temporal drives demand for Durable Execution  | Temporal](https://temporal.io/blog/temporal-raises-usd300m-series-d-at-a-usd5b-valuation?utm_source=newsletter&utm_medium=sponsorship&utm_campaign=newsletter-2026-03-05-node&utm_content=series-d-node)

过去一年，客户关注点从“如何提升工作流可靠性”转向“如何构建能在生产中稳定运行的AI系统”，核心解决方案不变但重要性显著提升。Temporal宣布完成由Andreessen Horowitz领投的3亿美元D轮融资，投后估值达50亿美元，多家顶级风投参与。

- 🚀 **融资里程碑**：完成3亿美元D轮融资，投后估值50亿美元，获a16z等顶级机构支持
- 🤖 **AI驱动变革**：传统架构难以应对AI长时任务、动态工作流等新需求，凸显持久化执行技术价值
- ⚙️ **技术普适性**：除AI场景外，金融交易、合规流程等长时运行业务同样依赖可靠执行框架
- 📈 **业务爆发增长**：年收入增长超380%，月安装量超2000万，AI企业执行量达1.86万亿次
- 🛡️ **企业级验证**：支持每秒15万+操作峰值，经受住云服务中断考验，获OpenAI、ADP等企业采用
- 👥 **生态拓展**：引入VMware前CEO担任董事会观察员，加速AI原生功能开发与开发者体验优化
- 🎪 **社区建设**：筹备2026年Replay大会，汇集实战案例分享与黑客松等开发者活动
- 🙏 **致谢生态**：承诺持续服务开源贡献者、生产用户及承载关键业务的企业客户

---

### [服务器端JavaScript中的fetch请求代理 - Human Who Codes](https://humanwhocodes.com/blog/2026/03/proxying-fetch-requests-server-side-javascript/)

**原文标题**: [Proxying fetch requests in server-side JavaScript - Human Who Codes](https://humanwhocodes.com/blog/2026/03/proxying-fetch-requests-server-side-javascript/)

本文介绍了在Node.js、Deno、Bun和Cloudflare Workers等服务器端JavaScript运行时中代理fetch()请求的方法，用于监控和控制网络流量。

- 🌐 **代理请求的用途**：用于记录流量、修改请求头、调整内容、通过缓存提升性能或隐藏原始IP地址。
- ⚙️ **Node.js代理方式**：通过环境变量（如`HTTP_PROXY`、`HTTPS_PROXY`）或使用`undici`包的`ProxyAgent`类编程实现。
- 🦕 **Deno代理方式**：通过`Deno.createHttpClient()`创建支持代理的客户端，并在fetch选项中指定。
- 🐰 **Bun代理方式**：直接在fetch选项中使用`proxy`属性设置代理服务器。
- ☁️ **Cloudflare Workers代理方案**：本身不支持原生代理，但可通过Docker容器运行`@humanwhocodes/proxy-fetch-server`工具实现。
- 🔧 **实现差异**：各运行时对fetch代理的支持方式不同，需根据具体环境选择相应配置方法。

---

### [为何我选择Electron而非原生开发（且会再次选择）- Syntax #983](https://syntax.fm/show/983/why-i-chose-electron-over-native-and-i-d-do-it-again)

**原文标题**: [Why I Chose Electron Over Native (And Iâd Do It Again) - Syntax #983](https://syntax.fm/show/983/why-i-chose-electron-over-native-and-i-d-do-it-again)

在Syntax播客第983集中，Wes Bos和Scott Tolinski讨论了开发自定义多源视频录制应用v_framer的经验，重点解释了为何选择Electron而非Tauri或原生API，并分享了应用开发中的关键技术挑战和解决方案。

- 🎙️ 讨论了现有屏幕录制应用的常见痛点，如功能限制和稳定性问题
- 🛠️ 详细介绍了v_framer应用的需求背景和开发目标
- 🔍 尝试了Tauri和WKWebView方案，但遇到模糊录制等技术难题
- ⚡ 切换到Electron后显著改善了开发体验和性能表现
- 🧪 提及了Electrobun混合桌面应用的实验性探索
- 🌐 对比了浏览器捕获与原生API在屏幕录制中的优劣
- 📦 分享了Mac应用上架所需的公证和证书管理流程
- 💳 讨论了一次性购买、试用版和桌面软件销售策略
- 🔑 使用自托管Keygen系统管理软件许可证密钥
- 📊 采用Google Sheets搭建了简易的候补名单系统
- ⌨️ 实现了键盘快捷键、FPS锁定等应用自定义功能
- 🔄 建立了基于CI/CD的无痛自动更新机制

---

### [GitHub - cosmiciron/vmprint：一款纯JavaScript、小巧的排版引擎，可在从Cloudflare Workers到浏览器的所有平台上实现位级精确的PDF输出。无需Headless Chrome即可打印文本。请访问下方主页尝试静态演示，亲自体验。· GitHub](https://github.com/cosmiciron/vmprint)

**原文标题**: [GitHub - cosmiciron/vmprint: A pure-JS, tiny typesetting engine with bit-perfect PDF output on everything—from Cloudflare Workers to the browser. No more Headless Chrome to just print text. AND -- try the static demos on the home page below and see for yourself. · GitHub](https://github.com/cosmiciron/vmprint)

VMPrint 是一个纯 TypeScript 编写的确定性、零 DOM 依赖的排版引擎/虚拟机，旨在为构建自定义文档生成器、边缘渲染管道或全新文字处理器提供底层数学基础设施。它通过基于真实字形度量的排版算法，实现跨平台一致的复杂页面布局，支持多栏文本、浮动元素、表格分页及多语言排版，并输出可序列化的 JSON 布局数据，便于测试和分发。

- 🚀 **确定性布局引擎** – 在不同操作系统和运行时环境中生成完全一致的布局，无布局漂移。
- 🌐 **零环境依赖** – 核心引擎无需无头浏览器、DOM 或 Node.js 内置模块，可在浏览器、Node.js 及边缘环境（如 Cloudflare Workers）中运行。
- 📏 **真实字形度量** – 直接从字体文件读取 OpenType 字宽和字距数据，基于精确的排版数学进行布局。
- ⚡ **高性能** – 在毫秒级内渲染复杂的多页布局，通过全局缓存实现高吞吐批处理。
- 📄 **多栏与混合布局** – 原生支持桌面出版风格的多栏区域，可在同一页面中混合单栏标题、多栏文章和浮动引文。
- 📊 **复杂表格支持** – 处理跨页表格，支持行列合并、智能行分割及自动重复表头。
- 🌍 **多语言排版** – 基于 Intl.Segmenter 实现字形级断行，支持语言感知的连字符处理及混合文字基线对齐。
- 🔧 **可插拔架构** – 可更换字体管理和渲染后端（如 PDF、SVG、Canvas），易于扩展。
- 📦 **轻量级与便携** – 完整依赖树约 2 MiB（压缩后），远小于 Chromium 的 170 MB，适合边缘环境和客户端静态打包。
- 🔄 **JSON 布局管道** – 布局输出为可序列化的对象树，支持预编译、快照测试和精确测量检查。

---

### [vmprint/documents/readme-assets/readme.pdf 位于主分支 · cosmiciron/vmprint · GitHub](https://github.com/cosmiciron/vmprint/blob/main/documents/readme-assets/readme.pdf)

**原文标题**: [vmprint/documents/readme-assets/readme.pdf at main · cosmiciron/vmprint · GitHub](https://github.com/cosmiciron/vmprint/blob/main/documents/readme-assets/readme.pdf)

这是一个名为“vmprint”的GitHub仓库，由用户“cosmiciron”创建和维护，主要用于文档和资源管理。

- 📂 仓库包含文档和资源文件，如readme.pdf
- ⭐ 项目获得286个星标，显示一定社区关注度
- 🔄 设有分支、议题和拉取请求等协作功能
- 📄 提供PDF等格式的文档资源
- 🛠️ 支持代码管理、安全检查和项目洞察

---

### [迪内罗.js](https://www.dinerojs.com/)

**原文标题**: [Dinero.js](https://www.dinerojs.com/)

本文档提供了关于API版本2.0.0的导航和资源，包括文档、更新日志以及旧版v1文档的访问入口。

- 📚 主要导航：包含文档和API 2.0.0版本的访问路径
- 🔄 更新记录：提供版本变更日志，便于追踪最新改动
- 📖 历史文档：保留v1版本文档供用户参考
- 🎨 外观设置：支持界面个性化调整选项

---

### [发布 v2.0.0 · dinerojs/dinero.js · GitHub](https://github.com/dinerojs/dinero.js/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · dinerojs/dinero.js · GitHub](https://github.com/dinerojs/dinero.js/releases/tag/v2.0.0)

Dinero.js v2 是一个完全重写的现代 JavaScript/TypeScript 货币处理库，采用函数式架构，提供纯函数、完全可树摇、支持大整数和任意精度计算，并包含完整的 ISO 4217 货币支持。

- 🚀 **完全重写**：v2 版本为现代 JavaScript 和 TypeScript 从头设计，用函数式纯函数 API 取代了 v1 的面向对象链式 API。
- 📦 **完全可树摇**：所有函数都是独立的，打包工具可以移除未使用的代码，减小打包体积。
- 💰 **结构化货币对象**：货币现在是用包含 `code`、`base` 和 `exponent` 属性的对象表示，取代了之前的 ISO 字符串，并内置了 166 种 ISO 4217 货币。
- 🔢 **BigInt 支持**：通过 `dinero.js/bigint` 入口点支持原生 `bigint` 运算，可处理超过 `Number.MAX_SAFE_INTEGER` 的金额，适用于加密货币和高精度金融场景。
- ⚙️ **可插拔计算器**：`createDinero` 工厂函数允许接入第三方任意精度库（如 big.js、JSBI）作为数值计算后端。
- 🧮 **自动精度追踪**：用 `scale` 参数取代 `precision`，并在计算中自动传播，`trimScale` 函数可在需要时将其缩减至最小安全表示。
- 🛡️ **编译时货币安全**：TypeScript 类型使用字面量代码，可在编译时捕获货币不匹配的错误（例如尝试相加 USD 和 EUR）。
- 🌍 **非十进制货币支持**：通过 `currency.base` 数组字段支持具有多重细分单位的货币（如旧式英镑）。
- 🔧 **新的实用函数**：增加了 `compare`、`toDecimal`、`toUnits`、`trimScale`、`normalizeScale`、`transformScale` 等新函数，以及八种舍入模式。
- 🐛 **多项修复与改进**：修复了 `allocate`、`convert`、`isPositive`、`toDecimal` 和舍入等方面的多个问题，并更新了货币数据。
- 📚 **全新文档**：文档使用 VitePress 完全重写，包含核心概念指南、实用教程、完整 API 参考和交互式示例。

---

### [Bun v1.3.10 | Bun 博客](https://bun.com/blog/bun-v1.3.10)

**原文标题**: [Bun v1.3.10 | Bun Blog](https://bun.com/blog/bun-v1.3.10)

Bun 1.3.1 版本发布，带来了全新的原生 REPL、支持编译为独立 HTML 文件、完全支持 TC39 标准 ES 装饰器、多项性能优化（包括更快的 structuredClone、Buffer.slice 和 path.parse）、Windows ARM64 原生支持、捆绑器新增 Barrel 导入优化、事件循环改进、TLS 保持连接、根证书更新、JavaScriptCore 引擎升级，以及大量错误修复和 Node.js 兼容性改进。

- 🚀 **全新原生 REPL**：用 Zig 完全重写，启动迅速，支持语法高亮、多行输入、Tab 补全、持久历史记录和 Emacs 键绑定。
- 🌐 **编译为独立 HTML**：`bun build --compile --target=browser` 可将所有资源内联到单个 HTML 文件中，无需服务器即可运行。
- 🛠️ **支持 TC39 ES 装饰器**：完全支持 Stage 3 标准装饰器，包括 `accessor` 关键字、装饰器元数据和正确的求值顺序。
- ⚡ **多项性能提升**：`structuredClone` 对数组克隆快达 25 倍，`Buffer.slice()` 快约 1.8 倍，`path.parse()` 快 2.2-7 倍，字符串和正则表达式操作也得到优化。
- 🖥️ **Windows ARM64 支持**：可在 ARM64 Windows 设备上原生运行 Bun，并支持交叉编译为 ARM64 可执行文件。
- 📦 **捆绑器 Barrel 导入优化**：自动优化纯 Barrel 文件，仅解析实际使用的子模块，提升构建速度。
- 🔄 **事件循环与 TLS 改进**：macOS 和 Linux 上事件循环更快；自定义 TLS 配置现支持保持连接。
- 🔒 **安全与兼容性更新**：更新根证书；修复多个安全漏洞和 Node.js 兼容性问题。
- 🐛 **大量错误修复**：涵盖 `Bun.spawn()`、`bun install`、CSS 解析器、Bun Shell、TypeScript 类型和 Windows 平台等方面。

---

### [GitHub - tc39/proposal-decorators: ES6类装饰器提案 · GitHub](https://github.com/tc39/proposal-decorators)

**原文标题**: [GitHub - tc39/proposal-decorators: Decorators for ES6 classes · GitHub](https://github.com/tc39/proposal-decorators)

该提案旨在为JavaScript类引入装饰器语法，允许开发者通过装饰器扩展类及其成员的功能，同时保持语义一致性和静态可分析性。

- 🎯 **装饰器定义**：装饰器是函数，可在类、类成员等定义时调用，用于替换、访问或初始化被装饰的值。
- 🔄 **核心能力**：装饰器可替换具有相同语义的值、通过访问器共享值，或在值定义后运行初始化代码。
- 🏗️ **应用范围**：支持装饰类、类字段、方法、访问器及新增的自动访问器（`accessor`关键字）。
- 📜 **设计目标**：简化装饰器编写与使用，避免非局部副作用，确保装饰后的值类型可预测。
- ⚙️ **执行步骤**：装饰器按顺序求值、调用（接收值和上下文对象）和应用，最终影响类定义。
- 🛠️ **上下文对象**：包含被装饰值的类型、名称、访问方法、静态/私有标志及添加初始化器的功能。
- 🔧 **自动访问器**：新增`accessor`语法，默认生成getter/setter，装饰器可包装其访问行为。
- ⏱️ **初始化时机**：通过`addInitializer`方法，装饰器可在类或成员定义后运行自定义初始化逻辑。
- 🔗 **元数据侧信道**：装饰器可通过`access`对象实现依赖注入等高级模式，访问实例的最终值。
- 🚀 **标准化进展**：提案已进入Stage 3，完成规范文本，并在Babel等工具中提供实验性实现。
- 🔄 **与旧版对比**：相比Babel/TypeScript旧版装饰器，本提案更优化、语义更清晰，且兼容字段的`[[Define]]`语义。
- 📊 **静态可分析性**：装饰器行为可预测，有助于工具进行树摇和优化，提升运行时性能。
- ⏳ **发展历程**：TC39 经过多年迭代，基于过往提案元素形成当前设计，旨在填补 JavaScript 元编程的空白。

---

### [GitHub - webpro-nl/unbarrelify：适用于JavaScript与TypeScript项目的桶文件移除工具（仅限ESM）· GitHub](https://github.com/webpro-nl/unbarrelify/)

**原文标题**: [GitHub - webpro-nl/unbarrelify: Barrel file removal tool for JavaScript & TypeScript projects (ESM-only) · GitHub](https://github.com/webpro-nl/unbarrelify/)

unbarrelify 是一个用于 JavaScript 和 TypeScript 项目（仅限 ESM）的 barrel 文件移除工具，旨在通过自动重写导入路径来优化项目性能并避免因 barrel 文件引发的常见问题。

- 🚀 **自动重写导入**：将消费者文件中的导入从 barrel 文件直接指向源文件，提升模块加载效率。
- ⚠️ **避免性能问题**：解决 barrel 文件导致的性能下降、内存占用增加、tree-shaking 失效及循环依赖等问题。
- 🔧 **灵活配置选项**：支持通过 `--skip`、`--only` 等参数精确控制处理范围，并提供 `--check` 模式用于 CI 检查。
- 📄 **保留关键文件**：自动跳过作为入口点（如 `package.json#exports`）或根目录 `index.*` 的 barrel 文件，确保项目结构完整。
- 🛠️ **支持编程接口**：提供 Node.js API，便于集成到自定义脚本或构建流程中。
- 📚 **附带丰富资源**：文档中列举了多篇关于 barrel 文件弊端的文章，帮助用户理解优化动机。

---

### [精简你的 JavaScript 与 TypeScript 项目 | Knip](https://knip.dev/)

**原文标题**: [Declutter your JavaScript & TypeScript projects | Knip](https://knip.dev/)

Knip 是一款用于 JavaScript 和 TypeScript 项目的自动化工具，旨在通过检测和清理未使用的依赖、导出和文件来优化代码库，从而提升性能、减少维护负担并简化重构过程。

- 🧹 **清理未使用代码**：自动发现项目中未使用的文件、npm 依赖和 TypeScript 导出，帮助保持代码库整洁。
- 🔧 **智能分析机制**：基于项目实际使用的框架和工具，从精细的入口点进行高级分析，确保结果准确且可操作。
- 🛡️ **经过实战检验**：已被数千个项目采用，包括 Shopify 等知名团队，证明了其可靠性和有效性。
- 🔌 **丰富的插件生态**：提供 100 多个插件，支持 Astro、Cypress、Next.js、Vite 等主流工具和框架，易于集成。
- 🌐 **在线体验与支持**：提供在线 Playground 供用户试用，并设有详细的故障排除指南，帮助快速上手和解决问题。
- 📢 **广泛社区认可**：获得众多开发者和技术团队的高度评价，被誉为提升代码质量和项目维护效率的必备工具。

---

### [发布 v5.8.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.8.0)

**原文标题**: [Release v5.8.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.8.0)

Fastify 框架发布了 v5.8.0 版本，包含多项更新、修复和新功能，涉及文档改进、依赖升级、类型修复和性能优化等方面。

- 📝 更新了安全警告和文档样式，并移除了 HackerOne 相关引用
- 🔧 修复了路由选项共享问题，并支持 Pino v9 和 v10 日志库
- ⚡ 新增了处理程序级别的超时支持，提升了错误处理能力
- 📦 升级了多个依赖包，包括 borp 和 TypeBox，并更新了 CI 工作流
- 🐛 修复了类型定义和错误消息格式，优化了插件和钩子的异步支持
- 👥 欢迎了四位新贡献者加入项目，社区反应积极

---

### [feat: 由 kibertoad 实现处理程序级超时的一流支持 · Pull Request #6521 · fastify/fastify · GitHub](https://github.com/fastify/fastify/pull/6521)

**原文标题**: [feat: First-class support for handler-level timeouts by kibertoad · Pull Request #6521 · fastify/fastify · GitHub](https://github.com/fastify/fastify/pull/6521)

Fastify 框架新增了针对请求处理程序的一级超时支持，允许在服务器级别和路由级别配置超时，并通过 `request.signal` 提供 AbortSignal 以实现协作式取消。

- 🕐 新增 `handlerTimeout` 选项，支持在服务器和单个路由上配置应用级超时，与现有的套接字级超时不同，它适用于 HTTP 保持连接场景。
- ⚡ 默认值为 0（无超时），禁用时零开销，不创建 AbortController 或计时器，仅每个请求进行一次分支检查。
- 🛠️ 超时触发时返回 503 响应并中止 `request.signal`，但不会强制终止处理程序，允许处理程序利用该信号向下游 I/O 传播取消。
- 🔗 `request.signal` 统一处理超时和客户端断开连接，通过 `signal.reason` 区分原因（`FST_ERR_HANDLER_TIMEOUT` 或通用 `AbortError`）。
- 🧹 在所有退出路径（正常响应、错误、`reply.hijack()`、超时、客户端断开）中完整清理计时器和关闭监听器，避免资源泄漏。
- 📝 超时错误可通过路由的 `errorHandler` 自定义，允许按路由调整状态码和响应体。
- 🚫 若未配置 `handlerTimeout` 而访问 `request.signal`，将抛出 `FST_ERR_MISSING_HANDLER_TIMEOUT` 错误，防止误用。

---

### [Pino - Node.js 超高速全自然 JSON 日志记录器](https://getpino.io/)

**原文标题**: [Pino - Super fast, all natural JSON logger for Node.js](https://getpino.io/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 🧬 基于基因数据的 AI 模型可为患者提供个性化治疗方案，实现精准医疗
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [GramIO - 强大的 TypeScript/JavaScript Telegram 机器人 API 框架](https://gramio.dev/)

**原文标题**: [GramIO - Powerful Telegram Bot API framework for TypeScript/JavaScript | GramIO](https://gramio.dev/)

从零开始，30 秒内创建一个功能完整的 Telegram 机器人项目。

- ⚡ 使用 `npm create gramio@latest` 快速搭建项目脚手架
- 🛠️ 支持 TypeScript、ORM、代码检查等现代开发工具
- 🔌 可灵活选择插件和 Docker 配置
- 🚀 实现极速项目初始化和部署

---

### [Telegram Bot API](https://core.telegram.org/bots/api#march-1-2026)

**原文标题**: [Telegram Bot API](https://core.telegram.org/bots/api#march-1-2026)

Telegram Bot API 是一个基于 HTTP 的接口，允许开发者创建和管理 Telegram 机器人，支持发送消息、处理更新、管理聊天等功能，并持续更新以增加新特性如话题、礼物、付费媒体等。

- 🤖 **Bot API 简介**：基于 HTTP 的接口，用于创建 Telegram 机器人，需通过 BotFather 获取唯一令牌。
- 📅 **近期更新**：包括 Bot API 9.5（添加日期时间实体、标签管理）、9.4（自定义表情符号、话题功能）、9.3（私聊话题、礼物系统）等，增强机器人功能。
- 🔧 **请求与认证**：所有请求需通过 HTTPS，支持 GET/POST 方法，使用唯一令牌进行身份验证，响应为 JSON 格式。
- 🔄 **获取更新**：支持两种方式：`getUpdates`（长轮询）和 Webhooks（推送更新），可接收 JSON 序列化的 `Update` 对象。
- 🌐 **Webhook 设置**：通过 `setWebhook` 配置 URL 接收更新，支持自定义证书、IP 地址和秘密令牌，确保安全。
- 📁 **文件发送**：三种方式：通过 `file_id` 重用文件、HTTP URL 下载、multipart/form-data 上传，各有大小限制。
- 💬 **消息与格式**：支持发送文本、媒体、位置等多种消息，可使用 Markdown 或 HTML 格式化文本，包括粗体、链接等。
- 🛠 **聊天管理**：提供方法管理聊天成员、权限、邀请链接、话题（论坛），支持禁言、提升管理员等操作。
- 🎮 **游戏与支付**：机器人可发送 HTML5 游戏，处理支付（包括 Telegram Stars），支持发票、订阅和退款功能。
- 📊 **内联模式**：允许机器人在内联查询中返回结果，用户可直接从聊天界面选择并发送内容。
- 🔐 **Telegram Passport**：统一身份验证方法，机器人可请求和验证用户身份文档，确保数据安全。

---

### [mp3tag.js](https://mp3tag.js.org/)

**原文标题**: [mp3tag.js](https://mp3tag.js.org/)

mp3tag.js 是一个用于编辑音频文件元数据的开源 JavaScript 库，支持在 Node.js 和浏览器环境中运行，遵循 ID3 规范，并提供在线编辑器与完整文档。

- 🆓 开源免费：基于 MIT 许可证，源代码托管于 GitHub，可供所有人自由使用
- 🌐 多平台运行：通过 Babel 转译，兼容 Node.js 和浏览器环境（包括旧版浏览器）
- 📏 符合标准：严格遵循 ID3 规范，支持对用户输入进行标准化验证
- ✏️ 内置编辑器：提供可离线使用的在线编辑器演示，源代码已开源
- 📚 完整文档：提供详细的使用文档，方便开发者查阅与集成

---

### [GitHub - isaacs/sax-js: 适用于 JavaScript 的 SAX 风格解析器 · GitHub](https://github.com/isaacs/sax-js)

**原文标题**: [GitHub - isaacs/sax-js: A sax style parser for JS · GitHub](https://github.com/isaacs/sax-js)

这是一个用于解析 XML 和 HTML 的 SAX 风格解析器，主要设计用于 Node.js 环境，但也适用于浏览器或其他 CommonJS 实现。它支持流式处理，提供多种事件监听，并允许通过选项调整解析行为，如严格模式、格式化设置等。

- 📦 **SAX 风格解析器**：专为 XML 和 HTML 设计的流式解析工具，适用于 Node.js 和浏览器环境。
- ⚙️ **灵活配置**：支持严格模式、文本修剪、大小写转换等多种选项，以适应不同解析需求。
- 🔗 **事件驱动**：提供丰富的事件监听，如标签打开、属性解析、错误处理等，便于实时处理解析内容。
- 📄 **基础功能**：能处理 XML 实体、CDATA 块和命名空间，但不支持完整的 HTML 解析、DOM 构建或 XML 验证。
- 🛠️ **使用简便**：通过简单 API 即可进行解析，支持流式写入和管道操作，适合处理 RSS 等 XML 文档。

---

### [GitHub - panva/jose: 适用于 Node.js、浏览器、Cloudflare Workers、Deno、Bun 及其他 Web 互操作运行时的 JWA、JWS、JWE、JWT、JWK、JWKS 实现 · GitHub](https://github.com/panva/jose)

**原文标题**: [GitHub - panva/jose: JWA, JWS, JWE, JWT, JWK, JWKS for Node.js, Browser, Cloudflare Workers, Deno, Bun, and other Web-interoperable runtimes · GitHub](https://github.com/panva/jose)

这是一个名为“jose”的 JavaScript 模块，用于 JSON 对象签名与加密，支持 JWT、JWS、JWE、JWK 和 JWKS 等标准，适用于多种 Web 互操作性运行时环境。

- 🔐 提供完整的 JOSE 标准实现，包括 JWT 签名/验证、JWE 加密/解密以及 JWK 密钥管理
- 🌐 跨平台兼容，支持 Node.js、浏览器、Cloudflare Workers、Deno 和 Bun 等运行时
- 📦 零依赖且支持 Tree-shaking 的 ESM 模块，也可通过 CJS 方式在特定 Node 版本中使用
- 🔧 包含丰富的工具函数，如密钥导入导出、JWK 指纹计算和令牌头解码等
- 🛡️ 遵循多项 RFC 安全规范，并通过官方测试向量验证算法实现
- 📚 提供详细文档，支持通过 npm、JSR、jsDelivr 和 GitHub 多种渠道分发
- ⭐ 社区活跃，拥有 7.4k 星标，采用 MIT 开源协议，接受赞助支持持续维护

---

### [发布 v4.9.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.9.0)

**原文标题**: [Release v4.9.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.9.0)

NodeBB v4.9.0 版本发布，包含多项新功能、错误修复、性能优化和代码重构，主要涉及联邦功能增强、用户界面改进、权限管理调整及系统稳定性提升。

- 🚀 **新功能添加**：支持联邦内容摘要中的“[...]”魔法分隔符、新增话题跨发权限、允许用户配置未读消息截止时间、引入访客行动号召模板等。
- 🐛 **错误修复**：修复了 Webfinger 响应头设置、话题清除、缓存创建延迟、图片溢出等多项问题，提升了系统稳定性。
- ⚡ **性能优化**：减少每次话题加载时的用户 ID 获取调用、优化缓存检测逻辑、并行处理搜索任务，提升运行效率。
- 🔧 **代码重构**：将 ActivityPub 管理页面独立为顶级模块、重构表情符号替换代码、移除全局环境变量依赖，改善代码结构。
- 📚 **文档更新**：新增管理控制台路由、完善世界模式下的帖子对象模式、补充 OpenAPI 模式定义。
- 🧪 **测试完善**：更新测试以支持无标题话题、修复多项测试用例，确保功能可靠性。
- 🛠️ **其他改进**：包括用户界面调整（如通知控件改为切换开关）、翻译更新、依赖包升级等。

---

### [GitHub - avajs/ava: 让你充满信心地开发 Node.js 测试运行器 🚀 · GitHub](https://github.com/avajs/ava)

**原文标题**: [GitHub - avajs/ava: Node.js test runner that lets you develop with confidence 🚀 · GitHub](https://github.com/avajs/ava)

AVA 是一个面向 Node.js 的测试运行器，以其简洁的 API、详细的错误输出、对新语言特性的支持以及线程隔离为特点，旨在帮助开发者更自信地进行开发。它强调最小化与快速执行，支持并发测试运行，并提供了增强的断言信息和自动化的 CI 并行测试功能。

- 🚀 **简洁高效**：提供简单的测试语法，运行快速且支持并发测试，强制编写原子测试，无隐式全局变量。
- 🧪 **全面支持**：内置 TypeScript 定义，支持 Promise、异步函数和 Observable，提供增强的断言消息和 TAP 报告器。
- ⚙️ **易于使用**：通过 `npm init ava` 或手动安装即可快速设置，支持 ES 模块，提供监视模式以实时运行测试。
- 🔧 **高级功能**：包括“魔法断言”以显示代码摘录和差异对比，自动清理堆栈跟踪以快速定位错误，并在 CI 环境中自动检测并并行运行测试。
- 📚 **丰富文档**：提供详细的文档涵盖测试编写、断言、快照测试、配置等，并包含常见问题解答和实用配方。
- 🌍 **社区活跃**：拥有多语言翻译、相关工具支持（如 ESLint 插件、TypeScript 集成），以及活跃的团队和贡献者社区。

---

### [设置 Next.js 源映射 - 可读堆栈跟踪 | Sentry](https://blog.sentry.io/setting-up-next-js-source-maps-sentry/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjs&utm_content=newsletter-classified-listing-blog-sourcemaps-learnmore)

**原文标题**: [Setting up Next.js source maps - Readable stack traces | Sentry](https://blog.sentry.io/setting-up-next-js-source-maps-sentry/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjs&utm_content=newsletter-classified-listing-blog-sourcemaps-learnmore)

本文介绍了如何在 Next.js 应用中配置 Sentry 以正确上传和使用源映射，从而在错误追踪中显示原始代码而非混淆后的代码块，并提供了调试和验证步骤。

- 🛠️ Next.js 构建流程会将源代码编译、压缩并分割成代码块，这有利于性能但不利于调试。
- 🔗 源映射和调试 ID 能将混淆后的代码映射回原始文件，Sentry 利用它们还原可读的堆栈跟踪。
- 🖥️ 开发环境中浏览器可直接访问源映射，但 Sentry 需要上传源映射才能显示原始代码。
- 🚀 建议使用 Spotlight 进行本地调试，避免开发噪声占用 Sentry 配额，将 Sentry 专注于生产环境问题。
- 📦 通过运行`npm run build`和`npm run start`模拟生产构建，触发 Sentry 自动上传源映射。
- 🔄 Sentry 在构建过程中收集并上传源映射，之后将其从构建输出中删除，避免泄露源代码。
- ✅ 验证源映射是否生效：在生产模式下触发错误，检查 Sentry 中的堆栈跟踪是否指向原始文件。
- ⚙️ 若源映射未生效，需检查 Sentry 配置、环境变量，并尝试删除旧源映射后重新构建上传。
- 📚 如遇问题，可参考 Next.js 源映射文档和故障排除指南，或通过 Discord 等渠道获取帮助。

---

### [学习 Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

**原文标题**: [Learn Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 🧬 基于基因数据的 AI 模型可为患者提供个性化治疗方案，实现精准医疗
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [获取失败](https://nodeweekly.com/link/181587/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/181587/web)

无法总结：获取内容失败，状态码 403。

---

### [npmx - npm 注册表的包浏览器](https://npmx.dev/)

**原文标题**: [npmx - Package Browser for the npm Registry](https://npmx.dev/)

npmx 是一个专为 npm 注册表设计的快速现代浏览器，提供即时搜索功能，支持多种前端框架，并鼓励社区参与贡献。

- 🔍 **即时搜索功能** – 提供快速搜索 npm 包的能力，可随时开启或关闭
- 🛠️ **多框架支持** – 兼容 Nuxt、Vue、React、Svelte、Next.js 等多种流行前端框架和工具
- 📅 **持续更新** – 最新版本 v0.2.2 于 2026 年 3 月 3 日发布
- 🤝 **社区参与** – 鼓励用户通过 GitHub 贡献代码，加入 Discord 社区交流，并通过 Bluesky 获取最新动态

---

### [发布 npmx：一款快速、现代的 npm 注册表浏览器](https://npmx.dev/blog/alpha-release)

**原文标题**: [Announcing npmx: a fast, modern browser for the npm registry](https://npmx.dev/blog/alpha-release)

npmx 是一个为 npm 注册表设计的快速、现代浏览器，旨在通过提供包大小、模块格式等关键数据，帮助开发者更高效地搜索、评估和管理 npm 包。该项目强调社区协作，自启动以来吸引了大量贡献者，并集成了社交功能和多语言支持，未来计划基于用户反馈持续改进。

- 🚀 **快速高效的包浏览**：提供 npm 包的快速搜索和详细数据（如安装大小、模块格式），帮助开发者高效决策。
- 🌍 **强大的社区驱动**：项目启动后迅速吸引全球 105 多名贡献者，通过开放协作构建了活跃的多元社区。
- 🔧 **实用功能集成**：支持下载统计、过时依赖警告、JSR 交叉引用等功能，并可直接从 README 启动 StackBlitz 等演示环境。
- 🌐 **国际化与可访问性**：提供 19 种语言、明暗主题及键盘友好设计，注重用户体验和包容性。
- 🤝 **社交与协作特性**：内置包点赞和社交功能，强调开源项目中人与人的连接，鼓励社区参与。
- 📈 **持续发展愿景**：目前处于 Alpha 阶段，积极收集用户反馈以迭代产品，目标是为 JavaScript 生态提供更好的包管理体验。

---

### [投资组合](https://www.dhzdhd.dev/blog/gleam-executable)

**原文标题**: [Portfolio](https://www.dhzdhd.dev/blog/gleam-executable)

本文介绍了将 Gleam 应用打包成单一可执行文件的多种方法，包括针对 Erlang 和 JavaScript 目标的不同工具链，并比较了它们的优缺点。

- 🛠️ **Gleam 项目创建**：通过`gleam new`创建项目，并使用`gleam build`指定 Erlang 或 JavaScript 目标进行构建。
- 🐭 **Erlang 目标：Gleescript**：通过添加`gleescript`依赖并运行相应命令生成 escript，但需目标机器安装 Erlang 虚拟机。
- 🌯 **Erlang 目标：Burrito**：可将 Elixir/Erlang 项目打包为自包含可执行文件，无需 Erlang 虚拟机，但需进一步适配 Gleam。
- 🦕 **JavaScript 目标：Deno 编译**：使用 Deno 内置的`deno compile`命令，需先用 ESbuild 等工具将 Gleam 生成的 JavaScript 代码打包为单个文件。
- 📦 **JavaScript 目标：Node SEA**：Node.js 的实验性功能，需通过复杂步骤配置并注入代码到 Node 二进制文件，目前兼容性和易用性较差。
- 🚀 **JavaScript 目标：Bun 编译**：使用`bun build --compile`快速打包并编译为可执行文件，操作简便且速度极快，但文件体积较大。
- ⚙️ **其他工具：Nexe**：可将 Node.js 应用编译为单文件，但文中未深入测试其在 Gleam 项目中的适用性。
- 📊 **总结对比**：Bun 在速度和易用性上表现最佳，但 Deno 和 Bun 生成的可执行文件体积较大；Gleescript 依赖外部环境，而 Node SEA 目前不够稳定。

---

### [重新利用你的旧 Kindle](https://www.mariannefeng.com/portfolio/kindle/)

**原文标题**: [Repurpose your old Kindle](https://www.mariannefeng.com/portfolio/kindle/)

本文介绍了如何将旧款 Kindle Touch 改装成实时公交信息显示屏，通过自定义服务器获取数据并每分钟刷新，同时支持通过菜单键退出仪表盘模式。

- 🛠️ **越狱与安装工具**：首先根据 Kindle 型号和固件版本进行越狱，随后安装 KUAL 启动器和 MRPI 插件管理器，过程中需注意操作顺序并禁用 OTA 更新。
- 🔗 **配置 SSH 连接**：通过 USBNetwork 扩展启用 SSH 功能，使 Kindle 能像普通服务器一样被远程访问，便于后续自定义代码的运行。
- 🖥️ **搭建图像生成服务器**：创建服务器端点，利用 NJTransit 的 GraphQL 接口获取公交数据，并通过 wkhtmltoimage 将 HTML 转换为适配 Kindle 屏幕分辨率的 PNG 图像。
- 📱 **开发 KUAL 自定义应用**：编写 KUAL 扩展脚本，实现仪表盘的启动、定时刷新和菜单键退出功能，其中使用 rtcwake 管理设备休眠以优化电池续航。
- 🔄 **优化与改进思考**：针对长期使用出现的屏幕残影和电池续航问题（目前约 5 天），作者计划尝试夜间清屏策略并调整刷新间隔以进一步提升体验。

---

### [GitHub - louislam/uptime-kuma: 一款精美的自托管监控工具 · GitHub](https://github.com/louislam/uptime-kuma)

**原文标题**: [GitHub - louislam/uptime-kuma: A fancy self-hosted monitoring tool · GitHub](https://github.com/louislam/uptime-kuma)

Uptime Kuma 是一款易于使用的自托管监控工具，提供丰富的监控功能和通知服务，支持多种安装方式，并拥有活跃的社区支持。

- 🚀 **功能丰富**：支持监控 HTTP(s)、TCP、Ping、DNS 等多种协议，提供 20 秒间隔的实时监测和多种通知方式（如 Telegram、Discord、邮件等）。
- 🐳 **便捷安装**：可通过 Docker Compose 或 Docker 命令快速部署，也支持非 Docker 环境（需 Node.js >= 20.4）。
- 🌐 **多语言与状态页**：支持多语言界面，可创建多个状态页面并映射到特定域名。
- 📊 **可视化界面**：提供响应式 UI、Ping 图表、证书信息显示，并支持浅色/深色模式。
- 🔄 **更新与维护**：提供详细的更新指南，项目通过 GitHub Issues 和 Reddit 社区进行问题讨论与支持。
- ❤️ **开源与贡献**：采用 MIT 许可证，鼓励用户通过提交 PR、测试版本或协助翻译等方式参与贡献。
- 🛠️ **高级功能**：支持代理、2FA、反向代理配置，并兼容主流 Linux 发行版和 Windows 系统。

---

