### [GitHub - cloudflare/agentic-inbox：一款带有AI代理的自托管邮件客户端，完全运行于Cloudflare Workers 之上](https://github.com/cloudflare/agentic-inbox)

**原文标题**: [GitHub - cloudflare/agentic-inbox: A self-hosted email client with an AI agent, running entirely on Cloudflare Workers · GitHub](https://github.com/cloudflare/agentic-inbox)

Agentic Inbox 是一个完全运行在 Cloudflare Workers 上的自托管邮件客户端，集成了 AI 智能代理，支持收发邮件、独立邮箱隔离和 AI 辅助功能。

- 📧 **完整邮件客户端** — 通过 Cloudflare Email Routing 收发邮件，支持富文本编辑器、回复/转发线程、文件夹管理、搜索和附件功能
- 🗂️ **独立邮箱隔离** — 每个邮箱运行在独立的 Durable Object 中，使用 SQLite 存储和 R2 管理附件
- 🤖 **内置 AI 代理** — 侧边面板集成 9 种邮件工具，可阅读、搜索、草拟和发送邮件，使用 Cloudflare Agents SDK 和 Workers AI 构建
- ✍️ **自动草稿功能** — AI 代理自动读取新邮件并生成回复草稿，发送前需用户明确确认
- ⚙️ **可配置且持久化** — 支持每个邮箱自定义系统提示、持久聊天历史、流式 Markdown 响应和工具调用可见性
- 🛡️ **安全认证** — 强制使用 Cloudflare Access 进行 JWT 验证，确保邮箱不暴露于公网
- 🏗️ **技术栈** — 前端使用 React 19、React Router v7、Tailwind CSS 等；后端基于 Hono、Cloudflare Workers、Durable Objects 和 R2；AI 代理使用 Cloudflare Agents SDK 和 Workers AI
- 🚀 **部署简便** — 一键部署到 Cloudflare，自动配置 R2、Durable Objects 和 Workers AI，需额外设置 Email Routing 和 Email Service
- 🔧 **架构清晰** — 浏览器通过 Hono Worker 与 MailboxDO 和 EmailAgent DO 交互，支持 WebSocket 连接，实现高效通信

---

### [调试 Next.JS 最佳实践：日志与追踪 | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-nextjsworkshop&utm_content=newsletter-primary-register)

**原文标题**: [Debugging Next.JS Best Practices: Logs and Tracing | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-nextjsworkshop&utm_content=newsletter-primary-register)

本研讨会聚焦于 Next.js 应用在生产环境中的调试最佳实践，涵盖日志记录、追踪和错误排查。

- 🛠️ 研讨会主题：调试 Next.js 最佳实践，包括日志与追踪
- ❓ 挑战：生产环境中难以定位问题根源，如 hydration 错误、服务端组件失败和性能瓶颈
- 📝 内容一：编写高上下文日志，记录失败原因、用户、操作和背景
- 🔍 内容二：查询和设置日志告警，捕获认证、支付、webhook 和第三方 API 调用中的静默失败
- 🔗 内容三：深入分布式追踪，覆盖客户端和 Node 运行时
- 🔄 内容四：将日志与追踪连接，无需切换工具即可获得完整上下文
- 📚 额外资源：包括 Sentry 入门指南、AI 代理与 MCP 服务器构建研讨会，以及 Next.js 日志简化文章

---

### [React 如何无序流式输出 UI 却依然保持有序 | React 内部探秘](https://inside-react.vercel.app/blog/how-react-streams-ui-out-of-order)

**原文标题**: [How React streams UI out of order and still manages to keep order | Inside React](https://inside-react.vercel.app/blog/how-react-streams-ui-out-of-order)

## 概述总结
React 通过 Suspense 边界实现无序流式传输，先发送立即可用的 HTML，用占位符标记未就绪组件，待数据就绪后通过 JavaScript 脚本将隐藏的组件内容替换到正确位置。

- 🚀 **React 18+ 支持无序流式传输**：React 18 引入`renderToPipeableStream()`，React 19 稳定了服务端组件，允许组件按数据就绪顺序而非 HTML 顺序流式传输。
- ⏳ **传统 SSR 的阻塞问题**：即使并行请求数据，页面仍需等待所有组件完成才发送 HTML，导致导航栏和页脚等无关组件被阻塞。
- 📦 **有序流式传输的局限**：组件按 HTML 顺序流式传输，慢组件仍会阻塞后续组件（如推荐组件阻塞页脚）。
- 🔄 **无序流式传输的原理**：用`<Suspense>`包裹慢组件，立即发送导航栏和页脚，用`<template>`占位符标记慢组件位置，数据就绪后通过 JavaScript 替换。
- 🧩 **HTML 流中的 Suspense 标记**：`<!--$?-->`表示待定状态，`<template id="B:0">`是占位符，`<div>loading..</div>`是回退 UI。
- 🛠️ **客户端替换机制**：服务器将就绪组件渲染为隐藏`<div>`（如`id="S:0"`），随后发送`<script>$RC("B:0","S:0")</script>`触发替换。
- 🔄 **生命周期状态机**：Suspense 边界经历`$?`（待定）→`$~`（排队等待 RAF）→`$`（完成）三个阶段，确保 DOM 正确更新。
- ⚠️ **潜在风险**：若手动插入相同 ID 的`<template>`，React 会错误替换，说明该机制依赖 DOM ID 的唯一性。

---

### [Remix 3 测试版预览 | Remix](https://remix.run/blog/remix-3-beta-preview)

**原文标题**: [Remix 3 Beta Preview | Remix](https://remix.run/blog/remix-3-beta-preview)

Remix 3 测试版预览发布，这是一个更简单、更快速、更贴近 Web 本身的全栈框架，强调可组合性与开发者体验。

- 🚀 Remix 3 测试版发布，但尚未生产就绪，欢迎反馈问题
- 🧩 从“中心栈”转向“全栈”，涵盖路由、请求、中间件、认证、表单、上传、数据、UI 等
- 🌐 路由基于 Fetch API，控制器返回响应，中间件管理请求生命周期，表单提交到 URL
- 🖼️ 引入“帧”（Frame）概念，实现服务器渲染的独立 UI 片段，支持客户端独立加载和导航
- 📝 组件采用过程式风格，状态和异步行为直观可见，支持可组合的 mixin
- 🎯 “去捆绑化”理念：运行时为真相源，不依赖预分析，对人和 AI 代理更友好
- 🔧 减少外部依赖，内置路由、会话、认证、表单、上传、静态文件、数据、UI 等核心功能
- 🧪 可通过 `npx remix@next new my-remix-app` 快速开始体验和反馈

---

### [未找到标题](https://x.com/KevinVanCott/status/2049151097042837841)

**原文标题**: [No title found](https://x.com/KevinVanCott/status/2049151097042837841)

此页面提示浏览器需启用 JavaScript 才能正常访问 x.com，并提供了相关帮助与政策信息。

- 🔒 检测到浏览器 JavaScript 被禁用，需启用或切换至支持的浏览器
- 🌐 可通过帮助中心查看支持的浏览器列表
- 📜 页面底部包含服务条款、隐私政策、Cookie 政策等法律文件链接
- ⚠️ 可能因隐私相关扩展导致访问异常，建议禁用后重试
- 🔄 提供“重试”按钮以应对临时加载问题

---

### [RFC: (iOS) React Native 中的 Swift 包管理器（Cocoapods 弃用）—— 作者：chrfalch · 拉取请求 #994 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/994)

**原文标题**: [RFC: (iOS) Swift Package Manager in React Native (Cocoapods deprecation) by chrfalch · Pull Request #994 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/994)

此 RFC 提案在 React Native iOS 项目中以 Swift Package Manager (SPM) 取代 CocoaPods，並獲得社群廣泛支持。

- 📄 **RFC 核心目標**：提出在 React Native iOS 專案中，逐步淘汰 CocoaPods，並以 Swift Package Manager (SPM) 作為替代方案。
- 🚀 **社群反應熱烈**：此提案獲得大量 👍、🎉、❤️、🚀 等表情符號的反應，顯示社群對此方向充滿期待。
- ⚙️ **自動連結機制**：透過 `setup-ios-spm.js` 腳本自動化處理相依性，包括執行 Codegen、生成 `autolinked/Package.swift`、下載預建 XCFramework，並建立 Xcode 專案。
- 🧩 **本地模組支援**：透過 `react-native.config.js` 中的 `spmModules` 設定，支援額外的本地原生模組整合。
- 🔄 **自動同步建置階段**：新增自動同步的建置階段，可在編譯前偵測相依性變更並重新產生自動連結的套件。
- ⚠️ **Swift 與 C++ 混用限制**：SPM 目前不支援在同一個 target 中混用 Swift 與 C++，這將影響基於此特性的函式庫（如 Nitro Modules、react-native-vision-camera 等），團隊正在尋找解決方案。
- 🏗️ **從原始碼建置**：最終版本將支援從原始碼建置 React Native，但目前的 POC 版本尚未支援。
- 🟤 **Brownfield 專案支援**：Brownfield 專案可透過 `Package.swift` 檔案整合，CLI 將提供選項來產生用於分發的獨立 `Package.swift` 檔案。
- 🔗 **靜態與動態框架**：SPM 支援在 `Package.swift` 中引用預建的 XCFramework 和原始碼檔案，提供框架連結的靈活性。
- 📝 **腳本鉤子**：SPM 的套件解析階段可執行自訂腳本，作為 `pod install` 的替代方案，用於執行設定或驗證等任務。

---

### [React Native 动画的真实成本：每种方法的基准测试](https://expo.dev/blog/the-real-cost-of-react-native-animations-benchmarking-every-approach)

**原文标题**: [The real cost of React Native animations: benchmarking every approach](https://expo.dev/blog/the-real-cost-of-react-native-animations-benchmarking-every-approach)

概述：本文讨论了人工智能在医疗领域的应用，强调了其提升诊断准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🩺 人工智能可辅助医生进行更精准的疾病诊断，例如通过分析医学影像识别早期肿瘤。
- 📊 机器学习算法能快速处理大量患者数据，帮助预测疾病风险和个性化治疗方案。
- 🔒 数据隐私问题需重点关注，确保患者信息在 AI 系统中得到安全保护。
- ⚖️ 算法偏见可能导致医疗不平等，需通过多样化训练数据来减少偏差。
- 💡 未来 AI 与医疗专家协作，有望优化资源分配并降低医疗成本。

---

### [React 中的无障碍性：常见错误及修复方法 - Certificates.dev](https://certificates.dev/blog/accessibility-in-react-common-mistakes-and-how-to-fix-them)

**原文标题**: [Accessibility in React: Common Mistakes and How to Fix Them - Certificates.dev](https://certificates.dev/blog/accessibility-in-react-common-mistakes-and-how-to-fix-them)

本篇文章探讨了 React 应用中常见的无障碍性（a11y）错误及其修复方法，重点涵盖语义缺失、焦点管理混乱、未标记元素和动态更新无声等问题，并提供了快速审核清单。

- 🔍 **使用正确的 HTML 元素**：用`<button>`替代`<div onClick>`，用`<a href>`进行导航，避免重复实现浏览器自带功能。
- 📑 **维护文档结构与标题层级**：按逻辑顺序使用`<h1>`到`<h6>`，并利用`<header>`、`<nav>`、`<main>`等地标元素帮助屏幕阅读器导航。
- 🏷️ **为所有交互元素添加标签**：表单输入需配`<label>`，图标按钮用`aria-label`或视觉隐藏文本，图片必须包含`alt`属性。
- 🔗 **使用`useId`连接标签和错误信息**：通过`aria-describedby`和`aria-invalid`将错误消息与输入框关联，并保持`role="alert"`容器常驻 DOM。
- 🎯 **管理焦点**：页面切换时用`tabIndex={-1}`将焦点移至新内容，模态框使用原生`<dialog>`自动处理焦点捕获和 Escape 关闭。
- 📢 **宣布动态更新**：使用`role="alert"`（紧急）或`role="status"`（非紧急）让屏幕阅读器读取变化，避免条件渲染导致无声更新。
- 🎨 **基于 ARIA 属性设置样式**：利用`aria-selected`、`aria-disabled`等属性直接应用 CSS 样式，减少对额外状态变量的依赖。
- ✅ **快速审核清单**：检查`<div>`点击事件、标题层级、表单标签、图标按钮、图片 alt、错误连接、模态焦点、条件渲染和动态更新，并通过 Tab 键和自动化工具（如 axe-core）测试。

---

### [在移动端何时使用 Apple 基础模型](https://www.callstack.com/blog/when-to-use-apple-foundation-models-on-mobile)

**原文标题**: [When to Use Apple Foundation Models on Mobile](https://www.callstack.com/blog/when-to-use-apple-foundation-models-on-mobile)

Apple 的 Foundation Models 框架为移动端 AI 提供实用的本地默认方案，但不应替代云端模型。以下是关键要点：

- 📱 **本地模型适用场景**：短提示和短输出、低延迟敏感、仅需本地上下文、离线可用、处理个人数据的任务，如文本重写、标题生成、结构化提取和轻量分类。
- ❌ **不适用场景**：需要长上下文窗口、多文档推理、工具调用、跨平台一致性、深度推理或依赖远程知识的任务，如复杂编码辅助。
- 🎯 **混合策略更优**：采用“本地优先”而非“仅设备”策略，本地处理简单频繁任务，云端处理复杂高质量任务，如 ChatXOS 应用案例。
- ⚙️ **React Native 集成模式**：通过`apple.isAvailable()`检查可用性，显式路由模型选择，流式输出 UI，支持取消操作，确保用户体验。
- 🔄 **第三方模型考量**：可下载第三方模型扩展能力，但需权衡模型打包、存储、更新、内存和兼容性等产品交付成本。

---

### [获取失败](https://www.npmjs.com/package/@react-native-ai/apple)

**原文标题**: [Failed to retrieve](https://www.npmjs.com/package/@react-native-ai/apple)

无法总结：获取内容失败，状态码 403。

---

### [使用 React 服务器组件进行部分页面缓存 - YouTube](https://www.youtube.com/watch?v=t9xB8xvySyo)

**原文标题**: [Partial Page Caching Using React Server Components - YouTube](https://www.youtube.com/watch?v=t9xB8xvySyo)

本頁面列出了 YouTube 平台的主要資訊與政策連結，涵蓋使用條款、版權、隱私及合作機會等核心內容。

- 📰 新聞中心：提供 YouTube 官方公告與最新消息
- ©️ 版權：說明內容創作者的版權保護與管理機制
- 📞 聯絡我們：提供使用者與平台聯繫的管道
- 🎨 創作者：針對內容創作者提供的資源與支援
- 📢 刊登廣告：說明廣告主如何在 YouTube 投放廣告
- 👨‍💻 開發人員：提供 API 與技術整合的開發者資源
- 📜 條款：列出使用 YouTube 服務的規範與協議
- 🔒 私隱：說明個人資料的收集、使用與保護方式
- 🛡️ 政策及安全：強調平台的安全政策與使用者保護措施
- ⚙️ YouTube 的運作方式：解釋推薦系統、內容審核等平台機制
- 🧪 測試新功能：介紹 YouTube 正在測試的新功能與實驗
- 🏢 版權所有：標示 YouTube 屬於 Google LLC（© 2026）

---

### [让蓝牙低功耗与 JavaScript 协同工作 - DEV 社区](https://dev.to/blackscripts/making-bluetooth-low-energy-work-with-javascript-1b5n)

**原文标题**: [Making Bluetooth Low Energy Work with JavaScript - DEV Community](https://dev.to/blackscripts/making-bluetooth-low-energy-work-with-javascript-1b5n)

本文探讨了在 JavaScript（特别是 React Native）中实现蓝牙低功耗（BLE）功能的挑战与解决方案，以自行车追踪器 BikeMesh 为例，从硬件固件决策到应用层 UI 设计，提供了完整的实践指南。

- 📡 **硬件决策是关键**：将 BLE 芯片从“配对聊天”模式改为“广播喊话”模式（iBeacon），是后续所有软件工作的基础，决定了跨平台兼容性和后台扫描能力。
- ⚙️ **权限配置易忽略**：iOS 需在 Info.plist 中添加蓝牙使用说明，否则应用静默崩溃；Android 12+ 需申请三个运行时权限（包括位置权限），遗漏则扫描无结果。
- 🔍 **数据解析需手动**：BLE 返回的是原始字节包，需自行解析 iBeacon 格式（公司 ID、UUID 等），JavaScript 需处理位运算和十六进制操作，并非高级 API。
- 🆔 **身份标识放载荷**：iOS 不暴露设备 MAC 地址，因此应将唯一标识（如 UUID）放在广播数据载荷中，而非依赖操作系统提供的设备 ID，以确保跨平台一致性。
- 📊 **信号强度会撒谎**：RSSI 值波动剧烈（可达 20 dBm），不应直接显示数字。建议将信号分为 6 个区间（如“很近”“近”等），配合颜色变化和触觉反馈，提供更稳定的用户体验。
- 🔋 **后台扫描有技巧**：iOS 限制后台持续扫描，但 iBeacon 的区域监控功能可让系统在后台自动唤醒应用，这是选择 iBeacon 格式的隐藏优势。
- 🔒 **安全风险需警惕**：iBeacon 广播无加密，存在被追踪和伪造的风险。静态 UUID 是隐私漏洞，可通过轮换标识或 HMAC 签名缓解；切勿在 JavaScript 包中存储敏感密钥。
- 🗺️ **GPS 与 BLE 协同**：BLE 仅提供近距离定位（米级），GPS 负责远距离定位（街道级）。当手机检测到 iBeacon 时，记录 GPS 坐标作为最后位置，用户靠近后再用 BLE 引导至具体物体。
- 🎯 **应用场景广泛**：该架构适用于资产追踪、室内导航、近距解锁、活动签到、零售触发、安全监护等产品，核心模式相同，仅产品层实现不同。

---

### [第一部分：如何在 React Native 中让纯 JSI 代码更快](https://blog.margelo.com/make-jsi-run-faster)

**原文标题**: [Part 1: How to Make Pure JSI Code Faster in React Native](https://blog.margelo.com/make-jsi-run-faster)

### 概述总结
本文探讨了在 JSI 代码中通过架构选择和内存优化，将性能提升 2-10 倍的关键技巧，并提供了具体基准测试数据。

- 📊 **HostFunction vs HostObject**：直接使用`HostFunction`比通过`HostObject`暴露函数快约 5 倍，因为避免了每次调用的属性解析开销（虚拟调度、字符串转换等）。
- 🔍 **NativeState vs HostObject**：使用`jsi::NativeState`替代`HostObject`管理状态，同样快约 5 倍，消除了动态属性解析层，直接访问原生指针。
- ⚡ **栈分配 vs 堆分配**：当字符串大小已知（如<512 字节）时，使用`char buf[256]`栈缓冲区比`std::string`快约 3 倍，避免堆分配和间接开销。
- 🎯 **选择正确的字符串构造函数**：根据数据格式选择`createFromAscii`、`createFromUtf8`或`createFromUtf16`，避免不必要的转换和扫描。
- 🔧 **减少 JS↔C++ 边界穿越**：合并多次小调用为一次大调用，减少边界穿越次数（参数验证、值转换等），这是热路径上的关键优化。
- 💡 **Nitro Modules 内置优化**：该框架已自动实现`NativeState`替代`HostObject`、缓存`PropNameID`、哈希分发等优化，减少手动工作。
- 🏆 **最终建议**：优先选择正确架构（如直接`HostFunction`、栈分配），再考虑微优化；热路径上的小决策能带来显著性能差异。

---

### [GitHub - vercel-labs/portless：用稳定的、命名的本地URL替换端口号。适用于人类和智能体。](https://github.com/vercel-labs/portless)

**原文标题**: [GitHub - vercel-labs/portless: Replace port numbers with stable, named local URLs. For humans and agents. · GitHub](https://github.com/vercel-labs/portless)

Portless 是一个将本地开发端口替换为稳定、命名的 .localhost URL 的工具，适用于人类和 AI 代理。

- 🚀 用 `portless run next dev` 替代 `next dev`，即可通过 `https://myapp.localhost` 访问应用，支持 HTTPS 和 HTTP/2
- ⚙️ 自动分配端口、生成本地 CA 证书并信任，首次运行无需手动配置
- 🔧 支持单仓库和 monorepo，通过 `portless.json` 或 `package.json` 中的 `"portless"` 键进行配置
- 🌐 提供子域名支持（如 `api.myapp.localhost`），并自动检测 Git 工作树分配唯一子域名
- 🛡️ 默认启用 HTTPS，支持自定义 TLS 证书、自定义 TLD（如 `.test`）和 LAN 模式（mDNS 发现）
- 🔗 与 Tailscale 集成，可通过 `--tailscale` 或 `--funnel` 将开发服务器分享到 Tailnet 或公网
- 📋 包含丰富命令：`portless list` 查看路由、`portless trust` 信任 CA、`portless clean` 清理状态等
- 🧩 自动处理框架兼容性（Next.js、Vite、Expo 等），并注入 `PORT`、`HOST` 等环境变量
- 🛑 非交互环境（如 CI）中直接报错退出，避免卡住任务运行器
- 🧹 支持通过 `PORTLESS=0` 绕过代理，以及清理孤儿进程和 hosts 文件

---

### [发布 v0.12.0 · vercel-labs/portless · GitHub](https://github.com/vercel-labs/portless/releases/tag/v0.12.0)

**原文标题**: [Release v0.12.0 · vercel-labs/portless · GitHub](https://github.com/vercel-labs/portless/releases/tag/v0.12.0)

### 概述总结
Portless v0.12.0 发布，新增 Tailscale 集成功能，允许通过 Tailscale 网络或公网共享应用，并改进了清理机制。

- 🚀 **Tailscale 共享**：新增 `--tailscale` 标志，可将应用通过 Tailscale 网络共享，每个应用自动分配独立 HTTPS 端口，无需额外配置。
- 🌐 **Tailscale Funnel**：新增 `--funnel` 标志，通过 Tailscale Funnel 将应用暴露至公网，自动启用 Tailscale 共享。
- 🔗 **环境变量支持**：子进程会收到 `PORTLESS_TAILSCALE_URL` 环境变量，包含应用的 Tailscale HTTPS 地址。
- 📋 **列表显示优化**：`portless list` 命令在 Tailscale 共享激活时，同时显示本地 URL 和 Tailnet URL。
- 🧹 **清理机制增强**：`portless prune` 可清除失效的 Tailscale 注册条目，`portless clean` 则移除 Tailscale serve/funnel 相关状态。
- 👥 **贡献者**：本次更新由 @ctate 贡献。

---

### [React 热键钩子](https://react-hotkeys-hook.vercel.app/)

**原文标题**: [React Hotkeys Hook](https://react-hotkeys-hook.vercel.app/)

本演示展示了 react-hotkeys-hook 库的核心功能，通过实时可编辑的代码示例，让用户直观体验键盘快捷键的绑定与管理。

- 🎮 **实时交互演示**：点击预览面板后按 `N` 键即可添加新任务，代码修改后立即生效
- 🚀 **简洁声明式 API**：通过单个 `useHotkeys` 钩子定义快捷键，无需复杂配置或包装组件
- 🎯 **组件级焦点绑定**：使用 ref 将快捷键限定在特定 DOM 元素，仅在元素聚焦时触发（如编辑器、弹窗）
- ⚡ **支持序列与组合键**：可处理修饰键组合（如 `ctrl+shift+k`）、vim 风格序列键（如 `g>i>t`）及重叠快捷键
- 📝 **自定义快捷键录制**：通过 `useRecordHotkeys` 钩子让用户录制专属快捷键，适用于设置面板和个性化功能

---

### [Expo Router 简介 - Expo 文档](https://docs.expo.dev/router/introduction/?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [Introduction to Expo Router - Expo Documentation](https://docs.expo.dev/router/introduction/?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

Expo Router 是一个基于文件系统的通用路由库，专为 Expo 构建的 React Native 应用设计，支持 Android、iOS 和 Web 平台。

- 📂 **文件即路由**：在 `app` 目录中添加文件，自动成为导航路由，简化开发流程。
- 🚀 **快速启动**：使用 `create-expo-app` 创建项目，并运行 `npx expo start` 即可开始。
- 📱 **原生优化**：基于 React Navigation，提供平台原生的导航体验，并自动支持深度链接。
- 🔗 **可分享**：每个屏幕自动生成可分享的链接，方便推广和调试。
- 🌐 **离线优先**：应用缓存并离线运行，自动更新，无需网络即可处理 URL。
- ⚡ **性能优化**：生产环境支持懒加载，开发环境支持延迟打包，提升效率。
- 🔄 **跨平台迭代**：支持 Android、iOS 和 Web 的通用快速刷新，加速开发。
- 🔍 **可发现性**：Web 端支持静态渲染，原生端支持通用链接，便于搜索引擎索引。
- ❓ **常见问题**：推荐用于新项目；可与 React Navigation 共存；文件路由简化重构、类型安全和深度链接。

---

### [GitHub - nanostores/nanostores：一个极小的（286字节）状态管理器，支持React/RN/Preact/Vue/Svelte，拥有许多可树摇的原子化存储](https://github.com/nanostores/nanostores)

**原文标题**: [GitHub - nanostores/nanostores: A tiny (286 bytes) state manager for React/RN/Preact/Vue/Svelte with many atomic tree-shakable stores · GitHub](https://github.com/nanostores/nanostores)

Nano Stores 是一个轻量级的状态管理库，支持多种前端框架，采用原子化存储和直接操作，体积小、速度快、可树摇。

- 📦 **超轻量**：压缩后仅 286-831 字节，零依赖，通过 Size Limit 控制大小。
- ⚡ **高性能**：原子化与派生存储设计，避免组件不必要的重渲染。
- 🌳 **可树摇**：打包时仅包含组件实际使用的存储，优化代码体积。
- 🧩 **多框架支持**：无缝集成 React、Vue、Svelte、Solid、Lit、Angular 等主流框架。
- 🧠 **智能存储**：提供原子（atom）、映射（map）、计算（computed）、效果（effect）等丰富类型。
- 🔄 **懒加载机制**：存储仅在监听器挂载时激活，无监听时自动禁用，节省资源。
- 🛠 **开发工具**：支持浏览器控制台日志、Vue Devtools 集成，方便调试。
- 📚 **最佳实践**：鼓励将逻辑从组件移至存储，分离变更与反应，减少 `get()` 在 UI 中的使用。
- 🧪 **测试友好**：提供 `keepMount`、`cleanStores`、`allTasks` 等工具，简化测试流程。

---

### [SSGOI - 现代网页应用的优雅页面过渡](https://ssgoi.dev/en)

**原文标题**: [SSGOI - Beautiful Page Transitions for Modern Web Apps](https://ssgoi.dev/en)

概述摘要
- 🚀 无需 View Transitions API 即可实现原生级网页过渡效果，兼容所有浏览器和框架
- ⚡ 零配置快速启动，默认值即可满足需求，支持 Safari 和 Firefox
- 📱 低端设备流畅运行：弹簧物理引擎+Web Animations API 确保 60fps 动画
- 🔄 支持多种过渡效果：淡入、旋转、条纹、百叶窗等，可自定义元素动画
- 🛠️ 全框架支持：React、Svelte、Vue、Angular、SolidJS、Qwik（即将推出）
- 📚 提供交互式演示和文档，几分钟内即可实现页面过渡
- 🆓 MIT 开源许可，免费使用，提供 GitHub、Discord 和 X 社区支持

---

### [GitHub - viclafouch/mui-otp-input: 📌 一个为 React 库 MUI 设计的一次性密码输入组件](https://github.com/viclafouch/mui-otp-input)

**原文标题**: [GitHub - viclafouch/mui-otp-input: 📌 A One-Time Password input designed for the React library MUI · GitHub](https://github.com/viclafouch/mui-otp-input)

## 概述总结
- 🔢 **MUI OTP 输入组件**：一个专为 React 库 MUI 设计的一次性密码输入组件
- 📦 **安装方式**：支持 npm、yarn 和 pnpm 三种包管理器安装
- 💻 **使用简单**：通过`MuiOtpInput`组件和`value`/`onChange`属性即可实现 OTP 输入功能
- ⚡ **Next.js 集成**：需在`next.config.mjs`中配置`transpilePackages`以支持 ESM 包
- 📚 **文档完善**：提供完整的文档、更新日志和 GitHub 发布页面
- 🛠 **TypeScript 支持**：内置 TypeScript 类型定义，便于类型安全开发
- 🐛 **问题反馈**：通过 GitHub Issues 提交 bug 报告或功能请求
- 📄 **开源许可**：采用 MIT 许可证，可自由使用和修改
- 🌟 **社区活跃**：获得 149 颗星标，29 个分支，22 个版本发布

---

### [2026 摇滚与反应节 – 科技、数据摇滚、美食与派对，奥斯陆洛克菲勒](https://reactnorway.com/?utm_medium=social&utm_source=ReactStatus)

**原文标题**: [Rock & React Festival 2026 – Tech, Datarock, Food & Party at Rockefeller, Oslo](https://reactnorway.com/?utm_medium=social&utm_source=ReactStatus)

React Norway 2026 將於 6 月 5 日在奧斯陸搖滾聖地 Rockefeller 舉辦，這是一場融合 React 技術與搖滾音樂的全端開發者大會。

- 🎸 活動亮點：一日單軌會議，白天學習 React 前沿技術，晚上享受搖滾音樂會與屋頂 BBQ
- 🎤 頂級講者陣容：來自 Hugging Face、Vercel、Amazon、Pinterest 等公司的 10 位業界領袖與 React 專家
- 🔒 安全實戰：Ramona Schwering 將現場演示 React 應用中的 XSS、注入攻擊等真實威脅與防禦方法
- 🤖 AI 前沿：Jack Herrington 展示 TanStack Start 與 AI 整合，Nico Martin 探討瀏覽器內多模態 AI 代理
- ⚡ 性能優化：Dominik Dorfmeister 分享如何用 Knip 移除 28,000 行無用程式碼，Aurora Scharff 講解 Async React 的中間狀態設計
- 🛠️ 開發工具：Robert Balicki 介紹 Isograph 編譯器驅動框架，Costa Alexoglou 分享低延遲配對程式設計經驗
- 🎟️ 票價方案：全端節日票 5990 克朗、僅音樂會 450 克朗、線上免費參與
- 🏆 競賽活動：下載背景音軌錄製獨奏，有機會贏得飯店住宿 + 節日門票
- 📍 場地資訊：Rockefeller 音樂廳可容納 1300 人，附近 Comfort Hotel 提供 15% 住宿折扣

---

### [JavaScript 中真正的新特性（以及接下来会有什么）—— Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

以下是您提供的文章内容摘要：

ECMAScript 2025 已正式发布，ECMAScript 2026 也即将到来。本文详细介绍了 JavaScript 中已落地的新特性、即将推出的功能，以及如何让 AI 编程助手使用这些现代 API。

- 🚀 **迭代器辅助方法**：ES2025 最令人兴奋的更新，为迭代器提供了 `.map()`、`.filter()`、`.take()` 等懒加载方法，无需先转换为数组，尤其适合处理无限或流式数据。
- 🔗 **Set 新方法**：ES2025 为 Set 添加了 `union`、`intersection`、`difference` 等标准集合操作，且不修改原 Set，参数支持“类 Set”对象。
- 📦 **JSON 模块**：ES2025 允许使用 `import config from './config.json' with { type: 'json' }` 原生导入 JSON，取代非标准的打包器魔法或运行时 fetch。
- 🛡️ **Promise.try**：ES2025 新增，用于统一处理可能同步、异步或抛出错误的函数，所有结果都通过 `.then`/`.catch` 处理，且无额外微任务延迟。
- 🔒 **RegExp.escape**：ES2025 新增，安全转义用户输入中的正则特殊字符，避免手动编写易出错的转义函数。
- 🔢 **Float16Array**：ES2025 新增的 16 位浮点类型数组，内存占用为 Float32Array 的一半，主要用于 WebGPU、TensorFlow.js 等场景。
- 🧮 **Math.sumPrecise**：ES2026 将落地，使用 Shewchuk 算法精确求和浮点数数组，避免累加误差。
- 🔄 **Uint8Array base64 和 hex**：ES2026 将落地，为 Uint8Array 原生提供 `toBase64()`、`toHex()` 等方法，取代手动转换。
- ❌ **Error.isError**：ES2026 将落地，跨 realm 检查值是否为 Error 对象，比 `instanceof` 更可靠。
- 🔗 **Iterator.concat**：ES2026 将落地，用于串联多个迭代器，无需手动编写生成器包装。
- 📝 **Map.getOrInsert**：ES2026 将落地，提供 `getOrInsert` 和 `getOrInsertComputed` 方法，简化 Map 的“获取或插入”模式。
- 📥 **Array.fromAsync**：ES2026 将落地，用于将异步可迭代对象收集为数组，取代手动 `for await...of` 循环。
- 📄 **JSON.parse with source text**：ES2026 将落地，reviver 函数可获取原始 JSON 文本，解决大数字精度丢失问题。
- ⏳ **Temporal**：已到 Stage 4，预计 ES2027 落地，是 Date 的现代替代品，提供 `ZonedDateTime`、`PlainDate` 等类型，正确处理时区和日期运算。
- 🧹 **using 关键字**：仍为 Stage 3，用于资源自动清理（如文件句柄、数据库连接），无需手动编写 `try/finally`。
- ⏰ **import defer**：仍为 Stage 3，允许延迟执行模块的顶层代码，仅在首次访问其属性时才执行，优化启动性能。
- 🤖 **AI 编程助手建议**：提供针对 Claude Code 等工具的“现代 JavaScript 偏好”指令，引导 AI 使用 ES2025/ES2026 新 API，避免生成过时代码。

---

### [数据类型 - Google 字体](https://fonts.google.com/specimen/Datatype)

**原文标题**: [Datatype - Google Fonts](https://fonts.google.com/specimen/Datatype)

概述：文章探讨了人工智能在医疗领域的应用，强调了其诊断效率提升、个性化治疗方案开发及数据隐私挑战等核心内容。
- 🩺 人工智能通过分析医学影像和病历数据，显著提高疾病诊断的准确性与速度。
- 💊 基于患者基因和病史的 AI 算法，可定制个性化治疗计划，提升疗效。
- 🔒 医疗数据共享面临隐私泄露风险，需加强加密技术与法规监管。
- 🤖 自动化流程（如药物研发）减少人力成本，但需警惕算法偏见问题。
- 🌐 远程医疗与 AI 结合，扩大医疗服务覆盖范围，尤其惠及偏远地区。

---

### [2026-04-28，版本 26.0.0（当前版）由 RafaelGSS 提交 · 拉取请求 #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526)

**原文标题**: [2026-04-28, Version 26.0.0 (Current) by RafaelGSS · Pull Request #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526)

Node.js 26.0.0 正式发布，带来 Temporal API、V8 14.6 等重大更新，并移除了多项旧功能。

- 🎉 **Temporal API 默认启用**：现代日期/时间 API，替代旧版 `Date` 对象，提供更强大的功能。
- ⚡ **V8 引擎更新至 14.6**：新增 `Map.getOrInsert()`、`Iterator.concat()` 等特性，性能与功能提升。
- 🌐 **Undici 升级至 8.0.2**：HTTP 客户端实现获得新功能与改进。
- 🗑️ **多项弃用与移除**：`writeHeader()`、`_stream_*` 模块等旧功能被彻底移除，`module.register()` 进入运行时弃用。
- 🔧 **构建与依赖变更**：GCC 要求提升至 13.2，放弃 Python 3.9 支持，更新 ICU、libuv 等依赖。
- 🐛 **已知问题与延期**：因 macOS 构建中 Temporal API 问题，发布推迟至 5 月 5 日。
- 🛡️ **安全修复**：包含 CVE-2026-21717 等安全补丁。

---
