### [Next.js 16.3：即时导航 | Next.js](https://nextjs.org/blog/next-16-3-instant-navigations)

**原文标题**: [Next.js 16.3: Instant Navigations | Next.js](https://nextjs.org/blog/next-16-3-instant-navigations)

## 概述摘要

Next.js 16.3 预览版发布，核心功能是"即时导航"，让服务器驱动应用拥有类似单页应用（SPA）的响应速度，同时保留服务器端渲染的优势。

- 🚀 **即时导航**：通过流式渲染（`<Suspense>`）或缓存（`'use cache'`）让页面跳转瞬间响应，无需等待网络往返
- 🔧 **配置选项**：启用 `cacheComponents: true` 和 `partialPrefetching: true` 即可体验新功能
- 🎛️ **灵活控制**：开发者可为每个路由选择"流式"、"缓存"或"阻塞"模式，`export const instant = false` 可关闭即时导航
- 🧩 **部分预取**：每个路由只预取一个可复用的"外壳"，而非为每个链接单独预取，减少网络请求
- 🔍 **即时洞察**：开发模式下将慢导航标记为错误，并提供 Playwright 测试助手 `instant()` 防止回归
- 🖥️ **导航检查器**：新 DevTools 工具可暂停导航到"外壳"阶段，直观查看预取内容
- ⚡ **性能提升**：v0 产品实测导航时间大幅下降，接近零延迟
- 🎵 **开源演示**：Next Beats 音乐播放器项目展示了即时导航的实际效果
- ⚠️ **已知问题**：Safari 工具兼容性、部分阻塞路由报告等问题将在稳定版修复

---

### [获取失败](https://github.com/vercel/next.js/blob/canary/skills/next-cache-components-adoption/SKILL.md)

**原文标题**: [Failed to retrieve](https://github.com/vercel/next.js/blob/canary/skills/next-cache-components-adoption/SKILL.md)

无法总结：获取内容失败，状态码 429。

---

### [Bluesky 上的@danabra.mov](https://bsky.app/profile/danabra.mov/post/3mp5b3n3xgc2k)

**原文标题**: [@danabra.mov on Bluesky](https://bsky.app/profile/danabra.mov/post/3mp5b3n3xgc2k)

概述摘要  
- 📜 该网页需要 JavaScript 才能正常交互，简单 HTML 界面无法满足其功能需求。  
- 🌐 提供 Bluesky 社交平台和 AT Protocol 的链接，供用户了解更多信息。  
- 💬 用户“dan”对 Next.js 新版本表示谨慎乐观，特别赞赏其逐步引入 SPA 式即时导航的功能。  
- 🚀 用户认为该方向值得鼓励，但仍需更多改进才能无条件推荐 Next.js。

---

### [Bluesky 上的@danabra.mov](https://bsky.app/profile/danabra.mov/post/3mp5b3nd3ws2k)

**原文标题**: [@danabra.mov on Bluesky](https://bsky.app/profile/danabra.mov/post/3mp5b3nd3ws2k)

### 概述总结
danabra.mov 宣布加入 Vercel 的 Next.js 团队，初期以兼职形式工作，并计划逐步了解用户问题以改进 App Router。

- 🚀 加入团队：danabra.mov 宣布加入 Vercel 的 Next.js 团队。
- ⏳ 兼职起步：初期为兼职工作，避免被大量错误报告淹没。
- 👀 关注问题：计划逐步关注用户日常遇到的 Next.js 问题。
- 🎯 优化目标：希望让 App Router 变得更好用。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=26q2&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=26q2&utm_content=primary)

Meticulous 是一款自动化、全面且确定性的测试工具，专为复杂代码库设计，可零开发工作量生成和维护测试套件，帮助开发者快速、可靠地交付代码。

- 🚀 **零开发工作量**：自动生成并维护测试套件，无需编写、修复或维护测试用例。
- 🔍 **全面且确定性**：从 Chromium 层面构建确定性调度引擎，消除测试不稳定问题，实现快速执行。
- 🧪 **自动化测试演进**：测试套件随应用变化自动更新，新增或移除测试，始终覆盖所有代码分支和用户流程。
- ⏱️ **闪电般快速**：测试在计算集群上高度并行化，1000 个屏幕的测试可在 120 秒内完成。
- 🔌 **简单集成**：只需添加脚本标签或安装加载器，即可在本地开发、预发布和生产环境中记录会话。
- 🛡️ **消除不稳定**：通过模拟后端响应（保存并重放原始记录），避免因数据变化导致的假阳性，无需特殊测试账户或模拟数据。
- 🤝 **灵活使用**：可与现有测试套件互补，或完全替代现有测试。
- 🏢 **受信赖**：已被 Dropbox、Notion、Engine 等超过 100 家组织采用，工程师反馈“立即爱上，无法想象没有它”。
- 📚 **支持主流框架**：提供 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等框架的集成示例。

---

### [Boshen 在 X 上表示：“我们从 Rolldown 和 Vite 中撤回了 Rust React 编译器集成，因为它将二进制文件大小从 28.7MB 增加到 33.8MB，增加了 17%，这对所有 Vite 用户来说是不合理的。

我目前的实验是让 Claude 理解我们的限制。

初步” / X](https://x.com/boshen_c/status/2069449703935336846)

**原文标题**: [Boshen on X: "We withdrew the Rust React Compiler integration from Rolldown and Vite because it increased the binary size from 28.7MB to 33.8MB, a 17% increase, which cannot be justified for all Vite users.

My current experiment is to have Claude understand our constraints.

Preliminary" / X](https://x.com/boshen_c/status/2069449703935336846)

概述总结
- 📦 因 Rust React Compiler 集成导致二进制体积从 28.7MB 增至 33.8MB（增加 17%），团队决定从 Rolldown 和 Vite 中撤回该集成
- 🤖 正在尝试让 Claude 理解项目约束，初步结果显示性能提升可达 2 倍，而二进制体积仅增加 1.4MB
- 🛠 下一步计划是优化代码（去“Slop 化”）并使其易于维护，同时将部分改动向上游提交

---

### [肯尼斯·斯科夫胡斯 | 将 Linear 从 styled-components 迁移至 StyleX](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

**原文标题**: [Kenneth Skovhus | Moving Linear from styled‑components to StyleX](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

### 概述总结
Linear 团队将 React 应用从 styled-components 迁移至 StyleX，主要出于性能优化和代码封装性考量。迁移过程借助编码代理工具和自定义代码转换工具，实现了渐进式替换，最终使页面渲染速度提升约 30%。

- 🚀 **性能提升**：通过消除运行时 CSS 生成与注入，页面导航渲染速度提升约 30%。
- ⚠️ **迁移动因**：styled-components 进入维护模式，且未适配 React 18 的 `useInsertionEffect`，导致性能瓶颈。
- 🛡️ **封装性强化**：StyleX 通过严格的样式契约和原子化系统，限制外部组件重写，减少维护噩梦。
- 🛠️ **代理辅助迁移**：开发了 `styled-components-to-stylex-codemod` 工具，处理 500+ 合并请求和约 10 万行迁移代码。
- 📈 **渐进式策略**：先定义样式基础（变量/常量），从叶子节点开始迁移，配合自定义 lint 规则和 CSS Modules 逃生舱。
- 🧩 **生态系统优势**：StyleX 由 Meta 维护，被 Figma、Cursor 等采用，提供确定性样式解析和类型安全。
- 🤖 **人类与代理协作**：代理可高效处理代码转换，但人类仍需验证复杂交互（如悬停状态）和系统设计。

---

### [为 React 编写自定义渲染器](https://www.callstack.com/blog/writing-custom-renderers-for-react)

**原文标题**: [Writing Custom Renderers for React](https://www.callstack.com/blog/writing-custom-renderers-for-react)

本文讨论了在 React 19 弃用 React Test Renderer (RTR) 后，为 React Native Testing Library (RNTL) 构建自定义测试渲染器的过程与挑战。

- 🧪 **背景与动机**：React 19 弃用了 RTR，迫使 RNTL 维护者寻找新的测试渲染方案，以保持轻量级、纯 JavaScript 的测试环境。
- 🛠️ **三大选择**：作者评估了三个选项——编写新测试渲染器、使用 Fantom（React 内部测试渲染器）、或转向设备/模拟器上的 E2E 测试，最终选择了构建新渲染器。
- 🔍 **React 渲染器原理**：React 通过元素树、Fiber 树和平台视图三层结构工作，渲染器负责将 Reconciler 的通用操作转换为平台特定的视图操作。
- 📝 **新渲染器实现**：构建了一个简单的宿主实例树（容器、实例、文本实例），实现了创建、添加、更新和移除节点等基本操作，并利用 Reconciler 的`HostConfig`接口。
- ⚠️ **边缘情况处理**：为支持 RNTL 的 Fire Event API，需通过`unstable_fiber`访问复合元素属性，因为新渲染器仅管理宿主元素树。
- 💡 **经验教训**：构建渲染器加深了对 React 内部机制的理解，包括元素树、Fiber 树和宿主实例树的关系，以及`HostConfig`作为连接桥梁的作用。
- 🎯 **未来用途**：新测试渲染器主要面向 RNTL，但设计灵活，可用于其他需要纯 JavaScript 测试的场景。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=https://expo.dev/)

**原文标题**: [Expo — Build Native Apps with React](https://expo.dev/?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=https://expo.dev/)

Expo 是一个全栈 React Native 框架，提供强大的云服务，帮助开发者在应用生命周期的每个阶段更快地构建、部署和迭代应用。

- 📱 **全栈框架**：Expo 提供从开发到部署的一站式解决方案，包括 SDK、构建、更新和托管服务。
- 🛠️ **强大开发工具**：支持 React、Kotlin、Swift 编写原生代码，拥有 100+ 生产级库，被 Meta 推荐为唯一原生框架。
- 🚀 **即时更新**：通过 OTA 更新功能，可快速将最新修复和改进推送给所有用户。
- 🤖 **自动化工作流**：支持自动构建、测试和发布，可配置分支触发构建和提交。
- 📊 **内置监控**：提供 Insights 监控用户平台分布、API 请求和错误率。
- 🌍 **跨平台发布**：从单一代码库构建并分发到 Android、iOS 和 Web。
- 👥 **活跃社区**：70,000+ Discord 成员，80% 的 React Native 开发者选择 Expo，500,000+ 项目已创建。
- 🔒 **企业级安全**：SOC 2 Type 2 和 GDPR 合规，可扩展至数亿用户。
- 🏆 **顶级应用**：Expo 应用曾获 App Store 第一名，深受开发者喜爱。
- 💬 **用户好评**：开发者称赞 Expo 简化开发流程、提升性能、降低门槛，比纯 React Native 更优。

---

### [Waku 的独特功能：切片](https://newsletter.daishikato.com/p/waku-s-unique-feature-slices)

**原文标题**: [Waku’s Unique Feature: Slices](https://newsletter.daishikato.com/p/waku-s-unique-feature-slices)

Waku 框架的 Slices 功能是一种独特的可复用组件机制，灵感来自 Gatsby 的 Slice API，支持独立渲染配置和懒加载，适用于静态与动态页面的灵活组合。

- 🧩 **Slices 定义**：放在 `src/pages/_slices` 目录下的可复用组件，文件路径作为其唯一 ID，并支持独立的渲染配置（如 `static`）。
- 🛠️ **使用方式**：通过 `<Slice id="greet" />` 组件引用，但必须在页面配置的 `slices` 数组中列出该 ID，以避免编译器魔法。
- ⏳ **懒加载功能**：标记为 `lazy` 的 Slice 可独立于页面加载，类似 Astro 的服务器岛屿，支持动态内容，且无需在页面配置中列出。
- 💡 **强大灵活性**：Slices 支持静态/动态组件与静态/动态页面的任意组合，概念简单直观，符合 Waku 的极简哲学。

---

### [一次被低估的重构如何节省了 90% 的内存使用 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

**原文标题**: [How an Underrated Refactor Saved 90% Memory Usage | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

TanStack Table V9 通过共享原型重构，在处理大规模数据时内存使用量降低高达 90%，从 V8 的约 2.7GB 降至 V9 的约 260MB，实现了 10 倍的可扩展性提升。

- 📉 **显著内存节省**：处理 100 万行×8 列数据时，V9 内存使用仅 257MB，相比 V8 的 2710MB 节省约 90.5%
- 🔄 **核心重构方法**：将行、列、单元格等对象的方法从每个实例独立创建改为共享原型，消除重复函数对象和闭包作用域
- 🚀 **可扩展性飞跃**：V8 最多处理约 150 万行，V9 可处理 1000-1600 万行才达到 4GB 内存限制
- ⚙️ **动态特性系统**：使用手动原型而非类继承，支持按需组合排序、筛选、分页等特性，保持树摇优化
- ⚠️ **微小破坏性变更**：解构方法不再有效（如`const { getValue } = row`），需通过`row.getValue()`调用
- 🧪 **基准测试验证**：通过 Playwright 和 Chrome DevTools Protocol 进行内存测量，涵盖分页、虚拟化等场景
- 💡 **适用性考量**：小数据量场景内存差异可忽略，但大规模数据处理时收益显著，为速度优化释放了内存预算

---

### [使用滤镜构建视频通话应用 — Margelo 博客](https://blog.margelo.com/building-videocall-app-with-filters)

**原文标题**: [Building a Video Call App with Filters — Margelo Blog](https://blog.margelo.com/building-videocall-app-with-filters)

以下是对该文章内容的总结：

本篇文章详细介绍了如何在 React Native 应用中，通过 VisionCamera 和帧处理器，在 Google Meet、Discord 和 WhatsApp 等应用中实现实时滤镜（如背景虚化、虚拟背景、自动居中缩放）的功能。核心思路是用 VisionCamera 接管摄像头，通过原生引擎处理每一帧，然后将处理后的帧注入 LiveKit 的视频源，从而在不改变编码、传输和信令的情况下，实现自定义视频效果。

- 📹 **核心架构**：VisionCamera 捕获帧 → vc-engine（原生引擎处理）→ LiveKit VideoSource → WebRTC 编码器 → 传输给其他参与者。所有下游组件保持不变，仅像素发生变化。
- 🔧 **后端简化**：使用 LiveKit 开源项目搭建后端，仅需两个路由（创建房间和加入房间），部署简单，让开发者专注于应用本身。
- 📱 **基础视频通话**：使用 React Native CLI 和 @livekit/react-native 可快速搭建视频通话，但 LiveKit SDK 对摄像头控制有限，无法直接添加滤镜。
- 🔄 **帧注入机制**：通过替换 LiveKit 的摄像头，将 VisionCamera 捕获的帧直接推入 WebRTC 视频源。关键在于获取视频源的 CapturerObserver（Android）或 delegate（iOS），然后调用 onFrameCaptured 或 didCaptureVideoFrame 方法。
- 🎥 **VisionCamera 接管摄像头**：禁用 LiveKit 的摄像头（video={false}），使用 VisionCamera 的帧输出。通过 Engine.forwardFrame 函数，在原生层进行格式转换和滤镜处理，最后推入 LiveKit 视频源。
- 🔗 **源创建与注册**：通过 RtcBridge.createTrack 创建轨道，并注册到引擎的 sources 映射中，确保帧能正确路由到对应的视频源。activeTrackId 由 JavaScript 动态设置。
- 🎨 **格式转换**：Android 需要将 YUV_420_888 转换为 I420（JavaI420Buffer）；iOS 需要重建 NV12 的 CVPixelBuffer。转换是必要的，因为引擎会读取帧并应用滤镜，产生新的输出缓冲区。
- 🖼️ **滤镜实现**：所有滤镜（背景虚化、虚拟背景、中心舞台、空中绘画）都基于相同的管道：转换 → 合成 → 推送。合成步骤混合了背景、摄像头帧和遮罩。
- 🌫️ **背景虚化**：包括三个步骤：1) 使用 MediaPipe（Android）或 Vision（iOS）生成人物遮罩；2) 对帧进行下采样模糊；3) 根据遮罩合成清晰人物和模糊背景。推理在后台线程异步进行，避免阻塞主线程。
- 🎨 **色彩与照片背景**：只需将背景替换为纯色或解码后的图像，遮罩和合成逻辑保持不变，代码改动极小。
- 🎯 **中心舞台**：通过 ML Kit（Android）或 Vision（iOS）检测人脸，计算裁剪区域并平滑缩放，实现自动跟随人物移动的效果。
- ✏️ **空中绘画**：使用 Skia 在帧上绘制手指轨迹，合成到视频流中，所有参与者都能实时看到，实现共享白板功能。
- ⚡ **性能优化**：遵循“不让摄像头等待”原则，forwardFrame 同步执行最小操作，分割和检测在后台线程异步进行。iOS 使用 GPU（Metal）处理，Android 使用 CPU（Kotlin），但可迁移到 NEON SIMD 或 GPU 计算着色器。
- 📊 **性能数据**：iPhone 13（GPU）可保持 30 fps；三星 Galaxy F14（CPU）在轻量效果下约 30 fps，复杂效果下约 15-20 fps。
- 🚀 **总结**：通过替换 LiveKit 的摄像头为 VisionCamera，将固定视频通话变为完全可编程的平台。所有滤镜基于同一管道，新增滤镜只需改变填充或合成方式。作者计划开源完整示例。

---

### [Takumi — 将您的 React 组件渲染为图像。](https://takumi.kane.tw/)

**原文标题**: [Takumi — Render your React components to images.](https://takumi.kane.tw/)

Takumi 是一個能將 JSX 直接渲染為圖像的 Rust 工具，無需瀏覽器，高效且輕量。

- 🚀 **無瀏覽器渲染**：直接解析 CSS、佈局樹、文字形狀並編碼像素，單一 Rust 二進制文件即可完成，比 Headless Chromium 更輕更快。
- 🎨 **代碼即設計**：ImageResponse 與 next/og 兼容，組件代碼即為圖像源碼，所見即所得。
- ⏳ **時間取樣動畫**：支援時間戳渲染，可輸出靜態 PNG 或動畫 WebP，CSS @keyframes 與 Tailwind animate-* 在渲染時解析。
- 🛠️ **完整 CSS 支援**：涵蓋 grid、float、absolute 定位、calc()、z-index、backdrop-filter、mix-blend-mode、clip-path、mask、WOFF2 字體、emoji、RTL 等進階屬性。
- 🌍 **多平台運行**：提供原生 Node.js 綁定、WASM 構建（用於 Cloudflare Workers 與瀏覽器）及 Rust crate，支援 macOS、Linux、Windows 的 x64 與 ARM64。
- 🏢 **實際生產應用**：已被 Dcard、Fumadocs、Nuxt OG Image 等專案採用，用於生成分享圖像與文檔 OG 圖。

---

### [升级至 v2 — Takumi](https://takumi.kane.tw/docs/upgrade/v2)

**原文标题**: [Upgrade to v2 — Takumi](https://takumi.kane.tw/docs/upgrade/v2)

### 概述总结
本文档详细介绍了从 Takumi v1 升级到 v2 的完整指南，包括 JavaScript 和 Rust API 的重大变更、CSS 默认值调整以及资源管理方式的改变。

- 🔄 **异步渲染**：顶层渲染函数（render/renderSvg/renderAnimation）现在需要`await`，因为会等待字体和图片加载完成
- 🖼️ **字体管理重构**：`Renderer`构造函数不再接受字体参数，改为通过每个渲染调用的`fonts`选项传递；`loadFont/loadFonts/loadFontSync`统一为`registerFont`
- 📦 **图片资源去全局化**：移除全局图片存储，改为通过`images`选项按`src`键值对传递；`fetchedResources`重命名为`images`
- 🎨 **输出格式优化**：`format`改为字符串（"png"|"jpeg"|"webp"等），支持单独的`quality`和`lossless`参数；`createImageResponse`移除，改用`new ImageResponse`
- 🦀 **Rust API 重构**：`GlobalContext`变为`Fonts`，通过`RenderOptions::builder().fonts(&fonts)`传递；`raster`特性重命名为`raster-backend`；`OutputFormat::Jpeg/WebP`携带`Quality`，无损 WebP 独立为`WebPLossless`
- 🔧 **CSS 默认值调整**：`position`默认值从`relative`改为`static`；`border-width`/`outline-width`默认值从`0`改为`medium`（3px）；负`scale`从折叠为 0 改为镜像效果；`line-clamp`变为简写属性
- 🚫 **SVG currentColor 行为变更**：SVG 图片中的`currentColor`不再继承宿主元素的`color`，而是使用 SVG 自身的默认值（黑色）
- 📐 **API 命名统一**：`measure_layout`→`measure`；`render_sequence_animation`→`render_animation`；`render`返回类型从`RgbaImage`变为`Bitmap`；`render_for_layout`移除`current_color`参数
- 🔄 **类型简化**：`LengthDefaultsToZero`和`ColorDefaultsToTransparent`别名移除，直接使用`Length`和`ColorInput`；`BackgroundPosition`重命名为`PositionValue`，`ObjectPosition`/`TransformOrigin`移除

---

### [ForesightJS](https://foresightjs.com/)

**原文标题**: [ForesightJS](https://foresightjs.com/)

### 概述总结
ForesightJS 通过预测用户意图，在内容被需要前智能预取，支持桌面端和移动端的不同策略，并提供了完整的开发工具和快速集成方案。

- 🖱️ **鼠标轨迹预测**：分析光标移动模式，预测用户即将点击的链接并提前预取内容
- ⌨️ **键盘导航预测**：追踪 Tab 键使用，当用户距离注册元素 N 个 Tab 时触发预取
- 📜 **滚动预测**：根据滚动方向判断用户即将到达的元素，提前预取内容
- 📱 **触控设备支持**：提供视口进入和触摸开始两种预测策略，适配移动端和触控笔
- 🎮 **实时调试工具**：通过官方开发工具可视化预测触发过程，支持鼠标、滚动和 Tab 导航测试
- ⚡ **高性能架构**：采用事件驱动设计，无轮询、无回流，优化核心性能
- 🚀 **快速集成**：支持 JavaScript、React、Vue，5 分钟内完成配置，提供完整类型安全

---

### [发布 V4.2.0 - `<Foresight>` 组件 · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.2.0)

**原文标题**: [Release V4.2.0 - The `<Foresight>` Component · spaansba/ForesightJS · GitHub](https://github.com/spaansba/ForesightJS/releases/tag/V4.2.0)

ForesightJS 发布 V4.2.0 版本，核心更新是引入 `<Foresight>` 组件，简化了元素注册流程，并优化了核心性能与修复了多个 bug。

- 🚀 **全新 `<Foresight>` 组件**：React 和 Vue 包均引入此声明式组件，替代 `useForesights` 和回调 ref，只需包裹元素即可完成注册。
- ⚙️ **全局 `dataAttributeMirroring` 设置**：数据属性镜像现在由全局管理器控制，无需逐元素配置（#133）。
- 🐛 **修复多个 Bug**：包括触摸策略无操作触发、桌面处理器初始化时忽略 `positionHistorySize` 等（#125, #124）。
- 📈 **性能优化**：仅活跃元素被观察器追踪，停用元素在重新激活前不占用资源（#126）。
- 🧹 **内部清理**：移除了重复的设置、注册和日志代码路径，并丢弃未使用的类型导出（#129, #127）。
- 🔧 **开发工具更新**：v2.2.0 适配核心变更，元素数据属性显示遵循新的全局设置（#133）。

---

### [GitHub - aidenybai/cnfast: `cn` 的快速替代方案 · GitHub](https://github.com/aidenybai/cnfast)

**原文标题**: [GitHub - aidenybai/cnfast: Fast drop in replacement for `cn` · GitHub](https://github.com/aidenybai/cnfast)

cnfast 是一个比 tailwind-merge 快 3.8 倍（最高 7 倍）的 cn 函数替代品，输出结果字节一致，API 相同，无需修改代码。

- ⚡ 性能提升显著：在缓存重渲染场景下速度提升 4.3 倍，冷启动合并引擎提升 3.8 倍，组件密集型代码最高提升 7 倍。
- 🚀 安装与迁移简单：通过 `npm install cnfast` 安装，或使用 `npx cnfast migrate` 一键迁移现有项目。
- 🎨 支持 shadcn/ui 集成：通过 `npx shadcn@latest add aidenybai/cnfast/cn` 命令直接替换 cn 工具函数。
- 📦 导出完整工具集：同时导出 clsx、twMerge 和 twJoin，方便灵活使用。
- 🔧 支持标签模板语法：使用 `cn\`...\`` 形式可缓存调用位置，在重复渲染时速度提升 4.3 倍。
- 📊 广泛测试验证：在 65 个工作负载中几何平均速度提升 3.8 倍，11.3 万个真实调用组中零输出差异。
- 🎯 适用场景广泛：适合数据网格、虚拟表格、实时仪表盘等高频率重渲染场景，可有效控制帧预算。
- 📚 开源与兼容：基于 MIT 许可，改编自 clsx 和 tailwind-merge 的代码，输出结果字节一致。

---

### [介绍 eve - Vercel](https://vercel.com/blog/introducing-eve)

**原文标题**: [Introducing eve - Vercel](https://vercel.com/blog/introducing-eve)

## 概述总结

eve 是一个开源的智能体框架，用于构建、运行和扩展智能体，它将智能体定义为文件目录，内置了生产环境所需的所有功能。

- 🚀 **eve 框架的核心理念**：构建智能体只需定义其功能，无需组装所有生产运行所需的组件，框架已内置持久化执行、沙箱计算、人工审批、子智能体和评估等功能

- 📁 **智能体即目录**：每个智能体是一个包含 agent.ts、instructions.md、tools/、skills/、subagents/、channels/和 schedules/等文件的目录，一目了然

- ⚡ **快速创建**：只需定义 agent.ts（配置模型）和 instructions.md（设定角色和规则），eve 自动将工具和技能文件连接成可运行的智能体

- 🔋 **内置电池**：包括持久化会话（可中断恢复）、每个智能体的独立沙箱环境、人工审批机制、安全连接到各种工具和数据服务

- 🌐 **多平台支持**：同一智能体可通过 Slack、Discord、Teams、Telegram、GitHub 等多个渠道运行，只需一个适配器文件

- 🔍 **内置追踪和评估**：每次运行生成 OpenTelemetry 追踪，支持导出到各种监控服务，评估功能可进行评分测试

- 🛠️ **扩展简单**：工具是一个 TypeScript 文件，技能是一个 markdown 文件，文件名和位置即定义，eve 自动处理注册和连接

- 💻 **本地开发和测试**：使用`eve dev`命令启动开发服务器，TUI 界面实时显示每个步骤，支持评估测试和 CI 集成

- 🚢 **一键部署**：智能体是普通的 Vercel 项目，使用`vercel deploy`部署，无需额外配置，部署不中断正在进行的会话

- 📅 **定时任务**：通过 cron 表达式定义调度文件，自动在指定时间触发智能体运行

- 🏢 **Vercel 内部实践**：运行超过 100 个生产智能体，包括数据分析师（月处理 3 万 + 问题）、自主 SDR（年成本$5000，回报 32 倍）、销售驾驶舱、支持工程师（92% 自动解决）、内容代理和路由代理等

- 🎯 **入门方式**：`npx eve@latest init my-agent`命令可在 1 分钟内创建第一个智能体，支持通过编码智能体自动搭建

---

### [GitHub - marmelab/react-admin：基于TypeScript、React和Material Design，构建在 REST/GraphQL API 之上的单页应用前端框架](https://github.com/marmelab/react-admin)

**原文标题**: [GitHub - marmelab/react-admin: A frontend Framework for single-page applications on top of REST/GraphQL APIs, using TypeScript, React and Material Design · GitHub](https://github.com/marmelab/react-admin)

react-admin 是一个基于 TypeScript、React 和 Material Design 的前端框架，用于构建运行在 REST/GraphQL API 之上的单页应用，由 marmelab 开源并维护。

- 🔌 **后端无关性**：支持连接任何 REST 或 GraphQL API，提供超过 45 个适配器
- 🧩 **功能组件齐全**：包含认证、路由、表单验证、数据表格、搜索过滤、权限管理、富文本编辑器、国际化、通知、主题等 hooks 和组件
- 🪡 **高质量保障**：注重无障碍、响应式、安全、性能和可测试性
- 💻 **优秀开发者体验**：提供完整文档、IDE 自动补全、类型安全、Storybook、演示应用和模块化架构
- 👑 **卓越用户体验**：支持乐观渲染、即输即滤、撤销操作、偏好设置和保存查询
- 🛠 **高度可定制**：可替换任意组件为自定义实现
- ☂️ **类型可选**：支持 TypeScript 或 JavaScript 开发
- 👨‍👩‍👧‍👦 **技术栈**：基于 Material UI、react-hook-form、react-router、react-query 和 TypeScript

---

### [发布 Reanimated - 4.5.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.5.0)

**原文标题**: [Release Reanimated - 4.5.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.5.0)

react-native-reanimated 4.5.0 版本发布，新增多项 CSS 动画功能并修复大量问题。

- 🎨 **CSS 核心动画支持更多属性**：阴影（shadowColor、shadowOpacity、shadowRadius、shadowOffset）、背景和边框（backgroundColor、borderColor、borderWidth、borderRadius）的 CSS 过渡现可在 iOS Core Animation 上运行，需启用 `IOS_CSS_CORE_ANIMATION` 特性标志。
- 🖱️ **CSS 动画伪选择器**：支持 `:hover`、`:active` 和 `:focus` 伪选择器，覆盖 Apple、Android 原生后端及 Web 实现。
- 🌐 **SVG 动画 Web 支持**：`react-native-svg` 组件的 CSS 动画现可在 Web 上运行。
- 🔗 **SharedTransitionBoundary 组件**：新增 `<SharedTransitionBoundary>` 组件，用于限定共享元素过渡的作用域，避免不同屏幕间的过渡冲突。
- 🐛 **大量修复**：修复了伪选择器类型问题、Android ANR 死锁、iOS 双重重载崩溃、内存泄漏、30fps 布局动画、Jest 环境检测等 30 余项问题。
- 🧹 **代码清理与优化**：移除 PlainStyle 类型、简化 CSS 过渡流程、优化 `useHandler` 上下文延迟初始化等。
- 👥 **新贡献者**：欢迎 `finloop`、`sorinc03`、`audrius-savickas`、`kasperski95`、`enisdenjo`、`Warabi1915181`、`patrickwehbe` 等首次贡献者。

---

### [OAuth 应用中的组织支持](https://clerk.com/changelog/2026-05-14-oauth-organizations?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=orgs-oauth&utm_content=06-26-26&dub_id=FcaMPCzQfLjheYyP)

**原文标题**: [Organizations support in OAuth Applications](https://clerk.com/changelog/2026-05-14-oauth-organizations?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=orgs-oauth&utm_content=06-26-26&dub_id=FcaMPCzQfLjheYyP)

概述：
Clerk 的 OAuth 应用现在支持组织上下文，允许用户在 OAuth 流程中选择组织，客户端可获取 org_id 声明。

- 🏢 OAuth 应用新增组织支持：用户可在 OAuth 流程中选择组织，客户端在访问令牌中收到 org_id 声明。
- 🔑 新增 user:org:read 作用域：客户端请求此作用域且用户授权后，同意屏幕显示组织选择器，令牌包含 org_id。
- 🚫 禁用同意屏幕时：org_id 自动填充为用户最后活跃的组织。
- 📋 userinfo 端点扩展：返回 org_name 和 org_slug，方便客户端显示组织上下文。
- ⚙️ 启用方式：在 Clerk 仪表板中为现有 OAuth 应用启用 user:org:read 作用域即可。
- 📚 无需其他更改：作用域启用后，客户端可在下次授权请求中使用。

---

### [GitHub - Agent-Field/agentfield: 像 API 和微服务一样构建、运行和扩展 AI 智能体——从第一天起就具备可观测、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平面，能将 AI 代理构建为可调用的 API，并提供生产级基础设施支持。

- 🤖 **核心功能**：将 Python、Go 或 TypeScript 编写的代理逻辑转化为 REST 端点，支持路由、协调、记忆和异步执行。
- 🧠 **AI 集成**：通过 `app.ai()` 调用 LLM 获取结构化输出，支持 100+ 模型、流式响应和工具发现。
- 🔧 **开发体验**：提供 CLI 脚手架 (`af init`)、热重载、自动注册，支持 Claude Code 等编码代理。
- 🚀 **生产特性**：支持异步执行、人工审批（`app.pause()`）、金丝雀部署、A/B 测试和蓝绿部署。
- 🔒 **安全与治理**：每个代理拥有 W3C DID 加密身份，提供防篡改的可验证凭证和标签策略执行。
- 📊 **可观测性**：自动生成工作流 DAG、Prometheus 指标、结构化日志和执行时间线。
- 🌐 **多语言支持**：提供 Python、Go、TypeScript SDK，以及 REST API 和 Docker/Kubernetes 部署。
- 🏗️ **架构**：无状态 Go 控制平面，代理可连接自任何环境，支持分布式代理网格和自动服务发现。
- 📚 **应用案例**：包括自主工程团队、深度研究引擎、安全审计等生产级示例。

---

### [桌面应用 | Deno 文档](https://docs.deno.com/runtime/desktop/)

**原文标题**: [Desktop apps | Deno Docs](https://docs.deno.com/runtime/desktop/)

### 概述摘要  
deno desktop 可将 Deno 项目（从单个 TypeScript 文件到 Next.js 应用）打包为独立桌面应用，输出包含代码、Deno 运行时和 Web 渲染引擎的可分发二进制文件，支持跨平台编译和自动更新。

- 🖥️ **核心功能**：将 Deno 项目转为桌面应用，输出跨平台二进制文件（含运行时和渲染引擎）。  
- 🚀 **版本要求**：需 Deno v2.9.0 或更高版本。  
- ⚖️ **设计优势**：默认使用系统 WebView 减小体积，同时兼容 Node/npm 生态；支持框架自动检测（如 Next.js、Astro、Fresh 等）。  
- 🔗 **进程通信**：采用进程内绑定而非 IPC，减少跨进程开销，提升性能。  
- 🌍 **跨平台编译**：单机可构建 macOS、Windows、Linux 版本，后端按需下载。  
- 🔄 **自动更新**：内置二进制差异更新（bsdiff），支持自动回滚。  
- 📦 **快速入门**：通过 `deno desktop main.ts` 命令即可将 HTTP 服务转为桌面窗口。  
- 🛠️ **功能模块**：涵盖配置、后端选择（CEF/WebView）、HTTP 服务、框架集成、多窗口管理、菜单、托盘、对话框、通知、热更新、DevTools、自动更新、错误报告、分发及 CLI 参考。

---

### [Node.js — Node.js 26.4.0（当前版本）](https://nodejs.org/en/blog/release/v26.4.0)

**原文标题**: [Node.js — Node.js 26.4.0 (Current)](https://nodejs.org/en/blog/release/v26.4.0)

Node.js 26.4.0 版本发布，带来多项新功能与改进，包括文件系统、网络、TLS 等模块的增强，以及性能优化和错误修复。

- 📦 **文件系统增强**：支持调用者提供的 `readFile()` 缓冲区，并新增 `node:vfs` 虚拟文件系统子系统
- 🔒 **TLS 安全升级**：新增 `certificateCompression` 选项，支持证书压缩功能
- 🌐 **网络功能改进**：`setKeepAlive` 支持 `TCP_KEEPINTVL` 和 `TCP_KEEPCNT` 参数；新增同步 `connectSync()` 和 `bindSync()` 方法
- 📚 **模块加载优化**：实现包映射（package maps）功能，提升模块解析能力
- ⚡ **性能提升**：优化 `Buffer.prototype.copy`、流处理路径，减少 WHATWG 流热路径的内存分配
- 🛠️ **开发者工具**：调试器支持 `--max-hit` 选项，改进探针模式日志记录
- 🔧 **依赖更新**：升级 npm 至 11.17.0、OpenSSL 构建配置支持压缩、V8 新增 `CopyArrayBufferBytes` API
- 🐛 **错误修复**：修复 QUIC 连接数据丢失、SQLite 栈溢出、流编码处理等问题
- 📋 **文档改进**：更新 `blockList` 稳定性状态为候选发布版，修复多处文档错误
- 🔍 **测试与构建**：新增 QUIC CI 作业，优化构建配置，增加多项测试覆盖

---

### [发布 v12.0.0-pre.1 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.1)

**原文标题**: [Release v12.0.0-pre.1 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.1)

npm v12.0.0-pre.1 发布了重大更新，包含多项破坏性变更、新功能、错误修复和依赖升级，旨在提升安全性和开发体验。

- ⚠️ 破坏性变更：默认许可证从 "ISC" 改为空字符串，Git 操作保留 HTTPS 协议，Node.js 版本要求提升至 ^22.22.2 || ^24.15.0 || >=26.0.0，`allow-git` 和 `allow-remote` 默认设为 "none"，未知配置和标志将抛出错误。
- ✨ 新功能：支持 `packageExtensions` 修复依赖清单、原生依赖补丁（`npm patch add/commit/update/ls/rm`）、移除 `npm init` 默认许可证、审计修复时警告最小发布年龄、新增 `min-release-age-exclude` 配置、默认拒绝安装脚本（`allowScripts` 可选）、`allow-git` 和 `allow-remote` 默认设为 "none"、全局 `npmignore` 文件、`publish --access=private` 别名、未知配置和标志错误处理。
- 🐛 错误修复：保留 Git HTTPS 协议、补丁操作警告未安装版本、解释锁文件不同步、修复补丁重试标记、适配 `@npmcli/run-script@11` 变更、匹配带点号和版本号的参数、生成有效 JSON、传递 `script-shell` 到发布生命周期、识别本地链接的 `allowScripts`、验证注册表路径、列出待处理脚本、建议全局安装的 `--allow-scripts`、修复 YAML 缩进、显示完整父命令路径、尊重 `prune/dedupe/uninstall/audit fix/link` 中的 `allowScripts` 策略、阻止原型污染、运行根 `preinstall` 前安装依赖、暂停进度条等。
- 📚 文档：澄清 `approve-scripts` 全局错误、`package.json` 覆盖值、全局更新和过时版本、最小 npm 版本要求、环境变量文档。
- 🛠️ 依赖更新：升级了 `npm-profile`、`@tufjs/repo-mock`、`npm-packlist`、`@npmcli/git`、`sigstore`、`node-gyp`、`tar`、`ssri`、`semver`、`pacote` 等大量依赖包。
- 🧹 杂项：添加 web-login 代理回归修复、更新问题模板、清理标志表默认值、升级 `template-oss` 和开发依赖。

---

### [atproto 中没有实例 —— 过度反应](https://overreacted.io/there-are-no-instances-in-atproto/)

**原文标题**: [There Are No Instances in atproto — overreacted](https://overreacted.io/there-are-no-instances-in-atproto/)

### 概述总结
atproto 协议没有“实例”概念，它通过分离托管与应用，实现类似 RSS 的聚合式去中心化。

- 📡 **核心区别**：atproto 没有 Mastodon 式的“实例”，托管（数据存放）与应用（聚合展示）是分离的，类似 RSS 与 Google Reader 的关系。
- 🧩 **历史对比**：传统社交网络（如 Facebook）将托管与应用捆绑，导致中心化；Mastodon 通过多个“实例”去中心化，但用户身份绑定于特定实例，且实例间通信复杂。
- 🚀 **atproto 设计**：用户数据独立托管（可自选服务商），应用通过协议聚合数据，用户可自由切换托管或使用不同应用，无需受限于单一实例。
- 🔄 **去中心化方式**：在 atproto 中，去中心化通过更换托管服务、开发新应用实现，而非运行多个完整数据库副本；共享基础设施（如中继）成本低廉。
- ⚠️ **常见误解**：询问“Bluesky 实例数量”是类别错误，因为 atproto 没有实例；真正衡量去中心化的指标是用户是否迁移托管、是否尝试新应用。
- 💡 **解决思路**：将托管与应用解耦，避免 Mastodon 中“身份绑定实例”“实例间断联”等问题，赋予用户更高自主权。

---

### [如果 npm 运行在 AT 协议上会怎样？ | 詹姆斯·M·斯内尔](https://www.jasnell.me/posts/what-if-npm-ran-on-atproto)

**原文标题**: [What If npm Ran on AT Protocol? | James M Snell](https://www.jasnell.me/posts/what-if-npm-ran-on-atproto)

以下是对该文章的概述总结：

- 🤔 **核心构想**：将 npm 包注册表构建在 AT Protocol（Bluesky 协议）之上，利用其去中心化身份（DID）、个人数据服务器（PDS）和 Merkle 搜索树等原语。
- 📦 **数据模型映射**：包命名空间映射到 DID/域名句柄，元数据作为词条记录存储在用户仓库，tarball 作为附件，注册表变为只读聚合器（App View），发布通过中继火线实时传播。
- 🔑 **命名与组织**：消除全局命名空间，包按 DID 作用域隔离（如`@jsnell.dev/lodash`）；组织可运行自己的 PDS，并通过双重发布记录（组织签名 + 个人签名）实现归属审计，防止单点攻破。
- 🛡️ **信任模型**：密码学签名证明发布者身份和记录完整性，但不保证代码安全；结合 Sigstore 提供构建来源证明，形成身份 - 来源 - 构建的三方验证链。
- ⚠️ **名称解析风险**：App View 可能将包名映射到恶意 DID，需通过双重记录（发布者声明+App View 授权）实现可审计的名称解析，锁文件固定 DID 而非句柄。
- 🏷️ **标签系统**：独立标签服务可发布安全公告、恶意软件标记等，用户选择信任的标签器，打破 npm 单一数据库的垄断。
- 🚀 **性能潜力**：App View 通过火线预缓存所有元数据，支持服务端一次性解析整个依赖树，减少客户端多次往返请求。
- 🔒 **私有包**：通过独立网络（私有 PDS、中继、App View）实现，与公共网络隔离，但共享相同协议和工具。
- 🧩 **真正难点**：PDS 密钥托管问题（个人用户依赖托管方）、撤销传播延迟、性能未经验证、小型项目运行 PDS 的额外负担。
- 💡 **独特优势**：可组合信任、无单点攻破、结构依赖混淆抵抗、透明所有权转移、可移植身份、可审计名称解析、身份 - 来源绑定。

---

### [cssQuake - 由 PolyCSS 驱动](https://cssquake.com/)

**原文标题**: [cssQuake - Powered by PolyCSS](https://cssquake.com/)

该文本是一个游戏界面的菜单选项和设置列表，涵盖了多人游戏、操作控制、调试功能和游戏玩法选项。

- 🎮 **多人游戏设置**：包括创建房间、选择名称/颜色/地图、设置击杀上限和最大玩家数，以及房间已满和返回选项。
- ⌨️ **操作控制**：移动（WASD）、视角（鼠标）、射击（点击）、跳跃（空格）、奔跑（Shift）、蹲伏（Ctrl），菜单导航用方向键和回车。
- 🛠️ **调试功能**：可开关显示轮廓、统计面板、FPS 面板，以及录制、捕捉、可见性、DOM、敌人、拾取物和世界元素。
- ⚙️ **游戏玩法选项**：可调整准星样式、动态光照、静音、粒子效果、敌人显示、伤害/移动/攻击禁用、鼠标反转。
- 🎯 **特殊内容**：包含对象/物品和敌人相关设置。

---

