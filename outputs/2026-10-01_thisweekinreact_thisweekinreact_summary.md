### [](https://www.skybridge.tech/?utm_source=ThisWeekInReact&utm_medium=newsletter)

**原文标题**: [Skybridge, the full-stack React framework for MCP apps and MCP servers | Claude & ChatGPT](https://www.skybridge.tech/?utm_source=ThisWeekInReact&utm_medium=newsletter)

阿萨德·伊克巴尔（Asad Iqbal）是 Noodle Seed 的首席技术官，他高度评价 Skybridge 模板的结构，称其在过去 24 小时内帮助自己从模板仓库快速打造出三个面向合作伙伴的生产级演示，并且与 Claude Opus 和 Codex 配合使用时非常容易上手。

- 👨💼 人物身份：Asad Iqbal，Noodle Seed 首席技术官
- ⏱️ 效率惊人：过去 24 小时内，从模板仓库推进到三个生产级演示
- 🤝 应用场景：这些演示面向合作伙伴
- 🏗️ 模板评价：Skybridge 模板结构出色、设计优雅
- 🤖 工具协同：非常容易结合 Claude Opus 和 Codex 使用

---

### [](https://www.skybridge.tech/)

**原文标题**: [Skybridge, the full-stack React framework for MCP apps and MCP servers | Claude & ChatGPT](https://www.skybridge.tech/)

Asad Iqbal（Noodle Seed 首席技术官）高度评价 Skybridge 模板，称其结构出色，借助 Claude Opus 和 Codex，在 24 小时内从模板仓库快速构建出三个面向合作伙伴的生产级演示。

- 👤 发言者：Asad Iqbal，Noodle Seed 首席技术官
- ⏱️ 成果：24 小时内从模板仓库完成三个生产级演示
- 🤝 用途：这些演示面向合作伙伴
- 🏗️ 评价：Skybridge 模板结构出色，易于复用
- 🤖 工具：与 Claude Opus 和 Codex 搭配使用非常轻松

---

### [](https://github.com/alpic-ai/skybridge)

**原文标题**: [GitHub - alpic-ai/skybridge: Skybridge is a full-stack TypeScript framework for MCP Apps and ChatGPT Apps. Type-safe. React-powered. Platform-agnostic. · GitHub](https://github.com/alpic-ai/skybridge)

Skybridge（alpic-ai/skybridge）是一个开源全栈 TypeScript/React 框架，用于构建 MCP Apps 与 MCP Servers，帮助开发者为 Claude、ChatGPT、VSCode 等支持 UI 的 MCP 客户端打造类型安全、可交互的应用。

- 🧩 核心定位：为 MCP Apps 和 MCP Servers 提供完整 React 全栈开发框架，抽象原始 SDK 的低层复杂度。
- 🌐 跨平台运行：一次编写，可在 Claude、ChatGPT、VSCode 及其他兼容 MCP 的客户端中运行。
- 🛠️ 开发体验：提供本地模拟器、HMR 热更新和永久隧道，方便把本地应用连接到 Claude 与 ChatGPT。
- 🤖 Agent 友好：包含 skills、CLI 与程序化开发工具 API，支持编码代理端到端构建 MCP 应用。
- 🔒 类型安全：类 tRPC 推理，从 MCP server 工具定义贯通到 React 视图，实现服务端到前端类型安全。
- ⚛️ React 优先：提供类 React Query 的 hooks 和高级状态管理。
- 📦 快速开始：人类可用 `npm create skybridge@latest my-app`；Agent 可运行 `npx skills add alpic-ai/skybridge -s skybridge`。
- 📚 文档完善：覆盖基础概念、核心概念、指南、API 参考与完整部署路径。
- ☁️ 部署选项：可在 Alpic 即时部署，支持 MCP 分析、永久隧道、应用商店合规审计与提交；也可自托管于 Node.js 平台。
- 🧪 示例丰富：包含综合 playground，以及电商、旅行、SaaS、游戏、教育等 ChatGPT/Claude 就绪模板。
- 🔐 Auth 示例：提供 Descope、Clerk、WorkOS AuthKit、Stytch、Auth0、Authplane 等 OAuth 认证示例。
- 🎨 UI 示例：包含 Manifest UI、Generative UI、mcpcn 等代理组件库与生成式 UI 方案。
- 👥 社区贡献：可通过 GitHub Issues、Discord、PR 参与，并有贡献指南、行为准则和安全政策。
- 📄 开源许可：MIT License，由 Harijoe、Fred Barthelet 与 Alpic 团队维护。
- ⭐ 仓库数据：约 2.1k stars、140 forks、8 watchers、969 commits、37 issues、20 PR、20 discussions。
- 🏷️ 主题标签：涵盖 agent、AI、apps-sdk、ChatGPT、Claude、MCP、React、TypeScript、skills、tooling 等。

---

### [Panda CSS 2.0 | Panda CSS 博客 - Panda CSS](https://panda-css.com/blog/panda-css-v2)

**原文标题**: [Panda CSS 2.0 | Panda CSS Blog - Panda CSS](https://panda-css.com/blog/panda-css-v2)

Panda CSS 2.0 正式发布，最大的变化是编译器完全用 Rust（基于 Oxc）重写，但样式 API 保持不变；性能大幅提升，同时带来可发布设计系统、新工具函数、官方 ESLint 插件等新特性，升级需注意 ESM-only、Node 22+ 及若干配置与 CSS 输出变更。

- 🚀 **核心重写**：编译器从 Node/TypeScript（ts-morph）迁到 Rust + Oxc，CLI 与打包器用原生绑定，浏览器用约 490 KB 的 WASM 绑定，管线为 extract → encode → emit。
- ⚡ **性能飞跃**：抽取快 15–37 倍；watch 模式重新解析快约 360 倍（每文件 650μs 降到 2μs 以内）；staticCss 在 29,000 条规则配置上从 25.7 秒降到约 0.3 秒，约快 85 倍。
- 🧠 **类型更轻**：生成类型的类型实例化减少约 99%，tsc 内存少 21–25%，类型检查时间减少 40–60%；运行时因记忆化约快 4 倍。
- 📦 **可发布设计系统**：用 `panda lib` 编写并发布 npm 包，消费端通过 `designSystem` 字段接入，无需在应用中重新抽取样式，支持跨配置、互相扩展。
- ✨ **新样式工厂**：新增 `viewTransition()`、`firstThatWorks()`、`keyframes()`、`positionTry()`，用于视图过渡、带回退的有序值、组件局部动画与锚点定位回退。
- 🎨 **新预设能力**：内置遮罩（mask）与滚动条（scrollbar）工具类，新增指针、用户校验、`inert` 等条件；变量改用 `@property` 注册，仅在真正使用时输出。
- 🛠️ **CLI 与工具升级**：`panda doctor`、`panda analyze`、`panda debug`、`--profile`、`--include`、`panda init -i` 等；日志统一为 `--log-level`。
- 🧩 **编辑器与 ESLint**：官方 `@pandacss/eslint-plugin` 提供无效 token、硬编码颜色、简写冲突等规则；类型服务插件与 LSP 为 `panda.config.ts` 提供真实补全与诊断。
- 📚 **其他新增**：`@pandacss/preset-typography` 提供 `prose` 配方；MCP 独立为 `npx -y @pandacss/mcp`；Vite、webpack、Rollup、Bun 打包插件支持 `transform: true` 消除运行时。
- 🔄 **升级要点**：Panda 2.0 仅支持 ESM，需要 Node 22+，`panda.config.ts` 基本沿用；hooks 移入 plugins，`createStyleContext` 拆分为 `createSlotRecipeContext` / `createRecipeContext`，`matchTag` 改为声明式 `jsxMatchTag`。
- ⚠️ **移除与输出变化**：删除 `studio`、`eject`、`lightningcss`、`browserslist` 等 9 个配置及模板字符串写法；CLI 合并为 `panda doctor`；边框覆盖按属性而非源码顺序排序，`scrollbarWidth` 改为关键字取值。
- 🧱 **渐进迁移提醒**：Panda 的 CSS 位于 `@layer` 中，未分层的旧样式会默认胜出；可运行 `postcss-cascade-layers` 去掉层级包装，或按路由、目录、团队划清边界。

---

### [](https://panda-css.com/blog/zero-runtime-all-the-way-down)

**原文标题**: [Zero runtime, all the way down | Panda CSS Blog - Panda CSS](https://panda-css.com/blog/zero-runtime-all-the-way-down)

overview summary
- ⚡ Panda CSS 2.0 的 source transforms 在构建时把 css()、patterns、recipes 重写为类字符串，让样式运行时彻底离开 bundle。
- 📦 在 @pandacss/vite、webpack、Rollup、Bun 插件中开启 transform: true 即可；CLI 和 PostCSS 仍生成 CSS，但因不改写源码而保留运行时。
- 🚀 示例页面从 14.3 KB gzip 降到 0.4 KB，连 token('colors.blue.500') 也被内联为具体值，几乎没有 Panda 代码进入 bundle。
- 🧠 过去“零运行时”只意味着 CSS 在构建时提取，但解析样式对象的 JavaScript 仍会在浏览器每次渲染时运行。
- 🏗️ 模式组件会折叠成实际元素，例如 <Stack> 变成 <div className="d_flex flex-d_row gap_4">，导入和包装组件消失。
- 🎛️ 配方和导入的 cva() 会在构建时解析变体，调用变成类字符串，不再需要读取配方运行时。
- 🔀 运行时值的三元表达式会预先计算两个静态分支，浏览器只负责选择其中一个类字符串。
- 🧷 样式 props 会和外部 className 拼接成字符串，不需要辅助函数或类名查找。
- 🛡️ 真正未知的值仍保留运行时调用，但周围可静态计算的部分会预计算，并通过轻量 cx/__pcx 辅助函数连接。
- 🔧 运行时变体 cva() 会编译成针对该配方的小函数，类名已是字符串，只剩按 props 查找；导出配方仍保留完整 API。
- 🧩 转换按调用点进行，一个不安全用法不会让整个文件回退；只重写 Panda 拥有的标签、模式和 importMap.jsx 中列出的模块。
- ✅ 最佳实践：枚举而非计算；通过 props 传变体名而非样式对象；仅对用户选择、DOM 测量、API 数据等真正未知值使用运行时 css()。

---

### [](https://panda-css.com/blog/typography-preset)

**原文标题**: [Prose styles for HTML you don't control | Panda CSS Blog - Panda CSS](https://panda-css.com/blog/typography-preset)

这款 CSS 排版预设用单一样式解决你无法直接管控的 HTML 内容排版问题，支持 Markdown、CMS 输出和流式文本，本站所有文章均由它渲染。

- 📝 **解决痛点**：站点大部分 HTML 并非你亲手编写——Markdown、CMS 富文本、模型逐字流式输出，都以纯标题、段落、列表、表格形式出现，以往每个项目都得手写样式表
- 🔄 **前后对比更简洁**：过去需要为每个元素写规则并重复暗色模式，如今只需一个 `prose()` 包装器即可搞定
- 🎛️ **仅暴露四个可调旋钮**：尺寸（sm 至 2xl，五档）、节奏（行高与块间距两个自定义属性）、颜色（语义 token 自带明暗值）、宽度（默认六十字符阅读行宽）
- 🎨 **颜色全用语义 token**：`prose.body`、`prose.heading`、`prose.link` 等共二十个，暗色模式零配置，覆盖方式与普通 token 一致
- 🧩 **其余全部手工调校且刻意不开放**：所有选择器都包在 `:where()` 中，用普通 `css()` 即可覆盖，无需 `!important`
- 🌊 **专为流式内容打造**：每个区块只从顶部留白，不依赖 `:last-child`、`:has()` 或 `:empty`，新段落追加时上方内容不会变动、页面不跳动
- 🚧 **保留你自己的组件**：开启 `notProse` 并标记元素，预设会跳过该元素及其内部全部内容，适合放置 Callout、嵌入内容和代码块
- 🚀 **上手简单**：安装 `@pandacss/preset-typography`，在 `panda.config.ts` 的 presets 中引入，运行 codegen，再用 `prose()` 包裹内容即可完成

---

### [](https://panda-css.com/blog/see-your-design-system)

**原文标题**: [See your design system, and what it uses | Panda CSS Blog - Panda CSS](https://panda-css.com/blog/see-your-design-system)

Panda Studio 推出了新功能：上传 design-system.json 即可可视化你的设计系统（颜色、间距、字体等），并新增「代码 token 使用分析」和「链接分享」两项能力，全程无需安装、无需账号、数据不离开浏览器。

- 🎨 **可视化渲染**：把 Panda 生成的 design-system.json 拖进去，颜色变成色卡网格、间距变成排序刻度、字体变成字体样本、时长与缓动变成可动效的标签，无需安装、账号或配置。
- 🔍 **新增功能一：用量分析**：上传源码文件或整个仓库文件夹，即可按类别报告哪些 token 被使用、哪些闲置、哪些高频；闲置列表就是可以删掉的 token。
- ⚙️ **两种统计精度**：若附带 panda.config.ts，真实的 Panda 编译器会通过 @pandacss/compiler-wasm 在浏览器内运行，与构建时提取和解析完全一致；若不提供配置，则改用名称匹配扫描，对具名 token 准确、对纯数字 token 仅近似，报告上会有徽章标明属于哪一档。
- 🔒 **本地运算、不上传**：浏览器里跑的是 Panda 2.0 同款 Rust 引擎编译成的 WebAssembly，数值来自你本机对代码的真实编译，在你点击 Share 之前任何内容都不会离开浏览器。
- 🔗 **新增功能二：链接分享**：点击 Share 会保存 token 并生成 /s/<slug> 只读页面，分享分析结果则附带用量报告（/a/<slug>），接收方看到的已用/未用明细与你完全一致；无需账号、团队或权限归属。
- 📄 **获取文件方式**：运行 `panda codegen --spec` 生成 styled-system/specs/design-system.json，打开 Studio 拖入并点击 Analyze 即可。
- 🛠️ **托管版不取代自建**：Studio 文档仍展示如何用约三十行代码自建查看器（每个类别都是 { name, value }，色卡只是一个 .map()），Studio 只是帮你省去搭建的那一步。

---

### [Next](https://blog.cloudflare.com/vinext-nextjs-on-vite/)

**原文标题**: [Next.js applications, powered by Vite: introducing Vinext 1.0 | Cloudflare Blog](https://blog.cloudflare.com/vinext-nextjs-on-vite/)

Vinext 1.0 正式发布，可将任意 Next.js 应用（Pages Router 或 App Router）迁移并部署到 Cloudflare Workers、Netlify、AWS Lambda 等平台；兼容性超过 99%，并强化缓存、可观测性、预渲染与缓存预热等能力。

- 🚀 Vinext 1.0 发布，目标是让 Next.js 应用可在任何 Web 平台部署，包括 Cloudflare Workers 免费计划。
- 🧪 大幅提升兼容性：同时支持 App Router、Pages Router 与混合应用，关键客户需求测试兼容率超过 99%（不含缓存组件）。
- ⚙️ 覆盖完整页面生命周期：服务端渲染、构建时预渲染、静态导出、页面级 ISR，以及后台和按需重新验证。
- 🗄️ 提供跨 App/Pages Router 与运行时的统一缓存函数，并支持 Cloudflare Workers Cache。
- 🔍 提供 Next.js 兼容的 tracing，兼容 OpenTelemetry、Sentry，并集成 Cloudflare Workers 原生 Observability。
- 🧩 兼容 `next/*` 公共接口和常见生态模式，如认证、MDX、图片优化、字体、metadata、环境变量等。
- ☁️ 对 Workers 运行时提供一等支持：开发和生产可用 workerd，并直接访问图片优化、Hyperdrive 等 bindings。
- 🛠️ 迁移流程简化：运行 `npx vinext check` 和 `npx vinext init` 即可验证兼容性并配置 Vite 与部署，保留原 Next.js 项目结构。
- 🧊 对 Next.js 16 的 Cache Components 与 `use cache` 仅有限支持，当前重点仍是核心兼容性与稳定性。
- 🔥 新增缓存预热：把预渲染从构建机器迁移到 Cloudflare 网络，先部署到 0% 流量版本预热，再安全提升到生产流量。
- 🤖 持续自动化维护：每日检查 Next.js canary 变更，每晚运行兼容矩阵，并用 agent 定位差异、复现问题、提议修复。
- 📦 可用命令：`npm create vinext-app@latest my-app` 新建应用，或 `npx vinext check && npx vinext init` 迁移；部署用 `npx @vinext/cloudflare deploy --warm-cache`。
- 🌐 开源与文档：访问 `vinext.dev`，源码在 `github.com/cloudflare/vinext`，欢迎 issue、PR、复现与反馈。

---

### [我几乎没怎么看代码，就写出了一个快 70 倍的 SQL 解析器 - Post](https://posthog.com/blog/sql-parser?utm_source=twir&utm_campaign=sept30)

**原文标题**: [I wrote a 70x faster SQL parser while barely looking at the code - PostHog](https://posthog.com/blog/sql-parser?utm_source=twir&utm_campaign=sept30)

PostHog 工程师用多个并行 Claude Code 会话重写 SQL 解析器：旧版是基于 ANTLR/C++ 的生成式解析器，新版是 Rust 中“手写”风格的高性能递归下降解析器，输出 AST 与源位置完全一致；生产环境平均快 454 倍，笔记本基准约 70 倍，并形成了一套由属性测试、语法生成、覆盖率引导和 shadow mode 组成的开发闭环。

- 🧩 PostHog 需要 SQL 解析器，把用户 SQL 转译为 ClickHouse SQL，以提供逻辑数据视图、性能优化和访问控制；解析器首先处理不可信输入并生成 AST。
- 🐢 旧解析器由 ANTLR 从 `.g4` 文件生成 C++ 代码，灵活但运行时依赖 ATN/图解释和动态 lookahead，因此速度受限。
- 🤖 作者用多个长期运行的 Claude Code 会话并行重写，最终产出 16K 行“手写”解析器代码、5K 行工具和数千行测试。
- 🧪 两条路线并行推进：一条追求性能，采用递归下降 + Pratt 表达式循环；另一条尽量复刻 ANTLR 行为，但把状态转移显式写成代码。最终两者都可行。
- 🎯 以旧 C++ 解析器作为 oracle，采用测试驱动开发：找到新旧解析器分歧、修复新解析器、重复，目标是对现实查询完全一致。
- 🔍 用 Hypothesis 做属性测试，并基于 ANTLR 语法生成 SQL 生成器；还加入 token 置换、括号扰动、生产匿名查询、ShrinkRay 最小化和覆盖率引导生成来发现边界用例。
- 🛠️ Claude 常做脆弱修复，例如 lookahead 从 1 个 token 改成 2 个 token；解决办法是让它在修改前加载语法文件和相关 C++ 源码，并让后台 PBT 持续产出失败用例供其领取。
- 🔁 最终迭代循环为：生成失败用例 → 加入回归套件 → 读 grammar/C++ 思考通用修复 → 修改并总结 → 跑回归 → 自主重复。
- 🚀 新解析器在 shadow mode 下与生产旧解析器并行比较，数百万次解析零分歧；原计划跑几天，但几小时后即切换生产流量，并保留 0.1% reverse shadow。
- 📈 新版与旧版输出 AST 和源位置完全相同；生产查询平均快 454 倍，标题中的 70 倍来自笔记本基准，因为生产环境多为更长 SQL，较少命中解析器缓存。
- 🧠 作者认为这不是“vibe-coded”：PBT、基于语法的代码生成和覆盖率引导接近 parser fuzzing 前沿；未来可能由解析器生成器提供 oracle，LLM 用 PBT/模糊测试“手写”高性能解析器。
- 🦀 技术形态是 Rust 编写的预测式递归下降解析器，带 Pratt 表达式核心、LL(2) 游标与局部受限非消费 lookahead，以及必要的有序选择回溯；完全由 Claude Opus 4.7 于 2026 年 5 月完成。

---

### [2026年9月安全版本发布 | Next.js](https://nextjs.org/blog/september-2026-security-release)

**原文标题**: [September 2026 Security Release | Next.js](https://nextjs.org/blog/september-2026-security-release)

overview summary
- 🔐 Next.js 发布 2026 年 9 月安全更新，修复此前因上游依赖延迟而推迟的关键与高危漏洞，并涵盖多项中低危问题。
- ⬆️ 更新已发布：v16.3.8（Active LTS）和 v15.5.27（Maintenance LTS），建议尽快升级依赖。
- 💻 升级命令：15.5 使用 `npm install next@15.5.27`；16.3 使用 `npm install next@16.3.8`。
- 🖼️ 高危：Image Optimization 存在 SSRF（CVE-2026-94483 / GHSA-cjq9-62q9-8jv4），攻击者控制的允许远程 URL 可能访问私网；未配置 `images.remotePatterns` 则不受影响。
- 🧪 中危：自托管 Pages Router 的 SSG/ISR 页面可能被缓存投毒（CVE-2026-94543 / GHSA-4jqv-mc3x-m676），不同路由内容可能替换缓存并错误展示，Vercel 部署不受影响。
- 🧨 中危：SSG/ISR 渲染缓存投毒可导致跨用户内容替换和持久性拒绝服务（CVE-2026-94484 / GHSA-mcj8-r9mp-w47p），根级 catch-all 页面配合 SSG/ISR 可被单个未认证请求污染共享缓存。
- 🖼️ 中危：App Router 元数据图片路由可绕过 `dynamicParams` 导致信息泄露（CVE-2026-94485 / GHSA-f87g-xv8r-7p7x），影响 webpack 构建；Turbopack 构建不受影响。
- 🔑 中危：嵌套 `'use cache'` 函数可能跨根参数值泄露缓存（GHSA-h694-7cp9-m8p3），外层缓存键遗漏根参数，可能返回其他参数的内容；泄露值不受攻击者控制。
- 📝 中危：待处理的 `use cache` 填充可将 Draft Mode 内容泄露到常规响应和持久页面（CVE-2026-94544 / GHSA-3w37-wq28-93x7），影响启用 Cache Components 或 `experimental.useCache` 且提供 Draft Mode 预览的站点。
- 🧑‍💻 低危：`next dev` 的 Model Context Protocol 端点不校验请求来源（CVE-2026-94486 / GHSA-39w2-rjm5-chcv），恶意网站可读取项目路径、源码片段、路由清单和开发日志；仅开发服务器受影响。
- 🛡️ 安全计划：Next.js 安全问题通过 Vercel Open Source Bug Bounty 协作处理，相关问题可联系 `security@vercel.com`。

---

### [React Summit US——美国最大的 React 会议](https://reactsummit.us/?utm_source=thisweekinreact)

**原文标题**: [React Summit US – The Biggest React Conference in the US](https://reactsummit.us/?utm_source=thisweekinreact)

React Summit US 2026 是美国最大的 React 会议，第 4 届将于 2026 年 11 月 17 日和 20 日在纽约举行，采用线下与线上混合形式，聚焦 React 生态、现代 Web 开发及 AI 在开发中的角色。

- 🗽 **定位与规模**：美国最大 React 会议，设 Base Camp 与 Summit 2 个 Track，50+ 讲者，10K+ 全球开发者，约 800 人纽约线下聚会。
- 📅 **核心日程**：11 月 17 日纽约线下+直播，11 月 20 日全远程日；combo 票还可参加 11 月 16 日的 JSNation US 与 AI Coding Summit。
- 🌐 **混合体验**：线下含 networking 与互动娱乐，线上含双 Track 直播、远程技术讨论室和全球 React 社区连接。
- 🧠 **内容主题**：覆盖 React 19、React Compiler、React Server Components、Next.js、Remix、TypeScript、TanStack、Expo、AI 工具链、全栈架构、安全与性能等。
- 🔥 **Deep Dives**：包括 AI 辅助编码、AI 工程、全栈开发与架构、晋升 Senior/Tech Lead 四大方向。
- 🎤 **讲者阵容**：Kent C. Dodds、Shaundai Person、David Khourshid、Josh Goldberg、Mark Erikson、Brad Westfall、Mike Grabowski、Cynthia Wang、Jeff Huleatt 等，更多待公布。
- 🛠️ **工作坊**：11 月 1-30 日提供 PRO 与免费工作坊，涵盖 Modern React Architecture、Product Engineering、Claude Code、Firebase/Google Cloud、Next.js 等。
- 🎟️ **票务价格**：Hybrid Regular $990；React Summit + JSNation + AI Coding Summit combo $1575；含酒店 combo $2800；Remote Early Bird $190；远程三会 combo $230；Multipass + Deep Dives $19/月。
- 💸 **优惠信息**：2 人以上团队享 15% 折扣；早鸟后价格上涨；分享徽章可赢取免费远程票。
- 📍 **举办地点**：Liberty Science Center，位于新泽西州泽西城自由州立公园，拥有西半球最大天文馆。
- 🎉 **特色体验**：曼哈顿景观渡轮、天文馆演讲、美国最大 React 派对、街机游戏与行业社交。
- 🤝 **赞助与社区**：设有 Platinum/Gold/Partners/Tech Partners 赞助体系；可申请赞助、志愿者，并遵守行为准则。
- 📦 **远程权益**：高清互动直播、远程 networking、免费远程工作坊、录制回放、技术讨论室、证书和数字 swag。

---

### [](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

**原文标题**: [Improving site performance by shipping more CSS - The GitHub Blog](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

GitHub 将 github.com 从 CSS-in-JS 全面迁移到 CSS Modules，以解决组件增长带来的客户端与服务端渲染性能问题。迁移通过 feature flag、视觉回归测试和渐进式发布完成，最终在 2026 年 6 月实现 100% CSS Modules，并移除 sx、styled-components 和 styled-system，同时显著提升性能且未中断 GitHub。

- 🚧 2023 年 Primer 组件数量激增，CSS-in-JS 导致首屏加载变慢、SSR 性能下降、样式更新失控。
- 🧩 选择 CSS Modules：使用原生 CSS、类名默认局部作用域、无客户端或服务端运行时，样式随 HTML 以 CSS 文件发送。
- 🚩 采用渐进迁移：为组件新增 CSS Modules 文件、用 feature flag 切换新旧样式、用视觉回归测试验证，再逐步向团队、员工和所有用户发布。
- 📈 到 2024 年 12 月，Primer 全部组件完成迁移，SSR 时间减少 55%，组件初始化时间减少 25%。
- ⚠️ GitHub 层面迁移的最大障碍是 sx prop：TypeScript 和设计令牌集成好、与组件共置，但动态内联对象运行时成本高、难以扩展。
- 🧱 创建 @primer/styled-react 包装库，让 sx 用法可继续消费新组件，同时逐步替换为 @primer/react 导入以释放性能收益。
- 🧹 “Styled Box Zero”按包迁移：把 sx 转为 CSS Modules、替换导入、预生产测试并部署；2025 年 4 月启动，峰值约 7,760 个 sx props。
- 🤖 8 名工程师用 6 个月迁移 6,419 个 props，SSR 提升 1%–22%；2026 年 4 月，两名工程师借助 Copilot coding agents 三周将剩余 895 个清零。
- 🧑💻 内部 VS Code 插件和 codemod 协助迁移，styled-components 进入维护模式也印证了迁移方向正确。
- 🎨 随后处理主题：GitHub 七个主题及高对比度模式依赖 styled-components；CSS 变量已在 @primer/css，需移除相关 JS 工具和用法，约两个月完成。
- ✅ 2026 年 6 月 GitHub 100% 使用 CSS Modules，从 dotcom 移除 sx、styled-components 和 styled-system，且未破坏 GitHub。
- 🌟 这次迁移演变为 UI 样式、主题和交付方式的逐步重新平台化，提升了性能、用户体验和可维护性。

---

### [在 Next.js 中重建](https://aurorascharff.no/posts/rebuilding-react-routers-global-hooks-in-nextjs/)

**原文标题**: [Rebuilding React Router's Global Hooks in Next.js | Aurora Scharff](https://aurorascharff.no/posts/rebuilding-react-routers-global-hooks-in-nextjs/)

React Router 的 `useNavigation()`/`useBlocker()` 提供全局路由状态，但 Next.js App Router 没有等价的全路由 hooks；文章讲解如何借助 React 的局部状态模型、`useTransition`、`Link` 的 `onNavigate` 和 Provider，在 Next.js 中重建全局进度条与导航拦截，并讨论覆盖范围与权衡。

- 🧭 React Router 通过 `useNavigation()` 暴露全局导航状态（如 `idle`/`loading`），`useBlocker()` 可阻止导航；Next.js 没有对应的 router-wide hooks。
- ⚠️ 全局状态会让局部反馈与全局导航耦合：详情面板需用 `q` 参数区分搜索导航，提交按钮需比较 `formAction` 判断是否属于自身表单。
- 🧱 React 原则是状态应靠近交互，只有更多组件需要时才提升到共同父级或 Context；Provider 可限定共享范围。
- 🔗 Next.js 提供更小 API：`useLinkStatus()` 读取父 `Link` 的 pending；`useTransition()`/`startTransition()` 管理局部 pending；`onNavigate` 可拦截同源客户端导航。
- ✨ Next.js 16.2 的 `Link` 新增 `transitionTypes`，替代手动使用 `onNavigate` + `addTransitionType` 的动画链接包装器。
- 🧩 重建全局进度条：`NavigationProvider` 用 `useTransition` 持有 `isPending`，`navigate()` 内包装 `router.push/replace`；`AppLink` 用 `onNavigate` 取消默认导航并调用 `navigate()`。
- 📊 `NavigationProgress` 从 Context 读取 `isPending`，在任意 `AppLink`/`navigate()` 导航时显示进度条。
- 🚫 重建导航拦截：Provider 存 `isBlocked`，`navigate()` 中执行 `window.confirm`；脏表单通过 effect 注册 `isDirty`。多个表单应存注册列表而非单一布尔。
- ⛔ 该拦截只覆盖 `AppLink`/`navigate()`，无法覆盖普通 `Link`、直接 `router.push()`、浏览器前进后退；`beforeunload` 只覆盖刷新/关闭标签页。
- 🔄 同样模式可用于搜索参数过滤和乐观更新：如 `FilterProvider`、`CalendarEventsProvider` 集中共享 URL/待处理状态。
- ⚖️ 结论：Next.js 遵循 React“状态就地启动、按需上移”的模型；Provider 方案对进度条容易接受，但对拦截器因覆盖不全可能丢失用户工作而更需谨慎。

---

### [Props 不是设计系统](https://vitonsky.net/blog/2026/09/18/design-system/)

**原文标题**: [Props Are Not a Design System](https://vitonsky.net/blog/2026/09/18/design-system/)

本文核心论点是：把任意样式通过 props 或工具类在调用处传入，并不能形成设计系统；应改用具名、可复用的变体与修饰符来管理组件样式，从而保证一致性、语义和可维护性。

- 🎨 多数 UI 套件允许传入任意样式，如圆角、尺寸、颜色或大量 Tailwind 类，这会把每次组件调用变成一次性样式决策，导致界面不一致。
- 🧩 文章将“在调用点决定样式”称为内联；无论用 `style` 属性、样式 props 还是工具类，机制不同但问题相同。
- ⚠️ 这种做法的根本问题包括：无法保证视觉一致性、代码缺乏语义、没有系统支撑、难以维护且容易出错。
- 🏷️ 解决方向是停止在调用处决定样式，改为一次性定义可复用、具名的界面单元。
- 🧱 使用变体（variant）：用语义化名称完整描述组件的所有视觉细节，不依赖外部全局重置或零散样式补充。
- 🎛️ 使用修饰符（modifier）：让受控变化（如 `size`）成为组件 API 的一部分，而不是从外部覆盖变体的逃生口。
- 🧭 当多个修饰符频繁组合出现时，应提炼为新的变体；核心纪律是规定样式决策允许存在于哪里。
- 🛠️ 该规则不依赖具体技术，可用 BEM、CSS Modules、Mantine、Chakra UI 主题 recipes 等方式实现。
- 🌱 坚持此方法会自然形成设计系统，使代码从一次性样式堆叠变成系统。
- 📚 文末延伸阅读还涉及：BEM 不只是 CSS 命名、UI 套件普遍缺少模块化设计、接口与 TypeScript 对代码质量的意义，以及用“是否有意义”改善 UX 等主题。

---

### [我们如何在两周内让 claude.ai 提速 3 倍 / claude.dev 博客](https://claude.dev/blog/how-we-made-claude-ai-faster/)

**原文标题**: [How we made claude.ai 3x faster in two weeks / claude.dev Blog](https://claude.dev/blog/how-we-made-claude-ai-faster/)

Anthropic 在两周冲刺内让 claude.ai 与 Claude 桌面应用核心体验约快 3 倍：他们把性能工作放进单个 Slack 频道，让 Claude 在 150+ 线程中循环执行测量、优化、部署、读取真实数据并用基准锁住成果，人类负责目标、取舍与批准，最终合并 3000+ 变更且无客户事故或回滚。

- 🚀 聚焦占 95% 用户活动的四段旅程：启动应用、开始对话、加载已有对话、发送消息；跨 Web/桌面与产品共 13 项测量。
- 📊 p75 关键结果：claude.ai 首次加载 3.1s→0.55s，桌面冷启动 6.31s→3.33s，Claude Code 新会话 0.8s→0.3s，Cowork 云加载 2.6s→0.73s；几何平均约快 3.1 倍，每天节省数万用户小时。
- 🤖 使用 Claude Tag beta（约 Opus 5.5 级内部模型）发现瓶颈、建立基准、提交 PR、监控部署；人类设定目标、权衡并批准。
- 🧠 起步时用 Datadog MCP 分析确定四个旅程和 13 个可比指标，列出约 20 个手选项目，并按毫秒估算影响；第 3 天即完成 12/13 目标。
- ⚡ 早期优化包括静态 composer 嵌入 HTML、V8 代码缓存、保持 composer 挂载、悬停预取会话、sidebar 重渲染减少 90%。
- 🧪 为摆脱部署节奏限制，采用 Valgrind + `node --predictable` 指令计数、V8 调用数、React commits、样式重算、DOM 变更等确定性实验室基准；若与墙钟不相关则弃用。
- 📉 指令计数案例：消息树组装指令 -48%、墙钟 -78%（4.6x）；状态行扫描指令 -31%、墙钟 -44%（1.8x）；CI ratchet 只允许指标下降。
- 🔁 核心循环：线程指出慢点 → Claude 追踪并建基准 → PR 按风险拆分、用户可见变更加 flag → 部署 → 读取真实数据 → 成功则 ratchet，失败则关 flag 迭代 → 找下一慢点。
- 🧵 横向扩展：同时运行 150+ 线程；单线程可出 50-100 个优化 PR，Claude 会自主开新线程；最忙日 200+ 变更，约 1/3 PR 增加遥测或护栏。
- 🔍 发现的问题包括 composer 输入路径有 6900 个 hooks/900 个 store 订阅、`:root:has()` 每次 DOM 变更加 24ms、遗留 `location.reload()` 每天 50 万隐藏重载、IndexedDB 重复克隆，以及 em dash/UTF-16 导致代码高亮走慢路径。
- 🛡️ 安全护栏：自动审查 + 至少一名人类批准、测试先于优化、短生命周期 feature flag；近 200 个 flag 过半已清理；高风险变更按员工→1%→全量逐步发布。
- 🎨 人类负责 steering：鼓励更大胆、裁决用户可感知的体验取舍、保持线程范围狭窄；例如拒绝为每发送 2ms 收益维护复杂构建插件。
- ⏱️ 侧线做出 120Hz 帧预算：用 DevTools begin-frame 控制实现确定性 8.33ms 预算，长回复主线程阻塞从约 750ms 降至约 200ms、CPU 约 1/3，120Hz MacBook 全程 120fps；流式渲染约 4x 更顺滑。
- 🌐 后续：当前约比 8 月初快 3 倍，ratchet 会维持成果；p95、其他旅程和超长对话仍有优化空间，并会分享对 Electron、Chromium、Node.js 等的上游贡献。

---

### [AI、开源，以及通往 TanStack Charts 的漫漫长路——Tanner Linsley](https://tannerlinsley.com/posts/ai-open-source-and-the-long-road-to-tanstack-charts)

**原文标题**: [AI, Open Source, and the Long Road to TanStack Charts â Tanner Linsley](https://tannerlinsley.com/posts/ai-open-source-and-the-long-road-to-tanstack-charts)

Tanner Linsley 回顾了自己从 Chart.js、react-charts 到 TanStack Charts 的图表库历程，以及如何借助 AI 在几小时内做出首个可运行版本、不到一周进入实验性 alpha。他还讨论了 AI 对开源的冲击、人类经验与库选择的重要性、代码审查方式，以及 TanStack 生态的后续计划。

- 🏃 谈话起因：他在跑步时开 Twitter Space，约 71 分钟聊图表库历史、AI、开源和开发乐趣；音频问题由 Kevin 帮忙解决。
- ❤️ 他仍热爱创造：理解 AI 让资深程序员不安，因为身份常与写代码速度绑定；但 AI 让他不必手工实现每个细节，能更专注于想法和 API。
- ⚔️ 他把 AI 比作 50 英尺光剑：能高效推进，也能制造混乱；开源中低质量贡献的问题早已存在，AI 只是放大了数量，判断力不会自动变好。
- 📈 图表经验始于 Nozzle：他用过 D3，参与 Chart.js 2.0 维护，并学到自己不想一直直接写 Canvas API。
- ⚛️ 因 React 的声明式理念创建 react-charts：React 负责渲染，D3 负责计算与布局，追求“给数据就出图”，但自动边距、标签、旋转文本等隐藏工作很多。
- 🔍 他长期研究 D3 源码、Grammar of Graphics、Observable Plot 等，形成对 API、数据模型和渲染的明确偏好，也积累了许多痛点。
- 🤖 用 AI 构建 TanStack Charts 时并非从零开始：几小时出首版，不到一周实验性 alpha，未手写代码；但仍投入类型安全、场景图、响应式、文档、测试、迁移与优化。
- ⚡ 早期反馈积极：更灵活、包更小、图表更快；朋友让 agent 迁移试用。他也承认 token 和金钱能换回实现时间，自己不想整夜思考图表几何。
- 🧩 他不会用 AI 重写所有 TanStack 库：Router、Start、Table、Form 的类型和复杂度仍需帮助；Charts 适合当前工具能力，并继承 D3、Chart.js、Observable Plot 等前人经验。
- 📚 开源仍然关键：库承载多年教训，不应让每个 agent 从 SVG 和数学重新发明；知道何时使用 TanStack DB、Virtual 等库像“魔法词”，背后是经验。
- 🔎 代码审查按项目分级：开源库多为人审加 AI 辅助，安全、发布和 CI 严格控制；tanstack.com 更快更松，但数据库迁移仍谨慎。他仍参与，不让自动化决定构建范围。
- 🧪 Charts 依赖测试、集成与浏览器测试、bundle 预算；他批准功能并描述 API，让 agent 实现而不破坏行为或增大包，并追问原因以理解过程。
- 🎮 问答还谈到 Three.js 的基础性、TanStack explore 小游戏，以及 Hotkeys：agent 可能过度包装已有功能，安装正确库只是用好它的第一步。
- 🚀 团队正推动 TanStack 生态稳定，包括计划中的 Start 1.0；他仍享受决定做什么、思考如何工作，并让想法对他人有用。

---

### [](https://nitayneeman.com/blog/how-to-sync-a-design-system-with-claude-design/)

**原文标题**: [How to Sync a Design System with Claude Design | Nitay Neeman's Website](https://nitayneeman.com/blog/how-to-sync-a-design-system-with-claude-design/)

本文解释如何通过 `/design-sync` 将 React 设计系统同步到 Claude Design，创建一份编译后、自渲染的组件库“镜像”，让 Claude 使用真实组件而非仿造组件；并以 shadcn/ui、Tailwind v4 和 Storybook 为例，覆盖镜像内容、验证评分、配置步骤、常见失败与最佳实践。

- 🧠 Claude Design 是 Anthropic 内置于 Claude 的设计工具，可将提示词转成屏幕、原型、幻灯片或单页，并可在对话、claude.ai/design 或 Claude Code 的 `/design` 中使用。
- ⚠️ 它默认不了解你的设计系统，会重新发明 Button 等组件，生成手写样式的新按钮，导致开发者仍需重建。
- 🪞 设计同步会在 Claude Design 内创建“镜像”：组件库的编译、自渲染副本，让 Claude 看到并使用真实组件。
- 📦 镜像不包含源码，而是单个 bundle，内含所有组件、样式表、字体和 React 副本，并附带类型定义、独立预览页和用法指南。
- 🚀 在仓库内用 Claude Code 执行 `/design-sync`，读取 `.design-sync/` 配置，构建并在上传前请求批准。
- ✅ 上传前同步会在真实浏览器中打开每个预览、截图并评分，可发现空白、几乎为空或变体完全相同等问题。
- 📚 Storybook 可选但很关键：stories 会成为预览和参考，Claude 会逐项对比、评分并尽量修复；没有 Storybook 时只能按占位卡和 rubric 判断。
- 🏢 上传后镜像出现在 Claude 账户的 Settings > Design systems；Pro/Max 为个人使用，Team/Enterprise 可发布为组织级，管理员可限制发布、设默认或删除。
- 🧊 镜像是单向快照，不是实时链接；代码变更后需重新运行 `/design-sync`，删除组件也可能残留，需检查文件列表。
- 🛠️ 最小示例使用 Vite + React + TypeScript，安装 Tailwind v4 Vite 插件、shadcn 的 Button/Card/Input、Storybook，以及 Playwright/Chromium。
- 📤 需要自写 `src/index.ts` 统一导出所有组件和 `cn()`；未导出的组件不会进入 Claude Design，也不会警告。类型定义需生成到 `package.json` 指向的 `dist/index.d.ts`。
- 🎨 用 Tailwind CLI 将 `src/index.css` 编译为 `ds.css`；字符串 `@import` 会内联 token，`url()` 导入在上传后失效，可能导致所有 shadcn 组件无样式。
- 🧩 用 `@source inline(...)` safelist 布局工具类，如 grid、gap、max-w、text、hover/dark 等，否则 Claude 写出的布局类不在编译 CSS 中而失效。
- ⚙️ `.design-sync/config.json` 配置包名、入口、globalName、Storybook 目录、buildCmd、cssEntry、extraFonts 和 conventions 文件；首次运行后保存 `projectId`，后续更新同一设计系统。
- ✍️ conventions 文件是成本最低的质量提升：预览展示组件外观，约定说明如何使用，例如不用 theme provider、dark mode 是 class、不要手写样式、用 variant/size、用 `cn()` 合并类名。
- 🧪 运行 `/design-sync` 后，Claude 将每个预览与 story 对比并评为 `match`、`close` 或 `mismatch`；`close` 不是通过，Claude 会尽量修复，但最终仍需人工查看。
- 🧭 常见失败包括：全部无样式、组件正常但布局崩塌、形状对但字体错、组件看似不对其实是预览取景或容器问题。
- 🧱 结果是 Claude 能使用 Card、CardHeader、`Button variant="outline"` 等真实组件，生成与 Storybook 和产品一致的界面，不再手写 div 和一次性工具类。
- 🌐 更大项目要注意：monorepo 中 `entry` 用仓库根路径而 `cssEntry` 相对包目录；多字体需逐项加入 `extraFonts`；若 Storybook 入口用 `url()` 导入 token，应为同步单独创建字符串导入的 CSS 入口。
- 📁 提交 config、conventions、`NOTES.md` 和单独 CSS 入口；忽略 `ds.css`、`dist/`、`ds-bundle/`、`.ds-sync/` 等生成物。
- 💡 结论：上传设计系统本身容易，真正的难点是确保每个组件在 Claude Design 中看起来与产品完全一致。

---

### [Preact 11 – Preact](https://preactjs.com/blog/preact-11/)

**原文标题**: [Preact 11 – Preact](https://preactjs.com/blog/preact-11/)

Preact 11 正式发布，这是基于 Preact X 稳定性的增量升级，带来 Hydration 2.0、自动 ref 转发和 Hook 参数使用 Object.is 比较等新功能；同时通过新大版本集中处理历史破坏性变更，面向现代 Web，并提升未来支持效率。

- 🚀 Preact 11 正式到来，作为 Preact X 的增量更新，延续其稳定性与可靠性。
- ✨ 新特性包括 Hydration 2.0、自动 ref 转发，以及 Hook 参数中的 Object.is 相等性检查。
- 🛠️ “Road to Preact 11” 议题始于六年前，期间 Preact X 的生命周期被大幅延长，许多原本被认为需要破坏性变更的改进也成功落地。
- 📦 现在决定集中打包多年考虑的破坏性变更并发布新主版本，以面向现代 Web、清理未成熟功能，并更高效地支持用户。
- 📘 升级指南包含从 Preact X 迁移到 Preact 11 的全部信息，包括新功能和支持的浏览器版本。
- ⚡ 对多数用户而言升级应简单快捷；多数变化与类型相关，类型更严格，并从更合适的位置导出。
- ✅ 所有第一方包，如 @preact/signals、preact-render-to-string、preact-iso、prefresh 和 @preact/preset-vite，自预发布起已支持 Preact 11，依赖很可能已兼容。
- 💚 Preact 团队感谢多年贡献者，并希望用户像他们一样对 Preact 11 感到兴奋。

---

### [](https://react-resizable-panels.vercel.app/examples/grid-basics)

**原文标题**: [react-resizable-panels | flexible layout components](https://react-resizable-panels.vercel.app/examples/grid-basics)

当前未提供可总结的文本内容，因此无法生成摘要。
- 📄 请在“Use the following content:”后粘贴需要总结的文章、新闻或段落。
- ✍️ 收到内容后，我会按“概览总结 + 带 emoji 的 `-` 要点”格式输出。
- 🌐 摘要将使用中文。

---

### [](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.13.0)

**原文标题**: [Release v2.13.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.13.0)

Redux Toolkit v2.13.0 是一个功能版本，重点现代化构建工具、新增 TypeScript 7 支持，并集中修复 RTK Query、createAsyncThunk、createEntityAdapter 与 combineSlices 的多项问题。

- 🛠️ 构建工具迁移到 TSDown 和 PNPM，并采用 Oxlint、Oxfmt；包布局、exports 与导出 API 仍与 2.12 保持一致。
- 📦 首次通过 PNPM 工作流发布，继续使用 NPM Trusted Publishing，并为每次提交提供 pkg.pr.new 预览包。
- 📚 Redux 文档合并到 redux.js.org，涵盖 Redux core、Redux Toolkit、React Redux 与 Reselect；旧站点重定向，内容去重并更新，RTK 文档位于 /toolkit/。
- 🔷 正式支持 TypeScript 7.0，并纳入 CI 测试矩阵；支持范围更新为 TS 5.6+。
- ⚛️ RTK Query 修复 useQueryState/useQuery 的 selector 记忆化与渲染期间直接读取 store 的问题，并修正 isSuccess 在错误后重新获取时错误翻转。
- 🧭 data 现在能反映 refetch 进行中通过 updateQueryData 产生的缓存更新；轮询按触发时的当前缓存状态读取。
- 🔁 修复重复查询被 thunk condition 拒绝后，排队标签失效过早执行并丢失的问题；falsy id 标签（如 0）可正确失效与清理。
- ♻️ Lazy query hooks 在 Fast Refresh 或 `<Activity>` 等 effect 重启且状态保留时，能够正确重新订阅。
- ♾️ Infinite queries 在超出列表末尾获取时不再触发 onQueryStarted，hook 结果类型加入页面错误标志。
- 🌐 fetchBaseQuery 仅在 URL 以 scheme 开头时视为绝对 URL；修复对无定义 endpoint 名称进行状态 rehydrate 时的错误。
- 🧵 createAsyncThunk 不再吞掉 pending 派发前发生的 abort，并在 rejectWithValue 传入 falsy payload 时正确设置 rejectedWithValue。
- 🗃️ createEntityAdapter 的 setAll 在重复 ID 时保留最后一项，与 setMany 一致；sorted adapter 的 updateMany 会先合并同一 ID 的多次更新。
- 🧩 combineSlices 的 state proxy 缓存改为按实例保存，避免多个 combined reducers 相互干扰；immutability middleware 现在能处理循环引用。
- 🧠 dynamic middleware 在中间件列表未变化时缓存组合后的中间件链；本次发布由 markerikson 于 9 月 29 日发布，并有其他贡献者参与。

---

### [发布 oxlint v1.86](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.86.0)

**原文标题**: [Release oxlint v1.86.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.86.0)

oxc 项目于 9 月 28 日发布 oxlint v1.86.0,该版本距上次发布累计合并 83 个提交,涵盖新特性、错误修复与性能优化,发布状态为不可变(Immutable)。oxc 仓库目前拥有约 22.9k Star、1.3k Fork,以及 581 个 Issue 与 347 个 PR。

- 🚀 新特性:react/only-export-components 规则支持 allowCompoundComponents 选项;新增 typescript/no-generated-empty-object-type 规则
- 🐛 错误修复:no-unnecessary-parameter-property-assignment 现已考虑参数属性的重新赋值情况
- 🐛 错误修复:eslint/one-var 在拆分声明时保留 declare;require-await 将 await using 计为 await
- 🐛 错误修复:react-compiler 支持递归函数表达式,并将无参数的 new Date 视为非纯操作
- 🐛 错误修复:oxlint 在仅类型检查模式下跳过类型感知规则,并在 CFG 遍历中跳过 undefined 子节点
- 🐛 错误修复:parser 支持处理 HTML 注释值
- 🐛 错误修复:node/no-exports-assign 从 style 调整为 suspicious 类别;import/no-duplicates 可区分导入属性
- 🐛 错误修复:unicorn/prefer-spread 不再检查字符串 split 调用
- 🐛 错误修复:no-unused-vars 遵循数组剩余绑定中的忽略模式,并识别被消费的更新表达式
- 🐛 错误修复:prefer-const 忽略内嵌赋值;unified-signatures 与上游规则对齐
- ⚡ 性能优化:no-unused-vars 在不存在序列检查时跳过相关判断
- ⭐ 社区反响:该版本获得 7 个 👍、2 个 ❤️ 与 2 个 🚀 反应,共 10 人参与互动

---

### [Vinext 1.0——Next.js 的全新替代方案——YouTube](https://www.youtube.com/watch?v=eFFH_4aD6Ig)

**原文标题**: [Vinext 1.0 - A New Alternative to Next.js - YouTube](https://www.youtube.com/watch?v=eFFH_4aD6Ig)

这是 YouTube 页面底部的导航与法律信息链接列表，涵盖平台介绍、资源入口、政策条款及版权声明。

- 🧭 包含“关于、新闻、版权、联系我们”等基础信息入口。
- 👥 汇集“创作者、广告、开发者”等面向不同用户的资源链接。
- 📜 提供“条款、隐私、政策与安全”等法律与政策相关内容。
- ⚙️ 包含“YouTube 工作原理”和“测试新功能”等平台机制说明。
- ©️ 底部标注版权归属：© 2026 Google LLC。

---

### [Margelo - 应用开发，精益求精。](https://margelo.com/)

**原文标题**: [Margelo - App Development, done right.](https://margelo.com/)

Margelo 是一家专注 React Native 的高端移动应用开发与工程咨询团队，帮助企业更快交付更优质的应用。其开源项目累计下载超 4.6 亿，向 React Native 核心贡献 815 项，代码运行于数十亿设备并支撑数千应用；服务覆盖从创意到上架、AI 集成、团队扩展与相机集成，客户评价集中称赞其速度、专业度和工程能力。

- 🚀 定位：帮助团队更快打造更好的 App，并以低摩擦方式融入客户工程团队。
- 📈 数据：开源项目下载 460,404,887+；React Native 核心贡献 815；客户应用下载 752M+；成功交付项目 192+；团队有 39 名资深开发者。
- 🛠️ 技术贡献与更新：ScrollView automaticallyAdjustKeyboardInsets、新架构可按压性问题修复、iOS Fabric 动态颜色支持、RNGP 禁用 bundle 压缩选项。
- ⭐ 客户口碑：Cosmos、Slingshot、Showtime、MyGroove、Steddy、Steakwallet、Stori、Pink Panda、ExtraCard 等 CEO/CTO 推荐，强调速度快、质量高、像团队一部分。
- 🧭 核心服务：Idea to AppStore，从产品设计到打磨完成的 iOS 与 Android 应用。
- 🤖 AI 集成：帮助团队在开发中使用 AI，并交付设备端 RAG、LLM、人脸识别、语音体验等功能。
- 👥 扩展团队：工程师加入客户团队，加速架构、升级、性能与功能开发，同时保持稳定性。
- 📷 相机集成：作为 VisionCamera 创建者，构建拍照、录像、扫描和实时视觉的高性能相机管线。
- 🧩 技术栈：React Native、Expo、TypeScript、C++、Swift、Kotlin、Objective-C、Java、原生模块、Brownfield 集成、EAS、性能优化、内购、Apple/Google Wallet、AR、AI、Web3、自定义 SDK 等。
- 📝 博客内容：React Native 性能、架构与实战报告；键盘处理指南（2026-05-26，17 分钟阅读）；Discord 新架构性能优化；VisionCamera V5 新特性。
- 📚 开源库：VisionCamera、MMKV、Nitro、Fast TFLite、Quick Crypto、Keyboard Controller、Legend List。
- 🎨 设计能力：为移动应用提供手工打造的产品设计，从早期概念到生产级界面、转场和动画。
- ⚡ AI 提效：通过智能体 AI 与 react-native-skills 加速原型、测试和基准，但所有 AI 辅助改动仍经工程师审查与自动化测试验证。
- 📬 联系与社区：可提交项目需求；并提供公司信息、Discord、GitHub、X、LinkedIn、Instagram 等入口。

---

### [Margelo 如何帮助 Discord 提升 React Native 新架构的性能 - Margelo](https://margelo.com/blog/margelo-discord-react-native-performance)

**原文标题**: [How Margelo Helped Discord Improve React Native's New Architecture Performance - Margelo](https://margelo.com/blog/margelo-discord-react-native-performance)

Margelo 与 Discord 合作定位并修复了 React Native 新架构下 Discord Android 动画卡顿的问题。根因不在单一慢函数，而在 Reanimated、Fabric Shadow Tree、commit hook 与渲染管线之间的复杂交互：大量不必要的 ShadowNode 克隆、React 提交时重复覆盖动画节点、非布局属性仍触发布局开销。通过动画结束后同步回 React、及时清理动画 props 注册表，并安全启用非布局属性同步更新快路径，Discord 新架构 Android 的卡顿帧率降低 26%，动画体验恢复到此前水平。

- 🎯 背景：Discord Android 迁移到 RN 新架构后功能可用，但动画和过渡像“2006 年 PowerPoint”，瓶颈指向 Reanimated v3 与新架构的交互。
- 🧩 Reanimated 支持布局动画、CSS 过渡/动画、shared value 驱动动画；Discord 重度使用 shared value 驱动动画。
- 🔄 JS 侧：useSharedValue 创建 mutable；`opacity.value = ...` 看似同步，实际会把更新调度到 UI runtime。
- 🎬 withTiming 返回动画定义而非普通数值；Reanimated 在 UI runtime 用自有的 requestAnimationFrame 逐帧推进动画。
- 🗺️ useAnimatedStyle 通过 mapper 监听 shared value 并计算新样式；createAnimatedComponent 用 viewDescriptors 注册应接收更新的视图。
- 📦 更新最终经 updateProps 批处理，并通过 JSI 调用 C++ 的 `global._updateProps`。
- ⚙️ C++ 侧 ReanimatedModuleProxy 将更新放入 animatedPropsRegistry，performOperations() 在每帧或原生事件触发时统一应用。
- 🌳 performOperations 调用 `shadowTree.commit()`，再执行 `cloneShadowTreeWithNewProps`，递归克隆受影响 ShadowNode 并合并动画 props。
- 🧱 Fabric 的 Shadow Tree 是原生视图同步源；ShadowNode 是不可变快照，任何更新都必须克隆并提交新的根节点。
- ✅ React 自身更新也走 completeRoot、completeSurface、shadowTree.commit；Reanimated 用 commit hook 在 React 提交前覆盖最新动画值，避免旧值回滚。
- 🐌 性能瓶颈：即使只动画一个视图，也可能克隆数百个 ShadowNode；commit hook 还会在 React 更新时克隆所有注册的动画节点。
- 🎨 另一问题：opacity 等不影响布局的属性仍可能触发 layout pass，每秒 60 次造成浪费；绕过 Shadow Tree 的快路径又曾引发 Pressable 和触摸系统正确性问题。
- 🛠️ 修复方案：动画结束后同步回 React，使节点与 Shadow Tree 一致，并尽早从 animated props registry 移除已稳定节点。
- 🚩 FORCE_REACT_RENDER_FOR_SETTLED_ANIMATIONS 自 v4.3.0 起默认开启，解决主要克隆开销。
- ⚡ 随后重新启用 ANDROID_SYNCHRONOUSLY_UPDATE_UI_PROPS / IOS_SYNCHRONOUSLY_UPDATE_UI_PROPS 快路径，直接同步更新非布局 props。
- 📈 结果：Discord RN 新架构 Android 的卡顿帧率降低 26%，动画性能恢复到接近此前水平。
- 🔮 未来：Software Mansion 与 Meta 将相关能力推进到 RN 核心的 shared animation backend（0.85 起 feature flag），Reanimated 将迁移并进一步提升动画性能。

---

### [DeployPulse | 面向 React Native 的托管 OTA 更新](https://deploypulse.io/)

**原文标题**: [DeployPulse | Hosted OTA Updates for React Native](https://deploypulse.io/)

overview summary
DeployPulse 是面向 React Native 的托管 OTA 更新平台，兼容 CodePush 与 Expo Updates，支持秒级发布、全球边缘分发、自动回滚、灰度发布与 CI 集成，并按月度活跃用户计费。

- 🚀 核心定位：托管 React Native OTA 更新，跳过应用商店审核，推送后数秒内全球上线。
- 🔌 双协议兼容：支持 react-native-code-push 和 expo-updates，同一账户可同时运行两种协议，无需改代码。
- ⏱️ 快速发布：使用 dpctl CLI，例如 `dpctl release-react MyApp ios -d Production -t "1.0.*"`，完成压缩、上传和设备部署。
- 🌍 全球边缘网络：34 个全球边缘区域，服务 130+ 国家；每月 1M+ 设备更新、10TB+ 带宽交付。
- ↩️ 自动回滚：设置错误率阈值，全量安装基础监控，发布异常时自动回滚到上一良好版本。
- 🎯 发布控制：支持按 semver 定位应用版本、按百分比灰度、Production/Staging 环境管理。
- 🖱️ 一键操作：可一键回滚、暂停发布、将测试版本从 Staging 推广到 Production。
- 📊 可观测与协作：实时跟踪下载、活跃安装、错误率和国家分布；支持角色权限与团队协作。
- 🔁 CodePush 迁移：只需将 `serverUrl` 从 App Center 改到 `apps.deploypulse.io`，SDK 和工作流不变，无需重新发布。
- 🔐 代码签名：支持自带密钥，发布时 RS256 签名，设备拒绝被篡改的更新。
- 📱 生态兼容：支持 Bare React Native、Expo prebuild/CNG、EAS Build；Expo Go 不支持 OTA；EAS Update 由 DeployPulse 替代。
- 🧪 CI/CD 集成：支持 GitHub Actions、GitLab CI、Jenkins、Bitrise、CircleCI，一条命令即可从流水线发布。
- 💳 定价模式：按月度活跃用户计费，不按席位；所有层级包含带宽，应用、部署和发布不限量。
- 🆓 套餐范围：免费版 10,000 MAU/100GB/3 个月保留；付费从 $20/月起，最高 Pro $500/月 1.5M MAU/25TB；企业版可定制。
- 📈 超额规则：付费计划带宽超量 $0.01/GB，免费层为硬上限；年付可省 17%。
- 🛠️ 三步开始：`npm i -g @deploypulseio/dpctl`，连接应用并获取部署密钥，然后推送 OTA 更新。

---

### [文本样式属性 · React Native](https://reactnative.dev/docs/next/text-style-props#fontvariationsettings)

**原文标题**: [Text Style Props · React Native](https://reactnative.dev/docs/next/text-style-props#fontvariationsettings)

这是 React Native Next 版本文档中的 Text Style Props 页面，列出 Text 组件可用的文本样式属性；该版本尚未发布，最新稳定文档为 0.87。属性涵盖字体、排版、对齐、装饰、阴影、平台差异和文本选择等。
- 📄 文档状态：Next 为未发布版本，建议参考最新 0.87；页面包含 TypeScript/JavaScript 示例和属性参考。
- 🎨 字体属性：color、fontFamily、fontSize、fontStyle、fontWeight；fontWeight 支持 normal、bold、100–900 或数字，默认 normal。
- 🧬 字体变体与可变字体：fontVariant 可用数组或空格分隔字符串；fontVariationSettings 支持对象或 CSS 字符串，如 `{wght: 500}` 或 `"'wght' 500"`。
- 📏 间距与行高：letterSpacing 调整字符间距；lineHeight 控制文本行基线之间的垂直间距。
- 📐 对齐方式：textAlign 默认 auto，Android 上 justify 需 API 26+，否则回退 left；Android 有 textAlignVertical/verticalAlign，verticalAlign 优先级更高。
- 📱 平台差异：iOS 的 fontFamily 支持 system-ui、ui-sans-serif 等；includeFontPadding 仅 Android，默认 true；textDecorationColor/Style、writingDirection 仅 iOS。
- 🧵 文本装饰：textDecorationLine 默认 none，支持 underline、line-through 等；textDecorationStyle 在 iOS 默认 solid。
- 🌫️ 文字阴影：textShadowColor、textShadowOffset、textShadowRadius 用于控制文字阴影。
- 🔤 大小写与方向：textTransform 默认 none，支持 uppercase、lowercase、capitalize；writingDirection 在 iOS 默认 auto，支持 ltr/rtl。
- 👆 文本选择：userSelect 允许用户选择文本及使用原生复制粘贴，优先于 selectable，默认 none。

---

### [React Native 模块无法使用 Android 的 Activity Result API — Matin Zadeh Dolatabad](https://www.matinzd.dev/blog/activity-result-api-for-react-native-modules/)

**原文标题**: [React Native Modules Cannot Use Android's Activity Result API — Matin Zadeh Dolatabad](https://www.matinzd.dev/blog/activity-result-api-for-react-native-modules/)

overview summary
- 📱 文章讨论 React Native Android 原生模块无法直接使用 AndroidX Activity Result API，因为模块懒加载时 Activity 已进入 RESUMED，注册会触发生命周期崩溃。
- ⏱️ AndroidX 要求在 Activity 到达 STARTED 前注册结果回调，以支持进程被杀恢复后的结果分发；但 RN 模块首次被 JS 访问时通常已错过时机。
- 🧩 旧 ActivityEventListener 仍可用，但需自行选择 request code，命名空间无协调，容易冲突；Health Connect 权限合同没有 startActivityForResult 回退，问题 #33639 自 2022 年仍未解决。
- 🛠️ 现有 workaround 有两类：让每个 App 在 MainActivity 加胶水代码，或由库声明透明 Activity；前者是 react-native-health-connect 当前做法，后者给宿主 App 增加额外 Activity，均有成本。
- 🌐 Expo 通过 registerActivityContracts 解决，Bare React Native 没有等价方案。
- 💡 作者发现 ReactActivity 继承 ComponentActivity，宿主 Activity 已有 ActivityResultRegistry，缺的只是模块访问它的途径。
- 🔌 新 API 放在 ReactContext 上：registerForActivityResult(owner, contract)，可在模块字段初始化时注册；launcher 在 Activity 可用时连接，提前 launch 会暂存并在连接后触发。
- 🚫 该方案无需修改 MainActivity、无需 manifest 条目、无需新增 Gradle 依赖，同时 ActivityEventListener 保持兼容。
- 🔑 实现难点包括：注册 key 不能用计数器，需用“owner 类名:contract 类名”避免模块创建顺序变化和恢复结果错配；多 Activity 切换时需针对当前 registry 重连，不能只看“是否已连接”。
- 🧵 ActivityResultRegistry 只能在 UI 线程操作，所有跨线程调用需转发到 UI 线程；进程被杀后结果可重发，但原 Promise 已随 JS 上下文消失，回调需容忍无 pending。
- 📦 PR #57798 已提交，附 SampleTurboModule 和 rn-tester 演示；核心反思是：多个库各自加 MainActivity 配置，其实是同一个缺失方法被重复买单。

---

### [](https://afonsojramos.me/blog/super-calendar/)

**原文标题**: [Shipping super-calendar | afonso jorge ramos](https://afonsojramos.me/blog/super-calendar/)

Super-calendar 是一个同时面向 React Native 和 react-dom 的日历组件库，主打虚拟化渲染、流畅手势/缩放、日期选择，并从 1.0 快速演进为 core/native/dom 多包架构，积极采纳社区反馈。

- 📦 已发布为 @super-calendar/native（React Native）与 @super-calendar/dom（react-dom），并提供在线演示。
- 🗓️ 一个组件覆盖月视图、周视图、3 日视图、日视图和日程列表。
- ⚡ 通过 @legendapp/list 做虚拟化，只挂载屏幕内日期，默认一次滑动翻一页，可选 freeSwipe 支持多页甩动。
- 🔍 时间网格支持 iOS/Android 捏合缩放和 Web Ctrl/Cmd+滚轮缩放。
- 🧵 行高使用 Reanimated shared value 直接驱动，缩放全程在 UI 线程运行，不触发 React 重渲染。
- 🧩 renderEvent 是真实组件，可读取事件框实时像素高度，按高度显示标题/时间等更多细节；CalendarEvent<T> 支持泛型事件数据。
- ✋ 支持拖动事件以移动/调整大小，重叠事件按并排列布局。
- 📅 日期选择器采用垂直滚动的 MonthList，可点击起止日期或长按拖选跨月连续范围；useDateRange 支持单日、多日、范围与禁用日期。
- 📦 提供独立 /picker 入口，让仅需日期选择器的应用跳过 Reanimated、gesture-handler 和整个时间网格。
- 🚀 1.0 于 6 月 26 日发布；6 月 29 日发布 2.0，拆分为 @super-calendar/core、native、dom 三个包。
- 🌐 core 包含日期数学、事件布局、重复扩展、时区转换、选择模型和主题 token；dom 版基于 Legend List DOM 渲染器，无需 React Native。
- 💬 1.0 后收到 21 个 issue 且全部处理，2.2–2.11 多项功能来自社区，包括资源日历和年视图。
- 🔗 可通过 npm、GitHub 源码和浏览器 live demo 使用。

---

### [5 个 react-native-enriched-](https://swmansion.com/blog/5-react-native-enriched-html-use-cases-you-might-not-know-about/)

**原文标题**: [5 react-native-enriched-html Use Cases](https://swmansion.com/blog/5-react-native-enriched-html-use-cases-you-might-not-know-about/)

react-native-enriched-html 旨在成为默认且广泛使用的基于 HTML 的富文本编辑器，基于原生原语构建，提供简洁 API 与优秀性能；其 EnrichedTextInput 不局限于富文本编辑，还能解决 React Native TextInput 在多个高级场景中的限制。

- 🎯 主要使命：让 react-native-enriched-html 成为默认且广泛使用的 HTML 富文本编辑器，基于原生组件，提供干净 API 和出色性能。
- 🧩 EnrichedTextInput 不限于富文本：许多功能即使不处理 HTML 也能使用，并可弥补 React Native TextInput 的不足。
- 😀 Emoji 选择器：通过 mentionIndicators=[':'] 与 onStartMention/onChangeMention/onEndMention，配合 setMention 完成表情替换，检测与替换在原生侧进行，避免 JS 端性能下降。
- ⚡ 斜杠命令：复用 mentions API，将 mentionIndicators 设为 ['/']，结合 CommandList 过滤和 setMention，让用户直接在输入框中执行命令。
- 🧰 自定义原生上下文菜单：contextMenuItems 可添加“AI 改写”“缩短”“翻译”等菜单项，onPress 提供当前 text、selection 和 range。
- 🔗 可定制链接检测：linkRegex 可自定义链接识别规则，htmlStyle 可控制链接颜色、下划线等显示样式。
- 🖼️ 粘贴图片：onPasteImages 返回图片 URL、宽高和 MIME 类型；可使用 setImage 内嵌，也可自行渲染或上传，React Native TextInput 不支持。
- 🚀 总结：该库用丰富功能减少生态碎片化，并持续扩展；可查看 landing page、详细文档和交互示例，也可联系团队提出新功能需求。

---

### [](https://expo.dev/blog/agentic-ci-for-expo-apps-with-testerarmy)

**原文标题**: [Agentic CI for Expo apps with TesterArmy â Expo blog](https://expo.dev/blog/agentic-ci-for-expo-apps-with-testerarmy)

目前没有收到可供总结的文章内容，因此无法提取关键要点并生成摘要。

- 📄 请在“Use the following content:”后补充需要总结的文本。
- 🧾 收到内容后，我会用中文输出简洁的要点列表。
- ✨ 每个要点将使用“-”符号，并搭配一个合适的 Emoji。
- 🎯 摘要会保留核心信息，确保准确且凝练。

---

### [使用 Claude](https://maestro.dev/blog/mobile-ui-testing-with-coding-agents?utm_source=this-week-in-react)

**原文标题**: [Mobile UI Testing with Claude Code, Cursor and Codex | Maestro](https://maestro.dev/blog/mobile-ui-testing-with-coding-agents?utm_source=this-week-in-react)

移动UI测试与Claude Code、Cursor和Codex的集成方案

- 🤖 AI编程助手可通过Maestro MCP连接iOS模拟器或Android模拟器，直接在聊天中运行UI测试
- 🔄 核心工作流程为“探索-保存-重跑”：先用内联YAML探索界面，成功后保存为Flow文件，后续可重复运行
- 📱 支持的AI代理包括Claude Code、Cursor、Codex、Copilot、Gemini、Windsurf等，设备涵盖Android模拟器、USB连接的实体Android设备、iOS模拟器和Chromium网页
- 🛠️ MCP的run工具接受三种输入：内联YAML（适合探索）、特定Flow文件（适合重跑）、Flow文件夹（适合批量测试套件）
- 📂 工作步骤：用inspect_screen查看屏幕→用yaml尝试步骤→将有效步骤保存到.maestro/目录→通过MCP或CLI重新运行
- 💡 实际示例：让代理测试Appearance屏幕的主题切换功能，保存为.maestro/appearance.yaml后，UI变动时重跑即可验证是否通过
- ✅ 保存的Flow文件是回归测试，任何代理或CLI都能在本地或CI中重复运行，实现可复现的端到端测试
- 🔗 MCP与CLI使用相同的YAML格式，设备上验证过的步骤与后续重跑的步骤完全一致

---

### [发布 @react-navigation/core@7.23](https://github.com/react-navigation/react-navigation/releases/tag/%40react-navigation%2Fcore%407.23.0)

**原文标题**: [Release @react-navigation/core@7.23.0 · react-navigation/react-navigation · GitHub](https://github.com/react-navigation/react-navigation/releases/tag/%40react-navigation%2Fcore%407.23.0)

react-navigation 仓库中的 @react-navigation/core@7.23.0 于 2026-09-29 发布，由 @satya164 发布并带有已验证签名；该版本包含 2 项错误修复和 1 项新功能，仓库当前约有 24.5k Star、5.1k Fork、800 个 Issues 与 53 个 PR。

- 📦 仓库公开，主要导航数据：24.5k Star、5.1k Fork、800 Issues、53 PR。
- 🚀 发布 @react-navigation/core@7.23.0，版本日期为 2026-09-29，发布者为 @satya164。
- 🔐 标签与提交均由 Satyajit Sahoo（@satya164）使用 GPG 密钥验证签名，发布标记为不可变。
- 🐛 错误修复：导航挂起时允许阻止移除；仅在有监听器时构建根状态。
- ✨ 新功能：为 tabs 增加 tabBarRepeatedPressBehavior。
- 👤 贡献者：@satya164；附带 3 个资源，并获得 1 个 ❤️ 反应。

---

### [](https://lynxjs.org/next/blog/lynx-4-0)

**原文标题**: [Lynx 4.0: Foldables, Media Queries, Liquid Glass, WebView, OpenUI, and More - Lynx](https://lynxjs.org/next/blog/lynx-4-0)

Lynx 4.0 正式发布，重点支持折叠屏与动态屏幕适配、CSS 媒体查询，开源 `<blur-view>` 和 `<webview>`，并增强桌面 CSS、ReactLynx、调试、AI 生成式 UI 与内存诊断；该大版本不含破坏性变更，后续将公布新愿景。

- 📱 折叠屏适配：与 TikTok 合作，窗口尺寸变化时同步更新 screen metrics、viewport、GlobalProps 并触发重排；响应式模式下 GlobalProps 更新会触发 ReactLynx re-render，使用弹性布局和相对单位的页面通常无需改代码。
- 📐 CSS 媒体查询：引入 Media Queries Level 4 核心能力，支持视口宽高、宽高比、方向、像素密度、min-/max-/and/or/not、逗号列表、范围语法及颜色方案偏好。
- 🧊 原生背景模糊与 Liquid Glass：开源 `<blur-view>`，跨 Web、HarmonyOS、iOS、Android 渐进增强；iOS 用 `blur-effect="glass"` 渲染 Liquid Glass，支持 `glass-style`、`glass-tint-color`、`glass-interactive`，以及 `glass-container` 与 `spacing`；Android 可设 `android-capture-target`。
- 🌐 WebView：开源 `<webview>`，支持 Android、iOS、HarmonyOS、macOS、Windows；可设置 `src` 加载网页，或在部分平台用 `html` 加载 HTML 字符串，需显式宽高。
- 🖥️ 桌面渲染：Clay 在 macOS/Windows 新增自定义文本光标属性 `-x-caret-*`，以及 `mask-composite` 多层遮罩合成，支持 `add`、`subtract`、`intersect`、`exclude`。
- ⚛️ ReactLynx：新增 `createElement` 与 `cloneElement`，可运行时动态创建和克隆 Lynx 元素；结构已知时仍推荐 JSX 以利于编译器优化。
- 🧭 统一调试元数据：Rspeedy 每次构建生成 `debug-metadata.json`，可把生产错误映射回源码，包括主线程字节码错误，并把运行时 UI 节点映射到创建它的 JSX。
- 🤖 AI 生成式 UI：新增 OpenUI 支持，`<OpenUiRenderer>` 可流式解析 OpenUI Lang 并渲染为 ReactLynx 组件；提供 `lynx-a2ui`、`lynx-openui` 和 `lynx-api-docs` 等 Agent Skills。
- 🧠 内存诊断：iOS/Android 支持全局 Lynx 内存查询，可异步收集存活实例的内存占用，并按 Elements、UI/Views、主线程/后台线程运行时分类。
- 🚀 升级与获取：将 Lynx 和 PrimJS 依赖更新至 4.0.x 及对应平台依赖，参考集成指南与发布说明；团队感谢社区反馈、代码贡献与经验分享。

---

### [](https://github.com/Fausto95/lucent)

**原文标题**: [GitHub - Fausto95/lucent: Write React Native native modules in TypeScript. Lucent compiles a checked subset to C++ and calls it through JSI: no Swift or Kotlin to write, and no JavaScript engine in native code. · GitHub](https://github.com/Fausto95/lucent)

Lucent 是一个实验性开源项目，旨在让开发者用 TypeScript 编写 React Native 原生模块，并将其受检子集编译为 C++，再通过 JSI 调用，从而避免编写 Swift/Kotlin，也避免在原生代码中嵌入 JavaScript 引擎。

- ⚠️ 项目明确标注为实验性，不适合生产环境；API 和语言子集可能在没有迁移路径的情况下变更。
- 🧩 使用 TypeScript 编写原生模块，Lucent 会把受检子集编译成 C++，并通过 JSI 调用。
- 🚫 无需编写 Swift 或 Kotlin，原生代码中也不需要 JavaScript 引擎。
- 🧮 示例：`squaredDistance` 会在 C++ 中计算并返回结果。
- 📱 模块可直接调用 iOS 和 Android SDK，类型来自 Xcode 与 Android SDK；同一个模块可同时包含两个平台的逻辑，例如剪贴板示例。
- 📦 支持 bare React Native 0.88+ 以及 Expo SDK 58+ 的 development builds。
- ⚙️ 安装方式：`npm i -D @lucent-lang/lucent`，然后运行 `npx lucent init`。
- 🧪 开发命令包括 `pnpm install`、`pnpm test`、`pnpm test:runtime`、`pnpm test:e2e` 等。
- 📚 文档涵盖安装、教程、工作原理、指南、参考、示例和路线图；架构与规范位于 `docs/`。
- ⭐ 仓库当前约有 24 stars、1 watcher、0 forks、2 issues，以及 643 次提交。
- 📄 项目采用 MIT 许可证，`CONTRIBUTING.md` 说明了贡献流程与提交风格。

---

### [发布 react-native-macos@0.83.0 · microsoft/react-native-macos · GitHub](https://github.com/microsoft/react-native-macos/releases/tag/react-native-macos%400.83.0)

**原文标题**: [Release react-native-macos@0.83.0 · microsoft/react-native-macos · GitHub](https://github.com/microsoft/react-native-macos/releases/tag/react-native-macos%400.83.0)

microsoft/react-native-macos 是一个从 react/react-native 分叉而来的公开仓库，当前页面展示了项目协作信息与最新版本发布。最新版本为 react-native-macos@0.83.0，由 microsoft-react-native-sdk 发布，包含与 React Native 0.83.10 同步的重要更新。

- 📦 仓库为 microsoft/react-native-macos，Public，fork 自 react/react-native  
- ⭐ 项目热度：4.4k Star，173 Fork  
- 🧩 协作数据：87 个 Issues、24 个 Pull Requests  
- 🗂️ 功能板块：Code、Issues、Pull Requests、Discussions、Actions、Projects、Wiki、Security and quality、Insights  
- 🔐 Security and quality 显示为 0  
- 🔔 通知设置：需登录后才能更改  
- 🚀 最新发布：react-native-macos@0.83.0，标记为 Latest  
- 📅 发布时间：9 月 30 日 00:37，由 microsoft-react-native-sdk 发布，21 次提交进入 main  
- 🔄 主要变更：与 React Native 0.83.10 同步，是 react-native-macos 首个 0.83 版本  
- 📦 发布资产：2 个  
- 🎉 互动：1 个 🎉 反应，Zeirison 表示 hooray

---

### [](https://github.com/callstackincubator/appduct)

**原文标题**: [GitHub - callstackincubator/appduct: Expose app tools securely - no debug menus in the binary · GitHub](https://github.com/callstackincubator/appduct)

Appduct 是 Callstack 的开源工具，让终端、测试运行器或 AI 代理在运行时调用 React Native、iOS、Android 应用中你明确注册的函数，默认不进入发布构建。

- 🔧 只暴露开发者主动注册的可调用函数，其他内容不可达，也没有隐藏调试菜单或秘密手势。
- 🧪 适合 E2E 测试：直接调用 `login(userId)`、`seedCart(items)` 等，跳过登录、引导、等待加载等繁琐步骤，减少不稳定和截图成本。
- 🤖 可让 AI 代理驱动应用：通过 MCP 配置接入 Claude Code、Cursor 等，或通过 CLI 供脚本和 CI 使用。
- 🧱 默认只包含在 debug 构建中，release 构建会完全编译移除；如需进入 TestFlight 等内部构建，可按构建选择加入。
- 🔄 会话在重载、切后台、网络波动后仍能自动恢复，一个后台服务可管理多台已连接设备。
- 📦 React Native 使用 `useAppductTool` + `zod` 注册工具，终端可用 `appduct tools call seed_cart --input '{"items":3}'` 调用。
- 🔗 CLI 和 MCP server 会自动读取 `app.json`、`Info.plist`、`build.gradle` 中的 deep-link scheme，无需额外配置。
- 🔐 安全默认：release 构建无相关代码；若主动带入外部构建，连接仍加密、验证对端身份，被拦截的链接不能进入，详见 `SECURITY.md`。
- 🛠️ 安装 CLI：`npm install -g appduct`；React Native 安装 `@appduct/react-native zod`，需要 development build 或 bare RN，Expo Go 不支持。
- 📱 无 React Native 也可用 Swift/Kotlin：iOS 使用 `AppductCore`，Android 使用 `com.callstack.appduct:core`，release 可搭配 `core-noop`。
- 🧩 主要包：`appduct` CLI/后台服务/MCP server、`@appduct/react-native`、`@appduct/shared`、`AppductCore`、Android core。
- ✅ 支持范围：RN iOS 15.1+、Android 新架构，Web 为 no-op；无 RN 时 iOS 15.1+、Android 7.0+；CLI 需要 Node 20+。
- 🌟 MIT 开源，Callstack 出品，永久免费，欢迎给项目点 star。

---

### [发布 NitroSQL](https://github.com/margelo/react-native-nitro-sqlite/releases/tag/v10.0.0)

**原文标题**: [Release NitroSQLite 10.0.0 · margelo/react-native-nitro-sqlite · GitHub](https://github.com/margelo/react-native-nitro-sqlite/releases/tag/v10.0.0)

NitroSQLite 10.0.0 是 margelo/react-native-nitro-sqlite 的一次重大版本更新，重点为需要更强 SQLite 连接控制与重复查询能力的应用带来独立连接、可复用预处理语句、原生调度队列和 macOS 支持，同时保持现有单连接用法兼容，并要求升级后重建原生应用。

- 🚀 v10.0.0 于 9 月 25 日发布，是 NitroSQLite 的重要版本，面向更复杂的 SQLite 连接与查询场景。
- 🔗 新增 `connection: 'independent'`，可为同一数据库文件打开独立句柄，每个句柄拥有独立原生 SQLite 连接和操作队列，支持只读句柄与并发读写。
- ⚠️ SQLite 仍只允许每个文件一个写入者；并发读写建议先初始化数据库，并在写连接启用 WAL 模式，读连接按事务快照查看已提交数据。
- ♻️ 新增 `db.prepare(query)`，可准备一次并复用预处理语句，支持同步或异步多次执行并传入新参数，关闭连接前需调用 `finalize()`。
- ⚙️ 异步查询、批次和文件导入进入每连接原生 FIFO 队列，不再等待前一结果返回 JavaScript；事务回调仍保持顺序，批次和导入为原子原生任务。
- 🍎 核心 SQLite 与可选 `sqlite-vec` 包现已支持 macOS，仓库加入桌面示例，并在 macOS 上运行共享测试套件。
- 📦 自 2024 年 10 月首个 npm 预发布、11 月 9.0.0 正式版以来，项目已迁移到 Nitro Modules，并加入可空 SQL 值处理、TypeORM 驱动、托管事务/批次队列、内存与查询结果优化、向量搜索等能力。
- 📱 项目还新增 Android 16 KB 页大小支持、可配置 iOS 数据库存储与迁移到 Application Support，以及移动端可配置 SQLite 构建选项。
- 🛠️ 升级需重建原生应用；现有单连接调用仍受支持，独立连接为可选功能且需要 SQLite mutex，`SQLITE_THREADSAFE=0` 构建会拒绝该功能。
- 🗑️ 数据库删除会拒绝仍被其他连接或附件使用的文件；已关闭的 session 对象不能操作同名替换连接。
- 📝 自定义原生集成可能需适配 C++ 签名变化；本次还包含 C++ 文件名前缀、扩展 API 文档和发布锁文件检查。

---

### [发布 v3.6.0 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.6.0)

**原文标题**: [Release v3.6.0 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.6.0)

LegendApp/legend-list 发布 v3.6.0，新增 viewPositionFallback，用于在初始或程序化滚动时将超大项目对齐到视口起点或终点，同时对适合视口的项目继续使用 viewPosition 对齐。

- 📦 仓库：LegendApp/legend-list，公开项目
- ⭐ 数据：3.4k Star，150 Fork
- 🐞 协作：63 个 Issues，30 个 Pull Requests，并包含 Discussions、Actions、Projects、Security and quality、Insights 等板块
- 🚀 版本：v3.6.0 为最新版本
- 👤 发布：由 jmeistrich 于 9 月 29 日 19:50 发布，提交为 3d80d16
- ✨ 新功能：添加 viewPositionFallback，支持超大项目在初始或程序化滚动时按视口起点/终点对齐
- 📎 资源：该版本附带 2 个 Assets
- ❤️ 反响：获得 3 个爱心反应，来自 buriev、SpasiboKojima 和 sajorahasan

---

### [](https://github.com/ng-native/ng-native)

**原文标题**: [GitHub - ng-native/ng-native: Angular apps, rendered as real native iOS and Android views, on React Native's Fabric renderer. · GitHub](https://github.com/ng-native/ng-native)

Angular Native 是一个开源项目，可将 Angular 应用直接渲染为真正的原生 iOS 和 Android 视图，基于 React Native 的 Fabric 渲染器实现，React 不参与渲染路径。

- 📱 **核心原理**：Angular 组件直接渲染到 React Native 的 Fabric 渲染器上，`<view>` 在 iOS 上是 UIView，在 Android 上是 android.view.View，React 完全不在渲染路径中
- 🚀 **快速开始**：通过 `npx create-expo-app@latest my-app --template @ng-native/template` 创建项目，用 Expo 启动、热重载并发布应用
- ✍️ **开发方式**：像写 Web 应用一样编写独立组件、signals、Signal Forms 和 @angular/router 路由
- 🎨 **样式支持**：组件样式表、CSS 变量、媒体查询、暗黑模式、过渡与 @keyframes，并支持 Tailwind 预设与 ios:/android: 变体
- 🧭 **原生导航**：@angular/router 覆盖原生栈、标签页、头部、模态和 sheet，支持守卫、解析器、懒加载路由与深度链接
- 📝 **表单**：Signal Forms 绑定原生控件
- 📦 **Expo 模块**：相机、定位、通知、安全存储、文件系统、SQLite、生物识别、地图、触觉反馈等以 Angular 服务形式注入
- 🎬 **动画**：支持 animate.enter/leave、CSS 过渡以及 Animated 和 Reanimated worklets
- 🧪 **测试**：Testing Library API 在 Node 中针对模拟 Fabric 运行组件，无需模拟器
- 🛠️ **集成现有工作区**：提供 Angular CLI 生成器（ng add @ng-native/schematics）和 Nx 生成器（nx add @ng-native/nx）
- 🌐 **Web 支持**：@ng-native/web 可将相同组件渲染到 DOM
- 📚 **完整示例**：包含银行（wallet）、习惯追踪（habits）、音乐播放器（music）、跑步追踪（runs）和笔记（notes）等完整应用
- 🧩 **核心包**：@ng-native/platform、components、router、device、expo、icons、metro、tailwind、testing、web、schematics、nx、fabric
- ⚙️ **环境要求**：Angular 22、Expo SDK 57、React Native 0.86（新架构）、Node 22.18 或更高版本
- ⚠️ **项目状态**：目前处于 alpha 阶段，0.x 版本间 API 可能变化，已知限制已列出并提供解决方案
- 📄 **许可证**：MIT 许可，独立开源项目，与 Google、Angular 团队或 Expo 无隶属关系
- 🙌 **贡献者**：erKam、Chau Tran、Stavros Thalassinos、Luis David Lopera、Ajit Panigrahi 等

---

### [](https://github.com/bhyoo99/react-native-nitro-rtmp)

**原文标题**: [GitHub - bhyoo99/react-native-nitro-rtmp: Live video streaming over RTMP and RTMPS for React Native, built on Nitro Modules. · GitHub](https://github.com/bhyoo99/react-native-nitro-rtmp)

本文介绍了 react-native-nitro-rtmp，一个基于 Nitro Modules 和 VisionCamera 5 的 React Native RTMP/RTMPS 直播库，支持硬件编码、GPU 合成和图层叠加，并提供了详细的 API、配置和使用说明。

- 📹 基于 VisionCamera 5 和 Nitro Modules，实现 React Native 的 RTMP/RTMPS 直播，相机功能完全由 VisionCamera 管理。
- 🎤 支持麦克风捕获，静音时发送静音以保持音频时间线不中断。
- 🎨 提供 GPU 混合器，支持相机和图像图层叠加，并可通过 PreviewView 预览实际发送的画面。
- ⚙️ 使用硬件 H.264 和 AAC 编码，支持 rtmp:// 和 rtmps://，可配置分辨率、帧率、码率等。
- 📦 要求 React Native 新架构（0.86+），依赖 react-native-vision-camera ^5.2 和 react-native-nitro-modules ^0.37。
- 🪝 主要 API 为 useRtmpStream 钩子，返回 cameraOutput 可传递给 VisionCamera 的 <Camera>，并通过 start()/stop() 控制推流。
- 🖼️ 可通过 stream.mixer 动态添加图像图层，实现自定义合成，支持 PNG/JPEG 叠加。
- 📊 提供类型化会话状态、错误代码和统计信息（如字节数、丢帧数等）。
- 🚫 限制：暂不支持发布时旋转、自适应码率、自动重连、后台模式；仅 H.264/AAC；无本地录制；iOS 模拟器无相机。
- 🔄 从 0.3 迁移需改用 VisionCamera 管理相机，并传递 cameraOutput，相机权限由 VisionCamera 处理。
- 🧪 包含验证流脚本和 C++ 主机测试，确保 RTMP 协议核心的可靠性。
- 📄 采用 MIT 许可证，基于 create-react-native-library 构建。

---

### [发布 v0.9.0 · mdjastrzebski/react-native-plain-text · GitHub](https://github.com/mdjastrzebski/react-native-plain-text/releases/tag/v0.9.0)

**原文标题**: [Release v0.9.0 · mdjastrzebski/react-native-plain-text · GitHub](https://github.com/mdjastrzebski/react-native-plain-text/releases/tag/v0.9.0)

该页面是 mdjastrzebski/react-native-plain-text 的 GitHub 仓库，主要展示 v0.9.0 最新版本发布内容，并包含仓库状态、功能新增、Bug 修复、重构与文档更新等信息。

- 📦 仓库信息：mdjastrzebski/react-native-plain-text，公开仓库；更改通知需登录。
- ⭐ 社区指标：140 Star、6 Fork、0 Issue、5 Pull Request。
- 🚀 最新发布：v0.9.0 为最新版本，发布于 9 月 25 日 06:54；自该版本以来 main 分支有 9 个提交，版本日期标注为 2026-09-25。
- ✨ 新功能：新增统一 Text 组件（#30）。
- 🧩 新增属性：hyphens 和 lang（#9）、lineBreakStrategyIOS（#26）、Android 的 android_hyphenationFrequency（#31）与 textBreakStrategy（#25）、iOS 的 writingDirection 样式属性（#27）。
- 🐛 Bug 修复：修复 Android 多行与 ellipsize 模式下的尺寸问题；修复示例中 color 属性的更新颜色操作。
- ♻️ 代码重构：调整代码结构（#23）；重命名 unstable_lineHeightClippingCompat。
- 📝 文档更新：补充缓存说明；记录 iOS 下划线位置。
- 📎 发布资源：包含 2 个 Assets；页面标签加载时曾出现错误提示。

---

### [发布](https://github.com/callstack/repack/releases/tag/%40callstack/repack%405.4.0)

**原文标题**: [Release 5.4.0 · callstack/repack · GitHub](https://github.com/callstack/repack/releases/tag/%40callstack/repack%405.4.0)

overview summary
Re.Pack 5.4.0 最新版本发布，重点改进多平台开发按需编译、统一命令入口，并修复 Android、Windows、Module Federation、source map、React Native 0.87 兼容及生产压缩等问题。

- 🚀 发布 @callstack/repack@5.4.0，标记为 Latest，包含 Minor Changes 与 Patch Changes。
- ⚙️ 多平台开发服务器改为按需编译：仅当某平台 bundle 首次被请求时才编译，避免 iOS/Android 互相等待。
- 🧭 新增统一入口 @callstack/repack/commands，支持自动检测 bundler 和 --bundler 覆盖；Re.Pack Init 已使用，旧入口保留但会有弃用警告。
- 🤖 修复 Android AGP 9 内置 Kotlin 支持导致的 “Cannot add extension with name 'kotlin'” 问题。
- 🪟 修复 Windows 资源加载失败：资源 URL 改用 path.posix.join，避免反斜杠导致 new URL 报 Invalid URL。
- 🧩 修复 BabelPlugin 的 resolveLoader.fallback 配置，改为数组形式以兼容 Rspack、RSDoctor 等工具。
- 🛡️ 让 ChunkLoadError 正常传播，使动态导入失败可被 React Error Boundary 捕获处理。
- 🗺️ 修复 Module Federation 主机与远程包的开发符号化，支持远程 source map、无效源 URL 容错和逐帧映射。
- 🧼 修复 source map 源名称与开发栈帧编码问题：不再设置 sourceRoot，开发服务器返回未编码文件名，编码目录资源不再 404。
- 📱 保留 iOS 脚本下载失败时的原始错误信息，不再显示 “Unknown error from a native module”。
- 🔗 修复 ModuleFederationPlugin 的 shared 数组形式读取 react-native 配置，使相关深导入继承 eager、import 和 version。
- ⏳ 编译失败时会拒绝挂起的 webpack 资源请求，避免请求一直等待。
- 🆕 支持 React Native 0.87，更新 polyfills、asset registry 和 private 路径别名解析逻辑。
- 🧵 修复 webpack compiler 的 getSource 对绝对路径双重拼接的问题，使其与 Rspack 行为一致。
- 🗜️ 修复 terser-webpack-plugin 5.6.0+ 下 .bundle 生产包未被压缩的问题。
- 📦 更新依赖 @callstack/repack-dev-server@5.4.0。

---

### [ViroReact 3.0.0：五大平台，一套代码库——ReactVision](https://www.reactvision.xyz/updates/viroreact-3-0-0-five-platforms-one-codebase/)

**原文标题**: [ViroReact 3.0.0: Five Platforms, One Codebase - ReactVision](https://www.reactvision.xyz/updates/viroreact-3-0-0-five-platforms-one-codebase/)

ViroReact 3.0.0 于2026年9月29日发布，将同一套代码库从三个平台扩展到五个平台，新增 visionOS 与 Web AR，并带来自有 VPS、多人共定位、Studio Scene Links、8th Wall 迁移、StudioSceneNavigator 改进及 Ctrl+Space 黑客松。

- 🚀 ViroReact 3.0.0 发布：同一代码库支持五个平台，已有 React Native 场景可运行到更多设备。
- 🥽 visionOS：场景可运行于 Apple Vision Pro；需升级 @reactvision/react-viro 3.0+，安装 @reactvision/react-native-visionos，添加 visionOS Expo 插件，并使用 ViroXRSceneNavigator，用法类似 Quest。
- 🌐 Web AR：相同组件可在浏览器运行，零安装、无需应用商店，只需链接；追求峰值性能仍选原生，追求触达和速度则选 Web，且同一代码仍可发布到其他原生平台。
- 🛰️ 新 ReactVision VPS：Cloud Anchors 与 Geospatial Anchors 现基于自有 Visual Positioning System，属于 ReactVision Spatial，未来还有更多 VPS 工作。
- 🤝 共定位：共享坐标框架、实时通道和复制状态，支持同房间多人真正多人 AR；同一设备家族内支持手机、Quest 和 visionOS。
- 🎬 Studio Scene Links：发布 Studio 场景并分享 URL，任何人打开即可获得 Web AR；在场景编辑器打开 publish 并开启 Publish to web 即可获取链接。
- 🔄 8th Wall 迁移：Studio 可导入现有 8th Wall 项目，MCP server 可在 IDE 内将 8th Wall 导出转换为 ViroReact 项目；之后可继续在 Studio 构建、用 StudioSceneNavigator 嵌入或通过 Scene Links 分享。
- 🧩 StudioSceneNavigator：本次更新带来 50 多项渲染改进，让 Studio 场景嵌入应用后渲染效果更好。
- 🏆 Ctrl+Space 黑客松：Expo x ReactVision 举办，2026年10月3日至11日虚拟构建周，全球开放，任何技能水平，个人或团队均可，用 ViroReact、Studio 或 MCP server 发布真实 AR/VR 应用。
- 📍 线下活动：将在旧金山、伦敦、多伦多和班加罗尔举行，细节仍在确定，目前以虚拟周为主要入口。
- 🔗 社区与资源：可在 X、LinkedIn、YouTube 关注，加入 Discord 社区，并打开 Studio 开始构建。

---

### [发布 v2.13.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.13.0)

**原文标题**: [Release v2.13.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.13.0)

Shopify/react-native-skia 发布 v2.13.0，包含 6 个提交，主要修复 Metal 上下文与 drawPatch 混合模式问题，移除旧架构支持，并新增 Android surfaceType 选择功能。仓库当前约 8.6k Star、653 Fork、44 个 Issue 和 55 个 PR。

- 📦 Shopify/react-native-skia 是公开仓库，现有约 8.6k Star、653 Fork、44 个 Issue 和 55 个 PR。
- 🚀 发布 v2.13.0，日期为 2026-09-24，自上一版本以来 main 分支有 6 个提交。
- ✅ 提交 8f4b85c 已由 GitHub 验证签名，GPG 密钥 ID 为 B5690EEEBB952194。
- 🍏 修复：创建 Metal direct context 时传入 GrContextOptions（#4075）。
- 🎨 修复：在 drawPatch 中遵循可选的 paint 和 blend mode（#4076）。
- 📃 修复：移除对旧架构的支持（#4070）。
- 🤖 新特性：可通过 android.surfaceType 选择 Android backing view（#4082）。
- ❤️ 该版本获得 3 个❤️反应，发布资产为 3 个。

---

### [发布 8.28.](https://github.com/getsentry/sentry-react-native/releases/tag/8.28.0)

**原文标题**: [Release 8.28.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.28.0)

sentry-react-native 发布最新版 8.28.0（9 月 24 日，由 sentry-release-bot 发布），重点为 iOS/Android 原生面包屑与追踪选项增加开关，并修复构建、超时、反馈表单等问题，同时升级 JavaScript SDK。

- 📦 版本：8.28.0 标记为 Latest，提交为 e6f7b49。
- 🍞 iOS 新增 enableNetworkBreadcrumbs，可禁用原生 HTTP 请求面包屑（#6764）。
- 📡 Android 新增 enableNetworkEventBreadcrumbs，可禁用原生网络连接面包屑（#6764）。
- 🔧 暴露更多原生面包屑开关：iOS enableAutoBreadcrumbTracking；Android enableActivityLifecycleBreadcrumbs、enableAppLifecycleBreadcrumbs、enableSystemEventBreadcrumbs、enableAppComponentBreadcrumbs（#6768）。
- 🕵️ iOS 新增 reportAccessibilityIdentifier，可从视图层级中省略 PII 辅助功能标识符（#6771）。
- 🚀 iOS 新增 enablePreWarmedAppStartTracing，可退出预热启动的应用启动追踪；新增 enableMetricKitRawPayload，将原始 MetricKit 诊断负载附加到 MetricKit 事件（#6772）。
- 🐛 修复：声明可选 peer dependencies，使严格与 Plug'n'Play 包管理器下导入可解析（#6729）；iOS 遵守 shutdownTimeout（#6749）。
- 🧱 修复 Android Gradle 插件不再在构建/发布构建时把生成的 sentry.options.json、modules.json 写入源码树（#6751、#6753）。
- 🍎 修复 Mac Catalyst 链接错误的 Sentry.xcframework 切片（#6758）；FeedbackForm 防止重复提交并在出错时保留草稿（#6769）。
- 🧩 内部：从入口点导出已公开的选项和配置类型，以便在 API 报告中跟踪完整形态（#6731）。
- ⬆️ 依赖：JavaScript SDK 从 v10.75.0 升级至 v10.75.2（#6763、#6767）。
- 📊 仓库状态：Fork 369、Star 1.8k、Issues 114、PR 10；发布页有 4 个资源，获得 1 个 👍。

---

### [](https://github.com/LegendApp/legend-list/releases/tag/v3.5.0)

**原文标题**: [Release v3.5.0 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.5.0)

LegendApp/legend-list 发布 v3.5.0，由 jmeistrich 于 9 月 29 日发布，包含 2 个提交并合并到 main；主要带来 Web 列表滚动容器共享、滚动停止后的渲染缓冲修复，以及单列列表性能优化。仓库当前约 3.4k stars、150 forks、63 个 issues、30 个 PR。
- 🚀 新增 `scrollElement`，让 Web 列表可以共享祖先元素的滚动条。
- 🐛 修复停止滚动时的行为：行会保持在最后滚动方向预渲染，而不是把渲染缓冲区向后移动。
- ⚡ 性能优化：当项目尺寸和数据未变化时，单列列表在首次渲染和滚动期间减少布局计算。
- 📦 发布信息：v3.5.0 由 jmeistrich 发布，包含 2 个提交，并已合并到 main。
- 📊 仓库概况：LegendApp/legend-list 当前约有 3.4k stars、150 forks、63 个 issues、30 个 PR。
- ⚠️ 页面曾出现加载错误提示，部分内容可能需要刷新查看。

---

### [发布 v0.26.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.26.0)

**原文标题**: [Release v0.26.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.26.0)

overview summary
- 🚀 software-mansion/argent 发布最新版 v0.26.0，2025年9月25日更新，包含 12 个提交合并到 main。
- 📦 CI 发布修复：发布任务附加自身打包的 tarball，而不是从 npm 取回的文件。
- 🖥️ boot-device 修复：在活跃 Xcode 的 Device Hub 中打开已启动的模拟器。
- ☁️ 云文档更新：说明 SIM_REMOTE_SESSION，支持一台电脑运行多个会话。
- 🧪 CLI 增强：目录运行结束时显示失败流程和重新运行命令。
- 📱 iOS 新功能：支持可折叠模拟器（iPhone Duo）。
- ⚠️ simulator-server 修复：在未就绪前退出时会说明原因。
- 🔢 版本号提升至 0.26.0；新贡献者 @bjjeong 首次贡献，完整变更见 v0.25.2...v0.26.0。
- 📊 仓库概览：公开项目，Star 2.9k、Fork 124、Issues 213、Pull requests 110、Assets 3。

---

### [发布 v0.21.15 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.21.15)

**原文标题**: [Release v0.21.15 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.21.15)

v0.21.15 是 callstack/agent-device 项目于 9 月 25 日发布的版本更新，由 thymikee 和 okwasniewski 两位贡献者完成，自 v0.21.14 以来共包含 105 次提交。本次更新以缺陷修复和代码重构为主，重点集中在 Android、iOS-runner、macOS 以及 WebDriver 提供者等模块。

- 📦 版本发布：callstack/agent-device v0.21.15，拥有 4.8k 星标与 315 次分支派生
- 🗓️ 发布信息：由 thymikee 于 9 月 25 日发布，自上一版本以来累计 105 次提交
- 👥 贡献者：thymikee 与 okwasniewski 共同参与本次更新
- 🤖 Android 修复：快照节点携带字段提示文本作为 placeholder（#2927）
- ✅ Android 修复：快照节点携带可勾选控件的选中状态（#2913）
- 📱 Android 修复：仅在启动的应用可读后才从应用打开操作返回（#2895）
- ⏱️ Android 修复：验证样本填充至截止时间而非固定三个点（#2926）
- 🧪 Android 测试：删除字节完全相同的重复文本输入用例（#2931）
- 🎉 Android 新功能：辅助截图在快照元数据中携带显示像素密度（#2928）
- ⏳ 超时修复：证明请求信封覆盖其最坏情况的工作量（#2916）
- ⌛ 等待修复：报告消耗等待预算的就绪工作（#2893）
- 🔧 iOS-runner 重构：将快照质量判定状态改为封闭枚举（#2888）
- 🖥️ macOS 重构：从单一所有者表派生 macOS 表面路由（#2886）
- 🧩 Provider-webdriver 重构：移除已被取代的云运行时工厂（#2930）
- 🏅 iOS-runner 测试：将生产构建的 runner 请求固定在 TS 与 Swift 双验证的黄金表中（#2900）
- 🔗 完整变更日志：可对比 v0.21.14...v0.21.15 查看全部改动

---

### [GitHub - kevinmoch/web-skill：WebSkill 网站与演示 · GitHub](https://github.com/kevinmoch/web-skill)

**原文标题**: [GitHub - kevinmoch/web-skill: WebSkill Website & Demo · GitHub](https://github.com/kevinmoch/web-skill)

WebSkill 是由 Chunhui Mo（Huawei）提出的草案，讨论“Agentic Web 向 SaaS（Skill as a Service）演进”：把标准化、可复用的 Agent Skill 变成前端原生能力，在浏览器内完成发现、读取、校验、运行、安装与卸载，并通过 OPFS 与 Web Worker 实现隐私隔离和个性化演进，最终推动 Web 标准化。

- 🧠 Agent Skill 是面向 AI 的模块化“培训手册”，封装领域知识、指令、元数据、脚本与模板，让通用模型变成专业执行者。
- 🎯 它解决三大痛点：上下文膨胀、领域知识差距、重复提示；典型场景包括编码规范、业务文档、安全合规。
- 🌐 WebSkill 是前端原生技能，运行在浏览器内，采用声明式契约，无需传统后端，形成自包含闭环。
- 🔒 三大特性：浏览器闭环执行、OPFS + Web Worker 隐私隔离、本地个性化动态演进。
- 🏗️ 架构为：对话输入 → 端侧 LLM 中心 → WebSkill 技能层 → Generative UI 交互层 → WebMCP 执行层。
- 🔁 对比传统后端 Skill：无需服务器、零外发数据、可直接操作 DOM/会话状态、随 Web 应用分发、支持个人化演进。
- 🛡️ 安全机制包括：OPFS 同源保护、防意图碰撞、Worker 沙箱、敏感操作需 Human-in-the-Loop 授权。
- 📁 TypeScript 实现标准 Agent Skills 协议：SKILL.md、scripts/、references/、assets/。
- 📉 渐进披露三层加载：先元数据，再指令，最后按需加载脚本与资源，降低 Token 消耗与响应延迟。
- ⚙️ scripts/ 仅支持 .ts/.js，必须导出 run，并提供 inputSchema；可用 JSON Schema、TS interface 或 JSDoc 推断，返回值遵循 MCP 标准。
- 🔌 支持标准 MCP TS SDK（endpoint:toolName）与 Chrome 实验性 MCP API（mcp#toolName）。
- 📄 页面级动态 WebSkill：主线程作 MCP Server，通过 MessageChannel 与 Worker 中 MCP Client 通信，页面关闭即失效。
- 🖥️ Generative UI 在缺参数时渲染表单，状态流转 IDLE → PARAMS_COLLECTED → AWAITING_USER → COMPLETED → EXECUTING，UIBridge 解耦 UI 框架。
- 🧩 标准化提案：Web IDL 增加 navigator.webskill，含 SkillDiscovery、MinimalRuntime、SkillManager 三类 API。
- 🧪 使用简单：discover/read/validate/run/install/uninstall；示例可几行代码运行“用计算器算 2+3”。
- 🚀 结论：WebSkill 仍处早期，但可解决上下文膨胀与隐私安全，把 Agent 能力变成轻量、动态、可分发、个性化的 Skill as a Service；未来浏览器或成为智能运行时。
- 🔗 官网与静态 Demo：webskill.ai、webskill.ai/demo；仓库 kevinmoch/web-skill，12 Stars、1 Fork、27 Commits、MIT。

---

### [优化具有 null 原型的对象](https://adventures.nodeland.dev/archive/optimizing-objects-with-null-prototypes/)

**原文标题**: [Optimizing objects with null prototypes](https://adventures.nodeland.dev/archive/optimizing-objects-with-null-prototypes/)

overview summary
本文解释 V8 中 `{ __proto__: null }` 创建的对象为何长期处于字典模式、导致属性访问变慢，并给出三种保持快速属性的替代写法；这些优化在 Node core WebStreams 中带来显著吞吐提升，但只应针对热路径使用。

- 🐢 `{ __proto__: null }` 创建的对象在 V8 中会进入字典模式（DICT），无论属性多少、`__proto__` 写在哪里，读取属性也不会恢复快速模式。
- ⚡ 唯一例外：当该对象被用作另一个对象的原型时，V8 会将其优化为原型并切换到快速模式（FAST）。
- 💸 代价明显：null 原型字面量构造约需 500–1500 ns，而普通字面量约 30 ns；后续每次属性访问都是字典查找，无法命中内联缓存。
- 🧪 已在 Node main（V8 14.6.202.34-node.34）和 Node v24.18.0 中用 `%HasFastProperties` 与 `--allow-natives-syntax` 验证，结果一致。
- ✅ 快速替代一：类实例，其 `prototype` 的原型为 null，例如 `new State()`，链为 instance → State.prototype → null。
- ✅ 快速替代二：先用普通对象字面量创建，再 `Object.setPrototypeOf(obj, null)`，可保留快速 map。
- ✅ 快速替代三：普通字面量；当读取的都是自有属性时，自有属性会遮蔽 `Object.prototype`，且对象可与其他同形字面量共享 map。
- 🚀 Node core WebStreams 第 16 轮：四个 per-stream 状态记录从 null 原型字面量改为类实例后，pipe-to 吞吐约 +105–112%，WritableStream 创建 +204%，ReadableStream +138%，TransformStream +134%。
- 🚀 第 19 轮：`kNilRequest`、`kNilPendingAbortRequest` 等哨兵对象改为普通字面量后再置 null 原型，pipe-to +12.3%–14.9%，带 transform 的 pipe-through +6.8%，writer 写入 +6.5%–17.6%。
- 📌 关键判断：只有创建或读取发生在热路径时，null 原型才影响性能；长期共享常量若被热路径反复读取，也属于该范畴。
- 🧭 建议：不要盲目删除所有 `__proto__: null`；优先修复每秒运行百万次路径上的对象，一次性传入 `Object.defineProperty` 等场景可忽略。
- 🛠️ 复现：文中提供 `nullproto.js` 脚本，可用 `node --allow-natives-syntax nullproto.js` 对比不同创建方式、属性读取和用作原型后的 FAST/DICT 状态。
- 🙏 结论：最便宜的优化有时是“如何创建对象”，而不是之后对对象做多少工作；感谢参与 WebStreams PR 的 V8 internals 探索。

---

### [](https://pepelsbey.dev/articles/svg-link-params/)

**原文标题**: [One SVG, nine posters: CSS linked parameters — Vadim Makeev](https://pepelsbey.dev/articles/svg-link-params/)

CSS 链接参数（CSS Linked Parameters）是一项新规范，允许把 CSS 值传入被链接的 SVG 等资源，由资源自行决定如何使用。文章以 Andy Warhol 的玛丽莲·梦露 SVG 海报为例，演示一个 SVG 文件如何通过 CSS 参数生成九种配色，并在不支持该特性的浏览器中依靠回退值正常显示。

- 🧱 传统 SVG 样式困境：内联 `<svg>` 可以使用 `currentcolor` 和继承属性；但 `<img>` 或背景图中的 SVG 是独立文档，页面 CSS 无法进入内部。
- 🆕 CSS Linked Parameters 是 Firefox 非标准 `-moz-context-properties` 的标准替代，可传入任意数量的命名值，而非只限于 `fill` 和 `stroke`。
- 🦊 支持现状：Firefox Nightly 153+ 默认开启实验实现，偏好项为 `layout.css.link-parameters.enabled`；Safari Technology Preview 253 有需手动开启的标志；其他浏览器暂无，离生产可用尚远。
- 🎛️ SVG 侧写法：用 `env(--name, fallback)` 声明可接收值，可写在表现属性或内部 `<style>` 中；因为有回退值，文件单独打开也能正常渲染。
- 🎨 CSS 侧写法：在承载图像的元素上设置 `link-parameters: param(--name, value)`；该属性不继承，必须设在带图像的元素本身。
- 🖼️ 案例：Warhol 1967 年 Marilyn 版画被描摹为四个 `<path>` 色版，对应 `--dark`、`--face`、`--hair`、`--back` 四个参数。
- 9️⃣ 同一个 SVG 被引用九次并传入九组颜色，形成九张不同海报；约 50 KB、一次网络请求，浏览器可共享底层文档但必须正确绘制每种参数化结果。
- 🛟 渐进增强免费：不支持时，SVG 中每个 `env()` 的回退值生效，页面不会坏；类似 `var(--brand, black)` 的契约。
- ⚠️ 尚未实现：Nightly 仅部分支持；`url()` 修饰符、URL fragment 传参、`param(color, …)`/`param(accent-color, …)` 简写、类型注解等缺失；内联 `<svg><use>` 和 `<object>` 暂时也不行。
- 🧪 参数不限于颜色：可传任意 CSS 声明值，包括页面中的 `var()`；SVG 侧的 `env()` 也不限于 `fill`，可用于描边宽度、透明度、变换等。
- ⏳ 结论：目前不应在生产使用，因为只有一个引擎、一个渠道、半套规范；但它值得关注，未来可实现一个图标文件适配多主题、插画跟随品牌色且作为普通缓存图像加载。

---

### [](https://kettanaito.com/blog/electron-to-pwa-and-back-again)

**原文标题**: [Electron to PWA: There and Back Again - kettanaito.com](https://kettanaito.com/blog/electron-to-pwa-and-back-again)

作者耗时一年构建 Electron 版 EPUB 编辑器，后因包体积等顾虑转向 PWA；投入约六个月重写后发现，PWA 在桌面端的关键能力与系统集成上存在根本限制，最终迁回 Electron。结论：PWA 适合增强网站或轻量套壳应用，但尚不能作为桌面应用的可替代方案。

- 📦 Electron 包体积大：Chromium shell 约 250MB，开发中一直担忧带宽与安装成本。
- ⚖️ 作者后来认为体积担忧被夸大：现代存储与网络足够快，Cloudflare 等不计出口流量，安装包大小影响有限。
- 🧱 Electron 真正痛点是低层与样板化：缺框架、HMR、窗口管理、类型安全 IPC、更新机制等；electron-builder/electron-vite 有帮助，但不是完整框架。
- 🌐 PWA 与 Electron 相似：都用 JS、运行在浏览器外壳，能力接近；且体积小、启动快、跨桌面与移动、更新现成、文件操作更顺畅、更易测试。
- 🔁 重写 PWA 较顺利：主要把主线程功能改为浏览器 API 和独立 worker，部分优化回到 Electron 后也保留。
- 🧩 PWA 文件 API 质量参差：File System API/OPFS 很好，但文件关联与启动参数 API 有重大 bug，跨浏览器差异大。
- 🍎 浏览器绑定问题：PWA 总在安装它的浏览器中打开，Safari 等兼容性差；作者一度想限制为 Chrome，感觉在和平台对抗。
- 🖥️ PWA 不像桌面应用：窗口控制/标题栏定制糟糕，无法定制托盘/程序坞菜单、系统级快捷键，部分快捷键被浏览器占用，也缺 “Open with” 等系统集成。
- 🧭 安装与发现困难：用户不熟悉 PWA，浏览器安装入口隐蔽，不利于商业软件获客。
- ↩️ 最终回归 Electron：中间短暂尝试 Electronbun；作者认为 PWA 适合“只是网页套壳”的 Electron 应用，其他需桌面集成的应用仍应用 Electron，并期待更好的框架。
- 🔮 总体判断：PWA 当前更多是网站增强和快速/离线入口，潜力未完全发挥；若补齐桌面短板，才可能成为桌面 Web 应用的主要方式。

---

### [](https://voidzero.dev/posts/announcing-vite-plus-1-0)

**原文标题**: [Announcing Vite+ 1.0 | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-1-0)

Vite+ 1.0 正式发布——由 Vite、Vitest、Rolldown、Oxc 团队打造的 Web 统一工具链，免费开源（MIT）、框架无关，通过单一命令 `vp` 将运行时、包管理器与前端工具链整合为经过测试的一体化技术栈。

- 🚀 **Vite+ 1.0 发布**：稳定版、MIT 许可，周下载量即将突破 200 万，安装命令为 `curl -fsSL https://vite.plus | bash`，随后用 `vp create` 新建项目或以 `vp migrate` 迁移现有项目。
- 🧩 **定位清晰**：它既不是框架，也不是包管理器，更不是 Vite 的替代品，而是把现有工具整合成单一配置文件和统一命令的测试化技术栈，项目甚至无需使用 Vite。
- 🔧 **九大命令覆盖开发全流程**：`vp create`（脚手架）、`vp install`（装依赖）、`vp dev`（HMR 服务器）、`vp check`（格式化+lint+类型检查）、`vp test`（单元/组件/浏览器测试）、`vp build`（生产构建）、`vp pack`（库构建与二进制）、`vp run`（带缓存的 monorepo 任务运行）、`vp env`（Node 版本管理）。
- 📄 **单一配置**：根目录一个 `vite.config.ts` 即可配置全部工具；不带参数运行 `vp` 会进入交互式提示。
- 🦀 **显著提速**：底层工具用 Rust 编写，Oxlint 比 ESLint 快 50–100 倍，Oxfmt 比 Prettier 快最多 30 倍，Vite 8 借助 Rolldown 构建更快；`vp run` 缓存任务可即时重放，`setup-vp` 将 CI 的 Node 与包管理器设置及依赖缓存合并为一步。
- 🔄 **告别工具维护**：单个 `vite-plus` 依赖替代 vite、vitest、eslint、prettier、tsup、turbo 等一堆依赖及插件配置，升级只需一次经过整体测试的版本提升。
- 🆕 **Beta 以来的更新**：新增 GitLab CI/CD 的 `setup-vp`、更多 `vp migrate` 迁移目标、Homebrew 与 Docker 镜像、`vp toolchain`、`vp env doctor`、`vp hooks` 与 `vp staged`；Vitest 5 稳定、Vite 8.1 推出实验性 Bundled Dev Mode、Oxc 原生支持 React Compiler（比 Babel 插件快 10 倍）。
- 🏢 **采用情况**：超过 2600 个公共仓库依赖 `vite-plus`，用户包括 Tiptap、Dify、vinext、BlockNote、Inkline、npmx 和 hono。
- 🔮 **未来规划**：远程缓存、更深入的 monorepo 诊断、`vp release` 与 `vp docs` 等功能正在计划中。

---

### [upm · 一个快速、小巧的 npm 包管理器](https://upm.sh/)

**原文标题**: [upm · A fast, tiny package manager for npm](https://upm.sh/)

一个面向 npm registry 的快速、轻量级包管理器，兼容常见框架与工具，并支持现有 Node.js 生态和锁文件，占用空间极小。
- ⚡ 快速且轻量：专为 npm registry 设计的包管理器
- 🧩 支持主流框架与工具：vite、vue、nuxt、next、@tanstack/react-start、nitro、h3、express
- ⬢ 兼容 Node.js，并可使用现有 .npmrc 配置
- 🔒 支持 npm、pnpm 或 bun 锁文件
- 💾 磁盘占用约 256 KB，打包后约 85 KB

---

### [隆重推出 MS](https://mswjs.io/blog/introducing-msw-3.0)

**原文标题**: [Introducing MSW 3.0 - Mock Service Worker](https://mswjs.io/blog/introducing-msw-3.0)

MSW 3.0 于 2026 年 9 月 30 日发布，在尽量减少破坏性变更的同时，完成了 ESM 化、细粒度入口、Node.js 支持更新、体积与依赖精简、GraphQL 订阅、全新 defineNetwork 网络 API，以及 Node.js 套接字级拦截架构等关键升级，并建议用户按迁移指南升级。

- 🚀 MSW 3.0 正式发布：延续 Fetch API 模拟方向，显著提升库的工作方式与能力。
- 📦 全面转为 ESM-only，原生发布 ESM 版本。
- 🧩 新增细粒度入口：`msw/http`、`msw/graphql`、`msw/sse`、`msw/ws`、`msw/utils/bypass`；根导出保留兼容，下一主版本将调整。
- 🖥️ Node.js 支持矩阵更新：弃用 v18 和 v20，支持 v22、v24、v26。
- 📉 精简依赖与体积：移除 `graphql`、`path-to-regexp`、`picocolors`、`statuses` 等；库 tarball 416KB→234KB，类型定义 190KB→90KB。
- 🗃️ `graphql` 成为可选 peer dependency。
- 🔁 GraphQL 支持补全：基于 WebSocket 拦截新增 GraphQL subscriptions。
- 🌐 引入实验性 `defineNetwork` API：区分网络来源 sources 与 handlers，未来将取代 `setupServer`/`setupWorker`。
- 🧱 新增网络原语：`NetworkSource`、`HandlersController` 等，支持自定义拦截器、HAR 回放、由测试运行器控制请求等。
- ☁️ 生态包如 `@msw/cloudflare` 已暴露 `setupNetwork`，即面向 workerd 预配置的 `defineNetwork`。
- 🛰️ Node.js 采用套接字级拦截：拦截 TCP/TLS 包装层，不 patch 请求客户端、内部类、Agent 或 `global.fetch`。
- 🔬 拦截流程：监听套接字连接，将数据包送入 `llhttp` 等解析器，确认协议消息后触发拦截，并可扩展到 SMTP 等协议。
- ⚡ 其他改进：处理器按类型分组、GraphQL handlers link-first、网站与文档重设计、`@msw/serve` 支持 WebSocket、测试覆盖提升。
- ⚠️ 迁移提醒：已有弃用、移除与 API 变更，建议阅读 2.x→3.x 迁移指南。
- 📥 安装：`npm i msw@^3.0.0`。

---

### [](https://mswjs.io/guides/integrations/react-native)

**原文标题**: [React Native - Mock Service Worker](https://mswjs.io/guides/integrations/react-native)

在 React Native 中，MSW 通过官方 `@msw/react-native` 包集成，提供预配置的 `network` 实例来拦截 `fetch` 和 `XMLHttpRequest` 请求，并自动补齐 React Native 缺少的标准 API；本文涵盖安装、配置、开发启用、测试、运行时管理 handlers 以及常见问题处理。

- 📦 集成方式：使用官方 `@msw/react-native` 包，它暴露 `network` 实例，用于 React Native 环境中的请求拦截。
- ⚠️ 使用警告：React Native 缺少部分标准浏览器 API，且某些 API 实现不符合规范，使用此集成需自行承担风险。
- 🛠️ 安装命令：通过 `npm install msw @msw/react-native --save-dev` 或 `pnpm add msw @msw/react-native --save-dev` 添加依赖。
- 🧩 无需 polyfill：该包会自行安装 `URL`、`TextEncoder` 等缺失 API，并且不会替换运行时已有的 API。
- ⚙️ 基本配置：从 `@msw/react-native` 导入 `network`，再用 `network.configure({ handlers })` 配置 handlers，用法类似 Node.js 中的 `setupServer`。
- 🚨 导入顺序：必须先导入 `@msw/react-native`，再导入任何来自 `msw` 的模块，包括 handlers。
- 🚀 开发启用：在应用入口条件调用 `network.enable()`，例如仅在 `__DEV__` 下动态导入并启用 mocking。
- 🧪 测试策略：单元/集成测试按 Node.js 集成方式搭配 Vitest 或 Jest；端到端测试需在开发中启用 MSW，并启动对应的 React Native 应用实例。
- 🔄 运行时管理：可用 `network.use()` 添加 handler 覆盖，用 `network.resetHandlers()` 移除覆盖，用 `network.disable()` 停止请求拦截。
- 🧯 常见问题一：`msw/native` 已被移除；应安装 `@msw/react-native`，将 `setupServer` 替换为 `network.configure`，将 `listen/close` 替换为 `enable/disable`。
- 🧯 常见问题二：若报错无法解析 `http`，通常是错误导入了 `msw/node`；应改为从 `@msw/react-native` 导入 `network`。

---

### [pnpm 12.7 | pnpm](https://pnpm.io/blog/releases/12.7)

**原文标题**: [pnpm 12.7 | pnpm](https://pnpm.io/blog/releases/12.7)

overview summary
- 📦 pnpm 12.7 是一次功能与修复更新，重点包括 Node 版本感知、安装/发布新参数、工作区自动转换、安全加固和大量 bug 修复。
- 🧭 全局 `node` shim 支持跟随最近的 `.nvmrc` / `.node-version`；同一目录下优先级为 `package.json` > `.node-version` > `.nvmrc`，仅 nvm 可识别的值会被忽略。
- 🛠️ 新增 `pnpm install --allow-build`，可允许/拒绝依赖生命周期脚本，并将决定记录到 `allowBuilds`。
- ⏳ 新增 `pnpm publish --publish-wait-timeout <ms>`，等待已发布版本和 tarball 可用；递归发布会先确认依赖包再发布依赖它的包，并支持 `publishWaitTimeout` 默认配置。
- 📁 没有 `pnpm-workspace.yaml` 时，`pnpm install` 会根据根 `package.json` 的 `workspaces` 字段创建它并链接项目；已有文件不会改动，`--ignore-workspace` 不会创建。
- 🚫 `pnpm install --force` 不再安装 `os`/`cpu`/`libc` 不匹配宿主平台的可选依赖；`forceIgnoresPlatform: true` 可恢复旧行为。
- ⚙️ 其他小改动：保留 `package.json` 空行、支持带注释的 `package.json5`、工作区发现顺序为 `package.json` > `package.json5` > `package.yaml`、`pnpm init --bare`、`reporter` 配置来源扩展、支持 `${VAR?}` 占位符、`publishConfig["@scope:registry"]`、Windows ARM64 运行时解析。
- 🔐 安全：项目 `pnpm-workspace.yaml` 中的 `userAgent` 不再展开环境变量；Nix 下系统工具同名 bin 不能劫持 shim/启动器；store/cache/state/modules 内的清单不再视为工作区项目；运行生命周期脚本的包不再硬链接进虚拟 store，防止改写源码或 store 副本。
- 🧠 安装修复：减少缺失 peer 依赖导致的内存耗尽、锁持有者消失时立即接管、TLS 证书失败立即报错、macOS 沙箱回退内置 CA、Windows 热安装 CPU 优化、支持 git 子模块、本地 tarball 替换重装、跳过 `devDependencies` 时不运行 `devPreinstall`/`prepare`、`--prod` 不误装仅满足可选 peer 的 devDependency、`pnpm fetch` 也会安装锁定 pnpm 版本。
- 🔗 解析与链接修复：可选 peer 同时是依赖时会重新安装；移除 `overrides` 后重新解析；`trustPolicy: no-downgrade` 选择最新非降级版本；`autoDedupe`/`pnpm dedupe` 对齐 catalog 版本；`--ignore-pnpmfile` 保留 checksum；`hoisted` 下可提升工作区包和 bin。
- 🧩 工作区与过滤：通过 symlink 到达的工作区项目会安装；catalog 指向工作区项目按工作区依赖处理；`workspace:` 支持非 semver 和构建元数据；`--frozen-lockfile` 对缺失工作区项目报错；注入包获得自身脚本输出；`--filter` 选择器按顺序求值，后续 inclusion 可重新包含。
- ➕ 增删改：`pnpm add` 在生命周期脚本前保存 `package.json` 并保存精确版本；`add/update <pkg>@<version>` 会移动 catalog 条目；`update` 保留仍满足的范围；`unlink` 移除 `link:` 依赖；`catalogPrune: true` 时清理未引用 catalog；支持 Yarn `patch:` 导入和 `sharedWorkspaceLockfile: false` 下的 patch。
- ▶️ 脚本执行：无终端脚本会随 pnpm 被杀而结束；`--filter`/`-r` 可运行依赖中的命令；`exec`/`dlx` 设置更多 npm 环境变量；`restart` 无脚本时运行 `stop` + `start`；`dlx` 按 Node 主版本分缓存；`pipeline` 可在 Git 工作树外运行且不缓存；`runtime:` 范围安装运行时而非 `node` npm 包。
- 📦 发布与部署：`publish` 无需 `node_modules` 解析 `workspace:` 依赖；`pack`/`publish` 支持 bundled 依赖、包内 symlink 和可执行权限；`deploy` 复制 `packageManager`、遵循 `virtualStoreDir`、跳过 `prepare`。
- 🌐 全局包与 Windows/WSL：全局命令使用当前调用的 pnpm；`self-update` 同时更新全局 pnpm 且不残留旧 `@pnpm/exe`；`setup` 修复 `Text file busy` 和误删 shell 启动文件行；Windows/WSL 等待被占用文件、重试保存锁文件、转义目录尾随点和空格、Git Bash 等环境传 Windows 路径。
- 🔎 审计与查看：`pnpm audit` 支持 `--filter` 并列出各受影响项目路径；工作区内 `list`/`licenses list` 默认只列当前项目；`list --only-projects` 打印所有选中项目；`licenses list` 兼容 `sharedWorkspaceLockfile: false` 和 `hoisted`；`store status` 不再把有构建脚本的包误报为已修改。
- 🧾 完整变更见 v12.7.0 发布说明。

---

