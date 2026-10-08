### [](https://blog.cloudflare.com/how-fast-is-the-web/)

**原文标题**: [How fast is the web? Explore billions of real-user measurements with BEACON | Cloudflare Blog](https://blog.cloudflare.com/how-fast-is-the-web/)

overview summary
Cloudflare 发布 BEACON（Browser Experience Across Cloudflare's Observed Network）公开数据集，基于 10,000 个大型网站、数十亿次真实用户测量，展示全球 Web 性能在浏览器、设备、国家和行业间的差异，并公开于 Google BigQuery 供研究与优化。

- 📦 BEACON 是匿名化真实用户监控数据集，覆盖主要浏览器引擎，每日更新于 Google BigQuery，并遵循 RUM Archive 标准。
- 🚀 它将 RUM Archive 的覆盖范围扩大约 100 倍，提供跨浏览器、设备和国家的 Web 性能视角。
- 🧭 目标是缩小“在我的机器上可用”与真实用户网络、设备条件之间的感知差距，推动更快、更普及的互联网。
- ⚡ 报告 Core Web Vitals：LCP（加载）、CLS（视觉稳定）、INP（交互响应），并以完整直方图发布，可查看任意百分位和长尾。
- 🌍 浏览器差异：WebKit 在 iOS 总体表现好，但在 46 个占流量超 10% 的国家，LCP 或 INP 至少比 Blink 差 10%；柬埔寨 WebKit LCP 差 50%。
- 🏛️ 行业差异：政府与政治、健康、儿童安全表现较好；广告、宗教、天气通常最差。
- 🧩 LCP 子项拆解：文档 TTFB、加载延迟、加载时长、渲染延迟；资源下载通常影响最小，发现 LCP 资源和解除渲染阻塞机会更大。
- 🖱️ INP 子项拆解：输入延迟、处理时间、呈现延迟；慢交互中 JavaScript 执行最长，CSS 布局重算带来的呈现延迟也显著。
- 🧭 单页应用：Soft Navigations 各百分位 LCP 比 Hard Navigations 快 2–3 倍，但初始落地页通常更重，需权衡首屏成本。
- 📈 可结合外部数据：例如与世界银行人均 GDP 关联，分析经济条件与各国 Web 性能的关系。
- 📡 Cloudflare Radar 将新增 Web Performance 版块，结合 IQI 网络质量数据与 BEACON，区分网站性能与用户网络性能。
- 🌍 初步发现：带宽与 LCP 通常同向变化；非洲传输体积更小，可能因网站针对网络约束优化，具体原因待研究。
- 🔐 隐私处理：去除域名、URL 路径等标识，按国家、系统、浏览器、协议聚合，少于 5 个数据点丢弃。
- 🧪 数据范围：为平衡流量偏差与样本量，选取 10,000 个大型网站并归一化，保留数十亿级日记录。
- 🔓 获取方式：BEACON 公开在 Google BigQuery，示例查询和 RUM Archive 文档可用，可在社区或 Discord 分享发现。
- 👏 项目致谢：启动源自 Cloudflare 1,111 实习生项目，Chisara Duru 和 Tong Zhou 做出关键贡献。

---

### [](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q4&utm_term=primary+content)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q4&utm_term=primary+content)

Meticulous 是一款面向复杂代码库的自动化端到端测试平台，通过记录用户会话、AI 生成并持续更新测试套件，实现零开发者维护、无 flakes、确定性验证，并能在 PR 合并前评估变更影响。

- ⚙️ 自动化、穷尽、确定性的验证，零开发者投入，支持以 AI 代理写代码的速度发布可靠代码。
- 🏢 受 100+ 组织信任，包括 Dropbox、Notion、Engine 等团队使用。
- 🎥 在本地开发、预发和预览环境添加 recorder script 记录会话，也可选记录生产环境以增加覆盖。
- 🤖 AI 引擎跟踪每次交互执行的代码分支，持续生成视觉端到端测试，覆盖每行代码、每个用户流程和边缘情况。
- 🔀 打开 PR 即可在合并前查看变更对用户工作流的影响。
- 🧪 默认保存并重放后端响应，实现无副作用测试，避免数据变化导致误报，也无需测试账号或模拟数据。
- 🛠️ 无需编写、修复或维护测试；测试随应用演进自动新增和淘汰，始终保持最新完整。
- ⚡ 从 Chromium 层构建的确定性调度引擎消除 flakes，执行速度极快，适合最复杂的应用。
- 🧮 可补充或替代现有测试套件；测试跨计算集群高度并行，1000s 屏幕可在 120 秒内出结果。
- 🧩 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit，添加 recorder script 并接入 CI 即可开始，几分钟完成设置。

---

### [](https://developer.chrome.com/blog/jpeg-xl-in-chrome)

**原文标题**: [Shipping JPEG XL in Chrome  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/jpeg-xl-in-chrome)

Chrome 从 155 版开始正式支持 JPEG XL（.jxl）解码；该格式以更高压缩率、无损/HDR、无损 JPEG 转码等能力面向现代 Web。Chrome 用 Rust 重写解码器以强化内存安全，同时通过 SIMD 与性能优化保持速度，并基于开发者反馈和互操作测试推进落地。

- 🚀 Chrome 155 起提供 JPEG XL（.jxl）图像格式解码支持。
- 🖼️ JPEG XL 是下一代图像格式，压缩率比 JPEG 高 30–50%，支持无损压缩、HDR 和无损 JPEG 转码。
- 💡 官方建议同时尝试 AVIF 与 JPEG XL；JPEG XL 更适合高保真/无损压缩、摄影图像和细粒度渐进解码。
- 🔒 安全优先：用纯 Rust 实现解码器 jxl-rs，减少越界读取、堆溢出、释放后使用等内存安全漏洞。
- ⚡ 性能不妥协：借助 Rust target_feature_11 与 jxl_simd 抽象层安全使用 SIMD，灵感来自 C++ Highway 和 libjxl。
- 🛠️ 优化继承 libjxl，采用跨区域通用处理流水线并减少数据复制，同时通过性能仪表板跟踪表现。
- 🧪 通过模糊测试和 AI 代码审查验证，整个实现历史未发现内存安全 bug。
- 👩‍💻 发布决策源于开发者持续反馈；JPEG XL 是 Interop 2026 热门提案，Chrome 也参与互操作调查与测试覆盖。
- 🌐 鼓励开发者、内容创作者和平台在流程中使用 .jxl 图片与动画，并提交 bug 反馈。
- 🙏 文章致谢 jxl-rs 与 Chrome 集成贡献者，包括 Helmut Januschka 等重要贡献者。

---

### [Chrome 155 发行说明 - Chrome](https://chromestatus.com/release-notes/155)

**原文标题**: [Chrome 155 Release Notes - Chrome Platform Status](https://chromestatus.com/release-notes/155)

Chrome 平台更新为 Web 应用带来窗口管理、后量子加密、CSS、数字凭证、企业调试策略、图像与媒体、WebGPU 及 WebTransport 等多项增强。  
- 🪟 新增窗口管理控制：拥有 window-management 权限的应用可最大化、最小化、恢复窗口，并通过 setResizable() 禁止调整大小；新增 CSS display-state 和 resizable 媒体特性，改善 VDI 远程应用窗口体验。  
- 🔐 WebCrypto 增加后量子密码与常用对称 AEAD：ML-KEM 768/1024、ML-DSA 44/65/87、ChaCha20-Poly1305 和 X-Wing。  
- 🎨 CSS symbols() 允许内联定义匿名计数器样式，支持 cyclic、numeric、alphabetic、symbolic、fixed 等计数系统，可用于 list-style-type、list-style、counter() 和 counters()。  
- ✂️ text-decoration-skip-spaces 控制下划线、上划线、删除线等文本装饰是否跳过空白字符，提升排版视觉效果。  
- 📐 margin-trim 可省略容器首尾子元素的外边距，支持普通块级和多列容器；此前对 flex/grid 的支持已移除。  
- 🪪 Digital Credentials API 支持凭证签发：发证网站可安全向用户移动钱包发起数字凭证配置；Android 借助 CredMan，桌面端借助 CTAP 跨设备方案。  
- 🛡️ chrome.debugger API 新增企业主机与截图限制：托管浏览器可依据 ExtensionSettings、DisableScreenshots 或 DLP 策略阻止调试器附加，并返回策略限制错误。  
- 🌈 PredefinedColorSpace 新增 srgb-linear 和 display-p3-linear，可用于 canvas。  
- 📦 JavaScript 支持 import … with { type: "text" }，按 TC39 提案将文本数据作为字符串模块导入。  
- 🖼️ Blink 新增 JPEG XL（image/jxl）解码，使用内存安全的纯 Rust 解码器 jxl-rs，支持渐进解码、广色域、HDR、高比特深度和动画。  
- ⏸️ 新增 media-playback-while-not-visible 权限策略，可暂停隐藏 iframe 中的可听媒体播放，重新可见后解除限制，提升体验与性能。  
- ⚛️ WebGPU/WGSL 支持 atomic<vec2u> 上的 64 位原子最小/最大操作，便于实现依赖 64 位原子性的算法。  
- 🌐 WebTransport 数据报增强：新增 datagramsReadableType: "bytes" 以支持 BYOB 读取；createWritable() 创建独立可写流，并可用 sendGroup、sendOrder 表达优先级，同时报告最大负载并丢弃超限写入。  
- 📊 WebTransport 可靠性与接收流：新增 reliability、supportsReliableOnly 属性；标准化 WebTransportReceiveStream，其 getStats() 返回 bytesReceived 与 bytesRead。

---

### [HTML 2026 状态](https://survey.devographics.com/en-US/survey/state-of-html/2026)

**原文标题**: [State of HTML 2026](https://survey.devographics.com/en-US/survey/state-of-html/2026)

提供的内容仅为“Loading...”，没有可供摘要的文章正文，因此无法提取主题、要点或结论。

- ⏳ 当前输入只有加载提示“Loading...”
- 📄 未包含任何文章内容或有效信息
- ❓ 无法进行有效总结，请补充完整文本

---

### [](https://example.com/)

**原文标题**: [Example Domain](https://example.com/)

该域名仅用于文档示例，无需许可，但并非可用服务，不应将其用于测试或监控。

- 📄 该域名用于文档示例，无需获得许可。
- 🚫 它不是一个服务。
- ⚠️ 避免依赖它进行测试或监控。

---

### [](https://www.debugbear.com/blog/example-dot-com-redesign-history)

**原文标题**: [Example.com Just Launched The Biggest Redesign In Decades | DebugBear](https://www.debugbear.com/blog/example-dot-com-redesign-history)

2026年9月28日，example.com 进行了数十年来最大幅改版，引入 JavaScript 多语言轮播和 SVG 书本图标；10月3日又取消轮播、直接展示所有语言。文章回顾了这次改版的实现细节、IANA 对改版理由的说明，并梳理该保留域名自2002年可查存档以来在文案、设计、CDN/服务器和 favicon 等方面的长期演变，同时提醒开发者不要将其用于测试或监控。

- 🌐 2026年9月28日改版：新增多语言支持，每5秒切换英语、阿拉伯语、中文、法语、俄语和西班牙语。
- 📖 页面说明 example.com 仅用于文档示例、无需许可，不是服务，不应依赖它做测试和监控；同时插入 SVG 书本图标。
- ✨ 语言切换采用透明度渐变动画，每个字符放在独立 span 中，并递增 CSS transition-delay，实现逐字过渡。
- ⏹️ 2026年10月3日：动画被移除，所有语言从一开始就全部显示。
- 🏛️ IANA 声明：改版主要为了降低带宽需求、提升实用性；页面拆为基础页和单独 JS 文件，自动化流量通常不会加载 JS，从而减少数据传输。
- ⚠️ IANA 强调该域名是文档占位符，不是通用可用性测试端点；提供 HTTP 服务只是“出于礼貌”。
- 📜 2002年1月20日最早存档：仅列出 ICANN/IANA 保留域名，使用表格布局，左上角有 ICANN 标志，服务器为 Apache 1.3.22。
- ✉️ 2002年3月28日：出现今日熟悉的简化文案，说明这些域名保留用于文档、不可注册。
- 🔗 2003年2月7日：加入 RFC 2606 链接；服务器升级为 Red Hat Linux 上的 Apache 1.3.27。
- ➕ 2010年7月30日：example.edu 被加入该页面所提及的域名，与 example.com、.net、.org 并列。
- 🔄 2013年7月29日：移除跳转，example.com 重新提供自有页面并改用 EdgeCast CDN；页面大改版为圆角卡片和“Example Domain”标题，域名列表消失。此前2011年起曾跳转到 IANA 页面。
- 🖋️ 2019年10月17日：字体栈现代化并增加 Mac、iPhone、Windows 等回退字体；文案微调。
- 🖥️ 2025年1月15日：Server 响应头消失，基础设施再次更换；背景涉及 EdgeCast/Edgio 与 Akamai 等变动。
- 🎨 2025年10月9日：再次改版，取消卡片设计、压缩 HTML，文案更直接，链接改为“Learn more”。
- ☁️ 2025年12月17日：迁移到 Cloudflare，响应头出现 cloudflare 和 CF-RAY。
- 🧩 2026年6月9日：添加空 favicon（data:,）并闭合 p 标签，避免浏览器请求 /favicon.ico。
- 🚫 2025年起提示“避免用于运维”：example.com 偶尔不响应，开发者不应依赖其做网络测试或监控。
- ⏳ 总结：改版并不定期，有时连续数月小改，有时长达七年不变；文章来自 DebugBear，并推广其页面速度/Core Web Vitals 监控服务。

---

### [IANA 关于 example.com 为何变更的邮件 | Oliver Dunk](https://www.oliverdunk.com/2026/09/30/iana-reply)

**原文标题**: [IANA's email about why example.com changed | Oliver Dunk](https://www.oliverdunk.com/2026/09/30/iana-reply)

作者就 example.com 页面内容变更向 IANA 发邮件询问，意外收到 IANA 副总裁 Kim Davies 的回复。邮件解释变更主要为了降低带宽或提升实用性，并重申该域名是文档示例用的占位符，不鼓励作为通用测试端点；信息可自由转发。

- 📧 作者当天电邮 IANA，询问 example.com 新内容，获 IANA 副总裁回复。
- 🎯 网站改动通常出于两个目的：减少服务带宽需求，或提升实用性。
- 🌐 example.com 本质是占位域名，不应有人访问；保留页面是说明注册原因与用途。
- ⚙️ 因流量很大，本周把内容拆成基础页面和额外 JavaScript 文件，自动流量通常不取 JS，从而降低数据需求。
- 📚 域名核心用途是文档示例，如说明中的示例；有人复制配置时忘记替换示例域名，会带来附带流量。
- 🚫 该域名并非通用可用性测试端点，IANA 不鼓励此类使用；主机无需运行 HTTP 服务，运营只是出于礼貌。
- ✅ Kim Davies 表示信息可自由使用和转发；邮件日期为 2026 年 9 月 30 日。

---

### [](https://web.dev/blog/web-platform-09-2026)

**原文标题**: [New to the web platform in September  |  Blog  |  web.dev](https://web.dev/blog/web-platform-09-2026)

2026年9月，Chrome 153/154、Firefox 155/156/157 和 Safari 27 进入稳定版，带来大量达到 Baseline Newly available 的 Web 功能；Beta 版则有 Chrome 155/156、Firefox 158、Safari 27.2，预览未来特性。

- 🚀 这是 Chrome 与 Firefox 双周发布的首个月份，稳定版浏览器更新密集。
- 📐 `progress()` CSS 数学函数在 Firefox 155 中支持，成为 Baseline 新可用，并支持 `no-clamp`。
- 🎨 `alpha()` 相对颜色函数在 Firefox 155 与 Safari 27 中支持，可调整颜色透明度并保留色域。
- ↩️ `revert-rule` CSS 关键字在 Safari 27 中支持，可将属性回滚到当前规则不存在时的值。
- 🌓 `light-dark()` 现在支持 `<image>` 值，可随明暗配色方案切换图片或渐变。
- 📌 Safari 27 支持滚动锚定与 `overflow-anchor`，减少 DOM 变化导致的阅读位置跳动。
- 🔤 `font-width` 属性与 `@font-face` 描述符在 Firefox 155、Chrome 154 中推进，成为 Baseline 新可用。
- 🖼️ Safari 27 支持懒加载图片的 `sizes="auto"`，按渲染宽度选择合适图片源。
- 🌊 Safari 27 支持 `ReadableStream` 异步迭代、跨上下文传输与 `ReadableStream.from()`。
- 🎞️ Safari 27 为 `AnimationEvent` 与 `TransitionEvent` 增加 `animation` 属性，便于直接访问动画对象。
- 🍪 Safari 27 支持 `cookieStore.set()` 的 `maxAge` 选项，用秒数设置 Cookie 生命周期。
- 📋 Safari 27 加入可定制 `<select>`，通过 `appearance: base-select` 与 `<selectedcontent>` 实现富样式下拉菜单。
- 🎥 Chrome 153 引入声明式 `<camera>` 与 `<microphone>` 元素，用于用户激活的音视频采集权限请求。
- 🧩 Chrome 153 新增 `Iterator.join()`、`Iterator.zip()`、`Iterator.zipKeyed()`；Firefox 155 新增 `Promise.allKeyed()` 与 `Promise.allSettledKeyed()`。
- 🌐 Firefox 155 扩展 WebTransport，支持协议协商、`createSendGroup()`、`draining`、`exportKeyingMaterial()` 等。
- ⚙️ Safari 27 支持 Service Worker Static Routing API，可通过 `InstallEvent.addRoutes()` 声明式路由并绕过启动。
- 🧪 Chrome 155 Beta 包含 `margin-trim`、`symbols()`、`text-decoration-skip-spaces`、JPEG XL 解码、文本模块导入与 Digital Credentials API。
- 🧪 Chrome 156 Beta 包含 `random()`、`corner` 简写、单轴滚动容器、`scroll-snap-type: pair`、媒体元素状态伪类、`import defer` 与 `<install>` 元素。
- 🧪 Safari 27.2 Beta 调整溢出对齐、固定定位与 `::picker(select)` 的安全对齐，并将 `flow-tolerance` 重命名为 `fit-tolerance`。

---

### [WebAIM：屏幕阅读器用户调查第11次结果](https://webaim.org/projects/screenreadersurvey11/)

**原文标题**: [WebAIM: Screen Reader User Survey #11 Results](https://webaim.org/projects/screenreadersurvey11/)

WebAIM 第11次屏幕阅读器用户调查（2026年7-8月，1780份有效回复）显示：JAWS仍是主要桌面屏幕阅读器，移动端iOS与VoiceOver占主导，标题导航依赖度高，PDF障碍突出，AI使用广泛，但对网页无障碍进展的乐观度略降。

- 📅 调查于2026年7-8月进行，共1780份有效回复，延续2009至2024年的系列调查。
- 🌍 受访者主要来自北美（54.1%）和欧洲（27.7%）；94.8%因残疾使用屏幕阅读器，83.2%为失明。
- 🧑‍💻 屏幕阅读器熟练度：57.8%自评高级；互联网熟练度：64.6%自评高级。
- 💻 桌面主屏幕阅读器：JAWS 55%、NVDA 32.9%、VoiceOver 6.5%；JAWS在北美/澳洲领先，NVDA在非洲/中东、亚洲、南美领先。
- 🧰 常用桌面屏幕阅读器：JAWS 69.2%、NVDA 59.3%、VoiceOver 42%、Narrator 36.1%；70.3%使用多种屏幕阅读器。
- 🌐 主浏览器：Chrome 52.3%、Edge 23.6%、Firefox 15.9%；最常见组合为JAWS+Chrome（31.2%）。
- 🪟 主操作系统：Windows 90.7%、Mac 6.3%；99.7%启用JavaScript。
- ⭐ 使用主屏幕阅读器主因：习惯/熟练49.3%、功能24.3%；多数用户对主屏幕阅读器满意。
- 💰 74.6%认为免费/低成本屏幕阅读器是可行替代，较2024年略降；NVDA/VoiceOver用户更认可。
- 📱 91.8%在移动设备使用屏幕阅读器；iOS占73.3%、Android占24%；VoiceOver常用72.2%、TalkBack 29.5%。
- 🧭 移动主浏览器：Safari 56%、Chrome 28.2%；约49%受访者桌面与移动使用量相当。
- 🛒 在线任务中54.8%偏好移动App，45.2%偏好网站；App偏好较2024年下降。
- 📉 32.2%认为网页内容更无障碍，44.9%认为没变化，22.9%认为更差；整体乐观度略降。
- 🏗️ 83.9%认为改进网站本身比改进辅助技术更能提升无障碍；该比例较2024年略降。
- 🧱 28.3%经常使用地标/区域导航；寻找长页信息时67.8%先用标题导航。
- 🔠 88.3%认为标题层级非常/有些有用；skip链接频繁使用升至37.7%。
- 📄 85.6%认为PDF很可能/有些可能带来障碍；Word文档为31.1%。
- 🤖 AI常见用途：生成图像描述/替代文本60.1%、复杂图像分析49.7%、在线任务指导40.6%、网页/文档摘要37.1%；仅8.2%未使用AI。
- 📈 趋势：JAWS回升、NVDA/VoiceOver下降；Windows使用增加；网页无障碍进展感知和免费屏幕阅读器可行性略降。

---

### [获取失败](https://www.w3.org/news/2026/updated-candidate-recommendation-scalable-vector-graphics-svg-2/)

**原文标题**: [Failed to retrieve](https://www.w3.org/news/2026/updated-candidate-recommendation-scalable-vector-graphics-svg-2/)

无法总结：获取内容失败，状态码 403。

---

### [](https://calibreapp.com/blog/airline-websites-are-slow)

**原文标题**: [It’s official: Airline websites are slow, but they don’t have to be | Calibre](https://calibreapp.com/blog/airline-websites-are-slow)

overview summary
这篇分析基于 Chrome UX Report 对全球 111 家顶级航空公司预订网站的真实用户 Core Web Vitals 数据，发现绝大多数航司网站速度极慢：95% 移动端未通过 CWV，连 Skytrax 排名靠前的航司也表现糟糕。问题源于复杂实时预订系统、第三方引擎、低质量 UI、阻塞式请求与缓存不足，但 Frontier、Ryanair 等证明可以做得更快；慢站点会直接损失转化与收入。

- 📊 研究覆盖 111 家全球顶级航司，优先使用直接预订引擎 URL，数据来自 2026 年 8 月 Chrome UX Report 真实用户指标。
- 🐌 95% 的航司网站在移动端未通过 Google Core Web Vitals；仅 5 个移动端、14 个桌面端通过。
- 📱 移动端各指标通过率：LCP 24%、CLS 45%、INP 15%；INP 最差，85% 站点交互超过 200ms。
- 🏆 Skytrax 顶级航司并未拥有最快网站：前 10 名全部未通过 CWV，卡塔尔航空移动端性能基准第 79，国泰航空排名最后。
- 🥶 国泰航空移动端 LCP 达 10.6 秒、INP 1.4 秒；Air Arabia 移动端 INP 1.85 秒；Air India Express 移动 TTFB 5.5 秒。
- ⏱️ 一次订票通常涉及约 20 次交互，慢交互会显著拖累选日期、选座、付款等核心流程。
- 🧩 航司预订系统复杂，依赖 Amadeus、Sabre、TravelSky 等第三方实时系统，聚合搜索难缓存。
- 🛠️ 主要问题包括：UI 实现差、骨架屏与布局位移、交互被服务器请求阻塞、预订搜索优化差、缓存不足。
- 🧪 同一预订引擎供应商既有快站也有慢站，供应商本身不能完全解释性能差异。
- 💸 慢性能直接损失收入：LCP 从 1.5 秒增至 2.5 秒，转化率约低 30%；每 32ms INP 影响约 1.5% 转化。
- 🏅 Frontier Airlines 移动和桌面表现最佳，9 个月内 LCP 从 3.29 秒降至 2.60 秒。
- ✈️ Ryanair 长期持续优化，是速度快、响应好的代表。
- 🇨🇳 海南航空是唯一进入 Skytrax 前十且性能排名较好的航司。
- ✅ 改进建议：监测真实用户性能、优先优化高流量页面、审查 API 与第三方脚本、善用 HTTP 缓存、异步请求、避免阻塞、稳定布局。
- 🔁 修复大型网站需要时间，应持续监控并逐项改善最差页面或交互，转化率和用户体验将随之提升。

---

### [CSS 现在负责你的工具提示定位 - Matt Smith](https://allthingssmitty.com/2026/10/05/css-does-your-tooltip-positioning-now/)

**原文标题**: [
    CSS does your tooltip positioning now - Matt Smith
  ](https://allthingssmitty.com/2026/10/05/css-does-your-tooltip-positioning-now/)

CSS 锚点定位让元素可跟随指定锚点自动定位，内置滚动/缩放重算和溢出翻转，适合 tooltip、popover 和下拉菜单，且多数场景无需 JavaScript。  
- 🧰 旧方案：用 `getBoundingClientRect()` 和 `top/left` 定位，需监听 `resize/scroll`，并手动计算溢出或翻转，或依赖 JS 库。  
- 🎯 新方案核心：给锚点设 `anchor-name`，给目标设 `position: fixed/absolute`、`position-anchor` 和 `position-area`，即可定位。  
- ♻️ 浏览器会自动在滚动、窗口调整时重新计算位置；仅适用于已绝对或固定定位的元素。  
- 🏷️ `anchor-name` 不必全页唯一，但每个锚点与其匹配目标之间必须唯一；组件复用时需为每个实例生成独立名称。  
- 📐 `position-area` 用 `bottom`、`top`、`bottom span-right` 等描述放置，替代手写 `top: calc()` 偏移。  
- 🔄 `position-try-fallbacks: flip-block, flip-inline` 可在溢出视口时自动翻转到另一侧，省去 resize 监听和手动检测。  
- 🪟 与原生 `popover` 配合可实现下拉菜单：自动置顶渲染、避免 `z-index` 争斗、点击外部轻关闭。  
- 📏 `anchor-size(width)` 可让下拉菜单宽度直接匹配触发按钮，无需 JS 测量。  
- 👁️ 锚点定位只解决“放在哪”，不解决“何时显示”；显示切换仍需 `:has()`、`popover` 或少量 JS。  
- 🧩 非兄弟元素可借助共同祖先上的 `:has()`，根据锚点状态显示注释。  
- 🧭 经验法则：相对特定元素定位用 `anchor-name/position-anchor`；相对自身容器用 `absolute + relative` 父级即可。  
- 🌐 现代 Chrome、Firefox、Safari、Edge 支持良好，但 Safari/Chrome 在回退定位边缘情况有差异，`popover` 默认 margin 可能干扰，旧浏览器需 `@supports` 回退。  
- ♿ 锚点关系是纯视觉的，屏幕阅读器仍按文档顺序朗读；`aria-describedby` 只能部分弥补，不应视为无障碍方案。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=frontendfocus&utm_term=home&utm_content=Cooperpress)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=frontendfocus&utm_term=home&utm_content=Cooperpress)

Expo 是一个面向移动与原生应用的全栈开发平台，提供 CLI、SDK、MCP、云模拟器等工具，并通过 EAS 覆盖构建、测试、部署、OTA 更新、监控与上架流程；它同时服务人类开发者与 AI agent，已被数百万开发者和大量生产项目采用。

- 🚀 Expo 帮助开发者构建精美且持续改进的原生应用，覆盖开发、测试、发布和监控全流程。
- 🧰 核心工具包括 Expo SDK、Expo CLI、Expo MCP、Expo Go、Snack、Orbit，以及 EAS 服务。
- 🤖 面向 agentic workflows，Expo 提供 Develop、Test、Deploy、Monitor 等能力，支持 AI 原生应用开发。
- 🧪 云模拟器和设备基础设施让团队与 AI agent 能在真实环境中测试，提前发现应用问题。
- 📦 部署支持 TestFlight 与应用商店原生发布，Update 负责后续 OTA 更新，并可控制渠道与灰度发布。
- 📈 Observe 提供崩溃信息、性能指标和 Update 采用率，帮助了解生产环境表现并快速修复。
- 🌐 使用单一代码库即可将应用分发到 Android、iOS 和 Web，依托 Build 与 Hosting 实现跨平台。
- 🔄 Update 支持快速 OTA 更新，将修复与改进即时送达用户。
- 📱 云模拟器为 coding agent 提供“设备”，让 agent 能启动应用、验证修复并证明结果。
- 🚀 Launch 简化 App Store 上架流程，无需配置或前置知识即可将应用交付真实用户。
- 🏗️ Workflows 可自动化构建、测试和发布，并在每次变更时运行测试套件，支持现成模板。
- 🧩 Expo SDK 经过 10+ 年打磨，提供 100+ 生产 API，一次安装即可使用，并欢迎所有原生代码。
- 🛠️ 基础设施支持 Expo、React Native、Swift、Jetpack Compose、Kotlin 等多种技术。
- 📊 规模数据包括 7M+ 周下载量、100K+ 活跃开发者、500K+ 项目、100K+ 日构建量。
- 💬 社区方面，80% 的 React Native 开发者选择 Expo，Discord 成员超过 70K。
- 🗣️ 开发者评价普遍称赞 Expo 让 React Native 开发更简单、性能更好、生态与文档更优，甚至推荐优先于纯 React Native。
- ✅ 合规与信任包括 Meta 推荐、React Foundation 会员、SOC 2 Type II、GDPR、CCPA 和 SSO。

---

### [](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/)

**原文标题**: [Why don’t more developers “use the platform”? | Read the Tea Leaves](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/)

文章围绕“使用平台”这一开发者口号展开，分析为何尽管平台 API 通常性能更好、可用性更强，许多开发者仍倾向自行用 JavaScript 或第三方库实现，并探讨历史、习惯、文档、乐趣、认知不足以及 AI 编程对这一现象的影响。

- 🕰️ 历史原因：浏览器长期落后于其上生态，jQuery 等库填补 API 空白，旧浏览器兼容问题让自建方案更合理。
- 🧭 熟悉度与习惯：开发者习惯从 npm、React 生态寻找组件，即使问题本可用平台 API 更直接解决。
- 📚 文档生态：许多 npm 包有友好 README 与教程，而 Web 平台文档曾分散在博客、StackOverflow、CSS Tricks 等站点。
- 🛠️ 自建更有趣：实现弹窗、焦点陷阱等虽复杂，但能带来学习、定制与成就感，还会产生“宜家效应”。
- 🧱 认知与 CSS 难度：不少 JavaScript 方案源于未深入理解 CSS，而 clear fix、floats、min-width: 0 等确实不直观。
- 🗄️ 不限于 Web：ClickHouse 案例说明，在不熟悉的平台上自建压缩或键值存储，可能不如平台原生能力高效。
- 🧠 专家视角：深入理解系统后，能用更少代码替代复杂实现，减少长期维护负担。
- 🤖 AI 的双面影响：乐观看，LLM 能精准选择平台 API 并削弱“宜家效应”；悲观看，它会重复造轮子、助长过度工程化。
- ⚖️ 结论：作者喜爱“使用平台”口号，也理解平台怀疑者；只要存在平台层，这场争论就会持续。

---

### [Sass：通往 Dart Sass 2 之路](https://sass-lang.com/blog/the-road-to-dart-sass-2/)

**原文标题**: [Sass: The Road to Dart Sass 2](https://sass-lang.com/blog/the-road-to-dart-sass-2/)

本文回顾 Dart Sass 从 1.0.0 到 Dart Sass 2 的发展路线，说明其在性能、JS 易用性、CSS/Sass 新特性上的进展，以及 2.0 将带来的破坏性变更、例外和迁移建议。

- 🎯 2018 年 3 月发布 Dart Sass 1.0.0，目标是延续 Ruby Sass 快速修复、紧跟 CSS 规范，并与 LibSass 竞争性能、改善 JS 使用体验。
- 🏆 2021 年下载量超越 node-sass，LibSass 去年正式结束生命周期。
- ✨ 新增 CSS 支持：颜色空间、数学函数、新 `if()` 语法；新增 Sass 特性：模块系统、嵌套 map 函数、一等 mixin 与模块。
- 🧰 使用场景扩展：重做 JS API、嵌入式 Dart Sass、`pkg:` 导入器、支持浏览器直接运行。
- ⚠️ 旧设计会逐步淘汰，如 `/` 作除法、减法运算符、可配置私有变量；破坏性变更大多留到主版本。
- 📅 Dart Sass 2 预计 2026 年 12 月发布，多数 1.x 弃用警告将变为错误。
- ⏳ 例外：`@import` 相关弃用（`import`、`global-builtin`、`color-module-compat`）及旧式 Sass `if()` 函数要到 Dart Sass 3 才移除。
- 🧾 本博文之后新增的弃用不会在 Dart Sass 2 中变成错误；具体为 1.105.0 之后引入的弃用不会报错。
- ➗ Dart Sass 2 将让 `/` 匹配 CSS，作为分隔符而非除法，生成斜杠分隔列表；除法改用 `math.div()` 或 `calc()` 中的 `/`。
- 🧪 迁移准备：用弃用控制把警告升级为错误；CLI 可传 `--fatal-deprecations=1.79.0,compile-string-relative-url,misplaced-rest,with-private,function-name,adjacent-compounds`，JS API 设置对应 `fatalDeprecations`。
- 🛠️ 若仍有弃用，可用 Sass migrator 自动迁移常见问题。
- ⚖️ 官方保留因 CSS 兼容性在三个月弃用期后做必要破坏性变更的权利。
- 📦 当前 Dart Sass 1.105.1；LibSass 与 Ruby Sass 已终止维护。

---

### [](https://dbushell.com/2026/10/07/sustainable-web-career/)

**原文标题**: [A sustainable web career, for when all this blows over â David Bushell â Web Dev (UK)](https://dbushell.com/2026/10/07/sustainable-web-career/)

网络行业正经历非理性低谷，财务与职业前景承压，但人们仍需要网络。作者建议不要在没有后路时辞掉有薪工作，并认为应回归基础、修炼稀缺技能，等行业回暖时占据有利位置。

- 📉 网络行业陷入阶段性困境，长期职业前景不稳，但网络需求本身并未消失。
- 🍺 不要在没有备用方案时辞职；先熬过这轮风波，等待情况好转。
- ♿ 无障碍是可持续职业重点：从第一天融入决策，学习指南，与真实用户测试，并尊重专家意见。
- 🎨 深入学习 CSS：掌握层叠层、低特异性选择器等，别依赖 CSS-in-JS 等限制性抽象。
- 🗣️ 沟通是稀缺软技能：简洁表达、敢于提问、提前处理顾虑、不指责，保持积极。
- ✊ 拒绝法西斯主义：科技界极右与仇恨抬头，不要沉默，警惕否认威胁的人。
- ⚛️ 不再值得投入 React：遗留框架、代码生成快于阅读、高薪岗位将减少。
- 🔒 GitHub 已成负担：私有仓库用自托管 git forge（如 Forgejo），CI/CD 本地化或选独立服务，并学基础 git。
- 📵 不要被影响者叙事主导：他们推销新奇事物，普通用户仍在使用网络，注意力经济不再重要。
- 🧭 结论：网络是为人服务的创造；丢掉繁荣期积累的负担，回归基础，为需求回归做好准备。

---

### [理解双向文本：开发者指南](https://blog.master.dev/you-dont-know-bidi-and-neither-does-chatgpt/)

**原文标题**: [Understanding Bidirectional Text: A Guide for Developers](https://blog.master.dev/you-dont-know-bidi-and-neither-does-chatgpt/)

双向文本（bidi）指同一段内容混合了从左到右（LTR）和从右到左（RTL）的文字。文章解释 Web 默认假设 LTR，导致阿拉伯语、波斯语、希伯来语等 RTL 内容在标点、数字、空格和中英文混排时显示错乱；并介绍 Unicode 双向算法、基准方向，以及用 `dir`、`dir="auto"`、`<bdi>`、LRM/RLM 等修复方式，同时提醒不要用 CSS `unicode-bidi` 控制渲染。文章还用 ChatGPT、Sublime Text、嵌套标题、数字跟随、列表和自动搜索等例子说明 bidi 问题及 LLM 的潜力。

- 🧭 双向文本需要同时处理“逻辑顺序”和“视觉顺序”，浏览器依靠 Unicode 双向算法决定字符显示位置。
- ⚠️ 计算机、浏览器和很多工具默认以 LTR 为中心；Sublime Text 曾不支持 RTL，导致 RTL 字符逐个从左到右错误显示。
- 🤖 ChatGPT 能理解语言含义，却可能在阿拉伯语、波斯语混排中错误排列数字、箭头和标点；问题在渲染层，不只是模型理解。
- 🧠 Unicode 中每个字符都有方向属性：拉丁字符通常强 LTR，阿拉伯/波斯/希伯来字符通常强 RTL。
- ⚪ 空格、标点、等号、数字等是中性或弱方向字符；算法会根据两侧强字符的“三明治规则”或基准方向决定其位置。
- 🧱 基准方向（base direction）为文本提供方向上下文；HTML 默认是 LTR，可在 `<html>` 或局部元素上设置 `dir="rtl"` / `dir="ltr"`。
- 🛠️ 修复原则：把 `dir` 尽量设置在紧贴目标内容的元素上；需要时可包裹 `<span>` 等内联元素来指定方向。
- 🔄 动态内容方向未知时，用 `dir="auto"`，让浏览器根据元素中第一个强方向字符判断方向。
- 🛡️ `<bdi>` 元素可自动隔离内容并设置 `dir="auto"`，防止相邻文本的方向性互相泄漏。
- 🫥 可使用不可见 Unicode 标记：LRM（U+200E）和 RLM（U+200F），在标点等中性字符旁提供强方向信号。
- 🚫 不要用 CSS `unicode-bidi` 控制双向文本渲染；方向是内容层问题，样式不应决定文字含义。
- 🧩 嵌套 bidi 很棘手：RTL 标题内的 `C++` 中，`+` 是中性字符，可能落到错误一侧，需要给内层 `C++` 再设 `dir="ltr"`。
- 🔢 数字方向弱，可能被前一个 RTL 字符“带走”；应隔离标题或数字所在片段，避免顺序错乱。
- 📋 列表中的逗号是中性字符，可能被相邻 RTL 名称影响，使整段顺序反转；应隔离每个名称。
- 🕵️ 有些情况仅靠标记无法预防，例如搜索字符串以 `CSS` 开头但整体是乌尔都语，`dir="auto"` 会误判为 LTR；需要脚本估算整体方向，如 Google Closure Library 的 `estimateDirection`。
- 💡 LLM 可帮助判断文本整体方向，但应用层仍需通过 `dir`、`<bdi>`、RLM/LRM 等把意图传给渲染器。
- 🌍 结语：平台和开发者应重视 RTL 用户，技术已足够成熟，应正确处理双向文本；可参考 W3C Internationalization: Directionality。

---

### [使用现代 CSS 实现 children-count()](https://css-tip.com/children-count/)

**原文标题**: [Implementing children-count() using Modern CSS](https://css-tip.com/children-count/)

本文介绍一种使用现代 CSS 和滚动驱动动画来“黑科技”实现 `children-count()` 的方法：在官方函数发布前，通过额外元素与宽度传递，间接获取容器子元素数量，并用于显示隐藏内容数量或动态网格布局。

- 🧮 目前已有 `sibling-count()` 可获取兄弟元素数量，但 `children-count()` 仍只有提案。
- 🛠️ 在正式发布前，可用 Scroll-Driven Animations 模拟 `children-count()`。
- ➕ 需在容器内添加额外元素（如 `<n>`），这是该方法的一个缺点。
- 📏 设置该元素宽度为 `calc((sibling-count() - 1) * 1px)`，减 1 是为了排除额外元素自身。
- 🔄 沿用“无需 JavaScript 获取元素宽高”的技巧，把其宽度传递给父元素。
- 🎞️ 通过 `@property --_n`、`timeline-scope`、`animation-timeline` 和 `animation-range: entry 100% exit` 建立动画。
- 🧮 在父元素上用 `--n: round(1 / var(--_n))`，即可将 `--n` 当作 `children-count()` 使用。
- 🧩 在额外元素上生成 `1px` 宽伪元素并设置 `view-timeline: --n x` 来触发时间线。
- 💡 可用于显示隐藏内容数量，或实现动态网格布局（灵感来自 kizu.dev）。
- ⚠️ 该方法非常 hacky，需谨慎使用；文末还列出更多 CSS 技巧，如渐变着色仅边框形状、纯 CSS 动态节点连接 II。

---

### [](https://howdopasskeyswork.com/)

**原文标题**: [How do passkeys work — Mystic Coders](https://howdopasskeyswork.com/)

overview summary
密码登录时你把"秘密"交给网站，而通行密钥（passkey）只发送"证明"，由网站用设置时保存的公钥来验证。私钥始终留在你的设备或密码管理器里，通过人脸、指纹或设备 PIN 在本地解锁，网站拿到的是签名而非你的生物特征。

- 🔐 核心区别：密码是发送秘密，通行密钥是发送证明，网站用公钥核验
- 🛠️ 创建步骤：在已登录状态下进入安全设置，选择"创建通行密钥"，挑选保存位置，并用面部、指纹或 PIN 批准
- 💾 保存位置：通常存于密码管理器（如 Apple 密码、Google 密码管理器、1Password），也可存于设备本身（如 Windows Hello）或实体安全密钥
- 🔑 登录流程：服务器生成一次性随机挑战，设备找到对应凭据并要求你授权
- ✍️ 签名机制：私钥对认证器数据与客户端数据哈希签名，证明绑定本次尝试和网站来源
- 🎭 假网站无效：浏览器会校验真实来源，仿冒域名既拿不到真站凭据，其注册的新密钥服务器也不认
- 🧬 隐私保护：面部、指纹或 PIN 只在本地校验，网站只收到"设备持有正确密钥"的证明
- 📱 设备丢失：同步型通行密钥可在其他设备恢复，设备绑定型则需要备用登录方式或账号恢复
- ⚠️ 局限：无法防范设备被入侵、会话被窃取或账号恢复流程被滥用
- 🖥️ 服务端实现：需注册选项/验证、登录选项/验证四个端点，账号授权、挑战生命周期、凭据存储与会话仍由应用负责

---

### [Panda CSS 2.0 | Panda CSS 博客 - Panda CSS](https://panda-css.com/blog/panda-css-v2)

**原文标题**: [Panda CSS 2.0 | Panda CSS Blog - Panda CSS](https://panda-css.com/blog/panda-css-v2)

Panda CSS 2.0 发布：核心是用 Rust 重写编译器并基于 Oxc，但保留原有样式 API；带来大幅性能提升、更轻类型、可发布设计系统及多项新功能，升级重点为 ESM-only 和少量破坏性变更。

- 🐼 样式写法不变：仍使用 `css()`、recipes、patterns、tokens、conditions 和 JSX 样式属性，变化集中在底层引擎。
- ⚡ 性能大幅提升：提取快 15–37×，watch 模式重解析约 360×，`staticCss` 约 85×，29,000 条规则从 25.7 秒降到约 0.3 秒。
- 🧠 类型更轻：生成类型实例化减少约 99%，`tsc` 内存降低约 21–25%，类型检查时间降低 40–60%。
- 🏃 运行时约快 4×：`css()` 和 recipes 增加 memoization，重复样式无需重复计算。
- 🔧 新引擎流水线为 extract → encode → emit：每个文件只解析一次，先检查 import，跳过不使用 Panda 的文件。
- 🧩 值解析增强：在 Rust 中直接解析 imports、操作符、三元、枚举和 `token()`，并支持跨文件常量折叠。
- 🎨 CSS 输出改进：断点改用 media-range 语法，容器查询使用 `inline-size`，层内排序确定，shorthand 排在 longhand 前。
- 🧬 全局变量改用 `@property`：默认值只在变量实际使用时生成，不再向所有元素注入 34 个变量。
- 📦 可发布设计系统：用 `panda lib` 打包，消费端通过 `designSystem` 引用，无需在应用中重新提取样式。
- 🎞️ 新增 `viewTransition()`：支持 View Transitions API，可定义 old/new 状态和命名过渡。
- 🛟 新增 `firstThatWorks()`：按顺序输出现代值加回落值，类型随属性推导。
- 🔑 新增 `keyframes()` 与 `positionTry()`：支持组件局部关键帧和 CSS anchor-positioning fallback。
- 🧰 基础预设新增 mask、scrollbar 工具，以及 `_pointerFine`、`_userValid`、`_inert` 等条件和更多 `text-wrap` 值。
- 🖥️ CLI 改进：`panda` 统一 codegen 与 CSS 生成；新增 `doctor`、`analyze`、`debug`、`--profile`、`--include`、`panda init -i`。
- 🧹 官方 ESLint 插件：复用提取引擎，提供 `no-invalid-token-paths`、`prefer-token`、`no-shorthand-longhand-mix`、`consistent-property-style` 等规则，并支持 oxlint。
- ✍️ 新增 `@pandacss/preset-typography`：提供 `prose` recipe，适合 Markdown 或 CMS 渲染的 HTML。
- 🔌 工具链更新：MCP 独立为 `npx -y @pandacss/mcp`；直接读取 `.vue`、`.svelte`、`.astro`；提供 Vite、webpack、Rollup、Bun 插件，`transform: true` 可移除运行时。
- ⚠️ 升级要求：ESM-only，需要 Node 22+；`panda.config.ts` 基本兼容，但 hooks 移入 plugins，`createStyleContext` 拆分为 `createSlotRecipeContext`/`createRecipeContext`，`matchTag` 改为 `jsxMatchTag`。
- 🗑️ 移除与合并：移除 `studio`、`eject`、`emitTokensOnly` 等 9 个配置；`inspect`、`validate`、`info` 合并为 `panda doctor`；日志标志合并为 `--log-level`。
- 🧱 迁移注意：Panda CSS 位于 `@layer` 中，未分层的旧样式会覆盖 Panda；可逐步迁移，使用 `postcss-cascade-layers` 或按路由、目录、团队划清边界。
- 📥 安装方式：`npm install @pandacss/dev@latest`，完整升级指南见官方文档。

---

### [](https://shaders.com/updates/shaders-is-open-source)

**原文标题**: [Shaders is now open source — Shaders](https://shaders.com/updates/shaders-is-open-source)

Shaders 于 2026 年 10 月 6 日宣布，其渲染引擎、全部 shader 组件与框架绑定以 MIT 许可证开源，让设计工程师和 AI 代理能基于生产级 WebGPU 组件构建视觉效果，同时 Shaders Pro 继续提供高级预设与支持。

- 🚀 Shaders 渲染引擎、所有 shader 组件和框架绑定现已开源，采用 MIT 许可证。
- ⭐ 项目已上线 GitHub，可前往 star。
- 🎨 开源初衷是让设计工程师无需成为图形程序员，也能使用创意 shader 效果。
- 🤖 AI 让 shader 创作更简单，因此开放核心组件、原语和渲染引擎更有价值。
- 🧱 开发者可基于生产验证组件和优化 WebGPU 运行时构建，无需从原始 shader 代码起步。
- 💎 Shaders Pro 仍是最快发现、定制和发布精致 WebGPU 效果的方式。
- 🌍 组件可用于个人与商业客户工作、SaaS、内部工具等，无需许可证。
- 🧾 可从设计编辑器免费导出代码，无限制。
- 🛠️ 可用公开且文档化的 defineShader 语言编写自己的组件（实验性），也可提交 PR 贡献。
- 📦 现有 Pro 订阅保留：1000+ 预设、55+ 预建区块、单提示安装、无水印渲染视频/图像、专属 Discord 角色和频道、优先支持。
- 💰 Pro 定价不变；过去 30 天若仅为商业用途或代码导出购买 Pro 且受影响，可联系团队解决；旧 Core 订阅将免费获得 Pro 权益。
- 💬 官方期待社区推进，并邀请在 Discord 交流；感谢创始人 Simon。

---

### [组件 — 着色器文档](https://shaders.com/docs/components)

**原文标题**: [Components — Shaders Documentation](https://shaders.com/docs/components)

该内容展示了一个包含 198+ 个组件的图形与视觉效果库，按功能划分为九大类，涵盖纹理生成、形状绘制、材质效果、风格化处理、交互模拟、扭曲变形、转场过渡、模糊处理与色彩调整，可用于实时渲染、动画及视频后期制作。

- 🎨 组件总数超过 198 个，分为九大类别，每类均有明确用途与数量标注
- 🖼️ 纹理类（Textures）54 个：可生成极光、光束、大理石、等离子、噪声、渐变等完整画面
- ⬛ 形状类（Shapes）16 个：提供圆、星形、心形、多边形等基于 SDF 的清晰矢量形状
- 💎 形状特效类（Shape Effects）23 个：为图形赋予玻璃、铬金属、水晶、霓虹、水、烟雾等真实材质质感
- ✨ 风格化类（Stylize）31 个：包括 ASCII 艺术、CRT 屏幕、故障、半调、胶片颗粒、VHS 等视觉风格
- 🖱️ 交互类（Interactive）16 个：支持光标响应的效果，如群集模拟、墨流、反应扩散、碎裂、烟雾等
- 🔀 扭曲类（Distortions）22 个：对图层进行弯曲、膨胀、万花筒、极坐标、3D 曲面等变形处理
- 🎬 转场类（Transitions）13 个：提供百叶窗、虹膜擦除、翻页、棋盘溶解等两图层过渡效果
- 🌫️ 模糊类（Blurs）9 个：涵盖高斯、散景、通道、线性、倾斜移轴、变焦等模糊方式
- 🎚️ 调整类（Adjustments）14 个：包含亮度对比度、曝光、色调分离、电影胶片、饱和度等色彩校正工具
- ⚡ 多种效果由 Paper Shaders 等技术驱动，支持真实光影、折射与物理模拟

---

### [](https://surveyjs.io/?utm_source=frontend&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=email)

SurveyJS 是一套用于客户端问卷与表单管理的 JavaScript 库，提供表单渲染、拖拽式创建、数据看板和 PDF 生成等核心能力，强调自托管、完整数据所有权和与任意后端集成的灵活性。

- 🧩 核心产品包括 Form Library、Survey Creator、Dashboard 和 PDF Generator 四大组件。
- 📝 Form Library 是 MIT 许可的 UI 组件，可解析 SurveyJS 表单 JSON 并即时渲染动态交互表单，用于收集用户响应并发送到自有数据库。
- 🛠️ Survey Creator 是白标拖拽式表单构建器，可自动生成描述结构、布局、样式和行为的 JSON schema，并可完全定制以匹配应用设计。
- 📊 Dashboard 可解析 JSON schema、识别数据类型，并通过交互式图表和表格可视化问卷结果。
- 📄 PDF Generator 可根据表单 JSON schema 渲染 PDF，支持导出可编辑或预填的 PDF 表单。
- 🔗 SurveyJS 面向客户端-服务器架构，可与任意后端技术栈集成，自动化安全提交和数据处理。
- 📚 文档提供 ASP.NET Core、Node.js、PHP、Python、WordPress、Node.js + PostgreSQL、Node.js + MongoDB 等后端集成示例。
- 🧾 每个表单由 JSON schema 定义结构、问题、逻辑和布局；schema 可由后端按用户角色、工作流状态或外部数据动态生成或修改。
- 🔄 JSON 驱动方式将表单视为动态、可版本控制的配置对象，便于实现数据驱动的表单工作流。
- 🎨 与 SaaS 工具不同，SurveyJS 允许完全控制表单管理体验，包括重设样式、配置或隐藏设置、本地化、扩展自定义问题类型、校验规则和操作。
- 📦 以 npm 包形式提供，支持 React、Angular、Vue3 和 vanilla JavaScript，可直接集成到现有代码库并用自有基础设施自动化管理。
- 🔐 按设计保障数据所有权与合规：SurveyJS 不存储或传输数据到外部服务，数据存储位置、加密方式和访问权限完全由用户决定。
- ✅ 有助于满足 GDPR、HIPAA 等数据保护法规以及内部安全标准，提供透明、可审计的解决方案。
- 🏢 自托管架构让企业可在自有环境中设计、渲染、收集、分析和导出表单，兼顾低代码灵活性、开发者自由和完整数据控制。
- 🏭 适用行业广泛，包括保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利和银行等。
- 🧰 主要能力覆盖安全数据收集、拖拽式表单创建、实时数据报告，以及将 Web 表单导出为 PDF。
- 🛡️ 自托管可避免第三方 SaaS 依赖，帮助确保受访者匿名性、隐私、合法合规和数据安全销毁。
- ⭐ 用户评价强调其灵活性、易用性、支持多种 JavaScript 环境、复杂条件逻辑、高度可定制、开源以及优质客服。
- 💳 许可方面，开发者许可证为一次性购买；维护订阅提供新功能、改进、错误修复和 Help Desk 支持，首次购买含 12 个月免费订阅，之后可续订。
- ♾️ Survey Creator 不限制管理员、受访者、表单数量、月度提交、文件上传或所用功能，所有表单和响应存储在用户自己的数据库中。
- 🖥️ SurveyJS 只专注前端，不提供后端解决方案或数据存储；用户需自建后端处理数据存储、处理和用户认证。
- 🔑 许可证可分配给团队成员或外包开发者，被分配者获得 Developer 状态，可使用许可证并联系支持。
- 📩 许可证密钥可在订单确认页、订单确认邮件以及账户的 License Manager 中获取。
- 🚀 官方建议通过文档、后端集成示例、All-in-One Demo 和定价方案进一步了解并开始试用。

---

### [](https://videojs.org/blog/videojs-10)

**原文标题**: [Video.js v10 is GA — let the migrations begin! | Video.js | Open Source Video Player](https://videojs.org/blog/videojs-10)

Video.js 10.0.0 于 2026 年 10 月 1 日正式发布，结束 Beta/RC；这是稳定版，并且是一次底层重构，整合 Video.js、Plyr、Vidstack、Media Chrome、Mux Player 的经验。
- 🚀 Video.js v10 GA：经过一年设计、开发和测试，10.0.0 正式上线，可从零开始或从 v8 等播放器迁移。
- 🧱 这不是简单升级，而是 ground-up rebuild；把五个播放器项目汇聚到一个项目与贡献者群体。
- 📉 RC 基准显示默认包比 v8 小 60%；可组合架构让用户不必打包未使用功能。
- ⚛️ 框架友好：一等 React 组件、原生 Web Components、TypeScript、Tailwind；状态、UI、媒体分离。
- 🎨 默认皮肤更精美，且可把皮肤源码引入项目，直接编辑布局、控件与样式。
- 🌐 支持 HLS、DASH、YouTube、Vimeo、Mux、Cloudflare Stream 等来源和服务。
- 🛠️ GA 改进文档与安装体验，提供更清晰的框架路径、CDN 组合，以及 v8 旧 API 到 v10 的迁移指导。
- 🧩 一等 Shadcn 支持：用 CLI 添加皮肤源码，按需改按钮、时间线、控件，不必等待配置项。
- 🤖 官方 Video.js skill 帮助编码代理使用 v10 模式与文档；安装命令为 `npx @videojs/cli agents skills`。
- 🐛 新增皮肤标题、章节展示改进，Compat 皮肤兼容 Safari 16；修复大量 bug 并扩大真实应用测试。
- ⚠️ SPF 新流媒体引擎组合框架带来最大体积节省，但尚不支持广告或真正低延迟直播；这些场景可用 HLS.js 后端的 HlsJsVideo（当前 HLS 默认）。
- 📦 v10 发布为 @videojs/react 和 @videojs/html；npm 上的 video.js 包仍为 v8。
- 🆓 仍为 Apache 2.0 免费开源；提供安装指南及从 Video.js v8、Mux Player、Media Chrome、Vidstack 迁移的指南。
- ❤️ 官方感谢团队和用户反馈，并邀请大家分享使用体验。

---

### [css-doodle — 使用 CSS 进行视觉艺术与创意编程](https://css-doodle.com/)

**原文标题**: [css-doodle â Visual art & creative coding with CSS](https://css-doodle.com/)

该内容介绍了一个面向视觉艺术与创意编程的 Web 组件，旨在将 CSS 提升为一种艺术表达语言，并提供入门指引与捐赠支持。
- 🎨 定位：用于视觉艺术与创意编程的 Web 组件
- 💻 核心理念：让 CSS 成为艺术创作语言
- 🚀 提供“Getting started”入门指南
- ❤️ 设有“Donate”捐赠入口

---

### [](https://css-doodle.com/discover)

**原文标题**: [Discover Â· css-doodle](https://css-doodle.com/discover)

这是一个以 yuanchuan 作品为主的创意代码与几何图案合集，包含发现、精选、热门、最新等浏览入口，主题涵盖分形、螺旋、对称、曲线、数学与生成艺术，并部分标注浏览器兼容性和热度/分页信息。

- 🧭 页面设有 Discover、Picks、Popular、Newest 等分类或筛选入口。
- 👤 绝大部分作品作者为 yuanchuan，呈现个人化的视觉实验合集。
- 🔷 作品主题包括 Triskelion pattern、Slicing grid、css-doodle shape、Multi-arm logarithmic vortex 等几何与生成图案。
- 🌌 也包含 Gloom、Swirl、Heart、Planet、Sunrise、Mandelbrot、Golden ratio、Fibonacci spiral 等自然、宇宙与数学灵感作品。
- 🖥️ 部分条目标注 Chrome Â· Firefox，说明存在浏览器兼容性提示。
- 🔢 一些作品带有 1、2 等数字，可能表示热度、票数或排序；结尾“1 2”更可能是分页。
- 🧪 其他内容包括 Mark Grotjahn, Untitled (1999)、Hyperbolic circles、Wavy lines、Fake 3d、Sunet、Bushes、Withe、Tiles、Hilbert curve、Lines、Symmetry 等实验性视觉。

---

### [](https://github.com/css-doodle/css-doodle/releases/tag/v0.55.0)

**原文标题**: [Release v0.55.0 · css-doodle/css-doodle · GitHub](https://github.com/css-doodle/css-doodle/releases/tag/v0.55.0)

css-doodle v0.55.0 发布，带来多种平铺类型、@pattern/@shaders 增强，同时包含破坏性变更、修复与内部优化。

- 🚀 v0.55.0 由 yuanchuan 发布，含 8 个提交合并至 main。
- 🧩 新增 @tile.circle、@tile.slice、@tile.cube、@tile.penrose、@tile.hex、@tile.triangle、@tile.delaunay，并可用 @tile.r/kind/x/y 读取单元格自身 tile。
- 🌐 新增 @tile.voronoi，支持 gap、points 和 seed。
- 🔲 新增 edge: 弯曲平铺边缘，shift: 实现 @tile.grid 行列砖块布局。
- 📈 @plot.scatter 新增 density 命令，并加速渲染、支持 fill: evenodd。
- 🎨 新增 squircle 与 cloud 形状预设，所有预设通过手调缩放适配盒子；修复 frame、bounds、星形等预设并移除 whale。
- ✨ @pattern 扩展：match {} 分支、纹理块、texture()/box()/segment()/ramp()/shape()、vec3 颜色与颜色名、// 注释、** 幂运算。
- 🔗 可在 @shaders 和 @pattern 主体中直接读取 $name，并传入单元格变量。
- ⚠️ 破坏性变更：平铺默认形状改为 slice 和 square，替代 voronoi；需显式 @tile.voronoi 保留旧外观。
- 🧹 破坏性变更：移除 @place 的 offset 别名与 viewBox padding 的 expand 别名。
- 🔧 其他变更：仅相邻值相乘，2 t 不再等于 2t；@row/@col/@depth 成为规范选择器名；更新时在已应用 sheet 重启动画；export() 仅嵌入自身 Google 字体；尺寸上限提至 200k。
- 🐛 修复：一元负号优先级、@R() 默认值、GLSL 双负号、百分号后缀、字符串中的 π、选择器注释、图像变量闪烁，以及 @t/@T 嵌套时钟。
- 🛠️ 修复：改进 @pattern 解析边界情况、嵌套图像缓存与 @svg-filter 共享；首帧用完整 sheet 渲染，并改善 shader 错误报告。
- 📦 内部：平铺与形状拆分为独立模块，简化计算；提升测试速度，精简 GLSL/esbuild 输出，删除死代码和解析缓存。

---

### [](https://github.com/viliket/pure-web-bottom-sheet)

**原文标题**: [GitHub - viliket/pure-web-bottom-sheet: A performant, lightweight, and accessible bottom sheet web component powered by CSS scroll snap and CSS scroll-driven animations. Works with any framework, supports SSR, multiple snap points, and nested scrolling mode. · GitHub](https://github.com/viliket/pure-web-bottom-sheet)

pure-web-bottom-sheet 是一个轻量、框架无关、可访问的底部面板 Web Component，基于 CSS scroll snap 与 CSS 滚动驱动动画实现原生般顺滑的交互，并支持 SSR、多吸附点与嵌套滚动。

- 🧩 核心机制：由浏览器原生滚动和 CSS scroll snapping 驱动面板移动，现代浏览器中核心功能几乎零 JavaScript，性能更佳。
- 🪄 关键特性：支持多个吸附点、嵌套滚动模式、内容高度自适应、展开后滚动、滑动关闭等能力。
- 🧱 框架无关：可用于原生 HTML，也提供 React、Vue、Astro 的封装与 SSR 支持。
- 📦 安装方式：通过 `npm install pure-web-bottom-sheet` 安装，并注册自定义元素即可使用。
- 🧩 主要组件：`<bottom-sheet>` 用于底部面板本体；`<bottom-sheet-dialog-manager>` 配合原生 `<dialog>` 实现模态对话框。
- 📌 槽位系统：默认内容槽、`header`、`footer`，以及 `snap` 槽位定义吸附点；`initial` 类可设置初始吸附点。
- ⚙️ 常用属性：`content-height`、`nested-scroll`、`nested-scroll-optimization`、`expand-to-scroll`、`swipe-to-dismiss`。
- 🎨 样式定制：提供 `--sheet-max-height`、`--sheet-background`、`--sheet-border-radius` 等 CSS 变量，以及 `sheet`、`handle`、`content`、`header`、`footer` 的 `::part` 选择器。
- 📣 事件与方法：`snap-position-change` 报告 `collapsed`、`partially-expanded`、`expanded` 状态；`snapToPoint(index, options)` 可滚动到指定吸附点。
- ♿ 可访问性：基于原生 Dialog 或 Popover API，支持触摸、键盘和鼠标滚动。
- 🌐 跨浏览器与 SSR：支持声明式 Shadow DOM 以减少初始打开时的 FOUC，已测试 Chrome、Safari、Firefox 桌面与移动端；最低要求 Safari 18.2+。
- 📄 项目状态：MIT 许可证，GitHub 约 126 stars、6 forks，欢迎贡献，并提供在线演示与技术文章链接。

---

### [](https://viliket.github.io/pure-web-bottom-sheet/)

**原文标题**: [Examples - pure-web-bottom-sheet](https://viliket.github.io/pure-web-bottom-sheet/)

本内容展示底部弹层组件的多种配置与使用场景，涵盖模态/非模态、嵌套对话框、动态内容、键盘避让、事件监听、程序化吸附及框架集成。
- 🚫 不可关闭底部弹层：支持多个吸附点
- 🪟 模态底部弹层：使用 dialog 实现，也可限制最大高度为视口一半
- 🧩 嵌套对话框：无额外样式，另有堆叠效果与背景缩放效果（额外样式）
- 🪶 非模态底部弹层：使用 Popover API，实现“纯 CSS”
- 💬 聊天场景：处理屏幕键盘避让
- 🔄 不可关闭底部弹层 + 动态内容：展示动态内容不会导致突然重新吸附
- 👂 模态底部弹层：监听吸附位置变化事件
- 📐 模态底部弹层：支持动态高度
- 🎯 程序化吸附：使用 snapToPoint()
- 📚 其他示例：React / Next.js 与 Vue / Nuxt 集成示例

---

### [](https://strich.io/?ref=frontend-focus)

**原文标题**: [STRICH | Barcode scanning for web apps](https://strich.io/?ref=frontend-focus)

STRICH 是面向 Web 应用的 JavaScript SDK，可在浏览器中通过摄像头实时扫描 1D/2D 条码；它完全客户端处理、无需后端，内置扫描 UI，兼容主流框架与浏览器，并提供免费试用及透明订阅/企业定价，适合将条码工作流迁移到 Web。

- 🧩 可通过 `npm i @pixelverse/strichjs-sdk` 安装，在 Web 应用中添加实时条码扫描功能。
- 📷 完全在客户端处理，无需后端；支持 Code 128、EAN、UPC、Code 39、ITF、QR、Data Matrix、Aztec、PDF417 等 1D/2D 码制。
- 🖥️ 内置扫描 UI，包含取景框、摄像头选择、闪光灯、点击对焦等；`PopupScanner.scan()` 可一行代码调用。
- ⚡ 基于 WebAssembly 和 WebGL，扫描速度快，兼容 Android/iOS 主流浏览器及高端、入门设备。
- 🧱 零依赖，支持 NPM/CDN，单文件含 TypeScript 类型绑定，兼容 Angular、Vue、React、SvelteKit 等框架。
- 🏆 针对褪色、损坏、光照不均、反色条码等困难场景，使用高级图像处理提升读取率，优于常见开源方案。
- 🌐 将条码流程放入 Web 应用可避开应用商店限制，通过链接/二维码分发，始终最新，降低成本并减少应用疲劳。
- 💬 客户评价普遍称赞其速度快、可靠性高、集成简单、文档优秀、支持及时、定价透明；用户包括 Thoughtbot、Brooklyn Public Library、SBB、Zeercle 等。
- 💰 Basic 为 €99/月，最多 1 万次扫描/月；Professional 为 €249/月，最多 10 万次扫描/月；均不限设备与应用，含更新和人工支持。
- 🏢 Business 起价 €4,000/年（1 个应用），扫描和设备不限，按应用数量计费；含自定义扫描 UI 品牌、离线许可检查、发票/银行转账。
- 🏭 Enterprise 按需报价，支持采购流程、SAP Ariba、经销商、OEM 授权及合理定制条款。
- 🔐 企业级支持包括定期更新、安全修复、创始人直接技术支持；可选离线操作，零网络流量，零依赖降低供应链风险。
- ✅ Pixelverse GmbH 是瑞士注册的 GS1 Solution Partner，支持并实施 GS1 标准。
- 🧪 超出套餐扫描限额不会立刻阻断扫描；连续两个月超限才要求 7 天内升级。
- 🆓 提供 14 天免费试用和免费演示应用，通常不到一天即可完成集成。

---

### [](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-sl1-txt)

**原文标题**: [Technology careers at Fidelity | Fidelity Careers](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-sl1-txt)

Fidelity 科技职业页面强调以创新重塑金融未来，结合初创心态与财富500强基础，持续投资创新并推动数字化未来；同时招聘技术人才，提供多个技术岗位、技能方向、每周专属学习时间及人才网络/职位提醒。

- 🚀 重新定义金融未来：推动有影响力的创新，打造明日科技，邀请加入并开启职业生涯。
- 🏢 初创心态 + 财富500强基础：承诺投资创新，兑现数字化未来。
- 📊 数据展示：呈现技术人才规模、2023年员工承担新/扩展角色比例及美国专利数量（原文数值以0占位）。
- 👩‍💻 员工体验：Monica（全栈工程师）表示，Fidelity 最棒的是人与人之间的互动。
- 💼 热门技术职位：数字资产交易工程师（Jersey City, NJ，现场）、首席软件工程师/开发者（Westlake, TX，现场）、数据工程总监（Durham, NC，现场）。
- 🔔 招聘方式：频繁发布新职位；若暂无合适岗位，可加入人才网络并订阅职位提醒。
- 🛠️ 所需技能：软件工程、全栈工程、云工程、数据可视化、人工智能与机器学习、架构、系统工程、系统分析。
- 📚 每周专属学习时间：技术人员可更新技能，如在线课程、职业辅导、导师影子学习等。
- 🔎 寻找技术理想职位：按技能和地点匹配，搜索职位。
- 🪙 更多信息：技术职业（职位类型、福利、播客）与加密职业（Fidelity 加密货币历史及招聘领域）。

---

### [](https://lab.ishadeed.com/tools/gradient-visualizer/)

**原文标题**: [Gradient Visualizer](https://lab.ishadeed.com/tools/gradient-visualizer/)

这组内容是一组界面操作控件，涵盖结果查看、重置、复制、CSS 编辑、延时播放、重新开始以及 1x/2x/3x 速度切换等功能。

- 📊 **Result**：查看或展示最终结果。
- 🔄 **Reset**：重置当前状态或设置。
- 📋 **Copy**：复制相关内容或代码。
- 🎨 **Edit CSS**：编辑 CSS 样式。
- ⏳ **Timelapse**：启用或查看延时/回放效果。
- 🔁 **Restart**：重新开始流程或动画。
- ⏩ **1x / 2x / 3x**：选择播放或运行速度。

---

