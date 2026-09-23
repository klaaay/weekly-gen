### [](https://tinyjs.app/)

**原文标题**: [tinyjs — desktop apps for macOS, Windows, and Linux in ~6 MB](https://tinyjs.app/)

tinyjs 是一个约 6MB 的 JavaScript 桌面应用运行时，使用操作系统自带的 WebView（macOS 的 WebKit、Windows 的 WebView2、Linux 的 WebKitGTK），后端基于 txiki.js（QuickJS + libuv）提供完整系统访问，无需 Electron、Chromium、HTTP 服务器或端口，旨在用纯 JavaScript 构建轻量原生桌面应用。

- 💾 安装方式：macOS/Linux 用 `curl -fsSL https://tinyjs.app/install | sh`；Windows 用 `irm https://tinyjs.app/install.ps1 | iex`；MIT 许可，Windows 11 预装 WebView2。
- 📦 极小体积：打包应用约 6MB，其中 5.6MB 为 txiki.js 运行时，约 380KB 为窗口启动器，其余为用户 HTML/CSS/JS；对比 Electron ≥150MB、Tauri ~10MB、Neutralino ~3MB。
- 🖥️ 原生窗口与零端口：使用系统 WebView，无捆绑 Chromium；页面与后端通过私有临时目录中的 Unix socket（Windows 为命名管道）进行 RPC，无监听端口、无冲突、无扫描。
- ⚙️ 完整系统访问：后端支持文件、套接字、进程、FFI、SQLite、fetch、WebSocket 等，无需 Node 即可运行。
- 🔄 开发体验：热重载——前端编辑实时替换到窗口，后端编辑重启进程；开发无需构建步骤。
- 🪟 原生界面：真实菜单栏（含 About/Quit）、文件面板、原生 alert/confirm/prompt，由 AppKit 等系统组件提供。
- 📦 打包与分发：`tinyjs build` 生成已代码签名、可公证的 .app 包；支持 `--dmg`、`notarize`、`publish`，内置更新器验证 sha256 和签名，支持回滚。
- 🌐 包装托管应用：可将窗口指向 URL，具备浏览器行为（对话框、下载、弹窗、查找），并通过 `tinyjs.json` 的能力门控按 origin 控制原生 API 访问。
- 🤖 代理就绪：每个项目附带技能文件，编码代理可直接了解完整 API。
- 📲 示例应用：shelf（应用商店，4.4MB）、amp（Winamp 风格播放器，支持 MIDI 和 tracker 模块）、Nib（Markdown 编辑器）、Platter（唱片播放器）、World Clock（菜单栏世界时钟）、Tiny Deck（API 演示）。
- 🚀 快速开始：`tinyjs new myapp` → `tinyjs dev`（热重载）→ `tinyjs build`（签名包）；后端在 `src/main.js` 定义 API，页面通过 `tiny.api.call` 调用。
- 🧱 架构分层：页面（HTML/CSS/JS）↔ `tiny.api.call/on` ↔ 启动器（WebKit/WebView2/WebKitGTK）↔ Unix socket/命名管道 ↔ 后端 txiki.js。
- ⚖️ 与 Electron 对比：Electron 捆绑 Chromium 和 Node，≥150MB，无端口；tinyjs 用系统 WebView 和 5.6MB JS 运行时，约 6MB；放弃统一渲染引擎和原生 Node 插件，保留纯 JS 全栈。
- ⚖️ 与 Tauri 对比：Tauri 后端为 Rust 需编译，~10MB，系统 WebView，无端口；tinyjs 后端为 JavaScript 无需编译，OS 功能（对话框、菜单、托盘、剪贴板、钥匙串、通知、全局热键、自启动、深链）内置为 API；Tauri 生态、移动端和跨平台打包更成熟。
- ⚖️ 与 Neutralino 对比：Neutralino 无后端运行时，页面侧通过 localhost WebSocket 代理 OS API，~3MB；tinyjs 有真实 JS 进程，完整系统访问，通过 0700 临时目录的 Unix socket 通信，无端口。
- 🌍 跨平台差异：渲染引擎不同（WebKit/WebView2/WebKitGTK），需分别测试；Linux 编解码依赖 GStreamer，Web Audio 在 WebKitGTK 下有爆音；优点是不捆绑引擎，随 OS 更新，减少 CVE 发布压力。
- 🧑‍💻 前端框架支持：通过 Vite 模板支持 React、Vue、Svelte、Solid、TypeScript；TypeScript 后端用 esbuild 打包；默认模板零依赖、纯 HTML/CSS/JS、无构建步骤。
- 📦 Node 依赖：运行时和 CLI 基于 txiki.js，无需 Node；仅 Vite 模板在开发和构建时需要 Node/npm，不随应用发布；原生 Node 插件不可用，纯 JS 包可打包。
- 🏗️ 构建限制：不能在 Mac 上构建 Windows 应用，需在目标 OS 构建；CI 矩阵可一次发布三平台。
- ✅ 生产状态：macOS 稳定，Windows/Linux 为 beta；MIT 许可；未移植的原生调用会干净失败或返回 null，便于特性检测。
- 📱 平台限制：仅桌面（macOS、Windows、Linux），不支持 iOS/Android。
- 💡 体积构成：5.6MB 为 txiki.js（QuickJS、libuv、SQLite、wasm），约 380KB 为启动器；若去掉 wasm 和 SQLite 可节省约 2MB，但仅为方向而非承诺。

---

### [GitHub - saghul/txiki.js：一个微型 JavaScript 运行时 · GitHub](https://github.com/saghul/txiki.js/)

**原文标题**: [GitHub - saghul/txiki.js: A tiny JavaScript runtime · GitHub](https://github.com/saghul/txiki.js/)

txiki.js 是 saghul 开发的小型但强大的 JavaScript 运行时，基于 QuickJS-ng 和 libuv，目标是支持现代 ECMAScript 并兼容 WinterTC；项目采用 MIT 许可，约 3.2k stars、229 forks，完整文档位于 txikijs.org。

- 📛 名称含义：txiki 在巴斯克语中意为“小、微小”，项目名为 txiki.js。
- 🧠 技术核心：使用 QuickJS-ng 作为 JavaScript 引擎，libuv 作为平台层。
- 🚀 快速开始：`git clone --recursive ... && cd txiki.js`，然后 `make`，最后运行 `./build/tjs` 进入 REPL。
- 🌐 Web 平台 API：支持 `fetch`、`WebSocket`、`Console`、`setTimeout`、`Crypto`、Web Workers 等。
- 🔌 网络与系统能力：支持 TCP、UDP、Unix sockets、HTTP server + WebSocket、文件 I/O、子进程和信号处理。
- 📚 标准库：提供 `tjs:sqlite`、`tjs:ffi`、`tjs:path`、`tjs:hashing` 等模块。
- 📦 编译分发：可通过 `tjs compile` 生成独立可执行文件。
- 🖥️ 平台支持：支持 GNU/Linux、macOS、Windows，以及其他 Unix 系统；Windows 支持有详细构建说明。
- 📖 文档：完整文档位于 txikijs.org。
- 📊 仓库状态：公开仓库，拥有 3.2k stars、229 forks、44 watchers、16 issues、2 pull requests、1,406 commits；主分支为 master，目录包含 `src`、`tests`、`deps`、`examples`、`website` 等。
- 🏷️ 许可与主题：采用 MIT 许可证；主题包括 javascript、libuv、quickjs、wasm；由 saghul 和贡献者共同构建。

---

### [](https://blackboard.sh/electrobun/)

**原文标题**: [Electrobun - Build ultra fast, tiny, cross-platform desktop apps](https://blackboard.sh/electrobun/)

Electrobun 2.0 已发布，主打超快、极小、跨平台桌面应用；它统一支持多语言与多种渲染后端，并带来 Hutch CLI、Cottontail 运行时、Warren 响应式框架、30 个模板，以及差分更新、签名、双发布通道等内置能力。

- 🚀 Electrobun 2.0 发布，用于构建超快、小巧、跨平台桌面应用，Hello World 压缩下载约 1 MB。
- 🧩 同一框架支持 TypeScript、Zig、Rust、Go、Odin，渲染可选系统 WebView、Chromium 或 WGPU。
- 📦 体积对比：Electrobun 原生主进程 1.28 MiB，Cottontail 约 15 MiB，典型 Electron 约 85 MiB（macOS ARM64、系统 WebView 渲染器）。
- 🛠️ 新 CLI Hutch：统一管理包、脚本、打包、固定工具链与发布，替代 npm、Bun 和旧 Electrobun CLI。
- ⚡ 新运行时 Cottontail：基于 Zig 与 JavaScriptCore 的 TypeScript 运行时，关键处兼容 Node.js/Bun 且更小。
- 🎛️ 新 Warren：受 SolidJS 启发的细粒度响应式框架，可写入原生 GPU 表面，或驱动 WebView 内的 UI。
- 🧬 六种主进程/语言：默认 TypeScript，可选 Zig、Rust、Go、Odin，共享核心、构建工具与打包流程。
- 🗂️ `hutch electrobun init` 提供键盘导航模板选择器，内置 30 个起始模板。
- 🔄 差分更新：zig-bsdiff 支持小至 4 KB 更新，可对接 S3、R2 或静态文件托管，无需更新服务器，并支持全量下载回退。
- 🗜️ 发布包为 Zstd 自解压包，首次运行会验证、解压并启动。
- 🔐 内建代码签名与公证：macOS 生成 DMG，Windows 生成 setup 可执行文件，Linux 提供自解压安装器。
- 🎮 three.js 与 Babylon 适配器：可从 Cottontail/Bun 控制原生 GPU 窗口，以及合成到 WebView 上的表面。
- 🌐 默认系统 WebView 保持体积小；可选打包固定 Chromium/CEF，以统一各平台渲染引擎。
- 🧪 内置 Canary 与生产两个独立发布通道。
- 🧰 30 个模板覆盖 Web 框架、应用骨架、GPU/原生、Warren UI 实验性界面等场景。
- 🏢 Dash 桌面产品端到端基于 Electrobun 2.0：Hutch 构建、Cottontail 运行、Warren 渲染部分界面、二进制差分更新。
- 📥 安装：macOS/Linux 使用 curl 脚本，Windows 使用 PowerShell；随后运行 `hutch electrobun init` 创建应用。

---

### [](https://www.perryts.com/)

**原文标题**: [Perry â Compile TypeScript to Native Executables | TypeScript Native Compiler](https://www.perryts.com/)

Perry 是一个将 TypeScript 直接编译为原生可执行文件的工具链，通过 SWC 解析、LLVM 生成机器码，静态链接自研运行时与 GC，无需 Node.js 或外部 JavaScript 引擎即可运行于桌面、移动、可穿戴、电视及 Web/WASM 等平台。

- 🚀 **核心定位**：Perry 把 TypeScript 编译成原生 GUI 与 CLI 应用，覆盖 macOS、iOS、iPadOS、visionOS、tvOS、watchOS、Android、Wear OS、Windows、Linux 与 Web/WASM，共 11 个正式目标，HarmonyOS 为独立预览。
- ⚙️ **编译流程**：TypeScript → SWC 解析 → Perry HIR（单态化）→ LLVM 代码生成 → 原生二进制，全程无中间 JavaScript。
- 📦 **无外部引擎**：Perry 运行时与垃圾回收器静态链接进各平台二进制，默认不依赖 Node.js、Bun、Deno 或 V8；可选 `--enable-js-runtime` 启用 V8 回退以兼容部分 npm 包。
- 💾 **体积与启动**：Hello World 约 330 KB，Mango 应用约 7 MB；macOS 运行时基准约 3.2 ms（Apple M 系列）。
- 🧵 **真多线程**：提供 `parallelMap`、`parallelFilter`、`spawn` 等真实 OS 线程，默认拒绝可变捕获，配合 SharedArrayBuffer 与 Atomics 做共享内存协调。
- 🎨 **原生 UI 组件**：35+ 原生控件映射到 AppKit、UIKit、GTK4、Win32、Android SDK、SwiftUI（手表）及 Web 的 DOM/CSS 桥。
- 🌍 **编译期 i18n**：自动提取字符串、支持 30+ 区域 CLDR 复数规则，翻译在编译期校验并烘焙进二进制。
- 🧩 **插件与包生态**：模块可在构建期组合、静态依赖可变为直接原生调用；约 50 个原生包与 Node API 实现（mysql2、pg、bcrypt、axios、sharp、lodash 等），53 个模块被跟踪，覆盖约 97% Node 测试套件。
- ✅ **语言支持**：完整支持数字、字符串、布尔、数组、对象、类、泛型、接口、联合类型、async/await、闭包等；Proxy、eval、动态 import、装饰器、弱引用等为部分或暂不支持。
- 📊 **基准测试**：在阶乘、闭包、二叉树、JSON 往返等项目上优于 Node.js 与 Bun；在素数筛、矩阵乘法上落后；结果因工作负载而异，非通用速度承诺。
- 🚢 **发布流程**：`perry publish` 支持构建、签名、打包、验证与提交，可发布到 App Store、Play Store 或直接分发；本地编译免费且为 MIT 许可。
- 🛠️ **上手方式**：支持 npm/npx、Homebrew、APT、winget 或源码安装，安装后用 `perry doctor`、`perry compile main.ts`、`perry check ./src` 验证工具链与兼容性。
- 🔗 **周边项目**：Coop 将 Perry 兼容的 TypeScript 目录转为原生应用库并通过 HTTP 服务，每台机器共享运行时与标准库，支持部署、检查与回滚。

---

### [](https://www.electronjs.org/)

**原文标题**: [Build cross-platform desktop apps with JavaScript, HTML, and CSS | Electron](https://www.electronjs.org/)

Electron 通过内嵌 Chromium 和 Node.js，将 JavaScript 带入桌面端，帮助开发者用 Web 技术构建跨平台原生应用，并简化开发、更新、分发、商店发布与崩溃监控。

- 🌐 基于 Web 技术：Electron 嵌入 Chromium 与 Node.js，让 JavaScript 可开发桌面应用。
- 💻 跨平台：应用可在 macOS、Windows、Linux 及所有支持架构上原生运行。
- 🧩 开源开放：Electron 是 OpenJS 基金会下的开源项目，由活跃社区维护。
- 🛡️ 稳定安全：捆绑 Chromium 构建，提供稳定渲染目标，并与 Chromium 同步获得安全修复。
- 🔌 可扩展：可使用 npm 生态中的任意包，或编写原生附加组件来扩展 Electron。
- 🏢 广受信任：1Password、Discord、Figma、GitHub Desktop、Notion、Slack、VS Code 等应用均在使用。
- 🪟 原生图形界面：通过主进程 API 定制窗口、菜单，并使用对话框或通知提醒用户。
- 🔄 自动更新：内置 autoUpdater 模块，基于 Squirrel，可向 macOS 和 Windows 用户推送更新。
- 📦 应用安装包：借助社区工具生成 .dmg、.msi、.rpm 等平台专用安装包。
- 🏪 应用商店分发：支持 Mac App Store、Microsoft Store 和 Snap Store。
- 🚨 崩溃报告：通过 crashReporter 模块自动收集 JavaScript 与原生崩溃数据。
- 🧰 技术自由：可搭配 React、Vue、Next.js、Tailwind CSS、Bootstrap、Three.js、Angular、TypeScript、webpack、Playwright、Testing Library、Sass 等。
- 🚀 Electron Forge：开箱即用的构建与发布工具包，可用 `npm init electron-app@latest my-app` 快速开始。
- 📥 安装方式：可直接从 npm 安装 Electron，稳定版示例为 `npm install --save-dev electron@latest`；文中提及 Electron 44.4.4、Node 24.21.0、Chromium 152.0.7977.130。
- 🧪 Electron Fiddle：用于创建和试验小型 Electron 项目，可保存为 GitHub Gist 或本地文件夹。

---

### [Deno 2.9 | Deno](https://deno.com/blog/v2.9#deno-desktop)

**原文标题**: [Deno 2.9 | Deno](https://deno.com/blog/v2.9#deno-desktop)

overview summary
- 🚀 Deno 2.9 发布，核心亮点是实验性 `deno desktop`、更轻松的 Node 项目迁移，以及显著的性能与内存优化。
- 🖥️ `deno desktop`：从脚本或 Web 框架项目生成原生桌面应用，UI 跑在 webview、逻辑跑在 Deno，最终编译为单个可分发二进制。
- 🧩 支持自动检测 Next.js、Astro、Fresh、Remix、Nuxt、SvelteKit、SolidStart、TanStack Start、Vite SSR 等框架。
- 🪟 内置原生桌面 API：`Deno.BrowserWindow`、`Deno.Tray`、`Deno.Dock`、原生对话框、`Deno.autoUpdate()`，并支持 webview 与 Deno 之间绑定函数。
- 🌐 两种桌面后端：默认 `webview` 使用系统引擎，体积小启动快；`--backend cef` 内置 Chromium，跨平台渲染一致但体积更大。
- 📦 发行产物复用 `deno compile`，支持 `.app/.dmg/.exe/.msi/.AppImage/.deb/.rpm`，可通过 `--target` 和 `--all-targets` 跨平台构建。
- ⚡ 性能大幅提升：冷启动从 34.2ms 降至 17.3ms；`Deno.serve` realworld 吞吐提升 1.27x；realworld RSS 从 142MB 降至 64MB。
- 🧠 启动优化包括：懒加载 `node:` 全局、限制 Node 引导到 Node workers、V8 代码缓存、压缩快照和 macOS chained fixups。
- 🧬 HTTP 与热路径优化：新增 Deno 自有 HTTP/1.1 服务路径，`crypto.subtle`、`console`/`Deno.inspect` 部分迁移到 Rust。
- 🎨 支持 CSS 模块导入：`import sheet from "./styles.css" with { type: "css" }`，返回 `CSSStyleSheet`，需 `--unstable-raw-imports`。
- 🔄 迁移 Node 项目更顺滑：`deno install` 可直接读取 npm、pnpm、yarn、Bun 的 lockfile，并生成保留精确版本与完整性哈希的 `deno.lock`。
- 🧩 支持 npm/yarn/Bun workspaces，并可自动迁移 `pnpm-workspace.yaml` 中的 packages、catalog、catalogs。
- 🔧 当工具调用 `node` 时，Deno 可提供 PATH shim 转发到自身，并翻译 Node CLI 参数；可用 `DENO_DISABLE_NODE_SHIM=1` 禁用。
- 🔗 依赖管理增强：`deno link`/`deno unlink` 稳定 `links` 字段，`deno list` 类似 `npm ls`，`preferPackageJson` 可让依赖写入 `package.json`。
- 📚 新增 `jsrDepsInNodeModules`，可通过 npm 兼容注册表把 JSR 依赖安装进 `node_modules`；工作区成员也会生成自己的 `node_modules/.bin`。
- 🛡️ 供应链安全：`min-release-age` 默认启用 24 小时；新增 `no-downgrade` 信任策略，防止维护者令牌被盗后的降级攻击。
- 🧪 测试增强：内置 `t.assertSnapshot()`、`--changed`/`--related`、`--retry`/`--repeats`、覆盖率阈值、`--shard` 分片、`Deno.test.each` 参数化测试。
- 🧱 `deno compile`：新增 `--include-as-is` 原样嵌入资源；编译产物可持久化 OpenKv/localStorage/caches；实验性 `--bundle`/`--minify` 显著缩小二进制。
- 📄 `deno bundle`：新增 `--declaration` 生成汇总 `.d.ts`，并支持 `package.json` 中 browser 字段的对象形式。
- 🧹 `deno fmt`：非 JS 格式化改用 lax 引擎；HTML/XML/SVG 默认格式化；CSS/SCSS/Less、SQL 得到新引擎；新增导入导出排序、JSON 尾逗号、`.editorconfig` 支持。
- 🏗️ `deno task`：支持基于输入指纹的缓存与输出恢复、`--jobs` 并发控制、`--if-present`、`--env-file`、任务名排除组通配符。
- 🟢 Node.js 兼容性升级到 Node.js 26：`process.version` 报告 v26.3.0，裸 Node 内置模块无需 flag，`node:test` 增强，NAPI 版本 10。
- 🔐 Web Crypto 扩展：新增后量子 ML-KEM、ML-DSA、SLH-DSA，以及 ChaCha20-Poly1305、SHA-3/SHAKE/KMAC/Argon2；新增 `SubtleCrypto.supports()`。
- 🌐 `Deno.serve` 变更：自动压缩默认关闭，需 `automaticCompression: true` 或环境变量开启；旧 `request.signal` 中止行为弃用。
- 📡 OpenTelemetry 增强：支持采样器、span 属性/事件数量限制，自动插桩扩展到 `node:http2`。
- 🧰 其他更新：Web Locks API、`navigator.userAgentData`、Happy Eyeballs v2、`fetch` priority、`Deno.watchFs` ignore、`process.kill` 自身无需 `--allow-run`、WASM global 导出、`deno watch` 子命令。
- 🙏 感谢社区贡献者，完整 PR 列表可在 GitHub 查看；升级命令为 `deno upgrade`。

---

### [使用 JavaScript、HTML 和 CSS 构建轻量级跨平台桌面应用 | Neutralinojs](https://neutralino.js.org/)

**原文标题**: [Build lightweight cross-platform desktop apps with JavaScript, HTML, and CSS | Neutralinojs](https://neutralino.js.org/)

Neutralinojs 是一个轻量、跨平台、零依赖的 JavaScript 框架，可通过原生 API 访问操作系统功能，并兼容多种前端框架与后端语言。

- 🖥️ 原生 API：通过 JavaScript 调用文件操作、执行命令和显示原生对话框等系统级功能。
- 📦 零依赖且便携：无需额外依赖或编译器，用一个平台即可开发所有平台应用。
- 🌍 跨平台支持：可在 Linux、Windows、macOS、Web 和 Chrome 上运行，单一便携应用兼容主流操作系统与浏览器。
- ⚡ 轻量快速：未压缩应用约 2MB，压缩后约 0.5MB，不像其他 Chromium 跨平台框架那样消耗大量内存或存储。
- 🧩 简单灵活：提供简单灵活的开发接口、便携自动更新器和 CLI，避免到处使用 OOP 类和耗时配置。
- 🔄 任意前后端：可与任意前端框架搭配并支持 HMR；也可通过子进程 IPC 集成到源码中，或用扩展 IPC 以任意后端语言扩展 API。

---

### [](https://github.com/paradedb/drizzle-paradedb)

**原文标题**: [GitHub - paradedb/drizzle-paradedb: Official extension to Drizzle for use with ParadeDB · GitHub](https://github.com/paradedb/drizzle-paradedb)

这是 ParadeDB 官方为 Drizzle ORM 提供的集成仓库，基于 pg_search 扩展，目标是让开发者在单个 PostgreSQL 中同时完成应用数据存储、全文检索、向量检索和聚合分析。项目采用 MIT 许可证，当前有 32 个 Star、2 个 Fork、118 次提交、0 个 Issue 和 1 个 Pull Request。

- 🧩 官方 Drizzle 与 ParadeDB 集成，底层由 pg_search PostgreSQL 扩展驱动。
- 🐘 核心理念是“Just use Postgres”：一个 Postgres 即可支持应用数据、全文搜索、向量检索和聚合。
- ⚙️ 兼容要求：Node 22.12+、Drizzle 1.0+、ParadeDB 0.25.0+、PostgreSQL 15+（含 pg_search 扩展）。
- 🔍 向量搜索需要 pgvector，ParadeDB Docker 镜像已默认包含。
- 📊 仓库状态：118 次提交、32 Stars、2 Forks、0 Issues、1 Pull Request。
- 🗂️ 仓库包含 src、tests、scripts、.github 等目录，以及多种代码质量与配置文件。
- 🤝 贡献流程见 CONTRIBUTING.md，涵盖开发设置、测试、lint 和 PR 工作流。
- 💬 支持渠道包括 GitHub Issue、ParadeDB Slack 社区、GitHub Discussions，也可联系官方获取商业支持。
- 📜 项目使用 MIT License，README 还包含行为准则、贡献指南和安全政策等文档。
- 🏷️ 主要主题标签：drizzle、full-text-search、hybrid-search、nodejs、orm、paradedb、postgresql、typescript、vector-search。

---

### [](https://duckdb.org/2026/09/18/opfs-wasm)

**原文标题**: [Persistent Databases in the Browser with DuckDB-Wasm and OPFS – DuckDB](https://duckdb.org/2026/09/18/opfs-wasm)

DuckDB-Wasm 现在可以借助浏览器 OPFS 创建持久化数据库，使 `.duckdb` 文件在页面刷新和浏览器重启后仍可打开；文章介绍了打开数据库、使用数据文件、文件处理模式、持久性保证、导出方法及注意事项。

- 🗂️ 背景：早期 DuckDB-Wasm 数据只存在 Wasm 内存中，持久化需手动序列化到 Parquet 并存入 IndexedDB；现代浏览器 OPFS 提供按源隔离、支持随机读写的文件系统。
- 🚀 用法：通过 `opfs://analytics.duckdb` 和 `READ_WRITE` 调用 `db.open()`，之后可正常建表、插入和查询，数据会写入带 WAL 和检查点的普通 DuckDB 文件。
- ⚠️ 版本坑：npm `latest` 的 1.33.1-dev57.0 会创建 OPFS 文件但不写入，导致无法持久化；应固定 1.32.0 或使用 `next` 标签的 1.33.1-dev64.0 及更高版本。
- 📦 数据文件：远程 Parquet 可在首次加载时通过 HTTP range 请求读入 OPFS，之后从本地读取；也可用 `COPY` 将聚合结果写入 `opfs://cache/...parquet`。
- 🗃️ 文件处理：`opfs: { fileHandling: 'auto' }` 会自动注册 SQL 中的 `'opfs://...'` 字面量；手动模式则用 `registerOPFSFileName()` 和 `dropFile()`，避免每条语句重复获取 OPFS 句柄。
- 💾 持久性：写入先进入 WAL，默认在超过 16MB 阈值、手动执行 `CHECKPOINT` 或干净关闭时写入主文件；浏览器标签可能被强制终止，建议每批写入后执行 `CHECKPOINT`，或设置 `checkpoint_threshold = '0KB'`。
- 🔒 存储限制：OPFS 仍可能被浏览器在磁盘紧张或长期未访问时清除；它应被视为快速本地缓存和工作状态，真实数据应保存在 DuckLake、S3 等稳定位置。
- 📤 导出：DuckDB-Wasm 尚不能直接移动 OPFS 文件，但可用 OPFS API 读取 `.duckdb` 文件用于下载，或用 SQL `COPY ... TO 'opfs://export/...parquet'` 导出 Parquet。
- ✅ 结论：建议批量写入后检查点、提供数据库下载能力，并阅读单文件单句柄、SQL 重命名限制等文档说明；这让本地优先分析应用无需服务器、IndexedDB 封装或自定义序列化。

---

### [一个分析型 SQL 数据库管理系统——DuckDB](https://duckdb.org/)

**原文标题**: [An analytical SQL database management system – DuckDB](https://duckdb.org/)

DuckDB 是一个可随处部署的开源分析数据库，提供友好 SQL、扩展能力、多语言客户端与多格式支持，并围绕 DuckDB、Quack、DuckLake、Iceberg 构成完整数据栈。

- 🔍 支持 cmd/ctrl + k 搜索，定位为通用数据整理工具。
- 🌍 可从边缘设备部署到数百核服务器。
- 🗣️ 提供受 PostgreSQL 启发的友好、表达力强的 SQL。
- 🧩 可通过扩展增加函数和新格式支持。
- 💻 为主要编程语言提供原生、高性能 API。
- 📂 可在本地或对象存储读写 CSV、JSON、Parquet、Iceberg 等格式。
- 🆓 MIT 许可，由独立 DuckDB Foundation 治理。
- 🦆 Duck Stack 包含 DuckDB、Quack、DuckLake、Iceberg。
- ⚙️ DuckDB：可进程内运行的分析 SQL 数据库，简单、快速、可移植。
- 🔌 Quack：客户端 - 服务器协议，客户端与服务器均为完整 DuckDB 实例。
- 🏞️ DuckLake：基于 SQL 的 lakehouse 格式，数据在对象存储，SQL 数据库作目录。
- ❄️ Iceberg：Apache Iceberg 一流支持，可直接高性能读写。
- 🔗 集成 AWS、Azure、GCP、Cloudflare、Hugging Face、SQLite、MySQL、PostgreSQL、MotherDuck 等。
- 🧑‍💻 客户端覆盖 CLI、Python、Go、Java、Node.js、C/C++、R、Rust、ODBC。
- 📦 支持 pip、npm、cargo、go get、curl、CLI 等安装方式。
- 📝 博客与示例涵盖 dbt v2、Wasm/OPFS、Claude Code Skills，以及 SQL、CSV/Parquet、空间、Pandas、UDF、JDBC 和 Web 服务。

---

### [](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system)

**原文标题**: [Origin private file system - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system)

源私有文件系统（OPFS）是 File System API 提供的源私有存储端点，对用户不可见，专为高性能文件操作设计，支持字节级访问与就地写入；它仅限安全上下文（HTTPS），可在 Web Workers 中使用，受浏览器存储配额限制，清除站点数据会删除其内容。自 2023 年 3 月起已在浏览器中广泛可用。

- 🗂️ OPFS 是 File System API 的一部分，存储空间按源隔离，用户无法像普通文件系统一样看到它。
- ⚡ 提供低层级、字节级的文件访问，并支持就地写入，性能优于普通文件系统访问。
- 🔒 仅在安全上下文（HTTPS）中可用，并且可在 Web Workers 中使用。
- 🧩 File System Access API 通过选择器访问用户可见文件，需权限提示、安全检查与临时文件，因此大文件更新较慢。
- 🚀 OPFS 不需要权限提示和安全检查，适合 SQLite 数据库修改等高性能、大规模文件操作。
- 💾 OPFS 受浏览器存储配额限制，可用 `navigator.storage.estimate()` 查看使用量；清除站点数据会删除 OPFS。
- 📂 通过 `navigator.storage.getDirectory()` 获取 OPFS 根目录的 `FileSystemDirectoryHandle`。
- 🧵 主线程使用基于 Promise 的异步 API，例如 `getFileHandle()`、`getDirectoryHandle()`。
- 📖 读取文件：获取 `FileSystemFileHandle` 后调用 `getFile()`，得到可操作的 `File`/`Blob` 对象。
- ✍️ 写入文件：调用 `createWritable()` 获得 `FileSystemWritableFileStream`，再用 `write()` 写入并 `close()` 关闭。
- 🗑️ 删除条目：可使用 `removeEntry()` 或 `remove()`；删除文件夹可传入 `{ recursive: true }`，也可用根目录的 `remove({ recursive: true })` 清空 OPFS。
- 📜 遍历目录：`FileSystemDirectoryHandle` 是异步迭代器，支持 `entries()`、`values()`、`keys()` 和 `for await...of`。
- ⚙️ Web Worker 中可调用 `createSyncAccessHandle()` 获得 `FileSystemSyncAccessHandle`，避免阻塞主线程。
- 🔁 同步访问方法包括 `getSize()`、`write()`、`read()`、`truncate()`、`flush()`、`close()`，适合高性能文件读写。
- ✅ 该功能自 2023 年 3 月起跨浏览器广泛可用，但仍应关注具体浏览器兼容性。

---

### [AI 编程让 CI 成了瓶颈](https://linear.app/now/ci-bottleneck-reworked)

**原文标题**: [AI coding has made CI a bottleneck, so we reworked ours to keep up](https://linear.app/now/ci-bottleneck-reworked)

Linear 因 AI 编码代理大幅加速交付，CI 成为新瓶颈，于是围绕“缩短 PR 等待时间”和“降低 runner 时间消耗”系统性优化 CI；虽然测试套件较年初接近四倍，PR 等待从 6 分钟以上降至 5 分钟出头，单个测试的 runner 时间约减半。

- 🤖 AI 代理让写代码和发 PR 更快，但验证速度没同步跟上，CI 因此成为瓶颈，推高基础设施成本并拖慢反馈。
- 🎯 Linear 优化目标：缩短 PR 在 CI 中的等待时间，并降低 runner 时间消耗；测试套件几乎四倍增长后仍实现整体提速。
- 🏗️ 改进分为四类：升级基础设施和工具、优化门控作业、减少重复设置、提升测试执行效率。
- ⚡ 基础设施升级：从 GitHub Actions 迁到第三方 runner，同类任务平均快 34%，`tsc` 快 52%；采用 `tsgo` 后每周 `tsc` 检查中位数降 73%。
- 🧹 移除 lint 对 TypeScript 类型信息的依赖，ESLint 不再需要完整类型图，API lint 时间降 68%，全仓 lint 降 55%，内存占用也大幅下降。
- 🔄 后续迁移到 Oxlint 更容易，因为纯语法规则更易移植，并进一步减少 lint 消耗的 runner 分钟。
- 🚦 优化门控作业：change-detection 限制 fetch depth、采用稀疏/blobless checkout；中位时长从 26 秒降至 8 秒，p90 从 31 秒降至 12 秒，最慢从 138 秒降至 37 秒。
- 🛡️ 替换 `actions/checkout` 为自定义 composite action，加入重试退避、低速超时和持久 git mirror，减少网络不稳定导致的 checkout 挂起。
- ✂️ 将 cache marker 写入移出关键路径，改为测试分片完成后运行但不阻塞合并，为每个 API PR 和 merge-queue 条目节省 42 秒。
- 📦 减少重复 setup：在 CI 基础镜像中预装 Postgres client 等共享依赖，避免每个测试分片重复安装。
- 📥 按需安装依赖：在 pnpm monorepo 中只安装 API 包及其依赖，`pnpm install` 从 44-73 秒降至 16-18 秒。
- 🗑️ 发现重建比缓存更快：`node_modules` 缓存命中约需 28 秒恢复，而过滤安装约 7.5 秒，因此放弃缓存；每分片 setup 从 110-140 秒降至 67-73 秒。
- 🧩 避免重放未变更设置：数据库改用 schema 快照和 bootstrap，容器数据库设置从约 12 秒降至 1-2 秒。
- 🧱 将 7 个短检查合并为 2 个作业并并发执行，基于 6 月用量每月节省约 87,000 runner 分钟，占 CI 总量 11.8%。
- 🧪 测试执行优化：Vitest 按文件分片，拆分大测试文件；增至 8 分片后关键作业初测快约 19%、便宜约 19%，最慢分片从 5.25 分钟降至 4.33 分钟。
- 🔗 最大单项提升：启用 `isolate: false` 的 opt-in Vitest 项目，让安全文件共享模块注册表；月省约 17%，最慢分片从约 300-379 秒降至 195 秒，总 API 分片 runner 时间从 32.8 分钟降至 22 分钟。
- ⚠️ 共享模块状态也是正确性风险最高的优化，需要每个文件显式 opt-in、补充 teardown，并把不安全文件留在隔离项目中。
- 📈 分片受 setup 固定成本限制；setup 优化后 8 分片才可行，之后 8 分片总 setup 约 7.5 分钟，低于原先 4 分片的 8.3 分钟。
- 🔮 若未进行这些优化，今天测试套件大约需要 11 分钟，接近当前等待时间的两倍；每周新增约 2,000 个测试，CI 提速仍需持续进行。

---

### [Oxlint | JavaScript 氧化编译器](https://oxc.rs/docs/guide/usage/linter)

**原文标题**: [Oxlint | The JavaScript Oxidation Compiler](https://oxc.rs/docs/guide/usage/linter)

Oxlint 是构建于 Oxc 编译器栈之上的高性能 JavaScript/TypeScript linter，主打大规模仓库与 CI 场景，提供快速性能、ESLint 迁移支持、类型感知检查和多文件分析，并强调可靠性与低噪声默认规则。

- ⚡ Oxlint 是基于 Oxc 的高性能 JS/TS linter，适合作为专用 linter，尤其看重 ESLint 迁移、CI 速度与类型感知能力。
- 🧰 若想要统一工具链（包含 Oxlint 与 Oxfmt），选择 Vite+；仅当依赖 ESLint 尚未支持的边缘插件行为时，才继续只用 ESLint。
- 🚀 面向大型仓库和 CI，架构消除 ESLint 的性能瓶颈，基准显示比 ESLint 快 50–100 倍。
- ✅ 默认聚焦高信号正确性检查，能发现错误、不安全或无用代码，减少噪音；规则可按需逐步启用。
- 📚 规则集超过 865 条，覆盖 ESLint 核心、TypeScript（含类型感知）、React、Jest、Vitest、Import、Unicorn、jsx-a11y 等，并支持兼容 ESLint 的自定义 JS 插件。
- 🔄 提供工具自动迁移整个 linter 配置，降低从 ESLint 迁移成本。
- 🧠 类型感知 linting 基于 TypeScript 编译器的原生 Go 版本 tsgo（TypeScript 7），保持完整 TS 兼容性与类型系统行为，可检测 floating promises 等关键问题；Biome 则自建类型推断，覆盖仍在完善。
- 🕸️ 支持一等公民的多文件分析，构建项目级模块图并跨规则共享解析与解析结果，改善跨文件 import 检查，并缓解 import/no-cycle 等规则的性能悬崖。
- 🤖 诊断信息同时面向人类和 AI：清晰消息外，还包含精确位置、上下文数据与文档链接，便于理解与自动修复。
- 🛡️ 将崩溃视为最高优先级 bug，性能回退也视为 bug，优先保障稳定性与吞吐量，尤其适合 CI 和大型 monorepo。
- 🛠️ 推荐安装为 dev dependency：pnpm add -D oxlint，并添加 "lint": "oxlint" 与 "lint:fix": "oxlint --fix" 脚本；后续可看 Quickstart、Configuration、编辑器与 CI 设置。
- 🧭 迁移路径：多数项目可直接替换 ESLint，并用 @oxlint/migrate 迁移配置；大型复杂仓库可增量迁移，先跑 Oxlint，再以 eslint-plugin-oxlint 禁用重叠规则运行 ESLint。
- 📂 支持 .js/.mjs/.cjs/.ts/.mts/.cts、.jsx/.tsx，以及 .vue/.svelte/.astro 中仅 lint `<script>` 块。
- 🧩 功能包括 870 条内置规则的原生插件、自动修复、忽略文件、行内忽略注释、多文件分析、类型感知 linting，以及 alpha 阶段的 JS 插件。
- 🏭 生产使用者包括 elastic/kibana、getsentry/sentry、electron/electron、renovatebot/renovate、preactjs/preact、date-fns/date-fns、outline/outline、PostHog/posthog、actualbudget/actual、cloudflare/agents。
- 📖 参考资源：规则参考、CLI 参考、配置文件参考、版本策略，以及“从 ESLint 迁移”指南。

---

### [更快的预览，](https://lovable.dev/blog/faster-previews-oj)

**原文标题**: [Faster previews, soon powered by OJ | Lovable](https://lovable.dev/blog/faster-previews-oj)

Lovable 发布 Rust 重写的预览引擎 OJ（Orange Juice），旨在替代 Vite 以支撑每天约百万级沙盒，带来更快冷启动、更低内存，同时保持现有配置与插件兼容。OJ 已开始逐步上线生产预览，并迁移至 Lovable GitHub 开源。

- ⚡ Lovable 预览是带热重载的真实开发服务器；Vite 适合单开发者，但在百万级沙盒下资源占用重，导致冷启动慢、内存高。
- 🥤 OJ 是单个 Rust 二进制，读取现有 `vite.config.ts` 或 `oj.config.ts`，通过兼容桥运行真实 Vite 插件，并原生实现 React Fast Refresh、TanStack Start 等。
- 🧱 OJ 基于 Rolldown 和 Oxc，从文件监听到 WebSocket 均为 Rust 端到端；仅当插件或服务端代码需要 JavaScript 时，才启动小型 Node sidecar。
- 🎯 设计重点：兼容优先、无需 JS 运行时驱动、不向项目安装工具链，并针对 agent 连续编辑合并更新，避免预览显示半成品状态。
- 📊 基准：1 万组件冷启动 1.2s vs Vite 4.9s，内存约 115MB vs >1.5GB；Excalidraw、Twenty 等真实开源应用可不改配置运行。
- 🧠 内存最关键：OJ 使用 Vite 约 1/3 到 1/8 的内存；但 Vite 冷启动包含 OJ 尚未支持的 `vite-plugin-checker`，速度对比并非完全对等。
- 🏭 生产实验：预览可用中位时间从 17.4s 降至 8.0s，沙盒获取从 14.5s 降至 3.0s，P90 开发服务器从 15.8s 降至 9.6s，开发服务器内存约少 6.5 倍。
- 🛠️ 对构建者：无需改变构建方式；OJ 会小比例逐步铺开，已有插件与配置继续工作，异常行为应作为 bug 反馈。
- 🌍 OJ 已从个人仓库迁移至 Lovable GitHub 组织：`github.com/lovablelabs/oj`，开放阅读、运行与贡献，更多实验功能即将公布。
- 👤 作者 Raphael Amorim 是 Lovable 工程师、OJ 创造者，专注 Rust 开发工具，曾参与 Rio 终端、Jam 语言等项目。

---

### [](https://rapha.land/introducing-oj/)

**原文标题**: [Introducing oj: your Rust native replacement for Vite — Raphael Amorim](https://rapha.land/introducing-oj/)

overview summary
- 🦀 oj 是 Rust 编写的 Vite 原生替代 dev server/打包器，可直接指向现有 Vite + React 项目，读取同一 `vite.config.ts` 并运行同一批插件，无需重写。
- 🧪 目前是实验性项目：已能不改代码运行大型生产应用，但尚未完成，Svelte 支持仍在开发，可能还有未知缺口。
- 🧩 兼容目标是“说 Vite，而不是 webpack”：通过兼容桥运行真实 Vite 插件，并原生重实现 React Fast Refresh 与 TanStack Start。
- 📦 部署目标是无需 Node、无需 `node_modules`，只交付一个约 28MB 的 Rust 二进制，适合临时沙盒、快速冷启动和轻量镜像。
- 📉 沙盒成本：Node dev server 约 295MB、冷启动约 18s；oj 单二进制冷启动 <1s；500 个沙盒约 144GB vs 14GB 磁盘。
- 🏗️ 底层基于 `rolldown` 和 `oxc`，提供按需、非打包 dev server，并用懒编译避免一次加载整个应用。
- 📊 10,000 组件基准：oj `dev --bundle` vs Vite 8.2.1 默认 dev，冷启动 1211ms vs 4917ms（4.1×），热启动 1067ms vs 4516ms，重载 223ms vs 1474ms。
- 🧠 同基准内存：oj 约 115MB，Vite 超过 1.5GB；作者称曾把 12GB 的 Vite 应用降到 1.8GB。
- ⚖️ 作者强调对比的是合理配置的 Vite，不是稻草人；基准可用 `node bench/run.mjs 10000` 复现。
- 🖼️ 真实应用 Excalidraw：不改配置即可运行；oj 冷/热启动约 0.8s、内存 288MB；Vite 冷启动约 2.3s、热启动约 1.1s、内存 2.4GB。
- ⚠️ oj 会跳过 `vite-plugin-checker`，因此没有浏览器内 TypeScript 类型错误覆盖层；应用本身服务不受影响。
- 🏢 更大真实应用 Twenty（约 15,000 模块）：oj 冷启动约 10.2s、热启动约 9.2s、内存 1.5GB；Vite 约 11.3s、10.2s、4.9GB，即使 oj 未预打包依赖也领先。
- 🌐 实验性部分打包：把依赖文件合并请求，干净 React 应用从 962 个依赖请求降到 18 个；50ms RTT 下首屏渲染从 8.8s 降到 0.33s（27×）。
- 🚀 项目起源于作者被 `vite build` 反复运行、代理/多 worktree 导致高内存和 swap 的痛苦；后来在 Lovable 的生产 TanStack Start 应用中经受压力测试。
- 💾 未来重点是实验性持久缓存：按源码哈希编译并落盘，热启动直接复用；默认关闭，可用 `oj dev --enable-cache` 或 `OJ_ENABLE_CACHE=1` 开启。
- 🧷 缓存正确性难点：某些插件把状态存内存并生成虚拟文件（如 `wyw-in-js` 的 CSS）；oj 只对导入不存在虚拟路径的缓存模块重新 transform，其余从缓存服务，但仍需更多测试。
- 🛠️ 已开源、MIT 许可、发布在 crates.io：`cargo install oj --locked`，进入 Vite 项目后运行 `oj dev`。
- 📣 作者承诺：如果不能不改配置运行你的应用，就是 bug；可开 issue 并附上 `vite.config.ts`。

---

### [](https://socket.dev/blog/oj-vite-rust)

**原文标题**: [Lovable’s OJ Rewrites Vite’s Dev Server in Rust as AI Lowers the Cost of Forking Open Source | Socket](https://socket.dev/blog/oj-vite-rust)

Lovable 将 Vite 开发服务器层用 Rust 重写为 OJ，在生产云预览环境中大幅降低沙箱获取时间与内存占用；这反映了 AI 降低开源软件重实现成本后，企业专用“slop fork”可能增多的趋势。

- 🚀 Lovable 用 Rust 构建 OJ，在云预览环境中替代 Vite，面向每天约 100 万个短生命周期开发沙箱。
- ⏱️ 生产部署显示，沙箱获取中位时间从 14.5 秒降至 3 秒，开发服务器进程内存约减少 6.5 倍。
- 🧩 OJ 并非完整重写 Vite：打包仍用 Rolldown，解析与转换用 Oxc；重写的是文件监视、模块图、编译协调、热更新和 WebSocket 处理。
- 🔌 OJ 可读取现有 vite.config.ts，并通过兼容桥运行 Vite/Rollup 插件；需要 JS 插件或服务端模块时启动小型 Node 进程。
- 📊 在 10,000 个 React 组件基准中，OJ 冷启动约 1.2 秒，Vite 默认非打包模式约 4.9 秒；打包模式下冷启动接近，但内存仍为 115MB 对 1,751MB。
- ⚠️ Evan You 认为早期基准“有些误导”，因为 Vite 有自带打包开发模式；Lovable 也承认 Vite 侧启用了 vite-plugin-checker，而 OJ 跳过该工作。
- 🧠 内存比 CPU 更难共享且更昂贵，因此 OJ 继续压低开发服务器空闲内存，以便每台主机容纳更多沙箱。
- 🧪 OJ 的窄目标不限于简单应用：Excalidraw 和 Twenty 可无需修改运行，Twenty 前端约含 15,000 个模块。
- 🤖 Evan You 预计 AI 使重实现成本骤降，会出现更多针对特定场景的“定制投影”，甚至每个公司维护自己的“slop fork”。
- 🍴 类似 TanStack Redact、Rspack，OJ 保留熟悉 API 但替换底层实现；好处是可针对自身负载优化，代价是碎片化、上游修复与安全补丁需各自跟踪。
- 🔮 若趋势延续，更多工程工作可能转移到下游实现，即使原始项目 API 仍具影响力；OJ 是这一趋势在 Vite 生态中的体现。

---

### [](https://www.npmchart.com/)

**原文标题**: [npmchart](https://www.npmchart.com/)

npmchart 是一个用于查看任意 npm 包下载趋势、版本发布与仓库活动的工具，支持多包对比，并展示精选包和常见对比示例。

- 📊 核心功能：查看任意 npm 包的下载趋势、版本发布和仓库活跃度。
- 🔍 支持同时对比多个 npm 包。
- ⭐ 精选包：layerchart v2.5.0，用于构建多种可视化的 Svelte 可组合图表组件。
- ⚡ 精选包：svelte v5.57.1，增强型 Web 应用框架。
- 🧰 精选包：@sveltejs/kit v2.70.3，快速构建 Svelte 应用的方式。
- 🛠️ 精选包：vite v8.3.0，基于原生 ESM 的 Web 开发构建工具。
- 📈 示例对比：数据可视化（Svelte），包括 layerchart、layercake、@unovis/svelte、svelteplot、@sveltejs/pancake。
- 🧩 示例对比：前端框架，包括 react、svelte、vue、@angular/core。
- 🏗️ 示例对比：构建工具，包括 vite、webpack、rollup、esbuild。
- 📦 页面还包含“weekly”等周度数据展示。

---

### [](https://www.npmchart.com/p/svelte)

**原文标题**: [svelte Â· npm downloads and repository activity](https://www.npmchart.com/p/svelte)

Svelte 是一个定位为“Cybernetically enhanced web apps”的 UI 框架，当前版本为 5.57.1，采用 MIT 许可证，由 rich_harris、conduitry、svelte-admin、svelte 维护；自 2016 年以来已发布 1092 个版本。页面数据显示近期下载量为 0，最新版本发布于 5 天前，并列出 15 个直接依赖与 18 个开发依赖。

- 🧬 项目定位：Cybernetically enhanced web apps（赛博增强型 Web 应用）。
- 📦 当前最新版本为 5.57.1，约 5 天前发布；使用 MIT 许可证。
- 🏷️ 标签包括 UI、framework、templates、templating、npm、github、website。
- 👥 维护者：rich_harris、conduitry、svelte-admin、svelte。
- 📚 版本历史：共 1092 个版本/发布，自 2016-11-17 起。
- 📉 下载数据：周下载量 0（较前一周 0），近 30 天 0；2026-06-25 至 2026-09-22 区间总下载量 0。
- 🕒 近期版本：5.57.0（4 周前）、5.56.10 与 5.56.9（上个月）、5.56.8/5.56.7/5.56.6/5.56.5（2 个月前）。
- 🧩 依赖规模：15 个直接依赖，18 个开发依赖。
- 🔧 直接依赖包括：@jridgewell/remapping、@jridgewell/sourcemap-codec、@sveltejs/acorn-typescript、@types/estree、acorn、aria-query、axobject-query、clsx、devalue、esm-env、esrap、is-reference、locate-character、magic-string、zimmerframe。
- 📊 其他数据：Stars、Last commit、Open issues 显示为“—”；Commits、Issues、Pull requests 无数据。

---

### [](https://github.blog/changelog/2026-09-18-stage-only-npm-tokens-for-safer-automation/)

**原文标题**: [Stage-only npm tokens for safer automation - GitHub Changelog](https://github.blog/changelog/2026-09-18-stage-only-npm-tokens-for-safer-automation/)

npm 推出“仅暂存”细粒度访问令牌，让自动化工作流可提交包版本供维护者用 2FA 审核发布，但不能直接发布到 npm registry；这是向 2027 年 1 月取消 bypass-2FA 直接发布过渡的迁移方案。

- 🛡️ npm 新增“仅暂存”令牌，用于更安全的自动化流程
- ⚙️ 创建细粒度访问令牌时，可选择 `Read and write (stage only)`
- 📤 工作流使用 `npm stage publish` 提交版本，维护者审核后用 2FA 批准发布
- 🚫 该令牌会拒绝直接 `npm publish`，即使配置了自动化绕过 2FA
- 🔑 仅暂存令牌仍保留其他包写权限，包括移动 dist-tags 和弃用版本，需像其他写令牌一样保护
- 🔄 此功能为选择加入，不改变现有令牌或其直接发布能力
- 📅 npm 计划 2027 年 1 月移除通过 bypass-2FA 令牌直接发布
- ✅ 若暂不能迁移到 trusted publishing，仅暂存令牌可作为迁移路径
- 📦 使用要求：对包有发布权限、npm 账户启用 2FA、npm CLI 11.15.0+、Node.js 22.14.0+
- 🔗 适用于现有 npm 包，可查阅 staged publishing 文档并在 npm 社区讨论中反馈问题或迁移阻碍

---

### [npm](https://docs.npmjs.com/trusted-publishers/)

**原文标题**: [Trusted publishing for npm packages | npm Docs](https://docs.npmjs.com/trusted-publishers/)

npm 可信发布（Trusted publishing）通过 OpenID Connect（OIDC）让 npm 包直接从 CI/CD 工作流发布，消除长期 npm token 的安全风险；它遵循 OpenSSF 可信发布者标准，要求 npm CLI 11.5.1+ 与 Node 22.14.0+，并支持 GitHub Actions、GitLab CI/CD、CircleCI 等云托管环境。

- 🔐 通过 OIDC 建立 npm 与 CI/CD 提供商的信任关系，自动检测 OIDC 环境并优先用于认证。
- 🧾 每次发布使用短期、加密签名、工作流专属的 token，无法被提取或复用。
- ☁️ 当前支持 GitHub Actions、GitLab CI/CD、CircleCI 的云托管 runner；暂不支持自托管 runner。
- ⚙️ 在 npmjs.com 包设置的“Trusted Publisher”区域配置提供商和必填字段。
- 📦 每个包最多可配置 10 个可信发布者，可从不同 CI/CD 或工作流发布。
- 🐙 GitHub Actions 需配置 `id-token: write`，并填写用户/组织、仓库、工作流文件名、可选环境与允许动作。
- 🦊 GitLab CI/CD 需配置 `id_tokens`，其中 `aud` 为 `npm:registry.npmjs.org`，并填写命名空间、项目名、CI 文件路径等。
- 🟠 CircleCI 需填写组织 ID、项目 ID、流水线定义 ID、VCS origin 等，并通过 `NPM_ID_TOKEN` 和 `circleci run oidc get` 获取 OIDC token。
- 🛡️ 建议启用可信发布后，将发布访问设置为“要求 2FA 并禁止 token”，可信发布者仍可正常使用 OIDC。
- 🧪 更高安全级别可仅允许 `npm stage publish`，使 CI 发布需维护者通过 2FA 审核批准。
- 📜 从 GitHub Actions 或 GitLab CI/CD 发布公开仓库中的公开包时，npm 默认自动生成 provenance 证明。
- 🚫 CircleCI 暂不支持 provenance；私有仓库即使发布公开包也不会生成 provenance。
- 🔒 可通过环境变量、`.npmrc` 或 `package.json` 的 `publishConfig.provenance=false` 关闭 provenance。
- 🔑 优先使用可信发布而非长期 token；安装私有依赖时仍建议使用只读细粒度 token。
- 🧰 额外安全措施包括部署环境审批、标签保护、审计可信发布配置、移除未使用发布 token。
- 🧯 若遇 ENEEDAUTH，检查工作流文件名大小写与扩展名、runner 类型、`id-token: write`、CircleCI ID，以及 `repository.url` 是否匹配。
- 🧱 限制：可信发布连接创建后不可修改，只能删除重建；OIDC 仅支持 `npm publish` 和 `npm stage publish`。
- 🔄 迁移建议：先配置并验证可信发布者，再限制 token 访问，最后撤销不再需要的自动化 token。
- 🚀 npm 计划未来支持更多 CI/CD 提供商并持续改进该功能。

---

### [Turborepo 2.11 | Turborepo](https://turborepo.dev/blog/2-11)

**原文标题**: [Turborepo 2.11 | Turborepo](https://turborepo.dev/blog/2-11)

Turborepo 2.11 于 2026 年 9 月 18 日发布，带来实验性 Rust/Python/Go 原生支持、最高 4 倍启动提速、现代包管理器兼容、生产环境裁剪，并称这是首个零已知 bug 的版本。

- 🚀 实验性原生支持 Rust、Python 和 Go：可读取 Cargo、uv、go.work 工作区，将其纳入同一个 Task Graph。
- 🧩 用一个 `turbo` CLI 统一运行 build、test、check、lint、format 等任务，并跨语言并行执行、遵守依赖关系。
- ⚙️ 支持在 `turbo.json` 中配置跨工具链依赖，例如 Python API 测试等待 Rust core 构建完成。
- ⚡ Time to First Task 比 2.9 最高快 4 倍：Vercel 后端 1037 包从 716ms 降至 394ms，前端 132 包从 361ms 降至 206ms，create-turbo 从 132ms 降至 34ms。
- 📦 支持 `devEngines.packageManager`：可用现代 Node.js 约定声明包管理器，未来主版本将弃用顶层 `packageManager`。
- 🛡️ 新增 nub 和 aube 包管理器支持：二者注重安装安全与速度，复用现有 npm、pnpm、Yarn 或 Bun lockfile，便于迁移。
- ✂️ 新增 `turbo prune --production`：可从 prune 输出中排除仅通过 `devDependencies` 可达的工作区包，优化生产镜像。
- ✅ 这是首个零已知 bug 的 Turborepo 版本；本版包含 91 项功能、109 项性能、195 项修复、40 项文档和 28 项示例更新。
- 🙌 可通过 `@turbo/codemod migrate` 升级，或用 `create-turbo` 新建仓库，支持 pnpm、yarn、npm、bun、nub、aube。

---

### [](https://eslint.org/blog/2026/09/eslint-v10.11.0-released/)

**原文标题**: [ESLint v10.11.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/09/eslint-v10.11.0-released/)

ESLint v10.11.0 是一次小版本升级，于 2026 年 9 月 18 日发布，主要带来性能优化、新功能和若干问题修复；核心 lint 结果与公共 API 保持不变，但启动和 linting 速度有所提升。

- 🚀 版本定位：ESLint v10.11.0 为 minor release，新增功能并修复上一版本中的多个 bug。
- ⚡ 启动优化：不再在加载 `eslint` 包时立即初始化 JSON Schema 校验器，减少约 45 个模块，包加载时间降低 20–25%。
- 🧠 规则执行提速：为常见节点选择器增加快速路径，并尽可能直接调用规则访问器，减少每节点包装函数开销。
- 🛠️ 问题报告开销降低：仅在必要时填充消息模板占位符，自动修复校验不再逐个 JSON 序列化，并复用 fixer 对象。
- 📄 指令处理优化：没有 `eslint-enable` 或 `eslint-disable` 注释的文件会跳过指令处理步骤。
- 🖨️ 默认格式化器优化：`stylish` 格式化器避免不必要地剥离终端控制字符，并减少每条消息的正则表达式运行。
- ✨ 新功能：`object-shorthand` 支持 `ignoreConstructors` 处理带引号属性；`no-unsafe-finally` 报告不安全的带标签 `continue`；`new-cap` 仅豁免引用全局对象的内置项。
- 🐛 Bug 修复：`prefer-object-spread` 和 `object-shorthand` 忽略或不再报告 `__proto__` 属性；类型与文档中 `TimePass.parse` 改为可选。
- 📚 文档更新：说明 `--cache` 可能为跨文件规则提供过期结果，并澄清 `preserve-caught-error` 的已知限制。
- 🧹 维护与 CI：包含性能快速路径实现、测试兼容性更新、依赖与 GitHub Actions 升级、生态插件更新以及新增 AI 披露要求等杂项。

---

### [](https://nodejs.org/en/blog/release/v26.10.0)

**原文标题**: [Node.js — Node.js 26.10.0 (Current)](https://nodejs.org/en/blog/release/v26.10.0)

Node.js 26.10.0（Current）于 2026-09-22 发布，由 Antoine du Hamel（@aduh95）维护，包含多项 SEMVER-MINOR 新功能、大量错误修复与测试优化。

- 🚀 **版本发布**：Node.js 26.10.0（Current）于 2026-09-22 发布，发布署名 @aduh95
- 🔐 **crypto 新增功能**：新增 `crypto.parsePKCS12()`，并为 Web Cryptography 加入混合 KEM 支持
- 📁 **ffi 新特性**：支持从挂载的虚拟文件系统（VFS）加载库
- 📄 **fs 新 API**：新增 `fs.openAsBlobSync`，并改进 `FileHandle.read`、`cpSync`、`rmSync` 等行为
- 🌐 **net 增强**：支持将 `net.BoundSocket` 发送到线程和子进程
- 📊 **性能钩子**：实现 `SlidingWindowHistogram` 与 Histogram 的 QRDE 分析支持
- 🗄️ **SQLite 更新**：`undefined` 现绑定为 NULL，并修复 URL 路径、用户自定义函数跟踪等问题
- 🛠️ **工具函数**：新增 `util.markPromiseAsHandled`、`util.throttle` 和 `util.debounce`
- 🔄 **流与网络修复**：修复 stream、HTTP/2、QUIC、TLS 等模块的多项稳定性与内存问题
- 🧪 **测试改进**：扩展直方图测试覆盖，优化大量测试性能并减少 flaky 情况
- 📦 **多平台下载**：提供 Windows（x64/ARM64）、macOS（Intel/Apple Silicon）、Linux（x64/PPC64LE/s390x/ARM64）、AIX 等安装包与二进制文件
- 🔑 **完整性校验**：发布 SHA256 校验和与 PGP 签名，确保下载安全
- ➡️ **下一版本**：Node.js 26.9.0（Current）

---

### [](https://github.com/nodejs/node/pull/65899)

**原文标题**: [util: implement debounce by jasnell · Pull Request #65899 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65899)

overview summary
Node.js PR #65899 由 jasnell 发起，最终为内置 util 模块加入 util.debounce 与 util.throttle，作为 semver-minor 新功能随 Node.js 26.10.0 发布，以减少对常用 npm 依赖的需求。
- 🧩 PR #65899 标题为“util: implement debounce”，目标合并到 nodejs/node:main。
- 🎯 作者 jasnell 在测试 QUIC、DTLS、perf_hooks 等新功能时频繁使用 debounce，因而希望它直接内置。
- ⏱️ 示例：util.debounce(fn, 1000) 会启动计时器；若触发前再次调用，计时器重置，1 秒后执行内部函数。
- 💬 ljharb 询问 AbortSignal-aware debounce 的 userland 先例；jasnell 引用 Deno std 与 p-debounce。
- ⚠️ bakkot 认为 AbortSignal 用法不太对：它只能从“未中止”变为“已中止”一次，而 debounce 会被多次调用；若接收 signal，应取消所有未来调用。jasnell 同意并更新实现。
- ➕ bakkot 建议加入 immediate/leading 选项；jasnell 随后添加 leading 选项。
- 🔁 bricss 建议同时提供 throttle；jasnell 加入 util.throttle，返回限制 fn 并发调用次数的函数。
- 📊 Codecov 报告补丁覆盖率约 95.51%，项目覆盖率 90.23%，缺失覆盖主要在 lib/internal/util/throttle.js 与 debounce.js。
- ✅ mcollina 批准变更并表示“几乎每个应用都会用到”；ljharb 的审查状态为等待中。
- 🧪 后续 PR #66034 修复 util.throttle 测试不稳定问题，使用模拟计时器并覆盖准时与延迟派发。
- 🚀 该功能带有 semver-minor 与 util 标签，并被列入 Node.js 26.10.0 (Current) 的 notable changes。
- 📦 相关提交最终落地在 312db1e...c081d10，PR 已关闭/合并。

---

### [获取失败](https://netil.medium.com/billboard-js-4-1-0-live-resizing-configurable-subchart-react-subpath-csp-safe-worker-e1a6fd0ece88)

**原文标题**: [Failed to retrieve](https://netil.medium.com/billboard-js-4-1-0-live-resizing-configurable-subchart-react-subpath-csp-safe-worker-e1a6fd0ece88)

无法总结：获取内容失败，状态码 403。

---

### [](https://github.com/quickjs-ng/quickjs/releases/tag/v0.17.0)

**原文标题**: [Release v0.17.0 · quickjs-ng/quickjs · GitHub](https://github.com/quickjs-ng/quickjs/releases/tag/v0.17.0)

quickjs-ng/quickjs 发布 v0.17.0 最新版本，由 saghul 于 9 月 18 日发布，主要带来大量错误修复、规范兼容改进、性能优化和文档更新；仓库现有约 3.8k Star、374 Fork、73 Issue、46 PR，社区反应积极。

- 📦 发布 v0.17.0：最新标签，提交 6d46d07，完整变更范围 v0.16.2...v0.17.0。
- ⭐ 仓库热度：约 3.8k Star、374 Fork、73 Issue、46 PR，并设有 Discussions、Actions 和安全质量入口。
- 📚 文档更新：项目列表新增 scriptc、Qbs、Vayu、react-native-quickjs 等。
- 🧭 架构支持：加入大端架构支持说明。
- 🏗️ 构建改进：支持条件 BUILD_DIR；Alpine GHA 改用镜像；Unix 上无条件链接 libm。
- 🐛 崩溃与内存修复：修复 segfault、String.prototype.normalize() 崩溃、JS_NewTypedArray 越界读、JS_FreeCStringUTF16 切片字符串问题。
- 🔁 Promise 修复：修复 Promise.withResolvers 的引用计数 bug。
- 🧪 测试兼容：启用 test262 host-gc-required 特性。
- 🧩 语言/运行时修复：修复 Iterator.from 的 GetIteratorDirect 处理；with 访问时检查属性删除。
- 🧰 API 与类型调整：将 JSClass 移出 quickjs.h；修正 int/int32_t 指针类型不匹配；增加私有符号。
- ⚡ 性能优化：优化 JS_DeleteGlobalVar，修复二次幂整数哈希碰撞，增大初始 atom 哈希表。
- 🗜️ 序列化优化：wire format 中更紧凑地存储常量 atoms。
- 🛡️ 规范兼容：DOMException 更符合规范；BigIntArray 转 Int8Array 时抛错。
- 🧵 TypedArray/ArrayBuffer 修复：防止可调整 ArrayBuffer 的 TypedArray 被 preventExtensions；修复 TypedArray.prototype.at() 处理调整后的 ArrayBuffer。
- 🖥️ WASI 修复：修正 JS_SetMemoryLimit 字节计算；启用可配置栈溢出保护。
- 🪄 编译优化：窥孔优化“取反 + 条件跳转”。
- 👥 社区贡献：7 位新贡献者，总贡献者 10+；发布资产 23 个，获 👍2、🎉5、❤️2、🚀1，共 7 人反应。

---

### [发布 v15.0.0 · vueuse/vueuse · GitHub](https://github.com/vueuse/vueuse/releases/tag/v15.0.0)

**原文标题**: [Release v15.0.0 · vueuse/vueuse · GitHub](https://github.com/vueuse/vueuse/releases/tag/v15.0.0)

VueUse v15.0.0 已发布为最新版本，于 9 月 16 日合并到 main，带来多项破坏性变更、新功能、错误修复与性能优化；仓库 vueuse/vueuse 约有 22.4k stars 和 2.9k forks。

- 🚨 破坏性变更：移除 templateRef，停止支持 Node.js 20，core 移除废弃的 timer 选项并改用 scheduler。
- 🔄 行为调整：useEventSource 处理 SSE message 并同时触发 onmessage 和 addEventListener；useIDBKeyval 支持跨标签页同步；useThrottleFn 默认 trailing 从 false 改为 true。
- 🆕 新功能：core 新增 useWebMCP，并新增 useLiveAnnouncer、useTemporalNow。
- 🐞 错误修复：修正 tree-shaking 注解；对齐 drauu peer 范围；onLongPress 在 pointercancel 时清除待处理长按。
- 🛠️ 更多修复：useBluetooth 去重断开监听并在挂载时重连；useCloned 自定义克隆函数类型安全；useFetch 忽略较新请求后的过期成功响应。
- 🧭 继续修复：usePointer 在 pointercancel 时重置 isInside；useResizeObserver 用 instanceof Element 防止 Comment 节点崩溃；useWebSocket 忽略被取代 socket 的消息。
- ⚡ 性能优化：DisabledFunctions 改用 Set。
- 👥 贡献与反馈：JonathanSchndr、Slessi 及另外 15 位贡献者参与；20 人做出反应，包括 👍10、❤️9、🚀10、👀3。

---

### [](https://www.wired.com/story/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/)

**原文标题**: [An Undercover Google Analyst Infiltrated a Notorious Supply-Chain Hacking Gang | WIRED](https://www.wired.com/story/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/)

概述：WIRED 报道称，Google 威胁情报团队/Mandiant 曾派卧底分析师潜入臭名昭著的供应链黑客团伙 TeamPCP 内部。在该团伙制造史上最严重软件供应链攻击期间，Google 从内部监控行动、预警受害者、协助破坏攻击，并提供线索帮助执法机构逮捕两名澳大利亚嫌疑人。

- 🕵️ Google/Mandiant 的卧底人员几乎从 TeamPCP 开始活跃时就打入其约 12 人核心聊天群 CanisterWorm。
- 💥 TeamPCP 发动史上罕见的大规模供应链攻击，污染数百个开源程序、窃取开发者账号，并释放《沙丘》主题自传播蠕虫 Mini Shai-Hulud。
- 🎯 受害目标包括 Trivy、LiteLLM、Checkmarx、TanStack、Mistral AI，以及 GitHub、Mercor、OpenAI、欧盟委员会等，最终逾千家公司被入侵。
- 🗄️ 卧底获得 TeamPCP 存放受害者凭据和访问令牌的服务器访问权，使 Google 能掌握其勒索计划。
- 🚨 Google 联系 AWS、微软等可撤销凭据的平台，并向数百家受害公司发出警告，抢在黑客利用前阻断。
- 🤖 Google 还发现团伙内有人用 AI 开发登录软件零日漏洞，以绕过双因素认证；Google 取得代码测试后通知厂商完成修补。
- 💔 合作团伙 ShinyHunters 后来背叛 TeamPCP，用其窃取凭据自行勒索却不分成，还把完整聊天日志主动发给 Google 的 Austin Larsen。
- 🧹 TeamPCP 因此缩小核心圈、迁移服务器，并踢出 ShinyHunters 及包括 Google 卧底在内的成员。
- 🔍 Larsen 仍通过 BreachForums 数据泄露、Gmail 地址、PayPal 争议等线索锁定嫌疑人，并发现被盗数据被备份到关联的 Google Drive。
- 👮 Google 将线索交给 FBI；美国完成法律程序后，澳大利亚警方逮捕 Ruben Ian Thomson 和 Louis Michael Gaebler，指控其参与黑客犯罪并称其为 TeamPCP“主要参与者”。
- 🛡️ Google 强调卧底只观察、不参与非法黑客或鼓励攻击；该行动体现新设 Cyber Disruption Unit 更主动打击网络犯罪的新策略。
- 🗣️ 研究员 Austin Larsen 在 SentinelOne LABScon 大会披露此案，称写报告作用有限，采取行动保护用户才是下一步。

---

### [](https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global)

**原文标题**: [Two WA men charged following AFP-FBI-WAPF disruption of alleged global cybercrime syndicate | Australian Federal Police](https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global)

澳大利亚联邦警察（AFP）、美国联邦调查局（FBI）与西澳警察（WAPF）联合行动，disruption 一个涉嫌通过恶意开源软件实施全球网络犯罪的团伙；两名西澳男子被捕并合计被控 14 项罪名，案件估计影响逾 1000 家组织、盗取超 50 万凭证和至少 300GB 数据，全球修复成本达数亿美元，调查仍在继续。

- 🚨 2026 年 8 月 27 日，AFP、FBI 与 WAPF 发布联合媒体声明，宣布捣毁一个全球网络犯罪团伙。
- 👥 两名西澳男子被捕：一名 21 岁来自 Cottesloe，一名 23 岁来自 Mandurah；两人于 8 月 27 日在珀斯地方法院出庭。
- ⚖️ 两人合计被控 14 项罪名，涉及未经授权修改数据、持有/提供数据意图实施计算机犯罪、处理犯罪收益、未遵守 3LA 命令等。
- 🧑‍💻 警方指称他们属于高度组织化团伙，参与数据入侵、身份犯罪和加密货币洗钱。
- 🧬 该团伙涉嫌在开源代码库中植入恶意代码，使被感染的软件被政府、学术界和私营部门等组织使用。
- 🌍 估计超过 1000 家全球组织受影响，逾 50 万凭证被盗，至少 300GB 数据被窃取。
- 💰 全球修复成本估计达数亿美元。
- 🔎 平行调查始于 2026 年 4 月，线索来自多家网络威胁评估公司；警方在 Cottesloe、Hamilton Hill 和 Mandurah 执行搜查并缴获电子设备。
- 🪙 警方指称两人为主要参与者，并通过加密货币获得报酬，金额仍在调查。
- 🕵️ FBI 称涉案人员据称属于网络犯罪组织 TeamPCP，并称案件涉及软件供应链攻击。
- 📣 调查仍在进行，不排除进一步逮捕和指控；警方呼吁网络犯罪受害者通过 Report Cyber 等渠道报告。

---

### [获取失败](https://soatok.blog/2026/09/12/the-v8-javascript-runtime-undermined-my-constant-time-javascript-library/)

**原文标题**: [Failed to retrieve](https://soatok.blog/2026/09/12/the-v8-javascript-runtime-undermined-my-constant-time-javascript-library/)

无法总结：获取内容失败，状态码 429。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Data 提供基于 Postgres 的 Tiger Cloud，面向任意规模时序工作负载；单服务可达每日 3 万亿指标、3 PB 数据、1 千万亿数据点，并被数千家 IoT 企业信赖，注册可获 $1000 信用。

- 🚀 快速开始：注册即获 $1000 信用额，30 天有效，无需信用卡，仅限新账户。
- 📈 极端规模：单个 Tiger Cloud 服务支持每天 3 万亿指标、3 PB 数据和 1 千万亿数据点。
- 🏭 行业信任：数千家 IoT 公司信赖并采用。
- ⚖️ 弹性扩展：通过最多 10 节点副本集分离读写，结合 SSD/S3 分层存储，实现低成本、近乎无限存储。
- 💰 不为闲置付费：计算与存储分离，可独立扩展，降低成本并优化性能。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级合规：支持 SOC 2、HIPAA、GDPR，始终加密，SSO、RBAC 和审计日志。
- 🔍 深度可观测性：查询下钻与仪表板，监控性能与错误，指标可发送至 CloudWatch、Datadog、Prometheus。
- ⚡ 快速部署：几分钟内预置数据库，可用 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 集成生态：兼容首选云厂商和更广泛的 Postgres 生态。
- 🏢 企业支持：合同化正常运行时间 SLA、区域数据隔离、合规认证，以及 24/7 全球 Postgres 专家支持。
- ⚖️ 法律与版权：包含隐私偏好、法律、隐私、站点地图；2026 Timescale, Inc. d/b/a Tiger Data 版权所有。

---

### [框架还重要吗？](https://brookslybrand.com/posts/do-frameworks-matter-anymore/)

**原文标题**: [Do Frameworks Matter Anymore?](https://brookslybrand.com/posts/do-frameworks-matter-anymore/)

文章探讨了在 2026 年 AI 代理编程与 vibe coding 盛行的背景下，web 框架是否仍然重要。作者指出，尽管模型生成前端代码的能力大幅提升，但框架提供的抽象、结构与约束依然关键；如果不使用显式框架，LLM 也会自行构建隐式框架。文章进一步追问“新框架是否还有意义”，并主张继续构建基于 web 标准、AI 友好且人类可推理的全栈框架，因为现有方案仍有改进空间。

- 🤔 核心问题：在代理编程时代，web 框架是否还重要？
- 🏆 流行观点认为 React 已胜出，模型训练数据充足，无需尝试新框架
- 🔄 作者反驳：若框架不重要，就不必用 React；若 React 有优势，则框架重要
- 🤖 不用显式框架时，LLM 会自动生成隐式框架，只是缺乏文档与维护
- 🧱 框架价值在于提供抽象、结构与约束，帮助代理产出可靠代码
- ⚡ HMR 对调试复杂交互仍有帮助，TypeScript 类型约束利于代理迭代
- 🚫 useEffect 对代理风险较高，作者更倾向明确限制其使用
- ⚔️ 框架战争已结束，但新框架的探索仍有空间
- 🌐 作者想要全栈、基于 web 标准、AI 友好且人类可推理的框架
- 🛠️ 结论：新框架是否重要，唯有动手构建才能验证

---

### [](https://seldo.com/posts/we-are-all-product-engineers-now/)

**原文标题**: [We are all Product Engineers now | Seldo.com](https://seldo.com/posts/we-are-all-product-engineers-now/)

AI 正在把写代码的边际成本推向零，软件开发生命周期中的编码、审查、维护、部署和运维将依次被代理接管；需求没有上限，因此行业不会萎缩，但“程序员”工作会转向产品工程：理解客户、定义“好”、做出令人愉悦的产品。未来十年动荡，更多人做软件，但几乎没人只是打字。

- 💸 写代码成本已崩塌：LLM 让最昂贵的编码环节趋近免费，整个行业围绕昂贵程序员的旧结构正在改变。
- 🤖 两大假设：代理将吃掉整个软件开发生命周期；软件需求实际上无限，当前初级岗位过剩只是过渡状态。
- 🧩 成本拆解：编码已崩塌；代码审查和维护即将自动化；部署与扩展是下一步；决定做什么、定义“好”、令人愉悦可能最安全。
- 📉 初级开发者受重创：AI 暴露职业中 22-25 岁就业比同龄低 19%，大厂入门招聘自 2019 年降 65%，但工程师占招聘比例反升。
- 🐞 代理进步快：修真实 bug 基准从约 50% 到约 95%，Claude Code 的 PR 84% 被合并，Big Sleep 发现 SQLite 漏洞。
- ⚠️ 审查危机：GitHub 提交和 PR 暴增，多数 PR 无审查，代理 PR 常由另一个代理审查；AI 垃圾提交导致 curl 关闭漏洞赏金。
- 🚀 运维与扩展：数据少但逻辑上将是下一波自动化，代理在更像操作系统的基准上仍低于 65%。
- 🍞 产品发现不可自动化：每个软件都是人的欲望的形式化，需求因客户而异，必须从客户脑中挖掘，无法机械训练。
- 🎨 设计/品味仍关键：当大家都能构建正确功能时，令人愉悦的设计成为竞争点；它按产品计价、不可转移。
- 🧑💼 新工作是产品工程师：历史上有系统分析师/产品经理；现在以 forward deployed engineer、解决方案工程师等名义招聘，平均总包约 24 万美元，高级超 60 万。
- 🏭 这不再是传统编程：代码写作只是最小部分，公司付钱买能深入客户业务、定义“好”并交付的人。
- 🎓 人才管道缺失：APM 等项目每年仅培训几十到几百人，大学/训练营不教需求分析与品味；市场会解决但太慢，会伤害一批人。
- 🪵 手艺损失真实：许多热爱编码的人将被迫转向产品工作；手艺像木工一样成为爱好，但不再是主要职业。
- 🔮 十年展望：动荡先来，之后行业更大、薪酬相当、形态接近产品工程；更多软件、更多制作者、几乎无人只是打字。

---

### [AI 是否正在改变 JavaScript 本身的设计方式？ - YouTube](https://www.youtube.com/watch?v=_iVDudRDS-4)

**原文标题**: [Is AI changing how JavaScript itself gets designed? - YouTube](https://www.youtube.com/watch?v=_iVDudRDS-4)

这是 YouTube 页面底部的常见导航与版权信息，涵盖平台介绍、政策条款、功能说明及 Google 版权归属。

- ℹ️ 关于：平台介绍信息
- 📰 新闻：媒体与新闻相关入口
- ©️ 版权：版权说明
- 📞 联系我们：联系方式
- 🎬 创作者：创作者相关资源
- 📣 广告：广告投放信息
- 👨‍💻 开发者：开发者资源
- 📜 条款：服务条款
- 🔒 隐私：隐私政策
- 🛡️ 政策与安全：平台政策及安全说明
- ⚙️ YouTube 运作方式：平台机制介绍
- 🧪 测试新功能：试用新功能入口
- © 2026 Google LLC：版权归 Google 所有

---

### [](https://www.brenelz.com/posts/solidjs-its-the-little-things/)

**原文标题**: [SolidJS, It’s the Little Things](https://www.brenelz.com/posts/solidjs-its-the-little-things/)

Solid 2.0 通过一系列细微但实用的改进提升开发体验：数据可直接查询是否 pending，乐观更新更少样板代码，派生状态可本地覆盖，计算位置可按值配置，服务端读取保持函数调用体验，运行时还能解释问题所在。单独看都是小细节，合起来让框架更自然、可预测、易于修复错误。

- ⏳ `isPending` 可直接询问响应式数据或表达式是否处于异步等待中，如 `isPending(user)` 或 `isPending(() => user().name)`；React 的 `useTransition` 只能笼统表示 transition pending。
- 🔄 乐观更新更省接线：`createOptimisticStore` 从 API 调用派生服务器真值，`action` 配合 generator 在本地 `push` 乐观变更，完成后 `refresh(messages)` 移除乐观层；React 的 `useOptimistic` 需手动连接获取与刷新，await 后还要再包 `startTransition`。
- 🧬 可写派生状态：`createSignal(() => props.name)` 能本地覆盖 prop，并在 prop 更新时自动重置；React 需用 previous prop 守卫在渲染中 setState 来同步重置。
- 🌐 可按响应源选择计算位置：`ssrSource: "client"` 让 `localStorage` 等仅浏览器可用的值在 hydration 后计算，服务端先渲染 `Loading` fallback；React 的 `use(browser())` 作用于调用组件，通常需拆分组件并包 `Suspense`。
- 📡 服务端读取也像函数调用：用 `GET` 包装 `"use server"` 函数，客户端 `await getMessages()`，端点、序列化、响应解码和类型都由 Solid 处理，GET 反映读取操作；React Server Functions 主要面向 mutation，Next.js 读取常用 RSC 或 API routes。
- 🧭 运行时更会解释自己：开发时会报 `STRICT_READ_UNTRACKED`，提醒顶层读取响应值不会更新，应移入 JSX tracking scope；可选归因引擎可追踪重跑原因、过度订阅、异步瀑布和自反馈 effect。
- ✅ 结论：这些“小东西”共同让 Solid 2.0 显得深思熟虑——数据可查询 pending，乐观层可叠加于服务器真值，计算位置可声明，出错时也有清晰的修复路径。

---

### [未找到标题](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)

**原文标题**: [No title found](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)

未收到可总结的正文内容，因此暂时无法提炼文章要点。请补充需要总结的文本，我会立即生成中文概览与要点列表。

- 📄 当前没有提供文章正文
- ✍️ 请粘贴或发送需要总结的内容
- 🧾 收到后将提取关键信息并整理为简洁要点

---

### [Notion 如何使用 CRDT 处理并发编辑](https://www.notion.com/blog/how-notion-handles-concurrent-editing-with-crdts)

**原文标题**: [How Notion handles concurrent editing with CRDTs](https://www.notion.com/blog/how-notion-handles-concurrent-editing-with-crdts)

Notion 在 2025 年前主要依赖基于块的文档模型和“最后写入获胜”机制，同一块并发编辑会丢失内容，离线模式还会放大风险。为此，Notion 用 CRDT 重新设计富文本编辑与数据模型，支持并发编辑、拆分、合并与富文本注释，并于 2025 年 7 月上线，成为全球最大规模 CRDT 部署之一。

- 🧩 旧系统问题：块作为独立记录可并行编辑，但同一块冲突时 LWW 会覆盖他人修改，协作者越多、离线编辑越多，丢数据风险越高。
- 🔄 解决思路：采用 CRDT，让多个客户端保留本地副本并确定性合并并发修改，尽量在不丢失更改的前提下保留用户意图。
- 🌳 核心结构：基于 RGA 的序列 CRDT，把插入字符表示为带唯一稳定 ID 的节点；ID 由会话 ID 和 Lamport 时钟组成，并引用 origin。
- 🪦 删除处理：删除不会真正移除字符，而是标记为 tombstone，以便在途或离线操作仍能定位和合并。
- ⏱️ 排序规则：指向同一 origin 的节点按 Lamport 时钟新者优先，会话 ID 作平局决胜；连续字符可合并为 run 以节省存储。
- 🎨 富文本支持：借鉴 Peritext，用 start/end 锚点存储加粗、斜体、链接等注释，区分可扩展与不可扩展注释，并支持重叠注释。
- ✂️ 并发拆分：引入 text slice、text slice tree、text instance，处理拆分块时文本跨块移动的问题；用 text instance ↔ block 映射定位目标切片。
- 🏷️ 搜索标签：切片拆分时追加 L/R 标签，操作携带标签并用前缀匹配限制需读取的块，避免多次拆分后查询大量块；同时使用紧凑编码节省空间。
- 🚀 上线影响：2025 年 7 月部署到生产，每分钟处理数百万 CRDT 操作，支持离线模式、智能体协作，并为实时协作状态、批量建议等未来功能打基础。
- 🙌 团队与招聘：文章致谢多位贡献者，并鼓励对协作软件未来感兴趣的工程师查看 Notion 招聘页面。

---

### [](https://plotly.com/blog/announcing-plotly-js-4-plotly-py-7/)

**原文标题**: [Announcing plotly.js 4.0 and plotly.py 7.0](https://plotly.com/blog/announcing-plotly-js-4-plotly-py-7/)

plotly.js 4.0 与 plotly.py 7.0 已发布，这是 Plotly.js 自 2015 年开源维护以来的第 275 次发布；新版带来 quiver 向量图、Sankey 方向/排序、完整 CSS Color 4 颜色支持、自带 TypeScript 类型、MathJax v4、地图缩放限制与 Plotly Cloud 一键分享，同时移除 Mapbox traces 等旧接口并调整多项默认行为。plotly.py 7.0 同步升级渲染引擎，Dash 应用升级 `plotly` 后也会获得 plotly.js 4.0。

- 🧭 发布概况：Plotly.js 4.0.0 发布，plotly.py 7.0 集成该版本；Dash 使用 plotly.py 内置的 Plotly.js，升级 `plotly` 即可让 Dash 图表同步更新。
- 🆕 新图表类型：新增 `quiver` 向量场图，每个箭头由位置 `x/y` 与方向 `u/v` 定义，可按大小着色，适用于风场、洋流、飓风、空气动力学和体育传球等场景。
- 🔀 Sankey 增强：新增 `direction` 控制流向 `forward/reversed`，新增 `sort` 支持 `auto/input`，并升级 d3-sankey。
- 🎨 颜色引擎：改用 `culori` 解析颜色，支持全部 CSS Color 4 字符串，如 `oklch()`、`lab()`、`lch()`、`color()`、`hwb()`、8/4 位十六进制、斜杠 alpha 等。
- 🧑‍💻 TypeScript：plotly.js 自带 TypeScript 类型，按 trace 生成接口，支持深层嵌套类型，可替代 `@types/plotly.js`。
- ➗ MathJax：支持 MathJax v3 和 v4，v4 为可选升级；LaTeX 字符串无破坏性变化，但不再支持 MathJax v2。
- 🗺️ 地图功能：geo 地图新增 `minscale/maxscale` 缩放限制；geo 默认 `fitbounds: "locations"` 自动适配数据；mapbox traces 改为 `map` traces，底层用 MapLibre，无需 token。
- ☁️ 分享图表：modebar 新增 Plotly Cloud 分享按钮，默认开启且上传前确认；可用 `showSendToCloud: false` 关闭，或用 `plotlyServerURL` 上传到自有服务器。
- 📥 下载命名：截图下载现在使用图表标题作为文件名，而不是 `newplot.png`、`newplot (1).png`。
- ⚙️ 默认行为调整：splom 轴默认 `matches: true`；双轴图默认 `tickmode: "sync"` 对齐网格线；`hoveranywhere` 返回真实数据值；国家名解析改用 `country-iso-search`。
- 🧹 移除与不兼容：移除 Mapbox traces、Chart Studio 配置、stream trace、`*src`、`layout.hidesources`；颜色字符串行为按 CSS 规范调整；国家历史名与已不存在国家名不再解析。
- 🐍 plotly.py 7.0：plotly.js 从 3.6.0 升到 4.0.0；`mapbox` 图对象与 Plotly Express 函数改为 `map` 版本；移除长期废弃的 figure factories、Orca 和 Kaleido <1.0，以及相关 `engine` 参数。
- 🛠️ 修复内容：包括地图图标按颜色渲染、跨反子午线地图自动适配与选择、直方图自动分箱、指数刻度、automargin 抖动、空值类别排序、零长度柱文本位置、浮点刻度伪影、colorbar 负 domain 崩溃、退化 MultiPolygon、parcats 数字颜色排序等。
- 🙌 社区贡献：本次发布有 22 位社区贡献者参与，涵盖 quiver、Sankey、地图缩放、直方图、刻度、地图选择、颜色排序和 plotly.py 修复等。
- 🚀 开始使用：JavaScript 可用 CDN 或 npm 安装 `plotly.js-dist-min@4`；TypeScript 用户导入 `plotly.js` 类型并移除 `@types/plotly.js`；Python 执行 `pip install -U plotly kaleido`；Dash 执行 `pip install -U dash plotly`。

---

### [发布 4](https://github.com/huggingface/transformers.js/releases/tag/4.3.0)

**原文标题**: [Release 4.3.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/4.3.0)

Transformers.js 4.3.0 是一次功能与修复并重的更新，核心包括结构化输出、三种新模型架构、Safari 26+ WebGPU 支持、文档全面重构，以及 ONNX Runtime 升级。

- 🚀 Transformers.js v4.3.0 发布，主要新增结构化输出、新模型、WebGPU 升级和文档重构，并升级 ONNX Runtime。
- 🧩 新增实验性、无依赖的 `@huggingface/transformers-structured-output` 包，可将生成约束为 JSON Schema、JSON 对象或正则表达式。
- ⚠️ 结构化输出目前一次仅支持生成一个序列，且需要设置足够的 token 预算以确保输出完成。
- 🧠 新增三种模型架构：DeepSeek-V4、Zaya 和 HRM-Text。
- 🌐 为 Safari 26 及以上版本启用 WebGPU 支持。
- 💾 存储改进包括：Cross-Origin Storage 改用 `requestFileHandle()` 并允许所有来源，非 HTTP(S) 资源跳过浏览器缓存写入，修复 Rspack/Webpack 的 `import.meta` 警告。
- 🛠️ 修复多项问题：重复模型文件下载、Whisper 进度回调、生成时 `num_logits_to_keep` 固定为 1、Granite Speech processor 特征数等。
- 🔊 其他修复包括：恢复全局导出、`RawAudio.toBlob()` 正确处理类型数组字节偏移和长度、Chatterbox 生成后释放 KV cache、Moonshine ASR token 解码。
- 🖼️ 为 Gemma3n 和 Gemma4 图像 - 音频 - 文本到文本模型固定 WebGPU KV cache。
- 📚 文档全面重构，启用 GitHub Actions 每周 Dependabot 更新，在内部 worker 上运行测试，移除未用代码和导出，并更新依赖。
- 🙌 感谢新贡献者，完整变更见 4.2.0...4.3.0；本次发布包含 2 个资产，并获得 5 个 🎉 反应。

---

### [Transformers.js · Hugging Face](https://huggingface.co/docs/transformers.js/index)

**原文标题**: [Transformers.js · Hugging Face](https://huggingface.co/docs/transformers.js/index)

Transformers.js 是 Hugging Face 的 JavaScript 库，让最先进的机器学习模型无需服务器即可直接在浏览器中运行。它的 API 与 Python 版 `transformers` 高度相似，基于 ONNX Runtime 推理，支持 NLP、计算机视觉、音频和多模态任务，并提供 pipeline、WebGPU、量化、教程与模板。

- 🌐 浏览器运行：可直接在浏览器中运行 🤗 Transformers 模型，无需服务端；功能与 Python `transformers` 等价。
- 🧩 多模态任务：支持 NLP、视觉、音频和多模态，如文本分类、问答、摘要、翻译、图像分类、目标检测、语音识别、TTS、零样本分类等。
- ⚙️ 推理后端：使用 ONNX Runtime；可用 🤗 Optimum 将 PyTorch、TensorFlow、JAX 模型转换为 ONNX。
- 🚀 Pipeline API：封装输入预处理、模型推理和输出后处理；情感分析等任务可一行调用，并支持指定模型 ID 或路径。
- 💻 设备选择：默认使用浏览器 CPU/WASM；设置 `device: 'webgpu'` 可启用 GPU，但 WebGPU 仍属实验性。
- 📦 量化选项：资源受限时可用 `fp32`、`fp16`、`q8`、`q4`；WebGPU 默认 `fp32`，WASM 默认 `q8`，`q4` 可降低带宽。
- 📚 文档结构：分为 Get Started、Tutorials、Developer Guides、Integrations、API Reference 五部分。
- 🧪 教程模板：覆盖原生 JS、React、Next.js、浏览器扩展、Electron、Node.js 服务端推理、Vercel AI SDK 聊天机器人。
- 🛠 开发指南：包含 WebGPU、量化模型、私有/门控模型访问、服务端音频处理；集成 Vercel AI SDK。
- ✅ 任务覆盖：支持大量 NLP、视觉、音频、多模态和强化学习任务；不支持表格问答、掩码生成、视频分类、文生图、VQA、表格分类/回归等。
- 🏷 模型查找：在 Hugging Face Hub 选择“transformers.js”标签，可按任务筛选兼容模型。
- 🧠 模型架构：覆盖 BERT、RoBERTa、T5、BART、CLIP、Llama、Qwen、Gemma、Mistral、Whisper、Wav2Vec2、ViT、SAM、DETR 等众多模型。
- 📌 版本安装：当前 `main` 版本需从源码安装；稳定版为 `v3.8.1`，可通过 npm 安装 `@huggingface/transformers`。
- 🎯 快速上手：官方提供 demo 和模板，可在 Hugging Face 上快速启动自己的 Transformers.js 项目。

---

### [](https://github.com/huggingface/transformers.js/blob/main/.ai/skills/transformers-js/SKILL.md)

**原文标题**: [transformers.js/.ai/skills/transformers-js/SKILL.md at main · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/blob/main/.ai/skills/transformers-js/SKILL.md)

Transformers.js 是 Hugging Face 推出的 JavaScript 机器学习推理库，可通过 `@huggingface/transformers` 在浏览器、Node.js、Bun、Deno 中运行文本、视觉、音频和多模态模型，支持 WebGPU 或 WASM，核心入口是 `pipeline()`。

- 📦 安装方式：`npm install @huggingface/transformers`，适用于 Node.js 20+、Bun、Deno 或现代浏览器 ES 模块环境。
- ⚡ 快速上手：`pipeline(task, model?, options?)` 是最常用入口；不传模型时会自动使用该任务的默认模型。
- 🧠 支持任务：覆盖文本分类、NER、问答、摘要、翻译、文本生成、语音识别、TTS、图像分类、图像分割、目标检测、深度估计、特征提取等。
- 🔍 模型筛选：可在 Hugging Face Hub 按 `library=transformers.js` 和 `pipeline_tag` 查找兼容模型。
- ✅ 模型预检：推荐模型前必须确认存在 ONNX 权重；可用 `ModelRegistry.get_available_dtypes(modelId)` 检查 dtype 列表。
- ⚠️ 异常区分：空数组表示模型存在但无 ONNX 文件；`ModelFileNotFoundError` 表示模型不存在或私有/受限；网络错误应重试而非拉黑模型。
- 🧩 量化选项：`dtype` 支持 `fp32`、`fp16`、`q8`、`q4`、`q4f16`，越小通常下载和运行越快，但精度可能下降。
- 🖥️ 设备选择：默认 CPU/WASM；传入 `device: "webgpu"` 可在支持时使用 GPU 推理。
- 🧹 内存管理：管道会持有模型权重和会话，使用后应调用 `await pipe.dispose()`，尤其长驻服务、替换模型或组件卸载时。
- ⚙️ 环境配置：通过 `env` 控制远程模型、磁盘缓存、浏览器缓存、日志级别和 fetch，如 `allowRemoteModels`、`useFSCache`、`useBrowserCache`、`logLevel`。
- 🔄 管道选项：支持 `progress_callback`、设备、dtype、缓存、生成参数、流式输出和 KV 缓存复用。
- 🚫 禁止事项：不要复用已 dispose 的管道；不要在热循环中重复创建管道；不要阻塞启动等待下载；不要编造模型 ID。
- 📚 参考文档：官方文档、API 参考、示例仓库，以及本地 `TASKS.md`、`CONFIGURATION.md`、`PIPELINE_OPTIONS.md`。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=sponsored)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=sponsored)

Meticulous 是面向复杂代码库的自动化端到端视觉测试平台，通过录制用户交互、AI 生成持续演进的测试套件，并在 PR 合并前展示影响，实现零开发维护、确定性、无 flake 的测试体验，可补充或替代现有测试体系。

- 🚀 核心卖点：自动化、穷尽式、确定性验证，零开发者投入，让代码以 AI 代理编写速度发布。
- 🏢 已获 100+ 组织信任，包括 Dropbox、Notion 等；用户称无需合并后调试、零维护、无 flake。
- 🎥 工作原理 1：在本地、预发和预览 URL 添加脚本标签记录日常交互，也可选择记录生产会话。
- 🤖 工作原理 2：AI 引擎跟踪每次交互执行的代码分支，生成持续演进的可视化端到端测试，覆盖每行代码、每个用户流程和边缘情况。
- 🔍 工作原理 3：打开 PR 即可看到变更对用户工作流的影响；默认保存并回放后端响应，实现无副作用测试，避免数据变化导致假阳性。
- 🧩 集成简单：只需添加录制脚本并安装 CI 集成，无需为每次测试设置特殊账号或 mock 数据。
- 🔄 测试自动演进：新功能或边缘情况出现时自动新增测试，过时测试自动移除，开发者无需编写、修复或维护测试。
- ⚡ 速度与稳定性：从 Chromium 层构建确定性调度引擎，消除 flake，并支持大规模并行执行。
- 🖥️ 大规模测试：测试在计算集群中高度并行，可测试数千个屏幕，并在 120 秒内获得结果。
- 🧪 灵活使用：可与现有测试套件组合，也可完全替代现有测试，适合最复杂的应用。
- 🛠️ 支持框架：NextJS、React、Vue、Angular、Nuxt、SvelteKit，通过脚本标签或 recorder-loader 接入。
- 🔐 配套入口：提供集成、安全与文档，几分钟即可设置并生成覆盖全应用的测试。

---

### [](https://github.com/shadcn-ui/lint)

**原文标题**: [GitHub - shadcn-ui/lint: An agent-first linter for Tailwind design systems. Write design system rules that agents can verify. · GitHub](https://github.com/shadcn-ui/lint)

@shadcn/lint 是 shadcn-ui 发布的面向 AI 编程代理的 Tailwind 设计系统 linter，让团队定义 UI 规则，并让代理在违规时获得基于组件、变体和主题的修复建议；项目采用 MIT 许可证，约 2.6k stars。

- 🎯 定位：agent-first linter，先定义设计系统允许什么，代理写错时解释问题并建议如何修复。
- 🧱 兼容性：适用于 Tailwind v4，不要求使用 shadcn/ui；支持 ESLint 和 Oxlint，以及 React、Vue、Svelte。
- 🩺 对比 TypeScript：TS 通常只报“不允许”，该 linter 还能告诉代理应改用 size、margin/gap、主题颜色，或去哪个文件查找配置。
- ⚙️ 可配置规则：通过 no-restyle、allow/deny、contracts 为 Button、CardTitle、CardContent 等组件设置独立策略。
- 📏 内置规则：包括 no-restyle、no-raw-colors、no-arbitrary-values、no-inline-styles、no-unknown-classes、require-static-classes。
- 💬 面向代理的消息：支持自定义错误消息和占位符，如 {{component}}、{{sizes}}、{{file}}，直接给出设计系统指引。
- 🧪 实测效果：150+ 任务运行中，多种模型通常在一轮修正后达到 0 违规；Claude 控制运行中修复成本降低 10%-48%。
- 🧩 为什么用 linter：可编程、无需改组件源码，可约束第三方组件，跨项目共享配置，同时保持组件灵活。
- 🚀 快速开始：让代理阅读 SETUP.md，或手动安装 @shadcn/lint；需 Node.js 20.19+，ESLint 9.30+ 或 Oxlint 1.80+。
- 🛠️ 配置：通过 settings.shadcn 设置 ui、componentImports、ignoreImports、mergeFunctions、variantFunctions、note 等。
- 🏢 Monorepo：使用 workspace 包导入前缀，对共享 UI 组件目录做规则 override，各应用保留自己的主题配置。
- 📚 资源：提供文档、规则选项、贡献指南、评测方法，并采用 MIT 许可证。

---

### [可插拔、可扩展且有趣的开发者工具 |](https://devfra.me/posts/pluggable-extensible-playful-devtools)

**原文标题**: [Pluggable, Extensible, and Playful DevTools | Devframe](https://devfra.me/posts/pluggable-extensible-playful-devtools)

Devframe 是 Anthony Fu 等人推出的框架无关 DevTools 基础层，旨在将 DevTools 从特定框架和开发服务器中解放出来：定义一次工具能力，即可通过统一的 Web 标准 handler 挂载到任意宿主框架、独立适配器或编码代理中，最终构建模块化、可组合、协作的通用 DevTools 生态系统。

- 🌱 **背景与痛点**：团队多年构建了 UnoCSS Inspector、Vite Plugin Inspect、Vitest UI、Nuxt DevTools 等工具，它们本质都在“让隐式状态可见”，却各自重复实现 RPC、状态同步、序列化、Web 界面等基础设施，且大多绑定单一框架。
- 💡 **愿景来源**：2023 年提出“Universal DevTools Ecosystem”，主张共享能力与框架特定能力自由组合；从 Nuxt DevTools 到 Vite DevTools 的实践逐步验证了方向。
- ⚙️ **Devframe 定位**：框架中立的 DevTools 构建基础，类比 Web 应用之于 Nuxt/Next.js，适配器层面类比 unplugin，让工具定义一次、多处运行。
- 🧩 **核心 API**：`defineDevframe()` 描述工具身份与能力（RPC、共享状态、SPA、诊断、代理接口）；`initDevframe()` 生成 Web 标准 `Request → Response` handler 及 Connect 风格中间件。
- 🔌 **可移植性**：基于 Web 标准边界，Hono、Nitro、Next.js、SvelteKit、Vite、Rsbuild 等均可原生挂载，仅需少量宿主胶水代码。
- 📦 **适配器生态**：同一份定义可打包为 CLI、独立 dev server、Vite DevTools 插件、MCP server、静态报告等多种入口，一个包可同时提供多种形态。
- ✅ **落地案例**：Node Modules Inspector、ESLint Config Inspector、Vite Plugin Inspect 已采用该模型；浏览器端 UI 框架自由选择，内置 devframes 覆盖 Vue、Svelte、Solid、React、Next.js。
- 🤖 **双接口设计**：视觉界面用于人类探索，编码代理通过 MCP 适配器获取结构化能力；RPC 默认私有需显式暴露，并集成 Vercel 的 json-render 支持代理生成可预测 UI。
- 📊 **内置 Devframes 示例**：Data Inspector（Vue + Jora 查询实时对象）、Terminals（Svelte + 浏览器 PTY 终端）、Accessibility Inspector（Solid + axe-core 扫描 WCAG 违规），另有 VS Code 编辑器、资源管理、Git 面板等。
- 🏗️ **Hub 组合层**：`@devframes/hub` 无头且框架中立，多个 devframes 共享 RPC 注册、状态存储、连接、认证与聚合 MCP 端点，通过 `initHub()` 统一挂载，提供一致入口。
- 🚀 **旗舰与落地**：Vite DevTools 是首个基于此基础的旗舰宿主；Nuxt DevTools v4 构建于 Devframe + Vite DevTools 之上，预计随 Nuxt v5 发布；Vue DevTools 正在迁移；Next.js DevTools 已有内部原型。
- 🎯 **下一步**：Devframe v1.0 稳定接口，Vite DevTools 将发布稳定版，继续探索编码代理接口、权限管理与跨工具协作的最佳实践，并欢迎社区贡献与反馈。

---

### [GitHub - hieunc229/mailflare：面向专业人士和团队的电子邮件 · GitHub](https://github.com/hieunc229/mailflare)

**原文标题**: [GitHub - hieunc229/mailflare: Email for professionals and teams · GitHub](https://github.com/hieunc229/mailflare)

Mailflare（hieunc229/mailflare）是一个基于 Cloudflare 的自托管自定义域名邮箱项目，面向个人与团队，支持邮件收发、邮箱管理、路由规则、实时通知，并可部署到 Cloudflare 或通过 Docker 自托管；仓库约 3.4k stars、469 forks，采用 AGPL-3.0 许可证。

- 📬 核心定位：为自定义域名提供自托管邮箱收件箱，运行在用户自己的 Cloudflare 账户中。
- ✉️ 主要功能：支持发送和接收邮件、附件、富文本、签名、自动回复，以及个人和共享邮箱的委托访问。
- 🗂️ 邮件管理：支持搜索、自定义文件夹、星标、稍后处理、归档、垃圾邮件和废纸篓。
- ⚙️ 路由规则：可按规则存储、转发、拒绝或分类 incoming messages，并支持实时收件箱更新和新邮件通知。
- 👥 账户与安全：可管理联系人、屏蔽发件人、导入导出邮件，以及账户、权限、API keys、webhooks、审计日志和数据库备份。
- ☁️ 工作原理：Email Routing 负责入站邮件，Cloudflare 邮件服务负责出站邮件，数据存储在 D1，附件存储在 R2。
- 💰 成本：接收邮件可免费设置；发送邮件需要 Paid Worker 计划（约 $5/月），推荐使用以获得更顺畅体验。
- 🚀 Cloudflare 部署：三步完成部署、初始化和连接域名；应用名需保持为 mailflare，且部署时必须提供 CF_TOKEN。
- 🔐 CF_TOKEN 要求：需要创建具有 Email Sending、DNS、Email Routing 等权限的 scoped Cloudflare API token。
- 🐳 Docker 自托管：也可作为单容器运行，用 SQLite 和本地文件替代 D1/R2，支持内置 SMTP 入站或 Cloudflare relay Worker。
- 🛠️ 本地开发：复制 .dev.vars.example 后安装依赖、运行本地数据库迁移和 npm run dev，访问 localhost:3000；可用 npm run db:seed 加载示例数据。
- 📚 文档与许可：提供部署配置、API 集成、故障排除文档，项目采用 AGPL-3.0 许可证。

---

### [发布 v14.0.0 · gridstack/gridstack.js · GitHub](https://github.com/gridstack/gridstack.js/releases/tag/v14.0.0)

**原文标题**: [Release v14.0.0 · gridstack/gridstack.js · GitHub](https://github.com/gridstack/gridstack.js/releases/tag/v14.0.0)

gridstack.js v14.0.0 已发布，核心带来 mode 与 cellHeight:'fill' 两项重大变更，并集中修复拖拽、缩放、触摸及 React/Vue 相关问题。
- 🚀 v14.0.0 为最新版本，由 adumesny 于 9 月 21 日 06:35 发布，提交 3f0469d 已通过 GitHub 验证签名。
- ⭐ 项目公共仓库当前约 9.1k Star、1.4k Fork，28 个 Issues、1 个 Pull Request。
- 🧩 重大变更：新增 mode?: 'top' | 'float' | 'list' | 'compact'，取代旧的 float:boolean。
- 📋 新增 list 模式：项目按行优先顺序连续重排，类似可排序列表；拖拽、缩放、添加或删除时其他项目自动重排，而非被向下推，拖放到另一项会占据其位置。
- 🔗 提供新的 list.html 演示。
- 📐 重大变更：新增 cellHeight: 'fill'，让行均分容器高度，形成固定尺寸网格。
- 🔗 提供新的 cell-height.html 演示。
- 🖱️ 侧边栏拖入项现在会触发 dragstart/drag/dragstop 事件。
- 🛡️ 修复在 change 事件期间调用 update() 导致崩溃的问题。
- 🧲 修复缩放时显示其他小部件缩放手柄的问题。
- 🕶️ 修复在打开的 Shadow DOM 中查找拖拽手柄，参见 title_drag.html。
- 📱 修复触摸中途销毁小部件时未释放全局触摸锁的问题。
- 📏 修复 API update() 未像拖拽一样遵守 maxRow 的问题。
- ⚛️ 修复 React/Vue 中渲染无 id 但有组件的拖入小部件。
- 🖲️ 允许从嵌套在 button/input 手柄内的元素开始拖拽。
- 🔁 修复 React/Vue 在交互式拖拽/缩放后重新渲染条目内容。

---

### [演示](https://gridstackjs.com/demo/index.html)

**原文标题**: [Demo](https://gridstackjs.com/demo/index.html)

以下为网格组件/库的演示索引，涵盖基础布局、嵌套网格、响应式、RTL、打印、序列化、移动触控、Web Component，以及 Angular、React、Vue 框架封装；旧版 jQuery 演示已不再支持，仅用于功能对比。

- 🧱 基础与布局演示：AniJS、Cell Height、Column、CSS & attributes、Float grid、Grid Lines、Static、Size To Content。
- 🧩 网格类型：List grid、List grid (advanced)、Two grids、Two grids Vertical、Web Component。
- 🪆 嵌套网格：Nested grids、Nested Advanced grids、Nested Constraint grids。
- 📱 交互与移动：Mobile touch、Title drag、Transform (scale+offset)、Lazy Load。
- 📐 响应式与方向：按列尺寸、断点、layout:'none'，以及 Right-To-Left (RTL)。
- 🖨️ 打印：Print grid、Print grid (advanced PrintOptions)。
- 💾 数据与状态：Serialization。
- ⚛️ React 集成：ReactJS、ReactJS (Hooks)、多网格、受控模式（标注 NOT Ideal）；官方 React Component wrapper。
- 🅰️ Angular 集成：现已提供 Angular Component，简化该框架集成。
- 🖖 Vue 集成：现已提供官方 Vue 3 Component wrapper。
- 🌐 其他示例与集成：Knockout.js、Website demo 1、Website demo 2。
- ⚠️ 旧版：Old v5.1.1 Jquery Demos 不再支持，仅用于对比旧版库功能，含 Two grids、Nested grids。

---

### [](https://github.com/sindresorhus/image-dimensions)

**原文标题**: [GitHub - sindresorhus/image-dimensions: Get the dimensions of an image · GitHub](https://github.com/sindresorhus/image-dimensions)

sindresorhus/image-dimensions 是一个轻量、零依赖的 JavaScript 库，用于获取图片尺寸，可在浏览器、Node.js、Bun、Deno 等现代 JavaScript 环境中运行；支持多种常见图片格式，并提供流式与内存数据两种 API 以及 CLI。仓库当前约 595 stars、19 forks，采用 MIT 许可。

- 📦 安装：`npm install image-dimensions`。
- 🖼️ 支持格式：JPEG、PNG（含 APNG）、GIF、WebP、AVIF、HEIF（含 HEIC）；支持所有格式不是目标，但欢迎添加 JPEG XL。
- 🌊 推荐 API `imageDimensionsFromStream(stream)`：从流中读取最少数据，返回 `{width, height, type}` 或 `undefined`；示例中只读取少量字节即可获取远程图片尺寸。
- 💾 API `imageDimensionsFromData(data)`：从已加载到内存的 `Uint8Array` 获取尺寸，返回相同结构或 `undefined`。
- 🏷️ `ImageType` 导出类型：`'png'`、`'jpeg'`、`'gif'`、`'webp'`、`'avif'`、`'heic'`。
- ⚠️ 注意：返回原始像素尺寸，不应用 EXIF 或 HEIF/AVIF `irot` 方向信息。
- 💻 CLI：`npx image-dimensions unicorn.png`，输出如 `630x400`。
- 🆚 与 `image-size` 对比：本包优势是零依赖、更小、支持非 Node.js 环境、无多余文件读取 API；`image-size` 优势是支持更多格式并支持 JPEG 方向。
- 🔗 相关包：`image-type` 检测图片类型，`file-type` 检测文件类型。
- 📄 仓库：公开、MIT 许可，主分支有 39 次提交，包含 fixtures、types、测试与 GitHub Actions 等文件。

---

### [](https://feedsmith.dev/)

**原文标题**: [Feedsmith: Fast JavaScript Feed Parser and Generator](https://feedsmith.dev/)

Feedsmith 是一个快速、全能的 JavaScript feed 解析与生成库，支持 RSS、Atom、RDF、JSON Feed 和 OPML，并兼容大量流行命名空间；3.0 版本已发布，带来改进和破坏性变更。它强调保留原始 feed 结构、宽松解析、类型安全和性能，适合处理真实世界中旧格式或不完全规范的 feed。

- 🚀 Feedsmith 可同时解析与生成 RSS、Atom、RDF、JSON Feed 和 OPML。
- 🧩 通用解析器与格式专用解析器会把 feed 转成镜像原始结构的对象，并将旧元素映射为现代等价元素。
- 🎉 Feedsmith 3.0 已发布，包含多项改进和破坏性变更，升级需参考迁移指南。
- 📡 支持格式包括 RSS 0.9x/2.0、Atom 0.3/1.0、RDF 0.9/1.0、JSON Feed 1.0/1.1、OPML 1.0/2.0。
- 🏷️ 命名空间覆盖广泛，如 Atom、Dublin Core、Syndication、Content、iTunes、Podcast Index、Media RSS、Spotify、YouTube、GeoRSS 等。
- 🧠 智能命名空间处理：会把自定义前缀规范化为标准前缀，例如 `<custom:creator>` 变为 `dc.creator`。
- 🛠️ 一个包即可完成解析和生成，减少多库切换成本。
- 🧽 宽松解析：规范化旧元素，大小写不敏感，容忍非官方命名空间 URI、空白、HTTPS 变体等。
- 🧯 对格式错误或不完整的 feed 也能优雅处理，并尽可能提取有效数据。
- ⚡ 性能突出，号称是最快的 JavaScript feed 解析器之一；基于 TypeScript，类型安全，支持 tree-shaking。
- ✅ 测试充分：超过 4000 个测试，99% 代码覆盖率。
- 💻 兼容 Node.js 和现代浏览器，也支持纯 JavaScript，无需 TypeScript。
- 🎯 核心理念是保留原始 feed 结构，而不是把 `author`、`dc:creator`、`creator` 或 `dc:date`、`pubDate` 等字段粗暴合并。
- 📚 相比其他库，它避免因合并字段、日期来源或多个 `<atom:link>` 处理不一致而导致信息丢失。
- 🌍 目标是完全按照规范支持所有主要 feed 格式和命名空间，其中 RDF 生成标记为计划中。

---

### [电子签名 API 指南](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/esignature-api-guide-add-signing-app/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=javascriptweekly_20260922)

**原文标题**: [eSignature API Guide: Add Signing to Your App](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/esignature-api-guide-add-signing-app/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=javascriptweekly_20260922)

本指南介绍如何将发票 PDF 提取为结构化 JSON，并解决不同版式带来的解析难题。

- 🧾 发票 PDF 通常没有统一布局，通用文本提取容易出错。
- 📊 多列表格、换行单元格和扫描页面是常见难点。
- 🔌 指南演示通过四个 API 调用，将原始发票 PDF 转换为带类型的 JSON。
- 🧩 还包含后处理代码，用于把 API 响应映射成清晰的发票 schema。
- ⚙️ 最终生成的 JSON 可直接供后端使用。

---

### [](https://fingerprint.com/try/bot-detection/?utm_source=JSWeekly09222026)

**原文标题**: [Fingerprint | Industry-leading Bot Detection](https://fingerprint.com/try/bot-detection/?utm_source=JSWeekly09222026)

Fingerprint 提供面向开发者和反欺诈团队的隐形机器人检测 API，可在约 10 行代码内为网站加入无感机器人与 AI 检测，并用多种信号判断自动化流量应放行还是拦截。

- 🤖 核心产品是隐形 bot 检测 API，面向开发者与反欺诈团队，主打无摩擦接入。
- 📦 通过 `npm i @fingerprint/agent` 安装，获取 API key 后可免费开始使用。
- 🧩 示例代码会在注册流程中检查 `event.bot !== "not_detected"`，若检测到机器人则阻止注册。
- 🛡️ 主要用例包括：检测已签名 AI agent、阻止虚假注册、机器人结账、账户接管和内容抓取。
- 🚫 CAPTCHA 被指已不适应现代互联网：给真实用户增加摩擦、破坏 AI agent，却仍可能放过高级机器人。
- 👻 Fingerprint 提供无 CAPTCHA、无挑战的体验，区分有益自动化与恶意机器人，保持用户流程顺畅。
- 🧠 可识别各类 AI agent 与机器人，例如 ChatGPT Agent、Gemini、Manus 等，并持续加入新机器人识别能力。
- 🔍 不只做 bot 检测：通过单一端点 `api.fpjs.io/v4/events/{event_id}` 获取更多信号，判断流量真实意图。
- 💻 兼容现有 JavaScript 技术栈：Web、JavaScript、React、Next.js、Preact、Vue、Nuxt、Angular、Svelte 等，后端不限。
- ⚙️ Rules Engine 支持无代码配置规则，结合 Browser Bot、Developer Tools、Anti-Detect Browser、Virtual Machine 和数据中心 IP 等信号拦截复杂欺诈。
- 🌟 基于开源技术，GitHub 星标 31.2K+，NPM 月下载 5,400,000+；Booking.com、Dropbox、Plaid、Binance、Resend 等公司信任。
- ⏱️ 可通过包管理器或 CDN 在几分钟内完成设置，免费开始，无需信用卡或销售通话。

---

### [](https://trigger.dev/changelog/chat-agent?utm_source=fnf&utm_medium=newsletter&utm_campaign=september&utm_term=js-weekly&utm_content=chat-agent-launch)

**原文标题**: [Introducing chat agent | Changelog](https://trigger.dev/changelog/chat-agent?utm_source=fnf&utm_medium=newsletter&utm_campaign=september&utm_term=js-weekly&utm_content=chat-agent-launch)

chat.agent 是 Trigger.dev 推出的持久化 AI 聊天代理方案，为每个对话分配独立的有状态 Linux 机器，支持无超时运行、流式传输、崩溃恢复和跨会话记忆，已在实际生产环境中处理数百万次会话。

- 🤖 **核心机制**：每个对话拥有独立的有状态机器，首条消息到达时启动，按需休眠与唤醒，全程无需手动管理状态
- 🐧 **真实 Linux 环境**：非受限运行时，可安装任意工具、运行 CLI、驱动无头浏览器，CPU 和内存可按对话配置
- ⏳ **无超时持久计算**：单轮对话可无限时长运行，生产环境中 1/20 的代理运行超过 36 分钟，远超普通请求限制
- 💾 **跨休眠记忆**：变量、缓存、子代理状态在对话轮次间保留，但机器崩溃后内存不恢复，重要数据仍需存数据库
- 🔄 **持久流式传输**：刷新页面后流从断点继续，无需重跑模型；关闭浏览器数天后回来，对话依然存在
- ⚡ **快速首轮响应**：Head Start 功能让首次 LLM 调用在本地热服务器中执行，测试中首 token 时间和整轮耗时均减半
- 💤 **等待零成本**：工具无 execute 函数时轮次暂停，代理挂起等待人工审批，暂停期间不计费，可跨周末
- 📊 **内置追踪与指标**：每轮对话为独立 span，AI 指标仪表盘展示成本、token、延迟，数据支持 TRQL 查询
- 🔌 **兼容 AI SDK**：服务端用 streamText，客户端用 useChat，chat.agent 作为传输层嵌入，无需中间 API 路由
- 🧩 **灵活扩展**：支持自定义代理循环、原始会话原语、对话压缩、提示缓存、MCP 服务器和 AgentChat 多客户端驱动
- 🧪 **测试与生态**：可在单元测试中驱动真实轮次，作为 Trigger.dev 任务复用队列、调度、批处理等现有功能
- 📜 **开源与计费**：Apache 2.0 开源，按实际运行的计算时间计费，暂停的对话不产生费用

---

### [neat-annotations — 整洁的手绘风格 CSS 注释](https://neat-annotations.syabro.com/)

**原文标题**: [neat-annotations — neat hand-drawn CSS annotations](https://neat-annotations.syabro.com/)

纯 CSS 的手绘标注库 neat-annotations，无需 JavaScript，仅一个小文件，可为任意行内元素添加箭头和手写标签。

- 🖍️ 纯 CSS 实现，无 JavaScript，单个小文件即可使用。
- 📦 安装：通过 jsDelivr 引入 CSS，或下载 neat-annotations.css 后本地链接。
- ✍️ 可选加载 Shantell Sans 手写字体；不加载则标签回退为 cursive。
- 🧭 用 ann-n、ann-e、ann-s、ann-w 等类按指南针方向绘制箭头。
- 🎨 内置五种颜色、动画彩虹和暖灰默认色，也可用 --ann-color 自定义任意 CSS 颜色。
- 🔆 目标高亮：默认添加标记；ann-no-mark 保留原填充；省略 data-note 可只做文本高亮。
- 🧷 支持堆叠注释：嵌套两个注释可从不同方向指向同一目标。
- 📝 长注释自动换行，可用 --ann-label-max-width 控制标签宽度。
- ⚖️ 示例来自 mdtask.dev，MIT 许可，源码在 GitHub。

---

### [](https://sunilpai.dev/posts/the-senior-engineer-death-spiral/)

**原文标题**: [the senior engineer death spiral • Solving the decision problem](https://sunilpai.dev/posts/the-senior-engineer-death-spiral/)

高级工程师在新岗位、晋升或接手大项目后，常因冒充者综合征而急于证明自己，试图模仿更高级别工程师、独自推进宏大方案，结果逐渐失联、硬扛压力，最终滑向倦怠甚至离职的“死亡螺旋”；破解之道是暂时“降一级”、成为最好的队友，转向以势头和日常节奏为核心，通过持续沟通、可靠交付和修复关系来重建信任与耐力。

- 🌀 触发点常是新工作、晋升或大项目：想立刻证明自己，于是设计更宏大的东西，甚至“扮演”更资深的工程师。
- 🕳️ 人会开始长时间消失，站会只说“进展顺利、很快有东西可展示”，但实际拿不出成果。
- 😰 内心压力升级为“我得更努力，把进度补回来”，随后失眠、漏餐、抑郁，工作和个人关系都受损。
- 🔥 螺旋终点可能是倦怠休假、绩效改进计划（PIP）、被解雇或主动辞职。
- 🌐 疫情、远程办公和编码代理让工程师更孤立、更少结构化支持，因此不能让同事不知道你在做什么。
- 🗣️ 要主动分享工作，做到“大家都知道你在忙什么”，但不必显得惹人厌。
- 🤝 从假设周围人都在善意合作开始：公司雇用的是现在的你，不是六个月后你想象中的自己。
- ⬇️ 反直觉做法是先“降一级”，成为最好的队友，做 bug、杂活、文档和组织性工作，帮助团队。
- 🚀 从结果导向转为势头导向：建立日常节奏，修复关系，获得耐力和信任。
- 🏃 大项目不靠一次性大爆发，而像马拉松一样，每天、每小时持续稳定推进，直到成为肌肉记忆。
- 📈 可靠性和信任会让队友与经理愿意交给你更大的任务；你在经营声誉，软件成果只是下游结果。

---

### [](https://simonwillison.net/2026/Sep/21/jev/)

**原文标题**: [Jev introduces a new shape of LLM—System One, aka Decision Models](https://simonwillison.net/2026/Sep/21/jev/)

TypeSafe AI 发布 Jev，作者将其视为“System One 模型”或更贴切的“决策模型”。它把文本输入转化为浮点决策输出，主打快速、廉价、适合分类与排序，同时也带来黑箱、偏见与评估难题；发布不到一周，社区已出现大量实验、开源复刻和工具支持。

- 🧠 TypeSafe AI 推出 Jev，称其为“System One 模型”的首个示例；Simon 和 Maggie Appleton 更倾向于叫它“决策模型”。
- 🔢 与传统 LLM 不同：Jev 接受文本输入，但不输出文本，而是返回类别、是/否答案、评分及对应置信度等浮点数。
- ⚡ 它非常快且便宜：只对输入收费，输出免费；首个模型输入价格为 $0.042/百万 token，低于 OpenAI GPT-5 Nano 的 $0.05/百万 token。
- 🧩 使用方式：构造 state 对象（字符串、字符串数组或键值对），可同时提交多个问题；问题并行评估，多个问题耗时接近一个问题。
- ❓ 支持三类问题：Noul 是/否问题返回 0 到 1 的置信度；Choice 在选项中给出置信度和概率分布；Score 在带描述的数值区间上返回浮点分。
- 🎯 适用场景包括分类任务、垃圾信息检测、标签建议、优先级与排名；也可用于搜索重排，例如先用 BM25 取 100 个候选，再让 Jev 评分。
- ⚠️ 当前局限：不擅长数字、日期和“对抗性内容”，官方文档也承认这些弱点。
- 🕳️ 黑箱问题回归：Jev 只返回浮点数，不解释原因；若判定垃圾信息，无法知道哪些内容信号导致该结果。
- ⚖️ 偏见风险突出：作者担心它被用于求职者排名等场景；测试旧金山湾区城市“好城市？”时，Cupertino 最高、East Palo Alto 最低。
- 🧪 评估更重要：因黑箱且便宜，适合跑数百甚至数千次结构化实验，成本只需几美分。
- 🎮 社区创意用途：jevchat 把它变成糟糕聊天模型，jev-leftpad 实现 left-pad，jev-2048 用它玩 2048。
- 🏗️ 开源复刻涌现：Kev 基于 Qwen 3.5 做出 0.8B、4B、9B 模型；还出现 JevBench 基准来比较“Jev 类决策模型”。
- 🔌 工具支持：Simon 发布 llm-typesafe 插件，为 LLM CLI/Python 库添加 Jev 支持，可通过命令行向 Jev 提问。
- 🌐 发布不到一周，围绕 Jev 的活动非常活跃，显示出这种新模型形态引发广泛关注。

---

### [](https://socket.dev/blog/github-actions-cache-mode)

**原文标题**: [GitHub Actions Adds cache-mode to Limit Cache Poisoning Risk | Socket](https://socket.dev/blog/github-actions-cache-mode)

GitHub Actions 新增 cache-mode，通过按工作流或作业限制缓存访问来降低缓存投毒风险，但并未覆盖所有 Actions 风险。

- 🛡️ GitHub Actions 推出 cache-mode，为 Actions 缓存提供最小权限控制，重点防范缓存投毒攻击。
- ☠️ 缓存投毒利用共享缓存：一个上下文写入的条目可被另一个上下文恢复并执行，攻击者可植入恶意构建产物或依赖，从而获得受信任工作流的权限和密钥。
- 🧪 该技术曾用于 2024 年 Ultralytics PyPI 包事件，以及 2026 年 5 月 TanStack npm 包事件；后者结合 `pull_request_target` 攻击，发布了 42 个 `@tanstack/*` 包共 84 个恶意版本。
- 🔏 SLSA 溯源与 Sigstore 签名无法发现被投毒的缓存，因为证明只覆盖构建来源，不保证从缓存拉取的输入完整性。
- ⚙️ cache-mode 支持四种值：`read` 仅恢复、阻止保存，是 `pull_request_target` 等低信任事件默认值；`write` 可恢复并可保存，是 `push` 等受信任事件默认值；`write-only` 仅保存、阻止恢复；`none` 阻止所有缓存访问。
- 🧱 作业级设置覆盖工作流级设置，由缓存服务强制执行，并贯穿可复用工作流，确保被调用工作流不会获得比调用方更多的缓存权限；低信任事件声明写权限会触发警告。
- 🤖 GitHub 建议 AI 代理工作流使用 `none`，因为这类工作流可能执行来自 issue 或 PR 文本的不可信输入；Cline 事件中 GitHub issue 的提示注入就疑似导致缓存投毒。
- 🗳️ `write-only` 模式源于公开反馈：安全研究员 Adnan Khan 推动加入该值，让受信任分支可填充缓存但永不恢复缓存。
- ⚠️ cache-mode 不能消除所有 Actions 风险，检出不可信代码、运行包生命周期脚本或在运行器内铸造 OIDC 令牌等路径仍可能暴露。
- 🔐 GitHub 建议为每个工作流或作业仅授予所需的缓存访问权限，即 cache-mode 所支持的最小权限原则。

---

### [](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

**原文标题**: [Postmortem: TanStack npm supply-chain compromise | TanStack Blog](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

2026 年 5 月 11 日 19:20–19:26 UTC，TanStack 的 Router/Start 仓库遭遇 npm 供应链攻击，42 个 `@tanstack/*` 包被发布 84 个恶意版本；5 月 15 日官方宣布全部清除，当前所有可用版本安全，其他 TanStack 包未受影响。

- 🚨 攻击链为 `pull_request_target` “Pwn Request” + GitHub Actions 缓存投毒 + 从 runner 内存提取 OIDC token；未窃取 npm token，发布流程本身未被攻破，但恶意代码用 OIDC 直接向 npm 发布。
- 📦 受影响范围仅限 Router/Start 仓库，共 42 包、每包 2 个版本、合计 84 个恶意版本；Query、DB、Store、AI、Table、Form、Hotkeys、Virtual、Pacer、Config、Devtools、CLI、Intent 等确认未受影响。
- 🧬 恶意载荷会在 `npm/pnpm/yarn install` 时解析恶意 `optionalDependencies`，运行约 2.3 MB 的 `router_init.js`，窃取 AWS、GCP、Kubernetes、Vault、npm、GitHub、SSH 等凭据。
- 📡 数据通过 Session/Oxen 加密文件上传网络外传，并枚举同一维护者的其他 npm 包进行自传播，扩大供应链影响。
- 🧪 预攻击阶段：攻击者创建 `zblgg/configuration` fork，伪造 `claude` 身份提交约 3 万行 `vite_setup.mjs`，并通过 PR #7378 触发 `pull_request_target` 工作流。
- ☠️ 缓存投毒：`bundle-size.yml` 在 `pull_request_target` 中检出 fork 的 merge ref 并构建，`actions/cache` 将污染后的 pnpm store 写入 `release.yml` 稍后会恢复的缓存 key。
- 💥 引爆阶段：`release.yml` 重跑时恢复被污染缓存，恶意二进制在测试/清理阶段运行，从 `Runner.Worker` 进程内存提取 OIDC token，绕过 Publish Packages 步骤直接发布。
- 🕒 两批恶意版本分别在 19:20:39 和 19:26:14 UTC 发布；随后被 deprecate，npm 在当晚至次日移除 tarball。
- 🔍 StepSecurity 研究员 `ashishkurmi` 在约 26 分钟后公开 issue #7383，提供完整 IOC 和包列表；Tanner 接到 Socket.dev 电话后启动响应。
- ⏱️ 响应时间：约 26 分钟公开检测；约 1 小时 43 分完成全部 84 个版本废弃；约 4 小时 35 分完成 npm 侧最后移除。
- 🛡️ 官方处置包括撤销团队推送权限、批量废弃、清理所有 TanStack GitHub Actions 缓存、重构 `bundle-size.yml`、固定第三方 action SHA、发布 GHSA-g7cv-rxg3-hmpx 并请求 CVE。
- ✅ 当前状态：2026-05-15 发布 all-clear，所有当前可安装的 TanStack 包（含 Router/Start）均安全。
- ⚠️ 用户建议：若在 2026-05-11 安装过受影响版本，应视安装主机可能被入侵，轮换 AWS、GCP、Kubernetes、Vault、GitHub、npm、SSH 等可达凭据。
- 🔎 关键 IOC：恶意 `optionalDependencies` 指向 `@tanstack/setup`；`router_init.js`；缓存 key `Linux-pnpm-store-6f923...`；外传域名 `filev2.getsession.org`、`seed{1,2,3}.getsession.org`；攻击者账号 `zblgg`、`voicproducoes`。
- 🧠 根因是三个已知漏洞链式利用：`pull_request_target` 信任边界错误、GitHub Actions 缓存跨 fork/base 投毒、OIDC token 可从 runner 内存读取；单独任一项都不足以完成攻击。
- 📝 教训：缺少内部发布告警，依赖外部发现；`pull_request_target` 和浮动 action 版本未审计；npm 不可 unpublish 导致移除延迟；OIDC 可信发布缺少逐次审核。
- ❓ 待查问题包括缓存日志、初始 PR 提交、fork 对象传播、实际下载量、其他仓库是否复用同类模式、维护者机器是否受影响等。

---

