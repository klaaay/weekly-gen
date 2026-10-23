### [Web Weekly——不止是普通的前端新闻简报](https://webweekly.email/?utm_source=newsletter&utm_medium=email&utm_campaign=WebToolsWeekly2026Q4)

**原文标题**: [Web Weekly â More than your regular Frontend newsletter](https://webweekly.email/?utm_source=newsletter&utm_medium=email&utm_campaign=WebToolsWeekly2026Q4)

Web Weekly 是一份聚焦 Web 平台本身的前端通讯，强调无需 `package.json`，内容由真人挑选并总结，面向关注 HTML、CSS、JavaScript，以及构建快速、可访问、令人愉悦网站的开发者。

- 📬 内容不止于框架新闻，更关注 Web 平台原生能力，无需 `package.json`。
- 👥 已获得 6,426 名开发者喜爱；最新第 201 期讨论了同一模块的多次导入、新的 `poster` 元素和 `vary` 响应头。
- 🧭 Baseline Updates 帮助追踪 Chromium、WebKit、Gecko 的新浏览器特性。
- 🔍 Random MDN 分享冷门 Web 开发知识，例如 `capture` 属性、`display: flow-root;` 和 `:local-link`。
- 🛠️ Tiny Helpers 推荐实用工具，包括 ColorPalette Pro、PWA Browser Scorecards、gradient.style、OddContrast、Easing Wizard、pkg-size、OKLCH 转换器和 Shadow Palette Generator。
- 💬 Bruno Pulis、Gustavo Goulart、Jay Oram 等读者好评称其内容有趣且总能学到新东西。
- ✍️ 所有文章均由真人手工挑选并总结，不使用 AI。
- 👨‍💻 作者 Stefan 是德国自由职业 Web 开发者，专注 Web 平台，致力于构建快速、可访问且令人愉悦的网站。

---

### [Foldkit | 基于 Effect 构建的 TypeScript 前端框架](https://foldkit.dev/)

**原文标题**: [Foldkit | TypeScript Frontend Framework Built on Effect](https://foldkit.dev/)

Foldkit 是一个基于 Effect 的 TypeScript 前端框架，核心采用 Elm 架构，将应用状态与副作用显式化，帮助团队和 AI 代理更快构建功能、追踪行为并更有信心地测试变更；当前处于 pre-1.0 阶段。

- 🧠 单一不可变 Model 保存整个应用状态，所有变更都通过唯一的 update 函数处理，避免隐藏变更、陈旧闭包和意外行为。
- ⚡ 副作用以 Command 值的形式从 update 返回，由运行时决定何时、如何执行，而不是散落在事件处理器中的命令式调用。
- 🧩 小型与大型应用共用同一套 Model、Message、update、Command 结构，让新功能有明确位置，代码评审也有共同约定。
- 🔍 DevTools 会记录每条 Message，可检查每个 Model 状态、查看变化并回退 UI；相同运行时数据还可通过 MCP 提供给 AI 代理。
- 🧪 纯 update 函数带来纯测试：Story 测试状态机，Scene 通过视图和可访问定位器测试功能，无需 DOM 与 mock。
- 📦 内置类型安全路由、服务端渲染/静态生成、无障碍 UI 组件、Submodels、浏览器生命周期管理，以及 Runtime.embed 嵌入能力。
- ✅ 适合已使用 Effect 的团队、复杂状态应用，以及希望统一架构和共享约定的团队；大型 React 存量项目、依赖 React 生态或主要为静态内容的站点需谨慎。
- 🚧 当前版本为 v0.169.0，提供 36 个示例应用，生产应用示例为 Typing Terminal；可通过 `npx create-foldkit-app@latest` 快速开始。

---

### [Mastro：无依赖。无需构建步骤。只是一个简单的 Web 框架和静态站点生成器。](https://mastrojs.github.io/)

**原文标题**: [Mastro: No dependencies. No build step. Just a simple web framework and static site generator.](https://mastrojs.github.io/)

Mastro 是一个极简、务实的 Web 框架和静态站点生成器，面向重视用户体验与 Web 标准的开发者；以约 800 行 TypeScript 实现，强调无依赖、无构建步骤，并可直接运行在 Node.js、Deno、Bun 或 Workers 等环境。

- 🧱 核心极简：仅约 800 行 TypeScript，无依赖、无构建步骤，代码按编写原样运行，可替换或 fork，避免锁定。
- 🚀 双模式：支持静态站点生成（SSG），适合博客、营销站和网店；也支持服务端渲染（SSR），可作为全栈框架使用。
- 🛣️ 统一路由：HTML、JSON REST API、CSS 和图片都通过同一套路由/API 提供。
- 🧩 渐进采用：可在现有代码中使用模板，或按路由逐步迁移，无需一次性重写。
- 🪶 轻量与性能：无冗余、启动快；示例中 500 个 Markdown 文件 SSG 约 0.5 秒，快于 11ty、Astro、Next.js 对比项。
- 📄 默认无 JS：可构建快速的内容驱动 MPA；需要交互时再按需加入 JavaScript 或 HTMX、Alpine、Preact 等库。
- 🔗 代码共享：显式共享服务端与客户端代码；可用 Preact+HTM/vhtml，或用 Reactive Mastro 在客户端复用模板。
- 🧰 可扩展生态：核心不含“全家桶”，通过 @mastrojs 插件扩展 Markdown、图片、OG 图片、RSS/Atom、Standard.site、类型安全 API 等。
- 👶 对新手友好：可在浏览器中的 VS Code 直接上线首个网站，按 HTML/CSS、静态博客、待办应用、REST API 逐步学习。
- 🧑‍💻 对资深开发者友好：直接使用浏览器与运行时标准，减少抽象层，避免前端工具链负担。
- 🌍 关注体验与标准：强调低端设备/3G 下的速度、可访问性、SEO 和良好开发体验。
- 💬 社区与开放：提供 Discord、Bluesky、GitHub Discussions 等交流渠道，鼓励贡献与反馈。

---

### [Meco：排名第一的新闻简报阅读器 | 清理你的收件箱](https://meco.app?utm_campaign=3nux)

**原文标题**: [Meco: The #1 newsletter reader | Declutter your inbox](https://meco.app?utm_campaign=3nux)

Meco 是一款专为阅读和管理新闻邮件而设计的聚合工具，旨在把订阅邮件从杂乱收件箱中解放出来，集中到更适合阅读的空间。它支持连接 Gmail/Outlook 或使用专属 Meco 邮箱，并提供 AI 摘要、筛选分组、个性化推荐、书签标注等功能，覆盖网页、iOS 和 Android。

- 📥 将新闻邮件移出收件箱，集中到专为阅读打造的空间，快速减少邮箱干扰。
- 🔗 支持连接现有 Gmail/Outlook 即时导入订阅，也可使用专属 Meco 邮箱订阅新内容。
- 🧠 提供 AI 每日音频简报与 AI 文本摘要，帮助用户快速掌握重点信息。
- 🗂️ 通过智能筛选和分组聚焦重要内容，并按兴趣发现个性化新闻邮件推荐。
- 🔖 支持保存、标注、分类和高亮文章，打造便于留存知识的“第二大脑”。
- 📬 提供每周精选摘要和一键退订，方便管理未读内容与冗余订阅。
- 📱 可在 iOS、Android 和网页端使用，并支持通勤时离线阅读。
- 🔒 强调隐私安全：不存储或处理用户邮件数据，邮件保留在本地设备。
- 💳 通过付费订阅盈利，不以广告或出售数据获利；若不适合可断开连接并恢复邮件到收件箱。
- 🚀 可免费开始使用，定位为集阅读、发现和组织新闻邮件于一体的阅读器。

---

### [Marionette 5 — 用于智能体驱动开发的 JavaScript 库](https://marionettejs.com/)

**原文标题**: [Marionette 5 — JavaScript library for agent-led development](https://marionettejs.com/)

Marionette 5.0 是一个面向“代理主导开发”的 JavaScript UI 库：代理学习框架模式，你负责指导应用方向，代码仍保持可读、可维护并归你掌控。页面还提供代理工作坊、生命周期演示、应用结构示例、RealWorld 案例与多个可交互 Demo。

- 🧭 核心定位：让 JavaScript UI 开发更适合代理参与，同时保持人类对应用方向和代码变更的掌控。
- 🤖 代理工作坊：可复制提示词给代理，让其阅读说明并构建小应用；代理需要可控制且你可观看的浏览器预览，且不应擅自创建文件、安装依赖或启动本地项目。
- 🔄 生命周期示例：Region 通过 `show` 渲染并挂载 View，替换时清理旧 View，清空后等待下一个 View，强调清晰的进入与退出。
- 🏗️ 应用结构：用 Application、Workspace、View、Region、CollectionView、Behavior、State 与事件组织屏幕、列表和功能，让每部分有明确归属。
- 🛡️ 合理监督：代理可以编写新功能，但 Marionette 让所有权更明确、变更更有归属、结构更易在 diff 中审阅。
- 📚 RealWorld 案例：跟踪一个由代理构建的 Conduit 应用，覆盖实现、审查及与其他示例的量化比较。
- 🎛️ 更少依赖束缚：不再强制需要 Backbone、jQuery 或 Underscore，可自行选择工具。
- 🧪 演示项目：包括 TodoMVC（变化列表与独立 View）、Radio Ghostbusters（外部组件与清理）、Cheese Patrol（就绪状态与取消未完成工作）。
- 🤝 开源与维护：项目由人工维护，可通过 GitHub Sponsors 支持文档、发布与维护，也可浏览周边商品。

---

### [Fixi 项目](https://fixiproject.org/)

**原文标题**: [The Fixi Project](https://fixiproject.org/)

Fixi Project 是一组轻量级小型 Web 库集合，每个库都借鉴现有工具并做轻量实现，可单独引入，也提供 CDN、npm 与五库合一压缩包。

- 🚲 **fixi（约 3.4/1.2kb）**：受 htmx 启发，提供增强 HTML 的能力。
- 🥊 **moxi（约 4.6/1.8kb）**：受 hyperscript 启发，用于内联脚本与响应式。
- 📡 **ssexi（约 4.1/1.4kb）**：受 hx-sse.js 启发，处理流式 HTML 与事件。
- ♻️ **paxi（约 1.5/0.6kb）**：受 idiomorph 启发，用于 DOM 修补/变形。
- 🐕 **rexi（约 4.3/1.4kb）**：基于 fetch，提供更顺手的 fetch() 封装。
- 🧰 每个库都是独立脚本，可通过 vendor、npm 或 CDN 引入；五库合一压缩版约 4.5kb br。
- ⚠️ 若同时使用，应先加载 moxi.js 再加载 fixi.js，确保 on-fx:init 与 on-fx:process 处理器在页面加载事件派发前注册。
- 📜 所有项目采用 BSD-0 许可证，并在 GitHub 上提供。

---

### [类型安全的 API 与 React 服务器组件 - Spiceflow](https://getspiceflow.com/)

**原文标题**: [Type-safe APIs and React Server Components - Spiceflow](https://getspiceflow.com/)

Spiceflow 是一个面向 Node.js、Bun 和 Cloudflare Workers 的类型安全全栈 React RSC 与 API 框架，强调简单统一：同一套代码可同时提供 JSON API、React 页面、Server Actions 和 OpenAPI。

- 🧩 **核心定位**：类型安全 API 框架 + 全栈 React RSC 框架，支持 React Server Components、Server Actions、布局和自动客户端代码拆分。
- 🌍 **跨运行时**：同一份代码可运行在 Node.js、Bun 和 Cloudflare Workers。
- 🛡️ **类型与校验**：基于 Zod 的 Schema 校验，类型安全 Fetch 客户端可推断路径参数、查询参数、请求体和响应。
- 🔗 **统一链式 API**：API 路由、中间件、Loader、布局和页面都挂在同一个 `Spiceflow` 实例上，链式定义同时决定运行时路由和 TypeScript 类型。
- 🚀 **两种用法**：可作为独立 API 框架使用；也可通过 Vite 插件启用完整 React RSC 全栈能力。
- 📦 **安装注意**：当前为预发布版本，应安装 `spiceflow@rsc`，不要安装 `spiceflow@latest`。
- 🤖 **AI 辅助**：可运行 `npx -y skills add remorses/spiceflow -g -y` 让 AI 编码代理了解用法；文档 URL 追加 `.md` 可获取原始 Markdown。
- 📚 **文档索引**：提供 `/llms.txt`、`/llms-full.txt` 和 `/docs.zip`，方便代理读取或本地检索全部 Markdown 文档。
- ⚡ **基础用法**：`.get()` 等 API 路由自动返回 JSON；`.page()` 和 `.layout()` 用于服务端渲染 React 页面；需要 Zod 校验时使用 `.route()`。
- 🏗️ **Vite 构建**：React 模式下 Vite 从同一入口构建 `rsc`、`ssr`、`client` 三个环境；每个 `"use client"` 文件自动成为浏览器 chunk。
- 🔄 **Server Actions**：标记为 `"use server"` 的 Server Actions 会成为 POST 端点，执行后重新渲染页面并获取最新数据。
- 🧱 **静态页面**：`.staticPage()` 在构建时生成 `.html` 和 `.rsc` 文件；在 Node.js 和 Cloudflare Workers 上，中间件仍会在静态页面请求前运行。
- ⚠️ **静态页面注意**：`vite build` 预渲染静态页面时也会运行中间件，但该请求没有 Cookie 或用户请求头，重定向可能导致构建失败。
- 🧪 **测试方式**：可直接用 Vitest 调用应用，无需浏览器和构建步骤；API 返回类型化 JSON，页面返回 `SpiceflowTestResponse`。
- 📖 **文档组织**：完整文档按功能拆分，涉及 API、Fetch Client、OpenAPI、MCP、Tracing、React、Data & Actions、Testing、Security、Deployment 等，建议开发前先阅读对应功能文档。
- ☁️ **部署支持**：覆盖 Cloudflare Workers、Service Bindings、Docker、部署偏移、缓存、绑定、后台任务等场景。
- 🆚 **框架对比**：Spiceflow 同时提供类型化 API 与 React RSC 应用；Hono 和 Elysia 偏 HTTP 框架，Next.js 则是基于文件路由和缓存的 React 平台。

---

### [jax-js – 面向 Web 的机器学习](https://jax-js.com/)

**原文标题**: [jax-js – ML for the web](https://jax-js.com/)

jax-js 是面向 Web 的纯 JavaScript 端到端机器学习库与编译器，受 JAX 启发，可在浏览器中通过 WebGPU 和 WebAssembly 高性能运行神经网络、图像算法、模拟与数值代码，并支持 JIT 编译。

- 🧠 提供与 NumPy/JAX 接近的 API 兼容性，从零编写且零外部依赖。
- ⚙️ 通过轻量编译器将高层操作转换为 WebGPU 与 WebAssembly 内核，支持 Wasm、WebGPU、WebGPU-fp16。
- 🌐 完全在客户端运行，覆盖 Chrome、Firefox、iOS、Android，并兼容主流浏览器、打包工具和 JS 模块。
- 📦 安装方式为 `npm install @jax-js/jax`。
- 🚀 可执行矩阵乘法等计算，以 GFLOPs 衡量性能，定位为高便携性的浏览器 GPU 机器学习框架。
- 💡 目标是让数值代码更易访问和部署，使计算密集型应用能在消费级硬件上本地快速运行。
- 🧪 提供浏览器内实时编辑器/REPL 和多个演示，包括 LLM Chat、神经细胞自动机、测地线计算、Whisper ASR、语音克隆 TTS、流体模拟、目标检测、CLIP 嵌入、MNIST 训练与 PCA。
- 📚 资源包括 GitHub 仓库与教程、REPL、API 参考，以及与其他 Web 机器学习库的基准比较。

---

### [](https://tinyjs.app/)

**原文标题**: [tinyjs — desktop apps for macOS, Windows, and Linux in ~6 MB](https://tinyjs.app/)

tinyjs 是一个用系统自带 WebView 和 txiki.js 后端构建约 6 MB 桌面应用的 JavaScript 运行时：无需 Electron、无需打包 Chromium、无需 HTTP 服务器和端口，主打纯 JavaScript 全栈、完整系统访问与原生桌面体验；同时提供跨平台安装、示例应用、开发构建流程，并坦诚说明与 Electron、Tauri、Neutralino 的差异和取舍。

- 📦 **体积与架构**：应用约 6 MB，由 5.6 MB 的 txiki.js 运行时和约 1–2 MB 的窗口启动器组成，页面使用普通 HTML/CSS/JS。
- 🖥️ **跨平台**：支持 macOS、Windows、Linux，分别使用 WebKit、WebView2、WebKitGTK 系统 WebView。
- ⚙️ **安装方式**：提供一行安装脚本；macOS 15+、Apple Silicon/Intel；Windows 10/11 x86_64/arm64，仅需 WebView2 运行时；Linux glibc 2.35+，需 libwebkit2gtk-4.1-0。
- 🔌 **零端口通信**：页面与后端通过私有临时目录中的 Unix socket 通信，Windows 使用命名管道；没有监听端口、端口冲突或扫描风险。
- 🧰 **完整系统访问**：后端基于 txiki.js，支持文件、套接字、进程、FFI、SQLite、fetch、WebSocket 等能力。
- 🔥 **开发体验**：前端修改热更新到窗口，后端修改自动重启进程；开发阶段无构建步骤。
- 🪟 **原生界面能力**：真实菜单栏、文件面板、alert/confirm/prompt 等由 AppKit 等系统组件处理，而非 div 模拟。
- 📦 **打包与签名**：`tinyjs build` 生成带代码签名、可公证的 `.app` 包；Windows/Linux 生成对应可执行文件或压缩包。
- 🌐 **包装现有网站**：可将窗口指向 URL，像浏览器一样处理对话框、下载、弹窗、页内查找，并通过 `tinyjs.json` 的能力门控限制来源可调用的原生 API。
- 🤖 **面向编码代理**：每个项目附带 skill 文件，让编码代理了解完整 API。
- 🧪 **示例商店 shelf**：4.4 MB 原生应用，可一键安装、更新、移除示例，目录从示例仓库自动更新。
- 🎵 **示例应用**：包括 amp（Winamp 风格播放器）、Nib（Markdown 编辑器）、Platter（唱片播放器）、World Clock（菜单栏世界时钟）、Tiny Deck（完整 API 演示）。
- 🚀 **快速开始**：`tinyjs new myapp`、`tinyjs dev`、`tinyjs build`；后端在 `src/backend/main.js` 导出 API，页面通过 `tiny.api.call()` 调用。
- 🧭 **框架对比**：Electron 体积 ≥150 MB 且捆绑 Chromium/Node；Tauri 约 10 MB 但后端为 Rust 且系统能力多为插件；Neutralino 约 3 MB 但无后端运行时、通过 localhost WebSocket 代理；tinyjs 约 6 MB、纯 JavaScript 后端、零端口。
- ⚠️ **限制与取舍**：三平台 WebView 渲染不完全一致，Linux 媒体编解码和 Web Audio 有差异；不能从 Mac 构建 Windows 应用；不支持 iOS/Android；部分 macOS 专属能力尚未移植。
- 🍎 **生产与发布**：macOS 为主平台，Windows/Linux 同样测试；支持签名、公证、`tinyjs publish` 静态托管更新清单，内置更新器校验 sha256 与签名并支持回滚。

---

### [GitHub - Hussseinkizz/dialogue：一个基于 Socket.IO、Hono 和 Bun 的基于事件的实时通信库。· GitHub](https://github.com/Hussseinkizz/dialogue)

**原文标题**: [GitHub - Hussseinkizz/dialogue: An event-based realtime communication library based on Socket.IO, Hono, and Bun. · GitHub](https://github.com/Hussseinkizz/dialogue)

Dialogue Ts 是一个基于 Socket.IO、Hono 和 Bun 的事件驱动实时通信库，旨在用统一的心智模型和 API 覆盖多种实时场景；项目提供完整文档、聊天示例以及客户端/服务端 SDK，并采用 MIT 许可证。

- 📚 文档与定位：完整文档位于 hussseinkizz.github.io/dialogue，核心目标是统一实时通信的扩展方式。
- 🧰 技术栈与前置条件：依赖 Bun 运行时与 Zod 校验，底层使用 Socket.IO、Hono、Slang Ts 等。
- 📦 安装方式：使用 `bun add dialogue-ts zod` 安装。
- 🧩 核心概念：事件由 `defineEvent` 定义并可选 Zod schema 校验；房间是事件广播频道；客户端可按事件类型订阅以减少无关流量。
- 🖥️ 服务端快速开始：通过 `createDialogue` 配置端口、房间、事件与 hooks，调用 `dialogue.start()` 启动；`trigger` 可向房间订阅者广播事件。
- 👥 服务端 API：支持获取、创建、删除房间，查询用户连接、用户所在房间、判断是否在房间，以及让用户离开所有房间。
- 💻 客户端 API：使用 `createDialogueClient` 连接服务端，支持 `join` 加入房间、创建/删除房间、监听房间创建/删除事件。
- 🔁 RoomContext：加入房间后可 `on` 监听事件、`trigger` 发送事件、`subscribe/unsubscribe` 管理订阅，并 `leave` 离开房间。
- 🪝 Hooks 生命周期：提供客户端连接/断开/加入/离开、房间创建/删除、事件触发与清理/加载等回调，便于通知、持久化和分析。
- 🗂️ 事件历史：可按事件启用 `history` 并设置 `limit`，支持加入房间时自动同步历史、客户端分页获取、服务端读取历史。
- 🧪 示例与许可：`example/` 内含可运行的聊天应用示例；项目采用 MIT 许可证。

---

### [GitHub - vinzdg/codenotch：一款 macOS 应用，可将 Claude Code、Cursor、Codex 和 Antigravity 的用量限制固定到屏幕边缘。 · GitHub](https://github.com/vinzdg/codenotch)

**原文标题**: [GitHub - vinzdg/codenotch: A macOS app that pins usage limits from Claude Code, Cursor, Codex, and Antigravity to a screen edge. · GitHub](https://github.com/vinzdg/codenotch)

Codenotch 是一款把编码助手用量限制、重置时间和会话状态固定到屏幕边缘的 macOS 工具，并提供 Windows 移植版与手机端配对查看。它聚合官方、派生或手动配置的用量来源，强调只读现有登录/缓存、失败时显示真实状态而非编造数字，同时支持本地模型监控、多账号、通知和高度可定制的外观。

- 🖥️ 主程序为 macOS 通用二进制，需 macOS 15+；正式版已签名、公证，并通过 Sparkle 自动更新。
- 🪟 Windows 版基于 Rust/Tauri 2，安装包未签名，首次运行需在 SmartScreen 中选择“更多信息 → 仍要运行”。
- 📱 iOS/Android 手机应用可通过二维码在同一 Wi-Fi 下配对，只显示刘海屏已有的用量百分比、重置时间和会话状态，不读取令牌或原始 API 响应。
- 🔐 配对码一次性且 5 分钟过期；可在设置中移除设备，凭证立即删除，服务器只响应局域网地址。
- 🔌 支持 Claude Code/Desktop、Cursor、Codex、DeepSeek、Antigravity、GLM、MiniMax、QianwenAI、GitHub Copilot、Kimi、Kiro、Amp、Apify、Kilo、OpenCode、Command Code、Grok 等及自定义端点。
- 🧠 支持本地 Ollama、LM Studio、oMLX 监控，显示模型、内存/显存、上下文、速度与思考状态；不保存提示词、推理或回复。
- 🪪 各提供商标注官方、派生或手动保真度；多数借用本机已有登录/会话，DeepSeek/MiniMax/QianwenAI 需在应用内显式登录，不读取浏览器 Cookie。
- 👥 支持 Claude、Codex、Command Code 多账号/多配置目录，每个账号独立成环、独立设置，顺序跨启动保留。
- ⚙️ 关闭某提供商只停止轮询并忘记其读数，不会注销原工具的借用账号。
- 🟠 刘海环在会话忙碌时旋转，等待用户时变为脉冲琥珀色；悬停可查看实时会话名称、运行位置和请求内容。
- 🔔 会话结束或等待输入时刘海自动展开 5 秒并播放提示音；点击可前置对应应用而非具体标签页，提示展开和声音可分别关闭。
- 🚨 提供商主限额达到 80% 和 100% 时各通知一次，窗口真正重置后才可再次通知，可按提供商静音。
- 📍 刘海可置于屏幕四边，按住 Option 拖动定位，各边记住位置；支持硬件刘海形状、居中、尺寸、常显/隐藏、强调色及 Dock/菜单栏显示。
- ⏱️ 刷新策略为工作时 30 秒、空闲时 5 分钟、窗口滚动时立即刷新；悬停、点击环和菜单会触发刷新，并支持“每次查看都询问提供商”。
- 🧱 架构以 UsageProvider 和 Fidelity 为核心，UsageStore 轮询、保留最后有效读数，并把失败降级为 stale/needsAuth/error 等可见状态。
- ⚠️ 官方没有统一“会话限额已用 N%”API，适配器读取各应用自身依赖的内部端点、本地数据库或 RPC，可能随版本变化；响应结构由测试固定，避免显示猜测值。
- 🧾 Claude Desktop 缓存读取严格只读且按组织匹配，超过 30 分钟（活跃时 2 分钟）不视为实时；Claude 未使用的重置信息来自缓存并标注观察时间。
- 🛠️ 开发可用 make run/test，发布需 Developer ID 与公证；Debug 构建可运行 Scripts/sign-local.sh 获得稳定本地签名，避免每次启动都弹钥匙串授权。
- 📜 项目采用 MIT 许可证，日志通过统一日志系统查看。

---

### [设计工程师的 UI 技能 | UI 技能](https://www.ui-skills.com/)

**原文标题**: [UI Skills for Design Engineers | UI Skills](https://www.ui-skills.com/)

该页面汇集面向设计工程的精选 UI 技能，提供 CLI 与 MCP 两种接入方式，覆盖 UI 路由、界面审计、前端设计、动效、React、设计系统与交互细节，并展示新技能、Design.md 采用案例、实用前端技巧以及招聘和订阅入口。

- 🧰 通过 `npx ui-skills` 可在终端运行 UI Skills CLI，也可用 MCP 将智能体连接到 UI Skills 目录。
- 🧭 `ui-skills-root` 可按主题、技术栈和意图，将用户需求路由到最小可用的 UI 技能集合。
- 🛠️ 多个技能专注于只读审计与改进计划，如 `improve-ui`、`improve-animations`、`improve-react` 和 `improve`，可输出供其他智能体执行的实施方案。
- 🎨 设计与前端技能涵盖 `frontend-design`、`better-ui`、`impeccable`、`ui-ux-pro-max`、`interface-design` 等，强调高质量、反通用 AI 审美和一致性。
- ✨ 动效与交互技能包括 `12-principles-of-animation`、`interaction-design`、`improve-animations`，关注微交互、转场和自然动效。
- 🧪 `design-lab` 提供交互式设计探索流程，包括访谈、生成变体和基于反馈的 UI 优化。
- 🆕 新技能包括 `create-canvas`、`talking-head-recut`、`slideshow` 和 `product-launch-video`，覆盖画布探索、视频图文包装、演示文稿和产品发布视频。
- 🏢 Design.md 展示了 Vercel、Atlassian、Mintlify、Unicef、Ant Design、Nuxt、Clerk 等组织的采用案例。
- 📐 学习要点包括用 `aspect-ratio` 防止布局跳动、用 `text-balance`/`text-pretty` 优化文本、用 `tabular-nums` 对齐数字，以及保证至少 44×44px 的触控目标。
- 💼 页面还提供设计及设计工程职位浏览入口，以及新 UI 技能、工具和资源更新的邮件订阅。

---

### [GitHub - puffinsoft/peek-cli：让编程智能体看到你的浏览器。· GitHub](https://github.com/puffinsoft/peek-cli)

**原文标题**: [GitHub - puffinsoft/peek-cli: Let coding agents see your browser. · GitHub](https://github.com/puffinsoft/peek-cli)

peek-cli 是 puffinsoft 推出的开源工具，让 Claude Code、Codex、Copilot 等编码代理通过浏览器扩展和 WebSocket 获取任意已打开标签页的截图，便于反复检查和完善前端设计。

- 👀 核心能力：编码代理可查看可用标签页并截取指定页面截图，截图会保存到本地 images 目录。
- 🧩 兼容性：支持 Claude Code、Codex、Copilot 等多种编码代理。
- ⚙️ 使用流程：每次启动需先运行 `peeked start` 启动 WebSocket 服务并连接浏览器，再用 `peeked list` 查看标签页、`peeked at <URL>` 截图。
- 📦 安装方式：安装 Chrome 扩展；运行 `npm i -g peeked` 安装 CLI；按需安装 Claude Code 或 Codex 的 Skill 插件。
- 🔒 安全性：编码代理只能通过 WebSocket 发送截图请求，无法访问浏览器、注入脚本或执行操作，扩展源码可审查。
- 🪪 项目信息：MIT 开源许可，GitHub 约 121 Star、5 Fork，Chrome 扩展已获 Chrome 网上应用店批准。

---

### [获取失败](https://api.wellput.io/v1/cm?cmid=1187656&tid=380&s1=v2-r1038777-p1187656-c50895&s2=Web%20Tools%20Weekly&s3=&s4=)

**原文标题**: [Failed to retrieve](https://api.wellput.io/v1/cm?cmid=1187656&tid=380&s1=v2-r1038777-p1187656-c50895&s2=Web%20Tools%20Weekly&s3=&s4=)

无法总结：获取内容失败，状态码 403。

---

### [](https://github.com/the-open-engine/zeroshot)

**原文标题**: [GitHub - the-open-engine/zeroshot: Open-source orchestration for coding agents. Define your own workflows, reviewers and repair loops. zeroshot enforces the process you configure. · GitHub](https://github.com/the-open-engine/zeroshot)

zeroshot 是一款采用 MIT 许可证的开源编码代理编排工具，通过可配置的“图”强制执行实现、独立审查和修复循环，让代理按既定流程工作，而不是只依赖提示词。它支持本地、云端和自托管运行，可混用 Claude Code、Codex、GitHub Copilot、Pi 等代理与模型；仓库约有 2k stars、194 forks、7 个 issue、2 个 PR 和 714 次提交。

- 🧩 核心理念：提示词只是建议，图才是约束；用户定义工作流、审查者和修复路径，引擎强制执行审查门禁与重试限制。
- 🔁 内置 software-change：worker 负责实现，acceptance 与 code reviewer 并行独立审查；被拒绝的工作带着双方反馈回到同一 worker 修复，再重新审查。
- 🧠 多模型与多代理：每个代理可使用不同模型和 harness，包括 Pi、Claude Code、Codex、GitHub Copilot；支持统一运行时配置或逐节点绑定。
- 📊 效果基准：在 20 个 ProgramBench 任务上，小模型配合审查循环以中位 58% 的成本达到较大模型的分数。
- 💻 快速安装：运行 `npm install -g @the-open-engine-company/zeroshot`，需要 Node.js 18+，会安装 Linux/macOS/Windows 原生二进制及 Codex、Copilot、Pi、Claude Code 技能。
- 🚀 CLI 使用：准备 `input.json` 和 `runtime.json`，通过 `zeroshot run --template software-change ...` 启动；可用 `--validate-only` 预检，并用 `zeroshot ui/list/status/logs` 查看运行。
- 🗂️ Profiles：可保存图及其运行时设置并复用；CLI 与 UI 共享本地 profile，也支持组织级共享配置。
- 🔬 auto-research：默认运行 10 轮，三个 scout 提出方向，researcher 选择父代并做实验，fresh reviewer 审核证据、正确性、泛化与进展；常规一轮约 5 次模型执行，记录存于 `.zeroshot/research`。
- 📦 交付选项：默认仅在本地保留工作；`--push` 推送托管分支，`--pr` 准备可合并 PR，`--ship` 走 PR、CI 和合并；PR/ship 默认处理可见反馈，可用 `--no-pr-feedback` 忽略。
- 🐳 自托管：Docker 目标镜像包含原生引擎和固定版本 Codex、Claude、GitHub Copilot、Pi CLI，支持持久化存储、网络隔离、HTTPS，并提供 profile 编辑器和运行查看器。
- 🛠️ 开发与许可：使用 `npm ci`、`npm run check`、`cargo test --workspace`；Node.js 构建静态 UI 并支持 npm 交付，Rust 提供 UI 服务；项目采用 MIT 许可证。
- 🌐 社区与文档：Discord 用于问答和分享运行/图，GitHub Issues 用于可复现 bug 和功能请求；提供版本化文档、CLI 参考、Python SDK、集群 API 和图契约等资源。

---

### [Yedric AI——发布一个能办事的 AI 助手](https://www.yedric.ai/)

**原文标题**: [Yedric AI â Ship an AI assistant that does things](https://www.yedric.ai/)

您尚未提供需要总结的文章内容，因此暂时无法提炼关键信息与要点。请补充文本后，我将按要求生成中文摘要。

- 📄 当前缺少待总结的正文内容，无法进行有效概括。
- ✍️ 请提供文章或文本，我会整理为简洁的要点列表。

---

### [TokenBlast — Claude Code 配置生成器](https://www.tokenblast.cc/)

**原文标题**: [TokenBlast — Config Generator for Claude Code](https://www.tokenblast.cc/)

Token Blast 是一个非官方社区工具，可通过滑块和预设调整 Claude Code 的环境标志，以平衡成本、思考深度与上下文配置，并支持搜索、保存、分享及版本差异比较。

- 🛠️ 提供滑块和预设，用于调节 Claude Code 的成本、思考与上下文相关环境标志。
- 💾 支持保存自定义预设、搜索完整标志目录，并查看不同版本间的变化。
- ⚙️ 生成的配置可复制粘贴到 `~/.claude/settings.json`，或用于 `/update-config` 技能。
- 🔗 配置可编码进 URL hash，便于分享。
- 🔍 可比较 Claude Code 各版本中标志的新增、移除或重构，并按全部、新增、移除、更改筛选。
- 🧩 界面包含 Configure、Compare、Clear Search、Reset、Save、Copy 等操作，以及自定义预设保存弹窗。
- ⚠️ 该工具为非官方社区工具，与 Anthropic 无关联、未获认可或赞助；Claude 和 Claude Code 是 Anthropic 的商标。
- 📌 标志说明和成本估算由社区根据观察推断，多数标志未文档化、可能变化或有误，使用前应核对 Anthropic 官方文档。
- 🏷️ 内容基于 Claude Code v2.1.107 生成，站点为 tokenblast.cc，作者 Conor Luddy，并显示预估成本。

---

### [GitHub - langchain-ai/openwiki：OpenWiki 是一个为你的代码库编写并维护智能体文档的命令](https://github.com/langchain-ai/openwiki)

**原文标题**: [GitHub - langchain-ai/openwiki: OpenWiki is a CLI that writes and maintains agent documentation for your codebase. · GitHub](https://github.com/langchain-ai/openwiki)

langchain-ai/openwiki 是一个面向代码库的文档 CLI，可将代码与知识源转化为可链接、可搜索、可阅读的 Markdown Wiki，供开发者和编码代理共同使用；文档归用户所有，并支持仓库代码文档与个人知识库两种模式。

- 🧠 **核心定位**：把仓库代码、测试和外部知识整理成带来源证据的 Wiki，帮助编码代理理解项目、回答问题并跨项目查找上下文。
- 🚀 **快速开始**：需 Node.js 22.22.0+，执行 `npm install -g openwiki`；通过 `openwiki integrations install ...` 接入编码代理，重启后让代理初始化仓库 Wiki，内容写入 `openwiki/`。
- 🤝 **代理集成**：支持 Codex、Claude Code、OpenCode、Cursor、IBM Bob、Kiro、Oh My Pi、Antigravity、GitHub Copilot CLI、Pi 等；默认用户级安装，支持 `list`、`uninstall` 和 `--project`。
- 🔎 **检索与跨库链接**：提供本地只读 MCP 工具 `openwiki_search`、`openwiki_read`；`openwiki link` 可把多个仓库 Wiki 组成命名工作区并跨库搜索。
- 🕸️ **可视化**：`openwiki visualize` 启动本地交互式节点图和 Markdown 阅读器；`--export` 可导出静态可视化目录，便于 GitHub Pages 等托管。
- 🔄 **持续更新**：`openwiki --update` 根据代码变更与证据状态决定更新；支持 GitHub Actions、GitLab CI、Bitbucket Pipelines 定时生成文档 PR，并可配置自动合并。
- 🧱 **两种模式**：`code` 模式记录当前仓库并写入 `openwiki/`；`personal` 模式汇入外部知识源，写入 `~/.openwiki/wiki`。
- ⚡ **并行与恢复**：原生 CLI 支持 `OPENWIKI_PAGE_CONCURRENCY=1..8` 并行写页面；页面任务持久化，可中断续跑，并适配提供商速率限制与重试。
- 📌 **Grounded Claims**：页面事实关联版本化源码证据，如 `repo://src/server.ts#L40-L82`；证据变化时可定位需确认、改写或废弃的事实，Claims 状态存于 `openwiki/.claims/`。
- 📦 **OKF v0.2 输出**：支持 Google Open Knowledge Format v0.2，包含 YAML front matter、来源与验证元数据；Mermaid 图自动生成、校验，失败时降级并可后续修复。
- 🔌 **连接器**：个人模式支持 Custom MCP、本地 Git、Notion、Gmail、X/Twitter、Web Search、Hacker News、Slack 等；LangSmith 连接器可为代码 Wiki 引入运行时 trace。
- 🧩 **模型提供商**：支持 14 种提供商，包括 OpenAI、Anthropic、Gemini、AWS Bedrock、GitHub Copilot、OpenRouter、OpenAI-compatible 本地或网关端点等。
- 🔐 **配置与隐私**：本地状态默认存于 `~/.openwiki`，可用 `OPENWIKI_CONFIG_DIR` 覆盖；`.openwikiignore` 可限制读取路径；遥测匿名且可通过环境变量关闭。
- 📄 **开源许可**：项目采用 MIT License，欢迎贡献；PR 应保持范围单一，避免捆绑无关变更。

---

### [](https://github.com/thedotmack/claude-mem)

**原文标题**: [GitHub - thedotmack/claude-mem: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More · GitHub](https://github.com/thedotmack/claude-mem)

claude-mem 是 thedotmack 开源的持久记忆压缩系统，采用 Apache-2.0 许可。它会自动捕获 AI 代理会话中的工具使用观察，用 AI 压缩成语义摘要，并把相关上下文注入后续会话，帮助 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等代理跨会话保持项目连续性。仓库约 102.3k stars、9k forks、322 watchers、3,520 commits，当前 46 个 issues、81 个 PR。

- 🧠 **持久记忆**：上下文可跨会话保留，会话结束或重连后仍能延续项目知识。
- 📦 **快速安装**：支持 `npx claude-mem install`，也可按 IDE 使用 `--ide opencode/t3code/antigravity/omp/pi` 等参数安装。
- 🔌 **多平台集成**：支持 Claude Code 插件市场、OpenClaw 网关、Codex、Gemini、Copilot、OpenCode、Grok Bot、Pi、DeepSeek Harness 等。
- 🔍 **智能检索**：默认提供 mem-search 技能；MCP 工具采用 search → timeline → get_observations 三层工作流，先筛选再取详情，约节省 10 倍 token。
- 🗄️ **技术架构**：通过生命周期 hooks 捕获事件，本地 Worker 提供 HTTP API/Web 查看器，SQLite 存储会话/观察/摘要，Chroma 向量库支持混合语义与关键词搜索。
- 🖥️ **本地工作台**：提供 My Work 实时请求、进度、人工交接和审查队列；记忆、会话与设置保留在 `/viewer`。
- 👥 **TeamBrain**：可选团队共享工作区，支持真实工作列表、成员归属和关联发现，个人请求与审查笔记保持独立。
- 🔒 **隐私与配置**：支持 `<private>` 标签排除敏感内容；可在 `~/.claude-mem/settings.json` 配置模型、端口、数据目录、日志和上下文注入。
- 🌐 **语言模式**：通过 `CLAUDE_MEM_MODE` 控制工作流与观察语言，如 `code--zh` 为简体中文模式，修改后需重启 Claude Code。
- ⚠️ **安装注意**：`npm install -g claude-mem` 只安装 SDK/库，不会注册插件 hooks；应使用 `npx claude-mem install` 或 `/plugin` 命令。
- 🧰 **系统要求**：Node.js 20+、支持插件的 Claude Code；Bun、uv 缺失时自动安装，SQLite 3 随附。
- 📄 **许可与支持**：Apache-2.0 许可，文档位于 `docs/`，问题通过 GitHub Issues 反馈，作者为 Alex Newman（@thedotmack）。

---

### [MongoQUI | 强大的 MongoDB GUI，用于查询、编辑和管理](https://www.mongoqui.com/?lz_click_id=d6786648-d678-72b8-8846-1d80a903b471)

**原文标题**: [MongoQUI | Powerful MongoDB GUI to Query, Edit & Manage](https://www.mongoqui.com/?lz_click_id=d6786648-d678-72b8-8846-1d80a903b471)

overview summary
MongoQUI 是一款面向把 MongoDB 当作生产基础设施的工程团队的桌面工作区，将查询编辑、自然语言 AI 助手、BI 级报告、团队协作与安全分享整合在一个本地优先的应用中，并提供 Web 版与分级订阅。

- 🎯 **产品定位**：不是普通 MongoDB GUI，而是集查询、分析、报表与共享于一体的工程工作区，强调键盘驱动、桌面速度与生产环境可用性。
- 🧠 **AI 助手**：可读取真实集合结构与字段统计，用英文生成 `find` 或聚合查询；默认先审后跑，不按 Run 不执行。
- 🛠️ **查询能力**：提供 Monaco 聚合编辑器、IntelliShell、可视化查询/聚合构建器，支持 27 种聚合阶段、SQL→MongoDB 转换及代码导出。
- 📊 **报告构建器**：将查询转为 DuckDB/Parquet 支持的图表、KPI 和仪表盘，可一键重跑、生成只读链接并分享给非技术同事。
- 👥 **团队协作**：支持共享连接、文件夹、查询与报告，提供 Admin/Editor/Viewer 角色、RBAC 和审计日志，避免共享生产凭据。
- 🔐 **安全控制**：包括 Argon2id 主密码、AES-256 静态加密、TLS、JWT 组织访问、设备会话、MFA、审计日志；SOC 2 Type II 仍在审计中。
- 🔗 **安全分享**：公开报告链接可设置密码与过期时间，并可一键撤销；编辑类操作需权限加密码解锁或登录会话。
- 💻 **平台支持**：macOS、Windows、Linux 桌面端加 Web 版，即 3+1 平台；本地优先、默认离线，云同步为可选。
- 🔄 **使用流程**：连接（SRV/TLS/X.509/AWS IAM，自动识别副本集、分片、索引与 Schema）→ 提问/编写查询 → 分析建模 → 分享与权限控制。
- 💰 **定价模式**：Free $0；Basic $119/席/年；Pro $229/席/年（最多 10 席）；Ultimate $399/席/年（无限席等）；首席提供 30 天试用。
- 📦 **版本动态**：v1.2.19 已发布，新增 AI Report Assistant、密码保护分享、DuckDB Report Builder 等能力。
- 📈 **产品数据**：宣称包含 27 种聚合阶段、70+ 功能标志、12 项安全控制、3+1 平台；强调数据来自产品实际计数。
- 🧭 **差异化**：相比 Compass/Studio 3T，额外整合 AI 查询、BI 级报表、团队 RBAC 与密码保护分享，减少额外 BI 工具与发票。
- ⚠️ **限制提示**：免费版仅 1 个连接、3 个标签等；AI token、报告刷新频率、团队人数与并发操作按套餐分级。

---

### [免费照片和视频编辑器](https://www.reels-editor.com/)

**原文标题**: [Free Photo & Video Editor](https://www.reels-editor.com/)

您尚未提供需要总结的文章内容，因此暂时无法生成摘要。请补充文本后再试。

- 📄 请在“Use the following content:”后粘贴需要总结的文章内容
- ✍️ 我将用中文输出概览摘要与要点列表
- 📌 要点会使用“-”符号，并配合合适表情符号提炼关键信息

---

### [文本模式叠加层 | 将网页转换为文本模式](https://extension.textmode.art/)

**原文标题**: [Textmode Overlay | Turn the web into textmode](https://extension.textmode.art/)

Textmode Overlay 是一款免费开源的浏览器扩展，可将网页中可见的 canvas 或视频实时转换为文本模式艺术，并支持调节样式、叠加 GPU 后处理效果及本地导出；所有媒体处理均在本地完成，无需账户或遥测。

- 🖱️ 使用流程：从工具栏或页面右键菜单打开扩展，选择媒体后指向可见的 canvas 或视频。
- 🎨 样式调节：可调整密度、字符、颜色、轮廓、字体，并使用可重新排序的后处理效果栈。
- 💾 导出方式：支持将画面保存为 TXT、SVG、PNG 或 JPG，且导出全程本地完成。
- 🔄 实时转换：通过 WebGL2 覆盖层采样正在播放的媒体，并跟随其尺寸和位置。
- 🪟 独立面板：可拖拽控制面板通过 Shadow DOM 与宿主页面隔离。
- 🌓 亮度与轮廓：可基于亮度、边缘结构或两者结合生成效果。
- 🔤 字体库：内置 4 款字体，并可在浏览器配置中保存最多 10 个 TrueType 上传字体。
- ✨ 后处理效果：提供 16 个可重新排序的 GPU 滤镜，涵盖颜色、CRT 畸变、扫描线、泛光和颗粒等。
- 🧠 站点记忆：按主机名记住当前设置。
- 🔒 本地处理：零扩展遥测、零账户，所有媒体处理均在设备本地运行。
- 🌐 生态系统：包括 code.textmode.art、editor.textmode.art、create.textmode.art、export.textmode.art 和 automata.textmode.art，分别用于文档、实时编辑、视觉创作、导出转换和元胞自动机探索。
- ❓ 常见限制：仅能转换浏览器允许像素访问的可见 canvas 和视频，且需要 WebGL2；跨域限制、DRM、受保护播放或受污染画布可能导致采样失败。
- 🔐 权限与存储：字体和设置保存在扩展管理的本地存储中，不同步到远程；权限包括用户触发的临时活动标签页访问、脚本注入、右键菜单操作和本地扩展存储。
- 🆓 授权方式：Textmode Overlay 免费且基于 MIT License 开源。

---

### [Reicon - 面向设计师与开发者的开源图标库](https://reicon.dev/)

**原文标题**: [Reicon - Open-Source Icon Library for Designers & Developers](https://reicon.dev/)

概述摘要
- 📭 您尚未提供需要总结的文章内容，因此暂无法生成摘要。
- 📝 请粘贴或发送原文，我会按“概述摘要 + 表情符号要点”的格式整理。
- ✅ 输出将使用“-”符号列出关键信息，并保持简洁。

---

### [错误](https://metacleanai.com/exif-viewer/)

**原文标题**: [Error](https://metacleanai.com/exif-viewer/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='metacleanai.com', port=443): Max retries exceeded with url: /exif-viewer/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Web 工具周刊 - 推荐中心](https://recommendations.page/web-tools-weekly/offer_recommendations/offer_recommendation_0c51fd192198)

**原文标题**: [Web Tools Weekly - Recommendations Hub](https://recommendations.page/web-tools-weekly/offer_recommendations/offer_recommendation_0c51fd192198)

这是面向订阅者的 Surfshark VPN 专属优惠，最高可享 86% 折扣，主打无限设备连接、家庭保护及多项安全功能。

- 🔐 订阅者专享优惠：Surfshark VPN 套餐最高可享 86% OFF。
- ⚡ 快速 VPN 套装支持无限设备，一个账号可同时连接多台设备并保护全家。
- 🛠️ 设置简单，无需复杂配置。
- 🛡️ 包含恶意软件防护、防垃圾邮件和广告拦截功能。
- 🌐 提供专用 IP。
- 👉 可查看所有专属优惠。

---

### [粒子图表 — 由光构成的 JavaScript 图表](https://particlecharts.com/)

**原文标题**: [Particle Charts — JavaScript charts made of light](https://particlecharts.com/)

Charticles 是一个零依赖的粒子图表库，将数据渲染为动态粒子云，支持柱状图、折线图、气泡图、雷达图、饼图和环形图，并强调响应式、可访问性与纯 JSON 驱动。

- ✨ 六种图表共用同一粒子引擎：柱状图支持分组、堆叠或水平布局；折线图平滑单调不过冲；饼图直接标注；环形图中心显示实时总计；气泡图用尺寸表达第三值；雷达图呈现多指标轮廓。
- 🧩 零依赖、单文件：一个 `<script>` 标签即可使用，无需构建；同时提供 ESM 源码、npm 包、CommonJS 构建和 TypeScript 类型。
- 📐 响应式与 HiDPI：通过 `ResizeObserver` 在容器尺寸变化时重新布局，并自动处理高清屏。
- 📊 数据输入简单：支持数字数组、`{label, value}`、多系列对象和 `{x, y}` 点，气泡图额外支持 `{x, y, r}`。
- 🌟 粒子视觉：支持密度、大小、辉光、抖动、速度、形状等参数；粒子叠加到离屏层并经过两次模糊实现 bloom 发光。
- 🧭 自动图表元素：自动生成坐标轴、刻度、图例、提示框和十字准线；图例支持键盘切换系列。
- ♿ 可访问性友好：每张图附带屏幕阅读器数据表，遵循 `prefers-reduced-motion`，并在滚出视口时暂停。
- ⚙️ 配置灵活：除 `data` 外几乎所有选项可选；可设置主题、颜色、字体、轴/网格/图例/提示框，以及各图表类型的曲线、堆叠、气泡半径、雷达层级、环形图内半径等。
- 🛠️ 提供 `update`、`setOptions`、`resize`、`toDataURL`、`destroy` 等方法，支持数据切换、样式调整、强制重排、PNG 快照和销毁。
- 🚀 快速上手：容器需设置高度，通过 CDN 或 npm 安装后用三行代码创建图表；官方展示案例包括 DrawDojo 等。

---

### [](https://github.com/hafizovic/SubPulse)

**原文标题**: [GitHub - hafizovic/SubPulse: See how active the YouTube channels you subscribe to are: days since the last upload, posting frequency, Shorts vs. videos, and average length. Node.js + SQLite, no dependencies. · GitHub](https://github.com/hafizovic/SubPulse)

SubPulse 是一个自托管的 YouTube 订阅频道活跃度分析工具，基于 Node.js、SQLite 和原生 HTML/JS 前端构建，无需 npm 依赖或构建步骤。它通过 Google OAuth 读取订阅数据，按需同步并展示频道更新情况，同时内置 API 配额控制、共享缓存和本地数据管理。

- 🎯 核心功能：查看订阅频道距上次上传的天数、发布频率、Shorts 与普通视频的对比、平均视频时长。
- 🛠️ 技术架构：Node.js 服务器 + SQLite 数据库 + 静态前端；Node ≥ 22.13 使用内置 `node:sqlite`，无 npm 依赖、无构建步骤。
- ✅ 前置要求：需要 Node.js ≥ 22.13、Google 账号和 Google Cloud 项目；无需数据库服务器、Docker 或 `npm install`。
- 🔑 Google 配置：启用 YouTube Data API v3，创建 Web 类型 OAuth 客户端，配置重定向 URI 为 `http://localhost:5173/auth/callback`，并将 Client ID/Secret 填入 `.env`。
- 🚀 启动方式：复制 `.env.example` 为 `.env`，运行 `npm start`，打开 `http://localhost:5173`，登录后点击 Sync；首次启动会生成 `data/subpulse.db` 和 `encryption.key`。
- ⚙️ 关键配置：`PORT` 默认 5173 且仅绑定 localhost；还支持 `BASE_URL`、`DATA_DIR`、`DATABASE_PATH`、`CHANNEL_TTL_HOURS`、`YOUTUBE_DAILY_QUOTA`、`ENCRYPTION_KEY`。
- 🔄 使用机制：仅在点击 Sync 时调用 YouTube；登录和刷新只读数据库；会话持续 30 天，服务器保存加密的 Google refresh token。
- 📊 配额规则：每个需抓取的频道约消耗 3 个 API 单位，缓存复用不消耗；默认每日 10,000 单位，约 300 个订阅全量同步约用 900 单位，配额于太平洋时间午夜重置。
- 🗄️ 数据设计：包含 users、sessions、channels、subscriptions、api_usage 表；频道统计在 `CHANNEL_TTL_HOURS` 内共享缓存；无订阅引用 30 天后删除频道，30 天未同步删除用户订阅。
- 🔐 退订与隐私：每行有 Unsubscribe 按钮，首次使用需额外授权“管理 YouTube 账号”，每次退订消耗 50 单位且应用内无法撤销；“Disconnect & delete my data”会立即撤销访问并删除用户。
- 🧹 重置与迁移：删除 `data/` 可重置全部本地数据，仅删除 `encryption.key` 会强制所有人重新登录；迁移到 Postgres/MySQL 只需重写 `server/db.js`。
- ⚠️ 已知限制：频率和平均值仅覆盖各频道最近 ≤50 个上传；Shorts 播放列表非官方 API 功能，可能失效，标记 est. 时回退为 ≤60 秒判断；未验证应用最多 100 个测试用户，公开上线需 Google OAuth 验证、HTTPS 和隐私政策。
- 🧪 常见问题：Node 过旧会报 `node:sqlite` 缺失；`redirect_uri_mismatch` 需确保 URI 完全一致；`access_denied` 需添加测试用户；Testing 模式下 refresh token 约 7 天过期，需每周重新登录。

---

### [fontglyph | 免费浏览器内 SVG 转 WOFF2 Web 字体转换器](https://fontglyph.com/)

**原文标题**: [fontglyph | Free In-Browser SVG to WOFF2 Web Font Converter](https://fontglyph.com/)

这是一个完全免费、注重隐私的浏览器端图标字体工具，可将 SVG/PNG 图标创建、编辑、导入并导出为 WOFF2 图标字体，所有处理均在本地完成。

- 🎨 支持将 SVG 和 PNG 图标转换为 WOFF2 图标字体。
- 🛠️ 可在浏览器中创建、编辑、导入和导出自定义图标字体。
- 🔒 隐私优先：文件不上传、不进行云端处理，转换全程在本地浏览器完成。
- 💾 图标库仅保存在当前浏览器会话中，SVG 文件和生成的 WOFF2 字体不会离开设备。
- 🆕 可新建字体库，或通过拖放 `.woff2` 文件或输入 URL 导入现有字体库。
- 📦 支持管理字形，并可导出 SVG 与 WOFF2，包含单色和彩色版本。
- 🌐 可选发布到 CDN 以便全球网站快速访问，但公开链接会使图标库对知晓链接者可见。
- 🗑️ 提供删除库、发布到 CDN、导出等管理操作。
- 📥 支持拖放或从剪贴板粘贴 SVG/PNG，并显示字形数量与大小。
- 🆓 工具完全免费，页面还提供条款、举报/DMCA、点赞和请喝咖啡入口。

---

### [GitHub - JonasKruckenberg/imagetools：使用自定义导入指令工具箱加载和转换图像！· GitHub](https://github.com/JonasKruckenberg/imagetools)

**原文标题**: [GitHub - JonasKruckenberg/imagetools: Load and transform images using a toolbox of custom import directives! · GitHub](https://github.com/JonasKruckenberg/imagetools)

imagetools 是一个用于在编译时加载、转换和优化图片的工具库，通过自定义导入指令实现，底层图像处理由 sharp 提供支持，主要面向 Vite 等前端构建场景。

- 🧰 提供易用的导入指令，可在编译时转换和优化图片
- ⚙️ 所有图像变换能力均由 sharp 驱动
- 🚀 支持输出现代图片格式
- 🖼️ 支持调整图片尺寸
- 🔗 支持轻松生成 srcset 响应式图片
- ⚡️ 开发模式下运行速度快
- 🔒 可移除图片元数据
- 🧩 架构可扩展
- 📦 主要包包括 imagetools-core 和 vite-imagetools
- ⭐ 项目约 1.1k stars、83 forks、3 watchers，累计 868 次提交
- 📄 采用 MIT 许可证
- 🤝 欢迎提交 issue 或 PR 参与贡献，也支持赞助项目发展

---

### [](https://webtoolsweekly.com/contact?opt=classifieds)

**原文标题**: [Contact Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

本页面说明如何联系 Web Tools Weekly 进行广告咨询，并列出广告合作方式与咨询表单要求。

- 📢 若想咨询在 Web Tools Weekly 投放广告，可先查看“Advertising Plans”页面了解选项。
- ✉️ 需发送消息询问当前广告位可用情况。
- 📝 若要讨论具体方案或预订广告位，请填写页面下方表单。
- ⚠️ 该表单仅用于广告咨询，不处理其他类型问题。
- 💬 一般咨询、简报相关问题或工具提交，可通过 X 私信、Bluesky 聊天，或订阅后回复简报邮件联系。
- 📋 表单必填项包括：姓名、邮箱地址、要投放广告的 URL、期望广告方案、备注/说明。
- 📌 可选广告方案包括：顶部广告 + 顶部文字链接、付费产品评测、中部图片广告、文字链接组合、分类广告、广告互换。

---

### [AI 驱动的产品采用与用户引导平台 | Userflow](https://www.userflow.com/)

**原文标题**: [The AI-Powered Product Adoption & Onboarding Platform | Userflow](https://www.userflow.com/)

Userflow 是面向 PLG（产品驱动增长）团队的 no-code 应用内引导与产品采用平台，帮助产品、增长、客户成功和营销团队提升新用户上手、功能采用、留存与转化，并通过 FlowAI 系列能力实现智能生成流程、识别摩擦点和自动推荐或执行解决方案。

- ⭐ 在 G2 上获得 4.8 分，受到 800+ 关注客户的团队信任。
- 🚀 核心价值：软件构建越来越容易，但让用户真正使用更难；Userflow 通过应用内引导覆盖从首次“啊哈时刻”到长期留存的全过程。
- 🧩 无需代码：产品、增长、客户成功团队可自行搭建个性化 tours、checklists、tooltips、announcements、banners 和触发式引导。
- 🎯  onboarding：按用户角色、套餐或已有行为提供个性化引导，帮助新用户尽快获得首次成功。
- 📈 采用与增长：在合适时机向正确用户展示新功能，把发布转化为使用和收入。
- 🛟 降低流失：FlowAI Signals 可识别流程中的掉点和困惑步骤，并推荐应用内修复方案。
- ⚡ FlowAI Builder：可从真实产品中生成完整 onboarding 流程，自动匹配品牌风格，并即时优化或本地化文案。
- 🔍 FlowAI Signals：持续分析应用内体验和 AI 对话，发现反复掉点、知识缺口和用户主要痛点。
- 🤖 Adoption Agent：不仅回答问题，还能结合上下文推荐并启动相关流程，甚至通过 Action Flows 代用户完成多步骤任务。
- 🔁 Action Flows：把洞察转化为干预，基于真实行为一键启动 walkthroughs、checklists 或情境引导，形成“发现问题—推荐方案—执行修复”的闭环。
- 🔌 Userflow MCP：可连接 Claude、ChatGPT 等兼容 MCP 的 AI 工具，用自然语言起草流程、创建分群、查看表现，所有套餐均包含读写权限。
- 👥 适用团队：产品与增长、客户成功、客户营销；尤其适合自助式、PLG、Web 产品、多用户路径和频繁发布的 B2B SaaS 团队。
- 🧱 集成与落地：可与现有技术栈配合，强调轻量设置、避免脆弱集成，并保持数据连接。
- 💬 客户成效示例：某客户实现价值时间缩短 50%、产品采用率提升 45%。
- 💳 定价：Essentials 为 300 美元/月或年付 240 美元/月；Studio 为 500 美元/月或年付 400 美元/月，包含 Adoption Agent；Enterprise 定制报价。Essentials 和 Studio 均含 1,000 MAU，并随用量扩展。
- 🆓 提供 14 天免费试用和 demo；首个应用内体验或 agent 可在几分钟内上线。

---

### [Yven — 面向小型和单人网络工作室的简易客户资产管理](https://yven.ca/?mtm_campaign=WebToolsWeekly)

**原文标题**: [Yven — easy client asset management for small and solo web shops](https://yven.ca/?mtm_campaign=WebToolsWeekly)

Yven 是面向小型和单人网站工作室的客户资产管理工具，把每个客户的域名、登录入口、续费日期、服务和工作时数集中在一处，支持快速搜索、工时记录与开票，并用续费摘要防止遗漏。它更像“客户资产登记与计费工具”，不是网站监控、密码管理器或完整 CRM。

- 🧭 核心痛点：靠 Ctrl-F、浏览器标签和零散表格管理客户并不可持续，信息容易散落在邮件、发票和多个后台中。
- 🗂️ 集中管理客户资产：为每个客户记录站点、域名、DNS、托管、SSL、邮箱、订阅、负责人、付款方和续费日期。
- 🔍 快速查找与记录：按“/”可同时搜索客户、站点、服务和发票；按“W”可在 30 秒内记录工作。
- 📥 快速导入：可用免费客户资产跟踪模板导入现有表格，映射列后约 3 分钟完成迁移。
- ⏱️ 工时与开票：小额请求和完整项目都可记录，按小时或固定费汇总到一张发票；内置开票已可用，QuickBooks 和 FreshBooks 推送即将推出。
- 🔔 续费摘要：每天一封按紧急程度排序的摘要，覆盖域名、证书和订阅，显示由谁付款，并提前提示自动续费。
- 💸 续费与加价：标记续费后自动顺延日期；可记录工时并生成发票；转售服务加价对客户保密。
- 🔐 安全与边界：不存储密码，只保存指向密码管理器的指针；不监控站点、不代续费、无客户登录，客户通过私密链接查看共享记录。
- 🧩 适用边界：适合单店账户，不是团队角色型 CRM；可与监控、CRM、ManageWP 等工具配合使用。
- 💳 定价与背景：21 天试用，一个套餐包含全部功能；创始价 CA$175/年或 CA$19/月，前 100 名后为 CA$249/年或 CA$29/月；由 Darren Harkness 为单人网站工作室打造，加拿大制造，数据可随时导出。

---

### [Unicorn Studio — 打造可交付的交互式图形](https://www.unicorn.studio/)

**原文标题**: [Unicorn Studio — Craft Interactive Graphics that Ship](https://www.unicorn.studio/)

通过可视化画布设计可交付上线的交互式图形，创建具备着色器、媒体、3D 与动态交互效果的生产级 Web 组件。
- 🚀 打造可实际发布的交互式图形
- 🧩 设计生产级 Web 组件
- 🎨 支持着色器、媒体与 3D 内容
- ✨ 集成交互式动态效果
- 🖼️ 在可视化画布中完成创作

---

### [API 设计、测试与文档平台 — Routebase](https://routebase.dev/)

**原文标题**: [API Design, Testing & Documentation Platform â Routebase](https://routebase.dev/)

Routebase 是一个基于单一“活”OpenAPI 规范的 API 设计、测试与文档平台：规范只需修改一次，文档、Mock 服务器、测试和监控便会同步更新，从而避免文档过期与契约漂移。

- 🎯 核心价值：解决 API 文档容易过期的问题，让文档、Mock、测试和监控始终围绕同一份规范保持同步。
- 🧩 API 设计：提供可视化 OpenAPI 编辑器，支持导入现有规范、复用 Schema、规范分支与治理规则，减少手写 YAML。
- 🚀 一键发布：发布版本后自动生成文档门户和 Mock 服务器，测试与监控也验证同一版本。
- 🧪 测试与开发：前端可基于 Mock 开发，QA 可在 CI 中运行测试套件；支持 HTTP 请求测试、声明式断言、场景链路、定时任务和 CI 门禁。
- 🛰️ 漂移监控：定时将真实响应与规范比对，发现缺失字段、类型不匹配、未记录新增等内容，并提供字段级差异和告警。
- 🤖 AI 与 MCP：内置 MCP 服务器，Claude、Cursor 等代理可按团队权限设计、检查和测试 API；文档门户支持 Markdown 响应与 Agent 就绪度评分。
- 🌿 协作流程：支持规范分支、合并请求、评审审批、冲突检测和破坏性变更检查。
- 📦 兼容与导入：可导入 OpenAPI、Postman、Insomnia 集合；没有规范也可从空规范或模板开始，测试不强制依赖 OpenAPI。
- 🔐 数据驻留：注册时可选择欧盟或美国数据区域，均运行在 Microsoft Azure 上。
- 💳 定价与试用：提供 14 天 Pro 试用，无需信用卡；免费版永久可用；Starter、Pro、Enterprise 按用户/月计费，年付最高节省 18%。
- 🏢 企业能力：Enterprise 25 席起可自助订阅，包含 SAML SSO、SCIM、审计日志导出、专属支持与 SLA。
- 🛒 购买方式：Starter、Pro、Enterprise 也可通过 Microsoft Marketplace 购买；可随时取消，数据保留并降级至免费版。

---

### [学习 Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

**原文标题**: [Learn Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

未提供可摘要的文章正文，因此目前无法生成内容要点；请补充文本后再试。
- 📄 当前输入在“Use the following content:”之后没有实际文章内容。
- ✍️ 请粘贴需要总结的完整文本。
- 🧾 收到内容后，我会按“概述 + 表情符号要点”的格式进行中文总结。

---

### [Mowgli：面向移动端、Web 和桌面应用的 AI 设计工具](https://mowgli.ai/)

**原文标题**: [Mowgli: AI design tool for mobile, web & desktop apps](https://mowgli.ai/)

该文本包含大量重复的“Browse example”占位内容，核心是在介绍 Mowgli：一个面向移动端、Web 和桌面应用的 AI 设计画布，强调以规格驱动的方式，将想法、设计、原型、协作与开发交接整合到同一平台中。

- 🎨 Mowgli 是 AI 设计画布，可快速设计、实验和制作移动端、Web 与桌面应用原型。
- 🧭 采用规格驱动模式，将流程、用户旅程和设计集中在一个画布中，并持续维护产品上下文。
- 🚀 支持从零开始描述想法并完成范围问卷，也可导入 Figma 文件或通过 MCP 连接编码代理导入现有产品。
- 🖼️ 提供情绪板功能，可探索 16+ 种定制视觉风格，混搭参考并确定色彩、字体和设计方向。
- 📱 可为整个产品生成高保真设计，覆盖每个屏幕、状态和流程，而不仅是顺利路径。
- 💬 通过聊天快速迭代设计，支持微调、新流程和重设计，规格保持同步，并提供实时协作与分享。
- 🔌 可连接 Claude Code、Codex、Cursor 等 MCP 应用，实现设计与代码双向同步；也可导出 Figma、React + Tailwind 代码和详细规格。
- 🧩 关键功能包括 AI 设计生成、原型交互、Figma 导入、对话式设计编辑、样式引导和响应式适配。
- 🗂️ 示例项目涵盖 Datadog Lite、LangSmash、Social Feed、Whitfield Dashboard、iOS UI Kit、PostHog 等。
- ⭐ 用户评价强调其提升视觉开发效率、保持品牌与设计系统一致性、加快从想法到交付的流程。
- 📚 页面还提供 FAQ 和博客内容，涉及 AI 设计工具、MCP 服务器、Claude Code UI 工作流等主题。
- ✅ 提供免费试用、演示入口，并鼓励用户免费启动产品设计。

---

### [](https://www.suprsend.com/)

**原文标题**: [Notification Infrastructure for email, sms, slack, push, inbox | SuprSend](https://www.suprsend.com/)

SuprSend 是面向现代应用的通知基础设施平台，帮助团队统一发送产品、交易与营销通知，覆盖所有渠道，并可在控制台、Claude、Slack 等环境中管理；平台已支撑每月 1 亿 + 通知，定位为生产级通知栈。

- 🚀 核心价值：把通知从代码中的 `send()` 升级为可管理、可扩展的基础设施，减少工程负担并加快上线。
- 🧩 主要能力：无代码工作流、WYSIWYG 模板编辑器、运行时数据建模、通知分析、实时应用内收件箱、广播、偏好中心、列表、集成与多租户。
- 🔔 高级通知逻辑：支持批处理/摘要、等待条件、时区感知、分支、智能渠道路由和 AI Agent 节点。
- 🤖 AI 与开发者工具：提供 MCP Server、Agent SDK、SuprSend Agent、CLI、API/SDK，可用自然语言、IDE 或终端创建和管理通知。
- 🏢 多租户与个性化：可为租户定制模板、偏好和路由，并支持按租户隔离通知。
- 📥 应用内收件箱：提供可定制 React 组件、Headless API、实时同步、标签/筛选/已读未读等能力，约 30 分钟可上线。
- ⚙️ 开发者体验：支持自动化部署、JSON Schema 校验、实时逐步日志、可观测性、Webhook/S3 数据同步及原生集成。
- 🔐 可靠与安全：面向企业级安全、合规、规模化和治理，提供回退、路由、重试，并支持 BYOC/自托管。
- 📈 典型用例：交易通知、协作提醒、多租户通知、批量摘要、定时提醒、公告/新闻通讯和产品更新。
- 💬 客户收益：案例称可减少 80% 支持工单、节省 600+ 开发小时，让产品团队无需工程支持即可管理通知并加速部署。
- ✅ 行动入口：提供免费开始、演示请求、文档和 Playground，强调快速上线与可扩展通知体验。

---

### [](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

**原文标题**: [Today's PHP Security Release, and How We're Strengthening PHP Security — The PHP Foundation — Supporting, Advancing, and Developing the PHP Language](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

文章概述：PHP 项目发布关键安全更新，修复两个可导致未认证远程代码执行的高危漏洞；文章复盘了漏洞发现与修复延迟、PHP 安全组织改进、披露过程受扰事件，并呼吁依赖 PHP 的机构资助基金会以加强长期安全能力。

- 🚨 PHP 发布 8.5.12、8.4.27、8.3.36 和 8.2.35，修复两个关键漏洞，运行 PHP 的服务器应立即更新。
- 🐞 两个漏洞分别是 OOM 内存损坏（CVE-2026-109618）和过期全局状态导致释放后使用（CVE-2026-109619），位于内存管理和错误处理等核心路径，影响严重且修复需权衡兼容性、性能和第三方扩展生态。
- 🧭 2024 年外部安全审计后已发现 OOM 问题迹象；但因安全团队共识决策困难、资源不足且缺乏已知 RCE 路径，修复多次停滞，文章承认这是结构性失败，并已开始改变决策流程。
- 🛡️ PHP Foundation 加强安全组织：2026 年 5 月成立 Ecosystem Security Team，增加专职人员，引入 AI 工具、sanitizer 构建和复现环境，并推动 Patch the Planet、Calif、OpenAI、Wiz、Trail of Bits 等审计与报告。
- 🤖 AI 辅助研究使漏洞报告激增；团队自 7 月 1 日以来发布 15 个 CVE，处理 100 多份无效、重复或不可复现报告，但每个判断和补丁仍由人工完成。
- 📣 披露过程受到干扰：CVE 编号提前泄露且附带错误发布时间和错误 CVSS 分数（实际为 9.2 而非 10.0）；PHP 提前预公告并调整发布时间；Calif 误发 PoC 视频，Chainguard 在协调发布前 6 个多小时发布含修复镜像，破坏禁运。
- ✅ 修复已在所有支持分支交付，发行版和 LTS 厂商提前获得补丁；基金会表示将改进流程，使未来需要复杂权衡的漏洞更快解决。
- 💰 文章呼吁依赖 PHP 的公司、托管商、云平台、发行版以及政府与公共机构资助 PHP Foundation，以扩充深谙 PHP 代码库的安全工程师并可持续处理结构性问题。
- 🙏 文章感谢 PHP 安全团队、发布经理、发行版维护者、报告漏洞的研究机构、提供工具与资金的机构以及所有赞助者。

---

### [Denys Cherednychenko 在 X 上：“有人能像给 6 岁](https://x.com/Denche2005/status/2112997524319752587)

**原文标题**: [Denys Cherednychenko on X: "Can someone explain the PHP vulnerability to me like I'm a 6-year-old?

Should I be worried or just avoid PHP developers for the next 48 hours?" / X](https://x.com/Denche2005/status/2112997524319752587)

一位开发者就近期披露的 PHP 漏洞在社交平台发文，希望有人用“给 6 岁小孩讲解”的方式说明情况，并半开玩笑地询问自己是否需要担心，还是干脆在未来 48 小时内避开 PHP 开发者。

- 🐘 发帖人询问能否用极其通俗、像讲给 6 岁小孩听的方式解释这轮 PHP 漏洞
- 😟 他关心的问题是：普通人是否真的需要为此担忧
- 🙈 他调侃是否应“在未来 48 小时内避开 PHP 开发者”，反映出对漏洞影响的焦虑与不确定
- 📣 该帖发布于 2026 年 10 月 21 日晚 8 点，获得约 210 万次浏览
- 💬 互动数据包括 294 条回复、185 次转发、5600 次点赞和 2300 次收藏，说明话题关注度较高
- 🔍 帖子本身没有给出漏洞技术细节，主要体现社区对 PHP 安全性事件的快速反应与求助心态

---

### [路易斯·拉扎里斯 (@LouisLazaris) / X](https://x.com/LouisLazaris)

**原文标题**: [Louis Lazaris (@LouisLazaris) / X](https://x.com/LouisLazaris)

路易斯·拉扎里斯（Louis Lazaris）是一位科技创业者与内容创作者，运营两份技术通讯，并在社交平台上保持活跃；其主页展示了个人身份、业务链接、网站及关注数据。

- 👤 账号信息：Louis Lazaris，用户名 @LouisLazaris
- 🪑 个人简介：自称“Chairman of the Bored”
- 📰 创办两份科技通讯：webtoolsweekly.com 与 techproductivity.co
- 🔗 提供个人链接聚合页：bio.link/louislazaris
- 💼 身份标签：Entrepreneur（创业者）
- 📍 地点信息：显示为加拿大多伦多，原文写作“Torontocisco, Canadafornia”
- 🌐 个人网站：impressivewebs.com
- 📅 加入时间：2009 年 5 月
- 📊 社交数据：关注 717 人，粉丝 5,471 人
- 🗂️ 主页分区：包含帖子、回复、转发、媒体等内容
- 🔇 其他内容：页面包含登录、注册等平台导航信息，非核心资料

---

### [Bluesky 上的 @louislazaris.com](https://bsky.app/profile/louislazaris.com)

**原文标题**: [@louislazaris.com on Bluesky](https://bsky.app/profile/louislazaris.com)

路易斯·拉扎里斯（Louis Lazaris）是前端开发者与新闻简报策划人；他的 Bluesky 资料汇总了个人网站、多个技术/效率/VS Code 相关项目，以及面向吉他爱好者的 YouTube 频道。

- 👤 姓名：Louis Lazaris；个人网站：louislazaris.com
- 🧑‍💻 身份：前端开发者、新闻简报策划人
- 🆔 Bluesky DID：did:plc:6if43vohxmohxuooa7bkkw5q
- ⚙️ 运营 Web Tools Weekly：https://webtoolsweekly.com
- 💼 提供 Tech Productivity：https://techproductivity.co
- 💻 维护 VS Code Email：https://vscode.email
- 🎸 开设面向吉他玩家的 YouTube 频道：youtube.com/@tunejotter
- 🌐 平台提示：需启用 JavaScript 才能使用 Bluesky；可在 bsky.social 与 atproto.com 了解更多

---

### [向《网络工具周刊》提交工具](https://webtoolsweekly.com/submit)

**原文标题**: [Submit a Tool to Web Tools Weekly](https://webtoolsweekly.com/submit)

这份内容征集面向前端开发者、程序员和设计师的实用工具推荐，可通过 X 或 Bluesky 提交，并说明了可接受的工具类型与排除项。

- 🛠️ 如果你开发或了解对前端开发者有用的工具，可通过 X 或 Bluesky 提交推荐。
- 📩 在 X 上可私信 @LouisLazaris；在 Bluesky 上可联系 @LouisLazaris.com。
- 📚 可提交类型包括：库、框架、插件、脚本、Web 应用、桌面应用、移动应用、API/服务、编辑器/IDE 等。
- 💡 也欢迎提交任何你认为对 Web 开发者、程序员或设计师有用的其他工具。
- 🚫 请勿提交文章或教程，这类内容不会被收录。
- 📰 生产力相关工具已转移到另一份通讯 Tech Productivity，也可通过上述方式提交。

---

### [头条 | 猜年份 | 每日历史游戏](https://www.headlines.games/)

**原文标题**: [Headlines | Guess the Year | Daily History Game](https://www.headlines.games/)

未提供可总结的文章内容，因此暂时无法提取关键信息。
- 📄 请在“Use the following content:”后粘贴需要总结的正文。
- ✍️ 收到内容后，我会用“- + 表情符号”的格式列出要点。
- 🧾 并在顶部附上简短的中文概述，不添加总结标题。

---

### [Web 工具周刊 | 面向前端开发者的每周通讯](https://webtoolsweekly.com/)

**原文标题**: [Web Tools Weekly | A Weekly Newsletter for Front-end Developers](https://webtoolsweekly.com/)

Web Tools Weekly 是一份面向 Web 开发者和前端开发者的每周邮件通讯，订阅人数达 15,905，每周发送一封，强调无垃圾邮件，并说明订阅后的数据收集、存储与跟踪政策。文章主要通过读者反馈展示其口碑，读者普遍称赞它能帮助发现新工具和库、提供实用 JavaScript 技巧，是值得长期订阅的高价值技术通讯。

- 📬 定位清晰：面向 Web 开发者的每周工具通讯，尤其适合前端开发者获取新工具与资源。
- 👥 订阅规模：现有 15,905 名订阅者，每周发送一封邮件。
- 🔒 订阅与隐私：订阅即同意接收邮件，并同意按 EmailOctopus 的隐私政策与条款存储和跟踪数据；表单受 reCAPTCHA 保护，适用 Google 隐私政策与服务条款。
- 💬 读者口碑：大量读者主动表达赞赏，称其通过“awesome test”，是出色的 Web 开发通讯。
- 🧰 实用价值：读者认为它能持续带来新工具、新库和实用 JS 技巧，常能找到日常可用的资源。
- ⭐ 长期认可：多位读者订阅多年，表示每周期待阅读，甚至从未错过一期，并称其为最好的技术通讯之一。

---

