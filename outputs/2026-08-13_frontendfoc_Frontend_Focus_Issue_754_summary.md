### [99%的网站流量都是机器人 | PatronView](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/)

**原文标题**: [99% of My Website Traffic Is Bots | PatronView](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/)

这是一篇关于作者在 PatronView 网站（一个 150 万页的捐赠者数据库）上，与爬虫和恶意机器人斗争一年的深度复盘。文章揭示了 99% 的真实流量都是机器人，并详细记录了从国家封锁、AI 爬虫拦截到住宅代理机器人防御的完整过程，以及最终沉淀出的 Cloudflare 防火墙规则和经验总结。

- 📊 真实流量占比极低：网站服务器每服务 128 万个页面，仅有约 5,977 次人类浏览，即每 214 次机器人加载对应 1 次人类访问，真实流量不足 0.5%。
- 🌍 大规模地域性攻击：来自中国的机器人曾在一天内产生 360 万次请求（来自 36 万多个独立 IP），最终被迫封锁中国、越南、新加坡等地区。
- 🤖 SEO 爬虫频扰：SemrushBot、AhrefsBot、MJ12bot 等爬虫反复抓取全站，robots.txt 与 Cloudflare 规则只能部分缓解。
- 🤯 AI 爬虫引荐比极低：Claude-SearchBot 的爬取与引荐比为 35,000:1（仅带来 12 个访客却抓取 42 万页）；Amazon Amzn-SearchBot 每天抓取 11.7 万页但从未带来任何访客，因此被直接封锁。
- 🚫 封锁“礼貌”爬虫有效：Claude 和 Amazon 的爬虫在收到 403 后会停止，抓取量骤降至每天 25 次，说明遵守规则的 AI 公司可以沟通。
- 🏢 数据中心机器人攻击：AWS、Azure 上的无头 Chrome 伪装成真实访客，污染统计并消耗资源；通过挑战数据中心 ASN（如 AWS、Azure）成功遏制。
- 🛑 关闭 CAPTCHA 脚本的代价：禁用 Cloudflare JavaScript Detections 后，Lighthouse 评分从 58 升至 99，但随即遭遇 Azure 爬虫每小时 2.3 万页的攻击，暴露了安全功能的平衡难题。
- 🏠 住宅代理机器人顽固：来自美国家庭 IP（如 Spectrum）的机器人绕过地理和 ASN 规则，使用伪造的旧版浏览器 UA；通过挑战过期浏览器版本（Chrome 100-130、Firefox 100-124）来拦截。
- 📋 最终防火墙规则：包括封锁中越、封锁 SEO/AI 爬虫、验证真实搜索爬虫跳过、非北美地区挑战、空 UA 挑战、数据中心 ASN 挑战、旧浏览器挑战以及每 10 秒 30 次请求的速率限制。
- 💸 成本冲击巨大：常规服务器成本约每月 $90，但峰值月涨 500%；机器人消耗 99% 的资源，且统计工具被污染，导致业务决策受影响。
- 💡 核心经验：检查服务器日志而非仅看 JS 统计工具；按 ASN 而非 IP 封锁；使用 Managed Challenge 代替硬封锁以便衡量；监控挑战解决率（0.24% 表示机器人，30% 则误伤人类）。
- ⚔️ 结论与展望：规则有效（每天阻止约 4.6 万请求），但这是一场“打地鼠”游戏，根本解决方案是经济手段（如 Cloudflare 的 pay-per-crawl 按次付费爬取），原则是“不带来访客的爬虫一律封锁”。

---

### [5个你应该知道的CSS属性，打造更好的文本设计 – Master.dev博客](https://master.dev/blog/typographic-css-tricks/)

