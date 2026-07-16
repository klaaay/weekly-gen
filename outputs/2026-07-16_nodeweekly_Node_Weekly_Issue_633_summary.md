### [交互式可视化：追踪单个 HTTP 请求约 200 毫秒的完整生命周期——DNS、TCP、TLS、内核、Node 事件循环、Postgres 及返回过程](https://200ms.thenodebook.com/#act-0-prologue)

**原文标题**: [An interactive visualization that follows a single HTTP request through its entire ~200ms life — DNS, TCP, TLS, the kernel, Node's event loop, Postgres, and back](https://200ms.thenodebook.com/#act-0-prologue)

概述总结：本文探讨了人工智能在医疗领域的应用，包括诊断辅助、药物研发和个性化治疗，同时强调了数据隐私和伦理挑战。

- 🩺 人工智能通过分析医学影像（如 X 光片、CT 扫描）提升疾病诊断的准确性和效率。
- 💊 加速药物研发过程，通过模拟分子交互和预测药物效果，缩短新药上市时间。
- 🧬 实现个性化治疗，根据患者基因、病史和生活方式定制治疗方案，提高疗效。
- 🔒 面临数据隐私挑战，需要严格保护患者健康信息，防止数据泄露和滥用。
- ⚖️ 引发伦理问题，如算法偏见可能导致医疗资源分配不均，需建立监管框架。

---

### [Node.js 是什么](https://www.thenodebook.com/node-arch/what-is-nodejs)

**原文标题**: [What Node.js Is](https://www.thenodebook.com/node-arch/what-is-nodejs)

Node.js 是一個基於 V8 引擎和 libuv 的 JavaScript 執行環境，專為伺服器端程式、CLI 工具和自動化腳本而設計，其架構可分為 V8、libuv、Node 核心 API 和用戶套件四大部份。

- 🏗️ **四大核心組件**：V8 負責 JavaScript 解析與執行，libuv 處理事件循環與非阻塞 I/O，Node 核心 API 提供 `node:fs` 等模組，用戶套件則透過 npm 擴充功能。
- ⏳ **非阻塞 I/O 模型**：Node 採用事件驅動、非阻塞架構，主線程僅執行 JavaScript，慢速 I/O 操作（如檔案讀取）交由 libuv 執行緒池處理，完成後再回調主線程。
- 🔄 **事件循環機制**：libuv 的事件循環管理定時器、I/O 輪詢和回調佇列，確保主線程在等待外部操作時仍可處理其他請求，避免傳統執行緒阻塞問題。
- ⚙️ **原生綁定橋樑**：Node 核心 API 透過 C++ 綁定連接 JavaScript 與原生程式碼，例如 `fs.readFile()` 呼叫會經過 libuv 的執行緒池執行檔案系統操作。
- 📦 **npm 生態系統**：npm 提供全球最大的軟體註冊庫，但依賴管理需謹慎，`left-pad` 事件凸顯供應鏈風險，鎖定檔案和套件審查是生產環境的必要措施。
- 🛠️ **廣泛應用場景**：Node 不僅用於後端服務，還支援 CLI 工具、桌面應用（如 Electron）、伺服器無伺服器平台（如 AWS Lambda）及前端建置工具（如 Vite）。
- ⚠️ **阻塞 vs 非阻塞範例**：阻塞伺服器使用 `busyWait()` 佔用主線程 500 毫秒，導致請求排隊；非阻塞伺服器透過 `setTimeout()` 釋放主線程，同時處理多個請求。

---

### [构建持久的 AI 代理系统 | Master.dev](https://master.dev/courses/agent-harness/?utm_source=email&utm_medium=newsletter&utm_campaign=cooperharness)

**原文标题**: [Build Durable AI Agent Systems | Master.dev](https://master.dev/courses/agent-harness/?utm_source=email&utm_medium=newsletter&utm_campaign=cooperharness)

本课程由 Netflix 高级工程师 Scott Moss 主讲，深入讲解如何为 LLM 构建生产级 Agent Harness（代理框架），涵盖持久化执行、安全沙箱、记忆系统和多代理编排等核心内容。

- 🎯 **课程核心**：将脆弱的 AI 代理演示升级为可恢复、可信赖、可安全部署的生产级系统，重点在于 Harness 基础设施而非代理本身
- 🛠️ **基础构建**：使用 Vercel AI SDK 和 TypeScript 搭建基础代理循环，实现工具调用、流式响应和实时 UI 更新
- 🔄 **持久化执行**：通过 NeonDB 和 DBOS 工作流系统实现会话中断后无缝恢复，所有步骤结果缓存至数据库
- 🔒 **安全沙箱**：创建隔离的代码执行环境（runCode 工具），保护主机系统安全，支持复杂运算如退款计算
- 🧠 **记忆管理**：实现对话摘要压缩和上下文水化策略，防止 token 限制，支持清除持久化事件日志
- 🤝 **多代理编排**：构建分诊代理、账单代理等专业子代理，支持代理间交接（Handoff）和并行任务分发
- 👁️ **监督机制**：引入"计划模式"，由监督代理创建执行计划，分派只读调查员子代理并行处理不同领域任务
- 👤 **人机协作**：预留人工审批接口（如退款操作），确保关键任务的可控性
- 🏆 **课程价值**：完成课程可获得证书，掌握前沿 AI 工程技能，助力职业发展至高级工程师

---

### [Fetch 需要错误代码 | James M Snell](https://www.jasnell.me/posts/fetch-needs-error-codes)

**原文标题**: [Fetch Needs Error Codes | James M Snell](https://www.jasnell.me/posts/fetch-needs-error-codes)

以下是对您提供的文章内容的总结：

概述：本文探讨了 Fetch API 在网络错误处理上的不足，特别是它无法区分 HTTP/2 和 HTTP/3 中不同类型的流重置错误。作者提出通过 TC39 的 Error 对象 `code` 属性提案，为 Fetch 错误添加结构化错误代码，从而让开发者能够安全地重试请求或采取其他恰当操作。

- 📡 **问题核心**：Fetch 规范将所有网络失败（如 DNS 解析失败、TLS 握手错误、流重置等）统一归为 `TypeError`，丢失了关键的诊断信息。
- 🔍 **有价值的错误码**：HTTP/2 和 HTTP/3 定义了多种错误码，其中 `REFUSED_STREAM`（HTTP/2）和 `H3_REQUEST_REJECTED`（HTTP/3）明确表示服务器未处理请求，可以安全重试。
- 🔄 **QUIC 的额外维度**：HTTP/3 基于 QUIC，支持独立的 `RESET_STREAM`（停止发送响应）和 `STOP_SENDING`（停止接收请求体），Fetch 无法区分这两种情况。
- 🧱 **Fetch 规范的现状**：网络错误被设计为信息毁灭的漏斗，所有错误在内部都是结构相同的“网络错误”，最终只产生一个无附加信息的 `TypeError`。
- 💡 **错误码提案**：TC39 正在推进为 `Error` 对象添加 `code` 属性的提案，允许通过 `new TypeError("message", { code: "ERR_HTTP_REQUEST_REJECTED" })` 传递结构化错误码。
- 🛠️ **提案如何帮助 Fetch**：如果 `TypeError` 可以携带 `code`，Fetch 规范就可以在现有错误表面传播协议错误信息，而无需引入新的 API 或错误类型。
- 📋 **错误码分类**：文章提出了一套与协议版本无关的错误码分类，包括流级错误（如 `ERR_HTTP_REQUEST_REJECTED`）、连接级错误（如 `ERR_HTTP_GOAWAY`）、方向性重置码和传输层错误码。
- 🔒 **安全考量**：在浏览器中，某些错误码（如 DNS 解析失败、TLS 错误）可能泄露跨源信息，应仅在同源或服务器端运行时暴露。
- 🧪 **Fetch 规范的修改**：需要修改网络错误概念、内部算法和 API 边界，以支持错误码的传递，同时确保安全过滤。
- ⏰ **时机**：该提案将在本月 TC39 全体会议上考虑推进，Fetch 错误报告缺口是推动该提案的具体用例之一。

---

### [Ant，一个轻量级的 JavaScript 运行时](https://antjs.org/)

**原文标题**: [Ant, a lightweight JavaScript runtime](https://antjs.org/)

本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了其在诊断、治疗和健康管理中的优势与挑战。

- 🩺 人工智能通过分析医学影像（如 X 光、CT）提升疾病诊断的准确率和效率，尤其在早期癌症检测中表现突出。
- 💊 在个性化治疗中，AI 可基于患者基因数据推荐最优药物方案，减少试错成本。
- 📊 健康管理方面，AI 驱动的可穿戴设备能实时监测生命体征，预警慢性病风险。
- ⚠️ 主要挑战包括数据隐私问题、算法偏见以及医疗人员对 AI 决策的信任度不足。
- 🔮 未来趋势：AI 与医生协作模式将更普及，但需完善法规与伦理框架以确保安全应用。

---

### [从 Express 到 Fiber：迁移指南 | Fiber](https://docs.gofiber.io/blog/express-to-fiber-guide/)

**原文标题**: [From Express to Fiber: A Translation Guide | Fiber](https://docs.gofiber.io/blog/express-to-fiber-guide/)

以下是您提供的文章摘要，包含概述和重点列表：

从 Express 迁移到 Fiber 的指南。Fiber v3 的 API 深受 Express 启发，路由、参数和中间件链的写法非常相似。本文通过对比表格，详细介绍了请求读取、响应写入、中间件链和错误处理等核心操作的对应关系，并指出了三个可能导致 Bug 的关键差异：Fiber 的上下文会被回收、错误作为值返回而非抛出异常、以及 Go 的并发模型（每个请求一个 goroutine）与 Node.js 不同。

- 📖 **Hello World 结构差异**：Express 分离 `req` 和 `res`，而 Fiber 将它们合并为单一的上下文 `c`，且处理器必须返回 `error`。
- 🛣️ **路由语法高度一致**：参数（`:id`）、可选参数（`:slug?`）和通配符（`*`）的写法完全相同，Fiber 还额外支持路由约束（如 `:id<int>`）。
- 📦 **模块化路由**：Express 使用 `express.Router()`，Fiber 使用 `Group` 方法，功能等价。
- 📥 **读取请求**：Fiber 的 `c.Params()`、`c.Query()`、`c.Get()` 等与 Express 的 `req.params`、`req.query`、`req.get` 一一对应。Fiber 通过 `c.Bind().Body(&dst)` 统一处理 JSON 和表单请求，无需单独配置 body-parser 中间件。
- 📤 **写入响应**：`c.JSON()`、`c.Status(404).JSON()`、`c.SendString()` 等与 Express 的 `res.json()`、`res.status(404).json()`、`res.send()` 直接对应，并推荐使用命名常量（如 `fiber.StatusNotFound`）而非数字状态码。
- ⛓️ **中间件链**：Express 使用 `next()`，Fiber 使用 `c.Next()`。由于 `c.Next()` 返回 `error`，在中间件中实现“后处理”逻辑（如记录耗时）比 Express 的 `res.on('finish')` 事件监听更简洁。
- 🚨 **错误处理**：这是最大的概念转变。Express 通过 `next(err)` 传递错误，Fiber 则要求处理器直接 `return error`，并通过全局的 `ErrorHandler` 配置统一格式化错误响应。`fiber.NewError()` 用于创建自定义错误。
- 🗂️ **静态文件服务**：Fiber 通过 `static.New("./public")` 中间件实现，与 Express 的 `express.static('public')` 功能相同，并额外支持压缩、字节范围和缓存控制。
- 🐛 **三大关键差异**：
    - **上下文会被回收**：`c.Params()`、`c.Query()` 等返回的值仅在处理器返回前有效。在 goroutine 或异步操作中使用这些值前，必须进行拷贝（如 `strings.Clone`）。
    - **错误是值，panic 是崩溃**：预期内的错误通过 `return error` 处理，而 `panic` 会直接终止请求。必须安装 `recover` 中间件，并将捕获到的 panic 视为需要修复的 Bug。
    - **并发模型反转**：Node.js 是单线程事件循环，禁止阻塞；Go 是每个请求一个 goroutine，允许阻塞但需要为共享状态（如缓存、计数器）加锁或使用 channel。

---

### [GitHub - gofiber/fiber: ⚡️ 受 Express 启发的 Go 语言 Web 框架](https://github.com/gofiber/fiber)

**原文标题**: [GitHub - gofiber/fiber: ⚡️ Express inspired web framework written in Go · GitHub](https://github.com/gofiber/fiber)

Fiber 是一个基于 Fasthttp、受 Express 启发的 Go 语言高性能 Web 框架，强调零内存分配和快速开发。

- ⚡️ **高性能**：基于最快的 Go HTTP 引擎 Fasthttp，优化零内存分配，性能极佳。
- 🚀 **快速入门**：安装简单（Go 1.25+），通过 `go get` 即可使用，示例代码快速创建服务器。
- 🎯 **丰富特性**：支持稳健路由、静态文件服务、中间件、WebSocket、SSE、模板引擎等。
- 💡 **Express 风格**：设计哲学借鉴 Express，降低 Node.js 开发者学习曲线，提供熟悉的方法和原则。
- 🔧 **零分配警告**：`fiber.Ctx` 值默认不可变，需在处理器内使用，避免引用以优化性能。
- 🤖 **基准测试**：经 TechEmpower 测试，性能表现卓越，详情见 Wiki。
- ⚠️ **兼容性**：因使用 unsafe，需 Go 1.25+；支持 `net/http` 和 Express 风格处理器，但原生 Fiber 处理器性能最佳。
- 📚 **丰富示例**：提供路由、静态文件、中间件、CORS、JSON、WebSocket、SSE 等实用代码示例。
- 🧬 **内置及外部中间件**：包含 adaptor、cors、logger 等内置中间件，以及 contrib、storage 等外部模块。
- 👍 **社区贡献**：鼓励通过 GitHub Star、赞助、撰写教程等方式支持项目。
- 💻 **开发工具**：提供 Makefile 命令（如 lint、test、benchmark）确保代码质量。
- ☕ **赞助支持**：开源项目依赖捐赠，支持者包括月度赞助商和一次性赞助者。
- 📄 **许可证**：MIT 许可证，免费开源，Logo 采用 CC BY-SA 4.0 许可。

---

### [NodeConf EU 2026 | 意大利博洛尼亚](https://nodeconf.eu/)

**原文标题**: [NodeConf EU 2026 | Bologna, Italy](https://nodeconf.eu/)

以下是您提供的 NodeConf EU 2026 会议内容的摘要：

概述总结
NodeConf EU 2026 将于 9 月 29-30 日在意大利博洛尼亚举行，为期两天，聚焦 Node.js 技术深度与社区交流。会议包含演讲、社交活动及晚宴，门票已包含社交晚宴。活动由多家赞助商支持，包括 Platformatic、Socket 等。

- 🗓️ 会议日期与地点：2026 年 9 月 29-30 日，意大利博洛尼亚 Hotel Savoia Regency 酒店
- 🎤 核心内容：两天技术演讲与“走廊交流”，聚焦 Node.js 运行时、平台、工具、可观测性、架构及生产系统
- 🍝 社交晚宴：9 月 29 日晚提供全席社交晚宴（含食物与葡萄酒），已包含在门票内，无需额外付费
- 👥 社区参与：汇聚维护者、工程师、库作者及 JavaScript 产品团队，强调面对面交流与深度讨论
- 🎟️ 门票与信息：可通过官网预订 2026 年门票，获取场地详情、地图及 YouTube 演讲回放
- 📢 社交媒体：可通过 X、Bluesky、LinkedIn 关注活动更新与社区动态
- 🤝 赞助商：包括 Platinum（Platformatic）、Diamond（待公布）、Gold（Socket、nxtedition）、Silver（待公布）及支持伙伴（OpenJS Foundation、Sentry 等）
- 🌍 社区伙伴：CityJS London、ZurichJS、BolognaJS、GrUSP 等

---

### [NodeConf EU 2026](https://ti.to/apropos/nodeconf-eu-2026)

**原文标题**: [NodeConf EU 2026](https://ti.to/apropos/nodeconf-eu-2026)

以下是对 NodeConf EU 2026 的摘要：

NodeConf EU 2026 将于 2026 年 9 月 29 日至 30 日在意大利博洛尼亚举行，这是欧洲历史最悠久的 Node.js 会议首次从爱尔兰小岛迁至博洛尼亚。会议将在萨沃亚·里根西酒店（一座 18 世纪别墅）举办，提供会议中心、餐厅、户外泳池和免费停车位。会议聚焦 Node.js 生态系统的性能、AI 开发、供应链安全及治理挑战，门票有限且不可退款。

- 🌍 会议迁至意大利博洛尼亚，新场地为萨沃亚·里根西酒店，拥有 10,000 平方米公园和 18 世纪别墅风格
- 🎯 会议注重思想碰撞，汇聚开发者、维护者和贡献者，为期两天，包含演讲和深度交流
- 🗓️ 2026 年 9 月 29 日至 30 日，上午 9 点至下午 6 点
- 🚀 议程涵盖 Node.js 性能扩展、AI 驱动开发、软件供应链安全和治理挑战
- ✈️ 交通便利：博洛尼亚机场（BLQ）距离场地 9 公里，博洛尼亚中央火车站连接主要城市，酒店靠近 A14 高速公路
- 🏨 酒店提供会议优惠房价，但住宿不包含在门票中，需尽早预订
- 🎫 门票数量有限，售完即止，不可退款，含增值税，可更改姓名至活动前一周
- 📧 购票后通过电子邮件获取发票说明，由 Apropos 代表 NodeConf EU 销售

---

### [Node.js 20 将于 2026 年 10 月 1 日停止支持 - Vercel](https://vercel.com/changelog/node-js-20-is-being-deprecated)

**原文标题**: [Node.js 20 is being deprecated on October 1, 2026 - Vercel](https://vercel.com/changelog/node-js-20-is-being-deprecated)

概述总结
- 📅 2026 年 10 月 1 日起，Vercel 将弃用 Node.js 20 用于构建和函数。
- 🔍 可通过 `vercel project ls --update-required` 命令查看受影响的项目。
- ✅ 现有部署不受影响，仅新部署会受影响。
- 🚫 2026 年 10 月 1 日后，Node.js 20 将在项目设置中禁用，新部署会报错。
- ⬆️ 可通过项目设置或 `package.json` 的 `engines` 字段升级 Node.js 版本。
- 🤖 可委托编码助手自动升级项目至 Node.js 24。
- 📦 若无法及时升级，可使用 Docker 容器化部署，固定 Node.js 20 镜像。
- ⚠️ 容器化部署需自行管理 Node.js 版本和安全更新。

---

### [代理与反射 - Piccalilli](https://piccalil.li/blog/proxy-and-reflect/)

**原文标题**: [
  Proxy and Reflect - Piccalilli
](https://piccalil.li/blog/proxy-and-reflect/)

本文介绍了 JavaScript 中的 Proxy 构造函数和 Reflect 对象，展示了如何拦截和重定义对象的基本操作，并提供了实用示例。

- 📘 **核心概念**：Proxy 允许创建代理对象，拦截目标对象的内部方法（如 `[[Get]]`、`[[Set]]`），通过 handler 对象中的陷阱函数自定义行为。
- 🔧 **基本用法**：`new Proxy(target, handler)` 创建代理，handler 定义陷阱函数（如 `get`、`set`），可修改属性访问或赋值结果。
- 🚫 **可撤销代理**：`Proxy.revocable()` 创建可撤销代理，调用 `revoke()` 后代理与目标断开，无法恢复。
- 🛡️ **Reflect 对象**：提供与陷阱同名的静态方法（如 `Reflect.set`），确保操作符合规范并返回正确布尔值，避免违反对象不变性。
- 💡 **实际应用**：可用于数据验证（如只允许字符串）、状态追踪（如记录属性访问次数）或构建响应式状态系统，无需第三方库。
- ⚠️ **注意事项**：Proxy 强大但易破坏对象基本行为，需谨慎使用；Reflect 提供安全护栏，推荐在陷阱中调用对应方法。

---

### [Telegram 无服务器](https://core.telegram.org/bots/serverless)

**原文标题**: [Telegram Serverless](https://core.telegram.org/bots/serverless)

# 概述总结

Telegram Serverless 让您直接在 Telegram 基础设施上运行机器人和 Mini App 的后端代码，无需管理服务器、容器或扩展。您编写 JavaScript 模块，通过单个命令部署，Telegram 在快速、隔离的 V8 沙箱中运行它们。

- 🚀 **无需基础设施** — 无需租用、修补或监控机器，代码按需自动扩展
- 📦 **开箱即用** — Bot API、SQLite 数据库和 HTTP 请求立即可用，无需安装或配置凭证
- ⚡ **快速隔离执行** — 每个调用在轻量级 V8 隔离环境中运行，靠近 Telegram 系统
- 💻 **真实开发工作流** — 项目在本地文件夹中受版本控制，可原子化部署和审查迁移
- 🗂️ **项目结构** — 包含 handlers/（更新处理程序）、lib/（共享代码）和 schema.js（数据库表）
- 🛠️ **CLI 工具** — 提供 init、push、migrate、run、status 等命令管理项目
- 📱 **BotFather 支持** — 可通过手机管理处理程序、库和数据库
- 🗄️ **内置数据库** — 每个机器人拥有独立 SQLite 数据库，使用类似 Drizzle ORM 的 DSL
- 🤖 **AI 辅助开发** — 项目包含 AGENTS.md 和 SDK 参考，便于 AI 编码助手使用
- 🔒 **安全同步** — 乐观并发检查防止多人部署时覆盖他人工作

---

### [Telegram 机器人 API](https://core.telegram.org/bots/api)

**原文标题**: [Telegram Bot API](https://core.telegram.org/bots/api)

Telegram Bot API 是一个基于 HTTP 的接口，用于开发者构建 Telegram 机器人。它提供了发送消息、管理群组、处理支付、创建游戏等多种功能，并支持通过 webhook 或长轮询接收更新。近期版本引入了富消息、临时消息、社区、访客模式、直播照片等多项新特性。

- 🤖 **机器人认证与请求**：每个机器人拥有唯一令牌，所有 API 请求需通过 HTTPS 发送至 `https://api.telegram.org/bot<token>/METHOD_NAME`，支持 GET/POST 及多种参数传递方式。
- 📩 **接收更新**：支持 `getUpdates`（长轮询）和 `setWebhook`（webhook）两种方式，更新以 JSON 格式的 `Update` 对象传递，包含消息、回调查询等多种类型。
- 💬 **发送消息**：提供 `sendMessage`、`sendPhoto`、`sendVideo` 等方法，支持文本、媒体、贴纸、位置、投票、发票等丰富内容类型，并可设置回复键盘、内联键盘等交互界面。
- 🎨 **富消息 (Rich Messages)**：自 API 10.1 起支持高度结构化的富文本消息，包含标题、列表、表格、媒体、公式、折叠块等，可通过 Markdown 或 HTML 格式发送。
- 👻 **临时消息 (Ephemeral Messages)**：API 10.2 引入，允许机器人在群组中向特定用户发送仅该用户可见的临时消息，并支持回复和编辑。
- 🏘️ **社区 (Communities)**：API 10.2 支持将多个超级群组、频道和机器人链接在一起，形成围绕共同主题的社区。
- 🚪 **访客模式 (Guest Mode)**：API 10.0 允许机器人接收非成员聊天中的消息并回复，通过 `guest_query_id` 和 `answerGuestQuery` 实现。
- 📸 **直播照片 (Live Photos)**：API 10.0 新增，可发送包含短视频的静态照片，并支持作为付费媒体发送。
- 📊 **投票增强**：API 10.0 起投票选项可包含媒体（图片、视频等），支持仅限成员投票、国家代码限制，并可将选项数降至最少 1 个。
- 🎮 **游戏与支付**：支持创建和发送 HTML5 游戏，记录高分榜；支持通过 Telegram Stars 或第三方支付提供商处理付款、订阅和退款。
- 🛡️ **安全与本地服务器**：可运行本地 Bot API 服务器以突破文件大小限制，并支持自定义 webhook 端口和 IP 地址。Mini App 安全已增强，默认禁止跨域调用。

---

### [GitHub - yagop/node-telegram-bot-api: 适用于 NodeJS 的 Telegram Bot API](https://github.com/yagop/node-telegram-bot-api)

**原文标题**: [GitHub - yagop/node-telegram-bot-api: Telegram Bot API for NodeJS · GitHub](https://github.com/yagop/node-telegram-bot-api)

这是一个用于 Node.js 的现代 Telegram Bot API 库，支持多种运行环境，提供简洁的中间件、键盘构建器和文件上传功能。

- ✨ 支持 Bun、Node.js、Deno、Cloudflare Workers 和 Vercel Functions 等多种运行环境
- 📦 通过 `npm install node-telegram-bot-api@next` 安装，v2 版本完全重写，不兼容 v1
- 🚀 提供 `Bot` 类，支持命令、正则匹配和消息事件的中间件处理
- 📡 提供 `Api` 类，1:1 映射 Telegram Bot API 方法，支持直接调用
- 🧩 支持 koa 风格中间件，包含 `use`、`on`、`command`、`hears` 和 `catch` 方法
- ⌨️ 提供 `InlineKeyboardBuilder`、`ReplyKeyboardBuilder` 和 `EntityBuilder` 构建键盘和富文本
- 📤 支持文件上传，包括磁盘路径、原始字节和流式上传，并自动处理重试
- 🪝 支持 Webhooks，兼容 Express、Next.js 和边缘运行时
- ⚠️ 错误处理提供结构化字段（如 `TelegramApiError`、`NetworkError`），支持自动重试 429 错误
- 🛡️ 内置弹性机制，包括自动重试、限流（全局和每聊天）和长轮询恢复
- 🌊 提供 `longPoll` 异步生成器，支持灵活的低级更新流处理
- 🐛 支持 `DEBUG` 环境变量进行调试，跟踪请求生命周期和轮询
- 🛠️ 开发工具包括类型生成、代码检查和构建脚本

---

### [Git worktrees 入门指南 - Human Who Codes](https://humanwhocodes.com/blog/2026/07/introduction-git-worktrees/)

**原文标题**: [A gentle introduction to Git worktrees - Human Who Codes](https://humanwhocodes.com/blog/2026/07/introduction-git-worktrees/)

這篇文章介紹了 Git worktrees 的基本概念與實用方法，幫助開發者在不影響主專案的情況下，同時處理多個分支任務，特別適合與 AI 編碼工具協作。

- 📂 **什麼是 Worktree**：Worktree 是將分支獨立存放在不同目錄中，與主專案共用提交歷史，但檔案與依賴各自獨立。
- 🚀 **建立 Worktree**：使用 `git worktree add` 指令建立新分支目錄，例如 `git worktree add ../project.worktrees/feature-name -b feature/name main`。
- ⚠️ **注意事項**：依賴需重新安裝（如 `npm install`），且每個分支只能被一個 worktree 檢出，主專案無法同時切換。
- 🗂️ **目錄命名習慣**：可將 worktree 放在主專案的同級目錄（如 `my-project-feature-name`）或統一放在 `my-project.worktrees` 子目錄中。
- 🔄 **合併變更**：可透過推送分支到遠端發起 Pull Request，或在本機手動合併：先 rebase 再 merge。
- 🧹 **清理 Worktree**：使用 `git worktree remove` 刪除目錄，再用 `git branch -d` 刪除分支。
- 🔍 **管理與快捷鍵**：用 `git worktree list` 查看所有 worktree，並可設定別名 `git config --global alias.wt worktree` 簡化操作。
- 🤖 **與 AI 協作**：Worktree 讓多個 AI 編碼代理能平行開發，避免互相干擾，且無需將程式碼上傳雲端。

---

### [Playwright 在 GitHub Actions 上的配置：真正快速运行的设置](https://endform.dev/blog/playwright-github-actions)

**原文标题**: [Playwright on GitHub Actions: The setup that actually runs fast](https://endform.dev/blog/playwright-github-actions)

本篇文章介紹了如何在 GitHub Actions 上優化 Playwright 測試流程，重點在於透過快取瀏覽器二進位檔和調整並行度來顯著提升執行速度，並提供完整的工作流程設定與常見錯誤排除建議。

- 🚀 **快取瀏覽器二進位檔**：將 Playwright 瀏覽器安裝在 `~/.cache/ms-playwright`，並以 `package-lock.json` 的雜湊值作為快取鍵，可將每次下載的 42 秒縮短至數秒，僅在更新 Playwright 版本時重新下載。
- ⚡ **調整並行度**：在 `playwright.config.ts` 中設定 `fullyParallel: true` 和 `workers: process.env.CI ? "50%" : undefined`，可根據執行器核心數自動擴展工作進程，將 40 個測試的執行時間從 2 分 25 秒降至約一半。
- 🎯 **按事件限制瀏覽器**：在 Pull Request 中僅執行 Chromium 測試（`--project=chromium`），而對主分支的推送則執行完整的三瀏覽器測試，可將測試執行次數減少三分之二。
- 📊 **上傳報告與內聯註釋**：使用 `actions/upload-artifact` 上傳 HTML 報告，並在設定中加入 `["github"]` 報告器，讓失敗測試直接顯示在 GitHub Actions 的摘要中，無需下載壓縮檔。
- 🛠️ **完整工作流程範例**：提供包含快取、條件式瀏覽器安裝、並行測試和報告上傳的完整 YAML 和設定檔，可直接套用於專案中。
- ⏳ **何時使用分片**：當單一執行器無法在 PR 審查時間內完成（約 5 分鐘）時，才考慮分片。對於 200 個測試以下的套件，通常透過調整工作進程和使用更大的執行器即可滿足需求。
- ❌ **常見錯誤**：避免安裝瀏覽器時遺漏 `--with-deps`、快取 `node_modules` 而非 npm 快取、設定過多工作進程導致資源競爭，以及忘記加入 `github` 報告器。

---

### [每个 GitHub 维护者本周应启用的 6 个安全设置 - GitHub 博客](https://github.blog/security/6-security-settings-every-github-maintainer-should-enable-this-week/)

**原文标题**: [6 security settings every GitHub maintainer should enable this week - The GitHub Blog](https://github.blog/security/6-security-settings-every-github-maintainer-should-enable-this-week/)

本文介绍了六项免费安全设置，帮助 GitHub 维护者在 30 分钟内显著提升项目安全性，降低被攻击风险。

- 🔒 **添加 SECURITY.md 文件**：为漏洞报告者提供明确的联系方式与报告范围，避免漏洞公开曝光，耗时约 10 分钟。
- 🛡️ **启用私有漏洞报告（PVR）**：允许研究人员私下提交安全报告，维护者可秘密处理并自主决定披露时间，仅需勾选一个复选框。
- 🔑 **开启密钥扫描与推送保护**：阻止密钥和令牌在提交时泄露，防范 AI 辅助提交导致的密钥泄露风险（2025 年新增 2865 万个泄露密钥）。
- 📦 **启用 Dependabot 与依赖审查**：自动检测依赖包中的已知漏洞，并在拉取请求中显示变更内容，将依赖审查时间缩短至 2 分钟。
- 🔍 **开启代码扫描（CodeQL）**：自动检测 SQL 注入、命令注入等常见漏洞，默认配置无需手动调整，每次拉取请求自动运行。
- 🛑 **启用默认分支保护**：要求拉取请求至少获得一个批准才能合并，防止凭据泄露或误操作直接推送到生产环境，使其他设置真正生效。

---

### [GitHub - run-llama/liteparse: 一个快速、实用且开源的文件解析器 · GitHub](https://github.com/run-llama/liteparse#liteparse)

**原文标题**: [GitHub - run-llama/liteparse: A fast, helpful, and open-source document parser · GitHub](https://github.com/run-llama/liteparse#liteparse)

LiteParse 是一个专注于快速轻量解析的独立开源 PDF 解析工具，提供高质量的空间文本解析及边界框，无需专有 LLM 功能或云依赖，所有操作均在本地运行。

- 📄 **快速文本解析**：使用 PDFium 进行空间文本解析，快速高效。
- 🔍 **灵活的 OCR 系统**：内置 Tesseract（零设置），支持通过 HTTP 服务器集成 EasyOCR、PaddleOCR 等，并提供标准 API 规范。
- 🧠 **复杂度检测**：在完整解析前，可廉价检查文档是否需要 OCR 或更重处理，便于路由、拒绝或估算成本。
- 🖼️ **截图生成**：可为 LLM 代理生成高质量页面截图。
- 📝 **多种输出格式**：支持 Markdown、JSON 和文本，Markdown 输出包含标题、表格、列表、图片和链接，适合 LLM 和 RAG 流水线。
- 🎯 **边界框**：提供精确的文本定位信息。
- 🌐 **多语言和多平台**：支持 Rust、Node.js/TypeScript、Python 和浏览器（WASM），兼容 Linux、macOS 和 Windows。
- ⚙️ **CLI 工具**：提供统一的命令行接口，支持文件解析、批量解析、截图生成和复杂度检查。
- 📂 **多格式输入**：自动将 Office 文档（Word、PowerPoint、Excel）和图像转换为 PDF 进行解析。
- 🛠️ **易于安装**：通过 npm、pip、cargo 或 WASM 安装，并可作为代理技能使用。

---

### [获取失败](https://github.com/run-llama/liteparse/blob/main/packages/node/README.md)

**原文标题**: [Failed to retrieve](https://github.com/run-llama/liteparse/blob/main/packages/node/README.md)

无法总结：获取内容失败，状态码 429。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

Tiger Cloud 提供可扩展的 PostgreSQL 时序数据库服务，具备企业级功能与高可靠性。

- 🚀 可处理每天 3 万亿指标、3 PB 数据及 1 千万亿数据点的超大规模时序工作负载
- 💰 新用户可获$1000 信用额度（30 天有效），无需信用卡
- 📈 通过最多 10 节点副本集实现读写分离，结合 SSD/S3 分层存储实现无限扩展
- ⚡ 计算与存储分离架构，独立扩展以避免闲置容量浪费
- 🔒 多可用区集群支持自动故障转移、时间点恢复和跨区域备份
- 🛡️ 符合 SOC 2、HIPAA 和 GDPR 标准，提供加密、SSO、RBAC 和审计日志
- 📊 深度可观测性：查询钻取与仪表盘，支持 CloudWatch、Datadog、Prometheus 集成
- ⏱️ 分钟级数据库部署，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 与主流云提供商及 PostgreSQL 生态系统无缝集成
- 🏢 企业级服务：合同 SLA、区域数据隔离、24/7 全球专家支持

---

### [发布 v7.0.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v7.0.0)

overview summary  
这是 setup-node 动作 v7.0.0 版本的发布说明，包含多项增强、错误修复、文档更新和依赖升级。

- 🚀 新增缓存主键和匹配键作为输出  
- 📦 迁移至 ESM 并升级依赖  
- 🐛 移除虚拟的 NODE_AUTH_TOKEN 导出  
- 🔧 仅在提供 mirrorToken 时在 getManifest 中使用它  
- 📝 添加使用受信任发布者（OIDC）发布到 npm 的文档  
- 📖 更新仅恢复缓存文档  
- 🛡️ 更新缓存建议以降低缓存投毒风险  
- ⬆️ 升级 @actions/cache 至 5.1.0，记录缓存写入被拒绝的情况  
- 👥 新增贡献者：chiranjib-swain、deiga、jasongin

---

### [获取失败](https://github.com/actions/setup-node/blob/main/docs/advanced-usage.md#publishing-to-npm-with-trusted-publisher-oidc)

**原文标题**: [Failed to retrieve](https://github.com/actions/setup-node/blob/main/docs/advanced-usage.md#publishing-to-npm-with-trusted-publisher-oidc)

无法总结：获取内容失败，状态码 429。

---

### [Mediabunny — 一个完整的浏览器端 JavaScript 媒体工具包](https://mediabunny.dev/)

**原文标题**: [Mediabunny â A complete JavaScript media toolkit for the browser](https://mediabunny.dev/)

概述：本文档是 Vue.js 官方文档的导航页面，列出了核心功能模块和资源链接，包括指南、API、LLMs、示例、博客、赞助商、许可证等信息。

- 🔍 搜索功能：提供站内搜索入口，方便用户快速查找内容
- 🧭 主导航：包含“指南”、“API”、“LLMs”、“示例”等关键模块，引导用户学习 Vue.js
- 📝 博客与赞助：提供技术博客和赞助商信息，支持社区发展
- 📜 许可证信息：明确 Vue.js 的开源许可证，确保合规使用
- 🎨 外观与代码注册：包含“代码注册表”和“外观”设置，个性化开发体验

---

### [支持的格式与编解码器 | Mediabunny](https://mediabunny.dev/guide/supported-formats-and-codecs)

**原文标题**: [Supported formats & codecs | Mediabunny](https://mediabunny.dev/guide/supported-formats-and-codecs)

Mediabunny 支援多種常見媒體容器格式與編解碼器，並提供編碼/解碼能力查詢及自定義編解碼器功能。

- 📦 **容器格式支援**：支援 ISOBMFF (.mp4)、QuickTime (.mov)、CMAF (.m4s)、Matroska (.mkv)、WebM (.webm)、Ogg (.ogg)、MP3 (.wav)、ADTS (.aac)、FLAC (.flac)、MPEG-TS (.ts)、HLS (.m3u8) 等多種格式，雙向讀寫。

- 🎥 **影片編解碼器**：支援 AVC/H.264、HEVC/H.265、VP8、VP9、AV1、ProRes（需擴充套件），部分依賴瀏覽器 WebCodecs API。

- 🎵 **音訊編解碼器**：支援 AAC、Opus、MP3、Vorbis、FLAC、AC-3、E-AC-3、多種 PCM 格式（如 pcm-s16、pcm-f32）、μ-law、A-law，內建所有 PCM 解/編碼器。

- 📝 **字幕編解碼器**：支援 WebVTT（僅寫入，不支援讀取）。

- 🔗 **容器相容性表**：明確列出各編解碼器與容器格式的相容組合（如 .mp4 支援 AVC、HEVC、AAC 等；.webm 僅支援 VP8/VP9/Opus 等子集）。

- 🔍 **編碼能力查詢**：提供 `canEncode`、`canEncodeVideo`、`canEncodeAudio` 函式，可依解析度、位元率等配置檢查瀏覽器支援性；另有 `getEncodableCodecs` 系列函式取得支援清單，以及 `getFirstEncodableVideoCodec` 找出最佳編碼器。

- 🔍 **解碼能力查詢**：提供 `canDecode`、`canDecodeVideo`、`canDecodeAudio` 函式，可依配置檢查解碼支援性；另有 `getDecodableCodecs` 系列函式取得支援清單。

- 🛠️ **自定義編解碼器**：可註冊自訂編碼器（繼承 `CustomVideoEncoder`/`CustomAudioEncoder`）或解碼器（繼承 `CustomVideoDecoder`/`CustomAudioDecoder`），需實作 `supports`、`init`、`encode`/`decode`、`flush`、`close` 方法，並遵循解碼順序與時間戳排序規則。

- ⚠️ **注意事項**：部分編解碼器（如 ProRes、AAC 編碼、MP3 編碼、FLAC 編碼、AC-3/E-AC-3）需透過擴充套件支援；WebM 僅支援 Matroska 子集；自定義解碼器需處理 B-frames 並按時間戳排序輸出。

---

### [发布 v1.45.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.45.0)

**原文标题**: [Release v1.45.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.45.0)

### 概述总结
Mediabunny 发布 v1.45.0 版本，新增服务器端扩展包，支持在 Node、Bun、Deno 环境中使用完整音视频功能。

- 🚀 **新增服务器端扩展包**：`@mediabunny/server` 允许在服务器端使用所有音视频编解码器和视频转换功能。
- 🎬 **新增视频样本资源**：`VideoSampleResource` 和 `AudioSampleResource` 可自定义数据支持，避免数据复制。
- 🔄 **新增视频帧转换功能**：`VideoSample.transform()` 支持调整大小、旋转、裁剪等操作。
- 🛠 **自定义转换器注册**：通过 `registerVideoSampleTransformer` 注册自定义转换器以支持 `VideoSample.transform()`。
- 🎨 **透明视频编解码优化**：新增基于 CPU 的 Alpha 分割/合并回退方案。
- 📦 **内存与性能改进**：`ReadableStreamSource` 默认缓存大小从 16 MiB 增至 32 MiB；修复转换 API 中轨道进程同步问题。
- 🐛 **关键 Bug 修复**：修复 CMAF 段识别、Chromium 音频时间戳错误、FLAC 解复用器负时间戳寻址等多项问题。

---

### [tinbase — 适合放在罐子里的 Supabase 兼容后端](https://www.tinbase.dev/)

**原文标题**: [tinbase — the Supabase-compatible backend that fits in a tin](https://www.tinbase.dev/)

tinbase 是一个与 Supabase 兼容的后端，无需 Docker，体积小巧，支持在浏览器中运行。

- 🚀 **极简部署**：单个 58 MB 可执行文件，无需 Node、npm 或 Docker，启动即用。
- 💾 **超低资源占用**：安装足迹仅 36 MB，负载下内存 66 MB，远低于 Supabase 本地栈（2.3 GB）。
- 🔄 **原生 SDK 兼容**：直接使用官方 supabase-js SDK，无需修改代码。
- 🗄️ **真实 Postgres**：支持 Postgres 17，包含 RLS、触发器、外键、jsonb 等完整功能。
- 🎯 **多引擎选择**：提供 WASM（PGlite）、原生 Postgres 17 和纯 JS 内存引擎三种后端。
- 🔐 **完整认证**：支持邮箱/密码、匿名、OTP、OAuth（Google/GitHub）等认证流程。
- 📡 **实时功能**：支持 postgres_changes、broadcast 和 presence，并带 RLS 过滤。
- 🧩 **内置工具**：包含 Studio 仪表盘（表格、SQL、认证、存储、RLS 策略）和 Edge Functions。
- 🌐 **浏览器运行**：整个后端可在浏览器标签页内运行，无需服务器。
- 🔗 **灵活接入**：支持连接外部 Postgres 数据库，通过 --database-url 参数指定。

---

### [PGlite](https://pglite.dev/)

**原文标题**: [PGlite](https://pglite.dev/)

概述：这是一个轻量级的 Postgres WASM 构建版本，压缩后体积小于 3MB。

- 🚀 采用 WebAssembly 技术，实现 Postgres 数据库的完整功能
- 📦 压缩后体积仅 3MB，极致轻量化设计
- ⚡️ 适合浏览器或边缘计算环境部署
- 🔧 保持 Postgres 核心特性，兼容标准 SQL 操作

---

### [GitHub - oguimbal/pg-mem: 用于单元测试的内存中 PostgreSQL 数据库实例](https://github.com/oguimbal/pg-mem)

**原文标题**: [GitHub - oguimbal/pg-mem: An in memory postgres DB instance for your unit tests · GitHub](https://github.com/oguimbal/pg-mem)

pg-mem 是一個實驗性的記憶體中 PostgreSQL 模擬器，可在 Node 或瀏覽器中運行，主要用於單元測試。

- 🗄️ 支援 Node.js 和 Deno，安裝簡單（npm i pg-mem）
- 🔄 支援狀態回滾，可建立還原點，適合單元測試
- 🛠️ 可自訂函數和類型，支援函數重載和可變參數
- 📦 提供多種流行資料庫庫的配接器（如 pg、typeorm、knex 等）
- 🔍 可攔截查詢、手動檢查/插入表格資料、訂閱事件
- ⚠️ 注意：SQL 語法解析器為自製，部分功能未實作；時間區和數字類型處理有限制
- 🧪 使用 Bun 進行單元測試，歡迎提交 Pull Request
- 📜 支援擴展模擬（如 uuid-ossp），可匯入生產環境 schema
- 🏷️ 主題標籤：nodejs、typescript、postgresql、unit-testing、hacktoberfest 等

---

### [推出 @neon/sdk，我们为 Neon API 打造的全新 TypeScript 客户端 - Neon](https://neon.com/blog/neon-sdk)

**原文标题**: [Introducing @neon/sdk, our new TypeScript client for the Neon API - Neon](https://neon.com/blog/neon-sdk)

Neon 推出 @neon/sdk，這是一款全新的 TypeScript 客戶端，用於與 Neon API 互動：基於 fetch、零依賴、從 OpenAPI 規範生成，並在上層提供符合人體工學的介面。它取代了舊的 @neondatabase/api-client。

- 🚀 **核心功能**：@neon/sdk 提供兩層架構：高層的 `createNeonClient`（包含資源命名空間、輪詢、重試等便利功能）和低層的 `raw`（每個端點對應一個可 tree-shake 的獨立函數）。
- ⏳ **自動輪詢**：高層客戶端會自動處理非同步操作（如資源就緒輪詢），讓開發者無需手動等待基礎設施佈建完成。
- 🖼️ **快照預覽**：`restore` 函數支援在還原快照前預覽分支，並可選擇提交或放棄，避免產生孤立分支。
- 🔄 **專案轉移**：`transfer` 函數簡化了跨組織的專案遷移，適合免費方案與付費方案分開管理的場景。
- 🖥️ **一鍵建立分支與運算**：`createWithCompute` 將建立分支與佈建運算資源合併為一個呼叫，直接返回連線字串。
- 🎯 **使用場景**：適合 CI/CD、開發腳本、平台整合等程式化操作，而 MCP 伺服器和 CLI 則更適合本地開發與編輯器內使用。
- 🛠️ **向後相容**：舊的 `@neondatabase/api-client` 不會立即棄用，但建議新專案直接使用 @neon/sdk。

---

### [Neon — 应用与智能体的 Postgres 后端](https://neon.com/)

**原文标题**: [Neon — Postgres backends for apps and agents](https://neon.com/)

Neon 是专为应用和 AI 代理设计的 Postgres 后端平台，提供无服务器数据库、认证、函数、对象存储和 AI 网关等一体化云原语。

- 🗄️ **无服务器 Postgres 数据库**：自动扩展计算、内存和存储，按需付费，避免过度配置和性能问题。
- 🔐 **内置 Better Auth 认证**：将用户认证与会话直接存储在 Postgres 中，无需额外平台费用，支持 HIPAA 和 SOC2 合规。
- 🧩 **即时分支与复制**：支持类似 Git 的数据库分支，可创建可编辑副本、匿名化敏感数据，并自动删除过期分支。
- 🚀 **高级自动扩缩容**：通过分离计算与存储，每天防止超过 5.4 万次性能降级，节省成本并避免事故。
- ☁️ **AI 网关与函数**：统一 API 调用所有模型，支持长时间运行无超时函数，并靠近数据库执行。
- 💾 **S3 兼容对象存储**：随项目分支的 blob 存储，便于开发与测试。
- 🔒 **企业级生产特性**：包括私有网络、日志导出、99.95% 可用性 SLA、即时时间点恢复和单点登录，无需高额承诺。
- 🏢 **由 Databricks 支持**：由 Postgres 提交者创立，2025 年成为 Databricks 公司，每天启动 1200 万个 Postgres 数据库。
- ⚡ **快速上手**：通过 `npx neon init` 一键集成，连接 MCP 客户端，立即开始构建。

---

### [GitHub - ai/nanoid：一个微型（118字节）、安全、URL友好、唯一的JavaScript字符串ID生成器](https://github.com/ai/nanoid)

**原文标题**: [GitHub - ai/nanoid: A tiny (118 bytes), secure, URL-friendly, unique string ID generator for JavaScript · GitHub](https://github.com/ai/nanoid)

Nano ID 是一个轻量、安全、URL 友好的唯一字符串 ID 生成器，适用于 JavaScript，具有高性能和低碰撞概率的特点。

- 🚀 **极致小巧**：仅 118 字节（压缩后），无依赖，Size Limit 控制体积
- ⚡ **超快速度**：比原生`crypto.randomUUID()`快 50%
- 🔒 **安全可靠**：使用硬件随机生成器，适用于集群环境
- 📏 **短 ID 设计**：比 UUID 使用更大字母表（A-Za-z0-9_-），ID 从 36 字符减至 21 字符
- 🌍 **跨平台支持**：已移植到 20 多种编程语言
- 🎨 **灵活定制**：支持自定义字母表、ID 长度和随机字节生成器
- 🛡️ **高安全性**：避免`Math.random()`，采用均匀分布算法，文档完善
- 📦 **多安装方式**：支持 npm、JSR、CDN 等多种安装途径
- 🧩 **框架兼容**：提供 React、React Native、PouchDB 等使用指南
- 🔧 **实用工具**：包含 ID 碰撞概率计算器、字典库、脏话过滤工具

---

### [GitHub - bcoe/c8: 使用 Node.js 内置覆盖率功能输出覆盖率报告 · GitHub](https://github.com/bcoe/c8)

**原文标题**: [GitHub - bcoe/c8: output coverage reports using Node.js' built in coverage · GitHub](https://github.com/bcoe/c8)

c8 是一个基于 Node.js 原生 V8 引擎的代码覆盖率工具，兼容 Istanbul 报告格式，可轻松集成到项目中。

- 📦 **快速上手**：通过 `npm i c8 -g` 全局安装，使用 `c8 node foo.js` 即可生成覆盖率报告。
- ⚙️ **灵活配置**：支持命令行参数、`package.json` 或 `.c8rc` 等配置文件，提供多种选项如报告格式、输出目录、文件包含/排除等。
- 🔍 **全源覆盖**：使用 `--all` 选项可检测项目中未加载文件的覆盖率，避免遗漏未测试的源文件。
- 🗺️ **SourceMap 支持**：自动处理内联或独立 `.map` 文件，支持 TypeScript、JSX 等编译代码的覆盖率映射。
- ✅ **覆盖率检查**：通过 `c8 check-coverage` 或 `--check-coverage` 设置阈值（如 `--lines 95`），确保代码质量，支持按文件检查。
- 🧪 **实验性功能**：支持 Monocart 报告库（需额外安装），提供更直接的 V8 覆盖率输出格式。
- 🚫 **忽略特定代码**：使用 `/* c8 ignore next */` 等注释跳过不需要覆盖的行、块或函数。
- 🖥️ **环境要求**：需 Node.js >= 12，利用原生 V8 覆盖率功能。

---

### [测试运行器 | Node.js v26.5.0 文档](https://nodejs.org/api/test.html#collecting-code-coverage)

**原文标题**: [Test runner | Node.js v26.5.0 Documentation](https://nodejs.org/api/test.html#collecting-code-coverage)

Node.js v26.5.0 的测试运行器 (`node:test` 模块) 是一个功能全面的测试框架，支持编写同步、异步和基于回调的测试，并提供了丰富的特性来组织、筛选和模拟测试行为。

- 📝 **核心测试编写**：支持同步（抛出异常则失败）、异步（Promise 拒绝则失败）和基于回调的测试函数，测试失败时进程退出码为 1。
- 🧩 **子测试与分层**：通过 `t.test()` 方法创建子测试，支持 `describe`/`it` 或 `suite`/`test` 别名进行分层组织，子测试失败会导致父测试失败。
- ⏭️ **测试控制**：支持跳过 (`skip`)、标记为待办 (`todo`)、预期失败 (`expectFailure`) 以及仅运行特定测试 (`only`)，并可通过 `--test-only` 命令行选项启用。
- 🏷️ **标签筛选**：通过 `tags` 数组为测试添加标签，使用 `--experimental-test-tag-filter` 命令行选项或 `testTagFilters` 配置项按标签筛选测试。
- 🔄 **重跑失败测试**：使用 `--test-rerun-failures` 选项持久化测试运行状态，以便在后续运行中仅重跑失败的测试。
- 🎲 **随机化执行顺序**：通过 `--test-randomize` 或 `--test-random-seed` 选项随机化测试文件和测试的执行顺序，帮助发现顺序依赖的测试。
- 📊 **代码覆盖率**：使用 `--experimental-test-coverage` 选项收集代码覆盖率，支持通过注释忽略特定行，并可通过 `lcov` 等报告器输出详细报告。
- 🎭 **模拟功能**：提供 `mock` 对象用于模拟函数、方法、属性、模块以及定时器（`setTimeout`、`setInterval` 等）和 `Date` 对象，支持通过 `TestContext` 自动清理模拟。
- 📸 **快照测试**：通过 `t.assert.snapshot()` 和 `t.assert.fileSnapshot()` 进行快照测试，使用 `--test-update-snapshots` 标志生成或更新快照文件。
- 📢 **测试报告器**：内置 `spec`、`tap`、`dot`、`junit` 和 `lcov` 报告器，支持自定义报告器，并可通过 `--test-reporter` 和 `--test-reporter-destination` 指定多个报告器和输出目标。
- 🔧 **生命周期钩子**：支持 `before`、`after`、`beforeEach`、`afterEach` 钩子，可在套件或测试级别执行设置和清理操作。
- 👀 **监听模式**：通过 `--watch` 标志启用监听模式，当测试文件或其依赖发生变化时自动重新运行受影响的测试。
- 🌍 **全局设置与拆卸**：通过 `--test-global-setup` 标志指定模块，该模块可导出 `globalSetup` 和 `globalTeardown` 函数，用于在所有测试前后执行全局设置和清理。
- ⚙️ **高级配置**：`run()` 函数提供丰富的选项，如并发数 (`concurrency`)、工作目录 (`cwd`)、文件列表 (`files`)、隔离模式 (`isolation`)、超时 (`timeout`)、分片 (`shard`) 和环境变量 (`env`) 等。
- 📡 **可观测性集成**：通过 `diagnostics_channel` 发布测试执行事件，支持与 OpenTelemetry 等可观测性工具集成，实现上下文传播和自定义仪表化。
- 🧪 **测试上下文**：`TestContext` 和 `SuiteContext` 对象提供丰富的属性和方法，如 `name`、`fullName`、`filePath`、`passed`、`error`、`attempt`、`tags`、`workerId`、`plan()`、`runOnly()`、`signal`、`skip()`、`todo()`、`waitFor()` 等。

---

### [GitHub - sindresorhus/np: 更好的 `npm publish` 工具 · GitHub](https://github.com/sindresorhus/np)

**原文标题**: [GitHub - sindresorhus/np: A better `npm publish` · GitHub](https://github.com/sindresorhus/np)

`np` 是一个增强版的 `npm publish` 工具，提供交互式 UI 和自动化流程，确保发布过程安全、可靠且高效。

- 🚀 **核心功能**：提供交互式 UI，自动检查分支、工作目录、依赖、测试，并处理版本号、Git 标签、npm 发布、回滚等操作。
- 🔒 **安全保障**：防止意外发布预发布版本，支持双因素认证（2FA），并在发布失败时自动回滚项目。
- 🧪 **测试与清理**：运行测试，重新安装依赖，确保项目与最新依赖树兼容。
- 📦 **版本管理**：自动升级 package.json 和 package-lock.json 中的版本号，并创建 Git 标签。
- 🌐 **多平台支持**：支持 npm、pnpm、Bun、Yarn，以及 GitHub Packages 和自定义注册表。
- ⚙️ **配置灵活**：可通过 CLI 选项、package.json 或配置文件（如 .np-config.json）进行全局或局部配置。
- 🖥️ **交互模式**：直接运行 `np` 无参数可启动交互式 UI，引导用户完成发布流程。
- 📝 **发布草稿**：自动打开预填好的 GitHub Releases 草稿，支持生成发布说明。
- 🧹 **文件检查**：警告可能发布的无关文件，帮助避免包体积过大或包含敏感文件。
- 🧪 **干运行模式**：支持 `--dry-run` 选项，在不实际推送或发布的情况下预览执行任务。
- 🔧 **高级功能**：支持签名 Git 标签、私有包、作用域包、自定义注册表、CI 发布、旧版本维护等。
- ❓ **常见问题**：提供 macOS 密钥链问题、Yarn 权限错误、发布挂起等问题的解决方案。

---

### [GitHub - kartikk221/hyper-express: 高性能 Node.js 网络服务器，拥有简单易用的 API，底层由 uWebsockets.js 驱动。](https://github.com/kartikk221/hyper-express)

**原文标题**: [GitHub - kartikk221/hyper-express: High performance Node.js webserver with a simple-to-use API powered by uWebsockets.js under the hood. · GitHub](https://github.com/kartikk221/hyper-express)

HyperExpress 是一个高性能的 Node.js 网页服务器，基于 uWebSockets.js 构建，旨在简化 HTTP 和 WebSocket 开发。

- 🚀 基于 C++ 编写的 uWebSockets.js，提供更高吞吐量，无需升级硬件即可提升应用性能
- 📦 支持 npm 安装，兼容 Node.js 22、24、26 版本，保持 CommonJS 和 snake_case API
- 🌐 提供简化的 HTTP 和 WebSocket API，支持服务器发送事件、多部分文件上传、模块化路由和中间件
- 🔒 支持多主机/域名 SSL 连接，并与 Express.js 部分兼容
- 📚 提供详细文档，涵盖服务器、路由、请求、响应、WebSocket、中间件、SSE 流、文件上传、会话引擎、静态文件服务等
- 🛠 使用原生 uWebSockets.js 插件，支持主流平台（macOS、Windows、glibc Linux），但不支持 Alpine Linux
- ⚠️ 与 Express 不完全兼容，部分中间件可能需自行适配；默认禁用 uWebSockets.js 版本头
- 🧪 本地测试需克隆仓库、运行 `npm ci` 安装依赖，并执行 `npm test` 等命令
- 📜 采用 MIT 许可证，拥有 2k 星标、109 个分支和 126 个版本发布

---

### [GitHub - helmetjs/helmet: 使用各种 HTTP 头保护 Express 应用的安全 · GitHub](https://github.com/helmetjs/helmet)

**原文标题**: [GitHub - helmetjs/helmet: Help secure Express apps with various HTTP headers · GitHub](https://github.com/helmetjs/helmet)

Helmet 是一个用于保护 Node/Express 应用安全的中间件，通过设置多种 HTTP 响应头来防御常见攻击，易于集成且维护成本低。

- 🛡️ **快速集成**：通过 `app.use(helmet())` 即可设置 13 个 HTTP 响应头，如 Content-Security-Policy 和 Strict-Transport-Security。
- ⚙️ **灵活配置**：可单独禁用或自定义每个头部，例如通过 `contentSecurityPolicy: false` 禁用 CSP，或传递对象配置特定头部。
- 🔒 **内容安全策略 (CSP)**：默认启用，防御跨站脚本攻击，支持自定义指令，如 `script-src`，并可设置 `reportOnly` 模式或禁用 `upgrade-insecure-requests`。
- 🌐 **跨域控制**：包括 Cross-Origin-Embedder-Policy、Opener-Policy 和 Resource-Policy，默认不启用或设为 `same-origin`，可调整策略值。
- 📡 **传输安全**：Strict-Transport-Security 默认强制 HTTPS，支持配置 `maxAge`、`includeSubDomains` 和 `preload`，建议开发环境禁用。
- 🚫 **防御机制**：X-Content-Type-Options 防止 MIME 嗅探，X-Frame-Options 防御点击劫持，X-XSS-Protection 禁用旧版 XSS 过滤器。
- 🔍 **隐私与性能**：Referrer-Policy 控制引用信息，X-DNS-Prefetch-Control 管理 DNS 预取，Origin-Agent-Cluster 隔离进程。
- 🗑️ **移除冗余**：默认移除 X-Powered-By 头部，节省带宽并提高安全性，但 Express 内置方法更推荐。
- 📜 **其他头部**：包括 X-Download-Options、X-Permitted-Cross-Domain-Policies 等，针对特定场景提供保护，均支持禁用或自定义。

---

### [发布 v6.0.0 · auth0/node-auth0 · GitHub](https://github.com/auth0/node-auth0/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · auth0/node-auth0 · GitHub](https://github.com/auth0/node-auth0/releases/tag/v6.0.0)

概述摘要  
- 💥 **重大变更**：`ConnectionAttributeIdentifier` 被拆分为三个独立类型（`EmailAttributeIdentifier`、`PhoneAttributeIdentifier`、`UsernameAttributeIdentifier`），需更新相关代码。  
- 🔄 **枚举值调整**：`PhoneProviderProtectionBackoffStrategyEnum` 中的 `None` 变体更名为 `Default`，需替换代码中的 `"none"` 字符串。  
- ❌ **子客户端移除**：`client.users.federatedConnectionsTokensets` 及其 `list()`/`delete()` 方法已被删除。  
- 🗑️ **字段移除**：所有连接选项类型中删除了 `federated_connections_access_tokens` 字段。  
- ✨ **新特性**：`PhoneAttributeIdentifier` 新增支持 `phone_otp` 作为 `default_method`，修复密码设置缺陷。  
- 🛡️ **安全增强**：自定义令牌交换新增可疑 IP 限流阶段支持。  
- 👥 **管理扩展**：新增组织角色成员和第三方客户端访问管理功能。  
- 🌐 **连接更新**：OIDC 连接类型覆盖范围改进。  
- 🚀 **兼容性**：支持 Node.js 26，认证 API 客户端无破坏性变更。

---

### [安全 AI 代理与用户认证 | Auth0](https://auth0.com/)

**原文标题**: [Secure AI Agent & User Authentication | Auth0](https://auth0.com/)

Auth0 是一个易于实施、可适应的身份验证和授权平台，每月阻止超过 30 亿次攻击，提供 99.99% 的正常运行时间，并支持每月超过 100 亿次身份验证。它专注于保护 AI 代理、内部 AI 工具、B2B 和 B2C 应用，提供 Token Vault、SSO、MFA 等关键功能，并可在 5 分钟内集成到任何应用中。

- 🔒 每月阻止超过 30 亿次攻击，保障安全。
- ⏱️ 提供 99.99% 的正常运行时间，性能始终在线。
- 📈 每月处理超过 100 亿次身份验证，可扩展性强。
- 🤖 专为 AI 代理设计，提供用户认证、工具控制和知识限制功能。
- 🛠️ 支持 Token Vault、SSO、M2M 认证和细粒度授权（FGA）。
- 🚀 可在 5 分钟内集成到任何应用，提供 30 多个 SDK 和快速入门指南。
- 🏢 适用于 B2B 和 B2C 场景，支持多租户和企业连接。
- 🔑 提供无密码登录、自适应 MFA 和机器人检测，提升用户体验。
- 📚 提供丰富的资源，包括白皮书、网络研讨会和电子书，涵盖 AI 安全、身份管理等主题。

---

### [ESLint v10.7.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/07/eslint-v10.7.0-released/)

**原文标题**: [ESLint v10.7.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/07/eslint-v10.7.0-released/)

ESLint v10.7.0 发布，新增多项功能和错误修复。

- 🚀 新增 `max-nested-callbacks` 规则的 `checkConstructorCallCallbacks` 选项，可统计构造函数回调的嵌套深度
- 🛠️ `preserve-caught-error` 规则新增 `errorClassNames` 选项，允许指定自定义错误类名以保留原始错误
- 💡 `no-compare-neg-zero` 规则新增建议功能，可替换 `-0` 为 `0` 或使用 `Object.is()`
- ✨ 其他新功能：支持 `radix` 规则中的 `Number.parseInt` 成员访问、报告无效的 `radix` 值等
- 🐛 修复多个错误：包括 `eqeqeq` 规则对静态模板字符串的处理、`no-invalid-regexp` 对阴影 RegExp 的误报等
- 📚 文档更新：包括 ESLint 迁移指南、配置文件路径修正等
- 🔧 内部改进：更新依赖、添加 Node.js 26 支持、优化 TypeScript 注释等

---

### [更新 AWS SDK for JavaScript v3 中的 TypeScript 版本支持 | AWS 开发者工具博客](https://aws.amazon.com/blogs/developer/updating-typescript-version-support-in-aws-sdk-for-javascript-v3/)

**原文标题**: [Updating TypeScript version support in AWS SDK for JavaScript v3 | AWS Developer Tools Blog](https://aws.amazon.com/blogs/developer/updating-typescript-version-support-in-aws-sdk-for-javascript-v3/)

AWS SDK for JavaScript v3 将更新对 TypeScript 版本的支持，自 2027 年 1 月 4 日起，仅支持过去 2.5 年内发布的 TypeScript 版本。

- 📅 新政策自 2027 年 1 月 4 日生效，要求 TypeScript 版本在发布后 2.5 年内
- 🔄 与 DefinitelyTyped 和 typescript-eslint 等生态系统的支持窗口保持一致
- 📊 各版本结束支持时间表：<=5.5 版至 2027 年 1 月 4 日，5.6 版至 2027 年 3 月 31 日等
- ✅ 支持版本将明确记录在 GitHub README 中，并定期更新
- 📦 此变更可减少包大小和 Lambda 部署包体积，简化发布流程
- 🛠️ 推荐升级 TypeScript 到受支持版本，或固定 SDK 版本以保持兼容
- ❓ 非运行时变更，仅影响类型兼容性和构建过程
- 📉 不再进行类型降级处理，因为降级类型占 SDK 发布包大小的 18%

---

### [Dependabot 版本更新引入默认包冷却期 - GitHub 更新日志](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/)

**原文标题**: [Dependabot version updates introduce default package cooldown - GitHub Changelog](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/)

概述总结
Dependabot 版本更新引入了默认的软件包冷却期，以增强供应链安全。

- 🔒 Dependabot 现在默认等待新版本发布至少三天后，再打开版本更新拉取请求，无需额外配置。
- 🛡️ 此冷却期有助于防止供应链攻击，避免在维护者和社区发现前合并受损或存在缺陷的版本。
- ⚡ 该默认设置仅适用于版本更新，安全更新仍会立即打开，确保关键修复不延迟。
- ⚙️ 用户可通过 `.github/dependabot.yml` 文件中的 `cooldown` 选项自定义冷却窗口或完全退出。
- 🌐 此默认设置适用于 github.com 上所有受支持的生态系统，并将在 GitHub Enterprise Server 3.23 中生效。

---

### [获取失败](https://github.com/tc39/agendas/blob/main/2026/07.md)

**原文标题**: [Failed to retrieve](https://github.com/tc39/agendas/blob/main/2026/07.md)

无法总结：获取内容失败，状态码 429。

---

### [GitHub - tc39/proposal-await-dictionary: 一个向 ECMAScript 添加 Promise.allKeyed 的提案](https://github.com/tc39/proposal-await-dictionary)

**原文标题**: [GitHub - tc39/proposal-await-dictionary: A proposal to add Promise.allKeyed to ECMAScript · GitHub](https://github.com/tc39/proposal-await-dictionary)

这是一个关于 `Promise.allKeyed` 的 ECMAScript 提案，旨在解决并行请求中的命名和顺序问题。

- 📜 **提案状态**: 该提案目前处于 Stage 2.7，由多位 TC39 成员共同推进。
- 🚀 **核心动机**: 解决 `await` 逐个属性造成的串行“瀑布”问题，以及 `Promise.all` 基于顺序而非名称容易导致的混淆。
- 🎯 **解决方案**: 引入 `Promise.allKeyed` 方法，允许传入一个包含 Promise 的字典对象，并返回一个同键名的结果字典，从而保持命名清晰。
- 🛡️ **避免未处理拒绝**: 新方案能自动处理所有 Promise 的拒绝，避免因某个 `await` 失败导致其他 Promise 未处理而引发进程退出。
- 🔗 **扩展 API**: 同时提供 `Promise.allSettledKeyed` 方法，以支持更细粒度的结果处理（区分成功与失败）。
- 💡 **设计考量**: 提案明确只处理自有可枚举属性（包括 Symbol 键），并遵循与 `Iterator.zipKeyed` 一致的设计模式。
- ⚖️ **替代方案对比**: 讨论了 `Promise.ownProperties`、`Promise.fromEntries`、重载 `Promise.all` 以及专用语法（如 `async const`）等替代方案，并解释了为何选择当前方案。

---

### [GitHub - tc39/proposal-decimal: JavaScript 内置精确十进制数提案 · GitHub](https://github.com/tc39/proposal-decimal/)

**原文标题**: [GitHub - tc39/proposal-decimal: Built-in exact decimal numbers for JavaScript · GitHub](https://github.com/tc39/proposal-decimal/)

TC39 的 JavaScript Decimal 提案旨在為 JavaScript 添加精確的十進制算術支援，解決二進制浮點數的捨入誤差問題，並滿足金融計算等場景需求。

- 📌 提案目標：在 JavaScript 中提供精確的十進制數字運算，消除 `0.1 + 0.2` 不等於 `0.3` 這類二進制浮點數的捨入錯誤。
- 💰 主要應用場景：金融計算、貨幣轉換、與支援十進制資料的系統（如資料庫）互動，以及前後端架構中對精確計算的需求。
- 🧩 資料模型：採用 IEEE 754-2019 Decimal128 標準，使用 128 位元儲存，支援最多 34 位有效數字，並包含 NaN、正負無窮大和負零等特殊值。
- 🛠️ 核心功能：提供精確的加、減、乘、除、取餘運算，支援五種 IEEE 754 捨入模式，並提供 `toString`、`toFixed` 等方法進行格式化。
- 🔗 與其他提案的關係：與 TC39 的 Amount 提案（處理精度和單位）互補，並與 BigInt、Keep trailing zeroes 等提案協同工作。
- 🚫 當前限制：不支援運算子重載（如 `+`、`*`），需使用方法進行運算；不引入新的字面量語法（如 `m` 後綴）。
- 📊 生態現狀：開發者已廣泛使用 `decimal.js`、`bignumber.js` 等第三方庫，本提案旨在標準化現有實踐。
- 💡 未來展望：未來版本可能考慮運算子重載、十進制字面量語法，以及進階數學函數（如三角函數、對數）的支援。

---

### [GitHub - dcrousso/proposal-Map-take · GitHub](https://github.com/dcrousso/proposal-Map-take)

**原文标题**: [GitHub - dcrousso/proposal-Map-take · GitHub](https://github.com/dcrousso/proposal-Map-take)

该提案建议为 `Map` 和 `WeakMap` 添加 `take(key)` 方法，用于在单个操作中移除并返回指定键的值。

- 📋 **核心功能**：`Map.prototype.take(key)` 和 `WeakMap.prototype.take(key)` 方法，移除键对应的条目并返回其值，若键不存在则返回 `undefined`。
- 🎯 **主要动机**：解决当前需要两次查找（`get` + `delete`）才能实现“读取并移除”的问题，提高性能并减少代码错误。
- 🔍 **语义说明**：行为等价于先执行 `get(key)` 再执行 `delete(key)`，返回 `get` 的结果；若键不存在或值为 `undefined` 均返回 `undefined`。
- 🌍 **广泛需求**：GitHub 上存在大量手动实现类似功能的代码（如 `getAndDelete`、`popEntry` 等），搜索结果显示数万至数十万相关用法。
- 📚 **语言先例**：多数语言的标准库（如 Rust、Python、Java、C#）都提供“移除并返回值”的操作，JavaScript 的 `Array.prototype.pop()` 也遵循此模式。
- 🏷️ **命名选择**：`take` 源自 Rust 的 `HashSet::take`，自然表达“从映射中取出值”；`getAndDelete` 是备选名称，强调读取后删除的语义。
- 🛠️ **Polyfill 实现**：通过 `Object.defineProperty` 在 `Map` 和 `WeakMap` 原型上添加 `take` 方法，确保与现有 `get` 和 `delete` 方法兼容。
- ❓ **待讨论问题**：是否支持可选默认值（如 `take(key, defaultValue)`），以及是否为 `Set` 和 `WeakSet` 添加类似方法。

---

### [Cloudflare 掉线](https://www.cloudflare.com/drop/)

**原文标题**: [Cloudflare Drop](https://www.cloudflare.com/drop/)

Cloudflare Drop 可让您无需账户即可将静态网站快速部署到 Cloudflare 全球网络。

- 📁 直接拖放包含 HTML、CSS、JS 的文件夹或 .zip 文件即可上传。
- 🌐 上传后自动分发到 Cloudflare 全球网络，并提供 `workers.dev` 实时 URL。
- ⏱️ 部署后需在 60 分钟内认领，否则链接失效。
- 🤖 AI 代理可通过浏览器自动化使用，但本地 CLI 项目推荐使用 Wrangler 工具。
- 🛠️ 未认证时可用 `npx wrangler@latest deploy` 命令，需指定输出目录、名称和兼容日期。
- ✅ 部署后若返回 404，请稍等重试，因为路由和资源可能需要短暂时间生效。
- 🔑 认领 URL 可获取临时预览账户所有权，需妥善保管且 60 分钟有效。
- ⚠️ 已认证环境下不要使用 `--temporary` 参数，直接使用 `wrangler deploy`。

---

### [Netlify](https://app.netlify.com/drop)

**原文标题**: [Netlify](https://app.netlify.com/drop)

概述摘要
Netlify 控制面板需要启用 JavaScript 才能正常使用，当前页面因 JavaScript 未启用而显示错误提示。

- 🚫 Netlify 控制面板因 JavaScript 被禁用而无法加载
- ⚙️ 用户需在浏览器设置中启用 JavaScript 功能
- 🔄 启用后重新打开页面即可正常使用

---

### [GitHub - commandprompt/plx: PostgreSQL 扩展：使用 Ruby、PHP、JavaScript 或 Python 方言编写存储函数，并转译为 plpgsql。](https://github.com/commandprompt/plx)

**原文标题**: [GitHub - commandprompt/plx: PostgreSQL extension: write stored functions in Ruby, PHP, JavaScript, or Python dialects that transpile to plpgsql. · GitHub](https://github.com/commandprompt/plx)

该页面显示了一个名为 **plx** 的 PostgreSQL 扩展项目，允许开发者用熟悉的语言（如 Ruby、PHP、JavaScript 等）编写数据库函数，这些函数会被自动转译为 PL/pgSQL 执行。

- 📦 **核心功能**：plx 是一个 PostgreSQL 扩展，支持用 Ruby、PHP、JavaScript、TypeScript、Python、Go、COBOL、Oracle PL/SQL 或 Transact-SQL 语法编写存储函数和触发器，并在 `CREATE FUNCTION` 时自动转译为 PL/pgSQL 存储。
- ⚡ **性能优势**：函数最终由 PostgreSQL 原生的 PL/pgSQL 解释器执行，性能接近原生 PL/pgSQL（差距约 11%），且无需加载额外语言运行时到后端。
- 🔧 **工作原理**：每个方言提供 `PlxSurface` 描述语法规则，共享转译器将代码结构化为 PL/pgSQL，转换发生在函数创建时而非每次调用，生成的 PL/pgSQL 存储在 `pg_proc.prosrc` 中，可审查和转储。
- 🎯 **适用人群**：适合希望将业务逻辑推入数据库但不想学习 PL/pgSQL 的开发者，以及希望用熟悉语法编写触发器/函数但保持 PL/pgSQL 性能和信任模型的团队。
- 📊 **字符串优化**：针对 PL/pgSQL 在循环中拼接字符串的 O(n²) 性能问题，plx 提供 `plx_strbuild` 字符串构建器，在 PostgreSQL 18 上可加速约 170 倍。
- 🛠️ **安装与兼容**：支持 PostgreSQL 13 至 18，通过 `make && make install` 构建安装，然后运行 `CREATE EXTENSION plx;` 即可启用。
- 📚 **文档丰富**：提供各方言详细文档、架构说明、性能基准、限制说明、调试指南和可运行食谱示例。
- 🏗️ **项目结构**：包含 C 源码（转译器、方言表面、PL 处理器）、文档、示例、测试套件和基准测试工具。
- 📜 **许可与状态**：采用 MIT 许可证，当前版本 1.3.0（2026 年 7 月发布），拥有 5 个星标和 0 个复刻。

---

