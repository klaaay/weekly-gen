### [](https://nextjs.org/blog/turbopack-chunking)

**原文标题**: [How Turbopack chunks your JavaScript | Next.js](https://nextjs.org/blog/turbopack-chunking)

overview summary
- 📦 Turbopack 将 JavaScript 代码拆分为多个“chunk”（块），每个块包含你的代码、依赖包和运行时，本页网络请求中即能看到这些随机命名的文件。
- ⚖️ 分块的核心矛盾在于：请求数量越少越好，但单个块越大越难跨页面复用，两者需要权衡。
- 🧩 最简单的方案是把所有代码打包成一个 chunk——缓存友好但首屏加载过量；按页面分包则避免过度加载，却会丢失共享代码的缓存。
- 🔍 更细粒度（每模块一个 chunk）能精确复用，但会产生数百个网络请求，小文件压缩效率也差。
- 🗂️ 为此引入“chunk group”（分块组）：一组同时加载的 chunk。Turbopack 只合并同一组内的 chunk，避免重复下载。
- 📊 合并两个 chunk 是否划算取决于用户访问路径：若用户从只需 A 的页面跳到需要 A+B 的页面，合并会导致 A 被重复下载；只有两个页面都需要合并后的文件时才节省请求。
- 🧮 Turbopack 按场景概率（单页访问 2/3、多页访问 1/3）和不同页面使用情况加权计算合并的收益与代价。
- 📈 在 nextjs.org 上的测试显示：默认设置比完全不合并减少一半以上请求且代码量略低；全力合并虽进一步减少请求，但总体多传输约 10% 代码，且后续导航可能更重。
- 🆕 Next.js 16.3 引入“generateComponentChunks”：同时生成合并版和未合并版 chunk，运行时根据浏览器已有缓存动态选择更便宜的加载方式，并可配合 `only-if-cached` 指令。
- 📐 新增“Analytics-based chunking”配置：`firstPageLoadPriority` 调节首屏与导航权重、`priorityRoutes` 指定重要路由、`clusters` 定义经常一起访问的路由组，从而让分块策略贴合真实用户行为。
- ✂️ 还通过三项措施减小代码体积：CJS 模块 tree-shaking（`turbopackCjsTreeShaking`）、共享 Turbopack 运行时（`turbopackSharedRuntime`，节省约 10 KB 和一次阻塞请求）、默认不再打包 WebAssembly 和 Web Worker 加载代码。
- 🧪 以上实验功能可在 Next.js 16.3 及以后版本中通过 `next.config.js` 开启试用。

---

### [TREX：运行你的代码的 AI 代码审查 | Greptile](https://www.greptile.com/trex?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=javascriptweekly_primary_sep8)

**原文标题**: [TREX: AI Code Review That Runs Your Code | Greptile](https://www.greptile.com/trex?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=javascriptweekly_primary_sep8)

TREX 是 Greptile 提供的自动化测试工具，会在沙盒中运行 PR 分支，以便发现只有代码实际运行才会暴露的 bug。它能启动服务、模拟输入、点击 UI，并把日志、截图、追踪等证据直接附在 PR 评论上，帮助开发者更快定位问题。相比单纯的代码审查，TREX 能多捕获约 20% 的运行时 bug，并兼容你仓库已有的技术栈和测试配置。

- 🚀 TREX 在沙盒中运行 PR 分支，专门捕捉只在运行时出现的 bug
- ⚙️ 可自动启动服务、模拟输入、点击 UI 流程，并保留日志、截图和追踪记录
- 🔍 工作流程三步：理解 PR 改动 → 在沙盒中运行 → 展示失败详情
- 📎 每条失败发现都附有日志、截图、追踪、脚本或 API 输出等证据
- 🧩 适配仓库原有的依赖、框架和测试环境，无需额外配置
- 🖥️ 支持端到端测试：可 mock 输入、启动开发服务器、用浏览器代理点击界面
- 📈 相比纯代码审查，TREX 能多发现约 20% 的 bug，尤其适合运行时问题
- 📦 Greptile 还提供 Agent、独立性代码验证、个性化学习等更多功能
- 🆓 提供 14 天免费试用，无需信用卡；详情可联系销售获取帮助

---

### [](https://vitest.dev/blog/vitest-5)

**原文标题**: [Vitest 5.0 is out! | Vitest](https://vitest.dev/blog/vitest-5)

Vitest 5 正式发布，这次大版本以性能为核心，带来了全链路的速度优化和多项新功能，如 Trace View、嵌套项目继承、vi.when 条件 Mocking、全新的 Benchmarking API 等，同时收紧了默认行为和断言检查，并引入了一些破坏性变更（要求 Vite ≥6.4 与 Node ≥22.12）。

- 🚀 性能提升显著：基于多套基准应用测量，vm 池、Browser Mode 和大型隔离套件速度提升明显，如 deps-heavy 提升 53%，大型 monolith 提升 19%。
- ⚡ 内联项目如果没有修改 Vite 配置，会复用声明它的 Vite server，共享文件只转换一次。
- 💾 文件系统模块缓存（fsModuleCache）已稳定，可在多次运行和不同 Vitest 进程间复用转换后的模块。
- 🔄 主进程与 worker 之间减少往返通信，预热模块一次即可送达 worker。
- 🧪 vmThreads/vmForks 重写：跨上下文复用编译代码、预预热模块图，并支持 require(esm)。
- 🌐 Browser Mode 更快：预打包自身运行时、启动 Vite 时预热浏览器、自适应打开浏览器会话，并减少每文件往返。
- 📦 安装体积更小：Vitest 现在打包自己的依赖，减少了 node_modules 数量和解析时间。
- 📊 覆盖率更快：v8 provider 有界内存合并与预编译 glob，istanbul 迁移到维护的 @vitest/istanbuljs 包。
- 🕵️ 新增 Trace View（Browser Mode）：记录每个交互、断言和 page.mark 的 DOM 快照，可在 UI/HTML 报告中逐步回放调试。
- 📂 嵌套项目与继承增强：内联项目默认继承根配置，被引用的配置可作为容器定义自己的 projects，--project 支持 -p 简写。
- 🎭 新增 vi.when API：按参数（深比较 + asymmetric matchers）为 spy 定义不同返回值或拒绝行为，并支持 thenReturnOnce/times 限制。
- ⏱️ Benchmarking 重写：bench 作为 test-context 夹具，可在普通 test() 内使用并参与 fixture/断言；支持 writeResult、bench.from() 基线对比和自定义 provider。
- 🌳 Locator 找不到元素时显示 ARIA 树，方便调试；locators 默认真实匹配（exact: true），避免 getByText('Item') 误匹配 "Item 1"。
- 🕰️ Fake timers 现在会同时模拟 Temporal API（基于 @sinonjs/fake-timers v15.4），并可通过 toNotFake 关闭。
- ⚠️ 异步断言（resolves、rejects、toMatchFileSnapshot）未 await 时直接失败；expect.poll 超时会 reject，并提供 AbortSignal。
- 📝 断言与类型系统强化：Matchers 接口引入返回类型和接收类型参数，自定义 matcher 可精确匹配期望参数类型。
- 🧹 clearMocks 默认启用：每个测试前自动 vi.clearAllMocks()，避免调用历史跨测试污染；可用 clearMocks: false 恢复旧行为。
- 📁 报告器与附件统一输出到根目录下的 .vitest 目录，HTML reporter 新增 singleFile 选项生成单文件报告，方便上传 CI 产物。
- 🔁 CLI 新增 --repeats 循环运行所有测试，用于定位 flaky；还提供 vitest doctor 自动推荐加速配置。
- 🔻 其他改进：新增 injectCjsGlobals 开关、coverage 支持子进程/worker 跟踪、junit 命名兼容选项、test.for 支持非 ASCII 等。
- 🔨 破坏性变更：要求 Vite >=6.4.0、Node.js >=22.12.0；建议升级前阅读详细迁移指南。

---

### [](https://vitest.dev/guide/browser/trace-view)

**原文标题**: [Trace View  5.0.0 | Vitest](https://vitest.dev/guide/browser/trace-view)

Trace View 是 Vitest 5.0 起的实验性功能，用于将浏览器交互记录为 DOM 快照，并可在内置查看器中逐步回放；它补充了实时浏览器视图的不足，方便调试失败重试、断言和用户操作，且可与本地 UI、无头浏览器、Vitest UI 或 HTML 报告等不同工作流结合使用。

- 📺 核心价值：记录每次测试的浏览器状态与交互步骤，在视图切换后仍能回看早期测试、失败重试、断言及截图。
- ⚙️ 启用方式：在配置中设置 `browser.traceView: true`，或通过 CLI 传入 `--browser.traceView`；查看器可从浏览器 UI、Vitest UI 和 HTML 报告打开。
- 🎛️ 查看器界面：左栏为步骤列表（含动作、断言、标记、生命周期，失败项标红），右栏为对应步骤的 DOM 快照（交互元素高亮）；选中步骤可跳转到源码位置。
- 🧩 常见场景组合：支持“本地可见浏览器 + 追踪回放”“无头浏览器 + Vitest UI”“独立浏览器窗口 + Vitest UI”以及 CI 下的静态 HTML 报告。
- 🔄 与 Playwright Traces 差异：`browser.traceView` 基于 rrweb，支持所有浏览器提供方，无需外部工具；`browser.trace` 为 Playwright 专属，需 `npx playwright show-trace` 打开；两者可同时启用。
- 📋 自动记录内容：包括 `expect.element(...)` 断言、点击/输入/悬停/滚轮等交互动作，以及测试生命周期事件（如重试后）；每条记录含 DOM 状态、时间、选择器和触发位置。
- ✍️ 自定义追踪标记：可通过 `page.mark()` / `locator.mark()` 添加命名条目，支持回调；用 `vi.defineHelper()` 可让追踪点指向实际调用处而非辅助函数内部。
- 🔁 重试与重复处理：每次尝试独立生成 trace，默认打开最近一次尝试，可在 Report 栏切换查看不同尝试。
- 🖼️ 快照保真度：默认捕获 DOM 树、属性、表单值、同源 CSS、视图尺寸和滚动位置；图片与 canvas 不内联。可选 `inlineImages` 和 `recordCanvas` 增强记录。
- ⚠️ 资源与安全限制：CSS 背景图、字体、非 CORS 图片等外部资源仍依赖原 URL，无法在 HTML 报告中完全便携；`recordCanvas` 启用时需放宽 iframe 沙箱并允许脚本，应谨慎使用。

---

### [](https://vitest.dev/guide/cli#vitest-doctor)

**原文标题**: [Command Line Interface | Guide | Vitest](https://vitest.dev/guide/cli#vitest-doctor)

overview summary
- 🧪 Vitest 提供多种 CLI 命令，涵盖测试运行、监听模式、基准测试、项目初始化、测试列表查看与性能诊断等功能，支持在开发与 CI 环境中自动切换模式。

- 🚀 使用 `vitest` 可启动测试，开发环境默认进入 watch 模式，CI 或非交互终端则自动执行单次运行；支持传入路径过滤器（如 `vitest foobar`）来精准运行匹配文件。
- 📍 Vitest 3 起支持通过 `文件名:行号` 精确定位测试（如 `vitest basic/foo.test.ts:10`），但要求提供完整文件名（相对或绝对路径），不支持行号范围。
- 🔁 `vitest run` 执行单次测试后退出（无监听）；`vitest watch`/`vitest dev` 监听文件变化并自动重跑，在 CI 或非 TTY 环境会回退为 `vitest run`。
- 🔗 `vitest related` 只运行与给定源文件相关的测试，适合与 lint-staged 集成；配合 `--run` 选项可确保命令正常退出。
- 📊 `vitest bench` 仅运行基准测试以比较性能；`vitest init browser` 可初始化浏览器测试项目配置。
- 📋 `vitest list` 以静态解析方式列出匹配的测试（Vitest 5 起默认不实际运行测试），支持 `--json` 与 `--filesOnly` 等输出控制。
- 🩺 `vitest doctor` 是性能诊断工具，通过实际运行测量不同配置（如 pool、isolate、module cache 等）对测试套件速度的影响，并给出优化推荐；它也验证 `isolate: false` 等候选配置是否安全，且对 DOM/jsdom 项目提供 vm 池与 happy-dom 的专项测量。
- 🔌 Shell 自动补全由 @bomb.sh/tab 驱动，在 zsh 中可将 `source <(vitest complete zsh)` 加入 `~/.zshrc`，并支持 npm/pnpm/yarn/bun 等包管理器场景。
- ⚙️ CLI 选项丰富且灵活：支持 camelCase 与 kebab-case 两种写法（如 `--passWithNoTests` 与 `--pass-with-no-tests`），布尔值可用 `--no-` 前缀取反。
- 🎯 常用选项包括：`-r/--root` 设置根路径、`-c/--config` 指定配置文件、`-t/--testNamePattern` 按名称正则过滤测试、`-u/--update` 更新快照、`--reporter` 指定报告器。
- 🌐 浏览器与覆盖率相关选项齐全，例如 `--browser.enabled`、`--browser.headless`、`--coverage.provider`、`--coverage.thresholds.*`、`--coverage.include/exclude` 等。
- 🧠 并发与执行控制选项包括 `--pool`（默认 forks）、`--fileParallelism`、`--maxWorkers`、`--sequence.shuffle.*`、`--sequence.seed`、`--isolate`（默认开启隔离）。
- ⏱️ 超时与重试参数：`--testTimeout`（默认 5000ms）、`--hookTimeout`、`--bail`（失败多少次后停止）、`--retry.count`、`--retry.delay`、`--repeats`。
- 🧩 类型检查选项：`--typecheck.enabled`、`--typecheck.only`、`--typecheck.checker`（tsc/vue-tsc/自定义路径）等。
- 🔬 实验性功能：`--experimental.importDurations.*` 监控导入耗时、`--experimental.diagnostics.*` 输出性能诊断提示、`--experimental.viteModuleRunner` 与 `--experimental.nodeLoader` 控制模块加载方式。
- 💾 `--shard=<index>/<count>` 支持将测试套件分片并行执行；`--merge-reports` 可合并 blob 格式的分片报告，并与 junit 等其他报告器搭配使用。
- 🧹 杂项便捷选项：`--passWithNoTests` 允许无测试时通过、`--clearCache` 清除 Vitest 缓存、`--standalone` 启动服务但不运行测试、`--listTags` 列出所有标签、`--tagsFilter` 按标签表达式过滤测试。

---

### [](https://webkit.org/blog/18227/fixing-top-level-await-in-safari/)

**原文标题**: [  Fixing Top-Level Await in Safari | WebKit](https://webkit.org/blog/18227/fixing-top-level-await-in-safari/)

Safari 27 重写了模块加载器，彻底修复了顶层 await 的规范兼容性问题。文章解释了问题成因、重写过程与测试方法，并鼓励开发者试用。

- 🆕 Safari 27 及 Technology Preview 251 现已完整支持顶层 await，解决此前“访问未初始化变量”等异常。
- ⏸️ 顶层 await 允许在模块顶层使用 await，导入它的模块会被挂起，但不依赖它的兄弟模块仍可并发执行。
- 🧩 旧模块加载器基于已废弃的 WHATWG Loader 提案，无法正确支持 ECMAScript 2022 引入的顶层 await，导致执行顺序错乱和初始化错误。
- 🔄 示例演示了动态导入同一模块三次时，旧实现出现 2、3、1 的错误完成顺序及访问未初始化导出的异常；新实现输出正确的 1、2、3。
- ⚙️ 旧加载器使用自托管 JavaScript 编写，虽能内联但启动慢、优化不稳定；重写后改为纯原生 C++，性能更稳定可靠。
- 🛠️ 重写始于 2026 年 1 月，删除旧代码后按 ECMAScript 规范将伪代码逐一翻译为 C++，先实现不依赖其他函数的叶子函数。
- 🧪 测试采用 Bun 团队提供的用例，并通过模糊测试生成复杂模块图，与其他引擎输出逐字节比对，确保正确性；同时通过 test262 和 WPT 相关测试。
- 📣 官方邀请开发者下载 Safari 27 测试版或 Technology Preview 体验，遇到问题可提交至 bugs.webkit.org。

---

### [](https://www.infoq.com/news/2026/09/jquery-20-years/)

**原文标题**: [Twenty Years of jQuery: How a Little Library Rewired Web Development - InfoQ](https://www.infoq.com/news/2026/09/jquery-20-years/)

jQuery 迎来 1.0 发布二十周年。它在 2006 年以极简的 `$()` 语法解决了浏览器兼容问题，大幅降低了前端开发门槛，并通过强大的社区影响了整个 JavaScript 生态。如今浏览器原生能力和现代框架虽已取代其核心地位，但 jQuery 仍广泛嵌在大量网站中，并由 OpenJS 基金会继续维护。

- 🎉 2006 年 8 月 26 日，jQuery 1.0 发布，John Resig 年初在 BarCampNYC 首次公开介绍，提出“编写 JavaScript 应该有趣”的口号
- ⚙️ 它用 `$()` 取代了冗长的 `document.getElementById`，通过 CSS 选择器、链式操作、动画和 Ajax 调用，解决了 IE6 等浏览器的不一致问题
- 🌍 jQuery 让设计师和后端开发者也能轻松上手前端开发，被称为“降低富 Web 应用构建门槛”的重要力量
- 👥 插件生态和活跃社区形成了统一而庞大的 JS 开发者群体，直接影响了后来各类框架的成长与传播
- 🏗️ 随着 React、Angular 等声明式框架兴起，以及 `querySelectorAll`、`fetch`、`classList` 等原生 API 普及，jQuery 逐渐被看作遗留代码，但并未完全消失
- 🛡️ 由于深度嵌入真实代码库，旧版 jQuery 漏洞至今仍是许多网站的安全隐患
- 📊 W3Techs 数据显示，全球仍有约 66% 的网站使用 jQuery，大量依赖 WordPress、Drupal、Bootstrap 和 Cypress 等生态延续
- ❤️ 也有开发者和团队持续撰文说明“为什么还在用 jQuery”，认为它帮助塑造了当今 Web 与开发者自身
- 🧑‍💼 jQuery 现由 OpenJS 基金会和贡献者社群维护，依然是开源友好的 MIT 许可项目

---

### [](https://bsky.app/profile/webdesignmuseum.org/post/3muu3c4wy222g)

**原文标题**: [@webdesignmuseum.org on Bluesky](https://bsky.app/profile/webdesignmuseum.org/post/3muu3c4wy222g)

overview summary  
这是关于微软在 1996 年将 JavaScript 引入 IE 3.0 并以 JScript 命名的历史事件，重点说明了改名背后的法律考量。

- 🗓️ 1996 年 9 月，微软在 Internet Explorer 3.0 中实现了 JavaScript，并将其命名为 JScript 1.0。
- ⚖️ 微软改用 JScript 名称，目的是避免与 Sun Microsystems 之间可能发生的专利诉讼。
- 🖥️ 该信息来源于 WebDesignMuseum 的帖子，记录了早期 Web 技术发展中的关键决策。

---

### [JScript - 维基百科](https://en.wikipedia.org/wiki/JScript)

**原文标题**: [JScript - Wikipedia](https://en.wikipedia.org/wiki/JScript)

overview summary
JScript 是微软开发的 ECMAScript 方言，曾用于 Internet Explorer 和 Windows 脚本宿主，属于专有软件，现已停止更新。它与 JavaScript 同名异源，但核心语言相同，支持条件编译等扩展。文章还介绍了多个版本分支，包括经典 COM 版、Managed JScript、Chakra 引擎和 JScript .NET，并提到相关安全问题和历史背景。

- 🧩 JScript 是微软的 ECMAScript 方言，用于 IE、HTML 应用及 Windows 脚本环境，属专有软件，最终版为 9.0（2011 年）。
- 📜 名称差异源于商标问题，与 JavaScript 实为同一语言核心，但 JScript 含条件编译等非标准扩展。
- 🛡️ 因安全漏洞曾被批评，微软在 IE 中增加了禁用 JScript 的选项。
- 🗂️ 经典 JScript（Active Scripting）版本从 1.0 到 5.8，对应不同 IE 和 Windows 版本，基于 ECMA-262 各版。
- 🧪 Managed JScript 基于 Dynamic Language Runtime，用于 Silverlight 和 ASP.NET，支持 CLR 环境。
- ⚡ Chakra（JsRT）引擎为 IE9+ 重构，分为旧版 Chakra 和 Edge 版 Chakra，另有兼容 COM 的“JScript 9 Legacy”。
- 🌐 JScript .NET 是 CLI 实现，功能偏向 .NET 应用，版本与 .NET Framework 同步，但与经典 JScript 产品线分离。
- 📚 微软文档曾将脚本参考转向 MDN，表明从 JScript 向 JavaScript 生态的过渡。

---

### [TeamPCP 的逮捕行动无法消除其所暴露的供应链风险](https://www.aikido.dev/blog/teampcp-arrested-supply-chain)

**原文标题**: [TeamPCP arrests don't fix the supply chain risk they exposed](https://www.aikido.dev/blog/teampcp-arrested-supply-chain)

overview summary
这篇文章是作者对 TeamPCP 组织被逮捕一事的个人回应。作者先澄清 TeamPCP 并非最初 Shai-Hulud 攻击的幕后黑手，但克隆了该蠕虫。文中表达了如释重负之感，提及自己曾受到该组织关注。作者分析了 TeamPCP 的混合动机与低门槛高破坏力的特点，强调制度与执法机构的重要性，同时指出攻击者与机构之间的时间差正被 LLM 拉大。最后作者认为类似团队会再次出现，但至少这个周末可以休息。

- 😮‍💨 作者对 TeamPCP 两名 20 多岁嫌犯在澳洲和美国执法机构联合行动中被捕感到极大宽慰。
- 🔍 明确区分：TeamPCP 与 2025 年夏天的原始 S1ngularity/Shai-Hulud 攻击无关，只是克隆了该蠕虫并广泛传播。
- ⚠️ 作者本人曾被 TeamPCP 点名，感到威胁而非荣幸，强调被犯罪组织注意是危险而非地位象征。
- 🎭 TeamPCP 难以归类：介于国家行为体、有组织网络犯罪和意识形态团体之间，混合了金钱、政治、破坏、自负和博眼球动机。
- 🛠️ 技术本身不算高深，但能快速利用公开漏洞和 LLM 工具将攻击规模化，危险在于“能力增强但克制缺失”。
- 🏛️ 技术防御只能遏制事件，无法实现问责；此次跨国逮捕凸显了健全执法机构的关键作用。
- ⏳ 攻击者可用数小时到数天发起新活动，而机构间的证据收集和司法协作需数月甚至数年，时间差正在扩大。
- 🤖 LLM 将进一步压缩攻击能力获取时间，而机构无法同等加速，如何在不牺牲正当程序的前提下缩小差距成为核心难题。
- 🔮 作者认为 TeamPCP 不会是最后一个：工具门槛降低、小团队能力飙升，类似威胁只会更多。
- 😌 虽然未来仍会有新的攻击与无眠之夜，但作者选择先庆祝当下——这个周末或许可以好好休息。

---

### [](https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared)

**原文标题**: [A Mini Shai-Hulud Has Appeared: Obfuscated Bun Runtime Payloads Hit SAP-Related npm Packages - StepSecurity](https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared)

StepSecurity 检测到一起针对 SAP 生态 npm 包的供应链攻击：攻击者在合法包中植入恶意 preinstall 钩子，下载 Bun 运行时并执行高度混淆的凭据窃取载荷。该蠕虫已确认感染 4 个核心 SAP 开发工具包，并通过窃取 npm token 自我传播，同时利用 IDE 自动化钩子实现持久化。

- 🔍 攻击发现：StepSecurity 通过 OSS AI Package Analyst 和 Harden-Runner 在恶意发布后数分钟内检测到该活动，并已通知 SAP 安全团队。
- 📦 受影响包：mbt@1.2.48、@cap-js/sqlite@2.2.2、@cap-js/postgres@2.2.2、@cap-js/db-service@2.10.1，均属 SAP 企业开发工具链。
- 🧬 攻击链：npm install 触发 `preinstall` → 运行 `setup.mjs` → 下载 Bun v1.3.13 → 执行 11.6 MB 混淆的 `execution.js`。
- 🕳️ EDR 规避：载荷刻意通过 Bun（而非 Node）运行，以绕过对 node 子进程的监控；执行后删除 Bun 二进制，不留下取证痕迹。
- 🔑 凭据窃取：并行收集 npm token、AWS/GCP/Azure Secrets、GitHub token、SSH 密钥、云配置及加密货币钱包等敏感文件，并打包外泄。
- 🧠 进程内存转储：在 GitHub Actions Linux runner 上通过 Python 读取 `/proc/{pid}/mem` 来提取 Runner.Worker 内存中的明文 secrets。
- 🇷🇺 CJIS 豁免：若系统区域设置为 `ru`，载荷会记录"Exiting as russian language detected!"并干净退出，指向俄罗斯/独联体背景。
- 🌐 外泄方式：在受害者 GitHub 账户创建公开仓库作为死信箱，仓库描述为“A Mini Shai-Hulud has Appeared”，名称采用 Dune 主题随机组合（如 sardaukar-sietch-247）。
- 🔐 加密保护：外泄数据先经 gzip，再用 AES-256-GCM 加密，AES 密钥以 RSA-4096（内嵌公钥）包装，即使截获也无法直接读取。
- 📁 持久化感染：向仓库注入 `.vscode/tasks.json`（`"runOn": "folderOpen"`）和 `.claude/settings.json`（SessionStart hook），使开发者打开 VSCode/Claude Code 时自动再次执行恶意代码。
- 🔄 蠕虫自传播：窃取的 npm token 经验证后，直接通过 HTTP API 构造 publish 请求，向所有可写 package 发布恶意版本；还会注入伪装成 Dependabot 的 GitHub workflow（分支 `dependabout/...`）窃取仓库 secrets。
- 🧩 混淆技术：payload 使用 obfuscator.io、自定义 base64 字母表、二次 `ctf-scramble-v2` 加密、eval 构造 require 等，静态分析难度极高。
- 🛡️ 检测与恢复建议：卸载受影响版本并降级到干净版（如 mbt@1.2.47），轮换所有凭据（npm token 尤其关键），删除 `.vscode/tasks.json` 和 `.claude/` 恶意文件，清理注入的 workflow 分支和 Dune 主题仓库，并固定精确版本。
- 📌 IOC 示例：`setup.mjs` SHA-256 `4066...5e34`，payload SHA-256 `80a3...0aac`，Bun 下载地址 `github.com/oven-sh/bun/releases/download/bun-v1.3.13/`，Dune 仓库名正则，以及 `claude@users.noreply.github.com` 提交者等。

---

### [](https://voidzero.dev/posts/whats-new-aug-2026)

**原文标题**: [Tales from the Void: August 2026 Recap | VoidZero](https://voidzero.dev/posts/whats-new-aug-2026)

overview summary
VoidZero 的 2026 年 8 月月度更新，重点介绍了 React Compiler 在 Vite 中的支持、各核心项目（Vite+、Vite、Vitest、Rolldown、Oxc）的进展、近期活动以及社区动态。

- ⚛️ React Compiler 现已通过 Oxc 集成到 Vite 8，构建时自动记忆组件和 Hooks，免去手写 `useMemo` / `useCallback`；相比 Babel 快 12–15 倍，比 React 官方 Rust 移植版快约 2 倍，并已用 10 万个源文件验证结果一致。
- 🚀 Oxlint 新增 22 条由 React Compiler 驱动的规则，可捕获违规并显示可执行的帮助信息；编译器打包在独立包中，非 React 用户不受影响。
- 🧰 Vite+ 更新：新增 `vp toolchain` 查看工具版本、`vp hooks` 管理 Git 钩子、支持从 `tsup` 迁移，以及 Codex CLI 与 Claude Code 沙箱运行。
- ⚡ Vite 发布关于减少小型公共 chunk 的 RFC，并修复 Bundled Dev Mode 的多项问题，欢迎反馈。
- 🧪 Vitest 5 进入 RC 阶段，功能趋于稳定；团队还 fork 了 IstanbulJS，发布现代化代码覆盖率引擎。
- 📦 Rolldown 支持属性混淆（property mangling）进一步缩减体积；按函数 `test`/`name` 分组的 chunk 生成速度提升约 3.4 倍；新增 Android armv7 目标支持。
- 🛠️ Oxc 发布了变量混淆工作原理的深度文章，并通过跨槽复用名称使混淆性能提升 3–4%。
- 📅 ViteConf 将于 10 月 15 日回归，可自选门票；VoidZero 成员还将在 ZurichJS、Cloudflare Connect、VueFes Japan 等活动中演讲。
- 🌐 社区亮点：Dillon Mulroy 发布 Oxlint 规则集 anti-slop；Tiptap 迁移到 Vite+；OpenAI Codex 模板改用 Oxc；另有 Ava 与 Vitest 快照对比工具、TSRX 官方 Oxc 集成及 Effect 诊断整合。

---

### [ViteConf 2026](https://viteconf.org/)

**原文标题**: [ViteConf 2026](https://viteconf.org/)

ViteConf 将于 2026 年 10 月 15 日迎来第五届，以“共同建设”为主题，强调 Vite 已成为全球默认构建工具（每周下载超 1.5 亿次），并汇聚众多生态贡献者展望未来。会议公布了丰富的演讲者阵容与往届精彩回顾，并提醒可添加日历提醒。

- 🌐 ViteConf 2026 将于 2026 年 10 月 15 日 10PM（UTC+8）举行，这是该社区会议的第五届。
- 📈 Vite 已成为 Web 默认构建工具，每周下载量超过 1.5 亿次，成就离不开无数开发者和合作伙伴的推动。
- 🤝 会议主题为“Building together. We are Vite.”，强调共建精神与生态协作。
- 🎤 演讲嘉宾包括 Evan You（Vue/VoidZero）、Ryan Carniato（Solid）、Matthew Phillips（Astro）、Alex Rickabaugh（Angular）、Daniel Roe（Nuxt）、Pooya Parsa（Nitro）等众多业界领袖。
- 🔧 议题覆盖 Vite、Vitest、Oxc、Module Federation、DevTools、Storybook、Astro、Nitp 等工具与框架生态的进展。
- 📺 提供往届精彩演讲回顾（2022–2025），如 Evan You 的“Beyond a build tool”和 Jim Dummett 的“JavaScript at the speed of Rust”。
- 🔔 页面支持通过 Google、Outlook 或 ICS 添加会议提醒，方便参与者准时加入。
- 🏢 会议由多家赞助伙伴支持，并有邮件订阅选项用于获取最新动态。

---

### [](https://deck.gl/docs/whats-new#deckgl-v94)

**原文标题**: [What's New | deck.gl](https://deck.gl/docs/whats-new#deckgl-v94)

该文章是 deck.gl 各版本更新日志的汇总，从 v9.4 到 v1 依次介绍了每个版本中的核心新特性，涵盖 WebGPU 支持、视图与控制器改进、新图层与扩展、多模块集成、性能优化、开发体验提升等多方面变化。

- 🚀 v9.4：作为 v9 系列终版，全面扩展 WebGPU 支持至所有官方图层，改善 Tile3DLayer 与 MVTLayer，并引入 GlobeView 交互增强与多画布基础
- 🧩 v9.4：新增 @deck.gl/maplibre 模块，支持 MapLibre v4–v6；多款图层增加解析抗锯齿、虚线/填充模式扩展，并优化拾取性能
- 🐍 v9.4：pydeck 支持图层扩展与特效，并新增在线 playground
- 🎛️ v9.3：重设计多款 Widget，新增 PopupWidget、ScrollbarWidget、SplitterWidget 等，并支持受控/非受控模式
- 🧭 v9.3：新增 TerrainController、pickable: '3d' 深度拾取、CSS 样式布局表达式，大幅增强 3D 导航能力
- 🗂️ v9.2：新增 14 个 Widget 组件，提供 React 封装；早期 WebGPU 预览支持部分图层渲染
- 🌐 v9.1：与 MapLibre 的 globe view 无缝整合，支持 React Widget 开发，并重构聚合图层新增 GPU 聚合方式
- 🦺 v9.0：采用 luma.gl v9 API 为 WebGPU 铺路，默认启用 TypeScript，新增 Controller 行为改进与首个 Widgets 模块
- ⚙️ v8.9：新增 CollisionFilterExtension、TerrainExtension 与 WMSLayer，并对构建工具链进行重大升级
- 📦 v8.8：提供公开预览的 TypeScript 类型，TileLayer 支持自定义索引系统，并新增 MapboxOverlay
- 🎭 v8.7：引入 MaskExtension 可实现地理围栏遮罩，新增 QuadkeyLayer，完善 CARTO 集成
- 🗺️ v8.6：Google Maps 矢量渲染层支持交错模式，OrthographicView 支持分轴缩放，并修正米制单位计算
- 🧵 v8.5：MVTLayer 解析提速 2–3 倍，GeoJsonLayer 支持 pointType 多样式点渲染，TextLayer 支持背景/边框/自动字符集
- 🔊 v8.4：强化移动端交互与控制器自定义，MVTLayer 支持 TileJSON 和二进制模式，渲染性能显著提升
- 🆕 v8.3：推出 @deck.gl/carto 模块，TileLayer 支持请求取消与更高精度控制，并整体优化内存使用
- 🧮 v8.2：大量改进瓦片图层体系，新增 GlobeView，支持跨 180° 经线绘制，并增强 pydeck 支持
- 🎯 v8.1：TileLayer 支持非地理视图，新增 MVTLayer 与 TerrainLayer，联合 ESRI 支持 ArcGIS 底图与 I3S
- ⚡ v8.0：重点优化性能（更新提速 1.5×，重绘提速 2.5×），增强二进制数据支持与 GPU 数据过滤能力
- 🧱 v7.3：引入 Tile3DLayer 以支持 3D Tiles，发布 pydeck Python 模块，完善过渡系统与资源管理
- 🔌 v7.2：新增 @deck.gl/extensions 模块，提供 Brushing 与 DataFilter 扩展，支持流式数据、阴影渲染与 HeatmapLayer
- 🎥 v7.1：支持屏幕后处理特效，GridLayer GPU 聚合增强，简单网络层支持 glTF 资源，并提供性能指标监控
- 📐 v7.0：重新组织图层模块，新增 glTF/loaders.gl 支持和新光照系统，引入二进制数据与尺寸单位等新 API
- 🔤 v6.4：TextLayer 支持 SDF 字体，ScatterplotLayer 支持描边填充，ContourLayer 新增等值线带
- 📏 v6.3：加入属性类型系统以提升更新性能，新增拖拽回调与 GPUAggregator 改进
- 🗂️ v6.2：借助 Mapbox Custom Layer API 实现图层交错渲染，默认启用 32 位高精度投影
- 🎯 v6.1：引入高精度地理投影实验模式、动态经线适配、JSON API 等
- 🎞️ v6.0：支持动画属性过渡与视图状态过渡，ScreenGridLayer 支持 GPU 聚合，并简化控制器用法
- 🖱️ v5.3：实现自动交互与数据加载、深层拾取以及透视/正交模式切换
- 📁 v5.2：支持非 React 使用方式并拆分多个 npm 子模块，新增 TextLayer 与测试工具
- 🧊 v5.1：为多个图层增加 GPU 过渡动画，并支持在 React 中用 JSX 创建图层
- 🖌️ v5.0：GPU 高亮、虚线路径、DevicePixelRatio 控制与图层过滤等特性加入
- 🖥️ v4.1：基于 luma.gl v4 获得 WebGL2 支持，新增查询方法、Shader 汇编和 Seer 集成
- 🔢 v4.0：新增 GeoJsonLayer、PathLayer 等核心图层，引入模型矩阵与图层属性能访问器机制
- 📈 v3.0：全面升级核心图层与访问器机制，新增 64 位高精度图层与 React 集成优化
- 🧩 v2：添加 3D 透视模式、属性自动管理并提升性能，新增 LineLayer
- 🎉 v1：deck.gl 初始开源版本，内含五个示例图层

---

### [Bun v1.4.1 | Bun 博客](https://bun.com/blog/bun-v1.4.1)

**原文标题**: [Bun v1.4.1 | Bun Blog](https://bun.com/blog/bun-v1.4.1)

Bun v1.4.1 版本发布，修复了 202 个问题，带来大量运行时、包管理、构建工具及生态兼容性改进，显著降低内存占用并提升启动与构建速度。

- 🚀 降低空闲内存占用：JavaScriptCore 在空闲期自动删除 JIT 代码，长时间运行的进程内存最多可降低数倍（如 Next.js SSR 从 222MB 降至 142MB）。
- 🌐 Bun.serve 新增 HTTP/2 支持：与 HTTP/1.1 共用端口和路由，通过 ALPN 协商；明文连接也可识别 HTTP/2 preface，但 WebSocket 与 trailers 暂不支持。
- 💾 Bun.write 支持流式写入：将 Response/Request/ReadableStream 直接写入文件，避免整块读入内存；128MiB 下载峰值 RSS 从 161MB 降至 13MB。
- ⏸️ WebSocket 新增 pause()/resume()：可暂停读取底层 TCP 以提供背压，并修复 bufferedAmount 恒为 0 的问题；ws 包同样适用。
- 🔐 node:crypto 实现 argon2 与 argon2Sync：支持 argon2d/i/id，输出与 Node 字节一致，且性能最高提升 9 倍。
- ⚡ Buffer 读写大幅加速：常用 read*/write* 方法被 JIT 内联，writeFloatLE 等提升 7–9 倍。
- 📊 AsyncLocalStorage.run() 提速约 2 倍：不再为每次 await/.then() 额外分配存储，嵌套 run() 提升明显，且修复 store 泄漏问题。
- 🖨️ Bun.inspect/console.log 对大对象从二次复杂度降为线性：1.6 万键对象打印从 140ms 降至 3.2ms；util.inspect 也提前截断超长数组。
- 📦 内置 Node 模块 require() 更快：node:fs、node:assert 等改为惰性加载内部模块，node:assert 从 6.22ms 降至 0.64ms。
- 🔑 首次 HTTPS 请求提速最多 3 倍：根证书以 DER 格式内嵌并按需解析，系统 CA 模式从 46.3ms 降至 15.3ms。
- 🔌 fetch() 复用 Unix socket 连接：循环 fetch 同一 socket 只建立 1 个连接；同时支持自定义 CA 并修复 chdir 后的相对路径错误。
- 🏠 localhost 与 *.localhost 全局解析到回环地址：不再查询系统解析器，修复 Docker IPv4 下连不上 localhost 的问题。
- 🛡️ fetch() TLS 验证改用 URL 主机名：不再受自定义 Host 头影响，避免不安全默认；如需对 IP 验证不同证书名可设 tls.servername。
- 🧩 服务器 WebSocket 支持 binaryType = "blob"：也兼容 ws 包，且 arraybuffer 模式现在发出 ArrayBuffer 而非 Uint8Array。
- 📄 --env-file 支持管道、FIFO 与 /dev/stdin：可从进程替换或 stdin 读取环境变量；默认 .env* 查找仍忽略非常规文件。
- 🚫 新增 --no-ffi-cc 禁用 bun:ffi 的 cc()：Worker 继承该标志且无法重开，防止不可信 JS 动态编译 C 代码。
- 🏷️ TypeScript 7.1+ 导入属性类型化：text/file/md/toml/yaml/sqlite/html 等均有正确类型，旧版 TS 仍按扩展名推断。
- 🧬 升级 JavaScriptCore：合入约 400 个 WebKit 提交，修复 JIT 错编译与深层解构崩溃，并更新 Promise.try 等到新规范。
- 📦 bun install 新增 workspace 独立 node_modules：通过 "selfContained" 配置为特定 workspace 保留传统布局（适配 Electron）。
- 📴 bun install --offline：完全离线安装（仅用缓存），可设为 bunfig 默认；缺失包会报错并提示名称。
- 🧾 bun install --prefer-offline：跳过元数据过期检查，直接用缓存；缓存缺失才下载。
- 📉 export * as 库打包体积大幅下降：zod 从 375KB 降至 77KB、fp-ts 降 85%、effect 降 56% 等；无用导出被彻底 tree-shake。
- ✂️ 动态 import() 可 tree-shake：仅保留被读取的具名导出；若命名空间被整体使用则保留全部。
- 🔗 --splitting 生成更少文件：入口与懒加载路由共享的代码并入入口 chunk，测试应用输出文件从 219 降到 151，启动模块从 70 到 2。
- 📏 新增 --min-chunk-size：将小型无副作用 chunk 并入较大入口 chunk，减少路由导航请求数；默认关闭。
- 🔮 浏览器构建自动添加 modulepreload：为每个脚本和懒加载 chunk 生成 <link rel="modulepreload">，并行预取依赖，减少往返。
- 🔄 更智能的 CommonJS 默认导入转换：可证明安全时将默认导入的属性读取转为顶层变量，React 示例输出从 8206 字节减到 1392 字节。
- 🧱 --splitting --target bun 下 require() 成为 chunk 边界：同步加载但分离 chunk，惰性 require 不再拖慢启动（启动 23.2ms→11.2ms）。
- ⚖️ 代码分割产物更小：chunk 间共享绑定使用全局统一命名，去除多余重命名；大型应用 minified 输出减少 19%。
- 🏷️ 嵌套类/函数保留名称：bun build 不再把 Model 重命名为 Model2，.name 与 unbundled/Rollup 一致。
- 🚀 bun build --compile 可执行文件启动更快：Claude Code 启动时间降低 20%（397ms→318ms）。
- 🧊 字节码体积缩小：序列化字节码从源码 9 倍降至 3 倍，Claude Code 安装体积从 376MB 降至 207MB；新增 --bytecode-depth 控制预编译深度。
- 🔄 支持 --compile --bytecode 交叉编译：跨平台生成字节相同可执行文件，消除平台差异。
- 📎 编译文件内文本导入更紧凑：3MB ASCII 文本导入只需增加 3MB 二进制和约 1MB 内存（原为 6MB/12.6MB）。
- 🧪 bun test --isolate 不再跨文件泄漏：mock/spyOn/plugin 不再保持模块图，80 个 mock 文件内存从 1591MB 降至 215MB，且 TZ/代理/TLS 设置不串扰。
- 🐛 大量 Node.js 兼容修复：涵盖 http/http2/net/tls/fs/crypto/dns/worker 等模块，修复 vite 端口自增挂起、testcontainers、better-sqlite3、grpc 互操作性等多个问题。
- 🛠️ Bun API 修复：修 server.upgrade() 泄漏、BodyStream 异常、Bun.file().slice 错发文件、WebView 崩溃、JIT/ffi 边界问题等。
- 🌍 Web API 修复：修复 fetch 超时回归、204/HEAD body 非空、TextDecoder 错误、WebSocket Host 头端口、crypto.subtle RSA-PSS 检查等。
- 💥 Runtime 修复：修复 import/require 混合语法错误、Worker 泄漏、structuredClone 竞态、字节码缓存偶发值错误、REPL 冻结与输出问题等。
- 📦 bun install 多项修复：无操作安装从 12.9s 降至 23ms、GitHub 依赖迁移、pnpm 迁移损坏 package.json、缓存竞争与大小写路径等问题。
- 🏃 bun run/init 修复：--filter 等忽略 bunfig、缓存失效、bun init 崩溃与 Ctrl-D 内部错误等。
- 🏗️ bun build 修复：修复插件 onResolve、barrel tree-shake、sideEffects、定义宏、JSX factory、minify 语法等大量边缘情况。
- 📦 bun build --compile 修复：修复 macOS 签名、UPX 不兼容、WSL2 EACCES、Worker 路径、4GiB 限制、字节码缓存非 ASCII 等问题。
- 🧹 其他修复：CSS 解析器支持新伪元素、bun test 覆盖率并行问题、Bun Shell 管道与变量处理、SQL/sqlite/S3 数值与流问题、TypeScript 类型定义、Windows 平台大量文件句柄与崩溃修复。
- 🙌 感谢 7 位贡献者：@alii、@dylan-conway、@jarred-sumner、@jvitormelo、@marshallofsound、@robobun、@sosukesuzuki。

---

### [](https://bun.com/blog/bun-v1.4.2)

**原文标题**: [Bun v1.4.2 | Bun Blog](https://bun.com/blog/bun-v1.4.2)

overview summary
- 🐛 修复了 `bun build` 中嵌套 `var` 与 `let` 变量名冲突的回归问题，解决了 Elysia 等构建的加载失败和潜在错误值计算。
- 🧠 修复了 `AsyncLocalStorage` 在 `store.exit()` 或嵌套 `store.run()` 内创建定时器/Promise 时导致的外部存储值内存泄漏。
- ⏱️ 修复了 `worker_threads` 中 `'online'` 事件未首先触发的问题，使 `@discordjs/ws` 不再因丢失首个消息而挂起。
- 🖼️ `Bun.Image` 现在支持解码 CMYK 和 YCCK 格式的 JPEG，并自动转换为 RGB，可进行后续变换和输出。
- ⚙️ 升级了 JavaScriptCore（约 350 个 WebKit 提交），修复了 `Intl` 和 TypedArray 正确性、`Proxy` 崩溃、`Date` 对象开销等问题。
- 🔧 修复了多个 Bug：如原型被 GC 后 JIT 优化代码的罕见崩溃、musl 上数组操作导致的 GC 崩溃/挂起、`.json()` 错误缺少具体 `SyntaxError` 信息、`bun install` 的哈希不匹配 panic、Linux 上 `FileSink` 描述符双重关闭问题。
- 🙏 感谢 3 位贡献者：@dylan-conway、@jarred-sumner、@robobun。

---

### [](https://docs.nvm-windows.com/features/newv2/)

**原文标题**: [What's new in v2 | nvm-windows Documentation](https://docs.nvm-windows.com/features/newv2/)

v2 版本在架构、安装流程、自动化、安全与企业支持方面进行了全面重写，引入操作模式和构建分发，提升了速度、灵活性与可管理性。

- 🚀 无需管理员权限，采用现代工作流，避免符号链接的权限问题
- 📌 支持多文件版本锁定（.nvmrc、.node-version、package.json 或自定义）
- ⚡ 下载与安装更快，体积缩小 40%，使用 .7z 压缩包并支持原生解压
- 🔄 自动安装缺失的 Node.js 版本，支持并行安装多个版本
- 💻 底层用 Go 和 Zig 重写，兼顾速度与可维护性
- 🏢 双构建模式：社区版（MIT 免费开源）与认证版（EULA，2026 年 9 月推出）
- 🔏 社区版不签名，认证版完整签名，署名“Author Software Inc”
- 🧩 引入操作模式：轻量 shim 与零延迟链接模式，适应不同场景
- 📂 按目录自动切换版本（读取 .nvmrc 等），支持缺失版本自动补装
- 📦 可选自动安装默认全局模块，支持用户定义别名
- 🗂️ Windows 原生集成：应用列表、事件查看器、通知中心、注册表偏好
- 🛡️ 安全与治理（附加组件）：版本防火墙、ADMX/GPO/Entra 策略控制、高级代理及自定义镜像支持
- 🔍 可观测性（附加组件）：提供 SBOM、来源证明、VEX 及结构化日志，适用于审计与 SIEM
- 🌐 支持离线/受限环境下的本地存档安装，并利用缓存复用已下载资源

---

### [Astro 7.3 | Astro](https://astro.build/blog/astro-730/)

**原文标题**: [Astro 7.3 | Astro](https://astro.build/blog/astro-730/)

Astro 7.3 正式发布，本次更新为 astro preview 添加 --ignore-lock 标志以支持多预览服务器并行，将运行时 logger 接入图像服务与缓存提供者，并为 @astrojs/cloudflare 新增 finalize() 辅助函数；文章还说明了升级方式并感谢社区贡献者。

- 🚀 Astro 7.3 版本发布，带来三项主要新特性及一系列小幅改进，完整变更日志可查阅官方文档。
- 🔓 `astro preview` 新增 `--ignore-lock` 标志，可绕过 lockfile 限制同时运行多个预览服务器，适用于 Playwright 测试等一次性快速启动场景。
- 📝 自定义图像服务与缓存提供者现在会接收到 Astro 的运行时 logger，其警告信息将遵循你的日志级别、输出目标及 `--silent` 配置，不再直接写入 console。
- ☁️ `@astrojs/cloudflare` 新增 `finalize()` 辅助函数，用于自定义 Worker 入口处理 `astro/fetch` 管道响应，自动应用 cookies 与 CDN 缓存默认值；Hono 中间件则无需额外调用。
- ⬆️ 现有项目可通过 `npx @astrojs/upgrade` 自动升级，或使用 npm/pnpm/yarn 手动安装 `astro@latest`。
- 👥 文章特别致谢 Astro 核心团队及众多社区贡献者，并邀请用户通过 Discord、GitHub、Bluesky、Twitter 等渠道反馈问题或分享建议。

---

### [](https://eslint.org/blog/2026/09/eslint-v10.10.0-released/)

**原文标题**: [ESLint v10.10.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/09/eslint-v10.10.0-released/)

ESLint v10.10.0 作为次要版本于 2026 年 9 月 4 日发布，主要新增功能并修复了多个规则和依赖相关的 bug，改进了若干边界情况的处理。

- 📅 发布于 2026 年 9 月 4 日，属于 minor 版本升级。
- ✨ 新增功能：`no-unexpected-multiline` 规则增加对带 `d` 和 `v` 标志的正则表达式字面量的检查。
- ✨ `new-cap` 规则新增对 `Object.prototype` 属性名的检查。
- ✨ `no-extra-bind` 规则修复了类字段和静态块中的漏报问题。
- 🔧 更新了 `new-cap`、`no-extra-bind`、`no-unreachable`、`prefer-object-has-own` 等规则，以避免边缘情况下的错误或意外行为。
- 🐛 多个错误修复：`prefer-object-has-own` 自动修复在 `Object` 被遮蔽时失效、`new-cap` 对 `UTC` 调用的误报、`no-unreachable` 忽略静态导入、支持 `/* exported */` 注释中的 `__proto__` 等。
- 🔧 依赖更新：`file-entry-cache` 升级到 v11，并改善了调试信息格式。
- 📝 文档更新：README、`no-control-regex` 的 `\c` 转义说明、兼容表链接及 `eqeqeq` 行为澄清。
- 🧹 维护与 CI 改进：更新 CodeQL action、跳过/恢复 EMFILE 测试、增强 Windows 上的生态测试兼容性。

---

### [](https://github.com/storybookjs/storybook/releases/tag/v10.6.0)

**原文标题**: [Release v10.6.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v10.6.0)

Storybook 10.6.0 正式发布，带来数百项修复与改进，核心亮点是面向 AI 代理工作流的全新技能（Skills）架构，并大幅增强 Angular-Vite、Vue 等框架的 MCP/技能支持，同时性能优化与包体积缩减显著。

- 💻 新增 `storybook skills` / `storybook tools` 命令，供代理工具与技能调用，并支持运行时派生与 JSON 输出
- 🅰️ Angular-Vite 加入实验性 MCP/技能支持，改进 docgen 分析、故事片段生成及组件输入输出文档
- 🟢 Vue 获得 MCP/技能支持，重构故事片段生成，并通过 vue-component-meta 提升 docgen 保真度，弃用 vue-docgen-api
- ⚡ 性能提升明显：工具 CLI 冷启动时间减半，整体包体积更小
- 🧩 修复 TanStack / NextJS-Vite 框架的多个问题，包括路由绑定、依赖优化与 Next.js 16.3 兼容
- 🔧 核心与构建层面改进：组件元数据管理状态机、docgen JSDoc 语义规范化、Windows 兼容性修复
- 🛠️ MCP 与开放服务工具集重构：共享 core toolsets、支持附加模式与自动生成项目本地子 host
- 📝 文档与搜索增强：支持标题级搜索、故事片段警告展示、组件描述与 API 说明
- 🐛 大量的框架级 bug 修复：Angular、Vue、NextJS、CLI、Core 等模块的迁移与边界问题
- 👥 由 @ghengeveld、@kasperpeulen 及另外 20 余位贡献者共同完成

---

### [](https://github.com/vuetifyjs/vuetify/releases/tag/v4.2.0)

**原文标题**: [Release v4.2.0 · vuetifyjs/vuetify · GitHub](https://github.com/vuetifyjs/vuetify/releases/tag/v4.2.0)

Vuetify 发布了 v4.2.0（代号 Crusader），将实验室中的 rules 组件提升为核心框架，同时为输入类、滑动类等组件带来大量新特性和 Bug 修复。团队还公开呼吁社区赞助，因为 OpenCollective 资金紧张。

- 💰 团队请求赞助：开源维护资金不足，希望使用者支持以继续更新版本。
- 🏅 实验室的 rules 组件正式被提升为核心框架组件。
- ⌨️ VAutocomplete/VCombobox/VSelect 等输入组件新增 open-on-focus、close-on-input-click、persistent-menu 及多选相关事件。
- 📝 VFileInput 新增 placeholder 支持；VCombobox 新增 trim-values；VDateInput 支持自动填充日期分隔符。
- 📏 VNavigationDrawer 支持百分比宽度；VBtnGroup 新增 size 属性，尺寸与独立按钮对齐。
- 📊 VProgress 系列新增值过渡的 duration 控制，VProgressLinear 新增 reveal 属性。
- 🧫 VSkeletonLoader 新增 chip-group 类型、types 属性，并重新支持 table-cell。
- 🎠 VSlideGroup 新增边缘事件、slide 函数以及 scroll-snap/scroll-distance 属性。
- 🔍 VTreeview 改进了搜索时的展开状态、ARIA 属性与键盘导航；VVirtualScroll 的 scrollTo 支持位置参数。
- 🛠️ 修复默认配置覆盖及父配置泄漏到菜单/对话框内容的问题。
- 🔧 VMenu 子菜单可访问性、VTextField 切换类型时保持光标、VRadio 独立 v-model 等多项 Bug 得到修复。
- 🧪 Labs 中 VHighlight 新增 ignore-accents 属性，可忽略重音符号进行匹配。

---

### [](https://www.youtube.com/watch?v=kHL3XzjpT5w)

**原文标题**: [The Story of VS Code | Official Documentary - YouTube](https://www.youtube.com/watch?v=kHL3XzjpT5w)

此為 YouTube 網站底部資訊與連結清單，涵蓋公司資訊、政策、合作選項與版權聲明。

- 📄 提供網站簡介、新聞中心、版權及聯絡我們等基本資訊連結  
- 👥 為創作者與廣告主提供相關服務入口，如創作者專區與刊登廣告  
- ⚙️ 列出開發人員資源、條款、私隱及政策與安全等法律文件  
- 🎥 說明 YouTube 的運作方式及測試新功能機制  
- ©️ 標示 © 2026 Google LLC 版權所有

---

### [](https://code.visualstudio.com/)

**原文标题**: [Visual Studio Code - The open source AI code editor | Your home for multi-agent development](https://code.visualstudio.com/)



---

### [](https://blog.gaborkoos.com/posts/2026-09-08-Half-Past-Fetch/)

**原文标题**: [Half Past Fetch](https://blog.gaborkoos.com/posts/2026-09-08-Half-Past-Fetch/)

`await fetch(url)` 只在响应头到达时结束，body 仍像流一样从网络中持续进入；文章由此展开连接复用、clone、取消、超时和流式处理等容易被忽略的后果。

- ⏱️ `await fetch(url)` 在响应头解析完成时即 resolve，body 仍在网络流式到达；通常需要第二次 `await response.json()` 或 `arrayBuffer()` 才能真正读完正文。
- 📦 服务端将 headers 和 body 一起发送时，这个间隙极其短暂；但只要 body 被故意延迟，就能看到 promise 提前数秒 resolve，而最后一个字节很久后才到达。
- 🔌 拿到 Response 后如果不读取 body 就离开，可能会浪费连接；是否复用取决于底层缓冲大小，Node 大约 16KB 就开始受影响，Chrome 可以容忍更多，不能当作可靠保证。
- ❌ 调用 `response.body.cancel()` 并不能让连接回到连接池；只有把 body 完整读完，连接才能真正被释放。
- 🍴 `clone()` 并不是生成独立副本，而是对仍在传输的流进行 tee 分叉；两个分支共享缓冲区，若某个分支无人读取，会保留整个响应大小的额外内存。
- ⚠️ 克隆后如果先 `await copy.body.cancel()` 再读原 body，会发生死锁：取消一个分支要等另一个分支读完才能结束。
- 🛑 Abort 在 fetch promise 已 resolve 后仍然有效：abort 不会让已有的 Response 消失，而是让下一次读取 body 的操作以 AbortError 拒绝；已经读到的数据仍然保留。
- 🕒 用 `Promise.race` 做超时只能覆盖 headers 到达前的阶段，无法中断慢速 body；`AbortSignal.timeout()` 传入 fetch 则能持续作用于整个 response body。
- 📊 正因 fetch resolve 后 body 还在到达，所以可以用 `pipeThrough(new TransformStream(...))` 实时观察进度或改写数据，再把流包成新的 Response。
- 📚 核心结论：`await fetch(url)` 只代表“请求头好了，正文即将开始”；后续连接、内存、取消和超时，都取决于你如何对待仍在流式到达的 body。

---

### [](https://wallabyjs.com/whatsnew/cli.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Test Runner CLI for Coding Agents](https://wallabyjs.com/whatsnew/cli.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

Wallaby CLI 将运行时测试智能引入 AI 编码代理工作流，支持在命令行直接运行测试并报告结果、覆盖率与运行时数据，无需编辑器会话或 MCP 服务器。它为多种主流代理和测试框架提供结构化反馈，显著减少 token 消耗、加快迭代，并帮助代理更有效地验证代码、调试失败与提升覆盖率。

- 🤖 为 Claude Code、Codex CLI、Copilot CLI、OpenCode、Pi 等 AI 编码代理提供命令行测试支持
- 📁 无需编辑器或 MCP 服务器，尤其适用于 git worktrees 和 headless 工作流
- 🧪 支持 Vitest、Jest 等框架，输出结构化运行数据：应测项、失败原因、代码覆盖率和运行时值
- ⚡ 大幅减少反复运行整套测试与解析原始输出的开销，降低 token 消耗并加速反馈
- 🛠 安装简便：运行 `npx skills add https://github.com/wallabyjs/skills --skill wallaby-cli` 即可启用
- 🔄 Wallaby 在需要时启动、代理退出后自动停止，并复用编辑器中已有的运行实例
- ✅ 代理能利用精确的测试与覆盖数据验证生成代码、提高测试质量和覆盖率，且无需改动源文件即可调试失败测试
- 🔮 未来将改进沙盒/CI 环境支持、连接既有编辑器扩展、优化 token 效率，并开放更多运行时数据

---

### [](https://evilmartians.com/chronicles/ten-anti-ai-slop-moves-for-frontend-projects-going-faster-than-humans-can-review)

**原文标题**: [10 anti-AI slop moves for frontend projects going faster than humans can review—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/ten-anti-ai-slop-moves-for-frontend-projects-going-faster-than-humans-can-review)

本文面向 TypeScript/React 与 AI agent 开发，提出 10 项对抗 AI 生成“看似可用实则难查”代码的工程措施。作者把检查分成三类：避免多余代码被写出、找出已被写出的问题、通过 CI 强制落地，并讨论了成本、渐进式推行顺序，以及自动化无法取代的人类判断。

- 🧾 **OpenAPI 契约先行**：前后端共用权威 API 规范，自动生成类型、客户端与 Zod schema；AI 猜错字段（如 `user.fullName`）会直接编译失败，审查重点回到小得多的契约本身。
- 🔒 **开启严格 TypeScript**：`strict: true` 并加上 `noUncheckedIndexedAccess`、`exactOptionalPropertyTypes`，强制处理“值可能不存在”的情况，减少 AI 代码里常见的乐观假设。
- 🧼 **把 linter 当作行为过滤器**：sonarjs 查复杂度/重复逻辑；`react-you-might-not-need-an-effect` 拦多余 effect；Vitest/Playwright 插件抓无断言测试和 `.only`；jsx-a11y 查无障碍；再禁用 `any`、非空断言等捷径。
- 🧱 **用依赖边界保护架构**：通过 eslint-plugin-boundaries 或 dependency-cruiser 声明组件/服务/工具/设计系统间的依赖方向，阻止 AI 每轮会话都“向 GitHub 平均架构漂移”。
- 🛠️ **把踩过的坑写成自定义 lint 规则**：AI 让自定义规则十分钟内可完成，规则应源于真实事故，例如“service 返回前禁止 `Math.round`/`toFixed`”，避免二次舍入 bug。
- 📏 **把规则前置到模型生成阶段**：把规则写进项目规则文件或 skill，让 agent 边写边看到指引；但这类预防只是概率性降低风险，不能替代事后检测。
- 🧬 **用变异测试检验测试是否真的有效**：Stryker 故意改动代码，找出没有任何测试会发现的变化；存活变异往往指向只执行不验证、快照未核实、断言 mock 而非代码的测试。
- 🪤 **用 Knip 与自定义脚本清除死代码**：Knip 找无人引用的文件/导出/依赖；自定义脚本可遍历入口图找不可达代码，或检查过期的 `vi.mock()`，把“不知道有多少问题”变成可度量的数量。
- 📑 **用 jscpd 抓重复代码**：AI 倾向新写一个实现而不是搜索已有实现；jscpd 按不同阈值检测文本重复，JSX 可宽松、业务逻辑应严格。
- 🚥 **让每项检查都在 CI 中成为门禁**：format/lint/tsc/unit/mutation/build 各自独立运行，分支不过就不能部署；唯一不可跳过的检查才真正有效。
- 💸 **注意成本并渐进式落地**：误报、过期规则、运行时间和新人理解成本都真实存在；应先以 warning 建立基线并只扫改动文件，再逐条提升为 error，最后才上 CI 门禁。
- 🧠 **自动化不能替代人的理解**：十项全绿只代表没有触发已知问题；功能对错、抽象时机、架构品味和产品判断仍需人工负责，这套机制是用来减少人工审查范围，而不是取消审查。

---

### [](https://kciter.so/posts/the-expensive-main-thread/en/)

**原文标题**: [The Browser's Main Thread Is Expensive | kciter.so](https://kciter.so/posts/the-expensive-main-thread/en/)

overview summary
本文围绕“浏览器主线程是昂贵资源”这一核心观点展开，说明主线程同时承担 JavaScript 执行与渲染管线，任何长任务都可能阻塞用户输入和屏幕绘制；真正的前端性能优化不只是让代码更快，而是从“省着用主线程”和“尽量不占用主线程”两个方向设计。

- 🧵 主线程同时负责 JS 执行、样式计算、布局、绘制与事件处理；长时间运行的任务会阻塞整个 UI，夸张场景下表现就是卡顿、掉帧、输入延迟。
- ⏱️ 60Hz 设备每帧约 16.6ms，实际可用预算约 10ms；超过 50ms 的任务被视为 long task，直接影响 INP、TBT 等性能指标。
- ✂️ 拆分任务：把长任务切成小块，用 setTimeout、requestAnimationFrame、scheduler.yield() 让出主线程，让输入和绘制有机会插入执行。
- 🧠 按时间预算拆分：动画进行中时可用 rAF 对齐帧周期，只占用每帧预算的一部分；但拆分过细会导致额外开销，JSON.parse 这类原子任务也无法拆分。
- 🗂️ 批处理高频工作：用 debounce、throttle、每帧只渲染一次、批量 DOM 写入等方式，减少重复布局、绘制和固定开销；React 的虚拟 DOM 也是这种思路。
- 🚦 任务优先级：通过 MessageChannel 自建任务队列，必要时把紧急任务插队到前面，实现“空闲时预处理、需要时快速响应”的 idle-until-urgent 模式。
- ⏳ 延迟非关键工作：代码拆分、IntersectionObserver 延迟离屏 Feed 内容的渲染、暂停不可见动画，让暂时不必要的工作不要抢占主线程。
- 🎬 把动画交给合成器：优先使用 transform 和 opacity，而不是 top/left/width 等触发布局的属性；FLIP 可以把真实布局变化伪装成合成器动画。
- ⚠️ 避免 layout thrashing：读布局属性后不要立即写样式，尽量把读操作和写操作分开；will-change 也不可滥用，否则会浪费大量图层内存。
- 👷 使用 Web Worker：把与 DOM 无关的重计算放到 Worker，如大文件解析、图片处理等；大块数据可用 transferable 对象转移所有权，避免 postMessage 复制成本。
- 🛑 直接消除工作：面对压倒性数据量时，选择丢弃过期消息、合并同类更新、用 memoization 跳过重复计算，或在源头上不做没必要做的事情。
- 💡 性能优化不是“我的代码是否太慢”就能回答的问题，而需要理解浏览器的线程模型，合理决定每项工作的大小、顺序、时机以及是否应该在主线程上执行。

---

### [](https://petewarden.com/2026/08/15/why-i-ported-moonshine-to-javascript/)

**原文标题**: [Why I ported Moonshine to Javascript « Pete Warden's blog](https://petewarden.com/2026/08/15/why-i-ported-moonshine-to-javascript/)

overview summary：作者解释了将 Moonshine 移植到 Javascript 的原因、开发过程中所涉及的工作、新版本的功能和示例，以及支持 Web 端的技术与市场考量，并邀请开发者提供反馈。

- 🧩 开发者频繁要求提供浏览器内运行的 Moonshine 版本，社区已有移植项目，但官方直到现在才发布完善版本。
- 🛠️ 移植工作远不止 C++ 核心编译成 WASM，还包括构建符合浏览器习惯的高级 API、完整测试体系、CI/部署集成和交互式示例。
- 📦 核心库增加了对内存模型和数据文件的支持，改进了此前仅部分方法支持内存缓冲的问题。
- 🌐 新版本已在 moonshine.ai 上线，包含从最小语音转文字示例到完整会议记录应用的各种演示，所有代码开源并附带内联示例。
- 🎤 使用 MicTranscriber 调用模型架构、设置文本回调、加载并启动即可在网页上运行语音转文本。
- 📈 支持 Javascript 的理由包括：开发者的明确需求、JS 在应用（Web 和服务端）中的主导地位、语音接口的增长前景。
- ⚡ 相比服务器方案，客户端推理更快速、成本更低，浏览器原生 API 却长期被忽视，本地语音智能是更合理的技术方向。
- 🖥️ 语音输入本质上应在客户端运行，因为当前硬件已足够支撑本地模型，无需将音频流传输至服务器再返回结果。
- 🔀 多语言/多平台切换成为常态，库的跨平台可用性（尤其 WASM）降低了开发者的框架采用风险，即使最终未必使用该选项。
- 💬 作者期待接收反馈，邀请开发者加入 Discord 社区，并希望了解用户用新版本构建出的应用。

---

### [](https://www.youtube.com/watch?v=OkuNJo9tTtg)

**原文标题**: [How can someone actually change JavaScript? - YouTube](https://www.youtube.com/watch?v=OkuNJo9tTtg)

YouTube 網站頁腳提供的各類導覽連結與版權資訊，涵蓋公司、法律、開發者、廣告與功能說明等區塊。

- 📰 新聞中心與版權、聯絡方式等公司資訊連結
- 🎨 提供創作者與廣告刊登相關的專區
- 👨‍💻 開發人員資源及 API 相關入口
- 📜 列明條款、私隱、政策及安全規範
- 🧪 說明 YouTube 運作方式與測試新功能機制
- ⚖️ 標示 © 2026 Google LLC 版權所有

---

### [Dropzone.js（拖放上传插件）](https://www.dropzone.dev/)

**原文标题**: [Dropzone.js](https://www.dropzone.dev/)

Dropzone.js 是一个免费、开源且广受欢迎的 JavaScript 拖拽上传库，旨在让文件上传既美观又易于使用，并支持高度定制。

- 📥 提供拖放文件上传功能，默认样式美观，也可深度自定义。
- 🆓 完全免费、开源，代码托管于 GitHub，并提供安装说明与问题反馈渠道。
- 📚 配置与定制文档可在 GitBook 上查阅。
- 🆘 用户可通过 GitHub Discussions 和 Stack Overflow（标签 #dropzonejs）获得社区支持。
- 🎵 作者还发布了新音乐视频「Don’t look back」作为额外消息。
- 🏗️ 自 2012 年起开发，兼容旧浏览器；即使没有 JavaScript 也有回退方案。
- 🚀 功能丰富：支持分块上传、错误处理、文件队列、多种安装方式、jQuery 插件及翻译等。
- ✔️ 经过良好测试，浏览器支持广泛，被数百万网站信赖使用。
- 🎨 默认设计即美观：包含图片预览、进度条、成功/错误图标，并支持主题定制。

---

### [发布 Rslib 1.0 - Rslib](https://rslib.rs/blog/v1-0)

**原文标题**: [Announcing Rslib 1.0 - Rslib](https://rslib.rs/blog/v1-0)

Rslib 1.0 是一个基于 Rsbuild 的 JavaScript 库构建工具，旨在用统一的流程帮助开发者构建工具库、UI 组件库、CLI 与 Agent 应用。1.0 版本在构建性能、声明文件生成、多框架支持、模块输出格式、生态集成以及 AI/Agent 工作流等方面都有显著提升，并进入稳定的 SemVer 公共 API 阶段。

- 🎉 正式发布 Rslib 1.0：支持从通用工具库、UI 组件库，到 CLI 与 Agent 应用的 JavaScript 库开发场景。
- 🔗 构建在 Rspack/webpack 生态之上：可复用 Rsbuild/Rspack/webpack 插件和配置，减少应用与库之间的重复维护。
- 🧩 支持多种输出：ESM/CJS、UMD/IIFE、Module Federation 远程模块，以及实验性的 Node.js SEA 可执行文件。
- ⚡ 性能提升明显：相比 0.7.0，未缓存构建时间缩短约 24.3%，缓存构建缩短约 56.7%，输出体积（Gzip 前）减少约 32.2%。
- 📄 声明生成更快：TypeScript 7 原生编译约快 2.4 倍，Isolated Declarations 约快 4.2 倍；后者需配合单独的类型检查流程。
- 🏗️ 支持 bundle 与 bundleless 模式，并可在同一项目同时产出，适配 SDK、CLI、组件库、monorepo 等不同交付方式。
- ⚛️ 开箱支持 React、Vue、Svelte、Solid 组件库，可通过插件启用 React Compiler，也支持在 bundleless 模式保留 JSX。
- 🎨 综合处理样式与静态资源：支持 CSS Modules、PostCSS、Sass/Less/Tailwind、图片/JSON/`new URL()`、Web Worker 与 Wasm。
- 🛠️ 使用方式灵活：无配置 CLI 可直接构建；配置文件支持共享顶层配置和多输出 `lib` 数组；JavaScript API 兼容 Node.js、Deno、Bun。
- 🧪 集成 Rstack 工作流：配合 Rstest 测试、Rspress 文档、Rsdoctor 分析，并可用 publint/arethetypeswrong 做 CI 发布前检查。
- 🤖 面向 AI Agent 友好：提供 Agent Skills、llms.txt 和 AGENTS.md，让编码 Agent 能更快理解和正确配置 Rslib 项目。
- 🚀 后续规划：继续优化 ESM/CJS 输出与声明生成效率，并加强库开发流程中测试、文档、质量检查和发布的集成体验。

---

### [](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-nl4-s)

**原文标题**: [Technology careers at Fidelity | Fidelity Careers](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-nl4-s)

overview summary：富达（Fidelity）为技术人才提供兼具创业氛围与大型企业资源的职业舞台，强调金融科技创新、跨团队协作与持续学习，并开放多种技术岗位与专项技能方向。

- 🚀 以创业心态结合财富 500 强企业基础，助力重塑未来金融科技  
- 👥 拥有庞大的技术团队，且 2023 年许多员工在内部承担新职责或扩展角色  
- 🤝 团队互动氛围浓厚，全栈工程师 Monica 认为“最好的部分就是人与人之间的交流”  
- 📍 近期开放岗位集中在 Durham, NC 与 Westlake, TX，包括系统分析高级经理、高级系统工程师、大型机 DB2 性能与容量总监等  
- 🧰 重点招募技能涵盖软件工程、全栈工程、云工程、数据可视化、人工智能/机器学习、架构、系统工程与系统分析  
- 🎓 每周为技术人员安排专门学习时间，支持在线课程、职业辅导、导师跟岗等成长方式  
- 🔗 官方还提供技术职业详细介绍与加密（Crypto）职业方向，便于求职者探索更多机会

---

### [虚拟 GPU](https://vgpu.sh/)

**原文标题**: [vgpu](https://vgpu.sh/)

vgpu 是一个面向 WebGPU 的着色器工具库，主打“一个 shader，处处渲染”。它让同一份 WGSL 既能在浏览器中交互显示，也能在 Node.js 无头环境里渲染成图片、视频或 CI 测试产物，并提供 WGSL 模块化、构建压缩和 CLI 支持。

- 🧩 跨端统一：同一 shader 可用于浏览器 canvas 和无头 Node.js，支持交互、任意分辨率、mp4 视频以及 CI 快照测试。
- 🚀 极简 API：通过 `effect()` 创建 shader，`draw()` 绘制到目标，再用 `frame()` 驱动渲染循环，简洁直观。
- 📦 WGSL 工程化：像 import TypeScript 一样导入/导出 WGSL；自动解析模块依赖、反射绑定、移除未使用声明并压缩为紧凑源码。
- 🛠️ CLI 辅助：`npx vgpu` 提供 docs、examples、check（WGSL 校验）和 doctor（运行时修复），便于嵌入 agent 工作流。
- 🎥 丰富示例：包含 Transmission（玻璃折射）、Black Hole（黑洞引力透镜）、FFT 海面仿真、Radiance Cascades 光照等高质量 WebGPU 演示。
- 📚 文档与集成：提供 Getting Started、核心概念、API 参考和只读源码示例，并开放 OpenAPI 3.1 描述给自动化工具使用。

---

### [](https://github.com/MasterKale/SimpleWebAuthn/releases/tag/v14.0.0)

**原文标题**: [Release v14.0.0 - The one after they go quantum · MasterKale/SimpleWebAuthn · GitHub](https://github.com/MasterKale/SimpleWebAuthn/releases/tag/v14.0.0)

SimpleWebAuthn v14.0.0 发布，重点为服务端加入 PQC 抗量子签名算法支持、浏览器端新增多个辅助方法，并提高了最低运行时版本要求。

- 🚀 服务端支持 ML-DSA-44、ML-DSA-65、ML-DSA-87 抗量子算法；在兼容环境中注册 passkey 时自动优先推荐 ML-DSA-44
- 🌐 浏览器端新增 `sendSignal()` 方法，统一调用 WebAuthn Signal API
- 🧭 新增 `browserSupportsPasskeys()`，更可靠地检测 WebAuthn/passkey 支持
- 🔎 新增 `getBrowserCapabilities()`，封装 WebAuthn 的 `getClientCapabilities()` 并加入额外特性检测
- 🔀 `verifyAuthenticationResponse()` 新增可选参数 `expectedTopOrigin`，支持跨源认证验证
- 📋 `MetadataService.initialize()` 新增可选 `logger` 参数，方便项目自定义记录状态输出
- 🔧 注册与认证方法中的 `transports` 类型更新为 `string[]`，调用更简单
- 🛠️“tpm”证明验证对 TPM 制造商 ID 的大小写容忍度更高
- ⚖️ `generateRegistrationOptions()` 与 `verifyRegistrationResponse()` 现使用同一套默认支持的算法列表
- 📜 `validateCertificatePath()` 支持含交叉签名证书的 x5c 数组
- ⚠️ 破坏性变更：最低运行时版本提升至 Node LTS 22.x+ 与 Deno v2.4.x+
- 👏 感谢贡献者 @agektmr 的帮助与支持

---

### [](https://github.com/eslint/config-inspector)

**原文标题**: [GitHub - eslint/config-inspector: A visual tool for inspecting and understanding your ESLint flat configs. · GitHub](https://github.com/eslint/config-inspector)

这是一个用于检查和理解 ESLint flat configs 的可视化工具，提供本地运行、静态构建和在线预览功能，并支持开发定制与贡献。

- 🔍 可视化工具：帮助开发者直观查看和理解 ESLint flat configs 配置。
- 🚀 快速使用：在项目根目录执行 `pnpx @eslint/config-inspector`，访问 `http://localhost:7777` 即可查看，配置变更会自动更新。
- 🌐 在线预览：无需安装即可直接在浏览器中体验工具功能。
- 📦 静态构建：通过 `pnpx @eslint/config-inspector build` 生成单页应用，可用于部署或配置对比。
- 🤝 贡献指南：项目遵循 ESLint Contributor Guidelines，可通过 issues 参与贡献。
- 🛠️ 技术栈：采用 pnpm、Nuxt & Vue、devframe、UnoCSS（启用 attributify）及 ESLint。
- 👨‍💻 开发流程：使用 `pnpm install` 安装依赖，`pnpm cli:dev` 启动检查和开发服务器，`pnpm dev` 提供 HMR 迭代，`pnpm build` 与 `pnpm start` 用于生产构建和启动。
- 📄 开源许可：项目基于 Apache-2.0 许可证发布。
- 💰 赞助支持：由 ESLint 及多家赞助商支持，可通过赞助展示品牌信息。

---

### [](https://gpuix.dev/)

**原文标题**: [React bindings for GPUI, Zed's GPU-accelerated UI framework — GPUIX](https://gpuix.dev/)

GPUIX 是 Zed 的 GPU 加速 UI 框架 GPUI 的 React 绑定，让开发者用 React 和 TypeScript 构建原生桌面应用：组件直接渲染到 GPU（Metal/DirectX/Vulkan/WebGPU），不依赖 Electron 或 WebView，同时保留热重载、自动化测试和现代前端开发体验。

- ⚛️ 用 React/TypeScript 直接编写 GPU 渲染的原生界面；React 协调器只发送“变更批次”给 Rust，Rust 持有整棵 retained tree，再用 GPUI 的即时模式在每帧重建元素。
- 🚀 快速上手：`bunx @gpuix/cli new my-app` 会下载官方 `example-app/`，随后 `cd my-app && bun run dev` 即可打开窗口。
- 🔧 从零接入时，必须在 `tsconfig` 设置 `"jsxImportSource": "@gpuix/react"`，否则 `<virtual-list>`、`<markdown>`、`hover` 等 JSX 类型无法通过 TypeScript 检查。
- 📄 入口文件必须以 `render(<App />)` 结尾；它负责创建窗口、挂载 React 并启动帧循环。
- 🔁 开发时使用 `bun --hot` 而非普通 `bun`，保存文件会在同一窗口重新挂载 React；发布用 `bun build --compile` 得到免运行时的单个原生二进制。
- 📦 包结构：`@gpuix/react`（reconciler 与类型）、`@gpuix/native`（napi 桌面 / wasm 浏览器原生渲染器）、`@gpuix/cli`（脚手架与命令）。
- 🎨 样式“像 CSS 但不是 CSS”：`div` 默认不是 flex，需手动 `display:"flex"`；`padding`/`margin` 只接受数值；颜色不会自动继承，`<text>` 必须显式设定 `color`，否则深色背景上会不可见。
- 📜 原生滚动容器与 `<virtual-list>` 面向长列表：虚拟列表只构建/布局/绘制可见行，并支持 `alignment`、`followTail`、`itemCount` + `windowStart` 窗口化方案。
- 🖊️ 原生输入体验：`<input>` 与 `<textarea>` 支持 IME、剪贴板、撤销/重做；焦点系统、键盘事件、`tabIndex` 与自动 FocusHandle 均已内置。
- 🧩 原生文本组件：`<code>`、`<diff>`、`<markdown>` 在 Rust 侧用 Syntect 处理高亮；渲染出的文本可跨元素选择、复制，也支持高亮与搜索（`highlight` / `useTextSearch`）。
- 🎬 `motion.div` 提供原生补间动画（宽高、透明度、圆角等），中间帧由 Rust 计算，不会触发 React 渲染或 N-API 调用。
- 🧰 无头基础组件：从 `@gpuix/react/select`、`/combobox`、`/tooltip` 命名空间导入后，可自行构建 shadcn 风格的 Select、ComboBox 与 Tooltip。
- 🪟 窗口与桌面能力：透明或 macOS 毛玻璃标题栏、标准应用菜单快捷键、后台启动（`focus:false`/`show:false`）、`activateWindow()`，并支持 macOS 菜单栏行为。
- 🌐 浏览器版本：同一套 React 应用可编译为 Wasm/WebGPU 运行，且支持 React Fast Refresh。
- 🧪 自动化与测试：`createTestRoot()` 提供 GPU 后端测试环境，支持 `getByTestId` locator、点击/输入/拖拽、虚拟时钟与截图；`launch()` 可驱动子进程应用而不抢占用户焦点。
- 🖼️ 示例生态完整：`todo`、`chat`、`mail`、`timeline`、`diff`、`native-text`、`counter` 等分别演示虚拟列表、动画、Markdown、时间线拖拽等核心场景。

---

### [](https://zed.dev/)

**原文标题**: [Zed — Your last next editor](https://zed.dev/)

Zed 是一款由 Rust 从零打造、以速度和协作为核心的代码编辑器，并推出 Delta 作为支持智能体的多人编码环境。Zed 整合了并行智能体、原生 Git、调试器、远程开发等能力，同时提供丰富的扩展生态与灵活 AI 模型接入，获得众多知名开发者的高度评价。

- 🚀 Zed 定位：极致轻量的多人协作代码编辑器，支持 macOS、Linux 与 Windows；底层由 Rust 编写，充分利用多核 CPU 和 GPU 加速体验。
- 🤖 Delta 介绍：Zed 团队推出的“多人智能体编码环境”，让开发者和多个 AI agent 能在同一项目中并行工作、共同编码。
- ⚡ 核心性能与协作：支持多个 agent 并行编辑文件、快速导航代码和运行工具；内建团队聊天、屏幕共享与项目共享功能。
- 🧠 AI 能力不锁单一模型：提供 Agentic Editing、内联助手、编辑预测（基于 Zeta2 开源模型），并可通过 ACP/MCP 接入 Claude Agent、Codex、OpenCode 等任意智能体。
- 🔧 工程内建功能：包含基于 DAP 的调试器、原生 Git 支持、LSP、多缓冲编辑、Vim/Helix 模式、开发容器与远程开发等硬核特性。
- 🧩 扩展生态丰富：已有 HTML、Java、PHP、SQL、TOML、主题等数百款高下载扩展，可拓展语言支持与个性化界面。
- 💬 开发者证言：José Valim、Dan Abramov、Mike Bostock 等知名工程师称赞其响应速度、AI 工作流与细节设计的出色表现。
- 📅 近期动态与博客：发布“Introducing Delta”、沙箱机制说明、以及 Zed Decoded 等系列文章，持续更新技术进展。

---

### [memlab](https://facebook.github.io/memlab/)

**原文标题**: [memlab](https://facebook.github.io/memlab/)

memlab 是一个用于检测和调试内存泄漏的工具，支持浏览器、Node.js 和 CI 环境，提供自动化泄漏检测、堆分析、可视化调试及 AI 集成等功能，工作原理是通过定义场景、运行测试并追踪引用链来定位泄漏。

- 🔍 浏览器泄漏检测：通过 Puppeteer 驱动应用，自动对比堆快照并聚类真正的泄漏对象。
- 🧩 堆遍历 API：提供面向对象的快照访问接口，支持 Chromium、Node.js 等，可构建自定义泄漏检测器。
- 🛠️ 内存 CLI 工具箱：内置重复字符串、超大对象和无限增长等分析，帮助发现优化机会。
- 🖥️ MemLens 调试：在浏览器页面内直接可视化并交互式调试泄漏，无需离开测试页面。
- ✅ Node.js 断言：单元测试可捕获自身堆快照并断言对象已释放，在 CI 中提前发现回归。
- 🤖 MCP 服务器集成：可将堆快照交给 Claude Code 或 Cursor 等 AI 代理，用自然语言调查内存问题。
- 📝 三步工作流程：编写测试场景（如点击操作）、运行 memlab CLI、通过引用链报告泄漏位置。
- 🔗 引用链追踪：从 GC 根节点到泄漏对象完整展示引用关系，聚合相似泄漏，减少修复数量。
- ⚡ 快速上手：使用 `npm install -g memlab` 安装即可开始泄漏检测。

---

### [星韵 LilyPond](https://lilypond.ky.fyi/)

**原文标题**: [Astro LilyPond](https://lilypond.ky.fyi/)

这是一个将 LilyPond 音乐记谱语法集成到 Astro 网站框架中的工具，让文本轻松转换为乐谱图像。

- 🎼 在 Markdown 中直接编写 LilyPond 代码，即可自动渲染为乐谱，也支持通过 Astro 组件使用。
- 📁 支持将文本输出为 .svg、.png 和 .pdf 格式，并兼容 remark 和 satteri 等 Markdown 处理器。
- ⚡ 构建时生成图像，无需客户端 JavaScript，非常适合静态网站，保持页面快速加载。
- ♿ 可根据乐谱标题和作曲家自动生成替代文本，也可手动提供说明，提升无障碍访问性。
- 📚 内置内容加载器，可读取整个文件夹中的 .ly 文件，并将其作为 Astro 内容集合使用。
- 🎶 支持全部 LilyPond 语法，并提供丰富的示例展示其功能与应用可能性。
- 🚀 快速上手只需运行 `npx astro add astro-lilypond`，即可完成安装与配置。

---

### [](https://vue-echarts.dev/)

**原文标题**: [Vue ECharts: Vue.js component for Apache ECharts™.](https://vue-echarts.dev/)

您尚未提供需要总结的文本内容。请发送文章或段落，我会按照指定模板为您生成摘要。

---

### [](https://fingerprint.com/webinar/workshop-new-account-fraud/?utm_source=JSWeekly09082026)

**原文标题**: [Live Build: The Device Intelligence Method to Stop New Account Fraud](https://fingerprint.com/webinar/workshop-new-account-fraud/?utm_source=JSWeekly09082026)

本次线上工作坊由 Fingerprint 的 Keshia Rose 主讲，聚焦如何用设备智能识别并阻止新账户注册欺诈，形式为实时编码实操，而非单纯演示。

- 📅 活動時間：9 月 16 日 上午 9 點 PT / 中午 12 點 ET，為一場 Live Build 實作工作坊
- 🎯 核心問題：如何區分真實新用戶與惡意註冊者，避免假帳號濫用試用額度、推薦獎勵與促銷優惠
- 🚫 傳統防護不足：email/電話驗證、IP 限流容易被繞過，且會懲罰正常用戶
- 🛡️ 解決方案：設備智能在註冊當下識別設備、檢查風險訊號，並封鎖同一設備的重複註冊
- ⚙️ 實作內容：在註冊頁加入 JavaScript agent，並在伺服器端取得已驗證的訪客資料
- 🤖 帳號建立前先檢查 bot 偵測與 Suspect Score，提前攔截可疑行為
- 👤 透過 visitor ID 實作「一設備一帳號」規則，封鎖無痕視窗與 VPN 後的再次註冊
- 🖥️ 工作坊形式：引導式開發，需開啟編輯器、複製 starter repo，與講者一起寫程式
- 💬 最後 15 分鐘提供實作指導與 Q&A，歡迎帶自身的註冊流程與問題
- 🎤 講者 Keshia Rose：Fingerprint 資深開發者倡導者，擅長將複雜的防詐騙概念轉化為實用解決方案

---

### [](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

Meticulous 是一款面向现代 Web 应用的自动化端到端测试工具。它通过录制真实用户交互并结合 AI 引擎自动生成、持续演化测试套件，帮助工程团队在不手动编写或维护任何测试的情况下，快速发现回归缺陷。该工具尤其擅长处理复杂代码库，以零干扰、零 flakes 和高并行性能获得 Dropbox、Notion 等组织的信任。

- 🧠 智能录制与生成：在本地、staging 和 preview 环境添加脚本记录用户会话，AI 引擎随后分析代码分支，自动生成覆盖所有用户流程和边界情况的视觉端到端测试
- ✨ 零开发者维护：测试套件会随应用功能演进自动新增和移除用例，开发者无需再手动修复、更新或清理测试
- 🎯 确定性无 flakes：从 Chromium 底层构建确定性调度引擎，能从根本杜绝测试随机失败，并提供闪电般执行速度
- ⚡ 超高速并行测试：数千屏测试可在 120 秒内并行完成，大幅缩短反馈周期
- 🔌 后端自动 Mock：录制响应自动保存并重放，测试无需配置专属账号、造数，也不会因动态数据产生误报
- 🧩 无缝集成灵活性：可作为现有测试套件的补充，也可完全替代，并支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流框架
- 🔒 安全与部署简单：只需几行安装代码即可接入 CI，产品同时强调安全与隐私保障，并被超过 100 家组织采用

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Data 是 Timescale 旗下面向 Postgres 时间序列工作负载的云服务，强调超大规模数据处理、弹性伸缩与成本优化，同时具备企业级安全合规、高可用、可观测性和快捷部署能力，并提供免费试用额度与广泛生态集成。

- 📈 真实规模：单个 Tiger Cloud 服务每日处理 3 万亿指标、3 PB 数据与 1 千万亿数据点
- 💰 免费试用：新账户可获 $1000 额度，30 天内有效，无需信用卡
- 🤝 客户信任：被数千家 IoT 领域的公司广泛采用
- 🚀 弹性扩展：支持最多 10 节点副本集、读写分离，并通过 SSD/S3 分层存储实现低成本“无底”存储
- 💸 成本优化：计算与存储分离，可独立扩缩容，避免为空闲容量付费
- 🔁 高可用保障：多可用区集群、自动故障转移、时间点恢复与跨区域备份
- 🛡️ 企业级安全：符合 SOC 2、HIPAA、GDPR，支持始终加密、SSO、RBAC 与审计日志
- 📊 深度可观测性：查询钻取与仪表盘可查看性能和错误，并支持将指标发送至 CloudWatch、Datadog、Prometheus
- ⚡ 快速启动：几分钟内即可创建数据库，并可通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 生态集成：可与主流云提供商及更大范围的 Postgres 生态工具无缝对接
- 🏅 企业级默认：提供合同化正常运行时间 SLA、区域数据隔离与合规认证
- 🕧 全天候支持：全球 Postgres 专家提供 24/7 支持，保障企业级响应时间

---

### [](https://github.blog/changelog/2026-09-04-new-api-endpoint-provides-privacy-safe-star-history-data/)

**原文标题**: [New API endpoint provides privacy-safe star history data - GitHub Changelog](https://github.blog/changelog/2026-09-04-new-api-endpoint-provides-privacy-safe-star-history-data/)

2026 年 9 月 4 日，GitHub 宣布推出新的 REST API 端点，用于获取仓库 star 历史数据，同时兼顾用户隐私。该端点允许管理员和协作者以外的开发者通过带时间戳的计数追踪 star 增长趋势，而无需查看具体 stargazer 的身份信息。

- 🆕 新增隐私安全的 star 历史 REST API 端点，可随时追踪仓库 star 增长趋势
- 🔒 不会暴露 stargazer 个人身份信息，仅提供历史计数及对应时间戳
- ⚙️ 此前 stargazer 列表端点仅限管理员和协作者使用，此端点作为合规替代方案
- 🔄 适用于更新和迁移此前依赖旧追踪方式的工具与集成
- 📅 相关公告发布于 2026 年 9 月 4 日，并提供文档与社区讨论链接供反馈

---

### [GitHub Star 历史 — 跟踪与比较开源项目 Star 增长](https://www.star-history.com/)

**原文标题**: [GitHub Star History — Track & Compare Open Source Star Growth](https://www.star-history.com/)

overview summary
- 这份内容来自 GitHub Star History 网站，展示了 2026 年 9 月 1 日至 7 日期间新增星标最多的 GitHub 仓库排行榜，并介绍了网站提供的各类功能工具。

- 📈 榜单首位是 `tt-a1i/archify`，周增星标约 13.8k；紧随其后的是 `mattpocock/skills`（+13.4k）和 `DietrichGebert/ponytail`（+12.7k）。
- 🔥 榜单中还包括 `deepseek-harness`、`ECC`、`VoiceStudio`、`humanizer`、`orca` 等热门项目，增星数从 3k 到 8k 不等。
- 🧭 网站提供“Star Map”和“Star Compare”功能，方便用户查看和对比任意 GitHub 仓库的星标历史。
- 👥 另设有“Top Committers”排行榜，支持按每周或全时间范围查看，并可随机浏览仓库。
- 🔍 页面支持输入 GitHub 仓库名直接查询其星标趋势，并支持“Clear all”清空记录。
- 📅 数据更新周期清晰标注为每周一次，并支持订阅更新，同时提供 Chrome 扩展。
- 🏆 该网站被视为“The de facto GitHub star history graph”，由 Bytebase 维护，最初由 @tim_qian 构建。

---

### [](https://www.star-history.com/blog/new-github-star-history-api/)

**原文标题**: [The New GitHub Star History API](https://www.star-history.com/blog/new-github-star-history-api/)

概述：GitHub 因隐私问题收紧了旧的 stargazer 接口访问权限，导致 Star History 等第三方图表工具无法正常获取非本人仓库的星标数据。在与 GitHub 团队沟通后，官方推出了新的专用 API，按周聚合星标数量而不暴露用户信息，解决了隐私与 40,000 星上限问题，使所有公共仓库的星标历史图表恢复正常，且大型仓库的曲线更加完整准确。

- 🔒 旧 stargazer 接口会公开每个星标用户的用户名、头像和主页，容易被爬取用于发送垃圾邮件，存在隐私隐患。
- 📉 旧接口每页返回 100 条，最多只能看到前 400 页（40,000 星），超过此规模的仓库无法获取完整曲线，图表尾部只能靠估算。
- 🚫 GitHub 于 6 月 30 日宣布限制 stargazers 端点及页面仅限仓库管理员和协作者访问，导致 Star History 无法为非维护者绘制图表。
- 🤝 Star History 作者与 GitHub 团队沟通，说明需求仅是“随时间变化的星标数量，不涉及用户数据”，官方随即着手构建专用端点。
- 🆕 新端点 `GET /repos/{owner}/{repo}/stargazers/history` 按日历周分组返回星标增量，含周起始时间戳、周总数和每日细化数组，空周补零。
- 📦 新接口分页每页最多 30 周，最多 100 页，足以覆盖约 57 年的数据，任何 GitHub 仓库都能完整回溯到创建周。
- 🔢 另有配套端点 `GET /repos/{owner}/{repo}/stargazers/count` 可直接返回当前星标总数。
- ✨ 新方案让任何公共仓库都不再受维护权限限制，同时彻底消除 40,000 星上限，大型仓库的曲线现在能真实画到最新。
- ⏱️ 数据成本取决于仓库年龄而非星标数，因此 30 万星的仓库与 300 星的仓库请求量相同，效率大幅提升。
- 💡 作者希望未来每个周条目能附带累计总数，这样无需拉取全部页面即可绘制局部曲线，可进一步节省请求资源。
- 📊 Star History 已立即采用新 API，之前两个月内损坏的图表现已恢复，且大型仓库图表比以往任何时候都更精准。

---

### [](https://www.star-history.com/?repos=solidjs%2Fsolid&type=date&legend=top-left)

**原文标题**: [GitHub Star History — Track & Compare Open Source Star Growth](https://www.star-history.com/?repos=solidjs%2Fsolid&type=date&legend=top-left)

该页面展示了 GitHub 趋势项目榜单，按周（2026 年 9 月 1 日至 7 日）统计 star 增长情况，并提供星标历史查询与比较工具。

- 📈 本周增长冠军为 archify，新增约 13.8k stars
- 🛠️ 排名第二的 skills（mattpocock）新增约 13.4k stars
- ✨ 第三名 ponytail 新增约 12.7k stars
- 🤖 deepseek-harness 以 8.8k 增量位列第四
- 📊 榜单涵盖 AI、设计、公共 API 等多元领域
- 🔍 站点支持输入仓库名查看星标历史
- ⚖️ 提供 Star Map 与 Star Compare 等对比工具
- 🏆 另有 Top Committers、周榜/总榜及随机浏览功能

---

### [](https://www.robinwieruch.de/agentic-coding-bet-on-primitives/)

**原文标题**: [Agentic Coding: Bet on the Primitives - Robin Wieruch](https://www.robinwieruch.de/agentic-coding-bet-on-primitives/)

这篇文章通过一次真实图表项目实验，论述了 agentic coding（智能体编程）正在改变开发者对“高层库 vs 底层原语”的选择逻辑。作者认为，抽象本质是预先支付的实现劳动，而 AI 让实现成本骤降后，团队更值得押注无观点的原语（如 d3-scale、date-fns、zod）与薄自有层；但高层库在特定场景下仍然合理。

- 🧪 作者用 D3 数学原语 + React 与 Recharts 分别实现同一套定制图表，结果原语版完美匹配设计系统，Recharts 版前 80% 更快，最后 20% 仍要手写 SVG，还遇到动画冻结等 workaround 问题。
- 💡 抽象是“编码化、预付的实现劳动”：安装库省下的是编写时间，付出的是灵活性；一旦需求偏离库主设计的路径，就得用 wrapper、补丁、配置 prop 和 issue 等待来持续还债。
- ⏳ 过去实现人力稀缺，所以“能装库就不手写”是最理性的选择；agentic coding 让实现劳动成本崩塌，使拥有自定义层的经济学发生了逆转。
- 📚 从 jQuery 到 meta-framework 的抽象阶梯曾一路向上，但 Tailwind 和 shadcn/ui 已预示回归低层、回归可拥有代码的潮流。
- 🧩 关键不是“有无依赖”，而是“是否带观点”：primitive 只替你计算（scale 把数字映射为像素），不决定你画什么；framework 则替你拥有渲染、动画和交互，只留配置接口与你谈判。
- 🛠️ 作者主张的自有薄层只有几百行代码，用项目设计 token 从头塑造，可避免升级履带、等待维护者和不明原因的动画冻结；但它依赖团队维护能力，需配合 agentic code review 保持质量。
- ⚠️ 高层库仍然赢的场景：团队尚无成熟 agentic workflow、UI 纯粹是商品（如默认风格内部仪表盘）、需要极深无障碍支持的组件（combobox、日期选择器、modal），以及你没有能力判断生成结果是否正确时。
- 📉 核心启发：旧法则“越贴近 happy path 库越值”没有变，但 agentic coding 大幅移动了交叉点，让更多原本属于库侧的定制需求转移到 primitive 侧。
- 🔭 未来最有价值的代码层，可能不再是某个安装的框架，而是团队基于原语亲手写出的薄层——因为你终于可以负担得起拥有它。

---

### [](https://vale.rocks/micros/20260902-1350)

**原文标题**: [You Don't Need Initial-Scale In Your HTML - 2 Sept 2026 13:50 UTC | Vale.Rocks](https://vale.rocks/micros/20260902-1350)

这篇文章指出现代浏览器已无需再为 viewport meta 标签声明 initial-scale=1.0；只要保留 width=device-width，就能避开旧版 iOS 的缩放问题，同时还能节省 19 字节。

- 🍏 2007 年 iPhone 发布时直接加载完整桌面网站，而非当时简陋的移动版网站，因此用户需要在手机上缩放浏览。
- 🛠️ 为适应小屏幕，Apple 引入了 viewport meta 标签，之后被各浏览器广泛支持，成为响应式设计的常见做法。
- 📐 其中 width=device-width 是核心，而 initial-scale=1.0 最初只是为了规避旧版 iOS 和部分浏览器的非预期缩放行为。
- ✅ 如今这些浏览器问题已修复，所以不再需要 initial-scale=1.0 作为兼容写法。
- 💡 推荐只使用 `<meta name="viewport" content="width=device-width">`，可以精简文档头部、省下 19 字节。
- 🌏 单个页面节省虽不起眼，但考虑到整个网络的规模，累积起来的优化仍有意义。

---

### [](https://webkit.org/blog/18283/submit-your-ideas-for-interop-2027/)

**原文标题**: [  Submit your ideas for Interop 2027 | WebKit](https://webkit.org/blog/18283/submit-your-ideas-for-interop-2027/)

概述：本文邀請大家為 Interop 2027 提交提案，強調提案需符合可測試性與網路標準，並提供撰寫優良提案的具體建議與提交方式。

- 📅 重要日期：提案徵集自 2026 年 9 月 3 日開始，截止日期為 2026 年 9 月 23 日，別錯過影響網路標準的機會。
- ✅ 必備條件：成功的焦點領域提案必須具備「可測試性」與「成熟網路標準」（如 W3C、TC39），否則應先去相關標準組織提案或協助發展。
- 🔍 測試不足的技術：若技術缺乏測試或基礎設施，可考慮提議為 Interop Investigation，而非 Interop Focus Area。
- 🎯 具體明確：最佳提案應聚焦單一功能或小範圍相關功能（例如 `font-size-adjust`，而非「排版」），並明確指出具體互通性問題。
- 💡 影響與價值：需清楚描述問題，並說明對開發者與使用者的好處；來自自身經驗的使用案例或證據能讓提案更有說服力。
- 📚 穩定標準連結：提案需連結到定義該技術的穩定標準文件（如 MDN），並查閱 WPT 測試涵蓋情況，說明如何補足測試。
- ✍️ 完整論述：不要假設讀者了解往年提案或技術細節；需充分說明為何此焦點領域重要、為何優先解決，並提供多人重視的證據。
- 🗳️ 提交方式：透過 GitHub issue 提交提案，可與他人合作；若已有類似提案，建議在現有 issue 留言支持，避免重複。
- 🌍 加入協作：Interop 計畫匯聚全球開發者、瀏覽器廠商與標準組織，參與提案能共同打造更一致、可靠的網路平台。

---

### [Vue.js 贴纸、T 恤、帽子等更多](https://commitgoods.com/collections/vue-js)

**原文标题**: [
    Vue.js Stickers, Tees, Hats, and More!
 – Commit Goods](https://commitgoods.com/collections/vue-js)

overview summary  
Vue.js 官方周边商店提供多種商品，所有收益將直接贊助專案維護，並包含新品與促銷的訂閱選項。  

- 💜 Vue.js 是高效能且易於上手的網頁介面開發框架，官方周邊商品持續支持專案成長。  
- 🛍️ 目前商店有 6 件商品，包含貼紙、T 恤、馬克杯及帽子等周邊。  
- 🏷️ 商品分類：貼紙 1 款、T 恤 1 款、馬克杯 3 款、帽子 1 款。  
- 💰 價格範圍：貼紙 $10.95、T 恤 $25 起、馬克杯 $14.95 起、帽子 $22.00。  
- 📦 所有 6 件商品均有庫存，並可依價格、最新或精選排序。  
- ♻️ 每筆購買都會提撥重要比例給 Vue.js 維護者，確保是官方正版且能實際贊助專案。  
- ✉️ 可訂閱電子報，搶先得知新品發布、周邊上架及促銷代碼，並可隨時取消。

---

