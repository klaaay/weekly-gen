### [Rust 正在吞噬 JavaScript | Lee Robinson](https://leerob.com/rust)

**原文标题**: [Rust Is Eating JavaScript | Lee Robinson](https://leerob.com/rust)

Rust 正全面取代 JavaScript 工具链，从构建工具（Babel、Webpack、Terser 等）到包管理器，凭借其高性能与内存安全优势。历经多年发展，如今几乎所有主流 JS 构建工具都已拥有 Rust 重写版本或替代品，且被大型企业和知名项目广泛采用。

- 🦀 **Rust 语言优势**：Rust 以速度、可靠性、内存效率闻名，连续十年被评为最受推崇的编程语言，被 Meta、Apple、Google 等巨头用于底层系统开发。
- 🔧 **JS 工具生态重塑**：Rust 正逐步替代 JavaScript 生态中的核心工具，包括代码压缩（Terser）、转译（Babel）、格式化（Prettier）、打包（Webpack）、代码检查（ESLint）等。
- 🚀 **标志性 Rust 工具涌现**：SWC（转译与打包）、Turbopack（Next.js 默认打包器）、Rolldown（Vite 默认打包器）、Biome（格式与检查）、Oxc（全栈工具链）等均基于 Rust，性能提升数倍至数十倍。
- ⏱ **2026 年全面落地**：Turbopack 作为 Next.js 16 默认打包器（2~5 倍生产构建速度），Rolldown 1.0 稳定版（10~30 倍于 Rollup），Biome v2 支持类型感知检查，Rspack 被 TikTok、Discord 等生产使用。
- 📦 **包管理器也转向 Rust**：pnpm 11.2 引入实验性 Rust 安装引擎 pacquet，显著提升冷安装速度；类似趋势扩展至 Python 生态（uv、Ruff）。
- 🧠 **AI 编码推动 Rust 增长**：Rust 的严格编译器非常适合 AI 生成代码，Bun 甚至将核心从 Zig 重写为 Rust（超过百万行修改），使 Rust 在 2026 年大幅增长。
- 🌐 **跨生态影响**：除 JavaScript 外，Rust 正吞噬 Python 等语言工具领域，成为开发工具性能革新的通用语言。

---

### [用 Rust 重](https://bun.com/blog/bun-in-rust)

**原文标题**: [Rewriting Bun in Rust | Bun Blog](https://bun.com/blog/bun-in-rust)

Bun 从 Zig 重写为 Rust，借助 Anthropic 的 Claude Fable 5 模型和 Claude Code 的动态工作流，在 11 天内完成了 535,496 行代码的机械移植，解决了大量内存安全漏洞，并带来了性能、内存和二进制体积的全面提升。

- 🦀 用 Rust 的 `Drop` 和借用检查器系统性地消除 use-after-free、double-free 和内存泄漏，替代了 Zig 中易出错的手动 `defer` 管理。
- 🐛 通过对抗性审查（Claude 在独立上下文中审查代码）在合并前捕获了 3 个关键 bug（例如 `uv_close` 异步后 Box 悬垂指针、负时间戳的 nsec 越界、`unwrap_or` 的急切求值 panic）。
- 📦 在 11 天内完成 6,502 次提交，峰值每分钟 58 次提交；API 成本约 $165,000，若人工完成估计需 3 人一年。
- ⚡ 重写后 HTTP 吞吐量提升 2.8%–4.8%，`next build` 等 CLI 任务加速 2.2%–4.7%，二进制体积缩小约 20%（Linux 88MB→70MB）。
- 🧹 利用 Rust 的 `Drop` 修复了 `Bun.build()` 多次调用时的内存泄漏（2,000 次构建后内存从 6.7GB 降至 609MB），并修复了 128 个在 v1.3.14 中可重现的 bug。
- 🔧 通过 `PORTING.md` 映射 Zig→Rust 模式、`LIFETIMES.tsv` 分析结构体字段生命周期、64 个并行 Claude 实例协作，实现了类 transpiled 风格的机械移植。
- ✅ 使用 TypeScript 编写的测试套件（100 万断言）验证重写正确性，CI 从 972 个失败测试文件逐步降至全平台全绿。
- 🧪 合并后增加了 24/7 覆盖引导 fuzzing（超过 1000 亿次执行自动生成修复 PR），以及 Miri 和 LeakSanitizer 持续检测。
- 📉 Rust 的 LLVM 代码生成能复用栈空间，减少了 TOML 等递归解析器的栈使用；仅约 4% 代码包含 `unsafe`，且大部分为单行 C++ 互操作。
- 🚀 Bun v1.4.0 是首个 Rust 版本，已发布 canary；团队可继续用 Rust 的 borrow checker 和工具链系统性提升稳定性，无需冻结功能开发。

---

### [](https://master.dev/courses/frontend-architecture/?utm_source=email&utm_medium=javascriptweekly&utm_content=frontendcooper)

**原文标题**: [Architect Scalable Frontend Applications | Master.dev](https://master.dev/courses/frontend-architecture/?utm_source=email&utm_medium=javascriptweekly&utm_content=frontendcooper)

该课程系统讲解了前端架构从单体应用到微前端的演进路径，涵盖架构原则、模块化、单体仓库和微前端实现，并结合大量实战练习。

- 🏢 **架构基础**：软件架构围绕业务目标、质量属性和约束做决策，包含风格、特性、决策和逻辑组件四大支柱
- 🧩 **单体架构**：以电商平台为例，介绍 C4 模型可视化架构，并指出边界不清晰会导致“大泥球”代码
- 📦 **模块化单体**：通过领域驱动设计划分子域，定义文件夹结构和边界，利用 ESLint 和 Dependency Cruiser 强制依赖规则
- 📁 **单体仓库**：将单体拆为多包工作区，使用 Turborepo 进行缓存、任务编排和依赖管理，可视化包依赖关系
- 🌐 **微前端架构**：当团队需要独立部署且架构驱动因素分化时引入微前端，实现方式包括 iframe、Web 组件和 Module Federation
- ⚙️ **Module Federation**：通过运行时共享代码，支持异步加载组件，处理错误边界，并实现微前端间状态通信（如 Nanostores）
- 🔄 **版本与服务发现**：管理微前端部署需考虑服务发现模式（如 mfmanifest.json），以及多版本依赖的协调策略
- ✅ **课程总结**：强调过度使用 Module Federation 的弊端（如 CSS 冲突），并根据成本分析决定是否采用微前端

---

### [](https://octanejs.dev/)

**原文标题**: [Octane — React's programming model, compiled](https://octanejs.dev/)

Octane 是 React 的编译后进化版，原生支持 hooks、Suspense 和 actions，通过预编译消除虚拟 DOM、hooks 规则和手动依赖数组，性能大幅领先 React 19，同时保持与 React 兼容的编程模型，支持逐步迁移。

- 🚀 **零虚拟 DOM**：模板直接编译为 DOM 操作，无虚拟 DOM 开销，@for 列表只移动最少的节点。
- 🔧 **无 Hooks 规则**：依赖由编译器自动追踪，hooks 可放在条件或提前返回后，无需维护依赖数组。
- ⚡ **性能显著提升**：在多数基准测试中比 React 19 快 2–12 倍，与 Solid、Vue Vapor 等并驾齐驱。
- 🔄 **渐进迁移**：支持 .tsrx 文件，可逐个组件嵌入现有 React 19 应用，通过 OctaneCompat 保持 SSR 和上下文。
- 📦 **兼容生态**：保留 hooks、memo、Suspense 等熟悉 API，提供 43 个第一方绑定（Three.js、react-hook-form 等）。
- 🧪 **成熟测试**：1.15 万 + 次测试执行，核心套件 3900+ 用例，覆盖运行时、编译器、SSR 和绑定。
- 🛠 **实用 CLI**：提供 `octane doctor` 检测配置问题、`octane add` 安装绑定、`octane explain` 解码生产错误等工具。

---

### [《地狱》](https://www.infernojs.org/)

**原文标题**: [Inferno](https://www.infernojs.org/)

Inferno 是一个极快的、类 React 的库，专为客户端和服务端的高性能 UI 构建而设计，支持动画、React 兼容、同构渲染，并与 React 存在一些差异。社区活跃，有 Discord 群组和赞助支持。

- ⚡ 极快性能：号称最快的前端框架之一，可在移动端实现 60 FPS。
- 🔄 React 兼容：API、概念和生命周期与 React 类似，可通过 `inferno-compat` 轻松迁移。
- 🎨 原生动画支持：v8.0 新增的原生动画功能。
- 🌐 同构渲染：支持客户端和服务端渲染，服务端渲染可快速启动。
- 🔍 与 React 差异：部分合成事件系统、不支持 React Native、不使用字符串 ref、函数组件支持生命周期、样式使用 CSS 属性名（如 `background-color`）而非驼峰。
- 💬 社区沟通：有 Discord 群组可供交流提问（https://discord.gg/SUKuhgaBpF）。
- 🙏 感谢支持：有贡献者和赞助者列表，可成为赞助商或支持者。

---

### [Octane — React 的编程模型，编译](https://octanejs.dev/docs/differences-from-react)

**原文标题**: [Octane — React's programming model, compiled](https://octanejs.dev/docs/differences-from-react)

Octane 保留了 React 的组件与 Hook 核心思路，但通过编译器和浏览器原生能力简化了规则。主要差异在于 Hook 追踪、事件处理、类名组合、更新机制和错误边界等。

- 🔧 **Hook 按源码位置追踪**：不再依赖执行顺序，可在条件或早返回后使用，但循环内需用 `@for` 或抽取为子组件。
- 📋 **依赖列表可选**：编译器自动从回调捕获中推断 `useEffect`、`useMemo` 等依赖，显式数组保持原生语义。
- 🎯 **事件使用浏览器原生对象**：没有合成事件，文本输入用 `onInput` 而非 `onChange`；`onChange` 保留原生行为，并新增 `suppressNativeChangeWarning` 抑制警告。
- 🎨 **类名组合支持 clsx 格式**：`class`/`className` 可接受数组、对象、嵌套值，自动拼接为空格分隔的字符串。
- ⏱️ **更新在微任务中批处理**：无时间切片，但保留过渡更新和 `isPending`；`flushSync` 立即刷新队列。
- 🚨 **错误边界用函数组件**：通过 `@try`/`@catch` 块实现，无类组件；未捕获错误输出到 `console.error`。
- 🌐 **服务器渲染返回 `{ html, css }`**：额外包含作用域样式；流式渲染按 Suspense 就绪顺序输出；水合时值不匹配自动修补并警告。
- 🚫 **移除部分 React API**：无类组件、StrictMode 双调用、`forwardRef`、`Children` 工具（推荐 `@for`）；保留 `useDebugValue` 和资源提示。

---

### [htm](https://four.htmx.org/)

**原文标题**: [htmx](https://four.htmx.org/)

htmx 4.0 正式发布，面向 Game Boy 平台（幽默说法），旨在让 HTML 直接实现现代 UI 交互，无需手写 JavaScript。它是一个轻量级（~11k min.br'd）、零依赖、支持 15 个扩展的超文本驱动库，是 intercooler.js 的继承者。

- 🎮 htmx 4.0 为 Game Boy 和 Game Boy Color 发布（宣传语），但实质是面向浏览器的库
- 🚀 让任何 HTML 元素都能发起 HTTP 请求（不再限于 `<a>` 和 `<form>`）
- 🖱️ 支持 click、submit 等多种事件触发请求
- 🔄 支持 GET、POST、PUT、DELETE 等全部 HTTP 方法
- ✂️ 仅替换页面局部内容（hx-swap），无需整页刷新
- 📄 快速示例：`<button hx-post="/clicked" hx-swap="outerHTML">Click Me</button>` 无 JavaScript 实现交互
- 📘 配套书籍《Hypermedia Systems》免费在线阅读，讲解如何构建超媒体驱动应用（HDA）
- 💰 感谢赞助商：Platinum 和 Silver 级赞助商
- 🧩 支持 15 个扩展，零依赖，压缩后仅约 11KB
- 🐾 是 intercooler.js 的继任者，在蒙大拿州制作

---

### [htmx 4：游戏 | swag.htmx.org](https://swag.htmx.org/products/htmx-4-the-game)

**原文标题**: [htmx 4: the game | swag.htmx.org](https://swag.htmx.org/products/htmx-4-the-game)

htmx 4.0 是首个在 Game Boy 平台上发行的 JavaScript 库游戏卡带，售价 25 美元，包含四个关卡，玩家通过收集泡菜、击败敌人来解锁完整源码，旨在推广精简客户端 JS 的理念。

- 🎮 第一款专为 Game Boy 平台设计的 JavaScript 库游戏卡带
- 💲 售价 25 美元，质量保证，支持退换
- 🥒 包含四个泡菜收集关卡，充满挑战
- 👾 击败最终 Boss“Warren”可解锁 htmx 4.0 完整源码
- 🏆 目标：将客户端 JavaScript 压缩至最小，避免“膨胀”
- 🛒 产品按需定制，仅接受印刷质量问题退换

---

### [GitHub - tc39/proposal-await-dictionary: 向 ECMAScript 添加 Promise.allKeyed 的提案 · GitHub](https://github.com/tc39/proposal-await-dictionary)

**原文标题**: [GitHub - tc39/proposal-await-dictionary: A proposal to add Promise.allKeyed to ECMAScript · GitHub](https://github.com/tc39/proposal-await-dictionary)

该提案旨在为 JavaScript 提供 `Promise.allKeyed` 方法，支持以对象形式并行等待多个 Promise，并保留键名，避免瀑布流和顺序混淆问题。

- 🚀 提案状态：TC39 阶段 3，由 Ashley Claymore 等人 champion。
- 🎯 动机：直接 `await` 每个属性会造成串行等待，`Promise.all` 依赖数组顺序易导致变量名错乱。
- 💡 解决方案：`Promise.allKeyed({ shape: getShape(), ... })` 返回同名属性的结果，行为与 `Iterator.zipKeyed` 对齐。
- 🔄 额外 API：`Promise.allSettledKeyed` 类似 `allSettled`，但以对象键返回每个 Promise 的状态与值/原因。
- 🧩 语法自然：与现有代码风格一致，避免临时变量和未处理的 Promise 拒绝。
- ⚖️ 替代方案讨论：不考虑深层拷贝、仅用自有键（包含 symbol）；曾考虑 `Promise.ownProperties`、`Promise.fromEntries` 或重载 `Promise.all`，但均有不理想之处。
- 🚫 专用语法（如 Swift 的 `async let`）被列为备选，但当前提案更简洁且无需新语法。

---

### [](https://x.com/rough__sea/status/2081809131548389636)

**原文标题**: [Ryan Dahl on X: "`deno compile` will soon support using quickjs instead of v8. dramatically reduces outputted binary size

 https://t.co/FZiK3C4ym7 https://t.co/9qEJ8u3bLu" / X](https://x.com/rough__sea/status/2081809131548389636)

overview summary  
Ryan Dahl 宣布 `deno compile` 将支持使用 QuickJS 替代 V8，大幅减小生成的二进制文件体积。此举引发讨论，包括性能权衡以及 Deno 是否建立了 JavaScript 虚拟机的抽象层。

- 🚀 `deno compile` 将支持 QuickJS 替代 V8，显著减小二进制体积  
- ⚖️ 用户指出 QuickJS 执行速度更慢、功能更少，与节省约 30MB 空间需权衡  
- 🧩 有开发者好奇 Deno 是否已为底层 JS 虚拟机构建抽象层，认为此特性很酷  
- 💬 评论区出现其他运行时（如 Bun）的对比提问，显示社区对这一趋势的关注

---

### [](https://github.com/denoland/deno/pull/36194)

**原文标题**: [feat: add experimental QuickJS backend by nathanwhit · Pull Request #36194 · denoland/deno · GitHub](https://github.com/denoland/deno/pull/36194)

该 Pull Request 为 Deno 添加了实验性的 QuickJS JavaScript 引擎后端，允许用户通过 Cargo 特性在 V8 和 QuickJS 之间切换，并提供了构建、验证及编译输出的相关支持。

- 🧩 创建 `deno_v8` 外观 crate，通过 `v8` 或 `quickjs` 特性切换引擎，默认保持 V8
- 🛠️ 提供 QuickJS 构建命令：`cargo build --bin deno --no-default-features --features quickjs`
- 🚀 添加 `--engine` 标志支持 `deno compile` 和 `deno desktop` 选择 QuickJS 运行时
- 🔧 CI 增加 QuickJS 后端检查，防止回归，发布对应 `denort-quickjs-*.zip` 制品
- 🐛 修复快照恢复、事件循环、GC 重入等问题，并添加回归测试
- ❌ 用户报告运行时错误（Vite 构建失败）和 Intl.DateTimeFormat 在 QuickJS 下实现不正确

---

### [Node.js — 查看新的 Node.js API 文档预览](https://nodejs.org/en/blog/announcements/new-api-docs-beta)

**原文标题**: [Node.js — Check out the New Node.js API Documentation Preview](https://nodejs.org/en/blog/announcements/new-api-docs-beta)

新的 Node.js API 文档预览版已在 beta.docs.nodejs.org 上线，带来全新设计、内置搜索、统一视觉风格等改进，内容本身保持不变，现面向社区征集反馈。

- 🔍 新增内置搜索功能，支持键盘快捷键，可快速跳转至任意 API 页面
- 🎨 与 nodejs.org 网站统一设计系统，增加持久侧边栏、每页目录，并适配小屏幕
- 📄 提供 `llms.txt` 文件，为 AI 工具提供结构化入口
- ⚙️ 底层使用 `doc-kit` 工具重构，替代旧版文档生成器
- 🌐 即使在禁用 JavaScript 的情况下也能正常使用，支持离线访问
- 💬 欢迎在 nodejs/doc-kit 仓库提交反馈，无论大小问题
- 🙏 感谢 Node.js 网络团队和社区成员的贡献与测试

---

### [](https://oxc.rs/blog/2026-07-22-type-aware-linting-stable)

**原文标题**: [Type-Aware Linting Stable | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2026-07-22-type-aware-linting-stable)

tsgolint v7 正式发布，作为 Oxlint 的类型感知 linting 引擎，兼容 TypeScript v7，新增 16 条规则，支持配置集成与规则性能分析，性能是 ESLint 的 12–18 倍，且安装包体积缩减 26.6%。

- 🚀 发布 tsgolint v7，基于 TypeScript v7.0.2，实现 61 条类型感知规则中的 59 条
- 📋 自 alpha 版本以来新增 16 条规则，如 consistent-return、prefer-find、prefer-optional-chain 等
- ⚙️ 支持在 oxlint.config.ts 或 .oxlintrc.json 中以配置方式开启 typeAware 和 typeCheck，无需嵌入脚本或 CI 命令
- ⏱️ 新增 --debug timings 报告，显示每条规则的耗时、调用次数及来源（原生或类型感知），便于优化
- 📈 性能大幅提升：在四个大型代码库上，tsgolint 比 ESLint + typescript-eslint 快 12–18 倍（如 VS Code 83.2s → 6.96s）
- 🔧 持续优化：并发的 tsconfig 发现、缓存文件读取、批处理语义诊断、针对性快速路径使 no-unnecessary-qualifier 在 VS Code 上加快 35 倍
- 📦 压缩下载体积：Darwin ARM64 二进制减少 26.6%（29.7MB → 21.8MB），npm 压缩包减少 44.9%（13.1MB → 7.2MB），性能不受影响
- 🙏 感谢 TypeScript 团队、typescript-eslint 团队及贡献者 Connor Shea、Cam McHenry、@auvred 等的协作与支持

---

### [](https://pnpm.io/blog/releases/11.11-11.14)

**原文标题**: [pnpm 11.11-11.14 | pnpm](https://pnpm.io/blog/releases/11.11-11.14)

pnpm 11.11 至 11.14 版本新增了原生工作区发布管理、诊断命令、访问控制等多项功能，同时修复了安全漏洞、优化了性能并解决了死锁问题。

- 🚀 内置工作区发布管理：新增 `pnpm change`、`pnpm lane` 和 `pnpm version -r`，支持变更记录、发布通道和版本升级。
- 🩺 诊断命令 `pnpm doctor`：端到端检查安装环境、存储、注册表连接等，并提供修复指引。
- 🔑 包访问与团队管理：`pnpm access` 和 `pnpm team` 命令，支持在注册表上管理包权限和组织团队。
- 🔗 收敛覆盖（Convergence Overrides）：空范围选择器 `"pkg@": "<version>"` 仅当依赖满足声明范围时重写，促进兼容包版本统一。
- 📦 带 scheme 的 `peerDependencies`：支持 `npm:`、`file:`、`git:` 等方案，按版本范围匹配并自动安装。
- 🎛️ 正则脚本选择器与 `--sequential`：`pnpm run` 支持正则匹配脚本，`-s` 选项强制串行执行。
- 🔌 自定义获取器便携委托：pnpmpfile 可返回 `{ delegate: <resolution> }` 信封，由内置获取器处理。
- 🛡️ 安全修复：修复路径遍历漏洞（依赖名包含遍历序列可写至 `node_modules` 外）、拒绝恶意 lockfile 写入、限制 ZIP 解压内存占用等。
- ⚡ 性能优化：冷解析内存峰值降低约 30%，修复大元数据解析时的内存溢出。
- 🔒 死锁修复：解决了因 peer 依赖循环导致 `pnpm install` 无限挂起的问题。
- 🐛 其他补丁：修复 `pnpm update` 改写精确版本、`pnpm install` 因 lockfile 符号链接失败、`pnpm outdated` 不检查本地依赖、子进程孤儿问题等。

---

### [发布 19.2.8（2026 年 7 月 21 日）· react/react · GitHub](https://github.com/react/react/releases/tag/v19.2.8)

**原文标题**: [Release 19.2.8 (July 21st, 2026) · react/react · GitHub](https://github.com/react/react/releases/tag/v19.2.8)

React v19.2.8 版本发布，主要针对 React Server Components 进行性能改进，提升了解码效率。

- 🚀 性能提升：React Server Components 解码性能改进（#37087，贡献者 @eps1lon）

---

### [版本 19.1.9（2026 年 7 月 21 日）· react/react · GitHub](https://github.com/react/react/releases/tag/v19.1.9)

**原文标题**: [Release 19.1.9 (July 21st, 2026) · react/react · GitHub](https://github.com/react/react/releases/tag/v19.1.9)

概述摘要：React v19.1.9 版本于 2026 年 7 月 21 日发布，主要包含 React 服务器组件的性能改进。

- 🚀 React v19.1.9 于 2026 年 7 月 21 日发布（由 @eps1lon 发布）
- ⚡ 提升 React 服务器组件解码性能（PR #37088，贡献者 @eps1lon）
- 👍 获得 4 个点赞、1 个😄、1 个🎉、1 个❤️、1 个🚀、1 个👀等反应

---

### [发布 19.0.8（2026 年 7 月 21 日）· react/react · GitHub](https://github.com/react/react/releases/tag/v19.0.8)

**原文标题**: [Release 19.0.8 (July 21st, 2026) · react/react · GitHub](https://github.com/react/react/releases/tag/v19.0.8)

React v19.0.8 版本发布，主要改进了 React Server Components 的解码性能。

- 🚀 React v19.0.8 于 2026 年 7 月 21 日发布
- ⚙️ 优化了 React Server Components 的解码性能（#37089，由 @eps1lon 贡献）
- 👤 本次发布的贡献者为 eps1lon

---

### [服务器函数中的拒绝服务 · 公告 · react/react · GitHub](https://github.com/react/react/security/advisories/GHSA-wx67-qw84-cm4g)

**原文标题**: [Denial of Service in Server Functions · Advisory · react/react · GitHub](https://github.com/react/react/security/advisories/GHSA-wx67-qw84-cm4g)

React 服务端函数存在拒绝服务漏洞，影响多个 Server Components 相关包的部分版本，攻击者可远程利用导致资源耗尽，建议立即升级至修复版本。

- 🔴 **高严重性拒绝服务漏洞**：CVE-2026-44907，CVSS 评分 7.5，攻击者无需认证即可通过网络发送特制 HTTP 请求触发，导致内存溢出或 CPU 过度使用。
- 📦 **影响范围**：`react-server-dom-webpack`、`react-server-dom-parcel`、`react-server-dom-turbopack` 的 19.0.0–19.0.7、19.1.0–19.1.8、19.2.0–19.2.7 版本。
- 🛠️ **修复版本**：已回传至 19.0.8、19.1.9、19.2.8，建议立即升级。
- 🚫 **影响限制**：如果应用未使用 React 服务端组件或相关框架/打包器插件，则不受影响。
- ⚠️ **弱点类型**：CWE-400（未控制资源消耗）和 CWE-770（资源分配无限制），攻击复杂度低，无需用户交互。

---

### [Ember 7.1 发布](https://blog.emberjs.com/ember-released-7-1/)

**原文标题**: [Ember 7.1 Released](https://blog.emberjs.com/ember-released-7-1/)

Ember 7.1 发布，重点关注开发者体验提升，包括新增内置模板助手、优化 GJS 文件使用、更新 API 文档以及 CLI 的多项改进。

- 🎉 新增内置模板助手：包含 `{{element}}`、`{{and}}`、`{{or}}`、`{{lt}}`、`{{eq}}` 等，简化动态标签生成和逻辑/比较运算，不再依赖第三方插件。
- ⚡ GJS 文件自动导入：`{{on}}`、`{{fn}}`、`{{hash}}`、`{{array}}` 等常用修饰器和助手在严格模板中自动生效，无需手动 import，代码更简洁。
- 📚 API 文档全面更新：所有文档中的模板示例改用 `<template />` 标签格式，与 GJS 文件标准对齐。
- 🔧 CLI 改进和依赖更新：提取自定义语义版本行为到独立库，更新 6 个依赖包至新主版本，并修复蓝图支持 ESM 模块，为 `type: module` 铺路。

---

### [Nuxt 安全补丁发布 · Nuxt 博客](https://nuxt.com/blog/v4-5-security)

**原文标题**: [Nuxt Security Patch Releases · Nuxt Blog](https://nuxt.com/blog/v4-5-security)

Nuxt 发布了 4.5.1 和 3.21.10 安全补丁，以及@nuxt/devtools 的 3.3.1 版本，修复了多个高危和关键漏洞，建议立即升级。

- 🚀 发布 Nuxt 4.5.1 和 3.21.10 安全补丁，推荐立即升级，同时更新@nuxt/devtools。
- 🔓 修复服务端远程代码执行（高危）：仅当启用 vue.runtimeCompiler 且使用特定动态组件时受影响，攻击者可注入模板代码执行。
- ⚠️ 修复未授权组件实例化（中危）：无需 vue.runtimeCompiler，可实例化任意 HTML 元素或全局组件，但无法执行代码。
- 🛡️ 修复路由规则授权绕过（高危）：规则键含大写字符时，appMiddleware 被跳过，现改为大小写不敏感匹配。
- 🚫 修复服务器组件拒绝服务（高危）：未认证请求可通过 v-for 或超大请求体导致服务器崩溃。
- 🔐 修复跨用户缓存页面有效载荷泄露（高危，仅 4.x）：缓存_payload.json 可能被其他用户获取，升级后需清除 CDN 缓存。
- 🖥️ 修复开发服务器路径泄露（低危）：仅当 dev server 绑定网络接口时，可能暴露项目路径和 UUID。
- 🛠️ 修复 Nuxt DevTools 远程代码执行（关键，仅开发环境）：未认证 RPC 方法可通过 Vite HMR 套接字执行任意命令，请确保锁文件包含 3.3.1。
- 🙏 感谢多位安全研究人员以及 Vercel、Netlify、Cloudflare 等平台的协作。

---

### [Nuxt 4.5 · Nuxt 博客](https://nuxt.com/blog/v4-5)

**原文标题**: [Nuxt 4.5 · Nuxt Blog](https://nuxt.com/blog/v4-5)

Nuxt 4.5 版本发布，这是迄今为止最大的一次更新，带来了 Vite 8、Rspack 2、实验性 SSR 流式渲染、稳定错误代码系统、新的 useLayout 组合式函数、命名视图，并为 Nuxt 5 做好了准备。

- ⚡️ **Vite 8 升级**：冷启动更快，基于最新 Rolldown 内部机制，透明升级，但需检查自定义插件兼容性。
- 🦀 **Rspack 2 与 Rsbuild 重构**：构建器性能更高，底层基于 @rsbuild/core，开发服务器改用中间件模式。
- 🌊 **实验性 SSR 流式渲染**：可将 HTML 骨架立即发送，再流式传输主体，显著改善 TTFB，支持按路由配置，自动为爬虫回退。
- 🩺 **稳定错误代码系统**：所有错误和警告都附带稳定代码（如 NUXT_E1001），生产构建中仅保留代码，提升调试体验。
- 🎨 **新的 useLayout 组合式函数**：响应式读取当前路由使用的布局，支持只读计算属性。
- 🪟 **命名视图支持**：通过文件名约定（name@view.vue）为页面提供多个 `<NuxtPage>` 出口，基于 Vue Router 长期支持的功能。
- 🚦 **useFetch/useAsyncData 的 enabled 选项**：根据响应式条件控制是否发起请求，支持取消正在进行的请求。
- 🔗 **NuxtLink 自定义插槽预取控制**：当使用 `custom` 属性时，插槽暴露 `prefetch`、`prefetched`、`shouldPrefetch` 等属性，便于手动控制预取。
- 🌐 **import.meta.envName**：运行时获取当前 Nuxt 环境名称（如 staging），可在应用代码中分支处理。
- 🔭 **SSR 事件诊断追踪**：通过诊断通道发布 nuxt.render、nuxt.data 等事件，支持 OpenTelemetry，可在 Node、Deno、Bun 等环境使用。
- 📦 **依赖升级**：unhead v3（更好的类型安全、为流式渲染铺垫）、unctx v3（修复异步上下文问题）、magic-string v1、Babel v8 等。
- 🛠️ **CLI 改进**：新增 `nuxt module remove`、非交互式 `nuxt init`、类型检查时自动安装依赖、支持 Golar 类型检查器、本地层配置热重载等。
- 🧩 **TypeScript 插件与命名布局插槽**：实验性 TypeScript 插件新增命名布局插槽功能，允许页面向布局的命名插槽注入内容。
- 🔥 **性能与可靠性提升**：共享文件监视器（减少资源占用）、更快的开发启动、更精简的生产构建、改进岛屿哈希、自动导入 $fetch、HMR 对 JSX 中 defineNuxtComponent 的支持。
- ⚠️ **升级注意事项**：Vite 8、Rspack 2 和 unhead v3 均为重大更新，需检查自定义配置与插件兼容性；Nuxt 3 将于 2026 年 7 月 31 日 停止支持，建议尽快升级到 v4。
- ⬆️ **升级方法**：运行 `npx nuxt upgrade --dedupe`（v3 用户使用 `npx nuxt@latest upgrade --dedupe --channel=v3`）。

---

### [ESLint v10.8.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/07/eslint-v10.8.0-released/)

**原文标题**: [ESLint v10.8.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/07/eslint-v10.8.0-released/)

ESLint v10.8.0 是一个小版本升级，新增了一些功能并修复了多个错误。更新了多个规则以避免边缘情况下的意外行为，并进行了大量文档和测试改进。

- 🚀 新增功能：从 `eslint/config` 导出 `ConfigObject` 类型
- 🐛 规则修复：修复 `no-unreachable-loop`、`prefer-object-spread`、`prefer-template`、`class-methods-use-this` 和 `preserve-caught-error` 中的错误
- 📚 文档改进：修复多个链接错误、更新术语和说明
- 🔧 杂项更新：更新依赖（如 minimatch、webpack）、添加测试断言位置、CI 流程及权限调整
- 🤖 贡献者：Francesco Trotta 和其他多位开发者参与贡献

---

### [](https://github.com/denoland/deno/releases/tag/v2.9.4)

**原文标题**: [Release v2.9.4 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.9.4)

Deno v2.9.4 发布，带来多项新特性和修复，涵盖桌面端 HMR、Node 兼容性增强、V8 升级以及大量性能优化。

- 🖥️ 桌面端支持 React Router 的热模块替换（--hmr）
- 📦 Node 兼容：Buffer.indexOf/lastIndexOf/includes 新增 byteLength/length 参数，支持原始 chacha20 加密
- 🔧 V8 升级至 150.2.0
- 🐛 修复缓存、Web Cache 存储、Canvas FFI 权限、编译 Windows 资源大小等多项问题
- 🌐 修复 WebTransport 握手缓冲、URL 解析异常及证书日期验证
- 🚀 性能优化：避免重复 ESM 快照、混淆内部源标识符、压缩 AppImage 运行时、使用 FxHash 热哈希映射
- 📁 修复 npm 包下载、锁文件处理、符号链接清理等依赖管理问题
- 🔒 修复权限提示中的双向控制转义、隔离原生插件等安全相关改进

---

### [版本 7.9.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.9.0)

**原文标题**: [Release 7.9.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.9.0)

Prisma 7.9.0 稳定版发布，重点引入了 CLI 自动补全、AI 代理支持、多项 Bug 修复、Prisma Studio 更新以及 Prisma Compute 公测。

- 🎉 CLI 自动补全：Prisma 为 bash、zsh、fish 和 PowerShell 提供 shell 补全，支持命令、选项及参数值。
- 🤖 AI 代理支持：`prisma init` 安装代理技能目录，新增 AI 安全检测，对有破坏性的命令进行保护。
- 🛡️ 数据库操作安全：`db push --accept-data-loss` 加入安全措施，`migrate-reset` 工具从 MCP 服务器移除。
- 🐞 Prisma Client 修复：修复 TypeScript 性能回归、`XOR` 类型错误、查询中的 Date 验证、文档注释转义等问题。
- 🔧 CLI 稳定性：修复多文件架构中符号链接循环和重复文件问题，Windows 下引擎缓存移至稳定目录。
- 📦 驱动适配器更新：`adapter-pg`/`adapter-neon` 修复 Bytes 列警告，`adapter-mssql` 修复 null 写入错误。
- 🗄️ 模式引擎改进：`migrate status` 正确报告回滚迁移，PostgreSQL 主键约束重命名分开执行。
- 🔒 安全增强：更新依赖修复安全建议，加密 Prisma 平台认证文件，提升 OpenSSL 版本。
- 🖥️ Prisma Studio 升级至 0.33.0：新增迁移历史可视化视图、流浏览器、SQL 编辑器 schema 感知支持。
- 🚀 Prisma Compute 公开测试：托管 TypeScript 应用，无冷启动，支持推送部署、分支环境和自定义域名。

---

### [获取失败](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v830)

**原文标题**: [Failed to retrieve](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v830)

无法总结：获取内容失败，状态码 429。

---

### [](https://github.com/vuejs/core/blob/minor/CHANGELOG.md#360-rc2-2026-07-22)

**原文标题**: [core/CHANGELOG.md at minor · vuejs/core · GitHub](https://github.com/vuejs/core/blob/minor/CHANGELOG.md#360-rc2-2026-07-22)

Vue 3.6 更新日志总结，重点介绍了全新 Vapor 模式、响应式系统重构及多项破坏性变更。

- 🚀 **Vapor 模式正式推出**：全新的编译模式，基于模板的编译优化，显著减小打包体积并提升性能，完全可选，支持 `<script setup>` 组件。
- ⚡ **响应式系统重构**：基于 alien-signals 重写 `@vue/reactivity`，大幅提升性能并降低内存占用。
- 🔥 **事件委托改为 opt-in**：从 3.6.0-rc.2 起，默认不再自动委托事件到 document，需显式使用 `.delegate` 修饰符。
- 🔄 **VDOM 互操作**：通过 `vaporInteropPlugin` 实现 Vapor 与 VDOM 组件嵌套，但仍有边缘情况限制。
- ❌ **不支持的 API**：Options API、`app.config.globalProperties`、`getCurrentInstance()` 在 Vapor 中返回 null，以及 `@vue:xxx` 生命周期事件。
- 🛠️ **自定义指令接口变更**：Vapor 模式下指令接收 reactive getter 作为 value，并可返回清理函数。
- 🧪 **RC 阶段稳定性**：Vapor 模式在 3.6.0-rc.1 中功能完整，推荐用于性能敏感页面或小型新应用。
- 🐛 **大量 bug 修复**：涵盖 hydration、transition、keep-alive、teleport、dynamic component 等场景，尤其在 vapor runtime 中修复了数百个问题。
- 📦 **性能优化**：包括静态模板缓存、v-for 块优化、作用域隔离、tree-shaking 增强等。

---

### [](https://www.youtube.com/watch?v=OytpXXeNmTQ)

**原文标题**: [TypeScript 7 Is Here (And It's 10× Faster) - YouTube](https://www.youtube.com/watch?v=OytpXXeNmTQ)

YouTube 網站底部導航連結一覽，涵蓋公司資訊、法律政策與平台功能。

- 📖 簡介：介紹 YouTube 的基本資訊與使命
- 📰 新聞中心：提供 YouTube 官方新聞與更新
- ©️ 版權：說明版權相關政策與權益
- 📞 聯絡我們：提供用戶與 YouTube 聯繫的方式
- 🎨 創作者：支援內容創作者的資源與工具
- 📢 刊登廣告：廣告主可用的投放服務
- 🛠️ 開發人員：開發者使用的 API 與技術文件
- 📜 條款：使用 YouTube 的服務條款
- 🔒 私隱：隱私權保護政策與資料使用說明
- 🛡️ 政策及安全：平台內容政策與安全規範
- ⚙️ YouTube 的運作方式：解釋平台運作機制
- 🧪 測試新功能：YouTube 正在測試的新功能
- 🏢 © 2026 Google LLC：版權歸屬與法律聲明

---

### [](https://domenic.me/agentic-coding-setup/)

**原文标题**: [My Agentic Coding Setup, July 2026 | Domenic Denicola](https://domenic.me/agentic-coding-setup/)

本文描述了作者在 2026 年 7 月使用的一套 AI 辅助编程环境，核心思路是利用可丢弃的 Linux 虚拟机、Tailscale 网络、前沿的代理工具（ChatGPT 桌面应用和 Claude Code）以及一系列辅助工具，实现从手机远程修复生产 bug 的高效工作流。

- 🖥️ **核心环境：可丢弃的 Linux VM** —— 在常开台式机上运行 Ubuntu Server 虚拟机，提供 Unix 环境，并允许代理以零审批模式工作（危险但高效）。
- 🔗 **网络打通：Tailscale** —— 将所有设备（台式机、笔记本、VM）组成私有网络，支持任意地点 SSH 访问和 HTTPS 服务暴露，实现无缝远程连接。
- 🤖 **代理工具：ChatGPT 桌面应用优先** —— 其 SSH 远程支持流畅，会话同步良好；Claude 桌面应用体验较差，仍需依赖 tmux 解决断连问题。
- 🛡️ **安全与容错** —— 通过 Git 频繁推送、私有仓库备份来防范 VM 损坏；同时开启代理完全权限（包括 sudo 和 gh CLI），接受小概率风险。
- 🌲 **并行工作：Git Worktrees + Portless** —— Worktrees 让多个代理在同一项目不同分支并行工作而不冲突；Portless 为每个代理分配的开发服务器提供独立的 Tailscale HTTPS URL。
- 🧰 **配置同步：chezmoi** —— 自动同步`AGENTS.md`、技能配置等 dotfiles 到所有设备，并备份在私有 GitHub 仓库中。
- 📱 **移动端开发** —— 结合 Tailscale VPN 和 ChatGPT/Claude 手机应用，可在路上启动远程会话、修复 bug、迭代预览，最终推送 PR 并合并。
- 🔧 **代码审查：VS Code Remote-SSH** —— 通过 SSH 扩展直接打开代理在 VM 中的工作树，方便审查代码和运行命令。
- 💡 **潜在改进** —— 使用 dev containers 提升安全性和工具隔离；改进会话模型与文件夹路径的绑定；备份会话历史以供回顾。

---

### [](https://domenic.me/youre-missing-the-point-of-promises/)

**原文标题**: [You're Missing the Point of Promises | Domenic Denicola](https://domenic.me/youre-missing-the-point-of-promises/)

Promise 的真正意义常被误解：它不仅是回调聚合，更是通过函数组合与错误冒泡，让异步代码像同步一样优雅。然而，jQuery 等库的错误实现破坏了这一核心特性。

- 🎯 Promise 的核心是提供同步函数与异步函数的直接对应，实现返回值和异常传递的流畅组合。
- 🔗 `then` 必须返回新 Promise，而不是修改原 Promise 状态，这样才能支持链式调用与状态隔离。
- ⚠️ 正确处理四种场景：fulfilled/rejected 状态下的 handler 返回或抛出，缺一不可；jQuery 仅支持第一种，导致错误处理完全失效。
- 🛠️ 错误处理自动冒泡：handler 中抛出异常或错误会转化为 rejected Promise，沿链传递至最近的拒绝处理器。
- ❌ jQuery 的“Promise”只是回调聚合器，破坏了 Promise/A+ 规范，导致跨库互操作时出现神秘失败。
- ✅ 推荐遵循 Promises/A+ 的库：Q、RSVP.js、when.js，它们正确实现了函数组合与错误传递。
- 📦 若被 jQuery 等限制，可使用`Q.when()`等工具将劣质 Promise 即时转换为规范 Promise。

---

### [](https://github.com/jsdom/jsdom)

**原文标题**: [GitHub - jsdom/jsdom: A JavaScript implementation of various web standards, for use with Node.js · GitHub](https://github.com/jsdom/jsdom)

jsdom 是一个纯 JavaScript 实现的网页标准库，专为 Node.js 环境设计，旨在模拟浏览器行为，用于测试和网页数据抓取。它提供了丰富的 API 来创建和操作 DOM，支持脚本执行、资源加载、自定义配置等高级功能。
- 📦 纯 JavaScript 实现的 DOM/HTML 标准，用于 Node.js 环境下的测试与爬取
- 🛠️ 通过 `new JSDOM(string)` 快速创建 DOM 对象，获取 `window` 和 `document` 等属性
- ⚙️ 支持多种自定义选项：`url`、`referrer`、`contentType`、`runScripts`、`resources` 等
- ⚠️ 脚本执行分“危险模式”和“外部模式”，需谨慎对待未知内容
- 🎞️ 可启用视觉模拟（`pretendToBeVisual`），支持 `requestAnimationFrame` 等 API
- 🔄 子资源加载通过 `resources` 选项配置，支持自定义代理和拦截器
- 🖥️ 虚拟控制台和 Cookie jar 提供可定制的日志与状态管理
- 🎨 支持 Canvas（需安装 `canvas` 包）和编码嗅探（自动处理 BOM 及 `<meta charset>`）

---

### [多米尼克·德尼科拉](https://domenic.me/)

**原文标题**: [Domenic Denicola](https://domenic.me/)

该内容是一位最近退休的浏览器标准工程师的个人简介与作品集，涵盖其技术贡献、当前兴趣和部分代表性文章。

- 🌐 曾专注于浏览器开发与 Web 标准（如 JavaScript Promise、模块、Streams、自定义元素、导航 API 等）
- 🤖 近期研究 Web 性能（预加载）和内置 AI API，将浏览器/OS 的 AI 模型暴露给开发者
- 🇯🇵 2022 年移居东京，学习日语，关注 AI 能力与安全研究，维护 jsdom 开源项目
- 📚 代表文章包括《我的智能编码设置》《Windows 原生应用开发之乱》《论 Streams 标准》《间隔重复系统》《数学意识》《解释 Web 魔法》等
- 💻 技术方向涵盖 Web 标准、JavaScript/Node.js（迭代器、严格模式、同伴依赖）等领域

---

### [](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=sponsored)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=sponsored)

概述：Meticulous 是一款自动化、穷尽式、确定性的测试工具，能在零开发者投入下生成持续演进的端到端测试套件，帮助团队以代理编写代码的速度发布，并适用于最复杂的代码库。超过 100 家组织信赖，包括 Dropbox 和 Notion。

- 🚀 无开发工作量：开发者无需再编写、修复或维护测试，测试随应用自动演进
- 🔍 穷尽式验证：AI 引擎追踪每次交互执行的代码分支，生成覆盖所有用户流程和边缘情况的测试
- 🧪 零假阳性：默认拦截并重放后端响应，无需特殊测试账号或 mock 数据，无数据变动导致的误报
- ⚡ 闪电速度：测试在计算集群上高度并行，1000+ 屏幕的测试可在 120 秒内完成
- 🛠️ 无 flakes：从 Chromium 层级构建确定性调度引擎，彻底消除测试不稳定
- 🔄 迭代加速：持续添加新测试、移除过时测试，测试套件始终与最新代码保持同步
- 💬 客户好评：Tony Xu（Dropbox）称“工程师立刻爱上，无需调试、零维护、无 flakes”；Erdem A.（Notion）说“开发者喜爱，已成为开发流程关键护栏”
- 🧩 集成广泛：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit，可通过 script 标签或 npm 包快速接入
- 🔗 可搭配或替代现有测试套件：既可补充现有测试，也可完全取代
- 🏢 超过 100 家组织信赖：包括 Dropbox、Notion 等
- 🔒 注重安全与合规：提供访问安全文档和集成指南

---

### [](https://medium.engineering/how-we-built-the-new-table-of-contents-feature-c3825d8c279d?gi=84e0ad71ded1)

**原文标题**: [Medium](https://medium.engineering/how-we-built-the-new-table-of-contents-feature-c3825d8c279d?gi=84e0ad71ded1)

Medium 团队基于流行的 Chrome 扩展，重新设计和构建了动态目录功能，解决了静态插入、不可维护、移动端不适配等问题，最终提升了读者的使用体验。

- 💡 **灵感来源**：Chrome 扩展的流行让团队意识到用户对目录功能的需求，但静态插入正文的方式存在维护和滚动问题。
- 🔧 **核心原则**：新方案在渲染时根据文章标题动态生成目录，不修改原文，确保作者无需手动维护。
- 🚀 **桌面设计迭代**：从顶部菜单改为右侧边栏，支持高亮当前标题、窗口滑动显示有限条目，并处理全宽图片等边缘情况。
- 📱 **移动端独立方案**：桌面右侧边栏在手机上无效，团队为移动端设计了单独的解决方案（暂未详细说明）。
- ⏱️ **开发与影响**：功能开发仅需几天，主要耗时在 UX 测试和设计迭代；不损害阅读时间和收入，反而通过提升用户体验促进用户留存。

---

### [ECMAScript - 介绍使用 import](https://nitayneeman.com/blog/introducing-import-defer-in-ecmascript/)

**原文标题**: [ECMAScript - Introducing Deferred Module Evaluation with import defer | Nitay Neeman's Website](https://nitayneeman.com/blog/introducing-import-defer-in-ecmascript/)

import defer 提案是 ECMAScript 新增的模块导入方式，它在保持同步 API 的同时，将模块顶级代码的执行推迟到首次访问其命名空间属性时，从而优化大型 JavaScript 应用的启动性能。该提案目前处于 TC39 阶段 3。

- 📉 **动机**：大型应用启动慢的主因是代码执行而非下载，动态导入虽能延迟加载，但强制异步 API，而 import defer 实现的是“延迟执行”而非“延迟加载”。
- 📥 **语法**：静态形式为 `import defer * as ns from "module"`，动态形式为 `await import.defer("module")`，仅支持命名空间导入，不允许单独命名导入。
- ⏳ **行为**：模块下载和链接立即完成，但顶级代码仅在首次读取 `ns` 的属性时同步执行，后续访问如同普通命名空间。
- ⚡ **顶层 await 限制**：如果模块自身或其依赖使用了顶层 await，则所有涉及部分会提前执行，只有纯同步模块才能被延迟。
- ⚠️ **错误处理差异**：延迟命名空间在访问时始终重新抛出模块执行中的错误，避免因不同导入时机导致行为不一致。
- 🚦 **当前状态**：阶段 3，V8（Chrome 需 flag）、Deno、Bun 已默认启用，Node.js 和 SpiderMonkey 在推进，Babel 插件可直接使用。
- 🏁 **总结**：未来可替代 CommonJS 的 `require` 惰性模式，在保持同步 API 的同时减少不必要的代码执行开销。

---

### [使用 Container Timing API 测量组件性能 – CSS Wizardry](https://csswizardry.com/2026/07/meaasuring-component-performance-with-the-container-timing-api/)

**原文标题**: [Measuring Component Performance with the Container Timing API – CSS Wizardry](https://csswizardry.com/2026/07/meaasuring-component-performance-with-the-container-timing-api/)

概述摘要  
Container Timing API 是一种实验性性能接口，允许开发者标记 DOM 区域并获取内容逐渐渲染的时序数据。它解决了标准指标（如 LCP）无法衡量自定义组件完整渲染的问题，通过跟踪区域内首次及后续内容绘制，提供组件渲染的渐进式视图。与 Element Timing 不同，它关注整个子树而非单个元素，且浏览器不判断组件“完成”，而是持续报告新内容绘制。该 API 目前处于 Chrome Origin Trial 阶段，适用于电商、搜索、仪表盘等场景，但需注意它不测量交互性或视觉完整性，应谨慎用于命名指标。

- 📊 **核心问题**：标准指标（如 LCP）无法衡量用户关心的自定义组件渲染进度，需要更细粒度的组件级性能数据。
- 🧩 **API 基础**：通过添加`containertiming`属性标记 DOM 区域，使用`PerformanceObserver`监听`container`类型条目，获取首次渲染时间、最新绘制时间、累积面积等信息。
- 🔄 **更新机制**：当区域内新内容性元素（如图像、文本）绘制到未计量的区域时触发更新，忽略纯装饰和内容性变化；区域移动或滚动入视口时也可能产生新条目。
- ❌ **无完成信号**：浏览器无法判断组件是否“完成”，API 只提供一系列更新，由开发者根据业务定义有意义的时间点（如首次渲染、最后大面积更新）。
- ⚖️ **与 Element Timing 对比**：Element Timing 关注单个元素（如一张图片），而 Container Timing 关注整个组件子树，提供累积的渲染进度。
- 🏪 **实际用例**：电商产品摘要（图片、价格、按钮逐步渲染）、搜索结果网格、仪表盘组件、出版商首页文章区域等。
- 🚫 **常见误用**：不测量交互性（需配合 Event Timing）、不提供视觉完整性百分比、不是新的 Core Web Vital、不建议过度标记每个 div。
- 🧪 **实验状态**：Chrome Origin Trial（版本 148-153），需注册 token 并在 HTML 或 HTTP 头中启用；属性在不支持浏览器中无害，需特性检测。
- 📋 **最佳实践**：从高流量页面中选一个重要组件，收集首次渲染、每次更新的面积和时间、最后绘制元素标签及用户首次交互时间，观察渲染模式变化后再命名指标。

---

### [Container Timing 源试用 | 博客 | Chrome for Developers](https://developer.chrome.com/blog/container-timing-origin-trial)

**原文标题**: [Container Timing origin trial  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/container-timing-origin-trial)

Chrome 正在从 Chrome 148 开始发起 Container Timing 性能 API 的起源试验。该 API 允许开发者测量网页中特定容器（如组件、小部件）的加载完成时间，提供比 LCP 和 Element Timing 更细致的性能洞察。

- 🚀 Container Timing 是 Chrome 从 148 版开始的新起源试验，用于测量容器级组件加载性能。
- 📊 不同于 LCP 只测量最大元素，Container Timing 可跟踪任意标记容器的渲染时间。
- 🛠️ 通过在 HTML 元素添加 `containertiming` 属性来标记要测量的容器。
- 🔍 使用 `PerformanceObserver` 监听 `container` 类型条目，获取首次渲染时间、最新绘制、绘制面积等信息。
- 🚫 子容器可用 `containertiming-ignore` 属性忽略，以免干扰主容器测量。
- ⚠️ 仅追踪有实际内容（contentful paint）的绘制，空白容器或更新已有元素文本不会触发新条目。
- 🔎 建议用 `typeof PerformanceContainerTiming !== "undefined"` 进行特性检测，避免 `supportedEntryTypes` 的冻结问题。
- ✅ 最佳实践：在 HTML 中尽早设置属性、使用有意义的标识符、只测量关键区域、忽略广告等无关内容。
- ⚙️ 可通过 Chrome 148 注册起源试验令牌启用，或在 Chrome 147 启用实验性标志进行测试。
- 📝 开发者可提交 GitHub issue 反馈意见，该 API 正处于标准化进程中。

---

### [不，我们无法让 Node.js 对原型污染进行加固](https://adventures.nodeland.dev/archive/no-we-cant-harden-nodejs-against-prototype/)

**原文标题**: [No, We Can't Harden Node.js Against Prototype Pollution](https://adventures.nodeland.dev/archive/no-we-cant-harden-nodejs-against-prototype/)

概述总结  
这篇文章认为，Node.js 无法通过硬化核心来防御原型污染，因为攻击者一旦能写入 `Object.prototype`，就早已获胜。真正的防御应在应用边界阻止原型被污染，而不是依赖运行时的打地鼠式修补。

- 🛡️ 原型污染的前提是攻击者已能写入 `Object.prototype`，此时任何 gadget 都只是症状，不是漏洞根源。
- 🔨 尝试在核心或库中封堵单个 gadget 是无效的“打地鼠”游戏，因为语言处处通过原型链读取属性，漏洞无穷无尽。
- 📜 JavaScript 语法（如解构、展开、模板字面量等）都会触及原型链，导致核心难以彻底防御。
- 🧩 即使使用“primordials”保证内置方法不被篡改，也无法阻止原型污染本身，它只能维护核心自身不会因修补而崩溃。
- ❌ Node.js 安全计划不将需要已存在原型污染的 gadget 视为漏洞，因其责任在应用源头。
- 🚧 真正解决方案是在边界阻止不可信数据写入原型，例如使用 `secure-json-parse`、`{ __proto__: null }` 对象、`Map` 替代对象字典。
- ⚠️ 如果攻击者已能写入原型，游戏已经结束，唯一防御就是不让这一步发生。

---

### [](https://master.dev/blog/cloudflare-workers-and-hyperdrive-with-sveltekit/)

**原文标题**: [Cloudflare Workers and Hyperdrive with SvelteKit – Master.dev Blog](https://master.dev/blog/cloudflare-workers-and-hyperdrive-with-sveltekit/)

本文介绍了如何在 SvelteKit 应用中集成 Cloudflare Workers 和 Hyperdrive，涵盖基础概念、环境配置、数据库连接管理以及常见问题解决，提供了一套完整的全栈部署方案。

- ☁️ Cloudflare Workers 是低延迟的云函数，类似 AWS Lambda，但冷启动几乎不存在，适合动态流量场景。
- ⚠️ Workers 要求每个请求重新建立数据库连接，不能复用长连接，否则会引发性能问题和数据库过载。
- 🔌 Hyperdrive 是 Cloudflare 的解决方案，维护预热的连接池，让 Worker 快速获取数据库连接，避免每次新建 TCP 连接的开销。
- 🛠️ 使用`npx sv create`和`npx wrangler deploy`搭建 SvelteKit 项目，并启用 Cloudflare 插件。
- ❗ 构建脚本中的`wrangler types --check`可能因类型文件不匹配导致失败，建议移除或手动运行`npx wrangler types`生成类型。
- 🔗 通过 Cloudflare 仪表盘连接 GitHub 仓库，实现自动部署到 Workers & Pages。
- 🧩 SvelteKit 中 Cloudflare 的`env`对象通过`platform`属性注入到服务器端（如 page server loaders），但不能在客户端使用。
- 📡 远程函数通过`getRequestEvent`获取`platform.env`，实现安全访问 Cloudflare 资源。
- 🗄️ 在`hooks.server.js`中使用`handle`函数，每次请求时通过 Hyperdrive 建立数据库连接，并将`db`对象存入`event.locals`，供后续路由使用。
- 🧬 在`app.d.ts`中扩展`Locals`接口以定义`db`类型，确保类型安全。
- 📚 使用 Drizzle ORM 等库通过`locals.db`执行查询，示例展示了列表和条件查询。
- 🌟 整体而言，Cloudflare Workers+SvelteKit 集成出色，仅需少量配置即可快速搭建高性能应用。

---

### [MapLibre GL JS 简介](https://maplibre.org/maplibre-gl-js/docs/)

**原文标题**: [Introduction - MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/)

MapLibre GL JS 是一个用 TypeScript 编写、基于 WebGL 的交互式地图渲染库，支持矢量瓦片和样式规范，提供快速入门、多种安装方式、API 文档和丰富示例。

- 🗺️ **核心功能**：使用 WebGL 在浏览器中从矢量瓦片渲染交互式地图，外观由 MapLibre 样式规范控制。
- 🚀 **快速开始**：通过 CDN 引入 CSS 和 ESM 脚本，几行代码即可创建地图（设置容器、样式、中心点和缩放等级）。
- 📦 **npm 安装**：运行 `npm install maplibre-gl`，ESM 模块自动被打包工具识别，需额外配置 worker URL。
- 🌐 **CDN / 无打包器**：直接使用 UNPKG 加载 ESM 模块，worker 自动同源处理；严格 CSP 下需手动设置 worker URL。
- 🎨 **CSS 必用**：Popups、Markers 等 DOM 元素依赖 CSS，可通过 CDN `<link>` 或打包工具导入 `maplibre-gl/dist/maplibre-gl.css`。
- 🔒 **CSP 指令**：若启用内容安全策略，需允许 `worker-src 'self'` 和 `img-src data: blob: 'self'`。
- 📚 **文档结构**：包含主要类（Map、Markers、Controls、Sources、事件处理等）、全局函数、用户交互处理、样式和示例指南。

---

### [发布 v6.0.0 · maplibre/maplibre-gl-js · GitHub](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · maplibre/maplibre-gl-js · GitHub](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.0.0)

MapLibre GL JS 发布 **v6.0.0**，带来多项重大变更与改进，包括切换至 ESM-only 发行、移除 WebGL1 支持、优化类型系统与性能、修复大量 Bug。

- ⚠️ **改为纯 ESM 发行**：不再提供 UMD 和 CSP 专用包，需改用 `<script type="module">` 或命名导入。
- ❌ **移除 WebGL1 支持**：现仅支持 WebGL2，带来性能提升与 Terrain3D 增强。
- 🔄 **事件系统重构**：所有地图事件变为真实类，`styleimagemissing` 改为仅通知事件，并新增异步图像解析器。
- 🧩 **类型系统改进**：Map 不再继承 Camera，而是组合；Evented 变成泛型抽象类，强化类型安全。
- 🚀 **性能优化**：内联淘汰依赖、使用 texStorage2D、优化特征状态数组化（提速 3.4 倍）、减少地形绘制开销。
- 🐛 **Bug 修复**：修复透明线条伪影、相机跳跃、跨域 worker 加载、内存泄漏、web 字体渲染等问题。
- 🎨 **新增特性**：添加 `fill-layer-opacity` 和 `line-layer-opacity` 统一图层透明度、`setMissingStyleImageResolver` 异步图片解析、`terrainSkirtLength` 移除地形垂直伪影。
- 📦 **构建工具升级**：TypeScript 目标升至 ES2022，类型生成改用 rolldown-plugin-dts（快 78 倍），使用 Rolldown 替代 Rollup。
- 🌐 **其他变更**：光照插值改用球坐标、`style.load` 新增事件类、Hash 控件改用 URLSearchParams、移除 Mapbox 引用。

---

### [maplibre-gl-js/docs/guides/v5到v6迁移指南.md 在 main 分支 · maplibre/maplibre-gl-js · GitHub](https://github.com/maplibre/maplibre-gl-js/blob/main/docs/guides/v5-to-v6-migration-guide.md)

**原文标题**: [maplibre-gl-js/docs/guides/v5-to-v6-migration-guide.md at main · maplibre/maplibre-gl-js · GitHub](https://github.com/maplibre/maplibre-gl-js/blob/main/docs/guides/v5-to-v6-migration-guide.md)

MapLibre GL JS v6 迁移指南总结了从 v5 到 v6 的主要变更，涵盖包格式、导入方式、脚本标签、Worker URL、CSP 设置、参数、pragma 指令、事件处理以及图片解析器的变化。

- 📦 v6 仅提供 ES 模块，移除了 UMD 和 CSP 构建，文件名为 `maplibre-gl.mjs` 和 `maplibre-gl-worker.mjs`
- 🔄 若使用默认导入 `import maplibregl`，需改为命名导入或命名空间导入；`<script>` 标签需改用模块脚本
- ⚙️ 直接浏览器 ESM 时 `setWorkerUrl()` 自动处理，使用 bundler（如 Vite、webpack）时仍需手动调用
- 🛡️ CSP 指令调整：跨域 CDN 需在 `worker-src` 中添加 `blob:`；自托管 worker 文件则不需要
- 🔍 新增参数 `zoomLevelsToOverscale`：默认启用新切片行为，若需旧行为可设为 `undefined`
- ✏️ 将 `#pragma mapbox` 替换为 `#pragma maplibre`
- 📅 所有事件现在都是类，建议检查 `type` 字段而非使用 `instanceof`
- 🖼️ `styleimagemissing` 事件被 `Map#setMissingStyleImageResolver` 替代，用于异步加载图片

---

### [Locize – 本地化与翻译管理平台](https://www.locize.com/?from=js-weekly)

**原文标题**: [Locize â Localization and Translation Management Platform](https://www.locize.com/?from=js-weekly)

Locize 是一个连接开发者与翻译团队的本地化平台，支持无需重新部署应用即可持续交付翻译更新，由 i18next 创建者开发，提供 AI 翻译、CDN 交付及 CI/CD 集成。

- 🌐 **一站式本地化平台**：连接代码、i18n 设置与翻译团队，无需重新部署即可持续更新翻译。
- 🤖 **AI 翻译 + 手动审核**：AI 自动翻译字符串，翻译者在专用 UI 中审核、管理术语库。
- 🔄 **自动化工作流**：通过 CLI/CI/CD 自动同步键值，翻译者无需接触代码。
- 📦 **CDN/API 交付**：翻译更新通过 CDN 即时推送，无需等待应用发布。
- 🧩 **与 i18next 深度集成**：支持任何 i18n 库，原生兼容 i18next，零 JSON 文件管理。
- 👥 **面向多角色**：开发者保持代码控制，管理者监控成本与进度，翻译者使用 In-Context Editor。
- 🆓 **免费试用 + 永久免费计划**：14 天全功能试用，无需信用卡，之后可选免费或付费方案。
- 🏢 **受全球团队信赖**：如瑞士信贷、瑞士红十字会、ABB 等，提升翻译效率与交付速度。

---

### [](https://github.com/usebruno/bruno)

**原文标题**: [GitHub - usebruno/bruno: Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia) · GitHub](https://github.com/usebruno/bruno)

overview summary  
Bruno 是一款注重隐私的开源 API 客户端，通过本地文件夹存储集合，支持 Git 协作，并提供 CLI 和 Docker 工具，旨在替代 Postman/Insomnia。

- 🚀 全新 API 客户端，颠覆 Postman 等工具  
- 📁 集合以 `Bru` 纯文本格式保存在本地文件夹中，支持 Git 版本控制  
- 🔒 完全离线运行，永不提供云同步，保障数据隐私  
- 💻 支持 Mac、Windows、Linux，可通过 Homebrew、Chocolatey、Snap、Flatpak 等多种包管理器安装  
- 🛠 提供 CLI 工具（`@usebruno/cli`），便于命令行运行和 CI/CD 集成  
- 🐳 官方 Docker 镜像（`usebruno/cli`），支持 alpine/debian 架构  
- 🌟 免费开源，同时提供付费商业版以维持可持续性  
- 📜 采用 MIT 许可证，资源可参与贡献

---

### [tslog：为 TypeScript 和 JavaScript 打造优美的日志记录体验](https://tslog.js.org/)

**原文标题**: [tslog: Beautiful logging experience for TypeScript and JavaScript](https://tslog.js.org/)

tslog v5 是一个为 TypeScript 和 JavaScript 设计的通用、高性能日志库，支持 Node.js、浏览器、Deno、Bun 等多个运行时，提供漂亮的默认输出和可选的结构化 JSON，内置秘密掩码、子日志器、可插拔传输与中间件，零运行时依赖，并针对 AI/LLM 应用做了优化。  
- 🌍 **通用运行时支持** — 同一套 API 覆盖 Node.js、浏览器、Deno、Bun、React Native 和 Workers  
- 📄 **结构化 JSON 输出** — 字段优先的扁平 JSON，可直接对接日志管线，可自定义键名  
- 🎨 **默认漂亮输出** — TTY 下彩色、管道/CI 下自动去色；JSON 生产环境可选  
- 🤖 **AI 与 LLM 优先** — 字段优先调用、代理/会话关联、llms.txt、OTel-GenAI 预设  
- 🎯 **零运行时依赖** — 只有 tslog 自身，不引入任何其他包  
- 🔒 **秘密掩码** — 支持键名、路径、正则匹配，可哈希化标记，防止日志泄露  
- 🧩 **子日志器与继承** — `child()`/`getSubLogger()` 继承设置和绑定字段，名称层级可追溯  
- 🚚 **可插拔传输与中间件** — 每传输可配级别/格式，`use()` 管道可修改或丢弃日志  
- 🧪 **漂亮错误与堆栈** — 结构化的错误格式，自动解析源映射，支持因果链  
- ⚡ **高性能** — 默认批量写入 stdout、懒加载堆栈捕获、模块级摇树优化  
- 🔄 **迁移指南** — 提供从 pino、winston、consola 迁移的详细映射，以及 v4→v5 升级路径

---

### [](https://github.com/fullstack-build/tslog)

**原文标题**: [GitHub - fullstack-build/tslog: 📝 tslog - Universal Logger for TypeScript and JavaScript · GitHub](https://github.com/fullstack-build/tslog)

tslog v5 是一个跨运行时、零依赖的日志库，支持 Node.js、浏览器、Deno、Bun 和 React Native。它提供字段优先的 JSON 输出、漂亮的可读格式、内置秘密屏蔽、子日志器、中间件和可插拔传输。与 pino、winston 等日志库相比，它拥有更全面的核心功能集，并已针对 LLM/代理日志和现代 TypeScript 工作流进行了优化。

- 🌐 **通用运行时支持** — 一个 Logger 可在 Node、浏览器、Deno、Bun 和 React Native 中使用，无需额外配置。
- 📄 **字段优先的 JSON 输出** — 扁平、可观测性就绪的 JSON 格式，可自定义键名（如 `messageKey`、`timeKey`）。
- 🖍️ **默认漂亮输出，JSON 可选** — 终端中彩色显示，管道/CI 中自动去色；生产环境可通过 `type: "json"` 切换结构化 JSON。
- 🔒 **秘密屏蔽与哈希** — 支持按键名、JSON 路径、正则表达式匹配，并提供移除或哈希替换选项。
- 🧩 **子日志器与继承** — 通过 `child()` 创建子日志器，继承设置和绑定字段，名称自动累积。
- 🪟 **中间件流水线** — 使用 `.use()` 添加中间件，用于记录增强、过滤或丢弃日志。
- 🔌 **可插拔传输** — 内置文件、HTTP、环形缓冲区、工作线程传输，支持每传输级别与格式，返回分离函数。
- 🚀 **零运行时依赖** — 除自身外无任何打包依赖，树摇友好。
- ⌨️ **完整 TypeScript 类型** — 用 TypeScript 编写，支持源映射的行号定位。
- 🤖 **LLM/代理友好** — 字段优先调用、`llms.txt`、OTel-GenAI 预设，支持 OpenClaw 代理日志。
- 📊 **预设与迁移兼容** — 提供 pino、OpenTelemetry、GenAI 预设，可从 pino/winston/consola 无缝迁移。
- ⚡ **高性能** — 默认启用批处理 stdout、惰性堆栈捕获、生产模式关闭堆栈，性能优化树摇。

---

### [GitHub - sindresorhus/eslint-package-json: 针对 package.json 的强大 ESLint 规则 · GitHub](https://github.com/sindresorhus/eslint-package-json)

**原文标题**: [GitHub - sindresorhus/eslint-package-json: Powerful ESLint rules for package.json · GitHub](https://github.com/sindresorhus/eslint-package-json)

概述：eslint-package-json 是一个基于 ESLint 的强大插件，用于检查和自动修复 package.json 文件中的错误，支持 flat config 和 @eslint/json。

- 📦 可检测并自动修复 package.json 中的常见错误（如无效名称、版本范围、exports 问题等）
- ⚙️ 安装要求 ESLint >=10.4、flat config 和 ESM，推荐使用预设配置快速启用
- 📋 提供 recommended 和 all 两种配置预设，recommended 包含无争议的规则
- 🛠️ 规则丰富，涵盖依赖版本、路径规范、脚本命名、字段有效性等，部分规则支持自动修复
- 🔧 与 npm-package-json-lint 不同，它直接集成到 ESLint 中，共享编辑器集成和 --fix 功能
- 📝 可通过 eslint.config.js 灵活禁用或调整规则，无需修改 package.json 本身
- 🚀 相比 eslint-plugin-package-json，规则更少但更强大，支持原生 @eslint/json 和自动修复优先

---

### [shadscan: 审核 shadcn 应用的 UI 基础](https://www.shadscan.com/)

**原文标题**: [shadscan: Audit shadcn apps for UI fundamentals](https://www.shadscan.com/)

请提供您希望我总结的文本内容，以便我按照模板生成概述和要点列表。

---

### [发布 v2.0.0 · kenwheeler/slick · GitHub](https://github.com/kenwheeler/slick/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · kenwheeler/slick · GitHub](https://github.com/kenwheeler/slick/releases/tag/v2.0.0)

Slick 轮播库发布 v2.0.0 重大版本，主要兼容 jQuery 4，修复多项问题并清理样式与资源。

- ⚠️ 重大变更：完全兼容 jQuery 4，替换已移除的 API（如 `$.isArray` → `Array.isArray`），重写模块加载，支持非浏览器环境
- 🔧 修复多项问题：焦点/模糊事件不再阻止传播、修正 `centerMode` 时 `slick-active` 类错位、修复居中逻辑与克隆 slide 的 ID 属性、更正 dots 按钮 `aria-label` 计数、修复 SCSS 与 `@charset` 问题
- 🎨 样式与性能优化：清理 `transform` 属性（无前缀、统一间距）、移除过时 CSS（如 `-webkit` 字体平滑）、删除 SVG 字体支持、新增 woff2 与 `font-display: swap`、拖拽光标改用 `grab`/`grabbing`、允许不可拖拽时选中文字

---

### [](https://kenwheeler.github.io/slick/)

**原文标题**: [slick - the last carousel you'll ever need](https://kenwheeler.github.io/slick/)

Slick 是一款功能丰富的响应式轮播插件，支持多种配置与交互方式，适用于不同展示场景。

- 📱 **完全响应式**：自适应容器并支持按断点单独设置参数
- 🖱️ **多种触发方式**：支持触摸滑动、鼠标拖拽、键盘导航
- 🔁 **循环与无限滚动**：可开启无限循环播放
- 🎨 **灵活展示**：支持单张/多张、可变宽度、自适应高度、居中模式
- 🔄 **自动播放与淡入效果**：可设置自动轮播及淡入切换
- ➕ **动态增删筛选**：支持添加、删除、过滤与取消过滤幻灯片
- ⚙️ **丰富配置项**：包含点、箭头、回调、懒加载、RTL 等
- 🗑️ **销毁与重置**：可通过 `unslick` 彻底销毁轮播
- 🔗 **同步联动**：支持两个轮播组件相互联动导航

---

### [jQuery 4.0.0 | jQuery 官方博客](https://blog.jquery.com/2026/01/17/jquery-4-0-0/)

**原文标题**: [jQuery 4.0.0 | Official jQuery Blog](https://blog.jquery.com/2026/01/17/jquery-4-0-0/)

经过 20 年的发展，jQuery 4.0.0 正式发布，带来了大量现代化改进与破坏性变更，建议查看升级指南后迁移。

- 🎉 **发布 20 周年纪念版**：jQuery 4.0.0 于 2026 年 1 月 17 日发布，是近 10 年来的首个大版本。
- 🗑️ **不再支持 IE 10 及更早版本**：仅保留 IE 11 支持，旧版浏览器请继续使用 jQuery 3.x。
- 🛡️ **新增 Trusted Types 与 CSP 支持**：确保 HTML 操作符合安全策略，并改用`<script>`标签避免 CSP 错误。
- 🔄 **源码迁移至 ES 模块**：从 AMD 切换到 ES 模块，使用 Rollup 打包，兼容现代构建工具和`<script type=module>`。
- ❌ **移除已弃用 API**：包括`jQuery.isArray`、`jQuery.parseJSON`等 13 个函数，改用原生方法，gzip 体积减少超 3KB。
- 🧩 **移除内部方法**：从原型中移除`push`、`sort`、`splice`，需用`[].push.call()`替代。
- 🎯 **焦点事件顺序遵循 W3C 规范**：新顺序为 blur→focusout→focus→focusin，与旧版不同。
- 📦 **精简版更小**：去掉了 Deferreds 和 Callbacks，gzip 约 19.5KB，建议使用原生 Promise。
- 🔧 **升级工具**：提供升级指南和 jQuery Migrate 插件，帮助平稳过渡。
- 📥 **下载方式**：可通过 CDN（`code.jquery.com`）或`npm install jquery@4.0.0`获取。

---

### [isomorphic-git · 一个纯 JavaScript 实现的 git，适用于 node 和浏览器！](https://isomorphic-git.org/)

**原文标题**: [isomorphic-git · A pure JavaScript implementation of git for node and browsers!](https://isomorphic-git.org/)

isomorphic-git 是一个纯 JavaScript 实现的 git，可在 Node.js 和浏览器环境中运行，与标准 git 完全兼容，支持克隆、提交、推送等核心操作，并提供 CLI 和模块化 API，被多个项目广泛使用。

- 🖥️ 纯 JavaScript 实现，支持 Node.js 和浏览器（含 WebWorker、ServiceWorker）
- 📁 与标准 git 完全兼容，使用相同的 .git 目录格式操作仓库
- 🔧 核心功能：克隆、初始化仓库、分支/标签管理、提交历史、检出、推送、合并等
- ✍️ 支持 PGP 签名、git config 及原始 git 对象读写
- 🛠️ 提供 isogit CLI，可在桌面或服务器上直接操作 git 仓库
- 🎯 API 按独立函数设计，便于现代打包工具按需加载，减小 bundle 体积
- 🌐 包含交互式在线演示（输入仓库 URL 即可获取分支和标签）及详细文档
- 👥 被多个项目使用，社区活跃，有用户展示和项目案例

---

### [](https://github.com/vercel/satori)

**原文标题**: [GitHub - vercel/satori: Enlightened library to convert HTML and CSS to SVG · GitHub](https://github.com/vercel/satori)

Satori 是一个将 HTML 和 CSS 转换为 SVG 的库，主要用于生成 Open Graph 图像等场景。它支持 JSX 语法和有限的 CSS 属性，底层基于 Yoga 布局引擎，能够高效地渲染静态、可见的元素。

- 🎯 **基本用法**：通过 JSX 或纯对象定义元素，调用 `satori()` 函数即可生成 SVG 字符串，需要指定宽高和字体数据。
- ⚛️ **JSX 支持**：仅接受纯静态、无副作用的 JSX 元素，不支持 `useState`、`useEffect` 等 React 特性，但内置实验性 JSX 运行时。
- 🧩 **HTML 元素子集**：支持 `<div>`、`<span>`、`<img>` 等常见元素，不支持 `<input>`、`<script>`、`<style>` 等，且 SVG 输出可能与浏览器渲染不完全一致。
- 🎨 **CSS 属性子集**：采用 Flexbox 布局引擎，支持 `display`、`position`、`margin`、`border`、`flex`、`font`、`text`、`background`、`transform`、`opacity`、`boxShadow` 等常用属性，但无 `z-index`、`calc` 支持。
- 🔤 **字体支持**：必须提供字体数据（TTF、OTF、WOFF 格式，不支持 WOFF2），通过 `fonts` 参数传入，支持多种字重和样式。
- 😀 **表情符号**：可通过 `graphemeImages` 选项自定义特定字符的图片，或使用 `loadAdditionalAsset` 动态加载表情图像和字体。
- 🌐 **多语言与区域**：支持通过 `lang` 属性指定区域，同一个字符在不同区域可有不同渲染结果。
- ⚙️ **运行时支持**：可在浏览器、Node.js（≥16）和 Web Worker 中使用，WASM 依赖以 base64 内联加载。
- 🧰 **独立构建**：提供不包含 Yoga WASM 的独立版本，需手动加载 `yoga.wasm` 文件。
- 📝 **字体嵌入**：默认将文本渲染为 `<path>` 路径，嵌入字体数据；可设置 `embedFont: false` 改用 `<text>` 元素。
- 🔍 **调试模式**：设置 `debug: true` 可绘制边框框线辅助调试。
- 🔧 **贡献与社区**：项目开源（MPL-2.0 许可证），欢迎通过 Vercel OG Image Playground 测试和报告问题。

---

### [GitHub - lmn1919/dompdf.js: 用一行前端代码将 HTML 转换为多页矢量 PDF · GitHub](https://github.com/lmn1919/dompdf.js)

**原文标题**: [GitHub - lmn1919/dompdf.js: Convert HTML to a multi-thousand-page vector PDF with a single line of frontend code · GitHub](https://github.com/lmn1919/dompdf.js)

dompdf.js 是一个基于 Rust、WebAssembly 和 TypeScript 的纯前端 DOM 转 PDF 引擎，可在浏览器中直接生成矢量 PDF，支持分页、自定义字体、加密等高级功能，无需服务器端依赖。

- 🧩 Rust + WASM 渲染管道，输出可选中文本的矢量 PDF
- 📄 支持大型文档的分页、页眉/页脚、自定义字体和 Unicode 文本
- 🔒 提供 PDF 压缩和加密功能
- 📦 通过 npm 或 CDN 安装，库名和包名均为 `dompdf.js`
- 🚀 快速启动示例：传入 DOM 元素和配置选项，返回 Blob 文件
- ⚙️ 主线程收集 DOM 快照，Web Worker 准备渲染数据，Rust/WASM 模块写出 PDF 字节
- 📋 稳定支持分页、文本渲染、图像、背景与边框、页眉/页脚、进度回调、压缩和加密
- 📏 分页推荐容器宽度与目标页面 CSS 像素一致（A4 为 794px）
- 🔤 非拉丁文字需显式嵌入字体，提供示例字体文件
- ⚠️ 保留少量旧版兼容选项（如 `onJspdfReady`），但实际不执行
- 🛠️ 本地开发需 Node.js 18+ 和 Rust 工具链，`npm install`、`npm run build`、`npm test` 等命令可用
- 📂 项目结构清晰：src（TypeScript）、wasm（Rust 写入器）、dist（构建输出）、examples（示例）、docs（文档）、scripts（脚本）

---

### [发布 v6.9.0 · verdaccio/verdaccio · GitHub](https://github.com/verdaccio/verdaccio/releases/tag/v6.9.0)

**原文标题**: [Release v6.9.0 · verdaccio/verdaccio · GitHub](https://github.com/verdaccio/verdaccio/releases/tag/v6.9.0)

概述摘要：Verdaccio v6.9.0 版本发布，包含多项重要变更，包括提升 Node.js 最低版本要求、支持原生 ESM 构建、修复关键依赖漏洞以及改进 URL 解析。

- 🤖 要求 Node.js 22 作为最低版本，推荐使用 Node.js 24，CI 测试覆盖 22/24/26
- 📦 同时提供 CJS 和 ESM 双构建输出，通过 `exports` 字段声明，CLI 默认运行 ESM 构建
- 🔧 构建工具从 Babel 迁移至 Vite 8 (rolldown)，本地开发改用 `tsx`
- 🔧 修复 @verdaccio/hooks 8.1.1 版本，恢复 ESM 构建下的 publish/unpublish webhook 通知
- 🔒 更新所有 @verdaccio/* 依赖至 2026-07-25 批次，修复 YAML 安全漏洞 (GHSA-52cp-r559-cp3m)
- 🌐 迁移 uplink/storage URL 解析至 WHATWG URL API，消除 Node.js 22+ 的 `url.parse()` 弃用警告，改进错误处理

---

### [无](https://expo.dev/blog/how-to-grow-usage-and-revenue-for-your-mobile-app?utm_source=jsweekly&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [None](https://expo.dev/blog/how-to-grow-usage-and-revenue-for-your-mobile-app?utm_source=jsweekly&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

您好，您似乎没有提供需要总结的文本内容。请将文章或段落发给我，我将按照要求用中文生成概述和带表情符号的要点列表。

---

### [适用于任意规模时序工作负载的 Postgres | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Data 提供基于 Postgres 的时间序列服务，可处理超大规模数据（每日 3 万亿指标、3PB 数据、1 千万亿数据点），新用户可获 $1000 免费试用额度，并具备弹性扩展、成本优化、高可用、企业合规、深度可观测和快速部署等核心能力。

- 🚀 处理规模：日处理 3 万亿指标、3PB 数据、1 千万亿数据点  
- 💰 免费试用：新用户可获 $1000 信用，30 天有效，无需信用卡  
- 🔧 无缝扩展：副本集最多 10 节点，SSD/S3 分层存储，成本高效  
- 💸 成本优化：计算与存储分离，独立扩展，避免为闲置容量付费  
- 🔒 高可用性：多可用区集群，自动故障切换，时间点恢复与跨区域备份  
- 🏢 企业合规：SOC 2、HIPAA、GDPR 认证，始终加密、SSO、RBAC、审计日志  
- 📊 深度可观测：查询钻取与仪表板，可集成 CloudWatch、Datadog、Prometheus  
- ⚡ 快速部署：数分钟完成数据库配置，支持 SQL、CLI、Terraform、Cursor、Claude Code  
- 🔗 生态集成：支持主流云提供商及 Postgres 生态系统  
- 🛡️ 企业支持：合同 SLA、地区数据隔离、24/7 专家支持

---

### [获取失败](https://js1024.fun/)

**原文标题**: [Failed to retrieve](https://js1024.fun/)

无法总结：获取内容失败，状态码 403。

---

### [获取失败](https://js1024.fun/demos/2026)

**原文标题**: [Failed to retrieve](https://js1024.fun/demos/2026)

无法总结：获取内容失败，状态码 403。

---

### [合集贡献者洞察](https://insights.linuxfoundation.org/collection/details/ojsf/contributors?timeRange=past365days&start=2025-07-23&end=2026-07-23)

**原文标题**: [Collection Contributors Insights](https://insights.linuxfoundation.org/collection/details/ojsf/contributors?timeRange=past365days&start=2025-07-23&end=2026-07-23)

OpenJS Foundation 是 Linux 基金会旗下项目，旨在支持 JavaScript 生态系统，拥有 43 个项目和超过 12 万贡献者，但当前项目平均健康评分仅为 31（令人担忧）。LFX Insights 平台提供贡献者、组织、地理分布等详细数据分析，帮助开发者优化决策。

- 🏗️ 由 Linux 基金会托管，专注于促进 JavaScript 生态协作与创新
- 📦 包含 43 个活跃项目，拥有 120K+ 贡献者
- ⚠️ 平均健康评分为 31，处于“令人担忧”状态
- 📊 提供贡献者、组织活跃度、季度留存率及地理分布等维度分析
- 🔍 LFX Insights 帮助开发者和组织做出更明智的开源依赖决策

---

### [项目 | OpenJS 基金会](https://openjsf.org/projects)

**原文标题**: [Projects | OpenJS Foundation](https://openjsf.org/projects)

OpenJS Foundation 是一个中立的非营利组织，托管 JavaScript 生态系统中一些最重要的项目，通过跨项目委员会（CPC）协调治理和技术流程，支持项目从孵化到归档的完整生命周期。

- 🌐 为 JavaScript 项目提供中立家园：OpenJS Foundation 以非营利身份托管如 Node.js、Electron、Express 等核心项目，并分享治理最佳实践。
- 📊 项目分为六大阶段：包括 Impact（影响）、At-Large（一般）、Incubation（孵化）、Feature Complete（功能完整）、Sunsetting（日落）和 Archived（归档），由 CPC 监督进程。
- 🚀 影响项目代表成熟稳定：如 Appium、Dojo、Electron、Express、jQuery、Node.js、webpack 等，广泛用于移动、桌面和 Web 开发。
- 💡 At-Large 项目涵盖范围广泛：包括 AMP、ESLint、Fastify、Grunt、Jest、Lodash、Mocha、Node-RED 等，覆盖 linter、框架、测试、工具等。
- 🔬 孵化项目聚焦创新：如 kepler.gl、vis.gl、Cosmos.gl、Lit 等，涉及地理空间可视化和 Web 组件。
- 🗃️ 归档项目保留历史：如 Chassis、HospitalRun、jQuery Mobile、RequireJS 等，虽然停止活跃开发但可供参考。
- 💰 资金来源与限制：通过会员费支持项目，公司可进行定向捐赠（白金无上限，金和银按比例），个人可通过 GitHub Sponsors 等直接支持项目。

---

### [我是如何不再用完 Token 的 · Daniela Baron](https://danielabaron.me/blog/how-i-stopped-running-out-of-tokens/)

**原文标题**: [How I Stopped Running out of Tokens · Daniela Baron](https://danielabaron.me/blog/how-i-stopped-running-out-of-tokens/)

随着 AI 工程工作量的增加，作者遇到了 Token 用量限制，通过安装工具和调整习惯，在不牺牲质量的前提下大幅降低了 Token 消耗。

- 📊 **监控用量**：通过 Claude 桌面的用量仪表盘和 Claude Monitor CLI 工具实时跟踪 Token 燃烧率，提前预警。
- ✂️ **rtk（输入 Token 节省器）**：拦截并压缩 CLI 命令输出，减少送往模型的输入 Token 量（实测节省约 31%）。
- 🗣️ **Caveman（输出 Token 节省器）**：改变回复风格，去除填充词和客套话，用碎片化、项目符号和箭头链表达，提高信号密度（宣称最高节省 65% 输出 Token）。
- 🔎 **CodeGraph（结构查询）**：将代码库解析为图数据库，替代 grep/读取文件来回答结构性问题，减少上下文消耗并加快速度。
- 🧠 **默认 Sonnet + 顾问 Opus**：日常使用较便宜的 Sonnet，仅在复杂任务时由 Opus 介入，平衡成本与质量。
- 🎯 **限定 Prompt 范围**：避免加载无关历史或上下文，只保留当前问题所需的核心信息。
- 📋 **定期执行`/context`**：查看当前上下文窗口内容，发现并移除无用的上下文。
- 🧹 **审计 CLAUDE.md**：将始终加载的`@`引用改为条件加载，减少每个会话的自动上下文体积（影响整个团队）。
- 🔄 **经常`/clear`**：任务完成后清除会话，避免重放过长且无用的历史对话（提示缓存只能部分缓解成本）。
- 💡 **效果验证**：作者优化后每日成本显著下降（附有图表），并列出 Headroom、Tool Search Tool、`/checkup`等未尝试的补充工具。

---

### [](https://github.com/rtk-ai/rtk)

**原文标题**: [GitHub - rtk-ai/rtk: CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies · GitHub](https://github.com/rtk-ai/rtk)

概述摘要  
RTK 是一个用 Rust 编写的高性能 CLI 代理，可在命令输出进入 LLM 上下文前进行压缩，最高减少 90% 的 bash 输出。支持 100+ 常用命令（如 git、cargo、docker 等），集成 15 种 AI 编码工具，并提供自动重写钩子、智能过滤、分组、截断和去重策略。安装简单，支持 Homebrew、脚本、Cargo 或预编译包，配有详尽配置、分析仪表盘和隐私控制。

- 💡 **核心功能**：拦截 shell 命令输出，压缩后传给 AI 代理，降低输入 token 消耗（输出缩减最高 90%，非账单缩减）。
- ⚙️ **支持命令**：涵盖 git、cargo、grep、docker、kubectl、aws 等 100+ 命令，按类型（文件、测试、构建、包管理、容器、基础设施等）提供优化策略。
- 🔧 **安装方式**：Homebrew (`brew install rtk`)、快速脚本、Cargo 安装或下载预编译二进制（支持 macOS、Linux、Windows）。
- 🔗 **AI 工具集成**：支持 Claude Code、GitHub Copilot、Cursor、Gemini CLI、Codex、Windsurf、Cline 等 15 种工具，通过原生钩子或插件实现命令自动重写。
- 🧠 **工作策略**：智能过滤（去除噪音）、分组（聚合相似项）、截断（保留关键上下文）、去重（折叠重复行）。
- 📊 **分析面板**：`rtk gain` 可查看 token 节省统计，支持图形、历史记录、JSON 导出等。
- 🔒 **隐私与遥测**：匿名使用统计默认禁用，需显式同意后收集（设备哈希、命令类别、版本等），不收集源码、路径、参数、密钥。
- 📝 **配置与卸载**：通过 `~/.config/rtk/config.toml` 自定义，`rtk init -g --uninstall` 一键移除钩子和配置。
- 👥 **核心团队**：Patrick Szymkowiak（创始人）、Florian Bruniaux、Adrien Eppling 等，社区活跃于 GitHub 和 Discord。

---

### [](https://socket.dev/blog/slopsquatting-targets-across-frontier-llms)

**原文标题**: [New Study Identifies 53 Slopsquatting Targets Across 5 Front...](https://socket.dev/blog/slopsquatting-targets-across-frontier-llms)

概述总结  
两个 Joyfill npm 测试版被植入恶意代码，利用区块链交易下载远程访问木马 DEV#POPPER。

- 🔒 两个 Joyfill npm 测试版本被篡改，包含导入时触发的恶意植入代码  
- ⛓️ 恶意代码通过读取区块链交易来动态获取远程访问木马的下载地址  
- 🦠 最终载荷为 DEV#POPPER 远程访问木马，可完全控制受害者系统  
- 🧪 仅影响测试版（beta）发布，正式版未受波及  
- ⏰ 该事件由 Socket 研究团队于 2026 年 7 月 28 日披露

---

