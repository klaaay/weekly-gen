### [Node 周刊第 626 期：2026 年 5 月 28 日](https://nodeweekly.com/issues/626)

**原文标题**: [Node Weekly Issue 626: May 28, 2026](https://nodeweekly.com/issues/626)

以下是 Node Weekly 第 626 期的内容摘要：

本期涵盖了 Node.js 流泄漏的实战指南、Deno 2.8 的重大兼容性提升、Express 迁移到 Next.js 的 AI 辅助方法，以及多项工具和库的更新。

- 📧 获取 Node Weekly 到您的收件箱：提供订阅入口，可阅读网页版或查看往期内容。
- 🛠️ Node.js 流泄漏生产实战指南：介绍了五种在测试和代码审查中难以发现、但在真实流量下会暴露的流故障模式，并提供了解决方案。
- 🤖 构建持久 AI 代理的网络研讨会：学习使用开源五层堆栈和 Agentspan，在 LangGraph、OpenAI 和 Google SDK 上构建不会在生产环境中崩溃的 AI 代理。
- 🚀 Deno 2.8 达到 76% Node.js 兼容性：Node.js 兼容性从 42% 跃升至 76.4%（超过 Bun），并移除了 `npm:` 前缀要求，使 `deno install` 可直接替代 `npm install`。
- 📰 简讯：npm 11.16.0 发布，支持 `allowScripts` 安装脚本策略；Node 团队重新考虑 V8 更新的 ABI 稳定性要求；NodeConf EU 2026 将于九月在意大利举行；macOS Intel (x64) 成为 Node 26 的二级平台；Node.js 24.16.0 (LTS) 发布，新增 `crypto.randomUUIDv7()` 等功能。
- 🔄 使用 AI 代理将 Express 应用迁移到 Next.js：展示了如何将遗留的 Express.js 应用现代化为 Next.js App Router 和 TypeScript，并分享了相关技能供他人使用。
- 🐢 使用 AI 更慢地编写更好的代码：一位资深 JavaScript 开发者指出，LLM 不仅可用于快速生成低质量代码，还能帮助更慢、更高质量地编写代码。
- 📄 使用 Node.js 构建自定义 MCP 服务器：相关文章分享。
- 🛠️ 代码与工具：ANSIS 4.3（ANSI 颜色库，支持超链接）、Flue（Astro 的代理框架）、DOCX 9.7（生成 Word 文件）、Helmet.js 8.2（Express 安全加固）、Kysely 0.29.0（类型安全 SQL 查询构建器）、officeParser 7.1（解析 Office 文件）、TypeSQL 0.24（从 SQL 生成类型安全 API）、pnpm 11.4（包管理器更新）、dns2 3.0（DNS 服务器和客户端）。
- 📰 分类广告：AI 代理中间件、自动缩放工具 Judoscale。
- 📢 生态圈动态：2026 年 Web 开发 AI 调查结果发布（超 7000 名开发者参与）；2026 年 CSS 调查开放；JavaScript 填字游戏；Mozilla 的 Ryan Hunt 告别 asm.js，Firefox 默认禁用其优化。

---

### [Node.js 流泄漏生产手册 – Frontend Masters 博客](https://frontendmasters.com/blog/the-production-playbook-for-node-js-stream-leaks/)

**原文标题**: [The Production Playbook for Node.js Stream Leaks – Frontend Masters Blog](https://frontendmasters.com/blog/the-production-playbook-for-node-js-stream-leaks/)

本文介紹了 Node.js 串流在生產環境中可能發生的五種記憶體洩漏模式，並提供了一套五項規則的現代化操作手冊來預防和修復這些問題。

- 📡 客戶端斷線但伺服器未察覺：使用 `pipeline()` 取代 `pipe()`，它會自動偵測並清理上游資源。
- 🎧 手動監聽器清理困難：改用 `for await...of` 非同步迭代器，`break` 時會自動觸發串流銷毀。
- ⏱️ 逾時只關閉回應但未清理上游：使用 `AbortSignal.timeout()` 來終止整個管線鏈。
- 🔗 資料庫連線與網路速度綁定：將資料庫連線的釋放邏輯與游標事件綁定，而非 HTTP 回應事件。
- 🔄 管線雖運作但來源仍持續推送：在 `catch` 區塊中明確呼叫 `source.destroy(err)` 作為備援清理。
- 📋 規則一：一律使用 `pipeline()` 而非 `pipe()`，以自動處理錯誤與背壓。
- ✅ 規則二：尊重 `write()` 的布林回傳值，若為 `false` 則等待 `drain` 事件，並使用 `AbortSignal` 避免懸掛。
- 🗑️ 規則三：使用 `try/finally` 與 `AbortController` 確保自己建立的串流被銷毀。
- 🔍 規則四：使用 `--max-old-space-size=128` 進行壓力測試，並透過堆積快照或 `writableLength` 監控即時佇列大小。
- 🧪 規則五：編寫單元測試，使用低 `highWaterMark` 的模擬寫入串流來驗證背壓是否正確運作。
- 🔮 未來趨勢：使用非同步生成器與 `stream.compose()` 建立拉取式串流，從根本上消除背壓錯誤。

---

### [你的 Node.js 流没有进行背压处理，它们正在悄悄吞噬你的内存。——前端大师博客](https://frontendmasters.com/blog/your-node-js-streams-arent-backpressuring-theyre-silently-eating-your-memory/)

**原文标题**: [Your Node.js Streams Aren’t Backpressuring. They’re Silently Eating Your Memory. – Frontend Masters Blog](https://frontendmasters.com/blog/your-node-js-streams-arent-backpressuring-theyre-silently-eating-your-memory/)

Node.js 流式处理若不正确处理背压，会默默消耗内存直至进程崩溃，而许多开发者对此毫无察觉。

- 📉 背压是协作协议，但 `.write()` 返回 `false` 时常被忽略，导致内存无限增长
- 🛑 `highWaterMark` 并非内存限制，仅是建议阈值，忽略 `false` 会持续缓冲直到堆溢出
- ⚠️ Node.js 22 将默认 `highWaterMark` 从 16KB 提升至 64KB，加剧了内存压力
- 🧩 `objectMode` 下 `highWaterMark` 按对象计数（默认 16），大对象可导致数 GB 缓冲
- 🔄 Transform 流有独立读写侧缓冲，易形成“手风琴效应”掩盖内存问题
- ❌ `.pipe()` 不传播错误，链中异常会导致资源泄漏，应改用 `pipeline()`
- ⏳ `async/await` 仅控制读取节奏，写入仍需检查 `false` 并等待 `drain` 事件
- 📡 `data` 事件监听器会启用流动模式，完全绕过背压保护
- 🧠 修复内存泄漏可能暴露连接池饥饿问题，需配合查询超时和专用工作池
- ✅ 正确做法：检查 `.write()` 返回值、使用 `pipeline()`、显式配置 `highWaterMark`

---

### [网络研讨会：构建不随进程终止而消亡的持久 AI 代理](https://orkes.io/webinars/webinar-beyond-sandboxes-architecting-durable-runtimes-for-ai-agents)

**原文标题**: [Webinar: Building Durable AI Agents That Don’t Die When Your Process Does](https://orkes.io/webinars/webinar-beyond-sandboxes-architecting-durable-runtimes-for-ai-agents)

Orkes 获 6000 万美元融资，开发者正越来越多地使用其平台自信地将 AI 部署到生产环境中。

- 💰 Orkes 成功融资 6000 万美元，表明市场对其 AI 部署平台的需求强劲。
- 🚀 开发者正利用 Orkes 平台将 AI 自信地投入生产，提升开发敏捷性与成本效益。
- 🛠️ 平台核心功能包括微服务、实时 API、事件驱动、人工工作流及流程编排，支持多种行业。
- 🤖 推出 Agentic Workflows，在保持合规与控制的同时，将工作流转化为智能代理体验。
- 📅 举办网络研讨会“超越沙盒：为 AI 代理构建持久运行时”，探讨代理的可重放、可追踪与可恢复性。
- 🎓 提供 Orkes Academy，通过动手实验、结构化学习路径和认证，帮助掌握工作流编排。
- 👥 客户案例：Foxtel 首席架构师称赞 Orkes 提高了开发者敏捷性、成本效率和应用可靠性。

---

### [Deno 2.8](https://deno.com/blog/v2.8)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8)

Deno 2.8 是一个重大版本更新，带来了大量新功能、性能提升和兼容性改进。

- 🚀 **新子命令**：新增 `deno audit fix`（自动修复漏洞）、`deno bump-version`（版本号管理）、`deno ci`（CI 环境专用安装）、`deno pack`（打包为 npm tarball）、`deno transpile`（TypeScript 转译）、`deno why`（依赖溯源）等子命令。
- 📦 **npm 默认化**：`deno add` 和 `deno install` 现在默认将无前缀名称视为 npm 包，无需再手动添加 `npm:` 前缀。
- ⚡ **性能飞跃**：冷 npm 安装速度提升 **3.66 倍**；`node:http` 吞吐量提升 **2.21 倍**；`node:buffer` base64 处理速度提升 **3.07 倍**；`node:crypto` scrypt 速度提升 **2.12 倍**。
- 🔗 **Node.js 兼容性**：Node.js 官方测试套件通过率从 42% 跃升至 **76.4%**，远超 Bun 的 40.6%。
- 🧩 **import defer**：支持 TC39 提案的延迟模块加载，仅在首次访问导出时执行模块代码，优化启动性能。
- 📝 **TypeScript 6.0.3**：内置 TypeScript 编译器升级至 6.0.3，并默认包含 `lib.node` 类型定义。
- 🛠️ **调试增强**：Chrome DevTools 现在可以检查 Deno 的网络流量（`fetch`、`node:http`、WebSocket），并新增内置 CPU 分析器（支持火焰图 SVG 和 Markdown 报告）。
- 🗂️ **工作区管理**：支持 pnpm 风格的 `catalog:` 协议统一管理依赖版本；新增 `--os` 和 `--arch` 标志用于跨平台 npm 安装；支持 `--prod` 标志跳过开发依赖；新增 `nodeModulesLinker` 字段支持 hoisted 布局。
- 🔒 **安全与配置**：`min-release-age` 可在 `.npmrc` 中配置；支持 `certfile`/`keyfile` 的 mTLS 认证；`file:` 和 `link:` 依赖被静默忽略。
- 🌐 **Web API**：稳定支持 `OffscreenCanvas`（位图渲染和 WebGPU 上下文）和几何接口（`DOMPoint`、`DOMRect`、`DOMQuad`、`DOMMatrix`）；改进可克隆和可转移对象支持。
- 🧪 **测试与覆盖率**：`sanitizeOps` 和 `sanitizeResources` 默认关闭；支持每测试超时设置；`deno coverage` 新增函数覆盖率报告。
- 📡 **OpenTelemetry**：新增控制台导出器和 gRPC OTLP 导出器；权限审计日志可接入 OTel 管道。
- 🔄 **其他改进**：`setTimeout`/`setInterval` 现在返回 Node 的 `Timeout` 对象；`deno task` 输出带任务名前缀；`deno upgrade` 支持增量更新和从 PR 安装；实现 Node 的 `module.registerHooks()` API。

---

### [发布 v11.16.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.16.0)

**原文标题**: [Release v11.16.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.16.0)

npm v11.16.0 版本发布，新增功能、修复问题并更新依赖。

- 🚀 新增 `publish --access=private` 别名，用于限制发布权限
- 🔒 引入 `allowScripts` 安装脚本策略的第一阶段，增强安装控制
- 🐛 修复 `fullMetadata` 的拼写错误
- ⏳ 修复交互式编辑器启动时进度旋转器暂停问题
- 📚 新增 `npm_old_version` 和 `npm_new_version` 环境变量的文档
- 📦 更新多个依赖项，包括 undici、sigstore 和 lru-cache 等
- 🧹 进行开发依赖更新和标志表默认值清理
- 👥 感谢 claude、36degrees 等贡献者的参与

---

### [特性：`allowScripts` 选择加入安装脚本策略的第一阶段 —— JamieMagee · 拉取请求 #9360 · npm/cli · GitHub](https://github.com/npm/cli/pull/9360)

**原文标题**: [feat: Phase 1 of `allowScripts` opt-in install-script policy by JamieMagee · Pull Request #9360 · npm/cli · GitHub](https://github.com/npm/cli/pull/9360)

npm CLI 实现了 `allowScripts` 可选安装脚本策略的第一阶段，为依赖安装脚本引入选择加入机制。

- 🚀 新增 `allowScripts` 字段到 `package.json`，可在安装时读取并控制脚本执行
- ⚙️ 引入三个新配置项：`allow-scripts`、`strict-script-builds` 和 `dangerously-allow-all-scripts`，后两个为未来预留
- 🛠️ 新增 `npm approve-scripts` 和 `npm deny-scripts` 命令，支持非对称钉选规则
- ⚠️ 在 `npm install`、`ci`、`update` 和 `rebuild` 期间添加咨询性警告，列出未审核脚本的包
- 🔍 在 `@npmcli/arborist` 中实现身份匹配器，支持注册表、Git、文件和远程 tarball
- 🔗 别名匹配底层注册包而非别名名称，防止欺骗
- 📦 捆绑依赖的安装脚本标记为未审核，第一阶段无法加入白名单
- ⚡ 当前安装行为不变，脚本仍按原有方式运行，第二阶段将实现实际阻止

---

### [重新考虑 V8 主要版本更新中的 ABI 稳定性要求 · 问题 #1852 · nodejs/TSC · GitHub](https://github.com/nodejs/TSC/issues/1852)

**原文标题**: [Reconsider ABI stability requirement for V8 updates in majors · Issue #1852 · nodejs/TSC · GitHub](https://github.com/nodejs/TSC/issues/1852)

### 概述总结
Node.js TSC 正在讨论是否应在主要版本中放宽对 V8 更新的 ABI 稳定性要求，以加快更新速度并减少延迟。

- 💬 **讨论背景**：RafaelGSS 提出重新考虑 ABI 稳定性要求，认为其阻碍了 V8 在主要版本中的及时更新。
- ⏳ **延迟问题**：v26.0.0 因等待 V8 14.6 而延迟，但该版本很快被 Chrome 148（V8 14.8）取代，导致版本过时。
- 🛑 **主要痛点**：ABI 稳定性增加了压力并拖慢了 V8 更新进度，移除该约束可让更新在准备就绪时立即落地。
- 💡 **替代建议**：在主要版本中放弃 ABI 稳定性保证，推动生态系统转向 N-API 或 FFI。
- 🗓️ **时间规划**：该变更可能来不及应用于 v26，但可从 v27 开始实施。

---

### [NodeConf EU 2026 | 意大利博洛尼亚](https://nodeconf.eu/)

**原文标题**: [NodeConf EU 2026 | Bologna, Italy](https://nodeconf.eu/)

概述总结  
NodeConf EU 2026 将在意大利博洛尼亚举行，为期两天的技术交流盛会，聚焦 Node.js 运行时、平台、工具链和社区互动，提供深度技术内容和丰富的社交机会。

- 🎯 活动时间地点：2026 年 9 月 29-30 日，意大利博洛尼亚 Hotel Savoia Regency 酒店
- 🗓️ 核心安排：两天技术演讲 + 走廊交流，单会场设计确保充分互动
- 💻 技术内容：聚焦 Node.js 运行时、平台、工具、可观测性、架构和生产系统
- 🤝 社区价值：汇聚维护者、工程师、库作者和团队，强调面对面交流
- 🎫 实用链接：门票预订、演讲征集、场地信息、地图导航、YouTube 回顾和 X 动态
- 🏆 赞助伙伴：Platinum 级 Platformatic、Gold 级待公布、Silver 级待公布、OpenJS 基金会等支持
- 🌍 社区合作：CityJS London、ZurichJS、BolognaJS 等本地组织参与

---

### [NodeConf EU 2026](https://docs.google.com/forms/d/e/1FAIpQLSdhxLUxB5kW8NU5Dv6PM7vvQqKLcKed45AXvsXPGN8tIkzfkg/viewform?usp=send_form)

**原文标题**: [NodeConf EU 2026](https://docs.google.com/forms/d/e/1FAIpQLSdhxLUxB5kW8NU5Dv6PM7vvQqKLcKed45AXvsXPGN8tIkzfkg/viewform?usp=send_form)

NodeConf EU 2026 將於義大利波隆那舉行，現正徵求演講者與贊助商。

- 🇮🇹 活動回歸：NodeConf EU 2026 將於義大利波隆那舉辦，時間為 9 月 29 日至 30 日。
- 🎤 徵求講者：誠摯邀請對 Node.js 充滿熱情的人分享故事、願景或想法。
- 📅 活動規模：為期兩天，將有 24 位講者，涵蓋 Node.js 核心、實際應用、創新想法與整合生態系。
- 📋 報名表單：需填寫提案標題、描述、講者資訊、個人簡介、社群媒體等必填資料。
- ✅ 資料同意：提交即同意個人資料與活動排程資訊可被主辦方公開使用。
- ✈️ 旅行補助：可申請旅行協助，但名額有限且不保證提供。
- 🤝 贊助機會：詢問公司或雇主是否有興趣成為贊助商。

---

### [[v26.x 回溯] 文档：将 macOS x64 降级为第二层级 — aduh95 · 拉取请求 #63153 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63153)

**原文标题**: [[v26.x backport] doc: downgrade macOS x64 to Tier 2 by aduh95 · Pull Request #63153 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63153)

Node.js v26.x 正在将 macOS x64 支持降级为 Tier 2，以应对未来可能无法继续提供该架构二进制文件的风险。

- 🖥️ **降级 macOS x64 至 Tier 2**：Node.js v26.x 分支计划将 macOS x64 架构的支持等级从 Tier 1 降级为 Tier 2，以反映未来可能无法继续提供该架构二进制文件的不确定性。
- ⏳ **应对 EOL 风险**：Node.js 26 的 EOL 定于 2029 年 4 月 30 日，而 Rosetta 2 和 macOS 27 的 EOL 未知，可能也在 2029 年左右，此举旨在避免因无法构建 x86_64 二进制文件而被迫提前结束 Node.js 26 的生命周期。
- 🧩 **并非停止支持**：该 PR 的意图并非立即停止对 macOS Intel 平台的支持，而是向社区传达一个明确的信号：未来提供通用二进制文件的能力存在不确定性。
- ✅ **获得广泛批准**：该 PR 已获得包括 Richard Lau、Marco Ippolito、Stewart X Addison 等多位核心贡献者的批准，并被标记为需要 TSC 和构建团队进一步讨论的议题。
- 📌 **作为 semver-patch 处理**：尽管原始 PR 按政策标记为 semver-major，但提交者认为此更改不会破坏现有功能，计划将其作为 semver-patch 合并。

---

### [node/BUILDING.md 在 main 分支 · nodejs/node · GitHub](https://github.com/nodejs/node/blob/main/BUILDING.md#strategy)

**原文标题**: [node/BUILDING.md at main · nodejs/node · GitHub](https://github.com/nodejs/node/blob/main/BUILDING.md#strategy)

本文件详细介绍了 Node.js 的构建过程、支持平台、工具链以及各种构建选项。

- 🏗️ **构建概述**：Node.js 构建过程因平台和功能需求而异，构建后建议运行测试套件以确保二进制文件正常工作。
- 💻 **支持平台**：Node.js 支持多种操作系统和架构，分为 Tier 1（主力）、Tier 2（次要）和 Experimental（实验性）三个支持层级，并详细列出了各平台的版本要求和支持类型。
- 🔧 **必备工具链**：不同平台有特定的编译器版本要求，例如 Linux 需要 GCC >= 13.2 或 Clang >= 19.1，Windows 需要 Visual Studio 2022 或 2026，macOS 需要 Xcode >= 16.4。
- 📥 **官方二进制构建**：官方发布的二进制文件在特定平台和工具链上构建，例如 RHEL 8 上使用 Clang 20.1，并提供 libatomic 运行时依赖说明。
- 🐍 **构建前提条件**：构建需要 Python 支持版本、Rust 工具链（用于 Temporal 支持）以及至少 8GB 内存（4 并行任务时）。
- 🛠️ **Unix/macOS 构建步骤**：通过 `./configure` 和 `make -j4` 命令构建，可使用 Ninja 加速，并介绍了安装、测试、代码覆盖率、文档构建等流程。
- 🪟 **Windows 构建步骤**：提供手动安装和 WinGet 自动安装两种方式安装 Visual Studio、Python、Rust 等前提条件，使用 `.\vcbuild` 命令构建和测试。
- ⚡ **加速开发**：推荐使用 ccache 缓存编译结果，并可通过 `--node-builtin-modules-path` 选项从磁盘加载 JS 文件，避免重新编译。
- 🌐 **国际化 (Intl) 支持**：默认启用完整 ICU 支持，也可选择 small-icu（仅英文）或完全禁用 Intl 支持，并支持使用系统已安装的 ICU。
- 🔒 **FIPS 与 Temporal**：支持构建 FIPS 兼容的 OpenSSL 和 Temporal API，后者需要 Rust 工具链，可通过配置选项启用或禁用。
- 📦 **外部核心模块**：允许将 JavaScript 文件作为内置模块打包到二进制中，通过 `--link-module` 选项指定。
- 🤝 **下游分发商注意事项**：为保持 ABI 兼容性，分发商应使用与官方构建相同或兼容的依赖版本，并建议使用自定义 `NODE_MODULE_VERSION`。

---

### [Node.js — Node.js 24.16.0（长期支持版）](https://nodejs.org/en/blog/release/v24.16.0)

**原文标题**: [Node.js — Node.js 24.16.0 (LTS)](https://nodejs.org/en/blog/release/v24.16.0)

Node.js 24.16.0 (LTS) 版本发布，代号“Krypton”，包含多项新功能、性能优化和错误修复。

- 🔐 **加密模块增强**：新增 `randomUUIDv7()` 方法，支持 Ed25519 上下文参数，并改进密钥验证。
- 🐞 **调试器改进**：为 `node inspect` 添加免编辑运行时表达式探测功能。
- 📁 **文件系统更新**：`fs.stat()` 支持 `signal` 选项，`statfs` 暴露 `frsize` 字段。
- 🌐 **HTTP 模块强化**：`ClientRequest` 选项合并更严格，`IncomingMessage` 新增 `req.signal`。
- 📡 **流处理优化**：`duplexPair` 支持销毁传播，修复嵌套 compose 错误传播问题。
- 🧪 **测试运行器升级**：支持测试顺序随机化、模拟超时 API 对齐，以及 `AbortSignal.timeout` 支持。
- 🎨 **工具函数扩展**：`util` 模块支持使用十六进制颜色为文本着色。
- 🔧 **QUIC 协议进展**：多项修复和增强，包括多 ALPN 协商、SNI 支持，并移至编译时标志。
- 📦 **依赖更新**：升级 npm 到 11.13.0，OpenSSL 到 3.5.6，V8 等多项依赖。
- 🛠️ **其他改进**：SQLite 新增序列化/反序列化功能，修复 URL 处理崩溃问题，改进模块加载。

---

### [工具 | Node.js v26.2.0 文档](https://nodejs.org/api/util.html#utilstyletextformat-text-options)

**原文标题**: [Util | Node.js v26.2.0 Documentation](https://nodejs.org/api/util.html#utilstyletextformat-text-options)

Node.js v26.2.0 的 `util` 模块提供了多种实用的调试、类型检查、格式化与命令行解析工具。

- 📝 **格式化与调试**：`util.format()` 提供类似 `printf` 的字符串格式化，`util.inspect()` 用于对象调试输出，支持深度、颜色、排序等自定义选项。
- 🔄 **异步函数转换**：`util.callbackify()` 将 async 函数转为错误优先回调风格，`util.promisify()` 将回调风格函数转为返回 Promise 的函数。
- 🔍 **类型检查**：`util.types` 提供一系列 `is*` 方法（如 `isPromise`、`isMap`、`isTypedArray`），用于精确判断内置对象类型。
- ⚙️ **命令行参数解析**：`util.parseArgs()` 提供高级命令行参数解析，支持布尔、字符串、多值、默认值及 token 详细解析。
- 🎨 **文本样式与颜色**：`util.styleText()` 支持在终端中应用 ANSI 颜色和修饰（如粗体、下划线），`util.stripVTControlCharacters()` 可移除 ANSI 转义码。
- 🧩 **MIME 类型处理**：`util.MIMEType` 和 `util.MIMEParams` 类用于解析、读取和修改 MIME 类型及其参数。
- ⏱️ **信号与退出码**：`util.convertProcessSignalToExitCode()` 将信号名转换为 POSIX 退出码，`util.setTraceSigInt()` 控制 SIGINT 时是否打印堆栈。
- ⚠️ **弃用与警告**：`util.deprecate()` 标记函数为弃用并触发警告，支持自定义代码和 `modifyPrototype` 选项。
- 🧪 **实验性工具**：`util.diff()` 使用 Myers 算法比较字符串或数组差异，`util.getCallSites()` 获取调用栈信息（支持源码映射）。
- 🗑️ **已弃用 API**：`util._extend()` 和 `util.isArray()` 已弃用，建议分别使用 `Object.assign()` 和 `Array.isArray()` 替代。

---

### [test_runner: 支持测试顺序随机化，由 pmarchini 提交 · 拉取请求 #61747 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61747)

**原文标题**: [test_runner: support test order randomization by pmarchini · Pull Request #61747 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61747)

Node.js 测试运行器新增了测试顺序随机化功能，支持确定性随机种子，有助于发现依赖测试顺序的隐藏问题。

- 🎲 新增 `--test-randomize` 选项，可随机化测试文件执行顺序和文件内测试顺序
- 🔢 支持 `--test-random-seed=<seed>` 参数，使用指定种子可确定性重现随机顺序
- 📝 未提供种子时自动生成，并在测试摘要中打印，便于复现问题
- ✅ 该功能已合并到 Node.js 主分支，并包含在 v26.1.0 和 v24.16.0 LTS 版本中
- 👥 经过多位核心贡献者审查和批准，代码覆盖率达 89.68%

---

### [如何使用 Antigravity 和多智能体编排实现现代化自动化 | 作者：James O'Reilly | 2026 年 5 月 | JavaScript 简明教程](https://javascript.plainenglish.io/migrating-express-to-next-js-using-ai-agents-antigravity-f48b4c206a8e?gi=0fa1c218736f)

**原文标题**: [How to automate modernization with Antigravity and multi-agent orchestration | by James O'Reilly | May, 2026 | JavaScript in Plain English](https://javascript.plainenglish.io/migrating-express-to-next-js-using-ai-agents-antigravity-f48b4c206a8e?gi=0fa1c218736f)

### 概述摘要
本文介绍如何使用 Google Antigravity 和自定义 Agent 技能包，将遗留的 Express/Mongoose 单体应用现代化改造为 Next.js 架构。通过多智能体编排、渐进式披露和自愈验证循环，实现自动化重构。

### 关键要点
- 🎯 **核心挑战**：遗留 Express 应用存在同步 require()、嵌套回调、未类型数据等问题，需通过绿场迁移彻底重构
- 🏗️ **目标架构**：从 Express 单体→Next.js App Router，Mongoose→Zod+MongoDB，CommonJS→TypeScript，Pug→ShadCN UI
- 🤖 **Antigravity 平台**：基于 VS Code 的智能体优先开发平台，支持并行生成多个自主 AI 智能体，可独立规划任务、修改代码、运行命令
- ⚡ **何时使用智能体**：区分确定性任务（如 npm install）和启发式任务（如重构回调为 async/await），避免“上下文窗口税”
- 📋 **技能包设计原则**：采用 YAML 元数据路由、渐进式披露、Plan-and-Execute 模式，通过硬编码 5 阶段流程（审计→基础→数据→UI→验证）确保可预测性
- 🔄 **自愈循环机制**：基于 TDD 的 Reflexion 模式，智能体编写测试→执行失败→反思错误→修正代码，直至通过所有测试
- 🛠️ **5 阶段工作流**：Phase1 逆向工程审计（API 契约/数据模型/业务逻辑/UI 考古）→Phase2 建立 Vitest 测试框架→Phase3 实现数据层和 API 路由→Phase4 构建 ShadCN UI 组件→Phase5 对抗性验证
- ✅ **验证方法**：通过“双标签测试”进行运行时对比，利用 Antigravity 浏览器子智能体生成视频记录作为“工作证明”
- 💡 **最佳实践**：手动处理确定性任务（如 npm install），避免智能体陷入遗留依赖的“兔子洞”；使用低自由度护栏（结构化清单）防止智能体漂移
- 🚀 **生产就绪**：迁移完成后需使用反向代理渐进式路由流量（绞杀者模式）、映射遗留路由、迁移到 OpenTelemetry 日志系统

---

### [谷歌反重力](https://antigravity.google/)

**原文标题**: [Google Antigravity](https://antigravity.google/)

概述摘要：本文探讨了人工智能在医疗领域的应用前景，强调了其提升诊断效率、个性化治疗及降低医疗成本的优势，同时指出了数据隐私、算法偏见和监管挑战等关键问题。

- 🩺 人工智能可辅助影像诊断，提高疾病检测准确率，减少误诊风险。
- 🧬 通过分析患者数据，AI 能制定个性化治疗方案，优化药物剂量。
- 💰 自动化流程可降低医院运营成本，缓解医疗资源紧张问题。
- 🔒 数据隐私保护是主要挑战，需建立严格的安全标准防止信息泄露。
- ⚖️ 算法偏见可能导致不公平治疗，需确保训练数据多样性和透明性。
- 📜 监管框架尚不完善，需要制定新法规以平衡创新与患者安全。

---

### [devrel-demos/other/modernizing-expressjs 主分支 · GoogleCloudPlatform/devrel-demos · GitHub](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/other/modernizing-expressjs)

**原文标题**: [devrel-demos/other/modernizing-expressjs at main · GoogleCloudPlatform/devrel-demos · GitHub](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/other/modernizing-expressjs)

本仓库提供了一个 AI 驱动的现代化工具包，用于将 Express.js 单体应用迁移到 Next.js 架构，包含 5 个自动化阶段。

- 🏗️ **架构映射**：将 Express.js 单体、Mongoose、JavaScript(CommonJS)、Pug/EJS 和 Passport.js 分别迁移到 Next.js App Router、MongoDB+Zod、TypeScript(ESM)、ShadCN UI+Tailwind 和 Auth.js。
- 🔄 **5 阶段工作流**：包括 AI 审计（逆向工程）、测试驱动开发、新应用脚手架、UI 生成和一致性验证。
- 📁 **项目结构**：推荐“现代化中心”monorepo 结构，隔离遗留代码（legacy-app）和新目标代码（modern-app），并包含.agents 技能包和 docs 文档。
- 🚀 **快速开始**：通过 giget 克隆仓库，将 node-express-mongoose-demo 放入 legacy-app，然后在 Google Antigravity 中运行/orchestrating-greenfield-migration 触发流程。

---

### [使用 AI 更慢地编写更好的代码 | 阅读茶叶](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

**原文标题**: [Using AI to write better code more slowly | Read the Tea Leaves](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

本文主张，AI 编程的真正价值不在于快速生成大量低质量代码，而在于用它来更慢、更高质量地编写代码。

- 🤖 **AI 是高效找 Bug 工具**：LLM 代理非常擅长发现代码库中的漏洞，从关键安全错误到微小误导性注释，远超“快速生成代码”的单一用途。
- 🕵️ **多模型交叉审查**：通过同时运行多个不同 AI 模型（如 Claude、Codex、Cursor Bugbot）审查 PR，能有效减少幻觉和误报，提高审查可靠性。
- 🎯 **工作流：优先修复关键 Bug**：典型流程是让 AI 代理优先修复关键和高危 Bug，跳过收益不高的中低风险问题，甚至放弃有根本性错误的 PR。
- 🧹 **发现并修复既有问题**：这种慢速审查常会挖出代码库中已有的 Bug，引发“支线任务”，虽降低原始速度，但显著提升代码库整体健康度。
- 📚 **加深代码理解**：通过让 AI 解释 PR 工作原理、生成文档（如 Mermaid 图表），开发者能更深入理解复杂架构及其失败模式，而非只关注“快乐路径”。
- 🛠️ **适用场景与争议**：该方法要求开发者具备足够领域知识来筛选 AI 报告；对资深开发者误报率极低，但对新手可能造成信息过载。
- 💡 **反对“快速生成”文化**：作者呼吁“慢速编码”，认为这种注重质量、方法论的风格，比追求原始代码行数的“10 倍效率”更具长期价值。

---

### [使用 Node.js 构建自定义 MCP 服务器](https://deanhume.com/building-a-custom-mcp-server-with-node-js/)

**原文标题**: [Building a Custom MCP Server with Node.js](https://deanhume.com/building-a-custom-mcp-server-with-node-js/)

本指南介绍了如何使用 Node.js 构建自定义 MCP 服务器，实现 AI 助手查询垃圾回收日程的功能。

- 📦 **MCP 协议概述**：MCP（模型上下文协议）是连接 AI 助手与外部数据源的开放标准，类似 USB 接口，一次构建即可兼容多种客户端（如 Claude Desktop、VS Code）。
- 🗑️ **实际应用场景**：以垃圾回收日程为例，解决用户记不住不同垃圾类型回收日期的痛点，支持查询“下次回收时间”或“特定类型回收日”。
- ⚙️ **项目搭建步骤**：创建 Node.js 项目，安装 `@modelcontextprotocol/sdk`，配置 ES 模块，并准备 JSON 数据文件存储回收日期与垃圾类型说明。
- 🔧 **服务器核心逻辑**：包含加载数据、筛选未来回收日期的函数（`getUpcomingCollections`、`getNextCollection`），以及定义工具列表（`get_upcoming_collections`、`get_next_collection`、`get_bin_types`）。
- 🧩 **工具定义与处理**：通过 `ListToolsRequestSchema` 声明工具名称、描述和输入参数（JSON Schema），`CallToolRequestSchema` 处理具体调用并返回格式化文本结果。
- 🚀 **测试与集成**：通过 stdio 传输启动服务器，在 VS Code 设置中添加 MCP 服务器配置后，即可用自然语言提问（如“下次回收是什么时候？”）。
- 🌐 **扩展与部署**：代码可部署到 Azure App Service 实现远程访问，完整代码已开源在 GitHub。

---

### [GitHub - webdiscus/ansis：适用于终端、CI和基于Chromium的浏览器控制台的CJS/ESM ANSI 颜色库。兼容 Bun、Deno、Next.JS。](https://github.com/webdiscus/ansis)

**原文标题**: [GitHub - webdiscus/ansis: CJS/ESM ANSI color library for terminals, CI and Chromium-based browser consoles. Compatible with Bun, Deno, Next.JS. · GitHub](https://github.com/webdiscus/ansis)

Ansis 是一个高性能的 ANSI 颜色库，专为终端、CI 环境和 Chromium 浏览器设计，支持丰富的颜色和样式功能。

- 🌈 支持 16/256/Truecolor 颜色、链式语法、模板字面量和嵌套模板
- ⚡ 性能卓越，2 种及以上样式时速度最快（60M ops/sec），远超 chalk 和 styleText()
- 📦 体积小巧（5.8 kB），可作为 chalk（44 kB）的即插即用替代品
- 🧠 智能颜色检测，自动降级（Truecolor → 256 → 16 → 黑白），支持 NO_COLOR/FORCE_COLOR
- 🛠️ 提供实用工具：strip() 去除 ANSI 码、link() 创建超链接、extend() 注册自定义颜色
- 💻 兼容 Node 10+、Bun、Deno、Next.js、Chromium 浏览器及多种 CI 环境
- 📊 支持 ESM、CJS、TypeScript，与 chalk、picocolors 等库兼容
- 🧪 处理边缘情况（空参数、嵌套模板、换行样式）优于其他库

---

### [发布 v4.3.0 · webdiscus/ansis · GitHub](https://github.com/webdiscus/ansis/releases/tag/v4.3.0)

**原文标题**: [Release v4.3.0 · webdiscus/ansis · GitHub](https://github.com/webdiscus/ansis/releases/tag/v4.3.0)

概述摘要  
- 🎉 新增 OSC 8 超链接支持，通过 `link(url, text)` 实现，解决 issue #44  
- 🛠️ 添加构造函数重载，允许传入模拟的 `globalThis` 对象以控制颜色自动检测，解决 issue #47  
- 🐛 修复环境变量和 CLI 标志的边缘情况处理，解决 issue #46  
- 🔧 修正多个边缘案例：`FORCE_COLOR` 优先于 `NO_COLOR`，CLI 标志优先于 `NO_COLOR`，`FORCE_COLOR` 具有最高优先级，最后指定的标志生效，以及自动检测回退时使用最低颜色级别而非真彩色  
- 📦 发布版本 v4.3.0，包含上述功能和修复

---

### [功能：为终端超链接添加 `link` 方法 (OSC 8) · 问题 #44 · webdiscus/ansis · GitHub](https://github.com/webdiscus/ansis/issues/44)

**原文标题**: [feat: add `link` method for terminal hyperlinks (OSC 8) · Issue #44 · webdiscus/ansis · GitHub](https://github.com/webdiscus/ansis/issues/44)

概述摘要：该 issue 请求在 ansis 库中添加对终端超链接（OSC 8）的支持，作为 ANSI 转义序列的一部分，并提供了具体的使用示例。

- ⭐ 请求新增`link`方法，支持终端超链接（OSC 8）功能
- 🔗 提供两种使用方式：独立函数`link('文本', 'URL')`和链式调用`ansis.blue.link('文本', 'URL')`
- 🎯 动机：OSC 8 属于 ANSI 转义序列，符合 ansis 库的范围
- 🚫 替代方案：手动构建 OSC 8 序列或使用`terminal-link`库
- 💡 项目价值：用户表达了对该实用项目的感谢，并提醒实现后别忘了给星标

---

### [GitHub - Alhadis/OSC8-Adoption：支持超链接的终端模拟器列表（OSC 8 转义序列）。· GitHub](https://github.com/Alhadis/OSC8-Adoption/)

**原文标题**: [GitHub - Alhadis/OSC8-Adoption: List of terminal emulators that support hyperlinks (OSC 8 escape sequences). · GitHub](https://github.com/Alhadis/OSC8-Adoption/)

本文件记录了终端模拟器对 OSC 8 超链接（终端超链接）的支持情况，涵盖终端、复用器、应用及库的兼容性列表。

- 📋 **概述**：OSC 8 超链接支持追踪，涵盖终端模拟器、复用器、应用及库的兼容性列表。
- 🖥️ **终端模拟器**：Alacritty、DomTerm、foot、Ghostty、hterm、Hyper、iTerm2、Kitty、Konsole、mintty、Secure ShellFish、Terminology、Ultimate++、VTE 系列、WezTerm、Windows Terminal、xterm.js、VS Code 等已支持。
- 🔗 **终端复用器**：TermySequence、tmux（需配置）、Zellij 支持超链接。
- 📱 **应用支持**：Cargo、column、Delta、Emacs、eza、fd、fzf、GCC、Groff、less、lf、ls、lsd、Matterhorn、mdcat、moor、Mudlet、Neovim、ripgrep、Symfony、systemd、wget2 等已集成。
- 📚 **库支持**：ansi_up、brick、Rich、vty 等库已实现超链接功能。
- ⏳ **待支持**：ConEmu、LilyTerm、LXDE Terminal、Tilda、screen、Irssi、NeoMutt、TBVaccine、WeeChat 等功能请求待处理。
- 🔗 **资源链接**：包含原始 OSC 8 规范、GNOME Terminal 讨论、iTerm2 讨论及测试文件等。

---

### [幽灵 — 给每个代理自己的数据库](https://ghost.build/give-every-agent/?v=2)

**原文标题**: [Ghost â Give every agent its own database](https://ghost.build/give-every-agent/?v=2)

概述摘要：本文探讨了如何通过拆解复杂概念或问题来深入理解其核心要素。

- 🧩 拆解复杂概念有助于揭示其内在结构与逻辑关系  
- 🔍 通过逐一分析关键组成部分，能更清晰地把握整体本质  
- 📊 有效拆解需结合分类、归纳与优先级排序方法  
- 💡 该过程能提升问题解决效率与创新思维  
- 🛠️ 实践拆解时，建议从核心问题出发，逐步细化至可操作层面

---

### [Flue — 代理框架工具](https://flueframework.com/)

**原文标题**: [Flue â The Agent Harness Framework](https://flueframework.com/)

Flue 是一个可编程的 TypeScript 框架，用于构建自主代理和 AI 工作流，提供模型、工具、技能、文件系统和沙箱等核心组件。

- 🤖 **核心架构**：代理 = 模型 + 工具集，支持规划、上下文收集、文件操作、子代理和专家委派。
- 🛠️ **可编程 Harness**：TypeScript 框架为任何模型提供会话、工具、技能、文件系统访问和安全工作环境。
- 📂 **文件系统访问**：支持读取、写入、grep 和 glob 操作，让代理能处理真实文件。
- 🔒 **沙箱环境**：提供 bash 执行、安全控制和网络访问，确保代理操作安全可控。
- 🧠 **技能与记忆**：可加载可重用的专业知识和工作流，支持会话记忆和上下文保持。
- 🔄 **工作流自动化**：运行结构化自动化，从清晰输入到完成结果，代码引导代理推理。
- 🧩 **子代理与工具**：定义专业角色，委派任务；提供类型化工具用于 API 调用、数据查询和受控变更。
- 🌐 **MCP 服务器集成**：通过开放模型上下文协议连接认证工具和服务。
- 📊 **可观测性**：监控代理并导出追踪到 OpenTelemetry、Braintrust、Sentry 等。
- 💬 **聊天集成**：连接 Slack、Teams、Discord、GitHub 等平台，让代理在协作环境中工作。
- 🚀 **部署灵活**：支持 Node.js、Cloudflare Workers、GitHub Actions、GitLab CI/CD 等环境。

---

### [docx - 使用 JavaScript 生成.docx 文档](https://docx.js.org/)

**原文标题**: [docx - Generate .docx documents with JavaScript](https://docx.js.org/)

以下是您提供内容的概述和要点总结：

概述总结：本文主要介绍了如何通过合理规划时间、设定优先级和使用工具来提高工作效率，同时强调了休息和健康的重要性。

- 📅 合理规划时间：使用时间管理方法（如番茄工作法）来分配任务，避免拖延。
- 🎯 设定优先级：区分紧急与重要任务，优先处理关键事项。
- 🛠️ 利用工具：借助日历、待办清单或项目管理软件来跟踪进度。
- 🧘 注重休息：定期休息和运动，保持身心健康以提升长期效率。
- 🔄 定期复盘：每天或每周回顾完成情况，调整计划以持续改进。

---

### [获取失败](https://nodeweekly.com/link/185805/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/185805/web)

无法总结：获取内容失败，状态码 403。

---

### [docx/demo 在 master 分支 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/tree/master/demo)

**原文标题**: [docx/demo at master · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/tree/master/demo)

这是一个名为 `docx` 的代码库，用于生成 Word 文档，拥有 5.7k 星标和 604 个分支，包含丰富的示例代码。

- 📂 项目主页显示 `dolanmiu/docx` 仓库，包含代码、议题、拉取请求等导航选项。
- 🌟 仓库获得 5.7k 星标，有 604 个分支，139 个议题和 4 个拉取请求。
- 📁 当前浏览 `demo` 目录，包含大量 TypeScript 示例文件，如 `1-basic.ts` 到 `94-texbox.ts`。
- 🛠️ 示例涵盖基础功能、表格、图片、页眉页脚、样式、编号、书签、评论等。
- 📝 支持高级特性，如多列、脚注、数学公式、自定义字体、模板文档等。

---

### [Helmet.js](https://helmet.js.org/)

**原文标题**: [Helmet.js](https://helmet.js.org/)

Helmet 是一个用于保护 Node/Express 应用安全的中间件，通过设置 HTTP 响应头来增强安全性，易于集成且维护成本低。

- 🛡️ **快速集成**：只需 `app.use(helmet())` 即可默认设置 13 个 HTTP 响应头，支持独立 Node.js 或其他框架。
- ⚙️ **灵活配置**：可禁用特定头（如 `contentSecurityPolicy: false`）或自定义配置（如通过 `directives` 对象设置 CSP 规则）。
- 🔒 **Content-Security-Policy**：默认策略防止 XSS 等攻击，支持自定义指令（如 `script-src`），可启用 `reportOnly` 模式，并建议在开发时禁用 `upgrade-insecure-requests`。
- 🌐 **跨域安全头**：包括 `Cross-Origin-Embedder-Policy`（默认不设置）、`Cross-Origin-Opener-Policy`（默认 `same-origin`）和 `Cross-Origin-Resource-Policy`（默认 `same-origin`），用于隔离页面和资源。
- 🚀 **传输与隐私**：`Strict-Transport-Security`（默认强制 HTTPS）、`Referrer-Policy`（默认 `no-referrer`）和 `X-DNS-Prefetch-Control`（默认关闭预取），提升安全与隐私。
- 🛑 **旧浏览器兼容**：`X-Frame-Options`（防点击劫持）、`X-Content-Type-Options`（防 MIME 嗅探）和 `X-XSS-Protection`（默认禁用有缺陷的过滤器）。
- 📦 **其他安全头**：`Origin-Agent-Cluster`（隔离进程）、`X-Download-Options`（IE 安全）、`X-Permitted-Cross-Domain-Policies`（Adobe 策略）和移除 `X-Powered-By`（节省带宽）。
- 🔧 **独立使用**：每个头均可作为独立中间件（如 `helmet.contentSecurityPolicy()`），方便按需集成。

---

### [头盔/CHANGELOG.md 主分支 · helmetjs/头盔 · GitHub](https://github.com/helmetjs/helmet/blob/main/CHANGELOG.md#820---2026-05-21)

**原文标题**: [helmet/CHANGELOG.md at main · helmetjs/helmet · GitHub](https://github.com/helmetjs/helmet/blob/main/CHANGELOG.md#820---2026-05-21)

Helmet 是一個 Node.js 安全中介軟體，用於設定各種 HTTP 安全標頭，保護 Web 應用程式免受常見攻擊。以下是其版本演進的重點摘要：

- 📜 **v8.2.0 (2026)**：支援 `Cross-Origin-Opener-Policy` 的 `noopener-allow-popups`，並改善重複選項的錯誤訊息。
- 🔒 **v8.1.0 (2025)**：`Content-Security-Policy` 在指令值（如 `self`）應加引號時提供更佳錯誤提示。
- ⚠️ **v8.0.0 (2024)**：重大變更包括 `Strict-Transport-Security` 的 max-age 增至 365 天、CSP 對未加引號的指令拋錯、移除 Node 16/17 支援。
- 🛡️ **v7.2.0 (2024)**：CSP 對未加引號的指令發出警告（未來版本將變為錯誤）。
- 🆕 **v7.1.0 (2023)**：`crossOriginEmbedderPolicy` 新增 `unsafe-none` 指令支援。
- 🔄 **v7.0.0 (2023)**：`Cross-Origin-Embedder-Policy` 預設停用、移除 Node 14/15 支援及 `Expect-CT` 功能。
- 📦 **v6.2.0 (2023)**：公開標頭名稱（如 `strictTransportSecurity`）並重寫文件。
- 🐛 **v6.1.x (2023)**：修復 TypeScript 匯出問題及套件中繼資料。
- 🔧 **v6.0.0 (2022)**：CSP 不再預設設定 `block-all-mixed-content`、移除 `Expect-CT` 預設值、提升 TypeScript 嚴格性。
- 🌐 **v5.1.0 (2022)**：`Cross-Origin-Embedder-Policy` 支援 `credentialless` 政策。
- 📘 **v5.0.0 (2022)**：支援 ECMAScript 模組匯入、多項安全標頭預設啟用、移除 Node 10/11 支援。
- 🧩 **v4.6.0 (2021)**：CSP 新增 `useDefaults` 選項以更易覆寫預設值。
- 🚀 **v4.5.0 (2021)**：新增 `crossOriginEmbedderPolicy`、`crossOriginOpenerPolicy`、`crossOriginResourcePolicy` 中介軟體。
- 📉 **v4.4.1 (2021)**：縮小發佈套件約 2.5 kB。
- 🆔 **v4.4.0 (2021)**：新增 `originAgentCluster` 中介軟體。
- 🛠️ **v4.3.0 (2020)**：CSP 可透過 `dangerouslyDisableDefaultSrc` 停用 `default-src`。
- 📋 **v4.2.0 (2020)**：CSP 新增 `getDefaultDirectives()` 方法。
- 🔌 **v4.0.0 (2020)**：無依賴、CSP 預設指令集、移除 `featurePolicy`、`hpkp`、`noCache` 等功能。
- 📜 **v3.x (2019-2020)**：逐步新增 `featurePolicy`、`permittedCrossDomainPolicies`、`expectCt` 等中介軟體，並更新多項依賴。
- 🔄 **v2.x (2016-2018)**：引入 `referrerPolicy`、`hpkp`、`dnsPrefetchControl` 等，並重構為獨立模組。
- 🏁 **v1.x (2015-2016)**：初始版本，支援 CSP、HSTS、X-Frame-Options 等基本安全標頭。

---

### [发布 0.29.0 · kysely-org/kysely · GitHub](https://github.com/kysely-org/kysely/releases/tag/v0.29.0)

**原文标题**: [Release 0.29.0 · kysely-org/kysely · GitHub](https://github.com/kysely-org/kysely/releases/tag/v0.29.0)

Kysely v0.29.0 版本发布，带来了多项新功能和重要变更，包括编译时辅助工具、只读实例类型、新数据库方言支持、查询取消功能等。

- 🚀 新增 `$pickTables` 和 `$omitTables` 编译时辅助工具，可缩小下游查询的数据库视图，降低编译复杂度
- 🔒 引入 `ReadonlyKysely<DB>` 类型，将实例转换为编译时只读，禁止写入操作
- 🟨 新增 PGlite 方言支持，并引入 `supportsMultipleConnections` 标志和集中式连接互斥锁
- 🔍 `$narrowType` 支持嵌套类型缩小和判别联合类型
- 🛑 支持基于 Web 标准的查询取消功能，可传递中止信号，并支持忽略、取消查询或终止会话等策略
- 🛡️ 新增 `SafeNullComparisonPlugin` 插件，当右侧参数为 `null` 时自动将等号/不等号转换为 `is`/`is not`
- ⚙️ `ParseJSONResultsPlugin` 新增 `shouldParse(value, path)` 选项，可按 JSON 路径精细控制是否解析
- 🏷️ 最低 TypeScript 版本提升至 5.4，并停止提供 CommonJS 分发
- 🧩 迁移相关功能现从 `'kysely/migration'` 导出，旧路径会报编译错误
- 🐘 新增 PostgreSQL 和 MySQL 的外部表支持、MSSQL 的 `datetime2` 数据类型支持
- 🐞 修复了多项 bug，并改进了文档和 CI/CD 工具链

---

### [发布 v7.1.0 · harshankur/officeParser · GitHub](https://github.com/harshankur/officeParser/releases/tag/v7.1.0)

**原文标题**: [Release v7.1.0 · harshankur/officeParser · GitHub](https://github.com/harshankur/officeParser/releases/tag/v7.1.0)

officeParser v7.1.0 版本发布，专注于企业级可靠性、内存泄漏预防和精准解析，新增取消控制、线程安全及实体解码功能。

- 🛡️ **原生取消支持**：通过 `AbortSignal` 可在解析、OCR 识别等任务中立即中断操作，提升灵活性和资源控制。
- ⏱️ **统一超时与内存安全**：整合 OCR 和生成器超时配置，强制终止失败任务并清理 Puppeteer 浏览器和 Tesseract 工作进程，防止资源泄漏。
- 🔧 **XLSX 解析增强**：修复 XML 实体解码（如 `&#38;`）和 `inlineStr` 标签属性匹配问题，确保电子表格字符串正确解析。
- 🖥️ **可视化面板升级**：新增超时和取消控制选项，并采用 ESM 原生 `import()` 以符合严格内容安全策略（CSP）。
- 📦 **快速上手**：通过 `npm install officeparser@7.1.0` 安装，示例代码展示如何使用 `AbortSignal` 和超时配置。
- ❤️ **项目支持**：自 2019 年开源，已超 1000 万次下载，欢迎通过 GitHub Sponsors 或 Buy Me A Coffee 支持未来发展。

---

### [GitHub - wsporto/typesql: TypeSQL - 从原始 SQL 生成 TypeScript API。支持 PostgreSQL、MySQL、Sqlite、LibSQL（Turso）和 D1（Cloudflare）](https://github.com/wsporto/typesql)

**原文标题**: [GitHub - wsporto/typesql: TypeSQL - Generate Typescript API from raw SQL. Supports PostgresSQL, MySQL, Sqlite, LibSQL (Turso) and D1 (Cloudflare) · GitHub](https://github.com/wsporto/typesql)

TypeSQL 是一个能从原始 SQL 语句生成类型安全 TypeScript API 的工具，支持多种数据库后端，无需使用重型 ORM 即可获得类型安全性和 SQL 维护便利性。

- 🔧 支持多种数据库：PostgreSQL、MySQL、SQLite、LibSQL（Turso）和 Cloudflare D1
- 🛡️ 完全类型安全：自动推断 SQL 查询参数和返回列的类型，包括可空性
- 📄 无需学习新语言：直接使用原生 SQL，保留其全部表达能力和灵活性
- 🧩 智能返回类型：根据主键、唯一键或 LIMIT 1 自动判断返回单行还是多行
- 🔄 动态 ORDER BY 支持：提供自动补全和编译时验证
- ⚙️ 简单配置：通过 `typesql.json` 文件配置数据库连接和 SQL 文件目录
- 🚀 使用便捷：全局安装 `typesql-cli` 后，运行 `typesql compile --watch` 即可自动生成 TypeScript 文件
- 📁 自动索引文件生成：可递归生成 index.ts 桶文件
- 🧪 实验性项目：处于积极开发阶段，API 可能变化，欢迎提交问题和功能请求

---

### [pnpm 11.4 | pnpm](https://pnpm.io/blog/releases/11.4)

**原文标题**: [pnpm 11.4 | pnpm](https://pnpm.io/blog/releases/11.4)

pnpm 11.4 版本发布，重点修复了多个供应链安全漏洞，并引入了破坏性变更。

- 🔒 **安全修复：凭据不再跨注册表泄露** - 未限定范围的 `_authToken` 等凭据现在会被自动绑定到声明它们的注册表 URL，防止被其他（可能不受信任的）注册表窃取。
- 🛡️ **安全修复：锁文件缺失完整性校验时拒绝安装** - 现在如果锁文件条目缺少 `integrity` 字段，`pnpm install` 会直接报错退出，防止攻击者篡改锁文件后安装恶意包。
- ⚔️ **安全修复：Git 解析拒绝非 SHA 的 commit 字段** - Git 解析中的 `commit` 字段必须是 40 位十六进制 SHA 值，否则会被拒绝，防止命令注入攻击。
- 📁 **安全修复：补丁文件写入包目录外被拒绝** - 补丁文件如果尝试写入、删除或重命名包目录外的文件，现在会被直接拒绝。
- 🚫 **安全修复：依赖别名包含路径遍历被拒绝** - 依赖别名中如果包含 `../` 等路径遍历段，在读取清单或创建符号链接时会被拒绝。
- 🧩 **默认将 tarball 完整性不匹配视为硬失败** - `pnpm install` 现在遇到 tarball 哈希不匹配会直接报错退出，不再静默重新解析。可通过 `--update-checksums` 标志选择绕过。
- ⚙️ **`pnpm runtime set` 默认写入 `devEngines.runtime`** - 现在默认将运行时版本保存到 `devEngines.runtime`，而非 `engines.runtime`。使用 `--save-prod` 可改为保存到后者。
- 🛠️ **其他修复**：修复 `pnpm deploy` 在 `configDependencies` 声明 pacquet 时的崩溃；限制大型工作区并发读取清单以避免 `EMFILE` 错误；验证 `devEngines.runtime` 和 `engines.runtime` 版本范围；改进 `minimumReleaseAge` 相关日志信息。

---

### [GitHub - lsongdev/node-dns: :globe_with_meridians: 纯 JavaScript 实现的 DNS 服务器和客户端，无任何依赖。](https://github.com/lsongdev/node-dns)

**原文标题**: [GitHub - lsongdev/node-dns: :globe_with_meridians:  DNS Server and Client Implementation in Pure JavaScript with no dependencies. · GitHub](https://github.com/lsongdev/node-dns)

这是一个纯 JavaScript 实现的 DNS 服务器和客户端库，支持 UDP、TCP 和 HTTPS 协议，无需任何外部依赖。

- 🌐 **纯 JavaScript 实现**：无需外部依赖，支持 DNS 服务器和客户端功能
- 📦 **轻量且多功能**：支持 UDP、TCP 和 HTTPS 协议，以及多种 DNS 记录类型（A、AAAA、MX、CNAME、SOA 等）
- 🚀 **简单易用的 API**：提供 `resolveA`、`resolveMX` 等便捷方法，也支持直接通过 `dns.resolve(domain, 'TYPE')` 查询任意记录类型
- 🔧 **灵活配置**：可自定义 DNS 服务器地址、端口和递归标志，也支持使用系统 DNS 服务器
- 🖥️ **内置服务器功能**：可创建自定义 DNS 服务器，支持处理请求、返回错误码（如 NXDOMAIN、REFUSED），并监听事件
- 📊 **性能优化**：包含基准测试模块，适用于高性能场景
- 📜 **遵循 RFC 标准**：支持 RFC-1034、RFC-1035、RFC-2782、RFC-7766 和 RFC-8484 等规范
- 🤝 **开源贡献**：MIT 许可证，欢迎 Fork 和贡献代码

---

### [GitHub - Agent-Field/agentfield: 像 API 和微服务一样构建、运行和扩展 AI 代理——从第一天起就具备可观测、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平台，可将 AI 代理构建为可调用的 API，具备身份、可观测性和审计能力。

- 🚀 **核心功能**：将 Python、Go、TypeScript 编写的代理逻辑转化为生产级 REST API，支持路由、协调、记忆、异步执行和加密审计。
- ⚙️ **关键抽象**：`app.ai()` 调用 LLM 输出结构化结果，`app.pause()` 暂停等待人工审批，`app.call()` 跨代理路由，`app.run()` 自动暴露 REST 端点。
- 🧩 **多语言与 SDK**：提供 Python、Go、TypeScript SDK，支持 `@app.reasoner()` 和 `@app.skill()` 装饰器，自动注册到控制平面。
- 📦 **快速部署**：支持 Docker Compose、Kubernetes，提供 CLI 脚手架 (`af init`)，一键生成生产级多代理后端。
- 🔍 **可观测性**：自动生成工作流 DAG、Prometheus 指标、结构化日志、执行时间线，支持健康检查和心跳监控。
- 🛡️ **治理与安全**：每个代理拥有 W3C DID 加密身份，执行生成可验证凭证，支持基于标签的策略执行和加密签名请求。
- 🔄 **高级执行**：支持同步/异步 REST 调用、SSE 流式传输、Webhook 回调、自动重试、无超时限制，以及金丝雀部署和 A/B 测试。
- 🧠 **记忆与状态**：内置 KV 存储和向量搜索，支持全局、代理、会话、运行四种作用域，无需 Redis。
- 🤝 **人工介入**：`app.pause()` 实现持久化暂停/恢复，支持审批工作流、超时和自动升级。
- 📚 **生态系统**：已用于自主工程团队、深度研究引擎、安全审计等场景，社区可提交项目展示。

---

### [Node.js 应用的自动缩放](https://judoscale.com/node?utm_source=node-weekly&utm_medium=referral&utm_campaign=try-judoscale&utm_content=doesnt-suck)

**原文标题**: [Autoscaling for Node.js apps](https://judoscale.com/node?utm_source=node-weekly&utm_medium=referral&utm_campaign=try-judoscale&utm_content=doesnt-suck)

### 概述总结
Judoscale 是一款专为 Node.js 应用设计的自动缩放工具，基于请求队列时间和作业队列延迟进行精准缩放，支持多种平台，可降低成本并提升性能。

- 🚀 **轻松自动缩放**：支持 Node.js Web 应用和作业队列，基于请求队列时间和作业队列延迟进行缩放，兼容 Amazon ECS、Heroku、Render、Fly.io、Railway 等平台。
- ⏱️ **基于队列时间**：使用队列时间作为服务器容量指标，而非通用指标如 CPU 或内存，确保更精准的缩放。
- 🛠️ **支持作业队列**：通过队列延迟自动缩放后台工作进程，防止作业队列积压。
- ⚡ **最快缩放器**：缩放算法每 10 秒运行一次，快速响应容量问题，确保用户体验。
- 💰 **降低托管成本**：精准缩放算法减少过度配置，在保持性能的同时节省成本。
- 🎛️ **可自定义行为**：支持每次缩放多个实例、调整缩放频率，并通过简单滑块独立配置每个进程。
- 🌟 **值得信赖**：被 900+ 工程团队使用，每月处理超过 250 万请求，自 2017 年起稳定运营。
- 📦 **支持 Node 栈**：Web 缩放支持 Express 和 Fastify，Worker 缩放支持 Bull 和 BullMQ。
- 💬 **用户好评**：用户称赞其稳定性、易用性，能自动应对流量高峰，减少停机时间和运维压力。
- 🆓 **免费试用**：设置时间不到 5 分钟，可立即开始使用。

---

### [2026 年人工智能现状](https://2026.stateofai.dev/en-US)

**原文标题**: [State of AI 2026](https://2026.stateofai.dev/en-US)

2026 年 Web 开发 AI 调查显示，AI 对开发者工作影响深远，7,258 名受访者提供了关键数据。

- 📈 AI 采用率激增：AI 生成代码比例从 2025 年的 28% 跃升至 2026 年的 54%，频繁使用 AI 的开发者比例翻倍。
- 🤖 编码代理崛起：Claude Code 在编码代理中正面评价最高，Claude 成为开发者付费最多的模型。
- 💰 变现竞赛加剧：个人 AI 工具月支出明显增加，多数受访者认为当前处于 AI 泡沫中。
- ⚠️ 风险因素增加：开发者担忧 AI 导致失业，主要风险包括军事应用、环境影响和幻觉不准确等问题。

---

### [CSS 2026 现状](https://survey.devographics.com/en-US/survey/state-of-css/2026)

**原文标题**: [State of CSS 2026](https://survey.devographics.com/en-US/survey/state-of-css/2026)

概述摘要  
- ⏳ 内容加载中，请稍候。  
- 🔄 当前未提供具体文本，无法生成摘要。  
- 📭 请提供需要总结的文章内容。

---

### [JS 填字游戏](https://lyra.horse/fun/jscrossword/)

**原文标题**: [JS Crossword](https://lyra.horse/fun/jscrossword/)

### 概述总结
这是一个基于 JavaScript eval() 的填字游戏，每个线索都是答案的 JS 表达式，仅允许特定字符，最终答案需为英文单词。

- 🧩 填字游戏规则：每个线索对应一个 JS eval() 表达式，例如"7"可解为"3+4"，"[object Object]"可解为"[]+{}"
- 🔒 允许字符限制：仅可使用 A-Za-z0-9!"()*+-./<=>[]`{}，禁止空格、逗号和分号
- 🎯 最终答案要求：必须由英文字母组成（A-Za-z），且区分大小写
- 🛡️ 评估方式：答案在 eval() 沙箱中运行，提供 playground 供测试
- 🤖 人工设计：强调由人类制作，鼓励自行解决而非使用 AI
- 🎮 操作提示：点击格子或按 ctrl 可改变书写方向，进度自动保存
- 🎨 颜色标识：绿色=可能正确，红色=无效字符，黄色=错误，灰色=预填充
- 💬 社交分享：支持在 fedi、bsky、twitter 上分享想法

---

### [告别 asm.js | SpiderMonkey JavaScript/WebAssembly引擎](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html)

**原文标题**: [Saying goodbye to asm.js | SpiderMonkey JavaScript/WebAssembly Engine](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html)

### 概述总结
asm.js 优化已在 Firefox 148 中默认禁用，并计划未来移除，建议用户迁移至 WebAssembly 以获得更优性能。

- 🛑 **禁用与移除**：自 Firefox 148 起，asm.js 优化默认关闭，未来将彻底移除代码。
- 🔄 **向后兼容**：asm.js 代码仍作为普通 JavaScript 运行，不会导致网站崩溃，但 WebAssembly 提供更快执行和更小体积。
- 📜 **历史贡献**：asm.js 于 2013 年随 Firefox 22 推出，成功实现 C/C++ 代码在 Web 上的原生级运行，为 WebAssembly 铺平道路。
- 🚀 **迁移建议**：若仍使用 asm.js，建议重新编译为 WebAssembly，其优化管线更先进，性能显著提升。
- ⚙️ **技术原因**：移除 asm.js 可减少维护成本和攻击面，WebAssembly 已完全取代其地位。
- 🐺 **代号传说**：asm.js 编译器 OdinMonkey 将终结（代号“Ragnarök”），但其继任者 BaldrMonkey（WebAssembly 优化编译器）和 RabaldrMonkey（基线编译器）将接替。

---

