### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

Meticulous 是一款自动化、全面且确定性的测试工具，能让开发者无需手动编写、修复或维护测试用例，即可快速、可靠地交付代码。

- 🚀 **零开发者投入的全面验证**：自动监控开发环境中的用户交互，生成覆盖所有代码分支、用户流程和边缘情况的端到端测试套件。
- 🤖 **AI 驱动的持续进化测试**：AI 引擎根据应用变化自动增删测试，确保测试套件始终最新且完整，无需人工干预。
- 🛡️ **从底层消除测试不稳定**：基于 Chromium 的确定性调度引擎，从根本上消除测试不稳定（flakes），并实现闪电般的测试速度。
- ⚡ **极速大规模测试**：测试在计算集群上高度并行化，可在 120 秒内完成数千个屏幕的测试。
- 🔌 **无缝集成与灵活使用**：支持 NextJS、React、Vue 等主流框架，可通过脚本标签或 SDK 集成；可补充或替代现有测试套件。
- 🏢 **被行业领导者信赖**：已获 Dropbox、Notion、Engine 等超 100 家组织采用，开发者反馈“爱不释手，无法想象没有它”。
- 🔒 **安全与合规**：提供集成与安全文档，确保企业级使用安全。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

该平台提供零开发工作量的自动化、穷尽且确定性的测试方案，专为复杂代码库设计，帮助开发者快速交付可靠代码。

- 🚀 **零开发工作量**：无需编写、修复或维护测试，测试套件随应用自动演进。
- 🤖 **AI 驱动测试生成**：通过记录日常开发交互，AI 引擎自动生成覆盖所有代码分支和用户流程的测试。
- 🔍 **穷尽性验证**：测试覆盖每一行代码、每个用户流程和边缘情况，确保无死角。
- ⚡ **闪电般速度**：测试在计算集群上高度并行化，1000+ 屏幕测试结果可在 120 秒内返回。
- 🛡️ **消除所有不稳定测试**：基于 Chromium 的确定性调度引擎，从根源上消除测试不稳定性。
- 🔄 **无缝集成**：支持 NextJS、React、Vue、Angular 等主流框架，只需添加脚本标签即可开始。
- 💼 **企业级信任**：被 Dropbox、Notion 等 100+ 组织采用，开发者反馈“无法想象没有它工作”。
- 🧪 **灵活使用**：可作为现有测试套件的补充或完全替代，无需特殊测试账户或模拟数据。

---

### [react/react-compiler | Oxlint | JavaScript 氧化编译器](https://oxc.rs/docs/guide/usage/linter/rules/react/react-compiler.html)

