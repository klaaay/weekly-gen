# [Web Tools Weekly Issue #697 (JS Libs, Testing, Mobile)](https://webtoolsweekly.com/archives/issue-697/)

### [无冷启动、无账单惊吓的托管 Node.js 服务](https://www.cloudways.com/en/velocity.php?id=948626&data1=webtoolsweekly26&data2=sponsorship)

Cloudways 推出 Velocity 公共预览，提供托管 Node.js 托管平台，面向生产级全栈应用、后端 API、内容站、内部工具和自动化/AI 工作流。其核心是以常开持久服务器、扁平月费和全托管运维，减少冷启动、按量账单波动以及安全补丁和扩容负担。

- 🚀 **公共预览**：Cloudways 发布 Velocity 的 Public Preview，提供托管 Node.js 托管，强调数分钟部署生产应用、无需自建服务器运维。
- 🧩 **部署流程**：连接 GitHub、GitLab 或 Bitbucket 仓库后，Velocity 自动检测框架并设置构建和启动命令；确认预设并点击 Deploy，内置 CI/CD 让应用快速上线。
- ⚙️ **框架与运行时**：开箱支持 12 个框架，包括 Next.js、Remix、React、Astro、Express、Fastify、Angular 和 n8n；可选 Node.js LTS 22.x 与 24.x，并可按应用选择。
- ⚡ **持久在线**：采用常开持久服务器而非 serverless，避免闲置关停和冷启动；扁平月费不随流量按量计费，与 Vercel、Railway、Heroku 的差异主要在托管程度和成本可预测性。
- 🛠️ **托管栈**：预配置 NGINX 与 PM2 及缓存，自动处理 OS 补丁、SSL、域名映射和备份；控制台可设置环境变量并查看构建与错误日志，PostgreSQL 可直接在仪表盘开通。
- 🛡️ **安全与 CDN**：所有套餐标配 WAF、DDoS 防护、恶意软件防护和 Cloudflare Enterprise CDN，不额外收费。
- 📦 **套餐资源**：月费从 Starter $20（2GB RAM、2 vCPU、5 个应用）到 Business $400（64GB RAM、16 vCPU、150 个应用），中间含 Professional $30、Growth $50、Scale $100、Plus $150、Advanced $300；所有套餐 10Gbps 网络，支持单服务器多应用和纵向扩容。
- 📊 **计费细则**：可随时升级或降级且无锁定；异地备份存储 $0.033/GB，超出套餐的 CDN 流量 $0.02/GB，额外磁盘 $1/10GB。
- 🧪 **试用与支持**：Starter 和 Professional 提供 3 天免费试用；所有套餐含 24/7 专家支持，覆盖基础设施和平台问题。
- 🔑 **黑五优惠**：新账户在 12 月 4 日前使用代码 `BFCM802` 创建，Velocity 账单前 2 个月减免 80%，每月最高减 $200；例如 $50 的 Growth 套餐降至 $10/月。

### [来自 Excalibur.js 的问候 | Excalibur.js](https://excaliburjs.com/)

Excalibur 游戏引擎强调免费开源、TypeScript 原生构建、完整且持续更新的 API 文档，以及基于现代 JavaScript 的跨平台能力；其公开项目采用 BSD 2 Clause 许可，游戏可运行于多数浏览器，并可通过 Cordova、Universal Windows Apps 或 Electron 打包为跨平台应用。

- 🔑 **开源许可**：Excalibur 保持免费开源，公开项目采用 BSD 2 Clause，并明确承诺不会更改。
- 🧩 **TypeScript 构建**：引擎从底层为 TypeScript 设计，利用类型系统让代码更清晰、可读和可维护，适合熟悉 C#、Java 等强类型语言的开发者。
- 📚 **API 文档**：提供完整 API 参考文档，并随每个版本自动更新，同时覆盖主代码分支。
- 🌐 **跨平台发布**：游戏编译为现代 JavaScript，可在多数浏览器及移动浏览器运行；也可借助 Apache Cordova、Universal Windows Apps 或 Electron 等原生应用包装器发布跨平台游戏。

### [Elo — 一种表达式语言](https://elo-lang.org/)

Elo 是一门面向 No-Code 工具的简单、可移植且安全的数据表达式语言，目标是让非技术用户也能安全地操作数据。它采用纯数据语义，并可将同一表达式编译为 JavaScript、Ruby、Python 和 SQL，同时提供原生日期时间、数据模式、管道与守卫等能力；关系代数支持仍在即将推出阶段，项目以 MIT 协议开源。

- 🎯 **项目定位**：Elo 面向 No-Code 工具和非技术用户，强调简单、可移植与安全，用于数据表达和操作，而非通用编程。
- 🧩 **语言设计**：Elo 是纯数据语言，一切皆为值，没有引用语义和 `new`，只有一种可正常工作的相等运算符，以降低非技术用户的理解与误用成本。
- 🌐 **跨语言编译**：同一表达式可编译为语义等价的 JavaScript、Ruby、Python 和 SQL，覆盖前端、后端与数据库；例如 `2 ^ 10 > 1000 and TODAY >= SOY` 会生成各目标语言的惯用代码。
- 🗓️ **时间原生**：日期、时间和时长是一等类型，支持 `D2024-06-15`、`P30D` 等直观字面量，可直接写 `TODAY > signup + P30D`，无需解析、转换或额外导入库。
- 🛡️ **数据模式**：支持用 schema 校验并强制转换不可信输入，例如 `Int(c | c > 0)` 约束容量必须为正，使后续代码运行在可信数据上。
- ⚙️ **函数式管线**：提供管道操作符、lambda 和较完整的标准库，支持 `filter`、`map`、`reduce` 等数据操作，并在 JavaScript、Ruby、Python、SQL 四个目标中保持相同语义。
- ✅ **运行时守卫**：可用 `guard` 给假设加标签并在运行时校验，如 `positive: _.age > 0`、`adult: _.age >= 18`，便于快速失败并明确代码所保证的条件。
- 🔮 **关系代数计划**：即将支持受 Tutorial D 启发、由 Bmg 驱动的关系代数，用于数据管线中的查询、连接和聚合，并保持可移植语义。
- 📚 **开源与上手**：项目采用 MIT 开源协议，提供 playground 和面向编程新手的入门内容；由 Bernard Lambeau 设计监督，Claude Code 参与共同设计与实现。

### [一次构建 devtool，随处挂载。](https://devfra.me/)

devframe 发布了一套面向 devtool 开发的框架无关基础层：只要用 `defineDevframe()` 定义一次工具，`initDevframe()` 就会把它转换为符合 Web 标准的 Request → Response handler；这个 handler 可以原生挂载到 Hono、Nitro、Next.js、SvelteKit、Vite、Rsbuild、Deno、Bun 等宿主中；同一份定义也能被适配器封装成 CLI、独立开发服务器、静态报告、MCP 服务器或 Vite DevTools 面板。它把工具边界收敛到 Web 标准请求与响应；任何支持该标准或 connect 风格中间件的框架都能接入，并复用同一套 RPC、状态与生态。

- 🚀 **核心发布**：devframe 提供与框架无关的 devtool 基础：用 `defineDevframe({ id, name, rpc, view })` 描述工具，用 `initDevframe(devframe, { base })` 得到 handler，实现构建一次、随处挂载。
- 🧩 **单一标准 Handler**：handler 的边界是 Web 标准 `Request`/`Response`；它可直接挂进 Hono、Nitro 全捕获事件路由、Next.js App Router route handler，Vite 则复用同一实例提供的 connect 风格 `nodeMiddleware`，只有面向宿主框架的适配层会变化。
- 📦 **适配器形态**：同一份定义可按发布方式选择入口：`devframe/adapters/cac` 生成独立 CLI，`devframe/adapters/dev` 启动开发服务器，`devframe/adapters/mcp` 以 `stdio` 等传输暴露给编码智能体，`devframe/adapters/build` 输出到 `outDir`（如 `dist-static`）生成自包含 SPA 快照用于 CI。
- 🔗 **类型安全 RPC 与共享状态**：双向调用基于 birpc，并可用任意 Standard Schema 校验器校验；同时提供可观察的 patch 同步状态，在连接断开重连后仍然保留。
- 🧠 **可视化与智能体双接口**：RPC 函数默认私有，需通过 `agent: { description }` 显式选择暴露给智能体；MCP 适配器把这些函数、资源及选定的共享状态转换为智能体可消费的接口，界面表现不同但数据源唯一。
- 🏢 **Hub 组合层**：`@devframes/hub` 是无头组合层：多个 devframe 可注册 docks、commands、terminals 和共享状态，并通过一个入口统一呈现；`initHub({ base, devframes, ui })` 产出的 handler 与独立 devframe 使用相同的 handler/中间件 API。
- 🎨 **内置 Devframe 跨 UI 框架**：内置 devframe 覆盖 Vue、Svelte、Solid 与 React；devframe 自身负责协议层，具体 UI 框架交由工具作者选择。

### [小巧的 JavaScript 运行时 | txiki.js](https://txikijs.org/)

文章正文只给出一个 JavaScript 运行时的定位信息：它被描述为“小型且强大”，并提供“Get Started”入口；正文没有披露具体产品名、版本、功能细节、实现机制或发布状态。

- 🎯 **运行时定位**：该 JavaScript 运行时强调“小而强大”，核心卖点是体积小与能力强的组合；原文未说明具体产品名、版本号或技术实现。
- 💻 **上手入口**：页面提供 Get Started 入口，用于引导用户开始使用；原文未给出安装步骤、API、代码示例或平台支持范围。

### [Octane — 编译实现的 React 编程模型](https://octanejs.dev/)

Octane v0.27.1 是 Inferno 的后继项目，采用编译器优先架构，把 React 的 hooks、Suspense 和 actions 带入无虚拟 DOM 的 TSRX 组件模型，由编译器自动追踪依赖并直接更新 DOM；它保留 React 式组件写法并支持与 React 双向互操作，目标是在不要求重写应用结构的前提下提升运行性能。

- 🚀 **版本定位**：Octane v0.27.1 以编译器优先方式实现 React 编程模型，延续 Inferno 对性能的关注，核心卖点是无虚拟 DOM、无 hooks 规则和无须手写依赖数组。
- 🧩 **无虚拟 DOM**：模板编译为克隆 DOM 节点并进行直接更新，keyed 列表只移动必要节点；现有 `.tsx` 组件可保留，并按组件逐个迁移到 `.tsrx`。
- 🧩 **自动依赖追踪**：编译器自动追踪 effects、memos 和 callbacks 使用的值，因此 hooks 可安全放在条件分支或提前 return 之后，不再需要依赖数组，也不受传统 rules of hooks 限制。
- ⚡ **并行异步**：独立的 `use()` 调用会同时启动而非逐个挂起，嵌套请求可更早开始，流式 SSR 会在每个边界就绪时立即发送。
- 🧩 **保留 React 心智模型**：仍提供 hooks、`memo`、context、portals、transitions、actions、受控表单和 Suspense；事件基于 DOM，refs 是普通 props，组件仍是接收 props 的普通函数。
- 🧪 **测试与生态**：测试执行超过 11,500 次，覆盖 compiler、runtime、SSR 和 bindings，核心套件有 3,900+ 个不同用例，React 派生覆盖逐例追踪；另提供 118 个官方 binding，覆盖状态、数据、路由、UI、表单、图表和 3D 等。
- 🛠️ **渐进迁移**：Octane 组件仍是带 props、hooks 和 context 的普通函数，状态与数据流保持 React 式；现有 TSX 可继续使用，迁移只需逐个组件转换为 TSRX，不需要重新设计，便于人工或编码代理审查。
- 🔄 **双向互操作**：`ReactCompat` 让 Octane 应用使用真实 React 组件，`OctaneCompat` 让 React 应用逐个岛屿接入编译后的 Octane 组件；两者都支持 SSR 和 hydration，各自保留事件，父级更新在 commit 后跨边界，context、Suspense 和限制见指南。
- 📱 **Lynx 原生**：通过 Lynx 可用 Octane 构建在 iOS 和 Android 上渲染原生视图的应用，hooks、context、Suspense 和 transitions 行为一致，只需把帧关键代码标记到主线程；Lynx 支持目前处于 early access。
- 🎨 **Three.js 预览**：`@octanejs/three` 是 React Three Fiber 的技术预览移植，页面中的实时 Three.js 场景会在滚动接近时才加载，并可拖动旋转。
- 🧠 **不采用 signals 作为基础**：Octane 允许在合适场景使用 signals，但不把它们作为框架基础，因为那会改变每个组件读取状态的方式；组件仍是从上到下执行的普通函数，由编译器负责簿记。
- 📊 **基准对比**：性能表以 Octane 为 1×，几何平均 React 19 + Compiler 为 2.1×、Preact 10 为 2.8×、Solid 2.0 RC 为 1.3×、Svelte 5 为 1.3×、Ripple 0.4 为 0.65×、Vue Vapor 3.6 RC 为 0.91×、Inferno 9 为 1.2×；每个主要 React 对比使用官方 React Compiler，信号型框架在信号负载领先，Octane 保持竞争。

