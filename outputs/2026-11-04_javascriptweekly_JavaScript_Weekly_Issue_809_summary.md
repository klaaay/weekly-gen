### [](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)

**原文标题**: [The AI cost of JavaScript frameworks | Read the Tea Leaves](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)

overview summary
- 🧭 作者批评前端技术选型常靠“感觉”，于是设计基准来检验 AI 编码时代不同 JavaScript 框架的实际表现。
- 🧪 方法是用 PokéAPI 构建一个小型但非平凡的宝可梦应用，让 Opus 5.5 以高 effort 使用各框架最新版生成；每个框架跑 5 次取中位数，Angular 部分指标因两次失败只取 3 次。
- 🛡️ 为防代理“作弊”，作者用基于可访问性树的规范符合性测试验证输出，并禁止预生成静态 HTML；同时未强制 SSR/CSR 或 CSS 方法论，只要求不用 Tailwind/Bootstrap 等组件框架。
- 💵 建造成本最低的是 Hono+htmx（$2.67）、Astro（$2.76）、Nuxt（$2.82）；较高的是 SvelteKit（$4.28）、Gracile+Lit（$4.65）、Angular（$4.97）。
- ⏱️ 构建时间最快为 Astro 8.2 分钟，其次 Hono+htmx 8.6、Nuxt 9.0；Angular 17.2 分钟最慢。Token 消耗 Nuxt 3.85M 最低，Angular 9.76M 最高。
- 🧠 MCP/skills 的使用很不一致且未必有效：Nuxt MCP 从未被使用，Next.js 技能文件仅 1/5 次读取，TanStack Start 技能文件仅 2/5 次被发现；作者怀疑当前 MCP/skills 可能弊大于利。
- 📊 Lighthouse 的 Performance、Accessibility、CLS 几乎饱和：多数框架 Performance 为 100 或 99、Accessibility 为 100、CLS 为 0；Vanilla 的 CLS 0.111 是例外。
- 📦 JS 传输字节差异明显：Astro 0 KiB、Vanilla 7 KiB、Gracile+Lit 8 KiB、Hono+htmx 18 KiB 较低；Next.js 142 KiB、TanStack Start 118 KiB、React Router 115 KiB 较高。
- ⚡ TBT 上 Astro、Gracile+Lit、Hono+htmx、SvelteKit、Vanilla 约为 0 ms；Angular 103 ms、Next.js 71 ms、Nuxt 40 ms 较高。LCP 总体奖励 MPA、惩罚 SPA：Astro 810 ms 最好，Next.js 2090 ms 最差，但波动很大。
- 📝 代码行数最少的是 Hono+htmx 1370 行，其次 Nuxt 1415、Astro 1461；Angular 2009 行最多。作者强调代码量会影响未来编辑的 token 成本和长期维护成本。
- ⚠️ 基准有局限：应用类型单一、LLM 与 Lighthouse 结果随机性大、Core Web Vitals 对 SPA 不利；Angular 有两次 SSR 应用拒绝非 localhost，未重跑，仅影响性能和代码量指标。
- 🧩 结论是应基于证据而非“感觉”选择框架；作者不试图妖魔化任何框架，而是希望推动更快、更可访问的 Web 体验，并提醒在 AI 编码时代重新审视 `npm install` 后的技术栈选择。

---

### [错误](https://gautamparab.com/writing/sixty-of-sixty-six-ranges-overlap/)

