### [Node 周刊第 592 期：2025 年 9 月 9 日](https://nodeweekly.com/issues/592)

**原文标题**: [Node Weekly Issue 592: September 9, 2025](https://nodeweekly.com/issues/592)

npm生态系统遭受重大供应链攻击，涉及流行包被入侵；Cloudflare Workers支持Node HTTP服务器；Node.js版本更新及多项工具发布。

- 🚨 npm生态系统遭受供应链攻击，Chalk、debug等流行包被入侵
- 🔧 Cloudflare Workers现已支持node:http客户端和服务器API
- 📦 Node.js v20.19.5 LTS发布，主要包含错误修复和依赖更新
- 🛡️ LavaMoat工具可沙箱化依赖项以增强安全性
- 🤖 CodeRabbit提供VS Code免费AI代码审查功能
- 📚 NodeBook新书深入探讨Node内部机制和V8引擎
- 📊 Intl.Segmenter可解决文本长度计算不准的问题
- 🐳 开发者分享弃用Docker转用Podman的经验
- 🛠️ 多项工具更新：Mediabunny媒体工具包、Prisma ORM、Electron等
- 🌐 JavaScript生态系统动态：浏览器定时器限制、Andromeda新运行时、JS会议日程等

---

### [npm 作者 Qix 因钓鱼邮件在重大供应链攻击中受侵](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

**原文标题**: [npm Author Qix Compromised via Phishing Email in Major Suppl...](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

DuckDB的npm账户遭受入侵，成为持续供应链攻击的最新受害者，多个软件包被植入相同的钱包盗取恶意软件。

- 🚨 DuckDB的npm账户遭入侵，供应链攻击持续蔓延
- 📦 多个软件包被植入相同钱包盗取恶意软件
- ⚠️ 攻击者通过账户接管方式实施恶意代码注入
- 🔒 开源软件供应链安全再次面临严峻挑战

---

### [npm钓鱼邮件利用拼写错误域名瞄准开发者...](https://socket.dev/blog/npm-phishing-email-targets-developers-with-typosquatted-domain)

**原文标题**: [npm Phishing Email Targets Developers with Typosquatted Doma...](https://socket.dev/blog/npm-phishing-email-targets-developers-with-typosquatted-domain)

Socket CEO Feross Aboukhadijeh在Risky Business Weekly播客中讨论了npm供应链攻击的现状、潜在风险及应对策略。

- 🎧 Feross做客播客解析npm钓鱼攻击事件
- 📦 强调近期供应链攻击实际影响有限
- ⚠️ 警告若攻击手段升级可能造成更大风险
- 🛡️ 探讨供应链安全防护措施的重要性
- 🔍 指出开源生态系统中依赖管理的脆弱性

---

### [DuckDB npm账户在持续供应链攻击中遭入侵](https://socket.dev/blog/duckdb-npm-account-compromised-in-continuing-supply-chain-attack)

**原文标题**: [DuckDB npm Account Compromised in Continuing Supply Chain At...](https://socket.dev/blog/duckdb-npm-account-compromised-in-continuing-supply-chain-attack)

npm作者Qix的账户因钓鱼邮件遭到入侵，导致多个流行包被发布恶意版本，引发供应链安全风险。

- 🎣 钓鱼邮件导致账户凭证泄露
- ⚠️ 恶意版本被发布到chalk-template、color-convert等热门包
- 🔐 供应链攻击影响下游开发者
- 📅 事件发生于2025年9月8日
- 👥 由多位安全研究人员联合披露

---

### [DuckDB NPM包1.3.3和1.29.2版本遭恶意软件入侵 · 安全通告 · duckdb/duckdb-node · GitHub](https://github.com/duckdb/duckdb-node/security/advisories/GHSA-w62p-hx95-gf2c)

**原文标题**: [DuckDB NPM packages 1.3.3 and 1.29.2 compromised with malware · Advisory · duckdb/duckdb-node · GitHub](https://github.com/duckdb/duckdb-node/security/advisories/GHSA-w62p-hx95-gf2c)

DuckDB的Node.js npm包遭受恶意软件攻击，涉及四个包的特定版本，团队在四小时内发现并采取措施处理，包括废弃受影响版本、联系npm删除并发布安全版本。

- 🚨 DuckDB的四个npm包（@duckdb/node-api@1.3.3、@duckdb/node-bindings@1.3.3、duckdb@1.3.3、@duckdb/duckdb-wasm@1.29.2）被注入恶意代码，旨在干扰加密货币交易
- 🕵️♂️ 攻击通过钓鱼网站实施，伪装成npm官网骗取维护者登录信息和2FA，并添加API令牌发布恶意版本
- ⏱️ 团队在四小时内发现攻击，立即废弃受影响版本并联系npm删除恶意包
- 🔒 发布更高版本（1.3.4/1.30.0）作为安全替代，并重置密码、令牌和API密钥
- 📅 事件发生于2025年9月8日，当前DuckDB正式版本为1.3.2，1.4.0计划于9月10日发布
- ⚠️ 严重性评级为高（CVE-2025-59037），团队道歉并审查内部流程以防止未来发生

---

### [Bluesky上的@bad-at-computer.bsky.social](https://bsky.app/profile/bad-at-computer.bsky.social/post/3lydioq5swk2y)

**原文标题**: [@bad-at-computer.bsky.social on Bluesky](https://bsky.app/profile/bad-at-computer.bsky.social/post/3lydioq5swk2y)

这是一个关于用户账户安全事件的帖子，用户因钓鱼邮件导致NPM账户被盗。  
- 🔐 用户因看似真实的2FA重置邮件导致账户被入侵  
- 📦 仅NPM账户受影响，已联系官方寻求恢复访问  
- 😔 用户承认因近期压力大而疏忽，承诺尽快解决问题  
- ⚠️ 事件发生在2025年9月8日，涉及虚假身份验证邮件攻击

---

### [发布到 npm 的 5.6.1 版本存在安全问题（已解决）· Issue #656 · chalk/chalk · GitHub](https://github.com/chalk/chalk/issues/656)

**原文标题**: [Version 5.6.1 published to npm is compromised (RESOLVED) · Issue #656 · chalk/chalk · GitHub](https://github.com/chalk/chalk/issues/656)

chalk项目版本5.6.1在npm发布时被植入恶意代码，现已解决。  
- 🚨 5.6.1版本存在恶意载荷（位于src/index.js第11行）  
- 🔄 问题与debug-js/debug#1005情况相同  
- 👍 63人确认问题存在  
- ⚠️ 2人对情况表示困惑  
- 👁️ 15人持续关注进展  
- 📦 漏洞通过npm包分发渠道传播

---

### [infowski: "好吧，又是npm恶意软件频发的一天。看起来…" - 华沙黑客空间社交俱乐部](https://social.hackerspace.pl/@informatic/115168929981581855)

**原文标题**: [infowski: "OK, so... Another day, another npm malware.
Seems…" - Warsaw Hackerspace Social Club](https://social.hackerspace.pl/@informatic/115168929981581855)

要使用Mastodon网页应用，需启用JavaScript或下载平台专用原生应用。  
- 🚫 需启用JavaScript才能运行网页版  
- 📱 可下载各平台专用原生应用替代使用

---

### [npm debug与chalk包遭恶意入侵](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised)

**原文标题**: [npm debug and chalk packages compromised](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised)

npm生态系统中18个高下载量的流行包（包括debug和chalk）于2025年9月8日被恶意代码注入，这些包每周总下载量超过20亿次。攻击者通过钓鱼邮件获取维护者账户权限后发布恶意版本，代码会在用户浏览器中静默拦截并篡改加密货币和Web3活动，将支付地址重定向到攻击者控制的账户。恶意代码通过劫持fetch、XMLHttpRequest和钱包API实现隐蔽攻击，目前部分包仍处于受控状态，建议立即检查版本并清理依赖。

- 🚨 **攻击范围**：涉及18个高频npm包（包括ansi-styles每周3.7亿次下载）
- 📧 **入侵手段**：攻击者伪装成npm官方支持（npmjs.help域名）发送钓鱼邮件
- ⚙️ **恶意行为**：注入的代码会篡改交易地址、钱包授权和网络响应数据
- 🌐 **多链攻击**：支持以太坊、比特币、Solana、波场等主流链的地址替换
- 🔍 **隐蔽技术**：使用字符串相似度算法替换为相似地址降低用户警觉
- ⚡ **响应状态**：维护者已删除大部分受污染版本，但simple-swizzle包仍存在风险
- 🛡️ **防护建议**：清理npm缓存、锁定依赖版本、使用Aikido SafeChain进行安全检测

---

### [GitHub - naugtur/运行齐克斯恶意软件](https://github.com/naugtur/running-qix-malware)

**原文标题**: [GitHub - naugtur/running-qix-malware](https://github.com/naugtur/running-qix-malware)

该仓库演示了如何通过LavaMoat防护机制阻止NPM恶意软件包"is-arrayish"的供应链攻击，该恶意软件会劫持加密货币交易地址。

- 🚨 演示了恶意包"is-arrayish 0.3.3"会劫持fetch、XMLHttpRequest和以太坊交易请求，替换收款地址
- 🛡️ 使用LavaMoat的隔离策略可阻止恶意代码执行，抛出"object is not extensible"错误
- ⚠️ 攻击影响有限，部分交易记录显示用户通过无效转账嘲讽攻击者
- 📦 通过@lavamoat/webpack插件实现依赖包隔离，限制各包全局对象访问权限
- 🔗 包含实际代码演示和防护机制实现原理说明
- 📝 项目采用MIT许可证，包含6次提交记录和43个星标

---

### [GitHub - LavaMoat/LavaMoat：用于沙盒化依赖图的工具集](https://github.com/LavaMoat/LavaMoat)

**原文标题**: [GitHub - LavaMoat/LavaMoat: tools for sandboxing your dependency graph](https://github.com/LavaMoat/LavaMoat)

LavaMoat是一套用于保护JavaScript项目免受软件供应链攻击的工具集，通过沙箱化依赖关系图来增强安全性。

- 🛡️ 防止恶意依赖窃取敏感数据或使应用易受攻击
- 🔧 提供安装时、构建时和运行时的多层次防护
- ⚙️ 允许通过配置控制依赖生命周期脚本的执行
- 🏗️ 使用SES沙箱限制包对平台API的访问权限
- 🌐 支持Node.js和浏览器环境的安全运行
- 📊 提供依赖图可视化工具（当前未维护）
- ⚠️ 提供高级安全功能scuttling（默认关闭）
- 📚 由MetaMask开发，ConsenSys资助，基于Agoric技术

---

### [使用政策 | LavaMoat](https://lavamoat.github.io/guides/policy/)

**原文标题**: [Using Policies | LavaMoat](https://lavamoat.github.io/guides/policy/)

LavaMoat策略用于控制应用程序依赖树中所有直接和间接依赖包对资源的访问权限，包括全局对象、内置模块和外部包。策略通过自动生成的policy.json和手动创建的policy-override.json文件管理，前者记录依赖包当前使用的资源快照，后者用于调整权限。策略采用允许列表机制，不支持拒绝列表方式，且需要将策略文件纳入版本控制。

- 🛡️ 策略定义：策略对象规定依赖包可访问的资源类型，包括全局变量、内置模块和外部包
- 📁 策略文件：policy.json由工具自动生成，policy-override.json用于手动调整权限
- ⚠️ 安全审查：需要定期审查自动生成的策略文件，可能发现可疑权限
- 🔧 权限调整：通过override文件授予缺失权限或限制过度权限
- 🌳 依赖追踪：使用规范名称标识包，防止恶意包冒名获取权限
- 🔒 精细控制：支持属性级权限控制，可限制对强大对象的特定字段访问
- 📊 运行时合并：运行时将override文件内容合并到自动生成的策略中
- ❌ 非拒绝列表：策略采用允许列表机制，不支持通过否定语句实现拒绝功能
- 📦 版本控制：建议将策略文件纳入版本控制以便审计和比较变更

---

### [将Node.js HTTP服务器引入Cloudflare Workers](https://blog.cloudflare.com/bringing-node-js-http-servers-to-cloudflare-workers/)

**原文标题**: [Bringing Node.js HTTP servers to Cloudflare Workers](https://blog.cloudflare.com/bringing-node-js-http-servers-to-cloudflare-workers/)

Cloudflare Workers 现在支持 Node.js 的 `node:http` 客户端和服务器 API，使开发者能够直接在边缘网络运行现有的 Express.js、Koa 等 Node.js 应用，无需重写代码即可享受零冷启动、自动扩展和低延迟的优势。

- 🌐 支持在 Cloudflare Workers 上运行 Node.js HTTP 服务器和客户端 API
- 🔌 基于标准 `fetch()` API 实现 `node:http` 客户端功能（GET、POST 等）
- 🚫 当前不支持 Agent API、Trailers 和 TLS 特定选项
- 🌉 提供两种集成方式：手动 `handleAsNodeRequest` 和自动 `httpServerHandler`
- ⚡ 支持 Express.js 和 Koa.js 等流行框架的无缝迁移
- 🚀 通过 `nodejs_compat` 兼容性标志启用此功能
- 🌍 充分利用 Workers 的全球网络和自动扩展能力

---

### [在Cloudflare Workers上运行Express.js](https://jross.me/run-express-js-on-cloudflare-workers/)

**原文标题**: [Run Express.js on Cloudflare Workers](https://jross.me/run-express-js-on-cloudflare-workers/)

Cloudflare Workers 自2025年8月5日起通过wrangler 4.28.0版本原生支持Express.js应用，显著提升了Node.js兼容性，允许开发者直接在本地开发环境中运行Express应用（生产环境支持即将推出），并利用Cloudflare生态系统的高效工具。

- 🚀 Cloudflare Workers现支持原生运行Express.js应用，降低Node.js开发者迁移门槛
- ⚙️ 通过启用`enable_nodejs_http_server_modules`兼容性标志和`httpServerHandler` API实现HTTP服务器支持
- 💻 示例代码展示Express应用与Workers环境集成，包括路由处理和KV存储操作
- 📝 需在wrangler.toml中配置Node.js兼容性标志和实验性功能以启用支持
- 🔄 建议现有Hono用户无需立即迁移，但Node.js老项目可快速适配Workers
- 🌟 Cloudflare持续改进Node.js兼容性，推动跨运行时应用开发

---

### [Node.js 兼容性 · Cloudflare Workers 文档](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)

**原文标题**: [Node.js compatibility Â· Cloudflare Workers docs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)

Cloudflare Workers 提供 Node.js 兼容性支持，通过内置 API 和 Wrangler 注入的 polyfill 实现 npm 包的使用，需配置兼容性标志和日期。

- 🚀 启用 Node.js 兼容性需在 Wrangler 配置中添加 `nodejs_compat` 标志并设置兼容日期为 2024-09-23 或之后
- 📦 Workers 运行时原生支持多数 Node.js API（如 Buffer、Crypto、HTTP），但文件系统、OS 等暂不支持
- ⚠️ 未支持的 API 通过 Wrangler 注入模拟 polyfill，调用时会抛出未实现错误
- 🎯 可单独启用 `nodejs_als` 标志仅支持 AsyncLocalStorage API
- 🔧 部分 API 支持有限（如 Performance hooks、TLS/SSL 为部分支持）
- 💡 用户可通过 GitHub 讨论区请求新增 API 支持

---

### [零配置 Express 后端 - Vercel](https://vercel.com/changelog/zero-configuration-express-backends)

**原文标题**: [Zero-configuration Express backends - Vercel](https://vercel.com/changelog/zero-configuration-express-backends)

Express.js 现在可以在 Vercel 上实现零配置部署，无需额外设置即可获得深度框架支持。

- 🚀 Vercel 现已原生支持 Express.js 框架，无需任何配置
- 🔧 无需使用 vercel.json 重定向或 /api 目录即可直接部署
- 🌐 框架定义的基础设施能自动识别并深度优化 Express 应用
- 👋 示例展示了一个简单的 "Hello World" Express 应用部署方式
- 📖 官方提供 Express on Vercel 部署文档和快速入门指南

---

### [Vercel Functions 现已支持优雅关闭 - Vercel](https://vercel.com/changelog/vercel-functions-now-support-graceful-shutdown)

**原文标题**: [Vercel Functions now support graceful shutdown - Vercel](https://vercel.com/changelog/vercel-functions-now-support-graceful-shutdown)

Vercel Functions 现在支持优雅关闭，允许在终止前执行清理任务。

- 🚀 Node.js 和 Python 运行时现支持优雅关闭功能
- ⏱️ 提供最多 500 毫秒时间执行清理操作
- 🔧 通过 SIGTERM 信号触发清理任务
- 💾 适用于关闭数据库连接和刷新外部日志等场景
- 📝 开发者可通过 process.on('SIGTERM') 注册处理函数

---

### [NodeBook | 精通Node.js - Node.js开发完全指南](https://www.thenodebook.com/)

**原文标题**: [NodeBook | Master Node.js - Complete Guide to Node.js Development](https://www.thenodebook.com/)

一本深入探讨Node.js内部机制、性能优化和生产工程实践的免费在线书籍，涵盖38章、240+子章节，约5000页内容，旨在帮助开发者从底层理解Node.js运行原理。

- 📖 全面解析Node.js架构：包括V8引擎、事件循环、libuv库和线程模型等核心机制
- 🔧 性能深度优化：涵盖垃圾回收调优、内存泄漏排查、V8编译管道和零拷贝流架构
- ⚡ 生产环境实践：提供分布式系统可观测性、原生插件开发和故障诊断等实战内容
- 📚 结构化学习路径：分为四大卷，从基础架构到高级性能调优，逐步深入
- 🆓 完全免费开放：所有章节可在线免费阅读，配套工具和资源无付费墙
- 📅 持续更新计划：2025-2026年逐步发布完整四卷内容，包含纸质版出版计划
- 👨💻 作者经验丰富：由拥有10年Node.js开发经验的Ishtmeet Singh编写，融合实际生产经验
- 🔍 实战案例丰富：每章包含动手实验、真实案例和性能洞察，注重实践应用

---

### [深入V8 JavaScript引擎 | NodeBook](https://www.thenodebook.com/node-arch/v8-engine-intro)

**原文标题**: [Inside the V8 JavaScript Engine | NodeBook](https://www.thenodebook.com/node-arch/v8-engine-intro)

V8 JavaScript引擎是一个兼具解释器和多层级JIT编译器的复杂系统，通过Ignition解释器生成字节码并执行，再通过Sparkplug、Maglev和TurboFan逐级优化代码，最终生成高性能机器码。其性能核心依赖于对象形状和类型的可预测性，隐藏类（Hidden Classes）和内联缓存（Inline Caches）是实现快速属性访问的关键机制。代码若违反假设（如动态属性修改或类型混合）会触发去优化（deoptimization），导致性能急剧下降。优化策略包括保持对象形状稳定、避免多态函数、谨慎使用delete操作符，以及优先使用整型运算。

- 🚀 V8采用四层编译管道：Ignition（解释器）→ Sparkplug（基线编译器）→ Maglev（中阶优化编译器）→ TurboFan（高阶优化编译器），平衡启动速度和峰值性能。
- 🧠 隐藏类（Hidden Classes）是V8优化基础，对象属性顺序或结构变化会创建不同隐藏类，破坏优化假设。
- ⚠️ 去优化（Deoptimization）在类型或形状假设失败时触发，可能导致性能下降2-100倍，常见于动态属性添加或类型混合。
- 🔍 内联缓存（Inline Caches）根据调用点历史优化属性访问，单态（monomorphic）最快，多态（polymorphic）次之，巨态（megamorphic）最慢。
- 🛠️ 性能优化关键：预初始化对象属性、使用构造函数稳定形状、避免delete操作（用undefined替代）、保持数组元素类型一致。
- 📉 常见性能陷阱：不稳定对象形状、多态函数、delete操作、混合数组元素类型，需通过 profiling（如--trace-deopt）识别和修复。
- 📚 历史演进：V8从Full-Codegen/Crankshaft架构过渡到现代多层级管道，注重内存效率和优化平滑性。
- ✅ 最佳实践：编写可预测、单调的代码，优先使用整型（Smi），通过工具（如Chrome DevTools）分析和验证优化效果。

---

### [事件循环详解 | NodeBook](https://www.thenodebook.com/node-arch/event-loop-intro)

**原文标题**: [The Event Loop explained | NodeBook](https://www.thenodebook.com/node-arch/event-loop-intro)

Node.js 事件循环机制深入解析，涵盖其单线程模型、异步处理原理及核心组件协作方式。

- 🌀 **单线程模型**：Node.js 使用单线程处理 JavaScript，通过事件循环实现高并发，避免阻塞主线程。
- ⏰ **定时器阶段**：处理 `setTimeout` 和 `setInterval` 回调，延迟时间为最小执行时间，实际执行时间可能因事件循环状态而延迟。
- 🔄 **轮询阶段**：核心阶段，处理 I/O 操作（如文件读取、网络请求），计算等待时间并调用系统通知机制，高效处理异步任务。
- 🧵 **Libuv 线程池**：默认 4 个线程，处理阻塞操作（如文件 I/O、DNS 查询），避免主线程卡顿，可通过 `UV_THREADPOOL_SIZE` 调整大小。
- ⚡ **微任务优先**：`process.nextTick` 和 Promise 回调（微任务）在事件循环各阶段之间立即执行，优先于宏任务（如定时器、I/O 回调）。
- 🛠️ **性能优化**：避免同步操作（如大 JSON 解析、复杂正则表达式），使用 `setImmediate` 分块处理 CPU 密集型任务，或通过 `worker_threads` 实现真正并行。
- 📊 **调试工具**：使用 `perf_hooks.monitorEventLoopDelay` 或 `async_hooks` 监控事件循环延迟和异步资源生命周期。
- ⚠️ **常见误区**：`setTimeout(..., 0)` 和 `setImmediate` 执行顺序不确定（主模块中）或确定（I/O 回调中），需注意垃圾回收可能导致的短暂阻塞。

---

### [未找到标题](https://x.com/satanacchio/status/1965072308789514255)

**原文标题**: [No title found](https://x.com/satanacchio/status/1965072308789514255)

浏览器检测到JavaScript被禁用，导致无法正常使用x.com平台，建议启用JavaScript或更换支持的浏览器，同时可参考帮助中心解决扩展冲突问题。

- 🚫 JavaScript未启用导致功能受限
- 🌐 建议启用脚本或切换兼容浏览器  
- 🔍 帮助中心提供支持浏览器清单  
- 🛡️ 隐私扩展可能引发冲突需暂时禁用  
- 🔄 尝试重新加载页面解决问题

---

### [Node.js](https://nodejs.org/en/blog/release/v20.19.5)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v20.19.5)

Node.js v20.19.5（LTS）版本发布，包含多项错误修复、依赖项更新、文档改进和团队人员变动。

- 🛠️ 修复了多个模块、DNS、HTTP、加密和调试器相关的错误
- 📦 更新了OpenSSL、zlib、acorn、corepack等多个依赖项版本
- 📝 添加了多名新的协作者和技术指导委员会成员
- 🔧 改进了构建系统和工具链配置
- 🐛 解决了内存泄漏和崩溃问题
- 📚 完善了文档内容和格式
- 🌐 提供了多平台二进制安装包下载链接

---

### [Node.js](https://nodejs.org/en/blog/release/v22.19.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v22.19.0)

Node.js v22.19.0 (LTS) 版本发布，包含多项功能增强、错误修复和性能优化，支持多种操作系统和架构。

- 🚀 CLI新增环境变量NODE_USE_SYSTEM_CA=1，支持系统CA证书
- ⏱️ 进程模块添加threadCpuUsage方法，支持线程CPU使用统计
- 🔐 加密模块新增tls.setDefaultCACertificates()方法，设置默认CA证书
- 🌐 DNS查询支持最大超时时间配置，提升网络请求可控性
- 📦 ESM模块移除--experimental-wasm-modules实验标志，正式支持WebAssembly模块
- ⚡ HTTP服务器新增keepAliveTimeoutBuffer选项，优化连接管理
- 🛡️ 网络模块更新net.blocklist，支持文件保存和管理功能
- 📚 文档多处更新和修正，包括版本验证指南和安全说明
- 🔧 性能优化和错误修复，涵盖缓冲区、流处理和V8引擎等方面
- 📊 基准测试工具增强，支持跟踪和校准功能
- 🌍 支持多种操作系统和架构，提供完整的安装包和二进制文件

---

### [使用`Intl.Segmenter` API实现精确文本长度 | 自动魔法](https://blog.sangeeth.dev/posts/accurate-text-lengths-with-intl-segmenter-api/)

**原文标题**: [
    
    Accurate text lengths with `Intl.Segmenter` API | Automagic
    
](https://blog.sangeeth.dev/posts/accurate-text-lengths-with-intl-segmenter-api/)

JavaScript中字符串长度计算因UTF-16编码存在偏差，如表情符号和某些语言字符会返回异常长度值，而Swift的字符计数方式更符合人类直觉。通过Intl.Segmenter API可实现准确的字素簇计数，但需注意性能开销和特殊控制字符的处理。

- 🧠 JavaScript的String.length基于UTF-16编码单元计数，导致表情符号（如👨‍👩‍👧‍👦长度显示11）和非拉丁字符（如印地语"दरबार"显示5）长度计算错误
- 🍎 Swift的String.count通过扩展字素簇（extended grapheme cluster）实现符合人类感知的字符计数（所有测试字符均返回预期长度）
- 🌐 Intl.Segmenter API提供浏览器原生解决方案，使用granularity: "grapheme"参数可准确分割字符（需注意$O(n)$时间复杂度和控制字符干扰）
- ⚠️ 实际开发中需权衡性能：表单验证等场景推荐使用字素计数，但不应盲目替换所有String.length用法
- 📖 涉及国际化应用时应避免基于英文字符长度限制姓名输入，尊重不同语言的命名习惯

---

### [用4美元VPS处理5亿次点击 - YouTube](https://www.youtube.com/watch?v=nk3Ti0tCGvA)

**原文标题**: [Handling 500M clicks with a $4 VPS - YouTube](https://www.youtube.com/watch?v=nk3Ti0tCGvA)

YouTube平台提供了全面的用户支持与资源，涵盖从创作者工具到政策指南的各项服务。  
- 📄 关于平台的基本信息与介绍  
- 📢 媒体相关资源与新闻发布  
- ©️ 版权保护与内容政策  
- 📞 用户联系与客服支持  
- 🎬 创作者专属工具与资源  
- 💼 广告合作与商业化选项  
- 💻 开发者接口与技术文档  
- 📑 使用条款与协议说明  
- 🔒 隐私政策与数据保护  
- ⚖️ 平台安全与合规指南  
- 🔧 功能测试与新产品体验  
- ™️ 版权声明与归属信息（谷歌2025）

---

### [从Docker迁移至Podman](https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too)

**原文标题**: [Switching from Docker to Podman](https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too)

作者分享从Docker转向Podman的实践体验，强调其在安全性、资源效率和系统集成方面的优势，并提供具体迁移指南。

- 🛡️ 安全性提升：Podman采用无守护进程架构和rootless模式，从根本上减少攻击面，避免Docker因守护进程权限过高导致的安全风险
- ⚡ 资源效率优化：无常驻后台进程降低内存占用，容器故障隔离设计避免单点故障影响其他服务
- 🔗 原生系统集成：直接生成systemd单元文件实现服务化管理，支持Kubernetes YAML生成实现开发生产环境一致性
- 🔄 无缝迁移兼容：CLI命令与Docker完全兼容，现有Dockerfile无需修改，支持别名直接替换
- 🐧 符合Unix哲学：专注核心功能，镜像构建（Buildah）和仓库管理（Skopeo）由专用工具处理
- 📚 实践迁移指南：提供从FastAPI项目构建、运行到生产部署的完整操作流程，包括多服务pod创建和Docker Compose替代方案

---

### [Node.js中的UDP：深度技术指南 - Pavel Romanov 著](https://nodevibe.substack.com/p/udp-in-nodejs-deep-technical-guide)

**原文标题**: [UDP in Node.js: deep technical guide - by Pavel Romanov](https://nodevibe.substack.com/p/udp-in-nodejs-deep-technical-guide)

UDP是一种无连接的传输层协议，相比TCP具有更高性能但缺乏可靠性保证。Node.js通过dgram模块支持UDP，但在高性能场景下存在数据拷贝次数多和垃圾回收延迟等限制。

- 🚀 UDP性能优势：无握手过程、数据包更小，但无传输保证、无序、无重传机制
- ⚠️ Node.js性能局限：数据需经过3-4次拷贝（C/C++仅1次），高吞吐量时垃圾回收可能造成延迟
- 📦 dgram模块使用：通过createSocket创建套接字，用bind绑定端口，connect可关联目标地址简化发送
- 🔧 底层实现：JavaScript → dgram模块 → UDPWrap(C++) → libuv → 系统调用 → 内核UDP栈 → 网络接口
- 📊 适用场景：适合低延迟需求但对可靠性要求不高的应用，如实时音视频、游戏等

---

### [媒体兔](https://mediabunny.dev/)

**原文标题**: [Mediabunny](https://mediabunny.dev/)

人工智能工具与资源导航平台，提供开发指南、API接口、大型语言模型应用示例及开源项目支持  
- 🧭 核心导航：结构化搜索功能与主导航系统  
- 📚 开发指南：提供详细的技术文档和使用教程  
- 🔌 API集成：开放接口支持开发者调用功能  
- 🧠 LLM资源：集中展示大型语言模型相关工具案例  
- 💡 示例演示：实用代码范例和应用场景展示  
- 🤝 赞助支持：开源项目赞助与协作机会说明  
- 📜 许可协议：明确平台使用条款和开源许可证  
- 🎨 界面定制：个性化外观设置与用户体验优化

---

### [支持的格式与编解码器 | Mediabunny](https://mediabunny.dev/guide/supported-formats-and-codecs)

**原文标题**: [Supported formats & codecs | Mediabunny](https://mediabunny.dev/guide/supported-formats-and-codecs)

Mediabunny 是一个支持多种媒体容器格式和编解码器的库，提供双向读写功能，并允许开发者通过实用函数检测浏览器编解码能力，同时支持自定义编码器和解码器以扩展兼容性。

- 📦 支持多种常见媒体容器格式，包括 MP4、MOV、MKV、WebM、Ogg、MP3、WAV 和 AAC，全部支持双向读写
- 🔧 内置支持 WebCodecs API 指定的所有编解码器及额外 PCM 音频编解码器，PCM 编解码器始终可用
- 🎥 视频编解码器包括 AVC/H.264、HEVC/H.265、VP8、VP9 和 AV1
- 🎵 音频编解码器涵盖 AAC、Opus、MP3、Vorbis、FLAC 及多种 PCM 格式（如 8/16/24/32 位有符号/无符号、浮点等）
- 📝 字幕编解码器目前仅支持 WebVTT（仅可写入，不可读取）
- 🌐 提供实用函数（如 canEncode、getEncodableCodecs）检测浏览器对特定编解码器的编码能力，支持自定义配置检查
- ⚙️ 允许注册自定义编码器和解码器，以扩展浏览器不支持的编解码功能或用于非浏览器环境（如 Node.js）
- ⚠️ 自定义编解码器需严格遵循实现规则（如数据包必须按解码顺序传递，样本必须按时间戳排序）
- 📊 不同容器格式对编解码器的支持存在差异（如 WebM 仅支持部分 Matroska 编解码器），需参考兼容性表

---

### [缩略图生成示例 | Mediabunny](https://mediabunny.dev/examples/thumbnail-generation/)

**原文标题**: [Thumbnail generation example | Mediabunny](https://mediabunny.dev/examples/thumbnail-generation/)

Mediabunny提供便捷的视频缩略图提取功能，用户可通过上传本地文件、输入远程链接或下载示例文件快速生成缩略图。

- 🖼️ 支持上传本地媒体文件提取视频缩略图
- 🌐 可通过输入远程URL加载在线媒体资源
- 📥 提供示例文件下载功能方便用户体验
- 🔧 作为开源工具支持查看源代码

---

### [元数据提取示例 | Mediabunny](https://mediabunny.dev/examples/metadata-extraction/)

**原文标题**: [Metadata extraction example | Mediabunny](https://mediabunny.dev/examples/metadata-extraction/)

Mediabunny是一个用于提取媒体文件元数据的工具，用户可选择本地文件或远程URL进行操作，并支持下载示例文件及查看源代码。

- 📁 选择或拖放媒体文件以提取元数据
- 🌐 支持加载远程URL或本地文件
- ⬇️ 提供示例文件下载功能
- 🔍 可查看工具源代码

---

### [程序化生成示例 | Mediabunny](https://mediabunny.dev/examples/procedural-generation/)

**原文标题**: [Procedural Generation example | Mediabunny](https://mediabunny.dev/examples/procedural-generation/)

该页面利用Mediabunny工具快速生成音乐弹跳球的程序化视频，用户可自定义视频时长和球体数量并实时生成。

- 🎬 通过Mediabunny工具实现程序化视频生成
- 🎵 生成带有音乐节奏的弹跳球动画效果
- ⚡ 支持极速生成视频内容
- 🎮 用户可自定义视频时长和球体数量
- 🔍 提供源代码查看功能

---

### [GitHub - Vanilagy/mediabunny：纯TypeScript媒体工具包，用于直接在浏览器中读取、写入和转换视频与音频文件。](https://github.com/Vanilagy/mediabunny)

**原文标题**: [GitHub - Vanilagy/mediabunny: Pure TypeScript media toolkit for reading, writing, and converting video and audio files, directly in the browser.](https://github.com/Vanilagy/mediabunny)

Mediabunny 是一个基于 TypeScript 开发的纯前端媒体处理工具库，支持在浏览器中直接读写、转换音视频文件，无需依赖且性能高效。

- 📦 纯 TypeScript 开发，零依赖，支持树摇优化
- 🎬 支持多种媒体格式（MP4、WebM、MP3、WAV 等）的读写和转码
- ⚡ 利用 WebCodecs API 实现硬件加速编解码
- ✂️ 提供转换 API，支持剪辑、转码、缩放等操作
- 🌐 兼容浏览器和 Node.js 环境
- 📄 采用 MPL-2.0 开源协议，允许商业使用
- 🔧 提供详细文档和开发指南，支持社区贡献

---

### [首页 | Rocketadmin](https://rocketadmin.com/?utm_source=nodeweekly)

**原文标题**: [Home | Rocketadmin](https://rocketadmin.com/?utm_source=nodeweekly)

Rocketadmin提供快速部署的数据库管理面板解决方案，支持多种数据库类型，5分钟内即可启动，无需编码且提供免费试用。

- 🚀 5分钟快速部署MySQL/PostgreSQL/MSSQL/Oracle/MongoDB管理面板
- 💰 节省$90,547开发成本，无需从零构建自定义管理后台
- ⏱️ 节省10,000小时开发时间，专注核心业务
- ⚡ 提供极致性能优化，响应速度大幅提升
- 🔒 通过1432项安全测试，保障数据安全与系统稳定
- 👨💻 每周5天专业技术支持团队提供协助
- ☕ 精心设计658次优化的直观用户界面
- 🌐 支持多设备响应式访问与远程协作
- 🔧 提供API集成、自定义权限管理和操作日志追踪
- 🆓 提供免费试用和30天免费周期，后续按用户数收费

---

### [GitHub - bbc/sqs-consumer：无需样板代码即可构建基于亚马逊简单队列服务（SQS）的应用程序](https://github.com/bbc/sqs-consumer)

**原文标题**: [GitHub - bbc/sqs-consumer: Build Amazon Simple Queue Service (SQS) based applications without the boilerplate](https://github.com/bbc/sqs-consumer)

该开源库简化了基于Amazon SQS的应用开发，通过封装底层逻辑让开发者专注于消息处理逻辑的实现。

- 🚀 支持通过npm或JSR安装，提供简洁API快速构建SQS消费应用
- 🔄 默认采用长轮询和顺序处理机制，支持批量处理配置提升并发性能
- ⚠️ 提供灵活的消息确认机制，可通过返回值控制消息删除行为
- 🛡️ 完整错误处理支持，配合SQS重驱动策略可实现死信队列功能
- 🔧 支持FIFO队列（需特定配置）和自定义AWS凭证配置
- 📊 实时监控状态（isRunning/isPolling），支持动态调整配置参数
- 🌐 要求SQS相关IAM权限，包含消息接收、删除和可见性变更操作
- 📝 采用Apache 2.0开源协议，拥有1.9k星标和67位贡献者

---

### [GitHub - actions/github-script：使用JavaScript编写GitHub API工作流脚本](https://github.com/actions/github-script)

**原文标题**: [GitHub - actions/github-script: Write workflows scripting the GitHub API in JavaScript](https://github.com/actions/github-script)

GitHub官方提供的actions/github-script工具，允许用户在GitHub Actions工作流中使用JavaScript脚本操作GitHub API，提供预认证的Octokit客户端和上下文对象，支持自定义脚本执行、结果返回、重试机制及外部模块调用。

- 🚀 提供预配置的GitHub API客户端和上下文对象，支持JavaScript脚本直接操作仓库事件
- ⚠️ 当前版本v8基于Node 24运行时，存在与早期版本的兼容性变更需注意
- 📦 支持通过require调用本地脚本文件或npm模块，包括ESM模块导入
- 🔄 内置请求重试机制，可配置重试次数和豁免状态码（默认400/401/403/404/422不重试）
- 🔐 支持使用自定义PAT令牌替代默认GITHUB_TOKEN以突破权限限制
- 📝 提供结果编码选项（JSON/字符串），可通过step outputs获取脚本返回值
- 🛠️ 集成@actions核心工具包（core/glob/io/exec），支持跨平台命令执行和文件操作
- 🌐 包含GraphQL查询支持，可通过github.graphql执行自定义API查询
- 📋 提供完整开发文档和类型支持（@actions/github-script类型声明包）

---

### [GitHub - dougmoscrop/serverless-http：在 AWS Lambda 中使用现有中间件框架（如 Express、Koa）🎉](https://github.com/dougmoscrop/serverless-http)

**原文标题**: [GitHub - dougmoscrop/serverless-http: Use your existing middleware framework (e.g. Express, Koa) in AWS Lambda 🎉](https://github.com/dougmoscrop/serverless-http)

该开源项目允许开发者将现有的Node.js中间件框架（如Express、Koa）无缝部署到无服务器环境（如AWS Lambda），无需创建HTTP服务器或管理端口。

- 🚀 支持多种框架：包括Express、Koa、Fastify等主流Node.js中间件框架
- 🌐 多平台兼容：主要支持AWS Lambda，实验性支持Azure和Genezio云平台
- ⚡ 使用简单：通过包装函数即可将现有应用转换为无服务函数
- 📊 项目活跃：拥有1.8k星标、169个分叉和51位贡献者
- ⚠️ 注意事项：需遵循无服务器环境限制，不支持内存会话和WebSocket等功能
- 🔧 灵活扩展：支持Promise异步处理和自定义中间件配置
- 📚 丰富示例：提供详细的使用示例和不同框架的部署案例

---

### [GitHub - cdimascio/express-openapi-validator: 🦋 使用 ExpressJS 和 OpenAPI 3.1.x 或 3.0.x 规范自动验证 API 请求、响应及安全配置](https://github.com/cdimascio/express-openapi-validator)

**原文标题**: [GitHub - cdimascio/express-openapi-validator: 🦋 Auto-validates api requests, responses, and securities using ExpressJS and an OpenAPI 3.1.x or 3.0.x specification](https://github.com/cdimascio/express-openapi-validator)

express-openapi-validator是一个用于ExpressJS的OpenAPI验证中间件，可自动验证API请求、响应及安全性，支持OpenAPI 3.0.x和3.1.x规范。

- 🦋 自动验证API请求、响应和安全性，基于OpenAPI 3.0.x或3.1.x规范
- 📖 提供完整文档，支持请求验证、响应验证（仅JSON）和安全验证
- 🛠️ 支持自定义格式、数据序列化/反序列化及多文件拆分规范
- 🚀 兼容Express 4和5，同时支持NestJS、Koa和Fastify框架
- 📦 通过npm安装，集成简单，无需改变现有代码结构或项目布局
- ⭐ 开源项目，拥有975个星标和229个分支，采用MIT许可证
- 🔧 包含错误处理中间件，需在验证路由前配置Express的body解析器

---

### [Prisma 6.15.0 版本发布 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.15.0)

**原文标题**: [Release 6.15.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.15.0)

Prisma 发布了 6.15.0 稳定版本，引入了多项新功能和改进，包括 AI 安全防护、运行时优化、Vercel Fluid 集成支持，以及 Prisma Postgres 管理 API 的正式可用性。

- 🛡️ 新增 AI 安全防护机制，防止 AI 助手执行破坏性数据库命令
- 🔧 简化 Prisma Client 运行时选项，移除冗余别名，提升一致性
- ☁️ 支持 Vercel Fluid Compute，通过 `attachDatabasePool` 实用工具防止数据库连接泄漏
- 🗄️ Prisma Postgres 管理 API 正式可用，支持编程方式创建和管理数据库实例
- 🔌 Prisma Postgres 现可在 Pipedream 中使用，支持与 2800+ 应用集成
- 📋 `npx create-db` 新增 `--json` 标志，方便以编程方式获取数据库详细信息
- 🌐 直接连接 Prisma Postgres 功能接近正式发布，支持更多 ORM 和工具

---

### [GitHub - tinylibs/tinypool: 🧵 极简Node.js工作线程池实现（38KB）](https://github.com/tinylibs/tinypool)

**原文标题**: [GitHub - tinylibs/tinypool: 🧵 A minimal and tiny Node.js Worker Thread Pool implementation (38KB)](https://github.com/tinylibs/tinypool)

Tinypool 是一个轻量级 Node.js 工作线程池实现，基于 Piscina 优化而来，专注于减少依赖和体积，适用于需要高效线程池但无需复杂功能的场景。

- 🧵 基于 Piscina 的极简线程池实现，安装体积仅 38KB
- 📦 零依赖且完全支持 TypeScript 和 ESM
- ⚙️ 支持 worker_threads 和 child_process 两种运行时
- 🚫 不包含利用率统计和操作系统级线程优先级功能
- 🔧 提供内存回收、任务取消及工作线程隔离等特色 API
- 🎯 主要服务于 Vitest，适合无复杂需求的高性能场景

---

### [GitHub - sidequestjs/sidequest：Sidequest 是一个面向 Node.js 应用的现代化、可扩展的后台作业处理器。](https://github.com/sidequestjs/sidequest)

**原文标题**: [GitHub - sidequestjs/sidequest: Sidequest is a modern, scalable background job processor for Node.js applications.](https://github.com/sidequestjs/sidequest)

Sidequest 是一个专为 Node.js 应用设计的现代化、可扩展的后台任务处理器，支持多数据库后端、提供可视化监控面板和全面的任务管理功能。

- 🚀 高性能：使用工作线程实现非阻塞任务处理
- 🗄️ 多后端支持：内置 PostgreSQL、MySQL、SQLite 和 MongoDB 支持
- 📝 TypeScript 原生支持：完全兼容现代 JavaScript 和 TypeScript
- 📊 可视化面板：提供响应式 Web 仪表板用于监控任务和队列
- ⏰ 定时任务：支持按特定时间调度任务执行
- 🔒 任务去重：通过灵活性唯一性约束防止重复任务
- 🛠️ CLI 工具：提供数据库迁移和管理的命令行接口
- 📦 模块化架构：采用 monorepo 结构，支持灵活部署
- 📄 开源协议：采用 LGPL-3.0 许可证，社区驱动开发
- 🌟 项目活跃：拥有 799 个星标和 11 个分支，持续维护更新

---

### [发布 v6.19.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.19.0)

**原文标题**: [Release v6.19.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.19.0)

MongoDB Node.js 驱动程序发布 6.19.0 版本，引入实验性查询加密文本搜索功能、TLS 安全上下文支持，并优化游标管理和连接握手流程。

- 🔐 实验性支持可查询加密文本字段的前缀、后缀和子字符串查询（需配合 mongodb-client-encryption@≥6.5.0）
- 🛡️ 允许为自动加密和客户端加密的 TLS 选项配置 secureContext
- 🚫 collection.findOne() 和 find() 方法彻底解决服务器游标遗留问题
- 📉 移除认证启用时的连接 ping 检测，改用连接池握手验证
- 📦 包含 NODE-4179/NODE-6472/NODE-7020/NODE-7059 等多项功能改进

---

### [GitHub - electron/electron: :electron: 使用 JavaScript、HTML 和 CSS 构建跨平台桌面应用](https://github.com/electron/electron)

**原文标题**: [GitHub - electron/electron: :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS](https://github.com/electron/electron)

Electron是一个使用JavaScript、HTML和CSS构建跨平台桌面应用程序的开源框架，基于Node.js和Chromium，被Visual Studio Code等众多应用采用。

- 🖥️ 支持macOS、Windows和Linux三大平台，提供多架构二进制文件
- 📦 通过npm安装便捷，可作为开发依赖项集成到项目中
- 🛠️ 提供Electron Fiddle工具，方便快速实验和学习API
- 🌐 文档支持多语言翻译，包括简体中文等8种语言
- 📝 采用MIT开源协议，拥有活跃的社区贡献和丰富的资源
- ⭐ GitHub上获得11.8万星标，被41.1万个项目使用
- 🔧 基于C++和TypeScript开发，支持程序化调用和自定义镜像

---

### [GitHub - express-rate-limit/express-rate-limit: Express 网络服务器的基础限速中间件](https://github.com/express-rate-limit/express-rate-limit)

**原文标题**: [GitHub - express-rate-limit/express-rate-limit: Basic rate-limiting middleware for the Express web server](https://github.com/express-rate-limit/express-rate-limit)

express-rate-limit 是一个用于 Express web 服务器的基本限速中间件，用于限制对公共 API 和端点的重复请求，支持多种配置选项和数据存储方式。

- 🚦 基本限速中间件，用于限制 Express 服务器的重复请求
- ⚙️ 支持自定义配置，如时间窗口、请求限制、响应消息等
- 💾 内置内存存储，并支持多种外部数据存储
- 📊 提供标准速率限制头信息（如 RateLimit 头部）
- 🔧 支持异步配置选项和自定义密钥生成器
- 🌐 与 express-slow-down 和 ratelimit-header-parser 兼容
- 📦 在 npm 上可用，拥有 3.1k 星和 237 个 fork
- 📄 采用 MIT 许可证，由 Nathan Friedly 和 Vedant K 维护

---

### [发布 v5.6.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.6.0)

**原文标题**: [Release v5.6.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.6.0)

Fastify项目发布了v5.6.0版本，包含类型系统优化、文档修正和性能说明改进，并迎来三位新贡献者。

- 🚀 修复TypeScript类型定义问题（#6287、#6292）
- 📝 更新路由选项类型并修正文档拼写错误（#6282、#6302）
- ⚡ 优化路由性能说明的表述清晰度（#6306）
- 👋 新增三位首次贡献者：@joshkel、@hmanzoni、@Prasad2604
- 📦 包含1个提交，由mcollina于9月5日通过GPG签名发布
- ❤️ 获得社区14位用户的表情符号互动（点赞/庆祝/爱心等）

---

### [GitHub - extremeheat/JSPyBridge: 🌉 实现 Node.js 与 Python 互操作的桥梁](https://github.com/extremeheat/JSPyBridge)

**原文标题**: [GitHub - extremeheat/JSPyBridge: 🌉. Bridge to interoperate Node.js and Python](https://github.com/extremeheat/JSPyBridge)

JSPyBridge 是一个实现 Node.js 和 Python 互操作的库，支持双向调用和对象交互，提供垃圾回收、异步支持和异常处理等功能。

- 🌉 支持 Node.js 和 Python 双向互操作，允许在两种语言中直接调用函数和访问对象属性
- 🔄 内置垃圾回收机制，确保资源有效管理
- ⚡ 支持异步和同步函数调用，以及双向回调
- 📚 提供迭代和异常处理支持，可无缝操作跨语言对象
- 🐍 通过 `require` 从 Python 调用 JavaScript，支持自动依赖安装和版本管理
- 📦 通过 `pythonia` 从 JavaScript 调用 Python，所有 API 调用需使用 `await`
- 🧪 包含丰富的示例，如事件发射器、ES5 类、回调函数和迭代操作
- ⚠️ 存在一些限制，如保留关键字 `ffid`、标准错误通信干扰和函数调用超时设置

---

### [发布 v4.5.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.5.0)

**原文标题**: [Release v4.5.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.5.0)

NodeBB论坛软件发布了v4.5.0版本更新，包含功能增强、问题修复和系统优化。

- 🚀 新增ActivityPub中继功能与自动分类规则，支持远程内容联邦化处理
- 📝 改进OpenAPI文档规范，修复接口定义与路由配置问题
- 🤖 引入智能摘要生成技术（sbd依赖），优化帖子标题和内容摘要
- 🌍 新增乌尔都语本地化支持，扩展多语言覆盖范围
- 🐛 修复包括DNS反绑攻击防护、通知已读状态、图片处理等35项系统缺陷
- ⚡ 重构缓存机制与数据库队列，提升系统性能和稳定性
- 🧪 完善测试用例并增加日志记录，强化系统调试能力
- 🔧 进行代码优化和依赖项调整，改善开发维护体验

---

### [ESLint v9.35.0 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/09/eslint-v9.35.0-released/)

**原文标题**: [ESLint v9.35.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/09/eslint-v9.35.0-released/)

ESLint v9.35.0 是一个次要版本升级，引入了新规则并修复了多个错误。

- 🆕 新增 preserve-caught-error 规则，强制在 catch 块内抛出错误时使用 cause 属性
- 💡 no-empty-function 和 no-empty-static-block 规则现在提供添加 /* empty */ 注释的建议
- 🔧 no-empty 规则现在允许包含注释的空 switch 语句
- 🐛 修复了多个错误，包括更新不可克隆选项的错误消息和修复 no-loss-of-precision 误报
- 📚 改进了文档，包括更新 --no-ignore 和 --ignore-pattern 的文档说明
- 🛠️ 进行了多项维护工作，包括升级 @eslint/js@9.35.0 和移除废弃的 context.parserOptions 用法

---

### [学习在Node.js中构建API | 使用Express、Postgres和Prisma创建REST API | Frontend Masters](https://frontendmasters.com/courses/api-design-nodejs-v4/?utm_source=email&utm_medium=nodeweekly&utm_content=nodejsv4)

**原文标题**: [Learn to Build APIs in Node.js | Use Express, Postgres & Prisma to Create REST APIs | Frontend Masters](https://frontendmasters.com/courses/api-design-nodejs-v4/?utm_source=email&utm_medium=nodeweekly&utm_content=nodejsv4)

本课程由Netflix的Scott Moss主讲，全面教授使用Node.js从零开始设计和构建API，涵盖Express路由、Prisma与PostgreSQL数据库操作、TypeScript集成、JWT身份验证及部署实践。

- 🚀 使用Express框架构建RESTful API并处理路由逻辑
- 🗄️ 通过Prisma ORM与PostgreSQL数据库进行读写操作
- 🔐 采用JWT实现路由保护与用户身份验证机制
- 🧪 包含单元测试(Jest)与集成测试(SuperTest)实践
- 🌐 最终部署到Render.com云平台实现项目上线
- ⏱️ 课程时长7小时4分钟，包含实战练习与错误处理专题
- ⭐ 学员反馈显示该课程对求职面试有显著帮助

---

### [编程未来特卖 | Frontend Masters](https://frontendmasters.com/sale/?utm_source=email&utm_medium=nodeweekly&utm_content=sale)

**原文标题**: [The Future of Coding Sale | Frontend Masters](https://frontendmasters.com/sale/?utm_source=email&utm_medium=nodeweekly&utm_content=sale)

前端大师年度会员优惠，提供290美元特价年费，帮助中级开发者快速晋升为高级开发者。会员可享受250多门优质课程、移动端离线播放、实时工作坊问答及Discord社区等权益。  
- 💰 年度会员特价290美元（原价390美元）  
- 🚀 助力从中级到高级开发者的职业晋升  
- 📚 250+精选课程与个性化学习路径  
- 📱 支持离线播放的移动端应用  
- 💬 实时工作坊问答与Discord社区接入  
- 🔍 新增全局及课程搜索功能  
- ⭐ 相比月费节省178美元，比原年费立减100美元

---

### [开始使用Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users)

Redis是一个高速数据平台，提供云端和本地解决方案，帮助团队快速构建应用程序，支持向量数据库、缓存和NoSQL数据库等多种数据技术。

- 🚀 全球最快的数据平台，助力快速开发应用
- ☁️ 提供云端和本地部署解决方案
- 🧠 支持向量数据库，构建高性能生成式AI应用
- ⚡ 内存缓存技术加速应用程序性能
- 🗃️ NoSQL键值存储，支持多种数据结构
- 📊 无缝从实验扩展到生产级AI应用
- 💻 支持多语言开发，提供开发者中心资源
- 🆓 提供免费构建选项，可立即体验

---

### [开始使用Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users%20)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users%20)

Redis是一个高速数据平台，提供云端和本地部署解决方案，帮助团队快速开发应用，支持向量数据库、缓存和NoSQL数据库等多种数据技术。

- 🚀 全球最快数据平台，提供云端与本地部署方案
- 🧠 支持向量数据库，助力生成式AI应用开发
- ⚡ 内存缓存技术显著提升应用响应速度
- 🗃️ 键值对NoSQL数据库，适用于实时数据处理
- 🌐 支持多语言开发，提供开发者与架构师专属资源
- 📊 支持从实验到生产环境的无缝扩展
- 🆓 提供免费入门选项和实时演示服务

---

### [为什么浏览器会限制JavaScript计时器？| 解读信号](https://nolanlawson.com/2025/08/31/why-do-browsers-throttle-javascript-timers/)

**原文标题**: [Why do browsers throttle JavaScript timers? | Read the Tea Leaves](https://nolanlawson.com/2025/08/31/why-do-browsers-throttle-javascript-timers/)

浏览器对JavaScript计时器进行节流以防止滥用，但开发者可通过其他API实现更精确的定时控制。

- ⏱️ `setTimeout(0)` 实际延迟约4毫秒，浏览器为防滥用设定了最小延迟限制
- 🔋 设备使用电池或处于后台时，节流更严格（如Chrome后台延迟达1秒）
- 🧪 作者通过基准测试比较了多种定时方案，`scheduler.postTask` 性能最佳（近0延迟）
- ⚖️ 浏览器节流策略源于两派争论：保护用户体验 vs 给予开发者控制权
- 🛠️ 推荐使用 `scheduler.postTask` 或 `MessageChannel` 替代 `setTimeout` 以实现精确定时
- ⚠️ Safari对 `MessageChannel` 存在额外节流，`window.postMessage` 可能干扰页面其他脚本
- 🔮 未来可能因API滥用出现新一轮节流，但当前标准更倾向于开发者控制

---

### [仙女座](https://tryandromeda.dev/)

**原文标题**: [Andromeda](https://tryandromeda.dev/)

Andromeda 是一个基于 Rust 构建的现代、快速且安全的 JavaScript 和 TypeScript 运行时，由 Nova 引擎驱动，具备零配置 TypeScript 支持、硬件加速图形和全面的 Web API。

- 🚀 基于 Rust 构建，提供高性能和内存安全保证
- ⚡ 集成 Nova 引擎，支持现代 JavaScript 和 TypeScript 运行时
- 🛠️ 零配置 TypeScript 支持，简化开发流程
- 🎨 硬件加速的 2D Canvas API，支持 WGPU 后端和 PNG 导出
- 🔧 内置语言服务器协议（LSP），提供实时诊断和丰富错误信息
- 📦 完整工具链，包括 REPL、格式化程序、打包器和编译器
- 🔒 安全特性包括内存安全基础、沙盒执行环境和基于权限的 API 访问
- 🌍 支持多平台，包括 Linux、macOS 和 Windows
- 📊 适用于图形可视化、高性能脚本、Web 服务和科学计算等多种应用场景
- 📉 与 Node.js 和 Deno 相比，具有更低的内存占用和更高的性能特性

---

### [新星](https://trynova.dev/)

**原文标题**: [Nova](https://trynova.dev/)

Nova是一个用Rust编写的实验性JavaScript和WebAssembly引擎，采用数据导向设计原则，目前处于开发阶段但发展迅速。

- 🦀 基于Rust语言开发的数据导向设计引擎
- 🔬 目前为实验项目但具备未来发展潜力
- 📊 已通过77%的test262测试套件
- 🚀 开发进展快速且持续优化中
- 📂 开源项目可访问GitHub仓库参与
- 💬 可通过Discord服务器与核心团队交流
- ✍️ 定期发布技术博客记录开发进展

---

### [2025年即将举办的JavaScript与React大会](https://thoughtbot.com/blog/upcoming-javascript-and-react-conferences-for-2025)

**原文标题**: [
        Upcoming JavaScript and React Conferences for 2025
    ](https://thoughtbot.com/blog/upcoming-javascript-and-react-conferences-for-2025)

2025年JavaScript与React技术会议前瞻，涵盖全球多地活动信息及行业趋势。

- 🌍 全球多地举办技术会议，包括波兰、美国、荷兰、奥地利等国家和地区
- ⚛️ React与JavaScript是核心主题，同时涵盖GraphQL、Vite等前端技术
- 💡 2024年关注性能优化、React生态演进及AI在工作流中的应用
- 🤖 2025年重点包括AI相关开发、生成式引擎优化等前沿话题
- 📅 会议时间从2025年9月持续至12月，提供线上线下多种参与方式
- 💰 参会费用从40欧元至1199美元不等，满足不同预算需求
- 👥 除了技术分享，会议更提供社区交流和专业人脉拓展机会

---

### [国际游乐场](https://intlin.site/)

**原文标题**: [Intl Playground](https://intlin.site/)

文章概述了人工智能在医疗领域的应用现状与未来潜力，重点讨论了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时提及了数据隐私和技术伦理等挑战。

- 🤖 人工智能辅助医学影像分析，提升诊断准确率
- 🔬 加速新药研发流程，缩短临床试验周期
- 🧬 推动个性化医疗发展，实现精准治疗方案
- 📊 面临医疗数据标准化与隐私保护挑战
- ⚖️ 需要建立相关伦理规范和法律监管框架

---

### [Fresh——简洁、易用、高效的Web框架](https://fresh.deno.dev/)

**原文标题**: [Fresh - The simple, approachable, productive web framework.](https://fresh.deno.dev/)

该内容提示用户点击某个菜谱以加载HTML内容，但未提供实际文本或文章信息。

- 📝 提示用户点击菜谱以加载内容
- 🌐 涉及HTML流式传输技术
- ❓ 缺少具体文本或可总结的实质信息

---

### [Fresh 2.0 进入 Beta 阶段，新增 Vite 支持 | Deno](https://deno.com/blog/fresh-and-vite)

**原文标题**: [Fresh 2.0 Graduates to Beta, Adds Vite Support | Deno](https://deno.com/blog/fresh-and-vite)

Fresh 2.0 已从 alpha 版本升级至 beta 阶段，引入 Vite 插件支持，显著提升开发体验和性能优化。

- 🚀 架构稳定并集成 Vite 插件，支持热模块重载和完整 Vite 生态系统
- ⚡ 生产环境启动速度提升 9-12 倍，路由按需加载且服务端代码打包优化
- 🔧 自动处理 React/Preact 别名映射，无需手动配置依赖
- 🧠 重新引入 <Head> 组件，支持更简洁高效的头部元素管理
- 📚 提供新版迁移指南和部署教程，支持 Deno Deploy 重大更新

---

### [GitHub - samhenrigold/LidAngleSensor：当你调整盖子角度传感器时的感受](https://github.com/samhenrigold/LidAngleSensor)

**原文标题**: [GitHub - samhenrigold/LidAngleSensor: tfw when you when your lid when uhh angle your lid sensor](https://github.com/samhenrigold/LidAngleSensor)

这是一个关于MacBook盖角度传感器的开源工具项目，由开发者samhenrigold创建，可实时显示笔记本屏幕开合角度并配有创意音效。

- 🖥️ 项目功能：通过传感器检测MacBook屏幕开合角度，支持播放木质门缓慢开启的创意音效
- ⚠️ 兼容性说明：仅支持2019款16英寸MacBook Pro及更新机型，已知M1芯片设备存在不兼容问题
- 🔧 安装方式：支持通过Homebrew包管理器快速安装（brew install lidanglesensor）
- 📝 开发背景：开发者自称因空闲时间较多而创作，同时附带了个人求职信息（纽约或远程设计/设计工程师岗位）
- 🎮 音效彩蛋：音效素材源自游戏《乐高蝙蝠侠3：飞越哥谭市》，提供可关闭音效的选项
- 📊 项目热度：获得3000星标和113次分叉，采用Apache-2.0开源协议
- ❓ 趣味FAQ：解释了项目作者显示为"Lisa"的原因（童年注册使用母亲姓名无法修改）

---

### [未找到标题](https://x.com/samhenrigold/status/1964428927159382261)

**原文标题**: [No title found](https://x.com/samhenrigold/status/1964428927159382261)

浏览器检测到JavaScript被禁用，导致无法正常使用x.com平台，建议启用JavaScript或更换支持的浏览器，同时可参考帮助中心解决扩展冲突问题。

- 🚫 JavaScript未启用导致功能受限
- 🌐 建议启用脚本或切换兼容浏览器  
- 🔍 帮助中心提供支持浏览器清单  
- ⚠️ 隐私扩展可能引发访问异常  
- 🔄 可尝试禁用扩展后重新加载

---

