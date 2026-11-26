# [Issue #768: The things you can now do directly in the browser — Frontend Focus](https://frontendfoc.us/issues/768)

### [GitHub - luruke/browser-2027：2027 年你能用浏览器做的事 ☕️ · GitHub](https://github.com/luruke/browser-2027)

这是 luruke 整理的 browser-2027 清单，也是七年前 browser-2020 的续作：它沿用原有规则，非穷尽地列出浏览器当下已经实现、但较少人知道的特性，面向非技术读者，并标注各引擎的支持情况与版本号。清单涵盖 WebGPU、HTML-in-Canvas、WebAssembly 3.0、视图过渡与滚动动画、新 CSS 能力、端侧 AI、硬件外设、窗口捕获、身份与应用化等方向，还单列了 Safari 27.3、WebMCP、WebNN 等尚在 beta、源试用或 flag 阶段的能力，以及 Interop 2027 的候选议题；从中可以看出，浏览器正从页面渲染器扩展为图形、AI、设备与系统能力的统一平台。

- 🚀 **清单续作**：browser-2027 是 browser-2020 的续作，延续“今天浏览器已实现、但少有人知的特性”这一非穷尽清单定位，不面向技术受众，并为每项标注 Chrome、Safari、Firefox 的支持版本。
- 🎨 **WebGPU**：作为 WebGL 的继任者，WebGPU 支持现代 GPU 渲染和通用 GPU 计算，现已进入所有引擎，包括 iPhone 和 Vision Pro：Chrome 113、Safari 26、Firefox 141。Firefox 在 Windows 141、Apple Silicon Mac 147 上支持，尚未覆盖 Linux、Android 与 Intel Mac；Chrome on Android 从 121 起支持，Linux 从 144 起部分支持。
- 🧩 **HTML-in-Canvas**：这一能力可以把真实的、仍在运行的 HTML 绘制进 2D canvas，或 WebGL、WebGPU 纹理，同时让文字保持可选、表单保持可用、屏幕阅读器仍然能读到内容，因此终于能给 `div` 套上 shader。Chrome 157 已支持，WebKit 已在 flag 后实现，Firefox 尚无信号。
- 📦 **3D 与图像格式**：`<model>` 元素可以像 `<img>` 一样嵌入可交互 3D 模型，无需 JavaScript 和 WebGL，由 Safari 27 在 iPhone、iPad、Mac 和 Vision Pro 上支持。2023 年被 Chrome 移除的 JPEG XL 回归：文件更小，支持 HDR 与渐进加载，Chrome 155、Safari 17、Firefox 158 支持。
- 🌐 **WebXR 与空间体验**：WebXR 现在支持手部追踪、深度感知，以及墙面、地板、桌面的平面检测，覆盖 Chrome on Android、Android XR 头显与 Meta Quest Browser，iPhone 上仍无实现。在 Vision Pro 上，网站可以用自有 3D 环境替换周围房间，空间照片与 180°/360° 视频可原生播放（visionOS 27）。
- ⚡ **WebAssembly 3.0**：运行 C++、Rust、Kotlin、Dart、C# 代码可达接近原生速度，新增垃圾回收、超过 4GB 的内存（Memory64），以及从同步代码调用异步 Web API 的 JSPI。GC 与 JSPI 已在所有引擎中提供，Memory64 在 Chrome 133、Firefox 134 与 Safari 27.3 beta 中提供。
- 🔗 **媒体与传输**：WebCodecs 逐帧直接访问浏览器的音视频编解码器，是网页版视频编辑器的基础：Chrome 94、Safari 26（视频能力自 16.4 起）、Firefox 130 桌面。WebTransport 基于 HTTP/3 提供低延迟双向流，面向游戏与直播类场景，三大引擎均已支持，Safari 自 26.4 起。
- 🔄 **过渡与滚动动画**：View Transitions 无需框架即可在同一页面的两个状态或两个页面之间做形变动画：同页过渡自 2025 年 10 月起所有引擎支持，跨页过渡由 Chrome 126 与 Safari 18.2 支持，Chrome 147 可在多个元素上同时过渡。滚动驱动动画用纯 CSS 绑定滚动位置并脱离主线程运行；滚动触发动画由 Chrome 146 支持。
- 🎨 **CSS 布局与组件**：锚点定位已全引擎支持（Chrome 125、Safari 26、Firefox 147），可在元素将移出屏幕时自动翻转。约 30 年来首次可以完全自定义原生 `<select>`，包括在选项内放图片（Chrome 135、Safari 27、Firefox flag）。CSS carousels 由浏览器生成箭头与圆点（Chrome 135）。`interpolate-size: allow-keywords` 一行代码解决 `height: auto` 动画。圆角可为 squircle、内凹、缺口或斜切，`border-shape` 让边框跟随任意形状（Chrome 139/147）。Grid Lanes 提供瀑布流布局（Chrome flag、Safari 26.4、Firefox Nightly）。
- ⚙️ **可计算的 CSS**：CSS 新增 `if()` 条件、`@function` 自定义函数、`random()` 与用于错落效果的 `sibling-index()`。其中 `if()` 在 Chrome 137 与 Safari 27.3 beta，`@function` 在 Chrome 139 与 Safari 27.3 beta，`random()` 在 Safari 26.2、Chrome 156、Firefox 161 beta，`sibling-index()` 已全引擎支持。
- 🧠 **端侧 AI**：Prompt API 在浏览器内置语言模型，页面可传入文本、图像和音频，离线运行且不向服务器发送数据；Chrome 148 桌面支持，需约 22GB 可用磁盘，Mozilla 与 WebKit 均正式反对该 API。另有 Translator、Summarizer、Language Detector（Chrome 138 桌面）以及不离设备的端侧语音识别（Chrome 139、Firefox 160 桌面）。
- 💬 **被代理驱动的浏览器**：浏览器可被 AI 代理操控：Chrome 中的 Gemini 能代为点击完成任务，先在美国的付费层级提供；Safari 27 在 macOS 上提供 MCP server，让编码代理打开并检查页面。
- 🛠️ **硬件外设**：Web Serial 可连接 Arduino、3D 打印机等串口硬件，不再是 Chrome 独占或桌面独占（Firefox 151 桌面、Chrome on Android 148）；WebHID、WebUSB、Web Bluetooth、Web MIDI 可接 Stream Deck、手柄、合成器、心率带与灯带，Safari 反对全部，Firefox 仅支持 MIDI。手柄震动三大引擎均支持。可折叠屏可检测折叠状态与铰链分割位置（Chrome 132/138，折叠 iPhone 上 Safari 27.1 需 flag）。
- ⚙️ **设备状态与权限**：Screen Wake Lock 阻止屏幕变暗或休眠，已全引擎支持；Keyboard Lock 在全屏时捕获 Esc、Cmd-Tab 等系统按键（Safari 26.4）；Compute Pressure 报告 CPU 压力，便于提前降质（Chrome 125 桌面，152 增加 CPU 性能档）；权限元素 `<geolocation>`、`<camera>`、`<microphone>` 改为由浏览器绘制的按钮，点击时才请求授权（Chrome 144 至 153）。
- 💻 **窗口、捕获与文件**：Document Picture-in-Picture 提供可放任意 HTML 的置顶浮窗（Chrome 116、Firefox 151，均桌面）；Element Capture 只录制或串流页面中的单个元素（Chrome 132 桌面，141 起在 macOS 14.2+ 可捕获系统音频）；Window Management、EyeDropper、Local Font Access 目前仅 Chrome 桌面支持；File System Access 可原地读写文件或文件夹，Safari 与 Firefox 只提供按站点的私有文件系统 OPFS。
- 🔑 **应用、身份与导航**：在 iOS 26 上，任何加入主屏幕的站点都以独立应用打开，无需 manifest；Web Install API 在 Chrome 158 桌面支持。Declarative Web Push 无需 Service Worker（Safari 18.4 iOS、18.5 macOS）。Digital Credentials 可向手机钱包索取驾照或身份证（Chrome 141、Safari 26），Passkeys 全引擎支持。Speculation Rules 让浏览器在后台完整渲染下一页，实现即时点击；Text fragments 可链接到页面中的具体句子；Temporal 修复 JavaScript 的日期与时区（Chrome 144、Firefox 139、Safari 27.3 beta）。
- 🧪 **即将到来**：Safari 27.3（2026 年 11 月 16 日起 beta）是超大型版本，包含 CSS `if()`、`@function`、`corner-shape`、Temporal、WebAssembly Memory64 与 WebGPU subgroups，还提供 Adaptive Dark Mode。Spatial CSS 在 visionOS 27.3 以 flag 提供开发者预览。WebMCP 让页面向浏览器 AI 代理暴露自身工具（Chrome 149 至 162 源试用，WebKit 反对、Mozilla 中立）。Web Haptics 自 Chrome 156 起在 flag 后提供。HDR 2D canvas 与更精细的 canvas 文本度量计划随 Chrome 160（2027 年 1 月）推出。WebGPU bindless 在 flag 后提供，光线追踪仅为工作组提案。WebNN 仅在 Chrome 与 Edge 以 flag 提供。Safari 的 VP9-alpha 透明视频支持据称已进入 WebKit 主干，但尚未随正式版发布。Overscroll Areas 在 Chrome 157 至 162 源试用。
- 🗓️ **Interop 2027**：各浏览器厂商于 12 月选定下一年的共同优先事项，票数最高的提案是 `border-shape`、`moveBefore()`、Temporal、gamut mapping 与可定制 select，选择截止 2026 年 12 月 17 日。
- ⚠️ **仍未落地**：Web Coffee API 七年后仍未发布，covfefe 协议没有第二家实现者，WebKit 的立场是 oppose。

### [GitHub - luruke/browser-2020：2020 年你可以用浏览器做的事情 ☕️ · GitHub](https://github.com/luruke/browser-2020)

总结失败：模型未返回符合格式的摘要。

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q4_2&utm_content=primary)

Meticulous 是一款面向复杂代码库的自动化端到端视觉测试产品，核心是通过记录开发者及其代理在开发、预发和预览环境中的真实交互，由 AI 持续生成并演进覆盖全代码分支的测试套件，并在拉取请求阶段展示变更对既有工作流和边缘案例的影响；其确定性调度引擎和并行计算集群旨在消除 flaky、降低维护成本，让团队以代理写代码的速度交付无回归代码。