### [GitHub - 8borane8/webtools-slick-server: Slick 是一个基于 Web 标准构建、面向 Deno 的小型、简单且超快的 Web 框架。 · GitHub](https://github.com/8borane8/webtools-slick-server)

Slick Server 是面向 Deno 的小型、轻量、超快 Web 框架，基于 Web Standards，通过模板、页面和 islands 将 Preact SSR、按需 hydrate、零配置资产构建、热重载与可选 SPA 导航组合在一起；README 的安装示例指向 `@webtools/slick-server@^0.7.0`，并强调端到端类型和共享 vendor bundle 以减少重复下载。

- 🚀 **框架定位**：Slick 使用模板描述共享壳、页面描述路由、islands 承载交互，默认输出静态 HTML，只在需要交互处向浏览器发送 JavaScript，目标是兼顾 SEO、首屏速度和轻量开发体验。
- 📦 **安装与依赖**：通过 `deno add jsr:@webtools/slick-server` 添加；`deno.json` 必须为 Preact 配置 JSX，并声明 `preact@^10.29.2` 和 `preact-root-fragment@^0.3.1`，存在 `islands/` 时后者必需；当前只支持 Preact 10，尚不支持 Preact 11；SPA 模式还需声明 `@webtools/slick-client@^0.3.0`。
- 🧩 **SSR 与 Islands**：模板和页面在服务端渲染为 HTML；只有 `islands/` 中的 Preact 组件会向浏览器发送 JavaScript 并在客户端 hydrate，其余页面保持静态 HTML；islands props 必须可 JSON 序列化，`children` 不会传输，且 island 至少渲染一个根元素，多个根元素可作为一个岛 hydrate，不能只渲染 `null` 或文本，根层也不要混文本与元素。
- ⚙️ **目录与配置**：`templates/`、`pages/`、`static/` 为必需目录，`islands/` 可选；页面和模板递归发现，重复 `url` 或 `name` 会拒绝启动；模板 `body` 必须且只能包含一个写在标记中的 `id="app"` 元素；配置包括 `env`、`port`（默认 5000）、`lang`（默认 `en`）、`r404`（默认 `/`）、`client`、`hotReload`、`trustProxy` 和 `sharedLibs`，`trustProxy` 仅应在单个可信反向代理后启用。
- 🔄 **热重载**：`hotReload: true` 时监听工作区（排除 `static/`、`node_modules/` 和隐藏目录），文件变化会失效其导入链并重载相关页面、模板和 islands；语法错误时记录错误并继续提供上一版本；修改 `config.env`、`port`、`sharedLibs` 或首次创建 `islands/` 仍须重启。
- 🔑 **编译期环境变量**：`config.env` 通过 esbuild `define` 在编译期注入为裸全局标识符，不使用 `process.env` 或 `Deno.env`；页面和模板仅在 SSR 可用，islands 在 SSR 与客户端可用，`static` 脚本和 vendor bundle 仅在客户端可用，修改后需重启。
- 🧠 **类型化请求数据**：基于 `@webtools/expressapi` 的类型化中间件，模板 `onrequest` 写入的 `req.data` 会在其 `head`、`body`、`favicon` 和使用该模板的页面中获得类型；页面第二类型参数可补充 `data`、`params` 和 `query`，也可用 `template()`、`page()`、`middleware()` 自动推断。
- 🎨 **动态渲染**：`title`、`favicon`、`head` 和 `body` 接受静态值或接收请求的函数，函数可以异步；请求对象提供 `path`、`params`、`query`、`cookies`、`headers`、`data` 等字段，便于按 URL 参数或用户数据生成页面。
- ⚡ **静态资产**：`static/` 挂载到站点根路径；CSS 会压缩并以 `text/css` 提供，JS/TS/JSX/TSX 会转译、压缩为 ES modules，其他文件原样提供；每个静态响应带 `ETag` 和 `Cache-Control: no-cache`，编译结果首次请求后内存缓存，热重载时每次请求重新编译且不缓存。
- 🔗 **共享库与 vendor bundle**：每个 island 独立打包，`sharedLibs` 把共用库打成 `/~vendors/<lib>` 单份 vendor bundle，并通过生成的 import map 让 island 保持外部引用；默认共享 Preact 生态，存在 `client` 时还共享 `@webtools/slick-client`；第三方库需同时加入项目 `deno.json` 的 `imports` 和 `sharedLibs`。
- 🌐 **SPA 客户端模式**：`client: true` 时首次请求仍完整 SSR，后续导航通过 `fetch` 请求 JSON，仅返回变化的页面和必要模板，并用 `X-Slick-Template` 头识别 SPA 导航；客户端按 `slick-type` 交换页面/模板的 `styles` 和 `scripts`，文档需保留 `#root`、`title` 和 shortcut icon。
- 🧭 **路由与保留路径**：每个页面暴露 `GET`/`HEAD`，`POST` 交给 `onpost` 或 SPA 导航；支持 `:params`，静态段优先于参数；`/~islands/*` 和 `/~vendors/*` 为保留路径；无匹配页面、保留路径或静态文件时重定向到 `r404`，未定义 `onpost` 的 POST 在 client 模式返回 405，否则 404。
- 🛠️ **API 与校验**：`Slick` 提供 `load()`、`start()` 和可直接用于测试的 `fetch(request)`；`load()` 会校验必需目录、默认导出、重复路由、`r404` 是否匹配及 island 导出，`start()` 调用 `load()` 后监听端口；导出 `Config`、`Page`、`Template`、`Render`、`SlickRequest`、`TemplateData`、`UrlParams` 等类型。

### [GitHub - vercel/workflow: Workflow SDK：使用 TypeScript 构建持久、可靠且可观测的应用和 AI 智能体 · GitHub](https://github.com/vercel/workflow)

Vercel 的 Workflow SDK 仓库 README 介绍了一套面向 TypeScript/JavaScript 的持久化工作流开发套件，让函数具备进度持久化、失败重试和内置可观测性，并支持等待期间不占计算资源；它把本地开发、Vercel 托管部署、自托管路径以及 AI Agent 场景纳入同一套 SDK 中。

- 🚀 **SDK 定位**：Workflow SDK 用于在 TypeScript 和 JavaScript 中构建持久、可靠、可观测的应用与 AI Agent，核心能力包括持久化工作流进度、重试失败步骤和内置可观测性。
- 🧩 **核心机制**：工作流等待时可挂起而不消耗计算资源，SDK 负责保存进度并在失败步骤上重试，以支持长时间运行和可靠执行。
- ⚡ **快速接入**：在现有项目中执行 `npm install workflow`；Next.js 在 `next.config.ts` 中使用 `withWorkflow` 配置集成；服务端代码可从 `workflow/api` 导入 `start`，传入工作流函数和参数来启动流程。
- 🔍 **本地观测**：运行应用后在另一终端执行 `npx workflow web` 打开本地可观测性 UI；`workflow` 包内置完整文档，编码代理可从 `node_modules/workflow/docs` 读取与版本匹配的指南。
- 🌐 **部署与自托管**：本地开发使用捆绑后端且无需配置；部署到 Vercel 可获得托管存储、排队、扩缩容和可观测性；自托管可使用 Postgres 后端或实现自定义 `World`；`Worlds` 页面列出维护者筛选的第三方 `Worlds`，可通过 `Worlds Manifest` 提交。
- 🛠️ **生命周期钩子**：`registerLifecycleHooks` 从 `workflow/api` 导入，在 workflow executor 的主机启动时注册处理器，用于应用级完成和失败上报；在工作流或步骤内调用会抛错；支持的框架/部署组合与流清理要求需查阅 lifecycle hooks 指南。
- 💬 **社区与安全**：社区交流在 GitHub Discussions；发现安全漏洞应负责任披露而非公开 issue；可邮件 `responsible.disclosure@vercel.com` 参与 OSS Bug Bounty 计划。

### [Kiesel JavaScript 引擎](https://kiesel.dev/)

总结失败：模型未返回符合格式的摘要。

### [检查文件是否由 Claude 创建 | Claude by Anthropic](https://claude.com/check-files)

Anthropic 提供 Claude 文件检查工具，用户可在浏览器中上传图片、视频或音频文件，检查其中是否带有 Claude 附加的 Content Credential；该工具基于 C2PA 元数据标准，只读取凭证而不上传文件，并明确不检测文本，文本检测另由处于私有预览的 Detection API 提供。

- 🚀 **文件检查工具**：用户可拖放或点击上传文件，检查其是否带有来自 Claude 的 Content Credential；若找到，只表示 Claude 可能制作或处理过该文件，不代表底层内容作者，也不包含用户身份信息。
- 📦 **支持格式与限制**：支持 JPG、PNG、GIF、WEBP、TIFF、HEIC、AVIF、SVG、DNG、JXL、MP4、MOV、AVI、WAV、MP3、M4A、FLAC，单文件最大 100 MB。
- 🧩 **C2PA 机制**：Claude 为受支持文件类型（如 `.png`、`.jpg`、`.svg`）在元数据中附加一个小型、经密码学签名的 Content Credential，说明文件可能由 Claude 制作或处理；这采用 C2PA 开放行业标准，与相机厂商和照片编辑软件记录图像来源所用标准相同，任何支持 C2PA 的工具都可读取。
- 🔍 **检测边界**：工具只读取文件附带的凭证，不读取文件本身；不检查文本，因为 Claude 对文本采用写作内容中的水印标记，文件检查器不覆盖文本检测。
- 💬 **文本检测**：文本需通过 `Detection API` 检查，目前面向符合条件组织进行私有预览，并按欧盟法律要求提供。
- 🛡️ **本地隐私**：工具在浏览器中运行，文件留在用户设备上，不会被存储或用于其他目的；使用工具即表示同意 Anthropic 的 Usage Policy 和 Privacy Policy。

### [GitHub - callstackincubator/agent-react-devtools：让 AI 智能体访问 React DevTools ⚛️🤖 · GitHub](https://github.com/callstackincubator/agent-react-devtools)

Callstack 孵化器项目 `agent-react-devtools` 让 AI 代理通过命令行获得 React DevTools 能力，可遍历组件树、读取 props/state/hooks，并对渲染性能做 profiling；项目提供 Web 与 React Native 接入、持久后台 daemon 和面向 LLM 的紧凑输出，目前处于早期实验阶段。

