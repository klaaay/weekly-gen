### [Tailwind CSS v4.3：滚动条、新颜色及更多功能 - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-3?ref=tailwindweekly.com)

**原文标题**: [Tailwind CSS v4.3: Scrollbars, new colors, and more - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-3?ref=tailwindweekly.com)

Tailwind CSS v4.3 和 v4.2 版本发布，带来了众多新功能和性能优化，包括新调色板、Webpack 插件、实用工具和 CSS 变体支持。

- 🎨 新增 **mauve、olive、mist、taupe** 四种中性色板，为设计提供更多温暖或冷调选择。
- ⚡ **@tailwindcss/webpack 插件** 让 Webpack 项目构建速度提升 2 倍以上，尤其适用于 Next.js 等框架。
- 📐 **逻辑属性工具** 新增 block-start/end 间距、inline/block 尺寸和逻辑 inset 定位，适配多书写模式。
- 🔤 **font-features-* 工具** 控制 OpenType 特性，如 tabular-nums，无需手写 CSS。
- 🔧 **滚动条工具** 支持 scrollbar-auto/thin/none 和颜色定制，避免布局偏移。
- 📦 **@container-size 工具** 创建尺寸容器，支持基于高度的容器查询。
- 🔍 **zoom-* 工具** 直接使用 CSS zoom 属性，支持任意值和变量。
- 📝 **tab-* 工具** 控制制表符渲染宽度，适合代码展示。
- 🔗 **@variant 支持堆叠和复合变体**，在 CSS 中更灵活地组合 hover/focus 等状态。
- 🎯 **功能工具默认值** 允许无值使用，如 `tab` 默认 4 空格，提升 API 一致性。

---

### [我们将您的设计转换为Tailwind CSS代码 | Design2Tailwind](https://design2tailwind.com/?ref=tailwindweekly.com#cta)