- 🧩 **录制与覆盖**：可通过可选 recorder script tag 接入本地开发、staging 和 preview 环境，记录用户及代理会话以增强覆盖率；也可仅依赖代理生成的会话，无需开发者额外投入。
- 🧠 **AI 演进测试**：AI 引擎跟踪实际执行的代码分支，持续生成视觉端到端测试套件，覆盖每条代码分支、用户流程和边缘案例；新功能出现时自动新增测试，过时测试自动移除。
- 🔍 **PR 影响预览**：每次 pull request 会收到评论，按边缘案例拆分展示对现有工作流和新功能行为的汇总影响；代理可看到类似视图，并在代码提交评审前迭代修改。
- ⚡ **确定性执行**：从 Chromium 层构建并采用确定性调度引擎，宣称是唯一消除 flakes 的测试工具，同时实现高速执行，经过复杂应用验证。
- 📈 **规模化并行**：测试在计算集群中高度并行化，可测试数千个屏幕，并在 120 秒内返回结果。
- 🔄 **兼容或替代**：可与现有测试套件组合使用，也可完全替换现有测试；测试随应用演进而自动更新，无需编写、修复或维护测试。
- 🔗 **框架集成**：提供 NextJS、React、Vue、Angular、Nuxt、SvelteKit 集成，通过 recorder script tag 或 @alwaysmeticulous/recorder-loader 在非生产环境启动录制。
- 🏢 **客户采用**：页面称已有超过 100 家组织使用，并引用 Dropbox、Notion、Engine 等工程负责人的评价，强调零维护、无 flakes 和作为开发流程护栏的价值。

### [Nudeps：类似打包器的导入，毫无包袱 • Lea Verou](https://lea.verou.me/blog/2026/nudeps/)

作者发布轻量构建工具 Nudeps，目标是实现 light-build 而非 no-build：继续用 `npm install` 管理依赖，并让浏览器通过裸标识符直接导入包，无需传统打包器。Nudeps 只处理依赖文件、不改用户代码，借助 import maps 与 JSPM 生成映射，可作为现有编译工具、静态站点生成器和 island 架构的补充，同时保留打包器在复杂场景中的位置。

- 🚀 **正式发布**：发布 Nudeps（可理解为 nude deps 或 new deps），定位为轻量构建工具：保留 `npm install` 管理依赖，在浏览器通过包名等裸标识符导入，无需打包器；目标不是取消构建，而是让构建更轻、可组合、非必需。
- 🧩 **核心机制**：利用已 Baseline Widely Available 的 import maps 支持裸标识符，底层用 JSPM 追踪依赖图并生成 import map；通过小脚本注入外部 import map，规避每页内联要求，并且只处理依赖文件，不改用户代码。
- ⚙️ **使用方式**：在项目目录运行 `npx nudeps install`，再在 HTML 中加入 `<script src="/importmap.js"></script>` 即可；之后 `npm install` 或 `npm uninstall` 会自动触发更新，无需 Nudeps watcher 或手动构建步骤。
- 📦 **产物结构**：把 `node_modules/` 中必要文件复制到可部署但不提交的 `client_modules/`，目录名包含版本号（如 `vue@3.5.45`）以提升去重和缓存粒度；生产环境可用 `prune` 仅保留实际使用的 specifier。
- 🔄 **安装钩子**：安装时把 Nudeps 写入 `devDependencies`，并在 `package.json` 增加 `dependencies` 与 `prepare` 脚本；前者在 npm 安装或卸载后重跑，后者让新克隆项目直接就绪。
- 🧪 **兼容范围**：支持 Vue、React（无 JSX 体验较差）、D3、gsap、Lit、Three.js 等运行时导入，也覆盖动态 `import()`、`import.meta.resolve()`、本地包、npm aliases、git 依赖和实验性 npm workspaces；CJS 包经小型 `require()` shim 可部分工作。
- 🎨 **非 JS 依赖**：Open Props、Bootstrap Icons 等可通过实际 URL 使用，并生成无版本 URL 的符号链接或重定向；但浏览器暂不支持通过 specifier 引入 CSS，这类包也不能再依赖其他包，除非自行打包。
- 🧠 **代理支持**：测试中 Claude 基本能理解 Nudeps，仅会做多余但无害的操作；项目加入 `SKILL.md` 后，按指示使用可消除这些误解。
- ⚠️ **限制与缺口**：不转换用户代码，JSX、TypeScript、Svelte 仍需编译工具；目前仅支持 npm，pnpm/yarn 在路线图；Worker 不支持 specifier；CJS 支持很实验性，依赖 `process.env` 等 Node API 的包需 stub 或单独打包，且尚无基准数据。
- 🔮 **后续计划**：后续重点是修 bug、补齐上述缺口、测试更多包以确认兼容性和发现边缘情况，并优先支持其他包管理器。

### [Web 依赖已经崩坏，我们能修复它们吗？• Lea Verou](https://lea.verou.me/blog/2026/web-deps/)

文章围绕 Web 平台缺少一等依赖管理展开：依赖复用本应像 Node.js 中 `npm install` 后直接 `import` 一样基础，但浏览器只提供 URL、specifier 与 import maps 等分散原语，迫使开发者依赖 Webpack、rollup、esbuild 等 bundler。作者认为 bundler 的性能优化和转译并非不可替代，真正的问题是依赖管理被外包且碎片化，导致使用第一个库就出现陡峭复杂度；现有 `node_modules` 路径、公共 CDN、import maps 等无构建方案均有安全、可组合性、传递依赖或维护性问题，因此呼吁在标准层面补齐 specifier、外部 import maps、客户端依赖部署和依赖图等能力。

- 🧩 **核心判断**：Bundler 常被归为性能优化工具，但它承担的性能优化、转译、依赖管理和调试增强中，只有依赖管理是几乎所有项目在首几行代码就会遇到的基础需求；需要复杂工具满足基础需求说明生态有问题。
- 📊 **使用与情绪**：State of JS 2024 显示 Webpack 被约九成开发者使用、认知度接近 100%，但依赖管理仍是第三大痛点；2026 年 3 月投票中 88% X 与 72% Mastodon 用户使用 bundler，三分之一 X 用户和一半 Mastodon 用户希望不用，17.6% X 与 40% Mastodon 受访者已跳过 bundler。
- ⚠️ **路径导入缺陷**：直接引用 `../node_modules/vue/dist/vue.esm-browser.js` 或复制到 `common/lib` 会部署冗余文件、带来安全风险，且多数 serverless 主机如 Netlify、Vercel 会在构建后移除 `node_modules`；更严重的是破坏传递依赖和封装，库无法知道使用方目录结构，htmx 因此选择不用依赖。
- 🔑 **Specifier 必要性**：specifier 如 `vue`、`lit` 是对 URL 的关键抽象，能解耦包位置、包内文件路径、版本和导入条件，并让传递依赖有稳定引用；任何要求手写路径并随依赖更新修改代码的方案都应视为不可行。
- 🌐 **公共 CDN 风险**：从 Unpkg、JSDelivr 或 esm.sh 导入看似零配置，但引入不受控域名的可执行代码，存在包或 CDN 被攻破、服务中断和本地开发依赖网络等问题；不锁定补丁版本或用 SRI 仍有风险，且 URL 导入容易让不同文件意外引入同一依赖的不同版本。
- 🛡️ **缓存优势消失**：公共 CDN 的跨站缓存收益自约 2020 年起被 double-keyed caching 取消，浏览器会按 origin 重新下载相同资源，以防止跨站计时泄漏；作者认为该权衡的带宽成本不公平地落在新兴市场用户身上。
- 📦 **Import maps 局限**：import maps 让浏览器使用 specifier，但当前主要是内联 HTML、需逐页包含且要映射每个传递依赖，违反 locality、composability、scalability；可用经典脚本在任何模块加载前通过 DOM 注入模拟外部 import map，JSPM 4.0 即如此，但仍需构建工具，生产不用 CDN 时受限。
- 🧪 **改进方向**：外部 import maps 可通过 `script type=importmap src` 原生支持，该能力原在规范中后因实现者兴趣不足移除，2022 年 WebKit 曾原型、WHATWG 议题后停滞；Firefox 尚未支持这些改进，已提议纳入 Interop 2027，Shopify 近期也推动了韧性改进。
- 🔄 **Specifier 全覆盖**：作者主张将 specifier 扩展到 JS 之外的 CSS 框架、图标、字体等资源，并修复 workers 与 `script type=module src=foo` 等场景；workers 场景受 `whatwg/html#10858` 停滞影响，可通过为各资源类型增加 ESM 式引用语法，或设计 `specifier:` URL scheme 统一引用并连接 specifier 与 URL。
- ⚙️ **轻量工具链**：import maps 不是完整方案但能减少工具重量；进一步可让 import maps 通过 JS API 或 import attribute 导入，甚至由 HTTP `Link` 头下发，使服务器像 gzip 一样透明处理映射，让脚本局部组合依赖图而非全局管理。
- 📦 **客户端依赖部署**：还需把 `node_modules` 的相关子集部署到公开 URL；可考虑在 `package.json` 中用 `clientDependencies` 显式标记客户端依赖乃至具体 exports，将检测与处理应用文件解耦，简单应用可手写，复杂应用交给工具。
- 🔍 **依赖图难题**：即使能标记客户端依赖并映射 specifier，仍需知道依赖间关系；当前靠解析大量 `package.json` 构建依赖图，在 Node.js 可接受，在浏览器因 HTTP 往返成本高不可行且未考虑 tree-shaking，作者倾向把该职责移到服务器侧，但更确定的是问题存在而非具体方案。
- 💬 **行动呼吁**：文章最后呼吁浏览器厂商、标准组织和开发者共同解决 Web 依赖管理，不是反对 bundler 存在，而是反对其成为获得一等依赖管理的唯一可行路径；问题不是编译而是碎片化。

### [没有提供可翻译的文章标题，只收到占位提示“One moment, please...”，请补充标题原文。](https://css-tricks.com/when-everything-has-changed/)

提供的正文仅包含“Loader Please wait while your request is being verified...”这一加载/验证提示，没有可用于整理的技术周刊内容，因此无法生成有事实依据的摘要。

- ⚠️ **内容缺失**：原文未包含产品、版本、功能或技术机制等信息，需提供完整正文后再整理摘要。

### [Firefox 161 开发者发行说明（稳定版） - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/161)

Firefox 161 Stable 于 2026 年 11 月 24 日发布，开发者侧新增 SVG referrerpolicy、CSS random() 与嵌套函数、HTTP 压缩字典传输、剪贴板自定义格式和 CSS Typed OM，并更新 WebTransport、Navigation API、WebRTC 与 WebDriver BiDi；HTML 和 JavaScript 无重要变化，附加组件开发也无重要变化，另有 6 项默认关闭的实验特性。

