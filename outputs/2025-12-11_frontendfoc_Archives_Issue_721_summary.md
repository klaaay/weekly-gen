### [Frontend Focus Issue 721: December 10, 2025](https://frontendfoc.us/issues/721)

**原文标题**: [Frontend Focus Issue 721: December 10, 2025](https://frontendfoc.us/issues/721)

总结失败：Expecting value: line 10 column 1 (char 9)

---

### [CSS Wrapped 2025](https://chrome.dev/css-wrapped-2025/)

**原文标题**: [CSS Wrapped 2025](https://chrome.dev/css-wrapped-2025/)

本文概述了近期 CSS 和 HTML 的新特性，重点介绍了可自定义组件、交互命令、下一代交互及优化的人机工程学功能，旨在提升开发者构建现代 Web 界面的效率和体验。

- 🎨 **可自定义组件**：新增了原生锚点定位和轮播滚动 API 等核心模块，支持通过 CSS 完全自定义`<select>`元素，包括下拉列表和选项的样式。
- 🚀 **调用者命令**：通过`commandfor`和`command`属性，无需 JavaScript 即可声明式地控制`<dialog>`和`[popover]`元素的显示、隐藏等操作。
- 💡 **对话框轻量关闭**：为`<dialog>`引入`closedby`属性，支持点击外部或按 ESC 键关闭对话框，提升用户体验。
- 🛠️ **提示弹出层**：新增`popover="hint"`类型，用于创建临时性 UI（如工具提示），且不会关闭其他弹出层，支持在`<a>`标签上使用。
- 🎯 **滚动标记与按钮**：通过`::scroll-marker()`和`::scroll-button()`伪元素，无需 JavaScript 即可创建可访问的轮播导航和标记。
- 🔗 **滚动目标组**：使用`scroll-target-group`属性将锚点链接列表转换为滚动标记，实现页面内导航高亮。
- 📐 **锚点容器查询**：结合`container-type: anchored`和`anchored()`函数，根据锚点位置动态调整样式（如工具提示箭头方向）。
- 🖱️ **兴趣调用者**：通过`interestfor`属性实现悬停或聚焦时触发 UI（如提示框），支持延迟设置，提升可访问性。
- 📜 **滚动状态查询**：使用`container-type: scroll-state`查询元素是否处于滚动、吸附或固定状态，并应用相应样式。
- 🔢 **树计数函数**：引入`sibling-index()`和`sibling-count()`函数，简化基于元素位置的动画和布局计算。
- 🧩 **嵌套视图过渡组**：通过`view-transition-group`属性嵌套过渡组，保留 3D 和裁剪效果，增强视图过渡的视觉效果。
- 🎥 **DOM 状态保留移动**：使用`moveBefore`方法移动元素（如视频或 iframe）时保持其状态（如播放进度），避免重新加载。
- 🧪 **高级 attr() 函数**：扩展`attr()`函数支持多种数据类型（如颜色、长度），并可在任意 CSS 属性中使用。
- 🎛️ **条件样式函数**：新增`if()`函数，基于媒体查询、特性支持或样式条件动态应用样式，简化响应式设计。
- 🛠️ **自定义 CSS 函数**：通过`@function`定义可重用的 CSS 函数，提升代码复用性和可维护性。
- 📏 **扩展范围语法**：在样式查询和`if()`语句中支持范围比较（如`>`、`<`），实现更灵活的样式逻辑。
- 🔲 **拉伸尺寸关键字**：使用`stretch`关键字使元素填充包含块，同时保留外边距，替代传统的百分比设置。
- 🔶 **角形状属性**：新增`corner-shape`属性，支持多种角形状（如斜角、凹槽、圆形），增强界面设计灵活性。

---

### [- YouTube](https://www.youtube.com/watch?v=rnT1XBZWHMk)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=rnT1XBZWHMk)

该内容为 YouTube 平台页脚导航链接，主要涵盖平台信息、用户指南及法律条款。

- ℹ️ 关于平台的基本信息与介绍
- 📰 官方新闻发布与媒体资源
- ©️ 版权政策与内容保护说明
- 📞 用户联系与客服渠道
- 🎬 内容创作者专属资源
- 📢 广告合作与商业推广
- 💻 开发者工具与 API 接口
- 📜 平台使用条款与协议
- 🔒 隐私保护与数据政策
- ⚖️ 平台安全规范与社区准则
- 🔧 产品功能运作机制说明
- 🧪 新功能测试与体验计划
- ⏳ 2025 年谷歌公司版权所有声明

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=referral)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=referral)

SurveyJS 是一个开源 JavaScript 库套件，用于在应用程序中自主构建、管理和分析调查与表单，确保数据完全自主掌控。