- 🚀 **项目定位**：为 AI agent 提供 React DevTools 访问能力，可在命令行检查组件树、props、state 和 hooks，并分析渲染性能；灵感来自 Vercel 的 `agent-browser` 与 Callstack 的 `agent-device`，项目仍属早期实验，欢迎 PR。
- ⚙️ **守护进程**：通过 `npm install -g agent-react-devtools` 安装或 `npx agent-react-devtools start` 直接运行；daemon 默认监听 8097 端口并跨 CLI 调用持久运行，`status` 展示连接应用数、组件数、运行时长和最后事件。
- 🔍 **组件检查**：`get tree` 支持 `--depth N`、`--all`、`--max-lines N`；默认过滤 `<div>` 等 host components 以压缩输出，带 key 或自定义元素名的 host component 始终显示；组件以 `@c1` 等标签标识，也可用数字 ID。
- 🧩 **查询命令**：`get component @c6` 查看 props、state、hooks，`find TodoItem` 按 display name 搜索并支持 `--exact`，另有 `count` 统计组件类型、`errors` 仅列出有错误或警告的组件。
- ⚠️ **错误与等待**：树和搜索结果会标注 `⚠2 ✗1` 等问题；无应用连接时 `errors` 以退出码 1 返回 `No React app is attached`；`wait --connected` 或 `wait --component App --timeout 30` 阻塞到条件满足，成功退出 0、超时退出 1。
- 📈 **性能分析**：`profile start/stop` 采集数据，`profile slow` 找平均渲染最慢组件，`profile rerenders` 找重复渲染最多组件，`profile timeline` 看 commit 时间线，`profile commit` 看单次 commit，`profile report @c1` 看单组件报告，`profile export` 导出 React DevTools Profiler JSON，`profile diff before.json after.json` 比较两次导出并支持 `--limit`、`--threshold`。
- 🌐 **Web 接入**：`init` 可为 Vite、Next.js、Create React App 打补丁，`uninit` 撤销；也可在入口首行加入 `import "agent-react-devtools/connect"`，处理 Vite hook stub、`react-devtools-core` 初始化与 WebSocket 连接，daemon 不在时 2 秒超时且不阻塞应用；Vite 可用 `reactDevtools()` 插件，仅 dev 模式运行，支持 `port`/`host` 选项。
- 📱 **React Native 接入**：React Native 0.87 移除独立 DevTools 自动连接路径后必须接入；安装 `npm install --save-dev agent-react-devtools` 后，用 `withAgentReactDevTools(config)` 包裹最终 Metro 配置并置于最外层，再在入口图可达的用户模块导入 `agent-react-devtools/react-native`；`init` 可自动处理常见 CommonJS Metro 配置和 `package.json` main、Expo Router 根布局、裸 `index.*`、Expo `App.*` 等入口，遇不安全识别会预检失败并保持文件不变；ESM `.mjs`、TypeScript、JSON/package-field、自定义 `--config` 或识别不确定时需手动配置。
- 🛠️ **原生端限制与排障**：该集成仅从原生开发运行时连接，生产原生构建不会连接，浏览器及默认/server 导入解析为 no-op；Android USB 需 `adb reverse tcp:8097 tcp:8097`；`status` 显示零连接时应检查 Metro 包装与入口导入、确认最外层包装、重启 Metro 并用 `--reset-cache` 或 `npx expo start -c` 清缓存，同时确认 daemon 监听 8097 且应用为开发构建。
- 💬 **代理协作**：与 `agent-browser` 联用需 `--headed` 模式，headless Chromium 不能正确执行 devtools 连接脚本；可用 `npx skills add callstackincubator/agent-react-devtools` 给 AI 编程助手添加技能，支持 Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot、Goose、OpenCode 和 Windsurf；Claude Code 也可通过 `/plugin marketplace add callstackincubator/agent-react-devtools` 与 `/plugin install agent-react-devtools@piotrski` 安装，Codex 从根 `AGENTS.md` 发现 `packages/agent-react-devtools/skills/react-devtools/SKILL.md`，若助手不自动加载技能可在 `AGENTS.md` 或 `CLAUDE.md` 写入手动命令说明。
- 🧪 **开发与许可**：仓库使用 `bun install` 安装、`bun run build` 构建、`bun run test` 测试、`bun run typecheck` 类型检查，采用 MIT 许可证。

### [获取失败](https://www.greatfrontend.com/interviews/pricing?utm_campaign=bf2026&utm_source=web-tools-weekly&utm_medium=newsletter&utm_content=wtw-link-1)

无法总结：获取内容失败，状态码 429。

### [Marlo — 开源 AI CMO 与 AI 营销平台](https://marlo.mlforge.in/marlo)

Marlo 推出开源、自托管的 AI CMO，通过 10 个营销代理覆盖 SEO、GEO、内容、社交与线索获取，并强调所有产出先由用户审核；它同时提供免注册免费网站审计和 $0 自托管、$9/mo 与 $29/mo 托管方案，试图让没有营销预算的小团队也能持续产出可执行的营销工作。产品仍处早期，尚无真实客户，页面中的增长数字为说明性场景。

- 🚀 **开源 AI CMO**：Marlo 是 AGPL 许可的开源、自托管 AI CMO，覆盖 SEO、GEO、内容、社交和需求生成；提供免注册的免费网站审计，返回评分和前三项修复，并可把审计作为链接分享。
- 🧩 **十个代理**：内置 Articles、SEO、GEO、Site Crawl、Reddit、X、LinkedIn、GitHub、Hacker News、Leads 共 10 个代理；默认产出草稿供用户审核，Marlo 不会替用户发布或发送，X 代理在用户连接自有 X API 凭据后可真实发帖。
- 🧠 **研究先行**：先抓取网站生成 `product-information.md`、`marketing-strategy.md`、`competitor-analysis.md`、`brand-voice.md`、`content-strategy.md` 等文档，再由各代理按同一套策略执行；示例显示抓取 24 页，内容要求基于站点真实信息，不虚构数字、客户或引语。
- 🔍 **SEO 与抓取**：SEO 代理通过 HTTP 真实爬取检查 meta 标签、标题结构、Open Graph、重定向链、robots.txt 合规性和服务器耗时；连接 PageSpeed Insights 密钥后拉取真实 Core Web Vitals。Site Crawl 代理支持首页之外的多页抓取，为 SPA 提供 JS 渲染回退，并可选逐页 PageSpeed 评分。
- 🌐 **GEO 检查**：GEO 代理通过 Tavily 实时搜索 API 执行确定性的 3 条查询引用缺口检查，而不是依赖 LLM 主观判断；目标是判断品牌是否出现在 ChatGPT、Perplexity 等 AI 答案中，让 AI 搜索可见性可计划、可衡量。
- 🔗 **集成与数据**：当前已接通 Google Search Console、Google Analytics、Gmail、GitHub、PageSpeed Insights、Tavily、Google Places 共 7 个集成，使用用户自己的 OAuth token 和 API key；自托管数据留在本地数据库，托管方案在服务器加密存储。WordPress、Webflow、Framer、Wix、Sanity、LinkedIn、X、WhatsApp、Telegram、TikTok、Instagram、Slack 标记为 SOON。
- 🛠️ **代理边界**：GitHub 代理把 SEO 发现整理成可审核的 PR 草案，包含描述、改动和建议 diff，但不会自动开 PR；Leads 代理从搜索结果和 Google Places 找真实线索，通过 Gmail 发送并跟踪外联，发送前由用户审核；Reddit 代理当前仅基于示例帖子，真实 Reddit API 接入在路线图中；Hacker News 代理在无法自动发布时会在界面完整披露。
- 📦 **三种运行方式**：自托管为 $0/mo 永久免费，需自带 LLM key（OpenAI、Anthropic 或任何 OpenAI 兼容端点）和集成 key，数据留在自有数据库，AGPL 许可；托管内置模型 $29/mo 包含 AI 模型费用；托管自带模型 key $9/mo 仅收托管费，模型费用直接付给模型提供商。三档均含全部 10 个代理，可随时取消，托管访问需联系。
- 📚 **免费 SEO 工具**：提供 canonical 标签、Open Graph 标签、meta description、H1 标签检查器和 `llms.txt` 生成器，均免注册；检查器与 Marlo 的 SEO 代理使用同一套审计逻辑，并解释每个标签的修复方法。
- 🧪 **早期限制**：Marlo 仍处早期且尚无客户，页面中的 40% 有机流量增长、3x 内容产出、12 个季度 campaign、28% 邮件转化提升等均为说明性场景，不是真实客户结果；Reddit 实时线程发现和 CMS/社交自动发布也尚未完成。

### [错误](https://a11y-tools.com/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='a11y-tools.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

### [GitHub - paulirish/chrome-capture：以 60-120fps / 2160p 从 Chrome 捕获标签页视频/音频 · GitHub](https://github.com/paulirish/chrome-capture)

Chrome 153+ 新增原生 MP4 标签页录制 API `Page.startScreenRecording`，用合成器直连进程外 AV1 编码器的共享内存管线取代约十年的 `Page.startScreencast`，支持标签页音频且停止几乎即时；作者同步发布 `chrome-capture` 与 `startRecording()`，提供 CLI、Playwright/Puppeteer/CDP 集成，并在 M4 Max 上展示相对 ffmpeg 管线的显著提速。

- 🚀 **原生录制**：Chrome 153+ 提供 `Page.startScreenRecording`，可把标签页以 60-120fps、最高 2160p 录成 AV1 编码的 `.mp4`，并支持标签页音频；`chrome-capture` 已发布到 npm，也可直接参考 `src/index.ts` 的轻量实现。
- 🧩 **核心机制**：帧从 compositor 经共享内存直送进程外编码器，Chrome 边录边把 AV1 写入 mp4，无需 ffmpeg；停止时编码已完成，因此可随时开始或停止，适合先登录、预热页面再只录目标交互。停止耗时约 17ms，2160p 下约 91ms。
- 🔄 **管线更替**：过去约十年 `Page.startScreencast` 将每帧 JPEG 经 base64 塞进 CDP JSON，再由 Playwright `recordVideo` 或 Puppeteer `page.screencast()` 送入 ffmpeg。Puppeteer v25.10+ 以实验性 `page.record()` 包装新 API 并弃用 `page.screencast()`；Playwright 的接入 PR #43999 仍处于开放状态。
- 💻 **CLI 用法**：`npx chrome-capture <url> <out.mp4> <duration>` 默认录制标签页音频；60fps 及以下使用 `--headless=new`，macOS 上 `--fps>60` 会自动切到 `--headful`，以便 Chrome 锁定 ProMotion 的 120Hz `CVDisplayLink`。1080p@120fps 示例需 120Hz 屏幕和 headful Chrome。
- 🔧 **编程接口**：`startRecording()` 接受 Playwright `Page`、Puppeteer `Page` 或 CDP session，默认 60fps、1280x720，可配置 `frameRate`、`maxWidth`/`maxHeight`、`captureArea`（`target` 视口或 `browserWindow`）以及 48kHz 立体声 Opus 标签页音频；支持 `await using`，代码块退出时写出 mp4，省略 `outputPath` 时 `stop()` 返回 Buffer。
- 🧪 **测试集成**：`@playwright/test` 提供 `screenRecordingFixture`，设置 `auto: true` 可自动录制每个测试并把 mp4 附加到报告，也可在测试中途手动调用 `start()`；原始 CDP 场景可用 `CdpScreenRecorder` 与 `connectCdpSession` 直接控制。
- 📊 **性能对比**：在 M4 Max 上重放同一段 6.4s、1280x800 的 UI 操作，`chrome-capture` 默认 60fps 对比 `recordVideo` 的 `startScreencast`+ffmpeg 管线：输出从 25fps（最高 60）升至 60fps（最高 120），总耗时 21s 降至 11s，停止与收尾 3800ms 降至 17ms，WebSocket 流量 10.5MB 降至 450KB，文件 480KB 降至 330KB，PSNR 32dB 升至 34dB；音频从无变为可选。
- ⚡ **码率质量**：目前没有 bitrate/CRF 旋钮；底层使用 `libaom` AV1 实时 1-pass VBR，目标码率随像素率线性增长：720p30 为 2Mbps、1080p60 为 9Mbps、1080p120 为 18Mbps、2160p120 为 72Mbps。1080p60 及以上是画质甜点，提高分辨率或帧率可间接提高码率；若需无损 1px 文本且只要求 10-15fps，仍可用 `Page.startScreencast({format: 'png'})` 加 ffmpeg 的离线管线。
- 📈 **性能上限**：Mac headless 可稳定 2160p@60，但 rAF 由合成 60Hz 定时器驱动而非显示器 `CVDisplayLink`；Mac headful 加 120Hz ProMotion 可达 1080p@120fps 和 2160p@120fps（119.9fps，59.8Mbps AV1 加立体声 Opus）；无 GPU 的 Headless Linux 为 1080p@60 或 1440p@60，解除 vsync 可到 1080p 75-83fps；Windows/Linux 独显配置尚未给出数据。
- ⚠️ **macOS 注意**：GPU 加速的 Mac 上不要传 `--disable-frame-rate-limit --disable-gpu-vsync`，否则 rAF 会飙到 1600-9800fps，淹没 Metal 命令队列并导致 capture readback 得不到足够资源，2160p@60 可能掉到 0.3fps；保留原生 vsync 才能达到 120fps。
- 🎨 **光标捕获**：Playwright 下 `await page.screencast.showActions()` 会把光标、元素高亮和点击徽标画进 DOM 且不启动 `Page.startScreencast`，`startRecording(page)` 可原生捕获；要自定义光标 SVG 和点击环，可注入 DOM overlay，示例见 `examples/custom-cursor/` 与 `examples/raw-cdp-cursor/`。