**原文标题**: [We convert your design to Tailwind CSS code | Design2Tailwind](https://design2tailwind.com/?ref=tailwindweekly.com#cta)

本页面介绍了一个由姐妹团队运营的 Tailwind CSS 设计转化服务，专注于将设计稿转换为可直接投入生产的代码。

- 👩‍💻 **姐妹团队**：Vivian 和 Daniela 拥有超过15年的前端经验，自2018年起专注 Tailwind CSS，提供干净、可预测且易扩展的代码。
- 🛠️ **服务范围**：支持 Figma、PSD、XD 和 Sketch 设计稿，并适配 React、Vue、Astro、Alpine.js 等主流框架。
- 🚀 **核心优势**：最小化自定义CSS、快速交付、无框架锁定、支持NDA、跨浏览器测试，且直接与编码者沟通。
- 📋 **清晰流程**：从需求分析、沟通对齐、编码开发到最终交付和反馈调整，共5个步骤。
- ⭐ **客户好评**：客户称赞其细致高效、代码质量高，能无缝集成到 Laravel 等项目，显著提升团队增长。
- 💰 **定价与FAQ**：首页 $350，附加页 $120；支持3轮修订；兼容最新版 Chrome、Safari、Firefox 和 Edge；可额外付费支持 React/Vue。

---

### [自学前端开发者的编程原则 - Piccalilli](https://piccalil.li/blog/programming-principles-for-self-taught-front-end-developers/?ref=tailwindweekly.com)

**原文标题**: [
  Programming principles for self taught front-end developers - Piccalilli
](https://piccalil.li/blog/programming-principles-for-self-taught-front-end-developers/?ref=tailwindweekly.com)

本篇文章为自学前端开发者总结了实用的编程原则，帮助写出更清晰、易维护的代码。

- 📚 **“三次法则”**：代码重复三次后才进行重构或优化，避免过早优化和过度设计。
- 🛠️ **“先让它工作，再让它正确，最后让它快”**：按优先级依次处理代码的正确性、合理性和性能，避免浪费精力。
- 🧩 **幂等性**：函数对相同输入始终返回相同输出，简化推理和调试。
- 🎯 **单一职责原则**：每个函数或模块只负责一个任务，便于修改和删除。
- 📊 **单一抽象层级**：函数内所有操作应处于相同细节水平，提升可读性。
- 🚫 **避免过早优化**：先构建简单可工作的系统，再逐步迭代复杂化。
- 🔁 **DRY（不重复自己）与YAGNI（你不会需要它）的平衡**：通过“三次法则”实际应用，避免过度抽象或冗余代码。

---

### [使用 safe-area-inset 构建移动安全布局 | Polypane](https://polypane.app/blog/using-safe-area-inset-to-build-mobile-safe-layouts/?ref=tailwindweekly.com)

**原文标题**: [Using safe-area-inset to build mobile-safe layouts | Polypane](https://polypane.app/blog/using-safe-area-inset-to-build-mobile-safe-layouts/?ref=tailwindweekly.com)

现代手机屏幕并非简单矩形，需使用安全区域内边距（safe-area-inset）确保内容不被系统UI遮挡，实现移动端安全布局。

- 📱 安全区域是屏幕中不被系统UI（如刘海、动态岛、手势条）遮挡的部分，通过CSS的`env(safe-area-inset-*)`变量获取各边距值。
- 🌐 `safe-area-inset-*`已广泛支持，可直接用于生产环境；可设置回退值（如`env(safe-area-inset-top, 1rem)`）增强兼容性。
- 🖥️ 默认浏览器会预留空间避免内容被遮挡，但需设置`viewport-fit=cover`启用全屏，并手动使用`env()`调整布局。
- ⚠️ 安全区域仅提供系统UI占用空间，不包含额外边距；需用`calc()`叠加自定义间距（如`calc(env(safe-area-inset-bottom) + 1rem)`）。
- 📱 桌面浏览器始终返回0，仅移动设备有非零值；Chrome响应式视图无法模拟，易导致开发阶段遗漏问题。
- 🔧 Polypane是首个支持模拟安全区域内边距的桌面浏览器，可实时查看不同设备的遮挡区域。
- 💡 浮动按钮等固定元素需用`env(safe-area-inset-bottom)`定位，避免被手势条遮挡；可结合`calc()`调整偏移量。
- 📊 `safe-area-max-inset-*`提供最大内边距值，适合需要稳定区域（如全屏对话框）的场景，但仅Chromium支持，需设置回退。
- ✅ 最佳实践：设置`viewport-fit=cover`+`env(safe-area-inset-*)`，确保所有内容可见可触，提供最佳用户体验。

---

### [SVG优化与无障碍基础 – David Bushell – 网页开发（英国）](https://dbushell.com/2025/06/25/svg-optimization-and-accessibility-basics/?ref=tailwindweekly.com)

**原文标题**: [SVG Optimization and Accessibility Basics â David Bushell â Web Dev (UK)](https://dbushell.com/2025/06/25/svg-optimization-and-accessibility-basics/?ref=tailwindweekly.com)

SVG 优化与无障碍基础一文概述了 SVG 的优化工具、最佳实践及无障碍访问技巧，强调手动优化和合理使用属性以提升性能与用户体验。

- 🚀 **SVGO v4 重大更新**：默认不再移除 `viewBox` 和 `title`，保留响应式缩放和无障碍描述，用户无需再手动配置。
- 🛠️ **手动优化优于自动化**：建议使用命令行工具（如 `npx svgo`）一次性优化 SVG，避免在每次构建中重复处理未修改文件。
- 📐 **内联 SVG 的关键属性**：必须保留 `viewBox`，并添加 `width` 和 `height` 以正确推断宽高比，避免渲染抖动。
- ♿ **无障碍标签选择**：使用 `<title>` 或 `aria-label` 提供文本描述；避免滥用 `aria-labelledby`，以防屏幕阅读器重复朗读。
- 🖼️ **装饰性 SVG 处理**：对纯图标使用 `aria-hidden="true"` 完全隐藏；若图标旁有可见文本标签（如“菜单”），则无需额外描述。
- ⚠️ **谨慎使用角色属性**：`role="img"` 可统一 SVG 为图像角色；`role="presentation"` 仅隐藏语义，但保留内部可聚焦元素（如 `<text>`）的可访问性。
- 🔍 **测试是关键**：无障碍方案需根据实际体验选择，并通过屏幕阅读器（如 VoiceOver）彻底测试，避免依赖单一建议。

---

### [获取失败](https://www.raspberrypi.com/?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://www.raspberrypi.com/?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 403。

---

### [Tailwind CSS 渐变边框插件](https://gradient-border.floriankiem.com/?ref=tailwindweekly.com)

**原文标题**: [Gradient Border Plugin for Tailwind CSS](https://gradient-border.floriankiem.com/?ref=tailwindweekly.com)

概述总结
- 🧠 人工智能技术正快速发展，深刻改变各行各业的生产方式与商业模式。
- 🌍 全球各国纷纷加大AI研发投入，争夺技术制高点，形成激烈竞争格局。
- ⚖️ 随着AI应用普及，数据隐私、算法偏见与伦理监管成为亟待解决的关键议题。
- 💼 自动化与智能系统可能导致部分岗位消失，但同时也催生新型职业与技能需求。
- 🔬 基础研究与跨学科合作是推动AI突破的核心动力，尤其在医疗、气候等领域的应用前景广阔。

---

### [WindyBase - 探索免费与高级的Tailwind CSS模板](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

WindyBase 是一个每周精选的 Tailwind CSS 模板和工具目录，旨在帮助开发者快速构建现代网站和应用。

- 🌟 提供精选的免费与付费 Tailwind CSS 模板、组件和工具，每周更新。
- 🖥️ 包含多种类别：着陆页、SaaS、博客、仪表盘、电商模板及组件库。
- 💰 模板价格从免费到 $249 不等，例如 Cosmic Themes 的模板多为 $77，也有免费选项如 Blogsmith Free。
- 🔍 支持搜索功能，方便用户查找所需资源。
- 📧 提供新闻订阅，用户可获取新模板和组件更新通知。
- 🛠️ 网站还包含提交项目、联系方式和法律条款等附加功能。

---

### [screenurl - 网站截图API | 捕获任意网址](https://screenurl.com/?ref=tailwindweekly.com)

**原文标题**: [screenurl - Website Screenshots API | Capture Any URL](https://screenurl.com/?ref=tailwindweekly.com)

ScreenURL是一个可将任意网址快速转为像素级截图的API服务，专为社交媒体预览、自动化测试、网站监控等场景设计，提供简单集成和透明定价。

- 📸 单次API调用即可在毫秒内生成任意网站的像素级完美截图
- ⚡ 平均响应时间低于2秒，基础设施针对速度优化
- 🔒 提供99.9%正常运行时间SLA，所有请求通过HTTPS加密
- 🖥️ 支持全页截图及自定义视口，最高支持4K分辨率
- 🎨 可选择PNG或JPEG格式，平衡质量与文件大小
- 🛠️ 提供cURL、JavaScript、Python等多语言代码示例，集成简单
- 💰 免费层每月100次截图，付费计划从$9/月起，含14天退款保证
- 🧪 支持实时演示功能，输入URL即可测试API效果
- 🏢 企业级方案提供无限截图、专属支持和自定义集成

---

### [crashcat - JavaScript 3D刚体物理](https://crashcat.dev/?ref=tailwindweekly.com)

**原文标题**: [crashcat - javascript 3d rigid body physics](https://crashcat.dev/?ref=tailwindweekly.com)

概述摘要
- 🐱 crashcat 是一个基于 JavaScript 的 3D 刚体物理引擎项目
- 📚 提供示例、文档和 GitHub 仓库，方便开发者学习和使用
- 🌐 支持通过 npm 安装，便于集成到项目中
- 🔧 可通过按 [d] 键显示调试视图，辅助物理模拟调试
- 🐦 项目维护者为 x.com/isaac_mason_，可关注获取更新
- 💰 提供赞助选项，支持项目持续开发

---

### [Cap：面向现代网络的自托管验证码](https://capjs.js.org/?ref=tailwindweekly.com)

**原文标题**: [Cap: Self-hosted CAPTCHA for the modern web.](https://capjs.js.org/?ref=tailwindweekly.com)

### 概述总结
这是一个自托管的、隐私优先的验证码解决方案，无需谷歌、无追踪、无视觉谜题，可作为reCAPTCHA的替代品，轻量且开源。

- 🔒 **隐私优先**：零遥测、无第三方网络，用户数据仅保留在您和用户之间
- ⚡ **极致轻量**：约20KB，零依赖，加载时间以毫秒计，比hCaptcha小250倍
- 🧩 **无视觉谜题**：后台静默运行工作量证明和浏览器检测，无需点击交通灯等操作
- 🆓 **完全开源**：Apache 2.0许可，可审计、可分支、可拥有，永久免费
- 🐳 **独立部署**：单个Docker容器即可部署，支持分析和多站点密钥
- 🤖 **无需用户交互**：可隐藏小部件，静默解决挑战，适合API和表单，支持无头浏览器检测
- ✅ **合规可定制**：符合GDPR和WCAG 2.2标准，所有样式通过CSS变量控制，无iframe锁定
- 🛡️ **双层架构**：同时运行工作量证明和浏览器检测，攻破一层仍受另一层保护
- 📊 **对比优势**：与reCAPTCHA、Turnstile、hCaptcha相比，自托管、开源、无追踪、更轻量
- 🚀 **快速迁移**：兼容reCAPTCHA/hCaptcha的API，15分钟内即可完成切换
- 💰 **成本极低**：自托管只需$5 VPS，无按请求收费、无第三方出口、无API配额

---
