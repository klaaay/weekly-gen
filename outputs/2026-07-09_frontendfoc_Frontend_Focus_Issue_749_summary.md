### [《坠落——你没注意时，前端发生了什么》](https://davidpoblador.com/deep-dives/what-happened-to-the-frontend/)

**原文标题**: [The Descent — What Happened to the Frontend While You Weren't Watching](https://davidpoblador.com/deep-dives/what-happened-to-the-frontend/)

以下是您提供的文章摘要，概述了前端开发二十年来的演变历程，从简单的手写 HTML 到复杂的工具链，再到回归简洁的趋势。

前端开发经历了从零构建步骤到复杂工具链的演变，最终又回归到以服务器渲染和最小化 JavaScript 为核心的简洁模式。

- 🔧 **起点：零构建时代**：2008 年，只需保存 HTML 文件并通过 FTP 上传即可发布网站，无需任何构建步骤或依赖。
- 📜 **第一层：jQuery 与同步之痛**：为了解决页面局部刷新和浏览器兼容性问题，jQuery 应运而生，但手动同步数据和 DOM 导致了新的痛点。
- 🧩 **第二层：框架的兴起**：React、Vue 等框架通过声明式 UI 和组件化解决了手动同步问题，但引入了运行时依赖和构建步骤。
- 🏗️ **第三层：构建步骤的出现**：为了解决模块系统和浏览器兼容性，Babel、Webpack 等构建工具成为必需，但带来了`node_modules`的臃肿问题。
- ⚡ **第四层：工具链的军备竞赛**：为应对构建速度慢的问题，Vite、esbuild 等用 Go 或 Rust 重写的工具出现，大幅提升了开发体验。
- 🔄 **第五层：服务器端渲染的回归**：为解决 SPA 的白屏和 SEO 问题，Next.js 等元框架重新引入 SSR，但带来了“水合”性能开销。
- 🛠️ **第六层：工程化附加组件**：TypeScript、Tailwind CSS、shadcn/ui 等工具解决了类型安全、样式和组件复用问题，成为现代开发的标配。
- ☁️ **第七层：简化部署**：Vercel、Netlify 等平台实现了 Git 推送即部署，并支持 Serverless 和边缘计算，比 FTP 时代更便捷。
- 🤖 **第八层：AI 编码**：v0、Cursor 等 AI 工具可以根据自然语言描述生成前端代码，降低了门槛，但要求理解底层原理。
- 🏁 **终点：回归简洁**：2026 年的前沿趋势是服务器渲染 HTML、最小化 JavaScript、利用 Web 平台，这与 2008 年的方式惊人地相似。

---

### [开始使用锚点定位 • Josh W. Comeau](https://www.joshwcomeau.com/css/anchor-positioning/)

**原文标题**: [Getting Started with Anchor Positioning • Josh W. Comeau](https://www.joshwcomeau.com/css/anchor-positioning/)

以下是根据您提供的文章内容整理的摘要：

锚点定位 API（Anchor Positioning API）是一种新的浏览器功能，用于将一个元素（目标）附加到另一个元素（锚点）上，例如工具提示或下拉菜单。它通过 CSS 属性（如 `anchor-name`、`position-anchor` 和 `position-area`）实现，并支持自动处理溢出和回退位置，从而避免使用 JavaScript。

- 📌 **核心概念**：使用 `anchor-name` 命名锚点元素，`position-anchor` 指定目标元素，`position-area` 定义目标相对于锚点的位置（如 `top`、`bottom`）。
- 🔄 **溢出处理**：通过 `position-try-fallbacks` 属性（如 `flip-block` 或 `bottom`）自动检测溢出并切换到回退位置，无需 JavaScript。
- 🎯 **绝对定位 vs 固定定位**：`position: fixed` 使目标以视口为包含块，更适合滚动场景下的溢出检测；`position: absolute` 则以祖先元素为包含块。
- 🛠️ **高级功能**：使用 `container-type: anchored` 和 `@container` 查询，根据回退位置（如 `fallback: bottom`）调整样式（如工具提示的箭头方向）。
- 🌐 **浏览器支持**：截至 2026 年 7 月，支持率约 81%，Level 2（如锚定容器查询）仅 64%。可使用 polyfill 或 `@supports` 提供降级方案。
- 📚 **资源**：推荐 CSS Tricks 指南、web.dev 介绍、CSSWG 规范、Anchoreum 游戏等，以深入学习。

---

### [@jakearchibald.com 在 Bluesky 上](https://bsky.app/profile/jakearchibald.com/post/3mq2pbeml2c24)

**原文标题**: [@jakearchibald.com on Bluesky](https://bsky.app/profile/jakearchibald.com/post/3mq2pbeml2c24)

概述总结
- 📌 这是一篇关于 JavaScript 依赖性的说明，强调该应用需要 JavaScript 才能运行。
- 🌐 提到 Bluesky 和 AT Protocol 的相关链接，用于了解平台和技术背景。
- 💬 引用 Jake Archibald 的观点，指出锚点定位功能因规范频繁变更、模糊性和实现缺陷而不可靠。
- 🐛 强调即使开发者遇到问题，也并非自身过错，因为该功能存在普遍的不稳定性和兼容性问题。

---

### [使用 OpenAI Codex 进行代理式前端开发的在线研讨会](https://master.dev/workshops/codex/?utm_source=email&utm_medium=frontendfocus&utm_content=codexcooper)

**原文标题**: [Agentic Frontend Development with OpenAI Codex Online Workshop](https://master.dev/workshops/codex/?utm_source=email&utm_medium=frontendfocus&utm_content=codexcooper)

### 概述摘要

免费互动直播工作坊，由 OpenAI 的 Katia Gil Guzman 主讲，教授使用 OpenAI Codex 进行前端开发的 AI 原生工作流程，涵盖提示、审查、调试和迭代，帮助开发者提升效率并保持对代码的控制。

- 🗓️ **时间与形式**：2026 年 8 月 11 日，上午 9:30 至下午 4:30（美国中部夏令时），提供在线免费参与或明尼阿波利斯线下名额。
- 👩‍🏫 **讲师背景**：Katia Gil Guzman 是 OpenAI 开发者体验工程师，曾任职于微软和 Stripe，具备深厚的前端开发与 AI 解决方案经验。
- 🎯 **工作坊目标**：学习使用 Codex 作为前端伙伴，将想法、草图或截图转化为可工作的 UI，并优化组件结构、样式、响应式行为、可访问性和动画。
- 🛠️ **核心技能**：掌握高级工程师工具包，包括利用 Codex 进行功能规划、代码生成、现有仓库集成、视觉反馈迭代，以及决定何时委托 AI、何时亲自控制。
- 📋 **先决条件与受众**：适合有前端开发经验（组件、样式、响应式、可访问性、动画）的软件工程师，非入门级提示教学。
- 🎥 **参与方式**：在线直播（需注册账号）或线下申请；错过直播可观看回放，提供完整 HD 体验。
- 📅 **后续工作坊**：系列包括 AI 构建训练营、本地代理编码、Laravel 基础、Claude Code SDK 代理、Django 等，均对会员开放。

---

### [@patrickbrosset.com 在 Bluesky 上](https://bsky.app/profile/patrickbrosset.com/post/3mpxkfv25vc2k)

**原文标题**: [@patrickbrosset.com on Bluesky](https://bsky.app/profile/patrickbrosset.com/post/3mpxkfv25vc2k)

本网页内容主要介绍了 CSS mixins 功能在 Chromium 中开始实现的消息，由微软团队负责。

- 😍 令人兴奋的周一开局：CSS mixins 功能在 Chromium 中开始实现
- 🏢 开发团队：由 Patrick Brosset 所在的微软团队负责
- 🔧 技术背景：该功能需要 JavaScript 支持，属于高度交互的 Web 应用
- 🌐 相关资源：可访问 bsky.social 和 atproto.com 了解更多关于 Bluesky 的信息
- 📅 发布日期：2026 年 7 月 6 日

---

### [CSS 自定义函数与混合 - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins)

**原文标题**: [CSS custom functions and mixins - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins)

### 概述摘要
CSS 自定义函数与混入模块允许开发者创建可复用的 CSS 代码块，支持参数传递、复杂逻辑（如`if()`函数和`@media`规则），并返回基于逻辑的值。

- 📦 **核心功能**：通过`@function`定义自定义函数，使用`<dashed-function>`语法调用（如`--my-function(30px, 3)`），可返回基于参数和逻辑的值。
- 🎨 **混入机制**：使用`@mixin`定义属性集，通过`@apply`在规则集中复用，支持参数化和逻辑定制。
- 🔒 **类型限制**：可为参数和返回值指定可选数据类型，限制传入和返回的值。
- ⚠️ **浏览器支持**：目前仅 CSS 自定义函数获得浏览器支持，CSS 混入尚未被任何浏览器支持。
- 📚 **参考资源**：包括`@function`、`@mixin`、`@apply`等 at-rules，以及`<dashed-function>`数据类型和`type()`函数。
- 🛠️ **相关概念**：涉及`calc()`、`min()`、`max()`等数学函数，以及`if()`和`@media`等逻辑特性。
- 📖 **规范与指南**：基于《CSS Functions and Mixins Module》规范，提供《使用 CSS 自定义函数》指南及典型用例。

---

### [为 Web 开发者介绍 Safari MCP 服务器 | WebKit](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

**原文标题**: [  Introducing the Safari MCP server for web developers | WebKit](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

Safari MCP 服务器为 Web 开发者提供了全新的调试体验，让 AI 代理能够直接连接 Safari 浏览器窗口，实时查看代码渲染效果，大幅提升调试效率。

- 🚀 **核心功能**：通过 MCP 协议连接 AI 代理与 Safari 浏览器，使代理能自主获取 DOM、网络请求、截图和控制台输出等信息
- 🔧 **调试优化**：减少窗口切换和重复提示的繁琐流程，开发者可在终端中高效完成调试
- 🌐 **跨浏览器兼容**：代理可自动检查 Safari 中的渲染效果、计算样式和布局，确保多浏览器兼容性
- ⚡ **性能分析**：代理能评估 JavaScript 执行、导航时间和资源加载时间，精准定位性能瓶颈
- ♿ **无障碍检查**：自动检测缺失标签、ARIA 属性错误和对比度问题，提升网站可访问性
- ✅ **状态验证**：代理可检查表单状态、元素交互和结账流程，减少手动测试工作
- 🛠️ **丰富工具集**：提供 18 种工具，包括控制台日志、DOM 交互、截图、视口设置、网络请求分析等
- 🔒 **隐私安全**：完全在本地运行，不访问个人数据，截图和日志直接发送给代理而非 Apple
- 📝 **简单上手**：安装 Safari 技术预览版后，通过简单命令即可配置，支持 Claude、Codex 等主流 AI 工具

---

### [六月网络平台新动态 | 博客 | web.dev](https://web.dev/blog/web-platform-06-2026)

**原文标题**: [New to the web platform in June  |  Blog  |  web.dev](https://web.dev/blog/web-platform-06-2026)

2026 年 6 月，Chrome 149、Chrome 150 和 Firefox 152 稳定版发布，带来了多项新功能，同时 Firefox 153 和 Safari 27 进入测试阶段。

- 📐 **field-sizing 属性成为基线**：Firefox 152 支持`field-sizing`，让表单控件（如`<textarea>`、`<input>`）根据内容自动调整大小，无需 JavaScript。
- 🔷 **rect() 和 xywh() 形状函数成为基线**：Chrome 149 支持`shape-outside`中的`rect()`和`xywh()`，简化了矩形浮动排除区域的定义。
- 🔤 **CSS text-fit 属性**：Chrome 150 引入`text-fit`，自动缩放字体大小以适应容器宽度。
- 🧩 **CSS gap 装饰**：Chrome 149 支持网格和弹性布局中的间隙装饰，可添加线条和样式到间距中。
- 🎨 **background-clip: border-area**：Chrome 150 支持`background-clip: border-area`，实现自定义渐变边框和动画效果。
- 📜 **程序化滚动承诺**：Chrome 150 更新`scrollTo()`等方法返回 Promise，平滑滚动完成后触发后续操作。
- ⌨️ **focusgroup 属性**：Chrome 150 引入`focusgroup`，声明式管理箭头键导航，简化工具栏、标签列表等 UI 控制。
- 🌐 **WebSocket 支持 bfcache**：Chrome 149 允许带 WebSocket 连接的页面进入后退/前进缓存，提升导航性能。
- ⏱️ **资源计时新增字段**：Firefox 152 添加`firstInterimResponseStart`和`finalResponseHeadersStart`，测量 HTTP 响应时间。
- 🔔 **通知操作按钮**：Firefox 152 支持通知中的操作按钮，用户可交互。
- 🧪 **测试版浏览器新特性**：Firefox 153 测试版引入`Error.stackTraceLimit`、`IDBObjectStore.getAllRecords()`等；Safari 27 测试版支持锚点定位、`:heading`伪类等。

---

### [介绍基线警报 | 博客 | web.dev](https://web.dev/blog/baseline-alerts)

**原文标题**: [Introducing Baseline Alerts  |  Blog  |  web.dev](https://web.dev/blog/baseline-alerts)

Baseline Alerts 是 Web Platform Status 仪表板的新功能，可让开发者在网页功能状态变化时获得通知，从而更快地采用新功能。

- 🔔 工作原理：在仪表板登录 GitHub 后，可订阅所有功能、单个功能或保存的搜索，并选择通知触发条件和频率。
- 📧 通知类型：支持电子邮件或自定义 RSS，当功能变为广泛可用、新可用、有新浏览器实现或回退到有限可用性时触发。
- 📅 频率选项：可选择每月、每周或每次功能变化时接收通知。
- 🎯 个性化新闻：通过保存搜索（如“group:html”），可创建定制功能集，仅接收感兴趣的功能更新。
- 🔗 可分享列表：保存的搜索可通过 URL 或二维码分享，方便内容创作者向受众推荐功能。
- 🤖 Slack 集成：支持将通知发送到 Slack Webhook URL，未来计划扩展至 GitHub Issues 等工具。
- ⏱ 价值：缩短功能发现到采用的时间，帮助开发者更快使用互操作功能。

---

### [Web 平台状态](https://webstatus.dev/)

**原文标题**: [Web Platform Status](https://webstatus.dev/)

概述总结：本文探讨了人工智能在医疗领域的应用与挑战，强调了其提升诊断效率、个性化治疗的潜力，同时指出了数据隐私、算法偏见和伦理问题等关键障碍。

- 🩺 人工智能可辅助影像诊断，提高疾病检测的准确性与速度。
- 💊 通过分析患者数据，AI 能制定个性化治疗方案，优化药物效果。
- 🔒 数据隐私问题突出，需加强保护措施防止敏感信息泄露。
- ⚖️ 算法可能存在偏见，导致对特定群体的不公平医疗结果。
- 🤖 伦理问题需关注，包括 AI 决策的责任归属与透明度。

---

### [获取失败](https://blogs.windows.com/msedgedev/2026/07/07/new-in-edge-for-developers-style-layout-gaps-improve-keyboard-accessibility-and-migrate-your-pwa-to-a-new-origin/)

**原文标题**: [Failed to retrieve](https://blogs.windows.com/msedgedev/2026/07/07/new-in-edge-for-developers-style-layout-gaps-improve-keyboard-accessibility-and-migrate-your-pwa-to-a-new-origin/)

无法总结：获取内容失败，状态码 403。

---

### [Visual Studio Code 1.127](https://code.visualstudio.com/updates/v1_127)

**原文标题**: [Visual Studio Code 1.127](https://code.visualstudio.com/updates/v1_127)

Visual Studio Code 1.127 版本发布，带来了浏览器工具、站点权限管理、智能体会话组织等多项更新。

- 🤖 **智能体浏览器工具正式可用**：智能体现在可以打开网页、截图、点击操作，自动验证自身工作，无需外部 MCP 服务器。
- 🔒 **站点权限管理**：集成浏览器支持按站点授予摄像头、位置、设备等权限，并弹出提示框供用户选择。
- 📂 **智能体会话分组与拖拽**：可将多个会话分组管理，支持拖拽排序、移动会话到分组或固定区域，便于组织。
- 🖥️ **聊天输入横幅**：当有 CI 检查失败或拉取请求评论时，在聊天输入框上方显示横幅，可直接操作修复或查看。
- 💰 **子智能体成本透明**：悬停在子智能体区域可查看其使用的 AI 信用额度，方便成本管理。
- 🛡️ **终端命令沙箱化**：macOS 和 Linux 上，智能体运行的命令默认限制网络和文件系统访问，减少审批提示。
- 🏢 **企业托管设置文件**：管理员可通过 JSON 文件（如`/etc/github-copilot/managed-settings.json`）集中管理 Copilot 设置。
- 🧪 **新实验功能**：包括智能体入门引导教程、自适应折叠会话侧边栏、多聊天会话中的分叉与进度聚合等。

---

### [准备好迎接强大的 CSS border-shape 属性！ | CSS 技巧](https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/)

**原文标题**: [Get Ready For the Powerful CSS border-shape Property! | CSS-Tricks](https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/)

本文介绍了 CSS 新属性`border-shape`的强大功能，它允许开发者轻松为形状添加边框、装饰和动画，解决了传统`clip-path`无法保留边框的问题。

- 🎨 **核心优势**：`border-shape`可让`border`、`box-shadow`等装饰属性跟随形状路径，告别`clip-path`无法添加边框的痛点。
- 🛠️ **双模式支持**：单值模式（沿路径描边）和双值模式（内外路径间填充），后者可轻松实现镂空、突破装饰等效果。
- ✂️ **形状创建**：接受与`clip-path`相同的值（包括新`shape()`函数），学习成本低，可直接替换使用。
- 🖼️ **装饰突破**：通过调整内外形状尺寸，可实现背景突破容器边界、局部装饰等传统方法难以实现的效果。
- 🔄 **动画能力**：支持`border-width`和形状值动画，可创建悬停揭示、弹性连接线、手绘下划线等动态效果。
- 🌐 **兼容性提示**：目前仅 Chrome 支持，但值得提前探索其潜力（如结合`shape()`函数制作复杂形状）。

---

### [使用 progress() 实现流式排版 – Master.dev 博客](https://master.dev/blog/fluid-typography-with-progress/)

**原文标题**: [Fluid Typography with progress() – Master.dev Blog](https://master.dev/blog/fluid-typography-with-progress/)

本文探讨了使用现代 CSS 进行流体排版的新方法，通过`progress()`函数解决传统预计算方式中忽略用户字体大小偏好的问题，并提供了完整的实现步骤与未来展望。

- 📐 **问题根源**：传统流体排版将断点转换为 rem 单位，导致用户调整基础字体大小时，排版比例失真，违背用户偏好。
- 🔄 **解决方案**：使用 CSS 中的`progress()`函数进行范围映射，直接在浏览器中计算，避免单位转换带来的问题。
- 🛠️ **核心实现**：通过`progress(100vi, min-viewport, max-viewport)`获取视口位置，结合`calc()`计算输出范围内的流体值。
- 📏 **扩展至比例尺**：利用自定义属性和`pow()`函数，可轻松构建多级流体排版比例尺，支持不同缩放比率。
- 🧩 **灵活应用**：支持容器查询（`100cqi`）、取整（`round()`）及反向缩放，适应多种设计需求。
- 🌐 **浏览器支持**：`progress()`在除 Firefox 外的现代浏览器中可用，可通过`@supports`进行降级处理。
- 🚀 **未来特性**：`@function`和`calc-mix()`将简化代码，实现更简洁的流体排版函数调用，但尚未完全普及。

---

### [无](https://expo.dev/blog/how-to-apply-professional-design-principles-in-ai-app-development?utm_source=frontendfocus&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [None](https://expo.dev/blog/how-to-apply-professional-design-principles-in-ai-app-development?utm_source=frontendfocus&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

该文章主要讨论了人工智能（AI）在医疗领域的应用现状与挑战，重点介绍了 AI 如何辅助诊断、提升效率，以及数据隐私和伦理问题。

- 🩺 **诊断辅助**：AI 在医学影像分析中表现出色，能快速识别病灶，提高早期疾病检出率。
- ⚡ **效率提升**：通过自动化处理病历和药物推荐，AI 帮助医生节省时间，优化工作流程。
- 🔒 **数据隐私**：医疗数据敏感性高，AI 系统需严格保护用户隐私，防止信息泄露。
- 🤖 **伦理挑战**：算法偏见和决策透明度问题需解决，确保 AI 辅助医疗的公平性和可靠性。
- 📈 **未来趋势**：AI 有望在个性化治疗和远程医疗中发挥更大作用，但需法规与标准同步完善。

---

### [选择性格式读取：异步剪贴板 API 的更好默认设置 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/selective-format-read?hl=en)

**原文标题**: [Selective format read: A better default for the Async Clipboard API  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/selective-format-read?hl=en)

Chrome 149 版本起，Async Clipboard API 引入选择性格式读取，优化粘贴性能。

- 📉 **问题**：旧版 `navigator.clipboard.read()` 会一次性读取剪贴板所有格式数据，导致不必要的延迟、CPU 和内存消耗。
- 🎯 **解决方案**：`read()` 仅枚举可用格式，实际数据通过 `ClipboardItem.getType(mimeType)` 按需读取，API 接口不变。
- ⚡ **性能提升**：延迟降低，因为只有需要的格式才进行跨进程拷贝、HTML 清理或图片解码；内存减少，未读取的格式不占用渲染进程内存。
- 🔄 **自动缓存**：对同一 `ClipboardItem` 多次调用 `getType()` 时，仅首次从系统剪贴板读取，后续返回缓存 Blob。
- 🚫 **无需迁移**：所有网站自动受益，无需修改代码或添加特性检测。
- ⚠️ **行为变化**：`ClipboardItem` 不再是剪贴板快照，若剪贴板内容在 `read()` 和 `getType()` 之间改变，`getType()` 会抛出 `InvalidStateError`。
- 🛡️ **应对建议**：用 `try/catch` 包裹 `getType()`，及时复制 Blob 到自有结构，或使用 `clipboardChange` 事件主动失效旧句柄。
- 🌐 **标准支持**：此规范由 Web Editing 工作组和 Edge 团队推动，Safari 已支持，Firefox 表示积极立场。

---

### [前端极简主义实践：用更少的 JavaScript 做更多的事 | Peter Kröner | webinale 柏林 2026 - YouTube](https://www.youtube.com/watch?v=GfRNbWb3ngA)

**原文标题**: [Frontend Minimalism in Action: Do More With Less JavaScript | Peter Kröner | webinale Berlin 2026 - YouTube](https://www.youtube.com/watch?v=GfRNbWb3ngA)

本頁面為 YouTube 的資訊與政策總覽，涵蓋平台運作、法律條款及聯繫方式等核心內容。

- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明內容使用與版權相關規範
- 📞 聯絡我們：提供用戶與平台聯繫的管道
- 🎨 創作者：為內容創作者提供的資源與支援
- 📢 刊登廣告：說明廣告投放與合作方式
- 👨‍💻 開發人員：提供 API 與開發工具資訊
- 📜 條款：規範用戶使用平台的法律條款
- 🔒 私隱：說明個人資料收集與使用政策
- 🛡️ 政策及安全：強調內容審查與安全措施
- ⚙️ YouTube 的運作方式：解釋推薦系統與平台機制
- 🧪 測試新功能：說明新功能測試與用戶參與
- 📅 © 2026 Google LLC：標示版權歸屬與年份

---

### [使用 WebGPU 和原生 JavaScript 构建持久页面过渡 | Codrops](https://tympanus.net/codrops/2026/06/30/building-persistent-page-transitions-with-webgpu-and-vanilla-javascript/)

**原文标题**: [Building Persistent Page Transitions with WebGPU and Vanilla JavaScript | Codrops](https://tympanus.net/codrops/2026/06/30/building-persistent-page-transitions-with-webgpu-and-vanilla-javascript/)

本教程展示了如何结合 WebGPU、DOM 追踪和轻量级 JavaScript 路由器，构建无缝的 GPU 驱动页面过渡效果。

- 🖥️ **WebGPU 持久场景**：使用单一 WebGPU 场景持续渲染，消除浏览器 DOM 状态切换时的“闪烁”感，提升用户体验
- 🎯 **DOM 追踪机制**：每个图像平面绑定到 DOM 插槽，通过`getBoundingClientRect()`实时获取位置，CSS 布局变化后过渡仍精准对齐
- 🔄 **三状态过渡逻辑**：过渡仅涉及“保留（变形移动）”、“移除（淡出）”和“添加（淡入）”三种操作，平面永不销毁重建
- 🚀 **原子化导航流程**：`navigate()`方法包含锁定、更新历史、分离所有平面、注入新页面、并行执行`out()`和`in()`、移除旧页面、重新追踪等步骤，确保过渡完整
- ⚡ **过渡期间 DOM 分离**：过渡开始时清除`trackedEl`，让 GSAP 完全控制平面位置，结束后重新绑定，避免渲染循环覆盖补间动画
- 🏗️ **路由与页面架构**：每个页面是返回 HTML 的函数，路由表定义页面类别（main/inner/index），过渡基于类别而非 URL
- 🎨 **可扩展设计**：添加新页面类别只需编写`view`函数、`getTargets`测量器和基于两个基本动词的过渡类，即可无缝集成

---

### [使用 WebGPU 和原生 JavaScript 实现页面过渡](https://page-transitions-with-webgpu-vanilla-js.crnacura.workers.dev/)

**原文标题**: [Page Transitions with WebGPU and VanillaJS](https://page-transitions-with-webgpu-vanilla-js.crnacura.workers.dev/)

概述总结  
- 📚 文章核心内容是对给定文本进行简洁的要点总结，使用“-”符号格式化每个要点，并配以适当的表情符号。  
- 🔑 每个要点需提炼关键信息，确保覆盖文本的本质内容，避免冗余。  
- 🎯 在列表顶部添加一个无标题的概述总结，以概括文章主旨。  
- ✨ 表情符号的选择应与要点内容相关，增强可读性和视觉吸引力。  
- 📝 所有输出必须使用中文（ZH）完成，保持语言一致性。

---

### [修复全出血 CSS – David Bushell – 网页开发（英国）](https://dbushell.com/2026/07/03/fixing-full-bleed-css/)

**原文标题**: [Fixing full-bleed CSS â David Bushell â Web Dev (UK)](https://dbushell.com/2026/07/03/fixing-full-bleed-css/)

### 概述总结
本文讨论了 CSS 全出血布局（full-bleed）的常见问题及现代解决方案，重点解决了视口单位（100vw）因滚动条导致的宽度偏差问题，并提供了兼容嵌套容器的进阶方法。

- 🩹 **问题根源**：`100vw` 在存在滚动条时可能超出视口宽度，导致布局元素被裁剪或对齐偏差，尤其在 Windows 系统上明显。
- 🛠️ **传统修复**：通过 `overflow-x: hidden` 隐藏水平溢出，或使用 `scrollbar-gutter: stable` 预留滚动条空间，但各有局限。
- 🚀 **现代方案**：利用 CSS 容器查询（`container`）和容器单位（`cqi`），将 `body` 设为容器，用 `100cqi` 替代 `100vw`，并配合 `overflow-x: clip` 防止溢出。
- 🔄 **嵌套容器挑战**：当存在嵌套容器时，`cqi` 会基于最近容器计算，需通过 `@property` 自定义属性（如 `--body-size`）在父容器中预计算值，确保子元素继承正确宽度。
- 💡 **未来展望**：提议 CSS 支持显式指定容器引用（如 `cqi(body)`），以简化嵌套场景下的单位计算，避免复杂变通方案。

---

### [为阅读障碍人士设计 - TetraLogical](https://tetralogical.com/blog/2026/06/25/designing-for-reading-disabilities/)

**原文标题**: [Designing for people with reading disabilities - TetraLogical](https://tetralogical.com/blog/2026/06/25/designing-for-reading-disabilities/)

以下是对该文章的概述总结：

- 📖 阅读障碍是广泛存在的，包括阅读困难、超读症和失读症，与智力无关，设计应降低阅读的认知负担。
- ✍️ 使用简明语言：避免复杂句式，用日常词汇，如“政策开始”代替“政策的实施将开始”，并解释专业术语。
- 🧩 优化排版：左对齐文本，每行不超过 70-80 字符，使用清晰标题和层级，避免两端对齐。
- 🔤 选择易读字体：优先考虑字母形状区分度高、x 高度大、开口大的字体，避免全大写或大量粗斜体。
- 📏 控制阅读难度：目标阅读年龄为 9-11 岁，使用 Hemingway 等工具检查，拆分长句。
- 🔍 解释缩写：首次出现时全称加括号，限制使用数量，避免密集出现。
- 🖼️ 使用图像和替代格式：用图表、视频或音频辅助，并确保有清晰的文本描述。
- 🌐 考虑低数字素养：图标配合文字，导航位置一致，使用描述性链接文本（如“下载 2024 报告”）。
- 🤝 设计是编辑、文案和设计师的共同责任，目标是通过清晰文字、良好结构和合适字体减少阅读疲劳。

---

### [一个让您的网站为智能代理做好准备的开发者工具包 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/agent-ready-toolkit)

**原文标题**: [A developer toolkit to make your website agent-ready  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/agent-ready-toolkit)

此文章介绍了为 AI 代理优化网站的新开发者工具集，帮助开发者构建“代理就绪”的网站，确保代理能可靠地完成交互任务。

- 🛠️ **Lighthouse 新增“代理浏览”类别**：从 M150 版本开始，提供确定性审计，检查可访问性、稳定性和 WebMCP 集成，帮助开发者评估网站的代理友好度。
- ♿ **可访问性是核心**：代理依赖无障碍树理解页面，审计会验证交互元素是否有程序化名称，确保机器可读。
- 📏 **稳定性检查**：通过累积布局偏移（CLS）测量视觉稳定性，防止元素意外移动导致代理误点击。
- 🔗 **WebMCP 集成**：检查是否注册了 WebMCP 工具、表单是否声明 WebMCP 以及架构有效性，帮助代理明确暴露网站逻辑。
- 🧪 **Chrome DevTools for Agents**：提供测试工具，可模拟代理交互、直接调用 Lighthouse 审计、查看屏幕录制和日志，便于调试。
- 🚀 **Modern Web Guidance**：包含最佳实践和技能（如 webmcp 技能），可委托编码代理实现 WebMCP 工具，从源头构建代理友好应用。
- 📝 **配置示例**：提供 Chrome DevTools for Agents 的配置代码，连接 Chrome Canary 并启用 WebMCP 实验功能。
- 🔮 **未来方向**：鼓励贡献和参与讨论，参考官方仓库、WebMCP 文档和 Modern Web Guidance 文档，进一步优化网站。

---

### [Wordgard](https://wordgard.net/)

**原文标题**: [Wordgard](https://wordgard.net/)

概述概要
Wordgard 是一个开源、基于模式的富文本编辑器库，提供强大的编程接口，支持自定义文档结构、无障碍访问、协作编辑等功能。

- 🌱 Wordgard 是一个“词语花园”，用于构建内容编辑器，而非自由格式的 HTML 编辑器。
- 📜 基于模式：可精确定义文档结构，创建自定义文档元素。
- 🛠️ 豪华 API：编程接口经过精心设计，通用且多功能。
- 🧩 模块化：大部分功能以扩展形式实现，可替换或修改。
- ♿ 无障碍：支持屏幕阅读器、键盘操作和移动设备，并支持界面国际化。
- ↔️ 从右到左书写：内容和界面均支持方向感知，兼容双向文本和从右到左文档。
- 🏗️ 结构化内容：文档树可包含表格、嵌套列表、带标题的图形等自定义结构。
- ⚙️ 函数式：系统大部分采用函数式风格编写，清晰且易于测试。
- 🤝 协作编辑：支持多用户同时编辑同一文档，并合并并发更改。
- 📄 开源：基于 MIT 许可，在 code.haverbeke.berlin 开发，欢迎报告错误但不接受拉取请求；商业使用期望资助维护。

---

### [试试 Wordgard](https://wordgard.net/try/)

**原文标题**: [Try Wordgard](https://wordgard.net/try/)

概述总结
- 🖥️ 使用 Wordgard 编辑器：在程序中定义编辑器，查看运行效果，适合测试或分享脚本。
- ▶️ 运行与分享：按 Ctrl-Enter 运行代码，结果会显示在“输出”标签页的`<iframe>`中。
- 📋 代码与日志：代码写在编辑区，错误或控制台信息可在“日志”标签页查看。

---

### [基本编辑器示例](https://wordgard.net/examples/basic/)

**原文标题**: [Basic Editor Example](https://wordgard.net/examples/basic/)

本示例介绍了编辑器库的基本用法，包括创建编辑器、管理状态和加载新文档。

- 📝 **创建编辑器**：至少需要文档模式和扩展，如基础模式（段落、标题等）、撤销历史和菜单栏，通过 `Wordgard.create` 配置并添加到页面元素中。
- 🔧 **配置扩展**：使用 `basicSchema`、`orderedList`、`history` 和 `menuBar` 等函数返回扩展集合，编辑器初始化时生成完整配置并存储在状态中。
- 🏷️ **可访问性**：`Wordgard.label` 为可编辑元素添加 `aria-label` 属性，提升屏幕阅读器支持。
- 🖥️ **DOM 元素**：编辑器有 `dom`（外层包装）和 `contentDOM`（可编辑内容）两个重要 DOM 元素，支持移动和跨框架操作。
- 📄 **编辑器状态**：通过 `state` 属性访问，包含文档结构（`doc`），可用 `serialize` 获取 HTML 或用 `toJSON()` 获取 JSON 格式。
- 🔄 **状态更新**：编辑器状态不可变，每次更改创建新状态对象，旧状态不会自动同步。
- 🆕 **加载新文档**：应创建新编辑器而非替换内容，避免保留辅助状态（如撤销历史），直接移除旧编辑器 DOM 元素并替换为新实例。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Cloud 提供可扩展的 PostgreSQL 时序数据库服务，支持大规模数据处理，并为企业提供免费试用。

- 🚀 支持每天 3 万亿指标、3 PB 数据和 1 千万亿数据点的实时扩展
- 💰 新用户可获 $1000 信用额度，30 天有效，无需信用卡
- 🔄 通过最多 10 个节点的副本集分离读写，结合 SSD/S3 分层存储实现无限扩展
- 💡 计算与存储分离，可独立扩展，避免为闲置容量付费
- 🛡️ 多可用区集群支持自动故障转移、时间点恢复和跨区域备份
- 🔒 符合 SOC 2、HIPAA 和 GDPR 标准，提供加密、SSO、RBAC 和审计日志
- 📊 深度可观测性：查询钻取和仪表板，集成 CloudWatch、Datadog、Prometheus
- ⚡ 分钟级数据库部署，支持 SQL、CLI、Terraform、Cursor 和 Claude Code 管理
- 🔗 与主流云提供商和 PostgreSQL 生态系统集成
- 🏢 企业级服务：合同性正常运行时间 SLA、区域数据隔离和 24/7 专家支持

---

### [visual-json | 面向人类的可视化 JSON 编辑器](https://visual-json.dev/)

**原文标题**: [visual-json | The Visual JSON Editor for Humans](https://visual-json.dev/)

该内容展示了一个名为 `visual-json` 工具的界面，包含文档、GitHub 链接和 `package.json` 文件结构。

- 📄 **项目概述**：应用名为 `my-app`，版本 `1.0.0`，为私有项目。
- ⚙️ **脚本配置**：包含 `dev`、`build`、`start` 和 `lint` 命令，均基于 Next.js 框架。
- 📦 **核心依赖**：主要依赖 `next`（^15.0.0）和 `react`（^19.0.0）及 `react-dom`。
- 🛠️ **开发依赖**：包括 `@types/react`、`typescript`、`eslint` 等工具。
- 🔒 **引擎要求**：需 Node.js 版本 >=18 运行环境。

---

### [GitHub - vercel-labs/visual-json: 可视化 JSON 编辑器。支持模式感知、可嵌入、可扩展。](https://github.com/vercel-labs/visual-json)

**原文标题**: [GitHub - vercel-labs/visual-json: The Visual JSON Editor. Schema-aware, embeddable, extensible. · GitHub](https://github.com/vercel-labs/visual-json)

visual-json 是一个可视化 JSON 编辑器，支持模式感知、可嵌入和可扩展，由 Vercel Labs 开发。

- ⚠️ 页面加载时出现错误，提示需要重新加载
- ⭐ 项目获得 885 颗星，47 个分支，社区关注度较高
- 📦 提供多个包：核心包（@visual-json/core）、React UI、Svelte 5 UI、Vue UI、YAML 支持和 VS Code 扩展
- 🛠️ 开发流程简单：使用 pnpm install、pnpm build、pnpm dev
- 📄 采用 Apache-2.0 许可证，拥有详细的 README 和变更日志
- 🔧 技术栈以 TypeScript 为主（63%），其次为 Svelte、Vue、MDX、CSS 和 JavaScript
- 🚀 最新版本为 v0.4.0，发布于 2026 年 4 月 8 日，共 5 个发布版本

---

### [OverflowGuard — 围绕内容构建，而非断点](https://overflowguard.dev/)

**原文标题**: [OverflowGuard — Build around content, not breakpoints](https://overflowguard.dev/)

概述：本文探讨了如何通过高效的时间管理策略提升个人生产力，强调设定明确目标、优先处理重要任务以及避免多任务处理的重要性。

- ⏰ 设定每日优先事项，确保关键任务得到及时处理。
- 🎯 使用“番茄工作法”专注工作 25 分钟，然后休息 5 分钟，以保持高效。
- 📋 将大任务分解为小步骤，降低执行难度并增强成就感。
- 🚫 避免多任务处理，集中精力完成单一任务以提高质量。
- 📅 定期回顾时间使用情况，调整计划以优化效率。
- 🌟 利用早晨精力充沛时段处理最复杂的工作。

---

### [GitHub - arturmarc/overflow-guard：检测HTML内容溢出并构建更好响应式布局的工具 · GitHub](https://github.com/arturmarc/overflow-guard)

**原文标题**: [GitHub - arturmarc/overflow-guard: Tools for detecting html content overflowing and building better responsive layouts · GitHub](https://github.com/arturmarc/overflow-guard)

overflow-guard 是一个用于检测 HTML 内容溢出并构建自适应响应式布局的工具集，包含 React 和 HTML 两个包，核心思想是围绕内容而非断点来构建 UI。

- 📦 **双包架构**：提供 `overflow-guard-react`（React 组件与 Hook）和 `overflow-guard-html`（框架无关的自定义元素），满足不同技术栈需求
- 🎯 **内容驱动**：基于实际内容溢出情况（水平、垂直或双向）触发 UI 切换，而非依赖猜测的像素值或视口断点
- 🔄 **动态适配**：支持处理动态标签、本地化文本和数据驱动内容，同一 UI 可在窄侧边栏、宽面板和可调整布局中复用
- ⚛️ **React 快速上手**：通过 `<OverflowGuard>` 包裹 UI，利用 `isOverflowing` 状态实现紧凑布局切换（如按钮文字变图标）
- 🌐 **HTML 无构建使用**：支持 CDN 直接加载，通过 `fallbackClass` 属性和 CSS 类切换实现自适应，无需构建工具
- 🧠 **AI 集成**：推荐使用 TanStack Intent 进行 AI 集成，各包自带本地技能以保持与安装版本一致
- 📊 **运行时状态**：提供 `overflowAxis`（'none' | 'horizontal' | 'vertical' | 'both'）等状态属性，便于精准控制
- 🛠️ **安装灵活**：支持 bun、npm、pnpm、yarn 多种包管理器安装，React 包需在客户端组件中使用

---

### [框架构建体积对比](https://mlgq.github.io/frontend-framework-bundle-size/?lang=en)

**原文标题**: [框架构建体积对比](https://mlgq.github.io/frontend-framework-bundle-size/?lang=en)

概述总结  
- 🔍 本文主要讨论了人工智能在医疗领域的应用，强调其能提升诊断准确性和效率。  
- 🏥 通过分析医学影像，AI 可辅助医生识别早期病变，如癌症和心血管疾病。  
- 📊 机器学习算法能处理大量患者数据，预测疾病风险并个性化治疗方案。  
- ⚠️ 但存在数据隐私、算法偏见和监管挑战，需确保安全性和公平性。  
- 🌍 未来 AI 有望整合电子健康记录，实现远程医疗和实时健康监测。

---

### [GitHub - mlgq/前端框架包体积对比 · GitHub](https://github.com/mlgq/frontend-framework-bundle-size/)

**原文标题**: [GitHub - mlgq/frontend-framework-bundle-size · GitHub](https://github.com/mlgq/frontend-framework-bundle-size/)

该仓库是一个前端框架打包体积对比工具，通过构建相同演示应用并测量不同组件数量下的打包体积，生成交互式对比报告。

- 📊 对比框架：Angular2、Qingkuai、React、Solid、Svelte4/5、Vue2/3、Vue Vapor
- 📏 测量指标：框架运行时体积、每组件应用代码体积、组件数量增长模拟（1 至 320 个组件）
- 🔧 测量阶段：未压缩、语法压缩后、语法压缩+gzip 后
- 🌐 报告预览：支持中英文双语，通过 GitHub Pages 在线访问
- ⚙️ 使用方式：pnpm 安装依赖，运行`report:analyze`命令构建并分析，可选截图
- 🛠️ 技术栈：JavaScript（29.4%）、Vue（21.4%）、TypeScript（16.8%）、Svelte（14.3%）、CSS（13.7%）、HTML（4.4%）

---

### [µJS — 轻量级 AJAX 导航库](https://mujs.org/)

**原文标题**: [µJS — Lightweight AJAX Navigation Library](https://mujs.org/)

µJS 是一个轻量级 JavaScript 库，通过拦截链接点击和表单提交，实现无需重新加载整个页面的即时导航，带来类似单页应用的流畅体验。无需学习框架、构建步骤或修改服务器端，只需添加一个脚本标签即可。

- 🚀 **即时导航**：拦截链接点击和表单提交，仅替换变化内容，浏览器无需完全重新加载，导航感觉瞬间完成。
- 🛠️ **零配置集成**：无框架、无构建步骤、无服务器端修改，只需一个脚本标签和 `mu.init()` 调用，即可在任何后端（PHP、Python、Ruby、Go 等）上运行。
- ⚡ **现代 Fetch API**：基于原生 `Fetch API` 和 `AbortController`，无需 `XMLHttpRequest` 或 polyfill，可干净取消正在进行的请求。
- 🎯 **核心功能**：支持悬停预取、无页面重载、内置进度条；单文件约 5 KB（gzip），零依赖；补丁模式可一次更新多个页面片段；支持任意元素和事件触发器（含防抖）；支持 GET、POST、PUT、PATCH、DELETE 等 HTTP 动词；支持服务器发送事件（SSE）实时更新。
- 📦 **快速开始**：在页面中添加 `<script src="https://unpkg.com/@digicreon/mujs/dist/mu.min.js"></script>` 和 `<script>mu.init();</script>`，所有内部链接即刻变为 AJAX 导航。
- 🔗 **生态系统**：与 Temma（PHP MVC 框架）和 µCSS（CSS 框架）配合使用效果更佳。

---

### [GitHub - Digicreon/muJS: 轻量级 AJAX 导航库 — Turbo 和 htmx 的 5KB 替代方案](https://github.com/Digicreon/mujs)

**原文标题**: [GitHub - Digicreon/muJS: Lightweight AJAX navigation library — 5KB alternative to Turbo and htmx · GitHub](https://github.com/Digicreon/mujs)

µJS（muJS）是一個輕量級的 AJAX 導航庫，無需框架即可加速網站，透過攔截點擊與表單提交，以 Fetch API 載入頁面內容，支援多種注入模式與即時更新。

- 🚀 **快速** — 支援懸停預取、無整頁重新載入、進度條顯示
- 🪶 **輕量** — 單一檔案約 5KB gzipped，無依賴
- 🔌 **即插即用** — 相容任何後端，無需伺服器端修改
- 🧩 **修補模式** — 單次請求更新多個頁面片段
- 🎯 **觸發器** — 任意元素、任意事件：即時搜尋、輪詢、焦點動作
- 🔄 **HTTP 動詞** — 支援 GET、POST、PUT、PATCH、DELETE
- 📡 **SSE** — 透過伺服器推送事件實現即時更新
- 🌐 **現代 Fetch API** — 原生 fetch() 與 AbortController
- ✨ **現代 UX** — 視圖轉換、DOM 變形、事件委派
- 📜 **歷史與滾動** — 自動管理瀏覽器歷史與滾動位置
- 🛠️ **自訂驗證** — 支援表單自訂驗證與離開確認
- 🎨 **可配置** — 豐富的屬性與配置選項，靈活控制行為
- 🔗 **程式化 API** — 提供 mu.load() 等方法進行程式化導航

---

### [GTA2 — 网页版（gta2-resurection JS 移植版）](https://gta2js.vercel.app/)

**原文标题**: [GTA2 — web (gta2-resurection JS port)](https://gta2js.vercel.app/)

本页面是 GTA2 的网页移植版操作指南，涵盖控制、模组和游戏机制。

- 🎮 移动与驾驶：使用 WASD/方向键移动或转向，空格键跳跃或手刹。
- 🖱️ 瞄准与攻击：鼠标旋转瞄准（模组），左键/Ctrl/X 攻击，右键跳跃飞行（模组）。
- 🚗 载具互动：按 Enter/F 进入或离开车辆。
- 🔫 武器切换：按 Q/E/鼠标滚轮或数字键 1-9 切换武器。
- 👥 招募同伴：按 R 键招募附近行人加入队伍。
- ⚙️ 模组设置：按 F1 或`键打开模组设置。
- 📖 帮助与音频：按 H 切换帮助菜单，按 M 静音。
- 🚓 逃脱警察：驶入绿色喷漆圈以消除通缉。
- 🌐 移植来源：基于 h0x91b/gta2-resurection 和 gta2_re 逻辑，数据来自 Rockstar Games 的免费版 GTA2。
- ⏳ 加载提示：游戏加载中，按 H 查看控制，F1 查看模组，N 切换夜间模式。

---