- 🚀 **正式发布**：Firefox 161 Stable 于 2026 年 11 月 24 日发布；HTML 与 JavaScript 无重要变化，附加组件开发也无重要变化。
- 🧩 **SVG 引用策略**：`<image>`、`<script>`、`<feImage>` 支持 `referrerpolicy` 属性及对应的 `SVGImageElement.referrerPolicy`、`SVGScriptElement.referrerPolicy`、`SVGFEImageElement.referrerPolicy`，用于控制通过 `href` 获取资源时 `Referer` 头的发送量，行为同 HTML 的 `img` 与 `script`。
- 🎨 **CSS random()**：新增 `random()` CSS 函数，可在指定范围内生成随机值并可选按步长限制取值；可选 `<random-key>` 让不同元素或属性的多个 `random()` 共享同一随机基值。
- 🎨 **CSS 嵌套函数**：`var()`、`attr()`、`env()` 的首个参数现在接受嵌套函数，例如 `var(attr(data-theme-prop type(<custom-ident>)))` 与 `env(var(--safe-area-block-start))`。
- ⚡ **压缩字典传输**：支持 Compression Dictionary Transport：服务器用 `Use-As-Dictionary` 标记字典响应，浏览器在匹配请求中通过 `Available-Dictionary` 列出已存字典，服务器可用 `Content-Encoding: dcb`（Brotli）或 `Content-Encoding: dcz`（Zstandard）压缩响应，显著减小版本间变化不大的资源（如 JavaScript bundle）体积。
- 🌐 **WebTransport 流预期**：`WebTransport` 新增 `anticipatedConcurrentIncomingUnidirectionalStreams` 和 `anticipatedConcurrentIncomingBidirectionalStreams` 属性，以及 `WebTransport()` 构造函数的对应 options，表示应用预期服务器同时打开的单向与双向入站流最大数量。
- 💬 **剪贴板自定义格式**：Clipboard API 通过 `Clipboard.write()` 与 `Clipboard.read()` 支持自定义剪贴板格式，格式为以 `web ` 为前缀的 MIME 类型（如 `web text/x-my-format`）；自定义格式仅能被与写入页面同源的页面读取。
- 🧭 **NavigationTransition.to**：`NavigationTransition.to` 返回正在进行导航的 `NavigationDestination`，使 `navigate` 事件处理器之外的代码（如 `navigateerror` 处理器）也能获知导航目标并报告失败导航。
- 🎨 **CSS Typed OM**：支持 CSS Typed Object Model API，脚本可通过 `Element.computedStyleMap()` 与 `HTMLElement.attributeStyleMap` 以带类型的 JavaScript 对象读写 CSS 值，而非仅字符串；`CSSColorValue`、`CSSRGB` 等颜色值接口在 Firefox 及其他浏览器均不支持。
- 🔄 **WebRTC 关键帧**：`RTCRtpSender.setParameters()` 新增可选 `setParameterOptions` 参数，可在修改 `active` 或 `scaleResolutionDownBy` 等发送编码参数的同一调用中要求编码器生成关键帧，接收端随后无需再请求关键帧。
- 🔄 **BiDi 参数与激活**：WebDriver BiDi 的 `script.callFunction` 在参数或 `this` 值包含未知 `type` 的本地值（含嵌套值）时返回 invalid argument 错误，而不再静默替换为 `undefined`；`script.evaluate` 与 `script.callFunction` 在 `userActivation: false` 时不再清除已有用户激活标志。
- 🐛 **BiDi 修复**：修复 `browsingContext.navigate` 与 `browsingContext.reload` 在上一文档仍加载时启动导航可能挂起或返回不正确错误；修复 `browsingContext.setViewport` 随会话时间推移变慢的性能问题；`network.continueRequest` 替换已有请求体时会更新 `Content-Length`，避免服务器收到截断或不完整请求体。
- 🧪 **margin-trim**：实验性 `margin-trim` 属性支持块容器，并在 Nightly 默认启用（`layout.css.margin-trim.enabled`）；它移除容器起始边、结束边或两边的子元素块轴外边距，同时保留相邻兄弟元素之间的外边距。
- 🧪 **跨文档视图过渡**：跨文档视图过渡在 Nightly 默认启用（`dom.viewTransitions.cross-document.enabled`），可用于为多页应用中同源页面之间的切换添加动画。
- 🧪 **渲染阻塞**：`<link>`、`<script>`、`<style>` 元素的 `blocking` 属性取 `render` 值时可在 Nightly 默认启用（`dom.element.blocking.enabled`），阻塞页面渲染直到标记的样式表加载完成或脚本执行完成，避免页面先以无样式或不完整状态出现。
- 🧪 **quotes match-parent**：`quotes` CSS 属性支持 `match-parent` 值，使元素使用与其父元素相同引号对集合中的引号；该特性在 Nightly 默认启用（`layout.css.quotes.match-parent.enabled`）。
- 🧪 **text-autospace-size**：新增 `text-autospace-size` 属性并在 Nightly 默认启用（`layout.css.text-autospace-size.enabled`），用于设置 `text-autospace` 在中日韩（CJK）与非 CJK 字符之间添加的间距大小。
- 🧪 **prefers-color-scheme**：`prefers-color-scheme` 媒体特性在 `meta` 元素以 `color-scheme` 指定单一配色方案时会反映该声明，便于按配色方案选择图片和视频并简化主题切换器；该特性在 Nightly 默认启用（`layout.css.prefers-color-scheme.meta-tag.enabled`）。

### [Web-Perf Wednesday 019 – Firefox 推出字典压缩 – CSS Wizardry](https://csswizardry.com/2026/11/web-perf-wednesday-019-firefox-ships-dictionary-compression/#firefox-ships-compression-dictionary-transport)

2026年11月25日的 Web-Perf Wednesday 019 聚焦 Firefox 161 支持 Compression Dictionary Transport：浏览器可把已持有的资源版本当作字典，让服务器只发送变化部分，从而缩小重复下载；同时 Prebid 修正 DOM 可见性回退测量，WebKit 为超大 will-change 合成层设内存上限并修复滚动与渲染问题，WPE 开始对隐藏视图节流。核心意义在于为重复资源传输提供新的渐进增强手段，但需要缓存、CORS、CDN 与发布节奏配合并实测收益。

- 🚀 **Firefox 161 发布**：Firefox 161 于 11 月 24 日发布并支持 Compression Dictionary Transport，可让 JavaScript、CSS、WebAssembly、HTML 等重复资源在版本相近时传输更小；但浏览器支持仍有限，MDN 将其标为实验性，应作为渐进增强而非新依赖。
- 🧩 **字典压缩机制**：首个响应通过 `Use-As-Dictionary` 声明可作字典；浏览器后续请求匹配资源时用 `Available-Dictionary` 发送字典哈希，并声明 `dcb`（Brotli）或 `dcz`（Zstandard），服务器据此返回基于浏览器已有字节压缩的响应；无合适字典时退回普通 Brotli、Zstandard 或 gzip。
- 📈 **收益与适用**：项目公布的历史测试中，周对周 YouTube 播放器 bundle 比仅用 Brotli 小 90%，较旧 CNN React bundle 小 63%，但这些是特定历史资源，不能直接预测所有 bundle；最适合大文件、频繁发布、高重复流量且版本间改动集小的资源，而一次性或每次重建的资源可复用内容少。
- ⚠️ **部署限制**：该标准要求安全上下文，字典与响应缓存新鲜度绑定；`no-store`、`no-cache`、`max-age=0, must-revalidate` 会阻止响应被用作字典，可缓存响应还需按 `Accept-Encoding` 和 `Available-Dictionary` 变化，跨源资源需要正确 CORS；发布节奏与缓存生命周期必须足够重叠，并确认 CDN 正确识别和转发新请求头。
- 🐛 **Prebid 修复**：Prebid 11.53.0 修复基于 DOM 的可见性回退测量：旧代码可能拒绝可见后代、错误处理单轴裁剪、漏掉 shadow root 内的裁剪与透明度，还可能把脱离文档的元素当作位于视口左上角；发布方在升级后看到数字变化，可能来自几何修正而非广告或布局变化，应先用带 overflow、shadow DOM、折叠槽和隐藏祖先的代表性版位验证。
- ⚙️ **WebKit 内存上限**：Safari Technology Preview 257 限制覆盖超大区域的 `will-change` 元素创建合成层，修复高内存占用；同时修复 60 Hz Mac 显示器上的滚动卡顿，以及受 Adaptive Dark Mode 滤镜影响的渐变密集页面渲染缓慢。该版本是预览软件，团队应记录全视口或长期 `will-change` 页面的内存与滚动表现，并移除不再服务于实际动画的声明；浏览器限制只是安全网，不会让不必要的图层提升免费。
- ⚡ **WPE 隐藏视图节流**：WebKit 的 WPE 移植版在视图隐藏时暂停 CSS 动画并节流 DOM 计时器，与 GTK 和 Cocoa 已有行为一致；WPEPlatform 已知视图是否映射，底层改动利用该状态停止隐藏内容全速运行。多 WebView 的嵌入式产品可减少仅一个视图可见时的 CPU 浪费，但应测试隐藏与恢复两个方向，确认时间敏感状态正确恢复；改动位于 WebKit 主分支，嵌入方需核对实际发布版本。

### [Ladybird 现已进入 Alpha 阶段 - Ladybird](https://ladybird.org/posts/alpha/)

Ladybird 浏览器于 2026 年 11 月 23 日进入 alpha 阶段，macOS 与 Linux 用户可直接下载体验。它的引擎完全从零自研，并非基于其他引擎的分支；浏览器本身功能朴素但可用。官方明确表示，目前它存在兼容性与崩溃问题，安全性也尚无保证；但会通过滚动通道持续推送自动更新，并公开征集漏洞报告和失效网站反馈。

- 🚀 **alpha 发布**：Ladybird 现已进入 alpha，提供 macOS 和 Linux 版本下载；浏览器主体功能朴素但可用，引擎为团队完全自研、并非其他引擎的 fork。
- ⚠️ **早期局限**：部分网站无法正常使用，浏览器偶尔会崩溃；用户可在浏览器内上报故障网站，崩溃后可先阅读崩溃报告再决定是否发送，具体说明见隐私政策。
- 🛡️ **安全态度**：官方明确表示，目前不对安全性作任何承诺，并称新浏览器被反复攻破是过程的一部分；欢迎安全研究者前来攻击，并按指定方式告知方法，以便加固 Ladybird。
- 🔄 **滚动更新**：alpha 采用滚动更新通道，会定期推送自动更新；此前用户必须从源码构建才能看到改进，如今可直接获得快速迭代的版本。
- 🧪 **测试支持**：支持 WebDriver 用于自动化测试，同时支持 Firefox DevTools 协议，方便网站开发者在自己站点上验证兼容性并反馈问题。

### [macOS 和 Linux 版下载 - Ladybird](https://ladybird.org/download/)

Ladybird 的下载页面面向处于 alpha 阶段的浏览器，集中提供 macOS 与 Linux 的获取、安装和问题反馈入口。页面列出磁盘映像、Flatpak、Ubuntu、Fedora 等安装方式，并说明 release 列表依赖 JavaScript，加载失败或不可用时可改用 release manifest 或从源码构建。

- 🚀 **Alpha 下载与反馈**：Ladybird 处于 alpha 阶段，下载页提供 macOS 和 Linux 版本；遇到 bug 或缺少功能可在 Ladybird 内或 GitHub 报告。
- 💻 **macOS 安装**：下载磁盘映像后打开，将 Ladybird 拖入 `Applications` 文件夹，再从 `Applications` 启动。
- 📦 **Linux 安装**：推荐使用 Flatpak，适用于大多数发行版；页面还提供 Ubuntu 版本选择、Fedora 及其他下载入口。
- ⚠️ **发布列表限制**：页面显示尚未发布 release，且最新 releases 列表需要 JavaScript 才能加载；未启用 JavaScript 时可从 `release manifest` 直接读取下载链接和校验和。
- 🔄 **加载失败回退**：下载列表无法加载时，页面提示检查连接并重载，也可改用从源码构建。

