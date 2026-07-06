### [React 文摘：邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

本内容介绍了一份专为 React 开发者设计的精选周刊通讯。

- 📧 每周一封邮件，服务超过 22,401 名前端工程师
- 📝 提供精心挑选的文章及简短摘要，节省阅读时间
- 🧠 每周学习新知识，保持技术更新
- 👍 读者好评：文章实用、内容紧跟 React 并发模式等前沿技术
- 🏢 读者来自各大知名公司
- 📅 覆盖 2013-2026 年，含隐私与广告说明

---

### [不同的水合与渲染策略——Nechiu Dan](https://neciudan.dev/hydration-and-rendering-strategies)

**原文标题**: [Different hydration and rendering strategies — Neciu Dan](https://neciudan.dev/hydration-and-rendering-strategies)

本文探讨了不同的水合（hydration）与渲染策略，旨在缩小页面“看起来就绪”到“真正可交互”之间的差距。文章从静态生成到最新的 Next.js 16.3，详细分析了每种策略的优缺点及适用场景。

- 📄 **静态生成 (SSG)**：在构建时预渲染 HTML，从 CDN 提供，速度极快，但内容可能过时，适合博客等静态内容。
- 🔄 **增量静态再生 (ISR)**：在 SSG 基础上，允许在后台按间隔或按需重新生成页面，兼顾了静态速度与内容的新鲜度。
- 🖥️ **客户端渲染 (CSR)**：浏览器下载并执行 JS 来构建 UI，交互响应快，但首屏加载慢，且对 SEO 不友好。
- ⚙️ **服务端渲染 (SSR)**：服务器渲染 HTML，浏览器接收后水合为交互式应用，解决了首屏空白和 SEO 问题，但水合过程本身有性能开销。
- 🚰 **流式 SSR**：利用`Suspense`将 HTML 分块流式传输，让用户无需等待最慢的组件即可看到页面，提升了感知性能。
- 🏝️ **岛屿架构 (Islands)**：页面主体为静态 HTML，仅对交互部分（岛屿）进行独立水合，极大减少了 JS 体积，适合内容为主的网站。
- 🧩 **React 服务端组件 (RSC)**：组件在服务端运行，不向客户端发送 JS 代码，仅发送序列化的 UI 描述，显著减小客户端包体积。
- 🔄 **TanStack Start**：采用客户端优先、RSC 即数据流的方式，允许在现有 SPA 中按需引入 RSC，灵活性高，但需要手动配置。
- ⚡ **细粒度响应式**：SolidJS、Svelte 等框架通过信号（Signal）实现组件只运行一次，状态更新直接操作 DOM，水合成本极低，适合高频更新的交互式 UI。
- 🚀 **可恢复性 (Resumability)**：Qwik 框架将执行状态序列化到 HTML 中，客户端无需水合，仅在用户交互时按需加载代码，实现了“零水合”。
- 🧭 **Next.js 16.3**：通过“缓存组件”和“部分预取”功能，将服务端渲染的导航体验提升至 SPA 级别的“即时”感，但需要开发者维护每个路由的缓存策略。

---

### [如何使用 Invoker Commands API 在 React 中打开模态对话框 — sergiodxa](https://sergiodxa.com/tutorials/open-a-modal-dialog-in-react-with-the-invoker-commands-api)

**原文标题**: [How to Open a Modal Dialog in React with the Invoker Commands API by sergiodxa](https://sergiodxa.com/tutorials/open-a-modal-dialog-in-react-with-the-invoker-commands-api)

本文介绍了如何使用 Invoker Commands API 在 React 中创建模态对话框，无需 useState 或 ref，仅通过 HTML 属性即可实现浏览器原生对话框的打开与关闭。

- 🛠️ **类型增强**：扩展 React 的 ButtonHTMLAttributes 类型，添加 `command` 和 `commandfor` 属性支持，使 TypeScript 能识别这些新属性。
- 🖥️ **渲染对话框**：使用 `useId` 生成唯一 ID，将 `commandfor` 与对话框的 `id` 绑定，按钮通过 `command="show-modal"` 触发浏览器原生行为。
- ❌ **无状态管理**：无需 `useState` 或 `ref` 调用 `showModal()`，React 仅负责渲染标记，浏览器处理交互。
- 🔘 **关闭按钮**：在对话框内使用 `method="dialog"` 的表单或 `command="close"` 的按钮关闭对话框，保持代码简洁。
- 📚 **保留复杂场景**：对于需要动画、嵌套覆盖或自定义焦点的复杂对话框，仍建议使用对话框库，此模式仅适用于简单场景。

---

### [为 React 编写自定义渲染器](https://www.callstack.com/blog/writing-custom-renderers-for-react)

**原文标题**: [Writing Custom Renderers for React](https://www.callstack.com/blog/writing-custom-renderers-for-react)

本文介绍了作者为 React Native Testing Library 构建自定义测试渲染器的过程，深入探讨了 React 渲染器的工作原理及其与协调器的交互。

- 🚀 **背景与挑战**：React 19 弃用了 React Test Renderer (RTR)，迫使作者为 React Native Testing Library (RNTL) 寻找新的测试渲染方案，以维持轻量级、纯 JavaScript 的测试环境。
- 🧩 **三种可选方案**：作者考虑了编写新测试渲染器、使用 Fantom（React 内部测试渲染器）或转向设备/模拟器端到端测试，最终选择构建新渲染器以保持现有测试库的兼容性。
- 🏗️ **React 渲染器核心**：React 通过元素树、Fiber 树和平台视图三层结构工作，协调器负责差异计算，渲染器实现具体操作（如创建、更新、删除节点），两者通过`HostConfig`接口通信。
- 🛠️ **测试渲染器实现**：新渲染器构建了简单的宿主实例树（容器、实例、文本实例），并实现了`appendChild`、`removeChild`、`commitUpdate`等基本操作，以支持测试断言。
- ⚡ **解决粗糙边缘**：为支持 RNTL 的 Fire Event API（需访问复合组件属性），作者添加了`unstable_fiber`逃逸机制，以绕过新渲染器仅管理宿主元素的限制。
- 💡 **构建渲染器的启示**：理解 React 渲染器需掌握元素树、Fiber 树和宿主实例树的关系，`HostConfig`是连接协调器与宿主环境的契约，且渲染器与 React 版本紧密耦合。

---

### [使用滤镜构建视频通话应用 — Margelo 博客](https://blog.margelo.com/building-videocall-app-with-filters)

**原文标题**: [Building a Video Call App with Filters — Margelo Blog](https://blog.margelo.com/building-videocall-app-with-filters)

### 概述总结
本文详细介绍了如何在 React Native 应用中，通过 VisionCamera 和帧处理器，在 Google Meet、Discord 等应用中实现实时滤镜（如背景模糊、虚拟背景、人物居中），并集成到 LiveKit 视频通话中。

- 📱 **核心原理**：用 VisionCamera 接管摄像头，通过原生引擎处理每一帧，再注入 LiveKit 的 WebRTC 视频源，实现自定义滤镜，而不改变传输和编码。
- 🔧 **后端简化**：使用 LiveKit 开源项目搭建后端，仅需两个路由（创建和加入房间），保持简单，让应用层专注实现功能。
- 🎥 **基础视频通话**：通过 React Native 和 `@livekit/react-native` 快速搭建，但 LiveKit 自带摄像头控制有限，无法直接添加滤镜。
- 🔄 **帧注入机制**：LiveKit 通过原生层的 `CapturerObserver`（Android）或 `RTCVideoCapturerDelegate`（iOS）接收帧，替换摄像头后，可将处理后的帧直接推入该接口。
- 🖼️ **VisionCamera 集成**：禁用 LiveKit 摄像头，使用 VisionCamera 捕获帧，通过 `Engine.forwardFrame` 将处理后的帧传入 LiveKit 视频源，实现无缝替换。
- 🛠️ **格式转换**：Android 需将 YUV_420_888 转换为 I420 格式，iOS 需重建 NV12 的 CVPixelBuffer，以确保 WebRTC 编码器正常处理。
- 🌫️ **背景模糊**：通过分割模型（MediaPipe/Vision）生成人物蒙版，对背景进行低分辨率模糊后合成，保持人物清晰，背景模糊。
- 🎨 **虚拟背景与颜色**：将背景替换为纯色或图片，复用相同蒙版和合成逻辑，仅改变背景填充内容。
- 🎯 **人物居中**：通过人脸检测（ML Kit/Vision）计算裁剪区域，平滑缩放，实现自动跟随人物移动的效果。
- ✏️ **空中绘图**：使用 Skia 渲染手指绘画，叠加到视频帧上，所有参与者实时可见，实现共享白板功能。
- ⚡ **性能优化**：保持同步处理最小化，将分割和检测等耗时操作放在独立线程，使用“最新帧优先”策略，确保摄像头帧率稳定。iOS 使用 GPU 处理，Android 使用 CPU（可迁移至 NEON SIMD）。
- 📊 **实测表现**：iPhone 13 全效果保持 30fps；低端三星 Galaxy F14 在复杂效果下降至 15-20fps，但可通过优化提升。
- 🚀 **最终结论**：通过 VisionCamera 接管摄像头，原生引擎处理帧，再注入 LiveKit，即可实现完全可编程的视频通话，新滤镜只需改变帧填充或合成方式。

---

### [Next.js 16.3：即时导航 | Next.js](https://nextjs.org/blog/next-16-3-instant-navigations)

**原文标题**: [Next.js 16.3: Instant Navigations | Next.js](https://nextjs.org/blog/next-16-3-instant-navigations)

Next.js 16.3 预览版发布，引入“即时导航”功能，旨在结合服务端渲染与单页应用的响应速度。

- 🚀 **即时导航核心机制**：通过 `Stream`（流式加载）或 `Cache`（缓存）让导航瞬间响应，避免网络等待；也可用 `Block` 强制延迟导航。
- ⚙️ **启用新功能**：需在配置中开启 `cacheComponents: true` 和 `partialPrefetching: true` 标志。
- 🧩 **部分预取**：不再为每个链接预取，改为按路由预取可复用的“外壳”，减少请求数量并支持离线导航。
- 🔍 **开发工具**：新增“即时洞察”面板和“导航检查器”，可暂停导航查看外壳内容，并用 `instant()` 测试助手防止回归。
- 🎯 **深度预取**：通过 `<Link prefetch={true}>` 和 `'use cache'` 可预取更多内容，但限制在构建时已知数据。
- 📉 **实际效果**：在 v0 产品中应用后，导航时间显著缩短，接近零延迟。
- 🛠️ **已知问题**：部分阻塞路由未报告、Safari 工具问题等，稳定版将修复。

---

### [CSS 状态与 JavaScript 事件之间的界限转移 | CSS 技巧](https://css-tricks.com/css-states-and-javascript-events/)

**原文标题**: [The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks](https://css-tricks.com/css-states-and-javascript-events/)

概述总结
- 🎯 CSS 伪类与 JavaScript 事件之间的界限正变得模糊，CSS 通过伪类来响应状态变化，而非直接监听事件。
- 🖱️ `:hover`和`:active`伪类分别对应指针进入/离开和按下/释放状态，是状态而非事件。
- 🔍 `:focus`和`:focus-visible`用于聚焦状态，后者通过浏览器启发式规则决定是否显示焦点指示器。
- 🧩 `:focus-within`和`:has()`允许 CSS 根据子元素状态（如聚焦）来样式化父元素，实现类似 JavaScript 的 DOM 遍历逻辑。
- ✅ `:checked`对应表单控件的选中状态，而`:valid`、`:invalid`等伪类处理表单验证逻辑，无需 JavaScript。
- 🎬 媒体元素伪类（如`:playing`、`:paused`）允许直接通过 CSS 样式化`<audio>`和`<video>`状态，替代 JavaScript 事件监听。
- 🗂️ `:popover-open`、`:open`和`:modal`分别对应弹出框、对话框和模态框的打开状态，无需监听`toggle`事件。
- 🔗 `:target`匹配 URL 哈希对应的元素，而`:fullscreen`检测全屏状态，均简化了 JavaScript 中的事件处理。
- ⚡ `event-trigger`提案允许 CSS 直接监听事件（如`click`）并触发动画，支持状态 ful 和 stateless 触发，未来可能支持事件冒泡。
- 💡 文章强调 CSS 的进化提供了更多选择，但 JavaScript 仍保留精确控制权，两者互补而非对立。

---

### [金发姑娘式可定制选择高度 - JakeArchibald.com](https://jakearchibald.com/2026/goldilocks-select-height/)

**原文标题**: [The Goldilocks customizable select height - JakeArchibald.com](https://jakearchibald.com/2026/goldilocks-select-height/)

### 概述总结
文章详细介绍了如何通过 CSS 优化自定义`<select>`下拉选择器的高度与位置，解决默认样式中的视口边缘对齐、过小或过大问题，并提供了跨浏览器的兼容方案。

- 📏 **默认样式问题**：默认`<select>`选择器会贴紧视口边缘，且高度可能过小或过大，影响用户体验。
- 🛠️ **添加视口边距**：通过`margin-block-end`和`max-block-size`调整，避免选择器紧贴视口边缘，但需处理 Firefox 不支持`stretch`的兼容问题。
- 🔄 **翻转位置适配**：使用`position-try-fallbacks: flip-block, flip-inline`等属性，确保选择器在翻转时边距自动调整，提升交互一致性。
- 📐 **最小高度限制**：通过`calc-size(fit-content, min(size, 12em))`设置智能最小高度，避免选项少时显示过大，但需为不支持`calc-size`的浏览器提供回退方案。
- 📏 **最大高度限制**：结合`calc-size(stretch, min(size, 30em))`和`min()`函数，防止选择器过高，同时保留视口边距。
- 💻 **完整 CSS 方案**：提供可直接复制的代码，包含所有兼容性处理，未来浏览器支持后仅需三行核心代码即可实现。

---

### [流式 HTML](https://olliewilliams.xyz/blog/streaming-html/)

**原文标题**: [Streaming HTML](https://olliewilliams.xyz/blog/streaming-html/)

### 概述总结
本文介绍了通过 `fetch()` 获取 HTML 流、使用 `textStream()` 方法处理文本流，以及将 HTML 流式注入 DOM 的新方法，包括安全与非安全版本，并对比了传统方法。

- 📡 **获取 HTML 流**：使用 `response.body.pipeThrough(new TextDecoderStream())` 或更简洁的 `response.textStream()` 方法，将字节流转换为文本流。
- 🚀 **流式注入 DOM**：新增 `streamHTML`、`streamAppendHTML` 等方法，支持将 HTML 流式注入元素，并分为安全（自动清理）和非安全（默认不清理）版本。
- 🔄 **非流式方法对比**：新方法包括 `setHTML`、`replaceWithHTML` 等非流式版本，其中非安全方法支持声明式影子 DOM 和 `runScripts` 选项。
- 🧩 **声明式局部更新**：通过 `<template>` 元素和 `<?marker>` 处理指令，实现 HTML 片段流式注入到指定位置，需注意安全方法默认移除 `<template>`。
- 🌐 **浏览器支持**：`textStream()` 和流式 DOM 方法目前仅在 Chrome Canary 中可用。

---

### [React 应用中的组件通信模式 — Neciu Dan](https://neciudan.dev/component-communication-patterns-in-react)

**原文标题**: [Component Communication Patterns in React Applications — Neciu Dan](https://neciudan.dev/component-communication-patterns-in-react)

本文总结了 React 应用中组件通信的多种模式，从简单的 Props 到复杂的事件驱动，帮助开发者根据组件距离和数据类型选择合适的方案。

- 📦 **Props 和回调**：父子组件间数据传递最直接的方式，数据向下流，回调向上传，适合近距离组件共享状态。
- 🧩 **组合（Composition）**：通过`children`属性传递渲染元素，避免中间组件无意义地传递数据，解决浅层属性钻取问题。
- 🎯 **状态就近（Colocation）**：将状态放在最需要它的组件中，避免提升到不必要的高层级，减少不必要的重新渲染。
- 🛠️ **命令式调用（Imperative Calls）**：使用`ref`和`useImperativeHandle`让父组件直接调用子组件的方法（如播放视频、聚焦输入框），适合“做某事”而非“共享状态”。
- 🌐 **Context**：用于跨越多层组件传递变化缓慢的值（如主题、用户），但需注意所有消费者都会重新渲染，且不适合高频更新的状态。
- 🏪 **全局状态库（如 Zustand）**：适合高频更新且组件需订阅不同切片的状态，通过选择器精确控制重新渲染，但需避免返回新对象的错误使用。
- 🖥️ **服务端状态（如 TanStack Query）**：处理属于服务器的数据（如用户、订单），自动管理加载、缓存、失效和重新获取，减少手动状态管理。
- 🔗 **URL 状态（如 nuqs）**：将描述当前视图的状态（如筛选、分页）放入 URL，实现可分享、可刷新、支持浏览器前进后退，适合视图相关状态。
- 📡 **事件驱动通信（Event Bus）**：用于完全解耦的组件间广播“事件”（如 Toast 通知），发送者和接收者互不知晓，但调试困难且存在时序陷阱，应作为最后手段。
- 🤔 **选择原则**：根据组件距离和数据类型选择最接近的工具，从 Props 开始，逐步向外扩展，避免过度使用全局方案。

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

概述摘要
- 📧 每周为软件工程师精心策划的新闻通讯
- 👥 已有超过 21,121 名软件工程师订阅
- ⏰ 每周一封邮件，节省寻找优质内容的时间
- 📚 精选文章并附简短摘要，每周学习新知识
- 💬 读者反馈：内容切合实际需求，如 API 设计
- 🌍 读者来自全球知名科技公司
- 📅 2013-2026 年持续运营，提供新闻通讯、隐私保护和广告服务

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一份为 CTO、工程经理和高级工程师精心策划的新闻通讯，旨在帮助他们成为更好的领导者。每周一和周四发送，内容精选并附有简短摘要，已吸引超过 29,240 名工程领导者订阅。

- 📬 每周两封邮件，提供精心挑选的领导力文章和简短摘要，节省寻找优质内容的时间
- 🚀 帮助 CTO、工程经理和高级工程师提升领导力，每周学习新知识
- 💬 读者反馈积极，称赞文章在软件领域、架构讨论、会议规划及沟通技巧方面精准到位
- 👥 受到众多科技领导者阅读，涵盖多家知名科技公司
- 📅 新闻通讯自 2013 年持续运营至 2026 年，提供新闻通讯、文章、隐私及广告服务

---

### [C# 文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

概述摘要  
C# Digest 是一份专为 .NET 开发者精心策划的每周新闻通讯，帮助读者节省时间、学习新知识，并已获得超过 21,217 名工程师的订阅和好评。

- 📬 每周一封邮件，精选高质量文章并附简短摘要  
- ⏱️ 节省筛选有价值内容的时间  
- 🧠 每周都能学到新东西  
- 🌟 读者反馈：文章实用，如操作结果模式、LINQ、DiagnosticListener 等，已用于实际工作  
- 👥 读者来自全球的.NET 工程师社区  
- 📅 新闻通讯由 Bonobo Press 自 2013 年起持续发布

---

### [让开发者保持最新动态 – Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 自 2013 年起为超过 94,000 名软件开发者、IT 专业人士和技术人员提供最新资讯，并发布简洁的新闻通讯，同时提供面向技术受众的广告服务。

- 📰 发布面向软件开发者、技术主管和 CTO 的简洁新闻通讯，深受技术人员喜爱
- 🎯 提供广告服务，帮助客户精准触达软件工程师、团队领导和技术决策者
- 📞 设有联系方式，欢迎咨询、建议或洽谈广告合作
- 📅 运营时间覆盖 2013 至 2026 年，并包含服务条款

---

### [过往新闻通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是对您提供的 React Digest 系列内容的摘要：

React Digest 系列涵盖了从 2026 年 3 月到 7 月的多期内容，聚焦 React 生态的最新动态、性能优化、安全漏洞、架构演进及工具创新。文章探讨了 React 19 的新特性（如自动记忆化、use() 钩子）、Next.js 的即时导航、TanStack Query 的数据管理、以及组件通信模式等主题。同时，也涉及了安全事件（如 Flight 协议 RCE 漏洞）、性能实践（如虚拟滚动、内存泄漏分析）和社区趋势（如从 Next.js 迁移到 Vite）。

- 🚀 **React 19 与性能优化**：React 19 自动处理记忆化，重点转向状态放置和并发特性（如 useTransition）；useEffect 的 bug 常源于不稳定的对象引用，最佳修复是直接移除效果。
- 🔄 **组件通信模式**：根据场景选择工具——Props 用于邻近组件，Context 适合慢变化值（如主题），Zustand 用于频繁更新；React Router v8 平滑升级，要求 React 19 和 Node 22。
- ⚡ **Next.js 即时导航**：Next.js 16.3 预览版通过更智能的预取和流式渲染实现即时点击反馈；同时，bloom filter 漏洞可能导致 URL 前缀重复，引发静默 404 错误。
- 🛡️ **安全漏洞与事件**：React 的 Flight 协议存在严重 RCE 漏洞，默认 Next.js 应用可被利用；TanStack npm 包遭链式 GitHub Actions 攻击，30 分钟内泄露云密钥。
- 🧩 **新工具与架构**：TanStack Query 零设置处理竞态条件、缓存和后台重取；React Fiber 将渲染拆分为 ~5ms 块，允许紧急更新（如点击）中断慢任务；Bippy 可运行时访问 React Fiber 树。
- 📉 **性能与内存泄漏**：86% 的前端项目存在内存泄漏，55,864 种模式源于定时器和事件清理缺失；Linear 通过浏览器存储和后台同步实现即时 UI，无加载动画。
- 🎨 **可访问性与错误处理**：常见 a11y 错误包括缺失语义、焦点断裂和动态更新无声；React Router 7 处理模态框和加载器无需 useEffect；测试 ID 可能暗示可访问性问题。
- 🔧 **React 19 新钩子**：useTransition 自动跟踪待处理状态，useActionState 捆绑错误和加载，免费修复竞态条件；use() 钩子跳过规则，在渲染时读取 Promise 并与 Suspense 协作。
- 🌐 **框架迁移与构建**：Railway 从 Next.js 迁移到 Vite，构建时间从 10 分钟降至 2 分钟；MDN 弃用 React SPA，改用服务器端 HTML 和 Lit Web 组件，开发启动从 2 分钟降至 2 秒。
- 📚 **社区与学习资源**：Mark Erikson 的 AI 编码设置使用父会话生成子任务，自定义插件保持上下文精简；一篇指南揭示信号无法真正修复 React 的怪癖；另一篇展示如何在 Next.js App Router 中处理错误。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了 React Digest 如何收集、使用和保护您的个人信息。

- 🔒 我们仅在收集前明确目的，并在法律要求或获得同意后使用您的信息。
- ⏳ 我们只保留实现目的所必需的信息，并在需要时确保其准确、完整和最新。
- 🛡️ 我们通过合理的安全措施保护个人信息，防止丢失、盗窃或未经授权的访问。
- 📧 我们仅收集您的电子邮件地址，用于发送新闻通讯，绝不用于其他目的。
- 👶 我们不会故意收集 13 岁以下儿童的信息，如果发现请立即联系我们。
- 📋 根据英国《数据保护法》，您可以请求获取我们存储的关于您的所有信息。
- ❌ 您可随时通过邮件请求删除您的数据，或点击退订链接取消订阅。
- 🚫 我们坚决反对垃圾邮件，绝不参与或推广任何形式的垃圾邮件行为。

---

### [媒体资料包 – 倭黑猩猩出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 提供面向程序员和技术领导者的高参与度新闻通讯广告服务，涵盖多个技术领域，并附有详细的媒体资料和合作流程。

- 📊 **高参与度受众**：新闻通讯的参与度是行业基准的两倍以上，订阅者多为决策者，来自 Google、Amazon 等知名公司。
- 📬 **四大新闻通讯**：Leadership in Tech（领导力）、Programming Digest（编程）、C# Digest（C#）、React Digest（React），各有不同的订阅人数、打开率和点击率。
- 💰 **广告定价透明**：每次赞助费用从$985 到$2,235 不等，CPC 在$1.93-$7.64 之间，并支持次要广告位。
- 📝 **纯文本广告格式**：广告以文本形式嵌入新闻通讯，需提供链接、标题和描述，截止日期为发布前 4 天。
- 🤝 **合作流程简单**：包括产品介绍、排期安排、发票支付、文案交付、广告上线和效果报告，建议提前几周联系。
- 🏢 **过往合作伙伴**：包括 Okta、GitLab、Datadog、MongoDB、Pluralsight 等知名品牌，常进行重复赞助。

---

