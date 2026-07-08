### [宣布 Vite+ Beta 版 | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-beta)

**原文标题**: [Announcing Vite+ Beta | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-beta)

Vite+ 测试版发布，统一了 Web 开发工具链，提供一致的工作流程。

- 🚀 Vite+ 测试版发布，统一了运行时、包管理器和前端工具，提供一致的工作流程。
- ⚙️ 核心命令包括 `vp dev`、`vp check`、`vp test`、`vp build`、`vp pack` 和 `vp run`，覆盖开发、检查、测试、构建和打包。
- 🔧 工具链整合了 Vite、Vitest、Rolldown、tsdown、Oxlint 和 Oxfmt，并内置任务运行器。
- 🎯 专注于团队和大型代码库，确保工具版本一致、配置易共享，并简化新成员设置。
- 📦 不取代 Vite 生态系统，Vite 插件和包管理器仍可继续使用。
- 📈 自 Alpha 版以来，已发布多个版本，合并了 500 多个拉取请求，改进了缓存、迁移、企业功能和跨平台支持。
- 🌐 已被超过 1,300 个公共仓库采用，包括 Dify、critical、BlockNote 等项目。
- 🗺️ 1.0 路线图包括远程缓存、GitLab CI/CD 支持、框架兼容性改进、更多迁移目标和文档优化。
- 📥 可通过 `curl` 或 `powershell` 安装，并使用 `vp create` 或 `vp migrate` 开始使用。

---

### [Vite | 下一代前端工具](https://vite.dev/)

**原文标题**: [Vite | Next Generation Frontend Tooling](https://vite.dev/)

Vite 是一款极速的前端构建工具，为下一代 Web 应用提供强大支持，深受社区和框架团队信赖。

- ⚡ **极速开发体验**：通过原生 ESM 实现即时服务器启动和闪电般的热模块替换（HMR），让开发过程更愉悦。
- 🛠️ **开箱即用的丰富功能**：内置对 TypeScript、JSX、CSS、WebAssembly 等的支持，通过插件轻松扩展。
- 🚀 **优化构建**：利用 Rolldown 实现高级树摇、内置压缩和精细分块控制。
- 🔌 **灵活的插件系统**：基于 Rollup 设计，并添加 Vite 特有选项，支持完全类型化的 API 和一流 SSR 支持。
- 🤝 **生态系统集成**：持续集成测试确保稳定性，为 SolidJS、Svelte 等众多框架提供动力。
- ❤️ **社区热爱**：拥有 80k+ GitHub 星标和 80m+ 周 NPM 下载量，被开发者誉为“JavaScript 联合国”。
- 💰 **免费开源**：采用 MIT 许可，由贡献者和赞助商支持，始终免费。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=primary)

Meticulous 是一款自动化、穷尽式且确定性的测试工具，能让开发者在零额外工作量的情况下，以 AI 生成的速度交付代码，并确保测试套件始终与应用程序同步演进。

- 🚀 **零开发者努力的穷尽验证**：自动化、穷尽式、确定性测试，让开发者无需再编写、修复或维护测试用例。
- 🤖 **AI 驱动的测试套件自动演进**：通过记录开发中的交互，AI 引擎生成覆盖所有代码分支和用户流程的测试，并随应用变化自动增删测试。
- 🔍 **PR 合并前可视化影响**：在拉取请求阶段即可查看对用户工作流的全部影响，通过模拟后端响应避免假阳性。
- ⚡ **极速迭代与无碎片测试**：大幅提升交付速度，从 Chromium 底层构建确定性调度引擎，彻底消除碎片测试，实现闪电般快速执行。
- 🏢 **企业级信任与集成**：受 Dropbox、Notion、Engine 等组织信赖，支持 NextJS、React、Vue、Angular 等主流框架，可补充或替代现有测试套件。
- 🔒 **安全与可扩展性**：测试在计算集群上高度并行化，1000 个屏幕测试可在 120 秒内完成，并提供安全集成文档。

---

### [ECMAScript 2026 新特性 | pawelgrzybek.com](https://pawelgrzybek.com/whats-new-in-ecmascript-2026/)