### [Ladybird的首个alpha版本发布](https://simonwillison.net/2026/Nov/23/ladybird/)

Ladybird 在 2026 年 11 月 23 日发布首个 alpha，首次让 macOS 和 Linux 用户无需自行编译即可安装这款自研浏览器；它自建 HTML 解析、CSS、布局、JavaScript 与 WebAssembly 等核心组件，并以多进程隔离运行标签页，同时大量借助 AI 编码代理快速提升 Web 平台兼容性。此次发布既展示了新浏览器引擎的进展，也明确了 alpha 阶段在兼容性、稳定性和安全性上的限制。

- 🚀 **首个 Alpha**：Ladybird 发布首个 alpha，提供 macOS 与 Linux 安装方式，用户不再需要自行编译；作者实测认为界面轻量、速度不错，多数尝试的网站可正常加载。
- 🧩 **自研核心**：浏览器自研 HTML 解析、CSS 引擎、布局、JavaScript 和 WebAssembly 等大部分关键组件，仅使用 HarfBuzz 做文字整形、Skia 做 2D 图形、ffmpeg 处理视频、SQLite 处理数据库类任务，其余来自 Ladybird 或 SerenityOS。
- 💻 **多进程隔离**：Ladybird 将不同标签页放在不同进程中；作者在一窗口开六个标签、另一窗口开一个标签后，进程树出现多个 WebContent 以及 Hub、RequestServer、Compositor、MediaServer、VideoDecoderServer 等独立进程，形成标签页隔离和共享服务并存的架构。
- 🧪 **兼容性实测**：作者成功运行视频压缩工具（ffmpeg 编译为 WebAssembly）、图片缩放工具和 Pyodide REPL；Datasette Lite 因 service worker 与 web worker 组合而失败，报错为 `undefined is not a function (evaluated from 'navigator.serviceWorker.startMessages')`，已提交 issue 并在源码中发现 FIXME。
- 🧠 **AI 编码代理**：项目今年大量使用编码代理：2026 年 2 月 23 日 Andreas Kling 称借助 Claude Code 和 Codex，在两周内将 LibJS 的部分 C++ 代码移植为 25,000 行 Rust；10 月又让代理针对 WPT 补齐缺失功能。
- ⚡ **十月跃升**：2026 年 10 月，Ladybird 将样式和布局移到独立线程、落地新的 JavaScript JIT，并用新的 Cranelift WebAssembly 引擎替换原有 C++ 实现，在 JetStream 3 WASM 基准上提升 7 倍；在约 225 万个子测试的 WPT 套件上新增 75,650 个通过项并超过 Safari，其中大部分增长集中在 10 月 22 日至 27 日，从约 212 万增至约 218 万，/css 增加约 3 万、/editing 增加约 1 万。
- ⚠️ **Alpha 限制**：官方称 alpha 阶段部分网站无法工作且偶尔崩溃，用户可从浏览器内报告坏站，崩溃后可查看并决定是否发送报告；官方不对当前安全性作承诺，公开邀请安全研究者攻击并反馈，以便加固。
- 🔍 **作者建议**：Simon Willison 不会用 Ladybird 登录 GitHub、Gmail 等敏感账户，但会保留用于匿名浏览和参与测试，并认为新浏览器引擎入局者带来的进展值得乐观。

### [获取失败](https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/)

无法总结：获取内容失败，状态码 403。

### [理解 CSS random() - Piccalilli](https://piccalil.li/blog/understanding-css-random/)

CSS 新增的 `random()` 函数允许在样式值中直接生成随机数，并通过随机种子与缓存键控制同一值在元素、属性、索引以及媒体查询和动画中的复用；Mat Marquis 借为边注生成轻微随机旋转的案例，演示默认作用域、显式 `property-scoped`/`element-scoped`、仅标识符的全局作用域以及仅供调试的 `fixed` 用法，并解释 CSS 声明式求值顺序导致的重复写法。

- 🧩 **基础语法**：`random(min, max)` 返回区间内的随机值，可选第三参数定义步长；`random(0px, 10px, 5px)` 只返回 0、5、10，作者用 `rotate(random(-2.5deg, 2.5deg))` 生成边注随机角度。
- 🔑 **种子与缓存键**：每次调用生成 0–1 的随机种子并据此计算值，如 `random(0px, 100px)` 在种子 .5 时得 50px、.25 时得 25px；同一缓存键对应同一种子，因此相同作用域内结果一致。
- 🎯 **默认作用域**：默认 `auto` 作用域绑定到单个元素、属性名和该属性值内 `random()` 调用的索引；不同 `.sidenote` 得到不同旋转，同一元素在媒体查询和 `@keyframes` 中重复相同调用可保持同一角度。
- ⚠️ **声明式重复**：CSS 不保证求值顺序，不能引用另一个 `random()` 的结果，因此媒体查询和 `@keyframes` 中需重复完整的 `random()` 调用；重复值让这些调用共享种子，而不依赖哪个先执行。
- 🔗 **显式缓存键**：第一个参数可写成 `--random-rotation auto` 或 `--random-key property-scoped`，由 `--` 标识符和作用域关键字组成一个参数；作用域关键字涵盖 `auto`、`property-scoped`、`property-index-scoped`、`element-scoped` 等，`auto` 只是给默认元素/属性/索引作用域加上可读标签。
- 🛠️ **属性级作用域**：`property-scoped` 把缓存键限定到属性而不区分索引，可使 `margin-block: random(property-scoped, 1rem, 5rem)` 的起止值相同；但它不再按元素隔离，匹配元素会共享同一值，可叠加 `element-scoped` 恢复按元素隔离。
- 🌐 **全局作用域**：只写 `--random-key` 而省略作用域会得到最广作用域：同一随机值可跨所有匹配元素、所有属性和索引复用，例如所有 `.sidenote` 的 `transform`、`border-width`、`font-size` 共用同一随机结果。
- 🧪 **固定种子**：`fixed` 用手动 0–1 基数固定种子，例如 `random(fixed 0.5, -2.5deg, 2.5deg)` 得 0deg，`random(fixed 0.5, 0deg, 20deg)` 得 10deg，`random(fixed 0.25, 0deg, 100deg)` 得 25deg；仅用于调试范围和效果，不应用于生产。
- 🎨 **边注实现**：边注由 Eleventy shortcode 解析 Markdown 并包成 `<aside class="sidenote">`，配合 grid、`animation-timeline: view()`、不同断点的 `scale()` 与随机 `rotate()` 制造轻微有机抖动；覆盖 `transform` 时必须重复 `rotate()` 以免旋转被撤销。
- 🔍 **自定义属性陷阱**：把 `random()` 存入自定义属性（如 `--random-margin: random(0px,10px)`）保存的是函数调用而非计算结果，每次通过 `var()` 使用都会重新求值。

### [2026年面向开发者的10个最佳HTML转PDF API](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/best-html-to-pdf-apis/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20261125)

文章比较 7 款 Docmosis Cloud 替代方案，核心背景是 Docmosis Cloud 按页计费，文档越长成本越高。对比维度包括模板语法、定价、托管方式和迁移工作量，并建议先筛选 1 到 2 个服务，用自己的模板测试后再切换。

- 🧩 **核心问题**：Docmosis Cloud 按页计费，因此文档越长，使用成本越高，这是寻找替代方案的主要动因。
- 🔍 **对比维度**：文章从模板语法、定价、托管方式和迁移工作量四个方面比较 7 款替代服务，帮助读者评估适配性与切换成本。
- ✅ **选型建议**：建议先筛选 1 到 2 个候选服务，用自有模板进行测试，确认效果后再正式迁移。

### [网页不再变重了吗？- Iron/Out](https://www.iron-out.io/blog/has-the-web-stopped-getting-heavier/)

HTTP Archive 对 2020 年 1 月至 2026 年 11 月页面重量的延长分析显示，移动端中位页面的 JavaScript 年增长已从 2022 年 11 月后约 70 kb 降至过去一年的 7 kb，4 月峰值 717 kb 后回落至 690 kb；但最重 10% 页面仍在增长，且约一半回落来自被测页面样本变化，作者强调目前只能描述趋势，不能证明与 AI 采用存在因果关系。

- 🚀 **增长近乎停滞**：截至2026年11月，移动端中位页面的JavaScript为690 kb，过去12个月仅增加7 kb；相比之下，2022年11月至2026年3月约为每年70 kb。4月峰值717 kb后下降3.9%，桌面端从803 kb降至756 kb；总页面重量中位从5月峰值2683 kb降至2617 kb。
- 🧩 **趋势拟合更新**：研究沿用Ethan Gardner的方法，对HTTP Archive 2020年1月至2026年3月的75个月数据以2022年11月为断点拟合两段直线，并延长8个月。若旧趋势延续，移动端中位页面今天应为747 kb，实际低57 kb；2022年11月以来的年增速由70 kb降至64 kb，原先的2.8倍加速变为2.5倍。
- 🔍 **样本换血影响**：HTTP Archive的页面清单来自Chrome UX Report且每月变化。用BigQuery原始抓取对比2026年4月和11月首页：整体中位下降27 kb（4.0%），其中两个月均被测量的1050万个页面下降14 kb（1.9%）；其余来自样本变化，510万个退出页面中位为551 kb，430万个新增页面中位为466 kb。因此标题跌幅约是既有页面实际减重的两倍。
- 📈 **重页面继续增长**：移动端90分位JavaScript从4月到11月增长2.3%至2138 kb，10月以2173 kb创纪录；75分位下降1.6%。桌面端中位下降5.9%，90分位增长2.0%。十分之一移动页面传输超过2 MB JavaScript，这一群体尚未见顶。
- 📦 **资源构成与文件数**：自2020年1月以来，移动端中位页面JavaScript增加297 kb，字体增加48 kb，CSS增加15 kb，HTML增加8 kb，图片减少35 kb。JavaScript请求数从19增至21，文件内字节增长76%，每文件约从21 kb增至33 kb，总请求数仍为69；当前690 kb仍比2020年多76%，文件数量几乎未变。
- ⚡ **等待时间改善有限**：在模拟中端手机和限速连接下，中位可交互时间从2020年1月的12.5秒降至2026年11月的11.8秒，近七年仅少0.7秒。真实用户移动端Core Web Vitals通过率从2020年1月的24%升至2026年10月的53%，但评估指标、设备和网络均已变化，不能作同口径比较；页面并未变轻，改善来自设备、网络、浏览器和针对性优化。
- 🧭 **因果仍不确定**：图表标注了Claude Opus 4.7、GPT-5.5、Gemini 3.5 Flash、Claude Sonnet 5、GPT-5.6、Claude Opus 5和Claude Opus 5.5等发布，但2025年中位增长期发布同样频繁，时间点无法单独归因。数据既不能证明AI写了额外代码，也不能用平台期证明相反结论；7个月序列过短，样本更替也说明中位数容易因非建站因素移动。
- 🗓️ **后续复测**：作者计划在春季重跑这项分析，以确认增长停滞是否持续。

