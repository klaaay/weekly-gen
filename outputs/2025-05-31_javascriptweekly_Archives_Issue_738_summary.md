### [《JavaScript 周刊》第 738 期：2025 年 5 月 30 日](https://javascriptweekly.com/issues/738)

**原文标题**: [JavaScript Weekly Issue 738: May 30, 2025](https://javascriptweekly.com/issues/738)

概述总结  
本期内容涵盖了多个 JavaScript 和前端开发领域的最新动态，包括框架更新、新 API 发布、工具推荐以及技术文章分享。  

- 🚀 **Remix 框架重大变革**：Remix 不再是一个 React 框架，转而成为基于 Preact 的全栈框架，专注于模型优先和低依赖性。  
- ⏳ **Temporal API 即将到来**：Firefox 139 已默认支持这一新的 JavaScript 日期和时间处理 API，未来将推广到更多运行时环境。  
- 🛠 **Angular v20 发布**：包含信号、增量水合等稳定功能，并引入了新的实验性 API 如资源流和 httpResource。  
- 📦 **Bun v1.2.15 更新**：新增了`bun audit`工具，用于项目依赖的安全审计。  
- 📖 **JavaScript 日期解析的“Wat”时刻**：探讨了为什么`2025/05/28`和`2025-05-28`在 JavaScript 中会被解析为不同的日期。  
- 🎥 **Chrome DevTools 性能调试新特性**：展示了重新设计的性能面板及其新功能，帮助开发者优化性能。  
- 📚 **React 概念可视化指南**：更新至 React 19，涵盖了 Actions、Transitions 和 Server Components 等新特性。  
- 🔧 **Svelte Flow 1.0 发布**：用于在 Svelte 中构建基于节点的 UI 和图表。  
- 🤖 **Google Gen AI SDK for TypeScript/JavaScript v1**：开发者现在可以在 Node.js 中使用 Google 的 Gemini API 和 Vertex 平台。  
- 📊 **Stack Overflow 开发者调查回归**：第十五届年度调查再次启动。

---

### [醒来吧，混音！ | 混音](https://remix.run/blog/wake-up-remix)

**原文标题**: [Wake up, Remix! | Remix](https://remix.run/blog/wake-up-remix)

概述  
Remix 团队宣布结束“休眠”，推出全新方向的 Remix v3，基于 React Router v7 的成熟基础，探索更轻量、更贴近 Web 的开发体验。  

- 🛌 **Remix 的“休眠”与重启**：Remix v2 与 React Router 合并后，团队完成整合并发布 React Router v7，现宣布重新激活 Remix 项目。  
- 🚀 **React Router v7 的成熟**：支持 RSC（服务器组件）和服务器路由，技术稳定且被 Shopify、GitHub 等大厂采用，为 Remix 提供坚实基础。  
- 🔄 **Remix v3 的新方向**：脱离特定范式，追求更简单、高性能的模块化工具链，减少依赖（如基于 Preact 分支），贴近 Web 原生开发。  
- 📜 **核心开发原则**：  
  - 🤖 **模型优先开发**：优化 LLM 工具链，支持 AI 集成到产品中。  
  - 🌐 **基于 Web API**：减少上下文切换，依赖 JavaScript 全栈生态。  
  - ⚡ **运行时优先设计**：避免静态分析污染，测试无需打包。  
  - 🚫 **减少依赖**：谨慎选择依赖，目标为零。  
  - 🧩 **强组合性**：模块单一职责、可替换，保持高内聚。  
  - 📦 **统一分发**：松散模块通过 `remix` 工具箱集中分发。  
- 🎸 **社区参与**：通过 Remix Jam 分享进展，邀请开发者加入探索。  
- 📩 **订阅更新**：提供邮件订阅，第一时间获取新特性与活动信息。

---

### [混音 - 打造更优质的网站](https://remix.run/)

**原文标题**: [Remix - Build Better Websites](https://remix.run/)

Remix 是一个全栈 Web 框架，专注于用户界面和现代 Web 应用体验，通过遵循 Web 标准帮助开发者构建更优质的网站。它提供了快速、流畅且稳健的用户体验，支持嵌套路由、并行数据加载、错误处理和渐进增强等功能。

- 🚀 **全栈框架** - Remix 是一个全栈 Web 框架，专注于用户界面和现代 Web 应用体验。  
- 🌐 **Web 标准** - 遵循 Web 标准，帮助开发者构建更快速、更稳健的网站。  
- 🔗 **嵌套路由** - 支持嵌套路由，优化数据加载和代码拆分，减少加载状态。  
- ⚡ **并行加载** - 在服务器端并行加载数据，减少请求瀑布流，提升性能。  
- 📝 **表单处理** - 内置表单处理功能，简化数据更新逻辑，支持渐进增强。  
- 🛡️ **错误处理** - 提供路由错误边界，优雅处理客户端和服务器端错误。  
- 🔄 **预加载** - 支持预加载资源和数据，实现近乎即时的页面切换。  
- 💬 **开发者好评** - 多位开发者称赞其易用性、性能和对现代 Web 开发的支持。  
- 🏗️ **灵活部署** - 基于 Web Fetch API，可部署在 Cloudflare Workers、Serverless 和 Node.js 环境。  
- 🎯 **用户体验优先** - 旨在提供更快的页面加载和无缝交互，提升整体用户体验。

---

### [合并 Remix 与 React Router | Remix](https://remix.run/blog/merging-remix-and-react-router)

**原文标题**: [Merging Remix and React Router | Remix](https://remix.run/blog/merging-remix-and-react-router)

React Router 和 Remix 将合并，React Router v7 将包含 Remix 的所有优秀特性，Remix 用户只需更改导入即可升级。  

- 🎉 **React Router v7 发布**：推荐所有新项目使用 React Router v7，并升级现有 Remix 应用。  
- 🌉 **合并背景**：Remix 和 React Router 功能逐渐趋同，Remix 本质上是“React Router 的框架”。  
- 🔄 **升级路径**：Remix 用户未来只需更改导入语句即可迁移到 React Router v7。  
- 🚀 **Remix 特性整合**：React Router v7 将包含 Remix 的自动代码拆分、简化数据加载、表单操作、SSR 等特性。  
- ⚡ **Vite 支持**：Remix 已转向 Vite，未来 React Router 也将提供 Vite 插件支持。  
- 📦 **Remix 的未来**：Remix 品牌保留，团队将专注于 React Router v7，未来可能推出更强大的服务端方案。  
- 🔧 **平滑升级**：提供代码修改工具和指南，确保升级过程无缝衔接。  
- ❓ **常见问题**：现有 Remix 用户可继续使用，未来升级只需更改导入；新用户可直接尝试 Remix 或等待 React Router v7。  
- 📢 **后续计划**：团队将专注于稳定 React Router v7，并通过博客、Discord 和 Twitter 分享最新进展。

---

### [React Router 官方文档](https://reactrouter.com/)

**原文标题**: [React Router Official Documentation](https://reactrouter.com/)

一个用户至上、标准优先、多策略的路由器，可部署在任何地方。提供文档、GitHub 和 Discord 支持。

- 🚀 **非破坏性升级**：从 v6 升级到 v7 无需更改现有代码，保持原有使用方式。  
- 🌉 **React 19 桥梁**：支持新的打包、服务器渲染、预渲染和流式功能，逐步过渡到 React 19。  
- 🛡️ **类型安全**：新增类型生成功能，为路由参数、加载器数据等提供一流的类型支持。  
- � **新手入门**：提供学习资源，帮助快速掌握 React Router。  
- 🔄 **v6 用户升级**：简单几步即可升级到 v7 版本。  
- 🏗️ **框架功能适配**：指导现有应用如何整合新框架特性。  
- ❓ **获取帮助**：通过 GitHub 讨论区解决遇到的问题。  
- ©️ **版权信息**：2025 年由 Shopify, Inc.提供。

---

### [Preact](https://preactjs.com/)

**原文标题**: [Preact](https://preactjs.com/)

Preact 是一个轻量级的 React 替代方案，提供相同的现代 API，但体积更小，性能更优，适合多种应用场景。

- 🚀 **轻量快速** - Preact 仅 3kB，是 React 的轻量级替代品，提供相似的 API 和更高的性能。
- 🏗️ **接近原生 DOM** - 提供最精简的虚拟 DOM 抽象，直接与浏览器平台特性集成，兼容其他库。
- 📦 **超小体积** - 体积足够小，使得应用代码成为主体，减少下载、解析和执行时间。
- ⚡ **高性能** - 采用简单可预测的 diff 算法，自动批量更新，优化到极致。
- 🧩 **便携与嵌入** - 小巧的体积使其可以嵌入到任何地方，构建部分应用或独立部件。
- 🛠️ **高效开发** - 支持标准 HTML 属性（如 `class` 和 `for`），提升开发效率。
- 🔄 **生态兼容** - 兼容 React 生态，通过 `preact/compat` 可以无缝使用 React 组件。
- 📝 **示例丰富** - 提供 Todo List 和 GitHub Stars 等示例，展示其易用性和功能性。
- 🌍 **多语言支持** - 支持多种语言，包括中文、英语、日语等，方便全球开发者使用。

---

### [JavaScript 即将推出的 Temporal API 及其解决的问题 | WaspDev](https://waspdev.com/articles/2025-05-24/temporal-api)

**原文标题**: [JavaScript's upcoming Temporal API and what problems it will solve | WaspDev](https://waspdev.com/articles/2025-05-24/temporal-api)

JavaScript 即将推出的 Temporal API 及其解决的问题

- 🕰️ JavaScript 的 Date 对象存在许多问题，主要源于 1995 年设计时的仓促和 Java 的早期影响。
- 🌍 Date 对象的主要问题包括有限的时区支持、夏令时处理困难、可变性导致的副作用、解析不一致以及 API 设计上的怪癖（如零基月份）。
- 🔄 Temporal API 旨在解决这些问题，提供不可变、更精确和更一致的日期时间处理方式。
- 📅 Temporal API 引入了多种新类型，如 PlainDate、PlainTime、PlainMonthDay 等，分别处理不同的日期时间场景。
- ⏱️ Temporal.ZonedDateTime 结合了时间和时区，解决了跨时区时间转换和计算的难题。
- ⏳ Temporal.Instant 表示绝对时间点，适用于时间戳和高精度时间计算。
- 📊 Temporal.Duration 用于表示时间间隔，支持复杂的时间算术操作。
- 📆 支持多种日历系统，如伊斯兰历、希伯来历等，满足不同文化的日期需求。
- 🚧 截至 2025 年，Temporal API 仅在 Firefox 139+ 中实验性支持，生产环境需使用 polyfill。
- 🔮 Temporal API 的推出标志着 JavaScript 日期时间处理的重大进步，解决了长期存在的痛点，提升了开发体验。

---

### [时间性文档](https://tc39.es/proposal-temporal/docs/)

**原文标题**: [Temporal documentation](https://tc39.es/proposal-temporal/docs/)

Temporal 是一个 ECMAScript 的现代日期/时间 API，旨在解决传统 Date 对象的诸多问题。它提供了易于使用的 API，支持所有时区和非公历日历，并严格处理日期和时间的表示与计算。

- 📚 Temporal 是 ECMAScript 的现代日期/时间 API，旨在解决传统 Date 对象的问题。
- 🌍 提供一流的时区支持，包括夏令时安全的算术计算。
- 📅 支持多种日历系统，不仅仅是公历。
- ⏳ 提供多种时间相关的类，如 Temporal.Instant、Temporal.ZonedDateTime 等，用于不同的使用场景。
- 🔧 Temporal.Now 提供当前系统时间和时区信息。
- 🕒 Temporal.Instant 表示一个固定的时间点，不考虑日历或位置。
- 🗓️ Temporal.ZonedDateTime 是时区和日历敏感的日期/时间对象。
- 📆 Temporal.PlainDate 表示不关联特定时间或时区的日历日期。
- ⏱️ Temporal.PlainTime 表示不关联特定日期或时区的时钟时间。
- 📅⏱️ Temporal.PlainDateTime 表示不携带时区信息的日历日期和时钟时间。
- 📅 Temporal.PlainYearMonth 表示没有日组件的日期，如“2020 年 10 月”。
- 📅 Temporal.PlainMonthDay 表示没有年组件的日期，如“7 月 14 日”。
- ⏳ Temporal.Duration 表示一段时间，用于日期/时间算术和测量时间差。
- ⚖️ 平衡（Balancing）解释了 Temporal.Duration 单位何时回绕到 0。
- 🌐 时区部分详细说明了如何在 Temporal 中处理时区。
- 📖 其他文档包括时间字符串的解析、序列化和格式化，以及如何处理时间模糊性。

---

### [航运时序 | SpiderMonkey JavaScript/WebAssembly引擎](https://spidermonkey.dev/blog/2025/04/11/shipping-temporal.html)

**原文标题**: [Shipping Temporal | SpiderMonkey JavaScript/WebAssembly Engine](https://spidermonkey.dev/blog/2025/04/11/shipping-temporal.html)

Temporal 提案为 JavaScript 中长期存在问题的 Date 对象提供了替代方案，现已在 Firefox 139 中默认启用，成为首个支持该功能的浏览器。这一成果主要由志愿者 André Bargull 贡献，展示了开源社区的强大影响力。

- 🚀 Temporal 提案旨在取代 JavaScript 中的 Date 对象，解决其长期存在的问题  
- 📚 提案于 2021 年 3 月达到 TC39 流程的第三阶段，意味着规范已完备并可实施  
- 🛠️ SpiderMonkey 的实现由志愿者 André Bargull 主导完成，贡献了 99 个补丁和近 200 个规范问题  
- 🔍 实现过程中规范持续演进，反映了大规模协作的复杂性  
- 🦊 Firefox 139 成为首个默认启用 Temporal 的浏览器  
- ❤️ 这一成就展示了开源社区和志愿者在现代软件开发中的持续重要性  
- 💡 文章鼓励贡献者参与，无论经验水平，提供了 SpiderMonkey 和 TC39 的贡献指南

---

### [宣布 Angular v20 发布。过去几年… | 作者：Minko Gechev | 2025 年 5 月 | Angular 博客](https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301?gi=4684599873f6)

**原文标题**: [Announcing Angular v20. The past couple of years have been… | by Minko Gechev | May, 2025 | Angular Blog](https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301?gi=4684599873f6)

Angular v20 正式发布，带来多项稳定性提升、开发者体验优化及未来功能预览。

- 🚀 **稳定性增强**：Signal API（`effect`、`linkedSignal`、`toSignal`）、增量水合（incremental hydration）和路由级渲染模式配置升级为稳定版，无 Zone（zoneless）进入开发者预览阶段。  
- 🔧 **开发者工具升级**：与 Chrome 合作集成 Angular 性能分析到 DevTools，新增组件实例化、变更检测等可视化追踪功能。  
- 💡 **实验性 API**：引入`resource`和`httpResource` API，支持基于 Signal 的异步状态管理和 HTTP 请求响应式处理。  
- ⚡ **服务器端渲染优化**：增量水合和路由级渲染模式配置正式稳定，支持按需加载组件并提升首屏性能。  
- 📝 **模板语法扩展**：支持指数运算符`**`、`in`操作符及未标记模板字面量，增强模板表达力。  
- 🛠️ **开发者体验改进**：  
  - 更新风格指南，简化文件名后缀规则（默认不再生成后缀）。  
  - 强化宿主绑定类型检查与语言服务支持。  
  - 实验性支持 Vitest 测试框架。  
- 🤖 **GenAI 支持**：新增`llms.txt`文件引导 AI 生成现代 Angular 代码，提供 AI 应用开发指南（`angular.dev/ai`）。  
- 🏷️ **弃用结构指令**：`*ngIf`、`*ngFor`和`*ngSwitch`标记为弃用，推荐使用内置控制流语法。  
- 🎭 **官方吉祥物计划**：发起社区投票，从三款候选设计中确定 Angular 吉祥物形象。  
- 🙌 **社区贡献**：225+ 开发者参与改进，包括表单验证增强、路由异步重定向等特性。  

未来将聚焦信号表单（signal-forms）、无选择器组件（selectorless）等方向，持续优化框架能力。

---

### [Angular 20——让魔力流动](https://www.telerik.com/blogs/angular-20-let-magic-flow)

**原文标题**: [
	Angular 20—Let the Magic Flow
](https://www.telerik.com/blogs/angular-20-let-magic-flow)

Angular 20 版本发布，专注于提升稳定性、性能和开发者体验，带来了一系列新特性和改进。

- 🎖️ **稳定化功能**：包括 `effect`、`linkedSignal`、`toSignal` 等 API 正式成为核心功能。  
- 🌊 **增量水合**：仅在视口内渲染 UI，提升性能。  
- 🛤️ **SSR 路由 API**：支持更精细的服务器端渲染配置。  
- 🧙‍♂️ **Zoneless 模式**（开发者预览）：减少对 Zone.js 的依赖，提升性能。  
- 🔥 **弃用旧指令**：`*ngIf`、`*ngFor` 和 `*ngSwitch` 被新的内置控制流（`@if`、`@for`、`@switch`）取代。  
- 🛠️ **动态组件创建**：支持信号输入、输出和双向绑定。  
- 🧪 **测试更新**：Karma 被弃用，探索 Vitest 作为替代方案。  
- 🛠️ **开发者工具增强**：Angular 性能分析集成到 Chrome DevTools。  
- 🤖 **GenAI 支持**：新增 `llms.txt` 文件帮助生成现代 Angular 代码。  
- 🎨 **Material 更新**：按钮组件对齐 Material 3 设计，新增覆盖 API 和动画控制。  
- 🏆 **社区投票**：Angular 社区正在投票选择新的官方吉祥物。  

更多详情可参考 [Angular v20 官方博客](https://blog.angular.io)。

---

### [GitHub - platformatic/php-node: Node.js 的 PHP HTTP 请求处理器](https://github.com/platformatic/php-node)

**原文标题**: [GitHub - platformatic/php-node: PHP HTTP Request handler for Node.js](https://github.com/platformatic/php-node)

platformatic/php-node 是一个允许在 Node.js 进程中运行 PHP 应用的工具，支持 Node.js 和 PHP 之间的直接通信，无需网络连接。适用于 Linux 和 macOS 平台，提供异步和同步请求处理方式。

- 🚀 **功能概述**: 在 Node.js 进程中运行 PHP 应用，支持直接通信。
- 🖥️ **支持平台**: 目前支持 x64 Linux 和 x64/arm64 macOS，未来可能扩展更多平台。
- 📦 **依赖安装**: 
  - Linux: `libssl-dev`, `libcurl4-openssl-dev`, `libxml2-dev`, `libsqlite3-dev`, `libonig-dev`, `re2c`
  - macOS: `openssl@3`, `curl`, `sqlite`, `libxml2`, `oniguruma`
- 🔧 **安装方法**: `npm install @platformatic/php-node`
- 📝 **基本用法**: 通过 `Php` 和 `Request` 类处理 HTTP 请求，支持异步和同步处理。
- ⚙️ **API 方法**:
  - `new Php(config)`: 创建 PHP 实例。
  - `php.handleRequest(request)`: 异步处理请求。
  - `php.handleRequestSync(request)`: 同步处理请求（不推荐用于生产环境）。
  - `new Request(input)`: 创建请求对象。
  - `new Response(input)`: 创建响应对象。
  - `new Headers()`: 管理 HTTP 头部。
- 🔄 **请求和响应对象**:
  - `Request` 包含 `method`, `url`, `headers`, `body`。
  - `Response` 包含 `status`, `headers`, `body`, `log`。
- 📜 **贡献与支持**: 项目属于 Platformatic 生态系统，贡献指南参考主仓库。支持通过 GitHub Issues 和社区 Discord。
- 📄 **许可证**: Apache-2.0 许可证。

---

### [tc39/agendas 仓库中 main 分支下的 agendas/2025/05.md 文件](https://github.com/tc39/agendas/blob/main/2025/05.md)

**原文标题**: [agendas/2025/05.md at main · tc39/agendas · GitHub](https://github.com/tc39/agendas/blob/main/2025/05.md)

TC39 议程仓库是一个公开的 GitHub 项目，主要用于讨论和记录 ECMAScript 标准的开发进程和相关会议议程。

- 📂 **仓库信息**：TC39/agendas 是公开的 GitHub 项目，包含 ECMAScript 标准开发的议程和讨论。  
- 🔔 **通知设置**：用户需登录 GitHub 才能更改通知设置以接收更新。  
- 🍴 **复刻与星标**：项目已被复刻 195 次，获得 1.1k 星标，显示较高的社区关注度。  
- 🛠 **功能选项**：提供代码、问题、拉取请求、操作和安全等导航选项，方便协作与管理。  
- ❌ **加载错误**：页面可能出现加载错误，需重新加载以解决问题。  
- 🔍 **更多导航**：提供额外的导航选项（如 Insights），便于深入查看项目数据和分析。

---

### [GitHub - tc39/proposal-seeded-random: 关于可生成可复现随机数序列的新 SeededPRNG 类的提案](https://github.com/tc39/proposal-seeded-random)

**原文标题**: [GitHub - tc39/proposal-seeded-random: Proposal for a new SeededPRNG class that yields reproducible sequences of random numbers.](https://github.com/tc39/proposal-seeded-random)

该提案旨在为 JavaScript 引入一个新的`Random.Seeded`类，用于生成可复现的伪随机数序列，适用于需要确定性随机数的场景（如测试、游戏、CSS 自定义绘制等）。

- 🌱 **提案概述**：新增`Random.Seeded`类，支持通过种子或状态初始化，生成可预测的随机数序列，解决现有`Math.random()`不可复现的问题。
- 🛠️ **核心功能**：
  - 构造函数支持`Uint8Array`（种子/状态）或`Number`（0-255 简写种子）。
  - `.random()`方法生成`[0,1)`范围内的浮点数（算法与 Rust/numpy 一致）。
  - `.seed()`生成子 PRNG 的随机种子，`.getState()`/`.setState()`实现状态序列化。
- 🔒 **安全设计**：默认使用 ChaCha12 算法，确保跨浏览器/版本的序列一致性，且种子熵充足。
- 🎮 **应用场景**：
  - CSS Houdini 绘制回调（如固定随机边框样式）。
  - 测试框架（CI 与本地结果一致）。
  - 游戏防存档作弊（固定随机事件序列）。
- ⚠️ **限制**：数字种子仅支持 0-255，避免低熵误用；状态为 112 字节，种子为 32 字节。
- 🔗 **生态整合**：与"更多随机方法"提案协同，未来扩展`Random.Seeded`的方法（如`randomInt()`）。
- 📜 **开源**：MIT 协议，GitHub 仓库含规范草案、示例及讨论（如 Issue #26/#35）。

---

### [GitHub - tc39/proposal-is-error: Error.isError 的 ECMAScript 提案、规范及参考实现](https://github.com/tc39/proposal-is-error)

**原文标题**: [GitHub - tc39/proposal-is-error: ECMAScript Proposal, specs, and reference implementation for Error.isError](https://github.com/tc39/proposal-is-error)

该仓库是 ECMAScript 关于 Error.isError 的提案及实现，已归档为只读状态，包含规范、参考实现及使用案例。

- 📅 **归档日期**：2025 年 5 月 28 日由所有者归档，现为只读状态。  
- 🚀 **提案状态**：处于 TC39 流程的 Stage 4，由@ljharb 起草。  
- 🔍 **核心功能**：提供`Error.isError`方法，用于可靠检测值是否为原生 Error 实例（解决跨域/iframe 场景下`instanceof`不可靠的问题）。  
- 💡 **使用场景**：  
  - 调试与错误报告（识别原生错误类型）  
  - 序列化（如 RunKit 需安全重构值）  
  - `structuredClone`的预判行为  
  - 跨 iframe 错误收集验证  
- 📜 **规范链接**：可通过[HTML 形式](tc39.es/proposal-is-error/)查看。  
- ⚖️ **许可协议**：MIT 许可证。  
- 🌟 **仓库数据**：126 星标、2 分叉、13 关注者。  
- 🛠️ **贡献者**：Jordan Harband（@ljharb）和 Sahin Deniz（@seahindeniz）。  
- ⚠️ **技术背景**：针对`Symbol.toStringTag`导致的`Object#toString`不可靠问题，补充 Error 实例的内部槽检测。

---

### [OpenJS 基金会成为 40 多个 JavaScript 项目的 CNA](https://socket.dev/blog/openjs-foundation-is-now-a-cna)

**原文标题**: [OpenJS Foundation Is Now a CNA for 40+ JavaScript Projects U...](https://socket.dev/blog/openjs-foundation-is-now-a-cna)

Vite 发布了基于 Rust 的打包工具 Rolldown-Vite 的技术预览版，旨在提供更快的构建速度和更低的内存占用，作为 Vite 的直接替代方案。

- 🚀 Vite 发布 Rolldown-Vite 技术预览版  
- 🔧 基于 Rust 开发的打包工具  
- ⚡ 提供更快的构建速度  
- 💾 显著降低内存使用  
- 🔄 可作为 Vite 的直接替代方案

---

### [Node.js 技术指导委员会拒绝支持功能悬赏计划 - Soc...](https://socket.dev/blog/node-js-tsc-declines-to-endorse-feature-bounty-program)

**原文标题**: [Node.js TSC Declines to Endorse Feature Bounty Program - Soc...](https://socket.dev/blog/node-js-tsc-declines-to-endorse-feature-bounty-program)

Vite 发布了基于 Rust 的打包工具 Rolldown-Vite 的技术预览版，旨在提供更快的构建速度和更低的内存占用，可作为 Vite 的直接替代方案。

- 🚀 Vite 推出 Rolldown-Vite 技术预览版  
- 🔧 基于 Rust 开发的打包工具  
- ⚡ 显著提升构建速度  
- 💾 大幅降低内存使用  
- 🔄 可作为 Vite 的直接替代方案  
- 📅 发布于 2025 年 5 月 30 日  
- ✍️ 作者：Sarah Gooding

---

### [Bun v1.2.15 | Bun 博客](https://bun.sh/blog/bun-v1.2.15)

**原文标题**: [Bun v1.2.15 | Bun Blog](https://bun.sh/blog/bun-v1.2.15)

本次 Bun 版本更新修复了 11 个问题，涉及多项功能改进和兼容性提升，包括安全审计、包管理、Node.js 兼容性增强及多项 Bug 修复。

- 🛠️ 修复 11 个问题（261 个👍），涵盖安全审计、依赖管理、Node.js 兼容性等  
- 🔍 `bun audit`：扫描依赖项的安全漏洞，类似`npm audit`  
- 📦 `bun pm view`：查看 npm 包的元数据（如版本、依赖等）  
- 🚀 `bun init`：新增规则引导使用 Bun 替代 Node.js/Vite/npm/pnpm  
- ⚙️ 实现`node:vm SourceTextModule`和`node:perf_hooks createHistogram`  
- 📥 支持多种安装方式：`curl`、`npm`、`PowerShell`、`scoop`、`brew`、`Docker`  
- 🔄 `bun upgrade`：升级 Bun 版本  
- 🛡️ 安全漏洞修复：`esbuild`依赖的中等风险漏洞（GHSA-67mh-4wv8-2f99）  
- 🔧 `BUN_OPTIONS`环境变量：支持全局命令行参数配置  
- 🌐 前端开发支持：Chrome DevTools 新增“自动工作区”功能，可直接在浏览器编辑文件  
- 📊 Node.js 兼容性改进：  
  - 支持`node:vm`模块的`SourceTextModule`  
  - 实现`node:worker_threads`的`Worker.getHeapSnapshot`  
  - 新增`node:perf_hooks`的`createHistogram`  
- ⚡ JavaScriptCore 升级：修复`await`崩溃、`NaN`优化等边缘问题  
- 🐞 Bug 修复：  
  - 解析器修复（如 JSX 命名空间属性、`node:assert`模块等）  
  - 运行时修复（如`Bun.plugin`稳定性、`BunRequest.clone()`保留`cookies`等）  
  - Node.js 兼容性修复（如 DNS 内存泄漏、TLS 密码套件错误等）  
  - TypeScript 类型修复（如`spyOn`类型推断）  
- 🙏 感谢 15 位贡献者！

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的命令行应用开发工具，允许开发者使用 React 组件构建交互式 CLI 应用。它支持 Flexbox 布局，并提供了丰富的组件和钩子来简化 CLI 开发。

- 🚀 **React 风格**：使用熟悉的 React 组件和钩子开发 CLI 应用。
- 📦 **Flexbox 布局**：通过 Yoga 引擎支持 CSS 类似的布局属性。
- 🎨 **样式支持**：支持文本颜色、背景色、加粗、斜体等多种样式。
- 🔄 **动态更新**：支持实时更新和交互式输入处理。
- 📊 **静态输出**：使用 `<Static>` 组件渲染永久性输出，如日志或已完成任务列表。
- 🛠 **丰富的组件**：包括 `<Text>`, `<Box>`, `<Newline>`, `<Spacer>`, `<Transform>` 等。
- 🎮 **钩子支持**：提供 `useInput`, `useApp`, `useStdin`, `useStdout`, `useStderr`, `useFocus` 等钩子。
- 📝 **测试友好**：支持使用 `ink-testing-library` 进行测试。
- 🔧 **开发者工具**：支持 React Devtools 进行调试和组件检查。
- 🌟 **社区支持**：被多个知名项目如 Gatsby、Prisma、Shopify CLI 等使用。

Ink 是一个强大且灵活的工具，适合构建复杂的命令行界面应用。

---

### [Docusaurus 3.8 | Docusaurus](https://docusaurus.io/blog/releases/3.8)

**原文标题**: [Docusaurus 3.8 | Docusaurus](https://docusaurus.io/blog/releases/3.8)

Docusaurus 3.8 发布，带来构建性能优化、新功能和未来标志（Future Flags）以支持 Docusaurus 4 的准备工作。

- 🚀 **性能提升**：通过多项优化改进构建基础设施性能，包括两个新的 Docusaurus Faster 选项。
- 🔧 **Docusaurus Faster**：通过启用实验性标志大幅提升构建速度，推荐使用 `experimental_faster: true` 快捷配置。
- 💾 **持久缓存**：启用 Rspack 持久缓存，使后续构建速度提升 2-5 倍，需保留 `./node_modules/.cache` 文件夹。
- � **工作线程**：引入 Node.js 工作线程池，静态站点生成时间平均缩短 2 倍。
- ⚡ **其他优化**：包括优化 macOS 开发服务器启动时间、Git 命令队列管理、SVG 精灵使用等。
- 🏷️ **未来标志**：引入 Docusaurus v4 的未来标志，帮助逐步适配即将到来的重大变更。
- 🎨 **CSS 层叠**：实验性支持 CSS 层叠，提供更好的 CSS 规则控制，减少对插入顺序的依赖。
- 🔄 **postBuild() 变更**：移除 `head` 属性，简化插件生命周期方法签名。
- 🌐 **翻译更新**：新增土耳其语、波兰语、中文和日语的主题翻译。
- 🛠️ **维护更新**：支持 Node.js 24 和 TypeScript 5.8，移除无用或未维护的 npm 包。
- 📦 **其他变更**：包括文档版本下拉菜单支持自定义版本、Bun 标签转换支持、更稳定的 CSS 类等。

---

### [Ember 6.4 版本发布](https://blog.emberjs.com/ember-released-6-4/)

**原文标题**: [Ember 6.4 Released](https://blog.emberjs.com/ember-released-6-4/)

Ember 6.4 版本发布，包含 Ember.js、Ember CLI 和 EmberData 的更新。此次 Ember.js 是 LTS（长期支持）候选版本，注重稳定性和错误修复，而非新功能。同时启动了 6.5 版本的测试周期，鼓励社区参与测试。  

- 🚀 **Ember.js 6.4 发布** - 作为 LTS 候选版本，强调稳定性，包含 4 个错误修复和性能改进。  
- ⚠️ **潜在破坏性变更** - 放弃对 TypeScript 4.9 的支持，要求使用`verbatimModuleSyntax`。  
- 🔄 **EmberData 更新** - 发布 5.4 版本，未来将更名为 WarpDrive，更多细节将在后续博客中介绍。  
- 🛠️ **Ember CLI 6.4 改进** - 包含 4 个错误修复和 1 个新功能（更新`ember-try`至 v4）。  
- 📦 **升级指南** - 推荐使用`ember-cli-update`工具升级，支持灵活调整 Ember 和 EmberData 版本。  
- 🙏 **社区致谢** - 感谢开源社区的贡献和支持，使 Ember 项目持续发展。

---

### [JSPM - JSPM 4.0 版本发布](https://jspm.org/jspm-4.0-release)

**原文标题**: [JSPM - JSPM 4.0 Release](https://jspm.org/jspm-4.0-release)

JSPM 4.0 发布，采用基于标准的约定优于配置的工作流程，为浏览器中原生 ESM 提供了现代开发支持，包括零配置构建、热重载服务器和简化的依赖管理。

- 🚀 **JSPM 4.0 发布**：全新标准化工作流程，支持原生 ESM 和导入映射。  
- 📂 **零配置操作**：`jspm install`自动生成`importmap.js`，`jspm serve`支持热重载和 TypeScript 类型剥离。  
- 🌐 **基于标准**：依赖原生 ES 模块、导入映射和浏览器语义，减少工具链学习成本。  
- 🔍 **调试简化**：无需源映射，浏览器工具直接支持标准模块。  
- 📦 **包管理革新**：`importmap.js`作为包管理产物，由 JSPM 自动维护，无需手动编辑。  
- 🔄 **热重载服务器**：`jspm serve`支持即时刷新、TypeScript 和导入映射感知。  
- 🛠️ **生产构建**：`jspm build`沿用运行时语义，优化入口点明确。  
- 🔮 **未来方向**：强化无 CDN 本地工作流和沙盒支持，注重标准与安全性。  
- 📚 **下一步**：阅读[入门指南](https://jspm.org/docs)或试用新版本反馈意见。

---

### [为什么在 JavaScript 中 2025/05/28 和 2025-05-28 是不同的日期？](https://brandondong.github.io/blog/javascript_dates/)

**原文标题**: [Why are 2025/05/28 and 2025-05-28 different days in JavaScript?](https://brandondong.github.io/blog/javascript_dates/)

在 JavaScript 中，日期字符串的解析行为因格式不同而存在差异，导致`2025/05/28`和`2025-05-28`可能被解析为不同的日期。以下是关键点总结：

- 🕰️ `2025/05/28`被解析为本地时区时间，而`2025-05-28`（ISO 格式）被解析为 UTC 时间，可能导致日期相差一天。
- 🔄 不同浏览器对日期字符串的解析行为不一致，尤其是在 ES5 和 ES6 规范变更期间。
- 📅 在 ES5 中，ISO 日期格式（如`2025-05-28`）被解析为 UTC 时间，而其他格式（如`2025/05/28`）被解析为本地时间。
- 🚀 ES6 规定，缺少时区偏移的日期时间字符串应被解析为本地时间，但 ISO 日期格式仍被解析为 UTC 时间。
- 🐛 浏览器实现存在多次变更，例如 Chrome 在解析行为上多次切换，最终与 Firefox 的行为一致。
- ⏳ Temporal API 将引入新的日期时间处理方式，避免时区歧义，要求明确指定时区或偏移量。
- 🤯 日期解析非常宽松，甚至包含无关文本的字符串也可能被成功解析（如`"it is wednesday..."`被解析为有效日期）。

---

### [啥](https://www.destroyallsoftware.com/talks/wat)

**原文标题**: [
    Wat
  ](https://www.destroyallsoftware.com/talks/wat)

"Destroy All Software" 是一个提供编程相关内容的平台，包括高级主题的教程、互动课程和会议演讲等。

- 🎥 提供屏幕录像教程，涵盖 Unix、TDD、OO 设计、Vim、Ruby 和 Git 等高级主题，每两周更新一次，时长 10 至 15 分钟。
- 💡 包含 Gary Bernhardt 在 CodeMash 2012 上的闪电演讲，但该演讲不代表任何人的实际观点。
- 📚 提供互动课程 "Execute Program"，涵盖 TypeScript、现代 JavaScript、SQL、正则表达式等，包含数百个在浏览器中运行的交互式代码示例。
- 🔗 平台还提供程序员指南、会议演讲、公司博客、联系方式等内容。
- 🔒 包含隐私政策、常见问题解答和最终用户许可协议（EULA）等法律信息。

---

### [DevTools 中的性能调试 - YouTube](https://www.youtube.com/watch?v=BHqxD9qr6Gw)

**原文标题**: [Performance debugging in DevTools - YouTube](https://www.youtube.com/watch?v=BHqxD9qr6Gw)

该文本列出了与平台（可能是 YouTube）相关的多个链接或版块，涵盖版权、联系方式、开发者信息、隐私政策等内容。  

- 📜 关于 - 平台的基本介绍或相关信息  
- 📰 新闻 - 提供最新的资讯或动态  
- ©️ 版权 - 版权声明及保护信息  
- 📞 联系我们 - 用户与平台沟通的渠道  
- 🛠️ 创作者 - 平台内容创作者的资源或信息  
- 📢 广告投放 - 商业推广或广告合作相关  
- 👨💻 开发者 - 开发者资源或 API 信息  
- 📝 条款 - 平台使用条款及条件  
- 🔒 隐私 - 隐私政策及数据保护措施  
- 🛡️ 原则与安全 - 平台运营准则和安全规范  
- ⚙️ YouTube 的运作方式 - 平台功能或算法的说明  
- 🧪 测试新功能 - 体验或试用最新推出的功能  
- © 2025 Google LLC - 版权归属及年份声明

---

### [SaaS 应用全教程 2025 | 7 天内用 Next JS、Supabase 和支付功能上线你的 SaaS 项目 - YouTube](https://www.youtube.com/watch?v=XUkNR-JfHwo&utm_source=cooper-press&utm_medium=newsletter&utm_campaign=jsm-saas&utm_content=05-28-25&dub_id=rtW4ncihZM1bEY70)

**原文标题**: [SaaS App Full Course 2025 | Launch Your SaaS in Under 7 Days with Next JS, Supabase & Payments - YouTube](https://www.youtube.com/watch?v=XUkNR-JfHwo&utm_source=cooper-press&utm_medium=newsletter&utm_campaign=jsm-saas&utm_content=05-28-25&dub_id=rtW4ncihZM1bEY70)

该文本列出了与平台（可能是 YouTube 或类似服务）相关的多个链接或版块，涵盖信息、版权、联系方式、开发者信息等内容。

- ℹ️ 关于：平台的基本信息介绍  
- 📰 新闻：相关动态或公告  
- ©️ 版权：版权声明与保护条款  
- 📞 联系我们：用户沟通渠道  
- 🛠️ 创作者：内容创作者相关信息  
- 📢 广告投放：商业推广与合作  
- 👨💻 开发者：开发团队或 API 信息  
- 📜 条款：使用条款与条件  
- 🔒 隐私：隐私政策说明  
- 🛡️ 原则与安全：平台准则与安全措施  
- ⚙️ 平台运作机制：如 YouTube 的运营方式  
- � 测试新功能：实验性功能体验  
- ⏳ 年份标识：© 2025 Google LLC

---

### [React，可视化 —— react.gg](https://react.gg/visualized)

**原文标题**: [React, visualized âÂ react.gg](https://react.gg/visualized)

网页开发的历史背景对于理解 React 的诞生至关重要，不同时期的技术如 jQuery、Backbone 和 AngularJS 都为 React 的创建提供了灵感。

- 🌐 了解 React 需先掌握其历史背景  
- 🔄 jQuery、Backbone 和 AngularJS 等技术影响了 React 的诞生  
- 💡 每个时代的技术都为 React 提供了不同的灵感

---

### [JavaScript 框架渲染 DOM 的 3 种方式 - YouTube](https://www.youtube.com/watch?v=0C-y59betmY)

**原文标题**: [The 3 Ways JavaScript Frameworks Render the DOM - YouTube](https://www.youtube.com/watch?v=0C-y59betmY)

这是一个关于网站或平台（可能是 YouTube）的页脚导航菜单，包含常见的信息分类和链接选项。

- 📜 关于 - 提供平台的基本信息和背景。  
- 📰 新闻 - 查看最新动态和公告。  
- ©️ 版权 - 版权声明和法律信息。  
- 📞 联系我们 - 用户反馈或问题联系渠道。  
- 🛠️ 创作者 - 创作者相关资源或工具。  
- 💼 广告 - 广告投放和商业合作信息。  
- 👨💻 开发者 - 开发者工具和 API 资源。  
- 📝 条款 - 使用条款和服务协议。  
- 🔒 隐私 - 隐私政策和数据保护说明。  
- 🛡️ 政策与安全 - 社区准则和安全措施。  
- ⚙️ YouTube 运作方式 - 平台功能和技术说明。  
- 🧪 测试新功能 - 体验实验性功能入口。  
- ™️ 版权年份 - 标注谷歌公司版权归属（2025 年）。

---

### [使用 Analog 在 30 分钟内用 Angular 构建博客](https://www.telerik.com/blogs/build-blog-angular-under-30-minutes-using-analog)

**原文标题**: [
	Build a Blog with Angular in Under 30 Minutes Using Analog
](https://www.telerik.com/blogs/build-blog-angular-under-30-minutes-using-analog)

使用 Analog 和 Angular 在 30 分钟内构建博客的教程。

- 🚀 **项目创建**：通过`npx create-analog@latest my-analog-blog`命令创建 Analog 项目，选择“Blog”模板和 Shiki 语法高亮器。
- 📝 **添加博客内容**：在`src/content/blog/`目录下添加 Markdown 文件，支持 Front Matter 元数据（如标题、描述、封面图等）。
- 🎨 **样式与布局**：可选择使用 Tailwind CSS 快速美化博客，并通过组件模板自定义文章列表和详情页的样式。
- 🔍 **内容路由**：利用`@analogjs/content`包自动解析 Markdown 文件，动态生成路由（如`/blog/[slug]`）。
- ⚡ **静态页面预渲染**：配置`vite.config.ts`中的`prerender`选项，实现博客页面的静态化，提升 SEO 和性能。
- 🗺️ **自动生成站点地图**：启用`sitemap`功能，帮助搜索引擎索引内容。
- 📂 **扩展功能**：支持在`src/app/pages`中添加 Markdown 页面（如关于页），并通过`meta`字段优化 SEO。
- 🔧 **代码高亮**：内置 Shiki 和 PrismJS 支持，可高亮显示代码块。
- 🌐 **示例与源码**：提供完整代码示例，便于快速上手和进一步定制。

---

### [模拟 | 模拟](https://analogjs.org/)

**原文标题**: [Analog | Analog](https://analogjs.org/)

Analog 是一个基于 Vite 的 Angular 框架，支持 SSR 和 SSG，并提供文件路由和 API 路由功能。

- ⚡ 使用 Vite 进行服务、构建和测试（Vitest）  
- 🔄 支持混合 SSR/SSG，适用于 Angular 应用  
- 📂 提供文件式路由和 API 路由支持

---

### [RedwoodSDK 是一个面向 Cloudflare 的 React 框架](https://rwsdk.com/blog/your-react-meta-framework-feels-broken)

**原文标题**: [RedwoodSDK is a React framework for Cloudflare](https://rwsdk.com/blog/your-react-meta-framework-feels-broken)

现代 React 元框架让开发体验变得复杂，开发者常感到代码与心智模型脱节，框架的抽象层掩盖了底层逻辑，导致调试和理解困难。RedwoodSDK 旨在回归 JavaScript 本质，减少魔法语法，直接利用 Web API，提供透明、可组合的开发体验。

- 🤯 开发者常感到现代 React 框架的代码结构复杂，路由系统像一门新语言，而非直观的模式匹配。  
- 🎭 框架承诺简化开发，实则引入间接层，抽象甚至掩盖了开发者自己的代码，导致调试和理解困难。  
- 🔮 框架中的“魔法”功能（如特殊导出、生成类型）增加了不透明性，开发者需依赖框架规则而非 JavaScript 本身。  
- ⚔️ 许多框架要求开发者放弃 JavaScript 心智模型，与 Web 平台对抗，而非利用其原生能力。  
- 🛠️ RedwoodSDK 提出解决方案：无魔法语法、直接使用 Web API（如 fetch）、本地与生产环境一致、基于 TypeScript/React/Vite 构建。  
- 📂 对比示例：Next.js 和 Remix 通过文件约定和隐藏规则实现路由，而 RedwoodSDK 显式定义路由，返回 JSX 或响应对象，保持代码透明。  
- 🌐 核心理念：无需框架伪装成新语言，直接基于 Web 标准（HTTP、JS 模块）开发，减少构建层抽象。  
- 🚀 RedwoodSDK 特点：零魔法、Web API 原生支持、一键部署、默认可组合性，让开发者专注业务逻辑而非框架规则。  
- 🔥 设计哲学：从第一性原理重构，追求“显而易见的简单”，使框架近乎“隐形”，仅依赖 TypeScript、React、Vite 和 Cloudflare。

---

### [无服务器、无数据库：利用`transformers.js`在 Astro 中实现更智能的相关文章推荐 | alexop.dev](https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/)

**原文标题**: [No Server, No Database: Smarter Related Posts in Astro with `transformers.js` | alexop.dev](https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/)

本文介绍了如何在 Astro 博客中使用 Hugging Face 的 transformers.js 实现基于嵌入向量的智能相关文章推荐功能，无需服务器或数据库支持。

- 🚀 **挑战与解决方案**：作者受到一篇关于嵌入向量的技术博客启发，决定在自己的 Astro 博客中实现更智能的相关文章推荐功能，替代传统的标签匹配方式。  
- 🔍 **嵌入向量优于标签**：嵌入向量通过数值向量捕捉文本的语义，使内容相似的文章能够被关联起来，而不仅仅是依赖标签匹配。  
- 📊 **向量与余弦相似度**：使用余弦相似度计算向量之间的相似性，例如“cat”和“kitty”的向量更接近，而“dog”则略有不同。  
- ⚙️ **Transformers.js 的应用**：通过 transformers.js 直接在 JavaScript 中运行 Hugging Face 模型，无需 Python 或服务器支持，嵌入向量生成和相似度计算均在浏览器或 Node.js 中完成。  
- 📂 **工作流程**：  
  - 加载博客的 Markdown 文件并去除格式化为纯文本。  
  - 使用 transformers.js 生成嵌入向量。  
  - 计算所有文章之间的余弦相似度。  
  - 为每篇文章保存前 5 篇最相关的文章到 JSON 文件。  
  - 在 Astro 中展示相关文章。  
- 💡 **成果与收获**：  
  - 无需额外服务器或数据库，所有操作在构建时完成。  
  - 灵活易用，可快速更换模型或方法。  
  - 推荐效果显著优于传统标签匹配。  
- 🔗 **相关资源**：作者提供了脚本代码和示例，并推荐进一步尝试嵌入向量和 Astro 的结合应用。

---

### [您使用的浏览器版本过旧](https://utcc.utoronto.ca/~cks/cspace-old-browser.html)

**原文标题**: [You're using a too-old browser](https://utcc.utoronto.ca/~cks/cspace-old-browser.html)

访问被拦截的提示：用户因使用过时浏览器或爬虫工具（如旧版 Chrome 或 archive.*系列）触发了反爬虫机制，可能影响正常浏览博客或 CSpace。建议升级浏览器或通过大学邮箱联系管理员提供 User-Agent 信息以申诉。特别提醒 archive.*用户因其爬虫行为类似恶意流量，推荐改用行为规范的 archive.org。

- 🚨 访问拦截原因：使用过时浏览器（如旧版 Chrome）或疑似爬虫工具  
- 🤖 背景：2025 年初为抵御 LLM 训练数据爬虫（含伪造 User-Agent）采取防护  
- 📧 申诉方式：通过大学邮箱联系管理员并提交浏览器详细信息  
- ⚠️ 特别警告：archive.*（如 archive.ph）因 IP 伪装等问题被归类为恶意爬虫  
- 🌐 替代方案：推荐使用合规的 archive.org 访问博客内容  
- ✍️ 声明日期：Chris Siebenmann，2025 年 2 月 17 日

---

### [JavaScript 中的多线程：使用 Web Workers - Honeybadger 开发者博客](https://www.honeybadger.io/blog/javascript-web-workers-multithreading/)

**原文标题**: [Multithreading in JavaScript with Web Workers - Honeybadger Developer Blog](https://www.honeybadger.io/blog/javascript-web-workers-multithreading/)

JavaScript 的单线程特性给开发者带来了诸多问题，尤其是长时间运行的任务与 UI 组件同时执行时，会导致网页冻结。HTML5 的 Web Workers API 提供了一种解决方案，允许在独立线程中执行耗时任务，从而避免阻塞主线程。本文探讨了单线程的问题、Web Workers 的实现方式及其应用场景。

- 🚀 JavaScript 单线程问题：长时间运行的任务会阻塞 UI 渲染，导致网页冻结。
- ⚙️ 模拟多线程：使用 setTimeout 和事件驱动架构模拟并发，但并非真正的多线程。
- 🌐 Web Workers：HTML5 提供的 API，允许在独立线程中执行任务，避免阻塞主线程。
- 🔄 并行与并发：Web Workers 支持并行（多 CPU 核心）和并发（单 CPU 核心任务切换）。
- 📊 适用场景：大数据处理、复杂数学计算、后台 I/O 等 CPU 密集型任务。
- 🛠️ 实现方式：创建 Worker 对象、线程间通信（postMessage）、终止 Worker（terminate/close）。
- 📂 外部脚本：使用 importScripts 在 Worker 中加载外部脚本。
- 🎨 OffscreenCanvas：将 Canvas 渲染任务移至 Worker 线程，提升性能。
- 🖥️ Node.js 中的 Worker：Node.js 10.5.0 引入 Worker 线程，用于后端 CPU 密集型任务。
- ⚡ WebAssembly 结合：与 Web Workers 配合，实现高性能计算，不阻塞 UI。
- 🔍 示例代码：提供 GitHub 链接，展示 Web Workers 的实际应用。

---

### [Svelte Flow 1.0 正式发布！ - xyflow](https://xyflow.com/blog/svelte-flow-release)

**原文标题**: [Svelte Flow 1.0 is here! - xyflow](https://xyflow.com/blog/svelte-flow-release)

Svelte Flow 1.0 正式发布，这是一个基于 Svelte 的库，用于构建节点式应用程序，如工作流编辑器、数据管道或可视化编程环境。新版本带来了许多改进和新功能，并完全适配 Svelte 5。

- 🎉 **Svelte Flow 1.0 发布**：经过两次重写，最终版本基于 Svelte 5 构建，性能更优，开发体验更好。
- 📚 **迁移指南**：提供了详细的迁移指南，帮助用户快速升级到新版本。
- 🚀 **新功能**：包括重新连接边、改进的 fitView、键盘导航、更好的无障碍支持等。
- 🔄 **功能对等**：与 React Flow 保持功能对等，未来新功能将同步开发。
- 💡 **开发体验**：通过 TSDoc 注释和改进的文档（包括学习部分和自动生成的 API 参考）提升开发体验。
- ⚡ **全面拥抱 Runes**：利用 Svelte 5 的 signals 和 runes 重构库，简化架构并提升性能。
- 🌍 **社区应用**：多个项目已在生产环境中使用 Svelte Flow，如 Windmill、Sparrow 和 Whimsy。
- 📢 **社区互动**：鼓励用户通过 Discord 提供反馈、分享想法或展示项目。
- 🙏 **致谢**：感谢 Svelte 团队和社区的支持与贡献。

---

### [基于节点的 React UI - React Flow](https://reactflow.dev/)

**原文标题**: [Node-Based UIs in React - React Flow](https://reactflow.dev/)

React Flow 是一个可定制的 React 组件库，用于构建基于节点的编辑器和交互式图表，具有丰富的功能和广泛的用户基础。

- 🚀 **快速入门** - 提供简单的安装方式（npm、pnpm 或 yarn），并内置拖拽、缩放、平移等基础功能。  
- ⚙️ **核心功能** - 支持节点和边的选择、移动、删除等操作，通过键盘快捷键即可完成。  
- 🌟 **开源与专业版** - MIT 许可的开源库，同时提供 React Flow Pro 以支持持续开发和维护。  
- 📊 **用户数据** - 拥有 29.8K GitHub Stars 和 1.42M 每周下载量，被 Stripe、Typeform 等公司广泛使用。  
- 🎨 **高度可定制** - 节点为 React 组件，兼容 Tailwind 和 CSS，支持自定义样式和交互。  
- 🔌 **插件扩展** - 提供 Background、Minimap、Controls 等插件，支持更复杂的应用场景。  
- 🌍 **社区与团队** - 由 xyflow 团队维护，同时开发 Svelte Flow，并积极推动开源生态发展。  
- 📢 **更新动态** - 定期发布版本更新（如 12.6.2、12.6.1），提供详细的变更日志。  
- 🏆 **应用案例** - 覆盖数据处理、聊天机器人、机器学习等多个领域，展示多样化使用场景。

---

### [示例 - Svelte Flow](https://svelteflow.dev/examples)

**原文标题**: [Examples - Svelte Flow](https://svelteflow.dev/examples)

React Flow 提供了丰富的示例和功能，帮助开发者快速实现常见用例，涵盖节点、边、交互、布局、样式等多个方面。

- 🆓 **示例浏览**：提供 MIT 许可和 Pro 订阅的示例，可直接用于项目  
- 🎛️ **功能概览**：展示基础功能，包括节点类型、子流程和工具栏组件  
- 🧩 **节点功能**：  
  - 边缘拖放添加节点  
  - 连接数限制  
  - 自定义节点内容  
  - 删除中间节点不断流  
  - 拖拽手柄限制  
  - 自动连接  
  - 节点重叠检测  
  - 节点大小调整  
  - 近距离自动连接  
  - 压力测试（渲染大量节点）  
  - 节点数据更新  
- 🧵 **边功能**：  
  - 自定义连接线  
  - 自定义边类型  
  - 边标签定制  
  - 边标记添加  
  - 内置边类型  
  - 浮动边（连接视口）  
  - 边重连锚点  
  - 点击连接  
- 🖱️ **交互功能**：  
  - 计算流路径  
  - 自定义上下文菜单  
  - 上下文缩放  
  - 拖放支持（HTML API 或 svelte-draggable）  
  - 连接验证  
- 📐 **布局功能**：  
  - Dagre 层级布局  
  - ELK.js 自动布局  
  - 水平流布局  
  - 子流程嵌套  
- 🎨 **样式功能**：  
  - 基础样式定制  
  - 暗黑模式  
  - Tailwind CSS 支持  
  - Turbo Flow（发光动画边框）  
- ✨ **其他功能**：  
  - 导出为图片  
  - Threlte 3D 可视化  
  - Hello World 入门示例  
  - useSvelteFlow 存储和操作

---

### [帽 — 现代、闪电般快速的 PoW 验证码](https://capjs.js.org/)

**原文标题**: [Cap — Modern, lightning-quick PoW captcha](https://capjs.js.org/)

概述总结  
该内容介绍了 Cap's widget 库的极简特性，重点突出了其体积小巧的优势。  

- ⚡️ **体积极小**：Cap's widget 库非常精简，最小化后仅约 20kb（包括 WASM）。  
- 📏 **高效对比**：比 hCaptcha 小 250 倍，显著提升了加载和运行效率。

---

### [演示 | Cap — 现代、极速的工作量证明验证码](https://capjs.js.org/guide/demo.html)

**原文标题**: [Demo | Cap — Modern, lightning-quick PoW captcha](https://capjs.js.org/guide/demo.html)

概述  
这是一个关于演示内容和资源的简要介绍，包括默认和自定义小部件，并指引更多演示资源的存放位置。  

- 📦 默认小部件  
- 🛠️ 自定义小部件  
- 📂 更多演示资源可在 GitHub 仓库的 demo 文件夹中找到

---

### [GitHub - tiagorangel1/cap: Cap 是一款轻量级、现代的开源 CAPTCHA 替代方案，采用 SHA-256 工作量证明](https://github.com/tiagorangel1/cap)

**原文标题**: [GitHub - tiagorangel1/cap: Cap is a lightweight, modern open-source CAPTCHA alternative using SHA-256 proof-of-work](https://github.com/tiagorangel1/cap)

Cap 是一个轻量级、现代的开源 CAPTCHA 替代方案，采用 SHA-256 工作量证明机制，注重隐私、性能和用户体验。

- 🚀 **开源轻量**：Cap 是完全开源的（Apache 2.0 许可证），核心库仅 12kb，比传统 CAPTCHA 更小巧高效。  
- 🔒 **隐私优先**：基于工作量证明，无需追踪或收集用户数据，符合 GDPR/CCPA 标准。  
- ⚡ **快速集成**：提供 JavaScript 库（@cap.js/widget 和 @cap.js/server），支持 Node.js、Bun、Deno 等运行时，也可通过 Docker 独立部署。  
- 🛠️ **高度定制**：支持自定义前端样式，提供浮动模式和隐形模式，适应不同场景需求。  
- 🤖 **反机器人**：利用 SHA-256 计算难题，对人类友好但能有效阻止自动化攻击。  
- 🌐 **多语言支持**：通过 REST API 和中间件（如 Express、Hono）兼容非 JavaScript 环境。  
- 📊 **功能对比**：相比 reCAPTCHA、hCaptcha 等，Cap 在隐私、开源性和易用性上表现更优。  
- 🐳 **应用场景**：适用于 API 防刷、表单防垃圾、登录防爆破等场景，尤其适合自托管需求。  
- 🔧 **扩展工具**：提供 CLI 命令行工具、Rust WASM 求解器和 Cloudflare 检查点中间件等配套方案。  
- 🔄 **活跃开发**：项目持续更新，拥有 1k+ Stars 和 29 个版本发布，社区贡献活跃。  

（注：省略了部分技术细节和对比表格中的重复信息，聚焦核心亮点。）

---

### [获取失败](https://javascriptweekly.com/link/169959/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/169959/web)

无法总结：获取内容失败，状态码 503。

---

### [GitHub - googleapis/js-genai：Gemini 和 Vertex AI 的 TypeScript/JavaScript SDK](https://github.com/googleapis/js-genai)

**原文标题**: [GitHub - googleapis/js-genai: TypeScript/JavaScript SDK for Gemini and Vertex AI.](https://github.com/googleapis/js-genai)

Google Gen AI SDK 是一个为 TypeScript 和 JavaScript 开发者设计的工具包，用于构建基于 Gemini 的应用程序，支持 Gemini Developer API 和 Vertex AI。以下是关键信息：

- 🚀 **功能概述**：支持 Gemini 2.0 功能，包括内容生成、函数调用、流式处理等。
- 🔒 **安全提示**：避免在客户端代码中暴露 API 密钥，生产环境建议使用服务器端实现。
- 📦 **安装**：通过 `npm install @google/genai` 安装，需 Node.js 18 或更高版本。
- 🔧 **初始化**：支持 Google AI Studio（API 密钥）和 Vertex AI（项目配置）两种方式。
- 🌐 **API 版本**：可设置稳定版（v1）或预览版（v1alpha）API 端点。
- 📂 **模块功能**：
  - `ai.models`：模型查询与元数据检查。
  - `ai.caches`：管理缓存以降低重复提示成本。
  - `ai.chats`：创建本地有状态聊天对象。
  - `ai.files`：上传文件并在提示中引用。
  - `ai.live`：实时交互支持（文本、音频、视频）。
- ⚡ **流式处理**：使用 `generateContentStream` 实现快速响应。
- 🔄 **函数调用**：通过声明函数让 Gemini 与外部系统交互，需四步流程。
- 📝 **内容生成**：支持多种内容结构输入，注意 `FunctionCall` 和 `FunctionResponse` 需显式处理。
- 🔄 **与其他 SDK 区别**：此为 Google Deepmind 官方 SDK，专注新 AI 功能，旧版 SDK 不再支持 Gemini 2.0+。
- 📊 **项目状态**：665 星，71 分支，Apache-2.0 许可，活跃开发中（最新版本 v1.3.0）。

---

### [ReactJust](https://reactjust.dev/)

**原文标题**: [ReactJust](https://reactjust.dev/)

专注于 React 本身  
不引入额外抽象层、内置功能或强制路由方案，自由选择工具与模式  

- ⚛️ 仅使用 React 核心功能，避免复杂抽象  
- 🛠️ 无内置路由等约束，灵活选用第三方工具  
- 🧩 支持自定义开发模式与架构偏好  
- 🚀 强调轻量化，聚焦 React 基础能力

---

### [GitHub - neutralinojs/neutralinojs：轻量级跨平台桌面应用开发框架](https://github.com/neutralinojs/neutralinojs)

**原文标题**: [GitHub - neutralinojs/neutralinojs: Portable and lightweight cross-platform desktop application development framework](https://github.com/neutralinojs/neutralinojs)

Neutralinojs 是一个轻量级、跨平台的桌面应用开发框架，支持使用 JavaScript、HTML 和 CSS 构建应用，并能在 Linux、macOS、Windows、Web 和 Chrome 上运行。它通过扩展 IPC 支持多语言扩展，并提供了轻量化的替代方案，避免像 Electron 那样依赖 Chromium 和 Node.js。

- 🚀 **跨平台开发**：支持 Linux、macOS、Windows、Web 和 Chrome 平台。  
- ⚡ **轻量化设计**：不捆绑 Chromium，利用操作系统自带的浏览器库（如 Linux 的 gtk-webkit2）。  
- 🔧 **多语言扩展**：可通过扩展 IPC 使用任何编程语言扩展功能。  
- 📦 **快速构建**：无需编译，构建时间极短（`neu build` 命令）。  
- 🛠️ **前端框架友好**：支持 React 等框架（如 `neu create hello-react -t codezri/neutralinojs-react`）。  
- 🌐 **内置 WebSocket 和静态服务器**：实现原生操作与 Web 内容服务。  
- 📚 **丰富文档**：提供详细文档（[neutralino.js.org/docs](https://neutralino.js.org/docs)）。  
- 💡 **开源生态**：核心 MIT 许可，依赖多个开源库（如 websocketpp、nlohmann/json 等）。  
- 🤝 **社区支持**：通过 StackOverflow（标签 `neutralinojs`）、Discord 和 GitHub Discussions 交流。  
- 📈 **赞助与贡献**：支持 Patreon 或 GitHub Sponsors，欢迎开发者参与（见 [贡献指南](https://github.com/neutralinojs/neutralinojs/blob/main/CONTRIBUTING.md)）。

---

### [Linkify：一款 JavaScript 插件](https://linkify.js.org/)

**原文标题**: [Linkify: a JavaScript plugin](https://linkify.js.org/)

Linkify 是一个 JavaScript 插件，用于在纯文本中识别链接并将其转换为 HTML <a> 标签，支持多种链接格式和自定义功能。

- 🌐 **功能概述**：Linkify 可自动识别并高亮 URL、#标签、@提及等内容，支持多种链接格式。  
- 📥 **安装方式**：通过 NPM 安装，命令为 `npm install linkifyjs`。  
- 🔗 **支持的链接类型**：  
  - 含协议的 URL（如 `https://github.com`）  
  - 无协议的 URL（如 `www.npmjs.com`）  
  - Emoji 域名（如 `👻💥.ws`）  
  - IP 地址（如 `127.0.0.1`）  
  - 邮箱地址（如 `hello@example.com`）  
  - @提及（如 `@tc39`）和 #标签（如 `#PhotoOfTheDay`）  
- 🛠 **扩展功能**：支持自定义链接格式、多语言和 Emoji，提供 React/jQuery 兼容。  
- 🚀 **性能优势**：轻量（约 11kB）、高测试覆盖率（95%+），兼容现代浏览器。  
- 📚 **文档与源码**：提供详细文档和 GitHub 代码库，开发者可快速上手。  
- ❤️ **开发者信息**：由 @nfrasser 开发，开源且支持社区定制。

---

### [GitHub - sindresorhus/image-type：检测Buffer/Uint8Array的图像类型](https://github.com/sindresorhus/image-type)

**原文标题**: [GitHub - sindresorhus/image-type: Detect the image type of a Buffer/Uint8Array](https://github.com/sindresorhus/image-type)

这是一个名为 `image-type` 的开源项目，用于检测 Buffer/Uint8Array 中的图像类型。

- 🏷️ **项目名称**: image-type  
- 🌟 **Star 数**: 399  
- 🍴 **Fork 数**: 16  
- 📜 **许可证**: MIT  
- 🛠️ **功能**: 检测 ArrayBuffer/Uint8Array 中的图像类型，返回扩展名和 MIME 类型  
- 📦 **安装**: 通过 `npm install image-type` 安装  
- 🖥️ **使用场景**: 支持 Node.js 和浏览器环境  
- 📄 **API**: 返回 `{ext: '扩展名', mime: 'MIME 类型'}` 或 `undefined`  
- ⚠️ **限制**: 需要至少读取 `minimumBytes`（当前为 4100 字节）才能检测文件类型  
- 🖼️ **支持格式**: 包括 jpg、png、gif、webp、psd 等多种图像格式  
- 🔗 **相关项目**: `file-type`（检测更多文件类型）、`image-dimensions`（获取图像尺寸）  
- 🌍 **资源**: 提供 README、MIT 许可证、行为准则和安全策略

---

### [GitHub - faker-js/faker: 在浏览器和 Node.js 中生成大量虚假数据](https://github.com/faker-js/faker)

**原文标题**: [GitHub - faker-js/faker: Generate massive amounts of fake data in the browser and node.js](https://github.com/faker-js/faker)

Faker 是一个用于在浏览器和 Node.js 中生成大量虚假（但逼真）数据的工具库，适用于测试和开发场景。

- 🚀 **功能丰富** - 支持生成人物信息（姓名、性别、职业等）、地理位置（地址、邮编等）、日期、金融数据（账户、交易等）、商业数据（价格、产品描述等）、黑客术语、数字/字符串以及多语言数据。
- 🌍 **多语言支持** - 提供超过 70 种语言环境，可生成符合地区特色的姓名、地址和电话号码等数据。
- ⚠️ **注意事项** - 生成的数据可能偶然与真实信息重合，请勿用于实际通信。
- 📦 **安装简单** - 通过 npm 安装 `@faker-js/faker` 即可使用。
- 🪄 **使用示例** - 支持 ESM 和 CJS 导入方式，提供生成随机用户数据等实用功能。
- 💎 **模块化设计** - 提供详细的 API 文档，支持模板字符串生成数据。
- 🌏 **本地化定制** - 可导入特定语言实例或自定义语言回退策略。
- ⚙️ **随机种子设置** - 通过设置种子值确保生成结果的一致性。
- 🤝 **赞助与贡献** - 项目依靠社区支持，欢迎通过 Open Collective 赞助或提交 PR 贡献代码。
- 📜 **历史与许可** - 项目采用 MIT 许可证，并提供了从原 faker.js 迁移的说明。

---

### [发布 v21.0.0 · sindresorhus/file-type · GitHub](https://github.com/sindresorhus/file-type/releases/tag/v21.0.0)

**原文标题**: [Release v21.0.0 · sindresorhus/file-type · GitHub](https://github.com/sindresorhus/file-type/releases/tag/v21.0.0)

overview summary  
该页面展示了 GitHub 仓库"sindresorhus/file-type"的 v21.0.0 版本更新内容，包含重大变更、改进和修复，同时页面加载时出现错误提示需重新加载。

- 🚨 **错误提示** - 页面加载时出现错误，提示需重新加载。  
- 🔄 **版本发布** - 发布 v21.0.0 版本，时间为 5 月 23 日 11:53。  
- ⚠️ **重大变更** - 要求 Node.js 20 环境，并移除了 Adobe Illustrator (.ai) 文件检测支持。  
- 📌 **MIME 类型修正** - 对 Matroska、FLAC、Apache Parquet 和 Apache Arrow 的 MIME 类型进行了正式 IANA 注册修正。  
- ✨ **功能改进** - 允许直接向导出函数传递选项，并新增`mpegOffsetTolerance`选项。  
- 🛠️ **问题修复** - 修复了部分 PAX TAR 格式的检测问题。  
- 🔍 **导航选项** - 页面提供了代码、问题、拉取请求、安全等导航选项。

---

### [GitHub - PrismarineJS/mineflayer: 使用强大、稳定且高级的 JavaScript API 创建 Minecraft 机器人](https://github.com/PrismarineJS/mineflayer)

**原文标题**: [GitHub - PrismarineJS/mineflayer: Create Minecraft bots with a powerful, stable, and high level JavaScript API.](https://github.com/PrismarineJS/mineflayer)

PrismarineJS 的 Mineflayer 是一个用于创建 Minecraft 机器人的强大、稳定且高级的 JavaScript API，支持从 Python 使用。

- 🚀 **功能强大**：支持 Minecraft 1.8 到 1.21 版本，提供实体追踪、方块查询、物理运动、攻击实体、物品管理等功能。
- 📚 **文档丰富**：包含教程、API 参考、常见问题解答及历史变更记录，适合初学者和高级用户。
- 🔧 **易于使用**：通过简单的 npm 安装即可开始使用，支持多种认证方式，包括微软账户和离线模式。
- 🌍 **多语言支持**：提供多种语言的文档，包括英语、中文、西班牙语等。
- 🛠️ **模块化设计**：依赖多个模块如 minecraft-protocol、prismarine-physics 等，实现高度可扩展性。
- 🎥 **可视化支持**：通过 prismarine-viewer 项目，可以在浏览器中实时查看机器人的行为。
- 🔌 **插件生态**：支持第三方插件，如 pathfinder、prismarine-viewer 等，扩展机器人功能。
- 🏗️ **社区活跃**：有大量使用 Mineflayer 的项目，如 Voyager、Chaoscraft 等，社区贡献者众多。
- 📜 **开源许可**：采用 MIT 许可证，允许自由使用和修改。
- 🧪 **测试完善**：提供详细的测试指南，支持针对特定版本或功能的测试。

---

### [一丝不苟](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=may30th2025)

**原文标题**: [Meticulous](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=may30th2025)

Meticulous AI 提供了一种无需编写和维护测试的自动化测试解决方案，通过记录用户交互并生成持续演化的测试套件，覆盖所有边缘情况和用户流程，帮助团队快速迭代并确保代码质量。

- 🚀 **无需编写测试** - Meticulous AI 通过记录用户交互自动生成测试，无需手动编写或维护测试用例。  
- 🔍 **全面覆盖** - 监控代码分支和用户流程，确保覆盖所有边缘情况和功能。  
- ⚡ **快速反馈** - 在合并代码前查看 PR 对用户流程的影响，避免回归问题。  
- 🛠️ **无干扰集成** - 通过简单的脚本标签添加到开发、预发布或生产环境，轻松开始记录会话。  
- 🔄 **自动演化** - 测试套件随应用功能更新自动调整，始终保持最新状态。  
- � **高效并行测试** - 支持大规模并行测试，数千次测试可在 120 秒内完成。  
- 🤝 **兼容现有测试** - 可作为补充或完全替代现有测试套件。  
- 💬 **用户见证** - 来自 Dropbox、WithPower 等企业的工程师认可其节省时间和提升信心的效果。  
- 📦 **多框架支持** - 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流前端框架。  
- 🔒 **安全可靠** - 提供生产环境录制选项，同时内置安全防护措施。

---

### [Notion 如何在 Amazon RDS 上借助 pganalyze 大规模运行 PostgreSQL](https://pganalyze.com/blog/how-notion-runs-postgres-at-scale?utm_campaign=postgresweeklyclassified05292025%20)

**原文标题**: [How Notion Runs PostgreSQL at Scale on Amazon RDS with pganalyze](https://pganalyze.com/blog/how-notion-runs-postgres-at-scale?utm_campaign=postgresweeklyclassified05292025%20)

Notion 使用 pganalyze 在 Amazon RDS 上规模化运行 PostgreSQL 的经验分享，展示了如何通过工具优化数据库性能、提升团队协作效率，并支持业务快速增长。

- 🚀 **Notion 的快速增长**：自 2015 年成立以来，Notion 用户量激增，尤其是在 2021 年 TikTok 病毒式传播后，数据库扩展成为关键挑战。
- 🔍 **面临的挑战**：早期单一 PostgreSQL 数据库在用户增长后出现性能问题，包括宕机、VACUUM 效率低和扩展限制。
- 🛠️ **解决方案**：通过分片核心数据库并采用 pganalyze 工具，Notion 获得了对 PostgreSQL 内部运行的深度洞察。
- 📊 **性能优化案例**：通过调整 GIN 索引类型，实现了 733% 的性能提升，查询时间从 5000 毫秒降至 600 毫秒。
- ⚡ **快速问题诊断**：pganalyze 帮助团队快速识别并解决新功能导致的查询负载问题，避免了生产环境的影响。
- 👥 **团队协作提升**：从基础设施团队扩展到产品工程师，pganalyze 的集成使用（如与 Okta 结合）促进了跨团队自主解决问题。
- 📈 **扩展与迁移**：在从 32 个数据库扩展到 96 个的过程中，pganalyze 确保了查询行为的一致性，支持了无缝迁移。
- 🔮 **未来计划**：Notion 计划探索动态分片和保持 PostgreSQL 版本更新，以应对更大规模的工作负载。
- 💡 **经验总结**：早期解决容量问题、选择合适的工具和策略对数据库的可扩展性和可靠性至关重要。

---

### [不只是感觉，Stack Overflow 开发者调查真的来了 - Stack Overflow](https://stackoverflow.blog/2025/05/29/not-just-a-vibe-the-stack-overflow-developer-survey-is-really-here/)

**原文标题**: [Not just a vibe, the Stack Overflow Developer Survey is really here - Stack Overflow](https://stackoverflow.blog/2025/05/29/not-just-a-vibe-the-stack-overflow-developer-survey-is-really-here/)

Stack Overflow 开发者调查迎来第 15 周年，聚焦开发者幸福感、薪资趋势与 AI 工具影响，邀请全球开发者参与数据收集，共同揭示行业现状与未来方向。  

- 🎉 **15 周年里程碑**：Stack Overflow 开发者调查与 YouTube、Wikipedia 等社区一样持续 15 年，探讨 AI 时代开发者对在线社区的依赖变化。  
- 😔 **开发者幸福感下降**：80% 开发者对工作不满或 complacent，薪资与远程工作对满意度的影响成为焦点，高薪群体（如后端、全栈开发者）满意度显著提升。  
- 💰 **薪资波动显著**：2024 年多国开发者薪资平均下降 7%，英国工程经理（+21%）与乌克兰全栈开发者（-44%）薪资变化两极，德国薪资几乎无变动。  
- 🤖 **AI 工具使用增长但信任分化**：76% 开发者计划或正在使用 AI 工具，但信任度因地区/经验异（印度 59% 信任 vs 德国 42% 不信任），资深开发者更认可 AI 提升效率。  
- 🔍 **2025 年新调查方向**：关注 AI 代理工作流应用、职业转型与 AI 的关系，以及社区动态如何被 AI 重塑，强调开发者真实声音的重要性。  
- 🌍 **呼吁参与**：通过填写调查贡献数据，帮助全球开发者社区洞察技术趋势与挑战。

---

### [CSS 我的世界](https://benjaminaster.com/css-minecraft/)

**原文标题**: [CSS Minecraft](https://benjaminaster.com/css-minecraft/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

例如：  

文本内容：  
"全球变暖导致极端天气事件增加，科学家呼吁减少碳排放。政府应制定更严格的环保政策，个人也可通过低碳生活贡献力量。"  

输出格式：  

全球变暖加剧极端天气，需集体行动减少碳排放。  
- 🌍 全球变暖导致极端天气事件增多  
- 🔬 科学家呼吁大幅减少碳排放  
- 🏛️ 政府需加强环保政策  
- 🚲 个人可通过低碳生活助力  

请提供您的文本内容，我会立即为您总结！

---

### [GitHub 笔记问题](https://simonwillison.net/2025/May/26/notes/)

**原文标题**: [GitHub issues for notes](https://simonwillison.net/2025/May/26/notes/)

GitHub Issues 是一个近乎完美的笔记本工具，具备丰富的功能和灵活性，适合公开和私密笔记管理，但缺乏离线同步支持。

- 📝 **免费且无限使用** - 适用于公开和私有笔记，支持全面的 Markdown 语法和高亮显示多种语言，可直接拖放图片或视频。  
- 🔗 **强大的互连功能** - 通过 URL 链接其他 GitHub 仓库的 issue，自动显示标题并双向关联，遵循可见性规则。  
- 🔍 **高效的搜索能力** - 支持单仓库、跨仓库甚至全平台搜索，便于快速定位内容。  
- 🤖 **全面的 API 支持** - 可通过 API 导出或编辑笔记，结合 GitHub Actions 实现自动化操作。  
- 📱 **缺少离线同步** - 作者仍依赖 Apple Notes 进行手机端离线记录，后续同步至电脑。  
- 🔒 **隐私与安全** - 信任 GitHub 的企业级数据保护，但避免存储敏感信息如密码。  
- 💰 **免费与非自托管优势** - 避免因配置或付费问题导致笔记丢失的风险。  
- ✅ **实用的待办清单** - 支持 Markdown 复选框语法，可关联其他 issue 并自动标记完成状态。  
- 💾 **本地备份实验** - 尝试过如`github-to-sqlite`等工具，但未实现定时自动化备份。  
- 🌍 **跨大陆备份需求** - 作者调侃需纸质笔记能自动备份至多洲才会放弃数字工具。  
- 📊 **强大的扩展性** - 处理海量 issue（如 VS Code 的 19 万+），无需担心容量限制。  
- 🤖 **与 LLM 结合的有趣应用** - 例如用`llm-fragments-github`工具汇总长达 1.5 年的 issue 讨论。  
- 📊 **个人数据统计** - 通过 GraphQL 查询发现已创建 9,413 个 issue 和 39,087 条评论，总计 48,500 条内容。  

（注：原文日期为 2025 年，部分内容可能为未来设想。）

---

### [GitHub - mathiasbynens/small: 各类最小语法有效文件合集](https://github.com/mathiasbynens/small)

**原文标题**: [GitHub - mathiasbynens/small: Smallest possible syntactically valid files of different types](https://github.com/mathiasbynens/small)

该项目收集了各种编程/脚本/标记语言的最小合法文件示例，涵盖文档、音频、可执行文件、图形、视频等多种类型。

- 📁 **项目概述**：收集各类文件格式的最小合法示例，始于一篇关于最小 HTML 文件的博客。  
- 🔍 **文件类型**：包含压缩包、音频、文档、可执行文件、图形、标记语言、视频等。  
- 📜 **开源协议**：作者放弃所有版权及相关权利（CC0）。  
- 🌟 **项目数据**：获 2.2k 星标、192 分叉，38 位贡献者参与。  
- 📂 **主要语言**：以 HTML 为主（68.9%），辅以 COBOL、Java 等。  
- 🔄 **协作欢迎**：鼓励提交 PR 补充新文件类型。  
- 🔗 **资源链接**：提供最小 HTML 示例的博客地址（mathiasbynens.be/notes/minimal-html）。

---

### [你可以像其他文本一样设置替代文本的样式 - Piccalilli](https://piccalil.li/blog/you-can-style-alt-text-like-any-other-text/)

**原文标题**: [
  You can style alt text like any other text - Piccalilli
](https://piccalil.li/blog/you-can-style-alt-text-like-any-other-text/)

文章概述了如何通过 CSS 和 JavaScript 优化图片加载失败时的替代文本（alt text）样式，提升用户体验。作者详细介绍了样式设置和渐进增强的实现方法。

- 📅 **发布日期**：2025 年 5 月 22 日  
- ✍️ **作者**：Andy Bell  
- 🌐 **主题**：通过 CSS 和 JavaScript 美化图片加载失败时的替代文本（alt text）  

- 🖼️ **默认样式问题**：图片加载失败时，alt text 使用浏览器默认样式，视觉效果较差。  
- 🎨 **基础样式优化**：通过 CSS 为`<img>`添加基础样式（如斜体、字号调整、文本平衡等），提升 alt text 的可读性。  
- 🛠️ **渐进增强**：使用 JavaScript 监听图片加载失败事件，添加`data-img-loading-error`属性，进一步优化 alt text 的边框、间距和布局。  
- ⚠️ **浏览器兼容性**：Safari 对 alt text 的渲染存在限制（需单行显示），需注意兼容性问题。  
- 💡 **用户体验**：通过细节设计（如边框、居中布局）提升界面美观度，同时强调编写高质量 alt text 的重要性。  
- 📚 **扩展学习**：作者推荐其 CSS 课程，帮助开发者深入掌握 CSS 技能。  

- 🔗 **示例链接**：文中包含多个 CodePen 示例，展示不同阶段的样式效果。  
- 📧 **订阅服务**：文末推广作者的新闻简报，提供精选设计与开发资源。

---