### [GitHub - kcmr/chai-aria-snapshot：用于内联 ARIA 快照的 Chai 断言。· GitHub](https://github.com/kcmr/chai-aria-snapshot)

chai-aria-snapshot 是面向 Chai 的插件，把 Playwright 与 Vitest 的 ARIA 快照思路引入浏览器测试，用 YAML 描述 DOM 元素的可访问树并断言角色、可访问名称、状态、阅读顺序和语义层级，从而降低断言对具体 HTML 标签的耦合。

- 🚀 **插件能力**：`chai-aria-snapshot` 用 YAML ARIA 快照断言 DOM 元素的可访问结构，覆盖 role、可访问名称、状态、阅读顺序和语义层级，不绑定具体 HTML 标签；思路来自 Playwright ARIA snapshots 和 Vitest 的 ARIA snapshots（由 Ivya 提供）。安装命令为 `npm install -D chai-aria-snapshot`，要求项目提供 Chai `^4.3.4 || ^6.3.0` 并在真实浏览器环境运行。
- 🧩 **模板语法**：每个 YAML 节点描述 role、可选名称、可选状态/属性和可选子节点或元数据；名称可精确匹配、用正则如 `/Details|More info/` 匹配或省略以匹配任意名称，方括号属性如 `[pressed=false]`、`[checked=mixed]`、`[disabled]`、`[level=2]` 只校验显式写出的项，行内文本和 `/url` 等属性可断言文本内容与链接目标。角色、名称和状态对应 Chrome DevTools 的可访问性树，完整语法见 Vitest ARIA snapshot 指南，支持属性取决于 Ivya 版本。
- 🌐 **Shadow DOM**：传给 `expect(element)` 的元素是快照根：可传宿主组件断言完整可访问输出，也可查询后代只检查较小子树；开放 Shadow DOM 和 slot 投影内容会被自动遍历，例如宿主 shadow root 中的 `h2` 与 light DOM 中经 `<slot>` 投影的 `p` 会按渲染顺序同时出现在断言中，无需单独查询 shadow root。
- 🎯 **匹配策略**：模板默认是部分匹配：未列出的名称、状态和兄弟元素可被忽略，只要列出的子节点按指定顺序出现；`/children` 可放在顶层或父节点块中，`contain` 为默认行为，`equal` 只允许该层级列出子节点但后代仍部分匹配，`deep-equal` 要求整棵子树与列出的子节点和后代完全一致。即使使用 `deep-equal`，状态和名称仍是逐节点显式启用，省略 `[pressed=false]` 不会校验该状态。
- ⚙️ **API 行为**：API 为 `await expect(element).to.matchAriaSnapshot(expectedYaml, options)`；`element` 必须是已连接 DOM 的 `Element`，`expectedYaml` 为非空 YAML 且自动去除公共前导缩进，`options.timeout` 默认 `1000` 毫秒、须为有限且 `>= 0` 的数值，设为 `0` 表示单次检查。正向和 `.not` 断言都返回 `Promise<void>`，必须 `await`；自动重试最多每 `50` 毫秒捕获并匹配一次直到通过或超时，并复用原始元素引用，若重渲染替换了 DOM 节点需先查询新元素。
- 🔄 **否定与校验**：`.not` 在观察到不匹配时立即 resolve，传 `{ timeout: 0 }` 可立即断言不匹配而无需等待；断开的元素、非 `Element` 值、空模板、非法 YAML 语法和非法 `timeout` 会快速失败并立即 reject，即使使用 `.not` 也不重试。
- 📊 **差异输出**：超时后失败会抛出 Chai 实例的 `AssertionError`，携带 `{ actual, expected, showDiff: true }`，差异渲染由测试运行器或报告器处理；插件不写文件也不改写测试源码，若需存储 `.snap` 文件可配合运行器的快照辅助工具，例如 `@web/test-runner-commands`，示例见 `demos/snapshot-output`。
- 🛠️ **开发测试**：开发需匹配 `package.json` 中 `engines.node` 的 Node.js、`packageManager` 指定的 pnpm，并安装 Playwright 浏览器以在 Chromium、Firefox 和 WebKit 运行测试，Linux 可能还需 Playwright 系统依赖；常用命令包括 `pnpm install`、`pnpm browsers:install`、`pnpm check`、`pnpm dev`、`pnpm test` 和 `pnpm format`。测试使用构建后的包声明，新检出缺类型时运行 `pnpm build`，`pnpm test` 和 `pnpm check` 也会自动构建；外部项目可先 `pnpm build`、`pnpm pack` 再安装生成的 `.tgz`。

### [Tinkerfont：字体测试 Chrome 扩展与 Firefox 附加组件](https://tinkerfont.com/)

Tinkerfont 是面向设计师、开发者和字体爱好者的 Chrome 扩展与 Firefox 附加组件，用于在真实网站上检查、替换和测试字体，让用户在改 CSS 或打开 Figma 前查看候选字体在真实内容、布局和断点下的表现；它支持 1900+ Bunny Fonts 或本地上传，规则按 hostname 本地保存，免费、无需账号且不收集浏览数据。

- 🧩 **右键检查**：右键菜单可打开 Tinkerfont 检查任意文本的字体规格，点击值可复制 family、color、contrast，或在可用时复制实验性字体文件 URL；该功能灵感来自 Fontanello。
- 🔍 **页面扫描**：扫描实时 DOM，列出页面实际使用的字体及计数；点选某个 family 可定位目标，或用 `*` 覆盖全部。
- ⚡ **即时替换**：可搜索 Bunny Fonts 的 1900+ 字体或上传字体，一键应用到页面，无需 DevTools、部署或账号。
- 🎯 **区域限定**：可在页面上选择元素来限定替换范围，例如只让导航或表格试用新字体；区域按 hostname 保存。
- 🔄 **规则持久化**：替换规则和区域范围按 hostname 存入本地，刷新或稍后回访仍保留；面板中的 Rescan 可清除并重来。
- 🔗 **分享与迁移**：Share 会复制当前 hostname 的规则和区域链接，队友在同一站点粘贴即可；也可从 tinkerfont.com/go 下载 JSON。面板支持 Export/Import 备份规则，Bunny Fonts 规则导入即用，自定义字体需在新设备重新上传文件。
- 🛡️ **隐私与本地存储**：无需账号，不向 Tinkerfont 服务器发送浏览数据（其不运营服务器）；规则、区域、主题和上传字体存于设备本地，Chrome 用 `chrome.storage.local`，Firefox 用 `browser.storage.local`。
- 📦 **格式与限制**：自定义字体支持 `.woff2`、`.woff`、`.ttf`、`.otf`；Bunny Fonts 以 data URL 内联，常在阻止外部字体 CDN 的页面生效，但 Chrome Web Store、`chrome://` 等受限页面无法运行扩展。
- 🌐 **浏览器支持**：提供 Google Chrome 和 Mozilla Firefox 版本；支持 Chrome 扩展的 Chromium 浏览器可能可用，但官方测试和发布覆盖的是 Chrome 与 Firefox。
- ✅ **免费使用**：安装和使用免费，所有功能无需付费；可选支持者捐助用于持续开发，无需账号。

### [Flashwright：最快的端到端测试框架，可直接替代 Playwright](https://flashwright.dev/)

Flashwright 是一个可直接替换 Playwright 的端到端测试框架，API、测试运行器和 npx playwright test 命令完全保持一致，通过安装别名包 @playwright/test@npm:flashwright-test 即可让现有测试套件无需修改直接运行；官方基准显示，其整套测试命令的耗时比 Playwright 快 2–4 倍，快于参与对比的全部 9 个框架。它只在 Playwright 耗时较多的地方做优化：复用浏览器进程、为每个测试新建上下文、根据页面变化重新检查等待条件、提前启动 worker、使用 V8 代码缓存、加速截图；同时把每一项改变默认行为的设置都做成可回退的类型化选项。

- 🚀 **无需改动即可替换**：导入、配置与 npx playwright 命令都保持不变，浏览器、报告器、trace viewer 和 VS Code 扩展仍由 Playwright 提供；只需把依赖换成 @playwright/test@npm:flashwright-test，现有套件即可无需改动直接运行。
- ⚡ **基准性能**：以 Playwright 1.64.1 为基线、在相同机器、Chromium headless shell 上取 15 次交替运行的中位数，所有场景至少快 2 倍：TodoMVC 24 个测试 1 worker 从 3617ms 降到 968ms（3.74×），4 workers 从 1767ms 降到 721ms（2.45×）；登录 setup 项目的 Shop 应用 18 个测试 1 worker 6429ms 降到 2950ms（2.18×）；8500 个元素的 Admin 应用从 6745ms 降到 3018ms（2.23×）；click 与断言场景达 4.10×。可用 node bench/matrix.mjs 15 复现。
- 📊 **横向对比**：同样的 24 个 TodoMVC 测试移植到 9 个工具，每个工具使用各自推荐的等待与隔离方式，所有计入运行中的测试都通过全部 24 个用例。1 worker 下 Flashwright 2.36s，Bun test + Bun.WebView 4.30s（1.8×）、Playwright 4.48s、Selenium + Mocha 5.40s、Puppeteer + Jest 6.17s、Nightwatch 6.29s、WebdriverIO 10.32s、Cypress 16.97s、TestCafe 22.46s；4 workers 下 Flashwright 1.47s、Playwright 3.02s，Cypress 因一次只跑一个 spec 文件需 Cypress Cloud 才能并行，为 16.99s。
- 🧩 **核心机制**：每个测试在 worker 保留的上下文里开新标签页，测试间重置所有可被改动的状态；动作与断言在页面变化时重新检查，而不是按退避计时器轮询；点击不再等待动画稳定，但仍执行命中目标检查。
- 🔧 **启动与截图优化**：worker 和浏览器在读取配置时就开始启动，最长的测试优先执行；通过 V8 代码缓存、懒加载和减少每次动作的浏览器往返加速启动；截图保持相同像素、更快编码，基线文件与 Playwright 逐字节一致。
- 🧠 **面向编码 Agent**：CI 之外可用 warm session 保持运行器、worker 和浏览器常驻，单个 TodoMVC 测试重跑从 Playwright 的 652ms、非 warm 的 234ms 降到 72ms，4 workers 场景从 1751ms 降到 490ms；同时提供 playwright mcp --adaptive-settle，在页面安静后立即返回，而不用固定等待 500ms。
- ⚙️ **默认值与回退**：isolation 默认 'recycled'（每次测试在重置过的上下文里开新标签页）、failFastWhenIdle 默认 true（页面不可能再变化时立即失败）、waitForAnimations 默认 false、testOrder 默认 'longest-first'、locatorPolicy 默认 'any'（设为 'test-id' 后只允许 getByTestId()）；另有 workersPerProcess、preloadPages、instantAnimations、blockResources 等选项，可按项目、文件或 describe 块恢复 Playwright 行为。
- ⚠️ **限制**：提速主要体现在 Chromium；Firefox 和 WebKit 除每个 worker 复用一个标签页外仍保持 Playwright 原有行为，且使用的是 Playwright 自己的浏览器构建。
- ✅ **兼容性验证与回滚**：以 Playwright 自身测试套件作为回归标准：tests/page 在 Chromium 上通过 2610/2610，runner、library 与 MCP 套件的结果与未改动的 Playwright 1.64.1 一致；回退只需执行 npm i -D @playwright/test@1.64.1，因为代码中没有任何地方引用 Flashwright。

