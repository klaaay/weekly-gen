### [获取失败](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

**原文标题**: [Failed to retrieve](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

无法总结：获取内容失败，状态码 403。

---

### [2027 年 Webhooks 现状 · Svix](https://www.svix.com/state-of-webhooks/?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=javascript-weekly-2)

**原文标题**: [State of Webhooks 2027 · Svix](https://www.svix.com/state-of-webhooks/?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=javascript-weekly-2)

Svix《The State of Webhooks 2027》报告评估了 489 家 API 公司，涵盖原有 100 家公司、创业公司榜单、Forbes AI 50 与 Fintech 50、开发者工具/API 创业公司及 66 家 AI API 提供商，重点分析 Webhook 采用率、安全性、可靠性、文档质量以及 AI 代理集成趋势。

- 📈 Webhook 采用率持续上升：原 100 家 API 公司中，仍在运营且有公开文档的公司有 88% 提供 Webhook，高于 2023 年的 83%。
- 🔐 签名与重试机制明显改善：HMAC-SHA256 签名使用率从 2023 年的 42% 升至 59%，指数退避从 30% 升至 53%，但重放保护仍停留在 40%。
- 📚 文档质量提升最大：测试指南覆盖率从 35% 升至 68%，代码示例从 43% 升至 65%，94% 的提供商记录了事件类型。
- 🌐 Standard Webhooks 快速普及：OpenAI、Anthropic 和 Google Gemini API 均采用该规范；标准 Webhook npm 包月下载量从 170 万增至 1.18 亿，相关库总下载量超过 6.4 亿次。
- 📦 规范采用仍有限：抽查中仅 8% 的 Webhook 提供商发送 Standard Webhooks 头，包括 Replicate、Supabase、GitLab 等；AI 公司中这一比例为 17%，其他公司仅 5%。
- 🤖 AI API 仍大量依赖轮询：57 家具有长运行任务的 AI API 中，19 家仍需轮询，其中 16 家完全未提供 Webhook，包括 Mistral AI、Cohere、xAI、Together AI 和 Groq。
- 🧩 AI 公司领先部分实践：AI 公司在 Standard Webhooks 和消息 ID 上高于其他公司，但所有 Webhook 提供商中仅 11% 发布可供代理生成处理程序的事件负载。
- 🔁 三年趋势稳定向好：自动重试从 67% 升至 77.5%，指数退避从 30% 升至 52.5%，投递日志从 23% 升至 41.2%；手动重试仍是最少采用的投递实践。
- 🧪 研究方法较严谨：Claude 依据 17 项标准阅读公开文档，其中 11 项沿用旧版、6 项针对 AI 时代新增；人工复核 136 个评分，一致率 95%，并重新核验证据引用。

---

### [宣布 Parcel 3 alpha](https://v3.parceljs.org/blog/v3-alpha/)

**原文标题**: [
      Announcing Parcel 3 alpha
    ](https://v3.parceljs.org/blog/v3-alpha/)

Parcel 3 alpha 于 2026-11-04 发布，是 Parcel 的 Rust 从零重写版本，核心、CLI、开发服务器、转换器、打包器和优化器均原生实现且不依赖 Node；相比 v2 构建最高快 100 倍、内存更低，并加入原生插件、内置 JS/TS 插件运行时、自动代码分割、库模式、tree shaking 与集中配置等能力。

- ⚡ 完全 Rust 重写：自包含二进制，无 Node 依赖，充分利用多核与共享内存，避免 GC 和跨语言序列化开销。
- 📈 冷构建性能：Storybook 16.62s→572ms（29×）、文档站 87.59s→810ms（108×）、库构建 131.47s→2.71s（49×）。
- 🧠 内存占用：对应场景 7.7GB→1.5GB（少 5.1×）、13.9GB→2.1GB（少 6.6×）、5.7GB→2.3GB（少 2.5×）。
- 🗂️ 架构更简单：优先优化冷构建，支持内存增量重建，减少磁盘缓存与失效跟踪，避免一类 stale-cache 问题。
- 📦 开箱即用：内置 HTML、CSS、JS、TS、SVG、图片优化、RSS/Atom、Web Manifest 等；新增 Tailwind（无需 PostCSS）、React Compiler、MDX、SVG→JSX、glob imports。
- 🛠️ 开发体验提升：可信 HTTPS 本地 CA、macOS 下 `--open` 复用标签页、内置 bundle analyzer、`parcel run` 支持 Node 入口 HMR。
- 🔌 原生插件：支持 Rust、Go、Swift 及 C ABI 动态库，提供 SDK 与 GitHub Actions 跨平台发布流程。
- 🧩 JS/TS 插件：基于 QuickJS 的嵌入式运行时，部分兼容 Node，启动快、内存小、可多线程；高性能场景建议用原生插件。
- ⚙️ 集中配置：`.parcelrc` 统一插件配置，构建开始时一次性解析，便于查找并提升性能。
- ✂️ 打包与 tree shaking：改进 bundle 合并成本模型，450 页站点每页 HTTP 请求少 64%、传输字节少 10%；CSS 顺序更安全；支持 SVG tree shaking；移除 scope hoisting。
- 📚 库构建增强：自动读取 `package.json#exports`，支持嵌套/多入口并行构建 ESM/CJS；每模块单独输出便于消费方 tree shaking；`.d.ts` 生成后续回归。
- 🚀 试用方式：安装 `parcel@next`，或用 `@parcel/parcel3` 的 `parcel3` 命令并行体验；压缩器插件、`.d.ts`、自定义 bundler 插件、JS API 等仍在开发。

---

### [2026 年 JavaScript 现状](https://survey.devographics.com/en-US/survey/state-of-js/2026)

**原文标题**: [State of JavaScript 2026](https://survey.devographics.com/en-US/survey/state-of-js/2026)

我无法完成摘要，因为您提供的内容仅为“Loading...”，并不是一篇实际的文章或文本。

- ⏳ 当前内容只有“Loading...”这一加载提示，没有任何可提取的正文信息
- 📄 没有具体段落、观点或数据可供归纳，因此无法生成要点或概述
- ❓ 内容可能尚未加载完成，或者复制时遗漏了真正需要摘要的文字
- 🙏 建议您重新粘贴完整的文章内容，我会立即按您要求的格式整理成中文要点列表
- ✅ 收到正文后，我会提供一段不含标题的总览摘要，以及带合适表情符号的“-”项目符号要点

请把实际文章内容发给我，我会马上为您总结。

---

### [Add wasip1 support, enabling CLI, API, browser, sync/async by jakebailey · Pull Request #64174 · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/pull/64174)

**原文标题**: [Add wasip1 support, enabling CLI, API, browser, sync/async by jakebailey · Pull Request #64174 · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/pull/64174)

该 PR（#64174）由 Jake Bailey 合并 162 个提交，为 TypeScript 引入实验性的 wasip1/WASM 构建，使 `tsc` 可在 WASI 主机、CLI、LSP、API 及浏览器中以同步/异步方式运行；相关 wasm 包与接口暂标为实验性，可能随时变更。

- 🧩 同一个 `tsc.wasm` 兼具“命令”和“reactor”两种模式：可直接运行 CLI/LSP，也可实例化后交给基于 IPC 的 JS API 使用。
- ⚙️ 借助 Wasm 导出和 binaryen 技巧生成单一 blob；由于 Go 编译器尚不支持 wasip3/组件模型，目前采用 wasip1。
- 📦 新增 `@typescript/typescript-wasip1-wasm` 制品包，包含 `lib/tsc.wasm`、类型声明和 `libFiles.json`，需与主包版本一致。
- 🧪 主包中的 `typescript/wasm` 提供 reactor 宿主、最小 WASI shim、`instantiateWasm`/`instantiateWasmSync`，并支持自定义同步/异步 transport。
- 🌐 API 统一入口，Node 内建模块按需加载；`typescript/sync` 与 `typescript/async` 可在浏览器中无打包加载，`vscode-jsonrpc` 仅在连接原生服务器时加载。
- 🖥️ 从 API 启动原生 `tsc` 需 Node.js 20.16+，通过 transport 则不受此限制；CLI 的 `engines` 仍保持 16.20。
- 🧑💻 VS Code Web 扩展新增 web 入口，通过 `ms-vscode.wasm-wasi-core` 运行 `tsc.wasm --lsp`，要求 1.0.4+，支持工作区挂载、目录变更重启及 `js/ts.experimental.useTsgo`。
- ✅ 测试覆盖 `test:api:wasm`、Playwright 浏览器冒烟测试，并将 Go 测试以 wasip1 在 CI 中运行；不支持子进程、Unix socket、绝对符号链接等的测试会被跳过。
- 🐞 修复了 wasip1 下 LSP 在 `initialize` 后挂起、stdin 忙轮询/调度器饥饿、空闲状态与关闭流程等问题。
- 💬 社区测试表明浏览器 Worker 中 LSP 的 `initialize` 和诊断可正常工作，但需处理 stdin `EAGAIN`、COOP/COEP 及文档说明。
- 🚧 内容映射器（content mapper）在 wasip1 下暂不可用，因为 `getLSPSpawn()` 返回 nil；社区提出了基于 `/.typescript/host-process` 设备的补丁思路。
- 🔭 后续计划包括不将 libs 打包进二进制、增加可传入 lib 目录的新参数，以及启用 vscode.dev。

---

### [TypeScript 演练场 v2](https://www.typescriptlang.org/play/v2/)

**原文标题**: [TypeScript Playground v2](https://www.typescriptlang.org/play/v2/)

这是 TypeScript Playground v2 的界面文本汇总，涵盖代码编辑、运行输出、项目配置、分享导出以及编译器加载设置；它的主要用途是在线编写和测试 TypeScript。

- 🧑‍💻 提供 `index.ts` 只读编辑区，可打开 TypeScript AST 查看器，并支持应用覆盖配置。
- ▶️ 支持运行和清空输出；当前问题数为 0，运行后可查看控制台输出。
- 🔗 支持复制 Playground 链接、Markdown 链接或预览，以及 Issue 内容，方便分享。
- 📦 项目设置中可添加文件、符号链接，并填写路径和目标路径。
- ⚙️ 行为设置包括自动下载导入包类型，以及输入时更新分享链接。
- 🎨 编辑器设置可调整字体大小、Tab 宽度、主题、自动换行、小地图和字体连字。
- 💾 可重置或保存设置，并使用导出、确认、取消等操作。
- ⬇️ 首次使用需下载并缓存 TypeScript 编译器文件，支持重试及不再提示。

---

### [ESLint 现已正式支持对 shell 脚本进行 lint 检查 - ESLint - 可插拔的 JavaScript Linter](https://eslint.org/blog/2026/11/eslint-shell-plugin-announcement/)

**原文标题**: [ESLint now officially supports linting of shell scripts - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/11/eslint-shell-plugin-announcement/)

ESLint 正式新增对 Shell 脚本的 lint 支持，推出官方插件 @eslint/shell，继续推进其语言无关的源码检查平台目标。

- 🐚 ESLint 于 2026 年 11 月 6 日宣布正式支持 Shell 脚本 lint，这是继 JSON、Markdown 和 CSS 之后的又一语言扩展。
- 📦 新插件名为 @eslint/shell，可通过 npm install @eslint/shell -D 安装，并在 eslint.config.js 中启用推荐配置。
- ⚙️ 推荐配置默认使用 Bash，可检测未加引号的变量展开、未使用变量、不安全的 read 用法等常见问题。
- 🧩 插件支持 Bash、POSIX sh 和 MirBSD Korn shell（mksh），也可手动配置规则和 Shell 方言。
- 🔍 规则灵感来自 ShellCheck，覆盖旧式命令替换、遍历 ls 输出、未加引号展开、printf 格式字符串中的变量等问题。
- 🌳 插件将 Shell 脚本解析为 ESTree 风格语法树，使 ESLint 规则可像遍历 JavaScript 一样遍历 Shell 语法树，从而支持自定义规则。
- 🛠️ 解析器基于 mvdan-sh，即 shfmt 使用的解析器；用户还可在 ESLint Code Explorer 中查看 Shell 语法树。
- 🚀 该支持让 Shell 脚本可与项目其他代码一起使用 ESLint 配置和规则 API 进行检查，有助于统一项目质量。
- 💡 ESLint 是独立开源项目，由志愿者维护，文章鼓励有兴趣的公司赞助项目；作者为 Nicholas C. Zakas。

---

### [发布 v1.65.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.65.0)

**原文标题**: [Release v1.65.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.65.0)

Playwright v1.65.0 发布，重点包括 Bun 测试运行支持、仅失败报告、独占测试锁、新 API 与缓存配置，同时带来 TypeScript 类字段、Cookie 匹配、inert 等待、代理认证和可访问名称等行为变更，并停止支持 Node.js 20。

- 🥟 测试运行器可通过 `--bun` 在 Bun 下运行，由 Bun 自行转译 TypeScript；但无 watch 模式，`--tsconfig` 和 JSX 配置不生效，堆栈、步骤名称及控制台输出支持存在差异。
- 🚨 新增 `failures` reporter，以及 HTML、JSON、JUnit reporter 的 `onlyFailures` 选项，仅保留意外失败、flaky 和中断测试。
- 🎯 新增 `-exclusive-` 测试锁，该测试运行期间不并行执行其他测试；`test.skip()`、`fixme()`、`fail()`、`slow()` 可仅传描述并记录为测试注释。
- 🗂️ 新增 `PLAYWRIGHT_TRANSFORM_CACHE_DIR` 控制转译缓存目录；`cdpSession.send()` 支持 `timeout` 和 `signal`；`reporter.preprocess()` 中可用 `testRun.mode()`。
- ⚠️ TypeScript 类字段遵循 `useDefineForClassFields`，字段初始化器先于构造参数属性执行；读取构造参数属性的初始化器会失败，需调整初始化或关闭该选项。
- ⏳ `locator.click/check/tap/fill/clear/selectOption` 会等待元素非 `inert`；分片运行全部无匹配测试时默认报“No tests found”。
- 🍪 Cookie 匹配遵循 RFC 6265，修正子域 host-only Cookie、`Path` 前缀等匹配；`APIRequestContext` 对无名称 Cookie 的处理更规范。
- 🔐 代理凭据不再发送给网站，仅用于代理挑战；网站认证应使用 `httpCredentials`。
- ♿ 浏览器不渲染的文本不再计入可访问名称和 aria 快照；`params` 会追加到已有查询串；`.css/.less/.scss` 导入需文件存在。
- 🧹 blob reporter 会先清空输出目录；CommonJS 中导入调用位置与 ESM 对齐；不再测试 Node.js 20，Docker 镜像升级到 Node.js 26。
- 🌐 浏览器版本为 Chromium 158.0.8127.18、Firefox 159.0、WebKit 27.2，并测试 Chrome 157 与 Edge 156。

---

### [Storybook 11 Beta 版](https://storybook.js.org/blog/storybook-11-beta/)

**原文标题**: [Storybook 11 beta](https://storybook.js.org/blog/storybook-11-beta/)

Storybook 11 beta 发布，重点是为编码代理（coding agents）提供官方技能和无头 CLI 工具，让代理能自主迭代 UI 开发。新版本包体积缩小 25%，上下文交付速度比 v10 快最多 10 倍，并升级了类型安全的故事格式与各核心框架支持。

- 🚀 **代理就绪的设计系统**：Storybook 11 beta 面向 React、Vue、Angular、Web Components 和 Svelte，提供官方技能与无头 CLI 工具，帮助代理避免重复组件、错误 API 和缺失状态。
- 🧠 **官方技能（Skills）**：`ui-workflow` 引导代理使用现有组件构建 UI、编写故事、测试并提交人工审查；`component-docs` 帮助代理以高效 token 格式查找组件 API 和文档。
- 🧪 **测试与审查**：代理可通过 `storybook tools test run` 运行 Vitest 功能与可访问性测试，并用 `storybook tools review create` 生成浏览器审查页面，分组展示变更组件和受影响页面。
- ⚙️ **无头 CLI 工具**：新增 `tools` 命令，提供快速无头 Storybook，支持列出和查看组件文档，便于编写自定义技能和工作流；大型项目冷启动 docgen 结果比 v10 快约 10 倍，TypeScript 7.1 稳定后预计再快 2 倍。
- 🧩 **类型安全故事（CSF 4）**：全新 factories API 实现完全类型安全，插件可扩展类型系统；提供 codemod 自动升级现有故事，CSF 3 仍完全支持。
- 🖼️ **框架支持升级**：React 使用 `react-component-meta` 获得更快更准的元数据；Vue 升级 `vue-component-meta` 并推进 Nuxt 代理就绪；Angular 推出 `@storybook/angular-vite`；Web Components 集成插槽、事件、CSS 变量等控件支持并自动计算 CEM；Svelte 升为核心框架，支持 Svelte 5 和 SvelteKit 3。
- 🛠️ **立即试用**：运行 `npx storybook@next upgrade` 升级现有项目（含自动迁移和迁移指南），或用 `npm create storybook@next` 新建项目；遇到问题可提交 GitHub issue。

---

### [使用 `__vite-browser-external` 虚拟模块进行远程代码执行 · 安全公告 · vitejs/vite · GitHub](https://github.com/vitejs/vite/security/advisories/GHSA-p4f5-76q4-ffq7)

**原文标题**: [Remote code execution using `__vite-browser-external` virtual module · Advisory · vitejs/vite · GitHub](https://github.com/vitejs/vite/security/advisories/GHSA-p4f5-76q4-ffq7)

Vite 开发服务器存在严重远程代码执行漏洞，攻击者可通过向开发服务器发送特制 HTTP 请求执行任意代码；该漏洞主要影响显式将 Vite 开发服务器暴露到网络的用户，官方已发布多个修复版本。

- 🔴 漏洞编号为 GHSA-p4f5-76q4-ffq7，严重等级为 Critical，CVSS 评分为 9.1。
- 📦 受影响包包括 npm 的 `vite` 和 `vite-plus`；`vite-plus` 受影响版本为 `<=1.5.0`，修复版本为 `1.5.1`。
- ⚠️ `vite` 受影响版本包括 `>=8.3.0,<=8.3.6`、`>=8.2.0,<=8.2.4`、`>=8.0.0,<=8.1.6`、`>=7.0.0,<=7.3.7`、`>=4.0.0,<=6.4.5`。
- ✅ 修复版本为 `8.3.7`、`8.2.5`、`8.1.7`、`7.3.8`、`6.4.6`。
- 🌐 仅当应用通过 `--host` 或 `server.host` 显式将 Vite 开发服务器暴露到网络时才会受影响。
- 🧩 漏洞源于 `__vite-browser-external:<suffix>` 和 `__vite-optional-peer-dep:<suffix>` 虚拟模块未对来自 URL 的模块 ID 进行转义，导致可注入任意代码。
- 📂 注入后可利用模块引用绕过 `server.fs` 检查，从而读取敏感文件。
- 💻 Vite 对 `new Worker` 和 `import.meta.glob` 使用 `eval` 提取模块值，攻击者可借此在服务器端执行注入代码，并可通过 `globalThis.process.getBuiltinModule` 等方式绕过限制。
- 🧪 PoC 展示了先确认 `/tmp/decoy-secret.txt` 被 403 阻止，再通过特制请求将文件拉入模块图并成功读取其内容。
- 🛠️ Vite 8 的漏洞代码位于 Rolldown 二进制中；Vite `8.3.7` 和 `8.2.5` 依赖 Rolldown `1.2.17` 的修复，Vite `8.1.7` 依赖 Rolldown `1.1.7`。
- 🏷️ 弱点类型为 CWE-116：输出编码或转义不当；目前无已知 CVE ID。
- 👥 报告者包括 g2hsec、spansh、martinpriest、zooyeon；该报告在 AI 辅助下提交。

---

### [2026 年 11 月安全更新 | Next.js](https://nextjs.org/blog/november-2026-security-release)

**原文标题**: [November 2026 Security Release | Next.js](https://nextjs.org/blog/november-2026-security-release)

Next.js 发布 2026 年 11 月安全更新，修复多个缓存、响应处理与图片优化相关问题，受影响用户应尽快升级至 v16.4.5（Active LTS）或 v15.5.29（Maintenance LTS）。

- 🔴 **高危：跨租户缓存泄露**：同时使用 `unstable_cache` 与 `use cache`、且缓存函数读取租户标识等 root parameter 时，冷缓存填充期间可能把其他租户的数据写入并返回给后续调用者。
- 🟠 **中危：嵌套 `use cache` 跨 root parameter 泄露**：内层缓存函数读取 root parameter 且外层未等待慢速异步值时，外层条目可能在依赖记录前被存储，导致租户、站点或语言环境内容被错误复用。
- 🟠 **中危：二进制参数导致跨用户缓存泄露与污染**：不同二进制参数可能生成相同缓存标识；若用于区分用户或账号，调用者可能收到他人缓存结果，或自己的结果被提供给他人。
- 🟠 **中危：自托管共享 shell 缓存污染**：启用 Cache Components 且未启用 Partial Prefetching 的 `next start` 应用，可能被未认证请求通过特制 URL 污染共享页面 shell，造成错误服务端渲染内容或持续 404。
- 🟠 **中危：过期压缩响应框架导致跨客户端响应注入/泄露**：自托管应用原样转发解压后的响应体但保留原压缩响应头时，在特定 HTTP/1.1 反向代理与共享后端连接场景下，响应可能被分配给错误客户端。
- 🟠 **中危：Edge 路由通过内部响应头暴露 Cookie**：Edge Route Handler 或 Edge API Route 使用 `NextResponse.cookies.set()` 设置 Cookie 时，序列化 Cookie 可能出现在可被同源 JavaScript 读取的 `x-middleware-set-cookie` 响应头中，即使标记为 `HttpOnly`。
- 🟠 **中危：图片优化 SVG 拒绝绕过**：攻击者控制的允许来源图片可能被误判为 AVIF，绕过 `images.dangerouslyAllowSVG: false`，使后端将原始字节识别并解码为 SVG，增加 SVG 解析器资源耗尽或解码器漏洞暴露风险。
- 🛡️ **安全项目与报告渠道**：Vercel 通过 Open Source Bug Bounty 与安全研究者合作；相关问题可联系 `security@vercel.com`。

---

### [Node.js — 2026 年 11 月 11 日星期三安全版本发布](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases)

**原文标题**: [Node.js — Wednesday, November 11, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases)

Node.js 计划于 2026 年 11 月 11 日（周三）或之后不久发布 26.x、24.x、22.x 安全版本，以修复最高严重级别为 HIGH 的安全问题；同时提醒用户使用受支持的最新版本，并关注后续安全公告。

- 🛡️ 26.x、24.x、22.x 三个发布线都将发布安全更新，最高严重级别均为 HIGH。
- 📅 安全版本预计于 2026 年 11 月 11 日（周三）或之后不久提供。
- ⚠️ 发生安全发布时，End-of-Life（已停止维护）版本始终会受到影响，建议按发布计划使用最新版本。
- 🏢 超过 Maintenance LTS 阶段的版本可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获得商业支持。
- 📢 可通过 Node.js 安全政策、SECURITY.md 流程及 nodejs-sec 邮件列表获取漏洞报告和安全更新信息。
- 🔜 下一次安全版本计划为 2026 年 10 月 21 日（周三）。

---

### [多线程 JavaScript ← arv-o-matic](https://blog.arv.tools/archives/2026/11/02/18.35.20/)

**原文标题**: [Multithreaded JavaScript ← arv-o-matic](https://blog.arv.tools/archives/2026/11/02/18.35.20/)

文章围绕多线程 JavaScript 的共享内存模型展开，记录了作者的三次实现尝试：从 Porffor 的“共享一切”实验，到面向当今浏览器的 @arv/threads，再到贴近 TC39 structs 提案的 @arv/structs，核心目标是让多个线程共享同一堆、全局环境与模块图，而不是像 Worker 那样彼此隔离。

- 🧵 共享线程与 Worker 的关键区别：共享线程共享同一 realm、模块图和对象堆，可直接读写同一 JavaScript 对象；Worker 则各自拥有独立堆、全局和模块图。
- 🔒 Pizlo 模型：读操作不加锁；对象记住创建它的线程，创建线程写入只需比较锁字；其他线程写入时对象被移交并加锁；允许竞态，但不会崩溃、撕裂或产生虚假值，也不会丢失无关属性的写入。
- 🧪 Phase 1 Porffor：将 JS AOT 编译为 C，再转 WebAssembly 或原生代码；改造后支持 Thread、Lock、Condition、SharedArrayBuffer 和 Atomics；GC 采用 stop-the-world 与安全点扫描；线程程序仅慢 0–7%，基准约慢 1%；8 线程 Mandelbrot 约 7 倍加速。
- 🧩 Phase 2 @arv/threads：为在当今浏览器和现有 JS 速度下使用，采用类型标注与所有权检查；值分为 Sending<T>、Shared<T> 和共享单元（struct、SharedArray、SharedMap、Lock、Channel）；检查器可发现发送后使用、别名、强转写共享值、async 中阻塞调用等问题。
- ⚙️ @arv/threads 编译器把共享 struct 布局到共享内存，字段读取变为类型化数组访问；N-body 800 体在 1/2/4/8 线程为 29/15/8/6 ms，单线程普通对象为 25 ms，仅擦除类型则 1820 ms；支持 i32、u8、bool、str、ref<T> 等字段。
- 🚧 Phase 2 的限制：实验性；共享内存固定 256 MB 且尚未完全释放；闭包不能跨线程；SharedMap 只有单锁；提供浏览器 playground。
- 📦 Phase 3 @arv/structs：按 TC39 structs 提案实现运行时与编译器，覆盖 struct、shared struct、SharedArray、Atomics.Mutex、Atomics.Condition；共享堆是一个 SharedArrayBuffer，每个共享 struct 在每个 worker 中用 Proxy 表示且 === 成立，字段可用类型化数组直接访问。
- 👷 Phase 3 示例：4 个 worker 通过共享 Tally 与 Mutex 共同计数到 1,000,000；postMessage 传递的是同一共享对象而非副本；仅声明为 shared struct 的对象被重写，普通路径不付成本。
- 🏁 结论：Phase 1 的“共享一切”模型最易用，但需要引擎支持，Bun 的 PR 值得关注；Phase 2/3 是当下可用方案；即使 LLM 能代写 SharedArrayBuffer 与编解码，序列化成本仍真实存在，架构可能败在序列化上。

---

### [Porffor](https://porffor.dev/)

**原文标题**: [Porffor](https://porffor.dev/)

Porffor 将 JavaScript 引擎重构为编译器，主打 AOT 编译、极低内存占用和二进制体积，适用于服务端、嵌入式等场景；目前处于 alpha 阶段，兼容性仍在持续完善。

- 🧠 Porffor 将 JS 引擎重构为编译器，像 C/Rust 一样在构建期一次性编译，运行时零解释。
- 📉 内存效率高一个数量级：1GB 内存可承载 1000+ 应用；Porffor 达 1,144 apps/GB、0.9MB/应用，约为 Node 容器的 40 倍、自托管 workerd 的 25 倍。
- ⚙️ 传统 Node/Deno/Bun 每次启动执行字节码/机器码，而 Porffor 在构建期将 JS/TS 经 C 编译为机器码。
- 🧪 需从头重新实现整个语言，使用官方 ECMAScript 测试套件 Test262；当前为 alpha，仍在快速改进。
- 📦 可编译 76.8% 的 1,295 个热门 npm 包，输出与 Node 匹配；通过 Effect 自身测试套件的 96.8%。
- 🧳 以单文件分发，用户直接运行；小型应用最高比打包 Bun/Deno 小 50 倍，React SSR 演示仅 2.6MB（Node 137MB、Deno 79MB、Bun 59MB）。
- 🌍 通过 C 编译，任何有 C 编译器的目标都能原生运行 JS，如嵌入式设备和特殊架构；也支持 WebAssembly，优于嵌入解释器方案。
- 🛠️ 安装命令：`curl -fsSL https://porffor.dev/install.sh | sh`。

---

### [JavaScript 结构体](https://tc39.es/proposal-structs/)

**原文标题**: [JavaScript Structs](https://tc39.es/proposal-structs/)

该草案提出为 JavaScript 增加固定布局对象 Struct 与可跨 agent 共享的 Shared Struct，并配套 SharedArray、Atomics 扩展以及 Mutex/Condition/UnlockToken 等高层同步原语；目标是在保证布局稳定与访问安全的前提下，支持共享内存并发编程。

- 🧱 Struct 是密封（sealed）的固定布局对象，所有声明字段会在实例暴露给用户代码前初始化；Struct 只能继承其他 Struct。
- 🔒 Struct 实例方法是非泛型的：当 `this` 不是声明该方法的 Struct 实例或其子类实例时，会抛出 `TypeError`。
- 🌐 Shared Struct 是可跨 agent 共享的固定布局 exotic object，不能包含方法或私有字段，字段只能保存原始值或其他可共享值。
- 🧵 Shared Struct 字段访问默认是无序（unordered）的，并受内存模型约束；可通过重载后的 Atomics 方法获得顺序一致性（seq-cst）访问。
- ⚛️ Atomics 扩展支持对 Shared Struct 字段执行 `load`、`store`、`exchange`、`compareExchange` 等原子操作。
- 🛡️ Shared Struct 创建使用临界区语义，避免其他 agent 观察到部分初始化的 Shared Struct 值；实现中不得允许 out-of-thin-air reads。
- 📦 新增 `Reflect.canBeShared(val)`，用于判断某个值是否可跨 agent 共享；原始值和 Shared Struct 可共享，其他对象默认不可共享。
- 🗃️ SharedArray 是带数组索引属性和不可变 `length` 属性的特殊 Shared Struct，长度在创建时固定。
- 🔐 Mutex、Condition、UnlockToken 作为无字段 Shared Struct 提供高层同步原语，支持 `lock`、`lockIfAvailable`、`unlock`、`wait`、`waitFor`、`notify` 等操作。
- 🧠 内存模型区分原子访问与数据访问：原子访问为顺序一致，数据访问为无序；支持 `seq-cst` 与 `unordered`，不支持 release-acquire 等中间强度排序。
- 📤 模块系统允许 `export default struct`，并定义 Struct 声明、绑定与求值等运行时语义。

---

### [Node.js — Node.js 26 到 27（Alpha）中值得注意的 V8 变更](https://nodejs.org/en/blog/announcements/notable-v8-changes-from-node-js-26-to-27-alpha)

**原文标题**: [Node.js — Notable V8 changes from Node.js 26 to 27 (Alpha)](https://nodejs.org/en/blog/announcements/notable-v8-changes-from-node-js-26-to-27-alpha)

Node.js 27 Alpha 将 V8 从 14.6 升级至 15.6，带来新的 JavaScript 语言特性、语义修正、序列化与内存行为变化、性能优化、诊断工具调整及 WebAssembly 更新。Alpha/Current 阶段仍可能出现 V8 破坏性变更；影响原生插件 ABI 时会提升 NODE_MODULE_VERSION，进入 LTS 后预计保持稳定。

- 🚀 **版本与发布节奏**：V8 升级到 15.6；Alpha/Current 阶段可能引入批量升级等破坏性变更，ABI 变更会伴随版本号提升。
- ✨ **默认语言特性**：新增 `Math.sumPrecise()` 减少浮点累加误差、`Intl.Locale.prototype.variants`，以及迭代器 `join()`、`includes()`、`Iterator.zip()`、`Iterator.zipKeyed()`。
- 🧪 **实验性特性**：新增 `--js-import-bytes`、`--js-regexp-buffer-boundaries`；修复 `import defer`、不可变 ArrayBuffer 等相关实现。
- 🔢 **Math 行为变化**：部分 Math 方法改用 LLVM libm，结果可能与旧版存在最后一位差异；`Math.random()` 改用直接 xorshift128+，相同 `--random-seed` 的序列也改变。
- 📅 **Date 变化**：`getTimezoneOffset()` 不再截断为整分钟，历史时区可能返回小数。
- 🔀 **数组排序**：大数组的 `Array.prototype.sort()` 改用 PowerSort，排序仍稳定，但比较器调用次数和副作用测试可能不同。
- 🧱 **错误栈访问**：`error.stack` getter 不再沿原型链查找捕获的栈；普通 `Error`、子类和 `Error.captureStackTrace` 对象不受影响。
- ⏳ **Promise 与 async/await**：顶层 await 的 ESM 求值不再触发会查找 `constructor`/`Symbol.species` 的 `then()`；`Promise.try` 在特定同 realm Promise 场景直接返回原 Promise。
- ⚛️ **Atomics 修正**：已阻塞 worker 再次 `Atomics.wait()` 抛 `TypeError` 而非崩溃；`notify/wait/waitAsync` 先读取类型数组长度再强制转换索引。
- 🔁 **迭代器辅助方法**：`take()`/`drop()` 传入超过 `2^53-1` 的有限值会抛 `RangeError` 并关闭迭代器；`Symbol.asyncDispose` 调用 `return()` 时不传参数。
- 📦 **模块语义**：`new import(...).x` 正确抛出 `SyntaxError`；部分模块加载崩溃边缘情况改为返回错误。
- 🔍 **正则表达式**：`/u`、`/v` 模式下负向 lookahead/lookbehind 不再匹配代理对内部。
- 🧮 **TypedArray 修正**：`subarray()` 对可调整 ArrayBuffer 子类省略多余 `undefined` 参数；`Float16Array` 的 `indexOf/lastIndexOf/includes` 支持负值；不可变缓冲区 `set()` 负偏移先抛 `TypeError`。
- 🧩 **语法与语义修正**：静态类初始化块中实例成员后的 `await`/`return` 正确报 `SyntaxError`；C 风格 for 初始化中的 `using` 只释放一次并视为不可变；转义 `get/set` 字段名获得 ASI；`delete super[key]` 先检查 `this`；`new Function` 先检查代码生成策略。
- 🛑 **致命错误处理**：更多 V8 致命错误先交由 Node.js 处理，`--report-on-fatalerror` 可生成诊断报告；极端语言特性使用可能改为 `RangeError`。
- 💾 **序列化变化**：`v8.serialize()`、`structuredClone()`、`postMessage()` 使用新格式，旧版 Node.js 无法反序列化；新格式支持更大可调整 ArrayBuffer，但 `v8.serialize()` 仍有 4 GB 限制。
- 🧠 **内存变化**：4–15 GB 内存机器默认老生代上限提高为物理/容器内存一半并限制在 256 MB–4 GB；Buffer/ArrayBuffer 计入 V8 全局分配限制；字节码按约 3 分钟未运行而非 GC 次数刷新。
- 📈 **性能优化**：数组方法、字符串、对象属性访问、Promise/async、RegExp、JSON.parse、BigInt 模除、模块解析及 Maglev 等多处优化；部分正则首次运行因提前编译可能变慢。
- 🧰 **诊断与调试**：堆快照更详细但体积和耗时约翻倍，并包含完整脚本源码，需按敏感数据处理；Live edit 支持完全移除；Profiler 转义和 jitdump 修复；追踪事件受 Perfetto 迁移影响。
- 🕸️ **WebAssembly 变化**：asm.js 不再编译为 Wasm；`--experimental-wasm-<name>` 更名为 `--wasm-<name>`；移除惰性验证、异步编译等旧标志；`memory.copy/fill` 内联、引用类型调用和 Table 填充等优化。
- 🏷️ **V8 标志调整**：多个已默认启用的 `--js-*` 标志被移除，若干实验性/矛盾标志重命名或删除，工具链需更新相关参数。

---

### [自动化调试与 AI 根因分析 | Sentry](https://sentry.io/resources/automated-debugging/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-evergreen&utm_content=newsletter-sponsored-link-resource-hub-learnmore)

**原文标题**: [Automated Debugging & AI Root Cause Analysis | Sentry](https://sentry.io/resources/automated-debugging/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-evergreen&utm_content=newsletter-sponsored-link-resource-hub-learnmore)

Sentry 的自动化调试将“发现—诊断—修复”闭环交给 AI 代理：错误监控捕获问题，Seer 基于生产上下文定位根因并生成修复 PR，开发者主要审核与合并；同时通过 MCP 接入自有代理和现有工具链，减少手工复现与修复成本。

- 🐞 自动化调试的核心是让系统端到端完成 bug 检测、诊断和修复，减少开发者手动复现、追踪和打补丁的工作。
- 🧭 典型流程分三步：检测（PR 或生产环境）→ 诊断（自动根因分析定位到具体代码行）→ 修复（生成补丁并打开 PR，可迭代 CI 与评审反馈）。
- 🤖 Seer 在错误发生时即可利用堆栈跟踪、引入问题的提交、Session Replay 等上下文，快速追溯根因并编写修复。
- 🔌 Sentry MCP Server 可连接 Claude Code、Cursor、Windsurf 等 MCP 兼容代理，让代理查询生产问题并提交修复。
- 🛠️ Seer Autofix 能对 issue 执行根因分析，自动打开包含修复和问题解释的 PR。
- 🔗 支持 GitHub、GitLab、Bitbucket、Azure DevOps，以及 Slack、Linear、Jira、PagerDuty，便于在团队现有工作流中触发和跟踪修复。
- 👀 自动化程度可控：团队可人工审核每个 PR，也可让代理夜间自动分诊并生成修复 PR。
- 📈 效果案例包括 Bolt 将 MTTD 降低 99%、Supabase 每周崩溃从 600+ 降至 10 以下、Anthropic 600+ 工程师使用 Sentry。
- 📚 资源涵盖博客、工作坊、客户故事和 Cookbook 配方，涉及 Next.js 静默结账失败、Supabase 安全通告、Cursor/Claude 集成等场景。
- 🚀 在付费 Sentry 计划中添加 Seer、连接代码仓库并开启，即可开始自动发现和修复 bug。

---

### [Spreading Liquid with three.js | mofu](https://mofu-dev.com/en/blog/fluid-foundation/)

**原文标题**: [Spreading Liquid with three.js | mofu](https://mofu-dev.com/en/blog/fluid-foundation/)

本文介绍作者如何在 three.js 中实现“液体粉底铺展”效果：基于已有的流体模拟速度场，用高度图记录液体厚度，结合透明度历史、法线计算和 Matcap 渲染，表现液体被拖拽后隆起、流动并留下痕迹的视觉。该方法侧重视觉效果而非物理精确，并附带纹理精度与三色液体混合实验。

- 🧪 背景：效果源自 2021 年日本化妆品品牌粉底推广项目，并在 Vue Fes Japan 2026 分享实现思路。
- 🌊 核心方案：沿用前文流体模拟的速度图，用其驱动液体铺展运动。
- 📏 高度图：用 FBO 保存液体厚度，每个像素的高度值表示该处液体量。
- 🔁 厚度更新：根据速度图反向追踪来源 UV，从源位置采样高度，计算当前像素“移出”和“移入”的厚度。
- 🎛️ 速度阈值：用 smoothstep 让低速区域几乎不流动，使运动集中在拖拽影响区域。
- 🫧 透明度历史：额外维护 alpha map，记录液体经过位置的最大值，避免厚度降低后颜色立即消失。
- 💡 法线计算：在片元着色器中采样相邻高度，通过叉积得到表面法线，制造隆起与高光。
- 🎨 渲染方式：不移动实际几何顶点，而是用高度图控制形状、Matcap 控制颜色高光、alpha map 控制残留透明度。
- ⚠️ 非物理精确：片元着色器无法直接向目标像素写值，多个像素可能采样同一来源，导致总体积不守恒，圆形拖动时液体量会累积。
- 🔬 纹理精度：32 位浮点纹理比 8 位纹理能更精细保存高度，减少法线和明暗上的阶梯感。
- 🌈 三色液体实验：三种液体各自拥有高度图和 alpha 历史，共享速度图，并用简化 Kubelka–Munk 模型混合颜色。
- 📝 写作动机：作者希望记录自己摸索出的实现方法，在 AI 更强之前留下思考与实现轨迹。

---

### [Prepack，重获新生](https://jamesbox.exe.xyz/artifacts/prepack-revived/)

**原文标题**: [Prepack, revived](https://jamesbox.exe.xyz/artifacts/prepack-revived/)

报告回顾了 2026 年复活 Prepack 的工程结果：团队用 AI agents、SMT 求解器 Z3 和差分模糊测试器重新攻克 Facebook 2018 年放弃的 JavaScript 部分求值器难题，并把问题追踪器、模糊测试发现和真实库片段整理成 194 个硬用例。原版 Prepack 0.2.54 仅通过 40/194，43 个静默错误；复活版通过 190/194，0 个静默错误，4 个为有意保留的干净诊断错误。核心结论是：多数历史难题已被工程化解决，但循环/递归等本质不可判定问题仍通过“可证明则变换、不可证明则拒绝”的方式处理。

- 🧭 **背景**：Prepack 是 Facebook 的 JavaScript 部分求值器，2018 年停止维护；复活项目重新处理其作者称为“困难、不可判定、too far”的问题。
- 🧪 **方法**：结合 AI agents、Z3 SMT 求解器、差分 fuzzer 和 194 个硬用例语料库，逐项验证正确性，而不是只靠启发式重写。
- 📊 **总成绩**：原版 0.2.54 通过 40/194，96 个错误/崩溃，43 个静默错误；复活版通过 190/194，0 个静默错误，4 个干净错误。
- 🔁 **P1 循环**：对局部效果使用 residual loop，并做一次符号迭代的健全性检查；涉及全局/外部状态的循环仍拒绝。
- 🧬 **P2 递归**：递归依赖未知值时改为 residual call，并检查效果；无法证明安全时拒绝。
- 🧩 **P3 控制流汇合**：修复多个静默误编译，支持未知值 switch、fall-through 和 residual try/catch。
- 🧠 **P4 路径条件**：用 Z3 做蕴含与可行性判断，并审计旧简化规则；审计发现 3,993 个失败报告，修复/删除 13 条不可靠规则，最终审计零失败。
- 📐 **P5 数值事实**：引入区间域和小范围分支拆分，解决抽象长度数组 push 等历史问题。
- 📦 **P6 内置函数与逃逸对象**：为 81 个内置函数建立声明式效果摘要，并实现“外部不动点”处理惰性缓存。
- 🌍 **P7 环境建模**：改为开放世界全局读取，生成 DOM/Node/Intl 模型，并支持带运行时守卫的 `--assume` 环境特化。
- 📉 **P8 输出体积**：用成本模型决定“写出计算结果”还是“保留计算代码”，语料库总输出缩小 40.5%，无案例超过输入 2 倍。
- ⚙️ **P9 生成器/异步**：初始化期间完成运行的生成器和已 settled Promise 可处理；结束时仍挂起的生成器被有意拒绝。
- 🏭 **真实库结果**：22 个真实库/应用 × 6 种配置共 132 次编译，0 个错误输出；18/22 至少一种配置可编译并匹配，4 个给出干净诊断。
- ⚛️ **React SSR 特化**：对已知应用、未知请求数据做特化；500/500 输出与 `renderToString` 字节一致，整页渲染约快 4–5.5×（JIT）和 9–10×（jitless），生成代码不再加载 React。
- ⚠️ **仍有限制**：循环/递归一般不可判定；大输入编译慢（如 `@babel/standalone` 约 279 秒）；UMD 可能因多模块系统探测导致输出翻倍；两个 React 形状仍会“构建成功但运行时抛错”；挂起生成器不近似处理。
- ✅ **适用场景**：最适合针对未知数据做特化、初始化很重且可受益于 V8 code cache 的 bundle；不建议替代 Node/V8 自身启动快照。
- 🔗 **交付物**：代码仓库暂为私有，包含语料库、设计笔记和站点；另有 Northstar Supply 在线演示展示 React 特化效果。

---

### [GitHub - facebookarchive/prepack：一个 JavaScript 打包优化器。· GitHub](https://github.com/facebookarchive/prepack)

**原文标题**: [GitHub - facebookarchive/prepack: A JavaScript bundle optimizer. · GitHub](https://github.com/facebookarchive/prepack)

Prepack 是 Facebook 的 JavaScript bundle 优化器/部分求值器，仓库已于 2022 年 2 月 12 日归档并转为只读；它通过重写 bundle 提升执行效率，适合初始化密集且解析可缓存的代码，并提供 CLI、插件生态、测试与开发流程。

- 🗄️ 仓库状态：facebookarchive/prepack 已归档为公共只读存档，归档日期为 2022-02-12。
- ⚙️ 核心功能：作为 JavaScript 部分求值器，重写 JavaScript bundle，使生成代码执行更高效。
- 🚀 适用场景：对初始化密集的代码效果最佳，尤其适合 JavaScript 解析可被有效缓存的环境。
- 📉 项目进展：Facebook Prepack 团队暂停 Prepack 及 React compiler 工作，相关 PR 更新减少。
- 💻 CLI 使用：可通过 npm 或 yarn 全局安装 prepack；使用 `prepack script.js`，或用 `--out` 输出到指定文件。
- 🔌 插件生态：存在 Rollup、Webpack、Parcel、VS Code、Babel Flow 等外部维护插件，问题需联系插件维护者。
- 🧪 测试与覆盖：提供 test262 状态及序列化测试覆盖率报告，可在 PR 的 checks/artifacts 中查看。
- 🛠️ 开发流程：克隆后初始化子模块，安装 yarn/node，使用 `yarn build/watch`、`yarn lint`、`yarn flow`、`yarn test`、`yarn validate`、`yarn repl`。
- 🌐 网站与许可：prepack.io 内容位于 `website` 目录，可本地启动；项目采用 BSD 许可并附专利授权。
- ⭐ 社区数据：约 14.1k stars、409 forks、192 issues、40 pull requests、1,596 commits。

---

### [Northstar Supply · Professional tools and shop supplies](https://jamesbox.exe.xyz/northstar/prepack/)

**原文标题**: [Northstar Supply · Professional tools and shop supplies](https://jamesbox.exe.xyz/northstar/prepack/)

该网站面向工坊提供工业用品与专业工具，覆盖测量、手动/电动工具、切割、安全防护等品类，并提供贸易采购、快速发货、保修和校准证书等服务。

- 🏭 面向工坊的工业用品供应：专业工具次日发货，涵盖测量仪器、手动与电动工具、切削工具及安全装备，均来自可靠品牌。
- 💼 提供团队贸易价，无最低订单；可全站选购商品或开通贸易账户。
- 🔨 本周特惠为 Oakhurst 无反弹锤：锻造并热处理，适合日常专业使用，工作面研磨、手柄舒适，享终身手动工具保修；现价 $46.95，原价 $62.99，优惠 25%，有货，截止 11 月 15 日周日。
- 🗂️ 商品分类齐全：测量与布局、手动工具、电动工具、切割与磨料、夹具与工件夹持、焊接与电子、电气测试、安全与 PPE，每类各 24 件产品。
- ⭐ 畅销品包括 Halvorsen 钢尺 $22.50、Meridian 精密螺丝刀套装 $39.99、Brightline 无刷锤钻 $240.95、Ironbark 钴钻头套装 $79.99 等。
- 🧰 更多畅销品包括 Brightline 快释杆夹 $19.50、Oakhurst 焊台 $282.95、Kestrel 钳形表 $100.99、Corvid 焊接头盔 $141.99（促销价）。
- 🚚 满 $150 免运费；下午 3 点前下单可当日发货。
- 🧾 提供 Net-30 贸易账户，支持发票账单和免税采购。
- 🛡️ 保修与认证：提供 2 年保修，手动工具享终身保修；所有测量仪器均附校准证书。

---

### [Yavashark：连续 950 天，我每天都在构建一个 JS 引擎 · Yavashark](https://yavashark.dev/blog/announcing-yavashark/)

**原文标题**: [Yavashark: I've Built A JS Engine Every Day For 950 Days Straight · Yavashark](https://yavashark.dev/blog/announcing-yavashark/)

Yavashark 是一个小型、可嵌入且易扩展的 JavaScript 引擎，作者自 2024 年 3 月 17 日起连续开发 950 天，目前由个人主导维护，已累计超过 4200 次提交，并通过约 82% 的 test262 测试套件。

- 🚀 项目定位：Yavashark 支持 Temporal、Intl，以及 TypeScript 和 React/TS，CLI 已可运行完整 react 与 react-dom 库。
- 🧪 测试进度：当前通过约 82% 的 test262，作者计划继续提升兼容性；Temporal 使用 Boa 的 temporal_rs，Intl 使用 icu4x。
- 🧩 扩展方式：可通过 Rust 宏将 Rust 函数和方法绑定到 JavaScript，便于为引擎添加自定义能力。
- ⚙️ 实验能力：支持 TCP、HTTP、文件系统、I/O 和早期定时器等实验性 API，但整体仍较初级。
- 🐢 性能现状：目前主要使用树遍历解释器，缺少隐藏类、内联缓存、NaN-boxing、高效对象布局和快速字节码，速度仍待优化。
- 🛠️ 路线图：计划引入并发移动式分代 GC、NaN-boxing 与优化对象格式、带内联缓存的新字节码等性能改进。
- 📊 原型表现：在 19 个微基准中，原型解释器平均比 V8 无 JIT 模式快约 3.5 倍，并在部分异常和生成器场景中优于开启 JIT 的 V8，但集成后仍可能有性能折损。
- 🌍 作者经历：作者已以 Invited Expert 身份加入 Ecma TC39，年龄不到 20 岁，可能是 TC39 中最年轻的成员之一。
- ⭐ 社区支持：作者希望读者为引擎仓库点 Star，并可通过 GitHub Sponsors 支持项目及其大学费用。

---

### [Yavashark](https://yavashark.dev/)

**原文标题**: [Yavashark](https://yavashark.dev/)

Yavashark 是一个实验性 JavaScript 引擎，提供可运行 JS 代码的 Playground，并展示控制台输出、缩放/时间范围控制以及多种运行结果状态。

- 🧪 Yavashark 定位为实验性 JS 引擎。
- 💻 示例代码包含 `console.log("Hello from Yavashark!")`，用于输出问候信息。
- 🔁 示例还定义了递归斐波那契函数 `fib(n)`，并调用 `fib(20)`。
- ▶️ 页面提供“Run”运行按钮，并提示可用 `Ctrl + Enter` 快捷运行。
- 🖥️ 包含 Console 控制台区域，用于查看执行输出。
- 📊 提供 Scale 缩放控制，可拖动缩放、双击重置缩放，并显示 count 和百分比。
- ⏱️ 时间范围可选 `3m`、`1y`、`all`。
- ✅ 结果状态包括 passed、failed、not implemented、parse error、timeout、crashed、skipped、runner error。

---

### [V8 中的隐藏类：为什么对象形状会影响速度 · Bitlyst](https://bitlyst.blog/p/v8-hidden-classes-inline-cache)

**原文标题**: [Hidden Classes in V8: Why Object Shape Changes Speed · Bitlyst](https://bitlyst.blog/p/v8-hidden-classes-inline-cache)

尚未提供需要总结的文章正文，因此无法提炼关键信息；请补充内容后，我将生成简洁的中文要点列表。

- 📄 当前输入为空，缺少可总结的文本。
- ✍️ 请粘贴文章内容，我会按要求整理关键要点。

---

### [ReactiveScript：初步发现 - YouTube](https://www.youtube.com/watch?v=J3PGI4yqta4)

**原文标题**: [ReactiveScript: Early Findings - YouTube](https://www.youtube.com/watch?v=J3PGI4yqta4)

该文本是 YouTube 页面底部的导航与法律信息，涵盖平台介绍、联系与商业入口、开发者与创作者资源、条款政策及版权声明。

- ℹ️ 提供“关于”“新闻”“版权”等平台信息入口。
- 📞 包含“联系我们”以及广告、创作者、开发者等合作与资源链接。
- 🛠️ 提供“测试新功能”和“YouTube 运作方式”等说明入口。
- 📜 列出服务条款、隐私政策及政策与安全相关链接。
- ©️ 版权声明为 © 2026 Google LLC。

---

### [GitHub - solidjs/reactivescript：响应式作为一种语言 ·](https://github.com/solidjs/reactivescript)

**原文标题**: [GitHub - solidjs/reactivescript: Reactivity as a Language · GitHub](https://github.com/solidjs/reactivescript)

ReactiveScript 是一个实验性的响应式 UI 小语言，将 Solid 2.0 的响应式语义提升为语言语义，并在代码运行前进行静态检查；`.rx` 文件会编译为普通 Solid 2.0，运行时除 Solid 本身外不增加额外机制。项目当前为 0.1 实验版，随 Solid 2.0 RC 演进，规范和编译器可能频繁变化。

- 🧪 目标：像 Rust 拒绝借用错误一样，让写入非 source、计算中写入、异步缺少 loading/error 边界、owner 泄漏等“形状错误”在编译期被拒绝。
- 🧠 适合 AI 编写：规则少且明确，检查器错误会指出违反的规则和常见修复方式；示例中 AI 仅凭规范冷启动编写应用并预测 70/71 帧行为。
- ✍️ 核心语法：`source` 是唯一可写状态，用 `:=` 写入；方程 `y = x * 2` 始终成立并随依赖重算；写入仅发生在事件处理器或 action 的命令式作用域。
- ⏳ 异步规则：`await` 写在方程中，编译器跟踪 pending 与失败，要求用 loading/errored boundary 明确两种情况；缺少 errored 边界会编译失败。
- 🧱 语言能力：结构化 stores 与按路径写入、乐观更新/加载中保留旧值、模块私有状态并导出 action、流式 SSR 与 hydration、server fn、scoped `<style>`、通过 TSX 投影交给 TypeScript 检查类型。
- 📁 仓库组成：`spec/` 编号规则，`scenarios/` 约 100 个可执行案例，`examples/` 真实 `.rx` 应用，`ref/` TypeScript 参考实现，`compiler/` Rust 生产编译器 `rxc`，`runtime/` 运行时薄层，`tooling/` 语言服务器与 VS Code 扩展。
- ⚙️ Vite 集成：安装 Solid 2.0 next、`@reactivescript/runtime`、`@reactivescript/compiler`；保留 `solid()` 插件，Solid Vite 插件可自动发现并编译 `.rx`。
- 🧑‍💻 编辑器与 CI：VS Code 扩展提供高亮和语言服务器；其他编辑器可运行 `npx @reactivescript/language-server --stdio`；CI 用 `rx-tsc --noEmit` 做类型与检查器错误检查。
- 🚀 快速试用：需要 Node 22+，克隆仓库后可直接运行 `node --experimental-strip-types ref/check.ts examples/todo.rx` 检查程序，或 `ref/run.ts` 跑所有场景；完整 Solid oracle 需构建 Solid next。
- 📖 规范阅读顺序：00 词汇、01 作用域、02 核心，再读 07 表面语法和 08 约束；所有行为主张都对应编号规则或场景，诊断保留 Solid 代码并分类。
- 📜 许可与纪律：MIT；坚持“核心先于 holds”、规则与场景而非散文、唯一语法，Solid 基础规则以上游为准并记录 `DV-n` 分歧。

---

### [ReactiveScript 探索之旅 - DEV 社区](https://dev.to/playfulprogramming/the-quest-for-reactivescript-3ka3)

**原文标题**: [The Quest for ReactiveScript - DEV Community](https://dev.to/playfulprogramming/the-quest-for-reactivescript-3ka3)

overview summary
本文是 Ryan Carniato 于 2021 年对“把细粒度响应式作为通用语言”的探索。他回顾了 Destiny Operator、编译糖、关键字/标签、函数装饰等方案，分析其在组合性、引用传递和语义表达上的局限，并提出让表达式默认响应式、用副作用操作符标记命令式逃逸的 ReactiveScript 构想。

- 🧠 作者受 Jay Phelps 启发，思考响应式不应只服务于框架 DSL，而可能成为通用编程语言特性。
- ➡️ “Destiny Operator” `<=` 用声明式等式表达响应式关系，例如 `b <= a + 1`，强调响应式声明不同于普通赋值。
- 🧩 现有 JS 细粒度响应式通常需要 getter/setter 或 `value()`，并形成“响应式状态、派生值、副作用”三部分 API。
- 💡 文章比较了多种语法方案：标识符加 `$` 编译糖、关键字/装饰器/标签、Svelte 的 `$:`、Vue 的 `$ref` 和 Marko 的标签式写法。
- ⚠️ Svelte 的 `$:` 接近 Destiny Operator，但难以把响应式信号本身导出模块，组合性依赖 Stores 等辅助系统。
- 🔁 Marko 标签和 Vue Ref Sugar 恢复了较多组合能力，但当响应式值离开局部作用域时，仍需 `$$()` 等额外语法处理引用传递。
- 🔍 核心难题是：如何保留响应性、区分按引用与按值传递，并避免普通函数无法理解响应式语义。
- 🔄 作者反转思路：让表达式默认响应式，只显式标记副作用/命令式逃逸，并尽量保留 JavaScript 语法与工具链优势。
- 🛠️ ReactiveScript 示例中，`$:` 标记副作用，函数参数可被包装为函数，局部变量按函数调用处理，派生值用 `const` 且惰性求值。
- 🌿 条件分支也可被编译为响应式重跑；组件可在最小细粒度更新下工作，但循环、数组映射和性能分析仍需进一步设计。
- 🚀 作者认为该方向便于编译期分析，未来可能用于部分水合等场景，但目前仍是开放构想。
- 💬 评论区补充讨论了 Svelte Stores 的可组合性、双向 Destiny Operator、Vue `$$()` 的适用场景，以及纯 JavaScript 运行时响应式方案。

---

### [EmbedPDF — 开源 PDF 解决方案](https://www.embedpdf.com/)

**原文标题**: [EmbedPDF — Open Source PDF Solutions](https://www.embedpdf.com/)

EmbedPDF 是一个面向 JavaScript 的开源 PDF 查看器，主打“无需痛苦地嵌入 PDF”，提供可直接使用的现成组件和可深度定制的无头库两种集成方式，支持 React、Angular、Vue、Svelte 与原生 JS，并以 Apache-2.0 协议开源。

- 📄 提供生产级 PDF 查看器组件，几分钟内即可嵌入应用，内置工具栏和布局。
- 🧩 同时提供无头组件方案，适合从零构建自定义 UI，强调可组合性与插件友好。
- ⚙️ 支持 React、Angular、Vue、Svelte 和 Vanilla JS，可适配现有技术栈。
- ✍️ 覆盖注释、高亮、下划线、绘图、笔记等文档协作功能。
- 📝 支持填写和保存交互式 PDF 表单，以及添加、保存和管理电子签名。
- 🔍 支持全文搜索、敏感内容永久涂黑、文档印章等现代 PDF 工作流能力。
- 🚀 快速开始只需复制少量代码，通过 CDN 即可初始化，无需构建步骤。
- 🌍 项目采用 Apache-2.0 开源协议，强调透明、安全、可靠，适合生产环境。
- 📈 拥有 4K+ GitHub Stars、1M+ npm 月下载量，并是 PDF Association 成员。
- 💬 获得法律软件 Align、PDF 工具 Stirling PDF、AI 引用工具 Grella 等开发者好评，尤其认可其性能、模块化插件架构和 Svelte 支持。

---

### [发布 Release v3.0.0 · embedpdf/embed-pdf-view](https://github.com/embedpdf/embed-pdf-viewer/releases/tag/v3.0.0)

**原文标题**: [Release Release v3.0.0 · embedpdf/embed-pdf-viewer · GitHub](https://github.com/embedpdf/embed-pdf-viewer/releases/tag/v3.0.0)

overview summary
EmbedPDF 3.0 是从 PDF 引擎层重建的重大版本，提供开箱即用查看器、Headless 组件和底层 Engine 三种使用方式，并带来全新包名、完整功能集、2.x 迁移指南及 CloudPDF 相关发布。

- 🚀 EmbedPDF 3.0 从 PDF 引擎底层重建，核心能力全面升级。
- 🧩 提供三种用法：一体化 Viewer、Headless 组件、EmbedPDF Engine。
- 🌐 Viewer 支持 HTML、React、Vue、Svelte、Angular，可用一个标签和少量配置接入。
- 🛠️ Headless 组件允许基于同一套插件自行构建查看器 UI，并提供主流框架绑定。
- ⚙️ Engine 可在浏览器通过 WebAssembly 运行，也可在 Node 中使用 macOS、Linux、Windows 原生构建。
- ✨ Viewer 默认开启全部功能且可逐项关闭，包括注释、表单与签名、涂黑、测量、页面编辑、搜索、打印和多标签阅读等。
- 📦 安装方式为 `npm install @embedpdf/viewer`，也支持 CDN；框架另有 `@embedpdf/viewer-react`、`-vue`、`-svelte`、`-angular` 包。
- 🔁 2.x 的查看器包名被 3.0 新包替代，官方提供逐项迁移指南；2.x 文档保留在 v2.embedpdf.com，修复通过 `v2-latest` 发布。
- ☁️ CloudPDF 发布 `@cloudpdf` 系列包，包括同款查看器、服务器 `@cloudpdf/server`（含镜像与 Helm chart）及 API SDK。
- 🧱 3.0.0 覆盖 Viewer、框架绑定、插件、Core、Engine 等大量包；多数包为 3.0.0，三个字体与印章包为 1.0.0。
- 🙌 官方感谢参与 `next` 版本测试并反馈问题的用户。

---

### [实时 PDF 查看器演示 — EmbedPDF](https://www.embedpdf.com/demo)

**原文标题**: [Live PDF Viewer Demo — EmbedPDF](https://www.embedpdf.com/demo)

这是一个关于 EmbedPDF 查看器在线演示的简短提示，当前页面正在加载查看器。

- 🖥️ 展示 EmbedPDF 查看器的实时演示
- ⏳ 页面显示“正在加载查看器…”状态
- ℹ️ 内容较少，未提供更多功能或操作说明

---

### [编辑器 AI SDK 游乐场 | Thinkfree Developers](https://playground.developers.thinkfree.com/playground/editor-ai-sdk/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=sdklaunch2026&utm_content=261110)

**原文标题**: [Editor AI SDK Playground | Thinkfree Developers](https://playground.developers.thinkfree.com/playground/editor-ai-sdk/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=sdklaunch2026&utm_content=261110)

您未提供需要总结的文章正文，因此暂时无法生成内容摘要。

- ❓ 当前输入中“Use the following content:”后为空，没有可提炼的文本。
- 📝 请补充或粘贴需要总结的文章内容。
- ✅ 收到内容后，我会用中文提供概述，并以“-”符号和合适的表情符号列出关键要点。

---

### [GitHub - paulirish/chrome-capture：从 Chrome 以 60-120fps / 2160p 捕获标签页视频/音频 · GitHub](https://github.com/paulirish/chrome-capture)

**原文标题**: [GitHub - paulirish/chrome-capture: 60-120fps / 2160p tab video/audio capture from Chrome · GitHub](https://github.com/paulirish/chrome-capture)

chrome-capture 是一个基于 Chrome 新版原生录屏能力的开源工具，可直接把标签页以 60–120fps、最高 2160p 录制成 AV1 编码的 MP4，并支持标签页音频，无需 ffmpeg。它封装了 Chrome 153+ 的 `Page.startScreenRecording`，相比旧方案在速度、文件体积和录制体验上都有明显提升。

- 🎥 支持 60–120fps、最高 2160p 的标签页视频与音频录制，输出 AV1 `.mp4`，无需 ffmpeg。
- ⚡ 基于 Chrome 153+ 原生 `Page.startScreenRecording`，视频帧从合成器经共享内存直达独立编码器，边录边写入 MP4。
- ⏹️ 停止录制几乎即时完成，无需像 ffmpeg 方案那样等待数秒收尾；可随时开始/停止，适合只录关键交互。
- 🧩 Puppeteer v25.10+ 已提供实验性 `page.record()` 并弃用 `page.screencast()`；Playwright 仍使用旧 `Page.startScreencast`，预计后续跟进。
- 💻 CLI 用法简单：`npx chrome-capture <url> <output.mp4> <duration>`；默认录制音频，≤60fps 时无头运行，macOS 上 >60fps 自动切换有头模式以利用 ProMotion 120Hz。
- 🛠️ `startRecording()` 支持 Playwright Page、Puppeteer Page 或原始 CDP 会话，默认 60fps，可配置输出路径、分辨率、录制区域和音频。
- 🧪 提供 `@playwright/test` fixture，可自动录制每个测试并附加 MP4 到报告。
- 🖱️ 可通过 Playwright `showActions()` 或自定义 DOM 覆盖层把光标、点击徽章等录进视频。
- 📊 M4 Max 基准测试中，6.4 秒 UI 回放：旧方案 25fps、总耗时 21s、停止耗时 3800ms、WebSocket 流量 10.5MB；新方案 60fps、总耗时 11s、停止耗时 17ms、流量 450KB。
- 📦 新方案文件更小、画质略优：示例中最终文件 330KB vs 480KB，PSNR 34dB vs 32dB，并支持可选音频。
- 🎚️ 暂无码率/CRF 参数；Chrome 使用 libaom AV1 实时 1-pass VBR，码率随像素率线性增长，如 720p30 约 2Mbps、1080p60 约 9Mbps、2160p120 约 72Mbps。
- 🚀 压力测试显示：Mac 无头可达 2160p60；120Hz ProMotion 有头可达 1080p120 和 2160p120；无 GPU 的 Linux CI 可达 1080p60/1440p60，解除 vsync 限制可到 1080p75–83fps。
- ⚠️ macOS GPU 加速环境不要同时启用 `--disable-frame-rate-limit --disable-gpu-vsync`，否则 rAF 过快会拖垮采集。
- ⭐ 仓库约 232 stars、4 forks，采用 Apache-2.0 许可证；实现较小，也可直接参考 `src/index.ts` 集成。

---

### [Text.js | 控制台框架](https://textjs.org/)

**原文标题**: [Text.js | The Console Framework](https://textjs.org/)

Text.js 是一个把全栈 React 应用直接渲染到浏览器控制台 `console.log` 中的框架，提供 React 组件、App Router 路由、服务端渲染、终端与 AI 代理运行能力，以及完整的开发工具链，让控制台变成可交互的应用界面。

- 🚀 通过 `bunx create-text-app` 快速创建项目，使用 `AsciiFont`、`Box`、`Text`、`useInput` 等组件构建控制台界面。
- 🧭 采用 App Router：`app/` 中的文件夹自动成为路由和布局，支持前进、后退与深链接，并适配 DevTools 面板尺寸。
- ⌨️ 统一处理键盘输入、粘贴和 IME 组合输入，通过隐藏的 `<textarea>` 将事件传递给应用。
- 🧱 提供布局、数据展示、图表、表单控件和键盘交互组件，如 Grid、Table、LineChart、Input、Dialog、CommandPalette 等。
- ⚙️ 渲染管线包括 React 自定义 reconciler、Yoga 布局、CellBuffer 绘制、脏行检测、RLE 编码和 `console.log` 输出。
- 📉 只有发生变化的帧才会产生一次 `console.log`；未变化帧为 0 次调用，并采用追加帧而非清空控制台，减少闪烁。
- ⚡ 性能示例：3,200 个单元格编码为 149 个 `%c` span；单行编辑约 0.011ms，完整重绘约 0.163ms，空闲帧 0 次调用。
- 🖥️ 支持 `runtime = "server"` 服务端渲染，浏览器只加载约 21kB gzip 的帧播放器，并通过 SSE 接收行增量。
- 🧩 支持 Partial Prerendering、中间件、缓存与 stale-while-revalidate，以及 static、bun、vercel、cloudflare 等部署适配器。
- 💻 同一套应用还可在终端中以真彩色 ANSI 运行，或通过 MCP 供编码代理导航路由、按键并读取文本帧。
- 🛠️ 配套 DevTools 扩展、VS Code 预览、ESLint 插件、测试工具、错误码文档和 `window.text` 控制台 REPL。
- 🌍 支持 Unicode 双向文本算法与 FIGlet 字体解析，并提供 10 章、约 65 分钟的控制台部署仪表盘课程。

---

### [GitHub - anomalyco/textjs：一个用于在浏览器控制台中渲染应用的 React 框架。 · GitHub](https://github.com/anomalyco/textjs)

**原文标题**: [GitHub - anomalyco/textjs: A React framework for apps that render in the browser console. · GitHub](https://github.com/anomalyco/textjs)

Text.js（anomalyco/textjs）是一个让 React 应用直接渲染到浏览器控制台的框架；该仓库采用 MIT 许可证，约有 185 stars、6 forks，累计 1010 次提交。它通过 Yoga 布局、`%c` 样式分段和单次 `console.log` 输出帧，未发生变化的帧不会输出。

- 🚀 项目定位：用于构建在浏览器控制台中运行的 React 应用，提供文档、教程和 Playground。
- ⚡ 快速开始：使用 `bunx create-text-app@latest` 创建项目，进入目录后安装依赖并运行 `bun dev`，然后打开浏览器控制台。
- 🖥️ 环境要求：需要 Bun 1.2+ 或 Node.js 22+，以及桌面版 Chrome、Edge、Firefox 或 Safari。
- 🧩 示例能力：示例使用 `useState`、`useInput`、`Box`、`Text` 构建控制台交互界面，支持用上下键增减计数。
- 📦 核心包：包括 `@textjs/app`、`@textjs/react`、`@textjs/core`、`@textjs/font`、`@textjs/opencode`、`create-text-app` 和 `eslint-plugin-textjs`。
- 🛠️ 扩展工具：提供 VS Code 扩展（实时预览、路由脚手架、错误链接）和 Chrome DevTools 扩展（组件树、帧检查器、时间线）。
- 👩‍💻 开发命令：使用 `bun install`、`bun test packages/`、`bun run typecheck` 和 `bun run --cwd apps/web dev`，站点运行在 `localhost:3000`。
- 🤝 贡献与许可：欢迎提交 Bug 报告和 Pull Request，需先阅读 `CONTRIBUTING.md`；安全问题按 `SECURITY.md` 报告，项目采用 MIT 许可证。

---

### [Jeasx 有哪些新功能？ » Jeasx - 轻松使用 JSX](https://www.jeasx.dev/news)

**原文标题**: [What's new in Jeasx? » Jeasx - JSX with Ease](https://www.jeasx.dev/news)

Jeasx 发布日志汇总：最新 3.0.0 是以流式渲染为核心的重大升级，带来约 2 倍渲染性能提升，同时引入多项破坏性变更与安全加固；后续版本持续升级 Fastify 与 jsx-async-runtime、修复安全漏洞，并围绕路由、静态文件、构建配置和核心精简进行迭代。

- 🚀 2026-11-02 Jeasx 3.0.0 发布：JSX 响应改为流式发送，浏览器在页面仍在渲染时即可收到首字节；基于 jsx-async-runtime@3，渲染约快 2 倍。
- ⚠️ 3.0.0 迁移重点：用 `html("...")` 替代 `{{ html: "..." }}`；`class`/`style` 改传字符串；`this.errorHandler` 迁移到 `jeasx.config.js` 的 `setErrorHandler`；`responseHandler` 若修改 HTML 需先读取 `ReadableStream`。
- 🧩 jsx-async-runtime@3 破坏性变更：原始 HTML 只能通过 `html()` 输出；不能关闭转义；`children` 行为更接近 React；生成器子节点只能渲染一次；`jsxToString` 可同步返回。
- ✨ jsx-async-runtime@3 新能力：`jsxToStream` 输出 `ReadableStream`；支持 Promise、可迭代/异步可迭代对象、字节、`Date`/`URL`/`Error` 等子节点；支持 Promise 属性和 render props；类型更完善。
- 🔒 3.0.0 安全：修复开发环境编译路由及 sourcemap 暴露问题；特殊路由名不可直接请求；拒绝畸形路径并返回 400；路由/文件查找忽略原型链属性；减少文件句柄泄漏。
- 🛠️ 3.0.0 其他修复：开发服务器等待首次构建；`dist` 优先于 `public`；修复 Windows/特殊字符路径；静态文件仅响应 GET/HEAD；构建前清理 `dist`。
- ⚙️ 3.0.0 新特性：`jeasx.config.js` 中 esbuild/Fastify 配置和 `FASTIFY_SERVER` 可异步；生产构建包含 dotfiles；支持 SIGINT/SIGTERM 优雅关闭。
- 🔄 2026-10-23 Jeasx 2.10.7：路由和守卫可返回 Web `Response` 或 `ReadableStream`；修复静态文件句柄泄漏；修复通过字面路径请求守卫文件绕过守卫的安全问题。
- 🚀 2026-09-04 Jeasx 2.10.3：`generateRoutes` 改用生成器，降低内存和计算开销；修复 Fastify 四项安全漏洞。
- 🧱 2026-08-04 Jeasx 2.10.0：移除核心 `BUILD_TIME`，改用 esbuild `define`；移除向浏览器自动注入 `BROWSER_PUBLIC_` 环境变量。
- 📦 2026-07-17 Jeasx 2.9.0：移除 `@fastify/formbody`、`@fastify/cookie`、`@fastify/multipart` 核心依赖，改为按需安装和配置。
- 📁 2026-07-07 Jeasx 2.8.1：守卫中可通过 `reply.file` 访问静态文件 metadata，便于鉴权、修改响应头和替换内容。
- 🔀 2026-07-03 Jeasx 2.8.0：统一静态资源与动态路由处理，所有文件由路由处理器处理，支持守卫控制静态资源；`@fastify/static` 迁移为 `@fastify/send`。
- 🧭 2026-06-02 Jeasx 2.7.0：用 `jeasx.config.js` 取代 `.env.js`，集中配置 esbuild 与 Fastify，并停止支持 `.env.js`。
- 🛡️ 2026-06-07/2026-06-21 2.7.1/2.7.4：利用 esbuild metadata 生成静态路由元数据，提升冷启动和路径遍历防护；启动时预计算模块路径。
- 📦 2026-05-08 Jeasx 2.6.0：`dist` 目录不再强制 browser/server 分离，服务器路由也可使用 esbuild loader；不再默认 external 常见资源扩展，也不再默认设置 target。
- 🧩 2026-04-01/2.4.1：守卫返回对象可作为路由额外 props，多个守卫按距离路由最近者覆盖同名 prop。
- 📝 2026-02-20 Jeasx 2.4.0：移除核心 MDX 支持，新增 `ESBUILD_SERVER_OPTIONS`/`ESBUILD_BROWSER_OPTIONS` 和 `FASTIFY_SERVER` 自定义能力，配置改为函数形式。
- 📝 2026-01-30 Jeasx 2.3.0：新增 MDX 支持，可直接用 `.mdx` 路由并在 Markdown 中嵌入 JSX；配置改为从 `.env.js` 直接导入。
- 🏷️ 2026-01-17 Jeasx 2.2.2：直接访问 404 页面时保留原始状态码（默认 200），便于静态导出；如需旧行为可在 `/[404]` 中手动设置 404。
- 🔐 其他版本：2.10.6、2.10.5、2.10.2、2.5.1 等多为 Fastify/@fastify/static 安全更新和依赖维护，建议保持升级。

---

### [示例中 Jeasx 的强大之处 » Jeasx - 轻松使用 JSX](https://expo.jeasx.dev/)

**原文标题**: [The power of Jeasx in examples » Jeasx - JSX with Ease](https://expo.jeasx.dev/)

Jeasx 是一个面向服务端渲染 Web 的轻量框架，以异步 JSX 作为直观模板语言，强调 HTML 优先、少魔法、小核心，并提供 55 个可运行示例，适合构建动态网站、无客户端 JavaScript 应用、HTMX 超媒体、流式页面及多内容类型路由。

- 🧩 核心主张：异步 JSX + 基于文件的路由，保持框架核心很小，其他能力通过用户自有代码集成。
- 🚀 提供 55 个示例，100% HTML 优先、0 魔法，可在 jeasx.dev 浏览，GitHub 克隆后本地运行并可自由修改。
- 🌐 动态网站：支持远程 API、JSON 数据、Markdown/MDX 渲染页面，如博客、产品页、MDX 支持。
- 📝 无客户端 JS 应用：用普通 HTML 表单构建交互应用，服务端处理逻辑，视图过渡提升体验。
- ⚡ HTMX 超媒体：路由可返回 HTML 片段，支持点击编辑、主动搜索、模板片段、无限滚动、Fixi.js 等。
- 🏝️ 客户端 JS 岛屿：可集成 Alpine.js、ArrowJS、Lit、Preact、React、Svelte、Vue 等现有库。
- 📡 流式与 SSE：支持 HTML 流、并行加载、乱序流、异步迭代、ReadableStream、Server-Sent Events 和聊天示例。
- 🖼️ 多内容类型：路由可返回图片、SVG、JSON、XML、Open Graph 图片等，并支持内容协商和 Response 对象。
- 🧱 JSX 渲染能力：涵盖组件组合、请求上下文、head 管理、JSX 拦截、国际化、声明式 Shadow DOM、客户端 JSX 和单元测试。
- 🔐 认证与安全：支持基础认证、登录会话、签名 Cookie、内容安全策略和 Cap 验证码。
- 🛠️ 错误处理与后处理：可捕获错误，并在发送浏览器前美化 HTML、提取样式等。

---

### [发布 v1.3.0 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.3.0)

**原文标题**: [Release v1.3.0 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.3.0)

overview summary
Rolldown v1.3.0 是一次小版本发布，新增实验性 import attributes、面向 AI/CI 的构建报告和 @rolldown/perf-kit，同时包含若干破坏性变更与重要修复；Vite 用户暂不应强制覆盖 Rolldown 版本。

- ⚠️ 这是小版本发布，但部分默认行为相比 1.2.16 有变化，升级前应先阅读破坏性变更说明。
- 🧩 新增实验性 import attributes 支持：`with { ... }` 会让同一文件的不同属性成为不同模块，`json`、`text`、`bytes` 无需插件即可工作；插件可在 `resolveId`、`load`、`transform` 中读取属性，并可在 `resolveId` 中修改。
- 🛑 Vite 用户注意：不要通过 `overrides` 或 `resolutions` 强制使用 `rolldown@1.3.0`；Vite 8.3.6 及更早版本需要改动才能兼容，应等待支持 Rolldown 1.3 的 Vite 版本。
- 🤖 新增实验性 agent-friendly 构建报告：配置 `devtools: { mode: 'report' }` 后，会在 `node_modules/.rolldown/report/` 输出 Markdown 和 JSON，涵盖耗时、chunks、modules、packages、依赖图、变更对比和原始指标数据。
- 📊 新增实验性包 `@rolldown/perf-kit`，可消费构建报告并测量页面 LCP/FCP、Node.js/Deno 服务就绪时间、Cloudflare Worker 全局作用域执行时间，帮助代理或开发者优化性能。
- 💥 破坏性变更：`preserveModules` 文件名现在遵循 Rollup，`[name]` 会保留非 JS 扩展名，例如 `data.json` 变为 `data.json.js`，依赖旧导出路径的库需更新。
- 💥 破坏性变更：CLI 的 `--input` 不能再与位置参数同时使用，应改用 `rolldown 1.js 2.js` 或多次传入 `--input`。
- 🩹 重要修复：外部导入现在能正确保留 import attributes，避免不同 attributes 的同一外部模块被错误合并；旧式 `assert` 关键字输出会转换为 `with` 并产生弃用警告。
- 🐛 其他修复覆盖 tree-shaking、CommonJS、watch、dev/lazy、sourcemap、JSON、插件队列和错误诊断等；同时包含性能优化、文档与测试更新。
- ❤️ 本次发布包含多位新贡献者的首次贡献，并感谢社区反馈与参与。

---

### [发布 v31.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v31.0.0)

**原文标题**: [Release v31.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v31.0.0)

jsdom v31.0.0 发布，包含多项破坏性变更，重点涉及 Canvas 后端迁移、CSS 解析与计算样式的新实现、HTML/XML 解析对阻塞脚本的处理，以及大量 DOM、资源加载、焦点和内存泄漏修复。

- 🚀 发布 v31.0.0，自上一版本以来有 7 个提交合入 main。
- 🎨 Canvas 与图像解码后端由 `canvas` 改为 `@napi-rs/canvas`，需安装 v1.0.13+；新后端提供预编译 Skia 二进制，渲染和编码字节可能不同。
- 🖼️ 新增 WebP 序列化，修复图片加载等待解码、丢弃过期请求、尺寸变化重复请求、失败图片绘制旧内容等问题。
- 🧩 CSS 解析、选择器匹配和计算样式改用新集成实现，支持级联层、嵌套、`@scope`、自定义属性、`@property`、`attr()`、`if()`、Shadow DOM 样式和可构造样式表，查询与重复样式读取更快。
- ⚙️ 修复大量 CSS 级联、简写、序列化和默认样式问题；计算声明会随 DOM/样式表变化实时更新，但序列化和计算值可能与旧版不同。
- ⏸️ HTML/XML 解析会在阻塞脚本所需资源就绪前暂停；`JSDOM`、`fromURL()`、`fromFile()` 可能返回部分解析文档，需等待 `DOMContentLoaded` 或 window 的 `load` 事件，并先检查 `readyState`。
- 🧾 异步解析恢复后遇到的 XML 语法错误会通过虚拟控制台以 `"xml-parsing"` 报告。
- 🆕 新增 `window.reportError()`、`element.ariaBrailleLabel` 和 `element.ariaBrailleRoleDescription`。
- 🔔 页面完成时的 `load` 事件仅在 window 触发，应使用 `window.addEventListener("load")` 或 `window.onload`，而非监听 document。
- 📝 修复 `document.open()` 和 `document.write()` 的事件清理、连续写入、嵌套脚本插入点、脚本创建输入流保持打开至 `document.close()` 等行为。
- 🧷 修复动态插入脚本对 `script.async = false` 执行顺序、准备时源文本/文档、跨文档收养后执行、惰性片段脚本执行等问题。
- 🚦 修复脚本阻塞无关图片/样式/框架、嵌套样式导入完成事件、循环导入、Shadow DOM 中 `<style>` 的 `load` 事件。
- 🛑 修复 `window.stop()` 取消子框架子资源和 XHR、抑制取消加载完成事件并允许后续请求；修复重复 `document.close()` 重放事件及 iframe `load` 事件。
- 🧠 修复请求拦截器 Promise 持有已关闭窗口导致的内存泄漏（v28.0.0 引入）。
- 🎯 修复焦点管理：元素变为不可聚焦后焦点异步移至视口，`blur()` 可立即释放；修复 `document.hasFocus()` 在聚焦前、切换中及框架内返回 false。
- 📄 修复 XML 文档中 `<template>` 解析与 `template.innerHTML` 序列化，包括带命名空间前缀的模板。
- 🧮 修复 `rect.toJSON()` 和 `performance.toJSON()` 在方法所属 realm 创建结果对象，而非宿主 Node.js realm。
- 👥 贡献者包括 Brooooooklyn、b84330808 等 4 人；发布包含 2 个资产。

---

### [发布 Remix v3.2.0 · remix-run/remix · GitHub](https://github.com/remix-run/remix/releases/tag/remix%403.2.0)

**原文标题**: [Release remix v3.2.0 · remix-run/remix · GitHub](https://github.com/remix-run/remix/releases/tag/remix%403.2.0)

Remix v3.2.0 是一次包含新功能与多项修复的版本更新，重点引入基于 nonce 的 CSP 中间件，并改进组件渲染、样式序列化、测试工具、文件/会话存储可靠性及 CLI 默认配置。

- 🔒 新增 `remix/middleware/csp` 的 `csp()` 中间件，为每个请求生成 nonce 和匹配策略，自动应用到 import map、模块预加载和 `css()` 样式，支持 report-only 与上报端点。
- 📦 新增 `package.json` 导出：`remix/headers/content-security-policy` 和 `remix/middleware/csp`，分别转发 `@remix-run/headers/content-security-policy` 与 `@remix-run/csp-middleware` API。
- 🧪 `remix/test` 的 mock/方法 spy 支持 `mockImplementation()`、`mockImplementationOnce()`、`resetCalls()`、`callCount()`、`restore()`，且 `t.mock` 在测试或清理失败时也会恢复。
- 🛠️ `remix new` 创建的应用现在生产环境会指纹化资源、关闭时关闭资源服务器，并在 Windows 命令 shell 中运行 `package.json` 脚本。
- ⚡ HMR 中添加/移除 `clientEntry` 会重启应用服务器，避免新响应使用过期的 hydration 边界；`clientEntry` props 的 hydration 更可靠。
- 🧩 `remix/component` 修复 JSX/`createElement()` 渲染限制、无效 mix prop、`$rmx` 数据传递，以及布尔 `aria-*`/`data-*`、Frame HTML 解析等客户端导航/渲染问题。
- 🎨 `css()` 与 `style` prop 的序列化更符合浏览器预期，`css()` 重渲染约快一倍；但数字单位、CSS 自定义属性大小写、厂商前缀和 `rmxc-*` 类名等输出有变化，需要更新测试/选择器。
- 📉 `remix/component` 浏览器运行时缩小约 10%；未使用 `<Frame>` 的应用不再加载 frame runtime，组件 JS 约减半。
- 🗂️ 修复 `remix/file-storage/fs` 上传流失败损坏已有文件，以及 `remix/session-storage/fs` 并发保存同一 session 损坏文件的问题。
- 📚 随 `remix` 安装的指南改为独立章节，完善 Files and Assets 与 Rendering UI 内容，并更新文档链接。
- 🐛 修复 `remix/test` 浏览器测试动态导入语法错误和 WebKit 进度超时卡住问题，并升级多项 `@remix-run/*` 依赖。

---

### [下一代开源 Wiki — Wiki.js](https://js.wiki/)

**原文标题**: [Next Generation Open Source Wiki â Wiki.js](https://js.wiki/)

Wiki.js 3.0 是新一代开源 Wiki 平台，面向从个人项目到数千名贡献者的团队，强调自托管、速度、可扩展性与完全可控；基于 Node.js + PostgreSQL，支持多平台部署，并采用 AGPL 免费开源许可。

- 🚀 **版本与定位**：Wiki.js 3.0 现已发布，定位为可规模化的自托管开源 Wiki，可从周末项目扩展到数千名贡献者。
- ✍️ **创作能力**：内置 Markdown 编辑器，支持实时分屏预览、代码高亮、表格、数学公式、Mermaid/PlantUML 图表，并提供可视化、AsciiDoc、Excalidraw 等编辑器。
- 🤝 **实时协作**：支持 Live Notes 多人同时编辑、评论与段落批注、只读用户提案审批、页面关注、提及通知和 Webhook 集成。
- 🗂️ **组织管理**：提供统一文件管理器管理页面与附件，内置 PostgreSQL 全文搜索，支持多站点、单页多语言、Git 双向同步及云存储备份。
- 🔐 **治理与权限**：支持 OIDC、LDAP、SAML、本地认证，按站点/路径/语言/用户组精细授权，提供版本历史、审计日志和 REST API。
- 🤖 **AI 可选接入**：MCP 服务器默认关闭，开启后 AI 代理可在连接者权限范围内搜索、读取和提出编辑。
- 🧩 **功能扩展**：包含反馈板、博客、内容块、图片编辑、标签、术语表、重定向、通知、生命周期规则、分析、Prometheus 指标、高可用等。
- 📦 **部署方式**：支持 Docker/Compose、Kubernetes/Helm、Linux/macOS/Windows 裸机及一键云模板，Node.js + PostgreSQL 即可运行。
- 🆓 **开源与获取**：免费永久使用、AGPL 许可，社区公开构建，可立即开始搭建 Wiki。

---

### [AI JS Day 2026 — 面向前端开发者的直播](https://lp.jetbrains.com/ai-js-day-2026/?utm_source=newsletter_js_weekly&utm_medium=cpc&utm_campaign=webstorm_javascript_day_2026_js_weekly_classified)

**原文标题**: [AI JS Day 2026 â Live Broadcast for Frontend Devs](https://lp.jetbrains.com/ai-js-day-2026/?utm_source=newsletter_js_weekly&utm_medium=cpc&utm_campaign=webstorm_javascript_day_2026_js_weekly_classified)

overview summary  
JetBrains AI.js Day 2026 是一场免费线上活动，将于 11 月 13 日举行，聚焦 AI 对 JS/TS 前端开发者的职业前景、核心技能与开发工作流的影响，并邀请多位行业专家分享实战观点与职业建议。

- 📅 活动时间：2026 年 11 月 13 日，线上举行，完全免费。
- 🎤 核心议题：AI 时代前端开发者是否仍有岗位、需要哪些新技能，以及代码库与职业方向将如何变化。
- 🧠 重点演讲包括：提示与结果之间的工程判断、AI 时代工程师的“判断力”、从前端转型 AI 工程师的路径。
- 🛠️ 工作流主题：如何把 Figma、Chrome DevTools、Storybook、MUI、Callstack、WebStorm 等工具与 AI 结合成可扩展的前端工作流。
- 👥 讲者来自 Atlassian、Google、Storybook、Material UI、CallStack、JetBrains、Figma 等公司。
- 🗓️ 议程从欢迎开场到总结收尾，包含多场主题演讲，时间覆盖 UTC、CET/CEST、EST/EDT 时区。
- 💬 观众可在演讲期间通过聊天提问，主办方会尽量实时解答。
- 📺 所有场次都会录制并发布到 YouTube，错过直播可回看。
- ✅ 需提前注册保存席位，可选择接收活动提醒及未来 JetBrains WebStorm 活动邮件。

---

### [账户共享检测与预防 | Fingerprint](https://fingerprint.com/use-cases/account-sharing-prevention/?utm_source=JSWeekly111026&utm_medium=newsletter)

**原文标题**: [Account Sharing Detection and Prevention | Fingerprint](https://fingerprint.com/use-cases/account-sharing-prevention/?utm_source=JSWeekly111026&utm_medium=newsletter)

Fingerprint 提供基于设备智能的账户共享检测与预防方案，帮助订阅业务识别多设备、多地点、多用户共享账户的行为，将共享用户转化为付费用户，同时兼顾反欺诈能力和正常用户体验。

- 🎯 核心目标：减少账户共享并提升收入，轻松检测共享账户用户并促使其转为付费用户。
- 🧠 设备识别：利用 70+ 设备与浏览器信号唯一识别设备，可限制单个账户可注册的设备数量。
- 🌍 共享检测：识别同一订阅被多人、多设备和多地点使用，包括通过 VPN 与 IP 信号发现的“不可能旅行”。
- 📈 业务量化：以高精度衡量账户共享造成的收入损失，只需少量代码即可集成。
- 🛡️ 反欺诈增强：文中称可将欺诈检测能力提升 5 倍。
- ⚙️ 智能信号：提供 20+ 高级风险属性，例如 VPN 检测，用于大规模阻止账户共享滥用。
- 😊 用户体验：仅对高风险用户增加安全验证步骤，可信订阅用户不会被额外挑战，降低误报影响。
- 🚀 集成与案例：提供 AI 代理安装指南及 `npx fingerprint`、`npx skills add fingerprintjs/skills` 等方式；Chegg 等订阅企业已用于检测共享账户并转化付费用户。

---

### [我测试了所有 JavaScript 运行时（令人惊讶）- YouTube](https://www.youtube.com/watch?v=zDw_DxM5GlI)

**原文标题**: [I tested EVERY Javascript runtime (surprising) - YouTube](https://www.youtube.com/watch?v=zDw_DxM5GlI)

本内容为 YouTube/Google 网站页脚导航与法律信息，汇总平台介绍、联系与版权、创作者/广告/开发者入口、条款隐私与安全政策，以及 2026 年 Google LLC 版权声明。

- 🏢 包含 About、Press、Contact us 等公司与联系信息入口。
- 👥 提供 Creators、Advertise、Developers 等面向创作者、广告主和开发者的链接。
- 📜 列出 Terms、Privacy、Policy & Safety、Copyright 等法律与政策页面。
- ⚙️ 包含 How YouTube works 与 Test new features，说明平台运作及新功能测试入口。
- ©️ 版权声明为 © 2026 Google LLC。

---

### [推出自适应深色模式 | WebKit](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/)

**原文标题**: [  Introducing Adaptive Dark Mode | WebKit](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/)

Safari 27.3 beta 推出自适应深色模式，可在用户启用深色外观后自动将浅色网站转换为深色，弥补深色模式用户多但网站支持少的差距，同时兼顾可用性、网站控制权与用户隐私。

- 🌓 **新功能发布**：Safari 27.3 beta 引入自适应深色模式，用户开启后，Safari 会自动把浅色网站呈现为深色。
- 📊 **需求缺口明显**：约 40% 的网页加载来自深色模式用户，但仅约 10% 的页面加载支持深色模式。
- 🧪 **试用方式**：将系统外观设为深色，访问亮色背景网站，Safari 会提供预览，点击“Try”即可体验。
- 🎨 **尊重网站声明**：若网站通过 `color-scheme: light dark` 等声明支持深色模式，自适应深色模式不会改动页面。
- 🔍 **智能分析页面**：对其他网站，Safari 会分析颜色并判断页面整体偏亮还是偏暗；偏暗页面不变，偏亮页面转为深色。
- 🌈 **颜色变换策略**：使用颜色矩阵在保持色相的同时反转明度，并尽量满足 WCAG 4.5:1 对比度要求，也会转换浅色 CSS 渐变。
- 🖼️ **图像与 SVG 处理**：多数图片保持不变；SVG 图标和标志在需要时调整颜色；位图会分析像素直方图，并反转简单黑白标志。
- ⚠️ **特殊内容保护**：`<canvas>` 内容保持不变；部分遮罩和 `mix-blend-mode` 效果可能被关闭以避免异常结果。
- 🛠️ **网站优化建议**：使用 SVG 图标、CSS 纯色或渐变、透明背景内容图、现代 CSS 按钮样式，并给容器增加内边距。
- 🧩 **局部或完整深色支持**：可对特定元素应用 `color-scheme: light dark`；完整支持可使用 `prefers-color-scheme`、`<picture>`、`light-dark()`、`color-mix()`、`contrast-color()` 等技术。
- 🚫 **可拒绝自动转换**：网站可用 `color-scheme: light only` 表示仅支持浅色模式，但 Safari 27.3 beta 1 暂不支持 `only` 关键字。
- 🔒 **隐私保护**：Safari 阻止网站检测用户是否启用自适应深色模式；JavaScript 查询 CSS 颜色会得到原始颜色，canvas 图像也按原始形式渲染。
- 💬 **反馈渠道**：网站开发者可联系 `web-evangelist@apple.com`；用户遇到问题可通过 Feedback Assistant 提交报告。

---

### [GitHub - mrdoob/codevember-2026:2026年11月每日创意智能体编程实验。· GitHub](https://github.com/mrdoob/codevember-2026)

**原文标题**: [GitHub - mrdoob/codevember-2026: Daily creative agentic coding experiments for November 2026. · GitHub](https://github.com/mrdoob/codevember-2026)

该仓库是 mrdoob 发起的 Codevember 2026 项目，旨在整个 2026 年 11 月期间，每天进行创意型智能体编程实验，并按照 @thespite 分享的提示词列表推进。项目公开、采用 MIT 许可证，已积累一定关注度。

- 📅 项目定位：2026 年 11 月每日创意智能体编程实验。
- 🧠 创作线索：实验主题遵循 @thespite 分享的提示词列表。
- 📂 当前进度：已建立 01 至 10 日文件夹，包含 Fold、Shatter、Melt、Tangle、Moss、Orrery、Hollow、Tesseract、Membrane、Caustic 等主题。
- 🔗 内容结构：前 10 天提供实验查看链接与源码链接。
- ⏳ 后续计划：11 至 30 日已列出关键词，如 Rust、Feather、Labyrinth、Tension、Mirage、Portal、Dissolve 等，但尚未提供实验或源码。
- ⭐ 仓库数据：44 个 Star、4 个 Fork、1 个 Watcher、29 次提交。
- 📜 开源许可：采用 MIT 许可证，仓库包含 README 与 LICENSE 文件。

---

### [推出 Vite 生态基金 | Cloudflare 博客](https://blog.cloudflare.com/launching-vite-ecosystem-fund/)

**原文标题**: [Launching the Vite Ecosystem Fund | Cloudflare Blog](https://blog.cloudflare.com/launching-vite-ecosystem-fund/)

Cloudflare 正式启动 Vite 生态基金，首轮向 44 个项目和维护者分配 301,300 美元，兑现其投入 100 万美元支持 Vite 开源生态的承诺；文章同时强调，AI 在提升开源价值的同时，也加剧了维护者负担与可持续性问题。

- 💰 **首轮资助**：Cloudflare 向 Vite 生态中的 44 个项目和维护者发放首轮 301,300 美元，后续将按季度继续分配承诺资金。
- 🎯 **资助目标**：重点支持关键依赖、生态重要插件、重要贡献者以及推动生态前进的项目。
- 🧑‍⚖️ **评选机制**：受助方由 Vite 技术栈核心团队成员组成的小组选出，成员来自 Vite、Vitest、Rolldown、Oxc、Vite+ 等项目，也包括非 Cloudflare 员工。
- 🤖 **AI 改变开源协作**：AI 让提交 PR 更容易，导致 PR 数量激增，但维护者数量未同步增长，审查负担显著上升。
- 🔥 **维护者倦怠加剧**：AI 加速项目迭代和功能竞争，可能形成“越用 AI 越要加速”的循环，进一步放大维护者 burnout 和可持续性问题。
- 🌱 **受助案例**：e18e 是首批受助方之一，其负责人 James Garbutt 长期参与开源，并帮助 Svelte、Storybook、Nx 等工具提升性能。
- 💵 **资金分配方式**：资金通过 Cloudflare 的 Open Collective 分配，包括对生态受助方的贡献资助和对核心维护者的津贴。
- ⏱️ **维护者津贴**：Vite 技术栈核心维护者每月最多可获 4,000 美元津贴，按每月贡献小时数以每小时 50 美元计费；已因相关工作获得报酬或受雇者不符合资格。
- 🌐 **更广泛的开源支持**：Cloudflare 还承诺向 Community Engineers Fund 额外投入 100 万美元，并通过 Project Alexandria 向开源项目提供 Cloudflare  credits。

---

