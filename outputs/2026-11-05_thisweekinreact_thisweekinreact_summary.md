### [调查和表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=this-week-in-react&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=this-week-in-react&utm_medium=email)

SurveyJS 是一套面向 JavaScript 应用的开源客户端调查与表单管理组件，支持自托管和完整数据所有权，帮助团队快速集成动态表单、拖拽式表单设计、数据仪表盘与 PDF 导出功能，避免数月定制开发，并满足隐私合规与无障碍要求。

- 🧩 **四大核心组件**：Form Library 渲染动态交互表单；Survey Creator 提供拖拽式表单生成器并输出 JSON Schema；Dashboard 用图表和表格可视化问卷结果；PDF Generator 将表单导出为可编辑或预填 PDF。
- 📝 **表单能力完整**：支持基础与高级题型、条件逻辑、校验、默认值、计算和自定义输入组件，可集成 React、Angular、Vue 3 或原生 JS。
- 🎨 **高度可定制与白标**：组件共享设计令牌和主题系统，支持内置/自定义主题及 Bootstrap、Material UI、shadcn/ui 主题适配器，便于匹配现有设计系统。
- ♿ **无障碍合规**：Form Library 和 Survey Creator 符合 WCAG、Section 508 和 ARIA 标准，支持键盘导航、屏幕阅读器和正确 ARIA 属性，并通过 Axe® 验证。
- 🔄 **离线数据收集**：调查、主题和回答可本地存储，离线创建、编辑和收集数据，恢复联网后自动同步。
- 🔐 **数据自主与合规**：可完全自托管，调查和回答存储在自己的基础设施中，无第三方介入，便于满足 HIPAA、FERPA、GDPR 等隐私与合规要求。
- ♾️ **无使用限制**：不限制表单数量、回答数量、管理员、受访者、提交量、文件上传或功能使用；所有数据存入自有数据库。
- 🧠 **AI 辅助**：可通过 API 集成 AI，实现自然语言生成表单、翻译和智能内容建议。
- 🏢 **行业适用广**：适用于保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利和银行等场景。
- 💳 **买断式许可**：Survey Creator、PDF Generator 和 Dashboard 采用一次性开发者许可，永久使用；含 12 个月免费维护，续订可选，无终端用户或实例额外许可费用。
- 🖥️ **仅聚焦前端**：SurveyJS 不存储、访问或跟踪数据，也不提供后端；用户可连接任意服务器、数据库和用户管理系统，自行实现审批流与认证。
- 🔑 **许可管理清晰**：许可持有者可在 License Manager 中分配开发者席位，被分配者可访问许可密钥和支持服务，但不能查看账单或管理团队。

---

### [为 Bootstrap、Material UI、shadcn/ui 自定义 SurveyJS 主题适配器](https://surveyjs.io/themes/theme-adapters?utm_source=this-week-in-react&utm_medium=email)