### [Codemagic 补丁](https://patch.codemagic.io/docs?utm_source=clickrelay&utm_medium=paid_newsletter&utm_campaign=codemagic-patch-self-host-in-twenty-minutes-direct&utm_content=web-tools-weekly)

Codemagic Patch 为 React Native 和 Capacitor 提供自托管 OTA 更新方案：开发者自行运行 Patch 服务器，应用从该服务器下载更新，而无需等待应用商店发版；同时提供 Codemagic 托管选项、按框架与应用接入的文档，以及供编码代理安装使用的 Patch skill。

- 🚀 **自托管 OTA**：Codemagic Patch 面向 React Native 和 Capacitor，开发者运行 Patch 服务器，应用从服务器获取更新，绕过应用商店发版等待。
- 🧩 **React Native 能力**：支持 JavaScript 与打包资源的 OTA 更新，并提供本地快速开始、服务端安装和应用接入文档。
- 🌐 **Capacitor 能力**：为 Web 资源提供实时更新，同样覆盖本地快速开始、服务端安装和应用接入。
- 🏢 **托管选项**：如不想自行运行服务器，可选择由 Codemagic 托管 Patch，需查看 Pricing 或联系 sales@codemagic.io。
- 🛠️ **编码代理技能**：提供 Patch skill，可按 React Native 或 Capacitor 以及 Claude Code、Cursor、Codex 或任意代理安装；示例包括 `/plugin install codemagic-patch --marketplace codemagic-ci-cd/codemagic-skills`、`npx skills add codemagic-ci-cd/codemagic-skills --skill patch-react-native-setup -a cursor`，Codex 需先执行 `codex plugin marketplace add codemagic-ci-cd/codemagic-skills` 再执行 `codex plugin add codemagic-patch@codemagic`。
- ✅ **首个 Staging 更新**：安装 skill 后，可用它发布并验证第一个 `Staging` 更新。
- 💬 **支持渠道**：遇到问题可在 GitHub 提 issue，或在 Discord 提问。

### [GitHub - mobile-next/mobile-mcp：Mobile MCP：让 AI 智能体驱动你的 iOS 和 Android 应用。适用于模拟器、仿真器和真机的 MCP 服务器。可与 Claude Code、Codex、Cursor 及任何 MCP 客户端配合使用。 · GitHub](https://github.com/mobile-next/mobile-mcp)

Mobile Next 的 mobile-mcp 是 Apache-2.0 许可的开源 MCP Server，面向 AI Agent 的 iOS/Android 原生应用自动化与开发；它以平台无关的统一工具连接模拟器、仿真器和真机，默认从原生 accessibility tree 读取结构化界面并仅在必要时使用截图与坐标，支持 Claude Code、Codex、Cursor 等 MCP 客户端，同时提供 Streamable HTTP、云真机和 Mobilewright 测试路径，降低跨平台移动自动化的接入成本。

- 🚀 **项目定位**：mobile-mcp 是 Apache-2.0 开源 MCP Server，让 Agent/LLM 通过统一接口驱动 iOS 与 Android 原生应用，覆盖模拟器、仿真器和真机，并兼容 Claude Code、Codex、Cursor 等任意 MCP 客户端。
- 🧩 **无障碍优先**：默认基于原生 accessibility tree 驱动应用，避免视觉模型和图像 token 开销；在需要时回退到截图加坐标操作，并输出结构化、确定性的 UI 元素数据。
- ⚙️ **统一控制**：同一套工具跨 iOS/Android 工作，无需 XCUITest 或 Espresso；覆盖点击、双击、长按、拖拽、滑动、输入、硬件按键、应用安装/启动/终止、录屏、深链、方向、定位和剪贴板。
- 🛠️ **平台支持**：iOS Simulator 需要 Xcode 和已启动模拟器（xcrun simctl），iOS 真机需 USB 连接并信任；Android Emulator 需要 Android SDK 和 adb，Android 真机需启用并授权 USB 调试。
- 💻 **快速安装**：npx @mobilenext/mobile-mcp@latest install 会检测本机 MCP 客户端并让用户选择配置，--yes 可无交互配置所有检测到的客户端；通用手动配置使用 command 为 npx、args 为 -y @mobilenext/mobile-mcp@latest，运行要求 Node.js v20+、Xcode command line tools 与 Android Platform Tools。
- 📱 **设备镜像**：在 Claude Code 中通过 /plugin marketplace add mobile-next/mobile-mcp 和 /plugin install mobile-mcp@mobile-mcp 安装插件后，/mobile-mirror [device-id] 可在 kitty 或 Ghostty 侧栏实时显示设备画面，并支持点击、输入及 Home/Back/App Switch/URL 按钮；需要支持 kitty graphics protocol 的终端。
- 🌐 **HTTP 模式**：默认使用 stdio；--listen 3000 启动 Streamable HTTP 服务并绑定 localhost:3000，客户端连接 http://<host>:3000/mcp；远程模式为无状态，无需会话亲和，适合 Smithery 等横向托管。--listen 旧版曾提供已弃用的 HTTP+SSE，现在客户端必须使用 Streamable HTTP，/mcp 上的纯 SSE 流程已不可用。
- 🛡️ **HTTP 安全**：设置 MOBILEMCP_AUTH=my-secret-token 后，所有 HTTP 请求必须携带 Authorization: Bearer my-secret-token；未设置时接受未认证连接并记录警告；绑定 localhost 时自动启用 Host-header DNS rebinding 保护，默认阻止非标准 URL scheme，可用 MOBILEMCP_ALLOW_UNSAFE_URLS=1 放开。
- 🧪 **CI 测试**：Agent 会话中的移动流程可转写为 Mobilewright 测试，使用 @mobilewright/test 的 screen.getByLabel、getByRole、tap 和 expect 等 API 形成确定性用例；npm init mobilewright@latest 初始化，并可接入 GitHub Actions 等 CI/CD。
- 📦 **批量命令**：MCP 提供设备管理、应用管理、屏幕交互、输入导航、日志与崩溃报告等工具；mobile_batch_commands 可在一次调用中按序执行多个工具，支持步骤间 delay，并可在末尾列出屏幕元素。
- 📊 **云真机**：通过 Mobile Next Cloud 工具 mobile_login_to_cloud_provider、mobile_list_remote_devices、mobile_allocate_remote_device、mobile_release_remote_device，可登录云设备提供方、列出可预订机型、独占预留和释放真实 iOS/Android 设备。
- 📝 **配置项**：MOBILEMCP_DISABLE_TELEMETRY=1 或 DO_NOT_TRACK=1 可关闭 PostHog/Scarf 匿名遥测；MOBILEMCP_LEGACY_ROBOT=1 对 Android 设备和物理 iOS 设备启用旧平台机器人，iOS 模拟器继续使用 mobilecli。

### [GitHub - mrousavy/react-native-data-scanner：适用于 React Native 的超快速单次 QR/条码/数据扫描 · GitHub](https://github.com/mrousavy/react-native-data-scanner)

react-native-data-scanner 是一个面向 React Native 的一次性 QR/条码/数据扫描库，基于 Nitro Modules 和平台原生扫描界面实现。Android 通过 Google Play Services 的 Google Code Scanner 扫描且无需相机权限，iOS 通过 VisionKit 的 DataScannerViewController 扫描；库提供简单的 scanBarcode API，并提醒 Expo 需使用开发构建或生产构建而非 Expo Go。

- 🚀 **扫描能力**：提供超快的一次性 QR/条码/数据扫描，适用于 React Native，依赖 `react-native-nitro-modules` 和平台原生扫描 UI。
- 🧩 **平台机制**：Android 使用 Google ML Kit 的 Google Code Scanner，通过 Google Play Services Activity 扫描，不需要相机权限；iOS 使用 VisionKit 的 `DataScannerViewController`。
- 📦 **安装依赖**：通过 `npm install react-native-data-scanner react-native-nitro-modules` 安装；Android 无需额外配置。
- 🛠️ **iOS 配置**：iOS 需在 `Info.plist` 或 Expo 配置中加入 `NSCameraUsageDescription`；Expo 应用因包含原生代码需使用开发构建或生产构建，不能在 Expo Go 中运行，修改原生配置后需重新构建。
- 🎯 **API 用法**：调用 `DataScanner.scanBarcode(options?)` 会展示原生扫描 UI，并解析用户选择的第一个条码；示例传入 `targetFormats: ['qr', 'ean-13']` 和 `enableAutoZoom: true`。
- ⚙️ **选项默认值**：`targetFormats` 为可选的非空格式数组，省略则扫描所有支持格式；`qualityLevel` 默认 `'balanced'`，`enableHighFrameRateTracking` 默认 `false`，`enableAutoZoom` 默认 `false`。
- ⚠️ **失败条件**：当扫描不可用、用户取消、已有另一个扫描正在进行，或扫描到的条码不包含可解码的字符串值时，Promise 会拒绝。
- 🔧 **Android 模块**：库通过 Android manifest 请求在安装时下载 Google Play Services 的 `barcode_ui` 可选模块。
- 💡 **进阶场景**：如需高级用例或应用内 `<Camera>` 视图，原文建议考虑使用功能完整的 VisionCamera 相机库。

### [GitHub - gmi-software/react-native-better-clustering：在 react-native-maps 上聚合点的更好（更快）方式 · GitHub](https://github.com/gmi-software/react-native-better-clustering)

GMI Software 开源 `react-native-better-clustering`（已发布 1.1.0），作为 `react-native-map-clustering` 的 drop-in replacement，在不改变 `react-native-maps` 工作流的前提下，把聚类索引改为通过 Nitro 在 C++ 后台线程构建，以缓解大量标记导致的挂载卡顿、重渲染重建索引和缩放时渲染过多问题。基准显示 100,000 个标记场景下首屏和 JS 阻塞显著降低，但该库只替换聚类层，`react-native-maps` 自身问题仍可能存在，且聚类点击后相机稳定约慢 0.45 秒。

