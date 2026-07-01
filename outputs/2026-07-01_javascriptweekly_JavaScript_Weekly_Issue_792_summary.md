### [Deno 2.9 | Deno](https://deno.com/blog/v2.9)

**原文标题**: [Deno 2.9 | Deno](https://deno.com/blog/v2.9)

Deno 2.9 发布，亮点包括 `deno desktop` 桌面应用构建、性能大幅提升、Node.js 项目迁移更便捷，以及测试和安全性增强。

- 🖥️ **deno desktop**：无需 Electron 样板代码，即可将 Web 应用构建为原生桌面应用，输出单一二进制文件，支持本地 API 和跨平台编译。
- ⚡ **性能飞跃**：冷启动速度提升约 2 倍（从 34ms 降至 17ms），HTTP 吞吐量提升 11%-27%，内存占用降低 2-3 倍。
- 🔄 **无缝迁移**：`deno install` 可直接读取 npm、pnpm、yarn、Bun 的锁文件，保留依赖版本，无需重写项目。
- 🧪 **测试增强**：内置快照测试、变更感知测试选择、重试/重复运行、覆盖率阈值、分片运行和参数化测试。
- 🔒 **供应链安全**：默认启用最小发布年龄（24 小时），新增 `no-downgrade` 信任策略防止降级攻击。
- 🎨 **CSS 模块导入**：支持通过 `import attributes` 导入 CSS 文件作为可构造样式表。
- 📦 **依赖管理**：新增 `deno link`/`unlink` 管理本地包链接，`deno list` 查看依赖树，支持 `preferPackageJson` 配置。
- 🛠️ **构建工具**：`deno compile` 新增 `--include-as-is` 嵌入静态资源、`--bundle` 减小体积、`--watch` 自动重建；`deno task` 支持输入缓存、并发控制。
- 🌐 **Node.js 兼容性**：目标升级至 Node.js 26，裸内置模块无需配置即可解析，新增 `process.resourceUsage()` 等 API。
- 🔐 **Web 加密**：新增后量子加密算法（ML-KEM、ML-DSA、SLH-DSA）、ChaCha20-Poly1305、SHA-3、Argon2 等，`crypto.subtle` 迁移至 Rust。
- 🌍 **其他改进**：实现 Web Locks API、User-Agent Client Hints API、Happy Eyeballs v2，`Deno.serve` 默认关闭自动压缩，`deno fmt` 新增 HTML/CSS/SQL 格式化。

---

### [POSETTE：Postgres 2026 演讲活动 - YouTube](https://www.youtube.com/playlist?list=PLOBORF8Y_l8g)

**原文标题**: [POSETTE: An Event for Postgres 2026 Talks - YouTube](https://www.youtube.com/playlist?list=PLOBORF8Y_l8g)

本頁面為 YouTube 平台相關資訊的總覽，涵蓋法律、政策、合作與功能測試等面向。
- 📰 新聞中心：提供 YouTube 官方新聞與公告。
- ©️ 版權：說明內容版權相關規範與申訴機制。
- 📞 聯絡我們：提供使用者與 YouTube 團隊聯繫的管道。
- 🎬 創作者：為內容創作者提供資源與支援。
- 📢 刊登廣告：說明廣告合作與收益相關資訊。
- 👨‍💻 開發人員：提供 API 與技術整合文件。
- 📜 條款：列出使用 YouTube 服務的條款與條件。
- 🔒 私隱：說明個人資料收集與使用政策。
- 🛡️ 政策及安全：規範內容與社群安全準則。
- ⚙️ YouTube 的運作方式：解釋平台推薦與演算法機制。
- 🧪 測試新功能：介紹正在測試中的新功能。
- ©️ 2026 Google LLC：版權聲明，標示所有權歸屬。

---

### [使用 TypeScript 7 更快迭代](https://code.visualstudio.com/blogs/2026/06/26/iterating-faster-with-ts-7)

**原文标题**: [Iterating faster with TypeScript 7](https://code.visualstudio.com/blogs/2026/06/26/iterating-faster-with-ts-7)

### 概述总结
VS Code 团队通过渐进式方法成功迁移至 TypeScript 7，实现了 7 倍类型检查加速和 4 倍构建速度提升，同时通过紧密协作帮助 TypeScript 团队完善了工具链。

- ⚡ **性能飞跃**：类型检查从 36 秒降至 5 秒（7 倍提速），`npm run watch`从 80 秒缩短至 20 秒，编辑器语言工具加载时间从近 1 分钟降至 10 秒。
- 🧩 **渐进式迁移策略**：分阶段推进（探索→TS6 桥接→并行运行→逐扩展迁移→全面切换），每个步骤都降低风险并持续反馈问题。
- 🔄 **双向协作价值**：VS Code 团队通过日常使用发现格式化差异、功能缺失等真实场景 bug，推动 TypeScript 团队优先修复，最终使 TS7 更稳定可靠。
- 🛠 **工具链简化**：迁移过程中用 esbuild 替代 webpack，结合`tsgo`（TS7）实现更简洁的构建流程，减少生产与开发环境差异。
- 🚀 **开发者体验提升**：日常编辑循环显著加速，代理辅助迭代更高效，开发者无需频繁等待编译或切换语言版本。

---

### [TypeScript 7.0 RC 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

**原文标题**: [Announcing TypeScript 7.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

TypeScript 7.0 RC 正式发布，基于 Go 语言重写，速度提升约 10 倍，并带来大量性能优化和新特性。

- 🚀 **性能大幅提升**：TypeScript 7.0 使用 Go 重写，结合原生代码速度和共享内存并行，速度约为 6.0 的 10 倍。
- 🛠️ **安装与兼容**：可通过 `npm install -D typescript@rc` 安装，与 6.0 保持类型检查逻辑一致，并支持通过 `@typescript/typescript6` 包并行运行。
- ⚡ **并行化控制**：新增 `--checkers` 和 `--builders` 标志，分别控制类型检查和项目构建的并行度，并支持单线程模式 (`--singleThreaded`)。
- 👁️ **改进的监视模式**：基于 Parcel 文件监视器移植，提供高效稳定的跨平台文件监视，显著降低资源消耗。
- 🔄 **6.0 新行为默认启用**：默认启用 `strict`、`module: esnext`、`stableTypeOrdering` 等，并废弃 `target: es5`、`downlevelIteration` 等旧特性。
- ✨ **模板字面量类型改进**：模板字面量类型现在正确保留 Unicode 码点，例如 `"😀"` 被视为单个字符。
- 📝 **JavaScript 支持重构**：JavaScript 分析更一致，废弃 `@enum`、`@class` 等旧模式，并更新了类型定义语法。
- 🖥️ **编辑器体验优化**：VS Code 扩展提供无缝体验，支持多线程请求，语言服务器命令失败率降低 20 倍以上。
- 🗓️ **发布计划**：RC 版已可用，稳定版预计一个月内发布，7.1 将提供稳定 API。

---

### [发布 v12.0.0-pre.2 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.2)

**原文标题**: [Release v12.0.0-pre.2 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.2)

npm CLI v12.0.0-pre.2 预发布版本更新，包含多项新功能、错误修复和依赖更新。
- 🚀 将“链接安装策略”从实验性升级为稳定版
- 🔗 扩展替换注册表主机功能，支持 URL 前缀匹配
- 🧹 安装脚本功能新增修剪未使用的 allowScripts 条目
- 🛠️ 支持通过 .npm-extension 的 transformManifest 进行强制清单修复
- 🐛 修复 SBOM 中生成的 purl 的 vcs_url 限定符百分比编码问题
- 📋 确保 npm token list 输出所有必需参数
- 🔍 在链接策略下正确显示未声明的工作区
- 📊 报告新链接安装的添加计数
- 🗺️ 在链接策略下报告逻辑依赖位置
- 🔒 关闭 allowScripts 的三个执行缺口
- 🖇️ 在链接安装策略下解析工作区本地二进制文件
- 📦 恢复 ls 命令的 100% 测试覆盖率
- ✅ 通过名称批准没有解析 URL 的依赖
- 🚫 在严格允许脚本模式下不标记惰性可选依赖
- 🎯 将 `npm link --workspace` 的作用域限定在工作区内
- 📚 文档推荐使用 install-strategy=linked 以捕获幽灵依赖
- ⬆️ 更新多个依赖包，包括 undici、tinyglobby、postcss-selector-parser 等
- 🧩 arborist 子包修复：处理跨文件/工作区边界的覆盖、转发传递覆盖、清理旧存储目录等
- 🛠️ libnpmexec 修复：防止跨工作区运行时的共享 binPaths 污染

---

### [恢复对 `.npmrc` 中未识别键的策略 · Issue #9699 · npm/cli · GitHub](https://github.com/npm/cli/issues/9699)

**原文标题**: [Revert policy on unrecognized keys in `.npmrc` · Issue #9699 · npm/cli · GitHub](https://github.com/npm/cli/issues/9699)

### 概述摘要
npm v12 计划对`.npmrc`中的未识别键实施硬错误策略，引发了生态系统的碎片化、安全问题和配置兼容性挑战。

- 🔴 **策略问题**：npm v12 计划对`.npmrc`中未识别键实施硬错误，导致大量下游问题
- ⚠️ **生态碎片化**：pnpm 已放弃对全局`.npmrc`的支持，其他工具被迫引入独立配置文件（如`.nubrc`）
- 🛡️ **安全风险**：配置被静默丢弃，许多项目升级后未意识到安全防护被削弱
- 💔 **统一配置梦碎**：原本接近实现的跨包管理器统一配置系统因该决策而瓦解
- 🔄 **可预测的后果**：pnpm 的回应（放弃非认证`.npmrc`和`npm_config_`环境变量）本可预见
- 📋 **npm 官方理由**：安全、防拼写错误、键冲突——但这些理由的收益远不及造成的生态混乱
- 💡 **替代方案**：建议采用`x-`前缀、点命名空间、INI 节语法等逃生舱机制，或维护已知键白名单
- 📢 **核心呼吁**：在稳定版发布前撤销该策略，或至少将硬错误降级为警告

---

### [npm 为高影响力账户添加预防性账户保护 - GitHub 更新日志](https://github.blog/changelog/2026-06-25-npm-adds-preventive-account-protection-for-high-impact-accounts/)

**原文标题**: [npm adds preventive account protection for high-impact accounts - GitHub Changelog](https://github.blog/changelog/2026-06-25-npm-adds-preventive-account-protection-for-high-impact-accounts/)

npm 为高影响力账户新增预防性保护措施，在检测到敏感账户变更时自动启用 72 小时只读模式，防止账户被劫持后发布恶意版本。

- 🔒 新增保护：npm 为高影响力账户添加临时预防性保护，检测到敏感变更（如更换邮箱或使用 2FA 恢复码）时自动触发。
- ⏰ 72 小时只读：账户进入只读状态，期间可安装、下载包及查看设置，但无法发布、管理令牌或修改组织成员。
- 📧 安全通知：变更发生时，系统会向原邮箱发送警报，关闭攻击者利用账户劫持发布恶意包的漏洞。
- 🔄 自动恢复：72 小时后账户自动恢复正常，无需用户操作，依赖的包始终保持可用。
- 🛡️ 暂停操作：发布、管理令牌、更改包可见性等影响注册表或账户安全的操作被暂停。
- 📞 支持联系：若账户意外受影响或需协助，可联系 npm 支持团队。

---

### [Svelte 2026 年 7 月新特性](https://svelte.dev/blog/whats-new-in-svelte-july-2026)

**原文标题**: [What’s new in Svelte: July 2026](https://svelte.dev/blog/whats-new-in-svelte-july-2026)

Svelte 2026 年 7 月更新：配置迁移至 vite.config、显式环境变量预览、工具链全面支持新声明标签

- 🚀 SvelteKit 配置可直接在 vite.config.js 中定义，不再需要 svelte.config.js（2.62.0）
- 🔑 实验性显式环境变量功能预览，将替代 SvelteKit 3 中的$env/*模块（2.63.0）
- 📁 远程函数命令可直接接收 File 对象，无需手动封装 FormData（2.64.0）
- 🔄 远程查询可刷新其他查询，便于数据变更后失效处理（2.65.0）
- 🗜️ 预渲染的.md 和.mdx 文件现支持预压缩，提升传输速度（2.66.0）
- ⚠️ 远程表单中布尔字段未标记可选时，SvelteKit 会发出警告（2.66.0）
- 🛠️ 新增 prerender.handleInvalidUrl 选项，自定义无效 URL 处理（2.67.0）
- 🏷️ 导出 RemoteFormEnhanceInstance 等类型，便于自定义增强回调（2.68.0）
- 📨 提交的 submit 字段保留值在表单操作负载中，简化多按钮表单处理（2.68.0）
- 🧩 Svelte CLI 模板默认使用{const ...}声明标签，展示最新语法（sv@0.16.0）
- 🎨 语言工具支持 Svelte 5 的{const ...}声明标签（svelte-language-server@0.18.1）
- 🖥️ CSS 补全现可在嵌套`<style>`标签中工作（svelte-language-server@0.18.1）
- ⚡ svelte-check 新增--config 选项和实验性 tsgo 支持（svelte-check@4.7.0）
- 🌐 社区展示：COLOR LAB、Cometline、Guild Wars 3 官网等新项目
- 📚 学习资源：Agentic Engineering with Svelte 系列、Joy of Code 实时数据教程
- 🧰 新工具：Mochi（SvelteKit 替代框架）、pottz（桌面应用打包）、Svelte TV（WebGL 渲染）

---

### [Rich Harris 谈 AI 与 Svelte：框架开发中的炒作与现实 - YouTube](https://www.youtube.com/watch?v=SKjXE_wfdDY)

**原文标题**: [Rich Harris on AI & Svelte: Hype vs. Reality in Framework Development - YouTube](https://www.youtube.com/watch?v=SKjXE_wfdDY)

本頁面為 YouTube 平台相關資訊的索引，涵蓋版權、政策、開發者及法律條款等核心內容。
- 📰 提供新聞中心與聯絡我們資訊
- ©️ 明確版權歸屬於 Google LLC
- 👤 為創作者與開發者提供相關資源
- 📢 包含廣告刊登與平台運作說明
- 🔒 詳列條款、私隱及安全政策
- 🧪 介紹測試新功能機制

---

### [AI SDK 7 现已可用 - Vercel](https://vercel.com/blog/ai-sdk-7)

**原文标题**: [AI SDK 7 is now available - Vercel](https://vercel.com/blog/ai-sdk-7)

AI SDK 7 发布，每周下载量超过 1600 万次，是用于构建 AI 应用的 TypeScript SDK，支持多种模型提供商，并作为 Vercel 开源代理框架的基础层。该版本在五个关键领域增强了代理的生产能力。

- 🤖 **开发代理**：提供推理控制、工具和运行时上下文、提供商文件及技能上传、MCP 应用支持，以及终端 UI，简化代理构建流程。
- ⚙️ **运行代理**：支持工具审批、持久化工作流（WorkflowAgent）、超时设置和沙箱环境，确保代理稳定运行。
- 🔗 **集成代理框架**：通过 HarnessAgent 统一接口，可集成 Codex、Claude Code、Deep Agents、OpenCode 或 Pi 等现有代理框架。
- 📊 **观察代理**：通过遥测、Node.js 追踪通道、生命周期事件和性能统计，全面监控代理行为。
- 🎤 **超越文本代理**：支持提供商无关的实时语音交互和视频生成，扩展应用场景。

---

### [Node.js — Node.js 26.4.0（当前版本）](https://nodejs.org/en/blog/release/v26.4.0)

**原文标题**: [Node.js — Node.js 26.4.0 (Current)](https://nodejs.org/en/blog/release/v26.4.0)

Node.js 26.4.0 版本发布，包含多项新特性、性能优化和错误修复。

- 📦 新增 `node:vfs` 虚拟文件系统子系统，支持挂载自定义文件系统实例
- 🗺️ 实现包映射（Package Maps）功能，增强模块解析能力
- 🔒 TLS 新增 `certificateCompression` 证书压缩选项
- 📁 `fs.readFile()` 支持调用者提供缓冲区，减少内存分配
- 🌐 `http.closeIdleConnections()` 现在可关闭预请求套接字
- 🔗 `net.setKeepAlive()` 支持 TCP_KEEPINTVL 和 TCP_KEEPCNT 选项
- 🚀 为 AArch64 和 x86_64 架构添加实验性快速 FFI 调用 API
- 📝 `blockList` 稳定性状态更新为发布候选
- ⚡ 多项流（stream）性能优化，减少分配并改进背压处理
- 🛠️ 更新依赖：npm 11.17.0、V8、OpenSSL、SQLite 等
- 🐛 修复多个错误，包括 QUIC、加密、调试器、测试运行器等模块

---

### [模块：包 | Node.js v26.4.0 文档](https://nodejs.org/api/packages.html#package-maps)

**原文标题**: [Modules: Packages | Node.js v26.4.0 Documentation](https://nodejs.org/api/packages.html#package-maps)

Node.js v26.4.0 文档概述了 Node.js 的模块系统，特别是关于包（Packages）的配置，包括如何通过 `package.json` 文件定义模块类型、入口点、导出和导入映射，以及包映射（Package Maps）等高级功能，以支持 CommonJS 和 ES 模块的混合使用和依赖管理。

- 📦 **包定义**：包由 `package.json` 文件描述的文件夹树组成，包含该文件和所有子文件夹，直到下一个 `package.json` 或 `node_modules` 文件夹。
- 🔍 **模块系统确定**：Node.js 通过文件扩展名（`.mjs`、`.cjs`、`.js`）、`package.json` 的 `"type"` 字段（`"module"` 或 `"commonjs"`）或 `--input-type` 标志来决定文件是 ES 模块还是 CommonJS。
- ⚙️ **模块解析与加载**：`require()` 支持文件夹作为模块、扩展名搜索和 JSON 文件；`import`/`import()` 不支持文件夹模块，需要完整文件扩展名，并支持 `file://` 和 `data:` URL。
- 📝 **`package.json` 字段**：关键字段包括 `"name"`（包名）、`"main"`（默认入口点）、`"type"`（模块类型）、`"exports"`（定义入口点和子路径导出）、`"imports"`（内部模块的私有映射）。
- 🚪 **包入口点**：`"exports"` 字段是现代替代 `"main"` 的方案，支持多个入口点、条件导出和封装，防止未定义子路径被导入。
- 🌐 **条件导出**：支持根据环境（如 `"import"`、`"require"`、`"node"`、`"node-addons"`、`"default"`）映射不同路径，条件按顺序匹配，从最具体到最通用。
- 🔗 **子路径导出与模式**：通过 `"exports"` 定义子路径（如 `"./submodule.js"`），支持模式匹配（如 `"./features/*.js"`）以减少 `package.json` 膨胀，并可用 `null` 排除私有子路径。
- 🔄 **子路径导入**：`"imports"` 字段允许包内模块使用以 `#` 开头的私有映射，可映射到外部包，类似 `"exports"` 的解析规则。
- 🏷️ **自引用包**：包内模块可通过包名引用 `"exports"` 中定义的导出，但仅限于已导出的子路径。
- 🗺️ **包映射（实验性）**：通过 `--experimental-package-map` 标志启用，使用 JSON 配置文件控制裸说明符解析，适用于 monorepo、依赖隔离和低文件系统耦合。
- 📋 **社区条件定义**：包括 `"types"`、`"browser"`、`"development"`、`"production"` 等，需清晰定义且不与其他条件冲突。
- ⚠️ **限制与兼容性**：`"exports"` 引入可能破坏现有包，需确保所有先前支持的入口点被导出；包映射为静态文件，不支持动态配置。

---

### [Formisch v1 RC 现已发布 | Formisch](https://formisch.dev/blog/formisch-v1-release-candidate/)

**原文标题**: [Formisch v1 RC is now available | Formisch](https://formisch.dev/blog/formisch-v1-release-candidate/)

Formisch v1 RC 现已发布，这是一个基于 schema 驱动、无头且类型安全的表单状态管理库，支持多框架。

- 🎉 Formisch 正式进入 Release Candidate 阶段，核心 API 和设计稳定，v1 发布前不会有破坏性变更
- 📋 基于 Valibot schema 定义表单，一个 schema 同时驱动运行时验证和 TypeScript 类型，无需额外类型定义
- 🧩 无头设计，开发者完全控制标记和样式，每个字段提供值、错误和输入属性
- ⚡ 路径完全类型化，字段重命名时 TypeScript 会标记所有不匹配位置；状态基于细粒度信号，仅重新渲染变更字段；打包大小约 2.5 kB
- 🔄 支持 React、Vue、Solid、Qwik、Svelte 和 Preact，构建时自动切换框架的原生响应式系统，无适配器开销
- 🛠️ RC 阶段主要强化现有功能：测试覆盖率达 100%，优化嵌套字段、字段数组和元组处理，改进状态和焦点处理，新增 isValid、isDirty、getDeepErrors 等便捷方法
- 🚀 从 Modular Forms 和 Valibot 发展而来，目标是成为框架无关的表单平台，类似 Vite 但用于表单
- 💬 鼓励用户试用并提供反馈，可通过 Playground、StackBlitz 体验，或在 GitHub 和 Discord 上报告问题

---

### [Prettier 3.9：重大解析器升级与格式化改进 · Prettier](https://prettier.io/blog/2026/06/27/3.9.0)

**原文标题**: [Prettier 3.9: Major parser upgrades and Formatting improvements · Prettier](https://prettier.io/blog/2026/06/27/3.9.0)

Prettier 3.9 版本发布，带来了主要解析器升级和大量格式化改进，涵盖 Markdown、YAML、Flow、GraphQL、Angular 以及 JavaScript/TypeScript 等多个领域。

- 🚀 **主要解析器升级**：Markdown 解析器升级至最新的 micromark v4，YAML 解析器升级至 yaml v2，Flow 采用新的 Rust 解析器，GraphQL 支持 v17 语法。
- 🐛 **JavaScript 格式化修复**：修复了 `--no-semi` 模式下注释、括号、空行、IIFE 函数、JSDoc 等多处问题，并优化了逻辑表达式、模板插值、成员链等格式。
- 🛠️ **TypeScript 改进**：修复了成员链换行、类型断言、联合类型、条件类型、类继承、枚举键引用、映射类型注释等多处问题，并优化了 `no-semi` 模式下的分号处理。
- 💧 **Flow 增强**：新增对 Flow 记录、匹配实例模式、隐式声明函数/组件、`writeonly`/`in`/`out` 方差修饰符的支持，并修复了可选返回类型、注释格式等问题。
- 📝 **Markdown 与 YAML 修复**：修复了 Markdown 中 CJK 换行、列表缩进代码块、setext 标题等问题；YAML 修复了键换行、块标量空格、空行保留等问题。
- 🎨 **CSS/SCSS/HTML/Angular 改进**：修复了 CSS 属性值换行、SCSS 尾逗号、HTML 注释与预格式化元素、Angular `@content` 块支持等问题。
- 🔧 **CLI 与杂项**：修复了特殊字符目录名崩溃、EditorConfig 搜索范围、缓存策略、文件名引号等问题，并更新了实验性 CLI 和 Printer 接口。

---

### [发布 Rspack 2.1 - Rspack](https://rspack.rs/blog/announcing-2-1)

**原文标题**: [Announcing Rspack 2.1 - Rspack](https://rspack.rs/blog/announcing-2-1)

## 概述总结
Rspack 2.1 正式发布，带来性能提升、新功能、输出优化及生态系统更新。

- 🚀 **性能大幅提升**：React Compiler Rust 版本比 Babel 版本快 7-13 倍；生产构建性能提升约 16%，HMR 提升约 5%
- 🦀 **React Compiler Rust 化**：通过内置 SWC 加载器直接启用，无需额外 Babel 转换开销
- 📘 **TypeScript 7 支持**：`ts-checker-rspack-plugin` 支持 TS7 类型检查，构建时间减少约 60%
- 🔄 **更快的循环依赖检查**：新增 `CircularCheckRspackPlugin`，采用图算法一次性检测循环组件，性能更优
- 🌐 **import.meta.glob 支持**：通过 glob 模式收集模块并按需加载，与 Vite/Turbopack 语法一致
- 🎨 **CSS 支持增强**：新增 `css/global` 模块类型，支持“全局默认，按需 :local”模式
- 📦 **createRequire 解析支持**：可静态分析 ESM 中通过 `createRequire` 创建的 require 调用
- ✨ **Magic Comments 升级**：支持 `rspack` 前缀的魔法注释，同时兼容 `webpack` 前缀
- 🔌 **Source Phase Imports 支持**：支持 TC39 提案，可导入未实例化的 WebAssembly.Module
- 🗑️ **持久缓存自动清理**：新增 `cache.maxAge`（默认 7 天）和 `cache.maxVersions`（默认 3 个版本）自动清理旧缓存
- 🌳 **pureFunctions 稳定化**：生产模式默认启用，可安全移除无副作用的函数调用
- 🔪 **分支感知依赖剪枝**：根据内联常量条件，自动标记不可达分支的依赖为无效
- ✅ **分支感知 ESM 导出检查**：识别 `in` 表达式保护下的导出访问，减少误报
- ⚡ **export const 值绑定优化**：非循环模块中，const 导出直接定义为只读值，减少 getter 调用开销
- 🧩 **生态系统更新**：TanStack RSC 支持、Rsbuild 2.1、Rslib 快速类型生成、Rstest 0.10 测试过滤、Rslint 400+ 内置规则、Rspress AI 技能、Rsdoctor AI 分析、rspack-merge 配置合并工具

---

### [发布 electron v43.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v43.0.0)

**原文标题**: [Release electron v43.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v43.0.0)

Electron v43.0.0 正式发布，包含多项堆栈升级、新功能、性能改进和错误修复。

- 🚀 **堆栈升级**：Chromium 升级至 150.0.7871.46，Node 升级至 v24.147.0，V8 升级至 15.0。
- 🆕 **新增功能**：包括 WebContents 克隆方法、macOS 通知管理、WebAuthn Touch ID 支持、全局快捷键暂停/恢复、堆栈跟踪支持等。
- ⚡ **性能改进**：应用启动性能提升，预加载脚本缓存为 V8 字节码，Linux/Windows 启用 ThinLTO 优化，V8 内置函数性能优化。
- 🐛 **错误修复**：修复了桌面捕获器挂起、frameless 窗口缩放、PDF 渲染崩溃、通知图标保存失败、DevTools 功能异常等大量问题。
- 🛠️ **其他变更**：回传上游 Chromium 修复，修复 Apple Silicon 上 Buffer/TextEncoder 的静默数据截断问题。
- 📅 **平台支持变更**：Electron 43.x.y 将是最后一个支持 32 位平台（Windows x86 和 Linux ARM）的版本系列。
- ⏳ **版本生命周期**：Electron 40.x.y 已结束支持，建议用户升级到更新版本。

---

### [ESLint v10.6.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/06/eslint-v10.6.0-released/)

**原文标题**: [ESLint v10.6.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/06/eslint-v10.6.0-released/)

ESLint v10.6.0 发布，这是一个次要版本升级，新增了功能并修复了多个错误。

- 🆕 新增 `no-constant-binary-expression` 规则的 `checkRelationalComparisons` 选项，可检测结果恒定的关系比较（如 `"a" > "b"` 总是 `false`）
- 🔧 改进了多个规则的正确性和边缘情况行为，包括 `max-classes-per-file`、`max-nested-callbacks`、`no-constant-binary-expression`、`no-extra-boolean-cast`、`no-promise-executor-return`、`no-throw-literal`、`prefer-exponentiation-operator`、`prefer-promise-reject-errors` 和 `radix`
- ✨ 新增功能：在 `no-constant-binary-expression` 中检测 `Symbol()` 和 `BigInt()`，并添加 `checkRelationalComparisons` 选项
- 🐛 修复多个错误，包括 `prefer-exponentiation-operator` 在语句开头的自动修复问题、`no-extra-boolean-cast` 中阴影 `Boolean` 的处理、`radix` 和 `no-throw-literal` 中阴影 `undefined` 的报告、`no-promise-executor-return` 中的无效类建议、`prefer-promise-reject-errors` 中阴影 `Promise` 的误报、`max-classes-per-file` 的报告范围、`max-nested-callbacks` 中 IIFE 的回调检测逻辑等
- 📚 更新了文档，包括 README、TypeScript 配置指南、代码路径图，并修复了 `prefer-const` 规则描述中的语法问题
- 🔄 进行了多项杂务更新，如 CI 流程优化、依赖项升级（markdown-it 到 v14、prettier 到 v3.8.4）、生态系统插件更新等

---

### [pnpm 11.9 | pnpm](https://pnpm.io/blog/releases/11.9)

**原文标题**: [pnpm 11.9 | pnpm](https://pnpm.io/blog/releases/11.9)

pnpm 11.9 版本发布，主要修复了多项问题并增加了新功能，包括为无法提供校验和的注册表自动计算 tarball 完整性、新增 `pnpm sbom --exclude-peers` 选项，以及改进了审计性能和依赖解析的确定性。

- 🔒 **完整性校验增强**：对于无法在元数据中提供校验和的注册表，pnpm 现在会在下载 tarball 后自动计算完整性并存入锁文件，后续安装可验证；若锁文件条目缺失完整性，会直接报错 `ERR_PNPM_MISSING_TARBALL_INTEGRITY` 而非静默重试。
- 📋 **SBOM 排除对等依赖**：新增 `pnpm sbom --exclude-peers` 标志，可移除对等依赖及其仅通过对等依赖可达的传递子树，与 `pnpm list --exclude-peers` 命名一致。
- 🛠️ **审计性能与修复改进**：`pnpm audit --fix` 现在为每个包合并写入单一的 `minimumReleaseAgeExclude` 条目；修复了循环依赖锁文件导致的审计性能回归，采用 Tarjan 强连通分量算法保持线性时间与内存。
- 🔄 **依赖解析确定性修复**：修复了可选传递对等依赖可能被随机添加或移除的非确定性解析问题，消除了锁文件变动和 `pnpm dedupe --check` 间歇性失败。
- 🪟 **Windows 兼容性优化**：修复了 `pnpm dlx` 在 Windows 上因清理失败导致原始错误被 `EBUSY` 掩盖的问题；缩短了缓存路径以避免深度依赖树超过 `MAX_PATH` 限制。
- 🚫 **网络与错误处理增强**：修复了非可重试网络错误（如 `SELF_SIGNED_CERT_IN_CHAIN`）导致 pnpm 挂起或崩溃的问题；注册表获取失败不再泄露内嵌在 URL 中的基本认证凭据。
- 🧹 **配置与排除逻辑修正**：修复了 `minimumReleaseAgeExclude` 和 `trustPolicyExclude` 中同一包的多个精确版本条目未正确合并为 `||` 析取的问题；`pnpm install --ignore-workspace` 不再覆盖 `pnpm-workspace.yaml` 中的 `allowBuilds` 映射。
- 🗂️ **元数据缓存优化**：在精确版本磁盘快速路径上填充内存中的包元数据缓存，避免大型单体仓库安装时重复磁盘读取；缓存键现包含注册表信息，防止不同注册表的同名包共享缓存。
- 🏷️ **其他修复与调整**：修复了 `pnpm patch` 在依赖解析为单个 git 托管版本时丢失包名的问题；移除了运行时依赖后同步清理匹配的 `devEngines.runtime` 或 `engines.runtime` 条目；`pnpm sbom` 现在为声明了 `bugs` URL 的组件发射 CycloneDX `issue-tracker` 外部引用。

---

### [为什么 Drizzle ORM 一个月无法在 NPM 上发布新版本 | vlt /vōlt/](https://www.vlt.io/blog/packument-size-limits)

**原文标题**: [Why Drizzle ORM couldn't publish new releases on NPM for a month | vlt /vōlt/](https://www.vlt.io/blog/packument-size-limits)

### 概述总结
Drizzle ORM 因 npm 包清单（packument）超过 100MB 限制，导致一个月内无法发布新版本。该限制源于 npm 注册表将所有版本元数据合并为一个文档，而 Drizzle 因频繁发布快照版本（每个版本约 131KB）迅速耗尽容量。最终通过 npm 支持团队删除旧版本解决，但暴露了注册表效率问题及替代方案。

- 📦 **问题根源**：npm 注册表将每个包的所有版本元数据存储为单一文档（packument），当 Drizzle ORM 的 packument 超过 100MB 时，新版本发布被阻止。
- 🚀 **触发原因**：Drizzle 每个版本约 131KB，且近期自动发布大量快照版本，仅需约 763 个版本即可达到 100MB 限制。
- 🛠️ **解决方案**：由于 npm 禁止 72 小时后删除版本，Drizzle 只能联系 npm 支持团队手动清理旧版本，最终将 packument 降至 61MB。
- ⚠️ **风险警示**：频繁发布开发版本或大型 package.json 的包易触发该限制，建议通过命令`curl -s https://registry.npmjs.org/<包名> | wc -c`监控 packument 大小。
- 💡 **优化建议**：避免发布所有开发构建版本，可考虑使用替代注册表（如私有注册表）存储快照；同时建议客户端支持按版本范围筛选，减少冗余数据传输。
- 🔄 **替代方案**：部分镜像注册表（如作者提供的服务）通过白名单机制仅保留必要元数据，将 Drizzle 的 packument 压缩至 1.7MB，大幅降低风险。

---

### [Drizzle ORM - 下一代 TypeScript ORM](https://orm.drizzle.team/)

**原文标题**: [Drizzle ORM - next gen TypeScript ORM.](https://orm.drizzle.team/)

Drizzle ORM 是一个高性能、类型安全的 TypeScript ORM，支持多种数据库和运行时环境，提供丰富的查询构建、迁移管理和数据操作功能。

- 🚀 **高性能**：通过 JIT 行映射器和优化查询，Drizzle 在基准测试中表现出极低的延迟和 CPU 负载，远超 Prisma 等竞品。
- 🗄️ **多数据库支持**：原生支持 PostgreSQL、MySQL、SQLite、SingleStore、MSSQL、CockroachDB、Gel 等主流数据库，并适配 Neon、Supabase、Turso 等云服务。
- 🔧 **完整工具链**：提供 `drizzle-kit` 命令行工具，支持模式生成、迁移、推送、拉取、导出和 Studio 可视化数据管理。
- 🧩 **类型安全**：基于 TypeScript 构建，提供强类型查询构建器，支持 Zod、Valibot、TypeBox 等验证库集成。
- 🌐 **跨运行时兼容**：支持 Node.js、Bun、Deno、Cloudflare Workers、Vercel Functions 等服务器端和无服务器环境。
- 🛡️ **高级特性**：支持行级安全（RLS）、事务、批量操作、缓存层、读副本、自定义类型和代码映射。
- 🆕 **持续迭代**：频繁发布新版本，引入 Gel 方言、MSSQL 支持、CockroachDB 支持、改进的迁移引擎和性能优化。
- 🎨 **开发者体验**：提供直观的 API、丰富的文档、社区支持和活跃的 Discord 社区，广受开发者好评。
- 🧪 **测试与稳定性**：拥有超过 7000 个测试用例，确保跨方言和命令的可靠性。
- 💡 **创新功能**：支持关系查询 V2、种子数据生成、SQL 控制台、Explain/Analyze 分析和 LLM 代理集成。

---

### [CSS 状态与 JavaScript 事件之间的界限变化 | CSS-Tricks](https://css-tricks.com/css-states-and-javascript-events/)

**原文标题**: [The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks](https://css-tricks.com/css-states-and-javascript-events/)

### 概述总结
CSS 正通过伪类模拟 JavaScript 事件监听，而即将到来的 `event-trigger` 功能将进一步模糊两者界限，为开发者提供更多选择。

- 🖱️ **:hover 和 :active** 分别对应指针进入/离开和按下/释放事件，但本质是状态而非事件
- 🔍 **:focus 和 :focus-visible** 模拟焦点事件，后者通过浏览器启发式判断是否显示焦点环
- 🧩 **:focus-within 和 :has()** 实现父元素根据子元素状态改变样式，:has() 更通用
- ✅ **:checked** 对应 change 事件，但伪类直接捕获选中状态
- 📝 **:valid/:invalid 与 :user-valid/:user-invalid** 前者立即触发，后者等待用户交互后触发，模拟 change 事件行为
- 🎬 **媒体元素伪类**（:buffering、:paused、:playing 等）对应 waiting、pause、playing 等事件，:volume-locked 无直接 JS 等价
- 🗂️ **:popover-open、:open、:modal** 对应 toggle 事件，但无需 JS 即可检测弹窗/对话框/详情元素状态
- 🖥️ **:fullscreen** 对应 fullscreenchange 事件，直接检测全屏状态
- 🔗 **:target** 对应 hashchange 事件，检测 URL 哈希匹配元素
- ⚡ **event-trigger** 新功能允许用 CSS 监听事件（如 click、interest）并触发动画，支持状态 ful（如 interest 进入/退出）和状态 less（如 click）触发方式

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Cloud 提供大规模时序数据处理的 PostgreSQL 服务，支持企业级部署与快速扩展。

- 🚀 单服务可处理每天 3 万亿指标、3PB 数据及 1 千万亿数据点
- 💰 新用户注册即获 30 天有效期的$1000 信用额度，无需信用卡
- 🔄 支持读写分离，最多 10 节点副本集，搭配分层 SSD/S3 实现无限低成本存储
- ⚡ 计算与存储分离架构，独立扩展避免闲置容量浪费
- 🛡️ 多可用区集群自动故障切换，支持时间点恢复与跨区域备份
- 🔐 符合 SOC 2、HIPAA、GDPR 标准，具备加密、SSO、RBAC 及审计日志
- 📊 深度可观测性：查询下钻、性能仪表盘，集成 CloudWatch、Datadog、Prometheus
- ⏱️ 数分钟内完成数据库部署，支持 SQL、CLI、Terraform、Cursor、Claude Code 管理
- 🔌 与主流云提供商及 PostgreSQL 生态系统无缝集成
- 🌐 企业级保障：合同化 SLA、区域数据隔离、24/7 全球专家支持

---

### [阻止安装脚本并非万能之策](https://nodesource.com/blog/npm-v12-install-scripts-not-a-silver-bullet)

**原文标题**: [Blocking Install Scripts Is Not a Silver Bullet](https://nodesource.com/blog/npm-v12-install-scripts-not-a-silver-bullet)

npm v12 关闭了安装脚本的自动执行，但这并非安全银弹，恶意代码会转向运行时执行。真正的防御需要结合权限模型和沙箱环境。

- 🔒 npm v12 默认关闭 `allowScripts`、`--allow-git` 和 `--allow-remote`，阻止安装时自动执行脚本
- 🚨 攻击者已从安装时攻击转向运行时攻击，通过顶级代码的 IIFE 在导入时执行恶意逻辑
- 🛡️ Node.js 权限模型（`--permission`）可限制运行时代码的能力，如阻止子进程、网络访问和文件写入
- ⚠️ 权限模型并非安全边界，存在绕过漏洞（如 CVE-2026-21636），且不限制 `process.env` 读取
- 🏗️ 建议结合容器、网络出口白名单和 CI 的 egress 监控（如 Harden-Runner）实现深度防御
- 📋 升级前需审查原生模块（如 bcrypt）的构建脚本，运行 `npm approve-scripts` 并提交白名单
- 🔍 在 CI 中启用权限模型和出口控制，可有效遏制恶意依赖的破坏范围

---

### [npm v12 即将到来的重大变更 - GitHub 更新日志](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

**原文标题**: [Upcoming breaking changes for npm v12 - GitHub Changelog](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

npm v12 即将发布，带来多项安全相关的默认变更，旨在减少自动执行的潜在风险，用户需提前在 npm 11.16.0+ 中通过警告进行准备。

- 🛡️ **allowScripts 默认关闭**：`npm install` 不再自动执行依赖中的 `preinstall`、`install`、`postinstall` 脚本（包括原生 `node-gyp` 构建），需通过 `npm approve-scripts` 显式信任。
- 🚫 **--allow-git 默认设为 none**：`npm install` 不再解析 Git 依赖（直接或间接），防止通过 `.npmrc` 覆盖 Git 可执行文件的安全漏洞。
- 🌐 **--allow-remote 默认设为 none**：`npm install` 不再解析远程 URL 依赖（如 HTTPS tarball），需通过 `--allow-remote` 显式允许。
- ⚙️ **如何准备**：升级至 npm 11.16.0+，运行 `npm approve-scripts --allow-scripts-pending` 查看待处理脚本，信任后提交更新后的 `package.json`，未批准的脚本将在升级后停止运行。
- 📅 **发布时间**：npm v12 预计于 2026 年 7 月发布，当前版本（11.16.0+）已提供警告和迁移工具。

---

### [肯尼斯·斯科夫胡斯 | 将 Linear 从 styled-components 迁移至 StyleX](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

**原文标题**: [Kenneth Skovhus | Moving Linear from styled‑components to StyleX](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

### 概述总结
Linear 团队将 React 应用从 styled-components 迁移到 StyleX，主要出于性能优化和构建更严格的样式基础。迁移过程使用代理辅助工作流，已转换超过 58% 的文件，页面渲染速度提升约 30%。

- 🚀 **性能提升**：消除运行时 CSS 生成和注入，页面间导航渲染速度提升约 30%
- 🔧 **迁移原因**：styled-components 进入维护模式，未采用`useInsertionEffect`优化；StyleX 提供最小运行时、更强封装和确定性样式解析
- 📦 **迁移工具**：开发了包含 10 万行代码的 codemod 工具，支持增量迁移，已处理 500+PR
- 🎯 **核心要求**：最小运行时、强封装、确定性解析、健康生态、良好开发体验
- 🧩 **迁移策略**：先定义样式基础，从叶子节点开始增量迁移，配合严格 lint 规则和 CSS Modules 逃生舱
- 🤖 **代理辅助**：代理可处理大量工作，但人类仍需检查视觉正确性（如悬停状态、主题分支）
- 📉 **挑战**：无设计系统导致迁移成本高，需收紧组件 API，处理复杂嵌套主题和父级依赖选择器

---

### [Tanner Linsley 打造 TanStack 以求其超越自身 · 构建日志 S1.E2 - YouTube](https://www.youtube.com/watch?v=rCJ9OdNdigQ)

**原文标题**: [Tanner Linsley Built TanStack to Outlive Him · The Build Log S1.E2 - YouTube](https://www.youtube.com/watch?v=rCJ9OdNdigQ)

本頁面列出了 YouTube 平台相關的資訊與政策連結，涵蓋版權、合作、開發及法律條款等核心內容。

- 📰 新聞中心：提供 YouTube 官方新聞與公告資訊
- ©️ 版權：說明內容版權相關規範與申訴機制
- 📞 聯絡我們：提供用戶與創作者聯繫 YouTube 的管道
- 🎬 創作者：針對內容創作者提供的資源與支援
- 📢 刊登廣告：介紹廣告投放選項與合作方式
- 💻 開發人員：提供 API 與開發工具相關資訊
- ⚖️ 條款：列出使用 YouTube 服務的條款與條件
- 🔒 私隱：說明用戶資料收集與使用方式
- 🛡️ 政策及安全：包含社群規範與安全措施
- 🤖 YouTube 的運作方式：解釋平台推薦與內容管理機制
- 🧪 測試新功能：介紹正在測試中的新功能
- 📅 © 2026 Google LLC：版權歸屬與年份標示

---

### [TanStack | 面向网页的开源应用技术栈。](https://tanstack.com/)

**原文标题**: [TanStack | The open-source application stack for the web.](https://tanstack.com/)

TanStack 是一个面向现代 Web 应用的开源技术栈，提供无头、类型安全、可组合的工具，支持开发者与 AI 代理，拥有庞大的 NPM 下载量和 GitHub 星标。

- 📚 **丰富的库生态**：涵盖框架（Start、Router）、数据管理（Query、DB、Store、AI）、UI/UX（Table、Form、Hotkeys）、性能（Virtual、Pacer）和工具（Devtools、Config、CLI、Intent），全部开源。
- 🔧 **核心设计原则**：框架无关（支持 React、Vue、Solid、Angular 等）、类型安全（TypeScript 优先）、生产级验证、无供应商锁定（MIT 许可）。
- 🤝 **社区与支持**：提供 Discord 社区、YouTube 频道、专业工作坊、合作伙伴计划和企业支持，维护者团队活跃。
- 📈 **最新动态**：TanStack Start 和 AI 赢得 2026 年开源奖项，博客分享技术优化（如内存节省 90%）和 AI 沙箱集成。
- 🏆 **赞助与认可**：有金、银、铜级合作伙伴和 OSS 赞助商，赞助商享有专属 Discord 频道和优先支持。

---

### [选择你的战斗者：为 Node.js 基准测试 5 个 WebSocket 服务器——火星编年史，邪恶火星人团队博客](https://evilmartians.com/chronicles/choose-your-fighter-benchmarking-5-websocket-servers-for-nodejs)

**原文标题**: [Choose your fighter: benchmarking 5 WebSocket servers for Node.js—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/choose-your-fighter-benchmarking-5-websocket-servers-for-nodejs)

本篇文章比较了五种在 Node.js 上运行 WebSocket 的方式，并揭示了基准测试中测量工具本身可能带来的偏差。作者通过多次实验和调整，最终得出了各方案在延迟、可靠性、恢复能力和资源占用方面的真实表现。

- 📊 **延迟表现相近**：在 10K 订阅者下，所有方案的原始延迟都在几毫秒内，差异不大。
- 🛡️ **AnyCable 可靠性领先**：在网络丢包模拟中，AnyCable 实现了 100% 消息送达，而默认 Socket.io 丢失约 15%。
- 🔄 **AnyCable 部署恢复能力强**：面对部署时的重连风暴，AnyCable 无需重启即可平稳过渡，而 uWebSockets.js 需要数秒恢复。
- 💾 **资源占用差异显著**：uWebSockets.js 每个连接最轻量（5 KB），AnyCable Pro 为 18 KB，Socket.io 约 52 KB，且 Socket.io 单机连接数上限约 120K。
- ⚠️ **基准测试陷阱**：作者发现测量工具（如笔记本电脑）会引入巨大偏差，例如将测量工具自身的延迟误判为服务器延迟，导致 AnyCable 的 p99 延迟被高估 20 倍。
- 🔧 **关键方法论**：将负载生成器与服务器放在同一内部网络，使用多分片避免单进程瓶颈，并始终用独立方法验证每一个惊人结果。
- 🏆 **最终得分榜**：AnyCable 在抖动下 100% 送达、部署无中断、大规模广播吞吐量领先（p99 比 uWS 低 10 倍），且延迟与竞品持平。

---

### [使用 TanStack Query 处理 Vue 中的变更](https://www.telerik.com/blogs/handling-mutations-tanstack-query-vue)

**原文标题**: [
	Handling Mutations with TanStack Query for Vue
](https://www.telerik.com/blogs/handling-mutations-tanstack-query-vue)

本文介绍了如何在 Vue 中使用 TanStack Query 处理数据变更（Mutation），包括创建、更新、删除等操作，并涵盖生命周期、缓存同步和乐观更新等高级功能。

- 📘 **Mutation 基础**：Mutation 用于修改服务器数据（如 POST、PUT、DELETE），通过 `useMutation` 钩子实现，返回 `mutate` 函数和 `isPending`、`isError` 等状态。
- 🔄 **mutate vs mutateAsync**：`mutate` 是“即发即忘”模式，错误通过响应式状态处理；`mutateAsync` 返回 Promise，适合需要 `await` 的场景，但需手动处理错误。
- ⚙️ **生命周期回调**：支持 `onSuccess`、`onError`、`onSettled` 回调，可在定义 mutation 或调用 `mutate` 时传入，用于处理成功、失败或清理逻辑。
- 🔁 **查询失效**：通过 `queryClient.invalidateQueries` 在 mutation 成功后使相关查询缓存失效，自动触发数据刷新，保持 UI 同步。
- 🚀 **乐观更新**：通过 `onMutate` 回调预先更新缓存，并在失败时回滚，提升用户体验，但建议仅在需要即时反馈的场景使用。
- 🧩 **实际应用**：mutation 与 `invalidateQueries` 结合，可统一管理表单提交、按钮点击等操作，避免手动管理加载状态和缓存刷新。

---

### [使用 Chrono 和 Web 组件解析字符串中的任意日期](https://www.raymondcamden.com/2026/06/24/parsing-arbitrary-dates-in-strings-with-chrono-and-a-web-component)

**原文标题**: [Parsing Arbitrary Dates in Strings with Chrono and a Web Component](https://www.raymondcamden.com/2026/06/24/parsing-arbitrary-dates-in-strings-with-chrono-and-a-web-component)

### 概述总结
本文介绍了如何使用 Chrono 库解析字符串中的日期，并构建一个 Web 组件来高亮显示日期内容。

- 📅 **Chrono 库功能**：可解析自然语言中的日期，如“Sep 12-13”或“tomorrow”，并返回日期对象，支持参考日期和持续时间。
- ⚙️ **解析方法**：`parseDate()`直接返回日期，`parse()`返回包含起始索引、文本和日期对象的详细结果。
- 🧪 **演示示例**：通过 CodePen 展示实时解析文本输入，自动提取日期并显示解析结果。
- 🔧 **Web 组件设计**：创建`<time-parse>`组件，自动识别文本中的日期，并用`<time>`标签包裹，设置`datetime`和`title`属性。
- 🎨 **样式与参考日期**：组件使用下划线高亮日期，支持通过`date`属性指定参考日期（如`date="2026-06-04"`）。
- 📝 **实现细节**：组件通过`connectedCallback()`解析内部文本，反向遍历匹配项，用`<time>`替换原文本，并处理时区格式。
- ⚠️ **注意事项**：持续时间解析可能不完美（如“10 to 11 AM”），但起始日期解析稳定；组件未使用 Shadow DOM，采用内联样式简化。

---

### [介绍 Nub：Node.js 的一体化工具包 — Nub](https://nubjs.com/blog/introducing-nub)

**原文标题**: [Introducing Nub: an all-in-one toolkit for Node.js — Nub](https://nubjs.com/blog/introducing-nub)

### 概述总结
Nub 是一个基于 Rust 构建的 Node.js 全功能工具包，通过增强而非替代原生 Node.js，提供 TypeScript 直接运行、更快的脚本执行、包管理及版本管理等功能，旨在现代化 Node.js 开发体验。

- 🚀 **核心定位**：Nub 是一个增强 Node.js 的工具包，而非替代品。它使用 Rust CLI 在原生 Node 上运行代码，兼容 98.8% 的 Node 生态。
- ⚡ **性能优势**：脚本运行器比 `pnpm run` 快 24 倍，二进制运行器比 `npx` 快 19 倍，TypeScript 文件运行比 `tsx` 快 2.9 倍。
- 🛠️ **多功能集成**：提供文件运行器（支持 TypeScript/JSX/装饰器）、脚本运行器、二进制运行器、文件监听器、包管理器（兼容 pnpm）和 Node 版本管理器。
- 🔒 **安全特性**：包管理器默认禁止生命周期脚本、阻止非注册表依赖、要求新版本发布后至少 24 小时冷却期，并支持构建脚本沙箱。
- 🌐 **现代 API 支持**：内置 Worker、Temporal、WebSocket、EventSource 等 API 的跨版本兼容，无需手动配置。
- 📦 **零锁定**：无专属 API、模块或配置文件，移除 Nub 后代码仍可正常运行，完全兼容现有 Node 项目。
- 🔄 **版本管理**：自动根据 `.node-version` 或 `package.json#engines` 解析并安装对应 Node 版本，无需手动干预。
- 💡 **TypeScript 优先**：支持枚举、命名空间、参数属性等非可擦除语法，并自动读取 `tsconfig.json#paths` 别名。

---

### [简介 | Zod](https://zod.dev/)

**原文标题**: [Intro | Zod](https://zod.dev/)

Zod 4 是 TypeScript 优先的验证库，支持从简单字符串到复杂嵌套对象的数据模式定义，具有零依赖、轻量核心、不可变 API 和 JSON Schema 转换等特性。

- 📦 **核心特性**：零外部依赖，2kb 核心包（gzip），支持 Node.js 和现代浏览器，TypeScript 优先并自动推断类型。
- 🔧 **安装与要求**：通过 npm 安装，需启用 `tsconfig.json` 中的 `strict` 模式，支持 TypeScript v5.5+。
- 🌐 **生态系统**：拥有丰富的库和集成，包括 tRPC、React Hook Form 等，提供 MCP 服务器用于文档搜索。
- 💰 **赞助商**：提供多层级赞助（白金、金、银、铜），如 coderabbit.ai、neon.tech 等。

---

### [发布 v0.2.0 · nubjs/nub · GitHub](https://github.com/nubjs/nub/releases/tag/v0.2.0)

**原文标题**: [Release v0.2.0 · nubjs/nub · GitHub](https://github.com/nubjs/nub/releases/tag/v0.2.0)

Nub v0.2.0 发布，新增 Web Worker 支持并强化了包管理器兼容性。

- 🚀 新增 Web Worker 支持：在 Node 中实现浏览器标准的 `Worker` 构造函数，支持 TypeScript/JSX 直接运行、内联 Worker、Classic 和 Module 模式，以及 `MessageEvent`/`ErrorEvent` 等规范特性。
- 🛠️ 包管理器兼容性修复：修复 yarn-berry 目录解析、pnpm 工作区版本链接、凭证泄露和 `minimumReleaseAgeExclude` 等问题，并解决 `packageManager` URL 格式崩溃。
- 🐳 工具与分发改进：推出官方 Docker 镜像（node:26 slim + alpine），新增 Homebrew 自动更新，并拆分 `nub-native` 工作区以优化构建。
- 📚 文档更新：添加 Node 版本/层级表、WebSocket/EventSource 说明、`/regex/` 多脚本选择器文档，以及 Homebrew 安装路径。
- 🧪 测试与内部优化：引入 WPT Worker 一致性测试、Node 版本矩阵烟雾测试，并修复多个构建和测试脚本错误。

---

### [Gea — 编译器优先的响应式用户界面](https://geajs.com/)

**原文标题**: [Gea — Compiler-First Reactive UI](https://geajs.com/)

Gea 是一个以编译器为核心的 UI 框架，通过将普通 JavaScript 类和函数转化为高效的 DOM 更新，实现了无需虚拟 DOM、无钩子、无信号的极致性能。

- 📜 **核心理念**：JavaScript 本身就是 API，无需学习新概念。类、函数和 getter 就是全部。
- ⚡ **编译时响应性**：Vite 插件在构建时分析 JSX，自动生成精确的 DOM 更新代码。
- 🎯 **无虚拟 DOM**：直接修改变化的元素，无 diff 和 reconciliation 开销。
- 🧬 **基于 Proxy 的 Store**：普通类通过深度 Proxy 实现响应式，数组方法和嵌套对象都支持。
- 📦 **极致轻量**：Hello World 仅 121 B (brotli)，且框架运行时在构建时可完全消失。
- 🛠️ **完整工具链**：内置路由、35+ 无障碍 UI 组件、移动端原语、VS Code 扩展和项目脚手架。
- 🚀 **性能领先**：在 js-framework-benchmark 中得分 1.02，超越 Solid、Svelte、Vue 和 React。
- 💻 **快速上手**：`npm create gea@latest my-app` 一键创建 Vite + TypeScript 项目。

---

### [GitHub - dashersw/gea：一个功能完备、响应式的JavaScript UI 框架。无虚拟 DOM。编译时 JSX 转换。基于代理的存储。精准的 DOM 修补。](https://github.com/dashersw/gea#compile-to-almost-nothing)

**原文标题**: [GitHub - dashersw/gea: A batteries-included, reactive JavaScript UI framework. No virtual DOM. Compile-time JSX transforms. Proxy-based stores. Surgical DOM patching. · GitHub](https://github.com/dashersw/gea#compile-to-almost-nothing)

Gea 是一个以编译器优先的响应式 JavaScript UI 框架，摒弃虚拟 DOM，通过编译时 JSX 转换和代理存储实现极小的打包体积和高效的 DOM 更新。

- 📦 **极小的打包体积**：Hello World 生产构建仅 121 B（brotli），交互式待办应用仅 4.9 KB（brotli），远小于 React、Vue、Svelte 等主流框架。
- 🚫 **无虚拟 DOM**：编译时分析 JSX 并生成精准的 DOM 补丁，只更新实际变化的元素，无 diff 或 reconciliation 开销。
- 🔄 **基于代理的响应性**：直接修改状态（如 `this.count++`），框架自动处理 DOM 更新，无需信号、钩子或依赖数组。
- 🧩 **熟悉的 JavaScript**：使用类、函数、对象和 getter 构建 UI，无需学习新编程模型；JSX 支持 `class` 和 `click={fn}` 等原生语法。
- 🛠️ **编译时优化**：Vite 插件在构建时分析代码并连接响应性，静态应用中框架运行时几乎消失。
- 📚 **丰富的功能包**：包括核心框架、无头 UI 原语、移动 UI 组件、服务端渲染和 Vite 插件，支持路由、可访问性和移动端导航。
- ⚡ **高性能基准**：在 js-framework-benchmark 中，加权几何平均为 1.02，接近手写原生 JavaScript 的性能。
- 🧪 **示例与文档**：提供飞行值机、待办应用、看板、Jira 克隆等示例，以及完整的文档和 AI 辅助开发工具。

---

### [现已推出：Depot CI API 和 CLI](https://depot.dev/blog/now-available-depot-ci-api?utm_source=fnf&utm_medium=newsletter&utm_campaign=depot-june&utm_term=javascript-weekly&utm_content=depot-ci-api)

**原文标题**: [Now available: Depot CI API and CLI](https://depot.dev/blog/now-available-depot-ci-api?utm_source=fnf&utm_medium=newsletter&utm_campaign=depot-june&utm_term=javascript-weekly&utm_content=depot-ci-api)

Depot CI API 和 CLI 现已全面可用，允许用户和 AI 代理通过命令行或 API 完成所有仪表盘操作，无需切换浏览器。

- 🚀 **全面可编程性**：Depot CI API 和 CLI 正式发布，支持通过终端或代理完成所有仪表盘功能，无需离开工作环境。
- 🤖 **AI 代理友好**：软件不再仅限浏览器操作，代理可直接访问运行、日志、工作流等信息，实现“问即答”的调试体验。
- 📜 **单一事实来源**：基于 protobuf/Connect API 生成 OpenAPI v3 规范，确保 CLI、脚本和代理使用同一份实时更新的接口描述。
- 🔧 **核心功能**：支持查看运行和工作流、拉取日志、启动/取消运行、管理密钥和变量，以及获取 AI 生成的运行摘要和指标。
- ⭐ **诊断命令**：`depot ci diagnose` 可自动分析失败步骤、提取关键错误行，并给出原因和下一步建议，避免日志洪流。
- 📉 **智能简化**：诊断功能会折叠相似的大矩阵失败，提供精确的深入命令，并默认避免信息过载。
- 💰 **无额外费用**：API 和 CLI 使用现有按用量定价，仅对计算资源（如运行工作流）收费，API 调用本身不产生额外费用。
- 📈 **持续更新**：未来新功能将同步在 API、CLI 和仪表盘中发布，确保一致性。

---

### [GitHub - educastellano/qr-code: 用于生成二维码的 Web 组件 · GitHub](https://github.com/educastellano/qr-code)

**原文标题**: [GitHub - educastellano/qr-code: Web Component for generating QR codes · GitHub](https://github.com/educastellano/qr-code)

这是一个用于生成二维码的 Web 组件项目，基于 qr.js 库开发，支持多种格式和自定义样式。

- 📦 可通过 npm 安装，使用`import 'webcomponent-qr-code'`引入，支持自定义组件名称
- 🎨 支持 PNG、HTML、SVG 三种输出格式，可通过`format`属性切换
- ⚙️ 提供丰富的配置选项：数据内容、模块大小、边距、CSS 单位、比例和纠错等级
- 🖌️ 支持通过`::part`伪元素自定义样式，可分别对 img、table、svg 元素进行样式覆盖
- 📜 项目采用 MIT 开源协议，拥有 525 个 Star 和 82 个 Fork，主要使用 JavaScript 开发
- 🚀 版本历史显示从 2013 年启动，经历了多次重大更新，包括支持 SVG、自定义元素名称和 ESM 发布

---

### [二维码](https://educastellano.github.io/qr-code/demo/)

**原文标题**: [<qr-code>](https://educastellano.github.io/qr-code/demo/)

本内容介绍了二维码生成中的格式、模块大小、边距、纠错等级及自定义样式等参数设置。
- 📐 支持 HTML、PNG、SVG 三种输出格式
- 🔲 模块大小可设为 0 以实现自适应缩放
- 📏 可调整二维码的边距（Margin）
- 🛡️ 提供四种纠错等级：低、中、四分位、高
- 🎨 支持自定义样式（Custom styles）

---

### [spartan - 驱动 Angular 全栈开发的尖端工具](https://spartan.ng/)

**原文标题**: [spartan - Cutting-edge tools powering Angular full-stack development](https://spartan.ng/)

本页面介绍了 spartan——一个基于 Angular、支持信号、SSR 和无区域模式的 UI 原语库，并展示了其组件示例、计费表单、团队协作、设置选项、贡献者社区及赞助信息。

- 🚀 核心特性：spartan 是专为 Angular 设计的无障碍 UI 原语库，支持信号、SSR 和无区域模式，可无限制定制样式。
- 💳 安全支付表单：提供信用卡支付界面，包含卡号、CVV、有效期及账单地址输入，所有交易加密。
- 👥 团队协作：支持邀请团队成员协作项目，当前无成员时可一键邀请。
- ⚙️ 系统设置：涵盖价格范围、计算环境（Kubernetes/虚拟机）、GPU 数量、外观设置（壁纸染色）及双因素认证。
- 📋 示例与组件：提供仪表盘、任务、认证、支付等组件示例，并支持评论、附件、归档等操作。
- 🌟 社区与贡献：由“The 300”社区构建，包含 146 位贡献者，项目 MIT 许可，永久免费，可赞助支持维护。
- 🔗 快速入门：用户可通过“Get Started”、“View Components”或 Star on GitHub 开始使用。

---

### [你的设计系统的基础 - shadcn/ui](https://ui.shadcn.com/)

**原文标题**: [The Foundation for your Design System - shadcn/ui](https://ui.shadcn.com/)

### 概述总结
该内容提供了一套可定制的聊天界面组件及金融仪表板设计系统，涵盖按钮、对话框、储蓄目标、分红收入、账户设置等核心功能模块。

- 🔘 **组件基础**：提供按钮（主要/次要/轮廓）、徽章、对话框、按钮组等可扩展的 UI 组件
- 📊 **金融仪表板**：显示储蓄目标（退休 65%/房地产 32%）、贡献历史、可领取余额（$1,211.29）及 Q2 股息收入
- ⚙️ **账户管理**：支持安全认证更新、支付限额调整、定期转账及循环卡支付管理
- 📈 **分析功能**：展示 418.2K 访问量（+10% 增长）、通知偏好设置（交易/安全/目标/市场提醒）
- 🔗 **设备连接**：支持扫描二维码关联移动设备，实现跨平台同步
- 💬 **聊天界面**：包含新对话启动、消息发送及 AI 流式回复的滚动行为优化提示
- ⚡ **能源监控**：显示家庭用电功率（当前 3.4kW）及太阳能发电量（+1.2kW）

---

### [发布 v1.6.0 · pionxzh/wakaru · GitHub](https://github.com/pionxzh/wakaru/releases/tag/v1.6.0)

**原文标题**: [Release v1.6.0 · pionxzh/wakaru · GitHub](https://github.com/pionxzh/wakaru/releases/tag/v1.6.0)

概述概要  
Wakaru v1.6.0 版本发布，主要提升反编译质量和可读性，新增源码映射、智能重命名等功能，并修复多项正确性问题。  

- 🗺️ 输出源码映射，支持将反编译代码映射回原始输入，并新增可视化映射视图  
- 🧠 SmartRename 智能重命名，恢复 React 和对象 getter 模式中的可读名称（含 React 19 useActionState）  
- 🔧 提升反编译质量，优化类表达式提升、Object.defineProperty getter 折叠、async/object-rest 辅助函数及 esbuild CJS 包装  
- ⏱️ CLI 诊断更友好，增加计时、格式检测、颜色输出、JSON 输出及崩溃时的预填问题链接  
- 🛡️ 正确性与安全性改进，扩展源码映射跨度传播至转换层级、类成员和 try/catch 块，捕获解析器与修复器崩溃  
- ✅ 无破坏性变更，现有 CLI 用法可继续正常工作

---

### [GitHub - Vanilagy/turbores: 极速 WASM 苹果 ProRes 视频解码器 · GitHub](https://github.com/Vanilagy/turbores)

**原文标题**: [GitHub - Vanilagy/turbores: An extremely fast WASM Apple ProRes video decoder · GitHub](https://github.com/Vanilagy/turbores)

TurboRes 是一个基于 Zig 和 TypeScript 构建的高性能 Apple ProRes 视频解码库，专为浏览器和 JavaScript 环境设计，无需硬件加速即可实现极速解码。

- ⚡ **极致性能**：支持单核与多核解码，4K 视频可达数百帧/秒，速度比原生 FFmpeg 快两倍以上。
- 🎬 **功能全面**：支持所有 ProRes 变体（422/444、LT、Proxy、4444），10/12 位色深，逐行/隔行扫描，最高 16K 分辨率。
- ✅ **精确可靠**：提供比特精确的解码结果，无近似处理，并完整验证输入数据，拒绝无效或恶意数据。
- 🌐 **跨平台兼容**：开箱即用于 Chromium、Firefox、Safari、Node、Deno、Bun 等环境。
- 🧩 **简单易用**：API 极简，与 WebCodecs API 和 Mediabunny 无缝集成。
- 📦 **体积小巧**：无运行时依赖，gzip 后仅约 50 kB。
- 🔧 **多线程支持**：提供共享内存多线程和 Worker 池两种模式，可显式控制并发数。
- 🎨 **零开销像素格式转换**：支持 I420、I422、I444 等格式，转换不增加额外性能成本。
- 📊 **性能卓越**：在 M4 MacBook Air 上，多线程解码 4K ProRes 422 HQ 达 228 FPS，远超 FFmpeg。
- 🛠️ **技术亮点**：采用 Zig 编写 WASM，使用 SIMD、分支无关熵解码、AAN IDCT 算法等优化技术。

---

### [Mediabunny — 一个完整的浏览器端 JavaScript 媒体工具包](https://mediabunny.dev/)

**原文标题**: [Mediabunny â A complete JavaScript media toolkit for the browser](https://mediabunny.dev/)

概述：Codec Registry 是一个用于管理和查找编解码器的注册表系统，支持多种导航功能，包括指南、API、LLMs、示例、博客、赞助商和许可证信息，并提供了代码注册表和外观设置选项。

- 🔍 提供搜索功能，方便用户快速查找内容
- 📚 包含主要导航菜单，如指南、API、LLMs、示例和博客
- 💰 设有赞助商和许可证信息模块
- 🗂️ 支持代码注册表管理
- 🎨 提供外观设置选项，可调整界面风格

---

### [GitHub - swimlane/ngx-charts: :bar_chart: 声明式图表框架 for Angular](https://github.com/swimlane/ngx-charts)

**原文标题**: [GitHub - swimlane/ngx-charts: :bar_chart: Declarative Charting Framework for Angular · GitHub](https://github.com/swimlane/ngx-charts)

这是一个基于 Angular 的声明式图表框架，使用 Angular 渲染 SVG 元素，结合 d3 的数学功能，提供美观且可定制的数据可视化解决方案。

- 📊 提供多种图表类型，包括柱状图、折线图、面积图、饼图、气泡图、环形图、仪表盘、热力图、树图和桑基图等
- 🎨 支持高度自定义，包括自动缩放、时间线过滤、线条插值、坐标轴标签和图例配置
- 🖱️ 具备高级交互功能，如实时数据支持、高级工具提示和数据点事件处理
- 💻 完全兼容 ngUpgrade，支持 Angular 的 AoT 和 SSR 等平台特性
- 🔧 可通过 CSS 完全自定义样式，并支持构建自定义图表
- 📦 通过 npm 安装：`npm i @swimlane/ngx-charts --save`
- 🏢 由 Swimlane 公司开源，用于网络安全自动化平台
- 📝 提供详细的文档和演示站点：swimlane.github.io/ngx-charts/
- ⭐ 在 GitHub 上获得 4.4k 星标和 1.2k 分支，拥有活跃的社区支持

---

### [NgxCharts](https://swimlane.github.io/ngx-charts/#/ngx-charts/bar-vertical)

**原文标题**: [NgxCharts](https://swimlane.github.io/ngx-charts/#/ngx-charts/bar-vertical)

这篇内容主要探讨了人工智能在医疗领域的应用现状与未来潜力，强调了其提升诊断效率、个性化治疗和优化医疗资源分配的作用，同时指出了数据隐私、算法偏见和监管挑战等关键问题。

- 🩺 提升诊断效率：AI 通过分析医学影像和病历数据，能快速识别疾病模式，辅助医生做出更准确的诊断。
- 🧬 个性化治疗：利用机器学习算法，AI 可根据患者基因和病史定制治疗方案，提高疗效并减少副作用。
- 📊 优化资源分配：AI 预测患者流量和疾病爆发趋势，帮助医院合理安排人力和物资，降低运营成本。
- 🔒 数据隐私风险：医疗数据敏感，AI 系统需严格保护患者隐私，防止数据泄露和滥用。
- ⚖️ 算法偏见问题：训练数据不均衡可能导致 AI 对特定人群诊断不准确，需加强数据多样性和公平性审查。
- 🚧 监管与伦理挑战：AI 医疗产品需通过严格审批，同时需建立透明问责机制，确保技术安全可靠。

---

### [发布 GopherJS 1.21.0 以支持 Go 1.21.13 · gopherjs/gopherjs · GitHub](https://github.com/gopherjs/gopherjs/releases/tag/v1.21.0)

**原文标题**: [Release GopherJS 1.21.0 for Go 1.21.13 · gopherjs/gopherjs · GitHub](https://github.com/gopherjs/gopherjs/releases/tag/v1.21.0)

GopherJS v1.21.0 发布，支持 Go 1.21.13，带来多项改进和修复。

- 🚀 上游 Go 支持升级至 go1.21.13
- 🔧 新增 `unsafe.Slice` 方法及索引指针改进，支持切片转换
- 🎯 改进了方法遮蔽和歧义解析，增强 nil 感知检查
- ⚡ 优化堆栈跟踪生成速度，尤其适用于 `t.Helpers()` 等场景
- 🗑️ 移除已弃用的 `node_syscall` 支持
- 🐛 修复了泛型最小化代码中的标识符冲突问题
- 🛠️ 更新了 `reflect`、`reflectlite`、`abi` 等核心包
- 📦 增加了 `max`、`min` 和 `clear` 内置方法
- 🔄 改进了 int64/uint64 索引和代理转换问题
- 🧪 测试时设置 `testing.Testing` 为 true
- 🧹 优化了调用帧生成和 math/bits 速度
- 🔒 版本由 grantnelson-wf 发布，并带有已验证的 GPG 签名

---

### [GitHub - jsdom/whatwg-url：JavaScript中WHATWG URL 标准的实现](https://github.com/jsdom/whatwg-url)

**原文标题**: [GitHub - jsdom/whatwg-url: An implementation of the WHATWG URL Standard in JavaScript · GitHub](https://github.com/jsdom/whatwg-url)

whatwg-url 是 WHATWG URL 标准的完整 JavaScript 实现，可独立使用或集成到 jsdom 等项目中，提供 URL 解析、序列化及底层算法支持。

- 📖 完全遵循 WHATWG URL 标准，支持最新的规范与平台测试
- 🔧 提供 URL 和 URLSearchParams 类，符合规范行为（如 USVString 转换）
- 🧩 导出底层 URL 标准 API，包括解析、序列化、主机/路径处理等函数
- ⚠️ URL 记录（URL record）包含 scheme、host、port 等属性，修改后需通过 basicURLParse 修复一致性
- ❌ 解析失败时返回 null，parseURLWithValidationErrors 额外返回验证错误数组
- 🛠️ 支持状态覆盖（stateOverride）参数，用于逐步构建 URL
- 📦 包含 webidl2js-wrapper 模块，提供基于 webidl2js 的接口包装器
- 🧪 开发需 Node.js，通过 npm install 安装依赖，npm test 运行测试
- 🌐 可构建并运行在线演示（live viewer），需执行 npm run prepare 和 npm run build-live-viewer
- 🤝 社区驱动项目，由志愿者维护，支持通过 Tidelift 订阅或直接贡献

---

### [实时 URL 查看器](https://jsdom.github.io/whatwg-url/)

**原文标题**: [Live URL Viewer](https://jsdom.github.io/whatwg-url/)

无法总结：未找到主要内容。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q2&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q2&utm_content=classified)

Meticulous 是一个自动化测试平台，通过记录开发者日常操作，利用 AI 生成全面且无干扰的端到端测试，大幅提升代码发布速度与可靠性。

- 🚀 **零开发工作量**：只需添加脚本标签，即可自动记录和生成测试，无需手动编写、修复或维护测试用例。
- 🧠 **AI 驱动测试套件**：AI 引擎持续追踪代码分支和用户交互，覆盖所有用户流程和边缘情况，测试随应用自动进化。
- 🔍 **确定性无干扰测试**：通过模拟后端响应（保存并重放原始记录），消除数据变化导致的误报，无需特殊测试账户或模拟数据。
- ⚡ **闪电般速度**：测试在计算集群上高度并行化，可快速测试数千个屏幕，结果在 120 秒内返回。
- 🏢 **企业级信任**：已被 Dropbox、Notion 等超过 100 家组织采用，开发者反馈“无法想象没有它的工作”。
- 🔧 **广泛集成**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流框架，可补充或替代现有测试套件。
- 🛡️ **从底层消除干扰**：基于 Chromium 构建的确定性调度引擎，从根源上消除测试不稳定因素，适用于最复杂的应用。

---

### [Trigger.dev | 构建和部署完全托管的人工智能代理与工作流。](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=june&utm_term=js-weekly&utm_content=homepage)

**原文标题**: [Trigger.dev | Build and deploy fully-managed AI agents and workflows.](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=june&utm_term=js-weekly&utm_content=homepage)

Trigger.dev 现已符合 HIPAA 标准，是一个用于构建和部署全托管 AI 代理与工作流的 TypeScript 平台。它支持长时间运行的任务、重试、队列、可观测性和弹性扩展，并与现有技术栈无缝集成。

- 🏥 符合 HIPAA 标准，确保医疗数据处理的安全性
- 🤖 支持构建生产级 AI 代理，具备工具调用、自动重试和全面可观测性
- ⏱️ 无超时限制，按实际执行时间付费，无需管理服务器
- 🔍 提供错误警报、高级过滤和版本控制，便于快速发现和修复问题
- 📡 支持实时状态更新和流式传输 LLM 响应到前端
- 🐍 自由定制构建过程，支持 Python、Prisma、Puppeteer、FFmpeg 等
- 🔄 内置重试机制，支持条件重试和细粒度控制
- 🌍 开源（Apache 2.0），拥有 15.5k+ GitHub 星标和活跃社区
- 💬 受到众多开发者好评，用于自动化邮件、AI 工作流、数据处理等场景
- 💰 简单定价，按使用付费，也支持自托管

---

### [2026 年 WebAssembly 运行时的性能表现 - Frank DENIS 的随想](https://00f.net/2026/06/23/webassembly-runtimes-2026/)

**原文标题**: [Performance of WebAssembly runtimes in 2026 - Frank DENIS random thoughts.](https://00f.net/2026/06/23/webassembly-runtimes-2026/)

2026 年 WebAssembly 运行时的性能表现显示，不同运行时在加密工作负载上的速度差异显著，且新指令支持是关键改进点。

- 📊 **整体趋势**：大部分运行时在 2024-2026 年间有性能提升，但幅度不一；Wasmtime 每年稳定提速，Bun 在 2025-2026 年实现大幅跃进。
- 🚀 **最佳性能**：Wasmer 在支持 wide_arithmetic 指令后表现最佳（1.33 倍原生速度），WAVM、WAMR 和 Wasmtime 紧随其后。
- 🔧 **关键特性**：wide_arithmetic 指令对加密代码至关重要，Wasmtime 和 Wasmer 因此获得最大加速（如 Wasmtime 从 2.41 倍降至 1.46 倍原生速度）。
- ⚖️ **运行时对比**：Wasmtime 逐年改善（2.67→2.54→2.41 倍原生），Node 缓慢提升（8.60→7.95 倍），Wazero 基本持平（约 4.7 倍），WAMR 稳定在 1.6 倍左右。
- 🐛 **兼容性问题**：部分运行时存在失败情况，如 Bun 旧版本在特定构建中崩溃，Node 需调整内存设置，WAMR 不支持 wide_arithmetic 指令。
- 📈 **测试方法**：基于 libsodium 基准测试，对比原生代码与多种 WebAssembly 构建（plain、lime1、simd128、wide_arithmetic），使用 2024-2026 年稳定版运行时。
- 💡 **实用建议**：WebAssembly 性能依赖运行时、版本、特性支持和部署模式；对加密工作负载，wide_arithmetic 值得关注，且应针对实际工作负载进行基准测试。

---

### [限制问题创建仅限协作者 - GitHub 更新日志](https://github.blog/changelog/2026-06-29-restrict-issue-creation-to-collaborators-only/)

**原文标题**: [Restrict issue creation to collaborators only - GitHub Changelog](https://github.blog/changelog/2026-06-29-restrict-issue-creation-to-collaborators-only/)

概述总结  
仓库管理员现在可以限制只有具有写入权限的协作者才能创建议题，从而减少不必要的议题创建，同时保持议题工作流程对活跃维护者和贡献者可用。此设置适用于议题、评论、讨论、项目和 Copilot 等入口点，并与拉取请求权限保持一致。  

- 🔒 新增功能：仓库管理员可限制议题创建仅限写入权限的协作者  
- 🚫 无写入权限的用户无法从议题、评论、讨论、项目或 Copilot 创建议题  
- 🔄 与拉取请求权限保持一致，增强一致性  
- ⚙️ 设置步骤：仓库设置 → 功能 → 议题 → 选择“仅限协作者创建”  
- 💬 如有问题或反馈，可加入社区讨论

---

### [Flow: JavaScript 的类型化方言 — JS 静态类型检查器 | Flow](https://flow.org/)

**原文标题**: [Flow: A Typed Dialect of JavaScript — JS Static Type Checker | Flow](https://flow.org/)

Flow 是一种类型化的 JavaScript 方言，现在与 TypeScript 语法相似，但更安全，并内置了 React 组件、renders 和 match 等特性。

- 🧩 **熟悉语法**：Flow 支持 keyof、readonly、unknown、索引访问类型 T[K]、extends 泛型约束、条件类型、映射类型和类型守卫，与 TypeScript 高度兼容。
- ⚛️ **React 一等支持**：内置 component 和 renders 语法，Props 作为命名参数并支持默认值，通过 renders 实现设计系统组合规则的类型检查。
- 🔍 **模式匹配 match**：match 作为表达式和语句，提供穷举检查、结构模式解构，缺失 case 时会明确提示。
- 🎯 **默认精确对象**：对象类型默认精确，能捕获多余属性（如 `sample: "free"`），防止运行时崩溃。
- 🛡️ **默认安全**：阻止不安全的方法提取（如 `counter.incr`），避免因 `this` 丢失导致的运行时错误。

---

### [Flow 已移植到 Rust](https://medium.com/flow-type/flows-ocaml-to-rust-port-78b95bcf49e9)

**原文标题**: [Flow has been ported to Rust | Flow](https://medium.com/flow-type/flows-ocaml-to-rust-port-78b95bcf49e9)

概述总结
Flow 的 OCaml 代码库已完全移植到 Rust，新版本速度提升 2 倍，并在 AI 辅助下完成了从解析器到类型检查器的全面移植。

- 🚀 **性能飞跃**：Rust 版 Flow 比 OCaml 版快 2 倍，检查阶段提速 30%-100%
- 🤖 **AI 主导移植**：使用 AI 代理团队完成解析器（4 周）和类型检查器（1 个月）的逐行移植
- 🔄 **保守策略**：坚持逐行移植而非重写，确保行为一致性和平稳过渡
- 🛠️ **性能优化**：AI 自动识别并修复大 O 问题、内存泄漏，累计实现 1%-2% 的微优化
- 🧩 **语言选择**：选择 Rust 而非 Go/Kotlin，以整合 SWC、oxlint 等 Rust 工具链
- 📋 **严格审查**：强制 AI 遵守无 unsafe 规则，保留原始 OCaml 注释便于人工审核
- ⏱️ **无代码冻结**：通过 AI 代理持续同步 OCaml 和 Rust 代码库，团队正常推进功能开发

---

### [介绍 | pnpm](https://pnpm.io/pnpr/)

**原文标题**: [Introduction | pnpm](https://pnpm.io/pnpr/)

概述：pnpr 是一个用 Rust 编写的、兼容 pnpm 的 npm 注册表服务器，提供私有包托管、缓存代理和安装加速功能，目前处于实验阶段，采用 PolyForm Shield 许可证。

- 🚀 **私有注册表**：托管组织内部私有包，支持按包设置访问和发布规则。
- 🔄 **缓存代理**：镜像上游注册表（如 npmjs.org），加速安装并应对上游故障。
- ⚡ **安装加速器**：在服务端解析依赖图，为 pnpm 提供现成的锁文件，提升安装效率。
- 🔗 **与 pnpm 的关系**：pnpr 是独立服务器，与 pnpm CLI 配合使用，可加速依赖解析。
- 📜 **许可证**：采用 PolyForm Shield 1.0.0，允许运行和自托管，但禁止用于竞争性产品。

---

### [Git 2.55 亮点 - GitHub 博客](https://github.blog/open-source/git/highlights-from-git-2-55/)

**原文标题**: [Highlights from Git 2.55 - The GitHub Blog](https://github.blog/open-source/git/highlights-from-git-2-55/)

Git 2.55 发布了多项新功能和改进，包括增量多包索引、修复提交命令、并行钩子、Linux 文件系统监视器、位图生成优化等。

- 📦 **增量多包索引**：`git repack` 现支持增量 MIDX 链，结合几何重组，减少维护时元数据重写，提升大型仓库效率。
- 🔧 **修复早期提交**：新增 `git history fixup` 命令，可将暂存更改直接合并到历史中的指定提交，并重放后续提交。
- ⚡ **并行钩子**：配置钩子现可并行运行，通过 `hook.jobs` 等选项控制并发数，提升性能。
- 🐧 **Linux 文件系统监视器**：`core.fsmonitor` 现支持 Linux，使用 inotify 加速 `git status` 等命令。
- 🚀 **位图生成优化**：通过避免树递归、重用位图等，生成时间从 612 秒降至 294 秒，伪合并位图也得到改进。
- 📉 **路径遍历打包**：`git pack-objects --path-walk` 现可与多种过滤器结合，生成更小包文件（如 16% 更小）。
- 📝 **格式化修订命令**：实验性 `git format-rev` 可从标准输入格式化提交，避免多次启动 Git 进程。
- 🔒 **侧带输出安全**：默认屏蔽终端控制序列，仅允许 ANSI 颜色，防止服务器注入恶意输出。
- 🛡️ **安全切换分支**：`git checkout -m` 使用自动暂存，冲突更改保存为 stash，避免丢失工作。
- 🌐 **远程组推送**：`git push` 现支持远程组，可一次推送到多个远程仓库。
- 📊 **图形限制**：`git log --graph` 新增 `--graph-lane-limit`，限制图列数，提升可读性。
- ⏳ **最旧提交选项**：`git rev-list` 和 `git log` 新增 `--max-count-oldest`，直接获取最旧 N 个提交。
- 🤝 **协商控制**：新增引用包含/限制选项，优化 fetch 协商，减少不必要对象传输。

---

### [PostgreSQL：PostgreSQL 19 Beta 1 发布！](https://www.postgresql.org/about/news/postgresql-19-beta-1-released-3313/)

**原文标题**: [PostgreSQL: PostgreSQL 19 Beta 1 Released!](https://www.postgresql.org/about/news/postgresql-19-beta-1-released-3313/)

PostgreSQL 19 Beta 1 已发布，带来了性能提升、开发者体验改进、安全增强、监控优化及逻辑复制等多项新功能。

- 🚀 **性能提升**：异步 I/O 自动扩展工作线程、引入`pg_plan_advice`扩展优化查询计划、自动清理支持并行、新增`REPACK`命令减少表重建开销，外键检查时插入性能提升 2 倍。
- 🧑‍💻 **开发者体验**：支持 SQL/PGQ 属性图查询、`FOR PORTION OF`子句支持 UPDATE/DELETE、新增`ALTER TABLE ... MERGE/SPLIT PARTITIONS`、`GROUP BY ALL`语法、`jsonpath`字符串处理函数扩展、`WAIT FOR LSN`实现副本读写一致性。
- 🔒 **安全增强**：支持服务器名称指示（SNI）实现多 TLS 证书、密码过期警告（默认 7 天）、弃用 md5 认证并发出警告。
- 📊 **监控与可观测性**：新增`pg_stat_lock`和`pg_stat_recovery`视图、统计视图增加`stats_reset`列、清理和分析进度视图增加`started_by`列、`EXPLAIN ANALYZE`支持异步 I/O 统计。
- 🔄 **逻辑复制与联邦查询**：复制序列值、`CREATE PUBLICATION ... EXCEPT`排除特定表、无需重启启用逻辑复制、`postgres_fdw`推送数组操作并利用远程统计信息。
- 🛠️ **其他亮点**：数据校验和可在线启用/禁用、JIT 编译默认禁用、默认压缩算法改为 LZ4、移除 RADIUS 认证、`vacuumdb --analyze-only`默认分析分区表。

---

### [Postgres 19 新特性：Beta 版深度解析](https://www.snowflake.com/en/blog/engineering/postgresql-19-features-beta/)

**原文标题**: [What's New in Postgres 19: Beta Release Deep Dive](https://www.snowflake.com/en/blog/engineering/postgresql-19-features-beta/)

Postgres 19 版本带来了广泛而实用的改进，涵盖性能、运维和开发者体验，使其成为一个全面升级的重要版本。

- 🏗️ **内置 REPACK CONCURRENTLY**：无需第三方扩展即可在线重建表，解决生产环境中的表膨胀和锁问题。
- 📂 **分区拆分与合并**：允许动态调整分区策略，适应数据量变化，无需重建整个表。
- 🔄 **逻辑复制更成熟**：同步序列值、支持 `EXCEPT` 子句排除表、自动启用逻辑复制，减少配置陷阱。
- 🧹 **自动清理更智能**：引入并行清理、优先级评分系统和新监控视图，提升维护效率与可观测性。
- 📊 **SQL 属性图查询**：支持图数据模型，无需额外数据库即可处理关系型数据中的图分析。
- 📋 **COPY 功能增强**：支持跳过多行头部、错误时设为 NULL、输出 JSON 格式，简化数据导入导出。
- 💻 **SQL 语法优化**：新增 `GROUP BY ALL`、窗口函数 `IGNORE NULLS`、`INSERT ... ON CONFLICT DO SELECT` 等，提升开发效率。
- ⚡ **性能全面改进**：优化查询计划器、排序、外键检查、SIMD 指令支持，升级即可获得性能提升。

---