### [请稍候……](https://css-tricks.com/beyond-12-columns/)

提供的正文只是加载或人机验证页面，其中包含 Loader 以及 Please wait while your request is being verified... 等提示文本，没有任何可整理的文章内容，因此无法提炼事件、版本或技术细节；需要补充实际文章正文后，才能生成技术周刊摘要。

- ⚠️ **正文不可用**：所给资料是页面加载与请求验证提示，不含标题、正文、产品或版本信息，无法据此总结主题与核心变化。
- 🔍 **待补充内容**：请提供完整的文章正文（含发布方、版本号、功能说明与限制等），以便按要点提炼有价值的技术细节。

### [玩转 CSS Layers | Kitty Giraudel](https://kittygiraudel.com/2026/11/01/playing-with-css-layers/)

2022年 Miriam Suzanne 已为 CSS-Tricks 写过 Cascade Layers 指南，但作者直到2026年末才首次认真研究 CSS 层，并在个人网站上实验性落地：用 `@layer` 按从弱到强建立样式层，将层顺序与 CSS 目录结构对齐，并处理第三方样式无法直接通过 `<link>` 指定层的问题，最终减少了部分特异性 hack 与 `!important`。

- 🧩 **分层机制**：用 `@layer` 定义样式“桶”及从弱到强的顺序；层内仍按选择器特异性计算，但层间不比较特异性，因此较强层里的 `p` 可压过较弱层里的 `#foo .bar.baz`。
- ⚙️ **站点分层**：作者按目录设置 `base`、`layout`、`components`、`pages`，并在最前加 `vendors`、最后加 `helpers`；在最先且全局加载的 `base/base.css` 顶部声明 `@layer vendors, base, layout, components, pages, helpers;`。
- 🛠️ **落地方式**：逐个样式表把内容包进与所在目录对应的 `@layer`；`base/helpers.css` 放入最高层 `helpers`，使 `NoPrint`、`VisuallyHidden` 等工具类始终优先。
- 🔗 **第三方样式**：目前无法直接给 `<link>` 指定层，给 `<link>` 增加 `layer` 属性的提案尚未实现；作者将 charts 等第三方样式改为用 `<style>` 包裹 `@import url(/css/vendors/charts.css) layer(vendors)`。
- 🔍 **关键细节**：层可嵌套，对本站过于复杂；未分层样式优先于已分层样式；可用 `revert-layer` 撤销当前层内应用的样式。
- 🌐 **兼容性**：CSS layers 全球浏览器支持约 97%；理论上可用 `@supports at-rule(@layer)` 检测，但 `@supports at-rule()` 本身支持更差，所以作者提醒不要这么做。
- ✅ **清理效果**：分层设置完成后，作者移除了若干特异性 hack 和 `!important` 标记；数量不算多，但基本都能借层机制清理掉。

### [压缩侧边栏的忧郁 – Master.dev Blog](https://blog.master.dev/the-compacting-sidebar-blues/)

Chris Coyier 的文章讨论了一个常见布局难题：当视口高度较矮时，应用侧边栏的导航项放不下，从而被迫出现内部滚动条；此时可以通过隐藏文字标签来压缩导航。文章先后尝试了滚动状态查询、魔法数字加尺寸容器查询，最后用 CSS 自定义属性配合 style query 比较 `--sidebar-h` 与 `--limit`，在不触发无限循环的前提下实现断点，并说明了浏览器支持现状。

- 🎯 **问题与目标**：侧边栏导航项过高时会触发内部滚动，对导航这种重要元素来说体验较差；目标是在高度不足时收起文字标签，只保留图标，并且不破坏可访问性（使用 `aria-label`，或用裁切方式隐藏而不是 `display: none`）。
- ⚠️ **滚动状态查询的陷阱**：用 `container-type: scroll-state` 配合 `@container sidebar scroll-state(scrollable: y)` 在出现滚动条时压缩样式，会形成无限循环：压缩后不再滚动，样式回退又导致溢出，Chrome 中表现为持续抖动。
- ⚙️ **魔法数字方案**：给侧边栏设置 `height: 100svb`、`container-type: size`，再用 `@container sidebar-height (height < 500px)` 隐藏标签。该数值来自截图测量，导航项数量、字体渲染、间距或图标尺寸变化后即失效。
- 🧩 **用 calc 和 sibling-count 精确计算**：把内边距 `8px`、图标 `23px`、图文间距 `6px`、文字高度 `14px` 相加后乘以 `sibling-count()`，再加上容器上下内边距，得到更贴近实际的 `--limit`；文字高度仍是唯一的魔法数字，用 `0.6lh` 替代同样属于估算。计算中混入 `<hr>` 等额外元素会让 `sibling-count()` 失准。
- 🔑 **自定义属性不能直接进容器查询**：`var()` 按元素解析，`@container ... (height < var(--navItemHeight))` 无法生效；而且允许这样做还可能引发“查询命中、属性变化、查询失效”的循环。需先用 `@property` 把 `--sidebar-h` 和 `--limit` 注册为 `<length>`。
- ✅ **Style Query 解法**：在 `.sidebar-inside` 上设 `--sidebar-h: 100cqh`，在 `.nav-item` 上设 `container-name: nav-item` 与计算出的 `--limit`，再用 `@container nav-item style(--sidebar-h < --limit)` 隐藏 `.nav-label`。因为 `--limit` 由不变化的常量算出，所以不会陷入循环。
- 🌐 **浏览器支持**：该方案在 Chrome 142+ 和 Firefox 154+ 可用，Safari 尚不支持 style query 的范围语法，因此会保留标签，但不会导致布局损坏。

### [AI 加速了构建：无障碍测试如何跟上？— Smashing Magazine](https://www.smashingmagazine.com/2026/11/ai-sped-up-build-how-can-accessibility-testing-keep-up/)

Level Access 的 2026 State of Digital Accessibility Report 基于 2500 多名从业者的调查指出，AI 已明显加速规划、设计和开发，但 QA 与测试没有同步提速，形成“双速工作流”；WebAIM 数据还显示首页自动检测错误同比上升。文章主张把人工判断嵌入发现、修复和举证三个环节，并让 AI 在成熟实践和护栏下放大效能。

- 📊 **调查结果**：2500 多名专业人士中，58% 认为 AI 加速了规划，61% 认为加速了设计，51% 认为加速了开发，但仅 30% 认为加速了 QA 与测试，形成构建快、验证慢的双速工作流。
- 📈 **错误上升**：WebAIM 对前 100 万首页的扫描显示，每页自动检测错误一年内从 51 个升至 56.1 个，增长 10.1%，并将 AI 辅助编码列为可能因素之一。
- 🧠 **成熟度差异**：在各项无障碍指标上持续改善的组织中，AI 采用率并非最大差异；训练、沟通和无障碍文化等实践成熟度更关键。调查仅为相关性，成熟项目也可能更善于记录成果。
- 🎯 **AI 放大器**：成熟无障碍项目中的受访者认为 AI 帮助排定问题优先级的可能性接近 6 倍，认为 AI 帮助在开发中更主动处理无障碍的可能性接近 3 倍；AI 更适合放大已有上下文、测试、环境和护栏。
- 🔍 **交接前移**：把人工检查点前移到交接和 PR：在交接中明确焦点顺序、可访问名称、状态、标题结构和变更播报，并写入设计系统组件、Cursor rules、AGENTS.md、Copilot instructions 和提示模板；GitHub Annotation Toolkit 可把意图标注在 Figma 画布上。
- 🛡️ **PR 门禁**：在 CI/CD 与 PR 中运行检查，按基线只审查变更，可阻止或警告合并；eslint-plugin-jsx-a11y 在提交前标记 React 问题，Pa11y 和 Lighthouse CI 扫描构建，Level CI 提供预合并检测、增量发现、质量门禁和 PR 修复建议。
- 🧪 **自动扫描与人审**：QualWeb 可按 W3C ACT 规则检查页面、屏幕和文档；同时使用 axe-core 和 Equal Access 等多引擎可互补发现。自动化适合广度覆盖，但键盘可达性、子菜单可用性等仍需人工评估。
- 💻 **责任分工**：设计师明确焦点、错误和状态；开发对自定义组件做键盘检查和屏幕阅读器冒烟测试，屏幕阅读器测试可能需要入门培训；UX/QA 走完整旅程；把无障碍指标纳入验收标准和完成定义，并用组件级测试兜底。
- 🛠️ **修复闭环**：问题票据应带元素、复现步骤、相关 WCAG 条款、建议修复和 PR 链接；在编辑器、设计文件或组件库提供指引，MCP server 可把发现和修复建议接入 Cursor、Claude 等助手；旧 backlog 先处理阻断关键旅程的问题，再优先快速修复。
- ⚠️ **绿测陷阱**：AI 编码助手倾向让检查通过而非保证体验正确，其输出只能当草稿；给具体修复指引并用 Awesome Copilot 的 accessibility instructions file 约束，重跑检查后还要合并前在上下文中审查语义、测试行为。绿色结果可能来自 div 上加 role="button"、冗余 ARIA 或编造 alt 文本。
- ✅ **证据留存**：让 AI 随修复写回归测试，把发现链接和判断写入 PR；通过测试只证明已知问题未回归，还需注明测试内容、所用辅助技术和判断。工具可自动汇总证据，Level Access Reporting Agent 将 VPAT/ACR 编写时间缩短 70% 以上，但前提是证据已存在，工具只放大实践。

### [JavaScript 迎来一套新的 HTML 插入 API — Amit Merchant — A blog on PHP, JavaScript, and more](https://www.amitmerchant.com/javascript-gets-a-new-set-of-html-insertion-apis/)

Chrome（及 Edge）正在推进一组更一致的 JavaScript HTML 插入与流式 API，用 setHTML()、appendHTML()、prependHTML()、beforeHTML()、afterHTML()、replaceWithHTML() 等具名方法替代 insertAdjacentHTML() 的位置字符串，并为每个插入方法提供流式变体；常规方法默认调用浏览器清理器，Unsafe 变体可关闭默认清理并通过 runScripts 控制脚本执行。该能力属于 Chrome 的 Declarative Partial Updates 工作并进入 HTML 平台，但当前主要存在于较新的 Chromium 版本，跨浏览器使用需特性检测或 html-setters-polyfill，且 polyfill 不还原原生流式行为。