**原文标题**: [react/react-compiler | Oxlint | The JavaScript Oxidation Compiler](https://oxc.rs/docs/guide/usage/linter/rules/react/react-compiler.html)

此规则在 lint 模式下运行 React 编译器的分析，并报告违反 React 规则的代码。

- 🔍 检测违反 React 规则的行为，如条件调用 hook、渲染时调用 setState、读取 refs 或修改 props/state
- ⚠️ 该规则仍处于实验阶段，未来会更好地适配 Oxlint
- 🚫 违反 React 规则的代码可能导致运行时不可预测的行为（如 UI 过时、无限重渲染、状态丢失）
- ✅ 遵循规则可保持组件正确性，并允许自动记忆优化
- 📝 支持配置`reportAllBailouts`选项（默认 false），可报告编译器跳过优化但未发现违规的情况
- ⚙️ 可通过配置文件或 CLI 启用，示例配置：`"react/react-compiler": "error"`
- 📅 该规则自 v1.70.0 版本起可用

---

### [杂务：将 oxlint 升级至 1.70.0 并启用 react/react-compiler 规则 —— 由 reidbarber 提交 · 拉取请求 #10203 · adobe/react-spectrum · GitHub](https://github.com/adobe/react-spectrum/pull/10203)

**原文标题**: [chore: upgrade oxlint to 1.70.0 and enable react/react-compiler rule by reidbarber · Pull Request #10203 · adobe/react-spectrum · GitHub](https://github.com/adobe/react-spectrum/pull/10203)

此 PR 将 oxlint 升级至 1.70.0 并启用原生 React 编译器规则，性能提升显著，同时检测出更多违规问题。

- 🚀 将 oxlint 从 1.63.0 升级至 1.70.0，启用原生 React 编译器规则，性能提升 5.8 倍（墙钟时间从 18.5 秒降至 3.2 秒）
- 🔍 原生规则比 JS 插件检测出更多违规（总计 585 个 vs 43 个），包括引用访问、不可变性、钩子规则等问题
- 📊 违规分类统计：引用访问 197 个、不可变性 150 个、钩子规则 85 个、大写调用 83 个、备忘录依赖 27 个等
- 🛠️ 当前已抑制所有违规，但团队可决定是否修复部分问题
- ✅ 已完成 PR 检查清单，包括链接相关 Issue、更新测试和文档等
- 👥 获得至少 2 位审核者批准（snowystinger 已批准），可合并至主分支

---

### [杂务 (代码检查)：用 oxlint 替换 eslint 的 js 插件，由 stipsan 提交 · 拉取请求 #13114 · sanity-io/sanity · GitHub](https://github.com/sanity-io/sanity/pull/13114)

**原文标题**: [chore(lint): replace eslint with oxlint jsplugins by stipsan · Pull Request #13114 · sanity-io/sanity · GitHub](https://github.com/sanity-io/sanity/pull/13114)

Sanity 仓库将 ESLint 完全替换为 oxlint，作为统一的代码检查工具，并升级了相关工具链。

- 🔧 **工具链升级**：将 oxlint 升级到 1.70.0，oxfmt 升级到 0.55.0，并移除了 ESLint 及其所有相关配置和依赖。
- 🚀 **规则迁移**：将 ESLint 的所有原生规则（如 `react/react-compiler`、`import/*`、`typescript/*`、`unicorn/*`）以及通过 jsPlugins 支持的插件（如 `tsdoc`、`i18next`、`boundaries`、`testing-library`）全部迁移至 oxlint。
- ⚡ **性能提升**：单一 oxlint 运行时间约 21.5 秒，相比之前 ESLint + oxlint 的 102 秒，速度提升约 4.7 倍。
- 🗑️ **配置清理**：移除了 28 个 `eslint.config.mjs` 文件、`@repo/eslint-config` 包、`.prettierignore` 以及所有 Prettier 相关步骤，统一使用 oxfmt 进行格式化。
- ♻️ **指令重命名**：将代码中 434 处 `eslint-disable`/`eslint-enable` 注释重命名为 `oxlint-disable`/`oxlint-enable`，并移除了 278 个未使用的禁用指令。
- 🧠 **类型感知检查**：在 `.oxlintrc.json` 中启用 `options.typeAware: true`，实现类型感知的代码检查。
- 🏗️ **Turbo 解耦**：将 `check:format`、`check:oxlint` 等任务从 Turbo 中移除，作为普通 pnpm 脚本直接运行，简化了 CI 流程。
- 🧪 **边界配置升级**：将 `eslint-plugin-boundaries` 配置迁移至 v6 版本的 `boundaries/dependencies` 规则，消除了弃用警告。

---

### [特性：为 rolldown 和 Vite 用户暴露 React 编译器选项 —— Boshen · 拉取请求 #9801 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/pull/9801)

**原文标题**: [feat: expose React Compiler options for rolldown and Vite users by Boshen · Pull Request #9801 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/pull/9801)

Rolldown 项目合并了 PR #9801，将实验性的 React Compiler 选项暴露给 Rolldown 和 Vite 用户，允许他们选择使用编译器记忆化功能。

- 🚀 新增`reactCompiler`选项，可通过 Rolldown 的`transform.reactCompiler`、Vite 的`viteTransformPlugin`的`transformOptions.reactCompiler`以及独立的`transform()`/`transformSync()` API 进行配置
- ⚙️ `reactCompiler`接受`true`（使用默认选项）或`ReactCompilerOptions`对象，作为 oxc 转换器的第一遍处理，在 AST 纯净状态下运行，早于 TS/JSX 降级
- 💡 实现上启用了 oxc 依赖的`react_compiler`特性，并将解析后的`PluginOptions`通过`BundlerTransformOptions`/`EnhancedTransformOptions`传递到`oxc::transformer::TransformOptions`中
- 📦 解析后的`PluginOptions`被装箱为`Option<Box<PluginOptions>>`（约 700 字节且几乎总是`None`），避免膨胀频繁克隆的每文件结构体
- 🧪 测试覆盖所有配置路径：bundler fixture、viteTransformPlugin fixture 和独立 transform()，包括默认关闭、`true`和选项对象（如`target`选择运行时、`compilationMode: 'annotation'`通过`"use memo"`选择加入）

---

### [feat(es/react-compiler): 由 magic-akari 添加 React 编译器 · 拉取请求 #11917 · swc-project/swc · GitHub](https://github.com/swc-project/swc/pull/11917)

**原文标题**: [feat(es/react-compiler): Add React Compiler by magic-akari · Pull Request #11917 · swc-project/swc · GitHub](https://github.com/swc-project/swc/pull/11917)

SWC 项目合并了 React 编译器的实验性支持，通过 Rust 桥接实现了 SWC 与 React 编译器 AST/作用域的转换。

- 🚀 新增 `swc_ecma_react_compiler` 桥接，支持 SWC 与 React 编译器 AST/作用域转换
- ⚙️ 添加 `.swcrc` 配置中的 `jsc.transform.reactCompiler` 选项
- 📦 引入 JS/WASM 选项类型，并移植了上游 SWC 集成测试
- 🧩 修复了静态块变量作用域、JSX 内建标签引用和默认导出绑定等关键问题
- 📈 二进制体积增加约 5MB，可通过优化 Rust 结构体返回而非 JSON 序列化来改善
- 🔄 使用 `oxc-project/forked-react-compiler` 进行测试，待官方 Rust crate 发布后替换临时依赖

---

### [feat: 由 CPunisher 提交的 PR #14435 · web-infra-dev/rspack · GitHub，升级 swc 以支持 React 编译器](https://github.com/web-infra-dev/rspack/pull/14435)

**原文标题**: [feat: bump swc to support react compiler by CPunisher · Pull Request #14435 · web-infra-dev/rspack · GitHub](https://github.com/web-infra-dev/rspack/pull/14435)

Rspack 通过 PR #14435 合并了一项重要功能：升级 SWC 以支持 React 编译器。

- 🚀 升级 SWC 相关依赖和 `@swc/types`，使 `builtin:swc-loader` 支持 `jsc.transform.reactCompiler` 配置。
- 🧪 新增 `builtin:swc-loader/react-compiler` 测试用例，验证 React 编译器输出。
- 📝 更新中英文 React 文档，将 `builtin:swc-loader` 设为首选 React 编译器方案，Babel 插件作为备选。
- 🔗 文档链接至 React 编译器官方配置文档，提供 `compilationMode` 等高级选项说明。
- 📦 二进制体积增加 4.97MB（约 7.90%），但性能测试显示无显著变化。

---

### [Turbopack: 通过 wbinnssmith 添加实验性 React 编译器支持 · 拉取请求 #94573 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/94573)

**原文标题**: [Turbopack: add experimental React compiler support by wbinnssmith · Pull Request #94573 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/94573)

Turbopack 新增实验性 React 编译器支持，通过配置选项启用，仅作用于客户端代码，并直接操作 SWC AST 避免重复解析。

- 🚀 新增 `experimental.rustReactCompiler` 配置选项，需与 `config.reactCompiler` 配合使用
- 🎯 编译器仅作用于客户端代码（包括 SSR），不处理 RSC
- ⚡ 直接在 Turbopack 的 SWC AST 上运行编译器，无需生成和重新解析
- 🔧 通过传递原始源代码到转换过程，实现高效编译
- ✅ 已合并到 canary 分支，通过 222/226 项检查

---

### [没人告诉你的创业营销真相](https://newsletter.posthog.com/p/the-stuff-nobody-tells-you-about?r=5t1b8o)

**原文标题**: [The stuff nobody tells you about startup marketing](https://newsletter.posthog.com/p/the-stuff-nobody-tells-you-about?r=5t1b8o)

### 概述总结
初创公司营销的核心在于真实、专注和实验精神，而非复杂策略或外包。

- 🚀 **营销早已开始**：你做的很多事（如 HN 发帖、公开手册）本身就是营销，只需弥合产品与用户之间的信息差。
- 🎯 **深度优于广度**：集中精力做好一个有效渠道（如持续写博客），而非尝试多个半途而废的渠道。
- 🔗 **匹配销售模式**：产品驱动增长（PLG）靠社区和口碑，销售驱动增长（SLG）靠定向接触和创始人网络，但初期避免 SEO。
- 🧪 **实验思维**：每次营销前明确“成功”的清晰标准（非数字目标），6 周内判断效果，失败也是收获。
- 📊 **归因不可信**：用户来源复杂，用注册时的“你从哪知道我们？”文本框获取真实信号，而非复杂归因模型。
- 🚫 **勿外包给机构**：早期营销需要创始人亲自理解用户和定位，外包会导致反馈慢且内容平庸。
- 👤 **首次招聘时机**：有真实用户、推荐者和付费用户后再招人，首选能写、懂漏斗、会沟通的通用型人才。

---

### [无需 JavaScript 的本地化时间格式化 · Issue #12591 · whatwg/html · GitHub](https://github.com/whatwg/html/issues/12591)

**原文标题**: [Localized time formatting without JavaScript · Issue #12591 · whatwg/html · GitHub](https://github.com/whatwg/html/issues/12591)

该提案旨在扩展 HTML `<time>`元素，使其无需 JavaScript 即可在服务端渲染的场景下，根据用户的时区和语言偏好自动格式化日期和时间。

- 🌐 **解决核心问题**：服务端渲染的 HTML 无法获知用户时区，导致无法正确显示绝对时间。现有方案（如相对时间、固定时区、IP 猜测或 JavaScript）均有缺陷。
- 🕰️ **核心解决方案**：扩展`<time>`元素，新增`format`属性（可选值`"date"`、`"time"`、`"datetime"`），通过 UA Shadow DOM 渲染格式化后的时间文本，并保留原始内容作为降级回退。
- ⚙️ **丰富的格式化属性**：提供`datefields`、`datelength`、`timeprecision`、`timezonestyle`、`hour12`、`calendar`和`timezone`等属性，允许精细控制日期和时间的显示方式。
- 🌍 **语言与时区自动检测**：通过 DOM 遍历查找最近的`lang`属性来确定用户语言；`timezone`属性可指定时区，或使用 UA 当前时区，或从`Temporal.ZonedDateTime`中提取。
- 🧩 **基于 ECMA-402 的格式化**：使用`Intl.DateTimeFormat`进行格式化，并将结果转换为 Shadow DOM 中的`<span>`元素，支持通过 CSS 伪元素选择器对日期/时间的不同部分（如星期、月份）进行单独样式化。
- 🏗️ **技术实现考量**：采用 Shadow DOM 而非 CSS `content`，以简化文本选择并支持部分样式化；属性命名参考 Unicode MessageFormat 2 标准。
- 🚧 **当前状态**：该提案处于“孵化”阶段（Stage 1），需要具体的实施方案、浏览器厂商的兴趣以及测试支持。

---

### [React 19 升级在 Gutenberg 中暂时回滚 – 构建 WordPress 核心](https://make.wordpress.org/core/2026/06/05/react-19-upgrade-temporarily-reverted-in-gutenberg/)

**原文标题**: [React 19 upgrade temporarily reverted in Gutenberg – Make WordPress Core](https://make.wordpress.org/core/2026/06/05/react-19-upgrade-temporarily-reverted-in-gutenberg/)

WordPress 和 Gutenberg 的 React 19 升级因兼容性问题被临时回退到 React 18，团队计划制定更稳健的升级策略。
- 🔄 React 19 升级在 Gutenberg 23.3.0 发布后，因与基于 React 18 的旧插件不兼容（如 `react/jsx-runtime` 对象形状差异导致崩溃）而回退。
- 🛠️ 问题根源在于插件自带旧版运行时，React 19 会主动检查并拒绝 React 18 生成的元素，尽管 API 本身变化不大。
- 📋 团队将设计更渐进的升级策略：包括实验性功能开关切换 React 18/19，以及为已发布插件提供兼容层。
- ⏸️ 回退版本已在 Gutenberg 23.3.2 中发布，为团队争取时间重新规划和测试升级方案。
- 🎯 仍承诺在 WordPress 7.1 中完成 React 19 升级，但需更谨慎的过渡。

---

### [TSRX](https://tsrx.dev/blog/rethinking-tsrx)

**原文标题**: [TSRX](https://tsrx.dev/blog/rethinking-tsrx)

TSRX 重新回归 JSX 语法，让专用语法保持显眼，不再伪装成普通 JavaScript。

- 🔄 **回归 JSX 本质**：静态文本现在直接使用 JSX 文本，无需额外引号或 `{''}`，与 JSX 用户预期一致。
- 💬 **支持 JS 注释**：允许在 JSX 子元素中使用 JavaScript 单行和多行注释，不会渲染为文本。
- 📦 **新增 `@{...}` 语句容器**：可包含 JavaScript 语句并以 JSX 模板结尾，作为表达式使用，支持变量赋值和组件体。
- 🚦 **显式 JSX 控制流**：使用 `@if`、`@for`、`@switch`、`@try` 等前缀，明确区分模板逻辑与普通 JavaScript，避免混淆。
- 🧩 **控制流可赋值**：JSX 控制流可直接赋给变量，无需包装成辅助函数，类型注解为 `JSX.Element`。
- 🎯 **保持 React/Preact hooks 显式**：不自动将条件 hooks 移入子组件，要求分支拥有 hook 状态的组件显式命名。
- 🛠️ **早期返回支持**：在 `@{...}` 组件体中允许顶层早期返回，行为与普通组件守卫返回一致。
- ✅ **进入 Beta 阶段**：核心语法已稳定，未来聚焦编译器、运行时、编辑器工具和文档的完善。

---

### [TanStack Start：Next.js 开发者的心智模型 | Adarsha Acharya](https://www.adarsha.dev/blog/tanstack-mental-model-for-nextjs-developers)

**原文标题**: [TanStack Start: A Mental Model for Next.js Developers | Adarsha Acharya](https://www.adarsha.dev/blog/tanstack-mental-model-for-nextjs-developers)

本篇文章从 Next.js 开发者的视角，深入解析 TanStack Start 的核心设计理念与关键特性，包括其以路由优先的架构、明确的服务器边界、类型安全的路由、缓存策略、渲染模式及服务端函数。

- 🧭 路由优先架构：TanStack Start 强调路由作为应用的核心，与 Next.js 的文件系统路由不同，它采用更灵活的路由配置方式。
- 🔒 明确的服务器边界：通过显式标记服务器端代码，避免混淆客户端与服务器逻辑，提升安全性与可维护性。
- 🔗 类型安全路由：提供强类型路由支持，减少因路径错误或参数不匹配导致的运行时问题。
- 💾 智能缓存策略：内置高效的缓存机制，优化数据加载性能，减少不必要的网络请求。
- 🖥️ 灵活渲染模式：支持静态生成（SSG）、服务端渲染（SSR）及客户端渲染（CSR），开发者可根据需求选择。
- ⚙️ 服务端函数：允许在客户端直接调用服务端函数，简化数据获取与业务逻辑的交互流程。

---

### [React 及同类框架中的模块系统依赖注入](https://www.jayfreestone.com/writing/module-level-dependency-injection-react/)

**原文标题**: [Module System Dependency Injection in React & Friends](https://www.jayfreestone.com/writing/module-level-dependency-injection-react/)

### 概述总结
本文探讨了在 React 及相关框架中，使用模块系统进行全局依赖注入（DI）的实践与局限性，并对比了静态 DI、运行时 DI 及编译时 DI 的优劣。

- 📦 **依赖注入的两种形式**：静态 DI 基于配置一次性绑定依赖，适用于环境切换；运行时 DI 根据运行时数据（如用户、租户）动态选择依赖，常见于 React Context 或服务定位器模式。
- 🧩 **模块系统 DI 的优势**：通过 Node.js 条件导出或子路径导入，实现编译时依赖替换，避免加载无用代码，提升性能（如`#analytics`在不同条件下解析不同实现）。
- ⚠️ **模块系统 DI 的缺陷**：无法在测试中内联替换依赖（需模块级 mock），且同一应用内无法同时使用多个版本依赖，削弱了灵活性和类型安全。
- 🛠️ **元框架中的 DI 实践**：React Router 和 Tanstack Start 支持中间件和服务器上下文实现 DI；Next.js 社区倾向模块系统 DI，但缺乏官方服务器上下文支持。
- 🔧 **推荐方案（穷人的 DI）**：将模块系统作为静态组合根工具，业务逻辑通过函数/工厂接受抽象接口，便于单元测试；E2E 测试中使用编译时 DI 替换基础设施（如分析客户端），保持显式依赖路径。

---

### [构建 LLM 安全设计系统 | Polar](https://polar.sh/blog/orbit-llm-safe-design-system)

**原文标题**: [Building an LLM safe design system | Polar](https://polar.sh/blog/orbit-llm-safe-design-system)

### 概述总结
Polar 团队正在构建名为 Orbit 的 LLM 安全设计系统，核心思路是通过类型系统和 CI 规则，将设计决策转化为代码中唯一可表达的选择，从而解决 LLM 生成代码时的风格漂移问题。

- 🎯 **核心问题**：LLM 能流畅编写 CSS/Tailwind 类，但会无意识地选择非品牌标准值（如不同灰色），导致界面风格逐渐偏离
- 🚫 **字符串风险**：Tailwind 类作为字符串给 LLM 无限犯错空间（如 p-4/p-5/p-[17px]），所有值语法正确但偏离系统规范
- 🧠 **意图驱动**：Orbit 令牌按意图命名（如`background-card`而非`bg-gray-100`），让 LLM 选择已定义的决策而非猜测数值
- 🔒 **CI 契约**：关键规则编码为 ESLint 规则在 CI 中执行，绿色 PR 即安全合并，取代易被忽略的文档建议
- 📦 **单一容器**：用类型化`<Box>`组件替代裸`<div>`，通过`as`属性保留语义（如`<Box as="nav">`），消除未约束的字符串入口
- 🌓 **内置暗色模式**：使用 CSS `light-dark()`函数让颜色值同时包含明暗主题，LLM 无法忘记暗色模式
- ✅ **初步成效**：代码审查从检查样式偏差转向行为与布局，LLM 被限制在正确的设计词汇表中
- ⚠️ **持续挑战**：令牌集需不断扩展满足实际 UI 需求，遗留 Tailwind 代码逐步迁移，需审计每个转义出口

---

### [Certificates.dev 免费周末 | 免费获取 React 开发者认证培训 - Certificates.dev](https://certificates.dev/react/free-weekend?utm_source=twir&utm_medium=newsletter&utm_campaign=react_free_weekend_june_2026&friend=TWIR)

**原文标题**: [Certificates.dev Free Weekend | Free access to React Developer Certification Training - Certificates.dev](https://certificates.dev/react/free-weekend?utm_source=twir&utm_medium=newsletter&utm_campaign=react_free_weekend_june_2026&friend=TWIR)

概述总结
- 🎓 提供 React 中级认证备考培训，限时 48 小时免费访问全部 9 章内容、13 个编码挑战、12 个测验和模拟考试
- 📅 活动时间为 6 月 27 日至 28 日，需提前预约席位
- 🏢 已为 680 多家公司认证开发者，考试由行业领袖（如 React 专家、微软 MVP）合作设计
- 📚 培训内容涵盖 JavaScript 基础、JSX 与组件、事件处理与状态管理、高级 Hooks 及导航等核心主题
- 💻 包含动手项目挑战：构建电影评分应用，逐步实现组件、状态管理、CRUD 操作和 TypeScript 集成
- 🎯 提供模拟考试（10 道选择题 +1 个编码挑战，限时 1 小时）以评估技能水平
- 🚫 不包含正式考试，考试券需单独购买，目前有黑五早鸟优惠（60% 折扣 + 赠送初级认证和 AI 课程）
- 🗳 邀请用户投票选择希望获得的其他框架/技术认证

---

### [氢能更新 | 氢能开发者预览](https://hydrogen.shopify.dev/update/hydrogen-developer-preview)

**原文标题**: [Hydrogen Update | Hydrogen developer preview](https://hydrogen.shopify.dev/update/hydrogen-developer-preview)

Shopify 与 Vercel 合作发布了 Hydrogen 开发者预览版，将其从框架重构为与框架无关、运行时无关且为 AI 代理设计的工具包。核心是纯 JavaScript，提供 Shopify 商店前端基础组件，支持 Next.js、SvelteKit 等多种框架，可在 Oxygen、Vercel、Cloudflare Workers 等环境运行。包含类型化的 Storefront API 客户端、购物车、产品集合等原语，以及内置的代理技能，帮助 AI 代理构建商店前端。

- 🛠️ **核心重构为工具包**：Hydrogen 从完整的 Remix 框架转变为框架无关的工具包，提供纯 JavaScript 核心和薄绑定层，开发者可自由选择框架和运行时。
- 🌐 **多框架与运行时支持**：React 绑定已可用，Vue、Svelte、Remix 3 绑定即将推出；支持 Oxygen、Vercel、Cloudflare Workers、Node、Deno 等运行环境。
- 🤖 **为 AI 代理优化**：内置代理技能（agent skills），版本化且随包安装，指导 AI 代理正确设置 Storefront API、购物车、分析等功能，避免常见错误。
- 🛒 **核心商务原语**：提供类型化的 Storefront API 客户端（gql() 查询自动类型推断）、购物车、产品/集合原语、货币格式化、Shop Pay、第一方分析及同意处理。
- ⚡ **服务端驱动与优化**：购物车和请求处理在客户端 JavaScript 加载前即可工作，支持乐观 UI 更新；自动处理购物车变更、重定向、分析令牌和缓存头。
- 🔧 **快速开始流程**：使用框架 CLI 创建项目后，运行`npx @shopify/hydrogen@preview setup`安装，然后让 AI 代理通过提示词自动搭建商店前端。
- 📋 **开发者预览状态**：API 可能变化，路线图包括更多框架绑定、客户账户和预测搜索；当前 Hydrogen 版本继续受支持，未来会提供迁移指南。

---

### [更新日志.md](https://raw.githubusercontent.com/facebook/stylex/main/CHANGELOG.md)

**原文标题**: [CHANGELOG.md](https://raw.githubusercontent.com/facebook/stylex/main/CHANGELOG.md)

## 0.19.0 版本更新摘要
- 🆕 新增 `@stylexjs/atoms` 包，支持内联原子样式
- 🔧 兼容 ESLint 10
- 🛠️ 为 `legacy-expand-shorthands` 添加 `gap` 自动修复，并在 `valid-shorthands` 中跳过单值 `gap` 和 `flex`
- 📝 扩展 `textWrap` 验证，支持 `pretty` 和 `stable` 值
- 🐛 修复 `sx` 属性运行时 stylex 导入注入问题
- 🔄 修复伪元素与伪类选择器排序问题
- 📂 修复别名主题文件解析为绝对路径
- 🔍 修复 `sort-keys` 自动修复排序
- 🧮 修复样式值解析器中 `and` 链的媒体类型括号化问题

---

### [GitHub Actions 设置 - 文档 | React Doctor](https://www.react.doctor/docs/ci-and-prs/github-actions-setup)

**原文标题**: [GitHub Actions Setup - Docs | React Doctor](https://www.react.doctor/docs/ci-and-prs/github-actions-setup)

## 概述摘要
本文档详细说明了如何在 GitHub 仓库中设置 React Doctor 的 GitHub Actions 工作流，以便自动审查每次拉取请求中的 React 代码问题。

- 🔧 **工作流配置**：创建`.github/workflows/react-doctor.yml`文件，使用`millionco/react-doctor@v2` Action，并设置`fetch-depth: 0`以获取完整 git 历史。
- 📝 **权限设置**：需要`pull-requests: write`、`issues: write`、`statuses: write`和`contents: read`权限，用于发布评论和设置状态。
- 🚫 **约束条件**：不添加安装、构建、矩阵、缓存步骤，仅创建或更新工作流文件，不修改其他文件。
- 📊 **PR 反馈机制**：在 PR 中创建粘性摘要评论、内联审查评论，并在 CI 日志中输出完整结果。
- ⚙️ **配置选项**：支持`blocking`（阻止级别）、`scope`（扫描范围）、`directory`（子目录）、`project`（项目选择）等输入参数。
- 🏗️ **Monorepo 支持**：通过`directory`和`project`参数指定子目录或项目，默认扫描所有 React 项目。
- 🔄 **运行行为**：PR 运行时报告新问题并可能失败；推送到`main`时仅记录分数，不发表评论或失败。
- 🛠️ **故障排除**：常见问题包括缺少`fetch-depth: 0`、权限不足、分支保护规则未设置等。

---

### [发布 v4.0.0 · airbnb/visx · GitHub](https://github.com/airbnb/visx/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · airbnb/visx · GitHub](https://github.com/airbnb/visx/releases/tag/v4.0.0)

visx v4.0.0 正式发布，这是一个重大版本更新，带来了多项增强、修复和破坏性变更。

- 🚀 新增对 React 19 的支持，并升级了 d3-shape、d3-path 等核心依赖
- 🐛 修复了堆叠条形图、响应式尺寸、工具提示等多个 Bug
- 💥 破坏性变更：要求最低 React 18 或 19，移除 prop-types，升级至 Yarn 4
- 📝 更新了 README 文档，移除了 Remix 按钮引用
- 🏠 内部重构：迁移至 Vitest、jsdom，升级 Node 至 22、Next 至 14
- 🔧 优化了发布流程，修复了 GitHub Actions 工作流和类型错误
- 🎉 感谢 11 位贡献者的共同努力

---

### [发布 v4.0.475 · remotion-dev/remotion · GitHub](https://github.com/remotion-dev/remotion/releases/v4.0.475)

**原文标题**: [Release v4.0.475 · remotion-dev/remotion · GitHub](https://github.com/remotion-dev/remotion/releases/v4.0.475)

Remotion v4.0.475 版本发布，重点引入了 Studio 交互功能，允许用户直接在画布上拖拽和编辑元素。

- 🎨 **Studio 交互功能上线**：现在可以在 Remotion Studio 中直接点击并拖拽画布上的元素，实现交互式代码修改。
- 🖱️ **拖拽操作多样化**：支持拖拽效果、视频、音频和图片到画布上，以及拖拽时间轴中的图层。
- 🔑 **关键帧设置**：可为 CSS、组件属性和效果属性设置关键帧，增强动画控制。
- 🧩 **内置交互组件**：使用 `<Img>`、`<Video>`、`<Sequence>` 等组件可自动获得交互能力。
- 🔄 **HTML 元素交互化**：通过 `<Interactive.Div>` 将普通 HTML 元素转为可交互。
- 🚫 **交互退出选项**：使用“轮廓切换”隐藏所有轮廓，或设置 `showInTimeline={false}` 排除交互。
- 🛠️ **多项 Studio 改进**：包括时间轴样式优化、变换原点编辑、关键帧缓动控制、选框选择等。
- 📦 **其他更新**：支持 `transform-origin` 关键词、`interpolateColors` 添加缓动、媒体组件防止初始双重跳转等。
- 📚 **文档优化**：升级 Docusaurus 和 Rspack，减少构建内存占用。
- 🔧 **内部改进**：实验性高 DPI 屏幕录制器。

---

### [发布 rsbuild-plugin-react-router@0.2.0 · rstackjs/rsbuild-plugin-react-router · GitHub](https://github.com/rstackjs/rsbuild-plugin-react-router/releases/tag/rsbuild-plugin-react-router%400.2.0)

**原文标题**: [Release rsbuild-plugin-react-router@0.2.0 · rstackjs/rsbuild-plugin-react-router · GitHub](https://github.com/rstackjs/rsbuild-plugin-react-router/releases/tag/rsbuild-plugin-react-router%400.2.0)

概述摘要  
- 🎉 发布 rsbuild-plugin-react-router@0.2.0 版本  
- 🔧 新增对 Rsbuild 2 的支持  
- 🛠️ 更新 Rsbuild/Rspack 工具链  
- 📦 版本基于 1 个提交至 main 分支  
- ⚠️ 加载页面时出现错误，建议重新加载

---

### [GitHub - vadimdemedes/ink: 🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps · GitHub](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的 CLI 构建工具，允许开发者使用组件化方式构建交互式命令行应用，并支持 Flexbox 布局。

- 🖥️ **React 驱动 CLI**：Ink 将 React 的组件化开发体验带入命令行，支持所有 React 特性，如 Hooks、状态管理和生命周期。
- 📦 **Flexbox 布局**：基于 Yoga 引擎，支持 CSS 类似的 Flexbox 属性（如 `flexDirection`、`alignItems`、`justifyContent`），方便构建复杂终端界面。
- 🎨 **丰富的组件库**：内置 `<Text>`（文本样式）、`<Box>`（布局容器）、`<Newline>`、`<Spacer>`、`<Static>`（静态输出）和 `<Transform>`（文本转换）等组件。
- 🔧 **强大的 Hooks**：提供 `useInput`（键盘输入）、`useFocus`（焦点管理）、`useApp`（应用生命周期）、`useAnimation`（动画驱动）等 Hooks，简化交互逻辑开发。
- 🧪 **测试与调试**：支持 `ink-testing-library` 进行组件测试，集成 React Devtools 实时调试组件树。
- ♿ **无障碍支持**：内置屏幕阅读器支持，可通过 `aria-*` 属性提供语义化输出，提升 CLI 可访问性。
- 🚀 **高性能渲染**：支持增量渲染、并发模式（React Concurrent Mode）和 FPS 控制，优化频繁更新场景的性能。
- 🔌 **扩展生态**：社区贡献了大量第三方组件和 Hooks，如文本输入、进度条、表格、选择列表等，加速开发。
- 📊 **广泛采用**：被 Claude Code、GitHub Copilot CLI、Shopify CLI、Prisma 等知名项目使用，拥有 39k+ GitHub Stars。
- 🛠️ **CI 友好**：在 CI 环境中自动优化渲染（仅输出最终帧），避免 ANSI 转义序列问题。

---

### [TanStack AI Beta：AI 工具界的瑞士成长记 | TanStack 博客](https://tanstack.com/blog/tanstack-ai-beta)

**原文标题**: [TanStack AI Beta: The Switzerland of AI Tooling Grows Up | TanStack Blog](https://tanstack.com/blog/tanstack-ai-beta)

TanStack AI 正式发布 Beta 版本，这是一个框架无关、提供商无关的 AI 工具包，强调无供应商锁定、开源和开发者控制权。

- 🎉 **Beta 版本意义重大**：核心 API 已稳定，协议已文档化并版本化，测试基础设施强大，从原型验证转向可构建真实产品的阶段。
- 🧩 **统一 API 覆盖所有模态**：文本、图像、视频、音频生成、实时语音聊天等，均通过同一套类型化活动模型实现，切换提供商只需更改导入和适配器。
- 🔒 **按模型类型安全**：对每个模型的具体选项和原生工具进行类型级限制，IDE 能准确提示，不兼容的工具会在编译时报错，而非生产环境静默失败。
- 🛠️ **构建真实系统的组件**：提供中间件、惰性工具发现、代码模式（安全沙箱执行 TypeScript）、主机端 MCP 连接以及实验性编排功能（支持人机协作、SSE 流等）。
- 🌐 **TypeScript 优先，基于开放协议**：核心是 AG-UI 事件协议，可与任何语言的后端（如 Kotlin、Python）互操作，前端支持 React、Solid、Vue 等主流框架。
- 🔍 **可观测的调试能力**：提供可插拔的调试日志（按类别开关）和同构开发者工具面板，清晰展示 LLM 内部流程、中间件执行和工具调用。
- ✅ **严格测试保障**：每次 PR 都运行 265 项确定性端到端测试，覆盖 10 个 LLM 提供商，能及时捕获提供商行为漂移和 API 变更。
- 💡 **保持开源与诚实**：无服务、无平台迁移、无供应商锁定，与 Vercel AI SDK 保持功能对比文档，鼓励社区贡献和反馈。

---

### [使用 LogTape 将 console.log 替换为结构化日志 | Sentry](https://sentry.io/cookbook/structured-logging-logtape/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=logs-fy27q1-cookbook&utm_content=newsletter-logtape-secondary-trysentry)

**原文标题**: [Replace console.log with structured logging using LogTape | Sentry](https://sentry.io/cookbook/structured-logging-logtape/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=logs-fy27q1-cookbook&utm_content=newsletter-logtape-secondary-trysentry)

本指南介绍了如何用 LogTape 和 Sentry 替换 console.log，实现结构化、可追踪的日志记录，帮助调试生产问题。

- 📝 **安装 LogTape 和 Sentry 插件**：通过 npm/pnpm/yarn 添加 `@logtape/logtape` 和 `@logtape/sentry` 包。
- ⚙️ **客户端配置**：初始化 Sentry 后，配置 LogTape 将日志发送到控制台和 Sentry，使用类别（如 `["my-app"]`）组织日志。
- 🖥️ **服务端隐式上下文**：利用 Node.js 的 `AsyncLocalStorage` 实现隐式上下文，自动附加 `userId` 或 `requestId` 等字段。
- 🔍 **使用过滤器控制日志级别**：通过 `withFilter()` 为不同环境设置最低日志级别，例如开发时显示 `debug`，生产环境只发送 `info` 及以上。
- 📊 **记录结构化对象**：用包含用户 ID、订单 ID 等丰富数据的对象替代字符串日志，提升可查询性。
- 🧩 **创建 React 上下文提供者**：在前端通过 `LoggerProvider` 和 `useLogger()` 钩子自动附加会话数据，无需手动传递。
- 🖇️ **在组件中使用日志**：在客户端组件中调用 `useLogger()` 获取已包含上下文的日志器，记录如帖子删除等事件。
- 🔗 **在 Sentry 中查看追踪日志**：错误发生时，在 Issues 中查看关联的日志、追踪和会话回放。
- 🔎 **在日志浏览器中查询**：在 Sentry 的 Explore > Logs 中按类别、严重性、用户 ID 等属性过滤和搜索日志。
- ⚡ **创建警报和仪表盘**：基于日志查询设置警报（如支付失败率飙升）和仪表盘，监控趋势并通知团队。

---

### [React Native 0.86 - 全面屏与开发者工具改进，无破坏性变更 · React Native](https://reactnative.dev/blog/2026/06/11/react-native-0.86)

**原文标题**: [React Native 0.86 - Edge-to-Edge and DevTools Improvements, no breaking changes · React Native](https://reactnative.dev/blog/2026/06/11/react-native-0.86)

React Native 0.86 版本发布，带来 Android 边缘到边缘支持和开发者工具改进，无破坏性变更。

- 📦 React Native 仓库迁移至 React 组织，GitHub 自动重定向，无需手动操作
- 📱 Android 15+ 边缘到边缘模式全面修复，包括 measureInWindow、KeyboardAvoidingView 和 Dimensions 等组件
- 🛠️ DevTools 新增明暗模式模拟功能，可通过 Command Palette 快速切换
- ✅ 无用户端破坏性变更，从 0.85 升级无需修改应用代码
- 🚫 废弃 ViewUtil.getUIManagerType 和 AppRegistry 部分 API
- ⚡ 性能优化：PerformanceObserver 默认阈值对齐 W3C 标准，修复动画闪烁问题
- 🐛 修复文本测量崩溃、非可逆变换触摸、Yoga 布局回归等多项问题
- 📡 新增 JSI API 支持类型数组、数组操作和错误创建
- 🔧 Android 修复 BackHandler、TextInput、Image 尺寸获取等多项问题
- 🌐 WebSocket 支持 Cookie 头，Blob 内容提供者适配新架构

---

### [React · GitHub](https://github.com/react)

**原文标题**: [react · GitHub](https://github.com/react)

这是 React 官方 GitHub 组织页面，展示了其核心开源项目与资源。页面列出了 10 个主要仓库，涵盖 Web 和原生 UI 开发框架、构建工具、布局引擎等，并提供了仓库的星标数、分支数、许可证及最近更新日期等关键信息。

- 📚 **react**：用于 Web 和原生用户界面的核心库，拥有 24.6 万星标，是最受欢迎的项目。
- 📱 **react-native**：使用 React 构建原生应用的框架，拥有 12.6 万星标，基于 C++ 开发。
- 🚀 **create-react-app**：一键设置现代 Web 应用的命令行工具，拥有 10.3 万星标。
- 🧩 **yoga**：可嵌入的布局引擎，遵循 Web 标准，拥有 1.88 万星标，基于 C++。
- 🚇 **metro**：React Native 的 JavaScript 打包工具，拥有 5.6 千星标。
- 🌐 **react-strict-dom**：标准化 Web 和原生平台样式化 React 组件的库，拥有 3.5 千星标。
- 📖 **react-native-website**：React Native 的官方文档网站，基于 MDX 编写。
- 🛠️ **react-native-devtools-frontend**：基于 Chrome DevTools 的 React Native 开发者工具前端。
- 📡 **react-native-cdp-status**：跟踪 Hermes 和 React Native 项目中 CDP 实现状态的仓库。
- 📝 **jsx**：JSX 规范，一种 ECMAScript 的 XML 类语法扩展。

---

### [React 基础](https://react.foundation/)

**原文标题**: [React Foundation](https://react.foundation/)

概述摘要  
React 基金会是一个社区驱动的透明倡议，致力于通过多方贡献维持和发展 React 生态系统，确保其长期繁荣。

- 🌐 **社区驱动与透明**：基金会以社区为核心，100% 透明运营，支持代码贡献、教育、组织和资金筹集。
- 🎯 **三大支柱**：资助维护者（直接财务支持）、教育资源（教程与文档）、全球可访问性（包容性发展）。
- 💻 **贡献途径**：通过代码提交、RFC、文档、组织活动或财务支持（商店购买、捐赠、赞助）参与。
- 🛒 **财务支持**：商店购物、直接捐赠、赞助 54+ 库（如 Redux、TanStack Query），或成为会员获得投票权。
- 🤝 **会员与创始成员**：正式成员可参与资金决策，创始成员已支持生态系统可持续发展。
- 📚 **教育与资源**：提供教程、文档、工作坊，帮助开发者掌握 React 及其生态系统。
- 🌍 **全球包容性**：确保所有背景和地区的开发者都能无障碍使用 React。
- 🚀 **立即行动**：贡献代码、组织活动、创建内容或支持财务，共同构建可持续未来。

---

### [Maestro MCP 服务器 | Maestro 文档](https://docs.maestro.dev/get-started/maestro-mcp?utm_source=this-week-in-react&utm_medium=newsletter&utm_campaign=mcp-viewer-jun17)

**原文标题**: [Maestro MCP Server | Maestro Docs](https://docs.maestro.dev/get-started/maestro-mcp?utm_source=this-week-in-react&utm_medium=newsletter&utm_campaign=mcp-viewer-jun17)

Maestro MCP 服务器允许编码代理编写、运行和调试移动端及网页端 UI 测试，支持多种主流编码代理工具，并集成了 Maestro Viewer 进行实时设备交互。

- 🚀 **快速入门**：Maestro MCP 服务器实现模型上下文协议（MCP），可直接集成 Claude Code、Cursor、GitHub Copilot 等编码代理。
- 📦 **安装步骤**：需先安装 Maestro CLI，再根据代理类型（如 Claude Code CLI、Claude Desktop、Codex CLI 等）配置 MCP 连接。
- 🖥️ **Maestro Viewer**：通过`open_maestro_viewer`工具在编码代理或浏览器中嵌入 iOS 模拟器/Android 模拟器，实时显示命令执行并支持交互。
- 🔄 **更新方法**：升级 Maestro CLI 即可更新 MCP 服务器，之后需在编码代理中重新加载 MCP 连接。
- 🛠️ **MCP 工具集**：包括`list_devices`（列出设备）、`inspect_screen`（获取视图层级）、`take_screenshot`（截图）、`run`（执行流程）等，支持本地和云端测试。
- ☁️ **云端集成**：`list_cloud_devices`、`run_on_cloud`和`get_cloud_run_status`工具需 Maestro Cloud 认证，支持提交流程并查看结果。
- 📚 **MCP 协议说明**：MCP 是开放标准，通过 JSON-RPC 2.0 在服务器和客户端间通信，Maestro MCP 服务器通过 stdio 暴露能力。

---

### [Chain React 2026](https://ti.to/chainreact/chainreact2026/discount/TWIR)

**原文标题**: [Chain React 2026](https://ti.to/chainreact/chainreact2026/discount/TWIR)

Chain React 是一场为期三天的 React Native 技术盛会，包含工作坊和会议，汇聚行业领袖与开发者，于 2026 年 7 月底在波特兰举行。

- 📅 活动时间：2026 年 7 月 29 日上午 8 点至 7 月 31 日下午 5 点
- 📍 举办地点：美国俄勒冈州波特兰市军械库（The Armory）
- 🎯 核心内容：1 天工作坊 + 2 天会议，聚焦 React Native 最新动态
- 🏢 顶级参与：来自 Meta、Amazon、Microsoft 等公司的领袖及全球开发者
- 📚 历史背景：自 2017 年起举办，持续吸引 React Native 领域知名人物
- 🤝 联合主办：由 Infinite Red 和 Expo 共同制作
- 🌐 社区贡献：通过 React Native Radio 播客、React Native Mornings 和 React Native Newsletter 传播信息
- 💰 门票信息：以美元计价，详情见官网
- 🔗 联系方式：邮箱 hello@chainreactconf.com，官网 chainreactconf.com

---

### [四年 React Native 快速加密之路：从钱包到节点同步——Margelo 博客](https://blog.margelo.com/four-years-of-react-native-quick-crypto)

**原文标题**: [Four Years of React Native Quick Crypto: From Wallets to Node Parity — Margelo Blog](https://blog.margelo.com/four-years-of-react-native-quick-crypto)

### 概述总结
本文详细介绍了 react-native-quick-crypto 库从 2022 年诞生到 2026 年的发展历程，涵盖其起源、关键贡献者、技术架构演进、性能优势及安全审计，最终成为 React Native 生态中 Node.js crypto 模块的替代方案。

- 📱 **起源与背景**：2022 年 2 月，Marc Rousavy 创建了 react-native-fast-crypto，旨在解决 Web3 钱包应用中纯 JavaScript 加密实现（如 SHA-256、HMAC）的性能瓶颈，通过原生 C++ 和 JSI 桥接替代慢速的 polyfill。
- 🔑 **核心贡献者**：Szymon Kapała 实现了 OpenSSL 集成、PBKDF2 和 HMAC 等基础算法；Oscar Franco 添加了 AES 加密、RSA 签名和 WebCrypto 部分功能；作者 Brad Anderson 于 2024 年加入，补充了 Ed25519、X25519 等本地优先应用所需算法。
- ⚙️ **技术架构演进**：2024 年通过 Nitro Modules 重构，用 TypeScript 规范生成 C++ 绑定，消除了手动 JSI 桥接的冗余代码，提升性能并降低 Bug 率。同步操作（如哈希）直接执行，重操作（如 PBKDF2）通过 C++ 线程池异步处理。
- 🚀 **性能对比**：在 iPhone 模拟器上，RNQC 相比纯 JS 库（如 crypto-browserify、@noble/hashes）实现显著加速：DH modp14 密钥生成快 7,480 倍，8MB HMAC SHA-256 快 1,418 倍，ECDH P-256 计算快 136 倍。
- 🔒 **安全与合规**：2026 年 4 月完成六阶段安全审计，修复了切片 ArrayBuffer 偏移错误、XSalsa20 密钥流重启问题、DH/ECDH 无效密钥检查、Bleichenbacher 预言机攻击等漏洞，并通过 CI 确保运行时零漏洞。
- 🌐 **功能扩展**：从钱包应用扩展到本地优先数据库（CRDTs），支持 Node.js crypto 模块全部功能，包括 X.509 证书、SHA-3、KMAC、后量子密码（ML-KEM、ML-DSA、SLH-DSA）等。
- 📈 **采用率增长**：周下载量从 2025 年 6 月的约 47,000 次增长至 2026 年 5 月的约 244,000 次，月下载量超 851,000 次，单日最高达 57,293 次，成为 React Native 加密库的默认选择。

---

### [React Native、Hermes 字节码与 Kindle 主页 | Rincon](https://sighery.com/posts/patching-kindle-homepage/)

**原文标题**: [React Native, Hermes bytecode, and the Kindle homepage | Rincon](https://sighery.com/posts/patching-kindle-homepage/)

Kindle 主页使用 React Native 和 Hermes 字节码技术，本文将深入探讨如何逆向工程和修补这些字节码以移除广告。

- 📱 Kindle 自 5.14.2 版本起，主页应用改用 React Native 开发，取代了之前的 Java 技术栈
- 🔧 Hermes 字节码版本不兼容（Kindle 使用版本 84，最新为版本 99），需要特定工具链进行逆向工程
- 🛠 hbctool 是关键的逆向工具，支持反汇编和重新汇编 Hermes 字节码，提供 Python API 进行自动化修补
- 📝 字符串修补有限制（不能改变长度），而指令修补更强大，可修改程序逻辑
- 💡 通过修改 isPremium 函数指令，可强制返回 true，展示如何绕过付费检查
- 🎯 使用 screenControl 工具和 KIWI 功能定位 Kindle 主页广告组件，识别出 Template49、Template18 等卡片
- 🚫 修补 Template49 和 Template18 的 render 函数（而非直接修补模板函数）可成功移除广告，而 Template5/2/13 可直接修补
- 🔍 通过字符串匹配（如 "Template18Card"）在众多 render 函数中定位目标，避免硬编码函数 ID
- 📦 KPP_Patch 项目已实现这些修补方案，欢迎社区贡献新补丁

---

### [使用预编译 XCFrameworks 加速 iOS 构建](https://expo.dev/blog/faster-ios-builds-with-precompiled-xcframeworks)

**原文标题**: [Faster iOS Builds with Precompiled XCFrameworks](https://expo.dev/blog/faster-ios-builds-with-precompiled-xcframeworks)

概述摘要  
- 🧠 本文主要探讨了人工智能在医疗诊断中的应用，强调其提升准确性和效率的潜力。  
- 📊 通过分析大量医疗数据，AI 能够识别早期疾病迹象，如癌症或心血管问题。  
- 🏥 实际案例显示，AI 辅助诊断系统在某些测试中已超越人类医生的表现。  
- ⚠️ 但文章也指出挑战，包括数据隐私、算法偏见和监管框架的缺失。  
- 🌍 未来展望中，AI 与医生协作的模式被认为是最佳路径，以实现更普惠的医疗服务。

---

### [我们如何将应用启动时间提升 50% | Pump.fun | 2026 年 6 月 | Medium](https://medium.com/@pumpdotfun_/how-we-improved-the-startup-time-of-our-app-by-50-b3107bed1bf9)

**原文标题**: [How We Improved the Startup Time of Our App by 50% | by Pump.fun | Jun, 2026 | Medium](https://medium.com/@pumpdotfun_/how-we-improved-the-startup-time-of-our-app-by-50-b3107bed1bf9)

### 概览总结
我们通过系统性优化和防护措施，将 Pump.fun 应用的启动时间缩短了 50%，重点解决了原生模块、JavaScript 包和运行时瓶颈。

- 📊 **启动时间重要性**：用户频繁打开应用时，每 100 毫秒延迟都会被感知，因此启动性能是关键产品指标。
- 🛠️ **测量与可观测性**：结合原生平台指标（Firebase、Xcode）和自定义分析（Datadog、react-native-performance），实现端到端启动阶段监控。
- 🔍 **剖析工具**：使用 Instruments（iOS）、Perfetto（Android）、APK Analyzer、Expo Atlas 和 Hermes CPU Profiler 分析发布构建版本。
- ⚡ **关键优化**：升级 React Native/Expo版本、启用R8混淆、移除冗余原生依赖（如Lottie、react-native-svg）、优化资源格式（WebP/AVIF）。
- 📦 **JS 包优化**：通过 Knip 检测死代码、Expo 摇树优化、将本地化文件移至 CDN，并利用 Hermes 追踪识别模块级耗时操作。
- 🚀 **运行时加速**：重写启动动画使用 useNativeDriver、合并延迟任务队列、对模块进行懒加载、将运行时计算（如 IDL 转换）移至构建时。
- 🛡️ **性能防护**：建立 CI 包大小检查、自动资源优化、死文件/包检测、Dangerfile 标记模块级操作，并开展团队培训工作坊。

---

### [MoQKit：适用于 iOS 和 Android 的原生移动 MoQ SDK](https://swmansion.com/blog/moqkit-native-mobile-sdk-moq-ios-android/)

**原文标题**: [MoQKit: A Native Mobile SDK for MoQ on iOS and Android](https://swmansion.com/blog/moqkit-native-mobile-sdk-moq-ios-android/)

MoQKit 是一个面向 iOS 和 Android 的原生 MoQ（基于 QUIC 的媒体传输）SDK，支持直播推流、播放和数据交换，基于 moq-ffi 构建，提供 Swift 和 Kotlin API。

- 📱 **原生移动 SDK**：提供 Swift（iOS）和 Kotlin（Android）API，用于直播推流、播放广播和自定义数据交换。
- 🎬 **四种演示模式**：包含播放器、发布者、聊天和 Boy 模式，帮助开发者快速上手。
- 🔗 **会话模型**：以 Session 为核心，管理中继连接，支持多路播放、发布和数据轨道。
- 📡 **播放流程**：连接中继 → 订阅命名空间 → 发现广播 → 选择轨道 → 原生渲染，延迟约 100 毫秒。
- 🎥 **推流功能**：支持摄像头、麦克风和屏幕捕获，可自定义视频/音频源。
- ⚙️ **安装方式**：iOS 通过 Swift Package，Android 通过 Maven Central，版本 0.2.0。
- 🧪 **基于 moq-lite**：使用更稳定的 moq-lite 协议，而非仍在演进的 moq-transport IETF 草案。
- 🚀 **React Native 支持**：正在开发中，先确保原生 API 稳定，再构建跨平台层。
- ❓ **常见问题**：MoQKit 适用于低延迟直播，非 WebRTC 替代品；可连接任何兼容中继，如 Fishjam 托管中继。

---

### [介绍 Observe：Expo 应用的性能监控](https://expo.dev/blog/introducing-observe)

**原文标题**: [Introducing Observe: Performance monitoring for Expo apps](https://expo.dev/blog/introducing-observe)

概述摘要：文章探讨了人工智能在医疗领域的应用，包括诊断辅助、药物研发和个性化治疗，同时指出了数据隐私和算法偏见等挑战。

- 🏥 人工智能通过分析医学影像和病历数据，帮助医生提高诊断准确性和效率。
- 💊 AI 加速药物研发过程，通过模拟分子相互作用和预测药物效果，缩短新药上市时间。
- 🧬 基于患者基因和生活方式数据，AI 支持个性化治疗方案，提升治疗效果。
- 🔒 数据隐私问题突出，医疗数据共享需严格保护患者信息，防止泄露。
- ⚖️ 算法偏见可能影响诊断公平性，需确保训练数据多样性和算法透明度。

---

### [原生开发变得简单了。我仍然押注 React Native。| Code with Beto](https://codewithbeto.dev/blog/still-betting-on-react-native)

**原文标题**: [Native got easy. I'm still betting on React Native. | Code with Beto | Code with Beto](https://codewithbeto.dev/blog/still-betting-on-react-native)

概述总结：文章作者 Beto 认为，尽管 AI 让原生开发变得更容易，但他仍坚持选择 React Native，因为跨平台开发能避免维护两套代码库的高昂成本，且 Expo 等工具正在缩小与原生体验的差距。

- 🤖 AI 降低了原生开发门槛，但跨平台需求依然存在
- 💡 原生开发意味着要么只支持一个平台，要么维护两套独立代码库，后者是长期负担
- 🛠️ React Native 结合 Expo 可以避免双重代码库的“税”，并支持引入原生组件
- 🚀 框架开发者也在利用 AI 优化自身工具，如 Expo Agent，使跨平台开发更轻松
- 📱 作者承认自己的应用在 Android 上不够完美，但单一代码库的灵活性值得接受
- 🧱 AI 降低了入门门槛，但技术基础不足的用户仍会因不知如何提问而遇到瓶颈
- 🔥 鼓励非技术用户尝试用 AI 构建简单应用，体验开发乐趣
- 🎯 作者押注 React Native，认为学习它是高杠杆投资，并推荐其课程中的新 Expo UI 部分

---

### [AI 辅助的 React Native 电视端迁移：Zattoo 的经验教训](https://www.callstack.com/blog/ai-assisted-react-native-migration-for-tv-lessons-from-zattoo)

**原文标题**: [AI-Assisted React Native Migration for TV: Lessons From Zattoo](https://www.callstack.com/blog/ai-assisted-react-native-migration-for-tv-lessons-from-zattoo)

Zattoo 通过 React Native 成功迁移了其电视应用，从多平台原生开发转向共享代码库，解决了组织和技术上的重复问题，并利用 AI 辅助工具加速了迁移过程。

- 📺 **跨平台挑战**：电视应用面临操作系统、设备、遥控器、输入模型和硬件性能的巨大差异，原生开发曾是唯一可行方案。
- 🔄 **组织瓶颈**：每个平台团队独立开发导致功能实现不一致，如暂停按钮在不同国家/地区的行为需多方协调，增加了协作成本。
- 🚀 **迁移契机**：亚马逊 Fire TV 和 Vega OS 的推出促使 Zattoo 选择 React Native，避免为每个新平台重复开发。
- 🧪 **概念验证先行**：从登录、后端通信、播放、输入等核心功能开始原型验证，而非全面重写，快速暴露实际问题。
- 📂 **共享代码策略**：共享配置、工具和业务逻辑，但保持平台差异显式化，如播放、SSO、输入处理等需平台特定实现。
- 📊 **性能与测试**：性能优化基于真实设备数据（如 Android TV 的 800+ 设备类型），测试聚焦行为级覆盖，平台差异通过辅助函数处理。
- 👥 **团队重组**：从平台团队转向价值流团队（如播放体验、内容搜索），降低认知负荷，原生专家支持产品团队而非孤立在平台筒仓中。
- 🤖 **AI 辅助作用**：AI 帮助理解遗留代码、生成测试初稿、加速重构，但关键决策（如流程优先级、平台行为、发布策略）仍需人工判断。
- 📝 **实用指南**：从风险流程开始，利用现有架构，保持平台差异显式，基于行为测试，用遥测数据指导性能优化，分离代码发布与平台部署，早期引入 React Native 经验。

---

### [Kotlin 编译器插件如何将 Android 首次渲染时间缩短 30%](https://expo.dev/blog/how-a-kotlin-compiler-plugin-cut-android-time-to-first-render)

**原文标题**: [How a Kotlin compiler plugin cut Android time to first render by 30%](https://expo.dev/blog/how-a-kotlin-compiler-plugin-cut-android-time-to-first-render)

概述：本文探讨了人工智能在医疗领域的应用，重点介绍了诊断辅助、药物研发和个性化治疗方面的突破，同时指出了数据隐私和伦理挑战。

- 🩺 人工智能通过分析医学影像，可辅助医生更快速、准确地诊断疾病，如癌症和心血管问题。
- 💊 在药物研发中，AI 能加速候选药物筛选和临床试验设计，缩短新药上市周期。
- 🧬 基于患者基因和病史，AI 可制定个性化治疗方案，提升治疗效果并减少副作用。
- 🔒 数据隐私问题突出，医疗数据共享需严格加密和合规管理，防止泄露风险。
- ⚖️ 伦理挑战包括算法偏见和决策透明性，需建立监管框架确保公平与责任。

---

### [App.js Conf 2026 回顾：手势处理 3.0 及更多](https://swmansion.com/blog/app-js-conf-2026-recap-gesture-handler-3-0-type-gpu-cli-screens-5-0-and-more/)

**原文标题**: [App.js Conf 2026 Recap: Gesture Handler 3.0 & More](https://swmansion.com/blog/app-js-conf-2026-recap-gesture-handler-3-0-type-gpu-cli-screens-5-0-and-more/)

App.js Conf 2026 大会回顾了 React Native 生态的多项重大更新，包括 Gesture Handler 3.0、TypeGPU CLI、Screens 5.0 等，并强调了社区交流的重要性。

- 🎤 **Gesture Handler 3.0 发布**：采用全新的基于 Hook 的 API，支持 SharedValues 直接配置手势，并推出新的 Touchable 组件，大幅减少心智负担和重新渲染。
- 📱 **React Native Bottom Sheet 库推出**：基于 Gesture Handler 和 Reanimated 构建，解决了底部弹出组件常见的滚动与手势冲突问题。
- 🖥️ **TypeGPU CLI 工具发布**：通过单命令配置，实现 GPU 着色器的 TypeScript 编写、死代码消除和跨平台使用（如 Three.js、React Native Skia）。
- 🤖 **设备端 AI 实践分享**：讨论 React Native Executorch 在 LLM 和计算机视觉应用中的挑战，包括应用体积、设备兼容性和电池消耗。
- 🧭 **Screens 5.0 即将到来**：将放弃旧架构支持，带来完全重写的堆栈和标签导航实现，与 Expo Router 深度协作。
- 👥 **社区活动亮点**：三天会议包含演讲、工作坊和线下交流，强调社区成员间的真实互动是活动核心价值。

---

### [GitHub - blazejkustra/react-native-morph-view: 使用平滑粘性效果将一张图像变形为另一张图像](https://github.com/blazejkustra/react-native-morph-view)

**原文标题**: [GitHub - blazejkustra/react-native-morph-view: Morph one image into another with a smooth gooey effect. · GitHub](https://github.com/blazejkustra/react-native-morph-view)

react-native-morph-view 是一个 React Native 组件，通过原生着色器实现两张图片之间的平滑“粘性”变形效果，只需切换一个 `toggle` 属性即可驱动动画。

- 🎨 **原生粘性变形** — 使用 Metal (iOS) 或 AGSL (Android) 着色器实现模糊加 Alpha 阈值效果，产生流体般的融合过渡，而非简单的交叉淡入淡出
- 🔄 **单一属性控制** — 切换 `toggle` 属性即可在 `from` 和 `to` 图片间双向变形，无需编写命令式动画代码
- 🖼️ **支持多种图片源** — 兼容本地资源 (`require(...)`)、远程 URL 或文件 URI，使用 React Native 标准图片格式
- 🌀 **粘性轮廓边框** — 可选边框会跟随变形轮廓动态变化，而非围绕视图的矩形 CSS 框
- ⚙️ **可调节粘性参数** — `blurRadius` 控制中间态的粘稠度，`duration` 控制动画时长
- 📱 **三平台支持** — iOS、Android 和 Web 共享同一 `<MorphView />` 接口，Web 使用动画交叉淡入淡出作为回退方案
- 🚀 **仅支持 Fabric 新架构** — 需要 React Native 0.76+ 及新架构
- 📦 **安装简单** — 通过 `npm install react-native-morph-view` 安装，要求 iOS 15.1+、Android API 33+
- 💡 **使用技巧** — 推荐使用透明背景的纯色形状图片以获得最佳效果；可搭配 `LayoutAnimation` 同步布局变化；通过 `tintColor` 实现主题色单色图标
- 📚 **包含示例** — `example/` 目录提供可运行演示，支持形状、照片和多图库变形，并带有实时参数控制

---

### [发布 v1.9.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.9.0)

**原文标题**: [Release Release v1.9.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.9.0)

uniwind 项目发布了 v1.9.0 版本，主要包含新功能与多项错误修复。

- 🚀 新增布局方向组件功能
- 🐛 修复更新 web 变体条件的问题
- 🔄 修复安装多个 uniwind 实例时打包器无限循环的错误
- 🎯 修复组合变体相互覆盖的问题
- 👤 本次发布由贡献者 Brentlok 完成主要工作

---

### [发布 8.14.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.14.0)

**原文标题**: [Release 8.14.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.14.0)

Sentry React Native SDK 8.14.0 版本发布，主要新增了深度链接追踪、性能监控和 Expo Router 支持等功能，并修复了多项问题。

- 🚀 新增深度链接与导航事务关联功能，可标记由深度链接触发的导航，并记录延迟时间，覆盖冷启动和热启动场景
- 📊 为 Android 性能分析添加内存、CPU 和帧率测量支持
- 🔧 新增 `enableAutoConsoleLogs` 选项，允许在保留手动日志的同时关闭自动 `console.*` 捕获
- 🧭 增强 Expo Router 支持，为 `push`、`replace`、`navigate` 等操作添加面包屑和跨度，并标记导航方法
- 🔒 对可能包含用户标识的 Expo Router 属性（如 `route.href`）进行隐私保护，仅在 `sendDefaultPii` 开启时记录
- ⚠️ 添加 Gradle 版本兼容性警告，当 `sentry-android` 版本不匹配时发出提示
- 🐛 修复多项问题，包括排除服务器端模块、启用 Expo SDK 56 的 fetch 检测，以及解决孤立依赖布局中的 `sentry-cli` 解析
- 🔧 内部改进：将 `sentry.gradle` 转换为 Kotlin DSL，并保留旧文件以保持向后兼容
- 📦 依赖更新：JavaScript SDK 升级至 v10.57.0，CLI 升级至 v3.5.0，Android SDK 升级至 v8.43.1，Cocoa SDK 升级至 v9.16.1

---

### [发布 2.32.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v2.32.0)

**原文标题**: [Release 2.32.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v2.32.0)

react-native-gesture-handler 发布了 v2.32.0 版本，主要包含重要变更、bug 修复和杂项改进。

- ❗ 重要变更：移除 Android 上的 `getChildInDrawingOrderAtIndex` 方法
- 📱 支持 React Native 0.86 版本
- 🛠 修复 `RNRenderer` 导入问题，适配 React Native 0.86+
- 🐛 iOS 修复：重复的 `testID` 问题
- 🐛 Android 修复：离散手势未触发 `onFinalize` 事件
- 🐛 Android 修复：报告的错误指针数量
- 🐛 iOS 修复：手势检索和坐标空间不匹配问题
- 🐛 iOS 修复：解析识别器时不再迭代到根节点
- 🐛 Android 修复：`LongPressGestureHandler` 中 `numberOfPointers` 配置的指针要求
- 🔧 杂项：移除旧架构 CI、修复 Pods 别名解析、移动 Ruby 工具到模块、更新 Expo 和 Reanimated 依赖

---

### [GitHub - N0ku/react-native-nitro-healthkit: 用于读取和写入健康数据的 React Native Nitro 模块：一个覆盖 Apple HealthKit（iOS）和 Android Health Connect 的 TypeScript API。支持快速 Swift/Kotlin/C++ 互操作、缓存、观察者及后台同步。](https://github.com/N0ku/react-native-nitro-healthkit)

**原文标题**: [GitHub - N0ku/react-native-nitro-healthkit: React Native Nitro module for reading and writing health data: one TypeScript API over Apple HealthKit (iOS) and Android Health Connect. Fast Swift/Kotlin/C++ interop, cache, observers, and background sync. · GitHub](https://github.com/N0ku/react-native-nitro-healthkit)

react-native-nitro-healthkit 是一个高性能的跨平台 React Native 库，通过单一 TypeScript API 在 iOS 和 Android 上访问健康数据，支持 Apple HealthKit 和 Android Health Connect。

- 🚀 **超高性能**：基于 Nitro Modules 构建，利用原生 Swift/Kotlin 和 C++ 互操作，提供原生级性能。
- 🌍 **跨平台支持**：一个 TypeScript API 对应 iOS Swift 和 Android Kotlin 两套原生实现。
- 📊 **数据全面**：支持步数、心率、活动能量、距离、睡眠、锻炼等约 130 种数量类型和 70 种类别类型。
- 🔒 **隐私优先**：内置 HealthKit 和 Health Connect 的授权流程，确保数据安全。
- ✍️ **数据写入**：支持 `writeQuantityData` 和 `writeCategoryData` 手动插入样本数据。
- 👀 **数据观察**：通过 `observeQuantityChanges` 和 `observeCategoryChanges` 实时监控数据变化。
- 🌙 **后台同步**：支持 Android WorkManager 和 iOS BGTaskScheduler 定期后台同步数据到后端。
- 🎯 **类型安全**：完整的 TypeScript 支持，提供类型定义和现代 async/await API。
- ⚡ **Promise 基础**：所有 API 均返回 Promise，便于异步操作和错误处理。

---

### [发布 v0.8.0 · JoaoPauloCMarra/react-native-nitro-markdown · GitHub](https://github.com/JoaoPauloCMarra/react-native-nitro-markdown/releases/tag/v0.8.0)

**原文标题**: [Release v0.8.0 · JoaoPauloCMarra/react-native-nitro-markdown · GitHub](https://github.com/JoaoPauloCMarra/react-native-nitro-markdown/releases/tag/v0.8.0)

概述摘要
- 🎉 发布 v0.8.0 版本，包含多项改进和修复
- ✨ 新增功能：MarkdownStream 支持自定义 renderMarkdown 渲染组件
- 📦 导出多个接口：useMarkdownStreamState、MarkdownStreamRenderProps 等，便于无头流式渲染
- 🔧 类型增强：启用 exactOptionalPropertyTypes 并优化可选属性，避免传递 undefined
- 🐛 iOS 修复：MarkdownSession 方法现在会截断越界范围，防止崩溃
- ⚡ 性能优化：MarkdownStream 在父组件稳定渲染时不再重新读取完整原生会话文本，减少不必要的桥接工作

---

### [发布 2.0.0 版本 · numandev1/react-native-compressor · GitHub](https://github.com/numandev1/react-native-compressor/releases/tag/v2.0.0)

**原文标题**: [Release Release 2.0.0 · numandev1/react-native-compressor · GitHub](https://github.com/numandev1/react-native-compressor/releases/tag/v2.0.0)

react-native-compressor 发布了 v2.0.0 版本，这是一个重大更新，引入了破坏性变更，并修复了多个问题。

- 🔄 迁移原生模块至 `react-native-nitro-modules`，需安装并链接该依赖
- 📱 最低 React Native 版本要求提升至 0.75+，iOS 目标版本升至 13.4+，Android SDK 升至 24
- 🚫 移除了通过 `NativeEventEmitter` 和 `NativeModules.Compressor` 的直接访问，改用回调 API
- 🐛 修复了视频导出时静默返回仅音频 MP4 的问题，现在会正确报错
- ⚙️ Android 的 `getFileSize` 方法在失败时现在会拒绝（reject）而非返回空字符串
- 🔧 升级后需执行干净的原生重建

---

### [GitHub - pablogdcr/react-native-data-detector: React Native 跨平台文本数据检测。在 iOS 上使用 NSDataDetector，在 Android 上使用 ML Kit 实体提取，检测电话号码、网址、电子邮件、日期和地址。](https://github.com/pablogdcr/react-native-data-detector)

**原文标题**: [GitHub - pablogdcr/react-native-data-detector: Cross-platform text data detection for React Native. Uses NSDataDetector on iOS and ML Kit Entity Extraction on Android to detect phone numbers, URLs, emails, dates, and addresses. · GitHub](https://github.com/pablogdcr/react-native-data-detector)

react-native-data-detector 是一个跨平台的 React Native 库，利用 iOS 的 NSDataDetector 和 Android 的 ML Kit 实体提取功能，检测文本中的电话号码、网址、电子邮件、地址和日期，并以结构化结果返回。

- 📱 **跨平台检测**：支持 iOS 和 Android，使用原生 API 确保高准确性，而非正则表达式。
- 🔍 **多种实体类型**：可检测电话号码、网址、电子邮件、地址（iOS 解析结构化组件）和日期（ISO 8601 格式）。
- 🚀 **React Hooks 支持**：提供 `useDataDetector`（命令式）和 `useDetectedEntities`（响应式，适合输入时检测）两个钩子，自动管理模型状态。
- 🌐 **多语言支持**：Android 上可选 15 种语言模型（如英语、法语、中文等），iOS 语言无关。
- ⚙️ **灵活 API**：包括 `detect()`、`prepareModel()` 等函数，支持指定检测类型和语言，并返回精确的位置和结构化数据。
- 💾 **离线可用**：Android 模型可预下载（约 5.6MB/语言），iOS 原生支持离线。
- 📦 **安装简便**：通过 npm 安装，iOS 需 `pod-install`，Android 自动在运行时下载模型。
- 📋 **平台差异**：iOS 使用 NSDataDetector，Android 使用 ML Kit；地址解析在 iOS 上更详细，Android 返回原始字符串。
- 🛠️ **要求**：iOS 15.1+，Android API 26+，Expo SDK 50+ 或裸 React Native。
- 📄 **开源许可**：MIT 许可，欢迎贡献。

---

### [发布 1.0.0 版本 & 更名！· software-mansion/react-native-enriched-html · GitHub](https://github.com/software-mansion/react-native-enriched-html/releases/tag/v1.0.0)

**原文标题**: [Release Release 1.0.0 & Rename! · software-mansion/react-native-enriched-html · GitHub](https://github.com/software-mansion/react-native-enriched-html/releases/tag/v1.0.0)

概述摘要  
- 🎉 库正式发布 1.0.0 稳定版本，感谢社区贡献  
- 💫 更名为 react-native-enriched-html，提升透明度  
- 📦 旧包 react-native-enriched 将退役，不再更新  
- 🔄 升级无破坏性变更，仅需安装新包并更新导入语句  
- 🚀 继续完善 Enriched 生态系统

---

### [发布 create-react-native-library@0.63.0 · callstack/react-native-builder-bob · GitHub](https://github.com/callstack/react-native-builder-bob/releases/tag/create-react-native-library%400.63.0)

**原文标题**: [Release create-react-native-library@0.63.0 · callstack/react-native-builder-bob · GitHub](https://github.com/callstack/react-native-builder-bob/releases/tag/create-react-native-library%400.63.0)

react-native-builder-bob 发布了 0.63.0 版本，主要更新了导出条件名称以增强唯一性，并包含了代码签名验证。

- 📦 发布 create-react-native-library@0.63.0 版本（2026-06-16）
- 🔑 该版本标签和提交均经过 GPG 签名验证（密钥 ID: 31DAAC48ACF28F61）
- ✨ 新增功能：为导出条件使用唯一名称（#948），由 @satya164 实现
- 🛠️ 包含 2 个资源文件
- ⚠️ 页面加载时出现错误，提示“请重新加载此页面”

---

### [发布 v3.0.6 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.0.6)

**原文标题**: [Release v3.0.6 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.0.6)

该页面是 LegendApp/legend-list 项目的 GitHub 发布页面，记录了 v3.0.6 版本的更新信息。

- 🔧 修复：KeyboardAwareLegendList 现在在启用 alignItemsAtEnd 时考虑底部安全区域，确保短聊天风格列表正确固定在键盘或安全区域上方，避免位置过低或产生多余滚动空间。
- 📅 版本：v3.0.6，由 jmeistrich 于 6 月 16 日 14:21 发布，基于主分支的 9 次提交。
- 👍 反应：该版本获得 6 个用户点赞。

---

### [发布 5.6.0 · zoontek/react-native-permissions · GitHub](https://github.com/zoontek/react-native-permissions/releases/tag/5.6.0)

**原文标题**: [Release 5.6.0 · zoontek/react-native-permissions · GitHub](https://github.com/zoontek/react-native-permissions/releases/tag/5.6.0)

### 概述总结
该页面是 react-native-permissions 库的 GitHub 发布页面，展示了 5.6.0 版本的更新内容。

- 📦 **版本发布**：5.6.0 版本于 6 月 16 日 发布，基于 master 分支的 1 次提交。
- 🔐 **安全验证**：提交由作者 zoontek（Mathieu Acthernoene）签名，GPG 密钥已验证。
- ✨ **新增功能**：添加了 `openContactPicker` 方法，用于在 iOS 18+ 上编辑有限的联系人选择。
- 👤 **新贡献者**：@pablogdcr 首次贡献，参与了此版本的开发。
- 📄 **相关链接**：页面包含代码、问题、拉取请求、操作、项目、安全与质量、洞察等导航选项。

---

### [发布 v0.17.6 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.17.6)

**原文标题**: [Release v0.17.6 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.17.6)

overview summary  
- 🚀 优化了 Rslib 启动构建性能  
- 📱 支持 iOS 外部 XCTest 运行器工件  
- 🔧 修复了外部 XCTest 运行器标志分类问题  
- 🛠️ 为 iOS 添加了无操作 XCTest 运行器启动模式  
- ❌ 修复了 Maestro iOS 运行器设置失败归因问题  
- 📊 改进了 Maestro 测试报告器功能  
- 🆕 新贡献者 @hannojg 首次参与贡献

---

### [学习 React Native 声明式手势与动画 - YouTube](https://www.youtube.com/watch?v=HmFvvd5bLSo&list=PLkOyNuxGl9jy5hgF3xR64k9reOM5jHDHl)

**原文标题**: [Learn React Native Declarative Gestures and Animations - YouTube](https://www.youtube.com/watch?v=HmFvvd5bLSo&list=PLkOyNuxGl9jy5hgF3xR64k9reOM5jHDHl)

本頁面列出了 YouTube 平台的各項基本資訊與政策連結，涵蓋版權、條款、隱私及創作者相關內容。

- 📰 **新聞中心**：提供 YouTube 最新消息與公告。
- ©️ **版權**：說明內容版權相關規範與申訴機制。
- 📞 **聯絡我們**：提供與 YouTube 團隊聯繫的管道。
- 🎨 **創作者**：針對內容創作者提供的資源與工具。
- 📢 **刊登廣告**：說明在 YouTube 上投放廣告的選項。
- 👨‍💻 **開發人員**：提供 API 與技術整合資訊。
- 📜 **條款**：列出使用 YouTube 服務的條款與條件。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋社群指南與安全保護措施。
- ⚙️ **YouTube 的運作方式**：解釋平台推薦與內容管理機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能。
- 📅 **© 2026 Google LLC**：版權年份與所屬公司資訊。

---

### [你好，项目重绘](https://wcandillon.dev/article/hello-project-redraw)

**原文标题**: [Hello, Project Redraw](https://wcandillon.dev/article/hello-project-redraw)

**概述总结**  
Redraw 是基于 WebGPU 构建的新型 2D 图元系统，允许开发者通过 TypeScript 函数（编译为 GPU 着色器）动态控制路径的描边宽度、颜色和羽化效果，实现丰富的矢量渲染，如物理材质、运动模糊和背景模糊。

- 🎨 **动态着色器函数**：描边宽度和颜色不再是静态值，而是接收几何信息（如弧长、切线）的 GPU 函数，支持正弦波、颜色插值等复杂效果。
- ⚡ **WebGPU 驱动**：利用 WebGPU 的计算着色器和存储缓冲区，构建高效的贝塞尔路径加速结构，无需重写整个图形栈。
- 🧠 **TypeGPU 编译优化**：着色器函数在打包时编译，运行时无依赖；`compTime` 特性允许静态 JS 表达式（如字符串数组）直接转换为着色器代码。
- 🌫️ **几何羽化**：基于路径几何而非像素模糊实现边缘柔化，支持分析性运动模糊（根据速度方向）和单通道背景模糊（如毛玻璃效果）。
- 💡 **物理渲染 (PBR)**：通过代码为 2D 界面添加材质深度，如程序化斜面效果，无需手动烘焙光照信息。
- 🚀 **实验阶段与访问**：项目仍处于实验阶段，提供在线演示；订阅者可提前体验，开发者可联系作者反馈需求。

---

### [App.js Conf 2026 - YouTube](https://www.youtube.com/playlist?list=PLSk21zn8fFZCE_TlHUVnTVMm7mNl_fzxl)

**原文标题**: [App.js Conf 2026 - YouTube](https://www.youtube.com/playlist?list=PLSk21zn8fFZCE_TlHUVnTVMm7mNl_fzxl)

YouTube 平台資訊總覽  
- 📰 **新聞中心**：提供官方新聞與更新  
- ©️ **版權**：保護內容創作者權益  
- 📞 **聯絡我們**：提供用戶支援與聯繫方式  
- 🎥 **創作者**：為內容創作者提供資源與工具  
- 📢 **刊登廣告**：協助品牌與廣告主推廣  
- 👨‍💻 **開發人員**：提供 API 與技術整合服務  
- 📜 **條款**：使用規範與服務條款  
- 🔒 **私隱**：用戶資料保護政策  
- 🛡️ **政策及安全**：平台安全與內容審核機制  
- ⚙️ **YouTube 的運作方式**：解釋平台功能與演算法  
- 🧪 **測試新功能**：新功能試用與回饋  
- 📅 **© 2026 Google LLC**：版權歸屬與法律聲明

---

### [Expo UI 速成课程 | React Native 中的真正原生 UI - YouTube](https://www.youtube.com/watch?v=4j6NvCNPGtE)

**原文标题**: [Expo UI Crash Course | Truly Native UI in React Native - YouTube](https://www.youtube.com/watch?v=4j6NvCNPGtE)

本頁面列出了 YouTube 平台相關的資訊與政策連結，包括版權、聯絡方式、創作者支援、廣告刊登、隱私與安全等核心內容。

- 📰 新聞中心：提供 YouTube 的最新公告與媒體資訊
- ©️ 版權：說明內容使用的版權規則與申訴機制
- 📞 聯絡我們：提供用戶與平台聯繫的管道
- 🎬 創作者：為內容創作者提供工具與資源
- 📢 刊登廣告：協助企業在 YouTube 上投放廣告
- 👨‍💻 開發人員：提供 API 與技術文件給開發者
- 📜 條款：列出使用 YouTube 服務的條款與條件
- 🔒 私隱：說明用戶資料的收集與使用方式
- 🛡️ 政策及安全：規範內容審查與安全準則
- ⚙️ YouTube 的運作方式：解釋推薦系統與平台機制
- 🧪 測試新功能：介紹正在測試中的新功能
- 🏢 © 2026 Google LLC：版權歸屬與法律聲明

---

### [React Native Radio - RNR 365 - Chain React 2026](https://infinite.red/react-native-radio/rnr-365-chain-react-2026)

**原文标题**: [React Native Radio - RNR 365 - Chain React 2026](https://infinite.red/react-native-radio/rnr-365-chain-react-2026)

概述总结
- 🎙️ 本期 RNR 365 播客邀请三位嘉宾讨论 Chain React 2026 大会，分享社区故事、AI 趋势和幕后趣闻
- 🏛️ Chain React 是专注 React Native 的单轨制技术大会，每年在波特兰军械库举办，以独特场地和社区氛围著称
- 🤝 大会强调面对面交流的价值，通过单轨制设计和波特兰特色场地促进开发者深度互动
- 🎤 特邀专业 MC Kenneth LaFrance 主持，穿插即兴喜剧和互动环节，提升参会体验
- 🍕 会后派对由 Expensify 赞助，在波特兰美食车聚集区附近举办，提供社交机会
- 🤖 2026 年大会将包含 AI 与 React Native 结合的主题演讲，涵盖语音识别、工作流优化等前沿话题
- 🎟️ 使用优惠码 FRIENDS15 可享门票折扣，鼓励开发者亲自参会获取 YouTube 无法提供的现场体验
- 📖 嘉宾分享幕后故事，包括"Tai Kwon Jive"偷比特币纪念币的趣闻，以及演讲者临时更换主题的意外事件
- 🌤️ 七月的波特兰气候宜人（少雨低湿），为参会者提供舒适的技术交流环境
- 💼 大会吸引决策者和开发者共同参与，被视为推动 React Native 未来发展的重要平台

---

### [加载器：通过 arcanis 实现包映射 · 拉取请求 #62239 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62239)

**原文标题**: [loader: implement package maps by arcanis · Pull Request #62239 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62239)

Node.js 引入实验性包映射功能，通过静态 JSON 文件替代 `node_modules` 目录解析，解决依赖解析中的已知问题。

- 📦 新增 `--experimental-package-map=<path>` 标志，允许 Node.js 使用静态 JSON 文件解析包，替代传统的 `node_modules` 目录遍历。
- 🚫 解决幻影依赖问题：包只能导入其显式声明的依赖，防止意外访问未声明的传递依赖。
- 🏗️ 修复 monorepo 中对等依赖解析问题：不同版本的同名包（如 react@18 和 react@19）可共存，避免 hoisting 导致的版本冲突。
- ⚡ 减少 I/O 操作：静态映射避免文件系统遍历，提升解析速度，尤其适合多 Git 树场景。
- 🔄 兼容 `node_modules`：包管理器可同时生成 `node_modules` 文件夹和 `package-map.json`，后者引用前者路径，实现渐进式采用。
- 🛡️ 严格模式：默认在发现问题时抛出错误（如访问未声明依赖），未来可考虑通过标志或字段切换为警告模式。
- 🔧 与导入映射的区别：包映射使用扁平化结构支持多版本共存，而导入映射的 `scopes` 字段按文件系统路径键控，无法满足此需求。
- 🤝 包管理器集成：Yarn、pnpm 等可自动生成 `node_modules/.package-map.json`，并通过 `NODE_OPTIONS` 注入标志。
- 🧪 实验性功能：当前处于 `--experimental-*` 标志下，允许迭代和反馈，未来可能标准化。

---

### [发布 v4.17.0 · yarnpkg/berry · GitHub](https://github.com/yarnpkg/berry/releases/tag/@yarnpkg/cli/4.17.0)

**原文标题**: [Release v4.17.0 · yarnpkg/berry · GitHub](https://github.com/yarnpkg/berry/releases/tag/@yarnpkg/cli/4.17.0)

yarnpkg/berry 仓库发布了 v4.17.0 版本，主要更新包括支持包映射生成、修复多个问题以及新增 npm 配置功能。

- 🎉 新增支持包映射生成功能（由 @arcanis 贡献）
- 🔧 修复了 yarnrc 配置中缺少的 catalog 设置（由 @cyphercodes 贡献）
- 📝 文档更新：澄清后台任务退出码（由 @StantonMatt 贡献）
- ❓ 修复了 `why` 命令中对等依赖的说明（由 @StantonMatt 贡献）
- 📖 文档修正：npmMinimalAgeGate 的默认值（由 @clemyan 贡献）
- 🚀 新增功能：允许按 npmScope 设置 npmMinimalAgeGate（由 @erlandasz 贡献）
- 👥 欢迎新贡献者：@cyphercodes、@StantonMatt 和 @erlandasz
- 🏷️ 版本标签：@yarnpkg/cli/4.17.0，基于 master 分支的 2 次提交

---

### [功能：通过 arcanis 添加对包映射的支持 · 拉取请求 #12430 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/pull/12430)

**原文标题**: [feat: add support for package maps by arcanis · Pull Request #12430 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/pull/12430)

pnpm 新增对 Node.js 实验性包映射 (package maps) 的支持，通过生成 `node_modules/.package-map.json` 文件并注入 `--experimental-package-map` 标志，让 Node.js 在 pnpm 管理的安装和脚本执行中使用包映射解析依赖。

- 🚀 新增 `node-experimental-package-map` 和 `node-package-map-type` 配置，控制包映射的生成与注入行为。
- 📝 在安装时自动生成 `node_modules/.package-map.json` 文件，支持隔离 (isolated) 和提升 (hoisted) 两种链接器。
- 🔧 在 `pnpm exec`、`pnpm run` 及生命周期脚本中自动注入 `--experimental-package-map` 标志到 `NODE_OPTIONS` 环境变量。
- 🧪 添加了标准 (standard) 和宽松 (loose) 两种包映射类型，宽松模式下允许类似提升的依赖访问。
- ⚡ 性能基准测试显示，新功能对安装性能影响极小，可忽略不计。
- 🐛 修复了 Yarn v2 锁文件导入兼容性问题，改用 `js-yaml` 库解析。
- 🛡️ 代码审查中发现了多个安全与正确性问题，包括原型污染、符号链接覆盖、路径引用错误等，已通过后续提交修复。

---

### [使用网络标准的深色模式](https://olliewilliams.xyz/blog/dark-mode/)

**原文标题**: [Dark mode with web standards](https://olliewilliams.xyz/blog/dark-mode/)

本文介紹了使用 CSS 和 JavaScript 實現網頁深色模式的標準方法，強調尊重用戶系統設定的同時，提供網站內切換選項。

- 🌗 **支援系統偏好與手動切換**：預設使用`<meta name="color-scheme" content="light dark">`遵循 OS 設定，並透過 JavaScript 更新 meta 標籤及 localStorage，讓用戶可自由切換亮色、深色或回歸系統模式。
- 🎨 **color-scheme 影響範圍**：影響 CSS 的`light-dark()`函數、系統顏色（如 Canvas）、滾動條顏色、預設 HTML 元素顏色、iframe（若內嵌文件同意）及使用`light-dark()`或`prefers-color-scheme`的 SVG。
- ⚠️ **color-scheme 不影響 prefers-color-scheme**：多數情況下，`prefers-color-scheme`僅反映 OS 設定，不隨`color-scheme`改變，因此無法用於內頁切換（但 iframe 和 SVG 是例外，會受父文檔影響）。
- 🖼️ **light-dark() 支援圖片與漸層**：此函數現可用於漸層和圖片背景，例如根據模式切換不同圖片或漸層效果，並支援單色與漸層間的切換。
- 🔧 **處理非顏色變化**：對陰影、邊框等非顏色屬性，可透過 CSS 自定義屬性（如`--dark`）搭配`@container style()`查詢實現模式切換，或使用`@property`定義`--usedScheme`來檢測當前模式。
- 🔮 **未來可能**：未來可能透過 JavaScript 直接覆蓋`prefers-color-scheme`，但目前尚無瀏覽器實現此規範。

---

### [我们在 Prisma Compute 上投入使用了 Bun 的 Rust 重写](https://www.prisma.io/blog/bun-rust-rewrite-prisma-compute)

**原文标题**: [We put Bun's Rust rewrite in production on Prisma Compute](https://www.prisma.io/blog/bun-rust-rewrite-prisma-compute)

本报告详述了 Prisma Compute 为何选择在 Bun 的 Rust 重写版本（canary）上启动公测，而非稳定版。核心原因是稳定版存在内存泄漏和连接池在实例暂停/恢复后无法恢复的致命问题，而 Rust 重写版在测试中完美解决了这些问题。

- 🚀 **选择 Bun 的原因**：Bun 是一个开箱即用、兼容 Node.js 的 TypeScript 运行时，能完美匹配 Compute 的需求——在数据库旁运行应用、空闲时缩零、流量恢复时快速唤醒。
- 🧠 **Compute 的严苛测试**：Compute 应用是长期运行的服务，需应对空闲暂停、内存快照恢复、连接池死连接等复杂场景，这对运行时可靠性提出了远超基准测试的要求。
- 💥 **稳定版的关键问题**：内存泄漏（如 S3 文件读取导致 RSS 持续增长直至容器被 OOM 杀死）和连接池在实例恢复后无法感知死连接，导致新查询永久挂起。
- ✅ **Rust 重写版的改进**：在相同测试下，Rust 重写版内存使用保持平稳（峰值约 118 MiB），连接池在恢复后能正常重连，解决了稳定版的所有关键故障。
- 🎯 **启动公测的决策**：团队在“使用有问题的稳定版”、“维护私有分支”和“采用修复问题的 canary 版”中选择了后者，尽管 canary 是预发布版本，但通过了实际负载测试。
- 🔧 **Rust 重写的优势**：Rust 的所有权模型和 RAII 模式减少了手动资源清理错误，编译器能提前发现问题，且新代码库更易于贡献和修复。
- 📡 **生产反馈循环**：通过在生产环境中发现问题、提炼可复现报告、推动上游修复，形成了高效的反馈闭环，这是开源运行时持续改进的关键。

---

### [TanStack Table V9 中的 TypeScript 性能 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-typescript-performance)

**原文标题**: [TypeScript Performance in TanStack Table V9 | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-typescript-performance)

TanStack Table V9 通过重构类型系统，大幅提升了 TypeScript 性能，将类型实例化次数从 V8 的 14.7 倍降至仅 2 倍，同时保持了更强大的模块化功能。

- 🚀 **性能大幅提升**：核心包类型实例化减少 78.3%（从 123 万降至 26.7 万），React 适配器减少 76.9%，所有适配器均提升 62-86%。
- 🔧 **模块化类型系统**：V9 引入 `TFeatures` 泛型参数，通过特征映射（Feature Map）实现按需组合，替代 V8 的全局声明合并，支持树摇和按表推断 API。
- ⚡ **关键优化措施**：用命名接口替代条件联合类型（减少 60% 实例化）、内部类型使用纯接口（再降 40%）、添加 `in out` 方差注解（React 适配器从 136k 降至 54.7k）、显式类型参数消除推断开销（节省 15%）。
- 📊 **测量方法**：使用 `tsc --extendedDiagnostics` 的 Instantiations 指标，配合 `--generateTrace` 定位瓶颈，确保优化可复现且稳定。
- 🎯 **开发者影响**：用户无需关注底层优化，编辑器体验从明显延迟变为即时响应；库作者可借鉴命名类型、接口优先、方差注解和显式类型参数等最佳实践。

---

### [支持那个 · 2026 年 6 月 13 日](https://nerdy.dev/prop-for-that)

**原文标题**: [Prop For That · June 13, 2026](https://nerdy.dev/prop-for-that)

### 概述总结
Prop For That 是一个 JS 库，通过声明式属性将 JS 动态信息实时映射为 CSS 自定义属性，让 CSS 能直接使用输入值、指针位置、滚动条尺寸等实时数据，无需手动编写 JS 代码。

- 🎯 **核心价值**：解决 CSS 无法直接获取 JS 动态信息（如输入值、指针位置、滚动条尺寸等）的痛点，通过数据属性声明即可自动生成实时 CSS 变量
- 🧩 **插件化架构**：所有功能以插件形式按需加载，支持指针位置、视口尺寸、元素可见性、输入状态、图像颜色提取、视频进度、设备传感器等 20+ 种实时属性
- 🔄 **样式查询集成**：与 CSS 样式查询（`@container style()`）配合使用，实现基于动态属性的条件样式，例如表单验证状态
- ⚡ **极简使用方式**：只需`import 'prop-for-that/auto'`，在元素上添加`data-props-for`属性，即可在 CSS 中使用`--live-*`变量
- 🖼️ **图像颜色提取**：可从图像或视频中提取平均色、强调色、亮暗色等，实现组件根据内容自动配色
- 📱 **设备感知能力**：支持电池状态、网络类型、CPU 压力、地理定位、设备倾斜等硬件信息（部分仅 Chromium）
- 🛠️ **社区反馈**：开发者普遍认为这是 CSS 与 JS 之间的优雅桥梁，但需注意 Firefox Dev Edition 可能存在性能问题
- 🚀 **未来扩展**：已计划支持屏幕键盘几何信息等更多实时属性

---

### [今日发布 Babel 8：仅支持 ESM，放弃 ES5 默认，并提供平滑迁移路径 · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

**原文标题**: [Releasing Babel 8 today: ESM-only, drop ES5 default, and a smooth migration path · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

Babel 8 今日正式发布，这是自 Babel 7 发布 8 年后的重大更新，旨在现代化核心架构并为未来 8 年做准备。

- 📦 **仅支持 ESM**：Babel 8 现在仅以 ESM 形式发布，需要 Node.js 22、24、26 或更新版本，不再支持已终止安全的旧版 Node.js。
- 🎯 **默认不再编译到 ES5**：`@babel/preset-env` 默认不再将代码编译到 ES5，而是基于 Browserslist 的默认查询，目标为 ES2023 及更新的浏览器，用户可手动指定 targets 以编译到 ES5 或 ES3。
- 🔄 **默认输出 ESM**：`@babel/preset-env` 现在默认编译为 ESM 而非 CommonJS，但用户仍可通过配置调整。
- ❌ **弃用 `loose` 和 `spec` 选项**：这些选项被移除或弃用，建议用户迁移到更细粒度的 `assumptions` 配置，该功能自 Babel 7.13.0 起已支持。
- 🧩 **分离 polyfill 注入**：`corejs` 和 `useBuiltIns` 选项被移除，改用 `babel-plugin-polyfill-corejs3` 插件来集中控制 core-js 注入。
- 🛠️ **其他破坏性变更**：包括大量细节调整，大多数应用会受部分影响，官方提供了完整的迁移指南。
- 💡 **TypeScript 类型支持**：所有 Babel 包现在都附带 TypeScript 类型，无需额外安装 `@types/babel__*` 包。
- 📉 **资金挑战**：尽管下载量从 2018 年的 170 万周下载量增长到 2026 年的 6.51 亿，但捐赠持续下降，团队呼吁用户和公司通过 OpenCollective 或 GitHub Sponsors 支持，或参与新 ECMAScript 提案的开发。
- 🔒 **Babel 7 支持终止**：Babel 8 稳定后，Babel 7 将停止功能更新，仅提供一年安全支持（至 2027 年 6 月），特殊需求可联系团队。

---

### [Biome v2.5——500 条代码规范规则、插件代码修复及跨文件代码检查 | Biome](https://biomejs.dev/blog/biome-v2-5/)

**原文标题**: [Biome v2.5—500 Lint Rules, Plugin Code Fix, and Cross-File Linting | Biome](https://biomejs.dev/blog/biome-v2-5/)

Biome v2.5 版本发布，新增 500 条 lint 规则、插件代码修复和跨文件 lint 功能，并带来多项性能优化和新特性。

- 🎯 **突破 500 条 lint 规则**：新增`noUndeclaredClasses`和`noUnusedClasses`跨语言规则，利用模块图分析 CSS 类使用情况，并提供详细的导入树诊断信息。
- 🚫 **依赖限制规则**：新增`noRestrictedDependencies`规则，基于 e18e 倡议数据检测可替代的废弃或臃肿依赖。
- ⬆️ **73 条规则升级**：大量规则从 nursery 升级至稳定组（correctness、suspicious、style 等），其中 4 条规则更名以更准确描述功能。
- 🔧 **插件增强**：支持通过`includes`设置限定插件作用路径；插件可声明代码修复（安全/不安全），自动应用`console.log`→`console.info`等替换。
- ✏️ **格式化新选项**：新增`delimiterSpacing`选项，为 JS/CSS/JSON/GraphQL 的定界符添加空格，提升可读性（尤其对阅读障碍者友好）。
- 👀 **监视模式**：`lint`、`format`、`check`命令支持`--watch`选项，实时检测文件变更并输出诊断（仅只读模式）。
- 🔍 **转到定义**：LSP 支持跳转到变量、类型、JSX 组件、CSS 类等的定义位置，提升代码导航效率。
- ⚙️ **lint 预设配置**：新增`linter.rules.preset`选项（如`"all"`），废弃`recommended`，可通过`biome migrate --write`自动迁移。
- 📦 **升级命令**：新增`biome upgrade`命令，简化独立安装的版本升级流程。
- 📊 **简洁报告器**：新增`concise`报告器，输出精简诊断信息，适合编码代理使用以节省 token。
- ⚡ **性能与扩展**：lint 和 check 速度提升约 13%；支持`.svg`文件格式化/lint；新增`organizeImports`排序功能（bare imports、style 分组等）；支持 pnpm 目录解析；Vue 语法解析可扩展到`.html`文件。
- 🤝 **社区贡献**：欢迎参与翻译、代码贡献（新 lint 规则、解析器、LSP 功能）、财务支持（Open Collective/GitHub Sponsors/企业支持计划）。

---

### [发布 v11.17.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.17.0)

**原文标题**: [Release v11.17.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.17.0)

npm CLI v11.17.0 版本发布，包含多项新功能、错误修复和依赖更新。

- 🎯 新增 `min-release-age-exclude` 配置选项，用于更精细地控制最小发布年龄排除规则
- 🛡️ 增强 `allowScripts` 工具链和 `inBundle` 安全加固，提升脚本执行安全性
- 🐛 修复 `approve-scripts/deny-scripts` 中点号和版本化参数匹配问题，并确保 `--json` 输出有效 JSON
- 🔧 修复 `script-shell` 未传递到发布生命周期钩子的问题，以及 `allowScripts` 对本地链接目标的识别
- 📦 修复远程 tarball 的注册表路径验证，防止无效路径
- 🔍 修复 `prune`、`dedupe`、`uninstall`、`audit` 和 `link` 命令中 `allowScripts` 策略的遵守问题
- 📋 修复 `approve-scripts` 在 `ignore-scripts` 设置下未列出待处理脚本的问题
- 💡 改进全局安装时 `unreviewed-scripts` 警告，建议使用 `--allow-scripts`
- 🚫 修复 `Queryable` 设置器中禁止键的污染问题，防止原型污染攻击
- 📚 更新文档，澄清 `approve-scripts` 仅在 `-g` 时抛出 EGLOBAL，以及 `package.json` 覆盖值规范
- ⬆️ 更新多个依赖包，包括 `postcss-selector-parser`、`tinyglobby`、`tar`、`semver`、`pacote` 和 `node-gyp`

---

### [pnpm 11.7 | pnpm](https://pnpm.io/blog/releases/11.7)

**原文标题**: [pnpm 11.7 | pnpm](https://pnpm.io/blog/releases/11.7)

以下是 pnpm 11.7 版本的总结：

pnpm 11.7 新增了 frozenStore 设置以支持只读包存储、--batch 标志用于批量发布工作区、作用域特定认证令牌，并将完整解析安装委托给 pacquet。同时强化了锁文件别名处理、使多个安装路径确定性化，并修复了发布和 Windows 相关问题。

- ❄️ 新增 frozenStore 设置：支持在只读文件系统（如 Nix 存储、只读挂载或 OCI 镜像层）上运行 pnpm install，通过不可变模式打开 SQLite 索引，并抑制所有写入存储的代码路径。
- 📦 发布工作区新增 --batch 标志：通过单个 PUT 请求将工作区所有包发送到注册表，实现全有或全无的发布，注册表需支持批量发布端点。
- 🔑 作用域特定认证令牌：允许同一注册表 URL 下不同作用域使用不同令牌，通过配置 auth 键中的作用域实现，如 @org-a 和 @org-b 使用不同令牌。
- 🦀 完整解析安装委托给 pacquet：当在 configDependencies 中声明 pacquet 时，pnpm 将依赖解析也委托给它，实现端到端的单次安装过程（包括解析清单、写入锁文件和物化 node_modules）。
- 🛡️ 安全增强：拒绝锁文件中的路径遍历和保留依赖别名（如 ../../../escape、.bin、.pnpm、node_modules），防止文件写入安装根目录外或覆盖 pnpm 布局。
- 🔧 修复 pnpm publish 忽略 strictSsl: false 的问题：现在该选项会正确转发到 libnpmpublish/npm-registry-fetch。
- 🪟 Windows 修复：修复了在 Windows 上运行 pnpm add 时的回归问题，以及命令失败后因缓慢的 wmic/PowerShell 进程查找导致的挂起问题。
- 🔄 确定性改进：使共享包子节点解析确定性化，修复了锁文件输出非确定性问题，以及 pnpm dedupe --check 在 CI 中间歇性失败的问题。
- ⚡ 性能优化：通过并发运行锁文件验证与获取和链接，加速了冻结锁文件的 pnpm install，同时依赖生命周期脚本仍会等待验证完成。
- 🔧 其他修复：包括 git 依赖路径保持、npm_config_* 环境变量保留、pnpm setup 不再提示批准构建脚本、304 响应更新缓存 mtime 等。

---

### [GitHub - gajus/zod-compiler: 在构建时将 Zod 模式编译为零开销的验证函数。支持 Vite、webpack、esbuild、Rollup 等](https://github.com/gajus/zod-compiler)

**原文标题**: [GitHub - gajus/zod-compiler: Compile Zod schemas into zero-overhead validation functions at build time. Works with Vite, webpack, esbuild, Rollup, etc · GitHub](https://github.com/gajus/zod-compiler)

zod-compiler 是一个构建时工具，可将 Zod 模式编译为零开销的验证函数，实现 2-75 倍的性能提升，同时无需更改现有代码。

- 🚀 **核心功能**：在构建时自动检测并编译所有导出的 Zod 模式，生成优化验证器，支持 `parse`、`safeParse` 和 `.is()` 类型守卫
- ⚙️ **多种使用模式**：提供自动模式（零代码改动）、显式 `compile()` 包装和 CLI 生成三种方式，适配不同项目需求
- 🔧 **广泛构建工具支持**：兼容 Vite、webpack、esbuild、Rollup、Rolldown、rspack、Bun、Farm 等主流构建工具
- 📈 **显著性能优势**：基准测试显示，简单字符串验证快 1.1 倍，大型对象验证快 73 倍，递归模式验证快 33 倍
- 🧩 **完整模式支持**：编译所有标准 Zod 类型（string、number、object、array、union 等），仅 transform/refine 带捕获变量时回退
- 🏗️ **模式提升优化**：自动将函数内定义的 Zod 模式提升到模块作用域，避免每次调用重复构建，大幅减少开销
- 📦 **零开销验证架构**：采用两阶段验证器——快速路径（单表达式链，零分配）和慢速路径（仅失败时收集错误）
- 🔒 **安全与兼容性**：保留原始 Zod 对象身份，兼容 tRPC、Hono、React Hook Form 等框架，支持 Standard Schema
- 🛠️ **诊断工具**：提供 `npx zod-compiler check` 命令分析模式编译覆盖率、快速路径资格和优化建议
- 📏 **行为差异**：默认保留未知键（可通过 `stripUnknownKeys` 选项匹配 Zod 行为），记录跳过符号键和非可枚举键

---

### [发布 v1.61.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.61.0)

**原文标题**: [Release v1.61.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.61.0)

Playwright v1.61.0 发布，新增多项功能与改进。

- 🔑 新增 WebAuthn passkeys 支持，可通过 `browserContext.credentials` 模拟虚拟验证器，无需实体硬件即可注册和应答 passkey。
- 🗃️ 引入 Web Storage API，通过 `page.localStorage` 和 `page.sessionStorage` 读写当前源的存储数据。
- 🌐 网络 API 新增 `apiResponse.securityDetails()` 和 `apiResponse.serverAddr()`，镜像浏览器端的响应安全详情和服务器地址。
- 🖥️ 浏览器和屏幕录制新增 `artifactsDir` 选项控制工件存储位置，`cursor` 选项控制指针动作光标装饰，`onFrame` 回调增加时间戳。
- 🧪 测试运行器扩展视频模式支持（如 `on-all-retries`），新增 `expect.soft.poll()`、`fullConfig.argv`、`fullConfig.failOnFlakyTests`，以及 `-G` 命令行缩写。
- 🛠️ 其他改进包括支持 Ubuntu 26.04，HAR 和跟踪记录包含 WebSocket 请求。
- 🌐 浏览器版本更新：Chromium 149.0.7827.55、Firefox 151.0、WebKit 26.5，并测试了 Chrome 149 和 Edge 149。

---

