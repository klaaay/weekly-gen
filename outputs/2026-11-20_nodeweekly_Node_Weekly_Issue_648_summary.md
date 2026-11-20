### [GitHub - jasnell/node-skills · GitHub](https://github.com/jasnell/node-skills)

**原文标题**: [GitHub - jasnell/node-skills · GitHub](https://github.com/jasnell/node-skills)

这是一个帮助编码智能体了解其训练数据之后新增的 Node.js 特性的 Agent 技能仓库，覆盖 Node.js 24 LTS 以来的新内置模块、新 API 与标志、默认值变更以及移除项；这些技能可在 Claude Code 和 opencode 中使用，每项技能都基于锁定提交的官方文档编写，并通过在 v24 LTS、current 和 main 构建上运行示例来验证其声明。

- 📦 **仓库概况**：jasnell/node-skills 为公开仓库，采用 MIT 许可，现有 31 个 Star、0 个 Fork，共 2 次提交，且未提供描述与话题标签。
- 🎯 **核心目标**：向编码智能体传授超出其训练数据范围的 Node.js 新特性，包括新模块、新 API 与标志、默认值变化以及移除项。
- 🧪 **验证机制**：每个技能都依据固定提交的 nodejs/node 文档撰写，并在 v24 LTS、current 和 main 构建上通过可运行示例校验其声明。
- 🧩 **技能矩阵**：涵盖实验性 API 检查、现代迁移、模块加载、进程超时、基准测试、直方图统计、测试运行器、内置工具、SQLite、ZIP、流迭代、加密、权限模型、诊断、网络、VFS、FFI、QUIC/DTLS 等约 18 个技能。
- ⚠️ **稳定性提示**：覆盖 Stability 1.x 特性的技能会带有“Experimental API”横幅，引导智能体先使用 node-experimental-check 对照已安装版本核实细节，然后再编写代码。
- 🔌 **Claude Code 安装**：推荐以插件方式安装（可版本化、可升级，技能命名空间为 node-skills:*），执行 `/plugin marketplace add jasnell/node-skills` 与 `/plugin install node-skills@node-skills`；也可用 install/install.mjs 以符号链接方式安装，使 git pull 后自动更新。
- 🛠️ **opencode 安装**：执行 `node install/install.mjs --target opencode`；由于 opencode 也会读取 ~/.claude/skills，因此 Claude Code 的安装已可直接使用，也可在 opencode.json 的 skills 数组中添加本仓库的 skills/ 目录。
- ⚙️ **安装器选项**：支持 --mode copy（复制而非软链接）、--only a,b、--uninstall 与 --dry-run；卸载仅移除安装器自身创建的内容。
- 🔄 **维护技能**：仓库内置项目级 node-skills-maintainer 技能，仅在本仓库内工作时加载、不随插件发布，覆盖新版本 API 调查、分类归属、并行智能体撰写、二进制矩阵验证、触发描述评测以及生命周期事件（晋升、移除、底线版本 EOL）。
- 🧰 **配套工具**：提供 survey.mjs（发现未覆盖的新 API）、结构、lint 与预算测试、skill-budget（常驻 ≤200 tokens、激活 ≤1000）、skill-lint、run-examples、check-drift、trigger-eval 和 discrepancies，且仅需 Node.js 24 及以上、无第三方依赖。
- 📚 **文档体系**：AGENTS.md 说明撰写契约，SURVEY.md 说明特性清单，PLAN.md 说明设计与决策，DISCREPANCIES.md 记录测试中发现的文档与行为不一致。
- 📄 **许可与致谢**：采用 MIT 许可，第三方声明见 THIRD_PARTY_NOTICES.md，其中 skill-budget 与 skill-lint 改编自 mcollina/skills。

---

### [为你的系统选择合适的智能体工作流 | Master.dev](https://master.dev/courses/ai-agent-workflows/?utm_source=email&utm_medium=nodeweekly&utm_content=aiagentcooper)

**原文标题**: [Choose the right agent workflow for your system | Master.dev](https://master.dev/courses/ai-agent-workflows/?utm_source=email&utm_medium=nodeweekly&utm_content=aiagentcooper)

本课程由 GitHub Copilot 团队的 Sabrina（Bri）Goldfarb 主讲，时长 4 小时 25 分钟，评分 4.8，属于 AI Engineering 与 Coding with AI 学习路径。课程围绕“上下文、可靠性、成本”三角权衡，系统讲解 AI Agent 基础、非 Agent 工作流、单 Agent 与多 Agent 架构，并强调从简单方案开始、通过测试与评估选择合适架构。

- 🎯 课程定位：学习构建高效 AI 工作流和 Agent 系统，避免盲目增加 token，而是平衡上下文、可靠性与成本。
- 🧱 前置要求：需具备 Practical Prompt Engineering 基础，或掌握任一编程语言并了解 LLM 基本知识。
- 🧠 Agent 基础：区分推理型 LLM 与 Agent；Agent 是由多个相连部分组成的系统，灵活性越高，控制权让渡越多。
- 🛠️ 工具与 MCP：工具让 Agent 与外界交互；清晰的工具元数据很重要，工具过多会损害性能；MCP 是连接 LLM 与工具/API 的标准。
- 📦 Skills 与 RAG：Skills 是按需加载的指令包，可节省上下文；RAG 通过分块、嵌入和搜索为 Agent 提供外部记忆。
- 🧩 上下文管理：围绕有限上下文窗口，介绍重排序、上下文压缩、最大边际相关性等技术及其成本与可靠性问题。
- 🧠 Agent 记忆：涵盖工作记忆以及语义、情景、程序性记忆，说明 Agent 如何在 LLM“无记忆”的前提下保存与检索信息。
- 🗺️ 规划与反思：比较“先计划后执行”与 ReAct；介绍 self-refine、Reflexion 等方法帮助 Agent 改进结果。
- 🔗 非 Agent 工作流：提示链让每次 LLM 调用衔接下一次，利于准确性与调试，但会增加延迟。
- 🚦 路由与并行：路由将输入分类到专用路径以节省成本；还涵盖并行化、评估器优化器、编排器 - 工作者等模式。
- 📊 工作流评分卡：这些模式本质上是函数、switch、if 等基础编程工具的组合；需保持上下文聚焦、控制成本并诚实处理错误。
- 🤖 单 Agent 系统：核心包括模型、工具、指令和停止条件；需谨慎选型与维护模型，并设计可靠工具。
- 🔁 单 Agent 模式：涵盖 ReAct 循环、Plan & Execute、Reflexion/自我优化，以及通过代码执行动作的 CodeAct；CodeAct 需要安全沙箱。
- 👥 多 Agent 系统：包括顺序式、并行式、监督者、调度器、评估器 - 优化器、点对点等模式，各有成本、延迟、错误传播与调试难度。
- 🧮 多 Agent 权衡：顺序式利于上下文管理与成本，但可能累积错误；并行更快但更贵；监督者适合复杂任务但可能过度设计；点对点灵活但混乱，通常作为最后手段。
- 🧪 评估与选型：通过具体反馈加入反思步骤来提升 Agent；在工作流、单 Agent、多 Agent 之间选择时，应从简单方案开始并针对实际用例测试。
- 🎓 课程收尾：回顾可靠性、成本、上下文之间的权衡，建议持续实验与测试；完成后可获得结业证书并分享至 LinkedIn。

---

### [获取失败](https://vlt.io/blog/free-public-npm-mirror)

**原文标题**: [Failed to retrieve](https://vlt.io/blog/free-public-npm-mirror)

无法总结：获取内容失败，状态码 429。

---

### [获取失败](https://www.vlt.io/blog/registry-metadata-70-percent-smaller)

**原文标题**: [Failed to retrieve](https://www.vlt.io/blog/registry-metadata-70-percent-smaller)

无法总结：获取内容失败，状态码 429。

---

### [Proposal: experimental `node:json` module with lazy views and schema-driven decoding · Issue #67504 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/67504)

**原文标题**: [Proposal: experimental `node:json` module with lazy views and schema-driven decoding · Issue #67504 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/67504)

该提案来自 Node.js GitHub Issue #67504，建议新增受 `--experimental-json` 控制的实验性 `node:json` 模块，利用 Node.js 已内置的 simdjson，提供惰性 JSON 视图和基于 Schema 的一遍式解码，以减少只读取少量字段时 `JSON.parse()` 构建完整对象及 `Buffer.toString()` 的开销。提案包含原型与性能数据，但模块命名、默认投影行为、Schema 支持范围等仍待讨论。

- 📦 **核心问题**：大型 JSON、配置、日志和 NDJSON 常只需少量字段，但 `JSON.parse()` 会为所有值创建 JavaScript 对象，且从文件或套接字读取的字节还需先转字符串。
- ⚡ **`json.parse(input)`**：一次解析文档，但仅在被读取时创建 JavaScript 值，返回只读惰性视图；`JSONObject` 类似 `Map`，支持 `get`、`has`、`size`、遍历等，`JSONArray` 支持 `at()`、`length` 和迭代。
- 🔍 **便捷访问**：支持 `atPointer()` 使用 RFC 6901 JSON Pointer，支持 `toObject()` 转换子树，`toJSON()` 可配合 `JSON.stringify()`。
- 🧩 **`json.decode(input, schema)`**：按 JSON Schema 子集直接构建普通对象，边解析边检查类型、应用默认值，并跳过 Schema 未声明的属性。
- 📋 **Schema 子集**：支持 `type`、`properties`、`required`、`additionalProperties`、`items`、`enum`、`const`、`default`、`nullable` 和本地 `$ref`；其他验证关键字会被拒绝而非静默忽略。
- 📥 **输入类型**：两个函数均接受字符串、`Buffer`、`TypedArray`、`DataView` 或 `ArrayBuffer`。
- 🚀 **性能原型**：在 `twitter.json` 读取每个 status 的 `id` 和 `user.screen_name` 时，`JSON.parse(buffer.toString())` 约 1994µs，惰性 `json.parse(buffer)` 约 384µs，`json.decode(buffer, schema)` 约 246µs；解码更多字段时为 392µs 对 1703µs。
- ⚠️ **并非替代完整解析**：该模块不是更快的 `JSON.parse()`；转换整个文档时 V8 的 `JSON.parse()` 更快，应继续作为默认选择。
- 🗣️ **开放问题**：模块应叫 `node:json`、放入 `util`，还是采用 `node:formats/json` 等共享命名空间；`decode()` 默认丢弃未声明属性与标准 JSON Schema 行为不同；是否扩展 Schema 或考虑 JTD；视图使用 `get(key)` 而非属性访问以避免 `Proxy` 性能损失。
- 🔄 **与 `JSON.parse()` 的差异**：指数溢出如 `1e309` 会成为 `SyntaxError` 而非 `Infinity`；未配对代理项转义会成为 `SyntaxError`；接受 UTF-8 BOM。
- 🧪 **替代方案评估**：npm 原生插件需编译或预构建二进制且维护不足；解析后再验证会增加成本；Ajv JTD `compileParser()` 接近但仅支持 JTD；流式解析省内存但对可放入内存的文档更慢。
- 💬 **社区讨论**：此前相关尝试包括 #61577、#61855、#62598；多位成员表示支持，建议与 YAML、TOML 等格式讨论 #67157 一并考虑共享命名空间；作者计划在命名于 #67347 确定前先提交受实验标志控制的 PR。

---

### [推出 OpenJS 广告网络 | OpenJS 基金会](https://openjsf.org/blog/introducing-the-openjs-ad-network)

**原文标题**: [Introducing the OpenJS Ad Network | OpenJS Foundation](https://openjsf.org/blog/introducing-the-openjs-ad-network)

OpenJS 基金会宣布推出 OpenJS 广告网络，这是一个选择性加入的广告计划，旨在为参与项目及基金会创造新收入，并支持 JavaScript 生态的长期可持续发展。

- 📢 OpenJS 广告网络采用 opt-in 模式，项目可自主决定是否加入及广告位位置。
- 💰 收入将与参与项目分享，为项目和维护者提供直接资金流，同时支持基金会共享基础设施与服务。
- 🌐 首批参与者包括 Node.js、Express.js、Fastify、Lodash、webpack、jQuery 及 OpenJS 基金会官网。
- 🔒 广告以隐私为核心，不使用行为定向或第三方跟踪，力求提供开发者友好的体验。
- 🛠️ BuySellAds 负责运营和销售该网络，OpenJS 审核并批准广告主，模式类似其与 MDN 的合作。
- 🧩 OpenJS 认为开源可持续发展没有单一方案，需要会员、赞助、资助、服务和广告等多元资金来源。
- ✅ 该计划已获 OpenJS 董事会批准，并得到交叉项目委员会支持，现开始与选择参与的项目合作。
- 📬 有兴趣触达 JavaScript 开发者的广告主可通过官方渠道联系。

---

### [Buffer.poolSize default increase (24.18.0, #63597) increases steady-state memory retention under long-running HTTP server load · Issue #67235 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/67235)

**原文标题**: [Buffer.poolSize default increase (24.18.0, #63597) increases steady-state memory retention under long-running HTTP server load · Issue #67235 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/67235)

Node.js 长期运行的 HTTP/HTTPS 代理服务在升级到 24.18.0+ 后出现 `external`/`arrayBuffers` 内存持续攀升，疑似由 `Buffer.poolSize` 默认值从 8 KiB 提高到 64 KiB 引起；问题可通过显式调回 8192 缓解，但会牺牲该变更带来的吞吐收益。

- 🧩 问题版本：Node.js 24.18.0+，涉及 `buffer` 与 `http` 子系统；生产环境为 Linux arm64，但机制应与平台无关。
- 📈 生产表现：升级到 24.22.x 后，`external`/`arrayBuffers` 约每 35–45 分钟攀升至 85% 系统内存阈值，触发 ECS 回收；`heapUsed` 保持平稳，说明不是堆内存泄漏。
- 🔍 对照验证：24.13.0 或 24.22.1 中强制 `Buffer.poolSize = 8192` 时内存可稳定 plateau；仅改回该参数即可恢复旧行为，锁定 #63597 为关键变量。
- 🧪 合成复现：默认 65536 时稳态平均 RSS 约 228.8 MB、`external` 约 34.8 MB；设为 8192 时分别约 191.9 MB、21.9 MB，显示池大小单独即可造成更高内存保留。
- 🧠 疑似机制：`Buffer.allocUnsafe()` 对小于 `Buffer.poolSize` 一半的分配会从共享池 `ArrayBuffer` 切片；任一小而长寿命的 buffer 未释放，就可能钉住整个池块，64 KiB 默认值将最坏保留放大 8 倍。
- ⚠️ 负载特征：高并发 HTTP 服务中大量短生命周期请求与少量慢请求/keep-alive 混合，正好会放大共享池中混合生命周期切片的保留问题。
- ✅ 预期行为：稳定流量下 `external`/`arrayBuffers` 应趋于平台期，而不是线性增长直至进程被健康检查重启。
- 🛠️ 临时方案：运行时设置 `require('buffer').Buffer.poolSize = 8192` 可缓解，但作者不希望长期保留，因为会放弃 #63597 的吞吐改进。
- 🔗 外部佐证：Next.js #99848 也报告类似 slab pinning；LRU 统计约 10 MB 时，Node 24/8 KiB 实际 `arrayBuffers` 为 42 MB，Node 26/64 KiB 达 221 MB。
- 💡 可能修复方向：对预期长寿命的小 buffer 使用 `Buffer.allocUnsafeSlow()` 等非池化存储，避免其共享池块；也可重新评估长期运行服务器场景下的池大小默认值。

---

### [tls: docs-deprecate TLS renegotiation, add allowRenegotiation opt-in by pimterry · Pull Request #67532 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67532)

**原文标题**: [tls: docs-deprecate TLS renegotiation, add allowRenegotiation opt-in by pimterry · Pull Request #67532 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67532)

该 PR 将 TLS 1.2 重协商标记为弃用，并新增 `allowRenegotiation` 选项，为后续默认禁用和最终移除铺路；目前改动不构成破坏性变更，已合并到 `main`。

- 🧩 PR #67532 为 `tls.connect()` 和 `tls.createServer()` 增加 `allowRenegotiation` 选项，并对相关 API 做文档弃用（DEP0213）。
- ⚙️ `allowRenegotiation` 当前默认 `true`；计划在 v27 改为默认 `false`，未来仅保留客户端选择性接受服务器发起重协商的能力。
- 🔐 弃用原因是重协商难以安全使用：现有连接可在请求处理中静默改变授权状态和配置，且近年出现过相关 CVE。
- 🌐 生态趋势支持移除：TLS 1.3 已删除重协商，HTTP/2 禁止重协商，HTTP/3 不支持 TLS 1.2；BoringSSL、OpenSSL、Go、Rustls 等也大多禁用或仅有限支持。
- ⏳ 迁移方面，可使用 `--pending-deprecation` 查找受影响代码；除“客户端显式启用并接受服务器请求”外，启用重协商会触发弃用警告。
- 🏷️ 该 PR 被标记为 `semver-minor` 和 `notable-change`，获 panva、jasnell、gurgunday、mcollina 批准，提交落地为 `b7df44b`。
- 💬 讨论中提到可更快禁用甚至移除，但担心 Kibana 等真实应用的遗留用例造成破坏；后续 PR #67618 将继续推进默认禁用。

---

### [Express 现已天生可观测 · Express.js](https://expressjs.com/en/blog/2026-11-17-express-tracing-channels/)

**原文标题**: [Express is now observable by design · Express.js](https://expressjs.com/en/blog/2026-11-17-express-tracing-channels/)

overview summary  
Express 路由器现在通过 Node.js TracingChannel 发布 `express.router.request`，让 APM、日志工具和用户代码可直接观测中间件、路由处理器与 `router.param()` 回调，无需 monkey patching；该能力基于诊断通道的生命周期事件和异步上下文关联，随 Express 5 的 router v2.3.0 提供，需 Node 18.19+。

- 🧩 Express 为每个中间件、路由处理器和 `router.param()` 回调发布 `express.router.request` TracingChannel。
- 🛠️ 过去依赖 monkey patching，存在保持处理器签名、获取 app 实例、模块加载顺序和打包内联等难题，自动插桩困难且易碎。
- 🚫 普通事件发射器不够用：有额外开销、需要实例才能监听、监听器异常会归因于库，并缺少异步操作上下文关联。
- 🔄 TracingChannel 包含 `start`、`end`、`asyncStart`、`asyncEnd`、`error` 五个生命周期通道，并用 AsyncLocalStorage 自动关联异步上下文。
- ⚡ 无订阅者时发布开销极低，库还可检查订阅者以避免分配上下文对象。
- 📦 事件上下文提供 `req`、`res`、`route` 模式、`handler`、`param`、`error`、`incomingError`、`errorHandler`、`result` 等字段。
- 📈 可用于按路由模式统计延迟、精确定位出错中间件或处理器，以及为 OpenTelemetry 创建与请求关联的 span。
- 🌐 Express 加入 mysql2、node-redis、ioredis、graphql、mongoose、Nitro 等自带 tracing channel 的生态趋势。
- 🔌 对 APM 而言，可消除模块劫持、加载顺序要求和 ESM 特殊处理，频道及其上下文成为稳定契约。
- ✅ 功能随 router v2.3.0 提供，Express 5 应用已依赖该包，无需升级 Express；需 Node 18.19 或更高版本。
- 📝 鼓励库和中间件作者发布自己的 tracing channel，以低成本让生态工具理解其行为。

---

### [诊断通道 | Node.js v26.13.1 文档](https://nodejs.org/api/diagnostics_channel.html#diagnostics-channel)

**原文标题**: [Diagnostics Channel | Node.js v26.13.1 Documentation](https://nodejs.org/api/diagnostics_channel.html#diagnostics-channel)

Node.js `node:diagnostics_channel` 模块提供创建命名通道的 API，用于发布任意诊断消息；自 v15.1.0 引入、v19.2.0 起稳定。模块提供 Channel、TracingChannel、BoundedChannel 三类核心对象，并内置 Console、Crypto、HTTP、HTTP/2、模块加载、NET、UDP、进程、Web Locks、Worker 线程、SQLite 等大量开箱即用的诊断通道。

- 📡 **核心用途**：模块作者可在顶层创建一个或多个命名通道（channel），用于上报任意消息数据，供他人订阅消费；建议同步编写文档说明通道名及消息数据结构。
- 🔓 **引入方式**：支持 ESM `import diagnostics_channel from 'node:diagnostics_channel'` 与 CommonJS `require('node:diagnostics_channel')` 两种方式。
- 🏷️ **命名建议**：通道名应包含模块名以避免与其他模块冲突；推荐复用顶层通道对象而非运行时动态获取，以减少开销。
- 📢 **发布/订阅基础 API**：`hasSubscribers(name)` 检查是否存在订阅者（便于在性能敏感代码中避免昂贵的消息构造）、`channel(name)` 获取通道对象、`subscribe(name, onMessage)` 注册同步执行的处理器、`unsubscribe(name, onMessage)` 取消订阅。
- 🧵 **Channel 类**：代表单个命名通道，避免发布时查找开销；实例提供 `hasSubscribers`、`publish(message)`（同步触发处理器）、`subscribe`/`unsubscribe`，不可直接 `new Channel()`。
- 🔗 **存储绑定（实验性）**：`bindStore(store[, transform])` 将 AsyncLocalStorage 绑定到通道，`runStores(context, fn, ...)` 在指定存储上下文中执行函数并发布消息，可支持上下文关联（如 Span 父子关系）。
- 🆕 **withStoreScope(data)**（v26.1.0）：返回可释放的 `RunStoresScope`，配合 `using` 语法与 `Symbol.dispose` 管理存储上下文，无需闭包包装，作用域结束自动恢复。
- 🧭 **TracingChannel 类**（v26.8.0 稳定）：由 start、end、asyncStart、asyncEnd、error 五个通道组成，用于统一追踪单个可追踪操作的完整生命周期，`tracingChannel(name)` 创建。
- 🎯 **追踪方法**：`traceSync`（同步）、`tracePromise`（Promise/thenable，非 thenable 会告警）、`traceCallback`（按 error-first 回调约定）；另提供 `subscribe`/`unsubscribe` 批量订阅、`hasSubscribers`。
- 🔁 **事件语义**：所有事件共享同一 context 对象便于弱映射关联；完成时扩展 `result` 或 `error`；只有追踪开始前已存在的订阅者才接收事件，以保证追踪图正确。
- ⚡ **BoundedChannel 类**（v26.1.0，实验性）：TracingChannel 的简化版，仅含 start/end 两个通道，适用于不涉及异步续延或错误处理的同步操作追踪；提供 `run(context, fn)` 与 `withScope()`。
- 🖨️ **内置通道：Console**（实验性）：`console.log`、`console.info`、`console.debug`、`console.warn`、`console.error`，接收参数数组。
- 🔐 **内置通道：Crypto**（v26.9.0）：`crypto.fips.indicator` 报告 OpenSSL FIPS 提供者检测到的非批准操作，需 `--enable-fips-indicator-events` 启用，异步投递、尽力而为、非权威审计日志。
- 🌐 **内置通道：HTTP 与 HTTP/2**（实验性）：HTTP 覆盖客户端请求创建/开始/错误/响应完成及服务端请求开始、响应创建/完成；HTTP/2 覆盖客户端与服务端流的创建、开始、错误、完成、正文发送与关闭。
- 🧩 **内置通道：Modules**：`require()` 的 start/end/error 与 `import()` 的 asyncStart/asyncEnd/error，消息包含 id、parentFilename 或 parentURL。
- 🔌 **内置通道：NET、UDP、Process**：客户端/服务端套接字创建、`net.Server.listen()` 的异步生命周期、UDP 套接字、`child_process`、`process.execve` 与 spawn 追踪。
- 🔒 **内置通道：Web Locks 与 Worker Threads**：每个 `locks.request()` 产生 start/grant/miss/end 事件（含 name、mode、steal、ifAvailable、error）；新线程创建发布 `worker_threads`。
- 🗄️ **内置通道：SQLite**（v26.8.0，实验性）：`sqlite.db.query` 在语句执行完成后发布，含展开的 SQL、数据库实例与纳秒级执行时长估计；属性能剖析事件，无对应 start 事件、无异步上下文传播，无订阅者时零开销。
- ⚠️ **注意事项**：订阅处理器中抛出的错误会触发 `uncaughtException`；多个内置通道仍标记为实验性，API 可能变化；订阅 SQLite 事件时不得关闭数据库或语句。

---

### [Node.js 的绿色线程 | James M Snell](https://www.jasnell.me/posts/green-threads-in-node)

**原文标题**: [Green threads for Node.js | James M Snell](https://www.jasnell.me/posts/green-threads-in-node)

overview summary
Node.js PR #67288 引入实验性 `node:green_threads` 模块，用独立 V8 isolate 与共享 OS 线程池实现低成本、可隔离的绿色线程；它介于 worker 和 vm context 之间，适合大量小型隔离任务，但仍处早期且限制明显。

- 🧵 PR #67288 为 Node.js 增加实验性 `node:green_threads`，稳定性为 1.0 早期开发，是否保留取决于实际用途。
- ⚙️ 绿色线程由运行时调度而非操作系统；每个线程有独立 V8 isolate、堆和 GC，但不占独立 OS 线程、事件循环或 Node.js 环境。
- 🧩 所有绿色线程共享进程级 OS 线程池，默认最多 8 个线程，可用 `NODE_GREEN_THREADS_POOL_SIZE` 调整，可同时存在数千个。
- 📨 通过 `postMessage`/`onmessage`、`MessagePort`、`env` 函数和 ES 模块导出与宿主通信，支持结构化克隆、传输 `ArrayBuffer`、真实 `Error` 及 `RpcTarget`/`AbortSignal`。
- 🚫 内部没有 `require()`、`process`、文件系统、网络等 Node.js API，只能使用宿主提供的少量全局对象和模块。
- ⏱️ 任务按序执行且不抢占；长任务会占用池线程，CPU 限制按 CPU 时间计算，内存限制覆盖 JS 堆与 `ArrayBuffer`。
- 🛑 超过 `maxTaskCpuTimeMs`、`maxCpuTimeMs` 或 `maxMemoryMb` 会停止该绿色线程并触发 `error`，不影响进程其他部分。
- 🔥 `setWarmPoolSize()` 可预热 isolate，显著加快启动；示例中启动 100 个约 1.6ms。
- 🆚 对比 worker：绿色线程更轻、有独立堆、无 Node.js API；对比 vm context：更重，但堆独立且可限制内存和 CPU。
- 📊 约 1,000 个空闲实例：worker 约 6.2MB/个，绿色线程约 1.4MB/个，vm context 约 0.25MB/个；绿色线程启动约 3,700/s，热池约 83,000/s。
- 💬 消息吞吐略低于 worker；相同并行度下 CPU 密集任务速度相近，但不能超过线程池的并行能力。
- 🏢 多租户场景中，绿色线程可用少量 OS 线程承载大量租户；坏租户的无限循环、微任务循环或堆膨胀可被限制，vm pool 则可能拖垮同 worker 的其他租户。
- ✅ 适合大量小型且多空闲的隔离代码、多租户处理器、插件/扩展系统、用户脚本/规则/转换，以及需要预热启动的场景。
- ⚠️ 主要限制包括无 Node.js API、无阻塞、无抢占、无调试器、创建比 vm context 慢且更耗内存、并行受池大小限制。
- 🧷 `Atomics.wait()` 会抛错；`setStallPolicy()` 可检测池线程停滞；极少数 V8 不响应终止时，线程 1 秒后被放弃，10 秒内无法停止池线程则可能中止进程。
- 🧪 目前需构建 PR 分支并用 `--experimental-green-threads` 试用；官方希望收集使用场景和设计反馈。

---

### [src: experimental green threads implementation by jasnell · Pull Request #67288 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67288)

**原文标题**: [src: experimental green threads implementation by jasnell · Pull Request #67288 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67288)

Node.js PR #67288 提出实验性 green threads：一种轻量级 worker，拥有独立 V8 isolate，但不暴露完整 Node.js API；多个实例共享少量物理线程池，通过消息、RPC 或模块导出执行任务，并支持按实例限制 CPU、内存和终止，面向大量小型、不可信代码的低成本托管。

- 🧵 核心机制：green thread 不绑定单个 OS 线程，也不带完整 Node.js 环境；多个实例共享线程池，每个任务在独立调用上下文中运行。
- 📦 主要能力：支持 `postMessage`、`env` RPC、模块 `exports`、ES 模块与 `resolve/load` 钩子、`MessageChannel/MessagePort`、`BroadcastChannel`、`evaluate()`、`terminate()`、`close()` 和 warm pool。
- ⚙️ 资源限制：可用 `maxTaskCpuTimeMs`、`maxCpuTimeMs`、`maxMemoryMb` 限制单个实例；默认无 Node.js API，只能使用 host 传入的能力。
- 🚀 对比 worker：内存约 1.36 MB/实例，而 worker 约 6.17 MB；冷启动约快 4 倍，热池可达 65k–100k 启动/秒；1000 个租户共享 8 个线程。
- 🧠 对比 vm context：`vm` 更省内存（约 0.25 MB/租户）且启动更快，但不是安全边界；`timeout` 有每次调用成本，且一个坏租户可能拖累或杀死同 worker 的其他租户。
- 🛡️ 隔离优势：每租户有独立堆和 CPU 限制，坏租户可被单独终止；消息、RPC 参数通过结构化克隆并重建，函数和 `RpcTarget` 以桩形式暴露，降低越权风险。
- 🧩 适用场景：多租户/serverless 小处理器、插件与扩展系统、不可信用户脚本、规则/转换任务，以及大量短命或空闲代码单元。
- 🧵 不适合场景：需要 `fs`、`net`、`child_process` 等 Node API、原生插件、Inspector/CPU Profiler、重并行计算、阻塞等待或少量长生命周期实例。
- 🚧 限制与风险：默认线程池上限为 8，可用 `NODE_GREEN_THREADS_POOL_SIZE` 调整；不防时序侧信道；RPC/消息未限流；忽略终止的 JIT 循环可能导致被放弃的 isolate 泄漏。
- 🔐 权限模型：新增 `--allow-green-threads`；未授权时创建 `GreenThread` 或 `setWarmPoolSize()` 会抛 `ERR_ACCESS_DENIED`，作用域为 `green-thread`。
- 📈 性能结论：单消息往返与 worker 接近（约慢 5%）；同等并行度下 CPU 密集吞吐相近；大量租户场景因减少 OS 线程竞争，吞吐约提升 15–20%。
- 🗣️ 社区讨论：模块命名 `node:green_threads` 是否应并入 `worker_threads`/`threads` 命名空间、`env` 命名、模块 API 设计、EventTarget 重复实现等仍有争议；PR 仍属实验性。

---

### [将我们的电子邮件 API 迁移到 Go · Resend](https://resend.com/blog/migrating-our-email-api-to-go)

**原文标题**: [Migrating our Email API to Go · Resend](https://resend.com/blog/migrating-our-email-api-to-go)

Resend 将邮件 API 从 Node 重写到 Go，核心目标不是“更快”，而是在提升性能的同时完整保留既有行为：错误响应、幂等性、限流、存储数据和邮件内容都必须与旧系统一致。团队用七周、约 140 个 PR 把新服务从空项目推进到生产流量，并通过差分测试、灰度发布和基础设施调优完成迁移。

- 🚀 七周内完成约 140 个 PR，从空项目上线到生产流量；到 10 月，Go 已承载全部邮件 API 流量。
- ⚖️ 并行运行阶段，Go 的中位延迟约为 Node 的一半，每任务内存约为 Node 的七分之一。
- 🛠️ 原 Node 服务在大请求突发时会出现任务无响应：解析和序列化大请求体阻塞事件循环，甚至已被限流拒绝的请求也会消耗 CPU；S3 超时还会表现为面向客户的 408/524 错误。
- ✅ 团队构建测试 harness，用相同请求对比 Node 与 Go 的响应、错误、数据库行、S3 对象、幂等性和限流行为，并把旧实现作为兼容性基准。
- ✉️ 为保持邮件内容一致，团队没有直接采用现成 Go HTML-to-text 库，而是移植了特定行为；初始版本精确匹配全部 60 个 Node 生成的 fixture。
- 📈 上线后仍需针对生产环境调优：任务规格两次翻倍，增加整点流量峰值容量，为 S3 上传加请求级超时，并随流量增长调整 Redis 连接池。
- 📊 50% 灰度数据显示：Go 每请求 CPU 约降低 62%；POST /emails 中位延迟从 58ms 降至 31ms，p99 从 498ms 降至 420ms；峰值任务数从 34 降至 10，每任务内存从约 1.3GB 降至约 180MB。
- 🧠 工程师访谈提到，最大难点是“未知的未知”：从异步默认的 Node 到同步默认的 Go、从宽松 JavaScript 到严格 Go，以及公共 API 必须兼容所有旧输入；例如手写重建 Node Buffer 的转换逻辑。
- 🧹 团队还删除了仅为保护 Node 事件循环而存在的复杂代码，并用 HTTP 状态码分布小部件在灰度期间快速确认新旧服务行为一致。
- 🤝 两位工程师表示协作高效自主，能各自负责模块、快速实验；批处理端点从决策到进入生产流量约用了一周。

---

### [开始使用 WarpBuild | 50 美元免费额度 | WarpBuild](https://www.warpbuild.com/start?utm_source=cooperpress&utm_medium=newsletter&utm_campaign=h2-2026&utm_content=nodeweekly-2026-11-19)

**原文标题**: [Get Started with WarpBuild | $50 in Free Credits | WarpBuild](https://www.warpbuild.com/start?utm_source=cooperpress&utm_medium=newsletter&utm_campaign=h2-2026&utm_content=nodeweekly-2026-11-19)

WarpBuild 为 GitHub Actions 提供即插即用的 CI runner 基础设施，主打“改一行 YAML 即可让构建快 2 倍、成本减半”，并针对 AI 时代代码提交与 CI 流水线激增的瓶颈，提供更快缓存、跨平台支持和企业级能力。

- 🤖 AI 代理持续生成代码与 PR，提交量和流水线运行次数激增，CI 已成为开发反馈循环的瓶颈。
- ⚡ WarpBuild 构建速度约为 GitHub 托管 runner 的 2 倍，价格约为一半，同时降低计费费率与运行时长。
- 🔁 只需把工作流中的 `runs-on: ubuntu-latest` 改为 `runs-on: warp-ubuntu-latest-x64-2x`，无需重写或迁移工作流。
- 💳 注册 `app.warpbuild.com` 后，在 `Settings > Billing` 使用优惠码 `START50` 可领取 50 美元免费额度，无需信用卡，约 2 分钟完成设置。
- 🖥️ 支持 Linux、macOS、Windows，覆盖 x86-64 与 ARM64，包括 M4/M5 Pro Mac，macOS runner 并发不限。
- 🚀 相比 GitHub 托管 runner，WarpBuild 提供更快的 CPU、磁盘和 3-10 倍更快的缓存。
- ☁️ 提供 WarpBuild 云托管 runner，也支持 BYOC 部署到自有 AWS、GCP 或 Azure，并支持静态 IP 与自定义镜像。
- 🔐 企业能力包括 SOC2 Type 2 认证、临时隔离 VM、SSO、访问控制及 24x7 SLA 支持。
- 🏢 客户包括 Braintrust、Raycast、OpenRouter、Comcast、Jane Street 等；案例显示构建时间可从约 25 分钟降至 9 分钟、从 30 分钟降至 8 分钟。
- ❓ 现有 GitHub Actions 工作流完全兼容，仅需修改 `runs-on` 标签；免费额度注册兑换后立即到账。

---

### [剖析 Node.js 站点构建：各阶段的事件循环利用率](https://marisstella.app/writing/the-idle-time-was-a-missing-cache/)

**原文标题**: [Profiling a Node.js site build: event loop utilization per phase](https://marisstella.app/writing/the-idle-time-was-a-missing-cache/)

该站点构建流程将约 170 个工具、指南、研究索引和博客生成约 4,500 个页面，每次部署和站点构建测试都会运行。文章先澄清此前“主线程 57% 空闲”的测量偏差，再介绍通过缓存预热和三项小优化，把构建时间缩短约 4–5 秒，约十分之一。

- 🏗️ 构建产物规模庞大：约 170 个工具及其指南、研究索引和博客被生成约 4,500 个页面，每次部署与测试都会执行。
- ⏱️ 早期 CPU 分析显示主线程 57% 时间空闲，但无法判断空闲对应哪个 `await`，因此改用分阶段计时和事件循环利用率来定位。
- 🖼️ 首次计时运行分别为 116 秒和 89 秒，主线程仅忙碌 36% 和 43%；大部分空闲耗在绘制分享卡片上，其中一轮 44 秒、忙碌 18%，另一轮 12 秒、忙碌 3%，均在等待 worker 线程池。
- 🗂️ 这些空闲主要源于未启用卡片缓存；CI 通过 `PAGES_CARD_CACHE` 复用上次生成的卡片。缓存预热后，同一构建耗时 38.9 秒，主线程忙碌 93%，说明此前的空闲来自测量方式而非构建本身。
- 🔥 预热后的构建是 CPU 密集型，CPU 分析发现三项可低成本消除的开销：gzip 大小计算 2 秒、Python 研究索引步骤 1.9 秒、剥离内联 `data:` favicon 的正则 0.9 秒。
- ⚙️ 优化方式包括：gzip 改为在线程池中异步处理、每次 8 个文件；Python 步骤提前启动并仅在首次读取输出时等待；正则前先做廉价的 `data:` 检查。
- 📉 优化前后构建除记录构建时间的 `version.json` 外字节完全一致，离线缓存名称相同且哈希覆盖每个文件；三组交替对比中构建快 5.0–8.5 秒，最佳估计为在 39–46 秒基础上减少 4–5 秒，约十分之一。
- ✍️ 剩余成本已不是等待：五轮处理都会读取并重写全部 4,500 个页面，写入文件现已成为分析中最大的单项开销。

---

### [当漏洞链称王时，每一个安全弱点都至关重要——Liran Tal](https://lirantal.com/blog/every-security-weakness-matters-vulnerability-chaining)

**原文标题**: [Every Security Weakness Matters When Vulnerability Chaining is King â Liran Tal](https://lirantal.com/blog/every-security-weakness-matters-vulnerability-chaining)

概述总结  
文章强调：评估安全弱点不能只看单项严重性，而要判断它在真实环境中能提供什么能力、跨越什么边界、满足哪些后续前提，从而识别可被串联成高危攻击的路径。

- 🧩 **漏洞链的本质**：一个漏洞的输出成为另一个漏洞的输入或权限前提；同应用中的两个漏洞并不自动构成链，需证明能力如何传递。
- 🔗 **GitHub Enterprise 案例**：用户配置 webhook → 绕过内网限制 → 内部 Graphite 发起 URL 请求 → CRLF 注入 → Memcached 写入 → Ruby 反序列化 → 远程代码执行。
- 🚪 **ProxyLogon 的启示**：预认证 SSRF/认证绕过改变了后续“需认证文件写入”漏洞的前提；后端若信任网关设置的头部，所有可达路径都需审视。
- 📊 **优先级应看连接路径**：CVSS 仍可用于初始排序，但还需结合部署暴露、权限、可达资产和已证实攻击路径，而非只按单项分数排队。
- 🧪 **Node.js 示例**：入口固定用 POST，worker 却按 URL 参数用 GET 请求目标，说明一个组件的限制不会自动传递到下游 fetch worker。
- ✅ **修复验证要测边界**：同时验证允许目标成功、禁止内网目标失败、重定向到禁止目标被拦截，并用目标端/网络端观测确认，不能只看 502。
- ⚠️ **攻击图不能靠假设**：服务存在不等于可达，可达不等于有权限或可利用；应明确记录未知项，并优先验证最具后果的最小假设。
- 🛠️ **安全评审行动**：挑选可授予网络访问、凭据或可控写入的已接受/延期问题，记录能力与下游前提，用无害标记验证关键连接，并在修复边界保留回归测试。
- 📌 **核心结论**：单个低危发现未必需紧急修复，但“单独影响低”必须追问“利用后什么变得可达或可控”；打断一条链不等于关闭所有路径，部署变化后需重新评估。

---

### [同一个 Express 应用在 Node 26、Bun 1.4 和 Deno 2.9 上：使用相同 node_modules 的负载测试 | Huseyin Babal](https://huseyinbabal.dev/posts/node-bun-deno-express-load-test/)

**原文标题**: [One Express app on Node 26, Bun 1.4 and Deno 2.9: a load test with the same node_modules | Huseyin Babal](https://huseyinbabal.dev/posts/node-bun-deno-express-load-test/)

本文对同一个 Express 5 应用、同一份 node_modules、同一台机器上的 PostgreSQL 和相同 k6 负载进行测试，对比 Node 26.13.1、Bun 1.4.4 和 Deno 2.9.8 的实际表现。测试共完成 36 轮、3080 万次请求且 0 失败；总体看 Bun 吞吐最高、延迟最低、内存占用约为另两者一半，Deno 在有数据库时略慢于 Node，无数据库时明显落后，Node 表现居中且稳定。

- 🧪 测试保持应用代码不变，只替换运行时；Bun 和 Deno 通过 Node 兼容层运行 Express，而非使用各自原生服务器。
- 📦 依赖只在 Node 镜像中用 npm 安装一次，node_modules 原样复制到三个运行时镜像，启动命令和基础镜像不同。
- 🏢 背景是运行时归属变化：Anthropic 收购 Bun，Cloudflare 收购 Deno，Node.js 仍归 OpenJS 基金会。
- 🚀 有数据库时，Bun 比 Node 多处理约 35–37% 请求；无数据库时多约 63%。
- 🐢 Deno 在有数据库场景比 Node 慢约 3–5%，无数据库场景慢约 17%。
- ⏱️ Bun 的 p95/p99 延迟最低；例如读请求为 33.6/41.0 ms，Node 为 43.8/52.4 ms，Deno 为 51.2/62.4 ms。
- 💾 Bun 的 RSS 约为 Node 和 Deno 的一半，读请求时约 76 MiB，而 Node 约 148 MiB、Deno 约 146 MiB。
- ⚙️ 三个运行时的启动到首次 200 响应时间接近，约 1.23–1.40 秒，Bun 略快。
- 📊 每轮顺序轮换，单运行时轮次波动低于 7%；有数据库时 Node 与 Deno 的差距接近噪声，不宜过度解读。
- 🔥 应用进程基本跑满一个 CPU 核心，PostgreSQL 不是瓶颈；连接池等待队列长度在三个运行时中相近，因此不能解释 Bun 的吞吐优势。
- 🧠 无数据库测试中事件循环延迟均上升，Deno 延迟最高、吞吐最低；Bun 使用 JavaScriptCore，其 heapUsed 不宜与 V8 直接比较，RSS 更适合横向对比。
- 📂 公开仓库包含应用、Dockerfile、k6 脚本、36 份结果、Prometheus 快照和 Grafana 回放配置，可复现实验。
- ⚠️ 测试不覆盖 Bun.serve、Deno.serve、其他框架、其他数据库驱动、cluster 多进程、TLS、更大机器和 serverless 冷启动。

---

### [回放节点 26 — 回放博客](https://replay.io/blog/replay-node-26)

**原文标题**: [Replay Node 26 — Replay Blog](https://replay.io/blog/replay-node-26)

Replay Node 已正式发布（GA），基于 Node 26 构建，是支持时间旅行录制的 Node 运行时。它可以完整捕获运行时行为，并可通过 Replay MCP 代理或 Replay DevTools UI 进行时间旅行调试，尤其适合排查服务器端问题。

- 🚀 **正式发布**：Replay Node 现已普遍可用，基于 Node 26，替代此前基于 Node 16 的早期 alpha 版本。
- 🧠 **现代 Node 支持**：重建录制运行时，支持现代 Node 能力，包括通过内置 type stripping 直接运行 TypeScript 文件。
- 🔄 **跟进当前版本**：未来 Replay Node 将持续跟踪当前 Node 发行版，不再为 Node 22/24 单独维护旧构建。
- 🐧 **平台限制**：目前仅支持 Linux x86-64；没有 Windows 构建，macOS 下载仍提供旧 Node 16 运行时，未来可能支持 Mac。
- 📦 **安装方式**：全局安装 `@replayio/node`，获得 `replay-node` 命令；首次运行会下载运行时到 `~/.replay/node/node`。
- ⬆️ **升级提示**：若之前安装过，需要执行一次 `replay-node --update`，因为它不会自动检查新版本。
- 🎬 **基本用法**：`replay-node script.js` 或 `script.ts` 可运行脚本，并在进程退出时保存一份录制。
- 🖥️ **服务器录制**：使用 `replay-node --exec` 可将 Replay Node 置于 PATH 前并录制其启动的 Node 进程；示例中用 `next start` 录制 Next.js 生产服务器。
- ⚠️ **Next.js 注意事项**：构建时预渲染页面不会出现在录制服务器中；`next dev` 会启动多个进程并各自生成录制，需关注处理请求的 `start-server.js`，并可提高 `NEXT_EXIT_TIMEOUT_MS` 避免录制写入不完整。
- ☁️ **上传与源码映射**：使用 Replay CLI 的 `replayio upload` 上传录制，`replayio list` 查看本地录制；上传会包含 Next 生成的 source map，便于查看原始 TypeScript 文件。
- 🔍 **代理调试**：将录制交给连接 Replay MCP 的代理后，`RecordingOverview` 可识别框架并总结服务器处理的请求和入口点；`Logpoint` 可查看未记录的变量值；`GetStack` 可查看调用栈。
- 🧪 **示例发现**：示例中 `sendAnalyticsData` Server Action 被调用 5 次，根布局和用户布局各发送两次分析数据；通过日志点还能查看重定向时完整的 user 对象，而应用本身并未记录这些信息。
- 🛠️ **DevTools UI**：可在 Replay DevTools 中打开服务器源码，查看每行执行次数、单步调试调用、检查变量，并在事后添加打印语句查看每次运行会输出的内容。
- 🔜 **后续方向**：下一篇文章将结合浏览器录制和服务器录制，用代理同时调查 Nadia 示例应用中的前后端问题。
- 📚 **更多信息**：可安装 Replay Node 试用，完整设置见 Replay Node 文档页，也可在 Discord 反馈问题。

---

### [发布 v14.0.0 · secretlint/secretlint · GitHub](https://github.com/secretlint/secretlint/releases/tag/v14.0.0)

**原文标题**: [Release v14.0.0 · secretlint/secretlint · GitHub](https://github.com/secretlint/secretlint/releases/tag/v14.0.0)

Secretlint v14.0.0 正式发布，主打更快、依赖更少、零配置开箱即用。全量扫描大型仓库的速度比 v13.1.0 提升 7 到 24 倍，官方规则内置后可一键安装使用，大多数用户无需修改现有配置即可升级。

- 🚀 **性能大幅提升**：全量扫描大型仓库比 v13.1.0 快 7～24 倍，单文件预提交检查也快了 1.6 倍。
- 📈 **实测数据**：linux 仓库 97,265 个文件从 56.5 秒降至 2.31 秒（24.5 倍），vscode 仓库从 13.9 秒降至 758 毫秒（18.3 倍），react 仓库从 2.82 秒降至 405 毫秒（7 倍）。
- 📦 **官方规则内置**：官方规则与预设已移入 @secretlint/core，只需 `npm install secretlint` 即可，不必再单独安装几十个规则包。
- ⚙️ **零配置运行**：找不到配置文件时自动运行推荐规则而非报错，`npx secretlint "**/*"` 即可直接使用。
- 🧵 **加速原理**：规则声明各自密钥的关键字，Secretlint 一次遍历文件字节匹配全部关键字；文件多时用工作线程读取和扫描，规则仍在主线程执行以保证结果一致。
- 🌐 **仍为纯 JavaScript**：未用 Rust 重写，无原生模块或 WebAssembly，@secretlint/core 与推荐规则仍可直接在浏览器中运行，并新增 Playwright 浏览器测试。
- 📉 **依赖精简**：secretlint 的第三方运行时依赖从 69 个减至 16 个。
- 🧩 **声明式规则**：规则可用带关键字的 patterns 数据定义，替代 create() 函数，自定义 patterns 配置同样高效。
- 🔄 **平滑升级**：规则 ID 保持不变，.secretlintrc 配置继续可用；官方规则包不再发布，建议卸载旧规则包（非必需）。
- ⚠️ **破坏性变更**：结果与 JSON 输出不再包含 sourceContent；`--secretlintrc` 仅指定单个文件；`--secretlintignore` 改为相对当前目录的路径；aws 规则 `enableIDScanRule` 必须为布尔值等。
- 📊 **性能分析**：`secretlint --profile "**/*"` 现在可按阶段、规则、模式和文件输出耗时摘要。
- 👥 **贡献者**：azu、renovate、awais-ur-rehman。

---

### [Secretlint](https://secretlint.github.io/)

**原文标题**: [Secretlint](https://secretlint.github.io/)

Secretlint 是一个可插拔的 linting 工具，用于防止提交凭据，并支持使用推荐规则快速检查项目文件；其演示仅在浏览器中运行，不会将输入发送到服务器。

- 🔑 Secretlint 是可插拔的 linting 工具，旨在防止提交凭据。
- 📦 可从 `secretlint/secretlint` 获取。
- ⚡ 快速开始：运行 `npx secretlint "**/*"` 即可检查项目中的所有文件。
- ✅ 无需配置文件或规则包，默认运行推荐规则。
- 🛡️ 演示安全：输入不会发送到服务器，仅在浏览器中运行。

---

### [npkill 1.0：现代开发吃掉了你的磁盘](https://zaldih.com/en/post/npkill-1-0-0/)

**原文标题**: [ npkill 1.0: modern development ate your disk](https://zaldih.com/en/post/npkill-1-0-0/)

npkill 1.0 在发布 7 年后带来重大升级：从只清理 node_modules 扩展为清理现代开发产生的多种可丢弃目录，并新增 profiles、新界面、多选、过滤、JSON 模式与 API，同时包含若干破坏性变更；普通使用 npx npkill 的用户可基本保持原有习惯。

- 🚀 npkill 最初是 2019 年的 200 行实验脚本，如今 1.0 版本完成范式转变，目标不只是 node_modules，而是现代开发占用的磁盘空间。
- 📦 新增 Profiles：默认 node profile 包含 node_modules、.next、.nx、.angular、coverage 等；还内置 python 等约 20 种 profile，可用 -p node,python 或 -p all 启用。
- 🛡️ 敏感结果默认隐藏，通用目录名会结合上下文判断，例如 target 需邻近 Cargo.toml 或 pom.xml，.venv 需包含 pyvenv.cfg。
- 🖥️ 新界面提供 Help、Options、Delete、Info 四个可选面板，可用左右键切换；Options 可实时修改参数并自动重启搜索。
- ☑️ 多选模式可用 t 开启：SPACE 选择/取消，ENTER 删除所选，a 全选/取消全选，v 选择范围，t 退出且不删除。
- 🔍 结果过滤可按类型或路径筛选，支持正则；结合多选可批量删除过滤后的结果。
- ⚙️ .npkillrc 配置文件可设置 rootDir、defaultProfiles、自定义 profiles、exclude、sortBy、sizeUnit 等，支持项目级或用户级配置及 --config 指定。
- 🧩 自定义 profiles 支持 nextTo 与 contains 规则，避免通用目录名误报；自定义同名 profile 会覆盖内置 profile。
- 📊 新增结果计数器显示结果摘要和启用 profile，新增滚动条显示当前位置。
- 🤖 JSON 模式包括 --json 与 --json-stream，适合脚本和实时处理；结合 --targets、--delete-all、-y 可无界面删除，建议先用 --dry-run。
- 🔧 内部重构将 core 与 cli 分离，高级用户可导入 API 构建自定义实现，但 API 仍可能变化。
- ⚠️ 破坏性变更：默认 node profile 会匹配更多目录；旧行为可用 -t node_modules；--target 改为 --targets；移除 -x、--bg-color、-nu、-gb；--sort last-mod 改为 age；--delete-all 仅配合 --targets。
- 🚫 默认不再进入 .git、.nvm 等目录，未知选项会报错，需 Node.js 20.19 以上；--exclude 支持路径写法。
- ⚡ 其他改进：搜索最高快 3 倍，新增 --no-size、--no-age、--no-stats、--older-than，自动切换 MB/GB，修复非 TTY、Android、结果闪烁等问题。
- ❤️ 作者感谢全球反馈与贡献，并强调只删 node_modules 的旧用法仍可保留；可通过 npx npkill@latest 试用。

---

### [BrowserPod 4.0：运行在浏览器中的 microVM，现已免费供任何用途使用](https://browserpod.io/blog/browserpod-40/)

**原文标题**: [BrowserPod 4.0: the microVM that runs in the browser, now free for any use](https://browserpod.io/blog/browserpod-40/)

BrowserPod 4.0 发布：这是一款基于 WebAssembly、可在浏览器中运行的 Linux 类 microVM。最大变化是核心库完全免费，无需账号或 API key，无计量与遥测；同时新增 fetch 网络、Edge TCP、SSH、pnpm 12 等能力，托管代理服务 BrowserPod Edge 作为可选付费服务保留。

- 🆓 **完全免费**：BrowserPod 4.0 可作为 npm 库免费用于个人、商业和生产环境，无使用限制、无费用、无账号、无 API key、无遥测。
- ⚙️ **浏览器内 microVM**：基于 WebAssembly 的 Linux 类内核，进程运行在独立 Web Worker 中，具备流式文件系统并支持本地持久化。
- 🧰 **多语言与工具支持**：支持 Node.js、Rust、git、bash、npm、pnpm，Python 处于预览阶段，Go 即将支持。
- 🚀 **核心优势**：执行在用户设备本地完成，带来零延迟；无需云端沙箱扩容，用户越多也不会增加云成本。
- 🎯 **主要场景**：AI agents、浏览器内 IDE/Playground/文档演示，以及将 AI 辅助开发嵌入产品的平台。
- 🔐 **新许可模式**：BrowserPod Community Licence 允许免费商用；自托管、打包分发或再分发运行时需要 BrowserPod Enterprise Licence。
- 🌐 **Fetch 网络**：无需 API key，Pod 的出站 HTTP/HTTPS 请求由浏览器 `fetch()` 或自定义 fetch 实现完成；支持本地 TLS 终止与证书生成，但受 CORS 限制，暂不支持入站流量和 Portals。
- 🛰️ **Edge 网络**：原托管代理更名为 BrowserPod Edge，需要 API key；支持按 key 配置域名策略，Pro 计划可自定义域名白名单，并可在任意端口建立 TCP 连接。
- 🔑 **SSH 与网络增强**：Edge 网络支持任意端口 TCP 后，基础镜像加入 OpenSSH，Pod 可作为真实 SSH 客户端使用。
- 🦀 **基础镜像更新**：新增 Rust 编写的 `ripgrep`、`fd` 和 `pnpm 12`，提升搜索、文件查找与依赖安装体验。
- 🗺️ **后续路线图**：计划支持 Fetch 网络入站流量、Go 工具链、C/C++ SDK，以及 Python 原生模块动态加载。
- 🧪 **快速上手**：通过 `npm install @leaningtech/browserpod` 安装并调用 `BrowserPod.boot()` 即可启动；也可使用 quickstart、BrowserCode 或让编码 agent 自动集成。

---

### [Playground IDE — BrowserCode](https://browsercode.io/ide?framework=vite)

**原文标题**: [Playground IDE — BrowserCode](https://browsercode.io/ide?framework=vite)

未提供可总结的文章内容，因此暂时无法生成摘要。
- 📄 请在“Use the following content:”后粘贴需要总结的文本。
- ✍️ 收到内容后，我会按“概述 + 要点”的格式输出中文摘要。
- ✅ 要点将使用“-”符号，并为每条配上合适的 emoji。

---

### [Node.js — Node.js 27.0.0-alpha.0.1.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.1.0)

**原文标题**: [Node.js — Node.js 27.0.0-alpha.0.1.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.1.0)

Node.js 27.0.0-alpha.0.1.0 于 2026-11-12 发布，是一个 Alpha 预览版本，由 Antoine du Hamel（@aduh95）发布，包含多项 SEMVER-MINOR 功能新增、大量安全修复、依赖升级及文档与构建改进。

- 🚀 **版本信息**：Node.js 27.0.0-alpha.0.1.0（Alpha），发布日期 2026-11-12，发布者 @aduh95。
- ⏱️ **child_process（次版本新增）**：新增 `subprocess.timedOut` 属性，用于判断子进程是否因超时被终止。
- 🔐 **crypto（次版本新增）**：新增带 CSR 支持的 X.509 证书生成能力，并使 X.509 检查的防护逻辑显式化。
- 🌐 **dns（次版本新增）**：合并相同的并发 `lookup()` 请求，减少重复解析开销。
- 📊 **http（次版本新增）**：按每次解析器执行批量处理请求体 span，提升追踪效率。
- 📦 **sea（次版本新增）**：为 VFS 模块生成编译缓存，加快单文件应用启动。
- 🧵 **worker（次版本新增）**：在启动快照中预加载流，优化 Worker 启动性能。
- 🛡️ **安全修复（多处私有 PR）**：涵盖 http2 流与内存保留、TLS SNI 与恢复/重协商限制、llhttp 重入、inspector WebSocket 帧越界读取、权限模型 `fs.watch` 泄露、HTTPS Agent TLS 策略隔离等。
- 🔧 **crypto 优化**：复用 HMAC 上下文、缓存同步摘要、跳过空 OpenSSL 错误队列清理、拒绝不可变随机填充缓冲区等。
- 🧩 **FFI 改进**：支持从指针调用函数、Fast API 函数可回收、修复签名冲突与回调参数校验等。
- 📁 **fs 修复**：非普通文件的 `readFile` 可中断、符号链接解析顺序、`cpSync()` 悬空链接中止问题、UTF-8 短读溢出等。
- 🗄️ **sqlite 改进**：64 位 UDF 返回值 API、缓存 SQLTagStore 构造模板、统一 BackupJob 退出点等。
- 🔄 **依赖升级**：llhttp 9.4.4、nghttp2 1.71.0、ngtcp2 1.26.0、V8 15.6.75.50、undici 8.12.4、npm 12.2.2、amaro 1.3.0、simdjson 5.1.1、perfetto 59.1 等。
- 👥 **文档与社区**：新增协作者 efekrskl、christianaurichzm 及贡献者 Philipp Dunkel，并修正多处文档说明。
- 🏗️ **构建与工具**：分离交叉编译的主机/目标 Rust 产物、同步 Torque 输出与 V8、更新 nixpkgs 固定版本、增加 Nix 变更汇总表等。
- 💻 **下载支持**：提供 Windows x64/ARM64、macOS Apple Silicon、Linux x64/PPC64LE/s390x/ARM64、AIX 等安装包与二进制文件，macOS Intel 二进制“即将推出”。
- 🔑 **校验信息**：发布页面附带 SHA256 校验值与 PGP 签名，便于验证下载完整性。

---

### [获取失败](https://github.com/nodejs/node/commit/33d4e6c73a)

**原文标题**: [Failed to retrieve](https://github.com/nodejs/node/commit/33d4e6c73a)

无法总结：获取内容失败，状态码 503。

---

### [Node.js — Node.js 27.0.0-alpha.0.1.1 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.1.1)

**原文标题**: [Node.js — Node.js 27.0.0-alpha.0.1.1 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.1.1)

Node.js 27.0.0-alpha.0.1.1（Alpha）于 2026-11-16 发布，由 @aduh95 发布；这是预发布版本，包含工具、构建、依赖、文档和测试方面的更新，并提供多平台安装包、二进制文件、源码和校验信息。

- 🚀 版本信息：Node.js 27.0.0-alpha.0.1.1（Alpha），发布日期为 2026-11-16，发布者为 @aduh95。
- 🔐 重要变更：在 darwin tarball 中，对 `bin/node` 执行公证（notarize），以提升 macOS 分发安全性（#67143）。
- 🛠️ 构建更新：使用 `--shared-simdutf` 时，不再包含 vendored simdutf；Linux 启用 PIE（#67410、#67386）。
- 📦 依赖更新：包含多项 V8 backport 或 cherry-pick，并将 nghttp3 升级至 1.19.0。
- 📚 文档更新：修复 releases.md 拼写问题，补充安全发布 steward、SQLite 数字与 BigInt 绑定、无效 X509 有效期、package exports fallback arrays、TLS 回调 `this` 绑定等说明。
- 🧪 测试改进：修复并稳定 watch mode、TLS resume、FIPS 下 fs stat cancel 等相关测试，以减少 flaky（时好时坏）。
- 🧰 工具更新：`review_backport.sh` 支持多提交 PR，mk-ca-bundle 更新至 1.35，yamllint 启用 strict mode。
- 💻 下载与校验：提供 Windows、macOS、Linux、AIX、ARMv8 等平台安装包或二进制文件，以及源码、文档和 PGP 签名 SHA256 校验；macOS Intel 64-bit Binary 显示为“即将推出”。

---

### [发布 v1.66.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.66.0)

**原文标题**: [Release v1.66.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.66.0)

v1.66.0 是 Mediabunny 的一次大规模稳定性与正确性更新，合并了 #636，包含 400+ 项改进和修复，几乎覆盖所有模块；这些修复来自为期数周的 LLM 辅助全代码库审计，目标是让库更可靠、更健壮、更“开箱即用”。

- 🚀 发布 v1.66.0，重点不是新增单一功能，而是系统性修复潜在缺陷、提升格式兼容性与运行时稳定性。
- 🆔 `InputTrack.id` 改为 `getTracks()` 中的 1-based 索引，确保多段 Matroska 文件中唯一；新增 `getFirstTimestampOrNull()` 和 `computeDurationOrNull()`，无包轨道返回 `null`。
- 🧩 新增多项格式能力：WAV `appendOnly`、HLS `targetDuration: Infinity`、混合 fragmented MP4、ISOBMFF 64 位浮点 PCM、MOV 中 MP3、无 `ftyp` 的 ISOBMFF、`srat`、Matroska 标题元数据、Ogg start trimming、VBRI、AAC PCE、6.1/7.1 AAC、ID3v2.2 `TXX`、HLS `fLaC` CODECS 等。
- 🛠️ 大幅修复 ISOBMFF/MP4：高采样率读写、PCM 跨帧丢数据、`tfdt` 漂移、并发 fragment 读取泄露未解密数据、`saio` 偏移、`pssh` 去重、fragmented muxer 关键帧和 `moov` 写入顺序、4 GiB 以上 `mdat`/chunk offset、`fastStart` 内存/预留问题、WebVTT 时间、MOV 中 AC-3/E-AC-3/MP3 兼容性等。
- 📦 修复大量 Matroska/WebM 问题：HE-AAC 采样率、旧版 AAC、TrueHD  seeking、引用块、AV1 `av1C`、`DisplayUnit`、立体视频尺寸、cluster 截断、多段轨道编号、未知大小 segment、投影元数据、lacing 时间戳、`DocTypeVersion > 4`、EBML 未知大小、muxer 负时长/大元素/`BlockDuration`、WebM WebVTT、VP9 色彩空间被改写等。
- 📡 修复 MPEG-TS：B 帧 DTS/PTS、HEVC AUD、PID 稳定性、首个 AAC 包失败后的半初始化、PAT/PMT 解析、init 输入、`getNextPacket` 竞态、open-GOP、伪 ADTS 同步字、音频时间戳漂移、直播延迟、负时间戳等。
- 🎧 改进 Ogg：`negativeTimestampSupport` 默认 `prefer-non-negative`，移除端部裁剪，修复 Vorbis framing bit、不同采样率轨道按时间交织、header page 顺序、granule 定位、截断文件、MIME `codecs=""` 等。
- 🎵 修复 FLAC：支持 2^32 以上总采样数、12/64 kHz 无包、并发 `getFirstPacket()` 索引损坏、`getPacket()` 浮点误差、非 ASCII PICTURE、单帧最小块大小、`onFrame` 校验等。
- 🌊 修复 WAVE：头部夸大/占位数据大小、未 finalize 文件、4 GiB 以上 RF64、data 后 chunk、精确时间戳取包、RIFF INFO UTC/UTF-8、奇数长度 padding、`WAVE_FORMAT_EXTENSIBLE`、`fact` chunk 等。
- 🎼 修复 MP3/ADTS/ID3：Xing/Info 帧计数与 CRC、CBR 码率、Layer I/II、保留位误同步、junk 检测、ID3v1/APEv2 时长、ADTS 非法配置、ID3v2.2/2.3/2.4 多种解析问题、日期统一 ISO 8601、封面 MIME/重复、BPM 0 等。
- 📺 修复 HLS：variant 引用未定义 media group、`CHANNELS`、I-frame playlist、相对 URL 解析、live 时间线/断点/init data、VOD target duration、重名 rendition、`fastStart: 'reserve'`、成对轨道拆分、HLS MP3 Xing、`CODECS`/`BANDWIDTH`/`RESOLUTION`/`FORCED` 等。
- 🔍 改进输入与探测：`computeDuration()` 不再把无包轨道算到 0，修复 `hasHighDynamicRange()` 误报、`computePacketStats()` 无穷速率、单瞬时包转换、帧率检测、64 位 `ftyp` 识别、已释放 `Input` 错误类型等。
- 🌐 修复数据源：`RangedSource` 长度语义、`FilePathSource` 文件句柄/短读/`read` 事件、`UrlSource` Range/headers/空资源/重试/错误消息、`CustomSource` 并发 `getSize`/流取消、`ReadableStreamSource` 释放取消等。
- 📤 修复输出与目标：取消输出时关闭未启动的 `StreamTarget`、`Output.cancel()` 错误处理、finalize 资源释放、`start()` 失败自动取消、`getMimeType()` 挂起、`FilePathTarget` 写失败句柄泄漏、chunked `StreamTarget` 栈溢出、`AppendOnlyStreamTarget` 不触发 `finalized` 等。
- 🎚️ 修复媒体源与编码器生命周期：MediaStream 源背压计数、非法添加同步抛错、关闭竞态、编码器失败/刷新/错误吞掉、`finalize()` 无轨道成功、首帧负时间戳关键帧、`sizeChangeBehavior`、`VideoTransformOptions.alpha`、Canvas/MediaStream 帧泄漏等。
- 🖼️ 修复样本处理：`AudioSample` 原始数据复制、`VideoSample` 奇数宽度色度列、可见矩形偏移、RGB/BGR 转换越界、`drawWithFit()` 裁剪、`transform()` 丢编码选项、YUV 转换失败泄漏、`SharedArrayBuffer`、空样本复制等。
- 🎞️ 修复编解码细节：隔行 AVC 高度、HEVC SPS 参考图像、AVC SPS、VP9 RGB、AV1 level、`avcC` 扩展、`hvcC` SEI 数组、HEVC 默认 `hvc1`、ProRes 色彩信息、7.1 E-AC-3、DTS-ES/DTS 96/24、AAC 默认 AAC-LC、`canDecode*` 缓存/泄漏等。
- 🔄 修复转换流程：DTS/TrueHD 扩展包提示、取消/失败状态、`done` 早于 finalize、track option 索引、trim 零时长帧、TrueHD 起始音频、PCM 回退、进度 NaN、长静音内存占用、隐式 HE-AAC 延迟起始等。
- 🧪 修复事件与 WebVTT：嵌套 emit 中 `once` 监听器重复/死循环、`EncodedPacket.clone()` 保留旧 `byteLength`、AES-128 HLS 失败后内存残留、无 payload cue、超过 99 小时 cue、BOM 解析等。
- ⚡ 各扩展包改进：`@mediabunny/server` 多线程编解码；AAC/FLAC/MP3/AC-3/DTS/TrueHD 更快并修复 worker 内存泄漏、重试、通道映射、采样率/位深/时间戳、编码器复用、DTS 512 样本延迟、TrueHD 静音填充、ProRes alpha/色彩/刷新、server 端 4 通道 AAC、`require()` 崩溃、`VideoSample.transform()` 等问题。

---

### [Bug fix mania by Vanilagy · Pull Request #636 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/pull/636)

**原文标题**: [Bug fix mania by Vanilagy · Pull Request #636 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/pull/636)

该合并请求是 Vanilagy/mediabunny 的“Bug fix mania”大型修复合集，将 61 个提交从 `bug-fix-mania` 分支合并到 `main`，集中修复容器解析/封装、HLS、MPEG-TS、Matroska、Ogg、WAVE、MP3/ADTS/FLAC、ID3 元数据、输入输出、媒体样本、编解码器及扩展包中的大量缺陷，并关闭多个相关 issue。

- 📦 PR #636 由 Vanilagy 合并，包含 61 个提交，3 项检查通过，合并后删除 `bug-fix-mania` 分支。
- 🐛 集中修复 #631、#633、#634、#630、#635、#642 等多个问题，覆盖 ID3、HLS、AVC SPS、FLAC、MPEG-TS、VP9 等关键场景。
- 🧩 核心 API 调整：`InputTrack.id` 改为 `getTracks()` 中的 1-based 索引；新增 `getFirstTimestampOrNull()` 和 `computeDurationOrNull()`，并改进时长/包统计。
- 📦 新增多项格式能力：WAVE append-only、HLS `targetDuration: Infinity`、混合 fragmented MP4、ISOBMFF 64-bit float PCM、无 `ftyp` 文件、`srat` box、Matroska 标题、Ogg start trimming、VBRI、ID3v2.2 `TXX`、HLS `fLaC` CODECS 等。
- 🎬 ISOBMFF/MP4 修复：高采样率、PCM 跨帧丢数据、`tfdt`/`saio`/`pssh`、fragmented MP4 关键帧与 `moov` 顺序、4 GiB `mdat`、`fastStart` 内存/预留模式、WebVTT `ctim`、24-bit FLAC 描述等问题。
- 📺 Matroska/WebM 修复：多段文件轨道编号、未知大小 segment、投影元数据、lacing 时间戳、`DocTypeVersion > 4`、空元素默认值、EBML 未知大小、AAC/AV1/TrueHD 解析、muxer 大元素和 `BlockDuration` 等问题。
- 📡 MPEG-TS 修复：B 帧 DTS/PTS、HEVC 分隔符、PID 稳定性、PAT/PMT 解析、并发 `getNextPacket()` 竞态、音频 PES 延迟、时间戳漂移、ADTS/HEVC 边界处理等。
- 🎵 Ogg/FLAC/WAVE/MP3/ADTS 修复：Ogg 头页/交错/seek/截断、FLAC 大样本数与并发索引、WAVE 占位大小与 >4 GiB、MP3 Xing/同步/垃圾字节、ADTS 非法配置和 ID3 中断等。
- 🏷️ 元数据/ID3 修复：ID3v2.2/2.3/2.4 的 unsynchronisation、非 synchsafe 帧长、日期/封面/注释解析，统一日期为 ISO 8601，修复封面重复和 BPM 0 等问题。
- 📶 HLS 修复：variant/media group、I-frame playlist、相对 URL、query 参数、fMP4 时间戳回绕、live 窗口滑动、`EXT-X-MAP`、`CODECS`/`BANDWIDTH`/`RESOLUTION`、HLS 输出断言失败等。
- 🔌 输入/输出与 Source/Target 修复：`Output.cancel/start/finalize` 资源释放、`StreamTarget`/`FilePathTarget` 句柄泄漏、`UrlSource` 重试与 Range、`RangedSource`/`CustomSource` 行为、LRU 缓存和读取事件等。
- 🎞️ 媒体样本/编解码修复：AVC/HEVC/VP9/AV1 解析、HDR 误报、PCM 时间戳漂移、`VideoSample`/`AudioSample` 复制/转换/颜色空间/alpha、编码器关闭与背压等问题。
- ⚙️ 扩展与性能：`@mediabunny/server` 多线程编解码；AAC/FLAC/MP3/AC3/DTS/TrueHD 扩展修复内存泄漏、通道映射、时间戳、flush 重用和编码质量问题；同时改进 tree shaking。
- ✅ 整体上这是一次覆盖面极广的稳定性与兼容性修复，重点提升多格式读写正确性、HLS/MPEG-TS 实时流可靠性、元数据解析一致性以及 I/O 资源管理安全性。

---

### [Release 8.23.0 · websockets/ws · GitHub](https://github.com/websockets/ws/releases/tag/8.23.0)

**原文标题**: [Release 8.23.0 · websockets/ws · GitHub](https://github.com/websockets/ws/releases/tag/8.23.0)

ws 项目发布 8.23.0 版本，新增 `maxPendingAutoPongs` 选项，并修复可导致远程内存耗尽的 DoS 安全漏洞；漏洞由多名报告者负责任披露，旧版本可通过限流加心跳或设置 `autoPong=false` 缓解。

- 🚀 版本：`8.23.0`，由 `lpinca` 于 11 月 12 日发布，包含 7 次提交。
- ✨ 新功能：引入 `maxPendingAutoPongs` 选项。
- 🛡️ 安全修复：修复远程内存耗尽 DoS 漏洞。
- ⚠️ 攻击方式：恶意对端持续发送 Ping 帧并停止读取，迫使自动 Pong 帧不断缓冲，最终导致内存耗尽和进程终止。
- 🙏 漏洞披露：该漏洞由多名报告者负责任披露。
- 🔧 缓解措施：受影响旧版本可结合限流与心跳，或设置 `autoPong=false`（如可用）。

---

### [发布 v26.0.0 · semantic-release/semantic-release · GitHub](https://github.com/semantic-release/semantic-release/releases/tag/v26.0.0)

**原文标题**: [Release v26.0.0 · semantic-release/semantic-release · GitHub](https://github.com/semantic-release/semantic-release/releases/tag/v26.0.0)

semantic-release 发布 v26.0.0（2026-11-16），带来错误修复、功能增强与多项破坏性变更；核心包括集成 @semantic-release/core 引擎、升级 npm 相关依赖、提高 Node.js 最低版本要求，并加强认证校验和分支状态检查。

- 🏷️ 发布信息：v26.0.0 由 github-actions 发布，包含自上一版本以来的 5 个提交，提交 c3f59b4 已通过 GPG 签名验证。
- 🐛 错误修复：处理 DEP0169 弃用问题；升级 npm 插件至新 beta 版本；修复 release 触发问题。
- ⚙️ CI 维护：更新 Node.js 引擎版本和测试矩阵。
- ✨ 新功能：在 verifyAuth 中实现 tags push 的 dry-run，并隔离分支状态检查（关闭 #3437）。
- 🧩 架构集成：集成 @semantic-release/core 引擎（#4334）。
- ⚠️ 破坏性变更：Node.js 最低版本要求为 v26.13.0；npm CLI 升级至 v12。
- 🔐 行为变更：在推送权限验证后，semantic-release 会检查本地分支是否与远程仓库分支保持同步。
- 📦 其他：发布页面显示 2 个资源。

---

### [使用 semantic-release 自动化你的发布。| Semantic Release](https://semantic-release.org/)

**原文标题**: [Automate your release with semantic-release. | Semantic Release](https://semantic-release.org/)

semantic-release 可实现发布流程全自动化，自动完成版本管理、发布说明生成与包发布，并严格遵循语义化版本规范，适合在 CI/CD 中运行且支持插件扩展。

- 🚀 全自动发布：无需手动步骤，自动判断下一版本号、生成发布说明并发布包。
- 🔢 语义化版本：严格遵循 SemVer，避免人为情绪影响版本号。
- ⚙️ CI/CD 集成：在发布分支每次成功构建后于 CI 环境运行，保证发布一致可靠。
- 🧩 插件扩展：通过插件支持任意包管理器和语言，并可用共享配置实现简单、可复用的设置。

---

### [发布 v3.0.0 · sindresorhus/nano-spawn · GitHub](https://github.com/sindresorhus/nano-spawn/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · sindresorhus/nano-spawn · GitHub](https://github.com/sindresorhus/nano-spawn/releases/tag/v3.0.0)

nano-spawn v3.0.0 是一次包含破坏性变更的版本，核心是要求 Node.js 22，并用新的 `input` 选项取代 `stdin`/`stdio` 中的 `{string: '...'}`；同时集中修复了 Windows 批处理参数、取消与子进程失败上报、`.pipe()`/`SIGPIPE`、迭代挂起和内存增长等问题。

- ⚠️ 破坏性变更：要求 Node.js 22；移除 `stdin` 和 `stdio` 选项中的 `{string: '...'}`，改用 `input` 选项。
- ➕ 新增 `input` 选项，例如 `await spawn('gh', ['auth', 'login', '--with-token'], {input: token})`；`input` 不能与 `stdin` 或 `stdio` 同时使用。
- 🔁 迁移方式：`stdin: {string: 'unicorn'}` 改为 `input: 'unicorn'`；若 `stdio` 首项是 `{string: '...'}`，改用 `input` 配合 `stdout`/`stderr`。
- 🪟 修复 Windows 批处理文件参数被双重转义的问题，避免 `mvn.cmd`、`sdkmanager.bat` 等收到多余的 `^` 字符。
- 🛑 修复取消子进程时的过早拒绝：使用 `signal` 取消会等待子进程退出和流关闭后再拒绝，错误中包含最终输出；若子进程忽略终止信号，Promise 保持 pending。
- 🚨 修复未上报的子进程失败：stdio 流错误会立即拒绝；迭代不再因流仍打开而挂起，也不会在单个流失败时丢行。
- 🔗 修复 `.pipe()` 错误、警告和 `SIGPIPE` 处理：目标提前停止读取时使用目标结果，源错误保留在 `pipedFrom`；无效 `stdin`/`stdout` 会抛出 `SubprocessError`；一个源管道到多个目标不再触发 `MaxListenersExceededWarning`。
- 🐛 其他修复包括：`--inspect-port` 值被误当脚本执行、macOS/Linux 上误替换 `node.exe`/`NODE`、提前 `break` 导致挂起、单流迭代内存增长、Windows 可执行检测缓存过期、相对 `PATH` 按子进程 `cwd` 解析，以及 `result.command` 中的控制字符转义。

---

### [发布 v8.0.0 · sindresorhus/quick-lru · GitHub](https://github.com/sindresorhus/quick-lru/releases/tag/v8.0.0)

**原文标题**: [Release v8.0.0 · sindresorhus/quick-lru · GitHub](https://github.com/sindresorhus/quick-lru/releases/tag/v8.0.0)

quick-lru v8.0.0 是一次包含破坏性变更、功能改进与多项修复的版本，重点包括要求 Node.js 22、统一迭代顺序、加强最大容量与过期时间校验，并新增 Map 风格的插入方法及修复驱逐、迭代和 TypeScript 类型问题。

- ⚠️ 破坏性变更：要求 Node.js 22。
- 🔁 `.keys()`、`.values()` 和迭代器（`for…of`、展开）现在与 `.entries()`、`.forEach()` 一致，按从最旧到最新顺序遍历。
- 📏 `maxSize` 无效时抛出 `TypeError`，`.resize()` 同样适用；必须是大于 0 的整数或 `Infinity`。
- ⏱️ `maxAge` 为负数或 `NaN` 时抛出 `TypeError`，不再接受负值或静默视为不过期。
- 🧹 `onEviction` 改为在条目移除后调用，而非移除前。
- ➕ 新增 `.getOrInsert()` 和 `.getOrInsertComputed()`，行为类似 upsert 提案中的同名 `Map` 方法。
- 🧩 `.forEach()` 回调第三个参数类型改为 `QuickLRU` 实例，而非 `Map`。
- 🛠️ `Options` 类型参数改为可选。
- 🐛 修复 `.set()` 覆盖仍缓存条目时错误调用 `onEviction`。
- 🐛 修复反复调用 `.evict()` 导致缓存无限增长。
- 🐛 修复 `onEviction` 读取过期条目时的无限递归。
- 🐛 修复迭代期间缓存变化导致跳过条目或访问循环中新增条目的问题。
- 🧾 修复 TypeScript 5.6+ 类型问题，使 `QuickLRU` 可赋值给 `Map`，并补齐 `.keys().map()` 等迭代器辅助方法类型。

---

### [发布 v4.0.0 · sindresorhus/debounce · GitHub](https://github.com/sindresorhus/debounce/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · sindresorhus/debounce · GitHub](https://github.com/sindresorhus/debounce/releases/tag/v4.0.0)

sindresorhus/debounce 发布 v4.0.0（11 月 14 日 19:30），包含破坏性变更、TypeScript 类型改进与多项修复；升级时需特别注意 Node.js 版本和 wait 参数校验变化。

- 🚀 发布 v4.0.0 最新版本，汇总破坏性变更、改进和修复。
- ⚠️ 破坏性变更：要求使用 Node.js 22。
- ⏱️ 对定时器无法处理的 wait 抛出 RangeError，包括 NaN、非数字字符串和大于 2147483647（约 24.8 天）的值。
- 🔄 此前 NaN 会导致完全不等待，过大的值会每毫秒重新设置定时器；现在改为抛出错误。
- 🧩 不同实例调用共享原型上的防抖方法时不再抛错。
- 📝 TypeScript 类型保留 readonly rest 参数，修复 `(...values: readonly number[]) => …` 形式无法调用的问题。
- 🐞 修复 `.flush()` 在 immediate 调用后再次以无参数方式调用函数的问题。
- 🐞 修复 `.trigger()` 在 immediate 模式已结束的 wait 中执行调用、丢弃函数对防抖函数的调用、以及函数抛错后再次执行的问题。

---

### [发布 v5.0.0 · sindresorhus/crypto-hash · GitHub](https://github.com/sindresorhus/crypto-hash/releases/tag/v5.0.0)

**原文标题**: [Release v5.0.0 · sindresorhus/crypto-hash · GitHub](https://github.com/sindresorhus/crypto-hash/releases/tag/v5.0.0)

crypto-hash v5.0.0 已发布，包含破坏性变更、输入兼容性增强，以及工作线程相关问题的修复。

- 🚨 破坏性变更：要求使用 Node.js 22。
- ⚠️ 非法的 `outputFormat` 现在会以 `TypeError` 拒绝；此前除 `'hex'` 外的值会静默返回 `ArrayBuffer`，导致 `{outputFormat: 'base64'}` 这类拼写错误不易被发现。
- ✅ 现在接受 `SharedArrayBuffer` 及共享内存视图作为输入。
- 🌐 现在接受来自其他 realm 的 `ArrayBuffer`，例如 `node:vm` 或 iframe 中的对象。
- 🧾 对不支持的输入会以清晰的 `TypeError` 拒绝，而不是抛出内部错误。
- 🐛 修复输入无法发送到 worker thread 时进程永不退出的问题。

---

### [发布 v0.41.0 · nvm-sh/nvm · GitHub](https://github.com/nvm-sh/nvm/releases/tag/v0.41.0)

**原文标题**: [Release v0.41.0 · nvm-sh/nvm · GitHub](https://github.com/nvm-sh/nvm/releases/tag/v0.41.0)

nvm v0.41.0 已发布为最新版本，包含自上一版本以来的 30 个提交；发布标签和提交均由 Jordan Harband 的 GPG 签名验证。该版本新增按版本类别筛选、LTS 状态记录和远程版本别名标注，并集中修复安装流程、缓存校验、凭据安全、路径/Windows/WSL、Shell 兼容性等大量问题，同时通过减少 fork、优化 grep/awk 和增强 CI 测试来提升性能与可靠性。

- 🚀 新功能：支持按 `alpha`、`lts`、`non-lts`、`iojs` 类别选择版本，并默认排除 alpha。
- 🏷️ `nvm alias` 可存储 `--lts` 和 `--lts=<name>`，并记录每个 Node 版本的 LTS 状态。
- 🔍 `nvm ls-remote` 会标注 `node` 别名和本地别名；新增 `nvm_has_italics` 检测终端斜体支持。
- 🛠️ 修复 `nvm install` 对 `--alias`、`--default`、`--save` 及 `./configure` 选项的处理，并避免污染调用者的 `NVM_NO_PROGRESS`、`TMPDIR`。
- 🔐 安全与缓存：仅在校验和通过后写入归档缓存；更谨慎地传递 `NVM_AUTH_HEADER`，掩码镜像凭据并限制重定向范围。
- 🧩 兼容性修复：处理符号链接 `.nvmrc`、CRLF、带反斜杠的 `NVM_DIR`、Windows/WSL、嵌套会话 PATH、bash 3.2 和 zsh 等问题。
- ⚡ 性能优化：减少 fork，优化 `grep`/`awk` 使用，zsh 下使用 `printf` 内建，读取 `/etc/os-release` 替代 `uname -a`。
- 📚 文档与测试：更新 README、cdnvm、Docker 说明，改进 CI 容器缓存、镜像和超时，补充 macOS/WSL 及单元测试覆盖。
- ✅ 发布页显示 3 个资产，获得 5 人共 5 个反应（4 个 🎉、1 个 ❤️）。

---

### [ONVIF](https://agsh.github.io/onvif/)

**原文标题**: [onvif](https://agsh.github.io/onvif/)

该库是面向 Node.js 的通用 ONVIF 客户端，提供 TypeScript + Promise API，支持 WS-Discovery、WS-Security、HTTP Digest 认证、懒加载服务模块，并针对多厂商摄像头兼容性做了适配。它覆盖 Profile S/T/G/M/C/A/D 相关服务，也可用于门禁、录像、分析等非摄像头设备。

- 📦 **安装要求**：需要 Node.js 18+，通过 `npm install onvif` 安装；发布包已包含编译后的 `build/`、类型声明、README、LICENSE 和 CHANGELOG，无需克隆仓库。
- 🧩 **模块与类型**：同一构建支持 CommonJS、ESM 和 TypeScript；提供 `onvif/compatibility`、`onvif/interfaces/*` 等子路径与类型化 WSDL 接口。
- 🚀 **快速开始**：创建 `Onvif` 实例后先调用 `connect()`，再调用 `device`、`media`、`ptz` 等服务方法，完成后调用 `close()`；也支持 `autoConnect: true`。
- 🔐 **认证与发现**：支持 WS-Security、HTTP Digest（MD5/SHA-1/SHA-256/SHA-512-256）以及 WS-Discovery 局域网设备探测。
- 🎥 **媒体与 PTZ**：连接时会探测媒体配置和视频源，默认使用 `activeMediaProfile`，可通过 `setActiveMediaProfile()` 切换；支持 RTSP/快照 URI 处理。
- 🚪 **非摄像头设备**：支持 Profile C/A/D 门禁与门控、Profile D 外部授权、Profile G 录像回放、Profile M 分析等场景。
- 🌐 **NAT 与地址重写**：`preserveAddress` 可将 XAddr 重写到构造地址；`rewriteUri()` 用于修正 RTSP/快照 URI 的主机地址。
- 🛰️ **Discovery 探测**：`Discovery.probe()` 默认双栈、多网卡探测，按 EndpointReference 去重，支持超时、类型/作用域过滤和状态诊断。
- 🧱 **服务命名空间**：包含 `device`、`events`、`media`、`media2`、`ptz`、`imaging`、`recording`、`replay`、`search`、`doorControl`、`accessControl`、`analytics` 等懒加载服务，`events` 为急切加载。
- 📤 **返回值规则**：SOAP 响应会自动解包；单字段返回该值本身，多字段返回对象，列表始终为数组，分页 `*List` 保留 `items`/`nextStartReference`。
- 📡 **事件订阅**：`onvif.on('event')` 启动全局拉点订阅；可用 `Subscription` 自定义主题过滤器，并自行调用 `unsubscribe()`。
- 🧪 **错误与兼容性**：提供类型化错误；已测试 ACTi、Axis、Dahua、Hikvision、Reolink、TP-Link 等多厂商设备，已知兼容性问题见 `quirks.md`。
- 📚 **文档与迁移**：提供 TypeDoc、`innerDocs/` 深入文档和示例；旧 `Cam` API 可通过 `onvif/compatibility` 或 `onvif@previous` 迁移。
- ⚖️ **免责声明**：项目为独立开源 ONVIF 客户端，与 ONVIF 官方无关联，也不声称通过 ONVIF 认证。

---

### [面向开发者的视频后端 — 快速添加视频 | Hyperserve](https://hyperserve.io/?utm_source=nodeweekly&utm_medium=newsletter&utm_campaign=classified_nov19)

**原文标题**: [Video backend for Developers — Add Video Fast | Hyperserve](https://hyperserve.io/?utm_source=nodeweekly&utm_medium=newsletter&utm_campaign=classified_nov19)

Hyperserve 是面向开发者的视频托管 API：支持接收用户上传的任意格式视频，自动转码并通过全球 CDN 分发，帮助应用快速加入视频能力，避免复杂后端、专有播放器和意外账单。集成流程为创建上传、客户端直传、完成后排队转码，覆盖上传、转换、托管、交付全流程，并提供 Webhook、文档与在线演示，按用量付费。

- 🚀 快速集成：后端创建视频记录并获取上传 URL，客户端无需 API Key 直接上传，随后调用完成接口触发转码。
- 🔄 全流程能力：上传支持公开/私有视频、自定义分辨率和缩略图；转换输出设备优化 MP4；托管提供全球低延迟 CDN；交付可在运行时获取合适分辨率 URL。
- 📦 输入兼容：支持 MP4、MOV、AVI、MKV、WEBM、WMV、M4V、MPG，单文件最高 5 GB。
- 🎚️ 输出灵活：输出 MP4，分辨率覆盖 144p 到 8K。
- 🔔 Webhook 通知：转码成功后可收到事件载荷，包含各分辨率状态和 CDN 视频 URL。
- 🧩 开发者友好：提供清晰文档、复制粘贴代码、API 参考和实时上传转码播放演示。
- 🛡️ 降低风险：无播放器锁定，平台只提供 URL，UI 由开发者掌控；无需视频专业知识；定价可预测，仅按使用量付费。
- 🎯 适用场景：社交与创作者内容、市场平台、SaaS 与内部工具、健康与健身等需要视频的应用。
- 💰 免费套餐：$0/月，10 个视频，单文件 200 MB，50 GB 带宽/月，免费编码，完整 API 访问。
- 📈 按量付费：免费编码，$0.04/GB 存储，$0.025/GB 带宽，完整 API 访问，无最低消费或承诺。
- ⏱️ 上线主张：免费开始，一个下午即可集成，快速交付视频功能并回归核心产品开发。

---

### [Odds API SDKs: Python, Node.js, PHP, Go, R, CLI and MCP - Odds-API.io](https://docs.odds-api.io/guides/sdks)

**原文标题**: [Odds API SDKs: Python, Node.js, PHP, Go, R, CLI and MCP - Odds-API.io](https://docs.odds-api.io/guides/sdks)

概览摘要
Odds-API.io 官方提供覆盖完整 v3 REST API 的多语言 SDK，包括 Node.js/TypeScript、Python、PHP、Go、R，以及命令行工具和 MCP 服务器。所有 SDK 均支持赛事、赔率、收盘赔率、结算、高尔夫独赢盘、博彩公司 ID 映射等完整功能，并保留服务器原始错误信息，部分还内置 WebSocket 实时流客户端。

- 📦 **官方包齐全**：提供 Node.js/TypeScript、Python、PHP、Go、R 五种语言 SDK，另有 CLI 工具和 MCP 服务器，均可通过 npm、pip、composer、go get、CRAN 等渠道安装。
- 🔑 **统一鉴权**：所有包需使用付费计划的 API Key，通过 `ODDS_API_KEY` 环境变量配置即可。
- 🌐 **完整 API 覆盖**：每个 SDK 覆盖全部 v3 公共端点，包括赛事、赔率、赔率摘要、收盘赔率、结算与评分、高尔夫独赢盘、参与者、市场及博彩公司 ID 映射。
- ⚡ **实时 WebSocket 支持**：Node.js、Python、Go 提供 WebSocket 客户端，支持断线重连并从最后 `seq` 恢复，配合 REST 快照实现实时赔率流。
- 🐍 **Python 特色**：同步与异步客户端、可选 pandas 数据帧和 WebSocket 扩展，要求 Python 3.8+。
- 📘 **Node.js 特色**：TypeScript 优先，支持 ESM 和 CommonJS，内置 `OddsWebSocket` 及异步迭代器，要求 Node.js 18+。
- 🐘 **PHP 特色**：支持命名参数、分页生成器、Guzzle 或任意 PSR-18 客户端，要求 PHP 8.1+。
- 🐹 **Go 特色**：每次调用均带 `context.Context`，类型化请求与响应，`oddsws` WebSocket 客户端，仅依赖标准库，要求 Go 1.22+。
- 📊 **R 特色**：所有函数返回整洁数据框，已在 CRAN 发布为 `oddsapiio` 包。
- 💻 **命令行工具**：`odds-api-cli` 可在终端查询赛事、赔率、价值投注和套利，支持表格或 JSON 输出。
- 🤖 **MCP 服务器**：版本 1.8.3 提供 33 个工具，覆盖全部公共 v3 端点，支持 Claude、Cursor、VS Code 等 MCP 客户端，并附带 AI 代理指南。
- 🏌️ **高尔夫独赢盘**：属付费附加功能，未开通时返回 403，各 SDK 会抛出对应的 `ForbiddenError`、`AddOnRequiredError` 等类型。
- 📜 **收盘赔率**：支持最多 10 个联赛、单次请求最长 366 天，SDK 迭代器自动分页获取。
- 🛠️ **错误处理完善**：各 SDK 保留服务器原始错误消息，区分限流、禁止访问、未找到等类型，并支持可选的重试与退避策略。
- 📈 **Google Sheets 插件**：可在电子表格中无需代码获取实时赔率，支持侧边栏、`=ODDS()` 公式和一键模板。

---

### [GitHub - Agent-Field/CodeAF：面向开放模型的开源软件工厂 · GitHub](https://github.com/Agent-Field/CodeAF)

**原文标题**: [GitHub - Agent-Field/CodeAF: Open-Source Software factory for Open Models · GitHub](https://github.com/Agent-Field/CodeAF)

CodeAF 是 AgentField AI 推出的开源编码代理平台，面向开放模型，以单一 Go 二进制提供“软件工厂”式工作流：集中管理多项目与对话，自动拆解、执行、测试和合并任务，并兼顾低成本、远程协作与自动化。

- 🏭 定位：面向开放模型的编码 harness 与开源软件工厂，采用 Apache 2.0 许可，目前为早期预览版。
- 🏆 基准表现：在 DeepSWE 的 113 个真实 GitHub issue 上，同模型对比十个 harness 排名第一，领先 Claude Code、Codex 等，且每解决一个 issue 的成本最低。
- 💻 安装与模型支持：单 Go 二进制，约 53 MB；支持一键脚本安装，可连接 OpenRouter、Codex/ChatGPT、DeepSeek、GLM、Kimi、MiniMax、Qwen、Ollama 及 OpenAI 兼容端点。
- 🪟 单窗口管理：home 汇总所有项目、对话、待处理事项、未读、运行状态和花费；tab 切换，alt+k 跳转，各项目可独立设置审批规则、模型和预算。
- 🧩 自然语言拆任务：一句话可拆成多个任务，分别在独立仓库副本和分支运行；通过检查后自动合入你的分支，不碰 main、dev 或 release 分支。
- 🏗️ 工厂式流水线：自动评估工作量、拆分、并行执行、测试和合并，只在必须时提问；需人工决策的事项集中在“needs you”。
- 🛠️ 子专家 harness：内置 senior-dev、sec、review 等专家，分别用于改代码、本地安全审计和 GitHub PR 审查；结果回传聊天，并支持保存重复工作流。
- 🤖 多模型 crew：每个任务由 worker、planner、checker 等席位协作，默认自动选模；/crew 可固定模型、限制开放权重模型、设置单任务和每日预算。
- 🔐 模型池与遥测：Model Pool 默认关闭，开启后仅发送匿名、无文本的模型评分数字；遥测默认发送匿名使用计数，绝不发送提示词、代码、路径等信息，可通过设置或环境变量关闭。
- ⏰ 自动化与无头模式：支持提醒、定时任务和监控；提供 do、exec、run 无头命令，适合 CI、cron 和脚本，并可输出 JSON 与退出码。
- 🌐 远程与移动：屏幕在本地、对话在工作机；通过 ssh 连接远程 devbox，断线可重连，文件双向传输，手机终端也能加入同一会话。
- ⚡ 性能：磁盘占用 53 MB，单会话 RAM 约 27 MB，16 个空闲会话约 507 MB，恢复 50 轮会话约 145 ms，显著小于同类工具。

---

### [框架性能 | 框架性能](https://frameworks.e18e.dev/)

**原文标题**: [Framework Performance | Framework Performance](https://frameworks.e18e.dev/)

Framework Performance 项目旨在比较现代 Web 框架的真实构建成本，关注开发者启动项目时继承的内容，以及应用运行时用户与服务端的体验；通过标准化测试呈现权衡，帮助框架作者迭代优化元框架，并延续 E18E 改善 JavaScript 生态的使命。

- 🎯 项目通过持续扩充的测试集和社区支持，帮助识别框架的性能取舍；测试问题或新想法可在 GitHub 仓库提交 issue。
- 🧩 测试分为开发期（Dev Time）与运行期（Run Time）两大部分。
- 🛠️ Dev Time 测量依赖数量、node_modules 大小、构建与安装时间、开发服务器启动、core-js polyfill、浏览器基线、最低 Node 版本。
- 🚀 Run Time 测量 Lighthouse 客户端/服务端渲染、初始加载、服务端吞吐、SSR 负载测试、SS 框架路由链接负载测试，以及 Core Web Vitals。
- 📈 Core Web Vitals 覆盖 LCP、CLS、FCP、TTFB、INP，并分别统计桌面端与移动端。
- ⚙️ Dev Time 与 Run Time 测试在 CI 流水线运行，结果保存为 JSON 供 Astro 文档站点加载，Methodology 页面说明指标采集方法。
- 🗂️ 项目追踪所有主版本与次版本，统计展示最新版本，并可在各框架详情页查看随时间变化。
- 🏗️ 所有测试与统计生成由基础设施合作伙伴 Depot 执行，以保证一致性、公平性与速度。
- 📦 当前测量框架及版本包括 Astro 7.4.12、Next.js 16.4.6、Nuxt 4.6.4、Pracht 1.0.0、React Router 8.5.1、SolidStart 2.2.2、Solid 2.0 2.0.0、SvelteKit 3.2.0、TanStack Start 1.169.5、Void 1.10.0。

---

### [Bun v1.4.5 | Bun 博客](https://bun.com/blog/bun-v1.4.5)

**原文标题**: [Bun v1.4.5 | Bun Blog](https://bun.com/blog/bun-v1.4.5)

Bun v1.4.5 是一个安全版本，主要更新 lsquic、c-ares、SQLite、llhttp 和 BoringSSL，并修复 HTTP/3、TLS 与 DNS 相关的安全问题。

- 🔐 该版本包含针对 HTTP/3、TLS 和 DNS 的安全修复。
- 🌐 受影响协议与 API 包括 HTTP/3、HTTP/1.1、TLS、DNS、Zstandard，以及 `Bun.serve`、`Bun.connect`、`Bun.dns`、`Bun.zstdDecompress`、`node:tls`、`node:https`、`node:http`、`node:quic`、`node:dns`、`node:zlib`、`fetch`、`DecompressionStream`。
- 📦 底层依赖升级：lsquic 从 4.9.4 升至 4.11.2，c-ares 从 1.34.8 升至 1.34.9，SQLite 从 3.53.4 升至 3.54.1，llhttp 从 9.4.2 升至 9.4.4，BoringSSL 更新至 2026 年 11 月版本。
- 🗄️ SQLite 3.54 不再允许 `ALTER TABLE` 添加、重命名或删除名为 `rowid`、`oid` 或 `_rowid_` 的列，并会在 `DEFAULT` 表达式中调用 `setAuthorizer()` 回调；macOS 上 Bun 使用系统 SQLite。
- 🛠️ 修复 HTTP/3 和 `node:quic` 的多项稳定性问题。
- 🔑 修复 `node:crypto` 中使用 SHA-3、SHA-512/224、SHA-512/256 和 RIPEMD-160 的 RSA 签名抛出 `ERR_OSSL_RSA_UNKNOWN_ALGORITHM_TYPE` 的问题。
- 📜 未知签发者的过期证书现在会像 Node.js 一样报告 `CERT_HAS_EXPIRED`；`allowPartialTrustChain` 配合 `crl` 时要求证书链以自签发证书结束。
- ✅ 自定义根证书验证更严格，部分旧证书会被拒绝；Bun 内置根证书不受影响。
- 🙌 感谢 4 位贡献者：@aphrody-dev、@dylan-conway、@Jarred-Sumner、@robobun。

---

### [Text.js | 控制台框架](https://textjs.org/)

**原文标题**: [Text.js | The Console Framework](https://textjs.org/)

Text.js 是一个“控制台框架”，用于在 `console.log` 中渲染全栈 React 应用；它把 App Router、组件、键盘交互和服务端渲染能力带入浏览器 DevTools，同时也支持终端和编码代理运行。

- 🚀 快速开始：运行 `bunx create-text-app` 创建应用，页面可直接在控制台中预览和交互。
- ⚛️ 技术底座：基于 React 19，支持并发渲染、Suspense 和错误边界；App Router 提供路由、前进/后退和深链。
- 🧩 组件体系：提供布局、数据表格、列表、树、Markdown、图表、表单控件、对话框和键盘快捷键等组件。
- ⌨️ 键盘输入：按键、粘贴和 IME 组合输入通过隐藏 `<textarea>` 传入应用，并支持焦点与 Keymap。
- 🖥️ 渲染管线：自定义 reconciler → Yoga 布局 → CellBuffer 绘制 → 脏行门控 → RLE 编码 → 单次 `console.log` 输出。
- ⚡ 性能优化：未变化帧不会触发日志；单行编辑约 0.011ms，空闲帧 0 次调用，3200 个单元格编码为 149 个 `%c` span。
- 📉 避免闪烁：Turbolog 采用追加帧而非每帧清空控制台，显著降低空白率。
- 🌐 服务端渲染：`runtime = "server"` 可在服务端渲染路由和异步组件，浏览器仅加载 21kB gzip 帧播放器，并支持 PPR、中间件和缓存。
- 🚢 部署与运行：支持 `static`、`bun`、`vercel`、`cloudflare` 适配器；`text run` 可在终端运行，`text mcp` 可让编码代理读取和操作帧。
- 🛠️ 开发工具：提供 DevTools 扩展、VS Code 预览、ESLint 插件、测试工具、TX 错误码、控制台 REPL、RTL 和 FIGlet 字体支持，并可在 DevTools 中运行 OpenCode Lite。
- 🎓 学习资源：免费课程共 10 章，约 65 分钟，覆盖入门、布局、输入、路由、数据、测试、终端运行和发布。

---

### [jQuery 4.1.0 与 3.8.0 发布：薪火相传 | 官方 jQuery 博客](https://blog.jquery.com/2026/11/17/jquery-4-1-0-and-3-8-0-released-passing-the-torch/)

**原文标题**: [jQuery 4.1.0 and 3.8.0 Released: Passing the Torch | Official jQuery Blog](https://blog.jquery.com/2026/11/17/jquery-4-1-0-and-3-8-0-released-passing-the-torch/)

jQuery 于 2026 年 11 月 17 日发布 4.1.0 与 3.8.0。4.1.0 是 4.x 系列首个次要版本；3.8.0 是 3.x 最后一次计划内功能发布，之后 3.x 仅接收关键安全与缺陷修复。官方鼓励升级到 4.x，并提供升级指南与 jQuery Migrate 插件协助迁移。

- 🚀 4.1.0 与 3.8.0 同步发布，可通过 jQuery CDN 和 npm 获取，也提供 slim 构建；第三方 CDN 会稍后跟进。
- 🔁 3.8.0 是 3.x 的“告别版”，并非 3.x 回归活跃开发；未来 3.x 只做关键修复，4.x 才是主要开发方向。
- 🧩 两个版本共有改进：AJAX transport 的 completeCallback 支持传入单个对象，便于未来扩展；选择器修复 ReDoS 漏洞，并统一使用宽松 document 比较。
- 🆕 4.1.0 为 jqXHR 增加 responseURL；支持序列化与表单关联的自定义元素；CSS 方法可在非 XHTML XML 文档中正常工作。
- ⚡ 4.1.0 内部全面改用 querySelectorAll，修复若干选择器问题；快速选择路径更严格，非法转义按规范解码为 U+FFFD；uniqueSort 去重优化到 O(N)。
- 🧷 3.8.0 支持 hidden="until-found"；正式弃用 jQuery 原型上的 push/sort/splice 以及 jQuery.expr[":"]、jQuery.expr.filters，Migrate 可提示迁移。
- 🛠️ 3.8.0 回移多个 4.0.0 修复：.html() 支持自移除脚本、cleanData 清理、<col> 尺寸、leverageNative 原生事件健壮性、CSS zoom 与隐藏 iframe 的支持测试等。
- 🙌 官方感谢提交补丁、报告缺陷和参与测试的贡献者及整个 jQuery 团队。

---