- 🚀 **具名插入方法**：提供 setHTML()、appendHTML()、prependHTML()、beforeHTML()、afterHTML()、replaceWithHTML() 六个方法，分别对应替换内容、追加末尾、插入开头、插到元素前或后以及替换元素；相比 insertAdjacentHTML() 的 beforeend 等位置参数，方法名直接表达操作意图。
- 🧩 **默认清理**：常规插入方法使用浏览器默认 HTML 清理规则，插入前移除 script 等被认为不安全的元素；也可传入自定义 Sanitizer，例如 new Sanitizer({elements:['em','i','b','strong']}) 仅保留指定元素。
- ⚠️ **Unsafe 变体**：每个插入方法都有 Unsafe 版本，如 setHTMLUnsafe()、appendHTMLUnsafe()；它们不自动应用默认清理器，可接收自定义 Sanitizer，并支持可选 runScripts，默认 false，设为 true 时会执行标记中的脚本，应仅用于可信来源。
- 🔄 **流式插入**：每个常规方法都有对应流式版本：streamHTML()、streamAppendHTML()、streamPrependHTML()、streamBeforeHTML()、streamAfterHTML()、streamReplaceWithHTML()，可将响应文本流直接管道到元素并在到达时增量处理，而不必等待完整响应。
- 💻 **管道用法**：示例包括 response.textStream().pipeTo(container.streamAppendHTML())，或在需要更多控制时使用 response.body.pipeThrough(new TextDecoderStream()).pipeTo(container.streamAppendHTML())；也提供 streamAppendHTMLUnsafe() 等流式 Unsafe 变体。
- 🌐 **浏览器支持**：这些 API 属于 Chrome 的 Declarative Partial Updates 工作并进入 HTML 平台，已出现在较新的 Chromium 版本，但尚未获所有浏览器支持；可用 'appendHTML' in Element.prototype 做特性检测，不支持时回退到 insertAdjacentHTML()。
- 📦 **Polyfill 限制**：Chrome 发布 html-setters-polyfill 以便在不支持原生 API 的浏览器中使用相同 API 形状，但它不复制原生流式行为，而是缓冲完整内容后再应用，因此只对常规插入的兼容性有帮助。
- 🎯 **设计意义**：新 API 让追加、替换或流式插入的意图仅凭方法名即可判断，提升常见前端 DOM 操作的一致性和可读性；流式能力尤其把 HTML 的流式特性带到 JavaScript 插入内容中。

### [使用现代 CSS 创建示意图和图表 – Master.dev Blog](https://blog.master.dev/creating-diagrams-and-graphs-using-modern-css/)

文章继续探讨仅用现代 CSS 绘制图表与连接线的实验：利用 anchor positioning、border-shape、shape() 和 if() 等特性，在元素间生成随位置变化或固定边侧连接的曲线，并通过四区域切换与连续性设计让多条形状看起来像一条完整连线。这些示例目前主要面向概念验证和趣味演示，尚未适合生产。

- 🎯 **动态连接**：连接线根据两个元素的位置和形状选择最近边侧；元素过近时改为连接中心。示例用 `hypot(100cqw,100cqh)` 计算伪元素对角线，以 `style()` 条件在 `if()` 中选择不同 `shape()`，但部分形状需要知道元素尺寸（示例中为 `60px`）。
- 🔄 **静态连接**：固定连接同一边侧，不随元素位置改变，例如右到左连接；优点是无需知道元素尺寸，但失去部分对称性，需要针对四个锚点区域分别配置，并让相邻区域的曲线在切换时保持连续。
- 🧩 **条件与连续性**：通过调整锚点定位配置覆盖不同区域，并利用 `if()`/`style()` 条件切换形状；可在 `shape()` 内嵌 `if()` 只改变一个控制值，例如垂直距离小于 `100px` 时把曲线改成直线，从而减少代码并保持视觉连续。
- 🛠️ **进阶实验**：文章展示直线在元素靠近时弯曲、元素过远时拉长变细，以及 zig-zag、双 zig-zag、spring 连接等趣味示例；其中 zig-zag 不够稳健，过度拉伸可能失效，spring 连接则更耐用。
- ⚠️ **支持与定位**：写作时只有 Chrome 和 Edge 完全支持所用特性；这些实现是探索 CSS 能力的实验和概念验证，尚不适合生产，但有助于理解 anchor positioning、`shape()`、`border-shape`、`if()` 等未来可用的 CSS 功能。

### [Button Sounds — 为你的 UI 打造的触感音效](https://buttons.joshwcomeau.com/)

本次请求未提供可整理的文章正文，因此无法确认事件、版本、功能机制或影响范围，也不能生成符合要求的技术周刊摘要。

- ⚠️ **缺少正文**：请补充文章正文后再生成；当前没有足够信息可提取发布内容、核心机制、限制或示例。

### [button-sounds - npmx](https://npmx.dev/package/button-sounds)

`button-sounds` 1.0.0 发布，提供 50+ 段专业录制的按钮点击与切换音效，并同时以原始音频文件和 npm 库形式服务 JavaScript 与 React 项目；其核心是用多采样随机播放降低重复感，同时在文档中给出音量、静音和浏览器自动播放限制等实践建议。

- 🚀 **发布内容**：`button-sounds` 1.0.0 已发布，MIT 许可，面向需要按钮点击与切换音效的 Web 和 React 开发者，提供 50+ 段专业录制的音效。
- 🧩 **核心机制**：每个音效不是单一 one-shot，而是录制数十个样本并保留若干可用版本，触发时随机选取一个；连续点击时会略有差异，减少机械重复感。
- 🎨 **音频规格**：声音在同一经过声学处理的房间用 Zoom H4 录制，并在 Adobe Audition 中进一步降噪；提供 48kHz `.wav` 和 192kbps MP3，均为立体声。
- 📦 **安装与依赖**：可通过 `npm install button-sounds` 安装；同一包服务 vanilla JavaScript 与 React bindings，Node.js 要求 >=18，依赖 `howler` ^2.2.4，`react` 和 `react-dom` 为可选 peer dependency（>=18），安装大小 9.2 MB。
- 💻 **按需打包**：React bindings 只有在代码中实际 import 时才会被 bundler 打包，现代 bundler 会移除未使用模块，避免 vanilla 用户额外引入 React 相关代码。
- 🛠️ **自托管**：若不想依赖 CDN 上的 MP3，可参考专门文档自托管音频文件；使用说明按 vanilla JS 和 React 分开，原始音频文件也面向非 JavaScript 场景。
- ♿ **用户偏好**：目前没有类似 `prefers-reduced-motion` 的显式声音偏好；建议以最大音量 25% 到 50% 播放，并提供静音开关，示例是博客右上角、明暗切换旁的 mute button。
- ⚠️ **自动播放限制**：浏览器的 media engagement index 会跟踪用户与站点的互动并计算信任度，具体启发式因浏览器而异且不断变化，因此无法保证音效 100% 触发；按钮音效被视为 nice-to-have，偶尔不播放可接受。

### [适用于任意规模时间序列工作负载的 Postgres | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter&utm_content=sponsored-chartquery-1125)

Tiger Data 展示 Tiger Cloud 面向任意规模时序工作负载的托管 Postgres 能力，强调单个服务可达每天 3 万亿指标、3 PB 数据和 1 quadrillion 数据点，并通过计算存储分离、副本集、跨可用区高可用、企业级合规与可观测性，降低时序数据库的扩缩容和运维成本。

- 🚀 **规模指标**：页面称单个 Tiger Cloud 服务可达每天 3 万亿指标、3 PB 数据和 1 quadrillion 数据点，用真实规模说明时序工作负载承载能力。
- 💻 **副本与存储**：通过最多 10 节点的副本集分离读写，并用 SSD/S3 分层存储实现低成本、可扩展的存储。
- ⚙️ **计算存储分离**：计算与存储分离，可独立扩缩容，避免为闲置容量付费，并分别优化成本和性能。
- 🛡️ **高可用**：多可用区集群支持自动故障转移、时间点恢复和跨区域备份。
- 🏢 **企业合规**：提供 SOC 2、HIPAA、GDPR 合规，常开加密、SSO、RBAC 和审计日志。
- 📊 **可观测性**：查询下钻和仪表盘提供性能与错误可见性，可将指标发送到 CloudWatch、Datadog、Prometheus。
- ⚡ **快速开通**：可在数分钟内开通数据库，并通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔗 **生态集成**：支持与首选云厂商及更广泛的 Postgres 生态集成。
- ✅ **企业支持**：企业方案包含合同化正常运行时间 SLA、区域数据隔离和合规认证，并提供 24/7 全球 Postgres 专家支持及企业响应时间保障。
- 💡 **试用优惠**：新账户可获得 1000 美元额度，30 天内有效，无需信用卡。

### [Alloy CSS | 一份样式表，搞定服务端渲染的 HTML](https://alloyhtml.com/)

Alloy CSS 发布 v1：它是一份面向服务端渲染 HTML 的样式表，采用 MIT 许可证、免费开源，不需要构建步骤，也不依赖 JavaScript 就能驱动对话框、菜单、抽屉、标签页和 Toast；它同时声称可为 Rails、Django、Laravel、htmx 以及 React、Vue 或单个 HTML 文件提供同一套类名，并附带面向 AI 生成代码的类名清单与校验工具，以及一套 82 页的付费模板。

- 🚀 **发布与定位**：Alloy CSS 以 `@alloyhtml/css@1` 发布，MIT 许可、免费开源，只需一行 `<link>` 引入 `https://cdn.jsdelivr.net/npm/@alloyhtml/css@1/dist/alloy.min.css`，没有构建步骤；示例 `example.html` 就是单个 HTML 文件加一份样式表、零脚本。
- 🧩 **无脚本交互**：对话框由 `<dialog>` 和命名它的按钮组成，菜单使用 popover，关闭不依赖脚本；官方示例中的菜单、标记发票已付的开关、Toast 和对话框均可实际点击，因此不存在需要加载、损坏或持续维护的脚本。
- 🌐 **框架与场景适配**：官方称它适用于 Rails、Django、Laravel 和 htmx，也同样适用于 React、Vue 或单个纯 HTML 文件，核心使用方式是让服务端渲染的 HTML 直接套用固定类名。
- 🎨 **暗色主题**：随包提供两套暗色主题，只需在引入套件后再加一个 `<link>`，并用 `media="(prefers-color-scheme: dark)"` 跟随访客设备；品牌色与字体同样只需一个小文件即可覆盖。
- 🧠 **面向 AI 生成**：官方提供 `alloyhtml.com/llms.txt` 作为提示入口，可用 `npx @alloyhtml/css skill` 在 Claude Code 中为整个项目保留技能；`npx @alloyhtml/css check app/` 会检出 AI 凭空写出的类，例如 `.mt-4`、`.btn`、`.btn-primary`，并提示改用套件类名或通过 `--css` 传入自定义样式表。
- 🧪 **兼容性验证**：在关闭 JavaScript 的 Chromium、Firefox 和 WebKit 中，按手机与桌面宽度测试；支持 Chrome 和 Edge 135、Firefox 144、Safari 26.2 及更新版本。
- 📦 **配套模板**：Alloy Templates 提供 9 类应用（商店、博客、招聘门户、医疗等）共 82 个页面，这些页面使用同一套 CSS、纯 HTML，一次性收费 29 美元；官方页面同时列出 Basketry、Seller Centre、Quiet Side、Studyhall、The Harbour Courier、Cedar Health、StagePass、Hireline、Wayboard 等 9 个演示产品。