- 🚀 **发布与定位**：`react-native-better-clustering` 1.1.0 是 `react-native-map-clustering` 的 drop-in replacement，保留相同 API 和 `react-native-maps` 工作流，目标是用更快的方式在 `react-native-maps` 上聚类点。
- 🧩 **核心机制**：聚类索引通过 Nitro 在 C++ 后台线程构建，而非在 JS 线程构建；重渲染时保留索引和每个已挂载标记，避免每次父级更新都重建索引。README 对比称旧库查询四倍屏幕区域，zoom 8 时渲染约 3–4 倍标记和气泡，多数在屏幕外。
- ⚡ **性能基准**：同一 App、默认 props、Release/Hermes、5 次中位数；`react-native-better-clustering` 1.1.0 release candidate 对比 `react-native-map-clustering` 4.0.0：100,000 个标记首次出现 434 ms 对 3,557 ms，挂载最长 JS 冻结 170 ms 对 3,558 ms，10 次父级重渲染期间 JS 阻塞 1,719 ms 对 35,899 ms；10,000 个标记对应为 193 ms 对 359 ms、27 ms 对 360 ms、0 ms 对 2,877 ms。
- 🔄 **迁移方式**：通常只需把 `react-native-map-clustering` 的 `MapView` 导入改为 `react-native-better-clustering`，`<Marker>` 子节点、cluster props 和 `react-native-maps` 选项可沿用；默认 cluster 颜色及 `style` 应用方式等存在差异。建议给每个 `Marker` 稳定 `key`，不要用数组索引。
- 🛠️ **问题修复**：README 列出对旧库问题的处理：为 `NaN` 缩放加有限值回退（#294），Android 上针对布局处理 `fitToCoordinates`（#285），实现 `maxZoom`/`spiralEnabled`（#274/#275），在渲染间保持稳定 cluster 引用（#255），并支持逐标记 `cluster={false}`（#297）。
- 📦 **安装要求**：支持 iOS/Android，需要 React Native 0.78+ 的 New Architecture、`react-native-maps` 1.20.1+ 和 `react-native-nitro-modules` 0.32.0+；Expo 需 development build，Expo Go 不可用。Android 必须配置 Google Maps key，否则地图挂载时崩溃；Expo SDK 55+ 用 `react-native-maps` 配置插件的 `androidGoogleMapsApiKey`，SDK 53/54 用 `expo.android.config.googleMaps.apiKey`。安装后需重新构建原生应用。
- 🎨 **可选动画**：`Reanimated` 4.1+ 为可选依赖；启用后，cluster 气泡在缩放时支持淡入淡出和滑动动画。
- ⚠️ **限制与回归**：该库只替换聚类，不修复 `react-native-maps` 自身问题，例如 Android 幽灵标记和导航崩溃仍可能发生；README 也注明点击 cluster 后相机稳定约晚 0.45 秒。
- 🔍 **高级 API**：提供 `useClusterer`、`Clusterer` 和无头引擎，供自有地图栈使用；100,000 点时 `useClusterer` 每次索引构建阻塞 JS 11 ms，对比 `react-native-clusterer` 5.0.2 的 234 ms 和 `use-supercluster` 1.2.0 的 2.3 s，且平移时不重建索引，而两者会重建。
- 📚 **文档与示例**：文档覆盖 props、`renderCluster`、可访问性、安装、迁移、高级 API、性能和故障排查；示例 App 包含 2,000 到 50,000 个标记的场景及设备基准。

### [agent-device：面向智能体的开源设备层](https://agent-device.dev/)

agent-device 以开源设备层的形式把编码代理接入真实应用运行环境，让代理在本地或云端的真机、模拟器和设备上控制移动、Web、TV 与桌面应用，并把截图、视频、日志和可回放脚本作为验证证据带到评审与 CI 中。它补上了代理写完代码后无法亲自到设备上验证的环节，同时通过 `.ad` 脚本、JUnit 报告、MCP/Node.js API 和托管设备接入，把代理自测、回归回放、性能剖析与多人多代理协作串成一条可执行链路。

- 🚀 **开源发布**：agent-device 是面向编码代理的开源设备层，让代理在本地或云端的真机、模拟器上控制移动、Web、TV 和桌面应用；支持 iOS、Android、HarmonyOS、tvOS、Android TV、Fire TV、Vega OS、macOS、Linux、Web、React Native、Expo、Flutter，安装命令为 `npm i -g agent-device`，页面显示 npm 3M+/mo、GitHub 5.5K。
- 🧩 **设备操作命令**：代理可通过 `open`、`snapshot`、`screenshot`、`record`、`press`、`fill`、`wait` 等命令读取界面并操作元素，支持 `@e2` 元素引用和 `role=button label="Done"` 选择器；原文用 onboarding 与 Contacts 示例展示跨 iOS/Android 运行、填写联系人并等待文本出现。
- 🧪 **代理自验证**：代理可在模拟器或设备上运行改动、读屏、点击流程并自行修复，在人工评审前附上截图和视频；Expensify 的代理技能会复现 bug、录前后视频、回放 `.ad` 脚本、测量 Sentry span 并剖析 React 渲染，作为 PR 证据。
- 📦 **证据与 CI 回放**：用 `--save-script` 把成功运行保存为 `.ad` 脚本，用 `record start/stop` 生成 mp4；CI 中执行 `agent-device test ./workflows --reporter junit:./tmp/junit.xml` 可在无模型参与下回放，并保留截图、日志和 JUnit 报告。
- 📊 **React 性能剖析**：`react-devtools profile start/stop/report` 可定位渲染问题；示例在 8.3s 内记录 8 次 commit、1303ms 渲染、8 次超过 16ms（最差第 6 次 188ms），ContactRow 的 memo 在 480/480 次更新中被绕过，报告建议在 ContactList 用 `useCallback`/`useMemo` 稳定传入的 object 和 function props。
- 🌐 **多地运行**：本机会话跟随 git worktree，CI 可回放脚本；设备主机用 `agent-device proxy --port 4310 --public-origin https://...` 建隧道，隧道终止 TLS 时该参数必填；托管设备内置 BrowserStack、AWS Device Farm、Limrun，TestMu AI 通过 provider 插件接入，Expo Simulators on EAS 也可驱动。
- 🛠️ **接口与生态**：`agent-device mcp` 启动官方 stdio MCP server，CLI、MCP 与类型化 Node.js API 共享同一运行时，会话、证据和回放行为一致；e2e 的 `@e2e-dev/mobile` 和 T3 Code 的模拟器/仿真器支持构建在其上，另有 AI SDK tools 与 Eve 集成。
- 🔄 **与现有框架互补**：与 Appium、Detox、Maestro 运行由人编写维护的套件不同，agent-device 让代理在运行时读应用并逐条选择命令；它可将运行保存为 `.ad` 脚本或导出严格 Maestro YAML，并用 `agent-device capabilities --platform <platform>` 查看目标平台能力。
- 🏢 **采用与协作**：Expensify、Shopify、MetaMask、Uniswap、Expo、T3 Code、e2e 等团队和项目使用；会话按 git worktree 隔离，设备占用声明防止并行代理抢占彼此的模拟器，`agent-device device status` 可查看谁持有哪些设备。

### [GitHub - callstack/react-native-bottom-tabs：React Native 原生底部标签栏 · GitHub](https://github.com/callstack/react-native-bottom-tabs)

Callstack 维护的 react-native-bottom-tabs 是一个为 React Native 提供原生底部标签栏的库，基于 iOS、Android 等平台的原生原语实现，而不是用 Web 技术模拟，目标是让标签栏获得更贴近平台的原生体验。仓库同时提供 Expo 模板和 React Navigation 集成包，覆盖手机、平板、电视、Vision Pro 和 Mac 等多种平台，但不支持 Web。

- 🧩 **原生实现**：该库使用原生平台原语构建底部标签栏，而非依赖 Web 或纯 JS 方案，以提供更贴近系统的交互和外观。
- 🌐 **平台覆盖**：支持 iOS、Android、iPadOS、visionOS、tvOS 和 macOS；由于原生原语在 Web 上不可用，Web 端需参考文档中的 Web Platform Support 指南。
- 📦 **包与集成**：仓库包含主包 `react-native-bottom-tabs`、Expo 模板 `@bottom-tabs/expo-template` 和 React Navigation 集成包 `@bottom-tabs/react-navigation`。
- 🛠️ **文档与构建**：完整文档发布在 oss.callstack.com/react-native-bottom-tabs，项目使用 `create-react-native-library` 创建，并采用 MIT 许可证。
- 📈 **社区数据**：仓库当前约有 1.5k stars、112 forks 和 415 次提交，页面显示 12 个 issue 与 22 个 pull request。

### [获取失败](https://www.greatfrontend.com/projects/pricing?utm_campaign=bf2026&utm_source=web-tools-weekly&utm_medium=newsletter&utm_content=wtw-link-2)

无法总结：获取内容失败，状态码 429。

### [GitHub - satya164/react-native-animated-observer：用于在 Animated 值与 Reanimated 值之间相互转换的辅助工具 · GitHub](https://github.com/satya164/react-native-animated-observer)

react-native-animated-observer 是用于观察 Animated 与 Reanimated 值并在两者间转换的 React Native 辅助库，面向组件使用 Animated 而应用使用 Reanimated，或反之的混用场景；它导出 AnimatedConverter 和 AnimatedObserver，通过原生组件派发值变化事件来更新对应的动画值。

- 🔄 **双向转换**：`AnimatedConverter` 可在 `Animated.Node` 与 `SharedValue<number>` 之间进行原生转换，帮助组件兼容不同的动画体系。
- 🎯 **转换范围**：`AnimatedConverter` 的 `from` 支持 `Animated.Node`，包括 `Animated.Value` 以及插值、加法等修改结果；`to` 支持 `Animated.Value` 或 `SharedValue<number>`。
- 🧪 **观察组件**：`AnimatedObserver` 观察给定值并在变化时通过 `onValueChange` 触发回调，`value` 支持 `number`、`Animated.Node`、`SharedValue<number>` 或 `DerivedValue<number>`，它是 `AnimatedConverter` 的构建块。
- ⚙️ **工作机制**：库渲染原生组件来接收 `Animated.Node` 或 `SharedValue<number>`，值变化时派发事件，再使用 `Animated.event`（native driver）或 `useEvent` 更新 `Animated.Value` 或 `SharedValue<number>`。
- 📦 **安装方式**：使用 `npm install react-native-animated-observer` 安装。

### [GitHub - software-mansion/enriched-markdown：跨平台 Markdown 富文本解决方案 · GitHub](https://github.com/software-mansion/enriched-markdown)

Software Mansion 的 enriched-markdown 是一个多平台 Markdown 富文本 SDK，目标是在 React Native、iOS、Android 等平台用原生文本 API 渲染 Markdown，并支持以 Markdown 为输出进行富文本编辑；它同时提供 React Native 库和面向 iOS Swift、Android Kotlin 的独立原生 SDK，覆盖 CommonMark/GFM、LaTeX、流式 Markdown 与代码高亮等能力。

- 🧩 **项目定位**：提供将 Markdown 渲染为原生文本，并以 Markdown 输出编辑富文本的多平台 SDK。
- 🌐 **多端覆盖**：以 React Native 库覆盖 iOS、Android、macOS 和 Web，同时提供 iOS Swift 与 Android Kotlin 的独立原生 SDK，并在 React Native TypeScript、iOS Swift、Android Kotlin 间保持一致的 API。
- ⚡ **原生渲染**：基于平台文本 API 实现高性能 Markdown 渲染，不使用 WebView。
- 📝 **富文本编辑**：提供带 Markdown 输出的文本输入能力，支持内联格式、标题、列表、链接和提及。
- 📚 **标准支持**：完整支持 CommonMark，并包含 GitHub Flavored Markdown 扩展，如表格、任务列表和删除线。
- 🧪 **数学公式**：通过 RaTeX 支持块级和行内 LaTeX 数学公式渲染。
- 🔍 **代码高亮**：通过 tree-sitter 提供原生代码语法高亮。
- 💬 **流式 Markdown**：支持面向 AI/LLM 聊天界面的实时 Markdown 流式渲染。
- ♿ **无障碍**：iOS 支持 VoiceOver，Android 支持 TalkBack，Web 提供语义化 HTML。
- 📦 **快速接入**：React Native 通过 `yarn add react-native-enriched-markdown` 接入并使用 `EnrichedMarkdownText`；Android 使用 `com.swmansion.enriched.markdown:compose:0.3.0`；iOS 通过 Swift Package 从 `0.1.0` 起接入。
- 🛠️ **开源许可**：项目以 MIT License 发布。

### [GitHub - V3RON/react-native-playback-controls：控制系统媒体界面（锁屏、控制中心、Android 媒体通知、蓝牙按钮），无需自行播放音频。· GitHub](https://github.com/V3RON/react-native-playback-controls)