**原文标题**: [5 CSS Properties You Should Know for Better Text Designs – Master.dev Blog](https://master.dev/blog/typographic-css-tricks/)

概述：本文介绍了五个鲜为人知但实用的 CSS 属性，用于提升网页文字设计的视觉效果，从背景裁剪、垂直对齐、断行装饰到字距动画与竖排文本组合，每个属性都附有简洁示例，帮助设计师轻松实现更具吸引力的排版。

- 🎨 `background-clip: text`：用图片或渐变填充文字内部，打造醒目的字效，需配合透明文字颜色。
- 📐 `vertical-align`：用于对齐行内元素（如图标、图片）与文本的相对位置；真正的块级垂直居中则由 `align-content` 实现。
- 🧩 `box-decoration-break: clone`：让文本断行后每个片段边缘都保留边框、阴影和圆角，避免断口样式缺失。
- ✨ `letter-spacing`：可正可负调节字距，配合过渡动画能实现文字展开/收缩的揭示效果，甚至支持首字母特殊样式。
- 🀄 `text-combine-upright`：在竖排文本中让指定横向内容（如数字、缩写）合并直立显示，适合垂直排版场景。

---

### [](https://master.dev/courses/frontend-architecture/?utm_source=email&utm_medium=frontendfocus&utm_content=frontendcooper)

**原文标题**: [Architect Scalable Frontend Applications | Master.dev](https://master.dev/courses/frontend-architecture/?utm_source=email&utm_medium=frontendfocus&utm_content=frontendcooper)

概述
- 🏗️ 这是一门关于前端架构演进的课程，由 Staff 工程师 Maxi Ferreira 讲授，时长约 3 小时 32 分，涵盖从单体应用到微前端的完整路径。
- 📚 课程先建立软件架构基础，包括架构风格、质量属性、架构决策与逻辑组件四大支柱，帮助学习者理解和评估不同架构。
- 🧩 单体架构部分讲解如何用 C4 模型可视化系统，并通过子域划分、模块化、ESLint 边界规则和 Dependency Cruiser 来避免“大泥球”式代码。
- 📦 Monorepo 部分演示如何将单体拆分为多包工作区，使用 Turborepo 管理依赖、缓存与构建任务，并可视化包之间的依赖关系。
- 🔌 微前端部分介绍 iframe、Web Components、Module Federation 等多种实现方式，并展示如何在独立应用间进行路由代理、状态共享与运行时组合。
- ⚙️ Module Federation 相关练习涵盖异步加载、错误处理、远程组件引入、Nanostores 解耦状态，以及从 1.5 升级到 2.0 的配置方法。
- 🗂️ 课程还讨论微前端部署中的版本管理与服务发现模式，并总结何时应避免不必要的 Module Federation，因为其可能带来 CSS 冲突等复杂问题。
- 🎓 完成课程后可获得结业证书，适合希望从资深开发者走向架构方向的学习者。

---

### [](https://www.youtube.com/watch?v=uOtxiH3QiPg)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=uOtxiH3QiPg)

overview summary
YouTube 頁面底部提供各類常用連結，涵蓋公司資訊、合作選項、法律條款與平台運作說明，方便使用者了解服務內容與權益。

- 📄 簡介：提供 YouTube 平台基本介紹與背景資訊  
- 🎬 媒體：供新聞媒體或內容合作夥伴查詢相關資源  
- ⚖️ 著作權：說明版權規範與申訴機制，保障創作者權益  
- 📞 與我們聯絡：提供使用者與 YouTube 團隊聯繫的管道  
- 🎨 創作者：協助內容創作者使用平台工具與資源  
- 📢 廣告：提供廣告主投放廣告與行銷解決方案  
- 🧑‍💻 開發人員：開放 API 與開發者文件，支援技術整合  
- 📋 條款：列出服務條款與使用規範  
- 🔒 隱私權：說明個人資料收集與保護政策  
- 🛡️ 政策與安全性：宣導社群規範與安全使用守則  
- ⚙️ YouTube 運作方式：解釋平台推薦、審核與營運機制  
- 🧪 測試新功能：介紹正在實驗中的新功能與體驗計畫  
- ©️ 版權聲明：顯示 © 2026 Google LLC，確認所有權歸屬

---

### [](https://www.bram.us/2026/08/09/unlock-diagonal-scrolling-with-css-scroll-axis-lock-none/)

**原文标题**: [Unlock Immediate Diagonal Scrolling with CSS scroll-axis-lock: none – Bram.us](https://www.bram.us/2026/08/09/unlock-diagonal-scrolling-with-css-scroll-axis-lock-none/)

overview summary  
- 🖱️ 瀏覽器預設的「滾動軸鎖定」會忽略非主要軸向的微小滾動，讓手勢保持單一軸向，但有時會阻礙對角滾動。  
- 🎯 新的 CSS `scroll-axis-lock` 屬性可讓開發者控制此行為，設為 `none` 可停用鎖定，讓滾動完全跟隨使用者輸入。  
- 📜 屬性值 `auto` 為預設，瀏覽器可依手勢主軸決定是否鎖定；`none` 則完全取消鎖定，允許即時對角平移。  
- 💻 瀏覽器支援度：Chromium 153 已支援，Firefox 與 Safari 目前不支援。  
- 🔍 可安全作為漸進增強使用，無需特別偵測；若需要可用 `@supports` 或 `CSS.supports()` 檢查。  
- 🧪 文章提供互動示範，可實際比較鎖定與未鎖定時的滾動差異，並顯示「軸已鎖定」警示。  
- 🖼️ 在 Safari 上鎖定較嚴格，圓形滾動會變成「繪圖板」效果；Chrome 較貼近輸入但仍有部分鎖定。  
- 📱 觸控平台中，iOS Safari 幾乎不鎖定，Android Chrome 則會鎖定。

---

### [Etsy工程师如何在流量高峰时保持应用零崩溃 | Sentry](https://sentry.io/resources/etsy-workshop/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=ecommerce-fy27q3-etsyworkshop&utm_content=newsletter-sponsored-link-register)

**原文标题**: [How Etsy's Engineers Keep Their App Crash-Free During Traffic Spikes | Sentry](https://sentry.io/resources/etsy-workshop/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=ecommerce-fy27q3-etsyworkshop&utm_content=newsletter-sponsored-link-register)

概述：本文将介绍Etsy工程师如何在流量高峰期间保持应用无崩溃，包括备战、实时调试和衡量业务影响，并附有相关资源推荐。

- 📈 流量高峰崩溃不仅是技术问题，更是收入损失问题，Etsy在假日购物季尤其重视。
- 🛠️ 由Etsy的Jay Henry与Sentry的Sergiy Dybskiy联合分享备战高峰流量的实战经验。
- 🔍 工程团队会进行实时调试，快速定位并解决崩溃问题。
- 💰 重点衡量崩溃对业务的实际影响，以数据驱动优化决策。
- 📚 提供实战故事与可操作建议，源自Etsy真实高流量事件。
- ✅ 附有“监控关键电商体验”开发者清单，帮助系统化检查。
- 🎥 推荐阅读会话重放调试电商性能问题，以及监控修复关键用户体验的指南。

---

### [](https://www.smashingmagazine.com/2026/08/how-baseline-can-help-ship-less-javascript/)

**原文标题**: [How Baseline Can Help You Ship Less JavaScript — Smashing Magazine](https://www.smashingmagazine.com/2026/08/how-baseline-can-help-ship-less-javascript/)

本文介绍如何借助 Baseline 对前端依赖进行审计，识别并移除那些已被现代浏览器原生支持的 JavaScript 库，从而显著减小打包体积。

- 📊 Baseline 是 WebDX 项目，用于标记跨浏览器特性状态：Limited availability、Newly available、Widely available（全主流引擎支持满 30 个月即广泛可用）。
- ✅ 删除依赖前先问三个问题：该原生替代品对我的目标受众是否安全？替换成本如何？原生功能是否真正覆盖我的实际用例？
- 🌍 国际化集群：Intl.RelativeTimeFormat、Intl.NumberFormat、Intl.ListFormat、Intl.DurationFormat 可替代 timeago.js、pluralize、numeral 等库，约省 14KB gz；其中 DurationFormat 仅 Newly available，需留意受众。
- 🔄 HTTP 客户端：fetch + AbortSignal.timeout 可替代 axios 的基本 GET/POST，约省 17KB gz；但拦截器、自动重试、上传进度等仍需自行封装或保留库。
- 🖥️ UI 原语：<dialog> 元素替代模态框和 focus-trap，Popover API 替代浮层，CSS anchor positioning 替代 Popper 定位，三者合计约省 24KB gz，并带来更好的可访问性默认值。
- 🔧 Lodash 工具：Object.groupBy / Map.groupBy 替代 groupBy，structuredClone 替代 cloneDeep，Set 方法（union、intersection、difference 等）替代集合运算，约省 8KB gz；debounce/throttle 仍可保留。
- ⏳ Temporal 尚不宜替换：它仍处于 limited availability（Safari 未支持），官方 polyfill 约 44KB gz，换掉 dayjs 反而使 bundle 变大，建议等 Safari 稳定版和 Baseline。
- 📋 审计流程：用 `npm ls --omit=dev` 列出生产依赖，用 Bundlephobia 或 bundle analyzer 测体积，在 webstatus.dev 或 MDN 查 Baseline 状态，再套用三问题决策。
- 🛡️ 对 Newly available 特性，可采用特性检测加回退：`if (typeof Intl.DurationFormat === "function")`，让现代浏览器少加载代码，同时不破坏旧浏览器。
- 📉 典型中型应用可移除约 60–90KB gzipped 的依赖；若使用完整 lodash 或更重 UI 库，节省空间还会更大。
- 🔭 未来值得关注：Temporal 原生支持普及、CSS anchor positioning 迈向 Widely available、Object.groupBy 和 Set 方法在 2026 年底成为 Widely，将开启新一轮替换。
- 📅 建议每季度运行一次依赖审计，持续检查哪些库已可交还给平台，这应成为长期习惯。

---

### [](https://lea.verou.me/blog/2026/dark-mode-toggles/)

**原文标题**: [
		Dark mode toggles: two states are enough • Lea Verou](https://lea.verou.me/blog/2026/dark-mode-toggles/)

overview summary
文章批判了网站中常见的三态深色模式切换（Light/Dark/System），认为它是数据模型泄漏到 UI，不符合用户真实目标。作者主张用设计良好的两态切换表达三态：显示当前系统解析值，点击切换为相反值并存储覆盖，再次点击清除覆盖恢复系统默认。文章还讨论了三态切换合理的场景（设置面板、依赖系统设置的颜色方案），并提炼出通用设计原则：用户不会主动寻求解决当前不存在问题的方案。

- 🌗 三态切换（Light/Dark/System）虽然常见，但本质是面向底层数据模型的 UI，而非用户目标。
- 🎯 用户只有在网站太亮或太暗时才会操作切换；网站正常时，他们不会主动寻找主题开关。
- ❌ “System”状态对真实用户往往无意义，用户不需要为不存在的问题提前声明意图。
- ⚠️ 三态切换增加认知负荷、占用界面空间，并可能迫使设计采用更复杂或更低效的交互（如下拉菜单）。
- 🔄 好的两态切换可以表达所有三态：显示当前解析后的图标（如太阳/月亮），点击切换为相反值并存储；再次点击则清除存储，回到系统默认。
- 🚫 常见错误是存储了与系统默认匹配的值，导致用户无法退回系统模式；或在系统偏好变化时错误清除用户主动设定的覆盖。
- 🧠 存储值的评估只能在用户交互时进行；覆盖值与系统偏好偶然一致时，应保留，因为那是用户的显式选择。
- 🛠 用户偶尔会误操作或困惑，但修复只需一次点击，且概率极低，不值得为了预防它而永久增加 UI 复杂度。
- ✅ 三态切换的合理场景：位于独立设置面板中的主题选项（用户处于决策模式），或颜色方案本身会随系统设置产生不同表现时。
- 📏 通用原则：不要用与当前情境无关的选项淹没用户；未来可能相关的选项应在那时再出现。
- 💡 核心精神是尊重用户努力：界面只暴露与当前用户目标相关的状态，避免强迫用户决策无关问题。

---

### [](https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/)

**原文标题**: [HTML over WebSockets: real-time SPAs with barely any JavaScript | Andros Fenollosa](https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/)

overview summary  
- 🧩 介绍“HTML over WebSockets”这一架构：服务器直接发送已渲染的 HTML，而非 JSON，客户端只负责放置内容，从而以极少的 JavaScript 构建实时 SPA。  
- 🌐 对比三种传输方式：HTTP（htmx）、SSE（Datastar）、WebSocket（Phoenix LiveView / Django LiveView），强调通道决定架构与通信模式。  
- 💡 起源：Chris McCord 在 ElixirConf 2019 展示 Phoenix LiveView，15 分钟构建实时 Twitter 克隆，推动该模式跨语言普及。  
- ⚙️ 工作原理：浏览器与服务器建立 WebSocket 持久连接；客户端发送文本请求，服务器查询数据库、用模板渲染 HTML 并推送；客户端只需将 HTML 插入对应位置。  
- ✔️ 优点：单一渲染引擎、无需 API、服务端保存状态、直接访问数据库、真正的实时推送、支持广播、减少流量与延迟、可构建轻量 SPA、SEO 友好、天然防 XSS 注入。  
- ❌ 缺点：服务器资源占用高（需保持连接和状态）、横向扩展复杂、高延迟下体验下降、离线不可用、学习曲线较陡。  
- 🛠️ 框架生态：Phoenix LiveView、Hotwire、Django LiveView、Blazor、Livewire、htmx、Datastar 等，覆盖多种语言与传输方式。  
- 💰 SSE 是低成本替代：仅需服务器到客户端的单向推送，基础设施简单、易扩展；但无法双向通信、仅支持文本，不适合聊天或协作编辑等重双向场景。  
- 🧭 选型建议：需要双向低延迟（聊天、协作、游戏）选 WebSocket；仅服务端推送选 SSE；普通请求-响应用 htmx over HTTP。  
- 🎯 核心思想：用 HTML 代替 JSON，留在单一语言，去掉 API、契约和一半前端复杂度；信任好的架构而非追逐潮流。

---

### [](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

**原文标题**: [
      Your SPA Is Leaking Memory. Soak Test It — Den Odell
    ](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

这篇文章介绍了单页应用（SPA）内存泄漏的严重性，并详细说明了如何通过前端浸泡测试（soak test）来检测和预防问题。作者基于 Playwright 给出了具体实现方案，涵盖指标采集、虚拟时钟与网络模拟等关键技术，并发布了现成的测试工具。

- 🧠 SPA 因页面从不重载，内存泄漏会不断累积，最终导致标签页崩溃，因此需要像后端一样进行浸泡测试。
- 📊 2026 年初针对 500 个流行 React/Vue/Angular 仓库的静态分析发现，86% 存在未清理的监听器、定时器或订阅。
- 🔁 浸泡测试核心：在同一浏览器上下文中将用户流程重复数百次，并测量流程开始与结束时的内存指标。
- 📈 通过 Chrome DevTools 协议（CDP）获取内存数据，先执行两次垃圾回收，再读取 JS 堆大小、DOM 节点数和监听器数。
- ⏱️ 测试需要先运行少量预热循环（如 5 次），避免首次加载代码和数据导致的内存增长误报。
- 🎯 断言主要关注 DOM 节点数和监听器数而非堆大小，因为堆大小波动较大，节点数可用固定容差（如 100）判断。
- ⏰ 使用 `page.clock` 虚拟时钟加速测试，配合网络模拟（如 `page.route` 和 `page.routeWebSocket`），在几分钟内模拟数小时的真实使用。
- 🔌 对轮询定时器场景，必须同时模拟网络响应并确保响应大小与生产接近，否则会严重低估实际泄漏规模。
- 🧰 作者已将上述逻辑封装为 `playwright-soak-test` fixture，可通过 npm 安装后直接复用。
- 🛠️ 定位泄漏源时，可在 Chrome DevTools 的 Memory 面板拍摄堆快照，并使用 "Detached" 过滤器查看被遗弃但仍有引用的 DOM 节点。
- 📚 文章最后推广作者的新书《Fast by Default: Practical Performance Engineering》，强调性能问题应由团队共同负责并提前预防。

---

### [](https://tylersticka.com/journal/improved-css-text-stroke/)

**原文标题**: [Improved CSS Text-Stroke â Tyler Sticka](https://tylersticka.com/journal/improved-css-text-stroke/)

长期以来，CSS 文字外描边因居中覆盖而影响可读性，但如今借助 `paint-order` 属性可将描边置于文字下方，显著改善效果。

- 🎨 过去所有主流浏览器仅支持带前缀的 `-webkit-text-stroke` 系列属性，且描边默认居中，导致粗描边覆盖文字、破坏辨识度。
- 😖 厚描边会侵入字形内部，在可变字体上问题更严重（如 Mona Sans 的 issue 与 Stack Overflow 上的讨论）。
- 🛠️ 设计师曾用多种变通方案：四向 text-shadow（Chris Coyier, 2010）、复制文字并在底层加描边（James Nowland, 2015）、使用 SVG filter（Dudley Storey, 2016）。
- ✅ 2024 年起 Chromium 已支持 `paint-order` 属性（此前 WebKit 与 Gecko 早已支持），可让描边绘制在文字填充下方，保持文字清晰。
- ✨ 示例：`paint-order: stroke fill; -webkit-text-stroke: 0.125em white;` 即可实现不遮挡字形的外描边。
- ⚠️ 仍有不足：描边可能产生尖锐角，缺少 `stroke-linejoin` 与 `stroke-miterlimit`；Firefox 中描边形状更圆润；`text-shadow` 会绘制在描边上方，需改用 `drop-shadow` 滤镜。
- 🕰️ 近二十年后仍需写 `-webkit-` 前缀，略显尴尬，但该实用技巧值得分享。

---

### [](https://spatie.be/blog/can-we-make-default-tailwind-a-more-accessible-choice)

**原文标题**: [Can we make default tailwind a more accessible choice? | Spatie](https://spatie.be/blog/can-we-make-default-tailwind-a-more-accessible-choice)

本文探讨了 Tailwind CSS 默认断点使用 `rem` 单位在可访问性上的权衡。作者通过实际案例说明，用户修改浏览器默认字号会移动 `rem` 断点并影响布局，而 `px` 断点不会；文章解析了相关规范、对比两种做法的利弊，并指出真正的关键在于是否有意识地做出选择。

- 🖥️ 作者遇到难以复现的布局错乱，最终发现是用户调大了浏览器默认字号，导致 Tailwind 的 `rem` 断点随之缩放，在未测试的视口宽度下触发了不同的布局。
- 📏 Tailwind 自 v3.2 起默认断点使用 `rem`（`sm: 40rem`、`md: 48rem` 等），注释中的像素值只是按 16px 换算的参考。
- 🔬 媒体查询中的 `rem` 不会响应作者 CSS 的 `html { font-size }`，而是根据规范基于“初始值”解析；但用户可以通过浏览器设置修改该初始值，从而移动这些断点。
- 🎯 三种操作对比：用户设置默认字号会同时缩放 `rem` 文本和 `rem` 断点，但 `px` 断点不变；页面缩放会缩放一切；作者设置 `html` 字号只影响文本，不影响断点。
- ✅ 使用 `rem` 断点能让需要更大默认字号的用户获得更宽的布局，避免文本被挤在固定宽度里，这是超越 WCAG 基本要求的可访问性提升。
- ⚠️ 但这也带来不可预测性：布局切换的临界点取决于用户隐藏的字体设置，难以测试和复现，可能导致卡片溢出、组件库内部断点异常等问题。
- ♿ WCAG 1.4.4 并未强制使用 `rem` 断点，页面缩放可以满足文本放大 200% 的要求，因此 `px` 断点不违反标准；`rem` 是额外的加分项，而非底线。
- 🛠️ 若想改用 `px` 断点，Tailwind v4 可通过 `@theme` 覆盖 `--breakpoint-*`，v3 可在 `tailwind.config.js` 的 `screens` 中直接指定像素值。
- 🤔 核心问题并非哪个单位“正确”，而是你是否清楚默认值背后的取舍：`rem` 更响应文本偏好但不够可控，`px` 更可预测但依赖页面缩放；选择应基于实际用户和有意识的决策。

---

### [](https://guillaumetech.github.io/posts/jpg-scaling-chrome/)

**原文标题**: [Guillaume Técher](https://guillaumetech.github.io/posts/jpg-scaling-chrome/)

概述：Chrome 在渲染小尺寸 JPEG 时，并未完整解码再缩放，而是采用“部分 IDCT 缩放”优化，跳过高频系数，只保留低频信息，导致图片在小尺寸下显得更粗/更厚。这种优化与 Firefox 等浏览器不同，因此出现渲染差异。

- 🖼️ 发现现象：同事电脑上的同一张 Logo 在 Chrome 中看起来更粗，Firefox 中更接近原图，换用 SVG 可解决。
- 🔍 最初怀疑是渲染 bug，后证实是 Chrome 的 JPEG 解码优化所致。
- 📉 完整解压大图再缩放到小尺寸很浪费：2000×2000 解压约 12 MB，而 20×20 只需约 1.2 KB。
- 🌲 缩小图片时，丢失的主要是高频细节（如树叶、树皮的纹理），低频信息（整体颜色和形状）保留下来。
- 🧩 JPEG 将图像分为 8×8 块，通过 DCT 转换为频率域，低频是纯色，高频是棋盘格模式。
- ⚡ 按 1/8 缩放时，每个 8×8 块只需一个像素，因此可跳过高频系数，仅用低频数据解码，节省内存和计算。
- 🔧 Chrome 使用 Skia + libjpeg-turbo，在目标尺寸较小时自动执行部分 IDCT 缩放，再配合传统下采样算法达到最终尺寸。
- ⚠️ 实际效果受 IDCT 缩放和后续缩放算法共同影响，并非单一原因。
- 🚫 结论：不适合用 JPEG 做图标等小尺寸图像，JPEG 是为照片感知设计的格式。

---

### [TermDOM | 使用HTML、CSS和DOM构建终端UI](https://termdom.org/)

**原文标题**: [TermDOM | Build Terminal UIs with HTML, CSS and DOM](https://termdom.org/)

TermDOM 是一个 JavaScript 库，它将 HTML、CSS 和 DOM 渲染到终端中，让开发者能用 familiar 的 Web 技术编写 TUI 和交互式 CLI，并自动响应 DOM 变更。

- 📦 安装：通过 `npm install @b9g/termdom` 获取，提供真实 DOM、级联样式和布局引擎，输出到终端。
- 🔄 核心机制：使用真实 DOM 文档，通过 MutationObserver 等自动重绘，支持纯 JS 或前端框架。
- 🖥️ 示例展示：用 HTML/CSS 定义卡片界面，`setInterval` 更新进度条文本，无需手动调用渲染。
- ✨ 元素即字形：每个字符都是 DOM 元素，改变 `textContent` 即自动绘制，如旋转的 spinner。
- ⌨️ 事件交互：支持 `keydown` 等 DOM 事件，可用 `querySelectorAll` 和 `classList` 构建文件浏览器，`scrollIntoView` 移动视角。
- 📝 文本输入：真正的 `<input>` 元素、真实光标和 :focus 样式，支持 CJK 输入法组合，按单元格度量。
- 🎨 样式与布局：CSS 级联继承，支持盒子模型、flexbox 和表格布局，尺寸对齐到整单元格。
- 🌐 文本处理：正确处理 CJK、emoji、组合字符宽度，希伯来文/阿拉伯文按视觉顺序显示，光标按字素移动。
- 📜 滚动与事件：文档可滚动，支持 `window.scrollTo()`；键盘、鼠标、焦点、粘贴事件来自 STDIN。
- 🧰 DOM 工具：实现 `querySelector`、MutationObserver、ResizeObserver、`getBoundingClientRect` 等标准 API。
- 🎛️ 表单控件：内置 `<input>`、`<textarea>`、`<select>`、复选框和单选钮，带默认行为和终端原生外观，可用 CSS 重绘。
- 🧩 Web 组件：支持 `customElements.define`、`attachShadow`、`<slot>`、`:host` 和作用域样式。
- 🖱️ 选择与全屏：支持拖选并用 `::selection` 样式；`requestFullscreen` 渲染到备用屏幕，退出时恢复 shell。
- ✅ 兼容性测试：通过探针套件对每个 DOM API、选择器和 CSS 属性进行实际渲染，生成兼容性矩阵。
- 📚 入门资源：提供指南链接和 GitHub 示例；名称与 DomTerm 相反，DomTerm 把终端放进 DOM，TermDOM 把 DOM 放进终端。

---

### [](https://crank.js.org/)

**原文标题**: [Crank.js](https://crank.js.org/)

overview summary
Crank.js 是一个强调“纯 JavaScript”的 UI 框架，允许开发者用普通函数、生成器和异步函数定义组件，支持 JSX 或模板标签，并提供声明式、可预测、对 Promise 友好的开发体验，同时附带相关博客文章与资源。

- ⚡️ Crank.js 是一个 JavaScript/TypeScript UI 库，组件由普通 JavaScript 函数、生成器和 Promise 定义，真正践行“Just JavaScript”理念。
- 🧩 支持 JSX 和 tagged template 两种写法，开发者可以自由选择更接近原生 JavaScript 的方式。
- 🔁 使用生成器函数定义有状态组件，通过 `yield` 保持状态，并借助 `this.refresh()` 显式触发更新，行为可预测，无需记忆化回调。
- 🌐 任何组件都可声明为 `async` 函数，直接 `await fetch()` 等异步操作，简化客户端和服务端数据加载。
- 🔄 异步生成器组件可同时处理异步和状态逻辑，配合 `Suspense` 实现加载态、竞态等高级场景。
- 🧹 组件支持清理逻辑，如清除定时器，避免内存泄漏，代码结构清晰。
- 📚 博客文章涵盖 Crank.py 介绍、响应式框架反思、从零构建 Crank.js 以及框架设计初衷等深度内容。
- 🎯 核心理念是减少框架集成代码，让开发者专注于编写原生 JavaScript，提升开发效率。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Cloud（Tiger Data）提供基于 Postgres 的时序数据解决方案，支持从千万亿级数据点到企业级安全合规的大规模场景，并强调弹性架构、可观测性与快速部署，同时为新用户提供试用额度。

- 📊 支持每天 3 万亿指标、3 PB 数据、1000 万亿数据点的大规模时序负载。
- 🎁 新账户可获 $1000 信用额度，有效期 30 天，无需信用卡。
- 🏭 深受数千家 IoT 公司信赖。
- ⚡ 轻松扩展：读写分离，副本集最多 10 节点，SSD/S3 分层存储降低成本。
- 💸 避免闲置容量：计算与存储解耦，可独立扩展并优化成本。
- 🔁 高可用性：多可用区集群、自动故障转移、时间点恢复及跨区域备份。
- 🛡️ 企业级合规：SOC 2、HIPAA、GDPR，全时加密、SSO、RBAC 与审计日志。
- 🔍 深度可观测：查询下钻与仪表盘，支持发送指标至 CloudWatch、Datadog、Prometheus。
- 🚀 快速启动：数分钟内部署，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 生态集成：可接入主流云平台及 Postgres 生态系统。
- 🏅 企业默认就绪：合同化 SLA、区域数据隔离、全球 24/7 专家支持。

---

### [获取失败](https://www.w3.org/WAI/eval/report-tool/)

**原文标题**: [Failed to retrieve](https://www.w3.org/WAI/eval/report-tool/)

无法总结：获取内容失败，状态码 403。

---

### [获取失败](https://www.w3.org/TR/WCAG-EM/)

**原文标题**: [Failed to retrieve](https://www.w3.org/TR/WCAG-EM/)

无法总结：获取内容失败，状态码 403。

---

### [](https://github.com/GoogleChromeLabs/use-webmcp-tool)

**原文标题**: [GitHub - GoogleChromeLabs/use-webmcp-tool · GitHub](https://github.com/GoogleChromeLabs/use-webmcp-tool)

use-webmcp-tool 是 Google Chrome Labs 维护的一个 React Hook，用于将 WebMCP 工具注册与组件生命周期绑定，让 AI 代理能发现并调用页面暴露的功能，并在浏览器不支持该实验性 API 时自动降级为无操作。

- 📦 安装：通过 `npm install use-webmcp-tool` 安装，要求 React 18+，纯 ESM，内置 TypeScript 类型，无运行时依赖。
- 🧩 核心功能：把页面的 JavaScript 函数注册为“工具”，供 AI 代理（浏览器内置、iframe 或扩展）调用，替代 DOM 抓取。
- 🔄 生命周期管理：组件挂载时自动注册，卸载时自动注销，确保代理看到的工具集与实际屏幕内容同步。
- 🛡️ 特性检测：基于当前 WebMCP 规范构建，在缺少 `document.modelContext` 的环境下安全降级为 no-op。
- 📝 使用方式：`useWebMCP` 接收 `name`、`description`、`execute` 等配置，返回 `supported`、`registered`、`error` 状态。
- 🔧 返回值规范化：自动将字符串、对象、Error、抛出值等统一转换为 MCP 标准格式，失败结果绝不伪装成成功。
- 🧪 测试覆盖：21 个测试，涵盖注册/注销生命周期、StrictMode、重注册条件及完整的返回结果规范化矩阵。
- 📄 许可证：Apache-2.0，并附带贡献指南。

---

### [](https://developer.chrome.com/docs/ai/webmcp)

**原文标题**: [WebMCP  |  AI on Chrome  |  Chrome for Developers](https://developer.chrome.com/docs/ai/webmcp)

overview summary  
WebMCP是一项提议中的网络标准，旨在通过向AI代理提供结构化的JavaScript工具和HTML表单注解，让代理更精准地执行操作（模拟鼠标点击和文本输入），从而提升任务完成效率与可靠性。它支持工具发现、JSON Schema定义和页面状态共享，可通过命令式或声明式API集成，并设有来源隔离与权限策略保障安全。目前处于开发与试验阶段，已有演示和反馈渠道。

- 🔧 WebMCP是提出的网络标准，帮助构建和暴露供AI代理使用的结构化工具，提升代理操作（actuation）的准确性与可靠性。
- 🖱️ 它通过JavaScript和HTML表单注解，让代理明确知晓如何与页面功能交互，替代以往依赖代理自行解析DOM的不稳定方式。
- 🔍 支持三大能力：发现（工具向代理注册）、JSON Schema（定义输入输出减少误解）、状态（共享当前页面上下文）。
- 📝 提供命令式API（标准JavaScript定义工具）和声明式API（HTML表单注解）两种集成方式，Angular已有实验性支持。
- 💬 典型应用场景包括客户支持表单填写、复杂的多城市旅行预订、日期选择、应用调试等。
- ⚠️ 目前存在限制：主要针对本地浏览器工作流，复杂界面需重构，且工具可发现性依赖代理直接访问站点。
- 🔒 安全方面，API受来源隔离（origin isolation）和权限策略（Permissions Policy）双重限制，跨源iframe需显式允许。
- 🧪 已提供多个演示（如zaMaker、旅行演示、小餐馆演示）及模型上下文工具检查器扩展用于测试和调试。
- 📣 WebMCP仍在积极讨论和演进中，欢迎通过GitHub、Chrome Status、Origin Trial等渠道参与反馈。

---

### [morphicons — 用于 React、Vue 和 Svelte 的 SVG 图标变形库](https://www.morphicons.com/)

**原文标题**: [morphicons — SVG icon morphing library for React, Vue & Svelte](https://www.morphicons.com/)

overview summary
Morphicons 是一个轻量级图标变形动画库，可让任意 stroke 风格 SVG 图标（如 Lucide、Tabler、Heroicons 等）互相平滑过渡；它用闭式解计算最优旋转，并结合弹簧物理实现可中断动画，核心不依赖 DOM，且零运行时依赖。

- 🧩 支持在 Lucide、Tabler、Heroicons 等任意 stroke 图标集之间互相变形，统一基于 24×24 网格。
- ⚙️ 通过闭式 2D Procrustes 求解最优相似变换：同构图标自动旋转，不同构图标则在对齐框架内变形。
- 🔄 内置 spring、smooth、snappy、bouncy 等多种动画预设，弹簧可中断，静止时尖角保持清晰。
- 📦 核心仅 6.5 KB（gzip），运行时依赖为 0，规划任意变形对耗时 <1 ms。
- 🖥️ 支持 React、Vue、Svelte、React Native、Next.js 及原生 JavaScript，所有图标共享同一个 rAF 循环。
- 📊 图标以数据而非组件形式传入（如 `d` 属性或 Lucide 的 `IconNode`），无需适配器或额外配置。
- 🎯 使用方式极简：只需 `<MorphIcon icon={open ? X : Menu} />` 即可完成切换动画。
- 🧰 还支持通过 `fitIcon` 适配任意网格的 stroke 图标集，并兼容 shadcn registry 等生态。

---

### [点阵](https://dotmatrix.zzzzshawn.cloud/)

**原文标题**: [Dot Matrix](https://dotmatrix.zzzzshawn.cloud/)

这是一个提供 55+ 免费开源加载动画的集合，名为 Dot Matrix Loaders，基于 React、TypeScript、Tailwind CSS 和 shadcn 构建。每个加载器都可以通过命令安装，复制代码即可使用和自定义，包含多种风格，并有 Playground 与 Showcase 供预览。

- 🎯 为每个应用设计的点阵加载动画集合，内容丰富。
- 🚀 通过 npx shadcn@latest add @dotmatrix/dotm-square-3 即可快速安装。
- 🛠️ 支持手动设置，方便按需配置项目环境。
- 🧩 基于 React、TypeScript、Tailwind CSS 和 shadcn 构建，技术栈现代。
- 💎 55+ 免费开源加载器，可随意复制代码并改造成自己的风格。
- 🎨 包含多种视觉样式，如 Neon Drift、Pulse Ladder、Core Spiral、Twin Orbit、Prism Sweep 等。
- 🌐 提供 Playground 和 Showcase，便于预览与挑选合适的加载动画。

---

### [](https://github.com/zzzzshawn/matrix)

**原文标题**: [GitHub - zzzzshawn/matrix · GitHub](https://github.com/zzzzshawn/matrix)

这是一个可复用的点阵式加载动画库，支持通过 shadcn registry 安装或手动复制源码使用，并附带一个基于 Next.js 的文档站点。项目结构清晰，提供常用开发命令，并支持发布到 shadcn 官方目录。

- 🎯 提供两种使用路径：主要推荐通过 shadcn registry 安装，次要方式是从文档手动复制源码。
- 🗂️ 采用单一 Next.js 应用布局：加载器组件位于 `loaders/`，应用路由位于 `app/`，注册表数据由 `registry.json` 和 `public/r/` 生成。
- ⚙️ 核心命令：`pnpm dev` 运行文档应用，`pnpm registry:build` 生成注册表文件，`pnpm test` 执行测试，`pnpm typecheck` 进行 TypeScript 类型检查。
- 🌐 构建时可通过 `REGISTRY_HOMEPAGE` 环境变量覆盖注册表元数据中的主页，默认值为 `https://dotmatrix.zzzzshawn.cloud`。
- 📋 若要被 shadcn 官方目录收录，需要在 `shadcn-ui/ui` 仓库的 fork 中额外编辑 `apps/v4/registry/directory.json` 和 `apps/v4/public/r/registries.json`。
- ⭐ 当前仓库拥有 543 个 Star、28 个 Fork、61 个提交，并包含 1 个 Issue 和 1 个 Pull Request。

---

### [关键CSS生成器 - Kigo工作室](https://kigo.studio/tools/critical-css-generator)

**原文标题**: [Critical CSS Generator - Kigo Studio](https://kigo.studio/tools/critical-css-generator)

Kigo Studio 提供 Critical CSS 生成工具，可提取首屏所需的最小 CSS，以提升页面速度、Core Web Vitals 与搜索排名；工具支持自订视口、等待时间及 JS 阻塞设定，并附有明确的实施步骤与 FAQ。

- 🚀 工具用途：生成首屏关键 CSS，减少渲染阻塞，加速页面显示并改善 SEO 与用户体验。
- ⚙️ 生成设定：可输入网址、视口宽高、渲染等待时间，并选择是否阻止 JS/动画，然后点击生成。
- 📄 步骤一：将生成的 CSS 放入 HTML `<head>` 内的 `<style>` 标签，置于其他样式表或阻塞脚本之前。
- 🔗 步骤二（简易）：将非关键 CSS 的 `<link>` 移到 `</body>` 前，并从 `<head>` 移除原链接。
- 📜 步骤三（进阶）：用 `DOMContentLoaded` 事件配合 JavaScript，在页面内容加载后动态追加非关键样式表。
- ❓ FAQ 摘要：关键 CSS 是首屏渲染所需的最小样式；工具藉由无头浏览器分析可见元素并抽取样式。
- 💡 效益说明：加快 FCP/LCP、提高 Core Web Vitals 分数、优化移动端与慢速网络体验。

---

### [](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/agentic-document-workflows/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260812)

**原文标题**: [Agentic Document Workflows with LLM Agents and PDF APIs](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/agentic-document-workflows/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260812)

overview summary  
此指南說明如何在 Power Automate 中，僅透過 HTTP 動作與 Webhook，串接 Foxit REST API，實現從 CRM 成交觸發 Word 轉 PDF、電子簽名流程及自動歸檔的完整自動化。

- 📄 從 CRM 成交狀態觸發，自動將 Word 合約轉換為 PDF 文件。  
- ✍️ 透過 Foxit 的 eSign API，將產生的 PDF 路由給相關人員進行電子簽名。  
- 📦 簽名完成後，利用 Webhook 自動將已簽署副本歸檔儲存。  
- 🔗 整個流程僅使用 Power Automate 的 HTTP 動作，無需額外自訂程式碼。  
- ⚡ 此方案提供輕量、可擴展的合約自動化範例，適合 CRM 與文件簽核整合場景。

---

### [](https://css.graphics/pipes/)

**原文标题**: [css.graphics/pipes](https://css.graphics/pipes/)

提供的内容“css.graphics /pipes”仅为一个网址，没有附带具体正文。根据其结构可推测，它指向css.graphics站点下的“pipes”相关页面，很可能涉及CSS图形绘制或管道视觉效果。由于信息有限，以下为基于该关键词组合的要点总结：

- 🌐 “css.graphics”是一个以CSS图形为主题的网站域名
- 📁 路径“/pipes”很可能代表该站点下的“管道”专题或页面
- 🖌️ 内容或与使用纯CSS绘制管道、连线等图形有关
- 🔧 也可能借用“管道”概念，说明样式或图形数据的传递流程
- ⚠️ 仅凭该链接无法获取文章详细内容，需访问页面才能进一步了解

---

### [](https://devblogs.microsoft.com/oldnewthing/20240611-00/?p=109881)

**原文标题**: [The origin story of the Windows 3D Pipes screen saver - The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20240611-00/?p=109881)

这篇文章讲述了Windows 3D Pipes屏幕保护程序的起源故事，源于一位OpenGL团队成员为展示硬件加速OpenGL功能而发起的内部屏保创作比赛，最终因营销团队的青睐而全部被纳入Windows NT。

- 🏆 Gizmodo将3D Pipes誉为“有史以来最好的屏幕保护程序”。
- 💡 故事由一位Windows OpenGL团队的成员亲口讲述。
- 🚀 OpenGL硬件加速已经实现，但Windows NT 3.5中缺乏让用户感知此功能的方式。
- 🖥️ 他选择用屏幕保护程序作为低风险宣传手段，即使出错也可让用户直接停用。
- 📢 团队举办了屏保写作大赛，获胜作品将被加入Windows NT。
- 🎨 参赛作品包括3D Text、3D Maze、3D Flying Objects以及3D Pipes。
- 📧 整个Windows NT团队通过邮件参与投票，营销团队也意外看到并试用了这些屏保。
- ✅ 营销团队在杂志拜访前夜决定取消投票，将全部3D屏保直接加入产品。
- 🌐 如今可在浏览器中运行3D Pipes的重建版本，重温怀旧体验。
- ⚠️ 评论区还提到这些屏保在服务器上会大量占用CPU，曾导致系统故障和业务中断。

---

### [](https://github.com/layoutit/cssGraphics)

**原文标题**: [GitHub - layoutit/cssGraphics: A DOM-ready 3D asset library powered by PolyCSS. · GitHub](https://github.com/layoutit/cssGraphics)

cssGraphics 是一个基于 PolyCSS 引擎的 3D 资产库，将动画和交互式 3D 模型渲染为纯 HTML/CSS，无需 WebGL 或 canvas。它包含多个针对经典 XScreenSaver 等场景的适配器，通过预生成数据与静态 DOM 实现运行时零几何构建和低开销。

- 🎨 核心特性：使用 PolyCSS 引擎，将 3D 模型呈现为真实 HTML/CSS，不依赖 WebGL/canvas 渲染器。
- 🚀 本地运行：执行 `pnpm install` 和 `pnpm dev` 即可启动开发环境。
- 🧩 适配器集合：内置 3D Pipes、Flower Box、Gears、Menger、Maze 等多个场景。
- 🌸 Flower Box：以 1,200 个稳定三角形叶片和哈希绑定的 q60 空间纹理光照图重建经典 Flower Box。
- ⚙️ Gears：源自 XScreenSaver Gears，24 组三齿轮装配体按序进出，浏览器仅保留 3 个齿轮根节点，运行时无几何/光照/DOM 构建。
- 🧊 Menger：将 18,048 个源面合并为 84 个共面平面束，采用预生成的 1,536 状态循环，运行时无递归、合并或光照计算。
- 🌀 Maze：从 24 个低旋转种子迷宫中加载预生成快照，运行时无迷宫生成、路径求解或几何构建。
- 📄 许可证：核心与包为 MIT 许可，各适配器保留自身条款；ElectroPaint 适配器非 MIT，需查看其本地许可。
- 📚 模型归属：目录模型归属信息位于 `site/public/catalog.json`。

---

### [错误](https://github.com/LayoutitStudio/polycss)

**原文标题**: [Error](https://github.com/LayoutitStudio/polycss)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /LayoutitStudio/polycss (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

