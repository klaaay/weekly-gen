### [](https://engineeringblog.yelp.com/2026/08/migrating-a-large-flow-monorepo-to-typescript.html)

**原文标题**: [Migrating a Large Flow Monorepo to TypeScript](https://engineeringblog.yelp.com/2026/08/migrating-a-large-flow-monorepo-to-typescript.html)

将大型 Flow Monorepo 迁移至 TypeScript 的完整过程：Yelp 从 2022 年开始规划，历时近四年，将超过 140 万行代码从 Flow 迁移至 TypeScript，通过逐包转换、自定义工具链、广泛文档化与社区协作，最终实现更高类型覆盖率与开发者生产力提升。

- 🎯 背景与动机：Flow 曾是 Yelp 的首选类型检查器，但随着 TypeScript 生态壮大、稳定性提升，以及 Flow 团队转向内部需求，TypeScript 成为更优选择。
- 🚫 核心原则：避免暂时禁用类型检查或批量插入忽略注释，确保迁移全程保持类型完整性，因为失去类型检查的代码几乎不会恢复覆盖。
- ⚙️ 迁移策略：采用逐包转换方式，使用 flowts 和自有 codemod 进行自动化转换，辅以手动修复，并通过 flowgen 生成 Flow 兼容的类型声明。
- 📦 Monorepo 基础：先前的 Lerna monorepo 迁移使工具更新和包间互操作成为可能，只需一次 PR 即可全生态支持 TypeScript，并按包粒度处理转换。
- 🔧 工具打磨与内部测试：Webcore 与 Design Systems 团队先行转换约 90 个基础包，并投入数月修复工具链、编写文档和 metatest 套件，确保工具可靠易用。
- 📣 正式发布与社区推进：2023 年 5 月向全公司推出，提供演示、Q&A、自动 Jira 工单跟踪及依赖图分析，帮助团队理解优先级。
- 📈 迁移进度与挑战：从启动时约 100 个包逐步增长，后期通过依赖图可视化识别瓶颈，制定季度计划，并手动转换关键包以加速收尾。
- 🤖 探索与放弃的方案：尝试自动化 cronjob 全流程转换与 LLM 修复早期失败，但工具能力不足，最终未纳入核心工具链，仅作为团队可选辅助。
- 🏁 最终成果：2026 年 2 月迁移完成，共转换 140 万行源码，整体类型覆盖率从 Flow 的 83.15% 提升至 TypeScript 的 96.44%，仅有约 6000 条@ts-expect-error 指令。
- 💡 积极反馈与附加收益：82% 的受访工程师报告生产力提升，45% 认为显著提升；同时得以采用 swc、@typescript-eslint 等仅支持 TypeScript 的工具，且 LLM 对 TS 代码处理更佳。
- 📚 经验教训：大规模外联与文档是关键，设置明确截止日期比让团队自主推进更有效，适时介入高杠杆包迁移能起到“倍增器”作用。

---

### [](https://flow.org/)

**原文标题**: [Flow: A Typed Dialect of JavaScript — JS Static Type Checker | Flow](https://flow.org/)

概述总结
- 🔷 Flow 是 JavaScript 的类型化方言，语法与 TypeScript 高度相似，但提供更强的安全保证。
- 🧩 熟悉语法：支持 `keyof`、`readonly`、`unknown`、索引访问类型等，与 TypeScript 兼容的泛型和类型操作。
- ⚛️ React 一等公民：内置 `component` 与 `renders` 语法，组件 props 直接内联命名，并能在类型层面约束组件渲染关系。
- 🔀 模式匹配 `match`：同时作为表达式和语句，无 fall-through，穷尽性检查可自动指出缺失的匹配模式。
- 📦 默认精确对象：对象类型默认精确，能捕获通过变量传递的额外属性，避免潜在的运行时崩溃。
- 🛡️ 安全默认：阻止不安全的类方法提取，在编译期识别 `this` 丢失问题，避免运行时异常。
- 🚀 已在 Meta 生产环境中应用于数百万个 JavaScript 与 React 文件。

---

### [](https://dashboard.render.com/register?utm_source=email&utm_medium=newsletter&utm_campaign=2026_newsletter_cooperpress&utm_content=js_weekly)

**原文标题**: [Render · The Easiest Cloud For All Your Apps](https://dashboard.render.com/register?utm_source=email&utm_medium=newsletter&utm_campaign=2026_newsletter_cooperpress&utm_content=js_weekly)

这是一个网页应用的提示信息，要求用户启用 JavaScript 才能正常使用。

- ⚙️ 请启用 JavaScript 以运行此应用。

---

### [](https://blog.cloudflare.com/kitesurf/)

**原文标题**: [Introducing Kitesurf: The agent-first browser that runs in V8 isolates on Cloudflare Workers | Cloudflare Blog](https://blog.cloudflare.com/kitesurf/)

overview summary：Cloudflare 正式发布 Kitesurf，一个为 AI 代理设计的、运行在 Workers V8 隔离环境中的全新浏览器。它针对 AI 场景大幅优化了 CPU 与内存效率，并通过 CDP 协议兼容现有自动化工具，目前已在 Browser Run 中开放免费测试。

- 🚀 Kitesurf 是 Cloudflare 专为 AI 代理构建的浏览器，完全运行在 Workers 上，可在 Browser Run 中免费试用（beta 版）。
- ⚡ 相比 Chromium，Kitesurf 在常见代理任务中 CPU 消耗降低 3.1-3.8 倍，内存消耗降低 4.7-7 倍，但墙钟时间慢约 1.7 倍。
- 🧩 核心设计原则：以测试驱动开发，使用 Rust 编译到 WebAssembly，强调异常安全、严格隔离与尽可能无状态。
- 🏗️ 三大组件：Engine（处理 CDP API 与会话状态）、PageScript（用 Dynamic Workers 解析 DOM 并运行脚本）、PageRenderer（负责光栅化生成图片/PDF）。
- 🎯 通过 215,000+ 项 Web Platform Tests，并针对真实网站进行集成与视觉回归测试。
- 🖥️ 支持现有 CDP 客户端（Puppeteer、Playwright、chrome-remote-interface 等），只需添加 `browser=kitesurf` 参数即可使用。
- ✅ 适合 AI 代理的页面渲染、HTML 提取、截图/PDF 等一次性 Quick Actions 场景。
- ❌ 暂不支持视频、WebGL、复杂持久化会话或真实 TLS 指纹的 bot 挑战交互。
- 🔮 未来规划：完善 CDP 覆盖、提升截图/PDF 保真度、增加 WPT 通过率，并计划开源 Kitesurf 供用户自部署。

---

### [](https://kitesurf.cloudflare.app/)

**原文标题**: [Kitesurf - stateless browser running entirely on Workers](https://kitesurf.cloudflare.app/)

Kitesurf 是 Cloudflare 推出的新型无状态、高可扩展且成本低廉的 Web 浏览器，完全运行在 Workers 之上，专为 Agentic Cloud 设计。它提供在线 Playground 供用户体验，并支持通过 Chrome DevTools 协议让 AI 代理直接驱动浏览器，无需本地安装或 API 令牌。

- 🧭 Kitesurf 是 Cloudflare 推出的浏览器，专为 Agentic Cloud 打造，完全基于 Workers，无状态且极具成本效益。
- 🎮 提供交互式 Playground，内置 Chrome DevTools，可实时检查 DOM 元素、控制台消息与网络活动。
- 🧠 Memory 面板展示每个 isolate 的 WebAssembly 内存占用（含 frame），便于理解页面资源消耗。
- ⏱️ Playground 限制：每次页面导航最多分配 20 秒 CPU 时间和 60 秒墙钟时间，超时后页面会被停止并在 DevTools 中说明原因。
- 🔍 支持输入任意 HTTPS URL，并可生成截图（📷）、PDF（🖨）或 HTML（📄）输出。
- 📚 内置多个演示站点（如 Hacker News、Cloudflare Docs、MDN、Wikipedia、甚至 Doom 游戏）供快速尝试。
- 🤖 Kitesurf 使用 Chrome DevTools Protocol，任何能驱动 Chrome 的代理都能直接驱动它，无需安装 Chrome 或 API 令牌。
- 🔌 可通过 chrome-devtools-mcp 对接多种 MCP 客户端，包括 opencode、Claude Code、Cursor 等，并提供现成的 JSON 配置示例。

---

### [pnpm 12 有什么不同 | pnpm](https://pnpm.io/blog/whats-different-in-pnpm-12)

**原文标题**: [What's different in pnpm 12 | pnpm](https://pnpm.io/blog/whats-different-in-pnpm-12)

pnpm 12 是以 Rust 重写的版本，目前为发布候选版。它基本保持与 pnpm 11 兼容，但有三项关键差异：项目感知的全局 bin、Git 依赖解析方式变化，以及移除 `--resolution-only` 标志。

- 🔄 pnpm 12 是 Rust 重写版，命令、标志、设置和 lockfile 格式均与 pnpm 11 兼容，文档对两个版本通用。
- 📦 全局安装的 node、deno、bun 现在会优先使用当前项目固定的版本（通过 `devEngines.runtime` 或作为依赖安装），不再需要单独的版本管理器；由 `globalShims` 设置控制。
- 🔗 GitHub、GitLab、Bitbucket 上的依赖说明符现在视为身份标识，统一通过规范的 HTTPS URL 解析，不再记录 SSH URL。
- 📝 旧版 pnpm 生成的 lockfile 中若包含 SSH 形式条目，需用 `pnpm update <package>` 手动重新解析，pnpm 不会自动改写。
- 🔑 访问私有仓库的 SSH 配置应通过 Git 的 `insteadOf` 重写实现，pnpm 会调用 git 自动应用该配置。
- ❌ `pnpm install --resolution-only` 已被移除，相关功能改用 `pnpm peers check` 直接从 lockfile 读取 peer 依赖问题。
- 🧪 pnpm 12 以 `next-12` 标签发布为 RC，可通过 npm 或 GitHub 预发布安装；Homebrew、winget、Scoop、Chocolatey 尚未提供。
- 🐛 使用过程中遇到问题，请向官方报告。

---

### [](https://x.com/bunjavascript/status/2085921831819858431)

**原文标题**: [Bun on X: "In the next version of Bun

`Bun.XML.parse` is a SIMD-accelerated XML parser builtin to Bun https://t.co/Ls8oFLdUsc" / X](https://x.com/bunjavascript/status/2085921831819858431)

概述：Bun 宣布将在下一版本中推出内置的 SIMD 加速 XML 解析器 `Bun.XML.parse`，引发社区讨论，有人期待更多内置功能，也有人质疑版本延期与性能表现。

- ⚡️ Bun 即将内置 `Bun.XML.parse`，采用 SIMD 加速技术，显著提升 XML 解析速度。
- 🗜️ 该解析器作为 Bun 的原生内置功能，无需额外依赖，开箱即用。
- 🧩 有用户调侃“现在只等 Bun.FTP 合并就完美了”，表达对更多内置模块的期待。
- ⏳ 部分用户质疑：为了一个 XML 解析器而推迟 1.4 版本是否值得。
- 📡 有人关心 SIMD XML 解析在面对大型 RSS 订阅源时的表现，建议进行相关基准测试。

---

### [](https://www.anthropic.com/research/riemann-zeta)

**原文标题**: [Learning more about Claude's mathematical capabilities \ Anthropic](https://www.anthropic.com/research/riemann-zeta)

overview summary
Anthropic 的一篇博文介紹了未發布版本的 Claude 在嘗試解決黎曼猜想時，意外將黎曼 zeta 函數零點位於臨界線上的比例下界從 41.6% 提升至 67.2%。Claude 結合多位數學家既有研究成果，並透過大規模並行子代理運算與驗證，最終產出論文、非正式專家說明及形式化證明。文章強調此結果雖未解開黎曼猜想，卻展現 AI 數學能力的快速進展。

- 🔢 挑戰與意外：Claude 受邀「認真嘗試」黎曼猜想，雖未成功，卻意外改進了相關的下界常數，將零點在線比例從 41.6% 提升至 67.2%。
- 📜 核心貢獻：模型結合 Baluyot、Goldston、Suriajaya、Turnage-Butterbaugh 等人的系列研究及 Bombieri 2000 年的論文，運用包含正負定子空間的二次型與秩不等式，突破了先前極限。
- 🧩 技術方法：Claude 構造合適的函數空間及 Weil 誘導的二次型，同時考慮正負定性並允許非對角形式，從而利用第一、二階矩資訊得出結論。
- 🤖 運算規模：整個過程在 Claude Code 中分兩次會話完成，使用 3100 萬個輸出 token，協調約 60 個子代理，執行 2400 條 shell 指令並撰寫數百個 Python 腳本進行數值驗證。
- ✅ 驗證流程：子代理間相互審查證明、搜尋反例、下載 54 篇 arXiv 論文確認原創性，並獨立重證；Anthropic 的兩位數學家 Levent Alpöge 與 Ralph Furman 檢查成果，同時完成 Lean 形式化證明。
- 💡 啟發意義：此結果為數學家想法的延伸提供新途徑，也顯示 AI 模型可能低估自身進步速度——Claude 起初對結果持懷疑態度，但在鼓勵提示下成功突破。
- 📄 延伸讀物：部落格附上 Claude 的論文、形式化證明、Anthropic 的非正式筆記、Claude 的推導過程說明及詳細對話紀錄，供專家查閱。

---

### [Ill Bloom：活跃利用期间的钱包生成漏洞调查](https://www.coinspect.com/blog/ill-bloom-investigation/)

**原文标题**: [Ill Bloom: Investigating a Wallet Generation Vulnerability During Active Exploitation](https://www.coinspect.com/blog/ill-bloom-investigation/)

Coinspect 针对一场影响多网络的钱包盗币事件展开了调查，最终发现了一个隐藏在钱包生成流程中超过十年的随机性漏洞。该漏洞在调查期间仍被攻击者积极利用。文章介绍了从根因分析、受影响应用识别、受害者保护到分阶段披露的完整过程。

- 🔍 调查始于 2026 年 5 月的一起钱包耗尽事件，最终追溯到 CryptoJS 库中的随机数生成漏洞，该漏洞已存在十二年之久。
- ⚠️ 该漏洞并非新零日，早已被公开讨论并被攻击者用于盗取资金，且调查期间仍有利用活动。
- 🔬 为评估影响范围，研究人员生成候选恢复短语并推导地址，再与链上交易数据比对，从而识别出真实暴露的账户。
- 📱 结合链上分析、公开源码研究、依赖追踪和逆向工程，确认了多个受影响钱包应用，包括已修复和已停止维护的项目。
- 🛡️ 暴露地址无法直接关联用户身份，保护受害者的主要难点是建立通知渠道，为此 Coinspect 发布了公开地址检查器供用户自查。
- 📢 披露决策经过谨慎权衡：虽然技术细节可能被滥用，但漏洞已遭利用，且 CryptoJS 已不再维护，披露有助于下游项目识别依赖风险并迁移资金。
- 🌐 完整技术披露、调查方法论和后续更新均可在 illbloom.org 上查阅。

---

### [](https://github.com/denoland/deno/releases/tag/v2.9.5)

**原文标题**: [Release v2.9.5 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.9.5)

overview summary
- 🚀 Deno v2.9.5 于 2026.08.06 发布，聚焦新功能、稳定性修复与性能提升，覆盖 CLI、Node 兼容性、网络、加密及运行时核心。
- ✨ 新增功能：`deno add --unscoped` 按非作用域名添加包、`deno task --members` 仅运行工作区成员任务、`Blob`/`Body` 新增 `textStream()`、实验性 QuickJS 后端。
- 🔧 主要修复：bundle 避免 esbuild 协议死锁并尊重文件权限、CLI 转义外部元数据控制字符、内部模块导入不再受用户导入映射影响。
- 🔐 安全与加密：新增 `raw-secret` 至 `KeyFormat`、支持 `deriveBits` 长度 0、校验 inspector 请求头、WebSocket 升级路径禁用 HTTP/2 server push。
- 📦 Node 兼容性改进：修复 Web Streams、http2 回调、`fs.readdir` 排序、实现 `util.diff`、`v8.promiseHooks`、`node:test` 标签及 fs `flush` 选项。
- 🌐 网络与 DNS：释放 QUIC 流资源、清理负载均衡监听器、处理畸形 DNS 记录、`node:dns.getServers()` 增加 `--allow-sys` 权限要求。
- ⚡ 性能优化：启动函数顺序调整、减少启动时模块求值、移除 Linux 展开表、异步 `readFile`/`writeFile` 在阻塞池打开文件、base64url 编解码改用 simdutf。
- 🧪 其他修复：FFI 拒绝非阻塞调用中的可调整缓冲区、npm 忽略无效包 bin 目标、`outdated` 不将 JSR 预发布版报告为最新版。

---

### [](https://github.com/denoland/deno/pull/36194)

**原文标题**: [feat: add experimental QuickJS backend by nathanwhit · Pull Request #36194 · denoland/deno · GitHub](https://github.com/denoland/deno/pull/36194)

Deno 合并了 PR #36194，引入实验性 QuickJS 后端，通过新增的 `deno_v8` 门面 crate 让用户可在 V8 与 QuickJS 引擎间切换，并支持 `deno compile`/`deno desktop` 使用 `--engine` 参数选择运行时。

- 🚀 新增 `deno_v8` 门面 crate，可重新导出上游 `rusty_v8` 或 `v8x`，作为 V8 与 QuickJS 的统一抽象层。
- ⚙️ 保持 V8 为默认后端，通过 `deno_core`、`deno`、`denort` 等 crate 暴露互斥的 `v8` 与 `quickjs` Cargo features。
- 🏷️ 为 `deno compile` / `deno desktop` 添加 `--engine v8|quickjs` 标志，用于选择生成二进制所使用的 JavaScript 引擎。
- 📦 发布 QuickJS 版本的 `denort` / `libdenort` 工件（如 `denort-quickjs-<target>.zip`），供 `--engine quickjs` 解析下载。
- 🔗 `v8x` 依赖被固定为精确 RC 版本（`v8x = "=149.4.0-rc.1"`），其跟踪的 V8 线路（149）与默认 `v8` crate（150）不同，需独立升级。
- 🧹 移除了原本混入的无关修复（如 `#[op2(reentrant)]` 改动、uv 定时器修复等），使 PR 聚焦于 QuickJS 后端本身。
- 🛠️ 提供构建与验证命令：默认 `cargo build --bin deno`；QuickJS 构建使用 `--no-default-features --features quickjs`。
- ❗ 已知限制：QuickJS 因体积约束未实现 `Intl`，已记录为文档化的限制，用户反馈 `Intl.DateTimeFormat` 行为异常。
- 🐛 有用户报告 QuickJS 下运行 Vite/Fresh 构建时出现运行时错误，以及 `--version` 仍显示 V8 信息的问题。
- 👀 代码审查提出多项问题：缺少 `--engine` 端到端测试、`deno_core` 默认 features 导致下游编译失败、二进制名称逻辑重复、uv 定时器潜在忙循环、macOS SDK 路径硬编码等。
- 🔒 安全提醒：引入第二引擎意味着新增攻击面，且 `v8x` 基于较旧 V8 线路的 RC 版本，安全更新保证与 V8 不同，需在文档中明确。
- ✅ 审查后修复了主要问题，补充了 `--engine` 帮助文本中关于 QuickJS 实验性与安全性的说明，最终通过 136 项检查并合并。

---

### [](https://nodejs.org/en/blog/release/v26.7.0)

**原文标题**: [Node.js — Node.js 26.7.0 (Current)](https://nodejs.org/en/blog/release/v26.7.0)

Node.js 26.7.0 当前版本发布，带来多项新特性、依赖升级与修复，涵盖加密、模块、测试运行器、性能优化及平台支持等方面。
- 🔐 crypto：支持通过 STORE 加载器载入私钥，并更新根证书至 NSS 3.125
- 📦 lib 与 src：新增 perfetto 性能追踪支持，并实现 perfetto trace agent
- 🧩 module：ModuleHooks 中实现 Symbol.dispose，提升资源管理能力
- 🧪 test_runner：新增 --test-coverage-include-all 选项，便于全量覆盖统计
- ⬆️ 大量依赖升级：npm 至 11.19.0、ngtcp2、nghttp3、simdjson、acorn、sqlite、V8 等
- 🛠️ 修复多项问题：包括 crypto Argon2 FIPS 绕过、HTTP/2 性能回退、FFI 崩溃、sqlite 释放后使用、流处理异常等
- 🌐 网络与文件系统：支持 Windows 下 TCP 句柄传输、AF_UNIX 路径的 BoundSocket，并优化流处理分配
- 📚 文档与工具改进：修复多处文档问题、稳定 --disable-warning、更新技术优先级与安全维护人员信息
- 🔢 提供各平台安装包与二进制下载，并附有 PGP 签名校验和

---

### [](https://github.com/solidjs/solid-start/discussions/2281)

**原文标题**: [SolidStart v2 is now Stable · solidjs/solid-start · Discussion #2281 · GitHub](https://github.com/solidjs/solid-start/discussions/2281)

SolidStart v2 已正式稳定发布。该版本从 Vinxi 迁移到 Vite 的 Environment API，简化了架构并更好地融入 Vite 生态，为 Solid v1 应用提供了面向未来的现代化基础，同时兼容 Vite 8/9，并增强了部署集成能力。升级指南和迁移说明已就绪。

- 🚀 SolidStart v2 正式稳定，为使用 Solid v1 构建全栈应用提供现代化基础
- ⚙️ 弃用 Vinxi，直接基于 Vite Environment API 构建，架构更简洁，贴近 Vite 生态
- 🧩 原生支持 Vite 8 的 Rolldown 工具链，并兼容 Tailwind CSS v4 等 Vite 插件
- 🌐 直接集成 Nitro v3、Cloudflare、Netlify 等部署 Vite 插件，部署更便捷
- 🔄 已预先适配 Vite 9 的破坏性变更，预计发布首日即可兼容
- 📝 从 v1 升级：将配置从 app.config.ts 迁移到 vite.config.ts，需 Node.js 24+ 和 Vite 8，其他变更见完整迁移指南
- 🏛️ 回顾 v1 推动的两大方向：多 Vite 环境（现由 Vite Environment API 原生支持）和共享部署基础设施（经 Nitro 实现）
- 🔮 Solid v2 未来将面向 Solid v2 演进，但当前版本是生产环境就绪的稳定选择，适合新老项目
- 🙌 感谢 20 余位贡献者的代码、测试、反馈与文档支持

---

### [未找到标题](https://www.solidjs.com/)

**原文标题**: [No title found](https://www.solidjs.com/)

您没有提供需要总结的文本内容。请发送文章或文本，我将按照要求格式（overview summary + 带表情符号的要点）用中文为您总结。

---

### [](https://github.com/preactjs/preact/releases/tag/11.0.0-rc.0)

**原文标题**: [Release 11.0.0-rc.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.0.0-rc.0)

overview summary  
Preact 发布了 11.0.0-rc.0 预发布版本，带来多项新功能、正确性修复、性能优化与维护改进，并更新了贡献者信息。  

- ✨ 新增 compat 中的 `use` 与 `useEffectEvent` 支持，增强 API 对齐。  
- 📡 `useSyncExternalStore` 支持 `getServerSnapshot`，改善服务端渲染场景。  
- 🌀 核心支持 `createPortal`，便于在 DOM 任意位置渲染内容。  
- 🔀 优先使用 `moveBefore` 替代 `insertBefore`，提升节点移动效率。  
- 🛡️ 避免修改用户提供的 style 对象，修复附加 `px` 时的副作用。  
- 🧩 修复模板元素内容复用、脏子节点严格相等跳过等问题。  
- ⚡ 通过最长递增子序列算法计算最小子节点移动，优化渲染性能。  
- 🔄 `flushSync` 支持批量更新，减少不必要的渲染次数。  
- 📦 多处减小核心包体积，提升加载性能。  
- 🔧 维护方面：升级 React 版本声明至 19.0.0、清理依赖、优化构建配置。  
- 👥 感谢多位贡献者，包括 Mesoptier、ssssota 等共同推动此版本。

---

### [](https://astro.build/blog/astro-720/)

**原文标题**: [Astro 7.2 | Astro](https://astro.build/blog/astro-720/)

overview summary
- 🚀 Astro 7.2 发布，核心亮点是实验性增量静态构建，同时新增会话支持退出、`astro preview` 后台模式及相对路径 logger 等改进。
- ⚡ 实验性增量静态构建：通过 `experimental.incrementalBuild` 开启，配合 `getStaticPaths()` 返回 `cacheKey`（如内容集合的 digest），可跳过未变更页面的重新生成；模块图哈希变化时仍会全量重渲染。
- 🔒 退出会话支持：配置 `session: false` 可移除会话运行时，Cloudflare、Netlify、Node 适配器不再绑定默认驱动；未配置驱动时也会自动 tree-shake。
- 🖥️ `astro preview` 后台模式：使用 `astro preview --background` 启动，支持 `status`、`logs`、`stop` 子命令，与 `astro dev` 后台机制一致。
- 📂 相对路径 logger：`logger.entrypoint` 可直接写相对字符串（如 `'./src/custom-logger.js'`），不再强制使用 URL 形式。
- 🛠️ 其他改进：包含多项 bug 修复和小优化，完整变更见 changelog；官方团队成员及社区贡献者列表已列出。
- 👕 相关链接：推出新周边商品，并附上 Astro 7.1 与 7.0 的回顾文章入口。

---

### [Motion（前身为 Framer Motion）：JavaScript 和 React 动画库](https://motion.dev/)

**原文标题**: [Motion (prev Framer Motion): JavaScript & React animation library](https://motion.dev/)

overview summary
Motion 是一款開源、MIT 授權的專業級 Web 動畫庫，提供 React、JavaScript、Vue 版本，具備混合引擎、AI 整合、小巧體積等優勢，並附豐富範例、開發工具與社群生態。

- 🎉 完全免費開源：採用 MIT License，可自由使用於商業與個人專案。
- 🏭 生產級可靠：被 Framer、Figma 等大型平台採用，支撐數十萬網站動畫。
- ⚙️ 混合引擎：結合 JavaScript 與硬體加速瀏覽器 API，實現高效能動畫。
- 🤖 為 AI 打造：提供代理相容文件、技能與 API，方便 AI 輔助開發。
- 🪶 輕量體積：API 體積比 GSAP 縮小最高 90%。
- 🎯 核心功能豐富：支援獨立變形、捲動動畫、原生手勢（hover/press/drag）、佈局動畫、彈簧物理、退出動畫、時間軸序列與 motion values。
- 📋 範例庫齊全：提供 430+ 可複製貼上的實例，涵蓋磁性游標、無限捲動、骨架閃爍等效果。
- 🧩 工作流加速：AI Kit 提供代理專屬動畫知識，Motion UI 提供生產級動畫區塊，兩者合併於 Motion+ 訂閱。
- 🏆 社群展示：集結 Motion 社群優秀作品，並開放投稿。
- 📢 持續更新：最新 v13.1.0 加入 Reorder 多維排序、RTL 支援；v13.0.0 改進 SVG 硬體加速與 AnimatePresence 行為。
- 🤝 業界合作：獲得 Framer、Cursor 等夥伴贊助與整合。
- 📊 MotionScore 審計：免費 60 秒網站動畫效能評級（S–F），提供代理可用修正建議。
- 📚 完整文件：涵蓋 React、JavaScript、Vue 三種 runtime，並提供 CSS Studio 等開發工具。

---

### [Baseline 如何帮助你减少 JavaScript 的交付量 — Smashing Magazine](https://www.smashingmagazine.com/2026/08/how-baseline-can-help-ship-less-javascript/)

**原文标题**: [How Baseline Can Help You Ship Less JavaScript — Smashing Magazine](https://www.smashingmagazine.com/2026/08/how-baseline-can-help-ship-less-javascript/)

文章介绍如何利用浏览器 Baseline 特性，通过审计和替换 JavaScript 依赖来显著减少打包体积。作者提供了可复用的决策框架，并分集群展示国际化、HTTP、UI 组件、Lodash 工具等常见依赖的原生替代方案，同时说明 Temporal 等暂不宜替换的反例，最后给出完整的审计流程。

- 📦 典型中型应用的依赖中，约有 60–90KB（gzipped）可被浏览器原生功能替代，显著减小 bundle 体积。
- 🧭 Baseline 分三档：有限可用、新可用、广泛可用（需 30 个月）；广泛可用才可放心直接替换，新可用则需检查受众。
- ❓ 替换前问三问：原生功能是否对你的用户安全？替换成本（如 polyfill 大小）是否划算？平台功能是否覆盖你的实际用法？
- 🌍 国际化集群：`Intl.RelativeTimeFormat` 替代 timeago.js，`Intl.NumberFormat` 替代 numeral，`Intl.ListFormat` 替代列表连接；`Intl.DurationFormat` 仍属新可用，需谨慎。
- 🌐 HTTP 集群：`fetch` + `AbortSignal.timeout` 可替代 axios 的基本请求，但缺少自动错误拒绝、拦截器、重试和上传进度，需按实际使用评估。
- 🎨 UI 集群：`<dialog>` 元素替代模态框和 focus-trap，Popover API 与 CSS anchor positioning 替代工具提示/下拉库，并带来更好的可访问性。
- ⚙️ Lodash 集群：`Object.groupBy`、`Map.groupBy`、`structuredClone`、Set 方法（union/intersection 等）可替代分组、深克隆和集合操作；debounce/throttle 仍无原生替代。
- ⏳ Temporal 案例：尚未达到 Baseline，且 polyfill 体积（19–44KB）远超现有库（如 dayjs 约 3KB），目前不建议替换，应等待 Safari 稳定支持。
- 🔍 审计流程：列出生产依赖、测量各包体积、检查替代特性的 Baseline 状态、用三问决策、并通过特性检测渐进增强。
- 📅 未来机会：Temporal 原生支持、CSS anchor positioning 成熟、`Object.groupBy` 达到广泛可用后，将带来更多依赖替换空间。

---

### [](https://day.js.org/)

**原文标题**: [Day.js · 2kB JavaScript date utility library](https://day.js.org/)

Day.js 是一个轻量级、与 Moment.js API 兼容的现代 JavaScript 日期时间库，体积仅 2kB，支持不可变操作与国际化，并拥有活跃的社区与赞助生态。

- 📦 极简体积：仅 2kB，比 Moment.js 更轻量，减少下载、解析和执行时间。
- 🔄 API 兼容：采用与 Moment.js 基本一致的 API，熟悉 Moment.js 即可零成本上手。
- 🛡️ 不可变设计：所有修改操作返回新实例，避免因数据变更引发 bug 与调试难题。
- 🌍 国际化支持：内置优秀的 i18n 能力，但按需加载，不会额外增加打包体积。
- 🧩 插件生态：依赖特定功能时需配合相应插件使用，保持核心库精简。
- 🤝 社区与赞助：提供 GitHub、Gitter 等交流渠道，并由多家赞助商支持持续开发。
- 📄 版权与文档：官网包含 Docs、GitHub 入口及多语言翻译，欢迎参与贡献。

---

### [](https://www.jsdelivr.com/blog/making-more-npm-packages-work-with-jsdelivr-esm/)

**原文标题**: [Making More npm Packages Work with jsDelivr ESM mode](https://www.jsdelivr.com/blog/making-more-npm-packages-work-with-jsdelivr-esm/)

jsDelivr 团队升级了 `/+esm` 工具链，并通过生产环境 APM 数据定位和修复了大量 npm 包兼容性问题，涵盖依赖升级、CommonJS 互操作、Node.js polyfill、source map 和性能优化，使更多包可在浏览器中直接运行。

- 🔄 升级后端为原生 ESM，并将 Rollup 从 2 代升到 4 代，同时修复了 JSON import attributes 等语法兼容问题。
- 📜 对声明 `"type": "module"` 的包，其 `.js` 入口不再进行 CommonJS 转换，从而支持顶层 `await`。
- 🌍 扩展 `NODE_ENV` 替换规则，覆盖 `globalThis.process`、`global.process`、括号属性写法等多种生成代码变体，同时避免误替换普通对象键。
- 🐚 将包入口的 `#!` shebang 替换为 `//` 以保持 source map 行列对齐，并修复 `browser` 字段中的自映射逻辑。
- 🔍 增强 CommonJS 命名导出检测：识别 TypeScript 的 `__exportStar`，合并两种 `cjs-module-lexer` 结果，支持条件分支赋值和非标识符属性名。
- 🔗 修复 CommonJS 导入外部 ESM 依赖时的默认导出误判，保留命名导出，并移除人为合成的 `export default null`。
- 📂 通过 `resolveImportMeta` 保留各模块发布时的 npm URL，使 `import.meta.url` 能正确解析同目录下的 `.wasm`、worker 等资源文件。
- 🗺️ 修复 source map 中空源、非法 `sourceRoot` 及 `sourcesContent` 冲突导致的加载失败，并改进生成 map URL 的标识方式。
- 🌳 将暂不支持的 Node.js 内置模块转为无副作用虚拟模块，先让 Rollup 进行 tree-shaking，若仍残留再返回原错误信息。
- 🛠️ 扩展 Node.js 兼容层共 16 项，涵盖 `util`、URL/path、`timers/promises`、`crypto`、`fs` 等 API，并修复多个 polyfill 实现和解析问题。
- ⚡ 对 ESM 包的最终压缩改用 esbuild 替代 Terser，大文件（>4MiB）同样走 esbuild；外部包 manifest 改为每包只拉取一次并复用。
- 📱 识别直接在 `.js` 中发布 JSX 的 React Native 包，返回明确的“unsupported JSX”提示，而非当作未知崩溃。
- ✅ 所有修复均配套回归测试；结合用户报告与生产数据，大幅减少了剩余兼容性积压，并让剩余失败原因更清晰。

---

### [jsDelivr - 为 JS 和开源提供的免费、快速、可靠的 CDN](https://www.jsdelivr.com/)

**原文标题**: [jsDelivr - A free, fast, and reliable CDN for JS and open source](https://www.jsdelivr.com/)

概述：这是一个为开源项目提供免费 CDN 服务的介绍，强调其快速、可靠、自动化，支持 npm 和 GitHub 的 JS 及 ESM 交付，自 2012 年运营，拥有巨大流量。

- ⚡ 提供免费 CDN，专为开源项目设计，主打快速与可靠
- 🤖 自动化服务，简化资源分发流程，无需手动干预
- 📦 优化了来自 npm 和 GitHub 的 JavaScript 与 ESM 模块交付
- 🌐 兼容所有 Web 格式，适用场景广泛
- 🗓️ 自 2012 年起持续运营，经验丰富
- 📊 过去一个月处理了 1500 亿次请求
- 💾 过去一个月数据流量超过 5000 TB

---

### [](https://sentry.io/resources/etsy-workshop/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=ecommerce-fy27q3-etsyworkshop&utm_content=newsletter-sponsored-link-register)

**原文标题**: [How Etsy's Engineers Keep Their App Crash-Free During Traffic Spikes | Sentry](https://sentry.io/resources/etsy-workshop/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=ecommerce-fy27q3-etsyworkshop&utm_content=newsletter-sponsored-link-register)

概述：Etsy 工程师如何在流量高峰期确保应用不崩溃，强调崩溃对收入的直接影响，并分享高峰流量应对、实时调试及业务影响衡量的实战经验。
- 📈 高峰期崩溃不仅是技术问题，更是收入损失问题
- 🛠️ Etsy 与 Sentry 专家（Jay Henry 和 Sergiy Dybskiy）联合分享实战经验
- 🚦 工程团队如何为峰值流量做好准备，确保应用稳定
- 🔍 实时调试技巧，快速定位并解决崩溃问题
- 💰 量化崩溃对业务的影响，在关键时刻优先修复
- 📖 提供真实事件案例与可落地的实践建议
- 🔗 附带更多资源：电商监控清单、会话回放调试、关键用户体验修复指南

---

### [](https://remysharp.com/2026/08/05/progressive-enhancement-inside-of-javascript)

**原文标题**: [Progressive Enhancement inside of JavaScript](https://remysharp.com/2026/08/05/progressive-enhancement-inside-of-javascript)

概述：作者通过一次慢速网络下的体验，探讨了渐进增强在 JavaScript 内部的应用，强调优先捕获用户交互并延迟加载重型模块，以提升网站在劣质网络下的可用性。

- 🚆 作者在火车上使用慢速网络时，发现许多网站加载失败，自己也遇到了类似问题。
- 🔧 渐进增强不仅适用于 HTML 由 JavaScript 增强，同样适用于 JavaScript 代码内部。
- 🎯 核心思考：能否在页面未完全就绪时，先捕获用户的操作意图？
- 📹 视频对比显示：修复前拖放文件会跳转到原始文本；修复后页面保持并显示“Loading”提示。
- 🐌 原代码需从 esm.sh 下载并解析约 600kB（解压后 1.3MB）的依赖，导致核心渲染逻辑被阻塞。
- ⚡️ 改进方法：将事件绑定、队列逻辑和视觉反馈内联在 HTML 后，优先响应用户操作，再延迟加载重量级模块。
- ✅ 即使在 GPRS 网络下，最终也能完成完整交互，耗时接近 2 分钟。
- ☁️ 项目本身无后端，作者考虑使用 Netlify ODB 上传渲染，速度可能更快。
- 💡 作者强调这不是新方法，而是因现实场景被重新提醒。

---

### [](https://blog.cloudflare.com/astro-issue-triage/)

**原文标题**: [How we built a software factory to drive Astroâs GitHub issue count to zero | Cloudflare Blog](https://blog.cloudflare.com/astro-issue-triage/)

Astro 团队通过构建一套由 AI 代理驱动的自动化 triage 管道（即“软件工厂”），将 GitHub 仓库的问题数从 200 多个降至约 30 个，并预计下月归零。该方案不仅提升了维护效率，还衍生出开源框架 Flue 和 triagebot-action，展示了 AI 代理在开源维护中的实际价值。

- 🤖 自动化 triage 管道：读取 bug 报告、在沙盒中复现、诊断根因，并发布预览版本供报告者验证。
- 🧩 每个阶段由隔离的子代理执行，通过 report.md 顺序传递信息，避免 LLM 强行臆断修复。
- 🏷️ 整个流程由 issue 标签驱动的状态机控制：新问题标记 `triage needed`，用户确认后转为 `fix verified`。
- 🚀 修复成功后自动通过 `pkg.pr.new` 生成预览版，并在 issue 中附上总结、日志和安装说明。
- ⚙️ 该自动化泛化为开源框架 Flue，支持通过 Slack、cron、webhook 等任意事件触发，不局限于 GitHub。
- 👥 自动化释放了维护者时间，使其能更深入参与 Discord 讨论、RFC 评审和新功能协作。
- 🔍 代理修复失败常暴露代码库隐患：不透明抽象、缺失注释文档、测试覆盖不足。
- 📝 典型例子：HMR 相关 bug 中代理反复修改某 if 条件导致回归，添加说明注释后行为立即修正。
- 📦 将 triage 逻辑解耦为独立仓库 `triagebot-action`，便于测试与迭代，并已被多个团队直接采用或 fork。
- 🆓 全部代码开源，鼓励开发者借鉴、改造，构建属于自己的自动化“工厂”。

---

### [](https://engineering.myhoai.com/posts/debugging-stuck-node-js-processes/)

**原文标题**: [Debugging stuck Node.js processes | HOAi](https://engineering.myhoai.com/posts/debugging-stuck-node-js-processes/)

生产环境中的 Node.js 应用间歇性卡死，常规调试手段无效。本文介绍了如何通过事件循环分析、追踪检测以及最终使用 Node 内置调试器生成 CPU profile 来定位根因，发现是空字符串上调用 indexOf 导致的无限循环，并分享了保留崩溃报告机制带来的长期收益。

- 🔍 关键应用健康检查间歇失败，日志、指标和本地模拟均无法解释故障原因。
- ⚙️ 卡死时 CPU 单核 100%、无网络和日志活动，指向事件循环被长时间占用。
- 🧭 第一轮使用事件循环阻塞检测器，只能发现小于 5 秒的短阻塞，修复后问题依旧。
- 💡 关键顿悟：若代码永不交还事件循环，基于追踪的检测器无法自报，需要不同方案。
- 🛠 利用 Node 内置调试器（`node inspect`）在容器被杀前生成 5 秒 CPU profile。
- 📈 通过 flame graph 可视化快速定位到问题代码：对空字符串调用`indexOf(str, N)`导致死循环。
- 🧰 崩溃报告入口点保留在生产环境，无性能损耗，后续又发现两个类似隐藏 bug。
- 🌐 已在 GitHub 开源演示工具，只需 Docker 和 curl 即可试用。

---

### [](https://www.youtube.com/watch?v=Xs-U7SY2uNE)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=Xs-U7SY2uNE)

该内容为 YouTube 页面底部的导航与版权信息，提供了平台相关链接、政策说明及版权声明。

- 📄 提供“简介”与“媒体”等基础信息入口
- ⚖️ 包含“著作权”与“条款”等法律相关内容
- 📞 设有“与我們聯絡”的联系方式
- 🎬 面向“創作者”与“廣告”合作提供专门入口
- 👨‍💻 提供“開發人員”相关资源
- 🔒 包含“隱私權”及“政策與安全性”说明
- 🛠️ 解释“YouTube 運作方式”并支持“測試新功能”
- ©️ 标注版权归属为 2026 Google LLC

---

### [](https://celld.dev/)

**原文标题**: [celld: self-hosted, distributed Durable Objects](https://celld.dev/)

celld 是一个自托管的分布式 Durable Objects 实现，基于 V8、SQLite、LTX 与 S3，完全兼容 Workers/DO API，在提供高持久性、低延迟和高密度的同时，显著降低大规模运行成本，并让用户掌控数据与故障域。

- 🚀 兼容性：Workers 和 Durable Objects 代码无需修改即可运行，支持常用 API。
- 💾 数据主权：数据存放在用户自己的 bucket 中，基础设施由用户选择。
- 💰 成本优势：规模化时比 Cloudflare DO 便宜数倍到数个数量级（如 1,000 个常驻单元：celld $49/月 vs DO $4,150/月）。
- 📦 安装便捷：提供 58 MB 静态可执行文件（curl 安装）或 Docker 容器运行。
- 🛡️ 持久性保证：每个 cell 有 epoch-fenced 写入者，确认写入零丢失（RPO=0），区域本地写延迟约 90 ms，节点故障后约 20 s 完成恢复。
- ⚡ 性能表现：无状态请求 p50/p99 为 0.2/0.3 ms，单线程吞吐约 94k req/s，唤醒休眠 cell 约 4 ms。
- 📊 高密度低成本：每个常驻 cell 仅占 4 MB RAM，8 GB 节点可承载 1,000 个 cell；非活跃 cell 几乎不产生 bucket 操作费用。
- 🔧 工作原理：以 bucket 为协调者，无成员协议/失败检测/共识；所有权通过一次原子写（CAS）声明，内置复制器持续将 SQLite 状态以 LTX 段备份至 bucket。
- 🔁 可靠性设计：cell 身份与机器解耦，所有权为租约；节点丢失后其他节点可接管并恢复，失败域由用户自行划定，且故障证据（SQLite/LTX 文件、日志）可直接用 sqlite3/grep 检查。
- ❤️ 致敬与许可：celld 是向 Cloudflare Durable Objects 模型（Kenton Varda 与 Workers 团队）的致敬之作，由 Deno Land Inc. 开发，采用 Apache-2.0 许可。

---

### [](https://github.com/denoland/celld)

**原文标题**: [GitHub - denoland/celld: self-hosted, distributed Durable Objects · GitHub](https://github.com/denoland/celld)

celld 是一个开源的自托管分布式 Durable Objects 守护进程，可在自有机器上运行 Cloudflare Workers 和 Durable Objects。每个对象作为独立 SQLite 数据库按名称寻址，并通过用户拥有的 S3 兼容存储桶复制；节点仅通过该桶协调，无需控制平面或共识。应用天然分片，空闲单元可休眠至近零资源占用。

- 📦 开源自托管分布式 Durable Objects 运行时，每个对象是独立 SQLite 数据库，并通过 S3 兼容桶复制。
- ⚖️ 节点使用对象存储的 CAS 机制保证单一所有权，无控制平面、故障检测或共识服务。
- 💤 空闲 cell 休眠至近零资源，唤醒时恢复数据库并继续执行，桶是持久真相源。
- 🚀 安装简单：curl 一键安装，支持 gh attestation 验证；另有 Docker 镜像（Linux x86-64/ARM64）。
- 🔧 使用标准 AWS 凭证链，`celld deploy` 部署 Worker，支持 Wrangler 配置子集、静态资产和 co-deployed assets。
- 🛡️ 安全设计：peer HTTP 不终止 TLS，需私有网络或加密覆盖；协议带版本、HMAC 认证、防重放，并拒绝公开广告地址（除非显式允许）。
- 📊 `celld diagnose` 检查节点租约、探测健康，并支持压力 shedding（水位、内存、CPU 触发），释放空闲 cell 而不重置 epoch。
- 🏗️ 从源码构建：`cargo build --locked`；协议定义在 `crates/celld/protocol.rs`，测试含故障注入模拟。
- 📧 贡献需通过邮件发送 `git format-patch`（禁用 PR），并要求贡献者同意 CLA 权利分配。
- 📄 许可证 Apache-2.0，公开部署前需阅读 limitations 与 security 页面。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Data 是一个基于 Postgres 构建的时间序列数据平台，专为大规模物联网和指标监控场景设计，强调弹性扩展、高可用、企业级安全与深度可观测性，并提供免费试用额度。

- 📊 支持真实世界超大负载：单实例每日处理 3 万亿指标、存储 3PB 数据，管理 1 千万亿数据点。
- 💵 新用户注册即送$1000 美元额度，30 天内有效，无需绑定信用卡。
- ⚙️ 弹性扩展：通过最多 10 个副本节点实现读写分离，并采用 SSD/S3 分层存储，兼顾性能与成本。
- 💰 计算与存储解耦，可独立伸缩，避免为闲置容量付费。
- 🔄 高可用保障：多可用区集群、自动故障转移、时间点恢复及跨区域备份。
- 🔐 企业级安全合规：通过 SOC 2、HIPAA、GDPR 认证，提供全程加密、SSO 集成、RBAC 权限控制和审计日志。
- 📈 深度可观测性：支持查询钻取与可视化仪表盘，可集成 CloudWatch、Datadog、Prometheus 监控体系。
- ⚡ 极速部署：数分钟内即可创建数据库，并支持 SQL、CLI、Terraform、Cursor 及 Claude Code 进行管理。
- 🔌 生态集成：适配主流云服务商及 Postgres 周边工具链。
- 🛠️ 企业级支持：提供合同化可用性 SLA、区域数据隔离及 24/7 全球专家支持。

---

### [](https://github.com/productdevbook/hucre)

**原文标题**: [GitHub - productdevbook/hucre: Zero-dependency spreadsheet engine. Read & write XLSX, CSV, ODS. Pure TypeScript, works everywhere. · GitHub](https://github.com/productdevbook/hucre)

hucre 是一款零依赖、纯 TypeScript 的电子表格引擎，支持 XLSX、CSV、ODS、JSON、NDJSON、XML 等多种格式的读写，具备流式处理、往返保留、密码保护、图表与透视表等丰富功能，可在 Node.js、Deno、Bun、浏览器及边缘运行时中运行。

- 📦 零依赖、纯 TypeScript 实现，支持 XLSX、CSV、ODS、JSON、NDJSON、XML 等多格式读写。
- 🌳 支持树摇（tree-shaking），按子路径导入可显著减小打包体积，gzip 后约 4–129 KB。
- ⚡ 提供流式读写（streamXlsxRows、writeXlsxStream）与增量写入器，可处理数百万行数据并保持较低内存占用。
- 🔒 内置 XLSX 密码保护（Agile 加密），基于 WebCrypto，零额外依赖，兼容 Node.js 与浏览器。
- 📖 可读取旧版 XLSB 和 XLS（BIFF8）文件，支持共享字符串、公式缓存值、合并单元格等。
- 🔄 支持往返保留（openXlsx/saveXlsx），未建模的部分按字节复制，图表、宏等可无损保留。
- 📊 原生支持图表读取、写入与克隆，覆盖柱状、折线、饼图等主流类型；透视表可写入结构骨架。
- 🧩 提供统一 API（read/write/readObjects/writeObjects），自动检测文件格式，简化对象操作。
- 🖥️ 附带 CLI 工具，可执行 convert、inspect、validate 命令，支持多种格式互转。
- 🛠️ 提供工作表操作（插入/删除行列、排序、克隆、移动）并智能更新公式和引用。
- 📄 支持 HTML/Markdown 导出与 HTML 表格导入，另含 JSON/NDJSON/XML 处理工具。
- 🔢 内置数字格式渲染器、日期工具、单元格引用解析和构建器 API（WorkbookBuilder）。
- 📋 提供模板引擎（{{placeholder}} 填充）、Excel 2024 原生复选框、无障碍（WCAG 2.1 AA）审计功能。
- ✅ 支持模式验证（validateWithSchema），含类型强制、正则、自定义校验和错误收集。
- 🌍 跨平台支持：Node.js、Deno、Bun、现代浏览器、Cloudflare Workers 等。
- 🏆 相比 SheetJS/ExcelJS 等库，依赖更少、ESM 原生、TypeScript 类型完善、支持流式与 ODS。
- 🧱 架构模块化：内置 ZIP/XML 引擎，符合 CSP，无 eval，worker 友好。
- 🛣️ 路线图中规划了公式计算、更多图表类型写入、流式 XML 读取、XLS/XLSB 写入等未实现功能。

---

### [](https://www.vlt.io/blog/1-0)

**原文标题**: [vlt 1.0 & Hosted Package Registries | vlt /vōlt/](https://www.vlt.io/blog/1-0)

vlt 1.0 正式发布，同时托管 JavaScript 包注册表与生态镜像也进入普遍可用阶段。vlt 已发展为一个安全优先、功能完整的包管理器，可作为 npm 的直接替代品，并通过新的托管服务提供兼容、高性能、隐私保护和主动恶意软件拦截，旨在帮助开发者、团队及 AI 代理更快速、安全、可靠地交付软件。

- 🎉 宣布 vlt 1.0 稳定版及托管注册表/生态镜像全面可用，形成端到端开发平台
- 🔍 提供 60+ 图原生伪选择器，其中约 30 个专攻安全领域，如 :malware、:cve、:unmaintained、:license、:vuln、:peer 等
- 🖥️ :host(local) 支持跨本机所有项目查询依赖，例如用 `vlt query ':host(local) #react:v(<19)'` 查找旧版 React
- ⚙️ --scope 标志将选择器能力扩展到 run、exec、pkg、version、pack、publish 等命令
- 🧩 Graph Modifiers 可通过 DSS 选择器及 CSS 特异性规则覆盖 vlt.json 中的任何依赖
- 📦 分阶段安装：vlt install 下载但默认不执行脚本，vlt build 选择性运行并默认阻止已知恶意软件
- 📚 Catalogs 支持在 vlt.json 中一次性定义依赖版本，并跨项目通过 catalog: 引用
- 🔐 OIDC 可信发布：CI 中无需长期令牌即可发布到 npm 公共注册表，开箱支持 GitHub Actions，并兼容 GitLab CI 和 CircleCI
- 🔄 vlt 客户端是 npm 的即插即用替代品，可运行完整的包生命周期，无需 npm 回退
- 🌐 托管注册表与 npm API 向后兼容，支持 npm、pnpm、yarn、bun 和 deno 安装及发布
- 💸 提供慷慨的免费层级，降低私有注册表的使用门槛，定价简单透明
- ⚡ 通过边缘基础设施分发包，冷安装性能在基准测试中比 npm 快最多 38%
- 🛡️ 私有包强制作用域隔离并验证清单，拒绝格式错误或不一致的发布内容
- 🚨 主动摄取 OSV 等恶意代码源，在索引阶段即拦截恶意包；已标记超 27.5 万个包版本，其中超 25% 仍可在 npm 公共注册表下载
- ✍️ 现在即可注册账号名称，并开始安装或发布包

---

### [宣布 TanStack Table V9 | TanStack 博客](https://tanstack.com/blog/announcing-tanstack-table-v9)

**原文标题**: [Announcing TanStack Table V9 | TanStack Blog](https://tanstack.com/blog/announcing-tanstack-table-v9)

TanStack Table V9 经过两年多开发正式发布，这是一个基于全新架构的重大版本，重点包括：创纪录的框架适配器、大幅性能提升、基于 TanStack Store 的状态管理重构、更强的类型安全、树摇支持、可组合性以及多项新功能。该版本为未来扩展奠定基础，并提供了各框架的迁移指南。

- 🚀 正式发布：TanStack Table V9 稳定版发布，历时两年多，核心逻辑和 headless 渲染模型保持不变。
- 🔌 框架适配器：支持 10 个专用适配器（React、Preact、Vue、Solid、Svelte、Angular、Lit、Alpine、Ember、Octane），所有适配器的响应式系统均基于 TanStack Store 重新设计。
- ⚡ 性能提升：共享原型降低内存占用，百万行场景下保留堆内存减少最多 86%；处理速度核心行模型提升 3.9 倍、分组聚合 1.7 倍、排序 1.6 倍、过滤 1.5 倍。
- 🧠 状态管理：基于 TanStack Store 和 alien-signals，实现细粒度订阅，组件只渲染使用的状态切片。
- 🛡️ 类型安全：可为每个表单独定义元数据类型，API 根据注册功能自动推断，前置条件在编译期检查，并优化了 TS 性能。
- 🌳 树摇与扩展：功能是显式、模块化的，只注册需要的功能即可减小打包体积，自定义功能与内置功能拥有同等的类型体验。
- 🧩 可组合性：`tableOptions()` 和 `createTableHook()` 可以组合复用配置，构建一致的表格系统，同时保持类型推断。
- ✨ 新功能：新增单元格选择（矩形范围、拖动、Shift 扩展）、单元格跨行跨列、多聚合列、行选择的 Shift 范围选择、`table.getMaxSubRowDepth()` 和 `row.getDisplayIndex()` 等 API。
- 🔮 未来方向：V10 发布将比 V8 到 V9 快得多，计划中包括 Solid 2 支持、完全透视、高级过滤表达式等。
- 📖 迁移指南：各框架（React、Preact、Vue、Solid、Svelte、Angular、Lit）提供迁移指南，Alpine、Ember、Octane 有快速入门，均从 Table V9 快速入门开始。

---

### [TanStack 存储](https://tanstack.com/store/latest)

**原文标题**: [TanStack Store](https://tanstack.com/store/latest)

overview summary
Store 是一个框架无关的轻量级响应式状态核心，专注于客户端局部状态，提供不可变更新、派生值、批处理与选择性订阅。它不规定整体架构，可独立使用或作为 TanStack 底层基础设施，并支持多种框架适配器。

- 🧠 **核心定位**：Store 是框架无关的 signals 实现，专为“局部状态”设计，强调小体积与明确边界。
- 🔒 **不可变更新**：通过 `createStore` 创建状态，使用 `setState` 显式更新，保证更新路径清晰且可预测。
- 🔄 **派生与批处理**：支持从其他 store 计算派生值，并可将多个相关写入合并为一次批量更新，提升性能。
- 🎯 **选择性订阅**：通过 selectors 让组件只订阅自己渲染所需的状态切片，避免多余重渲染。
- 🧩 **四个基础原语**：Store（状态值）、Derived（派生）、Batch（批处理）、Select（选择），保持核心直接而克制。
- ⚛️ **框架适配器**：同一套核心可对接 React、Preact、Solid、Vue、Angular、Svelte、Lit，仅绑定层不同，状态模型不变。
- 🏗️ **基础设施而非架构**：Store 只提供响应式原语，不强制应用级状态方案，适合用于客户端信号、局部派生与精确订阅。
- 📦 **生态定位**：与 Router（URL 状态）、Query（服务端状态）、DB（数据图）明确分工，只负责客户端 reactive 状态。
- 📈 **社区数据**：总下载量超 4.29 亿，周下载约 2784 万，GitHub 星标 877。
- 🤝 **赞助支持**：提供金/银/青铜及 OSS 赞助计划，赞助者可获得 Discord 私密频道、优先 issue 处理与直接支持。

---

### [](https://tanstack.com/blog/tanstack-table-v9-reactivity)

**原文标题**: [Inside TanStack Table V9 Reactivity | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-reactivity)

TanStack Table V9 的核心改进是重新设计响应式架构：将状态与选项读取下沉到框架无关的核心层，通过统一原子契约让各框架原生追踪依赖，从而在选中行、列宽调整等场景中实现仅更新相关组件的高性能渲染，同时保持对外 API 基本不变。

- 🔍 **直面渲染性能痛点**：复杂数据网格中，选中一行仅需更新复选框和计数器，不应让所有单元格重渲染；搜索、列缩放等更会放大性能问题。
- 🏛️ **V8 旧架构局限**：V8 通过稳定表格实例 + `setOptions` 同步外部状态，框架无法感知方法内部读取了哪些状态，导致依赖追踪缺失。
- 🔮 **Angular 早期尝试**：通过 Proxy 包装表格方法并用 `computed` 实现响应式，但只能覆盖表格实例方法，`flexRender` 渲染的组件仍需宽泛地检查更新。
- ⚡ **React Compiler 暴露问题**：稳定的 `row` 引用背后 `getIsSelected()` 变化时，编译器无法察觉方法内隐藏的状态读取，导致错误复用备忘录 JSX。
- 🔧 **V9 初期方案与瓶颈**：先尝试包装所有表格对象的每个方法，但对象规模呈 `R × C × N` 爆炸式增长，实际只依赖少量共享状态，方向不可行。
- 📡 **引入 TanStack Store**：核心采用 signal 驱动的 Store 和原子（Atom），使状态读取具备依赖追踪能力，从根本上解决方法包装问题。
- 🧩 **Options 纳入响应式图**：新增 `optionsStore`，让 `data`、`enableRowSelection` 等选项变化也能被表格读取处追踪，避免强制刷新适配器。
- 🔗 **双图同步的困境**：Store 核心与框架原生响应图之间用 notifier 桥接会出现漏更新或重复渲染，最终方案改为每个适配器原生实现统一原子契约。
- 🎯 **状态切片原子化**：分页、行选择、列宽、过滤等每个 feature 拥有独立 atom，方法如 `getIsAllPageRowsSelected` 仅依赖实际读取的状态。
- 🧬 **最终设计：统一契约**：核心仅依赖 `Atom`/`ReadonlyAtom` 接口，Angular/Solid/Vue 用原生信号、React 用 `@tanstack/react-store`、Ember 用 `@tracked`/`@cached` 实现，各适配器可复用同一套构造逻辑。
- ⚛️ **Signal 原生适配器自动追踪**：在 Angular/Solid/Vue 的 `computed`/`memo`/effect 中调用表格方法，即可自动注册依赖，实现精确更新。
- 🖥️ **React 选择性订阅**：React 通过 `useSelector`/`Subscribe` 显式订阅状态切片，隔离行选择、列宽等高频变更，且兼容 React Compiler 保持单元格备忘录化。
- ✅ **对外 API 不变**：应用仍传普通值、调用相同的方法，复杂度被封装在库内；最终效果是“选一行只更新该复选框和计数器，其他组件不受影响”。

---

### [](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

**原文标题**: [How an Underrated Refactor Saved 90% Memory Usage | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

在 TanStack Table V9 中，一项看似不起眼的“共享原型”重构，使处理大规模表格时的内存占用相比 V8 最高降低约 90%，可处理行数从约 100 万提升到 1000–1600 万；文章详细介绍了基准结果、实现原理、为何不用类、以及带来的破坏性变更。

- 🚀 大规模场景下 V9 比 V8 内存占用减少最多 90.5%，处理 800 万单元格时可节省约 2.4 GB 内存。
- 📊 基准测试覆盖分页、虚拟行、虚拟列和“综合”场景；小表差异不大，数据量越大优势越明显。
- 🔬 内存测量通过 Playwright 和 Chrome DevTools Protocol 完成，强制垃圾回收并记录保留 JS 堆。
- 🧠 V8 为每个 row/column/cell/header 对象都创建独立方法副本和闭包，导致海量重复内存开销。
- ⚙️ V9 改为在每个 table 实例上缓存共享原型，用 `Object.create` 创建对象，方法通过原型共享，并通过 `this` 获取当前实例。
- 🏷️ 该模式应用于 row、column、cell、header 对象，其中 row 对象收益最大。
- 🔀 不用 JavaScript 类，是因为 TanStack Table 的特性系统是动态组合的，类继承难以满足“按需注册 API”的灵活性。
- ⚠️ 这一重构带来破坏性变更：方法不能解构调用、不再是自身属性、浅拷贝会丢失方法，因此未在 V8 中实施。
- ✅ 对使用者来说几乎是隐形优化，官方会在 V8→V9 迁移指南中记录相关破坏性变更。

---

### [](https://github.com/sveltejs/devalue)

**原文标题**: [GitHub - sveltejs/devalue: Gets the job done when JSON.stringify can't · GitHub](https://github.com/sveltejs/devalue)

devalue 是一个 JavaScript 序列化工具，作为 JSON.stringify 的增强替代，能够处理循环引用、重复引用及多种特殊类型，并提供安全紧凑的输出。它提供多种 API 支持同步/异步序列化、自定义类型和跨运行时操作，同时着重于 XSS 防护。

- 🔄 支持循环引用（如 `obj.self = obj`）和重复引用（如 `[value, value]`）
- 🧩 支持 `undefined`、`Infinity`、`NaN`、`-0`、正则、日期、`Map`、`Set`、`BigInt`、`ArrayBuffer`、Typed Arrays、`URL`、`URLSearchParams`、`Temporal`、`Promise` 等特殊类型
- 🚀 核心目标为性能、安全（XSS 缓解）和紧凑输出，非目标包括人类可读性、函数序列化和版本间稳定性
- 📦 提供 `uneval`（生成等价 JS 代码）、`stringify`/`parse`（类似 JSON）、`stringifyAsync`（异步处理 Promise）、`unflatten`（从 JSON 片段恢复数据）等多种 API
- 🎨 支持自定义类型：通过 reducers/revivers 实现序列化/反序列化，也可用 replacer 配合 `uneval`
- ⚙️ 自定义操作（operations）允许无副作用序列化、外部运行时（如 `node:vm`）的序列化与恢复，以及跨 realm 的构造
- 🛡️ XSS 缓解：`uneval` 和 `stringify` 会转义危险字符（如 `</script>`），且对函数和非 POJO 抛错，防止任意代码执行
- ⚠️ 安全注意事项：不应使用 `uneval` 将用户数据从客户端发到服务器；使用 `eval` 时应采用间接调用（如 `(0,eval)(...)`），避免访问作用域
- 📚 项目受 `arson`、`oson` 等启发，并参考了 `lave`、`tosource`、`serialize-javascript` 等

---

### [](https://github.com/rob-balfre/svelte-select)

**原文标题**: [GitHub - rob-balfre/svelte-select: Svelte Select. A select component for Svelte · GitHub](https://github.com/rob-balfre/svelte-select)

svelte-select 是一个功能全面的 Svelte 选择/自动补全/typeahead 组件，专为 Svelte 5 设计，提供丰富的 props、snippets、回调函数和样式定制能力，支持多选、异步加载、分组及无障碍访问。

- 📦 安装：通过 `npm install svelte-select` 获取，v6+ 版本要求 Svelte 5，并使用 runes、回调 props 和 snippet props。
- ⚙️ 核心 Props：支持 `items`、`value`、`valueMode`（item/id）、`multiple`、`searchable`、`clearable`、`disabled`、`loading` 等常用配置。
- 🧩 Snippets 自定义：提供 `selection`、`clearIcon`、`chevronIcon`、`list`、`item`、`empty` 等 14 个 snippet，可灵活定制界面各部分。
- 📞 回调函数：包含 `onchange`、`onselect`、`onfocus`、`onclear`、`onerror`、`onfilter` 等，直接接收载荷数据。
- 🔤 Items 类型：支持简单字符串数组、对象集合、分组数据，并可通过 `groupBy` 自定义分组逻辑。
- 🔄 valueMode 模式：`item` 模式绑定完整对象，`id` 模式仅绑定标识符；字符串/原始类型数组自动保持原值，无需额外设置。
- ⏳ 异步加载：通过 `loadOptions` 传入返回 Promise 的函数，内置防抖，并可通过 `{ cancelled: true }` 保持加载状态。
- 🎯 列表定位：基于 floating-ui 实现浮动列表，通过 `floatingConfig` 可自定义位置策略。
- 🛠️ 高级覆盖：支持覆盖 `itemFilter`、`groupBy`、`loadOptions`、`filter` 等核心函数，并通过 `bind:this` 调用 `getFilteredItems()` 和 `handleClear()`。
- ♿ 无障碍：提供 `ariaValues`、`ariaListOpen`、`ariaFocused` 等 props，可自定义屏幕阅读器文本。
- 🎨 样式定制：支持 CSS 自定义属性（如 `--border-radius`、`--placeholder-color`）及 `inputStyles` 内联样式；还提供 `/no-styles` 入口和 Tailwind 样式表，便于集成框架。
- 📚 文档与示例：仓库含丰富示例、迁移指南（MIGRATION_GUIDE.md）和完整测试，方便开发者参考使用。

---

### [](https://github.com/farzher/fuzzysort)

**原文标题**: [GitHub - farzher/fuzzysort: Fast SublimeText-like fuzzy search for JavaScript. · GitHub](https://github.com/farzher/fuzzysort)

fuzzysort 是一个快速、小巧且零依赖的 JavaScript 模糊搜索库，可在 1 毫秒内搜索 13,000 个文件，提供干净的排序和丰富的 API，支持单键、多键搜索，以及快照、自定义归一化和 Web Worker 场景。

- 🚀 性能极佳：<1ms 搜索 13,000 个文件，零依赖，排序结果干净明了。
- 📦 安装简单：支持 npm 安装和 CDN 引入，使用 ESM 模块格式。
- ⚡ 快速上手：通过 `fuzzysort.go('query', targets, options)` 即可对对象数组或字符串进行模糊搜索。
- 🔧 可配置选项：支持 `limit`、`threshold`、`key`、`keys`、`scoreFn`，灵活控制搜索结果和评分。
- 🎯 结果对象丰富：`single()` 返回 `score`、`target`、`indexes`、`obj`，并提供 `highlight()` 方法高亮匹配部分。
- 🧠 高级用法：支持对多个嵌套键（如 `meta.desc`）搜索，并可结合 `scoreFn` 自定义加权评分。
- 💨 性能优化技巧：过滤不必要目标、使用 `snapshot()` 缓存不可变目标、或通过 `prepare()` 预编译目标字符串。
- 🔤 字符重映射：自动进行 NFKD 规范化、去除变音符号，并可用 `fuzzysort.remap()` 自定义字符映射。
- 👷 Web Worker 支持：为结构化克隆后的结果提供 `fuzzysort.score()` 和 `fuzzysort.highlight()` 方法。
- 🆕 v4.0.0 更新：改为 ESM、新增 `snapshot()`、`score()`、`highlight()`、`remap()`，改进多键高亮和子串评分。

---

### [](https://github.com/gtkx-org/gtkx)

**原文标题**: [GitHub - gtkx-org/gtkx: The React framework for Linux. Write native Linux applications with React and TypeScript. · GitHub](https://github.com/gtkx-org/gtkx)

GTKX 是一个面向 Linux 的 React 框架，让开发者使用 React 和 TypeScript 编写原生 Linux 应用。它基于 GNOME 技术栈，提供声明式 UI 层、完整的 GTK4/Adwaita API、Node.js 运行时和代码生成绑定，并包含开发服务器、测试工具、MCP 服务器等。项目已发布 1.0 版本，采用 MPL-2.0 许可证。

- 🚀 GTKX 是 Linux 平台的 React 框架，支持用 React 和 TypeScript 构建原生 Linux 应用。
- 🧩 基于 GNOME 栈和标准 Web 工具，为 GTK4 提供声明式渲染层，弥补 GtkBuilder 静态界面的不足。
- ⚡ 内置开发服务器支持 Fast Refresh，并包含 CSS-in-JS、列表/网格/对话框等高级组件。
- 🖥️ 完整暴露 GTK4、Adwaita 等 GObject-Introspection 库的 API，专为 Linux 设计。
- 🔧 运行于 Node.js 之上，Rust 核心通过 libffi 直接调用系统 GTK4 库，无需 libgirepository。
- 📐 从 GObject-Introspection 自动生成 TypeScript 类型和 FFI 调用，确保类型与实现完全同步。
- 📦 快速开始：执行`npm create gtkx`即可创建新应用，需 Linux 和 Node.js 24+。
- 📚 提供完整文档、教程和多个示例应用（hello-world、gtk-demo、browser、tutorial）。
- ✅ GTKX 1.0 已正式发布，遵循 MPL-2.0 许可证，欢迎贡献。

---

### [首页 - 比利时](https://mplemay.github.io/belgie/)

**原文标题**: [Home - Belgie](https://mplemay.github.io/belgie/)

Belgie 是一个 Python 库，它内嵌了带权限控制的 Deno 运行时，让 Python 开发者能够运行 JavaScript/TypeScript 脚本、管理 JS 依赖、构建 React MCP 应用，并为 AI 智能体提供 JS/TS 沙箱工具。

- 🚀 核心定位：从 Python 中运行 JS/TS/TSX 模块，支持内联或文件脚本，Python 与 JavaScript 之间的数据必须为 JSON 兼容格式。  
- ⚙️ 运行时与脚本：使用 `Runtime` 和 `Script` 类执行代码，支持同步与异步操作，并处理文件导入。  
- 📦 环境与依赖：通过 `Environment` 解析 npm、JSR、URL 及本地文件依赖，并使用锁文件跨多次运行共享依赖或工作区。  
- 🖥️ 命令执行：`Command` 可调用已安装的 JavaScript 包二进制（如 Vite），与运行时共用安全边界。  
- 🧩 MCP 应用：`BelgieExtension` 连接 Python MCP 工具与 React 组件（`<name>/widget.tsx`），开发时由 Vite 驱动，生产时提供自包含的 widget HTML。  
- 🤖 AI 代理集成：提供 `BelgieSandbox`，可为 Pydantic AI 或 LangChain 代理添加 `run_typescript` / `run_code` 沙箱工具。  
- 📥 安装与扩展：基础安装仅需 `uv add belgie`，按需添加集成 extra，如 `uv add "belgie[pydantic-ai]"`。  
- 🧭 选择路径：根据需求选择 Runtime、Environment、Command、MCP Apps 或 AI agents 作为入口，并参考安装指南与故障排除。

---

### [Deno：面向 Node 开发者的即插即用 JavaScript 运行时](https://deno.com/)

**原文标题**: [Deno, the drop-in JavaScript runtime for Node developers](https://deno.com/)

Deno 2.9 是一款快速、开源、与 Node 完全兼容的 JavaScript 运行时，内置 TypeScript 及众多开发工具，性能优于 Node，稳定性优于 Bun，并支持从包管理到桌面应用构建的全流程开发。

- 🚀 性能卓越：npm 安装速度比 Deno 2.8 快 3.66 倍，冷启动比 Deno 2.0 快 1.5 倍，内存效率和 p99 延迟均显著优于 Node 和 Bun。
- 🧰 内置全套工具：无需额外配置即可使用包管理器、测试运行器、格式化器、代码检查器、任务运行器、类型检查器、覆盖率工具、工作区管理器、基准测试器、文档生成器、Jupyter 内核、编译器和桌面应用构建器。
- 🔌 零配置支持 TypeScript 与 npm：可直接导入 npm 包（如 Hono、Chalk），通过 `deno check` 获得完整类型检查，无需 tsc、ts-node 或打包器。
- 📦 兼容 Node 生态：能直接运行 Node 项目，理解 npm、yarn、pnpm 锁文件，支持 CommonJS、node:* 导入、JSX/TSX 等。
- ⚡ 更快的包管理器：支持 npm workspaces，可从 npm 和 JSR 拉取依赖，使用全局缓存替代项目级 node_modules，安装速度远超 npm 和 Bun。
- 📚 内置标准库：提供经审核、无依赖的常用模块（解析、集合、格式化、日期等），由 Deno 团队维护并发布在 JSR 上。
- 🌐 紧跟 JavaScript 前沿：实现浏览器同款 fetch、Request、Response、Crypto 等 Web API，并率先支持 Temporal、Set methods、Iterator helpers、Promise.try 等新标准。
- 🛡️ 三层安全防御：默认拒绝文件系统、网络和环境变量访问；支持作用域授权（如 `--allow-net` 和 `--deny-net`）、子进程隔离、权限跟踪与审计日志；默认禁用 postinstall 脚本，通过 `deno audit` 审计依赖树。
- 📊 可观测性与调试：原生支持 OpenTelemetry（5 秒开启）、CPU 性能剖析（`--cpu-prof`）和 Chrome DevTools/VS Code 调试（`--inspect-brk`）。
- 🖥️ 多平台部署：提供官方 Docker 镜像，可部署到任意 Linux、macOS 或 Windows 平台，也可使用专为 Deno 打造的 Deno Deploy 托管服务，支持 Node 项目无需重写。
- 💻 Deno Desktop：可从 Web 技术栈构建原生跨平台桌面应用，生成 .app、.dmg、.msi、.AppImage 安装包，无需捆绑 Chromium。
- ❤️ 社区庞大：拥有超过 10 万 GitHub stars 和 40 万月活跃用户，被众多生产环境团队信赖。

---

### [展会观察](https://expo.dev/solutions/expo-observe?utm_source=jsweekly&utm_medium=email&utm_campaign=observe-beta)

**原文标题**: [Expo Observe](https://expo.dev/solutions/expo-observe?utm_source=jsweekly&utm_medium=email&utm_campaign=observe-beta)

overview summary
EAS Observe 是 Expo 推出的移动应用性能监控服务，它将性能指标与具体的构建和 OTA 更新直接关联，帮助开发者快速定位回归问题。它自动采集真实设备上的启动、帧率、可交互时间等指标，提供时间线标记、AI 一键交接、会话级详情和路由级分解，并支持可配置采样与隐私保护。

- 📊 自动采集真实用户体验指标：TTI、冷启动、热启动、帧丢失、包加载时间，无需自定义埋点。
- 🏷️ 每个构建/更新在时间线上显示为标记，悬停可看差值，点击可查看该版本的全部会话。
- 🤖 一键将指标、受影响会话、构建和回归差值交给 AI（Claude Code、Cursor 等），无需手动复制粘贴。
- 🔍 支持按指标从慢到快排序，下钻到单个会话，查看设备、系统、国家、更新渠道及完整事件时间线。
- 🧭 通过 Expo Router 集成，按路由拆分可交互时间，快速定位具体慢屏，并支持多选路由跨版本对比。
- 📉 提供 P50/P90/P99 百分位数据，覆盖旧设备、旧系统和不稳定网络，自动采集无需额外配置。
- 🔄 与 Sentry/Datadog 不同：Observe 理解发布管道，能将指标直接归因到特定构建或 OTA，根本原因定位从数天缩短到数分钟，且可互补使用。
- ⚙️ 支持通过 sampleRate 按安装确定性采样（0~1），也可在运行时用 dispatchingEnabled 排除设备，修改需新版本或 EAS Update。
- 📱 目前面向 Expo SDK 55+ 且使用 EAS 的应用，裸 React Native 支持在路线图中。
- 🔒 只收集性能时序、设备型号、系统版本、应用版本和匿名安装 ID，不含个人身份信息，重装后 ID 重置。

---

### [](https://fingerprint.com/try/bot-detection/)

**原文标题**: [Fingerprint | Industry-leading Bot Detection](https://fingerprint.com/try/bot-detection/)

Fingerprint 是一款隐形 Bot 检测 API，开发者用 10 行代码即可集成，用于识别 AI 代理、拦截恶意自动化行为，同时避免 CAPTCHA 对真实用户造成的干扰。产品覆盖假注册、优惠券滥用、账户接管、内容抓取等场景，支持主流前端框架，并提供规则引擎、丰富信号以及开源生态，已获得 Booking.com、Dropbox、Plaid、Binance 等企业信任。

- 🔍 隐形检测：通过 10 行代码集成，无感识别恶意 bot，避免 CAPTCHA 对真实用户的体验损害。
- 🤖 AI 代理识别：能区分签名、验证、未知等状态，覆盖 ChatGPT、Gemini、Claude 等常见 AI 代理。
- 🛡️ 关键防护场景：阻止假注册、结账优惠券滥用、账户接管攻击和自动化内容抓取。
- ⚙️ 开发者友好：支持 React、Next.js、Vue、Angular、Svelte 等前端库，后端可用任意技术消费数据。
- 📜 规则引擎：无需编写代码，即可配置规则并组合信号，拦截更复杂的 bot 攻击。
- 🧬 多信号支持：不仅提供 bot 检测，还通过更多流量信号判断自动化背后的真实意图。
- 🌐 开源可信：基于开源库构建，GitHub 星标 31.2K+，NPM 月下载量超 5.4M。
- 🚀 快速上线：通过包管理器或 CDN 即可设置，无需信用卡或销售沟通，分钟级完成接入。

---

### [](https://merget.ai/)

**原文标题**: [Merget â Version Control for AI Coding | Git Redesigned for AI Engineering
    Teams](https://merget.ai/)

Merget 是一款专为 AI 工程团队重新设计的版本控制系统，将 Git 的每次提交与 AI 提示词、意图和上下文绑定，解决 AI 生成代码时“为什么存在”无从追溯的问题，并提供实时 Token 智能、共享上下文和跨 Agent 协作能力。

- 🔄 为 AI 时代重写版本控制：每次提示词自动变成一次提交，完整记录意图与变更，弥补 Git 无法解释 AI 代码来源的缺陷  
- 🧠 意图不再丢失：提示词与代码差异（diff）深度链接，回答“为什么这样写”不再依赖聊天记录或猜测  
- 📜 历史清晰可读：按行、提示词、目标进行归因，告别“fix stuff”式无意义提交，让代码审查更高效  
- 🌐 统一上下文织物：所有 AI Agent 共享不可变的历史上下文，新会话自动继承先前决策，减少重复摸索和幻觉  
- 📊 实时 Token 智能：追踪每次 AI 提交的 token 消耗、模型性能及代码持久性评分，量化 AI 工程投入产出  
- ⚖️ 全面超越传统 Git Hosts：支持多 Agent 协同、无限持久 LLM 上下文、确定性提示词检查点与代码回滚，以及细粒度审计和治理  
- 🚀 快速上手：连接仓库后约 5 分钟即可看到自动生成的历史记录，并支持 macOS、Windows、Linux  
- 💼 核心主张：AI 虽写一半代码，但团队通过 Merget 完全拥有全部代码的上下文、归因与可控性

---

### [](https://js1024.fun/)

**原文标题**: [JS1024 - Annual Javascript & Shader Code Golfing Competition - Main Page](https://js1024.fun/)

overview summary
这是一个关于 JS1024 年度 JavaScript 与 Shader 高尔夫编程竞赛的全面介绍，涵盖比赛时间、规则、参赛方式、类别、工具资源及日程安排。

- 🎯 比赛目标：在 1024 字节或更少代码内创建 JavaScript 或 GLSL 程序，主题于 7 月 1 日公布，7 月 19 日截止提交，8 月初公布结果。
- 📏 核心规则：源码不超过 1 KiB；禁止恶意代码、外部文件及收集用户数据；需使用私密密钥评分；建议上传带注释的可读版本。
- 🗂️ 参赛类别：经典 Canvas 模式（提供预定义变量）、Shader 演示（类似 Shadertoy，GLSL ES 1.0）、无模板模式（从空白 HTML 自由发挥），p5.js 类别已取消。
- ⚠️ 注意事项：UTF-8 编码中部分字符占多字节；演示需兼容 iframe 导航栏；评分由参赛者互相进行，最高分获第一名。
- 🔧 工具资源：提供 Terser、Babel、GLSL Minifier、Packer、Roadroller 等压缩工具，以及 JavaScript 高尔夫技巧、游戏开发、WebGL 等教程。
- 📚 案例文章：包含钢琴、平台游戏、教育游戏等 1KB 演示的赛后分析，可学习压缩与创意技巧。
- 📅 时间表：7 月 1 日开放提交，7 月 19 日截止，8 月 1 日停止评分，约 8 月 5 日发布结果。
- 💝 支持社区：由 traian 开发，接受捐赠，并列出类似比赛如 js1k、js13kgames 等供参考。

---

### [](https://js1024.fun/results/2026)

**原文标题**: [JS1024 Competition - View results (2026 edition)](https://js1024.fun/results/2026)

您尚未提供需要总结的文章内容。请发送文本，我将按照以下格式为您生成中文摘要：

概述总结
- 📌 要点一
- 🔍 要点二
- 💡 要点三

请提供文章内容，我会立即处理。

---

### [](https://js1024.fun/demos/2026/25/bar)

**原文标题**: [Skydreams by KilledByAPixel - JS1024 Demo](https://js1024.fun/demos/2026/25/bar)

overview summary
Skydreams 是一款由 KilledByAPixel 制作的 Canvas 2D 交互演示，主题围绕天空中的跳跃梦境，玩家可通过鼠标进行控制，并支持分享。

- ☁️ 作品名称为 Skydreams，属于 Canvas 2D 演示
- 👨‍💻 作者是 KilledByAPixel
- 🌌 内容主题为“天空中的跳跃梦境”
- 🖱️ 使用鼠标控制交互
- 🔗 提供“分享演示”的功能选项

---

### [JS1024 - 查看 Skydreams 源代码](https://js1024.fun/demos/2026/25/source)

**原文标题**: [JS1024 - Viewing source of Skydreams](https://js1024.fun/demos/2026/25/source)

您好，您没有提供需要总结的文本内容。请将文章内容发送给我，我会按照您要求的格式（概述总结 + 表情符号项目符号）为您生成摘要。

---

### [](https://js1024.fun/demos/2026/25/source/m)

**原文标题**: [JS1024 - Viewing source of Skydreams](https://js1024.fun/demos/2026/25/source/m)

请提供您需要总结的文章内容，这样我才能按照模板为您生成中文概述和表情符号要点列表。您似乎没有粘贴任何文本，请补充后我再处理。

---

### [](https://www.docker.com/products/docker-sandboxes/)

**原文标题**: [Docker Sandboxes | Sandboxes for Coding Agents | Docker](https://www.docker.com/products/docker-sandboxes/)

概述：Docker Sandboxes 提供专为 AI 编码代理（如 Claude Code、Copilot CLI、Codex 等）设计的本地隔离沙箱环境，基于微虚拟机（microVM）实现硬件级安全隔离，支持快速创建与销毁，并允许代理自主执行安装包、运行 Docker 等操作而不会影响宿主机，同时可通过 Docker AI Governance 实现团队级策略管控。

- 🛡️ 每个代理运行在独立的 microVM 中，与宿主机完全隔离，保护文件系统和网络。
- ⚡ 支持“YOLO 模式”（`--dangerously-skip-permissions`）作为默认选项，让代理无需人工审批即可高速运行，同时保持安全。
- 🔧 可自定义网络和文件系统访问控制，并可通过 Docker AI Governance 在组织范围内强制执行。
- 🖥️ 代理可在沙箱内自行创建和管理 Docker 容器，拥有完整开发环境（安装包、运行服务、无人值守）。
- 🤖 原生支持 Claude Code、Copilot CLI、Codex、OpenCode、Kiro 等主流编码代理，也支持自定义代理。
- 📦 提供多平台安装方式：macOS（`brew install docker/tap/sbx`）、Windows（`winget install Docker.sbx`）、Linux（apt-get）。
- 🚀 启动速度优于传统 VM，默认一次性使用，易于快速创建和销毁（一键 dispose）。
- 💬 获得 NanoClaw 和 Warp 等团队认可，认为其在不牺牲安全的前提下赋予代理自主执行长任务的能力。
- ❓ 常见问题解答：沙箱与普通 VM 的区别、支持的代理列表、YOLO 模式的安全性、无需 Docker Desktop 即可使用，以及通过 Docker AI Governance 增强管理控制。
- 🏢 企业级扩展：提供网络策略、文件系统限制、MCP 治理、集中管理配置，由管理员定义一次，全局生效。

---

### [](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

**原文标题**: [The 2026-07-28 Specification | Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

MCP 发布 2026-07-28 规范，转向无状态协议核心，带来多往返请求、基于头的路由、可缓存列表、授权强化、正式扩展框架及 SDK 更新，旨在提升可扩展性、可靠性和企业级部署能力。

- 🔄 协议核心改为无状态：移除 initialize/initialized 握手和 Mcp-Session-Id，每个请求自描述，可任意落在负载均衡实例上。
- 📡 引入多往返请求（MRTR）：通过 input_required 和 inputResponses 实现工具调用中向用户确认或补参，替代旧的服务器主动请求。
- 🧭 新增基于 HTTP 头的路由：Mcp-Method 和 Mcp-Name 头让网关、限流器、WAF 无需解析 JSON 即可路由和鉴权。
- 🗂️ 列表结果可缓存：tools/list、prompts/list、resources/list 等响应携带 ttlMs 和 cacheScope，减少重复拉取。
- 🔐 授权强化：强制 RFC 9207 issuer 验证，绑定客户端凭证到签发方，并正式弃用动态客户端注册（DCR），转向 CIMD。
- 📋 Tasks 成为正式扩展：新增 tasks/get 和 tasks/update，支持轮询和订阅流，适合长时间运行的代理任务。
- 🚫 弃用 Roots、Sampling、Logging 及旧 HTTP+SSE 传输：至少保留 12 个月，新实现不建议采用。
- 📦 Tier 1 SDK 全部更新：TypeScript、Python、Go、C# 已支持新规范，Rust SDK 提供 beta 版本。
- 🌍 生态广泛支持：AWS、Google Cloud、Cloudflare、Microsoft Foundry、Netlify 等多家公司表示已采用或即将支持。
- 🚀 可立即上手：官方提供规范、完整变更日志、文档和迁移指南，帮助开发者平滑升级。

---

### [](https://blog.cloudflare.com/mcp-v2/)

**原文标题**: [The next generation of MCP | Cloudflare Blog](https://blog.cloudflare.com/mcp-v2/)

MCP 协议迎来重大更新，从有状态连接转变为完全无状态，大幅简化了服务器部署与运维，并已可在 Cloudflare Workers 上使用。

- 🔄 MCP 新规范（2026-07-28）彻底移除了初始化握手、会话 ID 等有状态机制，每个请求自带所需信息，协议变得完全无状态。
- 📦 服务器无需再依赖 Durable Objects 等状态基础设施，可直接作为普通 HTTP 工作负载运行在 Cloudflare Workers 上，降低复杂度和成本。
- 🧩 原 McpAgent 被新的 `createMcpHandler` 取代，并已正式进入官方 MCP TypeScript SDK，代码更简洁，迁移路径清晰。
- 🔁 引入 Multi Round-Trip Requests（MRTR）机制替代旧的交互式 elicitation，服务器可返回 `input_required` 提示，客户端收集信息后重试即可完成操作，无需保持开放流。
- 🛡️ 新增 `Mcp-Method` 和 `Mcp-Name` HTTP 头，网关、防火墙和速率限制器无需解析 JSON 即可识别请求类型，方便按方法进行管理和监控。
- 🔐 授权流程强化：优先支持预注册客户端和 Client ID Metadata Documents（CIMD），采用 RFC 9207 发行者识别，Token 与资源绑定，提升安全性。
- 📅 规范引入正式的功能生命周期（Active/Deprecated/Removed），旧功能至少保留 12 个月，给团队明确的升级时间窗口。
- 🛠️ TypeScript SDK 已完成向 Web 标准迁移，可兼容 Bun、Deno 等运行时；新旧协议客户端可同时支持，平滑过渡。
- 💬 Sentry、Linear 和 Anthropic 均对新规范表示认可，强调其易用性、可靠性以及对开放标准生态的推动作用。
- 🚀 开发者现在即可在 Cloudflare 上构建无状态 MCP 服务器，结合 Workers OAuth Provider 实现安全接入，并享受原有扩展能力。

---

### [](https://scriptc.dev/)

**原文标题**: [scriptc | TypeScript-to-Native Compiler](https://scriptc.dev/)

概述：scriptc 是一个将普通 TypeScript 编译为原生可执行文件的编译器，支持 macOS、Linux 和 Windows，无需 Node 或 JavaScript 引擎即可运行，并保证与 Node 行为逐字节一致。它采用三层显式分级机制：静态编译、动态运行（可选用内嵌引擎）和编译期拒绝，并提供覆盖率报告、差分测试等保障。

- ⚡ 原生编译：普通 TypeScript 直接变成小型原生二进制，无 Node、无 V8、无 JS 引擎，行为与 Node 逐字节一致。
- 📦 三层分级：每个构造明确归属——默认静态编译；`--dynamic` 可选内嵌约 620KB 引擎运行动态代码；其余编译期报错并给出提示。
- 🗺️ 覆盖率报告：`scriptc coverage` 逐语句显示哪些代码可静态编译、哪些需要动态引擎，以及具体阻塞原因。
- 🔄 零改动兼容：无需注解、无方言、无特殊标准库，使用真实 TypeScript 编译器做类型检查，与 Node 代码完全一致。
- 🚀 体积与速度：hello-world 二进制约 320KB，启动约 4ms，仅依赖 libSystem；对比 Node 的 ~120MB 运行时和 ~35ms 启动。
- 🧪 差分测试：所有程序在 Node 和原生二进制下运行，stdout、stderr 和退出码必须逐字节匹配，并定期在 AddressSanitizer 下复测。
- 🛠️ 快速上手：克隆仓库、构建编译器，几分钟内即可将 TypeScript 文件编译为原生可执行文件。

---

### [](https://2026.stateofcss.com/en-US/)

**原文标题**: [State of CSS 2026](https://2026.stateofcss.com/en-US/)

2026 年度的 State of CSS 调查显示，CSS 生态持续演进，但浏览器兼容性仍是核心痛点。锚点定位（Anchor Positioning）成为最受关注的新特性，却因支持不足难以落地；同时，CSS 开发中对 AI 的依赖度相对较低。调查还展现了 CSS 在布局、动画等领域的日益强大。

- 📅 调查于 2026 年 5 月 15 日至 6 月 29 日进行，共收到 4,902 份回复。
- 🎨 2026 年的 CSS 已支持页面过渡动画、masonry 布局，甚至能模拟微处理器、渲染 Doom，还能居中 div。
- ⚓ Anchor Positioning 位列最受欢迎新特性榜首，但也因浏览器支持不足成为开发者回避的首要特性。
- 🖥️ View Transitions、if() 等新特性同样受浏览器支持滞后所限，难以投入实际生产。
- 🌐 浏览器支持差异是生态关键阻碍，Interop 等跨浏览器倡议有望改善这一局面。
- 🤖 AI 生成的 CSS 代码平均仅占 28%，多数评论认为 AI 目前仍不擅长编写高质量 CSS。
- ✨ CSS 作为一门独特语言，历经数十年进化，其现代形态依然充满无限可能。

---

### [Node.js 周报](https://nodeweekly.com/)

**原文标题**: [Node Weekly](https://nodeweekly.com/)

概述：Node Weekly 是一份免费的 Node.js 新闻与文章周报，自 2013 年 8 月发布以来已累积 636 期，并提供订阅、历史归档、RSS 及明确的隐私与反垃圾政策。

- 📧 每周免费电子邮件，汇总 Node.js 新闻与文章
- 📅 已发布 636 期，创刊于 2013 年 8 月
- 🔗 提供订阅、最新一期、全部往期及 RSS 订阅入口
- 🔒 明确公示隐私、反垃圾邮件及 GDPR 政策承诺
- 🏢 由独立机构发布，认真对待用户数据与合规问题

---

### [React 状态](https://react.statuscode.com/)

**原文标题**: [React Status](https://react.statuscode.com/)

React Status 是一份每周精选的 React 相关资讯通讯，涵盖 Hooks、编程模式、性能优化、React Native 以及整个生态系统，自 2016 年 8 月起已发布 486 期。它提供订阅、历史期数浏览及 RSS 订阅功能，并明确承诺重视隐私、反垃圾与 GDPR 合规政策。

- 📬 每周精选 React 生态中的重要资讯，人工筛选
- 🪝 关注 Hooks、开发模式、性能优化及 React Native 等核心主题
- 📊 自 2016 年 8 月已累计发布 486 期，持续更新
- 🔗 支持订阅最新一期、查看全部历史期数及 RSS 订阅
- 🛡️ 明确承诺遵守隐私、反垃圾邮件及 GDPR 政策，由专业团队发布

---

