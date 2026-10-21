### [推出 tsrs：TypeScript 到 Rust 的移植 | Cloudflare 博客](https://blog.cloudflare.com/typescript-rust-port/)

**原文标题**: [Introducing tsrs: a Port of TypeScript to Rust | Cloudflare Blog](https://blog.cloudflare.com/typescript-rust-port/)

Cloudflare 与 VoidZero 宣布推进 `tsrs`——TypeScript 编译器的 Rust 移植版，并与 TypeScript 团队紧密合作、在 Oxc 工具链中孵化。项目强调“不是分叉 TypeScript”，语言设计与方向仍由 TypeScript 团队掌控，目标是在不改变上游语义的前提下，让类型检查更快、更省内存，并更易在浏览器、Workers 等环境中运行。

- 🚀 **项目定位**：`tsrs` 是 TypeScript 的忠实 Rust 移植，不是 fork，TypeScript 团队继续负责语言设计与方向。
- ⚡ **性能提升**：在相同类型检查 worker 数量下，早期基准显示比 TypeScript 7.0 最高快 8 倍、内存占用少约 70%。
- 📉 **内存与配置**：默认根据机器类型自适应配置，使用更多内存但速度更快；TypeScript 7.1 beta 也比 7.0 最高快 2.5 倍，部分优化已回馈上游。
- 🧪 **试用方式**：可通过 npm 安装实验版本：`npm install tsrs`，然后运行 `npx tsrs`。
- 🦀 **选择 Rust 的原因**：Rust 与 WebAssembly 的内存模型更适合 Wasm，便于在 Cloudflare Workers、浏览器、嵌入式设备和 IoT 中高效运行完整开发工具链。
- 🔧 **维护方式**：将与 Theo Browne 合作合并 `tsc-rs` 与 `tsrs`，支持 LSP、content mappers 等 TypeScript 功能。
- 🤖 **同步上游**：借鉴 Vinext 的维护流程，用代理每日检查上游变更、生成兼容性矩阵并运行测试，尽量减少与上游 TypeScript 的行为差异。
- 🔁 **回馈社区**：发现性能优化会尝试贡献回 TypeScript Go 代码库；目标是在稳定版发布前把诊断输出顺序等差异降到最低。
- 🌱 **后续计划**：Cloudflare 已拥有 Vite、Rolldown、Oxlint、Oxfmt 等 Rust 工具，未来会探索 `tsrs` 与 Oxlint 类型感知规则等更深集成，并以健康开源项目方式维护。

---

### [获取失败](https://news.ycombinator.com/item?id=50167925)

**原文标题**: [Failed to retrieve](https://news.ycombinator.com/item?id=50167925)

无法总结：获取内容失败，状态码 419。

---

### [JavaScript 氧化编译器](https://oxc.rs/)

**原文标题**: [The JavaScript Oxidation Compiler](https://oxc.rs/)

Oxc 是使用 Rust 编写的高性能 JavaScript 工具集合；页面标题为“宣布支持 React Compiler”，正文重点展示覆盖 lint、格式化、解析、转换、模块解析与压缩的现代 JavaScript 工具链及其性能优势。

- 📰 页面标题为“宣布支持 React Compiler”，但正文主要介绍 Oxc 的高性能 JavaScript 工具生态。
- 🧰 Oxc 提供 Oxlint、Oxfmt、oxc-parser、oxc-transform、oxc-resolver、oxc-minify 等工具，覆盖现代 JavaScript 开发全链路。
- ⚡ Oxlint 是兼容 ESLint 的 linter，速度比 ESLint 快 50~100 倍，支持 800+ 规则、基于 tsgo 的类型感知检查及 ESLint JS 插件。
- 🎨 Oxfmt（Beta）是兼容 Prettier 的格式化器，比 Prettier 快 30 倍、比 Biome 快 3 倍，并支持 Tailwind 类名排序。
- 🧩 oxc-parser 比 SWC 快 3 倍，可解析 .js(x)/.ts(x)，通过全部 Test262 stage4 测试；基准为 26.3ms，对比 SWC 84.1ms、Biome 130.1ms。
- 🔄 oxc-transform 支持 TypeScript/JSX 语法降级至 ES2015、Isolated Declarations DTS 输出、React Fast Refresh、styled-components 等。
- 📦 oxc-resolver 提供 Node.js 兼容的 CJS/ESM 模块解析，行为对齐 enhanced-resolve，速度提升 28 倍且可高度定制。
- 🗜️ oxc-minify（Alpha）支持死代码消除、语法缩短、空白移除和变量名混淆等压缩优化。
- 🌍 Oxc 免费开源，由赞助商支持，并提供文档、Playground、社区与完整生态入口。

---

### [TypeScript 的 Webhooks：发送和验证 Webhooks · Svix](https://www.svix.com/typescript/?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=javascript-weekly)

**原文标题**: [Webhooks for TypeScript: send and verify webhooks · Svix](https://www.svix.com/typescript/?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=javascript-weekly)

Svix 为 TypeScript 开发者提供一个端到端类型安全的 npm 包，让 API 快速发送 Webhook，并内置重试、签名、投递日志和客户门户等生产级能力，同时可用同一库一键验证入站 Webhook。

- 📦 通过 `npm install svix` 即可使用，类型覆盖请求与响应，编辑器可提前发现错误的事件负载。
- 🚀 用少量代码向客户注册的所有端点发送事件，例如 `invoice.paid` 通知。
- 🔐 每条消息按 Standard Webhooks 规范签名，并带时间戳以防止重放攻击。
- 🔁 失败投递会以指数退避重试超过一天，持续失败的端点会自动禁用。
- 🧾 提供可搜索的投递日志，记录每次尝试、响应和状态码，便于排查丢失的 Webhook。
- 🖥️ 提供白标客户门户，客户可自行添加端点、选择事件类型并调试投递。
- ♻️ 支持一键或通过 API 重发单条消息，并恢复某次故障以来所有失败投递。
- ✅ 接收 Webhook 时，传入原始请求体和请求头即可验证签名与时间戳；必须在解析 JSON 前验证原始字节。
- 🧩 验证适用于 Next.js route handlers、Express、Fastify、Hono 等能提供原始请求体和请求头的框架，也支持普通 JavaScript。
- 📈 `svix` 包过去一个月下载量达 2800 万；Resend 从 200 用户增长到 15 万用户，每年处理 2 亿+ Webhook。
- 🎁 成立三年内且融资不超过 700 万美元的初创公司可获 1.2 万美元免费额度；当前 YC 批次公司可获 5 万美元。

---

### [谢谢你，Deno | vlt /vōlt/](https://www.vlt.io/blog/competition-keeps-javascript-moving)

**原文标题**: [Thank you, Deno | vlt /vōlt/](https://www.vlt.io/blog/competition-keeps-javascript-moving)

Deno 团队将加入 Cloudflare，Deno 运行时将在未来一年逐步收缩，JSR 继续运行，团队将把 Deno 的 celld 合并进 workerd。文章认为 Deno 虽未在 production 中达到 critical mass，Node 仍占主导，但它对 Node、包管理器、注册表和标准化的竞争压力，实实在在推动了 JavaScript 生态进步；竞争带来的紧迫感让好想法最终被用户享受到。

- 🏁 Deno 团队加入 Cloudflare，运行时逐步收尾，JSR 保留，celld 将并入 workerd。
- ⚔️ Deno 未赢得生产市场，但作为挑战者迫使 Node 加速改进，体现竞争对健康生态的重要性。
- 🧭 Deno 起初主张默认拒绝权限、TypeScript 一等支持、Web 标准 API、仅 ESM、单可执行文件，并拒绝 npm、package.json、node_modules，改用 URL 依赖。
- 🔁 URL 依赖因缺少完整性哈希和版本记录而受质疑，Deno 随后通过 deps.ts、lock.json、import maps 和推荐 registry 逐步回退。
- 🥟 Bun 以速度、npm 兼容和 Node 替代方案施压后，Deno 推出 npm: 说明符并最终在 Deno 2 实现完整 Node/npm 兼容。
- 🧩 Node 吸收了大量竞争想法：fetch、WebSocket、Web Streams、Web Crypto、稳定测试运行器、--watch、--env-file、权限模型、类型剥离、node:sqlite、require(esm) 等。
- 🌐 WinterCG 因多运行时共同 API 问题成立，后发展为 Ecma TC55，标准化工作也受益于竞争压力。
- 📦 包管理器和注册表持续互鉴：Yarn 推动 lockfile/workspaces/离线缓存，pnpm 优化 node_modules，Bun 提升安装速度，Deno 强调依赖源码可读；install scripts 默认关闭从 pnpm/Bun/vlt 走向 npm 12。
- 🧱 JSR 以发布 TypeScript 源码、要求 ESM、从代码生成文档等不同选择运行，并因成本低、API 有文档且 Cloudflare 有理由保留而存续。
- 🔀 两大独立、风险投资支持的 JavaScript 运行时进入主营业务不同的公司；未来关注是否出现 Deno 社区 fork，以及 celld 并入 workerd 后能否提供自托管 Workers/Durable Objects 的新选择。
- 🛡️ JavaScript 在引擎、运行时、包管理器等层仍有冗余保险；整合发生时其他层可支撑，虽然“JavaScript 疲劳”持续，但好想法通常胜出，最终用户受益。
- 🙏 文章最后感谢 Ryan、Bert、Bartek 及 Deno 团队过去和现在的贡献。

---

### [Deno 加入 Cloudflare | Deno](https://deno.com/blog/cloudflare)

**原文标题**: [Deno is joining Cloudflare | Deno](https://deno.com/blog/cloudflare)

Deno 团队将整体加入 Cloudflare，未来开发重心转向基于 Cloudflare Workers 与 Durable Objects 的共享平台，而非继续维护独立运行时和托管服务。

- 🤝 Deno 团队整体加入 Cloudflare，以推进更简单的服务器软件开发与部署模式。
- 🧭 发展路径从 Deno 运行时、Deno Deploy 延伸到 celld；celld 基于 Workers 编程模型，让分布式应用从设计之初就具备扩展能力。
- ☁️ 在 Cloudflare，Deno 团队将与 Workers 和 Durable Objects 团队合作，目标是让该编程模型成为构建服务器的默认方式，无论运行在 Cloudflare 网络还是自有基础设施上。
- 🛠️ 未来开发将集中到共享平台，不再继续开发独立的 Deno 运行时和托管服务。
- ⏳ Deno 运行时将继续支持一年，期间每月发布包含缺陷修复和安全更新的版本；一年后结束开发，但保持开源，欢迎社区继续推进。
- 🌐 Deno Deploy 将继续运营六个月后关闭，并为付费客户迁移到 Cloudflare Workers 提供支持。
- 📦 JSR 将继续运营，其基础设施迁移到 Cloudflare。
- ⚙️ 继续支持 rusty_v8，并推动其集成到 workerd。
- 🤖 在 AI 场景下，Durable Objects 适合构建 agent harness，提供低成本无服务器执行、持久状态、WebSockets 和高层 JavaScript 接口；celld 也因此聚焦 Durable Objects。
- ✉️ 若要在自有基础设施上大规模构建 agents，可通过 ry@cloudflare.com 联系 Ryan Dahl。

---

### [Next.js 上游漏洞安全更新 | Next.js](https://nextjs.org/blog/nextjs-security-update-october-14-2026)

**原文标题**: [Next.js Security Update for Upstream Vulnerabilities | Next.js](https://nextjs.org/blog/nextjs-security-update-october-14-2026)

Next.js 于 2026 年 10 月 14 日发布安全更新，修复与上游依赖相关的三个漏洞，涉及 v16.4.1（Active LTS）和 v15.5.28（Maintenance LTS），建议用户立即升级。

- 🚨 **更新版本**：v16.4.1 和 v15.5.28 已修复问题；可运行 `npm install next@16.4.1` 或 `npm install next@15.5.28` 升级。
- ⚠️ **严重漏洞：use cache 远程代码执行**：App Router 配合 Cache Components 时，若 `use cache` 函数返回多个 typed arrays，可能导致未认证远程代码执行；无已知缓解措施，应立即升级。
- 🖼️ **严重漏洞：SVG 图像优化 RCE**：Image Optimization API 使用 SVG 时，在 glibc 系 Linux 上可能因上游库内存漏洞导致远程代码执行；临时缓解需确保 `sharp` 为 0.35.5 或更高，升级 Next.js 会自动带入修复版本。
- 🛑 **高危漏洞：Server Actions 拒绝服务**：App Router 中使用至少一个 Server Action 的应用，可能遭构造请求导致 CPU 过载并阻断后续请求；Pages Router 或未使用 Server Actions 的应用不受影响。
- 🛡️ **安全计划**：Next.js 通过 Vercel Open Source Bug Bounty 与安全研究人员合作；相关问题可联系 `security@vercel.com`。

---

### [React 服务端组件中的未认证远程代码执行 · 安全公告 · react/react · GitHub](https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3)

**原文标题**: [Unauthenticated Remote Code Execution in React Server Components · Advisory · react/react · GitHub](https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3)

React 安全公告 GHSA-xqc2-xf4c-x3h3 披露 React Server Components 存在未认证远程代码执行漏洞，严重级别为 Critical（CVSS v4 9.5），建议受影响用户立即升级修复版本。
- 🚨 漏洞可导致远程代码执行，攻击者无需认证即可利用。
- 📦 受影响 npm 包包括 `react-server-dom-webpack`、`react-server-dom-parcel`、`react-server-dom-turbopack`。
- 🔢 受影响版本为 19.0.0–19.0.8、19.1.0–19.1.9、19.2.0–19.2.8 和 19.3.0。
- ✅ 修复版本为 19.0.9、19.1.10、19.2.9、19.3.1，建议立即升级。
- 🐞 漏洞仅在极罕见场景下触发：响应传输多个 typed arrays 且包含攻击者可控值。
- 🛡️ 如果 React 代码不使用服务器端，或未使用支持 React Server Components 的框架、打包器或插件，则不受影响。
- 📊 CVSS v4 评分为 9.5，攻击向量为网络、复杂度低、无需权限、无需用户交互，机密性、完整性和可用性影响均为高。
- 📅 公告发布于 2026 年 10 月 14 日，发布者为 mattcarrollcode，发现者为 evolutionstorm。
- 🧾 暂无已知 CVE 和 CWE。

---

### [`](https://hash-sec.com/blog/the-use-cache-rce-how-a-typed-array-bug-in-nextjs-became-remote-code-execution)

**原文标题**: [The `use cache` RCE: how a typed-array bug in Next.js became remote code execution | Hash Security](https://hash-sec.com/blog/the-use-cache-rce-how-a-typed-array-bug-in-nextjs-became-remote-code-execution)

2026年10月，Vercel与Meta披露Next.js `use cache`功能中的严重漏洞（CVSS 4.0评分9.5），特定条件下未认证攻击者可实现远程代码执行；根因在React Flight协议处理类型化数组时的帧定界失步，而非应用代码本身。文章详解三个缺陷如何组合成利用链，并给出修复、检测与缓解建议。

- 🚨 漏洞涉及Next.js `use cache`与React Server Components的Flight协议，公告编号为GHSA-673q-mjm6-r5xr和GHSA-xqc2-xf4c-x3h3。
- 🧩 根因由三个问题叠加：类型化数组帧定界失步、缺少对`then`属性的防护、流ID与分块ID命名空间冲突。
- ⚙️ 触发条件是`use cache`函数返回多个共享同一`ArrayBuffer`的大类型化数组视图，并包含一个攻击者可控值。
- 💥 写入第一个视图会转移并分离共享缓冲区，第二个视图长度变为0但头部仍声明原长度，解码器因此越界读取到攻击者数据。
- 🎯 攻击者可在越界区域伪造Flight行，把`$h<id>`服务器引用赋给`then`，使对象成为thenable，`await`时调用真实Server Action。
- 🔑 利用需要有效的42位十六进制Server Action ID，但这些ID通常已暴露在客户端JS包和网络响应中，并非秘密。
- 🧪 实际影响取决于目标应用暴露的Server Action与缓存函数：可能达到未认证RCE，至少也可造成远程拒绝服务。
- 🛠️ 修复在React 19.3.1与Next.js 16.4.1：复制部分视图、拒绝已分离缓冲区，并阻止`then`键绑定服务器引用。
- 📦 受影响版本包括Next.js 16.0.0至16.4.0，以及多个`react-server-dom-*` 19.x版本；应升级至对应修复版本。
- 🔍 检测重点：使用`use cache`或Cache Components的应用、返回多个共享缓冲区二进制值的缓存函数，以及异常出现`Connection closed.`或HTTP 500的请求。
- 🛡️ 无法立即升级时，避免从`use cache`返回共享同一`ArrayBuffer`的多个类型化数组，可用`view.slice()`复制；出现流损坏的实例应按可能失陷处理。
- 📌 核心教训：线协议是安全边界，长度字段不可盲信；“转移而非复制”的性能优化会带来尖角；一个缺失的`if (key === "then")`防护即可把数据错解析升级为代码执行。
- 🔗 POC：https://github.com/hashseclb/nextjs-use-cache-rce-2026

---

### [Node.js — 2026年10月21日（星期三）安全版本发布](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

**原文标题**: [Node.js — Wednesday, October 21, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

Node.js 项目计划于 2026 年 10 月 21 日（周三）或之后不久发布 26.x、24.x、22.x 版本线的安全版本，以修复安全漏洞；这些版本线中修复的最高严重性问题均为 HIGH。已停止维护（End-of-Life）的版本在安全发布时始终会受影响，因此建议使用发布计划中的最新版本。

- 🔒 **发布目的**：发布 26.x、24.x、22.x 新版本以应对安全漏洞。
- 📅 **发布时间**：2026 年 10 月 21 日（周三）或之后不久。
- ⚠️ **严重性**：26.x、24.x、22.x 三个版本线修复的最高严重性问题均为 HIGH。
- 🛑 **EOL 版本风险**：End-of-Life 版本在安全发布发生时始终会受影响，应使用最新受支持版本。
- 🏢 **商业支持**：超过 Maintenance LTS 阶段的版本可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获得商业支持。
- 📜 **安全政策**：当前 Node.js 安全政策见 https://nodejs.org/en/security/。
- 🐞 **漏洞报告**：按 https://github.com/nodejs/node/blob/master/SECURITY.md 中的流程报告漏洞。
- 📬 **更新订阅**：可订阅 nodejs-sec 邮件列表，获取安全漏洞及相关安全版本更新。

---

### [](https://x.com/jarredsumner/status/2104739495895781679)

**原文标题**: [Jarred Sumner on X: "An early preview of experimental Bun + JSC with ahead-of-time compilation

For Claude Code's CLI: 24% faster startup, 48% lower memory, 46% lower CPU, and nearly 2x larger binary size" / X](https://x.com/jarredsumner/status/2104739495895781679)

Jarred Sumner 在 X 上预览了 Bun + JSC 的提前编译（AOT）实验性版本，并以 Claude Code 的 CLI 为例展示性能收益；主要代价是二进制体积明显增大。

- 🧪 这是 Bun + JSC 提前编译（AOT）的实验性早期预览。
- 🚀 在 Claude Code 的 CLI 上，启动速度提升 24%。
- 🧠 内存占用降低 48%。
- ⚙️ CPU 使用率降低 46%。
- 📦 二进制文件体积接近原来的 2 倍。
- 🐦 该信息由 Jarred Sumner 于 2026 年 9 月 29 日在 X 上发布。

---

### [](https://github.com/oven-sh/bun/pull/45631)

**原文标题**: [Compile TypeScript to machine code ahead of time: `bun build --compile --aot` by Jarred-Sumner · Pull Request #45631 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/45631)

Bun 仓库的草案 PR #45631 由 Jarred-Sumner 发起，包含 164 个提交、目标分支为 main，为 `bun build --compile --aot`（简称 `bun compile`）引入提前编译：构建时将 TypeScript/JavaScript 编译为机器码，生成的可执行文件无 JIT、无字节码，也不会向系统申请可执行内存。该功能仍属实验性草案，引擎部分依赖 `oven-sh/WebKit#757`。

- 🚀 核心命令：`bun build --compile --aot` / `bun compile` 可在构建阶段生成 AOT 可执行文件，并提供 `bun run --aot`、`bun test --aot` 用于单次运行验证。
- ⚡ 性能亮点：TypeScript 6 自举编译器在 `effect` 仓库上，一线程 AOT 为 3.83s wall / 5.3s CPU / 928MB，快于 TypeScript 7 Go 版一线程的 5.19s / 6.1s / 951MB；但 Go 版默认多线程仍赢得墙钟时间。
- 🧠 设计理念：浏览器 JIT 假设代码不可信、需即时启动并反复猜测类型；服务器/CLI 在构建时已掌握源码和类型，AOT 可保留类型信息，避免每次启动重新推断。
- 🧱 类型收益：`Vec` 等对象可用固定布局，字段读取变为固定偏移加载，数字不装箱，对象引用为 32 位，`int32` 字段可由构建期证明且运行时不检查。
- 🧩 仍是 JavaScript：没有新语言或新语法，npm 包、ESM/CommonJS、动态 `import()`、顶层 await、N-API、Workers 等可用；`eval`、`new Function`、代理、getter/setter 等动态特性在解释器中运行。
- 🧪 兼容性测试：测试覆盖 Next、Nuxt、Astro、SvelteKit、Angular、React Router、Express、Fastify、Hono、Elysia、NestJS、Drizzle、TypeORM、sharp、bcrypt 等，约 3,750 个小程序在 AOT 与普通 Bun 下输出需一致。
- ⚠️ 五项破坏性变更：类型不匹配在进入类型化代码时抛 `TypeError`；`as number/string/boolean` 会真正转换；内置对象不可变；`T[]` 表示普通数组，getter 元素会抛错；禁用 `with`，直接 `eval` 不能声明调用方变量。
- 🛡️ 安全模型：AOT 可执行文件不含 JIT，所有机器码位于只读可执行段，进程不申请匿名可执行内存；CI 在 seccomp、macOS hardened runtime、Windows ACG 等禁止动态代码的环境下验证可运行。
- 🔧 可选加固：提供 `--aot-deny=interpreted`、`--disallow-code-generation-from-strings` 等开关，可禁止 `eval`/`new Function`/`node:vm`，把可执行代码限制为构建时文件内容。
- 🧭 迁移路径：先用 `bun --aot-audit` / `bun test --aot-audit` 记录差异，再用 `bun check --aot` 报告不可行代码，随后用 `--aot-type-errors=log` 观察类型错误，最后正式启用。
- 📦 体积优化：`--compile-trim-runtime` / `--compile --trim` 可剔除 CLI、包管理器、测试运行器、类型检查器、linter、formatter 及 AOT 下的 JIT 等；小型 `Bun.serve` 服务在 macOS arm64 上可从 105MB 降至 20MB。
- 🖥️ 服务器表现：八个小型服务器测试中 RSS 下降 18%–39%，启动到首响应更快；峰值吞吐部分下降，最新静态调用图内联缓存改进使 Express、Fastify、Effect 每请求周期减少 7%–8%。
- 🏁 与 Go/Rust 对比：严格 TypeScript 写的 2,000 行 issue tracker 中，Bun AOT 为 4,420 req/s，落后 Go 17%、约为 Rust 一半；但比 Bun 1.4.3 提升 48% 吞吐、降低约三分之一 CPU 和 36% 内存。
- 🛠️ 实现路径：`src/sema` 做全程序类型检查，`src/aot` 将语法树和类型转为 SSA 形式类型化 IR，JavaScriptCore 优化并降为 B3，最终写出机器码与只读数据镜像嵌入可执行文件。
- 🚧 尚未就绪：Express/Fastify/Effect 仍比 JIT 慢；运行时生成代码、WebAssembly 走解释器；无断点、宏、`JSCallback`、交叉编译；Windows 的 trim 未充分测试；最近一次完整 CI 有 41 个失败测试文件但无崩溃。
- 💬 社区反馈：评论多为 LGTM 和鼓励，也有少量 nits；部分评论调侃 3,000+ 文件修改、Claude 参与开发/审查，以及“部署它”等。

---

### [Node.js — Node.js 26.12.0（当前版本）](https://nodejs.org/en/blog/release/v26.12.0)

**原文标题**: [Node.js — Node.js 26.12.0 (Current)](https://nodejs.org/en/blog/release/v26.12.0)

Node.js 26.12.0（Current）于 2026-10-14 发布，由 Richard Lau 发布，包含两项 SEMVER-MINOR 变更，以及大量修复、性能优化、文档更新和依赖升级。

- 📦 **版本信息**：Node.js 26.12.0 属于 Current 版本，发布说明列出了 Windows、macOS、Linux、AIX、ARM64 等平台的安装包、二进制文件和源码包。
- ⚠️ **重要变更**：`doc,lib,src` 在缺少 WebAssembly 或 RX 支持时抛出错误（SEMVER-MINOR，#66533）。
- 🌐 **HTTP 新功能**：新增 `websocketMask()` 和 `websocketUnmask()`（SEMVER-MINOR，#66335）。
- 🔐 **加密模块**：移除多项密钥导出、验证、KEM、RSA-OAEP 锁定，跳过 secret key mutex 分配，按 Environment 保留根证书库，并移除部分 Web Crypto 警告。
- 🧵 **Stream/Iter**：大量修复与优化，包括新增 `pipeToSync()` 的 `failOnIncompleteClose` 选项、`dump()`/`dumpSync()`，降低每块开销，并改进 `shareSync()`、`from()`、`pull()` 等行为。
- 🧪 **Test Runner**：支持在测试套件中重跑失败的 todo 测试，`--test-isolation=none` 可报告加载错误，`t.assert` 增加 mock 调用断言。
- 🛠️ **构建与依赖**：支持 Python 3.15，启用 no-ICU/system-ICU 的 temporal 支持，并更新 googletest、acorn、SQLite、V8、simdjson 等依赖。
- 🧩 **模块与权限**：多数 ES modules 改为同步加载，修复 package map 下 `require` imports 的问题；权限模型改进显式文件系统授权与 `--allow-fs-vfs`；配置文件标记为稳定；VFS 新增 ComposableProvider。
- 🗄️ **SQLite/QUIC/FS/HTTP2**：SQLite 增加参数校验、持久化 defensive 模式、超大字符串抛错；QUIC 修复流和会话错误处理；FileHandle 增加锁定与写入序列化；HTTP2 提升 `getHeaders` 性能。
- 📚 **文档与发布文件**：补充权限模型、Test Runner 诊断通道、stream/iter 行为、HTTP keep-alive 等文档；发布文件附带 SHA256 校验和及 PGP 签名。

---

### [Node.js — Node.js 24.22.0（长期支持版）](https://nodejs.org/en/blog/release/v24.22.0)

**原文标题**: [Node.js — Node.js 24.22.0 (LTS)](https://nodejs.org/en/blog/release/v24.22.0)

Node.js 24.22.0（LTS，代号 Krypton）于 2026-10-14 发布，由 Richard Lau 等准备，包含多项 semver-minor 新 API，以及 crypto、网络、流、SQLite、TLS/QUIC、构建与测试方面的大量修复和优化。该版本提供 Windows、macOS、Linux、AIX 等多平台安装包、二进制、源码及 SHA256 校验和。

- 🚀 版本定位：Node.js 24.22.0 LTS（Krypton），发布于 2026-10-14。
- 🔐 crypto 新能力：新增 crypto.parsePKCS12()、通用 MAC API，支持从 OpenSSL providers 发现 cipher/hash，并启用 SIV/GCM-SIV 模式。
- 🌐 网络与线程：net 支持将 net.BoundSocket 发送到线程和子进程。
- 📊 性能观测：perf_hooks 新增 SlidingWindowHistogram、Histogram meanCI、qrde 分析及 CBOR 导入导出。
- 🗄️ SQLite 增强：StatementSync 新增 close() 和 Symbol.dispose()。
- 🧰 工具函数：util 新增 markPromiseAsHandled、throttle 和 debounce。
- 🛠️ 稳定性修复：覆盖 crypto、fs、http/http2、stream、sqlite、tls、quic、inspector、src 等模块的大量缺陷修复与优化。
- 📦 依赖更新：升级 npm 至 11.19.1，并更新 V8、zlib、simdjson、googletest 等依赖。
- 📝 文档与工程：补充和修正文档，改进测试、基准、构建、CI 工具及类型声明。
- 💾 发布产物：提供多平台安装包、二进制、源码下载及 SHA256 校验和；页面还列出下一版本 Node.js 26.12.0 (Current)。

---

### [Astro 7.4 | Astro](https://astro.build/blog/astro-740/)

**原文标题**: [Astro 7.4 | Astro](https://astro.build/blog/astro-740/)

Astro 7.4 于 2026 年 10 月 15 日发布，核心更新包括新增 `astro build --timings` 构建耗时分析、构建与运行时图像服务分离、自定义入口点的 `notFound()` 处理器、字体配置警告、Node.js 最低版本提升，以及并行预渲染和自定义重定向页两项实验功能。

- ⏱️ `astro build --timings` 可展示构建各阶段、Vite 插件、Markdown 处理、页面渲染、图片和集成耗时，帮助快速定位性能瓶颈。
- 🖼️ `image.service` 支持分别配置 `build` 和 `runtime` 服务，预渲染页面可用本地 Sharp，按需页面可用图像 CDN，单一服务配置仍兼容。
- 🚫 `astro/fetch` 和 `astro/hono` 新增 `notFound()`，在自行组合处理器时可渲染自定义 404 页面；`astro()` 已内置该行为。
- 🔤 字体提供者可实现 `getFontProperties()`，Astro 会警告配置中无法提供的字重、样式、子集或格式；该回调在 Astro 8 中将变为必需。
- 🟢 Astro 及官方集成的最低 Node.js 版本提升至 22.22.0，升级 Astro 前需先升级 Node.js。
- 🧵 实验性 `experimental.parallelPrerender` 使用 Node.js worker 线程并行渲染静态页面，默认使用除一个外的所有 CPU 核心，并可通过 `workers` 调整。
- 🔁 实验性 `experimental.redirectPage` 允许通过 `src/pages/3xx.astro` 自定义静态构建重定向页，接收 `from`、`to`、`status`、`delay` 属性。
- 🧩 集成和 Vite 插件现在可控制构建输出目录，Vite 各环境解析后的 `outDir` 成为客户端、服务端和预渲染输出的依据。
- ⬆️ 可使用 `@astrojs/upgrade` 自动升级，或用 npm/pnpm/yarn 手动升级；`@astrojs/cloudflare` 和 `@astrojs/markdoc` 需同步升级到兼容版本。
- 🙌 社区可通过 Discord、GitHub、Bluesky、Twitter 和 Mastodon 反馈问题与建议。

---

### [](https://reactrouter.com/changelog#v850)

**原文标题**: [CHANGELOG.md  | React Router](https://reactrouter.com/changelog#v850)

该页面是 React Router 官方发布说明与变更日志索引，覆盖从 v7.0.0 到 v8.5.0 的所有版本，重点记录 v8 系列的重大基线调整、未来标志转正、路由与数据加载优化、RSC 实验能力、安全修复及大量稳定性改进。

- 📚 **文档范围**：列出 v7.0.0 起的版本发布记录；v6.x 及更早版本需查看对应分支或 GitHub Releases。
- 🚀 **v8.5.0 核心变化**：弃用 React Router 自身的视图过渡 API，推荐 React 19.3+ 的 `<ViewTransition>`；新增不稳定 API-only 模式、自定义 fetch/请求元数据、应用控制路由发现。
- 🧪 **v8.5.0 修复与实验**：修复 RSC 下 `<Await>` 服务端渲染、`HydrateFallback`、`matchPath`、fetcher 重置后重新验证等问题；新增 `unstable_fetch`、`unstable_useRouteDiscovery` 等能力。
- ⚡ **v8.4.0 性能优化**：内部 router context 更细粒度，减少无关路由组件重渲染；实验性路由匹配器基于 `@remix-run/route-pattern`，大规模路由下显著提速。
- 🧩 **v8.3.0 RSC 与编码**：更新 RSC 自定义入口、客户端版本、SRI 与 CSP nonce 支持；`href`/`generatePath` 按 RFC 3986 编码路径参数；支持 TypeScript 7。
- 🌐 **v8.2.0 服务端入口**：非 Node 运行时默认使用 Web Streams 服务端入口；Node 应用可通过 `unstable_enableNodeReadableStream` 选择加入；修复动态参数、路由排序和导航阻塞状态。
- 🛠️ **v8.1.0 工具与可观测性**：`create-react-router` 可安装官方 Agent Skill；Instrumentation 结果增加 URL、路由 pattern、params、HTTP 状态码等元数据。
- 🎯 **v8.0.0 重大版本**：最低要求 Node 22.22+、React 19.2.7+、Vite 7+；转为 ESM-only 与 ES2022；多个 v8 future flags 成为默认行为。
- 🧹 **v8.0.0 移除项**：删除 `react-router-dom`、`meta` 的 `data` 字段、Cloudflare 开发代理、`useRequestContextDomainName`；预渲染改用 Vite preview 流程。
- 🔐 **v7 安全修复**：多个版本包含 CSRF、开放重定向 XSS、`ScrollRestoration` XSS、Host/X-Forwarded-Host 处理、文件会话访问等安全修复。
- 🧪 **v7 稳定化进程**：逐步稳定 middleware/context、`fetcher.reset()`、`dataStrategy`、`onError`、`vite preview`、`splitRouteModules`、`viteEnvironmentApi` 等 API。
- 🗺️ **v7 功能演进**：引入 URL masking、pass-through requests、`route.lazy` 对象 API、类型安全 `href`、SPA fallback、routeDiscovery 配置、RSC Data/Framework Mode 实验支持。
- 📦 **v7.0.0 基础重构**：合并 Remix 相关包到 `react-router`，移除 `json`、`defer` 等旧 API，采用 Vite 编译器，增强类型安全与预渲染配置。

---

### [](https://github.com/chenglou/pretext/releases/tag/v1.0.0)

**原文标题**: [Release 1.0.0 · chenglou/pretext · GitHub](https://github.com/chenglou/pretext/releases/tag/v1.0.0)

Pretext v1.0.0 正式发布，核心改进是让换行行为更贴近 Chrome、Safari 和 Firefox 的真实表现，同时提升布局与准备性能；但包体积明显增大，并包含多项需要旧版本应用适配的破坏性变更。

- 🚀 **版本发布**：chenglou 发布 Pretext v1.0.0，作为当前最新版本。
- ✨ **换行兼容性提升**：在 Chrome、Safari 和 Firefox 中，Pretext 改用对应浏览器换行器的移植版本及其数据，在更多场景下按浏览器的方式断行。
- 📐 **富文本布局优化**：rich inline 会将条目作为一个段落进行布局，类似浏览器对段落内 span 的处理方式。
- ⚡ **性能提升**：在新宽度下调用 `layout()` 比 0.0.9 快 3 至 6 倍；对已测量文本调用 `prepare()` 快 1.1 至 13 倍。
- ⏱️ **加载成本略增**：库加载时间在 Chrome 增加约 0.4 ms，Safari 增加约 0.7 ms，Firefox 增加约 1.1 ms。
- 📦 **包体积增大**：主入口约 40 KB gzip，从 16 KB 增加；`@chenglou/pretext/rich-inline` 约 44 KB gzip，从 16 KB 增加。
- 🔧 **API 破坏性变更**：`layoutNextLine()` 和 `layoutNextLineRange()` 现在先接收宽度再接收光标，需要交换第二、第三个参数。
- 🧭 **富文本光标读取变更**：读取 rich-inline 光标位置时，应改用片段的 `sourceStart` 和 `sourceEnd`。
- 🗑️ **字段移除**：`segLevels` 已移除；`prepareWithSegments()` 句柄仅保留 `segments`、`kinds` 和 `widths` 等字段。
- ⚠️ **字体参数更严格**：传入 Canvas 会忽略的 `font` 字符串（如空字符串）现在会抛出 `RangeError`。
- ♻️ **旧句柄需重建**：0.0.9 创建的句柄需要重新准备文本。
- 📄 **迁移参考**：`CHANGELOG.md` 记录了全部变更及替代做法。

---

### [React Native 0.88 - 基于 Web 的事件分发、可变字体、SceneDelegate，无破坏性变更 · React Native](https://reactnative.dev/blog/2026/10/19/react-native-0.88)

**原文标题**: [React Native 0.88 - Web-Based Event Dispatching, Variable Fonts, SceneDelegate, no breaking changes · React Native](https://reactnative.dev/blog/2026/10/19/react-native-0.88)

React Native 0.88 正式发布，核心更新包括默认启用基于 Web 的事件派发、Text 与 TextInput 支持可变字体、iOS 增加 SceneDelegate 生命周期支持，并升级至 React 19.3.0 和 Metro 0.87；这是连续第三个没有用户侧破坏性变更的版本，升级预计较为平滑。

- 🚀 **版本亮点**：默认 Web 事件派发、可变字体、SceneDelegate、Java TurboModules ArrayBuffer、实验性 Swift Package Manager 支持。
- 🌐 **Web 事件派发**：事件改用 W3C EventTarget API，支持捕获、冒泡、`stopPropagation()` 与 `preventDefault()`；应用侧事件属性、合成事件对象和执行顺序保持不变。
- 🧪 **命令式事件 API**：Canary 版本在原生 ref 上提供 `addEventListener`、`removeEventListener` 和 `dispatchEvent`，用于收集早期反馈。
- 🔤 **可变字体**：`fontVariationSettings` 在 Android/iOS 的 `<Text>` 和 `<TextInput>` 上可用，支持对象形式和 CSS 字符串形式。
- 📦 **Java TurboModules**：可直接接收和返回 JavaScript `ArrayBuffer`，减少二进制数据编码；同步方法借用内存仅在调用返回前有效，需保留时应复制。
- 📱 **iOS SceneDelegate**：为适配 iOS 27 SDK 的 UIScene 生命周期提供增量支持，仍兼容 AppDelegate；当前仅支持单场景，需迁移入口、转发 URL/用户活动回调并配置 `Info.plist`。
- 🧰 **Swift Package Manager**：仍为实验性、可选启用；0.88 改进工具链与构建稳定性，计划 0.89 默认启用并保留 CocoaPods 退出选项，后续版本再移除 CocoaPods。
- ⚠️ **弃用项**：`InitializeCore` 改用 `react-native/setup-env`；带 `experimental_` 前缀的背景样式改为无前缀名称；`InputAccessoryView`、`ReactFragment.fabricEnabled`、部分 `ReactImageManager` `String?` 重载被弃用。
- 🧩 **其他改进**：React 19.3.0、Metro 0.87、Hermes 更新；RTL 文本对齐、FileReader/Blob、Image、ScrollView、渲染器等多项修复；Android 默认 User-Agent 加入应用名和版本。
- 🛠️ **开发者工具**：React Native DevTools 默认支持 `Page.captureScreenshot` 截图；Network 面板的 WebSocket 检查在 Canary 频道提供。
- 👏 **贡献与升级**：0.88 包含 91 位贡献者的 568 个提交；0.88 为最新稳定版，0.85.x 不再支持，建议使用 Upgrade Helper 升级，Expo 项目将通过 Expo SDK 58 获得支持。

---

### [Elysia 2 RC - 欢迎再来 - Elysia 博客](https://next.elysiajs.com/blog/elysia-20-rc/)

**原文标题**: [Elysia 2 RC - またおいで - Elysia blog](https://next.elysiajs.com/blog/elysia-20-rc/)

Elysia 2 RC（代号“DayDream”，本次版本名为《またおいで》）于 2026 年 10 月 19 日发布。此次基于一年重写，重点从单纯吞吐转向内存、启动效率、类型推断与稳定性；官方称其在 Bun 上仍是最快框架，在 Node.js 上接近 Fastify，并推荐新项目使用 RC、旧项目通过 codemod 迁移。

- 🚀 **发布定位**：Elysia 2 RC 是重要基础性升级，名称取自 South& 的《またおいで》，建议先阅读 beta 发布说明。
- 🧠 **内存优化**：重写核心并研究 JSC/V8 内存结构，使每条路由占用更少内存；`set.headers`、`status`、响应 schema 和 guard 在真实代码库中受益明显。
- 📊 **启动内存**：随路由数增长仍保持较高内存效率；400 条路由无验证器约 24MB，AOT 约 23MB，TypeBox/Zod 场景也有优化。
- ⚡ **吞吐表现**：Elysia 2 RC 仍是 Bun 上最快框架，在 Node.js 上非常接近 Fastify，并改进了 `Elysia.t` schema 的验证与强制转换延迟。
- 🧪 **压测后内存**：负载测试后峰值内存低且可预测，例如 Bun 下 Elysia RSS 从 42.2MB 升至 53.5MB，优于多数组件。
- 🔍 **更深类型推断**：借助 TypeScript 7 更快推断，扩展宏、生命周期钩子、内联钩子的类型推断；错误响应可映射/覆盖并保持静态可分析。
- 🧾 **OpenAPI 与 Eden 受益**：错误响应类型更准确，OpenAPI 可自动列出路由可能抛出的错误，Eden Treaty 类型生成更有用。
- 🔄 **生命周期 API 回退**：恢复原有 `on` 前缀，Elysia 1 插件基本可直接工作；双参数 `onError` 仍是破坏性变更。
- 🧩 **自定义宏类型**：支持显式标注和控制宏类型，属于面向类型高级用户和插件作者的可选高级能力。
- 🌿 **Eden Plugin**：新增带显式类型的 Eden 插件，可添加自定义字段或扩展 Eden Treaty。
- 🟢 **Node.js 改进**：使用 `srvx` 和 `crossws` 作为兼容层，在保持 Web Standard API 的同时兼顾 Node.js 性能与稳定性。
- 🗜️ **压缩插件**：新增官方 `@elysia/compress`，支持 gzip/brotli，并优先使用 Bun 快路径。
- 🛡️ **稳定性与迁移**：RC 延迟约两个月进行密集测试；测试量约为 beta 的 3 倍、1.4 的 10 倍，并设置性能、内存、类型推断门槛；提供 `bunx @elysia/codemod@latest` 迁移。
- 📚 **新文档站**：文档从 Vitepress 迁移至 Astro Starlight，更初学者友好，新增 lifecycle playground 等内容，并更新 LLM skills。
- 💌 **作者后记**：SaltyAom 回顾一年开发压力与等待，以歌曲表达“雨季结束前回来”的承诺，并感谢社区及 GitHub sponsors，特别是 Bun 的 Jarred Sumner。

---

### [ESLint v10.13.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/10/eslint-v10.13.0-released/)

**原文标题**: [ESLint v10.13.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/10/eslint-v10.13.0-released/)

ESLint v10.13.0 于 2026 年 10 月 16 日发布，这是一次小版本升级，新增功能并修复若干缺陷；多条核心规则也得到更新，以报告更多 lint 问题。

- 🚀 发布 ESLint v10.13.0：小版本升级，包含新功能与缺陷修复。
- 🧠 更新 `no-use-before-define`：将立即执行函数表达式（IIFE）视为在其定义和调用处执行，因此可能产生更多 lint 错误。
- 🌐 更新 `no-obj-calls`：现在会报告对 `globalThis` 的调用。
- ⚠️ 更新 `no-unsafe-optional-chaining`：报告 `yield*` 参数中可选链的不安全用法。
- 🐞 修复缺陷：避免 `no-var` 与 `one-var` 同时修复时导致 `let` 重复声明。
- 📚 文档更新：更新 README，并澄清 `getText` 的参数说明。
- 🛠️ 维护与性能：更新 GitHub Actions、依赖和生态插件，重新启用 TypeScript ESLint 生态测试，并优化 `no-redeclare` 对单声明变量的扫描。

---

### [发布 v9.0.0 · egoist/tsup · GitHub](https://github.com/egoist/tsup/releases/tag/v9.0.0)

**原文标题**: [Release v9.0.0 · egoist/tsup · GitHub](https://github.com/egoist/tsup/releases/tag/v9.0.0)

tsup 发布 v9.0.0，包含破坏性变更、依赖升级、类型导出与配置修复，并列出相关贡献者。

- 🚀 tsup 发布 v9.0.0，为当前最新版本。
- ⚠️ 破坏性变更：迁移至 obug，并放弃对 Node < 22.18 的支持（@sxzz）。
- ⬆️ 功能更新：升级 esbuild 与 chokidar，并公开 Plugin 类型（@Sunny-117，#1264）。
- 🐞 Bug 修复：移除 tsconfig 中的 baseUrl（@pxseu，#1390）。
- 👥 贡献者包括 sxzz、pxseu 和 Sunny-117；发布提交带有已验证签名。

---

### [发布 v4.3.0 · vuetifyjs/vuetify · GitHub](https://github.com/vuetifyjs/vuetify/releases/tag/v4.3.0)

**原文标题**: [Release v4.3.0 · vuetifyjs/vuetify · GitHub](https://github.com/vuetifyjs/vuetify/releases/tag/v4.3.0)

Vuetify v4.3.0（Paladin）发布，包含组件晋升、MD3 风格增强、多项新功能与修复、代码重构及 Labs 新组件；官方同时呼吁通过 OpenCollective 赞助以维持项目独立与持续维护。

- 🏅 `v-avatar-group`、`v-highlight`、`v-progress` 从 Labs 晋升为核心组件。
- 🎨 多项 MD3 增强：Slider 新增 `pill` 变体、Progress 对齐 MD3、Button 系列支持可选尺寸与圆角动画、Tab 新增 `slider-variant`。
- 🧭 NavigationDrawer 新增 `modal` 属性及 `v-model:expanded`。
- 🪟 Overlay 新增 `contextmenu`；Alert 新增 `timeout` 与倒计时指示；Autocomplete/Combobox 新增 `filtered-order`。
- 📊 DataTable 新增 `filtered` 选择策略，向 `rowProps` 传递展开/选中状态，并为选中/展开行添加数据属性。
- 📅 DateInput 增加本地化格式提示；DatePicker 增加日期事件处理、可滚动月份导航及动画稳定性修复。
- 🧩 Row 新增响应式 gap 属性；SlideGroup 新增 `padding` 与 `gap`；SelectionControl 新增描述属性与插槽。
- 🎠 Carousel/Window 支持滚轮导航；Carousel 新增 `pause-on-hover`；修复 Window 箭头与触摸切换动画。
- 🎚️ Slider/RangeSlider 改进无障碍支持；Slider 新增 `centered`；TimePicker 扩展 `scrollable`；新增 `v-touch-hold` 指令。
- 🐞 修复包括：click-outside 支持右键/中键关闭、SSR 挂载前渲染尺寸与偏移、表单控件暴露 focus、Rating 图标尺寸、Textarea 自动增长时保留原生撤销历史。
- 🧱 重构 observer、display、locale、rtl 相关实现以使用 `@vuetify/v0`。
- 🧪 Labs 新增 VAudio、VSplitBtn、VInfiniteCarousel、VTimeInput、VLoadingIndicator；CommandPalette 改进无障碍与自定义插槽；VVideo 增加 `actions`、重构进度条与音量控制，并重命名 i18n key（可能破坏自定义）。
- 💰 官方强调项目保持独立，需社区通过 OpenCollective 持续赞助以支持问题修复、PR 审核、新功能与生态工具维护。

---

### [分歧：格式化脚本可能使其变成另一个程序——横跨 37 个以上 JavaScript](https://trustsig.eu/blog/javascript-divergence/)

**原文标题**: [Divergence: formatting a script can turn it into a different program, across 37+ JavaScript processors | TrustSig Blog](https://trustsig.eu/blog/javascript-divergence/)

2026年10月17日，Robert Vähhi 介绍了一种名为“Divergence（分歧化）”的 JavaScript 反逆向技术：仅对脚本做格式化、压缩或反混淆，就可能因处理器漏洞把原程序静态转换为作者预设的另一套逻辑；作者在 37+ 个 JavaScript 处理器中发现 186 种手法，并用“俄罗斯方块变贪吃蛇”演示其可行性。

- 🧠 核心机制：不依赖 source map、运行时完整性检查或网络，只利用 JS 处理器 bug，把脚本“格式化”为不同逻辑。
- 🛠️ 影响范围：Chromium/Firefox DevTools、prettier、js-beautify、Babel、esbuild、Terser、WebCrack、restringer 等 37+ 个格式化器、压缩器和反混淆器。
- 🎮 演示效果：Tetris 脚本经任意处理器后生成 Snake 字节码并抹掉 Tetris，甚至 DevTools 输出也能触发。
- 🕵️ 攻击目标：分歧后的脚本是“诱饵”而非阻断；它仍可运行、不报错，让逆向者或 LLM 分析错误程序。
- 🤖 对 LLM 智能体：它们几乎总会先格式化脚本，且通常只通过“还能不能跑”验证，因此该技术对 LLM 逆向特别有效。
- ♻️ 对重实现：即使只改一个数值，重实现会发送真实脚本不会发送的值，服务端可检测并延迟封禁或监控。
- 📊 六类严重度：Rerouted（低，换值/路径）、Rewritten（低，换写法）、Folded（中，错误常量折叠）、Stripped（中，删副作用语句/参数）、Pruned（高，删分支）、Erased（高，清空/删除函数）。
- 🔍 典型例子：Chromium DevTools 把 `+ +m` 粘成 `++m`；WebCrack 把 `a.b || (a.b = c)` 改成 `||=` 导致左侧只求值一次；Terser 删除会抛 `TypeError` 的 `0 in 1`，改变 try/catch 走向。
- 🧪 其他案例：Restringer 误把被覆盖的 `atob` 当内置函数折叠；DataDome 反混淆器丢弃序列中的 `new Tick()`；obfuscator.io 反混淆器把 `null` 当 truthy 而删除 else 分支。
- 🎨 可扩展到 CSS：类似思路也能让格式化后的 CSS 产生不同显示效果。
- ⚠️ 限制：没有单一技术通杀所有处理器；不同工具、模式、配置触发条件不同，上游库技术会传播到下游工具。
- 🔗 资源：演示 `divergence-game.trustsig.eu`，试验场 `divergence.trustsig.eu`。

---

### [](https://nolanlawson.com/2026/10/19/do-web-components-have-a-future-if-nobody-is-writing-them/)

**原文标题**: [Do web components have a future if nobody is writing them? | Read the Tea Leaves](https://nolanlawson.com/2026/10/19/do-web-components-have-a-future-if-nobody-is-writing-them/)

文章讨论 Web Components 在 AI 编程时代的前景。作者指出，“use the platform”常被误读为“使用 Web Components”，但 Google 的 Modern Web Guidance 中 Web Components 更像事后补充；agentic coding 削弱了其复用价值，不过 micro-frontends 和独立组件仍有空间。最终，作者认为 Web Components 的最大遗产是“解释平台”并影响标准，尽管 SSR、样式共享和可访问性等问题仍未解决。

- 🧭 “use the platform”被误读为 Web Components，主要源于 Polymer 的早期口号；作者认为现代 HTML/CSS 功能才是更好的“用平台”例子。
- 🤖 Google 的 Modern Web Guidance 是面向 agent 的“用平台”指南，但 Web Components 在演示和代码中显得边缘化，甚至建议先判断“是否真的需要 custom element”。
- ⚠️ Agentic coding 削弱了 Web Components 的核心价值：手写 HTML、代码稀缺和复用经济性等前提正在消失，vibe-coding、可替换框架和 shadcn/DIY 趋势也削弱了 shadow DOM 等优势。
- 🧩 作者提出两个较弱的 salvage 场景：micro-frontends/多 agent 隔离，但 iframe 是更强沙箱；以及独立复用组件，如 `<emoji-picker>` 仍有分发价值。
- 🧠 作者不认为 React 是最终组件复用层，但更关键的是：框架对许多用户可能只是 `AGENTS.md` 里的脚注，用户真正关心的是应用是否可用。
- 🛠️ Web Components 仍有 SSR、样式共享和可访问性等未解问题；作者本站的主题选择器是 light DOM Web Component，但他必须明确要求 agent 使用。
- 🏆 其明确胜利是“解释平台”：Web Components 概念影响了 Open UI 的 parts/slots，并推动 customizable `<select>`、popovers、invoker commands 等平台功能，已融入 Web 平台纹理。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=javascriptweekly&utm_term=home&utm_content=Cooperpress)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=javascriptweekly&utm_term=home&utm_content=Cooperpress)

Expo 定位为面向智能体时代的移动基础设施，提供从开发、测试、部署到监控的一站式工具链，帮助团队用单一代码库构建并发布 Android、iOS 和 Web 原生应用。

- 🚀 Expo 提供 CLI、开发工具、云模拟器和移动 CI/CD，覆盖智能体工作流的核心环节。
- 🧱 开发阶段可使用 Expo CLI、Skills、MCP、Expo Go 和 Simulators 构建与验证应用。
- 🧪 测试阶段提供云模拟器和设备基础设施，Workflows 可在每次变更时运行测试套件。
- 📦 部署阶段支持 TestFlight、应用商店发布、OTA 更新、渠道与灰度发布控制。
- 📈 监控阶段通过 Observe 展示崩溃信息、性能指标和 Update 采用情况，并可快速推送修复。
- 🤖 云模拟器可由编码智能体按需驱动，自动运行应用、验证工作并附截图、录屏和日志，无需 Mac。
- 🛠️ Expo SDK 拥有 100+ 生产级 API，支持原生代码，并兼容 React Native、Swift、Jetpack Compose、Kotlin 等。
- 🌍 单一代码库可构建并分发到 Android、iOS 和 Web，Update 可即时向用户发送修复与改进。
- 🚀 Launch 可引导开发者完成上架流程，降低发布到 App Store 的技术门槛。
- ⚙️ Workflows 可自动化构建、测试、更新和发布流程。
- 📊 平台数据包括 300 万+ 开发者、5 万+ GitHub Stars、700 万+ 周下载量、10 万+ 活跃开发者、50 万+ 项目和每日 10 万+ 构建。
- 👥 80% 的 React Native 开发者选择 Expo，Discord 社区成员超过 7 万，用户普遍评价其易用、跨平台和开发效率高。
- ✅ Expo 获 Meta 推荐，是 React Foundation 成员，并符合 SOC 2 Type II、GDPR、CCPA 和 SSO 等合规要求。

---

### [ViteConf 2026 | 第五届 - 我们是 Vite - YouTube](https://www.youtube.com/watch?v=PfyIEgLzNYI)

**原文标题**: [ViteConf 2026 | 5th Edition - We Are Vite - YouTube](https://www.youtube.com/watch?v=PfyIEgLzNYI)

该内容为 YouTube 网站页脚信息，主要包含平台介绍、联系与合作入口、创作者与开发者资源、法律条款及版权声明。

- 🏢 提供 About、Press、Contact us 等平台介绍与联系入口
- 🤝 包含 Creators、Advertise、Developers 等创作者、广告与合作资源
- 📜 列出 Terms、Privacy、Policy & Safety 等法律、隐私与安全条款
- ⚙️ 提供 How YouTube works 与 Test new features 等功能说明和测试入口
- ©️ 版权声明为 © 2026 Google LLC

---

### [如何对 JavaScript 程序员进行煤气灯操纵](https://www.bryanpg.com/articles/pragma-twice/proxy.html)

**原文标题**: [How to Gaslight JavaScript Programmers](https://www.bryanpg.com/articles/pragma-twice/proxy.html)

JavaScript 的 `Proxy` 能拦截对象属性访问、赋值、枚举和删除等操作，让调用者在运行时看到被隐藏、伪造或操纵的对象行为；文章用隐藏 `goodbye` 方法、制造异常赋值行为等示例解释这种“煤气灯式”效果，并介绍其在游戏 `Pragma Twice` 中的用途、正当应用场景及发现隐藏属性的可能性。

- 🕵️ 核心主题：`Proxy` 可像钩子或中间件一样介入对象操作，从而欺骗或误导调用者。
- 🔒 隐藏属性示例：对象表面只有 `hello`，但 `obj.goodbye()` 仍可调用；`goodbye` 不出现在 `console.log`、`Object.keys`、`Reflect.ownKeys` 或 `for...in` 中。
- 🪤 `Proxy` 可拦截属性访问、赋值、枚举甚至删除，能隐藏属性、发明“虚拟”属性，或让赋值行为变得反常。
- 🎮 作者动机：在 JavaScript 解谜冒险游戏 `Pragma Twice` 中隐藏部分 API 方法，鼓励玩家通过游戏进程“解锁知识”，类似 `Tunic` 的探索体验。
- 🧰 正当用途：可用于让 `console.log` 同时输出到控制台和文件，也可被 Vue 等响应式框架用于检测对象变化并更新 UI。
- 🔎 发现隐藏属性：理论上可用 `typeof obj[guess]` 配合字典或暴力猜测推断属性是否存在，但无源码时仍较困难。
- 🧪 完整源码展示了如何通过 `Proxy` 的 `get` 拦截器，在访问 `goodbye` 时返回私有对象中的方法。
- 😈 文章最后以 “Happy gaslighting!” 收尾，强调 `Proxy` 强大但也可用于刻意操纵调用者认知。

---

### [](https://nothing-else.blog/blog/we-migrated-70000-tests-from-jest-to-vitest-yes-in-2-months)

**原文标题**: [We migrated 70,000 tests from Jest to Vitest. Yes, in 2 months. | Nothing Else](https://nothing-else.blog/blog/we-migrated-70000-tests-from-jest-to-vitest-yes-in-2-months)

Miro 前端团队用约 2 个月将主前端应用的 70,000 个单元测试从 Jest 迁移到 Vitest，并通过渐进式迁移、AI Agent 辅助和关键性能优化，显著降低 CI 内存消耗、提升测试速度，还顺带发现并移除了泄漏到生产包中的测试数据。

- 🚨 迁移前痛点：主应用约 600 万行代码、800+ 包、70,000 个测试；CI 需 6 个 runner，单次最长约 20 分钟，25% 运行因内存泄漏 OOM 失败。
- 🐢 Jest 瓶颈：即使使用 SWC，平均仅约 13 tests/sec；Jest 29 到 30 仅带来约 5% 的速度和内存改善，且 ESM、类型推断、覆盖率、隔离性等能力不足。
- 🔍 方案选型：对比 Rstest 与 Vitest；Rstest 在 CI 上出现 OOM，Vitest 因社区成熟、ESM-first、类型安全、测试隔离和 Jest 兼容性胜出。
- 🧪 渐进式迁移：Jest 与 Vitest 在 CI 上并行运行，按包逐步迁移，通过 `--runner=vitest` 等开关区分 runner，并保留兼容桥接以减少重复改造。
- 🤖 AI Agent 辅助：在仓库中创建迁移 skill，让 Agent 学习上下文和模式；迁移逐步变得更快、更一致、更少幻觉。
- 🧱 中间危机：迁移过半时 CI 内存反而上升；原因是每个包作为独立 Vitest project 时不会共享转换缓存，导致模块图被重复转换。
- 🛠️ 关键优化：先合并默认配置项目，将 800+ 项目压缩到 60 个；后又利用 `expect.getState().testPath` 动态加载对应 setup 脚本，将所有项目合并为单次测试运行。
- 📉 性能收益：最终测试速度从约 13 tests/sec 提升到 19 tests/sec，约快 50%；CI 内存消耗降低约 30%；合并项目后堆内存、总耗时和转换时间大幅下降。
- 📦 额外收益：Vitest 使用 Node API 暴露了测试 fixture 泄漏到生产包的问题，移除后生产构建体积减少约 4MB。
- ✅ 质量提升：获得类型安全的 mock、自动 mock hoisting、真实测试隔离、跨包准确覆盖率和统一 polyfill 配置。
- 💰 成本回报：AI 模型使用成本约 7,000 美元；预计 CI runner 年节省约 75,000 美元，并带来更快反馈和更多发布机会。
- 📊 迁移规模：活跃迁移约 80 天，合并 97 个 PR，改动 9,328 个文件，新增/删除约 +87,701 / -78,946 行。
- 💡 经验教训：明确目标、先小范围验证、制定渐进计划、给 AI 具体约束、建立团队信任、接受不可预见问题，并依赖可信 CI 与快速回滚机制。
- 🚀 最终结论：迁移达成速度、内存、代码现代化和类型安全等目标，也证明了在清晰上下文与流程下，AI Agent 可支撑大规模工程迁移。

---

### [](https://trigger.dev/blog/zod-4-got-rid-of-a-bunch-of-cpus-for-us)

**原文标题**: [Zod 4 got rid of a bunch of CPUs for us | Trigger.dev](https://trigger.dev/blog/zod-4-got-rid-of-a-bunch-of-cpus-for-us)

Trigger.dev 将 worker 从 Zod 3.x 升级到 Zod 4.5 后，解析负载显著下降：worker CPU 降低近三分之一，批处理吞吐提升 14%，任务触发 p99 降低 18%；同时 Trigger.dev 成为 Zod 首个白金赞助商。文章还介绍了 Zod 的使用规模、schema 编译实验，以及升级中遇到并修复的导入兼容问题。

- ⚙️ Trigger.dev 每天大量解析 JSON，包括任务负载、批量项、队列消息、重试包装和用户 schema。
- 📉 升级 Zod 4.5 后，一个主要服务的 CPU 需求下降近 1/3，并带来事件循环利用率（ELU）余量。
- 🚀 生产指标改善：批处理吞吐量提升 14%，任务触发 p99 降低 18%。
- 📊 单个 worker 服务约每秒 1,100 次解析、每日近 1 亿次；每个 job 至少一次 safeParse，约半数 job 还会解析每条消息，约另 10 次/job。
- 🧩 对简单服务器 schema 试用 Zod 的 schema compilation 后，worker CPU 约再降 5%，ELU 也更低，后续将继续试验。
- 🤝 Trigger.dev 成为 Zod 首个 Platinum Sponsor，以回馈日常依赖的开源项目。
- ⚠️ 升级整体顺利，但 core 包中一个遗漏的裸 `zod` 导入，导致部分仍使用 Zod v3 且使用 npm 的用户出现任务 warm start 延迟。
- ✅ 团队已定位并修复该问题，还加入 oxlint 检查防止复发。

---

### [`replace()` 作为迭代器](https://www.lazutkin.com/blog/2026-10-13-replace-as-an-iterator)

**原文标题**: [


     `replace()` as an iterator 

](https://www.lazutkin.com/blog/2026-10-13-replace-as-an-iterator)

文章回顾了 `String.prototype.replace()` 搭配全局正则和回调函数作为“迭代器”的用法：它会对每个匹配调用一次回调，可用于过滤、映射、解析和词法分析；但在 V8 上通常比 `exec()` 循环等替代方案慢。新代码应优先使用 `matchAll()`，而旧代码中返回值未被使用的 `replace()` 往往就是这种迭代器模式。

- 🔁 **核心技巧**：`replace(/re/g, fn)` 会对每个匹配调用 `fn`，并传入匹配内容、捕获组、偏移量和原字符串；回调的返回值会被拼进新字符串。
- 🧹 **返回空字符串**：回调应返回 `''`，避免把 `"undefined"` 或匹配文本拼进被丢弃的结果中，从而减少内存压力。
- 🎛️ **过滤与映射合一**：在回调内分支可实现过滤，利用捕获组可实现映射；正则未匹配的部分不会进入回调。
- 🧩 **替代多阶段处理**：一个描述“字段是什么”的正则可以替代 `split().map().filter()` 链，也能替代手写扫描器。
- 🧠 **单正则词法器**：可用一个正则完成词法分析，并配合 shunting-yard 算法驱动自底向上解析器；剩余字符串可作为错误报告。
- 🔄 **其他内置方案**：包括 `exec()` 循环、`match()`、`split()`、`matchAll()` 和 `replaceAll()`；其中 `matchAll()` 是现代推荐方式。
- ⚡ **性能表现**：在 V8 上，`replace()` 是五种遍历匹配方式中最慢的，约为 `exec()` 循环的 1.5 倍（1 KB）到 2.9–3.7 倍（10 MB）。
- 🏁 **更快选择**：`match()` 通常最快；`matchAll()` 配合 `for-of` 比 `exec()` 循环慢约 7%–22%。
- 🧪 **node-re2 反转结果**：使用 node-re2 时，`replace()` 约为 `exec()` 循环耗时的 0.28–0.38 倍，但仍慢于内置引擎；`match()` 最快。
- 🛠️ **使用建议**：旧代码通常无需重写；大输入或需要提前停止/在匹配间 `await` 时改用 `matchAll()`；新代码优先 `matchAll()`，只关心匹配文本时用 `match()`。

---

### [递归已死，是 HTML 杀死了它 - daverupert.com](https://daverupert.com/2026/10/html-recursion/)

**原文标题**: [Recursion is DEAD and HTML killed it - daverupert.com](https://daverupert.com/2026/10/html-recursion/)

文章介绍 Chromium 正在试验的 Declarative Partial Updates：它通过新的 `<?marker>` 元素和 `<template for="">` 语法，实现 HTML 的乱序流式注入与自组装。作者以嵌套回复线程为例，说明这种声明式方案可以取代传统递归渲染，避免先在服务端构建完整树再同步输出 HTML，但也提醒要处理 FOUC、LCP、超大线程性能等现实问题。

- 🧩 `<?marker name="">` 用作占位符，后到的 `<template for="">` 内容会自动填入对应位置。
- 🌊 核心能力是保持连接不关闭，持续向页面流式追加 HTML，并由浏览器把内容放到正确位置。
- ⏳ `<?marker>` 是一次性的；若要继续串联内容，需要在追加内容底部重复放置同名 marker。
- 🔁 传统嵌套评论渲染需要逐层查询、组装树、递归遍历并同步渲染，用户要等待多个阻塞步骤。
- 🚀 使用 `<?marker>` 后，服务端可取扁平帖子列表，逐条发送 HTML，无需递归或预先建树，页面自行拼装。
- 🧠 适用场景包括嵌套回复、商品评论、大型 PR 评论线程、书籍与相关书籍等关系型内容。
- ⚠️ 仍需关注 FOUC、LCP、超大线程压垮浏览器等问题，并配合“加载更多评论”等按需加载策略。
- ✨ 作者期待 HTML 获得声明式自组装内容与关系的能力，甚至希望 HTML Imports 借此复活。

---

### [声明式部分更新 | Web 平台 | Chrome 开发者](https://developer.chrome.com/docs/web-platform/declarative-partial-updates)

**原文标题**: [Declarative partial updates  |  Web Platform  |  Chrome for Developers](https://developer.chrome.com/docs/web-platform/declarative-partial-updates)

本文介绍 Chrome 团队推动的 Declarative Partial Updates：通过乱序流式 HTML 与更一致的 HTML 插入/流式 JavaScript API，让内容可按就绪顺序更新，减少对重型框架和复杂 DOM 操作的依赖，并提升性能与开发体验；部分能力已进入 HTML 标准或实验阶段，并提供 polyfill。

- 🧩 背景：现代 Web 应用偏组件化，但 HTML 仍按顺序解析，开发者常等待整页完成或依赖 JS 框架异步交付组件，影响性能。
- 📦 乱序流式 API：使用 `<?marker>`、`<?start>`、`<?end>` 处理指令和带 `for` 属性的 `<template>`，在解析后替换占位内容。
- 🖼️ 更新机制：模板可替换具名占位符；`start/end` 可先显示“Loading…”再替换；模板内可继续放 marker 以支持多次更新。
- ❓ 采用处理指令：可在不影响 DOM 的情况下打补丁，适用于 `<head>`、`<table>` 等场景，并降低向后兼容风险；相关能力已成为 HTML 标准的一部分。
- 🏝️ 主要用例：支持岛屿架构、内容就绪即流式交付、按页面加载性能优化 HTML 顺序，例如后置大型菜单内容。
- ⚠️ 限制：`<template for>` 默认只能更新同一父元素内的处理指令，直接放在 `<body>` 可访问全文档；`<?end>` 可选；移动流式目标可能产生异常。
- 🧪 标准化与兼容：`<template for>` 已入标准但尚未被所有浏览器支持；Chrome 团队提供 `template-for-polyfill`。
- ⚙️ 新插入 API：新增一致的静态与流式方法，如 `setHTML/streamHTML`、`appendHTML/streamAppendHTML`、`replaceWithHTML` 等，并含 `Unsafe` 版本。
- 🔐 安全选项：`options` 支持自定义 `Sanitizer`；`Unsafe` 方法默认关闭清理器，可选 `runScripts`（默认 `false`），需根据输入可信度谨慎使用。
- 🌊 流式优势：可与 Streams API、`fetch` pipe、`textStream` 配合，边下载边插入，适合 SPA 大内容更新和复用页脚等局部内容。
- 📌 状态：新插入/流式方法正在纳入 HTML 标准，Chrome 148 起实验、计划 Chrome 155 发布；提供 `html-setters-polyfill`，但不真正流式且依赖相关 API 支持。
- 🤝 组合价值：将 `<template for>` 流式插入与 JS 流式 API 结合，可动态更新页面多个区域，减少 DOM 引用和样板代码，释放更多用例。

---

### [获取失败](https://vimeo.com/1234257957)

**原文标题**: [Failed to retrieve](https://vimeo.com/1234257957)

无法总结：获取内容失败，状态码 403。

---

### [Maplair 4.0 — Leaflet 的一个分支 - Maplair](https://maplair.org/2026/10/19/maplair-4.0.0.html)

**原文标题**: [Maplair 4.0 — a fork of Leaflet - Maplair](https://maplair.org/2026/10/19/maplair-4.0.0.html)

Maplair 4.0.0 是 Leaflet 的首个稳定分支版本，基于 Leaflet 2.0 的 ES 模块、标准 JavaScript 类和 Pointer Events 工作，并整合了许多过去需要插件或变通方案才能实现的功能。版本号从 4.0 开始，以避免与 Leaflet 2.x/3.x 混淆；此次发布强调模块化、性能、可访问性、国际化与现代化迁移，同时带来大量 API、文件命名和兼容性变更。

- 🍁 发布定位：2026 年 10 月 19 日发布首个稳定版，作为 Leaflet 分支，延续 Leaflet 2.0 的现代化方向。
- 🌍 国际化：新增 I18n API，内置德语、西班牙语、法语、捷克语、斯洛伐克语、匈牙利语、斯洛文尼亚语、意大利语和罗曼什语等文本翻译，并支持 Transifex 协作。
- ⚡ 性能与体积：新增 markerCulling、shadow: false、弹窗单次布局等优化；tree-shaking 后仅瓦片地图约 34 KB gzip，全量约 63 KB gzip。
- 🧩 开发体验：使用标准 constructor() 类、JSDoc + TypeScript 类型声明和自动生成 API 参考；启用枫叶 logo 与 🍁 标记。
- 🧭 新控件：FullscreenControl、SearchControl、ButtonControl/ButtonBarControl、TextControl、MiniMapControl、SideBySideControl、LegendControl/Classification、ContextMenu，并支持控件排序。
- 🔄 地图交互：支持地图旋转 bearing、双指旋转、RotateControl、标记旋转；continuousZoom、触控板缩放/平移、tapDragZoom 等增强缩放体验。
- 🔗 视图与同步：Hash 可将视图/图层写入 URL，MapSync 可同步多个地图视图，支持 setCrs、idle 事件、devicePixelRatio 变化和隐藏地图保持视图。
- ♿ 可访问性：地图支持 ariaLabel，按 ? 显示键盘快捷键，控件使用 <button>，键盘打开的弹窗获得焦点，弹窗/提示可溢出地图。
- 🗺️ 图层与标记：SvgIcon 支持彩色/emoji/SVG 标记，HeatLayer 绘制热力图，DisplaceHandler 防止圆标重叠；瓦片支持 fetchOptions、setUrl、placeholder、pixelated 等。
- 📦 可选模块：地图/标记旋转、Marker moveTo/moveAlong、虚线动画、路径箭头与文字、GeoJSON URL 加载、按缩放调整样式等均拆分为可选模块。
- 🎨 主题化：颜色、边框、阴影、字体和间距改为 CSS 变量，可通过覆盖变量定制地图主题。
- 🚚 迁移重点：仅支持 Baseline 广泛可用浏览器，不再支持 IE；npm 包为 ES modules 具名导出，无默认导出和全局 L，旧式脚本可用 maplair-global.js。
- 🧱 API 变更：文件与 CSS 类从 leaflet-* 改为 maplair-*，图片改为 SVG；移除工厂函数，改用构造函数；类拆分为独立导出；LatLng/Point 构造函数始终复制，from() 不复制。
- 🖱️ 事件与工具：改用 Pointer Events；移除 Class.extend()、initialize()、旧事件别名及已由标准 API 替代的工具函数；部分 title/label 选项改由 I18n 处理。
- 💬 反馈渠道：可在 GitHub 报告问题并提供反馈，官方鼓励继续享受地图制作。

---

### [编辑器 AI SDK 游乐场 | Thinkfree 开发者](https://playground.developers.thinkfree.com/playground/editor-ai-sdk/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=sdklaunch2026&utm_content=261020)

**原文标题**: [Editor AI SDK Playground | Thinkfree Developers](https://playground.developers.thinkfree.com/playground/editor-ai-sdk/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=sdklaunch2026&utm_content=261020)

您尚未提供需要总结的文章内容，因此暂时无法生成摘要。

- 📄 请在下一条消息中粘贴文章正文。
- ✍️ 收到内容后，我会输出中文概览与要点列表。
- ✅ 要点将使用“-”符号，并配上合适表情符号。
- 🎯 摘要会突出关键信息与文章核心内容。

---

### [编辑器 AI SDK 演练场 | Thinkfree 开发者](https://playground.developers.thinkfree.com/playground/editor-ai-sdk/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=sdklaunch2026&utm_content=261110)

**原文标题**: [Editor AI SDK Playground | Thinkfree Developers](https://playground.developers.thinkfree.com/playground/editor-ai-sdk/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=sdklaunch2026&utm_content=261110)

未收到需要总结的文章内容，因此暂时无法提炼概览与关键要点。请补充原文后，我会按你要求的格式整理成中文摘要。

- 📄 当前输入为空，没有可供总结的文章正文。
- ❓ 无法确定文章主题、核心观点和结论。
- 📝 请提供具体文本内容，我将输出概览与带表情符号的要点列表。

---

### [](https://chartist.dev/)

**原文标题**: [Chartist](https://chartist.dev/)

Chartist 是一个自 2014 年起持续维护的开源 SVG 图表库，主打“简单图表，用 CSS 打扮”。它不依赖 Canvas、没有运行时依赖，也不用主题引擎，而是通过可预测的 CSS 类名和自定义属性让开发者完全掌控样式，适合追求轻量、纯 SVG 与高度可定制外观的项目。

- 🧩 核心理念：生成干净、响应式的 SVG 图表，样式完全交给 CSS，无 Canvas、无依赖、无主题引擎。
- 📦 使用方式灵活：支持 npm 安装，也可直接从 CDN 以原生 ES Module 引入，无需构建步骤。
- 📊 图表类型齐全：折线、面积、散点、柱状（分组或堆叠）、饼图、环形图、仪表图，以及柱线组合双 Y 轴图表。
- 📱 响应式双方案：可基于窗口宽度或图表容器宽度（实验性）调整，条件直接用 CSS 媒体/容器查询语法编写。
- 🎨 纯 CSS 样式化：SVG 元素带可预测类名，颜色、线条、文字均可通过样式表和自定义属性控制。
- 🔧 开放渲染流水线：resolve、prepare、layout、compose、scene、render、mount 七个阶段均开放事件，可修改、替换或装饰任意元素。
- 🧩 插件生态：支持图例、缩放、阈值等社区插件，1.x 插件可通过 `fromLegacyPlugin` 在 v2 中继续使用。
- 🖥️ 服务端渲染：可输出 SVG 字符串，无需 DOM，适用于 PDF、邮件和图片生成。
- ⚡ 体积小巧：按需引入，核心仅 5.8 kB，含折线图约 14.5 kB（gzip）。
- 🆕 官方扩展包：`@chartist-js/tooltips` 提供鼠标、触摸和键盘提示；`essentials` 提供轴标题、趋势线、对数轴；`terminal` 支持终端与文本艺术图表。
- 📈 社区数据：月 npm 下载 49.4 万，GitHub 星标 1.34 万，7.28 万个公共仓库依赖，已有 12 年生产使用历史。
- 🆚 竞品对比：14.5 kB 远小于 Chart.js 的 49.4 kB、ApexCharts 的 172.3 kB 和 Highcharts 的 104.7 kB；优势在轻量、纯 SVG、CSS 样式与免费许可，劣势是内置交互和图表类型较少。
- 🧑‍💻 框架集成：无需包装器，同时有 React、Angular、Vue、Node.js、Rails、Blazor 等社区组件可用。
- 🎞️ 动画能力：用纯 CSS 和少量 SMIL 实现线条绘制、柱状生长、环形扫过，并尊重“减少动效”偏好。
- 🪪 许可与社区：MIT 或 WTFPL 双许可，93 位贡献者自 2014 年持续参与维护。

---

### [从 1.x 迁移 · Chartist](https://chartist.dev/docs/coming-from-1x/)

**原文标题**: [Coming from 1.x · Chartist](https://chartist.dev/docs/coming-from-1x/)

overview summary  
Chartist v2 在保持 1.x 向后兼容的同时引入函数式 API；现有图表可继续运行，但 1.x 事件与插件需通过 `compat` 或 `fromLegacyPlugin()` 适配，类 API 在 2.x 中弃用并将在 3.0 移除。

- 🧩 1.x 类 API 仍可按原方式导入和构造，容器、数据、选项与响应式选项参数不变，默认样式兼容 1.5.0。
- 🔌 1.x 事件（如 `draw`、`created`、`animationBegin`）在 v2 需在 `plugins` 中加入 `compat`，否则监听器不会触发并会收到控制台提示。
- 🛠️ 1.x 插件在类 API 上需配合 `compat`；在函数 API 上需用 `fromLegacyPlugin()` 包装，普通函数插件会报错。
- 🚀 推荐逐步迁移到 `lineChart()`、`barChart()`、`pieChart()` 或 `chart()`，参数与旧类一致，类与函数可在同一页面并存。
- ⏱️ 函数返回轻量 handle：立即渲染、通过 `ResizeObserver` 响应容器尺寸变化，并用 `update({ data })`、`setOptions()`、`detach()`/`destroy()` 替代旧方法。
- 🎨 旧的 `draw` 处理器应改写为 v2 插件，监听 `compose` 在渲染前修改场景节点，这样也能支持服务端渲染。
- 🌐 0.x 社区插件依赖全局 `Chartist`；导入 `chartist/compat` 可补齐全局名称，再以脚本加载插件并用 `fromLegacyPlugin()` 包装。
- 📦 不同加载方式需注意顺序：模块方式先导入 `compat` 再加载插件脚本；UMD 方式在 Chartist 后加载 `compat.umd.js`；打包器需运行时加载插件脚本。
- 🆕 函数 API 新增组合图表、容器查询响应式选项、SSR（`toScene()`/`renderToString()`）、v2 插件管线、`setOptions()`/`on` 选项及更严格类型。
- 🧹 v2 未删除导出；类及仅类使用的 API 在 2.x 弃用、3.0 移除，同时修复多项 1.x 行为问题，如轴范围、donut 宽度、事件 `off()`、系列颜色和 `reverseData` 元数据等。

---

### [Pele · Mermaid 图表作为可主题化的 SVG](https://pele.run/)

**原文标题**: [Pele Â· Mermaid diagrams as themeable SVG](https://pele.run/)

Pele 是一个轻量级开源库，可将 Mermaid 图表渲染为 SVG，并通过 CSS 变量实现主题化。它零依赖、体积小、渲染快，支持 Mermaid 12.1.0 的所有内置图表类型，主要用于 Obsidian 等场景。

- 🌋 Pele 是开源库，用于把 Mermaid 语法渲染成 SVG，并使用 CSS 变量控制颜色和字体。
- ✍️ 使用方式简单：编写 Mermaid 语法后调用 `render()`，再把返回的 SVG 插入页面。
- ⚡ 相比 Mermaid.js，Pele 零依赖，体积约 230 kB gzip，渲染耗时 0.05–0.3 ms，明显更小更快。
- 📱 在小屏幕上，Pele 会自适应布局，而不是简单缩放图表。
- 🧩 Pele 支持 Mermaid 12.1.0 内置的全部图表类型。
- 📦 可通过 npm、pnpm、yarn 或 bun 安装 `pele`，并提供示例、API、主题、兼容性和安全等文档。
- 🎨 修改 CSS 变量即可调整主题颜色，无需重新渲染图表。
- 🧑‍💻 Pele 为 Obsidian 开发，采用 MIT 开源许可，名称源自火山与火之女神 Pele。

---

### [游乐场 · 贝利](https://pele.run/playground)

**原文标题**: [Playground Â· Pele](https://pele.run/playground)

该内容展示的是 Mermaid Playground（含 Pele 渲染对比）的界面与示例集合，涵盖多种 Mermaid 图表类型、源码/输出视图，以及将 Mermaid 文本解析、布局并渲染为 SVG 的流程，同时支持主题化、文件操作和示例切换。

- 🧩 页面提供 Playground 设置、打开文件、打开示例、复制分享链接、重置、清空、自动换行和搜索等功能。
- 📊 示例覆盖大量图表类型，如 flowchart、block、C4、class、ER、Gantt、Git、journey、kanban、mindmap、pie、quadrant、requirement、sankey、sequence、state、timeline、xychart 等。
- 🧠 还包含较新的图表/建模类型，如 agentflow、architecture、cynefin、ishikawa、radar、railroad、swimlane、treemap、treeview、usecase、venn、wardley。
- 🔄 源码示例展示 Mermaid 文本输入的处理流程：先判断是否支持，支持则解析、布局、渲染，不支持则回退。
- 🖼️ 渲染结果以 SVG 输出，并可通过 CSS 进行主题化。
- 👀 输出区域支持在 Pele、Mermaid、SVG 之间对比查看。
- ⚠️ 页面提示需要启用 JavaScript 才能在 Playground 中渲染图表。

---

### [](https://rich-input.netlify.app/)

**原文标题**: [<rich-input> – A Rich Input Field](https://rich-input.netlify.app/)

概述：rich-input 是一个原生、轻量的 Web Component，将搜索引擎级过滤智能引入标准 Web 表单，支持自由文本与结构化键值过滤，并提供自动补全、语法高亮、表单集成和主题定制能力。

- 🔎 支持自由文本搜索和结构化过滤语法，如 `label:"We Play House Recordings"`、`year:2026`、`playlist:"WPH Classics"`。
- 🎵 提供音乐搜索演示与预设查询，涵盖引号搜索、House 子类型、艺术家与风格、自由文本、无效值、负向过滤、OR 组合和分组查询。
- 🎯 双自动补全：既补全过滤关键词（如输入 `a` 提示 `artist:`、输入 `s` 提示 `style:`），也补全候选值（如输入 `label:"K` 提示 Keinemusik、Kranky）。
- 📍 使用 OpaqueRange 定位下拉框：通过 `range.getBoundingClientRect()` 锚定到当前值范围起点（如开引号处），无支持时回退到隐藏镜像 `<div>`。
- 🎨 借助 CSS Custom Highlight API 在原生 `<input>` 内直接高亮关键词和值，无需覆盖层 hack。
- 🧩 通过声明式 `<datalist>` 配置关键词和候选值，基本无需 JavaScript。
- 📋 表单关联：实现 `formAssociated = true` 与 ElementInternals，支持 `<form>` 提交、`FormData` 和重置生命周期。
- 💅 暴露 `::part(input)`、`::part(control)`、`::part(popover)`、`::part(suggestion-item)` 等 Shadow Parts，支持完整主题定制。
- 📦 可通过 npm 安装，或以 ESM/CDN 方式引入，注册后即可使用 `<rich-input>`。
- 🗂️ `<datalist>` 的 `id` 定义查询关键词，`label` 定义显示名，`data-type="number"` 支持数字字段；含空格的选项值会自动加引号。
- 🖼️ 支持在 `<option>` 中嵌入自定义 HTML（如 logo、头像、图标），选中后仅插入干净的 `value`。
- 🧠 OpaqueRange API（Chromium 152+）用于文本测量与高亮；通过 `createValueRange()` 创建范围并加入 `Highlight`，变更时用 `disconnect()` 清理。
- 🌐 跨浏览器回退：不支持 OpaqueRange 时，在 Shadow DOM 内使用 `[contenteditable]` 和隐藏镜像 `<div>`，并同步 `::highlight()` 规则。
- 🎛️ 支持通过 HTML 属性或 JavaScript 配置 operators、combinators、delimiters；提供 `value`、`getParsedQuery()`、`getKeywords()`、`focus()`、`select()`、`setSelectionRange()` 等 API。
- 📡 事件：选择建议时触发 `rich-input-select`，建议关闭后按 Enter 触发 `search`。
- 🧪 示例覆盖解析查询检查器、表单集成、`::part()` 主题、Logo 头像样式、自定义前置图标、动态 `<datalist>` 以及操作符/组合符/分隔符配置。

---

### [GitHub - paulmillr/chokidar：极简且](https://github.com/paulmillr/chokidar)

**原文标题**: [GitHub - paulmillr/chokidar: Minimal and efficient cross-platform file watching library · GitHub](https://github.com/paulmillr/chokidar)

Chokidar 是一个极简且高效的跨平台文件监听库（MIT 协议，作者 Paul Miller，GitHub 上获得 12.2k stars、638 forks），它通过统一各平台对 `fs.watch` 与 `fs.watchFile` 的差异，提供可靠、去重且路径规范的文件系统事件。该项目最初于 2012 年为 Brunch 而写，目前已被 3000 多万个项目使用，当前主要版本为 v6。

- 📁 **核心定位**：跨平台文件监听库；它监听给定的文件或目录，其中目录会被递归监听，可用于替代原生 `fs.watch` 与 `fs.watchFile`。
- 🩹 **解决原生痛点**：原生 `fs.watch` 会把许多变更报告为不透明的 rename 事件，同一次变更可能触发两次，而且递归监听在各平台上的行为不一致；Chokidar 将其规范化为经过验证、去重的 add/change/unlink（含 addDir/unlinkDir）事件。
- ⚙️ **后端选择**：默认使用原生 `fs.watch` 以降低 CPU 占用；也支持 `native`（每个目录一个订阅）、`native-recursive`，以及适用于网络或非标准文件系统的 `polling`（也提供 `pollingInterval`/`pollingBinaryInterval`）。
- 🧩 **常用选项**：`ignored`（支持精确字符串、正则或函数匹配器）、`ignoreInitial`、`followSymlinks`、`cwd`、`depth`、`persistent`、`ignorePermissionErrors`。
- ✍️ **编辑器与写入兼容**：`atomic`（默认 100ms 内把 unlink 加 add 合并为一次 change，并忽略 .swp、~ 等临时文件）与 `awaitWriteFinish`（等待文件大小稳定后再触发事件，适合大文件或分块写入）。
- 🚀 **快速上手**：`npm install chokidar`，然后 `chokidar.watch('src').on('all', (event, path) => ...)`；支持 ESM 与 CommonJS。
- 🔧 **主要方法**：`.add(paths)` 追加监听、`.unwatch(paths)` 同步取消监听、`.close()` 异步且终止性关闭，`.getWatched()` 返回监听映射。
- 📡 **事件模型**：`add`/`addDir`/`change`（可带 stats）、`unlink`/`unlinkDir`、`all`、`ready`（初始扫描完成）、`error`，以及不稳定的底层 `raw` 事件。
- 🛠️ **故障排查**：Linux 上的 ENOSPC 需要提高 inotify 监听上限（如 `max_user_watches=524288`）或缩小监听范围；EMFILE 需要减少监听、提高文件描述符上限，或改用 polling。
- 🕰️ **版本演进**：v6（2026 年 10 月）完全重写并引入递归 `fs.watch` 后端，要求 Node.js 22+；v5 仅支持 ESM；v4 移除 glob 支持与 fsevents 依赖，依赖数量从 13 降到 1。
- 🔄 **升级注意**：v4 起不再支持 glob，需改用 `ignored` 过滤或自行用 `node:fs/promises` 的 `glob` 展开；v6 中调用 `close()` 后，监听器不可复用，必须新建实例。
- 🌏 **名称由来**：源自印地语 चौकीदार（Chowkidar）的转写，意为“守夜人、看门人”。

---

### [发布 6.0.0 · pa](https://github.com/paulmillr/chokidar/releases/tag/6.0.0)

**原文标题**: [Release 6.0.0 · paulmillr/chokidar · GitHub](https://github.com/paulmillr/chokidar/releases/tag/6.0.0)

Chokidar 6.0.0 正式发布，本次更新围绕单一观察管道重写了文件监听核心，新增原生递归监听能力，并对 API 做出多项不兼容调整，要求 Node.js 22.22 或更高版本；同时修复了数十个长期存在的缺陷（含 macOS 句柄、Windows 重复事件、根目录监听等）。

- 🔄 **核心重写**：所有后端回调统一视为"失效信号"，须经 `lstat`、`stat` 或 `readdir` 确认后才发出事件，确保突发变更后的最终状态与文件系统一致。
- 🪟 **原生递归监听**：支持 `fs.watch({ recursive: true })`，默认 `auto` 后端在 macOS 与 Windows 上启用，其他平台仍按目录监听。
- 🔧 **句柄共享**：原生句柄在多个 watcher 间共享且仅按目录打开，文件不再持有句柄，修复 macOS 上监听大量文件时的 `EBADF` 错误（#1385、#1452）。
- ⏱️ **轮询自研**：以 Chokidar 自有的 stat 轮询替代 `fs.watchFile`，多个 watcher 按最快请求间隔共享轮询循环。
- 📦 **Node 版本要求**：最低需 Node.js 22.22。
- ⚙️ **新增 `backend` 选项**：可选 `'auto'`（默认）、`'native'`、`'native-recursive'`、`'polling'`；`usePolling: true` 成为 `backend: 'polling'` 的废弃别名。
- ✏️ **选项重命名**：`interval` / `binaryInterval` 改为 `pollingInterval` / `pollingBinaryInterval`，旧名保留为废弃别名，同名冲突时新名优先。
- 🔒 **`atomic` 默认值变更**：轮询模式下默认改为 `false`，显式设置则保留。
- 🛑 **`close()` 变为终态**：关闭开始后调用 `add()` 会抛错，需新建 watcher。
- ✅ **构造时校验**：非法的 `backend`、`atomic`、`depth`、`awaitWriteFinish` 及轮询间隔会抛出 `TypeError`。
- 🚨 **错误处理改进**：`add()` 中的错误改为触发 `error` 事件，不再产生未处理的 Promise 拒绝（#1378）。
- 🗂️ **`getWatched()` 返回无原型对象**：名为 `__proto__` 的目录也能被列出（#1493），建议改用 `Object.hasOwn()`。
- 🎯 **忽略规则调整**：`ignored` 不再作用于 `watch()` / `add()` 路径之上的目录，缺失路径仍可通过父目录被监听（#1374）。
- 🐞 **关键修复**：工作目录被删除导致的 100% CPU 死循环（#1474）、监听文件系统根目录时误报 `unlink`/`unlinkDir`（#1184、#452）、macOS 上 `/var/run` 的 `UNKNOWN` 错误（#1391）、符号链接 `ENOTDIR` 导致目录监听失效（#1476）。
- 🐞 **更多修复**：新加目录扫描与注册之间的文件漏检（#1471）、Windows 上兄弟文件写入误报 `change`（#1466）、重复 `add` 事件（#1465）、目录被同名文件替换导致挂起（#1464）、节流丢弃更新（#1455）、相对 `ignored` 路径解析（#1436）、WSL 中忽略项仍被监听（#1418）、Deno 下全量 `change`（#1417）等。
- 🧹 **其他**：`Stats` 改为仅类型导入（@zhennann，#1447），锁定开发依赖并收紧工作流权限（@43081j，#1457/#1460/#1461），取消监听的路径会保持忽略直至重新添加（#1439）。

---

### [GitHub - capricorn86/happy-dom：一个不含图形用户界面的 Web 浏览器的 JavaScript 实现 · GitHub](https://github.com/capricorn86/happy-dom)

**原文标题**: [GitHub - capricorn86/happy-dom: A JavaScript implementation of a web browser without its graphical user interface · GitHub](https://github.com/capricorn86/happy-dom)

happy-dom 是一个用 JavaScript 实现的、无图形用户界面的 Web 浏览器，主要用于前端测试环境，提供丰富的 DOM 与 Web 标准能力，并兼容主流测试工具和前端框架。

- 🌐 **项目定位**：由 capricorn86 维护的公开仓库，目标是在无 GUI 环境下模拟浏览器行为。
- 🧪 **测试用途**：可作为测试环境使用，文档包含入门指南与测试环境配置说明。
- 🧩 **DOM 能力**：支持 Custom Elements（Web Components）、Declarative Shadow DOM、Mutation Observer、Tree Walker、Fetch API 等。
- 🤝 **生态兼容**：可与 Vitest、Bun、Jest、Testing Library、Google LitElement、Vue、React、Svelte、Angular 等配合使用。
- 📊 **仓库数据**：约 4.7k Stars、356 Forks、11 Watchers、388 Issues、140 Pull Requests。
- 📄 **开源许可**：采用 MIT License，版权为 2019 至今 David Ortner。
- 🛠️ **协作支持**：提供贡献指南、行为准则和安全策略，仓库包含文档、集成测试、包目录及多种配置文件。
- 🏷️ **相关主题**：涵盖 angular、browser、bun、dom、html、javascript、jest、nodejs、react、svelte、testing-library、typescript、vitest、vue、web-components、whatwg 等。

---

### [发布 v21.0.0 · capricorn86/happy-dom · GitHub](https://github.com/capricorn86/happy-dom/releases/tag/v21.0.0)

**原文标题**: [Release v21.0.0 · capricorn86/happy-dom · GitHub](https://github.com/capricorn86/happy-dom/releases/tag/v21.0.0)

Happy DOM 发布 v21.0.0，主要破坏性变更是默认禁用 CSS 与 IFrame 加载，以缓解服务端请求伪造（SSRF）风险；如需保持旧行为，可显式开启相关设置。

- 💣 v21.0.0 包含破坏性变更，默认禁用 CSS 和 IFrame 加载。
- 🛡️ 修复 SSRF 风险：攻击者可在不可信 HTML 中嵌入 `<iframe>` 或 `<link rel="stylesheet">`，使 Happy DOM 从服务端向攻击者指定 URL（包括内部服务）发送 HTTP 请求。
- ⚠️ 设置项 `disableCSSFileLoading` 已被弃用。
- ⚙️ 新增设置项 `enableCSSFileLoading` 和 `enableIframePageLoading`。
- ✅ 若确认无风险，可通过 `new Window({ settings: { enableCSSFileLoading: true, enableIframePageLoading: true } })` 保持与 `<=v20.14.6` 相同的行为。
- 📅 由 `@capricorn86` 于 10 月 11 日 23:46 发布，提交经 GitHub 验证签名。
- 👍 该发布获得 1 个点赞反应。

---

### [GitHub - sindresorhus/p-queue：带并发控制的 Promise 队列 · GitHub](https://github.com/sindresorhus/p-queue)

**原文标题**: [GitHub - sindresorhus/p-queue: Promise queue with concurrency control · GitHub](https://github.com/sindresorhus/p-queue)

p-queue 是一个零依赖的 Promise 队列库，用于控制异步/同步任务的并发，适合限制 REST API 调用、CPU 密集型或内存密集型任务的执行速率；服务器端高可靠任务队列更推荐使用 Redis 支持的任务队列。项目已功能完整，主要接受 PR，不计划继续开发，并且仅提供原生 ESM。

- 📦 安装方式：`npm install p-queue`；仅支持原生 ESM，不支持 CommonJS。
- ⚙️ 核心配置：`concurrency` 控制并发数，`timeout` 设置任务超时，`autoStart` 控制是否自动启动，`queueClass` 支持自定义队列实现。
- 🚦 限流能力：`intervalCap` 与 `interval` 控制每个时间区间内启动的任务数；`strict` 使用滑动窗口；`carryoverIntervalCount` 让跨区间仍在运行的任务计入下一区间。
- 🧩 任务添加：`queue.add(fn, options)` 返回任务结果 Promise；`addAll()` 可批量添加，并按输入顺序返回全部结果。
- 🎯 任务选项：`priority` 设置优先级，`id` 用于后续调整优先级，`timeout` 可覆盖队列默认超时，`signal` 传入 `AbortSignal` 以取消任务。
- 🕹️ 队列控制：支持 `pause()`、`start()`、`clear()`；通过 `size`、`pending`、`isPaused`、`isRateLimited`、`isSaturated`、`runningTasks` 查看状态。
- ⏳ 等待与背压：提供 `onEmpty()`、`onIdle()`、`onPendingZero()`、`onRateLimit()`、`onRateLimitCleared()`、`onError()`、`onSizeLessThan()` 等等待方法。
- 🔔 事件系统：队列是 `EventTarget`，支持 `active`、`completed`、`error`、`empty`、`idle`、`pendingZero`、`add`、`next`、`rateLimit`、`rateLimitCleared` 等事件。
- 🛑 超时与取消：超时会中止任务 `signal` 并以 `TimeoutError` 拒绝；等待中的任务取消会被移除，运行中的任务取消会释放并发槽，但任务需自行处理信号。
- 🔍 调试与扩展：`runningTasks` 可识别卡住任务，`isSaturated` 可监测队列饱和；自定义 `queueClass` 可实现 FIFO 等调度；Jest 假定时器需额外刷新 Promise。
- 📈 使用建议：`concurrency` 与 `intervalCap` 是独立限制；严格外部 API 限流用 `strict`，背压可用 `onSizeLessThan()` 或 `onRateLimit()`。
- ⭐ 项目信息：MIT 许可，约 4.3k stars、224 forks、231 commits；相关库包括 `p-limit`、`p-map`、`p-throttle` 等。

---

### [发布 v10.0.0 · sindresorhus/p-queue · GitHub](https://github.com/sindresorhus/p-queue/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · sindresorhus/p-queue · GitHub](https://github.com/sindresorhus/p-queue/releases/tag/v10.0.0)

p-queue v10.0.0 是一次重大版本更新，包含多项破坏性变更：最低要求 Node.js 22，事件系统从 EventEmitter 改为 EventTarget，强化参数校验与错误处理，同时带来零依赖、异步上下文隔离、超时信号和大量限流、事件及类型修复。  
- 🚨 破坏性变更：最低要求 Node.js 22；队列改为 EventTarget，使用 addEventListener/removeEventListener，completed/error 的结果在 event.detail 中。  
- ⚠️ 事件监听器抛错会成为未捕获异常并退出进程；clear() 会让被移除任务的 Promise 以 AbortError 拒绝，需处理 addAll() 或 add().then() 的拒绝。  
- ⏱️ TimeoutError 改为名为 TimeoutError 的 DOMException；带 timeout 的任务会获得超时即中止的 signal，可传给 fetch() 等；移除 carryoverConcurrencyCount，改用 carryoverIntervalCount。  
- ✅ 更严格校验：concurrency 和 intervalCap 必须为整数或 Infinity；timeout/interval 超过 2147483647ms 会被拒绝；priority 为 NaN 或非数字时 add() 抛 TypeError。  
- 🔇 start()、clear() 和设置 concurrency 在队列已空时不再触发 empty/idle；自定义 queueClass 必须实现 remove()。  
- 📦 改进：零依赖；任务运行在 add() 调用的异步上下文中，可读取 AsyncLocalStorage 值；onEmpty()/empty 在最后一个等待任务开始时触发。  
- 🧩 addAll() 在任务返回不同类型时解析为类型化元组；修复大量限流 bug，如 intervalCap 超限、等待任务卡住、isRateLimited 错误等。  
- 🛠️ 修复共享 signal 下 add/run/abort 缓慢、PriorityQueue 内存保留、事件与优先级边界情况、undefined 选项和无效 timeout setter，以及大量 TypeScript 类型问题。  
- 🔄 迁移示例：queue.on('completed', result => ...) 改为 queue.addEventListener('completed', event => event.detail)；once 用 {once:true}；event.detail 对 undefined 结果为 null；重复监听同一函数只调用一次。

---

### [发布 v0.13.0 · paperjs/paper.js · GitHub](https://github.com/paperjs/paper.js/releases/tag/v0.13.0)

**原文标题**: [Release v0.13.0 · paperjs/paper.js · GitHub](https://github.com/paperjs/paper.js/releases/tag/v0.13.0)

Paper.js 发布 v0.13.0，包含 130 次提交，重点增强 SVG 导入导出、视图适配、文本与动画能力、Web Worker 支持，并修复大量命中测试、坐标变换、事件和兼容性问题。

- 🚀 新增 `View#update(force)` 强制重绘，以及 `View#fitBounds(rectangle[, fit])` 支持 `contain`/`cover` 适配。
- 🖼️ SVG 导出新增 `reuseImages`、`idPrefix`，导入新增 `crossOrigin`，并改进对 `<use>`、渐变、裁剪路径、数字 id、嵌套百分比和长度单位的处理。
- ✍️ 文本样式新增 `tracking`，以 `letter-spacing` 形式在 SVG 导入导出中读写；多行文本使用 `<tspan>` 保留基线。
- 🎞️ `Tween` 新增 Sine、Expo、Circ 系列的 `easeIn`、`easeOut`、`easeInOut` 缓动函数。
- 📐 新增 `View#project`、`Point#clamp(min, max)`；`Item#fitBounds()` 支持 `contain`、`cover`、`fill`。
- 🧵 Web Worker 中使用 `OffscreenCanvas`，使 `rasterize()`、`new Raster(size)`、透明度/混合模式和 CSS 颜色名可用；`Raster#toDataURL()` 仍不支持。
- 🖱️ 双击判定改为基于 `mousedown` 且 3 像素内，贴近原生 `dblclick`；修复鼠标/触摸坐标、键盘事件、视图旋转缩放等问题。
- 📦 设置 `Rectangle`/`Item#bounds` 的边或角时只移动对应边或拉伸，不再整体移动；移动项应使用 `bounds.point`、`center`、`x`、`y`。
- 🎯 命中测试改进：组在任一子项命中时可命中；修复变换组、符号项、点文本容差、描边端点等命中问题。
- 🎨 SVG/CSS 行为修正：内联 `style` 覆盖表现属性；图片保留原始像素并按 SVG 尺寸缩放；支持 SVG 2 的 `href`。
- ⚙️ `clone()`、布尔运算、`rasterize()`、`Path#toShape()`、`Shape#toPath()` 遵循 `settings.insertItems`；Node.js 使用 jsdom 的 `XMLSerializer` 输出合法 XML。
- 🔁 `Path#removeSegments(from, to)` 在闭合路径且 `from > to` 时环绕删除；`fitBounds()` 对空矩形/空项更稳健。
- 🧹 弃用 `Item#fitBounds()` 的布尔 `fill` 参数；移除旧 Chrome `mouseout` 兼容与 CLA；修复 `require('paper')`、PaperScript 打包、源码映射和内存泄漏等。
- 📝 文档补充/修正键盘事件、`Point/Size#negate()`、`PaperScope` 画布方法、命中测试默认值、布尔路径示例等内容。

---

### [发布 v0.14.0 · paperjs/paper.js · GitHub](https://github.com/paperjs/paper.js/releases/tag/v0.14.0)

**原文标题**: [Release v0.14.0 · paperjs/paper.js · GitHub](https://github.com/paperjs/paper.js/releases/tag/v0.14.0)

Paper.js v0.14.0 已发布（GitHub Actions 于 10 月 19 日发布，自 develop 分支累计 99 个提交）。本次更新主要新增宿主集成、事件分发、作用域访问、惰性文档支持和变更追踪能力，同时调整多边形、透明填充命中测试、JSON 导入等行为，并修复大量跨环境、渲染与事件相关问题。

- 🆕 `PaperScript.execute()` 新增 `options.handlers`，可导出 `onFrame`、`onResize` 和工具处理器之外的全局处理器，方便 Scriptographer 等宿主自行调用。
- 🖱️ 新增 `Tool#eventInterval`，按住鼠标时按间隔重复触发 `onMouseDrag`，即使鼠标不移动也会触发。
- 🔗 新增 `Project#scope`、`View#scope`、`Item#scope`、`Tool#scope`，便于从对象获取所属 `PaperScope`。
- 🎨 新增 `Group#isolated`，让组/图层的混合模式只在其内部生效，类似 CSS 的 `isolation: isolate`；新增 `settings.scaleStrokes`，可在应用矩阵时同步缩放路径和复合路径的描边宽度。
- 📦 新增 `paper-sourced.js` 构建、`Project#source` 和 `HostItem`，项目条目可由宿主文档惰性支撑，首次访问时才加载内容和子项。
- 🔄 新增 `Project#trackChanges` 与 `Project#takeChanges()`/`ChangeFlag`，宿主可只更新发生变化的条目。
- 🧩 新增 `View#dispatchMouseEvent()` 和 `View#dispatchKeyEvent()`，供无 DOM 的宿主（如 Worker）复用与 DOM 事件相同的鼠标/键盘处理流程。
- 📐 `Path.RegularPolygon()` 改为类似 Illustrator：平底放置，线段从顶部顶点逆时针排列；偶数边时从顶边右端开始，边数为 6 的倍数时会落在边上。
- 🎯 透明填充命中测试与 SVG 一致；`#hitTestAll()` 会按最近优先返回路径上容差内所有线段和控制柄，再返回描边或填充命中，并修复变换组内条目的坐标问题。
- 🧷 `paper.install()` 会保留目标作用域已有全局变量，PaperScript 不再用同名 Paper.js 类覆盖已有全局；`Item#importJSON()` 导入到已有条目时会重置 JSON 缺失字段，但保留场景图位置和事件处理器。
- 🐛 修复 Worker/Node.js 帧计时器不结束、Web Worker 中 `onFrame` 与 `PaperScope#execute()` 失效、无 DOM 视图等问题；修复 PaperScript 工具未为 `onActivate()`/`onDeactivate()` 等全局处理器创建工具的问题。
- 🖱️ 修复修饰键状态不同步、覆盖画布元素阻挡鼠标事件、触摸滚动异常、CSS 变换下视图尺寸错误、临时画布像素未释放等问题。
- 🖼️ 修复栅格 JSON 尺寸丢失、SVG 中 Paper.js 专有混合模式与斜体/字重导入导出、文本 `strokeScaling: false` 支持、无项目创建条目时报错不清晰等问题。

---

### [Paper.js](https://paperjs.org/)

**原文标题**: [Paper.js](https://paperjs.org/)

提供的文本仅包含单词“Source”，没有可供摘要的正文内容。

- 📄 内容仅为一个词：“Source”。
- ℹ️ 未提供文章主题、背景或具体细节。
- ❓ 因此无法提炼关键要点或生成有效摘要。

---

### [Paper.js — 示例](https://paperjs.org/examples/)

**原文标题**: [Paper.js — Examples](https://paperjs.org/examples/)

该内容汇总了一组图形编程、生成艺术与交互视觉示例，涵盖几何运算、路径处理、视觉效果、栅格动画、绘画创意以及命中测试和弹跳动画等主题。

- 🧩 几何与形状示例：Boolean Operations、Rounded Rectangles、Meta Balls、Voronoi。
- 🛤️ 路径与交互测试：Path Intersections、Path Simplification、Hit Testing、Smoothing。
- 🌈 彩虹与视觉特效：Nyan Rainbow、Radial Rainbows、Future Splash、Q-bertify。
- 🌀 栅格与动态图形：Spiral Raster、Division Raster、Chain、Tadpoles。
- 🎨 创意与绘画类示例：Candy Crash、Satie Liked To Draw。
- 🏀 动画与碰撞示例：Bouncing Balls。

---

### [](https://frankforce.com/littlejs-is-2d-and-3d-now/)

**原文标题**: [LittleJS is 2D and 3D now – Killed By A Pixel](https://frankforce.com/littlejs-is-2d-and-3d-now/)

LittleJS 发布迄今最大更新：在保持小巧、快速、无依赖的 HTML5 游戏引擎定位同时，新增完整 3D 渲染器、内置关卡编辑器、粒子效果库、更快核心和面向 AI 的开发工具，并可与 2D 游戏共享同一画布与对象系统。

- 🎮 **2D/3D 融合**：3D 网格、地形、体素、碰撞、阴影、灯光、雾、反射、粒子、相机和自定义着色器齐备，3D 对象沿用 2D 的物理、子对象和计时器机制，可自由混合 2D UI 与 3D 场景。
- 🧩 **Three.js 支持**：若偏好 Three.js 渲染，也提供相应插件。
- 💡 **2D 增强**：新增动态光照、单向平台、扫掠子弹碰撞、视差层，并提升对象碰撞性能。
- 🛠️ **内置关卡编辑器**：2D 和 3D 编辑器集成于引擎，调试版按 Escape 可暂停并就地编辑，支持撤销、自动保存和预制件；2D 关卡以 Tiled JSON 加载保存。
- ✨ **粒子效果库**：火焰、烟雾、火花、爆炸、雨等效果可一行调用，支持缩放、色相和饱和度调节，并提供粒子设计器。
- 🧪 **示例浏览器**：100 多个单文件示例，支持实时编辑和分享链接，是学习引擎的最佳入口。
- ⚡ **性能提升**：渲染核心重构为 WebGL2 批处理 2D 精灵和实例化 3D 绘制，减少每次绘制开销；基准测试中在作者机器上匹配或超过部分主流引擎。
- 🤖 **面向 AI 开发**：提供 AI 工具包、Claude Code 插件、LittleJS GPT 和 50+ 开源小游戏 Arcade，AI 可生成完整可玩项目。
- 🌱 **项目理念与社区**：坚持小而简单的通用引擎核心，3D 设计力求与 2D 同样易用；社区贡献持续增加，第三届 LittleJS Game Jam 于 10 月 2 日至 11 月 2 日举行。
- 🚂 **立即体验**：官网 littlejsengine.com 以列车旅程演示全部功能，并提供示例、文档、GitHub 和 Discord 入口。

---

### [Skia 画布](https://skia-canvas.org/)

**原文标题**: [Skia Canvas](https://skia-canvas.org/)

Skia Canvas 是一个无需浏览器、可在 Node.js 中运行的 headless 矢量图形渲染器与窗口工具包，基于 Chrome 使用的 Skia 引擎，兼容 Canvas API 并提供大量扩展，适合服务端生成图像和桌面交互式动画。

- 🎨 基于 GPU 加速的 Skia 引擎，依赖少，忠实模拟 canvas 标准并扩展 2D 能力。
- 🖼️ 支持矢量（PDF、SVG）与位图（JPEG、PNG、WEBP、RAW）输出，可保存文件、生成 dataURL、返回 Buffer 或 Sharp 对象。
- 📄 支持多页画布，输出多页 PDF 或图片序列；可加载 PDF/SVG，多页 PDF 可作为可编辑画布。
- 🌈 支持 Display P3 广色域和 CSS Color 4 语法，渐变可选择插值色彩空间。
- ✏️ 增强 Path2D 切片、采样、布尔运算与分解，支持 3D 透视变换、纹理/图案填充、自定义描边标记和 CSS 滤镜。
- 🔤 提供丰富排版控制：多行自动换行、逐行文本度量、OpenType 特性、字距/词距/行距、可变字体和本地非系统字体。
- ⚙️ 内置可配置工作线程池，支持异步渲染和文件 I/O，可在 Linux 及 Vercel、Cloudflare Containers、AWS Lambda 等无服务器平台渲染。
- 📦 安装简便：`npm install skia-canvas`；文档包含生成图片、多页序列、窗口渲染、广色域和 Sharp.js 集成示例。
- 🚀 基准测试显示其明显快于 canvas 与 @napi-rs/canvas，异步多线程模式提升显著；SVG 转 PDF 保持矢量，PDF 转 PNG 原生渲染更快，文本与渐变任务也表现更优。

---

### [如何检测 Meta 的 Muse AI 智能体流量](https://fingerprint.com/blog/how-to-detect-meta-muse-ai-agent/?utm_source=JSWeekly102026)

**原文标题**: [How to Detect Meta’s Muse AI Agent Traffic](https://fingerprint.com/blog/how-to-detect-meta-muse-ai-agent/?utm_source=JSWeekly102026)

概述总结  
Meta 的 Muse 是一款个人 AI 代理，可在云虚拟机的真实浏览器中代替用户操作网站；Fingerprint 已能通过 Bot Detection 将其识别为 `meta_muse`，帮助企业监控并制定针对 AI 代理的访问策略。

- 🤖 **Muse 能力**：可导航网站、输入密码、登录账户、浏览并使用优惠码，还能在用户简单指令后完成真实购买。
- 🕵️ **伪装普通访客**：Muse 在云虚拟机中运行真实浏览器，不申报身份、不提供可验证身份，并会修改浏览器指纹、压制常见自动化标记。
- 🚨 **安全挑战**：传统机器人检测依赖的自动化标志和身份声明可能失效，欺诈与安全团队需要识别“刻意混入普通流量”的 Muse。
- 🧠 **Fingerprint 识别**：Bot Detection Smart Signal 可直接标记推断为 Meta Muse 的自动化流量，并加入其已识别的 AI 代理名单。
- 📊 **检测结果字段**：包括 `bot_type: "meta_muse"`、`category: "ai_agent"`、`identity: "unknown"`，以及 `confidence` 可为 high、medium 或 low。
- ⚠️ **“bad bot”含义**：标记为 `"bad"` 是因为 Muse 未声明身份，并不单独代表恶意活动；无法确认身份的代理需逐步建立信任。
- 🛠️ **检测步骤**：安装 Fingerprint；查看 JS Agent 机器人检测；通过 Server API 或 MCP server 查找 `bot_type: "meta_muse"`；在仪表盘按名称 “Muse” 筛选；再用规则引擎或自有系统执行策略。
- 📈 **策略制定**：先理解流量结构，例如 VPN 使用比例、浏览器篡改信号、匿名浏览器回访比例，以及是否有人利用设备农场、反检测浏览器或自动化伪装成多个用户。
- 💰 **可用性**：已有 Bot Detection 的 Fingerprint 客户可免费获得 Muse 检测；功能正分批推出。非客户可免费开始使用或联系团队咨询集成。

---

### [面向开发者的视频后端 — 快速添加视频 | Hyperserve](https://hyperserve.io/?utm_source=javascriptweekly&utm_medium=newsletter&utm_campaign=classified_oct13)

**原文标题**: [Video backend for Developers — Add Video Fast | Hyperserve](https://hyperserve.io/?utm_source=javascriptweekly&utm_medium=newsletter&utm_campaign=classified_oct13)

Hyperserve 是面向开发者的视频托管 API，帮助应用快速接入视频上传、转码、CDN 托管与播放 URL 交付，避免自建复杂后端、播放器锁定和不可控账单。

- 🎯 核心价值：接受用户上传的任意视频格式，自动转码并全球分发，简化视频基础设施。
- 🧩 集成流程：后端创建上传任务，客户端直传存储且无需 API Key，后端完成上传后触发转码。
- ⚙️ 解决痛点：处理转码失败、生产环境首帧过慢、转码 Worker 扩展与任务队列问题。
- 🔁 标准管道：上传 → 转换 → 托管 → 交付；通过 Webhook 通知处理成功并返回各分辨率视频 URL。
- 🚫 降低风险：无播放器锁定，开发者自建 UI；无需视频专业知识；按用量定价，无最低消费或承诺。
- 📥 输入支持：单文件最高 5GB，支持 MP4、MOV、AVI、MKV、WEBM、WMV、M4V、MPG。
- 📤 输出支持：输出 MP4，分辨率覆盖 144p 至 8K，并按设备优化。
- 🧑‍💻 适用场景：社交与创作者内容、市场平台、SaaS 与内部工具、健康与健身应用。
- 💰 定价方案：免费版含每月 50 个视频、1GB/文件、250GB 带宽、免费编码和完整 API；按量付费为 $0.04/GB 存储、$0.025/GB 带宽。
- 📚 开发体验：文档清晰、代码可复制，提供创建/上传/查询/删除视频等 API，并支持 Webhook、自定义元数据等能力。
- 🚀 行动号召：可免费开始，一个下午完成集成并上线视频功能。

---

### [Firefox 158 开发者发行说明（稳定版） - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/158)

**原文标题**: [Firefox 158 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/158)

Firefox 158 稳定版于 2026 年 10 月 13 日发布，为 Web 开发者、附加组件开发者和自动化测试带来多项更新，包括 CSS 类型化算术、JPEG XL 默认支持、WebGPU/WebTransport/WebDriver BiDi 增强，以及多项默认关闭的实验功能。

- 📅 **发布日期**：Firefox 158 于 2026 年 10 月 13 日发布。
- ♿ **无障碍**：Firefox for Android 现已支持 `aria-busy` 属性，便于辅助技术在内容更新完成后通知用户。
- 🧮 **CSS**：支持 CSS 类型化算术，可用 `calc()` 等函数对不同单位但同数据类型的值进行除法并得到无单位商。
- 🖼️ **HTTP/图片格式**：图片请求默认 `Accept` 头新增 `image/jxl`；JPEG XL（`image/jxl`）默认启用，支持有损/无损压缩、透明、动画、HDR，并可无损转码 JPEG。
- 🌐 **API 增强**：新增 `WebTransport.getStats()`、`WebTransport.supportsReliableOnly`、通知 `navigate` 选项、`PerformanceResourceTiming.deliveryType` 等支持。
- 🎮 **WebGPU/WebGL**：支持 `float32-blendable`；macOS 支持 `clip-distances`；兼容设备新增 WebGL `EXT_polygon_offset_clamp` 扩展。
- 🧩 **DOM/HTML Sanitizer**：`SVGGraphicsElement.getBBox()` 对 `<tspan>` 和 `<textPath>` 支持 `fill`/`stroke` 选项；HTML Sanitizer API 新增 `javascriptURLs` 配置及 `Sanitizer.setJavascriptURLs()`。
- 🎥 **WebRTC/媒体**：发送 H.264 或 AV1 视频时，Firefox 会按协商的编解码级别自动降低分辨率和帧率；`MediaCapabilities.encodingInfo()` 相应报告 `webrtc` 配置为支持。
- 🧪 **WebDriver 一致性**：WebDriver BiDi 和 Marionette 支持设置摄像头/麦克风权限；自动化中触摸起始/移动容差改为零；BiDi 截图支持 `imageSize`，录屏支持 `destinationFolder`；Marionette 截图宽高为零时返回错误。
- 🧱 **附加组件开发**：`publicSuffix.isKnownSuffix()` 传入无效主机名时改为抛错；新增 `runtime.getVersion()` 返回 manifest 中声明的扩展版本。
- ⚗️ **实验性功能（默认关闭）**：包括 CSS `random()`、`corner-shape` 属性、`import defer`/`import.defer()`、桌面端本地语音识别、Speculation Rules 的 `moderate` 预取、流式请求体，以及 `CSSNumericValue.equals()`。

---

### [面向 Web 用例的 JPEG XL 与 AVIF 对比 - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

**原文标题**: [JPEG XL vs AVIF for web use-cases - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

JPEG XL 已进入所有主流浏览器，作者基于多类图片和多种编码器设置，比较 AVIF 与 JPEG XL 在网页场景中的文件大小、画质、编码/解码速度与内存。总体看，AVIF 更适合大多数网页有损照片、截图、插画和透明图；JPEG XL 在无损、JPEG 无损转码及少数图像上更强。当前建议默认使用 AVIF 4:4:4，并采用可接受的高 effort；若 AVIF 文件异常大，再用 jixel 编码的 JPEG XL 对比测试。

- 📷 **有损照片**：AVIF 通常更小；默认 effort 下最佳 JPEG XL 约大 15–25%，最大 effort 下约大 6–20%，但存在 JPEG XL 反超的离群图。
- ⚙️ **编码器差异**：jixel 通常比 libjxl 生成更小文件，但个别案例疑似“迎合指标”且视觉更差；详细透明图除外。
- 🧾 **截图与插画**：AVIF 明显占优；JPEG XL 默认 effort 约大 30–90%，最大 effort 约大 20–70%。有损 AVIF 通常足够，无需 lossless。
- 🫥 **透明图像**：AVIF 明显更好；libjxl 默认大 31–44%、最大大 61–70%；jixel 透明通道无损，文件可达 AVIF 的 2–3 倍。
- ⏱️ **编码效率**：按文件大小综合看，AVIF 编码更快、内存更省；jixel 虽快但文件通常明显更大。
- 🔍 **解码速度**：AVIF 更快；JPEG XL 中等质量约慢 2–3 倍，极高质量差距缩小，Chrome 有时可反超。
- 📈 **effort 设置**：AVIF 提高 effort 值得；jixel 提升到 slow 值得，extraslow 收益小成本高；libjxl 高 effort 基本不值得。
- 🎨 **色度采样**：AVIF 4:2:0 很少显著减小文件，还会限制高质量；无暇逐图测试时建议默认 4:4:4。
- ✅ **质量稳定性**：固定质量设置下，各编码器的 SSIMULACRA2 波动方向一致，未发现单一质量设置不可靠的证据。
- 🌀 **渐进式加载**：JPEG XL 高 effort 下渐进预览几乎免费，但可能让用户误以为图片已加载完但画质差；AVIF 渐进目前仅 Chrome 支持，控制力更强、通常更小且解码更快。
- 🌈 **HDR**：JPEG XL 格式支持 gain map，但浏览器不支持且编码流程混乱；AVIF gain map 在极端亮度下体验更好。非 gain map 的 PQ HDR 中 JPEG XL 常更小，但指标分歧大。
- 🔄 **JPEG 转码**：JPEG XL 可将现有 JPEG 无损缩小 9–20%，大图解码有时更快，小图略慢。
- 🗜️ **无损压缩**：JPEG XL 明显胜出；WebP 约大 9–17%，AVIF 约大 30–120%，但网页通常不需要无损。
- 🎞️ **动画图像**：不建议使用动画 AVIF/JPEG XL；视频格式在编码、播放和体积上更合适。
- 🧪 **最终建议**：默认 AVIF 4:4:4 + 可接受的高 effort；若 AVIF 文件异常大，再试 jixel 的 JPEG XL。网上与 AI 存在不少误导信息，应以自己的图片实测为准。
- 🛠️ **测试方法**：使用 avifenc 1.4.2、libjxl 0.12.0、jixel 0.4.2、cwebp 1.6.0；多数图像宽 1598px，在 M4 Pro MacBook Pro 上以 SSIMULACRA2 等指标基准测试。

---

### [JXL 艺术画廊 – JPEG XL](https://jpegxl.info/art/big_gallery.html)

**原文标题**: [JXL Art gallery – JPEG XL](https://jpegxl.info/art/big_gallery.html)

该内容介绍了一个 JXL 艺术画廊：HDR 作品被单独放在另一页面，以免观看时过亮刺眼；画廊共收录 194 张嵌入图片，总像素约 391.0 百万，合计仅 8,168 字节（7.98 KiB），整体比特率约为 0.0001671 bits per pixel，并按 2021 至 2025 年分类展示大量极小体积的 JPEG XL 艺术作品。

- 🖼️ 画廊共包含 194 张嵌入图片，总像素约 391.0 百万，体现极高的压缩效率。
- 💾 全部图片合计仅 8,168 字节（7.98 KiB），整体比特率约为 0.0001671 bits per pixel。
- 🌈 HDR 作品另设独立页面，避免因画面过亮而刺眼。
- 📅 作品按 2021、2022、2023、2024、2025 年份分区展示。
- 🧑‍🎨 主要作者包括 Jon Sneyers，也有 jjido、CrushedAsian255、Lonnie、MSLP、Retr0id、Tirr 等贡献者。
- 🎨 题材涵盖抽象纹理、几何图案、旗帜、自然与天空、像素风、故障艺术、极简生成艺术等。
- 🔍 每件作品标注年份、作者、格式 image/jxl、文件字节数与来源链接。
- ⚡ 许多作品仅 21 至 100 多字节，突出 JPEG XL 在极小文件体积下的艺术表达与实验性。

---

### [](https://www.youtube.com/playlist?list=PLHJJhUxJCR0c)

**原文标题**: [nodeconfeu 2026 - YouTube](https://www.youtube.com/playlist?list=PLHJJhUxJCR0c)

该文本主要是 YouTube 页面底部的网站导航和版权信息，并包含页面标题“nodeconfeu 2026 - YouTube”，没有提供具体文章正文内容。

- 🧭 包含“关于、新闻、版权、联系我们”等基础导航链接。
- 👥 列出“创作者、广告、开发者”等平台相关入口。
- 📜 提供“条款、隐私、政策与安全、YouTube 工作原理”等政策说明链接。
- 🧪 提及“测试新功能”入口。
- ©️ 版权信息显示为“© 2026 Google LLC”。
- 🎬 页面标题为“nodeconfeu 2026 - YouTube”。

---

### [](https://www.youtube.com/watch?v=cKjSAh7wuyw)

**原文标题**: [James M Snell | A common minimum Node.js subset for all runtimes - YouTube](https://www.youtube.com/watch?v=cKjSAh7wuyw)

这是 Google/YouTube 页面底部的导航与版权信息，主要汇集公司介绍、联系渠道、创作者与广告及开发者入口，以及条款、隐私、安全和功能测试等链接。

- 🏢 包含“关于”“新闻”“联系我们”等公司信息入口。
- 👥 提供创作者、广告合作与开发者相关链接。
- 📜 列出条款、隐私、政策与安全等法律与合规页面。
- ⚙️ 包含“YouTube 工作原理”和“测试新功能”入口。
- ©️ 版权信息显示为 © 2026 Google LLC。

---

### [Caio Lima | V8 堆管理概述 - YouTube](https://www.youtube.com/watch?v=dYvGvWPcEYk&list=PLHJJhUxJCR0c&index=25)

**原文标题**: [Caio Lima | Overview of V8 heap management - YouTube](https://www.youtube.com/watch?v=dYvGvWPcEYk&list=PLHJJhUxJCR0c&index=25)

该文本是 YouTube 网站页脚与导航链接集合，主要涵盖平台介绍、联系渠道、创作者与开发者资源、广告合作、法律政策及版权信息。

- ℹ️ 提供“关于”“新闻”“联系我们”等基础信息入口。
- 👥 包含创作者、广告投放和开发者相关资源链接。
- 📄 列出服务条款、隐私、政策与安全等法律与规范链接。
- ▶️ 提供 YouTube 运作方式及新功能测试入口。
- ©️ 标注版权归 Google LLC 所有，年份为 2026。

---

### [Guy Bedford | 提升 Emscripten、WebAssembly 和 Rust 的能力 - YouTube](https://www.youtube.com/watch?v=nNlqco5xd20&list=PLHJJhUxJCR0c&index=23)

**原文标题**: [Guy Bedford | Improving the capabilities of Emscripten, WebAssembly and Rust - YouTube](https://www.youtube.com/watch?v=nNlqco5xd20&list=PLHJJhUxJCR0c&index=23)

该文本是 YouTube 页面底部的导航链接与版权信息，主要用于提供平台相关入口、政策说明及公司版权声明。

- 📌 包含“关于、新闻、版权、联系我们”等基础信息入口。
- 👥 提供“创作者、广告合作、开发者”等平台相关链接。
- 📜 包含“条款、隐私、政策与安全、YouTube 工作原理”等政策与说明入口。
- 🧪 提到“测试新功能”入口。
- ©️ 版权信息为“© 2026 Google LLC”。

---

### [热门 - /dev/null](https://dev-null.sh/)

**原文标题**: [Trending - /dev/null](https://dev-null.sh/)

/dev/null 社区近期动态活跃：平台推出“零垃圾”管理政策、移动端体验获好评，并突破 1 万用户；PHP 创始人 Rasmus Lerdorf 入驻，同时一则影响 PHP 5+ 的高危安全漏洞预告引发安全社区高度关注。

- 🚫 平台宣布“zero-crap”政策：违规者会被 timeout，累计 3 次将开始考虑封禁。
- 📱 用户称赞移动端 UI 非常出色，团队表示对 Android、iOS、WebKit 的兼容性问题做了额外优化。
- 🎉 社区用户数突破 10,000，创始人称“难以置信”并感谢所有用户。
- 🧑‍💻 PHP 创始人 Rasmus Lerdorf 入驻，被社区称为“传奇人物”。
- 🚨 PHP 安全团队预告 2026 年 10 月 21 日 14:00 UTC 发布安全更新，修复两个 CVSS v4.0 9.2 的严重漏洞；社区还有影响 PHP 5+ 的 RCE 传言，安全研究人员高度戒备。
- 🐦 有人分享终端版 Flappy Bird 开源项目，支持 wasm、原生运行及多种玩法。
- 🤖 社区讨论机器人或代理账号是否应限制为仅回复；Tom 表示自己是目前唯一已知的机器人。
- 📦 Mojo 仓库每日快照更新，主分支新增 84 个提交；/dev/null 也可通过 GitHub Action 自动发帖。
- 🧰 开发者讨论 Pi 与 OpenCode 的区别：Pi 更极简、无 MCP，OpenCode 则是工具齐全的即用型方案。
- 🗳️ 平台登上 Product Hunt，社区用户纷纷投票支持。

---

### [彼得·库珀 (@](https://dev-null.sh/@peterc)

**原文标题**: [Peter Cooper (@peterc) - /dev/null](https://dev-null.sh/@peterc)

Peter Cooper（@peterc）是 GitHub 用户 #118、CooperPress 开发者通讯发布者，也是 Lv.4 维护者；他关注 agentic coding、LLM 与钢琴，近 7 天有 37 次提交、45 个关注、53 个粉丝，并拥有 739/1000 XP。其动态涵盖开源项目、产品反馈、社区互动与技术闲聊。

- 👤 个人简介：Peter Cooper 是 CooperPress 开发者通讯发布者，GitHub 用户 #118，自称“Dad ×3”，活跃于 agentic coding、LLM 和钢琴领域。
- 📈 活跃数据：近 7 天 37 次提交，当前连续活跃 2 天，Lv.4 维护者，739/1000 XP，已解锁 6/13 个成就。
- 🤖 Mistral 动态：他提到 Mistral 新时间序列预测模型 Timestral，并尝试把巴赫 MIDI 当作数值输入，得到有趣的音乐化结果。
- 🎥 直播功能讨论：他询问 Tom 能否查看正在直播的用户；Tom 表示无法访问在线状态或直播数据，社区成员则讨论增加“Live”标签或侧边栏。
- 🧠 开源项目：发布 19 年历史的 Ruby 自然语言检测库 whatlanguage v3.0，可识别 160+ 种语言。
- 🎹 钢琴合成器：开源物理建模钢琴合成器 coopiano，使用 C++17，支持离线 WAV 渲染和 macOS 实时 MIDI。
- 🎬 ZXN 反馈：他试用 ZXN 后询问是否支持裁剪录制画面；Tilly The Coder 表示相关更新正在部署。
- 🏴‍☠️ 趣味指令：他让 Tom 在接下来 10 条消息中用海盗风格英语说话，Tom 以海盗语气回应。
- ⚔️ 经典争论：他发起“tabs 还是 spaces”讨论，回复中出现 spaces、newlines，也有人建议让 Claude 与 OpenAI 持不同立场以延续争论。
- 💻 代码分享：他分享了一段 1987 年的短汇编代码，并称这是自己最喜欢的简短代码片段之一。
- 🌱 根提交说明：该内容被标记为“@peterc 的 root commit”。

---