**原文标题**: [What's new in ECMAScript 2026 | pawelgrzybek.com](https://pawelgrzybek.com/whats-new-in-ecmascript-2026/)

ECMAScript 2026 新增了多项实用功能，包括异步数组转换、错误检测、精确数学运算、Base64/Hex 转换、迭代器组合、JSON 源文本访问以及 Map 快捷操作。

- 📜 **Array.fromAsync**：新增异步数组转换方法，可轻松将异步迭代器或生成 Promise 的同步生成器转为数组。
- 🛡️ **Error.isError**：提供更安全的错误类型检测方法，替代 `instanceof Error`，避免误判。
- ➕ **Math.sumPrecise**：精确求和函数，解决浮点数精度问题，避免 `Array.reduce` 的常见陷阱。
- 🔢 **Uint8Array to/from Base64 和 Hex**：内置 Base64 和十六进制转换方法，减少外部依赖。
- 🔗 **Iterator Sequencing**：新增 `Iterator.concat` 方法，简化多个迭代器的顺序组合，并支持插入中间值。
- 📝 **JSON.parse source text access**：`JSON.parse` 的 reviver 回调新增 `source` 参数，支持精确还原 BigInt 等原始值；`JSON.stringify` 配合 `JSON.rawJSON` 避免序列化错误。
- 🗂️ **Upsert**：Map/WeakMap 新增 `getOrInsert` 方法，一键实现“存在则获取，不存在则插入”，减少冗余代码。

---

### [ECMA-262 - Ecma 国际](https://ecma-international.org/publications-and-standards/standards/ecma-262/)

**原文标题**: [ECMA-262 - Ecma International](https://ecma-international.org/publications-and-standards/standards/ecma-262/)

ECMAScript 2026 第 17 版规范正式发布，定义了通用编程语言标准，提供 HTML 和 PDF 版本，并包含历史版本存档。

- 📄 ECMAScript 2026 (第 17 版) 规范正式发布，标准编号 ECMA-262
- 🌐 规范以 HTML 版本为正式标准，PDF 版仅供打印参考
- 🏛️ 本版遵循 Ecma RF 专利政策制定
- ❌ 第 4 版标准号曾保留但未正式发布，因此不存在
- 🔗 最新草案可在 tc39.es/ecma262 获取，提交 bug 前请确认仍存在于最新版
- 🐛 问题反馈地址：github.com/tc39/ecma262#ecmascript
- 📚 提供从第 1 版 (1997) 到第 16 版 (2025) 的完整历史版本存档下载

---

### [JS1024 - 年度 JavaScript 与着色器代码高尔夫竞赛 - 主页](https://js1024.fun/#2026)

**原文标题**: [JS1024 - Annual Javascript & Shader Code Golfing Competition - Main Page](https://js1024.fun/#2026)

JS1024 是一年一度的 JavaScript 和 GLSL 编程竞赛，参赛者需在 1024 字节内创作程序，主题为“DREAMING”，比赛从 7 月 1 日开始，7 月 19 日截止提交，8 月 1 日结束评分，8 月 5 日左右公布结果。

- 🎯 竞赛要求：源代码不超过 1 KiB，禁止恶意代码、外部文件或提取用户数据，参与者需用密钥匿名评分。
- 📅 时间表：7 月 1 日主题公布并开放提交，7 月 19 日截止，8 月 1 日评分结束，8 月 5 日左右公布获奖者。
- 🖥️ 演示类别：包括经典画布模式、p5.js 演示（需使用 p5js 库）、着色器演示（WebGL1/GLSL ES 1.0，16:9 比例）和无 shim 的空白 HTML 文件。
- 🔧 工具资源：提供多种代码压缩工具（如 Terser、Babel、GLSL Minifier）和教程指南（如 JavaScript 高尔夫技巧、WebGL 指南）。
- 🏆 评分机制：参与者用密钥评分其他项目，最高分获第一名，结果通过公开投票决定。
- ❤️ 赞助与社区：由 Frank Force、Evan Hahn 等赞助，类似竞赛包括 js1k.com、js13kgames.com 等。

---

### [Ant1k 攻击 ~ js1024](https://js1024.fun/demos/2025/11/bar)

**原文标题**: [Ant1k Attack ~ js1024](https://js1024.fun/demos/2025/11/bar)

概述总结
蚂蚁入侵！点击挤压它们。

- 🐜 游戏主题：蚂蚁入侵，玩家需要点击挤压蚂蚁。
- 🖱️ 操作方式：通过点击来消灭蚂蚁。
- 🎯 游戏目标：阻止蚂蚁的入侵。

---

### [GitHub - tc39/proposal-error-code-property · GitHub](https://github.com/tc39/proposal-error-code-property)

**原文标题**: [GitHub - tc39/proposal-error-code-property · GitHub](https://github.com/tc39/proposal-error-code-property)

该提案旨在为 ECMAScript 错误对象标准化一个 `code` 属性，以提供机器可读的错误标识符，从而改善错误处理、跨环境传输和生态一致性。

- 📜 **核心用例**：允许程序通过 `e.code === 'ERR_CONNECTION_REFUSED'` 等字符串代码精确处理错误，避免依赖易变的消息文本。
- 🔒 **稳定合约**：错误代码作为文档化、版本化的标识符，提供跨版本的稳定接口，而错误消息可能随引擎或版本变化。
- 🌐 **跨环境识别**：字符串 `.code` 属性可跨越结构化克隆、序列化和跨 Realm 传输，克服 `instanceof` 的局限性。
- 📊 **改进遥测**：在监控系统中按 `.code` 聚合错误比按消息聚合更可靠，因为消息在不同引擎和版本间存在差异。
- 🌍 **支持国际化**：稳定的代码允许错误消息被本地化或映射为用户友好文本，同时保持机器可读性。
- 🤝 **生态对齐**：标准化一个生态已广泛使用的属性（如 Node.js 的 `ERR_*` 代码），可减少碎片化并为库作者提供推荐模式。
- 🛠️ **提升开发者体验**：文档和工具可引用错误代码（如 `ERR_INVALID_ARG_TYPE`），开发者能可靠搜索到定义性文档。
- 🚫 **范围外**：本提案不涉及定义 TC-39 规范自身的错误代码或命名空间，这些内容留待后续提案处理。
- 📚 **生态先例**：Node.js、Deno、Bun、Cloudflare Workers 等运行时，以及 axios、Firebase、Stripe 等库已广泛采用字符串 `.code` 属性。
- 🧩 **设计细节**：通过扩展 Error 构造函数的 options bag（类似 `cause`）接受 `code`，属性可为任意类型，默认不存在，可写可配置，不可枚举。
- ❓ **FAQ 要点**：标准化属性而非值，避免“字符串类型编程”问题；不定义新错误分类法；不强制使用字符串，但字符串是生态主流；符号代码会牺牲序列化和可读性；错误子类无法解决跨 Realm 和结构化克隆问题。

---

### [GitHub - cloudflare/vinext: 重新实现 Next.js API 接口的 Vite 插件——可部署至任何环境 · GitHub](https://github.com/cloudflare/vinext)

**原文标题**: [GitHub - cloudflare/vinext: Vite plugin that reimplements the Next.js API surface — deploy anywhere · GitHub](https://github.com/cloudflare/vinext)

vinext 是一个在 Vite 上重构 Next.js API 的 Vite 插件，主要面向 Cloudflare Workers 部署，支持 App Router 和 Pages Router。

- 🚀 **核心能力**：支持 App Router、Pages Router、React 服务端组件、服务端操作、中间件、ISR 和静态导出，覆盖约 94% 的 Next.js 16 API。
- ☁️ **主要部署目标**：原生支持 Cloudflare Workers，提供 `@vinext/cloudflare deploy` 一键部署命令，并支持 D1、R2、KV 等绑定。
- ⚡ **性能优势**：相比 Next.js/Turbopack，构建速度更快，客户端包体积更小（得益于 Rolldown 的树摇优化和更轻量的运行时）。
- 🛠️ **迁移工具**：提供 `vinext init` 和 `vinext check` 命令，可自动将现有 Next.js 项目迁移到 vinext，且不破坏原有配置。
- 🌐 **多平台支持**：通过 Nitro 插件可部署到 Vercel、Netlify、AWS、Deno Deploy 等平台。
- 📦 **模块兼容性**：所有 `next/*` 导入均有对应实现，包括 `next/link`、`next/image`、`next/navigation`、`next/headers` 等。
- 🧪 **测试覆盖**：拥有 1700+ Vitest 单元测试和 380 Playwright E2E 测试，包含从 Next.js 测试套件移植的用例。
- 🎯 **设计原则**：追求 95%+ 实际应用的兼容性，不支持 Vercel 专有功能和已弃用的 API，专注于最新 Next.js 16.x 版本。
- 🔄 **增量采用**：可逐步替换，先引入插件，修复兼容性问题，再部署。

---

### [发布 v6.0.0 · webpack/webpack-dev-server · GitHub](https://github.com/webpack/webpack-dev-server/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · webpack/webpack-dev-server · GitHub](https://github.com/webpack/webpack-dev-server/releases/tag/v6.0.0)

此版本为 webpack-dev-server v6.0.0 主要版本更新，引入了多项重大变更、新功能及依赖升级。

- 🚀 **重大变更**：升级 Express 至 v5，webpack 依赖范围提升至 ^5.101.0，并放弃对 Node.js < 22.15.0 的支持。
- 📦 **模块格式**：源码转为原生 ES 模块，通过 exports 字段同时提供 ESM 和 CommonJS 构建。
- 🗑️ **移除功能**：移除 CLI 标志、internalIP 方法、SockJS 支持、spdy 依赖及代理的 bypass 选项。
- 🔄 **依赖更新**：http-proxy-middleware 升级至 v4，webpack-dev-middleware 升级至 v8，并同步 originalUrl。
- 🧩 **插件支持**：新增插件功能，可集成到 webpack 编译器生命周期，支持多编译器设置。
- 🔒 **安全改进**：拒绝跨站请求至 open-editor 和 invalidate 端点，要求同源验证。
- 🛠️ **其他优化**：启用 HTTP/2 压缩中间件，使用原生 ANSI 样式，chokidar 升级至 v5，支持 glob 模式。

---

### [GitHub - sverweij/dependency-cruiser：验证并可视化依赖关系。你的规则。JavaScript、TypeScript、CoffeeScript。ES6、CommonJS、AMD。](https://github.com/sverweij/dependency-cruiser)

**原文标题**: [GitHub - sverweij/dependency-cruiser: Validate and visualize dependencies. Your rules. JavaScript, TypeScript, CoffeeScript. ES6, CommonJS, AMD. · GitHub](https://github.com/sverweij/dependency-cruiser)

dependency-cruiser 是一个用于验证和可视化 JavaScript、TypeScript 等项目依赖关系的工具，支持自定义规则和多种输出格式。

- 📦 **功能概述**：扫描项目依赖，基于自定义规则进行验证，并报告违规情况，同时可生成依赖关系图。
- 🛠️ **安装与配置**：通过 `npm install --save-dev dependency-cruiser` 安装，运行 `npx depcruise --init` 生成配置文件。
- 🎨 **可视化输出**：支持生成 SVG、Mermaid、HTML、CSV 等多种格式的依赖图，方便展示和理解项目结构。
- ✅ **规则验证**：内置检测循环依赖、缺失依赖、孤儿模块等规则，用户可自定义规则（如禁止测试文件夹外的代码依赖测试文件夹）。
- 📊 **报告方式**：支持命令行文本报告（类似 ESLint 格式）、图形报告和自包含 HTML 报告。
- 🌐 **多语言支持**：支持 JavaScript、TypeScript、CoffeeScript、Vue、Svelte 等，以及 Webpack 别名和模块。
- 📚 **文档丰富**：提供详细的命令行参考、规则编写教程、选项参考和常见问题解答。
- 🏆 **开源社区**：基于 MIT 许可证，拥有活跃的贡献者和 6.9k 星标，持续更新。

---

### [发布 v11.18.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.18.0)

**原文标题**: [Release v11.18.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.18.0)

npm CLI v11.18.0 发布，重点升级了链接安装策略并修复多项问题。

- 🚀 将链接安装策略从实验性升级为稳定版，并扩展了 replace-registry-host 的 URL 前缀匹配功能
- 🛠️ 新增 install-scripts 命令命名空间，并清理未使用的 allowScripts 条目，提升脚本管理效率
- ⚠️ 当最小发布年龄阻止审计修复时发出警告，增强安全审计的透明度
- 🐛 修复多项错误，包括 SBOM 生成中 URL 编码问题、令牌列表参数输出、工作区依赖标记等
- 📦 更新依赖项：undici、brace-expansion、tar、semver 和 npm-profile 至最新版本
- 📚 文档建议使用 install-strategy=linked 来捕获幻影依赖，提高项目可靠性
- 🔧 工作区组件（如 arborist、config、libnpmexec）同步更新，修复链接策略下的各种边缘情况

---

### [pnpm 11.10 | pnpm](https://pnpm.io/blog/releases/11.10)

**原文标题**: [pnpm 11.10 | pnpm](https://pnpm.io/blog/releases/11.10)

pnpm 11.10 版本发布，新增了 CI 友好的认证设置、新命令，并改进了性能与安全性。

- 🔐 新增 `_auth` 设置，支持通过环境变量或全局配置文件进行结构化注册表认证，避免 CI 环境变量名被丢弃的问题
- ⬆️ `pnpm self-update` 现可安装 Rust 版 pnpm v12，无 Node.js 启动开销
- 📍 新增 `pnpm prefix` 命令，打印当前包或全局前缀目录
- 🐛 新增 `pnpm issues` 命令，作为 `pnpm bugs` 的别名，打开包问题追踪器
- ⚡ 修复 `pnpm up` 误更新无关包的问题，提升准确性
- 🚀 针对忽略缩写元数据的注册表，加速解析并减少内存使用
- 🛡️ 强化全局包管理、`pnpm deploy` 和 `pnpm pack-app` 的安全性
- 🔧 多项补丁修复，包括原型污染风险、依赖解析顺序、shell 补全等

---

### [</> htmx ~ 与 AI 协作：一个具体示例](https://htmx.org/essays/working-with-ai/)

**原文标题**: [</> htmx ~ Working With AI: A Concrete Example](https://htmx.org/essays/working-with-ai/)

### 概述摘要
本文通过一个具体的 bug 修复案例，展示了 AI 在软件开发中的优势与局限，强调了人类开发者保持主导地位的重要性。

- 🧠 **AI 擅长调查与测试**：在分析 bug 根源和生成测试用例方面表现优异，能显著提升效率。
- ⚠️ **AI 解决方案易引入技术债**：AI 提出的修复方案可能过于取巧或复杂，需人工审查以避免长期问题。
- 🔧 **人类经验的关键作用**：熟悉代码架构的开发者能结合 AI 工具，提出更简洁、更符合系统设计的解决方案。
- 🎓 **避免“学徒陷阱”**：盲目接受 AI 建议可能导致代码质量下降，需保持批判性思维和领域知识。
- 👴 **AI 对年长开发者的价值**：弥补记忆力和精力下降的短板，帮助快速理解代码并生成更全面的测试。
- 🌱 **需警惕智力退化风险**：过度依赖 AI 可能加速认知能力衰退，需平衡工具使用与自主思考。

---

### [</> htmx - HTML 的高能工具](https://htmx.org/)

**原文标题**: [</> htmx - high power tools for html](https://htmx.org/)

htmx 是一款轻量级、无依赖的 HTML 扩展工具，通过属性直接在 HTML 中实现 AJAX、CSS 过渡、WebSocket 和服务器推送事件，可减少 67% 的代码量（相比 React），并支持现代用户界面开发。

- 🚀 htmx v4 正在积极开发中，已进入 Beta 阶段，目标于 2026 年夏季发布
- 🔧 通过属性（如 hx-post、hx-swap）在 HTML 中直接实现 AJAX 请求和动态内容替换
- 📦 体积小巧（约 16k min.gz'd），无外部依赖，可扩展性强
- 💡 打破传统限制：允许任何元素发起 HTTP 请求，支持多种事件和方法，实现局部屏幕更新
- ⚡ 快速集成：通过 CDN 引入脚本即可使用，示例中按钮点击即发送 POST 请求并替换自身
- 📚 官方推荐阅读《Hypermedia Systems》书籍，深入学习超媒体驱动应用开发
- 🤝 开发支持通过 GitHub Sponsors 进行，感谢所有赞助者（包括白金和银牌赞助商）
- 📌 htmx 2.x 已放弃 IE 支持，如需兼容 IE 可继续使用 1.x 版本

---

### [前端中的 W-Key：技术与产品的协同 | 奖章](https://medal.tv/blog/posts/w-key-in-frontend-synergizing-technology-and-product)

**原文标题**: [W-Key in Frontend: Synergizing Technology and Product | Medal](https://medal.tv/blog/posts/w-key-in-frontend-synergizing-technology-and-product)

本文介绍了 Medal 前端团队如何通过系统性技术重构，将原本臃肿、低效的前端代码库优化为高性能、易维护的现代化系统，最终实现渲染包从约 50MB 缩减至 2.7MB 的显著成果。

- 🧩 **组件问题诊断**：指出旧组件存在过多 props、职责不清、性能差等问题，阻碍开发迭代
- 🔧 **宏观优化策略**：从开发者体验入手，采用 PNPM 和 Vite 实现热模块替换，提升本地开发效率
- 🗑️ **代码清理革命**：利用 AI 工具系统清理死代码，规范导入路径，删除冗余文件
- 🚀 **构建系统统一**：将生产构建从 Rollup 迁移至 Vite，实现单构建系统，便于代码分割
- 📦 **包体积大幅缩减**：通过移除组件桶文件、外部化音频文件、动态导入翻译文件等操作，将渲染包从约 50MB 降至 2.7MB
- 🎨 **组件库现代化**：采用 Tailwind 和 Shadcn（Radix UI）替换旧组件，配合 ESLint 规则逐步淘汰遗留代码
- ⚡ **持续性能优化**：从 Radix UI 迁移至 Base UI，QA 团队已感知到应用响应速度提升
- 🏆 **最终成果**：开发效率显著提升，团队可一天内搭建完整页面，功能交付速度大幅提高

---

### [将实时 HDR 反射流式传输到每台设备 | Miris](https://www.miris.com/blog/streaming-real-time-hdr-reflections-to-the-web?utm_source=web_referral&mrls=web_referral&utm_medium=public_relations&mrlc=public_relations&utm_campaign=raz-pr&utm_content=sign_up&prg=scale&utm_term=javascript&dp=dp)

**原文标题**: [Streaming real-time HDR reflections to every device| Miris](https://www.miris.com/blog/streaming-real-time-hdr-reflections-to-the-web?utm_source=web_referral&mrls=web_referral&utm_medium=public_relations&mrlc=public_relations&utm_campaign=raz-pr&utm_content=sign_up&prg=scale&utm_term=javascript&dp=dp)

Miris 团队成功将 1.2GB 的高保真汽车 3D 模型，通过空间串流技术，实时传输到桌面浏览器、安卓平板和 Apple Vision Pro 等不同设备，并实现了 HDR 级别的实时反射效果，无需为每个设备单独优化或使用云端 GPU。

- 🚗 **一次上传，多端串流**：一个 1.2GB 的汽车源资产，经过 Miris 平台一次处理，即可自适应串流到各种设备（如头显、平板、手机），无需为每个平台重建模型。
- ✨ **实时 HDR 反射**：汽车漆面的反射是实时、视角依赖的，会随观察角度和环境光变化，达到了以往只有离线渲染或云端 GPU 才能实现的保真度。
- 📱 **设备端渲染**：所有图形渲染都在用户自己的设备上完成，不依赖云端 GPU，因此成本不会随用户数量线性增长。
- 🧩 **WebXR 支持**：基于 WebXR 标准，用户无需安装应用，直接在浏览器中即可获得沉浸式体验，覆盖桌面、平板和头显。
- 🎨 **材质保真度挑战**：汽车漆面的高光反射是图形学中最难处理的部分之一，Miris 通过上游预处理和自适应串流，在设备性能预算内保留了关键反射细节。
- ⚖️ **打破保真度与覆盖面的取舍**：以往的方案要么（像素串流）成本高，要么（glTF 网页查看器）画质差。Miris 的空间串流技术同时解决了成本和画质问题。
- 💡 **OpenUSD 原生支持**：Miris 平台原生支持 OpenUSD 格式，一次素材处理即可输出到 WebXR、Unity 等多个平台。

---

### [不同的水合与渲染策略——Nechu Dan](https://neciudan.dev/hydration-and-rendering-strategies)

**原文标题**: [Different hydration and rendering strategies — Neciu Dan](https://neciudan.dev/hydration-and-rendering-strategies)

以下是您提供的文章内容摘要：

本文探讨了不同的水合与渲染策略，旨在缩小网页“看起来就绪”与“实际可交互”之间的差距。

- 📄 **静态生成 (SSG)**：在构建时预渲染 HTML，从 CDN 提供，速度极快但内容可能过时。增量静态再生 (ISR) 可在后台定期或按需更新内容。
- 🖥️ **客户端渲染 (CSR)**：服务器发送空壳 HTML，浏览器下载并执行 JavaScript 构建所有 UI。首次加载慢，对 SEO 不友好。
- 🖨️ **服务端渲染 (SSR)**：服务器渲染完整 HTML，浏览器下载 JavaScript 并“水合”使其可交互。解决了白屏和 SEO 问题，但会重复工作，且水合期间页面不可用。
- 🚰 **流式 SSR**：使用`Suspense`将 HTML 分块流式传输，允许页面部分内容先显示，用户无需等待最慢的组件。选择性水合可优先处理用户正在交互的区域。
- 🏝️ **岛屿架构**：页面主体为静态 HTML，仅标记需要交互的部分（岛屿）独立水合。适合内容为主的网站，可大幅减少 JavaScript 体积。
- ⚛️ **React 服务端组件 (RSC)**：组件仅在服务器运行，其代码不发送到客户端。客户端仅下载标记为`"use client"`的交互组件，显著减小包体积。
- 🔄 **TanStack Start**：采用客户端优先、按需选择的方式使用 RSC，将其视为可通过 HTTP 获取的数据流，适合在现有 SPA 中逐步引入。
- ⚡ **细粒度响应式**：SolidJS 和 Svelte 等框架无虚拟 DOM，组件只运行一次以建立响应式图，状态变化时仅更新具体 DOM 节点，水合成本极低。
- 🚀 **可恢复性**：Qwik 将框架执行状态序列化到 HTML 中，客户端不进行水合，而是从服务器暂停的地方“恢复”。代码仅在交互发生时按需加载。
- 🧭 **Next.js 16.3 即时导航**：通过部分预渲染和客户端缓存可复用壳，实现类似 SPA 的即时点击导航体验，同时保留服务端模型优势。
- ✅ **如何选择**：内容网站首选 SSG 和岛屿架构；应用首选带 RSC 的 Next.js；性能瓶颈时考虑细粒度响应式或可恢复性；登录页后的应用可用 CSR。

---

### [无需 GPU 的 WebGL — Microlink 博客](https://microlink.io/blog/webgl-without-a-gpu)

**原文标题**: [WebGL without a GPU — Microlink Blog](https://microlink.io/blog/webgl-without-a-gpu)

通过将 Chrome 的 WebGL 渲染后端从 SwiftShader 切换到 Mesa llvmpipe，在无 GPU 服务器上实现 4 倍性能提升，将 3D 页面截图时间从约 24 秒降至约 6 秒。

- 🚀 **核心优化**：将 Chrome 标志从`--use-angle=swiftshader`改为`--use-angle=gl`，一行代码实现 4 倍加速
- 🖥️ **无 GPU 环境**：服务器无显卡，通过 CPU 模拟 GPU，llvmpipe 的 JIT 编译和并行处理比 SwiftShader 快 4 倍
- ⚙️ **关键配置**：需要虚拟显示（Xvfb）和从源码编译的 Mesa，避免静默降级为 2D 平面渲染
- 📊 **性能数据**：孤立测试从~24s 降至~6s，生产负载下从~24s 降至 7-14s，超时错误完全消除
- 🔍 **验证机制**：通过`browserless.report()`实时检测渲染器类型，CI 自动断言确保使用 llvmpipe 而非 SwiftShader
- 🛠️ **构建优化**：多阶段 Docker 构建，仅复制 Mesa 编译产物，镜像从 4.5GB 降至 2.65GB
- ⚠️ **注意事项**：避免使用`--disable-gpu`和`--in-process-gpu`标志，它们会破坏 llvmpipe 路径
- 🎯 **剩余挑战**：复杂着色器页面可能因首帧渲染竞争而显示黑色，需通过捕获时机控制解决

---

### [Tejas 的博客 - TypeScript 中的分布式条件类型](https://tejasbubane.github.io/posts/2026-07-04-typescript-distributive-union-types/)

**原文标题**: [Tejas' Blog - Distributive Conditional Types in TypeScript](https://tejasbubane.github.io/posts/2026-07-04-typescript-distributive-union-types/)

本文介绍了 TypeScript 中联合类型、泛型、条件类型及其分配条件类型的核心概念与应用场景。

- 🔗 **联合类型**：通过`|`符号组合多种类型，如`StringOrNumber`或`UserRole`，支持字面量类型。
- ⚙️ **泛型**：使用泛型创建可复用的类型模板，如`ApiResponse<T>`，避免重复定义。
- 🔀 **条件类型**：根据类型条件动态生成类型，如`Permissions<T>`根据是否为 Admin 返回不同权限类型。
- 🔄 **分配条件类型**：条件类型自动遍历联合类型的每个成员，实现类型转换，如将`User | Admin`转换为`User[] | Admin[]`。
- 🧹 **联合过滤**：利用分配条件类型的`never`分支过滤联合类型，如从`UserRole`中提取`"admin" | "superadmin"`。
- 📌 **实际应用**：通过`T extends unknown ? T[] : never`实现联合类型到数组联合的转换，保持类型安全。

---

### [Wordgard](https://wordgard.net/)

**原文标题**: [Wordgard](https://wordgard.net/)

Wordgard 是一个基于语义的富文本编辑器系统，提供强大编程接口，支持自定义文档结构和协作编辑。

- 🌱 核心概念：Wordgard 是“文字花园”，一个开源 JavaScript 库，用于构建内容编辑器，强调语义而非自由格式 HTML。
- 🎯 主要特点：提供强大编程接口，适合构建复杂、定制化的编辑器，是良好基础框架。
- 📐 Schema 基础：精确定义文档结构，可创建自定义文档元素，确保内容一致性。
- 🚀 高级 API：编辑器编程接口经过精心设计，具有通用性和多功能性。
- 🧩 模块化设计：大多数功能以扩展形式实现，可替换或修改，灵活适应需求。
- ♿ 无障碍支持：适用于屏幕阅读器、仅键盘用户和移动设备，支持 UI 国际化。
- ↔️ 双向书写：内容与界面均感知方向，支持双向文本和从右到左文档。
- 🏗️ 结构化内容：文档树支持表格、嵌套列表、带标题图形和自定义结构。
- ⚙️ 函数式风格：系统大部分采用函数式编程，提高清晰度和可测试性。
- 👥 协作编辑：支持多用户同时编辑同一文档，合并并发修改。
- 📜 开源许可：基于 MIT 许可开源，开发于 code.haverbeke.berlin，欢迎报告错误，但不接受拉取请求。
- 💼 商业使用：若商业使用，期望社会性支持维护，但无法律义务。
- 📞 社区互动：项目讨论和提问最佳在论坛，错误报告通过问题跟踪器。

---

### [《Eloquent JavaScript》](https://eloquentjavascript.net/)

**原文标题**: [Eloquent JavaScript](https://eloquentjavascript.net/)

《Eloquent JavaScript》第四版（2024 年）是一本关于 JavaScript、编程和数字世界奥秘的书籍，由 Marijn Haverbeke 撰写，可在网上免费阅读或购买纸质版。内容涵盖语言基础、浏览器编程和 Node.js 三部分，配有插图，并遵循知识共享许可协议。

- 📘 书籍介绍：由 Marijn Haverbeke 撰写，第四版（2024 年），提供在线阅读和纸质版购买
- 🎨 插图与许可：多位艺术家贡献插图，采用知识共享署名 - 非商业性许可，代码遵循 MIT 许可
- 📚 内容结构：分为语言（值、函数、对象等）、浏览器（DOM、事件、Canvas 等）和 Node.js 三部分
- 🎮 项目示例：包含机器人、平台游戏、像素艺术编辑器等实践项目
- 🌐 多格式与翻译：提供 PDF、EPUB、MOBI 格式，支持西班牙语、阿拉伯语、波斯语等多语言翻译
- 📖 附加资源：包含代码沙箱、练习解答、勘误表及前三版链接

---

### [ProseMirror](https://prosemirror.net/)

**原文标题**: [ProseMirror](https://prosemirror.net/)

ProseMirror 是一款介于结构化文档与经典 WYSIWYG 编辑器之间的富文本编辑框架，提供可定制的文档结构和协作编辑功能。

- 📝 核心定位：实现 WYSIWYG 编辑界面，支持比纯 HTML 更约束的结构化文档，可自定义文档形状和结构
- 🤝 协作编辑：原生支持多人实时协作编辑，功能稳定可靠
- 🧩 可扩展模式：通过文档模式自定义编辑结构，无需从头编写编辑器
- 🔧 模块化架构：按需加载代码，可替换系统组件
- 🔌 插件系统：轻松扩展功能，支持打包自定义扩展
- ⚛️ 函数式设计：采用不可变架构，易于集成现代 Web 应用
- 🎯 无偏见核心：库小巧通用，可构建不同类型的编辑器
- 💰 开源商业友好：允许商业使用，但期望盈利用户资助维护
- 🌐 开发与支持：在 Forgejo 开发，通过 npm 安装，支持主流浏览器和 IE11
- 🗣️ 社区参与：通过论坛讨论、问题跟踪器报告 bug，遵循行为准则
- 🏢 赞助支持：初始开发由 414 个个人/组织众筹，持续开发由公司支持

---

### [试试 Wordgard](https://wordgard.net/try/)

**原文标题**: [Try Wordgard](https://wordgard.net/try/)

概述总结
- 🖥️ 使用 Wordgard 编写程序定义编辑器，并查看运行结果，便于测试或分享脚本以解释问题或报告错误。
- ▶️ 按 Ctrl-Enter 运行当前代码，结果会在“输出”选项卡的`<iframe>`框中显示。
- 📤 代码可通过“分享”功能进行传播。
- 📝 模块可直接按名称导入，其他导入需使用 URL。
- ⚠️ 错误或控制台日志可在“日志”选项卡中查看。

---

### [基本编辑器示例](https://wordgard.net/examples/basic/)

**原文标题**: [Basic Editor Example](https://wordgard.net/examples/basic/)

### 概述总结
本文介绍了 Wordgard 编辑器库的基础用法，包括创建编辑器、配置扩展、管理文档状态以及加载新文档的方法。

- 📝 **创建编辑器**：需要文档模式（如`basicSchema`）和扩展（如撤销历史`history`、菜单栏`menuBar`），通过`Wordgard.create()`方法配置并挂载到页面元素。
- ⚙️ **配置扩展**：使用函数如`basicSchema`、`orderedList`返回扩展集合，配置以树形结构组合；`Wordgard.label`添加无障碍标签（aria-label）。
- 🖥️ **DOM 结构**：编辑器包含两个关键元素——`dom`（外层容器）和`contentDOM`（可编辑区域），可通过`parent`选项自动插入或手动放置。
- 📄 **文档状态**：通过`state.doc`获取当前文档，支持序列化为 HTML（`serialize().toHTML()`）或 JSON（`toJSON()`），状态不可变，编辑时生成新对象。
- 🔄 **加载新文档**：不要直接替换现有文档内容，应创建新编辑器并替换旧编辑器的 DOM 元素，以保持状态一致性。

---

### [GitHub - Agent-Field/agentfield: 像 API 和微服务一样构建、运行和扩展 AI 智能体——从一开始就具备可观测、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平面，能将 AI 代理像 API 和微服务一样构建、运行和扩展，具备开箱即用的可观测性、审计和身份管理能力。

- 🤖 **核心功能**：将 Python/Go/TypeScript 函数自动转为 REST API 端点，支持异步执行、重试、Webhook 和 SSE 流式传输。
- 🚀 **一键部署**：通过一条命令或提示即可生成包含代理、控制平面和 REST API 的生产级多代理后端（Docker Compose 堆栈）。
- 📈 **水平扩展**：无状态 Go 控制平面，可水平扩展；基于 PostgreSQL 的持久化队列支持租约处理，崩溃后自动恢复。
- 🧩 **多语言 SDK**：提供 Python、Go、TypeScript SDK，支持结构化 AI 输出、跨代理调用、服务发现和分布式状态管理。
- 👤 **人机协同**：支持 `app.pause()` 暂停执行等待人工审批，具备崩溃安全、持久化和审计能力。
- 🔐 **身份与治理**：每个代理拥有 W3C DID 加密身份，支持基于标签的访问策略、可验证凭证和防篡改审计追踪。
- 📊 **可观测性**：自动生成工作流 DAG 可视化、Prometheus 指标、结构化日志和执行时间线。
- 🎯 **金丝雀部署**：支持流量权重路由、A/B 测试和蓝绿部署，可逐步推出代理版本。
- 🛠️ **开发者体验**：CLI 脚手架、本地仪表盘、热重载、MCP 服务器集成，以及与 Claude Code 等编码代理的无缝协作。

---

### [Astryx 设计系统](https://astryx.atmeta.com/)

**原文标题**: [Astryx Design System](https://astryx.atmeta.com/)

订单状态概览  
- 📦 查询订单物流信息，了解当前配送进度  
- 🔍 确认订单号或登录账户查看详细状态  
- 📞 联系客服获取实时更新或解决延迟问题  
- ⏳ 注意配送时间受节假日或天气影响可能延长  
- ✅ 检查邮箱或短信通知，确认是否已签收或需自提

---

### [Driver.js - 纯 JavaScript 的产品导览与高亮功能](https://driverjs.com/)

**原文标题**: [Driver.js - Product Tours & Highlights in Vanilla JS](https://driverjs.com/)

driver.js 是一款轻量级 JavaScript 库，用于产品导览、高亮显示和上下文帮助，支持多种浏览器和设备，高度可定制且无依赖，每月下载量超过 400 万次，被众多知名企业和项目使用。

- 🚀 轻量无依赖：仅约 5kb，无需额外库，纯 JavaScript 编写，支持 TypeScript
- 🌐 广泛兼容：支持所有主流浏览器、移动设备，并适配 React、Vue、Angular 等框架
- 🎨 高度可定制：提供动画导览、高亮弹窗、自定义样式、覆盖层颜色等多种选项
- 📦 功能丰富：包含进度显示、退出确认、异步步骤、事件钩子等高级特性
- 💡 多种用例：适用于用户引导、交互教程、功能推广、上下文帮助、表单指导等场景
- 🔧 简易集成：只需导入库、描述步骤、调用 `drive()` 即可快速创建导览
- 🏢 企业信赖：被 Red Hat、Alibaba、Intel、Fiverr 等知名公司采用，GitHub 星标超 25.8k
- 🔓 MIT 开源：免费用于个人和商业项目，无需署名，永久可用

---

### [Upyo | 跨运行时电子邮件库](https://upyo.org/)

**原文标题**: [Upyo | Cross-runtime email library](https://upyo.org/)

本文件概述了 Upyo 邮件库的核心功能与可用传输方式，并提供了相关参考文档链接。

- 📧 **消息与附件**：支持邮件编写、消息发送及附件管理。
- 🚚 **多种传输方式**：涵盖 SMTP、JMAP、Lettermint、Mailgun、Plunk、Resend、SendGrid、Amazon SES 等。
- 🔄 **高级传输**：提供池传输、重试传输及 OpenTelemetry 集成。
- 🧪 **测试与自定义**：包含模拟传输及自定义传输接口。
- 📚 **完整参考**：列出所有核心包（如 @upyo/core、@upyo/smtp）及不稳定功能。

---

### [使用无 JS 或低 JS 选项减少 JS 工作量](https://aarontgrogg.github.io/NoLoJS/)

**原文标题**: [Reduce the JS Workload with No- or Lo-JS options](https://aarontgrogg.github.io/NoLoJS/)

概述总结  
- 📉 **减少 JS 负担**：本文提倡用 HTML 和 CSS 替代 JavaScript，处理手风琴菜单、导航等常见 UI 模式，以减轻浏览器 JS 工作负载。  
- 🧩 **组件列表**：收录了手风琴、CSS 轮播、筛选器、懒加载、模态框、视差滚动等 40+ 个无 JS 或低 JS 的组件示例。  
- 📚 **资源推荐**：引用了多篇相关文章和资源，如“You Don’t Need JavaScript for That”系列，并推荐了 Theo Soti、Utsav Meena 等作者。  
- 🤝 **贡献指南**：鼓励提交 PR，要求按功能命名模式、包含 README 描述、提供最小化代码示例（HTML/CSS/JS），并附上 CodePen 演示。  
- 📧 **联系方式**：可通过邮箱（aarontgrogg@gmail.com）或 GitHub/网站联系作者。

---

### [GitHub - azat-io/eslint-plugin-perfectionist: ☂️ 用于排序对象、导入、类型、枚举、JSX 属性等多种数据的 ESLint 插件](https://github.com/azat-io/eslint-plugin-perfectionist)

**原文标题**: [GitHub - azat-io/eslint-plugin-perfectionist: ☂️ ESLint plugin for sorting various data such as objects, imports, types, enums, JSX props, etc. · GitHub](https://github.com/azat-io/eslint-plugin-perfectionist)

ESLint Plugin Perfectionist 是一个用于排序代码中各种数据（如导入、对象、TypeScript 类型等）的 ESLint 插件，支持按字母、自然顺序或行长度排序，所有规则均可自动修复，旨在提升代码可读性、一致性和美观性。

- 📦 **安装简便**：需先安装 ESLint v8.45.0+，再通过 npm 安装插件，支持 Flat Config 和 Legacy Config 两种配置方式。
- ⚙️ **丰富规则**：提供 24 条可自动修复的规则，覆盖数组、类、枚举、导入、接口、JSX 属性等，多数规则包含在推荐配置中。
- 📚 **多种排序方式**：支持按字母顺序、自然顺序、行长度或自定义顺序排序，满足不同项目需求。
- 🔧 **安全可修复**：所有规则均可通过 `--fix` 自动修复，并考虑展开运算符和注释，确保代码行为不受影响。
- 📖 **完整文档**：提供详细文档和 FAQ，解答编辑器自动修复、安全性及与 Prettier 区别等问题。
- 🤝 **社区友好**：采用 MIT 许可证，遵循语义化版本，鼓励贡献，并设有行为准则和贡献指南。

---

### [发布 | TinyBase](https://tinybase.org/guides/releases/#v9-0)

**原文标题**: [Releases | TinyBase](https://tinybase.org/guides/releases/#v9-0)

TinyBase v9.0 主要关注可靠性和社区问题修复，包括持久化、同步、模式默认值等方面的改进，同时回顾了从 v8.5 到 v4.0 的各个版本的重要功能更新。

- 🔧 v9.0 专注于社区问题修复和可靠性提升，包括持久化、同步、模式默认值、基础设施限制和查询语义边缘情况的改进
- 💾 新增 Value 持久化子集配置功能，允许只保存或加载特定的 Value ID
- 🌐 WebSocket 同步器现在支持大负载分片和重组，解决了 Cloudflare Workers 等基础设施的消息大小限制问题
- ⏰ 模式默认值现在使用中性时间戳，避免覆盖其他对等方的新同步数据
- 🗄️ PowerSync 持久化修复了表格行更新逻辑，避免在启动时因模式验证导致的数据重写问题
- 📊 v8.5 引入了 React 图表组件模块，支持 LineChart、BarChart 和 CartesianChart 等组件
- 🧩 v8.4 和 v8.3 分别添加了 Solid 和 Svelte 的 DOM 组件和检查器支持
- 🔍 v8.2 和 v8.1 完成了 Svelte 和 Solid 框架的完整支持，包括响应式绑定和 UI 组件
- 🆕 v8.0 引入了对象和数组类型支持，以及强大的中间件系统用于数据拦截和转换
- 📝 v7.3 添加了遵循 React useState 模式的状态钩子，简化数据读写
- 🔢 v7.2 引入了参数化查询功能，允许定义带有命名参数的查询
- 📋 v7.1 添加了 Schematizers 系统，支持从 Zod、TypeBox、Valibot 等验证库转换模式
- 🔄 v7.0 增加了对 null 作为有效 Cell 和 Value 类型的支持
- 🌍 v6.7 到 v6.0 引入了 OPFS 持久化、React Native 支持、Durable Object SQL 存储、Bun SQLite 持久化等功能
- 🚀 v5.4 到 v5.0 引入了 MergeableStore CRDT 类型、Synchronizer 同步框架、WebSocket 同步服务器等重大功能
- 🗃️ v4.0 到 v4.8 添加了 SQLite、PostgreSQL、PowerSync、ElectricSQL、LibSQL、PartyKit 等多种持久化和同步集成

---

### [GitHub - katspaugh/wavesurfer.js: 音频波形播放器 · GitHub](https://github.com/katspaugh/wavesurfer.js)

**原文标题**: [GitHub - katspaugh/wavesurfer.js: Audio waveform player · GitHub](https://github.com/katspaugh/wavesurfer.js)

wavesurfer.js 是一个基于现代 Web 技术的交互式音频波形渲染与播放库，适用于网页应用，支持插件扩展和自定义样式。

- 🎵 **核心功能**：提供交互式波形渲染和音频播放，支持通过 npm 或 UMD 脚本引入，可创建实例并配置颜色、音频 URL 等选项。
- 📦 **插件生态**：官方维护多个插件，如 Regions（区域标记）、Timeline（时间轴）、Minimap（迷你图）、Envelope（淡入淡出）、Record（录音）、Spectrogram（频谱图）和 Hover（悬停显示）。
- 🎨 **CSS 样式**：使用 Shadow DOM 隔离样式，通过 `::part()` 伪选择器可自定义光标、区域等元素样式。
- ❓ **常见问题**：涵盖 CORS 问题、大文件支持（推荐预解码峰值）、流式音频（需预解码）、VBR 音频同步问题，以及 Web Audio 效果连接（仅导出音频元素）。
- 🛠️ **开发与测试**：使用 TypeScript 开发，通过 `yarn start` 启动开发服务器，采用 Cypress 进行端到端和视觉回归测试。
- 📊 **社区与资源**：GitHub 上拥有 10.3k 星标和 1.8k 分支，提供详细 API 文档、示例和讨论论坛，支持 BSD-3-Clause 许可证。

---

### [首页 | React 谷歌地图](https://visgl.github.io/react-google-maps/)

**原文标题**: [Home | React Google Maps](https://visgl.github.io/react-google-maps/)

react-google-maps 是一个为 React 应用提供 Google Maps JavaScript API 组件和钩子的库，支持响应式地图集成和扩展，并属于 vis.gl 框架套件。

- 🗺️ 提供 React 组件和钩子，用于轻松集成 Google Maps JavaScript API
- 🔄 支持将 Google 地图作为完全受控的响应式组件使用
- 🧩 包含可扩展的组件和钩子，方便编写自定义功能
- 🎯 属于 vis.gl 框架套件，可与 deck.gl 等库结合，实现高性能 2D 和 3D WebGL 可视化
- 📚 提供 API 参考文档和入门模板资源
- 🌐 基于 OpenJS Foundation 开源社区

---

### [2026 年 9 月 11 日瑞士 JavaScript 大会 | 苏黎世 JS Conf 2026](https://conf.zurichjs.com/?utm_source=javascript_weekly&utm_medium=newsletter&utm_campaign=2026_07_07_edition)

**原文标题**: [JavaScript Conference Sept 11 2026 Switzerland | ZurichJS Conf 2026](https://conf.zurichjs.com/?utm_source=javascript_weekly&utm_medium=newsletter&utm_campaign=2026_07_07_edition)

ZurichJS Conf 2026 是一场国际社区会议，将于 2026 年 9 月 11 日在瑞士苏黎世 Technopark 举行，提供学习、交流和工作坊，价格亲民，并由社区核心成员推动。

- 🗓️ **会议日期与地点**：2026 年 9 月 11 日，瑞士苏黎世 Technopark，包含社区日、工程日、会议日和会后放松日（9 月 9-12 日）。
- 👩‍🏫 **行业专家学习**：从 React、Vue、Angular 等框架专家及开发者工具、测试领域获得最新见解和最佳实践。
- 🛠️ **动手实践工作坊**：深入特定用例，提供专家指导和问答机会，强化学习效果。
- 🤝 **社区连接**：与 ZurichJS 社区建立联系，拓展人脉，创造跨国界的持久关系。
- 💰 **亲民价格**：票价较其他欧洲网络开发会议低 50%，提供社区定价。
- 🏆 **社区认可**：ZurichJS 在 JSNation 获得“年度全球社区”奖项，表彰其高影响力。
- 🧑‍🤝‍🧑 **核心贡献者**：Bogdan 赋予社区灵魂，Nadja 提供运营支持，Colin 带来冷静与帮助，共同推动会议成功。
- 🎟️ **门票与优惠**：提供学生票（通过提交项目赢取）、10% 折扣码（如 REACTJSBARCELONA_10），并解答常见问题（如转票、团队折扣）。
- 📢 **赞助与志愿者**：欢迎赞助商、合作伙伴和志愿者，提供赞助选项。
- 📱 **社交媒体互动**：在 Bluesky、LinkedIn、Twitter、Instagram 上关注最新动态。
- 📧 **联系与反馈**：提供咨询、反馈、问题报告渠道，并设有邮件订阅获取更新。

---

### [任意规模下的 Postgres 时间序列工作负载。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Cloud 提供大规模时间序列数据处理服务，支持实时扩展、高可用性和企业级安全合规。

- 📊 支持每天处理 3 万亿指标、3PB 数据及 1 万亿数据点，展现真实世界的大规模处理能力
- 💰 新用户可获$1000 信用额度（30 天有效），无需信用卡，仅限新账户
- 🏢 受到数千家物联网公司信赖
- 🚀 通过最多 10 个节点的副本集实现读写分离，结合分层 SSD/S3 存储，实现无限制且经济高效的扩展
- 💸 采用计算与存储分离架构，可独立扩展，避免为闲置容量付费，优化成本与性能
- 🔒 多可用区集群支持自动故障转移、时间点恢复和跨区域备份，确保高可用性
- 🛡️ 符合 SOC 2、HIPAA 和 GDPR 标准，提供始终加密、SSO 集成、RBAC 和审计日志
- 📈 提供查询钻取和仪表盘，可监控性能与错误，并集成 CloudWatch、Datadog、Prometheus
- ⚡ 数分钟内即可配置数据库，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 可与主流云提供商及 Postgres 生态系统集成
- 🏢 企业级服务包括合同 SLA、区域数据隔离、24/7 专家支持和合规认证

---

### [置信度评分的 PDF 翻译流水线：福昕与 Straker AI](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-translation-api-confidence-scoring/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260707)

**原文标题**: [Confidence-Scored PDF Translation Pipeline: Foxit and Straker AI](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-translation-api-confidence-scoring/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260707)

本指南介绍了如何使用 Foxit PDF 编辑器 API 通过 Python 和 cURL 示例，以编程方式批量处理 PDF 文档的页面操作、合并、拆分和扁平化，解决手动编辑效率低的问题。

- 📄 **页面操作**：支持添加、删除、旋转和重新排序页面，适用于批量文档整理。
- 🔗 **合并功能**：可将多个 PDF 文件合并为一个，简化文档管理流程。
- ✂️ **拆分功能**：按页数或书签拆分 PDF，便于分发或归档。
- 🖨️ **扁平化处理**：将表单字段和注释转换为静态内容，确保文档一致性。
- 🐍 **Python 示例**：提供可直接运行的代码，降低开发门槛。
- 🌐 **cURL 支持**：同时提供命令行示例，方便不同技术栈用户集成。
- ⚡ **批量处理**：API 设计支持高并发，适合每日处理数百份文档的场景。

---

### [为 Web 开发者介绍 Safari MCP 服务器 | WebKit](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

**原文标题**: [  Introducing the Safari MCP server for web developers | WebKit](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

Safari MCP 服务器为网页开发者提供了一种新的调试方式，让 AI 代理能直接连接 Safari 浏览器窗口，自动检查代码渲染效果，从而减少手动调试的繁琐步骤。

- 🚀 **提升调试效率**：AI 代理可自动访问 DOM、网络请求、截图和控制台输出，无需频繁切换窗口或输入提示词。
- 🕸️ **Safari 网页开发**：代理能直接检查代码在 Safari 中的实际渲染效果，优化开发流程。
- 🌐 **改善兼容性**：代理可检查 Safari 中的样式、布局，并与预期对比，避免跨浏览器问题。
- 📊 **性能分析**：代理可评估 JavaScript，获取导航和资源加载时间，找出性能瓶颈。
- ♿ **无障碍检查**：代理能检测缺失标签、ARIA 属性错误和对比度问题，提升可访问性。
- ✅ **状态验证**：代理可检查表单状态、元素交互、结账流程等，减少手动测试。
- 🛠️ **丰富工具集**：提供 18 种工具，包括控制台日志、DOM 交互、截图、网络请求、视口设置等。
- 💻 **本地运行**：服务器完全在本地运行，不访问个人信息，数据直接发给代理，不传给 Apple。
- 🔧 **快速上手**：安装 Safari Technology Preview 后，启用远程自动化，即可通过 Claude 或 Codex 等代理使用。

---

### [更新日志 - shadcn/ui](https://ui.shadcn.com/docs/changelog)

**原文标题**: [Changelog - shadcn/ui](https://ui.shadcn.com/docs/changelog)

概述：shadcn/ui 近期发布多项重大更新，包括默认组件库切换为 Base UI、推出聊天界面组件、GitHub 注册表支持、CSS 注入命令、以及全新紧凑风格 Rhea。

- 📦 **Base UI 成为默认组件库**：自 2026 年 7 月起，新项目默认使用 Base UI，Radix 仍受支持但非默认。提供迁移技能，可逐步迁移组件，保留自定义代码。
- 💬 **聊天界面组件发布**：2026 年 6 月推出 MessageScroller、Message、Bubble、Attachment、Marker 等组件，以及 scroll-fade 和 shimmer CSS 工具，优化流式聊天体验。
- 🗂️ **GitHub 注册表功能**：可将任何公开 GitHub 仓库转为注册表，通过 CLI 直接安装组件、钩子、工具等，无需额外服务器。
- ⚡ **shadcn eject 命令**：将 shadcn/tailwind.css 内联到全局 CSS 中，移除 shadcn 依赖，支持单仓库环境。
- 🎨 **引入 Rhea 风格**：2026 年 5 月推出更紧凑的 Luma 变体，保持圆角设计但缩小间距和控件尺寸，适合高密度产品界面。
- 🔧 **其他更新**：包括注册表验证、包导入别名、预设命令、Sera 风格、组件组合、RTL 支持、Blocks 社区、Monorepo 支持等多项改进。

---

### [无样式 UI 组件，用于无障碍设计系统 · Base UI](https://base-ui.com/)

**原文标题**: [Unstyled UI components for accessible design systems · Base UI](https://base-ui.com/)

Base UI 是一个无样式 UI 组件库，用于构建可访问的 React 用户界面，注重组合性、一致性和长期维护。

- 🎨 无样式设计：不捆绑任何 CSS，可与 Tailwind、CSS Modules、CSS-in-JS 等任意样式库和动画库配合使用。
- ♿ 高度可访问：遵循 ARIA 创作实践指南和 WCAG 2.2 标准，组件在多种浏览器、设备和环境中测试，确保无障碍性。
- 🔧 灵活与强大：提供更复杂的组件（如 Combobox 和 Autocomplete），支持输入擦洗、嵌套对话框和悬停触发菜单等高级功能。
- 🚀 积极维护：由 7 名全职开发者、设计师和管理员组成的专门团队持续开发，与 Radix UI 保持 API 兼容性，便于迁移。
- 💼 免费商用：基于 MIT 许可证，可自由用于商业项目，并支持修改。
- 📚 面向开发者：专为 React 设计，不适用于其他框架，未来可能考虑扩展支持。

---

### [PocketJS — 裸机现代网页](https://pocketjs.dev/)

**原文标题**: [PocketJS â Bare Metal Modern Web](https://pocketjs.dev/)

PocketJS 是一个能在 8MB 内存下运行现代 Web 界面的框架，通过将繁重工作移至构建时和 Rust 核心，让开发者使用熟悉的前端工具在 PSP 等受限硬件上构建流畅的 60 FPS 界面。

- 🚀 **超低内存运行**：在 8MB 内存预算内实现 60 FPS 动画，支持 PSP、macOS 等设备。
- 🧩 **熟悉的前端工具**：支持 Tailwind、Flexbox、Solid 和 Vue Vapor，保持现代开发体验。
- ⚙️ **构建时优化**：Tailwind 类在构建时编译为紧凑样式记录，无 CSS 解析器或运行时开销。
- 🖼️ **原生渲染**：布局、样式、文本和动画在 Rust 核心中处理，JSX 和信号量保持不变。
- 📱 **跨平台兼容**：同一 Rust 核心可移植到 PSP、macOS、3DS、Steam Deck、iOS、Android 等设备。
- 🎮 **游戏机友好**：专为 PSP 等受限硬件设计，支持原生按钮映射和焦点管理。
- 🔧 **精细响应式**：Solid 和 Vue Vapor 的响应式 API 直接与核心树通信，状态更新高效。
- 📝 **清晰文本渲染**：Inter 字体字形预烘焙为图集，支持亚像素定位，小屏幕文字清晰。

---

### [提交历史 — 一个 GitHub 用户终身提交的星星历史](https://commit-history.com/)

**原文标题**: [Commit History — a star-history for a GitHub user’s lifetime commits](https://commit-history.com/)

该页面展示了一个名为“Commit History”的 GitHub 用户终身累计提交次数排行榜，类似于 star-history 但专注于提交次数。

- 📊 页面显示 GitHub 用户终身累计公开提交次数的排行榜
- 🏆 榜首为 Dicklesworthstone（Jeff Emanuel），拥有 146,424 次提交
- 🥈 第二名 yegor256（Yegor Bugayenko）有 105,754 次提交
- 🥉 第三名 leodemoura（Leonardo de Moura）有 97,966 次提交
- 🔍 页面提供搜索功能，可查询特定用户的提交历史
- 👥 列出了多位知名开发者，如 fabpot、gaearon、hadley 等
- 📈 提交次数从榜首的 14.6 万次到第 25 名的 4.5 万次不等
- ❓ 页面底部提供“这些数字意味着什么？”的说明链接
- 💡 页面由 peetzweg 创建，并接受用户支持

---

### [管理您的个人资料 README - GitHub 文档](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)

**原文标题**: [Managing your profile README - GitHub Docs](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)

本指南介绍了如何通过创建与用户名同名的公开仓库并添加 README.md 文件来管理 GitHub 个人资料 README，包括添加、删除及前提条件。

- 🛠️ **前提条件**：需创建与用户名匹配的公开仓库，根目录包含 README.md 文件且内容非空；2020 年 7 月前创建的仓库需手动分享到个人资料。
- ➕ **添加步骤**：点击新建仓库，输入与用户名相同的仓库名，设为公开，启用 README 选项，创建后编辑 README 文件（可使用预填模板和表情符号）。
- ❌ **删除条件**：移除或清空 README 文件、将仓库设为私有、或仓库名与用户名不匹配时，README 会自动从个人资料移除；推荐设为私有以保留内容。
- 📚 **后续操作**：可参考“Profile reference”文档获取更多信息。

---

### [sindresorhus 的提交历史](https://commit-history.com/sindresorhus)

**原文标题**: [sindresorhus’s commit history](https://commit-history.com/sindresorhus)

该页面展示了 Sindre Sorhus 在 GitHub 上的公开提交历史统计。

- 📊 自 2009 年 12 月以来，累计公开提交总数达 35,028 次。
- 📈 最活跃的月份是 2025 年 9 月，当月提交了 884 次。
- 🏆 在 GitHub 提交次数排名中位列第 44 位。
- 🖼️ 提供可嵌入 GitHub 个人资料或项目 README 的动态图表，支持亮色/暗色主题自动切换。
- 🔗 页面底部包含可直接复制的嵌入代码示例。

---

### [PGlite](https://pglite.dev/)

**原文标题**: [PGlite](https://pglite.dev/)

概述摘要：这是一个轻量级的 Postgres WASM 构建版本，压缩后体积小于 3MB。

- 🚀 完整功能：提供完整的 Postgres 数据库功能，运行在 WebAssembly 环境中
- 📦 超小体积：压缩后仅 3MB 以下，便于快速加载和部署
- 🔧 轻量设计：针对 Web 环境优化，减少资源占用
- 🌐 跨平台：可在浏览器等支持 WASM 的环境中直接运行

---

### [PGlite 周下载量突破 1000 万 | Electric](https://electric.ax/blog/2026/06/25/pglite-reaches-10-million-weekly-downloads)

**原文标题**: [PGlite reaches 10 million weekly downloads | Electric](https://electric.ax/blog/2026/06/25/pglite-reaches-10-million-weekly-downloads)

PGlite（PostgreSQL 编译为 WASM）已达到每周 1000 万次 npm 下载量，本文回顾了其发展历程、应用场景及未来规划。

- 🚀 **下载量里程碑**：PGlite 每周 npm 下载量突破 1000 万，从一年前的 100 万增长至此，社区在本地模拟器、ORM 集成、测试套件、浏览器沙箱、AI 应用及工具链中广泛采用。
- 🖥️ **本地开发无需 Docker**：PGlite 让 CLI 在安装时即可提供数据库，并透明切换至云端 PostgreSQL，被 Prisma、Firebase、Netlify、AWS 等用于本地开发环境。
- 🤖 **本地 AI 与搜索**：AI 应用利用 PGlite 存储嵌入、元数据、对话历史及文档块，内置 pgvector 支持混合检索，如 GBrain 将其作为默认引擎，用于个人 AI 大脑。
- 🧪 **真实 PostgreSQL 测试**：测试套件使用 PGlite 快速启动、隔离测试，无需模拟或不同 SQL 方言，Drizzle、Supabase、Prisma 等均在其集成测试中使用。
- 🔌 **ORM 与框架集成**：PGlite 被 Drizzle、Kysely、Prisma、MikroORM、Effect SQL 等主流 ORM 和框架支持，开发者无需放弃现有迁移、查询构建器即可使用。
- 🌐 **浏览器沙箱与交互文档**：PGlite 在浏览器中运行 PostgreSQL，用于数据库设计工具（如 database.build）、交互式代码游乐场（如 LiveCodes、Codapi）及研究论文中的内嵌 SQL 示例。
- 📦 **PostgreSQL 的轻量嵌入**：PGlite 以单用户模式运行，支持类型、索引、约束、持久化、全文搜索、pgvector、PostGIS 等扩展，满足开发、测试、本地状态及生产环境统一数据库的需求。
- 🛠️ **发展历程**：从 2024 年 1 月概念验证起步，实现单用户模式 WASM 运行，逐步支持 wire 协议、参数化查询、扩展（如 PostGIS、pgvector），并优化性能。
- 🔮 **未来规划**：计划支持多连接、更多扩展（如 TimescaleDB、ParadeDB）、逻辑复制，并探索多线程 PostgreSQL，长期目标是打造类似 SQLite 的原生嵌入式库 libpglite。

---

