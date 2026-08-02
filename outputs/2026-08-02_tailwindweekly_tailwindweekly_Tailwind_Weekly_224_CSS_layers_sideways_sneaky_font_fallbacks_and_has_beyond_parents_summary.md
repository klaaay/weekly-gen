### [Setapp | 适用于 Mac 和 iOS 的强大应用](https://setapp.com/?irgwc=1&afsrc=1&iradid=343321&irpid=2662107&utm_content=ONLINE_TRACKING_LINK&utm_campaign=Vivian+Guillen&sharedid=&utm_medium=affiliate&mpaid=3&utm_source=impactradius&campaign=impactradius&type=home)

**原文标题**: [Setapp | Powerful apps for Mac & iOS](https://setapp.com/?irgwc=1&afsrc=1&iradid=343321&irpid=2662107&utm_content=ONLINE_TRACKING_LINK&utm_campaign=Vivian+Guillen&sharedid=&utm_medium=affiliate&mpaid=3&utm_source=impactradius&campaign=impactradius&type=home)

Setapp 推出单一应用订阅及包含数百款精选 Mac/iOS 应用的会员服务，文章介绍热门应用、订阅方案、使用方式、用户评价和平台优势。

- 🆕 全新单一应用订阅，也可选择全套会员
- 📱 数百款 Mac/iPhone 应用，含 AI 工具，7 天免费试用
- 🧰 推荐应用：Bartender、TextSniper、CleanMyMac、CleanShot X、Craft、Nitro PDF Pro
- 💰 三种方案：Mac $14.99/月、Mac+iOS $18.99/月、Power User $22.99/月，含 AI 积分
- 🚀 三步开始：安装 Setapp、选择应用、订阅
- 😊 用户好评：应用丰富、无病毒、性价比高、每月更新
- ✅ 精选应用、免费更新、无广告、应用指南、用户评价
- ❓ 常见问题：数据隐私、企业计划等

---

### [Thinking Horizontally in CSS @layer – Master.dev Blog](https://master.dev/blog/thinking-horizontally-in-css-layer/?ref=tailwindweekly.com)

**原文标题**: [Thinking Horizontally in CSS @layer – Master.dev Blog](https://master.dev/blog/thinking-horizontally-in-css-layer/?ref=tailwindweekly.com)

CSS @layer 的另一种思考方式：与其执着于垂直的层叠顺序，不如把组件视为水平并列的“两层结构”，通过将自定义属性放入 layer 中使其“刻意变弱”，从而让任何未分层样式都能轻松覆盖，避免特异性冲突。

- 🧱 **@layer 本质是垂直的层叠机制**：层与层之间按顺序或显式声明决定优先级，不受选择器特异性影响。
- 📚 **子层语法用点号表示**：例如 `@layer components.button`，子层仍归属父层，但内部顺序默认靠源码顺序。
- 🗂️ **组件数量众多时，垂直顺序不再重要**：几十上百个组件各自独立，组件间谁覆盖谁通常毫无意义。
- 🧩 **每个组件可混合“分层”与“未分层”样式**：用 `@layer` 包裹自定义属性（tokens），用 `@scope` 或类嵌套保护组件内部结构。
- 🎯 **核心技巧是让 tokens 故意变弱**：将自定义属性放入 layer 后，未分层的普通选择器（哪怕特异性很弱）也能轻松覆盖，无需 `root.root` 这类斗争。
- ↔️ **“水平思考”取代“垂直焦虑”**：每个组件本质上只是一个“两层堆栈”，整体看来是短而胖的水平结构，而非数百层的垂直金字塔。
- 💼 **CodePen 实际案例**：使用 `.module.scss`，组件根节点统一叫 `.root`，所有自定义属性放入 `@layer`，极大方便全局覆盖与主题调整。
- 💬 **评论区的澄清**：后定义的 layer 更强，未分层样式最强；组件间覆盖不重要，重要的是让组件内部的关键部分易于被外部覆盖。

---

### [](https://csswizardry.com/2026/04/font-family-doesnt-fall-back-the-way-you-think/?ref=tailwindweekly.com)

**原文标题**: [font-family Doesn’t Fall Back the Way You Think – CSS Wizardry](https://csswizardry.com/2026/04/font-family-doesnt-fall-back-the-way-you-think/?ref=tailwindweekly.com)

概述：本文探討了 `font-family` 回退機制中一個常被誤解的細節：當子元素指定了單一網頁字型時，瀏覽器不會繼承父層的字型堆疊，而是僅在該元素自己的宣告中尋找回退，若找不到就會落到瀏覽器預設的 Times 字型，導致突兀的文字閃現或版面位移。解法是每次宣告 `font-family` 時都寫完整的字型堆疊。

- ✍️ `font-family` 雖然是繼承屬性，但一旦在子元素上單獨宣告，就會「自我封閉」，不再參考父層的字型堆疊。
- 🔍 若子元素只寫 `font-family: "Open Sans"`，在字型載入完成前，瀏覽器只會從「這一行」找替代，找不到就退回瀏覽器預設（通常是 Times / Times New Roman）。
- ⚠️ 這就是為什麼常看到標題先閃現 Times 字型，而非預期的系統 sans-serif 字型；瀏覽器並沒有忘記父層設定，而是嚴格照子元素的宣告執行。
- 🛠️ 修正方法很簡單：每次指定 `font-family` 時都補上完整的字型堆疊，例如 `"Clan Pro", sans-serif`，至少加上通用字型家族，避免回退錯誤。
- 📋 文中列舉的設計系統變數（如 `--hero-hero`、`--heading-x-large`）都只寫了單一字型名稱，需要全部改成帶有 `sans-serif` 的完整堆疊。
- 📈 這個小細節影響不小：除了視覺上突兀的 serif/sans 混搭，若回退字型與網頁字型在寬高或比例上差異過大，還可能造成 CLS（版面位移）分數變差，影響 Core Web Vitals。
- 💡 作者建議：凡是值得覆寫的 `font-family`，就值得寫完整定義；這類看似微不足道的細節，常是大型專案難以定位的效能或體驗問題來源。

---

### [: :has() 不仅仅是父选择器 - YouTube](https://www.youtube.com/watch?v=cxSowU9sDdU&ref=tailwindweekly.com)

**原文标题**: [:has() is more than a parent selector - YouTube](https://www.youtube.com/watch?v=cxSowU9sDdU&ref=tailwindweekly.com)

overview summary
這是 YouTube 頁面底部的常用連結清單，涵蓋平台簡介、媒體服務、法律條款、合作機會與公司資訊。

- 📄 提供平台簡介與媒體相關資訊
- ⚖️ 說明著作權規範與法律條款
- 📞 提供聯絡管道與創作者支援
- 📢 包含廣告合作與開發人員選項
- 🔒 列出隱私權、政策與安全性說明
- 🧪 介紹 YouTube 運作方式與新功能測試
- ©️ 標示 2026 Google LLC 版權所有

---

### [](https://orshot.com/?ref=tailwindweekly.com)

**原文标题**: [Orshot – Automate Image, PDF & Video Generation via API](https://orshot.com/?ref=tailwindweekly.com)

Orshot 是一个面向营销团队与代理机构的创意自动化平台，核心是让用户通过模板一次设计，即可自动生成品牌统一的图片、多页 PDF 和视频，并支持通过 API、Zapier、Make、n8n 或白标编辑器嵌入工作流，大幅提升视觉内容生产效率。

- 🎨 从模板到全格式输出：在 Orshot Studio 中构建一次模板，即可渲染为图片、多页 PDF 或 MP4 视频；支持从 Canva、Figma 导入，并可标记动态参数实现个性化生成。
- 🧩 海量预设模板：提供超过 2,000 个预设计模板，覆盖社交媒体帖子、广告横幅、证书、演示文稿、电商视觉等，帮助用户快速上手并上线渲染。
- ⚙️ 内置自动化工作流：支持按计划、电子表格或 Webhook 触发，从 Google Sheets、Airtable、Shopify 等数据源拉取实时数据，并在平台内完成渲染、发布、重试与运行监控，无需额外工具链。
- 🔌 广泛集成与连接：兼容 Zapier、Make、n8n、Pipedream 等无代码工具，同时提供 REST API、SDK、动态 URL、签名 URL 和 CLI，方便开发团队灵活集成。
- 🤖 AI 智能体支持：提供 MCP 服务器地址，开发者可让 Claude、ChatGPT、Cursor 等 AI 代理直接生成品牌模板、批量渲染或发布到社交平台，免去自建图像基础设施。
- 🧩 白标嵌入式编辑器：可将 Orshot Studio 嵌入 React/Vue 应用，支持白标品牌定制、多租户、Webhook 事件、权限管理、多语言，让用户在自己产品内完成设计、渲染与发布。
- 👥 团队与企业功能：提供无限工作空间（按客户/活动隔离）、团队协作、审计日志、详细渲染日志与用量洞察，并支持自带 S3/R2 存储，确保安全与可控。
- 💬 客户口碑验证：多位用户表示从 Templated.io、BannerBear、Canva、Abyssale 等工具迁移到 Orshot，认为其编辑器、API、动画、AI 集成和支持服务更胜一筹。
- 💰 灵活的定价模式：免费提供 30 积分（无需信用卡）；付费方案包括 Launch（$39/月，1,500 积分）、Grow（$160/月，20,000 积分）、Scale（$349/月，75,000 积分）；另可选择 $12/月/账户的社交发布附加服务，以及企业定制方案。
- ❓ 常见问题涵盖免费使用、模板创建、集成方式、工作空间、积分机制、失败渲染不收费、邀请团队成员和工作空间数量限制等。

---

### [Remocn - 使用你的AI智能体制作产品演示视频](https://remocn.dev/?ref=tailwindweekly.com)

**原文标题**: [Remocn - Make a product demo video with your AI agent](https://remocn.dev/?ref=tailwindweekly.com)

overview summary
- 🎬 remocn 让 AI 代理根据你的描述自动生成产品演示视频，无需剪辑软件或动效基础。
- 🤖 只需在空文件夹中打开 AI 代理（如 Claude Code、Cursor），粘贴提示即可完成项目搭建并启动预览。
- ⚡ 视频由预制组件拼装，在浏览器中实时生成，你可用自然语言提出修改，秒级更新。
- 💰 相比传统动效设计（约 600 美元+两周），remocn 只需一个提示词和一下午，完全免费（MIT）。
- 🧩 提供五种构建块：动态文字、着色器背景、转场、动画图标和 UI 原型，供代理自由组合。
- 📦 生成代码完全归你所有，无账户、无运行时依赖、无锁定，可轻松复制进仓库。
- 🏆 已获 shadcn、OrcDev 等众多开发者好评，社区支持活跃，260+ 组件持续增长。
- 📖 无代码经验也能上手，初始设置约 10 分钟，熟悉后每支视频制作不超过 1 小时。
- 📧 遇到问题可邮件求助，社区与赞助商共同维护项目发展。

---

### [](https://www.pikapods.com/?utm_source=tailwind-weekly&utm_medium=newsletter&utm_campaign=first&ref=tailwindweekly.com)

**原文标题**: [PikaPods - Instant Open Source App Hosting](https://www.pikapods.com/?utm_source=tailwind-weekly&utm_medium=newsletter&utm_campaign=first&ref=tailwindweekly.com)

PikaPods 是一个专注于开源应用托管的平台，提供简单、隐私友好的服务，用户无需自己管理服务器即可运行 n8n、Immich、Actual 等应用。起步价仅为 $1.80/月，并赠送 $5 新用户额度，支持自定义域名、自动更新及多种资源配置，同时通过收入分成支持开源开发者。

- 💰 起步价仅 $1.80/月，新用户可获 $5 欢迎额度，完全托管且持续更新
- 🚀 精选开源应用一键部署，如 n8n 自动化工具、Immich 相册管理、Actual 财务应用
- 🔒 数据隐私优先：无广告、无追踪、无监控，仅提供托管服务
- 🌍 支持欧盟和美国数据中心，也可绑定自己的域名
- 🛠️ 无需技术技能即可上手，所有配置、数据库和更新均在后台自动完成
- 💾 通过 SFTP 随时下载数据，无供应商锁定，可自由迁移
- 🤝 将 20% 收入分享给开源项目作者，助力开源生态
- 🖥️ 统一界面管理所有应用，可灵活调整 CPU、内存和存储资源
- 📊 透明定价，按实际用量付费，并提供多种配置选择

---

### [](https://www.obdev.at/products/microsnitch/index.html?ref=tailwindweekly.com)

**原文标题**: [Micro Snitch](https://www.obdev.at/products/microsnitch/index.html?ref=tailwindweekly.com)

Micro Snitch 是一款面向 Mac 的超轻量菜单栏应用，可在后台持续监控麦克风与摄像头的使用状态，并在有应用调用这些设备时立即提示用户，同时支持日志记录以便事后追踪可疑活动，帮助用户防范偷拍或窃听。

- 🎤 实时监控麦克风与摄像头：任何应用调用设备时，都会在菜单栏显示当前活动状态。
- 📷 弥补系统不足：摄像头指示灯可能看不到，麦克风更是完全没有活动提示，Micro Snitch 可填补这一盲区。
- 🖥️ 屏幕覆盖提示：当麦克风或摄像头被开启时，屏幕上会显示醒目覆盖层，确保你不会错过提醒。
- 📜 日志记录功能：即使你不在电脑前，所有设备状态变化也会写入日志，方便事后查看可疑活动。
- 🔍 隐私守护定位：专门帮助你判断是否有人在未经允许的情况下通过你的 Mac 进行偷拍或窃听。
- 🛍️ 获取方式：支持免费下载试用，也可通过 Mac App Store 购买。

---

### [MXroute — 为您的域名提供邮件托管服务](https://mxroute.com/?ref=tailwindweekly.com)

**原文标题**: [MXroute — Email Hosting for Your Domains](https://mxroute.com/?ref=tailwindweekly.com)

MXroute 是一家自 2013 年起独立运营的邮件托管服务商，主打“无废话”的可靠邮件服务，提供无限域名和账户，按年付费，无隐藏费用与按席位收费。

- 📧 核心服务：提供 SMTP、IMAP、POP3 完整协议，支持别名、转发、Sieve 过滤等标准邮件功能。
- 🌐 无限资源：所有套餐均包含无限域名与无限账户，仅按存储空间区分价格。
- 🛡️ 高投递率：使用高信誉 IP 池，若因 IP 信誉导致投递失败，服务商负责重新发送。
- 🔒 安全与监控：频繁安全审计、真实物理监控，结合自定义 SpamAssassin 规则与持续日志审计来过滤垃圾邮件。
- 👨‍💻 人工支持：无聊天机器人，由运营者本人处理工单，期望用户具备邮件基础知识。
- 💰 定价方案：小 10GB（$59/年）、中 25GB（$69/年）、大 50GB（$79/年），每账户限 400 封/小时。
- 📦 大存储选项：从 100GB 到 1TB 不等，年付或月付，适合企业与大容量用户。
- 🔄 转售计划：提供白标控制面板、客户登录、自定义品牌与定价，基础设施由 MXroute 维护。
- 🏢 公司背景：2013 年由 Jarland Donnell 和 Ryan Arp 创立，至今保持独立，无投资方或退出计划。

---

### [](https://2fas.com/?ref=tailwindweekly.com)

**原文标题**: [2FAS — Authenticator and Password Manager](https://2fas.com/?ref=tailwindweekly.com)

2FAS 是一款本地优先的密码管理器与双因素认证（2FA）应用，强调隐私与安全，无需账户、匿名使用，数据仅存于设备端，并通过开源、零知识加密等机制保护用户信息，广受好评。

- 🔐 密码与 2FA 令牌全部存储在你的设备本地，无服务器即无数据泄露风险。
- 🏆 获 PCMag 推荐，2FAS Pass 与 2FAS Auth 平均评分 4.7，下载量超 600 万次。
- 🕶️ 无需账户、100% 匿名使用，支持云端及手动备份，并提供三级安全层级控制。
- 🔧 支持令牌自定义（分组、徽章、图标与标签），并可通过浏览器扩展安全共享密码。
- 📱 原生 iOS/Android 应用，兼容 Apple Watch，支持离线使用，加密密钥仅归用户所有。
- 🔓 开源且源代码可查，加密白皮书公开算法与设计决策，确保完全透明。
- 💬 社区评价极高：用户称赞其免费、无广告、无隐藏订阅、界面简洁、迁移与恢复便捷。
- 👥 活跃社区驱动开发：GitHub 代码审阅、Discord/Reddit 互助、众包翻译及捐赠支持。
- 🛡️ 自 2015 年起以安全与隐私为核心，坚持“安全在心、隐私为设计”理念。

---