**原文标题**: [Customize SurveyJS Theme Adapters for Bootstrap, Material UI, shadcn/ui](https://surveyjs.io/themes/theme-adapters?utm_source=this-week-in-react&utm_medium=email)

SurveyJS 通过统一的 CSS 变量设计令牌架构，让表单库、Survey Creator、PDF Generator 和 Dashboard 的外观更易定制，并能更自然地融入现有应用。官方还提供面向 Bootstrap、Material UI、shadcn/ui 的主题适配器，以及面向自定义设计系统的 AI 辅助样式工作流。

- 🎨 **统一设计令牌**：SurveyJS 各库共享基于 CSS 变量的令牌架构，开发者可集中修改外观，而不必逐条调整 CSS 规则。
- 🧩 **主题与一致性**：支持设计令牌、主题、跨产品一致样式、便捷主题共享，符合现代设计系统方法。
- 🚀 **现成主题适配器**：为 Bootstrap、Material UI、shadcn/ui 提供 CSS 映射文件，减少定制工作量，让控件更贴近宿主框架风格。
- 🅱️ **Bootstrap 适配**：将 SurveyJS 设计令牌映射到 Bootstrap 样式，使控件在 Bootstrap 应用中更原生。
- 🎯 **Material UI 适配**：让 SurveyJS 遵循 MUI 的排版、间距、颜色和组件表面风格。
- ⚡ **shadcn/ui 适配**：对齐 shadcn/ui 的设计令牌与工具类样式模式。
- 💻 **源码与演示仓库**：可在 GitHub 查看所有适配器演示、检查配置并在本地运行示例。
- 🤖 **自定义应用方案**：若应用使用专有组件或独立设计系统，可结合 SurveyJS 样式技能与 MCP 服务器辅助 AI 编码代理。
- 🛠️ **AI 辅助流程**：安装样式技能、连接 MCP 服务器、让代理分析设计令牌并生成、验证所需 CSS 映射和覆盖。
- 📚 **更多支持**：提供 FAQ、联系渠道和快速开始入口。

---

### [前端测试——来自 Palantir 超过一百万行 TypeScript 的经验教训](https://www.meticulous.ai/blog/lessons-from-a-decade?utm_source=this_week_in_react&utm_medium=newsletter&utm_campaign=26q3_2&utm_term=react_link)

**原文标题**: [Testing Frontend — Lessons from over a million lines of TypeScript at Palantir](https://www.meticulous.ai/blog/lessons-from-a-decade?utm_source=this_week_in_react&utm_medium=newsletter&utm_campaign=26q3_2&utm_term=react_link)

概述：文章基于 Palantir 十余年前端测试经验，总结如何用测试显著提升工程速度，核心是降低测试维护成本、选对测试边界，并最终通过自动生成测试把维护成本降到接近零。

- 🧭 测试策略的关键不是“多写测试”，而是让测试容易编写、几乎无需维护，否则会拖慢团队。
- 🛠️ 维护成本决定可长期负担的测试数量；降低单测维护成本能指数级提升测试整体价值。
- 🎯 单元测试应测试“最小切割”的合适范围：覆盖足够复杂的功能，同时只跨越尽量少且稳定的 API。
- 🧩 测试边界应选择稳定的领域 API，避免依赖易变的内部实现细节，否则重构会导致测试频繁失效。
- ⚛️ 通常不建议写 Enzyme 或 React 组件测试；应把复杂逻辑抽成工具函数单独测试，减少对 DOM 结构的依赖。
- 🔗 可扩展集成测试应寻找应用中稳定的 API，把复杂度集中在输入值变化上，使新增测试只需添加数据文件。
- 📸 MapboxGL 通过 style spec JSON 与截图快照测试，实现“写一次、几乎不用改”的测试结构。
- ✅ 手工测试建议：为复杂逻辑写单元测试，为关键系统部分写少量集成测试，再用少量端到端测试做冒烟验证。
- 🚫 前端不应追求 100% 手工测试覆盖率，否则维护成本会超过收益。
- 🤖 Meticulous AI 通过记录开发与生产交互、理解执行代码路径，自动维护接近全覆盖的可视化快照测试，实现零开发者维护并减少 flaky 测试。

---

### [2026 年 11 月安全版本 | Next.js](https://nextjs.org/blog/november-2026-security-release)

**原文标题**: [November 2026 Security Release | Next.js](https://nextjs.org/blog/november-2026-security-release)

Next.js 发布 2026 年 11 月安全更新，修复 7 个与缓存隔离、响应处理、Cookie 泄露及图片优化相关的漏洞，建议尽快升级至 v16.4.5（Active LTS）或 v15.5.29（Maintenance LTS）。

- 🔐 官方发布安全补丁，修复多个中高危漏洞，应用应尽快更新 Next.js 依赖。
- 🚨 高危：同时使用 `unstable_cache` 与 `use cache` 时，可能跨租户泄露缓存内容，尤其影响按根参数区分租户的应用。
- 🧩 中危：嵌套 `use cache` 函数可能跨根参数泄露内容，导致租户、站点或语言专属内容被错误复用。
- 👤 中危：二进制参数可能产生相同缓存标识，造成跨用户缓存泄露或污染。
- 🏠 中危：自托管应用在特定配置下，共享页面 shell 可能被未认证请求污染，导致错误内容或持续 404。
- 🌐 中危：stale 压缩响应帧处理不当，在特定 HTTP/1.1 反向代理配置下可能导致跨客户端响应注入或泄露。
- 🍪 中危：Edge 路由通过 `NextResponse.cookies.set()` 设置 Cookie 时，可能经内部响应头暴露序列化 Cookie，包括 `HttpOnly` Cookie。
- 🖼️ 中危：图片优化中攻击者可控图片可能绕过 SVG 拒绝策略，增加 SVG 解析器资源耗尽或解码漏洞风险。
- 🛡️ 漏洞通过 Vercel 开源漏洞赏金计划协作处理，相关问题可联系 `security@vercel.com`。

---

### [](https://github.com/react/react/pull/36921)

**原文标题**: [[compiler] Preserve AST source offsets and declarator ranges by magic-akari · Pull Request #36921 · react/react · GitHub](https://github.com/react/react/pull/36921)

该 PR（#36921）已合并，核心目标是让 React Compiler 在 Rust 与 TypeScript 后端重建 AST 节点时保留原始源码偏移量和声明符范围，从而修复下游 source map 与 AST 消费方的定位错误。

- 🎯 问题根源：生成节点可能保留 `loc` 却丢失节点级 `start`/`end` 偏移；声明符范围在常量传播后可能反转，或漏掉类型转换初始化器的右括号。
- 🦀 Rust 后端：将原始 AST 偏移独立于 `loc.start.index`/`loc.end.index` 贯穿 lowering 与 codegen，并存为内部、不序列化的 HIR 元数据。
- 🧩 TypeScript 后端：在 codegen 时从原始 AST 恢复节点偏移。
- 📐 声明符范围：分别携带语句和声明符位置，输出原始声明符范围；源元数据缺失时保持缺失。
- 🧪 测试与 CI：snap 增加共享声明范围断言，补充缺失/偏移元数据的单测，并在 Rust 编译器 CI 中加入 `cargo test --workspace`。
- ✅ 验证结果：`cargo test` 59 项、Jest 3 项、`yarn snap`/`--rust` 各 1832 个 fixture、Babel AST 相关 1811/1812/1797 项通过；TS/Rust 产出一致。
- 🔬 回归覆盖：FBT 复数 fixture 端到端验证下游 Babel transform 能使用保留的原始偏移。
- 📈 体积与性能：ARM64 上 `SourceLocation` 32→48 字节、`Place` 40→56 字节；评审测得 x86_64 NAPI 编译中位数约慢 2.1%，作者接受该权衡。
- 🔗 关联影响：关联 Next.js #97392 与 Rspack #15350，解决 SWC/Rspack 场景下 React Compiler source map 映射丢失问题。
- 🚀 合并状态：已获批准，253 项检查通过，2026-10-30 由 javache 合并进 `react:main`。

---

### [](https://github.com/thejustinwalsh/react-concurrent-store/pull/27)

**原文标题**: [Add failing tests for concurrency by rickhanlonii · Pull Request #27 · thejustinwalsh/react-concurrent-store · GitHub](https://github.com/thejustinwalsh/react-concurrent-store/pull/27)

该内容是 GitHub 上 `thejustinwalsh/react-concurrent-store` 仓库的草稿 PR #27，由 `rickhanlonii` 提交，拟将 1 个提交从 `rickhanlonii:rh/tests` 合并到 `thejustinwalsh:main`，主题为“为并发添加失败测试”。作者使用 Claude 将 React 仓库中涉及 state 的测试迁移到该并发 store，并针对失败用例新增测试，以对比内置 React state 与该库的行为；部分失败属于预期情况，例如 fixups，但另一些看起来是真实的并发 bug。

- 🧪 PR #27 为草稿状态，标题是“Add failing tests for concurrency”，计划合并 1 个提交到主分支。
- 🤖 作者让 Claude 复刻 React 仓库中所有使用 state 的测试，并将其中的 state 替换为该并发 store。
- 🐞 对于失败的测试，作者让 Claude 在本仓库创建对应的失败测试，以展示内置 React state 与并发 store 的差异。
- ⚠️ 作者审查后认为，部分失败是预期内的，例如测试 fixups，但其他失败看起来是真实的并发 bug。
- 👍 相关评论获得了 4 个 🎉 和 1 个 👀 反应。
- 📌 当前没有评审、指派人员、标签、项目、里程碑或部署记录。

---

### [](https://github.com/vercel/next.js/pull/101050)

**原文标题**: [Add router.experimental_prepare() by acdlite · Pull Request #101050 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/101050)

Next.js 的 PR #101050 由 acdlite 提交并合并到 canary，核心是为 `useRouter()` 返回的路由器新增 `experimental_prepare(href)`，用于提前发起导航请求但不更新路由，并把响应写入 back/forward 导航共用的本地缓存；该功能由 `experimental.prepareNavigation` 控制。

- 🧩 **PR 状态**：该 PR 已合并进 `canary`，合并提交为 `5a5a4cd`，相关分支已删除。
- 🚀 **新增 API**：`experimental_prepare(href)` 会走与常规导航相同的步骤，包括动态请求，但不会立即更新路由器。
- 🔁 **返回句柄**：该 API 返回的句柄包含 `push()` 和 `replace()`；提交时会执行常规导航。
- ⏱️ **使用场景**：推荐在 `pointerdown` 时准备、在 `click` 时提交，以更早启动动态请求；未来可能内建到 `Link` 中。
- 🗄️ **缓存行为**：提交时可读取自准备开始以来写入的 bfcache 条目，不受过期时间限制；若请求仍在进行中，提交会复用它。
- ⚠️ **语义限制**：不提交则数据留在 bfcache，历史遍历可能看到较旧数据；准备的数据不会过期；刷新或 Server Action 会使准备的数据失效。
- 🚫 **提交限制**：一个句柄只能提交一次，后续调用无效，并且仅在开发环境给出警告；常规导航到同一路由不会复用准备的数据。
- 🔒 **实验开关**：该功能完全由 `experimental.prepareNavigation` 控制。
- ✅ **测试与审查**：测试通过，Vercel Agent 审查未发现问题，PR 通过自动 squash 合并，245/246 项检查通过。
- 📎 **关联变更**：PR #101051 调整了实验性功能的审查规则；Cloudflare vinext #4515 正在跟进支持该 API。

---

### [](https://github.com/vercel/next.js/pull/100850)

**原文标题**: [create-next-app: remove App Router prompt and always use App Router by timneutkens · Pull Request #100850 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/100850)

该 PR 已合并至 Next.js canary 分支，核心是让 `create-next-app` 不再询问是否使用 App Router，而是默认始终启用 App Router，仅保留显式退出选项以支持 Pages Router。

- 🚀 PR #100850 由 timneutkens 合并到 `vercel/next.js` 的 `canary` 分支，改动集中在 `create-next-app`。
- 🧭 移除“是否使用 App Router?”交互提示，新项目默认始终使用 App Router。
- 🎯 原因是 App Router 已是推荐默认，原提示只会带来误选 Pages Router 的机会，且保存的 `app: false` 偏好会静默生成 Pages Router 项目。
- ⚙️ 实现上，除非传入 `--no-app` 或 `--api`，否则设置 `opts.app = true`；从默认/偏好展示中移除 `app`，并忽略已保存的 `app` 偏好。
- 🧱 `--no-app` 仍作为显式退出方式，现有 Pages 模板及相关测试保持不变。
- ✅ 更新 `prompts.test.ts`：移除 customize 流程中的 App Router 提示；保存 `app: false` 时“复用上次设置”测试现在期望生成 `app/` 目录；`index.ts` 类型检查无新增错误，但 `create-next-app` e2e 未在本地运行。
- 📝 同步更新安装指南和 `create-next-app` CLI 参考文档，删除提示行及推荐默认摘要中的 App Router。
- 🔍 该 PR 获 kassens 批准，126 项检查通过后合并。

---

### [](https://github.com/vercel/next.js/pull/100130)

**原文标题**: [[experiment] support App Router route.go handlers by timneutkens · Pull Request #100130 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/100130)

该 PR #100130 由 timneutkens 提交并于 2026 年 11 月 3 日合并到 canary 分支，实验性地为 Next.js App Router 增加 Go 语言编写的 `route.go` 处理器支持。它建立在 #99980 的 `turbopack-go` 基础之上，允许 Go 的 `package main` 声明 `GET`、`POST` 等 HTTP 方法函数，由 Next.js 生成调度入口并在 Node.js 与受监督的 Go worker 之间完成运行时集成，同时为部署适配器提供 `runtime: 'go'` 的可执行输出。

- 🚀 **核心功能**：开启 `experimental.goRoutes: true` 并使用 Turbopack 时，`route.go` 中的 Go 函数可直接处理 HTTP 请求，自动支持 HEAD/OPTIONS 并校验处理器签名。
- 🧩 **分工明确**：Go 源码发现、声明分析、编译、持久缓存、目标构建与编译器生命周期由 #99980 的 `turbopack-go` 负责；本 PR 补充 Next.js 路由约定、HTTP 入口生成、原生端点元数据与运行时集成。
- 🖥️ **运行模式**：开发与自托管 `next start` 仍由 Node.js 掌管路由、重写和 `proxy.ts`；私有 Go worker 保留流式响应、头、Cookie、参数、取消及故障恢复能力，生产环境会重试启动失败。
- 📦 **部署适配**：适配器获得 `APP_ROUTE` 输出字段、`runtime: 'go'` 和可执行 `filePath`，`goTarget` 选项用于选择目标；复制出的基于 PORT 的服务器无需 Next.js 或 Go 工具链即可运行。
- ✅ **验证结果**：Rust clippy（`turbopack-go`、`next-api`、`next-napi-bindings`）通过；完整工作区/原生构建与 TypeScript 检查通过；Go 路由开发测试 18 项、生产测试 15 项通过，服务器追踪 6 项测试和 5 个快照通过。
- 🔍 **审查意见**：Vercel 机器人指出 `DevServer.ensurePage` 覆盖中 `definition` 为必选，而基类 `NextNodeServer.ensurePage` 为可选，在 `exactOptionalPropertyTypes: true` 下会触发 TS2416 错误。
- 🔗 **关联工作**：后续有 #100170（预编译 Go 前端与独立 worker）、#101009（分离图像滚动断言）等 PR；合并时 125 项检查全部通过。

---

### [React.lazy、Suspense 与隐藏的 300 毫秒启动延迟 • 标签页小部件](https://tabwidgets.com/blog/react-lazy-suspense-delay)

**原文标题**: [React.lazy, Suspense and the Hidden 300 ms Startup Delay • Tab Widgets](https://tabwidgets.com/blog/react-lazy-suspense-delay)

overview summary
文章复盘了 Tab Widgets 新标签页扩展的启动性能问题：真正瓶颈不是包体积，而是 React.lazy 首次渲染必挂起，叠加 Suspense 固定 300ms 的揭示节流。团队最终改为“不触发 Suspense 的代码门控”，让组件代码就绪后立即渲染，使首个组件内容从约 540ms 提前到约 298ms。

- 🧩 Tab Widgets 是 React 19 + Rspack 新标签页扩展，每个小组件独立成 chunk，并通过 React.lazy 与 Suspense 按需加载。
- 🐢 性能剖析发现：headless Chromium 中脚本约 100ms 已加载执行，但组件约 380ms 才出现，中间大量时间浏览器处于空闲。
- ⏱️ 根因是两件事叠加：lazy 组件首次渲染必定 suspend；Suspense 对挂起内容有全页共享的 300ms 揭示节流，导致占位符至少停留 300ms，组件还成批出现。
- 📉 缩小主包并未解决问题：移除模态框 re-export、移出 luxon 等改变文件分布或减少约 100KB，但对内容出现时间无可测影响；扩展从本地磁盘加载，字节不是关键。
- 🛠️ 第一版修复利用 React 私有字段 _init/_payload 预加载 lazy 组件，并在首屏前最多等待 100ms；headless 下从约 380ms 降至约 95ms，但慢机器上超时组件可能更晚。
- ✅ 最终方案不再让组件因自身代码 suspend：用 useLazyReady 判断代码是否就绪，未就绪时渲染普通占位并启动预加载，完成后通过 state 更新替换；保留 Suspense 和错误边界处理失败。
- 🔐 同一思路也用于权限检查等 suspending query，避免仅几毫秒的检查被 300ms 节流拖慢。
- 📊 Windows Chrome 实测（4 次冷启动、20 组件仪表盘）：首个组件内容 540ms→298ms，85% 内容 540ms→336ms；全部内容 540ms→544ms，因 Weather 和 Word of the Day 仍在数据请求时 suspend。
- 🧪 若不碰 React 私有字段，可用自建模块缓存和 useLoadedComponent 实现“预加载 + 占位 + 状态替换”，并自行处理失败重试。
- 💡 经验：衡量“何时出现”而非只看包大小；寻找主线程空闲；理解框架的有意节流；实验室定位后要在真实设备确认。

---

### [异步 React 与渐进式服务端操作 | ebey.dev](https://ebey.dev/blog/3myyseusgd22h)

**原文标题**: [Async React & Progressive Server Actions | ebey.dev](https://ebey.dev/blog/3myyseusgd22h)

文章讨论 React 异步 API 与渐进式 Server Actions 如何让表单在 JavaScript 加载前也能提交，并在加载后获得更流畅的增强体验。核心观点是：只要 Server Action 始终直接作为 `<form action>`，表单就能在无 JavaScript 时工作；若需要乐观更新等客户端增强，则需借助 `useHydrated` 在 hydration 后条件启用。

- 🧩 React Router 推动了原生 `<form>`、`useNavigation()`、`useFetcher()` 等渐进增强模式，理念是“JavaScript 前可用，JavaScript 后惊艳”。
- ⚙️ `"use server"` 让 React 组件模型直接支持服务端表单动作，本质上是在告诉 `<form>` 如何发起真实 POST 请求。
- ⏳ `useTransition` 可用于处理异步工作与 pending 状态，但样板代码较多；`useActionState` 简化了表单 action、状态和 loading 管理，可理解为“异步版 useReducer”。
- ✨ `useOptimistic` 用于在异步操作进行期间乐观更新 UI，其状态只存在于 transition 生命周期内。
- 🖥️ `useActionState` 与 Server Action 结合后，表单在 JavaScript 加载前仍可提交，同时能提供 pending 反馈。
- ⚠️ 如果把 Server Action 包在客户端函数中再传给 `useActionState`，hydration 后可用，但表单在 JavaScript 前将不再知道如何提交。
- 🚦 乐观 Server Action 若把客户端定义的 `enhancedAction` 传给 `<form>`，同样会破坏无 JavaScript 提交能力。
- 🪝 解决方案是使用 `useHydrated`，在 hydration 前传原始 `action`，hydration 后再传增强后的 action，从而兼顾渐进增强与乐观 UI。
- ✅ 关键规则：Server Action 必须始终作为 `<form action>` 的最终 action；这样 React 才能统一支持“JavaScript 前可用、之后增强”的异步体验。

---

### [理解 React 内部原理](https://www.alexandretrotel.org/articles/understanding-react-internals)

**原文标题**: [Understanding React internals](https://www.alexandretrotel.org/articles/understanding-react-internals)

本文深入探讨 React 内部机制，强调 React 的本质是调度器而非仅 Hooks，并涵盖服务端渲染、水合、渲染阶段、提交阶段、异步 React、lanes 及组件序列化等通常隐藏的细节，鼓励通过阅读源码真正掌握 React。

- 🧩 大多数人通过 Hooks 学习 React，但 Hooks 只是表面，应暂时放下。
- ⚙️ React 底层是一个调度器，决定渲染什么、何时渲染以及什么可以等待。
- 🌐 文章将深入异步 React、lanes、服务端与客户端之间的组件序列化、水合等隐藏部分。
- 📖 作者基于日常使用和阅读 React 源码的经验总结，建议直接阅读源码以理解原理。
- 🎯 读完后应能理解 React 到掌握程度，知道每个 Hook 何时使用以及为什么。
- 🧠 这会改变使用 React 的方式，尤其是服务端与客户端之间以及 React 与浏览器交互的心智模型。

---

### [可写派生状态：停止同步状态 | 趣味编程](https://playfulprogramming.com/posts/writable-derived-state/)

**原文标题**: [
	Writable Derived State: Stop Synchronizing State | Playful Programming
](https://playfulprogramming.com/posts/writable-derived-state/)

文章指出，常见的“把服务端默认值同步到本地状态”模式会在用户刷新或重新访问标签页时覆盖用户修改；更合理的做法是采用“可写派生状态”，只在用户尚未编辑时使用服务端数据，用户编辑后以本地覆盖值为准，并在保存成功后重新获取服务端数据再清除本地覆盖，从而避免不必要的状态同步与 `useEffect`。

- 🧩 核心问题：应用常需要“服务端提供默认值，但允许用户覆盖默认值”，直接同步服务端状态会导致服务端更新总是覆盖用户数据。
- ⚠️ 典型 bug：使用 `useEffect` 将 `serverState` 复制到 `todos`，初次可用，但刷新或重新访问页面后会重置用户修改。
- 💡 根因认知：所谓“从服务端同步客户端数据”，更准确的理解应是“当客户端数据缺失时使用服务端数据”。
- 🔁 解决方案：只保存用户覆盖值 `userTodos`，通过 `const todos = userTodos ?? serverState.payload` 派生最终数据。
- ⚛️ 额外收益：该模式可移除不必要的 `useEffect`，符合 React 官方“You Might Not Need an Effect”的建议。
- 🧪 TanStack Query 同样适用：保存成功后 `refetch()`，成功后将本地覆盖值设为 `null`，让服务端数据重新成为来源。
- ✅ 最终效果：状态管理更可预测、更高效，组件更简单，也减少客户端与服务端状态同步带来的复杂性。

---

### [如何为 OAuth 和 MCP 构建一个良好的同意屏幕 | PropelAuth](https://www.propelauth.com/post/good-consent-screen-for-oauth-and-mcp?utm_source=twir&utm_campaign=nov4&utm_medium=newsletter)

**原文标题**: [How to Build a Good Consent Screen for OAuth and MCP | PropelAuth](https://www.propelauth.com/post/good-consent-screen-for-oauth-and-mcp?utm_source=twir&utm_campaign=nov4&utm_medium=newsletter)

OAuth/MCP 同意屏看似只是“应用名 + 权限列表 + 两个按钮”，实际要帮用户判断四件事：授权给哪个账号、是谁在请求、对方能做什么、授权结果会跳到哪里。随着 MCP 引入 DCR/CIMD，客户端可能未经人工注册就发起请求，因此同意屏必须更清晰地展示身份、权限和风险信号。

- 👤 明确展示当前登录账号的邮箱，并提供退出/切换账号入口，避免用户授权给错误账号。
- ✅ 将请求的 scope 渲染为带通俗说明的复选框；可选权限可取消，必需权限保持勾选且禁用，不允许授予的权限也要可见并标注，不能静默隐藏。
- 🔒 同意屏上的勾选本身不生效：签发的 token 只能包含用户勾选的 scope，MCP 服务器还必须在每次工具调用时校验 scope。
- 🔗 展示授权后返回的重定向 URI，并优先显示域名；用户可据此判断是否与预期目的地一致。
- 💻 对 localhost、127.0.0.1 或自定义 scheme 等本地重定向单独提示：这是用户电脑上的应用，只有确认是自己刚刚发起的连接才应批准。
- 🏷️ 在 CIMD 场景下，client_id 是 URL，域名才是身份，client_name 只是客户端自述；未知发布者应使用“一个自称某某的应用”这类措辞，而不是直接信任名称。
- 🚨 重点识别名称与域名不一致、仿冒域名、重定向到无关域名等风险；例如 claude-code.ai 不等于 claude.ai，claude.ai.something.example 的可注册域名其实是 something.example。
- 🖼️ 不要为未识别发布者展示 logo，因为 logo 是强信任信号，可能被请求方滥用。
- 🔁 客户端后续申请更多权限或权限含义变化时，应再次弹出同意屏并标出新增/变化内容，不能因曾经授权过就静默扩展。
- 🏢 B2B 产品还需让用户选择授权给哪个组织，并按用户在该组织中的角色决定可授予的 scope。
- 📋 核心清单：显示账号、权限可勾选、展示重定向、本地重定向特殊提示、域名即身份、未知发布者不显示 logo、增权重新征得同意、B2B 明确组织与角色限制。

---

### [发布 v2.14.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.14.0)

**原文标题**: [Release v2.14.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.14.0)

Redux Toolkit v2.14.0 已发布，重点提升 dispatch 路径与 RTK Query 类型检查性能、缩小 esbuild 下 `createSlice` 包体积、新增 RTK 自有 `Draft`/`Patch` 类型与多项 API，并修复大量 RTK Query 生命周期、轮询、upsert、定时器、Hooks 和 `fetchBaseQuery` 问题；同时官方公布了 Redux Toolkit 3.0 路线图。

- 🚀 这是功能版本，显著加速 dispatch 路径，并提升 RTK Query 的 `Api` 类型检查速度。
- ⚡ dispatch 优化包括：`createAction.match` 先比较 `action.type`，`createReducer` 不再每次分配数组，listener middleware 使用快照并跳过无关 action。
- 📈 基准中，200 个 listener 处理无关 action 从 108K 提升到 5.34M ops/sec；RTKQ 无关 action 从 352K 提升到 468K ops/sec。
- 📦 esbuild 现在可将 `createAsyncThunk` 从 `createSlice` 中 tree-shake 掉，仅导入 `createSlice` 的包约小 1 kB（brotli）。
- 🧠 RTK Query `Api` 类型检查优化后，测试应用类型实例化减少 22%，检查时间在 TS 6 下降约 25%，TS 7 原生预览下降约 18%。
- 🧩 新增 RTK 自有 `Draft`、`WritableDraft`、`Patch` 类型，生成的声明不再引用 Immer；新增 `ApiRootState`、listener action 类型和 Hook result 类型，`RootState` 已弃用并将在 3.0 移除。
- 🗃️ Entity adapter 新增 `removeMany({ where })` 和 `selectByIds`，并提升 `removeMany` 性能。
- 🔍 RTK Query 新增 `selectEntriesForEndpoint`、`selectAllQueryEntries` 缓存条目选择器，以及用于 DevTools 的 `createApiActionSanitizer`。
- 🐛 修复大量 RTK Query 问题，涉及生命周期、轮询、upsert、定时器、多 store、Hooks、`skipToken`、`NaN` 参数、`fixedCacheKey`、超时与解析错误等。
- 🛠️ 其他修复包括 listener `take`/`condition`/`delay` 定时器泄漏、`autoBatchEnhancer` raf fallback 报错、循环引用序列化检查，以及将 `@types/react` 改为可选 peer 依赖。
- 🧭 官方同时公布 Redux Toolkit 3.0 路线图，v2.14.0 的改进为后续 2.x 功能和 3.0 破坏性变更铺路，并邀请社区反馈 RTK Query 用法与 3.0 计划。

---

### [Redux Toolkit v2.x 与 v3.0 路线图 · reduxjs/redux-toolkit · 讨论 #5536 · GitHub](https://github.com/reduxjs/redux-toolkit/discussions/5536)

**原文标题**: [Redux Toolkit v2.x and v3.0 roadmap · reduxjs/redux-toolkit · Discussion #5536 · GitHub](https://github.com/reduxjs/redux-toolkit/discussions/5536)

Redux Toolkit 维护者 markerikson 于 2026 年 11 月 1 日公布 RTK 2.x 与 3.0 路线图：2.x 将先清理内部实现、修复问题并逐步加入新特性；3.0 预计约 6-8 个月后发布，核心方向是仅提供 ESM、改进 RTK Query 和 `createSlice` 的定制能力，并通过适度破坏性变更提升可用性与开发体验，同时配套迁移指南和 codemod。

- 🕰️ 历史回顾：Redux 于 2015 年发布，早期因冗长模式被贴上“样板代码”标签；2019 年 RTK 作为官方标准库推出，2021 年 RTK Query 发布，2023 年各包升级以支持 CJS/ESM 双格式。
- 🎯 3.0 定位：变更规模类似 React 18→19，而非 Angular 1→2；多数代码无需改动，破坏性变更需以更好的 DX 和可用性为目标。
- 📦 打包策略：RTK 3.0 将仅发布 ESM，简化构建发布流程、减少安装体积；所有包将同步发布大版本。
- 🧱 RTK Query 重构：调整 `createApi` 类型与定义，支持先创建 core API 再在运行时添加 React 支持；`query` 字段拟改名为 `request`；`state.api.queries` 将改为按 endpoint 嵌套，提升更新性能，但会破坏直接访问该内部结构的代码。
- 🛠️ `createSlice` 与不可变性：重构定制方式，改善未使用 thunk 时的 tree shaking，并支持添加自定义 creator；探索将 Immer 替换为可插拔的不可变更新库，但默认仍推荐 Immer。
- 🔤 命名调整：`extraReducers` 计划重命名为 `respondTo`，2.17 先提供别名并弃用，3.0 移除并报错。
- ⚙️ Redux 核心与 thunk：计划将 thunk 中间件移入 `redux` 核心包，弃用 `redux-thunk`；可能把 `reduceReducers` 加入核心。
- 🧪 2.x 路线：2.14 聚焦内部正确性与性能；2.15 重写 RTKQ 请求行为与中间件；2.16 改进缓存条目写入/更新语义；2.17 加入水合/脱水、Suspense 预备、按 endpoint 的 baseQuery 等。
- ⚠️ 其他破坏性变更：RTKQ 现有 module 系统将改变，`unstable_sideEffectsInRender` 可能移除，最低 TypeScript 版本提升至 TS6；将提供 codemod、lint 规则和迁移指南。
- 🗓️ 时间表：2.x 工作立即开始，3.0 粗略预计 6-8 个月内发布，但坚持“准备好再发”；近期会建 3.0 集成分支供试用和反馈。
- 💬 社区反馈：通过 #5483 跟踪路线图，#5534 收集 RTK Query 使用反馈，#5535 征集 3.0 破坏性变更意见；欢迎社区参与，但使用 AI 辅助贡献需确保理解并对结果负责。

---

### [发布 · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases)

**原文标题**: [Releases · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases)

该版本系列（4.14.8–4.18.1）主要增强了 `Workspace` 标签页布局能力，新增整组标签页拖拽、可折叠标签页、空闲空间 API、模型规范化与 RTL 支持，同时修复了尺寸计算、拖拽交互、多窗口、打包和类型依赖等问题。

- 🧩 **4.18.1**：修复标签列表被压缩至 0px 后空闲空间不继续更新，以及 RTL 布局下拖拽、方向键、边缘投放和溢出属性异常。
- 🧰 **4.18.0**：新增 `normalizeWorkspaceModel`、标签列表空闲空间 API、`maxWidth/maxHeight` 限制，并改进折叠/最小尺寸处理和拖拽预览。
- 🖱️ **4.17.0**：支持拖拽整个 tabset，新增可折叠 tabset、`collapse/expand` API、最近标签选择行为和 tabset 拖拽预览。
- 🗂️ **4.16.0**：新增 `Workspace` 组件，支持标签页在 tabset 间/内部拖拽、边缘分屏、调整大小和最大化，并提供渲染、样式和状态 hooks。
- 🎨 **4.16.1**：为 split 增加 `classNames/styles` 支持；修复分隔条拖拽中断、元素 ID 冲突及边缘点击优先级问题。
- 📦 **4.15.3**：通过 `sideEffects: false` 和 pure 注解改善 tree-shaking，避免未使用组件被打包。
- 🪟 **4.15.2**：修复 `vh/vw/em` 尺寸在多窗口场景下错误使用全局 `window` 的问题。
- 🧾 **4.15.1**：将 `@types/react` 声明为可选 peer dependency，改善严格包管理器下的 TypeScript 类型解析。
- 🪝 **4.15.0**：新增 `useParentGroup/useParentPanel/useParentGrid` hooks，并优化 `resize/collapse/expand` 的空间分配与恢复逻辑。
- 🛠️ **4.14.8**：修复 `pointermove` 目标被移除导致的 stacking order 错误，以及 `ResizeObserver` 前调用布局方法时的尺寸校验问题。

---

### [发布 11.1.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.1.0)

**原文标题**: [Release 11.1.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.1.0)

Preact 11.1.0 已发布，主要新增对 React Compiler 的兼容运行时支持，并包含 VNode 识别、布局副作用错误隔离、SVG 样式值处理及类型定义方面的修复与改进；同时提示新版 VNode 标记对相关生态包有最低版本要求。

- 🚀 新增 `preact/compat/compiler-runtime`，用于支持通过 React Compiler 编译的应用（#5323）
- 🔒 使用共享 symbol 标记强化 VNode 识别（#5335）
- 🧩 隔离 layout-effect 错误至抛出错误的组件，避免影响无关 effects 和生命周期回调（#5321）
- 🎨 修复 compat 中无单位 SVG paint 与 aspect-ratio 值被错误追加 `px` 的问题（#5233）
- 🧾 类型定义允许在所有合法 input 类型上使用 `list` 属性（#5331）
- ⚠️ 新 VNode 标记要求使用 `@preact/signals` 2.11.4+ 和 `preact-render-to-string` 6.8.2+
- 👏 贡献者包括 JoviDeCroock、dylanpulver 和 playlikeboy

---

### [发布 @tanstack/redact@0.3.0 · TanStack/redact · GitHub](https://github.com/TanStack/redact/releases/tag/%40tanstack%2Fredact%400.3.0)

**原文标题**: [Release @tanstack/redact@0.3.0 · TanStack/redact · GitHub](https://github.com/TanStack/redact/releases/tag/%40tanstack%2Fredact%400.3.0)

本次发布为 TanStack redact 的 0.3.0 版本，属于小版本更新，重点增加了面向浏览器 SPA 的 Webpack 与 Rspack 插件，并完善了 Rsbuild 配置指南及相关构建适配能力。

- 📦 发布版本：@tanstack/redact@0.3.0
- 🧩 新增浏览器 SPA 插件：支持 Webpack 和 Rspack，并提供 Rsbuild 设置指南
- 🔄 共享 Vite 功能选择与包解析逻辑
- 📌 保留精确别名与包归属信息
- ⚛️ 按需将所选运行时适配到 React 18
- 🔗 相关变更合入 PR #143
- 🚀 由 github-actions 发布，包含 8 个提交，发布时间为 11 月 3 日 18:37
- 📁 发布资源共 3 个

---

### [发布 · inertiajs/inertia · GitHub](https://github.com/inertiajs/inertia/releases)

**原文标题**: [Releases · inertiajs/inertia · GitHub](https://github.com/inertiajs/inertia/releases)

该页面汇总了 Inertia.js 在 GitHub 上的版本发布记录，涵盖 3.x 与 2.x 分支的最新版本、主要功能更新、错误修复、依赖升级和社区贡献者信息；整体显示 3.x 为当前迭代重点，2.x 仍持续维护。

- 🚀 最新版本为 v3.11.0，由 pascalbaljet 于 11 月 2 日发布，新增 Live props 支持并升级依赖。
- 🧩 v3.10.0 集中修复多项问题，包括 useHttp 的 FormData 索引格式、React 类型可选依赖、Windows SSR 样式恢复、SSR 异常请求处理和相对 URL 解析。
- 🔄 v3.10.0 还新增 QUERY HTTP 方法支持，修复 InfiniteScroll 滚动位置、异步请求取消、预取缓存中断和历史导航响应过期等问题。
- 🔐 v3.9.1 修复 XSRF Token 仅发送至同源 URL，并为每条加密历史记录使用唯一 IV，提升安全性。
- 🧠 v3.9.0 改进队列任务处理、历史恢复与页面更新冲突、navigate 事件类型、QuotaExceededError 处理、Vite sourcemap 保留和后台轮询暂停选项。
- 🛠️ v3.8.0 修复 SSR 多字节 UTF-8 解析、Axios 未安装时的核心类型、资源版本比较、乐观更新回退、SSR CSS 链接和 BigInt 支持，并新增 WhenMounted 组件。
- 📦 v3.7.1 与 v3.7.0 涉及 SSR CSS 链接修复与回滚、视图切换中断处理、预取计时器清理、初始页面 JSON 转义，以及 Form 组件的 cancel、cancelOnUnmount 和 usePoll 状态返回。
- 🧪 v3.6.1 改进 Svelte 异步渲染、内置 HTTP 客户端原始请求体支持，并修复 PHP 8.5 PDO 弃用提示。
- 🔧 v2.3.29 与 v2.3.28 继续维护 2.x，包含预取缓存清理、加密历史唯一 IV、React back_forward 页面恢复、Form getFormData 防护及依赖升级。
- 👥 发布记录显示大量社区贡献者参与，dependabot 频繁更新 GitHub Actions 依赖，版本列表共约 13–14 页。

---

### [](https://skullet.lochie.me/)

**原文标题**: [Skullet 🦴 Smart skeleton states](https://skullet.lochie.me/)

文章讨论“为等待而设计”，强调加载状态是用户最先看到的内容，并在慢速网络下成为用户最常看到的部分。  
- ⏳ 主题聚焦于等待体验与加载状态的设计。  
- 👀 加载状态是用户进入页面后最先看到的内容。  
- 🐢 在慢速连接环境下，加载状态是用户最常看到的部分。  
- ✍️ 作者为 John Doe，阅读时长约 4 分钟。

---

### [](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect/releases/tag/v1.1.0)

**原文标题**: [Release v1.1.0 · nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect · GitHub](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect/releases/tag/v1.1.0)

该内容介绍的是 `eslint-plugin-react-you-might-not-need-an-effect` 仓库发布的 `v1.1.0` 最新版本，发布日期为 2026-11-01，由 github-actions 发布，提交号为 `2d0d7ef`，并带有 GitHub 验证签名。该版本包含一项新功能，以及三项配置与提示信息相关的修复。

- 🚀 发布版本：`v1.1.0`，为当前最新版本
- 📅 发布时间：2026-11-01 15:38
- ✅ 提交信息：`2d0d7ef`，提交已通过 GitHub 验证签名
- ✨ 新功能：支持重命名后的 React Hook 导入
- 🛠️ 修复：为 flat configs 命名
- 🛠️ 修复：停止向 lint 集合中添加文件
- 🛠️ 修复：移除 `no-pass-data-to-parent` 消息中的重复引号
- 📦 附件：包含 2 个 Assets

---

### [发行版 · remorses/safe-mdx · GitHub](https://github.com/remorses/safe-mdx/releases)

**原文标题**: [Releases · remorses/safe-mdx · GitHub](https://github.com/remorses/safe-mdx/releases)

safe-mdx 发布页汇总了从 1.9.0 到 2.1.0 的版本更新，重点包括迁移到 mdastic 解析器、增强流式/增量解析、扩展 MDX 表达式中的 JSX 与模块能力，并强化安全与错误提示。

- 🚀 最新 2.1.0 新增 `createMdxStreamParser`，适用于 LLM 式持续增长的 Markdown；已闭合块不会重复解析并保持对象身份，解析器基于 mdastic 0.5。
- ⚠️ 2.0.0 为破坏性更新：仅使用 mdastic 解析，移除 remark、unified、micromark 依赖及 remark API；`mdxParse` 更快，语法错误为 `MdxParseError`。
- 🧩 2.0.0 节点类型改由 mdastic 提供；点号 JSX 标签优先按字面量键解析，如 `'Tree.Folder'`，以适配 React Server Components。
- 🛡️ 1.14.0 增加可选 `sanitize`：默认关闭，开启后移除 `script`、`object`、`embed` 等标签及危险属性/URL，并产生 `sanitize` 错误。
- 🧾 1.13.0 支持页面级 `export function` 和 `export const`，开启函数求值后导出组件/工具可在同页使用，并支持 React hooks；仍不支持 `export default`、`export class`、re-exports。
- 🧱 1.12.0 支持在 MDX 表达式中渲染 JSX，包括条件、三元、数组、对象和回调结果；支持 fragment、嵌套组件 props 校验，并将 `react-dom` 声明为 peer 依赖。
- 🔧 1.11.5/1.11.4 修复嵌套 JSX 表达式属性中的表达式值、children、spread 属性、点号组件名、错误传播和 JSX 注释处理。
- 🧑‍💻 1.11.0 改进 MDX 边界错误信息：导出、未解析导入、缺失作用域变量会给出带行号的清晰提示，并提升标识符检查准确性。
- 📦 1.10.0 允许模块导入值用于 MDX 表达式和 JSX 属性，支持 `?raw`、`?url`、`?inline` 等无扩展查询导入。
- 🔗 1.9.0 修复内容根目录之上的相对导入解析，保留 `../` 段以便下游工具映射外部 Markdown 文件。

---

### [Codemagic Patch | 面向 React Native 的自托管 OTA 更新](https://patch.codemagic.io/?utm_source=rn-weekly&utm_medium=newsletter)

**原文标题**: [Codemagic Patch | Self-hosted OTA updates for React Native](https://patch.codemagic.io/?utm_source=rn-weekly&utm_medium=newsletter)

Patch 是面向 React Native 的自托管 OTA 更新方案，主打快速部署、低成本、安全分发和可扩展管理；通过 CDN、指纹校验、差分包与发布控制，帮助团队高效向大量用户推送更新，并突出其相较其他自托管 OTA 工具在运维简化、监控和支持方面的优势。

- ⚡ 20 分钟完成安装：一条命令启动安装向导，自动配置 OAuth、CDN 缓存规则和 TLS，并通过 Docker Compose 启动服务。
- 🔐 阻止不兼容版本发布：通过指纹校验目标原生二进制，避免发布不兼容的更新。
- 📦 设备只下载小型差分包：二进制差分仅发送变更内容，弱网环境下也能更顺畅更新。
- 📊 发布、监控与推广：仪表盘提供完整发布指标，并支持分阶段发布和回滚控制。
- 🌐 服务器可承载大量用户：设备向 CDN 发起检查和下载请求，避免源服务器过载。
- 🆚 对比其他自托管 OTA：Patch 在吞吐能力、宕机影响、指纹校验、差分包、安装时机、发布指标、仪表盘、RBAC 和支持许可方面更具优势。
- 🧭 安装模式更灵活：支持立即、重启、恢复、挂起等多种安装时机。
- 🏢 由 Codemagic 打造：拥有十余年移动 CI/CD 经验，已向生产应用交付数十亿次 OTA 更新。

---

### [Codemagic 补丁](https://patch.codemagic.io/docs)

**原文标题**: [Codemagic Patch](https://patch.codemagic.io/docs)

Codemagic Patch 提供面向 React Native 与 Capacitor 的自托管 OTA 更新方案：由你自己运行 Patch 服务器，应用从该服务器下载更新，而无需等待应用商店发布。

- 🚀 自托管 OTA：应用可直接从你的 Patch 服务器获取更新，减少对商店发版的依赖。
- ⚛️ React Native：支持 JavaScript 与打包资源的 OTA 更新，文档包含本地快速开始、服务器安装和应用配置。
- 📱 Capacitor：支持 Web 资源的实时更新，文档包含本地快速开始、服务器安装和应用配置。
- 🤖 AI 辅助文档：可将 llms.txt 链接粘贴给 AI 代理，帮助查找相关页面。
- 💬 帮助与支持：如有问题，可在 GitHub 提交 issue，或在 Discord 中咨询。

---

### [宣布 Vega 2.0 正式发布](https://developer.amazon.com/apps-and-games/blogs/2026/10/vega-2-0-sdk-launch)

**原文标题**: [Announcing Vega 2.0 general availability ](https://developer.amazon.com/apps-and-games/blogs/2026/10/vega-2-0-sdk-launch)

亚马逊宣布 Vega OS 2.0、Vega SDK 2.0 及高级 Vega 开发者工具正式可用，结束开放测试；Vega OS 已运行于数千万设备并覆盖所有 Vega 驱动的 Fire TV，本次更新重点提升应用性能、开发效率与构建信心。

- 🚀 **正式发布**：Vega OS 2.0、Vega SDK 2.0 和 Vega Developer Tools 从 Open Beta 毕业，面向开发者全面开放。
- 📺 **设备覆盖**：Vega OS 已支持数千万台设备，包括 Echo 与 Fire TV；Vega OS 2.0 已推送到所有 Vega 驱动的 Fire TV 设备。
- ⚛️ **React Native 0.83**：引入 React 19、React Compiler 与 React Native DevTools；编译器自动处理 memoization，减少手动优化和 CPU 开销。
- ⚡ **Hermes v1**：改进构建时编译与设备端运行表现，尤其有利于大型目录 JSON 解析、行排序过滤和布局计算。
- 🧩 **原生 API 扩展**：提供任务调度、自定义 UI 组件等超出 React Native/WebView 的能力，支持混合 UI；原生工具与 AI 能力处于早期访问阶段。
- 🤖 **ADBT for AI**：面向 AI 编程代理提供 Amazon 设备知识与工作流，支持 Java/Kotlin Fire OS 应用迁移、EMBER 目录、Launcher、Live TV、性能调试和无障碍流程。
- ⏱️ **迁移提效**：ADBT 可生成 React Native 0.72 到 0.83 的升级计划；早期伙伴测试称 AI 辅助代码迁移可在一天内完成（不含测试）。
- 💬 **DevAssistant**：在开发者文档门户中基于官方文档回答 Vega 问题，新增领域选择、聊天历史、页面上下文、搜索概览和本地化支持。
- 🔒 **API 稳定性**：Vega 2.0 明确 API 表面在次要 SDK 版本间保持稳定，破坏性变更仅随年度主要版本发布。
- 🗓️ **发布节奏**：未来每年一次主要版本，次要版本定期发布，便于开发者规划升级并保持 SDK 更新。
- 🛠️ **升级路径**：现有应用可下载 Vega 2.0 SDK 并查看发布说明；使用 React Native 0.72 的应用建议迁移到 0.83，并用 ADBT 制定迁移计划。
- 🆕 **新开发者入口**：可通过教程搭建环境并构建首个 Vega 应用，也可下载 SDK、查看发布说明及 GitHub 示例应用。

---

### [适用于 Vega OS 的 React Native 0.83](https://developer.amazon.com/apps-and-games/blogs/2026/10/react-native-for-vega-os)

**原文标题**: [React Native 0.83 for Vega OS ](https://developer.amazon.com/apps-and-games/blogs/2026/10/react-native-for-vega-os)

Vega OS 的 React Native 0.83 支持已随 Vega SDK 0.24 推出，开发者可从 RN 0.72 升级，获得 React 19、React Compiler、Hermes v1、React Native DevTools 及最新库和 CSS 样式能力。亚马逊提供 ADBT MCP 升级助手和实操工作坊，帮助完成迁移；新项目默认使用 0.83，旧版 0.72 应用虽支持到 2027 年，但官方建议尽快升级。

- 🚀 **升级范围**：从 RN 0.72 到 0.83 跨 11 个版本，但 Vega 一直使用新架构，无需架构迁移。
- 🛠️ **ADBT 升级助手**：Amazon Devices Builder Tools MCP 可接入 AI 编程助手，检测版本、校验环境、加载 Vega 0.83 知识库并生成分步 TODO。
- 📋 **迁移步骤**：升级 Vega SDK 0.24、安装 ADBT、新建分支、运行升级工作流、构建验证 Metro 显示 RN 0.83，再启用 React Compiler 并分析性能。
- ⚛️ **React 19 与 React Compiler**：编译器在构建时自动做 memo 化，减少 TV 焦点切换时大量无意义重渲染。
- ⚡ **Hermes v1**：带来 AOT 编译和类型特化，适合数值循环、递归、字符串解析等场景；官方称在 Expensify 低端 Android 设备上包加载快 3.2%、可交互时间快 7.6%，但需自行测量。
- 🔍 **React Native DevTools**：按 `j` 打开浏览器调试工具，支持组件树/Memo 标记、Profiler 和 Network 面板，无需代理即可查看网络请求；需先转发 8081 端口。
- 📚 **生态库升级**：React Navigation、Gesture Handler、Reanimated 4、Lottie、SVG、Screens、Fast Image 等更新到适配 React 19 的版本。
- 📦 **Expo 模块**：expo-image、expo-linear-gradient、expo-file-system、expo-linking、expo-localization 等可用于 0.83，便于跨平台共享代码；部分包尚未稳定，升级前需查看发布说明。
- 🎨 **样式增强**：包含 Yoga 3 和 CSS 对齐属性，如 `boxShadow`、`outline`、`filter`、`mixBlendMode`，适合 TV 焦点光效、焦点环和未聚焦卡片弱化。
- 🆕 **新项目与示例**：新建 Vega OS 应用默认使用 0.83，AmazonAppDev GitHub 示例应用也已升级，可作为参考。
- 🧪 **学习与反馈**：提供 RN 0.83 升级实操工作坊；升级遇到问题可通过 ADBT 反馈流程或 Amazon Developer 社区论坛反馈。
- ⏳ **旧版支持**：RN 0.72 应用可继续工作至 2027 年，但官方建议尽早迁移以让用户获得新能力。

---

### [当 AI 编写所有代码时，工程师会怎样？](https://newsletter.posthog.com/p/if-ai-writes-all-the-code-whats-left?utm_source=twir&utm_campaign=nov4)

**原文标题**: [What happens to engineers when AI writes all the code?](https://newsletter.posthog.com/p/if-ai-writes-all-the-code-whats-left?utm_source=twir&utm_campaign=nov4)

AI 写代码不会让工程师消失，而是把工作重心转向“驾驶产品循环”：监控、定方向、做实现决策、评估代理产出并持续改进系统。PostHog 的代理 PR 占比四个月内从约 20% 升至 70%，工程师更像在构建“软件工厂”。

- 🧭 **核心判断**：AI 可能写出全部代码，但工程师不会灭绝；“会写代码”不再是工程师的唯一定义。
- 📈 **现实变化**：PostHog 的 monorepo PR 中，代理发起比例从约 20% 升至 70%；Anthropic 虽称“编程基本解决”，仍有 208 个含“engineer”的岗位。
- 👀 **监控情况**：工程师花大量时间监控代理、修错、响应客户、看仪表盘、跟进 PR，并建立站会机器人、仓库侦察、异常告警等系统主动获取信息。
- 🎯 **设定方向**：工程师综合个人经验、用户与公司重要性、技术可行性、竞争格局，通过 RFC 等方式决定产品该往哪走。
- 🛠️ **决定如何构建**：即使不写代码，工程师仍决定范围与实现方式，需要懂代码库、代理能力与盲点，避免只“生成代码”却引入 bug 或攻击面。
- ✅ **评估代理工作**：工程师仍需代码审查、测试与追问代理是否按方向执行；PR 量从 1 月 1441 增至 8 月 4869、工程人数仅增 10%，促使团队自建审查与预览系统。
- 🔁 **改进整个循环**：监控、方向、实现、评估相互反馈；工程师更多在构建“软件工厂”，而非只构建软件。
- 🤖 **自驱产品案例**：PostHog 的 Scout 代理可基于反馈和错误率发现 MCP 问题、生成修复、代理审查并升级人工复核，发布后继续评估是否真正解决。
- 🧠 **仍是工程工作**：这类似 OODA 循环；代码变便宜后，信息源、方向设定、实现知识、评估方式及其连接，才是工程师和产品的独特价值。

---

### [发布 0.89.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.89.0-rc.0)

**原文标题**: [Release 0.89.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.89.0-rc.0)

overview summary
React Native v0.89.0-rc.0 是预发布版本，于 11 月 4 日发布，包含 37 个提交，重点清理旧架构 API、强化新架构默认行为，并带来性能、Android/iOS 平台、工具链和稳定性修复。

- 📦 发布信息：v0.89.0-rc.0 为预发布版，附带 Hermes V1、ReactNativeDependencies 和核心 dSYM。
- ⚠️ 破坏性变更：`AccessibilityState::selected` 改为 `std::optional<bool>`；移除 `react-native/assets-registry`；Babel 关闭 `plugin-transform-destructuring`；移除旧 C++ Geometry 头文件；Community CLI 插件需显式加入 `devDependencies`。
- 🏗️ 新架构：Android/iOS 移除 `bridgelessEnabled`、`fabricEnabled`、`turboModulesEnabled` 等旧配置，bridgeless 始终启用；TurboModules 的 `+moduleName` 变为可选。
- ✨ 新增能力：加入 `useAppState()` Hook、`structuredClone`/`DOMException`、`Array.prototype.toSorted/toReversed` polyfill、`experimental_onSafeAreaInsetsChange`、Text 的 `lineBreak`/`wordBreak`，并导出 `SafeAreaInsets` 类型。
- ⚡ 性能优化：默认启用文本布局缓存和 Android 文本测量优化；VirtualizedList 减少分配；Android Touch、ScrollView、TurboModules 降低 JNI 开销；Renderer/Yoga 减少 `dynamic_cast` 和拷贝。
- 🤖 Android：`targetSdk` 升至 37，升级 NDK r28c、fbjni 0.8.1、Fresco 3.9.0、Kotlin 2.3.21；支持 Activity Result API、PCH codegen、`strictCxxApiEnabled`。
- 🍎 iOS：支持 Show Borders、`RN_STRICT_API`/`RN_ALLOW_FRAMEWORKS`、`RCTHost jsCallInvoker`；改进 SwiftPM 配置与 `RCTBridgeModule` 空值标注。
- 🧰 工具链：Metro 最低版本升至 0.87.2，Hermes 升级，DevTools 升级至 Electron 43；Codegen 支持读取 `react-native.config.cjs`，ESLint 修复 flat config 与深层导入问题。
- 🗑️ 废弃与移除：废弃 `unstable_batchedUpdates`、`JavaTurboModule::invokeJavaMethod` 缓存参数、Android 旧 UIManager surface 生命周期、iOS 旧 `RCTBridge` API；移除 `TextInput blurOnSubmit`、`hasTVPreferredFocus`、`unstable_getScrollParent`、split-bundle API 等。
- 🐞 关键修复：修复 `Easing.bezier` 陡峭曲线、Animated 颜色/共享动画、WebSocket `close()` 后消息、Image `resizeMode`/`fadeDuration`、IntersectionObserver `rootMargin`、LayoutAnimation 参数、Runtime 死锁。
- 📱 平台修复：Android 修复无障碍 live region、Text RTL/省略/字体缩放、TextInput 滚动与键盘问题、Modal 崩溃与导航栏透明；iOS 修复 TextInput、Switch、ScrollView、Accessibility 等相关问题。
- 🧪 构建/测试修复：修复 Jest 在 pnpm/Yarn pnpm 下的解析、Gradle 自动链接缓存、Hermes Windows/源码构建、CocoaPods module map/SwiftPM、Codegen 第三方组件启动崩溃。
- 🔄 升级提示：可使用 Upgrade Helper 升级，完整变更见 `CHANGELOG.md`；该版本为 RC，需重点关注破坏性变更和旧架构 API 清理。

---

### [为 RNTester 添加视觉回归测试 · robhogan 的拉取请求 #59115 · react/react-native · GitHub](https://github.com/react/react-native/pull/59115)

**原文标题**: [Add visual regression testing for RNTester by robhogan · Pull Request #59115 · react/react-native · GitHub](https://github.com/react/react-native/pull/59115)

该 PR（react-native#59115）为 RNTester 新增公共 CI 视觉回归测试：用 Maestro 流程截图，并与基线逐像素比较，支持 fork PR 且不把 PNG 基线提交进仓库；流程分为无凭据截图捕获、受信任的比较与发布、以及基于标签的变更批准，最终已合并。

- 🎯 **目标**：把 RNTester 的渲染/文本覆盖从 Meta 内部 jest-e2e 迁移到公共 CI，作为现有 Maestro E2E 之外的独立视觉流程。
- 🧪 **捕获方式**：视觉测试是 Maestro flow，深链到示例、等待就绪并按 `testID` 裁剪截图；Maestro 只截图，不判定通过/失败。
- 🔐 **信任边界**：截图捕获 job 在 Test All 中复用 Android/iOS Release 构建，运行 PR 代码但无 secrets；比较/批准在 `main` 上的受信任 workflow 中运行。
- 📱 **设备固定**：Android 使用 Pixel 7 API 35 模拟器（1080x2400、420dpi），iOS 使用 iPhone 17 Pro / iOS 26.2；一次 Maestro 调用跑完所有 flow，失败 flow 单独重试。
- 🖼️ **比较与报告**：Compare workflow 在 Test All 完成后运行，把捕获 artifact 当不可信数据先验证，再用 pixelmatch 比较；按平台发 check run，并发一条含期望/实际/差异图的 PR 评论。
- 📌 **基线规则**：每次 push 到 `main` 生成按 commit 和设备环境 key 区分的基线，不覆盖；PR 与其 base commit 或最近更早的 `main` 基线比较，批准不会直接提升 PR 图片为新基线。
- 🧭 **环境 key**：覆盖 OS、设备、屏幕尺寸/密度、字体缩放、语言、外观、动画、系统镜像及 Android 模拟器版本，避免 CI 环境漂移造成误报。
- 🏷️ **变更批准**：维护者添加 `visual-change-approved` 标签记录对“当前差异指纹”的批准；后续 push 若改变差异，标签会被移除并需重新审核。
- ⚙️ **存储与安全**：使用 GCS + GitHub OIDC，无存储 secret；仅 `main` 上两个受信任 workflow 可写，需 create-only 权限，读取公开；报告/批准 30 天过期，成本很低。
- 🧪 **严格策略**：默认任何像素变化都算差异，可按测试在 `config.json` 中放宽；测试中捕获跨多次构建/runner 字节一致，故暂不设阈值。
- ✅ **验证情况**：fork 中验证无视觉变化通过、故意文本布局变化失败、批准标签生效；5 次 Android/4 次 iOS 捕获字节一致；无关 job 失败时比较仍运行；iOS 捕获两个测试降至 2m20s。
- 🚧 **当前范围**：先加入两个文本测试并设为非阻塞，计划移植高价值 jest-e2e 测试后再把检查设为必需；尚未测试第三方 fork 无法访问存储凭据。
- 📦 **结果**：经 review 后拆分为 7 个提交并补充 README，最终由 robhogan 合并（`b1755a3`）。

---

### [](https://better-auth.com/blog/security-release-2026-11-03)

**原文标题**: [Security release on Tuesday, November 3, 2026](https://better-auth.com/blog/security-release-2026-11-03)

Better Auth 于 2026 年 11 月 3 日发布安全版本 v1.7.16 和 v1.8.0-beta.5，修复 12 个安全公告中的问题；建议所有用户尽快升级到对应版本，Vercel 虽已部署 WAF 防护，但仍推荐更新。

- 📅 安全版本：v1.7.x 升级至 1.7.16，v1.8.0-beta.x 升级至 1.8.0-beta.5。
- 🧩 包需同步升级：`@better-auth/expo`、`@better-auth/electron`、`@better-auth/passkey`、`@better-auth/stripe`、`@better-auth/kysely-adapter` 等独立发布包也使用相同版本，应一起更新。
- 🛡️ Vercel 防护：对可合理识别的问题已应用 WAF 保护，但仍建议升级到最新版。
- 🚨 严重/高危问题：Expo 授权代理可签署非其签发的值；电话号码可在验证前被占用；Electron 桌面登录可能返回服务器密钥并跳过双因素认证。
- ⚠️ 中危核心问题：邮箱变更链接在地址易手后仍有效；OAuth 可能把未验证的提供商邮箱视为已验证；MySQL 序列 ID 可能返回其他请求的记录；撤销的会话在二级存储或 Cookie 缓存下仍可能有效。
- ⚠️ 中危插件问题：Email OTP 尝试次数限制可被竞争绕过且验证码与地址绑定不严；Admin 角色具备 `user:update` 时可改他人电话号码；Organization 管理员可用填充角色名邀请所有者；Stripe 计费操作可指向其他客户账户。
- 🔎 低危问题：Passkey 验证未强制校验来源和用户验证。
- ⬆️ 升级方式：将 `better-auth` 及所有 `@better-auth/*` 包更新至 1.7.16，或 beta 线的 1.8.0-beta.5；阅读所用插件公告，部分修复需增加配置步骤，例如列出可信来源。
- 📬 安全报告：请先阅读安全政策，再通过 GitHub 私密报告或 `security@better-auth.com` 联系；官方感谢所有私下报告问题的人。

---

### [Apple 开发者计划详解：免费与付费对比](https://expo.dev/blog/apple-developer-program-explained-free-vs-paid)

**原文标题**: [Apple Developer Program explained: free vs paid](https://expo.dev/blog/apple-developer-program-explained-free-vs-paid)

未提供可总结的文章内容，因此暂时无法生成要点。
- 📄 请在“Use the following content:”后粘贴文章正文。
- 🔍 收到文本后，我会按“概览总结 + 表情符号要点”的中文格式提炼关键信息。

---

### [一款在 Expo 上三天内发布的 WebGPU 猫咪解谜游戏，由 AI 智能体担任 QA 团队](https://expo.dev/blog/purrkour-webgpu-typegpu-game-expo-three-days)

**原文标题**: [A WebGPU cat puzzle game shipped in three days on Expo, with an AI agent as the QA team](https://expo.dev/blog/purrkour-webgpu-typegpu-game-expo-three-days)

您尚未提供需要总结的文章内容，因此暂时无法生成基于原文的要点摘要。
- 📭 当前消息中未包含可总结的文本。
- 📝 请补充文章正文，我将按要求用中文要点和表情符号进行概括。

---

### [如何使用你的编码代理在 iOS 和 Android 上验证 UI 变更 | Maestro](https://maestro.dev/blog/verify-ui-changes-with-your-coding-agent?utm_source=this-week-in-react&utm_medium=newsletter&utm_campaign=verify-ui-changes)

**原文标题**: [How to Verify UI Changes on iOS and Android with Your Coding Agent | Maestro](https://maestro.dev/blog/verify-ui-changes-with-your-coding-agent?utm_source=this-week-in-react&utm_medium=newsletter&utm_campaign=verify-ui-changes)

本文介绍如何让 AI 编码代理在完成 iOS/Android UI 修改后，借助 Maestro MCP 在模拟器或真机上自行验证改动，并生成前后截图，从而在同一会话中完成实现、检查与修复闭环。

- 🎯 核心问题：许多代理会话只停留在改代码，仍需人工打开模拟器判断 UI 是否正确。
- 🤖 解决方案：Maestro MCP 让编码代理在 iOS Simulator、Android 模拟器或连接的 Android 真机上操作应用、检查视图层级并截图。
- 🧩 兼容工具：支持 Claude Code、Cursor、Codex、GitHub Copilot、Gemini、Windsurf、JetBrains AI Assistant、Grok Build 等可连接 Maestro MCP 的代理。
- 🔄 工作流：用自然语言描述产品结果，代理修改代码、构建并安装 Debug 包，然后在同一对话中打开真实界面验证。
- 🛠️ 常用工具：`list_devices` 选择设备，`run` 启动应用或执行步骤，`inspect_screen` 读取实时视图层级，`take_screenshot` 捕获前后截图。
- 🧪 示例：代理移除“Log Meal”底部弹层中的“Add a cup of water”，安装新包后用 Maestro 打开弹层，确认水相关入口消失，Photos、Describe、Barcode 和 More ways to log 仍在。
- 📸 验证结果：代理可根据设备反馈报告改动已显示、相关 UI 正常，或继续修复并重新检查。
- 💬 其他提示：可要求确认已改屏幕行为，或指出仍不对并要求修复、重装、复查。
- 💾 持久化：当路径验证通过后，可将成功步骤保存为 `.maestro/` 下的 Flow，并通过聊天或 CLI 运行 `maestro test .maestro/your-flow.yaml`。
- ✅ 要点：编码代理不仅能实现 UI 改动，还能通过 Maestro MCP 在真实设备环境中证明改动存在，并在需要时形成可复用测试流程。

---

### [React Native 屏幕 5.0.0-beta.1](https://swmansion.com/changelog/react-native-screens-5-0-0-beta-1/)

**原文标题**: [React Native Screens 5.0.0-beta.1](https://swmansion.com/changelog/react-native-screens-5-0-0-beta-1/)

react-native-screens 5.0.0-beta.1 于 2026 年 11 月 3 日发布，是 5.0 首个 beta，支持 React Native 0.88，并包含 4.30.1 中已发布的 4.x 修复。重点包括 iOS 容器内模态、Android Stack v5 转场与替换动画、iOS 27 导航栏最小化/恢复及安全区调整、表单页替代 Liquid Glass，以及破坏性的 Tabs 图标 API 变更。

- 🚀 版本定位：5.0.0-beta.1 为预发布版，支持 RN 0.88；5.0 预发布从 main 分支切出，因此包含 4.30.1 的内容。
- 🧩 iOS 新模态：新增 `ContainedModalProvider` 与 `ContainedModalOverContent`，模态限制在 provider 边界内（如 SplitView 列），并提供出现/消失生命周期事件；Android 与 Web 暂不渲染。
- 🎞️ Android Stack v5：支持 `slideFromRight`、`fade`、`iosFromRight` 等可配置转场预设，可设置 `duration`、`easing`、`distance`；新增 `replaceAnimation` 选择 replace 表现为 pop 或 push。
- 📱 iOS 27 与 Stack v4/v5：Stack v4 新增 `minimizationBehavior`、`restorationBehavior`；两个 Stack 均新增 `safeAreaAdjustment` 控制导航栏最小化时安全区跟随方式。
- 🪟 表单页与 Liquid Glass：iOS 26.1+ 表单页可替换 Liquid Glass 材质；Stack v4 表单页新增 `sheetRef` 与 `selectDetent` 命令切换 detent。
- ⚠️ 破坏性变更（Tabs 图标）：移除 `templateSource` 和 `xcasset` 类型；iOS `imageSource` 默认着色；需迁移到 `imageSource` + `renderingMode` 或 `sfSymbol`；相关类型导出移除，统一用 `TabsScreenIconIOS`。
- 🛠️ 其他改进：SplitView 支持第三方定制导航项与大标题；Android Tabs 配置变更在 React 事务结束后统一应用。
- 🐞 修复重点：Android 嵌套 Stack 弹出报错、Tabs 点击同帧外观、表单页键盘/状态栏/拖拽/无障碍问题；iOS Tabs 在 iPhone Duo 与搜索标题问题；Web `Screen` 样式保留等。
- 👥 新贡献者：欢迎 @nkt、@ilp0、@Av1for、@Bram-dc、@dongriDK。

---

### [发布 · react-native-webview/react-native-webview · GitHub](https://github.com/react-native-webview/react-native-webview/releases)

**原文标题**: [Releases · react-native-webview/react-native-webview · GitHub](https://github.com/react-native-webview/react-native-webview/releases)

该页面汇总了 `react-native-webview` 近期发布版本，最新为 v17.1.0。更新重点包括 Android WebView 属性与消息配置修复、对 React Native 0.80+ 和公共 codegen API 的适配，以及 v14–v16 中的多项破坏性变更：Android 最低 API 24、仅支持新架构、Windows 需使用 React Native Windows 新架构（Fabric）。

- 🚀 v17.1.0（最新，2026-11-04）：Android 新增 `profile` 属性，用于隔离 Cookie Jar（#4063）。
- 🐛 v17.0.2（2026-11-04）：修复 Android 将每个 WebView 的属性状态保存在视图自身，而不是共享 ViewManager 中（#4066）。
- 🐛 v17.0.1（2026-11-04）：修复 Android 需在所有属性设置完成后再应用消息通信配置的问题（#4067）。
- ⚠️ v17.0.0（2026-11-03）：改用 React Native 公共 codegen API；破坏性变更：要求 React Native ≥0.80，macOS 要求 `react-native-macos` ≥0.81。
- 📍 v16.0.2（2026-11-03）：修复 Android 对 `ACCESS_COARSE_LOCATION` 权限的处理（#3947）。
- 📷 v16.0.1（2026-11-03）：修复 Android 带 `capture` 的文件输入无法打开相机的问题（#4064）。
- 🧱 v16.0.0（2026-07-11）：移除旧架构（Paper）支持，必须使用新架构；同时修复 macOS Fabric 回收、`dataDetectorTypes`、iOS `clearCache` 与 Cookie 观察者注销等问题。
- 🪟 v15.0.0（预发布，2026-07-05）：Windows 支持新架构（Fabric），移除旧架构 WebView 与 WebView2 Paper 实现；全平台升级 React Native 版本，如 RN 0.86、React 19.2.7。
- 📦 v14.0.1（2026-06-20）：将原生 TypeScript 预览移至 devDependency（#3966）。
- 📱 v14.0.0（2026-06-20）：破坏性变更：Android 最低要求 API 24（Android 7.0 Nougat），移除旧版文件上传路径与兼容代码（#3965）。

---

### [发布 Release 1.10.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.10.0)

**原文标题**: [Release Release 1.10.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.10.0)

margelo/react-native-nitro-fetch 发布 v1.10.0，主要带来 Android Cronet 缓存与预取优化、XMLHttpRequest 桥接、流式请求/WebSocket 内存修复，以及跨域重定向与请求校验等安全性和规范兼容改进。

- 📦 版本发布：v1.10.0 为最新版本，发布于 11 月 4 日，包含多项新功能、修复和测试补充。
- ⚙️ Android 优化：Cronet HTTP 缓存大小可配置；包构造时预热 Cronet 引擎；修复 R8 下 hybrid object 构造函数被移除的问题。
- 🧠 预取能力：新增非持久化原生 `prefetch()`，并新增 `clearPrefetchCache()` 用于清理预取缓存。
- 🍪 Cookie 与重定向安全：修复流式请求 Cookie 管理；跨域重定向时丢弃 `Authorization`，同源重定向保留；复用重定向 body 并宽松解析 origin。
- 🧩 Fetch 兼容性：将 `NitroResponse` 识别为标准 Fetch Response；非法请求头名称/值、GET/HEAD 携带 body 会抛出 `TypeError`；`stream: true` 支持跟随重定向。
- 🌐 XMLHttpRequest：新增 XHR bridge；按规范修复状态、错误、校验、进度事件字节数、无 credentials 时省略 Cookie、失败清空响应、仅服务端流式时流式处理等行为。
- 🧵 流式与内存：`stream: true` 请求完成后可被回收；JavaScript 繁忙时仍可读取流式 body；关闭 WebSocket 后释放回调以便垃圾回收。
- 🛡️ 稳定性与安全：修复 Hermes 无采样 profiler 时 `profileFetch` 崩溃；JS token 刷新 pinning、iOS 拒绝重复 hosts；`nitro-fetch-pinning.json` 应用于 WebSockets。
- 👥 社区贡献：新增 @oblador、@vnxpixel、@hannojg、@riteshreal、@gustavomts、@SvenLinderoth 等贡献者。
- 🔗 完整变更：可查看 `v1.9.0...v1.10.0` 的 Full Changelog。

---

### [发布 v10.0.0 · callstack/react-native-pager-view · GitHub](https://github.com/callstack/react-native-pager-view/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · callstack/react-native-pager-view · GitHub](https://github.com/callstack/react-native-pager-view/releases/tag/v10.0.0)

本次发布为 react-native-pager-view 的 v10.0.0 最新版本，由 troZee 于 11 月 4 日发布，包含 1 个提交。该版本包含一项破坏性变更，并集中修复了 iOS/Android 的多项交互、渲染与状态问题，同时更新了 CI 和仓库维护流程。

- 🚀 **破坏性变更**：将 PagerView 转换为函数组件。
- 🐛 **通用修复**：跳过空子元素，并在每次拖拽时关闭键盘。
- 🍎 **iOS 修复**：离开页面时清除焦点并隐藏键盘，修复 iOS 15 上的滚动事件、FullWindowOverlay 渲染、Detox 点击事件及隐藏导航栏问题。
- 🤖 **Android 修复**：优化垂直拖拽交给下方 ScrollView，修复同次提交新增页面的 setPage、空 Pager 新增页面显示、滑动结束状态上报及 Compose 状态保存问题。
- 🧹 **代码清理**：移除 iOS 死代码并加强挂载前事件保护，移除 Android 已废弃的事件和包 API。
- 🔁 **CI/维护**：为 GitHub Actions 添加 Dependabot，使用机器人关闭不活跃 issue，并调整 iOS CocoaPods 任务缓存。
- ✅ **发布状态**：标记为 Latest，包含 2 个资源文件，并获得 1 个 🎉 反应。

---

### [Maestro CLI 2.12.0：Cloud 上传的队列优先级](https://maestro.dev/blog/maestro-cli-2-12-0)

**原文标题**: [Maestro CLI 2.12.0: queue priority for Cloud uploads](https://maestro.dev/blog/maestro-cli-2-12-0)

Maestro CLI 2.12.0 于 2026 年 10 月 28 日发布，核心是为 Maestro Cloud 上传加入队列优先级，并修复/改进了 iOS、Android、Web、截图测试、MCP 与并发会话等多方面问题。

- ☁️ Maestro Cloud 上传支持队列优先级：使用 `maestro cloud --priority high` 可让该上传的流程优先于本组织内等待中的 normal/low 流程；high 适合候选发布或热修复，low 适合可等待的夜间任务，normal 为默认值。
- ⚙️ 优先级可通过 CLI、GitHub Actions 和 MCP 的 `run_on_cloud` 使用，也可在上传仍运行时从 Maestro Console 修改；仅调整本组织队列顺序，不影响跨组织排序或并发限制；需 CLI 2.12.0 或 Maestro Cloud action 3.1.0。
- 📜 滚动速度必须介于 0 到 100，越界点会使流程失败；此前越界值会静默使用默认值，升级前建议检查流程。
- 🧪 无效的 `index`、point 和 speed 值会报告为测试错误：字面量在上传、设备启动前捕获，变量值在运行时检查，避免 Maestro Cloud 不必要地重试。
- ⌨️ Android 上 `pressKey: Tab` 现在移动焦点，而不是输入错误字符，后续输入会落到预期位置。
- 📱 Android 输入不再等待窗口动画；Android 12+ 的 `inputText` 和 `eraseText` 直接注入按键事件，慢启动页不再导致“Device server died”，示例中 21 个字符从超过 200 秒降至 4 到 16 秒；点击仍会等待动画。
- 🚀 `start-device` 不再在模拟器启动或 sdkmanager 上无限挂起：约 5 秒内提示，可识别已安装系统镜像，启动失败约 1 分钟内报错并指向模拟器日志。
- 🖥️ 模拟器可在 Xcode 27 上启动；Xcode 27 不再自带 Simulator.app，模拟器以无头方式启动，在设备查看器中流式显示并接受点击和按键；Xcode 26 及更早版本不变。
- 🛡️ iOS 应用崩溃检测更可靠，即使系统未写崩溃报告，也会读取模拟器终止记录区分真实崩溃、正常停止或断言失败，并写入运行包中的 `logs/crash-report.txt`；模板化 app ID 如 `${APP_ID || 'com.example.app'}` 也会为实际应用收集报告。
- 🌐 Web 上 `launchApp` 会等待其打开的页面，避免下一步与 Chrome 竞争；页面不可达时由 `launchApp` 返回连接错误；Web 录制和深色模式模拟支持 Chrome 153 至 155。
- 🧷 截图流程恢复上传到 Cloud：使用 `assertScreenshot`（包括嵌套 `runFlow`）的工作区可正常校验和上传，修复 2.11.0 引入的校验错误；截图差异写入运行包的 `assertScreenshot/`，列于 `manifest.json`，失败信息包含路径。
- 🪟 修复 MCP 的 Android 设备镜像在 Windows 上冻结的问题。
- 📁 修复长流程名导致的“File name too long”：每个流程的产物目录名会缩短并附加短哈希，超过 Windows 255 字节限制也不再阻止运行。
- 🔐 并发会话数据库访问更安全：会话键值存储的读写使用同一文件锁；若一次只运行一个 Maestro，则无变化。
- ⬆️ 升级命令：`curl -fsSL "https://get.maestro.mobile.dev" | bash`；Windows 和 Homebrew 步骤见更新指南。

---

### [发行版 · jpudysz/react-native-unistyles · GitHub](https://github.com/jpudysz/react-native-unistyles/releases)

**原文标题**: [Releases · jpudysz/react-native-unistyles · GitHub](https://github.com/jpudysz/react-native-unistyles/releases)

该内容汇总了 react-native-unistyles 仓库从 v3.3.0 到 v3.8.1 的发布记录，重点涵盖主题与样式修复、性能优化、Metro 集成演进、最低 React Native 版本提升、Web/SSR 与跨平台兼容性改进，以及社区贡献者的修复。

- 🚀 最新版本 v3.8.1 为补丁发布，修复 Reanimated 动画运行期间主题切换在 Android 卡顿数秒、iOS 调试构建中止的问题，并恢复 Web 上 `withUnistyles` 对 Gesture Handler 3 组件的样式支持。
- 🖥️ v3.8.1 还修复 Expo Router `web.output: "server"` 下页面 500 错误，并改进服务端样式接管、`<Display>`/`<Hide>` 与服务端渲染兼容性。
- ⚠️ v3.8.0 引入破坏性变更：最低要求 React Native 0.85+ / Expo SDK 56+；实验性 Metro 集成不再运行 Babel 转换，并预告 Babel 插件将在下一版本弃用、4.0 移除。
- ⚡ v3.8.0 大幅优化 Web 样式更新：改为通过 CSSOM 按规则增删改，避免整体重写 `<style>`，新增/删除样式快 2–8 倍，未变化样式重应用可快 100 倍以上。
- 🔄 v3.8.0 提供从 Babel 插件迁移到 Metro 集成的三步方案，并新增 codemod 处理 `styles.useVariants()` 返回值变更。
- 🎨 v3.7.0 的破坏性变更是 `UnistylesRuntime.themeName` 始终返回应用主题；读取 ScopedTheme 主题名应使用 `useUnistyles().rt.themeName` 或 `withUnistyles`。
- 🧩 v3.7.0 增加 React Native 0.88 新样式属性支持、DevTools 性能追踪中的“Unistyles”轨道，并修复 Android Modal 键盘 insets、Expo 重复包、Next.js 服务端组件、Reanimated 样式等问题。
- 🚇 v3.6.0 推出实验性零配置 Metro 集成，可替代 Babel 插件；同时优化普通视图渲染性能、支持 Reanimated CSS 过渡跟随主题、修复 `useVariants` 内存泄漏和 iOS 渐变主题更新。
- 🛠️ v3.5.x 系列集中提升稳定性：恢复并超过 3.3.0 的挂载/主题切换性能，修复 ScopedTheme 延迟组件、深层 style 数组、Activity 隐藏状态、Android 自适应主题、iOS `use_frameworks!` 构建、动画 ref 崩溃与 worklet 读取样式风险。
- 🧠 v3.5.0 重点修复主题更新丢失、冻结屏幕恢复卡顿、StyleSheet 引用环导致的重载内存泄漏、OTA/dev reload 后运行时状态被旧实例清除，以及 Web 影子注册表累积问题。
- 📦 v3.4.0 将最低 React Native 版本提升至 0.81，依赖 `ShadowNode::getFamilyShared()`，并移除旧版本兼容代码；RN 0.76–0.80 用户需停留在 Unistyles 3.3.x。
- ✨ v3.3.0 增加 `transformOrigin` 字符串解析、Android 背景图原生属性解析、React Navigation inactive 行为支持，并修复系统栏 mock、Web 影子注册表重置等问题。
- ❤️ 多个版本均感谢社区贡献者提交 PR、复现问题和详细 bug 报告，体现项目在主题系统、跨平台渲染与构建工具链上的持续迭代。

---

### [](https://github.com/appandflow/react-native-safe-area-context/releases/tag/v5.11.0)

**原文标题**: [Release Release 5.11.0 · appandflow/react-native-safe-area-context · GitHub](https://github.com/appandflow/react-native-safe-area-context/releases/tag/v5.11.0)

react-native-safe-area-context 发布 v5.11.0，本次更新主要集中在新版响应式落地页与文档站点、README 展示优化，以及 Android 和 Web 端安全区域相关修复与功能增强。

- 🚀 新增响应式项目落地页，并更新 README 横幅
- 🌐 文档与落地页部署至 Vercel，域名为 rnsac.appandflow.com
- 🔗 README 的 About 部分新增线上网站链接
- 🎨 优化落地页按钮、许可证悬停样式，并恢复更小的按钮与左对齐布局
- 📱 Android 端支持尊重父级为其子树调整的窗口 insets
- 📐 新增适配屏幕圆角的安全区域 insets
- 🖥️ 修复 Web 端滚动时安全区域 insets 增大的问题
- 🗺️ 为新域名宣传 sitemap
- 📦 正式发布 5.11.0，包含 5 个提交，完整变更范围为 v5.10.1...v5.11.0
- 👥 新贡献者 @floco-af 参与发布；贡献者包括 satya164、janicduplessis 等 5 人

---

### [GitHub - margelo/react-native-tgfx · GitHub](https://github.com/margelo/react-native-tgfx)

**原文标题**: [GitHub - margelo/react-native-tgfx · GitHub](https://github.com/margelo/react-native-tgfx)

该项目是 margelo 在 GitHub 上开源的 react-native-tgfx 仓库，页面展示了项目简介、源码结构、文档入口、许可证信息与社区协作数据，便于了解项目概况和参与贡献。

- 📦 仓库信息：react-native-tgfx 为公开仓库，归属于 margelo。
- ⭐ 社区数据：获得 64 个 Star、3 个 Fork，Watcher 数量为 0。
- 🐛 协作状态：当前有 1 个 Issue 和 7 个 Pull Request。
- 📚 文档入口：项目文档地址为 https://tgfx.margelo.com。
- 📜 开源许可：采用 MIT License，并提供 Contributing 贡献指南。
- 🗂️ 主要目录：包含 apps、docs、packages、patches、scripts、.github/workflows、.claude 等。
- 📄 根目录文件：包括 README.md、ROADMAP.md、CONTRIBUTING.md、AGENTS.md、LICENSE、package.json、bun.lock 等。
- 🧾 代码活动：主分支为 main，包含 Branches 和 Tags，历史提交约 320 次。
- 🛠️ 功能入口：提供 Code、Issues、Pull Requests、Actions、Projects、Security and quality、Insights 等仓库导航功能。

---

### [发布 v3.9.0 · wcandillon/react-native-skia · GitHub](https://github.com/wcandillon/react-native-skia/releases/tag/v3.9.0)

**原文标题**: [Release v3.9.0 · wcandillon/react-native-skia · GitHub](https://github.com/wcandillon/react-native-skia/releases/tag/v3.9.0)

react-native-skia 发布 v3.9.0（2026-11-02），主要包含渲染与 GPU 生命周期、Android 兼容性、Canvas API 及异步读取等方面的修复与增强。

- 🚀 版本发布：v3.9.0 共 7 个提交合入 main，由 GitHub Actions 发布。
- ⚛️ 渲染修复：重渲染后保留未变化的场景节点，减少不必要更新。
- 🍏 后台处理：应用进入后台时暂停 GPU 工作。
- 📱 GPU 探测：改为首次使用时探测 GPU，不再单独创建线程。
- 🗺️ Atlas API：改进 atlas API polyfill。
- 🗿 Canvas 日志：帧无法开始时记录失败日志，而非静默丢弃。
- 🤖 Android 修复：Imagination GPU 上不再请求 TransientAttachments；主线程任务投递不再调用 Java。
- 🎨 功能恢复：恢复 Canvas 的 colorSpace 属性。
- 🖼️ 新功能：支持异步 readbacks。

---

### [React Native 0.88 与 Expo 58 库就绪情况 · NativeKeel](https://nativekeel.com/react-native-0-88-library-readiness)

**原文标题**: [React Native 0.88 & Expo 58 library readiness Â· NativeKeel](https://nativekeel.com/react-native-0-88-library-readiness)

概述：文章检查了 590 个下载量最高的、包含原生代码的 React Native 库，评估它们对 React Native 0.87/0.88 与 Expo SDK 58 的兼容性。结果显示，0.88 本身没有破坏性变更，但 0.87 的两项变更会导致部分库构建失败或运行崩溃，影响从 0.86 及更早版本升级、以及从 Expo SDK 57 升级到 58 的应用。

- 📊 共检查 590 个库：572 个通过两项兼容性检查，18 个会在 0.87/0.88 上出问题。
- ⚠️ React Native 0.88 没有自身破坏性变更，但 0.87 有两项会破坏库的变更，升级路径上的应用都会遇到。
- 🍎 iOS 头文件改为 XCFramework 后，库若写 `#import "RCTBridge.h"` 而不是 `#import <React/RCTBridge.h>`，会因找不到文件导致构建失败。
- 🧩 JavaScript 侧移除了 `InteractionManager` 以及 `StatusBar` 的 `setBackgroundColor`、`setTranslucent`、`setNetworkActivityIndicatorVisible`；开发构建会抛错，发布构建可能崩溃。
- 📉 18 个受影响库按周下载量排序，包括 `@react-native-menu/menu`、`react-native-date-picker`、`react-native-ios-context-menu`、`react-native-bottom-tabs`、`react-native-svg-charts` 等。
- 🛠️ 已提交 8 个修复并在 0.87.1 上测试；部分库已在主分支或新版本修复，也有库暂无修复、停止维护或仓库归档。
- 🔍 该检查不覆盖 Android 构建、运行时行为及其他变更；通过检查不代表完全兼容，被列出的库则确定需要处理。
- 💻 可使用 `npx nativekeel` 扫描已安装库的 iOS 代码，在升级前发现 0.87 构建问题；工具免费开源并在本地运行。

---

### [GitHub - callstackincubator/simlock：一个控制平面，让并行编码代理不再争抢同一个模拟器。 · GitHub](https://github.com/callstackincubator/simlock)

**原文标题**: [GitHub - callstackincubator/simlock: A control plane so parallel coding agents stop fighting over the same simulator. · GitHub](https://github.com/callstackincubator/simlock)

Simlock 是一个开源控制平面，面向并行运行的编码代理，通过设备租赁避免多个代理争用同一台 iOS 模拟器、Android 模拟器或已注册手机；它负责设备启动检查、独占分配、排队、自动创建与清理，并可通过网关扩展多台 Mac/Linux 机器。

- 🎯 **核心目标**：让每个编码代理独占一台设备，直到释放，避免并行开发时争抢模拟器。
- 📱 **支持设备**：iOS 模拟器、Android 模拟器和已注册手机。
- 🔄 **调度机制**：无空闲设备时自动创建；机器满载时排队请求；自动清理无人使用的设备。
- 🌐 **多机扩展**：可先在一台 Mac 上使用，再通过 Gateway 将多台 Mac/Linux 机器组成设备池。
- 🚀 **快速上手**：全局安装 `npm i -g simlock`，运行 `simlock doctor` 检查环境，再用 `simlock lease --platform ios --device "iPhone 16"` 租赁设备。
- 📚 **文档支持**：官网提供安装、设备使用、Worker、Gateway，以及命令、配置、事件和错误参考等文档。
- 📊 **项目概况**：MIT 开源，594 Stars、28 Forks、65 Issues、16 Pull Requests、639 Commits，主题为 agents、emulators、simulators。
- 💡 **社区背景**：由 Callstack 团队打造，鼓励 Star 和参与贡献。

---

### [GitHub - vercel-labs/agent-desktop：面向 AI 智能体的计算机使用命令行工具 · GitHub](https://github.com/vercel-labs/agent-desktop)

**原文标题**: [GitHub - vercel-labs/agent-desktop: Computer use CLI for AI agents · GitHub](https://github.com/vercel-labs/agent-desktop)

agent-desktop 是 Vercel Labs 开源的 AI 智能体桌面操作工具，通过操作系统无障碍树读取并操作 macOS、Windows、Linux 桌面应用，无需截图或像素匹配，提供 CLI 和 C 库两种使用方式。

- 🖥️ 核心能力：将桌面应用的无障碍树转为 JSON，并为可操作元素生成 ref，智能体可点击、输入并重新读取界面验证结果。
- 🤖 无内置模型：操作循环由外部智能体控制，agent-desktop 只负责观察与执行桌面操作。
- 📦 安装方式：支持 `npm install -g agent-desktop`、Homebrew，也提供 x64/ARM64 原生二进制。
- 🔁 典型流程：先 `snapshot` 获取带 ref 的快照，再对 ref 执行 `click`/`type`，最后再次快照确认；UI 变化会返回 `STALE_REF` 或 `AMBIGUOUS_TARGET`。
- ⌨️ 操作模式：默认无头执行，不移动指针、不改变焦点；加 `--headed` 可进行物理输入；敏感文本可通过 `--stdin` 传入。
- 🧰 命令丰富：共 60 个命令名、56 个可操作命令，覆盖观察、元素操作、键鼠、应用窗口、通知、剪贴板、等待、会话和系统信息。
- 🔌 MCP 支持：`agent-desktop mcp` 可通过 stdio 将所有命令暴露为 MCP 工具，便于智能体框架调用。
- 🪟 平台支持：macOS 13+ 使用 AX API，Windows 10 1809+ 使用 UI Automation，Linux Ubuntu 24.04+ 使用 AT-SPI。
- 🧑‍💻 开发者集成：提供 `libagent_desktop_ffi` C 库，可在进程内调用；还提供技能文档和 `AGENTS.md` 集成指引。
- 🔐 安全提醒：快照、剪贴板、截图、命令输出和调试产物可能包含隐私桌面内容，应避免进入公开日志或上传。
- ⭐ 项目热度：约 15.1k stars、1k forks，采用 Apache-2.0 许可证。

---

### [发布 v0.31.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.31.0)

**原文标题**: [Release v0.31.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.31.0)

v0.31.0 发布概览：Argent 发布 v0.31.0，自 v0.30.1 以来包含 26 次提交，重点加入 HarmonyOS 设备支持、iOS 运行器品牌化，并集中优化 MCP、截图差异、设备启动、CI 与文档。

- 🚀 v0.31.0 于 10 月 28 日发布，包含 26 次提交，完整变更对比为 v0.30.1...v0.31.0。
- 📱 新增 HarmonyOS 支持：可通过 hdc 驱动 HarmonyOS 设备，并补充构建与签名 HAP 的文档。
- 🍎 iOS 设备运行器更名为 Argent Runner，并添加应用图标。
- ⚡ MCP 性能与稳定性改进：await-ui-element 后返回屏幕、并发捕获操作后截图与元素树、只读工具发送 readOnlyHint、元素树不可读时限制操作后捕获。
- 🐞 修复工具客户端：去除 ARGENT_TOOLS_URL 末尾斜杠，并在 spawn 后关闭父进程的 tool-server 日志 fd。
- 🎯 修复手势与截图差异：拒绝越界归一化坐标与字符串参数，并处理 diff 恰好等于 maxMismatch 的快照。
- 🖥️ 修复设备/模拟器启动：等待被杀死模拟器后再启动、macOS Android 模拟器禁用 guest Vulkan、支持在外部杀死后启动 AVD。
- 🔒 修复网络与远程行为：includeBody 拒绝字符串、会话关闭后拒绝 MoQ 发送、空或空白 --host 视为 127.0.0.1。
- 🛠️ CI/文档更新：使用自托管 tart macOS runners、按 sand label 定位 runner，并修正文档与模拟器服务器停止说明。
- 👥 贡献者包括 blazejkustra、monsterlag 等 5 人。

---

### [](https://swmansion.com/changelog/react-native-rag-0-11-0/)

**原文标题**: [react-native-rag 0.11.0](https://swmansion.com/changelog/react-native-rag-0-11-0/)

react-native-rag 0.11.0 于 2026 年 11 月 2 日发布，属于小版本更新；主要涉及 @react-native-rag/executorch 的依赖升级、ExecuTorchLLM 的模型加载与上下文适配，以及一项依赖版本要求的破坏性变更，API 本身保持不变。

- 🚀 @react-native-rag/executorch 现运行于 react-native-executorch 0.11。
- 🧠 ExecuTorchLLM 通过新的异步 createLLMRunner 加载模型，并按模型的 maxContextLen 适配对话上下文。
- 🔤 将 tokenizer 的 BOS 和 EOS token 传入聊天模板（#27，由 @msluszniak 贡献）。
- 📦 适配器支持 react-native-worklets 最高至 0.13（#27）。
- ⚠️ 破坏性变更：@react-native-rag/executorch 要求 react-native-executorch ^0.11.0，以及 react-native-blob-util 0.24.11 或更新版本；API 无变化。
- 🔗 提供完整变更日志：v0.10.0...v0.11.0，并附发布卡片与下载入口。

---

### [Argent e2e 教程：录制移动端测试并在 CI 中运行 | Argent 博客](https://argent.swmansion.com/blog/argent-e2e-tutorial/)

**原文标题**: [Argent e2e Tutorial: Record a Mobile Test and Run It in CI | Argent blog](https://argent.swmansion.com/blog/argent-e2e-tutorial/)

本文介绍 Argent e2e 如何用简短 YAML 文件记录并回放移动端端到端测试：编码代理录制一次操作路径，`argent e2e run` 即可在本地或 CI 中无 AI 模型回放。文章覆盖安装、稳定 ID、录制首个测试、本地运行、GitHub Actions 集成、Android 支持和主要限制。

- 📱 Argent e2e 测试保存在 `.argent/e2e/` 的 YAML 文件中，可像普通代码一样提交和审查；文件不保存设备 ID，因此同一测试可跨模拟器或设备运行。
- 🧰 准备条件包括 macOS + Xcode、可构建到模拟器的 App，以及用于录制的编码代理（如 Claude Code、Cursor、Codex）；运行测试不需要代理。
- ⚙️ 安装时执行 `npx @swmansion/argent@latest init`，向导会安装 Argent、注册 MCP 服务器并添加录制技能；`--local` 可固定项目内版本。
- 🎯 为关键页面添加稳定 ID（iOS 用 `accessibilityIdentifier`，React Native 用 `testID`，Android 用 resource id）；稳定 ID 比文本更抗文案和布局变化，坐标点击则很脆弱。
- 🎬 录制时让代理从 App 新启动开始执行目标路径；代理会实际操作并验证结果，完成后回放并生成 YAML，其中包含 `launch`、`await`、`tap`、`type`、`assert` 等步骤。
- ▶️ 本地运行使用 `argent e2e run search --platform ios`；CLI 会打印每步结果，成功退出码为 0、失败为 1；失败时停止测试、跳过剩余步骤并截图，`--output` 可指定工件目录。
- 📂 运行整个目录使用 `argent e2e run .argent/e2e --recursive --platform ios`；目录运行在失败后继续，最后汇总失败测试、失败步骤、原因和单独重跑命令。
- 🍎 GitHub Actions 工作流在 `macos-15` 上构建 Release、启动 iPhone 模拟器、安装 App、运行全部 e2e 测试并上传失败截图；整个作业约 5 分钟，测试本身约 30 秒。
- 📌 CI 中应固定 `--platform` 和 `--device`，并用 `--output` 上传失败截图；CI 只需 Argent CLI，不必运行 `init`；失败检查通常会直接显示截图和失败原因。
- 🤖 Android 可复用同一 YAML：使用 Ubuntu 24.04+、支持 KVM 的 Linux runner，设置 `ARGENT_EMULATOR_NO_WINDOW=1`，启动模拟器并安装 APK；若 iOS/Android ID 不同，可在 `launch` 中按平台配置。
- ⚠️ 限制包括：每次运行只覆盖一台设备、`launch` 会保留 App 数据和后端状态、坐标步骤易失效、测试串行执行、macOS runner 成本较高；可用 `ios-remote`/Argent Cloud 替代。
- ✅ 关键结论：代理只需录制一次，之后 `argent e2e run` 无模型调用、不消耗 token；修复 bug 时可让代理把复现路径记录为测试；示例仓库 `argent-e2e-example` 包含 App、测试与 CI 工作流。
- ❓ 常见问题：Argent e2e 属于 `@swmansion/argent`；录制需要 AI 代理、运行不需要；0.30.0 将 flows 更名为 e2e tests 并兼容旧目录；支持原生 iOS/Android、React Native、Expo、Flutter、Kotlin Multiplatform 等。

---

### [“也许 React Native 是不可能的”Alex Mikucki x Chas J](https://www.youtube.com/watch?v=NYOM5ujWI9Y)

**原文标题**: [“Maybe React Native Is Impossible” Alex Mikucki x Chas Jhin From Discord | Software Mention Podcast - YouTube](https://www.youtube.com/watch?v=NYOM5ujWI9Y)

该内容是 YouTube 网站页脚中的导航与法律信息，涵盖平台介绍、媒体与联系渠道、创作者和开发者资源、广告合作、条款与隐私政策、安全说明、功能测试入口，以及版权归属信息。

- ℹ️ 提供“关于”“新闻”“联系我们”等平台基本信息入口。
- 🎬 包含“创作者”“广告”“开发者”等面向不同用户的资源链接。
- 📄 列出“条款”“隐私”“政策与安全”等法律与合规相关页面。
- 🛠️ 提供“YouTube 运作方式”和“测试新功能”的说明或入口。
- ©️ 标注版权信息为“© 2026 Google LLC”。

---

### [pull_request_target 默认被阻止 12 月 2 日 - GitHub 变更日志](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/)

**原文标题**: [pull_request_target blocked by default December 2 - GitHub Changelog](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/)

GitHub 宣布，自 2026 年 12 月 2 日起，公共仓库中的 `pull_request_target` 事件将默认被阻止；除非适用的 Actions 事件策略明确允许。原定生效日期为 2026 年 11 月 2 日。私有仓库和内部仓库不受影响。该规则初期以评估模式运行，并通过两次临时强制窗口帮助用户识别受影响的工作流。

- 🚫 **默认阻止**：2026 年 12 月 2 日起，公共仓库中的 `pull_request_target` 工作流默认被阻止；除非 Actions 事件策略明确允许。
- 🔒 **安全原因**：`pull_request_target` 在基础仓库上下文中运行，并可访问密钥；若执行来自 fork 的不可信代码，可能导致流水线被破坏或密钥被窃取。
- 🗓️ **临时强制窗口**：2026 年 11 月 9 日和 11 月 16 日，UTC 16:00–18:00 将临时执行默认保护。
- ⚠️ **窗口期行为**：被阻止的 `pull_request_target` 工作流尝试会生成失败运行并带有错误注解，工作流不会执行；窗口结束后恢复评估模式，允许运行但会给出警告。
- 🧰 **提前准备**：在 11 月 9 日首次窗口前，使用 Insights 查看哪些工作流运行会被该规则阻止。
- ✅ **处理选项**：保留默认规则以阻止 `pull_request_target`，或在适用的 Actions 事件策略中显式允许，并通过工作流文件定向允许特定工作流。
- 🌐 **适用范围**：适用于 GitHub Free、GitHub Team 和 GitHub Enterprise Cloud 上的公共仓库，不适用于 GitHub Enterprise Server。

---

### [](https://developer.chrome.com/blog/html-in-canvas)

**原文标题**: [HTML-in-Canvas in Chrome 157: Interactive DOM inside 2D, WebGL, and WebGPU  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/html-in-canvas)

HTML-in-Canvas API 在 Chrome 157 正式稳定发布，经过 Origin Trial 后落地，旨在将可交互、可访问的 DOM 内容融入 2D、WebGL 与 WebGPU 画布，兼顾浏览器原生能力与 GPU 加速图形性能。

- 🚀 Chrome 157 稳定版正式推出 HTML-in-Canvas API，打通 DOM 与 `<canvas>` 的交互与像素级控制。
- ⚖️ 过去开发者需在 canvas 与 HTML 间取舍：canvas 性能强但缺乏文本选择、无障碍、查找等能力；HTML 语义与可访问性好但复杂 UI 性能和像素控制有限。
- 🧩 旧方案痛点明显：`fillText()` 会破坏可访问性和浏览器功能；浮动 HTML 覆盖层存在同步延迟、裁剪/z-order 限制和逐帧性能开销。
- ✅ 新 API 让 canvas 内 HTML 保持交互与浏览器集成，包括文本布局、表单控件、选择复制右键、无障碍树、翻译、自动填充、页内查找、扩展和 DevTools。
- 🎨 支持媒体编辑与导出，可将包含实时 DOM 的 canvas 合成导出为图片或视频流。
- 🏗️ 主要用例包括大型 canvas 应用、3D/WebXR 场景与游戏、媒体编辑导出，以及着色器驱动的表现型 UI。
- ⚙️ 快速上手需设置 canvas 的 `content="drawable"`、标记子元素为 `drawable`；2D 使用 `drawElementImage()`，3D 使用 `updateElementGeometry()` 同步变换。
- 🧱 生态支持包括 Three.js `HTMLTexture`、PlayCanvas `setSource()`、Babylon.js `HtmlTexture`、PixiJS `HTMLSource` 和 CanvasUI 等第三方社区项目。
- 🛟 兼容性方面应先检测 API 支持；不支持时可回退到替代 UI、浮动 HTML 覆盖层或 `html2canvas`、`dom-to-image` 等库。
- 📚 后续可查阅 Chrome for Developers 文档、Modern Web Guidance、WICG 仓库反馈和社区示例。

---

### [](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

**原文标题**: [Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

Node.js 27.0.0-alpha.0.0.0 是 2026-10-29 发布的 Alpha 版本，由 Rafael Gonzaga 发布，核心变化是升级到 V8 15.6，并包含大量 semver-major 破坏性变更、弃用、实验性 API 和安全修复。

- 🚀 V8 升级至 15.6.75.13（Node.js 26 为 14.6），默认启用 `Math.sumPrecise()`、`Intl.Locale.prototype.variants`、`Iterator.prototype.join()`、`Iterator.prototype.includes()`、`Iterator.zip()` 和 `Iterator.zipKeyed()`。
- 🧪 新增实验特性需 flag：`import defer`、Immutable `ArrayBuffer`、RegExp buffer boundaries。
- 🧠 内存默认值变化：未设置 `--max-old-space-size` 时，堆上限为物理内存一半，限制在 256 MB 到 4 GB；`Buffer` 和 `ArrayBuffer` 占用计入堆限制，依赖旧默认值的应用需显式配置。
- 📦 序列化格式变化：`v8.serialize()`、`structuredClone()`、`postMessage()` 使用新格式，旧版 Node.js 无法读取；编译缓存和 `v8.cachedDataVersionTag()` 会随 V8 补丁变化。
- ⚠️ 可观察行为变化：`Math` 方法可能最后一位不同；`Math.random()` 序列改变；`error.stack` 不再沿原型链查找；`await` 微任务更少；大数组 `sort()` 使用 PowerSort 且保持稳定；堆快照更大更慢；asm.js 不再编译为 WebAssembly。
- 🔐 构建与加密：要求 OpenSSL 3 或更高版本，移除捆绑 FIPS provider、legacy OpenSSL 代码路径和 OpenSSL engine 支持；多项 crypto API 校验增强并进入 EOL；Intel macOS 支持降为实验性。
- 🌐 运行时与 API：`fs` 原生实现 glob、新增 `mkstemp()`；HTTP `keepAliveTimeout` 默认增至 65 秒、`req.headers` 改为空原型、拒绝超限响应头；新增实验性 `net/promises`；`domain` 运行时弃用并迁移到 AsyncLocalStorage。
- 🧩 其他 semver-minor：`zlib` 增加 `crc32c`；`vfs` 取消 flag；`test_runner` 增加 mock/promise 辅助；`process` finalization 返回 unregister 函数；新增 `--experimental-strip-private-modules`。
- 🔧 原生模块：`NODE_MODULE_VERSION` 更新至 153，原生插件需要重新编译。
- 🛡️ 安全与修复：包含 CVE-2026-58042 DNS `resolveAny` 大响应处理等修复，并更新 npm 12.1.0、OpenSSL 4.1.0 及多项依赖。
- 💻 发布物：提供 Windows、macOS、Linux、AIX、ARM64 等安装包和源码，macOS Intel 二进制“即将推出”，并附带 SHASUMS 与 PGP 签名。

---

### [发布 v31.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v31.0.0)

**原文标题**: [Release v31.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v31.0.0)

jsdom v31.0.0 发布，包含多项破坏性变更与能力升级：canvas 图像后端迁移至 `@napi-rs/canvas`，CSS 解析/选择器/计算样式改用新集成实现，HTML/XML 解析会在阻塞脚本处暂停，并伴随大量脚本、资源加载、焦点与文档写入相关修复。

- 🚀 **版本发布**：v31.0.0 为最新版本，由 domenic 于 11 月 4 日发布。
- 🎨 **Canvas 后端迁移（破坏性）**：可选 canvas/图像解码后端从 `canvas` 改为 `@napi-rs/canvas`；需安装 v1.0.13+ 的 v1.x 版本，单独安装 `canvas` 不再启用支持，渲染与编码结果可能不同。
- 🖼️ **Canvas 功能与修复**：新增 WebP 序列化（`toDataURL()`/`toBlob()`）；修复图像解码等待、过期请求丢弃、尺寸变化重复请求、失败图像绘制旧内容，以及上下文/序列化/MIME/空画布异步 `null` 等行为。
- 🎯 **CSS 引擎升级**：采用新的集成实现，扩展并加速选择器查询与重复样式读取；支持级联层、嵌套、`@scope`、`@property`/`CSS.registerProperty()`、类型化 `attr()`、`if()`、Shadow DOM 样式、伪元素计算样式及可构造样式表。
- 🧩 **CSS 修复**：修复大量级联、简写、序列化、默认样式问题；计算声明会随 DOM 与样式表变化保持实时更新，序列化与计算值可能与旧版不同。
- ⏸️ **HTML/XML 解析行为变化（破坏性）**：解析会在阻塞脚本处暂停，等待所需资源；`JSDOM`、`fromURL()`、`fromFile()` 可能返回部分解析文档，应等待 `DOMContentLoaded` 或 `load`，并先检查 `document.readyState`。
- 🧾 **XML 异步错误**：异步解析恢复后遇到的 XML 语法错误会通过虚拟控制台以 `"xml-parsing"` 报告。
- 🪟 **新增 API**：加入 `window.reportError()`，可派发 `error` 事件并向虚拟控制台报告未取消错误；新增 `element.ariaBrailleLabel` 与 `ariaBrailleRoleDescription`。
- 📄 **文档与脚本修复**：`load` 仅在 window 触发；修复 `document.open()/write()/close()`、动态脚本 `async=false` 顺序、脚本准备时源文本/文档、跨文档采用、惰性片段脚本执行等行为。
- 🔄 **资源与生命周期修复**：修复图片/样式表/框架被脚本延迟、嵌套样式表导入完成事件、循环导入、Shadow DOM `<style>` 加载、`window.stop()` 取消请求、重复 `document.close()`、iframe 加载事件及内存泄漏。
- 🎛️ **焦点与序列化修复**：修复元素变为不可聚焦后的焦点保留、`document.hasFocus()` 时序、XML 文档 `<template>` 解析/序列化，以及 `rect.toJSON()`/`performance.toJSON()` 在方法 realm 中创建结果对象。

---

### [宣布 Parcel 3 alpha](https://v3.parceljs.org/blog/v3-alpha/)

**原文标题**: [
      Announcing Parcel 3 alpha
    ](https://v3.parceljs.org/blog/v3-alpha/)

Parcel 3 首个 alpha 发布，核心从 JavaScript 全面重写为 Rust 原生二进制，主打最高 100 倍构建提速、显著降低内存占用，并新增原生插件、内置语言支持、集中配置、更智能的代码拆分和库构建能力。

- 📅 2026-11-04 发布 Parcel 3 首个 alpha，完全用 Rust 重写，不再依赖 Node。
- ⚡ 相比 Parcel 2 最高快 100 倍；基准中 Storybook 快 29 倍、文档站快 108 倍、库构建快 49 倍。
- 🧠 内存占用大幅下降：Storybook 少 5.1 倍、文档站少 6.6 倍、库构建少 2.5 倍。
- 🚀 架构优先优化冷构建，减少磁盘缓存开销和失效问题，同时保留内存增量重建。
- 📦 内置 HTML、CSS、JS、TS、SVG、图片优化、RSS/Atom、Web Manifest 等常见能力。
- 🆕 新增原生 Tailwind 支持（无需 PostCSS）、React Compiler、MDX、SVG→JSX 和 glob imports。
- 🛠️ 开发体验增强：可信 HTTPS、本地证书、`--open` 复用浏览器标签页、内置 bundle analyzer。
- ▶️ 新增 `parcel run`，可构建并运行 Node.js 入口，支持 HMR，适合 React Server Components。
- 🧩 支持 Rust、Go、Swift、C 等语言编写原生插件，通过稳定 C ABI 扩展 Parcel。
- 🟨 支持 JavaScript/TypeScript 插件，基于 QuickJS 的自定义运行时，部分兼容 Node 常用能力。
- ⚙️ 将插件配置集中到 `.parcelrc`，减少分散配置文件并提升配置解析性能。
- 📉 更智能的打包算法：450 页站点每页 HTTP 请求少 64%、传输字节少 10%。
- 🌳 Tree shaking 改进：支持 SVG，移除 scope hoisting 以降低 bug 面并支持 top-level await。
- 📚 库模式增强：自动读取 `package.json#exports`，并行构建多目标，每个模块单独输出便于消费方 tree shaking。
- ⚠️ 暂不支持 TypeScript `.d.ts` 生成，压缩插件、自定义 bundler 插件、JavaScript API 等仍在开发中。
- 💾 二进制小于 30 MB、零 npm 依赖，比 Parcel 2 总安装体积约小 4 倍。
- 🧪 可通过安装 `parcel@next` 试用，或安装 `@parcel/parcel3` 使用 `parcel3` 命令与 v2 并行测试。

---

### [Rspack 2.3 发布 - Rspack](https://rspack.rs/blog/announcing-2-3)

**原文标题**: [Announcing Rspack 2.3 - Rspack](https://rspack.rs/blog/announcing-2-3)

Rspack 2.3 已于 2026 年 10 月 29 日发布，重点包括集成 SWC Next 解析器、提升构建性能、降低内存与产物体积、引入实验性新缓存和 Loader 缓存，并增强内置 CSS 与整个 Rstack 生态。

- 🚀 Rspack 2.3 核心更新包括 SWC Next 集成、构建提速、内存和 bundle 体积优化、新实验缓存、Loader 缓存及内置 CSS 改进。
- ⚡ SWC Next 使用扁平 ESTree AST，原生解析最高快 3 倍，JavaScript API 解析最高快 10 倍；Rspack 已采用该解析器，three.js 解析时间降 14%，React 10k 降 6%。
- 🧠 内存优化显著：真实项目构建峰值 RSS 降 27.4%，构建后 RSS 降 36.5%；开发启动峰值降 33.8%，稳态降 34.8%；整体构建性能约提升 5%，大型项目最高提升 20%。
- 📦 SplitChunks 新增 `dedupDepth`（生产模式默认 `1`）和 `minRemainingSize`，并改进模块去重，减少重复代码与输出体积；两个大型项目 Brotli 体积分别降 2.4% 和 9.9%。
- 🗄️ 新实验缓存 `experiments.newCache` 按构建任务存储结果，降低磁盘占用约 79%、冷构建峰值内存约 16%，减少缓存写入对编译的阻塞，并提升开发与生产构建间的复用性。
- 🧩 Loader 缓存可细粒度缓存单个 Loader 的转换结果，适合 `babel-loader`、`less-loader` 等昂贵 Loader；测试中构建时间从 63.8 秒降至 11.2 秒，约 5.7 倍加速。
- 🔍 新增 `module.rules[].use.codeFilter`，先在 Rust 侧检查代码内容，仅在需要时调用 JavaScript Loader；10,000 个模块测试中 Loader 调用减少 90%，构建时间降低约 23%。
- 🎨 内置 CSS 改进 CSS Modules 作用域、组合、值引用和嵌套选择器；支持 CSS-only 入口生成独立 CSS 文件，以及 `css-import`、`asset-url` externals 和 `rspackIgnore` 注释。
- 🛠️ 其他改进包括按需编译减少冗余构建、原生 watcher 兼容 `ts-loader`/`vue-loader`、改进忽略规则和文件检测、增强 webpack 插件钩子兼容与类型定义，并新增 `output.wasmStreamingFallback`。
- 🌐 Rsbuild 生态更新：支持 TanStack CLI 创建 TanStack Start 项目、新增 Lynx Rsbuild 插件、支持 Brotli 压缩体积报告、默认使用 compact-hashed ID 等。
- 📚 Rslib 1.0 发布，支持 `?inline` 内联 Wasm 模块，并可用 TypeScript 7.1 Beta 生成类型声明及支持 Content Mappers。
- 🩺 Rsdoctor 2.0 发布，推荐使用 Agent CLI 进行 AI 辅助分析；安装体积降 56%、分析时间降 57%、开发模式 HMR 时间降约 47%。
- 🧪 Rstest 增强浏览器模式 API 和截图测试，新增 `pressSequentially()`、React hydration 配置及 `toMatchScreenshot()` 视觉回归测试。
- 📖 Rspress 2.1.0 默认支持 WebMCP，提供站点信息查询、文档搜索和页面导航工具，并支持通过 `useWebMcp` 注册自定义工具。

---

### [](https://vitest.dev/blog/vitest-5-1)

**原文标题**: [Vitest 5.1 is out! | Vitest](https://vitest.dev/blog/vitest-5-1)

Vitest 5.1 于 2026 年 11 月 2 日发布，重点带来更精准的测试筛选、交互式快照审查、默认失败追踪、浏览器模块 Mock 性能提升，以及覆盖率、假计时器和测试报告能力增强；多项新功能为实验性，部分默认行为有所调整。

- 🚀 新增实验性 `--since-last-run`：根据上次运行记录的依赖文件修改时间，只运行受影响测试，不依赖 Git，适合 AI 编码代理反复跑测试。
- 🖼️ 新增交互式快照审查：watch 模式下按 `i` 逐个查看失败快照，按 `a` 接受、`r` 拒绝，支持内联快照、`.snap`、文件快照和 ARIA 快照。
- 🧭 Trace View 稳定并默认启用 `'failure-only'`：仅失败浏览器测试保留步骤和失败时 DOM 快照，可在浏览器 UI、Vitest UI 和 HTML reporter 中查看，并支持切换 ARIA 树视图。
- 🧵 新增实验性 `experimental.traceTimeline`：Node 测试失败时展示 `expect.poll`、`vi.waitFor`、`vi.waitUntil` 的等待步骤与耗时；`vi.waitFor` 和 `vi.waitUntil` 新增 `message` 选项。
- 🔁 新增 `--last-failed`：从结果缓存读取上次失败测试并只重跑它们，可按完整测试名组合筛选。
- ⚡ 浏览器模式模块 Mock 改用 import map（实验性 `browser.importMapMocks`），避免拦截网络请求；基准中 Mock 场景耗时降低约 52%，混合场景降低约 38%。
- 🖱️ 新增实验性 `userEvent.pointer`：支持按下、移动、释放等底层指针操作，可用于将元素拖拽到精确位置。
- ⏱️ 新增 `fakeNodeBuiltins`：让 `node:timers` 和 `node:timers/promises` 也支持假计时器；`vi.setSystemTime` 支持 `Temporal.Instant` 和 `Temporal.ZonedDateTime`；浏览器定位器操作会推进假计时器。
- 📊 新增 `TestCase.attempts()`：分别返回每次重试或重复运行的状态、错误和耗时；默认报告会合并多次失败尝试的头部。
- 🎨 覆盖率改进：HTML 报告新增明暗主题并跟随系统；istanbul 插桩改用 Oxc 和 magic-string，速度提升 5–10 倍；v8 新增 `coverage.ignoreNode`。
- 🚀 性能改进：`isolate:false` 下复用 worker 缓存、加速 `toEqual` 类型化数组比较、优化 Firefox Trace View，并改进浏览器模式高负载下的 WebSocket 调度。
- 🔧 其他变更：浏览器模式默认端口改为 `23315`，`api.port: 0` 可让系统选择空闲端口，浏览器测试无法连接服务器时会直接失败而不再无限等待。

---

### [8.1.0 发布：字节与文本导入、Source Map 范围映射以及 ESLint 配置 · Babel](https://babeljs.io/blog/2026/11/02/8.1.0)

**原文标题**: [8.1.0 Released: bytes and text imports, source map range mappings, and ESLint configs · Babel](https://babeljs.io/blog/2026/11/02/8.1.0)

Babel 8.1.0 已于 2026 年 11 月 2 日发布，是 Babel 8.0.0 之后的首个次要版本。此次更新重点加入 Import Bytes/Text 与筛选命名空间转换、实验性 source map range mappings，并扩展解析器和 ESLint 插件支持。

- 🚀 新增 `@babel/plugin-proposal-bytes-modules` 和 `@babel/plugin-proposal-text-modules`，支持通过 `import ... with { type: "bytes" / "text" }` 导入原始字节或文本，并根据 `targets` 编译为 `fetch`、`require` 等目标平台加载方式。
- 🧩 新增 `@babel/plugin-proposal-filtered-namespaces`，支持 deferred re-exports 提案中的筛选命名空间语法，将其编译为命名导入和类似模块命名空间的对象；暂不支持与 `import defer` / `export defer` 组合使用。
- 🗺️ 新增实验性 `sourceMapRanges` 生成器选项，可生成 range mappings 以减少 source map 体积；需确保后续工具和浏览器开发者工具支持，且与 `inputSourceMap` 同用时当前会被忽略。
- 🧪 `@babel/parser` 新增对多个 TC39 提案的解析支持：deferred re-exports、`import.sync` 和非共享 `structs`，但目前仅支持解析，尚不支持转换。
- ✅ `@babel/eslint-plugin` 新增 `configs.recommended` 和 `configs.all`，可与 `@eslint/js` 对应配置配合使用，替换部分 ESLint 规则以兼容 Babel 支持的实验性语法。
- 🤝 Babel 为志愿者驱动项目，文章呼吁通过 Open Collective 捐赠或直接参与 ECMAScript 新提案的实现。

---

### [](https://github.com/trpc/trpc/releases)

**原文标题**: [Releases · trpc/trpc · GitHub](https://github.com/trpc/trpc/releases)

该页面是 tRPC GitHub 仓库的 Releases 页面，集中展示从 v11.14.1 到 v11.24.0 的版本更新记录，内容涵盖客户端、服务端、React Query/TanStack Query、WebSocket/SSE、OpenAPI、Next.js、依赖升级、CI 发布流程及社区贡献等修复和新特性。

- 📦 **版本发布概览**：发布列表包含 v11.24.0、v11.23.0、v11.22.1、v11.19.0 等多个版本，并支持查看标签、比较版本和分页浏览历史发布。
- 🆕 **v11.24.0 最新版本**：11 月 3 日发布，重点修复 TanStack React Query 订阅状态、客户端 transformer 错误、React Query 服务端辅助函数游标传递、WebSocket 退避、SSE 解码错误、批量校验错误、Fastify `maxBodySize` 和 WebSocket `maxBatchSize` 等问题，并新增 Next.js App Router 缓存标签层级子路径与 HTTP URL 路径分隔符选项。
- 🚀 **v11.23.0**：11 月 2 日发布，改进 React Query 无限查询游标注入、`createTRPCReact` 代理类型、TanStack React Query 5.105 类型支持、405 响应 `allow` 头、`Content-Type` 覆盖、`basePath` 兼容性，并将 `unstable_localLink` 重命名为 `localLink`。
- 🛠️ **v11.22.1**：10 月 31 日发布，包含大量 CI/发布流程修复、依赖更新、服务端流取消与序列化修复、React Query 查询键与 `skipToken` 修复、WebSocket/SSE 连接清理等，并有 20 多位新贡献者参与。
- 🔧 **v11.19.0**：9 月 16 日发布，修复 JSONL 流取消、WebSocket 操作信号、HTTP 请求取消、订阅任务清理、懒加载路由匹配等问题，同时升级 Node、pnpm、TypeScript、ESLint、Prettier、Vitest、Turbo、Docusaurus 等工具链。
- 🌐 **v11.18.0**：6 月 18 日发布，为 OpenAPI 增加服务器 URL 支持，并为 TanStack React Query 的 mutation options 增加前缀支持。
- 🧩 **v11.17.0**：4 月 28 日发布，新增订阅类型推断辅助函数，修复流式 `onError` 原因解包、React 19 代理强制转换、私有工作区版本管理等问题，并更新多项依赖。
- 🔄 **v11.16.0**：3 月 28 日发布，重点增强 OpenAPI 循环类型支持，移除类型深度限制 20，支持 `zod.lazy` 的 Standard Schema 回退，并从输出中剥离符号。
- 🧪 **v11.15.x 系列**：3 月发布，新增服务端最大批量大小功能，修复 Node VM 错误处理，并改进赞助商链接的静态 HTML 渲染以利于 SEO。
- 👥 **社区与维护**：多个版本列出新贡献者、贡献者名单、发布资源和反应表情，体现项目持续迭代与社区参与活跃。

---

### [x18n：i18n 文件，已检查并维护](https://x18n.dev/)

**原文标题**: [x18n: i18n files, checked and maintained](https://x18n.dev/)

x18n 是一款用于检查和维护 i18n 文件的工具；它会读取项目中的语言文件和 translate 调用，报告缺失、未使用和损坏的键，并在不破坏原格式的情况下修改语言文件，适用于人工、CI 和编码代理。

- 🧭 无需初始配置即可在项目根目录运行；它会自动从依赖中识别 i18n 库，并定位语言文件。
- 🔍 `x18n check` 可像 `tsc --noEmit` 一样检查缺失、未使用和无效的键；出现错误时以状态码 1 退出。
- 🧾 `x18n get` 可查看某个键在所有语言中的值及代码使用位置；`search` 可根据界面文本反查键；`rename` 可跨语言和代码重命名，并支持 `--dry-run` 预览差异。
- 🖥️ `x18n ui` 可在浏览器中浏览和编辑所有键，同时为代理提供 MCP；`init` 可生成 `x18n.config.ts`。
- 📊 项目状态视图会展示资源、键、用法数量以及各语言的覆盖率。
- 🧩 CLI、VS Code、UI 和代理共用同一配置，并输出一致的诊断结果；VS Code 支持原地显示翻译、跳转定义、查找引用和重命名。
- 🤖 面向代理提供翻译提示、安全写入命令和 MCP 工具，可翻译、检查并清理消息。
- 🏗️ 预设覆盖 vue-i18n、i18next、next-intl、ngx-translate、Laravel、Rails、Flutter 等众多框架，也可通过 YAML 或 TypeScript 插件扩展。
- 🔄 提供 `x18n migrate i18n-ally`，可将 i18n-ally 的设置和自定义框架迁移为 x18n 配置。

---