- 📚 **表单库** – 免费 MIT 许可的 UI 组件，可解析 JSON 并即时渲染动态交互式表单，支持收集用户响应并发送至自有数据库。
- 🛠️ **调查创建器** – 支持拖放操作的表单构建器，自动生成描述表单结构、样式和行为的 JSON 模式，可完全自定义以匹配应用设计。
- 📊 **仪表板** – 通过 JSON 模式识别数据类型，将调查结果以交互式图表和表格可视化。
- 📄 **PDF 生成器** – 将表单 JSON 模式渲染为 PDF，支持导出为可编辑或预填的 PDF 文件。
- ♿ **无障碍支持** – 完全符合 WCAG、Section 508 和 ARIA 标准，支持键盘导航和屏幕阅读器。
- ∞ **无使用限制** – 可创建无限表单、收集任意数量响应，所有数据存储于自有数据库，无管理员、受访者或功能上限。
- 🧩 **自定义输入字段** – 支持定义自定义问题类型，可扩展内置组件或集成 Angular、React、Vue 3 组件。
- 📶 **离线数据收集** – 支持完全离线工作，本地存储调查、主题和响应，恢复在线后自动同步。
- 💳 **一次性购买许可** – 开发者可一次性购买永久使用 Survey Creator、PDF 生成器和仪表板，包含 12 个月免费维护。
- ✅ **自定义数据验证** – 支持创建自定义客户端规则和服务器端检查，超越基础验证器。
- 🔓 **开源与自主托管** – 所有库开源（支持 React、Angular、Vue 3、Vanilla JS），可自行托管以完全控制数据存储和隐私。
- 🎨 **白标化定制** – 可完全控制表单和 Survey Creator 的外观，支持内置主题或自定义 CSS 变量。
- 🤖 **AI 辅助** – 可通过 API 集成 AI，实现自然语言表单生成、翻译和智能内容建议。
- 🏢 **多行业适用** – 适用于保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利组织和银行等行业，支持安全收集敏感数据。
- 🔒 **数据安全与合规** – 支持自托管，确保数据流完全自主控制，符合 HIPAA、FERPA、GDPR 等法规要求。
- 🔄 **前后端分离** – 仅提供前端 UI 库，需自行构建后端处理数据存储、用户管理和业务逻辑。
- 📋 **灵活许可管理** – 许可可分配给团队开发者，便于直接获取许可证密钥和技术支持。

---

### [获取失败](https://frontendfoc.us/link/178222/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/178222/web)

无法总结：获取内容失败，状态码 403。

---

### [delayed-message-timing/README.md 位于主分支 · WICG/delayed-message-timing · GitHub](https://github.com/WICG/delayed-message-timing/blob/main/README.md)

