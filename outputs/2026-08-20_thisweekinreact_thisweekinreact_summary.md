### [从 57 个 bug 到 1 个，感谢 Seer | Sentry 博客](https://blog.sentry.io/57-bugs-to-1/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=seer-fy27q3-evergreen&utm_content=newsletter-first-sponsor-dan-mindru-blog-learnmore)

**原文标题**: [From 57 bugs to 1, thanks to Seer | Sentry Blog](https://blog.sentry.io/57-bugs-to-1/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=seer-fy27q3-evergreen&utm_content=newsletter-first-sponsor-dan-mindru-blog-learnmore)

概述：文章介紹了 Sentry 的 Seer 如何結合 AI 代理，大幅降低修復 bug 的成本，並將作者的 bug 數從 57 個降到 1 個。作者將 bug 分為三類，並分別說明對應的自動化修復策略，同時強調「上下文」（traces、logs、Session Replays）對於 AI 修復的關鍵作用。

- 🦷 作者在牙醫診所意外收到一個自動產生的 PR，內容是合理的 bug 修復且測試全綠，按下 merge 後驚覺 AI 已能低成本自動修復程式碼。
- 💰 傳統 bug 排序因「修復成本 > 商業價值」而被無限期擱置，但 2026 年 AI 的智慧、上下文長度、工具呼叫能力與代理協作，徹底翻轉了修復的經濟效益。
- 📡 豐富的遙測上下文（Sentry 的 trace、裝置資訊、網路、logs、Session Replays）是 AI 修復的關鍵；沒有上下文，再強的 AI 也無從下手。
- 😊 Friendly bugs（單純、可重現、低風險）：設定 Seer「Stop after PR drafted」後，Sentry 會自動分析、產出修復 PR，作者只需確認並合併。
- 😠 Grumpy bugs（跨檔案、需深入調查）：由 Seer 做根因分析，再將修復交接給 Cursor / Claude Code / Copilot 等雲端代理，在真實環境中驗證並開 PR。
- 🤘 Punk bugs（依賴生產資料或第三方服務、難以重現）：透過 Sentry MCP 伺服器讓代理讀取生產上下文，並由人類補充歷史／商業邏輯，協同找出根因與修復方向。
- 🔐 仍有些 bug 成本過高或風險太大，例如 MSAL 認證到期導致資料遺失的 bug，最終只能以「每次輸入即儲存」的替代方案降低傷害。
- 🚀 多數 bug 如今已能以極低成本自動修復；即使複雜 bug 無法全自動，AI 也能大幅縮短調查與驗證時間，讓開發者更專注於真正重要的問題。

---

### [](https://oxc.rs/blog/2026-08-18-react-compiler-support)

**原文标题**: [React Compiler Support | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2026-08-18-react-compiler-support)

概述：Oxc 项目宣布在 Oxlint 和 Oxc Transform 中集成 React Compiler，提供 22 条基于编译器验证的规则和自动记忆化转换，性能远超 Babel，并计划与 Vite 插件集成。

- 🎉 宣布支持：Oxlint 新增 22 条 React Compiler 规则，用于捕获违反 React 规则的行为；`oxc-transform-react` 包实现自动记忆化，初步基准测试比 Babel 快 10 倍以上。
- ⚙️ Oxlint 使用：通过 `.oxlintrc.json` 启用 react 插件和 correctness 类别，规则分类与上游 ESLint 预设对齐；旧的 `react/react-compiler` 规则已被替代。
- 📦 Transform 使用：安装 `oxc-transform-react` 后，通过 `transformSync` API 配置 `reactCompiler` 和 `jsx` 选项即可完成转换。
- 🔌 Vite 集成：原生 `@vitejs/plugin-react` 集成等待 `vitejs/vite-plugin-react#1419` 合并，保持工具链中立。
- 🚀 性能优势：初步基准显示 `oxc-transform-react` 比 `babel-plugin-react-compiler` 快 10 倍以上，典型文件从约 100 ms 降至约 10 ms。
- 🧩 技术背景：React Compiler 最初是 Babel 插件，后移植到 Rust；Oxc 将其内嵌（vendored），直接运行在 Oxc AST 上，移除中间 Babel AST 和 JSON 往返。
- ⚡ 本地性能：Oxc 版本比原始 Rust 移植版快约 2 倍，同时减少内存分配。
- ✅ 一致性保障：与最新实验版 `babel-plugin-react-compiler` 输出一致，在超过 10 万个源文件的大型仓库中验证通过。
- 🔧 诊断改进：Oxlint 显示紧凑代码框架、相关源位置、帮助信息和文档链接，便于编码代理修复问题。
- 📉 二进制体积：从初始 8.66 MiB 降至 3.97 MiB（macOS ARM64），且 React Compiler 位于独立可选包，不影响 Oxc Transform 体积。
- 🗺️ 源码映射：修复了原始 Rust 移植版中不完整的源码映射支持，确保在 React Compiler、TypeScript、JSX 和 Fast Refresh 中正常工作。
- 🔭 未来工作：继续完善剩余 TODO（约 57 个集中式诊断构造器），修复 Babel 实现中的缺陷，欢迎反馈和贡献。
- 🙏 致谢：感谢 React Compiler 团队（特别是 Joseph Savona 和 Lauren Tan）的开源工作与支持。

---

### [](https://github.com/vitejs/vite-plugin-react/pull/1419)

**原文标题**: [feat(react): add native React Compiler support by Boshen · Pull Request #1419 · vitejs/vite-plugin-react · GitHub](https://github.com/vitejs/vite-plugin-react/pull/1419)

overview summary
该 PR 为 @vitejs/plugin-react 添加了原生 React Compiler 支持，通过可选依赖 oxc-transform-react 实现，将 TS/JSX、Fast Refresh 和 React Compiler 统一在一个转换流程中，同时避免增加 Rolldown 的复杂度。该功能已通过审查并合并，随后发布为 6.1.0。
- 🚀 为 @vitejs/plugin-react 添加原生 React Compiler 支持
- ⚙️ 新增 compiler 选项，基于 oxc-transform-react 包
- 🔄 启用后，一个 pass 即完成 React Compiler、TypeScript/JSX 与 Fast Refresh 转换
- 💻 React Compiler 与 Fast Refresh 仅客户端使用；服务端用同一包处理 TS/JSX
- 📦 独立包设计，避免给 Rolldown 增加框架特定编译器的体积与复杂度
- 👥 经过多位维护者审查与多轮修复，最终合并
- ✅ 已合并至 main，并标记为实验性
- 🎉 后续发布 plugin-react@6.1.0，多个项目跟进使用

---

### [发布 Biome CLI v2.5.8 · biomejs/biome · GitHub](https://github.com/biomejs/biome/releases/tag/%40biomejs%2Fbiome%402.5.8)

**原文标题**: [Release Biome CLI v2.5.8
 · biomejs/biome · GitHub](https://github.com/biomejs/biome/releases/tag/%40biomejs%2Fbiome%402.5.8)

Biome v2.5.8 发布了，本次更新聚焦于新增 lint 规则、性能优化和多种解析/格式化修复。新增了 React Compiler、Svelte 旧式常量、CSS @property 校验等规则，并将 HTML style 属性纳入 CSS 解析；同时修复了 Svelte、Vue 和 GritQL 相关的多个问题。

- 🆕 新增 useReactCompiler 规则，可报告 React Compiler lint 模式诊断。
- 🆕 新增 noSvelteLegacyConst 规则，禁止旧式 {@const}，推荐使用 $derived()。
- 🆕 新增 noInvalidPropertyInitValue 规则，校验 @property 的 initial-value 与 syntax 描述符是否匹配。
- ⚡ 优化 noImportCycles 和 noMisusedPromises 的性能。
- 🧩 HTML style 属性值现按 CSS 解析，所有 CSS lint 规则都会应用。
- 🐛 修复 useAwait、noUselessUndefined、noUselessFragments 等规则中的误报和崩溃。
- 🛠 修复 Svelte 中以对象字面量开头的表达式解析失败，Vue 内置实例属性（如 $slots、$event）不再误报。
- 🎨 修复 CSS 格式中块注释缩进和伪类/伪元素内注释位置的保留问题。

---

### [](https://github.com/biomejs/biome/issues/10974)

**原文标题**: [☂️ `useReactCompiler` remaining work · Issue #10974 · biomejs/biome · GitHub](https://github.com/biomejs/biome/issues/10974)

该议题追踪 Biome 中 `useReactCompiler` 规则的剩余工作，当前为 0/1 进度。它整理了上游失败的测试用例，并提出了预过滤、规则拆分及架构改进方向。

- 📋 总括问题：#10974 追踪 `useReactCompiler` 规则的剩余工作，目前 0/1 个子任务完成。
- ✅ 第一类失败用例：Biome 与 Babel 输出一致，是 OXC oracle 漏报，并非 Biome 缺陷（如 `error.bug-invariant-local-or-context-references.js` 等）。
- 🔧 第二类：React Compiler Rust 移植的已知前沿问题，如 `todo-round3_promote_used_temps.js` 中的 PromoteUsedTemporaries 分歧。
- ⚠️ 第三类：深度边界用例中 Biome 与 Babel/OXC 均报错但原因不同，例如默认参数访问局部变量、可选链 Hook、未闭合 eslint 抑制等。
- 🎯 需要解决预过滤启发式问题（参见 #10710 评论）。
- 🔀 考虑将规则拆分为多个独立规则。
- 🍴 需要 fork：移除脆弱的字符串比较诊断；跳过 Biome CST → Babel AST → HIR 转换，直接从 Biome CST 生成 HIR。

---

### [](https://github.com/oven-sh/bun/issues/24356#issuecomment-5276435139)

**原文标题**: [Support React Compiler w/ Bun's built-in bundler · Issue #24356 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/issues/24356#issuecomment-5276435139)

overview summary  
该 issue 请求在 Bun 内置打包器中支持 React Compiler。由于 React Compiler 已发布 v1.0，作者希望 Bun 能像其他打包器一样支持该插件，以便在 `bun build` 和 `Bun.build` 中使用。同时强调此请求与 Next.js/Turbopack 无关，并指出 React Compiler 会改变组件编写方式，因此切换构建工具影响较大。

- 📌 该 issue 是 bun 仓库的 #24356，标题为“Support React Compiler w/ Bun's built-in bundler”，当前状态为已关闭。  
- ⚛️ React Compiler 于 2025 年 10 月发布 v1.0，能显著提升速度并改变 React 代码编写方式（无需手动 memoize）。  
- 🎯 请求在 Bun 的 `bun build` CLI 和 `Bun.build` JS API 中支持 React Compiler，以替代 Vite 等打包器。  
- 🚫 作者明确表示此问题与 Next.js 或 Turbopack 无关，相关讨论请参见 issue #23554。  
- 🔄 如果 Bun 不支持，替代方案是继续使用 Vite、Webpack、Rollup 或其他打包器。  
- 🏷️ 该 issue 标记为 `bundler` 和 `enhancement`，无分配人员、无项目、无里程碑，也没有关联的 PR。

---

### [循环工程到底是什么？为什么大家都在讨论它？](https://posthog.com/newsletter/loops?utm_source=twir&utm_campaign=aug19)

**原文标题**: [WTF is loop engineering and why is everyone talking about it?](https://posthog.com/newsletter/loops?utm_source=twir&utm_campaign=aug19)

overview summary  
本文探讨了 AI 工程领域興起的「循環（loop）」概念：不是讓代理依提示寫程式，而是設計能自我提示、自主完成長期任務的循環系統。文中說明構成循環的四要素、當前熱潮的原因、與產品工程師的關聯，以及為何程式碼本身從不是重點。

- 🔁 循環的核心：代理不是被動等待提示，而是主動自我提示，執行長期任務並可同時使用多個代理加速進展。  
- 🎯 構成循環的四要素：明確目標、持續餵入的上下文（工具、資料、錯誤等）、代理自我驗證的評估機制，以及代理本身。  
- 👶 具體實例：PR 保母（讓 CI 變綠）、Bug 修復器（用測試與日誌驗證）、Flaky 測試獵人（連續綠跑）、效能自動研究員（擊敗基準，如修復三年舊 bug 並提升 11% 效能）。  
- ⏳ 為何現在爆紅：模型能處理更長任務（如 Opus 4.6 完成 12 小時任務的比率大增），Stripe 一天完成全碼庫遷移，且 Claude Code 已內建/loop 指令。  
- 🧩 子代理與工具成熟：主循環可派生子代理執行工作，配合壓縮、技能、MCP、雲端執行，讓循環更可靠且可放手。  
- 🚗 超越 AI 炒作：循環的終極目標是「自驅動產品」，代理自動收集資料、改進產品並評估成效，無需工程師逐步介入。  
- 👷 產品工程師早已手動完成此循環：透過分析、訪談用戶、迭代改進與評估，PostHog 等工具正將這流程自動化。  
- ⚖️ 限制與未來：循環不會消滅工程工作，而是將 1% 的小優化（bug、UX 問題、轉換微調）自動化，讓人專注更有策略性的任務。  
- 💡 程式碼從不是問題：工程師的價值在方向、品味與同理心，設計循環只是工作抽象層次的提升，而非取代。

---

### [](https://github.com/react/react/pull/37290)

**原文标题**: [[flags] Enable enableParallelTransitions by acdlite · Pull Request #37290 · react/react · GitHub](https://github.com/react/react/pull/37290)

这是 React 仓库中一个已合并的 PR 记录，核心内容是将 `enableParallelTransitions` 特性标志的默认值从关闭切换为开启，并对相关 fork 和测试渲染器进行同步，为后续版本发布做准备。

- ✨ 合并 PR #37290：反向撤销了 #35709，默认启用 `enableParallelTransitions`。
- 🔧 在 OSS/canary 默认配置及所有硬编码 fork（包括 React Native fork）中开启该标志，并保持测试渲染器同步。
- 🌐 不改变 www 渠道：仍由 GK（Gatekeeper）控制，`www.js` 与 `www-dynamic.js` 保持原样。
- 📌 标志本身仍保留在仓库中，本次只是把默认值改为开启。
- 📊 体积影响极小：`react-dom-client.production.js` 约增加 0.03%，gzip 约 +0.02%，其余包无显著变化。
- 💬 审阅者 eps1lon 询问为何不先走 `__EXPERIMENTAL__`；作者说明该功能已在 Meta 生产环境验证，下一步将部署到 Vercel 应用，目标进入 React 19.3，并可快速回退。
- ✅ eps1lon 批准，247 项检查通过后合并进 `react:main`。
- 🔁 合并后由自动机器人（DiffTrain）同步到其他分支/仓库，并触发了 Next.js 的升级 PR。

---

### [](https://github.com/TanStack/router/discussions/8087)

**原文标题**: [Maintainer review of anonrig/router performance, compatibility, and PR claims · TanStack/router · Discussion #8087 · GitHub](https://github.com/TanStack/router/discussions/8087)

tannerlinsley 对 anonrig/router 进行了公开审查，指出其最初“19 倍更快”和“drop-in 替代”的说法建立在不对等的基准测试上，且“TanStack 忽视工作”的说法与公开历史不符；项目后续虽有实质修正，但仍存在行为兼容性差距，不能作为补丁集直接合并。

- 🔍 审查覆盖公告版、首次修正版和最新版三个快照，并公开了技术结论、PR 历史和更正记录。
- 📊 原始 19.80x 结论可复现但无效：该基准反复调用已加载的服务端路由器，命中了特殊跳过 loader 的返回路径，比较的不是等价工作。
- ⚖️ 后续 14x 导航声明同样有问题：省略的 `staleTime` 被 fork 当作永久有效，导致 loader 调用被跳过；显式设为 0 后结果反转甚至落后。
- ✅ 作者 Yagiz 收到审查后快速修复了多项问题，包括移除误导性标题、修正基准、增加服务器请求隔离和回归测试。
- 🤝 公开记录显示 TanStack 并未无视这些贡献：有讨论、有合并、有替代 PR 且保留作者署名，还有作者自行关闭的 PR。
- 📆 公告中“超过两个月”的说法不准确：当时三个未合并的 PR 实际是 54 到 56 天，而且私信沟通也未被后续公开帖如实呈现。
- 🧩 最新版已修正 loader 计数差异，在同等 loader 调用数下，约 15–16x 的吞吐优势在小同步 loader 的 Node 场景可复现。
- 🚧 但“drop-in”需要行为兼容：公告版自带的复制测试套件有 197 个失败案例；最新版 163 个文件全部通过，但仍只是修改后的子集。
- ⚠️ 定向差异探针发现 fork 在 `loaderDeps` 变化、loader 上下文复用、同步/异步错误处理等方面与 TanStack 行为不同。
- 🗂️ 记忆历史的优化是有代价的：2,100 次 push 后 `go(-2100)` 无法回到起点，因为最早一半历史被主动丢弃。
- 🔧 该 fork 是独立实现而非可复制的补丁集；只有少量优化与上游 PR 重叠，其余需按 TanStack 架构逐项适配验证。
- 📣 维护者认可当前版本的改进，但仍要求 Yagiz 公开更正原始“19x”“drop-in”和 PR 时间线的不实描述。

---

### [](https://www.reddit.com/r/nextjs/comments/1vnlcsk/were_the_nextjs_team_ask_us_anything/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vnlcsk/were_the_nextjs_team_ask_us_anything/)

您没有提供需要总结的文本内容。请发送文章或段落，我会按照您要求的格式（顶部无标题概述，下方以“-”开头的表情符号要点列表）用中文为您生成总结。

---

### [React Router v9 · remix-run/react-router · 讨论 #15371 · GitHub](https://github.com/remix-run/react-router/discussions/15371)

**原文标题**: [React Router v9 · remix-run/react-router · Discussion #15371 · GitHub](https://github.com/remix-run/react-router/discussions/15371)

React Router v9 的 GitHub 提案讨论，由维护者 brophdawg11 发起，概述了 v9 的发布时间、设计原则、未来标记、新 API 与弃用计划，并收集社区反馈。v9 预计在 Node 22 EOL 后约 2027 年中发布，重点在于精简 API、简化迁移路径，并保持年度发布节奏。

- 🗓️ v9 预计于 2027 年中发布，v8 已于 2026 年 6 月发布，v9 将在 Node 22 EOL 之后推出。
- 🎯 设计原则强调“少即是多”，在保持能力的前提下减少 API 表面，并通过 future flags 和弃用警告简化升级。
- 🚩 未来标记 `unstable_enableNodeReadableStream` 正在等待社区反馈与指导委员会投票。
- 🔧 新 API 计划稳定 `useRoute` 和 `useRouterState`，以整合路由数据访问，可能替代部分现有 hooks。
- 🗑️ 弃用计划包括：最低 Node 版本升至 24、移除 `react-router reveal --no-typescript` 标志、弃用 View Transition APIs 以支持 React 原生组件。
- 🤔 仍在讨论是否提升 React/Vite 最低版本，以及是否进一步弃用声明式模式。
- 💬 社区提议增加 SPA 模式下的 prefetch、第一方客户端缓存、改进 fetcher 开发体验，但需评估是否符合 v9 范围。

---

### [](https://reactsummit.us/?utm_source=thisweekinreact)

**原文标题**: [React Summit US – The Biggest React Conference in the US](https://reactsummit.us/?utm_source=thisweekinreact)

React Summit US 2026 将在 2026 年 11 月重返纽约，以混合形式举行，集结全球 React、现代 Web 开发与 AI 领域开发者，包含线下主场、远程直播、免费工作坊及多场周边活动。

- 🗓️ 日期：2026 年 11 月 17 日（纽约线下 + 远程）与 11 月 20 日（纯远程），11 月 16 日可组合参加 JSNation US 与 AI Coding Summit。
- 📍 地点：纽约/新泽西 Liberty Science Center，拥有西半球最大天文馆，并有曼哈顿景观渡轮体验。
- 🎫 规模：2 大主题轨道、50+ 演讲者、全球 10,000+ 开发者参与，现场约 800 人。
- 🌐 形式：混合会议，Day 1 现场直播互动，Day 2 全线上，并配有免费远程工作坊。
- 🤖 重点内容：AI 辅助编程、AI 工程、全栈架构、技术领导力等深度专题，以及 React 19、Server Components、TypeScript、Next.js 等热门主题。
- 🛠️ 工作坊：覆盖 React 高级架构、Claude Code、Next.js 实战等，分免费与 PRO 两种类型。
- 🎤 知名讲者：Kent C. Dodds、David Khourshid、Mark Erikson、Brad Westfall、Maurice de Beijer 等众多行业专家。
- 💃 特色活动：西半球最大天文馆内的演讲、美国最大 React 派对、互动式远程技术讨论室。
- 🎟️ 门票方案：常规线下票 $990、三会组合票 $1575（含酒店 $2800）、远程早鸟票 $190、Multipass 订阅 $19/月起。
- 🎁 优惠机会：8 月 31 日前购混合票可免费获得 Claude Code 工作坊；分享个人徽章可争取免费远程票。
- 🏢 赞助与伙伴：多家铂金、黄金及技术伙伴支持，另有志愿者与赞助合作开放申请。

---

### [](https://julesblom.com/writing/hoistable-svg-defs-ii)

**原文标题**: [Hoistable SVG Defs, Take Two: Impersonating the DOM | JulesBlom.com](https://julesblom.com/writing/hoistable-svg-defs-ii)

overview summary
本文探讨了在 React 中优雅管理 SVG `<defs>` 去重与生命周期问题的新方案。作者先回顾了上一版基于 `useEffect` 注册表的缺陷，然后引入 React Aria Collections 的核心技巧：通过伪造一个“假的 DOM 节点”作为 portal 容器，让 react-dom 在 commit 阶段直接通知挂载/卸载，再配合 `useSyncExternalStore` 同步状态。最终实现无需 `useEffect`、无需手动注册的去重 `<defs>`，但依赖 React 未文档化的私有契约，存在版本兼容风险。

- 🎯 问题核心：SVG 的 `<marker>`、`<linearGradient>` 等 defs 元素需要全局唯一 id，但组件难以“拥有”自己依赖的定义，导致重复渲染与 id 冲突。
- 🔄 旧方案局限：上一版通过 `DefsProvider` + `DefsPortal` 把定义汇集到单个 `<defs>`，用 state 里的 Map 注册表去重，但依赖 `useEffect` 的 setup/cleanup 来模拟挂载状态，违背 React 数据流直觉。
- 💡 新思路来源：React Aria 的 Collections 组件面临“父组件需感知子组件”的问题，其解法是“渲染到伪造的 document 对象”，让 reconciler 直接告诉父组件所有挂载/卸载事件。
- 📦 伪造 DOM 的技巧：实现一个普通 JS 类，包含 `nodeType`、`createElement`、`appendChild`、`removeChild` 等方法，足以骗过 react-dom。用 `createPortal(children, fakeContainer)` 将 JSX 渲染进这个假容器，commit 时 react-dom 自动调用这些方法。
- 🔑 传递真实 props：为避免 react-dom 将 props 字符串化，只给 portal 元素传 ref，ref 回调在 commit 阶段直接把 `{id, children}` 挂到伪元素上，绕过属性管道。
- ⚛️ 状态同步：伪造容器兼作 external store，通过 `useSyncExternalStore` 订阅其变化；`Defs` 组件重新渲染时按文档顺序去重（首个 id 胜出），并真正渲染到 `<defs>` 中。
- ✅ 相比旧方案的改进：完全移除 `useEffect` 注册表；无需 `useId` 生成实例 ID；初始渲染不再出现重复定义；挂载/卸载完全由 reconciler 驱动。
- ⚠️ 潜在风险：react-dom 对 portal 容器要求的方法集合是私有契约，未记录，React 版本升级可能破坏功能；另外每次变更需要两次渲染（先写假容器，再写真实 DOM），但第一次渲染极廉价。
- 🧩 总体评价：方法依然奇特，且代码量不少，但比上一版“逆着 React 潮流”的注册表方式更优雅、更符合 React 内部机制。

---

### [](https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs)

**原文标题**: [How we migrated lovable.dev away from Next.js and turned it into another Lovable app | Lovable](https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs)

overview summary  
本文详细介绍了 lovable.dev 从 Next.js/Vercel 迁移到自家 TanStack Start 平台的完整过程。团队采用渐进式双框架并行策略，结合 AI 代理辅助编码，在保持业务持续迭代的同时完成了大规模迁移，最终实现了 dogfooding、性能提升和统一技术栈的目标。

- 🏠 背景与规模：lovable.dev 拥有 42M+ 月独立访客、近 400 条路由、910K+ 行非生成代码，迁移后与普通用户应用一样托管在 Lovable 平台上，仅需不到 200 行特殊代码。
- 🐶 核心动机：通过 dogfooding 切身体验用户痛点，缩短反馈闭环；同时推动单个应用的大规模扩展能力，并将最佳实践反哺给 builder agent。
- 🔀 渐进式迁移：放弃 big-bang 重写，采用 proxy worker 在 Next.js 与 TanStack Start 之间按路由和用户分发请求，实现逐路线平滑迁移。
- 🧩 共享代码架构：通过 `#shared` 别名和 lint 规则强制共享代码框架无关，最终 90-95% 代码为框架无关，Next.js 特定代码仅占 3%。
- 🤖 AI 辅助迁移：开发者构建 agent skills 和规划循环，以可量化指标驱动，自动生成迁移 PR、审查兼容性，单人即可完成原本需要多团队协调的工作。
- 🚦 流量切换策略：按路由组进行多阶段 A/B  rollout（内部 → 1% → 100%），同一时间只推进一个外部 rollout，整体耗时约两个月。
- 💥 OOM 事故警示：dashboard 组 rollout 曾引发内存超限，根因是静态 JSON 在模块级解析导致 isolate 内存飙升；通过延迟解析、精简字段、服务端 stub 等优化后问题解决。
- ⚖️ 框架对比体验：TanStack Start 启动更快（10s vs 70s）、内存占用更低（1.5GB vs 8GB），抽象更直观，AI 代理出错更少；但复杂应用需要大量自定义打包配置。
- 📈 实际收益：中位 TTFB 降低 49%，CI 构建从 12+ 分钟缩短至 6-9 分钟，支持用 Lovable 自编辑 lovable.dev，非技术员工也能参与改进。
- 🔮 未来展望：团队计划利用沙箱能力让用户导入和编辑任意现有软件（包括 Next.js 应用），进一步扩展 Lovable 的适用范围。

---

### [](https://nextjs.org/blog/making-v0-navigations-instant)

**原文标题**: [Making Navigations Instant in v0 | Next.js](https://nextjs.org/blog/making-v0-navigations-instant)

overview summary
- ⚡ Next.js 16.3 推出新机制，让动态应用也能实现即时页面导航，无需将数据获取或渲染代码移至客户端。
- 🧩 动态内容可在用户浏览时被预渲染并缓存于浏览器中，通过 Suspense 或 'use cache' 实现部分预渲染，兼顾个性化与速度。
- 🧪 新增 `instant()` Playwright 测试助手，可断言导航中哪些 UI 即时可见且无网络请求，将“快”这一模糊目标变为可验证的确定性测试。
- 🤖 v0 团队使用代理循环：为每条慢导航编写失败测试 → 应用修复 → 重新运行直至通过，最终 16 个新测试进入 CI 防止回归。
- 🔧 常见修复只需将动态数据访问移到 Suspense 边界之下，少数情况需更大重构（如移除根布局中的阻塞依赖）。
- 📦 提供两个 Skill：`next-cache-components-optimizer` 用于优化现有 Cache Components 应用，`next-cache-components-adoption` 用于迁移旧应用。
- 🏗️ 框架在代理时代仍至关重要：`instant()` 这类深度集成框架的验证器，能将模糊的 UX 体验转化为确定性测试，引导代理生成更优质的 UI。

---

### [](https://tkdodo.eu/blog/reliable-query-prefetching-with-tanstack-router)

**原文标题**: [Reliable Query Prefetching with TanStack Router](https://tkdodo.eu/blog/reliable-query-prefetching-with-tanstack-router)

本文探讨了在 TanStack Router 中结合 TanStack Query 实现可靠查询预取的方法，指出常见的数据重复加载问题，并提出通过路由上下文共享 queryOptions 来根治。

- 📌 推荐在 route loader 中尽早触发查询，组件用 `useSuspenseQuery` 接手 promise，避免组件自行请求带来的延迟与瀑布流。
- ⚠️ 但该模式要求组件查询与 loader 预取保持 100% 同步，应用变大后极易因遗漏而逐渐“分叉”。
- 🔍 示例：新增 `asOf` 搜索参数后，若 loader 未同步，会先预取“今天”数据，再在组件里重新请求快照数据，造成多余请求和二次挂起。
- 🛠️ 修复第一步：用 `loaderDeps` 让 loader 感知相关查询参数，但这只是缓解症状，重复定义问题仍在。
- 🧩 根本方案：使用新的 `context` 函数把 `queryOptions` 放入 Route Context，loader 与组件都从同一上下文读取，彻底消除重复与漂移。
- 🔄 该模式还能利用上下文继承，让子路由复用父级预取的 `queryOptions`，例如根路由预取用户数据，任意子组件可直接消费。
- ⚡ `context` 只在 `params` 或 `loaderDeps` 变化时执行，不会因无关搜索参数变化触发组件不必要的重渲染。
- ✅ 最终结论：这是确保组件消费内容与 loader 预取内容始终一致的最佳可扩展方案，尤其适合大型应用。

---

### [](https://tanstack.com/blog/tanstack-router-navigation-lanes)

**原文标题**: [Inside a TanStack Router Navigation | TanStack Blog](https://tanstack.com/blog/tanstack-router-navigation-lanes)

导航调用在应用代码中看似一行 `await router.navigate({ to: '/account' })`，但 TanStack Router 内部实际上由四个独立生命周期协同完成：当前事务（transaction）、私有路线分支（lane）、加载器飞行（loader flight）和框架渲染回执（render receipt）。本文通过一个包含预加载、并发点击、错误、重定向和缓存的多重重叠场景，解释了为什么必须分离“取消/取代/发布/渲染”这四个概念，以及它们如何共同决定一次导航的最终结果。

- 🧭 一个 `navigate()` 调用背后可能同时发生：悬停预加载、点击复用加载、用户中途切换路由、某个 loader 出错、另一个 loader 重定向、旧加载结果仍被缓存、框架延迟渲染等复杂重叠事件。
- 🔀 路由器必须独立回答四个问题：哪些加载工作应继续？哪个导航可以发布？路线尝试最终得出什么结果？框架是否真的渲染了发布内容？
- 🏛️ 这四个答案分别由“当前事务”（transaction）、“私有路线分支”（lane）、“加载器飞行”（loader flight）和“框架渲染回执”（render receipt）管理，避免把所有状态压缩进少数变量而导致各类 bug。
- 🛤️ lane 是路由匹配后生成的私有未发布草稿：按父到子顺序串行执行 `beforeLoad`，然后并行运行所有符合条件的 loader。
- ⏱️ 如果 loader 超过 `pendingMs`，路由器可以先发布 pending UI，但 lane 仍会继续工作以产出最终结果；最终发布后导航才算完成。
- 🎟️ current transaction 是一个单槽位，持有当前允许发布到页面的导航；当新导航（如 `/settings`）占据该槽位，旧 lane 就失去发布权，即使它的部分工作（如 `/account` 的加载）仍然有用。
- 🔗 loader flight 封装了一次加载器调用：包含 promise、abort controller 和 lease（租约）计数。每个需要该结果的消费者（如预加载或导航）持有一个租约，只有最后一个租约释放后加载才可能被中止。
- 🧩 多个 loader 的独立结果（成功、错误、重定向）并不会直接决定路线结果；lane 会等待已启动的 loader 全部落定，再归约为一个语义结果——重定向启动新导航、错误选择错误边界、成功则允许完整 lane 发布。
- 🔄 重定向属于控制流而非 UI 结果：它会丢弃当前 `/settings` lane 并启动到 `/login` 的新导航，因此 `/settings` 的错误永远不会出现在页面上。
- 📤 发布（publish）只是把路线分支交给框架请求渲染，并不等于渲染完成；React 可能因旧树忙碌、suspense 或懒加载而延迟提交，甚至被下一次发布直接取代。
- 📋 render receipt 跟踪每一次精确发布：新发布会对旧发布回执 `ack: false`，若框架成功提交则 `ack: true`。只有 `ack: true` 才证明框架真正渲染了该发布。
- ✅ `ack: true` 时导航解析并触发后续生命周期；`ack: false` 不代表导航失败，只表示该发布在提交前被替换。被取代的公开 `navigate()` 仍可链接到替代它的导航，因此两个回执答案都会释放内部等待。
- 🧠 通过将租约、事务、lane 和回执分离，`navigate()` 依然对外呈现为一个 promise，同时路由器能够正确处理预加载共享、并发导航、缓存保留、重定向优先和渲染竞态等复杂场景。

---

### [](https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3)

**原文标题**: [Building App-like Experiences with Next.js 16.3 | Next.js](https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3)

overview summary
- ⚡ Next.js 16.3 推出「即時導航」，結合 Cache Components 與 Partial Prefetching，在保留 Server Components 優勢的同時，提供可媲美單頁應用程式的流暢點擊體驗。
- 🎵 示範應用包含音樂播放器 Next Beats、社群動態 Drop、日曆 Flow 與團隊聊天 Huddle，展示各項功能如何整合。
- 🧩 Cache Components 透過 `'use cache'` 與 `cacheLife` 讓資料跨導航重複使用，重訪頁面時可跳過載入畫面；`cacheTag` 搭配 `updateTag` 可在資料變更後即時失效重取。
- 🔗 Partial Prefetching 在點擊前預先取得可見 `<Link>` 的 App Shell；對特定連結加上 `prefetch={true}` 可連同 URL 相關內容一併預取，讓商品或詳細頁幾乎立即顯示。
- 🖱️ Client Components 負責互動狀態與事件處理，搭配 Context Provider 放在共用佈局中，可讓播放控制等介面跨路由持續同步，同時其 children 仍保持伺服器渲染。
- 🔄 透過 `useTransition`、`useOptimistic` 與 Server Actions，可在網路延遲下立即呈現樂觀更新，失敗時自動回滾並顯示錯誤提示。
- 📡 離線重試功能（`experimental.useOffline`）可讓軟導航、RSC 請求、Prefetch 或 Server Action 在連線中斷時暫停並自動重試，但目前僅供實驗且不建議用於生產。
- ⏳ Suspense 邊界可控制串流內容的顯示順序；巢狀邊界能使頁面由上而下穩定呈現，避免內容載入後互相推擠造成版位跳動。
- 📥 用戶端資料擷取可搭配 SWR 或 React Query：由 Server Component 預先載入資料並透過 SWRConfig/HydrationBoundary 傳遞，再由瀏覽器接手輪詢、重新驗證與樂觀更新。
- 🎞️ React 的 `<ViewTransition>` 可用於淡入串流內容、清單項目位置變動的 morph 動畫，以及支援前後導航方向感的頁面轉場，讓介面變化更容易追蹤。
- 🧪 示範應用皆附 Playwright 端對端測試，利用 `instant()` helper 將斷言範圍限制在預取 UI 上，方便驗證即時導航行為。
- 💬 官方邀請社群透過 GitHub Discussions、Issues 與 Discord 提供回饋，共同塑造 Next.js 的未來發展。

---

### [](https://aurorascharff.no/posts/coordinating-optimistic-updates-in-nextjs/)

**原文标题**: [Coordinating Optimistic Updates in Next.js | Aurora Scharff](https://aurorascharff.no/posts/coordinating-optimistic-updates-in-nextjs/)

这篇文章介绍了在 Next.js 应用中协调乐观更新的模式，重点是如何结合 React 的 useActionState 与 useOptimistic 处理重叠的用户写入操作，确保界面即时响应并按顺序保存数据。

- 🔄 核心模式：组合 useActionState 与 useOptimistic，实现乐观更新与有序请求队列，解决交互重叠时的写入竞争。
- ⏳ useActionState 作为异步 reducer，自动排队后续 action，并等待前一次保存完成后再继续执行。
- ✨ useOptimistic 在 action 尚未完成时临时呈现新状态，提升界面响应速度，避免用户等待。
- 🧩 使用纯 reducer 函数（如 channelLayoutReducer）从“当前状态 + 变更”计算下一状态，同时用于乐观 UI 和实际写入。
- 🚀 在 Huddle 示例中，通过 startTransition 包裹 dispatch，频道拖拽后立即移动，同时布局变更按序保存。
- ❌ 保存失败时捕获错误并返回上一次已确认的 state，useOptimistic 自动回滚临时 UI，无需额外反向操作。
- 📆 在 Flow 示例中，使用 EventChange 描述创建、更新、删除、移动和调整事件，由单一 Server Function 分派处理。
- 👥 利用 Context（CalendarEventsProvider）共享 pendingChanges 列表，让月视图、周视图及弹窗组件都能读取相同的乐观状态。
- 🎯 自定义 useOptimisticEvents hook，将 pendingChanges 叠加到各 Server Component 传入的 events 上，避免把整个日历树变成单个客户端组件。
- 🔁 事件写入失败时，服务器数据不变，UI 在 action 结束后自动回到已确认状态，同时通过 toast 展示错误。
- 📚 对于需要轮询、跨组件频繁同步或客户端缓存的数据（如消息），建议使用 SWR 或 TanStack Query 等客户端数据库。
- 📝 该模式让 Server Components 继续作为数据源，只补充必要的客户端状态协调，轻量且适用于大多数交互场景。

---

### [](https://next-intl.dev/blog/nextjs-root-params)

**原文标题**: [Using next/root-params in Next.js 16.3 – Internationalization (i18n) for Next.js](https://next-intl.dev/blog/nextjs-root-params)

Next.js 16.3 引入 `next/root-params` API，让深层 Server Components 能直接读取根布局的动态段值（如 `[locale]`）。这一特性填补了国际化场景的关键缺口，使 next-intl 可原生支持静态渲染、简化代码并减少变通方案。同时，根布局的定义更灵活，支持多个根布局与自定义路由，但当前不适用于 Route Handlers 和 Server Actions。

- 📌 Next.js 16.3 新增 `next/root-params`，允许深层 Server Components 读取根布局的动态段（如 `[locale]`）参数。
- 🎯 对 next-intl 至关重要：无需 `setRequestLocale` 即可支持静态渲染，并更紧密集成 Next.js 缓存机制（如 `cacheComponents`）。
- 🏗️ 根布局概念扩展：任何没有上层布局的布局都算根布局，可位于 `app/[locale]/layout.tsx` 等动态段中。
- 🔀 通过路由组可实现多个根布局，`next/root-params` 返回值取决于组件渲染位置；共享代码可提供回退值（如默认 `'en'`）。
- ⚙️ 静态渲染需配合 `generateStaticParams`，但注意 `dynamicParams = false` 与缓存组件不兼容，建议用运行时校验和 `notFound()` 守卫未知 locale。
- 🔧 next-intl 集成极简：只需在 `i18n/request.ts` 中读取并验证 `rootParams.locale()`，即可全局生效。
- ⚠️ 当前限制：`next/root-params` 不适用于 Route Handlers 和 Server Actions，可通过显式传递 `locale` 参数（如 `bind`）绕过。
- 🧹 可简化代码：移除 pass-through 根布局（改用 `global-not-found`）、不再手动读取 `params`、移除手动 locale 覆盖和 `setRequestLocale`。
- 🛠️ 支持自定义路由（如 `[tenant]`），能结合 next-intl 核心功能实现更复杂的国际化场景。

---

### [](https://trustedrouter.com/openai-compatible-llm-api?utm_source=thisweekinreact&utm_medium=sponsored_newsletter&utm_campaign=react_link_20260819&utm_content=react_link_every_model)

**原文标题**: [OpenAI-Compatible LLM API Router | TrustedRouter](https://trustedrouter.com/openai-compatible-llm-api?utm_source=thisweekinreact&utm_medium=sponsored_newsletter&utm_campaign=react_link_20260819&utm_content=react_link_every_model)

overview summary
TrustedRouter 是一个与 OpenAI 兼容的 LLM API 路由器，允许用户仅更换 `base_url` 即可通过同一接口调用数百种模型，无需更换 SDK 或绑定信用卡。它强调隐私（零日志）、实测性能数据、策略感知路由和可验证的网关安全性。

- 🔑 保持 OpenAI SDK，只需将 `base_url` 改为 `https://api.trustedrouter.com/v1`，创建密钥即可开始调用。
- 🌐 一个 API 入口可访问数百个模型和路由，支持 `trustedrouter/cheap` 等别名，也可指定具体提供商。
- 🚫 无需信用卡即可创建 API 密钥并发出首个请求，默认不记录提示词或输出日志。
- 📊 基于实时 TTFT、TTFB、吞吐量和可用性数据衡量提供商表现，而非依赖供应商宣传。
- 🛡️ 支持策略感知路由，可比较 ZDR、机密计算、提供商 E2EE 以及上游策略来源。
- 🔍 网关可验证，公开运行镜像、源码提交、摘要和 attestation 路径。
- 📋 实时目录展示当前路由、价格、隐私属性和实测性能，快照时间戳为 2026-08-20T01:04:17.127Z。
- 🧩 提供 494 个公开模型、51 个提供商、1515 条配置路由，以及 299 条 ZDR 路由和 32 条 E2EE 路由。
- ⚡ 示例模型包括 Claude Opus 4.8、GPT-5.5、Gemini 3.5 Flash、Kimi K2.7 Code、GLM 5.2、MiniMax M3 等，显示价格、上下文长度和实测速度。
- 📈 支持按提供商浏览全部模型，查看完整排行榜，并审查各提供商的政策说明。
- ❓ 常见问题确认：可继续使用 OpenAI SDK，也可通过显式模型 ID、提供商过滤器或别名（如 `trustedrouter/auto`、`trustedrouter/zdr`）选择精确提供商。

---

### [用于 TSRX 的 OXC](https://compiled.run/oxc-tsrx)

**原文标题**: [OXC for TSRX](https://compiled.run/oxc-tsrx)

OXC for TSRX 是一个独立社区项目，旨在让 `.tsrx` 文件在 OXC 和 Vite+ 工具链中获得与 `.tsx` 同等的原生 lint 与格式化支持，并强调极致的性能、基于 OXC 的真实实现、编辑器集成以及最终上游到 OXC 的目标。

- 🚀 提供 `oxc-tsrx` 工具，一条安装命令即可让 `.tsrx` 文件像 `.tsx` 一样被 lint 和格式化，集成 OXC 与 Vite+ 工具链。
- ⚡ 性能领先：同一 1000 个 TSX 文件，ESLint + typescript-eslint 耗时 648ms，官方 Oxlint 42ms，Oxlint + TSRX 49ms，混合 `.tsx` 和 `.tsrx` 文件为 71ms。
- 📊 设有严格的发布门禁：普通文件性能与 OXC 包装路径持平（门禁 ≤1.05×），顺序格式化 122 MiB/s，冷启动 4.8ms，原生编辑器诊断 0.13ms，读取 TSRX 源码 215 MiB/s。
- 🧩 基于 OXC 构建而非复制：所有 OXC 调用集中在单一小型适配器 crate，并提供官方 `oxc-parser` 同款 API，额外支持 `.tsrx` 解析，适用于 codemods、bundler 插件等。
- 🔍 诊断与格式化准确：真实 OXC 规则运行于内存中的临时 TSX 副本，但结果锚定回原始 `.tsrx` 源码；格式化会先转换、再重解析比较，确保落盘前无误。
- 🛠️ 编辑器天然支持：官方 OXC VS Code 扩展可识别 `oxc-tsrx` 安装的项目本地 `oxlint`，提供 `.tsrx` 实时诊断、格式化和经校验的快速修复。
- 🎯 终极目标是上游到 OXC：作为独立社区项目，语言核心保持小巧、隔离并受基准测试约束，便于 OXC 维护者审查；不声称获得 OXC 维护者背书。
- 📄 项目独立且开源：不隶属于 VoidZero 或 OXC 团队，MIT 许可证，固定 OXC 版本为 8e0ed2ebb961，基准报告日期 2026-07-29。

---

### [](https://gtkx.dev/blog/gtkx-1-0)

**原文标题**: [GTKX 1.0: The React framework for Linux | GTKX](https://gtkx.dev/blog/gtkx-1-0)

GTKX 1.0 正式发布，这是一个面向 Linux 的 React 框架，在成熟的 GTK4 API 之上提供了声明式 UI 层。它让开发者用 JSX 编写界面，并与 React 生态无缝集成，同时保留了 GTK 的原生体验，为 Linux 桌面开发带来现代化的开发流程。

- 🚀 GTKX 1.0 发布：Linux 专属的 React 框架，在 GTK4 之上提供声明式层，通过 JSX 创建 GObject 实例，无需浏览器即可开发桌面应用。
- ⚛️ 完整支持 React 19：hooks、context、Suspense、portal 和 React Compiler 均按标准行为工作；应用是普通 Node.js 进程，可直接使用 npm 生态和 Node API。
- 🏗️ 代码生成机制：CLI 读取系统安装的 .gir 文件，生成本地化的 @gtkx/gi 和 @gtkx/jsx 包，覆盖完整 GTK 组件、枚举和函数，无需发布到 npm。
- 🧩 一切皆元素：所有 GObject 都能以 JSX 形式使用，属性映射为 props；复杂 API 通过行为（behaviors）扩展，支持自定义 prop 声明。
- 📊 性能优化：ListView、ColumnView 等集合视图支持大数据量渲染，通过原生 cell recycling 保持流畅，同时将状态管理保留在 React 中。
- 🧪 测试友好：@gtkx/testing 查询无障碍树，userEvent 模拟真实用户交互；每个测试运行在独立 headless Wayland compositor 中，避免共享状态干扰。
- ⚡ 开发体验：快速刷新（Fast Refresh）、打包构建、资源编译（glib-compile-resources）、类型安全的 GSettings 绑定，以及文档生成和 MCP 服务器支持。
- 🛡️ 1.0 稳定性承诺：生成元素、配置文件和核心 API 已冻结，1.x 版本不会引入破坏性变更；v0 迁移路径清晰，主要涉及导入路径和挂载方式调整。
- 🔮 未来路线图：计划推出 gtkx deploy（Flatpak/DEB/RPM 发布）、动画库、导航和表单解决方案，社区可通过 issue tracker 影响优先级。

---

### [](https://github.com/unjs/unhead/releases/tag/v3.3.0)

**原文标题**: [Release v3.3.0 · unjs/unhead · GitHub](https://github.com/unjs/unhead/releases/tag/v3.3.0)

这是 unhead v3.3.0 的发布说明，引入破坏性变更（oxc-parser 改为可选 peer 依赖），并带来多项新功能、错误修复与性能优化，覆盖 bundler、React、schema-org、验证及核心 unhead 模块。

- ⚠️ 破坏性变更：`@unhead/bundler` 不再自动提供 `oxc-parser`，使用非 Rolldown 构建时需手动安装（`pnpm add -D oxc-parser`）
- 🚀 新功能：支持为 Vite 目标转译静态内联脚本；验证时对废弃 Twitter 元数据发出警告
- 🐞 修复：压缩声明性 JSON 脚本内容、兼容无 `Object.hasOwn` 的浏览器、保留数字零 head 内容
- ⚛️ React 修复：支持 Fragment 子元素、保留 Helmet 默认标题回退、规范化 Head JSX 属性、标准化 provider 实例属性、支持原始内容
- 🔍 schema-org：改进 Google 丰富结果一致性、补充缺失字段、在节点类型缺失时应用默认值
- 🛠️ 脚本与类型：脚本加载期间保持稳定代理、支持文档推测规则、收窄 `unpackMeta` 返回类型
- 🧹 unhead 核心：渲染新鲜的服务端 head 到 DOM、去重标量 Open Graph 与 Twitter 元数据
- ⚠️ 验证改进：警告过多 prefetch、验证 head 输入形状；vue 拒绝被忽略的服务器属性解析器
- 🏎️ 性能：使 Vite DevTools 套件可选、复用可用的 Rolldown 解析器
- 👥 贡献者：由 harlan-zw 和 danielroe 完成，共 26 个提交

---

### [发布](https://github.com/facebook/astryx/releases)

**原文标题**: [Releases · facebook/astryx · GitHub](https://github.com/facebook/astryx/releases)

overview summary  
该文本是 facebook/astryx 设计系统在 GitHub 上的发布说明，记录了 v0.4.5 至 v0.1.8 多个版本的更新，涵盖新组件上线、功能增强、国际化与可访问性改进、破坏性变更及大量修复。

- 🚀 v0.4.5：新增 BottomSheet 的 snapPoints 拖拽停靠功能；语言包扩展至 30 种；DateRangeInput 支持范围跨度限制；FormLayout 支持默认可选性；修复 iOS 拖拽问题与状态点形状区分。
- 🎁 v0.4.4：BottomSheet 正式进入 Core；新增 CDN 无构建模板；defineTheme 支持亮/暗色元组；修复多个手势与 IME 合成输入问题。
- ✨ v0.4.3：新增字符统计/截断工具；ComplexSelector 增强；useContainerReveal 支持悬停延迟；修复 Banner 焦点丢失、主题继承损坏及 Markdown 安全漏洞。
- 🔧 v0.4.2：AvatarGroup 溢出主题化；ChatMessageBubble 支持宽度属性；新增主题模板命令；修复 Avatar 主题目标与焦点陷阱问题。
- 🛠️ v0.4.1：焦点环改为主题令牌；多个组件支持 React Server Components；Selector 指示器位置可选；修复 TimeInput 播报与 Banner 图标主题等。
- ⚠️ v0.4.0：破坏性变更（DropdownMenu 类型重命名、useTableRowExpansion 迁移为树形插件）；新增 Avatar 回退主题、CodeBlock 复制按钮、useClipboard Hook 等。
- 🔄 v0.3.0：破坏性变更（RadioGroup 必需 label、authoring 迁移至 CLI）；新增 Carousel 循环、Dialog 逻辑位置、Pagination 输入变体、Markdown 主题目标等。
- 🌐 v0.2.0：新增 Avatar 交互、DropdownMenu 子菜单、RTL API、statusVariant tooltip；移除 TabList 中误导性的 orientation 属性。
- 📦 v0.1.9：补丁版；新增 Avatar 提示、Breadcrumb 菜单、DateInput format、elevation 属性、Table 行状态插件等。
- 🧩 v0.1.8：破坏性变更（Avatar 尺寸重命名）；新增 Collapsible 禁用、DropdownMenu 选择项、Outline 键盘导航、Table 树形数据插件。

---

### [错误](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.85.0)

**原文标题**: [Error](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.85.0)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /react-hook-form/react-hook-form/releases/tag/v7.85.0 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [](https://ui.shadcn.com/docs/changelog/2026-08-questionnaire)

**原文标题**: [August 2026 - Questionnaire - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-08-questionnaire)

该文本是 shadcn/ui 发布的新组件「Questionnaire」介绍，用于构建多步骤问题流程，支持多种答案类型、校验、键盘操作与 UI 组合，并可在多个组件库及无头原语中使用。

- 📋 新增 Questionnaire 组件，适用于多步骤问题流程（如代理澄清、用户引导、调查、表单填写与配置）。
- 🔧 兼容 Base UI、React Aria 和 Radix，提供全部八种样式变体。
- ☑️ 支持单选、多选、自由文本答案，以及可跳过的可选问题。
- 🎛️ 内置上一步、下一步、提交和自定义进度控件，支持受控导航、默认值与条件问题。
- ⌨️ 提供键盘导航，可选字母或数字快捷键，并支持原生表单序列化。
- 🧩 可独立使用，也可作为 Card 或 Dialog 组合布局。
- 📦 安装命令为 `pnpm dlx shadcn@latest add questionnaire`。
- 🎨 另外在 `@shadcn/react` 中提供无样式的 headless 原语 `<Questionnaire />`。

---

### [介绍 Fig - Ben Gubler](https://www.bengubler.com/posts/2026-08-14-introducing-fig-ui-runtime)

**原文标题**: [Introducing Fig - Ben Gubler](https://www.bengubler.com/posts/2026-08-14-introducing-fig-ui-runtime)

overview summary
- 🚀 Fig 是一个基于 React Fiber 的轻量级 TypeScript UI 运行时，体积约为 React 的一半，支持完整的 fiber 并发渲染。
- 💡 核心理念是重新实现 React 的精华，同时采用更贴近平台的语义（如 AbortSignal）并简化 API。
- 🧩 组件仅支持函数式，使用原生 HTML 属性名（如 class 而非 className），并提供 mixin 机制复用 props 和事件。
- 🔄 用 useReactive 替代 useEffect，效果接收 AbortSignal 来自动取消过期请求；生命周期钩子改名以避免混淆。
- 🖱️ 事件处理器基于原生浏览器事件，通过 mixin 绑定，并同样支持 AbortSignal 中断。
- 📌 DOM 访问使用 bind 替代 ref/forwardRef，更简洁直接。
- ⏳ Suspense 支持 readPromise/readData 触发，Context 自带 Provider，无需 .Provider 包裹。
- 📊 内置键控数据资源（dataResource），支持 Suspense、刷新时保留旧数据显示，方便库作者。
- 🖥️ 服务器组件被当作可流式传输的“Payload”数据，无需元框架即可使用；结合 TanStack 可无缝集成。
- 🎨 支持资源资产声明（CSS、预连接）的自动去重与提升，以及原生 View Transitions（需显式启用）。
- 📦 其余 API（useState、useMemo、createElement、Suspense 等）与 React 基本一致，并有 TanStack Router/Start 适配器。
- 🧪 已在作者个人网站投入使用，鼓励用户尝试用 LLM 重写迁移，对比包体积和性能。

---

### [](https://github.com/rshono/rshono)

**原文标题**: [GitHub - rshono/rshono: Minimalist web framework based on Hono, Rspack and React Server Components · GitHub](https://github.com/rshono/rshono)

overview summary：Rshono 是一个基于 Hono、Rspack 和 React Server Components 的极简 Web 框架，提供脚手架命令快速创建应用，并包含核心包、创建工具、基准测试网站与测试应用等模块。项目采用 MIT 许可，目前在 GitHub 上拥有 62 颗星。

- 🚀 极简 Web 框架，整合 Hono、Rspack 与 React Server Components
- ⚡ 使用 `npx @rshono/create@latest my-app` 快速初始化项目
- 📦 核心包 `packages/core` 提供框架主体功能
- 🛠️ `packages/create` 为项目脚手架工具
- 📊 `packages/benchmarks` 对比 Rshono、Next.js 与 TanStack Start 的性能
- 🌐 `apps/website` 官方网站与文档，自身即用 Rshono 构建
- 🧪 `apps/testbed` 用于测试框架功能的示例应用
- 🔒 提供贡献指南、安全策略与变更日志
- 📜 采用 MIT 许可证发布
- ⭐ 仓库现有 62 颗星、3 个 fork，并拥有 1 个 issue 和 6 个 pull request

---

### [发布 v2.](https://github.com/huozhi/sugar-high/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · huozhi/sugar-high · GitHub](https://github.com/huozhi/sugar-high/releases/tag/v2.0.0)

Sugar High v2.0.0 是一次重大更新，从仅面向 JavaScript 的高亮器发展为一个小巧可组合的高亮工具包。默认 API 保持简单易用，同时新增的核心 API 支持编辑器、渲染器、Remark 插件和自定义语言组合。本次发布包含 25 种规范内置语言、第一方 React 组件与 Remark 插件，并带来若干破坏性变更和性能提升。

- 🎉 发布 v2.0.0：从 JavaScript 高亮器升级为可组合高亮工具包，默认 API 不变，新增核心 API 支持多种集成场景。
- 🗂️ 25 种规范内置语言：相关方言统一而非重复，涵盖 JS/TS/JSON/Shell/HCL 等，并支持扩展语言。
- 📦 安装包：提供 sugar-high@2、@sugar-high/react@1 和 @sugar-high/remark@1 三个 npm 包。
- ⚡ 默认 highlight() API：支持 highlight(source)、指定语言（如 python、diff），以及通过 cx、mark、markLine 自定义 token 与行样式。
- 🔤 语言共享规则：JS 包含 JSX，TS 包含 TSX，JSON 包含 JSONC，Shell 覆盖 sh/Bash/zsh 别名，HCL 包含 Terraform 别名。
- 🧩 可组合核心 API：sugar-high/core 提供 parse()、generate()、render()，支持自定义解析、生成和渲染流程。
- 🏷️ 语言规范化：使用 sugar-high/lang 的 lang(fileExtension) 可对扩展名或 Markdown fence 进行语言归一化。
- ⚛️ React 组件：@sugar-high/react 导出 Code 和 Editor；Code 支持行号、自动数字感知 gutter 和高亮行范围，Editor 为轻量受控编辑器。
- 📝 Remark 插件：@sugar-high/remark 提供 ESM-first 的 remarkSugarHigh，可高亮 fenced code，并共享语言规范化和呈现钩子。
- 🎨 主题与指南：提供可复制的浅色/深色主题、CSS 变量配方以及 agent 设置指导。
- ⚠️ 破坏性变更：低层 tokenizer/parser 配置移至 parse()；tokenize、generate 等不再从根导出；lineClassName 改为 markLine；语义 token 节点暴露 tokenType；React 子路径移除；Remark 集成改为 ESM-first。
- 📏 体积与性能：完整包 minified 23.54 KiB / gzip 8.59 KiB；核心仅 3.57 KiB / 1.74 KiB；Python 高亮约每秒 26–27k 次操作。
- 🛡️ 工程化改进：包含包边界消费者测试、包体积报告和通过 OIDC 实现的 npm 来源验证。
- 🙏 致谢：感谢所有社区用户的问题反馈、集成测试和 API 贡献。

---

### [](https://tanstack.com/blog/announcing-tanstack-form-v2-alpha)

**原文标题**: [Form v2 is here: All you need to know about the alpha | TanStack Blog](https://tanstack.com/blog/announcing-tanstack-form-v2-alpha)

TanStack Form v2 alpha 正式发布，这是基于 v1 反馈从零重写的核心版本，带来了更快的运行时性能、更安全的类型，以及重新设计的验证器、监听器、Schema 处理和 SSR 流程，旨在解决 v1 中的主要痛点。

- 🎉 发布 v2 alpha：经过 v1 一年多反馈，核心重写，API 基础语法保持熟悉，同时提升性能和类型安全。
- 🔄 验证器重做为 pipeline：每个验证器独立声明触发事件，支持一个验证器多触发器（change/blur）、多验证器共享触发器，并通过 bailIfInvalid 控制执行顺序。
- ⏱️ 条件验证增强：触发事件可附带 when 条件，例如首次提交后才验证后续变更，无需在验证器内部提前返回。
- 👂 监听器同步重做：采用与验证器相同的 pipeline 模型，支持多事件监听、多个监听器共享触发器，以及条件触发。
- 📐 新增 Schema 导向模式：formOptions 提供 strictSchema 和 looseSchema，解决默认值与 schema 类型不匹配问题；loose 模式允许 null/undefined 且不改变已匹配类型。
- 🛡️ 表单组合类型安全：v2 允许对组合组件进行 branding，字段值类型不兼容的组件（如 string 字段上的 NumberInput）会在编译期报错。
- 🌐 SSR 体验改进：服务器验证与客户端共享同一份 formOpts，serverValidate 返回可区分 success 的结果，客户端直接传入 serverState，无需手动 mergeForm。
- ⏳ 暂缺功能：alpha 尚未包含内置表单持久化、非 React 适配器的 Form Composition，以及 Submit meta（多提交动作的附加数据类型）。
- 🧪 试用指南：当前仅支持 React 适配器，提供迁移指南；另有两个公开 RFC（#2296 和 #1823）待讨论，欢迎社区反馈。

---

### [](https://github.com/preactjs/preact/releases/tag/11.0.0-rc.0)

**原文标题**: [Release 11.0.0-rc.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.0.0-rc.0)

overview summary
Preact 11.0.0-rc.0 版本发布，带来了新特性、正确性修复、性能优化与维护更新，核心功能更完善，包体积进一步缩减。

- ✨ 新增 compat 中的 `use`、`useEffectEvent` 钩子，并支持 `useSyncExternalStore` 的 `getServerSnapshot`
- 🚀 核心支持 `createPortal`，实现跨容器渲染
- 🔧 正确性修复：优先使用 `moveBefore`、避免修改用户样式对象、修复模板元素复用及子节点比较等问题
- ⚡ 性能优化：采用最长递增子序列减少 DOM 移动，批量更新 `flushSync`，显著降低核心包体积
- 🛠️ 维护更新：将 React 版本提升至 19.0.0，引入现代构建配置，清理依赖并优化贡献命令
- 👥 感谢 JoviDeCroock、ssssota、Mesoptier 等贡献者的共同努力

---

### [](https://thoughtbot.com/blog/humid-1-0-react-server-side-rendering-in-rails-can-be-easy)

**原文标题**: [
        Humid 1.0: React server-side rendering in Rails can be easy! 
    ](https://thoughtbot.com/blog/humid-1-0-react-server-side-rendering-in-rails-can-be-easy)

overview summary  
Humid 1.0 是一个专为 Rails 打造的轻量级 React 服务端渲染工具，基于 mini_racer 嵌入 V8 引擎，无需额外 Node.js 进程，代码精简且易于上手，同时为未来迁移到 Cloudflare V8 isolates 提供了铺垫。

- ⚛️ Humid 1.0 发布：为 Rails 提供简单易用的 React 服务端渲染方案，解决现有工具过于复杂的问题  
- 🧩 安装与使用：仅需添加 `gem "humid"`，并用 `setHumidRenderer` 定义渲染函数，即可从 Ruby 端调用 `Humid.render` 输出 HTML  
- 🚀 核心优势：无独立 Node.js 进程，依托 mini_racer 的高性能嵌入式 V8，全部代码不足 200 行，且自带埋点与遥测支持  
- 🎯 设计目标：面向渲染前已备好全部数据的常见场景，同步调用、一次返回 HTML；同时为边缘端 Cloudflare V8 isolates 迁移做平滑过渡  
- ⚠️ 注意事项：仅支持同步渲染，无流式或异步数据获取；mini_racer 是裸 V8 环境，需自行补充 polyfill（如 React 所需）；线程安全但不 fork 安全，需参考官方指南配置服务器

---

### [让我放弃 Zustand 的状态库](https://www.youtube.com/watch?v=397MsJf8HGg)

**原文标题**: [The state library that made me drop Zustand - YouTube](https://www.youtube.com/watch?v=397MsJf8HGg)

overview summary
该内容为 YouTube 页面底部的标准链接和版权信息列表，涵盖平台介绍、法律条款、联系方式及功能说明等基础导航项。

- 📌 “关于”提供平台背景与使命介绍
- 📰 “新闻”展示媒体资讯与官方动态
- 📮 “联系我们”提供用户沟通渠道
- 🎨 “创作者”面向内容生产者的资源与支持
- 📢 “广告”说明广告合作与投放选项
- 💻 “开发者”提供 API 与技术接口信息
- 📄 “条款”列明使用协议与规则
- 🔒 “隐私”说明数据保护政策
- 🛡️“政策与安全”强调社区准则与安全机制
- ❓ “YouTube 运作方式”解释平台功能与推荐原理
- 🧪 “测试新功能”介绍实验性特性
- ©️ 版权声明归 Google LLC 所有（2026 年）

---

### [](https://www.effect.website/blog/releases/effect/40-rc)

**原文标题**: [We think this is it ... | Effect Blog](https://www.effect.website/blog/releases/effect/40-rc)

Effect 团队在多年开发、Beta 测试与生产验证后，正式发布 Effect 4.0 的 Release Candidate（RC），邀请社区参与最终验证。团队认为接口已趋近最终形态，并将在稳定版前全力修复问题与完善迁移体验，目标在 2026 年 Q3/Q4 推出正式版。

- 🚀 宣布 Effect 4.0 发布候选版本（RC），可通过 npm、pnpm、yarn、bun 安装 `effect@rc` 进行体验。
- ✅ RC 是信心的声明，不再计划大规模破坏性变更，接口已假定为最终形态。
- 🏭 社区已在生产环境中运行数月，团队还完成了对整个代码库的深入审计，修复了各类边界问题。
- 🧭 当前是迁移最佳时机，团队优先投入迁移支持，提供详细迁移指南并密切监控 GitHub issues，同时通过 Discord 和 Office Hours 提供实时帮助。
- 🧪 呼吁社区使用真实应用进行测试和验证，报告回归、Bug、迁移缺口或性能问题，用户是发布前的最终把关者。
- 📚 接下来将重写并完善文档，并投资语言工具与编码代理支持，提升整体开发体验。
- 📅 稳定版目标定在 2026 年 Q3/Q4，期待社区共同参与验证。

---

### [](https://share.transistor.fm/s/55d1846a)

**原文标题**: [This Month in React | TMIR July 2026: React-alikes, GOVERNANCE, and state management](https://share.transistor.fm/s/55d1846a)

overview summary
该文本为播客页面的功能选项列表，包括订阅平台、分享与下载等操作入口。

- 🎧 提供多种播客平台订阅入口，如 Apple Podcasts、Spotify、YouTube 等
- 📤 支持通过链接或嵌入代码分享节目内容
- 🔗 可复制链接到剪贴板，方便外部传播
- ⬇️ 提供下载功能，便于离线收听
- 📝 包含完整文字稿（Full Transcript）及章节信息
- 🖥️ 可跳转至官方网站查看更多内容
- 🔔 设有订阅、关注及更多剧集入口，方便持续跟进
- 🎁 包含“Trailer”（预告）和“Bonus”（花絮）等额外内容

---

### [](https://www.agent.sh/?utm_campaign=agent&utm_source=twir&utm_medium=email=utm_content=aug19)

**原文标题**: [Agent Conf 2026 | Warsaw | Shaping the Future of Agentic Development](https://www.agent.sh/?utm_campaign=agent&utm_source=twir&utm_medium=email=utm_content=aug19)

Agent Conf 2026 将于 2026 年 9 月 17-18 日在波兰华沙举行，聚焦“塑造 Agentic 开发未来”，汇聚工程师与构建者，探讨 AI 智能体驱动的软件构建新范式。大会涵盖主题演讲、四大议题方向、案例分享与社区交流，并依托主办方 Callstack 的深厚技术社区资源。

- 📅 会议于 2026 年 9 月 17-18 日在波兰华沙 Crowne Plaza Warsaw The HUB 举办，位于市中心商务区。
- 🤖 主题为“塑造 Agentic 开发未来”，面向使用 AI 智能体构建软件的工程师与开发者，现已开放购票。
- 🎤 演讲嘉宾包括 Carl Ross、Kent C. Dodds、Nader Dabit 等 AI 工程领袖，议题覆盖 AI 编排、Vibe Coding、智能体可观测性等前沿方向。
- 🧭 大会设置四大议题：Vibe Coding、Agentic 工程基础、多智能体编排与协调、采纳案例研究，兼顾前沿探索与生产实践。
- 📊 真实案例分享：如 AI 智能体将告警调查时间减少 70%、构建亿级智能体控制平面、用智能体工程一年内推出新银行等。
- 🏢 主办方为 Callstack，基于其 React Native EU 社区经验，已有 10 年活动组织历史，全球累计参会者超 2 万人，合作品牌超 30 家。
- 💎 设有白金、黄金、银牌及社区合作伙伴等赞助层级，并开放伙伴招募，欢迎企业加入塑造 AI 工程生态。
- 🏨 与 Crowne Plaza 和 Holiday Inn 两家酒店合作，为参会者提供特惠住宿预订服务。

---

### [](https://www.agent.sh/workshop?utm_campaign=agent&utm_source=twir&utm_medium=email&utm_content=program)

**原文标题**: [Build Your Own Software (re)Factory | Agent Conf 2026](https://www.agent.sh/workshop?utm_campaign=agent&utm_source=twir&utm_medium=email&utm_content=program)

本次工作坊聚焦于如何构建一个可控制的“软件工厂”，通过协调多个 AI 编码代理，将复杂功能需求从设计拆解到并行开发、验证与交付，弥补单一代理在可控性和工程化上的不足。

- 📅 活动于 2026 年 9 月 16 日举行，主题为“Build Your Own Software (re)Factory”
- 🤖 核心目标是让并行 AI 代理转化为可监管的软件工厂，提升多步骤流程的可见性和干预能力
- 🧩 实践流程从 PRD 拆解功能请求为可执行 ticket，映射依赖后并行启动代理工作
- ✅ 引入验证门禁：自动测试变更、失败任务返回代理重试，并阻止不完整或错误的工作
- 📊 任务状态全程可视化，涵盖 ready、in progress、blocked、verified、done 五个阶段
- 📋 议程包括启动演示、环境验证、两个构建阶段、午餐、扩展工厂练习和闪电演示
- 🧑‍🏫 主讲人为 Giovanni Laquidara，来自亚马逊的开发者倡导者，专注代理式 AI 与 harness 工程
- 📌 后续活动为 9 月 17-18 日在波兰华沙举办的“Shaping the Future of Agentic Development”会议，可购票并订阅新闻通讯获取更新

---

### [Agent Conf 2026 | 华沙 | 塑造智能体开发的未来](https://www.agent.sh/)

**原文标题**: [Agent Conf 2026 | Warsaw | Shaping the Future of Agentic Development](https://www.agent.sh/)

overview summary
Agent Conf 2026 是一场聚焦于 Agentic Development 的开发者大会，将于 2026 年 9 月 17 日至 18 日在波兰华沙举办，汇聚工程师与构建者，探讨用 AI 代理构建软件的新范式，涵盖主题演讲、四大议题方向、赞助商与社区故事。

- 📅 大会于 2026 年 9 月 17-18 日在波兰华沙 Crowne Plaza Warsaw The HUB 举行，定位为中欧 AI 枢纽。
- 🤖 主题为“塑造 Agentic 开发的未来”，旨在让工程师与构建者共同探索 AI 代理化的软件开发方式。
- 🎤 演讲者阵容包括 Carl Ross、Kent C. Dodds、Nader Dabit、Tejas Kumar 等 AI 工程与编排领域领袖，分享实践与前沿研究。
- 🧩 四大议题方向：Vibe Coding（直觉式协同编码）、Agentic 工程基础、多代理系统编排、实际采用案例研究。
- 🛠️ 议题覆盖提示词工程、代理调试、成本与失败模式、多代理任务协调、以及生产环境中的真实经验与度量。
- 🏢 赞助商分为白金、金、银、伙伴及社区伙伴等级，主办方 Callstack 鼓励企业参与合作以触达 AI 工程社区。
- 📖 会议源于 2017 年创办的 React Native EU，拥有 10 年活动组织经验，累计 2 万多名全球参会者及 30 多个合作伙伴。
- 🏨 与 Crowne Plaza 及 Holiday Inn 两家酒店合作提供优惠房价，方便参会者住宿与会后交流。
- 📬 可订阅新闻通讯，获取 AI 与 React Native 相关更新。

---

### [](https://reactnative.dev/blog/2026/08/11/react-native-0.87)

**原文标题**: [React Native 0.87 - Strict TypeScript API, Metro Update, Swift Package Manager, AGP 9 Support · React Native](https://reactnative.dev/blog/2026/08/11/react-native-0.87)

overview summary
React Native 0.87 正式发布，本次更新以 Strict TypeScript API 为默认 JavaScript API，带来更快的 Metro、iOS 上实验性 Swift Package Manager 支持，并提高了最低工具链要求（Node.js 22、AGP 9、Kotlin 2.0+），同时包含多项破坏性变更与弃用调整。

- 🎯 Strict TypeScript API 成为默认：类型直接由源码生成，提升准确性与覆盖率；API 范围限定为 react-native 根导出，内部文件变更不再影响外部。
- 🚫 破坏性变更：深层导入（react-native/Libraries/*）变成类型错误；部分类型名称和结构更新，如 refs 改为 ViewInstance、TextInputInstance 等。
- 🔁 提供临时退出开关：通过 tsconfig.json 添加 "react-native-legacy-deep-imports" 自定义条件可继续使用旧类型，该开关保留至 0.88。
- ⚡ Metro 更新至 0.87：source map 生成快 2 倍，内存占用减半；支持 TypeScript/ESM 配置文件，移除 .es6 与 YAML 配置支持。
- 📦 实验性 Swift Package Manager（iOS）：可替代 CocoaPods，仅需 Xcode；通过 npx react-native spm 命令集成，自动检测依赖变化并重新 autolinking。
- 🧩 头文件结构调整：新增 ReactNativeHeaders 与 ReactNativeDependenciesHeaders XCFrameworks；裸角括号导入需改为带命名空间，如 <React/RCTAppDelegate.h>。
- 🤖 Android Gradle Plugin 9 支持：需在 gradle.properties 中设置 android.builtInKotlin=false 和 android.newDsl=false 以兼容当前生态。
- 📈 最低环境要求提升：Node.js >= 22.13.0；Android 端 Kotlin 2.0+、minCompileSdk 34、compileSdk/buildTools 升级至 37。
- 🗑️ 多处 API 移除：如 InteractionManager（用 requestIdleCallback）、Modal animated prop、StatusBar 部分 props、useTurboModules 标志等。
- ⏳ 弃用提醒：InitializeCore、ImageBackground、NativeMethods、DrawerLayoutAndroid 等均有替代方案，未来版本将移除。
- 🙏 致谢与升级：0.87 包含 74 位贡献者的 265 个提交；现有项目可用 Upgrade Helper 迁移，新项目用 CLI 初始化，Expo 通过 expo@canary 获取。

---

### [面向每一家企业的 AI 客户支持平台 - Crisp](https://crisp.chat/en/?utm_source=twir&utm_medium=newsletter&utm_campaign=crisp_q3_nl&utm_content=19aug26)

**原文标题**: [The AI Customer Support Platform for Every Business - Crisp](https://crisp.chat/en/?utm_source=twir&utm_medium=newsletter&utm_campaign=crisp_q3_nl&utm_content=19aug26)

Crisp 是一个面向 AI 优先客户支持的一体化平台，包含 AI 代理 Hugo、全渠道共享收件箱、知识库、自动化、CRM 与分析工具，可帮助企业自动化大量咨询并提升团队效率。

- 🤖 推出 AI 支持代理 Hugo，可自动化 50% 的咨询，让团队专注于高价值工作。
- 📥 全渠道共享收件箱，集中管理来自网站、邮件、WhatsApp、Messenger、Instagram 等渠道的对话。
- 🧠 通过 4 步构建 AI 代理：训练 AI、创建无代码工作流、测试部署、验证并优化效果。
- 📚 内置知识库，让客户自助搜索答案，减轻客服压力并提升自主性。
- ⚙️ 提供无代码自动化工具，既支持客户面向的 AI 聊天机器人，也可加速内部团队回复。
- 👥 自带支持 CRM，同步客户数据与历史交互，实现个性化沟通。
- 📊 提供分析功能，监控团队绩效，识别优化方向，提升服务效率。
- 💬 可快速嵌入网站的聊天插件，支持网页、iOS、Android 和 React 应用，实时引导转化。
- 🎯 面向客服、销售和营销团队，支持跨渠道支持、销售自动化和营销触达。
- 🌟 已获 10,000 家公司信任，客户反馈强调其灵活性、自动化能力与优秀体验。

---

### [](https://github.com/react/react-native-website/pull/5111)

**原文标题**: [[docs] Update Strict TypeScript API guide by huntie · Pull Request #5111 · react/react-native-website · GitHub](https://github.com/react/react-native-website/pull/5111)

该 PR 为 React Native 官方文档网站更新了“严格 TypeScript API 指南”，面向 0.87 版本发布，经过多轮评审和修改后成功合并至主分支。

- 📝 合并 PR #5111，标题为“更新严格 TypeScript API 指南”，由 huntie 提交并合入 react/react-native-website 主分支。
- 🚀 针对 React Native 0.87 版本进行文档更新，并完成全文措辞润色。
- 🔧 新增并整合了 ref 类型指导，同时加入 `react-native/setup-env` 的使用说明。
- 📑 新增“开始之前”“更新测试模拟”和“常见问题”等章节，并关联 proposal #1003，替代旧 PR #5067。
- 🔄 根据评审意见多次 force-push 更新分支，将默认方式从“选择加入”改为“选择退出”，并注明仍需后续 PR 继续完善。
- ✅ Simek 最终批准更改，合并提交为 c2a4ad9，8 项检查全部通过，随后删除源分支。
- 🔗 该 PR 被 0.87 发布博客草稿 #5201 引用，并带有 CLA Signed 与 p: Facebook Partner 标签。

---

### [](https://reactnativeconnection.io/?utm_source=thisweekinreact.com)

**原文标题**: [React Native Connection Conference](https://reactnativeconnection.io/?utm_source=thisweekinreact.com)

overview summary
React Native Connection 是法国首个专注于 React Native 开发者社群的会议，将于 2026 年 9 月 24 日在巴黎举行，提供全天议程、多位知名讲师、门票方案、赞助商与社区资源。

- 🗓️ 会议定于 2026 年 9 月 24 日在巴黎举办，是法国首个专门面向 React Native 开发者的会议。
- 🎤 讲师阵容包括来自 Meta、Expo、Callstack、Margelo、Software Mansion 等公司的专家，涵盖工具链、导航、性能、XR 等主题。
- 🎟️ 门票分为 Early Bird（已售罄）、Regular（289 欧元）和免费 Community 票，社区票需在 9 月 17 日前申请。
- 📋 全日议程包含主题演讲、圆桌讨论、咖啡休息和社交环节，议题涉及 React Native 测试、键盘交互、Web 支持、导航库、动画等。
- 🤝 会议旨在帮助开发者在法国及国际社区中建立持久联系，并了解 React Native 领域的最新实践与趋势。
- 🏢 赞助商包括 RevenueCat、The Mobile-First Company 和 Codemagic，媒体合作伙伴有 weshipit.today 与 This Week In React。
- 👥 组织团队由多位资深 React Native 开发者与社区活跃成员组成，拥有丰富的移动开发和开源贡献经验。
- 📌 会议提供 FAQ、赞助联系渠道，并设有往届活动回顾、其他技术会议和社区资源入口。

---

### [](https://margelo.com/blog/fitting-RAG-in-your-pocket)

**原文标题**: [Fitting RAG in Your Pocket: Local Retrieval in React Native - Margelo](https://margelo.com/blog/fitting-RAG-in-your-pocket)

文章介绍如何在 React Native 中构建一个完全离线的 RAG（检索增强生成）应用，从本地聊天问答到图像搜索，使用本地 LLM、嵌入模型和 SQLite 向量数据库，并强调数据管道中容易出错、静默失败的细节。

- 🎯 目标：构建完全在设备上运行的 RAG，无需服务器或 API，即使在廉价手机和飞行模式下也能流畅工作。
- 🤖 本地生成使用 Qwen2.5-0.5B（469MB），通过 @react-native-ai/llama 加载，基于 llama.cpp 执行。
- ⚠️ 设备上下文窗口仅 4K tokens，而 WhatsApp 导出超过 21K tokens，导致请求被直接拒绝（Context is full）。
- 💡 解决思路不是扩大窗口，而是先检索最相关的消息片段，再仅将少量上下文交给模型——这正是 RAG 的核心思想。
- 🔍 语义检索依赖嵌入模型：文本转为 384 维向量，含义相近的内容在向量空间中彼此靠近，从而解决同义词、昵称等关键词匹配失效的问题。
- 🗄️ 通过将 sqlite-vec 编译进 nitro-sqlite，SQLite 直接变成向量数据库，支持原生 KNN 搜索，无需额外的数据库引擎。
- ✂️ 分块策略：按日期分组、保留每条消息的发送者前缀，避免分块时丢失说话人信息，防止模型后续幻觉归因。
- 🌐 嵌入模型选用多语言 MiniLM（384 维，约 119MB），避免纯英文模型在处理中英混合聊天时产生雷同向量、检索失效。
- 📥 批量插入向量时使用 JSON 数组字符串，并通过 executeBatch 一次性写入；查询时用同一模型嵌入问题，再执行 KNN 搜索返回最相关片段。
- 📝 生成阶段使用 temperature:0、stop 序列以及系统提示词（“只依据上下文回答”），防止小模型过度发挥或继续模拟聊天。
- 🔁 后续问题（如“多少钱？”）通过继承上一问题 + 重放最近几轮对话来解决，使模型能正确解析“it”等指代。
- 📷 向量搜索可以脱离 LLM：文章进一步展示使用 CLIP 嵌入图像与文本，实现文本搜图、以图搜图、相机搜图三种方式。
- ⚡ 性能数据（低端手机）：图像解码 16ms、CLIP 推理 64ms、KNN 5ms——神经网络不是瓶颈，像素解码和预处理才是。
- ⚙️ 常见陷阱：图像像素格式（BGRA/RGBA）不能硬编码，否则会默默交换红蓝通道，导致所有相似结果错误；分块、嵌入模型不匹配等也会静默失败。
- 🚀 未来方向：GraphRAG，通过抽取知识图谱可以回答“我们计划但从未成行的旅行有哪些？”这类需要跨片段推理的问题。
- 🧠 核心教训：RAG 失败大多是无声的——分块丢失信息、嵌入模型不匹配、字节序错误等，都会给出自信但错误的结果，因此应先排查数据管道，再怀疑模型。

---

### [](https://swmansion.com/blog/the-memory-hermes-cant-see-stale-shadow-nodes-in-react-native/)

**原文标题**: [The Memory Hermes Can't See: Stale Shadow Nodes in RN](https://swmansion.com/blog/the-memory-hermes-cant-see-stale-shadow-nodes-in-react-native/)

概述：本文探討了 React Native 新架構中 Shadow Tree 的記憶體問題：動畫更新與元件卸載時，舊的 Shadow Node 會因 JavaScript 端的 Wrapper 持有引用而無法釋放，直到 GC 偶然觸發才被清除。作者透過實驗證實此現象，並嘗試強制週期性 GC 與設定記憶體壓力兩種方法，雖能暫時緩解但都不是理想的修復方案。

- 🧠 發現：測量持續掛載/卸載動畫視圖的 App 時，發現 GC 偶爾執行才能釋放數十 MB 記憶體，顯示有隱藏記憶體累積。
- 🌳 原因：Shadow Tree 的 Node 不可變，動畫更新會複製 Node 並產生新修訂版；但元件卸載後，舊的 Shadow Node Wrapper 仍指向已死修訂版的 Node，阻礙釋放。
- 🔗 機制：Shadow Node Wrapper 是 JS 物件，透過 JSI 持有 C++ 的 shared_ptr；GC 不知道這些物件背後掛著大量堆外記憶體。
- 📊 實驗一：每 60 秒強制執行 GC，可阻止 Shadow Node 累積，記憶體曲線趨平，但非實際可用的解法。
- ⚙️ 實驗二：為每個 Wrapper 設定 2 KB 外部記憶體壓力，也能防止累積，但導致 GC 過度頻繁觸發，可能耗費 CPU。
- ⚠️ 兩難：強制 GC 與硬編碼記憶體壓力都證實了診斷，但不適合直接出貨；作者尚無完美修復方案。
- 🕳️ 反諷：小應用因 GC 不常觸發，反而更容易受此問題影響；實驗結果也可能因單次 GC 釋放大量記憶體而失真。
- 🔮 預告：下一篇文章將探討 react-native-worklets 模式與 Hermes 版本對 Expensify App 記憶體消耗的影響。

---

### [](https://shopify.engineering/mobile-e2e-testing)

**原文标题**: [How we raised mobile end-to-end test stability to 98% (2026) - Shopify](https://shopify.engineering/mobile-e2e-testing)

overview summary
Shopify 通过重建移动端 E2E 测试框架，将稳定性从 50% 提升到 98%，核心是严格 API 与计算机视觉。

- 🔍 旧框架问题：基于 Appium 的灵活 API 导致测试滥用暂停和隐式等待，产生大量 flaky；断言的是组件树而非用户真实所见。
- 🏗️ 重建方案：在 Appium 外层封装严格的 builder API，只暴露安全操作，同时保留底层驱动能力但默认不可见。
- ✅ 每步必断言：任何点击、等待、输入后必须声明预期屏幕状态，失败可立即定位；常用步骤可复用，逃生口统一用 `UNSAFE_` 前缀标记。
- 👁️ 计算机视觉定位：用 PaddleOCR 识别文本、OpenCV 匹配 Polaris 图标，像用户一样“看屏幕”找元素；Test ID 仅作为显式后备。
- ⚡ 编写效率提升：写测试直接 `touch({ text: 'Save' })`，无需检查器；AI agent 也能零代码库知识快速生成正确测试。
- 🎥 自诊断视频：每次运行生成带注释的视频，展示每一步查找内容和位置，失败原因几秒内可见，无需重跑。
- 💻 统一 CLI：同一命令可在本地模拟器、CI、远程设备云运行，切换环境只需改一个参数。
- 📈 数据结果：稳定性从 50% 升至 98%，剩余失败多为网络或模拟器启动问题；新增预合并 flakiness gate 防止不稳定测试进入阻塞套件。
- 🔮 后续计划：验证成功后推广到其他应用；核心经验是限制 API 面、用视觉交互、强制每步断言、先验证稳定性再合入。

---

### [如何使用 Expo 构建一个健壮的活动跟踪器 — Expo 博客](https://expo.dev/blog/how-to-build-a-resilient-activity-tracker-with-expo)

**原文标题**: [How to build a resilient activity tracker with Expo â Expo blog](https://expo.dev/blog/how-to-build-a-resilient-activity-tracker-with-expo)

overview summary
该文介绍了如何使用 Expo 生态构建一个抗应用终止、GPS 噪声和后台杀死的步行追踪器，核心策略包括后台任务、卡尔曼滤波、多层持久化与单调合并，以及跨平台步数采集。

- 📱 挑战：纯内存态在后台/被杀时丢失，GPS 漂移导致虚假距离，无崩溃恢复。
- 🎯 目标：后台追踪、GPS 滤波、持久化恢复三者协同，实现“不可杀死”的会话。
- ⚙️ TaskManager：在 React 树外注册后台定位任务，冷启动时从存储恢复状态，并按时间排序处理批量位置点。
- 🧠 关键设计：进程被回收后重新播种累加器，避免距离停止增长；用户主动杀应用则无法恢复。
- 📡 定位配置：Android 需`killServiceOnDestroy:false`，避免距离间隔过滤；权限需后台定位和前台服务，且需检查系统定位总开关。
- 🛰️ 卡尔曼滤波：结合精度门限（30m）、速度门限（8m/s）、异常点门限和卡尔曼平滑，滤除车辆和漂移距离。
- 📏 距离计算：优先积分多普勒速度（`coords.speed`）而非位置差分，配合 0.3m/s 死区和 10 秒 dt 上限，消除正偏差。
- 🧱 三层持久化：内存（Zustand）、本地（AsyncStorage）、云端（Supabase），在后台转换时写盘，云端用 GREATEST 避免覆盖。
- 🔁 单调合并：两个写入方（后台任务和前台 store）共用键，采用“保留更高值”策略，确保距离/步数不倒退。
- 💾 恢复机制：启动时检查孤儿会话，区分“服务器无此会话”与“网络不可达”，离线时默认保留本地快照。
- 👣 步数追踪：iOS 用 Pedometer 轮询；Android 自建 Kotlin Expo Module，用 STEP_COUNTER 基准 + 前台差值，并限制在 GPS 看到步行速度时。
- ✅ 实际结果：零会话丢失、距离准确、与专业硬件接近、杀进程后可恢复。
- ⚠️ 残余风险：OEM 电池管理（小米/华为/三星等）仍可能杀服务；iOS 16.4 后需保持连续更新或背景指示器。
- 🚀 Expo 意义：TaskManager、Expo Modules、EAS Build 等已支持原生能力，无需 eject 即可实现复杂追踪应用。

---

### [在 React Native 应用中扫描条形码：完整指南（2026）- Margelo](https://margelo.com/blog/react-native-barcode-scanner)

**原文标题**: [Scanning Barcodes in React Native Apps: The Complete Guide (2026) - Margelo](https://margelo.com/blog/react-native-barcode-scanner)

本文是 2026 年 React Native 扫码方案的完整指南，系统比较了免费与付费库、底层引擎、各平台行为差异、格式兼容性及弃用库替代方案，并给出按使用场景的选择建议。

- 📊 选择建议：一次性简单扫码用 react-native-data-scanner；需要自定义相机界面用 VisionCamera；Expo Go 项目用 expo-camera；高吞吐工业场景考虑商业 SDK。
- 🧩 底层引擎：ML Kit、AVFoundation、VisionKit、ZXing 决定扫码行为与格式支持，库只是封装层。
- ⚡ 最简单方式：react-native-data-scanner 一次调用即可完成扫码；Android 通过 Google Play services 无需相机权限，iOS 需 NSCameraUsageDescription。
- ⚠️ 简单方式代价：使用系统自带 UI、每次只能扫一个码、无法在关闭相机前验证代码、要求 iOS 16+、不支持 Expo Go。
- 🎥 最强大方式：VisionCamera 支持自绘 UI、连续多码扫描、JS 内验证，并可通过 ML Kit 插件实现跨平台一致解码。
- 📱 iOS 零依赖方案：VisionCamera 的 Object Output 基于 AVFoundation，无额外依赖；可通过平台后缀文件与 autolinking 排除实现 iOS 零扫描依赖。
- 🧪 Expo 方案：expo-camera 适用于 Expo Go，Android 用 ML Kit，iOS 用 AVFoundation/ZXing；onBarcodeScanned 会重复触发，需手动置 undefined 实现单次扫描。
- 🖼️ 图片扫码：VisionCamera 提供 scanCodesInImageAsync；Expo 的 Camera.scanFromURLAsync 在 iOS 上仅支持 QR 码。
- 🔢 格式注意：各库格式字符串不同；iOS 会把 UPC-A 报告为 EAN-13；只请求所需格式可显著提升性能。
- 🪪 PDF417：所有库均支持，但密集或损坏的码可能失败；建议全分辨率扫描，仅大规模工业场景才需商业引擎。
- 🗑️ 弃用库：react-native-camera、react-native-qrcode-scanner、expo-barcode-scanner 等已停止维护，应迁移到 VisionCamera 或 expo-camera。
- 💰 商业 SDK：Scandit/Scanbot 适合极端边缘场景，但报价不透明、基准测试缺少公开方法论；建议先用免费方案验证，再决定是否付费。
- ✅ 结论：2026 年 React Native 扫码已是成熟方案，从最简单的工具开始，按需求逐步升级即可。

---

### [](https://expo.dev/blog/fable-5-vs-gpt-5-6-sol-expo-apps)

**原文标题**: [Fable 5 vs GPT-5.6 Sol: I spent $2,000 and 2 billion tokens to find out who wins â Expo blog](https://expo.dev/blog/fable-5-vs-gpt-5-6-sol-expo-apps)

这是一篇关于 AI 模型开发 Expo 应用能力的对比实验。作者花费 2000 美元、消耗超过 20 亿 token，用 Fable 5、GPT-5.6 Sol 和 GPT-5.5 分别开发三款 React Native/Expo应用，并进行代码质量、速度、成本等多维度评估。结果显示Fable 5 在绝大多数场景下表现最佳，但 GPT-5.6 在特定自动化任务中也有独特优势。

- 💰 实验背景：作者耗资$2,000、消耗 20 亿 token，让三个 AI 模型从头到尾“一次性”构建三个 Expo 应用，全程不人工改代码。
- ⚖️ 测试规则：三个模型（Fable 5、GPT-5.6 Sol、GPT-5.5）使用相同提示词、模板和工具，并强制在 iOS 模拟器上逐项验证功能。
- 📱 应用 1（AI 卡路里追踪器）：Fable 5 在 UI 一致性和代码健康度上胜出（88 分），GPT-5.5 残留模板“探索页”显得粗糙，GPT-5.6 主页细节最佳。
- 📊 应用 1 指标：Fable 5 成本$276.95、耗时 3h45m；GPT-5.6 成本$170.16、耗时 5h17m；GPT-5.5 成本$157.23、耗时 5h20m。Fable 5 最快但最贵，代码质量仍领先。
- 💬 应用 2（ChatGPT 克隆）：GPT-5.5 无法正常回复，Fable 5 和 GPT-5.6 均可流式输出；Fable 5 使用原生按钮与侧边栏，UI 更佳。
- 📉 应用 2 指标：Fable 5 耗时 2h、代码量 2.0k 行，仅为 GPT 模型的一半左右，代码健康度 85 分，全面碾压对手。
- 🛏️ 应用 3（SwiftUI 转 Expo 重写）：Fable 5 完美还原睡眠追踪应用，包括实时活动、图表和主题，甚至修复了 Swift 原版的一个 bug。
- ⏱️ 应用 3 指标：Fable 5 耗时 3h25m 但成本高达$558.83（$163/h）；GPT-5.6 耗时 13h34m 但成本仅$254.50，代码健康度 86 分非常接近 Fable 的 88 分。
- 🔍 Token 消耗主因：模拟器验证工具（Argent）产生大量截图与操作元数据，占用上下文窗口，建议用子代理执行验证以避免污染主上下文。
- 🏆 最终结论：Fable 5 像“资深同事”，代码更少、更快、质量更高，适合完整 PR 和创意验证；GPT-5.6 是“拼命三郎”，适合明确定义的自动化任务和简单脚本。
- 🔮 未来展望：作者可能测试更多模型（如 Kimi）或对比不同验证工具；相关代码、技能和 MCP 服务器均已开源共享。

---

### [](https://swmansion.com/blog/haptic-feedback-on-the-web-why-the-web-deliberately-refuses-to-be-as-tactile-as-native-apps/)

**原文标题**: [Web Haptic Feedback: Why It Refuses to Be More Tactile](https://swmansion.com/blog/haptic-feedback-on-the-web-why-the-web-deliberately-refuses-to-be-as-tactile-as-native-apps/)

概述：本文章探讨了为何网页端的触觉反馈远不如原生应用丰富，其根本原因在于浏览器厂商在隐私、指纹识别和安全方面做出的权衡。文章解释了振动 API 为何简单、原生应用为何不受同等限制、苹果为何不支持该 API，以及未来的 Web Haptics API 如何通过语义化设计在功能与隐私间取得平衡。

- 📱 网页仅提供单一振动 API（`navigator.vibrate()`），只能控制振动时长或序列，无法调整振幅、频率等底层特性，即使硬件支持更复杂效果。
- 🛠️ 开发工具如 Pulsar 通过将振动拆分为精确时间脉冲序列，在现有 API 限制下模拟“强度”和“频率”变化，但无法突破浏览器未开放的能力。
- 🔍 先进触觉功能可能暴露设备硬件特性，由于振动马达存在微观制造差异，结合陀螺仪等传感器可读取独特的振动特征，形成难以清除的硬件级浏览器指纹。
- 🧩 即使仅让网站查询设备触觉能力（如是否支持振幅控制），也会将用户划分成更小群体，增加指纹识别的熵值，因此浏览器刻意避免暴露这些信息。
- 🛡️ 触觉与运动传感器结合会带来额外隐私风险，如利用振动与加速度计可推断设备所处的物理环境（桌面、沙发或手中），甚至被用于侧面攻击或广告画像。
- ⚙️ 振动 API 的设计初衷是“最低共同标准”，因为早期移动设备触觉硬件差异巨大，统一为开关式振动以确保跨设备可预测，但硬件进步后 API 仍未演进。
- 🔐 原生应用通过应用商店安装、审核及明确的权限声明（如 Android 的 VIBRATE 权限）建立信任链；而网页脚本无需安装即可执行，第三方代码来源复杂，风险更高。
- 🌐 网页上运动传感器原本无需用户明确授权，容易成为指纹和侧信道攻击目标；苹果从 iOS 12.2 起逐步收紧权限，要求 HTTPS 和用户手势才能请求传感器数据。
- 🚫 浏览器对振动功能还有额外限制：需用户交互后才可触发，页面不可见时自动抑制，振动时长通常限制在 10 秒左右；目前仅 Chromium 系支持，Safari 和 Firefox 均不支持。
- 🍎 苹果拒绝实现振动 API 的原因在于其 Taptic Engine 硬件可提供精细触感，而现有 API 仅能表达简单的开关脉冲，不值得兼容；此外也担心指纹、耗电和广告滥用。
- 🔮 提议中的 Web Haptics API 转向“语义化触觉”：通过预定义效果（如 tick、edge、align、hint）描述交互意图，由浏览器决定具体体验，并刻意隐藏硬件能力，同时通过权限策略阻止第三方 iframe 默认使用。
- 📌 核心结论：网页触觉限制是保护隐私与安全的有意设计，开发应将其视为渐进增强，善用现有 API 的创造性组合，并期待未来 API 在体验与隐私间找到更好的平衡。

---

### [](https://configcat.com/blog/ab-testing-react-native-apps-with-feature-flags/?utm_source=thisweekinreact_newsletter&utm_medium=sponsor&utm_campaign=reactnative_20260819)

**原文标题**: [A/B Testing React Native Apps with Feature Flags | ConfigCat Blog](https://configcat.com/blog/ab-testing-react-native-apps-with-feature-flags/?utm_source=thisweekinreact_newsletter&utm_medium=sponsor&utm_campaign=reactnative_20260819)

overview summary  
- 🧪 A/B 测试是一种向不同用户群发布两个版本（A/B）并对比效果的方法，可降低永久发布新功能的风险。  
- 🚩 在 React Native 中，使用功能标志（如 ConfigCat）可避免为每个变体单独发版和等待应用商店审核，一个构建即可控制流量并支持秒级回滚。  
- ⚖️ 演示实验：通过 ConfigCat 的百分比选项，将 50% 用户分到变体 B（修改按钮文案），50% 留在变体 A（原文案），用 Amplitude 追踪“SignupButton Clicked”事件。  
- 📦 前置依赖：安装 `configcat-react`、`@amplitude/analytics-react-native` 和 `@react-native-async-storage/async-storage`。  
- 🛠️ 步骤包括：创建功能标志并设置 50/50 分流 → 集成 ConfigCat → 连接 Amplitude 数据源 → 在按钮点击时发送事件并按 `buttonText` 分组建图。  
- 📊 测试期间每日检查图表，主要观察异常下降；结束后使用 Amplitude 的 Compare 功能对比结果。  
- 🧹 结束测试时若 B 获胜，将规则设为 100% true 并验证后移除标志；若 A 获胜或结果不明确，则设为 false 并清理，避免遗留“僵尸标志”。  
- 🏆 额外技巧：订阅 ConfigCat 的 `flagEvaluated` 钩子，自动向 Amplitude Experiments 发送 `$exposure` 事件，无需手动记录变体。  
- ✅ 同一模式可扩展至定价页、onboarding 流程、结账改版等任何有明确假设和可衡量结果的实验。

---

### [](https://invertase.io/blog/react-native-firebase-v26-release)

**原文标题**: [React Native Firebase v26: A New Foundation for the Next Decade](https://invertase.io/blog/react-native-firebase-v26-release)

React Native Firebase v26 是一次里程碑式的大版本发布，围绕 TurboModules、TypeScript 全量迁移和模块化 API 完成了根本性架构升级，为未来十年的发展奠定基础。此次更新整合了 19 个包，移除了旧版命名空间 API，并通过自动化类型对比确保与 firebase-js-sdk 保持高度一致。升级需要启用 React Native 新架构，未准备好的用户可继续使用 v25。v26 还带来了 Firebase AI、Firestore Pipelines、Auth/Functions 增强及多项可靠性修复，同时路线图聚焦 Swift Package Manager、原生消息体验和安全供应链。

- 🏗️ 核心架构升级：JavaScript 全面迁移至 TypeScript，经典 Bridge 替换为 TurboModules，并移除命名空间 API，全面转向模块化调用（如 `getAuth(app)`）
- 🔄 类型自动对齐：CI 中内置与 firebase-js-sdk 的 TypeScript 形状对比，避免 API 漂移在上线后才暴露
- ⚠️ 升级条件：所有带原生桥接的包均要求新架构（Codegen TurboModules），无法启用时建议暂留 v25
- 🧭 迁移支持：提供自动化迁移清单和手动迁移指南，需同步升级包、启用新架构、去除命名空间导入并移除多余的 `.then`
- 🤖 Firebase AI：新增 Firebase AI Logic 包，旧的 vertexai 包转为包装层，涵盖工具、实时/模板 API、Imagen 和函数调用
- 🗄️ Firestore Pipelines：支持 stages、expressions 及原生对等能力，满足大规模数据查询需求
- 🔐 Auth & Functions 增强：新增 Android 手机号验证、TOTP MFA、流式 callable 和更完善的 Credential Manager 指导
- 🛠️ 可靠性修复：解决消息存储限制、OOM、React context 竞争和 APNs 超时等关键稳定性问题
- 🚫 弃用项：Dynamic Links 随 Google 产品关停而移除，消息权限 API 弃用并转向平台原生通知库
- ⏳ 进行中工作：消息事件暂时使用旧版原生事件代理，部分 FieldValue 辅助方法仍待上游原生 SDK 支持
- 🎯 未来路线图：优先推进 Swift Package Manager 支持（v26.1 已开始）、原生消息卓越体验和供应链安全最佳实践

---

### [](https://github.com/Shopify/react-native-skia/releases/tag/v2.11.0)

**原文标题**: [Release v2.11.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.11.0)

react-native-skia 发布了 v2.11.0 最新版本，发布于 2026 年 8 月 6 日。该版本主要包含一项依赖升级和一项新功能，并附带资源文件与签名验证。

- 🔖 最新版本为 v2.11.0，发布于 2026 年 8 月 6 日。
- 🐛 修复：升级到 m152（#3993）。
- ✨ 新功能：支持从单个共享值驱动多个动画属性（select）。
- 📦 包含 3 个资源文件。
- 🔏 提交经 GitHub 验证签名（GPG 密钥 ID：B5690EEEBB952194）。
- 🧩 自该发布以来，已有 4 个提交合并到 main 分支。

---

### [](https://github.com/callstackincubator/rozenite/releases/tag/v2.1.0)

**原文标题**: [Release v2.1.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v2.1.0)

rozenite v2.1.0 发布了，包含许多功能增强、UI 改进、错误修复和基础设施迁移，主要贡献者是 V3RON 和 AndreiCalazans。

- 🎨 为 UI 组件添加 Storybook，并新增 List 和 NestedList 组件
- 🧩 实现功能标志插件，支持特性开关控制
- 🚀 CLI 新增 `rozenite skills` 命令，并支持从 lockfile 自动检测包管理器
- 🐛 修复存储插件在失效事件中包含条目计数，以及应用重载后恢复存储的问题
- 🔧 修复 TanStack Query 插件重载后重新同步面板，中间件改用自研限流器解决 Metro CJS 加载问题
- 📦 自动化 Chrome 扩展签名发布打包，并修复 manifest.json 格式化
- 📚 添加兼容性表格和网站页面，简化并人性化插件和入门文档
- ⚙️ 迁移至 oxfmt、lefthook、pnpm v11，统一包元数据和 README
- 🛠️ 移除多个私有 react-native 导入（Fusebox DevTools 和网络活动插件），修复启动停滞问题
- 👥 贡献者：V3RON 和 AndreiCalazans

---

### [](https://github.com/getsentry/sentry-react-native/releases/tag/8.23.0)

**原文标题**: [Release 8.23.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.23.0)

sentry-react-native 发布了 8.23.0 版本，主要包含 iOS 内部实现迁移、多项关键修复、内部代码调整以及 Android SDK 依赖升级。若你的 React Native 版本低于 0.75，需要额外修改 Podfile 配置才能正常安装。

- 🔄 将 iOS 内部实现从废弃的 `PrivateSentrySDKOnly` 迁移到 `SentrySDK.internal`，并重新引入此前因截图问题被回滚的修复（底层 cocoa bug 已在 9.24.0 修复）。
- ⚠️ 如果目标 React Native < 0.75，必须在 `ios/Podfile` 中添加 `use_modular_headers!`，否则 `pod install` 会因 Swift pod 依赖 ObjC 模块而失败。
- 🐛 修复内部诊断日志去向：将 TurboModule  instrumentation、scope sync、Expo Router error boundary 等 10 处内部警告从 Sentry Logs API 改为 debug logger，仅当 `debug: true` 时输出，避免污染项目数据。
- ⏱️ 修正 callback 风格原生模块调用的耗时统计：现在会等待成功/失败回调完成才记录时长，慢调用会生成 `native.turbo_module` breadcrumb；旧架构下失败回调也会按 React Native 约定记为错误。
- 📦 修复 Expo config plugin 中 `config-plugins` 的解析方式，改为通过 `expo` 包解析。
- 🔗 使 `Podfile.lock` 中的 `RNSentry` SPEC CHECKSUM 机器无关：改用 `$(PODS_ROOT)/sentry-xcframeworks/…` 符号链接，避免开发者和 CI 之间锁文件频繁变动，也无需再设置 `SENTRY_XCFRAMEWORK_CACHE_DIR` 临时变量。
- 🛠️ 将 `enableTurboModuleTracking` 标记为内部选项并修正文档：该选项只安装原生 `TurboModulePerfLogger`，没有消费者接收回调，实际不会产生任何数据；相关功能来自默认启用的 `turboModuleContextIntegration()`。
- 📈 升级 Android SDK 依赖：从 v8.51.0 升至 v8.52.0。

---

### [](https://github.com/software-mansion/react-native-screens/releases/tag/4.27.0)

**原文标题**: [Release 4.27.0 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/4.27.0)

react-native-screens 4.27.0 版本发布，主要新增对 React Native 0.87 的支持并修复 iOS 运行时崩溃，同时引入实验性 ScrollToTopGuard 组件，并将 Split 组件完整从 Swift 迁移到 Objective-C。该版本还包含多项改进、错误修复和杂项更新。

- 🚀 支持 React Native 0.87.0-rc.3，并修复 iOS 运行时崩溃 (#4461)
- ✨ 新增实验性 iOS 组件 ScrollToTopGuard (#4454)
- 🔄 将 Split 组件各部分从 Swift 迁移到 Objective-C (#4458, #4459, #4462, #4463, #4465, #4466)
- 📦 Android Stack v5：支持通过 view command 发送多个更新 (#4243)
- 📱 iOS Stack v5：实现头部菜单的基本 view commands；Stack v4 为 UIMenu 子菜单增加 subtitle 支持 (#4339, #4469)
- ⚙️ 将 backTitleVisible 默认值从字符串 `'true'` 改为布尔值 `true` (#4457)
- 🧪 测试补充：新增 Stack v5 preventNativeDismiss 嵌套栈场景 (#4279)
- 🐛 修复 Android：防御性处理意外 menuItemId、header 高度 inset 计算、屏幕移除时 header 更新导致的崩溃，以及 FormSheet v4 的 inset/布局监听器清理 (#4450, #4452, #4468, #4470)
- 🐛 修复 iOS：转场期间不再交换 view controller 的 view、Stack v4 方向回退继承、Tabs 异步图标加载后重新布局 tab bar 防止 iOS 26 标签截断、Stack v5 使用 framework 风格导入 React 头文件 (#4455, #4456, #4460, #4472)
- 🐛 修复 JS：禁止使用 ViewInstance 类型 (#4471)
- 🧹 杂项：更新工作流、移除 v4 夜间发布流程、更新 react-navigation 子模块、修复 FabricExample 增量编译等问题 (#4353, #4366, #4396, #4401, #4451, #4453, #4467)

---

### [Maestro CLI 2.8.0：从元素内部任意点滑动](https://maestro.dev/blog/maestro-cli-2-8-0)

**原文标题**: [Maestro CLI 2.8.0: swipe from any point inside an element](https://maestro.dev/blog/maestro-cli-2-8-0)

Maestro CLI 2.8.0 发布，带来流程编写新能力、设备处理改进、云端上传与报告修复，以及多项可靠性修复。

- 🖐️ `swipe.from` 新增可选 `point` 参数（支持百分比或绝对坐标），可从元素内部指定位置开始滑动，适配复合布局和滑动确认手势；省略时保持原有居中行为。
- 🔢 变量 `${VAR}` 扩展至 `launchApp.permissions`、`setPermissions` 的值以及 `assertScreenshot.thresholdPercentage`，让同一流程文件可跨环境复用。
- 🔄 `childOf` 选择器每次重试都会刷新视图层级，不再需要先 `assertVisible` 父级，深层嵌套链在元素缺失时也能在一个超时内正确失败。
- 📱 Android 模拟器启动设有默认 3 分钟的有界超时（可用 `MAESTRO_DEVICE_BOOT_TIMEOUT` 配置），挂起或崩溃时会在超时内清晰报错。
- 🏁 `setDeviceLocale` 在 Android 上更快：先检查当前语言，匹配则跳过；需要更改时通过 `getprop` 确认完成，秒级生效。
- 🎯 `startDevice` 的语言设置会应用到刚启动的设备，修复多设备环境中语言可能落到无关设备的问题。
- 📱 缺少 `devicectl` 的主机上，iOS 物理设备列表会被跳过，但仍返回 `simctl` 列出的模拟器。
- 📤 上传仅在安全时重试：读取超时或网关 502 等结果未知场景会停止并提示检查；读取超时调整为 15 分钟，移除 5 分钟调用超时，恢复后端 4GB 最大上传。
- 🗂️ `takeScreenshot` 和 `startRecording` 的路径会预先校验，非法路径在文件操作前报 `InvalidCommand`，写入失败报 `DestinationIsNotWritable`。
- 🔧 `onFlowEnd` 在 `onFlowComplete` 失败时也会执行，确保最需要的设备日志和 `manifest.json` 被收集。
- 📊 JUnit 与 HTML 报告已链接到 Cloud：每个 `<testcase>` 携带 `cloud.runId` 和 `cloud.runUrl`，`<testsuite>` 携带 `cloud.uploadId` 和 `cloud.url`；HTML 报告增加每流程“Maestro Cloud run”链接和上传 ID 链接。
- ⏱️ JUnit 时间戳截断为整秒（`yyyy-MM-ddTHH:mm:ss`），套件持续时间为墙钟时长并匹配 `startTime`，符合 schema 供 CI 工具解析。
- 🔗 Cloud 的 similar-device 提示可复制粘贴，`start-device` 命令回显正确的 `--device-os`（如 `android-34`）并反映用户提供的 `--device-model`。
- ⏲️ `maestro test` 和 `maestro cloud` 对超过 1 秒的时长统一以整秒显示。
- 🚀 通过 `curl -fsSL "https://get.maestro.mobile.dev" | bash` 更新至 2.8.0 即可获得以上全部改进。

---

### [](https://github.com/software-mansion/enriched-markdown/releases/tag/v1.0.0)

**原文标题**: [Release v1.0.0 · software-mansion/enriched-markdown · GitHub](https://github.com/software-mansion/enriched-markdown/releases/tag/v1.0.0)

这是 software-mansion 的 enriched-markdown 库 v1.0.0 版本的发布说明，重点引入了完整的 Markdown 输入编辑管道、iOS 原生渲染系统，以及大量跨平台修复、重构和测试改进。

- 🎉 正式发布 v1.0.0，包含 30 次提交，累计大量新功能与改进。
- ✍️ 新增输入块编辑管道，支持 H1-H6 标题块、粘贴时导入块范围，以及标题工具栏和切换命令。
- 📱 iOS 端新增完整 Markdown 渲染系统：AST 转 attributed string、SwiftUI 视图、异步解析渲染、主题系统，覆盖标题、链接、代码块、图片、列表、引用、分割线等。
- 🖼️ 增强图片功能：支持自定义请求头、加载本地图片、保留原始图片，以及图片的 maxHeight、aspectRatio、resizeMode 样式。
- 📋 改进列表与代码块：支持列表项间距、有序列表起始编号、GFM 风格代码块、代码块高亮颜色与流式渲染。
- 🐛 大量修复：包括光标测量、链接误点、数学公式渲染、软换行、Web WASM ArrayBuffer 问题、macOS 文本输入、代码块尺寸计算等。
- 🔧 重构输入层：提取 EditPipeline、BlockEditCoordinator、FormattingStore、事件发射器等，统一 iOS 与 Android 实现。
- 🧪 测试完善：新增渲染器单元测试、Maestro e2e 测试，并更新截图。
- 📚 文档与构建：增加 iOS README 和示例应用，修复 Expo 配置插件，补充发布脚本，并支持 React Native 0.87。
- 🆕 欢迎多位新贡献者：wildseansy、yyq1025、EthanCai9568、chrfalch、slavaluka、tomekzaw、hsource、maksg、CodingItWrong。

---

### [](https://github.com/callstack/react-native-pager-view/releases/tag/v9.0.0)

**原文标题**: [Release v9.0.0 · callstack/react-native-pager-view · GitHub](https://github.com/callstack/react-native-pager-view/releases/tag/v9.0.0)

react-native-pager-view 的 v9.0.0 版本发布页面，展示了仓库概况、版本更新内容及用户互动信息，但页面加载时出现错误。

- ⚠️ 页面加载失败，提示“Uh oh!”，建议重新加载页面
- 📦 该仓库为 react-native-pager-view，拥有 3.3k Star、473 Fork、140 Issues 和 6 个 Pull Requests
- 🚀 最新版本 v9.0.0 于 8 月 11 日 13:39 发布，包含 4 个提交
- 🧩 主要更新：支持 Android Jetpack Compose（#1092）
- 📎 发布资产包含 2 个文件
- 👍 用户反馈：获得 1 个火箭表情反应

---

### [](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v3.2.0)

**原文标题**: [Release v3.2.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v3.2.0)

overview summary
react-native-gesture-handler v3.2.0 版本发布，重点引入基于 Touchable 的新 Pressable 组件、跨平台 hover 回调支持、Touchable 底层重构，以及大量错误修复与依赖更新。

- 🔄 采用 AGP v9，并实现基于 Touchable 的 `Pressable` 组件。
- 🖱️ 为 Touchable 添加 hover 回调支持（Android / iOS / Web）。
- ♻️ 在 Android、iOS、Web 上重构 Touchable，使其不再依赖 `GestureDetector`。
- 🐛 修复触摸事件序列化缺少 `allTouches` 时导致的崩溃问题。
- ⚡ 改进 Android 按钮性能：跳过不可见的下层 drawable，并按属性事务配置按钮。
- 🛠️ 修复多平台 Bug：包括 Android 的 `minDistance` 重置、iOS 的视图分离回调保证、macOS 的触摸事件传递等。
- 📚 完善文档：新增“Getting Started”页面、Touchable 部分、状态与回调流程图等。
- 🔧 更新类型定义、提取共享模块、解耦 Web 处理器，并清理过时 API 使用。
- 🤝 新贡献者 @tshmieldev 和 @hurali97 首次参与贡献。
- 📦 依赖升级：React Native 0.87，并更新多项安全相关的依赖包。

---

### [](https://github.com/software-mansion/react-native-reanimated/releases/tag/worklets-0.12.0)

**原文标题**: [Release Worklets - 0.12.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/worklets-0.12.0)

本版本为 Worklets 0.12.0，主要带来了运行时能力增强、脚本加载优化与新配置选项，并修复了多个问题。

- 🔄 Worklet 运行时现支持 `WeakRef`，通过启用 Hermes 微任务队列并在 C++ 层处理，提升资源管理能力。  
- 📦 Bundle Mode 脚本加载方式与 React Native 对齐，本地 bundle 使用 mmap，Android 开发服务器下载流式缓存，并复用 RN 已下载的 bundle。  
- 🔓 `createWorkletRuntime` 新增 `enableLocking` 选项，可创建无互斥锁的运行时，适用于能自行保证线程安全的高级场景。  
- 🛠️ 修复了多个问题：`RetainingSerializable` 竞争条件、Web 端 `scheduleOnUI` 错误、Jest mock 缺失、应用后台时 UI 循环未暂停等。  
- 🧹 清理了已废弃的 WorkletRuntime 同步 API，移除多余导入，并补充了相关文档说明。  
- 📝 改善了 `createSerializable` 的警告提示，并调整了 Release 行为的一致性。  
- 👥 本次发布由 tjzel 和 tshmieldev 贡献，完整变更见 `worklets-0.11.3...worklets-0.12.0`。

---

### [](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.6.0)

**原文标题**: [Release Release 1.6.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.6.0)

react-native-nitro-fetch 发布了 v1.6.0 版本，本次更新包含多项修复、新功能及维护性变更，共合并 10 个提交。

- 🎉 新增 tvOS 构建支持，扩展平台兼容性
- ⚙️ 新增可选项，支持退出开发工具上报（opt out of dev tools reporting）
- 🔧 修复预取缓存注册的原子性问题，避免死锁
- 🛠️ 修复 Android 上不再发送伪造的 Sec-WebSocket-Protocol 和 Origin 头
- 📱 修复 iOS 上跨 fetch 传输共享 URLCache 的问题
- 🔗 统一 iOS 和 Android 上 file:// 路径的百分号解码行为
- 🧹 移除 node_modules 并更新 lockfiles 等维护性提交
- 📦 自上一版本以来共有 10 个提交合入 main 分支

---

### [](https://github.com/JubaKitiashvili/expo-pretext/releases/tag/v1.2.0)

**原文标题**: [Release v1.2.0 — Android hotfix + measurement parity · JubaKitiashvili/expo-pretext · GitHub](https://github.com/JubaKitiashvili/expo-pretext/releases/tag/v1.2.0)

v1.2.0 是一个重要修复版本，主要解决了 Android 原生模块从未编译、Web 端字体测量错误、API 缺失导出以及断行逻辑等问题，并扩充了测试语料库，Android 实测全部通过。

- 📱 修复 Android 原生模块：补上缺失的 `android/build.gradle`，让 Expo 自动链接生效，并解决加载时 `textStyleToFontDescriptor()` 产生 `undefined` 导致的崩溃。
- 🐛 修复三个此前不可见的缺陷：合并分段被计为零宽度、CJK 单元继承零宽度父级、恰好占满一行被误判为不换行；Android 高度预测从 13/24 提升至 24/24。
- ⚠️ 重要提醒：Android 用户必须重建开发客户端，仅靠 JS 重载无法加载从未编译过的原生模块。
- 🌐 修复 Web 字体测量：Canvas 后端不再给字体族加引号，`'System'` 及 `sans-serif`/`serif`/`monospace` 等 CSS 关键字能正确识别，避免浏览器静默回退。
- 🔧 补全 `layoutNextLineRange()`、`measureLineGeometry()`、`materializeLineRange()`、`LineGeometry`、`LayoutLinesResult` 的包入口导出，此前无法导入。
- ✂️ 修复词内符号链断行问题，`#hashtag`、`mention@domain`、`foo#$bar` 不再被中间拆断。
- 📏 Android 的 `getFontMetrics()` 现在与其他后端一致，返回负的 `descender` 和真实的 `x-height`/`cap-height`，而非固定比例。
- 📦 Gradle 构建输出不再泄漏到发布的 tarball，包体更干净。
- 🧪 高度快照语料从 14 组扩至 22 组，基线从 210 行增至 435 行，并加入 keep-all 测试，能更早发现问题。
- 🙏 感谢社区贡献者 `ahundt`、`shahzaib78631` 和 `arnolicious` 的修复与报告。

---

### [发布 v0.20.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.20.0)

**原文标题**: [Release v0.20.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.20.0)

此版本为 software-mansion/argent 项目的 v0.20.0 发布说明，主要围绕流程录制与调试功能进行改进，并引入多项性能优化和 CI 质量门禁，共包含 23 个提交。

- 🚀 发布 v0.20.0，包含 23 个提交及多位贡献者
- 🌐 新增功能：在每个启动步骤启动一个 Chromium 实例
- 🔄 重构工具服务器：使用 @swmansion/argent-cloud-sdk 处理 MoQ 与输入协议
- 🎥 新增功能：支持并发流程录制
- ⏳ 新增空闲条件：等待屏幕停止移动后再继续
- 🛠️ 修复调试器：降低失败率，结构化未连接结果、分类 CDP 故障并缩小恢复范围
- 📚 文档更新：拆分 argent-create-flow 为参考，并新增 argent-qa-flows
- ⚡ 性能优化：录制器不再在每一步返回整个流程文件
- 🧪 CI 改进：添加 knip 防死代码门禁
- 👥 贡献者：j-piasecki、jwajgelt 等共 5 位开发者

---

### [](https://github.com/appandflow/react-native-safe-area-context/releases/tag/v5.9.0)

**原文标题**: [Release Release 5.9.0 · appandflow/react-native-safe-area-context · GitHub](https://github.com/appandflow/react-native-safe-area-context/releases/tag/v5.9.0)

这是 `react-native-safe-area-context` 的 v5.9.0 版本发布说明，主要针对 Web 平台修复了多个问题，并升级了构建工具。

- 🐛 修复了测量元素已分离时引发 `NotFoundError` 的问题
- 🐛 修复了嵌套的 `SafeAreaProvider` 在 Web 上无法报告自身 frame 和 insets 的问题
- 🐛 修复了 Web 上窗口大小变化时 insets 和 frame 不更新的问题
- ✨ 新特性：采用 AGP v9 构建工具

---

### [](https://expo.dev/services/tuft)

**原文标题**: [Expo Tuft](https://expo.dev/services/tuft)

Tuft 是 Expo 推出的技术预览产品：一个运行在永不休眠的专用机器上的 AI 代理，可通过 iMessage、Slack 等消息工具远程指挥它编写代码、创建 PR，让开发者不必守在笔记本前，兼顾自由与生产力。

- 🚀 Tuft 让代码能通过 iMessage 从安全专用的远程机器上发出，合上笔记本也能持续工作。
- 🤖 它被定位为“队友”而非 API，拥有独立身份、凭据、权限和完整审计记录。
- 👥 可通过 Slack 同时编排多达 15 个代理，并能在同一条 iMessage 线程中无缝切换 Claude Code 与 Codex。
- 🖥️ 随时可通过 Web 或 SSH 进入原生终端 UI，自由选用你喜欢的 CLI。
- 💬 专为异步消息场景设计，无需在旅途中解读冗长日志，像发短信一样轻松跟进任务。
- 🛠️ 提供严肃硬件选项：可运行在 Tuft 云上，也可使用专门为你配置的 Mac Mini。
- ⏰ 代理在你睡觉时继续工作，完成后再 ping 你，节省等待时间。
- 🔐 安全从第一原则出发：像对待实习生一样，只给代理完成任务所需的最小权限。
- 🌄 团队相信最佳创意常产生于离开办公桌时——Tuft 负责把想法快速变成 PR。
- 📋 当前为早期技术预览，团队欢迎开发者加入等待列表并共同塑造未来。

---

### [](https://github.com/margelo/ai-chat-demo)

**原文标题**: [GitHub - margelo/ai-chat-demo: A ChatGPT-style mobile chat app in React Native with context about Margelo · GitHub](https://github.com/margelo/ai-chat-demo)

这是一个开源的 ChatGPT 风格移动聊天应用，基于 React Native 构建，集成了 RAG 知识库，能够流式回答关于 Margelo 的问题并展示推理过程。

- 🧠 核心机制：使用 OpenAI Responses API 通过 WebSocket（react-native-nitro-websockets）流式传输，Socket 在应用启动时原生预热，支持 token 级流式输出和对话记忆（previous_response_id）。
- 📚 知识库（RAG）：模型可调用 search_margelo_kb 工具，通过 react-native-nitro-fetch 查询 Pinecone 向量数据库；仅基于检索到的上下文回答 Margelo 相关问题，不依赖模型记忆。
- 💬 渲染体验：回复以原生 Markdown 呈现（react-native-enriched-markdown），支持流式动画、可点击链接，并可通过底部表单（react-native-true-sheet）展示可折叠的“思考过程”。
- 📜 列表交互：采用 @legendapp/list 实现键盘感知和锚点定位，模拟 ChatGPT 的滚动与锚定行为，适合流式回复场景。
- 🎨 视觉效果：iOS 26+ 使用 @callstack/liquid-glass 实现真实 Liquid Glass 表面，其他平台回退为普通圆角；Skia 实现“Thinking”闪烁标签；图标使用 SF Symbols 并在 Android 上回退到 Material Design Icons。
- 🖼️ 附件支持：通过 react-native-image-picker 选择图片，以 base64 数据 URL 发送，并用 react-native-nitro-image 显示缩略图。
- 📱 运行要求：支持 iOS 和 Android（新架构），需要 Xcode + CocoaPods、Node >=22.11、React Native 环境、OpenAI API key 以及已填充的 Pinecone 索引。
- ⚠️ 安全注意：这是演示项目，API 密钥内置于应用包中，仅适合本地使用；生产环境务必通过中继服务器保护密钥。
- 🛠️ 设置与脚本：安装依赖、复制 config.example.ts 为 config.ts 并填写密钥、执行 pod install 后即可运行；提供 lint、typecheck、format、react-compiler-check 和 jest 等 CI 脚本。
- 📁 项目结构：代码清晰分区，包含状态管理（zustand）、OpenAI 协议处理、RAG 搜索、hooks、screens 和可复用 components。
- 🙏 开源致谢：依赖多个优秀开源库，如 Nitro Modules、Reanimated、Skia、LegendList、Liquid Glass 等，感谢所有作者。

---

### [](https://github.com/joshuayoes/ios-simulator-mcp/releases/tag/v2.1.0)

**原文标题**: [Release v2.1.0 - App Lifecycle Tools 📱 · joshuayoes/ios-simulator-mcp · GitHub](https://github.com/joshuayoes/ios-simulator-mcp/releases/tag/v2.1.0)

iOS Simulator MCP 2.1.0 版本发布，重点新增应用生命周期管理工具、命令行改进、文档更新与版本升级。

- 📱 新增 `terminate_app` 工具：通过 bundle identifier 终止运行中的应用，支持冷启动/热启动测试、重置状态及崩溃恢复流程，并在应用未运行时返回友好错误提示
- 🔗 新增 `open_url` 工具：可在模拟器中打开任意 URL 或深链接，涵盖 https 网页、自定义 URL scheme（如 `myapp://profile/123`）、通用链接及 OAuth 重定向流程
- 📋 新增 `list_apps` 工具：以 `name — bundleId` 格式列出全部已安装应用，便于在调用 `launch_app` 或 `terminate_app` 前发现标识符；通过 `plutil -convert json` 解析 `simctl listapps` 输出，兼容不同 Xcode 版本格式
- ⚙️ 命令辅助功能新增可选 stdin 输入支持：用于 `list_apps` 的 plutil 数据转换，且所有命令执行统一走 `execFile` 路径，具备输出上限和一致错误处理
- 📄 新增 TESTING.md 文档：说明项目实际验证流程（PR 审查 harness、严格 MCP 配置隔离、发布后冒烟测试及已知风险）；QA.md 重写为面向 Settings app 的版本无关发布场景
- 🧪 QA.md 新增脚本化场景，端到端演练三个新工具；README 补充 `terminate_app`、`open_url`、`list_apps` 参数参考
- 🔨 项目版本号已提升至 2.1.0，并包含已签名提交验证

---

### [](https://www.youtube.com/watch?v=eiGcqvji4nk)

**原文标题**: [Can a Specialized Model Beat Frontier Models at React Native? - YouTube](https://www.youtube.com/watch?v=eiGcqvji4nk)

概述摘要：这是 YouTube 页面底部常见的信息链接集合，涵盖版权、联系方式、创作者服务、广告合作、开发者选项、法律条款及隐私安全等内容。
- 📋 提供关于页面、新闻媒体联系方式及版权声明信息
- 📞 展示用户联系渠道与创作者支持入口
- 📢 包含广告合作与开发者资源选项
- ⚖️ 列出服务条款、隐私政策及平台安全规则
- 🔍 说明 YouTube 功能测试与平台运作方式
- 🗓️ 标注版权归属及年份（© 2026 Google LLC）

---

### [React Native Radio - RNR 369 - RNR 解释：AppRegistry](https://infinite.red/react-native-radio/rnr-369-rnr-explains-appregistry)

**原文标题**: [React Native Radio - RNR 369 - RNR Explains: AppRegistry](https://infinite.red/react-native-radio/rnr-369-rnr-explains-appregistry)

这段内容来自 React Native Radio 播客第 369 集，Robin Heinze 与 Tyler Williams 深入浅出地讲解了 React Native 中 AppRegistry 的运作原理、常用方法，以及它在原生应用集成（brownfield）、后台任务和 Expo 等场景中的实际应用。

- 🎙️ 主持人 Robin Heinze 与 Tyler Williams 共同解释 AppRegistry 的作用，帮助开发者理解这个日常却少被深究的 API。
- 📱 AppRegistry 的核心功能是将 React 根组件注册到原生应用，通常在 index.js 或 App.js 中通过 `registerComponent` 调用。
- 🔧 `registerRunnable` 是更底层的注册方式，适合运行非组件逻辑，例如启动器、端到端测试或决定当前挂载哪个应用。
- 🔑 `getAppKeys` 返回所有已注册的 key，常用于 brownfield 应用——即在原生应用中嵌入多个独立的 React Native 界面。
- ▶️ `runApplication` 负责真正启动已注册的应用，一般由原生端或内部机制调用，开发者很少直接使用。
- ⚙️ `registerHeadlessTask` 可在 Android 后台运行无 UI 的 JavaScript 任务，如持续上传 GPS 坐标、处理后台消息；iOS 上则需使用 `registerRunnable`。
- 🧩 `setWrapperComponentProvider` 可为所有注册组件统一包裹 Provider（如 Redux、主题），方便共享状态或上下文，非常适合 brownfield 场景。
- 📚 阅读官方文档能发现日常使用中忽略的功能，即使是最常见的 API 也有更多用途，有助于提升开发信心。
- 💼 本集由 Infinite Red 赞助，该公司专注于 React Native 和 Expo 应用开发，并提供相关咨询服务。

---

### [](https://infinite.red/react-native-radio/rnr-370-copilotkit-with-mike-ryan)

**原文标题**: [React Native Radio - RNR 370 - CopilotKit with Mike Ryan](https://infinite.red/react-native-radio/rnr-370-copilotkit-with-mike-ryan)

本期节目邀请 CopilotKit 首席架构师 Mike Ryan，探讨如何将 AI 代理接入 React Native 应用，重点介绍了 AG-UI 协议、生成式 UI 的不同实现方式、共享状态与安全边界，以及 CopilotKit 的现状和未来规划。

- 🤖 CopilotKit 是一套 SDK，用于构建“代理前端”，让 AI 响应不仅输出文本，还能渲染交互式 UI。
- 🔄 AG-UI 是开放协议，标准化代理到任意前端界面的流式通信，解决 SSE 流、状态持久化和重连等问题。
- 🧩 AG-UI 与 MCP 互补：MCP 让代理调用外部工具，AG-UI 则负责把代理步骤和响应实时传给界面；CopilotKit 也支持 MCP 与 MCP Apps。
- 🎨 生成式 UI 分为三种：完全受控（通过 useComponent 暴露开发者定制的组件）、声明式（借助 A2UI 由代理从组件目录组装界面）、完全开放式（iframe 内动态生成 HTML/CSS/JS）。
- 💾 AG-UI 支持共享状态，前端组件可直接读写代理状态，实现用户与 AI 之间的双向协作，比如选择菜单或确认操作。
- 🛡️ 安全边界很关键：此类技术适合信息检索与展示，但若涉及真实世界决策，应结合“人类介入”机制，让用户批准工具调用后再执行。
- 📱 典型移动场景包括医疗报告问答与图表可视化、根据用户偏好个性化过滤菜单等。
- ⚛️ CopilotKit 的 React Native SDK 目前以无头 API 形式提供，兼容 Expo，基于 MIT 开源，并期待社区贡献更多内置组件。
- 🚧 React Native 适配中曾遇到 UUID 生成、SSE 流处理与 Fetch 差异等挑战，但 SDK 已封装解决，开发者可直接使用。
- 🔮 未来计划将 AG-UI 代理带到 Slack、Teams、Discord、WhatsApp 等平台，并强化用户记忆与个性化学习能力。

---

### [CSS：收件箱里的炸弹 | PortSwigger Research](https://portswigger.net/research/css-the-bomb-inside-your-inbox)

**原文标题**: [CSS:the bomb inside your inbox | PortSwigger Research](https://portswigger.net/research/css-the-bomb-inside-your-inbox)

这项研究由 PortSwigger 的 Gareth Heyes 完成，系统性地探讨了如何利用 CSS 攻击 Webmail 客户端，涵盖信任边界绕过、令牌窃取、CSS 清理器绕过、图像代理绕过、CSS 突变、UI 欺骗和密码窃取等技术与实际利用，并提出了防御措施与未来攻击方向。

- 📧 研究发现 Webmail 客户端中广泛存在 CSS 清理不严问题，可被用于窃取令牌、劫持 UI 甚至控制 AI 浏览器。
- 🏷️ 利用 HTML `<label for>` 可控制页面 UI 元素，例如在 Outlook 中固定邮件或打开工具栏，且 Microsoft 至今未修复。
- 🤖 通过 `:before`/`:after` 伪元素隐藏文本，可对 AI 浏览器（如 OpenAI Atlas）执行间接提示注入，诱导其自动打开恶意标签页。
- 📋 利用剪贴板粘贴时的 CSS 竞态条件（Firefox 尤甚），可窃取 Medium 等网站的 12 位十六进制登录令牌，且 Yahoo Mail 和 AOL Mail 同样受影响。
- 🔒 即使 CSP 阻止外部资源，仍可通过字体高度预言与动画组合，利用数字频率和 `inset` 属性实现令牌外泄。
- 🧪 发现多种 CSS 外部请求语法，包括 `image-set()`、`@import`、sourceMappingURL 等，可用于绕过清理器或图像代理。
- 🖼️ 图像代理可被 CSS 转义或特殊语法绕过，从而在 Fastmail、ProtonMail 和 Gmail 中追踪邮件是否被阅读，甚至显示受害者 IP。
- 🧬 CSSOM 解析可导致 CSS 突变：浏览器会解码转义字符，使原本安全的 CSS 变成恶意代码，影响 Fastmail 等基于 CSSOM 过滤的客户端。
- 🧩 Outlook 的 CSS gadget 允许通过自定义 data 属性注入 `position:fixed`，从而突破邮件信任边界并篡改整个页面。
- 🖱️ CSS hotwiring 技术可利用 `:before` 伪元素覆盖全屏，让受害者在任意点击时触发 VIP、侧边栏等非预期 UI 操作。
- ⌨️ 作者构造出可在 Outlook（DOMPurify + CSS 清理）中运行的密码键盘记录器，并通过 Firefox 的 select 行为实现实时按键窃取。
- 🛡️ 防御建议包括使用沙箱 iframe 严格隔离邮件、阻止图片请求和 select 菜单、限制危险选择器及自定义属性，并避免使用攻击者可控的域名。
- 🔮 未来攻击包括利用 Chrome 的 `selectedcontent` 实现纯 HTML 键盘记录器，以及使用 interest invokers 在 Chrome 中构建实时键盘记录器。

---

### [](https://green.sapphi.red/blog/how-variable-mangling-works-in-oxc-minifier)

**原文标题**: [How Variable Mangling Works in Oxc Minifier | green.sapphi.red](https://green.sapphi.red/blog/how-variable-mangling-works-in-oxc-minifier)

概述：本文介紹 Oxc Minifier 中變數名稱混淆（variable mangling）的實作原理，涵蓋其目標、基本步驟（生存性計算、槽位分配、名稱生成）以及背後的數學演算法（弦圖與完美消除順序），並說明如何兼顧程式碼縮減與語意保留。

- 🌐 變數混淆是透過將變數名稱替換為更短名稱來縮減程式碼大小，例如 `foo` 改為 `a`，同時須確保不改變程式語意。
- 🧩 核心策略包括「盡量重用相同變數名稱」與「使用最短名稱」，並特別最佳化 gzip 等壓縮後的體積。
- 📊 步驟一：計算每個符號的「生存性」（liveness），即該變數可被參考的 scope 集合，例如 `total` 可存在於父層與兩個 if 區塊中。
- 🗂️ 步驟二：引入「槽位」（slot）概念，將生存性不重疊的變數分配到同一槽位，使它們可共用相同名稱；優先處理較外層 scope 的變數以利重用。
- ✏️ 步驟三：依字元頻率順序（如 `e`, `t`, `n` 等）生成短名稱，並根據變數出現頻率決定名稱長度，一字符優先給最常出現的槽位。
- 🧬 從數學角度看，變數生存性形成 scope 樹的子樹，槽位分配可轉化為弦圖（chordal graph）的最小著色問題，能多項式時間求解。
- 🔄 Oxc Minifier 的處理順序（由淺層至深層）正好是弦圖的「完美消除順序」反向，因此貪婪著色可達到最少槽位數，即最佳解。
- 💡 實務上需額外處理須保留原名稱的變數，但上述機制是 Oxc Minifier 變數混淆的核心；作者也坦言是先直覺實作後才理解其理論基礎。

---

### [](https://nodejs.org/en/blog/release/v26.7.0)

**原文标题**: [Node.js — Node.js 26.7.0 (Current)](https://nodejs.org/en/blog/release/v26.7.0)

Node.js 26.7.0（Current）于 2026-08-05 发布，由 Antoine du Hamel 负责。本次更新引入多项新特性，包括 crypto 私钥 STORE 加载、perfetto 支持、ModuleHooks 的 Symbol.dispose、test_runner 覆盖率新选项，并伴随大量依赖升级和 bug 修复。

- ✨ **新特性**：crypto 支持通过 STORE loaders 加载私钥；lib 新增 perfetto 支持；ModuleHooks 实现 Symbol.dispose；test_runner 新增 `--test-coverage-include-all` 选项。
- 🔐 **Crypto 安全与修复**：根证书更新至 NSS 3.125；修复 Argon2 绕过 FIPS 模式、KDF 错误保留、私钥生成选项验证及多项错误处理问题。
- 📦 **依赖升级**：npm 升级至 11.19.0，并更新 V8、sqlite、nghttp2/nghttp3、zlib、ada、simdjson 等多个核心依赖。
- 🌐 **HTTP/网络改进**：修复 writableFinished 与 'finish' 事件、IncomingMessage 信号中止问题；HTTP/2 减少分配但部分改动已回滚；net 支持 Windows TCP handle 转移及 AF_UNIX 路径。
- 🐛 **FFI 修复**：修复回调崩溃、快速调用参数验证、字符串保留、ppc64 跳板寄存器及优化缓冲区转换等问题。
- 🧪 **测试与构建**：test_runner 新增全覆盖支持；修复多个测试稳定性问题；构建系统加入 perfetto CI 并提升 Rust 要求至 1.86。
- 📚 **文档与类型**：大量文档改进，包括 stream.isDestroyed()、`--permission-audit` 行为、`--disable-warning` 稳定性；typings 补充 heap_utils 等类型。
- 🔧 **其他修复**：sqlite 修复会话生命周期与 use-after-free；quic 修复分段 client hello 崩溃与 stop sending 行为；permission 支持 v8.setHeapSnapshotNearHeapLimit。
- 📦 **发布物**：提供 Windows、macOS、Linux、AIX 多平台安装包与二进制，并附 SHA256 校验和及 PGP 签名。

---

### [Astro 7.2 | Astro](https://astro.build/blog/astro-720/)

**原文标题**: [Astro 7.2 | Astro](https://astro.build/blog/astro-720/)

概述：Astro 7.2 发布，带来实验性增量静态构建、会话支持可关闭、预览后台模式及相对日志入口等新功能，并包含社区贡献与升级指引。

- 🧱 实验性增量静态构建：通过 `experimental.incrementalBuild` 启用，路由可利用 `cacheKey`（如内容摘要）跳过未变化页面的重新生成，显著提升大型静态站点构建速度。
- 🔑 缓存键机制：`getStaticPaths()` 返回 `cacheKey`，Astro 同时哈希模块图，两者均匹配时才复用旧页面；未设置的路由始终重新渲染，现有项目行为不变。
- 🚫 会话支持可完全关闭：新增 `session: false` 配置，移除 SSR 中的会话运行时并跳过适配器默认驱动，减少冷启动解析开销，未配置驱动时也会自动摇树移除。
- 🖥️ 预览服务器后台模式：`astro preview --background` 支持后台运行，配合 `status`、`logs`、`stop` 子命令管理，与 `astro dev` 行为一致，方便 AI 代理使用。
- 📄 相对日志入口：`logger.entrypoint` 现在可直接使用相对字符串路径（如 `'./src/custom-logger.js'`），无需 `new URL` 包装，URL 形式仍兼容。
- ⬆️ 升级方式：推荐使用 `npx @astrojs/upgrade` 自动升级，也可通过 npm/pnpm/yarn 手动安装最新版。
- 🙌 社区致谢：感谢核心团队及大量外部贡献者，并欢迎通过 Discord、GitHub、社交媒体反馈问题。
- 🛒 周边商品：官方商店推出定制衬衫、贴纸、帽子等，支持项目发展。

---

### [pnpm 12 有什么不同 | pnpm](https://pnpm.io/blog/whats-different-in-pnpm-12)

**原文标题**: [What's different in pnpm 12 | pnpm](https://pnpm.io/blog/whats-different-in-pnpm-12)

overview summary  
pnpm 12 是用 Rust 重写的发布候选版，兼容 pnpm 11 的命令、设置和 lockfile 格式，但带来五个关键变化：全局二进制感知项目版本、Git 依赖解析统一、包管理器命名行为修正、循环依赖 lockfile 确定性，以及移除 `--resolution-only` 标志。升级不算迁移，现有项目可平滑过渡，但需注意个别破坏性变更。

- 📦 **项目感知的全局二进制**：全局安装的 `node`、`deno`、`bun` 现在会优先运行当前项目固定的版本（通过 `devEngines.runtime` 或作为依赖安装），由 `globalShims` 设置控制；项目外仍使用全局版本，无需额外版本管理器。
- 🔀 **Git 依赖解析统一**：对 GitHub、GitLab、Bitbucket，所有 specifier 形式（如 `owner/repo`、`github:`、`git+https:`、`git+ssh:`）都视为同一依赖，统一通过规范的 HTTPS URL 解析；旧 lockfile 中的 SSH 条目需用 `pnpm update <package>` 一次性重新解析；私有仓库改用 Git 的 `insteadOf` 配置，pnpm 不会记录 SSH URL。
- 🧰 **包管理器命名修正**：`pnpm add yarn` 现在安装真正的 Yarn（而非 npm 包）；`pnpm add -g node/deno` 安装实际运行时；`pnx yarn@4`、`pnx node@22` 可直接运行指定版本；git 托管的依赖会用其要求的包管理器准备；`pnpm shim add yarn` 可创建跟随项目版本的命令，避免遮蔽 PATH。
- 🔁 **循环依赖 lockfile 确定性**：按包 ID 固定断开循环，lockfile 只由依赖图决定，重排 workspace 顺序、`package.json` 条目或重复安装都会产生字节相同的 lockfile；循环重的 workspace 解析 peers 快 2–3 倍、内存少 25%、lockfile 更小；现有 lockfile 可继续使用，但首次重新解析会有一次性 diff。
- ❌ **移除 `--resolution-only`**：该标志在 pnpm 12 中不存在，直接报错；替代方案是 `pnpm peers check`，它直接从 lockfile 读取 peer 依赖问题，无需重新解析或安装，CI 脚本需特别注意这一破坏性变更。
- 🚀 **尝试安装**：pnpm 12 以 `next-12` 标签发布在 npm 和 GitHub prerelease，Homebrew、winget、Scoop、Chocolatey 尚未提供，可通过官方文档的 RC 安装方式试用并反馈问题。

---

### [迁移指南 | 指南 | Vitest](https://main.vitest.dev/guide/migration.html#vitest-5)

**原文标题**: [Migration Guide | Guide | Vitest](https://main.vitest.dev/guide/migration.html#vitest-5)

overview summary
Vitest 5.0 迁移指南涵盖了环境要求、若干破坏性变更、默认值调整、API 重写与包弃用，并提供了从 Jest 和 Mocha+Chai+Sinon 迁移的说明。升级前需重点注意 mock 行为、配置继承、浏览器模式、覆盖率与报告路径等变化。

- 🚀 环境要求：需要 Vite >= 6.4.0 和 Node.js >= 22.12.0
- 🧹 `clearMocks` 默认开启，每个测试前自动清除 mock 的调用记录，但保留实现
- 🏷️ `testNamePattern`（`-t`）现在匹配用 ` > ` 连接的完整测试名
- 🧩 内联项目默认继承根配置（`extends` 默认为 `true`），数组选项会合并而非覆盖
- 📁 被引用配置文件中的 `projects` 字段生效，可声明嵌套项目
- ⚡ 内联项目默认共享 Vite 服务器，以加快测试；可用 `sharedViteServer: false` 关闭
- 📌 `vi.mock`、`vi.unmock`、`vi.hoisted` 必须在模块顶层调用，嵌套调用会抛错
- 🕷️ 浏览器模式下 automock 模块继续使用自动生成的 stub；如需原实现可传 `{ spy: true }`
- 🐕 类 mock 现在会链接到原型的 prototype，`instanceof` 和原型方法正常可用
- 📊 Benchmark API 重写：`bench` 不再从 `vitest` 顶层导入，改为从测试上下文获取
- 🔐 Vitest UI 必须通过带 token 的 URL 进行认证访问
- 🕰️ 假定时器与 `setSystemTime` 现在也会模拟 `Temporal` API
- 🎯 `toThrow("")` 现在匹配任意错误消息（空字符串视为子串），不再只匹配空消息
- 📋 断言类型新增 `R`（返回类型）和 `T`（接收类型）两个类型参数
- ⏳ `expect.poll` 超时后会失败，回调可接收 `AbortSignal`
- ⚠️ 未 await 的异步断言（如 `resolves`、`rejects`）现在会导致测试失败
- 🎨 测试标题与检查值改用 `pretty-format` 格式化，部分快照可能需要更新
- 🗑️ 移除 `test.sequential`、`describe.sequential` 和 `sequential` 选项，改用 `concurrent: false`
- 🖱️ 浏览器 locator 现在序列化为对象（包含 `selector` 和 `locator`），默认严格匹配文本
- 📝 `toHaveTextContent` 改为严格相等；正则/部分匹配请使用新的 `toMatchTextContent`
- ⏳ `vitest-browser-vue` 和 `vitest-browser-svelte` 的 `render` 变为异步，需要 `await`
- 📈 覆盖率 glob 阈值的 `perFile` 不再继承顶层配置；`include`/`exclude` 匹配规则更精确
- 📂 不再从父目录自动查找配置文件，需用 `--config` 显式指定
- 🌐 DOM 环境中对 `globalThis`/`window` 的赋值会同步到底层 DOM 实现
- 🔧 `populateGlobal` 返回的描述符需用 `Object.defineProperty` 恢复原值
- 🌐 浏览器 orchestrator URL 必须包含 `sessionId`；`browser.api` 已弃用，改用顶层 `api`
- 📁 报告和产物统一输出到项目根目录的 `.vitest` 下；`json`/`junit` 默认写入文件而非 stdout
- 🖼️ `toMatchScreenshot` 引用截图使用独立的 `screenshotDirectory` 配置
- 🔢 Worker 和并发 ID 从 1 开始，`VITEST_POOL_ID`/`VITEST_WORKER_ID` 值随之变化
- ⚙️ `resolveConfig` 直接返回已解析的 Vite config，Vitest 配置位于 `viteConfig.test`
- 📦 `@vitest/runner`、`@vitest/ws-client` 弃用；WebdriverIO provider 迁移至 vitest-community
- 🚫 移除多个废弃入口点，如 `vitest/coverage`、`vitest/reporters`、`vitest/snapshot` 等
- 🔁 从 Jest 迁移：globals 默认关闭，`mockReset` 行为不同，`mock` 状态持久，模块 mock 需返回对象，`requireActual` 改用 `vi.importActual`，`done` 回调需改用 async/await
- 🧪 从 Mocha+Chai+Sinon 迁移：测试结构基本一致，支持 Chai 风格断言，`vi.fn`/`vi.spyOn` 替代 spy/stub，定时器基于 `@sinonjs/fake-timers`

---

### [未找到标题](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)

**原文标题**: [No title found](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)

请提供您希望我总结的文章内容，我会按照要求的格式（先总览概述，再用带 emoji 的“-”项目符号列出要点）用中文为您总结。

---

### [](https://svelte.dev/blog/sveltekit-3-release-candidate)

**原文标题**: [The SvelteKit 3 Release Candidate is here](https://svelte.dev/blog/sveltekit-3-release-candidate)

SvelteKit 3 进入候选发布阶段，在配置、别名、TypeScript、Service Worker、环境变量、错误处理、路由及构建工具等方面做出多项关键更新，并引入实验性远程函数。

- 🚀 SvelteKit 3 现已进入 RC 阶段，若测试顺利将很快推出稳定版，不再引入破坏性更改。
- 🔧 现有项目可通过 `npx sv@next migrate sveltekit-3 --tasks all --confirm` 自动迁移并生成待办清单。
- 🆕 创建新应用使用 `npx sv@next create my-new-app`。
- 📁 配置从 `svelte.config.js` 移至 `vite.config.ts`，统一配置入口，简化异步解析。
- 🔗 共享代码别名由 `$lib` 改为 `#lib`，采用 Node 子路径导入，需携带文件扩展名。
- 🗂️ TypeScript 配置更简单：改为扩展 `$app/tsconfig`，并需显式指定 `include`/`exclude`（含 service worker）。
- ⚙️ Service Worker 重构：可直接从 `$app/env`、`$app/paths`、`$app/manifest` 导入，并可通过 `$app/service-worker` 获取 `self` 类型。
- 🔐 环境变量功能增强：通过 `src/env.ts` 声明依赖，支持公开/私有、构建时/启动时解析、类型安全及 Standard Schema 校验。
- 🛡️ 错误处理大幅改进：基于 Svelte 5 错误边界，所有错误（含 `error()` 主动抛出）都经过 `handleError`，并附带 sourcemap 堆栈跟踪。
- 🧭 浅路由改为 `goto` 的 `shallow: true` 选项，并支持 `persistState: true`，同时会触发导航钩子。
- ⚡ 强制要求 Vite 8，借助 Rolldown 获得更快构建，并采用 Environment API；不支持 FetchableDevEnvironment。
- 🔮 远程函数仍处于实验阶段，被视为未来客户端与服务器通信的核心方案，官方正在积极完善。
- 📣 官方鼓励用户升级测试并反馈意见和 bug。

---