react-native-playback-controls 是一个采用 MIT 许可证的 React Native 库，用于在不自行播放音频的前提下控制系统媒体界面，包括 iOS 锁屏和 Control Center、Android 媒体通知以及蓝牙/硬件媒体按键。它定位为面向新架构 Turbo Modules 的 react-native-music-control 替代方案，由应用自己的播放器负责音频与 AVAudioSession，本库负责系统级“正在播放”界面和远程命令。

- 🎯 **项目定位**：库只管理系统媒体 UI 和远程命令，不播放音频；播放器可使用 react-native-video、expo-audio 或原生 AVPlayer 等，系统层“now playing”表面由本库接管。
- 🧩 **架构限制**：仅支持启用新架构的 React Native，依赖 Turbo Modules 与 codegen EventEmitter，不提供旧架构回退；开发与测试基于 RN 0.83，未验证旧版 0.8x 的新架构兼容性。
- ⚙️ **平台要求**：iOS 15.1+；Android minSdkVersion 24+、compileSdk 36。安装使用 yarn add react-native-playback-controls 或 npm install，并执行 cd ios && pod install。
- 🛡️ **iOS 前置条件**：控件仅当应用是系统当前“Now Playing”应用时出现，需有处于 .playback 分类且实际输出音频的活跃 AVAudioSession；本库刻意不触碰 AVAudioSession，若需后台接收命令还需在 Info.plist 配置 UIBackgroundModes: audio。
- 📱 **Android 前置条件**：前台服务权限和 manifest 声明由库自动处理；应用需在 Android 13+ 调用 startSession 前自行请求 POST_NOTIFICATIONS，否则会话可启动但不显示通知；startSession 必须从前台调用，后台启动会抛错。
- 🔄 **Android 生命周期**：用户从最近任务划掉应用后，媒体通知和控件会被关闭，这是设计行为；当前版本没有复活机制，因为 JS 已停止无法处理按键。
- 💻 **核心 API**：PlaybackControls.startSession(options) 启动应用级会话并返回 PlaybackSession，提供 setNowPlaying、setPlaybackState、setCommands 和 addCommandListener；useRemoteCommand(session, command, handler) 用于在组件生命周期内订阅单个远程命令。
- 🎨 **命令差异**：iOS 仅投递 toggle-play-pause，Android 始终投递 play/pause；示例建议同时注册 play、pause、toggle-play-pause，以覆盖两个平台。
- 📚 **文档内容**：docs/API.md 记录完整方法签名、错误码、CommandConfig、NowPlayingMetadata、PlaybackState 等类型，以及 setNowPlaying 的合并与替换语义、toggle-play-pause 投递方式等平台差异。
- ⚠️ **常见问题**：iOS 控件不显示通常是应用不是当前 Now Playing 应用或缺少活跃 AVAudioSession 与音频输出；Android 13+ 无通知通常是未请求 POST_NOTIFICATIONS；session-already-active 表示已有会话需先 end()，foreground-required 表示在 Android 后台调用了 startSession。
- 🔮 **路线图**：v1 刻意暂缓评分/反馈命令、自定义通知按钮、shuffle/repeat、队列元数据、CarPlay/Android Auto 浏览等能力，后续想法记录在 docs/IDEAS.md。

### [联系 Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

Web Tools Weekly 发布了一个广告咨询联系页面，说明在该周刊投放广告的流程和可选方案，并提醒该表单仅用于广告咨询，不构成预订。

- 🏢 **广告方案**：页面列出可选的广告位：Top Ad + Top Text Link、Paid Product Review、Middle Image Ad、Text Link Combo、Classified Listing 和 Ad Swap，用户可在表单中选择意向方案。
- 📝 **表单必填项**：咨询表单要求填写 Name、Email Address、URL to Advertise、Ad Plan Desired 以及 Comments / Instructions，用于说明具体需求或问题。
- ⚠️ **非预订声明**：页面明确提示提交表单不构成预订（booking），表单仅用于广告咨询或询问当前档期与可用性。
- 💬 **其他联系方式**：非广告类咨询或工具投稿不在该表单范围内，需通过 X 私信、Bluesky 聊天或直接回复订阅邮件联系。
- 🔗 **查询入口**：用户可先在 Advertising Plans 页面查看投放选项，再发消息询问当前是否有可用档期。

### [Keyframer.dev — React Native 可视化动画编辑器](https://keyframer.dev/)

总结失败：模型未返回符合格式的摘要。

### [内置分析功能的 JavaScript 数据网格 | Lattice Grid](https://www.latticegrid.dev/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=lg_launch_2026q3&utm_content=text_ad_w35)

Lattice Grid 将高性能数据网格与仪表盘、甘特图、看板、日历、排程器和表单整合为同一套实时数据应用组件，并通过数据路由引擎让多个视图共享一条实时数据流。它内置浏览器端派生网格、分组统计比较、数值解释和聚类分析，提供多框架接入，并采用按域名授权、localhost 免费的模式。

- 🧩 **统一套件**：一个授权覆盖 Grid、Dashboards、Gantt、Kanban、Calendar、Scheduler 和 Forms，所有视图共享同一份实时数据；页面按正在构建的视图组织为可运行组件。
- 📊 **视图能力**：Dashboards 提供 KPI 瓦片、图表和地图，可在 Designer 或代码中构建；Gantt 支持依赖、关键路径和资源负载；Kanban 移动卡片会更新行；Calendar 基于日期列并可拖拽改期；Scheduler 标记人员或机器过度分配；Forms 含记录编辑器和应用外壳。
- 🔍 **分析能力**：支持从现有行派生网格并按服务汇总成本、对两个或以上服务做统计检验并报告 p 值、差值区间和结论、拆解总值构成，以及按成本和变化生成聚类；筛选后所有结果基于剩余行重算。
- 🔗 **数据路由**：Data Router 将订单、发货和事件等单一直播流按记录类型分区，每个网格和图表只接收自己的切片并实时更新，无需为每个面板单独建立连接。
- 🛠️ **框架集成**：提供 JavaScript、React、Vue、Svelte、Angular、Web Component、htmx 和 Python 入口；可从现有框架的运行示例复制 starter，htmx 页面可从服务端渲染的普通表格起步。
- 🔑 **授权模式**：单域名授权为 1,000 美元，含不限开发者和一年支持；localhost 免费且无密钥和时间限制，staging、preview 或 CI 带小水印但不影响运行，非商业 key 去水印、单域名六个月可续，正式产品或内部工具需按域名授权。
- 🧪 **在线演示**：演示使用 5000 条生成的云成本数据，全部在浏览器中运行；筛选主网格后，派生网格、分组比较、数值解释和聚类都会随剩余行重新计算。

### [Instaparser](https://instaparser.com/)

Instaparser 推出面向开发者的网页内容清洗 API 平台，一次性提供文章抽取、PDF 解析和 URL 摘要三类接口，所有套餐均包含这三项能力；它基于 Instapaper 自 2008 年起打磨的解析引擎，宣称不做与反爬机制对抗的抓取，而是专注理解页面内容，直接返回结构化 JSON。平台已提供 Python 与 Node SDK，并可免注册粘贴 URL 试用，意味着 RAG 流水线、稍后读、新闻监测等场景可以用一个接口替代自建正文提取与 PDF 处理链路。

- 🚀 **三个 API 同时提供**：平台提供 Article Extraction、PDF Extraction、URL Summaries 三类接口，且不按功能单独计费，每个套餐都包含全部三个 API。
- 🧩 **文章抽取返回结构**：POST /api/1/article 只需传入 url，无需编写 CSS 选择器；200 响应包含 title、author、date、content（文章正文的干净 HTML）、word_count、thumbnail、excerpt、url、domain 等字段。
- 📦 **PDF 与摘要端点**：PDF 解析支持上传文件或 GET /api/1/pdf?url={url}，可处理扫描件、多栏排版和表格；POST /api/1/summary 一次调用即可返回任意 URL 的摘要，适用于链接预览、社交卡片和压缩 LLM 上下文。
- 🧠 **解析引擎来源**：底层沿用驱动 Instapaper 的同一套解析引擎，自 2008 年起经过数十亿篇文章的打磨，官方强调对复杂网页边界情况已有现成处理。
- 💻 **SDK 与调用方式**：提供 Python 客户端 instaparser（InstaparserClient）和 Node 包 instaparser-api（new InstaparserClient({apiKey})），也可直接使用 curl 携带 Authorization: Bearer YOUR_API_KEY 与 Content-Type: application/json 调用。
- 📊 **按量定价档位**：Trial 为 $0 永久免费，含 1,000 credits/月、1 req/sec、社区支持且无超额；Beta $150/月含 100,000 credits、10 req/sec、超额 $0.0012；Live $500/月含 500,000 credits、25 req/sec、超额 $0.0011；Scale $900/月含 1,000,000 credits、50 req/sec、超额 $0.001。
- 🎯 **产品定位**：官方将其定位为 extraction 而非 scraping：不投入代理池和绕过机器人检测，而是专注理解页面内容，让用户无需自行维护抓取基础设施即可获得结构化数据。
- 🧪 **免注册试用**：首页支持直接粘贴任意 URL 查看 200 响应示例，无需注册；同时提供 blog.instapaper.com、eugenewei.com、seths.blog 等示例站点供体验。

### [PingSentinel — 网站可用性监控 | 时刻守护您的网站](https://pingsentinel.com/)

总结失败：模型未返回符合格式的摘要。

### [Ithy | 多AI深度研究](https://ithy.com/?utm_source=web_tools_weekly&utm_medium=newsletter&utm_campaign=creator_tests_202611&utm_content=web_tools_weekly_classified)

提供的正文仅要求比较不同模型的观点，并阅读各模型完整回答与合并答案，未包含具体产品、版本、功能或技术机制信息，因此无法形成实质性的技术周刊摘要。

- 🔍 **内容缺失**：正文只有比较观点和对照完整回答与合并答案的说明，没有可供总结的事件、发布或技术细节。

### [网站、SEO、安全与代码检查 | Zof Tools](https://zof.ai/tools)

Zof Tools 将 13 项聚焦检查整合为一个按范围付费的网站、代码与 API 诊断工具集，覆盖网站健康、SEO、安全、性能、可访问性、代码审计、OpenAPI、依赖供应链、PR 验证、用户旅程和 Agent Readiness 等场景；每项检查强调证据、覆盖范围、限制和可执行的下一步，不提供虚构评分，并提供有限免费预览、单次付费、月度订阅及网站组合包，便于用户先小范围验证再决定是否扩大检查。

- 🛠️ **工具集**：共 13 项检查：Website Health Check、SEO Audit、Website Security Check、Code Audit、Performance Check、Accessibility Check、API Check、GDPR & Cookie Behavior Check、OpenAPI Contract Check、Dependency & Supply Chain Check、Pull Request Verification、User Journey Check 和 Agent Readiness Check；每项给出发现证据与建议的下一步。
- 🧪 **免费预览**：每项工具提供有限免费预览，例如 Website Health Check/SEO Audit 最多 5 页、Code Audit 最多 100 个文件或 1 MB、API Check 1 个端点；完整运行需付费，页面称无需信用卡即可开始，报告默认私密。
- 📦 **单次与订阅**：单次运行价格从 $4.50 到 $24.50；月度计划从 $9.50/月到 $49.50/月，需登录账户并验证目标，每个计费周期含 4 次付费运行，未用次数不结转；Pull Request Verification 和 User Journey Check 不提供月度计划。
- 🏢 **网站组合包**：Website bundle 将网站健康、SEO、被动安全、性能和可访问性五项检查打包，面向一个已验证域名；单次 $24.50，或 $39.50/月含 4 次组合运行，每次按页面检查最多 100 页、性能检查最多 10 个 URL，代码和 API 检查需单独购买。
- 🔍 **执行与报告**：流程为选择检查、选择范围、查看证据；报告展示已执行检查、覆盖范围、限制和观察到的发现，付费报告提供可用下载格式。
- 🗓️ **报告保留**：报告在 30 天后过期，需自行下载保留；为有效付费额度或计划保留的目标可在报告过期后继续存在。
- 🛡️ **源码与凭据**：待处理源码归档加密且 24 小时内过期，处理完成后源码删除；保存的 API 凭据和仓库连接按保存的到期日失效，可在 Billing 中撤销。删除保存的扫描数据也会移除这些凭据和连接。
- 🧭 **账户关闭**：账户关闭会删除账户数据并登出所有会话；需先完成订阅和可支付结账，并在下次续费日前在账单门户取消续费；删除会放弃未使用的付费运行且不退款。会计、防欺诈、争议和支付对账所需的金额、产品和提供商交易引用保留，Stripe 记录不因账户删除而删除，本地收据和登录邮箱地址会移除。
- ⚠️ **使用限制**：检查仅限用户拥有或获授权的公开目标；Website Security Check 为被动首页检查，API Check 不发送写操作，GDPR & Cookie Behavior Check 仅做被动观察，Pull Request Verification 使用有界静态和语法检查，User Journey Check 仅在运营方批准的测试环境中选择有界表单和登录动作并使用加密测试凭据引用。
- 💬 **支持与隐私**：扫描或购买问题可发邮件至 support@zofai.com，并提供 scan ID 或收据编号，不要发送访问令牌、密码或私有源码归档；账户或隐私请求使用同一地址并注明 Tools 账户。

