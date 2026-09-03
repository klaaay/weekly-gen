### [PlanetScale -](https://planetscale.com/?utm_source=this_week_in_react&utm_medium=email&utm_campaign=2026_q3_this_week_in_react&utm_content=slot_1)

**原文标题**: [PlanetScale - the worldâs fastest and most scalable cloud hosting for Vitess and Postgres](https://planetscale.com/?utm_source=this_week_in_react&utm_medium=email&utm_campaign=2026_q3_this_week_in_react&utm_content=slot_1)

PlanetScale 提供业界领先的云端数据库服务，涵盖 Vitess/MySQL 与 Postgres 两大产品线。其最大特色在于结合 NVMe 无限 IOPS 的极速性能、基于 Vitess 与 Neki 的横向扩展架构，以及高可用性设计。平台同时强调安全性（SOC 2/HIPAA/PCI DSS 合规）、成本效益，并配备分支开发、在线迁移、流量管控等丰富的开发者功能，是目前大规模高并发工作负载的理想选择。

- ⚡ **极致性能**：采用 NVMe 驱动器提供无限 IOPS，性能远超 Aurora 等竞品，并支持如“PlanetScale Metal”的快速套餐方案。
- 🔄 **横向扩展**：Vitess 支持 MySQL 水平分片，架构源自 YouTube 生产环境；Neki 则针对 Postgres 提供下一代分片能力。
- ☁️ **灵活部署**：提供多区域、多云（AWS/GCP）以及“Bring Your Own Cloud”托管选项。
- ⏱️ **高可用性**：具备跨可用区的主备架构、自动故障转移，并承诺高达 99.999% 的 SLA。
- 🛡️ **合规安全**：通过 SOC 2、HIPAA、PCI DSS 等认证，并提供安全的连接方式（如 PrivateLink）。
- 🧩 **开发工作流**：核心特色是数据库“分支”功能，支持无停机在线迁移、安全模式变更及一键回滚。
- 🔭 **可观测性**：内置 Query Insights 等工具，可全面监控集群健康与查询性能。
- 💰 **成本效益**：相比 RDS 与 Aurora，对多数工作负载成本更低，并提供高性价比的 Metal 套餐。
- 🤖 **智能管理**：具备 AI 代理驱动的数据库优化能力，保障安全访问。
- 🚀 **广泛客户**：Slack、Etsy、GitHub、Block 等巨头处理 PB 级数据时都信赖此方案。
- 🌐 **全球加速**：通过全局边缘网络与只读区域设计，显著降低跨区域读延迟。
- 🛠️ **生态集成**：支持 Datadog、Prometheus 等多种监控和数据处理生态工具。

---

### [自优化数据库 - PlanetScale](https://planetscale.com/docs/self-improving-database)

**原文标题**: [Self-improving database - PlanetScale](https://planetscale.com/docs/self-improving-database)

PlanetScale MCP 服务器让 AI 编码代理结合生产环境性能数据（Insights）和 Schema Recommendations，自动定位并优化高影响查询，经过开发环境验证后提交 pull request，形成数据库性能自我改进的闭环；该方案支持 Postgres 与 Vitess，可手动运行，也能通过 Cursor Automations 定时执行。

- 🤖 MCP 服务器为 AI 代理提供 Insights 与 Schema Recommendations 数据，使它能够结合代码库执行性能优化。
- ⚙️ 核心流程：拉取性能数据 → 定位影响最大的查询或 schema 问题 → 搜索相关代码 → 修改 → 开发环境验证 → 提交 PR。
- 🔁 优化任务可一次运行，也可用 Cursor Automations 在后台按每日/每周计划自动执行。
- ✅ 使用前需满足：安装并认证 MCP 服务器、使用 MCP 兼容的 AI 编码代理、数据库已有 Insights 数据，并通过 AGENTS.md 指定 org、database、branch。
- 🔒 如需最小权限，可使用仅含 Insights 的 MCP 服务器（insights-only），避免向代理暴露查询执行工具。
- 🧭 建议从手动迭代开始：先运行示例提示词、审查生成的 PR，再逐步加入针对代码库的 guardrails（目录、ORM、linter、迁移命令等），稳定后再升级为定时任务。
- 📊 Insights 优化提示词要求代理分析影响最大的查询——例如慢查询、高 rows read、高频或高 egress，并在修改前用 EXPLAIN 建立基准。
- 📝 提示词中还应包含规则：一次只优化一个查询、检查是否已有重复 PR、修改后再次基准测试、运行 linter，并在 PR 描述中说明选择理由、预期影响与前后对比。
- 🗂️ Schema Recommendations 提示词让代理查找未处理的 schema 推荐并实现最早的一条；若无推荐则什么都不做，同样一次只处理一条。
- ⚠️ 涉及删除表或列时必须分两步走：先移除代码中所有引用并安全部署，之后才能执行 schema 层面的删除变更。
- 🧪 取得可靠结果的关键：单次只修一个问题、在开发环境用 EXPLAIN 验证、用 AGENTS.md 提供上下文、针对自己的技术栈定制提示词。
- 🛡️ 所有自动生成的 PR 仍需人工审查后才能合入生产，因为 schema 与查询变更需要结合业务判断。

---

### [StyleX — 适用于宏大界面的样式系统](https://stylexjs.com/)

**原文标题**: [StyleX — styling system for ambitious interfaces](https://stylexjs.com/)

overview summary
StyleX 是一个适用于高要求界面的样式系统，强调表现力、类型安全、可组合、可预测和主题化能力。页面提供了完整的开发者资源，包括快速上手、思考指南、文档、API、Playground、博客与 GitHub 等入口。

- 🎨 具表现力（expressive）的样式系统，专为雄心勃勃的界面设计
- 🔒 类型安全（type-safe），减少样式错误
- 🧩 可组合（composable），支持灵活复用样式
- 🔮 可预测（predictable），样式行为稳定可控
- 🎭 可主题化（themeable），便于定制与换肤
- 📚 提供丰富开发者资源：Get Started、Thinking in StyleX、Develop、Learn、API
- 🧪 提供 Playground 与 Blog，方便实践与交流
- 🐙 开放 GitHub 参与渠道，支持社区贡献
- 📄 页面含常见法律、隐私、条款链接，版权归属于 Meta Platforms

---

### [](https://astryx.atmeta.com/)

**原文标题**: [Astryx Design System](https://astryx.atmeta.com/)

这句话是用户在等待订单时发出的简短询问，核心表达了对订单配送状态的急切关注，以及希望获得清晰、实时信息的需求。

- 📦 订单疑问：明确表示用户想知道自己的订单目前在哪里。
- 🔍 追踪需求：暗示用户希望获取物流进度或配送状态更新。
- ⏳ 情绪信号：可能透露出等待时间较长或信息不透明带来的焦虑。
- 🛒 应用场景：常见于电商购物后的订单查询或与客服沟通中。

---

### [](https://linear.app/now/styling-linear-for-the-future-stylex)

**原文标题**: [Styling Linear for the future with StyleX](https://linear.app/now/styling-linear-for-the-future-stylex)

Linear 团队在历经数月、超过 1000 个 PR 后，将 React 应用的样式方案从 styled-components 迁移到 StyleX。文章讲述了这次大规模迁移的原因、工具与 AI 代理结合的执行方式、配套规范建设，以及最终的收益。

- 🔄 背景：styled-components 曾足够灵活，但类似 `styled(Button)` 的开放 API 导致“远距离改样式”和 UI 回归，React 18 并发渲染后还出现性能退化。
- 🧠 选型：团队要求新方案需在构建时生成样式、避免远距离样式修改、提供可预测的样式合并；StyleX 相比 vanilla-extract 更贴合 colocated 风格和团队使用习惯。
- ⚖️ 权衡：迁移到原子 CSS 让父级选择器、全局选择器等模式更难实现，但这恰恰消除了旧系统在高复杂度下难以推理的问题。
- 🤖 执行路径：先通过确定性 codemod 驱动，再让 AI 代理辅助处理边界情况；代理能力随 Fable、Sol 的发布逐渐加强，但人工判断始终不可缺失。
- 🧩 降低风险：新旧系统共存期先定义 StyleX 变量和共享原语，代理任务有窄边界和清晰检查清单，并从叶子组件开始迁移，避免触碰级联风险。
- 📊 推动采纳：开发者工具条显示每页 styled-components 剩余数量，可视化组件归属和每周迁移图表；PR 机器人拦截新增 styled-components 文件。
- 🛠️ 强制规范：用自定义 lint 规则与 oxlint 覆盖常见错误和设计 token 使用，并通过类型感知的仓库级检查器追踪 `sx`、`className`、`style` 跨文件的合并与传播。
- 🔍 规则分类：包括遗留清理、`sx` 接口契约、样式覆盖与简写检查、设计交互一致性，以及编译器/运行时/主题安全的保障。
- 🎨 保留逃生舱：CSS Modules 用于全局选择器或第三方 DOM；ThemeProvider 扩展 StyleX 主题，支持按照需要的子树注入动态生成的多样化主题。
- 🚀 性能收益：对比测试显示，移除运行时样式注入后，视图密集型页面主线程 CPU 工作量降低约 20–35%，中端设备约提速 30%，导航时 CSS 注入从数百条降到零。
- 🏁 长远价值：迁移后组件样式契约明确、优先级确定性高、工具实现强制约束；系统在运行时更快、更不容易被误用，也更适合 AI 代理协作开发。

---

### [](https://flaviocopes.com/stylex/)

**原文标题**: [A deep dive into StyleX](https://flaviocopes.com/stylex/)

StyleX 是一种 JavaScript 语法与编译器，用于在构建时将样式对象编译为普通 CSS，使开发体验类似 CSS-in-JS，但浏览器收到的是静态类名，无运行时注入。文章涵盖其核心心智模型、React/Vite 与 Astro 集成、主要特性（组合、变体、伪类、响应式、主题、令牌等）、静态约束、对比其他方案及适用场景，并强调其在编码代理（agent）方面的优势与权衡。

- ⚙️ StyleX 将 `stylex.create()` 中的 JS 样式对象在编译时转为小型可复用原子 CSS 类，组件通过 `stylex.props()` 组合类名，无 CSS-in-JS 的生产期注入。
- 🧩 核心要解决的问题：全局类名冲突、样式覆盖不可预测、样式归属不清、未使用 CSS 过多。StyleX 让样式就近组件、类名不可碰撞、冲突按传入顺序解决。
- 🔧 手动配置 React + Vite：安装 `@stylexjs/stylex` 与 `@stylexjs/unplugin`，并在 `vite.config.ts` 中先启用 `stylex.vite({dev,useCSSLayers})` 再放 React 插件。
- 🔎 调试时可使用 StyleX DevTools Chrome 扩展，通过 `data-style-src` 属性和可读标记类名定位样式来源。
- 🚀 也可用于 Astro：通过 Vite 插件接入，React 组件可静态渲染或无交互时零 JS 输出；全局 CSS 与 StyleX 分层共存。
- 🌱 StyleX 生成原子 CSS：每条声明独立成类，相同属性和值可在全局复用，减少 CSS 重复，HTML 中类名增多但样式表体积增长缓慢。
- ✨ 样式组合使用 `stylex.props(styles.card, styles.featured)`，后传入的样式覆盖前者，冲突由 JS 层在传给浏览器前解决。
- 🎯 支持条件样式（真值/三元表达式）、变体对象查找、`:hover`/`:focus` 等伪类，以及 `@media`、`@supports` 等媒体查询，均以“属性优先”结构内联表示。
- 🔑 动态值（如进度条）可通过样式的函数形式实现，编译器会生成静态类 + CSS 变量，将真实值放入 `style` 属性，但参数和函数体受限。
- 🎨 用 `stylex.defineVars()` 创建设计令牌，`stylex.createTheme()` 定义主题变量组；组件消费语义令牌，主题决定具体值。
- 🔓 组件可通过 `StyleXStyles` 类型接受父级传入的样式对象，并可限制允许的 CSS 属性，构成类型化的自定义契约。
- 🎞️ 动画使用 `stylex.keyframes()` 自动生成并引用名称；`@stylexjs/atoms` 提供实用原子类应对小型局部异常。
- ⛓️ StyleX 具有静态约束：样式对象不能使用任意 JS、import 普通值或对象展开，需改用 `defineVars` / `defineConsts` 或 `props` 组合，以保证可编译。
- 🌐 全局 CSS 仅负责 reset、字体、文档默认值等；复杂关系状态需使用 `stylex.when` 和 marker 类，避免全局选择器影响无关元素。
- 🔍 ESLint 插件可检测未用样式、简写冲突、键排序，并能通过 `propLimits` 限制属性允许值（如固定间距刻度），让类型和 lint 约束设计决策。
- 🤖 StyleX 对编码代理尤其有意义：它比 Tailwind 更冗长，但限制了无效选择空间，让代理更不容易写出不一致的样式，也让代码审查更聚焦。
- ⚠️ 代价包括：构建配置更复杂、语法比 Tailwind 类长，第三方组件生态多为 Tailwind，需要转换；依赖纯 JavaScript 组件体系，不适合全局大样式表或内容驱动页面。
- 📊 对比：与普通 CSS、Tailwind、运行时 CSS-in-JS 相比，StyleX 优点是可预测组合和低运行时代价，主要成本是编译器设置和严格规则。
- 🗓️ 适用场景：新 React 应用、组件库增长、大量 AI 或代理编写/修改 UI 时。不适用于小型静态站或 Markdown 内容为主的页面（如 flaviocopes.com）。
- 🏗️ 生产构建后应检查 `dist/assets` 中的 CSS 为哈希原子规则，应用代码中不再存在原始 `stylex.create()` 对象，以确认编译成功。

---

### [](https://github.com/aidenybai/tailwind-stylex)

**原文标题**: [GitHub - aidenybai/tailwind-stylex: Bring Tailwind design system to StyleX · GitHub](https://github.com/aidenybai/tailwind-stylex)

tailwind-stylex 是一个连接 Tailwind CSS 与 StyleX 的开源工具，它把 Tailwind 的默认设计令牌转换为可直接在 StyleX 中使用的类型安全常量，支持自动补全且免去自定义配置、扫描或生成步骤。

- 🎯 核心目标：让 StyleX 开发者直接复用 Tailwind 默认设计系统，获得类型提示和自动补全体验。
- 📦 安装命令：使用 pnpm 安装 `tailwind-stylex` 和 `@stylexjs/stylex`。
- ⚙️ 编译配置：若用 `@stylexjs/unplugin`，需在 `externalPackages` 中加入 `"tailwind-stylex"`；若用 postcss 插件，则需在 `include` 中添加 `node_modules/tailwind-stylex/tokens.stylex.js`。
- 💡 基础用法：从 `tailwind-stylex/tokens.stylex` 导入 `colors`、`spacing`、`radii` 等令牌，并在 `stylex.create` 中直接使用；如 `colors.stone100`、`radii.lg`、`spacing[4]`。
- 🔢 数值令牌写法：对带数字的名称使用方括号，例如 `fontSizes["2xl"]`、`containers["7xl"]`、`spacing[8]`。
- 🗂️ 令牌分类丰富：提供颜色、布局（间距/断点/容器等）、排版（字体/字号/行高等）、表面效果（圆角/阴影/模糊）、动效（缓动/动画/透视）以及默认值。
- ✨ 编辑器支持：每个令牌都能自动补全并显示精确取值。
- 📜 开源许可：项目基于 MIT 许可证发布，当前拥有 81 颗 Star。

---

### [](https://syntax.fm/show/1035/why-everyone-is-moving-to-stylex)

**原文标题**: [Why everyone is moving to Stylex? - Syntax #1035](https://syntax.fm/show/1035/why-everyone-is-moving-to-stylex)

Overview summary  
Meta 的 StyleX 正迅速普及，它在构建时将大量样式编译为少量可复用类名，实现零运行时与完全类型安全。本期 Syntax 播客探讨了它与其他 CSS 方案的区别，为何对 AI 代理特别友好，以及其优缺点与替代方案。

- 🎙️ StyleX 是 Meta 开发的 CSS 工具，核心是在构建时把数千条样式压缩成少量可复用类名，运行时无需任何处理。  
- 🔍 与传统的 CSS 作用域方法不同，StyleX 专注于编译期优化，而非依赖运行时或特定框架机制。  
- 🤖 许多开发者认为 StyleX 对 AI 代理更友好，因为它结构清晰、可预测性高，便于自动化生成与维护样式。  
- 🛡️ StyleX 提供完全类型安全，并支持设计系统约束，能从编译层面限制非法或不一致的样式使用。  
- ⚙️ 无运行时依赖：所有样式都在构建时计算完成，不向浏览器发送额外 JS，有效提升性能。  
- 📦 样式可以像模块一样导入、导出和自动导入，支持跨文件复用，避免重复定义。  
- 🧩 支持通过 JavaScript 对象进行组合与覆盖，令样式的扩展和覆盖逻辑更直观灵活。  
- ✍️ 缺点是手写体验较差：语法相对冗长，对开发者不够友好，更适合由工具或代理生成。  
- ⏳ 现代 CSS 属性往往要等待实现，StyleX 的编译方式可能滞后于最新 CSS 特性落地。  
- 🪆 嵌套 CSS 与嵌套选择器处理起来很棘手，StyleX 选择了更平坦、显式的样式结构来规避复杂性。  
- 🔄 主要替代方案包括 Panda CSS 和 CSS Modules，它们各有不同的作用域策略和开发体验。  
- ✨ 自动补全体验极佳：由于样式结构严格且类型明确，StyleX 在 AI 代理辅助编码时表现尤为突出。

---

### [i18n 与 AI | Lingui](https://lingui.dev/ai-tools)

**原文标题**: [i18n with AI | Lingui](https://lingui.dev/ai-tools)

Lingui 为 AI 工具提供了多种资源，帮助开发者更准确地进行国际化（i18n）开发，涵盖可复用的技能包、文档文件和实时文档检索服务。

- 🤖 **Agent Skills（代理技能）**：提供可复用的最佳实践与故障排查指南，减少 AI 对 Lingui API 的误用和幻觉。
- 🛠️ **多种安装方式**：支持 Skills CLI、Claude Code 插件、Plugins CLI、Gemini CLI、GitHub CLI 等，可整体或单独（`--skill`）安装。
- 📄 **Context Files（上下文文件）**：提供 `llms.txt` 和 `llms-full.txt` 静态文档，适合作为兜底参考，但体积大、需定期更新。
- ⚡ **Context7 MCP**：通过实时索引和按需搜索提供最新文档，token 消耗低，是首选方案。
- 🔧 **快速使用**：在提示中加 `use context7`，或直接配置 MCP 服务器（`npx -y @upstash/context7-mcp`）即可接入。

---

### [](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/75429)

**原文标题**: [[react] 19.3 by eps1lon · Pull Request #75429 · DefinitelyTyped/DefinitelyTyped · GitHub](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/75429)

该 PR 是 DefinitelyTyped 仓库中针对 React 19.3 的草稿类型定义更新。它由协作者 eps1lon 发起，目标是将原本仅存在于 canary 通道中的 React 类型迁移到稳定入口，并同步调整 react-dom 等多个相关类型包，使类型定义匹配 React 19.3 的预发布版本。

- 📝 草稿 PR #75429 标题为“[react] 19.3”，目标分支为 DefinitelyTyped master，用于支持 React 19.3 的 TypeScript 类型。
- 🔀 PR 包含两个主要提交：将 `react-dom` 的 `browser()` 类型移至稳定，以及将 React 其余 canary 类型迁移到稳定入口。
- 🧩 `react-dom` 中，`browser()`、`BrowserUsable` 返回类型和 `RendererUsable` 注册项等被移入主 `index.d.ts`，并新增 `@version 19.3.0` JSDoc 标记。
- ⚛️ `react` 中，`<ViewTransition>` 组件、`addTransitionType`、`FragmentProps` 的 `ref`、`SubmitEvent` 的 `submitter` 等均转为稳定类型，ts5.0 fork 也保持同步。
- 🗂️ `unstable_useCacheRefresh` 仍保留在 `react/canary`；两个 canary 入口被保留以供旧引用解析，但 `react-dom/canary` 已变为空壳。
- 🧪 对应测试从 canary 测试文件移动到稳定测试文件，并用真正的 `$ExpectType` 断言替换了过时注释。
- 📦 多个 `@types` 包版本提升到 19.3.9999：`@types/react`、`@types/react-dom`、`@types/react-is`、`@types/react-test-renderer` 等，`@types/react-dom` 对 `@types/react` 的 peer dependency 下限升至 `^19.3.0`。
- 🔄 `react-refresh` 类型同步更新：移除运行时已删除的 `findAffectedHostInstances`，新增导出的 `_getMountedRootCount`。
- 👀 当前 PR 状态为 Needs Author Action，并等待 johnnyreilly 与 Jessidhia 在标记 ready 后进行审查。

---

### [浏览器 – React](https://react.dev/reference/react-dom/browser)

**原文标题**: [browser – React](https://react.dev/reference/react-dom/browser)

`browser` 是 React 在 Canary/Experimental 渠道提供的 API，配合 `use` 使用，可将组件标记为“仅在浏览器端渲染”。在服务器渲染期间，它会暂停组件渲染并显示最近的 `<Suspense>` 回退内容；在浏览器中则返回 `undefined`，组件正常渲染。该 API 提供可选的 `reason` 参数，用于向 `onBrowserBailout` 报告原因；同时也能用于中止服务器渲染并让浏览器接管后续内容。

- 🧪 仅限 React Canary/Experimental 渠道使用，不可用于稳定版
- 🏷️ 通过 `use(browser(reason?))` 调用，将组件标记为仅浏览器渲染
- 🖥️ 服务器渲染时：组件被跳过，最近的 `<Suspense>` 显示 fallback；浏览器中返回 `undefined` 并正常渲染
- 📝 可选参数 `reason`：字符串或函数，作为 `onBrowserBailout` 错误的 `cause`；函数仅在服务器端调用，适合延迟创建 Error
- ⚠️ 使用限制：服务器渲染时必须在 `<Suspense>` 边界内；React Server Components 应用中必须在 Client Component 中调用；单独调用 `browser()` 无效，必须传给 `use`
- 💾 典型场景：读取 `localStorage` 等浏览器专有 API，代替 `typeof window` 或 effect 挂载判断
- 🔀 支持条件调用：可在组件或 Hook 中根据条件（如 prop 是否存在）决定是否跳过服务器渲染
- 📡 服务器端可通过 `onBrowserBailout` 回调报告浏览器专属渲染的发生，并获取错误信息与组件栈
- ⏳ 可用 `browser()` 作为 `abort()` 的原因，中止挂起的服务器渲染，让浏览器完成剩余内容渲染，且不会触发 `onError`/`onRecoverableError`

---

### [](https://vercel.com/kb/guide/deploy-a-tanstack-start-app-to-vercel)

**原文标题**: [How to Deploy a TanStack Start app to Vercel | Vercel Knowledge Base](https://vercel.com/kb/guide/deploy-a-tanstack-start-app-to-vercel)

这是一个关于如何将 TanStack Start 应用部署到 Vercel 的完整指南。借助 Nitro Vite 插件，Vercel 可以自动识别项目并完成构建，开发者能通过 Git 或 Vercel CLI 快速部署，服务端函数默认运行在 Fluid compute 上，并按实际 CPU 使用计费。文中还介绍了环境变量配置、部署验证、常见故障排查及 FAQ。

- 📘 TanStack Start 是基于 TanStack Router 的全栈框架，搭配 Nitro 构建输出为 Vercel Functions
- ⚙️ 先决条件：Vercel 账号与 CLI、Node.js 24+、已有的 TanStack Start 项目及 Git 仓库
- 🔌 安装 Nitro：在项目根目录使用 pnpm、yarn、npm 或 bun 添加 `nitro`
- 🧩 注册插件：在 `vite.config.ts` 的 plugins 数组中加入 `nitro()`，与 TanStack Start 插件并列
- 🔐 环境变量：通过 Vercel 控制台或 `vercel env add` 设置；`VITE_` 前缀变量会进入客户端，无前缀变量仅供服务端安全使用
- 🚀 部署方式：从 Git 仓库导入可自动检测框架；CLI 运行 `vercel` 预览，`vercel --prod` 直接发布
- ✅ 验证部署：检查 SSR 内容渲染、路由导航和 server functions 响应；404 通常代表 Nitro 插件缺失或配置错误
- 🛠️ 框架检测失败时，可在 Dashboard、`vercel.json` 的 `framework: "tanstack-start"` 或用 CLI 手动指定
- 🐛 本地构建成功但 Vercel 返回错误，请核对 Node.js 版本及项目设置是否一致
- 💸 Fluid compute 默认启用，按活跃 CPU 计费，不收取空闲时间费用，并可随流量自动扩缩容
- ⚡ 性能优势：静态资源走 CDN、函数实例复用降低冷启动，支持流式 SSR 加快首屏展示
- ❓ FAQ 要点：支持开箱即用、自动创建预览部署、Hobby 免费起步、Pro/Enterprise 适合商业化与团队协作

---

### [](https://nextjs.org/blog/august-2026-security-release)

**原文标题**: [August 2026 Security Release | Next.js](https://nextjs.org/blog/august-2026-security-release)

Next.js 发布了 2026 年 8 月安全更新，修复了多个严重漏洞。官方在提前检测到上游新问题后，为 v16.3.3（Active LTS）和 v15.5.24（Maintenance LTS）提供了修复版本，强烈建议用户尽快升级以保护应用安全。

- 🔒 紧急安全发布：官方提前发布安全更新，新增一个涉及上游依赖的严重漏洞；版本 v16.3.3 与 v15.5.24 现已可用。
- ⚙️ 升级命令：用户需通过 npm 升级 next 依赖（15.5 系列使用 `npm install next@15.5.24`，16.3 系列使用 `npm install next@16.3.3`）。
- 🖼️ 严重漏洞一：图像优化 API 在处理攻击者控制的 AVIF 图片时可触发未认证远程代码执行（与 libheif/sharp 相关）；新版本将禁用 AVIF 优化直至上游修复完成。
- 🖥️ 严重漏洞二：使用 Pages Router 与 App Router 且没有 Cache Components 的应用，若是 Windows 文件系统环境，可能遭受未认证远程代码执行；Linux/macOS 不受影响，且无已知临时缓解措施。
- 🛡️ 安全计划：Vercel 通过开源漏洞奖励项目邀请研究者参与，相关疑问可联系 security@vercel.com。

---

### [](https://reactadvanced.com/?utm_source=thisweekinreact)

**原文标题**: [React Conference In London, October 23 & 26, 2026](https://reactadvanced.com/?utm_source=thisweekinreact)

本次 React Advanced Conference 是一個於 2026 年 10 月 23 日與 26 日在倫敦及線上同步舉行的混合式進階 React 開發者大會，涵蓋 AI 工程、全端開發、React Server Components 等深度技術主題，並提供工作坊與多元交流機會。

- 📅 活動時間：10 月 23 日為倫敦現場加線上直播日，10 月 26 日為全日遠端日，預計吸引超過 800 位現場與 5000 位全球遠端開發者參與。
- 🎤 講者陣容堅強：邀請 40 多位來自 Vercel、Google DeepMind、Meta、Shopify、Apollo GraphQL 等公司的核心貢獻者與資深工程師分享實戰經驗。
- 🤖 AI 主題貫穿全場：涵蓋 AI Agents、AI 輔助開發、AI 編程工具、In-Browser ML、AI 生成 UI 與 AI 安全等新興領域的深度探討。
- ⚛️ 核心技術議程：聚焦 React 19、React Server Components、Next.js Cache、React Compiler 等框架生態系統的最新架構趨勢與實際採用策略。
- 🏢 四大主題深潛（Deep Dives）：包含全端開發與架構、AI Agents 與輔助編碼、AI 工程應用，以及從工程師成長為 Tech Lead 的職涯技能。
- 🛠️ 工作坊規劃：提供 5 場以上免費與付費的遠端實作工作坊，主題涵蓋現代 React 架構、Claude Code、TanStack AI 與 React DevOps 實務。
- 🎟️ 票價方案多元：Hybrid 全票 £540，組合 TechLead Conf 票 £690，遠端早鳥票 €180，另有 Multipass 訂閱方案（每月 €17）可參加多場 GitNation 會議。
- 💻 現場與虛擬互動：安排現場與線上的混合社交活動、講者問答、主題討論室，以及倫敦現場的 React Party（含卡拉 OK 與招待會）。
- 📍 場地資訊：實體活動將在倫敦市中心 Chiswell Street 52 號的 The Brewery 前 Whitbread 釀酒廠舊址舉行。
- 🎓 社區回饋：GitNation 提供 100 個多元獎學金名額，支持 underrepresented 與財務弱勢的技術人才免費參與大會。

---

### [让 React Testing Library 测试速度提升 43% • sigh.dev](https://sigh.dev/posts/making-react-testing-library-faster/)

**原文标题**: [Making React Testing Library Tests 43% Faster • sigh.dev](https://sigh.dev/posts/making-react-testing-library-faster/)

overview summary：本文介紹了在 Sentry 的 HackWeek 中，透過針對 jsdom 與相關函式庫的三項底層最佳化，讓 React Testing Library 測試速度提升 43%，且完全不改測試程式碼；過程中使用 Codex 輔助分析與驗證，重點在於讓修補真正落地於開源套件。

- 🚀 最終成果：在 jsdom 30 上，三項變更合併後測試從 17.18s 降到 9.77s，比原本 jsdom 26 的 12.41s 還快 21%，整體加速 43%。
- 🧠 核心策略：不改測試寫法（不換 getByRole、不用 getByTestId、不換 userEvent），只加速底層機制，讓測試維持原樣但更快。
- 🤖 Codex 協作過程：先從寬泛目標開始，並設法讓 Codex 在真實測試中驗證，避免只信微基準測試，也阻止它走偏（拆測試檔、改用便宜查詢、改 React runtime）。
- 🏷️ 最大優化：jsdom 的 input.labels 處理改為建立「label 到 control」的索引並共享，避免每次查詢都重複掃整個 DOM；100 個控制的 labels 讀取從 60.52ms 降到 0.67ms（約快 91 倍）。
- ⚡ 選擇器快速路徑修復：DOMSelector 原本因文件封裝物件比較永遠不等，導致 matches() 走不到快速路徑；修正後 matcher 基準測試快 89%，getByRole('button') 大基準快 42%。
- 🔄 事件路徑優化：jsdom 在建立事件路徑時直接記錄 effective target，並略過沒有監聽器的元素準備，事件吞吐量依樹深度與監聽器數量提升 12%–36%。
- ✅ 適用場景：大型且多 label 的表單、大量使用 getByRole 搭配 accessible name、深層 DOM 樹、頻繁 userEvent/fireEvent、依賴 matches() 的函式庫，才會明顯受惠。
- 📦 目前狀態：label cache 與 event-path 修正已合進 jsdom，但尚未發布；DOMSelector fast-path 修正仍在審核中。

---

### [](https://tendto.github.io/en/posts/ssg-for-react-with-vite/)

**原文标题**: [Tentopolis > SSG for React with Vite](https://tendto.github.io/en/posts/ssg-for-react-with-vite/)

文章介绍如何用 React 和 Vite 实现 SSG（静态站点生成）：先比较 CSR、SSR 与 SSG 的优劣，指出 SSG 在许多场景下是更实用的默认选择；再逐步改造标准 Vite React 项目，在构建时用 renderToString 预渲染 HTML，并在客户端用 hydrateRoot 水合页面。文章还提醒水合匹配的常见陷阱，并列举了可直接使用的替代方案。

- ⚛️ 作者通常用 React + Vite 开发 SPA，但也认可 SSG 能减少首屏计算、提升 SEO 并支持静态托管。
- 📄 默认 CSR 项目中，index.html 只包含空 `#root` 和脚本，页面内容需等 JavaScript 执行后才能生成。
- 📊 CSR 客户端负担高、服务端负担低、可静态托管，但首屏慢且 SEO 差；SSR 反之但无法静态托管；SSG 兼顾低客户端负担和静态托管能力。
- 🧠 SSG 还没成为默认配置，作者认为主要原因是惯性，类似 IPv4 到 IPv6 的迁移阻力。
- 🛠️ 实现 SSG 的核心是在 build.tsx 中通过 `renderToString` 把 React 组件渲染成 HTML 字符串，并 mock 掉 `localStorage` 这类浏览器 API。
- 📝 修改 index.html，在 `#root` 中加入 `<!-- ReactApp -->` 占位符，用于后续插入预渲染内容。
- ⚙️ 在 vite.config.ts 中添加自定义插件，仅在 production 模式下用 `transformIndexHtml` 将占位符替换为预渲染 HTML。
- 🔄 main.tsx 中需根据环境切换：开发环境用 `createRoot`，生产环境用 `hydrateRoot`，让 React 直接复用现有 DOM 并绑定事件。
- ⚠️ 水合要求预渲染 HTML 和客户端虚拟 DOM 完全一致；需避开多余空白、浏览器专属 API、服务端与客户端渲染结果不同等陷阱。
- 🧩 若不想自己实现，可使用 Vite Plugin React SSG、Next.js、Astro 等现成方案；自制方案的优势是零额外依赖且构建过程可定制。
- ✅ 多数项目更适合 SSG，但若首屏内容强依赖用户登录状态、偏好等客户端数据，CSR 仍有其价值。

---

### [](https://posthog.com/newsletter/context-engineering?utm_source=twir&utm_campaign=sept2)

**原文标题**: [We used context engineering to 5x conversion and 2x activation](https://posthog.com/newsletter/context-engineering?utm_source=twir&utm_campaign=sept2)

PostHog 团队分享了他们如何用“上下文工程”构建 AI 引导向导 PostHog Wizard，成功让付费转化提升 5 倍、激活速度提升 2 倍，并总结出六条核心经验：重点不是提升推理能力，而是为 Agent 持续提供准确、新鲜、可组合的上下文。

- 🧭 从摩擦日志出发：团队通过观看用户录屏发现接入 PostHog 的痛点，于是用一条 CLI 命令打造 AI 向导，把原本 2 小时的接入压缩到 8 分钟。
- 🧠 第 1 课｜推理不是瓶颈：复杂的规划、子代理、剪枝等手段提升有限；真正让 Agent 质变的是喂入更多更有针对性的上下文。
- 📦 第 2 课｜不要硬编码知识：他们建起“上下文工厂”（context mill），从文档、源码、API 规范等来源打包成可版本化的技能包，让 Agent 无需重新部署即可远程获取新知识。
- 🔄 第 3 课｜在源头修复上下文漂移：代码迭代太快导致文档过期，于是加入“文档代理”，让每个功能 PR 自动生成文档 PR，经人工审核后保持文档与代码同步。
- 🧩 第 4 课｜复用上下文组合新技能：通过声明式 YAML 规范共享基础内容并定义变体，向导支持的框架从 5 个扩展到 25 个以上，还催生了如 audit-3000 这样的新技能。
- 🌐 第 5 课｜消除上下文孤岛：用 API、MCP、CI/CD 等连通公司内部各种知识源（包括开源手册），让上下文自由流动；同一个上下文层还能支撑销售、支持和营销等各类 Agent。
- 💰 第 6 课｜投资上下文回报极高：向导用户付费转化率从 2.6% 提升到 14.2%，首次事件时间从 3.8 小时缩短到 1.9 小时，首月 MRR 增加 80%。
- 🧰 总结：构建公司级上下文层是未来所有 Agent 业务的高杠杆投资，也催生了全新的“上下文工程师”团队。

---

### [](https://github.com/vitejs/vite-plugin-react/releases/tag/plugin-react%406.1.0)

**原文标题**: [Release plugin-react@6.1.0 · vitejs/vite-plugin-react · GitHub](https://github.com/vitejs/vite-plugin-react/releases/tag/plugin-react%406.1.0)

插件 @vitejs/plugin-react 发布 6.1.0 版本，新增实验性的原生 React Compiler 支持，可通过安装 oxc-transform-react 并启用 compiler 选项来使用。

- 🚀 发布 plugin-react@6.1.0，带来实验性原生 React Compiler 支持
- 📦 需先安装依赖：`npm install -D oxc-transform-react`
- ⚙️ 在 Vite 配置中启用 `compiler: true` 选项即可激活
- 🧪 该功能仍处于实验阶段，适合提前尝鲜
- 🎉 社区反响热烈，获得 33 个 🎉、5 个 ❤️ 和 2 个 🚀 反应，共 35 人参与互动

---

### [Bun 1.4 |](https://bun.com/blog/bun-v1.4)

**原文标题**: [Bun 1.4 | Bun Blog](https://bun.com/blog/bun-v1.4)

Bun 1.4 是一个重大更新，聚焦于 Node.js 兼容性、性能优化、内置标准库扩展，并完成由 Zig 到 Rust 的重写；同时改进了包管理器、测试/构建工具链和安全性，大幅降低内存与 CPU 占用，并扩展了多平台支持。

- 🚀 Node.js 兼容性大幅提升：新增 +1,517 个 Node 官方测试，`node:http`/`fs`/`cluster` 等模块通过率超过 97%，`node:sqlite`、`node:trace_events` 达 100%，Playwright、Next.js 16、vitest、OpenTelemetry、dd-trace 等生态工具已可运行。
- ⚡ 性能与资源优化：闲置 CPU 使用率降低 5 倍，内存最高减少 48%（HTTP 服务场景），Linux/Windows 启动速度提升 2–2.5 倍，二进制体积缩小至多 17%。
- 🔧 核心架构重写：Bun 代码库从 Zig 迁移到 Rust，首个正式发布版本，Claude Code 与 Prisma Compute 已提前采用。
- 🖼️ 新增内置图像处理 `Bun.Image`：支持 JPEG/PNG/WebP/GIF/BMP 的解码、缩放、旋转与编码，API 类似 sharp，比 sharp 快约 1.38 倍，无需原生插件。
- 🌐 内置无头浏览器自动化 `Bun.WebView`：可导航、点击、执行 JS 与截图，基于系统 WebKit 或已安装 Chrome/Edge。
- 📝 内置 Markdown 解析 `Bun.markdown`：支持 HTML、React 元素和终端渲染，兼容 GFM；`bun ./README.md` 可直接在终端美化展示 Markdown。
- ⏰ 系统级定时任务 `Bun.cron()`：在 Linux/macOS/Windows 注册 OS 级 cron 作业，也支持进程内定时器，任务不会重叠。
- ⌨️ 内置伪终端 `Bun.Terminal`：无需 node-pty 即可驱动 bash/vim/htop，并支持 Windows。
- 📦 大量内置模块替代第三方依赖：包含 `Bun.JSON5`、`Bun.XML`、`Bun.TOML`、`Bun.Archive`、`CompressionStream`、`URLPattern`、`Bun.stringWidth`、`Bun.sliceAnsi` 等，实现零安装、零依赖。
- 🧰 包管理命令增强：新增 `bun audit fix`、`bun dedupe`、`bun prune`、`bun pm diff`/`licenses`；`bun install` 速度比 npm/pnpm/yarn 快 15–33 倍，并支持全局虚拟存储与流式解压。
- 🧪 测试运行器并行化：`bun test --parallel`、`--isolate`、`--shard`、`--timings`、`--changed`、`--retry` 及 `jest.useFakeTimers()` 支持，显著提升大型测试套件效率。
- 🏗️ 构建能力升级：内置 React Compiler（比 Babel 插件快约 20 倍）、barrel import 优化、标准 TC39 装饰器、`--compile --asset` 嵌入资源、bytecode ES modules 支持及更快代码分割。
- 📊 可观测性工具：`--cpu-prof`/`--heap-prof`/`--metafile-md` 可生成 Chrome DevTools 可读的 Markdown 报告；支持 Datadog 持续剖析与异步堆栈追踪。
- 🔒 安全强化：大量 TLS 证书校验默认收紧，`checkServerIdentity` 在发送请求前执行；tarball 解压、HTTP 解析、Redis TLS 主机名校验均有加固。
- 🖥️ 平台扩展：新增原生 FreeBSD x86_64/aarch64 构建、Windows ARM64 原生支持、实验性 Android 构建，Linux glibc 最低版本降至 2.17，并支持 Win AppContainer。
- ⏩ 流与网络增强：原生 `ReadableStream`/`WritableStream`/`TransformStream`，HTTP/3 服务端与 fetch 客户端（实验），多媒体 Range/条件请求、文件目录静态服务、fetch 请求压缩等新特性。
- ⚠️ 升级注意事项：报告 Node.js 26（`NODE_MODULE_VERSION=147`），移除 `writeHeader`，x64 仅保留 baseline 构建，`Temporal` 默认启用，部分 JSX/TS 配置语义变更，需测试兼容性。

---

### [](https://formisch.dev/blog/formisch-v1/)

**原文标题**: [Formisch v1 is here | Formisch](https://formisch.dev/blog/formisch-v1/)

Formisch v1 已正式发布，这是一个基于 schema 的框架无关表单库，现已在生产环境中稳定可用，并带来多项新增功能和迁移支持。

- 🎉 Formisch v1 正式发布，采用语义化版本控制，破坏性变更仅随主版本更新。
- 🧩 框架无关，支持八种框架，schema 与表单逻辑可跨框架复用，无需应用级配置。
- 📦 新增 Angular 与 React Native 支持，后者为首个无 DOM 环境，核心逻辑独立于 DOM 运行。
- 🧭 六个框架共提供 15 份迁移指南，全面覆盖 TanStack Form，另有 Formik、React Hook Form、VeeValidate 等迁移路径。
- 🤖 文档支持以 Markdown 页面和 MCP 服务器提供，方便 AI 代理直接读取当前文档。
- 🗺️ 后续计划包括元框架支持、通过 Standard Schema 支持更多 schema 库（如 Zod）。
- 🚀 可通过在线 playground 快速体验，或使用 npm 安装对应包与 Valibot 开始使用。
- 🙏 感谢所有 RC 测试者、贡献者与赞助商，欢迎通过 GitHub 和 Discord 反馈。

---

### [](https://github.com/TanStack/query/releases/tag/release-2026-08-22-1856)

**原文标题**: [Release Release 2026-08-22 18:56 · TanStack/query · GitHub](https://github.com/TanStack/query/releases/tag/release-2026-08-22-1856)

TanStack Query 发布了 2026-08-22 版本，主要更新 query-core 以及 React、Vue、Solid、Preact、Lit 等生态包，带来新查询方法、大量修复与性能优化，并完成多项工程化调整。
- ✨ 新功能：query-core 新增简化的查询方法，方便开发调用。
- 🐛 query-core 修复：优化 MutateFunction 类型、falsy combine 结果缓存、select 错误清理、retryer 释放、resetQueries 状态保持、程序化设置数据时的 suspense 处理等。
- 🐛 框架适配修复：React Query 保持未订阅 useQueries 空闲、改进 infinite query 类型并移除 placeholderData；Preact Query 支持函数式 throwOnError 重试；Vue Query 保留泛型推断；Solid Query 在 memos 外解析 client。
- 🐛 其他修复：broadcast-client 可恢复跨标签页消息错误并处理 postMessage 拒绝；lit-query 增加 DataTag 并迁移构建；eslint-plugin-query 修正原型属性误报。
- ⚡ 性能优化：跳过无操作水合回调、跳过未使用的查询结果跟踪、减少 observer 移除开销、去重跟踪属性。
- 🧹 工程化与维护：tsup 迁移至 tsdown、TypeScript 升级到 7 且最低版本调整为 5.6、贡献指南新增 AI 指南、文档链接检查支持 Windows。
- 📦 包版本更新：核心及多个框架包升至 5.102.0，Svelte 相关包保持 6.1.39。
- 👥 贡献：共 25 位贡献者参与，包括 chatman-media、TkDodo 等。

---

### [](https://github.com/remorses/gpuix)

**原文标题**: [GitHub - remorses/gpuix: Node.js & React bindings for Zed’s GPUI. Build memory efficient native apps with React and no Electron · GitHub](https://github.com/remorses/gpuix)

GPUIX 是 Zed 的 GPU 加速 UI 框架 GPUI 的 React/TypeScript 绑定。它让你用 React 组件直接渲染到 Metal、DirectX、Vulkan 等 GPU 后端，构建原生高性能桌面应用，不需要 Electron 或 WebView；同一个应用还能通过 WebGPU/Wasm 在浏览器中运行。

- 🚀 快速开始：使用 `bunx @gpuix/cli new my-app` 创建官方示例，或 `bun add @gpuix/react react` 从零搭建；入口用 `render(<App/>)` 即可创建窗口并启动 GPU 帧循环。
- ⚛️ 核心架构：React reconciler 将每次提交聚合成原子的 mutation 批（`applyBatch`），Rust 侧用 `RetainedTree` 保存元素，每帧构建临时 GPUI 元素树完成布局与绘制。
- 🧩 内置元素丰富：包括 `div`、`text`、`input`、`textarea`、`virtual-list`、`code`、`diff`、`markdown`、`img`、`svg`、`anchored` 等。
- 🎨 样式接近 CSS：支持 flex/grid、圆角、阴影、渐变、`hover`/`active` 等；但 `<text>` 不会继承父级颜色，必须显式设置 `color`，否则在深色背景下看不见。
- 🖱️ 事件体系完整：包含点击、鼠标移动/进出、滚轮、键盘、focus/blur，以及 `<input>`/`<textarea>` 的 change/submit；键盘焦点基于 GPUI 原生 FocusHandle。
- 📜 原生滚动与虚拟列表：`overflow:"scroll"` 即可获得原生滚动；`<virtual-list>` 只构建可视区域的行，支持 `alignment`、`followTail`、`itemCount` 窗口切片和编程式滚动。
- 📝 文本与富文本：原生输入支持 IME、选区、剪贴板、撤销；`<code>`、`<diff>`、`<markdown>` 在 Rust 侧用 Syntect 高亮，文字默认可跨元素选择和复制。
- 🔍 搜索与高亮：通过 `highlight` 属性和 `useTextSearch` hook 实现查找条；虚拟列表中要自行用 `findRanges` 计算总匹配数和偏移，避免定位到错误行。
- 🧩 无头 UI 原语：`@gpuix/react/select`、`combobox`、`tooltip` 提供无样式复合组件，可像 shadcn 那样在本地封装成自己的 UI 组件。
- 🪟 窗口控制灵活：支持透明/模糊背景、隐藏标题栏、红绿灯坐标、`focus:false`/`show:false` 后台启动；macOS 上自动安装包含 ⌘Q、⌘H 等标准快捷键的应用菜单栏。
- 🤖 自动化测试能力强：提供类 Playwright 的 locator API（`getByTestId`、`getByText` 等），基于真实 GPU 测试渲染器，可模拟点击、输入、滚轮、拖拽，并支持冻结时钟做确定性截图。
- 🖥️ 跨平台与打包：桌面端通过 napi-rs（macOS Metal / Windows DirectX / Linux Vulkan）；浏览器端是 wasm-bindgen + WebGPU。`bun build --compile` 可打成分发用的单文件原生二进制。
- 📌 项目状态：开源 Apache-2.0，核心功能已大面积可用；尚未完成/规划中的包括 Canvas 元素、多窗口、真正的 React Refresh 热更新等。原生 `.node` 修改需重新构建，约 4 秒可完成“编译到截图”循环。

---

### [](https://github.com/vercel/satori/releases)

**原文标题**: [Releases · vercel/satori · GitHub](https://github.com/vercel/satori/releases)

这是 Vercel 的 `satori` 仓库在 GitHub Releases 页面上的发布记录，显示范围从 0.29.0 到最新版 0.33.4，发布于 2026 年 7 月至 8 月。内容涵盖多项新功能与修复，包括 WebP 图片、HarfBuzz 文本整形、CSS 新特性支持，以及缓存、性能和 SSRF 安全加固。

- 🖥️ **0.33.4**：修复 Playground 卡片使用 Geist 字体的问题 (#790)
- 🎨 **0.33.3**：优化 opacity（不透明度）处理 (#789)
- 🗃️ **0.33.2**：改进字体缓存机制 (#788)
- ⚡ **0.33.1**：改进缓存并更新基准测试（性能提升约 12%）(#787)
- ✍️ **0.33.0**：新增 HarfBuzz 文本整形支持 (#735)
- 🌫️ **0.32.0**：新增 `backdrop-filter` 支持 (#786)
- 📐 **0.31.0**：新增 `clip-path` 中的 `shape()` 支持 (#785)
- 🔶 **0.30.0**：新增 `corner-shape` 支持 (#784)
- 🔒 **0.29.1**：加固 SSRF 防护，覆盖尾点、重定向和 DNS (#777)
- 🖼️ **0.29.0**：新增 WebP 图片支持 (#622，关闭相关 issue)


---

### [](https://react-aria.adobe.com/releases/v1-21-0)

**原文标题**: [v1.21.0 | React Aria](https://react-aria.adobe.com/releases/v1-21-0)

overview summary
该版本为 v1.21.0，主要新增 NavigationTree 组件，并对 Menu 与 TokenField 进行显著升级，同时包含大量跨组件的修复与更新，并发布多个相关包的新版本。

- 🎉 新增 NavigationTree 组件：展示层级化链接，适用于侧边栏与复杂应用导航，支持键盘导航与嵌套路由。
- 📂 Menu 菜单大升级：新增异步加载与空状态支持，可配合 MenuLoadMoreItem 从 API 分页加载，并用 renderEmptyState 显示加载或空数据提示。
- 🔄 TokenField 选区 API 变革：TokenFieldValue 以 selectedRange 取代 caretPosition，记录完整选区范围，并可通过 withSelectedRange 更新与恢复撤销/重做后的选择。
- 🌐 常规通用改进：重新导出 react-aria-components 相关类型，新增 setInteractionModality 导出，并优化 Safari 焦点环、locale 插件过滤及 usePreventScroll 等行为。
- 📅 日历与日期修复：支持在 isDateUnavailable 下选择可见范围外的日期；修复埃塞俄比亚与科普特历法在新年日期的年份估算问题。
- 🧩 多个组件修复：Checkbox/Switch/RadioGroup 的 inputRef 支持回调引用，Dialog 可在 Tabs 或 Select/Combobox 中正常工作，Table 拖放更可靠，Tabs 修复 RTL 垂直方向箭头键行为等。
- 🍽️ Menu 额外增强：新增异步加载、空状态与 typeahead 示例支持。
- 📦 发布包更新：涉及 @internationalized/*、react-aria、react-stately、react-aria-components 等，其中 react-aria-components 升至 1.21.0。

---

### [](https://astryx.atmeta.com/blog/astryx-v0-5-0)

**原文标题**: [Astryx v0.5.0: 30 locales, one Escape key, and bottom sheets in core · Astryx](https://astryx.atmeta.com/blog/astryx-v0-5-0)

overview summary
Astryx v0.5.0 是一次重要版本发布，汇集了 0.4.0 以来的八个版本更新，包含两个破坏性变更、三个组件晋升、多语言支持、无障碍改进及 CLI 增强，旨在提升组件库的可访问性、国际化与开发体验。

- 🚀 核心发布：`@astryxdesign/core` 升级至 0.5.0，所有稳定版包需同步更新；`lab`、`charts`、`richtext`、`vega` 等 canary 包独立版本管理。
- ⚠️ Banner 破坏性变更：移除 `defaultIsExpanded`，改用 `collapsible` 布尔值或配置对象（支持 `isOpen` 受控模式），并提供 codemod 自动迁移。
- ⌨️ 统一 Escape 键关闭机制：所有浮层共享单一关闭堆栈，每次按键只关闭最顶层，支持 React 树嵌套与 portal；同时移除旧 UMD bundle 及三个废弃页面模板。
- 📦 三个组件晋升：`BottomSheet` 与 `BottomSheetSwitcher` 进入 core，`Stepper` 与 `Step` 进入 core，`RichTextEditor` 系列移至独立 `@astryxdesign/richtext` 包。
- 🌍 新增 30 个语言环境目录：日期组件与国际化 Provider 联动，Calendar 使用 CLDR 名称，CJK 输入法下的键盘事件处理更安全，新增 `useLocale` 与 `useCollator` 工具。
- 🎨 主题继承增强：`extends` 会解析基础主题到子主题输出，非法继承直接报错；焦点环改为 CSS token 驱动，支持深浅色配色元组。
- ♿ 无障碍改进：TabList 遵循 WAI-ARIA tabs 模式，ButtonGroup 单 tab 焦点移动，Breadcrumbs 当前项增加字重区分，触摸目标满足 WCAG 2.5.8 最小 24×24 要求。
- 🧱 组件与 API 增强：FormLayout 支持 `defaultOptionality`，DateRangeInput 新增范围限制，DateTimeInput 增加时间选项间隔，MultiSelector 自定义格式化，AspectRatio 可在断点覆盖 ratio 等。
- 🛡️ Markdown 安全修复：拒绝 `javascript:`、`vbscript:` 和 `data:text/html` URL；增量解析大幅减少流式内容重建块数量。
- 🛠️ CLI 工具升级：`astryx theme targets` 支持 JSON 输出，`theme template`/`build` 更灵活，`template --cdn` 生成无构建页面，新增五个仪表盘模板及文档搜索集成。
- 🙏 致谢社区：特别感谢提交者贡献与 Markdown 安全漏洞修复；完整变更记录见 v0.5.0 release 页面。

---

### [Waku 1.0 (RC)— Waku](https://waku.gg/blog/waku-v1-rc)

**原文标题**: [Waku 1.0 (RC) — Waku](https://waku.gg/blog/waku-v1-rc)

Waku 1.0 RC 已发布。这是一个围绕 React Server Components 设计的最小化 React 框架，此次 RC 确定了公开 API，并明确标记不稳定 API；同时新增了类型安全导航和即时导航能力，另有若干修复与破坏性变更。这是 v1 最终版前的最后一次反馈窗口。

- 🚀 Waku 1.0 候选版（RC）正式发布，公共 API 已冻结，不稳定 API 被显式标记；这是 v1 最终版前最后一次收集反馈的机会。
- 🧭 导航全面支持类型安全：目标路由模式可自动补全，params 类型随模式推导，重命名路径或漏写 slug 会直接变成编译错误；replace、prefetch、unstable_redirect 同样适用，search params 通过 codec 按路由定义类型，原有字符串 API 仍可用。
- ⚡ 即时导航：Waku 会缓存已访问路由的静态外壳，<Link> 可在点击前预取；启用实验性 unstable_instant 后，外壳命中缓存可立即渲染（含 Suspense fallback），再流式注入动态内容。
- 🔧 其他改进包括：修复重定向、404、hash 目标及版本偏差问题；请求处理更严格（来源检查防 CSRF、更严格的 server action 验证、可配置请求体上限）；unstable_redirect 支持外部网站 http/https URL。
- ⚠️ 破坏性变更：请求上下文改为只存在于请求中，并移入 router；移除了 waku/server 的 unstable_getContext()/unstable_getContextData()，改用 waku/router/server 的 unstable_getRequest()、unstable_getHeaders()、unstable_setNonce()，上下文数据需自行配合 AsyncLocalStorage。
- 🛠️ Middleware 不再能读写 Waku 上下文；需要在渲染作用域内运行代码（如注入每请求数据或设置 CSP nonce）时，应使用 createInterceptor 注册拦截器；middleware 仍可处理响应头和自身存储。
- 💬 欢迎通过 GitHub Discussions 或 Discord 提交反馈，帮助 v1 最终版尽快落地；也可以到 GitHub 上给项目点个星。

---

### [发布 TanStack Charts v0.16.0 · TanStack/charts · GitHub](https://github.com/TanStack/charts/releases/tag/v0.16.0)

**原文标题**: [Release TanStack Charts v0.16.0 · TanStack/charts · GitHub](https://github.com/TanStack/charts/releases/tag/v0.16.0)

TanStack Charts v0.16.0 是迁往官方 Alpha 的重要版本，包含破坏性 API 变更、类型校验增强及多项行为修复，各框架适配包同步更新依赖。

- 🚀 正式进入官方 Alpha 常规 0.x 发布线，发布 v0.16.0。
- 📐 图表定义现在必须配置笛卡尔 `scales.x` / `scales.y`，极坐标则需 `scales.angle` / `scales.radius`。
- 🧹 移除了 pre-Alpha 临时根属性、运行时适配器和相关开发警告。
- 🔄 自定义标记需用 `ChartMarkPointX` / `ChartMarkPointY` 替换旧的 `ChartMarkX` / `ChartMarkY`，并从 `@tanstack/charts/mark/scale-values` 导入。
- 🗺️ 极坐标布局回调改为从 `layout.scales` 读取保留映射。
- 🧩 保留 scale 条目会在类型边界精确校验：已物化维度必须配置 scale，未使用维度需显式设为 `null`。
- ✅ 运行时校验仍会检查必需的保留条目和实际物化的通道。
- 🛡️ 内置标记选项字面量会拒绝不支持的属性，同时保留类型化通道、命名 scale ID 与泛型标记包装器。
- 📉 修复发散堆叠中精准为零的单元格造成的假尖峰，使其保持原有正/负基线。
- 📌 固定工具提示现在会在图表/工具提示外按下指针时关闭，便于焦点离开后恢复指针检查。
- 🔗 各框架适配包（React、React Native、Octane、Preact、Vue、Solid、Svelte、Angular、Lit、Alpine）均同步依赖 `@tanstack/charts@0.16.0`。

---

### [更新日志 | nuqs](https://nuqs.dev/docs/changelog#v2.10.0)

**原文标题**: [Changelog | nuqs](https://nuqs.dev/docs/changelog#v2.10.0)

这是 nuqs 库从 v2.10.1 到 v1.17.3 的更新日志摘要，涵盖框架适配、新功能、Bug 修复、文档优化与工程化改进。

- 🔧 v2.10.x：修复测试适配器的 URL 更新队列、挂载渲染与导航后状态恢复问题，并优化文档键盘快捷键与无障碍体验
- ✨ v2.10.0：React 适配器新增 serverSearch，用于通过 SSR 填充搜索参数；修复 debounce 回调时机与 popstate 队列重置
- ⚛️ v2.9.x：正式支持 react-router v8，并在适配器默认选项中引入 history；修复 TanStack Router 跨页转场、Next.js 缓存组件陈旧值及 Activity 状态失效等问题
- 🛠 v2.8.x：新增 react-router v5 支持；修复 React Router 同步、Next.js App Router 队列重置，并为 Next.js 16 cacheComponents 增加 CI 测试
- 🧩 v2.7.x：引入 multi-parsers（多解析器）与测试适配器的 memory 选项；修复乐观状态闪烁；文档站点迁移至 nuqs.dev
- 🔄 v2.6.0：新增 processUrlSearchParams 中间件，并支持在 createSerializer 中使用该中间件来处理 URL 查询参数
- 🚀 v2.5.0：重要功能版——新增 key isolation、debounce 防抖、TanStack Router 支持、Standard Schema 接口与适配器级默认选项，并显著缩减包体积
- 📄 v2.4.x：新增 parseAsPageIndex 解析器和测试辅助工具；支持 shallow: false 的全页导航以及 scroll 选项
- 🏷 v2.3.x：加入 react-router v7 支持、shallow routing、loader 功能与 UrlKeys 类型辅助，并改进与 React Router 的兼容性
- 🧪 v2.2.x：新增测试 HOC，支持动态默认值，并将 React 19 加入 peer 依赖范围；修复多条序列化相关问题
- 🌐 v2.0.0：重大架构重构——从仅 Next.js 扩展为通用 React 框架库，引入适配器体系（Next.js、Remix、React Router、One 等），并改为 ESM-only
- 🐛 v1.x：早期版本持续修复，包括允许 null 清除参数、序列化器默认值处理、localStorage 检测、URL 特殊字符编码等
- 📚 文档与社区：新增 changelog 独立页面、shadcn registry、赞助商展示、用户排行榜及 LLM 可读功能（如 copy as markdown、llms.txt）
- 🔐 工程与安全：持续升级依赖并修复安全漏洞，适配 React 19/Next.js 16，支持 TypeScript 7，并新增 bundle 体积对比与更严格的 CI/CD 工作流

---

### [](https://github.com/fuma-nama/fumapress/releases/tag/fumapress%401.0.0)

**原文标题**: [Release fumapress@1.0.0 · fuma-nama/fumapress · GitHub](https://github.com/fuma-nama/fumapress/releases/tag/fumapress%401.0.0)

Fumapress 1.0.0 是一次重大重构版本，核心 API 重新设计，带来独立 CLI、自动图像优化、Glass 布局支持与推荐插件预设，并新增 GraphQL、Obsidian、Notion 等集成。

- 🚀 核心 API 重构：布局配置移入 config（renderPage/renderRoot/renderNotFound/defaultLayoutProps），loader 改为 content，插件类型更名为 PressPlugin、AppShape
- 🔧 修复 aiPlugin 导出：从类型导出改为值导出，运行时 `import { aiPlugin }` 不再失败
- 💬 Glass 布局 AI 支持：aiPlugin 接入 Glass 原生 aiChat，Ask AI 触发入口从浮动按钮移到 header/sidebar
- 🖼️ 自动图像优化：按部署平台自动匹配 Vercel/Cloudflare/Node.js Sharp；条件不足时回退普通 `<img>`，显式配置优先
- 🛠️ 独立 CLI：提供 fumapress dev/build/start 命令，Waku.js 变为普通依赖，新项目无需再安装 waku/react-server-dom-webpack
- ⚙️ 迁移变化：移除 waku 依赖、把 waku.config.ts 改为 vite.config.ts，并将相关配置移到 press() 插件选项中
- 🧹 自动去重框架包：press() Vite 插件自动检测并 dedupe，避免重复 React context，无需手动配置 resolve.dedupe
- 🤖 新增 robots.txt 插件与 RSS 插件，可分别自动生成 robots.txt 和 RSS feed
- ⭐ “recommended”插件预设默认启用：自动加入 llms.txt、robots.txt、rss、search
- 🐙 仓库支持扩展：site.git 支持 github/gitlab/bitbucket provider，GitHub URL API 更名 getFileUrl()
- 👾 升级到 Waku beta 8，内置搜索迁移至 ZBSearch，移除 @orama/orama，并改用 fumadocsMdx() 注册 MDX 插件
- 📐 新增 Glass 布局 wrapper（fumapress/layouts/glass），需要 Fumadocs UI v16.12+，并导入 glass.css
- 📊 linkValidationPlugin 新增 report 选项：可输出 dist/fumapress-diagnostics.json，让 CI 注释死链而非直接失败
- 🔗 修复博客标签页链接：现在能正确解析自定义 paths.tags 和当前 locale，避免 404
- 📦 新增 GraphQL、Obsidian、Notion 集成，分别支持 schema 文档、Obsidian vault 渲染和 Notion 页面渲染
- 🟢 未指定 base URL 时不再报错

---

### [](https://github.com/TrySound/rifm/releases/tag/v1.0.0)

**原文标题**: [Release v1.0.0 · TrySound/rifm · GitHub](https://github.com/TrySound/rifm/releases/tag/v1.0.0)

RIFM 1.0 是一次全面现代化发布：从 Flow/JavaScript 迁移到 TypeScript，重构构建、测试与 CI 基础设施，新增 React 19 支持，并带来面向未来的 ESM-only 破坏性变更。

- 🔄 从 Flow/JavaScript 迁移到 TypeScript，并生成 TypeScript 声明文件
- 📦 用 tsdown 替代 Rollup 负责打包
- 🧪 用 Vitest 替代 Jest，并通过 Playwright 增加真实浏览器测试覆盖
- ⚛️ 新增 React 19 支持，同时保留 `react >=16.8` 的 peer 依赖
- 🚀 开发与 CI 从 Yarn/Travis 迁移到 pnpm/GitHub Actions
- 🔏 通过 npm provenance 实现可信发布（trusted publishing）
- 🌐 用更快、可访问的 Vite 网站替换旧版 Next.js demo
- 📖 重写 README，补充更清晰的 API 与 caret 行为文档
- ⚠️ 破坏性变更：包现在仅支持 ESM，目标为 ES2022；不支持 `require("rifm")`；移除 Flow 声明与打包源码；exports 仅保留公开的 `rifm` 入口

---

### [版本发布 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases#release-v7.86.0)

**原文标题**: [Releases · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases#release-v7.86.0)

这是 react-hook-form 在 GitHub 上的 Releases 页面记录，涵盖 v7.79.0 至 v7.87.0 的多个 v7 正式版，以及一个 v8.0.0-beta.3 预发布版。整体更新集中在表单 API 增强、TypeScript 类型改进、大量边界问题修复，以及性能和包体优化。

- ✨ 新增 / 增强 API：`trigger()` 支持 `shouldTouch`，`setValue()` 新增 `delayError` 与 `shrink`，新增类型安全的 `getErrors()`，并通过 `formContext` 暴露 `resetDefaultValues()`。
- 🧩 FieldArray 与表单结构：新增 `FieldArray` 组件；`useFieldArray` 支持 `disabled`；修复 append/prepend/insert/remove 时根错误丢失、dirtyFields 不稳定和错误位置变化等问题。
- 🧬 TypeScript 优化：新增 `OpaqueTypes` 注册表，可将 Dayjs、Decimal 等第三方类型声明为不透明叶子类型，避免深层递归导致的“Excessive complexity”；递归类型深度设 10 层上限；改进 FormState、getFieldState 等类型定义。
- ⚛️ React 兼容性与原生行为：支持 React `<Activity />`；增强 `<Form />` 提交行为；修复 Activity 子树首次隐藏时 `useWatch`/`useFormState` 不同步、Controller 在 null 父节点下提交 undefined、onChange promise、StrictMode/快速刷新等问题。
- 🐞 Bug 修复覆盖状态与输入：修复 `resetField` 不重算 isValid、`unregister` 的 keepDirty 行为、`values` + `keepDirtyValues` 破坏数组/冻结对象、`useWatch` 在 name 变为 null 时的旧值、`clearErrors` 内部状态，以及 File/Blob/checkbox/radio 等输入处理问题。
- ⚡ 性能与体积：优化 `getDirtyFields`、`createFormControl`、`cloneObject`、`unregister` 和 onChange 高负载场景；移除死代码，降低包体积。
- 🔄 v8.0.0-beta.3：同步 master 分支，纳入近期 v7 的 bug 修复、性能改进与开发体验更新。
- 🤝 社区致谢：多个版本感谢 candymask0712、EduardF1、wanxiankai、zigzagdev、JSap0914、bluebill1049 等贡献者的参与。

---

### [](https://share.transistor.fm/s/f48613c6)

**原文标题**: [This Month in React | TMiR 2026-08: Release candidate season; is that an asteroid hitting web educators?](https://share.transistor.fm/s/f48613c6)

该内容展示了一个播客节目的分发与互动界面，提供订阅、分享、下载及多平台收听选项，并包含额外内容如预告片、花絮和完整文字稿。

- 🎧 提供“预告片”和“彩蛋”等附加音频内容
- 🔔 支持一键订阅，并显示订阅人数（10）
- 📤 可分享节目，并支持复制链接
- ⬇️ 提供下载功能，便于离线收听
- 📺 列出多种收听平台：Apple Podcasts、Spotify、YouTube、Amazon Music、Pandora 等二十余个
- 📄 包含完整文字稿（Full Transcript）与章节（Chapters）功能
- 🔗 提供嵌入（Embed）代码及更多节目信息入口

---

### [](https://wallabyjs.com/?referrer=ThisWeekInReactSep26)

**原文标题**: [Wallaby - AI-Ready Test Runner with Instant Feedback in Your Editor](https://wallabyjs.com/?referrer=ThisWeekInReactSep26)

Wallaby.js 是一款面向 JavaScript/TypeScript 开发者的测试运行工具，能在编辑器中即时反馈测试结果，通过实时调试、AI 集成与精准执行机制大幅提升开发效率，获得大量用户好评。

- ⚡ 即时测试反馈：输入代码时自动运行测试，实时将结果与覆盖率显示在代码旁，无需等待保存。
- 🎯 精准执行机制：仅重新运行受代码变更影响的最小测试集，甚至只跑单个测试，反馈速度极快。
- 🕰️ 时间旅行调试器：可在代码执行中前后步进，查看运行时值并快速定位缺陷成因。
- 📋 内联错误与覆盖率：错误信息、单行覆盖率及未覆盖区域直接显示在编辑器行号旁，方便快速定位。
- 🔬 深度检视工具：支持树状展开复杂对象、交互式查看运行时值，并提供 diff 与快照管理。
- 🧪 选择性测试运行：可只运行当前打开或正在编辑的测试文件，也支持单测试聚焦执行。
- ♻️ 无锁定限制：作为现有测试框架与 IDE 的插件，不强制绑定 API、框架或供应商。
- 🤖 AI 原生支持：通过 Skill 与 MCP 服务器向 AI 工具提供实际运行值、执行路径与依赖关系，辅助代码修复和生成。
- 📈 性能分析与洞察：提供测试 CPU 分析器与项目级测试/覆盖率总览，支持排序和过滤。
- 💰 效率提升显著：官方估算仅基本功能即可带来约 10.84% 的效率增益，每年节省约 2396 美元。
- 🧑‍💻 开发者口碑极佳：众多用户称赞其让 TDD 更轻松有趣，是 JS/TS 生态中“必备”的效率神器。

---

### [](https://wallabyjs.com/whatsnew/cli.html?referrer=ThisWeekInReactSep26)

**原文标题**: [Test Runner CLI for Coding Agents](https://wallabyjs.com/whatsnew/cli.html?referrer=ThisWeekInReactSep26)

Wallaby CLI 将运行时测试智能引入 AI 编码代理工作流，使编码代理无需编辑器或 MCP 服务器即可直接通过命令行运行测试，并获得精准的结果、覆盖率与运行时数据，从而显著提升效率并减少 token 消耗。文章还介绍了简单的启用方式、工作方式以及未来路线。

- 🤖 支持 Claude Code、Codex CLI、Copilot CLI、OpenCode、Pi 等 AI 编码代理，直接在命令行获得测试结果与运行时数据。
- 📁 特别适合 git worktrees 等无头工作流，无需编辑器会话或 MCP 服务器即可执行测试。
- 🧪 兼容 Vitest、Jest 等测试框架，为代理提供结构化信息：该跑哪些测试、失败原因、覆盖范围和运行时值。
- ⚡ 替代整组套件重复运行和原始输出解析，大幅减少 token 消耗，并显著加快反馈循环。
- 🛠️ 启用方式简单：执行 `npx skills add https://github.com/wallabyjs/skills --skill wallaby-cli` 即可。
- 🔄 Wallaby 只在代理需要时启动、退出时自动停止，并能复用编辑器已启动的实例，最大限度降低启动开销。
- ✅ 代理能利用准确的测试/覆盖率数据校验生成代码、改善测试质量并提高覆盖率；还可在不修改源文件的前提下调试失败测试，减少不必要改动。
- 🔮 这是早期版本，后续将改进隔离/沙盒/CI 环境支持，连接编辑器扩展，通过 evals 提升 token 效率，并暴露更多运行时数据。

---

### [](https://github.com/react-native-community/discussions-and-proposals/pull/1018)

**原文标题**: [RFC: Reducing React Native’s C/C++ Public API by coado · Pull Request #1018 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1018)

overview summary
该内容为 GitHub 上一个关于缩减 React Native C/C++ 公共 API 的 RFC 拉取请求，提出对组件可见性进行重新分层、移动与限制。

- 📝 提交了“缩减 React Native 的 C/C++ 公共 API”RFC 草案（PR #1018）
- 🔀 拉取请求包含 14 个提交，逐步调整各模块的可见性等级
- 📦 将 `jserrorhandler`、`react/runtime` 等组件移入框架层级
- 🔓 将 `attributedstring`、`renderer/debug`、`react/utils` 调整为 public 可见性
- 📉 将 `imagemanager` 降级为 public（限制访问范围）
- 🗂️ 移动 `uimanager` 与 `animationbackend` 到更合适的层级
- 🧩 重新划分多个公共组件层级，并调整 `react/renderer/bridging`
- ⏳ 目前 PR 处于打开状态，尚无正式 Reviewers 或 Assignees
- 💬 早期收到来自社区的火箭与眼睛表情反馈，代表一定关注度

---

### [](https://crisp.chat/en/?utm_source=twir&utm_medium=newsletter&utm_campaign=crisp_q3_nl&utm_content=2sep26)

**原文标题**: [The AI Customer Support Platform for Every Business - Crisp](https://crisp.chat/en/?utm_source=twir&utm_medium=newsletter&utm_campaign=crisp_q3_nl&utm_content=2sep26)

Crisp 是一個專為客戶支援打造的 AI 優先全通路平台，整合 AI 助手 Hugo、共用收件匣、知識庫、CRM 與分析工具，協助企業自動化超過 50% 的客戶詢問，並透過無程式碼工作流程打造專屬 AI 客服體驗，幫助團隊更有效率地解決問題。

- 🤖 提供 AI 客服平台與 AI 助手 Hugo，能自動化大量客戶詢問，讓團隊專注於重要事務。
- 📥 整合共用收件匣，集中管理來自網站、Email、WhatsApp、Messenger 等 10 多個管道的對話。
- 🧠 內建 AI 功能，包括智慧回覆、自動摘要、寫作工具與支援副駕駛，降低客服工作量。
- 🔧 透過 4 步驟打造 AI Agent：訓練 AI、建立工作流程、測試部署、驗證與優化。
- 📚 提供知識庫與說明中心，讓客戶自行搜尋解答，提升自主服務能力。
- 🛠️ 支援無程式碼自動化流程，可建立內部工作流程或客戶導向的 AI 聊天機器人。
- 📊 具備客戶關係管理（CRM）與分析功能，協助追蹤客戶資料與團隊績效。
- 💬 聊天小工具可快速嵌入網站或應用程式，支援即時對話並引導轉換。
- 🎯 適合客戶支援、銷售與行銷團隊，透過 AI 工作流程自動化銷售與再行銷。
- ⭐ 已獲得超過 10,000 家公司信賴，並獲得客戶好評，強調其靈活性與自動化能力。
- 💡 提供 14 天免費試用、無需信用卡，並可預約產品示範。

---

### [](https://margelo.com/blog/margelo-joins-callstack)

**原文标题**: [Margelo Joins Callstack to Advance High-Performance React Native Engineering - Margelo](https://margelo.com/blog/margelo-joins-callstack)

Margelo 宣布加入 Callstack，交易估值超过 2000 万欧元，将自身高性能 React Native 技术与 Callstack 的企业级交付经验相结合，并继续维护开源项目。

- 💶 Margelo 以超过 2000 万欧元的估值正式加入 Callstack。
- ⚛️ 核心开源项目（如 Nitro Modules、VisionCamera、react-native-mmkv）将继续保持开源。
- 🤝 双方优势互补：Margelo 的性能优先工程 + Callstack 的企业级规模化交付经验。
- 🚀 面对 AI 加速开发，未来更聚焦架构、性能、原生集成、验证与发布安全等关键环节。
- 👤 Marc Rousavy 将继续领导现有开源库的开发，并参与整合后产品方向的制定。

---

### [未找到标题](https://expo.dev/blog/introducing-observe)

**原文标题**: [No title found](https://expo.dev/blog/introducing-observe)

您尚未提供需要总结的文本内容。请发送文章或段落，我会按以下模板为您生成中文要点总结：

overview summary  
- ✨ 概括性要点

---

### [](https://www.openiap.dev/docs/updates/announcements#2026-08-19-amazon-fireos-vega)

**原文标题**: [OpenIAP - Unified Specification for In-App Purchases](https://www.openiap.dev/docs/updates/announcements#2026-08-19-amazon-fireos-vega)

您尚未提供需要总结的文章内容。请发送文本，我将按照以下格式为您生成中文要点总结：

overview summary
- Emoji Bulletpoint

---

### [](https://github.com/react/react-native/pull/57723)

**原文标题**: [[ResizeObserver 3/3] ResizeObserver Web API implementation by paradowstack · Pull Request #57723 · react/react-native · GitHub](https://github.com/react/react-native/pull/57723)

该 PR 为 React Native 新架构实现了 ResizeObserver Web API，默认由 `enableResizeObserverByDefault` 特性开关关闭，旨在提升 Web 兼容性；实现涵盖 JS/C++ 层、测试与示例，经多轮评审修复后已合并至 main。

- 📌 系列定位：此 PR 是 3/3 的收尾实现，依赖前序 `feat/LayoutEventEmitter` 父级改动。
- 🎯 核心目标：为 React Native 新架构加入 `ResizeObserver` Web API，默认由 `enableResizeObserverByDefault` flag 控制（关闭）。
- 📏 相比 `onLayout` 更强：调用方可选择观察 `content-box`、`border-box` 或 `device-pixel-content-box`，并能拿到对应盒子的尺寸。
- 🧩 总体架构：JS 层 `ResizeObserver` / `ResizeObserverEntry` / `ResizeObserverSize` 建立在单例管理器与 `NativeResizeObserver` TurboModule 之上，采用 `notify` + `takeRecords` 拉取模型。
- ⚙️ C++ 层设计：`ResizeObserverManager` 在 `shadowTreeDidCommit` 时收集变更，并在事件循环的“update the rendering”步骤（`runResizeObservations`）内计算并投递观察结果。
- 🔒 运行前提：需要 bridgeless 与新版事件循环；旧版调度器仅挂载 no-op delegate。
- ⚠️ 规范偏差 1：RN 没有同步重布局循环，因此每个 tick 只做一次 gather/broadcast，不会触发“通知未投递”错误；回调中引发的尺寸变化在下一个 tick 投递。
- ⚠️ 规范偏差 2：对同一目标重复 observe 相同 box 是无操作，不会重新投递；该行为与浏览器一致，而非规范中的字面算法。
- ⚠️ 规范偏差 3：跨 observer 的回调顺序按首次 `observe()` 的顺序决定，而非构造顺序。
- 🧪 测试覆盖：Fantom `ResizeObserver-itest.js` 覆盖大量场景；RN-tester 展示 box size、文本、可见性等示例；`RuntimeSchedulerTest.cpp` 新增渲染循环相关测试。
- 📝 评审关注点 1：Flow 类型中的 `ResizeObserverEntry` 与 `ResizeObserverSize` 应声明为 class。
- 🔁 评审关注点 2：回调内部引发的更新需要进入规范中的 `resizeObserverDepth` 循环，避免只执行一次。
- 📐 评审关注点 3：`contentRect` 的 origin 需按规范处理，且应移除昂贵的 `computeRelativeLayoutMetrics` 调用，因为 ResizeObserver 只关心元素自身尺寸、不关心视口位置。
- 🔐 评审关注点 4：构造函数需沿用私有构造模式（如 `_public`），changelog 在转为正式通道前应保持 `[internal]`。
- ✅ 作者修复后：实现加入 gather / broadcast / depth 循环，补充更多 Fantom 与 RuntimeScheduler 测试，修正 Flow 类型、删除高开销调用，并同步 Package.swift 与快照。
- 🚀 最终状态：PR #57723 由 `meta-codesync` 在 `b03652a` 合并；标签包括 `CLA Signed`、`Merged`、`p: Callstack`、`Shared with Meta`。

---

### [](https://github.com/stephanww/rn-dev-security-guide)

**原文标题**: [GitHub - stephanww/rn-dev-security-guide: The React Native Developer's Security Guide: A field guide to supply-chain and toolchain security for React Native developers - securing your workstation, dependencies and CI. · GitHub](https://github.com/stephanww/rn-dev-security-guide)

overview summary
《React Native 开发者安全指南》是一本面向 macOS 上 React Native 开发者的实地安全手册。它的核心论点是：React Native 仓库本质上是一个“多语言执行环境”，一次 `git clone && yarn && pod install` 就会在多个运行时执行不可信代码；攻击者更倾向于攻击开发者本身，因为拿到开发者笔记本即可获得签名分发渠道。书中聚焦工作区、依赖、工具链和 CI，而不是最终用户的应用安全，并提供防御、检测、应急响应以及配套的 opengrep 规则集。

- 📘 面向 React Native 开发者、技术负责人和任何克隆过陌生仓库的人，假设读者没有安全背景。
- 🎯 安全范围聚焦开发者工作站、工具链、仓库与 CI，不讨论安全存储、证书固定、越狱检测等终端用户安全话题。
- 🧩 一个 RN 仓库会涉及 Node、Ruby、CocoaPods/Gradle、Xcode 等多个运行时，使攻击面复杂且隐蔽。
- 💻 攻击者一旦控制开发者的 Mac，就能获得源码、npm token、签名证书、密钥、浏览器会话甚至 AI agent 的执行权限。
- 🍎 Apple 侧覆盖 Ruby/CocoaPods/Xcode 构建阶段与签名材料威胁；🤖 Android 侧覆盖 Gradle、`gradle-wrapper.jar` 与 keystore。
- 🧠 还讨论了非依赖树威胁，如开发服务器端口暴露、AI agent 被滥用、伪装面试/ClickFix、CI 系统扩展攻击等。
- 🛡️ 防御部分提供安装加固、隔离最小权限、检测 grep 技巧、事件响应流程和团队强制策略。
- 📂 附录包含“文件风险图谱”“安全克隆手册”“macOS 三行应急命令”等可直接使用的参考内容。
- 📅 书中所有事实均注明日期并能追溯来源，内容截至 2026 年 8 月。
- 🔍 配套的 119 条 opengrep 规则按章节组织，可在仓库或 CI 中运行；示例代码刻意“结构真实但功能惰性”，不会直接变成可用攻击。

---

### [React Native Connection 大会](https://reactnativeconnection.io/?utm_source=thisweekinreact.com)

**原文标题**: [React Native Connection Conference](https://reactnativeconnection.io/?utm_source=thisweekinreact.com)

overview summary
- 📅 React Native Connection 是法国首个专为 React Native 开发者举办的会议，2026 年 9 月 24 日将在巴黎举行全天活动。
- 🎤 大会汇集多位知名演讲者，涵盖测试、键盘交互、Web 支持、导航、动画、App Intents、XR、桌面应用等话题。
- 🎫 门票分为早鸟（已售罄）、常规（289€+税）和免费社区票（9 月 17 日前申请），所有门票含完整会议、餐饮与社交活动。
- 🍽️ 活动日程从上午 9 点欢迎仪式持续至晚上 10 点酒吧交流，包含多场演讲、咖啡/午餐休息及闭幕拍照环节。
- 🏅 赞助商包括 Gold 级 Doctolib，Silver 级 ReactVision、RevenueCat、The Mobile-First Company、Codemagic，以及媒体合作伙伴。
- 🧑‍💼 组织团队由多位资深 React Native 专家组成，致力于社区建设与技术分享。
- ❓ 官网提供常见问题解答与赞助联系渠道，并支持查看往届会议（2023-2025）及相关技术会议信息。

---

### [](https://margelo.com/blog/speeding-up-expensifys-networking-with-nitro-fetch)

**原文标题**: [Speeding up Expensify's networking with NitroFetch - Margelo](https://margelo.com/blog/speeding-up-expensifys-networking-with-nitro-fetch)

文章介绍了 Expensify 如何迁移到 NitroFetch，通过全局替换 fetch 并针对关键启动请求启用原生预取，同时解决认证、证书固定等复杂生产环境问题，最终显著缩短了常规请求耗时和冷启动关键请求的完成时间。

- 📦 NitroFetch 是基于 Nitro Modules 的 fetch 替代品，底层使用 Cronet 和 URLSession，常规请求平均提速约 15–30%，并支持预取与流式能力。
- 🔄 Expensify 采用全局 polyfill 方式替换 `fetch`、`Headers`、`Request`、`Response`，Web 端保留浏览器原生 fetch。
- ⚙️ 安装后需重建原生应用，并在入口文件最先导入 polyfill，避免其他模块捕获旧的全局 fetch。
- 🚀 通过 `prefetchOnAppStart` 注册关键启动请求（如 `ReconnectApp`），让原生层在 JavaScript 启动前就开始网络请求，与 bundle 加载并行执行。
- 🧠 预取匹配依赖 `prefetchKey`，不比较 URL 或 body；因此注册时需保证请求描述与后续真实请求完全对应，否则可能取到错误数据。
- 🔐 启动预取涉及认证时，利用 `registerTokenRefresh` 在原生层刷新 token，并序列化认证请求供原生执行。
- 👤 持久化预取队列需按账户隔离：`prefetchKey` 中加入 `accountID`，并在登出或账号切换时调用 `clearTokenRefresh` 与 `removeAllFromAutoprefetch` 清理。
- 📱 原生接入：iOS 自动处理启动预取；Android 需在 `Application.onCreate()` 中调用 `AutoPrefetcher.prefetchOnStart(this)`，且失败不影响正常启动。
- ⏱️ 性能提升：常规请求时长降低 15–30%；关键启动请求完成时间 iOS P50 从 1676ms 降至 1409ms（-267ms，15.93%），Android P50 从 3223.5ms 降至 2573ms（-650.5ms，20.18%）。
- 🛡️ Expensify 的 Cronet 不继承原有 OkHttp 的证书固定配置，需自建证书固定实现并打补丁；自定义传输层行为应全面复查 DNS、TLS、代理等假设。
- 🧪 测试策略包含单元测试与多端 QA，并保持“失败开放”：预取失败不影响正常请求路径，注册或清理错误最多记日志。
- 💡 核心经验：在共享请求层迁移、完整替换原生全局对象、预取范围要窄、把原生预取视为持久化且带身份的数据、重新验证传输层安全，并用真实用户旅程测试而非仅测 HTTP。

---

### [](https://margelo.com/blog/building-a-3d-ai-avatar-in-react-native)

**原文标题**: [Building a 3D AI assistant using React Native and GPT-Realtime - Margelo](https://margelo.com/blog/building-a-3d-ai-avatar-in-react-native)

overview summary  
- 🐿️ 本文介绍如何用 React Native 与 GPT-Realtime 构建一个名为 AvatarAssist 的 3D AI 助手：一只会对话、可执行日程安排的松鼠角色。  
- 🧊 使用 Margelo 的 react-native-filament 渲染 GLB 模型，并通过 useModel、ModelRenderer 与 FilamentView 呈现场景。  
- 🎞️ 模型自带 20 个动画，但只使用 idle 与 wave；动画在 UI 线程渲染回调中逐帧驱动，避免 JS 阻塞。  
- 📷 相机采用 35mm 镜头投影，并支持拖拽旋转与重力感应视差；背景用循环视频而非静态图。  
- 🖐️ 阴影并非真实投射，而是用半透明椭圆 PNG 叠加在模型脚底，并随模型整体变换。  
- 🎙️ 绕过传统 LLM+TTS 串联延迟，改用 gpt-realtime 通过原生 WebSocket 直接接收音频 token；首个回复明显更快。  
- 🎚️ 音频用 react-native-audio-api 以 24kHz 播放，并以 Promise 链保证 PCM 块按序解码、连续播放。  
- 👄 口型通过音频 RMS 响度驱动：设置阈值门控与“开快闭慢”的非对称平滑，让嘴巴动作更自然。  
- 📅 模型可通过工具调用 add_calendar_event，调用结果回传会话并触发后续语音确认。  
- 🕒 每次会话指令都注入“当前本地时间与 ISO 8601 示例”，避免模型把“明天 9 点”算成错误时区。  
- ⚡ 启动优化：删除没用的动画剪辑、缩小模型，并用 react-native-bootsplash 的 HideOnDraw 在模型真正绘制后才瞬间隐藏启动屏。  
- 📊 对比显示云端 gpt-realtime 首字 574ms，优于最佳端侧模型 6130ms；端侧模型内存与 CPU 开销也明显更高。  
- ✨ UI 细节：使用 Liquid Glass 按钮、SF Symbols 配合 Material 图标回退、键盘动画让角色后退缩小、懒加载原生底部弹窗展示对话记录。  
- 🔓 项目整体开源，并列出所用 OSS 库与致谢贡献者。

---

### [未找到标题](https://expo.dev/blog/pasting-images-into-textinput-should-not-be-this-hard)

**原文标题**: [No title found](https://expo.dev/blog/pasting-images-into-textinput-should-not-be-this-hard)

请提供需要总结的文本内容，我才能按照模板为您生成要点列表。目前没有收到任何文章或段落。

---

### [](https://swmansion.com/blog/react-native-gesture-handler-s-touchable-the-button-we-wish-we-had-sooner/)

**原文标题**: [Gesture Handler's Touchable: Button We Wish We Had Sooner](https://swmansion.com/blog/react-native-gesture-handler-s-touchable-the-button-we-wish-we-had-sooner/)

React Native Gesture Handler 3 推出了全新统一的 Touchable 组件，旨在解决过去按钮组件过多、反馈各异的问题。该组件在保持高度可定制性的同时，利用平台级动画获得更优性能，并逐步取代旧有的按钮组件，成为大多数场景下的首选。

- 🔘 背景：团队曾因不同视觉反馈维护了 9 个按钮组件，造成混乱与重复开发，尤其在 React Native 演进后问题加剧。
- 🧩 解决方案：Gesture Handler 3 中推出统一组件 Touchable，并弃用其他旧按钮；保留 Pressable 作为 Touchable 的轻量包装，以便无缝替换原有 RN Pressable。
- 🎨 自定义能力：Touchable 允许针对默认、按下、悬停三种状态分别设置 scale、opacity 和 underlay 颜色，也支持各状态独立设置过渡时间。
- ⚙️ 平台级动画：内置动画运行在平台层（Android ObjectAnimator、iOS CoreAnimation、Web CSS），避免不必要的 JS 重渲染，并适配系统无障碍设置（如“减少动态效果”）。
- ⚡ 性能优势：测试数据显示 Touchable 渲染速度优于 Pressable 和旧 RectButton，在 Pixel 9 Pro 上均耗时约为 Pressable 的 0.88 倍，差异在高性能设备上更明显。
- 🧭 使用建议：大多数场景直接使用 Touchable；需要多击、长按等高度自定义交互时使用 useTapGesture；已有 RN Pressable 代码可继续用 Gesture Handler 的 Pressable 包装作为过渡。
- 🔄 迁移路径：未来主版本会移除已弃用按钮组件，建议尽早迁移；可手动修改或借助官方迁移技能自动完成。

---

### [](https://www.callstack.com/blog/working-with-the-react-native-super-app-showcase-repository)

**原文标题**: [Working With the React Native Super App Showcase Repository](https://www.callstack.com/blog/working-with-the-react-native-super-app-showcase-repository)

本文介绍了 Callstack 开源的 React Native 超级应用参考项目（Super App Showcase），它借助 Re.Pack 与 Module Federation V2 在运行时加载联邦化迷你应用，让独立功能团队可以自主发布，同时避免代码库碎片化、二进制膨胀和运行时崩溃。文章详细拆解了 Host Shell、联邦式迷你应用和 Shared SDK 三层架构，并说明了冷启动流程、模块管理、性能优化和生产部署要点，为构建和治理超级应用提供了可落地的参考蓝图。

- 🏗️ 架构角色划分清晰：Host Shell 是唯一包含原生二进制的包，负责根导航、启动逻辑、认证门槛和远端模块来源声明；联邦式迷你应用对应独立功能域，以单个导航器或 Provider 暴露；Shared SDK 作为单例库定义共享依赖契约与运行时服务。
- 📏 两条不可妥协的规则：原生代码只能存在于 Host Shell，否则重复注册原生模块会直接崩溃；所有共享包通过统一依赖目录声明版本，Module Federation 中的单例依赖需保持一致，避免出现第二个 React 实例破坏 Hooks 等问题。
- ⚙️ 冷启动流程精心设计：Host 启动时配置持久化脚本存储，让已下载的远端 Bundle 在应用重启后仍可用；随后挂载 Shared SDK 中的共享数据 Provider 并打开全局数据流，再通过 Suspense 加载认证 Bundle。
- 🔐 认证体验无闪烁：认证 Provider 在验证存储令牌期间保持初始加载态，原生启动屏作为 fallback 一直显示到会话状态确定，避免直接闪现登录界面。
- 🧩 迷你应用按需下载：通过认证后主导航才渲染；用户首次进入对应 Tab 或功能时，才会下载对应功能域的 JavaScript Bundle，实现运行时按需加载。
- 🛡️ Shell 的容错与模块解析：Host 使用 Module Federation V2 按平台动态解析 manifest 端点；每个远程挂载点都包裹错误边界，网络失败只会让该功能显示本地回退界面，其余应用不受影响。
- 🔑 认证逻辑独立部署：Auth Provider 以联邦化 render prop 暴露给 Host，Host 只根据来自远端容器的状态决定渲染内容，认证 UI 和逻辑可独立发布。
- 📦 迷你应用不携带原生代码：每个迷你应用暴露完整导航栈而非单屏，内部可自由增加路由；原生依赖全部声明为 peer dependencies，构建时借助宿主模块目录解析类型，运行时解析到 Shell 已加载的共享单例。
- 📚 Monorepo 与依赖目录管理：Shared SDK 通过单一工具函数生成所有打包器的共享依赖声明，新增或更新共享单例只需一行代码并自动同步到整个仓库；新增功能模块遵循明确的五步流程（初始化、配置联邦、设置解析、注册远程、加载边界）。
- ⚡ 实时性能和渲染优化：全局实时数据服务位于 Shared SDK 单例中，新订阅组件可同步拿到缓存并在首帧显示正确数据；高频价格更新被隔离在叶子组件，列表不整体重渲染，动画使用 Reanimated 共享值，并启用 React Compiler 与 transitions。
- 🌍 生产化考量：需将本地 manifest URL 换成稳定远程托管或可信任的发现服务，并制定缓存、回滚、离线、监控和签名验证策略；同时要用后端路由防止旧版本 Host 拉取不兼容的新 Bundle 版本。
- ✅ 参考价值：该 Showcase 把 Module Federation、Re.Pack、共享依赖和运行时加载放在真实应用中演示，清晰展示了 Shell 负责原生运行时与引导、迷你应用独立部署、Shared SDK 保持跨包一致性的分工，可直接改编到自己的团队与产品中。

---

### [](https://ospfranco.com/concurrent-engines-crash/)

**原文标题**: [React Native Bridgeless, race conditions with concurrent JS runtimes | Oscar Franco](https://ospfranco.com/concurrent-engines-crash/)

React Native Bridgeless 架构在重载或 OTA 更新时会让新旧两代 JS 运行时短暂并存，导致像 op-sqlite 这样的纯 JSI 模块因共享全局状态而触发竞态崩溃。文章剖析了具体失败场景，并提出按“代”隔离存活性标志、在构造/排队时绑定上下文等修复思路，同时总结了关键工程教训。

- 🔄 Bridgeless 重载期间新旧实例有数秒真实重叠，两条线程可同时访问同一原生模块状态，而旧桥接则是严格串行、先拆后建。
- 🧠 op-sqlite 把数据库列表、invalidated 标志和 CallInvoker 都放在进程级全局变量中，在“只有一个运行时”的假设下原本安全。
- 💥 崩溃发生：后台长查询被中断后回调回来时，全局 invoker 已被新代替换，导致 JSI 析构发生在错误线程或使刚销毁的旧运行时。
- 🔧 修复核心：让每个 generation 拥有独立的 `shared_ptr<atomic<bool>>` 存活性标志，`install()` 分配新标志，`invalidate()` 只翻转自己那一份。
- 📌 回调或排队任务在创建时拷贝并绑定当前 generation 的 `alive` 与 `invoker`，运行时只检查绑定的那份，绝不动态读取全局指针。
- ⏳ `DBHostObject` 构造时把全局状态存入成员变量，任何 update hook 自动获得正确且不可被后续全局替换骗过的上下文。
- ✅ 桥接重构后不能假设“全局当前运行时”恒存在；应在创建时捕获代际身份，而不是使用时借全局。
- 🛠️ 共享原生注册表需要真正的锁；失效时不仅被动等待，还应主动中断在途工作以确保预算内完成清场。

---

### [](https://configcat.com/blog/ab-testing-react-native-apps-with-feature-flags/?utm_source=thisweekinreact_newsletter&utm_medium=sponsor&utm_campaign=reactnative_202609)

**原文标题**: [A/B Testing React Native Apps with Feature Flags | ConfigCat Blog](https://configcat.com/blog/ab-testing-react-native-apps-with-feature-flags/?utm_source=thisweekinreact_newsletter&utm_medium=sponsor&utm_campaign=reactnative_202609)

概述：本文介紹如何在 React Native 應用程式中，結合 ConfigCat 功能旗標與 Amplitude 分析工具，執行嚴謹的 A/B 測試。內容涵蓋為何使用功能旗標、設定流程、事件追蹤、結果分析，以及測試結束後的清理與注意事項。

- 🧪 A/B 測試能讓不同用戶群看到不同版本，以降低全面上線風險，並以數據決定是否推出新功能。
- 🚩 功能旗標讓你在單一 App 版本中控制實驗，免去重新送審與等待商店更新的時間，也能即時關閉問題版本。
- ⚖️ 使用 ConfigCat 的百分比選項將流量 50/50 分流，確保用戶固定看到同一版本，提升實驗可信度。
- 📦 安裝 configcat-react、@amplitude/analytics-react-native 與 AsyncStorage 等必要套件。
- 🏗️ 在 ConfigCat 建立旗標後，透過 configcat-react 的 Provider 與 useFeatureFlag 決定按鈕文字（A/B 版本）。
- 📊 在 Amplitude 建立專案並設定來源，建立可重用的服務來傳送「SignupButton Clicked」事件。
- 🖱️ 每次點擊按鈕時記錄事件，並附上變體（如按鈕文字或明確的 A/B 屬性），方便後續比較分析。
- 📈 在 Amplitude 建立分析圖表，以 buttonText 分組並使用長條圖，每日檢查有無異常，有問題可立即關閉旗標。
- 🧮 測試結束後，利用 Amplitude 的 Compare 功能比較期間數據，判斷變體 B 是否值得全面推出。
- 🧹 結束測試務必清理：勝出就全量上線再移除旗標；落敗則設 false 並刪除旗標，避免產生殭屍旗標。
- 🔔 可善用 ConfigCat 的 flagEvaluated hook，自動傳送 $exposure 事件至 Amplitude，追蹤用戶所見變體。
- ✅ 藉由功能旗標，A/B 測試只需發布一次，即可涵蓋按鈕文案、定價頁、Onboarding 或結帳流程等各種實驗。

---

### [](https://gtkx.dev/blog/gtkx-1-4)

**原文标题**: [GTKX 1.4: Introducing @gtkx/navigation | GTKX](https://gtkx.dev/blog/gtkx-1-4)

文章介绍了 GTKX 1.4 版本的主要更新：核心是发布 @gtkx/navigation，用原生 libadwaita 小部件渲染 React Navigation，支持 stack、tab、drawer 和 split view 等导航器；同时加入资源/图标导入、受控列表选择、部署版本约束等改进，并说明了升级迁移和后续版本计划。

- 🚀 发布核心：GTKX 1.4 推出 @gtkx/navigation，由原生 libadwaita 小部件（AdwNavigationView、AdwViewStack、AdwOverlaySplitView、AdwNavigationSplitView 等）驱动 React Navigation，覆盖 stack、tab、drawer 与 adaptive split view。
- 🧭 导航状态仍由 React Navigation 核心负责，渲染层只处理 GTK 外观和平台体验，因此页面转场、HeaderBar、返回按钮、手势和可访问性均与 GNOME 一致。
- 🔤 导航树类型安全：路由参数集中在导航器定义中，屏幕 props 与 navigate/静态配置自动推导，开发期即可校验 Route params 与 navigation 调用。
- ↪️ 原生返回天然同步导航：HeaderBar 返回按钮、Escape、Alt+Left、鼠标侧键和 Adwaita 边缘滑动都会通过 React Navigation 分发；usePreventRemove 可拦截 pop 并弹出确认/丢弃对话框。
- 🗂️ Tabs 和 Drawer 的平台化：标签页用 AdwViewStack 实现，支持懒加载、tabPress 阻止切换、popToTopOnBlur；抽屉使用 AdwOverlaySplitView，支持 collapsed 状态、DrawerActions 和自定义 drawerContent。
- ➗ 分屏导航器适合 GNOME 主从界面：createSplitViewNavigator 的侧栏与内容栈在 AdwBreakpoint 折叠时自动变成单视图，返回从内容页回到侧栏，且导航状态在宽窄布局中保持同一套数据模型。
- 🧪 测试友好：配合 @gtkx/testing，测试直接点击可见控件、输入文字或发送 Escape；禁用动画后 push/pop 在断言前已完成，不需要导航专用测试设施。
- 📦 新的 opt-in 资源导入：future.v2ResourceImports 支持用 ?resource、?icon、?url 将文件加入模块图，开发时热更新资源，生产构建生成并注册 gtkx.gresource；新项目默认启用。
- 🖼️ applicationIcon 转移到顶层配置，统一开发与打包入口，兼容单张图标或完整图标主题目录，保留 symbolic 与尺寸变体。
- 🎛️ GtkListBox 增加受控 selectedIndex 属性，索引选择匹配行，-1/null 清除；组件等待 children、抑制自身写入的 notify 并纠正漂移，便于侧栏高亮直接绑定路由。
- 🧰 部署增强：deploy.minimumLibraryVersions 可写明 Debian/RPM 的库版本约束；GTK/libadwaita 之外的 GIR 依赖通过 deploy.depends 指定发行版包；构建元数据在 1.4 中改变，--skip-build 提升前需重建一次。
- 🔧 原生边界修复与升级注意：信号名必须用 GLib 拼写（如 data-changed）；部分所有权不安全的 Cairo API 被移除；回调中借用的结构体只在调用期间有效；deploy.icons 需迁移到 applicationIcon。
- 🔜 未来规划：@gtkx/forms 和 @gtkx/i18n 预计与 GTKX 1.5 一起发布。

---

### [](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.6.0)

**原文标题**: [Release Reanimated - 4.6.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.6.0)

react-native-reanimated 发布了 4.6.0 版本，主要新增 React Native 0.87 支持、CSS 动画与过渡回调的原生化、contrastColor 工具函数，以及 Android 平台驱动 CSS 过渡的实验性特性，并包含大量稳定性修复与新贡献者更新。

- 🎉 支持 React Native 0.83–0.87，需搭配 Worklets 0.12.x
- 🔄 新增 CSS 动画与过渡回调（如 onCSSAnimationStart/End、onCSSTransitionRun/End）在 iOS 和 Android 上的原生支持
- 🎨 新增 `contrastColor` worklet，可自动返回与给定颜色对比度更高的黑或白，支持动画与 JS 线程使用
- 🤖 实验性功能：Android 上可通过 ObjectAnimator 驱动 opacity 过渡，默认关闭，需通过特性开关启用
- 🐛 修复多项问题：伪类选择器、触摸 :hover/:active、CSS 关键帧插值、文本样式过渡、键盘动画崩溃、布局动画闪动等
- 🛠️ 优化性能：批量 CSS 事件投递、过渡命令批处理、复用帧回调等
- 🧑‍💻 新增 14 位首次贡献者，包含多项依赖与类型兼容性改进

---

### [](https://kirillzyusko.github.io/react-native-teleport/blog/1-2-0-android-fast-reparenting)

**原文标题**: [What's coming in 1.2.0: smoother teleportation on Android 🚀 | Teleport](https://kirillzyusko.github.io/react-native-teleport/blog/1-2-0-android-fast-reparenting)

1.2.0 版本针对 Android 平台的视图重挂载机制进行了重构，通过新的快速路径避免 teleport 时出现空白帧，尤其改善了视频和地图等 surface 内容的切换流畅度，且完全向后兼容。

- 🚀 核心改进：重新设计了 Android 上的 reparenting 机制，采用轻量级 detachViewFromParent/attachViewToParent API，实现同步移动且不脱离窗口。
- ⬜ 问题根源：旧版使用 removeView/addView 会临时分离视图，导致 SurfaceView/TextureView 的渲染表面断开，在下一帧前露出背景空白。
- 🎥 显著提升：视频、地图等 surface-backed 视图在 teleport 时不再闪烁或出现空白帧，切换更加无缝。
- 🛡️ 安全兜底：仅当两个父视图属于同一 Android 窗口且无焦点/布局过渡需求时启用快速路径，否则自动回退到旧逻辑，无需开发者配置。
- 🧪 测试保障：新增端到端回归测试，自动检测视频 teleport 中的空帧；并在 Android API 28、31、36 上验证了视频和地图内容。
- ✨ 升级方式：无破坏性 API 变更，直接运行 yarn add react-native-teleport@1.2.0 即可，旧项目自动享受优化。
- 📝 反馈渠道：升级后若仍遇到空帧，可携带设备、Android 版本及视图类型提交 issue。

---

### [](https://github.com/margelo/nitro/releases/tag/v0.37.0)

**原文标题**: [Release Release 0.37.0 · margelo/nitro · GitHub](https://github.com/margelo/nitro/releases/tag/v0.37.0)

margelo/nitro 的 v0.37.0 版本于 2026-08-20 发布，包含 2 项特性、14 项问题修复和 1 项文档更新。本次更新主要将 Props 与 ComponentDescriptor 移入 Nitro Modules 核心，并针对 View 属性处理和回收机制做了一系列稳定性修复。

- ✨ 特性：通过 C++ 模板将 Props 和 react::ComponentDescriptor 移入 Nitro Modules 核心
- 🐛 修复：将 react-native-nitro-modules 的 peer dependency 标为可选；CachedProp 更名为 ReactProp，并保留旧名作为弃用别名
- 🐛 修复：提升 View Props 的引用安全、不可变性与解析兼容性，包括避免悬空引用、使 CachedProp 和快照不可变、为 RN<85 添加 RawPropsParser bool 参数、保留数组/Record 值的 `| undefined`、保留经典解析方式与原生默认值
- 🐛 修复：完善 View 回收与复用的跨平台行为，调用基础 View Component Descriptor 的 adopt、重置可回收 View、在 Android 上要求 props 可构造的 View state、支持 iOS 的 View drop 上报以及 recycling fallback
- 📚 文档：将 react-native-nitro-theme-transition 加入 awesome 列表

---

### [从 v3 升级 | 屏幕转场](https://screen-transitions.esjr.org/migrating-from-v3/)

**原文标题**: [Upgrading from v3 | Screen Transitions](https://screen-transitions.esjr.org/migrating-from-v3/)

本文是“屏幕转场架构”从 v3 升级到当前版本的指南，重点说明迁移中需要修改的依赖、导入、API 与行为验证，大部分既有转场代码无需调整。

- 🔄 大多数转换代码无需改动；迁移工作集中在依赖、导航器导入以及 v3 已弃用的 API 上。
- ⏳ v3 仍兼容旧生态；当前版本要求 React 19.2、Reanimated 4、Worklets 0.8、React Navigation 7.3+，Expo Router 需 56.2.10+（仍为 Alpha）。
- 📦 替换导航器导入：React Navigation 改用 `react-native-screen-transitions/react-navigation`，Expo Router 改用其专属入口点。
- 🗑️ 移除 v3 导航器专属 props：不再支持 `nativeScreens`、`enableNativeScreens` 及 `independent`；独立导航树需配合 `NavigationIndependentTree`。
- ♻️ 替换弃用的转场别名：如 `snapVelocityImpact→gestureSnapVelocityImpact`、`expandViaScrollView→sheetScrollGestureBehavior`、`gesture.direction→initiator` 等。
- 🖼️ 移除旧版共享预设（`SharedIGImage` 等），改用 `bounds(id).navigation.zoom()` 或基于 `bounds(id).styles()`/`values()` 自定义构建。
- 🧪 非活动屏幕行为（`hide`/`pause`/`unmount`/`keep`）实现改为 React 19.2 Activity；需测试订阅、输入框、滚动状态、嵌套导航和昂贵副作用。
- 📱 在 iOS 和 Android 上验证：快速 push/pop、手势取消与重复滑动、深层 bounds 堆栈、重叠转场中的浮动遮罩、四种 inactive 模式，以及嵌套堆栈和深链场景。

---

### [Maestro CLI 2.9.0：浅色和深色模式在一个流程中](https://maestro.dev/blog/maestro-cli-2-9-0)

**原文标题**: [Maestro CLI 2.9.0: light and dark mode in one flow](https://maestro.dev/blog/maestro-cli-2-9-0)

Maestro CLI 2.9.0 发布，重点支持在同一流程中测试明暗模式，并改进 WebView 兼容性、配置灵活性及 Android/Web 可靠性。

- 🌗 新增 `setDarkMode`、`toggleDarkMode`、`assertDarkMode` 和 `assertLightMode` 命令，可在一次流程中切换并验证浅色与深色模式，支持 iOS、Android 和 Web。
- 📁 `config.yaml` 支持否定通配符（如 `!文件`），可跳过指定非 Maestro YAML 文件，测试目录内文件无需重排。
- 🕸️ Android WebView 检查增强：可稳定捕获 React、Vue、Angular 等 SPA 页面元素，深层 DOM 也能完整读取，无法读取时快速失败并给出明确错误。
- 🛡️ Android 16（API 36）上单个 WebView 无响应时会被隔离，不再阻塞整个流程运行。
- 🌐 Web 流程兼容 Chrome 151+，命令可正确作用于页面，并增加响应超时防止无响应目标挂起运行。
- ✅ Android 表单验证错误现可被文本匹配器读取，可直接断言“Email is required”等提示信息。
- 🔤 空输入框在视图层级中以空 `text` 报告，占位符单独作为 `hintText` 暴露，便于区分空值与已填充状态。
- ⏱️ `setDeviceLocale` 在慢速设备上最多额外等待 30 秒，确保系统应用语言设置。
- 🔁 `maestro cloud` 上传状态轮询遇到无响应时会自动重试，与服务器错误共享预算，避免网络波动导致 CI 步骤失败。
- ⬆️ 建议更新至 2.9.0，完整变更日志见 GitHub 链接，升级指南涵盖 macOS、Windows 和 Homebrew。

---

### [](https://github.com/uni-stack/uniwind/releases/tag/v1.11.0)

**原文标题**: [Release Release v1.11.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.11.0)

uniwind 发布了 v1.11.0 版本，主要新增 filter 支持与 scoped variables，修复 React Native 0.87 相关兼容问题，并进行了多项代码整理；本次更新共 10 个提交，含一位新贡献者。
- 🚀 新增 iOS 与 React Native 0.87 canary 的 filter 支持，以及 scoped variables 功能。
- 🐛 修复 uniwind 类型与 React Native 0.87 的兼容问题，并添加 browser exports 字段解决 Web RN 打包错误。
- 🧹 清理 filterFn、优化 dataSet 处理、更新颜色方案逻辑，并为测试增加类型检查。
- 🎉 新贡献者 @dlebedynskyi 的首次贡献；本次贡献者还包括 @jpudysz 和 @Brentlok。
- 📜 完整变更见 v1.10.1...v1.11.0。

---

### [发布 v0.21.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.21.0)

**原文标题**: [Release v0.21.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.21.0)

页面展示了 software-mansion/argent 项目的 GitHub v0.21.0 发布说明，主要包含针对 profiler、flow 自动化、工具链的修复与改进。尽管页面有多次加载错误提示，但核心内容是来自 v0.20.0 到 v0.21.0 的 49 个提交更新。

- 📦 发布 v0.21.0：由 github-actions 发布，包含自 v0.20.0 以来的 49 个提交，完整变更见 v0.20.0...v0.21.0。
- 🔬 修复 profiler 相关问题：按分析报告实际输出的组件名处理、用 Metro 的 logicalDeviceId 识别设备、支持 top_n 参数并修正 CPU 窗口取样方式。
- 💪 增强 flow 稳定性：iOS 主线程卡顿不再导致步骤失败；重构 when 块机制、手势 selector 未解析时先 settle，并保证 settle 至少进行两次读取。
- 🔨 新增 shake 工具：适用于 iOS 模拟器和 Android 模拟器，还可在 microinteractions 标志后晃动宿主窗口。
- 🧩 工具链调整：移除工具输入 schema 中的顶层 JSON Schema 组合器；工具服务器拒绝同时携带 text 和 key 的键盘调用。
- 🧪 测试与 E2E 修复：将组件名测试使用模块导出类型；固定 npm postinstall hook 缺失的问题；截图差异支持尚不存在的 outputDir。
- 👥 参与贡献者：j-piasecki、kacperkapusciak 以及其他 3 位贡献者；版本获 3 个 👍 回应。

---

### [](https://github.com/callstackincubator/rozenite/releases/tag/v2.3.0)

**原文标题**: [Release v2.3.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v2.3.0)

Rozenite v2.3.0 正式发布，最大亮点是新增对 Lynx 的支持，使同一套 DevTools、插件与 CLI 可直接调试 Lynx 应用；同时带来多项 CLI、中间件、UI 和测试方面的改进与修复。

- 🚀 核心发布：Rozenite for Lynx，通过 @rozenite/lynx 在 Lynx 后台线程安装运行时，@rozenite/lynx-dev 作为 rspeedy 插件桥接 DebugRouter 与 inspector 协议，无需修改 DevTools 即可适配 Lynx。
- 🔌 插件与集成：官方插件声明了各自支持的集成；中间件可解析目标集成，并允许插件声明支持；同时按目标解析 CDP 能力配置，便于插件按域过滤工具。
- ⚙️ CLI 与构建：插件入口改为用 tsc 编译（替代 Vite）；新增 rozenite agent tap 将插件消息流式输出到 stdout；`rozenite open` 现在会扫描每个集成的默认端口。
- 🧪 测试与质量：新增 @rozenite/testing 包，支持进程内插件协议测试；CI 缓存 Turborepo 产物并强制格式化检查；通过测试防止发布包误带 Rozenite 开发代码。
- 🛠️ 中间件改进：重构 agent console 缓冲、预览和光标；新增 React 渲染报告聚合与组件错误暴露；getProfileTimeline 可报告提交成本；修复会话重连时 React 出站通道的重新绑定问题。
- 🎨 UI 与体验：新增 RozeniteLoader、ToggleGroup、VirtualizedList、QueryField 等组件；应用启动时显示连接设备的启动画面，并标注正在调试的框架名称。
- 📊 性能分析插件：require-profiler-plugin 已迁移到 @rozenite/ui，并新增包合并、require 链和重复依赖检测能力。
- 🐛 关键修复：调试器源现在从 Expo 的 dev server 派生；允许被能力过滤的域拒绝不拥有的工具；Playground 深度链接改用 rozenite:// 协议。
- 📱 新示例：新增 Lynx playground 应用，便于快速体验 Rozenite for Lynx。
- 📚 网站与文档：升级 Rspress 至 2.0.21；将 Storybook 构建纳入 Turborepo 任务，完善发布与文档流程。

---

### [](https://github.com/callstack/agent-device/releases/tag/v0.20.10)

**原文标题**: [Release v0.20.10 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.20.10)

agent-device v0.20.10 版本发布，重点提升 AI/LLM 集成、移动端自动化准确度、Web 交互能力以及 CI/云运行的可靠性与安全性，共含 44 个合并 PR。

- 🤖 集成增强：新增第一方 agent-device/ai-sdk 工具集，支持 AI SDK 应用直接调用；精简 MCP 服务器指令并添加 MCP-only 帮助工具，降低配置与发现成本。
- 📱 iOS 快照优化：统一私有 AX 滚动可见性，移除离屏子树泄漏及被裁剪后代；将快照呈现显式化，并让过渡快照基于可见捕获生成。
- 📲 Android 可见性与手势修复：覆盖兄弟节点仅隐藏其实际覆盖内容；快照作用域只解析一次并披露 API 23 遮挡扫描缺口；饱和滚动手势保持在状态栏下方。
- 🖱️ 新增 Web hover 命令：支持悬停门控菜单、工具提示等仅靠点击或触摸无法操作的网页 UI。
- 🔒 会话与云运行安全加固：拒绝 `.`、`..` 及空会话名等无效路径；无会话变更操作强制设备认领；远程守护进程诊断可传回调用者；WebDriver 云会话创建设有独立预算，避免泄漏计费会话。
- ✅ CI 流程精简：跳过仅含文档变更的设备车道；停靠的 replay 套件改为仅手动分发；夜间 iOS 运行完整 XCTest 套件；临时 GitHub 评论失败不再导致 Bundle Size 任务失败；移除冗余或级联作业。
- 🧹 其他稳定性修复：拒绝选择器形态的等待参数、移除开发环境中的重复测试目录、锁定超长测试文件行数等。
- 📦 发布统计：46 个提交、44 个合并 PR、1 位贡献者（@thymikee），完整对比范围 v0.20.9...v0.20.10。

---

### [发布 v0.6.0 · henrypldev/react-native-nitro-mlx · GitHub](https://github.com/henrypldev/react-native-nitro-mlx/releases/tag/v0.6.0)

**原文标题**: [Release v0.6.0 · henrypldev/react-native-nitro-mlx · GitHub](https://github.com/henrypldev/react-native-nitro-mlx/releases/tag/v0.6.0)

该发布为 react-native-nitro-mlx 的 v0.6.0 版本（2026-08-21），主要新增了多项 iOS 与语音相关功能，同时修复了嵌入和语音识别中的关键问题，并优化了智能体聊天体验。

- ✨ iOS 新增按轮次（turn-scoped）的推理原语，便于更灵活的多轮交互（#40）
- 🔄 规范化 LLM 生成轮次的输出结果（#39）
- 🤖 简化智能体聊天体验（#42）
- 🗣️ TTS 支持可配置的语音速度（#36）
- 🐞 修复 embeddings 的 MLX 输入限制和掩码问题（#37）
- 🎙️ 定义并校验直接 STT 音频传输契约（#38）

---

### [E](https://expo.dev/services/simulators)

**原文标题**: [EAS Simulator: Simulators built for agents](https://expo.dev/services/simulators)

Expo 推出 EAS Simulator（早期访问），这是一个专为 AI 代理打造的云端模拟器服务。代理可以按需启动安全隔离的云模拟器，安装构建、实际操作并自行验证结果，支持大规模并行运行，最终把证明以录像形式直接呈现在 PR 上，从而真正“闭环”验证代理编写的代码。

- ☁️ 提供“为代理构建的模拟器”：按需快速启动安全的云端 iOS 模拟器，支持并行运行多个实例。
- 🔁 闭环工作流示例：崩溃报告进入队列 → 代理修复代码 → 构建在云模拟器运行 → 会话录像作为证据附在 PR 上。
- 🧩 无需手写冗长说明：用实际运行录像代替“看起来没问题”的代码描述。
- 📈 弹性伸缩：模拟器可按需扩容并行执行，代理任务结束后自动销毁。
- 🔒 安全隔离：每个会话相互隔离，并运行在与 EAS Build、Submit、Workflows 相同的可靠基础设施上。
- 🛠️ 兼容现有工具：支持通过 argent 或 agent-device 驱动模拟器，与本地工作流保持一致。
- ⌨️ 一键启动会话：执行 `eas simulator --platform ios`，代理获得可操控的模拟器，你可实时观看运行过程。
- ✨ 当前为早期访问阶段，可通过加入等待列表或联系团队获取体验资格。

---

### [](https://infinite.red/react-native-radio/rnr-371-rnr-explains-pan-responder)

**原文标题**: [React Native Radio - RNR 371 - RNR Explains: Pan Responder](https://infinite.red/react-native-radio/rnr-371-rnr-explains-pan-responder)

这一集 React Native Radio 解释了 React Native 内置的 PanResponder API，它是用于处理触摸手势的基础工具。虽然大多数实际场景中开发者会优先选择性能更好的 React Native Gesture Handler，但理解 PanResponder 能帮助你掌握手势生命周期和底层触摸处理机制，也适合简单应用或不想引入额外依赖的情况。

- 🤏 PanResponder 是 React Native 内置的触摸手势识别 API，支持拖拽、滑动、多点触控等操作。
- ⚡️ 它主要在 JavaScript 线程上处理事件，因此性能受限；React Native Gesture Handler 在原生侧处理，更快更顺滑。
- 🧩 适用场景包括简单原型、避免第三方依赖、库作者，以及想理解手势底层原理的开发者。
- 🔄 原生触摸事件从 iOS/Android 派发到 JS 层，JS 计算后再返回原生层响应；新架构提升了这一流程的效率。
- 🎛 核心回调有 onStartShouldSetPanResponder、onMoveShouldSetPanResponder（是否认领触摸），以及 onPanResponderGrant、Move、Release、Terminate 等生命周期回调。
- 📊 gestureState 对象提供 dx/dy、vx/vy、moveX/moveY、x0/y0 和活动触摸数，可用于绘图、手势映射和动画判断。
- 🛠 使用时通过 PanResponder.create(config) 创建实例，把返回的 panHandlers 绑定到 View，并通常放入 ref 保持稳定。
- 📚 虽然约 99% 的实践场景仍建议使用 React Native Gesture Handler，但学习 PanResponder 能让你更深刻地理解 React Native 的触摸处理机制。

---

### [](https://infinite.red/react-native-radio/rnr-372-looking-back-on-chain-react-2026)

**原文标题**: [React Native Radio - RNR 372 - Looking back on Chain React 2026](https://infinite.red/react-native-radio/rnr-372-looking-back-on-chain-react-2026)

这是一期对 Chain React 2026 大会的复盘播客。Robin、Mazen 和 Gant 回顾了会议中关于 AI、React Native、工作坊、赞助商、美食与社交互动等内容，强调线下会议中“人与人连接”的不可替代价值，并透露明年已有新计划。

- 🎙️ 主持人 Robin、Mazen 与 Gant 在会后录节目，笑谈“Chain React 宿醉”，并用 Gant“走到哪都有水灾”的趣闻开场。
- 🤝 核心观点：线下会议仍然重要，真正的价值在“走廊社交”和直接对话，而不是事后可看录像的演讲内容。
- 🏢 赞助商非常踊跃，RevenueCat 的盲盒与自拍拉花咖啡最吸睛，Callstack、Expo、Infinite Red 等也都用心布展。
- 🛠️ 工作坊日意外扩大为四个，包括 Expo/Infinite Red、Software Mansion 动画、女性科技主题，以及 Amazon 的 React Native AI 相关场次，反馈全部正面。
- 🗣️ 由 Expensify 主持的核心贡献者聚会，让 Meta、Expo、Callstack、Software Mansion 等团队与产品用户直接对话，讨论痛点和未来方向。
- 📡 会议 Wi-Fi 报价高达 12000 美元，Gant 拒绝后由 Jed 用约 4500 美元的自建设备加蜂窝数据卡搞定，并且全程相当稳定。
- 🍽️ VIP/演讲者晚宴在 10 Barrel Brewing 屋顶举行，自由交流氛围浓厚；会议餐饮则由 Devil's Food Catering 提供，被形容为“米其林级”享受。
- 🎤 开幕日由 Expo CEO Charlie Cheever 的主题演讲切入“AI 是房间里的大象”，随后 Mazen 演示了移动端向量数据库与完全离线的 AI 应用。
- 💪 第二天开场演讲是 Seth 的个人经历，他用自己开发的声音 App 改善医疗处境，激励全场“I'm a builder”。
- 🎯 为了提升午餐后低迷气氛，主办方设计了“Software Squares”游戏秀，多位知名社区成员参与，笑点密集，成为全场高光之一。
- 🃏 定制“收藏卡”是本次大会的一大亮点，鼓励参会者主动找演讲者和赞助商交流，也对新人和内向者非常友好。
- 🎉 会后派对在 Expensify 的古银行总部举行，现场豪华且人气高涨；参与者还继续探索波特兰的酒吧、餐厅和街机吧。
- 🔮 大会接近尾声时，团队暗示明年已有“大想法”，甚至开玩笑说可能是“Chain React 邮轮”，引来大家会心一笑。

---

### [](https://www.bram.us/2026/08/20/the-future-of-css-target-multiple-classes-with-the-class-prefix-selector/)

**原文标题**: [The Future of CSS: Target Multiple Classes with the Class Prefix Selector – Bram.us](https://www.bram.us/2026/08/20/the-future-of-css-target-multiple-classes-with-the-class-prefix-selector/)

概述：本文介紹了 CSS 即將推出的「類別前綴選擇器」（Class Prefix Selector），旨在簡化對具有相同前綴的多個類別的樣式設定，解決現有使用屬性選擇器效能低落、需額外加入基礎類別或冗長列舉的問題，並說明其語法、設計決策與目前的瀏覽器支援狀態。

- ✨ 新選擇器 `.prefix-*` 正式加入 CSS Selectors Level 5，可一次匹配所有以指定前綴開頭的 class，例如 `.btn-*` 可涵蓋 `.btn-primary`、`.btn-secondary` 等。
- 🐢 現行做法效能不佳：`[class*=" btn-"]` 這類屬性選擇器比一般 class 選擇器慢近 20 倍，且會耗費 frame budget。
- ⚙️ 語法非常簡單：在 class 名稱後加上 `-*` 即可，例如 `.btn-* { ... }`，不需修改 HTML 或列出所有類別。
- 🚫 此選擇器預設**不會**匹配空字串或雙連字號的情況，例如 `class="foo-"` 或 `class="foo--"` 不會被 `.foo-*` 選中。
- 🔍 目前僅支援連字號（`-`）作為分隔符；其他分隔符（如 `_`）未來可能加入，但任意萬用字元（如 `.foo*`）與中間萬用字元（如 `.card-*-primary`）將不被允許，以避免過度匹配與影響瀏覽器效能最佳化。
- ❌ CSSWG 決定不重用既有的 `[class|="foo"]` 屬性選擇器，原因包括：`|=` 會同時匹配精確值（如 `en`）造成誤用、無法匹配非開頭的 class、效能較差，以及為了未來 CSS 萬用字元擴充（如 `[data-*]`、`custom-framework-*`）鋪路。
- 🌐 瀏覽器支援尚未開始（Chromium、Firefox、Safari 皆為 ❌），此功能仍屬早期草案，可能需要數年才能正式使用。
- 🧪 可用 `@supports selector(.foo-*)` 進行功能偵測，文章附有 CodePen 示範。

---

### [](https://bsky.app/profile/did:plc:hxmev3uady7j4litwnr5fzbg/post/3muk7eu23w22b)

**原文标题**: [@sebastienlorber.com on Bluesky](https://bsky.app/profile/did:plc:hxmev3uady7j4litwnr5fzbg/post/3muk7eu23w22b)

Seb 分享了一則關於 HTML 規格新進展的消息：支援「無序串流」（out-of-order streaming），允許以模板稍後取代文件中的佔位清單，目前已獲 Chrome/Edge 支援，並可能為 React SSR 的 Suspense 帶來新可能。

- 🎉 HTML 規格正式納入「無序串流」（out-of-order streaming）功能
- 📄 文件中原本的「清單」佔位符，可被稍後出現的模板內容取代
- 🚀 Chrome 與 Edge 已率先支援此功能
- 👍 其他瀏覽器對此持正面態度
- 🔮 未來有望為 React Suspense 的伺服器端渲染（SSR）提供新動力

---

### [pnpm 12.0 | pnpm](https://pnpm.io/blog/releases/12.0)

**原文标题**: [pnpm 12.0 | pnpm](https://pnpm.io/blog/releases/12.0)

pnpm 12 稳定版发布，基于 Rust 重写，兼容 pnpm 11 的命令、标志、设置和锁文件格式，安装需使用 next-12 标签；主要带来性能提升、安全强化与若干新功能，同时明确了若干破坏性变更与修复。

- 🦀 基于 Rust 重写，兼容 pnpm 11 全部命令、标志、设置和锁文件格式，升级体验平滑
- 📦 安装需通过 `pnpm self-update next-12` 获取，npm `latest` 仍指向 11 版本
- 🔗 Git 依赖统一通过 HTTPS 解析身份，SSH 仅用于实际传输，锁文件不再记录 SSH URL
- ⚠️ `pnpm-workspace.yaml` 中未知设置会报错或警告，并提示最接近的正确拼写
- 🔄 循环依赖图的 peer 解析固定剪切边，锁文件可复现，大型工作区解析速度提升 2–3 倍、内存减少约 25%
- 💾 Linux 上 `auto` 导入优先使用硬链接，btrfs 上物化 `node_modules` 时间约减半
- 🚫 `engineStrict` 现在会因常规依赖链中不兼容的引擎而失败，不再受 optional 子树影响
- 🌐 全局安装的 node/deno/bun 可按项目自动切换版本，支持 `globalShims` 配置，默认信任签名版本
- 📥 pnpm 可安装并运行 npm、Yarn Classic/Berry/6、Bun，支持 `pnx` 与 `pnpm shim add`
- 🏷️ 新“registry revisions”机制：允许同一版本替换 tarball，锁文件记录 revision 行，可用 `pnpm update --patches` 获取
- 🎯 `pnpm init` 现在固定最新发布版本，而非运行命令的版本，失败时回退到当前版本
- ✅ `pnpm stage approve` 支持批量批准，按依赖顺序处理，一次 OTP 覆盖整个批次
- 🧹 `audit.ignorePrune` 可清理审计报告中已不再出现的忽略条目
- 🛑 `pnpm setup`、`self-update` 等全局修改命令在 sudo 下拒绝运行，防止污染 root 主目录
- ☁️ 远程副作用缓存（概念验证）：可上传/下载依赖构建产物，仅限 Linux/glibc x64 与 arm64
- 🔧 内置兼容数据库移除静态分析依赖，解决 TypeScript 7 版本冲突等异常
- 📂 当项目上层无目录可硬链接时，默认 store 放入 `node_modules/.pnpm-store`，适配沙箱环境
- 🗑️ `hooks.filterLog` pnpmfile 钩子已弃用，改用 `loglevel` 控制输出
- 📝 新版文档与“What's different”页面说明所有变更细节，欢迎反馈问题

---

### [](https://zod.dev/blog/zod-4-5)

**原文标题**: [Zod 4.5](https://zod.dev/blog/zod-4-5)

overview summary
- Zod 4.5 正式发布，npm 安装 `zod@latest` 即可体验，新版本聚焦于大幅提升解析性能、降低内存占用，并引入了预编译模式 `z.compile()` 以及一系列新 API 和严格化修复。
- 🚀 旗舰功能 `z.compile()`：允许对任意 schema 进行预编译，解析速度最高可提升约 9 倍，并支持通过 `import "zod/compile"` 或 Node.js CLI 参数实现全应用自动编译。
- ⚡ 性能优化：`.safeParse()` 不再捕获堆栈跟踪，使失败路径解析提速约 7.5 倍；单个 schema 的内存占用从 7.5kb 锐减至 784 字节，降幅达 9 倍。
- 🆕 新增 `z.creditCard()` 校验器，支持 12-19 位数字及空格/连字符分隔，并附带 Luhn 校验和验证。
- 🆕 新增 `z.properties()`：作为 `z.property()` 的多属性版本，允许在 `instanceof` 等 schema 上追加属性约束。
- 🆕 恢复 `z.deepPartial()` 为顶层函数，并新增 `.exactPartial()` 方法，用于生成 `exactOptionalPropertyTypes` 语义下的可选字段（显式 `undefined` 会被拒绝）。
- 🆕 新增 `z.validate()`/`z.validateAsync()` 快速校验入口，仅返回布尔值而不构造 `ZodError`，无效输入场景下比 `.safeParse().success` 快至 16 倍。
- 🆕 新增 `z.input()`/`z.output()` 运行时工具，用于独立校验编解码器两侧的数据形态；新增 `z.toZod<T>()` 辅助静态类型到 schema 的映射。
- 🆕 新增 `z.getDiscriminatedOption()`，可按判别值安全地提取判别联合中的成员 schema。
- 🔄 递归 schema 现在支持解析循环输入（Zod Mini 需显式注册 memoizer），参考循环对象可被正确解析且保持引用同一性。
- 🔑 `z.object()` 现支持声明 symbol 键，TypeScript 可将其推断为唯一 symbol 并纳入必填校验。
- ⚠️ 破坏性修复：`z.iso.datetime()` 对带时区偏移的输入强制要求秒级精度；`z.string()` 长度计算由 UTF-16 码元改为 Unicode 码点；record 键与 intersection 行为对齐 TypeScript 索引签名语义。
- 🛡️ 安全加固：`__proto__` 键一律被剔除，字符串格式如 `z.ipv6()`/`z.ulid()`/`z.httpUrl()`/`z.emoji()` 的校验逻辑全面收紧以修复绕过及性能问题。
- 🧩 新增 8 种语言环境（locale），包括孟加拉语、印地语、卡纳达语、巴西葡萄牙语、斯洛伐克语、土库曼语、中库尔德语与挪威尼诺斯克语。
- 📦 版本共合入 155 个提交，并同步更新了 JSON Schema 转换、`fromJSONSchema` 导入器及错误信息映射等周边工具的兼容性与正确性。

---

### [虚拟 GPU](https://vgpu.sh/)

**原文标题**: [vgpu](https://vgpu.sh/)

vgpu 是一个基于 WebGPU 的着色器工具，让同一份 shader 代码可在浏览器、无头 Node.js 及 CI 环境中复用，支持交互渲染、任意分辨率输出、视频生成与自动化快照测试，并提供 WGSL 模块化、CLI 辅助与丰富示例文档。

- 🎨 一套 shader 随处渲染：浏览器交互、任意分辨率、视频导出、无头 Node.js 与 CI 测试均可用同一特效代码。
- 🧩 示例展示 `effect()` 与 `draw()` 的简洁用法，可轻松绑定 uniform、逐帧渲染并在适当时释放 GPU 资源。
- 📦 WGSL 可像 TypeScript 一样导入导出：自动解析模块图、反射绑定、剔除未使用声明并压缩生成精简源码。
- 🛠️ 内置 CLI（`npx vgpu`）引导开发者：提供文档阅读、示例拉取、WGSL 校验和运行时诊断修复。
- ✅ 支持 CI 渲染测试：`pnpm test:render` 可编译 shader、渲染无头帧、对比快照，快速验证正确性。
- 🌊 官方示例覆盖丰富场景：Next.js 徽标体积散射、FFT 海面、Radiance Cascades 全局光照及 ONNX 深度估计等 WebGPU 演示。
- 📚 文档体系完整：含快速开始、核心概念、API 参考和只读源码示例，并为 agent 工具链提供 OpenAPI 3.1 描述。

---

### [](https://remix.run/blog/remix-3-release-candidate)

**原文标题**: [Remix 3 Release Candidate | Remix](https://remix.run/blog/remix-3-release-candidate)

2026 年 8 月 31 日，Remix 团队发布了 Remix 3 的首个 Release Candidate（RC）。该版本将数据库管理、schema 验证、类型安全路由、无打包资源服务及全新 UI 运行时整合进单一的 `remix` 依赖中，并计划于 10 月 2 日 Remix Jam 正式发布；RC 意味着功能开发已冻结，团队将专注于修复、安全与文档。
- 📅 首个 RC 发布于 2026 年 8 月 31 日，正式版将于 10 月 2 日 Remix Jam 活动中推出。
- 📦 所有能力汇总为单一 `remix` 包，真正实现“全栈框架、单一依赖”。
- 🗄️ CLI 内置完整数据库工作流：迁移、seed、状态检查、重置、擦除、回滚。
- 🔥 全栈 HMR：服务端模块热更新，并让兼容 UI 组件原地刷新。
- 📂 改进无打包资源服务，支持 JS/CSS/图片/字体/npm 包并内建预加载。
- 🧭 路由更安全快速，类型推断更强，并新增 `router.mount()` 可组合路由。
- 🎨 扩展 UI 库，新增 tabs、toggles、context menus 等内置组件。
- ⚛️ 新增 SPA 支持，将同一套路由、中间件、控制器模型带到纯客户端渲染应用。
- 🔧 新增 `remix.json` 配置与 `remix doctor`，可检查浏览器可访问资源。
- 🤖 基于 Web 原语、类型安全，UI 状态只是 JS 作用域，因此对 AI/agent 编程特别友好。
- 🛡️ 单依赖减少 `package.json` 与供应链攻击面；同时可按需替换（如 Zod/Drizzle）保持可组合与可控。
- ✋ RC 标志功能开发结束，团队转向 bug 修复、安全审计、文档完善并备战 Remix Jam。
- 🧪 可立即试用：`npx remix@next new my-remix-app`。

---

### [发布 Rspack 2.2 - Rspack](https://rspack.rs/blog/announcing-2-2)

**原文标题**: [Announcing Rspack 2.2 - Rspack](https://rspack.rs/blog/announcing-2-2)

Rspack 2.2 正式发布，带来多项性能优化、新特性、生态工具升级与破坏性变更，重点改善构建速度、HMR 效率、模块体积，并扩展平台支持与工具链集成。

- ⚡ 性能提升：包含 30+ 项优化，生产构建时间缩短约 5%，CopyRspackPlugin 提速 3-4 倍，内置 CSS 解析提速约 3 倍，Wasm 体积减少约 1.1 MB。
- 🔄 更优 HMR：避免不必要的 CSS 请求，JS 热更新时间不再随样式表增大而显著增长；同时修复 mini-css-extract-plugin 导致的页面闪烁。
- 🧩 更短模块 ID：新增 `compact-hashed` 策略，在真实项目中使压缩 JS 减小 0.33%、gzip 后减小 0.87%，且保持 ID 稳定。
- 🌐 `import.meta` 增强：支持 `import.meta.rspackPublicPath` 等 Rspack 专属变量，并为 `import.meta.glob` 新增 `caseSensitive` 选项。
- 🎯 Browserslist Baseline 支持：可通过 `target: 'browserslist:baseline widely available'` 定位 Baseline 特性兼容的浏览器版本。
- 🖥️ 更多平台支持：新增 RISC-V 64、ppc64le、s390x 等 Linux 架构的原生绑定，减少对 Wasm 的依赖。
- 🏗️ Rsbuild 2.2：支持导入文本资源、Node.js 构建默认分包（示例项目体积减少 98%）、Solid v2 RC（Rust 编译器快 20 倍）、Octane 模板、动态端口、自定义压缩配置及自定义重启逻辑。
- 🧪 Rstest 更新：支持 Module Federation 远程模块测试、Playwright E2E 测试，并可预打包 jsdom/happy-dom 环境（测试时间最多减少 53%）。
- 🔧 Rslint 增强：内置 500+ 规则，完整覆盖 TypeScript-ESLint 规则集；`defineConfig` 提供完整类型提示，内置常用全局变量，并提供与 ESLint v10 对齐的 JavaScript API。
- 📚 Rslib 进展：0.23.2 支持 TypeScript 7，声明文件生成提速 5-10 倍；1.0 RC 已发布，稳定版即将到来。
- 📖 Rspress：获得 AFDocs 100/100 的 Agent 友好评分，通过多种机制优化 Agent 对文档的发现与理解。
- 🤖 Agent 插件：发布 Rstack Agent Plugin，兼容 GitHub Copilot、Codex、Cursor 等，提供完整 Rstack Skills 支持。
- ⚠️ 升级指南：Wasm 插件因 swc_core 升级到 77 而需重新构建；RSC 插件改为使用 React preinit 加载 CSS，集成方需同步升级 `react-server-dom-rspack` 至 0.1.0。

---

### [](https://webpack.js.org/blog/2026-08-29-webpack-5-110/)

**原文标题**: [Webpack 5.110 | webpack](https://webpack.js.org/blog/2026-08-29-webpack-5-110/)

Webpack 5.110 发布，重点包括超过 30 项内置性能检查、内置 CSS/HTML/JavaScript 压缩能力，以及原生 CSS 管线取代旧 loader 生态。同时带来依赖外部化预设、跨平台规则、Tree Shaking/SSR/HTML/Output/MultiCompiler 改进和大量性能优化与修复。

- 🚀 新增 Performance Hints：内置 30 余项性能检查，可报告重复包、无用模块、加载瀑布流、不匹配规则等问题；默认关闭，用 `performance.all` 或单项开关开启。
- 📊 提示可设为 `hints: "stats"` 只收集到 stats，不产生警告；检查在哈希计算后进行，不影响输出文件哈希。
- 🗜️ 内置压缩器现支持 JavaScript、CSS 和 HTML，并可按资产类型配置；CSS/HTML 压缩默认保守，优先保持语义与浏览器兼容。
- ♻️ 原生 CSS 管线已具备 CSS Modules、解析、HMR、代码分割与压缩能力，`css-loader`、`style-loader`、`mini-css-extract-plugin` 被标记弃用，官方提供 codemod 迁移。
- 📦 新增 `externalsPresets.nodeModules`，可智能外部化 `node_modules`；externals 还支持 `sideEffects: false`，帮助摇树优化。
- 🪟 新增 `Rule.glob` 和 `Rule.descriptionRelativePath`，解决正则路径在 Windows 上失效的问题；`performance.osDependentRules` 可检测此类规则。
- 🌲 Tree Shaking 与 Scope Hoisting 增强：`require()` 解构、`module.exports` 对象、命名空间导出等可被正确摇除，依赖顺序使模块哈希更稳定。
- 🖥️ SSR 支持内置 CSS：样式会写入全局注册表 `__webpack_css_server_styles__`，方便服务端渲染时收集并注入。
- 📝 HTML 改进：热更新可直接修补 `<head>`；入口的 `html` 选项可覆盖全局 `output.html`；解析器更贴近 HTML 规范。
- 🏗️ Output/Library 更新：新增 UMD AMD 容器、资源提示去重、`[containedpath]`/`[containedfile]` 占位符，并改善 ESM 输出与库构建 source map 行为。
- 🔄 MultiCompiler 优化：`done` 钩子能识别实际运行的编译单元，新增 `shutdown` 钩子，共享 watcher 并增强崩溃恢复能力。
- 👀 其他改进：失败请求会提供名称或大小写建议，新增 `stats.hints` 和 `hintsCount`，支持更多 `output.environment` 特性与 UNC 路径。
- 🔧 性能与 Bug 修复：用内置轻量 scope 分析器替换 `eslint-scope`，按需加载运行时模块，解析和代码生成更快，同时修复大量已知问题。

---

### [](https://nodejs.org/en/blog/release/v26.8.0)

**原文标题**: [Node.js — Node.js 26.8.0 (Current)](https://nodejs.org/en/blog/release/v26.8.0)

Node.js 26.8.0（Current 版本）于 2026-08-26 发布，带来了多项新功能与改进，涵盖加密、SQLite、性能优化、开发者工具等领域，并更新了相关依赖与下游工具链。

- 🚀 benchmark：新增 `--analyze` 模式，便于比较分析性能数据。
- 🔐 crypto：更新根证书至 NSS 3.126，并启用 SIV 与 GCM-SIV 加密模式。
- 🩺 diagnostics_channel：将 TracingChannel 标记为稳定特性。
- 📊 直方图：改进 histogram 实现，并在 perf_hooks 中加入统计假设检验功能。
- ⚡ net：提升 net.BlockList 的性能表现。
- 🎨 REPL：新增基础语法高亮功能。
- 🗄️ SQLite：为 StatementSync 增加 `close()` 与 `Symbol.dispose()` 方法，并加强多项安全与健壮性检查。
- 🧩 util：新增非抛出式 `MIMEType.parse()` 方法。
- 📦 zlib：新增 ZipEntry、ZipFile 和 ZipBuffer 等 ZIP 处理支持。
- 🛠️ 其他修复：涵盖 fs、http、stream、test_runner、TLS、URL 等多个模块的缺陷修复与性能优化。
- 📥 提供 Windows、macOS、Linux、AIX 等多平台安装包与二进制文件，附 SHA256 校验值。

---

### [](https://github.com/jestjs/jest/releases/tag/v30.5.0)

**原文标题**: [Release v30.5.0 · jestjs/jest · GitHub](https://github.com/jestjs/jest/releases/tag/v30.5.0)

Jest v30.5.0 是一次大型发布，重点更新了 jest-runtime、jest-resolve 与 jest-haste-map，引入新 mock 配置、describe 级重试、重构文件监听、大量 ESM 互操作修复、性能优化及依赖升级。
- ✨ 新增 `mockFn.whenCalledWith(...args)`，可按不同参数列表配置返回值，支持非对称匹配器和链式调用。
- 🔁 `jest.retryTimes(n, { entireDescribe: true })` 支持重试整个 describe 块（含钩子与嵌套测试）。
- 👀 将非 watchman 的 `jest-haste-map` 监听与爬虫重写为 `@parcel/watcher` + `fdir`，修复 Windows 锁定文件、watchman 故障等健壮性问题。
- 📦 依赖更新：`babel-plugin-istanbul` v8、`glob` v13；用 `@jest/source-map` 替代 `source-map-support`，修复内存泄漏并保留 source map 正确性。
- ⚡ 性能优化：模块解析暖成本约降至 1/3；减少 `jest-runtime` 每 require 开销；快照相关依赖懒加载；watchman socket 缓存避免热启动额外进程。
- 🆕 新 API 与能力：快照失败暴露 `matcherResult.snapshotPath`；`--collectTests` 支持展开 each 及汇总报告；`AggregateError` 嵌套错误可读渲染且进入 JSON 输出。
- 🇪🇺 ESM 大量改进：Node 24.9+ 下 automock/手动 `__mocks__` 支持同步 ESM；补全 `unstable_mockModule` 作用域与异步工厂行为；`require(esm)`、循环依赖、`import.meta` 等更贴近 Node。
- 🧭 解析器增强：默认解析器尊重 `--preserve-symlinks`；`moduleNameMapper` 同时匹配 `fs` 与 `node:fs`；支持将自定义 resolver 写成 ES module。
- 🐛 另有约 60 项修复，涉及 jest-circus、haste-map、config、mock、transform 缓存等。
- 📚 维护与文档：记录与 Node 模块系统的有意差异，更新 React Native 教程，弃用说明等。

---

