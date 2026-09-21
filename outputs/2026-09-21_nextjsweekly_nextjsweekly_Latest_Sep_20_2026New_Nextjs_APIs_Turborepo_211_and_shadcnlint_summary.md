### [React Bits - 适用于 React 的动画 UI 组件](https://reactbits.dev/c/micro)

**原文标题**: [React Bits - Animated UI Components For React](https://reactbits.dev/c/micro)

未提供可总结的文章内容，请补充文本后我将按模板生成摘要。
- 📄 当前输入为空，无法提取关键信息或生成摘要。
- ✍️ 请粘贴需要总结的文章正文。
- ✅ 收到内容后，我会输出简洁的中文要点列表，并为每条要点搭配合适的表情符号。

---

### [Arcjet - AI 智能体运行时安全](https://arcjet.com/?utm_source=njsw&utm_medium=cpc&utm_campaign=septlaunch)

**原文标题**: [Arcjet - AI agent runtime security](https://arcjet.com/?utm_source=njsw&utm_medium=cpc&utm_campaign=septlaunch)

overview summary
Arcjet 为 AI agent 提供运行时安全，把安全决策放到实际执行动作的代码边界，在工具、API、数据库调用前完成观察、拦截与审计。它覆盖提示注入、PII/DLP、工具越权、成本失控、机器人滥用，并通过 SDK、框架集成和远程策略支持工程与安全团队协作。

- 🛡️ **核心理念**：身份只说明“谁在请求”，无法判断“下一步会发生什么”；必须在每个动作步骤做决策。
- ⚠️ **风险放大**：单步看似安全，跨工作流可能变成未授权工具调用、数据外泄、成本爆炸或序列漂移。
- 🔍 **其他控制盲点**：提示扫描器看 token，网关看数据包，仪表盘看昨天；真正边界是发起调用的动作。
- 🧭 **三步机制**：Observe 观察动作与运行上下文；Enforce 在执行前返回允许/阻止/脱敏/待审；Audit 保存决策与证据。
- 🚫 **提示注入检测**：在用户输入、API 响应、工具输出进入模型前检测恶意指令。
- 🔧 **工具控制**：按身份、角色、路由和类型化输入限定 agent 可执行动作，DENY 时工具不会运行。
- 🕵️ **敏感信息与 DLP**：在进入模型上下文、日志或第三方工具前剥离姓名、地址、证件号、银行/卡号等 PII。
- 💸 **Token 与预算**：按用户、组织、agent 或运行设置 token 桶，防止失控循环耗尽预算。
- 🤖 **机器人与传统防护**：同一客户端和决策对象提供 Shield WAF、机器人检测、邮箱验证和注册保护。
- 🧩 **广泛集成**：支持 JavaScript、Python、Go，以及 Claude Code、Codex、Copilot、LangChain、OpenAI Agents、Vercel AI SDK 等 20 个 SDK/框架。
- 📜 **双轨策略**：工程团队用代码内规则做版本控制、测试和 dry run；安全团队用远程策略实时调整阈值。
- 🚀 **轻量部署**：不是控制平面、网关或代理；作为 import 加入现有代码，按服务逐步覆盖，无新增 sidecar/容器。
- 👁️ **看到动作而非仅流量**：能区分 $12,000 与 $12 的退款，适用于 coding agents、队列消费者、定时任务和工作流步骤。
- ✅ **合规与性能**：SOC 2 Type II；本地决策开销 <1ms，需云 API 时约 20-30ms；检测 600+ 机器人类型。
- 🧾 **审计证据**：记录决策、策略版本、执行者、输入和运行历史；敏感检查在进程内运行，数据不出本地。
- 🎯 **上手方式**：先对一条路由或工具处理器启用 dry run，观察决策后再阻止；运行 `npx skills add arcjet/skills` 或预约演示。

---

### [](https://www.reddit.com/r/nextjs/comments/1wcd0jj/quick_notes_on_what_actually_causes_nextjs/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1wcd0jj/quick_notes_on_what_actually_causes_nextjs/)

未检测到可总结的文本内容，请提供文章正文后我再生成中文摘要与要点。

- 📄 当前“Use the following content:”后为空，无法提取关键信息。
- 📝 收到内容后，我会先给出无标题概述，再列出核心要点。
- ✅ 每条要点将使用“-”符号，并搭配合适 emoji。

---

### [](https://github.com/vercel/next.js/pull/97393)

**原文标题**: [Add experimental parameter matching APIs by gnoff · Pull Request #97393 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/97393)

该 PR 是 vercel/next.js 的开放 PR #97393，目标是在 Cache Components 之上引入实验性参数匹配 API，用 `experimental.paramMatching` 控制未知参数请求走 404、阻塞生成、立即 fallback 还是动态渲染。当前实现、测试与性能统计均已有大量进展，但仍存在编码相关测试失败、构建失败和本地部署验证阻塞，尚未准备合并。

- 🧩 PR #97393 由 gnoff 提交，处于开放状态，目标分支为 `codex/closed-route-revalidation`，来源分支为 `jstory/unstable-matcher`，包含 90 个提交。
- 🎯 新增 `experimental.paramMatching`，需同时启用 `cacheComponents: true`；`generateStaticParams` 继续负责构建时具体预渲染，匹配配置决定未知参数值的处理策略。
- ⚙️ 支持按参数配置 `not-found`、`blocking`、`fallback`、`dynamic` 等模式；未配置参数会继承推断，未配置且无示例的尾部保持动态。
- 📦 示例中 `[lang]` 配置 `not-found`，`[top]` 配置 `blocking`，`[bottom]` 配置 `fallback`；新 `lang` 返回 404，新 `top` 阻塞生成，新 `bottom` 可立即返回 fallback UI。
- 🧪 支持异步 `experimental_generateParamMatching()`，无参并返回部分对象，可从外部配置加载策略，独立于 gSP，且同一模块在一次路由评估中共享结果。
- 🧷 类型支持普通 TypeScript 对象字面量，可选 `satisfies ParamMatching`；`ParamMatching<'lang' | 'top'>` 可约束键，生成类型与运行时校验会拒绝非法键和模式。
- 🧱 策略从 layout 向 page 合并，后代只替换自己声明的键；模块只能配置自身段或更上层参数，且合并结果必须遵循 `not-found → blocking → fallback → dynamic`。
- 🚫 显式 `not-found` 前的所有参数也必须显式 `not-found`，Next.js 不会静默关闭未配置前缀或改写继承意图；并行分支必须产出一致策略。
- 🖥️ 显式 `fallback` 必须对应非空 shell，不能静默变为 blocking；blocking 也需验证可达的有用 shell，`instant = false` 只跳过 shell 验证而非 hint 收集。
- 🛠️ 开发环境保留 shell 选择，并把显式 fallback 边界加入未知参数；生产环境将 closed-parameter 名称持久化到 renderer manifest metadata。
- 🚏 路由准入在查询 ISR 前检查；构建生成 URL 即使缓存过期或消失仍允许访问，其他 URL 按最具体 matcher 准入，缓存内容不授予渲染权限。
- 🔑 根 fallback 查询键需修正为 `nxtPlang` 而非逻辑名 `lang`；闭环前缀沿用现有 fallback-false adapter 合约，不引入新的 adapter/proxy 合约。
- 📤 初始阶段 `output: export` 要求每个参数显式 `not-found`，以避免静默改变匹配语义，并为未来客户端 fallback 留空间。
- 🔍 诊断信息只在同时启用 `experimental.paramMatching` 与 `NEXT_PRIVATE_DEBUG_PARAM_MATCHING=1` 时打印。
- 🧪 多项测试通过：98 个匹配单元测试、28 个生产构建合约测试、25 个开发路由用例、类型检查与 lint 等；fixture 覆盖闭环、缓存、根参数、并行路由组等。
- 🔴 仍有失败：百分号编码 URL 在生产运行中返回 500；`dynamicParams: false` 重验证与空缓存套件中 `next build` 失败；部分 param-matching-routing 与 root-params 用例也未通过。
- 📊 性能统计显示：`node_modules` 增加约 483 kB，Webpack 冷构建增加约 731 ms，缓存构建增加约 559 ms；Turbopack 缓存构建减少约 265 ms，整体被标记为 3 个回归、1 个改进。
- 🚧 实际 grouped-function 部署验证因缺少 `VERCEL_ADAPTER_TEST_TOKEN` 与 `VERCEL_ADAPTER_TEST_TEAM` 而在本地阻塞；PR 仍需至少一个 approving review。
- 🧱 该 PR 基于 #98944、#98891、#98950、#98964 等前置改动，前置可独立 review；诊断日志可单独移除，部分堆栈与 base 分支经历过多次调整。

---

### [我们如何](https://nextjs.org/blog/how-we-closed-1500-github-issues)

**原文标题**: [How we closed 1,500 GitHub issues in one month | Next.js](https://nextjs.org/blog/how-we-closed-1500-github-issues)

Next.js 团队借助 AI 代理在三周内关闭 1,462 个 GitHub issue，将公开积压从 2,244 降至 995，即使同期新增 218 个报告；核心是用只读研究代理审查旧 issue，再由维护者审核关闭，并持续自动化维护 backlog。

- 📈 背景：Next.js 每周平均收到 36 个新 issue，AI 编码代理让报告更详细，也大幅增加审查量。
- 🗂️ 积压峰值：2025 年 1 月达到 3,109 个未关闭 issue，到 2026 年 8 月 10 日仍有 2,244 个，旧 bug、重复项和不支持版本报告掩埋了新回归。
- ⏳ 曾用规则：2025 年 1 月引入 stale workflow，两年无活动后标记，后来改为 18 个月，但“不活跃”无法判断 issue 是否仍有价值。
- 🤖 AI 审查：基于 Vercel 开源代理框架 eve 构建 closability 研究代理，在 Vercel Sandbox 中运行 Next.js 仓库、Node.js、Playwright 和 Chromium。
- 🔍 调查流程：读取 GitHub 讨论、检查支持版本、搜索相关 issue/PR/commit/release/文档，必要时在报告版本、最新稳定版和 canary 上复现，并寻找反驳证据。
- 📊 结构化结果：代理返回关闭置信度、主要原因、摘要、证据和引用；置信度保持保守，仅复现失败不足以建议关闭。
- 🔒 安全限制：代理在沙箱外只读，不能评论、关闭 issue、推代码或部署，并忽略 issue 或仓库内容中的指令以防提示注入。
- 🧑💻 人工审核：结果进入 Close Queue，由维护者阅读证据后决定；关闭原因包括已修复 543 个、重复 278 个、预期行为 237 个、不再可复现 89 个、不支持或过时 66 个、其他 249 个。
- 🔁 纠错机制：GitHub Action 允许 14 天内请求重开；截至 2026 年 9 月 4 日，1,459 个保持关闭，仅 3 个被重开，保持关闭率 99.8%。
- 🧩 Maintainer Agent：closability 只是多个 eve 代理之一，其他代理负责复现、canary 验证、二分定位、端到端测试和准备修复；仪表盘和 Slack 用于审查与通知。
- 📅 持续运行：每周一 closability 会研究最多 100 个至少 30 天无活动的 issue；若 issue 有新活动，则丢弃已保存研究。
- 🚀 自动化扩展：近期开始让代理自动关闭最明确案例：置信度 80 以上由第二代理复核，若两者都建议关闭，则第二代理选择原因并写评论，再由 GitHub Action 关闭，每周最多 25 个；所有代码变更仍经人工审查。

---

### [Turborepo 2.11 | Turborepo](https://turborepo.dev/blog/2-11)

**原文标题**: [Turborepo 2.11 | Turborepo](https://turborepo.dev/blog/2-11)

Turborepo 2.11 版本发布，新增对 Rust、Python 和 Go 的原生支持（实验性），显著提升启动速度，并带来多项包管理器兼容性和部署优化功能，这是首个零已知漏洞的版本。

- 🚀 **多语言原生支持**：实验性支持 Rust、Python 和 Go，可将 Cargo、uv、go.work 工作区与 JavaScript 统一到同一任务图中，实现跨语言任务并行执行与依赖管理
- ⚡ **启动速度大幅提升**：Time to First Task 相比 2.9 最高快 4 倍，在 Vercel 后端大型 monorepo（1037 个包）中提速 45%，前端仓库（132 个包）提速 43%
- 📦 **devEngines.packageManager 支持**：遵循现代 Node.js 约定声明包管理器，未来将逐步弃用顶层 packageManager 字段
- 🔧 **新增包管理器支持**：正式支持 nub 和 aube 两款注重安全与速度的 JavaScript 包管理器，可复用现有锁文件轻松迁移
- ✂️ **生产环境裁剪**：新增 `--production` 标志，可在 `turbo prune` 时排除仅通过 devDependencies 引用的工作区包，优化 Docker 镜像体积
- 🎉 **首个零已知漏洞版本**：此版本修复了所有已知漏洞
- 🛠️ **升级便捷**：提供 pnpm、yarn、npm、bun、nub、aube 多种包管理器的自动化升级与新建仓库命令
- 📊 **丰富的更新内容**：包含 91 项功能、109 项性能优化、195 项修复、40 项文档更新和 28 项示例
- 👥 **社区协作成果**：由 Anthony 和 Tom 等核心团队及众多社区贡献者共同完成

---

### [](https://github.com/shadcn-ui/lint)

**原文标题**: [GitHub - shadcn-ui/lint: An agent-first linter for Tailwind design systems. Write design system rules that agents can verify. · GitHub](https://github.com/shadcn-ui/lint)

@shadcn/lint 是面向 AI 代理的 Tailwind 设计系统 linter，让团队用可验证规则约束 UI 生成；它兼容现有设计系统，支持 Tailwind v4、ESLint 和 Oxlint，不强制使用 shadcn/ui。当代理违反规则时，报错会说明问题并基于组件、变体和主题给出修复建议。

- 🎯 **核心定位**：为编写 UI 的代理而生，定义设计系统允许与禁止的用法，代理可运行 lint 检查自己的工作。
- 🧩 **兼容性**：适用于 Tailwind v4 项目，shadcn/ui 非必需；同时支持 ESLint 与 Oxlint。
- ⚙️ **工作方式**：团队配置规则，linter 报错不仅指出违规，还提示应改用哪些组件、变体、尺寸或主题值。
- 🧠 **对比 TypeScript**：TS 类型只能说明“不允许 padding”等限制，@shadcn/lint 能进一步告诉代理如何修复，例如使用 size、margin 或父级 gap。
- 🛠️ **可配置 contracts**：可为不同组件或组件部件设定独立规则，例如 Button 允许 `w-full`、`mt-*`，不允许 `p-4`、`hover:rounded-full`。
- 🧱 **组件部件级控制**：可让 CardTitle 修改排版但禁止改字体族/字重，让 CardContent 修改间距但禁止改排版。
- 💬 **自定义消息与占位符**：错误信息可包含 `{{component}}`、`{{sizes}}`、`{{file}}` 等占位符，帮助代理找到可用尺寸或主题文件。
- 📏 **内置规则**：包括 `no-restyle`、`no-raw-colors`、`no-arbitrary-values`、`no-inline-styles`、`no-unknown-classes`、`require-static-classes`。
- 🤖 **为代理优化**：错误会告诉代理“哪里坏了、该用什么、在哪里找”，建议来自项目现有组件、变体和主题。
- 📊 **测试效果**：在 150+ 任务运行中测试，几乎所有任务一轮修正内达到零违规；示例模型均将错误从数十项降到 0。
- 💰 **成本优势**：Claude 对照运行显示，借助 lint 反馈修复违规比仅靠规则节省 10% 到 48% 成本。
- 🧰 **为什么用 linter**：规则可编程，无需改组件 API；可对第三方组件应用规则；可跨项目共享设计系统配置。
- 🚀 **快速开始**：可让编码代理读取 `SETUP.md` 并安装配置，然后选择规则，定义设计系统允许的用法。
- 📦 **安装要求**：需要 Node.js 20.19+；Oxlint 需 1.80+，其 JS 插件 API 为 alpha；ESLint 需 9.30+。
- 🔧 **共享设置**：通过 `settings.shadcn` 配置 `ui`、`componentImports`、`ignoreImports`、`mergeFunctions`、`variantFunctions`、`note` 等。
- 🏢 **Monorepo 支持**：可为共享 UI 包设置导入前缀，并在组件目录覆盖规则，例如 `packages/ui/src/components/**`。
- 📄 **许可与文档**：项目采用 MIT license，提供 README、贡献指南、文档、规则选项与 evals 说明。

---

### [](https://github.com/LinuxCTRL/adinject-react)

**原文标题**: [GitHub - LinuxCTRL/adinject-react: Headless Ad Engine & In-Article / In-Feed Inserter for Next.js App Router & React 19 · GitHub](https://github.com/LinuxCTRL/adinject-react)

adinject-react 是一个面向 Next.js App Router 与 React 19 的零依赖广告引擎，它把"该在哪里、何时、如何安全地插入广告"这件事从广告网络手中接管过来。通过声明式组件在文章段落和内容流中自然植入广告位，实现零布局偏移、同意状态感知投放，并在广告被拦截或未填充时自动降级为联盟营销内容。项目还配套了可视化开发调试工具 adinject-devtools，并支持 Sanity Portable Text AST 直接注入、多广告网络适配以及 IAB 可见性追踪。

- 🎯 定位清晰：零运行时依赖，专注解决 React/Next.js 内容站点的广告位插入问题，与 AdSense/GAM 等只管"投放什么创意"的网络互补
- ⚡ 上手极简：`npm install adinject-react` 后，在根布局配置 `AdInjectProvider` 与 `ConsentProvider` 即可，广告位组件自动继承 client ID，无需重复传参
- 📰 文章内插广告：`<InArticleAds />` 可按段落间隔、起始偏移、最大数量规则自动注入，无需改动 CMS 原文
- 🧩 信息流插广告：`<AdInjectFeed />` 用 interval 与 startOffset 将广告卡片交织进网格、列表或无限滚动流中
- 🛡️ 零 CLS 设计：提前预留精确宽高比的占位框，避免创意加载时把正文内容往下推
- 🔁 联盟兜底引擎：广告被拦截或未填充时，自动替换为高转化的食谱/商品推荐卡片，避免空白区域
- ✅ 合规同意管理：集成 Google Consent Mode v2 与 IAB GPP，用户拒绝授权时切换为无 Cookie 的静态联盟卡片
- 🔒 幂等缓存：通过 idempotencyKey 记忆化，防止路由切换或 React StrictMode 下重复渲染广告位
- 🌐 网络无关适配器：内置 GAM（GPT）与 Ezoic 适配器，也可自行编写适配层
- 🔗 自动联盟链接：`injectHtmlAffiliateKeywords` 可将关键词转为带 FTC 披露的联盟链接，并设有密度上限防止堆砌
- 📊 可见性追踪：`useAdMetrics` 按 IAB 标准（≥50% 可见且 ≥1 秒）统计，并对无头爬虫做无效流量过滤
- 🧱 Sanity 深度集成：`injectPortableTextAds` 直接在 Portable Text AST 上操作，绕开正则解析与 DOM 抓取
- 🛠️ 配套 DevTools：可视化点击插广告、一键自动选最佳位置、AI 提示词生成、合规审计与 6 类行业创意样机
- 💻 兼容性广：覆盖 Next.js 14/15/16 与 React 18/19，自带严格 TypeScript 类型
- 🕵️ 隐私承诺：零遥测、100% 本地执行、拒绝授权后无追踪 Cookie
- 📚 API 完备：提供 10+ 组件、7 个转换器/钩子与多网络适配器，覆盖从插入、兜底到度量的完整链路

---

### [](https://github.com/vercel-labs/vgpu)

**原文标题**: [GitHub - vercel-labs/vgpu: Modular cross-runtime WebGPU library for shaders, 3D scenes, GPU tensors, neural networks, and math viz · GitHub](https://github.com/vercel-labs/vgpu)

vgpu 是 Vercel Labs 开源的跨运行时 WebGPU TypeScript 库，面向着色器、3D 场景、GPU 张量、神经网络和数学可视化，主打类型化 WGSL 导入、极简 GPU-first API，并让同一套代码运行在浏览器、无头 Node 和测试环境。

- 🧩 类型化 WGSL：`.wgsl` 文件可像 TypeScript 模块一样导入导出，反射机制自动保持绑定名、类型和布局正确，无需手写声明。
- ⚙️ 单一 `Gpu` 上下文：`init()` 返回一个句柄，`draw`、`effect`、`frame`、`surface`、`target` 等入口都以其为首参，避免隐藏全局状态。
- 📦 体积小：未使用声明在压缩前被裁剪，完整全屏特效约 25 KB gzip，且该预算由 CI 强制执行。
- 🌐 多运行时：同一公共 API 覆盖浏览器、Dawn 支持的无头 Node（`vgpu/node`）和用于测试/CI 的确定性 mock（`vgpu/mock`）。
- 🎞️ 显式帧控制：如 `frame(gpu, f => f.pass(target, effect))`，pass、clear、draw 都需显式调用，不依赖隐式场景图状态。
- 🤖 面向 Agent：文档、示例画廊和着色器校验可通过 CLI 运行，如 `npx vgpu docs`、`npx vgpu examples`、`npx vgpu check`。
- 🚀 快速开始：使用 `pnpm add vgpu` 和 `@webgpu/types`，通过 `init/surface/effect/clock/frameLoop` 即可在 canvas 上运行全屏特效。
- 🖥️ Node 快速开始：`vgpu/node` 支持 `target`、`draw`、`frame`，可读取像素并 `dispose()`；`vgpu/mock` 让测试无需真实 GPU。
- 📚 WGSL 标准库：`@vgpu/wgsl-std` 提供 hash、noise、color、sampling 等可复用声明，着色器也可导出自己的 `fn`、`struct` 或 `const`。
- 📖 文档与示例：完整文档位于 `vgpu.sh`，包含入门指南、性能手册和交互式示例，也可通过 CLI 离线访问。
- 🧰 Agent 资源：支持示例搜索/拉取、`npx skills add vercel-labs/vgpu`、`llms.txt`、OpenAPI 发现 API，以及 MCP 端点与本地 `npx vgpu mcp`。
- 🗂️ Monorepo 包：公开入口为 `vgpu`，其他包包括 `@vgpu/cli`、`@vgpu/core`、`@vgpu/wgsl`、`@vgpu/wgsl-std`、`@vgpu/adapter-node`、`@vgpu/adapter-mock`、`@vgpu/render`。
- 📈 仓库数据：约 2.2k Stars、113 Forks、40 Issues、13 PR，MIT 许可，含 1,596 次提交。

---

### [](https://avos.news/?utm_source=nextjs-weekly&utm_medium=newsletter)

**原文标题**: [Avos | Agentic News Reader: The Front Page of Your World](https://avos.news/?utm_source=nextjs-weekly&utm_medium=newsletter)

Avos 是一个代理式新闻平台：AI 在你睡觉时阅读你信任的来源，并为唯一读者“你”生成每天早上的一份私人简报，相当于你个人世界的头版。它支持自定义主题、公司、市场、区域、语言、语气、深度与发送时间，强调信号优先、隐私保护和多语言输出，并提供免费计划与付费高级功能。

- 📰 核心定位：AI 夜间读取可信来源，每早生成一份仅你阅读的私人版头版。
- 🧭 自定义关注：可设定主题、公司、市场、区域，覆盖你指定的领域。
- ✍️ 你当主编：语气、深度、日程由你决定，Avos 负责阅读与写作。
- 🌐 多源聚合：读取全球媒体与你的 RSS，将数百来源汇成一份晨间简报。
- 🔎 信号优先：AI 过滤并呈现真正影响你的动态，剔除噪音。
- 🗣️ 多语言支持：英语、德语、西班牙语、法语、波兰语、希腊语、印尼语等。
- 🔒 私密阅读：只为你一人生成，不出售数据；免费计划含广告。
- ⚙️ 制作流程：告诉 Avos 你的世界，AI 通宵抓取、过滤、去重，你只读一份简报。
- 🎛️ 规则灵活：可实时调整栏目、语气、来源、日程，发消息即可修改。
- 🤖 产品理解：可视为代理式 RSS 阅读器，把未读列表变成每日简报。
- 🧩 内容类型：新闻标题、文章摘要、金融数据、自定义 AI 版块均可独立配置。
- 💸 价格方案：免费计划可开始使用；付费解锁更多积分、无广告和高级定制。
- ⏰ 发送安排：每日、每周或自定义频率，可设置时间和时区。
- 🛡️ 数据处理：只收集交付简报所需信息，不卖个人数据，详情见隐私政策与条款。
- 📬 最终承诺：明天的简报，今天就能进入你的收件箱，可免费开始。

---

### [使用 StyleX 为 Linear 打造面向未来的样式](https://linear.app/now/styling-linear-for-the-future-stylex)

**原文标题**: [Styling Linear for the future with StyleX](https://linear.app/now/styling-linear-for-the-future-stylex)

Linear 将 React 应用从 styled-components 迁移到 StyleX，耗时远超预期，合并 1000+ PR，结合确定性工具、编码代理与人工判断，最终实现构建时生成样式、运行时零 CSS 注入，并建立更清晰的样式边界。

- 🎯 迁移原因：styled-components 过度灵活，使跨组件改样式成为常态，团队扩大和代理参与后更难维护。
- ⚡ 性能驱动：CSS-in-JS 在渲染时生成并注入样式，React 18 并发渲染后出现性能回退，且 styled-components 进入维护模式。
- ✅ 选择 StyleX：构建时生成样式，API 小，样式与组件同置，合并确定性，类型安全，并故意让外部重样式变难。
- ⚖️ 对比方案：vanilla-extract 有静态提取和类型安全，但 API 更碎片化，样式与组件分离不符合团队习惯。
- 🧱 迁移策略：先定义 StyleX 变量、常量和共享原语，再从叶子组件开始迁移，降低级联和共享组件风险。
- 🤖 自动化与代理：开发确定性 codemod `styled-components-to-stylex-codemod`，配合测试套件、在线 playground 和代理处理重复工作。
- 🧪 人工判断仍关键：代理常难验证复杂 hover、主题分支和细微布局差异，需人工测试；Fable 和 Sol 发布后能力提升。
- 📈 推动采用：开发者工具栏计数、组件高亮工具、迁移进度图，以及 PR 机器人阻止新增 styled-components。
- 🧹 清理遗留：自定义 lint 和仓库检查器禁止 styled-components 回归，并移除无用 className/style props。
- 🔌 组件样式契约：以 `sx` prop 作为标准接口，确保跨组件传递、合并顺序正确，且不静默丢弃样式。
- 🧩 组合与优先级：检查 className、style、JSX spread、sx、stylex.props()、mergedSx() 的覆盖问题，并限制易改变结果的简写。
- 🎨 设计一致性：用共享变量替代硬编码颜色、字体、阴影、动画、光标和细边框，并统一 hover/press/链接行为。
- 🛡️ 编译器与主题安全：防范 defineConsts 运算、未定义动态值、原始 CSS 变量、主题 token 误用和 portal 主题问题。
- 🚪 保留逃生口：全局选择器或第三方 DOM 用 CSS Modules；主题通过自定义 ThemeProvider 在运行时注入按边界作用域的 CSS 规则。
- 🌈 主题模型：Linear 主题由少量输入在 LCH 空间生成 100+ 颜色变量，选中行、焦点、菜单、浮层可重新生成嵌套主题。
- 🚀 收益：视图密集页面主线程 CPU 降低约 20–35%，中端机器约快 30%，导航期间注入 CSS 规则从数百降到零。
- 🧭 长期价值：样式边界更清晰、契约显式、优先级确定、工具强制执行，更适合日益由代理编写的代码库。

---

### [获取失败](https://blog.master.dev/new-things-you-should-know-about-html-here-in-mid-2026/)

**原文标题**: [Failed to retrieve](https://blog.master.dev/new-things-you-should-know-about-html-here-in-mid-2026/)

无法总结：获取内容失败，状态码 429。

---

### [](https://mensurdurakovic.com/motion-is-the-part-you-are-not-supposed-to-notice)

**原文标题**: [Motion is the part you are not supposed to notice — Mensur Duraković — Mensur Duraković](https://mensurdurakovic.com/motion-is-the-part-you-are-not-supposed-to-notice)

作者通过六项动效优化，将博客网站从功能正常提升到体验流畅，强调动效虽不被注意却至关重要，如同好肉需精心烹饪。

- 🎞️ 文章列表整体级联出现：使用 `staggerChildren` 让列表作为单一物体进入，而非逐行淡入，总耗时约 0.5 秒。
- 🔍 搜索对话框动画：用 `AnimatePresence` 实现进出动画，修复点击外部关闭和焦点管理问题。
- 📏 页头滚动收缩：基于滚动位置驱动 motion value 避免重渲染，引入迟滞规则防止抖动，且不引起布局变化。
- 📖 阅读进度条：2px 线条显示文章阅读进度，基于文章元素而非页面，无数字，平滑且诚实。
- 🖱️ 统一悬停效果：所有卡片使用相同 CSS 悬停规则，支持键盘 `:focus-visible`，移动端不粘滞。
- 🔄 页面过渡：使用 View Transitions API 实现图片跨页面过渡，注意 `router.push` 异步渲染问题。
- 💎 整体价值：这些改动并非功能特性，但共同塑造精致体验，如同好肉需好烹饪。

---

### [](https://www.nikhilsnayak.dev/blog/introducing-effective-rsc)

**原文标题**: [Introducing effective-rsc | Nikhil S](https://www.nikhilsnayak.dev/blog/introducing-effective-rsc)

effective-rsc 0.1.0 已发布，它是一个实验性全栈框架：用 React Server Components 作为应用模型，用 Effect 作为运行时，并结合 Rspack、Bun 与浏览器 Navigation API；文档站已上线，仓库还包含 Vercel 部署适配器和 hello-world 示例。

- 🚀 核心定位：React 负责 UI，Effect 负责运行时，目标是为服务、错误、并发、取消和资源生命周期提供统一后端模型。
- 🧩 技术组合：RSC 应用模型 + Effect 运行时 + Rspack 原生 RSC 集成 + Bun 服务器运行时 + Navigation API 客户端导航。
- 📄 页面即 Effect：路由参数由 Schema 解码，路由与应用服务在一个组合点闭合，Server Functions 复用同一运行时并保留 React 的 `"use server"` 协议。
- ⏸️ 在 Server Component 中可用 `yield*` 代替 `await`：服务依赖保留在类型里，由 application Layer 提供实现，工作绑定请求作用域；请求中止会中断 Effect 并清理资源。
- 🧭 客户端路由基于 Navigation API：目标页面首次 UI 提交即视为导航完成，不等完整 Flight 流，同时协调 URL、UI、Suspense、滚动、焦点和 View Transitions。
- 🌐 无 History API 兼容层：缺少 Navigation API 或 NavigationPrecommitController 时回退整页导航；水合、客户端组件和 Server Functions 仍可用，无 JS 时保留原生链接与表单行为。
- 🛠️ 快速开始：`bunx create-ersc-app my-effective-rsc-app`，再运行 `bun run dev`；包内含 `LLMS.md`，方便编码代理先阅读，也可让代理生成书签管理器示例。
- ☁️ 部署：可直接部署到 Bun，或使用 Vercel 适配器；文档站运行在 Vercel。
- ⚠️ 状态：实验性框架，使用 React Canary、Effect v4 RC、TypeScript 7、Rspack RSC 实现和现代浏览器 API；目前仅支持 Bun 作为服务器运行时。
- 🙏 致谢：基于 React、Effect、Bun、Rspack 生态；Rspack 与 `react-server-dom-rspack` 提供原生 RSC 编译和传输，特别感谢 Cong-Cong Pan，并受 rsc-html-stream、Waku、Twofold、Next.js、Vite RSC 等项目启发。
- 🔗 提供 GitHub、文档、完整示例、npm 等链接，并邀请试用反馈；另有构建 RSC 框架系列文章，涵盖 Server Components 与 Client Components。

---