### [免费 IBAN 检查器：验证 92 个国家的任意 IBAN](https://ibanchecker.cash/)

ibanchecker.cash 上线了一套面向个人与企业开发者的 IBAN 校验平台，可在浏览器内实时完成格式、长度与 ISO 13616 MOD-97 校验码验证，并交叉比对覆盖 92 个国家、2407 家金融机构的目录，返回银行名称与 BIC。平台同时提供单笔校验、文档智能提取与 CSV 批量校验三种工具，以及返回 JSON 的 REST API；所有校验在浏览器或 API 内存中完成，不写入数据库或日志，基础设施部署于 Cloudflare 全球边缘网络并公开每五分钟采样的可用性数据。

- 🧩 **核心机制**：校验分三步：先按 SWIFT IBAN Registry 核对国家代码前缀、字符长度与结构模式；再用 ISO 13616 定义的 MOD-97-10 算法验证校验位；最后从有效 IBAN 中解析银行 BIC 与分行代码并匹配机构目录。
- 🌐 **覆盖范围**：支持 92 个国家的 IBAN 格式，机构目录包含 2407 家金融机构，来源以各国央行和 EPC 登记册为主，每个来源均在页面标注；SWIFT/BIC 目录覆盖 200 多个国家。
- 🛠️ **三种工具**：IBAN Validator 校验单个 IBAN 并返回格式、校验位与银行信息；Smart Extract 从文档或邮件中自动找出所有 IBAN；Bulk Checker 支持上传 CSV 或表格，数秒内校验数百条记录。
- 🛡️ **零数据留存**：网页端校验完全在用户浏览器内执行，IBAN 不会发送至服务器；通过 API 调用时在内存中校验后即丢弃，不写入数据库或日志，站点不使用跟踪 Cookie。
- ⚡ **边缘基础设施**：全部运行在 Cloudflare 全球边缘网络的 300 多个节点上，可用性每五分钟测量一次并公开发布。
- 💻 **开发者 API**：提供返回 JSON 的 REST API，响应包含 valid、iban、country、bank、bic、length 及 format/mod97/bank_found 三项检查结果；按月订阅、无年度绑定，Growth 计划起提供优先支持，Enterprise 提供 DPA 与定制合同。
- 🔄 **本地格式互转**：免费工具支持英国 Sort Code、德国 BLZ、法国 RIB、荷兰与比利时账号、土耳其及巴基斯坦、阿联酋账号转换为 IBAN，也可将 IBAN 反解为本地字段，另提供 37 国的测试 IBAN 生成器与 IBAN 二维码生成。
- 📊 **国家格式示例**：页面列出各国固定长度与示例：德国 DE 22 位、英国 GB 22 位、法国 FR 27 位、荷兰 NL 18 位、西班牙 ES 24 位、意大利 IT 27 位，示例 `DE89370400440532013000` 可解析为 Commerzbank Köln、BIC `COBADEFF`。

### [Mo 在 X 上：删除你的 AGENTS 文件中的所有内容，并替换为：始终以整洁、模块化、具备恰当架构和关注点分离的方式构建代码。绝不要仅仅因为我提出要求就硬塞一个功能。如果你找不到自然构建它的简单方法，并且你会建议重构…… / X](https://x.com/atmoio/status/2119525790723494116)

有开发者建议清空 `AGENTS` 文件并将全部内容替换为一条面向编码代理的强约束指令，要求以整洁、模块化和关注点分离的方式实现代码，拒绝为满足需求而生硬拼接功能，并在需要重构时提前停止并说明。其意义在于把“架构优先、必要时先重构”的工程规范前置到代理配置中，减少补丁式开发。

- 🧩 **AGENTS 配置**：建议删除 `AGENTS` 文件原有全部内容，只保留一条新的代理行为约束。
- 🛠️ **编码规范**：要求代码实现始终整洁、模块化，具备合理架构和关注点分离，避免因用户请求而直接外挂式添加功能。
- ⚠️ **重构前置**：如果无法自然、简单地实现功能，且需要先重构才能保持整体整洁，代理应提前停止工作并明确说明，而不是继续硬做。

### [Louis Lazaris (@LouisLazaris) / X](https://x.com/LouisLazaris)

提供的正文实际上是一个 X（Twitter）个人资料页，并不是文章正文；内容只包含 Louis Lazaris 的账号简介、外部链接、加入时间与关注数据，因此没有技术发布、版本更新或功能机制这类可供摘要的正文信息。

- 💡 **内容性质**：所给材料是个人资料页，只有简介、所在地、外部链接和关注数等界面信息；缺少可提炼的文章正文，无法按技术周刊的要求总结事件、变化与意义。
- 📚 **账号背景**：Louis Lazaris 自称 Chairman of the Bored，是两份技术周刊 webtoolsweekly.com 和 techproductivity.co 的创办人，个人站点为 impressivewebs.com，账号于 2009 年 5 月加入。
- 📊 **账号数据**：页面显示 5,486 位粉丝、717 个关注，并列出帖子、回复、转发、媒体等分区标签，这些属于界面元素，并非文章内容。

### [@louislazaris.com 在 Bluesky 上](https://bsky.app/profile/louislazaris.com)

这是一则前端开发者 Louis Lazaris 的 Bluesky 个人资料，集中展示其前端开发与 newsletter 策展身份，以及 Web Tools Weekly、Tech Productivity、VS Code Email 等项目链接和面向吉他爱好者的 YouTube 频道，同时提示使用 Bluesky 需启用 JavaScript，并给出 bsky.social 与 atproto.com 的了解更多入口。

- 💻 **身份定位**：Louis Lazaris 自述为前端开发者和 newsletter 策展人，个人站点为 `louislazaris.com`。
- 🔗 **项目与链接**：资料列出 `webtoolsweekly.com`、`techproductivity.co`、`vscode.email` 等项目链接，以及 YouTube 频道 `@tunejotter`。
- 🌐 **平台与标识**：页面属于 Bluesky，提示需启用 JavaScript 才能使用，并提供 `bsky.social`、`atproto.com` 供进一步了解；账号带 `did:plc:6if43vohxmohxuooa7bkkw5q` 标识。

### [向 Web Tools Weekly 提交工具](https://webtoolsweekly.com/submit)

这是一则面向前端开发者的工具征集公告：周刊开放推荐入口，邀请开发者通过 X 或 Bluesky 提交自建或已知的实用工具，供前端、编程与设计领域的读者参考。征集明确限定为工具类内容，文章与教程不予收录，与生产力相关的工具则已分流至另一份通讯 Tech Productivity。

- 💬 **提交渠道**：可通过 X 私信 @LouisLazaris（每周一、周二开放）或 Bluesky 聊天 @LouisLazaris.com 提交推荐。
- 📦 **征集范围**：接受库、框架、插件、脚本、Web 应用、桌面应用、移动应用、API / 服务、编辑器 / IDE，以及其他对 Web 开发者、程序员或设计师有用的工具。
- ⚠️ **不予收录**：文章和教程类内容不会被纳入；生产力相关工具已迁移至另一份通讯 Tech Productivity，同样通过上述渠道提交。

### [维基百科今日热门趋势 · WikiPop](https://wikipop.sowin.io/)

WikiPop 以维基百科浏览量为观察窗口，记录每日最受关注的条目；2026年11月24日位列榜首的是 `Miss Universe 2026`，因为波多黎各本土选手 Jennifer Barreto 夺冠，并成为首位已婚女性冠军和首位母亲冠军，该条目获得394,056次浏览。该站点同时展示了其不依赖数据库的静态更新方式：通过 `GitHub Actions` 每天抓取 `Wikimedia REST API` 数据，写入 `JSON`，生成静态页面，并部署到 `GitHub Pages`。

- 🎯 **热点条目**：2026年11月24日的高浏览条目为 `Miss Universe 2026`；第75届环球小姐赛事在波多黎各圣胡安的 José Miguel Agrelot Coliseum 举行，由 R'Bonney Gabriel、Mario Lopez、Zuri Hall 和 Dayanara Torres 主持，昨日浏览量为394,056。
- 🧩 **冠军意义**：Jennifer Barreto 在主场波多黎各夺冠，成为首位已婚女性冠军和首位母亲冠军；这位27岁的社会工作者也终结了波多黎各自 Zuleyka Rivera 夺冠以来的冠军荒。上届冠军 Fátima Bosch 为她加冕；上届赛事伴有操纵指控，组织者对此否认。
- 🔄 **WikiPop 机制**：WikiPop 每天选取最受欢迎的维基百科条目并保存归档，提供每日邮件和 RSS。同一文章若在最近30天内已成为头条，则不会再次被推荐。
- ⚙️ **无数据库架构**：站点使用扁平 `JSON` 文件、定时任务和静态 HTML。每天由 `GitHub Actions` 从 `Wikimedia REST API` 获取热门条目，写入 `JSON`，编译静态页面，再提交回仓库，最后由 `GitHub Pages` 提供服务。
- 🎨 **视觉设计**：设计方向借鉴 Lichtenstein 的 `Image Duplicator`，追求过去互联网的趣味感。背景圆点用纯 CSS 实现，并通过专为此制作的 `WikiPop's Background Adjuster` 调整到理想效果。
- 🛠️ **.xxx 过滤**：`.xxx` 常成为维基百科最热门页面。作者推测，这与用户搜索“xxx”后误点或出于好奇有关；由于它每天都靠前并且日常变化不大，站点将其过滤掉。
- ⚠️ **内容限制**：页面中的事件摘要标注为 AI 生成，可能包含错误。该摘要使用网络搜索和维基百科进行研究，由 Claude Sonnet 5.5 生成，并由另一位 Claude Sonnet 5.5 编辑审阅改写。

### [Web Tools Weekly | Web 开发者每周通讯](https://webtoolsweekly.com/)

Web Tools Weekly 是一份面向前端开发者的每周邮件技术通讯，主打新 Web 工具、库和 JS 技巧；页面显示已有 15,946 名订阅者，并提供邮箱订阅表单、隐私与数据追踪说明以及读者评价。

- 🗓️ **周刊定位**：每周发送一封邮件，面向前端开发者，用于跟踪新的 Web 工具和库。
- 📚 **内容重点**：每期包含 JS 技巧，读者评价称其能帮助发现可日常使用的新工具，并常被当作每周技术汇总阅读。
- 📈 **订阅规模与反馈**：页面显示 15,946 名订阅者，并展示多条来自开发者的推荐，强调其作为 Web 开发通讯的实用性和持续阅读价值。
- 🔑 **订阅与数据**：页面提供邮箱订阅表单，订阅即同意接收 Web Tools Weekly 邮件，并同意按 EmailOctopus 的隐私政策与条款存储和追踪数据；表单受 reCAPTCHA 保护。
