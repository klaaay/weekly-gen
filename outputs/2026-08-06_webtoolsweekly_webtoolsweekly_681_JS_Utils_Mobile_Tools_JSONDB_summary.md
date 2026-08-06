### [订阅 | 超人类 AI](https://www.superhuman.ai/subscribe?utm_source=wp_ads&utm_medium=Web+Tools+Weekly&utm_content=v2-r769560-p1040662-c45319&transaction_id=1026177dbf8d156e9221a65b078db8)

**原文标题**: [Subscribe | Superhuman AI](https://www.superhuman.ai/subscribe?utm_source=wp_ads&utm_medium=Web+Tools+Weekly&utm_content=v2-r769560-p1040662-c45319&transaction_id=1026177dbf8d156e9221a65b078db8)

overview summary  
- 🤖 SUPERHUMAN AI 是一个专注于人工智能工具、教程与新闻的平台，帮助用户快速提升技能。  
- ⏱️ 每天仅需 3 分钟，即可掌握最新 AI 知识与实用技巧，高效学习。  
- 👥 已吸引超过 200 万读者订阅，助力提升生产力与职业发展。  
- 💌 提供免费订阅服务，注册后即可获取丰富资源。  
- 📚 包含 1,000+ 提示词、AI 课程及速查表，满足不同学习需求。  
- 🔒 平台设有隐私政策与使用条款，保障用户权益。

---

### [](https://github.com/okikio/undent)

**原文标题**: [GitHub - okikio/undent: undent removes extra leading spaces from template literals and multi‑line strings. · GitHub](https://github.com/okikio/undent)

undent 是一个用于 JavaScript/TypeScript 的库，主要解决模板字符串和多行字符串中因代码缩进而产生多余空格的问题。它自动检测并去除共同缩进，同时提供对齐、嵌入、自定义实例以及 Unicode 视觉对齐等高级功能，适用于 Deno、Node.js、Bun 等所有 JavaScript 运行环境。

- 📦 核心功能：通过标签模板 `undent` 自动去除字符串中的共同缩进，并修剪首尾空白行
- ✂️ 保留换行风格：支持 `\n`、`\r\n`、`\r` 原样保留，不进行隐式转换
- 📐 多行插值对齐：使用 `align()` 让多行值保持插入列对齐，避免后续行回退到列 0
- 🧩 嵌入已有缩进内容：使用 `embed()` 先去除值自身的缩进，再对齐到插入位置
- 📄 普通字符串处理：通过 `.string()` 或 `dedentString()` 处理非模板字符串，如 SQL、配置文件
- ⚙️ 自定义实例：通过 `.with()` 或 `createUndent()` 配置策略（common/first）、修剪模式、换行符等
- 🎨 Unicode 视觉对齐：提供 `createUnicodeColumnOffset()` 支持终端中制表符、emoji、宽字符的视觉对齐
- 🚀 性能优化：按模板调用位置、包装器对象、嵌入内容加精确 pad 字符串进行缓存，避免重复计算
- 📚 丰富 API：包含 `align`、`embed`、`dedentString`、`splitLines`、`rejoinLines` 等工具函数
- 🔒 安全边界：缓存有界且不混用不同布局，但并非安全隔离机制，多租户场景需自行评估

---

### [树，来自皮埃尔](https://trees.software/)

**原文标题**: [Trees, from Pierre](https://trees.software/)

概述：這是一個高效能、可自訂的開源檔案樹渲染函式庫 @pierre/trees，提供虛擬化、Git 狀態、拖放、搜尋過濾、無障礙鍵盤操作、多種圖示與主題，並支援 CSS 變數與密度調整。

- 📦 可透過 `pnpm add @pierre/trees` 安裝，目前版本為 1.0.0-beta.6
- 🗂️ 支援 `flattenEmptyDirectories` 選項，可將單一子資料夾鏈摺疊為一行，讓樹狀圖更緊湊
- 🔍 內建 Git 狀態徽章（M/A/D/R/U/忽略），並自動為含變更子項的資料夾顯示圓點指示
- 🖱️ 可透過 `composition.contextMenu` 與 `renderContextMenu` 自訂右鍵選單，並支援觸發按鈕或兩者並用
- 🚚 啟用 `dragAndDrop` 即可拖曳檔案/資料夾，支援懸停自動展開、禁用搜尋時拖曳，並可用 `canDrag` 鎖定特定路徑
- 🔎 提供三種搜尋模式：隱藏非匹配項、摺疊非匹配資料夾、展開含匹配項的資料夾
- ⚡ 自動虛擬化，可流暢渲染數萬個項目（示範包含 2,956 個檔案），並支援 `stickyFolders`
- ♿ 預設具備鍵盤導覽、焦點管理，以及 ARIA tree/treeitem 角色，符合 WCAG 2.1 指引
- 🎨 內建 minimal、standard、complete 三種累進圖示層級，並可用 CSS 變數覆寫或完全自訂 sprite
- 🌗 支援 Pierre 的 Shiki 主題（如 pierre-light / pierre-dark），可同步更新側欄與 Git 裝飾顏色
- 🎛️ 可透過 `style` prop 覆寫 CSS 自訂屬性，範例包含 Light、Dark 與 Synthwave '84（使用 OKLCH 色彩）
- 📐 提供 `density` 參數（compact / default / relaxed 或自訂數值），統一調整列高與間距
- ❤️ 由擁有超過 150 年分散式系統經驗的 Pierre Computer Company 團隊開發，並提供 Discord 與 GitHub 社群連結

---

### [µJS — 轻量级 AJAX](https://mujs.org/)

**原文标题**: [µJS — Lightweight AJAX Navigation Library](https://mujs.org/)

µJS 是一个轻量级前端库，无需框架和构建步骤，即可将传统多页网站变成类似单页应用的即时导航体验。

- ⚡️ 拦截内部链接和表单提交，通过 AJAX 后台获取页面，仅替换变化内容，实现无刷新快速导航。
- 🧩 零学习成本：只需引入单个 script 标签并调用 `mu.init()`，兼容 PHP、Python、Ruby、Go 等任何后端。
- 🔄 基于原生 Fetch API 和 AbortController，无 XMLHttpRequest，可自动取消过期的请求，支持 View Transitions 和 DOM morphing。
- 🚀 功能强大：支持悬停预取、内置进度条、补丁模式（一次请求更新多个页面片段）、任意元素/事件触发、完整 HTTP 动词、SSE 实时更新。
- 📦 极简体积：单文件约 5 KB gzipped，零依赖，无需构建步骤。
- 🛠 与 Digicreon 生态集成：可搭配 Temma（PHP MVC 框架）和 µCSS（CSS 框架）使用。

---

### [](https://techproductivity.co/)

**原文标题**: [Tech Productivity | A Weekly Newsletter for Tech Pros Who Want to Get Stuff Done](https://techproductivity.co/)

overview summary
这份内容是一份面向技术从业者的电子通讯（Newsletter）介绍，包含订阅信息、隐私与数据条款说明，以及多位读者对通讯内容的积极评价。

- 📧 面向技术专业人士的电子通讯“Tech Productivity”，目前拥有 3,511 位订阅者。
- 📅 每周一发送一封邮件，承诺无垃圾邮件，并设有隐私政策说明。
- 🔒 订阅即表示同意接收邮件，并遵守相关条款与条件，数据通过 EmailOctopus 收集和追踪。
- 🛡️ 网站受 reCAPTCHA 保护，并适用 Google 隐私政策与服务条款。
- 💬 多位读者（Nick C.、Marek S.、Saeed K.、Mark W.、Roxana B.、Roderik V.）自发分享好评。
- ⭐ 读者普遍认为该通讯内容简洁、信息量大，每周都期待阅读。
- 🛠️ 读者反馈从中发现许多实用且可日常使用的新工具，价值很高。

---

### [面向现代 Web 的 Markdown 引擎](https://comark.dev/)

**原文标题**: [The Markdown Engine for the Modern Web - Comark](https://comark.dev/)

概述：Comark 是一个面向现代 Web 的高性能 Markdown 解析引擎，支持流式解析、组件语法（Vue/React/Svelte/Angular）、自动闭合不完整语法，并兼容 markdown-it 插件，旨在将 Markdown 视为数据而非代码。

- 🚀 高性能流式解析：支持实时解析，自动闭合不完整语法，适合 AI 聊天界面和渐进加载场景。
- 🧩 原生组件支持：在 Markdown 中嵌入组件，可渲染为 Vue、React、Svelte、Angular 等多种框架组件。
- ⚡ 运行时解析：无需构建步骤，可在服务端、浏览器或 Worker 中解析，内容保存后即时生效。
- 📦 统一解析器，多端输出：同一份源码可渲染到 Vue、React、Svelte、Angular、Nuxt、HTML 和 ANSI。
- ✅ 标准 Markdown 兼容：默认支持 CommonMark 和 GFM，属性和组件为可选语法，不引入新语言。
- 🔌 丰富插件生态：兼容 markdown-it 插件，支持 Shiki 高亮、KaTeX 数学公式、Mermaid 图表、目录等。
- 📄 可序列化文档：解析结果为纯 MarkdownDocument，易于遍历、缓存、序列化和网络传输。
- 🛠️ 快速上手：安装简单，提供各框架文档，可在几分钟内将 Markdown 渲染为 UI。

---

### [](https://github.com/ybouane/liquidglass)

**原文标题**: [GitHub - ybouane/liquidglass: A liquid glass effect library for the web. Apply realistic glass refraction, blur, chromatic aberration, and lighting effects to any HTML element using WebGL shaders. · GitHub](https://github.com/ybouane/liquidglass)

LiquidGlass 是一个基于 WebGL 的液体玻璃效果库，可让任意 HTML 元素呈现真实的折射、模糊、色差与光照效果，支持 npm/CDN 安装，并提供简洁的 API 和丰富的逐元素配置。

- 🔮 核心功能：通过 WebGL 着色器实现玻璃折射、高斯模糊、色差、菲涅尔反射、多光源高光、内描边和投影等效果。
- 📦 安装与引入：支持 `npm install @ybouane/liquidglass`，也可直接从 CDN 以 ES module 方式导入。
- 🚀 快速上手：调用 `LiquidGlass.init({ root, glassElements, defaults })` 即可启动；玻璃元素必须是 root 的直接子元素，并通过 `data-config` 配置参数。
- ⚙️ 工作原理：普通子元素先栅格化到隐藏 Canvas，静态内容缓存，`data-dynamic` 或 `<video>` 每帧重捕获；每个玻璃元素注入子 `<canvas>` 并运行着色器渲染。
- 🧩 实例 API：`init()` 返回 Promise，实例暴露 `fps`、`destroy()` 和 `markChanged(element?)`，用于手动刷新无法自动检测的变化。
- 🎛️ 逐元素配置：支持 `blurAmount`、`refraction`、`chromAberration`、`cornerRadius`、`zRadius`、`floating`、`button`、`bevelMode` 等 20 余项参数。
- 🏷️ 元素属性：`data-dynamic` 让内容每帧重采，`data-config` 使用 JSON 配置；`<video>` 自动视为动态内容。
- 🖼️ 堆叠与层级：库重新实现 CSS stacking-context 规则，识别 z-index、transform、filter、opacity 等触发条件来确定绘制顺序。
- ⚠️ 限制与性能：玻璃元素必须为 root 直接子元素；root 自身不会被捕获；多个 root 不共享折射；`data-dynamic` 应谨慎使用，避免每帧全量重绘。
- 🌐 浏览器支持：需要 WebGL 1.0 + Canvas 2D + SVG foreignObject，主流现代浏览器均可用，并支持 WebGL 上下文丢失自动恢复。
- 📄 开源许可：MIT License。

---

### [](https://github.com/franciscop/brownies)

**原文标题**: [GitHub - franciscop/brownies: 🍫 Tastier cookies, local, session, and db storage in a tiny package. Includes subscribe() events for changes. · GitHub](https://github.com/franciscop/brownies)

Brownies 是一个轻量级 JavaScript 存储库，以类似对象的方式统一操作 cookies、localStorage、sessionStorage 和数据库存储，支持类型保留、订阅变化、标准迭代，并提供简单的安装与配置方式。

- 🍫 提供 `cookies`、`local`、`session`、`db` 四种存储对象，均可通过 set/get/delete 直接操作。
- 📦 安装：`npm install brownies`，也支持 CDN 引入或 JSFiddle 试用。
- 🥠 cookies 操作自动保留 number、boolean、string、array、object 等类型，底层用 JSON + encodeURIComponent 编码。
- ⚙️ cookies 支持全局配置 `expires`、`domain`、`path`、`secure`，需使用 `cookies[options]` 方式设置。
- 🗂️ `local` 和 `session` 对应 localStorage 与 sessionStorage，同样保留类型并可用 `delete` 删除。
- 🔄 存储对象支持 `Object.keys()`、`Object.values()`、`Object.entries()`、for...of 等标准迭代方式，可轻松遍历删除。
- 👂 `subscribe()` 可监听属性变化，支持原生 API 和跨标签页触发；`unsubscribe()` 可通过返回的 id 或回调取消订阅。
- ⚛️ 提供 React 组件中同步多标签页状态的示例，并提醒保持订阅数量较低以控制性能。
- 💡 2.0 起采用自定义数据存储，不能用原生 `getItem` 直接读取 brownies 写入的数据。
- 🏷️ 库名源于作者前同事的布朗尼，寓意“比 cookies 更好吃”，仓库曾用名 clean-store。

---

### [](https://www.policystack.dev/)

**原文标题**: [PolicyStack — privacy and consent primitives for developers](https://www.policystack.dev/)

PolicyStack 是一个开源框架，将隐私与同意视为代码基础设施，提供可组合的构建模块，让团队像处理认证、支付或功能标志一样，以代码形式管理隐私——版本可控、可测试，并可供 AI 代理使用。

- 🔧 将隐私与同意作为“原语”，以代码形式融入技术栈，替代沉重的 SaaS 横幅和手写法律页面。
- 🧩 提供三大构建模块：Consent（无头同意状态机）、Policy（类型化配置）、Cloud（托管控制平面）。
- ⚡ Consent 核心小于 4KB，适配 React、Vue、Solid、Svelte、Angular，并内置 GA、Meta Pixel 等集成。
- 📜 Policy 允许用 TypeScript 定义隐私策略一次，渲染为 React 组件或 Markdown，附赠一个 shadcn 风格的同意横幅。
- ☁️ Cloud 提供跨应用的集中式策略版本管理、审计日志和同意分析，按需选用。
- ✅ 原则：版本控制、可测试、可组合、体积小、Apache-2.0 开源、诚实（不提供法律建议）。
- 🤖 设计 DX 的同时也让 AI 代理容易读取；机器可读表面是合规的“收据”，而非目标本身。
- 💰 核心模块永久免费并依靠赞助维护，永不重新授权或功能封锁；Cloud 是唯一的商业部分且可选。
- 🏆 获得 Onstage Top 100 认可。

---

### [](https://github.com/WebReflection/buffered-clone)

**原文标题**: [GitHub - WebReflection/buffered-clone: A structured clone equivalent able to encode and decode as a buffer. · GitHub](https://github.com/WebReflection/buffered-clone)

buffered-clone 是一个类似 structuredClone 的序列化工具，能将几乎所有 JavaScript 支持的类型以及 ImageData 转换为二进制格式，并提供接近原生性能的递归序列化、灵活的缓冲区控制以及简单的编解码 API。

- 🧬 提供类似 structuredClone 的序列化能力，支持所有 JS 类型及 ImageData 转二进制。  
- ⚡ 递归处理几乎任何可序列化内容，运行至“热”状态后接近原生 structuredClone 速度。  
- 💾 支持写入预分配缓冲区、SharedArrayBuffer，以及可增长的 ArrayBuffer。  
- 🔧 支持 toJSON，并规划了类似 MessagePack 的扩展机制。  
- 📦 通过 BufferedClone 构造函数可配置 byteOrder、circular、byteOffset、byteLength、useFloat32、useUTF16 等选项，并利用 encode/decode 进行操作。  
- 📜 项目为 MIT 许可证，当前在 GitHub 上拥有 43 stars、1 fork 和 4 watchers。

---

### [](https://github.com/maplibre/maplibre-react-native)

**原文标题**: [GitHub - maplibre/maplibre-react-native: MapLibre React Native – Interactive vector tile maps with MapLibre Native in Expo and React Native supporting Android & iOS. · GitHub](https://github.com/maplibre/maplibre-react-native)

MapLibre React Native 是一个用于 React Native 和 Expo 的交互式矢量地图库，基于 MapLibre Native，支持 Android 与 iOS。它源自 rnmapbox 的分支，在 MapLibre 与 Mapbox SDK 分道扬镳后独立发展，提供文档、贡献指南和社区支持。

- 📱 为 React Native 和 Expo 提供基于 MapLibre Native 的 Android 与 iOS 地图支持。
- 🔄 源自 rnmapbox 社区库分支，因 MapLibre 与 Mapbox SDK 分化而独立。
- 📖 完整文档位于 maplibre.org/maplibre-react-native/。
- 🤝 通过 CONTRIBUTING 指南参与开发，可在 OpenStreetMap Slack 的 #maplibre-react-native 频道交流。
- 🗺️ 支持交互式矢量瓦片地图，覆盖多种使用场景。
- ⭐ 项目在 GitHub 上拥有 644 星、117 个 fork，采用 MIT 许可证，并配有行为准则与安全策略。

---

### [](https://github.com/lodev09/react-native-true-sheet)

**原文标题**: [GitHub - lodev09/react-native-true-sheet: The true native bottom sheet experience 💩 · GitHub](https://github.com/lodev09/react-native-true-sheet)

这是一个 React Native 原生底部弹窗（Bottom Sheet）库，基于新架构 Fabric 实现，提供高性能、原生体验，并支持多平台特性。

- ⚡ 基于 Fabric 新架构构建，性能卓越
- 🚀 完全原生实现，零 JS Hack，保证流畅度
- ♿ 原生无障碍与屏幕阅读器支持
- 🔄 提供灵活 API，支持命令式方法和生命周期事件
- ⌨️ 内置键盘处理，自动调整弹窗位置
- 📐 支持 iPad 和 Android 平板的侧边弹窗
- 🪟 原生支持 iOS 26+ Liquid Glass 效果
- 🐎 对 react-native-reanimated 提供一流支持
- 🧭 内置 React Navigation 的 sheet navigator 集成
- 🌐 完整支持 Web 平台
- 📦 安装要求：React Native 0.81+、新架构、Xcode 26.1+（v3+），Expo SDK 54+ 可直接安装
- 📝 基本用法：通过 ref 调用 present/dismiss，使用 detents 控制弹窗高度
- 🤖 支持 AI 技能，可自动生成正确代码并避免常见错误
- 📚 提供完整文档、示例、迁移指南和 Jest 测试方案
- ⚖️ 采用 MIT 开源许可证，由 @lodev09 维护

---

### [获取失败](https://recs.page/web-tools-weekly?ref_code=7c293df6a4&lc=link_campaign_b7f2c08f285c&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recs.page/web-tools-weekly?ref_code=7c293df6a4&lc=link_campaign_b7f2c08f285c&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [](https://github.com/IronTony/react-native-docusign)

**原文标题**: [GitHub - IronTony/react-native-docusign: 📱 React Native / Expo native module for in-app DocuSign captive signing. TypeScript bindings for the DocuSign iOS + Android SDKs (consumer-supplied via CocoaPods / Maven), useDocuSignSigning hook, Expo Config Plugin. Cross-platform 13-field session payload · GitHub](https://github.com/IronTony/react-native-docusign)

这是一个 React Native / Expo 原生模块，非官方封装 DocuSign 官方 iOS 与 Android SDK，让应用能在 App 内直接展示原生 DocuSign 签名界面（captive signing）。基于 Expo Modules API，需在 Expo SDK 55+ 或裸 React Native 0.74+ 中使用，不支持 Expo Go，需开发构建或重新 prebuild。

- 📱 核心能力：提供原生应用内嵌入式签名 UI，含文档查看、表单字段、签名笔、日期选择器、附件和下拉框；无 WebView、无 HTML 桥接。
- 🔄 双平台流程差异：会话流程（initialize → loginWithAccessToken → presentCaptiveSigning）iOS 和 Android 均支持；URL 流程（presentCaptiveSigningWithUrl）仅 iOS 支持，Android 会抛出 not_implemented。
- 🔗 统一 13 字段后端会话负载：integratorKey、accessToken、envelopeId 等字段在同一代码路径下双平台通用，后端只需生成一次。
- 📦 SDK 不随包分发：iOS 通过 CocoaPods 拉取 DocuSign-iOS-SDK 4.1.1，Android 通过 DocuSign Maven 仓库拉取 androidsdk 2.1.4；Expo Config Plugin 会在 prebuild 时下载并处理 Android sdk-pdf AAR 的 Glide 类冲突。
- ⚙️ 安装与配置：npm 安装后需在 app.config 中加入插件，并执行 npx expo prebuild --clean；裸 RN 项目需手动添加 Pod、Maven 仓库及权限描述。
- 🔑 API 摘要：提供 initialize、loginWithAccessToken、presentCaptiveSigning、presentCaptiveSigningWithUrl（iOS only）、logout、isLoggedIn、endSigningSession、reset，以及三种事件监听器和 useDocuSignSigning hook。
- 🔐 认证模式：JWT Grant 必须在后端完成，移动端只获取短期 access token 使用后立即丢弃；后端需通过 Connect webhook 作为签名状态最终依据。
- 📄 字段预填：SDK 不提供客户端预填 API，预填需在后端创建信封时通过 tabs（textTabs、dateTabs 等）完成。
- 🧹 多信封链式签名：连续多次签名之间建议调用 endSigningSession 清理 SDK 状态，避免 iOS WebKit 竞态导致第二次打开卡在 spinner。
- 🚫 主要限制：URL 签名仅 iOS；不支持离线签名、模板管理、自定义签名 UI；无 Web 支持；部分保存不可用。
- 🛠️ 常见问题：iOS 登录失败常因 Info.plist 缺少 AppIdentifierPrefix；Android 构建找不到 SDK 需确认 DocuSign Maven 仓库已加入；Expo Go 无法使用。

---

### [](https://github.com/mathnotes-app/mobile-ink)

**原文标题**: [GitHub - mathnotes-app/mobile-ink: Production-grade React Native ink engine with native Skia/Metal drawing and continuous canvas primitives. · GitHub](https://github.com/mathnotes-app/mobile-ink)

@mathnotes/mobile-ink 是生产级的 React Native 墨迹绘制引擎，从 MathNotes 笔记应用提炼而成，提供原生 Skia/Metal 渲染、连续笔记本画布及 Apple Pencil 支持等高级能力，旨在成为社区共享的高性能绘图基础。

- 🖊️ 核心定位：iOS 优先的原生绘图引擎，包含 Apple Pencil 输入、Skia/Metal 渲染、笔迹序列化、选择、缩放与动量滚动。
- 🎯 项目动机：填补开源领域缺少成熟笔记画布引擎的空白，避免每个团队重复构建底层原生栈。
- ⚖️ 对比优势：相比 PencilKit、React Native Skia 和 Web canvas，额外提供连续笔记本、页面池、长文档交互及原生内存管理等关键能力。
- 📦 功能概览：支持连续笔记本（固定原生引擎池）、多工具（笔、荧光笔、橡皮擦、选择、形状识别）、JSON 序列化和缩放渲染。
- 📱 平台与兼容：iOS 已生产使用，Android V1 支持 GPU 渲染与核心功能；Expo Go 不支持，需 dev-client 或 prebuild。
- 🔧 安装要求：需安装 @shopify/react-native-skia、gesture-handler、reanimated、worklets，并配置 iOS/Android 原生构建环境。
- 🚀 快速上手：通过 `<InfiniteInkCanvas>` 组件即可创建连续笔记本画布，支持工具状态和保存回调。
- 🧩 公开接口：提供低层 `NativeInkCanvas`、视图控制 `ZoomableInkViewport`、引擎池 `ContinuousEnginePool` 及完整笔记本壳 `InfiniteInkCanvas`。
- 📝 示例应用：example/ 为 Expo dev-client 应用，演示绘图、缩放、工具、选择、保存/重载等完整路径。
- 🗺️ 路线图：近期聚焦改进安装文档、增加集成示例、优化选择性能，并完善 Android 基准测试。
- 📄 开发与许可：提供完整开发脚本（类型检查、测试、构建），采用 Apache-2.0 许可证。

---

### [](https://github.com/hryhoriiK97/expo-paperkit)

**原文标题**: [GitHub - hryhoriiK97/expo-paperkit: Apple PaperKit for Expo/React Native · GitHub](https://github.com/hryhoriiK97/expo-paperkit)

expo-paperkit 是一个为 Expo/React Native 提供 Apple PaperKit 标记体验的库，支持绘图、形状、标注等功能，适用于 iOS 和 macOS。

- ✏️ 提供完整的 PaperKit 绘图画布，支持 Apple Pencil
- 🔶 支持插入形状、文本框和箭头/线条
- 💾 可将标记数据保存为 base64 并恢复
- 🖼️ 可将画布导出为 PNG 或 JPG 图片
- ↩️ 支持撤销和重做操作
- ⚙️ 可配置功能集、缩放比例和画布尺寸
- 🎨 集成 iOS 的 PKToolPicker 和 macOS 的 MarkupToolbar
- 🏞️ 支持设置背景图片
- 👁️ 提供只读模式，用于查看已保存的标记
- 📋 要求 iOS 26.0+ 或 macOS 26.0+、Expo SDK 54+、React Native 0.81+
- 📦 通过 `npm install expo-paperkit` 或 `yarn add expo-paperkit` 安装
- ⚠️ 需要原生代码，无法在 Expo Go 中运行；macOS 需使用 expo-desktop 配置
- 🚀 快速开始示例展示了 `PaperMarkupView` 和 `PaperMarkupRef` 的基本用法，包括保存、导出和监控标记变化
- 📚 提供完整的 API 参考文档（props、事件、ref 方法及类型）
- 📄 基于 MIT 许可证开源

---

### [](https://github.com/software-mansion/react-native-enriched-html)

**原文标题**: [GitHub - software-mansion/react-native-enriched-html: HTML-based Rich Text solution for React Native · GitHub](https://github.com/software-mansion/react-native-enriched-html)

overview summary  
react-native-enriched-html 是一个基于 HTML 的 React Native 富文本解决方案，提供原生输入与显示组件，支持新架构，可在 Android、iOS 和 Web 上运行，并具备高度可定制样式、链接、提及、图片等功能。

- ⚡ 完全原生的输入与显示组件，仅支持 React Native 新架构（Fabric），兼容 RN 0.81–0.86。
- 🎨 支持实时、同步的 HTML 解析与文字样式，可自定义样式以无缝集成 UI。
- 🔤 EnrichedTextInput 为非受控输入组件，直接与原生组件交互，性能优秀且用法简单。
- 📄 EnrichedText 显示组件可与输入组件完美配合，保证编辑与显示视觉一致。
- 🛠️ 安装简单：Bare RN 应用使用 `yarn add` + pod install；Expo 需 prebuild，不支持 Expo Go。
- ✏️ 提供 toggleBold 等命令式方法，通过 ref 调用；onChangeState 事件报告样式状态（isActive/isBlocking/isConflicting）。
- 📋 支持多种内联标签（粗体、斜体、下划线、删除线、行内代码、链接、提及、图片）和段落标签（标题、列表、引用、代码块等）。
- 🚫 样式之间存在冲突与阻止关系，如 `<b>` 在 `<codeblock>` 内被阻止，标题与段落样式互斥。
- 🔗 链接支持自动检测（可自定义正则）及手动通过 `setLink` 设置，并可编辑现有链接。
- 💬 提及功能支持自定义指示符（默认 `@`），提供 onStartMention、onChangeMention、onEndMention 事件及 `setMention` 方法。
- 🖼️ 支持通过 `setImage` 插入行内图片，图片会替换选中文本或插入光标位置。
- 📡 其他事件包括 onFocus、onBlur、onChangeText、onChangeHtml、onChangeSelection、onLinkDetected、onMentionDetected、onKeyPress、onPasteImages 等。
- 🧩 可通过 `contextMenuItems` 扩展原生文本菜单（Android 和 iOS 16+）。
- 📚 提供完整的 API 参考文档，并说明已知限制：目前仅支持单层列表，不支持嵌套列表。
- 👥 由 Software Mansion 开发，基于 MIT 许可证，并由 Filament 赞助。

---

### [](https://github.com/watadarkstar/react-native-nsfw-detector)

**原文标题**: [GitHub - watadarkstar/react-native-nsfw-detector: A fast on device AI image safety detector for React Native / Expo using a CoreML model to detect nudity and unsafe visual content in images. · GitHub](https://github.com/watadarkstar/react-native-nsfw-detector)

react-native-nsfw-detector 是一个基于 CoreML 的 React Native/Expo 库，用于在 iOS 设备端快速检测图像中的 NSFW 内容，无需网络请求，简单易集成。

- 📱 支持 React Native 0.70+、iOS 13+，需 Xcode 10+ 及 CoreML 环境
- 🧠 使用 CoreML 模型在设备端推理，快速、轻量、无网络依赖
- ⚠️ 注意：iOS 模拟器精度显著降低，建议在实体设备上测试
- 📦 支持 npm 或 yarn 安装，集成方便
- 💻 提供简单的 Promise API：`checkNSFW(imageUri)` 返回置信度，可自设阈值
- 🔧 附带示例 Expo 应用，可本地运行验证真实推理效果
- 🔄 基于 LOVOO 的 NSFWDetector 构建，采用 MIT 许可证
- 👤 开发者：Adrian，可通过 Twitter 联系或提交 PR 贡献

---

### [](https://github.com/LegendApp/legend-motion)

**原文标题**: [GitHub - LegendApp/legend-motion: Legend Motion is a declarative animations library for React Native, to make it easy to transition between styles without needing to manage animations. · GitHub](https://github.com/LegendApp/legend-motion)

overview summary
这是一个关于 Legend-Motion 动画库的 README 介绍，强调其为 React Native 提供声明式动画，便于在样式间平滑过渡，无需手动管理动画状态。

- 📦 安装方式：`npm install @legendapp/motion` 或 `yarn add @legendapp/motion`
- 🎬 使用 `Motion.View` 组件，通过 `initial`、`animate`、`whileHover`、`whileTap`、`transition` 等 props 轻松定义动画
- ✨ 支持 React Native 和 react-native-web 双平台
- 🔄 API 设计类似 Framer Motion，方便在 React Native 与 React 之间混合使用
- 🖼️ 支持 SVG 和线性渐变动画，并支持 `transformOrigin` 属性
- 👆 内置 `whileHover` 和 `whileTap`，方便处理触摸和悬停交互
- 🚪 提供 `AnimatePresence` 组件实现退出动画
- 🧩 零额外依赖，基于 React Native 内置 Animated，专为高性能打造
- 🔤 使用 TypeScript 编写，提供强类型支持
- 📚 完整文档与在线示例可在官方网站查看
- ⚠️ 从 1.x 升级时，`whileTap` 和 `whileHover` 需要 `Motion.Pressable` 祖先组件来跟踪状态
- 🧑‍⚖️ 采用 MIT 许可证，由 Jay Meistrich 创建并维护

---

### [未找到标题](https://www.vpdae.com/redirect/1m6ckzpndu36hwa8ddokjx3coa0)

**原文标题**: [No title found](https://www.vpdae.com/redirect/1m6ckzpndu36hwa8ddokjx3coa0)

无法总结：未找到主要内容。

---

### [](https://github.com/boringSQL/dryrun)

**原文标题**: [GitHub - boringSQL/dryrun: PostgreSQL schema intelligence MCP server with offline linting, migration safety, query validation for AI coding assistants. · GitHub](https://github.com/boringSQL/dryrun)

overview summary
DryRun 是一个面向 PostgreSQL 的 MCP（模型上下文协议）服务器，旨在让 AI 编码助手在不连接生产数据库、不接触凭据的前提下，获得完整的 schema 智能。它由 CLI 工具和 MCP 服务器组成：CLI 负责从数据库提取 schema 快照，并支持离线 lint、迁移安全分析、查询验证、快照 diff 和多节点统计；MCP 服务器则让 AI 助理直接基于快照工作。项目强调安全性和离线工作流，支持多种安装方式、团队快照共享、OCI 注册表推送，以及与 Claude Code/Codex 等工具的快速集成。

- 📌 核心价值：通过离线 schema 快照为 AI 助手提供数据库结构认知，避免 AI 直接连接生产库，降低误操作和数据泄露风险。
- 🔒 安全设计：凭据不离开 DBA 机器；MCP 服务器无需数据库连接，也无需 SUPERUSER 权限，减少 SQL 注入和 AI 误删风险。
- 🛠️ 双组件架构：CLI 工具负责导入、分析和生成 JSON 快照；MCP 服务器读取同一快照并暴露 14 个工具（schema 探索、查询验证、迁移检查等）。
- 📋 CLI 分析能力：包含 20+ 命名/类型/分区等约定规则和 13 条结构审计规则；迁移安全分析（锁类型、表重写检测）；SQL 解析和列引用校验；快照差异对比；副本活动统计。
- 🚀 安装方式：Homebrew（需先 `brew trust`）、npm/npx（自动缓存预编译二进制，支持 macOS/Linux/Windows x64/arm64）、源码构建（Go 1.26+）。
- ⚡ 快速体验：克隆仓库后进入 `examples/demo` 运行 `dryrun lint`，无需数据库即可看到 22 条违规（6 error、16 warning）的示例输出。
- 🏁 快速开始：有数据库访问时用 `dryrun init --db`；无访问时由他人导出 `schema.json` 后 `dryrun init` + `dryrun import`，所有命令离线工作。
- 🗄️ 多节点与多库：支持从只读副本单独采集活动指标，按 `(project_id, database_id)` 键控快照，通过 profile 管理多套数据库配置。
- 👥 团队协作：快照可推送到 POSIX 目录或任何 OCI 注册表（GHCR、GAR、ECR 等），内容寻址和增量推送让共享高效且幂等。
- 🤖 MCP 集成：一条命令即可在 Claude Code 或 Codex 中启用（如 `claude mcp add dryrun -- dryrun mcp-serve`），也支持 npx 运行；服务器自动发现项目内 `.dryrun/schema.json`。
- 🔗 生态关联：dryrun 是 boringSQL 套件的一部分，与 RegreSQL（SQL 回归测试）和 Fixturize（数据子集/脱敏）配合使用。
- 📚 文档完善：提供教程、多节点统计、配置参考、CLI 稳定性说明和安全概览等资源链接。

---

### [](https://github.com/n-e/pg-typesafe)

**原文标题**: [GitHub - n-e/pg-typesafe: Strongly typed queries for PostgreSQL and TypeScript · GitHub](https://github.com/n-e/pg-typesafe)

pg-typesafe 是一个为 PostgreSQL 查询生成 TypeScript 类型的工具，无运行时依赖且零额外冗长，使普通 pg 查询获得完全类型安全体验。

- ⚙️ 核心能力：通过静态分析常量 SQL 查询，自动推断参数类型与返回行类型，查询写法与原生 pg 完全一致
- 🚀 快速上手：安装 `pg-typesafe` 后运行命令连接数据库，生成 `src/defs.gen.ts`，再将 `Pool` 转换为 `TypesafePool` 即可启用类型检查
- 🛠️ 配置灵活：支持命令行参数（如 `connectionString`、`definitionsFile`、`tsConfigFile`）及 `pg-typesafe.config.ts` 配置文件，参数均有 JSDoc 说明
- 🔢 BIGINT 映射：可按需将 PostgreSQL BIGINT 类型转换为 JavaScript `bigint`，结合 `pg` 的 `setTypeParser` 与配置中的 `transformParameter`/`transformField` 实现
- 🗄️ JSONB 类型化：支持将 JSONB 列映射为特定 TypeScript 类型，可根据表名和列名自动生成对应的外部接口定义
- 🔄 类型传播：通过 `TypesafePoolClient`、`TypesafeQuerier` 等类型，可让传递连接参数的函数也保持完整类型安全
- ⚠️ 使用限制：仅支持常量 SQL 查询，动态拼接查询无法分析，推荐使用常量以规避 SQL 注入并提升性能
- 🔀 同类工具：与 `pgtyped`、`kysely`、`Zapatos` 等方案相比，pg-typesafe 零额外冗长，更贴近原生 pg 风格

---

### [](https://visual-json.dev/)

**原文标题**: [visual-json | The Visual JSON Editor for Humans](https://visual-json.dev/)

这是一个名为 my-app 的 Next.js 项目配置，版本为 1.0.0，属于私有项目，包含常用脚本、核心依赖及开发依赖，并指定了 Node.js 版本要求。

- 📦 项目名称 my-app，版本 1.0.0，标记为私有
- ⚙️ 脚本命令：dev 启动开发、build 构建、start 启动生产、lint 代码检查
- 🔗 核心依赖：Next.js ^15.0.0、React ^19.0.0、React-DOM ^19.0.0
- 🛠️ 开发依赖：TypeScript ^5.6.0、ESLint ^9.0.0、@types/react ^19.0.0
- 🚀 引擎要求：Node.js 版本需大于等于 18

---

### [获取失败](https://recs.page/web-tools-weekly?ref_code=fde5b5c207&lc=link_campaign_d8b9780aafe8&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recs.page/web-tools-weekly?ref_code=fde5b5c207&lc=link_campaign_d8b9780aafe8&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [获取失败](https://sql.studio/)

**原文标题**: [Failed to retrieve](https://sql.studio/)

无法总结：获取内容失败，状态码 525。

---

### [](https://github.com/taleshape-com/shaper)

**原文标题**: [GitHub - taleshape-com/shaper: Visualize and share your data. All in SQL. Powered by DuckDB. · GitHub](https://github.com/taleshape-com/shaper)

overview summary
Shaper 是一个开源、SQL 优先的数据分析与仪表盘平台，旨在通过编写 SQL 快速构建仪表盘、报表和客户分析，支持自托管和托管服务，并提供了丰富的可视化、安全与集成特性。

- 🚀 开源项目，采用 MPL-2.0 许可证，可自托管，拥有 1.2k Stars。
- 💡 SQL 优先设计，只需简单 SQL 查询即可创建可视化图表（如分类柱状图、时序曲线等）。
- 🔄 支持跨多个数据源查询，并基于 Git 工作流实现版本控制和团队协作。
- 🔐 提供行级安全机制（通过 JWT 令牌）和白标定制，满足企业级需求。
- 📊 支持嵌入式分析，可通过 JS/React SDK 轻松嵌入页面，而无需 iframe。
- 📧 自动生成 PDF、PNG、CSV 和 Excel 报表，支持定时警报及可分享的密码保护链接。
- 🐳 快速启动：运行 Docker 容器 `docker run --rm -it -p5454:5454 taleshape/shaper`，然后访问 `http://localhost:5454/new`。
- ☁️ 提供托管计划和专家支持，可部署在云端或客户自有基础设施，并负责更新、安全与监控。
- 🤝 开放贡献，提供贡献指南，并通过 GitHub Releases 发布更新记录。

---

### [](https://github.com/toon-format/toon)

**原文标题**: [GitHub - toon-format/toon: 🎒 Token-Oriented Object Notation (TOON) – compact, human-readable serialization of JSON data for LLM prompts. TypeScript SDK, CLI, benchmarks. · GitHub](https://github.com/toon-format/toon)

overview summary
TOON（Token-Oriented Object Notation）是一种面向 LLM 的紧凑型 JSON 序列化格式，通过缩进和表格化结构显著减少 token 消耗，同时保持高精度；适合统一结构数据，并提供了完善的工具链与多语言实现。

- 📦 TOON 是 JSON 数据模型的紧凑可读编码，作为 JSON 与 LLM 之间的转换层，无损且可直接替换。
- 🧠 核心优势：相比格式化 JSON 减少约 42.6% 的 token，同时检索准确率（72.2%）略高于 JSON（71.4%）。
- 📐 结合 YAML 缩进与 CSV 表格形式，支持四种形式：内联、表格、键控表格和列表，统一数组对象可折叠成表格。
- ⚠️ 不适用场景：深度嵌套、非均匀结构、半均匀数组、纯表格数据（CSV 更小）或延迟敏感场景。
- 📊 基准测试：混合结构上 TOON 效率最高（29.2 acc%/1K tok），扁平数据比 CSV 多约 5.9% token，但强于 JSON/YAML/XML。
- 🛠️ 提供 TypeScript SDK 和 CLI，支持 JSON↔TOON 转换、流式编码（encodeLines）、replacer 自定义等。
- 🌐 多语言生态：Python、Rust、Go、Java、Swift、.NET 等实现，并有 VS Code、Neovim 等编辑器插件。
- 🏷️ 文件扩展名为.toon，媒体类型为 text/toon，始终 UTF-8 编码；官方规范文档齐全。
- ⭐ 项目在 GitHub 上拥有 25.1k stars、1.1k forks，采用 MIT 许可，由 Johann Schopplich 维护。

---

### [](https://github.com/tinqerjs/tinqer)

**原文标题**: [GitHub - tinqerjs/tinqer: An unfaithful port of Linq to Sql to Typescript · GitHub](https://github.com/tinqerjs/tinqer)

Tinqer 是一个类型安全的 TypeScript 查询构建器，灵感来自 .NET LINQ，通过解析内联箭头函数生成 SQL，支持 PostgreSQL 和 SQLite，提供 CRUD、连接、聚合、窗口函数和全文搜索等完整功能。

- 📦 核心特性：Tinqer 是类型安全的 TypeScript 查询构建器，将内联箭头函数解析为表达式树并编译为 SQL，支持 PostgreSQL 和 SQLite
- 🚀 快速开始：安装 @tinqerjs/tinqer 及适配器，使用 createSchema 定义模式，通过 executeSelect 等执行查询
- 🔧 SQL 生成：toSql 函数可生成 SQL 和参数，方便调试和自定义执行
- 🧩 类型安全：基于 TypeScript 泛型，查询结果类型自动推断
- 🔗 查询组合：计划不可变且可组合，支持创建可复用基础查询并分支扩展，参数累积合并
- 🛡️ 行过滤器：通过 withRowFilters 为表附加行级谓词，自动应用于 SELECT/UPDATE/DELETE，实现授权范围控制
- 🤝 连接支持：支持内连接（join）、左外连接（groupJoin + selectMany）和交叉连接，遵循 LINQ 模式
- 📊 分组聚合：groupBy 后可使用 sum、avg、count、min、max 等聚合
- 🪟 窗口函数：支持 ROW_NUMBER、RANK、DENSE_RANK，自动子查询包装以支持对窗口结果过滤
- 🔍 全文搜索：通过 withFts 启用全文搜索，提供 helpers.fts.match 和 rank，适配 PG 和 SQLite
- ♻️ CRUD 操作：支持 insert、update、delete，包括 ON CONFLICT、RETURNING 和自引用更新
- 🔒 自动参数化：所有字面量自动参数化，防止 SQL 注入，外部参数通过 params 对象传递
- 🔤 字符串操作：提供 icontains 等大小写不敏感辅助函数，支持 includes、startsWith 等表达式
- 🗄️ 数据库支持：PostgreSQL 与 SQLite 适配不同，如布尔类型、JSON、窗口函数版本要求等
- ⚖️ 与 LINQ 差异：Lambda 不能捕获外部变量，连接需在构建器内组合，无延迟执行，右/全外连接需手动 SQL
- 📖 文档与许可：提供详细指南和 API 参考，基于 OXC 解析器，MIT 许可证

---

### [联系 Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

**原文标题**: [Contact Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

该内容为 Web Tools Weekly 的广告合作联系说明，提供多种广告方案及联系方式，并区分广告咨询与一般咨询渠道。

- 📢 广告合作需先查看“Advertising Plans”页面了解选项，再发送消息确认当前档期。
- 📝 若有意向或预订广告位，需填写下方表格，包括姓名、邮箱、广告网址及所选广告方案。
- 💼 可选广告方案：顶部广告 + 顶部文字链接、付费产品评测、中部图片广告、文字链接组合、分类列表、广告互换。
- ✉️ 该表格仅用于广告咨询；其他问题或提交工具，请通过 X（推特）、Bluesky 聊天或订阅邮件回复联系。

---

### [Tabstack - 网络数据与浏览器自动化 API](https://tabstack.ai/)

**原文标题**: [Tabstack - Web Data and Browser Automation APIs](https://tabstack.ai/)

overview summary  
Tabstack 提供一套托管 Web API，让开发者通过单一 API 调用即可完成网页数据提取、结构化 JSON 输出、研究问答与浏览器自动化，无需自行管理 LLM、浏览器或数据管线；平台强调隐私（数据不用于训练）、Mozilla 背书，并提供免费试用与多档付费方案。

- 🚀 一个 API 调用搞定网页数据提取与自动化：传入 URL、schema、问题或任务，返回结构化数据、带引用的答案或完成浏览器操作。  
- 🧩 核心端点：`/extract/json`、`/extract/markdown`、`/generate/json`、`/research`、`/automate`，覆盖从抓取到智能体执行的全流程。  
- 📄 `/extract/json` 按用户定义的 schema 返回匹配 JSON，示例：从 Nike 商品页获取名称、价格及每尺寸库存状态。  
- 🧹 `/extract/markdown` 可将任意网页转为干净 Markdown，适合 RAG 或知识库摄入，无需维护爬虫。  
- 🔍 `/research` 在单次 API 调用中运行研究智能体，基于实时网页生成带内联引用的综合答案，并支持 SSE 流式输出。  
- 🤖 `/automate` 用自然语言描述任务，Tabstack 在真实网页上完成导航、点击、填表及多步流程；内置开源浏览器引擎 Pilo，比截图方案节省 60–80% token。  
- 💻 提供 TypeScript、Python SDK、MCP 与 CLI，可快速集成到现有 agent 或技术栈（约 30 秒接入）。  
- 🛠️ 实际应用场景：竞品价格监控、线索丰富、研究型产品、自动预订/结账、工作流自动化、知识库数据摄入。  
- 🔒 隐私与透明：请求页面仅用于完成调用后清除；默认遵守 robots.txt；Mozilla 支持并公开文档化数据实践；数据不会用于训练模型或出售。  
- 💰 定价：新账户含 10,000 免费额度；付费方案 Starter $10/月、Team $99/月、Pro $499/月，另有企业定制；按动作计费，例如 Extract(JSON) 50 额度、Research(Fast) 250 额度。

---

### [](https://www.getcrosstab.com/)

**原文标题**: [Crosstab - Export data from any website in one click](https://www.getcrosstab.com/)

Crosstab 是一个强大的 Chrome 扩展程序，能够将网页浏览转化为可定制的数据集，通过自然语言定义数据、跨页面导出、自动化搜索，并支持多种 AI 模型集成，帮助用户轻松收集和分析数据。

- 🌐 **一键定义数据集**：用自然语言描述你想导出的数据及其结构，即可从任意网站提取内容。
- 📄 **多页面导出**：支持跨多个页面提取数据，并整合为一个数据集。
- 📁 **CSV 导出**：一键导出为 CSV 文件，方便导入其他工具使用。
- 📋 **即时复制**：点击即可将数据复制到剪贴板，快速粘贴到目标位置。
- 🔍 **智能搜索模式**：在任意平台上自动搜索并丰富现有数据，加速研究流程，支持大量数据行的批量处理。
- 🧠 **AI 智能结果**：先进 AI 会为你的提示词从数百行数据中筛选最相关的结果。
- ⚙️ **后台处理**：大型搜索任务可在后台运行，节省等待时间，提高效率。
- 🤖 **即时 AI 集成**：一键将数据发送到 ChatGPT、Claude 或 Grok，并自动格式化输出，便于后续分析。
- 🔄 **工作流扩展**：可进一步将数据发送到 OpenAI、Google Sheets、HubSpot、Airtable、Notion 等数千个平台。
- 💰 **透明定价**：免费版含 10 次导出额度；Plus 每月 $15（500 额度）；Pro 每月 $30（2000 额度）；Teams 每月 $50（5000 额度，含座位管理和优先支持）。
- 🔒 **企业级安全**：遵循 SOC2、HIPAA、GDPR 标准，零数据保留，所有传输数据默认加密。
- ❓ **常见问题支持**：官网提供常见问答，并可联系 info@crosstab.app 咨询定制方案和集成问题。

---

### [PgNative - 适用于 macOS 的快速原生 PostgreSQL 客户端](https://www.pgnative.com/)

**原文标题**: [PgNative - Fast Native PostgreSQL Client for macOS](https://www.pgnative.com/)

overview summary  
PgNative 是一款适用于 Mac 和 Windows 的轻量级原生 PostgreSQL 客户端，主打快速、简洁、无订阅，一次付费永久使用，并提供免费版与 Pro 版（$49）。适合日常 PostgreSQL 工作，并附有相关博客指南。

- 💻 支持 Mac（Apple Silicon 与 Intel）和 Windows，原生轻量，运行快速。
- ⚡ 核心特点：快速查询执行、界面简洁聚焦、无臃肿功能。
- 🔒 数据本地保存，隐私安全；无需订阅，一次购买 $49 永久使用。
- 🎯 目标用户：后端开发者、PostgreSQL 用户、追求简单快速且讨厌订阅制的人群。
- 🆓 提供免费下载与 Pro 购买选项，可在官网获取。
- 📸 网站直接展示应用截图（查询编辑器与表浏览器），不搞轮播图。
- 📝 博客文章涵盖：轻量级 pgAdmin 替代方案、通过 SSL 连接云 Postgres（Supabase、Neon、RDS）、与 TablePlus 的对比等实用指南。

---

### [](https://rork.com/)

**原文标题**: [Rork — create mobile and web apps using AI in minutes](https://rork.com/)

Rork 是一个让使用者透過聊天與 AI 協作來打造 iOS 應用程式、上架 App Store 並獲利的平台，同時推出了可隨時隨地建置與發布 App 的「Rork Max App」，並有年輕創業家的成功案例作為號召。

- 📱 用 AI 聊天就能開發原生 iOS App，並可直接發布至 App Store 開始賺錢
- ⚡ 推出 Rork Max App，讓使用者能在手機上隨時隨地建置、安裝與發布應用程式
- 🏃 兩位 18 歲跑者利用 Rork 在 6 個月內將 App 做到年收入 24 萬美元（月收入約 2 萬美元）
- 🎯 提供入門指南、教學文件、常見問題與部落格等豐富資源，協助使用者打造真實應用
- 🌟 設有創辦者故事、Rork Stars 與聯盟計畫等社群與推廣管道
- 💖 由舊金山、第比利斯與倫敦團隊打造，並提供服務條款、隱私政策與隱私選擇等說明

---

### [](https://www.usetusk.ai/)

**原文标题**: [AI Testing Platform | API, Unit & Integration Testing - Tusk](https://www.usetusk.ai/)

Tusk 是一个面向编码代理的 AI 验证层，通过分析生产流量和业务上下文自动生成测试用例与代码审查，帮助团队在合并代码前捕获回归缺陷、提升覆盖率，并显著加速发布周期，同时保持工程师工作流不被干扰。

- 🛡️ 作为编码代理的 AI 验证层，有效防止 bug 与质量问题，让团队放心使用自动化编码工具
- 📡 基于实时生产流量和业务上下文生成测试用例，可在 43% 的 PR 中捕获真实回归问题
- ⚙️ 提供代码审查、单元测试、API 测试及 CoverBot 等核心功能，全面覆盖质量保障环节
- 🚀 支持单命令 CLI 安装与自动设置，专为代理优化，可在本地或 CI 中无缝运行
- 🤖 完全自主迭代测试脚本，遇到错误自动修复，无需人工往返调试
- 🔄 测试具备自愈能力，每次提交自动维护现有测试套件，始终匹配最新业务逻辑
- 🎯 适用于回归测试、安全重构、API 契约监控等关键场景，精准覆盖盲区
- 📈 帮助团队快速达成覆盖率目标，案例显示测试数量从 2,500 增至 7,000+，效果显著
- ⭐ 深受 DeepLearning.AI、Hamming、Promptfoo 等快速成长公司工程领导者的信赖与推荐

---

### [](https://x.com/shadcn/status/2085163855408214356)

**原文标题**: [shadcn on X: "Alright. I want you to read this.

Earlier today, I released a new component.

What you see is the finished result.

What you don’t see are the days of planning, research, testing, designing, simplifying, throwing ideas away, and trying again before I felt it was ready.

Within" / X](https://x.com/shadcn/status/2085163855408214356)

shadcn 分享了自己发布新组件后迅速被 AI 复制移植的体验，并由此引发对创造力、抄袭成本与 AI 时代创作激励的深刻反思。他强调，当复制变得几乎免费且即时，小型创意作品的生存空间将被挤压，进而威胁整个创新生态；同时，作为 AI 的早期使用者，我们的选择将塑造未来所有创意领域的默认规则。

- 🧩 发布新组件后，成品虽看起来简单，但背后是数日的规划、研究、测试与迭代，而这些努力在几小时内就被 AI 复制并移植到其他框架。
- ⚠️ 这次被复制的是开源作品，尚可接受；但如果这是某人的第一件产品，甚至第五件、第十件，当新想法立刻沦为提示词，创意者的尊严与收益将荡然无存。
- 💭 当“执行得更快”“规模更大”或“想得更宽”都不再是护城河时，创意和执行都变得廉价，那么谁还愿意承担创造性的初始成本？
- 🔄 复制本身不新鲜，但如此高速、低成本、大规模的复制是全新的；过去复制需要理解与努力，反而带来对原作者的敬意，如今这种敬意消失了。
- 🌱 创造力始于小步尝试，如果第一步就注定被无意义地复制，我们失去的不仅是小产品，更是未来可能创造出伟大作品的人。
- 🧭 作为 AI 技术的先行者，我们的使用方式将定义全球默认规范，这种影响会扩散到写作、设计、音乐、研究等一切需要首次创意风险的领域。
- ⚖️ 最终的选择在于我们：用 AI 建造更伟大的事物，还是用它把每一个新想法拆解成可抄袭的零件；这个决定将塑造整个创意生态的未来。
- 💬 评论者也指出：这正是艺术家们曾遭受的困境——作品被用于训练图像模型；同时，分享时应提及原作，保持社交连系与尊重。

---

### [](https://x.com/LouisLazaris)

**原文标题**: [Louis Lazaris (@LouisLazaris) / X](https://x.com/LouisLazaris)

Louis Lazaris 在社交媒体上分享了他近期编辑的三份技术电子报内容，涵盖 Web 开发工具、技术生产力和 VS Code 插件等主题。

- 📌 Louis Lazaris 是一位加拿大博主，自称“无聊主席”，运营三份电子报：Web Tools Weekly、Tech Productivity 和 VSCode.Email。
- ⚽️ Tech Productivity #390：涉及梅西跑动分析、GitHub 求职追踪工具、现代求职误区，以及公司扁平层级的管理方式。
- 📦 Web Tools Weekly #679：包含 Web 框架与组件库、测试与调试工具、Git/GitHub 及 CLI 工具。
- 🏗️ Web Tools Weekly #678：聚焦 JavaScript 库与框架、构建工具及 AI 工具。
- 🔢 VSCode.Email #221：介绍二进制十六进制查看扩展、浆果风格主题、VS Code 默认安全变更，以及一篇“Vim 悼文”。
- 🐙 VSCode.Email #220：涵盖 GitHub Markdown 预览、5 万次 eval 实验的启示、VS Code 中 GitHub Copilot 的浏览器工具，以及带 Vim 键绑定的终端电子表格编辑器。

---

### [](https://bsky.app/profile/louislazaris.com)

**原文标题**: [@louislazaris.com on Bluesky](https://bsky.app/profile/louislazaris.com)

概述：这是 Bluesky 平台上一位前端开发者 Louis Lazaris 的个人资料简介，列出了他的职业身份及相关网站链接。

- 👨‍💻 他是前端开发者和新闻通讯策展人，主要服务于 Web 开发领域。
- ⚙️ 维护 Web 工具周报网站（webtoolsweekly.com），专注分享前端工具资源。
- 💼 运营技术生产力网站（techproductivity.co），聚焦效率与工具应用。
- 💻 提供 VS Code 相关邮件资讯服务（vscode.email），覆盖编辑器技巧与插件。
- 🎸 在 YouTube 开设吉他教学频道（@tunejotter），面向吉他爱好者分享内容。
- 🌐 个人主页（louislazaris.com）汇集其所有作品与简介，并附有 AT Protocol 身份标识。

---

### [](https://webtoolsweekly.com/submit)

**原文标题**: [Submit a Tool to Web Tools Weekly](https://webtoolsweekly.com/submit)

概述：这是一个面向前端开发者的工具提交指南，说明了提交渠道、可接受的工具类型以及注意事项。

- 📮 可通过 X（@LouisLazaris）或 Bluesky（@LouisLazaris.com）私信提交工具
- 🧩 接受库、框架、插件、脚本、Web 应用、桌面应用、移动应用、API/服务、编辑器/IDE 等各类工具
- 🚫 不接受文章或教程类投稿
- 📋 生产力相关工具请改投至另一份通讯《Tech Productivity》，也可用相同渠道提交

---

### [](https://github.com/davmlaw/they_live_adblocker)

**原文标题**: [GitHub - davmlaw/they_live_adblocker: Replace Ads with They Live style slogans · GitHub](https://github.com/davmlaw/they_live_adblocker)

《They Live Adblocker》是一个基于 uBO Lite 的趣味分支项目，它没有直接隐藏被拦截的广告，而是用 1988 年电影《They Live》中的标语白色方块将其替换，借此传达反消费主义讽刺意味。

- 🔀 这是 uBlock Origin Lite 的一个非官方 fork，核心改动是将“被隐藏的广告”变成带有电影《They Live》标语的白色占位块
- 📝 标语随机选一条显示，如 OBEY、CONSUME、WATCH TV、SLEEP、SUBUMIT、CONFORM 等，每个被处理的广告只配一句
- 📥 安装过程：从 Releases 下载 `uBOLite_theylive.chromium.zip`，解压后打开 `chrome://extensions`，启用“开发者模式”，点击“加载已解压的扩展程序”选择文件夹
- ⚙️ 默认的“基础”过滤模式只在网络层拦截广告，不会产生可替换的元素，因此必须将网站的过滤模式设为 **Optimal** 或 **Complete**，才能看到 OBEY 标语效果
- 🛠 源码构建需要 Node 22，使用 `git clone --recursive` 拉取子模块，然后在 `uBlock` 目录运行 `tools/make-mv3.sh chromium`（也可指定 firefox/edge/safari）
- 🧩 实现原理：fork 修改了 uBO Lite 的 CSS 注入点，用白底遮罩配合 `::after` 伪元素显示标语，同时用 MutationObserver 监听动态加载的广告并给元素随机标记短语
- ⚠️ 注意：这是个人爱好项目，不是官方 uBO 产品；部分站点可能因广告位被强制显示而出现布局偏移；用户自定义的隐藏规则仍会正常隐藏，不会变成标语
- 📜 许可证为 GPL-3.0，与上游 uBlock Origin / uBO Lite 一致

---

### [](https://webtoolsweekly.com/)

**原文标题**: [Web Tools Weekly | A Weekly Newsletter for Front-end Developers](https://webtoolsweekly.com/)

这是关于 Web Tools Weekly 新闻通讯的介绍，包含订阅信息、隐私政策说明以及多位读者的好评推荐。

- 📧 每周发送一封邮件，目前有 14,101 位订阅者。
- 🔒 承诺无垃圾邮件，并明确数据收集与使用政策，需同意条款。
- 🛡️ 网站受 reCAPTCHA 保护，适用 Google 隐私政策和服务条款。
- ⭐ 多年来收到大量读者自发好评，认为它通过了“awesome”测试。
- 🧰 读者称赞其精选的 Web 开发工具和库，能帮助前端开发者保持更新。
- 💡 每期附带 JavaScript 技巧，提供意想不到的实用建议。
- 🗓️ 许多读者长期订阅，每周期待，认为是最有用的技术汇总之一。
- 🙌 读者普遍感谢编者工作，称其为“杀手级”新闻通讯。

---

