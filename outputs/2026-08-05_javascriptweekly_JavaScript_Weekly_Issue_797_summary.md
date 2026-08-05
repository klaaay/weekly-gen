### [](https://nextjs.org/blog/next-16-3)

**原文标题**: [Next.js 16.3 | Next.js](https://nextjs.org/blog/next-16-3)

Next.js 16.3 正式发布，带来多项性能优化与全新功能，包括大幅降低开发内存占用、加快构建与渲染速度，并引入“Instant Navigations”套件以提升导航体验，同时提供实验性特性供开发者尝试。

- 🚀 开发服务器内存占用最高减少 90%（如 vercel.com 从 21.5GB 降至 2GB），基于磁盘缓存与内存驱逐机制。
- ⚡ `next build` 重复构建可使用缓存，CI 构建速度最高提升 5.5 倍；同时支持 TypeScript 7 进行更快类型检查。
- 📈 服务端渲染改用原生 Node.js 流，替代 Web Streams，在负载下可多处理约 22% 的请求。
- 🤖 AI 编码代理可自动读取与项目版本匹配的文档（通过 AGENTS.md 指向本地 node_modules），无需额外配置。
- 🔗 预取请求合并小载荷，减少请求数量；不可变静态资源可在部署间复用，避免缓存失效问题。
- 🛡️ 新增 `catchError` 自定义错误边界，支持重试失败的 Server Components，且不干扰 `notFound` 或 `redirect`。
- 📂 内置 Vite 兼容的 `import.meta.glob` 导入，便于从文件系统加载多个模块并获得热更新支持。
- 🌍 新增 Root Params（如 `lang`），可在任意 Server Component 直接访问根级动态参数，避免 prop-drilling。
- ⚡ “Instant Navigations”套件上线：Instant Insights 自动检测慢导航；Partial Prefetching 精细控制预取内容。
- ♻️ 改进 ISR：未预渲染的页面首访可显示即时加载壳，后台升级为完整预渲染页，后续访问直接命中缓存。
- 🔍 新增 Navigation Inspector 工具，可暂停加载并可视化导航壳层；提供 Playwright `instant()` 测试助手防止回归。
- 🧪 实验性 Rust 版 React Compiler 直接集成 Turbopack，冷构建提速约 34%，热构建约 46%；网络弹性功能 `useOffline` 支持断线重试。
- 📦 升级方式：运行 `npm install next@latest`，并支持通过 `cacheComponents` 和 `partialPrefetching` 配置启用新特性。

---

### [@danabra.mov 在 Bluesky 上](https://bsky.app/profile/danabra.mov/post/3mp5b3nd3ws2k)

**原文标题**: [@danabra.mov on Bluesky](https://bsky.app/profile/danabra.mov/post/3mp5b3nd3ws2k)

dan 在 Bluesky 上发布声明，宣布自己加入 Vercel 的 Next.js 团队，初期以兼职身份工作，并希望通过关注用户反馈来推动 App Router 的改进。

- 🎉 宣布加入 Vercel 的 Next.js 团队
- ⏳ 初期为兼职，暂时不希望被大量 bug 报告淹没
- 👀 会持续关注 bug 报告，以了解用户日常遇到的真实问题
- 🚀 目标是让 App Router 变得更好

---

### [](https://x.com/rauchg/status/2077870043833229692)

**原文标题**: [Guillermo Rauch on X: "I’m excited to welcome two legends of developer tools, Pete Hunt (@floydophone) and Nick Schrock (@schrockn), to Vercel.

Pete was one of the pioneers of @reactjs at Meta. He made an early bet to power Instagram Web with ⚛️ React, evangelizing it internally and externally. He" / X](https://x.com/rauchg/status/2077870043833229692)

overview summary
- 🎉 Vercel 创始人 Guillermo Rauch 宣布两位开发者工具传奇人物 Pete Hunt 与 Nick Schrock 正式加入团队。
- ⚛️ Pete Hunt 是 React 早期先驱，曾推动 Instagram Web 采用 React，将负责领导 Frameworks 与 Next.js 的发展。
- 📊 Nick Schrock 是 GraphQL 联合发明者，将专注 Agentic Developer Experience，助力下一代智能代理与自我改进软件的未来。
- 💼 Rauch 表示这是初创公司创始人的梦想成真，团队正在招聘，欢迎直接私信联系。
- 🔥 社区反响热烈，多位开发者送上祝贺与期待。

---

### [](https://nextjs.org/blog/next-16-3-instant-navigations)

**原文标题**: [Next.js 16.3: Instant Navigations | Next.js](https://nextjs.org/blog/next-16-3-instant-navigations)

Next.js 16.3 即将推出“Instant Navigations”功能，目标是在不牺牲服务端驱动架构优势的前提下，让导航体验达到客户端 SPA 的即时响应水平。文章介绍了问题根源、开启方式、Stream/Cache/Block 三种控制选项、全新的路由级预取机制、配套开发工具与测试方法，以及未来的默认化和离线导航计划。

- 🧭 背景痛点：服务端驱动的导航依赖网络往返，点击后没有即时反馈，显得“像传统网站”；而 SPA 导航能立刻显示页面外壳，体验更流畅。
- ⚙️ 开启方式：需要在 `next.config.ts` 中设置 `cacheComponents: true` 来启用新行为，未来该标志将成为默认配置。
- 🎛️ 三种导航控制：路由 `await` 数据时，开发者可选择 Stream（配合 `<Suspense>`）、Cache（配合 `'use cache'`）或 Block（通过 `export const instant = false`），从而决定导航是否即时。
- 🔍 Instant Insights：开发环境中会自动标记并报错慢导航，帮助定位非即时路由；未来还计划在构建阶段捕获这些回归。
- 🧪 测试辅助：提供来自 `@next/playwright` 的 `instant()` 测试助手，可精确断言点击链接后哪些内容必须立即可见，防止重构导致性能回退。
- 🚀 预取策略重构：不再为每个链接单独预取，而是按路由只预取一个可复用的 loading shell，并在客户端缓存；这类似于 SPA 的按路由代码分割，同时为离线导航打下基础。
- ⚡ Partial Prefetching：通过 `partialPrefetching: true` 开启，未来也将成为默认；它只预取每个可见路由的 shell，大幅减少多余请求。
- 🛠️ Navigation Inspector：新增的 DevTools 工具可暂停导航在 shell 阶段，直观查看每个路由预取的内容，以及哪些部分需要等待网络。
- 🔗 深度预取选项：使用 `<Link prefetch={true}>` 可对特定链接进行额外预取，再配合 `'use cache'` 预取更多内容，避免“全有或全无”的限制。
- 📉 内部验证：v0 团队已在生产环境采用这些工具，导航耗时显著下降，具体模式将在后续文章中分享。
- 🎵 开源示例：Next Beats（基于 Next.js 16.3 Preview 的音乐播放器）展示了 Instant Navigations 的实际效果，源码已在 GitHub 上公开。
- 📦 试用与反馈：可通过 `npm install next@preview` 安装 16.3 Preview；已知问题包括 Safari 下 Instant Insights 工具异常（建议用 Chrome/Firefox）、部分阻塞路由未报告等，团队正在修复。

---

### [](https://nextjs.org/blog/next-16-3-ai-improvements)

**原文标题**: [Next.js 16.3: AI Improvements | Next.js](https://nextjs.org/blog/next-16-3-ai-improvements)

Next.js 16.3 预览版推出一系列面向 AI 代理（agent）开发体验的改进，重点是让代理基于版本匹配的本地文档、可操作的错误提示和浏览器内省能力，更高效地编写和维护 Next.js 应用。

- 📦 **AGENTS.md 自动管理文档**：`next dev` 会自动写入或更新 `AGENTS.md` 指针，引导代理阅读 `node_modules` 中本地捆绑的版本匹配文档，避免依赖过时的训练数据；已有项目可通过 codemod 补齐。
- 🛠️ **新增三个官方 Skills**：`next-dev-loop` 让代理驱动完整开发反馈循环；`next-cache-components-adoption` 逐步采用 Cache Components；`next-cache-components-optimizer` 将路由优化为即时加载；稳定版还追加了第四个 Skill。
- 🌐 **agent-browser 支持 React 内省**：`next-browser` 合并入通用 `agent-browser` CLI，v0.27 起可查看组件树、检查 fiber、分析重渲染和 Suspense 状态，让代理能验证运行时渲染结果。
- ⚠️ **可操作错误提示**：Instant Insights 在 overlay 和终端中提供标记的修复菜单（Stream / Cache / Block），并附“Copy prompt”按钮，直接生成给代理的修复指令；构建和 CI 日志同样适用。
- 📄 **为代理编写的错误文档**：每个错误都有独立的 `/docs/messages` 页面，统一包含 Patterns、Trade-offs 和 Gotchas，帮助代理理解修复边界和易错点。
- 🧩 **精简 MCP 服务器**：移除知识库相关工具，新增 `get_compilation_issues` 和 `compile_route`，让代理直接从运行中的 dev server 快速检查编译，无需反复运行完整构建。
- 📝 **文档支持 Markdown 输出**：任意 `nextjs.org/docs` URL 追加 `.md` 即可获得纯文本版，也支持 `Accept: text/markdown`，并提供 `/docs/llms.txt` 与 `/docs/llms-full.txt` 索引。

---

### [](https://master.dev/courses/frontend-architecture/?utm_source=email&utm_medium=javascriptweekly&utm_content=frontendcooper)

**原文标题**: [Architect Scalable Frontend Applications | Master.dev](https://master.dev/courses/frontend-architecture/?utm_source=email&utm_medium=javascriptweekly&utm_content=frontendcooper)

本課程深入探討前端架構從單體到微前端的演進，涵蓋軟體架構核心概念、模組化單體、Monorepo 管理，以及微前端實作與通訊策略，協助開發者有效擴展大型程式碼庫並做出務實的架構決策。

- 🏛️ 課程以實作角度介紹軟體架構四大支柱：架構風格、特性、決策與邏輯元件，並以 RPG 角色創建來比喻，幫助理解與評估不同架構。
- 🧱 單體架構單元聚焦電商平台實作，使用 C4 模型視覺化系統，並探討模組邊界模糊導致的「大泥球」問題。
- 📦 透過領域驅動設計的子域概念來劃分模組、定義資料夾結構與邊界，建立「模組化單體」。
- 🚧 使用 ESLint boundaries 外掛與 Dependency Cruiser 等工具，強制執行跨模組依賴規則，防止架構腐化。
- 🗂️ Monorepo 單元示範將單體轉換為多套件工作區，並採用 Turborepo 進行快取、任務編排與依賴管理，提升建置效率。
- 🔀 透過 Turborepo 標記套件並定義依賴方向，可自動偵測循環依賴與錯誤套件關係，並產生依賴圖視覺化專案結構。
- 🌐 微前端單元介紹 iframe、Web Components、Module Federation 等不同實作方式，並探討獨立部署與團隊擴展的成長需求。
- ⚙️ 實作 Module Federation 設定 host 與 remote，分享 React 等共用依賴，並以 react-lazy 非同步載入遠端模組，加入 Suspense 與錯誤處理。
- 💬 微前端間通訊可透過 postMessage API 或傳遞 props，並使用 Nanostores 建立原子狀態與監聽器，達成狀態解耦。
- 🆕 Module Federation 2.0 新增 MFManifest.json 標準化、運行時註冊遠端模組，並簡化型別定義自動產生流程。
- 📋 課程亦探討前端服務發現模式與版本管理，最後點出過度使用 Module Federation 可能造成的 CSS 衝突等成本，建議依架構需求審慎評估。

---

### [](https://zserge.com/posts/worst-htmx-ever/)

**原文标题**: [Let's make the worst htmx ever!](https://zserge.com/posts/worst-htmx-ever/)

该文章讲述了作者用约 40 行代码实现一个简化版 HTMX 克隆的过程，重点展示其核心机制（扫描、发送、交换）以及如何通过事件系统扩展插件功能。

- 🔧 核心原理：通过声明式属性（如`x-get`、`x-target`、`x-swap`）实现事件触发、AJAX 请求和 DOM 更新，仅需后端返回 HTML 片段。
- ⚙️ 实现步骤：使用`querySelectorAll`扫描带`x-`属性的元素，绑定默认触发器（按钮为`click`，表单为`submit`），并通过`fetch`发送请求，最后按指定模式（替换、追加、删除等）交换内容。
- 🔁 动态内容处理：利用`MutationObserver`监听 DOM 变化，只对新插入的节点重新扫描绑定，避免全量重扫，提升性能。
- ⏱️ 触发器增强：支持自定义事件语法（如`load`、`changed`、`delay:500`、`once`），通过解析属性实现延迟、去重、一次性触发等高级行为。
- 🎯 目标定位扩展：除`querySelector`外，支持`closest`、`next`、`previous`、`document`等关键字，方便灵活选择交换目标元素。
- 📡 事件生命周期：在请求前后和交换前后分别触发`x:beforeSend`、`x:afterSend`、`x:beforeSwap`、`x:afterSwap`，允许开发者通过`preventDefault()`取消或修改流程。
- 🧩 服务端响应头支持：处理`HX-Trigger`（触发自定义事件）、`HX-Redirect`（跳转）、`HX-Refresh`（刷新页面）、`HX-Retarget`（重设目标）等头部，增强与后端协作能力。
- 🧰 插件化架构：基于事件系统，无需改动核心代码即可实现`x-confirm`（确认框）、`x-indicator`（加载指示）、`x-disable`（禁用状态）、`x-select`（响应片段选择）、`x-push-url`（历史记录）等扩展。
- ⚠️ 局限与展望：缺少错误处理、异步取消、视图过渡等高级功能，作者认为这些可作为读者练习，或直接使用成熟的 HTMX 库。

---

### [让我们来做史上最差的 React！](https://zserge.com/posts/worst-react-ever/)

**原文标题**: [Let's make the worst React ever!](https://zserge.com/posts/worst-react-ever/)

作者在德国假日突发奇想，尝试用最简单的方式实现一个“最烂的 React 克隆”，只为理解底层原理。文章逐步展示了从 hyperscript 到渲染算法、状态管理、以及用标签模板字面量解析 JSX 的整个过程，最终产出一个不足 1KB、支持 hooks 的玩笑项目“O!”，并发布在 GitHub 上。

- 🏖️ 作者因德国假日空闲，决定亲手实现一个低性能、多 bug 的 React 克隆，以体验核心机制。
- ⚛️ 用极简的 `h(tag, props, ...children)` 函数替代 JSX，将布局转为虚拟节点对象。
- 🛠️ 渲染函数 `render` 递归将虚拟节点转为真实 DOM，通过简单对比决定插入、更新或删除。
- 🔄 组件通过 `forceUpdate` 回调强制整体重渲染，状态则用全局变量管理，简单粗暴。
- ✂️ 使用 ES6 标签模板字面量 `x\`...\`` 编写了一个迷你 HTML 解析器，支持标签、属性、文本等语法，免去 JSX 转译。
- 🧩 解析器基于“文本 / 开标签 / 闭标签”三状态状态机，搭配正则表达式，实现简短但效率低。
- 📦 项目命名为“O!”，压缩后小于 1KB，还加入了 keys 和 hooks，颇具讽刺意味。
- 🤣 这是一款“玩具”库，作者明确表示不要在生产环境使用，但欢迎反馈和 PR。

---

### [让我们来打造史上最烂的 VueJS！](https://zserge.com/posts/worst-vuejs-ever/)

**原文标题**: [Let's make the worst VueJS ever!](https://zserge.com/posts/worst-vuejs-ever/)

overview summary  
- 🧪 文章介绍如何从零构建一个极简的 VueJS 克隆框架，揭示其核心原理并不复杂。  
- 🔍 Vue 的响应式基于 `Object.defineProperty`，通过自定义 getter/setter 拦截属性访问和修改，实现依赖追踪。  
- 📝 表达式求值借助 `new Function` + `with` 实现安全的 `eval`，如 `call('a+1', {a:42})` 返回 43。  
- ⚙️ 通过代理数据对象，收集表达式访问过的变量，并在变量变化时触发相关表达式重新求值。  
- 🧩 支持类似 Vue 的指令（`q-text`、`q-on:click`、`q-bind:style`），每个指令绑定 DOM 节点和表达式。  
- 🛠️ 核心代码包括 `walk` 遍历 DOM 绑定指令、`proxy` 拦截数据访问、`$dep` 记录当前依赖，整体仅需少量代码。  
- 🎯 示例计数器展示了点击按钮更新文本，证明框架可用且逻辑简单。  
- 🚀 进阶建议：实现 `q-if` 和 `q-each`，完整源码托管在 GitHub（zserge/q）。  
- 📚 补充说明：Vue 2 使用 `Object.defineProperty`，Vue 3 改用 ES6 的 `Proxy`/`Reflect`，作者鼓励读者自行实现并提交 PR。

---

### [](https://htmx.org/)

**原文标题**: [</> htmx - high power tools for html](https://htmx.org/)

htmx 是一个轻量级、无依赖的 HTML 扩展库，让你直接在 HTML 中用属性实现 AJAX、CSS 过渡、WebSocket 和 SSE，从而以超文本的简洁与力量构建现代界面，相比 React 可减少 67% 的代码量，目前 htmx v4 正在测试中，预计 2026 年夏季发布。

- 🚀 htmx 4 已进入 beta 测试，目标 2026 年夏季正式发布，更多信息见 four.htmx.org
- ⚡ 通过 hx-post、hx-swap 等属性，直接在 HTML 中发起 AJAX、CSS 过渡、WebSocket 与 SSE 请求
- 📦 体积仅约 16k（min+gz），无依赖、可扩展，相比 React 减少 67% 代码量
- 💡 突破传统限制：不只是 `<a>` 与 `<form>` 能发请求，不只是 click/submit 触发，不限于 GET/POST，不必整页替换
- 🔧 快速上手：引入 CDN 脚本，用 `hx-post="/clicked"` 和 `hx-swap="outerHTML"` 即可让按钮点击后 AJAX 替换自身
- 🔄 htmx 是 intercooler.js 的继任者，2.x 已放弃 IE 支持，需要 IE 可用 1.x 长期维护版
- 📚 官方书籍《Hypermedia Systems》已发布，讲述如何用 htmx 构建超媒体驱动应用
- 💝 支持 htmx 开发可通过 GitHub Sponsors，已有白金、金、银级赞助商，源自蒙大拿 ʕ •ᴥ•ʔ

---

### [](https://evilmartians.com/chronicles/the-secure-way-to-release-an-npm-package)

**原文标题**: [The secure way to release an npm package in 2026—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/the-secure-way-to-release-an-npm-package)

供应链攻击已成为 npm 发布的核心威胁，攻击者通过 LLM 自动化窃取包和令牌；安全发布不仅是防护，也是提升 npm 信誉与竞争力的手段。文章提供了一套完整的加固方案：从 Trusted Publisher、Staged Publishing、CI 工作流加固、依赖冷却、权限限制，到构建流程简化与依赖缩减，强调“无令牌、最小依赖、人工审批”的原则。

- 🔐 优先使用 npm Trusted Publisher，用 GitHub 工作流发布而非 npm token；在 npm 设置中仅允许 `npm stage publish`，并禁用 token。
- ✅ 启用 Staged Publishing：CI 先执行 `npm stage publish`，再由维护者用硬件 2FA 手动批准，兼顾自动化与安全。
- 🛡️ 为 npm 包启用 Provenance，让 CI 签名确认来源；但理解它只证明“来源正确”，不等于“内容安全”。
- 📜 用 GitHub 分支/标签规则集限制：只允许仓库管理员创建标签，阻止攻击者通过写权限触发发布。
- 🧹 固定所有第三方 CI action 为 SHA 提交哈希（而非 `@v7` 标签），推荐 `actions-up` 工具自动管理。
- 🚨 增加 CI 工作流安全 lint（如 zizmor），并固定 `actions/checkout`、`actions/setup-node` 等为长 SHA。
- 🕒 设置新依赖版本冷却期（3 天可拦截约 94% 恶意包）：npm 用 `min-release-age`，pnpm/yarn/bun 各有对应配置。
- 🚫 使用 npm 12、pnpm 10、yarn 4.14 或 bun，默认禁用依赖的 `postinstall` 脚本，减少恶意代码执行面。
- 🔒 发布工作流中只给 `id-token: write`，避免安装 npm 依赖或使用多余第三方 action；构建和发布分拆为独立 job，用 artifact 传递产物。
- 🧱 尽可能取消构建步骤：直接发布源码或用 TSDoc 类型注释的 `.js`；如必须构建，用更小编译器（如 ts-blank-space）并禁用缓存。
- 📦 发布新版本只需打 tag（如 `v1.0.1`），CI 自动测试、构建并进入 Staged Packages，等待手动批准。
- 🕵️ 用 drydock 等工具在批准前检查 npm 包与源码的 diff，避免构建步骤注入恶意代码。
- 🔍 减少依赖数量与攻击面：用 `npmgraph` 分析嵌套依赖，用 `@e18e/cli` 寻找更轻量替代，小工具可用 LLM 重写为本地文件。
- 🖥️ 使用 Dev Container 隔离开发环境，限制依赖、IDE 扩展和 LLM 对系统的访问；团队可共享一致环境。
- 🌐 对 CI 使用 Harden Runner 的域名白名单（`egress-policy: block`），阻止恶意程序外传令牌。
- ⚠️ 不要抱有“小包没人黑”的侥幸：现代攻击是自动化蠕虫式的；应将安全视为基本功，并扩展到 Docker 镜像、IDE 扩展、Python 环境等所有第三方依赖。

---

### [获取失败](https://www.npmjs.com/package/postcss)

**原文标题**: [Failed to retrieve](https://www.npmjs.com/package/postcss)

无法总结：获取内容失败，状态码 403。

---

### [](https://socket.dev/blog/popular-npm-packages-in-the-keyv-and-cacheable-namespaces-compromised-in-active-supply-chain)

**原文标题**: [Popular npm Packages in the keyv and Cacheable Namespaces Co...](https://socket.dev/blog/popular-npm-packages-in-the-keyv-and-cacheable-namespaces-compromised-in-active-supply-chain)

该报道揭示了一个伪装成正常依赖的 npm 恶意软件包集群，通过拆分恶意功能绕过检测，最终向阿里巴巴开发者部署跨平台远控木马（RAT）。

- 🎯 攻击目标明确锁定阿里巴巴开发者，具有高度针对性。
- 📦 恶意 npm 包集群表面上看似无害，实则通过依赖链分发恶意载荷。
- 🧩 恶意功能被拆分到多个包中，以规避安全检测和审查。
- 🖥️ 最终载荷为跨平台 RAT，可控制 Windows、macOS 或 Linux 系统。
- 🕵️ 攻击手法体现供应链攻击的隐蔽性与复杂性，开发者需警惕来源不明的依赖包。

---

### [](https://github.com/wiz-sec-public/wiz-research-iocs/blob/main/reports/keyv-packages.csv)

**原文标题**: [wiz-research-iocs/reports/keyv-packages.csv at main · wiz-sec-public/wiz-research-iocs · GitHub](https://github.com/wiz-sec-public/wiz-research-iocs/blob/main/reports/keyv-packages.csv)

该文本展示了一个 GitHub 公开仓库的页面片段，内容涉及安全研究项目的报告文件，并包含版本控制与项目管理的常用功能入口。

- 📄 页面对应公开仓库 `wiz-sec-public/wiz-research-iocs`，属于安全研究领域。
- ⭐ 仓库获得 103 个 Star 和 9 个 Fork，具备一定关注度。
- 📁 核心文件路径为 `reports/keyv-packages.csv`，位于报告目录中。
- 🧾 该 CSV 文件共 444 行，大小约 28.2 KB，属于中等规模的数据文件。
- 🛠️ 页面提供 Code、Issues、Pull Requests、Actions、Projects 等标准 GitHub 功能导航。
- 🔒 文件支持预览、代码查看、原始内容下载及编辑操作。

---

### [](https://astro.build/blog/whats-new-july-2026/)

**原文标题**: [What’s new in Astro - July 2026 | Astro](https://astro.build/blog/whats-new-july-2026/)

overview summary
Astro 生态在 2026 年 7 月迎来大量新动态：官方发布了 7.1 版本，社区活动与竞赛火热开展，众多知名企业采用 Astro Starlight 搭建文档，同时涌现出海量社区工具、主题模板与精选案例网站，生态活力持续攀升。

- 🚀 官方发布 Astro 7.1，新增更多 CSP 选项、自定义分页 URL、多开发服务器及更低内存的内容集合等功能
- 🇩🇪 官方宣布将于 9 月 5 日在德国威斯巴登举办 Astro Together FRA x Seibert 线下聚会，名额有限需提前报名
- ☀️ Astro Mart 推出 2026 夏季系列周边商品
- 🏆 Webflow 与 CodeTV 联合举办黑客松：使用 Astro 构建、GSAP 实现动画、部署至 Webflow
- 🏢 Mozilla、Supabase、Framework、System76 等知名企业均使用 Astro Starlight 构建官方文档
- 🎨 精选一批风格新奇有趣的 Astro 网站（Weird Wide Web），涵盖历史问答、食物储存指南、球衣测验等创意案例
- ✨ Cosmic Canvas 板块展示视觉惊艳、动画流畅的高质量 Astro 站点，包括 MARQY、Radian R&D 等
- 👏 社区 shout-out 给 @adamchal，感谢其在核心仓库、文档和 Discord 中的积极贡献
- 📝 社区精选内容：Astro 7 基准测试（743 页站点构建时间减半）、利用 Starlight 自动化跨仓库文档、Astro 7.0 空白处理等
- 🔄 收录多篇迁移故事：从 Hugo、Jekyll、Next.js 迁移到 Astro 的实际经验分享
- 🛠️ 新增大量社区集成与工具：测试工具、幻灯片框架、表单处理、SEO/AEO 套件、CMS 编辑器、内容加载器、Dev 工具栏应用及 Starlight 插件等
- 🎨 主题目录本月新增 100+ 主题与模板，涵盖 SaaS、医疗、餐饮、摄影、电商、教育等各类场景，并持续更新至 v7
- 🌐 大量新提交的 Astro 站点案例上线 showcase，覆盖电商、博客、AI、SEO 工具、本地服务等丰富行业
- 📚 Starlight in the wild 收录了 iframe-resizer、Semantic Release、Echo、Stellar SDK、Sentry 等众多项目的文档站
- 📢 鼓励社区通过展示墙、主题目录、package.json 关键词、社交媒体及 Discord #showcase 频道提交下月内容

---

### [](https://svelte.dev/blog/whats-new-in-svelte-august-2026)

**原文标题**: [What’s new in Svelte: August 2026](https://svelte.dev/blog/whats-new-in-svelte-august-2026)

本月最大的新闻是 SvelteKit 3 预览版（@next）首次发布，带来了多个新模块和功能改进；稳定版也有持续更新，语言工具增强了对错误页的类型支持；此外还有丰富的社区项目、学习资源以及即将举办的 Svelte Summit 活动。

- 🚀 SvelteKit 3 预览版共发布 13 个版本，亮点包括新 `$app/manifest` 和 `$app/service-worker` 模块、浅路由内置、`refreshAll` 替代 `invalidateAll` 等。
- 📦 远程表单新增 `submitted` 属性，可即时响应表单提交事件；`defineEnvVars` 移至 `@sveltejs/kit/env` 子路径。
- 🔀 `goto` 现在内置浅路由，通过 `state` 选项实现，并支持 `persistState: true` 在刷新后保留状态；`noScroll` 与 `keepFocus` 合并为 `reset` 选项。
- ⚠️ `error(status, {...})` 被弃用，改为 `error(status, message, {...})`，错误消息参数成为必填项。
- 🔄 `invalidateAll` 更名为 `refreshAll`，旧名称进入弃用状态。
- 🧩 新 `$app/manifest` 模块暴露 `immutable`、`assets`、`prerendered` 和 `routes`，方便在运行时检查构建输出；新 `$app/service-worker` 模块取代旧 `$service-worker`，且 `$app/paths` 可在 service worker 中导入。
- 📡 SvelteKit 现在可以在数据、远程表单响应、标签页聚焦和可见性变化时自动检测新部署，默认 `version.pollInterval` 为一小时。
- 🗺️ 生产构建开始支持 sourcemaps；Tracing 功能移出实验命名空间，并移除了 `instrumentation` 标志。
- 📝 表单字段新增 `dirty()` 和 `field.touched()` 辅助方法，改善验证交互体验。
- 🛠️ CLI 与语言工具更新：`sv` 更可靠地检测包管理器，add-on 作者可在 setup 阶段动态添加选项，`+error.svelte` 自动获得 `page` 和 `error` 属性类型。
- 🧹 `svelte-language-server` 移除了 lodash 依赖，安装体积更小、启动更快；Svelte Inspector 新增组件栈上下文菜单，方便在父子组件间跳转。
- 🎨 社区展示丰富：Recipe Jar、Doota、Loot Raiders 等新应用问世；LayerChart 2.0、Mochi、rsvelte 等库和工具更新；还有多篇学习资源和回顾文章。
- 📅 Svelte Summit Ljubljana 2026 定于 11 月 19-20 日举行，11 月 18 日为工作坊日，记得保存日期。

---

### [](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=26)

**原文标题**: [USPTO TTABVUE. Proceeding Number 92086835](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=26)

无法总结：未找到主要内容。

---

### [](https://tanstack.com/blog/tanstack-has-a-new-look)

**原文标题**: [TanStack Has a New Look | TanStack Blog](https://tanstack.com/blog/tanstack-has-a-new-look)

TanStack 发布了全新品牌视觉，由首位专职设计师 Andy Beutler 主导，系统化地重新设计了 Logo、字体、设计令牌和组件库。本文阐述了新设计背后的理念：旧式“干净整洁”的开发者风格已不够独特，品牌希望以更温暖、克制且带有人性关怀的视觉，传达“为开发者省下时间，让他们去享受生活”的核心目标。整个设计系统集中托管在 /ds 页面，以便长期维护和持续演进。

- 🎨 TanStack 正式推出全新品牌视觉，告别过去“足够好”的设计状态。
- 🧑‍🎨 首次聘请专职首席设计师 Andy Beutler，将分散的设计品味整合为统一的设计体系。
- 📐 新系统包含全新 Logo、全局字体、设计令牌、/ds 设计系统页面、组件套件、Phosphor 图标和棕榈树加载器。
- 🤖 旧式“干净整洁”的开发者风格已不再稀缺，因为 AI 可以轻易生成类似设计，品牌需要更独特的人性化表达。
- 🌴 沙滩与棕榈树主题象征“你被照顾好了，放心去享受生活”，是品牌核心价值观的视觉化体现。
- ⏳ TanStack 的核心产品是“把时间还给开发者”，帮助他们避开状态、路由、表格等领域的重复劳动和 bug。
- ✨ 新品牌追求用心、温暖和克制，拒绝过度设计，专注于精挑细选的细节并做到位。
- 📁 设计系统统一集中在 /ds，颜色、文字和组件都有了共享的标准，让长期维护更加一致和高效。
- 🚧 重新设计尚未完全收尾，部分页面仍在新旧过渡中，但已建立起可依赖的基础。
- 💡 即使是在为 AI 构建工具，品牌也希望让人感受到背后的用心与温度，而不是机器制造的冷漠感。

---

### [](https://tanstack.com/blog/introducing-tanstack-markdown-and-highlight)

**原文标题**: [Introducing TanStack Markdown and TanStack Highlight | TanStack Blog](https://tanstack.com/blog/introducing-tanstack-markdown-and-highlight)

概述：TanStack Markdown 和 TanStack Highlight 是两套刻意精简的库，用于替代 tanstack.com 中笨重的 Markdown 与代码高亮方案，将文档页面传输体积从约 1.1 MiB 降至约 27 KiB，并移除了内容相关的 RSC 架构。两者职责分离、体积小、无运行时依赖，已在实际生产内容中验证。

- 📦 推出两个新库：TanStack Markdown 负责解析为可序列化的文档树，TanStack Highlight 负责将代码转为语义化 HTML，两者互不依赖，通过回调连接。
- 🔪 解析与高亮分离：Markdown 解析无需加载高亮器，高亮器也可独立用于非 Markdown 代码，语言集和主题契约由使用者显式选择。
- 🌳 Markdown AST 是普通数据：纯对象与数组，可缓存、索引、跨服务端传输，支持 HTML/React/Octane 渲染，解析器仅 4.9 KB gzipped，零运行时依赖。
- 🚫 不支持的范围：不覆盖所有 CommonMark 边界情况、不提供异步插件链、不自动链接、不执行 MDX、不内置消毒器；默认转义原始 HTML 并移除危险 URL 协议。
- ⚡ 流式处理采用重解析策略：每次 UI 更新时同步重新解析累积文本，无增量解析器状态，流式扩展仅约 0.2 KB gzipped。
- 🖥️ 高亮器不为编辑器设计：无初始化 Promise、无自动语言检测、无隐藏语言注册表；空核心 1.7 KB，含全部 25 种语言约 8 KB，未知语言回退为纯文本。
- 🎨 一次代码树适配所有主题：输出含稳定 `th-*` 语义类、无内联颜色；深浅主题通过 CSS 变量切换，无需重新高亮。
- 🧪 小库依赖测试保障正确性：提交语料含 333 个来自 2,940 个文档文件的样本，覆盖 token 保真、确定性 HTML、包导出、体积预算及吞吐预算。
- 🏗️ tanstack.com 已是首个生产语料：两库已驱动官方文档与博客，使网站移除了内容专属 RSC 路径，同时保留性能优势并减小后续导航体积。
- 🔶 Alpha 阶段契约仍可调整：适合渲染已知技术内容的网页场景；若需要完整 CommonMark、大量语言、TextMate 保真或 MDX 生态，则不宜替换现有工具。

---

### [](https://github.com/mobxjs/mobx/releases/tag/mobx%407.0.0)

**原文标题**: [Release mobx@7.0.0 · mobxjs/mobx · GitHub](https://github.com/mobxjs/mobx/releases/tag/mobx%407.0.0)

MobX 7.0.0 正式发布，同步推出 mobx-react-lite 5 和 mobx-react 10。本次为清理型更新，聚焦现代运行时与装饰器模型，大幅减小打包体积，移除多项废弃 API，并调整 React 绑定要求。

- 📉 打包体积显著下降：ESM prod gzip 从 17.02 KiB 降至 13.96 KiB，最小 tree-shaken 示例仅 10.32 KiB。
- 🔧 强制使用 Proxy 支持的 observable 对象与数组，移除 ES5/非 proxy 回退；不再支持 `configure({ useProxies })` 及 `{ proxy: false }` 选项。
- 🚫 彻底移除旧版（legacy）装饰器支持。
- 🏷️ 命名空间注解与比较器改为命名导出，例如 `observable.ref` → `observableRef`、`computed.struct` → `computedStruct`、`comparer.identity` → `compareIdentity` 等。
- 🔍 移除公共 `trace` API，建议改用 `toJS`、`getDependencyTree`、`getObserverTree`、`spy` 或 `mobx-log` 进行调试。
- ⚛️ `mobx-react-lite` 5 和 `mobx-react` 10 要求 MobX 7 与 React 18+；前者面向函数组件，后者增加类组件及 Stage 3 `@observer` 类装饰器支持。
- 🧩 React 绑定包推荐公共 API 精简为：`observer`、`Observer`、`useLocalObservable`、`enableStaticRendering`、`isUsingStaticRendering`。
- 🗑️ 移除 `Provider`/`inject`/`MobXProviderContext`、`useObserver`、`useLocalStore`、`useAsObservableSource`、`useStaticRendering` 及 React batching 相关导入，建议改用 React 18+ 原生方式或 `createContext`、`useEffect` 等。
- ⏭️ 废弃 `observer(fn, { forwardRef: true })`，应直接传入已创建的 `React.forwardRef(...)` 组件。
- 🩹 补丁优化：缩短压缩错误 URL，进一步降低生产包体积。

---

### [](https://github.com/mobxjs/mobx/releases/tag/mobx-react%4010.0.0)

**原文标题**: [Release mobx-react@10.0.0 · mobxjs/mobx · GitHub](https://github.com/mobxjs/mobx/releases/tag/mobx-react%4010.0.0)

MobX 相关包发布重大版本更新，包括 MobX 7、mobx-react-lite 5 和 mobx-react 10，主要聚焦现代运行时、移除废弃 API、优化包体积，并明确 React 18+ 的绑定方式。

- 🚀 发布 MobX 7、mobx-react-lite 5 和 mobx-react 10，这是针对现代运行时和装饰器模型的清理版本。
- 📦 包体积显著减小：ESM 生产包 gzip 从 17.02 KiB 降至 13.96 KiB，最小 tree-shaken 示例为 10.32 KiB。
- 🔄 MobX 7 始终使用 Proxy 实现可观察对象和数组，移除了 ES5/非 Proxy 回退，不再支持 `configure({ useProxies })` 及 `proxy: false` 选项。
- 🏷️ 不再支持旧版装饰器，命名空间注解和比较器属性改为命名导出，例如 `observable.ref` → `observableRef`、`computed.struct` → `computedStruct`、`comparer.default` → `compareDefault` 等。
- 🕵️ 移除公共 `trace` API，调试请改用 `toJS`、`getDependencyTree`、`getObserverTree`、`spy` 或 `mobx-log` 包。
- ⚛️ mobx-react-lite 5 和 mobx-react 10 要求 MobX 7 和 React 18+；`mobx-react-lite` 支持函数组件和 `forwardRef`，`mobx-react` 在此基础上增加类组件及 Stage 3 `@observer` 类装饰器支持。
- ✂️ 如果不需要类组件支持，建议从 `mobx-react-lite` 导入函数组件，以减小打包体积；`mobx-react` 会将函数组件委托给 `mobx-react-lite`。
- 🧹 移除 React batching 相关导入（包括 React Native 深层导入），React 18+ 渲染器已自动处理 batching。
- 🎯 推荐公开的 React 绑定 API 为：`observer`、`Observer`、`useLocalObservable`、`enableStaticRendering`、`isUsingStaticRendering`。
- 🗑️ 移除 `Provider`、`inject`、`MobXProviderContext`，改用 `React.createContext`；同时移除 `disposeOnUnmount`、`PropTypes`、`useObserver`、`useLocalStore`、`useAsObservableSource`、`useStaticRendering` 及多个 batching 相关导出，并提供了对应替代方案。
- ⚠️ 废弃 `observer(fn, { forwardRef: true })` 和旧版函数组件 `contextTypes` 处理，请将已创建的 `React.forwardRef(...)` 组件传递给 `observer`。

---

### [](https://github.com/bytecodealliance/javy)

**原文标题**: [GitHub - bytecodealliance/javy: JS to WebAssembly toolchain · GitHub](https://github.com/bytecodealliance/javy)

Javy 是一个由 Bytecode Alliance 开发的 JavaScript 到 WebAssembly 工具链，它能在 Wasm 嵌入式运行时中执行 JavaScript，并生成体积可选的 Wasm 模块。
- 🧩 Javy 是 JS 到 WebAssembly 的工具链，属于 Bytecode Alliance 项目。
- 📏 动态链接可生成仅 1–16 KB 的超小 Wasm 模块；默认静态链接则至少 869 KB。
- 📥 预编译的 CLI 可从 GitHub Releases 页面直接下载。
- ✍️ 示例 JS 代码通过 `readInput` 从 stdin 读取 JSON，处理后在 `foo` 函数中转换数据，再用 `writeOutput` 输出到 stdout。
- 🛠️ 使用 `javy build index.js -o destination/index.wasm` 将 JS 编译为 Wasm 二进制。
- 🚀 可用 Wasmtime 等引擎执行，例如 `echo '{ "n": 2, "bar": "baz" }' | wasmtime index.wasm`，输出 `{"foo":3,"newBar":"baz!"}`。
- 📚 更多细节可查阅文档或运行 `javy --help`。

---

### [](https://nodejs.org/en/blog/release/v26.6.0)

**原文标题**: [Node.js — Node.js 26.6.0 (Current)](https://nodejs.org/en/blog/release/v26.6.0)

Node.js 26.6.0（Current）已于 2026 年 8 月 3 日发布，主要带来 FFI、测试运行器的新功能，以及大量依赖更新和问题修复。

- 🎯 新增 FFI 接口`getCurrentEventLoop`，用于获取当前事件循环。
- 🧪 测试运行器新增`context.log()`方法及`test:log`事件，便于在测试中输出日志。
- 📄 测试运行器在`TestStream`事件中新增`entryFile`字段，报告入口文件信息。
- 🔒 多项加密（crypto）修复：完善 RSA-PSS 密钥 DER 处理、清理私钥副本、限制 KangarooTwelveParams 长度等。
- ⚡ 优化事件模块，避免保留已移除的事件名，并改进`once()`和`removeListener()`性能。
- 🖥️ net 模块支持 BoundSocket 同步连接，并允许 TCP Server 和 Socket 跨工作线程转移。
- 🚀 大量流（stream）性能优化，包括使用环形缓冲区、改进背压机制和异步迭代速度。
- 📦 依赖升级：npm 升至 11.18.0、V8、zlib、c-ares、ngtcp2 等均有更新。
- 🐛 修复多个跨模块问题，如 Blob 流泄漏、HTTP/2 代理崩溃、QUIC 流处理等。
- 📝 文档大幅更新，新增协作者 MikeMcC399，并修正多处文档错误。
- 🔧 其他改进：为 RISC-V 启用 OpenSSL 汇编支持、提升文件系统匹配性能、修复 Windows 符号链接处理。
- 📥 提供 Windows、macOS、Linux、AIX 等全平台安装包与二进制下载。

---

### [](https://nodejs.org/en/blog/release/v24.19.0)

**原文标题**: [Node.js — Node.js 24.19.0 (LTS)](https://nodejs.org/en/blog/release/v24.19.0)

Node.js 24.19.0（代号 Krypton）作为 LTS 版本正式发布，带来多项新特性、性能优化与稳定性提升，覆盖 buffer、ESM、fs、http、net、perf_hooks、stream、tls 等模块，并更新了 OpenSSL 构建配置以支持压缩。
- ✨ buffer：实现 `blob.textStream()`，支持以文本流方式读取 Blob。
- 🔧 deps：更新 OpenSSL 构建配置以支持压缩，为 TLS 证书压缩等能力提供基础。
- 📦 稳定性：`blockList` 状态升级为候选发布（RC），`stream.compose` 标记为稳定。
- 🚀 ESM：新增 `--experimental-import-text` 实验标志，允许导入文本文件作为模块。
- 📁 fs：支持调用者提供缓冲区给 `readFile()`，减少内部内存分配开销。
- 🌐 http：新增 `httpValidation` 选项，用于配置请求头值验证行为。
- 🔌 net：`setKeepAlive()` 现在支持 TCP_KEEPINTVL 和 TCP_KEEPCNT 参数，便于精细控制 TCP 保活。
- ⏱️ perf_hooks：支持按事件循环迭代采样延迟，帮助更精确地诊断性能问题。
- ⚙️ src：允许空的 `--experimental-config-file` 文件，简化配置流程。
- 🔄 stream：暴露 `ReadableStreamTee`，便于流的复制与分流处理。
- 🔒 tls：新增报告协商后的 TLS 组功能，并支持 `certificateCompression` 选项（依赖 OpenSSL 压缩支持）。

---

### [](https://github.com/vitejs/vite/blob/v8.2.0/packages/vite/CHANGELOG.md)

**原文标题**: [vite/packages/vite/CHANGELOG.md at v8.2.0 · vitejs/vite · GitHub](https://github.com/vitejs/vite/blob/v8.2.0/packages/vite/CHANGELOG.md)

overview summary  
此内容为 Vite 官方仓库中 `packages/vite/CHANGELOG.md` 的 GitHub 页面截图，显示版本号为 v8.2.0，并提供了文件浏览、历史记录、原始代码下载等操作入口。页面当前存在加载错误提示，但核心信息为该版本更新日志文件的基本元数据。

- 📄 显示文件为 Vite 项目的 `packages/vite/CHANGELOG.md`，当前版本标记为 v8.2.0。  
- 🔢 文件共 2345 行，约 260 KB，包含该版本的完整变更记录。  
- 🧭 页面提供代码预览、Blame、历史记录、原始文件下载等 GitHub 标准操作。  
- ⚠️ 页面顶部有加载错误提示，并建议重新加载，但主体内容仍可访问。  
- 🔗 仓库地址为 `vitejs/vite`，公开显示 82.2k Star、8.6k Fork，以及多个后续导航标签（Issues、PR、讨论等）。

---

### [发布 v9.7.0 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.7.0)

**原文标题**: [Release v9.7.0 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.7.0)

概述：此版本为 react-three-fiber v9.7.0，主要聚焦于 reconciler 修复与增强，包括子元素重排同步、pierced props 重置、宿主 props 更新、实例重建批处理，以及对齐 react-dom 的事件优先级和微任务支持。

- 🔧 修复内部子元素在 React 重排后不同步的问题，避免细微 bug
- 🛠️ 修复 pierced prop 取消设置时错误重置为基类对象的问题
- ⚙️ 修复宿主 props（如 dispose、onUpdate）更新异常，以及命令式更新被意外覆盖的问题
- 📦 强化实例重建批处理，避免因 React.memo 等导致实例被忽略的边界情况
- ⏱️ 事件优先级对齐 react-dom，例如滚轮连续事件优先于指针脉冲事件
- 🧵 支持 reconciler 微任务，可根据优先级延迟处理工作
- 📝 附带多项文档更新、CI 调整及新贡献者加入

---

### [发布 v10.0.0 · lerna/lerna · GitHub](https://github.com/lerna/lerna/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · lerna/lerna · GitHub](https://github.com/lerna/lerna/releases/tag/v10.0.0)

Lerna v10.0.0 正式发布，带来多项破坏性变更、新功能和修复。核心变化包括：CI 模式下检测到远端落后会抛错、Lerna 改为纯 ESM 并提升 Node 版本要求、更新 conventional-changelog 依赖链，同时新增 bun 支持和多项稳定性修复。

- 🚨 CI 模式下若本地 checkout 落后于远端，版本管理和发布时将抛出 EBEHIND 错误；可通过 `--ci-behind-behavior` 或 `lerna.json` 中的 `command.version.ciBehindBehavior` 恢复旧行为。
- 📦 Lerna 现在仅提供 ESM 版本，最低 Node 版本要求提升至 22.13.0（支持 ^22.13.0、^24.0.0、^26.0.0）。
- 🔄 使用当前 conventional-changelog API 替换弃用的依赖，生成的 `CHANGELOG.md` 可能不同（空白规范化、标签 URL 编码），但仍兼容旧解析器/写入器选项和 Handlebars 模板。
- 🧹 移除 `p-map-series`、`p-pipe`、`p-reduce`、`p-waterfall` 以及 `upath` 依赖。
- 🔧 支持仅暴露 ESM import 条件的 changelog presets。
- 🔐 支持 CircleCI 上的 OIDC 可信发布。
- 📜 发布和 postpublish 生命周期脚本的输出会显示在终端。
- 🐰 新增 bun 作为受支持的包管理器。

---

### [发布 v4.13.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.13.0)

**原文标题**: [Release v4.13.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.13.0)

Hono v4.13.0 正式发布，重点提升了核心性能（最高 1.25 倍加速），新增了对 HTTP QUERY 方法的一流支持，并引入了 Method Not Allowed 中间件，同时包含多项中间件与 JSX 相关改进。

- 🚀 性能大幅提升：核心请求/响应路径经多项底层优化后，常见路由速度最高提升 1.25 倍（如 JSON 路由从 528ns 降至 422ns）。
- ⚡ 具体优化手段：跳过不必要的 Headers 分配、用 indexOf 替代正则测试、惰性分配内部状态、优化 URL 解码等。
- 🆕 新增 QUERY 方法支持：遵循 RFC 10008，可通过 `app.query()` 定义处理逻辑，请求体可作为查询条件。
- 🔄 内置中间件适配 QUERY：Cache 中间件按请求体哈希缓存，ETag 支持条件请求，CORS 默认允许 QUERY 方法。
- 🛑 新增 Method Not Allowed 中间件：路径匹配但方法不允许时返回 405 和 Allow 头，并支持自定义响应。
- 📦 RegExpRouter 改进：在路由注册时即检测不支持的路径并抛错，实现启动时快速失败，同时注册与首次匹配速度提升约 20%。
- 🧩 其他改进：headers 工具同步 IANA 注册表、JWT/JWK 中间件支持 realm 选项、JSX useRef 对齐 React 19、函数组件可返回数组等。

---

### [](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

**原文标题**: [
      Your SPA Is Leaking Memory. Soak Test It — Den Odell
    ](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

SPA 页面长期运行会像后端服务一样累积内存泄漏，文章介绍用 Playwright 浸泡测试在压缩时间内发现并定位这类问题。

- 🧠 后端团队常用浸泡测试（soak test）发现长时间服务的泄漏；SPA 因不刷新页面，同样需要这种测试。
- 📊 2026 年初对 500 个流行 React/Vue/Angular 仓库的分析显示，86% 存在监听器、定时器或订阅未清理的问题。
- ⚠️ 严重时团队只能定时强制刷新 SPA 来释放内存；Gmail 早在十多年前就在发布前用内存检查避免此类问题。
- 🛠️ 利用现有 Playwright 端到端套件可构建前端浸泡测试：在同一个浏览器上下文中循环执行用户流程，并比较前后内存指标。
- 📏 通过 Chrome DevTools Protocol（CDP）收集垃圾后读取指标，包括 JS 堆大小、DOM 节点数和事件监听器数。
- 🎯 断言时优先看节点数和监听器数，因为堆大小波动大；节点数可设置固定容差（如 100），监听器数则要求不增长。
- 🔁 soak() 函数先运行 5 次暖身（避免懒加载和缓存导致误报），再循环 200 次，最后对比基线和结束读数。
- ⏰ 定时器泄漏是最大问题（近 44% 来自 setTimeout）；用 page.clock.install() 和 runFor() 可快速模拟数小时定时器触发。
- 🌐 假时钟还需配合模拟网络（page.route），否则真实 fetch 响应会打乱定时器节奏，导致测试频率与真实不符。
- 📡 WebSocket 可用 page.routeWebSocket() 模拟；流式响应（如 AI 接口）较难处理，因为 route.fulfill() 只接受字符串或缓冲区。
- 🔍 若测试失败，可用 DevTools 堆快照并过滤“Detached”，查看哪些被移除的 DOM 节点仍被监听器或变量引用。
- 🌙 浸泡测试适合加入夜间自动化任务，能在代码合入前发现泄漏，而不是等用户报告页面越来越慢。
- 📘 这种“提前测试性能问题”的思路是作者新书《Fast by Default》的核心实践之一。

---

### [你的 JSON 在骗你](https://blog.gaborkoos.com/posts/2026-08-03-Your-JSON-Is-Lying-to-You/)

**原文标题**: [Your JSON Is Lying to You](https://blog.gaborkoos.com/posts/2026-08-03-Your-JSON-Is-Lying-to-You/)

JSON 并非无损的 JavaScript 对象快照；`JSON.stringify` 与 `JSON.parse` 组合会悄悄改变数字精度、删除 `undefined`、把 `Date` 变成字符串、把 `NaN` 变成 `null`，还会丢失原型与类型信息。文章强调必须把 JSON 视为一种经过明确转换的交换格式，在跨进程传输前定义清晰的 wire shape、校验输入，并对特殊值采用显式编码。

- 🔢 大整数在序列化前后都会失真：`9007199254740993` 会因 IEEE 754 精度限制变成 `9007199254740992`，`JSON.parse` 同样会丢失精度，`BigInt` 则直接抛出 TypeError。
- 📌 安全传输大整数的最佳做法是使用十进制字符串表示，例如 `"id": "9007199254740993"`，并由 schema 明确该字段为数字字符串。
- 🚫 `undefined` 在对象属性中会被直接删除，在数组中会变成 `null`，顶层序列化则返回 `undefined`；这会让“属性不存在”和“属性值为 undefined”在 JSON 中无法区分。
- ⚠️ 若 API 需要区分“不更新”和“清除字段”，应显式使用 `null` 或约定字段，而不是依赖 `undefined` 保留语义。
- 📍 JavaScript 中对象键顺序稳定且可预测，但 JSON 规范认为对象成员无序；其他语言运行时可能不保持顺序，因此有顺序含义的数据应改用数组。
- 🔐 签名、哈希、缓存键等依赖字节级比较的场景，需要统一 canonical JSON 规则，否则属性顺序或空白差异会导致相同对象产生不同字节。
- 🧬 JSON 会擦除类型：`Date` 变成 ISO 字符串，`Map`/`Set`/`RegExp`/`Error` 变成空对象，`NaN`/`Infinity` 变成 `null`，类型数组和类实例失去原型与方法。
- 🕰️ `Date` 序列化后只保留 UTC 字符串，原始时区偏移和墙钟时间丢失；解析后无法自动恢复为 `Date`。
- ⚙️ `JSON.stringify` 会调用 `toJSON()`、触发 getter，并执行 replacer 函数，因此序列化可能带来副作用、抛错或改变输出，不能只当作静态读取。
- 🔁 JSON 无法表达对象身份：共享引用解析后会变成独立副本，循环引用会抛出 `TypeError: Converting circular structure to JSON`。
- 👻 只有可枚举的字符串键自有属性会被序列化；原型方法、非枚举属性、symbol 键和私有字段都会丢失。
- 🛡️ `JSON.parse` 本身不会导致原型污染，但后续递归 merge 等操作可能把 `__proto__`、`constructor` 当作危险路径；应使用 schema 白名单过滤意外字段。
- 📏 解析前的资源限制很重要：超大或极度嵌套的 JSON 会消耗大量内存/CPU，应在 `JSON.parse` 前限制请求体大小、嵌套深度和集合数量。
- 🏷️ reviver 不会自动恢复类型；用 `$type` 标签显式标记类型是可靠做法，但不要把所有 ISO 字符串都当作 `Date`，否则会误改普通文本。
- 📦 实践建议：为每个边界定义 wire shape（传输对象），在解析后用 Zod/Valibot/TypeBox 等运行时校验，并为异常值设计明确编码。
- 🧪 测试应覆盖完整收发链路：不仅验证生产者输出的字符串，还要验证接收方运行时的解析结果，例如跨语言测试大整数与签名字节。
- 🔄 当数据模型需要二进制、类型化字节串或更宽数值范围时，可考虑 MessagePack 或 CBOR，但仍需双方明确约定扩展与标签。
- ✅ 结论：JSON 没有坏，问题在于把最小交换格式当作 JavaScript 状态的无损克隆；`JSON.parse(JSON.stringify(value))` 是转换而非通用深拷贝。

---

### [富达技术类职位 | 富达职业](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-nl1-s)

**原文标题**: [Technology careers at Fidelity | Fidelity Careers](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-nl1-s)

富达的科技职业页面展示了这家财富 500 强企业以创业心态推动金融科技创新，强调人才发展、技能培养与多元岗位机会，并邀请技术人才加入以共同定义金融的未来。

- 💼 富达科技岗位致力于重新定义金融未来，推动有影响力的创新，并帮助员工开启职业旅程。
- 🏢 在创业心态与财富 500 强基础之上，持续投资创新并兑现数字化未来的承诺。
- 📊 拥有数千名技术员工，2023 年有相当比例的员工承担了全新或扩展的职责，并获得多项美国专利。
- 🤝 员工评价富达最棒之处在于人与人之间的充分互动与协作。
- 📌 当前开放岗位涵盖技术总监、代币化与分布式账本产品负责人、软件工程总监等，工作地点分布在北卡、德州、新泽西等地。
- 🛠️ 重点招募技能包括软件工程、全栈工程、云工程、数据可视化、人工智能与机器学习、架构、系统工程及系统分析。
- 📚 每周设有专门学习时间，技术人员可通过线上课程、职业辅导、导师跟岗等方式持续更新技能。
- 🔍 提供职位搜索功能，并有更多关于技术职业及加密相关职业的信息供进一步了解。

---

### [](https://blog.cloudflare.com/cdnjs-dev-platform-migration/)

**原文标题**: [Dogfooding at scale: migrating cdnjs to Cloudflareâs Developer Platform | The Cloudflare Blog](https://blog.cloudflare.com/cdnjs-dev-platform-migration/)

overview summary  
cdnjs 是互联网上最繁忙的开源 CDN 之一，现已完全迁移至 Cloudflare 开发者平台。此次迁移解决了旧架构的观察性、存储分裂、流水线脆弱等问题，并借助 Workers、Workflows、R2、KV、Queues 等组件构建了全新架构，同时突破了平台限制并惠及所有用户。

- 📈 cdnjs 规模巨大：服务全球约 12% 的网站，平均每秒 10.8 万次请求，每日 90 亿次，缓存命中率 98.6%。
- 🤖 LLM 助力流量：ChatGPT、Claude 等 AI 工具在生成 HTML 演示时频繁引用 cdnjs，其不可变版本与 SRI 哈希使其成为可靠依赖。
- 🚨 旧架构痛点：缺少统一追踪、存储分裂（KV 与 GitHub 双源）、对象事件粘合流水线、26 个字母分片函数、GitHub 仓库过大无法服务。
- 🏗️ 新架构设计：R2 作为文件内容唯一事实来源，KV 仅存元数据，Workers Cache 前置缓存，DigitalOcean 作为灾备镜像。
- ⚙️ 流水线重构：基于 Cloudflare Workflows 实现持久执行，每 10 分钟检查更新，按包/文件粒度拆分子工作流，支持失败恢复。
- 🧩 容器辅助压缩：预压缩逻辑因内存需求暂用外部 Rust 压缩容器，通过 Queue 与 R2 事件通知衔接，未来计划改为流式处理。
- ⏳ 迁移挑战：避免重新处理文件导致 SRI 哈希不匹配，改为原样从 KV 复制到 R2，并通过 Queues 分片迁移确保不遗漏。
- 🔓 平台限制突破：迁移中遇到单次 Worker 1000 子请求限制与 Workflow 1024 步限制，推动平台提升至 1000 万子请求与 10,000（可配 25,000）步。
- 🔮 未来展望：新架构为未来支持 ES Modules 等现代浏览器原生模块提供了可能，但仍需进一步评估。

---

### [](https://cdnjs.com/)

**原文标题**: [cdnjs - The #1 free and open source CDN built to make life easier for developers](https://cdnjs.com/)

cdnjs 是一个免费、开源的 CDN 服务，由 Cloudflare 提供支持，旨在帮助网站更快速、更轻松地加载库文件，并鼓励社区贡献与捐助以维持可持续发展。

- 🌐 免费且开源：cdnjs 是开放源码的 CDN 服务，供所有网站免费使用。
- 📊 广泛采用：全球超过 12.5% 的网站信任并使用 cdnjs。
- 🚀 海量请求：每月处理超过 2000 亿次请求，性能表现极佳。
- ⚡ 提速加载：借助 Cloudflare 网络，让库文件的加载更快、更简单。
- 🤝 社区支持：可通过 GitHub 参与贡献，帮助 cdnjs 保持可持续发展。
- 💰 捐助渠道：也可通过 Open Collective 或 Patreon 捐赠 5 美元支持项目。

---

### [](https://healeycodes.com/adding-defer-to-the-typescript-compiler)

**原文标题**: [Adding Go's defer to the TypeScript Compiler — Andrew Healey](https://healeycodes.com/adding-defer-to-the-typescript-compiler)

将 Go 的 defer 语句加入 TypeScript 编译器是一次有趣的实验，但实现后反而让人确信它并不适合 TypeScript；文章还探讨了替代方案 Explicit Resource Management。

- 🧪 作者尝试为 TypeScript 编译器添加 Go 风格的 `defer`，通过 AST 树重写实现，无需新增工具链。
- ⚙️ TypeScript 编译器本身已支持语法识别与替换，例如 ES5 下 class 会被重写为函数，因此 `defer` 可复用这套机制。
- 📝 实现步骤包括：让解析器识别 `DeferStatement`、做语法检查（如必须位于函数体内、操作数必须是调用表达式）、复用普通调用检查。
- 🎯 为匹配 Go 语义，`defer` 会立即捕获 callee、receiver 和参数值；即使后续方法被重新赋值，也会调用原始方法。
- 📚 包含 `defer` 的函数会生成一个栈，执行到 `defer` 时压入闭包，函数退出时按后进先出顺序执行清理。
- ⏳ 注册发生在执行到 `defer` 时，而非函数开始；因此 `if` 或循环中的 `defer` 只在对应分支或迭代中生效。
- 🔄 转换后的代码使用 `try/finally` 实现，在异步函数中会依次 `await` 每个清理操作；`defer await` 会被直接拒绝。
- ⚠️ 错误处理很复杂：所有 deferred 调用都会执行、保留原始错误、多个错误时用 `AggregateError` 聚合；Go 中错误是值，而 JS 异常是控制流。
- ❌ 实现过程中发现 `defer` 不属于 TypeScript：一旦清理函数可能抛错或拒绝，就需要定义聚合、优先级和异步执行策略，这些 Go 并不需要。
- 💡 更好的替代方案是 ECMAScript Explicit Resource Management（`using` 声明），例如借助 `Disposable` 对象在作用域结束时自动释放资源。
- 🔧 作者的 MVP 实现可在其 TypeScript fork 分支中找到。

---

### [](https://www.totaltypescript.com/typescript-5-2-new-keyword-using)

**原文标题**: [TypeScript 5.2's New Keyword: 'using' | Total TypeScript](https://www.totaltypescript.com/typescript-5-2-new-keyword-using)

TypeScript 5.2 引入了新的 `using` 关键字，用于自动释放实现了 `Symbol.dispose` 的资源，并支持异步版本 `await using`，可简化文件句柄、数据库连接等资源的管理，基于已进入 Stage 3 的 TC39 提案。
- 🆕 `using` 关键字：在变量离开作用域时自动调用其 `Symbol.dispose` 方法，实现资源清理。
- 🔑 `Symbol.dispose`：新的全局符号，任何对象只要拥有该属性函数，即可被视为“资源”。
- ⏳ `await using` 与 `Symbol.asyncDispose`：用于需要异步释放的资源（如数据库连接），确保释放完成后再继续执行。
- 📁 文件句柄示例：使用 `using` 可避免手动 try/finally 关闭文件，代码更简洁可靠。
- 🗄️ 数据库连接示例：通过 `await using` 实现连接自动关闭，类似 C# 中的 `using` 用法。
- 🚀 该提案已进入 Stage 3，适合早期采用者测试，未来有望成为 JavaScript 标准特性。

---

### [学习 Remix 3 | Malstrom.me](https://malstrom.me/blog/learning-remix-3)

**原文标题**: [Learning Remix 3 | Malstrom.me](https://malstrom.me/blog/learning-remix-3)

overview summary  
Remix 3 目前处于 beta，本文以「未打包（unbundled）」架构展示其核心特性：集中式路由、Frames 流式渲染、服务端优先的数据加载、按需水合、借助浏览器原生 API 实现乐观更新与精细 pending 状态。作者将 Solid 2.0 的演示应用移植到 Remix 3，通过一个 issue 浏览器示例，逐步实现侧边栏导航、注释加载、表单提交、乐观评论计数及界面淡入淡出等交互，强调 Remix 的「batteries-included」且不依赖构建工具的灵活设计。

- 🔧 Remix 3 当前为 beta 版，API 在稳定版前可能变化；演示应用采用「unbundled」架构，使用 Node 运行时加载器按需转译 TS/TSX，无需打包器。
- 📦 项目依赖极简，仅需 `remix` 包作为运行时依赖，配合 Node 原生 TypeScript 支持及少量开发依赖，脚本通过 `remix/node-tsx` 运行。
- 🗂️ 路由通过集中式 `app/routes.ts` 定义，支持 `route`、`resources`、`get`、`post` 等 DSL，并提供类型安全的 `href` 构建器。
- 🖼️ 引入「Frames」机制：页面可拆分为独立帧，服务端根据 `X-Remix-Target` 头返回对应组件，通过 `<Frame>` 嵌套实现类似嵌套路由的流式渲染。
- 💧 组件默认仅服务端渲染；使用 `clientEntry()` 包装组件后，Remix 会按需将对应 JS 发送到浏览器，实现定向水合，类似 Astro 的岛屿架构。
- 🧩 Remix 组件分为 setup scope 与 render scope：setup 只运行一次，render 函数在更新时重新执行，使用普通变量、闭包和手动 `update()` 管理状态，而非 hooks 或 signals。
- 🗄️ 数据层内置 SQLite 支持：通过 `remix/data-table` 定义表结构、执行 CRUD 与查询，`remix/data-schema` 提供 Standard Schema 兼容的校验，迁移脚本内置 `up/down`。
- 🧭 导航通过 `link()` mixin 实现，可指定目标 frame 和滚动行为；侧边栏高亮通过监听 Navigation API 的 `currententrychange` 完成，但需等待 transition 结束以避免撕裂。
- ⏳ 加载边界：将评论列表拆分为独立 frame 并懒加载，使用 `<Frame fallback>` 显示占位 UI；但等待整个 transition 完成会导致高亮滞后，需要更精确的事件机制。
- ✍️ 表单提交使用 `formData()` 中间件和 `navigate()` 重新验证目标帧；无 JS 时优雅降级为原生 POST，有 JS 时手动 fetch 后局部刷新。
- ⚡ 乐观更新：利用 frame handle 作为事件通道，在提交时立即插入临时评论（负 id 显示「Saving...」），待服务器响应并 reload 后释放；手动编排所有状态，不需框架特殊原语。
- 🔢 乐观评论计数：通过 `window` 上的自定义 `CommentCountEvent` 广播实时评论数，Sidebar 卡片监听事件后更新，兼顾乐观值与服务器最终值。
- 📣 显示议题通知：新增 `IssueShownEvent`，在评论组件渲染时广播当前 issueId，侧边栏据此即时高亮，取代了原先复杂的 URL 匹配和 transition 等待逻辑。
- 🌫️ Pending 淡入淡出：组合 `link()` 与 click 监听器，在导航时降低卡片和详情面板透明度；通过 `QueueTask` 获取 Frame handle，监听 `reloadStart`/`reloadComplete`，并利用 `issueshown` 在渲染瞬间精准结束 pending 状态。
- 🎯 文章总结：借用浏览器原生事件、Frame 生命周期和极简状态管理，即可在 Remix 3 中实现与 Solid 2.0 同级别的现代交互体验，充分体现框架的开放性与灵活性。

---

### [为什么 npm 依赖树如此庞大 | Andrew Nesbitt](https://nesbitt.io/2026/07/28/why-npm-dependency-trees-are-so-big.html)

**原文标题**: [Why npm Dependency Trees Are So Big | Andrew Nesbitt](https://nesbitt.io/2026/07/28/why-npm-dependency-trees-are-so-big.html)

npm 依赖树庞大的根源在于其解析策略：与 Bundler 强制单一版本不同，npm 允许同一包的多版本共存，使约束冲突不再成为维护者的沟通成本，从而放任依赖无限膨胀。

- 📦 npm 的模块加载基于文件路径而非包名，不同版本的同一包可分别安装在各自的 node_modules 目录中，互不干扰。
- ⚖️ Bundler 强制整个应用共享每个 gem 的唯一版本，约束冲突会导致安装失败，因此维护者被迫保持宽泛版本范围并相互协作。
- 🆓 npm 中依赖约束对作者毫无代价，即使固定精确版本也不会导致下游安装失败，微包依赖习惯因此繁荣。
- 🌳 代价转移至整个生态系统：2017 年 npm 已是最大且增长最快的依赖网络，平均安装一个包需信任 79 个包和 39 位维护者。
- 🔁 重复副本会破坏模块级单例状态（如 React 的 hooks），peerDependencies 用于强制共享版本，但 npm 7 的强制执行曾引发争议，催生 --legacy-peer-deps 逃生口。
- 🦀 Cargo 采用混合策略：semver 兼容范围内像 Bundler 一样统一版本，不兼容范围则像 npm 一样允许多副本；0.x 的 caret 规则导致大量 crate 落入多版本阵营。
- 🧩 Rust 生态中，serde 等基础 crate 长期坚守 1.x 以避免分裂，但宽松侧同样存在重复：一个小型 demo 项目就出现 141 个 crate 及多个重复主版本。
- 💡 结论：依赖树的大小由解析器的容错方式决定，npm 用复制而非协调解决冲突，这正是其依赖树持续膨胀的根本原因。

---

### [TanStack 图表](https://tanstack.com/charts/latest)

**原文标题**: [TanStack Charts](https://tanstack.com/charts/latest)

TanStack Charts 是一个基于图形语法的现代图表库，当前版本 0.3.1。它强调类型安全、声明式 API 和小体积，支持从简单折线到复杂交互的多种图表，并可通过主题与样式轻松定制，适用于人类与 AI 代理。

- 📦 已发布 npm 0.3.1；紧凑 React 折线图 gzip 后 16.48 KiB，框架无关场景仅 8.12 KiB。
- 🧩 提供覆盖趋势、柱状、分布、层级、地理、网络、极坐标、交互等大量示例，展示多样化的图表表达能力。
- 🛡️ 严格 TypeScript 编译，字段、数据类型、域、键、工具提示与回调均与源数据安全关联，拒绝无效定义。
- ⚙️ 声明式 API（如 `defineChart` 和 marks），支持图层共享坐标系统，面积、规则、线、点、标签可自由组合。
- 🎨 通过 CSS 变量、主题、标记属性、自定义工具提示或自绘渲染器，轻松让图表匹配产品视觉风格。
- 📉 冷页面打包对比：TanStack Charts 仅 26.6–32.1 KiB，明显小于 Chart.js、Observable Plot、Recharts、ECharts 等竞品。
- 📚 构建在 Leland Wilkinson 的图形语法之上，并借鉴 ggplot2、Vega-Lite 与 Observable Plot，但运行时为独立实现。
- 🤝 设有黄金/白银/青铜合作伙伴及 OSS 赞助商，赞助商可享私人 Discord 频道、优先 issue 处理和直接支持。

---

### [比较库 | TanStack Charts 文档](https://tanstack.com/charts/latest/docs/comparison)

**原文标题**: [Compare Libraries | TanStack Charts Docs](https://tanstack.com/charts/latest/docs/comparison)

TanStack Charts 对比文档概述了其与 Chart.js、ECharts、Recharts、Observable Plot 等库的架构差异、内建能力、包体积、许可模式及选型建议，并给出了可复现的基准测试方法和一致性语料规模。

- 📌 对比基于固定版本：TanStack Charts 0.6.5（workspace 11ba458）、Chart.js 4.5.1、ECharts 6.1.0、Recharts 3.10.1、Observable Plot 0.6.17
- ✅ TanStack Charts 内建轴/网格、图例、指针 tooltip、多系列、选择（onSelect）、动画与响应式调整，无需额外插件
- 📊 其他库（如 D3、Chart.js、ECharts、Recharts）部分能力需借助插件、外部组合或宿主布局，并非全部开箱即用
- 📦 包体积方面，TanStack Charts 受控测试约 28.71–34.14 KiB，小于 Chart.js（44.70–58.21 KiB）和 ECharts（153.10–173.18 KiB）等；uPlot 最小但能力更基础
- ⚖️ 许可上 TanStack Charts 为 MIT，ApexCharts/Highcharts 有商业使用限制，AG Charts 为社区版 + 付费企业版
- 🏛️ 框架中立：TanStack Charts 采用核心 + 适配器，支持默认 SVG 和可选 Canvas/WebGL，而 Recharts、visx、Nivo 仅限 React
- 🛠️ TanStack 将分箱、分组、缩放、刷选、数据获取等明确留给应用层或 D3 模块，不纳入默认运行时，强调显式所有权
- 🧩 选型建议：Canvas 标准图选 Chart.js，广谱图表选 ECharts，React SVG 组件选 Recharts，探索性标记选 Observable Plot，类型化跨框架组合选 TanStack Charts
- 🔍 一致性语料含 109 个 TanStack/参考库对比对（75 个源自 Observable Plot、23 个 Recharts、11 个 ECharts），含可执行交互场景
- 🧪 复现命令提供 pnpm benchmark:size、benchmark:check、benchmark:stress:quick、conformance:quick，并需固定 Playwright 浏览器版本

---

### [](https://github.com/Agent-Field/pr-af)

**原文标题**: [GitHub - Agent-Field/pr-af: #1 open-source code reviewer on Code-Review-Bench · GitHub](https://github.com/Agent-Field/pr-af)

PR-AF 是一个基于 AgentField 的开源智能代码审查工具，在 Martian Code-Review-Bench 基准上排名开源第一。它采用动态多代理流水线，根据每个 PR 定制审查计划，以证据根基和复合漏洞分析为核心，同时大幅降低审查成本。

- 🏆 在 Martian Code-Review-Bench 上以 0.706 golden recall 排名开源第一（超过 42 个对比工具）
- 🔍 比领先商业工具多发现约 3 倍真实问题（595 个独立有效发现）
- 🧠 动态编译审查维度，为每个 PR 生成专属审查计划并临时创建聚焦审查代理
- ⚙️ 通过 AST 提取与调用链验证，配合可证伪性门过滤无证据或已缓解的发现
- 🔗 复合漏洞合成：跨文件聚类相关风险，识别孤立问题背后的系统性威胁
- 💸 每次审查成本约为闭源工具的 1/10，支持 DeepSeek、GLM-5.2、Opus 等模型灵活切换
- 🚀 一键调用：支持 af CLI、curl API 或 GitHub Actions 零配置触发，并自动发布内联评论
- 📦 提供 Docker Compose 与 Railway 一键部署，支持自托管 API 和完整基准复现脚本
- ⏱️ 执行时间约 35-50 分钟，适合深度 CI/CD 架构审计而非快速交互式审查
- 🌐 属于 AgentField 生态，相关项目还有 SWE-AF 和 SEC-AF 等自动化工厂
- 🛡️ 误报率极低，所有发现均附带文件、行号、建议和证据来源

---

### [](https://github.com/AsyncBanana/microdiff)

**原文标题**: [GitHub - AsyncBanana/microdiff: A fast, zero dependency object and array comparison library. Significantly faster than most other deep comparison libraries and has full TypeScript support. · GitHub](https://github.com/AsyncBanana/microdiff)

overview summary
Microdiff 是一个极简、高速、零依赖的 JavaScript 对象与数组比较库，支持 TypeScript，并可在多种运行环境使用；它提供简单统一的 diff() 接口，支持循环引用，性能显著优于同类库，并附带完整测试与基准测试。

- 🚀 性能极佳：比多数对象 diff 库快两倍以上，无循环模式下更快
- 📦 体积极小：压缩后不足 1kb，且零依赖
- 🌎 环境兼容：支持 Deno、Node、Bun、Web 与 Service Worker，自带 TypeScript 类型
- 🔰 使用简单：仅需调用单个 diff(obj1, obj2) 函数即可比较对象差异
- 📅 类型全面：完整支持 Date、RegExp 等特殊对象
- 🧩 返回三种变更类型：CREATE、REMOVE、CHANGE，包含 path、value、oldValue 等属性
- 🔄 循环引用支持：默认开启，也可通过 cyclesFix: false 关闭以提升性能
- 📊 基准测试：提供 bench.js 供用户自行运行，结果仅供参考
- 🤝 贡献指南：可 fork 仓库、运行 npm run build / bench / test，并需阅读行为守则
- 📄 开源许可：MIT license，托管于 GitHub，拥有 3.8k star 和 82 fork

---

### [](https://github.com/inokawa/virtua)

**原文标题**: [GitHub - inokawa/virtua: A zero-config, fast and small (~3kB) virtual list (and grid) component for React, Vue, Solid, Svelte and Angular. · GitHub](https://github.com/inokawa/virtua)

概述总结：virtua 是一个零配置、快速且小型的虚拟列表（和网格）组件，支持 React、Vue、Solid、Svelte 和 Angular，旨在提供最佳性能而无需复杂配置，并自动处理动态尺寸测量、滚动位置调整等实际难题。

- ✨ 零配置：开箱即用，内置处理动态尺寸、反向滚动、iOS 滚动、命令式滚动等复杂场景
- ⚡ 高性能：优化 CPU 占用和 GC、减少同步布局重排与视觉跳动，并针对 JIT 和框架特性进行优化
- 📦 体积小：每个组件约 3kB gzipped，且支持 tree-shaking，对现代 Web 开发友好
- 🔄 灵活多用：支持固定/动态尺寸、水平/反向/RTL 滚动、移动端、无限滚动、滚动恢复、DnD、键盘导航、sticky 等丰富场景
- 🌍 框架无关：已支持 React、Vue、Solid、Svelte、Angular，未来可能扩展更多框架
- 🛠 安装简单：npm install virtua；旧浏览器若无 ResizeObserver 需使用 polyfill
- 📚 多种用法示例：提供垂直/水平滚动、自定义 Virtualizer、Window 滚动、二维网格（实验性 VGrid）等代码示例
- 🧠 性能优化技巧：复杂场景下可使用 useMemo、memo 或 memoize 的 render prop 减少重渲染，降低 bufferSize 也可能有效
- ❓ 常见问题解答：item 必须传唯一且稳定的 key（避免用索引，尤其开启 shift 时）；ResizeObserver 报错可安全忽略；TS 需用 moduleResolution: bundler/nodenext 以解析多框架入口
- 📊 功能对比：相比 react-window、react-virtualized 等，virtua 在动态尺寸、反向滚动、无限滚动、窗口滚动、SSR 和 RSC 支持等方面内置更好，部分高级功能仍需自定义
- 🤝 开源贡献：欢迎提交 Issue、PR 和参与 Discussions，项目使用 MIT 许可证

---

### [故事书 - Storybook](https://inokawa.github.io/virtua/?path=/story/basics-vlist--default)

**原文标题**: [storybook - Storybook](https://inokawa.github.io/virtua/?path=/story/basics-vlist--default)

您似乎还没有提供需要总结的文章内容。请发送文本，我会按照以下模板为您生成中文摘要：

overview summary
- Emoji 要点

请提供内容后，我会立即为您总结。

---

### [](https://github.com/inokawa/virtua#comparison)

**原文标题**: [GitHub - inokawa/virtua: A zero-config, fast and small (~3kB) virtual list (and grid) component for React, Vue, Solid, Svelte and Angular. · GitHub](https://github.com/inokawa/virtua#comparison)

overview summary  
virtua 是一个零配置、快速且体积小（约 3kB）的虚拟列表/网格组件库，支持 React、Vue、Solid、Svelte 和 Angular，旨在提供最佳性能并处理现实世界中的复杂滚动场景。

- 🎯 核心定位：零配置虚拟化，自动处理动态尺寸测量、反向滚动、iOS 支持等难题。
- ⚡ 性能优化：通过减少 CPU 占用、降低同步布局重排、优化 CSS 等方式实现流畅滚动。
- 📦 轻量级：每个组件约 3kB（gzipped），支持 tree-shaking。
- 🧩 灵活多用：支持固定/动态尺寸、横向滚动、反向滚动、RTL、移动端、无限滚动、滚动恢复、拖拽、键盘导航等。
- 🌐 多框架支持：提供 React、Vue、Solid、Svelte 和 Angular 适配器。
- 🚀 快速上手：安装 `npm install virtua`，旧浏览器需 ResizeObserver polyfill。
- 📚 组件示例：提供 VList（垂直/水平滚动）、Virtualizer（自定义标记）、WindowVirtualizer（窗口滚动）、experimental_VGrid（网格）等用法。
- 🔧 性能调优：可使用 useMemo 或 render prop 缓存元素，减少重渲染；必要时减小 bufferSize 或为图片设置固定高度。
- ⚠️ 常见问题：ResizeObserver 错误可安全忽略；项目必须传唯一 key；moduleResolution 需设为 bundler 或 nodenext。
- 📊 对比优势：在功能覆盖、动态尺寸、反向滚动、无限滚动、滚动恢复、SSR 支持等方面优于多数替代库（如 react-window、react-virtualized 等）。
- 🤝 开放贡献：欢迎提交 Issue、PR，参与讨论，支持通过 fork 和 CI 检查参与开发。

---

### [视角](https://perspective-dev.github.io/)

**原文标题**: [Perspective](https://perspective-dev.github.io/)

概述：Perspective 是一个交互式分析与数据可视化组件，专为大型或流式数据集设计，支持浏览器、Python 和 JupyterLab 等多种部署方式，具备高性能查询引擎与灵活的 UI 集成能力。

- 🚀 提供基于 C++ 编写的高性能流式查询引擎，可编译为 WebAssembly 和 Python，支持 Apache Arrow 读写及流式处理。
- 🧩 采用框架无关的 Custom Element 用户界面，可通过 WebAssembly 在浏览器本地运行，或通过 WebSocket 连接 Python/Node 服务端。
- 📓 提供 JupyterLab 组件与 Python 客户端库，适用于 notebook 交互分析及可扩展的 Voila 生产应用。
- 🌐 基于 Perspective.js 的 Custom Element 可轻松集成到任意 Web 框架，通过简单查询语言实现 API 与用户交互的对称配置。
- 🔄 工作区可混合虚拟服务端 Python 数据与浏览器端数据，支持数据视图的交叉筛选、复制、导出、堆叠与保存。
- ⚡ 借助 WebAssembly 实现极速查询计算，并通过 Apache Arrow 保持低内存占用与高效数据序列化，达到桌面级性能。
- 🐍 perspective-python 基于同一 C++ 数据引擎，可作为生产环境虚拟化服务器，或作为嵌入式 JupyterLab 组件用于研究。
- 📊 虚拟化的 perspective-viewer 仅渲染当前屏幕所需数据，支持超大数据集瞬时加载；也可通过 Arrow 高效流式传输完整数据集，减轻服务器负担。
- 🔬 面向研究人员与数据科学家，PerspectiveWidget 作为 Jupyter/JupyterLab 组件，支持 Pandas 与 Apache Arrow 数据的交互式可视化。

---

### [](https://github.com/perspective-dev/perspective/pull/3207)

**原文标题**: [Window columns by texodus · Pull Request #3207 · perspective-dev/perspective · GitHub](https://github.com/perspective-dev/perspective/pull/3207)

overview summary  
- 🧱 此 PR 为 Perspective 引擎、虚拟服务器（DuckDB、Clickhouse、Polars）及 `<perspective-viewer>` UI 新增「窗口列」支持。  
- ⚙️ 新增 `ViewConfig` 的 `windows` 字段，支持 `sum`、`avg`、`count`、`min`、`max`、`stddev`、`var`、`lag/lead`、`diff`、`rate`、`ema` 等聚合函数。  
- 📐 窗口帧类型包含 `"rows"`、`"range"`、`"cumulative"`，并可搭配 `partition_by` 与 `order_by`（升序/降序）。  
- 🔗 窗口列与表达式列行为一致，排序、筛选、透视及更新过渡均可正常运作。  
- 📝 文中提供三个示例配置：10-tick 平均窗口、5 秒平均窗口（含 `order_by`）、累计求和窗口。  
- 🐛 此 PR 同时修复了「导出 PerspectiveWidget 至静态 HTML 失败」的问题（#2846）并补充相应测试。  
- ✅ PR 合并了 6 个提交，包含窗口函数实现、UI 修复、Cargo 警告修复等，最终合并至主分支。

---

### [](https://github.com/neutralinojs/neutralinojs/releases/tag/v6.9.0)

**原文标题**: [Release Neutralinojs v6.9.0 released! · neutralinojs/neutralinojs · GitHub](https://github.com/neutralinojs/neutralinojs/releases/tag/v6.9.0)

Neutralinojs v6.9.0 正式发布，新增多项 API 和功能，并更新了版本配置。

- 🌐 新增基于 C++ 的 net API，提供 get、post、put、patch、delete、options、head、request 等网络请求方法，帮助应用绕过 CORS 限制。
- 💽 computer API 新增 getDisks()，可获取磁盘的厂商、型号、挂载点、容量、剩余空间和序列号等信息。
- 🖥️ computer API 新增 getMachineId()，用于获取平台特有的机器唯一标识。
- ⚙️ app API 新增 getProcessId()，可获取应用进程 ID。
- 🔧 os API 新增 setEnv(key, value)，支持更新进程环境变量。
- 🌍 os API 新增 getLocaleInfo()，可获取当前区域设置的完整信息，包括未解析区域、解析后的地区和语言。
- 📦 更新配置文件中的 cli.binaryVersion 为 6.9.0，运行 neu update 即可获取该版本。

---

### [](https://github.com/amol-/dukpy/releases/tag/0.6.0)

**原文标题**: [Release 0.6.0 · amol-/dukpy · GitHub](https://github.com/amol-/dukpy/releases/tag/0.6.0)

DukPy 0.6.0 是一次重大版本更新：JavaScript 引擎从 Duktape 迁移至 QuickJS-NG，新增文件运行接口并支持现代 ESM，同时移除若干旧功能和兼容层，并提高 Python 版本要求至 3.9+。

- 🚀 引擎迁移到 QuickJS-NG v0.11.0，支持现代 JavaScript 语法及原生 Promise/任务队列
- 🆕 新增 `dukpy.run(path, **kwargs)` 和 `JSInterpreter.run(path, **kwargs)`，CLI 改用文件运行器
- 📦 `run()` 支持 ESM 静态 `import`/`export`、`import.meta.url`、`import.meta.main` 和顶层 `await`，并按 Node 风格区分 `.mjs`、`.cjs`、`.js`
- 🔧 CommonJS 运行时支持 `require`、`module`、`exports`、`__filename`、`__dirname`，缓存与 ESM 互通，失败模块可重试
- 🔄 ESM 可导入 CommonJS：默认导出为 `module.exports`，仅命名导出 `module`、`exports`、`require`
- 🛡️ Promise 微任务在结果序列化前排空，失败时抛出 `JSRuntimeError`；堆栈耗尽、超大分配和阻塞式 `Atomics.wait` 均有安全处理
- 🐍 Python 回调保留参数顺序和 JSON 类型，支持 Unicode 名称/值，`None` 返回映射为 `undefined`，异常转为可捕获的错误
- 🎨 结果转换对齐 `JSON.stringify`：`null`、`undefined`、`NaN`、无穷值映射为 `None`；循环引用和 BigInt 失败时抛出运行时错误
- 📦 npm 安装器强制 HTTPS，并拒绝不安全 tar 路径、路径遍历、符号链接逃逸等；TypeScript 升级至 5.7.3
- ❌ 移除通用 Babel 支持、CoffeeScript、Duktape 全局对象和旧模块系统
- 🐍 最低 Python 版本提高到 3.9，删除 Python 2 兼容代码；旧 `dukpy/run.py` 模块移除，需改用 `dukpy.run()`
- ⚠️ `evaljs()` 仍仅支持脚本，不自动检测 ESM；CommonJS 模块 ID 改为规范化文件式 ID，某些行为存在破坏性变化

---

### [](https://github.com/isomorphic-git/isomorphic-git)

**原文标题**: [GitHub - isomorphic-git/isomorphic-git: A pure JavaScript implementation of git for node and browsers! · GitHub](https://github.com/isomorphic-git/isomorphic-git)

overview summary
- 🔄 isomorphic-git 是一个纯 JavaScript 实现的 git 库，可在 Node.js 和浏览器环境中运行，无需原生 C++ 模块依赖。
- 🎯 目标是与 canonical git 实现 100% 互操作，通过直接修改 ".git" 目录文件来执行操作，并提供完整的 API 与 CLI 工具。
- 👥 原项目作者已离开，现由两位志愿者维护，属于社区驱动项目，功能开发需用户自行贡献或赞助。
- 🌐 支持 Node 10、Chrome 79、Edge 79、Firefox 72、Safari 13、Android 10、iOS 13 等环境。
- 📦 可通过 npm 安装，支持在 Node 中使用原生 fs 模块，在浏览器中使用 LightningFS 等文件系统模拟库。
- ⚠️ 浏览器环境受同源策略限制，需通过 CORS 代理（如 @isomorphic-git/cors-proxy）进行克隆和推送操作。
- ⌨️ 提供名为 "isogit" 的 CLI 工具，可翻译命令行参数为 JS API 调用，适合快速测试。
- 📚 支持大量 git 命令，包括 clone、commit、push、pull、merge、stash、log、branch 等。
- 💬 社区支持通过 Gitter 聊天室和 GitHub Issues 进行，项目使用语义化版本控制。
- 🧪 开发测试使用 Jest 和 Karma，并配有自定义 mock server 用于测试 git 仓库 fixtures。
- 🏢 已被 nde、git-app-manager、GIT Web Terminal、Clever Cloud、Stoplight Studio 等项目使用。
- 🏆 类似项目包括 js-git 和 es-git，项目遵循 all-contributors 规范，感谢所有贡献者。
- 📄 项目采用 MIT 许可证发布，并接受 OpenCollective 赞助支持。

---

### [](https://github.com/dmmulroy/better-result)

**原文标题**: [GitHub - dmmulroy/better-result: Lightweight Result type for TypeScript with generator-based composition. · GitHub](https://github.com/dmmulroy/better-result)

better-result 是一个面向 TypeScript 的轻量级 Result 类型库，利用生成器组合简化错误处理，使失败显式化，并清晰区分预期错误与程序缺陷，同时保持零运行时依赖。

- 🎯 核心心智：`Result<T, E>` 由 `Ok` 和 `Err` 组成，调用者必须显式处理失败；不可恢复的异常用 `Panic` 表示。
- 🧩 生成器组合：`Result.gen` 配合 `yield*` 线性编写多步骤工作流，第一个 `Err` 短路，所有错误类型自动联合。
- 🏷️ 类型化错误：`TaggedError` 创建带 `_tag` 字面量的真实 `Error` 子类，支持 `is()`、`match()` 和 `toJSON()`。
- ⚙️ 异步工作流：`Result.gen` + `Result.await` 处理多步异步任务；短管道可用 `Promise.then(Result.andThenAsync(...))`。
- 🔧 转换与恢复：`map`、`mapError`、`andThen`、`tryRecover` 等组合子作用于对应分支，恢复时可返回备用成功值。
- 👀 观察副作用：`tap`、`tapError`、`tapBoth` 系列在不改变 Result 的前提下提供日志、指标等能力。
- 📤 提取结果：`match` 需要双分支策略；`unwrapOr` 提供默认值；`unwrap` 仅用于断言不变量，失败时抛 `Panic`。
- 🔁 异步重试：`Result.tryPromise` 捕获 Promise 拒绝，支持重试次数、退避策略、抖动及取消信号。
- 📚 集合处理：`Result.all` / `allAsync` 要求全部成功，`partition` / `partitionAsync` 处理所有项目，`flatten` 展平嵌套 Result。
- 🔒 传输边界验证：`Result.codec` 基于 Standard Schema 验证序列化/反序列化，提供安全与 unsafe 两种变体。
- 💥 缺陷处理：用户回调意外抛出会转为 `Panic`，保留原始 `cause`，不会污染错误联合类型。
- 📦 环境要求：需要 TypeScript 5.4 或更高版本，仅支持 ESM，零运行时依赖。
- 📈 迁移至 3.0：`TaggedError` 不再有尾随工厂调用，`serialize`/`deserialize` 被 `Result.codec` 替代，并新增恢复、匹配、集合等 API。

---

### [GitHub - beaugunderson/ip-address:](https://github.com/beaugunderson/ip-address)

**原文标题**: [GitHub - beaugunderson/ip-address: 💻 a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript · GitHub](https://github.com/beaugunderson/ip-address)

这是一个用于在 JavaScript 和 TypeScript 中验证和操作 IPv4 与 IPv6 地址的流行库，支持 CIDR、子网、特殊属性检查、Teredo/6to4 解码、URL 解析等，零运行时依赖，被 npm 生态大量使用。

- 📦 通过 `npm install ip-address` 安装，并支持 TypeScript 类型定义，兼容 CommonJS 和 ESM。
- ✅ 提供 `Address4` 和 `Address6` 类，用于验证、解析地址，支持 CIDR 子网、IPv6 区域标识及 URL 中的主机和端口解析。
- 🔍 功能涵盖子网成员判断、子网范围查询、特殊属性检测（私有、ULA、环回、链路本地、组播、未指定、CGNAT、文档地址等）。
- 📝 区分 correct form（RFC 5952 简洁形式）与 canonical form（完全展开形式），并解释 subnet、zone、v4-in-v6、Teredo、6to4 等术语。
- 🛠 API 提供多种静态构造方法（如 `fromBigInt`、`fromURL`、`fromByteArray`）及丰富的实例方法（如 `inspectTeredo`、`inspect6to4`、`to4in6`、`networkForm` 等）。
- 🔒 安全漏洞通过 GitHub 私有报告处理，发布版本带有 npm provenance 证明；地址属性检查仅为 SSRF 防护的一层，需注意 DNS 重绑定等风险。
- 🌍 每周约 6600 万次下载，通过 `socks`、`proxy-agent`、npm/pnpm、Puppeteer 等依赖链被广泛使用，也被 Juniper、IPFS 等项目采用。

---

### [Foxit API + n8n：自动化您的文档处理流水线](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/foxit-api-n8n-document-pipeline/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260804)

**原文标题**: [Foxit API + n8n: Automate Your Document Pipeline](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/foxit-api-n8n-document-pipeline/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260804)

overview summary  
该指南演示如何利用 Foxit 的 REST API，在 Power Automate 中构建一个由 CRM 成交事件触发的自动化工作流：从 Word 合同生成 PDF，通过电子签名 API 完成签署，并自动归档已签署文件，全程仅依赖 HTTP 操作和 Webhook。

- 📄 触发机制：CRM 中的交易状态变为“已成交”时，自动启动工作流。  
- 🔄 文档转换：通过 Foxit REST API 将 Word 合同转换为 PDF 格式。  
- ✍️ 签署流程：调用 Foxit eSign API 将 PDF 发送给相关方进行电子签名。  
- 🔔 状态通知：使用 Webhook 实时接收签署完成或拒绝的事件回调。  
- 📥 自动归档：签署完成后，系统自动下载并保存已签署的 PDF 到指定位置。  
- 🧩 无代码集成：整个流程仅使用 Power Automate 的 HTTP 请求操作，无需编写复杂代码。

---

### [Meticulous AI - 无需编写测试的前端自动化测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

overview summary
- 🚀 Meticulous 是一个自动化且穷尽的测试平台，能以零开发工作量生成并维护端到端测试，帮助开发者快速、可靠地交付代码。
- 🧠 通过脚本记录开发、预发布及生产环境的用户交互，AI 引擎持续生成覆盖所有代码分支、用户流程和边缘情况的测试套件。
- 🔄 在 PR 阶段即可预览变更对用户工作流的影响，自动 mock 后端响应，确保测试无副作用、无脆弱性，无需配置测试账户或数据。
- ⚡ 测试套件随应用演进自动增删，无需人工编写或维护；从 Chromium 层构建的确定性调度引擎彻底消除 flaky 测试，并支持并行计算，上千屏幕测试可在 120 秒内完成。
- 🏢 受到 Dropbox、Notion 等超 100 家组织信任，可与现有测试套件互补或完全替代。
- 🖥️ 支持 Next.js、React、Vue、Angular、Nuxt、SvelteKit 等主流框架，提供简单脚本标签或 loader 集成方式。
- 🔒 强调安全与集成，提供文档和快速启动指引，帮助用户快速部署并覆盖整个应用。

---

### [](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

**原文标题**: [The Unified Gateway for APIs, AI, and MCP - Zuplo](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

overview summary  
Zuplo 是一个统一的 API 与 AI 网关，可安全管理、治理和观测所有 API、LLM 与 MCP 调用。它提供双向流量控制（出站调用模型、入站代理调用你的 API），通过一个可编程策略引擎实现认证、限流、预算、审计、可视化和计费。支持快速上线、高可用，并有大量生产案例验证。

- 🌐 **统一网关定位**：一个网关同时处理出站 LLM 调用与入站 AI Agent 调用，覆盖 REST、GraphQL、MCP 与多种模型提供商。
- 🛡️ **安全与治理**：内置认证（API Key / JWT / OAuth 2.1 + PKCE）、Schema 校验、速率限制、提示注入防御，所有策略统一执行。
- 💰 **成本控制**：动态速率限制吸收流量尖峰，按团队设置 token 预算硬上限，防止失控 Agent 超支。
- 👁️ **全链路可见性**：每次调用按客户端、用户、工具归因，实时仪表盘展示调用趋势、延迟、拒绝原因，并可导出至 Datadog / SIEM。
- 📦 **Agent 原生支持**：Claude、Cursor、Codex、ChatGPT 等 Agent 可通过 Zuplo 网关连接，所有 MCP 工具调用均被记录和计费。
- 🧩 **MCP Server 快速发布**：将 OpenAPI 操作标记为 MCP 工具，无需写代码即可在数小时内上线安全的 MCP Server。
- 📊 **商业化与计费**：内置套餐、配额、按请求/token 计费，并直接对接 Stripe，实现计量收入。
- ⚙️ **代码集成简便**：出站侧仅需更换 OpenAI SDK 的 baseURL；入站侧在 OpenAPI 中扩展配置即可。
- 🚀 **生产级表现**：99.99% SLA、300+ 边缘节点、SOC 2 Type II，支持超过 10 亿终端用户。
- 📈 **可量化价值**：已实现削减约 41% 总支出、减少 90% 硬件占用、节省 70% 成本，并快速完成合规迁移。
- 📝 **免费试用**：免费层包含每月 10 万请求，无需信用卡，数分钟即可上线。

---

### [](https://www.youtube.com/watch?v=o98XmRVjxWs)

**原文标题**: [The secret third option for JavaScript comments - YouTube](https://www.youtube.com/watch?v=o98XmRVjxWs)

overview summary  
- 📺 這是 YouTube 的頁面底部資訊，列出主要功能與法律相關連結。  
- 🔍 提供「簡介」、「媒體」、「與我們聯絡」等基本網站資訊。  
- 🎨 針對創作者與廣告客戶，設有專屬合作與開發者入口。  
- ⚖️ 涵蓋著作權、條款、隱私權及政策安全性等重要法律聲明。  
- 🛠️ 說明 YouTube 運作方式及測試新功能的相關內容。  
- 📅 顯示目前版權年份為 2026 Google LLC。

---

### [ECMAScript® 2027 语言规范](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html#sec-hashbang)

**原文标题**: [ECMAScript® 2027 Language Specification](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html#sec-hashbang)

本文是 ECMAScript 语言规范的目录结构及第 12 章“词法语法”的详细摘要。规范从整体框架到具体词法规则均作了系统定义，涵盖数据类型、抽象操作、执行模型、内置对象以及语法细节等核心内容，为 JavaScript 引擎实现提供权威依据。

- 📘 规范前部章节包含介绍、范围、一致性、规范性引用及概述，并定义了实现近似、实现定义、宿主定义、类型、原始值、对象、构造函数、原型等关键术语。
- 🏗️ 第 5 章说明符号约定，包括上下文无关文法、词法与正则文法、算法约定、完成记录、数学运算、值表示及同一性等。
- 🗃️ 第 6 章详述 ECMAScript 数据类型：Undefined、Null、Boolean、String、Symbol、Numeric（Number 与 BigInt）、Object，以及规范类型如列表、记录、完成记录、引用记录等。
- 🔧 第 7 章定义抽象操作，涵盖类型转换（ToPrimitive、ToNumber、ToString 等）、测试与比较操作、对象操作、迭代器操作及可处置对象操作。
- ⚙️ 第 8 章介绍语法导向操作，包括求值、作用域分析、标签、函数名推断、Contains 及绑定初始化等。
- 🧠 第 9 章描述可执行代码与执行上下文，涉及环境记录、私有环境、域（Realm）、执行上下文、作业队列、代理（Agent）及 WeakRef 处理模型。
- 🧬 第 10 章详述普通对象与异质对象行为，包括 ECMAScript 函数对象、内置函数对象、绑定函数、数组、字符串、参数、类型化数组、模块命名空间、不可变原型及 Proxy 对象。
- ✏️ 第 12 章（词法语法）规定源码先转换为输入元素，根据语法上下文选用不同词法目标符号（如 InputElementDiv、InputElementRegExp 等）。
- 🔤 词法细节包括 Unicode 格式控制字符、空白字符表、行终止符（LF、CR、LS、PS）、单行与多行注释、Hashbang 注释以及 token 分类。
- 🏷️ 名称与关键字部分说明 IdentifierName、私有标识符、Unicode 转义、关键字与保留字分类，以及条件关键字（如 async、await、yield）的使用规则。
- 🔣 标点符号与字面量涵盖所有运算符标点、数字字面量（十进制、二进制、八进制、十六进制、BigInt 等）、字符串字面量、正则表达式字面量和模板字面量词法组件。
- 🔄 自动分号插入规则详述三种基本情形、受限产生式（如 return、break、continue、throw、箭头函数等），并给出示例与易错场景。
- 📦 后续章节（13–16）覆盖表达式、语句与声明、函数与类、脚本与模块的完整语法和语义。
- 🧩 第 18 章起列举标准内置对象，包括全局对象、基础对象、数字与日期、文本处理、索引集合、键控集合、结构化数据、内存管理、控制抽象对象（迭代器、Promise、生成器等）及反射。
- 📎 另有附录：规范性附录 B（Web 浏览器附加特性）、信息性附录 C–F（严格模式、宿主分层点、兼容性说明）以及参考文献和版权信息。

---

### [](https://www.seangoedecke.com/llms-reward-expertise/)

**原文标题**: [LLMs reward expertise](https://www.seangoedecke.com/llms-reward-expertise/)

LLM 让每个人都能成为通才，但真正高效使用 LLM 的关键在于领域专业知识。文章以 Terence Tao 与 ChatGPT 的数学对话为例，说明专家能通过简洁、有目的性的提示引导模型产出更优结果，并指出人类知识仍然是瓶颈，因为难点在于准确传达所需解决方案。

- 🧠 过去有技术短板需依赖他人或搜索，如今 LLM 让所有人能写出基本可用的代码，人人皆可成为通才。
- ❌ 许多人认为使用 LLM 毫无技能门槛，因为同样模型对新手和专家给出相同结果——这种看法是错误的。
- 🎯 提示工程师最重要的技能，是在所提示领域拥有真正的专业知识。
- 🧮 Terence Tao 与 ChatGPT 讨论 Jacobian 猜想反例的对话，展示了专家如何获得截然不同的高质量互动。
- ✍️ Tao 的消息简短且直击要点，不逐点回应模型，只回应核心；模型也自动进入“与数学家对话”模式，输出更简洁。
- 🧐 Tao 对可疑回答会温和推回（如“这看起来比我期望的更复杂”），而非直接否定，并经常自主提出下一步建议。
- 🔑 真正关键不是提示技巧，而是理解数学本身：能从冗长回复中提取相关想法、提出替代思路、识别“看起来奇怪”的地方。
- 💻 作者在编程工作中也有同样体验：对代码库有深入理解时，能更有力地驱动 LLM，例如说“这里应该更简单”或“我们不是已有 X 了吗”。
- 📐 系统设计问题由具体细节主导，熟悉具体代码库比掌握通用原则更有价值；Tao 的那些具体问题（如“X 在这里成立吗”）源于领域知识。
- ⚙️ 没有领域知识时，也能从 LLM 得到一些成果，这并不差；但有专业知识者能通过强力引导，从同一个模型中榨取更多价值。
- 🔮 即使模型越来越强，人类专业知识依然有用；对许多任务，瓶颈在人而非模型，因为难在向模型精确表达人类想要的解决方案。
- 💬 文章在 Hacker News 引发讨论：有人分享专业知识帮助或缺乏专业知识的教训，也有人怀疑这是种“自我安慰”，作者则指出 OpenAI 的数学提示也需要专家数学家筛选与验证。

---

### [](https://devblogs.microsoft.com/ifdef-windows/a-new-way-to-bring-native-windows-apis-to-javascript-introducing-dynamic-api-projections-for-node-js/)

**原文标题**: [A new way to bring native Windows APIs to JavaScript - introducing dynamic API projections for Node.js - #ifdef Windows](https://devblogs.microsoft.com/ifdef-windows/a-new-way-to-bring-native-windows-apis-to-javascript-introducing-dynamic-api-projections-for-node-js/)

微软发布了一项面向 Node.js 的动态 Windows Runtime (WinRT) API 投影技术（公开预览），让 Electron 或纯 Node.js 应用可以直接用 JavaScript/TypeScript 调用 Windows 原生 API，无需 C++/C# 桥接或 node-gyp 原生插件。它通过读取 .winmd 元数据自动生成 JavaScript 包装器和 TypeScript 声明，并由共享运行时统一调度调用，覆盖设备端 AI、通知、存储、剪贴板、网络等非 UI 类 Windows API。

- 🚀 新发布：动态 WinRT 投影让 Electron/Node.js 直接从 JS/TS 调用 Windows Runtime API，无需 C++/C# 桥接或 node-gyp
- ⚙️ 核心机制：codegen 读取 .winmd 元数据生成 .js 包装器与 .d.ts 声明，运行时统一通过 COM vtable 调度，非逐类原生插件
- 📦 三个 npm 包：@microsoft/winappcli（协调配置）、@microsoft/dynwinrt-codegen（生成绑定）、@microsoft/dynwinrt（预编译共享运行时，支持 x64/arm64）
- 🤖 设备端 AI：支持 Phi Silica 本地语言模型（文本生成/摘要/重写）、Windows ML 模型与执行提供程序目录
- 🔔 应用与内容 API：通知（含进度条）、文件/文件夹选择器、存储、剪贴板（富文本 HTML）、图像解码
- 🖥️ 系统与设备 API：网络、传感器、全球化、加密
- 📝 Electron 示例：原生通知（AppNotificationBuilder）与 Phi Silica 摘要均只需 JavaScript 代码，含流式输出
- 🛠️ 可扩展配置：通过 package.json 的 winapp.jsBindings.additionalWinmds 添加 Windows SDK 或自定义 WinRT 组件 API，依赖类型自动传递解析
- 🟢 纯 Node.js 支持：无需打包 MSIX，用 npx winapp run 注册 loose-layout 包并赋予包标识即可运行
- 🔄 重新生成而非重建：Windows API 元数据更新后只需重跑 codegen，无需等待手写包装器
- 🔑 调试标识：需要包标识的 API 可用 npx winapp node add-electron-debug-identity 为 Electron 可执行文件赋予临时标识
- 📣 公开预览反馈：CLI 问题提交至 microsoft/winappCli，运行时/代码生成问题提交至 microsoft/dynwinrt

---

### [](https://blog.cloudflare.com/grpc-workers/)

**原文标题**: [Cloudflare Workers and Containers now support inbound TCP connections and gRPC | The Cloudflare Blog](https://blog.cloudflare.com/grpc-workers/)

Cloudflare 在 Agents Week 宣布扩展 Workers 与 Containers 能力，新增入站 TCP 连接支持，并全面强化 gRPC 应用部署方式，涵盖从 Worker 到 Durable Objects、Containers 的 socket 转发，以及通过 gRPC-web 自动转换实现 Workers 原生 gRPC 服务与客户端功能，目前以私有 beta 形式开放。

- 🚀 新增 `connect(socket)` 处理器，让 Worker 可直接接受来自 Spectrum 的入站 TCP socket，并支持双向读写。
- 🔀 Worker 可将 socket 转发至其他 Worker、Durable Objects 或 Containers，实现全链路灵活路由与全双工通信。
- 📦 Cloudflare Containers 现在支持完整双向流式 gRPC 服务器，可用任意语言部署，并借助 330+ 节点实现低延迟语音与推理。
- 🌐 Workers 可作为 gRPC 服务器或客户端运行，代码使用 gRPC-web，Cloudflare 自动在 gRPC 与 gRPC-web 之间转换，无需客户端改动。
- 📱 该能力让移动端 gRPC 后端可直接构建在 Workers 上，也可在现有 gRPC 后端前放置 Worker 以迁移或优化性能。
- 🔒 所有新功能均通过私有 beta 提供，官方希望先与部分开发者验证完善，未来还将扩展至 UDP 等更多协议支持。

---

### [](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/)

**原文标题**: [Stacked pull requests are now in public preview - GitHub Changelog](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/)

GitHub 现已推出堆叠式拉取请求（Stacked Pull Requests）的公开预览版，旨在将大型变更拆分为多个小型、可独立审查的拉取请求，并支持一键合并，帮助团队更高效地协作与审查。

- 🚀 堆叠式 PR 将大改动拆分为有序的小型 PR 层，每层独立审查与检查，最终可一键合并全部层。
- 🧩 通过 CLI 扩展 `gh extension install github/gh-stack` 可在一分钟内创建首个堆叠 PR。
- 💻 支持在 github.com、GitHub CLI、移动端以及 Copilot 等编码代理中创建和管理堆叠 PR。
- 👀 每层 PR 可单独查看差异，并通过顶部的堆叠地图了解整体上下文，实现并行审查。
- 🔀 可选择合并全部层，或仅合并部分低层；其他 PR 会自动 rebase 并重新定向，分支保护与检查仍生效。
- ✅ 内置的审查、检查与合并队列功能与现有工作流无缝集成。
- 💬 公开预览将在未来几天内对所有仓库开放，合并队列支持也将逐步推出。
- 📚 更多详情请查阅官方文档，并可在 stacks 讨论区反馈意见。

---

