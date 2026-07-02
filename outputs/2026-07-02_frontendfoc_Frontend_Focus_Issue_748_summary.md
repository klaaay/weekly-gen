### [金发姑娘式的自定义选择高度 - JakeArchibald.com](https://jakearchibald.com/2026/goldilocks-select-height/)

**原文标题**: [The Goldilocks customizable select height - JakeArchibald.com](https://jakearchibald.com/2026/goldilocks-select-height/)

### 概述摘要
本文介绍了如何通过 CSS 自定义`<select>`元素下拉选择器的高度，实现“恰到好处”的尺寸控制，避免过大或过小，并确保在不同浏览器中表现一致。

- 📏 **默认尺寸问题**：默认下拉选择器会填满视口高度，难以判断是否溢出，且缺乏视觉边界。
- 🛠️ **解决方案概述**：通过添加视口边距、设置最小和最大高度，并使用`calc-size()`和`position-try-fallbacks`等 CSS 特性优化体验。
- 🔧 **Firefox 兼容性**：使用`max-block-size: calc(100% - 1em)`作为`stretch`的降级方案，避免边距溢出。
- 🌐 **Chrome/Safari修复**：利用`flip-*`值自动翻转边距方向，确保下拉框翻转时边距正确。
- 📉 **防止过小**：使用`calc-size(fit-content, min(size, 12em))`设置最小高度，避免选项少时下拉框过小。
- 📈 **防止过大**：通过`calc-size(stretch, min(size, 30em))`限制最大高度，避免下拉框过高。
- 🧩 **完整 CSS 代码**：提供可直接复制的样式，包含所有降级方案和兼容性处理。
- ⏳ **未来简化**：待浏览器全面支持后，仅需三行 CSS 即可实现相同效果。

---

### [介绍 <usermedia> HTML 元素 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/usermedia-html-element)

**原文标题**: [Introducing the <usermedia> HTML element  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/usermedia-html-element)

Chrome 151 推出了 <usermedia> HTML 元素，作为 Capability Elements 套件的一部分，旨在简化摄像头和麦克风权限的获取流程，提升用户体验和安全性。

- 🎯 **核心功能**：<usermedia> 元素通过用户点击触发，直接管理摄像头和麦克风权限请求，并返回 MediaStream 对象，替代了传统的 getUserMedia() JavaScript API。
- 📈 **显著成效**：实际数据表明，该元素大幅提升了权限恢复成功率（Cisco 从 10% 升至 65%），并显著减少了媒体捕获错误（Zoom 降低 46.9%）和用户反馈问题（Google Meet 减少 17%）。
- 🔧 **简化实现**：开发者只需在 HTML 中添加 `<usermedia>` 标签，并通过 `setConstraints()` 方法配置硬件偏好，即可通过 `stream` 事件获取媒体流，大幅减少样板代码。
- 🔒 **安全与信任**：元素仅在用户物理点击后触发权限提示，提供了明确的用户意图信号，并支持一键恢复被拒绝的权限，解决了长期存在的“权限黑洞”问题。
- 🎨 **严格样式限制**：为确保可读性和防止欺骗，元素强制要求高对比度、不透明度为 1、最小尺寸等样式约束，并支持 `:granted` 等 CSS 伪类状态。
- 🛠️ **渐进增强与迁移**：不支持的浏览器会回退为普通 HTML 元素，开发者可通过检测 `HTMLUserMediaElement` 来提供基于 getUserMedia() 的降级方案，Origin Trial 参与者只需替换标签和更新检测逻辑。
- 🗺️ **未来规划**：后续将推出专注于视频的 `<camera>` 和专注于音频的 `<microphone>` 元素，进一步细化功能控制。

---

### [Webflow 开发者平台](https://developers.webflow.com/?utm_source=cooperpress-newsletter&utm_medium=email&utm_campaign=fy27-cooperpress-newslettter&utm_content=frontend-focus)

**原文标题**: [Webflow Developer Platform](https://developers.webflow.com/?utm_source=cooperpress-newsletter&utm_medium=email&utm_campaign=fy27-cooperpress-newslettter&utm_content=frontend-focus)

Webflow 开发者平台提供全面的工具和基础设施，帮助开发者构建、扩展和部署网站及应用。

- 🚀 **核心功能**：提供 CLI 工具（`npm install -g @webflow/webflow-cli`）、REST API、SDK、Webflow Cloud 部署、代码组件、DevLink 和 MCP 代理支持，实现全栈开发。
- 💰 **显著效益**：被超过 30 万组织信赖，实现 10 倍成本节省、67% 开发工单减少、56% 表单填写增加、1170% 流量增长等关键成果。
- 🛠️ **开发者工具**：包括 API 和 SDK、Webflow Cloud、代码组件、应用市场、CLI 和 DevLink，支持从命令行到可视化画布的各种开发需求。
- 📚 **文档与入门**：提供全面的指南、参考和示例，涵盖认证（OAuth 2.0）、CMS API、站点管理、自定义代码和 Webhooks。
- 🔗 **应用与集成**：支持市场应用（如 HubSpot、Zapier、PayPal）和原生集成（如 OpenStreet Map、Anthropic Claude、Google Docs），并可通过 API 和 SDK 构建自定义集成。
- 📰 **开发者博客**：发布技术文章，如 Webflow Cloud 独立域名运行、Algolia 搜索增强、AI 生成代码治理等。
- 👥 **社区与支持**：提供 GitHub 开源项目、Beta 测试、Webflow 社区、Reddit、Discord 等渠道，以及 Webflow University、YouTube 和 Webflow Way 等按需资源。
- 🎮 **趣味互动**：页面还包含一个 Webflow 主题的桌上足球小游戏（Webflow Foosball），作为开发体验的趣味点缀。

---

### [CSS 状态与 JavaScript 事件之间的界限变化 | CSS 技巧](https://css-tricks.com/css-states-and-javascript-events/)

**原文标题**: [The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks](https://css-tricks.com/css-states-and-javascript-events/)

## 概述总结
CSS 正通过伪类模拟 JavaScript 事件监听，实现状态驱动的样式控制，同时未来可能引入 `event-trigger` 属性直接触发动画。

- 🖱️ `:hover` 和 `:active` 分别对应指针进入/离开和按下/释放事件
- 🎯 `:focus` 与 `focus/blur` 事件对应，`:focus-visible` 需结合键盘操作启发式判断
- 🔗 `:focus-within` 和 `:has()` 实现父元素根据子元素状态变化样式
- ✅ `:checked` 对应 `change` 事件，用于复选框/单选按钮状态检测
- 📝 `:valid/:invalid` 立即生效，`:user-valid/:user-invalid` 等待用户交互后触发
- 🎬 媒体元素伪类（`:buffering`、`:paused`、`:playing` 等）对应 JavaScript 媒体事件
- 🗂️ `:popover-open`、`:open`、`:modal` 直接对应弹窗/对话框/详情元素状态
- 🖥️ `:fullscreen` 对应 `fullscreenchange` 事件，`:target` 对应 URL 哈希变化
- ⚡ `event-trigger` 允许用 CSS 声明事件监听，通过 `animation-trigger` 触发动画（支持有状态/无状态模式）

---

### [现代 UI 模式 - Una Kravets - CSS Day 2026 - YouTube](https://www.youtube.com/watch?v=8FSLsVAJj2w)

**原文标题**: [Modern UI Patterns - Una Kravets - CSS Day 2026 - YouTube](https://www.youtube.com/watch?v=8FSLsVAJj2w)

本頁面概述了 YouTube 平台相關的資訊，包括法律、政策、合作與技術等面向。

- 📰 **新聞中心**：提供 YouTube 官方新聞與公告。
- ©️ **版權**：說明內容版權相關規範與保護機制。
- 📞 **聯絡我們**：提供用戶與創作者聯繫 YouTube 團隊的管道。
- 🎬 **創作者**：專為內容創作者提供的資源與支援。
- 📢 **刊登廣告**：介紹在 YouTube 上投放廣告的選項與流程。
- 👨‍💻 **開發人員**：提供 API 與技術工具給開發者使用。
- 📜 **條款**：列出使用 YouTube 服務的相關條款與條件。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋社群規範、安全指南與內容審核政策。
- ⚙️ **YouTube 的運作方式**：解釋平台推薦、搜尋與內容管理機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能與實驗。
- 🏢 **© 2026 Google LLC**：標示版權歸屬與法律聲明。

---

### [Chrome 150 新特性 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/new-in-chrome-150)

**原文标题**: [New in Chrome 150  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-150)

Chrome 150 已发布，带来多项新功能，包括 CSS 属性改进和组件导航增强。

- 🎨 **CSS text-fit 属性**：自动缩放字体大小以适应容器宽度，无需手动计算或 JavaScript，实现响应式排版。
- ⌨️ **Focusgroup 属性**：为 Web 组件提供声明式方向键导航，支持焦点记忆和 Tab 键停止，替代复杂脚本。
- 🖼️ **CSS background-clip: border-area**：原生创建渐变边框，裁剪背景至边框区域，避免使用 border-image 的变通方案。

---

### [构建时间 - 用 CDN 流量点亮一面墙](https://eduardoboucas.com/posts/2026-06-29-wall-map/)

**原文标题**: [Build Times - Lighting up a wall with CDN traffic](https://eduardoboucas.com/posts/2026-06-29-wall-map/)

### 概述总结
本文讲述作者如何利用 CDN 流量数据，结合木质世界地图和可编程 LED 灯，打造一个实时显示全球网络活动的物理数字交互装置。

- 🌍 **项目灵感**：作者受物理与数字世界融合的启发，结合对地图的热爱和 CDN 工作背景，决定制作实时显示 CDN 流量的地图装置。
- 🪵 **木质地图选择**：选用激光切割的木质世界地图，每个大陆和岛屿为独立部件，便于钻孔和安装 LED 灯。
- 💡 **LED 布局挑战**：针对小国无法放置 LED、大国过于空旷的问题，采用分组标记（小国合并）和区域标记（大国分州/省）的折中方案。
- 🔧 **“佛罗里达事件”**：钻孔时因操作不慎导致佛罗里达半岛断裂，后用废弃木料重新切割、打磨并粘合修复。
- ⚡ **电子元件配置**：使用 247 个 WS2811 RGB 可寻址 LED 灯，通过树莓派控制，并采用 5 个独立电源模块避免电压衰减。
- 🖼️ **隐藏布线安装**：将电线穿过墙体隐藏，并用 3D 打印支架将地图固定在墙面上，留出空间放置 LED 灯和线缆。
- 📍 **校准工具**：开发命令行工具逐个点亮 LED 灯，手动输入对应城市/地区名称，建立 LED 编号与地理位置的映射关系。
- 📄 **数据格式设计**：定义通用 JSON 格式，允许任意数据源（如天气 API、CDN 流量）通过指定国家/地区代码、颜色、亮度和闪烁频率来驱动地图显示。
- 🌡️ **实时数据展示**：先通过天气 API 实现全球温度热力图（蓝冷红热），再接入 Netlify CDN 流量数据，用 LED 闪烁速度反映区域请求量。
- 🚀 **未来计划**：计划添加电子墨水屏控制器、物理按钮切换数据源，并开发 Web 界面供用户提交自定义数据源。

---

### [字体真棒](https://fontawesome.com/changelog)

**原文标题**: [Font Awesome](https://fontawesome.com/changelog)

概述总结  
- 📚 本文探讨了人工智能在医疗诊断中的应用，强调其提高准确性和效率的潜力。  
- 🩺 通过分析大量医学影像数据，AI 能辅助医生检测疾病，如癌症和视网膜病变。  
- ⚠️ 但存在数据隐私、算法偏见和监管挑战，需谨慎推进技术落地。  
- 🤝 人机协作是关键：AI 作为工具，最终决策仍需医生专业判断。  
- 🌍 全球范围内，AI 医疗正逐步推广，但需平衡创新与伦理风险。

---

### [字体真棒](https://fontawesome.com/icons/packs/pixel)

**原文标题**: [Font Awesome](https://fontawesome.com/icons/packs/pixel)

全球变暖导致极端天气频发，科学家呼吁加快减排行动，以降低气候风险并保护生态系统。

🌍 全球变暖加剧极端天气事件，如热浪、洪水和干旱的频率与强度  
📉 科学家强调，若不迅速减排，气候风险将显著上升，威胁人类生存环境  
🌱 保护生态系统成为当务之急，减少碳排放有助于缓解气候危机  
⚡ 呼吁各国加快能源转型，推广可再生能源，减少化石燃料依赖  
🔬 研究显示，及时行动可降低未来灾害损失，保障可持续发展

---

### [@zachleat.com 在 Bluesky 上](https://bsky.app/profile/zachleat.com/post/3mplrk6xttc2l)

**原文标题**: [@zachleat.com on Bluesky](https://bsky.app/profile/zachleat.com/post/3mplrk6xttc2l)

### 概述摘要  
纪念 Google Reader 关闭 13 周年，呼吁网站添加 RSS/Atom/JSON Feed，构建有意义、积极的网络连接。  

- 📅 纪念 Google Reader 于 2013 年 7 月 1 日关闭 13 周年  
- 🌐 呼吁网站添加 RSS/Atom/JSON Feed  
- 🤝 强调构建有意义、积极的网络连接  
- 💡 鼓励延续开放网络精神，替代集中式服务

---

### [获取失败](https://www.w3.org/news/2026/pointer-events-level-3-is-now-a-w3c-recommendation/)

**原文标题**: [Failed to retrieve](https://www.w3.org/news/2026/pointer-events-level-3-is-now-a-w3c-recommendation/)

无法总结：获取内容失败，状态码 403。

---

### [CSS 中文本上的动画径向渐变遮罩](https://cassidoo.co/post/radial-mask-text-css/)

**原文标题**: [An animated radial gradient mask over text in CSS](https://cassidoo.co/post/radial-mask-text-css/)

### 概述总结
本文详细介绍了如何使用 CSS 的`mask`属性和`repeating-radial-gradient`实现文字上的动态径向渐变遮罩效果，并分享了作者在字体选择、浏览器兼容性等方面的经验。

- 🎨 **核心效果**：通过 CSS 遮罩在文字上创建环形渐变条纹，形成独特的视觉动画效果
- 🔤 **字体选择关键**：需要选择具有完美圆形字母"o"的字体（如 Fredoka），确保条纹显示效果
- 🛠️ **技术实现**：使用`mask: repeating-radial-gradient()`设置圆形渐变遮罩，通过`--stripes`变量控制条纹宽度
- ⚙️ **动画技巧**：利用`@property`注册自定义属性实现渐变动画，解决传统 CSS 渐变难以动画化的问题
- 🌐 **浏览器兼容**：Firefox 和 Safari 存在渲染差异，需避免使用`rem`单位，调整像素值确保跨浏览器显示
- 🔧 **调试经验**：手动调整渐变中心点坐标（198.2px 69.6px）以对齐字母"o"，字体或字号变化需重新校准
- 💡 **扩展玩法**：修改`--stripes`值（如 3px 或 10px）或`calc()`中的乘数（2→4）可改变条纹粗细和间距

---

### [获取失败](https://codepen.io/cassidoo/pen/QwdMQVm)

**原文标题**: [Failed to retrieve](https://codepen.io/cassidoo/pen/QwdMQVm)

无法总结：获取内容失败，状态码 403。

---

### [使用 Web 标准的暗黑模式](https://olliewilliams.xyz/blog/dark-mode/)

**原文标题**: [Dark mode with web standards](https://olliewilliams.xyz/blog/dark-mode/)

### 概述总结
本文介绍了使用 Web 标准实现暗色模式的最佳实践，重点讲解如何通过`color-scheme`属性和`prefers-color-scheme`媒体查询，在尊重用户系统设置的同时提供网站内切换功能。

- 🌓 **核心原则**：默认尊重用户系统设置（通过`<meta name="color-scheme" content="light dark">`），同时提供网站内切换按钮让用户自定义。
- 🔄 **切换实现**：使用 JavaScript 更新`<meta>`标签的`content`属性（light/dark/light dark），并将用户选择保存到`localStorage`中持久化。
- 🎨 **影响范围**：`color-scheme`控制 CSS `light-dark()`函数、系统颜色（如 Canvas）、滚动条颜色、HTML 默认元素颜色、iframe 样式（需子文档同意）及支持`light-dark()`的 SVG。
- ⚠️ **关键局限**：`color-scheme`不会影响`prefers-color-scheme`媒体查询，因此无法直接通过媒体查询响应网站内切换（iframe 和 SVG 是例外，但存在浏览器兼容性问题）。
- 🖼️ **图片与渐变**：`light-dark()`函数现已支持渐变和图片，可基于颜色方案切换背景图片或渐变效果。
- 🛠️ **高级技巧**：通过 CSS 自定义属性 + 样式查询（`@container style()`）实现非颜色属性（如阴影/边框）的暗色模式切换，解决`box-shadow`在暗色背景不可见的问题。
- 🔮 **未来展望**：可能通过 JavaScript 覆盖`prefers-color-scheme`（Chrome 已有原型），但 Safari 团队反对该方案。

---

### [Ghost —— 智能体数据库](https://ghost.build/?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Ghost â the database for agents](https://ghost.build/?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

### 概述总结
Ghost 是一款专为 AI 代理设计的托管 Postgres 数据库服务，支持按任务快速创建、分支和销毁独立数据库，确保生产环境安全无风险。

- 🚀 **为代理而生**：每个代理任务分配独立数据库，避免冲突，生产环境不受影响。
- ⚡ **秒级创建与分支**：0.4 秒内创建新数据库，支持即时分支（copy-on-write），方便安全实验。
- 🔒 **安全隔离**：只读模式、硬性消费上限，防止代理误操作破坏生产数据。
- 💰 **灵活定价**：按需模式（免费 100 小时/月）和专用模式（$10/月起），仅按查询时间计费。
- 🛠️ **原生代理集成**：支持 MCP、CLI、psql 等工具，方便 Claude、Cursor 等代理直接使用。
- 📊 **真实数据实验**：分支功能可复制任意大小数据库，确保实验结果有效。
- 🧹 **自动清理**：支持定时删除数据库，避免代理遗留资源浪费。
- 🌟 **用户验证**：已获 AI 平台、金融科技公司等用户好评，消除代理冲突、迁移回滚等问题。

---

### [使用视图过渡提升网页用户体验 – Bramus Van Damme | beyond tellerrand 杜塞尔多夫 2026 - YouTube](https://www.youtube.com/watch?v=TUcWdCrITdw)

**原文标题**: [Supercharge Web UX with View Transitions – Bramus Van Damme | beyond tellerrand Düsseldorf 2026 - YouTube](https://www.youtube.com/watch?v=TUcWdCrITdw)

本頁面概述了 YouTube 平台相關的法律、政策、聯絡與營運資訊。

- 📰 **新聞中心**：提供 YouTube 官方新聞與公告。
- ©️ **版權**：說明內容版權相關規定與保護機制。
- 📞 **聯絡我們**：提供用戶與創作者的聯繫管道。
- 🎬 **創作者**：針對內容創作者提供的資源與支援。
- 📢 **刊登廣告**：介紹廣告投放與合作機會。
- 👨‍💻 **開發人員**：提供 API 與開發工具資訊。
- 📜 **條款**：列出使用 YouTube 的服務條款。
- 🔒 **私隱**：說明用戶資料的收集與使用政策。
- 🛡️ **政策及安全**：涵蓋社群規範與安全措施。
- ⚙️ **YouTube 的運作方式**：解釋平台推薦與內容管理機制。
- 🧪 **測試新功能**：介紹正在測試中的新功能。
- 📅 **© 2026 Google LLC**：版權歸屬與法律聲明。

---

### [无需 GPU 的 WebGL — Microlink 博客](https://microlink.io/blog/webgl-without-a-gpu)

**原文标题**: [WebGL without a GPU — Microlink Blog](https://microlink.io/blog/webgl-without-a-gpu)

无 GPU 环境下，通过 Chrome 标志将 WebGL 渲染速度提升 4 倍

- 🚀 **核心优化**：将 Chrome 的 ANGLE 后端从 SwiftShader 切换为 Mesa llvmpipe，使 3D 页面渲染时间从~24 秒降至~6 秒
- 💻 **无 GPU 设计**：服务器使用无显卡的 Linux 节点，通过 CPU 模拟 WebGL 渲染，降低成本与维护复杂度
- ⚙️ **关键配置**：仅需修改一行 Chrome 标志 `--use-angle=gl`，但需配合虚拟显示（Xvfb）和 `LIBGL_ALWAYS_SOFTWARE=1` 环境变量
- 🏗️ **Mesa 编译**：从源码编译 Mesa llvmpipe，启用共享 LLVM 实现 JIT 编译，通过多阶段 Docker 构建将镜像从 4.5GB 压缩至 2.65GB
- 📊 **验证机制**：通过 `browserless.report()` 实时检测 GPU 类型，CI 断言强制要求 `gpu.type` 为 `software` 且 `gpu.device` 为 `llvmpipe`
- ⏱️ **性能对比**：SwiftShader 渲染耗时 24-31 秒，llvmpipe 仅需 6 秒（空闲）或 7-14 秒（负载），彻底消除超时请求
- 🧪 **测试陷阱**：开发机 GPU 会掩盖问题，单次运行结果不可靠，需使用确定性着色器基准测试确保数据稳定
- ⚠️ **已知限制**：复杂片段着色器页面可能因首帧绘制竞争导致黑屏，需通过捕获时机优化解决

---

### [持久模式与主题——构建持久化切换方案 | 始终扭曲](https://www.alwaystwisted.com/articles/modes-and-themes-that-stick-building-a-persistent-toggle-solution)

**原文标题**: [Modes and Themes That Stick - Building a Persistent Toggle Solution | Always Twisted](https://www.alwaystwisted.com/articles/modes-and-themes-that-stick-building-a-persistent-toggle-solution)

文章介绍了一种分离“模式”（亮/暗）与“主题”（强调色）的持久化切换方案，采用渐进增强的三层架构，确保用户体验流畅且可访问。

- 🎨 **分离模式与主题**：使用独立的 `data-mode` 和 `data-theme` 属性，避免将两者混为一个属性，保持 CSS 清晰和逻辑独立。
- 📻 **原生单选按钮**：采用 `<input type="radio">` 搭配 `<fieldset>` 和 `<legend>`，确保语义正确、键盘可操作，并自动处理互斥选择。
- 🧩 **三层渐进增强**：Layer 1（HTML+CSS 基础）、Layer 2（阻塞脚本防止颜色闪烁）、Layer 3（交互与持久化），每层独立工作，故障时仍可降级。
- 🚫 **避免闪烁**：在 `<head>` 中嵌入阻塞脚本，在首次渲染前从 `localStorage` 读取并应用保存的模式/主题，消除颜色闪烁。
- 💾 **使用 localStorage**：相比 Cookie（浪费带宽）和 IndexedDB（过于复杂），localStorage 简单、同步、仅客户端，适合存储少量偏好。
- 🎯 **存储意图而非结果**：保存“system”字符串而非解析后的亮/暗值，以便在 OS 模式变化时实时跟随，同时允许用户显式覆盖。
- 🧪 **处理系统模式**：通过 `matchMedia` 监听 OS 主题变化，仅在用户选择“system”时自动更新，确保意图与显示一致。
- 🎛️ **CSS 样式技巧**：隐藏原生单选按钮，样式化 `<span>` 模拟按钮，使用 `:checked` 和 `:focus-visible` 确保视觉反馈和可访问性。
- ♿ **无障碍要点**：原生控件提供键盘导航和语义，避免额外 `aria-label`，确保颜色对比度满足 WCAG 标准。
- ⚠️ **常见陷阱**：`localStorage` 在隐私模式下可能抛出异常，需用 `try/catch` 保护；阻塞脚本必须内联；避免混合 `data-mode` 和媒体查询策略。
- 🤔 **反思与取舍**：作者最终移除了自己网站的主题切换，因为维护成本超过实际使用价值，有时仅尊重系统偏好就足够了。
- 🌟 **核心哲学**：持久化不是炫技，而是尊重用户已做的选择并优雅降级，让“记住偏好”成为自然体验而非额外功能。

---

### [流式传输 HTML](https://olliewilliams.xyz/blog/streaming-html/)

**原文标题**: [Streaming HTML](https://olliewilliams.xyz/blog/streaming-html/)

### 概述总结
本文介绍了通过 `fetch()` 获取 HTML 流、将其流式传输到 DOM 的新方法，以及相关的安全与非安全操作、声明式部分更新和浏览器支持情况。

- 📡 **获取 HTML 流**：使用 `fetch()` 时，通过 `response.body.pipeThrough(new TextDecoderStream())` 或新的 `textStream()` 方法，可将字节流解码为文本流。
- 🖥️ **流式插入 DOM**：Chrome Canary 新增了 `streamHTML`、`streamAppendHTML` 等流式方法，可将 HTML 流直接插入元素，并支持安全（自动清理）与不安全（无默认清理）版本。
- 🔒 **安全 vs 不安全**：安全方法（如 `streamHTML`）自动清理 HTML；不安全方法（如 `streamHTMLUnsafe`）不清理，但可配置清理器，并支持声明式 Shadow DOM 和 `runScripts` 选项。
- 🏗️ **声明式部分更新**：通过 `<template>` 元素和 `<?marker name="...">` 处理指令，可将流式 HTML 定向更新到页面特定位置，实现部分页面刷新。
- ⚙️ **新旧方法对比**：新非流式方法（如 `setHTMLUnsafe`）替代了旧方法（如 `innerHTML`），并增加了对声明式 Shadow DOM 和脚本执行的控制。
- 🌐 **浏览器支持**：`textStream()` 和流式 DOM 方法目前仅在 Chrome Canary 中可用。

---

### [使用滚动驱动动画实现相反滚动方向 | CSS 技巧](https://css-tricks.com/scroll-driven-animations-opposing-scroll-directions/)

**原文标题**: [Using Scroll-Driven Animations for Opposing Scroll Directions | CSS-Tricks](https://css-tricks.com/scroll-driven-animations-opposing-scroll-directions/)

概述总结
- 📜 本文介绍了如何使用 CSS 滚动驱动动画实现多列内容在滚动时以相反方向移动的效果
- 🎨 通过`animation-timeline: view()`和`@keyframes`定义列内元素的滚动动画，实现向上或向下平移
- 🧩 HTML 结构为父容器包含多个列，每列内有多个项目，CSS 负责布局和动画
- 🖥️ 仅在宽屏（>=50rem）生效，利用`@media`查询限制效果
- 🎭 使用伪元素和渐变遮罩实现元素在容器边界淡出的视觉效果
- ⚙️ 定义三个关键帧动画（`scroll1`、`scroll2`、`scroll3`），分别控制不同列的移动方向和偏移
- ♿ 通过`prefers-reduced-motion`媒体查询尊重用户减少动效的偏好
- 🔄 使用`@supports`检测浏览器支持，提供降级方案（如普通时间线动画）
- ✅ 当前支持 Chrome 和 Safari，Firefox 尚未支持，但可通过渐进增强实现兼容

---

### [网络正变得对 AI 更友好，而非对人 | TechPolicy.Press](https://www.techpolicy.press/the-web-is-being-made-accessible-for-ai-not-people/)

**原文标题**: [The Web Is Being Made Accessible for AI, Not People | TechPolicy.Press](https://www.techpolicy.press/the-web-is-being-made-accessible-for-ai-not-people/)

### 概述总结
文章指出，当前网络正在为 AI 系统而非人类进行无障碍改造，这种趋势可能忽视残障人士的真实需求，并存在“无障碍洗白”的风险。

- 🤖 **AI 优先的网络改造**：Svelte 等框架为 AI 提供纯文本格式文档，但这类改造主要服务于 AI 系统，而非残障用户。
- 🚫 **无障碍标准被忽视**：尽管 WCAG 要求语义化 HTML，但 95% 的网站存在无障碍缺陷，而 AI 优化内容（如 llms.txt）反而破坏了屏幕阅读器所需的结构。
- ⚖️ **“斜坡自动化效应”**：残障人士争取的基础设施（如路缘坡道）被机器人占用，类似现象在数字领域重演——AI 需求驱动变革，但残障群体利益被边缘化。
- 🚧 **基础设施的双刃剑**：自动驾驶汽车推动道路标线改善，但送货机器人却与轮椅使用者争夺空间，甚至制造新障碍。
- 🎭 **“无障碍洗白”风险**：AI 公司宣称其技术能解决无障碍问题，但实际可能引入新障碍，并削弱政治力量推动真正无障碍立法的意愿。
- 🛠️ **需要残障人士主导设计**：政策制定者应确保 AI 驱动的变革由残障专家共同设计，而非仅服务于商业利益。
- 📉 **商业需求优先于公民权利**：当科技公司需要相同设施时，行动立即出现，而残障人士数十年的呼吁却被忽视，这暴露了资源分配的不平等。

---

### [SlimSelect - 高级 JavaScript 选择下拉库 | 原生 JS 多选](https://slimselectjs.com/)

**原文标题**: [SlimSelect - Advanced JavaScript Select Dropdown Library | Vanilla JS Multi-select](https://slimselectjs.com/)

概述总结
- 🚫 此网站需要启用 JavaScript 才能正常运行
- ⚙️ 请确保浏览器已开启 JavaScript 功能
- 🔄 若未启用，网站可能无法正常显示或交互

---

### [发布 v4.0.0 · brianvoe/slim-select · GitHub](https://github.com/brianvoe/slim-select/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · brianvoe/slim-select · GitHub](https://github.com/brianvoe/slim-select/releases/tag/v4.0.0)

Slim Select 4.0.0 发布，对下拉选择组件进行了重大重构，新增模态模式、提升性能并优化样式。

- 📱 **新增模态模式**：新增 `settings.modal` 选项（`'off'`、`'on'`、`'mobile'`），在移动端或指定情况下，选项面板以居中模态框形式打开，支持背景遮罩、关闭按钮和键盘关闭。
- ⚡ **性能与搜索优化**：本地搜索直接过滤现有 DOM 节点，避免每次按键重建列表；API 搜索结果临时存储，清除搜索后恢复原始目录；使用 `content-visibility: auto` 和 `ResizeObserver` 提升长列表和定位性能。
- 🎨 **样式改进**：新增 `--ss-search-height` 和 `--ss-option-height` CSS 变量，默认继承 `--ss-main-height`；滚动条颜色跟随主色和背景色；支持 `prefers-reduced-motion` 减少动画。
- ✅ **质量提升**：包含 477 个 Vitest 单元测试和 46 个 Playwright E2E 测试，扩展了可访问性、键盘、API 搜索等功能覆盖。
- 🔧 **重大变更**：Vue/React 包装器不再支持原生 `<option>`，需通过 `data` 属性传递选项；`events.search` 回调签名变更，新增 `catalog` 参数；`selectAllText` 属性移除，默认使用“Select All”/“Unselect All”；模态模式在移动端默认启用；`option.data` 现在返回普通对象而非 `DOMStringMap`；可关闭选项组改为手风琴行为。
- 📚 **迁移指南**：提供了从 3.x 迁移到 4.0 的详细说明，包括 Vue/React 数据传递、搜索回调、CSS 变量、模态默认值等变更。

---

### [vale.rocks/FixCSS 主分支 · Tangled](https://tangled.org/vale.rocks/FixCSS)

**原文标题**: [vale.rocks/FixCSS at main · Tangled](https://tangled.org/vale.rocks/FixCSS)

FixCSS 是一个用于修正 CSS 设计错误的库，能自动将纠正后的属性名、值、选择器和语法转换为浏览器兼容的 CSS。

- 📚 核心用途：修复 CSS 设计中的已知错误，按“应有”方式编写 CSS
- 🛠️ 客户端使用：直接引入 `fixcss.js` 脚本，自动转换 `<style>` 块、内联样式和 DOM 变化
- ⚙️ 构建时使用：支持 CLI 命令和编程方式（npm 包 `@declanchidlow/fixcss`）
- 🔧 核心函数：`fixCSS()` 转换 CSS 字符串，可选修复简写默认值、轴顺序、选择器组合符
- 🎛️ 可选功能：`convertCCW()` 将逆时针四值简写转为顺时针，`convertProperties()` 仅转换属性名
- 🌐 浏览器运行时：`start()` 自动监听 DOM，`shutdown()` 停止，`convertPage()` 手动转换
- 💻 CLI 选项：支持输入/输出文件、标准输入、监听模式、禁用特定修复（如 `--no-axis`）
- 📦 依赖与关联：基于 BritCSS 项目，100% JavaScript，开源在 tangled.org

---

### [CSS 设计错误不完全列表 - CSS 工作组维基](https://wiki.csswg.org/ideas/mistakes/)

**原文标题**: [Incomplete List of Mistakes in the Design of CSS - CSS Working Group Wiki](https://wiki.csswg.org/ideas/mistakes/)

以下是 CSS 设计中常见错误的不完整列表，若有人发明时光机应予以修正：

- 📝 `white-space: nowrap` 应改为 `no-wrap`，且换行行为不应归入此属性
- 🔄 `animation-iteration-count` 应简化为 `animation-count`（类似 `column-count`）
- 📐 `vertical-align` 不应应用于表格单元格，CSS3 对齐属性应直接存在于 Level 1 中
- ⚖️ `vertical-align: middle` 应命名为 `text-middle` 或 `x-middle`，因其并非真正居中
- 📏 百分比高度应基于 `fill-available` 计算，而非在 auto 情况下未定义
- 📊 表格布局应更合理
- 📦 `box-sizing` 默认应为 `border-box`
- 🖼️ `background-size` 单值应复制该值，而非默认第二个为 `auto`；`translate()` 同理
- 📍 `background-position` 和 `border-spacing` 应先接受垂直值，以匹配 4 方向属性如 `margin`
- 🔁 `background-repeat` 默认值应为 `no-repeat`（虽 90 年代合理，但后续更实用）
- 🔄 4 值简写如 `margin` 应逆时针排列（使内联起始值位于块结束和内联结束值之前）
- 📊 `z-index` 应改名为 `z-order` 或 `depth`，并默认适用于所有元素
- 📝 `word-wrap`/`overflow-wrap` 应移除，改为 `white-space` 的关键字如 `nowrap`
- ⚠️ 单个盒子的上下外边距不应自动折叠，这是所有外边距折叠问题的根源
- 📉 应允许部分折叠而非用奇怪规则处理 min/max 高度
- 🖥️ 表格（如其他非块元素）应形成伪堆叠上下文
- 🎨 `currentColor` 应保留连字符为 `current-color`，其他多词颜色名同理
- 🌈 应采用可预测的颜色命名系统（如 CNS）而非任意 X11 名称
- 🔲 `border-radius` 应改为 `corner-radius`
- 📌 绝对定位替换元素在设置相反偏移属性时应拉伸，而非起始对齐
- ✂️ `hyphens` 属性应命名为 `hyphenate`
- 🎨 `rgba()` 和 `hsla()` 不应存在，`rgb()` 和 `hsl()` 应接受可选第四参数
- 🔗 后代选择器应为 `>>`，间接兄弟选择器应为 `++`，以保持 ASCII 艺术逻辑
- 🖌️ `*-blend-mode` 属性应简化为 `*-blend`
- 🔣 Unicode 范围语法应与 CSS 一致，如 `u0001-u00c8`
- 🔤 Unicode 范围不应有独立微语法和分词处理
- 📝 `font-family` 应要求字体名加引号，避免解析 `font` 时需依赖 `font-size`
- 📐 Flexbox 中 `flex-basis` 与 `width`/`height` 的关系应简化
- 🚫 `:empty` 应改为 `:void`，而 `:empty` 应选择仅含空白的元素
- 📊 `table-layout: fixed; width: auto` 应产生填充可用宽度的固定布局表格
- 📝 `text-orientation` 初始值应为 `upright`
- 🔗 `@import` 应更积极去重并允许共享样式表对象
- 🔍 选择器应分割顶级逗号，仅忽略未知/无效部分而非整个选择器
- 🔗 `:link` 应始终具有 `:any-link` 语义
- 📐 `flex` 简写应接受 `fr` 单位而非纯数字
- 📝 `display` 属性应改为 `display-type`
- 📋 `list-style` 属性应改为 `marker-style`，`list-item` 改为 `marked-block`
- 📝 `text-overflow` 应始终适用，不依赖 `overflow`
- 📏 `line-height: <percentage>` 应计算为等效的 `line-height: <number>`
- 📝 `::placeholder` 应改为 `::placeholder-text`，`:placeholder-shown` 改为 `:placeholder`
- 🖥️ `overflow: scroll` 应引入堆叠上下文
- 📐 `size` 应作为 `width` 和 `height` 的简写，而非 `@page` 属性
- 🔲 网格属性中应避免混合关键字（如 `span`）与标识符，可能使用函数表示法
- 💬 注释不应允许在 CSS 中几乎任何位置，以免对象模型难以表示
- 📐 Flexbox 对齐属性应相对于书写模式而非 flex-flow
- 🖼️ `shape-outside` 名称应包含 `wrap-`，避免与 `clip-path` 混淆
- ⚠️ `!important` 应改用其他写法，因其易被工程师误解为“不重要”

---

### [FixCSS - 2026 年 7 月 1 日 04:00 UTC | Vale.Rocks](https://vale.rocks/micros/20260701-0400)

**原文标题**: [FixCSS - 1 July 2026 04:00 UTC | Vale.Rocks](https://vale.rocks/micros/20260701-0400)

概述摘要  
- 🎨 CSS 最初设计简单，仅用于轻量文本页面，但随网络发展被迫快速演进。  
- ❌ 设计过程中存在明显错误和随时间暴露的缺陷，CSS 工作组已发布《CSS 设计错误不完全列表》。  
- 🔄 由于现有软件依赖，这些错误无法直接修复，否则会引发兼容性问题。  
- 🛠️ FixCSS 库应运而生，通过客户端、Node 包和 CLI 方式，模拟一个“未犯错误”的替代 CSS 时间线。  
- 📌 该项目主要作为概念验证或趣味工具，不适用于生产环境。  
- 📦 源代码托管于 Tangled，NPM 包名称为@declanchidlow/fixcss。

---

### [Sentry 201：让 Sentry 更实用 | Sentry](https://sentry.io/resources/201-series/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=brand-fy27q2-201workshop&utm_content=newsletter-sponsored-link-register)

**原文标题**: [Sentry 201: Making Sentry More Useful | Sentry](https://sentry.io/resources/201-series/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=brand-fy27q2-201workshop&utm_content=newsletter-sponsored-link-register)

Sentry 201 工作坊系列，教你善用 Sentry 订阅中的各项功能，涵盖集成、采样、调试及自动化工作流。

- 🎓 三部分工作坊系列，涵盖 Sentry 订阅中所有功能及实际应用方法
- 🔗 第一场（6 月 24 日）：集成与采样，避免意外
- 🐛 第二场（6 月 30 日）：使用 Traces、Logs 和 Metrics 进行调试
- 🤖 第三场（7 月 7 日）：使用 Sentry MCP、CLI 和 Seer 构建代理工作流
- 🎧 赞助的 Syntax 播客，可在各大平台收听

---

### [GitHub - educastellano/qr-code: 用于生成二维码的 Web 组件 · GitHub](https://github.com/educastellano/qr-code)

**原文标题**: [GitHub - educastellano/qr-code: Web Component for generating QR codes · GitHub](https://github.com/educastellano/qr-code)

这是一个名为 `<qr-code>` 的 Web Component 项目，用于在网页中生成二维码，基于 qr.js 库开发，支持多种格式和自定义样式。

- 📦 **安装与导入**：通过 npm 安装 `webcomponent-qr-code`，支持直接导入或自定义元素名称。
- 🎨 **自定义样式**：使用 `::part` 伪元素可分别对 PNG、HTML、SVG 格式的二维码进行样式定制。
- ⚙️ **核心选项**：支持设置数据内容、格式（png/html/svg）、模块大小、边距、CSS 单位、比例及纠错等级（L/M/Q/H）。
- 🛠️ **贡献指南**：鼓励 Fork 项目、创建功能分支、提交更改并提交 Pull Request。
- 📜 **版本历史**：从 v0.0.1 到 v2.0.0，逐步增加了 SVG 支持、自定义样式、ESM 发布等特性，并移除了旧版兼容。
- 📄 **许可信息**：采用 MIT 许可证，项目拥有 545 颗星、83 个 Fork，主要使用 JavaScript（93.7%）和 HTML（6.3%）。

---

### [二维码](https://educastellano.github.io/qr-code/demo/)

**原文标题**: [<qr-code>](https://educastellano.github.io/qr-code/demo/)

本内容介绍了二维码生成中的核心参数与格式选项，包括输出格式、模块尺寸、边距、纠错等级及自定义样式。
- 📐 支持 HTML、PNG、SVG 三种输出格式
- 🔲 模块尺寸可设置为“可缩放大小”（值为 0 时）
- 📏 可配置二维码边距（Margin）
- 🛡️ 提供四种纠错等级：低（L）、中（M）、四分位（Q）、高（H）
- 🎨 支持自定义样式（Custom styles）

---

### [GitHub - mcollina/snipgrapher · GitHub](https://github.com/mcollina/snipgrapher)

**原文标题**: [GitHub - mcollina/snipgrapher · GitHub](https://github.com/mcollina/snipgrapher)

snipgrapher 是一个 CLI 工具，用于从代码文件、标准输入或内联源码生成图片片段，支持多种输出格式和自定义样式。

- 🖼️ **核心功能**：通过 CLI 将代码渲染为 SVG、PNG 或 WebP 格式的图片，支持语法高亮（基于 Shiki）和多种主题。
- 📦 **安装与使用**：通过 `npm i -g snipgrapher` 全局安装，支持 `render`、`batch`、`watch`、`themes list`、`fonts`、`doctor` 和 `init` 等命令。
- ⚙️ **配置选项**：支持通过 JSON、YAML 或 TOML 配置文件（如 `snipgrapher.config.json`）自定义主题、字体、边距、行号、窗口控件、阴影、背景样式和水印。
- 🔧 **程序化使用**：可作为 Node.js 模块导入，通过 `renderToFile` 函数以编程方式生成代码图片。
- 🌐 **环境变量**：支持 `SNIPGRAPHER_*` 环境变量覆盖配置，优先级为 CLI 标志 > 环境变量 > 配置文件 > 默认值。
- 🎨 **样式定制**：提供多种主题（如 Carbon 主题集）、字体（如 Fira Code、JetBrains Mono）和背景样式（纯色或渐变）。
- 📂 **批量处理**：支持 `batch` 命令批量处理匹配文件，并生成清单文件。
- ✅ **质量保证**：包含 lint、格式检查、类型检查、测试和基准测试等质量检查流程。

---

### [四季](https://shiki.style/)

**原文标题**: [Shiki](https://shiki.style/)

概述总结  
- 🌈 基于 TextMate 语法引擎，与 VS Code 同源，确保高精度和高美观度。  
- 🚀 与 VS Code 同步优化，持续提升语法高亮和代码解析的准确性。  
- 🔧 支持丰富语言特性，提供流畅的编辑体验，减少错误提示。  
- 💡 自动适配 VS Code 更新，无需手动调整配置即可享受最新改进。

---

### [STRICH | 网页应用条码扫描](https://strich.io/?ref=frontend-focus)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=frontend-focus)

STRICH 是一個專為網頁應用程式設計的 JavaScript SDK，能在瀏覽器中實現即時、客戶端的一維/二維條碼掃描，無需後端支援。它提供簡單透明的定價、優秀的開發者體驗，並獲得眾多客戶好評，尤其擅長處理受損或環境惡劣的條碼。

- 🚀 **純客戶端掃描**：所有影像處理在瀏覽器中即時完成，無需後端伺服器。
- 💰 **簡單透明定價**：無需大額預付，提供 14 天免費試用，可隨時取消。
- 🧑‍💻 **開發者友善**：零依賴，支援所有主流框架，提供詳盡的文件與 TypeScript 類型綁定。
- 📱 **跨平台相容**：可在 Android 和 iOS 的所有主要瀏覽器上運作，包括高階與低階裝置。
- 🔍 **支援多種條碼**：涵蓋 Code 128、EAN、QR Code、Data Matrix、PDF417 等常見一維與二維條碼。
- 💪 **讀取困難條碼**：採用先進影像處理技術，能有效讀取褪色、破損、光線不均或反色的條碼。
- 🏢 **企業級功能**：提供白標籤、離線操作、GS1 標準支援及優先技術支援。
- 🗣️ **客戶高度評價**：多位用戶稱讚其整合簡單、掃描速度快、穩定性高，且支援服務優良。

---

### [寻找屏幕无法显示的颜色——Ryan Moulton 的文章](https://moultano.wordpress.com/2026/06/19/where-to-find-the-colors-your-screen-cant-show-you/)

**原文标题**: [Where to Find the Colors Your Screen Can’t Show You – Ryan Moulton's Articles](https://moultano.wordpress.com/2026/06/19/where-to-find-the-colors-your-screen-cant-show-you/)

本文探讨了屏幕无法显示的真实世界颜色，尤其是青色，并指导读者如何在自然界和人造环境中找到它们。

- 🌿 屏幕与真实颜色的差距：数字屏幕和 sRGB 色域无法显示许多真实世界的颜色，尤其是高饱和度的青色，因为屏幕通过混合红绿蓝三原色来模拟颜色，但无法覆盖整个可见光谱。
- 🔬 颜色感知的科学原理：人眼只有三种视锥细胞，通过对比它们的响应强度来感知颜色；任何使这三种细胞发出相同信号的混合光，看起来都是同一种颜色。
- 🎨 色域限制的根源：CIE 1931 色度图显示，屏幕的 sRGB 色域只覆盖了人眼可见颜色的一小部分，尤其是青色区域，因为需要“负红色”才能显示，而这在物理上不可能。
- 🌳 自然界的超色域颜色：在落叶林中，光线穿过叶片多次过滤后，会产生比屏幕显示的绿色更饱和的“超绿”；水中由于红光被吸收，也会产生屏幕无法显示的青色和蓝色。
- 🐦 鸟类与结构色：鸟类拥有比人类更丰富的色觉，它们的羽毛通过纳米结构（如气泡或薄层）产生高饱和度的结构色，许多颜色（如孔雀的青色）超出屏幕色域。
- 🦋 蝴蝶的虹彩：蝴蝶翅膀的鳞片通过复杂结构产生虹彩色，在不同角度和偏振光下呈现从绿到蓝的色域，远超屏幕显示能力。
- 💡 人造光源中的隐藏颜色：绿色交通灯实际上是美丽的青绿色，因为 LED 发出近乎纯光谱的颜色；激光则能产生最纯净、最饱和的颜色。
- 🔦 生物发光与荧光：深海生物、萤火虫、蝎子等在黑暗中发出的青色光，是屏幕无法复制的真实颜色体验。
- 👁️ 注意力的力量：这些颜色一直存在，但只有当我们知道并留意时，才能真切感受到它们的震撼；屏幕的局限让我们低估了世界的色彩丰富度。

---

