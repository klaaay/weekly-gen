### [前端聚焦第 701 期：2025 年 7 月 16 日](https://frontendfoc.us/issues/701)

**原文标题**: [Frontend Focus Issue 701: July 16, 2025](https://frontendfoc.us/issues/701)

概述总结  
- 🚀 严格限制条件下的创新：一个项目展示了在带宽和处理能力等严格限制下如何激发创新，并提醒设计时要考虑广泛的用户需求。  
- 🔒 简化前端安全：FusionAuth 提供简单几行代码即可实现登录、注册、SSO 和 MFA，支持 React、Vue、Angular 和原生 JavaScript。  
- 🍏 苹果浏览器引擎限制：苹果被指未遵守欧盟《数字市场法案》（DMA），未在 iOS 上开放浏览器引擎选择。  
- 🌐 WebAssembly 的应用：文章总结了 WebAssembly 在浏览器和服务器端的广泛应用，以及它如何渗透到各个领域。  
- 🔥 前沿动态：Mozilla 将在 Firefox 141 中支持 WebGPU（Windows 优先），AI 对开源开发者生产力的影响，以及 Firefox 团队征求用户反馈。  
- 📏 CSS 技巧：包括设置行长度、滚动驱动动画、堆叠变换等 CSS 新特性的应用和教程。  
- 🛠️ 工具与资源：介绍了 SveltePlot、Eleventy LibDoc、SplitThing、Chili3D 等工具，以及设计令牌和 SSR 检查工具。  
- 📢 呼吁与建议：开发者呼吁 ARIA Notify API 的广泛支持，并分享了纯 HTML 和 CSS 的现代应用案例。

---

### [比起我后来创造的一切，这 128 千字节更让我自豪 | 作者：Mike Hall | 2025 年 7 月 | Medium](https://medium.com/@mikehall314/im-more-proud-of-these-128-kilobytes-than-anything-i-ve-built-since-53706cfbdc18)

**原文标题**: [I’m more proud of these 128 kilobytes than anything I’ve built since | by Mike Hall | Jul, 2025 | Medium](https://medium.com/@mikehall314/im-more-proud-of-these-128-kilobytes-than-anything-i-ve-built-since-53706cfbdc18)

概述总结  
作者 Mike Hall 分享了一个在极端技术限制下（128KB 页面预算、老旧设备、弱网络环境）成功构建高性能、高兼容性网页项目的经历，通过创新设计和技术优化证明了美观与可访问性并非对立，而约束条件反而催生了更优雅的解决方案。  

- 🎨 **美观与可访问性共存**  
  反驳了“美观与 WCAG 指南无法兼顾”的观点，强调优秀设计应在约束中解决问题。  

- 📱 **极端技术限制**  
  项目目标：128KB 页面预算（含所有资源）、适配 240px 功能机至 4K 屏、兼容 Opera Mini（仅 2 秒 JS 执行时间）。  

- 🖥️ **系统字体替代方案**  
  放弃网页字体，使用设备默认字体以节省空间，避免 FOUT 问题，同时确保跨设备一致性。  

- 🛠️ **轻量级自研工具**  
  开发微型库 Whizz 替代主流框架，仅实现 DOM 操作和 AJAX，通过局部内容更新减少数据传输。  

- 🖼️ **图像优化技巧**  
  采用 SVG 为主（压缩至极致）、JPEG 双倍缩放降质法、TinyPNG 压缩，并为老旧设备提供 PNG 回退。  

- ✂️ **代码极致压缩**  
  HTML/CSS/JS全面手工优化，包括去除冗余标签、舍入SVG路径精度、甚至调整换行符节省字节。  

- 🆎 **品牌需求巧实现**  
  用 SVG 的`<defs>`复用路径模拟文字外描边效果，避免字体文件体积问题。  

- 🌍 **广泛兼容性验证**  
  最终产品在 Lynx、PSP、智能电视等非常规设备上流畅运行，弱网环境下表现远超竞品。  

- 💡 **约束激发创新**  
  项目证明严格限制能推动更普适、高效的解决方案，呼吁现代开发重新审视“少即是多”的价值。

---

### [苹果浏览器引擎禁令持续，即便在 DMA 下——开放网络倡导](https://open-web-advocacy.org/blog/apples-browser-engine-ban-persists-even-under-the-dma/)

**原文标题**: [Apple's Browser Engine Ban Persists, Even Under the DMA - Open Web Advocacy](https://open-web-advocacy.org/blog/apples-browser-engine-ban-persists-even-under-the-dma/)

Apple 在 DMA 法规下仍禁止第三方浏览器引擎，尽管法规明确要求开放竞争。Safari 作为苹果高利润产品，每年为苹果带来约 200 亿美元搜索收入，占其年运营利润的 14-16%。苹果通过技术限制和合同条款阻止其他浏览器引擎在 iOS 上运行，从而维持其市场垄断地位。

- 🚫 **苹果的浏览器引擎禁令**：苹果禁止第三方浏览器引擎在 iOS 上运行，尽管 DMA 明确禁止此类行为。
- 💰 **Safari 的高利润**：Safari 每年为苹果带来约 200 亿美元收入，占其运营利润的 14-16%。
- 🔧 **技术限制**：苹果设置多项技术障碍，如强制浏览器厂商创建全新应用，导致现有用户流失。
- 🌍 **全球影响**：苹果仅在欧洲允许第三方引擎，但限制使其商业上不可行。
- ⚖️ **DMA 合规问题**：苹果的行为被指不符合 DMA 的“有效合规”要求，仍在通过合同和技术手段限制竞争。
- 📉 **市场竞争受限**：苹果的限制削弱了浏览器和 Web 应用的竞争力，保护其 App Store 收入。
- 📢 **监管呼吁**：Open Web Advocacy 等组织呼吁欧盟调查苹果的合规性，并强制其做出改变。

---

### [WebAssembly：是的，但用来做什么？ - ACM Queue](https://queue.acm.org/detail.cfm?id=3746171)

**原文标题**: [WebAssembly: Yes, but for What? - ACM Queue](https://queue.acm.org/detail.cfm?id=3746171)

WebAssembly（Wasm）已发展十年，目前在部分领域取得成功但仍未完全发挥潜力。文章分析了 Wasm 的成功与失败案例，并探讨了其未来应用方向。

- 🎯 **早期成果与局限**  
  Wasm 在将 C++/Rust 桌面应用移植到 Web（如 Adobe Photoshop）和组件嵌入（如 SQLite）方面表现优异，但在游戏行业未成主流。

- 🌐 **Web 生态挑战**  
  JavaScript/TypeScript仍是Web开发首选，但WasmGC的推出为Java/Kotlin等语言提供了平等竞争的技术基础（如Google Sheets 已切换至 WasmGC）。

- 🔌 **非 Web 场景应用**  
  - 插件隔离（如 Firefox 通过 RLBox 沙箱化 C 库）  
  - 轻量虚拟化（如物联网固件升级、WALI 工具链替代容器）  
  - 组件模型（标准化跨模块交互，被 Shopify 等用于云服务扩展）。

- ☁️ **云计算的机遇**  
  Wasm 的毫秒级冷启动特性为边缘计算和 FaaS 提供了低延迟解决方案，但组件模型生态仍处于早期竞争阶段。

- 🔮 **未来方向**  
  聚焦安全隔离需求场景：内核驱动开发、替代 eBPF、构建 Wasm 操作系统，以及 AI 时代敏感数据的可信计算。

- ⚠️ **关键障碍**  
  语义鸿沟（如字符串需手动处理）、开发者生态偏好 JS/TS，以及组件模型标准化进程的未成熟性。

---

### [在 Firefox 141 中为 Windows 提供 WebGPU 支持——Mozilla 图形团队博客](https://mozillagfx.wordpress.com/2025/07/15/shipping-webgpu-on-windows-in-firefox-141/)

**原文标题**: [Shipping WebGPU on Windows in Firefox 141 – Mozilla Gfx Team Blog](https://mozillagfx.wordpress.com/2025/07/15/shipping-webgpu-on-windows-in-firefox-141/)

Firefox 141 将在 Windows 平台上发布 WebGPU 支持，这是一个现代化的图形处理器接口，旨在提升网页游戏、可视化和本地计算的性能。未来还将扩展至 Mac、Linux 和 Android 平台。

- 🚀 Firefox 141 将在 Windows 上推出 WebGPU 支持，为网页内容提供高性能图形计算和渲染能力。  
- 🌐 WebGPU 已在 Chrome 中提供，并预计在 Safari 26 中推出。  
- 🛠️ Firefox 的 WebGPU 实现基于 WGPU，一个跨平台的 Rust 库，支持 Direct3D 12、Metal 和 Vulkan。  
- 📅 未来计划包括在 Mac、Linux 和 Android 上推出 WebGPU 支持。  
- ⚡ 目前存在一些性能问题，如 IPC 开销和任务完成检测延迟，将在后续版本中优化。  
- 🐞 用户可通过 Bugzilla 报告问题，并提供详细的重现步骤和系统信息。  
- 🔧 开发人员可通过 WGPU 项目参与贡献，这是一个活跃的开源项目。  
- 🎮 WebGPU 有望推动网页 3D 图形和计算的未来发展。

---

### [衡量 2025 年初 AI 对资深开源开发者生产力的影响 - METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

**原文标题**: [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity - METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

2025 年初 AI 技术对资深开源开发者生产力的影响评估  

- 🤖 **生产力提升**：AI 工具显著提高了代码编写和调试效率，减少了重复性任务的时间消耗。  
- 🛠️ **工具整合**：开发者更频繁地使用 AI 辅助工具，如代码补全、错误检测和自动化测试。  
- 📊 **数据驱动**：研究显示，使用 AI 的开发者在项目完成速度上平均提升了 30%-50%。  
- 🌍 **社区协作**：AI 促进了跨时区协作，通过智能翻译和文档生成降低了沟通壁垒。  
- 🔍 **挑战与适应**：部分开发者面临学习曲线，需适应 AI 工具的工作流程和决策逻辑。  
- 💡 **创新加速**：AI 帮助快速原型设计，推动更多实验性项目和创意解决方案的出现。  
- ⚖️ **伦理考量**：开源社区开始讨论 AI 生成代码的版权归属和贡献者身份认定问题。

---

### [火狐浏览器的下一步方向？由你决定。- Mozilla Connect](https://connect.mozilla.org/t5/discussions/where-s-firefox-going-next-you-tell-us/m-p/100698)

**原文标题**: [
	Where’s Firefox going next? You tell us. - Mozilla Connect
](https://connect.mozilla.org/t5/discussions/where-s-firefox-going-next-you-tell-us/m-p/100698)

自动建议功能可在您输入时提供可能的匹配项，帮助快速缩小搜索结果范围。

- 🔍 自动建议功能实时提供搜索建议  
- ⚡ 提升搜索效率，快速缩小结果范围  
- 💡 输入时动态显示可能匹配项  
- 🎯 帮助用户更精准地找到目标内容

---

### [@bell.bz 在 Bluesky](https://bsky.app/profile/bell.bz/post/3ltvwqogl7k22)

**原文标题**: [@bell.bz on Bluesky](https://bsky.app/profile/bell.bz/post/3ltvwqogl7k22)

这是一个关于 Bluesky 互动网页应用及 CSS 技巧的简短内容。  

- 🌐 这是一个高度互动的网页应用，必须启用 JavaScript 才能使用。  
- 📖 了解更多关于 Bluesky 的信息，请访问 [bsky.social](bsky.social) 和 [atproto.com](atproto.com)。  
- ✍️ 用户 Andy Bell（bell.bz）分享了一条 CSS 技巧。  
- 💡 CSS 小贴士：使用 `:target { scroll-margin-block-start: 2em; }` 可以为通过 URL 锚点跳转的元素（如 example.com/#my-element）增加呼吸空间。  
- ⏰ 发布时间：2025 年 7 月 14 日 08:09:20（UTC）。

---

### [在 CSS 中设置行长度（及文本适应容器） | CSS-Tricks](https://css-tricks.com/setting-line-length-in-css-and-fitting-text-to-a-container/)

**原文标题**: [Setting Line Length in CSS (and Fitting Text to a Container) | CSS-Tricks](https://css-tricks.com/setting-line-length-in-css-and-fitting-text-to-a-container/)

文章概述了如何通过 CSS 设置文本行长度以及如何让文本适应容器宽度，同时探讨了未来可能的 CSS 新特性。

- 📏 **行长度定义**：行长度指多行文本容器的宽度，过长会导致阅读困难。  
- 🎯 **WCAG 建议**：每行不超过 80 字符（中文等语言不超过 40 字符），可用`ch`单位实现（如`width: 80ch`）。  
- 🔍 **最佳行长度**：研究表明 50-75 字符为最佳范围，需结合响应式设计灵活调整。  
- ⚙️ **动态调整工具**：推荐使用`clamp()`和`min()`函数实现响应式行长度（如`width: clamp(min(93.75vw, 50ch), 70vw, 75ch)`）。  
- 📐 **文本适应容器（JS）**：通过 SVG 和少量 JS 代码实现标题文本自适应容器宽度，继承 CSS 样式。  
- 🧩 **纯 CSS 方案**：Roman Komarov 的复杂方案利用容器查询和数学计算，但需重复文本和自定义属性。  
- 🔮 **未来特性展望**：可能引入`text-grow`和`text-shrink`属性，支持多行文本缩放，但存在争议（如更倾向`font-size: fit-width`）。  
- 💡 **总结与参与**：当前 CSS 工具已大幅简化行长度设置，鼓励开发者通过 GitHub 反馈未来特性需求。

---

### [多列布局与分段 - Rachel Andrew - CSS Day 2025 - YouTube](https://www.youtube.com/watch?v=NfwDP9shxNQ)

**原文标题**: [Multicol and fragmentation - Rachel Andrew - CSS Day 2025 - YouTube](https://www.youtube.com/watch?v=NfwDP9shxNQ)

关于 YouTube 的相关信息与链接  

- 📢 关于 - 提供 YouTube 平台的背景和基本信息  
- 🗞️ 媒体 - 查看 YouTube 的新闻和公告  
- ©️ 版权 - 了解版权相关政策和信息  
- 📩 联系我们 - 获取与 YouTube 联系的途径  
- 🎨 创作者 - 资源和支持内容创作者的信息  
- 💼 广告 - 广告合作和推广相关内容  
- 👩💻 开发者 - 开发者工具和 API 信息  
- 📜 条款 - 使用 YouTube 的服务条款  
- 🔒 隐私 - 隐私政策和数据保护措施  
- ⚖️ 政策与安全 - 平台规则和安全指南  
- 🔧 YouTube 工作原理 - 平台运作机制解析  
- 🧪 测试新功能 - 体验和反馈最新功能  
- © 2025 Google LLC - 版权归属声明

---

### [CSS 多栏布局模块第二级](https://www.w3.org/TR/css-multicol-2/)

**原文标题**: [CSS Multi-column Layout Module Level 2](https://www.w3.org/TR/css-multicol-2/)

CSS 多列布局模块概述  
该模块描述了 CSS 中的多列布局功能，允许元素内容分布在多个列中，同时保持子元素的正常流。  

- 📜 **多列容器**：通过设置`column-width`或`column-count`将元素变为多列容器，子元素仍按正常流排列，列宽自适应可用空间。  
- 🛠️ **属性控制**：  
  - `column-width`：指定列的理想宽度（如`12em`），实际宽度可能调整以填充空间。  
  - `column-count`：固定列数（如`2`），宽度随容器变化。  
  - `columns`：简写属性，可同时设置列数和宽度（如`columns: 2 12em`）。  
- 📏 **间隙与分隔线**：  
  - `column-gap`：定义列间间隙（如`1em`）。  
  - `column-rule`：在间隙中央添加分隔线（类似边框样式，如`thin solid black`）。  
- 🔄 **内容分布**：  
  - `column-fill`：控制列是否平衡高度（`balance`）或顺序填充（`auto`）。  
  - `column-span`：元素跨越多列（如`all`跨所有列，或指定整数跨部分列）。  
- ⏯️ **分列与溢出**：  
  - 内容超出列高时会分片到下一列。  
  - 溢出列在连续上下文中可见，在分页媒体中移至下一页。  
- 🖌️ **样式限制**：列盒子为匿名盒子，无法直接设置背景、边距等属性。  

示例：  
```css  
body {  
  columns: 2 12em;  
  column-gap: 1em;  
  column-rule: thin solid black;  
}  
h2 { column-span: all; }  
```  
该规范还涉及分列算法、堆叠上下文及与分页媒体的交互，确保布局灵活且适应不同场景。

---

### [如何使用 Clerk、Lovable 和 Supabase 构建 AI 编码规则应用](https://clerk.com/blog/build-app-with-lovable-supabase-clerk?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=ai-coding-rules&utm_content=07-16-25-fef&dub_id=WaIt7IKo1LZKVDqH)

**原文标题**: [How to build an AI coding rules app with Clerk, Lovable, and Supabase](https://clerk.com/blog/build-app-with-lovable-supabase-clerk?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=ai-coding-rules&utm_content=07-16-25-fef&dub_id=WaIt7IKo1LZKVDqH)

本文介绍了如何利用 Clerk、Lovable 和 Supabase 构建一个安全的 AI 编码规则应用。通过结合这些工具，开发者可以快速搭建全栈应用，实现用户认证和数据存储功能。

- 🛠️ 使用 Lovable 的 AI 生成器、Clerk 进行认证和 Supabase 进行数据存储，构建安全的全栈应用。
- 🤖 Lovable 是一个 AI 驱动的“氛围编码”平台，允许开发者通过聊天与 AI 代理构建全栈应用和网站。
- 🔐 Clerk 是一个用户管理和认证平台，可以快速将认证添加到应用中。
- 📦 Supabase 是一个开源的 BaaS，基于 PostgreSQL，支持 RLS 等高级功能，并与 Clerk 和 Lovable 集成良好。
- 📝 通过 Lovable 的提示功能，用户可以创建应用来存储 AI 编码规则，并为不同的项目添加标签。
- 🔧 在构建过程中，可能会遇到认证失败或类型不匹配等问题，可以通过重新提示或调整配置来解决。
- 🚀 结合 AI 和现代开发工具，开发者可以更快地原型设计和发布应用，但仍需人工监督以确保应用的正确构建。

---

### [滚动驱动粘性标题 | CSS-Tricks](https://css-tricks.com/scroll-driven-sticky-heading/)

**原文标题**: [Scroll-Driven Sticky Heading | CSS-Tricks](https://css-tricks.com/scroll-driven-sticky-heading/)

概述总结  
滚动驱动动画是一种强大的技术，通过将元素的运动和变化与用户的滚动位置直接绑定，可以创建动态、互动性强的网页体验。本文介绍了如何利用伪元素和 CSS 动画实现滚动驱动的标题变换效果，并强调了无障碍支持和浏览器兼容性的重要性。

- 🎯 **滚动驱动动画简介**  
  通过滚动位置控制元素动画，增强网页互动性和视觉效果。

- 🔍 **技术实现**  
  使用伪元素的`content`属性动态改变文本，结合`@supports`检测浏览器支持。

- 🛠️ **基础设置**  
  从语义化 HTML 开始，确保无障碍支持，静态内容作为回退方案。

- 📏 **关键帧与魔法数字**  
  通过实验确定滚动百分比触发点（如 30%、60%、90%），使用`step-end`确保文本切换精准。

- ♿ **无障碍与兼容性**  
  通过`aria-hidden`和`.srOnly`类分离动画标题与静态标题，确保辅助技术和不支持 SDA 的浏览器正常显示内容。

- 🌈 **动画增强**  
  可扩展动画效果，如文本颜色渐变或背景色变化，提升视觉吸引力。

- ⚠️ **用户偏好**  
  通过`prefers-reduced-motion`媒体查询尊重用户减少动画的偏好。

- 💡 **创意扩展**  
  鼓励开发者尝试更多滚动驱动动画的可能性，创造独特网页体验。  

- 🙏 **致谢**  
  特别感谢 Cristian Díaz 对示例的无障碍审查和改进建议。

---

### [堆叠变换 – Frontend Masters 博客](https://frontendmasters.com/blog/stacked-transforms/)

**原文标题**: [Stacked Transforms – Frontend Masters Blog](https://frontendmasters.com/blog/stacked-transforms/)

概述：Chris Coyier 在 CSS Day 活动中了解到 `animation-composition` 属性，并通过实验和示例详细解释了其工作原理和应用场景，特别是与 `transform` 属性的结合使用。

- 🎨 Chris Coyier 在 CSS Day 的 CSS Café 活动中首次了解到 `animation-composition` 属性，并对其功能产生兴趣。  
- 📝 他通过阅读 MDN 文档和实际实验，探索了 `animation-composition` 的三种行为：`replace`（默认）、`add` 和 `accumulate`。  
- 🔄 `replace` 会完全替换元素原有的 `transform` 值，而 `add` 会将动画的 `transform` 值追加到原有值之后。  
- ➕ `accumulate` 则会累加匹配的 `transform` 值（如 `translateX`），而不是简单追加。  
- 🐢 为了帮助理解，Chris 用 Logo 语言中的“乌龟”动画示例演示了 `transform` 值的叠加效果。  
- ⚠️ 需要注意的是，`animation-composition` 不仅适用于 `transform`，也适用于其他属性如 `opacity`，但其行为可能有所不同。  
- 📚 他推荐了 David Khourshid 的 CSS 动画课程，供读者深入学习。

---

### [动画合成 - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-composition)

**原文标题**: [animation-composition - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-composition)

CSS 的`animation-composition`属性用于指定当多个动画同时影响同一属性时的复合操作方式。

- 🆕 该功能自 2023 年 7 月起在最新设备和浏览器版本中可用，旧版本可能不支持。  
- 🎨 属性语法支持三种复合操作：`replace`（覆盖默认值）、`add`（叠加效果）、`accumulate`（累积值）。  
- 🔄 多动画场景下，属性值按`animation-name`顺序循环分配。  
- 📊 示例展示了不同值对`transform`属性的影响：`replace`会替换基础值，`add`会叠加变换，`accumulate`会合并数值。  
- 📚 适用于所有元素，不可继承，默认值为`replace`。  
- 🌐 兼容性需查看最新浏览器支持情况，相关资源包括 CSS 动画教程和其他动画属性。

---

### [请给我们 ARIA Notify - Nic Chan](https://www.nicchan.me/blog/please-can-we-have-aria-notify/)

**原文标题**: [Please, can we have ARIA Notify - Nic Chan](https://www.nicchan.me/blog/please-can-we-have-aria-notify/)

文章讨论了 ARIA Notify API 的必要性以及当前 ARIA 实时区域的局限性，强调了开发者在使用实时区域时面临的挑战和问题。

- 🎯 作者对 ARIA Notify API 的推出表示期待，认为它将改善屏幕阅读器通知的现状。
- ⚠️ 实时区域存在不一致性和不可预测性，实现起来复杂且容易出错。
- 🛠️ 在开发 Audiom 时，实时区域是必要的，但使用体验并不理想。
- 👀 实时区域在隐藏状态下无效，必须存在于 DOM 中，可能造成用户混淆。
- 🕹️ 在模态对话框中使用实时区域需要额外的管理，增加了复杂性。
- 😩 开发者因实时区域的复杂性而难以正确实现，导致无障碍功能受限。
- 🔄 实时区域的规范本身存在不一致性，不同辅助技术表现不同。
- 🌍 国际化问题使得实时区域和 ARIA 标签在翻译工具中表现不佳。
- 💡 ARIA Notify API 有望提供更好的控制和用户体验，但需解决现有问题。
- 📢 作者呼吁改进屏幕阅读器通知机制，以更轻松地创建无障碍应用。

---

### [获取失败](https://frontendfoc.us/link/171878/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/171878/web)

无法总结：获取内容失败，状态码 403。

---

### [2025 年我为何选择纯 HTML 与 CSS 进行创作](https://joeldare.com/why-im-writing-pure-html-and-css-in-2025)

**原文标题**: [Why I’m Writing Pure HTML & CSS in 2025](https://joeldare.com/why-im-writing-pure-html-and-css-in-2025)

作者在 2025 年选择使用纯 HTML 和 CSS 构建网页，强调其高效、简洁和可持续的优势。

- 🚀 **极速加载与部署**：纯 HTML 和 CSS 页面加载快、部署简单，无需复杂框架或脚本。  
- 🛠️ **开发轻松愉快**：摒弃过度工程化，回归基础技术，构建过程简单高效。  
- 🌿 **历久弥新**：HTML 自 1991 年诞生至今仍兼容现代浏览器，基础文档需求无需复杂设计。  
- 🐢 **页面臃肿问题**：2024 年研究显示网页平均体积达 2.65MB 且逐年增长，影响性能与可访问性。  
- 🌐 **普适托管方案**：纯 HTML 可托管于 GitHub、免费云服务甚至树莓派，成本极低。  
- ♿ **无障碍与 SEO 优势**：语义化 HTML 自动提升可访问性和搜索引擎排名，无需额外开发。  
- 🔒 **安全性高**：静态页面几乎无攻击面，免于安全补丁和依赖更新困扰。  
- ⚡ **无构建步骤**：直接通过`git push`部署，省去复杂工具链和配置流程。  
- 📧 **倡导简约实践**：作者推出免费课程，鼓励开发者尝试纯 HTML/CSS 构建生产级页面。

---

### [获取失败](https://frontendfoc.us/link/171826/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/171826/web)

无法总结：获取内容失败，状态码 403。

---

### [设计滚动行为：何时保存用户位置 - NN/g](https://www.nngroup.com/articles/saving-scroll-position/)

**原文标题**: [Designing Scroll Behavior: When to Save a User’s Place - NN/g](https://www.nngroup.com/articles/saving-scroll-position/)

文章概述了在设计滚动行为时保存用户位置的重要性，并探讨了何时应保存或重置滚动位置以优化用户体验。

- 📜 保存滚动位置能减少用户操作成本，尤其在长列表浏览时避免重复滚动。  
- 🔄 当用户频繁返回同一页面（如电商比价、播客浏览）时，保存位置能提升效率。  
- ⏱️ 若内容实时更新（如新闻、体育赛事），应重置滚动位置以确保用户看到最新信息。  
- 🕒 长时间未访问后返回页面时，重置位置可帮助用户重新建立浏览上下文。  
- 🤔 用户意图不明确时，默认保存位置并提供快捷重置选项（如“跳至最新消息”）是低干扰设计。  
- 🎯 滚动行为设计需结合具体场景，细微差异可能显著影响用户体验。

---

### [AI 没有扼杀网页设计——模板才是始作俑者](https://webdesignerdepot.com/ai-didnt-kill-web-design-templates-did-it-first/)

**原文标题**: [AI Didn’t Kill Web Design —Templates Did It First](https://webdesignerdepot.com/ai-didnt-kill-web-design-templates-did-it-first/)

页面加载速度不再是唯一关键，CLS（布局偏移）已成为用户体验的核心指标，设计师需比开发者更重视其影响。  

- 🎨 **设计师责任重大**：CLS 主要由视觉布局变动引起，设计师需在早期规划中避免元素动态位移。  
- ⚡ **用户体验优先**：频繁的布局偏移会导致用户误点击、阅读中断，直接影响留存率与转化率。  
- 🛠️ **协作必要性**：开发者依赖设计稿实现，若设计未考虑 CLS，后期修复成本高昂。  
- 📊 **量化标准**：CLS 评分低于 0.1 为优，超过 0.25 则需紧急优化，需通过工具（如 Lighthouse）持续监测。  
- 🌐 **响应式设计挑战**：多设备适配易引发布局偏移，设计师需提前测试不同视口下的稳定性。

---

### [GitHub - svelteplot/svelteplot: Svelte 绘图框架](https://github.com/svelteplot/svelteplot)

**原文标题**: [GitHub - svelteplot/svelteplot: Svelte Plotting Framework](https://github.com/svelteplot/svelteplot)

SveltePlot 是一个基于分层图形语法理念的可视化框架，其 API 设计灵感来源于 Observable Plot，由 Gregor Aisch 创建。  

- 🌟 **项目信息**：SveltePlot 是一个 Svelte 绘图框架，官网为 svelteplot.dev  
- 📜 **许可证**：采用 ISC 许可证  
- ⭐ **关注度**：获得 216 颗星，13 个复刻  
- 🛠 **开发状态**：最新版本为 v0.3.7（2025 年 7 月 8 日发布），共有 15 个版本发布  
- 📂 **代码结构**：主要使用 TypeScript（49%）和 Svelte（47.3%）开发  
- 🔍 **功能特点**：支持数据可视化和交互式可视化，适用于数据分析  
- ❗ **错误提示**：页面加载时可能出现错误，需重新加载  
- 👥 **贡献者**：共有 10 位贡献者参与项目开发

---

### [示例 - SveltePlot](https://svelteplot.dev/examples)

**原文标题**: [Examples - SveltePlot](https://svelteplot.dev/examples)

SveltePlot 是一个基于 Svelte 框架的数据可视化工具，提供丰富的图表类型和交互功能，适合快速构建动态图表。

- 📊 **SveltePlot 简介**：基于 Svelte 的数据可视化框架，支持多种图表和交互功能。  
- 🚀 **快速入门**：提供详细指南和示例，帮助用户快速上手。  
- 🌟 **核心功能**：包括绘图（Plot）、标记（Marks）、比例尺（Scales）、转换（Transforms）和分面（Facets）。  
- 📈 **标记类型**：支持多种图表类型，如面积图（Area）、柱状图（Bar）、散点图（Dot）、地图（Geo）等。  
- 🔄 **数据转换**：提供丰富的数据处理功能，如分组（Group）、排序（Sort）、堆叠（Stack）等。  
- 🎨 **高级功能**：支持渐变（Gradients）、交互（Interactivity）、投影（Projections）等。  
- 📚 **示例丰富**：涵盖多种场景，如渐变折线图、美国地图、地震数据可视化等。  
- ⏱ **最后更新**：2025 年 7 月 8 日。

---

### [GitHub - ita-design-system/eleventy-libdoc：用于制作精美文档的Eleventy入门项目](https://github.com/ita-design-system/eleventy-libdoc)

**原文标题**: [GitHub - ita-design-system/eleventy-libdoc: An Eleventy starter project to craft slick documentation](https://github.com/ita-design-system/eleventy-libdoc)

一个基于 Eleventy 的文档生成工具，专注于简洁、响应式和无障碍的文档设计，具有高性能和低技术依赖的特点。

- 🚀 **项目简介**: Eleventy LibDoc 是一个易于使用、内容优先的 Eleventy 启动项目，用于创建响应式文档。  
- 🔍 **核心功能**: 包括搜索、主导航、目录、代码高亮和沙盒等自建组件，支持无 JavaScript 运行。  
- 🏗️ **快速开始**: 克隆仓库后运行`npm install`，配置`settings.json`即可构建。  
- ♿ **无障碍设计**: 开发时注重无障碍访问，确保广泛兼容性。  
- ⚡ **高性能**: 低前端依赖和原生 JavaScript 组件保障良好性能。  
- 📄 **内容展示**: 支持多格式内容呈现，包括可打印页面和沙盒演示。  
- 🔧 **配置灵活**: 提供详细的配置参数和 SEO 优化选项。  
- 🌐 **在线文档**: 包含全面的使用说明和参数文档。  
- 📊 **项目状态**: 102 星，12 分支，最新版本 v0.6.0（2025 年 7 月发布）。  
- 👥 **贡献者**: 由 Olivier 3lanc 和 Tyler V 维护，主要语言为 CSS 和 JavaScript。

---

### [Eleventy LibDoc](https://eleventy-libdoc.netlify.app/)

**原文标题**: [Eleventy LibDoc](https://eleventy-libdoc.netlify.app/)

Eleventy LibDoc 是一个专注于内容、易于使用的 Eleventy 起始项目，用于创建响应式文档。它注重无障碍性和性能，包含多种自建组件，支持无 JavaScript 环境，且页面可打印。

- 🚀 **项目概述**：Eleventy LibDoc 是一个用于创建响应式文档的 Eleventy 起始项目，注重无障碍性和性能。
- 📂 **快速开始**：克隆仓库后运行 `npm install`，配置 `settings.json`，并通过 `npx @11ty/eleventy --serve` 启动。
- 🌟 **主要特性**：
  - 内容优先，易于安装和使用。
  - 无障碍设计，兼容多种浏览器。
  - 高性能，低前端依赖。
  - 支持搜索、智能导航和浮动目录。
  - 无 JavaScript 时仍可运行基本功能。
  - 图片转码和响应式代码高亮。
- ⚙️ **配置**：通过 `settings.json` 设置网站标题、描述、Logo、作者、Favicon 等。
- 📝 **创建内容**：支持 Markdown、HTML 和多种小部件（如警告、按钮、图标卡片等）。
- 🏠 **主导航**：包含首页链接、搜索输入和 Eleventy 导航，支持无限层级。
- 📁 **文件结构**：
  - `_data/`：全局数据配置。
  - `_includes/`：模板文件。
  - `assets/`：用户静态文件。
  - `core/`：系统 UI 资源。
- 📄 **其他文件**：如 `.eleventy.js`、`settings.json` 等用于项目配置。

---

### [分物](https://splitthing.therealflo.dev/)

**原文标题**: [SplitThing](https://splitthing.therealflo.dev/)

SplitThing 是一个工具，允许用户上传图片并将其分割成自定义的网格。

- 🖼️ 上传图片：支持拖放或点击浏览选择图片  
- 🔢 自定义网格：可设置行数和列数来分割图片  
- 📦 下载结果：分割后的图片可以打包成 ZIP 格式下载  
- 👀 实时预览：上传图片后可即时查看分割效果  
- ©️ 版权信息：由 Florian Reintgen 开发并保留所有权利  
- 💻 开源代码：可在 GitHub 上查看项目源代码

---

### [GitHub - xiangechen/chili3d：一款基于网页的3D CAD 应用，支持在线模型设计与编辑](https://github.com/xiangechen/chili3d)

**原文标题**: [GitHub - xiangechen/chili3d: A web-based 3D CAD application for online model design and editing](https://github.com/xiangechen/chili3d)

Chili3D 是一个基于浏览器的开源 3D CAD 应用程序，支持在线模型设计和编辑，采用 TypeScript 开发，通过 WebAssembly 实现高性能。

- 🌐 **项目概述**: 基于 Web 的 3D CAD 工具，无需本地安装，支持在线建模和编辑。
- 🛠️ **核心功能**: 提供基础形状创建、2D 草图绘制、布尔运算、高级编辑工具等。
- 📏 **精准操作**: 支持对象捕捉、工作平面捕捉、轴跟踪和特征点检测。
- 🔄 **编辑工具**: 包括倒角、圆角、修剪、移动、旋转等操作。
- 📐 **测量工具**: 可测量角度、长度，计算面积和体积。
- 📁 **文档管理**: 支持创建、打开、保存文档，导入/导出 STEP、IGES、BREP 格式。
- 🌍 **多语言支持**: 目前支持中文和英文，欢迎贡献其他语言。
- ⚙️ **技术栈**: 使用 TypeScript、Three.js、OpenCascade（通过 WebAssembly）、Rspack 构建工具。
- 🚀 **开发状态**: 处于早期开发阶段，核心 API 可能变动，功能正在完善中。
- 📜 **许可证**: 采用 AGPL-3.0 许可证，商业许可需联系作者。
- 📧 **联系方式**: 通过 GitHub 讨论或邮箱 xiangetg@msn.cn 联系。

---

### [辣椒 3D](https://chili3d.com/)

**原文标题**: [chili3d](https://chili3d.com/)

该内容提示需要启用 JavaScript 才能运行应用。

- 🛠️ 需要启用 JavaScript 以运行此应用

---

### [designtokens.fyi](https://designtokens.fyi/)

**原文标题**: [designtokens.fyi](https://designtokens.fyi/)

设计令牌相关术语及其概念的简要介绍  

- 🏷️ **Alias** - 设计令牌的别名，用于引用其他令牌  
- 🏋️ **Bloat** - 设计系统中过度膨胀或冗余的令牌  
- 🤔 **Choice** - 设计决策中的选择与权衡  
- 🧩 **Component** - 设计令牌关联的 UI 组件  
- 🛠️ **Custom Property** - 自定义属性（如 CSS 变量）  
- ✂️ **Delimiter** - 分隔符，用于命名约定（如“-”或“_”）  
- 🌐 **DTCG** - 设计令牌社区组织（Design Tokens Community Group）  
- 🌍 **Global** - 全局作用域的令牌  
- 📊 **Graph** - 令牌关系的可视化表示  
- 🎯 **Intent** - 令牌的设计意图或用途  
- 👆 **Interaction** - 与用户交互相关的令牌  
- 📝 **JSON** - 令牌常用的数据格式  
- 📶 **Level** - 令牌的层级结构（如基础、语义等）  
- 🏠 **Local** - 局部作用域的令牌  
- 🎨 **Mise en Mode** - 设计模式的应用  
- 🌓 **Mode** - 主题模式（如亮/暗模式）  
- 📂 **Namespace** - 命名空间，用于组织令牌  
- ⚙️ **Option** - 可配置的令牌选项  
- 🔢 **Primitive** - 原始值（如颜色、间距等基础令牌）  
- ⚡ **Priority** - 令牌的优先级或覆盖顺序  
- 🔧 **Property** - 令牌对应的属性（如`color`或`font-size`）  
- ❓ **Purpose** - 令牌的特定用途说明  
- 📏 **Scale** - 刻度系统（如间距、字体大小的阶梯值）  
- 🗃️ **Schema** - 令牌的结构化定义规范  
- 🔍 **Scope** - 令牌的作用范围（全局/局部）  
- 💡 **Semantic** - 语义化令牌（如`primary-color`）  
- 📐 **Smedium** - 介于小（Small）和中（Medium）之间的尺寸  
- 🏷️ **State** - 组件状态相关的令牌（如悬停、禁用）  
- 👕 **T-shirt** - T 恤尺码命名法（XS/S/M/L/XL）  
- 🎭 **Theme** - 主题相关的令牌集合  
- ⬆️ **Tier** - 令牌的分层（如基础、组件、主题）  
- 🏷️ **Token** - 设计系统的最小样式单元  
- 🔄 **Variable** - 动态引用的变量值

---

### [检查服务器端渲染（SSR）](https://punits.dev/check-server-side-rendered/)

**原文标题**: [Check Server-side Rendering (SSR)](https://punits.dev/check-server-side-rendered/)

该工具用于检测网页的服务器端渲染（SSR）问题，通过对比禁用和启用 JavaScript 的页面版本，帮助用户识别未进行 SSR 的内容，并提供优化建议。

- 🌐 **工具功能**：检测网页中未进行服务器端渲染的部分，通过对比不同渲染方式的页面版本。
- 🔍 **使用方式**：输入 URL，选择用户代理（如 Googlebot、Chrome 等），工具会显示服务器端渲染和常规渲染的对比。
- ⚡ **SSR 重要性**：服务器端渲染能加快内容显示速度，并影响搜索引擎爬虫的索引效率。
- 🆓 **免费使用**：目前工具免费，旨在收集用户反馈以改进功能。
- 📅 **结果存储**：未登录用户的结果存储 2 天，登录用户存储 7 天。
- 🛠️ **开发者背景**：由 Punit Sethi 创建，用于团队内部沟通 SSR 问题，现开放给 SEO 专家、网站所有者等使用。
- 📧 **反馈渠道**：用户可发送邮件至 punit@tezify.com 报告问题或提出新功能建议。
- 📜 **法律信息**：工具版权归 Tezify 所有，创建于印度，提供隐私政策和服务条款链接。

---

### [FontGen - 字体配对工具](https://www.fontgen.io/)

**原文标题**: [FontGen - Typography Pairing Tool](https://www.fontgen.io/)

FontGen 是一个帮助设计师和开发者快速找到完美字体搭配的工具，提供直观的界面和强大的功能，提升排版效率与美感。

- 🎨 完美字体搭配：通过智能工具快速生成视觉层次分明的字体组合，提升设计效果。  
- 🔄 随机字体生成：一键点击即可自动生成新的字体组合，激发设计灵感。  
- 🔒 锁定偏好字体：在探索其他选项时保留喜欢的标题或正文字体，灵活调整排版。  
- 💾 保存收藏组合：高级用户可无限保存字体组合，建立个人字体库以便随时调用。  
- 📊 海量资源支持：1000+ 字体、50 万 + 组合可能性、15+ 排版分类，搭配可能性无限。  
- 🚀 快速上手：加入数千设计师与开发者的行列，用智能工具轻松打造精美排版。

---

### [GitHub - SaintSin/astro-pandabox: 适用于 Astro 的轻量级 Lightbox 和画廊组件](https://github.com/SaintSin/astro-pandabox)

**原文标题**: [GitHub - SaintSin/astro-pandabox: A lightweight Lightbox and gallery component for Astro](https://github.com/SaintSin/astro-pandabox)

一个轻量级的 Lightbox 和图库组件，专为 Astro 设计，支持内容集合、触摸滑动和自定义过渡效果。

- 🚀 **项目名称**: Pandabox - 一个轻量级的 Lightbox 和图库组件，适用于 Astro  
- 🌟 **功能特点**:  
  - 支持内容集合（Content Collections），包括 alt 文本、标题和描述  
  - 使用 Astro 的 Image 组件进行图片优化  
  - 无依赖，现代 CSS 实现  
  - 自定义过渡效果（淡入淡出或滑动）  
  - 触摸滑动切换图片  
- 📂 **文件结构**:  
  - 主要组件文件：`Pandabox.astro`  
  - 配置文件：`config.ts`（用于内容集合）  
  - 图库数据存储在 JSON 文件中（如`content/galleries/panda.json`）  
- ⚙️ **使用方法**:  
  - 在页面中引入`Pandabox.astro`组件  
  - 通过`galleryid`指定 JSON 文件，`transitionType`设置过渡效果（`fade`或`slide-in`）  
- 🎨 **自定义样式**:  
  - 通过 CSS 变量控制过渡时间、缓动效果等（如`--duration-zoom-in`、`--ease-slide-transition`）  
- 📜 **许可证**: MIT  
- 🌐 **演示地址**: [astro-lightbox.netlify.app](https://astro-lightbox.netlify.app)  
- ⭐ **项目状态**: 41 stars, 1 fork

---

### [熊猫盒子：Astro 轻箱与画廊](https://astro-lightbox.netlify.app/)

**原文标题**: [PandaBox: An Astro Lightbox and Gallery](https://astro-lightbox.netlify.app/)

PandaBox 是一个基于 Astro v5 的光箱和图库工具，支持内容集合管理、图像优化及多种过渡效果，同时展示了一系列熊猫的有趣习性和特点。

- 🚀 适配 Astro v5，支持内容集合管理（包括 alt 文本、标题和描述）  
- 🖼️ 使用 Astro Image 组件优化图像，无额外依赖  
- 🎨 现代 CSS 设计，支持自定义过渡动画（淡入淡出或滑动）  
- 👆 触屏滑动切换幻灯片  
- 🐼 内含熊猫主题示例图库  
- 🌿 熊猫冷知识：每天吃 38 公斤竹子，12-16 小时进食  
- 🌳 擅长爬树，幼崽尤其活泼好动  
- 💧 需每日饮水，99% 饮食为竹子  
- 🛋️ 独居动物，性格温和慵懒  
- 📸 示例图库含 12 张熊猫照片及趣味解说（如进食坐姿、嗅觉灵敏等）

---

### [非 HTML 内容](https://frontendfoc.us/open/701/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/701/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