**原文标题**: [delayed-message-timing/README.md at main · WICG/delayed-message-timing · GitHub](https://github.com/WICG/delayed-message-timing/blob/main/README.md)

该页面是 WICG（Web 平台孵化器社区组）中一个名为“delayed-message-timing”的公共仓库，用于讨论和开发与延迟消息计时相关的 Web 平台功能。

- 📂 这是一个公开的 GitHub 仓库，属于 WICG 组织，专注于“delayed-message-timing”项目。
- 🔔 页面显示通知设置提示，用户需登录才能更改。
- 📊 仓库当前数据：1 个分支，4 个星标，代码、问题、拉取请求等部分可查看。
- ⚠️ 页面加载时遇到错误，提示用户重新加载页面。
- 🔍 导航选项包括代码、问题、拉取请求、操作、项目、安全和洞察等常规 GitHub 仓库部分。

---

### [错误](https://frontendfoc.us/link/178224/web)

**原文标题**: [Error](https://frontendfoc.us/link/178224/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='www.maxdesign.com.au', port=443): Max retries exceeded with url: /articles/two-trees.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [获取失败](https://frontendfoc.us/link/178225/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/178225/web)

无法总结：获取内容失败，状态码 403。

---

### [Let's Encrypt 证书十年历程 - Let's Encrypt](https://letsencrypt.org/2025/12/09/10-years.html)

**原文标题**: [
10 Years of Let's Encrypt Certificates -  Let's Encrypt
](https://letsencrypt.org/2025/12/09/10-years.html)

Let's Encrypt 作为全球最大的证书颁发机构，在成立十周年之际回顾了其通过自动化技术推动 HTTPS 普及的历程，已保护近十亿网站，并将继续致力于降低互联网安全的技术与成本门槛。

- 🌐 2015 年 9 月首次签发公开可信证书，现已成为全球最大证书颁发机构
- 📈 证书签发量从 2016 年单日百万增至 2025 年单日千万级，反映规模化自动化架构的成功
- 🔒 推动全球 HTTPS 加密连接率从 30% 提升至 80%，美国达 95%，显著增强网络安全
- 🏆 获得 Levchin 密码学实践奖等荣誉，学术论文被广泛引用
- 🤝 初期获 Mozilla、EFF、思科等赞助，IdenTrust 的技术合作为项目启动奠定基础
- ⚙️ 持续推出国际化域名、通配符证书等功能，并升级基础设施应对数据增长
- 🌱 未来将继续通过免费证书服务降低安全门槛，推动互联网隐私保护发展

---

### [Orion 1.0 ✨ 超越浏览 | Kagi 博客](https://blog.kagi.com/orion)

**原文标题**: [Orion 1.0 â´ï¸ Browse Beyond | Kagi Blog](https://blog.kagi.com/orion)

经过六年开发，Orion for macOS 1.0 正式发布，标志着这款浏览器正式结束测试阶段，与 iOS 和 iPadOS 版本一同成为成熟产品。它基于 WebKit 引擎构建，注重速度与隐私，无任何遥测数据收集，旨在为用户提供一个快速、可定制且不妥协的浏览体验。作为 Kagi 生态系统的一部分，Orion 倡导“以人为本”的网络理念，并计划扩展至 Linux 和 Windows 平台。

- 🚀 **正式发布**：经过六年开发，Orion for macOS 1.0 正式版发布，结束测试阶段。
- 🌐 **生态扩展**：作为 Kagi 生态系统（“Kagiverse”）的一部分，涵盖搜索、助手、浏览器、翻译和新闻等功能。
- 🛡️ **隐私至上**：坚持零遥测、无广告跟踪技术，隐私保护为默认设置。
- ⚡ **速度与性能**：基于 WebKit 引擎，针对 macOS 和 iOS 深度优化，追求快速启动和流畅体验。
- 🤖 **审慎的 AI 集成**：核心无内置 AI 代码，注重安全，避免不安全的 AI 代理集成。
- 🛠️ **功能丰富**：提供专注模式、链接预览、配置文件隔离等独特功能，兼顾简单使用与高级定制。
- 👥 **社区驱动**：由六人小团队开发，依靠用户反馈和付费订阅者支持，保持独立运营。
- 💰 **可持续模式**：完全免费，通过打赏、订阅和一次性购买等方式获得用户资助。
- 📱 **多平台覆盖**：已推出 macOS、iOS 和 iPadOS 版本，Linux 版处于 Alpha 测试，Windows 版计划于 2026 年底发布。
- 🔮 **未来规划**：路线图包括更深度的定制、性能改进、Orion+ 专属功能及与 Kagi 工具的进一步整合。

---

### [获取失败](https://frontendfoc.us/link/178228/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/178228/web)

无法总结：获取内容失败，状态码 403。

---

### [谷歌年度搜索回顾](https://trends.withgoogle.com/year-in-search/2025/)

**原文标题**: [Google's Year in Search](https://trends.withgoogle.com/year-in-search/2025/)

这份《2025 年度搜索报告》汇总了全球用户在谷歌上的热门搜索趋势，涵盖了新闻、人物、娱乐、体育、生活方式等多个类别，反映了当年的社会关注焦点和流行文化。

- 🌍 **全球趋势**：报告覆盖了全球数十个国家和地区的搜索数据，部分国家/地区的数据暂不可用。
- 🔍 **热门搜索**：年度最热门的搜索词包括 AI 模型“Gemini”、板球赛事“印度对英格兰”、政治人物“查理·柯克”以及“iPhone 17”等。
- 📰 **新闻事件**：重大新闻搜索包括“查理·柯克遇刺”、“伊朗局势”、“美国政府停摆”、“新教皇选出”及自然灾害等。
- 👥 **焦点人物**：搜索量高的公众人物涵盖音乐人（如 Kendrick Lamar）、主持人（Jimmy Kimmel）、政治宗教人物（教皇利奥十四世）及活动家（Greta Thunberg）等。
- 🎬 **娱乐内容**：热门搜索包括演员（Mikey Madison）、电影（《Anora》、《超人》）、电视剧（《鱿鱼游戏 3》）、书籍（Colleen Hoover 作品）及播客。
- ⚽ **体育动态**：热门搜索聚焦运动员（Terence Crawford）、球队（巴黎圣日耳曼）及重大赛事（FIFA 俱乐部世界杯、亚洲杯）。
- 🎮 **生活与游戏**：热门游戏（《GTA 6》、《宝可梦传说 Z-A》）、食谱（热蜂蜜、嫁给我鸡肉）及通过“哼歌搜索”找歌功能受关注。
- 🗺️ **地图探索**：用户常搜索全球知名书店、交通枢纽和植物园，体现了对旅行与文化地标的兴趣。
- 📊 **历史数据**：报告提供了自 2001 年以来的历年搜索趋势回顾，可供对比分析。

---

### [商店 | 互联网档案馆商店 | 满足您内心的档案管理员一切所需](https://store.archive.org)

**原文标题**: [
Shop | Internet Archive Store | Everything for the archivist in you	](https://store.archive.org)

互联网档案馆商店是一个非营利性在线商店，销售品牌商品以支持其数字图书馆服务。

- 🛒 商店销售多种品牌商品，包括限量版棒球衫、帽子、T 恤、手套、袜子、手提袋等
- 🏛️ 所有收益均用于支持非营利性的互联网档案馆数字图书馆
- 💰 商品价格从 15 美元到 80 美元不等，可按价格高低排序浏览
- 🧢 特色商品包括“1 万亿网页”限量版棒球衫和棒球帽
- 🌐 商店与互联网档案馆的博客、开放图书馆等服务相互关联

---

### [获取失败](https://frontendfoc.us/link/178231/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/178231/web)

无法总结：获取内容失败，状态码 520。

---

### [设计可访问性：'lang'属性的作用 - HTMHell](https://www.htmhell.dev/adventcalendar/2025/6/)

**原文标题**: [Accessible by Design: The Role of the 'lang' Attribute - HTMHell](https://www.htmhell.dev/adventcalendar/2025/6/)

本文探讨了 HTML 中`lang`属性的重要性，强调它是确保网站可访问性的关键因素，尤其影响屏幕阅读器、盲文显示器和翻译工具的正确运作。

- 🌐 **`lang`属性定义页面语言**：用于告知浏览器和辅助工具页面使用的语言，如`<html lang="en">`表示英语。
- 📊 **缺失问题普遍存在**：根据 WebAIM 百万报告，缺失语言属性连续七年成为常见可访问性故障之一，影响约 15.8% 的首页。
- 🔊 **屏幕阅读器依赖此属性**：缺失`lang`属性会导致屏幕阅读器错误猜测语言，造成发音混乱，使内容难以理解。
- ⚖️ **WCAG 强制要求**：WCAG 3.1.1 准则将设置页面语言列为 A 级基本要求，缺失则网站被视为不可访问。
- 🔧 **影响多种辅助工具**：包括盲文显示器（影响盲文转换规则）、自动翻译工具（降低翻译准确性）和排版功能（如引号显示与断字处理）。
- 🌍 **多语言页面需局部设置**：页面内不同语言部分应使用`lang`属性标记（如`<span lang="fr">`），以确保辅助工具切换正确语音。
- 🛠️ **各框架设置方法**：React、Vue、Angular 等现代框架需在根模板文件（如`index.html`）中直接设置`<html>`标签的`lang`属性。
- ✅ **简单却关键的可访问性修复**：正确设置`lang`属性是提升网站可访问性最快速、有效的措施之一，确保所有用户平等获取内容。

---

### [CERN 如何利用 TimescaleDB 推动突破性物理研究 | 虎嗅数据](https://www.tigerdata.com/blog/how-cern-powers-ground-breaking-physics-with-timescaledb)

**原文标题**: [How CERN Powers Ground-Breaking Physics with TimescaleDB | Tiger Data](https://www.tigerdata.com/blog/how-cern-powers-ground-breaking-physics-with-timescaledb)

欧洲核子研究中心（CERN）利用 TimescaleDB 替代传统 Oracle 数据库，构建下一代数据归档系统（NGA），以应对大型强子对撞机等实验产生的海量时序数据管理挑战。该系统通过灵活的插件化架构提升性能、降低技术债务，并计划于 2027 年前全面投入生产。

- 🚀 **应对数据挑战**：CERN 原有基于 Oracle 的归档系统存在架构僵化、性能瓶颈等问题，无法高效处理每日数百 GB 的时序数据。
- 🔧 **战略转型**：与西门子合作开发 NGA 系统，采用可插拔后端设计，支持 PostgreSQL 和 TimescaleDB，已部署约 500 个系统。
- 📊 **选型依据**：TimescaleDB 凭借时序数据优化、自动分区、压缩功能及持续聚合能力，在写入吞吐量（超 4 万行/秒）和查询性能上表现突出。
- 💾 **存储优化**：列式压缩技术减少 78%-95% 存储空间，查询压缩数据速度提升 10-40 倍。
- 🎯 **未来规划**：计划 2027 年前全面替代 Oracle，通过 CERN 内部 DBOD 服务实现标准化部署，支撑物理实验的数据可追溯性与实时分析需求。

---

### [网页性能报告剖析 - 网页性能日历](https://calendar.perfplanet.com/2025/the-anatomy-of-a-web-performance-report/)

**原文标题**: [  The Anatomy of a Web Performance Report - Web Performance Calendar](https://calendar.perfplanet.com/2025/the-anatomy-of-a-web-performance-report/)

本文介绍了 Web 性能报告的结构与设计理念，强调一份优秀的报告应通过清晰的层次和叙述，将原始数据转化为易于理解的洞察，从而帮助不同角色的团队成员识别问题、把握机会并采取行动。

- 🖼️ **测试背景**：报告开篇明确测试的 URL、地点、设备和时间戳，为所有性能指标提供解读框架，确保数据具有实际意义。
- 📊 **优化评分**：通过压缩、缓存、CDN 使用等关键优化项目的评分，快速评估网站是否遵循最佳实践，识别可快速改进的环节。
- 📚 **学习资源**：提供精选的文章和案例链接，鼓励团队持续学习，将技术报告与知识分享相结合，促进共同理解。
- 🧪 **核心 Web 指标实验数据**：在受控环境中测量 LCP、CLS 和 TBT，用于即时发现回归问题，充当早期预警系统。
- 🌍 **核心 Web 指标 CrUX 现场数据**：展示真实用户在不同网络、设备和地理条件下的性能体验，反映网站的实际表现和趋势变化。
- 🤖 **AI 洞察**：基于所有数据生成易于理解的执行摘要，明确指出改进点、回归问题及其影响，帮助团队快速决策。
- 🏆 **Lighthouse 评分**：从可访问性、最佳实践和 SEO 等维度提供整体质量评估，揭示与性能相关的交叉问题。
- ⏱️ **性能结果时间线**：列出 TTFB、首次渲染、FCP 等关键加载里程碑，帮助定位延迟发生的具体阶段。
- 📦 **内容资源分布**：分析 JavaScript、图片、字体等资源的字节占比，揭示可能导致性能问题的根本原因。
- 🔗 **完整测试链接**：在保持报告简洁性的同时，提供深入查看瀑布图、日志等详细数据的入口，满足深度排查需求。

---

### [我未能用 Claude 重现 1996 年《空中大灌篮》网站 | j0nah.com](https://j0nah.com/i-failed-to-recreate-the-1996-space-jam-website-with-claude/)

**原文标题**: [I failed to recreate the 1996 Space Jam Website with Claude | j0nah.com](https://j0nah.com/i-failed-to-recreate-the-1996-space-jam-website-with-claude/)

作者尝试使用 Claude AI 仅凭截图和素材文件复刻 1996 年《太空大灌篮》官网，但最终失败。整个过程揭示了 Claude 在视觉空间精确测量和自省修正方面的核心局限。

- 🎯 **任务设定**：提供官网截图和素材，要求 Claude 精确复刻采用绝对定位的静态页面
- 🤖 **盲目自信**：Claude 初期声称完美复刻，实际布局存在明显偏差，且自我评估与输出结果脱节
- 📏 **测量缺陷**：Claude 承认无法获取精确像素坐标，仅能进行视觉估算，导致定位误差
- 🛠️ **工具失效**：作者添加网格覆盖、坐标参考、分屏对比等辅助工具后，Claude 仍陷入自我验证循环
- 🔍 **视觉局限**：推测 Claude 的视觉编码器将图像分块处理，丢失细节精度，导致语义理解与几何执行不匹配
- 📈 **错误固化**：每次迭代调整仅微调错误布局，未能突破初始错误的空间认知框架
- 🧩 **分区尝试**：将截图分割为六个区域分别分析，仍无法改善定位精度
- 🔬 **放大实验**：提供 200% 放大截图试图增强细节识别，但 Claude 未能正确处理比例换算
- 🧠 **认知矛盾**：能够准确描述布局概念（如“行星环绕排列”），却无法转化为精确的 CSS 坐标
- 🏁 **未解难题**：最终承认失败，认为这个 28 年前的网页设计意外成为 AI 空间推理能力的基准测试

作者总结指出，Claude 在评估自身输出时存在过度自信倾向，无法区分自生成内容与外部事实，导致错误在迭代中不断固化而非纠正。

---

### [NoLoJS：利用 HTML 与 CSS 减轻 JavaScript 负担 - 网页性能日历](https://calendar.perfplanet.com/2025/nolojs-reducing-js-workload-html-css/)

**原文标题**: [  NoLoJS: Reducing the JS Workload with HTML and CSS - Web Performance Calendar](https://calendar.perfplanet.com/2025/nolojs-reducing-js-workload-html-css/)

本文介绍了如何利用现代 HTML 和 CSS 功能替代传统的 JavaScript 实现，以减少 JavaScript 负担，提升网页性能与用户体验。

- 📜 **使用 details 和 summary 元素实现手风琴效果**：无需 JS 即可创建可展开/收缩的内容面板，支持单个或多个面板控制，并可通过 CSS 自定义样式与动画。
- 📏 **利用 field-sizing 属性实现表单元素自适应**：通过一行 CSS 让 textarea、input 或 select 元素根据内容自动调整尺寸，无需 JS 监听输入。
- 🔍 **结合 input 和 datalist 实现自动过滤下拉框**：输入时自动筛选选项，适用于搜索、筛选等场景，部分输入类型在浏览器中有限制。
- 🪟 **使用 popover 属性创建模态框/弹出层**：通过 HTML 属性实现弹窗，支持自动关闭或手动控制，并可添加遮罩层和关闭按钮。
- 🧭 **基于 popover 实现侧边导航菜单**：将内容隐藏在屏幕外，点击时滑入，可通过 CSS 调整位置和动画，支持手动或自动关闭。
- 🛝 **通过 scroll-behavior 属性启用平滑滚动**：只需一行 CSS 即可实现页面内的平滑滚动，需考虑用户偏好减少动画的需求。
- 📌 **使用 position: sticky 实现粘性定位**：让元素在滚动时固定于容器边缘，适用于表头、侧边栏等，无需 JS 计算滚动位置。

---

### [滚蛋联系页面 - Nic Chan](https://www.nicchan.me/blog/the-f-off-contact-page/)

**原文标题**: [The f*** off contact page - Nic Chan](https://www.nicchan.me/blog/the-f-off-contact-page/)

本文作者回顾了一次不理想的网页设计项目经历，客户执意采用一种阻碍用户联系的“滚蛋式联系页面”，作者虽不认同却未能成功劝阻，最终项目虽完成但令其感到失望，并反思了导致此情况的原因与教训。

- 🚫 “滚蛋式联系页面”是大公司为减少咨询量而设计的障碍性页面，不适合以服务为导向的客户
- 🎨 客户仅从美观而非用户体验角度选择设计，偏离了项目目标
- 🔥 设计团队因忙于处理其他更紧急的修改要求，未能坚持反对此不良设计
- 😔 项目虽按时完成且客户满意，但作者因未达到自身质量标准而感到失望
- 💸 项目初期提供折扣报价，导致客户低估团队的专业价值，视其为执行工具而非合作伙伴
- 📚 作者反思应更好地教育客户理解设计流程的重要性，避免跳过关键规划步骤
- ✍️ 通过博客公开表达设计价值观，以吸引理念一致的客户，并明确拒绝不合适的合作对象

---

### [使用 Invoker Commands API 控制对话框和弹出层 - HTMHell](https://www.htmhell.dev/adventcalendar/2025/7/)

**原文标题**: [Controlling dialogs and popovers with the Invoker Commands API - HTMHell](https://www.htmhell.dev/adventcalendar/2025/7/)

Invoker Commands API 为 `<button>` 元素新增了 `command` 和 `commandfor` 属性，允许开发者无需编写 JavaScript 即可控制对话框和弹出层的显示、隐藏等交互行为，简化了网页交互元素的实现。

- 🚀 **无需 JavaScript**：通过新增的 `command` 和 `commandfor` 属性，可直接控制对话框和弹出层，减少代码量。
- 🎭 **对话框与弹出层区别**：对话框通常包含需用户执行的操作，必须显式关闭；弹出层用于短暂信息展示，可点击外部轻量关闭。
- 🔧 **支持的命令**：包括 `show-modal`、`close`、`request-close` 用于对话框，以及 `show-popover`、`hide-popover`、`toggle-popover` 用于弹出层。
- ✨ **自定义命令**：支持以 `--` 前缀创建自定义命令，扩展 API 功能，例如控制 `<details>` 元素的开关。
- 🌐 **浏览器支持**：截至 2025 年底，已在 Chrome、Edge、Opera、Firefox 等现代浏览器中实现，并提供 polyfill 以兼容旧版浏览器。
- 🔮 **未来展望**：计划增加更多内置命令，如控制 `<details>` 元素、日期选择器及媒体播放功能，并鼓励用户提交新命令建议。

---

### [那次我尝试向五岁侄女解释 HTML 和 CSS | CSS-Tricks](https://css-tricks.com/that-time-i-tried-explaining-html-and-css-to-my-5-year-old-niece/)

**原文标题**: [That Time I Tried Explaining HTML and CSS to My 5-Year Old Niece | CSS-Tricks](https://css-tricks.com/that-time-i-tried-explaining-html-and-css-to-my-5-year-old-niece/)

作者通过向五岁侄女解释 HTML 和 CSS 的过程，重新发现了网页开发基础工作的魅力与意义，并反思了教学与学习的重要性。

- 🧱 用“盖房子”和“乐高积木”的比喻向孩子解释 HTML 是网页的结构框架，CSS 则是装饰和美化
- 👧 孩子的直观视角（将空白网页看作“房子”）帮助作者重新理解 HTML 与 CSS 的核心关系：HTML 定义内容，CSS 控制外观
- 🎨 通过实际演示简单的 CSS 样式（宽度、高度、边框和颜色），让孩子亲眼看到代码如何“让房子变漂亮”
- 💡 教学过程中作者意识到自己常忽略基础工作的魅力，被孩子的“A-ha!”时刻提醒应放慢脚步欣赏每一行代码
- 🏗️ 解释经历让 HTML 从代码变成“建筑材料”，CSS 从样式表变成“塑造形状的黏土”
- 🧠 这次经历体现了费曼学习法的精髓：通过教学来检验和深化自己的理解
- 🌈 作者反思成人常陷入工具和最佳实践的争论，而孩子却能直击本质，找回工作的初心与乐趣

---

### [跨浏览器非阻塞画布图像渲染 - 网页性能日历](https://calendar.perfplanet.com/2025/non-blocking-image-canvas/)

**原文标题**: [  Non-blocking cross-browser image rendering on the canvas - Web Performance Calendar](https://calendar.perfplanet.com/2025/non-blocking-image-canvas/)

本文探讨了在 Canvas 中实现跨浏览器非阻塞图像渲染的挑战与解决方案，旨在解决大图像解码时主线程阻塞的问题，以提升用户体验。

- 🎨 **Canvas 渲染的挑战**：处理大图像时，保持主线程响应性是一大难题，不同浏览器对图像解码的支持不一致，导致跨浏览器兼容性复杂。
- 🔍 **多种解码方法尝试**：文章测试了六种图像加载与解码方法，包括标准加载、使用`decode()`方法、结合`OffscreenCanvas`和`createImageBitmap`等，但每种方法在不同浏览器中均有阻塞问题。
- 🌐 **跨浏览器最终方案**：通过结合针对 Chromium 和非 Chromium 浏览器的不同方法，成功实现了在 Firefox、Chrome 和 Safari 中非阻塞图像解码，确保 UI 流畅。
- ⚡ **性能提升显著**：优化后，在处理大图像（如 7MB 的精灵图）时，UI 卡顿消失，视频预览等交互体验得到明显改善，尤其适用于媒体管理平台等需要高性能渲染的场景。
- 🔮 **浏览器兼容性展望**：目前仅 Firefox 完全遵循规范，希望 Chrome 和 Safari 未来能统一实现，以简化开发并进一步提升跨浏览器性能。

---

### [浏览器评分](https://browserscore.dev/)

**原文标题**: [Browser Score](https://browserscore.dev/)

该测试评估浏览器对网页平台功能的识别情况，而非验证其正确实现。

- 🔍 测试仅检查浏览器是否识别网页平台功能
- ⚠️ 注意：不涉及功能实现正确性的验证
- 📊 当前识别率显示为 0%（0/0 功能）
- ⏱️ 测试完成时间为 0 毫秒

---

### [宏观镜 - AI 代码审查与状态更新](https://macroscope.com/?utm_medium=newsletter&utm_source=frontendfocus&utm_content=primarysponsor)

**原文标题**: [Macroscope - AI Code Review & Status Updates](https://macroscope.com/?utm_medium=newsletter&utm_source=frontendfocus&utm_content=primarysponsor)

Macroscope 是一款 AI 驱动的工程洞察平台，通过分析代码库自动生成提交摘要、进行代码审查、追踪项目进展，并提供团队生产力数据，旨在帮助工程领导者获得清晰的项目可见性，同时节省工程师的汇报时间。

- 🚀 **自动生成摘要**：自动总结提交内容和拉取请求，无需手动编写描述
- 🐛 **智能代码审查**：通过分析抽象语法树构建知识图谱，精准检测错误并减少误报
- 📊 **项目可视化**：实时展示工程时间分配、项目变化和团队活动数据
- 💬 **集成问答系统**：支持在 Slack 中提问，基于代码库和 Git 日志提供准确答案
- 🔗 **无缝集成**：快速连接 GitHub、Jira/Linear 和 Slack 等工具（安装仅需 10-30 秒）
- 🛡️ **企业级安全**：通过 SOC 2 Type II 认证，数据加密存储传输，员工无法访问客户源代码
- 💰 **灵活定价**：提供团队版（每位开发者 30 美元/月）、企业定制方案和开源项目免费计划
- ⭐ **客户认可**：多位科技公司高管称赞其提升团队效率、改善代码审查质量和提供深度洞察的能力

---

### [GitHub - cloudflare/telescope：跨浏览器网页性能测试代理](https://github.com/cloudflare/telescope)

**原文标题**: [GitHub - cloudflare/telescope: Cross-browser web performance testing agent](https://github.com/cloudflare/telescope)

Telescope 是一个由 Cloudflare 开发的开源跨浏览器网页性能测试工具，用于收集和分析网页加载过程中的各项性能数据，支持多种浏览器和自定义测试参数。

- 🌐 **跨浏览器测试代理**：支持 Chrome、Firefox、Safari 和 Edge 等多种浏览器，用于诊断和评估网页性能。
- 📊 **数据收集全面**：测试过程中自动收集控制台输出、视频记录、性能指标、HAR 文件、资源计时数据和页面截图等。
- ⚙️ **灵活的参数配置**：提供丰富的命令行选项，如自定义请求头、Cookie、网络节流、禁用 JavaScript 等，以适应不同的测试场景。
- 📈 **HTML 报告生成**：支持生成并自动打开详细的 HTML 测试报告，便于结果可视化分析。
- 🔧 **程序化调用支持**：可通过 Node.js 脚本直接调用，方便集成到自动化测试流程中。
- 📦 **依赖与环境要求**：基于 Playwright 控制浏览器，需要安装 ffmpeg 处理视频，并支持通过 npm 安装和管理依赖。

---

### [GitHub - filipsobol/sonda：适用于JavaScript和CSS的通用可视化工具与分析器。兼容多数打包工具和框架。](https://github.com/filipsobol/sonda)

**原文标题**: [GitHub - filipsobol/sonda: Universal visualizer and analyzer for JavaScript and CSS. Compatible with most bundlers and frameworks](https://github.com/filipsobol/sonda)

Sonda 是一款通用的 JavaScript 和 CSS 可视化分析工具，兼容主流打包工具和框架，通过分析源码映射提供精确的打包报告。

- 🛠️ **通用分析工具** – 支持 Vite、Rollup、webpack 等多种打包工具，以及 Next.js、Nuxt、Astro 等框架
- 📊 **精准可视化报告** – 基于源码映射分析，展示 Tree Shaking 和压缩后的模块体积，生成交互式 HTML 报告
- 🌐 **在线体验** – 提供官方文档和在线演示，便于快速了解和使用
- 📦 **开源项目** – 采用 MIT 许可证，拥有活跃的社区维护和版本发布
- ⭐ **受欢迎程度** – 在 GitHub 上获得大量关注，被众多项目所使用

---

### [索达报告](https://sonda.dev/demo)

**原文标题**: [Sonda report](https://sonda.dev/demo)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统通过分析医学影像提升疾病识别准确率
- 💊 基于算法的个性化治疗方案推荐助力精准医疗发展
- ⚡ 智能流程管理工具优化医院资源分配与患者就诊体验
- 🔬 基因组学与 AI 结合加速新药研发和病理机制研究
- ⚖️ 数据隐私保护与算法透明度成为实际应用中的关键议题

---

### [React 代理抓取工具](https://www.react-grab.com/blog/agent)

**原文标题**: [React Grab for Agents](https://www.react-grab.com/blog/agent)

React Grab 现已升级为可直接与 AI 编程代理交互，允许用户在浏览器中直接选择 UI 元素并发送指令，代理将根据精确的代码上下文自动编辑文件，无需切换应用或手动复制粘贴，从而显著提升前端开发效率。

- 🚀 **核心升级**：从仅复制代码上下文，变为可直接与 AI 代理对话并实时编辑代码，全程在浏览器内完成。
- 🆓 **保持不变**：工具仍免费开源，兼容 Claude Code、Cursor、OpenCode 等多种 AI 编程工具，保留“点击元素获取 React 上下文与文件路径”的核心功能。
- 🖱️ **新功能亮点**：支持从页面直接启动代理、同时运行多个 UI 任务、代码修改后自动刷新，操作流程无缝衔接。
- ⚡ **效率提升**：通过提供精确的组件堆栈与代码位置，使代理平均任务速度提升约 66%，减少文件搜索与工具调用时间。
- 🔧 **简易设置**：通过 CLI 一键安装，或按框架添加脚本即可快速集成，支持自定义代理适配器。
- 🔮 **未来展望**：将推出专为 UI 工作流设计的 AI 代理 Ami，与 React Grab 深度结合，实现更精准的代码修改与设计系统理解。

---

### [GitHub - aidenybai/react-scan：扫描React性能问题，消除应用中的缓慢渲染](https://github.com/aidenybai/react-scan)

**原文标题**: [GitHub - aidenybai/react-scan: Scan for React performance issues and eliminate slow renders in your app](https://github.com/aidenybai/react-scan)

React Scan 是一款用于自动检测 React 应用性能问题的工具，无需代码更改即可快速识别和优化慢渲染组件。

- 🔍 **自动检测性能问题**：无需代码修改，直接集成即可扫描 React 应用中的渲染性能问题。
- 🎯 **直观可视化工具**：通过工具栏和渲染轮廓线高亮显示需要优化的组件，避免复杂火焰图分析。
- ⚡ **快速上手**：支持 CLI 命令（如 `npx react-scan localhost:3000`）和多种安装方式（npm、浏览器扩展等）。
- 📊 **智能分析功能**：提供组件重渲染原因分析、性能剖析器、交互延迟检测，并支持 LLM 提示优化建议。
- 🛠️ **灵活配置选项**：支持自定义扫描行为、动画速度、工具栏显示等，满足不同开发环境需求。
- 🌐 **生产环境监控**：提供 React Scan Monitoring 服务，帮助持续追踪生产环境中的性能问题。
- 📄 **开源与社区支持**：基于 MIT 许可证开源，拥有活跃的 Discord 社区和详细的贡献指南。

---

### [GitHub - pengzhanbo/caniuse-embed: 在你的网站中嵌入 CanIUse 兼容性表格](https://github.com/pengzhanbo/caniuse-embed)

**原文标题**: [GitHub - pengzhanbo/caniuse-embed: Embed the CanIUse compatibility table in your site](https://github.com/pengzhanbo/caniuse-embed)

这是一个用于在网站中嵌入 CanIUse 兼容性表格的开源工具，通过 Astro 框架和 Vercel 平台实现高效、轻量的数据展示，并利用增量静态再生保持数据更新。

- 🚀 **项目目的**：在网站中嵌入 CanIUse 的浏览器兼容性数据表格，提供可配置、可靠且完全响应的展示。
- 📦 **技术方案**：使用 Astro 进行服务端渲染，为每个功能生成独立的静态页面，大幅减少数据加载量（从 18MB 降至 20KB 以内）。
- ⚡ **性能优化**：通过 Vercel 的 ISR（增量静态再生）能力，每 7 天自动重新生成并缓存页面，确保数据新鲜度且无需重新部署。
- 📄 **使用方法**：在文档中引入指定 JavaScript 文件，并通过 HTML 片段配置要展示的功能和参数。
- 🛠️ **开发背景**：为解决原有嵌入方案加载数据过大、影响页面速度的问题而重新开发。
- 📚 **相关资源**：项目文档提供了详细的使用说明，代码仓库包含完整的源代码和配置文件。
- 📄 **开源许可**：项目基于 MIT 许可证开源，允许自由使用和修改。

---

### [我能否使用... HTML5、CSS3 等的支持表格](https://caniuse.com/)

**原文标题**: [Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/)

该网站提供网页技术兼容性查询服务，包含最新功能更新、浏览器支持数据及实用工具，帮助开发者测试和优化网站跨平台兼容性。

- 🏠 网站核心功能为查询 CSS、JavaScript 等网页技术在不同浏览器和设备上的兼容性
- 🔍 提供最新功能索引，如 CSS if() 函数、WebAssembly 多值支持等，并展示热门搜索功能
- 📊 支持导入 Google Analytics 数据，查看功能在自身网站访客中的实际使用情况
- 🤝 与 BrowserStack 合作，支持在 2000+ 真实浏览器和设备上测试网站兼容性
- 🛠️ 提供第三方工具集成，包括嵌入支持表格、命令行工具和 CSS 检查工具
- 📈 展示主流浏览器版本的功能支持评分，如 Chrome 143 得 438 分
- 🔗 推荐相关兼容性查询站点，涵盖电子邮件 HTML/CSS 支持、无障碍功能及 WebView 能力文档

---

### [GitHub - mdn/browser-compat-data：MDN 上展示的 Web 技术浏览器兼容性数据](https://github.com/mdn/browser-compat-data)

**原文标题**: [GitHub - mdn/browser-compat-data: Browser compatibility data for Web technologies as displayed on MDN](https://github.com/mdn/browser-compat-data)

MDN 浏览器兼容性数据（BCD）项目提供 Web 技术（如 Web API、JavaScript 功能、CSS 属性等）的机器可读浏览器兼容性数据，旨在帮助开发者更轻松地创建跨浏览器兼容的网站，并被 MDN Web Docs、CanIUse、Visual Studio Code 等多个平台使用。

- 🗃️ **项目内容**：包含超过 15,000 个 Web 技术特性的兼容性数据，涵盖 API、CSS、HTML、JavaScript、SVG 等多个领域。
- 📦 **安装与使用**：支持通过 npm 或 CDN 导入，提供 Node.js、Deno 和浏览器环境下的多种导入方式。
- 🛠️ **数据结构**：以树形对象组织数据，包含详细的浏览器和特性支持信息，并遵循严格的模式定义。
- 🔄 **版本管理**：遵循语义化版本控制，但底层兼容性数据可能频繁更新以反映浏览器和标准的变化。
- 🤝 **贡献与协作**：鼓励社区贡献，提供详细的贡献指南，并通过 Matrix 聊天室进行交流。
- 🌐 **应用广泛**：被许多工具和平台使用，如 Firefox 开发者工具、Visual Studio Code、TypeScript 等，以提供兼容性检查和文档支持。
- ⚠️ **限制说明**：不跟踪 UI 变更、无关特性或框架自定义功能，也不涉及屏幕阅读器兼容性数据。
- 🐛 **问题反馈**：欢迎提交错误报告或新特性建议，以帮助改进数据准确性。

---

### [NativewindUI](https://nativewindui.com/)

**原文标题**: [NativewindUI](https://nativewindui.com/)

该产品由 Nativewind 和 React Native Reusables 的开发者打造，提供结合 Tailwind CSS 的本地化 UI 组件库，旨在让移动应用开发兼具原生体验与高效开发速度。

- 🛠️ 提供 30 多个美观的组件和模板，专为移动设备设计，具有原生外观和手感
- ⚙️ 基于 React Native、Expo 和 Nativewind 技术构建，确保开发兼容性和性能
- 🚀 已有超过 3,000 名开发者使用，实现原生质量与网页开发速度的结合
- 📦 包含丰富的组件和模板资源，支持多样化应用开发需求
- 💼 展示多个合作案例，如 Limitless、coblocks 等，体现实际应用效果

---

### [非 HTML 内容](https://frontendfoc.us/open/721/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/721/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

