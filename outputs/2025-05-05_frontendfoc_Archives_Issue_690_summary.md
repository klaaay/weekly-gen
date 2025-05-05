### [前端聚焦第 690 期：2025 年 4 月 30 日](https://frontendfoc.us/issues/690)

**原文标题**: [Frontend Focus Issue 690: April 30, 2025](https://frontendfoc.us/issues/690)

概述总结  
本期内容涵盖了前端开发的最新动态、工具推荐和技术文章，包括 Google Chrome 可能被出售的讨论、新的开发工具 Tonkotsu、CSS 排版技巧、3D 效果实现，以及 Web 历史的回顾等。  

- 🚀 **Google Chrome 的未来** — DHH 认为强制 Google 出售 Chrome 可能对 Web 生态造成负面影响。  
- 🍜 **Tonkotsu IDE** — 一款面向 JS 和 TS 开发者的自然语言 IDE，提供免费早期访问。  
- 📏 **CSS 排版新单位** — Jen Simmons 介绍了`lh`和`rlh`单位如何简化垂直排版。  
- 🎚️ **3D 翻页效果** — Jhey Tompkins 分享了如何在 Web 上实现复古的分页翻转效果。  
- ⚡️ **Web 历史小知识** — 1993 年万维网软件进入公共领域，1989 年 Web 概念诞生。  
- 🦊 **Firefox 新功能** — 新增标签分组和支持 View Transition API。  
- 🍪 **Brave 浏览器更新** — 社区推动屏蔽 Cookie 同意弹窗。  
- 📑 **HTML 包含问题** — Chris Coyier 探讨了 HTML 原生无法实现包含功能的难题。  
- ❌ **友好的错误提示** — Amy Hupe 分享了如何设计帮助用户解决问题的错误信息。  
- 🎨 **Canvas 元素利弊** — Heydon Pickering 分析了 Canvas 的可用性和性能权衡。  
- 🦉 **CSS 猫头鹰选择器** — Zoran Jambor 解析了`* + *`选择器的用途和替代方案。  
- 🔗 **CSS 锚点定位** — Geoff Graham 介绍了如何用锚点定位简化重叠元素布局。  
- 💬 **特殊字符与用户体验** — Stéphanie Walter 讨论了编码问题如何影响用户体验。  
- 🤖 **AI 编程的隐形成本** — Matheus Lima 反思 AI 编码对开发乐趣的冲击。  
- 🌀 **CSS Blob 效果** — Temani Afif 展示了仅用 CSS 实现的可交互 Blob 形状。  
- 🛠️ **工具推荐** — 包括响应式字体生成器、CSS 可视化编辑器、表单构建器和 Storybook 9 测试版等。

---

### [别让谷歌出售 Chrome](https://world.hey.com/dhh/don-t-make-google-sell-chrome-93cefbc6)

**原文标题**: [Don't make Google sell Chrome](https://world.hey.com/dhh/don-t-make-google-sell-chrome-93cefbc6)

概述总结  
David Heinemeier Hansson 认为，尽管谷歌在广告市场存在垄断行为，但强制其出售 Chrome 浏览器将对互联网生态造成巨大伤害。Chrome 的成功源于其技术优势和市场选择，而非垄断手段。谷歌对网络的持续投入推动了网络技术的发展，而削弱 Chrome 可能导致网络平台在与 iOS 应用商店等封闭平台的竞争中处于劣势。  

- 🌐 **Chrome 的成功是市场选择的结果**：Chrome 凭借技术实力和投资赢得了浏览器战争，并非通过垄断手段。  
- 🔍 **谷歌依赖健康的网络生态**：谷歌的商业模式依赖于可搜索、广告支持和 AI 驱动的网络，因此其推动网络发展是出于经济利益。  
- 🦍 **网络需要强大的支持者**：谷歌作为网络技术的推动者，对抗了苹果等封闭平台的竞争，维护了网络的开放性和应用能力。  
- ⚙️ **持续的技术投入至关重要**：Chrome 推动了多项网络技术进步（如嵌套 CSS、Web Push 等），若投资减少，网络可能停滞。  
- 💰 **财富与短期价值的区别**：Chrome 的长期价值在于持续投入，强制出售可能导致其技术优势迅速消失。  
- ⚖️ **应惩罚广告垄断，但保护 Chrome**：谷歌的广告垄断行为应受制裁，但不应以牺牲网络技术发展为代价。  

关于作者：  
- 🚀 **David Heinemeier Hansson**：Basecamp 和 HEY 的联合创始人兼 CTO，Ruby on Rails 的创造者，作家和赛车手，投资丹麦初创公司。

---

### [使用行高单位优化你的排版 | WebKit](https://webkit.org/blog/16831/line-height-units/)

**原文标题**: [  Polishing your typography with line height units | WebKit](https://webkit.org/blog/16831/line-height-units/)

网页排版中通过行高单位（lh）实现精细化设计的新工具，显著提升视觉效果与开发效率。

- 🌟 CSS 新增 lh 和 rlh 单位（2023 年全浏览器支持），1lh 代表当前文本行高，rlh 则基于根元素行高  
- ✂️ 传统 1em 段落间距（左图）vs 1lh 间距（右图）对比：后者更精致，完美契合文本垂直节奏  
- 📐 应用场景：边距 (margin-block: 1lh)、内边距、间隙等布局尺寸，实现与文本流自然对齐  
- 🛠️ 渐进增强方案：同时声明 1em 和 1lh，老旧浏览器自动回退到 em 单位  
- 🌐 94% 浏览器兼容性，可通过 Demo 即时体验效果  
- 🎨 结合近年十余项 CSS 新特性，可轻松实现专业级网页排版  
- 💬 作者 Jen Simmons 邀请在 Bluesky/Mastodon 平台交流使用反馈

---

### [《用 JavaScript 实现时间旅行》- Jhey ʕ•ᴥ•ʔ](https://craftofui.substack.com/p/time-travel-with-javascript)

**原文标题**: [Time Travel with JavaScript - by Jhey ʕ•ᴥ•ʔ](https://craftofui.substack.com/p/time-travel-with-javascript)

文章概述：本文介绍了如何使用 JavaScript 和 GSAP 动画库创建一个类似 Vestaboard 的 3D 翻页效果显示板，通过时间轴控制和动画技巧实现字符的动态切换。

- 🚀 使用 JavaScript 和 GSAP 实现 3D 翻页效果，模拟 Vestaboard 的显示效果。
- 🛠️ 通过分解任务，先创建单个翻页元素，再组合成完整的显示板。
- ✂️ 使用 clip-path 和 CSS 样式对翻页元素进行裁剪和旋转，实现动态效果。
- 🔄 利用 GSAP 的时间轴控制和动画 API，实现字符的无缝切换和循环播放。
- ⏱️ 通过控制时间轴的位置（scrubbing）来实现字符的动态切换，而非反向播放动画。
- 📜 支持自定义字符序列，包括字母、数字和表情符号，并可扩展为多行显示。
- ⚙️ 提供了基于 Web Animation API (WAAPI) 的无依赖版本实现，但功能相对简化。
- 📢 作者预告将推出相关课程，并邀请读者加入等待列表。

---

### [翻页式显示器 - 维基百科](https://en.wikipedia.org/wiki/Split-flap_display)

**原文标题**: [Split-flap display - Wikipedia](https://en.wikipedia.org/wiki/Split-flap_display)

翻页显示装置是一种机电数字显示设备，用于展示可变的字母数字文本和固定图形。以下是关键点：

- 🚄 主要用于机场和火车站的公共交通时刻表（1960 年代至 1990 年代），又称 Solari 板（意大利制造商）或 Pragotron（中欧制造商）。  
- ⏰ 消费类数字钟表（翻页钟）曾广泛采用此技术。  
- 🎨 每个字符/图形位置由多个印刷好的 flaps 组成，通过翻转显示内容，大 flaps 可展示完整单词，小 flaps 显示单个字符。  
- 💡 优点：高可见性、广视角、静态时低功耗、更新时金属声提示。  
- 🔄 替代方案：翻转点阵屏和 LED 屏（可数字化更新但可读性较低）。  
- 📺 1970 年代游戏节目常用作计分板（如《Family Feud》早期版本），艺术领域也有应用（如 Juan Fontanive 作品）。  
- 🖼️ 非信息用途：专辑封面（如 The Enemy 乐队）和当代艺术装置。  
- 📸 知名案例：布拉格火车站、巴黎北站等地的 departure boards。

---

### [获取失败](https://frontendfoc.us/link/168687/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/168687/web)

无法总结：获取内容失败，状态码 403。

---

### [万维网软件公开发布 - CERN 文献服务器](https://cds.cern.ch/record/1164399/)

**原文标题**: [Software release of WWW into public domain - CERN Document Server](https://cds.cern.ch/record/1164399/)

1993 年 4 月 30 日，CERN 正式将万维网（WWW）软件发布至公共领域，标志着互联网技术迈向全球开放的关键一步。

- 🌐 1993 年 4 月 30 日，CERN 将万维网技术公开发布，推动全球互联网发展。  
- 📄 文档编号 CERN-IT-9304003，包含软件进入公共域的法律声明。  
- 🔍 可通过 CERN 文档服务器访问原始文件（含 2 张图片及多尺寸版本）。  
- 🖥️ 关键词：公共领域（public domain）、网络（web）、计算机（computer）。  
- ⚠️ 使用条款注明版权归 CERN 所有（1993-2025），但允许公共访问。  
- 📥 支持多种格式下载（JPG、BibTeX 等）及嵌入代码供外部调用。  
- 🌍 页面提供多语言选项，凸显 CERN 的国际协作属性。

---

### [万维网历史 - 维基百科](https://en.wikipedia.org/wiki/History_of_the_World_Wide_Web)

**原文标题**: [History of the World Wide Web - Wikipedia](https://en.wikipedia.org/wiki/History_of_the_World_Wide_Web)

万维网的历史概述

- 🌍 1989 年：蒂姆·伯纳斯 - 李在欧洲核子研究中心（CERN）提出万维网的构想，旨在通过超文本系统共享信息。
- 🖥️ 1990 年：伯纳斯 - 李开发了第一个网页浏览器和服务器，并创建了 HTML、HTTP 和 URL 等核心技术。
- 🚀 1991 年：万维网首次向公众开放，CERN 发布了第一个网站。
- 🌐 1993 年：NCSA Mosaic 浏览器的发布使图形化网页浏览成为可能，推动了互联网的普及。
- 💻 1994 年：网景公司成立，发布了 Netscape Navigator 浏览器，引发了第一次浏览器大战。
- 🔄 1995 年：微软推出 Internet Explorer，并与 Windows 捆绑，逐渐占据浏览器市场主导地位。
- 📈 1990 年代末：互联网商业化加速，电子商务兴起，如亚马逊和 eBay 的成立。
- 💥 2000 年代初：互联网泡沫破裂，许多互联网公司倒闭。
- 🌟 2004 年：Web 2.0 概念兴起，强调用户生成内容和社交互动，如 Facebook 和 YouTube 的出现。
- 📱 2010 年代：移动互联网和智能手机的普及，推动了响应式网页设计的发展。
- 🔗 2010 年后：Web 3.0 和语义网的概念提出，旨在实现更智能的数据互联和去中心化网络。
- 🛡️ 安全与隐私：随着网络的发展，网络安全和隐私保护成为重要议题。

---

### [获取失败](https://frontendfoc.us/link/168624/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/168624/web)

无法总结：获取内容失败，状态码 403。

---

### [Firefox Nightly 140.0a1：查看所有新功能、更新与修复](https://www.mozilla.org/en-US/firefox/140.0a1/releasenotes/#note-790833)

**原文标题**: [Firefox Nightly 140.0a1, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/140.0a1/releasenotes/#note-790833)

Firefox Nightly 最新版本 140.0a1 于 2025 年 4 月 28 日发布，每日更新并持续优化功能，适合开发者与测试者参与反馈。  

- 🚀 **新功能**：Firefox 139 起，Nightly 版新增智能标签组功能，自动归类语义相似的标签页并命名。  
- 🛡️ **隐私增强**：Firefox 140 试验性引入反追踪隔离技术，防止恶意网站通过插件资源进行指纹识别。  
- 💻 **开发者支持**：  
  - Linux/macOS版支持WebCodecs的H265解码（Firefox 138/137起）。  
  - 新增`PerformanceEventTiming.interactionId`支持，优化交互性能指标（INP）。  
  - 移除非标准事件`afterscriptexecute`和`beforescriptexecute`。  
  - 支持视图过渡 API（View Transition API）。  
  - 全平台新增`aria-keyshortcuts`无障碍属性支持。  
- ⚠️ **系统兼容性**：  
  - 不再支持 Windows 8.1 及以下、macOS 10.14 及以下系统，建议转用 Firefox ESR 版本。  
  - 提供多平台（Windows/macOS/Linux）32/64 位及 ARM 架构下载选项。  
- 📢 **社区参与**：鼓励用户通过 Bugzilla 提交问题、加入 Matrix 聊天室反馈，或关注 Nightly 的 Bluesky/Mastodon 账号及博客。  
- ℹ️ **其他资源**：包含完整版本变更日志、新闻稿及 Firefox 支持计划详情。  

（注：部分功能可能不会进入正式版。）

---

### [视图过渡 API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)

**原文标题**: [View Transition API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)

View Transition API 提供了一种在不同网站视图之间创建动画过渡的机制，适用于单页应用（SPA）和多页应用（MPA）。

- 🌟 **功能概述**：View Transition API 简化了视图切换和过渡动画的实现，适用于 SPA 和 MPA。
- 🧠 **设计目的**：减少用户认知负荷，保持上下文连贯性，并降低加载延迟感。
- 🛠 **历史难点**：传统实现需大量 CSS 和 JavaScript，且存在可访问性问题（如焦点混乱）。
- 📜 **接口与事件**：
  - `ViewTransition`：表示视图过渡，提供状态回调（如动画开始/结束）。
  - `startViewTransition()`：启动 SPA 视图过渡。
  - `pagereveal` 和 `pageswap` 事件：用于跨文档导航时操作过渡。
- 🏗 **HTML/CSS 扩展**：
  - `<link rel="expect">`：标识关键内容以确保过渡一致性。
  - `@view-transition` 和 `view-transition-name`：控制过渡行为。
  - 伪元素（如 `::view-transition-old`）：管理过渡中的旧视图和新视图。
- 🎨 **示例应用**：
  - 图库过渡（SPA）、页面滑动效果（MPA）、视频播放器动画等。
- 📚 **规范与兼容性**：基于 CSS View Transitions Module Level 1，需检查浏览器支持情况。
- 🔍 **延伸阅读**：开发者资源（如 Chrome 官方教程）和社区文章。

---

### [Brave 的 Cookiecrumbler 工具借助社区力量拦截 Cookie 提示](https://www.bleepingcomputer.com/news/security/braves-cookiecrumbler-tool-taps-community-to-help-block-cookie-notices/)

**原文标题**: [Brave's Cookiecrumbler tool taps community to help block cookie notices](https://www.bleepingcomputer.com/news/security/braves-cookiecrumbler-tool-taps-community-to-help-block-cookie-notices/)

Brave 推出开源工具 Cookiecrumbler，利用 AI 和社区审核机制智能拦截 Cookie 弹窗，避免破坏网站功能，同时严格保护用户隐私。

- 🌐 Brave 开源新工具 Cookiecrumbler，结合 AI 检测与人工审核机制，精准拦截 Cookie 同意弹窗  
- 🛡️ 自 2022 年起默认拦截所有网站 Cookie 横幅，但发现过度拦截会导致网站功能异常（如支付流程中断/页面空白）  
- 🤖 工作流程：区域代理爬取热门网站→Puppeteer 检测弹窗→LLM 分类生成解决方案→GitHub 社区复核  
- 🔒 隐私保护设计：后端运行不涉及用户数据/仅用代理模拟浏览/暂未集成至浏览器  
- 📂 开发者友好：开源项目可供隐私工具开发者、网站审计人员等直接调用或改进过滤规则  
- ⏳ 未来计划：通过完整隐私审查后才会整合至 Brave 浏览器

---

### [探寻答案：为何仅靠 HTML 无法实现文件包含？——Frontend Masters 博客](https://frontendmasters.com/blog/seeking-an-answer-why-cant-html-alone-do-includes/)

**原文标题**: [Seeking an Answer: Why can’t HTML alone do includes? – Frontend Masters Blog](https://frontendmasters.com/blog/seeking-an-answer-why-cant-html-alone-do-includes/)

文章探讨了为何 HTML 本身不支持直接包含（include）其他 HTML 文件的功能，尽管这在网页开发中是一个普遍需求。

- 🔍 **问题核心**：开发者需要在多个页面中重复使用相同的 HTML 片段（如页眉、页脚），但 HTML 缺乏原生支持“包含”功能，导致必须依赖其他工具或技术。
- 🛠️ **现有解决方案**：  
  - 使用 JavaScript 动态加载和插入 HTML。  
  - 服务器端包含（如 SSI、PHP）。  
  - 静态网站生成器（如 Jekyll、Eleventy）。  
  - Web Components 或`<iframe>`（但存在性能和可访问性问题）。  
  - 编辑器全局替换功能。
- ❓ **为何 HTML 不原生支持？**  
  - 可能涉及性能问题（如预加载扫描器冲突）。  
  - 异步加载导致布局抖动或渲染问题。  
  - 安全性或跨域限制。  
  - 嵌套或循环包含的复杂性。  
  - 缺乏明确的标准化提案或优先级。
- 🌐 **历史与标准争议**：  
  - HTML5 后标准演进缓慢，新标签功能有限。  
  - 开发者需求与浏览器厂商关注点不匹配（如更倾向于 Web Components 而非原生 HTML 功能）。  
  - 过去尝试（如 HTML Imports）因浏览器支持不足被废弃。
- 💡 **开发者观点**：  
  - 部分认为 HTML 应保持“无逻辑”的静态标记语言特性。  
  - 另一部分呼吁原生支持，以简化小型项目开发流程。  
- 🔮 **替代方案推荐**：  
  - HTMX 等轻量库接近纯 HTML 解决方案。  
  - 服务器端预处理（如 Go 模板、PHP）仍是主流选择。  

文章最终未得出明确结论，但引发了对 HTML 设计哲学、标准化流程及开发者实际需求的深入讨论。

---

### [如何编写真正帮助用户而非令其沮丧的错误提示信息 - Piccalilli](https://piccalil.li/blog/how-to-write-error-messages-that-actually-help-users-rather-than-frustrate-them/)

**原文标题**: [
  How to write error messages that actually help users rather than frustrate them - Piccalilli
](https://piccalil.li/blog/how-to-write-error-messages-that-actually-help-users-rather-than-frustrate-them/)

如何编写真正帮助用户而非令其沮丧的错误提示信息  
2025 年 4 月 17 日  
作者：Amy Hupe  

- 🔍 **忽视错误处理的现状**：用户体验设计中常忽略错误路径，导致用户遇到无意义的代码或死胡同，缺乏标准化解决方案。  
- 📝 **错误类型分类**：需提前规划表单错误、验证错误、404/500 页面、无搜索结果、断网等场景，避免意外错误出现。  
- 👥 **人性化表达**：避免机械语言（如“发生错误”），改用口语化指导（如“请输入 6 位验证码”），参考 Monzo 的“请用手机操作”示例。  
- 🚫 **避免过度俏皮**：错误时用户需要解决方案而非幽默（如“小糊涂蛋”可能激怒用户），需优先清晰与共情。  
- 🎯 **主动语态明确责任**：用“我们无法处理您的申请”替代被动表述，明确问题与操作步骤。  
- 🔄 **提供明确后续行动**：可修复错误（如“检查卡片信息”）与不可修复错误（如“稍后重试或联系客服”）均需指引。  
- ♻️ **统一错误模式**：建立可复用的错误文案模板（如 GOV.UK 的字段缺失提示），提升一致性与效率。  
- 💡 **错误处理的价值**：妥善处理错误能赢得用户信任，体现对其时间与体验的尊重。  

作者 Amy Hupe 是英国设计系统与内容设计顾问，曾服务于 GOV.UK 等机构。

---

### [画布元素：HeydonWorks](https://heydonworks.com/article/the-canvas-element/)

**原文标题**: [The canvas element: HeydonWorks](https://heydonworks.com/article/the-canvas-element/)

概述总结  
本文探讨了 HTML 中的`<canvas>`元素，分析了其设计初衷、功能特点、适用场景以及与 SVG 的对比，同时强调了文本优先的设计理念和可访问性的重要性。

- 🖥️ `<canvas>`元素最初由苹果开发，用于“Dashboard widgets”，后被 HTML5 标准化，作为替换元素嵌入内容。  
- 📜 作者强调“文本优先”设计理念，认为网页应以文本为基础，HTML 是格式化文本的金属语言。  
- 🎨 `<canvas>`通过脚本提供分辨率相关的位图画布，主要用于动态、脚本化的 2D/3D 图形渲染（如 WebGL）。  
- ⚠️ 使用`<canvas>`渲染文本存在可访问性问题（如 WCAG 1.4.5 准则），且需依赖 JavaScript，不推荐替代常规文本。  
- ♿ 规范建议：若存在更合适的元素（如`<div>`或 SVG），应避免使用`<canvas>`，因其可访问性支持有限。  
- 🔄 动态`<canvas`>需开发者手动维护与后备内容的交互对等性（如`drawFocusIfNeeded()`方法），实现复杂。  
- 🆚 与 SVG 对比：SVG 基于矢量、分辨率无关且支持无障碍，适合静态图形；`<canvas`>性能更优，适合高频动画（如模拟 snowfall）。  
- ❄️ 讽刺性用例：`<canvas`>最适合模拟雪花飘落——尽管网上已有大量类似教程。  
- 👕 文末附带作者个人链接（打赏和服装品牌）及其他 HTML 元素列表。

---

### [引用元素：HeydonWorks](https://heydonworks.com/article/the-cite-element/)

**原文标题**: [The cite element: HeydonWorks](https://heydonworks.com/article/the-cite-element/)

这篇文章讨论了 HTML5 中`<cite>`元素的用法及其历史演变，并夹杂了作者个人的创作轶事和幽默吐槽。

- 📜 作者曾创作一部关于 Tailwind CSS 的讽刺小说《The Wind Beneath His Tail》，后因担心网络审查删除相关内容，仅通过谷歌图片缓存恢复片段。  
- 🖋️ HTML5 规定`<cite>`标签仅用于标注作品标题（如书名），而 HTML4 允许标注作者名等更广泛内容，这一改动曾引发争议。  
- 🔄 2014 年 WHATWG 试图放宽限制允许标注说话者，但 W3C 规范仍坚持仅限作品标题，且两者规范链接存在冲突。  
- 🤷 作者建议不必过度纠结`<cite>`内容，因其语义对屏幕阅读器和 SEO 影响极小，并吐槽元素名应改为`<citation>`更合理。  
- 😅 穿插大量冷幽默：如小说标题被解读为"放屁"，以及用"牛排砸桌"等荒诞情节讽刺 CSS 代码臃肿问题。  
- 💸 文末附作者打赏链接和服装品牌广告，延续其戏谑风格。

---

### [什么是 CSS 猫头鹰选择器（* + *）？ - YouTube](https://www.youtube.com/watch?v=0O0ssm70g1g)

**原文标题**: [What is CSS Owl Selector (* + *)? - YouTube](https://www.youtube.com/watch?v=0O0ssm70g1g)

该页面列出了 YouTube 的相关信息和链接，包括关于平台、联系方式、创作者支持、广告合作、开发者资源以及政策条款等内容。

- 📢 Press - 媒体相关资讯  
- ©️ Copyright - 版权信息  
- 📩 Contact us - 联系我们  
- � Creators - 创作者支持  
- 💼 Advertise - 广告合作  
- 👩💻 Developers - 开发者资源  
- 📜 Terms - 使用条款  
- 🔒 Privacy - 隐私政策  
- ⚖️ Policy & Safety - 政策与安全  
- 🔧 How YouTube works - YouTube 运作机制  
- 🆕 Test new features - 测试新功能  
- © 2025 Google LLC - 版权归属谷歌公司

---

### [如何将 Clerk 投入生产环境](https://clerk.com/blog/how-to-take-clerk-to-production?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=clerk-prod-fef&utm_content=04-30-25&dub_id=2RfU57OWsCDiC0C5)

**原文标题**: [How to take Clerk to Production](https://clerk.com/blog/how-to-take-clerk-to-production?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=clerk-prod-fef&utm_content=04-30-25&dub_id=2RfU57OWsCDiC0C5)

概述  
本文详细介绍了如何将 Clerk 应用从开发环境迁移到生产环境，包括设置自定义域名、配置 DNS 记录、更新 API 密钥以及注册 OAuth 凭证等关键步骤。

- 🔄 **开发与生产环境的区别**  
  - 开发实例：使用共享 OAuth 凭证、允许 HTTP、快速启动  
  - 生产实例：强制 HTTPS、专用凭证、需自定义域名和 DNS 配置  

- 🌐 **设置自定义域名**  
  - 确保用户登录域名的安全性，用于身份验证  

- 🛠️ **创建生产实例**  
  - 在 Clerk 仪表盘中切换至生产环境，选择克隆或新建实例  
  - 重新配置未自动迁移的集成（如 SSO）  

- 📡 **配置 DNS 记录**  
  - 添加 Clerk 提供的 DNS 条目，验证域名所有权和电子邮件认证  

- 🔑 **更新 API 密钥**  
  - 替换开发环境的`pk_live_`和`sk_live_`密钥至生产环境  

- 🔗 **配置社交登录**  
  - 在生产环境中为每个身份提供商（如 Google）注册应用并设置回调 URI  

- 🚀 **快速上线步骤**  
  1. 获取自定义域名  
  2. 创建生产实例  
  3. 设置 DNS 记录  
  4. 更新生产 API 密钥  
  5. 注册并配置 OAuth 凭证  
  6. 重新部署应用

---

### [锚点定位不在乎源顺序 | CSS-Tricks](https://css-tricks.com/anchor-positioning-just-dont-care-about-source-order/)

**原文标题**: [Anchor Positioning Just Don't Care About Source Order | CSS-Tricks](https://css-tricks.com/anchor-positioning-just-dont-care-about-source-order/)

文章讨论了 CSS 中的锚点定位（Anchor Positioning）技术，该技术允许元素定位不受 HTML 源代码顺序的限制，从而更灵活地控制布局。

- 🎯 锚点定位不依赖 HTML 源代码顺序，使元素定位更灵活。  
- 🏗️ 传统方法需通过父元素相对定位和子元素绝对定位实现覆盖效果。  
- 🔗 使用`anchor-name`定义锚点元素，`position-anchor`连接子元素到锚点。  
- 📏 `position-area`和`anchor-size()`可精确控制子元素覆盖锚点元素的位置和尺寸。  
- 🚀 锚点定位简化了布局实现，分离了内容与表现，提升了开发效率。  
- 🌐 目前仅最新版 Chrome 默认支持该特性。

---

### [你好，我叫 Stéphanie——关于“特殊字符”、包容性设计与用户体验的探讨](https://stephaniewalter.design/blog/hello-my-name-is-stephanie-talk-encoding-special-characters-issues-poor-user-experience/)

**原文标题**: [Hello my name is St�phanie - a talk on "special characters", inclusive design and user experience](https://stephaniewalter.design/blog/hello-my-name-is-stephanie-talk-encoding-special-characters-issues-poor-user-experience/)

概述  
本文探讨了特殊字符在网页设计中的重要性，以及因编码和数据库问题导致的用户体验问题。作者通过自身经历，展示了这些问题的广泛影响，并呼吁更包容的设计。

- 🌍 **全球化与多样性**：在全球化背景下，支持各种字符（如特殊符号、非拉丁字母）对用户体验至关重要。  
- 😞 **表单挑战**：许多网站禁止特殊字符，导致用户被迫错误拼写自己的名字，影响体验。  
- 🖥️ **字体与显示问题**：字体缺失或子集化可能导致特殊字符无法正确显示（如显示为▯或乱码）。  
- 🔠 **编码错误**：数据库或打印时的编码问题会生成乱码（如 StÃ©phanie），甚至影响实际生活（如快递、签证）。  
- 📦 **现实影响**：编码错误可能导致包裹无法送达、登机牌与护照不匹配等严重后果。  
- ✈️ **行政障碍**：签证或官方文件中名字不匹配可能被拒绝入境，凸显系统包容性的缺失。  
- ♿ **包容性设计**：应遵循 Postel 法则，接受多样化的输入，而非为了方便限制字符。  
- 📚 **延伸阅读**：推荐了关于姓名多样性、程序员对名字的误解等相关文章。  

作者强调，问题不仅关乎“é”，而是关于让网络成为对所有人更友好的地方。

---

### [AI 编码的隐性代价——糟糕的软件](https://terriblesoftware.org/2025/04/23/the-hidden-cost-of-ai-coding/)

**原文标题**: [The Hidden Cost of AI Coding – Terrible Software](https://terriblesoftware.org/2025/04/23/the-hidden-cost-of-ai-coding/)

AI 编码的隐性成本：效率提升背后可能牺牲了编程的乐趣与心流体验，作者担忧过度依赖 AI 工具会剥夺开发者从创造性解决问题中获得的深层满足感。

- 🤔 作者最初积极拥抱 AI 工具，但逐渐意识到其可能消解编程的快乐本质  
- 🎧 传统编程中的"心流"状态（完全沉浸、时间感消失）是职业幸福感的核心来源  
- ⚡ 心理学家米哈里提出的"心流"理论：挑战与技能平衡时产生的创造性愉悦  
- 🤖 当前 AI 辅助编程更像"策展"——描述需求、评估结果，而非亲手构建  
- 📈 承认 AI 提升效率，但质疑长期可能造成开发者与工艺的疏离  
- ❓ 灵魂拷问：当代码生成取代亲手编程，我们是否也外包了成就感？  
- 🌱 可能的出路：在系统设计等更高层次或 AI 无法替代的领域寻找新满足  
- 💡 呼吁刻意保留手工编码空间——不为效率，只为守护职业初心

---

### [悬停效果的斑点形状](https://css-tip.com/blob-hover/)

**原文标题**: [Blob shape with hover effect](https://css-tip.com/blob-hover/)

概述：介绍了一种使用 CSS 新特性`shape()`创建动态 Blob 形状的方法，并提供了代码生成器和示例，同时提到目前仅支持 Chrome 浏览器。

- 🌟 使用 CSS 新特性`shape()`创建独特的 Blob 形状  
- � 提供在线代码生成器方便快速获取代码  
- 🎭 通过过渡效果实现炫酷的悬停动画（形状切换）  
- ⚠️ 目前仅兼容 Chrome 浏览器  
- 📌 附两个 CodePen 实战示例（作者 Temani Afif）  
- 🔗 文末推荐更多 CSS 技巧：圆角箭头盒子（4/22）和圆角多边形生成（4/17）

---

### [Blob 形状 CSS 生成器](https://css-generators.com/blob/)

**原文标题**: [CSS Generator for Blob shapes](https://css-generators.com/blob/)

这段内容主要介绍了一个 CSS 代码片段，用于创建一个特定形状的 blob 元素，并提供了复制代码和项目支持的选项。

- 🔍 **Granularity** - 提到了代码的精细程度或细节处理。  
- 📏 **Depth** - 可能指形状的深度或复杂程度。  
- 🔄 **Rotation** - 可能涉及形状的旋转或动态效果。  
- 🔵 **Shape ID** - 定义了特定形状的标识或生成方式。  
- 🛠️ **Generate** - 提供了生成形状的 CSS 代码。  
- 📋 **Copy the CSS** - 可直接复制提供的 CSS 代码。  
- ❤️ **Support This Project** - 呼吁支持该项目。

---

### [网页设计的未来：100 年后我们还能认出它吗？](https://webdesignerdepot.com/the-future-of-web-design-will-we-even-recognize-it-in-100-years/)

**原文标题**: [The Future of Web Design: Will We Even Recognize It in 100 Years?](https://webdesignerdepot.com/the-future-of-web-design-will-we-even-recognize-it-in-100-years/)

1  
设计师的 2025 年 4 月新工具  

- 🎨 2025 年 4 月推出了一系列令人兴奋的新设计工具  
- 🛠️ 这些工具旨在提升设计师的工作效率和创造力  
- 📅 Carrie Cousins 介绍了这些工具的最新动态  
- 💡 包括创新功能和用户友好的界面设计  
- 🔍 适合各类设计师，从平面到用户体验设计

---

### [获取失败](https://frontendfoc.us/link/168637/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/168637/web)

无法总结：获取内容失败，状态码 403。

---

### [职业发展 | Brilliant](https://brilliant.org/careers/)

**原文标题**: [Careers | Brilliant](https://brilliant.org/careers/)

Brilliant 致力于培养全球问题解决者，专注于成人数学、数据科学及 AI 等领域的互动学习，拥有健康商业模式和多元文化团队，提供远程全职岗位并鼓励多样性申请。

- 🌟 使命与愿景：打造全球问题解决者，专注成人数学/数据/CS/AI 的互动学习  
- � 团队特质：100+ 成员，高影响力低自负，重视卓越/冒险/坦诚  
- 🚀 业务现状：付费用户数十万，盈利稳健，估值务实  
- 🌍 工作文化：核心协作时段（太平洋 10am-3pm），季度线下聚会，倡导自主与高强度创新  
- 🧩 人才画像：多背景通才，爱好独特（如密码学竞赛/VR 开发/分子生物研究）  
- ✨ 开放岗位：远程工程师（Android/交互软件等）、内容制作人  
- 📧 申请方式：支持非公开岗位投递，鼓励弱势群体申请 jobs@brilliant.org  
- 🔍 特色课程：聚焦实用技能（如统计/神经网络），剔除抽象理论

---

### [响应式排版比例生成器 - DK Web 解决方案](https://dkwebsolutions.co.uk/our-tools/responsive-typographic-scale-generator)

**原文标题**: [Responsive Typographic Scale Generator - DK Web Solutions](https://dkwebsolutions.co.uk/our-tools/responsive-typographic-scale-generator)

这是一个关于响应式排版比例生成器的工具介绍，帮助设计师和开发者创建具有视觉层次和响应式字体大小的网站。

- 🎨 工具提供多种排版比例选择，如小调二度、大调二度、小调三度等，适用于不同设计需求。
- 📱 用户可自定义最小和最大屏幕宽度、基础字体大小（PX 或 REM 单位）。
- ✨ 生成器展示六种标题和一种正文文本的字体大小，适用于移动端和桌面端。
- 💻 提供标准 CSS 和 SASS/SCSS 代码，可直接复制使用，支持响应式设计。
- 🔧 如需调整，可使用 CSS Clamp Generator 自定义字体大小范围。
- ❓ 常见问题解答包括排版比例的作用、不同比例的适用场景、流体排版和 CSS clamp 的解释。
- 📚 排版比例适用于多种场景，如博客、新闻网站、海报、广告和高档时尚网站。
- 📱 流体排版确保字体大小根据屏幕尺寸平滑过渡，优化用户体验。
- 📝 提供联系方式，欢迎用户提出新工具建议或改进意见。

---

### [CSS 编辑器 - getButterfly](https://getbutterfly.com/css-editor/)

**原文标题**: [CSS Editor - getButterfly](https://getbutterfly.com/css-editor/)

这是一个 CSS 编辑器的 Beta 版本界面，提供了丰富的样式编辑功能，支持 2D/3D 效果、背景、边框、滤镜等设置，目前处于实验阶段，未来将增加更多功能。

- 🐸 CSS 编辑工具处于 Beta 测试阶段  
- 🎨 支持背景设置（纯色/渐变/图片）和混合模式  
- 📦 提供 2D 和 3D 盒子模型编辑功能  
- 🌈 包含边框样式、圆角、阴影等装饰属性  
- 🔍 具有高级滤镜和背景滤镜效果  
- 🌀 支持 2D/3D 变形转换功能  
- ⚠️ 当前为 0.0.5 版本，暂不支持预设保存等特性  
- 🛠️ 开发者标注了即将推出的自定义预设等功能  
- 📝 底部留有"Hello World!"测试文本区域  
- ℹ️ 由 Ciprian Popescu 开发，含版本更新日志

---

### [SurveyJS - 用于调查与表单的 JavaScript 库](https://surveyjs.io?utm_source=frontend_focus&utm_medium=referral)

**原文标题**: [SurveyJS - JavaScript Libraries for Surveys and Forms](https://surveyjs.io?utm_source=frontend_focus&utm_medium=referral)

开源 JavaScript 表单构建库概览

- 📚 **表单库** - 免费开源的 MIT 许可 JavaScript 库，可渲染动态 JSON 表单并收集响应。
- 🛠️ **调查创建器** - 自托管拖放表单构建器，实时生成 JSON 表单定义，支持商业用途需开发者许可证。
- 📊 **仪表盘** - 提供交互式可定制图表和表格，简化调查数据分析，需商业开发者许可证。
- 🖨️ **PDF 生成器** - 将 SurveyJS 表单渲染为 PDF 文件，支持无限数量表单保存为可编辑或只读 PDF，需商业许可证。
- 🔒 **数据安全** - 自托管解决方案，确保敏感数据完全掌控，避免第三方 SaaS 平台依赖。
- 🎨 **完全定制** - 支持 CSS 主题编辑器，可融入品牌标识和设计语言。
- 🔗 **集成支持** - 兼容 React.js、Angular、Vue.js、Knockout 和 jQuery，后端自由选择。
- 💼 **永久许可** - 商业用途需一次性购买永久开发者许可证，无版税限制。
- 🛡️ **专业技术支持** - 提供技术专家指导和详尽开发者文档。

- 🏥 **医疗保健** - 自动化医疗数据收集，设计无限医疗表单，安全收集敏感患者数据。
- 🛒 **电子商务** - 集成调查工具，创建客户满意度调查和产品反馈表单，接受在线支付。
- 🏦 **银行业** - 设计贷款申请和合规调查表，确保数据收集安全高效。
- 🎓 **教育** - 创建评估测试和学生反馈表单，安全收集教育数据。
- 💼 **人力资源** - 设计员工反馈调查和绩效评估表，优化 HR 流程。

- 💬 **用户评价** - 用户高度评价其灵活性、易用性和卓越的技术支持。
- ❓ **常见问题** - 提供详细的许可模型、集成支持和 SaaS 使用解答。

---

### [SurveyJS - 用于调查与表单的 JavaScript 库](https://surveyjs.io?utm_source=frontend_focus&utm_medium=referral)

**原文标题**: [SurveyJS - JavaScript Libraries for Surveys and Forms](https://surveyjs.io?utm_source=frontend_focus&utm_medium=referral)

开源 JavaScript 表单构建库概览

- 📜 **表单库**：免费开源的 MIT 许可 JavaScript 库，可渲染动态 JSON 表单并收集响应。
- 🛠️ **调查创建器**：自托管的拖放表单构建器，实时生成 JSON 定义，支持商业用途需开发者许可。
- 📊 **仪表盘**：通过交互式图表和表格简化调查数据分析，需商业开发者许可。
- 📄 **PDF 生成器**：将表单保存为可编辑或只读 PDF，需商业开发者许可。
- 🔒 **数据安全**：自托管确保敏感数据完全掌控，符合 HIPAA、FERPA、GDPR 等法规。
- 🎨 **完全定制**：通过 CSS 主题编辑器自由定制品牌风格。
- 🔗 **集成支持**：兼容 React.js、Angular、Vue.js 等前端框架，后端自由选择。
- 💼 **永久许可**：商业用途需一次性付费的永久开发者许可，无版税限制。
- 🛡️ **专业支持**：提供技术支持和详尽文档，助力构建表单管理系统。
- 🏢 **多行业适用**：保险、医疗、市场研究、教育、HR、电商、非营利、银行等行业均可定制表单。
- 💬 **用户评价**：用户高度评价其灵活性、易用性和卓越支持。
- ❓ **常见问题**：解答许可模式、开发者数量、后端集成、SaaS 使用等疑问。

---

### [Storybook 9 现已进入测试阶段](https://storybook.js.org/blog/storybook-9-beta/)

**原文标题**: [Storybook 9 is now in beta](https://storybook.js.org/blog/storybook-9-beta/)

Storybook 9 现已进入测试阶段，带来更轻量、更强大的 UI 测试工具集，支持组件测试、交互测试、无障碍测试等多种功能，同时优化了性能和用户体验。

- 🚀 **Storybook 9 Beta 发布**：功能完备，欢迎试用并提供反馈，帮助完善最终版本。  
- 🧩 **组件测试工具**：结合单元测试的速度和端到端测试的准确性，支持大规模测试覆盖。  
- 🔄 **交互测试增强**：支持单次、批量或全量运行，并新增监视模式实时测试。  
- ♿ **无障碍测试升级**：全新 UI 界面，支持全量测试并查看违规详情。  
- 👀 **视觉测试**：一键检测所有故事的像素级变化。  
- 📊 **测试覆盖率**：快速计算组件测试的代码覆盖率。  
- 🪶 **体积减少 48%**：依赖更轻量，安装更快且避免冲突。  
- 🏷️ **标签分类**：新增标签系统，便于故事组织和筛选。  
- ⚛️ **React Native 全面支持**：兼容 Web 端，支持文档和测试功能。  
- ⬆️ **一键升级**：通过`npx storybook@next upgrade`自动迁移，提供代码修改指南。  
- 📢 **反馈征集**：团队全力支持，欢迎提交 GitHub 问题以优化版本。  
- ✉️ **社区与招聘**：加入开发者社区或应聘 Storybook 团队职位。

---

### [标注单声道](https://qwerasd205.github.io/AnnotationMono/)

**原文标题**: [Annotation Mono](https://qwerasd205.github.io/AnnotationMono/)

Annotation Mono 是一款精心设计的手写风格等宽字体，具有可变轴特性，支持多种语言和符号，并包含精选的连字功能。

- ✒️ 字体风格：理想化的手写风格，灵感来源于等宽位图字体，兼具高可读性和手写特色。
- 🔧 可变轴：支持重量（wght）和倾斜（slnt）两个可变轴，重量从 Thin 到 ExtraBlack，倾斜从 0° 到 -15°。
- 🌍 语言支持：目前支持 377 种基于拉丁的语言，未来计划增加更多语言和技术符号。
- ➡️ 连字功能：包含标准连字（liga）和风格集（ss01），优化编程中常见的符号组合（如 ->、<=、>=）。
- 🔢 OpenType 特性：提供旧式数字（onum）等功能，旧式数字更适合与小写文本搭配。
- 📥 下载：可从 GitHub 下载 Annotation Mono 字体。

---

### [GitHub - qwerasd205/AnnotationMono：一款精心设计的手写风格等宽字体](https://github.com/qwerasd205/AnnotationMono)

**原文标题**: [GitHub - qwerasd205/AnnotationMono: A lovingly crafted handwriting-style monospace font.](https://github.com/qwerasd205/AnnotationMono)

概述：Annotation Mono 是一款手写风格等宽字体，设计精美，适用于多种场景，包括编程、标签、标题和漫画文字。  

- 🖋️ **字体风格**：手写风格的等宽字体，灵感来源于单色位图字体，兼具可读性和手写特色。  
- 🎨 **多样化应用**：可变字重设计，适合代码、标签、标题及漫画文字等多种用途。  
- 🌐 **项目信息**：托管在 GitHub 上，58 颗星，0 个分支，采用 OFL-1.1 许可证。  
- 📂 **文件结构**：包含构建脚本、许可证、README 等文件，主要语言为 HTML 和 Python。  
- 🔖 **版本发布**：最新版本为 v0.2，发布于 2025 年 4 月 3 日。  
- 📚 **更多详情**：可通过项目主页 [qwerasd205.github.io/AnnotationMono](https://qwerasd205.github.io/AnnotationMono) 进一步了解。

---

### [GitHub - mirisuzanne/track-list: 为音频轨道列表增强播放列表控制功能](https://github.com/mirisuzanne/track-list)

**原文标题**: [GitHub - mirisuzanne/track-list: Enhance a list of audio tracks with playlist controls](https://github.com/mirisuzanne/track-list)

一个用于增强音频轨道列表的 Web 组件，提供播放列表控制功能。

- 🎵 该 Web 组件允许一次仅播放一个轨道，并在当前轨道结束后自动播放下一个。
- ⏯️ 提供播放/暂停按钮以及上一曲/下一曲控制功能。
- 📝 使用示例中展示了如何通过 HTML 标记嵌入音频轨道列表。
- 📦 支持通过 npm 安装或手动下载源代码集成到项目中。
- 🎨 提供丰富的样式钩子（style hooks）用于自定义播放控制菜单的外观和交互状态。
- 🔌 包含两个插槽（slots）：`tracks`用于音频轨道列表，`menu`用于播放控制菜单。
- ❤️ 项目由 OddBird 维护，鼓励通过 GitHub 赞助或 Open Collective 支持其开源工作。

---

### [曲目列表 Web 组件演示](https://mirisuzanne.github.io/track-list/demo.html)

**原文标题**: [track-list Web Component Demo](https://mirisuzanne.github.io/track-list/demo.html)

overview summary  
这是一个关于 Web 组件的介绍，该组件用于增强音频元素列表的播放控制功能，支持播放列表操作，并提供了 GitHub 上的源代码。同时，文中列举了一些示例曲目和注意事项。  

- 🎵 Web 组件增强音频列表，提供播放列表控制功能  
- ⏯️ 一次仅播放一首曲目，当前曲目结束后自动播放下一首  
- ⏮️⏭️ 包含播放/暂停按钮及上一首/下一首控制按钮  
- 💻 源代码可在 GitHub 上获取  
- 📋 示例曲目包括《The Holes They Leave》《Teacup Gorilla》等（2015 年发布）  
- ⚠️ 非所有曲目均为必选，后备方案为单独曲目播放  
- 📜 部分曲目标题包含特殊标注（如 C.A. Conrad 的文字引用）

---

### [设计令牌名称生成器](https://namedesigntokens.guide/)

**原文标题**: [Design Tokens Name Generator](https://namedesigntokens.guide/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结。  
- 📌 要点一  
- 🔍 要点二  
- 📊 要点三  

请提供具体内容，我会为您整理成清晰简洁的格式。

---

### [GitHub - dbismut/draggable-slider: 使用 StackBlitz ⚡️ 创建](https://github.com/dbismut/draggable-slider/)

**原文标题**: [GitHub - dbismut/draggable-slider: Created with StackBlitz ⚡️](https://github.com/dbismut/draggable-slider/)

这是一个名为“draggable-slider”的公开项目，由 dbismut 创建，主要功能是实现可拖拽的轮播组件。

- 🚀 **项目创建**：使用 StackBlitz 平台开发，基于 Vite 技术栈。  
- 🌟 **受欢迎程度**：获得 71 个星标和 2 个分支。  
- 📂 **文件结构**：包含多种配置文件（如.gitignore、package.json 等）和示例页面（React、Vue、Vanilla 等）。  
- 🔗 **相关资源**：项目介绍和演示链接可在 Twitter 和 StackBlitz 上查看。  
- 📊 **技术栈**：主要使用 TypeScript（占比 84.3%），辅以 HTML、CSS、Vue 和 JavaScript。  
- 📝 **文档**：提供 README 文件说明项目详情，但未发布正式版本。

---

### [可拖动滑块 - StackBlitz](https://stackblitz.com/edit/vitejs-slider)

**原文标题**: [Draggable Slider - StackBlitz](https://stackblitz.com/edit/vitejs-slider)

好的，请提供需要总结的文本内容，我会按照您要求的模板进行整理，包括概述总结和带 emoji 符号的要点列表。  

示例模板：  

[这里是概述总结，直接呈现文章核心内容]  

- 📌 Emoji 要点 1  
- 🔍 Emoji 要点 2  
- 💡 Emoji 要点 3  

请提供具体文本以便我为您生成内容。

---

### [非 HTML 内容](https://frontendfoc.us/open/690/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/690/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

