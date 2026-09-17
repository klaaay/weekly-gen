### [往昔的 CSS 奇趣 | Vale.Rocks](https://vale.rocks/posts/css-relics)

**原文标题**: [CSS Curiosities of the Past | Vale.Rocks](https://vale.rocks/posts/css-relics)

本文回顾了 CSS 发展史中大量非标准、浏览器专属和 hack 式用法，重点涉及 Internet Explorer 的解析怪癖、布局修复、滤镜、表达式、HTML 组件与厂商前缀，说明这些做法如何被用于兼容旧浏览器，并最终随标准化和浏览器更新而退出历史舞台。
- 📜 文章将 CSS 视为曾被迫承担额外角色的技术，梳理规范之外的浏览器 hack、技术限定语法和引擎专属片段。
- ⭐ 早期用属性前缀区分浏览器：`*width` 只被 IE7 及更早识别，`_width`/`-width` 只被 IE6 识别，称为 star hack 等。
- ❗ IE7 及更早会把 `!interesting`、`!ie` 等任意感叹号字符串当作 `!important`；IE6 及更低还有 `!important` 被后声明覆盖的 bug。
- 🧭 文档级浏览器检测：`* html {}`、`*:first-child+html {}`、`html > /**/ body {}`、`body:empty {}` 等分别用于定位旧 IE 或早期 Firefox。
- 🧹 Clearfix 依赖 IE 的 `hasLayout`：`zoom:1` 可触发布局，避免浮动子元素导致父容器塌陷。
- 🖱️ IE6 之前不支持 `cursor:pointer`，只支持非标准 `cursor:hand`，因此常见同时写两者。
- 🧮 CSS 表达式/Dynamic Properties：IE5 起可在 CSS 中执行 JS，如 `expression(eval(...))` 模拟固定定位或 min/max-width，但反复求值、性能很差，IE8 终止支持。
- 🎛️ IE 滤镜：用 `filter: alpha(...)`、`AlphaImageLoader`、`gradient` 等 DirectX 组件处理透明度、透明 PNG 与渐变；语法随版本变化，IE10 移除。
- 📜 IE5.5 起支持 `scrollbar-*-color` 定制滚动条，常被 MySpace 等个人页面大量使用。
- 🧩 HTML Components：IE5/5.5 通过 `behavior:url(.htc)` 在 CSS 中挂接脚本，常用 JScript 模拟 `:hover` 等，IE10 移除。
- 📦 Box Model Hack：Tantek Çelik 利用 `voice-family` 解析 bug，让 IE5/5.5 与标准浏览器各自得到正确盒模型宽度。
- 🍀 Holly Hack：利用 IE Mac 注释解析 bug，配合浏览器检测，把修复只应用于 Windows IE6 及更早。
- 📏 Double Margin Float bug：IE 中左浮动元素可能双倍外边距，添加 `display:inline` 可规避。
- 🧰 工具栏屏蔽：站点曾用 CSS 隐藏 Skype、Ask 等工具栏注入内容，如 `.skype_pnh_container`、`#apn-null-toolbar`。
- 🏷️ 厂商前缀：`-webkit-`、`-moz-`、`-o-`、`-khtml-`、`-ms-` 曾用于实验特性，但因生产环境滥用导致厂商不得不保留支持，后来改用功能标志；多数前缀已过时。
- ⏳ 总结：这些 CSS 怪癖多已成为历史；除遗留场景外，开发者不必再担心 IE 等旧浏览器的古怪行为。
- 💰 文末附有支持作者的一次性或定期付款链接。

---

### [](https://tantek.com/CSS/Examples/boxmodelhack.html)

**原文标题**: [Box Model Hack](https://tantek.com/CSS/Examples/boxmodelhack.html)

本文介绍一种针对旧版 IE（IE5/Windows、IE5.5/Windows）的 CSS 盒模型 hack：利用其解析缺陷先设置宽度再覆盖，使带边框和内边距的 `div.content` 与其他浏览器等宽；同时补充为 Opera 5 等浏览器准备的规则、样式表验证建议以及 `?xml` 序言问题。

- 📦 `div.content` 设置 20px 边框、30px 内边距、背景 `#ffc`，并应在包含边框后与蓝色条等宽。
- 🐞 第二个规则利用 IE5/Windows 和 IE5.5/Windows 的 CSS 解析 bug，先设 `width:400px`，再通过 `voice-family: "\"}\""; voice-family:inherit; width:300px;` 覆盖为 300px。
- 🎛️ 该 hack 的目标是让旧 IE 也采用正确宽度，避免盒模型差异导致布局错位。
- 🎭 追加 `html>body .content { width:300px; }`，即“对 Opera 5 友好”规则，帮助支持 CSS2 选择器/盒模型但有相同解析 bug 的 UA；注意 `>` 周围不要留空格。
- 🧹 由于有解析 bug 的 UA 可能忽略后续规则，该规则可让异常解析器“追平”样式表。
- 🔵 用 `p.ruletest { color: blue }` 验证解析是否恢复：该段应为蓝色；若为红色，说明应被覆盖的旧规则仍在错误生效。
- 🧪 最后一条 `p.ruletest` 规则并非必需，只为证明上述盒模型 hack 规则能正确收尾。
- 📜 避免不必要的 `?xml` 序言；IE6/Windows 遇到它会使用怪异盒模型，建议直接省略。
- ✅ 将样式表作为媒体无关文件验证；W3C CSS 验证器对 `voice-family` 在 screen 样式表中报错属于验证器问题，之后按需用 `@import` 引入媒体相关元素。
- 🌍 文末列出多语言翻译：法语、葡萄牙语、俄语、西班牙语、德语、荷兰语、土耳其语等。
- 📚 另附更多 hack、示例与测试（CSS 示例、XHTML 测试、语义 XHTML 等）及相关阅读（Pandora's Box、Five Year Hackiversaries）。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Data 的 Tiger Cloud 是面向任意规模时序工作负载的 Postgres 服务，宣称单服务可达每天 3 万亿指标、3 PB 数据和 1 千万亿数据点，并提供弹性扩展、高可用、企业合规、可观测性、快速部署与生态集成；新账户可获 1000 美元信用，30 天有效且无需信用卡。

- 📊 单 Tiger Cloud 服务规模：每天 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 🎁 新账户注册可获 1000 美元信用，30 天有效，无需信用卡，仅限新账户。
- 🏢 受 IoT 等领域数千家公司信赖。
- ⚙️ 核心能力包括副本集最多 10 节点、读写分离、SSD/S3 分层存储，支持弹性扩展。
- 💰 计算与存储分离，可独立扩展，避免为闲置容量付费，优化成本与性能。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级：SOC 2、HIPAA、GDPR 合规，始终加密、SSO、RBAC、审计日志。
- 🔍 深度可观测性：查询下钻与仪表盘，指标可发送至 CloudWatch、Datadog、Prometheus。
- 🚀 快速开通：几分钟内配置数据库，支持 SQL、CLI、Terraform、Cursor、Claude Code 管理。
- 🔌 集成：可搭配首选云提供商和更广泛的 Postgres 生态。
- 🏅 企业就绪：合同 SLA、区域数据隔离、合规认证，以及 24/7 全球 Postgres 专家支持与保证响应时间。
- 📬 页面提供联系与开始使用入口，并包含隐私、法律、网站地图和版权信息。

---

### [前端检查清单 - Web 开发最佳实践 | 前端检查清单](https://frontendchecklist.io/)

**原文标题**: [Front-End Checklist - Web Development Best Practices | Front-End Checklist](https://frontendchecklist.io/)

前端检查清单（Front-End Checklist）是一个面向现代 Web 开发的开源质量规则库，目前处于 Beta 阶段。它为人类和 AI 代理提供可信赖的前端质量标准，包含 350+ 条规则，覆盖上线、评审、无障碍、性能、安全、隐私和 SEO 等流程。用户可按 11 个分类浏览规则，或使用精选清单快速上手，还能通过 MCP 协议接入 AI 工具。项目由 David Dias 于 2017 年创建，MIT 开源许可，GitHub 获 74.1k 星，个人使用永久免费。

- 🚧 项目目前处于 Beta 阶段，部分问题仍在修复中
- 📋 提供 350+ 条规则，分布在 11 个分类中，涵盖现代 Web 开发全流程
- ♿ 各分类规则数量：无障碍 95 条、SEO 94 条、性能 43 条、CSS 32 条、JavaScript 26 条、HTML 25 条、图片 25 条、安全 22 条、测试 13 条、国际化 5 条、隐私 5 条
- 🗂️ 提供四份精选入门清单：上线清单（16 条，45 分钟）、SEO 审计（12 条，30 分钟）、性能快速优化（8 条，20 分钟）、无障碍基础（12 条，35 分钟）
- 🤖 支持通过 MCP 协议集成 Claude、Cursor 等 AI 工具，实现代码审查、规则检索和 CI/CD 清单生成
- 🛠️ 即将推出团队协作空间、分析仪表盘和智能提醒等专业版功能，基础功能对个人永久免费
- 🌍 项目 2017 年创建，被全球数千名开发者使用，由 David Dias 维护并采用 MIT 开源许可

---

### [所有前端规则 | 前端检查清单](https://frontendchecklist.io/rules)

**原文标题**: [All Frontend Rules | Front-End Checklist](https://frontendchecklist.io/rules)

前端检查清单（Front-End Checklist）是一个仍处于 Beta 阶段的开源项目，汇总 385 条前端开发规则与最佳实践，覆盖可访问性、SEO、性能、CSS、JavaScript、HTML、图片、安全、测试、i18n、隐私等类别，并提供指南、精选工作流与 AI 友好资源，旨在帮助团队提升前端质量。

- 🚧 项目处于 Beta，部分问题仍在修复中。
- 📋 可浏览全部 385 条前端开发规则与最佳实践。
- 🗂️ 主要分类：可访问性 95、SEO 94、性能 43、CSS 32、JavaScript 26、HTML 25、图片 25、安全 22、测试 13、i18n 5、隐私 5。
- 🎯 面向现代 HTML、CSS、JavaScript、性能、可访问性和 SEO 开发。
- 🤖 提供 AI 友好资源，包括 MCP 概览和 llms.txt。
- 🧭 包含指南、如何使用检查清单、项目介绍、社区提及、源代码和站点地图等入口。
- 📦 开源 MIT 许可，由 David Dias 创建；GitHub 74.1k，并提供 X 链接。

---

### [](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)

**原文标题**: [Safari 27 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)

该页面依赖 JavaScript 才能正常显示内容；若未启用，需开启后刷新。同时为自动化与辅助工具提供了 Markdown 版本入口。

- ⚠️ 页面需要 JavaScript 支持才能查看内容。
- 🔄 需在浏览器中启用 JavaScript 并刷新页面。
- 🤖 面向自动化工具和辅助工具，提供了页面内容的 Markdown 版本。
- 🔗 可通过“查看 Markdown”链接访问该版本。

---

### [](https://developer.apple.com/documentation/safari-developer-tools/connecting-an-ai-agent-to-safari)

**原文标题**: [Connecting an AI agent to Safari | Apple Developer Documentation](https://developer.apple.com/documentation/safari-developer-tools/connecting-an-ai-agent-to-safari)

该页面依赖 JavaScript 才能显示内容；用户需在浏览器中启用 JavaScript 并刷新页面，同时页面为自动化工具和辅助工具提供了 Markdown 版本可供查看。

- ⚠️ 页面提示：需要 JavaScript 才能查看内容。
- 🔄 建议操作：开启浏览器 JavaScript 并刷新页面。
- 🤖 适用对象：自动化工具和辅助工具。
- 📝 替代方式：提供 Markdown 版页面内容。
- 🔗 可查看：点击“View Markdown”访问该版本。

---

### [](https://developer.chrome.com/blog/new-in-chrome-153)

**原文标题**: [New in Chrome 153  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-153)

Chrome 153 已开始推送，本次更新重点包括单轴滚动容器、`<camera>` 与 `<microphone>` 能力元素，以及 JavaScript 联合迭代方法 `Iterator.zip()` 和 `Iterator.zipKeyed()`。官方同时提供完整发布说明、更新列表和订阅渠道，Chrome 154 也将在后续发布。

- 🚀 Chrome 153 正在推出，发布于 2026 年 9 月 8 日，本文汇总了该版本的关键功能。
- 📐 单轴滚动容器：CSS `overflow` 支持 `auto`、`scroll`、`hidden` 与 `clip` 组合，例如 `overflow: scroll clip`，可让单轴滚动而不把另一轴变成滚动容器；Chrome 153 起在 Beta、Dev、Canary 无需 flag 即可测试。
- 📷 新增 `<camera>` 和 `<microphone>` 能力元素：它们是声明式、用户激活的 HTML 控件，分别用于请求视频和音频捕获。
- 🔒 这些元素嵌入浏览器控制且严格样式的 UI，用户点击后才会触发权限提示或启动媒体流，并沿用 `<usermedia>` 的安全模型与权限恢复路径，适合单能力媒体场景。
- 🔗 支持 TC39 Joint Iteration 提案：新增 `Iterator.zip()` 和 `Iterator.zipKeyed()`，用于同步多个迭代器的推进；前者产出数组，后者产出键控对象。
- ⚙️ `Iterator.zip()` 默认使用 `"shortest"`；`"longest"` 会持续到所有迭代器结束并用 `padding` 填充；`"strict"` 在输入迭代器长度不等时抛出 `TypeError`。
- 📚 更多变更可查阅 Chrome 153 发布说明、ChromeStatus 更新和 Chrome 发布日历；也可订阅 Chrome Developers YouTube、X 或 LinkedIn 获取动态。
- 🔮 Chrome 154 发布后，官方将继续介绍新功能。

---

### [](https://developer.chrome.com/blog/chrome-154-beta)

**原文标题**: [Chrome 154 beta  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-154-beta)

Chrome 154 beta 于 2026 年 9 月 2 日发布，面向 Android、ChromeOS、Linux、macOS 和 Windows 平台，带来 CSS/UI、JavaScript、Web API、WebGPU 等多方面更新，并新增源试验功能。

- 🚀 **发布信息**：Chrome 154 于 2026 年 9 月 2 日进入 beta 频道，可从 Google.com 或 Google Play 下载。
- 🎯 **scroll-marker-group 模式**：新增 `links`（默认，导航列表行为）和 `tabs`（标签页行为）两种模式，分别改变焦点顺序与无障碍行为。
- ✍️ **text-decoration-inset**：控制下划线、上划线、删除线相对文字边缘的内缩或外延距离，支持 auto、长度和百分比值。
- ␣ **text-decoration-skip-spaces**：控制装饰线是否跳过空白字符，避免在空格下方绘制装饰。
- 🧵 **CSSStyleValue 暴露至 Worker**：将 CSS Typed OM 的构造函数扩展到 Worker 全局作用域，符合规范与其他浏览器引擎。
- 🔤 **FontFace width 与 font-width**：作为 stretch 和 font-stretch 的别名，对齐最新 CSS 字体加载与 CSS Fonts 4 规范。
- 👆 **Light dismiss 改进**：popover 和 dialog 改用 click 事件触发关闭，触摸滚动和右键不再误触发。
- 🖼️ **响应式 iframe**：允许站点启用响应式尺寸，避免子文档出现滚动条。
- 🔁 **Iterator includes()**：TC39 提案，为迭代器添加 includes() 方法，类似 Array.prototype.includes()。
- 🔌 **WebSocket 构造函数选项包**：支持传入 WebSocketInit 字典，可指定 protocols，并为未来选项预留扩展点。
- 🔐 **WebCrypto 算法更新**：新增后量子与对称 AEAD 算法，包括 ML-KEM、ML-DSA、ChaCha20-Poly1305 和 X-Wing。
- 🌐 **Background Fetch 安全强化**：强制 CORS，并限制对本地/回环服务器的访问，需相应 LNA 权限。
- 🛑 **Fetch 转发中止原因**：将 AbortController 的 abort reason 暴露给 Response 对象及其 ReadableStream。
- 📄 **HTML 插入与流式方法**：新增位置插入方法（before、after、append、prepend、replaceWith）与流式方法（streamAppendHTML 等）。
- 💳 **安全支付确认语言验证**：locale 字段无匹配语言时返回 NotSupportedError，未设置则跳过验证。
- 🌍 **WebSocket targetAddressSpace**：可将公共主机名连接视为本地或回环目标，绕过混合内容限制。
- 🎮 **WebGPU WGSL 片段深度**：允许为 @builtin(frag_depth) 添加 less/greater 修饰符，启用 early-Z 优化。
- 🪟 **Window Shape API**：ChromeOS 上获白名单的隔离 Web 应用可定制非矩形窗口形状，需 unframed 模式与 window-management 权限。
- 🧪 **新源试验**：Private Verification Tokens（PVT）在常规浏览中签发、隐私浏览中兑换，减少验证码摩擦。

---

### [](https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/)

**原文标题**: [Automattic's board forces CEO Matt Mullenweg into leave of absence | TechCrunch](https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/)

Automattic 董事会将创始人兼 CEO Matt Mullenweg 强制安排为带薪休假，并任命 CFO Mark Davies 为临时 CEO；Mullenweg 称自己反对该决定，此事发生在其公司与 WP Engine 诉讼、裁员和内部争议不断的背景下。WordPress.org 表示开源项目不受影响，Mullenweg 仍是 WordPress 项目领导者。

- 🏢 Automattic 是 WordPress.com、Tumblr、WooCommerce、Pocket Casts 的母公司，由 Mullenweg 于 2003 年共同创建 WordPress 后创立。
- ⚖️ Mullenweg 在全员 Slack 中称，CFO Mark Davies 与董事 Ann Dunwoody、Toni Schneider、Sue Decker“合谋”投票，将他强制安排为带薪休假；他投了反对票。
- 🗳️ Davies 被选为临时 CEO；Mullenweg 称会议前 50 分钟才收到决议，并要求由独立法律顾问审查，甚至只求数小时，但被拒绝。
- ✅ Automattic 向 TechCrunch 确认 Mullenweg 正在休假，Davies 以临时 CEO 领导公司，董事会对其领导力和团队执行力有信心。
- 🧩 Davies 告诉员工 Mullenweg 仍留在董事会；WordPress.org 执行董事 Mary Hubbard 称开源 WordPress 项目不受影响。
- 🏛️ 近年来 Automattic 深陷争议：与 WP Engine 长期诉讼，Mullenweg 曾要求对方按月总收入 8% 支付 WordPress 品牌版税。
- 📜 WP Engine 于 2024 年 10 月起诉 Automattic 和 Mullenweg，指控诽谤与滥用权力；Automattic 去年提出反诉，WP Engine 今年 2 月称 Automattic 拟对另外 10 家竞争对手提出版税要求。
- 🚪 2024 年，Mullenweg 要求不认同他的员工带遣散费离职，159 人离开；他还曾停用部分 WordPress.org 社区成员账号。
- 📉 2025 年 4 月，Automattic 裁员 16%，包括一些任职十多年的老员工。
- 😶🌫️ 员工反应不一：有人“欣喜若狂”或“松一口气”，也有人因公司更不稳定而心情复杂。
- 🔥 董事会此时行动原因不明；有人猜测与他年度参加火人节后常“带着想法回来”有关，今年该活动 9 月 7 日结束。
- 📱 Mullenweg 在 X 上暗示法律纠纷相关指控，否认“恶意藏匿/破坏证据”，并预告可能遭遇抹黑报道；他还提到在火人节被盗后找回的尼康 D6 相机。
- 📨 Mullenweg 未回应 TechCrunch 的置评请求。

---

### [](https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/)

**原文标题**: [Matt Mullenweg tells (trolls?) Automattic staff, saying he's back in control after CEO ouster | TechCrunch](https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/)

Matt Mullenweg 在董事会将其罢免数日后，于 Automattic Slack 宣称自己重新掌控公司并回归 CEO；但董事会尚未正式确认，员工也未收到确认，令事件真假难辨。

- 🧑💼 TechCrunch 看到的 Slack 截图及多名员工消息显示，Mullenweg 称“董事会重新达成一致，我掌控 Automattic”。
- 🗳️ 仅在数天前，Automattic 董事会投票罢免其 CEO 职务，原因未知，并让 CFO Mark Davies 任临时 CEO，公司发言人曾证实。
- 📝 Mullenweg 回应置评称将发博客，但博客内容其实是买船屋；他还分享 LL Cool J《Mama Said Knock You Out》视频链接。
- ❓ Automattic 未确认其回归声明；截至发稿，员工未听到董事会确认，Davies 的 Slack 账号已被停用。
- 🏴‍☠️ 他还移除 Automattic Slack 的所有管理员，并发“海盗”帖且爆粗；被问是否在恶搞时答：“我不是巨魔，我是海盗，显然。”
- 📣 WordPress.org 执行董事 Mary Hubbard 在 X 表示，看到 Mullenweg 回归 CEO 感到“欣慰和高兴”。
- 🕵️ 在 Reddit/X 上，Mullenweg 称“事情与表面不同”，招募系统管理员和安全研究员帮他搬走托管在 Automattic 的东西，并暗示 Silver Lake 参与“摧毁”他的生活。
- ⚖️ Silver Lake 是 WP Engine 的多数股东，而 WP Engine 正与 Mullenweg 和 Automattic 诉讼。
- 😂 他在 X 发“Boards are never boring. 😂”，并曾发创始人建议：“如果几年没有政变企图，说明你没招到足够强的领导者。”
- 🔄 文章更新补充了评论和社交媒体链接；目前局势仍不明朗。

---

### [](https://css-tricks.com/)

**原文标题**: [CSS-Tricks - Learning for front-end designers and developers](https://css-tricks.com/)

本文主要介绍为即将推出的 CSS random() 函数创建兼容所有浏览器的 polyfill，并汇总近期 CSS/前端热门文章、最新文章与浏览器更新。
- 🎲 核心文章：Lee Meyer 于 2026 年 8 月 31 日讲解如何为新兴 CSS random() 函数打造全浏览器可用的 polyfill。
- 🧩 相关标签：CSS functions、polyfill、random、resource。
- 🔥 热门文章：涵盖 gap decorations、CSS border-image 动画、CSS 状态与 JavaScript 事件边界、ariaNotify()、aria-hidden 警告、暗色模式切换、border-shape、cos()/sin() 等。
- 📰 最新文章：包括 What’s !important #18、Document Picture-in-Picture API 网页小部件、MicroLighter 语法高亮、WordPress 纯 PHP 区块注册、CSS 类前缀选择器提案。
- ⚡ Quick Hits：Safari TP 252 测试 named-feature() 和 user-select；Firefox 157 Nightly 支持 overscroll-behavior: chain；Chrome 153 率先实现 scroll-axis-lock、<camera>、<microphone>；Chrome 155 Dev 实现 random()，Safari 也已支持，Firefox 支持 symbols()。
- 📚 文末可继续浏览 archives。

---

### [获取失败](https://geoffgraham.me/why-css-tricks-has-been-quiet/)

**原文标题**: [Failed to retrieve](https://geoffgraham.me/why-css-tricks-has-been-quiet/)

无法总结：获取内容失败，状态码 403。

---

### [更好的图标和标签对齐](https://ishadeed.com/article/aligning-list-icons/)

**原文标题**: [Better Icon and Label Alignment](https://ishadeed.com/article/aligning-list-icons/)

这段内容承诺将分享简洁清晰、配有图表或实例、能带来新知或提醒，并确保高质量的内容推荐。

- ✂️ 言简意赅，清晰说明要点，不啰嗦。
- 📊 至少包含一个图表或明确例子。
- 💡 让你学到新东西，或至少起到提醒作用。
- ⭐ 保证提供顶尖质量的内容推荐。

---

### [反对 JPEG XL 的理由 | Gianni Rosato](https://giannirosato.com/blog/post/case-against-jxl/)

**原文标题**: [
      The case against JPEG XL | Gianni Rosato
    ](https://giannirosato.com/blog/post/case-against-jxl/)

文章认为 JPEG XL 虽是技术上令人印象深刻的图像编解码器，却不应成为 Web 图像编解码器；作者曾是 JXL 支持者，但基于 2026 年压缩效率、解码性能与 Web 需求，认为 AVIF 已足够覆盖 Web 场景，JXL 更适合 Web 之外的专业用途。

- 🖼️ JPEG XL 是 JPEG 的升级版，也比 WebP 更全能，但 2023 年被 Chrome 拒绝；Rust 解码器进入 Firefox/Chrome 后，围绕它的争论再次升温。
- 👤 作者曾大力支持 JXL，为 Interop 2024 背书，并与主要作者多次交流；本文意在实证分析，而非攻击作者或表达政治立场。
- 🌐 Web 主要需要通用有损压缩，而非无损压缩；JXL 无损仅比无损 WebP 小约 11.9%，且测试集不现实，不值得为少量内容引入新编解码器。
- 📉 有损压缩方面，现代 AVIF/AV1 编码器经过感知调优，在速度与码率保真上更强；CVVDP、MS-SSIM、SSIMULACRA2 等指标显示 libjxl 明显落后。
- 🧱 JXL 编码工具存在劣势：缺少方向预测和去块环内滤波；gaborish/EPF 不能完全替代 DLF；XYB 收益有限，且 B 通道强量化损害颜色保持。
- 🧩 非摄影图像表现较弱，替代方案复杂：splines 缺乏 PoC，patches 比 AV1 IntraBC 开销更大，还依赖参考帧、混合、字典等额外概念。
- ⏱️ 解码时间不具竞争力：JXL 慢于 WebP/AVIF；JPEG 重压缩虽省约 20%，但解码多约 33%；特殊构造图像可极慢解码，带来 JXL-bomb 风险。
- 🚀 AVIF 已实现渐进解码，在约 2%–3% 文件大小时就能显示可用图像，且总文件更小；JXL 的渐进解码体验不如 AVIF。
- 🎯 Web 编解码器应目的明确、高效、范围狭窄；JXL 被设计成“全能格式”，不符合 Web 省带宽、快解码、防滥用的需求。
- 🧭 AVIF 已覆盖整个保真范围，JXL 在 Web 的唯一真正优势已消失；JXL 更适合 Web 之外的专业工作流、相机厂商和手机 OEM 等场景。
- 🗳️ 作者认为许多 JXL 支持理由来自希望更多开发者选择或反 Google 政治，而非技术必要性；JXL 并非无用，但不急于进入浏览器。

---

### [](https://blog.sentry.io/metrics-caught-ai-size-estimate/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=metrics-fy27q3-evergreen&utm_content=newsletter-sponsored-link-blog-learnmore)

**原文标题**: [Using Application Metrics to fix a broken size estimator | Sentry Blog](https://blog.sentry.io/metrics-caught-ai-size-estimate/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=metrics-fy27q3-evergreen&utm_content=newsletter-sponsored-link-blog-learnmore)

作者开发自托管视频剪辑工具 Cliparr 时，发现 AI 编写的视频文件大小估算器存在严重偏差，通过 Sentry Application Metrics 收集匿名真实数据后定位并修复问题，将估算误差从最高 83% 降至约 5%。

- 🎬 **起因**：视频编码后常遇"文件过大"报错，而理论上文件大小 = 比特率 × 时长，但实际受编解码器、格式、设备等因素影响，难以验证估算公式是否可靠。
- 💡 **巧妙方案**：将导出引擎从编辑器剥离，做成独立公共工具 Cliparr Convert，让访客免费使用并匿名上报指标，实现"真实数据 + 新工具 + SEO 收益"三重利好。
- 📊 **KPI #1 估算是否诚实**：用 distribution 记录实际大小与估算大小的比值，发现旧 AI 公式平均比值 1.57，最大偏差达 83%；原因是错误地用分辨率比例计算（分辨率其实不影响文件大小）。
- ✅ **修复效果**：改用正确的比特率公式后，平均比值降至 0.97，误差控制在约 5% 以内，并新增 estimator basis 属性便于区分公式。
- 🔍 **意外发现**：复制模式（不重编码）高估约 16%，GIF 估算稳定高估约 9%——均由 distribution 按属性分组所得。
- 👥 **KPI #2 用户行为**：mp4 输出格式比其他格式常见 2.5 倍，sharp 质量 + 原始分辨率是最常用设置，说明用户更倾向于格式转换而非压缩。
- ⚙️ **KPI #3 是否运行正常**：用 started / completed / failed 三个计数器追踪转换漏斗，目前失败率几乎为零。
- 📲 **KPI #4 安装情况**：将 PWA 安装做成多阶段漏斗计数器（prompt 可用→展示→点击→接受/拒绝→安装完成），并按设备形态与安装模式分组。
- 🧭 **为何用 Metrics 而非 Logs/Traces**：Traces 通常被采样，不适合需要精确总数的 KPI；Logs 面向调试；Metrics 记录每个数值且不采样，是"我们有意衡量"的明确声明。
- 🚀 **关键结论**：只需添加约 10 个指标、每个配 5 个属性，就能回答数百个产品级问题；无需写查询，甚至可用 MCP 或 Seer 通过自然语言直接提问。
- 💰 **上手成本**：Sentry 所有套餐（含免费 Developer 层）均含 5GB Application Metrics，开始使用只需几行代码。

---

### [](https://www.bram.us/2026/09/11/webkit-supports-interactive-widget-and-hopefully-safari-will-too/)

**原文标题**: [WebKit supports interactive-widget … and hopefully Safari will too? – Bram.us](https://www.bram.us/2026/09/11/webkit-supports-interactive-widget-and-hopefully-safari-will-too/)

概述总结
- 🌐 WebKit 已支持 `interactive-widget`，但是否会进入正式版 Safari 仍不明确；该特性主要用于解决虚拟键盘遮挡固定导航栏等问题。
- 🧑‍💻 作者 Bramus 于 2026 年 9 月发文，回顾该功能的背景、发展过程，并展示其在 WebKit 中的运行效果。
- 🕰️ 背景可追溯到 2022 年 Interop 的 Viewport Investigation Effort；Chrome 108 起改为虚拟键盘弹出时只调整 visual viewport，以与 Safari 行为对齐。
- ⚠️ 这一变化带来副作用：`position: fixed` 内容可能被虚拟键盘遮挡，因此 Chrome 推出 `interactive-widget` 指令。
- ⚙️ `interactive-widget` 写在 viewport meta 标签中，支持三个值：`resizes-visual`（默认，只调整视觉视口）、`resizes-content`（同时调整视觉与布局视口）、`overlays-content`（不调整视口，类似 Virtual Keyboard API 的 `overlaysContent=true`）。
- 🧪 作者自行编译 WebKit，并在 iPhone 模拟器的 MobileMiniBrowser 中测试，三种取值均正常工作。
- 🍎 但他仍想在真实 iOS Safari 中验证，可能需等待 Safari 27.1；Safari Technology Preview 发布说明未提及该功能，桌面版则出现了特性标志。
- 🤔 作者关注 Safari 浮动地址栏等 UI 差异，以及 `viewport-fit` 在 Safari 26 中损坏且尚未修复的问题。
- 📊 浏览器支持：Chrome 108（Android）与 Firefox 133（Android）已支持；Safari/WebKit 源码已实现，但尚未在公开版本或 Safari Technology Preview 中发布。
- 🔗 作者期待 Safari 跟进，并提供了 `interactive-widget` 指南、视口与虚拟键盘行为说明、Chrome Android 变更预告等资源。

---

### [使用 CSS 锚点定位的旁注](https://vincent.bernat.ch/en/blog/2026-css-sidenotes)

**原文标题**: [Sidenotes with CSS anchor positioning](https://vincent.bernat.ch/en/blog/2026-css-sidenotes)

本文介绍如何用 CSS 锚点定位实现边注：无需 JavaScript 即可支持多块内容，宽视口时显示在页边距并与引用标记对齐，窄视口或旧浏览器则回退到对应段落下方。

- 👤 作者是边注重度用户，认为边注能把可选内容留在正文旁，避免读者跳到底部再返回。
- 🧩 Tufte CSS 可无 JS 渲染边注，但只接受行内内容；CSS 锚点定位是更灵活的替代方案。
- 🌐 支持情况：Chrome 125（2024-05）、Firefox 147（2026-01）、Safari 26（2025-09）；旧版可能有碰撞问题，但本文方案依赖较新功能。
- 📚 2023 年 Eric Meyer 的“Nuclear Anchored Sidenotes”展示了该技术，主要优势是边注可放在 HTML 任意位置，并适合文本浏览器、屏幕阅读器、feed 阅读器和阅读模式。
- 📱 窄视口或不支持锚点定位时，边注以弱化颜色显示在引用段落下方；宽视口且支持时移到右边距，与引用标记同高，除非会与前一边注碰撞。
- ⚓ 标记用 `<sup data-anchor="--lf-sn-YYY">` 作为锚点，匹配的 `<aside role="note" data-anchor="--lf-sn-YYY">` 放在段落后。
- 🎯 通过 `@supports` 和 `@media(min-width:72rem)` 启用定位：引用标记设 `anchor-name`，边注设 `position:absolute`、`position-anchor` 和 `anchor-name:--lf-sidenote`。
- 📐 `top: max(anchor(top), anchor(--lf-sidenote bottom, -1rlh) + 1rlh)` 处理三种垂直情形：无前注则对齐标记顶部；可能碰撞则放到前注下方；否则仍对齐标记顶部。
- 🔤 typed `attr()` 可从 `data-anchor` 提取并解析为 `custom-ident`；支持较新浏览器有限，也可在 HTML 内联 `anchor-name`/`position-anchor` 以兼容更多浏览器。
- ↕️ 完整样式表还会把引用标记改为“↓”（边注在下方）或“→”（边注在边距），Gwern 文章列出更多实现与权衡。
- ✍️ 作者花大量时间在构建系统、Pygments 高亮、MDN 修正和 SVG 插图，但认为这篇边注方案值得。

---

### [](https://yatil.net/blog/wcag-3-road-to-hell-paved-with-supplemental-requirements)

**原文标题**: [WCAG 3’s road to hell is paved with supplemental requirements · Eric Eggert](https://yatil.net/blog/wcag-3-road-to-hell-paved-with-supplemental-requirements)

文章批评 WCAG 3 最新草案把核心要求与补充要求、断言混在一起，认为 Bronze/Silver/Gold 无法有效激励组织超越最低标准。作者主张改用模块化方案，让非核心要求独立成模块并可按需组合；同时质疑 WCAG 3 全面替代 WCAG 2 的必要性，认为更简单清晰的规范才更易采用。

- 😔 作者向 W3C AGWG 致歉，并指出工作组可能存在群体确认偏误，容易低估外部意见。
- 📄 新 WCAG 3 草案发布，配套变更日志和主席公告；动机是推动组织超越最低无障碍要求。
- ✅ WCAG 3 将 WCAG 2 A 与 AA 大致合并为基础层，满足全部 Core Requirements 即视为符合 WCAG 3。
- ⚠️ 问题出在 Supplemental Requirements 和 Assertions：它们是非必需要求，作者认为几乎无人真正在意，如同今天的 AAA。
- 🥉 工作组希望用 Bronze/Silver/Gold 激励超出基线，作者称这是“白日梦”：可选合规不会发生，连 WCAG 2 AA 的问题修复都常被质疑。
- 📚 混合必需与非必需要求使文档冗长、难扫描、难理解、难满足；“WCAG 3 Bronze”也无法说明网站实际可访问性，缺乏用户价值。
- 🎚️ WCAG 2 的 AAA 常被用作泄压阀，把缺乏共识的要求推过去，结果既无后果，也难给残障用户带来实际好处。
- 🧩 替代方案是模块化：将字幕等补充要求做成 BetterCaptions、SignLanguage、EasyLang 等模块，而非塞进核心规范。
- 🏢 模块化可让专家分组工作；公司可声明“WCAG 3+BetterCaptions”，政策制定者可细粒度要求“WCAG 3+BetterCaptions+SignLanguage+EasyLang”。
- 🤔 Assertions 如焦点指示样式指南，更像属于无障碍成熟度模型或 OngoingTraining 模块，对实际无障碍提升作用可疑。
- ⏳ 作者肯定工作组十年进展，但认为应尽快决定路线，避免继续沉没成本；更简单、清晰、少而明确的指南更有效。
- 🔄 WCAG 3 目前臃肿且距发布仍远；若核心要求约等于 WCAG 2 AA 加少量新增，全面换标准未必值得，还可能导致不同辖区切换不一、组织需同时遵守两套标准。
- 🚫 结论：标准不是编纂善意的地方；非必需要求是否算“可选要求”，也许永远说不清。

---

### [为 CSS border-image 添加动画 | CSS-Tricks](https://css-tricks.com/animating-css-border-image/)

**原文标题**: [Animating CSS border-image | CSS-Tricks](https://css-tricks.com/animating-css-border-image/)

本文介绍如何用 CSS 的 `border-image` 搭配渐变与自定义属性动画，做出会“绘制”和旋转的动态边框效果，并展示从线性渐变到圆锥渐变等多种变体。

- 🎨 `border-image` 可用图片或渐变替代普通实线/虚线边框，适合做更有趣的 UI。
- ⚠️ 主要限制：`border-image` 不会随元素圆角弯曲，动画环绕边框时需变通处理。
- 🧩 替代方案包括 CSS mask；作者引用 Temani Afif 的做法，但更偏好 `border-image` 的效率与自动复制到四边。
- ⚙️ `border-image-slice` 能切片图像/渐变，类似 `background-size` 和 `background-position`，但切片可贯穿整个边框。
- 🖼️ 示例 HTML 很简单：一个 `.card` 容器，内含文字，并用背景图呈现人物像。
- 📐 基础样式设置卡片尺寸、比例、背景图；边框用 `linear-gradient`、`border-image-slice: 1`、`border-image-width: 5px` 和 `border-image-outset: 5px`。
- ✨ 渐变默认不能平滑过渡，需用 `@property` 注册自定义百分比变量，例如 `--p`，再在 `:hover` 中从 `0%` 过渡到 `100%`。
- 🔄 动画时红色从起点延伸到终点，边框像“自己画出来”一样。
- 🎞️ 变体可使用 `conic-gradient`、`border-image-repeat: round`，并注册 `--n` 控制切片、`--a` 控制角度。
- 🧪 悬停时把 `--n` 增至 `20`、`--a` 转到 `360deg`，可让边框切片变厚并旋转绘制。
- 🧠 还可尝试多颜色、重复渐变等更多效果；作者鼓励读者拆解示例并分享新创作。

---

### [深入解析 StyleX](https://flaviocopes.com/stylex/)

**原文标题**: [A deep dive into StyleX](https://flaviocopes.com/stylex/)

这篇文章深入介绍 StyleX：一种用 JavaScript 对象编写样式、在构建时编译为常规原子 CSS 的方案；涵盖 React/Vite 与 Astro 设置、组件样式、变体、响应式、主题、令牌、限制与取舍，并讨论其为何适合编码代理。

- 🎯 StyleX 是 JavaScript 样式语法与编译器：开发时像 CSS-in-JS，构建后输出普通 CSS 类，生产渲染不注入样式。
- 🧩 它主要解决大型应用中的 CSS 问题：命名冲突、覆盖难查、删除不安全、样式归属不清、复用困难和未使用 CSS。
- 🧠 核心心智模型：用 `stylex.create()` 定义样式对象，编译器生成小型原子类，再用 `stylex.props()` 应用。
- ⚛️ React + Vite 设置：安装 `@stylexjs/stylex` 与 `@stylexjs/unplugin`，将 `stylex.vite()` 放在 React 插件之前。
- 🃏 第一个组件：`stylex.create()` 接收具名样式组，`stylex.props()` 返回 `className` 和必要时 `style`，可直接展开。
- 🛠️ StyleX DevTools：开发模式添加 `data-style-src` 与可读标记，Chrome 扩展可查看样式来源、顺序和对应源文件。
- 🚀 Astro 集成：复用同一 Vite 插件，适合 React 组件；开发时引入 `/virtual:stylex.css` 与运行时，生产构建抽取 CSS。
- 🧱 原子 CSS 策略：每条声明生成一个类，相同声明可跨组件复用与去重，HTML 类名更多但样式表重复更少。
- 🧬 样式组合：`stylex.props(styles.card, styles.featured)` 中后者覆盖前者，冲突在浏览器看到类列表前解决。
- 🔀 条件样式：使用普通 JavaScript 的 `&&` 或三元表达式，`false`、`null`、`undefined` 会被忽略。
- 🎨 变体实现：用对象查找如 `colorStyles[color]`，TypeScript 可约束可选键，无需额外变体配置。
- 🖱️ 交互状态：伪类写在属性内部，如 `backgroundColor: { default, ':hover', ':active' }`；伪元素放在样式顶层。
- 📱 响应式样式：媒体查询按属性嵌套，可与伪类组合，也支持 `@supports` 和容器查询。
- 📏 动态值：样式函数可接收简单标识符并返回对象字面量，生成 CSS 变量加元素行内 `style`；已知状态应优先用变体。
- 🎛️ 设计令牌：用 `stylex.defineVars()` 创建类型化 CSS 变量，必须放在 `.stylex.ts` 等文件并具名导出。
- 🌗 主题：用 `stylex.createTheme()` 覆盖变量组，在局部应用中生效，组件继续使用语义化令牌。
- 🧱 父传样式：组件可接受 `StyleXStyles` 类型，甚至限制允许的属性，比任意 `className` 更安全可审查。
- 🎞️ 关键帧动画：用 `stylex.keyframes()` 定义动画，再在 `animationName` 中引用，无需手动传递全局动画名。
- 🧪 内联原子：`@stylexjs/atoms` 提供工具类式原子样式，适合小例外；可复用组件仍推荐命名样式。
- 🚧 静态约束：样式必须在构建期可解析，不能用任意 JS、普通导入值或对象展开；共享值用 `defineVars()` 或 `defineConsts()`。
- 🌐 全局 CSS：仅保留 reset、body 默认、字体、CMS 原始 HTML 等；启用 CSS layers 时注意未分层全局规则优先级更高。
- ✅ Lint 支持：`@stylexjs/eslint-plugin` 可校验样式、发现未使用样式、检查简写、排序，并限制属性值。
- 🤖 对编码代理友好：语法更冗长但约束更强，减少随意值、深层选择器和命名自由度，让代理生成的 UI 更一致、更易审查。
- ⚠️ 代价与限制：设置比普通 CSS 复杂，语法比 Tailwind 长，生态组件多偏 Tailwind，且需放弃部分全局样式与深层选择器模式。
- 📊 方案对比：原生 CSS 灵活但需管理；Tailwind 编写快但标记膨胀；运行时 CSS-in-JS 动态但增加运行时；StyleX 可预测组合但编译器与规则更严格。
- 🧭 适用场景：适合新 React 应用、成长中的组件库、大量编码代理改 UI 的项目；小型项目或静态 Markdown 站点不必为它迁移。
- 📦 生产构建：Vite 构建后输出哈希原子类 CSS，应用代码中不再包含原始 `stylex.create()` 对象。

---

### [](https://stylexjs.com/)

**原文标题**: [StyleX — styling system for ambitious interfaces](https://stylexjs.com/)

StyleX 是一个面向复杂、雄心勃勃界面的样式系统，强调表达力、类型安全、可组合、可预测和可主题化；页面汇集了入门、学习、API、博客、演练场、社区参与以及法律版权等信息。

- 🎨 核心定位：为 ambitious interfaces 提供样式系统。
- 🧩 核心特性：expressive、type-safe、composable、predictable、themeable。
- 🚀 入门入口：Get Started、Thinking in StyleX。
- 📚 资源导航：Docs、API、Blog、Playground，并支持搜索（⌘K）。
- 🛠️ 开发与学习：Develop、Learn、API、Explore。
- 🤝 社区参与：Participate、GitHub。
- ⚖️ 法律与致谢：Acknowledgements、Legal、Privacy、Terms。
- ©️ 版权归属：Copyright © 2026 Meta Platforms, Inc.。
- 🦋 社交链接：Bluesky。

---

### [支持 `headers` 属性 — Adrian Roselli](https://adrianroselli.com/2026/09/support-for-headers-attribute.html)

**原文标题**: [Support for `headers` Attribute — Adrian Roselli](https://adrianroselli.com/2026/09/support-for-headers-attribute.html)

overview summary
本文重新测试 HTML 表格 `headers` 属性的可访问性支持，结论是其在屏幕阅读器/浏览器组合中的支持仍不一致；跨行、跨列和复合表头应避免，`headers` 属性基本无用，移动端屏幕阅读器通常忽略表头。

- 📉 `headers` 属性的支持依旧很差，作者 2022 年和 2023 年的旧结论在这次测试中基本成立。
- ⚠️ TL;DR：避免跨行/跨列和复合表头，因为各平台支持不一致，`headers` 属性大体无用。
- 📱 移动端屏幕阅读器与浏览器组合通常忽略行、列和跨列表头，无论是否使用 `headers` 属性。
- 🖥️ 桌面端屏幕阅读器与浏览器组合，即使没有 `headers` 属性，也能较好地处理跨列表头；主要例外是 Safari。
- 🧪 测试覆盖 Firefox/NVDA、Chrome/JAWS、Edge/Narrator、Safari/VoiceOver macOS、Chrome/TalkBack、Firefox/TalkBack、Safari/VoiceOver iPadOS；Firefox/Orca 因虚拟机问题未完成。
- 🍎 Safari/VoiceOver macOS 一旦使用 `headers`，似乎需要到处设置，但仍可能播报错误表头轴；iPadOS 表现又不同。
- 🤖 Chrome/TalkBack 与 Firefox/TalkBack 中，`headers` 属性没有影响，表头也常不被播报。
- 🐞 已知缺陷包括 Chromium 忽略 `headers`、跨行表头被重复播报、JAWS 播报错误列标题、WebKit 行标题播报错误等。
- 🧰 浏览器开发工具难以暴露表格标题关系，因此需要手动屏幕阅读器测试；评论中有人建议用 aViewer 等工具辅助调试。
- 📜 RGAA/RAWeb 5.7.4 要求用 `headers` 属性关联表头，但作者对“规定技术实现而非可衡量用户结果”的可访问性要求持谨慎态度。
- ✅ 结论：不要依赖 `headers` 属性解决复杂表头问题，优先避免跨行/跨列和复合表头，并基于真实用户测试结果决策。

---

### [谷歌和 OpenAI 希望你的网站能与智能体对话](https://agenticweb.nearestnabors.com/p/webmcp-agentic-web-openai-google)

**原文标题**: [Google and OpenAI Want Your Site to Talk to Agents](https://agenticweb.nearestnabors.com/p/webmcp-agentic-web-openai-google)

WebMCP 试图把网页变成 AI 助手与代理可直接调用的工具层，Google Chrome、OpenAI 等正联合推动其落地，但它仍只是 W3C 草案，标准、安全与商业博弈都未尘埃落定。

- 🌐 WebMCP 连接 Web 与 AI 助手/代理；Chrome 与 OpenAI 联手推广，合作伙伴包括 Cloudflare、Shopify、Netlify、Vercel、Render。
- 🎓 作者推出 LinkedIn Learning 课程《WebMCP in 10 minutes》，赶上这波宣传，但因此错过相关竞赛。
- 📜 WebMCP 只是 W3C Web Machine Learning 社区组草案，不是 W3C 标准，也未进入标准轨道；2026 年 5 月才启动 TAG 及隐私安全组的早期广泛审查。
- 🔧 API 仍在快速变动：`provideContext()`/`clearContext()` 被删，`unregisterTool()` 改为 `AbortSignal`，API 从 `navigator` 移到 `document`；微软参与合著却在 Edge 中将其藏在 flag 后。
- ⚖️ OpenAI 曾推出代理浏览器 Atlas，后并入 ChatGPT；Amazon 因 Comet 代理购物起诉 Perplexity，先获禁令，后于 2026-08-04 上诉被推翻，案件未完。
- 🛒 第九巡回法院认为用户指挥代理时，访问权属于用户而非 Perplexity；但零售商想控制购买界面以追加销售和卖广告，代理购物威胁其商业模式。
- 🌉 WebMCP 被视为通往代理式 Web 的桥梁：Google 押注代理化 Chrome/Gemini，OpenAI 押注 ChatGPT 成为世界入口，网页成为人类优先的兜底层。
- 🛍️ WebMCP 需站点主动选择加入；Shopify 积极拥抱代理购物，并与 OpenAI 探索 MCP Apps/WebMCP，因其客户是商家而非购物者。
- 🧰 WebMCP 不提升发现性，只提升代理可操作性；工具绑定标签页且短暂，代理必须已在页面上才能知道；可减少截图/DOM 转储和往返。
- 🔐 安全风险：页面内工具可访问用户实时会话和 cookie；提示注入未解决。现有 `readOnlyHint`、`untrustedContentHint` 注释，`requestUserInteraction()` 仍无规范算法，同意管理仍在讨论。
- ✅ 是否让站点支持代理：若用户已开始用 AI 助手/代理浏览器，可在一个重要流程试水 WebMCP，观察 3–6 个月；已有语义化、可访问表单时只需加少量属性。
- 🔗 作者提供 LinkedIn Learning 课程《WebMCP in 10 minutes》供进一步学习。

---

### [](https://www.youtube.com/watch?v=xtVvkRTH5ck)

**原文标题**: [WebMCP is here (and you should care) - YouTube](https://www.youtube.com/watch?v=xtVvkRTH5ck)

這段內容是 YouTube 的頁尾／底部導覽資訊，列出平台介紹、新聞、版權、聯絡、創作者、廣告、開發者、條款、私隱、政策安全、運作方式、新功能測試及版權聲明等連結與資訊。

- ℹ️ 簡介：提供平台基本介紹入口
- 📰 新聞中心：官方新聞與媒體資訊
- ©️ 版權：版權相關說明與規範
- 📞 聯絡我們：提供聯繫管道
- 🎬 創作者：創作者相關資源與入口
- 📢 刊登廣告：廣告投放與合作資訊
- 💻 開發人員：開發者資源與技術入口
- 📜 條款：服務條款與使用規範
- 🔒 私隱：私隱政策與資料處理說明
- 🛡️ 政策及安全：平台政策與安全資訊
- ⚙️ YouTube 的運作方式：說明平台運作機制
- 🧪 測試新功能：實驗功能與新功能測試
- © 2026 Google LLC：版權所有與年份標示

---

### [](https://neat-annotations.syabro.com/)

**原文标题**: [neat-annotations — neat hand-drawn CSS annotations](https://neat-annotations.syabro.com/)

neat-annotations 是一个纯 CSS 的手绘风格标注库，无需 JavaScript，只需一个小文件就能为网页元素添加箭头和手写标签。

- ✏️ 纯 CSS 实现，无 JavaScript，仅需一个小文件即可使用
- 📦 通过 CDN 引入样式表，或下载 neat-annotations.css 本地链接
- 🖋️ 可选加载手写字体 Shantell Sans，跳过则标签回退为 cursive 字体
- 🧭 支持指南针方向设置箭头指向（如 ann-n 表示北向）
- 🎨 提供五种颜色加动画彩虹色，以及暖灰色默认色
- 🌈 可通过 --ann-color 自定义任意 CSS 颜色
- 🔆 支持目标高亮，省略 data-note 可隐藏箭头和标签，仅作文字标记
- 📚 可嵌套标注，从不同方向指向同一目标
- 📏 长注释自动换行，可用 --ann-label-max-width 控制行宽
- 📄 采用 MIT 许可证，源码托管于 GitHub

---

### [](https://github.com/syabro/neat-annotations)

**原文标题**: [GitHub - syabro/neat-annotations: Hand-drawn CSS annotations for inline content · GitHub](https://github.com/syabro/neat-annotations)

neat-annotations 是一个为网站内联内容添加手绘箭头与手写标签的纯 CSS 注释工具，无需 JavaScript 或构建步骤，以单文件形式提供。以下是要点总结：

- 📦 仓库信息：`syabro/neat-annotations`，MIT 许可证，约 720 stars、19 forks、36 commits。
- 🎨 核心功能：为网页元素添加手绘箭头、手写标签和目标高亮。
- 🧩 技术特点：纯 CSS，无 JavaScript，无构建步骤，使用单个 `neat-annotations.css` 文件。
- 🚀 快速开始：通过 jsDelivr 引入样式表，或用 `span` 包裹目标并设置 `class="ann ..."` 与 `data-note`。
- ✍️ 字体支持：可选加载 Shantell Sans；未加载时标签回退为 cursive 字体。
- 📐 布局提醒：注释位于目标外部且不预留空间，需要给箭头和标签留出足够边距。
- 🧭 API 用法：基础类 `ann`；方向类包括 `ann-n`、`ann-ne`、`ann-e`、`ann-se`、`ann-s`、`ann-sw`、`ann-w`、`ann-nw`；标签由 `data-note` 提供。
- 🌈 颜色样式：默认暖灰，内置 amber、blue、green、red、purple、rainbow；rainbow 支持动画并尊重 `prefers-reduced-motion`。
- 🎯 高亮模式：省略 `data-note` 和方向类可仅作标记；`ann-no-mark` 可保留目标原有填充。
- 🧱 进阶能力：注释可嵌套；长标签按 `--ann-label-max-width` 换行。
- ⚙️ 可调变量：包括 `--ann-color`、`--ann-mark`、`--ann-font`、`--ann-target-gap`、`--ann-label-gap`、`--ann-label-max-width`、`--ann-arrow-x/y`、`--ann-text-x/y`、`--ann-rotate` 等。
- ♿ 可访问性：注释是视觉增强，`data-note` 不应作为唯一必要信息来源；重要内容需在可见 HTML 中重复或用 `aria-describedby` 关联。
- 📄 许可证：MIT。

---

### [](https://rich-input.netlify.app/)

**原文标题**: [<rich-input> – A Rich Input Field](https://rich-input.netlify.app/)

rich-input 是一个原生、轻量的 Web Component，为普通网页表单带来搜索引擎级过滤体验；用户可输入自由文本或结构化条件（如 label:"We Play House Recordings"、year:2026、playlist:"WPH Classics"），并以内联高亮、自动补全和表单集成提升搜索交互。

- 🎵 支持自由文本与结构化键值查询，示例包括 label、year、playlist 等过滤字段。
- 🧩 基于原生 Web Component，轻量并利用现代 Web 平台能力。
- 🎯 双自动补全：既补全过滤关键字（如 a→artist:、s→style:），也补全对应值（如 label:"K→Keinemusik 或 Kranky）。
- 📍 使用 OpaqueRange 将建议弹层定位到当前范围起点，例如引号开头；无支持时回退到隐藏 mirror-div。
- 🎨 通过 CSS Custom Highlight API 在原生 input 内高亮关键字和值，如 ::highlight(label)、::highlight(year)。
- 🧩 声明式 `<datalist>` 配置，无需 JavaScript；id 定义关键字，label 显示名称，data-type="number" 支持数字。
- 📋 表单关联 formAssociated = true，支持 `<form>` 提交、FormData 和表单重置。
- 💅 通过 ::part(input)、::part(control)、::part(popover)、::part(suggestion-item) 等实现完整主题化。
- 🖼️ 富选项标记：可在 `<option>` 内嵌入图片或 HTML，建议项显示 logo，选中后只插入干净的 value。
- 🧠 OpaqueRange API 用于范围测量、高亮创建与清理；兼容回退使用 contenteditable 和隐藏镜像 div。
- 🌈 支持自定义高亮样式与无效值红色波浪线；也可嵌入 `<style>` 自动注入 shadow root。
- 🧱 暴露 Shadow Parts 与 slots（leading、trailing、默认 slot），便于自定义图标和布局。
- 🔍 提供 value、getParsedQuery()、getKeywords()、focus/blur/select、setSelectionRange() 等 API。
- 📣 事件包括 rich-input-select 和 search，分别用于选择建议和按 Enter 搜索。
- 🔄 支持动态添加或更新 <datalist>，通过 MutationObserver 与 slotchange 即时更新。
- 🚀 可 npm install rich-input 或通过 ESM/CDN 加载，并适配多浏览器高亮与定位回退。

---

### [Chrome 平台状态](https://chromestatus.com/feature/6297362687066112)

**原文标题**: [Chrome Platform Status](https://chromestatus.com/feature/6297362687066112)

未提供可总结的正文内容，因此暂时无法生成文章摘要。  
- 📄 请补充或粘贴需要总结的文本内容。  
- 🧭 收到内容后，我会用中文提炼核心信息。  
- ✅ 输出将包含概览摘要，以及每条以“-”开头并配 emoji 的关键要点。

---

### [](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

**原文标题**: [CSS Custom Highlight API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

CSS Custom Highlight API 是 2025 年 6 月起在最新浏览器中可用的新特性，它允许开发者通过 JavaScript 创建任意文本范围，并使用 CSS 进行样式化，而无需修改页面的 DOM 结构。该 API 扩展了现有高亮伪元素（如 `::selection`）的能力，为高亮文本范围提供了更灵活、可编程的解决方案。

- 📌 通过 JavaScript 创建 `Range` 对象，再用 CSS 样式化，实现任意文本范围的高亮。
- 🎯 扩展了 `::selection`、`::spelling-error` 等伪元素，支持自定义高亮范围。
- 🔧 使用四步：创建 `Range` 对象 → 创建 `Highlight` 对象 → 通过 `HighlightRegistry` 注册 → 用 `::highlight()` 伪元素设置样式。
- 🗂️ 核心接口：`Highlight`（表示范围集合）和 `HighlightRegistry`（通过 `CSS.highlights` 访问的类 Map 注册表）。
- 📝 示例：监听搜索框输入，查找匹配文本并创建范围，注册为 `search-results` 高亮，再用 CSS 设置背景色和文字颜色。
- ♿ 无障碍注意：自定义高亮不提供语义，建议使用 `<mark>` 或额外提示；`type` 属性可暴露语义，但支持情况不一。
- 🌐 浏览器兼容性：Baseline 2025，自 2025 年 6 月起在最新设备和浏览器版本可用，旧设备可能不支持。
- 📚 规范：CSS Custom Highlight API Module Level 1。

---

### [](https://expo.dev/services/simulators?utm_source=frontendfocus&utm_medium=email&utm_campaign=agentic-development&utm_term=lp)

**原文标题**: [EAS Simulator: Simulators built for agents](https://expo.dev/services/simulators?utm_source=frontendfocus&utm_medium=email&utm_campaign=agentic-development&utm_term=lp)

EAS Simulator 是 Expo 推出的早期访问服务，为 AI 代理提供按需、安全、可并行的云端模拟器；代理可安装构建、驱动应用并验证修复，最终把会话录像作为 PR 证明。

- 🧪 面向代理：代理可在云端模拟器中安装并操作构建，自动验证自己的代码修改。
- ☁️ 按需启动：需要时创建安全的云模拟器，数量可随代理需求横向扩展，完成后自动销毁。
- 🔁 闭环流程：从崩溃报告或缺陷进入队列，到代理写修复、在模拟器运行，再到 PR 中附上会话录像。
- 📹 PR 证明：不再只提交“看起来差不多”的 500 行代码，而是用会话录像证明修复有效。
- 🔐 端到端安全：每个会话隔离运行，依托 EAS Build、Submit、Workflows 的同一基础设施。
- 🧰 自带工具：可用 argent 或 agent-device 驱动模拟器，延续本地工作流。
- ⌨️ 一条命令：用 `eas simulator --platform ios` 让代理获得可驱动会话，你获得可观看的实时流。
- ⏳ 早期访问：目前已开放等待名单，可加入或联系团队。

---

### [SnapDOM：浏览器捕获引擎](https://snapdom.dev/)

**原文标题**: [SnapDOM: Browser Capture Engine](https://snapdom.dev/)

SnapDOM 是一个零依赖的浏览器捕获引擎，可将 UI 的实时 DOM 渲染状态捕获为图像，并从一次可复用捕获中导出多种格式；核心采用 MIT 许可，月下载量超 100 万，插件可扩展 PDF、矢量、HTML/代理上下文以及 GIF/视频录制能力。

- 🧩 **零依赖与 MIT 许可**：核心可用于个人或商业项目，支持加载所需插件或通过公共 API 自定义扩展。
- 📸 **一次捕获，多种导出**：同一结果可输出 PNG、JPG、WebP、SVG、canvas 或 Blob，canvas 还能用作 WebGL 纹理。
- ⚡ **V3 快速重复捕获**：复用资源和未变化捕获，导出按需执行，仅重新捕获发生变化的元素。
- 🎨 **渲染细节完整**：捕获 Web 字体、伪元素、SVG、背景、开放 Shadow DOM 及表单控件当前状态。
- 🧠 **HTML 与代理上下文**：插件可导出自包含 HTML、文本/JSON 大纲，以及带交互元素映射的截图。
- 🎞️ **GIF 与视频录制**：录制插件逐帧捕获实时元素，适合动画、交互演示和短片段。
- 📄 **SnapDOM Pro 增强**：提供可搜索 PDF 和可编辑矢量，支持 PDF 文本层/分页，以及导出到 SVG 和 Figma。
- 💰 **发布优惠**：PDF/Vector 插件首年个人 $19.50、商业 $49.50，之后 $39/$99 每年；前 30 名购买，截止 2026-09-29 或售罄。
- 🛠️ **应用场景**：产品仪表盘导出、WebGL 画布纹理、代理页面理解、视觉测试基线等。
- 📚 **文档与演示**：涵盖安装/捕获/导出、API、选项、React/Vue/Svelte 指南、食谱、工具对比和 21 个实时演示。
- 📦 **安装方式**：`npm i @zumer/snapdom@latest`，或通过 `unpkg` 引入；当前 v3.x.x，月下载 1m+。

---

### [](https://github.com/niklasvh/html2canvas)

**原文标题**: [GitHub - niklasvh/html2canvas: Screenshots with JavaScript · GitHub](https://github.com/niklasvh/html2canvas)

html2canvas 是由 niklasvh 维护的开源 JavaScript HTML 渲染器，可在浏览器端将网页或局部 DOM 渲染为 canvas“截图”，但基于 DOM 模拟生成，并非真实截图，且项目仍处实验阶段。
- 📸 功能：允许直接在用户浏览器中对网页或部分网页进行“截图”。
- 🧠 原理：读取 DOM 和元素样式，在客户端生成 canvas 图像，无需服务端渲染。
- ⚠️ 局限：截图可能无法 100% 还原真实页面，不适合 Node.js，跨域内容需要代理到同源。
- 🧪 状态：仍非常实验性，不建议用于生产环境或直接基于它构建应用。
- 🌐 兼容：支持 Firefox 3.5+、Google Chrome、Opera 12+、IE9+、Safari 6+，旧浏览器需 Promise polyfill。
- 🎨 CSS：每个 CSS 属性需手动构建支持，目前仍有许多属性未支持。
- 🧩 用法：调用 `html2canvas(element[, options])`，返回包含 `<canvas>` 的 Promise，可用 `then` 处理。
- 📦 构建：可下载现成构建，或通过 `git clone`、`npm install`、`npm run build` 构建浏览器包。
- 🔗 资源：提供主页、下载、问答、示例和测试控制台。
- 🤝 贡献：PR 应提交到 develop 分支，并需测试所有支持浏览器；不完整 CSS 属性应补充测试。
- 📊 项目：MIT 许可，约 31.9k Star、4.9k Fork、976 Issues、78 PR。
- 🏷️ 主题：dom、javascript、screenshot。

---

### [](https://github.com/zumerlab/snapdom/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · zumerlab/snapdom · GitHub](https://github.com/zumerlab/snapdom/releases/tag/v3.0.0)

SnapDOM v3.0.0 是首个稳定版本，带来自动复用捕获、增量重捕获、自动字体嵌入和新捕获 API，核心与官方插件统一到 v3 发布线；同时包含破坏性变更、渲染/字体/Canvas/兼容性修复，以及插件、文档和测试维护更新。

- 🚀 **版本发布**：v3.0.0 是 SnapDOM v3 首个稳定版，2026 年 9 月 14 日发布，包含 13 个提交，核心与官方插件共享 v3 发布线。
- ⬆️ **升级提示**：从 v2 升级需阅读迁移指南；v2 源码和 v2 文档仍可用。
- ✨ **核心功能**：自动复用符合条件的未更改捕获，并为安全的本地变更重建受影响子树；支持按捕获会话隔离并发捕获。
- 🔤 **字体与 API**：自动嵌入捕获内容使用的 Web 字体；新增 `fromString()` 捕获 HTML 字符串，以及 `preCapture()` 在悬停/聚焦时准备已学习捕获。
- 🧩 **渲染引擎**：SVG 引擎仍为默认；原生 html-in-canvas 引擎仍属实验性，需要自定义构建。
- ⚠️ **破坏性变更**：`width` 和 `height` 优先于 `scale`；字体嵌入自动启用；`preCache` 被移除；旧捕获选项不再支持；核心脱敏仅限密码字段；`afterExport` 不再链式返回结果。
- 🎨 **布局渲染修复**：修正伪元素框、滚动容器、图片对齐、变换元素协调、离屏捕获、分数宽度换行、包装高度、`visibility`/`content-visibility`、文本截断测量、CSS `zoom` 和 SVG `<use>` 填充色等问题。
- 🖋️ **字体与伪元素**：保留图标字形及斜体图标字体样式；跳过非生成伪元素；保留自定义 `@font-face` 规则、图标字体外的其他字体，并仅输出源中声明的描述符。
- 🖼️ **Canvas 与 Shadow DOM**：限制 canvas 帧等待，空 canvas 警告，保留 WebGL 的 `toDataURL()` 前帧；slotted light DOM 仅克隆一次；支持跨窗口/iframe 的 DOM 类型检查。
- 🔧 **兼容性修复**：修复 legacy bundle 全局变量泄漏，并修正 iframe 相关指导。
- 🔌 **插件与导出**：官方插件对齐 v3，覆盖 HTML、上下文、元素映射、PDF、图像效果、GIF/视频录制；向插件暴露捕获几何、导出选项和 canvas 裁剪；color-tint 插件支持跨窗口 clone roots。
- 📚 **文档更新**：对齐包引用、版本标签和插件展示；记录插件 hook 契约并修正 subpath 导入；补充服务端捕获、DOM 捕获边界与集成指南；重写 `llms.txt` 和 `llms-full.txt`。
- 🧪 **测试维护**：暴露内部视觉演示，扩大回归覆盖，视觉套件拆为 6 个分片；改进网络依赖测试调度，等待 iframe 样式、导入字体和图片解码；测试独立于捕获引擎并固定 `devicePixelRatio`。
- 🛠️ **构建流程**：停止从 `npm run build` 自动推送 changelog。
- 🔗 **完整变更**：完整变更日志为 `v2.23.1...v3.0.0`。

---

### [GitHub - spiritov/ds.css：重现 DS / DS Lite 界面的 CSS 框架 · GitHub](https://github.com/spiritov/ds.css)

**原文标题**: [GitHub - spiritov/ds.css: css framework recreating the DS / DS Lite's UI · GitHub](https://github.com/spiritov/ds.css)

ds.css 是一个用 CSS 重建任天堂 DS / DS Lite 部分界面元素的框架，提供全局与作用域样式及 Web Components，支持 unpkg、本地下载和 npm 使用。

- 🎮 项目定位：用 CSS 框架复刻 DS / DS Lite 的部分 UI 界面。
- 🌐 预览地址：css.ds.dreamyard.xyz，项目采用 MIT 许可证。
- ⚡ 最快用法：在 HTML 的 `<head>` 中通过 unpkg 引入 `https://unpkg.com/@spiritov/ds.css`。
- 📦 其他安装方式：复制 `/dist` 内容本地引入，或运行 `npm i @spiritov/ds.css`。
- 🎯 作用域样式：可引入 `ds-scoped.css`，并在父级 `div` 上添加 `class="ds-css"`，仅在局部生效。
- 🧩 Web Components：内置小部件可从 unpkg 导入，例如 `ds-calendar.js`，再使用 `<ds-calendar>`。
- 🛠️ 框架集成：小部件支持手动下载引入，也可通过 npm 在 Web 框架中使用；Svelte 中可在 `onMount` 内动态 `import`。
- 🚧 TODO：计划添加更多 PictoChat 组件和更多 DS 风格组件。
- ⭐ 仓库数据：`spiritov/ds.css` 已有 589 stars、9 forks、3 watchers、93 commits；Issues 和 Pull requests 均为 0。
- 📁 文件结构：包含 `dist`、`postcss`、`src` 等目录，以及 `README.md`、`LICENSE`、`package.json` 等文件。

---

### [首页 - 花札报告](https://hanafuda.report/?ref=frontendfocus)

**原文标题**: [Home - Hanafuda Report](https://hanafuda.report/?ref=frontendfocus)

Hanafuda Report 是一份无噪音的任天堂主题邮件通讯，每周日由关注任天堂超过 25 年的 Chris Brandrick 策划，已有超过 8000 人订阅，帮助读者掌握必读任天堂新闻。

- 📬 每周发送邮件摘要，汇集全网最佳任天堂文章、评测、视频和新闻。
- 🎮 每期包含未来一周所有将发售游戏的清单，方便玩家锁定下一款想玩的游戏。
- 🗓️ 由资深任天堂粉丝 Chris Brandrick 每周日精选编辑，定位为任天堂通讯。
- 📰 最新期包括 #499（2026 年 9 月 13 日）塞尔达、银河战士、星之卡比等；#498（2026 年 9 月 6 日）双重 Nintendo Direct 将至；#497（2026 年 8 月 30 日）Switch 2 第三方阵容延续，《艾尔登法环》到来。
- 💬 订阅者称赞其信息精确、简洁，是了解任天堂主机与游戏动态的高效必读通讯。

---

### [未找到标题](https://css.ds.dreamyard.xyz/)

**原文标题**: [No title found](https://css.ds.dreamyard.xyz/)

ds.css 是一个受 DS / DS Lite 固件启发的 CSS 框架，通过语义化 HTML 与类名搭配来构建界面，并提供按钮、颜色、网格、表单、Pictochat、日历与时钟等组件。

- 🎮 ds.css 是一个 CSS 框架，也是对 DS / DS Lite 固件的致敬。
- 📦 安装与入门请查看 GitHub 的 readme。
- 🧩 样式混合使用语义化 HTML 和类名；例如按钮用 `<button>`，更宽按钮需加 `class='button-lg'`。
- 🎨 提供 16 种主题颜色，可用类名给部分组件上色；也有对应 CSS 变量，如 `--color-ds-slate`，类名如 `ds-slate`、`ds-slate-50`。
- 📐 2 个 CSS 变量可帮助设置网格尺寸并对齐组件中的内容。
- 🪗 Accordion 的标题可以着色。
- ⏳ Alert 可与加载动画搭配使用，加载动画也可单独使用。
- 📊 Bars 应设置宽度。
- 🔘 Buttons 有 3 种宽度。
- 🔘 Radio Buttons 需要为每个 `<input>` 设置颜色才会显示为选中；`<fieldset>` 需自备容器，示例使用网格布局。
- 🖼️ Info Box、Settings、Input、Pictochat 等组件可用；Input 的 Bumpers 可放在输入框前后。
- ✨ Pictochat 有 2 个高亮类；`ds-slate-50` 版本的颜色可能更适合 Pictochat 标题。
- 📅 Calendar 和 Clock 作为 JavaScript 模块单独导入；可用 `style` 属性着色，并用 `border-hidden` 隐藏轮廓。
- 📏 Grids 应设置宽度和高度（如果其中没有内容）。

---

### [](https://github.com/SAPTARSHI-coder/EaseMotion-css)

**原文标题**: [GitHub - SAPTARSHI-coder/EaseMotion-css: Animation-first CSS framework with reusable UI components, modern effects, and zero dependencies. Lightweight, beginner-friendly, and open-source. · GitHub](https://github.com/SAPTARSHI-coder/EaseMotion-css)

EaseMotion CSS 是一个零依赖、动画优先的现代 CSS 框架，通过可读性极强的类名（如 `ease-fade-in`、`ease-slide-up`）让开发者无需构建步骤即可快速构建流畅动效界面，由 Saptarshi Sadhu 维护并采用 MIT 开源协议。

- ⚡ **核心理念**：以"能用英语说出的，就应该能写成类名"为设计哲学，动画是一等公民，类名即文档，无需查阅即可使用
- 📦 **零依赖零配置**：无构建步骤、无依赖，仅需通过 CDN 或 npm 引入单个样式文件即可使用
- 🎯 **内置资源**：提供 80+ 布局工具类、20+ 动画类、6 种按钮变体、13 种卡片变体，以及 60+ CSS 自定义属性设计令牌
- 🪶 **轻量体积**：压缩后仅 28.2 kB，原始文件 174.1 kB，兼顾性能与功能
- 🚀 **多重引入方式**：支持 CDN（jsDelivr 推荐、unpkg、GitHub Raw）、npm 安装、粒度化按需导入及模块化动画导入
- 🧩 **框架友好**：无缝兼容 React、Next.js（App Router/Pages Router）、Vue、Svelte、Astro 等，并提供专用 `<Animate>` React 包装组件
- 🎨 **SCSS 集成层**：提供 `animate()`、`transition()` 等 SCSS 混入，可在自有样式表中复用动画令牌而无需额外类名
- 🎛️ **易于定制**：通过覆盖 CSS 自定义属性即可全局换肤，并使用 `@layer` 级联层让用户样式始终优先，无需 `!important`
- 🔁 **循环动画控制**：通过 `--ease-animation-iterations` 变量可自定义 `.ease-bounce`、`.ease-pulse` 等循环动画的迭代次数
- 🌐 **浏览器兼容性**：支持现代常青浏览器（Chrome 49+、Firefox 31+、Safari 9.1+、Edge 15+、Opera 36+），不支持 IE 11 及更早版本
- ♿ **无障碍支持**：遵循 `prefers-reduced-motion` 媒体查询，在系统层面为偏好减少动效的用户最小化动画
- 🤝 **社区贡献机制**：所有提交需放入 `submissions/` 对应目录并遵循命名规范（如 `ease-hover-sap` 加唯一后缀），核心 `core/` 与 `components/` 仅限维护者编辑
- 📊 **贡献规范更新**：每位贡献者每日限制 25-100 个 PR，最多同时认领 2 个活跃 issue，需遵循 Conventional Commits 提交规范并压缩提交历史
- 🌟 **GSSoC 2026 支持**：开放 500 个全新已批准 issue（#59099 至 #59610），欢迎新手通过 `good first issue` 标签入门
- 🗺️ **路线图清晰**：v1.0 已发布核心工具与动画库，v1.1 进行中（React 组件库、SCSS 模块化、Next.js 模板），v1.2+ 规划表单组件、暗色模式、模态框与滚动触发动画
- 👥 **社区活跃**：已拥有 644 位贡献者、268 颗 Star 和 1.1k 次 Fork，累计超过 100,000 次提交

---

### [EaseMotion CSS — 文档](https://saptarshi-coder.github.io/EaseMotion-css/)

**原文标题**: [EaseMotion CSS — Documentation](https://saptarshi-coder.github.io/EaseMotion-css/)

EaseMotion CSS 是一个以动画优先、人类可读的 CSS 库，用接近英语的类名编写 UI，无需记忆工具类或复杂配置；它无依赖、无构建步骤、无需 JavaScript，并提供可选 Motion Engine、组件、工具类与贡献规范。

- 📢 维护者公告（2026 年 8 月）：所有贡献者账号已解封，仓库范围软封禁已移除。
- 🚦 公告称每日贡献 PR 上限为 100 个/贡献者；GSSoC 新增 500 个已批准议题（#59099–#59610），位于 `submissions/examples/`。
- 🧠 设计哲学：人类可读（如 `ease-fade-in`）、动画优先、可组合、干净最小。
- 📦 安装方式一：CDN 最快，推荐 jsDelivr，也支持 npm、unpkg、GitHub Raw CDN。
- 🧩 安装方式二：npm 安装 `easemotion-css`，可在 HTML 链接或 CSS 中 `@import`。
- 🎛️ 安装方式三：按需加载 `core/variables.css`、`base.css`、`animations.css`、`utilities.css` 及组件样式。
- 🌀 安装方式四：模块化动画导入；必须先加载 `easemotion/variables.css`，再加载 `fade.css`、`slide.css` 等或 `all.css`。
- ⚙️ Motion Engine 为可选 JS 运行时：通过 `em=""` 属性在 HTML 中描述动画，运行时解析、编译并注入优化 CSS。
- 🔤 `em` 属性令牌：动画名（必需）、时长（默认 300ms）、缓动（默认 ease）、延迟（默认 0ms）、重复（默认 1）、填充模式（默认 both）。
- 🧰 引擎可用独立 API：parser、compiler、optimizer；`className` 生成稳定类名，`optimizeHtml` 可构建时 tree-shaking，示例节省 42.3%。
- 🎨 变量通过 `:root` CSS 自定义属性定义，并支持 `prefers-color-scheme` 深色模式。
- 🧱 工具类涵盖间距、布局、flex、grid、排版；视觉工具包括 backdrop blur、blend modes、mask、text stroke、gradient text、highlight。
- ✨ 动画示例：`ease-fade-in`、`ease-slide-up`、`ease-bounce`、`ease-hover-grow`、`ease-flip-3d`、`ease-shimmer-text`、`ease-mask-reveal`。
- 🧩 组件包括按钮、卡片、滚动进度、表单；表单支持验证状态、尺寸变化与深色模式。
- 🤝 贡献为策展制：不改核心样式，提交自包含 demo，由维护者标准化和整合。
- 📁 提交必须放在 `submissions/examples/your-feature-name-xx/`，遵循三文件规则：`demo.html`、`style.css`、`README.md`。
- 🏷️ 文件夹用 kebab-case 并加唯一后缀；`demo.html` 必须浏览器直接打开，无 CDN/外部框架；`style.css` 不需预先加 `ease-` 前缀。
- 📝 `README.md` 必须回答：这是什么、如何使用、为什么有用。
- 🚫 严禁直接编辑 `core/`、`components/`、`docs/`、`examples/`，只能在 `submissions/examples/` 提交，否则 PR 自动关闭。
- 📌 严格仓库规则：最多 2 个活跃分配议题；24 小时无进展自动取消分配；PR 每日上限 25；提交前 squash 提交。
- ✅ bug、功能请求与分配均通过 GitHub Issues；Discord 可选；集成后的类名统一使用 `ease-` 前缀，沙盒提交阶段可先用自定义类名。

---

### [面向设计工程师的 UI 技能 | UI 技能](https://www.ui-skills.com/)

**原文标题**: [UI Skills for Design Engineers | UI Skills](https://www.ui-skills.com/)

UI Skills 是一个面向人类与 AI 智能体的设计工程技能集合，旨在帮助创建更好的界面。它提供 CLI、MCP 接入方式，以及可按主题、技术栈和意图路由的 UI 技能目录，并附带实用 Playbook。

- 🧰 UI Skills 汇集设计工程技能，服务人类与智能体，提升界面创建质量。
- 🚀 Agent 可从“start here”开始，通过 CLI 或 MCP 连接 UI Skills 目录。
- 🧭 根技能 ui-skills-root 根据主题、技术栈和意图，将需求路由到最小可用技能集。
- 🔍 审计与改进类技能包括 improve-ui、improve-animations、improve-react、improve，通常只读源码并生成自包含实施计划，不直接修改代码。
- 🎨 前端设计类技能包括 frontend-design、better-ui、impeccable、bencium-innovative-ux-designer、gpt-tasteskill，强调生产级、非通用 AI 审美与高设计质量。
- 📊 界面与交互类技能包括 interface-design、design-lab、ui-ux-pro-max、interaction-design、12-principles-of-animation，覆盖仪表盘、SaaS、微交互、动效原则等。
- ✅ 质量与规范类技能包括 web-design-guidelines、rams、frontend-ui-engineering，关注可访问性、间距、排版、对比度、组件架构与可维护性。
- 👥 技能由多个作者与团队贡献，如 ibelick、anthropics、emilkowalski、shadcn、antfu 等。
- 📘 Playbook 提供实用规则：用 aspect-ratio 防止布局偏移、用 text-balance/text-pretty 优化文本、用 tabular-nums 对齐数字、触控目标至少 44×44px。
- 🔗 页面提供“See skills”和“See playbook”入口，可浏览完整技能与手册。

---

### [PDF 数据提取：将 PDF 转换为结构化 JSON](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-data-extraction-api-structured-json/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260916-)

**原文标题**: [PDF Data Extraction: Turn PDFs into Structured JSON](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-data-extraction-api-structured-json/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260916-)

Google Document AI 的七款处理器将于 2026 年 6 月退役，促使团队寻找替代方案。本文从集成设置、提取架构、输出模式和数据驻留等方面，对比 Foxit PDF Structural Extraction API 与 Google Document AI，提供真实实现细节而非功能清单，以帮助决策。

- 📅 Google Document AI 七款处理器计划于 2026 年 6 月退役，推动团队评估替代方案。
- 🔍 对比对象为 Foxit PDF Structural Extraction API 与 Google Document AI。
- ⚙️ 比较重点包括集成设置、提取架构、输出模式和数据驻留。
- 🧩 目标是基于实际实现细节做选择，而不是只看功能列表。

---

### [STRICH | 适用于 Web 应用的条形码扫描](https://strich.io/?ref=frontend-focus)

**原文标题**: [STRICH | Barcode scanning for web apps](https://strich.io/?ref=frontend-focus)

STRICH 是面向 Web 应用的 JavaScript SDK，可在浏览器中通过摄像头实时扫描 1D/2D 条码，强调完全客户端处理、无需后端、易集成与企业级支持。它由瑞士 Pixelverse GmbH 开发，提供免费 14 天试用、透明定价，并适用于从个人开发者到大型企业的多种场景。

- 🌐 浏览器内运行：为 Web 应用添加条码扫描，图像处理全在客户端完成，无需后端。
- 📦 安装方式：`npm install @pixelverse/strichjs-sdk`，也提供演示应用和免费 14 天试用。
- 🇨🇭 瑞士制造：STRICH 是德语“stroke”的意思，由 Pixelverse GmbH 开发。
- 🧩 开发者友好：零依赖，兼容主流框架，文档完善，提供 TypeScript 类型绑定。
- 🏷️ 支持 1D 条码：Code 128、EAN、UPC、Code 39、Code 93、ITF、Databar、Codabar。
- 🔳 支持 2D 条码：QR Code、Data Matrix、Aztec Code、PDF417，包括美国驾照等。
- 📷 内置扫描 UI：包含瞄准覆盖层、相机选择、闪光灯、点击对焦；Popup Scanner 可一行代码调用。
- 🛠️ 复杂条码读取：可处理褪色、损坏、光照不均、低光、反色条码，优于 ZXing-JS 和 Quagga 等方案。
- 📱 Web 扫码优势：绕过应用商店、链接或二维码分发、跨平台单代码库、降低成本、减少应用疲劳。
- 🚀 PWA 能力：可安装到主屏幕，支持离线运行和推送通知，提升参与度与留存。
- ⚙️ 现代 Web 技术：基于 WebAssembly 和 WebGL，兼容 Android/iOS 主流浏览器及高低端设备。
- 💬 客户评价：强调快速、可靠、易集成和支持优秀，用户包括 Thoughtbot、Brooklyn Public Library、SBB、Zeercle 等。
- 🏢 企业就绪：定期维护、创始人支持、可预测年费、采购友好、支持采购订单和银行转账。
- 🔒 安全合规：可选 Offline Operation 实现零网络流量，零依赖降低供应链风险，NPM 使用 Trusted/Staged 发布。
- ✅ GS1 支持：Pixelverse GmbH 是瑞士注册 GS1 Solution Partner，支持 GS1 条码标准。
- 💶 定价：Basic €99/月含 10k 扫描；Professional €249/月含 100k 扫描；Business 起 €4,000/年无限扫描与设备；Enterprise 按需报价。
- 📈 超限政策：不会拒绝扫描，连续两个月超限会提示升级；订阅包含最新版本更新。
- ⏱️ 集成通常不到一天，可先体验演示应用或开始免费试用。

---

### [](https://page-rage.com/)

**原文标题**: [Page Rage](https://page-rage.com/)

Break 是一款可改造任意网页的浏览器扩展，支持 Chrome、Firefox、Edge，Safari 版即将推出；同时提供无需安装、任意浏览器可用的预制页面，并附带一组主题/页面名称。

- 🧩 可对任意网页使用 Break
- ⚙️ 需安装浏览器扩展
- 🌐 支持 Chrome、Firefox、Edge
- 🍎 Safari 版本即将推出
- 🎬 可观看预告片
- 📄 提供 Break 预制页面
- 🚀 无需安装，任何浏览器均可使用，效果出色
- 🎭 预制页面/主题包括 Rageit、The Daily Dread、Discontent、Envy、Nest、Pain Mail

---

