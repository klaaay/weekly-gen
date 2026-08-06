### [CSS 现状 2026](https://2026.stateofcss.com/en-US/)

**原文标题**: [State of CSS 2026](https://2026.stateofcss.com/en-US/)

2026 年 CSS 现状调查揭示了 CSS 生态系统的显著发展，其中 Anchor Positioning 成为最受关注的新特性，但也因浏览器支持问题而让开发者却步。此外，AI 在 CSS 编写中的应用仍处于较低水平，CSS 被视为一门独特且持续演进的语言。

- 📊 调查于 2026 年 5 月 15 日至 6 月 29 日进行，共回收 4,902 份回复
- 🧩 CSS 2026 已支持页面过渡、masonry 布局，甚至能模拟微处理器和渲染 Doom，当然也能居中的 `<div>`
- 📌 Anchor Positioning 被评为最受欢迎的新 CSS 特性，同时也是开发者因浏览器支持问题最想用却避免的特性
- 👍 其他热门特性包括 `:has()`、CSS Nesting、`@container` 尺寸查询、View Transition API 等
- ⚠️ 浏览器支持滞后是核心痛点，View Transitions、`if()` 等特性同样面临此问题，Interop 等项目正在努力改善
- 🤖 AI 趋势：CSS 仍以手动编码为主，平均仅 28% 的 CSS 代码由 AI 生成，多数评论认为 AI 尚不擅长编写优质 CSS
- 🌟 CSS 被视为一门独特语言，其长期演变过程令人着迷，完整调查结果提供了更全面的数据

---

### [TREX：运行你的代码的 AI 代码审查 | Greptile](https://www.greptile.com/trex?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=frontendfocus_primary_aug5)

**原文标题**: [TREX: AI Code Review That Runs Your Code | Greptile](https://www.greptile.com/trex?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=frontendfocus_primary_aug5)

TREX 是 Greptile 推出的 PR 运行时验证工具，能在沙盒环境中实际运行你的 PR 分支，找出只有运行时才会暴露的 Bug，并附上日志、截图等证据直接评论到 PR 上；相比纯代码审查，可多捕获约 20% 的运行时问题。

- 🧪 TREX 會在沙盒中實際執行 PR 分支，偵測僅在運行時出現的錯誤。
- 🔍 第一步：自動理解 PR 變更、程式庫、測試套件與技術棧，判斷需要執行什麼。
- ⚙️ 第二步：啟動服務、開發伺服器、Mock 輸入、API 呼叫與瀏覽器代理來執行測試。
- 🐛 第三步：失敗時追蹤到相關程式碼，並在 PR 上留下附有證據的評論。
- 📸 每個發現都會附上 logs、截圖、追蹤、影片或 API 輸出，不只說失敗，更展示失敗過程。
- 🧩 支援與既有專案相同的依賴、框架與測試設定，無需大幅改動。
- 🖱️ 具備端到端測試能力，可模擬輸入、啟動 dev server，並用瀏覽器代理點擊 UI 流程。
- 📈 相較於僅做 code review，TREX 能多抓約 20% 的執行期 bug。
- 🚀 提供 14 天免費試用，無需信用卡；另有 Agent、獨立驗證與個人化學習等 Greptile 功能。

---

### [](https://www.bram.us/2026/07/30/styling-the-navigation-declarative-route-and-navigation-matching-in-css/)

**原文标题**: [Styling the Navigation: Declarative Route and Navigation Matching in CSS – Bram.us](https://www.bram.us/2026/07/30/styling-the-navigation-declarative-route-and-navigation-matching-in-css/)

概述：Chrome 團隊提出了一項 CSS 新規範，用於以宣告式方式匹配路由與導覽狀態，讓開發者不需撰寫複雜 JavaScript 即可依據「從哪來、到哪去」來設定樣式與 View Transitions，目前已開放反饋並可在 Chrome Canary 中試用。

- 🧭 此提案旨在解決 MPA View Transitions 中需用 JavaScript 攔截導覽、解析 URL、動態設定轉場類型的繁瑣問題。
- 📍 新增 `@route` 規則，可透過 `url-pattern()` 定義具名路由，支援 `pathname`、`search` 等描述符，語法基於 path-to-regexp。
- 🔀 新增 `@navigation` at-rule，可查詢目前導覽的 `from` 與 `to` 端點，並搭配 `@view-transition` 設定不同轉場效果。
- 🖱️ 引入 `:nav-source` 偽類，可選中觸發離開導覽的來源元素，類似 `NavigateEvent.sourceElement`。
- 🔗 新增 `:link-to()` 選擇器，可依連結目標路由來設定樣式，但目前尚不支援參數比對。
- 💬 團隊將於 CSS Working Group 柏林會議討論此提案，並徵求開發者意見，歡迎到 w3c/csswg-drafts#12594 提供反饋。
- 🧪 此功能可於 Chrome Canary 開啟 Experimental Web Platform Features 旗標進行實驗。

---

### [](https://css-tricks.com/css-gap-decorations-now-available/)

**原文标题**: [Gap Decorations Are Now Available, Here’s What’s New | CSS-Tricks](https://css-tricks.com/css-gap-decorations-now-available/)

CSS Gap Decorations 已在 Chrome/Edge 149 等 Chromium 浏览器中正式可用，它让开发者无需再靠 border 和伪元素 hack 就能直接装饰 grid 与 flexbox 的间隙。文章介绍了该特性从早期预览以来的 API 调整，并通过六步示例演示了如何使用行/列规则、自动重复、规则连接、可见性控制与覆盖顺序等功能。

- 🚀 Chrome/Edge 149 起全面支持 CSS gap decorations，可原生装饰 grid 和 flexbox 的间隙。
- 📐 特性扩展了 `column-rule`，新增 `row-rule` 和规则简写 `rule`，支持在水平和垂直两个方向绘制装饰线。
- 🔄 早期属性改名：`row-rule-outset`/`column-rule-outset` 变为 `row-rule-inset`/`column-rule-inset`，语义改为从边缘向内缩进。
- 🧩 新增精细控制 longhand 属性：`row-rule-inset-cap/junction/start/end` 及对应 `column-rule-*`，可分别调整末端、交叉点与起止位置。
- 🖌️ `gap-rule-paint-order` 改名为 `rule-overlap`，用于控制行/列规则交叉时的层叠顺序。
- 👁️ 新增 `rule-visibility-items`，可控制是否在空内容区域旁绘制间隙规则。
- 🌐 其他浏览器引擎已参与标准讨论，未来有望跨浏览器互操作；现在可将其视为渐进增强，或使用开发中的 polyfill。
- ♾️ 使用 `repeat(auto)` 可让分隔线数量随新增 section 自动适配，无需手动硬编码。
- 🧮 在 flex/grid 布局中可用 `rule` 简写添加装饰，并通过 `overlap-join` 让行列规则在交汇处整齐连接。
- 🧹 `rule-visibility-items: around` 可避免空网格单元旁出现悬空装饰线。
- 📏 `column-rule-inset` 可缩短分隔线以留出呼吸空间；`column-rule-inset-cap` 可单独控制两端缩进。
- 🔀 `rule-overlap: column-over-row` 可让列规则覆盖行规则，自定义交叉处的视觉层级。
- 🧪 可通过 interactive playground、MDN 文档和更多 demo 上手体验每个属性。

---

### [](https://2026.html.energy/)

**原文标题**: [HTML Day â August 8th, 2026](https://2026.html.energy/)

HTML Day 2026 是一年一度的 HTML 庆祝活动，将于 2026 年 8 月 8 日（星期六）在全球各地举行，鼓励人们线下聚会、写作和分享 HTML，并欢迎各地组织者自主发起活动。

- 🌐 活动定于 2026 年 8 月 8 日（星期六），全球各地将同步举办 HTML 写作与庆祝聚会。
- 📋 若你的城市未出现在列表中，可自行组织活动，并通过提交城市、时间、地点、组织者等资讯登记。
- 🎨 组织者需先制作包含活动信息的 HTML 海报或网站，可参考往届范例获取灵感。
- ✉️ 提交信息时需提供城市、日期、时间、组织者姓名与邮箱、Instagram 账号、具体地点及活动链接，并可选择活动“能量”主题。
- ✅ 提交前可预览确认所有资讯无误，通过审核后活动会列在官网，并鼓励自行宣传。
- ❤️ HTML Day 由社区驱动，由 Laurel Schwulst 与 Elliott Cost 于 2019 年发起的 HTML Energy 组织，与任何公司或机构无隶属关系。
- 🤝 活动依赖各地组织者共同促成，也欢迎赞助支持；有兴趣者可联系 sponsor@html.energy。
- 💡 帮助方式包括：在城市组织活动、加入 Patreon、推荐公司赞助、向亲友宣传，或参加任意城市的活动。
- 📲 可订阅邮件列表，并关注 Instagram、Bluesky、Twitter 获取最新活动动态与 HTML 梗图。
- 🖼️ 官网展示了往届活动照片和 HTML 相关梗图，也欢迎投稿 meme@html.energy。
- 🏢 赞助方包括 t4t.social 与 Neocities，分别提供跨性别友善社群及重现网页创意表达的服务。
- 🌍 更多相关链接包括 Are.na、Special Fish、Instagram、Bluesky、Twitter 与 YouTube；页面由 HTML Energy 制作。

---

### [](https://developer.chrome.com/blog/new-in-chrome-151)

**原文标题**: [New in Chrome 151  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-151)

Chrome 151 版本更新引入了三项关键功能：全新的 `<usermedia>` 能力元素、声明式 Shadow DOM 的插槽分配属性，以及面向单页应用的新性能指标，帮助开发者更便捷地处理用户媒体权限、组件封装和性能监控。

- 📷 **新增 `<usermedia>` 元素**：以声明式方式管理摄像头和麦克风权限，无需手动调用 `getUserMedia()`，浏览器自动处理用户意图、权限提示和媒体流传递。
- 🧩 **Shadow DOM 插槽分配增强**：支持在 `<template>` 上使用 `shadowrootslotassignment="manual"` 属性，实现纯 HTML 的手动插槽分配，无需编写 JavaScript，且与 Firefox 和 Safari 兼容。
- ⚡ **新增软导航与交互性能指标**：引入 `soft-navigation` 和 `interaction-contentful-paint` 两种 PerformanceEntry，用于追踪 SPA 中由交互触发的路由变化和内容绘制延迟。
- 🔧 **可配合 PerformanceObserver 使用**：开发者可通过 `PerformanceObserver` 监听新的性能条目，并利用 `buffered` 选项获取页面之前的软导航记录。
- 📚 **更多资源与订阅**：如需了解完整更新，可查看 Chrome 151 发布说明和 ChromeStatus 更新，并订阅 Chrome Developers 频道获取后续版本信息。

---

### [每次更新，更加强大](https://blog.google/security/chrome-stronger-with-every-update/)

**原文标题**: [Stronger with every update: How we’re making Chrome and the web safer in the AI Era](https://blog.google/security/chrome-stronger-with-every-update/)

overview summary  
Chrome 安全团队在 AI 时代利用大语言模型（LLM）全面升级漏洞的发现、分类、修复与发布流程，显著提升安全响应速度，并通过内存安全、主动防护与生态协作，构建更安全的浏览器与网络环境。  

- 🔍 **AI 驱动漏洞发现**：Chrome 安全团队自 2023 年起将 LLM 用于模糊测试，2024 年推出 Naptime，2025 年与 DeepMind、Project Zero 合作开发 Big Sleep，成功发现 V8 引擎和图形栈漏洞；2026 年更是用 Gemini 挖出一个潜伏 13 年的沙箱逃逸漏洞。  
- 🛠️ **增强代理能力**：通过模型互操作、构建包含历史 CVE 和 Git 历史的 Chrome 知识库、引入 SECURITY.md 与“评论家”代理、多次运行模型等，大幅提升漏洞挖掘效率并降低误报。  
- 🛡️ **安全防护与人工奖励并行**：AI 扫描在断网、受限环境中运行，严格控制模型行为；同时继续通过漏洞奖励计划（VRP）激励外部研究者，并调整提交方向以补充内部发现。  
- ⚙️ **自动化漏洞分类**：四阶段流程（过滤噪音、复现漏洞、补充元数据、自动指派）将单个安全报告的分类时间从 5–30 分钟大幅缩短，每月为开发者节省数百小时。  
- 🤖 **多代理修复工作流**：修复代理生成候选补丁，评论家代理评估选择，测试编写代理提前验证跨平台兼容性；Chrome 149 和 150 修复了 1072 个安全漏洞，超过此前 23 个里程碑总和。  
- 🚀 **加速发布与补丁**：从主分支直接合并安全修复，过渡到两周一个里程碑、每周安全更新，并试点每周两次安全发布；同时自动化生成发布说明和 CVE 描述，缩短披露延迟。  
- 🔄 **消除重启负担**：投资“动态补丁”技术，可在浏览器运行中更新子进程；在 Chrome 150 中，macOS 窗口全关时检测到待更新会自动重启，避免用户手动干预。  
- 🧠 **内存安全双轨战略**：短期强化 C++ 运行时（MiraclePtr、MiracleObject、spanification、结构加固），长期迁移至 Rust 等内存安全语言，并建立 Rust SDK 以降低迁移摩擦。  
- 🛡️ **提交前防御**：在 CI/CQ 管道中部署 AI 模型扫描代码差异，提示 spanification 修复、标记悬空指针、强制数值安全，并通过语义分析拦截“隐性安全风险”。  
- 🌐 **生态安全协作**：Google 向 Alpha-Omega 项目捐款 1250 万美元，参与 Akrites 项目；Chrome 依赖超 2300 个第三方组件，正推动自动化更新管道，并结合 GOSSIP 等安全信号降低供应链风险。  
- 🎯 **结论与愿景**：AI 时代漏洞增多并非失败，每修复一个漏洞就减少一个攻击面；通过快速发布、动态补丁、智能重启和结构性防御，Chrome 将持续保护用户，让网络变得更安全。

---

### [](https://www.euronews.com/my-europe/2026/08/02/ai-generated-label-becomes-mandatory-in-the-eu-for-companies)

**原文标题**: [AI-generated label becomes mandatory in the EU for companies | Euronews](https://www.euronews.com/my-europe/2026/08/02/ai-generated-label-becomes-mandatory-in-the-eu-for-companies)

概述：欧盟自本周日起实施 AI 透明度新规，要求企业为 AI 生成的专业内容明确标注，以帮助公众辨别真伪，违规将面临高额罚款。该法规分阶段生效，现有系统需在 2026 年底前适应，并豁免纯个人使用及艺术创作等情形。

- 🤖 欧盟新规要求企业从周日开始为 AI 生成的专业内容添加清晰标签，包括聊天机器人提示、图像或文本的 AI 标识。
- 🏷️ 企业可通过嵌入水印或其他标记来实现标注，不遵守规定将面临巨额罚款。
- 🎭 法规特别关注深度伪造，要求告知用户是否接触情绪识别、生物识别分类、深度伪造及无人工审核的公共利益文本。
- 🛡️ 欧盟官员表示，生成式 AI 使虚假信息规模空前，新规旨在维护公民对所见所闻的信任。
- 📋 规则仅影响专业用途的 AI 内容，纯个人使用不受影响；涉及公共利益的 AI 生成文本若无人工编辑监督也需标注。
- ⏳ 现有 AI 系统需在 2026 年 12 月 2 日前适应新规，艺术、创意、讽刺及虚构类作品可获豁免。
- ⚖️ 欧盟因增加企业负担而受到批评，但有专家认为合规要求虽难实施，最终仍会得到解决。
- 🌐 大型科技公司已提前行动：TikTok 要求创作者标注 AI 内容，Meta 在社交平台使用“AI 信息”标签，Google 签署欧盟 AI 行为准则并开发数字标记工具。
- ⚠️ Google 高管提醒，过多的重叠标签和法律披露可能反而让用户困惑，增加监管复杂性可能适得其反。

---

### [](https://pudding.cool/2026/06/mow/)

**原文标题**: [Why some people mow a lawn better than others](https://pudding.cool/2026/06/mow/)

人们解决割草路径规划问题的方式接近最优解，其策略与计算机科学的经典问题密切相关。

- 🧠 人类在割草路径规划上表现出色，52% 的参与者接近最优解，16% 完全完美。
- 🗺️ 该问题形式化为覆盖路径规划，与旅行商问题类似，但草坪的结构性让人类更容易应对。
- ⚖️ 随着问题规模增大，精确算法变得不可行，人类和计算机都依赖启发式策略来寻找“足够好”的路径。
- 🔄 关键决策在于预判死胡同：最优玩家会先处理开放区域，最后进入死胡同区域，避免回溯。
- 🧩 优秀玩家采用“分解”策略，将大草坪分成小部分逐一解决，并“压缩”经验形成心理模型。
- ⏱️ 思考时间长短与表现好坏无关，关键在于思考时机：最佳玩家在岔路或陷阱前深思，其余时间流畅前进。
- 📊 在最大草坪上，表现略有提升，表明布局比规模更能影响人类的路径规划效率。
- 📉 移动速度相近时，最优玩家回溯更少，他们将注意力集中在关键决策点上，而非均匀分配。

---

### [](https://master.dev/blog/something-nobody-told-you-about-the-image-element-it-can-overflow/)

**原文标题**: [Something Nobody Told You About The Image Element (It Can Overflow!) – Master.dev Blog](https://master.dev/blog/something-nobody-told-you-about-the-image-element-it-can-overflow/)

概述：这篇文章揭示了 `<img>` 元素隐藏的溢出机制。作者指出图片元素既是“容器”又是“内容”，在 `object-fit: cover`、`border-radius`、`object-position` 等属性下，图片内容可以溢出自身。文章还详细解释了 `object-fit: none` 和 `fill` 的区别，并展示了一些基于这些特性的创意 CSS 效果。

- 🔍 图片元素默认有 `overflow: clip`，但你可以改为 `visible` 让内容溢出显示。
- 🖼️ `<img>` 元素与图片资源是“容器与内容”的关系，因此内容可能溢出容器。
- ✂️ `object-fit: cover` 为了保持比例会裁剪图片，导致部分内容超出元素边界。
- 🟣 `border-radius` 也会让矩形图片内容溢出圆角区域。
- ↔️ `object-position` 可以平移图片内容而不移动元素本身，从而产生溢出。
- 🧩 `object-fit: none` 保持图片固有尺寸不缩放，元素尺寸变化时可能造成溢出。
- 🔄 `object-fit` 默认值是 `fill`，与 `none` 相反，内容总是填满元素盒子。
- 🎨 利用这些溢出特性，可以实现悬停、3D、加载动画等无需额外元素的纯 CSS 特效。
- 🛠️ 这些技巧在无法修改 HTML 结构时尤其有用，可替代伪元素方案。
- 🧠 理解图片是“替换元素”有助于掌握其内容与 CSS 格式化模型的关系。

---

### [CSS lh 单位](https://ishadeed.com/article/lh-unit/)

**原文标题**: [The CSS lh unit](https://ishadeed.com/article/lh-unit/)

这份内容提出了高质量内容分享应遵循的标准，强调清晰、示例与学习价值。

- 🎯 观点表达应简明扼要，避免冗长赘述。
- 📊 每条内容需包含至少一个图示或具体例子，辅助理解。
- 💡 内容应让你学到新知识，或至少唤醒已有认知。
- 🏆 保证内容推荐质量上乘，值得信赖。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

overview summary
这是 Tiger Data（Timescale 公司）提供的 Postgres 时间序列云服务，专为大规模 IoT 和时序数据设计，强调弹性扩展、企业级合规与高可用，并提供免费试用额度。

- 📈 单服务可处理每天 3 万亿指标、3 PB 数据、1 千万亿数据点，适用超大规模场景
- 🎁 新用户获 $1000 信用额度，30 天内有效，无需信用卡
- 🏢 被数千家 IoT 企业信任
- ⚖️ 读写分离支持最多 10 个副本节点，结合 SSD/S3 分层存储实现无上限且低成本扩展
- 💰 计算与存储分离，可独立扩展，避免闲置容量支出，降低总成本
- 🔒 高可用：多可用区集群、自动故障转移、时间点恢复与跨区域备份
- 🛡️ 企业级：SOC 2、HIPAA、GDPR 合规，支持始终加密、SSO、RBAC 和审计日志
- 🔍 深度可观测性：查询下钻与仪表板，可向 CloudWatch、Datadog、Prometheus 发送指标
- 🚀 数分钟即可完成数据库部署，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 可与主流云厂商及 Postgres 生态系统无缝集成
- 🤝 企业版提供合同化 SLA、区域数据隔离、合规认证，以及 7×24 小时专家支持与保证响应时间

---

### [](https://evilmartians.com/chronicles/5-best-practices-for-preventing-chaos-in-tailwind-css)

**原文标题**: [5 best practices for preventing chaos in Tailwind CSS—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/5-best-practices-for-preventing-chaos-in-tailwind-css)

overview summary
本文總結了使用 Tailwind CSS 時避免程式碼混亂的五大最佳實踐，並強調前提是具備設計系統與元件化開發方式，才能長期維持可維護性。

- 🧩 前提一：需先建立設計系統與設計令牌（design tokens），避免在程式碼中重複出現魔法數值（如 oklch 顏色），統一在 @theme 或 tailwind.config.js 定義。
- 🧱 前提二：需採用元件化開發，將重複的 class 列表封裝成元件，避免 HTML 結構冗長難維護；同時避免使用 @apply，以免失去 Tailwind 的優勢並增加 CSS 體積。
- ✂️ 最佳實踐一：盡量減少 utility class 的數量，例如用 py-4 取代 pt-4 pb-4，用 flex justify-between 取代 flex flex-row justify-between，並善用 border-black/50 等簡寫。
- 🗂️ 最佳實踐二：將設計令牌分組並以語意化方式命名（如 primary、secondary、error），讓設定檔結構清晰，方便團隊擴充與維護。
- 📏 最佳實踐三：維持 class 排序一致，可透過官方 Prettier 外掛自動排序，提升可讀性並減少認知負擔。
- 🎨 最佳實踐四：避免透過 props 任意傳入 utility class 造成樣式不一致，應預先定義元件 variants（如 primary、secondary、danger），並搭配 clsx 或 tailwind-merge 管理樣式。
- ⚡ 最佳實踐五：縮減最終 CSS 大小；Tailwind v4 自動壓縮，v3 則需透過 CLI --minify 或 cssnano 手動設定。
- ✅ 總結：遵循以上規則並搭配設計系統與元件化架構，就能長期愉快使用 Tailwind CSS，保持專案整潔且易於維護。

---

### [](https://seg6.space/posts/center-div/)

**原文标题**: [we finally learned to center a div, then browsers added sidebars — seg6](https://seg6.space/posts/center-div/)

这篇文章讨论了在浏览器中实现真正居中的问题。虽然现代 CSS 让 div 居中变得容易，但默认是在网页视图（webview）内居中，忽略了侧边栏等浏览器界面。作者通过 JavaScript 测量窗口差异，并利用指针事件精确定位，开发了"center, actually"扩展，让用户自定义居中元素。

- 📐 现代 CSS（如 Grid）虽然能轻松居中 div，但无法考虑浏览器侧边栏，导致居中位置偏离窗口中心。
- 🧮 通过`outerWidth`与`innerWidth`之差可以估算浏览器 UI 宽度，但 DevTools 等左右两侧 UI 使得计算不准确。
- 🖱️ 利用指针事件的`screenX`和`clientX`可以精确计算 webview 在窗口中的位置，从而应用正确的位移。
- 🔧 作者创建了浏览器扩展"center, actually"，可自动检测居中元素或手动选择，以可选的方式实现真居中。
- 🌐 提供了演示和讨论，让用户直观看到效果并反馈。

---

### [](https://textslashplain.com/2026/08/04/security-is-hard-yall/)

**原文标题**: [Web Security is Too Hard – text/plain](https://textslashplain.com/2026/08/04/security-is-hard-yall/)

作者在 Cloudflare 遇到一个看似钓鱼攻击的合法产品，引发对 Web 安全困境的反思，并提出了对开发者、用户和安全工作者的具体建议。

- 🕵️ 作者看到 Cloudflare 新产品的推文，发现心仪用户名可用，急于注册。
- ⚠️ 授权页面出现在 cloudflare.pay 而非 cloudflare.com，且界面与常见“同意钓鱼”攻击高度相似。
- 🤔 页面缺少“举报可疑请求”链接，评论区也找不到相关功能，进一步加剧怀疑。
- 🔍 经查询 AI 助手和文档后确认，这确实是合法产品，绿色对勾是安全 UI 元素，而非攻击者伪装。
- 🌐 合法网站行为“比钓鱼还像钓鱼”，凸显了 SmartScreen 等网址信誉服务在误报与漏报之间的艰难平衡。
- 🛠️ 给开发者的建议：将应用托管在受信任域名下、从受信任页面提供链接、将安全信息放在合适位置、提供上下文内举报入口、并测试举报流程。
- 👤 给用户的建议：点击前先思考，情况不明时不妨等待。
- 💬 给安全极客的建议：切勿责备受害者，他们面对的是不可能轻松完成的任务。

---

### [](https://www.vincentschmalbach.com/time-serves-ai-bots-a-different-website/)

**原文标题**: [TIME Is Serving AI Bots a Different Website, With Ads Built In - Vincent Schmalbach](https://www.vincentschmalbach.com/time-serves-ai-bots-a-different-website/)

TIME 正在为 AI 爬虫提供与人类访问者完全不同的网站版本：一个仅含 13KB 纯 Markdown 的页面，并内嵌了广告，而人类访问的是 303KB 的完整 HTML。通过 User-Agent 区分流量后，TIME 将部分 AI 机器人导向这层隐藏的“机器专属网站”，每次访问都被记录为一次广告曝光，并以 token 为单位计费。

- 🤖 TIME 根据 User-Agent 区别响应：ClaudeBot、PerplexityBot、OAI-SearchBot 收到 13KB 的 text/markdown 版本，而 Chrome、Safari、Googlebot 收到 303KB 的 text/html 完整页面。
- 🚫 不同机器人待遇不同：GPTBot 和 ChatGPT-User 被 406 拒绝，而 OAI-SearchBot（ChatGPT 搜索所用）被放行，说明这是精细的逐 bot 策略。
- 📄 Markdown 版本剥离了布局和脚本，仅剩纯文本，且不包含人类页面中的任何设计元素。
- 💰 该 Markdown 版本内置赞助广告：例如“Best Inventions of 2025”页面中出现了完整的 Ally Bank FAQ，以及 Project Management Institute 的赞助内容；人类访问的 HTML 中完全找不到这些广告。
- 🔢 每个机器人请求都会生成唯一的 `x-mobian-impression` UUID，并配合 `cache-control: no-store`，意味着每次 AI 读取都被计为一次独立广告展示；`x-mobian-tokens` 显示计数单位是 token 而非页面浏览。
- 🏷️ 广告在 Markdown 内虽标注为“Sponsored”或有合作伙伴标签，但人类读者毫不知情，这种受众分裂是隐蔽的。
- 📈 作者认为随着 AI 流量在许多网站超过人类流量，这预示了未来网络将优先为 AI 模型设计，广告也将直接嵌入模型消费的内容流。

---

### [](https://polypane.app/blog/cheatsheets-for-flex-grid-anchor-positioning-and-invoker-commands/)

**原文标题**: [Cheatsheets for flex, grid, anchor positioning and invoker commands | Polypane](https://polypane.app/blog/cheatsheets-for-flex-grid-anchor-positioning-and-invoker-commands/)

Polypane 為 CSS Day 製作了一套關於 Flexbox、Grid、Anchor 定位與 Invoker 命令的實用速查表，並免費提供下載，同時也計畫推出印刷版本。

- 🎨 為 CSS Day 攤位特別設計的速查表，共有四款：Flexbox、Grid、Anchor 定位與 Invoker 命令。  
- 📥 所有速查表皆可從 polypane.app/cheatsheets 免費下載，提供 PDF 與 PNG 格式，並已設定為可直接印刷的 A5 尺寸（含 3mm 出血）。  
- 🖼️ 線上版本模擬了實體卡片的霧面質感與圓角設計，讓使用者瀏覽時能感受印刷成品的效果。  
- 📚 這些速查表並非 Polypane 專屬，而是通用參考工具，適合放在桌上快速查詢 CSS 語法。  
- 📬 未來計畫推出實體 A5 卡片組，可透過訂閱電子報獲得通知，或在研討會現場免費領取。  
- 💬 官方歡迎使用者提供其他主題的速查表建議或對現有版本的意見回饋。

---

### [按钮和链接之间的区别](https://unplannedobsolescence.com/blog/buttons-vs-links/)

**原文标题**: [
The Difference Between a Button and a Link
](https://unplannedobsolescence.com/blog/buttons-vs-links/)

无法总结：未找到主要内容。

---

### [](https://blog.exe.dev/devtools-must-be-open-source)

**原文标题**: [Devtools must be open source - exe.dev blog](https://blog.exe.dev/devtools-must-be-open-source)

本文提出，AI 智能体让软件个性化变得极其简单，用户只需拿到源代码，就能让智能体下载、修改、并与上游持续同步；因此开发工具必须开源，闭源软件因无法被深度个性化，将难以适应用户需求。

- 🔄 五年前，工程师几乎不为自己写软件，因为投入产出比太低；如今智能体彻底改变了这一成本结构。
- 📝 核心方法只需两种提示：一是“下载源码并本地构建、记录修改动机”，二是“设定 cron 每晚拉取上游更新并 rebase 本地改动”。
- 🧩 这些提示可以打包成智能体的“技能”，用户甚至不需要编程，直接说“把界面改成高对比度”即可完成个性化。
- 🥩 作者用一个语句就把 meat.dev 工具集成进 Shelley，让它在后台自动预处理 diff；而用 VS Code 扩展 API 或 vimdiff 实现同样功能几乎不可能。
- 💡 智能体驱动的个性化意味着：源码本身就是扩展系统，以往复杂的插件机制、配置文件都变得不再必要。
- 🏢 个人和小团队不用再购买笨重且需要迁就的可配置软件，可以直接组装专属工具；这篇博客本身就是定制软件。
- 🔓 因此，开源是个人化软件的基石：开源智能体 Pi、Codex 都能被轻松改造，而闭源 Claude Code 只能依赖固定钩子。
- ⚠️ 如果闭源工具的自定义能力不够用，作者建议直接换用可个性化的开源智能体。

---

### [](https://github.com/jespervos/blossom-carousel)

**原文标题**: [GitHub - jespervos/blossom-carousel: Native-first carousel enhanced with drag support for pointer devices. · GitHub](https://github.com/jespervos/blossom-carousel)

Blossom Carousel 是一个基于原生浏览器滚动构建的轮播库，它不替代原生滚动，而是通过轻量拖拽增强指针设备交互，同时保留真实滚动容器的性能、可访问性和兼容性。

- 🥇 原生滚动：保留完整的滚动性能与可访问性，作为核心交互模型。
- 🚀 指针拖拽：为鼠标、触控笔等所有指针类型提供基于物理的自定义拖拽体验。
- ➡️ 导航控件：内置上一页、下一页和圆点导航，支持自定义圆点渲染。
- ✨ 无抽象：与所有原生 Web API 原生协作，如 scroll-snap、position sticky 和滚动驱动动画。
- 💡 按需加载：在触屏设备上体积为 0kb，仅检测到精细指针时加载脚本。
- 🧱 框架支持：提供 React、Vue、Svelte、Web Components 及核心包。
- 🚧 实验性循环滚动：支持无限循环轮播功能。
- 🤖 Agent Skills：为 AI 编码助手提供包特定指导和自动安装技能。
- 📦 迁移指南：覆盖 Embla、Swiper、Splide、Slick、Flickity 等常见库的迁移说明。
- 📖 示例与许可：提供按复杂度分类的示例，采用 Apache-2.0 许可证。

---

### [花开旋转木马](https://www.blossom-carousel.com/)

**原文标题**: [Blossom Carousel](https://www.blossom-carousel.com/)

Blossom Carousel 是一款为现代网页设计的轮播组件，其核心理念是增强而非取代浏览器原生的滚动机制。它通过物理拖拽、CSS 配置以及与框架的无缝集成，让开发者能够快速构建高性能、可定制的轮播体验，并且组件本身极其轻量。

- 🌟 **增强原生滚动**：Blossom 的核心是增强浏览器原生滚动行为，而非重写，确保滚动体验流畅自然。
- 💧 **物理拖拽感**：实现了类似原生的鼠标物理拖拽效果，并能在拖拽与滚动之间无缝衔接。
- 🚀 **现代 Web 构建**：完全为现代浏览器技术设计，支持 CSS scroll-snap、position sticky 及滚动驱动动画等特性。
- 📦 **简易安装与使用**：可通过 `npx skills add` 命令快速添加，并提供了清晰的、无抽象层级的 React 组件 API（如 `BlossomCarousel`、`BlossomPrev`）。
- 🎨 **CSS 配置驱动**：开发者可直接利用标准 CSS 属性（如 `scroll-snap-type` 和 `scroll-snap-align`）来定义轮播行为与样式。
- 🏆 **生产级验证**：已被多个高质量项目采用，月下载量超过 3.13 万次，且拥有 wearecollins.com 等知名案例。
- 🧩 **框架封装支持**：提供框架专用的封装组件，让开发者无需额外配置即可快速上手集成。
- 🎛️ **完全控制权**：不覆盖或限制任何默认行为，允许开发者对每个细节进行无摩擦的自定义。
- 0️⃣ **极致轻量设计**：组件引擎按需加载，在触屏设备上初始体积为 0kb，实现性能最优化。

---

### [TanStack 图表](https://tanstack.com/charts/latest)

**原文标题**: [TanStack Charts](https://tanstack.com/charts/latest)

TanStack Charts 是一个基于图形语法的声明式图表库，最新 0.6.5 已发布，以极小的包体积提供丰富的图表类型、交互和主题定制能力，并具备严格的 TypeScript 类型安全保障。

- 📦 TanStack Charts 0.6.5 已发布到 npm，框架无关核心仅 8.12 KiB gzip，紧凑 React 行图仅 16.48 KiB。
- 📊 内置大量示例：条形图、极坐标图、交互工具提示、动画、地理地图、分布图、趋势图等，覆盖常见可视化场景。
- 🔒 类型安全且声明式：所有示例在严格 TypeScript 下编译，字段、类型、标度、工具提示和回调均与源数据绑定，无效定义会被拒绝。
- 🎨 可高度定制：支持 CSS 变量、主题、标记属性、自定义工具提示或自定义渲染器，轻松融入产品风格。
- ⚡ 性能与体积优势：冷页 bundle 对比中，TanStack Charts 为 26.6–32.1 KiB，远小于 Chart.js、Observable Plot、Recharts、ECharts 等。
- 🧩 基于 Leland Wilkinson 的图形语法，API 受 Observable Plot 启发，但运行时为独立实现，不依赖 D3 或 InternMap。
- 🤝 提供合作伙伴和赞助计划，赞助者可获得专属 Discord 频道、优先问题处理和直接支持。

---

### [](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/crm-triggered-document-pipeline/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260805)

**原文标题**: [Build a CRM-Triggered Document Pipeline with Foxit](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/crm-triggered-document-pipeline/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260805)

概述摘要
该指南介绍如何利用 Power Automate 与 Foxit REST API，实现从 CRM 成交到合同生成、电子签名及自动归档的完整自动化流程，全程仅使用 HTTP 操作和 Webhook。

- 📄 触发转换：CRM 中交易状态变为“已成交”时，自动触发 Power Automate 工作流，将 Word 合同转换为 PDF。
- 🔗 API 集成：通过 Foxit 的 REST API 执行 PDF 生成，无需额外编码或本地安装，仅用 HTTP 请求即可调用。
- ✍️ 电子签名：转换后的 PDF 自动通过 Foxit eSign API 发送给相关方进行签名，简化签署流程。
- 📡 状态同步：利用 Webhook 实时接收签名完成通知，确保流程在正确时机进入下一步。
- 🗂️ 自动归档：签署完成的合同自动保存至指定位置（如 CRM 记录或云存储），实现文档集中管理。
- ⚙️ 纯低代码：整个工作流构建于 Power Automate 的 HTTP 操作之上，适合快速部署与维护。

---

### [](https://www.csstypestudio.com/)

**原文标题**: [CSS Type Studio: Advanced Typography with CSS](https://www.csstypestudio.com/)

overview summary  
这是一个名为“CSS Type Studio”的网页工具，用于可视化调整和实验 CSS 排版属性。它提供多种文本示例、全局与元素级排版控制、字体变体、间距与列表样式，并支持保存、分享布局，以及免费/付费账户功能。

- 🎨 支持多种显示模式：Light、Dim、Dark、Cool、Warm 颜色模式
- 📏 可设置全局属性，如字体大小单位（rem/px）和最大宽度
- 🔤 针对不同元素（H1–H4、段落、列表、byline、dateline）单独调整排版
- ✒️ 字体设置包含 family、大小、样式、字重（100–950）及变体配置
- 🔠 字型变体：大写形式（small caps、titling caps 等）、连字、数字形式（tabular、oldstyle 等）
- 📐 文本对齐、缩进、字间距、行高、词间距等精细控制
- 💬 文本换行方式：nowrap、balance、pretty、stable 等选项
- 🔡 支持 text transform（大写/小写/首字母大写）及 kerning 设置
- 👁️ 文本渲染模式：优化速度、可读性或几何精度
- 🔍 光学尺寸（optical sizing）与字重、样式、小型大写字母的合成开关
- 📏 可调上下边距、左内边距，以及列表样式（disc、decimal、roman 等）
- 💾 支持保存布局、删除布局，并通过链接分享布局（无需登录也可查看）
- 🔑 免费用户可登录保存/分享布局，获取 CSS 代码；Pro 付费订阅解锁更多功能
- 💳 账单管理通过 Stripe 处理，支持升级到 Pro 月度订阅

---

### [](https://www.extend.ai/ui)

**原文标题**: [Open source UI kit for modern document apps - Extend UI](https://www.extend.ai/ui)

这是一个开源 UI 工具包，专为现代文档应用设计，提供多种 React 组件，支持 PDF、DOCX、XLSX、CSV 等文档的查看与处理，并集成了边界框引用、文件上传、电子签名等功能，可快速嵌入用户流程、代理或内部工具。

- 📚 开源 UI 工具包，聚焦现代文档应用场景
- ⚛️ 提供 React 组件，覆盖 PDF、DOCX、XLSX、CSV 等格式查看
- 🔲 支持边界框引用（bounding box citations）
- 📤 内置文件上传功能
- ✍️ 支持电子签名（e-signing）
- 🛠️ 可快速集成到用户界面、代理或内部工具中
- 📄 包含 PDF 查看器组件
- 📑 包含文档拆分（Document Splits）组件
- 📊 包含 XLSX 查看器组件
- 📁 包含文件系统组件
- 🧩 包含 Schema Builder 组件

---

### [](https://github.com/extend-hq/ui)

**原文标题**: [GitHub - extend-hq/ui · GitHub](https://github.com/extend-hq/ui)

Extend UI 是一套开源 React 组件库，专为文档代理、用户文档流程和内部工具设计，包含 14 个组件，支持 PDF/DOCX/XLSX 查看、文件上传/缩略图、电子签名、布局块等功能，可完全自定义并以 MIT 许可证分发，可通过 shadcn 组件注册表安装。

- 📦 提供 14 个组件，包括 PDF/DOCX/XLSX 查看器、文件上传、文件缩略图、电子签名、文档拆分、布局块和 Finder 风格文件浏览器。
- 🔍 内置边界框引用和布局块示例，支持 OCR 布局检查、字段级引用审查和 PDF 覆盖层。
- 🧩 通过 shadcn CLI 轻松安装，如 `npx shadcn@latest add @extend/pdf-viewer`，安装后可直接导入组件使用。
- ✏️ 组件以源码形式复制进项目，可自由修改；共享基础组件（Button/Select 等）会自动复用项目已有的实现。
- 📂 提供三个典型示例：Layout Blocks（OCR 布局）、Bounding Box Citations（人工审查）、File System（文件浏览）。
- ⚙️ 源自 Extend 内部生产环境，已处理数百万页文档，修复和改进持续回流到开源项目。
- 🌐 相关链接：文档 https://www.extend.ai/ui，GitHub https://github.com/extend-hq/ui，registry 命名空间 @extend/*。
- 🛠️ 本地开发：`pnpm install` 后运行 `pnpm v4:dev`，站点地址为 http://localhost:4000。
- 📄 采用 MIT 许可证，由 Extend 团队创建和维护，适合构建现代文档处理产品。

---

### [](https://github.com/tejaswigowda/ffmpeg-webCLI)

**原文标题**: [GitHub - tejaswigowda/ffmpeg-webCLI: A browser-based video editor powered by ffmpeg.wasm. No uploads, no servers -- all processing happens locally in your browser using WebAssembly. · GitHub](https://github.com/tejaswigowda/ffmpeg-webCLI)

ffmpeg-webCLI 是一个基于浏览器的视频编辑器，利用 ffmpeg.wasm 在本地设备上完成所有视频处理，无需上传文件到服务器。它提供 30 多种视频操作、批处理与操作链组合、离线 PWA 支持，并强调隐私与零上传。适用于处理敏感视频、无法安装软件或希望完全离线工作的场景，也可通过本地服务器自行部署。

- 🖥️ 纯浏览器视频编辑器：基于 ffmpeg.wasm，所有处理通过 WebAssembly 在本地完成，零上传、零服务器。
- 🔒 隐私优先：视频文件不离开设备，避免云工具（如 CloudConvert、Kapwing）带来的数据泄露和隐私政策风险。
- ⚡ 30+ 视频操作：包括 GIF 制作、格式转换、压缩、裁剪、变速、旋转/翻转、淡入淡出、音量调节、去除元数据、缩略图提取等。
- 🎬 多种格式支持：MP4、WebM、MKV、MOV、AVI、GIF、MP3、AAC、WAV、OGG、FLAC、JPG、PNG。
- 🧩 高级功能：原始 FFmpeg 命令行、软/硬字幕嵌入、Whisper 自动字幕、拼接、画中画、并排视频、混音、媒体信息深度扫描。
- ⛓️ 操作链（Stack Mode）：将多个兼容操作合并为单次编码的 filter chain，避免重复编码画质损失，并可与批处理结合。
- 📚 批处理：一次处理多个文件，支持实时进度、独立下载、ZIP 全部；25 种操作可用，多输入或内存密集型操作会禁用。
- 📴 离线 PWA：首次加载后完全离线可用，可安装为桌面/移动应用，静态资源和 ffmpeg 核心均缓存于本地。
- 💡 屏幕唤醒锁：处理视频期间自动保持屏幕常亮，防止设备休眠中断任务。
- 🖱️ 实时预览与尺寸估算：调整参数时即时显示输出效果和文件大小预估，改善操作体验。
- 🧠 自动字幕（Whisper）：浏览器内完成语音转录，支持 Tiny/Base/Small 模型，生成 SRT 后可编辑并嵌入或硬烧录。
- 🔧 本地运行方式：使用 `node server.js` 启动，或通过任何设置 COOP/COEP 头的静态服务器部署，以满足 SharedArrayBuffer 要求。
- 📄 开源许可：GPL-3.0 授权；底层依赖 ffmpeg.wasm（LGPL-2.1）及 FFmpeg。

---

### [](https://tejaswigowda.com/ffmpeg-webCLI/)

**原文标题**: [ffmpeg webCLI](https://tejaswigowda.com/ffmpeg-webCLI/)

这是一个名为 ffmpeg webCLI 的纯前端视频处理工具，强调离线优先，100% 在浏览器本地运行，数据不会离开用户设备。用户需先加载 FFmpeg 核心（约 31MB），随后可拖拽或选择视频文件，进行裁剪、批处理，并应用丰富的音视频操作，且操作可堆叠为链式流程，最终以多种格式输出并下载。

- 🔒 完全离线运行，所有处理都在浏览器本地完成，无需上传数据至服务器。
- 📥 需先点击加载约 31MB 的 FFmpeg 核心，才能开始处理视频。
- 🎞️ 支持拖拽或点击选择本地视频，兼容 MP4、WebM、MOV、AVI、MKV、GIF 等格式。
- 📚 支持批量队列处理，可同时管理多个文件，并一键导出全部结果（ZIP）。
- ✂️ 提供视频修剪功能，可拖动起点与终点，并可应用于所有操作或单独启用。
- 🔄 操作可单个执行或堆叠成链，按顺序作为一条滤镜链进行统一编码处理。
- 🎥 支持格式转换：MP4、MKV、MOV、WebM、GIF、AVI，并可调整分辨率、CRF 质量与编码预设。
- 🎵 可提取音频为 MP3、AAC、WAV、OGG、FLAC；也可移除音轨或调节音量（可静音）。
- 🖼️ 支持生成 GIF、提取缩略图，并可设置帧率、宽度与时间戳。
- ⏩ 支持视频速度调整（0.25× 至 4×）、旋转/翻转、裁剪、反转播放（倒放）。
- 🌗 提供淡入淡出、亮度/对比度/饱和度调节、灰度化、锐化/模糊及降噪等滤镜。
- 🧹 可去除元数据（GPS、相机信息、创建日期等），并重新编码视频与音频。
- 📝 支持嵌入字幕（软字幕或硬烧录），也可用 Whisper 在本地自动生成并嵌入字幕，全程数据不出浏览器。
- 🧩 可叠加 Logo 或图片水印，支持位置与宽度百分比控制。
- 🎚️ 支持混音（背景音乐）、拼接片段、并排合成、画中画等高级合成功能。
- 📐 提供填充至目标宽高比（16:9、9:16、1:1 等）与颜色填充选项。
- 🔊 可进行音频归一化（EBU R128，适应不同平台响度标准）及循环播放设置。
- 🎛️ 提供原始 FFmpeg 命令模式，可自定义参数并预览完整命令，适合高级用户。
- 📊 可查看媒体信息、当前命令预览、处理进度条及 FFmpeg 日志，完成后直接下载输出文件。

---

### [](https://markodenic.com/tools/neumorphism-css-generator/)

**原文标题**: [Neumorphism CSS Generator - Marko Denic - Web Developer](https://markodenic.com/tools/neumorphism-css-generator/)

概述：这是一个关于 Neumorphism（软 UI）CSS 生成器的介绍与使用指南，涵盖其设计理念、CSS 实现原理、可访问性注意事项、浏览器支持、与玻璃拟态的区别，以及常见问题解答。

- 🎨 Neumorphism 是一种“新拟物”风格，通过元素与背景同色并使用明暗双阴影，营造出凸起或凹陷的柔和质感。
- 🛠️ 使用生成器时，需选择背景色、尺寸、圆角，并调整距离、强度、模糊度，可选平面、凹、凸、按压等形状，最后复制生成的 CSS。
- 💻 CSS 核心是单条 `box-shadow` 规则：暗色阴影在右下，亮色阴影在左上（光源默认左上），如 `box-shadow: 12px 12px 24px #bebebe, -12px -12px 24px #ffffff`。
- 📥 若要让元素呈现“按压”效果，只需在两条阴影后都加上 `inset` 关键字，例如 `inset 12px 12px 24px #bebebe, inset -12px -12px 24px #ffffff`。
- ⚠️ 可访问性风险：元素与背景色一致、对比度低，可能导致边缘不可见、点击暗示弱，且难以满足 WCAG 对比度要求；建议保持文字高对比、为关键控件补充清晰的悬停/聚焦/激活状态，并将该风格作为点缀而非唯一交互信号。
- 🌐 浏览器支持极佳：纯依赖 `box-shadow`，现代 Chrome、Firefox、Safari、Edge 均无需前缀即可使用。
- 🆚 与玻璃拟态的区别：Neumorphism 使用同色系双阴影呈现“软实体”感；Glassmorphism 则使用背景模糊和透明度营造“磨砂玻璃”效果，若需要后者可改用玻璃拟态生成器。
- ❓ 常见问答要点：双阴影模拟单一光源；暗色模式同样适用（深灰背景 + 更暗阴影 + 微亮高光）；按钮可做但必须加强交互反馈；该风格在 2026 年仍常用于概念设计、仪表盘和极简界面。

---

### [](https://twilson.net/scroll-mask)

**原文标题**: [Scroll Mask Tailwind CSS Utilities — Tim Wilson](https://twilson.net/scroll-mask)

这是一个用于 Tailwind CSS 的实用工具集合，可基于滚动位置让滚动容器的边缘产生淡出（遮罩）效果，且无需任何 JavaScript。

- 🎭 核心机制：利用 CSS `animation-timeline: scroll()` 和 `mask-image` 实现滚动渐隐，完全无 JS 依赖。
- 📦 安装方式：将提供的 CSS 代码直接添加到 Tailwind CSS v4 的样式表中即可使用。
- 🔄 轴向工具：`scroll-mask-y` 控制垂直滚动，`scroll-mask-x` 控制水平滚动，分别淡出对应轴的两端。
- 🧭 方向工具：支持 `scroll-mask-t`、`scroll-mask-b`、`scroll-mask-l`、`scroll-mask-r`，分别淡出上、下、左、右单个边缘。
- 🎛️ 自定义淡出范围：通过 `-from-*` 后缀（如 `from-80%`）设定不透明停止位置，从而控制渐变区域的大小。
- 🧩 兼容性：需要浏览器支持 `animation-timeline: scroll()`，否则相关效果不会生效。

---

### [STRICH | 适用于 Web 应用的条形码扫描](https://strich.io/?ref=frontend-focus)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=frontend-focus)

STRICH 是一个专为网页应用设计的 JavaScript 条码扫描 SDK，支持 1D/2D 条码实时识别。它完全在浏览器端处理图像，无需后端服务，并强调性能、易集成和透明定价。网页应用相比原生应用具备无需应用商店审核、分发简单、开发成本低等优势。STRICH 提供现代 Web 技术（WebAssembly/WebGL）构建的扫描 UI、Pop up 扫描器、对破损/光照不佳条码的强识别能力，以及企业级功能（离线操作、定制品牌等）。定价采用订阅制，提供免费试用和不同层级方案，并获得大量真实客户的好评。

- 📦 STRICH 是用于 Web 应用的条码扫描 SDK，支持 1D/2D 条码，完全在浏览器端处理，无需后端。
- 🚀 支持主流一维码（Code 128、EAN、UPC、Code 39 等）和二维码（QR、Data Matrix、Aztec、PDF417），并持续增加新类型。
- 🌐 选择 Web 应用条码扫描的优势：无应用商店限制、通过链接/二维码轻松分发、降低开发成本、避免“应用疲劳”、PWA 可增强用户粘性。
- ⚙️ 基于现代 Web 技术（WebAssembly、WebGL）构建，兼容主流浏览器和 Android/iOS 设备，零依赖，支持所有主流框架。
- 📷 内置成熟扫描 UI（含瞄准线、相机切换、手电筒、点击对焦），并提供 Popup Scanner，可一行代码快速集成。
- 🧠 强大的图像处理能力：可读取褪色、破损、光照不均、反光甚至反向（浅色条码深色背景）的条码，优于 ZXing-JS 和 Quagga。
- 💼 企业级功能：持续维护与技术支持、按年固定收费（与扫描量/设备数无关）、可选定制品牌（去除 STRICH logo）、离线运行（零网络流量）以及 GS1 Solution Partner 认证。
- 💰 定价方案：Basic 版每月 €99（10k 次扫描/月）、Professional 版每月 €249（100k 次扫描/月）、Business 版每年 €4,000 起（无限制扫描和设备，可定制品牌），另提供企业定制报价。
- 👍 大量客户证言：用户认可 STRICH 在户外光照、破损标签等恶劣条件下的可靠识别、快速集成、优秀文档和支持服务，并称赞其性价比优于其他 SDK。
- 🔧 FAQ 要点：若连续两个月超过扫描限额不会拒绝服务，只会提示升级；订阅模式始终享有最新版本；可先通过免费 Demo 验证兼容性和识别率。
- 🆓 提供 14 天免费试用，一般一天内即可完成集成，且可从 NPM 或 CDN 安装，附 TypeScript 类型定义。

---

### [面向开发者的电视 — CodeTV](https://codetv.dev/)

**原文标题**: [tv for developers — CodeTV](https://codetv.dev/)

CodeTV 是一個由開發者製作、為開發者而設的原創影音平台，提供多個競賽、實境秀與訪談系列，涵蓋產品開發、網頁挑戰、AI 建置與企業成長故事，並設有社群支持與電子報訂閱。

- 🎬 近期節目包含《The Full Stack》第七集原型週（Pitch 轉為可展示產品）及第六集提案週（8 隊取 7 隊晉級）。
- 🖥️《Web Dev Challenge》最新一集要求打造令人驚豔的著陸頁，還有「用 atproto 重建網站」挑戰。
- 🏗️《The Greenfield Games》團隊在 6 小時內建置知識管理系統（Notion 主題）與 CRM 系統（Salesforce 主題）。
- 🎙️《The Build Log》訪談 Tanner Linsley（TanStack 開源社群轉永續經營）與 Clerk CEO Colin Sidoti（不以退出為目標）。
- 📺 原創系列包含《The Full Stack》（Kelsey Hightower 主持）、Web Dev Challenge（4 季）、The Greenfield Games（AI 建置 vs 購買）、The Build Log、Web Lunch、Learn With Jason、The Web Dev Podcast、Leet Heat 與 #DoItAnyways。
- 🤝 CodeTV 與知名開發工具品牌合作，提供個人或企業支持者方案，以創造更多原創節目並建立開發者社群。
- ✉️ 網站提供電子報訂閱，內容包含獨家資訊與產業新聞，承諾不寄垃圾郵件、不分享個資，一鍵即可退訂。

---

### [](https://www.youtube.com/watch?v=rCJ9OdNdigQ)

**原文标题**: [Tanner Linsley Built TanStack to Outlive Him · The Build Log S1.E2 - YouTube](https://www.youtube.com/watch?v=rCJ9OdNdigQ)

此為 YouTube 頁面底部的連結分類，涵蓋媒體、法律、合作與政策等資訊。
- 📋 簡介與媒體：提供關於 YouTube 的基本介紹及媒體相關資訊。
- ⚖️ 著作權與法律條款：說明著作權規範、服務條款及法律事項。
- 📞 與我們聯絡：提供使用者聯繫 YouTube 的管道。
- 🎨 創作者與廣告：針對內容創作者與廣告主的相關服務與資訊。
- 👨‍💻 開發人員與技術：提供開發人員所需的工具與資源。
- 🔒 隱私權與政策安全性：涵蓋隱私保護、平台政策與安全規範。
- ⚙️ YouTube 運作方式與測試：說明平台運作機制與新功能測試。
- 📅 © 2026 Google LLC：版權宣告，顯示所有權屬於 Google。

---

### [Web 开发挑战赛第三季](https://codetv.dev/series/web-dev-challenge/s3)

**原文标题**: [Web Dev Challenge Season 3](https://codetv.dev/series/web-dev-challenge/s3)

本內容介紹《Web Dev Challenge》第三季第五集「The Best Landing Page Ever」，以及本季其他集數、周邊花絮與合作夥伴等資訊。

- 📺 第三季共 5 集，第五集主題為打造令人驚豔的落地頁面，於 2026 年 7 月 7 日播出。
- 🗓️ 本季其他集數：3/10「打造讓人忍不住把玩的 App」、3/24「打造幫助人們創作的 App」、4/7「打造拉近人際的 App」、6/4「用 atproto 重建你的網站」。
- 🎬 花絮包含 6/4 釋出的第四集預告，由 Bluesky 贊助。
- ⏱️ 每一集節目中，開發團隊須在 4 小時內打造出獨特 App。
- 🖥️ 本季開發者工作站由 BenQ、UPLIFT Desk、Logitech、CalDigit 等品牌贊助提供。
- 🛠️ 過往季度也曾與 Anglepoise、Keychron、Ugmonk 等品牌合作。
- 🤝 本季由多家公司合作贊助製作完成。

---

### [](https://codetv.dev/series/web-dev-challenge/s3/e5-best-landing-page-gsap/play)

**原文标题**: [The Best Landing Page Ever | Web Dev Challenge | S3.E5](https://codetv.dev/series/web-dev-challenge/s3/e5-best-landing-page-gsap/play)

概述总结
- 📭 未检测到需要总结的文本内容，请提供文章正文，以便我为您生成简洁的要点列表。

---

### [首页 | GSAP](https://gsap.com/)

**原文标题**: [Homepage | GSAP](https://gsap.com/)

GSAP 是一款专为专业人士打造的强大 JavaScript 动画库，能轻松动画 JS 可触及的一切，提供丝滑流畅的性能与丰富工具，覆盖滚动、SVG、文本和 UI 交互等场景，并获得众多知名品牌采用。

- 🚀 专业级 JS 动画库，可轻松动画任何 JS 能操作的内容
- ✨ 提供丝滑流畅的性能与无与伦比的支持，让你专注创作
- 🎯 支持 UI、SVG、WebGL 等多样化动画场景
- 📈 内置大量即插即用的缓动函数，也可自定义曲线
- 🎬 轻松编排、控制复杂的动画序列
- 📜 ScrollTrigger 将滚动转化为流畅的叙事体验
- 🖼️ SVG 插件支持移动、变形等多种效果
- 🔤 文本插件实现无缝且引人注目的文字动画
- 🖱️ UI 交互工具打造精致、易用的交互体验
- 🏢 被众多知名品牌使用，并有年度 Showreel 展示案例

---

### [](https://codetv.dev/series/web-dev-challenge/s3/e4-rebuild-your-website-again/play)

**原文标题**: [Rebuild your website (again) | Web Dev Challenge | S3.E4](https://codetv.dev/series/web-dev-challenge/s3/e4-rebuild-your-website-again/play)

总览摘要：这段内容提供了生成摘要回复时必须遵循的格式与要求，涵盖模板结构、符号使用、信息提炼和语言规定等要点。

- 📋 输出需采用“概述摘要 + 表情符号要点”的固定模板。
- ➖ 每个要点使用“-”符号作为前缀。
- 🔑 须提炼关键信息，准确把握文章核心与本质。
- 😊 需为每条要点挑选合适的表情符号。
- 🏷️ 顶部添加概述摘要，且不带任何标题。
- 🌐 所有内容必须使用中文（ZH）撰写。

---

### [](https://bsky.app/)

**原文标题**: [Bluesky](https://bsky.app/)

overview summary  
该页面提示用户当前为高度交互式 Web 应用，必须启用 JavaScript 才能正常使用，并提供了 Bluesky 与 AT Protocol 的相关链接。

- 🌐 此应用为高度交互式网页，需启用 JavaScript 才能运行。  
- ⚠️ 仅支持简单 HTML 界面，但并非当前应用的形式。  
- 🔗 提供 Bluesky 官网链接：bsky.social。  
- 📄 提供 AT Protocol 技术文档链接：atproto.com。  
- 🏠 当前页面为网站首页。

---

### [](https://www.youtube.com/watch?v=OgqWEz-Rrrw)

**原文标题**: [Devs vs. AI Agents: Rebuild Workday in 6 hours | The Greenfield Games S1.E2 - YouTube](https://www.youtube.com/watch?v=OgqWEz-Rrrw)

这段文本是 YouTube 页脚链接的列表，涵盖平台介绍、媒体资源、法律条款、联系渠道、创作者与开发者支持以及平台运作方式等信息。

- 📄 简介：提供 YouTube 平台的基本介绍
- 🎥 媒体：面向媒体的新闻与资源入口
- ⚖️ 著作權：版权相关说明与申诉渠道
- 📞 與我們聯絡：联系 YouTube 团队的方式
- 👩‍🎨 創作者：为内容创作者提供的支持与服务
- 💰 廣告：广告投放与商业合作信息
- 👨‍💻 開發人員：面向开发者的 API 与工具资源
- 📋 條款：使用平台需遵守的服务条款
- 🔒 隱私權：用户隐私保护政策说明
- 🛡️ 政策與安全性：平台内容政策与安全保障机制
- ⚙️ YouTube 運作方式：解释平台的推荐与审核等运行机制
- 🧪 測試新功能：介绍 YouTube 正在测试的新功能
- ©️ 版权声明：© 2026 Google LLC 版权信息

---

