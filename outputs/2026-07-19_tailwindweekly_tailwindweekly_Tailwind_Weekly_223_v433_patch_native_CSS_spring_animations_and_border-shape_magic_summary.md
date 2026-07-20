### [发布 v4.3.3 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.3?ref=tailwindweekly.com)

**原文标题**: [Release v4.3.3 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.3?ref=tailwindweekly.com)

Tailwind CSS v4.3.3 版本发布，修复了多项关键问题，提升了 CLI 工具、CSS 解析和浏览器兼容性等方面的稳定性。

- 🛠️ 修复 `@tailwindcss/cli` 中 `--watch --poll` 模式在文件系统事件不可靠时无法工作的问题
- 🎨 支持任意十六进制颜色与主题颜色进行大小写不敏感的匹配（如 `bg-[#fff]` 和 `bg-[#FFF]` 都会匹配到 `bg-white`）
- 🖥️ 防止 Preflight 覆盖 Firefox 中 `iframe:focus-visible` 的原生轮廓样式
- 🔧 修复 JS 插件中 `theme('colors.foo')` 在同时存在 `--color-foo` 和 `--color-foo-bar` 时的解析问题
- 📐 确保分数透明度修饰符（如 `shadow-sm/12.5`）与命名的阴影大小正常工作
- ✂️ 修复选择器 `[data-foo]div` 被错误解析为一个选择器的问题，现正确解析为两个
- 🔄 确保 `@tailwindcss/postcss` 在 Sass 等预处理器更改输入 CSS 但文件未变更时能正确重建
- 🌐 修复 CSS 嵌套在 Lightning CSS 未运行时（如 `@tailwindcss/browser` 和 Tailwind Play）的处理问题
- 🎨 防止无彩色主题颜色在 `oklch` 等极性色彩空间中混合时发生色相偏移
- 📏 优化 `--spacing(0)` 为 `0px` 而非 `0`，确保在 `calc(...)` 中保持 `<length>` 类型
- ⚡ 仅在 `@tailwindcss/cli --watch` 模式下按需加载 `@parcel/watcher`，避免无法加载时影响其他模式
- 🌍 使用明确的平台字体替代 `system-ui` 和 `ui-sans-serif`，使 CJK 文本在 Windows 上尊重页面的 `lang` 属性
- 🗂️ 防止 `@tailwindcss/upgrade` 在子目录运行时重写忽略的文件
- 📂 确保较早的 `@source` 规则指向的嵌套文件在后续 `@source` 规则指向父文件夹时仍能被扫描
- 🔄 防止 `@tailwindcss/vite` 在扫描文件被 Vite 处理但未作为模块加载时触发全页面重载

---

### [发布 v0.16.0 · tailwindlabs/tailwindcss-intellisense · GitHub](https://github.com/tailwindlabs/tailwindcss-intellisense/releases/tag/v0.16.0?ref=tailwindweekly.com)