**原文标题**: [Error](https://gautamparab.com/writing/sixty-of-sixty-six-ranges-overlap/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='gautamparab.com', port=443): Max retries exceeded with url: /writing/sixty-of-sixty-six-ranges-overlap/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [GitHub - nolanlawson/agent-framework-benchmark：针对示例应用的 JavaScript 框架与 Claude Token 使用量的实验性基准测试 · GitHub](https://github.com/nolanlawson/agent-framework-benchmark)

**原文标题**: [GitHub - nolanlawson/agent-framework-benchmark: Experimental benchmark of JavaScript frameworks and Claude token usage on a sample app · GitHub](https://github.com/nolanlawson/agent-framework-benchmark)

该项目是一个实验性基准，用来比较不同 JavaScript 框架下，Claude 编码代理构建同一个非平凡 Web 应用所需的 token、时间，以及最终应用的性能；所有代理使用相同规格、测试、工具和提示词，仅框架不同。

- 🧪 基准应用是一个由本地 PokeAPI 支持的 Pokédex，代理需实现 `SPEC.md` 并通过 `npm test`。
- 📦 覆盖框架包括 Next.js、Nuxt、TanStack Start、React Router、SolidStart、SvelteKit、Angular、Astro、Qwik、Gracile、Hono + htmx 和 vanilla。
- 🐳 每个代理在全新的 Podman 容器中独立运行，构建出的应用再在另一个容器中用 Lighthouse 测量。
- ⚙️ 运行要求 Linux、Podman 4.3+、Node 20+、约 15 GB 磁盘和 Claude 凭据；支持单框架或全框架、多次迭代运行。
- 📊 结果写入 `runs/<timestamp>/report.md`，包含 Lighthouse 指标、代码行数、token 使用和每次迭代的详细数据。
- 🗂️ 约 2 GB 的 Pokémon 数据只在构建 `pokedex-base` 镜像时下载一次，代理不会重复下载，也不消耗 token。
- 🔐 凭据通过 `ANTHROPIC_API_KEY` 或 `CLAUDE_CODE_OAUTH_TOKEN` 传入容器，不写在命令行或运行目录中，建议使用有限额的密钥。
- 🧱 运行会构建 `pokedex-base`、`pokedex-agent`、`pokedex-measure` 三类镜像；代理只能看到导出的干净仓库，无法看到 gold 实现和测量代码。
- ✅ 代理完成后，仅其 `app/` 会被复制到全新基础容器中运行最终测试，避免测试、数据或后台进程影响结果。
- 🚀 测量阶段以生产模式通过 Caddy 提供 HTTPS/HTTP2 服务，对 6 个 URL 做移动端 Lighthouse 测试，取多次运行中位数，并预热服务端缓存。
- 🧠 每个框架会预装其官方推荐的 AI 工具；工具支持不均衡本身就是基准的一部分，例如 Next.js、Nuxt、Astro、SvelteKit、Angular、React Router 有官方工具，而 SolidStart、Qwik、Gracile、vanilla 基本没有。
- 📝 统一提示词要求使用指定框架的最新稳定版，自主工作直到 `npm test` 通过；代理是否使用 MCP、skill 等会记录在 transcript 中。
- ⏱️ 可通过 `bench/tokens.mjs` 汇总单个 transcript 的 token 使用；报告还会统计应用源码的非空行数。
- 📌 设计上要求数据实时从 API 获取，禁止构建时静态生成数据页；不人为增加 API 延迟；只测量页面加载，不测量加载后的交互。
- ⚖️ 该站点内容密集，首屏指标更有利于服务端渲染的 MPA；样式受共享设计令牌、系统字体、无 CSS 框架和动画等约束，以减少视觉差异干扰。
- ⚠️ 单次迭代波动很大，应至少运行 3 次再下结论；测试对 shadow root 内文本的检查存在已知限制。
- 🔧 项目为 AI 生成，PR 已关闭；作者更希望用户提 issue、fork 或用自己的 token 继续实验。

---

### [构建本地 AI 编码工作流 | Master.dev](https://master.dev/courses/local-ai/?utm_source=email&utm_medium=javascriptweekly&utm_content=localaicooper)

**原文标题**: [Build a Local AI Coding Workflow | Master.dev](https://master.dev/courses/local-ai/?utm_source=email&utm_medium=javascriptweekly&utm_content=localaicooper)

overview summary
本课程（约 4 小时 3 分钟，评分 4.9）讲解如何用本地模型搭建私有、零单 token 成本、不受厂商限速或停服影响的 AI 编码环境，涵盖 LM Studio、模型与量化选择、硬件适配、VS Code/终端代理集成及远程访问。

- 🧠 本地模型已能胜任日常编码，核心优势是代码隐私、零 token 成本、完全自主控制与可微调。
- 🛠️ 从安装 LM Studio、开启开发者模式、加载小模型并本地对话开始实践。
- 🔍 讲解 LLM 基础：权重、训练与推理、token、上下文记忆，以及温度、Top P、Top K、seed 对输出随机性的影响。
- 💻 硬件重点是 CPU、GPU、内存；Nvidia CUDA GPU 更适合 AI，模型尽量完整放入显存以避免明显降速。
- 🧩 在 Hugging Face/LM Studio 找模型时，要关注模型家族、命名、参数、任务、格式、量化来源和评测结果；Mac 优先 MLX，通用场景常用 GGUF。
- 🎯 模型可按能力分为通用/编码、instruct、reasoning、vision、tool calling、embedding/reranker；MOE 通过路由提升推理速度。
- ⚙️ 量化用更少比特表示权重（FP32/FP16/Q8 等），可降低文件与内存占用但影响质量；上下文越大，内存需求越高。
- 📈 评估本地推理看加载时间、首 token 时间、每秒 token 数和内存占用；建议用固定提示对比模型与量化，再长期试用判断质量。
- 🔌 可将 LM Studio 设为本地服务器，推荐 OpenAI 兼容 chat completions，并接入 VS Code 扩展、JSON 自定义 provider 或 Pi 终端编辑器。
- 🌐 远程访问可用 LM Link 或 Tailscale 私有网络；租用云端 GPU 可运行开放权重模型，但会牺牲本地隐私换取硬件灵活性。
- ✅ 结课框架：结合模型家族、量化与系统内存选型；可从 Qwen 小模型起步，再按硬件逐步试用更大模型。

---

### [为什么这个指纹识别脚本在制造生物武器？](https://nullpt.rs/fingerprinting-bioweapons)

**原文标题**: [Why Is This Fingerprinting Script Creating Bioweapons?](https://nullpt.rs/fingerprinting-bioweapons)



---

### [指纹花园](https://fingerprint.garden/)

**原文标题**: [fingerprint.garden](https://fingerprint.garden/)

该内容呈现的是一个面向脚本与浏览器工件分析的仪表盘界面，包含家族筛选、交付方式、站点观察、来源比对、常量与浏览器 API 搜索等功能，但当前无画布数据可显示。

- 📅 界面日期为 2026 年 10 月 26 日，覆盖“所有家族”，并提供重置与清除筛选功能。
- 📊 视图支持网格、字段、信号等模式，交付方式包括 CDN、第一方和混合。
- 🗂️ 支持按采集顺序排序，并可查看最常观察站点与最近观察站点。
- 🧭 可按首次发现、分组、脚本家族、渲染方式筛选；支持悬停集群并拖动探索。
- 🧱 当前显示比例为 100%，但提示“未找到画布”。
- 🔍 支持按精确来源或 SHA-256 比对工件，并可搜索全部常量、按厂商过滤。
- 🌐 支持搜索全部浏览器 API，并可按厂商过滤。

---

### [在 JavaScript 中生成不带括号的字符串 - Bartosz 的博客](https://blog.ikaes.de/generating-strings-without-parentheses-in-javascript/)

**原文标题**: [generating strings without parentheses in javascript - bartosz's blog](https://blog.ikaes.de/generating-strings-without-parentheses-in-javascript/)

本文介绍了一种在 JavaScript 中不使用括号、方括号等特殊字符生成任意字符串，并进一步执行任意代码的技巧，核心是滥用 `Error.prepareStackTrace` 对字符串原型方法的调用能力。

- 🧠 目标是实现与 JSFuck 相反的效果：仅用 `+`、`=`、`,`、`.` 等少量字符生成任意字符串或代码。
- ⚠️ 技巧依赖 JavaScript `Error` 对象及其 `name`、`message`、`toString()` 行为，通过覆写原型控制输出内容。
- 🕵️ 访问 `error.stack` 会触发 `Error.prepareStackTrace`，其 `this` 是全局 `Error` 函数，参数包含错误对象和结构化栈数组，等价于可无括号调用二元函数。
- 🧩 通过覆写 `Error.toString`、错误对象 `toString` 和 `Array.prototype.toString`，可把 `prepareStackTrace` 变成 `String.prototype.split`，将字符串拆成字符数组。
- 🔢 使用 `Array.prototype.shift` 逐个取出字符，并通过 `valueOf` 技巧在无括号情况下调用 `shift`，从而模拟 `arr[i]` 索引。
- ➗ 利用 `Array.prototype.indexOf` 返回 `-1` 做减法生成数字，再用 `Array.prototype.join` 将数字转成字符串。
- 🏗️ 组合 JSFuck 式字符提取技巧构造 `String["fromCharCode"](...)` 表达式，注入 `Function` 构造函数生成返回目标字符串的函数。
- 🚀 进一步可把字符编码的 JavaScript 传给 `eval`，实现不使用引号执行任意代码；完整代码和生成器在作者 GitHub 仓库。

---

### [](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)

**原文标题**: [Octoverse: Commits, pushes, reach new highs in 2026 as developers build with agents - The GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)

2026 年 Octoverse 报告显示，GitHub 开发活动创历史新高：过去 12 个月推送 179 亿次、提交 343 亿次、合并 PR 13 亿次；AI 编码代理从试用走向日常协作，推动 PR 创建、模型选择、行业渗透和全球开发者增长全面加速，但“构建什么、为谁构建、是否合格”仍由开发者决定。

- 🚀 开发节奏创新高：过去 12 个月推送 179 亿次，超过 2024 与 2025 年总和；提交 343 亿次，合并 PR 13 亿次，日均 350 万次。
- 🤖 代理成为日常工具：截至 9 月超 40% 的 PR 由代理起草，3 月为 17%；有代理配置的新仓库平均提交量是无配置仓库的 8 倍。
- 🛠️ 自动化持续扩展：GitHub Actions 每秒运行 1440 个作业（日均 1.24 亿），Dependabot 合并超 3000 万个 PR。
- 🌍 全球开发者超 2.25 亿：美国 3830 万、印度 3200 万、中国 1240 万、巴西 1020 万；美印年内各增超 1000 万。
- 🏭 行业覆盖扩大：采矿、建筑、医疗、农业等公共仓库自 2022 年增长数倍；建筑约 9% 仓库有代理 PR，为各行业最高。
- 🧪 代理 PR 更广更快：约 87% 涉及多文件；到 9 月 90% 的代理相关 PR 两周内合并，非代理约 86%。
- ☁️ Copilot 代理化加深：55% 月活用户使用代理功能；Copilot cloud agent 同比增长 230%。
- 🧠 模型选择多元化：9 月 61% 自选模型的 Copilot 用户使用不止一种模型；付费用户可用 47 个模型，无一模型请求占比超 25%。
- ⚖️ 模型按任务分工：开发者自选请求中 38% 流向通用模型、37% 流向深度推理与规划、25% 流向快速轻量模型。
- 💻 语言格局：TypeScript、Python、JavaScript 仍居前三；TypeScript 年内新增 362 万月贡献者最多，Rust 增速最快。
- 📈 开源贡献翻倍：公共贡献达 25 亿，较 2025 年的 11.2 亿翻倍以上；社区项目与厂商工具形成分工。
- 🔮 增长预测分歧：43 个模型预测 2031 年开发者规模，约半数认为增长超 3 倍，近半数认为 2-3 倍，仅 3 个认为低于 2 倍。
- 🚀 不变的核心：火箭 emoji 仍是仓库最常用符号；工具与行业继续变化，但创意、判断与代码价值仍由开发者决定。

---

### [](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/)

**原文标题**: [pull_request_target blocked by default December 2 - GitHub Changelog](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/)

GitHub Actions 将从 2026 年 12 月 2 日起，在公共仓库中默认阻止 `pull_request_target` 事件，除非适用的 Actions 事件策略明确允许；私有和内部仓库不受影响，并设置两次演练窗口供提前排查。

- 📅 自 2026 年 12 月 2 日起，所有公共仓库默认阻止 `pull_request_target`，除非适用的 Actions 事件策略明确允许；此前计划于 2026 年 11 月 2 日执行。
- 🔒 该规则旨在降低安全风险：`pull_request_target` 在基础仓库上下文中运行并可访问机密，若执行来自 fork 的不可信代码，可能危及流水线或窃取机密。
- 🧪 规则最初以评估模式运行，可先查看哪些工作流运行会被阻止，再进入正式强制执行。
- 🏢 私有和内部仓库不受影响；该变更适用于 GitHub Free、GitHub Team 和 GitHub Enterprise Cloud 的公共仓库，不适用于 GitHub Enterprise Server。
- ⏰ 演练窗口为 2026 年 11 月 9 日和 11 月 16 日的 16:00–18:00 UTC；期间受影响公共仓库中被默认规则阻止的 `pull_request_target` 尝试会失败并显示错误注解，工作流不会执行。
- 🛠️ 建议在 11 月 9 日首次演练前使用 Insights 查看受影响的运行；可选择保留默认阻止，或在适用事件策略中通过工作流文件定向明确允许 `pull_request_target`。

---

### [兼容性标志 · Cloudflare Workers 文档](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-the-temporal-api)

**原文标题**: [Compatibility flags Â· Cloudflare Workers docs](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-the-temporal-api)

Cloudflare Workers 的兼容标志用于按需启用或禁用特定运行时行为，便于测试即将默认的变更或保留旧行为；通过 compatibility_date 可批量启用截至该日期的默认兼容变更。标志可在 Wrangler 配置、Dashboard 或 API 的 metadata 中设置，历史记录按最新优先列出，许多标志都有默认启用日期。

- 🧩 兼容标志可启用尚未默认的功能，也可禁用已默认的破坏性变更，以维持旧行为。
- 🗓️ compatibility_date 用于批量启用截至该日期的兼容变更；compatibility_flags 用于精确开关特定标志。
- ⚙️ 设置方式包括 Wrangler 配置文件的 compatibility_flags、Cloudflare Dashboard 的 Workers 设置，以及 Workers Script/Versions API 请求体中的 metadata。
- 🟢 Node.js 兼容：nodejs_compat 启用 Node.js API；2024-09-23 至 2026-08-03 默认包含 nodejs_compat_v2，可用 no_nodejs_compat_v2 仅保留 v1；2026-08-04 起两者默认启用，无需显式添加；完全关闭需同时使用 no_nodejs_compat 和 no_nodejs_compat_v2。
- 🔐 仅需 AsyncLocalStorage 时使用 nodejs_als；部分 Node.js 模块仅提供非功能 stub，会按兼容日期和 nodejs_compat 自动启用。
- 🕰️ 重要近期默认变更包括 Temporal API（2026-12-01）、Wasm 模块名堆栈（2026-12-01）、process.version 报告 Node 24（2026-11-24）。
- 🧱 2026-11-17 起多项默认变更：新模块注册表、cache 选项不再覆盖源 Cache-Control、pipeTo 反向错误/关闭传播、入站 Request.signal。
- 🛡️ Durable Object 待处理 I/O 可防止驱逐（2026-10-01）；WebCrypto 现代算法（ML-KEM/ML-DSA 等）需 webcrypto_modern_algorithms。
- 📣 规范一致性改进包括 dispatchEvent 异常报告后继续分发（2026-09-15）、WebSocket 标准 binaryType 与自动回复 close、CJK TextDecoder、Queue 错误码等。
- 🐍 Python Workers 相关标志包括 Python 3.14（2026-09-08）、共享标准库、.pth 文件处理等，部分标志要求 workers-py 1.1.3+。
- 🧪 实验性标志无默认启用日期：queue_consumer_no_wait_for_wait_until 可让 Queue 消费者不等待 ctx.waitUntil 再确认；HTMLRewriter 可将 ESI include/comment 视为 void 标签。
- 🧩 其他历史标志覆盖 fetch/cache/streams/URL/URLPattern/WebSocket/HTMLRewriter/Workflows/容器 PID/错误序列化/ctx.exports/tracing 等，升级兼容日期前应检查破坏性变化。
- 📝 文档按最新优先列出 flags history，并说明新旧标志替代关系；若 npm 包报错，建议先更新兼容日期及 Wrangler 或 Cloudflare Vite 插件。

---

### [Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

**原文标题**: [Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

overview summary
- 🚀 Node.js 27.0.0-alpha.0.0.0（Alpha）于 2026-10-29 发布，由 Rafael Gonzaga 发布，是下一主版本的早期预览。
- 🧠 V8 从 14.6 升级至 15.6.75.13，默认启用 Math.sumPrecise、Intl.Locale variants、Iterator.join/includes/zip/zipKeyed 等新特性。
- 🧪 实验特性包括 import defer、Immutable ArrayBuffer、RegExp buffer boundaries，需通过对应标志启用。
- 🧮 未设置 --max-old-space-size 时，默认堆上限改为物理内存一半并限制在 256MB–4GB；Buffer/ArrayBuffer 内存计入堆限制。
- 📦 v8.serialize、structuredClone、postMessage 使用新格式，旧版 Node.js 无法读取；编译缓存标签会随 V8 补丁变化。
- ⚠️ 可观察行为变化：Math 使用 LLVM libm、Math.random 序列变化、error.stack 不再沿原型链查找、await 微任务减少、大数组 sort 使用 PowerSort。
- 🧾 堆快照包含更多内部对象、数值和脚本源码，生成时间和文件大小约翻倍；asm.js 不再编译为 WebAssembly。
- 🔐 加密与构建大改：要求 OpenSSL 3+ 并升级至 OpenSSL 4.1.0，移除捆绑 FIPS provider、旧 OpenSSL 代码路径和 OpenSSL engine 支持，多项 crypto API 验证/弃用。
- 🌐 HTTP/网络变化：HTTP 拒绝超限响应头，req.headers 改为 null 原型，keepAliveTimeout 默认 65 秒；HTTP/2 增大默认窗口；net 新增实验性 net/promises。
- 📁 运行时 API：fs.glob 原生实现，domain 模块运行时弃用并迁移至 AsyncLocalStorage，REPL 改用 inspector，新增 --allow-env 权限。
- 🧪 工具链/测试：npm 升级至 12.1.0，test_runner 改用 AsyncLocalStorage，vfs 取消实验标志，新增 fs.mkstemp、zlib crc32c 和 --experimental-strip-private-modules。
- 🛡️ 安全与修复：修复 CVE-2026-58042 DNS resolveAny 大地址回复问题，并更新 undici、SQLite、zlib、brotli 等依赖。
- 💻 平台：Intel macOS 支持降级为实验性且其二进制“即将推出”；提供 Windows、macOS Apple Silicon、Linux、AIX 等安装包/二进制及源码。

---

### [](https://nodejs.org/en/blog/release/v26.13.0)

**原文标题**: [Node.js — Node.js 26.13.0 (LTS)](https://nodejs.org/en/blog/release/v26.13.0)

Node.js 26.13.0 于 2026-10-28 发布，正式将 26.x 系列转入长期支持（LTS），代号为“Lithium”，将持续更新至 2029 年 4 月底。本次发布主要更新 LTS 元数据，功能上与 Node.js 26.12.1 基本一致。

- 🏷️ 版本信息：Node.js 26.13.0（LTS），代号“Lithium”，由 Richard Lau 发布。
- 🔄 LTS 过渡：该版本标志着 Node.js 26.x 正式进入长期支持阶段。
- 🗓️ 支持周期：将持续接收更新至 2029 年 4 月底。
- 🧾 变更内容：除更新 `process.release` 等元数据以反映 LTS 状态外，与 Node.js 26.12.1 相比没有其他变化。
- ⚠️ Linux 依赖提醒：从 Node.js 25 起，官方 Linux 二进制文件链接到 `libatomic`，部分 Linux 发行版可能需要单独安装。
- 💻 下载支持：提供 Windows 64 位、Windows ARM 64 位、macOS Intel 和 Apple Silicon、Linux 64 位、Linux PPC LE、Linux s390x、ARMv8、AIX 等平台安装包或二进制文件。
- 📦 其他资源：提供源代码、发布文件页面和 API 文档链接。
- 🔐 完整性校验：发布内容包含 SHA256 校验值和 PGP 签名，供下载校验使用。

---

### [Node.js — Node.js 版本发布](https://nodejs.org/en/about/previous-releases)

**原文标题**: [Node.js — Node.js Releases](https://nodejs.org/en/about/previous-releases)

Node.js 发布页面说明了版本发布节奏、LTS 支持策略、各版本生命周期状态，以及下载页中“推荐”和“社区”安装方法的分类标准；生产环境应优先选择 Active LTS 或 Maintenance LTS。

- 🚀 主要版本进入 Current 状态 6 个月，便于库作者适配支持。
- 🗓️ 历史上，奇数版本（如 9、11）6 个月后停止支持；偶数版本（如 10、12）转入 Active LTS。
- 🔄 从 Node.js 27 起改为年度发布，每个主版本在 6 个月 Current 及 6 个月 Alpha 阶段后进入 LTS。
- 🛡️ LTS 意为长期支持，通常保证关键缺陷修复共 30 个月；生产应用只应使用 Active LTS 或 Maintenance LTS。
- 📊 版本表列出各版本的代号、首次发布、最后更新和状态；文中 v26、v24、v22 为 LTS，v27 为 Alpha，v25、v23、v20 等为 EOL。
- 🧰 下载页提供 CLI、系统包管理器和版本管理器等非交互安装方式，并分为“推荐”和“社区”两类。
- ✅ “推荐”方法需与官方发布同步、使用未修改的官方二进制、支持多版本并存，并与 Node.js 项目保持紧密沟通。
- 🌐 “社区”方法需支持所有非 EOL 版本、至少适配一个官方支持的操作系统，且免费、开源、非商业付费服务。

---

### [Vitest 5.1 已发布！ | Vitest](https://vitest.dev/blog/vitest-5-1)

**原文标题**: [Vitest 5.1 is out! | Vitest](https://vitest.dev/blog/vitest-5-1)

Vitest 5.1 于 2026 年 11 月 2 日发布，重点提升了测试筛选、快照审阅、失败追踪、浏览器模块 Mock 与覆盖率体验，并带来多项性能优化。

- 🚀 新版为 Vitest 5.1，建议先阅读入门与功能指南，并欢迎社区参与问题分类、PR 审查和讨论支持。
- ⏱️ 新增实验性 `--since-last-run`：首次运行记录每个测试加载的文件及依赖，后续仅运行自上次运行以来变更、删除或上次失败仍未通过的测试；无需 Git，适合 AI 编码代理。
- 🖼️ 新增交互式快照审阅：watch 模式按 `i` 逐个查看失败快照，按 `a` 接受新快照、按 `r` 保留旧快照，覆盖内联快照、`.snap` 文件、文件快照和 ARIA 快照。
- 🧭 Trace View 稳定并默认启用 `'failure-only'`：仅记录失败浏览器测试的步骤，失败报告展示操作时间线；可设为 `'on'` 记录所有测试并附带每步页面快照。
- 🧵 新增实验性 `experimental.traceTimeline`：Node 测试中记录 `expect.poll`、`vi.waitFor`、`vi.waitUntil` 步骤，失败时打印等待时长与位置；`vi.waitFor/vi.waitUntil` 支持 `message`。
- 🔁 新增 `--last-failed`：从结果缓存读取上次失败测试并仅重跑，可按完整测试名筛选；若文件级失败则重跑整个文件。
- 🌐 Browser Mode 通过 import map 提供模块 Mock：基准中无 Mock 耗时降低 16%，有 Mock 降低 52%，混合场景降低 38%；实验性 `browser.importMapMocks` 在支持多 import map 的浏览器启用。
- 🖱️ 新增实验性 `userEvent.pointer`：支持底层指针按下、移动、释放序列，可用于精确拖拽等交互。
- ⏳ 新增 `fakeNodeBuiltins`：让 `node:timers` 和 `node:timers/promises` 也使用假定时器；默认关闭，计划下个大版本默认开启。`vi.setSystemTime` 支持 `Temporal.Instant` 和 `Temporal.ZonedDateTime`。
- 📊 新增 `TestCase.attempts()`：分别返回每次重试/重复运行的状态、错误和耗时；默认报告器会把多次失败合并为一个标题。
- 📈 覆盖率改进：HTML 报告新增明暗主题并跟随系统；Istanbul 插桩改用 Oxc + magic-string，速度提升 5–10 倍，仓库 479 个文件从 3.7s 降至 0.38s；V8 新增 `coverage.ignoreNode`。
- ⚡ 性能优化：`isolate:false` 复用 worker 缓存；`toEqual` 类型化数组比较提速（2MiB 数组 1.5s→125ms）；Firefox Trace View 提速；Browser Mode WebSocket 在高负载下更稳定。
- 🔧 其他变更：Browser Mode 默认端口改为 `23315`，`api.port:0` 可让系统选择空闲端口；浏览器测试无法连接服务器时会直接报错而非无限等待。

---

### [](https://rspack.rs/blog/announcing-2-3)

**原文标题**: [Announcing Rspack 2.3 - Rspack](https://rspack.rs/blog/announcing-2-3)

Rspack 2.3 于 2026 年 10 月 29 日发布，核心是集成 SWC Next 解析器、提升构建性能、降低内存占用与产物体积，并引入实验性新缓存和按 loader 缓存，同时改进内置 CSS 支持与 Rstack 生态工具。

- 🚀 **SWC Next 集成**：采用更紧凑的 ESTree AST，原生解析速度最高为 SWC 的 3 倍，JavaScript API 解析最高快 10 倍；Rspack 解析耗时和指令数均有下降。
- 🧩 **未来插件能力**：SWC Next 计划支持用 JavaScript 编写高性能转换插件，预计在 Rspack 2.4 或 2.5 引入相关 loader。
- 🧠 **内存优化**：真实项目构建峰值 RSS 降低 27.4%，构建后 RSS 降低 36.5%；开发启动峰值降低 33.8%，稳定态降低 34.8%。
- ⚡ **构建性能**：整体构建速度较 2.2.0 提升约 5%，部分大型项目最高提升 20%；新增基于 allocative 的内存快照诊断能力。
- 📦 **SplitChunks 优化**：新增 `splitChunks.dedupDepth`（生产模式默认 `1`）和 `minRemainingSize`，改进模块去重，减少重复代码和过小产物。
- 📉 **产物体积收益**：两个大型真实项目开启 `dedupDepth: 1` 后，Brotli 压缩体积分别减少 2.4% 和 9.9%。
- 🗄️ **新实验缓存**：减少磁盘占用、降低缓存写入对编译的阻塞，并提升缓存恢复可靠性；磁盘占用约降低 79%，冷构建峰值内存约降低 16%。
- 🔧 **缓存启用方式**：新缓存默认关闭，可通过 `experiments.newCache: true` 和 `cache.type: 'persistent'` 启用。
- 🧱 **Loader 缓存**：支持细粒度缓存单个 loader 的转换结果，适合 babel-loader、less-loader 等昂贵 loader；测试中构建时间从 63.8 秒降至 11.2 秒。
- 🎯 **按代码内容过滤 Loader**：新增 `use.codeFilter`，先在 Rust 侧检查代码，仅在需要时调用 JS loader；测试中 loader 调用减少 90%，构建时间降低约 23%。
- 🎨 **内置 CSS 改进**：增强 CSS Modules 作用域、组合、值引用和嵌套选择器支持；支持 CSS-only 入口、`css-import`/`asset-url` externals 及 `rspackIgnore` 注释。
- 🛠️ **其他改进**：优化按需编译、原生 watcher 时间戳与忽略规则、webpack 插件钩子兼容性、TypeScript 类型，以及 WebAssembly 流式加载回退配置。
- 🧪 **Rsbuild 更新**：TanStack CLI 支持 Rsbuild，新增 Lynx Rsbuild 插件、Brotli 文件大小报告、默认 compact-hashed ID，以及更细粒度的开发服务器配置。
- 📚 **Rslib 更新**：Rslib 1.0 发布，支持 `?inline` 内联 Wasm，并支持 TypeScript 7.1 Beta 的 Content Mappers 生成类型声明。
- 🩺 **Rsdoctor 2.0**：推荐使用 Agent CLI 进行 AI 辅助分析，安装体积减少 56%，分析时间减少 57%，开发模式 HMR 时间减少约 47%。
- 🖱️ **Rstest 更新**：浏览器模式新增 `pressSequentially()`、React hydration 测试支持，以及基于 Playwright 的截图回归测试 `toMatchScreenshot()`。
- 🌐 **Rspress 更新**：Rspress 2.1.0 默认支持 WebMCP，内置站点信息查询、文档搜索和页面导航工具，并支持注册自定义工具。

---

### [GitHub - swc-project/swc-next：一个基于 Rust 的全新 Web 平台 · GitHub](https://github.com/swc-project/swc-next)

**原文标题**: [GitHub - swc-project/swc-next: A new Rust-based platform for the Web · GitHub](https://github.com/swc-project/swc-next)

SWC Next 是一个用 Rust 编写的全新 JavaScript/TypeScript 工具链，也是 SWC 从零开始的重写版本，核心设计是扁平化、基于 ESTree 的 AST，以提升性能和可扩展性。

- 🚀 性能显著提升：原生解析器基准最高比 SWC 快 3 倍，JavaScript API 基准最高快 10 倍。
- 🧩 支持 JavaScript 插件：Rust 与 JavaScript 之间可快速往返 AST，便于用 JavaScript 编写插件。
- ✅ 注重正确性：已针对 Test262、TypeScript 和 Babel 测试，并补充单元测试。
- ⚠️ Rust API 仍处于早期阶段：生产环境建议继续使用 SWC 的 Rust API。
- 📦 JavaScript API 通过 `@swc-next/core` 提供，可用 `npm install @swc-next/core` 安装，并支持 `parseSync`、`printSync` 等用法。
- 🗺️ 项目在独立仓库开发并发布独立包，逐步对齐 SWC 能力，长期目标是成为 SWC 的下一个主版本并合并回 SWC 仓库。
- 🏗️ 架构设计参考“扁平化 AST”等文档；当前 Rust AST API 存在已知健全性问题，例如节点 ID 和类型化句柄未绑定所属 `Ast`，跨 AST 使用可能导致访问无关节点甚至未定义行为。
- 🔄 兼容性方面，计划支持部分 SWC `.swcrc` 选项，但 Rust 和 JavaScript API 不会与 SWC 兼容，配置兼容尚未实现。
- 🙏 项目借鉴了 Yuku、Zig、rowan、Oxc、esbuild 等项目的设计与实现。
- 📄 自有代码采用 Apache License 2.0，第三方代码和数据保留其上游许可证条款。

---

### [发布 v2.0.0-beta.1 · Leaflet/Leaflet · GitHub](https://github.com/Leaflet/Leaflet/releases/tag/v2.0.0-beta.1)

**原文标题**: [Release v2.0.0-beta.1 · Leaflet/Leaflet · GitHub](https://github.com/Leaflet/Leaflet/releases/tag/v2.0.0-beta.1)

Leaflet 发布 v2.0.0-beta.1，这是 Leaflet 2.0 的首个 beta，相较 alpha 在打包体积、TypeScript 支持、性能、无障碍和稳定性方面大幅升级，同时引入较多破坏性变更并提供完整迁移指南。

- 🚀 **首个 2.0 beta**：标志着 Leaflet 2.0 进入新阶段，功能和架构均有显著提升。
- 📦 **完全支持 tree-shaking**：仅打包实际使用内容，地图加瓦片层体积降至 25.6 kB gzip，低于此前的 38 kB。
- 🧩 **内置 TypeScript 类型**：类型由源码生成并以严格模式检查，支持类型化配置、按类事件和插件模块扩展。
- 🎨 **默认 Marker 改用内联 SVG**：可配合任意打包器或 CDN 开箱即用，支持 CSS 颜色和旋转，解决默认图标加载问题。
- ⚡ **性能明显提升**：默认 Marker 渲染快 25–45%、DOM 节点减半；对象创建约快 2 倍；矢量图层重绘快 12–14%。
- ♿ **无障碍增强**：尊重 `prefers-reduced-motion`，Marker 支持键盘点击与方向键拖动，地图容器增加 `role="region"` 和 `aria-label`。
- 🖱️ **交互体验改进**：限制惯性速度、拖拽出窗口后仍保持、缩放时减少灰屏闪烁、相邻多边形以子像素精度对齐。
- 🐞 **修复 40+ 个问题**：包括长期存在的瓦片缝隙、矢量偏移或模糊、缩放时光标漂移、iOS 双击缩放异常等。
- 🧭 **目标浏览器为 Baseline 2022**：支持 Safari 15.4+ 等较新浏览器环境。
- ⚠️ **破坏性变更较多**：移除默认导出，类改为扁平命名，仅发布压缩构建，停止深层导入，并用内置类型替代 `@types/leaflet`。
- 🔧 **API 与架构调整**：`initialize()` 改为 `constructor()`，移除 `Class.extend()`，`prototype.options` 改为 `mergeOptions/defaultOptions`，移除 `Browser` 命名空间，`keypress` 改为 `keydown`。
- 📝 **文档与工作流升级**：API 参考由 TypeScript 类型生成，网站改用 Node 脚本构建，测试迁移至 Vitest，并在每个 PR 检查 tree-shaking、包体积、类型和 API 变更。

---

### [Effect 4.1（发布）| Effect 博客](https://effect.website/blog/releases/effect/41)

**原文标题**: [Effect 4.1 (Release) | Effect Blog](https://effect.website/blog/releases/effect/41)

Effect 4.1 已发布，新增 `effect/crypto`、Glob 文件匹配、流式 CSV、HttpApi Problem Details 等功能，并包含多项增强与破坏性变更；升级前需查看完整 CHANGELOG 并逐项处理迁移。

- 🔐 **Crypto 服务**：新增 `effect/crypto`，覆盖随机数、哈希、加密、签名和密钥管理；需通过 `NodeCrypto.layer` 等平台层显式提供，替代 `effect/Crypto`。
- 📁 **Glob 匹配与文件搜索**：新增实验性 `Glob` 模块，支持路径匹配；`FileSystem.glob` 可在 Node、Bun、Deno 上按同一语法搜索文件。
- 📊 **流式 CSV**：`effect/encoding` 新增不稳定 `Csv` 模块，支持流式解析/写入文本或 UTF-8 字节、表头记录，并可通过 `Schema` 转换单元格。
- 🧾 **HttpApi Problem Details**：支持 RFC 9457 `application/problem+json` 错误渲染、文档和解析；可用 `HttpApiError.Problem` 声明类型化问题，内置错误可通过 `HttpApiSchema.asProblem` 选择启用。
- ⚙️ **更多亮点**：改进子进程命令行与敏感参数处理、AI `Decision.Image` 与 `Decision.locate`、MCP 按请求提供服务和可见性控制、连接池指标、ISO 8601 时长、字面量联合匹配及失败日志级别。
- 🧨 **破坏性变更**：Crypto 不再包含在运行时 `*Services` 中，`effect/testing/TestCrypto` 移除，部分 SQL/EventLog API 改用 `Digest.Digest`。
- 🧩 **升级注意**：子进程模板对 shell 语法更严格；自定义 `FileSystem` 需实现 `readDirectoryEntries`；MCP 注册层改走 transport 的 `registrations` 选项。
- 🗄️ **持久化与网络**：`KeyValueStore`/Redis 持久化键按 store 隔离，Redis `PersistedQueue` 锁格式更新；RPC `discard: true` 在服务端确认后完成；`Toml.parse` 返回 `Result`。
- 🌐 **其他迁移点**：HTTP 请求方法类型改为 `string`；Node 流/套接字读取新增 `readSize`，`chunkSize` 变为有界拉取大小；`BunHttpServer` 默认禁用 10 秒 `idleTimeout`；OpenTelemetry `NodeSdk`/`WebSdk` 需从子路径导入。

---

### [pnpm 12.17.0 | pnpm](https://pnpm.io/blog/releases/12.17.0)

**原文标题**: [pnpm 12.17.0 | pnpm](https://pnpm.io/blog/releases/12.17.0)

pnpm 12.17.0 是一次功能增强与稳定性修复版本，重点新增全局 peers 检查、`overrides` 依赖组选择器与通配符、`outdated/update` 对运行时、包管理器、Cargo 与 Python 依赖的检查更新，并修复 Docker 多用户文件权限、本地依赖重复安装漏检、全局命令依赖解析等问题。

- 🚀 `pnpm peers check` 新增 `--global/-g`，全局安装或更新后会提示使用 `pnpm peers check -g`。
- 🔍 `pnpm outdated` 与 `pnpm update` 可检查/更新 `devEngines.packageManager`、`packageManager`、`devEngines.runtime`、`engines.runtime` 和 `runtime:` 依赖；启用 Cargo/Python 时也处理 `Cargo.toml`/`Cargo.lock` 与 `pyproject.toml`/`pylock.toml`。
- 🧩 `overrides` 支持 `:prod`、`:optional`、`:peer` 伪选择器及 `*` 通配符；非范围覆盖不再错误添加 peer 依赖，用 `"-"` 删除可选依赖也会清理 `dependencies` 重复项。
- 🐳 新建文件权限改为遵循 umask（如 `0644`），修复 Docker 中以其他用户运行时的可读性问题；涉及 workspace 状态、`pnpm-workspace.yaml`、deploy、patch、dedupe 及 Cargo/Python 文件，编辑已有文件则保留原权限。
- 🔗 修复 `node_modules` 为符号链接时写入失效依赖链接的问题；全局安装的命令现在能找到 pnpm 提升的依赖。
- ⚙️ 切换项目固定 pnpm 版本时，会安装当前主机原生二进制并修复缺失；全局虚拟存储下依赖环中任一依赖变化会让环内包获得新目录，避免加载旧副本。
- 📦 `nodeLinker: hoisted` 下无法提升到根目录时，各 workspace 项目保留自己的包副本并分别执行构建脚本。
- 🔁 重复安装与本地依赖修复：避免 `--frozen-lockfile` 刚写入就报过期；正确检测 `file:`、注入的 `workspace:../dir`、本地 tarball、`package.json` 及 pnpmfile `readPackage` 变化；被删除的 `workspace:`/`link:` 链接会重新链接。
- 📦 `pnpm update --latest` 配合包选择器时只在声明范围内更新；`pnpm add <pkg>@<tag>` 与 catalog dist-tag 行为更一致，catalog 记录精确版本，npm alias 保存解析后的版本范围。
- 🖥️ 脚本/`pnpm exec` 启动的进程生命周期更接近直接运行命令；递归/并行任务中止时 Unix 先发 `SIGTERM`，Windows 会结束相关进程。
- 🪟 Windows 下 `.cmd`/`.bat` shim 在关闭 MSYS 参数转换时改用 Git Bash，避免误开交互式 cmd。
- 📁 `pnx` 与 `pnpm create` 支持在 `--dir` 或 `--workspace-root` 指定目录执行；`--env-file` 行为与 Node 一致，不再展开变量或拒绝文件内容。
- 🛠️ 设置与提示改进：`gitTagVersion=false` 时 `pnpm version` 不再提交/打标签；`publishBranch` 支持 workspace 配置与环境变量；新增 `--strict-ssl`、`--local-address`；`doctor` 注册表检查超时 15 秒；配置解析错误统一为 `ERR_PNPM_INVALID_SETTING`；无效依赖名错误会指出项目目录。
- ⚡ 性能修复：从存储硬链接时每个存储文件每次安装只 stat 一次，降低大型工作区离线安装 CPU 开销；Node.js `latest` 选择器改为最新稳定版。

---

### [ESLint v10.14.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/10/eslint-v10.14.0-released/)

**原文标题**: [ESLint v10.14.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/10/eslint-v10.14.0-released/)

ESLint v10.14.0 于 2026 年 10 月 30 日发布，属于小版本升级，包含新特性与多项 Bug 修复，并更新了部分规则在边缘场景下的行为、文档及维护性依赖。

- 🚀 **发布信息**：ESLint v10.14.0 为 minor release，新增功能并修复上一版本发现的问题。
- 🧩 **重点规则更新**：`func-name-matching`、`no-invalid-this`、`no-restricted-globals`、`object-shorthand`、`yoda` 已更新，以避免错误或意外行为。
- ✨ **新特性**：修复 `func-name-matching` 中的属性描述符处理（#21400）。
- 🐞 **Bug 修复**：要求 `minimatch` 10.2.6 以避免脆弱的 `brace-expansion`；修复 `no-restricted-globals` 在全局对象作为属性值时崩溃；处理 LS、PS 和空 hashbang 注释；修复 `no-invalid-this` 对无初始化 `accessor` 字段崩溃；更新 `@humanfs/node`；避免 `object-shorthand` 对 super 方法产生无效修复；修复 `yoda` 在语句开头进行非法自动修复。
- 📚 **文档更新**：从文档语言切换器中移除 `zh-hans`；更新 README；自定义规则文档用虚拟插件替代 `--rulesdir`；移除 Tidelift 商业支持；更新 v10 的 `loadESLint()` 文档；修订 PR 模板中的 AI 致谢选项。
- 🛠 **维护工作**：禁用 `eslint-plugin-unicorn` 生态测试；更新 `github/codeql-action`、生态插件及 `prettier` 至 v3.9.10；在循环修复警告信息中添加故障排查页面 URL。
- 👥 **贡献与标签**：由 Milos Djermanovic 等贡献，最后更新于 2026 年 10 月 30 日，标签为 Release。

---

### [Nuxt DevTools v4 · Nuxt 博客](https://nuxt.com/blog/devtools-v4)

**原文标题**: [Nuxt DevTools v4 · Nuxt Blog](https://nuxt.com/blog/devtools-v4)

Nuxt DevTools v4 基于 Devframe 与 Vite DevTools 重构，带来完整 Vue DevTools，并让 Nuxt 接入可复用的统一 DevTools 生态；它随 Nuxt v5 发布，也支持 Nuxt 4.5+，现有应用无需修改即可使用。

- 🚀 发布于 2026 年 10 月 28 日，核心变化是构建在 Devframe 和 Vite DevTools 之上，不再复制 Vue DevTools，而是直接继承完整功能。
- 🔧 重构原因：旧版从 v1 起只为 Nuxt 设计，各模块需专用 API，Vue DevTools 功能需复制维护，难以同步；Devframe 从底层解决面板、服务端通信和数据展示的通用需求。
- 🧩 Devframe 是框架无关的 DevTools 工具包，用一次定义描述面板、类型化 RPC 和共享状态，可运行在 Nuxt、Vite、Next.js、CLI、静态报告或 MCP Server 等宿主中。
- 🌐 生态双向互通：其他基于 Devframe/Vite DevTools 的工具可在 Nuxt 使用，为 Nuxt 构建的工具也可在 Nuxt 外使用；通用工具与构建工具层可被不同宿主复用。
- 🏗️ 三层架构：Devframe Hub 为基础，组合可移植 devframe；Vite DevTools 增加 Vite 工具链能力，如 Vite 插件、Vitest、Rolldown、Oxc；Nuxt DevTools 再增加 Vue DevTools、Pinia、Nuxt 模块、自动导入等 Nuxt 层。
- 🔄 这是过渡版本：旧的 `@nuxt/devtools-kit` API 仍可通过 shim 工作，开发时会输出警告提示模块更新；用户界面体验保持连续。
- 🧭 模块作者建议迁移到 Devframe（跨工具复用）或 Vite DevTools（仅 Vite、改动最小）；旧辅助函数有对应新 API 和诊断码，例如 `addCustomTab` → `ctx.docks.register`、`extendServerRpc` → `ctx.scope().rpc.register` 等。
- ⚠️ docks 宿主暂不支持 vnode 视图和标签分类；依赖这些能力的模块需暂时继续使用 shim。
- 📦 可用 `defineDevframe()` 定义可移植工具，并通过适配器输出 Vite 插件、独立 CLI、静态报告和 MCP Server；Nuxt UI 可用 `@devframes/nuxt/single` 获得类型化 `$rpc` 客户端。
- 🖥️ 使用方式不变，快捷键为 macOS `Shift + Option + D`、Windows `Shift + Alt + D`；推荐直接用 Nuxt 5，Nuxt 4.5+ 可运行 `npx nuxt module add @nuxt/devtools@4`。
- 🙏 官方感谢 Devframe、Vite DevTools、Vue DevTools 贡献者，并邀请用户试用和反馈问题。
- 📚 相关发布：Nuxt 4.6 让 Nuxt 服务端无关（`nuxt/server`），重建类型化 `$fetch`，加入 sessions、Vue Vapor 支持和新的开发错误页，并随 Nuxt CLI v4 发布。

---

### [smoores.dev - 不，npm，“estee”不是“testem”的拼写错误](https://smoores.dev/post/no_npm_estee_is_not_a_typo/)

**原文标题**: [smoores.dev - No, npm, “estee” is not a typo of “testem”](https://smoores.dev/post/no_npm_estee_is_not_a_typo/)

文章作者讲述了 Storyteller 项目因 npm 包名“estee”被判定为与现有包名过于相似而无法发布，进而批评 npm 的 typosquat 防护规则过于粗糙：它基于 Levenshtein 距离，会误伤正常名称，并大幅压缩可用短包名空间；作者曾通过客服手动解决“audiobook”包名封锁，但这次未能绕过自动规则，最终只能改用“estie”。

- 🧩 Storyteller 因“storyteller”命名空间已被占用，只能使用较长的“@storyteller-platform/”作为 npm 命名空间。
- 😄 作者为命令行工具“@storyteller-platform/align”取了昵称“estee”，但在发布 v0.0.1 时被 npm 以“与 espree、testem 过于相似”为由拒绝。
- 📏 npm 使用 Levenshtein 距离规则，禁止与热门包名编辑距离不超过 2 的新包名；“estee”到“testem”只需两次编辑。
- 📉 作者指出该规则在短字符串上会严重压缩命名空间：4 字符包名理论上很多，但距离阈值会让可用名称比例极低。
- 🔍 备用名“hoid”也被拒绝，并牵出一长串并不像真实拼写错误的“相似包名”，如 hoek、hono、uid、uuid、zod 等。
- 🚫 作者批评规则会误伤合法项目，例如可能阻止“preact”因“react”存在而诞生，也会阻止“estree”因“espree”存在而诞生。
- 📮 作者曾就“audiobook”包名被禁联系 npm 客服并成功手动解决，但这次客服表示无法绕过自动 typosquat 封锁。
- 📝 作者指出客服引用的 npm 博客文章讲的是标点差异导致的重复包名问题，与本次经历并不一致。
- 😔 作者怀疑 npm/GitHub 内部仍可手动绕过该限制，但最终只能把 CLI 名称改为“estie”，并惋惜短 npm 包名时代可能已结束。
- ⚖️ 作者理解 npm 防止 typosquatting 恶意包的压力，但认为规则笨拙，且可能确有必要，令人无奈。

---

### [莱文斯坦距离 - 维基百科](https://en.wikipedia.org/wiki/Levenshtein_distance)

**原文标题**: [Levenshtein distance - Wikipedia](https://en.wikipedia.org/wiki/Levenshtein_distance)

莱文斯坦距离（Levenshtein distance）是一种用于衡量两个字符串差异的字符串度量，定义为将一个字符串转换为另一个字符串所需的最少单符号编辑次数；经典模型中插入、删除和替换的成本均为 1。它由苏联数学家 Vladimir Levenshtein 于 1965 年在纠错码背景下提出，属于更广泛的编辑距离家族，并与序列比对密切相关。

- 📏 **定义**：两个字符串之间的莱文斯坦距离是最少插入、删除或替换操作数，每个操作单位成本为 1。
- 🧮 **递推计算**：通过动态规划计算前缀距离，边界为 D(i,0)=i、D(0,j)=j，核心递推取删除、插入、匹配/替换三种情况的最小值。
- 🐱 **示例**：`kitten` 与 `sitting` 的距离为 3；`uninformed` 与 `uniformed` 的距离为 1。
- 📐 **度量性质**：单位成本下满足非负性、同一性、对称性和三角不等式；长度 m、n 的字符串满足 |m−n| ≤ lev(a,b) ≤ max(m,n)。
- 🔁 **与其他距离的关系**：Damerau–Levenshtein 允许相邻符号交换；最长公共子序列距离只允许插入和删除；Hamming 距离只允许替换且要求等长。
- 🔤 **应用场景**：用于拼写检查、OCR 纠错、近似字符串匹配、文本数据库查询、记录链接与去重。
- 🗣️ **语言学与语音**：常用于语音/音系转写比较和方言计量学，也可使用加权版本按语音特征调整替换成本。
- 🧬 **生物信息学**：编辑距离与序列比对相关，但实际生物序列比对通常使用更丰富的评分系统和空位惩罚。
- 💻 **标准算法**：动态规划算法通常关联 Wagner–Fischer 1974 年形式化；完整矩阵需 Θ(mn) 时间和 Θ(mn) 空间。
- 🧠 **内存优化**：若只需距离值，可将空间降至 O(min(m,n))；若需重建最优编辑脚本，可用回溯或 Hirschberg 线性空间方法。
- ⚡ **高级算法**：包括 Ukkonen 的阈值/距离敏感算法、Myers 的位并行算法、Levenshtein 自动机，以及近似算法和条件下界研究。
- ⏱️ **复杂度**：精确计算通常为 O(mn)；Backurs 与 Indyk 表明强次二次精确算法会推翻 SETH，这是条件性下界。
- 🌐 **Unicode 注意事项**：实现可基于字节、码元、码点或扩展字形簇，不同选择会得到不同距离；比较 Unicode 文本时应说明比较单位和是否进行 NFC/NFD 等规范化。
- 🕰️ **历史发展**：Levenshtein 1965 年提出编辑度量但未给出常见矩阵算法；后续发展出线性空间重建、距离敏感算法、位并行方法、自动机、近似算法和下界研究。

---

### [我们如何在不牺牲兼容性的情况下将 clarity.js 缩小 4.5%——了解您的客户 | Microsoft Clarity 博客](https://clarity.microsoft.com/blog/how-we-made-clarity-js-smaller/)

**原文标题**: [How We Made clarity.js 4.5% Smaller Without Sacrificing Compatibility - Understand your customers | Microsoft Clarity Blog](https://clarity.microsoft.com/blog/how-we-made-clarity-js-smaller/)

clarity.js 团队借助 AI 编码代理 pi 和 autoresearch，将“改代码—构建—测量 gzip 体积—跑测试—保留或回滚”做成自动化实验循环；在 50 多次实验后，脚本缩小了 1,257 个 gzip 字节，体积减少 4.5%，且未牺牲功能或兼容性。文章的核心发现是：源代码看起来更简洁、更高效的写法，不一定能让 gzip 后的脚本更小；真正有效的优化往往来自消除命名空间导入、删除整段函数、调整压缩器选项等，而最大收益因 Zone.js/Angular 兼容性无法上线。

- 🧪 团队用 AI 代理自动化做 50 多次小实验，每次约 35 秒，逐个测量 gzip 后体积并跑测试，决定保留或回滚。
- 📉 最终 clarity.js 减少 1,257 个 gzip 字节，体积下降 4.5%，没有减少功能。
- 🧩 Gzip 会压缩重复字节序列，因此重复代码成本低；新函数名、新调用模式、唯一字符串才会增加真实体积。
- 😬 提取小助手常适得其反：coordinates() 助手让 gzip 增加 23 字节，dim() 增加 13 字节，提升共享数组增加 2 字节，使用 `||=` 增加 3 字节。
- 🧱 最大可发布优化是消除命名空间导入，减少 444 个 gzip 字节，占总节省 35%；其中 data/index.ts 的 13 个命名空间导入贡献 324 字节。
- 🗑️ 删除整个函数有效，共减少 84 个 gzip 字节；例如用 Response API 替代 12 行手动流读取，减少 44 字节，删除多余 parseSignals() 包装减少 20 字节。
- ⚙️ 调整 Terser 选项减少 301 个 gzip 字节；有效选项包括 `passes: 3`、`hoist_vars: true`，以及 Rollup IIFE 输出上的 `freeze: false`。
- 🔤 将模板字符串改为字符串拼接减少 110 个 gzip 字节；因目标是 ES5，模板字符串会编译成 `.concat()` 调用。
- 🧹 大块重复代码去重有效，减少 109 个 gzip 字节；例如用 `Object.assign({}, buffer)` 替代 27 行逐属性复制。
- 🚫 最大未发布优化是把 TypeScript 目标从 ES5 提升到 ES2017/ES2020，可省 2,308 个 gzip 字节，几乎等于其他优化总和的两倍；但会破坏 Zone.js 对 Promise 和 ES5 生成器式 async/await 的拦截，导致 Angular 变更检测静默失效。
- ⏱️ 自动化实验循环适合体积优化：每个小改动可能只省 5–50 字节，人工不值得，但机器可在一小时内测试约 100 个想法。
- ✅ 实践建议：检查并转换被当作值传递的 `import * as X`；逐个测试压缩器选项；能删整函数就删；不要为“整洁”提取小助手；测量 gzip 体积而非原始体积；尽量自动化实验。

---

### [你想要的会话回放，没有噪音 | Sentry](https://sentry.io/resources/201-session-replays/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=replay-fy27q4-sessionreplayworkshop&utm_content=newsletter-sponsored-link-register)

**原文标题**: [The session replays you want without the noise | Sentry](https://sentry.io/resources/201-session-replays/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=replay-fy27q4-sessionreplayworkshop&utm_content=newsletter-sponsored-link-register)

本次研讨会介绍如何在不被噪音干扰的情况下精准获取所需的 Session Replay，涵盖自定义 React Hooks、带录屏的用户反馈，以及通过筛选器和标签定位目标会话。

- 🎯 研讨会提供实操视角，帮助创建自定义 React Hooks 并获取所需会话回放。
- 📊 采样设置：讲解两种采样率、缓冲区模式的作用，以及官方推荐的默认值。
- 🪝 自定义 Hooks：可捕获特定用户群体、已知有问题的 URL，或刚上线的流程等目标会话。
- 🐞 用户反馈：接入反馈组件，让 Bug 报告自动附带对应的 Replay。
- 🔍 查找回放：利用筛选器、无效点击与愤怒点击、自定义标签，按产品实际结构切分会话。
- 🔒 隐私：介绍默认设置以及如何自定义隐私选项。
- 🎙️ 还提到赞助的开发者播客 Syntax Podcast，可在常用收听平台查看。

---

### [未满一周不安装：npm 的 7 天冷却期](https://brunoj.com/nothing-installs-at-our-company-until-its-a-week-old/)

**原文标题**: [Nothing Installs Until It's a Week Old: a 7-Day npm Cooldown](https://brunoj.com/nothing-installs-at-our-company-until-its-a-week-old/)

公司在公共包仓库前部署代理网关：npm、pnpm、Yarn、Bun 与 pip、uv 的新版本需满 7 天才可安装，pub 为 3 天，Maven/Gradle/Go 只缓存不延迟，CocoaPods、Google Maven、Docker 镜像不经过网关；网关还提供版本黑名单和按账号、令牌、CI 记录的下载日志。

- 🧨 动机：今年多起供应链劫持都在数小时内被撤下，但全新安装可能在发布后几十秒内中招，7 天等待能覆盖这一高风险窗口。
- 🔐 规则：npm/pnpm/Yarn/Bun 和 pip/uv 冷却 7 天，pub 冷却 3 天；过新版本从版本列表隐藏，下载返回 404，即使 lockfile 锁定也不行。
- 🚦 入口与治理：通过 Google 登录发放个人令牌，CI 按 IP 或服务令牌接入；黑名单可按精确版本封禁并返回 403，下载日志可查“谁先装了”。
- 🧰 选型：用 git-pkgs/proxy 单二进制代理 npm、PyPI、pub、Maven、Go 等；Verdaccio 只支持 npm，且其文档称过滤是“展示规则，不是访问控制”。
- 📊 12 天数据：81,710 次下载、14 个账号；6,116 个过新版本被隐藏；71 次因 lockfile 固定过新版本被拒；黑名单 0 条。
- 🧱 兼容性坑：Yarn 1、旧 bun.lockb、uv --frozen、Poetry、pnpm 11 环境变量等可能绕过或不适配；Dependabot/Renovate 也要设置至少 7 天冷却，否则更新 PR 会失败。
- ⚠️ 其他副作用：npm audit 不经过冷却；当最新版被隐藏时可能把预发布版当作最新允许版本；网关宕机会导致自托管 CI 无法安装依赖。
- 🕵️ 局限：冷却只争取时间，不检查包内容；若一周内无人发现，投毒版本仍会在第 8 天进入；react-native-international-phone-number 和 xz-utils 是发现太慢的反例。
- ⚙️ 可落地设置：npm `min-release-age=7`、pnpm `minimumReleaseAge=10080`、Yarn `npmMinimalAgeGate="1w"`、Bun `minimumReleaseAge=604800`、uv `exclude-newer="7 days"`、pip `--uploaded-prior-to=P7D`、Dependabot `cooldown: default-days: 7`、Renovate `"minimumReleaseAge": "7 days"`。
- 🧾 配置提示：git-pkgs/proxy 的 cooldown 可按生态设置默认与例外，denylist 可按精确包版本封禁；在 v0.10.0 中 Maven/Go 仍不受 default 冷却限制。
- 🧮 结果：vite 8.3.5 发布后的下一个周三才被放行；作者强调“只看年龄，不看流行度”，规则偶尔也被自己打破，例如代理升级到 v0.10.0 仅两天。

---

### [设计系统应默认快速 | Den Odell](https://denodell.com/blog/design-systems-should-be-fast-by-default)

**原文标题**: [
      Design Systems Should Be Fast by Default | Den Odell
    ](https://denodell.com/blog/design-systems-should-be-fast-by-default)

设计系统应“默认就快”：组件性能会直接影响所有使用它的应用，因此性能应像可访问性一样成为设计系统的核心质量指标，并通过真实数据量下的自动化测试防止性能回退。

- 🧱 分层架构中，浏览器、框架、设计系统和产品代码共享同一主线程；底层设计系统占用越少，上层应用响应越快。
- ♿ 组件常在少量数据下测试，真实应用给出大量数据后才暴露性能问题；设计系统团队应将性能与可访问性并列重视。
- 🔍 作者测试了 10 个流行开源设计系统，涵盖 React、Lit、FAST、Stencil 和 SAP 等技术；发现只有 Spectrum Web Components 有自动化组件级性能测试，其他多数只关注包体积。
- ⏱️ 测试任务包括打开含 249 个国家的下拉框、一次勾选 100 个复选框；使用生产构建、Chrome、CPU 4 倍降速，并取三次测试中位数。
- 🏁 国家下拉框最快为 Fluent 61ms、Carbon 63ms；Ionic 最慢，达 1266ms，且 UI 最长阻塞 1133ms。
- ☑️ 勾选 100 个复选框最快为 Fluent 29ms、Carbon 41ms；Ant Design 最慢，为 421ms，约为 Material UI 的 6 倍。
- 🧩 性能不由框架单独决定：同为 Lit 的 Carbon 与 Spectrum Web Components 差异明显；Ionic 下拉框很慢，但复选框表现不算差。
- 🐌 Ionic 慢主要因为 Stencil 在无 shadow DOM 的 slot 中反复扫描已有选项，添加选项近似 O(n²)；可通过使用 shadow DOM 或优化 Stencil 的 fallback 检查修复。
- 🐌 其他根因包括：Material UI 长列表未虚拟化；UI5 打开时一次性计算大量隐藏元素样式；React Spectrum 存在布局抖动；Ant Design 批量勾选时同时播放 100 个动画。
- ✅ 修复方向包括：长列表虚拟化、批量读写布局、批量选择时关闭动画、用合成层 opacity 动画替代高成本重绘，以及让浏览器原生处理 slot。
- 🧪 建议用 Playwright 编写组件性能测试和性能预算，例如 249 项下拉框打开总耗时低于 300ms、最长阻塞低于 100ms、250 项耗时不超过 125 项的 2.5 倍。
- 🚀 最终建议：把快速行为设为默认，文档标注组件测试过的数据量，用真实页面性能分析指导优化，并在发布说明中给出优化前后的性能数据。

---

### [](https://charpeni.com/blog/the-bun-dependabot-gap-dependabot-alerts-dont-see-bun-lock)

**原文标题**: [The Bun Dependabot Gap: Dependabot Alerts Don't See bun.lock | Nicolas Charpentier](https://charpeni.com/blog/the-bun-dependabot-gap-dependabot-alerts-dont-see-bun-lock)

GitHub 的依赖图目前无法读取 `bun.lock`，因此 Bun 项目中的 Dependabot 告警只能看到 `package.json` 声明的直接依赖，传递依赖和通过 `catalog:` 声明的依赖都不可见；迁移到 Bun 还可能让旧 lockfile 相关告警被误标为已修复。作者为此推出基于 dependency submission API 的 `bun-lock-submission` GitHub Action，并给出检查、部署和后续清理建议。

- 🐰 本文是“CVE 卫生”系列第 5 篇，重点从“修复 CVE”转向“先知道 CVE 是否存在”。
- 🔍 GitHub 依赖图支持 npm、Yarn、pnpm 的 lockfile，但不支持 `bun.lock`，所以 Bun 项目的 Dependabot 告警只覆盖 `package.json` 中的直接依赖。
- ⚠️ 传递依赖以及 `catalog:` 声明的依赖不会触发告警；示例中 `bun audit` 发现 3 个漏洞，Dependabot 只报告 1 个。
- 🔄 从 npm 或 Yarn 迁移到 Bun 后，旧 lockfile 消失，相关未修复告警可能被标记为“已修复”，但漏洞仍存在于 `bun.lock` 中。
- ✅ 检查方法：在 Insights → Dependency graph 中查看是否识别 `bun.lock`，并对比 Dependabot 告警来源与 `bun audit` 结果。
- 🛠️ 解决方案是使用 GitHub dependency submission API；作者构建了 `bun-lock-submission` Action，读取并提交仓库中的所有 `bun.lock`。
- 📦 该 Action 支持 workspace、catalog、monorepo，区分直接/传递依赖和运行时/开发依赖，并尽量减少重复告警；同时提供 npm CLI 用于预览提交内容。
- 🚦 注意事项：告警跟随默认分支；首次运行可能产生大量告警，需要安排分诊；私有包应通过 `exclude` 排除，避免与同名公共包混淆。
- 🔧 Dependabot 对 Bun 项目只告警、不自动开安全更新 PR，修复仍需配合 `bun audit fix`。
- 🧹 建议：先检查是否受影响，复查迁移到 Bun 时关闭的告警，添加该 Action 并预留分诊时间；等 GitHub 原生支持 `bun.lock` 后删除工作流并运行 `bunx bun-lock-submission clear`。

---

### [检查空白字符有多难？](https://serce.me/posts/2026-10-30-how-hard-is-it-to-check-for-whitespace)

**原文标题**: [How hard is it to check for whitespace?](https://serce.me/posts/2026-10-30-how-hard-is-it-to-check-for-whitespace)

检查空白字符看似简单，实则涉及 Unicode 定义差异、不同运行时规则和历史兼容性；Guava 通过完美哈希函数高效实现该检查，展示了简单函数背后的复杂细节。

- 🔍 文章从 Guava 的空白字符检查方法切入，说明它为何比简单的 `c == ' '` 复杂得多。
- 📚 Unicode 的 `White_Space` 属性定义了 25 个空白字符，包括空格、制表符、换行、不换行空格等，各有不同用途。
- ⚠️ 字符名称和外观可能误导，例如 `ZERO WIDTH SPACE (U+200B)` 并不是空白字符，而 `OGHAM SPACE MARK` 有时会显示为可见横线。
- 🌐 不同运行时规则不一致：Java 排除 `U+00A0` 等字符，Python 识别 29 个空白字符并包含 `U+001C`，JavaScript 对 `U+0085` 和 `U+FEFF` 的处理又不同。
- 🕰️ Unicode 标准会演变，例如 `U+180E` 在 Unicode 6.3 中被重新分类，给追求向后兼容的语言和库带来挑战。
- ⚡ Guava 使用完美哈希函数：通过乘法与位移计算索引，在 32 字符表中查找并确认匹配，避免逐个比较。
- 🔢 魔术数字 `1682554634` 可通过暴力搜索找到其他可行乘数，Guava 的实现也经历了从简单匹配到 `mod-79` 再到完美哈希的演进。
- 💡 文章结论是：即使是 `isWhitespace` 这样简单的函数，背后也可能包含 Unicode 细节和算法设计；完美哈希还可用于 HTTP 方法检查等场景。

---

### [一项提议：在人工智能时代如何招聘初级工程师 | Seldo.com](https://seldo.com/posts/a-proposal-how-to-hire-junior-engineers-in-the-age-of-ai/)

**原文标题**: [A proposal: how to hire junior engineers in the age of AI | Seldo.com](https://seldo.com/posts/a-proposal-how-to-hire-junior-engineers-in-the-age-of-ai/)

概述：随着 AI 编码兴起，初级工程师招聘自 2023 年起急剧萎缩，传统编码面试已失效，而多数公司只招资深工程师或依赖实习项目，均非长久之计。作者基于"产品工程师"这一新岗位的定义，提出一套结构化面试方案：让候选人在一小时内向扮演客户的 LLM 挖掘需求，并指挥另一个 LLM 编写出可运行的软件，以此考察产品感、系统思维与书面表达能力；该方案借鉴医学界的 OSCE 标准化病人考核，且坚持由人类做最终评判。

- 📉 **初级招聘崩塌**：斯坦福研究显示 22–25 岁开发者就业较 2022 年峰值下降近 20%，Anthropic 新招工程师中初级占比从 27% 跌至 9%，而资深岗位需求持续增长。
- 💀 **编码面试已死**：作者十余年来一直批评编码面试，如今 Anthropic 部分团队、Canva、Meta、Google 均已改用或试点 AI 辅助与技术理解类面试，但尚无公认方案。
- 💰 **自私但合理的理由**：初级产品工程师更便宜、更易招，而 2025–2026 年 71% 的岗位增长集中在资深工程师；不培养新人，整个行业将萎缩。
- 🏫 **常见替代方案都不靠谱**：付费实习慢且贵，创业公司无力承担；名校筛选只是"富家子弟"过滤器；"饥饿感""品味"等标准含义模糊；非结构化面试预测效度仅 0.19（结构化 0.42）。
- 🎯 **该考察什么**：产品感（从混沌信息中找出真问题、反驳表面需求）、系统级智力（在脑中装下整个系统、识别约束变化）、书面表达能力（无法用自然语言解释就无法有效提示智能体）。
- 🧪 **核心提案**：给候选人 1–2 小时，与一个掌握全部需求细节的 LLM"客户"对话，并指挥另一个（对所有人相同的）LLM 写出可运行、甚至已部署的真实软件。
- 📜 **规则设计**：可随时追问客户、可展示半成品、可多次推倒重来；但不允许"越狱"客户套取需求文档——现实中客户不会被这样骗。
- ⚖️ **评分与公平**：任务统一、与岗位相关，可高度贴近真实业务；用评审智能体自动生成并运行测试，但最终打分必须由人类完成，且需人工校准。
- 🩺 **并非新发明**：医学界自 1960 年代起就用 OSCE 标准化病人考核，学生面对同一演员、按清单评分，与本方案高度相似；科技界类似尝试仅有 Palantir 的拆解面试与初创公司 Promptster。
- 🚫 **不要全自动化**：模型评审与人类一致率仅相当于人类彼此间的一致率，且部分评审模型存在严重偏差；纽约市还要求对自动化招聘工具做年度偏见审计。
- 🔮 **前景**：方案目前仍是理论，尚未实测；但率先跑通的公司将在该岗位需求爆发时，获得一批可自我定义需求的廉价高能力开发者。

---

### [如何在不到 350 字节内让 postMessage 类型安全——Martian Chronicles，Evil Martians 团队博客](https://evilmartians.com/chronicles/how-to-make-postmessage-type-safe-in-under-350-bytes)

**原文标题**: [How to make postMessage type-safe in under 350 bytes—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/how-to-make-postmessage-type-safe-in-under-350-bytes)

typed-channel 是一个极小型的 TypeScript 库，用统一、类型安全的方式封装 postMessage，适用于 Web Worker、iframe、标签页和页面内事件总线；开发者只需定义一次消息名和载荷，TypeScript 就会在发送端和接收端进行检查。最新 0.11 版本新增可取消的请求/响应能力，取消请求时，对端正在执行的处理也会停止。

- 📦 **体积极小**：核心约 271 字节，包含 postMessage 传输约 341 字节，零依赖；请求/响应功能单独引入，约 1 kB。
- 🧩 **解决原生 postMessage 痛点**：消息名是普通字符串、载荷为 any、跨边界无类型检查、路由依赖 switch、监听器清理麻烦、各边界重复样板代码。
- 🔤 **一次定义消息契约**：通过 ClientMessages、WorkerMessages 等类型映射声明双向消息，emit 和 on 自动获得类型检查，拼写错误无法通过编译。
- 🔌 **传输与通道分离**：channel 负责消息类型，transport 负责跨边界传输；更换 transport 即可适配 Worker、iframe、BroadcastChannel、MessagePort、EventTarget 等场景。
- 🧹 **更安全的订阅管理**：on 返回取消订阅函数，避免手动保存 handler 再调用 removeEventListener，减少重复监听和内存泄漏。
- 🪟 **多场景复用**：同一套 API 可用于 Web Worker、iframe、页面内事件总线；也支持同时接入多个 transport，让一次 emit 同时到达当前标签页和其他标签页。
- 🛠️ **可自定义传输**：transport 只需实现 on 和 emit 两个函数；文章以 Figma 插件为例，展示用十几行代码封装 figma.ui.postMessage 和 parent.postMessage。
- 📨 **0.11 新增请求/响应**：createTypedRpcChannel 在 emit/on 之外增加 request/handle，请求参数和返回值均有类型，handler 抛错会让调用方 Promise 拒绝。
- ⏱️ **基于 AbortSignal 的取消与超时**：request 接受 AbortSignal，可用 AbortSignal.timeout(5000) 设置超时；取消时会通知对端并中止 handler 的工作，避免“结果没人要但仍在计算”。
- 🧭 **使用建议**：先安装 typed-channel，用 createTypedChannel 和消息映射处理单向消息；需要应答时再用 createTypedRpcChannel；遇到内置 transport 未覆盖的边界时自行实现 transport。

---

### [Web 无法承受 JavaScript 运行时单一文化 – console.log()](https://redmonk.com/kholterhoff/2026/10/27/js-runtime-monoculture/)

**原文标题**: [The Web Can’t Afford a JavaScript Runtime Monoculture – console.log()](https://redmonk.com/kholterhoff/2026/10/27/js-runtime-monoculture/)

文章围绕 JavaScript 运行时生态的整合风险展开：Deno 团队加入 Cloudflare 且 Deno 运行时将停止开发，使服务器端 JS 运行时进一步向少数实现集中；作者以 IE6 和浏览器引擎整合为鉴，担忧服务器端重演“单 culture”，削弱标准多样性、创新竞争与故障隔离能力。

- 😟 Deno 宣布团队加入 Cloudflare，Ryan Dahl 表示 Deno 运行时开发将在一年后停止，主要通用运行时进一步减少。
- 🧭 文章类比 IE6：曾占约九成浏览器份额后缺乏竞争，开发者被迫适配单一浏览器怪癖而非开放标准。
- 🔁 Firefox、Safari、Chrome 曾恢复浏览器竞争，但 Blink/Chromium 的扩张又导致浏览器引擎高度集中。
- 🖥️ 服务器端也有类似历史：Node.js 曾因治理问题停滞，贡献者分叉出 io.js，竞争压力促成 2015 年回归中立基金会治理。
- ⚙️ Deno 虽未超越 Node，却推动了 TypeScript、Web API、权限安全等特性，许多创新后来被 Node 吸收。
- 🧱 当前主要运行时多依赖浏览器引擎：Node、Deno、Cloudflare workerd 基于 V8，Bun 基于 JavaScriptCore。
- 📉 独立实现减少会削弱标准制定：Web 标准通常需要两个独立实现，WinterTC 等标准工作也需多元声音。
- 💥 单 culture 会放大系统性风险：Heartbleed 显示共享基础库的单一缺陷可影响大部分 Web，V8 同样存在集中风险。
- 🚀 挑战者消失会带走创新压力：Deno 推动安全与工具改进，Bun 推动速度竞争，竞争减少可能拖慢进步。
- 🌱 Deno 的独立分叉如 Ende、Dodo 已出现，但成熟度和可持续性仍待观察；Linux 的多发行版与多资金来源被视为多样性范例。
- 🗣️ Cloudflare 的 James Snell 强调“没有选择从来不是好事”，Bun、Deno、Node 等并存才能推动生态前进。
- ⚠️ 作者结论：Web 曾因持续建设和资助替代方案而走出 IE6 时代，如今 JS 运行时轨迹需警惕重演 IE6 式整合。

---

### [Handwired：将你的常规 JavaScript 代码变成神经网络](https://chenglou.me/handwired/)

**原文标题**: [Handwired: turn your regular JavaScript code into a neural net](https://chenglou.me/handwired/)

文章介绍了一种将普通 JavaScript 代码转换为神经网络的方法：无需训练、结果精确且完全可微，并可在无 GPU 的浏览器中运行。

- 🧠 将常规 JS 代码自动转换为神经网络结构，核心特点是“无需训练”且保持精确性。
- 🔄 代码仍完全可微，适合在浏览器中直接运行，不依赖 GPU。
- 🧮 示例中把条件表达式转换为 ReLU 组合：用 `relu(a - 4) - relu(a - 5)` 表示 `a > 4`。
- 🧩 转换后可继续用权重和层进行计算，示例展示约 9,909 个权重、130 层、0 次训练。
- 🖥️ 演示包括 Mini OS：用 JS 编写并转换后，支持大列表、动画、堆叠、滚动、拖拽、输入和图片等 DOM 渲染。
- 🎨 “Learned gallery”展示可解冻已编译程序的权重并进行实时训练。
- 🔍 搜索 100,000 个 JSON 文档的演示中，正则匹配、JSON 解析和高亮均由 JS 编写，再转换为 WebGPU 内核以实现大规模并行。

---

### [Pretext 演示](https://chenglou.me/pretext/)

**原文标题**: [Pretext Demos](https://chenglou.me/pretext/)

Pretext 提供一系列小型浏览器演示，展示无需在热路径中进行 DOM 测量即可计算文本高度、手动行路由，以及宽度紧凑的多行 UI 布局能力。

- 🪗 Accordion：根据 Pretext 计算的文本高度展开和折叠区块。
- 💬 Bubbles：紧凑的多行消息气泡，在保持相同行数的同时减少浪费空间。
- 🧩 Dynamic Layout：固定高度的编辑版式，支持感知障碍物的标题路由与连续流。
- 🔤 Variable Typographic ASCII：粒子驱动的 ASCII 艺术，对比比例字形测量与等宽版本。
- 📰 Editorial Engine：动画光球、实时文本重排、引文和多栏流，无需 DOM 文本测量。
- ⚖️ Justification Comparison：并排展示 CSS 两端对齐、贪心断词与 Knuth-Plass 段落布局，揭示“河流”和间距取舍。
- 🧾 Rich Text：富文本内联、代码片段、链接、标签、自定义 emoji 和图片一起布局，胶囊与图片保持完整，文本自然换行。
- 💬 Markdown Chat：虚拟化聊天演示，使用 marked 解析，富文本内联流助手处理段落内容，pre-wrap 处理围栏代码。
- ✂️ Ellipsis：按行数截断文本、路径中间省略号及“… more”链接，均在绘制前裁剪。
- 🧱 Masonry：文本卡片遮挡演示，高度预测来自 Pretext 而非 DOM 读取。

---

### [SerpApi：Google 搜索 API](https://serpapi.com/?utm_source=cooperpress-newsletter)

**原文标题**: [SerpApi: Google Search API](https://serpapi.com/?utm_source=cooperpress-newsletter)

未检测到需要总结的正文内容，目前无法生成文章摘要；请提供文本后再进行概括。
- 📄 请在“Use the following content:”后粘贴需要总结的文章内容。
- ✍️ 收到文本后，我会用中文按“概述 + 表情符号要点”的格式输出。
- 🔍 摘要将提炼关键信息、保留核心观点并控制篇幅。
- ✅ 每条要点都会以“-”符号开头，并配有合适表情符号。

---

### [x18n：i18n 文件，已检查并维护](https://x18n.dev/)

**原文标题**: [x18n: i18n files, checked and maintained](https://x18n.dev/)

x18n 是一款用于检查和维护 i18n 文件的工具，可读取项目中的 locale 文件与 translate 调用，报告缺失、未使用和异常的 key，并在不破坏原格式的前提下修改 locale 文件，适合人工、CI 与编码代理使用。

- 🧰 核心能力：读取 locale 文件与项目中所有 translate 调用，检查缺失、未使用和损坏的 key。
- ⚙️ 开箱即用：在项目根目录运行即可自动识别依赖中的 i18n 库并找到 locale 文件，无需初始配置。
- ✅ `x18n check`：像 `tsc --noEmit` 一样报告错误，出错时以退出码 1 结束，适合 CI。
- 🔎 `x18n get` / `search`：查看某个 key 在各语言中的值及代码使用位置，或根据界面文案反查 key。
- ✏️ `x18n rename`：跨所有 locale 和代码调用重命名 key，支持 `--dry-run` 预览 diff。
- 🖥️ `x18n ui` / `init`：浏览器中浏览编辑所有 key，并为代理提供 MCP；`init` 可生成 `x18n.config.ts`。
- 📊 项目状态：展示各 locale 的覆盖率，以及资源、key 和使用次数的统计。
- 🧩 多端一致：CLI、VS Code、UI 与代理读取同一配置并给出一致诊断。
- 🛠️ 框架与扩展：支持 vue-i18n、i18next、next-intl、ngx-translate、Laravel、Rails、Flutter 等，并可通过 YAML 或 TypeScript 插件扩展。
- 🔁 迁移支持：`x18n migrate i18n-ally` 可将 i18n-ally 的设置和自定义框架转换为 x18n 配置。

---

### [GitHub - lokalise/i18n-ally：🌍 适用于 VS Code 的一站式 i18n 扩展 · GitHub](https://github.com/lokalise/i18n-ally)

**原文标题**: [GitHub - lokalise/i18n-ally: 🌍 All in one i18n extension for VS Code · GitHub](https://github.com/lokalise/i18n-ally)

i18n-ally 是 Lokalise 维护的 VS Code 一站式国际化（i18n）扩展，提供翻译管理、代码提取、缺失翻译报告、机器翻译等能力，并已发布 v2.0 的 Editor UI 与 Review System。

- 🌍 项目定位：面向 VS Code 的 all-in-one i18n 扩展，代码托管于 GitHub，采用 MIT 许可证。
- ⭐ 社区数据：约 4.9k stars、415 forks、402 issues、72 PRs、28 watchers、1,767 commits。
- 🎉 v2.0 更新：新增 Editor UI 和 Review System，并提供从 v1.x 迁移的说明。
- ✍️ 核心功能：内联注释、悬停与直接操作、集中管理翻译、从代码提取翻译、报告缺失翻译、机器翻译、JSON/YAML 注释。
- 🧩 兼容能力：支持多根工作区、远程开发、多种主流框架、关联 locale 消息，扩展自身也使用 i18n。
- 🗣️ 多语言支持：扩展界面支持英语、简繁中文、挪威语、西班牙语、日语、荷兰语、葡萄牙语、法语、瑞典语、乌克兰语、俄语、德语、泰语、土耳其语、韩语、匈牙利语等。
- 🤝 贡献与致谢：欢迎协助翻译；项目受 think2011/vscode-vue-i18n 启发，Vue SFC 支持由 vue-i18n-locale-message 提供。
- 📚 资源入口：提供文档、FAQ、配置说明、支持格式列表和贡献指南。

---

### [GitHub - earendil-works/djs · GitHub](https://github.com/earendil-works/djs)

**原文标题**: [GitHub - earendil-works/djs · GitHub](https://github.com/earendil-works/djs)

djs 是用 no_std Rust 编写的轻量级 JavaScript/TypeScript 引擎，主要面向 wasm32，用于在 pi codemode 中替代 QuickJS，执行模型编写、调用工具、处理结果并输出数据的脚本；核心设计围绕可暂停 VM、低成本宿主数据传递、确定性执行和运行持久化。

- 🧭 **项目定位**：小型 JS/TS 引擎，主要服务 wasm32，在 pi codemode 中替代 QuickJS，运行模型生成的工具调用脚本。
- 🧱 **核心架构**：所有 VM 状态存放在单个字节 arena 中，用 u32 偏移寻址；创建 VM 只需复制预构建镜像，挂起成本低。
- ⏸️ **随处暂停**：解释器不依赖 Rust 栈递归执行 JS 调用，可在指令间、宿主调用、getter、回调、promise job、generator 和 async 函数中暂停并恢复。
- 🔌 **低成本数据传递**：入参使用紧凑 wire format，出参由宿主直接读取堆，VM 内无需序列化。
- 🛠️ **编译与内建**：无 AST 的单遍编译为栈字节码，解析时擦除 TypeScript；内建库用严格 TS 子集编写，热路径可编译为可恢复 Rust 状态机。
- 💾 **持久化与确定性**：等待工具的运行可导出为 continuation dump（JavaScript 程序），后续可加载或带原因拒绝；时钟、随机数和弱引用由宿主提供，相同输入产生字节一致堆镜像。
- ✅ **一致性表现**：test262 active 组通过 38,069/38,109（99.9%）；差分语料 539/550；pi codemode 测试 221/226。有意跳过 Intl、Temporal、SharedArrayBuffer/Atomics、Annex B、sloppy mode、direct eval、modules 等。
- ⚡ **性能表现**：wasm 下指令数比值显示 tight loop 0.42、属性访问 0.49、字符串 0.51 等较低；map/filter/reduce 2.92、forEach 1.49 等回调密集场景较高，是主要差距。pi 自身基准为 4.2 ms vs 5.3 ms，启动 1.0 ms vs 3.9 ms。
- 📦 **体积与启动**：djs_wasm.wasm 为 1,471 KB（gzip 525 KB，brotli 423 KB），其中 base snapshot 186 KB；wasm 创建 VM 约 40 µs，Sandbox 约 60–140 µs。
- 🚀 **构建与使用**：支持 cargo build、run、repl、disasm、strip-types 及 build-wasm.sh；JS 宿主包 @djs/host 提供 Sandbox、runAsync、begin/dump，js/pi/vm.ts 实现 pi codemode VM 合约。
- 🧪 **测试与工程流程**：包含 cargo test、test262 ratchet、差分语料、JS host 测试；gate.sh 把关 main，merge-to-main.sh 负责合并；crates 分层覆盖 core、bgen、prelude、wasm、cli、test262、difftest、bench、docs。
- 📚 **文档体系**：docs/guide、ARCH.md、TESTING.md、decisions、compiler、objects、host、wire、cli、builtins README 及 AGENTS/work README 提供设计与流程说明。
- 📈 **仓库概况**：224 stars、4 forks、1 watcher、1,526 commits，主分支为 main。

---

### [](https://flask.palletsprojects.com/en/stable/)

**原文标题**: [Welcome to Flask — Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/)

这是 Flask 3.1.x 官方文档首页，介绍 Flask 是轻量级 WSGI Web 应用框架，强调快速上手并可扩展到复杂应用；文档涵盖入门、用户指南、教程、常见模式、API 参考、部署、安全与扩展开发等内容。

- 🚀 Flask 是轻量级 WSGI Web 框架，目标是让入门快速简单，同时支持扩展到复杂应用。
- 📦 Flask 依赖 Werkzeug WSGI 工具包、Jinja 模板引擎和 Click CLI 工具包，查阅资料时也应参考它们的文档。
- 🧭 入门路径包括 Installation、Quickstart 和 Tutorial，常见模式见 Patterns for Flask。
- 📘 User’s Guide 覆盖配置、路由、模板、请求数据、响应、会话、日志、错误处理、测试、调试、信号、类视图、应用生命周期、蓝图、扩展和 CLI 等。
- 🧩 Tutorial 展示从项目布局、应用设置、数据库、蓝图视图、模板、静态文件到测试和部署的完整小型应用。
- 🛡️ 文档包含安全注意事项（XSS、CSRF、JSON 安全、安全头、Host 头校验）和生产部署指南。
- ⚙️ API Reference 提供应用对象、蓝图、请求/响应、会话、测试客户端、全局变量、模板渲染、配置和信号等详细参考。
- 📚 Additional Notes 涉及 Flask 设计决策、“micro”含义、异步/ASGI 支持、扩展开发指南、贡献、BSD-3-Clause 许可证和版本变更。
- 🏷️ 当前文档对应 Flask 3.1.x，变更记录最新列出 3.1.3，版权归 Pallets 所有。

---

### [GitHub - tractordev/webframe：像运行程序一样运行网页 · GitHub](https://github.com/tractordev/webframe)

**原文标题**: [GitHub - tractordev/webframe: Run a web page like a program · GitHub](https://github.com/tractordev/webframe)

webframe 是一个跨平台命令行工具与 Go 库，可在隐藏的系统 WebView 中加载 URL 或本地文件，并将网页控制台、异常与 JavaScript 求值连接到终端，让网页像本地程序一样运行。

- 🌐 跨平台：macOS 使用 WebKit，Linux 使用 WebKitGTK，Windows 使用 WebView2；通过 glaze/purego 调用系统组件，通常是单个小二进制，多数平台无需 cgo。
- 🎯 典型用途：运行 WASM、WebGPU、Web Audio、DOM 等浏览器专用代码；后台长驻页面；REPL 调试；脚本化测试；headless 运行 SPA/模拟器；也可作为 Go 库实现跨平台隔离。
- 📦 安装：从 Releases 下载对应平台压缩包，或用 Go 1.27+ 源码构建 `make build`；Linux 需 WebKitGTK 4.1/6.0 和显示/Xvfb，Alpine 使用 musl 版并安装 webkit2gtk-4.1、xvfb。
- 🚀 基本用法：`webframe [flags] <url|file>`，参数必填，可用 `about:blank`；Linux 无显示时自动启动私有 Xvfb。
- 🧰 关键参数：`-c` 交互控制台、`-x FILE` 加载后运行脚本、`-i FILE` 页面脚本前注入、`-E NAME[=VALUE]` 暴露环境变量、`-t DURATION` 超时、`-e` 首次异常退出、`-y` 接受对话框、`-w [WxH]` 显示窗口、`-d` 开发者工具、`-p` 隐私模式。
- 🖨️ 输出行为：`console.log` 原样输出到 stdout，其他 console 方法带前缀；异常、未处理 Promise 拒绝、资源加载失败和页面加载失败输出到 stderr，并尽量保留堆栈细节。
- ⚠️ 错误细节限制：`file://` 页面或跨域无 CORS 的脚本异常只显示 `Script error.`，需要完整错误时应通过 HTTP 提供页面。
- 💬 对话框默认按“取消”处理，`confirm` 返回 false、`prompt` 返回 null；使用 `-y` 时接受，`confirm` 为 true、`prompt` 返回默认文本。
- 🧑‍💻 控制台模式：`-c` 在页面加载后从 stdin 逐条求值，支持跨行语句、保留 var/函数声明、等待 Promise，并在 stdin 关闭后退出；无终端时可按流处理，适合脚本。
- 🧪 脚本与测试：`-x` 在 load 后运行文件并等待 Promise；抛错即退出 1；用 `webframe.exit(code)` 或 `window.close()` 控制退出，配合 `-t` 防止 CI 挂起。
- 💉 注入与测试辅助：`-i` 在每次页面加载和导航前于顶层 frame 注入脚本，适合 stub、fetch hook、测试辅助；`-E` 把指定环境变量以字符串暴露到只读 `webframe.env`，便于隐藏密钥但页面所有脚本可读。
- 🧭 生命周期与退出码：窗口关闭、SIGINT、SIGTERM、stdin 关闭等退出 0；`-e` 异常、`-x` 脚本抛错、首载失败退出 1；错误用法退出 2；`-t` 超时退出 124；SIGHUP 重新加载原始 URL。
- ⏱️ 隐藏不降速：各平台关闭节流，隐藏页面中的定时器和 `requestAnimationFrame` 仍全速运行，并让页面认为自身可见且有真实视口。
- 🐳 Docker：提供 Alpine + WebKitGTK + Xvfb 镜像，约 580 MB，以非 root 用户在 `/work` 运行；需挂载 `-x`/`-i` 文件，并用 `docker run -e` 传入 `-E` 变量。
- 🧱 Go 库：CLI 是 `webframe` 包的薄封装；`New` 创建 Frame，需主 goroutine 调用 `Run`；提供 `Navigate`、`Reload`、`Eval`、`EvalContext`、`Terminate`，除 `New`/`Run` 外可从任意 goroutine 调用。
- 🛠️ 构建与测试：构建使用 `CGO_ENABLED=0` 并可交叉编译；Alpine musl 例外需 cgo+zig；`.dev/vm` 用 Lima 在 Ubuntu、Alpine、macOS 15、Windows 11 ARM64 上跑冒烟测试。
- 📚 示例与许可：包含 hello、bench、timers、csp、todo、links、status、v86 等示例；项目采用 MIT 许可证，约 255 stars。

---

### [请稍等……](https://kevs3d.co.uk/phoria2/)

**原文标题**: [One moment, please...](https://kevs3d.co.uk/phoria2/)

当前页面处于加载状态，系统正在验证请求，需要用户稍候。

- ⏳ 页面显示加载提示
- 🔐 系统正在验证请求
- ⌛ 请耐心等待验证完成

---

### [尸鬼](https://shiki.style/)

**原文标题**: [Shiki](https://shiki.style/)

该内容介绍了一款强调“准确且美观”的文本语法高亮能力，其底层由 TextMate 语法驱动，并与 VS Code 使用相同引擎，且会随 VS Code 的更新而持续改进。

- 🎯 主打准确且美观的语法高亮体验
- 🧩 由 TextMate 语法提供支持
- 💻 与 VS Code 使用相同引擎
- 📈 随 VS Code 的更新而不断改进

---

### [发布 11.1.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.1.0)

**原文标题**: [Release 11.1.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.1.0)

Preact 11.1.0 于 10 月 31 日发布，新增 React Compiler 兼容运行时，并带来 VNode 识别加固、布局副作用错误隔离、SVG/宽高比单位修复和类型增强；使用 Signals 或 SSR 包时需注意兼容版本要求。

- 📅 Preact 11.1.0 正式发布，包含功能、修复和类型更新。
- 🚀 新增 `preact/compat/compiler-runtime`，支持使用 React Compiler 编译的应用。
- 🛡️ 通过共享 symbol 标记强化 VNode 识别。
- 🧩 将 layout-effect 错误隔离到抛错组件，避免影响无关 effects 和生命周期回调。
- 🎨 在 compat 中不再为无单位的 SVG paint 和 aspect-ratio 值追加 `px`。
- 📝 类型定义允许所有有效 input 类型使用 `list` 属性。
- ⚠️ 新 VNode 标记要求 `@preact/signals` 2.11.4+ 和 `preact-render-to-string` 6.8.2+（使用这些包时）。
- 👏 贡献者包括 JoviDeCroock、dylanpulver 和 playlikeboy。

---

### [发布 v4.0.0 · porsager/postgres · GitHub](https://github.com/porsager/postgres/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · porsager/postgres · GitHub](https://github.com/porsager/postgres/releases/tag/v4.0.0)

postgres.js v4.0.0 是一次底层全面重写：连接池、连接、协议、启动和套接字层均被重写，公共 API 大体保持与 3.4.9 兼容，但在参数类型推断、运行时支持、事务/连接语义等方面有重要变更；同时修复多项安全与正确性问题，新增连接调度、追踪、Channel Binding、Cloudflare Workers 支持，并显著提升性能与测试覆盖。

- 🔄 底层重写：查询、helper、事务、游标、COPY、listen、subscribe、大对象和 options 基本沿用 3.4.9，但内部实现全部更新。
- 🛡️ 安全修复：连接参数中的 NUL 字符不能再注入额外参数；名为 `__proto__` 的列会作为自有属性处理，避免原型污染。
- ⚠️ 参数类型变更：v4 默认由服务器推断参数类型（`infer: false`），`Date`、`boolean`、`Buffer`、`bigint` 等不再由客户端标注；非 UTC 下 `timestamp/date` 按 UTC 处理，必要时需显式 cast；`infer: true` 保留 v3 行为。
- 📦 运行时与模块：仅支持 ES module；要求 Node.js 20+、Bun、Cloudflare Workers，Deno 通过 Node 兼容层；CommonJS/Deno 构建移除，Node 20.19/22.12+ 可用 `require` 加载。
- 🚫 移除 `sql.array()`：直接传数组并在需要时 cast，如 `${ids}::int[]`；调用 `sql.array()` 抛 `ARRAY_REMOVED`。
- 🔐 事务与连接语义更严格：服务器 `ROLLBACK` 的 `COMMIT` 会拒绝；已 release 的连接或已结束事务再查询会拒绝；不安全 `begin` 抛 `UNSAFE_TRANSACTION`；事务内无法构建/序列化的查询会中止事务。
- 🧭 新连接调度：连接繁忙时按预计完成时间流水线化查询，慢查询集中处理；混合负载下快查询 p99 降低 2 到 100 倍，1ms 查询 p99.9 从 792ms 降至 5ms；`scheduler: false` 可回退。
- ⏱️ 新增控制能力：`queue_timeout` 控制等待连接超时；`.signal(abortSignal)` 可取消等待中或运行中的查询；游标在批次间取消会停止并关闭 portal。
- 🧩 SQL 构建增强：`sql` 与 `.join()` 支持片段/值拼接；嵌套 `sql.begin` 使用 savepoint；`sql.rollback()` 回滚事务或 savepoint；事务内任意位置可流水线化；支持按名称自定义类型（如 pgvector）。
- 🔁 资源与连接管理：`using/await using` 自动释放连接/关闭池；`unref_sockets` 允许进程空闲退出；`min/idle_timeout` 控制保活连接；`user` 可为函数以轮换凭据；支持 `PGPASSFILE`/`~/.pgpass`；支持命名参数。
- 📡 复制与订阅增强：持久化复制槽 `slot: 'name'`，处理函数完成后才确认事务，失败可重投，支持异步处理；`subscribe` 增加 `truncate` 事件及 `lsn/time/xid`；断线重连带退避。
- 🔒 传输安全：TLS 上支持 SCRAM-SHA-256-PLUS 通道绑定，`channel_binding` 默认 `prefer`；Node.js 支持 `sslnegotiation: 'direct'` 直连 TLS（PostgreSQL 17+）；Cloudflare Workers 通过 `cloudflare:sockets` 支持。
- 🔍 可观测性：`query.text`/`query.parameters` 可在发送前查看；`sql.stats` 展示连接状态；提供 `postgres:query/connect/transaction` 等 tracing 通道及 `pool/notice` 通道，无订阅者时无开销。
- 🧠 预编译与游标：列类型变化时预编译语句会重新准备；`sql.close()` 完成查询后关闭连接且池仍可用；事务/保留连接支持多个命名游标。
- 🐛 正确性修复：33 个回归测试覆盖的 bug 被修复，包括冷池只开一个连接、错误字段名 `data_type_name`、`JSON.stringify(PostgresError)`、游标回调等待、大对象 `end`、Bun/Workers 问题、语句重名 `42P05`、URL/IPv6/socket 解析、查询答案错配等。
- ⚡ 性能优化：参数类型已知的语句一次往返完成 prepare/describe/run；`int2/int4/oid/bool` 直接按字节解码；结果形状稳定后使用编译函数构建行；每连接单一增长缓冲区，减少分配。
- 🧪 测试完善：新增协议/类型/查询构建/错误单测、带故障注入的模拟测试、按领域拆分的集成测试；CI 覆盖 PostgreSQL 14-18、Node 20/22/24、Bun、Deno、Cloudflare Workers 和 TypeScript 类型测试，并统计覆盖率。

---

### [短信欺诈检测与预防 | Fingerprint 设备智能](https://fingerprint.com/use-cases/sms-fraud/?utm_source=JSWeekly110326&utm_medium=newsletter)

**原文标题**: [SMS Fraud Detection and Prevention | Fingerprint Device Intelligence](https://fingerprint.com/use-cases/sms-fraud/?utm_source=JSWeekly110326&utm_medium=newsletter)

通过引入 Fingerprint 作为第一层防护，可减少短信一次性验证码的发送，并替代约 95% 的短信验证；同时将每次登录与唯一设备标识关联，便于识别和阻断欺诈行为，即使对方使用 VPN、无痕模式或跨多个账户也能应对。

- 🔐 增加 Fingerprint 第一层防护，减少 SMS OTP 使用
- 📉 可替代约 95% 的短信验证
- 🆔 每次登录关联唯一设备标识，提升识别能力
- 🚫 更易识别并阻断欺诈活动，包括 VPN、无痕模式和跨账户行为

---

### [Expo：用于构建应用软件的智能体移动基础设施](https://expo.dev/)

**原文标题**: [Expo: Agentic Mobile Infrastructure for building application software](https://expo.dev/)

Expo 定位为面向代理式移动开发的基础设施平台，提供从开发、测试、部署到监控的一体化工具链，帮助团队用单一代码库构建并发布原生应用，同时让 AI 编码代理可借助云模拟器自主验证应用。

- 🚀 核心定位：Agentic mobile infrastructure，结合 CLI、Skills、MCP 等构建代理式移动工作流。
- 🧱 四大环节：Develop 开发、Test 测试、Deploy 部署、Monitor 监控。
- 🤖 AI 原生：提供 Expo Claude Code connector，面向 AI 原生应用开发。
- 📱 开发测试：Expo Go 真机测试；Simulators 云模拟器可由代理按需驱动，无需 Mac，并附截图、录屏和日志作为验证。
- 🚢 发布分发：Build 构建并分发 Android、iOS、Web；Update 提供 OTA 更新、渠道与灰度控制；Launch 简化 App Store 上架。
- 🔁 自动化：Workflows 自动执行构建、测试和发布，并可在每次变更时运行测试套件。
- 📊 监控：Observe 提供崩溃信息、性能指标和 Update 采用率，发现问题可通过 Update 修复。
- 🧩 SDK：Expo SDK 积累 10+ 年，提供 100+ 生产 API，一次安装，支持 React Native、Swift、Jetpack Compose、Kotlin 等原生代码。
- 📈 规模数据：3M+ 开发者、50K+ GitHub stars、7M+ 周下载、100K+ 活跃开发者、500K+ 项目、100K+ 日构建。
- 💬 社区：80% React Native 开发者选择 Expo，Discord 70K+ 成员，开发者评价积极。
- ✅ 信任合规：获 Meta 推荐，React Foundation 成员，SOC 2 Type II、GDPR、CCPA、SSO 合规。

---

### [GitHub - Agent-Field/CodeAF：面向开放模型的开源软件工厂 · GitHub](https://github.com/Agent-Field/CodeAF)

**原文标题**: [GitHub - Agent-Field/CodeAF: Open-Source Software factory for Open Models · GitHub](https://github.com/Agent-Field/CodeAF)

CodeAF 是 AgentField 推出的开源“软件工厂”，面向开放模型优化编码工作流，以单个 Go 二进制运行并采用 Apache-2.0 许可；它把多项目、多会话和代理任务集中到一个窗口，并声称在 DeepSWE 基准上以最低单题成本排名第一。当前为早期预览，功能覆盖子代理、自动任务拆分/测试/合并、模型编排、自动化和无头执行。

- 🏭 **定位**：将调度、检查与合并自动化，用一个窗口管理本机所有项目和对话，任务通过检查后自动落到工作分支，不会直接进入 main/dev/release。
- 🥇 **基准表现**：在 DeepSWE 的 113 个真实 GitHub issue 上，senior-dev 子代理对比十种编码 harness 解决最多问题、每题成本最低，领先 Claude Code、Codex、OpenCode 等。
- 🧱 **产品形态**：Go 单二进制、约 53MB、Apache-2.0；首次启动可连接 OpenRouter，也支持 Codex、DeepSeek、GLM、Kimi、MiniMax、Qwen、Ollama 及 OpenAI 兼容端点。
- 🗂️ **工作方式**：用自然语言描述问题，CodeAF 可把一句话拆成多个任务，在各自仓库副本和分支上并行执行，对话仍可继续使用。
- 🤖 **内置子代理**：senior-dev 负责改代码并运行构建测试，sec 做本地安全审计，review 审查 GitHub PR；还可设计并保存自定义 harness 处理重复工作。
- 🧠 **模型编排**：每个任务由 worker、planner、checker 等席位自动选模型，另有 reflex/small 处理小调用；可按任务使用 best/cheap、固定席位模型或限制为开放权重模型，默认单任务预算上限 5 美元。
- 📊 **Model Pool**：默认共享无文本的模型测量数据，可查看待发送内容并关闭；提供签名索引，也支持自建 relay。
- ⏰ **自动化**：用自然语言设置提醒、定时任务和监视；错过的任务会在 CodeAF 重新打开时补跑一次，并保留历史记录。
- 🖥️ **无头与远程**：`do`/`exec`/`run` 支持 CI、cron、脚本和 JSON 输出；屏幕在本地运行、会话在远程 devbox 运行，断线可重连，手机也可通过 ssh 接入同一对话。
- ⚡ **性能**：单二进制约 53MB，16 个空闲会话约 507MB，单轮峰值约 122MB，恢复 50 轮会话约 145ms，显著小于对比工具。
- 🔒 **遥测与反馈**：默认发送匿名使用计数，不包含提示、代码、路径、身份等信息；可通过设置、`CODEAF_TELEMETRY=off` 或 `DO_NOT_TRACK=1` 关闭。项目仍处于早期预览，鼓励通过 Discord 或 issue 反馈问题。

---

### [Chrome 157 中的 HTML-in-Canvas：在 2D、WebGL 和 WebGPU 中实现交互式 DOM | 博客 | Chrome 开发者](https://developer.chrome.com/blog/html-in-canvas)

**原文标题**: [HTML-in-Canvas in Chrome 157: Interactive DOM inside 2D, WebGL, and WebGPU  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/html-in-canvas)

Chrome 157 正式稳定发布 HTML-in-Canvas API，让 HTML DOM 内容可以渲染进 `<canvas>`，并在 2D、WebGL、WebGPU 中保持交互性、可访问性和浏览器原生能力，从而结合 DOM 的丰富功能与 canvas 的高性能图形控制。

- 🚀 **正式发布**：HTML-in-Canvas API 在成功完成 Origin Trial 后，随 Chrome 157 稳定版上线，发布日期为 2026 年 10 月 26 日。
- 🧩 **解决核心矛盾**：过去开发者要在 `<canvas>` 的高性能像素控制和 HTML 的语义化、可访问性、表单与浏览器集成之间做取舍，现在可以兼得。
- ♿ **无障碍与交互增强**：canvas 内的 HTML 内容支持屏幕阅读器、文本选择、复制粘贴、右键菜单、查找、翻译、自动填充和拼写检查。
- 🖼️ **保留 DOM 能力**：支持文本布局与格式化、多行/双向文本、CSS 样式、表单控件，以及浏览器扩展和 DevTools 调试。
- 🔍 **可索引与可导出**：Web 爬虫和 AI 代理可索引渲染进 2D/3D 场景的 DOM 内容；完整 canvas 合成内容可导出为图片或视频流。
- 🎮 **主要用例**：适用于大型 canvas 应用、3D 场景与游戏、媒体编辑与导出、着色器驱动的表达型 UI 等场景。
- 🛠️ **快速上手**：为 canvas 设置 `content="drawable"`，给子元素添加 `drawable`，2D 中使用 `drawElementImage()` 绘制；3D 中可通过 `updateElementGeometry()` 同步 DOM 与像素几何。
- 🧱 **框架生态支持**：Three.js 提供 `THREE.HTMLTexture`，PlayCanvas 支持 `setSource()`，Babylon.js 提供 `BABYLON.HtmlTexture`，PixiJS v8.19.0 支持 `HTMLSource`，另有 CanvasUI 组件库。
- 🛟 **兼容与回退**：可通过检测 canvas 的 `content` 属性判断 API 支持情况；不支持时可回退到浮动 HTML 覆盖层或 `html2canvas`、`dom-to-image` 等第三方方案。
- 📚 **后续资源**：官方提供完整技术文档、Modern Web Guidance、WICG GitHub 反馈渠道和社区示例，便于进一步探索与落地。

---

### [Canvas 内嵌 HTML 的 WebGL 示例](https://chrome.dev/html-in-canvas/)

**原文标题**: [HTML-in-Canvas WebGL Examples](https://chrome.dev/html-in-canvas/)

该页面展示了实验性“HTML in Canvas”API 的一系列演示，旨在将真实 HTML 内容渲染进 WebGL 画布，实现 3D 变换、交互与视觉效果；演示分为沉浸式 3D 体验、核心能力测试与框架支持三大类。

- 🎮 沉浸式 3D 体验：提供基于原生 WebGL 与 Three.js 的 3D 交互广告牌，并支持在 3D 广告牌上播放视频
- 🗾 3D 标签与翻译：展示东京 3D 标签的多语言翻译效果
- 📖 3D 交互书籍：包含书页角落翻卷（Book Corner Curl）动效演示
- 🌊 着色器特效：展示流体棱镜（Fluid Prism）着色器与可变形 HTML 页面
- 🅰️ 创意排版：用 Typebeat 演示基于 Canvas 的布局排版
- 🐉 3D 模型渲染：包含 Stanford 龙模型与 PBR 材质的猛犸象渲染
- 👓 交互演示：展示可交互眼镜和物理交互效果
- 🔤 核心能力测试：覆盖复杂文本渲染、画布内视频、internalFormat 颜色、CSS 滤镜、D3 数据可视化与交互表单
- 🧩 进阶特性：包括离屏 HTML-in-Canvas、多画布轮播、内嵌 iframe 与 TypeScript 演示
- 🛠 框架支持：兼容 Three.js、PixiJS 与 Babylon.js 等主流 3D 与渲染框架

---

### [CheerpJ 5.0：浏览器中的 Java 21/25、完整 OpenJDK 以及全新的 WasmGC 引擎](https://labs.leaningtech.com/blog/cheerpj-5.0)

**原文标题**: [CheerpJ 5.0: Java 21/25 in the browser, full OpenJDK, and a new WasmGC engine](https://labs.leaningtech.com/blog/cheerpj-5.0)

CheerpJ 5.0 是面向浏览器的完整 OpenJDK/WebAssembly 发行版，支持在浏览器中运行和编译现代 Java 应用；本次重点包括 Java 21/25 支持、完整 JDK、实验性 WasmGC 引擎，并为 2027 年初的 CheerpJ 6.0 稳定版铺路。

- 🚀 2026 年 11 月 2 日发布 CheerpJ 5.0，核心目标是让现代 Java 应用和库直接在浏览器中运行。
- ☕ 新增 Java 21 和 Java 25 支持，连同 Java 8、11、17，完成 2025 年 2 月公布的 Java LTS 对齐路线图。
- 🧰 首次为所有支持版本提供完整 JDK 而非仅 JRE，使 `javac` 和 `jshell` 可在客户端运行，从而支持在浏览器中编译 Java。
- ⚙️ 架构由 C++ 编写的 JVM/JIT 编译为 WebAssembly，并包含完整未修改的 OpenJDK（含 JNI 层）及虚拟化系统层。
- 🔍 基于 Java 字节码运行，不要求源码，支持反射、运行时类生成、自定义类加载器、多线程与同步，也兼容 Kotlin、Scala 和混淆 JAR。
- 🧪 引入实验性 WasmGC 执行引擎：新解释器与第二 JIT 后端，Java 对象变为 WasmGC 对象，热代码编译为 WebAssembly，内存由浏览器 GC 管理。
- 🎮 WasmGC 有望显著改善启动和运行性能，并简化与 Wasm 原生库的交互，为 LWJGL 3、现代 Minecraft 及模组铺路。
- ⚠️ WasmGC 目前不稳定且需手动启用，要求 Chrome/Edge 137+、Firefox 153+、Safari 27+，不建议用于生产；CheerpJ 6.0 计划于 2027 年初实现生产可用。
- 🖥️ 可运行大型 Swing/AWT 桌面应用，支持自定义 Look & Feel、多窗口、剪贴板和打印；JavaFX 与 SWT 暂不支持但在规划中。
- 🧱 Browsercraft 直接获取 Mojang 原始 `client.jar` 并在浏览器中未修改运行，无需反编译，是重要压力测试与展示案例。
- 🔗 Library Mode 允许 JavaScript 通过 `async/await` 调用 Java 库、对象、数组和原生方法，例如在客户端用 iText 生成 PDF。
- 🧑‍💻 集成 BrowserCode 后，可在浏览器中修改、用 `javac` 编译并运行现代 Java 代码。
- 🛠️ 5.0 还提升 Java 11/17 稳定性，优化类文件解析、JIT、JAR 下载性能，并改进拖放、剪贴板与移动端支持。
- 🗺️ 后续计划包括稳定 Java 25、WasmGC 生产化、提供 NPM 包与现代接口、保持与 Java LTS 最多 6 个月延迟，以及基于 BrowserPod 内核重建 syscall 层。
- 📜 CheerpJ 为商业软件，个人、教育、业余、评估等场景有免费社区许可；商业许可按桌面/应用授权，企业可自托管、再分发并获得支持，非营利和教育机构有折扣。

---

### [](https://simonwillison.net/2026/Oct/28/vibe-game-development/)

**原文标题**: [The October inflection point for vibe game development](https://simonwillison.net/2026/Oct/28/vibe-game-development/)

2026 年 10 月，Simon Willison 认为“氛围游戏开发”迎来新的拐点：以 Claude Opus 5.5 为代表的模型已能仅凭自然语言提示生成真正好玩、可玩的浏览器游戏，并在游戏设计、3D 建模和音乐生成等方面显著进步，游戏开发门槛被大幅降低。

- 🎮 **核心判断**：继 2025 年 11 月编码智能体拐点之后，2026 年 10 月是“氛围游戏开发”的拐点，模型开始具备做出“有趣游戏”的能力。
- 🧠 **关键能力**：Claude Opus 5.5 在 3D 建模、音乐生成和游戏设计上有明显提升，尤其能理解“让它更有趣”这类模糊指令。
- 🌳 **Tree Appreciator**：用 Claude 普通聊天一次提示生成，基于 three.js 的“欣赏树木差异”小游戏，无需迭代，画面和体验令人愉悦。
- 🏰 **Emberwick**：从俯视角奇幻 RPG 引擎原型扩展为完整游戏，有剧情、魔法系统、洞穴巨魔等，约 15 分钟流程，但需较多试玩和修复。
- 🤖 **Battle Drones**：最成功项目，Command & Conquer 风格 RTS，支持 2–4 人多人、地图生成、回放和 LLM 对战，已以 Apache 2.0 开源，并有社区分支 Panache。
- 🎃 **Pumpkin Farmer / Quarter Sun Cove**：受半月湾南瓜节启发，动物角色的温馨南瓜种植模拟器，包含大量彩蛋和细节，但玩法仍较复杂、尚在迭代。
- ⏱️ **投入极低**：这些项目每个作者投入不超过 4 小时，主要靠 Claude Code 长时间生成，说明少量创意输入已能产出可玩成果。
- 🧪 **对比模型**：GPT-6 Astra 也能构建游戏，但“趣味感”暂不及 Opus 5.5；作者预计 OpenAI 年底前会追上。
- ⚔️ **社区争议**：氛围编码游戏同时涉及 AI 生成美术、音乐、写作和代码，可能加剧玩家与开发者对 AI 素材的反感，并导致社区分化。
- 🚀 **未来机会**：真正值得期待的是有人认真投入创意、品味、试玩和迭代，做出“没有 AI 就不会存在”的独特游戏。
- 🛠️ **实践建议**：可从“Build a mobile-friendly three.js game where...”开始，用 ChatGPT 或 Claude 快速做原型；进入概念验证后改用 Codex 或 Claude Code；效果不够好时加上“Make it a LOT more fun”。

---

### [Game Off 2026：主题是 SHIFT - GitHub 博客](https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/)

**原文标题**: [Game Off 2026: The theme is SHIFT - The GitHub Blog](https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/)

GitHub 第 14 届年度游戏创作马拉松 Game Off 2026 于 2026 年 11 月举行，主题为“SHIFT”（切换/转变），鼓励开发者以各种方式诠释该主题，并在 2026 年 12 月 1 日 13:37 PST 前提交作品；活动规则宽松、欢迎新手，允许使用成熟引擎和 AI 辅助开发，提交后将由参与者互相投票评选。

- 🎮 **活动概况**：GitHub 年度为期一个月的游戏创作马拉松 Game Off 迎来第 14 届，多年来已有数千名开发者参与，作品从精致平台游戏到奇思妙想实验应有尽有。
- 🔀 **主题 SHIFT**：可理解为换挡、切换视角、变换维度、位移比特、上夜班，甚至做一款只能用 Shift 键操作的游戏，创意诠释完全自由。
- 📅 **关键截止**：须在 2026 年 12 月 1 日 13:37 PST 之前把代码推送到 GitHub，并在 itch.io 上完成提交（仅推代码不算参赛）。
- 💡 **灵感示例**：双键操作游戏、换挡改变重力/时间的赛车、旋转镜头让墙面变地板的视角解谜、双现实切换的平台跳跃、变形冒险、便利店夜班恐怖、甩锅侦探喜剧、位运算解谜等。
- 🧠 **实用建议**：先专注一个核心机制和一个可玩关卡，再考虑扩展；也可用 GitHub Copilot 提供主题与限制条件来头脑风暴概念。
- 🛠️ **参与方式**：单人成队均可，语言、引擎、框架、素材任选；需 GitHub 账号与公开仓库存放源码，并在 itch.io 加入 jam。
- 🗳️ **投票机制**：提交关闭后由参与者互评，投票截至 2027 年 1 月 1 日 13:37 PST，评选总体、玩法、画面、音频、创新与主题诠释等奖项，结果发布于 GitHub 博客与社交渠道。
- 📜 **宽松规则**：项目须在 jam 期间从零开始（模板与起始项目可用），许可证自定、开源鼓励但非必需，商业/委托/原创素材均可，AI 辅助允许但提交时需说明使用情况。
- 🧰 **工具推荐**：Godot、Unity、Unreal、Phaser、Pygame、Bevy、LÖVE、Flame、Ebitengine、Defold、libGDX、HaxeFlixel、raylib、PICO-8、TIC-80 等。
- 🤝 **社区支持**：Game Off 2026 社区与 Discord 可用于提问、分享进度、寻找队友；新手也能轻松上手，许多人正是在此完成人生第一款游戏。

---

### [](https://itch.io/jam/game-off-2026)

**原文标题**: [Game Off 2026 - itch.io](https://itch.io/jam/game-off-2026)

Game Off 2026 是由 GitHub 与 Lee Reilly 主办的年度游戏开发挑战，主题为“SHIFT”，鼓励个人或团队在 2026 年 11 月使用任意编程语言、游戏引擎或库制作游戏，并提交至 itch.io 参与互评。

- 🎮 **活动性质**：年度游戏开发挑战，个人或团队均可参加，创作方式与工具不限。
- 🗓️ **提交时间**：2026 年 11 月 1 日至 12 月 1 日；须在 12 月 1 日 13:37 PST 前推送游戏。
- 💡 **主题“SHIFT”**：可理解为换挡、视角转换、维度切换、位移、夜班、Shift 键，或按位偏移等。
- 🧩 **创意方向**：仅用 Shift 键操作、换挡改变物理规则、视角解谜、双现实切换、变形冒险、夜班恐怖、喜剧侦探、位运算解谜等。
- 🛠️ **参与步骤**：创建免费 GitHub 账号、加入 itch.io Game Off 页面、建立公开代码仓库、在 itch.io 提交游戏。
- 🗳️ **评审方式**：提交结束后参赛者互相投票，评选 Overall、Gameplay、Graphics、Audio、Innovation、Theme Interpretation。
- ⏳ **投票截止**：2027 年 1 月 1 日 13:37 PST。
- 🚀 **新手建议**：游戏开发挑战适合首次做游戏、尝试新引擎或学习新语言；可按语言选择 Phaser、Pygame、Godot、Unity、Unreal、Bevy、libGDX、Flame、Ebitengine、LÖVE、Defold、LIKO-12 等。
- 💬 **社区支持**：可在 Game Off 2026 社区提问或寻找队友，也有社区运营的 Discord 服务器。
- ✅ **实用提示**：先实现一个核心机制和一个可玩关卡，再扩展复杂内容；同时可借机学习 Git 与 GitHub。

---

