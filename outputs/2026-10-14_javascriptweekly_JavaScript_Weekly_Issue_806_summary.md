### [Deno 加入 Cloudflare | Deno](https://deno.com/blog/cloudflare)

**原文标题**: [Deno is joining Cloudflare | Deno](https://deno.com/blog/cloudflare)

Deno 团队将整体加入 Cloudflare，未来开发重心转向与 Workers、Durable Objects 结合的共享平台；同时公布 Deno runtime、Deno Deploy、JSR 等项目的过渡安排。

- 🚀 Ryan Dahl 于 2026 年 10 月 9 日宣布，整个 Deno 团队加入 Cloudflare，以进一步推进简化服务器软件开发的使命。
- 🧩 长期目标包括改进模块分发、JavaScript 运行时安全、完整工具链、独立可执行文件发布，并持续强化 Node.js 兼容性。
- ☁️ Deno Deploy 让应用运行更简单，但也暴露了底层复杂性，这推动了 celld 的出现。
- 🏗️ celld 基于 Cloudflare Workers 编程模型，让开发者从一开始就能构建分布式应用，并把扩展能力内置到编程模型中。
- 🤝 加入 Cloudflare 后，Deno 团队将与 Workers 和 Durable Objects 团队合作，目标是把该编程模型变成构建服务器的默认方式，无论运行在 Cloudflare 网络还是自有基础设施上。
- 🛑 未来开发将投入共享平台，不再继续开发独立的运行时和托管服务。
- ⏳ Deno runtime 将继续支持一年，期间每月发布错误修复和安全更新；一年后结束开发，但仍保持开源，欢迎他人继续开发。
- 📦 Deno Deploy 将继续运营六个月，之后关闭；付费客户迁移到 Cloudflare Workers 时将获得支持。
- 🌐 JSR 将继续运营，其基础设施将迁移到 Cloudflare。
- 🔧 团队将继续支持 rusty_v8，并推动其整合进 workerd。
- 🤖 AI 时代更需要更好的抽象；Durable Objects 适合 agent harness，具备低成本无服务器执行、持久状态、WebSockets 和高级 JavaScript 接口，celld 因此聚焦 Durable Objects。
- 📬 Kenton Varda 与 Ryan Dahl 在 Cloudflare 博客发布联合文章；若要在自有基础设施上大规模构建 agents，可联系 ry@cloudflare.com。

---

### [](https://dbushell.com/2026/10/03/deno-to-node/)

**原文标题**: [Friendship ended with Deno, now Node is my best friend â David Bushell â Web Dev (UK)](https://dbushell.com/2026/10/03/deno-to-node/)

作者长期使用 Deno 后重新转向 Node，因为 Node 已大幅现代化，而 Deno 因公司化、创新停滞和稳定性问题不再值得使用。

- 🔄 作者本月在 SvelteKit 客户项目中大量使用 Node，发现现代 ECMAScript 语法已受支持，旧 API 也被更新或替换，不必再见到 `require()`。
- 📦 包管理改用 FNM 管理 Node 版本，并用 PNPM 替代 NPM，还把 `npm`、`npx` 别名到 `pnpm`、`pnpx`。
- 🛡️ 在 `pnpm-workspace.yaml` 中配置 `minimumReleaseAge: 1440` 和 `trustPolicy: no-downgrade`，以延迟恶意包更新。
- 🧩 Node 能运行 TypeScript，但拒绝处理 `node_modules` 下的 TS 文件；作者认为这是哲学限制而非技术限制，并提到需用 Tsdown 打包发布。
- 🏠 因 GitHub 问题，作者自建 Forgejo；NPM 限制导致包失去 provenance，需配置 PNPM 信任策略允许自己的包。
- 🚀 将静态站点生成器从 Deno 迁移到 Node v26.10.0：替换文件系统 API 为 `node:fs`、`Deno.serve` 为 Hono Node 适配器、`@std/path` 为 `node:path`。
- ⚡ 迁移后构建速度提升约 15%，代码仍偏 Deno 风格，未来可探索更多 Node 内置 API。
- 📉 Deno 衰退：公司化后产品缺乏吸引力、裁员、创新停滞，还出现 JSR 限流、ZSH 集成故障、并发 HTTP 请求 bug 等问题。
- 🗑️ 作者最终卸载 Deno，并请求删除 JSR 账户，旧包版本仍可安装。
- ⚠️ 文中还提到 Oracle 商标纠纷不乐观，以及 2026-10-10 关于 Cloudflare 收购的更新。

---

### [celld：自托管、分布式的 Durable Objects](https://celld.dev/)

**原文标题**: [celld: self-hosted, distributed Durable Objects](https://celld.dev/)

celld（v0.6.2 beta）是一个自托管、分布式的 Durable Objects 运行时，让现有 Cloudflare 应用无需改动即可运行，状态存进你自己的 S3 存储桶，并在大规模下把成本降低几个数量级。

- 🚀 兼容 Cloudflare 应用：Workers、Durable Objects、Durable Object Facets、KV、Queues、D1、R2、Workflows、Cron、静态资源、动态 Workers 均受支持；Containers 仍为实验性
- 📦 部署极简：安装 58 MB 静态可执行文件（`curl -fsSL celld.dev/install.sh | sh`），或直接运行 Docker 容器 `ghcr.io/denoland/celld`
- 💾 数据自主：每个 cell 拥有独立 SQLite 数据库，节点共享一个 S3 兼容桶（也支持 Google Cloud Storage、Azure Blob Storage），无成员协议、故障检测或共识服务
- 🔒 持久性：RPO=0，已确认写入零丢失；节点被 SIGKILL 后约 20 秒完成故障转移且不丢数据
- ⚡ 性能：无状态请求 p50/p99 约 0.2/0.3 ms，单 worker 线程约 94k 请求/秒，唤醒休眠 cell 约 4 ms
- 🧮 密度与成本：每个常驻 cell 约 0.47 MB 内存，8 GB 节点可承载约 2,500 个 cell，约 $0.02/常驻 cell-月，闲置 cell 几乎无成本
- 💰 成本对比：100/1,000 个常驻 cell 时 celld 约 $49/月（Cloudflare DO 约 $415/$4,150），10 万个 cell 时 celld 约 $1,949/月（DO 约 $415,000）
- 🔧 架构：Workers 处理请求，KV、D1、队列、Workflow 也都是 cell；节点间路由请求并复制写入，条件桶写入决定 cell 所有权，一个 cell 同时只在一个实例上运行
- 🩺 自托管的价值：可自选节点位置与故障域，并通过所有权记录、SQLite/LTX 文件和日志（如 sqlite3、grep）排查故障——但仍需自担运维责任，不保证可靠性
- ⚠️ 边界与差异：不支持依赖 Cloudflare 网络、GPU 或浏览器农场的能力；`celld deploy` 读取现有 `wrangler.json`，遇到未知键会直接停止而非忽略
- ❤️ 定位：以 V8 + SQLite + LTX（Litestream 副本格式）构建的有状态分布式系统，是对 Kenton Varda 与 Cloudflare Workers 团队 Durable Objects 理念的致敬，Apache-2.0，由 Deno Land Inc. 出品

---

### [Deno 加入 Cloudflare | Cloudflare 博客](https://blog.cloudflare.com/deno-joins-cloudflare/)

**原文标题**: [Deno is joining Cloudflare | Cloudflare Blog](https://blog.cloudflare.com/deno-joins-cloudflare/)

Deno 团队正式加入 Cloudflare，双方将合并 workerd 与 celld 两大项目，目标是让开发者能在自有基础设施上以一等公民的方式自托管 Workers 与 Durable Objects，从而把 Workers 编程模型推广为构建服务器应用的主流方式。

- 🤝 **Deno 团队加入 Cloudflare**：Deno 团队（包括 Node.js 创造者 Ryan Dahl 与 Bert Belder）整体加入 Cloudflare，共同推进 Workers 生态。
- 🔗 **合并 workerd 与 celld**：将 Deno 的 celld 与 Cloudflare 的开源运行时 workerd 融合，形成统一的自托管方案。
- 🎯 **核心目标**：大幅简化 Workers 与 Durable Objects 的自托管，让开发者在更多地方使用相同的基础原语。
- 🧩 **Durable Objects 的价值**：它是"带 SQLite 数据库的分布式单例"，每个对象如同独立可寻址的小型服务器，单线程执行、支持 WebSocket、可同步访问本地数据库，天然实现分片与扩展。
- 🗄️ **celld 的设计理念**：一个用 Rust 编写的单二进制文件，唯一外部依赖是对象存储，避免多云、多数据库的复杂纠缠。
- 📜 **回溯历史**：Ryan Dahl 从 Node.js、Deno 一路探索更强大的抽象，认为网络应用的分布式计算、状态协调与自动扩缩容才是真正的难题。
- 🚫 **反驳"锁定"理论**：Cloudflare 强调 Workers 与众不同是因为它更好，而非故意制造迁移障碍；这种设计让全球数百个位置的部署既简单又便宜。
- 🔓 **开源才是好生意**：Workers 运行时 workerd 是开源的，且与生产环境代码一致；Shopify 等大客户正是因开源才选择合作，甚至有客户借此迁移离开。
- ⚠️ **workerd 的短板**：其 Durable Objects 仅支持单实例，无法扩展，这是长期存在的生产就绪性缺口，TODO 注释可追溯至最初版本。
- 🎉 **为何欢迎 celld**：celld 是与 Cloudflare 实现完全兼容、且专注自托管与可扩展性的 Workers/Durable Objects 实现，正是 Cloudflare 一直想造却没时间造的东西。
- 🛠️ **后续计划**：Ryan 与 Bert 将领导把 celld 的代码与理念合并回 workerd，使自托管成为受支持的一等构建方式，未来数月将有更多公告。
- 🚀 **马上可试**：迫不及待的开发者今天就可以开始自托管 celld 或 workerd。

---

### [](https://jsr.io/)

**原文标题**: [JSR: the JavaScript Registry](https://jsr.io/)

JSR 是面向现代 JavaScript 和 TypeScript 的开源包注册表，支持浏览、搜索和发布包，并强调 TypeScript/ESM、npm 兼容及多运行时支持。  
- 📚 提供 Docs、Why JSR?、Discord、包搜索、发布包和浏览包等入口。  
- ⭐ 首页展示 Featured 包，如 @kysely/kysely、@es-toolkit/es-toolkit、@zod/zod、@punkpeye/fastmcp、@rabbit-company/web、@campfire/core、@am/neuralnetwork、@sigmasd/jsr-mcp、@iuioiua/redis、@img/png。  
- 🔄 Recently updated 包含 @sholvoir/generic 0.4.9、@swanfactory/hcweb 0.20.1、@fathym/ioc 多个版本、@o-industrial/common 0.1.1544-round-10 等更新包。  
- 🆕 New to JSR 包含 @spy4x/tasks、@lavender/lockbox、@adanos/finance-sentiment、@primp/vue、@gunsnprices/gunsnprices、@dynamicsninja/garminconnect 等新包。  
- 🧩 Why JSR? 为 TypeScript 与 ESM 设计：发布 TS 源码，自动生成 API 文档、.d.ts 文件并转译，保证跨运行时兼容。  
- 📦 基于 npm：JSR 不是 npm 替代品，而是其超集；模块可用于任何 JS 包管理器和含 node_modules 的项目。  
- 🌐 支持任意运行时：Node.js、Deno、Bun、Cloudflare Workers 等，并提供强类型编辑体验。  
- 📅 页面页脚显示时间 2026/10/14, 1:00:21 UTC，以及 Docs、GitHub、Discord、Bluesky、X、YouTube 链接。

---

### [](https://github.com/Agent-Field/CodeAF)

**原文标题**: [GitHub - Agent-Field/CodeAF: Open-Source Software factory for Open Models · GitHub](https://github.com/Agent-Field/CodeAF)

CodeAF 是 AgentField AI 推出的开源“软件工厂”式编码工具，专为开放模型优化，主打低成本前沿级编码体验。它以单个 Go 二进制运行，把多项目、多任务、多模型协作整合进一个窗口，并支持子 harness、自动模型编队、无头模式和远程开发。目前它在 DeepSWE 基准上表现第一，且资源占用远低于同类工具，但仍处于早期预览阶段。

- 🏆 在 DeepSWE 上，同一模型下十款编码 harness 中排名第一，超过 Claude Code、Codex、OpenCode、Kilo 和 DeepSeek 官方 harness，且每个已解决问题成本最低。
- 🧰 面向开放模型打造的编码 harness，用 Go 编写为单个小二进制，除自身外无需安装其他东西，Apache 2.0 许可证，由 AgentField AI 出品。
- 📦 安装方式为 `curl -fsSL https://agentfield.ai/get/codeaf | bash`，然后运行 `codeaf`；也可固定版本或从源码构建，首次启动可连接 OpenRouter、Codex ChatGPT 计划，或接入 DeepSeek、GLM、Kimi、MiniMax、Qwen、Ollama 等。
- 🪟 一个窗口管理所有项目：`home` 列出机器上所有项目和对话，`enter` 打开标签页，`tab` 切换，`alt+k` 跳转；每个项目有独立审批规则、模型和支出限额。
- 🗣️ 对话即任务：一句话可拆成多个任务，每个任务在仓库副本和独立分支运行；通过检查的工作自动落到你的分支，绝不直接进入 main、dev 或 release 分支。
- 🏭 “工厂”模式：它负责拆分、调度、并行执行、测试和合并工作，只在必要时询问；问题集中在 `needs you`，其余自动决策并记录。
- 🧩 子 harness 是专才代理：针对 PR 审查、修复 issue、依赖审计等固定工作，有专属计划、检查与模型，输入输出均为类型化；即将原生支持 PR-AF，目前有 `/senior-dev`。
- 🧠 多模型编队：一次会话多个模型；seat 与你对话，worker 干活，planner 规划，checker 验收；默认自动按任务类型、历史表现和目录元数据评分选模型，方法为 Pareto Crewing。
- 💸 成本控制：`/crew` 查看座位、模型、供应商、每任务默认 5 美元限额和每日上限；`/crew pin checker <model>` 固定模型，`/task --best` 或 `--cheap` 调节，`/redo stronger` 重跑。
- 🌐 模型池默认开启，仅发送无文本的汇总数字，如角色、模型、评分等，不发送代码、提示、路径或身份；可关闭，也支持只读模式或完全关闭。
- 📌 长期指令：规则、提醒和监控统一设置，比如“不要直接提交 main”“每周一草拟更新”“CI 变红时通知我”，可作用于当前项目或全局，并受每日支出限制。
- 🖥️ 无头模式：同一工厂去掉对话，用于 CI、cron、脚本和基准测试；`codeaf do "..." --timeout 30m --json` 输出一个 JSON 和退出码，计划、运行、检查一次完成，遇到疑问记录假设。
- 🔐 远程开发：屏幕在本地，对话在拥有工作的机器上；`codeaf chat --host devbox` 使用 SSH 配置，输入不等待网络，关盖后工作继续，文件和截图可双向传递，手机终端也可接入同一对话。
- ⚡ 性能：单个 Go 二进制 53 MB，比竞争对手小至多 21 倍；每新增会话 RAM 27 MB，16 个空闲会话 507 MB，单轮峰值 122 MB，恢复 50 轮会话 145 ms。
- 📚 文档与遥测：内置手册，`alt+.` 查看键位，Guide 涵盖标志、键、斜杠命令和退出码，docs/ 有架构、无头、远程、限制；默认发送匿名使用计数，不发送代码、提示、路径等，可通过 `/settings`、`CODEAF_TELEMETRY=off` 或 `DO_NOT_TRACK=1` 关闭。
- 📈 仓库信息：417 stars、53 forks、260 issues、17 PR、3,178 commits，主要语言 Go，Apache-2.0，Topics 包括 agent-harness、agentic-coding、coding-agent、open-models、software-factory 等。

---

### [Bun v1.4.3 | Bun 博客](https://bun.com/blog/bun-v1.4.3)

**原文标题**: [Bun v1.4.3 | Bun Blog](https://bun.com/blog/bun-v1.4.3)

Bun v1.4.3 于 2026 年 10 月 10 日发布，核心亮点是内置极速 TypeScript 类型检查器 `bun check`，同时在运行时、网络、构建、安装、编译、安全与 Node.js 兼容性方面带来大量改进和修复。

- 🚀 安装支持 curl、npm、PowerShell、Scoop、Homebrew、Docker；升级使用 `bun upgrade`。
- 🧠 新增 `bun check`：内置超快 TypeScript 类型检查器，基于 typescript-go 移植，读取 `tsconfig.json`，无需安装 `typescript` 包。
- ⚡ 性能：比 `tsc` 7.0.2 快 3x–6.4x，内存少 2.2x–4.9x；通过 TypeScript 7.0.2 全部 51,210 项一致性测试。
- ✅ 在 72 个故意误配的开源项目中对比 `tsc`，1,103 个配置中 1,102 个完全一致，仅 vuejs/core 有 1 个不匹配。
- 🧪 每提交运行模糊测试与变异测试，包括 136,235 个模糊函数和 Effect 源码 913 次变异，均无差异。
- 🔁 集成方式：`bun run --check` 先类型检查再运行，`bun test --check` 检查测试文件，`bun build --check` 检查后再打包。
- 🌐 新 `Bun.FetchSession`：为请求组提供独立 TLS、代理、keep-alive 和连接池。
- 🔐 `fetch()` 代理增强：支持 `NO_PROXY` 通配符/CIDR/IPv6/host:port、`ALL_PROXY`、`proxy: false` 和 `ERR_PROXY_TUNNEL`。
- 🧩 实验性 `Bun.ModuleGraph`：单进程运行多个应用实例，模块状态、`require.cache`、定时器和 I/O 隔离。
- 🚫 `--disallow-code-generation-from-strings` 现在真正阻止 `eval()`、`new Function()`、vm、`data:` import、Worker eval 等。
- 📈 `node:http` 大响应最高快 2.7x；大于 16KB 响应每 tick 一次写出，`Bun.serve` 直接流 4×16KB 快 83%。
- 🧬 JavaScriptCore 升级：`JSON.parse`、正则、`Object.values`、数组操作等多项提速，并修复 Wasm/Intl/RegExp 等行为。
- ⏱ 大量拒绝 Promise 处理更快：10 万条 `Promise.allSettled` 从 24s 降至 148ms，16 万已拒绝 Promise 从 83s 降至 24ms。
- 🗜 `CompressionStream` 支持 level：gzip/deflate 0-9、brotli 0-11、zstd 1-22，越界抛 `RangeError`。
- 📦 `Bun.serve` 支持 `If-Range`，可安全续传下载；文件未变返回 206，否则返回 200 完整响应。
- 📉 `bun install` 无锁文件时跳过不会安装的 tarball，冷缓存安装大幅减少下载。
- 🏗 `bun build` 多入口/分包内存大幅降低：800 入口从 2121MB 降至 276MB。
- 🔗 `Bun.build` 输出名支持 `[hashN]`，`[hash13]` 为完整 64 位哈希；metafile 标识 split import 的 `entryPoint`。
- 🧊 `bun build --compile` 支持 `--bytecode-order` 按真实运行 profile 布局字节码，冷启动 1.01s→0.53s，常驻内存 59.5MB→20.5MB。
- ⚡ `--compile --bytecode` 启动更快：约 2300 模块 CLI 首屏 698ms→579ms；新增 `--compile-jit-policy`。
- 🛠 其他修复：`crypto.randomInt`、zstd/zlib、`Bun.color`、`transpiler.transformSync`、vm、HTTP/1.1 流水线、内存归还等。
- 🔒 安全加固：TLS 握手期间验证、证书名匹配、CVE-2026-48618、HTTP/2 流重置限速、`Bun.SQL`、`fetch`、`bun install` 等。
- 🟢 Node.js 兼容性：大量 `node:http`、`node:http2`、`node:tls`、`node:net`、`node:child_process`、`node:vm`、`node:fs`、`node:crypto` 等修复。
- 🧰 其他模块修复：`Bun.serve`、`Bun.spawn`、`HTMLRewriter`、`Bun.Image`、`Bun.markdown`、YAML、`Bun.Glob`、`bun:ffi` 等。
- 📦 工具链修复：`bun install`、`bun build`、minifier、CSS parser、`bun test`、Bun Shell、SQL/SQLite/S3、TypeScript 类型、Windows 均有多项修复。

---

### [Bun v1.4.3 | Bun 博客](https://bun.com/blog/bun-v1.4.3#javascriptcore-upgrade)

**原文标题**: [Bun v1.4.3 | Bun Blog](https://bun.com/blog/bun-v1.4.3#javascriptcore-upgrade)

Bun v1.4.3 于 2026 年 10 月 10 日发布，核心亮点是内置 TypeScript 类型检查器 `bun check`，并带来运行时、构建、安装、安全与 Node.js 兼容性的大量性能提升和修复。  
- 🚀 发布版本为 Bun v1.4.3，支持 `curl`、`npm`、PowerShell、Scoop、Homebrew、Docker 安装，并可用 `bun upgrade` 升级。  
- 🧠 新增内置 TypeScript 类型检查器 `bun check`，兼容 `tsc` 错误输出，读取 `tsconfig.json`，并利用全部 CPU 核心。  
- ⚡ `bun check` 比 `tsc 7.0.2` 快 3 到 6.4 倍，内存占用少 2.2 到 4.9 倍，无需安装 `typescript` 包。  
- ✅ `bun check` 通过 TypeScript 7.0.2 完整合规测试套件，共 51,210 项测试全部通过。  
- 🔍 在 72 个故意误配置的开源项目中，`bun check` 与 `tsc` 对比 286,267 个错误，仅 1 个不匹配。  
- 🧪 支持 `bun run --check`、`bun test --check`、`bun build --check`，类型错误会阻止运行、测试或构建。  
- 😴 服务器空闲时 CPU 占用降低 67% 到 89%。  
- 🔐 新增 `Bun.FetchSession`，为每组请求提供独立 TLS、代理、keep-alive 和连接池。  
- 🌐 `fetch()` 更好支持 `NO_PROXY`、`ALL_PROXY`、CIDR、通配符、IPv6，并支持 `proxy: false`。  
- 🧩 实验性新增 `Bun.ModuleGraph`，可在单进程运行同一应用的多个隔离模块图实例。  
- 🛑 `--disallow-code-generation-from-strings` 可阻止 `eval()`、`new Function()` 及其他字符串转代码方式。  
- 🌐 `node:http` 和 `Bun.serve` 的大响应最高快 2.7 倍，超过 16 KB 的响应每个 tick 一次写出。  
- 🧬 JavaScriptCore 升级带来 `JSON.parse`、正则、数组、`for...of`、解构等多项性能提升与规范修复。  
- 💧 大量 rejected promise 处理优化：`Promise.allSettled` 处理 10 万个抛出异常的异步调用从 24 秒降到 148 毫秒。  
- 🗜️ `CompressionStream` 支持压缩级别，gzip/deflate 为 0-9，brotli 为 0-11，zstd 为 1-22。  
- 📥 `Bun.serve` 支持 `If-Range`，客户端可安全续传未变化的文件。  
- 📦 `bun install` 无锁文件时会跳过不会进入 `node_modules` 的 tarball，减少冷缓存下载。  
- 🏗️ `bun build` 多入口点内存占用大幅降低，支持 `[hashN]` 输出名，并改进 metafile 的 `entryPoint` 信息。  
- 🧊 `bun build --compile` 支持 `--bytecode-order` 按真实运行 profile 布局字节码，某大型 CLI 冷启动从 1.01 秒降到 0.53 秒。  
- 🐛 修复多项性能回归：`crypto.randomInt()`、zstd、`node:zlib`、`Bun.color()`、`vm`、`Bun.serve` 流水线请求等。  
- 🔒 安全加固覆盖 TLS 握手验证、证书名称匹配、`Bun.SQL`、`node:http2` 流重置限流、`fetch()`、`bun install` 等。  
- 🧷 大量 Node.js 兼容性修复，涉及 `node:http`、`node:http2`、`node:tls`、`node:net`、`node:dns`、`node:child_process`、`node:vm`、`node:fs`、`node:crypto` 等。  
- 🧪 `bun test`、Bun Shell、SQL/SQLite/S3、YAML、Markdown、HTMLRewriter、Bun Image 等也有多项修复。  
- 🪟 Windows、TypeScript 类型、打包器、压缩器、CSS 解析器、转译器均有修复与改进。  
- 🧭 官方建议用 `bunx -p typescript@7.0.2 tsc --noEmit --pretty false > tsc.txt` 和 `bun check --no-pretty > bun.txt` 对比，若结果不同可提交 issue。

---

### [](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere/)

**原文标题**: [Announcing AWS Lambda Web Functions | AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere/)

AWS Lambda Web Functions 正式发布，允许开发者直接运行标准 HTTP Web 应用而无需改写成事件处理器，与 Event Functions、MicroVMs 共同构成三种计算形态。

- 🚀 **新形态发布**：AWS Lambda Web Functions 于 2026 年 10 月 12 日推出，支持直接部署标准端口监听的 HTTP 服务器
- 🌐 **框架无锁定**：兼容 Express、Hono、Fastify、Next.js 等任意 Node.js 框架，无需适配器或改写代码
- ⚡ **一条命令部署**：使用 `aws lambda-web deploy` 即可完成打包、创建、发布 revision 并返回 HTTPS URL，全程不到一分钟
- 📊 **三种形态互补**：Event Functions 适合事件处理与队列消费；Web Functions 适合 Web 应用与 API 后端；MicroVMs 适合运行不可信的有状态代码
- 🔄 **多并发执行**：每个执行环境最多同时处理 128 个并发请求，突发流量可共享热环境而非为每个请求新建环境
- 💰 **活跃 CPU 计费**：仅计量代码实际消耗的 CPU 时间，I/O 等待几乎不消耗 CPU，内存按环境存活时间计费，适合 SSR、API 后端、AI 推理流式响应等场景
- 🌍 **多区域自动分发**：通过 `--regions` 参数自动复制代码并配置延迟路由，单一全球 URL 将请求导向延迟最低的区域
- 🐤 **金丝雀发布**：可通过 API 在 revision 之间按权重分配流量（如 90/10），无需额外工具
- ☁️ **与 CloudFront 集成**：可将 Web Function 端点设为 CloudFront 源，支持 OAC 私有源模式，静态资源走缓存、动态请求走 Web Function
- 📍 **可用区域**：美东（弗吉尼亚北部）、美东（俄亥俄）、美西（俄勒冈）、亚太（东京）、欧洲（爱尔兰）
- 🖥️ **运行环境**：启动时支持 Node.js 24（nodejs24.x）on Arm64，并支持 VPC 连接
- 🎯 **快速上手**：`aws lambda-web deploy --name hello-world --hello-world`

---

### [Stack Overflow 2026 年开发者调查](https://survey.stackoverflow.co/2026)

**原文标题**: [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026)

概述总结  
Stack Overflow 第16届年度开发者调查覆盖169个国家、30,903名技术人，围绕工作、AI、技术、社区与知识五大类别，主题聚焦“你最近好吗？”。结果显示工作满意度下降，AI使用与信任快速上升，Python在AI相关开发中领先，开发者在获取可信答案与工作上下文方面仍面临挑战。

- 🌍 调查规模：103个问题、5大类别、30,903份回应、覆盖169个国家，评估467项技术。
- 😟 工作满意度：33%对工作不开心，45%“得过且过”，仅22%开心；创新与不确定性影响职场感受。
- 🧑‍💻 自由职业上升：自由职业/自雇比例从3.9%升至10.5%，AI代理让个人更像“代理管理者”。
- 🤖 AI使用普及：80%受访者每天至少使用AI一小时；62%对工作中使用AI持正面态度。
- 🔐 AI信任提升但有条件：87%对AI输出有某种信任，远高于去年的31%；但48%只在可验证时信任。
- 📚 来源引用很重要：93%受访者认为AI回答引用来源重要，说明AI输出仍难被完全直接采信。
- 🐍 AI开发语言：AI相关开发中Python使用率最高，达39%；其后是JavaScript、HTML/CSS、SQL等。
- 🧓 资深开发者偏好：16年以上经验者常用SQL（63%）、JavaScript（62%）、HTML/CSS（56%）。
- 🛠️ 自建 vs 购买：19%受访者自建工具替代供应商，其中过半使用AI工具辅助。
- 🔎 社区找答案：82.7%用在线搜索，69.9%问AI代理，43.7%搜索已知仓库，28.8%直接问信任的人。
- 💬 工作问题来源：同事/队友（72%）、代码与注释（63%）、内部文档/维基（60%）最常用。
- 📉 Stack Overflow使用变化：64%因AI减少访问简单问题，29%总体提问减少，27%贡献减少。
- 🧩 上下文障碍：63%遇信息不完整，61%关键上下文在人脑中，56%信息过时，53%分散在太多工具。
- ⏳ 上下文发现滞后：约79%常在上手或完成任务后才发现重要上下文；75%花5小时以上搜索答案。
- 📌 AI采纳关键：31%看重准确有用结果，29%看重安全隐私，27%看重价格与价值匹配。
- 🎯 AI代理所需上下文：项目目标/需求（85%）和代码、仓库、技术文档（73%）最重要。

---

### [获取失败](https://news.ycombinator.com/item?id=50052814)

**原文标题**: [Failed to retrieve](https://news.ycombinator.com/item?id=50052814)

无法总结：获取内容失败，状态码 419。

---

### [发布 v4.6.6 · colinhacks/zod · GitHub](https://github.com/colinhacks/zod/releases/tag/v4.6.6)

**原文标题**: [Release v4.6.6 · colinhacks/zod · GitHub](https://github.com/colinhacks/zod/releases/tag/v4.6.6)

Zod 发布 v4.6.6，重点说明 9 月 21 日六个恶意提交虽被推送到 main，但同日已回滚并从历史中移除，且从未发布到 npm；该版本还包含类型、解析边界、文档与发布流程相关改动。

- 🏷️ v4.6.6 由 github-actions 于 10 月 11 日 16:19 发布，对应提交 9c21983。
- ⚠️ 9 月 21 日有六个恶意提交使用泄露的 git 凭据被推送到 main。
- ↩️ 这些提交同日通过 #6620 回滚，并已从 main 历史中移除。
- 📦 恶意提交从未发布到 npm；v4.6.6 的 npm provenance 指向 284243f，即 9c21983 的重写前副本，内容相同。
- 🧩 类型修复：将 record 的输出和输入声明为成员，而非基类型参数（#6645）。
- 🛡️ v4 修复：在解析元素前检查 array、set 和 map 的大小边界（#6652）。
- 📚 文档更新：Zod Mini 直接加载 en locale、从 zod/locales 导入、收紧 z.locales tree-shaking 说明，并调整 Code for Japan 铜牌赞助商 logo。
- 🚀 发布流程：改为暂存 npm 版本而非直接发布（#6622），并在暂存版本获批前暂停 release-approval 环境运行（#6638）。
- 📊 仓库与互动：70 个 issue、18 个 PR，仅协作者可创建 PR；发布页有 2 个资源，获得 3 👍、3 🚀、5 👀，共 9 人回应。

---

### [获取失败](https://news.ycombinator.com/item?id=50057591)

**原文标题**: [Failed to retrieve](https://news.ycombinator.com/item?id=50057591)

无法总结：获取内容失败，状态码 419。

---

### [即将发布的 Next.js 上游漏洞安全更新 | Next.js](https://nextjs.org/blog/upcoming-nextjs-security-update-october-2026)

**原文标题**: [Upcoming Next.js Security Update for Upstream Vulnerabilities | Next.js](https://nextjs.org/blog/upcoming-nextjs-security-update-october-2026)

Next.js 计划于 2026 年 10 月 14 日（下周三）发布带外安全更新，修复三个上游依赖漏洞（两个严重、一个高危）；其中两项修复因上游协调而从 9 月安全版本推迟。官方将随更新发布完整公告，并建议尽快升级到已修补版本。

- 🗓️ 发布时间：2026 年 10 月 14 日（下周三），将发布 Next.js 带外安全更新。
- 🛡️ 漏洞概况：共涉及 3 个上游依赖漏洞，其中 2 个为 Critical，1 个为 High。
- ⏳ 延期说明：其中 2 项修复因上游协调，从 9 月安全版本推迟。
- 📄 公告内容：完整安全公告将随更新发布，包含影响范围、受影响版本和升级说明。
- ⬆️ 行动建议：更新可用后，尽快升级到已修补版本。
- 🤝 安全合作：通过 Vercel 开源漏洞赏金与研究人员合作；疑问可联系 security@vercel.com。

---

### [](https://tanstack.com/blog/tanstack-start-1-0)

**原文标题**: [TanStack Start 1.0 is Stable | TanStack Blog](https://tanstack.com/blog/tanstack-start-1-0)

TanStack Start 1.0 已正式稳定并可用于生产；作者 Tanner Linsley 回顾了从 Router 到全栈框架的多年历程，重点包括类型安全、灵活选择代码运行位置、RSC 取舍、AI 代理影响，以及社区与合作伙伴的支持。

- 🚀 2026年10月13日，TanStack Start 1.0 发布稳定版，正式承诺生产可用。
- 🏗️ Start 起源于 Router，核心目标是通过 TypeScript 实现路由、参数、loader、context 的端到端类型安全。
- 🧩 希望提供不同于 Next.js/RSC 的选项：保留 SPA 开发体验，同时支持 SSR、流式、服务器函数和全栈中间件。
- 🌐 createIsomorphicFn 允许同一调用在服务端和客户端有不同实现，并自动移除另一环境代码。
- 👥 Manuel Schiller、Florian Pellet、Christopher Horobin 等贡献者大幅推进类型安全性能、SSR 性能（约 5.5 倍吞吐）和框架质量。
- 🧱 框架无关与部署自由：支持 Vite、Nitro、Rsbuild、Solid，避免维护大量部署适配器。
- ⚛️ 曾投入大量精力支持 RSC，但最终因复杂性和收益权衡在 tanstack.com 移除，强调可选择性集成而非核心依赖。
- 🤖 2025-2026 年 AI 代理显著改变开发流程，带来安全扫描、PR 激增，也促使 TanStack Intent/skills 帮助代理正确使用 API。
- 🔐 安全成为开源维护常态，团队与合作伙伴用 AI 主动发现和修复漏洞。
- 🤝 众多合作伙伴支持：Netlify、Lovable、Vercel、Render、Cloudflare、Railway、WorkOS、Clerk、Prisma、Sentry 等。
- 📚 鼓励试用 1.0，查看文档和迁移指南，并可让 AI 代理协助新建或迁移项目。
- 🙏 公开感谢维护者、贡献者、合作伙伴和社区，称 Start 已比个人最初设想更强大。

---

### [引言](https://partytown.qwik.dev/)

**原文标题**: [Introduction](https://partytown.qwik.dev/)

Partytown 是由 QwikDev 维护的懒加载库，旨在将资源密集型第三方脚本移入 Web Worker，释放主线程并专注于核心应用代码，从而提升网站性能。它不保证适用于所有场景，使用前需参考 FAQ 与 Trade-Offs。

- 🎯 核心目标：释放主线程资源，仅用于主 Web 应用执行，并隔离第三方脚本。
- 🧵 将分析、指标、广告、A/B 测试、追踪器等第三方脚本从主线程迁移到 Web Worker。
- ⚙️ 支持在 Web Worker 中同步读写主线程 DOM 操作，让脚本尽量按原始方式运行。
- 🧪 可沙箱化第三方脚本，允许或拒绝其访问主线程 API，并隔离长时间运行任务。
- 🚦 通过批量 DOM 读写、节流主线程访问，减少第三方脚本造成的布局抖动。
- ⚠️ 第三方脚本常见负面影响：请求过多、JS 过大阻塞 DOM、CPU 解析执行延迟交互、单点故障、缓存不足、legacy API、过多 DOM/CSS、重复加载框架等。
- 🚫 第三方脚本还常阻塞 `window.onload`，即使使用 `async` 或 `defer`。
- ✅ 最适合非关键渲染路径的代码；大多数第三方脚本符合该场景，异步特性也适合。
- 📊 典型用例：Google Tag Manager、Google Analytics、Facebook Pixel、Mixpanel、Hubspot、Segment、Amplitude 等。
- 🔌 提供多种框架与平台集成：Angular、Astro、Next.js、Nuxt、React、Remix、SvelteKit、WordPress、Shopify 等。
- 🛠️ 配置包括代理请求、转发事件、沙箱、调试、第三方服务与常见服务。
- 👥 社区渠道包括 Discord、@QwikDev，并提供多篇相关文章与测试页面。
- 📚 注意：Partytown 并非在所有场景都可用，使用前应查看 FAQ 和 Trade-Offs。

---

### [介绍 Marionette 5 — Marionette](https://marionettejs.com/news/introducing-marionette-5/)

**原文标题**: [Introducing Marionette 5 — Marionette](https://marionettejs.com/news/introducing-marionette-5/)

Marionette 5.0.0 正式发布，带来独立核心、灵活集成以及辅助 AI 助手使用的工具。维护者 Paul Falgout 与 OpenAI 助手 dot 展开对话，分享他为何重返 v5 以及实际尝试的结果。

- 🚀 Marionette 5.0.0 发布：核心不再依赖 Backbone、jQuery 或 Underscore，同时保留 Views、Regions、CollectionViews 和 Applications 的清晰结构
- 🤖 回归动因：随着 AI 助手承担越来越多编码工作，Paul 重新思考是否值得继续投入 Marionette，而非迁移到主流框架
- 💡 架构优先：他向多个 AI 询问“若 JavaScript 存在但尚无框架，助手会想要怎样的生态”，答案聚焦 Regions、可预测生命周期、明确所有权与状态分离
- 🧠 多方验证：Claude Opus 4.7 与 Gemini 3.5 均认可该架构价值，虽在消息总线和响应式等细节上有分歧
- 🔧 灵活集成：通过适配器可选保留 Backbone，支持 Lit 模板与可观察数据等渲染和数据方案
- 📚 助手工具：提供版本匹配文档、Marionette 技能、TypeScript 声明及 ESLint 规则，帮助助手定位已安装 API
- ⚡ 实测表现：RealWorld 基准中文章导航中位数 175ms，Vue 为 425ms；Vikunja 迁移中富任务打开中位数 1.04 秒，Vue 为 3.72 秒，缩短 72%
- 🧭 平滑迁移：迁移指南允许现有应用通过适配器保留 Backbone Models、Collections 与持久化，逐步更新至 v5 契约
- 🛠️ 上手建议：可在小型功能上试用 v5，新项目使用快速开始，现有项目参考迁移指南

---

### [Bootstrap 6 Alpha | Bootstrap 博客](https://blog.getbootstrap.com/2026/10/08/bootstrap-6-alpha/)

**原文标题**: [Bootstrap 6 Alpha | Bootstrap Blog](https://blog.getbootstrap.com/2026/10/08/bootstrap-6-alpha/)

Bootstrap 6 Alpha 1 于 2026 年 10 月 8 日发布，是 Bootstrap 的一次重大现代化重构，围绕 Sass 模块系统、CSS 变量与 token maps、ESM-only JavaScript、现代浏览器特性和新工具链全面升级。它继续定位为面向人类与 AI 的开源设计系统，后续将分批介绍颜色主题、组件、网格、表单、前缀与工具类、JS 插件等变化。

- 🚀 Bootstrap 6 首个 Alpha 版本发布，目标是让更多人、人类或 AI，更快更轻松地构建软件。
- 🧱 Sass 全面转向 `@use` / `@forward` 模块系统，视觉定制改为 CSS 变量与 token maps，可通过 `$root-tokens` 和组件 token 映射覆盖，并支持运行时修改。
- 🎨 新体系以 CSS 为优先：Sass 负责程序化生成变体、工具类和函数，CSS 负责视觉定制，几乎所有 v5 Sass 变量都变为 CSS 变量。
- 🌐 浏览器基线大幅提高：要求 Chrome/Edge 130+、Firefox 132+、Safari 18+，使用 `light-dark()`、`:has()`、容器查询、`oklch()`、`color-mix()`、原生 `<dialog>` 等新特性，不再为旧浏览器提供回退、前缀或 polyfill。
- 📦 安装方式：`npm i bootstrap@6.0.0-alpha.1` 或使用 CDN；JavaScript 仅支持 ESM，`<script>` 需添加 `type="module"`。
- 🏷️ 响应式与状态修饰改为前缀写法：如 `.d-md-none` → `.md:d-none`，`.col-lg-6` → `.lg:col-6`，`.opacity-50-hover` → `.hover:opacity-50`，`.offcanvas-md` → `.md:drawer`。
- 🧩 CSS 现代化亮点包括：CSS layers、`oklch()` / `color-mix()`、`light-dark()`、范围媒体查询、容器查询、原生 `<details>` / `<summary>` 手风琴、原生 `<dialog>`、`:where()`、`@property`、`content-visibility` 等。
- ⚙️ JS 与工具链更新：插件 ESM-only，无 UMD 和 `window.bootstrap`；源码改为 TypeScript 并自带类型；Rolldown 替代 Rollup/Babel，Vitest + Playwright 替代 Karma，文档使用 Astro 7。
- 🤖 面向人类与 AI 的配套：提供 `llms.txt`、`llms-full.txt` 文本文档，并在 `skills/` 目录加入代理技能文件，用于迁移、构建工具、组件编写等任务。
- ♻️ Bootstrap 5 仍可用并受支持，将尽快发布 v5.4.0，之后再公布 Bootstrap 5 的终止支持日期。
- 🧑🤝🧑 社区感谢：特别感谢共同维护者 Julien，以及所有贡献者、Open Collective 支持者、提交 issue 和 PR 的参与者。
- 📝 后续反馈：目前仍是 Alpha，Beta 前仍可能明显变化；可通过 GitHub Discussions、Issues 或 Pull Request 提供反馈。
- 🖥️ 其他更新：博客与 Icons 网站改版，新增搜索、分类页和布局；并推出私有 `@twbs/bui` 包用于共享 Bootstrap 文档组件。

---

### [发布 v5.3.0 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v5.3.0)

**原文标题**: [Release v5.3.0 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v5.3.0)

Express v5.3.0 已发布，由 UlisesGascon 于 10 月 9 日发布，包含 2 个提交。本次更新重点包括 HTTP 头冲突修复、安全依赖升级、QUERY 条件请求支持、多个核心依赖升级与性能优化，以及大量文档、CI 和依赖维护更新。

- 🚀 v5.3.0 为最新版本，完整变更范围是 v5.2.1...v5.3.0。
- 🐞 修复 `res.send()` 中 `Content-Length` 与 `Transfer-Encoding` 的 HTTP 头冲突：仅在没有 `Transfer-Encoding` 时添加 `Content-Length`，且 ETag 生成不受影响。
- 🔐 升级 `qs` 至 `^6.16.0`，修复数组长度限制绕过、攻击者控制 `isBuffer` 导致拒绝服务等多个 CVE。
- 🛡️ 升级 `proxy-addr` 至 `^2.0.8`，修复 CVE-2026-90711。
- ✅ `req.fresh` 现在支持 QUERY 请求的条件重新验证，匹配验证器时可返回 304 Not Modified。
- 🌐 `res.redirect()` 的 HTML 响应新增 `<!DOCTYPE html>`、`<title>` 和 `<body>`，提升浏览器兼容性。
- 🧩 `app.render` 在 options 为 `null` 时也能正确处理，行为与省略 options 或传空对象一致。
- 📦 升级 `content-type` 至 `^2.0.0`、`type-is` 至 `^2.1.0`，Content-Type 解析约快 1.5 倍；`res.send()` 保留已有参数，且解析失败不再抛错。
- 🪵 默认错误处理器现在记录完整错误对象，保留 `Error.cause` 和库特定属性，例如 Sequelize 的 `parent`/`original`。
- 📎 升级 `content-disposition` 至 `^2.0.1`，`res.download()`、`res.attachment()`、`res.sendFile()` 对有效 HTTP token 文件名不再加引号。
- 🛡️ 升级 `body-parser` 至 `^2.3.0`，修复 CVE-2026-12590；无效 `limit` 会在解析器初始化时抛错，避免请求体大小限制被静默禁用。
- ⚡ 性能优化：`res.send()` 发送未显式设置 Content-Type 的字符串响应时，避免重复处理 Content-Type。
- 🧹 维护更新：包含大量文档、CI、依赖升级与测试改进；完整变更和新贡献者列表见发布说明。
- 👥 贡献者：Cherry、blakeembrey 等 38+ 位贡献者参与，并有大量新贡献者首次提交。

---

### [获取失败](https://lemire.me/blog/2026/10/10/websocket-servers-in-javascript-node-js-bun-and-deno-in-2026/)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/10/10/websocket-servers-in-javascript-node-js-bun-and-deno-in-2026/)

无法总结：获取内容失败，状态码 202。

---

### [获取失败](https://lemire.me/blog/2023/11/25/a-simple-websocket-benchmark-in-javascript-node-js-versus-bun/)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2023/11/25/a-simple-websocket-benchmark-in-javascript-node-js-versus-bun/)

无法总结：获取内容失败，状态码 202。

---

### [](https://sindresorhus.com/blog/swift-website)

**原文标题**: [This Website Is Now Made in Swift — Sindre Sorhus](https://sindresorhus.com/blog/swift-website)

该网站已从 Astro 完全迁移到 Swift：所有页面、组件和样式统一用 Swift 编写，开发体验类似 SwiftUI；编译器在构建期检查链接、样式、脚本和内容数据，最终浏览器仍收到纯 HTML、CSS 和少量 JavaScript，因此体积小、速度快且维护更安心。

- 🧑💻 网站现在完全由 Swift 构建，不再需要从应用开发切换到另一套网站语言和工具。
- ⚙️ 选择 Swift 的关键是编译器：链接、类名、样式、脚本和 60 多个应用的数据大多在编译期校验，重命名页面会让旧链接无法编译。
- 🧩 组件写法类似 SwiftUI：组件是带 `body` 的 struct，HTML 来自 Elementary，路由、样式和内容由自研小框架处理。
- 🎨 样式即修饰符：`.style { … }` 会生成类似 `back-link-1x2y3z4` 的类名，包含文件名和样式哈希，避免样式泄漏。
- 🧬 共享样式和变体用 enum case 表示，可自动补全，拼写错误无法通过编译；每个页面只加载自身组件所需的 CSS。
- 🛡️ 使用现代 CSS，包括级联层、`light-dark()`、相对颜色、滚动驱动动画和容器单位；没有预处理器，也没有 Tailwind。
- 🔒 CSS 自定义属性是类型化的，给长度类变量设置颜色会编译失败；`RegisteredProperty` 还能生成 `@property`，让浏览器动画化变量。
- 📱 响应式与可访问性类型化：断点和媒体查询可组合，语义颜色自动适配明暗模式和高对比度设置。
- 🔗 链接像 SwiftUI：页面是静态成员，`.apps` 会自动补全，不存在的页面无法编译；构建后还会检查生成 HTML 中的链接和 ID。
- 📜 带交互的组件是自定义元素，脚本只作用于自身元素，不会误伤页面其他部分；无需框架和打包器。
- 🚀 体积小、速度快：博客文章压缩后约 14 KB，应用页约 29 KB，无 Web 字体，图片懒加载，悬停链接可后台预加载。
- 📝 内容即数据：每个应用是带类型化元数据的 Markdown，`@Frontmatter` 宏生成解码器，`@NonEmpty`、`@CalendarDay` 等会拒绝无效值并给出文件与行号。
- 🔄 构建时从 App Store、GitHub 和 npm 获取评分、价格、下载量等数据并缓存；`swift run website check` 可捕获编译器无法发现的问题。
- 🧪 警告会导致构建失败，数百个测试检查类型无法覆盖的情况；自动补全和重命名重构让大改动更安心，`swift run website serve` 保存即刷新。
- 🌐 源码已开源；1999 年风格主页作为压力测试，包含 81 个自定义元素、留言簿、外星人游戏、虚拟独角兽和 MIDI 点唱机。

---

### [](https://github.com/sindresorhus/sindresorhus.github.com)

**原文标题**: [GitHub - sindresorhus/sindresorhus.github.com: Personal website of Sindre Sorhus · GitHub](https://github.com/sindresorhus/sindresorhus.github.com)

这是 Sindre Sorhus 的个人网站仓库（sindresorhus.github.com），一个公开的静态个人网站项目，使用 Swift 生成、Markdown 写作，并通过 GitHub Pages 与 Cloudflare 部署和缓存。

- ⭐ 仓库为 Sindre Sorhus 个人网站，站点是 sindresorhus.com，公开，约 365 stars、71 forks、18 watchers。
- 🏷️ 主题包括 personal-website、sindresorhus、unicorns、website；采用 MIT 许可，并包含行为准则与贡献指南。
- 🧱 站点用 Swift 生成；内容为 content/ 下的 Markdown，静态文件在 public/；带独立文件的页面使用目录 + index.md。
- ⚙️ 开发命令：swift run website build 写入 dist；serve 本地服务并热重载；check 构建并检查拼写等问题；swift test 运行测试。
- 🖼️ 预览服务器提供 /_gallery 组件画廊；设置 GITHUB_TOKEN 可避免 GitHub API 限流。
- 💾 本地构建会缓存 App Store、GitHub 等响应一小时，构建后快速且可离线工作。
- 🚀 推送 main、手动运行和夜间任务都会通过 ci.yml 构建、测试并发布到 GitHub Pages；无变化则跳过部署。
- 🔎 部署后把 sitemap 中的 URL 提交给 IndexNow（Bing 等），密钥位于 public/indexnow.txt。
- ☁️ Cloudflare 可对 sindresorhus.com/* 设置“缓存一切”；配置 CLOUDFLARE_API_TOKEN 和 CLOUDFLARE_ZONE_ID 后，每次部署会清除缓存。
- ⚡ CSS、图标和脚本 URL 带内容哈希（如 ?v=...），可缓存一年；Cloudflare 对 v= 查询设置一年边缘 TTL 和 immutable 头，其他文件使用默认缓存。
- 📁 仓库包含 README、license、Sources、Tests、content、public、.github/workflows 等，共有 65 次提交。

---

### [Sentry 如何调试自己的 AI 智能体 | Sentry](https://sentry.io/resources/agent-tracing-series/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=agenttracing-fy27q3-agenttracingseries&utm_content=newsletter-sponsored-link-workshop-2-register)

**原文标题**: [How Sentry debugs its own AI agents | Sentry](https://sentry.io/resources/agent-tracing-series/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=agenttracing-fy27q3-agenttracingseries&utm_content=newsletter-sponsored-link-workshop-2-register)

Sentry 举办工作坊，介绍其工程师如何在生产环境中使用 Agent Tracing 调试自身 AI 功能背后的代理；Ryan 和 Serge 将讲解如何采集追踪、调查代理行为，并在追踪数量过多时定位值得修复的故障，同时涵盖利用用户挫败感等信号规模化发现问题，以及如何入门代理追踪并审查不断增长的追踪数据。这是代理调试工作坊系列第二部分；第一部分由 Serge 讲解 traces/spans 基础，并跟踪电商、Slack、GitHub Actions 中的代理，适合新手会前点播观看。另有 Syntax 开发者播客赞助信息。

- 🧭 主题：Sentry 如何调试自家 AI 代理
- 👥 主讲：Ryan 与 Serge，聚焦生产环境中的 Agent Tracing
- 🔍 演示如何采集 traces、调查代理行为并找出关键失败
- 📈 当 traces 太多时，如何用信号（如用户挫败感）规模化发现问题
- 🚀 覆盖如何开始代理追踪并审查不断增长的 traces
- 🧩 这是代理调试工作坊系列第二部分
- 📚 第一部分：Debugging agents in different environments，Serge 讲解 traces/spans 基础，并跟踪电商、Slack、GitHub Actions 中的代理；建议新手会前点播
- 🎙️ 赞助 Syntax 开发者播客，可在常用平台收听

---

### [小巧应用与TinyJS](https://www.raymondcamden.com/2026/10/08/tiny-apps-with-tinyjs)

**原文标题**: [Tiny Apps with TinyJS](https://www.raymondcamden.com/2026/10/08/tiny-apps-with-tinyjs)

TinyJS 是一个面向桌面应用的开发方案，类似 PhoneGap/Apache Cordova，但仅用于桌面端；它结合系统 WebView 与 txiki.js 桥接，让前端可调用文件系统、原生对话框等系统能力，且打包体积通常仅约 6MB，远小于 Electron。作者通过一个 RSS 转 HTML 小应用演示了其基本工作方式。

- 🖥️ 作者此前在直播中介绍过 Tauri（HTML + Rust）和 Flet（全 Python），最近发现了另一个选择 TinyJS。
- 🧩 TinyJS 类似 PhoneGap/Apache Cordova：应用运行在系统 WebView 中，并通过桥接到 txiki.js 来执行系统调用。
- 📦 主要卖点是打包体积小，通常约 6MB，相比 Electron 非常小；它只面向桌面应用。
- ⚙️ 支持原生对话框、系统菜单、凭据存储、SQLite、应用更新等桌面应用常见能力。
- 🚀 安装后可用 `tinyjs new appname` 创建项目；默认生成 vanilla 项目，关键文件包括 `frontend` 和 `main.js`。
- 🔌 `main.js` 是后端服务层，可导出 API，前端通过 `await tiny.api.call('hello', {...})` 调用。
- ▶️ 使用 `tinyjs dev` 运行应用并启用 HMR；作者测试中重载速度非常快。
- 🧱 CLI 提供多种脚手架，包括 Alpine；每个项目有 `tinyjs.json`，用于保存项目元数据、后端文件和前端工作方式。
- 🌐 WebView 中 `fetch` 仍受 CORS 限制，但可使用 `tiny.fetch`；作者据此构建了 RSS 解析应用。
- 📰 RSS 演示使用 Alpine.js 和 rss-parser 浏览器版：先用 `tiny.fetch` 获取 XML，再用 `parseString` 解析并渲染条目。
- 📚 官方文档和原理解释适合进一步学习；作者下一步计划测试 OAuth 登录流程与自定义 URL scheme。

---

### [](https://tinyjs.app/)

**原文标题**: [tinyjs — desktop apps for macOS, Windows, and Linux in ~6 MB](https://tinyjs.app/)

tinyjs 是一个极简桌面应用运行时，用 JavaScript 编写后端，复用操作系统自带的 webview，整个应用仅约 6 MB，同时提供完整的系统访问能力与原生窗口体验。

- 📦 **核心定位**：基于系统原生 webview（macOS 用 WebKit、Windows 用 WebView2、Linux 用 WebKitGTK），后端运行在 txiki.js（QuickJS + libuv）上，不打包 Chromium、不启动 HTTP 服务、不占用端口。
- 📉 **体积对比**：Electron ≥ 150 MB、Tauri 约 10 MB、tinyjs 约 6 MB（其中运行时约 5.6 MB，窗口进程约 1–2 MB），三平台体积一致。
- 🔌 **零端口通信**：页面与后端通过私有临时目录中的 Unix socket（Windows 为命名管道）进行 RPC，无监听、无冲突、无扫描风险。
- 🖥️ **完整系统访问**：支持文件、套接字、子进程、FFI、SQLite、fetch、WebSocket 等能力。
- 🔄 **热重载**：前端修改直接换入活动窗口，后端修改自动重启进程，开发时无需构建步骤。
- 🪟 **原生外壳**：真实菜单栏、文件面板、原生 alert/confirm/prompt，以及 `tinyjs build` 生成已签名、可公证的 .app 包。
- 🌐 **可包装网站**：将窗口指向某个 URL 即可像浏览器一样运行，并通过 `tinyjs.json` 中的能力门控按来源限制原生 API 调用。
- 🤖 **对 AI Agent 友好**：每个项目自带 skill 文件，编码代理可直接了解全部 API。
- 🧩 **示例应用**：包括 shelf（4.4 MB 原生应用商店）、amp（Winamp 风格播放器，支持 MIDI 与 tracker 模块）、Nib（Markdown 编辑器）、Platter（黑胶唱片播放器）、World Clock（菜单栏世界时钟）、Tiny Deck（全 API 演示）。
- ⚡ **快速上手**：`tinyjs new myapp`、`tinyjs dev`、`tinyjs build` 三步即可；后端就是一个导出 `api` 对象的 JS 文件，页面通过 `tiny.api.call()` 调用。
- 🧪 **框架支持**：提供 React、Vue、Svelte、Solid、Preact、Lit、Alpine 等 TypeScript 模板，集成 Vite 与 HMR；默认模板零依赖、纯 HTML/CSS/JS。
- 🛠️ **无需 Node**：运行时与 CLI 均基于 txiki.js，仅在选用 Vite 模板时开发/构建阶段需要 Node。
- 🚧 **平台限制**：需在目标平台构建（不支持跨平台打包），macOS 稳定，Windows 与 Linux 为 beta；不支持 iOS 和 Android。
- 📤 **发布流程**：内置签名、公证、`tinyjs publish` 更新清单，更新器校验 sha256 与代码签名，支持原地替换、重启与失败回滚。
- ⚖️ **对比取舍**：相比 Electron，放弃统一渲染引擎与 Node 原生插件；相比 Tauri，后端为 JavaScript、原生 API 无需插件，但 Tauri 生态与移动端更成熟；相比 Neutralino，tinyjs 提供真正的后端进程而非 localhost WebSocket 代理。
- 📜 **许可**：MIT 许可，作者 tarwin。

---

### [](https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/)

**原文标题**: [yet another way to invoke functions without parentheses - bartosz's blog](https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/)

文章介绍一种在 JavaScript 中不使用括号就能调用任意函数的新技巧，核心是利用 `Error.prepareStackTrace`、原型污染与 `toString`/`valueOf` 等机制组合生成并执行代码。

- 🔍 核心思路：覆盖 `Error` 对象的 `prepareStackTrace` 函数；它通常在访问 `error.stack` 时被调用，用于格式化堆栈跟踪。
- ⚙️ `prepareStackTrace` 的参数为错误对象和堆栈的结构化表示（代码位置数组），其函数签名与 `Function` 构造函数相同。
- 🧩 若第二个参数是合法 JavaScript 代码，就能借此生成任意函数；但堆栈本身是 `Array`，直接使用会报语法错误。
- 🛠️ 需控制 `Array.prototype.toString()` 的返回值，使其返回所需 JS 载荷。方法一：直接用常量函数覆盖；方法二：通过原型污染把载荷塞入其他函数再覆盖 `Array` 原型。
- 💡 作者选择留在 `Error` 领域：利用 `Error.prototype.toString`，并通过污染 `Object.prototype.message` 来操控输出。
- 🚀 结合函数生成与数组转字符串，即可生成任意 JavaScript 函数。
- ✅ 调用新函数可用 `valueOf` 技巧：覆盖对象的 `valueOf`，再将其作为原始值调用；也可用 `toString` 并与字符串拼接。
- 📜 最终载荷示例：`Object.prototype.message='alert\x281337\x29'; Array.prototype.toString=Error.prototype.toString; Error.prepareStackTrace = Function; const x = new Error; x.valueOf=x.stack; +x;` 可在浏览器控制台尝试。

---

### [](https://sergiodxa.com/articles/the-remix-way)

**原文标题**: [The Remix Way](https://sergiodxa.com/articles/the-remix-way)

Sergio Xalambrí 于 2026 年 10 月 2 日分享了他用仍处 alpha 阶段的 Remix v3 重建博客与应用的经验，并由此总结出一套“Remix 方式”：强调契约驱动、Web 标准、近零依赖、按需水合，以及路由、MCP、后台任务等统一抽象。最终他构建了 88 个包、11 个应用。

- 🧪 起点：作者用 Remix v3（v0.0.0-alpha.3）重建近 650 篇文章的博客，涉及 D1 数据库、RSS/Atom/JSON Feed、缓存、Markdown 与代码高亮。
- 🧩 契约驱动：Remix 不只提供实现，还提供 Database、SessionStorage 等契约；作者据此构建 @sdxc/data-table-d1、@sdxc/data-table-sqlstorage、@sdxc/session-storage-kv。
- 💾 缓存抽象：@sdxc/cache 定义 Cache 契约，包含内存实现用于测试，以及 Worker KV 实现用于生产。
- ✉️ 邮件传输：为监控应用定义 Transport 契约，先用 Resend，后无缝切换 Cloudflare，仅需改一行代码。
- 💳 计费抽象：自建 Billing 契约，并以 Memory、Stripe、Polar 三种实现验证契约是否合理。
- 🎨 组件模型：基于 remix/component 构建 UI，尽量少用客户端 JS；博客实现零水合，监控应用只水合必要组件。
- 🧵 样式系统：用 @sdxc/u 在 remix/component 的 css mixin 上实现类似 Tailwind 的可嵌套 mixin，并配合 @sdxc/ui 使用。
- 📦 近零依赖：作者自建大量包，如 api-client、auth、billing、cache、cron、markdown、rss、mcp、jobs 等，第三方依赖很少且多为开发依赖。
- 🛣️ 路由设计：Remix 路由器将路由定义与处理映射分离，支持懒加载、服务端与客户端复用，以及类型安全的 URL 解析。
- 🤖 MCP 集成：用 @sdxc/mcp 把工具和资源定义成类似路由处理器，MCP 服务器直接挂到 Remix 路由器上。
- ⏰ 后台任务：@sdxc/jobs 用 jobs 表定义任务、cron 与输入 schema，配合 dispatcher、中间件和类型安全入队。
- 🌐 Web 原语：优先使用 Web API 与标准，例如 Dialog 用 command/commandfor 触发，i18n 使用 Unicode MessageFormat 2 与 Intl.MessageFormat。
- 🧪 示例应用：作者构建职位板 demo，使用 19 个自建包，列表仅水合一个组件，详情用 frame 按需加载，岛屿仅 846 字节。
- 🔐 Demo 细节：发布表单使用原生 dialog 属性，验证码与限流作为中间件；发布任务通过 Transport 发邮件，内存传输会落到 outbox 页面。
- 🔗 开源地址：所有包与 demo 都在 github.com/sergiodxa/monorepo，demo 位于 apps/demo。
- 🏁 结论：经过六个月、88 个包、11 个应用，作者从“用 Remix 构建”转向“按 Remix 方式构建”。

---

### [](https://julesblom.com/writing/react-visual-notation)

**原文标题**: [A visual notation for React's parent and owner trees | JulesBlom.com](https://julesblom.com/writing/react-visual-notation)

本文介绍 Jules Blom 提出的一种 React 可视化记法，用于将组件的父树与 owner 树绘制成图，从而提供代码本身难以展示的结构性概览；文章发布于 2026 年 10 月 8 日。

- 🧩 核心主题：为 React 的 parent tree 与 owner tree 设计可视化记法。
- 📊 主要用途：把 React 组件表示为图表，便于查看组件之间的结构关系。
- 🔍 价值主张：弥补仅阅读代码时难以获得整体结构概览的不足。
- ✍️ 作者信息：文章由 Jules Blom 撰写。
- 📅 发布时间：2026 年 10 月 8 日。
- 📚 页面信息：包含目录区域，但目录内容显示为加载中。

---

### [](https://julesblom.com/react-trees)

**原文标题**: [React Trees Playground | JulesBlom.com](https://julesblom.com/react-trees)

React Trees Playground 由 Jules Blom 制作，是一个将 React 代码以“父级—所有者”记法静态可视化的工具，用于理解初始渲染中的父树与所有者树关系。  
- 🧩 粘贴 React 代码，即可用 parent-owner 记法阅读 React 的父树与所有者树。  
- 📘 若不了解父级与所有者的区别，可先阅读《Parents & Owners in React: Data Flow》。  
- 🗂️ 横行代表父树，即输出落点；弧线代表所有者树，即 props 来源。  
- 🖱️ 点击边界方块、context provider 或 memo 圆盘，可查看其覆盖范围。  
- 🧪 仅绘制初始渲染：hooks 返回初始值，effects 与数据获取不执行，未知 imports 变成命名透传行。  
- 📚 提供多类示例：context & memo、状态下移、内容提升、廉价 context、标题 context、Suspense & lazy、reducer & context、错误边界、portal modal。  
- 🏷️ 标记包含 arcs、lanes、ids、state、force、suspended、errored、contexts、share、copy link。  
- 🔍 阅读标记说明：component、宿主元素、结构 fiber、父级结构、所有者边、React.memo、createPortal 目标、lazy、context、Suspense、error boundary、Profiler、Activity、ViewTransition。  
- 🧭 特殊标记中，Profiler 测量区域渲染，Activity 控制子树挂载/隐藏，ViewTransition 将子树作为整体动画，Suspense/error boundary 捕获且排他。  
- 🔗 支持分享与复制链接，便于保存或传播当前视图。

---

### [](https://blog.master.dev/testing-an-iframes-postmessage-handler/)

**原文标题**: [Testing an iframe’s postMessage Handler – Master.dev Blog](https://blog.master.dev/testing-an-iframes-postmessage-handler/)

本文以 iframe 中“请求父页面调整自身高度”的 widget 为例，说明 postMessage 监听器默认可被任何能引用目标窗口的窗口调用；通过三种攻击展示天真实现的风险，并依次加入 origin、source、payload 校验与高度 clamp，最后给出发送端 targetOrigin 和反向回复的安全实践。

- 🧱 iframe 像“砖墙”：父子文档 CSS/DOM 隔离，同源策略进一步阻止跨源脚本互访，但真实嵌入仍需受控通信。
- 🚪 postMessage 是官方通信门：任何能引用目标 window 的窗口都能发消息，message 监听器若不校验，就像公开无认证 API。
- 📦 典型需求：评论、结账等 widget 测量自身高度，用 `parent.postMessage({type:'resize', height}, '*')` 请求父页面调整 iframe 尺寸。
- ⚠️ 天真父页面：只监听 message 并直接设置 `event.data.height`，不检查来源、窗口或数据形状；首次能工作，但隐患很大。
- 🚨 攻击 1 错误 origin：陌生页面可伪造 `{type:'resize', height:1 或 999999}`，导致 widget 被压成 1px 或撑爆页面。
- ✅ 修复 1：严格比较 `event.origin` 与预期 origin，不要用 `includes`、宽松正则，也不要允许字符串 `"null"` 作为 opaque origin。
- 🚨 攻击 2 正确 origin 错误窗口：同源的其他 iframe 也能通过 origin 检查，若 handler 信任“同源”会混淆多个嵌入实例。
- ✅ 修复 2：比较 `event.source` 与 `iframe.contentWindow`，只接受目标 iframe 的消息；但仍需保留 origin 检查，并隔离不信任代码。
- 🚨 攻击 3 合法数据攻击：height 可为 `-50`、`1e9`、字符串、`null`、`NaN`、`Infinity` 等；postMessage 用结构化克隆，`null` 读取 `.height` 会抛错。
- ✅ 修复 3：先验证 payload 是非 null、非数组对象且 `type === 'resize'`，再要求 height 为有限 number，避免 `Number()` 强制转换，并 clamp 到安全范围（示例 100–1200px）。
- 🧾 完整 handler 顺序：origin -> source -> payload -> clamp；每次拒绝记录原因，开发时保留日志，生产替换为 no-op/指标并加入速率限制。
- 📤 发送端安全：targetOrigin 不要用 `'*'`，应指定唯一允许接收的 origin；回复时用 `event.source.postMessage(..., event.origin)`。
- 🛡️ 额外加固：不需要收消息就别注册 listener；同时了解 sandbox、CSP frame-ancestors、MessageChannel 等机制。
- 🧪 本地复现：克隆仓库运行 `python3 serve.py`，host 在 `localhost:4173`、widget 在 `4174`；两个端口即两个 origin，`file://` 无法复现。

---

### [](https://anoma.ly/notes/opencode-2-0/)

**原文标题**: [OpenCode 2.0](https://anoma.ly/notes/opencode-2-0/)

OpenCode 2.0 是一次重大重构，基于数百万每日用户经验，带来大量新功能、性能提升和错误修复，目标是让代理系统更灵活地满足各种需求。

- 🚀 服务架构：2.0 默认自动以单一后台进程运行，TUI、Web 界面和桌面应用都连接同一中心服务。
- 🧩 编程接入：@opencode/client 可自动发现本地服务，支持 CLI 的 opencode api 命令，也可通过 /pair 或 opencode pair 连接其他应用。
- 🔄 API 重写：旧 API 从零重建，支持几乎所有代理需求；OpenCode 能调用自身 API，例如把当前会话移入 git worktree。
- 📦 客户端包：发布 @opencode/client，提供原生 JavaScript 和 Effect 客户端，适合脚本与定时任务。
- 💻 Code Mode：@opencode/codemode 内置极简 JavaScript 解释器，把 MCP 服务器或 OpenAPI 端点转换为代理可调用的函数。
- 🔗 工具编排：Code Mode 可单次往返调用多个工具、映射结果并继续调用；所有 MCP 服务器默认启用，减少上下文膨胀。
- 🧵 后台子代理：主代理可把任务交给后台子代理并继续工作，支持自动或手动触发，甚至使用不同模型。
- ⚙️ 后台 Shell：Shell 工具可异步运行长任务，完成时通知；可按 ctrl+b 把前台命令或子代理移到后台。
- 🔌 插件系统：2.0 几乎所有功能都以内部插件实现，已有 80+ 插件；TUI 插件转为稳定，支持热重载和自写自用。
- 🧰 SDK：@opencode/sdk 让 OpenCode 可作为库使用，复用 CLI 代码，可部署到服务器或 Durable Objects，并连接任意 OpenCode 客户端。
- ⬆️ 升级方式：CLI 先确保在最新 1.x，再运行 opencode upgrade --major；桌面端下载最新版。
- ⚠️ 破坏性变更：1.0 插件不再工作，Server API 完全不同，tui.json 配置移至 json；其他变化大多向后兼容，可让 OpenCode 按文档自动迁移。

---

### [](https://github.com/earendil-works/pi)

**原文标题**: [GitHub - earendil-works/pi: AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI · GitHub](https://github.com/earendil-works/pi)

Pi 是 earendil-works 推出的极简、可扩展 AI agent 工具包，提供统一 LLM API、agent loop、TUI 与编码 agent CLI，采用 MIT 许可；仓库热度约 11.5 万 stars、1.46 万 forks，并包含完整 monorepo、安装与开发流程。

- 🧩 **定位**：Pi 是可按个人工作流定制的 agent harness，支持 extensions、skills、prompt templates、themes，并可打包为 Pi packages 通过 npm 或 git 分享。
- 🤖 **能力边界**：内置强大默认功能，但不包含 sub-agents 和 plan mode；可让 Pi 自行构建，或安装符合自己方式的包。
- 🖥️ **使用方式**：支持交互模式、print/JSON 模式、RPC，以及 Pi TypeScript SDK；OpenClaw 是实际集成案例。
- ⚙️ **安装**：提供 curl 与 Windows PowerShell 安装脚本，也可用 npm 安装 `@earendil-works/pi-coding-agent`；要求 Node.js 22.19+，可用 `pi update` 更新。
- 🔐 **登录运行**：进入目标项目目录后运行 `pi`，使用 `/login` 连接订阅或 API key，然后给 Pi 分配任务。
- ❄️ **Nix 支持**：可用 `nix run github:earendil-works/pi/stable` 运行，支持 Linux/macOS 的 ARM64 与 x86-64，并可固定版本。
- 📦 **Monorepo 包**：包含 chord、pi-telemetry、pi-ai、pi-durable、pi-agent-core、pi-coding-agent、pi-tui；Slack/聊天自动化见 pi-chat。
- 🛡️ **权限与容器化**：无内置权限系统，默认继承启动用户权限；更强隔离可选 Gondolin、Docker、OpenShell 等方案。
- 🤝 **贡献规则**：遵循 CONTRIBUTING.md 与 AGENTS.md；新贡献者 issue/PR 默认自动关闭，维护者每日审查，长期计划见 RFCs。
- 🧪 **开发命令**：常用 `npm install --ignore-scripts`、`npm run build`、`build:offline`、`check`、`./test.sh`、`./pi-test.sh`。
- 🔗 **本地包消费**：用 `npm run pack:packages` 生成统一产物，再用 `use-local-packages.mjs` 配置外部 npm/pnpm 项目。
- 🏗️ **独立二进制**：可从 GitHub release 源码包与 SHA256SUMS 校验后，用 `build-binaries.sh` 构建，支持离线模型数据与指定平台。
- 🔒 **供应链加固**：外部依赖精确锁定，设置 `min-release-age=2`，以 package-lock 为准，阻止意外 lockfile 提交，并运行 npm audit/signatures。
- 📊 **社区分享**：鼓励分享 OSS coding agent 会话；可用 `badlogic/pi-share-hf` 发布到 Hugging Face，作者也公开 pi-mono 会话。
- 📜 **许可**：项目采用 MIT 许可，pi.dev 域名由 exe.dev 捐赠。

---

### [](https://tamagui.dev/blog/version-three)

**原文标题**: [Tamagui 3: a new native runtime, more native compilation, flat style props, React Strict DOM, and Tailwind syntax for one cross-platform UI codebase.](https://tamagui.dev/blog/version-three)

Tamagui 3 是面向 React Native 与 Web 的统一 UI 大版本升级，核心包括 C++ 原生样式运行时、改进的优化编译器、扁平样式 props、React Strict DOM/Tailwind 前端，并清理旧 API，新增 LSP、多选 Select、Field/Form、统一 Adapt、一等动画 API 与内联主题变量。

- 🚀 核心目标：让更多样式工作移出 React 渲染路径，同时保持 React Native 与 Web 共用一套 UI 代码库。
- 🧠 优化编译器：V3 在原生端支持更多条件表达式、嵌套三元、独立条件 props、静态 spread、styled.dynamic() 和 .resolve() 链；静态布局与颜色可被提升，Web 端提取原子 CSS。
- ⚡ 原生运行时：@tamagui/native-registry 用 C++ 注册表链接符合条件的原生视图，主题更新经 Fabric 直接应用，不重渲染 React 组件；需 RN 0.82+ 新架构，opt-in beta。
- 🧩 扁平样式 props：基础值和条件并列在同一属性值中，支持字符串与对象形式，如 bg="background hover:background-hover"、p="4 sm:6"，并支持 dark:sm:hover: 链式修饰符。
- 🧹 配置 v6 重命名：多词主题键改为 kebab-case（如 border-color、background-hover），提供 flat-values codemod 先报告后写入。
- 🌐 React Strict DOM：以 html 为作者表面，写语义元素，在 Web 渲染为 DOM，在原生渲染为 React Native 等价组件。
- 🎨 Tamagui Tailwind：在同一表面上用 className 写工具类，Web 编译为原子 CSS，iOS/Android 解析为 RN 样式，并与 Tamagui props 共用编译器、tokens 和主题。
- 🧱 styled/unstyled 按导入路径：tamagui 是默认带样式组件包；@tamagui/ui 和逐组件包提供无样式行为/部件；tamagui/unstyled 统一重导出。
- 🧪 零运行时与原生可选路径：Web 可用 experimental.zeroRuntime: 'report' 或 enforce 将符合条件的入口编译为 React host 元素和 CSS；原生运行时与普通编译绑定分离。
- 🦀 语言服务器：@tamagui/lsp 为 Rust 单二进制，提供补全、诊断、hover token/主题解析和内联色块；支持 VS Code、Neovim、Helix、Zed、Emacs、Sublime、JetBrains，使用 tree-sitter 边写边解析。
- 📊 优先级分层：base styled() < variants < component resolvers < callsite style props < style；className 与 callsite props 同层；同一 flat value 内 clause 顺序无关，按平台、条件数量、类别排序。
- 🔁 样式组合新 API：style() 定义可复用样式，styled.dynamic() 处理依赖单一 prop 的值，.resolve() 处理依赖完整 props 的样式；v4 计划零运行时静态提取。
- 🗑️ 移除旧 API：focusable→tabIndex、fullscreen→position/inset、themeInverse→theme="inverse"、styleable→createStyledHOC；useProps/usePropsAndStyle 移除，useStyle 仅解析 style piece。
- 🪙 Token 变化：移除 $true 和 true token；控件尺寸改为 xs/sm/md/lg/xl，md 默认；@tamagui/get-token 不再运行时步进，改用 getVariableValue 与系数。
- 📏 字体值：数字 fontSize 保留平台默认行高，字符串如 "17px" 表示精确像素；v5 配置将 font size/lineHeight 固定为 px 字符串以保持 v2 视觉。
- 🌗 主题更新：推荐 inverse 作为普通 sub-theme；新增 <ThemeUpdate> 内联覆盖主题值，支持 dark:、blue:、ios: 等修饰符；config variables 取代 defaultProps。
- 📱 Sheet 与 Adapt：Sheet.Frame 拆为 Sheet.Container 和 Sheet.Background，Overlay 必须是直接子级；Dialog/Popover/Select 统一 Adapt handoff，滑出期间保持挂载，并有 typed onTransition。
- 🎞️ 动画 API：导出 useAnimationDriver、useAnimatedNumber、useAnimatedNumberStyle 等；CSS driver 用 rAF 和真实完成回调；onTransition 取代 onDidAnimate；Sheet 暴露 useAnimatedPosition。
- ♿ FocusScope 与组件行为：FocusScope 支持 noFocus，不再支持 function-as-children；更多 data-state="open|closed"；Select 支持 multiple 和 string[] value；Tabs 默认 automatic；Slider、Separator、Avatar.Fallback 等修复。
- 📝 Field/Form：新增 behavior-only Field，Form 成为跨平台字段协调器，自动关联 label/description/error/control，支持函数或 Standard Schema（Zod 4、Valibot、ArkType）校验，并聚焦首个无效控件。
- 🖼️ 图标与 ScrollView：Icons 按当前 font.size 比例解析，移除 @tamagui/lucide-icons-2，可用 CLI 按需生成；@tamagui/scroll-view 不再经 react-native-web，提供干净 Web 实现。
- ⚖️ optimizeFor：Web 默认 updates（细粒度 theme/media 跟踪，重渲染更少），native 默认 first-render（首屏更快，可能重渲染更多）；主题/媒体变化仍生效。
- 🛠️ 迁移：用 @tamagui/cli setup 或 migrate --from v2；给编码代理 CLI 打印的升级 prompt；运行 tamagui check --strict 与 flat-values codemod；搜索移除 API/旧模式，并确保 SafeAreaProvider 位于 TamaguiProvider 外。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=javascriptweekly&utm_term=home&utm_content=Cooperpress)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=javascriptweekly&utm_term=home&utm_content=Cooperpress)

Expo 是面向 AI/代理式移动开发的基础设施，提供从开发、测试、部署到监控的完整工具链。它基于 React Native/Expo，支持用单一代码库构建 iOS、Android 和 Web 应用，并通过 EAS 服务、云模拟器和 OTA 更新加速发布与迭代，已服务 300 万+ 开发者并获得 50K+ GitHub stars。

- 🚀 定位：面向代理式工作流的移动基础设施，整合 CLI、Skills 和 MCP，支持 AI 原生应用开发。
- 🧱 四大环节：Develop、Test、Deploy、Monitor。
- 📱 开发工具：Expo SDK、Expo CLI、Expo Go、Snack、Orbit；可在任意设备上开发测试。
- ☁️ 测试能力：云模拟器与设备基础设施，可供团队和编码代理按需运行测试，无需 Mac。
- 🚢 部署发布：Build 和 Hosting 将应用分发到 Android、iOS 与 Web；Launch 引导上架 App Store。
- ⚡ 更新机制：Update 提供 OTA 更新、渠道与灰度发布，快速推送修复和改进。
- 📊 可观测性：Observe 展示崩溃、性能指标和 Update 采用率，并支持快速修复。
- 🧩 Expo SDK：10+ 年积累，100+ 生产级 API，一次安装即可使用，兼容原生代码。
- 🌐 多技术栈：支持 Expo、React Native、Swift、Jetpack Compose、Kotlin。
- 🤖 代理能力：云模拟器可由编码代理驱动，自动运行、验证并附带截图、录屏和日志。
- 🔄 自动化：Workflows 自动完成构建、测试、更新和发布。
- 📈 规模数据：7M+ 每周下载、100K+ 活跃开发者、500K+ 项目、100K+ 每日构建。
- 👥 社区与信任：80% React Native 开发者选择 Expo，Discord 70K+ 成员，Meta 推荐，React Foundation 成员。
- 🔐 合规：SOC 2 Type II、GDPR、CCPA、SSO 合规。

---

### [](https://h3.dev/blog/v2)

**原文标题**: [H3 v2 - H3](https://h3.dev/blog/v2)

H3 v2 已于 2026-10-03 稳定发布：这是基于 Web 标准的完全重写，兼容大多数 v1 工具，速度更快、体积更小。

- 🎉 H3 v2 现已稳定，整体重写并保持与多数 v1 工具兼容。
- 🌐 Web 标准优先：基于 Request、Response、URL、Headers；处理器使用 event.req、event.url 和 event.res，返回值会自动转换为 Response。
- 🚀 跨平台运行：同一应用支持 Node.js、Bun、Deno、Cloudflare Workers、Service Workers 和浏览器；srvx 提供通用服务器层，event.req.runtime 可访问运行时细节。
- 🌳 类 URLPattern 路由：采用 rou3 v1，支持命名参数、正则约束、可选/重复参数、分组和通配符，并按树状逐段匹配保持快速。
- 🧩 中间件与插件：支持 (event, next) 中间件、内置 onRequest/onResponse/onError/basicAuth/bodyLimit 等助手，以及 definePlugin() 可复用插件。
- 🔒 类型安全：处理器、响应和 HTTPError 均有类型；验证处理器及 body/query/params 校验可配合任何 Standard Schema 库。
- 📏 路由规则：h3/rules 引擎可通过一个配置对象为路由组添加 headers、重定向、CORS、缓存和代理。
- 🧰 内置工具：包含 cookies（含分块）、sessions、CORS、代理、静态文件、缓存头、SSE、通过 crossws 的 WebSockets、JSON-RPC/MCP 助手和 h3/tracing 插件。
- ⬆️ 升级友好：多数 v1 工具继续可用，弃用的 v1 名称仍会导出；Node.js 环境要求 >= 20.19。
- ❤️ 特别感谢：感谢贡献者、测试者、社区、Nitro 社区和赞助者，并邀请加入 Discord 分享反馈。

---

### [](https://h3.dev/migration)

**原文标题**: [Migration - H3](https://h3.dev/migration)

概述总结
- 📦 H3 v2 处于 beta，可通过 nightly 渠道试用，迁移指南可能持续更新。
- 🟢 要求 Node.js >= 20.19，推荐最新 LTS，仅 ESM；CJS 可通过 require(esm) 使用 require("h3")，也支持 Bun/Deno。
- 🌐 基于 Web 标准 URL、Headers、Request、Response；Node 下用 srvx 兼容层，其他运行时用原生 Web API。
- 🔄 event.web 更名为 event.req；event.node.{req,res} 仅 Node 运行时可用，未来建议 event.runtime.node。
- 📤 响应需显式 return 或 throw；send/sendError/sendStream/sendWebResponse 改为 return 值、throw createError、return stream/response。
- 🧩 其他响应工具：sendNoContent→return noContent()，sendIterable→return iterable()，sendProxy→return proxy()，sendRedirect→return redirect()，handleCors 需检查返回值。
- 🛣️ Router 已并入 H3 核心：用 new H3() 替代 createApp()/createRouter()；采用新路由引擎 rou3。
- 🧭 中间件 app.use("/path") 仅匹配 /path，匹配子路径需 "/path/**"；event.path 为完整路径，可用 withBase() 处理前缀。
- ⚙️ Router API 变化：router.add(method, path)、router.all 替代 router.use；不再支持 lazy 数组/多路径写法，移除 app.resolve。
- 📥 请求体优先用 event.req.text()/json()/formData()/body；readBody 支持 JSON 与 urlencoded；无请求体返回空值。
- ⚠️ request.json/readBody 不再使用 unjs/destr，需过滤和清理用户数据，避免原型污染。
- 🍪 Headers 原生化：header 值始终为字符串；Set-Cookie 使用 headers.getSetCookie 获取数组。
- 🧹 弃用/更名：createError→HTTPError，eventHandler/defineEventHandler→defineHandler，lazyEventHandler→defineLazyEventHandler，useBase→withBase。
- 🔧 请求工具迁移到 event.req.headers/get、event.req.method、event.url.pathname；x-forwarded-proto 默认不信任，需显式开启。
- 🗂️ 响应工具迁移到 event.res.headers/status/statusText；Node 工具改为 defineNodeHandler、fromNodeHandler、toNodeHandler。
- 🧪 移除 Web/Plain 工具与大量类型导出；Body 工具迁移到原生方法，isStream/isWebResponse 改用 instanceof。
- 📝 类型更名：App→H3、AppOptions→H3Config、NodeListener→NodeHandler、H3Headers/Response→原生 Headers/Response 等。

---

### [](https://shaders.com/updates/shaders-is-open-source)

**原文标题**: [Shaders is now open source — Shaders](https://shaders.com/updates/shaders-is-open-source)

Shaders 渲染引擎、着色器组件和框架绑定于2026年10月6日以 MIT 许可证开源，核心基础向所有人开放；Shaders Pro 继续作为最快发现、定制和交付 WebGPU 效果的方式，订阅权益与价格保持不变。

- 🚀 2026年10月6日宣布：Shaders 渲染引擎、所有 shader 组件及框架绑定现已开源，采用 MIT 许可证。
- 🎯 初衷是让设计工程师无需成为图形程序员，也能使用创意 shader 效果。
- 🤖 AI 让 shader 创作更简单，但开放基础更有价值；你和智能体可基于生产级组件及优化的 WebGPU 运行时构建。
- 🧩 任何人都可在个人、商业客户项目、SaaS 和内部工具中使用 Shaders 组件，无需许可证。
- 📤 可从设计编辑器免费导出代码，设计 shader 并发布，无限制。
- 🧪 可编写自己的组件（实验性）；defineShader 语言已公开并有文档，欢迎提交 PR。
- 💎 Pro 订阅保留全部现有权益：1000+ Pro 预设、55+ 预构建区块、无水印渲染视频和图片、专属 Discord 角色与频道、优先支持。
- 💰 Pro 定价不变；若过去30天内仅为商业用途或代码导出购买 Pro 且受影响，可联系团队解决；旧 Core 订阅将免费获得 Pro 权益。
- 💬 创始人 Simon 期待社区推动发展，并欢迎在 Discord 交流。

---

### [组件 — 着色器文档](https://shaders.com/docs/components)

**原文标题**: [Components — Shaders Documentation](https://shaders.com/docs/components)

该内容展示了一个包含 190+ 个视觉特效组件的库，按功能划分为九大类别，涵盖纹理生成、形状绘制、材质效果、风格化处理、交互模拟、变形扭曲、转场过渡、模糊及色彩调整，每个组件均以 JSX 标签形式列出并附带简要说明。

- 🧩 组件总数超过 190 个，分为纹理、形状、形状效果、风格化、交互、扭曲、过渡、模糊、调整共 9 大类
- 🎨 纹理（55 个）：能独立生成完整画面的图案，如极光〈Aurora〉、光束〈Beam〉、砖墙〈BrickPattern〉、彩色噪点〈PerlinNoise〉、大理石〈Marble〉、等距立方体〈IsometricCubes〉等
- 🔷 形状（16 个）：基于有符号距离场的高分辨率几何图形，含圆、星、心、水滴、圆角矩形、平行四边等
- 💎 形状效果（23 个）：给形状赋予玻璃、金属、水晶等真实材质与光照，如拉丝金属〈BrushedMetal〉、铬〈Chrome〉、全息〈Hologram〉、霓虹〈Neon〉、水〈Water〉
- 🖌️ 风格化（31 个）：对下层图层施加整体视觉处理，如 ASCII 字符画、粉笔、CRT 屏幕、故障〈Glitch〉、胶片颗粒、半色调、VHS
- 🖱️ 交互（16 个）：响应鼠标的模拟效果，如鸟群〈Boids〉、光标涟漪、墨流〈InkFlow〉、磁屑〈MagneticFilings〉、反应扩散〈ReactionDiffusion〉
- 🌀 扭曲（22 个）：对图层进行弯曲、位移等形变，如鼓包〈Bulge〉、万花筒、极坐标转换、3D 透视、旋转扭曲〈Twirl〉
- 🔄 过渡（13 个）：两层之间的擦除与溶解，如百叶窗、棋盘擦除、虹膜擦除、翻页、随机条带
- 🌫️ 模糊（9 个）：从景深到移轴的各类模糊，含高斯模糊、散景〈BokehBlur〉、通道模糊、移轴〈TiltShift〉、缩放模糊
- 🎚️ 调整（14 个）：面向任意图层的色彩与明暗校正，如曝光、双色调、胶片色调〈FilmStock〉、色相旋转、色调分离、自然饱和度

---

### [](https://nodejs.org/en/blog/release/v26.11.0)

**原文标题**: [Node.js — Node.js 26.11.0 (Current)](https://nodejs.org/en/blog/release/v26.11.0)

## 概述总结

Node.js 26.11.0（Current）于 2026-10-07 发布，由 Antoine du Hamel（@aduh95）主导。本次更新带来大量 SEMVER-MINOR 新特性、性能优化与安全修复，覆盖 buffer、http、perf_hooks、crypto、sqlite、ffi、stream 等核心模块，并同步升级多项依赖。

- 📅 **版本信息**：Node.js 26.11.0（Current），发布日期 2026-10-07，发布人 @aduh95
- 🧱 **Buffer 增强**：新增 `isLatin1` 与 `Buffer.stringLength()`，并修复大缓冲区负索引与 UTF-16LE 的 `indexOf` 起始位置问题
- 🌐 **HTTP 增强**：新增 `isValidHeaderName()` 与 `isValidHeaderValue()`，并优化请求路径归一化与服务器热路径性能
- ⚡ **HTTP/2 新选项**：新增 `connectionWindowSize` 配置项
- 📊 **perf_hooks 升级**：新增 `histogram.diff()`、`histogram.snapshot()`，支持记录 0，修复 `monitorEventLoopDelay()` 分辨率截断，并强化 CBOR 导入校验
- 🔒 **Process 稳定化**：`process.ref` / `process.unref` 正式从实验性毕业为稳定 API
- 🗄️ **SQLite 更新**：重命名 `DatabaseSync` 与 `StatementSync`，新增虚拟表支持（`createModule()`），并改进重开连接状态恢复
- 🧩 **src 新能力**：新增 `--process-timeout=N` 参数、堆内存分析输出包含 size 与 count、允许嵌入方豁免链接绑定的 addon 权限
- 🔐 **Crypto 大量修复**：包括 AES-GCM 短 IV、PBKDF2 迭代限制、JWK 导出错误映射、RSA 模数长度报告、Argon2 无线程派生、cSHAKE/KMAC 后端支持等
- 🧵 **FFI 改进**：支持 64 位参数接受安全整数、优化指针范围校验、修复 `PrepareFunction` 释放后使用等多项内存安全问题
- 🚰 **Stream 优化**：webstreams 快速路径提速、修复 pipeline 尾端死锁、支持 `ArrayBufferView` 写入等
- 📦 **依赖升级**：NSS 根证书更新至 3.129、OpenSSL 3.5.9、npm 11.20.0、undici 8.11.2、zlib 1.3.2.1、时区数据 2026e 等
- 🐧 **平台支持**：Alpine Linux 正式升级为 tier 2 支持，新增 z/OS 与 LIEF 1.x 构建支持
- 📥 **下载资源**：提供 Windows/macOS/Linux/AIX/ARM64 等多平台安装包、二进制文件与源码，附 SHASUMS 与 PGP 签名校验

---

### [迁移到 v5 - Hono](https://hono.dev/docs/guides/migrating-to-v5)

**原文标题**: [Migrating to v5 - Hono](https://hono.dev/docs/guides/migrating-to-v5)

Hono v5 保持核心精简，将运行时适配器拆分为独立包，并带来多项破坏性变更；本文列出从 v4 迁移所需的关键更新。

- 📦 仅支持 ESM：CommonJS 构建被移除；Node.js 需 22.12 或更高版本，仍可用 `require()` 加载 ESM。
- 🧩 运行时适配器独立成包：如 `@hono/bun`、`@hono/aws-lambda`、`@hono/vercel` 等；`hono/cloudflare-pages` 移除，推荐改用 Workers。
- ⚙️ `onError()` 改为可路由中间件：签名从 `(err, c)` 变为 `(c, next)`，错误通过 `c.error` 读取；`notFound()` 支持路径和多个中间件。
- 🧵 路由规则：注册会叠加而非替换，返回响应即停止，调用 `next()` 继续；路径相对 `basePath()`，不受 HTTP 方法影响。
- 🚨 非 Error 抛出：字符串或普通对象会被包装为 `Error` 进入 `onError`，原值在 `c.error.cause`，字符串还会成为 `c.error.message`。
- 🎨 `getColorEnabledAsync()` 移除：改用 `getColorEnabled()`，Cloudflare Workers 需传入 bindings；`logger()` 已自动处理。
- ❓ `c.req.query()` 可能返回 `undefined`：类型变为 `Record<string, string | undefined>`，`queries()` 同理。
- 📥 `c.req.json()` 返回 `unknown`：不再返回 `any`，需显式指定类型或配合 `c.req.valid()`。
- 🚫 `c.json()` 对不可 JSON 序列化值抛错：`undefined`、函数或 symbol 会抛 `TypeError`，与 `Response.json()` 一致。
- 🧭 通配符匹配统一：段尾 `*` 可匹配空，段中 `*` 不是通配符，单独 `*` 匹配一个非空段；RegExpRouter 可能回退 SmartRouter。
- 🗑️ 移除废弃 API：`app.mount()` 改用 `mount` 中间件，`app.fire()` 改用 `@hono/service-worker`，`matchedRoutes`/`routePath` 改用 `hono/route`。
- 🧱 SSG 与其他移除：`toSSG()` 钩子改由 `plugins` 传入；Bearer Auth 消息配置改名；`pathResolve`、`SSG_DISABLED_RESPONSE`、`getQueryStrings()`、`UnOfficalStatusCode` 等移除或更名；`timingSafeEqual()` 仅接受字符串。

---

### [](https://github.com/handlebars-lang/handlebars.js/releases/tag/v4.7.10)

**原文标题**: [Release v4.7.10 · handlebars-lang/handlebars.js · GitHub](https://github.com/handlebars-lang/handlebars.js/releases/tag/v4.7.10)

handlebars.js 发布 v4.7.10，为最新版本，由 jaylinski 于 10 月 5 日 23:07 发布，包含自上一版本以来 251 次 master 提交；重点是多轮安全修复、依赖与文档维护，以及 `{{#each}}` 的惰性迭代兼容性变化。

- 🚀 v4.7.10 是最新发布版，由 jaylinski 发布，包含 251 个新提交。
- 🔐 安全修复：压缩时清理 source map URL；预编译输出中转义 `<!--` 和 `<script`。
- 🧠 `{{#each}}` 改为惰性迭代，并在线性时间内去除空白，提升性能与安全性。
- 🛡️ 多项加固：不信任上下文数据特殊属性；仅编译模板字符串形式的 partials；仅分派已知节点类型；在编译器而非解析器中验证 AST 值。
- ⚠️ 修复关联安全公告：GHSA-xw65-4hp5-5hc7、GHSA-p8wg-vrv2-v86f、GHSA-8r5x-fm3f-whwj。
- 📦 维护更新：澄清 `--root` 不限制文件系统访问；升级 minimist 至 ^1.2.8；修复 Ruby 组件发布文档和 Composer 组件定义。
- 🔄 兼容性说明：`{{#each}}` 现在像 `for...of` 一样遍历 Map、Set、生成器等可迭代对象，且渲染期间新增的值也会被访问。
- 👍 社区反应：获得 2 个点赞、2 个火箭等，共 4 人反应。

---

### [](https://github.com/mathiasbynens/he)

**原文标题**: [GitHub - mathiasbynens/he: A robust HTML entity encoder/decoder written in JavaScript. · GitHub](https://github.com/mathiasbynens/he)

`he` 是一个用 JavaScript 编写的健壮 HTML 实体编码/解码库，支持全部标准化命名字符引用，能像浏览器一样处理歧义 `&` 和边缘情况，并可正确处理 astral Unicode 字符；提供 `encode`、`decode`、`escape`、`unescape` API、CLI、完整测试套件及 MIT 许可。

- 🧩 **项目定位**：`he`（HTML entities）是 JavaScript 的 HTML 实体编码器/解码器，支持所有标准化命名字符引用。
- 🌐 **兼容与正确性**：像浏览器一样处理歧义 ampersand 和边缘情况，且能正确处理 astral Unicode 符号。
- 📦 **安装与模块**：通过 `npm install he` 安装；发布为 ECMAScript 模块，支持命名导出，也可在浏览器用 `<script type="module">` 引入 `src/he.mjs`。
- 🛠️ **encode API**：`he.encode(text, options)` 默认编码非可打印 ASCII 及 `& < > " ' \``；选项包括 `useNamedReferences`、`decimal`、`encodeEverything`、`strict`、`allowUnsafeSymbols`。
- ⚙️ **全局默认选项**：可通过修改 `he.encode.options` 覆盖 `encode` 的全局默认设置。
- 🔄 **decode API**：`he.decode(html, options)` 按 HTML 规范解码命名和数字字符引用；选项包括 `isAttributeValue`、`strict`，也可通过 `he.decode.options` 全局覆盖。
- 🧼 **escape/unescape**：`he.escape(text)` 转义 `& < > " ' \``；`he.unescape` 是 `he.decode` 的别名。
- 💻 **CLI**：全局安装后可用 `he --encode`、`he --decode`、`--use-named-refs`，并支持文件与管道输入输出。
- ✅ **严格模式与测试**：有完整测试套件；`strict` 可在遇到无效码点或解析错误时抛异常，适合用于 HTML 解析器/验证器。
- 🚀 **运行环境**：ES2022 模块，支持现代浏览器和 Node.js v22+；CLI 也需要 Node.js v22+。
- 🧑‍💻 **开发脚本**：`npm test` 测试、`npm run coverage` 覆盖率、`npm run build`/`fetch` 生成数据、`npm run format` 格式化。
- 🏷️ **项目信息**：作者 Mathias Bynens，MIT 许可证，仓库约 3.6k stars、264 forks、57 watchers，主题含 decode/encode/html-entities/javascript，在线演示为 mths.be/he。

---

### [v1.22.0 | React Aria](https://react-aria.adobe.com/releases/v1-22-0)

**原文标题**: [v1.22.0 | React Aria](https://react-aria.adobe.com/releases/v1-22-0)

v1.22.0 于 2026 年 10 月 8 日发布，核心新增基于原生浏览器滚动手势的 Sheet 滑动覆盖层，适合移动端托盘、导航抽屉和通知横幅；同时加入 Turbopack 支持、虚拟键盘感知的覆盖层定位，并包含多项组件修复与文档更新。

- 🆕 新增 Sheet 组件：可从视口边缘滑入的可滑动覆盖层，基于原生浏览器滚动手势。
- 👆 Sheet 适合触控场景，如移动端 sheets、导航抽屉和通知横幅。
- ⚡ `@react-aria/optimize-locales-plugin` 新增 Turbopack 支持。
- ⌨️ 覆盖层定位现支持虚拟键盘等交互式小部件。
- 🧩 通用修复包括：`GlobalDOMAttributes` 支持 `suppressHydrationWarning`，修复 `preventFocus` 的 `TypeError`，并调整开发环境可见性检查。
- 🎨 现在会对无效的 `rgb()` / `rgba()` 颜色字符串抛出错误。
- 📱 React Native 启用 `useControlledState` 早期 effect。
- 📚 Collections 在开发环境警告重复 collection key。
- 🔽 ComboBox 在空响应后异步项到达时重新打开 popover。
- 📅 Date/Time 修复年份选择器最终受限年份，并在 CLDR 不支持本地化值时使用默认纪元。
- 📋 Forms 新增开发警告，用于检测无效焦点移动。
- 🔗 Link 的 `LinkContext` 新增 `aria-current` 支持。
- 🪟 Popover 内部清除 Popover 上下文。
- 📊 Table 修复 `useGridCell` 覆盖可聚焦子项焦点恢复的问题。
- 🌬️ Tailwind 文档新增 data attributes 到 Tailwind 选择器映射说明。
- 🧾 TokenField 将 `TokenFieldContext` 作为值导出，并修复编辑 token 后光标跳动。
- 🌳 Tree 修复 `useTreeData` 子树移动验证。
- 📦 发布包包括 `@internationalized/number@3.6.9`、`@react-types/shared@3.37.0`、`@react-aria/optimize-locales-plugin@2.1.0`、`react-aria@3.53.0`、`react-aria-components@1.22.0`、`react-stately@3.51.0` 等。

---

### [](https://react-aria.adobe.com/Sheet)

**原文标题**: [Sheet | React Aria](https://react-aria.adobe.com/Sheet)

Sheet 是一个可滑动覆盖层组件，可从视口边缘滑入，用于移动端底部面板、导航抽屉、通知横幅和嵌套设置流程，并支持位置、吸附点、动画、堆叠与完整 API。

- 📐 核心定位：Sheet 从屏幕边缘滑入，支持 bottom、top、left、right、start、end、center 等位置。
- ↔️ 滑动关闭：swipeDirection 控制可滑动方向，默认与 position 相同；start/end 会随 RTL 自动镜像。
- 🧲 吸附点：snapPoints 让 Sheet 先停在部分高度，可拖拽展开或下滑关闭，支持像素和 CSS 长度。
- 🧭 场景建议：start/end 适合导航抽屉，bottom 适合移动端面板，top 适合通知横幅。
- 🎞️ 动画：swipeAnimation、swipeAnimationRange 让 CSS keyframes 与滑动手势、进出场同步，backdrop 也可动画。
- 📚 堆叠：Sheet 可嵌套，stackAnimation 让父级 Sheet 在子级打开时后退缩放，实现多级流程。
- 🛒 示例：购物车 Sheet 展示商品、数量加减、小计、配送费、总价和下单按钮。
- ⚙️ 多级设置：Settings → Account → Advanced 嵌套演示表单、保存与返回。
- 🧩 API 结构：SheetTrigger、SheetOverlay、SheetBackdrop、Sheet、SheetContent，配合 Heading、Text、Button slots。
- ♿ 交互控制：preventDismissal 可禁止滑动/Escape/外部点击关闭；shouldCloseOnInteractOutside 可定制外部关闭。
- 🎨 样式状态：提供 data-position、data-swipe-direction、data-stack-index、data-expanded、data-entering/exiting 等属性。
- 📏 CSS 变量：--sheet-scroll-padding-y/x、--visual-viewport-height/width 用于处理浏览器 UI 和软键盘遮挡。

---

### [](https://pnpm.io/blog/releases/12.12.0)

**原文标题**: [pnpm 12.12.0 | pnpm](https://pnpm.io/blog/releases/12.12.0)

pnpm 12.12.0 主要新增远程缓存共享任务结果与依赖构建、addMissingPeerTypes 设置，并让 pnpm add --config 与 pnpm update 管理配置依赖；同时修复 dangerouslyAllowAllBuilds 与 allowBuilds 的冲突，并改进部署、--depth、workspace peer 解析、安装速度与 _auth 处理。

- 📦 pnpm pipeline 可通过远程缓存跨机器共享任务结果；结果作为签名制品存放在 pnpr 或兼容 Turborepo Remote Cache API 的服务器（如 Vercel Remote Cache）。
- 🧱 远程副作用缓存可保存依赖构建到 Turborepo Remote Cache 服务器；两类缓存都读取新的 remoteCache 设置（服务器名与签名密钥），pnpm pipeline --report 按 remoteCache.org 记录运行。
- 🧩 新增 addMissingPeerTypes：将 peer 依赖的 @types 包链接到每个 peer 依赖它的包旁边，例如 peer 依赖 react 时链接项目的 @types/react，便于全局虚拟存储下 TypeScript 查找类型。
- ⚙️ pnpm add --config 与 pnpm update 现在像普通依赖一样管理配置依赖；add --config 按 pnpm add 规则在 pnpm-workspace.yaml 保存版本范围（如 ^1.2.0），并在 lock 锁旧版时重新解析。
- 🔄 pnpm update 在范围内更新配置依赖，--latest 更新到最新；指定包名时只更新该配置依赖。
- 🛡️ allowBuilds 中设为 false 的包，即使 dangerouslyAllowAllBuilds 为 true 也不再运行构建脚本；两者现在表示“除拒绝外全部允许”。
- 🧯 即使无法读取配置，pnpm 也会切换到项目固定版本；此前全局配置、.npmrc、_auth 或无法解析的 pnpm-workspace.yaml 会阻断所有命令（包括 pnpm --version）。
- ↕️ pnpm update 与 pnpm why 重新接受 --depth Infinity，修复 invalid value 'Infinity' for '--depth <DEPTH>'。
- 🔗 不带 injectWorkspacePackages 的 pnpm deploy 会像注入安装一样，把链接 workspace 包的 peer 依赖绑定到父级提供的版本，避免 ERR_PNPM_DEPLOY_AMBIGUOUS_PEER。
- 📁 pnpm deploy --legacy 遇到被部署项目的 workspace 依赖声明了项目自身未依赖的 workspace: peer 依赖时，不再报 ERR_PNPM_SPEC_NOT_SUPPORTED_BY_ANY_RESOLVER；pnpm 会从 workspace 复制该 peer 到部署目录。
- 🧷 自动安装的 workspace: peer 现在始终解析到 workspace 项目，不再从注册表安装 workspace:* 或 workspace:^1.0.0。
- 🧹 注入的 workspace 包把某依赖同时列为 peer 依赖时，重复安装不再重新解析；使用硬链接的未变更注入 workspace 包冻结安装更快。
- ⚡ 带 !generated/** 等子树排除的 workspace 发现更快。
- 🔐 _auth 中 registry URL 下不以 @ 开头的键会跳过并警告，避免未来新增字段破坏当前版本；但持有 authToken 对象却缺少 @（如 org 表示 @org）仍会报错。

---

### [JavaScript条码与二维码扫描器SDK，适用于Web应用](https://strich.io/?ref=js-weekly)

**原文标题**: [JavaScript Barcode & QR Code Scanner SDK for Web Apps](https://strich.io/?ref=js-weekly)

STRICH 是一款面向 Web 应用的 JavaScript 条码扫描 SDK，可直接在浏览器中通过摄像头实时扫描 1D/2D 条码，主打客户端处理、无需后端、零依赖、易集成，并提供透明订阅定价与免费 14 天试用。

- 📦 通过 npm 安装：`npm i @pixelverse/strichjs-sdk`，支持 NPM/CDN、TypeScript 类型绑定及所有主流 Web 框架。
- 📷 支持多种 1D 条码：Code 128、EAN、UPC、Code 39、Code 93、ITF、Databar、Codabar 等。
- 🔳 支持多种 2D 条码：QR Code、MicroQR、Data Matrix、Aztec Code、PDF417 等，包括美国驾照 PDF417。
- ⚡ 完全客户端运行，实时扫描，无需后端；利用 WebAssembly 和 WebGL 提升速度与兼容性。
- 🖥️ 内置扫描 UI：目标框、摄像头选择、闪光灯、点击对焦等；PopupScanner 可一行代码启动扫描。
- 🧠 针对挑战性条码优化：褪色/损坏印刷、光照不均/反光、反色条码等。
- 🌐 兼容 Android/iOS 主流浏览器，适配高端与低端设备，并提供各主流框架示例代码。
- 🧩 零依赖、单文件、TypeScript 类型安全，持续跟进新兴 Web 能力并优化扫描体验。
- 🏢 企业级特性：定期维护、创始人直接技术支持、可选离线操作附加组件、零网络流量。
- 🔐 安全合规、供应链风险低；NPM 采用 Trusted 和 Staged publishing；Pixelverse 是瑞士 GS1 解决方案合作伙伴。
- 💰 定价透明：Basic €99/月（最高 1 万次扫描）、Professional €249/月（最高 10 万次扫描）。
- 🏷️ Business 起价 €4,000/年（1 个应用），无限扫描和设备，按应用数量计费；Enterprise 按需报价。
- 🧾 固定年费、不按扫描量或设备数计费；支持采购订单、银行转账、Paddle，以及 SoftwareOne、SHI、worldsoft 等经销商。
- 🆓 提供 14 天免费试用与演示应用，集成通常不到一天；超限不会阻止扫描，但连续两月超限需升级。
- 📈 客户评价强调性能/准确性高、跨设备稳定、户外可靠、集成快、文档好、支持好、定价可预测。
- 🏛️ 适合将扫描流程迁到 Web：免应用商店、易分发、始终最新、降低成本、避免应用疲劳。
- 🔗 被 Brooklyn Public Library、SBB、Zeercle 等用于实际扫描流程；相比 ZXing-JS、QuaggaJS 等开源方案，STRICH 提供商业维护与支持。

---

### [推出聊天代理 | 更新日志](https://trigger.dev/changelog/chat-agent?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=js-weekly&utm_content=chat-agent-launch)

**原文标题**: [Introducing chat agent | Changelog](https://trigger.dev/changelog/chat-agent?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=js-weekly&utm_content=chat-agent-launch)

Trigger.dev 发布 chat.agent：为每段对话提供持久、有状态、无超时的 Linux 计算环境，让 AI 聊天可跨刷新、崩溃和长时间等待继续运行；它兼容 AI SDK，并内置追踪、指标、审批暂停、自动恢复和按运行计费。

- 📅 2026年8月10日发布，chat.agent 自7月2日 GA、6月起生产可用，已服务数百万会话与超84年计算。
- 🧠 每个对话拥有独立有状态机器，从首条消息启动，按需休眠/唤醒，并在轮次间保存变量、缓存和子代理。
- ⏳ 回合无超时，流可持久化；刷新会从中断处重放，关闭浏览器数天后回来对话仍在。
- 🛠️ 用 Trigger.dev task 编写回合：接收 messages 返回 stream，AI SDK useChat 直接连接，无需 API 路由。
- 🏭 Arena 的 Agent Mode 已基于 chat.agent 在生产大规模运行。
- 🐧 背后是真实 Linux 机器，可安装依赖、执行 CLI、ffmpeg、无头浏览器等；机器规格从 micro 0.25 vCPU 起，可按 agent/对话配置。
- 💾 内存跨休眠保留，但崩溃会丢堆内存；重要数据应入库，会话恢复后继续。
- 🛡️ 运行被杀/OOM 后，下条消息会启动新运行并恢复对话；部署不中断运行，用 chat.requestUpgrade() 主动升级版本。
- ⚡ Head Start 可选：首轮 LLM 调用在热服务器中与 agent 启动并行，测试中首 token 时间和整轮时长约减半。
- 🌐 Head Start 返回标准 Web Fetch handler，可挂载 Next.js、Hono、SvelteKit、Remix、TanStack Start 等，无需适配器。
- 🧾 内存快照而非事件重放，不强制确定性；Date.now、Math.random、fetch 等可正常使用。
- 🆓 等待不花钱：无 execute 的工具会让回合挂起等待审批，暂停期间不计费；支持停止、引导、编辑、分支、重新生成。
- 📊 每回合是追踪 span，内置 AI 指标仪表盘：花费、调用、TTFT、tokens/s、成本/模型、延迟百分位、最贵运行等；数据可通过 TRQL 查询，sessions.list 可列会话。
- 🧩 继续用 AI SDK：服务端 streamText，客户端 useChat，chat.agent 作为 transport；只发送新消息，历史在服务端累积。
- 🪜 可逐层深入：chat.agent 管理回合循环，自定义 agent 自己写循环，原始 session primitives 直接读写流。
- 💰 长对话更便宜：compaction 接近上下文限制时总结，prompt caching 缓存稳定前缀；触发条件与摘要可自定义。
- 📝 提示词可放代码库并随部署版本化，也可在仪表盘覆盖文本/模型，每次生成可追溯版本。
- 🤖 浏览器之外：AgentChat 可从任务、脚本或其他 agent 驱动对话；MCP server 可从 Claude Code/Cursor 对话。
- 🧪 可在单元测试中真实驱动 agent 回合，无需网络或任务运行时；因是 Trigger.dev task，排队、批处理、调度、评估等现有功能都可用。
- 🧰 OOM 自动在更大机器重试且不丢消息，recovery boot 恢复上下文，版本升级迁移挂起对话，skills 可按需加载指令/脚本。
- 📜 Apache 2.0 开源；按实际运行的 compute 时间计费，挂起不计费；文档三步上手，已有应用可用迁移指南。

---

### [](https://hyperserve.io/?utm_source=javascriptweekly&utm_medium=newsletter&utm_campaign=classified_oct13)

**原文标题**: [Video backend for Developers — Add Video Fast | Hyperserve](https://hyperserve.io/?utm_source=javascriptweekly&utm_medium=newsletter&utm_campaign=classified_oct13)

Hyperserve 是面向开发者的视频托管 API，用简单接口解决视频上传、转码、存储、CDN 分发和播放 URL 输出，让应用快速加入视频功能，无需自建视频团队或绑定专有播放器。

- 🎥 核心价值：接受用户上传的任意格式，自动转码并全球分发，无需复杂后端、专有播放器和意外账单。
- ⚡ 集成流程：后端创建视频并获取上传 URL；客户端直传无需 API key；后端完成上传并触发转码，几分钟即可添加视频。
- 🔄 输出模式：任意视频输入，输出播放 URL；Webhook 会通知处理成功，并返回各分辨率的状态与 CDN 视频地址。
- 🧱 四步功能：上传（公共/私有、自定义分辨率与缩略图）、转换（优化 MP4）、托管（全球低延迟 CDN）、交付（运行时选取合适分辨率）。
- 🛡️ 降低风险：无播放器锁定，开发者控制 UI；无需视频专业知识；按用量计费，价格可预测，无最低消费或承诺。
- 📥 支持规格：输入格式包括 MP4、MOV、AVI、MKV、WEBM、WMV、M4V、MPG，单文件最高 5GB；输出 MP4 分辨率覆盖 144p 至 8K。
- 📱 适用场景：社交与创作者内容、市场平台、SaaS 与内部工具、健康与健身等需要视频的应用。
- 💵 定价方案：免费版 $0/月，含 50 个视频、1GB/文件、250GB 带宽/月、免费编码和完整 API；按量付费推荐为 $0.04/GB 存储、$0.025/GB 带宽、免费编码。
- 📚 开发者体验：文档清晰、代码可复制，提供入门、分辨率、Webhooks、自定义元数据、文件限制等指南，以及完整 API 参考。
- 🧪 其他亮点：提供实时 Demo 测试上传、转码与播放，并对比 Mux、Cloudflare Stream、Cloudinary、api.video 等方案；定位为现代开发者的快速部署视频后端。

---

### [浏览器指纹是新的 Cookie](https://royfish.dev/fingerprints-are-the-new-cookies)

**原文标题**: [Fingerprints are the new cookies](https://royfish.dev/fingerprints-are-the-new-cookies)

禁用 JavaScript 时，页面内指纹脚本无法运行，但 IP、请求头等网络层方法仍可识别你；文章说明浏览器指纹正取代第三方 Cookie，结合广告数据交易、Google 的策略转变、指纹原理与信息熵，并给出检测与防护建议。

- 🕵️ 禁用 JS 只能挡住页面脚本指纹，不能避免 IP、User-Agent、语言等网络请求信息暴露。
- 🍪 第三方 Cookie 受限后，设备指纹成为更隐蔽的跨站追踪手段，能保持稳定身份并用于广告与数据出售。
- 💰 广告与数据经济：网站用广告获利，若你注册账号，数据买家可获取姓名、活动、与 AI 对话等，拼出极详细画像。
- 🎭 Google 叙事：2019 承诺消灭第三方 Cookie，随后以 Privacy Sandbox 拖延，最后保留 Cookie 并允许广告产品使用设备指纹。
- 🧩 指纹数据来自网络请求和代码环境：IP、请求头、GPU、CPU、内存、屏幕、音频、字体、扩展等。
- 📉 单个特征很普通，但“最新 Chrome + 法语 + M4 Mac + 硬件测量”等组合会迅速变得近乎唯一。
- 🔢 信息熵解释：越稀有的答案信息量越大；1/2 约 1 bit，1/8 约 3 bits，1/128 约 7 bits。
- ⚠️ 特征往往不独立，不能简单相加；贝叶斯告诉我们实际识别比理想模型复杂。
- 🧪 熵的应用：医学检测假阳性、密码强度、法医在百万人口中锁定个人约需 20 bits。
- 🛡️ 可到 coveryourtracks.eff.org 测试浏览器指纹独特性。
- 🌐 浏览器防护：Chrome 基本等于公开 ID；Safari/Firefox 部分防护；Brave、Tor、Mullvad Browser 有高级反指纹。
- 🧱 隐私扩展可能破坏网站，且用户少反而增加独特性；引擎级防护比扩展更有效。
- 🔬 页面示例通过 OfflineAudioContext、WebGL、Canvas、Intl、navigator、crypto.subtle 采集并哈希特征，生成固定昵称。
- 🧠 核心：指纹不必全球唯一，只需在目标样本中足够独特；不想被追踪就需选择更隐私的浏览器并接受取舍。

---

### [](https://github.com/pingdotgg/ts-rust)

**原文标题**: [GitHub - pingdotgg/ts-rust: An experimental Rust port of the TypeScript 7 compiler (tsc) · GitHub](https://github.com/pingdotgg/ts-rust)

ts-rust（又名 tsc-rs）是微软原生 TypeScript 编译器（Go 版 tsc）的实验性 Rust 移植版本，由 LLM 完成代码编写，据称在真实项目中达到 100% 兼容，并且比官方 Go 版 tsc 7 快约 2 到 3 倍。

- 🦀 **项目定位**：ts-rust 是对 microsoft/TypeScript（原 typescript-go）原生编译器的直接 Rust 移植，保留 Go 的算法与行为，命令行、语言服务器和 API 与 tsc 一致。
- 📦 **安装方式**：通过 `npm install -D tsc-rs` 安装，再用 `npx tsc-rs -p tsconfig.json` 运行；npm 包名与 typescript 区分，另有各平台独立压缩包。
- 💸 **开发成本**：早期用 OpenAI 模型花费超 40 万美元 token 仅到约 84% 兼容；改用 Claude Opus 5.5 后 10 小时做出可用 v0，两周内约花费 2.4 万美元 API 费用。
- ⚡ **性能表现**：在 60 个开源项目上类型检查耗时约为 Go 版的 一半（几何平均）；六个真实应用中默认模式比 tsc 7 快 2.10 倍，`--fast` 模式快 2.90 倍。
- 🏁 **基准测试**：T3 Code 完整类型检查中，tsc-rs --fast 为 9.77 秒，tsc-rs 为 14.30 秒，tsc 7 为 42.55 秒，bun check 为 59.24 秒，tsc 6 为 191.00 秒。
- ✅ **兼容性**：全部 184,749 个移植的 Go 测试通过；在 120 个开源仓库上，命令行输出仅在与 Go 自身输出不稳定处有差异。
- 🎛️ **四个可选开关**：`--fast`、`GOPORT_FAST_STEAL=1`、`--checkers N`、`GOPORT_LAZY_MEMBERS=1`、`GOPORT_FAST_NEVER_ORDER=1` 可提升速度或降低内存，默认全部关闭。
- 🧩 **Effect 诊断内置**：集成 Effect 语言服务诊断（377xxx 代码），包含悬停、内联提示、快速修复、重构等编辑器功能，无需第二个编译器。
- ⚠️ **已知问题**：monorepo 中可能多报 TS6059；`tsc -b` 并行构建时输出读取顺序可能与 tsc 不同；长时间编辑内存增长略高于 tsc；`--version` 打印的是所移植的 TypeScript 版本。
- 🔧 **开发结构**：核心编译器在 `crates/ts_goport`，WASM 构建在 `crates/ts_wasm`，代码生成工具在 `tools/`，Windows 需 MSVC 工具链并以 LF 行尾克隆。
- 📜 **许可证**：MIT 协议，并保留所移植代码的 TypeScript（Apache-2.0）与部分 Go 标准库（BSD-3-Clause）许可与声明。

---

### [高级软件工程师，原生移动端，远程 - 美国 - Coinbase | Adam Wolf | 25条评论](https://www.linkedin.com/posts/adamawolf_senior-software-engineer-native-mobile-activity-7511201803389186048-JV6b)

**原文标题**: [Senior Software Engineer, Native Mobile, Remote - USA - Coinbase | Adam Wolf | 25 comments](https://www.linkedin.com/posts/adamawolf_senior-software-engineer-native-mobile-activity-7511201803389186048-JV6b)

Coinbase 的 Adam Wolf 宣布将消费者交易应用从 React Native 全面迁移到 Swift 和 Kotlin，核心原因是 AI 编码代理降低了双端构建成本，原生体验更优；团队正在招聘原生移动工程与移动 QA，并引发关于 KMP、Flutter、共享核心和发布周期的讨论。

- 🚀 Coinbase 消费者交易应用将完全原生化：从 React Native 迁移到 Swift 与 Kotlin。
- 🤖 关键推动力：AI 编码代理大幅降低“同一功能构建两次”的成本，使原生重写更可行。
- ⚡ 原生优势：启动更快、崩溃更少、首日接入新 iOS/Android 能力；对真实资金交易应用尤其重要。
- 🧑‍💻 移动工程师角色转变：减少样板代码和桥接维护，更多投入架构设计与用户体验，代理承担重活。
- 📣 招聘信息：Native Mobile 与 Mobile QA，职级从 Senior 到 Senior Staff，并附多个申请链接。
- 💬 评论争议：有人建议用 Kotlin/Compose Multiplatform 或 Flutter，以共享逻辑并保持原生体验。
- 🧭 历史视角：评论者认为当年选 RN 合理，如今原生优势回归；AI 降低双代码库成本，KMP 可进一步降低风险与工作量。
- 🧪 技术路线讨论：是否完全原生，还是用 Rust/KMP 共享核心、SwiftUI/Compose 做 UI；也涉及 SDUI 与 App Store 发布周期。
- 🛡️ 质量关注：AI 生成代码质量、静态分析、密钥扫描和架构规则需快速运行，以尽早发现问题。
- 📊 有人呼吁公开迁移中的 UX/技术性能对比基准，也有人表示会引用 Coinbase 与 Shopify 的原生趋势。

---

### [](https://crashunited.itch.io/klattsch/devlog/1580425/klattsch-engine-is-free-software-put-it-in-your-game)

**原文标题**: [klattsch engine is free software - put it in your game! - klattsch by Crash United](https://crashunited.itch.io/klattsch/devlog/1580425/klattsch-engine-is-free-software-put-it-in-your-game)

klattsch 是一个免费、MIT 许可的语音合成引擎，可通过 npm 包直接嵌入游戏，支持 WAV 烘焙、浏览器实时合成、Godot/Unity/原生/Rust 集成，并可用于程序化角色语音、动态文本与口型同步。

- 🎙️ klattsch 应用基于 MIT 许可的免费语音合成引擎，`klattsch` npm 包就是底层引擎，可直接把这种声音放进自己的游戏。
- 🧾 输入 ARPABET 音素，并加入音高、速度、颤音、呼吸等指令即可合成语音；音高可用音符（如 `bC4`）或频率。
- 🖥️ 无需写代码：CLI 示例 `npx klattsch "..." guard_halt.wav` 可生成低慢守卫说“halt, who goes there”的 WAV。
- 🧱 构建时烘焙：`klattsch/dialog-bake` 可读取 CSV 对话，输出 `out/<id>.wav`，适合 Unity、Unreal、GameMaker、Ren’Py 等音频导入流程。
- 🌐 Web 实时合成：通过 AudioWorklet 与 `compileString` 在浏览器实时发音，支持 Phaser、PixiJS、Vite、webpack 等。
- 🎮 Godot 集成：`klattsch/godot` 是编辑器插件和示例，可烘焙 `voice_lines.csv`，也支持 `JavaScriptBridge` 用于 Web 嵌入。
- 🎛️ klattsch 是合成器而非固定音效板：实时计算可控制音高、速度、呼吸、颤音、声道缩放，创造无限角色声线。
- 👥 程序化角色：`b95 r180` 像守卫，`b160 r240 s1.2` 像店主；随机参数可生成无限语音变化。
- 🗣️ 运行时生成句子：可用 `klattsch/pronounce` 处理程序化名字、动态输入，或映射音节做 Animalese 式咿呀声。
- 👄 口型同步：`compileString` 返回带时间戳的 schedule，可驱动嘴部动画；`dialog-bake --schedules` 可导出 JSON。
- ⏱️ 示例 countdown-choir：合唱团唱出剩余时间，随倒计时更惊慌，展示运行时改字符串、压缩时间、升调。
- ✍️ 应用可当编辑器：GUI 钢琴卷帘便于尝试和作曲，切文本模式复制音素字符串到代码，也可直接导出 WAV。
- 🧩 原生嵌入：引擎纯计算，可在 QuickJS/Jint 等嵌入式 JS 解释器运行 `compileString` 和 `renderToBuffer`，把 PCM 送入引擎音频 API。
- 🦀 Rust 移植：`klattsch-rs` 已在 crates.io；`FormantSynth::process` 实时安全，适合 Bevy、godot-rust、cpal。
- 📜 MIT 许可：声音可商用、免版税；若打包代码，需保留版权和许可证文本；不要求开源。
- 🙏 作者请求：若用于游戏，可在鸣谢写 “Speech synthesis by klattsch / Tony Gies”，并分享作品。
- 💰 获取：klattsch 应用在 itch.io 售价 $9.99 起；标签包括 Audio、chiptune、TTS、vocal-synth、retro 等。

---

### [Kiesel JavaScript 引擎](https://kiesel.dev/)

**原文标题**: [Kiesel JavaScript Engine](https://kiesel.dev/)

您尚未提供需要总结的具体文本内容，因此目前无法生成文章摘要。请补充文章、段落或文字内容后，我将按要点进行提炼。

- 📄 当前输入中未检测到可总结的文本内容。
- ✍️ 请粘贴或发送需要总结的文章、段落或文字。
- 🔍 收到内容后，我会提取关键信息并压缩为简洁要点。
- 🧾 输出将使用中文，并以“- + Emoji”的格式呈现。
- 🌟 摘要会保留核心观点、重要事实与关键结论。

---

### [](https://linus.dev/posts/kiesel-devlog-15/)

**原文标题**: [Kiesel Devlog #15: Release 0.4.0 — Linus Groh](https://linus.dev/posts/kiesel-devlog-15/)

Kiesel 发布 0.4.0，完成 Zig 0.17 升级，包含 2.5 个月内 64 次提交；新增多项 API、迭代器辅助方法、SerenityOS 等平台移植，并改进内联缓存，0.5.0 将重点提升解析器速度。

- 🚀 发布 Kiesel 0.4.0：完成 Zig 0.17 更新，跨 2.5 个月共 64 次提交。
- 🧰 新增 Kiesel.args 与 Kiesel.env：结合文件/标准输入 I/O，可实现简单 cat(1) 克隆。
- 🔁 迭代器辅助继续扩展：新实现 Iterator Join、Iterator Includes、Iterator Chunking。
- ⏳ 实现 Await Dictionary 提案：目前仍处于 Stage 3。
- 🌐 完成 SerenityOS 移植：融合 SerenityOS、Zig 与 Kiesel，逐步上游化 Zig 的 SerenityOS 目标支持。
- 🧱 上游化多项改动：包括 SerenityOS LibC/Kernel 修改与 Kiesel 包，交叉编译基于最小补丁的 Zig 标准库。
- 💾 其他平台进展：DOS 移植因 dos.zig 复苏而实现，OpenBSD/NetBSD 二进制已在 CI 中构建。
- 🧠 改进内联缓存：补齐多态属性访问（最多 4 个后转为 megamorphic）、计算属性访问、原型查找。
- 📈 IC 实现仅数百行：微基准测试中带来稳定 20–30% 加速。
- 👀 0.5.0 计划：解析器即将变快，敬请期待。

---