### [GitHub - ngxson/wllama：llama.cpp 的 WebAssembly 绑定 - 支持浏览器内 LLM 推理 · GitHub](https://github.com/ngxson/wllama)

wllama 是 llama.cpp 的 WebAssembly 绑定，让 LLM 推理直接在浏览器内运行；V4 发布宣称最高 2.8 倍提速，不再要求预分割模型，并加入推测解码和 LoRA 适配器支持，同时覆盖 WebGPU、多模态、语音与实时音频等能力。

- 🚀 **V4 发布**：V4 宣称最高 2.8 倍提速，不再要求预分割模型，并支持推测解码与 LoRA 适配器；兼容性问题可参考 `@wllama/wllama-compat`。
- 🧩 **浏览器推理**：基于 WebAssembly SIMD 在浏览器内执行推理，无需后端或 GPU；推理在 worker 中运行以免阻塞 UI，并根据浏览器支持自动切换单线程或多线程构建，模型缓存在 OPFS 以支持快速加载、多连接下载和断点续传。
- 🌐 **WebGPU 支持**：WebGPU 自动启用，默认将所有层 offload 到 GPU；可通过 `LoadModelParams.n_gpu_layers` 调整 GPU 层数，设为 0 禁用 GPU，未放入 GPU 的层由 CPU 运行；该支持由 PR #215 引入。
- 📦 **GGUF 加载**：可直接加载单个 GGUF 文件，即使超过 4GB 也无需预分割；已用 `llama-gguf-split` 分割的模型仍受支持，传入首个分片即可自动加载全部块，`parallelDownloads` 默认 3。推荐 Q4、Q5 或 Q6 量化，不建议使用 IQ（含 imatrix），可能推理慢且质量低。
- 🧠 **模型能力**：提供完整类型定义的 OpenAI 兼容 API，并支持图像、音频和视频多模态输入、工具调用、推测解码（MTP、DFlash、DSpark、Eagle3）以及 LoRA 适配器。
- 🎨 **语音接口**：`createSpeech` 可做文本转语音并返回 WAV，`stream: true` 时按块返回；`createTranscription` 转写音频。相关 API 需要支持音频的模型及 mmproj 文件，例如 `LFM3-Omni`，可用 `getLoadedContextInfo()` 查看 `has_audio_input`、`has_audio_output`、`has_audio_stream`、`has_live_asr`、`has_audio_duplex`、`audio_voices` 等能力。
- 💬 **实时音频**：实时会话使用与 OpenAI realtime API 和 llama-server `/v1/realtime` 相同事件；会话在 `close()` 前占用一个 slot，只有读取 `events()` 时推理才运行。支持默认对话、`type: 'transcription'` 转写、`intent: 'transcription'` 实时 ASR，以及面向 `has_audio_duplex` 模型（如 Hibiki 法译英）的全双工模式：首段音频开启响应，每 80 ms 输入产生 80 ms 输出音频及翻译文本，`response.cancel` 结束响应；实时 ASR 需要 `has_live_asr`，`LFM3-Omni` 不具备。
- ⚠️ **限制条件**：多线程需设置 `Cross-Origin-Embedder-Policy` 和 `Cross-Origin-Opener-Policy` 响应头；单个 wasm 实例内存上限为 4GB，超出部分会拆分到多个 worker 的 wasm 实例（`rpc_workers`，默认自动），此模式需要多线程及 JSPI 或 compat 构建，较旧且无 JSPI 的 Firefox 无法加载这类模型，单线程则会加载失败并报错。
- 🛠️ **包与构建**：npm 包 `@wllama/wllama` 提供预构建 wasm；本仓库不附带二进制，需要 Docker 执行 `npm run build:wasm` 和 `npm run build`，也可从 CDN 加载 wasm 文件但不推荐。

### [Wllama - 由 ngxson 制作的 Hugging Face Space](https://huggingface.co/spaces/ngxson/wllama)

总结失败：模型未返回符合格式的摘要。

### [GitHub - github/relative-time-element：标准 \<time\> 元素的 Web 组件扩展。· GitHub](https://github.com/github/relative-time-element)

GitHub 的 `relative-time-element` 通过 Web Component 形式扩展标准 `<time>` 元素，把服务端缓存的 ISO 8601 时间戳在浏览器端本地化为用户所在时区和语言，并按相对时间自动更新；无 JavaScript 时仍显示缓存的后备文本，兼顾 HTML 片段缓存、本地化与渐进增强。

- 🧩 **核心机制**：使用 `<relative-time datetime='2014-04-01T16:30:00-08:00'>April 1, 2014</relative-time>`：`datetime` 必须是 ISO 8601，元素文本提供默认日期；浏览器加载自定义元素后，用 `Intl.DateTimeFormat` 和 `Intl.RelativeTimeFormat` 按用户偏好替换为本地时区/格式。
- 📦 **npm 包**：包名为 `@github/relative-time-element`，可通过 `npm install @github/relative-time-element` 安装；依赖 `Intl.DateTimeFormat` 与 `Intl.RelativeTimeFormat`，旧浏览器需为自定义元素及这两个 Intl API 引入 polyfill。
- 🎯 **格式模式**：`format` 支持 `datetime`、`relative`、`duration`；默认 `auto` 是 `relative` 的别名，后续主版本将改为 `relative`。`elapsed`、`auto`、`micro` 已弃用，分别建议迁移到 `duration formatStyle=narrow`、`relative`、`relative`（可配 `formatStyle=narrow`）。
- 🔄 **相对时间与阈值**：`relative` 按距当前时间输出 `in 20 days`、`20 days ago`、`now` 等，超过 `threshold`（默认 `P30D`，即 30 天）后转为绝对日期并可用 `prefix`（默认 `on`）加前缀；该阈值仅在 `format=relative/auto` 且 `tense=auto` 时生效。
- 🧪 **duration 显示**：`duration` 按年、月、周、天、小时、分钟、秒倒数或计时，默认省略值为 0 的单位；其渲染使用 `font-variant-numeric: tabular-nums` 保持数字等宽，避免计时器跳动，可通过 `relative-time::part(root)` 覆盖。
- 🗓️ **时区与语言**：`time-zone` 接受 IANA 时区名（如 `America/New_York`），未设置时沿 DOM 向上继承最近祖先，否则用浏览器默认时区；`lang` 同样向上继承，最终默认 `en`，并传给 `Intl` API。
- ⚙️ **关键属性**：支持 `datetime`/`date` 设置其一覆盖另一个、`tense`（`auto`/`past`/`future`）、`precision`（默认 `second`）、`formatStyle`（`long`/`short`/`narrow`），以及 `second`、`minute`、`hour`、`weekday`、`day`、`month`、`year`、`time-zone-name` 等传给 `Intl.DateTimeFormat` 的字段；`no-title` 可移除 `title`。
- 🎨 **compact 绝对时间**：`absolute-format=compact` 会在显示绝对时间戳时压缩文本，适用于显式 `format=datetime`、超出阈值或 `data-prefers-absolute-time` 选择的绝对输出；今天显示为 `today at 3:04 PM`，其他日期显示为 `Nov 2, 2026`，不显示时区名，并覆盖部分可见文本的格式属性但不改变完整 title。
- ♿ **可访问性**：元素在 Shadow DOM 的 `span[part=root]` 中渲染，可用 `::part(root)` 定制样式；`title` 对屏幕阅读器和键盘用户不可访问，添加 `no-title` 便于自行实现可访问 tooltip；`micro` 可能被 VoiceOver 把 `1m` 读成 `1 meter`，官方建议谨慎使用。
- 💻 **React 用法**：在 React 中可从 `@github/relative-time-element` 导入 `RelativeTimeElement`，并在 `React.JSX.IntrinsicElements` 中声明 `relative-time` 的类型后直接使用。

### [CodePen Commander — 直接从 CLI 同步、托管并构建本地 CodePen 2.0 Pens – Bram.us](https://www.bram.us/2026/11/19/codepen-commander-cli-tool-cdpn/)

Bramus 发布开源 CLI 工具 CodePen Commander（命令 `cdpn`，NPM 包 `codepen-commander`），用 CodePen API v2 把本地 CodePen 2.0 Pen 的克隆、双向同步、批量操作、初始化/模板/分叉、离线预览与静态构建、部署和域名管理等流程搬到终端，减少本地文件与线上 Pen 之间手工复制粘贴；使用 API 需 CodePen Pro，要求 Node.js 20 及以上，1.4.0 起补充批量树遍历与更安全的删除/回收站流程。

- 🚀 **发布安装**：以 MIT 开源的 `codepen-commander` 发布，提供 `cdpn` 命令；全局安装 `npm install -g codepen-commander`，要求 Node.js 20+，调用 CodePen API v2 需要 Pro 账户。
- 🔑 **认证配置**：`cdpn auth login` 打开 API 设置页校验密钥，把命名配置保存到 `~/.cdpn` 并限制为 0600；命令按 `--profile`、`CODEPEN_API_KEY`、当前目录 `.cdpn.json`、克隆 URL 所有者自动选择配置，另有 status/list/default。
- 🔄 **同步机制**：提供 `clone`、`status`、`pull`、`push -m`、`sync`；`push` 将文本、二进制、删除和 `.cdpn.json` 元数据作为单个原子版本上传，等待构建并报告诊断，还会把编译器补丁写回本地；`sync` 做双向三方同步并在双方分叉时标记冲突；可用 `.cdpnignore` 排除额外文件，始终忽略 `.cdpn.json`、`.cdpnignore`、`.git`、`node_modules`、`.DS_Store`。
- 🧩 **克隆新建**：克隆 v1 Classic Pen 时可选转换为 2.0（工具轮询等待浏览器手动转换）或以未链接方式克隆；已有本地 demo 文件夹执行 `push`/`sync` 可按标题、隐私等创建 Pen，并复用 `.cdpn.json` 中信息。
- 📦 **配置清单**：每个受管 demo 根目录的 `.cdpn.json` 保存 `pen_id`、`profile`、同步版本/哈希、文件映射和 `info` 元数据；`info` 中标题、描述、标签、访问级别、模板可编辑并在下次推送同步，Protected 密码不存储，未链接状态可只含 `info`，建议提交进 Git。
- 🗓️ **初始化模板**：`cdpn init` 为现有 demo 交互写入未链接 `.cdpn.json` 与 `.codepen/pen.config.json`（选 classic 时另写 `classic.config.json`）并可立即推送；`cdpn new` 从自有模板或默认 2.0 starter 脚手架，支持 `--as-template`，非空目录拒绝运行；`cdpn fork` 仅支持自己的 Pen，可打开浏览器手动 fork 后回填 URL 克隆。
- ⚡ **批量操作**：1.4.0 起 `status`、`push`、`pull`、`sync`、`delete`、`unlink` 支持指定目录和批量树遍历；批量模式必须显式加 `all`，默认只作用于当前目录或单个路径，`--dry-run` 可预览。
- 🛡️ **批量安全**：树遍历限定在根目录内，把每个 Pen 文件夹视为叶子，跳过符号链接、`.git`、`node_modules`、被 `.cdpnignore` 忽略的路径和静态构建产物；目录名恰为 `all` 会询问是 `./all` 还是全树，破坏性 `delete all`/`unlink all` 先列出目标并二次确认，脚本可用 `--yes`。
- 💻 **本地预览构建**：`cdpn serve` 默认在 `127.0.0.1:3000` 离线预览单个 Pen 或 Pen 目录，`cdpn build --out dist --watch` 生成静态可部署目录；单 Pen 模式直接处理，集合模式递归发现 `.cdpn.json` 并生成内存或静态 `demos.json`，自带明暗索引页且保留已有根 `index.html`，构建到 Pen 子目录时自动加入 `.cdpnignore` 并提示更新 `.gitignore`。
- 🧪 **构建块模拟**：`serve`/`build` 在本地即时模拟 CodePen 2.0 的 `classic` 块（组装 `.pen.html` 与 `classic.config.json`）和 `packages` 块（依据 `package.json` 生成 `esm.sh` import maps）；未模拟的构建块显示提示页，服务只绑定 `127.0.0.1` 且不暴露 `.cdpn.json`、`.env` 等点文件，无 `.cdpn.json` 的子目录被跳过。
- ⚠️ **删除恢复**：1.4.0 的 `cdpn delete` 默认把线上 Pen 移入 CodePen Deleted Items（Trash，可恢复 3 天）并保留本地 `.cdpn.json` 与 `.codepen/`；`--cleanup` 删除 `.codepen/` 但保留仅含 info 的未链接 `.cdpn.json`，`--full-cleanup` 删除两者但不删源文件；检测到线上已删时可恢复、永久删除或 `unlink`。
- 🌐 **部署域名**：`cdpn deploy` 推送本地修改并部署到 CodePen Hosting，`cdpn domains` 查看默认 `*.codepen.app` URL、自定义域名及 DNS 记录，`cdpn domains add` 绑定域名；`cdpn open` 可打开编辑器、预览或部署站点，`undeploy` 和 `domains delete` 可撤销。
- 📊 **JSON 输出**：除交互式 `auth login`、打开浏览器的 `open` 和长运行的 `serve` 外，数据/状态命令支持 `--json`，非交互输出包含类似 HTTP 状态码和消息的 `status` 与 `contents` 的稳定 JSON 信封，便于脚本、CI 和 AI 代理集成。