**原文标题**: [Release v0.16.0 · tailwindlabs/tailwindcss-intellisense · GitHub](https://github.com/tailwindlabs/tailwindcss-intellisense/releases/tag/v0.16.0?ref=tailwindweekly.com)

概述总结  
- 🚨 页面加载时出现错误，需重新加载  
- 📦 Tailwind CSS IntelliSense 发布 v0.16.0 版本  
- 🐛 修复了多个问题，包括诊断源添加、性能提升和初始化错误  
- 🔧 改进大型文件和 v4 版本的实用工具查找性能  
- ⚠️ 标记 `@variant` 在自定义变体中为已弃用  
- 📏 为 `@container` 显示像素等效值  
- 🖥️ 修复 Vue 文件中类悬停和 `cssConflict` 警告问题  
- 🔒 发布版本由 Robin Malfait 签名并验证

---

### [发布 v0.8.1 · tailwindlabs/prettier-plugin-tailwindcss · GitHub](https://github.com/tailwindlabs/prettier-plugin-tailwindcss/releases/tag/v0.8.1?ref=tailwindweekly.com)

**原文标题**: [Release v0.8.1 · tailwindlabs/prettier-plugin-tailwindcss · GitHub](https://github.com/tailwindlabs/prettier-plugin-tailwindcss/releases/tag/v0.8.1?ref=tailwindweekly.com)

概述总结
- 🐛 修复了在 JavaScript 字符串字面量中排序类时删除转义序列的问题，该问题可能导致 Vue 属性表达式生成无效代码
- 🔧 恢复了在使用 prettier-plugin-svelte v4 时，Svelte 标记和动态 class={...} 表达式中的类排序功能
- 📦 发布了 v0.8.1 版本，包含上述修复
- 🔑 该提交由 Robin Malfait 使用 SSH 密钥签名验证
- 👥 获得了社区的反应：1 个🎉和 3 个❤️

---

### [我们将您的设计转换为 Tailwind CSS 代码 | Design2Tailwind](https://design2tailwind.com/?ref=tailwindweekly.com)

**原文标题**: [We convert your design to Tailwind CSS code | Design2Tailwind](https://design2tailwind.com/?ref=tailwindweekly.com)

本網站提供將設計稿轉換為 Tailwind CSS 代碼的專業服務，由一對姊妹團隊運營，擁有超過 15 年前端經驗。服務涵蓋多種設計工具與框架，流程清晰，並提供報價、修改與跨瀏覽器測試。

- 🎨 支援 Figma、Sketch、Adobe XD、Photoshop 等多種設計工具
- ⚛️ 可適配 React、Vue、Astro、Alpine.js、Shopify、Statamic 等框架
- 👩‍💻 由 Vivian 和 Daniela 姊妹直接溝通與編碼，無中間人傳話
- 🧹 代碼風格乾淨、可預測、易於擴展，最小化自定義 CSS
- 🌐 支援 Chrome、Safari、Firefox、Edge 等最新瀏覽器測試
- 📋 流程包含：分析需求、溝通、編碼、反饋調整、交付
- 💰 定價從首頁 $350 起，額外頁面 $120，提供 3 輪修改
- 📞 可透過表單索取報價，24 小時內回覆
- 🗣️ 客戶好評：效率高、細節注重、代碼整合順暢
- 📦 交付內容包括完整專案檔案，可一鍵運行

---

### [Baselair - 微缩模型画师的最佳社区](https://thebaselair.com/?ref=tailwindweekly.com)

**原文标题**: [Baselair - The best community for miniature painters](https://thebaselair.com/?ref=tailwindweekly.com)

这是一个微型模型爱好者的社区平台，汇集了各种主题和风格的模型作品展示。

- 🎨 社区专注于微型模型涂装，欢迎分享作品并与其他爱好者交流
- 🏷️ 作品涵盖多种主题：动漫、奇幻、科幻、历史、恐怖、军事、赛博朋克等
- 👤 每个作品展示包括作者、点赞数、保存数和评论数
- 📊 热门作品示例：Dwarf Lord（34 赞）、Medusa（134 赞）、Mandalorian Initiates（138 赞）
- 🖼️ 平台提供发现、筛选和排序功能，方便浏览不同风格模型
- 🎯 用户可关注作者、保存喜欢作品，形成互动社区
- 🎭 作品类型多样，从角色模型到场景地台，从奇幻到科幻应有尽有

---

### [获取失败](https://flxwebsites.com/?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://flxwebsites.com/?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 403。

---

### [原生 CSS 中的弹簧与弹跳效果 • Josh W. Comeau](https://www.joshwcomeau.com/animation/linear-timing-function/?ref=tailwindweekly.com)

**原文标题**: [Springs and Bounces in Native CSS • Josh W. Comeau](https://www.joshwcomeau.com/animation/linear-timing-function/?ref=tailwindweekly.com)

以下是您提供的文章内容摘要：

CSS `linear()` 函数是一种新的计时函数，通过指定多个点来模拟弹簧、弹跳等复杂动画，弥补了贝塞尔曲线的不足。

- 📚 **简介**：`linear()` 函数通过连接多个点来绘制缓动曲线，而非使用数学曲线，可用于模拟弹簧和弹跳等效果。
- 🛠️ **动态生成**：推荐使用工具如 Linear() Easing Generator 或 Easing Wizard 自动生成 `linear()` 值，避免手动编写。
- ⏱️ **局限性**：仍基于时间（需指定持续时间），无法完美模拟零阻尼弹簧；中断时缺乏惯性，行为不自然。
- 💻 **性能**：即使包含 40+ 数据点，帧率影响可忽略；CSS 包体积增加有限（如 3 个弹簧约增 1.3kB gzip）。
- 🎯 **有效使用**：建议将 `linear()` 存储在 CSS 变量中，配合 `@supports` 为旧浏览器提供贝塞尔曲线回退，并遵循 80/20 规则保持一致性。
- 🔍 **深入**：文章作者在动画课程中进一步探讨了 `linear()` 与其他技术的结合应用。

---

### [使用 Web 标准的暗黑模式](https://olliewilliams.xyz/blog/dark-mode/?ref=tailwindweekly.com)

**原文标题**: [Dark mode with web standards](https://olliewilliams.xyz/blog/dark-mode/?ref=tailwindweekly.com)

### 概述总结
本文介绍了使用 Web 标准实现深色模式的方法，重点是如何通过`color-scheme`和`prefers-color-scheme`媒体查询来尊重用户系统设置，同时提供网站内的手动切换功能。

- 🌓 **默认尊重系统设置**：使用`<meta name="color-scheme" content="light dark">`标签，让网站首次加载时自动匹配用户操作系统偏好。
- 🔄 **支持用户手动覆盖**：通过 JavaScript 切换`<meta>`标签的`content`属性值为`light`、`dark`或`light dark`，并将选择保存到`localStorage`中。
- 🎨 **`color-scheme`影响范围**：包括`light-dark()`函数中的颜色、系统颜色（如`Canvas`）、滚动条颜色、HTML 元素默认颜色、iframe 样式（需内嵌文档同意）以及使用`light-dark()`或`prefers-color-scheme`的 SVG。
- 🚫 **`color-scheme`不影响**：`prefers-color-scheme`媒体查询（除非在 iframe 或 SVG 中），因此无法通过它实现页面内切换；`<picture>`元素中的媒体查询也不受影响。
- 🖼️ **`light-dark()`扩展应用**：支持渐变和图片切换，例如根据模式使用不同渐变或图片资源（需 Chrome/Edge 150+、Firefox 150+、Safari TP）。
- 🛠️ **处理非颜色变化**：通过 CSS 自定义属性（如`--dark`）和样式查询（`@container style()`）实现阴影、边框等非颜色元素的模式切换。
- 🔮 **未来展望**：可能通过 JavaScript 覆盖`prefers-color-scheme`媒体查询（Chrome Canary 有原型，但 Safari 团队反对）。

---

### [准备好迎接强大的 CSS border-shape 属性吧！| CSS 技巧](https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/?ref=tailwindweekly.com)

**原文标题**: [Get Ready For the Powerful CSS border-shape Property! | CSS-Tricks](https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/?ref=tailwindweekly.com)

CSS border-shape 属性为形状设计带来革命性突破，支持边框、阴影跟随形状，并实现动画效果。

- 🎨 **核心功能**：border-shape 可替代 clip-path，让 border、box-shadow 等装饰属性完美贴合形状边缘，解决传统 CSS 形状无法添加边框的痛点。
- ⚡ **双模式语法**：支持单值（描边模式）和双值（填充模式），双值可定义内外边界，轻松实现镂空、切割等复杂效果。
- 🌟 **突破性装饰**：通过调整形状参数（如 inset(0 -100vw)）可创建突破元素边界的背景装饰，或实现局部装饰效果。
- 🔄 **动画支持**：支持 border-width 动画（如悬停展开）和形状值动画（如弹性变形），可制作手绘下划线、电光边框等动态效果。
- 🛠️ **兼容性**：目前仅 Chrome 支持，但已可结合 shape() 函数实现 SVG 级形状控制，并配有在线生成器简化创作。
- 💡 **实战案例**：包括边框加载动画、可拖拽弹性连接线、悬停变形气泡等，展示从基础形状到复杂交互的完整应用场景。

---

### [Juicy - 自定义 Mac 电池提醒与健康监测](https://getjuicy.app/?ref=tailwindweekly.com)

**原文标题**: [Juicy - Custom Mac Battery Alerts & Health Monitoring](https://getjuicy.app/?ref=tailwindweekly.com)

Juicy 是一款专为 Mac 设计的电池管理应用，提供自定义提醒、健康监测、设备追踪等功能，弥补了 macOS 原生的不足。

- 🍎 **解决原生痛点**：macOS 仅提供 10% 和 5% 的电池提醒，且无法自定义；Juicy 允许设置任意电量提醒，并消除烦人的原生弹窗。
- 🔔 **精美自定义提醒**：支持在 3%、20%、80% 等任意电量设置提醒，通知带有屏幕发光效果，美观且不易错过。
- 📊 **电池健康追踪**：实时显示健康度、循环次数、温度，并提供 Apple 维修建议，所有信息一目了然。
- 🖥️ **主题化菜单栏图标**：提供紧凑的 iPhone 风格电池图标，可显示百分比，节省空间且智能变色。
- 🔄 **生命周期提醒**：对充电、拔电、80% 电量等事件发出通知，可自定义声音，帮助保护电池寿命。
- 📱 **多设备追踪**：同时查看 AirPods、iPhone、iPad、Magic Mouse 等设备的电量，支持低电量和充满提醒。
- 🚫 **自动关闭原生提醒**：自动消除 macOS 烦人的电池弹窗，不干扰工作流程。
- 🔋 **充电限制与保养**：可将充电限制在 50%-80% 区间，支持航行模式、自动放电和一键补电至 100%。
- ⚡ **应用能耗洞察**：实时查看各应用耗电情况，支持 24 小时、7 天、30 天历史记录，快速找出耗电大户。
- 🛠️ **外接设备支持**：连接 iPhone 或 iPad 后，可查看其真实电池健康度、循环次数和温度。
- 💻 **原生 Mac 体验**：使用 Swift 编写，专为 Apple Silicon 优化，CPU 占用低于 0.1%，非 Electron 应用。
- 💰 **定价灵活**：提供 3 天免费试用（无需信用卡）；Pro 版 $14.99（一年更新），终身版 $24.99（永久更新），支持 14 天退款。
- 👨‍💻 **独立开发**：由独立开发者 Dominik 打造，注重品质，无风险投资或企业臃肿。
- ❓ **常见问题**：兼容 macOS 15.0+（Sequoia），支持 Apple Silicon 和 Intel；数据本地处理，隐私安全；与 AirBuddy、coconutBattery 等相比，功能更全面且集成度高。

---

### [GitHub - petekp/tw-fade 位于 tailwindweekly.com · GitHub](https://github.com/petekp/tw-fade?ref=tailwindweekly.com)

**原文标题**: [GitHub - petekp/tw-fade at tailwindweekly.com · GitHub](https://github.com/petekp/tw-fade?ref=tailwindweekly.com)

tw-fade 是一個專為 Tailwind CSS v4 設計的滾動感知邊緣淡出工具，完全基於 CSS，無需 JavaScript。

- 🎭 使用 CSS 遮罩實現滾動感知淡出，內容在滾動到邊緣時自然消失
- 🚫 無需額外 DOM 元素，遮罩直接應用於滾動容器本身
- 🌐 表面中性，遮罩能揭示元素背後的內容，而非繪製假背景色
- 🧩 可組合使用方向、大小、滾動距離和清除區域等獨立工具
- 📦 支援 Tailwind v4 源路徑和預構建 CSS 兩種安裝方式
- 🔄 支援所有四個邊緣的淡出，包括物理垂直和邏輯水平方向
- ⚙️ 可自定義淡出帶寬度（fade-size-*）和滾動開啟速度（fade-travel-*）
- 🧹 清除區域（fade-clear-*）可保留不透明條帶，用於固定標題或控制項
- 🔧 提供強制開啟（fade-always）和禁用（fade-none）淡出的工具
- 🌍 支援 RTL 閱讀方向，水平淡出會根據 dir 屬性自動調整
- ♿ 僅影響視覺，不影響內容移動、滾動行為或焦點順序
- 🖥️ 瀏覽器支援：Chrome/Edge 120+ 完整功能，Safari 26+ 完整，Firefox 為靜態淡出
- 📱 動態內容支援，提供 React 重新掛載和動畫重置模式

---

### [PikaPods - 即时开源应用托管](https://www.pikapods.com/?utm_source=tailwind-weekly&utm_medium=newsletter&utm_campaign=first&ref=tailwindweekly.com)

**原文标题**: [PikaPods - Instant Open Source App Hosting](https://www.pikapods.com/?utm_source=tailwind-weekly&utm_medium=newsletter&utm_campaign=first&ref=tailwindweekly.com)

### 概览摘要
PikaPods 提供开源应用托管服务，起价每月 1.80 美元，强调隐私保护、无追踪、简单管理，并支持开源开发者。

- 🤗 新用户可免费试用，并获得 5 美元欢迎信用额度
- 🛡️ 数据完全隐私，无广告、无追踪、无数据泄露
- 🌍 支持欧盟和美国服务器位置，可用自定义域名
- ⚡ 特色应用包括 n8n（工作流自动化）、Immich（照片管理）和 Actual（财务管理）
- 💻 提供简单界面，自动管理配置、数据库和更新
- 🔒 安全设计：隔离容器、加密连接和内置防火墙
- 🆓 无供应商锁定，可通过 SFTP 随时下载数据
- 💰 透明定价，仅按使用付费，起价 1.80 美元/月
- 🤝 支持开源开发者，分享 20% 收入给项目作者
- 📊 资源灵活：CPU、内存和存储可按需调整
- 🏢 由 Peakford 公司运营，拥有超过十年托管经验

---

### [Larasend](https://larasend.com/?ref=tailwindweekly.com)

**原文标题**: [Larasend](https://larasend.com/?ref=tailwindweekly.com)

概述总结：本文主要探讨了人工智能在医疗领域的应用与挑战，包括诊断辅助、药物研发和患者监护等方面，同时强调了数据隐私和伦理问题的重要性。

- 🩺 人工智能通过分析医学影像和病理数据，显著提升了疾病诊断的准确性和效率。
- 💊 在药物研发中，AI 加速了候选药物的筛选和临床试验设计，缩短了新药上市周期。
- 📊 智能监护系统利用可穿戴设备和传感器，实时监测患者健康状况，提前预警风险。
- 🔐 数据隐私保护成为关键议题，需确保患者信息在 AI 应用中的安全与合规使用。
- ⚖️ 伦理问题如算法偏见和决策透明度，要求建立严格的监管框架和公平性评估机制。

---

### [袖套 3 — 正在您的桌面上播放](https://replay.software/sleeve?ref=tailwindweekly.com)

**原文标题**: [Sleeve 3 — Now playing on your Desktop](https://replay.software/sleeve?ref=tailwindweekly.com)

概述摘要  
Sleeve 3 是一款专为 Mac 设计的音乐配件应用，支持 Apple Music、Spotify 和 Doppler，提供高度自定义的桌面音乐展示与控制体验，售价 5.99 美元，无订阅或内购，需 macOS 26 Tahoe。

- 🎵 支持 Apple Music、Spotify 和 Doppler 的音乐播放控制与展示  
- 🎨 提供主题功能，可创建、切换和分享自定义主题，双击即可安装  
- 🖼️ 自定义专辑封面：缩放、圆角、阴影、灯光和架子效果，或完全隐藏  
- ✍️ 自定义曲目信息：字体、粗细、大小、透明度、颜色和阴影  
- 🖥️ 界面自定义：布局、对齐、位置，可显示或隐藏播放控件和背景层  
- ⚙️ 设置选项：窗口层级（前置、后置或浮动）、Dock 显示、键盘快捷键  
- 🔗 集成 Last.fm 记录收听记录，支持在 Sleeve 中点赞 Spotify 曲目  
- ⌨️ 自定义键盘快捷键控制播放、点赞和音量，带 HUD 反馈  
- 🌗 支持浅色和深色模式，实时预览所有调整  
- 🎛️ 数十种设置精细控制外观：播放控件、曲目信息字体、系统外观样式等  
- 🖥️ 专为 macOS Tahoe 和 Apple Silicon 优化，使用 Swift 和 SwiftUI 构建  
- ☁️ 主题通过 iCloud 自动同步，支持高对比度和减少透明度  
- 💻 低 CPU 占用，支持 Mission Control 和全屏模式  
- 🛒 售价 5.99 美元，无订阅或内购，需 macOS 26 Tahoe  
- 📧 支持通过邮件联系，提供文档和购买查询工具，以及媒体资料包

---

### [shiply.now — 一键发布任何应用](https://shiply.now/?ref=tailwindweekly.com)

**原文标题**: [shiply.now — publish any app in one call](https://shiply.now/?ref=tailwindweekly.com)

Shiply.now 是一个无需账户、无需信用卡即可一键发布应用的平台。只需一个 HTTP 调用，即可将应用部署到真实 URL，包含后端、数据库、函数、邮件和自定义域名。定价透明，无隐藏费用。

- 🚀 **一键发布**：通过一个 HTTP 调用即可将应用发布到真实 URL，无需账户或设置。
- 💰 **透明定价**：固定价格 $0 / $8 / $24，无按使用量计费，无意外账单。
- 🤖 **AI 集成**：兼容 Claude Code、Cursor、Codex 等 AI 代理，可直接粘贴提示词发布。
- 🔗 **实时 URL**：发布后立即获得一个 24 小时有效的匿名 URL，可一键转为永久链接。
- 🎨 **模板丰富**：支持落地页、作品集、文档、启动页等多种模板，无需构建步骤。
- 🌐 **自定义域名**：可绑定自己的域名，通过 Cloudflare 自动配置 DNS。
- 🗄️ **数据库支持**：内置 Cloudflare D1 和 Neon Postgres 数据库。
- ⚡ **边缘函数**：支持 Workers Lite 动态端点和函数，无需服务器。
- 📧 **表单收集**：可捕获表单提交，并提供测试收件箱。
- 🔄 **所有权转移**：支持原子性所有权转移，可通过 Stripe Connect 收款。
- 🔒 **隐私控制**：默认公开但 URL 随机，可添加密码或限制特定用户访问。
- 📊 **无隐藏费用**：固定月费，不会因流量激增而产生额外费用。
- 🖼️ **自动推广**：每个发布站点都会生成 Open Graph 预览卡片，免费站点带有“Published with shiply”标记。

---