### [用户引导与产品导览库 | Intro.js](https://introjs.com/)

Intro.js 是面向产品新手引导的轻量级 JavaScript 库，通过分步 tour 和就地 hints 高亮页面元素，帮助用户更快理解产品。页面集中展示其 10kB、无外部依赖、跨框架和可定制等特性，并给出 npm/CDN 安装示例、AGPL 开源授权及一次性终身商业授权方案。

- 📈 **采用规模**：页面称其被全球 5000+ 团队使用，GitHub 获 23.5K stars，npm 年下载量 10M，jsDelivr 月 CDN 请求 110.9M。
- 🧩 **核心功能**：提供分步 tours 和可就地打开的 hints，用于高亮页面元素并引导用户完成 onboarding，每个步骤均可配置。
- ⚡ **轻量与零依赖**：Intro.js 体积为 10kB，无外部依赖，API 设计简洁，目标是在几分钟内交付产品引导而不增加应用负担。
- 🎨 **可定制与跨栈**：可配置引导流程和每一步的外观；纯 JavaScript 可运行于任意框架，并提供 React、AngularJS、Ember、Rails、WordPress 等封装。
- 🛠️ **安装与启动**：支持通过 `npm`、`yarn`、`pnpm` 或 CDN 安装，使用时引入 JavaScript 和 CSS 两个文件；定义 steps 后调用 `start()` 启动。
- 💻 **代码示例**：示例用 `introJs.tour().setOptions({ steps: [...] }).start()` 配置并启动，步骤可只包含 `intro` 文案，也可用 `element` 指向 `#login` 等页面元素。
- 🔑 **授权模式**：Open Source 方案为 0 美元永久，采用 AGPLv3，适用于个人、开源和非商业项目；在商业应用、网站或插件中使用需购买商业许可，商业许可为一次性终身授权。
- 📦 **商业方案**：Starter 为 9.99 美元终身，限 1 个商业项目且无商业支持；Business 为 49.99 美元终身，含 5 个项目、1 个月商业支持、1 个自定义主题；Premium 为 299.99 美元终身，含无限项目、6 个月支持、3 个自定义主题和 24/7 优先支持。
- 📚 **内容延伸**：FAQ 进一步说明免费使用边界、终身许可含义、框架兼容、无依赖和外观定制；博客涉及触屏 Mac 的 Web 应用 onboarding、Warp 的开发者激活经验、React/Next.js 接入教程及 2026 年 SaaS onboarding 趋势。

### [GitHub - wieandteduard/port-menu：一款小巧的 macOS 菜单栏应用，可跟踪各个项目中的开发服务器。· GitHub](https://github.com/wieandteduard/port-menu)

Port Menu 是一个小型 macOS 菜单栏应用，用于自动追踪跨项目的本地开发服务器，无需配置即可查看运行中的服务及其项目、分支、端口和运行时长，并支持停止、打开或复制 localhost 地址；项目面向 macOS 14（Sonoma）及以上用户提供下载，源码构建需 Xcode 15+，发布包经签名和公证。

- 🚀 **自动发现**：Port Menu 常驻菜单栏，每隔几秒扫描本机运行中的开发服务器，无需配置或设置，点击图标即可查看当前运行的服务。
- 🧩 **项目上下文**：对检测到的服务显示 Git 仓库名、当前分支、端口和运行时长，帮助区分不同项目的本地服务。
- ⚙️ **服务操作**：可从菜单直接停止服务器、在浏览器中打开服务，或右键复制 localhost URL。
- 💻 **系统要求**：提供 macOS 下载，要求 macOS 14（Sonoma）或更高；安装方式为打开 DMG 后将 `Port Menu.app` 拖入 `Applications`，再从应用程序启动并点击菜单栏图标。
- 🛠️ **源码构建**：仓库包含 `Porter.xcodeproj`，克隆后进入 `Porter` 目录并打开工程；构建要求 Xcode 15+。
- 📦 **发布与许可**：签名并公证的 macOS 构建发布在 GitHub Releases 页面，维护者发布流程见 `docs/releasing.md`；项目采用 MIT 许可证。
- 🧪 **测试**：测试命令为 `xcodebuild test -project "Porter.xcodeproj" -scheme "Porter" -destination "platform=macOS"`。

### [GitHub - Pagepro/nexity：Nexity 是一个开源系统，用于在 Next.js + Sanity 上创建并发展 AI 原生网站。 · GitHub](https://github.com/Pagepro/nexity)

Nexity 是 Pagepro 开源的 AI 原生网站系统，基于 Next.js + Sanity，面向每次网站改动都落到开发者身上的团队。它把设计系统、页面区块和 Sanity schema 交给 Claude Code、Codex、Cursor 等编码代理，让营销人员用 AI 搭建新板块，再由开发者审核上线，并提供只读审查代理与可复用技能。

- 🚀 **开源发布**：Nexity 以 MIT 协议开源，定位为在 Next.js + Sanity 上启动和扩展 AI 原生网站的系统，提供 `base/` 无品牌起点和 `theme-meridian/` 演示站，后者可用 `pnpm seed` 导入 Meridian 示例数据。
- 🧩 **代理层**：项目内置 `.agents/` 代理层，含 `AGENTS.md` 说明构建方式、`DESIGN.md` 约束视觉、`BRAND.md` 约束品牌表达，以及 `styling-fidelity-reviewer`、`sanity-schema-reviewer`、`groq-parity-reviewer` 等只读审查器；`create-section` 技能会调用这些审查器，并提供项目初始化、创建区块、修复链接、生成 alt 文本、审计 Sanity 使用的技能。
- 🛠️ **仓库与栈**：`base/` 是 pnpm monorepo：`web/` 为 Next.js 16 App Router 应用并内嵌 `/admin` Studio，`studio/` 为共享同一 schema 的独立 Sanity Studio；最低要求 Node.js 22.12 和 pnpm 12.15，采用 React 19.3、Sanity Studio 6.20、Tailwind CSS 4.3、TypeScript 7.0 等。
- 🎨 **页面构建**：提供约两打即用区块，包括 hero、功能网格、bento、统计、定价、FAQ、表单、CTA、列表等，共用可见性、明暗主题、分隔线和锚点 ID 选项；Studio 支持点击编辑、草稿实时预览、发布时按标签重新验证而无需重建，并有 Sections Gallery 示例内容。
- 🌐 **站点能力**：内建每页 SEO 字段、分享图生成、XML sitemap、`IS_INDEXABLE` 控制的 `robots.txt`、JSON-LD 和发布前 GROQ 检查；为 AI 代理提供 `llms.txt`，任意 URL 加 `.md` 可读 Markdown 版本；还包含 c15t GDPR 同意、GTM、Resend 联系表单、Sanity CDN 图片优化和 PWA manifest。
- ⚠️ **已知限制**：从 starter 创建的项目不会自动更新；仅单语言；newsletter 表单只有 UI，未接邮件服务前不存储地址；CMS 重定向和重写发布后约两分钟生效；部分技能依赖 Chrome、Python Pillow/ImageMagick 或带写权限的 Sanity token；`product-mock` 仅在 `theme-meridian/` 可用；seed 会替换同 ID 文档，应使用新数据集；生产环境只在 `/admin` 提供 Studio。
- ⚡ **快速开始**：要求 Node.js 22.12+、pnpm 12.15 和 Sanity 账号，运行 `npm create sanity@latest -- --template Pagepro/nexity/base` 后执行 `pnpm dev`，站点在 `http://localhost:3000`，Studio 在 `/admin`；代理层已为 Claude Code 和 Codex 链接，可用 `pnpm agent:doctor` 检查，Cursor 需更新技能或手动配置。

### [请稍候……](https://www.kirupa.com/arcade/)

收到的内容仅为“Please wait while your request is being verified...”验证提示，未包含可整理的文章正文，因此无法生成技术周刊摘要。

- ⚠️ **正文缺失**：输入中没有产品、版本、技术机制或发布信息，无法提取有效技术要点。

### [Ductus · 将你的笔迹化作字体](https://ductus.sorenblank.com/)

一款将个人手写笔迹转化为字体的工具，用户按引导逐个小写字母书写，约五分钟完成 26 个字母的采集；界面提供开始、返回、撤销、清除和下一步等操作，并强调内容不会离开手机、设备或电脑。

- 🎨 **手写转字体**：用户按提示书写 26 个字母，工具据此生成个人手写字体。
- ⚡ **快速采集**：流程约需五分钟，界面显示 1 of 26 等进度，并提示 Write a small a 和 Lowercase。
- 🛡️ **本地隐私**：原文强调 Nothing leaves this phone device computer，即书写内容不离开本地设备。
- 🛠️ **书写控制**：界面提供 Start、Back、Undo、Clear、Next 等操作，便于返回、撤销、清除和进入下一步。
